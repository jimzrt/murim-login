# Checkpoint Review — 465–469

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

# Chapters 465–469

## Plot

Jin Taekyung defeats the Dongting Fisherman inside his underwater refuge after surviving the fisherman’s Heavenly Silkworm Thread, Inner-Family Heavy Hand, and other attacks. He seals the fisherman’s acupoints, carries him through the collapsing refuge, and escapes underwater with the Water Rescue Worker Title’s gills and webbed feet. The fisherman is held alive for interrogation about Dark Heaven.

A severe storm prevents the group’s return across Dongting Lake. Despite Taekyung’s seals, the Dongting Fisherman briefly moves independently, grabs Taekyung, and warns him to run. Jeok Cheongang destroys a waterspout with Flame-Extinguishing Divine Fist, allowing Mu Song’s vessel to advance, while Jeok, Mungyeong, and Zhuge Feng travel toward Taekyung’s location. Hyeongong remains behind.

A cliff collapses after a tremendous roar, revealing a gigantic Lv. ??? Mutated Water God Dragon. Its monster’s Fear overwhelms Hyuk Mujin and Gung Gibang, but Taekyung and Cheongpung resist it. Taekyung’s iron spear cannot pierce its scales, and he concludes that the creature may have caused the Dongting Fisherman’s earlier mental disturbance.

## Continuity

- The Dongting Fisherman is severely injured, immobilized by Taekyung’s Paralysis, Mute, and Sleep Acupoint seals, and held alive for interrogation about Dark Heaven.
- The fisherman accepted Dark Heaven’s hand and is implicated in massacring innocent commoners and children.
- Taekyung suffered only a minor internal injury from Inner-Family Heavy Hand and remains combat-capable, but his iron spear cannot penetrate the Mutated Water God Dragon’s scales.
- The fisherman’s involuntary movement, terrified warning, and apparent mental disturbance remain unexplained; the creature’s Fear is a possible cause.
- The fisherman’s underwater secret refuge collapsed. Earlier deliberate damage throughout the refuge and its connection to the fisherman or another intruder remain unresolved.
- An unprecedented storm disrupted travel on Dongting Lake. Mu Song’s best sailors from Water Dragon Stronghold are operating the vessel, and Jeok Cheongang opened a route by destroying a waterspout.
- Jeok Cheongang, Mungyeong, and Zhuge Feng are moving toward Taekyung; Hyeongong remains at the original location.
- The giant creature is known locally as Dongting Lake’s Two-Horned Beast or Water God Dragon. Its origin, relationship to the modern Sea Serpent, and purpose are unknown.
- Honglan survived the Dongting Lake disaster and is recovering. Ju Wongong remains unconscious under guard after passing the most dangerous stage of his injuries.
- Jin Wikyung is cooperating with Taekyung’s investigation as an inspector for the new Murim Alliance.
- The shared symbols between the Arch Lich’s magic circle and Dark Heaven’s formations remain unexplained.
- The Sea Serpent Society and three Yangtze River Channel League strongholds, including Donghu Stronghold, were destroyed with more than a thousand casualties. The perpetrators, motive, and lack of Moving Formation traces remain unknown.
- The captured Three Fiends is a former-generation great fiend and Supreme Peak Dark Heaven subordinate being transported alive for investigation, including possible codes or markings.
- Jeok Cheongang carries a sharp, armor-hard object whose nature remains unknown.

## Translation Decisions

- Render 천잠사 as “Heavenly Silkworm Thread,” 운철 as “meteorite iron,” 초인 as “superhuman,” 극쾌 as “extreme swiftness,” 노괴 as “old monster,” and 신병이기 as “divine weapon.”
- Render 수상 구조대원의 물갈퀴 as “Water Rescue Worker’s Webbed Feet” and 수상 구조대원의 아가미 as “Water Rescue Worker’s Gills.”
- Render 변이된 수신룡 as “Mutated Water God Dragon,” 이각수 as “Two-Horned Beast,” 수신룡 as “Water God Dragon,” 시 서펜트 as “Sea Serpent,” and 피어 as “Fear.”
- Continue rendering 오기조원 as “Five Qi Returning to Origin,” 노화순청 as “Furnace Fire Pure Blue,” 반로환동 as “Returned to Youth,” 복자 as “diviner,” 일위도강 as “Single Reed Crossing the River,” and 장제자 as “Senior Disciple.”
- Render 점혈 as “Pressure-Point Strike,” 마혈 as “Paralysis Acupoint,” 아혈 as “Mute Acupoint,” and 수혈 as “Sleep Acupoint.”
- Preserve Taekyung’s dry humor, blunt profanity, and sexual innuendo; render 씨부럴 as “sibu-leol” in direct abuse.
- Preserve the Dongting Fisherman’s emotionless, inhuman presentation and violent combat voice, along with Cheongpung’s deferential, innocent speech.

## Durable state

{
  "active_continuity": [
    "The Dongting Fisherman remains severely injured, immobilized by Taekyung's seals, and held alive for interrogation about Dark Heaven.",
    "Taekyung believes the Dongting Fisherman encountered the Mutated Water God Dragon before the group and that its Fear caused his apparent mental disturbance.",
    "Taekyung suffered only a minor internal injury from the Dongting Fisherman's Inner-Family Heavy Hand and remains capable of fighting, but his iron spear cannot pierce the creature's scales.",
    "Honglan survived the Dongting Lake disaster and is recovering; Ju Wongong remains unconscious under guard after passing the most dangerous stage of his injuries.",
    "Jin Wikyung is acting as an inspector for the new Murim Alliance and is cooperating with Taekyung's investigation.",
    "The shared symbols between the Arch Lich's magic circle and Dark Heaven's formations remain unexplained.",
    "The Sea Serpent Society and three Yangtze River Channel League strongholds, including Donghu Stronghold, were destroyed with more than a thousand casualties, while the perpetrators' wider plans remain unknown.",
    "The captured Three Fiends is a former-generation great fiend and Supreme Peak Dark Heaven subordinate whom Taekyung is transporting alive to investigate possible codes or markings.",
    "An unprecedented storm over Dongting Lake prevented ordinary passage; Mu Song brought his best sailors from Water Dragon Stronghold, and Jeok Cheongang opened a route through the storm by destroying a waterspout.",
    "Jeok Cheongang, Mungyeong, and Zhuge Feng are moving toward Taekyung's location, while Hyeongong remains behind.",
    "A giant Mutated Water God Dragon, also known locally as Dongting Lake's Two-Horned Beast or Water God Dragon, has emerged and possesses a monster's Fear.",
    "The creature's Fear overwhelmed Hyuk Mujin and Gung Gibang, while Taekyung and Cheongpung resisted it."
  ],
  "continuity_sources": [
    469,
    468
  ],
  "open_questions": [
    "What is the Dongting Fisherman's exact role within Dark Heaven, what information will he reveal, what caused his involuntary movement and terrified warning, and was his prior mental disturbance caused by the creature's Fear?",
    "What caused the earlier deliberate destruction inside the refuge, and how was it connected to the Dongting Fisherman or another intruder?",
    "What are the origin and purpose of the symbols shared by the Arch Lich's magic circle and Dark Heaven's formations?",
    "Who destroyed Donghu Stronghold and the related Yangtze River Channel League strongholds, why was no Moving Formation trace left, and was the destruction a diversion?",
    "What is the sharp, armor-hard object carried by Jeok Cheongang, and what are the true origin, relationship to the known Sea Serpent, and purpose of the Mutated Water God Dragon?"
  ],
  "safe_through": 469,
  "temporary_decisions": [
    "Render 천잠사 as Heavenly Silkworm Thread, 운철 as meteorite iron, 초인 as superhuman, and 극쾌 as extreme swiftness.",
    "Render 노괴 as old monster, 신병이기 as divine weapon, 수상 구조대원의 물갈퀴 as Water Rescue Worker's Webbed Feet, and 수상 구조대원의 아가미 as Water Rescue Worker's Gills.",
    "Preserve Taekyung's dry contemporary humor and blunt profanity, render 씨부럴 as sibu-leol in direct abuse, and preserve the Dongting Fisherman's emotionless, inhuman presentation and violent combat voice.",
    "Continue rendering 오기조원 as Five Qi Returning to Origin, 노화순청 as Furnace Fire Pure Blue, 반로환동 as Returned to Youth, 복자 as diviner, 일위도강 as Single Reed Crossing the River, and 장제자 as Senior Disciple.",
    "Render 변이된 수신룡 as Mutated Water God Dragon, 이각수 as Two-Horned Beast, 수신룡 as Water God Dragon, 시 서펜트 as Sea Serpent, and 피어 as Fear."
  ],
  "version": 1
}

## Reading copies

## Chapter artifact 465

# Chapter 465

*Boom!*

The direction of White Flame’s spearhead was knocked aside by the force of the impact.

A streak of light that had flown in along a truly bizarre trajectory writhed like a living creature before raining down over my head.

*Shh-shh-shh-shing!*

A downpour of Force.

Faced with that destructive power, which illuminated the dark cave in an instant, I smoothly twisted my body.

*Swish. Boom-boom-boom!*

My shoulder, neck, waist, and chest…

The streak of light swept within a hair’s breadth of the vital acupoints throughout my body before piercing and smashing through the solid cave floor.

An attack that would have killed me instantly if I had reacted even a moment later.

But the Dongting Fisherman’s attack failed to touch even a single hair on my body, and that moment of danger turned into an opportunity.

Just like now.

*Whoom!*

White Flame’s spearhead, shaken by the impact a moment earlier, snapped sharply through the air and went for the Dongting Fisherman’s throat.

His grayish-white eyes widened as he turned his body, and a snow-white streak of light hurriedly flew across to block the spearhead.

But…

*That won’t be enough.*

If the Dongting Fisherman was an old monster who had accumulated massive amounts of internal energy over a long lifetime, then I was a monster who had surpassed those years through System rewards and countless battles fought on the edge of death.

Even if our internal energy was equal, my body housed the strength of a giant that had surpassed the limits of humanity.

*Boom!*

The instant the blue-white flames touched the streak of light, a thunderous boom rang out like the sky itself had split apart, and the Dongting Fisherman’s body was sent flying.

The small old man’s body smashed through the solid rock before crashing into the wall. At the same time, the cave shook, and huge stalactites came tumbling down.

I glared at the grayish-white eyes visible beyond the falling debris and spoke slowly and clearly.

“Get up. Quit the pathetic act.”

*Crack-crack-crack.*

Only a moment earlier, his limbs had hung limp as though he were dead. Now they moved with vigor.

The Dongting Fisherman rose from the hollow his impact had left in the wall and cracked his neck from side to side.

With the sound of bones grinding against one another, he began walking. A long fishing rod had somehow appeared in his wrinkled hand.

*The black-wood fishing rod.*

It could not compare to Ten-Thousand-Year Cold Iron, but it was the Dongting Fisherman’s signature weapon, said to have a strength comparable to meteorite iron while being extraordinarily flexible.

Despite being partially damaged, it was still one zhang long. A fishing line and hook with a faint sheen hung from its tip.

*That’s…*

I had never seen it before, but I had heard of it.

The Heavenly Silkworm Thread, a rare treasure said to stand shoulder to shoulder with the Sichuan Tang Clan’s Soul-Severing Thread.

It was strange enough that a mere silkworm cocoon was treated as a spiritual treasure, as though even the grand name Heavenly Silkworm were insufficient. But that was not as surprising as the fact that its thread was so tough and sharp that even steel could not cut it.

The fishing line attached to the black-wood fishing rod was that very Heavenly Silkworm Thread.

*I’ll have to be careful.*

There was nothing to lose by being cautious. Even if Fire Dragon Armor was a divine weapon, it was not an invincible suit of armor capable of blocking everything.

I opened my mouth while staring at the Dongting Fisherman, who had stopped three zhang away.

“You have two choices. The first is to die by my hand right here. The second is to confess every single thing you know without leaving anything out, then atone to the victims. Which one do you want?”

“……”

Instead of answering, his hazy grayish-white eyes stared blankly at me.

There was no emotion in that gaze. For a moment, a chill rose along my spine at the sight of eyes that were impossible to believe belonged to a human being.

*…What is this feeling?*

Everyone had emotions.

But the Dongting Fisherman was different. He was clearly breathing, and I could sense life within him, yet he seemed like an object with nothing inside.

*What the hell is this…?*

I did not have time to think about it for long. The next moment, I flinched and tightened my grip on the spear shaft.

A nameless fish had suddenly moved only a few steps away.

The fish, its bones exposed and the flesh around its belly torn away, thrashed several times before stopping completely.

Clear teeth marks from where someone had bitten into it remained on its body.

*No way.*

I looked at the Dongting Fisherman and narrowed my eyes.

Red blood and glinting scales clung to the wrinkles around his mouth.

Only then did I realize what the sound I had heard on the way here was—and what he had been doing until just moments ago.

*He was tearing it apart and eating it raw. A live fish, at that.*

What kind of crazy old man was this?

Suddenly, a classic fantasy movie that had been played constantly on the cable movie channels flashed through my mind.

Now that I thought about it, he did look a little like the monster from that movie. His small frame, his hunched back, even his sparse hair.

I clicked my tongue softly and spoke to the Dongting Fisherman.

“This changes the genre… The divine treasure you people are looking for isn’t a ring, is it?”

“……”

“Fine, don’t answer. I was planning to ask you while plucking out the few hairs you have left, one by one.”

“Guh.”

“Oh, shit. What was that?”

I opened my eyes wide at the Dongting Fisherman’s sudden reaction.

I had just blurted out whatever came to mind. Had I somehow hit a balding man’s sore spot?

But I had no way of knowing whether the Dongting Fisherman had reacted to the threat to his hair roots or for some other reason.

Before I could say anything else, his old grayish-white eyes widened, and an enormous roar burst from his throat.

“GRAAAAAH!”

*Rumble-rumble-rumble!*

This was not the cry of the old man who shouted from the hill behind the neighborhood every morning at dawn.

The roar, infused with powerful internal energy, traveled through the air and slammed into the cavern. Everything around us shook and burst apart—the floor, the walls, everything.

And before the shock wave could even begin to spread, the Dongting Fisherman’s body shot toward me, leaving behind a pale afterimage.

*Whoooooosh!*

His eyes had turned pitch-black.

As the Dongting Fisherman charged toward me with the streak of light, I spoke in a low, sunken voice.

“Turn down the volume, you sibu-leol bastard.”

*Fwoosh! Boom!*

The blue-white flames coated the transparent spearhead, and I stepped forward.

*Pop!*

Three zhang was not a short distance.

But the Dongting Fisherman and I were both superhuman beings who had set foot in the realm of Supreme Peak. The moment we shot toward each other, distance became meaningless. The gap vanished, and the air exploded.

White Flame’s spearhead, charged with extreme heat, and the Heavenly Silkworm Thread, writhing like a living creature while holding several *jiazi* of internal energy, tore through space.

*Shh-shh-shh-shh-shing!*

The speed was worthy of being called extreme swiftness.

The Heavenly Silkworm Thread, extending from the tip of the black-wood fishing rod, surged like a wave.

Its bizarre, unfathomable movements were unlike anything I had ever felt from the countless weapons I had faced before.

The scars left on the countless corpses scattered throughout Donghu Stronghold flashed before my eyes.

*He killed weak and innocent commoners with this martial art.*

I was neither a particularly sensitive person nor a *junzi*. I had no reason to defend the bandits of the Yangtze River Channel League. They were a group of river bandits who had gathered to plunder, and they had undoubtedly taken someone’s life and property.

It might seem as though I had taken lives too, but the difference between me and them was that they had not killed to survive. They had done it because it served their purposes.

But…

*People should not have died like that.*

Hundreds had been trampled like ants and cut down like livestock. Hundreds more had been drowned in the middle of Dongting Lake.

And most of them had not been martial artists. They were commoners who did not know even a single form of martial arts. There had even been children who could not write their own names.

People like that should not have died in such a manner.

A person could not kill another person like that.

“You get it, you son of a bitch?”

In the slowed world, my voice was buried beneath the raging wind.

Power surged through the hand gripping the spear shaft. Feeling the mighty Scorching Yang Qi boiling throughout my body, I brought the spearhead down at an angle.

*Fwoosh. Shhk!*

A single spark blossomed in the air.

At the same time, the streak of light scattered.

A section of the Heavenly Silkworm Thread was severed along the path traced by my spearhead and fluttered away.

The Dongting Fisherman, whose form had been countered so easily, let out a strange scream and swung the black-wood fishing rod again.

*Shing. Shh-shh-shh-shh-shing!*

Streaks of light split the air in every direction.

The Heavenly Silkworm Thread, filled with Force, sliced through space, piercing and cutting through everything that stood in its way.

But I avoided every attack and silently swung my spear.

*Shhk! Shhk! Shhk!*

I could see it clearly.

I could see where that strange weapon shaped like a fishing rod would go, and what movements the Heavenly Silkworm Thread attached to it would make as it came for me.

My half-open eyes took in every detail of the situation, while my senses, opened wide, read the attacks that were about to follow.

*If this were me before my Middle Dantian opened, it would have been difficult.*

When the place where you stand changes, the scenery you see changes as well.

Opening my Middle Dantian had expanded my senses and given me a new field of vision I had not even known existed. The result was unfolding right before my eyes.

*Here it comes.*

A strange weapon such as the black-wood fishing rod was difficult to master at first. But if one maximized its advantages and learned the appropriate martial arts, it became extremely difficult to deal with.

But I accurately predicted the trajectory rushing toward me and swung my spear.

*Shhk!*

“GRAAAAAAAH!”

The Heavenly Silkworm Thread was cut again by a fast, razor-sharp strike.

Without inflicting any meaningful damage on me, the thread that had once stretched five zhang had been reduced by nearly half. An even more ferocious aura poured from the Dongting Fisherman’s entire body.

“Now that’s more like a person.”

But martial arts displayed greater power when the mind and body were stable.

When the mind shook, the body lost its balance as well, and one’s movements became larger and rougher.

Finding a gap in the loosened net was not difficult for me.

*Whoooooosh!*

*Flamefire Path.*

A single streak of flame raced across the damp cave floor.

Its internal energy consumption was tremendous, and its trajectory was simple, but like most of the Fire Gate Clan’s martial arts, the Flamefire Path had two major advantages.

*It’s fast and destructive.*

*Boom!*

The air grew hot, and all the moisture around us evaporated.

I stepped onto the ground, now dry and crumbly as desert sand, and shot forward like an arrow.

*Swish!*

I turned my head, and the Heavenly Silkworm Thread that had been aimed at the back of my neck brushed past.

The Dongting Fisherman failed to land his attack and hurriedly redirected the thread, trying to wrap it around my entire body.

But I kicked off the ground half a beat faster.

*Boom! Shhk!*

Something as cold as ice traveled through the tip of my foot, then quickly grew hot as fire.

The flesh at the tip of my bare big toe had been cleanly sliced away.

The pain was severe enough that an ordinary person would have screamed, but I accepted it calmly.

*This is nothing.*

I had endured countless injuries and unimaginable pain while traveling between the modern world and Murim.

There had been times when I writhed in agony as though every bundle of nerves in my body were being severed, times when I had genuinely wished to die.

Compared to that, an injury like this was nothing.

No—it was an absurdly cheap toll.

For the loss of only part of my big toe, I had gained an opportunity to decide the outcome of this life-and-death duel.

*Now!*

My hands and feet moved like flowing water, obeying the command sent from my brain.

My movements were faster and cleaner than ever, without a hint of wasted motion.

I pulled the spear shaft back, then whipped it forward with all my strength.

*Whoooooosh—thud!*

The strike was truly as swift as lightning.

White Flame left my hand, smashed through the Dongting Fisherman’s shoulder as he sensed the danger and tried to retreat, then buried itself deep in the wall.

“GRAAAAAAAH!”

Listening to his scream of pain, I raised my fist toward him.

“I told you to turn down the volume.”

“……!”

*Thud!*
## Chapter artifact 466

# Chapter 466

Even without using internal energy—and though I’d held back—I had already far surpassed human limits through pure physical strength alone.

*Boom!*

The fist struck him squarely in the middle of the face, and the Dongting Fisherman’s entire body jerked. From his perspective, it must have felt like being hit with an iron club.

His pitch-black pupils trembled, and yellow teeth soaked in blood came tumbling from his gaping mouth.

*One more.*

*Thud!*

The Dongting Fisherman, blood pouring from his mouth and nose like a waterfall, staggered and waved his hand.

It was a small movement, but my sharp senses took in everything happening around me with perfect clarity.

*Swish!*

Something sliced through the air with a faint yet sharp sound, aiming for my back.

I already knew what it was.

*The Heavenly Silkworm Thread.*

Instead of dodging, I twisted the wrist of the Dongting Fisherman’s hand gripping the black-wood fishing rod.

*Crack!*

His bones broke, and the hand that had lost its strength let the black-wood fishing rod slip free. At the same time, the Force-infused Heavenly Silkworm Thread fluttered through the air.

“Where do you get off pulling that bullshit, you son of a bitch? Who do you think you’re fooling?”

The answer that came back was a heavy sound splitting the air.

*Whoom!*

The Dongting Fisherman’s palm strike shot toward me with terrifying momentum. But I had already prepared for it, so I reached out to meet it without hesitation.

*Boom!*

A swift, concise move of the Flame Divine Palm.

Two Forces—one white and one blue—collided in midair, and razor-sharp winds whipped around us.

Through my wildly fluttering hair, I stared at the Dongting Fisherman with cold eyes.

“What are you doing, you bald bastard?”

“……!”

I did not need an answer.

I already knew what I had to do, and the tip of my foot was already lashing out at the Dongting Fisherman’s knee with lightning speed.

*Thud!*

His bones crunched. His body staggered, and blood spilled from the corner of his mouth.

The heavy impact momentarily disrupted the flow of his internal energy, and the Palm Force gathered in the palm still pressed against mine began to fade.

“All right. As of today, we’re officially a thing.”

The scales of power had already tipped in my favor. I laced my fingers tightly between his and twisted with all my strength.

*Crack!*

Sibu-leol. I had never even held a woman’s hand in my life, yet here in Murim, I had interlocked fingers with enough men to fill a truck.

Of course, since it was an affectionate finger-lock fueled by the pent-up rage of a lifelong virgin, it was always effective.

Just like now.

“Gyaaaaaaah!”

A scream of pain burst from the Dongting Fisherman’s mouth, which had been silent until now.

I clenched my fist and punched him again and again as he stared at me with his pitch-black eyes wide open.

*Thud! Thud! Thud-thud-thud!*

Under the unceasing rain of fists and palms, the Dongting Fisherman’s movements slowly weakened.

Or so I thought.

“Gueeeeeegh!”

Why?

Carelessness, born from thinking I had completely secured the advantage? Confidence that I could capture him without killing him?

Whatever the reason, I had failed to be thorough, and that created an opening.

*Splaaash!*

My vision turned completely red.

The sticky blood the Dongting Fisherman vomited drenched my face and froze my body for an instant.

And the counterattack of a Supreme Peak master fighting for his life was fiercer than I had expected.

*Boom!*

With a sound like compressed air exploding, a stream of internal energy flowed through the surface of the Fire Dragon Armor as though it had passed straight through it, then battered my upper body.

My vision blurred.

As the scenery flashed past me, one thought crossed my mind.

*Damn it. Inner-Family Heavy Hand.*

He still had this much strength left?

I swallowed the blood surging up my throat and drew on my internal energy.

I had taken an unexpected blow, but compared to the Dongting Fisherman’s condition, this was nothing.

That I had suffered only a minor internal injury despite being caught off guard by the Inner-Family Heavy Hand was proof enough.

*Whoooosh!*

I sent my internal energy, its flow interrupted for only an instant, coursing through every limb and acupoint in my body.

The acupoints damaged by the Inner-Family Heavy Hand complained of a little pain, but that was all.

Just as a carp in a pond does not die because someone scoops out a bowlful of water, I was fine as well.

*I’ll finish this.*

I twisted my body around in midair as I shot forward. The opposite cave wall rushed toward me, so I gently planted my foot against it, then detonated the internal energy that had flowed into my toes.

*Boom!*

With a roar like the sky splitting apart, the unyielding rocks in the wall exploded.

Hundreds—thousands—of fragments tore through every direction, but I was already gone.

*Whoooooosh!*

Heavier than a rock, faster than the wind.

My body tore through the air several times faster than when I had been thrown back, carrying the weight of ten thousand *geun*.

“Dongting Fisherman!”

My shout reverberated through the vast cavern. Several *jiazi* of Scorching Yang Qi infused in my voice crushed the water and pushed the rocks aside.

And at the end of it all, there was one person.

“……!”

The Dongting Fisherman had just pulled White Flame out of his shoulder and the rock wall behind him when he spotted me and opened his eyes wide.

His blackened pupils shook, and a glimpse of white flashed across them.

His trembling mouth opened, and his one remaining front tooth quivered pitifully.

“C-c-c-come…”

Don’t come, you mean?

Fuck off.

I had no idea why the man who had been acting like a madman only moments ago was trembling like that, but my mind was already made up.

*I was planning to take you back in one piece if possible…… but that’s not going to happen.*

Regret would be useless now. The Dongting Fisherman should have regretted his actions long ago.

Before taking Dark Heaven’s hand. Before brutally slaughtering innocent commoners and children. He should have regretted it and repented then.

Now that we had come this far, repentance was unnecessary.

All that remained was punishment for the crimes he had committed.

*You’re fucking dead.*

I did not care if I crushed all four of his limbs. As long as he was still breathing, I could pull out every last strand of his hair and tooth, then drive a stalactite into his ass.

I would take his life only after he had spat out everything he knew about Dark Heaven.

I would keep him alive by the barest margin.

Only until my anger at what he had done had diminished, even slightly.

With exactly that much force, I shot toward him. In the slowed world, I extended my fist.

*Flame-Extinguishing Divine Fist.*

*Whoooooosh!*

The fiercely burning blue-white hellfire swallowed the palm strike the Dongting Fisherman thrust at me, even with his broken hand.

His Palm Force, now murky like muddy water, shattered and evaporated under the power of the Scorching Yang Qi. Beyond the endless whirlwind of wind and flashes of light, my fist wreathed in flame broke through the Body-Protecting Qi surrounding the Dongting Fisherman.

*Crack! Booooom!*

The Dongting Fisherman opened eyes whose blood vessels had all burst, vomited blood, and was driven into the wall.

Fine, spiderweb-like cracks spread across the hard rock of the cavern wall. Soon, they widened into a massive fissure that reached all the way to the ceiling.

*Rumble. Rumble-rumble-rumble!*

The ceiling collapsed, and the ground split apart.

The rocks that had endured tremendous water pressure deep beneath the vast freshwater lake of Dongting Lake began collapsing one after another. Streams of water surged up from every direction.

*Collapse.*

This space, created at some unknown time, would soon come crashing down.

Just like its owner, who would never return to his secret refuge.

*I have to hurry.*

*Rattle-rattle!*

I pressed the Dongting Fisherman’s acupoints to stop the bleeding. Then, in case anything happened, I sealed him with Pressure-Point Strikes so he could not move even a hair.

I hoisted the small old man onto my back, then punched forward without hesitation.

*Boom! Rumble-rumble-rumble!*

A raging current was visible through the hole in the floor, which had opened up like a sinkhole.

I took a deep breath, then leaped toward the violent water.

*Splash!*

As the cold water closed around my body, a familiar message rang in my ears.

> **System**
>
> Title effect activated: Water Rescue Worker
>
> Special Skill embedded in the Title applied.
>
> Water Rescue Worker’s Webbed Feet generated.
>
> Water Rescue Worker’s Gills generated.
>
> **Remaining duration:** 18 hours, 43 minutes, 32 seconds

There was plenty of time.

I moved my body powerfully with the current.

Before long, I saw the Dongting Fisherman constantly blowing bubbles from his mouth and nose. That reminded me of something I had momentarily overlooked.

*What the…… Ah.*

Even if someone was a master of water arts, that only applied when they had enough internal energy and consciousness to operate those techniques.

He did not have gills like I did. If he stayed underwater for too long, he might die.

*Wait. If that’s the case……*

A flash of insight crossed my mind.

At the same time, I began swimming with all my strength.

I might have been willing to donate an interlocked-finger clasp, but I could not give up my first kiss as well.

Especially not to a crazy old man who was nearly a hundred years old!

* * *

*Rumble-rumble-rumble!*

A vibration that began somewhere deep underwater grew so powerful that it reached the people on the surface.

At the sudden anomaly, the old boatman shrank into himself with fear in his eyes, while the other three men’s faces stiffened.

“Um, I think…….”

“It seems it has finally begun. Or perhaps it has already ended.”

Gung Gibang answered Cheongpung’s murmur in a heavy voice.

Hyuk Mujin, who had been anxiously watching the trembling cliff and river, suddenly opened his mouth.

“We have to go.”

Gung Gibang furrowed his brow.

“What?”

“It’s certain that something happened to our Captain. I have a bad feeling.”

“But Jin Taekyung, that bastard…….”

“He told us not to move and wait. I know.”

“Then why?”

“I have a terrible habit of not listening to people.”

“Damn. You sound proud of it.”

“Isn’t it better than sitting here sucking our fingers?”

At Hyuk Mujin’s words, Gung Gibang bit his lower lip.

He had been feeling uneasy for some time as well.

He did not know exactly when it had begun, but his heart was pounding violently, and every one of his senses was on edge.

*Why am I like this? Did something really happen to that bastard?*

A single face flashed before his eyes.

The Sleeping Dragon of Shanxi.

No—the Blazing Flame Divine Dragon, Jin Taekyung.

The kind of bastard who would come back alive even if you dropped him into the deepest pit of the underworld. More vicious than A-Gwi, and strong enough to beat Yama himself into the ground.

*I’ve never once imagined that bastard dying…… No, nothing is absolute, so surely not?*

Gung Gibang had not taken Jin Taekyung’s words before he entered the river lightly. By now, after traveling with him for so long, he knew that there was always a reason behind the man’s words and actions.

But this time, he could not help wavering.

*Goddammit. The weather’s a complete mess, too. What the hell am I supposed to do?*

*Rumble. Crash!*

Just as the old boatman had said a couple of *shichen* earlier, even calling the current weather on Dongting Lake the worst possible would have been an understatement.

A raging storm and lightning crashing down from the sky.

Gung Gibang looked around with a conflicted expression and finally opened his mouth.

Or rather, he was just about to open it when—

“It’s all right.”

“Huh?”

“What?”

Gung Gibang and Hyuk Mujin turned their heads at the same time.

Someone was smiling brightly in their field of view.

At the edge of the small island where they stood, Cheongpung had been lying face-down, listening to something. He brushed the sand from his ear and grinned.

“Benefactor is coming.”

And then—

*Splaaash!*

A person shot up with a towering column of water and landed roughly on the sandy shore.

A muscular young man with a small old man slung over his back.

It was Jin Taekyung.

“Captain!”

“You’re back!”

“Benefactooor!”

“Don’t come near me, you dickheads. If any of you is trying to hug me, all three of you are getting killed today.”

After stopping the three men charging toward him with cries of joy, Jin Taekyung continued in a serious tone.

“We don’t have time, so I’ll ask directly. Raise your hand if you’ve ever kissed someone. Or if you want to try. Hands up.”

Two of them caught on quickly.

One was hopelessly oblivious.

As Gung Gibang and Hyuk Mujin quietly backed away, one hand shot into the air with a bright, innocent shout.

“Me! Me! I haven’t kissed anyone even once!”

“Fuck. Thank God.”

“Huh?”

With a radiant smile on his face, Jin Taekyung held the Dongting Fisherman out toward the bewildered Cheongpung.

“Your wish has just come true.”

*Rumble. Crash!*

Thunder and lightning shook the entire world.
## Chapter artifact 467

# Chapter 467

I’ve always been the kind of person who thinks the process matters just as much as the result.

But sometimes, I deliberately look away from the process.

Not every process has to be perfect and beautiful, after all.

*What matters is the result. The result.*

Yeah, that’s all I’m saying.

And behind the process that everyone—including me—had chosen to ignore, an excellent result finally revealed itself.

*Cough. Splash.*

Water spilled through the Dongting Fisherman’s cracked lips as he coughed.

Cheongpung, who had shown a moving spirit of self-sacrifice against the Dongting Fisherman, opened his mouth with a strange expression.

“It feels weird.”

I exchanged glances with Hyuk Mujin and Gung Gibang, as well as the old boatman, then answered in a solemn voice.

“It’s always like that the first time.”

“Did you feel the same way, Benefactor?”

“……Of course.”

I had never done it before, but even if I did, I would not feel the way Cheongpung did. No, I shouldn’t.

I answered while subtly looking away. Cheongpung nodded, then took a deep breath.

“But I really don’t understand this.”

“You’re excited. That’s all.”

“It smelled strange, too. Like fish.”

*What a nose.*

I remembered the Dongting Fisherman tearing into a raw fish before our fight and answered.

“You’re imagining it.”

“My stomach feels sick.”

“That’s because your hormones are being secreted. Kissing is good for your immune system and helps relieve stress, too……”

“What?”

“Nothing.”

“My stomach just feels really nauseous. I want some sweets.”

Hyuk Mujin patted Cheongpung on the shoulder with a guilty look.

“I’ll buy you some later, Young Hero Cheong.”

“You will, Hyuk Mujin?”

“Yes. I’ll find some way to feed you until your stomach bursts.”

“But you’re poor too, Hyuk Mujin. Last time, I saw you picking up silver nyang at the ferry landing……”

“My father is rich.”

Hyuk Mujin was the son of a wealthy family. He only seemed poor because he had suffered all sorts of hardship while following me around. His family business was thriving by the day.

At the proud declaration of a second-generation rich kid planning to bleed his father dry, the other two men, who had been watching Cheongpung with sad eyes, joined in.

“Young Hero Cheong, I’ll chip in too, even if I have to beg for it.”

“This old man is also willing to lower your fare a little.”

“Wow! Really?”

“……”

A pang of guilt stabbed at one corner of my heart.

But it couldn’t be helped. It had definitely been his choice.

After forcing myself to rationalize it, I checked the Dongting Fisherman’s condition.

“How is he?” Hyuk Mujin asked from over my shoulder.

I nodded. “He’s fine.”

“Uh…… He doesn’t really look fine.”

I was momentarily speechless as I looked down at the Dongting Fisherman.

Both arms were twisted at bizarre angles. Countless wounds covered his body beneath his clothes, which had been torn to shreds.

This was merely the extent of the injuries visible to the naked eye. Serious internal injuries came on top of that.

“What on earth happened?”

I gave them a brief summary of what had happened inside the underwater cave.

“I was on guard in case something happened, but he was weaker than I expected, so I beat the shit out of him and dragged him back.”

“……”

After a brief silence, Hyuk Mujin spoke.

“But the Dongting Fisherman is a master of incredible water arts.”

“That’s why I beat him on land. Turns out there was a cave inside.”

“You have an incredible talent for describing extremely difficult things as if they were easy.”

“It wasn’t extremely easy, but it wasn’t extremely difficult either.”

“……”

“The important thing is that he’s still breathing.”

“It seems miraculous that he’s still breathing.”

“Considering what that old man has done, he deserves to die right now.”

“That’s true. Either way, it’s fortunate. I was worried about the Dongting Fisherman, of course, but I was also worried that Dark Heaven’s other bastards might be there with him.”

That was something I had been considering as well.

According to Honglan’s testimony, the only person responsible for the Dongting Lake tragedy was the Dongting Fisherman.

But the slaughter of Yangtze One Saber and so many others at Donghu Stronghold would have required at least two Supreme Peak masters, if not more.

*Mungyeong said the same thing.*

No matter how rapidly I had grown, facing two or more Supreme Peak masters at once was……

Well, it was something I could only hesitate to answer.

Even when people reached the same realm, their abilities could vary wildly.

*The Dongting Fisherman was a step below me.*

I had been lucky. If the Dongting Fisherman had been moving with another Dark Heaven powerhouse, the tables might have been turned on me instead.

Of course, I wouldn’t have started a fight with such slim odds in the first place.

“But shouldn’t this old man be waking up by now? Why isn’t he moving at all? Did he swallow too much water?”

At Gung Gibang’s question, Cheongpung, who had been rinsing his mouth with water from the lake, answered.

“He’s been hit with Pressure-Point Strikes. Right, Benefactor?”

“Yeah. Exactly.”

At present, the Dongting Fisherman had his Paralysis, Mute, and Sleep Acupoints struck.

Even if his Sleep Acupoint were released and he woke from his forced sleep, his body was paralyzed, and he could not even move his lips. He could not even squirm like a grub, much less resist.

“What do you intend to do now?”

“We’ve accomplished our objective, so we’re going back.”

We were not the only ones who knew the location of this place. If Dark Heaven had caught wind of it and sent reinforcements, we could easily have ended up trapped instead.

*If a monster like the Western Heaven Demon Lord showed up, we might have to prepare ourselves to die.*

There were clear limits to what Cheongpung and I could do alone.

It was certain that Dark Heaven had been involved in the series of incidents that had taken place in Hubei Province. But the biggest problem was that we knew neither their location nor their members.

If I could force the Dongting Fisherman to talk, however, we could expose every last detail about them and launch a counterattack.

The Fire King and the Slaughter Saint—two peerless Supreme Peak masters—as well as Wudang and the Zhuge Clan, the undisputed rulers of Hubei Province, would all commit their full strength.

“We’re leaving. Right now.”

However, an obstacle I had not considered stood in our way.

“Um, Great Hero.”

The old boatman had suddenly spoken. After hesitating for a moment, he continued with a stiff expression.

“I’m sorry, but this old man’s humble opinion is that it will be impossible.”

“What?”

“As you know, Great Hero, the state of Dongting Lake right now……”

*Rumble-rumble-rumble! Crash!*

Thunder booming from all directions swallowed the rest of the boatman’s words.

He hunched his shoulders as though frightened, then pointed around us with anxious eyes.

“Look. How could we launch a boat in conditions like these?”

“……!”

There was good reason for him to tremble in fear like that.

The sky had turned pitch-black, and lightning struck here and there. Heavy rain had begun pouring down at some point, and the waters of Dongting Lake had risen noticeably. Violent whirlpools lashed against the cliffs and rocks.

*Of all times for this to happen.*

It had not been this bad when we entered the Dongting Fisherman’s secret refuge. Yet in the short span of less than a shichen, the situation around us had deteriorated toward the worst possible outcome.

But……

“We have to go.”

“G-Great Hero.”

“I understand that you’re afraid, but it’s possible. You saw it with your own eyes. You saw how we got here.”

I had suffered a minor internal injury, but I was still in good condition.

On top of that, we had Cheongpung, a Supreme Peak master, and Gung Gibang, who possessed exceptional martial arts. Hyuk Mujin could also lend a hand in an emergency.

No matter how bad the weather was or how violent the current became, it was not so impossible that we could declare it hopeless.

The old boatman thought differently.

“This old man has held an oar on Dongting Lake for more than forty years. I’ve never ferried great masters like you before, but I’ve also never launched a boat in weather as vicious as this.”

The old boatman stammered in a trembling voice.

“All I know how to do is read the water and row a boat. I’m an unremarkable old man, but I’ve spent more than half my life on Dongting Lake. If it can’t be done, it can’t be done.”

“Boatman.”

Gung Gibang stepped forward, but before he could say anything, the boatman shook his head repeatedly.

“I know what you’re going to say. But no matter how skilled you are, it’s clear you won’t make it very far.”

“Why do you think that?”

“The boat won’t hold up.”

“……!”

At the boatman’s firm declaration, everyone—including me—opened their eyes wide.

That was right. No matter how sturdy it was, a ferryboat was still a ferryboat.

To find the Dongting Fisherman’s secret refuge, the boat had needed to be light and small. It had been perfect for that purpose, but those same advantages were now its greatest weaknesses.

*It would take at least two shichen to reach land, even if we took the shortest possible route…… What if the boat sank before then?*

The answer to the question I had asked myself came back immediately in the negative.

*Even if I used my internal energy to perform Rising on Duckweed, Crossing Water, the distance left is too great. And that was before the weather became like this. The boatman is right. The boat won’t hold.*

Even at a glance, I could see spots where wood had been torn from the surface of the ferryboat hauled up onshore.

Like its owner, whose hair had turned completely white, the ferryboat was also somewhat old. The current and the voyage today had been especially rough.

*Damn it.*

This wasn’t something I could solve by persuading the boatman.

I could use the Water Rescue Worker Title’s effect, which still had plenty of time remaining, or try the same method of using the Inventory that I had used at Dongting Lake before.

But even after considering all the circumstances, the risk was too great.

“Captain.”

I raised my head at Hyuk Mujin’s voice and saw the faces looking back at me.

Under their gazes, I thought for a moment, then bit my lip.

“What about the route leading in?”

“Pardon?”

I spoke clearly to the old boatman, who had hunched his shoulders at another peal of thunder.

“If it’s difficult to get out, wouldn’t it also be difficult to get in? Especially in conditions like these.”

“Ah, of course it would. The passage is so narrow that anything but a ferryboat like this old man’s would be unable to enter, and with these insane currents, getting in is several times harder than getting out. Launching a boat on Dongting Lake in weather like this is madness to begin with.”

Then that was even better.

It meant that a possible invasion by Dark Heaven would naturally be blocked as well.

*It’s better to wait here until the weather settles down.*

That was the exact moment I finished thinking and was about to give an order.

*Tap. Tap-tap-tap!*

A sudden movement began nearby.

I and the others turned our heads toward its source and opened our eyes wide at the same time.

*What the hell?*

The small old man who had been lying still as though dead—the Dongting Fisherman—was twitching.

Even as we watched, the trembling running through his body was becoming faster and stronger.

“He was definitely under Pressure-Point Strikes…… How?”

Cheongpung muttered as though groaning.

As the person who had struck the Dongting Fisherman’s pressure points, I could not easily accept what was happening either.

But the surprise lasted only a moment.

Before my mind could fully understand what was happening, my body had already moved.

*Swish!*

I shot forward like a gust of wind and thrust out my hand at top speed.

First, the Sleep Acupoint.

Next, the Paralysis Acupoint.

Finally, the Mute Acupoint.

The moment I finished striking his pressure points again, I realized something I had not expected.

*His acupoint seals had never come undone in the first place. This was simply…… the Dongting Fisherman’s body reacting independently of his will.*

That was when I hesitated in confusion.

*Grab!*

A hand seized my wrist, which had been left hanging in midair.

The Dongting Fisherman was staring at me with his eyes wide open.

Unlike in the cave, his pupils looked like those of an ordinary person.

They were filled with fear.

And then a hollow voice, empty as though his soul had left his body, pierced my ears.

“Run.”

What?

I had no time to form a question.

I wasn’t given a chance to react.

At the moment every sense in my body went taut, an enormous roar erupted behind me.

*Kaboom—!*
## Chapter artifact 468

# Chapter 468

*Rumble-rumble-rumble, crash!*

It was a storm unlike anything anyone had ever experienced.

Every time thunder boomed alongside the lightning, the rain grew heavier, and the river thrashed like a violent dragon.

And one ship was trying to make its way against it all.

“Hard to port!”

At Ship-Fire Boy Mu Song’s shout from the stern of the ship, which rocked like a willow leaf before the raging waves, the river bandits of Water Dragon Stronghold gritted their teeth.

“Grrrrgh!”

“Keep rowing! Put your asses into it and row!”

“Anyone who slacks off from this moment on had better watch out! What was it called again? Right! I’ll sentence you to the dip-and-taste punishment!”

“Aaaaaah!”

Every one of them was an experienced, highly skilled sailor.

But despite Mu Song’s seasoned commands and the river bandits’ efforts to summon every last ounce of strength they possessed, the worst weather they had ever encountered refused to let the ship advance any farther.

*Crash! Boom!*

The sail, stretched to the point of tearing, gave way beneath the force of the wind. Rocks of every size came flying from all directions and slammed into the deck.

Mu Song’s eyes flashed with disbelief at the impossible sight.

*What in the world is this?*

What he had learned from his Master, the Seafaring King, was not limited to martial arts.

If anything, he had first learned how to steer all sorts of ships, predict the weather, and read the currents—before he had learned martial arts.

Mu Song had been a sailor before he was a Murim martial artist, and no river bandit would follow a captain without the ability to lead.

The little boy who had yearned for the Yangtze had grown into a captain so skilled that even old sailors acknowledged him. Even his bleak Master, who possessed not a trace of affection for his Disciple, had once said:

> “It’s a shame. If your grit and martial talent had been even half as good as your skill with ships, you might have taken your Senior Brother’s place.”

There could not be two masters of the Yangtze River Channel League.

The Seafaring King, who had chosen his Senior Disciple as his successor, sent Mu Song to Sichuan. After founding Water Dragon Stronghold, Mu Song soon distinguished himself and seized control of Sichuan’s Yangtze at a young age.

Yet even Mu Song had never seen anything like this.

His Master, the Seafaring King, and the old river bandits who had spent their entire lives as sailors before retiring had probably never seen it either.

*It wasn’t like this when we left the Yangtze tributary. So how…?*

The reason was simple.

A sudden change in the weather—so drastic that it was shocking.

Their current location was none other than Dongting Lake.

After receiving Zhuge Feng’s sudden summons, Mu Song had selected his most capable subordinates, crossed Tianling Falls, and immediately set out for Dongting Lake after asking around for Jin Taekyung’s whereabouts.

Not long afterward, they had run into a storm more suited to the middle of the sea.

*Is this even possible? On Dongting Lake?*

Hubei Province’s climate was generally warm. Its annual rainfall was fairly consistent, and although the Yangtze occasionally flooded, the flooding was rarely severe. In fact, it was one of the reasons the region had become such a fertile breadbasket.

Dongting Lake? It was certainly one of the three largest lakes under heaven, but it was still only a lake.

No matter how bad the weather became, it should not have been worse than the Yangtze’s current. Compared to the unpredictable whirlpools of the sea, it should have been laughable.

That was what he had believed.

At least until two shichen ago.

*It wasn’t this bad when we first launched the ship.*

He had not been particularly worried. Since Dongting Lake was not connected to the Yangtze or the sea routes, there was no way to bring a swift ship here. They had borrowed a small merchant vessel instead and headed for the place where Jin Taekyung’s group was said to have gone.

Or rather, they had tried to.

Unlike at the beginning, the weather had worsened the closer they came to their destination.

It was as though they had crossed some invisible line. Strange phenomena that should not have been possible on a lake were appearing everywhere.

*Whoooooosh.*

A waterspout rose with a chilling howl of wind.

It towered to a dizzying height, blocking the narrow waterway as it advanced toward the merchant vessel, a groan slipped between Mu Song’s clenched teeth.

“What the fucking hell is this…?”

If they were caught in that, it was over. Even if they managed to get past the waterspout, the merchant vessel’s poor durability would not let it survive for long.

Torn between concern for the safety of his subordinates and his desire for revenge against Dark Heaven, which had killed Yangtze One Saber, Mu Song finally moved his lips.

“I’m sorry, but I’m afraid this is as far as we can go.”

An old voice answered him.

“That’s enough.”

And then—

*Snap!*

Behind Mu Song, a small figure that had remained perfectly balanced leaped from the mast.

The figure shot toward the waterspout through the driving rain and wind, then clenched a fist.

*Hooooong.*

A single stream of wind wrapped around the fist mottled with age spots. The air stopped moving, and not a single drop of rain dared approach.

At the tip of that fist, hellfire capable of burning everything took shape.

“Get the hell out of my way.”

Alongside a voice like boiling lava, Fire King Jeok Cheongang threw a punch.

*Flame-Extinguishing Divine Fist.*

*Whoooooosh!*

The next moment, Mu Song and the river bandits saw it clearly.

The flames rising from the fist transformed into a fire dragon and bit into the waist of the waterspout.

The churning water collapsed in an instant beneath the overwhelming Scorching Yang Qi, and all its moisture evaporated. The waterspout, which had been approaching the merchant vessel with the power of ten thousand *geun*, became a dense cloud of steam that spread like fog around them.

Then—

*Boom!*

The heavy sound of something splitting the air scattered the steam.

Jeok Cheongang stood tall in midair, looking down at the merchant vessel. His voice, more deeply subdued than usual, drifted from his lips.

“What are you waiting for? Hurry up and follow me.”

He was not speaking to Mu Song or the river bandits under his command. Their roles had been decided from the beginning, and they had more than fulfilled them.

The battlefield that was about to unfold was a place permitted only to true masters.

And as everyone watched, one person stepped forward.

“Single Reed Crossing the River. Even Master Bodhidharma of Shaolin used a reed leaf to cross a river. From now on, you’d better come down instead of wasting your internal energy for no reason.”

There was not even a trace of emotion in the dry, monotonous voice.

The bright, warm boy who had been caring for the sick as a medical apprentice only a short while ago was nowhere to be found.

As Mu Song and the river bandits flinched and stepped aside, Mungyeong clicked his tongue inwardly.

*Dong Feng. You foolish Disciple. In the end, things turned out exactly as you wanted.*

He had lived as a medical apprentice for more than forty years.

With hands that had taken more than a thousand lives, he had treated and cared for sick patients.

Instead of fiends, he had fought the bastard called plague. He had gained the undeserved reputation of being a Divine Physician, but he had never once taken wealth or chased fame.

It had merely been atonement.

And a vow.

But now, the stone pagoda he had built deep within his heart over decades of living as a medical apprentice had come crashing down.

No—perhaps the stone pagoda had collapsed on the day he boarded the swift ship leaving Sichuan.

*This is also the path this old man chose. How could I blame anyone else?*

With a dry chuckle, he stepped forward. Behind him, a middle-aged man in disheveled scholar’s robes appeared.

“This junior will go with you, Seniors.”

At the words of Zhuge Feng, the current Family Head of the Zhuge Clan and the Crouching Dragon Guest, Mungyeong answered in a dry voice.

“Of course you should. Why else would I bring a burden like you?”

“You certainly have a talent for embarrassing people.”

Mungyeong made a show of frowning. He had no intention of listening to Zhuge Feng’s rambling, especially when the man was no more than a babe compared to him.

“Enough nonsense. Get on my back.”

“You underestimate this junior. My enlightenment may not match that of the other Family Heads of the Five Great Families, but when it comes to internal energy alone…”

“There’s a reason I brought you here. If I had prioritized martial arts, I would have brought that youngster Hyeongong of Wudang instead. But shouldn’t someone remain back there?”

“……”

Perfected Being Hyeongong was a master senior enough to stand shoulder to shoulder with the Sect Leaders of the Nine Sects and One Gang.

Mu Song and the river bandits had been unable to determine Mungyeong’s identity beyond knowing that he was a Returned to Youth master. They were shocked by the way he referred to the respected elder, Perfected Being Hyeongong, as a child.

“Gasp!”

“Who in the world is that man…?”

But Mungyeong had neither the time nor the inclination to answer.

He stretched out his hand, and Zhuge Feng’s body came sliding toward him.

After seizing none other than the current Family Head of the Zhuge Clan with Seizing an Object Through Empty Space, Mungyeong lightly stepped off the deck and leaped like a bird.

*Snap!*

A movement technique both stealthy and impossibly elusive.

Not a single person left aboard the ship could recognize the Ghost Illusory Slaughter Step, perfected to its ultimate stage.

Leaving the stunned men behind, Mungyeong’s body shot forward as though folding space.

“Is this the right direction?”

*Splash!*

Two—no, three figures moved swiftly across the surface of the river.

Zhuge Feng, dangling from Mungyeong’s hand, answered Jeok Cheongang.

“According to what Ship-Fire Boy told us, we only need to move straight ahead from here.”

“Are you certain?”

“Of course. However…”

“However?”

After hesitating for a moment, Zhuge Feng continued.

“We still don’t know whether Young Hero Jin is there.”

“He is. Without a doubt.”

Jeok Cheongang immediately shook his head. His tone was nearly one of certainty.

“This weather… It isn’t a coincidence. Something unknown came here, and Taekyung is clearly after it.”

“It’s too early to jump to conclusions. Identifying what it is must come first.”

At Mungyeong’s words, Jeok Cheongang unconsciously reached inside his robes.

His hand closed around something as sharp as a sword blade and as hard as armor.

When Mungyeong had first brought it and shown it to the two of them, neither Jeok Cheongang nor Zhuge Feng had been able to believe what it was.

*What is this? What in the world is happening?*

Just then, as the unease rapidly swelling in the old man’s chest grew, so did the speed at which he crossed the river with Rising on Duckweed, Crossing Water.

*Rumble-rumble-rumble!*

A tremendous roar rang out from beyond the violent rain and dense fog.

The three men opened their eyes wide.

“This is…”

It was not thunder and lightning rumbling across the sky.

The black sky above their heads was quiet. The enormous sound from a moment earlier had clearly come from somewhere several hundred *jang* ahead of them.

“You bastards—!”

Jeok Cheongang’s furious roar rang out, and his body shot forward first. Mungyeong followed with Zhuge Feng held firmly in his grasp, splitting the water on either side.

But before even an instant had passed, the three men were forced to stop simultaneously.

“……”

The impact was so immense that none of them could open their mouths.

They did not even need to move closer to confirm what had caused it.

At last, the identity of “it” appeared in the distance.

The three men stood frozen, speechless.

* * *

*Rumble-rumble-rumble!*

The cliff collapsed with a deafening roar.

Massive boulders that had clearly been part of it for centuries came pouring down like a rain shower, and an enormous spray of water surged upward.

But none of that mattered.

I stared with trembling eyes at “it” rising from among the destruction.

More precisely, I stared at the System window floating above its head.

> **System**
>
> Lv. ??? Mutated Water God Dragon
## Chapter artifact 469

# Chapter 469

Everyone saw it. They could see it.

Amid the blackened sky and the violent rain and wind, they saw the shower of bizarre rocks pouring down from above.

*Rumble-rumble-rumble, crash!*

When a massive boulder struck the surface of the lake, spray erupted several *jang* into the air. Birds that had lost their nests tumbled from the collapsing cliff with sharp cries, while torrential rain and lightning battered the world without pause.

And as everything collapsed around them… one being alone reared up.

*Whoooooosh!*

Water streamed down its body like a waterfall.

Far below, the humans reduced to tiny dots gazed up at the being that had finally revealed itself, their eyes filled with stunned disbelief.

It was enormous.

The word felt insufficient, yet no other word came to mind.

Only one question filled everyone's head.

*What is that?*

Scales with an ominously beautiful black sheen. A sturdy torso so thick that ten large men would have to stretch out their arms to encircle it.

As their gazes traveled up the long, flexible body rising more than thirty *jang* above the surface, they saw two horns jutting from its forehead.

And beneath them, a pair of eyes.

Blood-red pupils stretched into long vertical slits. Between the slowly parting scales, saw-edged teeth emerged, along with a beast's maw that looked like a dark cave had been transplanted into its face.

“Grrrrr.”

The ominous growl that echoed down from the distant sky sent a chill deep into the bones of Crouching Dragon Guest Zhuge Feng.

*What is this…?*

Zhuge Feng had been called the greatest genius in his clan since infancy.

He possessed an exceptional mind that never forgot anything he had seen, as well as an insatiable thirst for knowledge. Over the years, he had read tens of thousands of books and made the world's vast knowledge his own.

The river of knowledge within Zhuge Feng was endlessly broad and deep.

Or so he had thought.

Until he saw that.

*This can't be.*

It was the fear of facing the unknown for the first time in his life.

At that moment, Zhuge Feng realized that all the knowledge and information he had accumulated had turned to foam.

He also realized that fragments of the many myths and legends he had dismissed as nonsense had appeared before his eyes.

*Could those absurd stories… really have been true?*

Zhuge Feng had always firmly believed in the power of his knowledge.

He was a martial artist, but first and foremost, he was the Family Head of the distinguished Zhuge Clan, and he had used reliable information and knowledge to protect his many clansmen and his family’s power.

To a man like him, unverified superstition was not worth considering. Believing in an illusion no one had ever seen was simply foolish.

But someone standing a hundred *jang* away from Zhuge Feng was different.

Unlike Zhuge Feng, he was not a Family Head responsible for an entire household. He was merely an old boatman who had survived by relying on his own experience and a single ferryboat.

“……!”

The old boatman stared into the sky with trembling eyes.

A colossal being stood tall amid the collapse of everything around it. The sight alone made his legs buckle, while unbearable awe and fear pressed down on his shabby shoulders.

The cry that the pressure kept him from releasing echoed only inside his heart.

*It’s the divine spirit. The spirit of Dongting Lake has revealed itself!*

The world was filled with more superstitions than anyone could count. Hubei Province was no exception.

An old man told a child, and when that child grew old, he told another child. Stories passed from mouth to mouth for hundreds of years.

The old boatman was no different.

A native of Hubei Province who had spent his entire life on the water, he knew the identity of the being he called a divine spirit.

The Two-Horned Beast of Dongting Lake.

The Water God Dragon.

The true master of Dongting Lake.

*Ah… ahhh…*

The old boatman trembled violently. His entire body shook beneath an incomprehensible emotion, and something surged in one corner of his chest.

It was an emotion only he, among everyone present, could feel.

Awe and fear that could never be expressed in words.

A boatman to the very marrow of his bones, he could not believe that he had come face-to-face with the master of Dongting Lake. The aura flowing from that being made it difficult to breathe.

*The divine spirit is angry. All of this happened because the divine spirit was enraged!*

The old boatman realized that his guess had been correct.

The countless deaths that had occurred one after another over the past month. He did not know why, but the divine spirit had certainly been angered beyond measure.

And in the end, it would punish him just as it had punished the others.

With death!

He could not die like this. Somehow, he had to calm the divine spirit's anger.

A cracked cry burst from the old boatman's mouth as he stood there as if entranced.

“D-Divine spirit! I have committed no sin!”

The silence that had settled over everyone shattered. The old boatman's cry scattered into the rain and wind.

Before the others, frozen rigid by the giant being's appearance, had a chance to stop him, the old boatman ran toward the water on trembling legs.

“Divine spiriiit!”

*Tap-tap-tap, splash!*

The instant the old boatman's shabby straw sandals touched the water of Dongting Lake—

*Swish.*

In a world that had slowed to a crawl, a gigantic pair of eyes turned toward him.

The old boatman's reflection appeared in the vertical, blood-red pupils. As the being recognized the tiny, insignificant human, the light in its eyes began to burn red.

*Whoooooosh!*

A chilling aura erupted in every direction from the thirty-*jang*-long body.

Birds that had been taking flight lost their strength and fell. Thousands of fish fleeing in schools through the depths of Dongting Lake floated belly-up to the surface.

An aura as immense as its body, an aura akin to death.

Neither insignificant creatures nor even humans could remain unharmed before it.

Before that invisible aura even reached him, the old boatman's entire body had already stiffened like a stone statue.

His mouth hung open, his eyes bulged wide. Just as his pupils began to roll white beneath the grip of terror—

*Whoosh! Thud!*

With a sharp whistle of something cutting through the air, the old boatman's body crumpled where he stood.

A young man gently caught his frail body, then raised his head and stared at the enormous being.

“Hey, you sibu-leol eel bastard.”

“……!”

At the clearly audible voice, the enormous being's pupils swelled as though it had realized something.

Different.

Every human on the ground had frozen from shock and fear, but that young human was different. He had neither been shocked nor trembled in fear.

Fear of the unknown came from facing something incomprehensible.

But that young human was free from all of it. It was not merely that he had no fear. He looked almost familiar with it.

Just like now.

“Can't you open those eyes properly?”

With that offhand remark from the young man, Jin Taekyung, a streak of light cut across the air.

*Whoooooosh! Thud!*

* * *

When I first saw the thing, only one thought flashed through my mind.

*Am I seeing things?*

I had no choice but to think that. A monster I had seen somewhere before had appeared right in front of me—not in the modern world, but in the Murim.

If it had merely been an illustration inserted into a fantasy novel, that would have been one thing. Unfortunately, its source was the *Monster Encyclopedia*, completed over the past several decades by countless leading scholars and Hunters who had fought in the Great Cataclysm.

*Could that be…?*

Although the monster I had fought most often during my Hunter career had been low-level creatures like goblins, the section I had looked at most in the *Monster Encyclopedia* was the one covering the highest-level monsters.

And that thing was one of the monsters given a particularly large entry.

*…A Sea Serpent.*

As its name suggested, a Sea Serpent was a marine monster.

In the early days of the Great Cataclysm, a Sea Serpent announced its existence to the entire world by sinking a US carrier battle group. For some reason, it vanished shortly after the Great Cataclysm.

No, let me correct that.

At least, that had been the case until a moment ago.

*A Sea Serpent in the Murim? What the hell is going on…?*

I stood frozen in shock, but I soon noticed something strange.

*Wait. Something's different.*

In the modern world where I had been born and raised, the Sea Serpent was not some fictional monster that appeared only in mythology.

It was one of the highest-level monsters serving the Demon King Asmodeus, as well as one of the major culprits responsible for inflicting terrible damage on humanity.

Naturally, high-resolution photographs of the Sea Serpent itself had been preserved, along with video records of its battles.

But the monster that had appeared before me now was clearly different from the Sea Serpent shown in the *Monster Encyclopedia*.

*The Sea Serpent is shaped more like a sea snake, but that thing looks closer to an Eastern dragon.*

Now that I looked closely, I was certain. The size and length of its body were slightly different, as were the shape of its face.

If there was one crucial similarity between these two monsters that were alike, yet different…

*Whoooooosh!*

It was that.

An inherently ferocious aura possessed only by monsters—fundamentally different from the killing intent martial artists called killing intent.

*Fear.*

Fear was exactly what it sounded like: terror, dread.

Every monster possessed it, but the stronger the monster, the more powerful it became.

It shackled an enemy's body by instilling fear and terror, then shattered the enemy's mind.

*Just like the Dongting Fisherman.*

The scattered puzzle pieces in my head began falling into place.

The Dongting Fisherman's state, which had seemed almost insane. His clear eyes returning only after all his strength had drained away.

*He must have encountered that thing before us.*

Even a Supreme Peak master with immense martial prowess and an unshakable mind could be overwhelmed by the fear of facing the unknown for the first time.

In terms of Fear alone, an S-rank Hunter would probably be much better equipped to deal with it than a Supreme Peak martial artist.

And…

*That goes for me, too.*

*Ding.*

> **System**
>
> - You resisted **Fear**!
> - A powerful mind overcomes terror!

*Whoosh, thud!*

I caught the old boatman's collapsing body as I struck his pressure points.

One second. No—even a quarter of a second later, and this poor old man might have gone mad from Fear or simply died.

I raised my head and looked at the enormous being standing in the distance.

*Damn. It's huge.*

I had never fought a Sea Serpent, but this thing was clearly no pushover.

It had just taken a spear I had hurled with all my strength and still had not fallen.

*Bam!*

With a heavy impact, the colossal body, more than thirty *jang* long, swayed slightly.

The sight was like watching a small mountain move. I bit down gently on my lip.

*I couldn't pierce its scales.*

I could tell from the sound alone. Even after pouring all my strength into the iron spear I had just taken from my Inventory, I had failed to inflict any meaningful damage.

If I had used White Flame, forged from Ten-Thousand-Year Cold Iron, I could have dealt a more decisive blow.

But if I could not finish it in One Strike, that would be a foolish move.

It was more urgent to act before the enormous monster recovered from its confusion.

I turned my head and drew a deep breath as I pulled internal energy up from my dantian.

“Cheongpung! Hyuk Mujin! Gung Gibang!”

“Hup!”

“Urgh!”

A thunderous shout burst from my mouth, so massive that it was hard to believe it had come from me. The bodies of the three men, who had been frozen like stone statues, flinched.

No.

Not three. Two.

Unlike Gung Gibang and Hyuk Mujin, whose eyes looked as though half their souls had left their bodies, Cheongpung was staring at me with a startled expression.

“You startled me. What is it, Benefactor?”

“……?”

*What the hell is this guy?*

Anyone would naturally freeze upon seeing a monster like that. I was the exception because I had been exposed to monsters to the point of loathing them while growing up in the modern world.

But Cheongpung had been born and raised in the Murim. The fact that he could overcome Fear so easily was astonishing.

“Young Hero Cheongpung. Are you really all right?”

“Huh? What about it?”

“I mean, that thing over there…”

“Oh, right. I was really surprised.”

Cheongpung spread both arms and cried out emphatically.

“It’s huge! Really huge! I’ve never seen anything like that in my life!”

“……”

*I hadn’t thought that through.*

*Cheongpung had been out of his mind from the beginning.*

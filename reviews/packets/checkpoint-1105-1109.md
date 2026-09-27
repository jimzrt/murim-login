# Checkpoint Review — 1105–1109

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

# Chapters 1105–1109

## Plot

At the North Gate, Jeok Cheongang faces the Dalai Lama and Potala Palace forces rather than leave to reach Taekyung at the West Gate. There, the Blood Lord absorbs blood and life force, kills roughly two hundred defenders with redirected arrows, and clashes with Taekyung. As Taekyung unleashes One Annihilation, Cheongpung—who survived being buried in the earlier blast—cuts a concealed Black Ghost with the Zaha Divine Technique. Taekyung collapses, but the System gives no death confirmation; the Blood Lord survives, initially without his senses or memories.

Taekyung manages to shout an order to attack. Cheongpung and Jeong Hogun’s Embroidered Uniform Guards push through the fanatics toward the Blood Lord, who regenerates by absorbing blood, regains his strength and memories, and remembers a debt to Mae Jonghak. Cheongpung wounds him, but the Blood Lord calls for reinforcements. Countless flying beasts descend around an unidentified being, and a violent impact fills Cheongpung’s vision with blood.

## Continuity

- Xining remains under attack by Dark Heaven and the Potala Palace; fighting continues at the breached West Gate. Jeok Cheongang faced the Dalai Lama’s forces at the North Gate.
- Taekyung used One Annihilation, collapsed, then shouted an order to attack while weakened. His condition afterward is unknown; the System did not confirm the Blood Lord’s death.
- Cheongpung survived the blast, used the Slaughter Saint’s Ghost Illusory Slaughter Step blended with Dark Fragrance Drift, and attacked the Blood Lord. The final impact obscured his vision with blood; his fate is unknown.
- The Blood Lord can absorb blood to regenerate. He regained his strength and memories and remembered a debt to Mae Jonghak.
- Countless flying beasts descended after the Blood Lord called for reinforcements; the being at their center is unidentified.
- The Lord of Heaven’s interest in Taekyung remains unexplained. The hidden Dark Heaven agent among Cheongheoja’s Disciples remains unidentified, and Cheongheoja’s favor to Taekyung remains undisclosed and unfulfilled.

## Translation Decisions

- Render 西藏 as “Xizang” for the Murim region; retain “Tibet” when Taekyung identifies it from his modern-world perspective.
- Keep “Blood Lord” for 혈주, “Lord of Heaven” for 천주, and “Embroidered Uniform Guard” for 금의위.
- Retain “Twelve Secret Monks,” “Black Ghost,” “Zaha Divine Technique,” “Ghost Illusory Slaughter Step,” and “Dark Fragrance Drift.”
- Keep “One Against a Hundred” distinct from “One Against a Thousand,” and render 天上天下, 萬魔仰伏 as “Heaven above and earth below; All demons bow!”

## Durable state

{
  "active_continuity": [
    "Dark Heaven and the Potala Palace are attacking Xining; fighting continues at the breached western wall.",
    "Jin Taekyung used One Annihilation, survived, and shouted an order to attack while weakened.",
    "The Blood Lord regenerated by absorbing blood, regained his strength and memories, and remembered a debt to Mae Jonghak.",
    "Countless flying beasts descended on the battlefield after the Blood Lord called for them; the being at their center is unidentified.",
    "Cheongpung attacked the Blood Lord; a violent impact at the end of the chapter obscured Cheongpung’s vision with blood."
  ],
  "continuity_sources": [
    1108,
    1109
  ],
  "open_questions": [
    "What condition is Jin Taekyung in after using One Annihilation?",
    "What happened to Cheongpung in the final impact?",
    "What are the flying beasts and the being at their center?",
    "Why does the Lord of Heaven want Taekyung, and what does he intend to do with him?",
    "Which of Cheongheoja’s Disciples is the hidden Dark Heaven agent, and what did Cheongheoja ask Taekyung to do?"
  ],
  "safe_through": 1109,
  "temporary_decisions": [
    "Render 西藏 as “Xizang” for the Murim region; retain “Tibet” when Taekyung identifies it from his modern-world perspective."
  ],
  "version": 1
}

## Reading copies

## Chapter artifact 1105

# Chapter 1105

Could it be because Xining had faced one foreign invasion after another for so many years?

The four walls surrounding Xining now ran a full ten ri in length, enclosing a vast area with a sturdiness rarely seen even in the Central Plains.

But everything had its pros and cons.

The walls had been reinforced little by little over time, making them effective at keeping out invaders. But that also meant there was more ground to defend.

The defenders had to find ways to keep in touch with one another across such vast distances.

They did so with war drums and flags stationed at various points.

But at least in this moment, the blood-red flash that suddenly erupted in the west was enough to render all of that useless.

*Fwoooosh.*

Would it look like this if dozens, hundreds of sunsets overlapped?

The world slowed. Countless eyes flew wide at the strange sight, impossible to describe.

The soldiers on a dozen or more watchtowers, beating their assigned war drums and waving their flags with all their strength.

The people hiding in Xining’s Inner City, clutching their families and peering through cracks in the doors.

The combined forces of the imperial troops and Murim warriors, fighting back the enemies surging toward them like waves—and even the Supreme Peak masters at the heart of their ranks, at the very front, cutting down enemy after enemy without pause.

And the moment every one of them felt an instinctive chill run up their spines—

*Pop.*

At last, the blood-red flash rising over the western wall swelled.

No—it exploded in a vivid, horrifying burst of red light.

*Rumble-rumble-rumble!*

The deafening roar made everyone’s ears ring.

The ground shook. The entire stone wall trembled.

Then a colossal shock wave surged over the western wall and crashed down on the people frozen like statues.

“Danger—!”

*KA-BOOOOM!*

The rushing wind swallowed someone’s single shout and swept across everything.

The North Gate was no different.

Dust and shattered rock flew through the air, mixed even with ownerless blades. Everyone ducked and threw themselves toward cover.

Everyone except one man, still holding the front line.

*Fwoosh—BOOM!*

Flames burst from a forcefully thrust punch, devouring the space around him.

Even the storm, like a natural disaster, bowed before its heat. Everything flying toward the defenders at the North Gate evaporated in an instant.

*Shhhhh.*

Ash drifted slowly away on the now-gentle breeze.

But the eyes of the man who had protected his allies from the unexpected threat—Fire King Jeok Cheongang—were more somber than ever.

*…What in the world was that?*

Though he held the chief seat among the Ten Kings, he had already reached a realm where he could stand shoulder to shoulder with the Three Saints.

That was why he could feel it with every inch of his skin, every one of his senses.

The immense power contained in that distant blood-red flash that had erupted in the west.

And if its shock wave had reached the North Gate, more than two hundred jang away, what state must the West Gate—the source of that strange phenomenon—be in?

*Blood Lord, how did you…?*

Jeok Cheongang bit his lip without realizing it.

The Blood Lord’s martial prowess had advanced unmistakably since their encounter at Mount Song. But what also weighed on his heart was the voice of someone he couldn’t stop thinking about.

*“I’ll take the West Gate.”*

Jin Taekyung.

When his Disciple had said that just before the battle, Jeok Cheongang had answered without a moment’s hesitation.

*“Absolutely not. Instead of spouting that nonsense, do one more complete circulation. And don’t go getting yourself stabbed just because you’re acting up.”*

*“My internal energy’s in great shape, and I can take a few stabs. So I’ll take responsibility for the West Gate.”*

*“I said no.”*

*“Why not?”*

*“You have to ask? That damned bastard has been mine for a long time. Today, I’ll finally collect the blood debt from that day.”*

Jeok Cheongang’s answer had been both true and untrue.

He did want revenge for Hong Dao, his old friend. But the more important reason was that the enemy’s main force, including the Blood Lord, was stationed at the West Gate.

His Disciple was a reckless brat who’d long since thrown manners out the window. But he was his one and only Disciple.

The person who had become more precious to him than anything else in the world. He couldn’t leave him alone in the most dangerous place.

Of course, Taekyung knew his Master far too well for Jeok Cheongang to hide that bashful concern behind roundabout words.

*“There you go worrying again. You don’t have to do that anymore.”*

*“Worry? Don’t be ridiculous. Just know that it’s absolutely out of the question.”*

*“I’ll be fine. I have no intention of dying a pointless death. Do you think I’m crazy? I’m doing this because I’ve got a good reason.”*

*“A good reason?”*

*“You know already. As long as the Lord of Heaven wants me this badly, those guys can’t lay a finger on me. Well, I might get a little hurt.”*

*“That…”*

Even Jeok Cheongang couldn’t easily argue with that.

Ever since the incidents surrounding Mount Song and Sichuan, powerful enemies—including the Southern Heaven Demon Empress—had been decidedly reluctant to take Jin Taekyung’s life. And the battle in Gansu had made all those suspicions certain.

Seeing his Master waver, Jin Taekyung drove in the final nail.

*“No matter which gate I take, they’ll follow me, since I’m their most important target. In that case, it’s better for me to take the West Gate. It’s the best-defended, isn’t it?”*

Every word he’d said had been right from beginning to end. In the end, Jeok Cheongang had no choice but to give in and head reluctantly to the North Gate.

But—

*I shouldn’t have done it.*

In this moment, Jeok Cheongang couldn’t help but deeply regret his decision.

He’d judged wrong.

The Blood Lord’s martial prowess far exceeded what he’d imagined, and Jin Taekyung’s lie had been so effortless, even though he knew exactly how his Master would react.

*At this rate… that boy’s in danger.*

The attack that had unfolded before everyone’s eyes could only have come from someone with the intent to kill.

So, though his body had grown young again, his heart was still that of an old man. Feeling himself grow impatient, Jeok Cheongang turned toward the west.

No—he was about to.

Until the next instant, when he sensed a sharp thread of killing intent shooting like a needle from beyond the wall.

“Where are you rushing off to, donor?”

The voice was low.

Yet the several jiazi of internal energy within it were enough to shake the entire area around the North Gate.

So was the immense aura emanating from the old monk standing tall atop a colossal elephant, unlike anything Jeok Cheongang had ever seen at the Nanman Beast Palace.

“If you leave like this, donor, all the way I’ve traveled will have been for nothing.”

His frame was tiny, his skin wrinkled with age.

But his presence was like that of a giant, and Jeok Cheongang already knew who he was.

He also knew what it meant that this old monk—the Dalai Lama, Palace Lord of the Potala Palace—had appeared at the North Gate leading all those troops.

“…So this was your plan. From the beginning.”

A low groan slipped from between his lips.

Then the Dalai Lama spoke, turning Jeok Cheongang’s ominous suspicion into certainty.

“The Fire Gate Clan’s line will end. Right here, today.”

At that moment—

*Bwaaaaaaa!*

As the Potala Palace forces surged toward him to the sound of a war horn, Jeok Cheongang gritted his teeth without realizing it.

*Crack.*

His lips went white. His nails dug deep into his skin, and hot blood ran between his fingers—not the conflict he felt.

It wasn’t too late yet.

He had to go. Even now.

To his Disciple. To Jin Taekyung.

But—

“P-Potala Palace! They’ve joined the battle!”

“Arrows! Bring more arrows!”

“Form a defensive line! Don’t retreat, even if it costs us our lives!”

“Sir Jeok, we don’t have time to hesitate!”

Shouts and screams from all sides held him in place.

Eyes filled with fear, resolve, or faith grabbed at his hands and choked at his throat. Along with them, the urgent voice of Perfected Being Hyeoncheon, fighting at his side at the North Gate, pierced his ears.

*What would he have done? That boy—what would he have done?*

With the question buried deep in his heart, Jeok Cheongang squeezed his eyes shut.

In that brief, profound darkness, he recalled the conversation he’d had with his Disciple the day before.

*“I never wanted to be a hero.”*

*“That doesn’t matter. You don’t become a hero just because you want to. You earn the right when the world calls you one.”*

*“Like people call you a Great Hero, Old Master?”*

*“What?”*

*“You just said it yourself. You didn’t set out to follow some great cause. You just went where your feet led you, where the wind took you, and before you knew it, people were calling you a Great Hero.”*

*“……!”*

He remembered it clearly.

The bright smile directed at him when he’d been left speechless. The playful expression. The clear eyes.

Perhaps that was what he feared more than anything else.

Perhaps the thought that he might never see that face again had come first.

But when Jeok Cheongang had asked Taekyung whether he was still afraid of the enemy, his Disciple had nodded without hesitation and added:

*“Even so, I won’t turn away from that fear.”*

Calm. Resolute.

And everything that had happened that day was the answer to the question Jeok Cheongang had just asked himself.

*Fwoooosh.*

In an instant, tremendous heat swallowed the space.

Beyond his slowly rising eyelids, eyes glowing red with heat poured out a gaze like flame.

Toward the Dalai Lama and the Twelve Secret Monks flying through the air toward him.

Toward the two Black Ghosts who had appeared, and the vast enemy army surging in behind them.

*Grnnnnk.*

As the space warped under the unbearable heat, the giant of fire roared with all his might.

“Come on!”

As if he meant to burn the whole world.

“This old man is Jeok Cheongang, the eighteenth Sect Leader of the great Fire Gate Clan—the Fire King!”

He hoped his roar would reach his Disciple.
## Chapter artifact 1106

# Chapter 1106

*BOOM!*

The flash before my eyes was blood-red.

*Pwoom!*

Every strike carried an unfathomable force, churning through the air.

*Krrrunch!*

The world kept turning upside down, then righting itself.

No—not the world. Me.

*Fwoooooosh—BOOM!*

A tremendous shock ran up my spine, then spread through my entire body.

And the result of dozens of exchanges, unfolding like lightning, was me buried deep beneath layers of fallen stone from the wall.

*Cough.*

Blood surged up against my will and seeped past my lips.

A System warning chime rang in my ears along with the ringing in them, and pain radiating from every corner of my body proved it was no lie.

*I’m sure I heard something.*

I muttered weakly to myself.

Just before the assault sent me flying, I’d heard someone’s familiar voice ringing out in the distance for a brief instant.

But I must have imagined it.

One of those hallucinations that came to me every now and then when I was exhausted and hurting.

“……Damn it.”

Blood kept welling up. My torn-up hands tingled.

Even so, with a quiet curse, I forced my aching body upright.

No. I had to.

If I didn’t stop that monster, none of the thousands of allies risking their lives to defend the West Gate could.

*Splash. Splash.*

Heavy footsteps approached, neither fast nor slow.

With every step, the blood that swirled ankle-deep in the downpour trembled like a living thing.

*Shhhhhh.*

It was enough to make anyone who saw it feel a chill run down their spine.

Hundreds of snakes, red from head to tail, seemed to slide across the surface of the water.

And at the end of their eerie advance stood a monster, already prepared to take in new power.

*Hssss.*

The blood seeped into his skin as though it had never been anywhere else.

Then the monster’s eyes glowed an even fiercer red, flashing through the pounding rain.

They were fixed on a single person among the countless allies frozen like statues.

Me.

“Didn’t I tell you?”

His low voice cut clearly through the rain.

The monster of blood had absorbed all the blood within a radius of more than a hundred feet, devouring the life and strength it contained. He fixed his gaze on me, eyes bright with delight.

“You can never be my equal. No one on this battlefield can.”

The veterans who’d survived for years in Murim, a mountain of sabers and a forest of swords, had a saying.

Confidence could turn into conceit and arrogance—and beyond those lay sheer hubris. Those were the feelings you had to watch out for most.

If an enemy was swept up in them, you were supposed to seize on that weakness and find a way to survive.

It had passed down among martial artists like a maxim, and Jeok Cheongang had often given me similar advice.

But—

*This isn’t conceit.*

I knew it instinctively.

No—I was the one facing that monster, so I couldn’t help but know better than anyone.

This wasn’t arrogance, or hubris. It was certainty.

A certainty even I, who had created more possibilities and variables than anyone under heaven, couldn’t deny.

The monster who had become the true Blood Lord was approaching, his power and presence crushing everything around him—greater than anyone else on this battlefield.

*Krrr.*

The air trembled. The ground shook.

Neither the torrential rain nor the arrows that the archers on the still-standing parts of the wall had summoned the courage to loose could touch a hair on his head.

They had only managed to provoke him.

*Vmmmm.*

As if caught by an invisible hand, the hundred or so arrows hovering above the Blood Lord’s head suddenly trembled and turned around.

Toward the insects who deserved to die for daring to bar the path of a monster who had drawn close to the absolute ruler.

“Get out of the way!”

The instinctive cry burst from my lips.

*Fwhoosh! Thud-thud-thud!*

With a single, ferocious roar, the arrows flashed through the air like streaks of light.

The shield-bearers protecting the archers with their iron-plated shields. The archers taking cover behind them.

Everything in the arrows’ path.

*Thud.*

It began with the unit commander at the front dropping to one knee.

They stared blankly at one another.

Eyes wide with disbelief, they looked back and forth between the huge holes torn through their bodies and the monster standing hundreds of feet away. Then they breathed their last.

“T-This can’t be……”

*Thump. Clatter.*

One by one, bodies fell onto the ground slick with blood and rain.

Some stumbled backward in terror. Some tried to advance, refusing to believe death was coming. Some crumpled where they stood without even a final cry.

Each met death in a different way, but not one of them could escape it.

They all died.

Two hundred of our allies—archers, shield-bearers, even martial artists.

In a single instant.

*Slide. Splash!*

At that moment, someone’s nameless body rolled over the wall and landed in a pool of blood.

“Heaven above and earth below.”

In the suffocating silence that settled over everything, Dark Heaven’s followers had entered past the broken ranks and wall ruins that had crumbled with the Blood Lord’s arrival. As if bewitched, they began reciting their creed.

“All demons bow!”

They no longer shouted.

The killing intent they’d unleashed in their desperate efforts to cross the wall was gone, too.

*Shhk!*

They simply swung the blades in their hands without a word.

“Heaven above and earth below……!”

Their faces glowed with rapture as they marveled at the miracle unfolding before their eyes.

“All demons bow……!”

They praised the one ruler who wasn’t on this battlefield, yet could bring all under heaven to their knees from within that deep darkness.

Even if death awaited them at the end.

*Crunch!*

“L-Lord of Heaven.”

Even when a stray blade cut their throats, when their arms and legs were severed, when their chests were pierced, they never lost the smiles etched across their lips.

The dozen fanatics charging at me without a hint of fear were no different.

“A-at last. The glory of martyrdom……”

*Stab! Krrrunch!*

In the end, humans were made of flesh. Once their heads were gone, they couldn’t speak.

That was true not only of the Temporary Strength Pill, which let a person draw on strength beyond their limits at the cost of their life, but of anything they could take.

But why?

I’d swung my hand like a blade and cut their heads off in one blow, yet it sounded as if their unfinished words were still carrying on in my ears.

Again and again. Without a single moment of silence.

“These…… crazy bastards.”

A curse slipped out of me, my breathing suddenly ragged.

It felt like the blood in my body had turned to ice.

I thought I’d seen and dealt with enough lunatics to last a lifetime.

The twenty-first-century world I’d been born and raised in was a place with its own kind of barbarity, different from Murim.

Skyscrapers soared above the clouds. More than half a century had passed since humanity first ventured into space. A civilization combining cutting-edge science and Magic had grown brighter and more powerful than ever.

But nothing changed.

The modern world was still full of Madmen.

People were murdered in broad daylight. Judges’ gavels and reporters’ cameras swayed under the weight of money and liquor.

And that wasn’t all.

Dictators, relics of a bygone age, prepared for wars—and started them.

There were plenty of people trying to bridge the distance between religions and sects with missiles and terror instead of forgiveness and reconciliation.

In the world I’d seen, they were all fanatics.

Madmen who’d lost their minds by attaching themselves blindly to their own goals. They saw and felt only what they wanted, swaying as they got drunk on it.

Of course, the most extreme of them had been the fanatics who followed the Doppelganger. But now I could say it without a doubt.

The size and purity of the madness I’d seen in them was nothing next to the Dark Heaven followers before me.

And at the center of this blood-soaked storm of madness, a monster came hurtling forward with the momentum of Mount Taishan.

“Have you ever seen moths?”

I could feel it.

The Blood Lord’s ease—and the fact that he never let his guard down.

His red eyes were fixed solely on me, as though he had no interest in the battles raging all around us. They brimmed with certainty and killing intent.

“I have. Countless times, before the Tianshan Mountains fell under that person’s control. I saw those foolish things fly toward torches and burn to death.”

I didn’t answer.

Instead, I drove the shaft of White Flame, still in my grip, deep into the ground at my feet. Then I kicked up the weapons strewn around me and sent them flying at him.

*Fwoooooosh—BOOM!*

*Krrrunch!*

The blades, wreathed in Force, cut through the air one after another. Then an immense shock wave slammed into the space around them with a deafening roar.

Not where I’d aimed—the Blood Lord—but somewhere in the air and ground.

“But one day, as I watched them, a question occurred to me.”

The Blood Lord swung his Red Blade at lightning speed, casually knocking aside everything flying toward him, and continued speaking in a clear voice.

“Did those things fly toward the torch knowing they’d burn to death? Or could they only fly toward it because they didn’t know?”

*Crunch!*

I cut down the enemies charging at me from every direction. After the wall, our ranks were now collapsing fast, too.

The sight of fanatics charging in, shouting about martyrdom, and the wave of fear they stirred up were even overpowering the effect of One Against a Thousand.

“I still haven’t found the answer. No—I never bothered looking. It wasn’t long before I met that person and gained such overwhelming power that I didn’t need to think about how moths felt.”

At that moment—

*Whoooooom!*

The Blood Lord lifted his Red Blade high. A massive, crimson Force surged along its scarlet edge.

A power beyond anything I’d ever seen—or even imagined could exist.

“But I think someone like you could know the answer.”

Certainty in himself.

Killing intent sharp as a blade. Hatred beyond anger. The elation of finally achieving his purpose.

Every one of those feelings—his aura and power—was directed solely at me.

I found it hard to breathe. My hand trembled.

But I was ready.

I’d prepared my greatest attack. Maybe my last.

I took a deep breath and let the words that had been circling on the tip of my tongue spill out.

“I’m not one of them.”

“What?”

“I’m the kind of bastard who doesn’t burn to death even if he flies into the flames. Who flies in first whether he knows what’ll happen or not. That’s me.”

“……!”

The silence felt like an eternity, though it lasted only an instant.

At its very end, the Blood Lord answered.

No—he moved.

So did I.

*Pop.*

Across more than a hundred feet of space that vanished in an instant, his Red Blade carved a massive line of blood-red light.
## Chapter artifact 1107

# Chapter 1107

Murim warriors spend their whole lives lingering at the crossroads of life and death.

Some live out their natural years thanks to their skill and the luck they were born with. Others get dragged into some petty squabble and die like dogs in an instant.

That was probably why.

Because they lived closer to death than anyone, they’d even coined a grand term like a life-and-death duel, trying to make their own uncertain end sound a little more solemn.

But at some point, I realized that no matter how many fancy words the world had to offer, or how many valorous titles people bestowed on one another, the nature of it never changed.

In the end, this was just a fight.

One where each person gave everything they had to bring down the opponent in front of them, driven by their own cause, circumstances, or selfish feelings.

It could be fair. It could be unfair.

That was why it was a fight.

A simple, straightforward process in which the one who was even half a step faster, ten geun stronger, and far more vicious and cunning won.

And I knew that very well.

I knew the gap between my opponent and me, and what the best I could do right now was.

*And the worst, too.*

Watching the Blood Lord cross a dozen or so jang through the slowed world, I muttered to myself.

Regret over this choice? Fear of death?

I didn’t know.

To be exact, there wasn’t enough time to come up with an answer.

Even in the sluggish flow of time, the Blood Lord moved like a flash of light—and I was definitely slower.

Half a step.

No. Right now, there was a gap of more than a full step between us, one I could never close. It stood like an iron wall.

So, in the end, there was nothing else I could do.

I could only charge at him like a moth.

Before that torch, reeking of blood, swallowed everyone, I had to put it out with one last, all-out beat of my wings.

*Grnnk.*

Every muscle in my body contracted at once.

At the same time, the internal energy I had left—less than a third—surged from my Lower Dantian to my Middle Dantian, then awakened the hundreds of large and small acupoints and the Eight Extraordinary Meridians lying dormant in my body.

*Hoo.*

I was hot, as if I’d become a fire dragon myself. If I opened my mouth and roared, it felt like lava would pour out.

But I couldn’t do that.

I had only one chance to spew out that lava.

It wasn’t my first time, but it was all but certain to be my last.

Just as the System warning chime that suddenly pierced my ears in this very moment seemed to say.

*Beeeeeeep.*

It stretched out into a long ringing in my ears, following the slowed passage of time. It sounded like the flatline of a heart monitor announcing a patient’s cardiac arrest. That wasn’t an exaggeration.

One Annihilation.

This colossal lava, boiling up from deep within me, held enough destructive power to turn even me to ash.

*Fwoooosh.*

Heat warped the space as it slowly surged outward.

Flames that had seared my Lower Dantian and Middle Dantian, hundreds of acupoints, and the Eight Extraordinary Meridians layered over the spearhead.

For my one and only, final chance.

*This is all I’ve got. The only way to bring him down.*

Of course, this wasn’t the first time I’d used One Annihilation against the Blood Lord.

During the Shaolin Bloodshed, he’d taken the full force of it and still gotten back up, thanks to his incredible regenerative ability.

But there was an almost unfathomable gulf between the me who’d been stuck at the Peak realm back then and the me I was now.

And One Annihilation had grown just as much—powerful enough to devour even its wielder’s life.

*Unlike last time, he won’t get back up now.*

One blow to render even the Blood Lord’s terrifying recovery useless.

The moment blue-black flames, which would turn his body and even his soul to ash in an instant, flickered along the spearhead of White Flame, drawn far back—

*Fsssss.*

A sudden chill crept down my spine.

What was this feeling?

I was the archer. My body was the bow, and the string was already drawn taut.

All I had to do was let go.

All I had to do was thrust my spear at the Blood Lord, now just one jang away, as if to blow up the whole world—and it would all be over.

Then why, at the most important moment, was this inexplicable sense of wrongness suddenly coming over me?

Fear of the death that was all but certain now?

Regret for the life I’d lived and the people I’d leave behind?

Or a flashback of my life, arriving with the sense that this was the end?

No.

I was wrong.

This feeling coming over me now wasn’t like any of those I’d experienced several times before.

This was a warning.

A warning from the other me—the one that followed nothing but instinct.

And at last, the moment reason and instinct met inside me—

……!

……!!

Time, held back until now, and every sound and sight around me came crashing down all at once, like a massive wave breaking through a dam.

And with it came a blurred afterimage, flashing between the Blood Lord and me as we shot toward each other.

*Fwoooosh!*

A fierce whistle split the wind and rain, shooting from an unseen blind spot.

I realized too late that it was there—the figure clad from head to toe in pitch-black armor. No, *it*.

I felt the blood in my body turn cold.

*Black Ghost……!*

So that was it.

That was what the unease I’d felt earlier meant.

The card the Blood Lord had kept hidden until the very end. He had grown stronger than before, and his planning had grown sharper still.

*He planned it. He’d been waiting for this moment from the start.*

The realization struck like lightning through my skull.

Only then did I understand.

It wasn’t the Blood Lord who’d let his guard down. It was me.

The other side could learn from past mistakes, too.

Despite his inhuman regenerative ability and overwhelming martial prowess, the Blood Lord had waited for One Annihilation until the very last moment, then put the Black Ghost he’d kept hidden in front of him as a shield.

As if he wouldn’t allow even the smallest variable.

And the price of my carelessness was shoving me hard in the back, right at the edge of a cliff.

There was no other way.

I’d already come too far to turn back.

“Damn it.”

Realizing there were no more choices, I let out the curse I’d been holding back and thrust my spear—the weight of my past and future resting on its tip.

*Gooooom.*

The space warped.

The fire dragon’s flames roared, flooding everything I could see in blue-black.

And at the last moment, as that dreadful heat was about to devour everything in its path, a streak of light swept past the Black Ghost like an apparition.

*Shhk.*

A tiny whistle—so faint I wouldn’t have heard it if my senses hadn’t been sharper than ever.

And it wasn’t an apparition or a hallucination.

* * *

One Annihilation.

When that terrifying strike—the one that had briefly cornered him in the not-so-distant past—shot toward him, the Blood Lord thought:

*It’s over.*

Certainty in a life-and-death duel was no different from poison.

But even he, who’d endlessly turned over the final moments of the four Demon Lords and the Demon Empress who had fallen to Jin Taekyung, couldn’t help but feel certain now.

Blazing Flame Divine Dragon Jin Taekyung.

The vile connection with that damned brat, who made him sick just to think about, ended here.

The plan was that perfect. It was as good as a success already.

*You’ll never kill me.*

There was no mistaking it: Jin Taekyung had grown beyond recognition.

And so, the Blood Lord had no doubt that the strike he couldn’t begin to understand had grown terrifyingly powerful, too.

It had become so powerful that even the Blood Lord, who now considered himself all but immortal, had thought of death when he felt the unprecedented energy wrapped around the spearhead.

But this was as far as it went.

*The lion uses all its strength, even when hunting a rabbit.*

A predator always gives everything it has, even when catching a single rabbit.

It had taken the loss of an arm and a long period of humiliation for the Blood Lord to realize that and put it into practice. But thanks to that, he was able to avoid the sharp teeth the rabbit had hidden.

The one Black Ghost he’d kept by his side for this moment alone.

He’d sent as many as eight Black Ghosts to the three gates other than the West Gate, and entered through the breached wall alone, all to pin down the enemy and make that brat let his guard down.

So Jin Taekyung would focus solely on him.

So he would believe that the Blood Lord was his only enemy.

And the Blood Lord’s plan had worked.

No—more accurately, he thought it had worked.

As massive flames erupted from the spearhead and swallowed the space, a streak of light flew in from somewhere and swept past the Black Ghost that, following its orders, had moved between Jin Taekyung and the Blood Lord.

*Shhk.*

*……What?*

A ripple he couldn’t conceal spread across the Blood Lord’s eyes, which had been filled with unwavering certainty.

Then his gaze trembled and settled on the Black Ghost’s neck, which was slowly rising into the air.

A handful of purple Force scattered like flower petals from the gap between the body’s halves, separated with empty space between them.

*That’s…*

There was no mistaking it.

That distinctive light, spreading like the petals of a plum tree or the colors of the sunset, belonged exclusively to the Zaha Divine Technique.

Staring blankly at the scene, stunned as if the world had stopped, the Blood Lord remembered a face he’d momentarily forgotten.

The man looked remarkably like the one who had taken his arm, yet had vanished from the battlefield so anticlimactically that he’d hardly seemed worthy of inheriting that man’s teachings.

But before the Blood Lord could speak the name of the other brat that had surfaced in his mind, the blue-black flames swallowed the Black Ghost’s body without a trace—and engulfed him.

*KWA-AAAAA!*

A colossal pillar of fire surged up, sweeping across heaven and earth.
## Chapter artifact 1108

# Chapter 1108

He was dead.

No—he’d thought he was dead.

A quarter of an hour ago, the young man who had hurriedly thrown himself in front of Jin Taekyung, lost in a Trance and unable to sense the danger, had been certain he was about to die.

But he hadn’t.

After a blood-red flash charged with an unprecedented force came a tremendous impact that battered his entire body.

When he finally opened his eyes, clinging to the thread of consciousness that had briefly been severed, the young man buried beneath a pile of stones—or rather, Cheongpung—muttered to himself:

*This is the most dangerous thing I’ve ever been through… No, it isn’t.*

If this had happened before—or, more precisely, if he hadn’t gone through what happened on Mount Song—he might have trembled with fear.

Overwhelmed by the terror of death, something he’d never experienced before, and frozen by the killing intent and madness he’d never felt amid the clear streams and plum blossoms of Lotus Peak, he might have been unable to move.

But—

*I have to move.*

Things were different now.

The child who had wandered through Huashan’s beautiful scenery had entered the martial world and learned how to run.

He’d faced the world’s ugliness and learned what anger felt like. He’d spent time with good people and come to understand what human decency meant.

So even knowing that countless threats and hardships still lay ahead, he could rise again.

That was the right path his grandfather, who had raised him, had taught him. It was the chivalry he had learned from watching Jin Taekyung.

*Go. To my Benefactor. To them.*

Cheongpung pushed himself to his feet, unsteady.

He shoved aside the stones weighing down his body and endured the pain from bones broken here and there, moving slowly.

And more stealthily than ever before.

*“You want me to teach you martial arts?”*

Perhaps it was the blood trickling from the large and small wounds etched across his body. In his wavering vision, a conversation he’d once had with the Slaughter Saint seemed to echo in his ears.

*“Do you even know what you’re asking?”*

*“Uh, I think so.”*

*“Unbelievable. The Sword Saint’s Disciple, of all people, wants to become a mere assassin.”*

*“Huh?”*

*“You idiot. I don’t practice martial arts. I practice the art of killing. It’s not for someone like you.”*

Back then, the Slaughter Saint had shaken his head with a bitter smile.

At least, until he heard Cheongpung’s reply.

*“Huh. I don’t think that’s true.”*

*“What?”*

*“My grandfather told me it’s not the tool that matters, but the person holding it. And there was an assassin I saw a long time ago who didn’t seem like the kind of person who’d hurt someone for no reason.”*

*“……!”*

*“Oh, and he said everyone we cross paths with in this world could become our teacher and Benefactor.”*

*“……You.”*

*“Please take care of me, Granduncle!”*

Remembering how the Slaughter Saint had silently watched him, then spoken with an expression that grew complicated, Cheongpung let out a quiet breath.

*Hoo.*

His heart, pounding from pain and blood loss, grew calm. The blood flowing from wounds across his body gradually stopped, and his presence faded.

*“It won’t be easy to master even one technique. You don’t have the time, and the situation won’t allow for it.”*

*“Wow, so you’re saying yes, right? You are, aren’t you?”*

*“Damn it. Fine. But I have one condition.”*

*“A condition?”*

*“Never call me that again.”*

*“Yes, Little Master!”*

*“Damn it.”*

*“Oh. Sorry, Granduncle.”*

*“……Where in the world did the Sword Saint pick up a lunatic like you?”*

The Slaughter Saint probably hadn’t known.

Before even a month had passed since their journey began, he’d find himself asking that question again—but with a very different meaning.

*“……Where in the world did the Sword Saint pick up a lunatic like this?”*

*“Grandpa said a stork brought me. My Benefactor said it was something about ovulation, fertilization, and implantation, but I couldn’t make heads or tails of it.”*

*“……I really can’t understand.”*

*“Right? I’d never heard such bizarre words in my life.”*

*“……It’s my first time, too. Seeing a case this bizarre.”*

The Slaughter Saint’s bewildered face rose before Cheongpung’s eyes.

At the same time, his feet, now as light as feathers, touched a pool of blood.

No—they barely brushed it.

*Shhk.*

Ghost Illusory Slaughter Step.

The unique footwork technique created by the greatest assassin of all time—so stealthy that no other technique under heaven could match it—unfolded beneath Cheongpung’s feet.

*“You were right, Granduncle. This really isn’t easy.”*

*“……Is that something someone who reached three-tenths mastery in only a month should be saying?”*

It was the unique technique of none other than the Slaughter Saint, known as the greatest assassin of all time.

And yet Cheongpung had mastered Ghost Illusory Slaughter Step at a dazzling speed.

For someone else, a month might have been *only* a month. For him, it was an entire month.

*“I like martial arts. A whole, whole lot.”*

*“That much I know…… This is driving me mad. How is this even possible?”*

It was possible.

To Cheongpung, all of it came as naturally as breathing.

He watched with his eyes and moved with his body, and before he knew it, the technique became his.

Just as the words implied, it was reborn with Cheongpung’s own character woven into it—a new martial art that belonged to him alone.

*Whoosh.*

Cheongpung moved forward.

With each step, neither fast nor slow, it seemed that only he could smell the fragrance of plum blossoms spreading through the air.

Dark Fragrance Drift.

The fragrance of Huashan’s plum blossoms spread through the pouring rain. It had merged with Ghost Illusory Slaughter Step, which Cheongpung had brought to nine-tenths mastery over the past six months with the Slaughter Saint, becoming quieter and more elusive still.

So much so that even with both eyes open, no one could clearly make out his presence.

*Shh-shh-shh-shhk!*

“Graaagh!”

*Thrust! Slice!*

“Heaven above and earth below; all demons—Guh!”

The battle raging all around had already spun beyond anyone’s control, and yet no one noticed Cheongpung slipping past them.

As he crossed the heart of the battlefield, he blended naturally into everything around him.

He was the rain falling ceaselessly over everyone’s heads. He was one of Dark Heaven’s fanatics, drunk on madness and the effects of the Temporary Strength Pill—and one of the martial artists and soldiers trying to stop them.

He was a part of this chaotic battlefield, and the battlefield itself.

Moving in only one direction, toward only one person.

*Benefactor.*

Cheongpung saw him.

*Gooooom.*

The space warped as if gripped by an invisible hand. Jin Taekyung was about to unleash, all at once, an appallingly immense force.

And charging at him was the Blood Lord, while a pitch-black figure lunged from his blind spot, as though it had been waiting for this very moment.

*I’m too late.*

His instincts whispered.

It was a shame, but this wasn’t enough.

Cheongpung had neither the strength to bring down the Blood Lord nor the time.

But—

*He can do it. My Benefactor can.*

That wasn’t a guess. It was certainty.

An unwavering faith in Jin Taekyung.

So Cheongpung shot forward without hesitation.

Straight toward the enormous flames erupting in a distant flash of light.

Straight toward the Black Ghost, which had thrown its own body in the way as a shield to counter that unprecedented force.

*Fwoosh.*

Time slowed. Space disappeared.

Just before One Annihilation was unleashed, a flash of light slipped between his tightly shut eyelids and pierced his retinas like a needle.

But Cheongpung could feel it clearly.

The Black Ghost standing at the end of his path.

The strike he was making now, drawing a single line toward that pitiful figure.

And then—

*Shhk.*

The moment he passed the Black Ghost with a cut almost too quiet to hear, a lightning-like shiver surged up his spine.

A shiver that wouldn’t fade, not even in the dreadful heat swallowing the space he had just crossed.

*I did it.*

At the same time, a colossal fire dragon swallowed the Black Ghost’s body as it tilted helplessly.

No—or rather, it swallowed the blood-red monster charging from behind it.

*KWA-AAAAA!*

Even as the overwhelming shock wave swept him away, Cheongpung laughed aloud.

He watched the Red Blade shatter beneath the pillar of fire that had finally burst forth.

But he didn’t know.

At that very moment, one person was watching the blue-black flames dye everything around them.

Jin Taekyung’s face had gone colder than ever.

*Cough.*

His skin was deathly pale, his eyes growing cloudy.

Still, though he coughed up a whole bowlful of blood, Jin Taekyung forced his heavy eyelids open to watch the wave of fire he had unleashed.

He took in the clearest information in the world—the only information he could hear.

*Beep! Be-be-beep!*

He’d poured everything he had into it.

With a body emptied of strength and senses gone dry, he tried to understand what was happening.

But he couldn’t see or hear.

Not among the countless holographic windows floating in the air. Not amid the System warnings ringing without pause in his ears.

The clear chime announcing the enemy’s death never came.

Not even as his legs gave way, the spear shaft the only thing keeping him upright.

*Splash.*

And as Jin Taekyung’s knees plunged into a pool of blood—

*Drip. Drip.*

From within the wave of fire that had engulfed a radius of dozens of jang, the charred body of the monster stood up.

* * *

Thirst.

That was the first thing the Blood Lord felt when he regained consciousness.

*What the hell happened?*

He didn’t know. He couldn’t know.

He remembered nothing.

He couldn’t even recall who he was or what kind of life he’d lived.

Only the instinct to quench this terrible thirst remained, taking control of his body.

*Scuff.*

The sound of his unsteady footsteps was as dry as if he were walking through a desert.

Why was that?

The Blood Lord wondered blankly.

He’d been sure there was something somewhere around here that could quench his thirst.

He’d been sure of it.

*Why?*

He turned his head and looked around. But he couldn’t see anything. His senses had failed, his retinas burned away, trapping him in pitch-black darkness.

All he could make out was a faint sound.

……!

……!!

A strange noise.

Yes, he remembered. The sound of screams and steel clashing.

And then, from the unknown thing that touched his skin, came a feeling that was familiar—and strangely dear.

*Splash.*

At that moment, forgotten sensations and memories awoke.

Something hot, wet, and sticky.

The Blood Lord remembered what this utterly familiar thing was.

*Blood.*

Something inside the human body. The source of his strength—and the only liquid that could quench his thirst now.

*I’m thirsty.*

Strange. Just thinking it was enough for him to feel the blood splattered across his body seeping into him.

And with it, his senses gradually grew more vivid.

But—

*More. Give me more.*

This wasn’t nearly enough.

He needed far, far more blood.

“More!”

With the cry escaping his lips, the Blood Lord flung his hand out with all his strength.

*Grab.*

At last, his fingertips touched someone’s shoulder. At the same time, a voice rang more clearly in his ears, echoing like a distant sound.

“Blood Lord! We’ll protect you—!”

But before the desperate voice could finish, the Blood Lord’s teeth, already grown, sank into the man’s throat.

*Crunch!*

He chewed and swallowed.

For greater strength. To quench his thirst.

Only then did the world around the monster grow bright.
## Chapter artifact 1109

# Chapter 1109

The moment fierce flames swept through the area, there wasn’t a single person—ally or enemy—who hadn’t thought the Blood Lord was dead.

That was how much power the strike had contained.

Even with the Blood Lord’s near-immortal regenerative ability, surviving that dreadful, hellish heat had seemed impossible.

But there was one exception.

Jin Taekyung, who had summoned those flames by using even his own life as kindling.

*Splash.*

His knees crumpled into a pool of blood. Beyond the drifting ashes, the monster who had stopped just short of death began to rise.

And then, between Jin Taekyung’s lips, now pale as snow, burst a single shout, squeezed out with every ounce of strength he had left.

“Attack!”

The Azure Dragon’s Roar shook the world around them, breaking the momentary silence and setting time in motion again.

The first to respond was another Divine Dragon, still hurtling far away, swept up in the aftermath of One Annihilation.

“……!”

Cheongpung’s eyes flew open.

The thrill and elation that had filled his pupils just after he cut off the Black Ghost’s head were nowhere to be found.

Only overwhelming shock and confusion rushed in to fill their place.

*How is this even possible……!*

It was a reality he couldn’t believe.

But it was also one he had no choice but to accept. Gritting his teeth, Cheongpung twisted around.

*Whoosh.*

His body spun against the howling wind. As he did, the tip of his foot struck the empty air.

No—it burst through it.

*Boom!*

Compressed air exploded.

The distance of more than twenty jang closed in an instant, and the staggering monster loomed suddenly closer.

*I’ll kill him. No matter what!*

Cheongpung’s mind was cold as ice.

His instincts were screaming.

If he didn’t stop that terrible monster now, he might never get another chance.

He had to bring the creature down by any means necessary, before it recovered its original strength.

But what awaited Cheongpung’s descending sword as it cut through the wind was another group of monsters, known by a different name: fanatics.

“Stop him!”

“Heaven above and earth below; all demons—!”

*Sh-sh-sh-shhk! Slice!*

Purple Force flowed along the sword and cut through flesh and bone without hesitation.

Thirty-Six Plum Blossom Swords.

Huashan’s proudest technique filled the space. Along the path traced by his blade, the Force of the Zaha Divine Technique blossomed and scattered like petals.

Beautiful, and yet tragic.

And more than anything, utterly brutal.

*Thud! Fwoosh!*

He cut, and cut, and cut again.

They fell, and fell, and fell again.

But—

*They’re not backing down……*

Cheongpung’s face turned deathly pale.

Before long, everything around him was stained red.

Blood poured out without pause, washing away the fragrance of his sword technique and obscuring the purple Force.

And that wasn’t all.

The defenders who had joined the fight were swinging their weapons with the resolve to die, but even so, the wall of fanatics held firm.

To them, death—the thing every living person feared—was a sacred martyrdom.

“The great Lord of Heaven’s power has descended upon this land! We will give our lives to protect His Apostle!”

“Lord of Heaven, lead us!”

The fanatics’ spirits had never been higher than after witnessing the Blood Lord survive.

No—now it was something beyond madness.

To some, it was a strange and terrible calamity. But to the fanatics, it was a miracle proving their faith had been right all along.

And amid that whirlpool of madness and death, Cheongpung saw it clearly.

A monster slowly retreating from the jaws of death, absorbing the blood of friend and foe pouring in from every direction.

*Rustle.*

First, new flesh began growing from the body that had been charred black.

*Crack.*

Melted bone and muscle regenerated.

*Plop. Plop.*

Lips that had stuck together came apart, revealing sharp, white teeth.

Along with a long, blood-red tongue that flicked hungrily, driven by an unbearable thirst.

“……More. Give me more.”

The moment a voice like scraping metal slipped from the monster’s parched lips, Cheongpung felt the blood in his whole body turn cold.

*Already?*

It was a sight too bizarre to describe—and a recovery far too fast.

It was well beyond what he and the other allies had expected.

So much so that he wondered if they should retreat right now, even if only to delay the monster’s recovery for a little while.

But even in that fleeting moment, the mindless monster was regaining its original strength at an astonishing rate.

“More!”

The Blood Lord’s sudden cry sent a shiver down Cheongpung’s spine.

Was it because his voice had become much clearer and sharper?

No.

It was the majestic internal energy carried in that cry—something Cheongpung hadn’t been able to feel just moments ago.

*No!*

As a scream rang out in his heart, Cheongpung thrust his sword forward with all his strength.

*Sh-sh-sh-shhk!*

Force brighter and more powerful than ever tore through the space.

The fanatics blocking his way, endlessly chanting their eight-character incantation, were cut to pieces and scattered.

A breakthrough aimed at a single point.

Following close behind Cheongpung came Jeong Hogun and the Embroidered Uniform Guards under his command, who had joined the fight.

“Wipe out the rebels!”

“Long live His Majesty the Emperor!”

They were the Great Nation’s finest troops in name and reality, their ranks made up of martial artists from at least Supreme First Rate to Peak.

They had cast aside the golden armor and helmets bestowed by the Son of Heaven, but their dazzling pride and vows still shone. Their sword points were all aimed in one direction.

At the Blood Lord.

*Fwoooosh! Boom!*

A deafening crash sent a thick spray of blood surging through the air.

And a tiny crack began to form in the ranks of the countless fanatics, which had seemed like an unbreakable iron wall.

*Slice! Thud-thud-thud!*

Even with Temporary Strength Pills, they could not close the gap in martial enlightenment.

Dozens of Huashan’s finest techniques poured from Cheongpung’s blade, while the Embroidered Uniform Guards, led by Jeong Hogun, drove into the fanatics’ formation like an awl.

Before another enemy could fill the gap.

So they could get one step closer, one moment sooner, to the Blood Lord.

*If this keeps up, we can do it.*

No—they had to do it.

It wasn’t only Cheongpung who thought so.

They all thought so, and they were all prepared to die.

The Kunlun Sect Daoist who, even with a sword buried in his chest, used his last strength to grab hold of a fanatic.

The young, nameless soldier behind him, squeezing his eyes shut as he thrust his spear.

The middle-aged Embroidered Uniform Guard, pressing his spilling entrails back into his split abdomen as he advanced, clad in a pride brighter than his armor.

Every one of them instinctively knew.

If they let this chance Jin Taekyung had created slip away, they might never be able to bring that monster down.

If the West Gate fell, not only would they be slaughtered—the hundreds of thousands of people sheltering in the Inner City would be massacred, too.

Their unshakable, desperate resolve shot toward the wall of fanaticism like the spear of someone kneeling behind them.

“Now!”

At Cheongpung’s shout, every ally who had pushed deep into enemy lines squeezed out their remaining strength and lunged forward.

A life-or-death charge that might be their last—but one none of them would regret.

*Crack-crack-crack!*

Fountains of blood burst into the air.

Cries of pain spilled from every direction, and the bodies of allies and enemies alike tangled together as they crumpled.

But that was enough.

Countless fanatics still surrounded them, but at this moment, Cheongpung had only one target.

*Crunch. Crunch.*

The monster, chewing on something unknown—something he didn’t want to know—suddenly turned its head to look at Cheongpung.

It had two arms and two legs like a human, but could no longer be called human. In its red hand was a corpse with no head.

No—dozens of bodies already lay at the monster’s feet.

The fanatics’ corpses, dried up like mummies.

“Who are you?”

His expression and tone made it seem as though he truly wanted to know.

Cheongpung didn’t know why the monster couldn’t remember him, but one thing was certain.

*He still hasn’t fully recovered.*

Watching his reflection in those blood-red pupils, Cheongpung spat out his answer.

His voice held more hostility than ever.

“You don’t deserve to hear my name.”

And at that moment—

*Flash.*

Purple light burst from Cheongpung’s fingertips, which moved faster than sound.

*Slice!*

Skin split, and blood flew.

The Blood Lord stared at Cheongpung in bewilderment, then blinked as he noticed the deep gash across his chest.

“Ah, ah……?”

Along with the pain, forgotten memories began to rise slowly to the surface.

And with them came anger.

“You……”

His hand reached out as if he were entranced.

But before he could recover his memories, Cheongpung was already moving without hesitation.

*Slice, slice, slice!*

They moved at a speed like streaks of light, their bodies tangling and crossing. Each time they did, blood sprayed into the air.

More precisely, the Blood Lord’s blood.

*Drip-drip-drip.*

Watching his own blood spatter across the ground, the Blood Lord’s eyes widened.

“……No.”

It wasn’t the pain.

Thirst.

The more blood he lost, the more that terrible thirst—briefly quenched—tightened around him once again.

*Sh-sh-sh-shhk!*

Even as a storm of sword strikes rained down, the Blood Lord felt his thirst growing stronger and looked around.

*I need it. Blood. I need more.*

But despite that desperate desire, Cheongpung was squeezing out the last of his strength with every attack, giving him no time to quench his thirst.

*Thud! Crack!*

Blood was flowing everywhere as the battle went on, but it wasn’t nearly enough.

It could only patch up the large and small wounds appearing across his body, one after another.

But he had remembered something else he’d briefly forgotten.

Something very important to him—another source of blood that could quench his thirst.

*Right. That’s right.*

The Blood Lord grinned, unable to contain his joy.

Then he raised both hands toward the sky and cried out in an eager voice.

“Come! Hurry!”

At that instant—

*Whoosh!*

The purple Force Cheongpung had sent flying grazed the Blood Lord’s arm, frozen for a moment.

No—it cut through it.

*Slice!*

Both arms shot high into the air. At the same time, pain and thirst surged through him.

But even after losing the arms he had barely regenerated, the Blood Lord’s smile didn’t fade.

He knew.

The countless shadows plunging down toward him would quench his thirst. They blocked even the heavy rain pouring over his head at that moment, blotting out the already dark sky until it turned utterly black.

*Kiiieeet!*

At the bloodcurdling sound that suddenly rang out from the air, Cheongpung instinctively looked up.

And he saw.

No. Everyone saw it clearly.

Countless flying beasts—too many to count—plunged toward the battlefield, their blood-red eyes flashing.

And at the center, at the very end of them all, was one being.

*Flap-flap-flap!*

A wave of monsters that could neither be blocked nor avoided.

Beyond the thunder of countless wings beating as they poured down and covered the space, the voice of the monster who had finally regained all his strength and memories pierced Cheongpung’s ears.

“I remember your name.”

“……!”

“And the debt I owe that bastard, Mae Jonghak, the Sword Saint.”

At that moment—

*Crack-crack-crack!*

With a horrible sound of flesh and bone tearing, sticky blood painted Cheongpung’s vision red.

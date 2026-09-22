# Checkpoint Review — 635–639

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

# Chapters 635–639

## Plot

Jin Taekyung and Yayul Cheok pursue Ailao Mountain’s Wraith into the forbidden Poisonblood Grounds, a deadly region created by the former Five Poisons Sect. The grounds’ Poison Mist and venomous creatures kill past Nanman expeditions, including Baeksang’s grandfather. Jin resists the poison with his Myriad-Poison Ring and gives Cheok a poison-warding pearl before they press deeper.

They learn that the Nanman Beast Palace’s uncertain legendary treasure, the Beast King Stone, supposedly commands every ferocious beast and vanished after the founding conflict with the Five Poisons Sect. Jin and Cheok find a dead Bai warrior and are attacked by five Thousand-Year Spiders. Four spiders die, while the last lures them through prepared webs and summons thousands of venomous beasts. Jin destroys the swarm with One Annihilation and White Flame; Cheok tears off the spider’s leg, but its survival after the fall remains unresolved.

## Continuity

- Jin Taekyung and Yayul Cheok remain inside the Poisonblood Grounds, pursuing the injured final Thousand-Year Spider.
- Jin’s Myriad-Poison Ring protects him from the Poison Mist; Cheok relies on Jin’s High-Grade Poison-Warding Pearl.
- The Poisonblood Grounds was created by the Five Poisons Sect and contains lethal poison, unknown life-forms, countless dead spirits, and venomous beasts.
- The Beast King Stone is a possibly nonexistent Nanman Beast Palace treasure said to command all ferocious beasts. Its disappearance followed the battle between the First Palace Lord and the Five Poisons Sect’s founding Sect Leader.
- The Thousand-Year Spider is highly intelligent, commands local venomous beasts, prepares web-covered battlefields, and can spray corrosive slime. Four of five spiders are dead; the last lost a leg and fell, with its survival unknown.
- Cheok is the Bai people’s great chieftain and Palace Lord of the Nanman Beast Palace.
- The chain Quest **My Good Sir, Do Not Cross That Swamp** remains active; failure means death.
- Unresolved: whether the surviving spider can be killed, whether the Beast King Stone exists, and whether the Poisonblood Grounds or its beasts connect to the Ailao Mountain massacre or Dark Heaven.

## Translation Decisions

- Use **Poisonblood Grounds**, **Poison Mist**, **Beast King Stone**, and **Thousand-Year Spider**.
- Use **Myriad-Poison Immunity** for 천독불침 and **Mildly Poisoned** for 미약한 중독.
- Use **Beast Miao King** for 야수백왕 and retain **Yayul Cheok** as the Bai people’s great chieftain and Palace Lord.
- Use **One Annihilation** for Jin’s technique and retain **White Flame** for his summoned spear.
- Preserve the colloquial quest title **My Good Sir, Do Not Cross That Swamp**.
- Use **Sword Demon**, **two-headed horn snake**, **black frog**, and **golden bee**.

## Durable state

{
  "active_continuity": [
    "Jin Taekyung and the Beast Miao King confronted the last surviving Thousand-Year Spider in the Poisonblood Grounds.",
    "The Thousand-Year Spider deliberately lured them into a web-filled battlefield and summoned the surrounding venomous beasts as guards.",
    "Jin Taekyung used One Annihilation with White Flame, three jiazi of Scorching Yang Qi, and hellfire to destroy the summoned army.",
    "The Beast Miao King tore one of the Thousand-Year Spider's legs free after Jin cleared away its guards.",
    "The injured Thousand-Year Spider fell toward the ground, and its survival remains unresolved.",
    "Yayul Cheok is the Bai people's great chieftain and the Palace Lord of the Nanman Beast Palace."
  ],
  "continuity_sources": [
    639
  ],
  "open_questions": [
    "Did the Thousand-Year Spider survive the fall after losing its leg?",
    "Can Jin Taekyung and the Beast Miao King finish the injured Thousand-Year Spider?"
  ],
  "safe_through": 639,
  "temporary_decisions": [
    "Use Sword Demon for 검마.",
    "Use two-headed horn snake for 쌍두각사, black frog for 흑와, and golden bee for 금봉."
  ],
  "version": 1
}

## Reading copies

## Chapter artifact 635

# Chapter 635

*Ding.*

> **System**
>
> - **Ailao Mountain’s Wraith** has appeared!

Ailao Mountain’s Wraith.

A being and a name I had never seen or heard of before.

But before I could even process the new information, the colossal Black Tiger identified by the System as Ailao Mountain’s Wraith let out a thunderous roar.

*Gwaaaaaaaaaang!*

Its roar tore through the darkness and reverberated across the entire mountain. The air around us rippled like waves, while grass and branches shattered into pieces.

This was not the howl of an ordinary beast.

It was something primal—something that drew out the fear hidden deep within one’s heart and went on to shake the very soul.

And I was the person in this world who knew the true nature of that power better than anyone.

*Fear.*

I had realized it instinctively from the moment I met those blue-white eyes.

That the enormous beast that had appeared so suddenly was more than the word *beast* could ever encompass.

And the reason this sensation did not feel entirely unfamiliar was that I had encountered something resembling this creature a few months ago in Hubei.

*The Water God Dragon.*

The master of Dongting Lake, who had been driven insane and rampaged after losing its reason to Dark Heaven. A rare spiritual creature that had entered a new realm after several hundred years.

I sensed qi like the Water God Dragon’s emanating from the Black Tiger towering like Taishan, and I was not the only one who felt it.

*Whine…*

By ordinary standards, White Tiger was more than worthy of being called a spiritual creature, but it was no match for that intense Fear.

Unlike the creature whimpering like a frightened puppy, however, someone else stepped forward without the slightest hesitation.

“Was this your doing?”

*Boom!*

With a furious shout, the Beast Miao King kicked off the ground with all his strength. His body shot forward, covering more than ten zhang in the blink of an eye.

Radiant light burst from the fist he had clenched tightly.

*Whoooosh!*

A heavy sound split the air. Destructive Force coiled around his fist like thread, erasing everything in its path as it advanced.

And at its end…

*Slash!*

There was nothing.

Only empty space.

“……!”

“……!”

It had dodged the Beast Miao King’s punch—a blow from a Supreme Peak master belonging to the Ten Kings.

It happened in the blink of an eye. Having moved through the darkness like mist to evade the Beast Miao King’s attack, the Black Tiger swung its enormous front paw, black as night.

*Swish!*

Unbelievably fast.

And terrifyingly powerful.

*Boom! Crack-crack-crack!*

A tremendous shock wave swept in every direction with a deafening roar. The Beast Miao King was pushed back by the immense force delivered in an instant, his eyes widening.

“What the…?”

But he was not even given enough time to be shocked. A hungry predator standing before its prey did not hesitate.

*Gwaaaaaaaaaang!*

Another roar shook Ailao Mountain.

The people of this world were not accustomed to Fear. That might have been different in the modern world, where Gates and monsters had become common sense and everyday life, but not here.

And the Beast Miao King had been caught even more off guard because this was his first encounter with an existence so far beyond anything he had expected.

“Kh!”

It was only the slightest moment of paralysis. For the Beast Miao King, it might have been the best possible outcome, but life-and-death duels between people of great skill were decided by the opening exposed in a single instant.

That fact did not change merely because his opponent was a beast rather than a martial artist.

*Whoosh!*

In a world that seemed to have slowed, the Black Tiger’s claws—resembling hooks—were just about to tear through the air.

At that moment, a spear that had left my hand became a dazzling streak of light and tore across the space between us.

*Shreeeek! Boom!*

A deafening roar split the heavens, and the space within a radius of more than ten zhang shook violently.

Qi against qi.

Strength against strength.

And the victor of that brief clash was me.

*Crack!*

The Black Tiger’s enormous body, sent flying backward as though it had become one with the spear, vanished beyond the forest shrouded in darkness. Far away, dozens of giant trees clustered together snapped and swayed.

The mountain birds that had long since awakened and must have been watching us in silence took flight all at once, while countless leaves and branches poured down like a rain shower.

*Tap. Rustle!*

Now was the perfect time to catch it.

But I had barely begun chasing after the Black Tiger when I was forced to stop.

*Why can’t I sense it…?*

I could not feel its presence.

Not even a trace.

The only clues left behind were the wreckage scattered around as though a bomb had exploded and a spear lying on the ground with its blade shattered.

I could not find any footprints or bloodstains.

*Did it escape the range of my Qi Sense? And that quickly?*

As I glared into the surroundings, the Beast Miao King arrived alongside White Tiger and spoke with an expression mingling anger and shame.

“Where is it?”

“It seems to have run away. I can’t find it.”

“……Damn it. I made a fool of myself.”

“I understand. I really do. I’m not just saying that.”

Mungyeong and Jeok Cheongang had also been shaken, if only briefly, by the Fear emanating from the Water God Dragon.

The Beast Miao King was an incredible master worthy of being counted among the Ten Kings, but it was unreasonable to compare him with those two, who had reached a realm beyond humanity.

If anything, that meant he had broken free of Fear’s influence even more quickly than I had expected.

Perhaps it was because, as a native of Nanman, he had often encountered strange venomous beasts and ferocious animals from an early age.

In any case, what mattered most right now was…

“It’s still alive. There’s no blood, so it doesn’t seem to have suffered any significant injury.”

At my low voice, the Beast Miao King nodded.

“I thought so. When it realized it could not dodge, it bit down on the spearhead at the last moment. And that spearhead was clearly wreathed in Force. I’ve lived my entire life in Nanman, but I’ve never seen or heard of anything like that creature.”

“I don’t think that’s true.”

“What do you mean?”

“What you said at the end.”

Before the Beast Miao King could answer, I continued calmly.

“Even if you’ve never seen it, you must have heard of it. I’m sure of it.”

For now, we could not sense the creature’s presence, but there was no telling when it might leap out again.

The Beast Miao King, who had naturally placed his back against mine while keeping watch over the surroundings, stiffened.

“Could it be…?”

“You’re probably thinking of the right thing. Something similar happened in Hubei Province.”

“……Are you talking about that imugi?”

The Beast Miao King muttered the words like a groan, then continued.

“There was something about that in the letter I received from the Murim Alliance. But I privately thought it was an absurd story.”

“Are you really the Lord of the Nanman Beast Palace? Your only son is riding around on a White Tiger, and you couldn’t believe that?”

“He rides a White Tiger, not an imugi.”

“……Ah.”

Fair enough.

An imugi was something that appeared only in mythology. Even if the information had come from the Murim Alliance, it was only natural that he would have trouble believing it.

His short and decisive answer left me with nothing to say. Then the Beast Miao King suddenly opened his mouth.

“If that is the case, was that creature that just appeared also the work of the Southern Heaven Demon Empress—that witch?”

“I can’t say for certain. But it’s highly likely.”

There were too many suspicious points for me to flatly declare that it was not.

Although Ailao Mountain had once been the headquarters of the Five Poisons Sect, it had remained quiet for more than a hundred years. The sudden massacre that had taken place there, along with the power of the Black Tiger that had appeared out of nowhere, both seemed to overlap with what had happened to the Water God Dragon in the past.

*“Ailao Mountain’s Wraith.”*

What on earth was the creature’s true identity?

Where were the two hundred warriors who should still have been here, aside from the people now sprawled around us as cold corpses? And where were the ferocious beasts they commanded?

I was slowly scanning the area with a heavy gaze when—

*Grrr.*

White Tiger, which had barely recovered from the influence of Fear, suddenly lowered its body and raised its tail straight up.

The Beast Miao King and I realized what that meant and turned our heads reflexively.

Far away, the darkness was rippling.

*That’s…!*

Both the Beast Miao King and I had overlooked something while talking about other matters.

An animal’s sense of smell was dozens, even hundreds of times keener than a human’s. And tigers, which primarily hunted at night, possessed an equally powerful sense of smell.

Which meant…

*This creature’s sense of smell reaches farther than the range of my Qi Sense.*

The instant I realized that, the Beast Miao King and I kicked off the ground at the same time.

* * *

During the chase, I learned exactly why people called tigers mountain lords.[^1]

*Ah. Look at that fucking bastard.*

I stared at the black shape racing far ahead while silently swallowing a curse.

No matter how fast we ran along the winding mountain ridges, no matter how many cloud-shrouded, mist-covered peaks we crossed, we could not catch up.

With its tremendous strength, inexhaustible Stamina, and elusive movements, the creature stayed ahead of the Beast Miao King and me from start to finish. Even White Tiger—a spiritual creature that could boast some pretty impressive white fur—could not catch it.

No. White Tiger was growing increasingly anxious instead.

*It makes sense. Its opponent isn’t an ordinary tiger.*

The word *mountain lord* did not merely mean the king of the mountain. It was also a term for a mountain spirit. But that creature was not the spirit of Ailao Mountain.

It was its wraith.

No—perhaps it was closer to an even more ominous evil spirit.

And the sights I witnessed while endlessly chasing the Black Tiger only reinforced that thought.

“That damned beast…!”

His voice seemed to boil like molten lava. The Beast Miao King’s furious gaze was fixed on corpses whose limbs hung limp.

Deep valleys. The edges of cliffs. Ravines that must once have run clear but had now been stained black by poison…

The corpses of Nanman warriors lay along the path we were taking like signposts, and the stench of blood and decay carried on the wind was unbearable.

“How dare they? How dare they do something like this!”

A savage aura poured from the Beast Miao King’s entire body as he took in the horrific scenes flashing past us.

He was angrier at that moment than I had ever seen him, and his movements became that much rougher.

“You bastard!”

*Tap-tap—shreeeek!*

In an instant, his body shot forward at a terrifying speed and streaked toward the Black Tiger without hesitation.

But the opponent was a being known as Ailao Mountain’s Wraith. A direct confrontation might have been another matter, but the Beast Miao King could not match its natural physique and speed.

*Papat!*

Just as expected.

The Black Tiger had surpassed the limits of an ordinary spiritual creature. Rather than being caught, it widened the distance even further and soon vanished into a deep, dark valley.

It gave us a look as though to say, *Come and get me if you dare.*

*What?*

Only then did I slow down and look around.

Ancient trees and vines filled every direction, while the hot, humid air mixed with mist carried the distinctive stench of poison.

I did not know exactly where we were, but after running mindlessly in pursuit of the creature, I could at least guess that we had reached the heart of Ailao Mountain.

*This is…*

I had a very bad feeling.

A truly bad feeling.

Unlike me, who was gradually slowing down, the Beast Miao King charged straight into the valley. There was not even the slightest hesitation in his retreating figure.

“Great Hero Yayul, wait—!”

*Crack!*

I had no time to stop him. And even if I had, the Beast Miao King would not have listened.

A little anger could rouse a slackened mind. But anger that went beyond its limits could put the mind to sleep.

“Damn it.”

I muttered the curse under my breath and looked at White Tiger, which had suddenly grown quiet.

As though it had sensed the ominous signs already, it paced anxiously around the entrance to the valley where the Beast Miao King had disappeared. When its eyes met mine, it shook its head like a person.

“Was that supposed to mean it’s dangerous?”

*Grrr.*

“This guy’s pretty smart. We agreed for the first time. But there’s nothing we can do this time.”

*Grrr…*

“You don’t have to follow me, so turn back here. And if you meet your master or anyone else, tell them we’re here.”

It was intelligent enough to be counted among spiritual creatures, so I trusted that it understood me.

As Yayul Mok had done, I gently stroked White Tiger between the eyes, then stepped toward the valley.

Without a trace of fear.

With my head held high.

“……”

*I’ll be able to make it back alive, right?*

[^1]: *San-gun*, literally “mountain lord,” is a traditional epithet for a tiger and can also refer to a mountain spirit.
## Chapter artifact 636

# Chapter 636

The valley was narrow and dark. Ancient trees of unknowable age grew thickly enough to block out the moonlight, while strange plants and creatures I had never seen before covered every direction.

And some of them were quite aggressive.

*Hiss!*

I was using my movement technique when I suddenly reached out. Something that had shot up from the grass like lightning writhed in my grip.

*Crackle. Crackle!*

*What is this? A snake?*

After taking a closer look, I realized I was only half right.

It was a snake, but not an ordinary one. The horns growing from either side of its triangular head were proof enough.

Wait. Haven’t I seen this somewhere before?

I stared intently at the snake and muttered under my breath.

“Mimi… No, a Thousand-Year Poison Horned Snake?”

*Crackle.*

Why was this thing here? Wasn’t the Thousand-Year Poison Horned Snake supposed to be one of the rarest venomous creatures in the world?

*Now that I look at it again, it seems a little different.*

*Is it because this is basically China? There are knockoffs everywhere.*

Compared to Mimi, its body was larger, but its sheen and horns were inferior.

I stared at the snake in my hand with disbelief, then threw it into the distance and picked up speed. Whether it really was a Thousand-Year Poison Horned Snake or not, one thing seemed certain: just as I had guessed, this valley was not a safe place.

*Just as I thought. Is this a trap?*

Perhaps because I had wasted a short amount of time before entering, the Black Tiger and the Beast Miao King were already far ahead.

The one fortunate thing was that, unlike the Black Tiger—which left no footprints, as though it really were a wraith—the Beast Miao King’s tracks remained here and there.

*Swish, swish, swish!*

After running like that for about seven minutes, I spotted a vast swamp drawing closer in the distance, along with a familiar back standing at its center.

I shouted.

“Great Hero Yayul! Stop! Stop charging in headfirst!”

“……I had already stopped.”

The Beast Miao King was telling the truth. His face was still twisted with anger, but he was standing perfectly still, with the corpses of venomous creatures and ferocious beasts scattered around him.

“What happened here?”

“They suddenly attacked from every direction like mad. I lost sight of it because of them.”

Humans and beasts alike knew better than to recklessly attack someone stronger than themselves. If anything, beasts with sharper instincts were even more cautious.

And yet, they had still blocked the Beast Miao King’s path.

“Could it have been for that creature’s sake?”

“I don’t know. But whatever the reason, it isn’t strange. This land has always been like this. It was probably the same a hundred years ago, and two hundred years ago.”

It was a strange answer. He sounded as if he had known about this place from the beginning.

When I gave him a questioning look, the Beast Miao King continued with a stern expression.

“In the past, unlike the other tribes, the Five Poisons Sect focused on raising venomous beasts rather than ferocious animals.”

Poison was scorned everywhere, but in truth, it was one of the most efficient weapons in existence.

That was even more true from the Five Poisons Sect’s perspective. They had turned all of Nanman except themselves into enemies and had to fight opponents who outnumbered them by at least dozens of times.

“The place they created for that purpose was called the Poisonblood Grounds.[^1] A place where the most savage and vicious beasts and venomous creatures in all of Nanman—and even the entire world—ran rampant. The most lethal yet secret legacy left behind by the Five Poisons Sect.”

“Then does that mean this is…”

The Beast Miao King gave a small nod.

“This is the Poisonblood Grounds.”

“Huh. No wonder there wasn’t even a path. But it doesn’t seem as dangerous as you made it sound. I can still breathe.”

Of course, I had encountered a knockoff Thousand-Year Poison Horned Snake on the way here, and poisonous air had seeped into me like carbonation with every breath in and out, but I had been more or less fine so far.

That changed after I heard the Beast Miao King’s next words.

“It would be. We are only in the outskirts of the Poisonblood Grounds. This is barely the entrance.”

“The entrance?”

“According to the records, around a hundred years ago, only the finest elites from each Nanman tribe were selected to enter the Poisonblood Grounds. They carried hundreds of jars filled with lamp oil and held poison-warding pearls in their mouths. What do you think happened?”

“I doubt they all returned safely and lived happily ever after.”

“Not a single person returned. Everything came to nothing after that, and it is the main reason Ailao Mountain has remained a forbidden land to this day.”

I followed the direction of the Beast Miao King’s pointing finger and saw a massive swamp stretching for hundreds of zhang.

I gazed blankly at the mist resting over it, then cautiously opened my mouth.

“By the way, is the fog around here usually green?”

“Of course not. Fog is usually white.”

“That one is green.”

“Ah. That is because it is poisonous mist.”

“……”

For a moment, I was thrown off by how naturally he said it, as casually as a mother announcing, “We’re having soybean-paste stew for dinner tonight.” I forced myself to remain calm and asked,

“……Where exactly have you brought me?”

“The Poisonblood Grounds.”

“……”

*For fuck’s sake. He calls that an answer?*

At my utterly disbelieving stare, the Beast Miao King smacked his lips.

“I only found out after entering. The records did not state the exact location of the Poisonblood Grounds.”

It was a goddamn mess. As I wondered whether White Tiger could bring the others this far, I asked,

“Then what is deeper inside?”

“How would I know? Everyone died.”

“That’s incredibly reassuring.”

“Baeksang’s grandfather, who had been the Palace Lord of this Palace at the time, also died there. I heard he was the strongest warrior in the history of the Bai people.”

The position of Palace Lord of the Nanman Beast Palace was not passed down through a single family in an entirely hereditary succession.

Yayul Mok was only the nominal Young Palace Lord. If the position of Palace Lord became vacant, a tribal council would be held, and one of the great chieftains from the four most powerful tribes would be elected as Palace Lord by vote.

“Was he stronger than Great Hero Yayul?”

“That is impossible to know. The standards for strength are always changing. But if he had lived in the same era as me, it would not have been strange for there to be a Beast Bai King instead of a Beast Miao King.”

Judging by how highly the Beast Miao King spoke of him, Baeksang’s grandfather had clearly been at least a Supreme Peak master by Central Plains standards—someone who had opened the Middle Dantian, if not gone beyond that.

*The problem is that a master of that level was wiped out in the Poisonblood Grounds alongside Nanman’s elite warriors.*

*And the even bigger problem is that I have to go in there now.*

But still…

“We’ve come all this way. We can’t turn back now. Let’s go.”

At my calm declaration, the Beast Miao King looked surprised.

“That is unexpected. I thought you would suggest turning back.”

“Someone once said that if a man draws his sword, he should cut through even the Poisonblood Grounds.”

“……Who said that?”

“I did.”

The Beast Miao King stared at me with a dubious expression, then broke into a grin.

“Elder Jeok raised his Disciple well.”

“Well, if we’re being technical, it was years of violence and oppression… But what’s the point of going into every little detail? No matter what I say, Great Hero Yayul won’t listen anyway.”

“Is that something you say?”

*Crack.*

A sound like bones grinding out of alignment rang from the Beast Miao King’s tightly clenched fist. A chill entered his voice.

“I am the great chieftain of the Miao people, but I am also the Palace Lord of the Nanman Beast Palace. I have to collect the blood price for them.”

Perhaps this was why he had been able to become the Palace Lord of the Nanman Beast Palace.

As I looked at him in a new light, the Beast Miao King suddenly spoke.

“Thank you. For helping me.”

“What else could I do? People died. I couldn’t leave you here alone and turn back.”

“Even if there were no Dark Heaven inside, would you still do it?”

“I’m not such a coward.”

A faint smile formed at the corner of the Beast Miao King’s mouth.

“I have heard that people in the Central Plains call men like you chivalrous heroes.”

“People who dislike me usually call me a fucking bastard. I mostly get called a lunatic.”

Those were undeniable facts, so I was not offended. Besides, most of the people who had called me those things had died by my hand.

That was why people always had to watch their mouths.

*A chivalrous hero.*

I still did not know whether I was truly one.

I had simply ended up here after starting something, and somehow people had begun calling me that.

*A chivalrous hero in the Central Plains. A hero in the modern world.*

But what did that matter? Whatever other people called me, I had always done what I wanted. Dark Heaven had merely been an especially loathsome existence among the things I disliked.

*Fine. Let’s face it. Whatever is in there.*

I might not have had a chance alone, but with the Beast Miao King beside me, we had a chance—even if the Southern Heaven Demon Empress herself was waiting inside.

*Step.*

I had just finished my thoughts and followed the Beast Miao King into the swamp shrouded in deep green poisonous mist when—

*Ding. Ding. Ding.*

> **System**
>
> - **Quest condition:** **Investigate Ailao Mountain Within the Time Limit** has been completed!
>
> - **Unexpected Quest:** **Unknown Omen** has been successfully completed!
>
> - Quest completion rewards have been granted!
>
> - A small amount of **EXP** and **Fame** has been acquired!
>
> - **High-Grade Antidote** ×20 acquired!

The System notifications rang out without warning. But they were not over yet.

*Ding.*

> **System**
>
> - You have entered the hidden location, **Poisonblood Grounds**!
>
> - **Poisonblood Grounds** is the most secret location created by the former Five Poisons Sect. Countless venomous creatures were raised here, and deadly poisons for which no antidote existed were created.
>
> - You have achieved the extremely rare Achievement **How’d You Find This?**
>
> - You have acquired a **High-Grade Poison-Warding Pearl** as an Achievement reward!
>
> - A Chain Quest has been created!
>
> - Would you like to accept the Quest **My Good Sir, Do Not Cross That Swamp**?

“……”

*For fuck’s sake. Look at that goddamn quest title.*

I stared sourly at the holographic window. The longer I looked at it, the less I wanted to answer. In the end, I nodded.

> **System**
>
> - Quest **My Good Sir, Do Not Cross That Swamp** has been accepted!

And at the exact moment I instinctively sighed in the deep green poisonous mist, I realized.

*Beep.*

> **System**
>
> - The penalty effect of **Poison Mist** has activated!

“……!”

Something had gone seriously wrong.

*Beep! Beep! Beep-beep-beep!*

> **System**
>
> - Poison permeating the air is entering your body through your respiratory tract and skin!
>
> - Due to your traits, **Myriad-Poison Immunity** and **Scorching Yang Qi**, the penalty from **Poisoned** has been reduced!
>
> - You have been afflicted with the **Mildly Poisoned** status abnormality!
>
> - All stats have decreased by 10!
>
> - If **Mildly Poisoned** persists for a certain length of time, the penalty effect will increase and may even result in death!

“……”

I had been poisoned just from sighing once?

And if poison could enter through my skin, that meant I would get poisoned even if I stopped breathing.

*What the fuck kind of bullshit is this?*

It was absurd from the start, but I put up with it. Fortunately, I happened to have an item that was especially effective in situations like this.

*Open Inventory. Summon.*

I took out a ring set with a gleaming black jewel. The moment I put on the sacred treasure of the Sichuan Tang Clan, the Myriad-Poison Ring, a System notification announced that my status abnormality had been removed, and the heaviness that had briefly settled over my body vanished.

*Just as I thought.*

I smiled contentedly and stroked the Myriad-Poison Ring. Then I noticed someone silently glaring at me and flinched.

“Oh. You startled me. What is it?”

“……Hngh. Poison. Hngh. Don’t talk to me. Hngh.”

Oh, right. He was here too.

I gave the Beast Miao King a flat, chilled stare and tossed him the High-Grade Poison-Warding Pearl I had received as the Achievement completion reward.

[^1]: *Dokhyeolji*, literally “poison-blood grounds,” the name given to this deadly region by the Five Poisons Sect.
## Chapter artifact 637

# Chapter 637

This was a first.

The first time I had crossed a swamp this long and wide.

The first time I had fought things that weren’t human while breathing Poison Mist like ordinary air.

*Splash!*

A sudden sound rang out behind me. I smoothly pivoted and brought down my straightened hand like a blade.

*Slash!*

Even its visible body length alone was easily more than three zhang.

But neither its sharp teeth nor its armor-thick hide could stop the qi imbued in my knife-hand.

The enormous crocodile looked like something I might have seen in a documentary about the Amazon. It split in half and fell onto the blackened surface of the water.

*Splash!*

A fishy scent of blood and an even more vile stench wafted out, but I only felt nauseated for a moment. It was much more bearable than I expected.

That was because I had already been covered from head to toe in slime and blood that smelled worse than sewage.

*This isn’t exactly fighting fire with fire.*

Nanman Life Pro Tip: If you’re worried about a bad smell, get used to an even worse one.

“……Fuck.”

I briefly came back to reality, but the Poisonblood Grounds, shittier than a two-shift loading-and-unloading job, didn’t even allow me a short moment of clarity.

*Swish!*

A snake hidden in the marsh shot toward my neck like an arrow.

And the moment the creature exposed its black, razor-sharp fangs and opened its jaws wide toward my thigh—

*Whack!*

Thick fingers, like the branches of a great tree, blew away its triangular head.

There was no doubt it was dead. The Beast Miao King grabbed the snake’s limp tail, slammed it into the swamp, and spoke with a serious expression.

“Dohn’ led yer gar’ down.”

“Don’t let my what?”

“Be gareful.”

“……Ah. Right.”

Roughly translated, he meant, Don’t let your guard down. Be careful. Something like that.

Nanman’s greatest warrior, now over eighty years old, was speaking less clearly than an eight-year-old because his mouth was stuffed with the poison-warding pearl.

“Almos’ dere.”

That pronunciation sounded awfully familiar.

I wanted to ask if his hometown was somewhere around Gyeongsang-do, but I held back. Not only was this no time for that, the swamp really was coming to an end, just as the Beast Miao King had said.

That didn’t mean our situation had improved, though.

*Open Quest Window.*

*Ding.*

> **System**
>
> **Quest**
>
> **My Good Sir, Do Not Cross That Swamp**
>
> You have entered the Poisonblood Grounds.
>
> In Ailao Mountain, once the headquarters of the former Five Poisons Sect, this place was hidden more deeply and secretly than anywhere else. Unknown and undiscovered life-forms dwell here.
>
> A cursed land filled with poisonous mist and the spirits of countless dead.
>
> No one can tell you what awaits you beyond this point. You have no choice but to see it with your own eyes and find out.
>
> **Grade:** Supreme Peak
>
> **Restriction:** Jin Taekyung
>
> **Mission:** ???
>
> **Reward:** ???
>
> **Failure:** Death

“……”

No matter how many times I looked at it, this was ridiculous.

It had been a long time since I had seen a Quest window this concise. The mission and reward were both unclear, but if I failed, I was definitely fucked.

Then again, it had always been similar. It had been the same in the modern world’s Gates, and it seemed to be the same after I came to the Murim.

*Win and live. Lose and die.*

It was a simple yet brutal logic.

Hunters and Murim practitioners alike were people who always lived with one foot in the Sanzu River.[^1]

And just as I had until now, I had no intention of dying this time either.

*Splash.*

When the swamp ended, relatively soft ground appeared. Every time the foul-smelling slime fell to the ground in the wake of my and the Beast Miao King’s footsteps, I could see the already blackish earth around us becoming even darker.

“Vile.”

The Beast Miao King spat out the poison-warding pearl and continued as he looked around.

“This is only the second place this horrible I’ve seen in my life.”

“What was the first?”

“The Great Faction War. Everywhere we went, hell was spread before our eyes.”

Since he was comparing this place to a war in which hundreds of thousands of people had killed one another, there was no need to elaborate on what kind of place the Poisonblood Grounds was.

*Fwoooosh.*

Poison Mist rolled toward us, covering the earth that had been dyed completely black. The Beast Miao King swallowed a groan at the grim sight.

“Damn it. If I had known this would happen, I should have trained in poison arts when I was young.”

“You didn’t know this would happen. Isn’t that why you didn’t learn them?”

The Beast Miao King nodded regretfully.

“That is true. I thought my own martial arts would be enough. That was also why I never learned the beast-taming techniques everyone else studied.”

“That makes sense. Why learn something you don’t need?”

I suddenly felt a strange sense of kinship.

If the modern world had people who gave up on math and people who gave up on English, Nanman had people who gave up on poison and people who gave up on beast taming. For the record, I had given up on every subject when I took the college entrance exam.

“Come to think of it, I thought people from Nanman all learned poison arts by default.”

“If that were true, wouldn’t this be the Nanman Poison Palace rather than the Nanman Beast Palace?”

“……Oh.”

“That is a prejudice held by people from the Central Plains. It is true that the nature of Nanman’s land means we encounter poison easily, but most tribes primarily deal with ferocious beasts. After the Five Poisons Sect rose to power, we rejected poison even more strongly. You can tell just by looking at the sacred treasure passed down through our Palace for generations.”

“Oh. Is that so…… Wait?”

What did he just say?

I stopped for a moment and stared at the Beast Miao King. He frowned and looked back at me.

“What?”

“No, it’s what you just said.”

“That we came to reject poison arts? For a Palace that suffered such severe damage, it was only natural.”

“Not that. I mean the sacred treasure. The sacred treasure.”

“Ah. That was what you meant. I thought you were asking about something else.”

The Beast Miao King answered as if it were nothing, but from my perspective, it wasn’t something I could simply brush off with an *Oh, I see.*

“The Nanman Beast Palace had a sacred treasure?”

“Any faction with a long tradition should have at least one sacred treasure. Judging by what I have personally seen and experienced, that is even more true of the Central Plains.”

He wasn’t wrong. Even small- and mid-sized sects, not to mention ordinary martial arts schools in the neighborhood, hung up an old iron sword and called it a sacred treasure to give themselves an air of importance.

But among those objects, there were also things that truly deserved to be called sacred treasures.

The Green Jade Buddha Staff, the sacred treasure of Shaolin Temple—the Mount Tai and Northern Dipper of the Murim, whose lineage had continued for a thousand years—was one such object.

And for some reason, Dark Heaven was targeting those very sacred treasures.

They had even caused the major incident known as the Shaolin Bloodshed to do so.

*But there was a sacred treasure like that in the Nanman Beast Palace too?*

As far as I knew, the history of the Nanman Beast Palace stretched back more than three hundred years.

This Outer Lands faction, formed through the alliance of dozens of tribes, had emerged from its struggle against the Five Poisons Sect and become the ruler of Nanman after a long war.

There was nothing strange about it having a sacred treasure or two, but……

The important thing was that I was only hearing about something this important for the first time.

“I’ve never heard that the Nanman Beast Palace had a sacred treasure.”

The Beast Miao King nodded at me as I forced myself to speak calmly.

“Of course not. It disappeared not long after the Palace was founded.”

“What?”

“Actually, it might never have existed in the first place. The existence of the Beast King Stone is a story passed down from Palace Lord to Palace Lord like a legend. We cannot even be certain that it was real.”

“The Beast King Stone……”

Its name alone was extraordinary. The Beast Miao King nodded at my quiet murmur and continued.

“As I said, it is a legendary tale. A sacred treasure said to have been carried by the First Palace Lord, one that could make every ferocious beast under heaven obey him. It supposedly disappeared after the First Palace Lord and the founding Sect Leader of the Five Poisons Sect grievously wounded each other in battle.”

A single pebble supposedly held the miraculous power to rule over every ferocious beast under heaven. It was nothing short of a legend.

And it was a story passed down by word of mouth for hundreds of years.

If I started working on it right now, then in a few hundred years, I could insist that I had been born from an egg.

*Well, I still have to keep the existence of the Beast King Stone in mind……*

For now, though, it was far more credible that the Southern Heaven Demon Empress intended to create a “rift” in Nanman than that her goal was the Beast King Stone, a legendary object whose existence was not even certain.

“Come to think of it……”

“Yes?”

The Beast Miao King suddenly spoke. He looked back and forth between me and the Poison Mist, then continued hesitantly.

“That. Do you have another one?”

The “that” he was referring to was none other than the Myriad-Poison Ring.

I answered firmly.

“No.”

“Then let me borrow it for a moment……”

“Hey, Mr. Yayul. Cut the nonsense and hold the poison-warding pearl in your mouth.”

“……What did you just say?”

“Ah. My tongue slipped for a moment. If you don’t want to get poisoned, keep the poison-warding pearl in your mouth.”

The Beast Miao King shot me a displeased look, but then put the large poison-warding pearl in his mouth without another word.

Though he held the lowest seat, he was still a master powerful enough to belong among the Ten Kings.

With martial prowess that had reached such a lofty realm and vast internal energy, he was not likely to succumb easily to poison. But a minimum level of prevention was always necessary.

*A High-Grade Poison-Warding Pearl should keep most ordinary poisons from penetrating.*

Of course, there was no need to mention me, since I was wearing the sacred treasure of the Sichuan Tang Clan—the Myriad-Poison Ring.

The Beast Miao King looked at me enviously before stepping into the Poison Mist.

*Step.*

The sound of his footsteps echoed unusually loudly.

The deep green mist covering every direction was so dense that I could not see even an inch ahead, and yet the surroundings were strangely quiet.

*As if something is watching its prey.*

It was strange. I could feel the gaze of something looking at us through the dense Poison Mist, and yet the area was quieter than it had been in the swamp.

And I was not the only one who sensed the atmosphere.

—A small patch of grass ten or so zhang away, to the northwest. Do you sense it?

A Sound Transmission pierced my ear. I gave a small nod.

—The grass beside the rock?

—Yes. There is something there. Could it be……

I thought of Ailao Mountain’s Wraith. The ghostlike presence I had felt from it, and its ray-like movements.

—It isn’t the wraith. Even if it were, we couldn’t catch it from this distance.

—That depends on how we go about it.

At the same time, the Beast Miao King thrust out one palm like lightning.

*Boom!*

Compressed air exploded, and the thick mist scattered for a brief instant.

Beyond the temporarily brightened field of vision, I saw the powerful palm force sweep through the grass like a storm.

And then……

“Guh!”

There was a scream. Not the cry of a beast, but unmistakably the scream of a human.

“……!”

“……!”

Our eyes widened as we looked at each other. Then the Beast Miao King and I shot toward the source of the scream with lightning speed.

*Whoooosh!*

In the brief instant it took to cut through the mist, countless thoughts flashed through my mind.

But the first two words that came to me were Dark Heaven.

*It’s them.*

Who else could be inside Ailao Mountain, the forbidden land of Nanman—and specifically the Poisonblood Grounds?

Something sharp seemed to pierce through my entire body.

Feeling my heart pound violently, I closed the distance of more than ten zhang in an instant.

And the moment I confirmed the owner of the scream who had been flung out of the grass, a dazed voice slipped from my lips.

“What the hell……?”

Dark red blood stained the corner of his mouth. His eyes were wide open.

There was no doubt that he was a human corpse, but he was wearing clothing that was painfully familiar to both me and someone else.

“……Why is a Bai warrior here?”

Like the Beast Miao King’s hollow voice, filled with confusion, the identity of the corpse that had been alive only moments ago was none other than a Bai warrior.

His body, dressed in white garments like a burial shroud, had been tightly wrapped in something sticky and tough.

*Rope. No, thread?*

In a situation I could not begin to understand, the Beast Miao King and I stared wide-eyed.

That was when—

*Rustle. Rustle-rustle.*

When had they gotten there? Where had they been hiding?

Along with the countless presences approaching from every direction, I suddenly felt darkness settle over my head. I looked up.

And at last, I saw them.

*Hissss!*

Some beings descended like ghosts from a tree so enormous that it was impossible to guess its age.

They had black bodies, countless legs, and stiff hair covering them. The Beast Miao King discovered them and muttered like he was groaning.

“……Thousand-Year Spiders.”

The monster of the Poisonblood Grounds had appeared.

[^1]: The Sanzu River is a Buddhist river associated with the boundary between life and death.
## Chapter artifact 638

# Chapter 638

Spiders?

I’d seen more than enough of them in my life. Even during the war-torn Great Cataclysm, all kinds of bugs had stubbornly survived inside Hope goshiwon[^1]—and spiders had been among its most regular guests.

[^1]: A goshiwon is an inexpensive Korean housing arrangement consisting of extremely small rooms with shared facilities.

Jin-ho hyung had even said this once:

> “Could the landlord of this building be Fabre, by any chance?”

The kind of insect density that could make you believe an entomologist dead for nearly two hundred years had been brought back to life.

But someone once said that humans were creatures of adaptation.

At first, I had been disgusted by the spiders that appeared at all hours of the day. Before even a year had passed, I had grown used to them, and a few years later, I had developed enough expertise to identify different species.

> “Hyung, say hello. This one’s a ghost spider. The one next to it is a Joro spider.”
>
> “Enough with the greetings. I know what they are, so get them away from me.”
>
> “And this one’s a Brazilian wandering spider.”
>
> “I said get it away—wait, why the hell is a Brazilian wandering spider wandering around Hope goshiwon? Does this situation make any sense?”
>
> “It’s not like it can’t make sense. I fought a goblin yesterday.”
>
> “Ah.”
>
> “And this one’s a tarantula. Looks like it just moved in.”
>
> “Is this a nightmare? Why on earth is there a tarantula…?”

What a mysterious goshiwon ecosystem.

I had spent the flower of my youth there among countless spiders, and eventually, I had lived alongside them like neighbors.

But I could say this with certainty: I had never seen anything as hideous or enormous as the spider that had just appeared before my eyes.

“……A Thousand-Year Spider?”

The unfamiliar name that slipped between the Beast Miao King’s lips was one I had never heard before, and the creature itself was on an entirely different level from a tarantula or a Brazilian wandering spider.

*What the hell is that……*

If someone asked whether I had ever seen a spider bigger than a bear, I would nod without hesitation.

Because I was looking at one with my own two eyes.

Five of them, in fact.

*Skritch, skritch!*

Their movements were ghostlike. Every time their eight stiff, hair-covered legs moved, their enormous bodies slid along the trunks of the great trees.

Then, the moment our reflections—rapidly drawing closer—appeared in the eyes of the monsters, both large and small, the Beast Miao King shouted like a thunderclap.

“It’s coming!”

And the next moment—

*Shhhhhaaa!*

Pale, viscous slime poured down from overhead and covered a radius of more than ten zhang.

Thanks to the Beast Miao King’s warning, I had barely escaped the attack’s range. When I looked at the scene unfolding before me, my eyes widened.

*Hissss!*

The ground, the rocks, the grass—even the unidentified Bai warrior’s corpse that we had been forced to leave behind—

Everything touched by the slime was melting away with a foul stench, as though someone had poured acid over it.

*Acid?*

If I hadn’t dodged it despite not knowing what it was—or if even a little had touched me—the slime might have instantly melted away part of my body.

Just looking at it sent a chill down my spine.

But our current situation was not favorable enough for me to stand around being shocked.

*Skritch, skritch!*

Between the thick grass.

Beyond the dense mist.

Atop the great trees that hid even the sky.

Five venomous spiders, each larger than a bear and indescribably hideous, were closing in around us from every direction.

“……Are they forming a perimeter?”

The Beast Miao King answered my incredulous mutter as he raised his internal energy.

“Among the countless venomous beasts of Nanman, the Thousand-Year Spider is called a king. More than being ferocious, it is a cunning creature. There is even a record of a thousand warriors once trying to exterminate one, only for it to kill half of them over ten days and nights before vanishing.”

“What do you mean, it’s just a spider? No, wait. They’ve been around for a thousand years, so I suppose that makes sense.”

“They are called Thousand-Year Spiders because they are capable of living for as long as a thousand years. No one knows how old those creatures truly are. The simultaneous appearance of multiple ones like this may also be a first.”

Countless venomous beasts existed in Nanman.

And yet, five monsters called kings had appeared all at once.

I looked at the slime that was still melting everything around us and muttered inwardly.

*Damn it. We really walked right into this.*

The corpses of the remaining Nanman warriors that we had failed to find.

I thought I understood why the ferocious beasts they had commanded had vanished without a trace.

After filling their bellies to some degree through hunting, they must have carried the corpses deeper into the Poisonblood Grounds to stockpile food.

*Bound tightly in spiderwebs, just like the Bai warrior who died earlier.*

They were certainly planning to hunt us the same way.

But—

*That’s what you think.*

I stretched my empty hand into the air as the creatures closed their perimeter with a horrifying sound.

*Open Inventory. Summon.*

*Ding.*

In response to my command, the limitless warehouse with no known end opened its doors by itself.

Among the countless weapons I had collected in preparation for emergencies, my hand closed around a spear radiating a pure white light.

“Did I just see something wrong……?”

“You did. It’s a three-section folding spear, so I usually keep it in my sleeve.”

Leaving the Beast Miao King behind as he stared at me in disbelief, I sent my internal energy into the White Flame spearhead hanging at an angle.

*Fwoooosh.*

Flames of tangible qi bloomed over the spearhead, which radiated a chilling sharpness.

As the blue flames kindled by Scorching Yang Qi flickered, the dense Poison Mist surrounding us and the five Thousand-Year Spiders that had marked out positions around us and were slowly tightening their noose both flinched as though they had been burned.

*Hissss.*

Their cries and movements were filled with caution. Their eyes, black like beetles and varying in size, darted rapidly in every direction.

But it was too late to retreat now.

For them.

For us.

The die had already been cast. All that remained was for one side to live and the other to die.

And the ones being hunted here today would not be us.

“What are you waiting for?”

I aimed the spearhead, its blue flames wavering, and continued.

“Get in here already.”

Those words were the signal.

*Shhhhhaaa!*

Toward the waves of pale slime pouring down from the front, back, left, right, and the air overhead, the Beast Miao King and I shot forward, cutting through space.

*Whoooosh!*

The wind brushed past my entire body.

The venom that had seeped in through my respiratory tract and skin weakened helplessly, while the flames surging around the silver spearhead blazed even more fiercely.

*Now.*

*Fwoosh! Kwoooong!*

With a single swing.

The horizontal strike I unleashed in a circle from where I stood caused the slime falling from every direction to evaporate as it grazed past.

And before that, the Beast Miao King’s fist had already shot through the air.

*Boom! Hissss!*

With a tremendous explosion, the slime burst in every direction.

An acidic downpour covered a radius of several dozen zhang.

But the Beast Miao King and I, unharmed down to the tips of our hair, continued forward without hesitation, leaving everything melting behind us.

*Whoooosh!*

The Beast Miao King headed toward the Thousand-Year Spider blocking his path.

I headed toward another one clinging to a great tree in midair.

We had made no agreement and formed no plan, but the glance we exchanged in that brief instant was enough for us to understand each other’s intentions.

*Grab.*

A large palm caught the tip of my foot just as I kicked off into the air.

The muscles in the Beast Miao King’s arm rippled, making his age of more than eighty seem meaningless. With a thunderous roar, tremendous strength launched my foot away like a shot put.

“Go!”

*Whoooosh!*

I felt weightless throughout my entire body.

I shot into the air faster and more powerfully than ordinary Stepping on Empty Air could ever compare to, and before I knew it, I was hurtling straight toward the face of a massive monster with eight legs.

—……!

A multitude of emotions could be read in its many eyes, both large and small.

I brought the spearhead down toward the Thousand-Year Spider, which was staring at me in shock almost like a human.

*Swish! Slash!*

A streak of flame cut across the air, followed by a spray of sticky blood.

At the same time, the Thousand-Year Spider that had sacrificed three of its eight legs—each harder than steel—to survive hurriedly spat out slime.

*Splatter! Hissss!*

Thanks to the Scorching Yang Qi that countered the poison and my quick movements, I avoided the slime.

But the distance had been too close.

The pain that flared up just from it brushing against my skin and clothes was scorching.

Instead of groaning from the pain, however, I took advantage of the opening and drove the spearhead into the creature’s enormous body as it tried to flee.

*Crack! Thrust!*

Unlike ordinary insects, spiders are arthropods with thin exoskeletons, so their bodies are not especially hard.

No matter how much the Thousand-Year Spider was called the king of venomous beasts, it could not block Force.

“Fuck, you think I’ve only killed one or two spiders? If you’d lived in Hope goshiwon, your whole extended family—in-laws and eighth cousins included—would’ve died by my hand.”

—Kiiiiiieet!

The enormous body writhed with a scream.

I avoided the slime that shot toward me again, then grabbed and tore off the leg swinging toward my side with my bare hands.

*Crack!*

—Kieeeet!

I might have fallen for it once, but I would not fall for the same trick twice.

The Thousand-Year Spider was no longer merely struggling—it was convulsing. I drove the spearhead down into its head.

*Thrust!*

The legs that had been moving aimlessly lost their strength, and the enormous body stiffened.

At the same time, a notification followed, turning my guess into certainty.

*Ding.*

> **System**
>
> - Defeated **Lv. 117 Thousand-Year Spider**!
> - Gained a substantial amount of **EXP** and **Fame**!
> - **Thousand-Year Spider** is a special existence among countless venomous beasts. An additional **Reward** will be granted accordingly!
> - Achieved the rare achievement **Indiscriminate Hunting Bug**!
> - When facing insect-form enemies in the future, you will gain additional stats!

System notifications poured out as though they had been waiting for me.

But I was in no position to inspect every line in the holographic window floating in the air.

Below the great tree where I was standing, the Beast Miao King was in the middle of a one-against-many bloodbath.

*Hissss!*

“You bastards! Even tearing you to pieces wouldn’t be enough! How dare you do this to my hair!”

“……”

He was worried about his hair even in a situation like this.

The clothes worn by the Beast Miao King had already melted away halfway, revealing his skin in several places, and almost all of his once-thick hair had been eaten away by the slime.

Even so, true to his title as one of the Ten Kings, he had already killed one and was fighting three at once.

*Wham!*

Correction.

Two now.

The moment the Beast Miao King’s fist, thrown with a savage aura, smashed one of the Thousand-Year Spiders apart, I kicked off the great tree and plunged toward the ground like a bolt of lightning.

*Whooosh! Crack!*

The spearhead pierced through the Thousand-Year Spider’s body like tofu.

At the same time, the powerful Scorching Yang Qi I had drawn up from my dantian surged through the creature’s body.

*Fwoosh. Boom!*

With an explosive roar, its enormous body burst into pieces.

A tremendous amount of bodily fluid sprayed out and evaporated at the same time. On top of the corpse, now impossible to recognize, only a new System notification remained.

*Ding.*

> **System**
>
> - Defeated **Lv. 109 Thousand-Year Spider**!
> - Gained a substantial amount of **EXP** and **Fame**!
> - Because you additionally defeated an extremely rare existence, you gained bonus **EXP**!
> - **Level Up!**

*Fwoooosh.*

Invisible healing light swept over my entire body.

The skin melted by the slime and the internal energy I had expended were restored, while the flames on the spearhead, which had been slowly dying down, suddenly blazed as fiercely as though they had never weakened.

*Fwoosh.*

—Sssssss……

And the method chosen by the last Thousand-Year Spider, which had been staring fearfully at the blue flames in the darkness, was none other than escape.

*Pat-pat-pat!*

All eight legs kicked off the ground at once.

Its enormous body leaped into the air and then landed lightly after stepping on something invisible.

That was when I caught sight of something glittering beyond the flames illuminating the darkness.

*A spiderweb?*

With that thought flashing through my mind, the Beast Miao King and I charged after the fleeing Thousand-Year Spider.
## Chapter artifact 639

# Chapter 639

When you thought about it, it was only natural.

No matter how extraordinary a Thousand-Year Spider was as a venomous creature, its essence was still that of a spider.

Spiderwebs were spread everywhere throughout the Poisonblood Grounds, practically their home territory, and the last survivor of the five Thousand-Year Spider siblings had completely lost the will to fight and was fleeing along its webs.

And there was one thing I hadn’t expected in this situation…

*Thump! Shhhhk!*

That enormous spider was much, much faster than I had imagined.

*……What the hell? Why is it so fast?*

I didn’t know whether it was because the creature was fleeing for its life or because it had laid webs everywhere in preparation for emergencies.

Whatever the reason, the distance between us and the Thousand-Year Spider hardly narrowed at all, and I had no good way to catch it as it fled back and forth between the air dozens of zhang above us and the great trees.

*No wonder Spider-Man was so fast……*

I was muttering inwardly as I used my movement technique when an inexplicable chill swept over my entire body. I instinctively ducked my head.

*Slice!*

With a sharp cutting sound, a handful of hair drifted through the air.

The thing that had narrowly grazed past me was none other than a spiderweb.

It was as tough and elastic as steel wire, and striking it at such high speed had turned it into a razor-sharp edge.

“Great Hero Yayul!”

The moment I realized that, I shouted a warning, but the Beast Miao King’s response was a little late. He was larger than me, and his movements were rougher.

*Slice!*

*What is this? I feel like I’ve seen a razor commercial.*

Instead of flesh and bone, the top of the Beast Miao King’s head had been shaved clean. He answered with a miserable expression.

“……Why did you call me?”

“……Nothing. I just felt like calling you.”

The thick hair that had once streamed behind him like a lion’s mane was nowhere to be seen.

The Beast Miao King’s crown, stripped bare by the Thousand-Year Spiders’ barrages of acid-laden phlegm and their webs, gleamed like an octopus that had just come ashore.

*Is this a battle between Doctor Octopus and Spider-Man?*

The sides seemed to be reversed, but still.

Thinking of it as watching a scene from a superhero movie made my heart swell with grandeur.

Of course, the octopus Miao King’s anger over his now-sparse hair was reaching the heavens.

“You bastard! How dare you!”

Naturally, his hair wasn’t the only reason he was angry.

They might have belonged to different tribes, but he had lost hundreds of warriors who were practically his own people overnight. A savage energy flowed from the corners of his reddened eyes.

*Kra-boom!*

The moment the Beast Miao King stamped his foot, the damp ground, saturated with poison and moisture, sank inward like a sinkhole.

At the same time, he used the tremendous rebound force to leap high into the air and threw a punch.

*Whoooom! Bang!*

Compressed air burst apart, and the wind rippled.

The Fist Energy released as it tore through space severed the webs that had melted into the darkness and shot toward the Thousand-Year Spider.

*Shreeeek! Shhk!*

But contrary to what the Beast Miao King and I had hoped, the projected Fist Energy cut through empty air, and the Thousand-Year Spider, having narrowly escaped death, let out a chilling cry.

—Ssssssissss!

It wasn’t an ordinary cry.

A strange noise that burrowed into my ears and spread through the space like Sound Transmission caused countless movements to register in my sharpened senses.

*This is……*

*Rustle.*

The Poison Mist that had transformed the Poisonblood Grounds into a land of death.

The grass stained black.

Between the great trees whose ages were impossible to guess, *those things* emerged into view, and I recalled a word I had momentarily forgotten.

*King of the venomous beasts.*

It was a short and accurate expression for the Thousand-Year Spider.

The venomous beasts that had crouched throughout the Poisonblood Grounds, waiting for orders, had finally answered their king’s call. They had become an army of countless creatures and were blocking the path ahead of the Beast Miao King and me.

*Slither. Ssssss!*

Snakes and centipedes as long and enormous as whips. Spiders and toads the size of human heads. Hundreds of bees pouring out from somewhere among the leaves of the great trees.

Venomous beasts with hideous forms I couldn’t identify—and didn’t want to identify—were converging and joining together.

In the blink of an eye, dozens became hundreds. Hundreds became thousands. At last, they formed a single wall.

*Kraaaaa!*

The countless venomous beasts blocked the only path through the Poisonblood Grounds and surged toward us as a gigantic triangular wave.

And above them, at a much lower height than before, the Thousand-Year Spider stood on its web and looked down at us.

It no longer fled. Now it gazed down upon the ground like a king.

Looking at it, I muttered under my breath.

“Fucking bastard. Acting cool now, are you?”

It had clearly been aiming for this from the beginning.

Nanman really was a goddamn place. What kind of animals and spiders were this cunning?

I had entered the Poisonblood Grounds following the Black Tiger known as Ailao Mountain’s Wraith. The Thousand-Year Spider we encountered there had finally summoned all its guards once it reached a battlefield favorable to itself.

Judging by everything I had seen firsthand, its intelligence was in no way inferior to an ordinary human’s.

*Compared to some glutton, it’s Einstein.*

Taishan suddenly came to mind, and I turned toward the Beast Miao King.

Even for a man who had lived his entire life in Nanman, this seemed to be a sight he had never seen before. He let out a low groan, and when our eyes met, he spoke with a solemn expression.

“There is no need to be afraid. Neither you nor I will die here.”

Afraid?

Instead of answering, I let out a quiet laugh.

It would be hard to find another word that was both closer to me and farther from me than that one.

When I thought about it, I had always considered myself a coward. Yet when faced with the threat of death, I had never once backed down.

*At first, I became a Hunter because I wasn’t afraid. Later, I learned martial arts because I was afraid.*

It was a strange thing. I had fought and struggled with all my strength because I was afraid of dying, yet I kept heading toward battlefields where it wouldn’t have been strange for me to die at any moment.

But……at least today, I didn’t think I would die.

*Kraaaaaaaaa!*

As I watched the wave of venomous beasts roll closer, I suddenly opened my mouth.

“When those things are gone, kill it immediately. No—just hurt it enough to leave it barely breathing.”

“What?”

“Remember this. You cannot delay even a little. We need to deal with him now, while he’s lowered his height without suspecting anything.”

“What are you talking abou—”

Now.

Instead of answering the Beast Miao King’s question, I lightly touched the ground. The internal energy surging from my dantian was already racing toward my toes.

*Slither. Boom!*

Compression.

And then, an explosion.

The internal energy that burst from a single point—the tip of my toe—gave my entire body the speed of a beam of light. At the same time, a fierce gale wrapped around me and scattered the deep green Poison Mist.

Beyond it, a colossal wall formed by thousands of venomous beasts was waiting for me.

*Kraaaaaa!*

A thick shadow fell over my head.

The Poisonblood Grounds were already dark, but at that moment, they sank into complete darkness.

Then brilliant light burst from the blade of the White Flame spear in my hand.

*Vooooom.*

Along with a sound like a swarm of bees, flames bluer than the sky began to burn.

Three jiazi’s worth of powerful Scorching Yang Qi drew together, linked, and coalesced, transforming into an even greater hellfire.

And at the end of it all—

*One Annihilation.*

*Ruuuumble!*

A flash and a roar tore through the darkness, making even the earth and sky tremble.

* * *

Beast Miao King Yayul Cheok had thought of himself as a wild man since childhood.

He was a raw, rough person, as far removed from etiquette and refined manners as one could get.

But they said a position made the person.

As he lived, he found himself with responsibilities that had to be shouldered from the front. He also found people who followed him despite there being nothing worth admiring in him.

As the years flowed relentlessly onward, he eventually became the great chieftain of the Bai people. Then one day, he looked around and found himself sitting in the weighty position of Palace Lord of the Nanman Beast Palace.

*How did this happen?*

He had no idea.

He had only trained in martial arts his entire life. How had things ended up like this?

But the water had been spilled long ago. It was too late to turn back, and impossible to scoop it up again, so he did his best to fulfill his duties as Palace Lord.

He no longer beat people up.

He also cut down on the profanity that had once come as naturally as breathing.

If he smacked the ears of a tribal chieftain who was unbelievably incapable of understanding what he was told, he could find peace of mind—but by now, that chieftain would rise in rebellion against the Nanman Beast Palace after being rendered permanently deaf.

But even the lips of the Beast Miao King, who had become much tamer through his long years as Palace Lord, began to move on their own when he witnessed the sight unfolding before his eyes.

“Uh, what the fuck is that? Uhhh.”

*Ruuuumble!*

Everything was breaking apart and melting.

The wave of thousands of venomous beasts was shattering to pieces right before his eyes.

The two-headed horn snake that hunted bears whenever it grew bored. The black frog that could kill a hundred bulls with a single drop of poison. The golden bees said to strip a tiger down to its bones in half a gak.[^1]

[^1]: A traditional East Asian unit of time, roughly equivalent to seven and a half minutes.

*Fwoosh! Kraaaaaa!*

Thousands of venomous beasts whose strength matched their hideousness were turning to ash before the blue flames and the roar that lit up the darkness.

*……This is insane.*

It had been more than fifty years since the Great Faction War.

That was how long it had been since he had witnessed a scene this astonishing.

Even the final ultimate technique unleashed by the Demonic Cult’s Sword Demon just before his death could not compare with the sight before him. And even Fire King Jeok Cheongang, who had easily dodged the Sword Demon’s final strike and methodically trampled him until he was on the verge of death, had never displayed this level of destructive power.

Of course, that applied to the man having these thoughts as well.

Even Beast Miao King Yayul Cheok himself.

*How is this possible?*

Unable to hide his shock and confusion, the Beast Miao King stared at the back of the young man standing tall before the blazing hellfire.

Then a single sentence suddenly flashed through his mind.

> *“When those things are gone, kill him immediately. No. Just don’t let him stop breathing.”*

“……!”

At first, he had wondered what kind of nonsense Jin Taekyung was spouting.

But that nonsense had become reality.

At the same time, the Beast Miao King realized what he needed to do.

*Boom!*

His body shot toward the sky with a thunderous roar.

Although the Beast Miao King’s movements were half a beat late, the same was true of the Thousand-Year Spider, which had been confronted with a situation it could never have predicted.

—S-Siss?

Several large and small eyes moved in different directions as though confused. Then they spotted the Beast Miao King and stopped.

A cold smile formed at the corner of his mouth as he flew upward, his remaining hair streaming behind him.

“I’ve finally caught you. You piece of shit. I’ll tear you apart.”

—……!

The Thousand-Year Spider had made two fatal mistakes.

First, it had underestimated the young human’s strength.

Second, it had killed the old human’s tribespeople and shaved off the thick hair he had always been proud of.

*Splaaash!*

The slime it spat out in one last act of resistance cut through the air, while the Beast Miao King’s outstretched hand caught one of the Thousand-Year Spider’s legs.

*Crack!*

—Siiiiiiit!

With the pain of its leg being ripped out, the Thousand-Year Spider let out a scream and plummeted toward the ground.

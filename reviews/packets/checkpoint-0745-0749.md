# Checkpoint Review — 745–749

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

# Chapters 745–749

## Plot

The Prophet meets the hidden Hasasin in a desert, using an undetectable transparent barrier to conceal their base and displaying a hoard of Magic Gems and enchanted weapons. He absorbs ten unrefined S-rank Magic Gems and orders Al-Nizar and the Hasasin to prepare another judgment against apostates and Western heretics. At the same time, an enormous tsunami approaches Tokyo.

Leviathan, an ancient S-rank sea demon once commanded by Asmodeus, awakens in response to the world’s rising magical power and an untouched Magic Gem. Japan identifies it as Susanoo as it devastates Tokyo Bay and nearby cities with waves, storms, lightning, and water attacks. The Prophet announces a second wave of terrorism, while monster waves appear elsewhere and Shanghai becomes a threatened target because China supports Jin.

Japan requests Korean assistance. Ares Guild, Peace Guild, and the Korean Air Force send five teams toward Tokyo, but unstable magical power prevents safe use of Teleport Magic. Michael Silbert enters the battlefield with Huginn, seeking to surpass Cheon Taemin and Jin.

Jin reaches Leviathan and uses One Annihilation, destroying its teeth, half its maw, and one eye, but suffering catastrophic recoil and acquiring the potentially permanent Broken Body debuff. A Top-Grade Potion removes his other conditions but cannot heal Broken Body or restore the lost combat attributes. With the Water Rescue Worker Title, Jin and the Skeleton King pursue Leviathan underwater. Leviathan swallows the Magic Gem and flees toward the open sea; Jin cuts through its magical wave and launches another attack, whose result is unresolved.

## Continuity

- The Prophet commands the revived Hasasin, possesses at least ten unrefined S-rank Magic Gems, and has announced another judgment and a second terrorist campaign.
- The Prophet’s identity, age, gender, and connection to the current disasters remain unknown. His concealment barrier cannot be detected by science or Magic.
- Leviathan has reappeared in Japan after more than thirty years. Japan calls it Susanoo, but Jin recognizes it as the ancient sea demon once commanded by Asmodeus.
- Leviathan has been severely wounded by Jin’s One Annihilation but remains alive, has swallowed the Magic Gem, and is fleeing underwater while Jin pursues it.
- Jin’s Broken Body debuff remains active. His combat-related attributes are reduced by 50%, and recovery may involve permanent attribute loss.
- The Water Rescue Worker Title lasts twenty-four hours but is 20% less effective because of its incompatibility with Scorching Yang Qi.
- Michael Silbert and Huginn have entered the Japanese crisis. Michael intends to become the undisputed best and has identified Shanghai as a likely next target.
- Five Korean Hunter teams and the Air Force are assisting Japan; Teleport Magic remains unsafe because Tokyo’s magical-power distribution is highly unstable.
- The Supreme Peak Quest **Unknown Death** remains active. Siegfried Wassmann’s killer, the method used, and Michael’s possible involvement are still unknown.
- Magic Johnson has found no breakthrough in Siegfried’s research, The Prophet remains untraceable, and Huginn’s undisclosed operation remains unresolved.
- The outcome of Jin’s latest attack on Leviathan and the consequences of Leviathan consuming the Magic Gem remain unknown.

## Translation Decisions

- Render **선지자** as **The Prophet**, **하사신** as **Hasasin**, **알 나자르** as **Al-Nizar**, and **알라의 심판** as **Allah’s Judgment**.
- Render **레비아탄** as **Leviathan** and **스사노오** as **Susanoo**.
- Render **마력** as **magical power**, distinct from **mana**; render **마정석** as **Magic Gem**.
- Retain **One Annihilation**, **Broken Body**, **Water Rescue Worker**, **Top-Grade Potion**, **Scorching Yang Qi**, and **light-flames** as established terms.
- Preserve the distinction between Leviathan’s true identity and Japan’s name, Susanoo.

## Durable state

{
  "active_continuity": [
    "The Prophet commands the revived Hasasin and has announced a second series of terrorist attacks after the earlier attacks called Allah's Judgment.",
    "The Prophet can create a transparent concealment barrier that cannot be detected by science or Magic.",
    "The Prophet possesses at least ten unrefined S-rank Magic Gems that retain their original power.",
    "The retired Grand Mage Siegfried Wassmann was found dead in his sealed hideout after his life force was apparently drained by unknown magic.",
    "Michael Silbert remains the strongest suspect in Siegfried's death and has personally entered the Japanese battlefield while pursuing his ambition to become the undisputed best.",
    "Jin has accepted the Supreme Peak Quest Unknown Death, whose mission is to discover the truth behind Siegfried's death.",
    "Michael and Huginn continue manipulating events and media coverage to isolate Jin and punish countries and Guilds that support him.",
    "Magic Johnson is investigating stolen research materials from Siegfried's laboratory but has not yet produced results.",
    "Huginn has completed an undisclosed operation whose consequences remain pending.",
    "Japan has requested Korean emergency assistance, with five Ares Guild and Peace Guild teams and the Korean Air Force heading toward Tokyo.",
    "Leviathan has been severely wounded by Jin's One Annihilation, swallowed the Magic Gem it sought, and is fleeing underwater while Jin pursues it.",
    "Jin's Broken Body debuff remains active after a Top-Grade Potion removed his other status abnormalities, leaving his combat attributes reduced and risking permanent loss."
  ],
  "continuity_sources": [
    749
  ],
  "open_questions": [
    "Who killed Siegfried Wassmann, by what magic, and why?",
    "How did Michael Silbert learn about A Area and Cheon Taemin's condition, and did he order Siegfried's death?",
    "What is The Prophet's identity, and how are the Prophet's terrorist campaign and Leviathan's reappearance connected?",
    "What is Huginn's undisclosed operation, and can its consequences actually bring Jin down?",
    "Will Jin's second spear attack kill Leviathan, and what consequences will follow from the Magic Gem Leviathan swallowed?"
  ],
  "safe_through": 749,
  "temporary_decisions": [
    "Render 선지자 as The Prophet.",
    "Render 레비아탄 as Leviathan and 스사노오 as Susanoo.",
    "Render 마력 as magical power, distinct from mana.",
    "Render 마정 and 마정석 as Magic Gem.",
    "Render 마계어 as Demon Realm language and 광염 as light-flames."
  ],
  "version": 1
}

## Reading copies

## Chapter artifact 745

# Chapter 745

The desert night was bitterly cold.

Where the scorching sunlight and shimmering heat had vanished, nothing remained but subzero temperatures and an unusually enormous moon.

A daily temperature swing of no less than sixty degrees.

But even the frigid cold could not stop the footsteps of someone climbing a crescent-shaped dune.

*Sssrrk.*

Despite ascending a steep slope, the figure moved as though gliding across the sand.

The hem of a thin silk robe brushed against the grains before coming to a stop.

“This is the place.”

The moment that flat voice rang out, the empty air rippled.

*Ffft.*

With the faintest sound, a dozen or so figures descended onto the dune.

Every one of them had their face concealed by a black mask and turban. They politely dropped to one knee and whispered,

“Inshallah. We pay our respects to the great Prophet who has returned to this land.”

Standing alone before them, the Prophet’s robe fluttered lightly.

“Inshallah. I wondered when you would finally reveal yourselves.”

Those words made it clear that The Prophet had seen through everything from the beginning. The dozen pairs of eyes visible above the masks trembled.

“Prophet…”

“I know. I know that you act for my sake. That is why you followed me even while defying my orders.”

“If you would punish us for our disobedience, we would gladly pay for it with our lives. But we, the Hasasin, will never leave your side, no matter the circumstances.”

The Hasasin. Or the Assassins.

After their stronghold was conquered by their enemies around the thirteenth century, this venerable order of assassins had survived as nothing more than a religious sect. Then, with the Great Cataclysm, they had risen again.

And they had never once bent their will.

“The Western heretics are both cunning and powerful. If you were to be discovered by them…”

“Al-Nizar. More loyal than anyone, yet foolish and full of worry.”

“…”

“Look at me.”

The leader of the Hasasin flinched and cautiously raised his head.

The great Prophet stood against a sky scattered with stars, gazing down at him.

A mysterious light shone from the eyes framed by the strangely dark folds of the robe.

“Do you still not understand?”

The Prophet stretched both arms toward the sky.

*Vwoooom.*

An immense force swelled, pushing out the edges of The Prophet’s robe. The wind died, and the air vibrated.

The Hasasin swallowed unconsciously. Their gazes followed the Prophet’s hands, and in the next moment—

*Shhhhhhhk.*

They saw it.

Beginning in the sky and curving around an area several hundred meters in radius, a transparent membrane had formed.

It was both a protective barrier that no product of science—not even Magic—could see through and a screen that concealed them from their enemies’ eyes.

“As long as I protect you, they will not discover even our shadows.”

“…”

“…”

Even the Hasasin, who had endured extreme training, could not hide their surging emotions at that moment.

First, because their Prophet possessed such astonishing abilities.

And again, because The Prophet had called even lowly servants like them “us.”

“Inshallah…!”

“Prophet!”

Their cries of joy and emotion echoed through the quiet desert.

But that was not the end of the miracle the Prophet would show them today.

*Sssrrk.*

As the long, voluminous sleeve of The Prophet’s robe fluttered, the crescent-shaped dune beneath their feet began to shake.

No—it split apart.

*Crk-crk-crk!*

It was a truly miraculous sight.

In the distant past, if Moses had parted the Red Sea and led the Hebrews across, then this new Prophet, appearing after more than a thousand years, had divided part of a vast sea of sand in two.

And what had been hidden beneath the countless grains of sand glittered in the moonlight like a gift from God.

“My God…”

“Prophet. What in the world are those?”

But instead of answering the Hasasin’s questions, the Prophet silently extended a hand.

*Clank. Clank. Clank!*

Locks burst apart as though exploding under the force of invisible energy.

At last, the leader of the Hasasin saw the contents of the dozens of iron chests and opened his eyes wide.

“T-this is…”

A bright light that even the darkness could not conceal.

Countless gold and silver bars unlike anything he had ever seen. On top of that, the radiance of weapons imbued with various forms of Magic dazzled his pupils.

But something else shocked him more than anything.

“Magic Gems…!”

The cry that escaped him like a groan was the truth.

Magic Gems.

And not just any Magic Gems—there were hundreds of them, clearly ranging from high-grade to top-grade. Some among them were especially large and radiated an immense force.

*Fwoooosh.*

Even he, a leader of the Hasasin who had reached the realm of an S-rank Hunter, could not easily approach that powerful energy.

“Hk.”

The leader of the Hasasin involuntarily sucked in a startled breath. Then the Prophet’s familiar, toneless voice reached his ears.

“They are S-rank Magic Gems. They retain all their original power.”

“P-Prophet…”

“Stand back. This is power you cannot handle.”

With that quiet warning, the unrefined S-rank Magic Gems rose into the air.

They moved like living creatures before being drawn into the Prophet’s robe.

There were ten of them.

The leader of the Hasasin’s gaze trembled as he watched.

*How in the world does the Prophet possess those…?*

He had already known that the Prophet’s abilities were extraordinary beyond common sense.

But from the time of the Great Cataclysm until now, only a little over a hundred S-rank monsters had officially appeared in human history.

On extremely rare occasions, a tiny number of A-rank monsters had possessed S-rank Magic Gems. But those instances were exactly what they were—exceptional cases. Even in the Middle East, where countless Gates existed, S-rank Magic Gems had appeared only once or twice.

And yet ten S-rank Magic Gems had gathered here.

All of them retaining their original magical power.

*It’s an incredible amount. Unbelievable.*

Despite his boundless faith in The Prophet, this time he could not help but ask—or so he thought.

The moment he turned his head, he met the faint glow of The Prophet’s eyes between the folds of the robe.

“I will ask you. Who do you think the person standing before you is?”

“…”

That gaze seemed to have already seen through everything.

The leader of the Hasasin felt as though he had been struck by lightning and dropped to his knees.

How dare someone like him question what the Prophet was doing?

It was something that could not happen—and must never happen.

“Great Prophet, please forgive this sinful servant!”

The air froze in an instant.

The Hasasin touched the weapons at their sides and waited for the Prophet to speak.

If The Prophet gave the order, they were prepared to eliminate their own leader without a moment’s hesitation.

Because The Prophet was a prophet who conveyed God’s word and the one who led them all.

After the death of the Prophet Muhammad, the Islamic world had fought and feuded for more than a thousand years, and the sands of the desert had been stained with blood.

As the years passed, a tiny few enjoyed immense wealth and power. But in the great cities built on oil, what took priority was not the word of Allah, but the capitalism of the apostates.

Now was the time to gather Allah’s children, who had once turned blades against one another, beneath a single root—and to save their brothers persecuted even in the Western world.

In the name of the great God.

In the name of the Prophet who had come to them decades ago in God’s place.

And just as an invisible blade slowly cut through the silence, one tightly closed mouth finally opened.

“Al-Nizar.”

It was a voice that revealed neither age nor even gender.

At the call, the leader of the Hasasin swallowed. His entire body was already soaked in cold sweat.

“Prophet.”

“I will give you one final warning, son of God. You are still immature—and that is precisely why I care for you all the more.”

“…”

“Inshallah. All of this is the result of the long patience and providence God has granted me. You must never doubt it. Do you understand?”

“I will remember. I will remember it well.”

*Drip.*

A liquid mixed with cold sweat and tears dampened the grains of sand.

The Prophet gazed benevolently at the trembling leader of the Hasasin, whose body shook with emotion and relief, and continued.

“The time has come again. Tell your brothers who have been preparing.”

At those words, everyone’s eyes flashed open.

Nearly ten days had passed since the day they called “Allah’s Judgment.”

Everyone who followed the Prophet had been waiting impatiently for the next day of judgment.

“Prophet. Do you mean…”

“God wills it. Bring down God’s hammer upon the apostates gnawing away at us from within and the Western heretics.”

The eyes visible above the masks gleamed with fanaticism and exultation.

The Prophet gazed up at the star-scattered sky and muttered,

“There isn’t much time left until the end.”

Some wanted catastrophe. Some struggled to prevent it. And still others wanted something beyond it.

Even now, they were all rushing toward their own purposes.

* * *

Sugihara Gyoiku was a laborer who had worked in cargo shipping for a long time.

He was a lifelong Tokyo native and, at the same time, a seasoned laborer who had entered the maritime transport industry when he was young.

Some people occasionally looked down on him for doing manual labor, but he did not particularly care.

Not everyone in the world could become a Hunter, lawyer, or doctor. And he, too, was a necessary part of this world.

But lately, he had been in a terrible mood.

No—there was no way he could feel good.

*Chikushō. Those damn monsters.*

Just ten days earlier, a monster wave in Tokyo had killed and injured many people.

Tokyo Tower, which he had secretly been proud of as a Tokyo native, had collapsed horribly. The chicken restaurant he had frequented for thirty years had also vanished in the aftermath.

*I didn’t like that the owner was a Chosenjin,[^1] but the chicken was incredible.*

The fact that he could no longer enjoy Korean-style chicken and beer after work made Gyoiku sad. But setting that aside, he went to work again today.

“Gyoiku-san. You’re here?”

“Yo.”

After exchanging brief greetings with his fellow laborers, he went straight to the work site.

Tokyo Bay, where he worked, was already packed with cargo ships.

“Where should we start?”

“They’ve already started. Come on.”

Sugihara Gyoiku loaded cargo onto the ships while chatting with his coworkers about this and that.

News that Tokyo’s magical-power distribution had been rising particularly sharply lately. Reports that the current prime minister, who came from a prestigious political family, had said something insane again.

And talk about the tsunami, among other things.

“A tsunami?”

“Yes. Apparently, it’s gradually getting closer to Tokyo. They say it’s enormous.”

“Hmm.”

“Don’t worry. The government said it would die down soon.”

“Well, I suppose.”

He was a little worried, but that was all.

Even if it was a tsunami, it would not reach Tokyo in the end.

Tokyo Bay, in particular, was literally a bay where the sea extended into the land, and its magical defense systems had also been thoroughly established.

*When I finish work today, maybe I’ll look for a new Korean chicken place.*

Gyoiku straightened his back, thinking about something pointless.

And at the same time, he froze like a stone statue.

“Huh?”

*What is that?*

That was the first thought that flashed through his mind.

Then, in the next moment, something he had heard just a little while ago rang through his head.

*The tsunami.*

Gyoiku stared blankly, mouth open, toward the sea beyond the harbor.

A colossal wave unlike anything he had ever seen was racing toward him, rising so high that it seemed capable of blocking out the sunlight.

*Goooooong.*

Along with the cry of some unknown thing—a sound that froze him merely by hearing it.

[^1]: A Japanese ethnic slur for Koreans.
## Chapter artifact 746

# Chapter 746

Returning to everyday life usually means stability.

But immediately after the mysterious death of Siegfried Wassmann, we returned to our respective positions only to face a frantic stretch of time.

“The magical-power distribution in the C-rank Gate in Sokcho, Gangwon Province, is rising rapidly. It’s currently at Stage Two…… entering Stage Three! It’s a mutation Gate!”

“How many people can we deploy right now?”

“Four teams are on standby at the Gangwon Province branch. If we use the Teleport Magic circle connected to Sokcho City Hall, they can be sent to the site within five minutes.”

“Send them out immediately. This could lead to a monster wave if we’re not careful, so make rescuing survivors and quickly suppressing the situation our top priorities.”

The situation after our return was, quite literally, the worst.

Until only a few years ago, mutation Gates had occurred no more than once a month. Now, three or four were appearing every day—and that figure was limited to Korea alone.

Instead of stock prices, the magical-power distribution chart was hitting an upward trend every single day without fail.

Every broadcasting station cut back on entertainment programming, while the newly established disaster-breaking-news channels featured experts from every field engaging in fierce debates.

“Many people overlook the fact that the rise in magical-power distribution has been happening steadily every year. Compared to the period immediately after the Great Cataclysm, the current figure is actually on the low side. Once this situation is over, things will calm down quickly, so there’s no need for the public to worry—”

“Calm down quickly? What kind of nonsense is that? And how can you compare things to immediately after the Great Cataclysm? To put it bluntly, after we killed the Demon King on the ‘Day of Victory,’ did humanity put down its weapons and all dance Ganggangsullae together?[^1] Back then, you could go to Han River Park and see lizardmen. Do you not remember that it took nearly a year just to deal with the monster armies that remained?”

“I live in Ilsan, so I never saw lizardmen in Han River Park. I’m right.”

“What a fucking moron…”

“Come on, now. You’re a year younger than me, so watch your language.”

“A year younger, my ass, you fucking bastard. My parents filed my birth registration late. Happy now?”

“Mr. Host, are you really going to sit there and watch this?”

It was no longer particularly surprising to see silver-haired authorities in academia turn red in the face on television and engage in title matches over their respective arguments.

Even as they grabbed one another by the collars, the news on the next channel was reporting breaking developments about mutation Gates or monster waves somewhere in the world.

And in the middle of those horrific scenes, I did my best to struggle through them.

*Shhk!*

The spearhead of White Flame smoothly cut through leather and bone harder than armor.

The enormous monster—I had no idea how many I’d killed by then—stopped dead in its tracks. Then it slowly turned around and split in two from top to bottom.

*Shff. Thud!*

The moment its three-meter-tall body fell, divided into two perfectly equal halves, I locked eyes with a man who had fallen a few steps away.

He had survived by the narrowest margin, and in his hand was a plastic picket sign with red-painted letters.

**ARREST INTERNATIONAL CRIMINAL JIN TAEKYUNG!!!**

*Hmm.*

I wondered how I was supposed to react in a situation like this, then simply gave him a bitter smile.

Even if he hated me that much, using three exclamation marks was going a little too far.

“Are you okay?”

“……Ah.”

“You look fine apart from a few scratches, but stay seated just in case. It’s all over anyway, so the rescue team will be here soon.”

I turned away from the man, who was only moving his lips.

In the street, reduced to a wasteland in barely thirty minutes, the corpses of dead monsters were mixed together with human bodies.

I sharpened my senses and searched the surroundings, but I could no longer feel any signs of life.

*It wasn’t supposed to cause this much damage.*

It was a tragedy that a monster wave had occurred in this peaceful little city.

And it was also a tragedy that the hundreds of protesters who had gathered to condemn me had chosen this street as their rallying point.

*Splash. Splash.*

I crossed the street, stepping through puddles where red and blue blood had mixed together.

Hyenas that had gathered after catching the scent wasted no time rushing in with cameras and microphones.

“What do you think about this monster wave?”

“You arrived faster than anyone else and suppressed the monster wave! First of all, as a fellow human being, I’d like to express my deepest gratitude—”

“These people had gathered to condemn you. Is it possible that this monster wave was artificially caused by someone who supports you—”

“Why has Mr. Sky still not shown himself? What connection do you have to the death of Siegfried Wassmann, who died recently?”

“Jin, give us a statement!”

It felt as though filth were pouring down on me from every direction.

There were people defending me, but far more reporters were frantic to come up with sensational headlines.

And many of them had probably been paid a considerable amount of money by someone else in exchange for asking questions like these.

For example…

*The Odin Guild.*

It was something I had already more or less expected. Even when Team Leader Choi first told me about it, I hadn’t been particularly surprised.

Worsening public opinion through media control.

Blatantly dragging me and the Ares Guild, which enjoyed overwhelming public support, through the mud was not something just anyone could attempt.

But Michael Silbert had enough power and justification to do exactly that.

The problem was that, at least where the media was concerned, his efforts were working far better than I had imagined.

“The Prophet still hasn’t revealed himself. What would you like to say to The Prophet, who is surely watching you from somewhere?”

“Statistics show that while the Ares Guild suppresses an average of 3.6 incidents per day, the Odin Guild resolves 6.5. Do you have anything to say about that?”

“Mr. Jin Taekyung! Mr. Jin Taekyung!”

“Hey, you! What kind of question is that? Do you call yourselves reporters?”

“Everyone, move back. Now!”

It was pure chaos.

Reporters rushing forward in pursuit of more articles and payment. Police officers and Hunters trying to hold those reporters back.

I slipped through them, feeling as though my insides were twisting, while listening to someone’s voice echoing in my head.

“You humans… are a real shitshow.”

I never thought I would live to hear something like that from a monster.

But I couldn’t think of anything to say in response.

No—maybe I had simply lost all my strength the moment I saw that picket sign.

“Shut up. You’re loud.”

Even though I hadn’t used that much internal energy, the mental exhaustion was considerable.

I gave the Skeleton King, stored in my Inventory, a brief answer, then pulled out the Magic Scroll I had brought along and tore it.

*Riiip. Fwoosh!*

The moment the Teleport Magic activated, its distinctive sensation swept through my entire body.

The scenery around me changed in an instant. As my vision quickly recovered, I saw a familiar face.

“You got back quickly. I only heard a little while ago that you were returning.”

Song Song’s voice was thick with exhaustion. Dark circles that hadn’t been there before hung beneath her eyes, and she immediately pulled out a handkerchief and held it out to me.

“Wipe your face first. There’s blood on it.”

I looked back and forth between the handkerchief and Song Song, then smacked my lips.

“I’m asking because I’m curious, but are you saving your Clean Magic to make soup with?”

“Do you think Magic works by putting coins into it? You can chug potions to replenish mana, but you can’t replenish mental energy that’s already been spent. I’m already not getting enough sleep these days, so shut up and use the handkerchief.”

I had nothing to say, since I knew exactly who the main reason for her lack of sleep was.

I silently wiped away the blood and handed the handkerchief back. Song Song accepted the dirty cloth and quietly chanted a spell.

“Clean.”

“……?”

*Whooosh.*

The dust and blood vanished in an instant, leaving the handkerchief spotless.

Song Song blinked innocently at me as I stared at her in disbelief.

“What? It’s designer.”

That shameless remark—and the fact that Song Song had clearly planned for this situation—made me snort despite myself.

“Ha.”

“You’re finally smiling. You looked like you were about to die on TV a little while ago.”

“You were watching?”

“I watched the whole thing live. I even heard those insane reporter bastards spouting bullshit.”

“……Well, I suppose I have to put up with it. If you think about it, I am partly responsible for this whole mess.”

Song Song suddenly furrowed her brow.

“Are you going to spout bullshit too?”

“……”

“Just when I thought you were getting back to normal, what’s this? If you want to blame yourself that badly, kill those bastards first and then beat yourself up all you want.”

That was exactly what I wanted to do.

But it wasn’t as though that would be easy. Three days had already passed since our trip to Switzerland, and almost nothing had changed.

Magic Johnson’s investigation had yet to produce any results. The Prophet’s whereabouts could not be traced even with every kind of Magic and satellite surveillance. And the Odin Guild, led by Michael Silbert, continued to soar higher by the day.

“Don’t blame yourself or worry too much. Other people are working hard too, not just you. Uncle Kkeokjeong in particular was running around like a madman yesterday, saying he was going to fly straight to Paris and cut Michael’s head off.”

“That… It’s reassuring to have an entire army on our side, but if he did that, Uncle Kkeokjeong would be the one losing his head.”

“Yeah, I told him exactly that.”

“You told him that?”

“Yeah. It’s true. Anyway, he looked a little dejected after hearing it, but he accepted it pretty quickly.”

That alone was something to be grateful for.

Song Song and I walked along, exchanging various bits of conversation.

By the time I had finished hearing all the news about my mother and Hayeon, who were staying at the mansion under ironclad security, we arrived at the office where Team Leader Choi was waiting.

“You’re back.”

He looked even more exhausted than Song Song. The office, which was always kept neat and orderly, was a mess, and the desk was covered with empty coffee cups.

“Thank you for your hard work on such a long trip. But…”

Team Leader Choi looked back and forth between Song Song and me, then lowered his voice.

“Where is the other person?”

“Don’t worry. He came with us.”

“I’m here.”

Had I left him cooped up for too long?

I took the Skeleton King out of my Inventory, pretending to rummage through the subspace pouch at my waist as I recited the command.

*Inventory open. Summon.*

The next moment, a sturdy young white man popped into existence.

Song Song muttered,

“Wow. Smooth delivery.”

“Shut your mouth, beautiful but ill-mannered human female. How dare you compare this body to such a thing…”

“Thanks. That really brightens my mood.”

“You damn…”

The Skeleton King’s face was full of displeasure as he muttered a curse, but there was nothing we could do about it.

*Even if his identity has already been exposed to some extent, we have to hide him as much as possible.*

We had scrubbed his past and identity clean, but the word “perfect” did not exist in this world. Even the Pentagon, known to have the best security in the world, had been breached in the same way.

Given the circumstances, we had no choice but to limit his exposure as much as possible.

But when I heard Team Leader Choi’s next words, I realized that I had to play the Skeleton King.

“Three minutes ago, Tokyo Bay collapsed.”[^2]

[^1]: Ganggangsullae is a traditional Korean circle dance and folk song.

[^2]: The Korean wording literally says that Tokyo Bay “collapsed,” preserving the alarming ambiguity of the announcement.
## Chapter artifact 747

# Chapter 747

Beneath a sky shrouded in dark clouds, Sugihara Gyoiku thought blankly.

*What the hell is happening?*

His mind, belonging to nothing more than an ordinary civilian, could not process what had happened to him.

His trembling limbs had already stopped obeying their owner’s will, and his stomach, full of salty seawater, could not withstand the rough movements of the rescue helicopter.

No—perhaps what Gyoiku truly could not endure was the horrifying reality that had suddenly come crashing down on him.

“Ugh—bwaaaargh!”

Dirty vomit sprayed in every direction.

Some of it hit the other people loaded into the rescue net with Gyoiku, but no one complained or even seemed to care.

They simply stared at the scene unfolding below them with empty eyes.

*Crack!*

It broke, collapsed, and was swept away.

A gigantic wave dozens of meters high—perhaps even hundreds.

Even though they were witnessing it with their own eyes, they could not believe the disaster unfolding across the sea as it swallowed everything in its path.

The port of Tokyo Bay, where hundreds of ships had entered and departed every day, had already vanished without a trace. Cargo ships weighing tens of thousands of tons were shattered like Styrofoam, then carried along by the waves into the nearby industrial complex.

*Rumble—BOOM!*

With a deafening roar, fierce flames surged upward and swallowed the people’s screams.

Beneath the constant wail of alarms, cars and crowds that looked tiny as swarms of ants scattered in every direction to escape the disaster.

To escape the horrifying calamity.

Unable to accept the fate that had befallen them.

And behind those struggling desperately to survive, an enormous shadow fell across the ground.

*Whoooosh!*

“Ah… Ahhh…”

The survivors watching the whole scene from above let out vacant moans.

The land they had painstakingly rebuilt through decades of sweat and blood after the Great Cataclysm was collapsing. A magnificent civilization was falling apart.

The white foam that had always scattered against the breakwaters and the blue seawater had both turned red.

Nothing could stop that enormous wave as it smashed through and swept away everything in its path.

No—even if the wave itself subsided, it would make no difference.

Because this was not merely a natural disaster.

Beneath the deep waters that had swallowed the port and industrial complex, an even greater calamity was lurking.

The survivors who had miraculously lived through it knew the truth. That was why, upon spotting dozens of fighter jets flying toward them from the opposite direction, they could only scream as though coughing up blood.

“N-No!”

“Don’t come here!”

But their desperate cries reached no one.

Not the squadron of fighter jets streaking across the sky with sonic booms.

Not the elite Japanese Hunters who had boarded those aircraft to deal with the situation.

And not the deep-sea monster that had awakened from its long sleep.

*Goooooong.*

A low but immense rumble stirred up the waves that had begun to subside.

The strengthening wind turned into a storm and howled through the air, while thunderous roars soon echoed among the countless dark clouds covering the sky.

*Rumble, rumble…*

Every living thing in the vicinity froze like a statue and stared blankly at the sky.

It was a fear engraved deep in their bones—a primal instinct they could feel simply because they were alive.

Power.

The power of nature. But at the same time, a power that was not natural.

“What the hell is that…?”

The pilot was muttering in a groan as he prepared to relay the order for the Hunters on standby to descend.

At that moment—

*Fwoosh!*

Hundreds, thousands of bolts of lightning plunged down from the sky and flooded the entire world with white light.

* * *

The Japanese Ministry of Defense’s operations control room, hastily called into session, was silent.

A suffocating silence. Throats moving soundlessly. Eyes clouded with shock.

Although dozens of high-ranking officials and generals were present, not a single person spoke first.

All they could do was stare with vacant eyes at the holographic screen installed inside the control room.

*What… What the hell just happened?*

A single thought occupied everyone’s mind.

That was how shocking the scene they had witnessed was.

A flash of light so intense that it filled the holographic screen. When the people who had instinctively closed their eyes finally opened them again, all they could see were dozens of aircraft plunging toward the ground—and the waves swallowing them whole.

“Th-They’ve been… completely wiped out.”

An oblivious report feebly broke the silence, revealing the truth that everyone wanted to avoid facing.

Everything had vanished.

No—they had died.

The hundreds, thousands of lightning bolts had turned everything within their range to ash.

The rescue helicopters carrying those who had miraculously survived. The fighter squadron proudly fielded by the Air Self-Defense Force. The hundreds of Hunters mobilized in an emergency.

They had all been finished.

But the thing that had plunged the operations control room into deathly silence was not merely the tsunami that had already swallowed as many as ten cities and now threatened the capital.

It was the monster.

They had seen the form of a monster that had vanished several decades ago—one they had believed would never appear again.

“……Susanoo.”

That was the monster’s nickname, given because it was said to rule the sea and storms.

But the general who muttered the name like a groan hurriedly closed his mouth.

The next moment, he felt the Defense Minister’s glare fixed on him.

“Th-That was…”

“Shut your trap, Yoshimura.”

The Japanese Defense Minister cut off the man’s hurried excuse and looked around the room.

Half of the people who needed to produce a solution immediately were still floundering in shock. The other half waited for his lips to open again.

Like baby birds waiting for food.

Or like people hoping for a single scapegoat who could take responsibility for this disaster in their place.

*Crack.*

The elderly Defense Minister ground his teeth.

There were so many generals and officials, yet no matter where he looked, there was no suitable person.

The foolish, cowardly Prime Minister had buried himself in a bunker long ago, while the very few capable and responsible commanders did not have powerful enough backers to enter the Ministry of Defense’s control room.

In the end, there was only one person who could shoulder the blame right now.

*These incompetent bastards!*

The Defense Minister cursed them inwardly, completely forgetting that he himself had risen through the ranks thanks to an ancestor from a daimyo family.

Still, he was not so ignorant that he could deny the reality bearing down on them.

“Stop that thing with everything we have! I don’t care whether it’s the Self-Defense Forces or Hunters. Mobilize every resource at our disposal!”

“Yes, sir!”

“And…”

*Bang!*

The Defense Minister slammed his wrinkled hand against the table, then squeezed his eyes shut without being able to continue.

*Do we really… do we really have to go this far?*

A brief hesitation passed through his mind.

But it lasted only for a moment.

The situation had already spiraled beyond control, and to prevent an even greater disaster as much as possible, *that man* was more qualified than anyone else.

“Ask the world for help. And that man in particular—we must bring him here, no matter what diplomatic price we have to pay.”

“What?”

“If it’s him…”

His lips trembled like a child being forced to eat broccoli.

Then, facing the people staring back at him with no idea what he meant, the Defense Minister shouted until it seemed as though he were coughing up blood.

“That man! I said call that Chōsenjin![^1] Jin Taekyuuung!”

His pride as a subject of the Great Japanese Empire could not accept it, but he had no other choice.

That monster—Leviathan—was a demon sent down by heaven.

*We can’t let that nightmare happen again!*

Not long afterward, news broadcast on large and small holographic televisions installed throughout the control room informed them that the Defense Minister had made the right choice by selecting Jin Taekyung.

> —The entire world has once again been engulfed in flames. Ten days ago, the figure known as “The Prophet,” who carried out an unprecedented series of terrorist attacks, announced a second series of attacks in a video…

> —Breaking news. A monster wave has occurred in Manhattan, United States. Beginning with this incident, the United States and the rest of the world have entered a state of emergency…

> —At present, entry and exit bans have been imposed on countries where monster waves have occurred. As a result, part of the emergency Hunter mobilization order intended to support Tokyo, Japan, has fallen through. Among the countries in the nearest region of Asia, only Korea is believed to be capable of providing support…

* * *

“Japan’s Ministry of Defense has officially requested emergency assistance through the Ministry of Foreign Affairs.”

The news delivered to us by President Baek Hanseong was the starting gun announcing that everything had begun.

“Ares Guild and Peace Guild are heading out as the advance team. Five teams are already waiting—B-rank or higher, and limited to volunteers only.”

Team Leader Choi’s response had been faster than anyone’s.

The moment he first heard what had happened in Tokyo, he had already issued the mobilization order. President Baek Hanseong had prepared the Air Force so that we could reach our destination as quickly and safely as possible.

“What about the Teleport Magic circle?”

Team Leader Choi shook his head at my question as I gathered the equipment we needed.

“We could try it, but the probability of failure is far too high right now. The magical-power distribution around Tokyo rose sharply because of the monster wave ten days ago, and it’s already measuring more than three times the previous level.”

“Damn it. This reminds me of China.”

“Yes. It’s the same situation as back then.”

Mana and magical power were natural opposites.

If we attempted spatial movement while the magical-power distribution was rising sharply and growing unstable like this, our bodies could be broken apart like a thousand-piece puzzle—even if they were solid lumps of iron.

“Then how long will it take?”

“Taking the worsening weather in the area into account, we estimate about thirty minutes.”

“Thirty minutes…”

Of course, we would not be making a safe landing on a broad airport runway.

There was at least a ninety-percent chance that Tokyo International Airport, once the pride of Japan, had already been blown to absolute shit.

*And the remaining ten percent is the chance it’ll be blown to shit on our way there.*

I took a deep breath.

The video sent by Japan’s Ministry of Defense replayed in my mind.

The Maritime Self-Defense Force being swept away by a gigantic triangular wave. The land being submerged.

The wave had shattered the extensive defensive Magic installed along Japan’s coastline as though it were nothing, swallowed tens of thousands of people, and turned even the last remnants of hope to ash beneath countless lightning bolts.

As though proving the power ascribed to it by myths passed down from time immemorial.

*Leviathan.*

The devil of the sea that had ruled the waters during the Great Cataclysm.

One of the most powerful S-rank monsters commanded by the Demon King Asmodeus, it was a calamity that had vanished along with his death.

Some claimed that Leviathan had died alongside the Demon King. Others argued that the monster had survived and was merely waiting for the right time.

But without any evidence or proof, time continued to pass.

And today—

The nightmare known as Leviathan had been resurrected.

It had crossed more than thirty years to return to this world.

*Was its appearance a coincidence, or…*

An inevitability intended by someone?

Muttering the unresolved question inwardly, I finished my preparations and began walking toward the Hunters and aircraft waiting for me.

The wind blowing from far away seemed to carry a faint smell of blood.

[^1]: A derogatory Japanese term for a Korean.
## Chapter artifact 748

# Chapter 748

“Jin Taekyung has accepted Japan’s request for assistance.”

Michael Silbert replied calmly to Huginn’s report.

“And?”

“Ares Guild and Peace Guild have assembled five teams from their handpicked elites, and the Korean government is mobilizing the Air Force to send them to Tokyo. I prepared the profiles of the Hunters involved, just in case.”

The tablet Huginn handed over contained detailed personal information on the Hunters included in the relief force. Michael glanced at it, and a faint smile crossed his lips.

“Well done. What about assistance from countries other than Korea?”

“There is none at present. China could be a great help if it joined us, but it lost its core forces in the war against the Lich, and its relationship with Japan is poor. They will not respond to the request.”

China had already suffered enormous losses from the Lich and the terrorist attack that had taken place in Beijing ten days earlier.

Even for China, which possessed an immense number of Hunters, confronting an apex monster capable of causing a disaster on its own was an enormous burden.

Even more so when the country requesting assistance was Japan, with whom China had the worst possible diplomatic relationship.

“There is no need to worry about China. Even if the old Chairman wants to help Jin Taekyung, the circumstances at home will not permit it.”

Hearing those words, Huginn realized that there was something he had not yet been told.

“Are you planning to strike China again?”

“If anyone heard that, they might misunderstand. Terrorism is an unfortunate incident that no one can predict until it occurs. Don’t you agree?”

Under Michael’s unwavering gaze, Huginn lowered his head.

“My apologies. I misspoke.”

“Don’t worry about it. Everyone makes mistakes.”

“……”

“And this is only my personal opinion, but I suspect Shanghai may become the next target.”

His tone was casual, but Huginn could smell the thick blood embedded in those words.

Shanghai was China’s most populous major city.

Following Beijing, which had been targeted by the terrorist attack ten days ago, it was obvious that an enormous number of people would perish.

*China is certainly paying a steep price for siding with Jin Taekyung.*

When one thought about it, China was not the only country involved.

This series of incidents, which most people regarded as indiscriminate terrorism, contained an element of punishment directed at the countries and Guilds that had shown friendly attitudes toward Jin Taekyung.

*And the result will be one of two things.*

Huginn muttered inwardly as he looked at his superior.

There stood a conqueror with the greatest ambition in the world, advancing toward a grand objective.

But why was it?

*I have a bad feeling about this.*

The situation was unquestionably perfect.

Leviathan was a monster as powerful as the Lich.

And unlike the Lich subjugation, which had involved no fewer than six S-rank Hunters, Jin Taekyung could not expect any outside assistance this time beyond the forces already at his disposal, including Japan’s.

But…

*If Jin Taekyung manages to overcome even this…*

The thought came to him ominously.

Perhaps, just this once, his superior had made the wrong choice.

Perhaps this trap would instead become a sturdy rope that pulled Jin Taekyung out of the mire he had been trapped in.

However, Huginn’s worries were soon buried beneath a vibration that reached them.

*Rrrrrumble.*

“Entry into the operation area complete. Preparing to descend in ten seconds.”

The pilot’s report came through the speakers at the same time as the aircraft trembled. A moment later, his superior’s quiet voice reached Huginn’s ears.

“It has begun.”

Michael’s gaze had already turned toward the window, his body clad in dazzling silver armor.

A major city engulfed in monstrous cries and enormous flames.

There lay the battlefield where the name Michael Silbert would once again be etched into the minds of the entire world.

“Prepare yourself, Huginn.”

Pressing down a helmet engraved with a crown, Michael looked like an ancient god as he continued speaking to his crow.

“Prepare for me to become the undisputed best.”

The wait had been long, and the pain had run deep.

Now he wanted to paint himself across this world of vivid colors. Not Cheon Taemin, nor Jin Taekyung, but the name Michael Silbert.

* * *

Humanity, which ruled the five oceans and six continents, had given names of its own choosing to every living thing in the past and present.

Rabbits. Dogs. Cats. Horses. Dinosaurs…

But there were certainly exceptions.

Some beings passed down from the distant past possessed forms beyond humanity’s ability to comprehend and overwhelming power. It was difficult to explain them as anything else.

Much like the being now driving humanity toward catastrophe.

*Goooooong.*

A low cry reverberated in every direction.

Beneath deep waters filled with countless pieces of wreckage and mixed with blood, a gigantic mythical beast advanced with the waves, smashing and sweeping away everything that stood in its path.

*Craaaack!*

Some called it a crocodile. Others described it as a whale.

But in the end, humanity could not define it as anything.

It was far too enormous to be treated as a mere living creature, and it possessed a mysterious power that could not be explained.

Thus, it was called an inexplicable monster. And after the passage of countless years, it came to possess a single name that meant only itself in this world.

Far away, amid the screams of human beings, that name rang out.

“Le—Leviathan!”

“It’s an order! B-rank Hunters and below, withdraw from the battlefield immediately…!”

*WHOOOOOOM!*

The shouts and screams that had echoed so loudly vanished. A wave containing an overwhelming force swallowed and pulverized everything.

Humans. Buildings. Even the pitiful defensive Magic.

*Grrrrr.*

After unleashing waves dozens of meters high and sweeping them in every direction, Leviathan let out a satisfied growl.

It had truly been a long time.

Since it had awakened from its tedious sleep. Since it had rampaged freely like this.

*Yes. That was the last time.*

Leviathan thought of its master.

The Demon King Asmodeus.

An absolute ruler who had unified the chaotic Demon Realm and forced every monster into submission.

But Asmodeus, powerful as he had been, had eventually fallen to human hands, and Leviathan had retreated into the deep sea to sleep.

With its master gone, it could no longer obtain the enormous quantities of magical power and food it had once enjoyed. To survive until the day its master returned, it had needed to conserve its strength.

And its wait had not been in vain.

*It has changed. It cannot compare to the time when the Demon King was here, but it has definitely changed.*

Leviathan had been doubtful when it first awoke and crossed the ocean.

But the closer it came to this place, the more clearly it understood.

The abundant magical power permeating the water, the land, and the air.

And what, exactly, had awakened it from its sleep.

*…!*

At some point, Leviathan’s enormous pupils flashed.

In the deep waters that had become part of the sea, a powerful energy reached it from among countless pieces of wreckage and human corpses.

*That is…*

There was no mistake. This was the source of a monster’s power—the appetizing scent of a Magic Gem.

And not one touched by human hands, but a lump of pure magical power that retained all of its original energy.

An excellent source of food, more than enough to replenish the strength it had expended, had been waiting for Leviathan in the human settlement.

*So that was why.*

Leviathan realized how it had been able to awaken.

With the magical power that had seeped into this world, and something containing energy of that magnitude, it had been entirely possible.

Leviathan was the calamity and ruler of the sea. Its starving body, weakened by a long sleep, had responded to the waves of energy carried through the seawater.

*If I can make that magical power my own…*

Greed filled Leviathan’s eyes. A feast had been laid out before it. There was no reason to refuse.

*Whoooooosh.*

Leviathan surged forward.

As it advanced to swallow its prey, the water grew shallower and part of its back emerged from the sea, but the beast did not hesitate for even a moment.

It had already assessed the situation. The humans blocking its path were weak, and seawater that obeyed its will surged in every direction.

“It’s coming!”

“Lightning mages, prepare!”

“Ranged units, fire!”

*Fwish-fwish-fwish! Crackle!*

Countless arrows and lightning spells streaked through the air and plunged down. Hunters who had hastily gathered unleashed a concentrated volley with every ounce of strength they possessed.

And the result was so pitifully insignificant that it was almost tragic.

*BOOM-BOOM-BOOM!*

After a series of explosions, the Hunters widened their eyes at the sight revealed before them.

“What the…?”

A little scorching and dozens of wounds.

No—scratches.

That was the full extent of the damage they had inflicted on the monster before them. And the price that returned moments later was harsh.

*Whoooosh—BOOM!*

A massive tail suddenly emerged and struck the surface of the water.

Seeing the waves surge upward with a thunderous roar, the tanks at the front clenched their teeth. They shifted their weight onto their legs, which were half submerged in water, and layered their Tower Shields together to form a wall.

*Clack-clack-clack!*

Their movements were vigorous and as fast as lightning.

Though there were fewer than a hundred of them, everyone who had remained there was at least a B-rank Hunter. As seasoned warriors, they knew their duty.

“Formaaaaation!”

“Don’t retreat! Hold the line!”

“Protect us from the enemy, Great Shield!”

And at that moment, when the desperate shouts of the tanks blended with the mages’ incantations—

“Get lost.”

Along with Demon Realm language that no one there could understand, the enormous wave that had surged up around Leviathan advanced and split apart.

*Splaaash!*

One wave became dozens, and dozens became hundreds of streams of water. Filled with powerful magical power, they transformed into spears and descended upon the Hunters.

*KABOOOOOM!*

A shock wave arrived with a thunderous roar and shook everything around them.

Hundreds of spears made of water and magical power tore through the overlapping defensive Magic and crushed the Tower Shields that had stood before them like an iron wall.

*Crack! Thunk-thunk-thunk!*

“Urgh…!”

The water spears swallowed even the screams as they smashed through armor and cleaved bone and flesh.

As streams of water turned red with the blood they had absorbed, powerful winds blew over the heads of the Hunters collapsing to the ground.

*Tat-tat-tat-tat-tat!*

Propellers spun violently.

Dozens of unmanned fighter jets arrived through the storm and unleashed the guns and missiles mounted on their airframes without the slightest hesitation.

Destroying Leviathan?

They did not even dream of it.

Their only objective was to delay the monster, even for a brief moment, before the main force capable of confronting it arrived.

But contrary to the hopes of those watching the scene from the operations control room, Leviathan’s power and authority were simply too overwhelming.

*Goooooong.*

The primordial beast that controlled tidal waves and storms roared. Lightning fell from the sky, already filled with dark clouds, and swept over the unmanned fighter jets.

*Rrrrrumble—BOOM!*

Crashes and explosions. Or sinking.

At the center of that calamity, Leviathan advanced, dragging its enormous body forward.

It felt slightly fatigued after its long sleep and the considerable magical power it had already expended, but such things did not matter in the slightest.

The lump of magical power that was rapidly drawing closer even now.

As long as it had that thing, which gave off a scent so appetizing it could numb reason, it could recover its original strength.

It could cover this land in a tidal wave and make it its own.

*Grrrrraaaah.*

At last, with its prey before it, Leviathan opened its jaws wide.

Its maw, resembling that of a crocodile, swallowed in a single bite the corpses and wreckage submerged in the deep water—and the lump of magical power that existed somewhere among them.

No, it tried to swallow them.

The next moment—

If not for a streak of light that descended onto the rippling surface of the water.

*Fwoooooosh! Craaaack!*

Blue-white light-flames imbued with searing heat burned through the waves.
## Chapter artifact 749

# Chapter 749

Leviathan was both the calamity and the king of the sea.

That was true in the Demon Realm and on Earth alike.

The sea was Leviathan’s birthplace and undefeated battlefield, and within this vast territory granted to it at birth, there was nothing that could escape the king’s watch.

Yes, that was certainly how it should have been.

*Fwoooooosh!*

In the blink of an eye, the monster’s movement stopped with its prey before it, greed filling its thoughts. At the same time, Leviathan’s senses, numbed by its long starvation, awakened.

*What is this?*

When had it begun?

As realization dawned and the world slowed around it, Leviathan could see and feel everything clearly.

A mighty force, swift as lightning and carrying the heat of the sun.

The flames plunging down and swallowing the blue surface were headed straight for it.

*Splaaash!*

There was no time left to hesitate.

The enormous maw it had opened to swallow its prey turned sharply underwater.

A moment later, Leviathan crushed the flames with hundreds of teeth imbued with magical power.

No—it had believed, without the slightest doubt, that it could.

*Krrrk!*

That was what it believed until the instant the flames and its teeth collided, bringing a violent impact that shook its head.

*Krrrrrrk!*

—…!

What?

Leviathan’s enormous eyes widened in pain and shock.

The teeth that had sunk dozens of aircraft carriers during the Great Cataclysm—teeth so sharp and destructive that they were weapons in their own right—had been shattered in a single strike.

*How? How is this possible?*

Leviathan froze, caught in an unanswered question.

Then the countless bubbles stirred up by the collision scattered, revealing the cause of all its confusion.

A spear.

*Gooooong.*

The silver spear was wrapped in flames that refused to go out even amid the water and waves, and it trembled faintly.

As though it were a living creature.

As though it liked the touch of the hand holding it.

And flowing through the owner of that spear was the blood of a species Leviathan had killed countless times.

—How can a mere human…!

At the cry of the mythical beast, filled with undisguised astonishment, the small and insignificant human answered by merely moving his lips.

One Annihilation.

A distant flash of light dyed the sea.

* * *

People often say that life comes down to one big shot.

I agree—especially because when you go for that one shot, it can be the very shot that costs you your life.

*Rrrrrumble!*

A thunderous roar, as if the sky—or rather, the sea—were splitting apart.

At the same time, a tremendous shock wave sent my body flying after I had expended every ounce of strength.

Swept up in a whirling current, I could hear warning sounds ringing out endlessly through my fading vision.

*Beep. Beep-beep!*

> **System**
>
> - You have exhausted all your internal energy and stamina!
>
> - Your body cannot withstand the recoil of **One Annihilation**!
>
> - Status abnormality, **Internal Energy Depletion**, has been applied!
>
> - Status abnormality, **Exhaustion**, has been applied!
>
> - Status abnormality, **Anemia**, has been applied!
>
> - Status abnormality, **Muscle Tear**, has been applied!
>
> - Status abnormality, **Internal Injury**, has been applied!
>
> - Warning! Warning! Remember that every action comes with a price!
>
> - Excessive abuse of power may return as a blade turned against you.
>
> - Special debuff, **Broken Body**, has been applied!
>
> - All combat-related attributes decrease by 50 until recovery! Depending on the recovery process and its results, you may permanently lose some attributes!
>
> - **Strength** temporarily decreases by 50!
>
> - **Agility**…

.

.

.

High risk, high return.

That was exactly what it meant.

As I grew stronger, the power of One Annihilation had risen exponentially as well.

It had risen to the point that even this nearly perfect body—which people in Murim might mistake for a Heavenly Martial Physique—could no longer withstand it.

*Damn it.*

I was dizzy. My breathing was ragged.

My body had gone beyond exhaustion and fallen into ruin, screaming in agony, while my dantian, dry as a desert, begged me to stop.

The aftermath was severe enough that I could not even move a finger.

But if I had not anticipated a situation like this, I would never have attempted something as insane as firing One Annihilation in the first place.

*Open Inventory. Summon.*

The command entered into the System activated the instant I thought it.

Along with a silhouette that abruptly appeared in my blurred vision, someone’s curt voice rang out inside my head.

—You look awful. It’s a perfect look for you, you bastard.

I never thought that rude tone would sound so welcome.

Seeing me grin despite the pain, the Skeleton King clicked his tongue and shoved a small crystal bottle into my mouth.

A solution that could be used only in this world.

The treasure known as a Top-Grade Potion.

*Gulp.*

The instant I finally forced it down my throat, a refreshing energy spread through every corner of my body.

*Ding!*

> **System**
>
> - You have used **Top-Grade Potion**!
>
> - All status abnormalities have been removed!

My empty dantian filled to the brim. My torn muscles knitted back together, and my hazy vision became clear and sharp.

Its healing power was comparable to a Level Up.

But the warning that followed was something even I had not expected.

*Beep!*

> **System**
>
> - The special debuff, **Broken Body**, rejects the effect!
>
> - This debuff cannot be removed by artificial means!
>
> - The effects of **Broken Body** remain active!

*…What the hell?*

I was briefly flustered by the situation I had never experienced before, but I had no time to dwell on what the warning meant.

The battle was not over yet.

*Grrrrrrrrrrr!*

A roar that could be heard clearly even underwater.

Leviathan’s enormous body, impossible to hide even among the countless wrecks and corpses sunk deep beneath the sea, writhed in pain.

*KABOOOOOM!*

Though it was some distance away, Leviathan’s condition was horrifying at a glance.

The maw said to have once torn an aircraft carrier to pieces with a single bite had been ripped halfway off, along with one eye. Green blood poured from its flank, where the hide and bones had vanished, spreading across a radius of several hundred meters.

But even that was incredibly fortunate for the monster.

If it had not instinctively turned its head at the last moment—and if this had been land instead of underwater—it would have met its end long ago.

*I should have finished it with one strike.*

It was regrettable, but there was nothing I could do.

My opponent was Leviathan, the calamity of the sea.

They say even a stray dog gets the home-field advantage in its own yard, and fighting a creature born in the sea and ruling over it was several times more difficult underwater than fighting the Arch Lich.

But…

*I’ll kill it. I have to.*

*Splaaaaash!*

The Skeleton King and I shot forward at the same time. The powerful current blocking our path was no obstacle at all.

I wrapped my hand, fitted with transparent webbing, tightly around the spear shaft.

This was the effect of the **Water Rescue Worker** Title I had obtained after completing the Quest at Dongting Lake a few months ago.

Once activated, it lasted for only twenty-four hours. Worse, because it clashed with the **Scorching Yang Qi** I had learned, all my power was reduced by a full twenty percent.

Even so, the effect was worth every drawback.

*Fwoooooosh!*

I moved as quickly as though I were using a movement technique on land.

Leviathan, howling in pain, spotted us closing in and roared.

—GRAAAAAAAH!

The instant it opened its half-torn maw as wide as it could—

*Krrrk. Krrrrrk!*

The flow of the water changed.

Even though there was not a breath of wind underwater, everything around us was sucked toward Leviathan’s maw as if caught in a tornado.

It was a scene worthy of a disaster.

But I did not stop. Instead, I stepped on a nearby piece of wreckage and kicked off it, accelerating even further.

Toward the mythical monster.

Toward the powerful magical power writhing within it.

And then—

*Gooooong.*

The water and wreckage gathering around Leviathan burst outward in a massive wave.

*KRAAAAAAAASH!*

*Was this what the Breath of the dragons said to have once existed felt like?*

The wave of water, filled with tremendous magical power, shot forward, erasing everything in its path.

—You treacherous human!

The Skeleton King’s desperate shout came from behind me.

But I did not answer him.

Instead, I drew up the internal energy filling my lower dantian and embedded an undying flame into the blade of White Flame.

*Sssssss!*

Scorching heat spread in every direction.

The raging current and pressure melted away as though they had never existed. In place of the chill held by the sea, an energy like molten lava dominated the surroundings.

At least for this moment, this space belonged to me alone.

Nothing else could intrude.

*Cut.*

With that single thought dominating my mind, I brought down the spearhead.

Blue-white flames, stretching forward like a snake, lashed at the enormous wave that had reached the space directly before me.

No.

They cut it.

*Shhk!*

The wave split precisely in half and scattered to either side.

In that instant, I saw Leviathan’s eyes widen in shock.

And I saw its enormous body swimming away at an unbelievable speed toward something in the distance, something scattering a chilling energy.

*The Magic Gem!*

I finally understood.

Why the monster that had disappeared for decades had suddenly revealed itself.

What had drawn it to this archipelago.

—Stop it!

The Skeleton King thrust out a hand with a scream.

Bones rose upward like a growing tree and forcefully pushed against the tips of my feet.

*Bang!*

My body shot forward with a dull boom, and I advanced toward Leviathan, cutting through the powerful current.

*GRAAAAAH! KRRRUNCH!*

Its crocodile-like maw swallowed a massive piece of wreckage.

Steel beams that had once been a cargo ship.

A pile of concrete from a collapsed building.

And along with them, something infinitely smaller by comparison, yet carrying an energy more dangerous than anything else.

*Crunch.*

Leviathan chewed and swallowed everything in a single bite before turning its head.

It watched me draw closer with eyes that held both fear and mockery, then swam away at a speed I had never seen before.

Not toward me or the Skeleton King, but toward the vast sea from which it had come.

—It’ll take time for it to absorb the energy! Kill it before then!

Hearing the Skeleton King’s shout, I gripped White Flame in reverse.

The distance between Leviathan and me was barely a hundred meters.

But no matter how powerful the effect of the **Water Rescue Worker** Title was, I could not catch up to Leviathan’s speed.

*Once. Just once.*

I gathered every bit of internal energy I had left and poured it into the spearhead.

*This time… I’ll finish it. I have to.*

I focused all my attention.

I felt the flow of the water and calmed my breathing. Every nerve and muscle throughout my body seemed to awaken one by one, gathering toward my fingertips and shoulder.

*Krrrrrk.*

Then, at the instant the veins across my entire body stood out—

Like releasing a tightly drawn bowstring, I hurled the spear forward with every ounce of strength I possessed.

*KRAAAAAAAASH!*

A single line of flame streaked across the deep water.

But there was no monster’s scream at the end of it.

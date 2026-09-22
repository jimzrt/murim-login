# Checkpoint Review — 705–709

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

# Chapters 705–709

## Plot

The three-hundred-warrior Baekcheon Unit arrives under Wang Ho, revealing that Baeksang secretly trained the Bai warriors and ordered them to follow Yayul Cheok against Dark Heaven. Joined by roughly three thousand warriors awakened by the Beast King Stone, Yayul rallies an army of approximately thirteen thousand against the Southern Heaven Demon Empress. Her five hundred elites have been annihilated, and the mutants retreat before the sacred stone’s light.

The Empress raises a dragon tornado and enters a desperate battle with the Beast Miao King. The allied forces suffer heavy losses, including more than half the Baekcheon Unit, while Jin Taekyung fights the mutants from the guardian spirit’s back with White Flame despite his injuries and depleted Internal Energy. After killing the transformed Nanman tribespeople, Jin continues toward the Empress, refusing to consider the disaster finished while she lives.

The Beast Miao King overwhelms the exhausted Empress, but she awakens the innate qi she has carried since birth through the rift. Baeksang emerges from the ruins and stabs her from behind, disrupting her final attack. The resulting explosion gravely wounds Baeksang, Yayul Cheok, the White Tiger, and many others. The sacred stone shrinks to the size of a child’s fist, and its light fades.

Rather than flee with the guardian spirit, Jin returns to the battlefield to help the surviving Baekcheon warriors. Inspired by him, Wang Ho changes their objective from delaying the Empress to killing her. Fewer than twenty warriors remain. Jin drives White Flame through the Empress’s chest, but his heart meridian tears and he reaches the brink of death. As she tries to finish him with her remaining hand, an unidentified attacker destroys her arm and coldly insults her.

## Continuity

- Yayul Cheok leads approximately thirteen thousand allied Nanman and Bai warriors against the Southern Heaven Demon Empress.
- Wang Ho commands the Baekcheon Unit; fewer than twenty warriors remain after the battle.
- Baeksang secretly trained the Baekcheon Unit and arrived to stab the Empress, but was flung away with catastrophic injuries. His fate is unresolved.
- The Empress’s five hundred elite subordinates have been annihilated or captured.
- The mutants are retreating or have been killed; they were transformed Nanman tribespeople who retained their martial arts.
- The Empress is critically wounded, has lost her only arm, and continues consuming her remaining life force and innate qi.
- Jin Taekyung has driven White Flame through the Empress’s chest, but his heart meridian is torn and he is near death.
- Yayul Cheok is unconscious and gravely wounded by embedded sword fragments after shielding Jin from the explosion.
- The White Tiger is gravely wounded, and the sacred stone has diminished to roughly the size of a child’s fist with only faint light remaining.
- The guardian spirit urged Jin to flee but remains with him; the future of the guardian spirit and sacred stone is unresolved.
- The unidentified attacker who destroyed the Empress’s arm has not been identified.
- The Nanman Beast Palace has suffered catastrophic damage but has not completely collapsed.

## Translation Decisions

- Retain **Southern Heaven Demon Empress**, **Honglan**, **guardian spirit**, **White Tiger**, **Beast King Stone**, **sacred stone**, **Baekcheon Unit**, **Beast Miao King**, **Dark Heaven**, **Force**, **demonic qi**, **innate qi**, **White Flame**, and **Fiend**.
- Render **경천동지** as **cataclysm**, **심맥** as **heart meridian**, and **수도** as **hand blade**.
- Use **Palace Lord** for 궁주, **Commander of the Baekcheon Unit** for 백천대주, and **Dai people** for 태족.
- Preserve Jin Taekyung’s conversational profanity and first-person voice, along with the guardian spirit’s terse, compassionate telepathic dialogue.

## Durable state

{
  "active_continuity": [
    "Jin Taekyung has returned to the battlefield and is fighting beside the Baekcheon Unit so they can survive together.",
    "Fewer than twenty Baekcheon Unit warriors remain in the assault on the Southern Heaven Demon Empress.",
    "Jin Taekyung has driven White Flame through the Southern Heaven Demon Empress's chest.",
    "Jin Taekyung's heart meridian is torn and he is at the brink of death.",
    "The Southern Heaven Demon Empress is critically wounded and continues burning through her remaining innate qi.",
    "The Southern Heaven Demon Empress attempts to kill Jin Taekyung before she dies.",
    "An unidentified attacker has destroyed the Southern Heaven Demon Empress's only arm."
  ],
  "continuity_sources": [
    709
  ],
  "open_questions": [
    "Will Jin Taekyung and the Southern Heaven Demon Empress survive their mutually fatal injuries?",
    "Who is the unidentified attacker who intervened against the Southern Heaven Demon Empress?",
    "Will Baeksang survive his catastrophic injuries?",
    "Will Yayul Cheok and the White Tiger survive their wounds?",
    "What will happen to the diminished sacred stone and the guardian spirit?"
  ],
  "safe_through": 709,
  "temporary_decisions": [
    "Render 경천동지 as cataclysm.",
    "Retain innate qi, Force, divine artifact, sacred stone, Baekcheon Unit, and Fiend.",
    "Preserve the guardian spirit's telepathic dialogue with em dashes.",
    "Preserve Jin Taekyung's first-person conversational voice.",
    "Render 심맥 as heart meridian and 수도 as hand blade."
  ],
  "version": 1
}

## Reading copies

## Chapter artifact 705

# Chapter 705

“Commander of the Baekcheon Unit Wang Ho, paying his respects to the Palace Lord.”

The moment she heard those first words, the Southern Heaven Demon Empress thought the world had stopped.

At the same time, within the slowed passage of time, everything surrounding her surged toward her like waves and obscured her vision.

Not the pitch-black martial uniforms that were practically the symbol of Dark Heaven, but clothing and armor as white as snow.

Three hundred warriors whose clothing and features clearly marked them as Bai people, along with beasts that let out low growls.

And then…

Flap.

A single flag fluttered in a breeze that had blown in from somewhere, bearing three characters scrawled in a vigorous, soaring hand.

Baekcheon Unit.

“……!”

The Southern Heaven Demon Empress’s pupils trembled.

She did not understand.

Why did those characters beneath the endless dark sky, or that old silk fluttering in the wind after having yellowed with the passage of considerable time, unsettle her so deeply?

And why were memories she had once dismissed as insignificant surfacing again at this very moment?

*Demon Empress. Baeksang is secretly training warriors and beasts. They are made up exclusively of Bai people, but after investigating them thoroughly, most of them…*

*Orphans who lost their parents in the Great Faction War or to the plague. Their whereabouts became unknown after the great fire several years ago.*

*Y-you knew?*

*Yes. For a long time. He probably established a hideout in a place called Wenshan, didn’t he?*

*Th-then, may this lowly servant dare ask the Demon Empress just one thing?*

*You’re curious, aren’t you? Why I only watch even though I know everything.*

*Forgive my impertinence, but yes. Even now, a considerable portion of the vast supplies flowing to Baeksang is being used to train warriors. If he should ever harbor different intentions…*

*So what? It’s amusing.*

*Pardon?*

*Think about it. What could possibly change just because he feeds elixirs to orphans who have nowhere to go and teaches them a few forms of martial arts?*

*Th-that…*

*No matter how many times you hammer scrap iron, it remains scrap iron. You can never create a divine weapon from that. But… I find it rather entertaining. Watching Baeksang struggle desperately to hold on to scrap iron while inflated with a vain dream. Imagining the expression he’ll make when that hope turns into despair is amusing, too.*

*……!*

*And Baeksang could never harbor different intentions. Even if something like that happened, it would merely become another source of amusement for me.*

That had happened more than a dozen years ago.

That spy who had risen to the position of Great Chieftain at a young age had beaten his head against the floor until blood ran from his forehead before leaving, and the Southern Heaven Demon Empress had naturally forgotten about him.

No—she had erased him from her mind entirely.

The events taking place in a remote mountain valley untouched by human footsteps had gradually faded from the Southern Heaven Demon Empress’s attention as well.

*It was far too insignificant to keep watching.*

It was only natural. She held Baeksang’s leash, and even if he cut it himself and charged at her, she possessed more than enough power to crush him to death in an instant.

The arrogance and leisure born from overwhelming strength—things only the powerful could display.

But only now did the Southern Heaven Demon Empress realize.

The hunting dog named Baeksang, whom she had believed could never betray her, had cut his own leash one day.

Her own arrogance had brought them all here today.

“……Baekcheon. The Baekcheon Unit.”

The Southern Heaven Demon Empress muttered the words like a groan.

While she dreamed of the dark sky that would soon arrive, someone else had been looking up at a sky with white clouds drifting across it.

No. He had kept it in his heart.

Even while following someone as a hunting dog wearing a leash he had never wanted, even while knowing that path was wrong, he must have written those characters while filled with guilt and anger at having no choice but to continue.

On that yellowed, worn silk that had once been dazzlingly white, he must have drawn the sky he had wanted to see.

And the wish he could not fulfill with his own hands had been passed on to one person.

“Leave. I have already cleared the East Gate. The guards at the underground prison will be more lax than usual, so the Han Chinese should be able to escape this place without much difficulty.”

“……!”

At the low voice that echoed through the space, Jin Taekyung let out a groan as he stared wide-eyed, alternating his gaze between the Baekcheon Unit and the Beast Miao King.

“No way.”

It felt as though the scattered pieces were slowly fitting together.

The Beast Miao King stared at the Southern Heaven Demon Empress with bloodshot eyes and continued the words he had heard from someone’s mouth several days earlier.

“Go straight to Wenshan, which lies to the northeast. Then show this to those staying on its highest peak.”

Whoosh. Clatter.

Something slipped from the Beast Miao King’s hand, traced an arc through the air, and landed at the Southern Heaven Demon Empress’s feet.

Made of jade, it was one half of someone’s split identification token—and the sole token of authority capable of mobilizing the Baekcheon Unit.

“I have already walked an irreversible path. I cannot stop of my own will, and even if I did stop, it would not be enough to prevent the grand scheme.”

The Beast Miao King’s voice trembled.

Inside the sleeping quarters, where dim light lingered, the face of his sworn brother seemed to flash before his eyes—the man who had severed with his own hand the wrist a swordsman valued as much as life itself.

Along with the last words Baeksang had spoken to him.

“I will never stop. So… Palace Lord, you must not stop either. Continue to the end with that boy, Jin Taekyung. Take a different path from mine.”

That was all.

The sworn elder brother had left, and the sworn younger brother had remained.

And three days later, the Baekcheon Unit had knelt before the token in the Beast Miao King’s hand.

They remembered the request of the one man who had become a father and teacher to them after they lost their homes and families.

*If someday someone other than me brings this token, he is the lord you must serve.*

Thus, the three hundred warriors who had slept in a remote mountain valley for decades descended from the mountains behind the Beast Miao King.

Rumors of warriors racing fearlessly across the wilderness spread quietly—and swiftly.

*The Palace Lord has returned!*

*Our Dai people will join the Palace Lord! Protect this land from the traitors who colluded with Dark Heaven, usurped the Palace Lord’s position, and betrayed Nanman!*

*Mobilize every warrior at once. Send out the messengers!*

As many as ten thousand warriors headed for the Nanman Beast Palace, leaving behind a vacuum of equal size.

The tribal chieftains who had rebelled against Baeksang and left the Nanman Beast Palace led their warriors to join their true Palace Lord.

*You all…*

*We will follow you with our lives, Palace Lord.*

One day. Then another.

Before long, they had become a massive army and were racing toward the Nanman Beast Palace when they encountered an unexpected enemy.

No—they thought it was an enemy.

A large force numbering roughly three thousand.

That was how they saw it until a Bai man at the head of the army stepped forward alone and knelt.

*We surrender.*

The Beast Miao King asked him why, and the Bai man answered with a vacant expression.

*The being who protects the divine artifact awakened everyone, including me. It showed us which path was right and what choice we needed to make.*

The Beast King Stone was a legend and a miracle.

And that day, the Bai man—no, the Captain of the Guards—was not the only one who witnessed the wondrous sight on Ailao Mountain.

*That Han Chinese bastard. No, Great Hero Jin Taekyung told us to find the Palace Lord as quickly as possible. He said that if we delayed any longer, everything would be over.*

Once the three thousand warriors who had surrounded Ailao Mountain joined them, there was nothing capable of stopping them.

Not the rugged mountains, nor the deep swamps and dense jungles.

The same was true of the group that realized something had gone wrong and hurried toward the Nanman Beast Palace.

“I had to rush to the Inner Palace and didn’t see it through to the end. How did the battle turn out?”

At the Beast Miao King’s sudden question, his gaze fixed on the Southern Heaven Demon Empress, Commander of the Baekcheon Unit Wang Ho wiped the blood from his cheek and answered.

The heat of the battle that had yet to fade still burned in his eyes.

“We suffered two hundred casualties.”

“And them?”

“Annihilated. We killed or captured every last one of them.”

Watching the entire situation unfold, Jin Taekyung let out a quiet laugh. He did not know the details, but he could more than guess how things were going.

“Old hag. You’re fucked, huh?”

“……!”

The Southern Heaven Demon Empress clenched her teeth before she could stop herself.

A bitter scent of blood filled her mouth.

Dead. Every last one of them.

No fewer than five hundred elites had been slaughtered.

The thousands of warriors who had stormed in with the Beast Miao King had trampled the final move that could have overturned this precarious situation in an instant.

*No. No, this is impossible…!*

Unbearable fury boiled within her. At the same time, an even greater sense of unease and a cold chill lingered in her chest.

The two characters filling the Southern Heaven Demon Empress’s mind now were death.

*…Die? I’m going to die? Me?*

She could not believe it.

She had lived for more than one hundred and thirty years.

Since her youth, she had used every means available to become beautiful and preserve her youth, building formidable martial prowess in the process of repeatedly abandoning all human morality.

Even if she were to meet her end someday, she had never imagined dying at someone else’s hands.

But that absurd fantasy—something she had never once considered—was now becoming reality and striding toward her eyes.

Along with killing intent as sharp as a pointed awl.

Thump.

Hundreds of feet stepped forward at once, their combined impact spreading as a tremendous echo.

Grrrr.

The beasts carrying the warriors on their backs let out low growls.

Light flowed outward from the largest White Tiger among them, wrapping around them all and protecting them from the darkness.

Fwoooosh.

It was faint, but unmistakable.

The mutants felt the power of the sacred stone that had shared its fate with this land throughout the distant ages, and instinctively stepped backward.

No—perhaps they had felt it, too.

That they could not win a battle against these people.

That even with bodies made more vicious and powerful, the outcome would not change—not even if the Southern Heaven Demon Empress leading them joined the fight.

—Krrk.

—Kk.

The bizarre cries echoed like groans.

There were nearly a thousand monsters, each with an appearance as hideous as the sounds they made.

Yet the Baekcheon Unit did not waver even a fraction as they aimed their weapons, drenched in the blood of the enemies they had faced before, at the mutants.

Shing.

Hundreds of spears and blades flashed in the hazy light.

Several decades ago, someone had been wrong to call them scrap iron and regard them as nothing more than a form of entertainment.

No.

Perhaps it had been true—at least back then.

But the scrap iron that was endlessly hammered, cooled, and heated was transformed anew at some point.

Into hard steel.

Then into sharp, famed swords capable of cutting even steel.

And there was only one person in all the world capable of wielding the famed sword known as the Baekcheon Unit.

“Give us your command, Palace Lord. No…”

A middle-aged man whose black hair had turned half gray with the passage of time—the Commander of the Baekcheon Unit, Wang Ho—spoke in a weighty voice.

“My lord.”

At the same time, his gaze—and the gaze of every member of the Baekcheon Unit—shifted in one direction.

Then the lips of the giant who had stood tall before them all like an iron tower opened.

The Beast Miao King, Yayul Cheok.

“I will advance. Follow me.”

“As you command.”

That was all.

The next moment, they advanced together.

Like a wave beginning in the middle of the ocean.

Like an arrow leaving its bowstring.

Like a single bolt of lightning.

And at the front, alongside the Beast Miao King, was the enormous body of a White Tiger shooting forward.

—Kraaaaaaang!

Krrrunch!

With a roar that shook heaven and earth, its forepaw swung down and tore apart and crushed everything in its path.

Gripping the guardian spirit’s mane, white enough to match his own pallor, Jin Taekyung muttered,

“No, fuck. I’m exhausted enough to die, so why the hell am I—”

But his dismayed mood at the sudden acceleration, along with his suspicion that the guardian spirit might be some kind of Korean-made tiger, vanished the very next moment.

To be precise, they had no choice but to vanish.

Gooooong.

The air froze in an instant.

At the center of a dragon-tornado rising as it pulled in the surrounding darkness, the Southern Heaven Demon Empress lifted her head.

Jin Taekyung yanked the guardian spirit’s mane backward at lightning speed.

His ace in the hole: reverse gear.

The guardian spirit understood his intention perfectly and hurled its body away.

Forward.

Whoosh!

—Hold on tight, human!

“……”

No, fuck.
## Chapter artifact 706

# Chapter 706

A thought suddenly occurred to me.

*Can’t I sit this one out now?*

The greater good. A spirit of self-sacrifice. Self-sacrifice unto death. And so on.

They were all good words. Warm enough, but also a little embarrassing. They were good words, sure, but…

*I feel like I’ve done plenty of that already.*

I had come all the way to this cursed continent-sized greenbelt for the greater good, and I had fought while wearing my spirit of self-sacrifice over my entire body—so thoroughly that it might as well have been tattooed onto me.

No, considering how many battles I had fought in Nanman, even calling it fighting felt unfair.

I had fought a fucking lot.

In forests. On plains. In swamps and jungles.

I had driven spearheads into the bodies of spiders the size of houses. Against the Nanman warriors who swarmed toward me without pause, hungry for glory, I had answered with fire and fists.

It would have been better if things had ended there.

At the Poisonblood Grounds, I had found myself in the insane situation of facing two Supreme Peak masters at once. And before I had even fully recovered from those injuries, I had been forced to fight a monster known as the Southern Heaven Demon Empress.

*And then there was One Annihilation.*

One Annihilation.

It literally meant killing everything with a single strike, but lately, I had begun to wonder whether *everything* included me.

What the fuck was I pouring into that one blow? My internal energy—or my lifespan?

Still, things had not turned out too badly. Just when I had been wondering whether that was the day I would see the ending of my life, the Beast Miao King and the Baekcheon Unit had appeared. With the Beast Miao King’s help, I had partially recovered from my Internal Injury, and I had also learned that allies were already swarming outside the Inner Palace.

The fact that the battle had turned in our favor finally let me breathe a little easier.

At least until a certain insane tiger suddenly accelerated.

Whoosh!

No, fuck. Was this guy’s staple food Frosted Flakes?

I had sensed it from the first time we encountered him on Ailao Mountain, but the guardian spirit was faster than the three hundred members of the Baekcheon Unit—and even faster than the Beast Miao King.

Across the vast Inner Palace, now reduced to ruins, one thousand mutants formed a wall like an iron rampart.

Toward the Southern Heaven Demon Empress beyond them, the guardian spirit’s silver body shot forward like the wind.

As I heard the guardian spirit’s thought echo through my mind, I thought,

—Hold on tight, human!

*Is this an assassination attempt…?*

It happened at that exact moment.

A massive, murky light burst above the heads of the mutants.

Kraaaaaaash!

—Duck.

Along with the brief thought, the guardian spirit tilted its body. Its powerful forepaw struck the ground, and its enormous body changed direction at an angle.

Whoosh!

Its senses and movements were truly worthy of a spiritual creature—or rather, the term *divine beast* seemed even more appropriate.

The Southern Heaven Demon Empress’s palm strike, packed with tremendous internal energy, missed its target and slammed into the ground.

Boom! Rumble, rumble!

A cloud of dust rose with the explosion.

At the same time, I brought the spearhead of White Flame down toward the countless fragments that flew through the air and came crashing toward us.

Whoosh!

The spearhead split the air with a shrill whistle. The countless fragments thrown outward by the impact of the palm strike were reduced to powder and scattered on the wind.

And then—

Thud-thud-thud-thud!

Hundreds of figures mounted on enormous beasts shot through the surrounding darkness and the pale cloud of dust.

A triangular wedge formation carrying tremendous weight and momentum.

At its tip, a middle-aged man with half-gray hair thrust out one fist.

The Beast Miao King.

Fwoom! Boom!

There was no furious shout. No command.

But the green Fist Force that erupted in place of his voice crushed dozens of mutants in an instant, opening a gap. Three hundred charging spears became sharp awls and drove into it.

Kra-crack!

Blood burst into the air, and severed limbs flew high above the ground.

One thousand against three hundred. Humans and beasts against monsters.

Slice! Slice!

Whoosh, stab-stab-stab!

“Guh!”

—Kraaaaaaang!

Horrible screams and the sounds of cutting rang out in every direction.

What awaited the Baekcheon Unit after their initial charge crushed hundreds of mutants was a fierce close-quarters battle. Beyond it, the Beast Miao King shot toward the true enemy waiting for him.

“Southern Heaven Demon Empress!”

His body surged forward like a streak of light alongside his roar. A moment later, the aftermath of their collision, carrying a distant flash of light, shook the foundations of the earth.

Boom! Rumble!

Countless movements tangled together, along with sharp weapons flashing in every direction. Above their heads, the darkness slowly scattered under the pressure of the green Force.

*The Southern Heaven Demon Empress is already exhausted. The Beast Miao King has the advantage.*

But the battlefield that had descended into close combat was not going well.

The beasts that had grown even larger and stronger through mutation were no weaker than First Rate masters. The warriors who retained all the martial arts they had possessed as humans moved at speeds incomparable to before as they targeted the Baekcheon Unit.

Just like now.

Whoosh, slice!

A mutant’s head flew into the air with a sharp cutting sound.

Only belatedly realizing what had happened behind him, the Baekcheon warrior stared at me with wide eyes.

“No matter how busy you are, you should watch your back.”

“Thank you. But you are…?”

The Beast Miao King, or the Baekcheon Unit.

As I hesitated for a moment between those two choices, I answered,

“I’m an ally. I’ll lead the way, so follow me.”

It was a choice I could not avoid.

The Baekcheon Unit could stand against such overwhelming numbers because every single one of its members had reached at least the realm of a Supreme First Rate master. The mutants, whose bodies had been completely consumed by demonic qi, were powerful.

With the Beast Miao King no longer acting as their rallying point, the guardian spirit and I had to take the lead.

“…Shit. Now that I think about it, why the hell am I—”

—Am I imagining it, or do you seem to fight just fine while complaining?

“Tell me honestly. You have a grudge against me, don’t you?”

Crack!

Whether driven by the ferocity granted by demonic qi or by loyalty to the commander it sought to protect, a mutant charged out of the hazy dust cloud and filled my vision—only for the guardian spirit to crush it in a single blow.

—A grudge?

“Don’t play dumb, you bastard. You accelerated like your life depended on it because I set fire to Ailao Mountain.”

Kra-crack!

Four or five heads tore free under a single sweep of its forepaw. The guardian spirit clicked its tongue—despite being a tiger—and answered,

—How ridiculous.

“Are you sure?”

—No.

“Then is this revenge for the Thousand-Year Spider that lived upstairs?”

—What nonsense are you spouting now?

“I thought about it carefully, and the whole thing is suspicious. You know what they say. *Our friendly neighborhood Thousand-Year Spider… up!*”

Stab!

With my shout, the spearhead of White Flame shot out and pierced straight through the head of the tiger that had leaped toward us, casting a shadow over the guardian spirit’s head.

Grrrk…

The cry quickly faded away. With the tiger’s life extinguished in its death rattle and its body still impaled on my spearhead, I swung it with all my strength.

Fwoom! Crack!

The carcass, weighing several hundred pounds at least, flew through the air and crushed other mutants.

“Unless you’re consumed by a grudge, why would you throw a patient who needs to recuperate into a mess like this? That’s the conclusion I reached.”

Whoosh! Slice!

Five heads flew into the air along the path of the spearhead as I swept it sideways like flowing water.

The headless corpses collapsed at the same speed they had charged. The guardian spirit stared blankly at the sight and muttered,

—I think you mean a different kind of patient from the one I know.

“Are you insane? Can’t you see my condition?”

—I’m saying this because I’m looking at it directly.

“That’s only because you don’t understand my condition. Even breathing makes my bones ache.”

Stab!

—You keep stabbing meaty things here and there with your spear. Don’t say that as though it’s convincing.

“Damn it. I’m only doing this because I’m trying to survive somehow…”

—Do you know something?

“What?”

—For a human, you are remarkably bad at lying.

“What does that—”

I did not even have time to finish.

Crack! Whoosh!

A silver mane wet with blood scattered through the air. The guardian spirit leaped upward after bursting a mutant’s head, then swung its forepaw as it descended.

Its hooklike claws carried blade-sharp wind and an energy that could only be called Force.

Boom! Rumble!

One strike.

Amid the thunderous sound and the vibrations, dozens of mutants were sent flying as bloody pulp, and even more mutants rushed forward to fill the empty space.

Whoosh!

—Kweeeek!

Their movements were swift and ferocious, completely at odds with their grotesque cries.

Sword Energy pouring in streams from the weapons of several mutants was proof that they had once been warriors renowned even in Nanman.

But…

—Kraaaaaaang!

The guardian of the sacred stone, existing solely for its sake.

At the roar of the enormous White Tiger, a creature no one else had ever seen, the mutants’ bodies froze.

At the same time, as though we had arranged it beforehand, I brought White Flame down at an angle.

*Cut them. All at once.*

The Scorching Yang Qi that had amounted to three jiazi was gone. So was the blue-white flame that had once wound around the transparent spearhead and burned.

All I had left now was a body as heavy as waterlogged cotton, along with a small amount of internal energy—so little that I wondered whether it could fill even one handful—and the only divine weapon I could still trust: White Flame.

That was all, without a doubt, but…

I did not know.

Slice!

Why I kept cutting without pause.

Stab!

Why I kept stabbing.

Crack!

Why I kept swinging my spear as I fought the mutants.

Why, even then, I forced strength into my aching legs to keep from falling off the guardian spirit’s back.

No. Perhaps I dimly understood.

Even the meaning behind what the guardian spirit had said to me moments earlier.

“…Damn it.”

At the curse that slipped from my lips before I could stop it, the guardian spirit laughed softly.

—I told you. You are bad at lying.

“…”

—If you wanted to live, you would never have come here in the first place. And yet, even though you are exhausted, you refuse to stop fighting.

“Enough. Shut up.”

—Why is that? Because you pity those who were once human like you before falling into monsters? Or because you want to kill the vile human who turned them into monsters?

“……!”

The moment I heard the thought that seemed to whisper inside my head, I found it hard to breathe. Something hot surged up from deep inside my chest.

But the hand I thrust forward was still driving my spear toward another mutant’s throat.

Thrust!

The transparent spearhead tore through flesh and severed bone. I saw the darkness slowly recede from the opponent’s eyes, which had been stained completely black without a trace of white.

And in that empty space, I saw death settle in.

Thud.

The body collapsed. I stared at the unknown warrior whose life had ended with his face twisted grotesquely, then muttered,

“Did he feel pain?”

—Yes. Probably.

Crack!

A leopard that had charged at me the moment I stopped moving was sent flying like a cannonball.

The guardian spirit swung its massive forepaw and killed the mutant, then continued in a calm voice.

—But after that brief moment of pain, a great and warm rest must have been waiting. For those people, simply being alive must be agony.

“……!”

—They do not resent you. So, human. Stop blaming yourself.

Damn it.

I knew that. I had done my best. I had always fought while risking death, and I had come all this way to stop a terrible disaster.

But as always, the best effort did not necessarily produce the best result.

*I should have stopped it.*

In the end, I had failed to stop it. I had saved many people, but I had also failed to save many others.

Ultimately, the only thing I could do was end their lives with everything I had.

Just like now.

Fwoooooosh!

The spearhead I swung with all my strength tore through the wind and split the air. At the same time, my entire body, which had endured the full aftermath of One Annihilation, screamed.

A burst of agony so intense that my vision turned white.

But I gritted my teeth and endured it. I sent a single spear packed with terrifying strength and speed toward the people who had once been human like me.

Kra-crack!

The spearhead carved a huge arc through the air. At its end, a raging gale became soaked in dark red blood.

Severed heads and limbs flew through the air, followed by countless deaths and moments of rest.

Ding. Ding. Ding.

This was the first time.

The first time I had wanted to cover my ears at the clear ringing of the chimes announcing EXP gained. The first time the sight of my enemies collapsing while spraying blood had felt so unbearably sorrowful.

But I did not stop moving.

Slice. Slice. Slice!

I cut.

I cut again.

And I cut once more.

Until everything blocking the road ahead had disappeared. Until the spearhead cut through nothing but empty air.

Fwoom!

The world tilted.

No—the body that could not withstand the force carried by the spearhead tilted.

And in the next moment, just as I began to roll from the guardian spirit’s back, a rough hand caught me.

“It’s over. Please stop.”

Commander of the Baekcheon Unit Wang Ho.

Breathing harshly at the astonishment and shock in his voice, I looked around.

The Baekcheon Unit had been reduced by more than half. Countless corpses lay submerged in pools of blood gathered in every direction.

But…

*No.*

He was wrong.

This fight—and today’s disaster—was not over.

Not until I had snuffed out one particular person’s life for good.

“Let’s go.”

—…Human.

“We have to finish it.”

At my voice, which slipped through cracked lips, the guardian spirit seemed about to answer. Instead, it pushed its heavy body forward.

Whoosh!

Wind swept over my entire body.

At the end of the road we were traveling, one person was struggling to live despite vomiting blood.

No.

There was a monster.
## Chapter artifact 707

# Chapter 707

The Southern Heaven Demon Empress could not understand.

Why had the grand plan she had never doubted would be perfect fallen into such disarray? And why had she been reduced to the humiliation of matching a mere member of the Ten Kings?

But she had no time to continue wondering.

Whoosh!

A fierce sound of splitting air crushed the wind.

A massive figure surged forward, erasing the space around it. Green Fist Force erupted from the Beast Miao King’s fist, illuminating the world.

Kraaaaaaash!

It had not been that long ago.

If this had been the Southern Heaven Demon Empress of the past—or even the Southern Heaven Demon Empress from just two shichen ago—she would have snorted and deflected that Fist Force.

Even though the Beast Miao King was one of the Ten Kings, and even if he had been relatively underestimated because he was from Nanman, he was clearly a level below her.

That was how it had been.

Until someone’s attack took one of her arms and tore open her side.

*Jin Taekyung.*

A single name that filled her with rage merely by bringing it to mind.

Gritting her teeth, the Southern Heaven Demon Empress thrust out a foot. Her figure vanished.

The Beast Miao King realized that his attack had failed to connect and reacted instantly.

Whoosh!

His towering body stood over eight feet tall. Yet the Beast Miao King moved like the wind, and his tiger eyes, from which flames poured in streams, were already fixed on the Southern Heaven Demon Empress as she rushed toward his side.

Shwaaak!

His enormous hand, as large as a tiger’s forepaw, raked across the air.

Slice!

The wind that rose like a blade cut through the hem of her robe. At that instant, the Southern Heaven Demon Empress leaped into the Beast Miao King’s reach and thrust out a palm with all her strength.

Whoosh!

Under normal circumstances, that strike should have crushed flesh and burst bone and internal organs.

But waiting for the Southern Heaven Demon Empress’s small hand, drenched in blood, was the Beast Miao King’s palm—several times larger than hers.

Boom!

The world shook.

At the same time, murky internal energy, as though laced with deadly poison, flowed toward the point where their palms met and churned one person’s insides.

But the Beast Miao King swallowed the blood surging up his throat and grinned.

“So this is all you’ve got?”

“……!”

The Southern Heaven Demon Empress’s eyes widened.

It was unbelievable. That the Beast Miao King could smile even in a situation like this.

And that her full-strength palm strike had become so pathetically weak.

Crack.

At that moment, blood trickled through the gaps between her clenched teeth, and the Southern Heaven Demon Empress’s figure blurred.

Whoosh-whoosh-whoosh—boom!

Compressed air burst outward with a series of sharp reports.

In the span of an instant, her hands and feet struck every part of the Beast Miao King’s body like flashes of lightning, making his massive frame jolt.

But that was all.

The external arts he had trained for countless years had hardened the Beast Miao King’s body until it was as tough as steel. And the Southern Heaven Demon Empress’s attacks—which should long ago have left the Beast Miao King vomiting blood and collapsing to his knees—were no longer as heavy as before.

No. Their power was gradually diminishing.

The demonic qi flowing from the rift was strengthening her, but it could not undo the massive injuries Jin Taekyung had inflicted on her earlier, nor could it repair the mental strength that had been thrown into disorder as a result.

And the first person to realize this was none other than the Southern Heaven Demon Empress herself.

*…Tired? Me?*

Everything had a limit. But at some point, the Southern Heaven Demon Empress had forgotten her own.

She had no choice but to forget it.

She had not felt her limits in a very long time. No one had been able to push her that far.

Until now.

Whoosh—crack!

The relentless sounds of splitting air, ringing as if something were chasing her, abruptly stopped.

At that moment, the Southern Heaven Demon Empress felt a sharp pain travel through her hand.

Crack.

The bones shifted out of place in the small fist that should have smashed into his chest and burst his heart.

The Beast Miao King seized her fist in his enormous palm and bared his bloodstained teeth.

“I told you. I’d tear off all four of your limbs and kill you.”

“……!”

At the cold voice boring into her ear, the blood vessels in the Southern Heaven Demon Empress’s eyes burst as she stared wide-eyed.

She instinctively reached out with her other hand to seize the Beast Miao King by the throat. But then she saw the green Fist Force filling her vision and realized—

*Ah.*

Someone else had already taken one of her arms.

Boom!

The world turned upside down.

The Southern Heaven Demon Empress’s vision faded as she flew away like a cannonball.

In the slowed-down world, light and darkness flashed endlessly before her eyes. The sky and the earth traded places, twisting together.

And at the end of it all, an impact awaited her—one that seemed capable of grinding her entire body into powder.

Kraaaaaaang!

The ruins of the Inner Palace had been piled up like a small mountain. The Southern Heaven Demon Empress crashed deep into their center, piercing through the mound, and violently vomited blood.

“Kweh-heeeeeck!”

Splash!

It was dark. Red.

Dark-red blood mixed with pieces of internal organs sprayed across the countless large and small fragments scattered in every direction.

She felt her body trembling along with the horrible pain.

*This… This can’t be happening. This can’t be happening.*

At that moment, when a single thought denying reality filled her mind, something entered the Southern Heaven Demon Empress’s blurred field of vision.

Thud. Thud.

The ruins shifted little by little. From within them, someone’s figure staggered upright.

A faint light appeared in the Southern Heaven Demon Empress’s eyes, which had been shaking without pause.

Hope.

That was what it was.

“M-Me. Hurry, take me…”

With a voice that seemed ready to go out at any moment, the Southern Heaven Demon Empress extended her trembling hand.

Toward the figure slowly rising on two legs twisted at unnatural angles.

Toward her loyal subordinate, whose neck hung limply, already torn open by something, and who was awaiting a recovery that surpassed even supernatural powers.

“Hurry. Hurry and take me as far away from here as possible…”

At this moment, the Southern Heaven Demon Empress was more desperate than anyone else in the world.

The grand plan she had prepared had achieved only half of its intended success, and death—something she had never once considered—now loomed before her eyes.

She had to escape this place somehow.

She wanted to survive, even if that was all she could do. If she survived, she could plan for the future.

She could return again and continue her grand plan and her revenge somewhere else.

But the Southern Heaven Demon Empress’s final hope faded the next moment, along with the shadow that fell over the masked man’s head.

Whoosh. Crack!

The thing casting that shadow was not the Beast Miao King, Jin Taekyung, or anyone else.

It was simply a massive boulder.

It had probably been dislodged by the force of the impact.

Somewhere in the ruins piled up like a mountain—perhaps even the foundation stone of the Nanman Beast Palace—a massive stone weighing a thousand geun crashed down over the Southern Heaven Demon Empress’s final hope.

The masked man, who had lost his reason long ago and now did nothing but obey his master’s commands, was crushed beneath the boulder. His limbs twitched.

And as the Southern Heaven Demon Empress stared blankly at the sight, the sound of footsteps like thunder reached her ears.

Thud. Thud.

A footfall approached over blood-soaked ground, treading on sand and rubble.

No—footfalls.

No strange cries or clashing weapons accompanied those unusually loud steps.

*Ah.*

The Southern Heaven Demon Empress raised her head and finally understood.

The fierce battle that had wagered the fate of this land—the fate of Nanman—was already over.

And along with it, the fate she had carried forward for so many years was also nearing its end.

At the head of the approaching group was the person who had created this entire situation.

Thud.

The blood-soaked forepaw of a wild beast stepped over the ruins as it came closer.

A massive White Tiger stopped only three jang away. On its back, a face she never wanted to see again—not even in a dream—stared down at her.

“Feels like it’s been a while since I last saw you… You’ve gotten a lot prettier.”

Whoosh! Thud!

The Finger Qi she fired on instinct grazed Jin Taekyung’s shoulder and pierced through some part of the ruins behind him.

He casually rubbed the blood flowing from the cut, then licked his palm, wet with blood.

“Thanks. I was thirsty anyway. Is this what they mean by a grandmother’s affection?”

“……!”

A surge of blood welled up and leaked through her clenched teeth.

As she forced every last bit of strength into her body and tried to rise, a dozen or so spears flew over Jin Taekyung’s head.

Whiiiiiiish—boom!

With a single wave of her hand, the Southern Heaven Demon Empress knocked away the assault spears fired by the Baekcheon Unit. The blood vessels in her eyes burst as she glared at Jin Taekyung.

“How dare you!”

Fwoooooosh!

Her voice, carrying internal energy, shook the surroundings.

The Southern Heaven Demon Empress had lost one arm and suffered massive Internal Injury, but the power granted by the demonic qi flowing from the rift remained.

But…

*It’s not enough.*

Even so, she could not overturn the current situation.

The Southern Heaven Demon Empress understood that better than anyone. She knew the desperate reality that had befallen her.

And when she saw the Beast Miao King standing beside Jin Taekyung, she became certain.

*I’m going to die.*

In a body reduced to this state, she could do nothing.

Even if she miraculously survived and escaped this place, thousands of Nanman warriors were waiting for her outside.

Certain death.

Those two words bound her entire body with an unimaginable weight. They erased every thought from her mind and emptied her confused heart.

Then, at the moment all of the Southern Heaven Demon Empress’s thoughts stopped, a low sound of splitting air broke the silence.

Whoosh!

The Beast Miao King, the guardian spirit, and Jin Taekyung.

As though they had agreed from the start, they became a single streak of wind and surged forward—as if to deny her even the briefest opening, let alone time for final words.

They had only one resolve: to cut off the breath of the Fiend known as the Southern Heaven Demon Empress.

Kraaaaaaaash!

Powerful green Fist Force pressed down on the air.

Bloodstained teeth tore through the wind.

A transparent spearhead carrying the last handful of internal energy held blue-white hellfire within it.

And every one of those sights was reflected in a single person’s eyes.

At the same time, a faint light entered the empty gaze of the old woman watching death approach from every direction, second by second, after losing the beauty she had once possessed above all others.

*Lord of Heaven.*

The most noble and dignified being in the world.

In the distant past, the Southern Heaven Demon Empress had felt love from the moment she first saw the Lord of Heaven, and she had prostrated herself at his feet and sworn her loyalty.

She had vowed to offer that insignificant life for him.

Even if her youth and beauty faded someday, she had promised to remain by his side forever, even if only from a distance.

She had not known then.

She had not known that the day she would offer her life would come so soon.

She had not known that a day would come when she could no longer remain at the side of the Lord of Heaven she revered above all else.

But…

*Please remember me. Remember that this lowly woman once stood at your side.*

If the Lord of Heaven remembered her—if he remembered her as a servant who had loved him more than anyone else—that would be enough.

If only that could happen…

She could gladly burn through the life she had left with a smile.

Just as she was doing at this very moment.

Crack.

In the slowed-down world, the Southern Heaven Demon Empress heard the sound of the *rift*—a sound only she could perceive.

Innate qi.

The purest and most powerful force she had carried since birth awakened.

A vast, unprecedented energy surged through her entire body and gathered in her hand.

Gooooooooong.

Space twisted, as though invisible hands were tearing it apart.

Looking at the astonished faces of the three beings before her, the Southern Heaven Demon Empress smiled.

No—she tried to smile.

Thud!

Until a sword thrust out from the heap of ruins behind her and buried itself in her back, emerging from the deep, dark gap between the fallen stones.
## Chapter artifact 708

# Chapter 708

Thwack!

Along with the clear sound of flesh being pierced that bored into her ears, the world surrounding the Southern Heaven Demon Empress came to a halt.

The only thing she could vividly feel was the cold blade driven deep into her back.

Why? Who? How?

Countless questions filled her mind amid the distant agony.

At the same time, instinct moved her body before reason could. The Southern Heaven Demon Empress spun around at lightning speed and thrust out a palm.

Whoosh!

Innate qi. The moment some of the unprecedented internal energy held in her hand struck the collapsed ruins—

Kraaaaaaash!

With a tremendous roar, tons upon tons of rubble exploded outward.

And hidden among those countless fragments was the answer to the questions the Southern Heaven Demon Empress had just asked herself.

“Kugh!”

A figure was helplessly flung away in the aftermath of the explosion.

One sleeve of the white robe, stained with blood and dust, hung empty. Blood gushed from the wound in his chest, an injury beyond recovery.

But his cold, steady gaze remained fixed on the Southern Heaven Demon Empress until the very end.

His eyes, filled with an immeasurable mixture of rage and regret, seemed to whisper to her.

*I’ve been waiting for this moment for a very long time.*

“Baeksang…!”

A single name burst from her lips like a scream.

At the same time, the Southern Heaven Demon Empress’s eyes widened as she felt the wind sweeping toward her from behind.

Shwaaaaaak!

The time lost to the unexpected attack had been no more than an instant.

But that brief moment—the span of a single blink—had benefited someone else and become poison to the Southern Heaven Demon Empress.

Crack.

Swallowing the sticky blood in her mouth, the Southern Heaven Demon Empress spun around while pulling the sword embedded in her back free at lightning speed.

Three beings swept toward her like a sudden gale.

The Beast Miao King, the guardian spirit, and Jin Taekyung.

The moment she saw them, the qi and blood within her, already thrown into turmoil by Baeksang’s attack, convulsed.

She could feel the flame of mutual destruction, kindled by burning her own life as fuel, flickering like a candle in the wind.

Pain surged through her again, and her vision blurred.

But she could not stop. She must not stop.

*Kill.*

With that single thought, the Southern Heaven Demon Empress gritted her teeth and reached out.

Toward the three figures already rushing into view.

Toward the enemies who dared stand in the way of the grand undertaking the most noble Lord of Heaven wished to accomplish.

Gooooooooong.

In the slowed-down world, an unprecedented energy flowed through her bloodstained hand and into the blade.

The sword, whose master had changed, slashed down diagonally.

Shwaaaaaak!

And the Southern Heaven Demon Empress saw it.

Three pairs of eyes slowly widening beyond the warped space.

And the green Force surging up like an iron wall, as though to protect them all.

But…

*It’s over.*

Along with the Southern Heaven Demon Empress’s inaudible mutter, a distant flash of light swallowed everything.

Fwoooooosh!

* * *

It was a massive explosion, unlike anything anyone in this land had ever seen.

Fwoom! Ruuuuumble!

Yohi and Muyaho, who had been evacuating the survivors along with countless wild beasts.

The thousands of warriors who had surrounded the darkened Inner Palace with blood-soaked weapons held upright.

And the tribespeople running toward the hills outside the Outer Palace, gasping for breath.

They all saw it, and one word came to mind.

*A cataclysm.*

There was no other way to describe it. The distant flash and violent tremors spread far beyond the Inner Palace, traveling endlessly into the distance, and everyone who felt that power froze in place.

No—they trembled beneath a fear that seemed to bind even their souls.

“A-Aah…!”

The groans rising from every direction all turned toward one place: the Nanman Beast Palace they had left behind.

Boom. Rumble.

It was collapsing.

The pavilions and homes their ancestors had spent long years building with blood and sweat—the place where they had been born and raised—were on the verge of collapsing before their eyes.

What more needed to be said?

Thousands upon thousands of vacant eyes turned toward the Nanman Beast Palace.

They wanted to take in one last sight of their beloved homeland—a place they could never return to now.

But the deep despair hanging before their eyes soon changed into hope.

Ruuuuumble…

The tremors gradually subsided. The ground, which had been collapsing as though it would swallow the Nanman Beast Palace whole, stopped moving, and the houses and pavilions that had swayed as though they might topple at any moment were left merely leaning.

An unimaginable disaster.

And then, a miracle.

Those who watched the unbelievable scene were overcome with relief and joy.

Meanwhile, someone who had caused a disaster despite possessing nothing more than a human body trembled with pain and rage.

“T-This is impossible… Kweh-heeeeeck!”

Drip. Drip.

Dark-red blood spilled down from the corner of her mouth.

In the empty space where everything within a radius of fifty jang had been shattered and hurled far away, the Southern Heaven Demon Empress looked around with eyes filled with a crimson glare.

It had been a single strike. One certain opportunity.

She would not have cared even if she had died.

She could no longer return alive, and even if she went on living, she would have to spend the rest of her days in this old, hideous form.

And yet…

She had survived.

She, who should have been blown apart and killed after swallowing everything in the explosion, had survived in this humiliating state.

“Baeksang! You bastard. How dare you!”

Rumble!

The qi wave that erupted along with her terrible roar of rage shook the surrounding space.

Baeksang’s unexpected attack.

That single sword, which he had probably thrust forward by squeezing out every last bit of his remaining strength, had twisted everything.

In that instant, the tangled qi and blood had prevented the Southern Heaven Demon Empress from putting all her innate qi into the strike. That was why she had avoided being killed in the explosion.

But the same was true of *them*.

“Cough.”

Thud.

Several dozen jang away, a graying giant dropped to one knee, vomiting blood mixed with pieces of his internal organs.

Countless fragments were embedded throughout his body. Behind his broad back, the Southern Heaven Demon Empress saw the massive White Tiger and a young man lying motionless, drenched in blood.

“Yayul Cheok, you bastard…!”

As blood-filled phlegm boiled in her throat, the image of the Beast Miao King she had seen at the final moment flashed before her eyes.

At the last moment, he had stepped in front of Jin Taekyung without a moment’s hesitation.

*Why?*

She could not understand.

Why had the Beast Miao King, Yayul Cheok, who had earned the great title of one of the Ten Kings in the distant Central Plains, made such a choice?

And that foul-smelling beast had done the same.

*Risk their only lives? For a mere brat?*

Along with her question, one certainty seized the Southern Heaven Demon Empress.

*Jin Taekyung. No matter what it takes, I have to kill that one.*

The Palace Lord of the Nanman Beast Palace, a man no different from a king of a nation, and the White Tiger possessing a divine artifact had risked their lives for him.

That meant he was the most dangerous possibility in this place.

And the Southern Heaven Demon Empress still had innate qi that she had not yet poured out.

The last strength she had gained by burning her life.

*Lord of Heaven. Please forgive this disloyal servant who dares attempt to defy your will.*

Step.

The Southern Heaven Demon Empress muttered the words quietly in her mind and took a heavy step forward.

At that moment, a sharp sound of splitting air rang out.

Shk! Crack!

A spear that had flown from somewhere trembled in the Southern Heaven Demon Empress’s grasp.

She crushed the steel spearhead with her bare hand and let her eyes glow with blood-colored light.

“Do you all want to die?”

A middle-aged man stood upright where her chilling voice was directed. He wore armor that had been torn almost to shreds.

No, he was not alone.

Drip. Thud.

In the already devastated space, more than a hundred warriors staggered to their feet and gathered behind the middle-aged man, gripping their swords and spears tightly.

Though they had been relatively far from the center, every one of them had suffered injuries both large and small. Still, they stood in the Southern Heaven Demon Empress’s way to fulfill the mission entrusted to them.

Splash.

The middle-aged man picked up something half-submerged in a pool of blood and tied it tightly around his forehead.

Three characters were written on the old silk, still impossible to hide beneath the blood.

**Baekcheon Unit.**

That was the middle-aged man’s answer to the question asked moments earlier.

It was the answer of Wang Ho, Commander of the Baekcheon Unit—and the will of every surviving member of the unit.

And then, the next moment—

Screeeeeech! Boom!

The Fiend known as the Southern Heaven Demon Empress charged toward them.

* * *

A flash of light.

And an explosion.

That was the last memory remaining in my mind, and when I opened my eyes again, I thought everything would be over.

I would either be alive.

Or dead.

The result of a battle was always one of those two things.

But when I suddenly opened my eyes after passing through a brief darkness, I realized that I had only been half right.

I had survived, but the battle was not over yet.

Kraaaaaack!

“Gaaaaah!”

“Stop it—!”

Slice!

“Noooo!”

As the senses that had briefly faded returned, I could see.

Blood spraying into the sky and limbs flying upward.

Someone’s body, crushed into a bloody mess beneath overwhelming power, being flung away.

Whoom! Boom!

Drip.

Blood that had burst only a few steps away splashed across my face.

As I stared blankly at the warrior whose life had ended with a hole blown through the center of his chest, a weak voice reached my ears.

No—it was someone’s mental voice.

—Human.

Only then did I realize what was supporting my back.

And whose warmth I could feel.

Then, as I turned my head after sensing the thick scent of blood seeping deep into my nose, I lost the ability to speak.

“……!”

A massive body trembled intermittently in a deep pool of blood.

Its silver fur, which had seemed almost mystical, was soaked through with blood. Its pale blue eyes struggled to blink in my direction.

—You’ve slept a long time.

“……What is this?”

—I have no regrets. Neither does he.

Suddenly, a memory came back to me.

At the moment that distant flash had filled my vision, there had been green Force and a silver mane blocking my eyes.

*No way.*

As always, my ominous prediction turned out to be right.

The moment I turned my head, I saw a large back.

The man kneeling on one knee, looking no different from a bloody corpse, was the Beast Miao King, Yayul Cheok.

He had already lost consciousness.

The fragments of sword blades embedded all over his body must have come from shielding someone else from the attack.

“This is insane. Why the hell…?”

—Go.

“What?”

—Leave. Hurry. There’s no time.

As I stood speechless, the guardian spirit weakly moved its head and spat something out.

Fwoooooosh.

The sacred stone, now no larger than a child’s fist, emitted a faint light.

Realizing what the guardian spirit meant, I gritted my teeth.

“Don’t give me that bullshit.”

—If even those people fall, you’re next. But if you run, you can live.

Kraaaaaack!

“Gaaaaaaaah!”

As the earth shook, another person’s scream followed.

The Southern Heaven Demon Empress entered my field of vision, her veins standing out across her entire body as she burned through the last of her life and tore apart more than a hundred members of the Baekcheon Unit.

“……!”

A chill swept over me before that overwhelming power.

As I froze in place, the guardian spirit whispered with all its strength.

—Go. Now!

I knew.

At least, I knew that the guardian spirit was right.

The Southern Heaven Demon Empress did not have much time left, and if I escaped alone, I would be able to survive.

But…

“I’d regret it for the rest of my life.”

I muttered dazedly and grabbed the sacred stone.

Then I rose and ran.

Not toward the Outer Palace.

Toward the Southern Heaven Demon Empress.
## Chapter artifact 709

# Chapter 709

Screeeeeech!

Jin Taekyung’s figure, shooting forward at breakneck speed, wavered slightly.

His limbs, which were usually as light as down, hung limp and cried out in pain, while his toes felt incomparably heavier than before each time they touched the ground.

The aftermath of that devastating One Annihilation.

If not for the Beast Miao King’s help, there was no doubt Jin would have been unable even to stand properly by now.

Even if he had endured through sheer desperation, the destructive power unleashed by the Southern Heaven Demon Empress would certainly have taken his life.

And yet… he had survived.

To save Jin Taekyung, who had been in the worst condition of them all, the Beast Miao King and the guardian spirit had thrown themselves into danger, risking their lives. Carrying on their resolve, the Baekcheon Unit was still staking their lives at this very moment.

Toward the deep darkness.

Toward a Fiend they had no way of opposing.

Crack!

One strike.

The blood-soaked hand of the Fiend shattered bone and flesh before punching through a chest.

The life of someone whose name Jin did not know guttered out just like that, and someone else stepped forward to fill the empty space.

*Why?*

Jin Taekyung did not know them, and they did not know Jin Taekyung.

And yet every one of them was willingly throwing away their life.

They filled the empty places left by their comrades, who were dying one after another, and charged toward a death they did not have the strength to stop.

And the sight of the Baekcheon Unit overlapped with that of someone who had forced a smile in the darkness of a cave.

*Go on ahead, Taekyung.*

He had survived because he ran, and because he survived, he had regretted it countless times. If he could return to that moment, Jin Taekyung would have said this.

“I’m not going. Never.”

At the voice that slipped through his clenched teeth, Wang Ho, Commander of the Baekcheon Unit, turned his head.

Soaked in blood whose owner could not be identified, he widened his eyes when he spotted the rapidly approaching figure.

Jin Taekyung should not have remained here.

This was precious time that his lord, the Beast Miao King, and the hundred warriors of the Baekcheon Unit—including Wang Ho himself—had staked their lives to secure.

His only mission must have been to survive by any means necessary.

And yet he had come looking for danger of his own accord.

“What the hell is going on…!”

Just as Wang Ho cried out in alarm and moved to block Jin Taekyung, who had rushed right up to him, a nail-pierced hand came down on his shoulder.

At the same time, a low voice pierced his ear.

“Let’s live through this together.”

“……!”

“Fucking hell. I said let’s survive together!”

Wang Ho’s body abruptly went rigid.

He did not know what to say.

Jin Taekyung was not calling for them to die together. He was crying out that they should survive together, his eyes burning like fire even as they glistened with tears.

Wang Ho could not stop that young man from leaving him behind and running toward death.

And then he understood.

Why the Beast Miao King—his lord, who had to lead nearly one hundred thousand tribespeople—had made that choice.

*Was this why? Was it because of this very sight that you wanted to protect that young man more than your own safety?*

If Jin had returned so they could die together, it would have been nothing more than foolhardy courage.

But Jin Taekyung had returned so they could fight together. To save as many people as possible, even if it was only one more, and for everyone to survive.

Tsstsst!

The Sword Energy that had seemed ready to go out regained its strength. Wang Ho straightened the blade enveloped in blue qi and charged forward.

Then he shouted to his subordinates, fewer than half of whom now remained.

“Kill that Fiend!”

It was a tiny yet enormous difference in mindset.

Would they hold her back?

Or would they kill her?

Until now, the Southern Heaven Demon Empress had been an existence they could not kill with their combined strength. No—all of them had mistaken that for the truth and accepted their deaths.

But now it was different.

From this moment on, this was a fight to kill the Southern Heaven Demon Empress.

A fight for their own survival.

At its center stood one young man who had made them realize all of this.

“Southern Heaven Demon Empress!”

Along with his roar, full of rage, a faint flame sprang up from Jin Taekyung’s toes.

Boom!

With a small explosion, the sunken ground split apart like a spiderweb.

Propelled by the recoil, his figure shot forward even faster.

At its end waited a Fiend stained with blood and darkness.

Slice! Shraaaaaak!

A body was cleaved in two by a hand blade wreathed in murky darkness.

Beyond the blood spraying in every direction, the Southern Heaven Demon Empress saw Jin Taekyung tearing through space as he charged toward her—and smiled delightedly.

*You foolish child. Your recklessness has become my final chance.*

Until a moment ago, she had been furious.

Her innate qi, which had been fueled by her life, was being consumed with every passing moment. The hundred warriors of the Baekcheon Unit who had blocked her path without regard for their own lives continued to die, gnawing away at what little strength she had left.

But now she could smile.

Her most important prey had come searching for the place where he would die, foolishly walking there on his own two feet.

“Now, all you small fry… get the hell out of my way.”

Roooooar!

Murky palm Force swept over the warriors blocking her path.

Their figures were flung in every direction, spitting blood.

And then, beyond the space that had emptied in an instant, a sound split the air.

Screeeeeech! Boom!

The Southern Heaven Demon Empress knocked away an iron spear that shot toward her like a flash of light with her bare hand, then swung down with her hand blade.

Whoooosh!

Space split apart, and blade-like wind whipped through it.

But Jin Taekyung’s figure was nowhere to be seen.

*Above!*

The moment she realized it, the Southern Heaven Demon Empress’s figure blurred.

A transparent spearhead slashed down from the sky too late to catch her, cutting through her afterimage.

Slice!

No. The spearhead had cut through more than just an afterimage.

The Southern Heaven Demon Empress felt a drop of blood roll down her forehead.

Her expression hardened slightly.

*Fast.*

In a way, it was only natural.

A martial artist who had reached the Supreme Peak could already be called superhuman without exaggeration.

But the reason they could be called superhuman was not merely their enlightenment in martial arts. It was also their overwhelming internal energy.

Internal energy that could further maximize physical abilities honed through years of training.

*Then how…?*

Jin Taekyung had clearly spent most of his internal energy. How could he still produce such fast, powerful attacks?

Shk-shk-shk-shk!

The spear tip trembled.

Dozens of spear shadows multiplied and poured toward every part of the Southern Heaven Demon Empress’s body.

Their speed and power far exceeded anything she had expected.

But the Southern Heaven Demon Empress did not retreat.

“How dare you, you little brat…!”

Along with her voice, which seemed to boil with rage, her only hand split the air and shot forward.

The palm strike, steeped in the blood of countless warriors, swallowed the spear shadows rushing toward her face.

Roooooar!

No matter how many falsehoods there were, in the end, only one truth would emerge.

The dozens of spear shadows vanished as they were swept away by the palm Force.

The Southern Heaven Demon Empress’s hand, shrouded in murky darkness, seized the transparent spearhead.

Slice!

Ten-Thousand-Year Cold Iron—the metal said to be harder and sharper than anything beneath heaven—tore through the Force and cut into her flesh.

At the same time, pain surged through her.

But the Southern Heaven Demon Empress smiled instead.

*I’ve got it.*

At that moment—

Shwaaaaaaak!

Her qi flowed along the spearhead and swept through Jin Taekyung’s insides.

Boom!

“……!”

His body jolted.

The internal injuries that had briefly settled with the Beast Miao King’s help were shaken once again.

But Jin Taekyung swallowed the blood surging up his throat and tightened his grip on the spear shaft.

Crack!

The White Flame spearhead caught in the Southern Heaven Demon Empress’s hand rotated and drove farther forward.

Her grip was shredded in an instant, and pain rushed through her.

The Southern Heaven Demon Empress’s eyes widened.

“You…”

But before she could finish, a sharp sound of splitting air rang out.

Shiiiiing!

A sword came flying through the wind.

The owner of the sword, wrapped in blue Sword Energy, was none other than Wang Ho, Commander of the Baekcheon Unit.

Slice!

The Southern Heaven Demon Empress twisted her body in haste, but it was already too late.

Her Body-Protecting Qi had weakened beyond comparison to before and could not stop the Sword Energy.

Feeling the pain radiating from her slashed flank, the Southern Heaven Demon Empress kicked upward.

Screeeeeech—crack!

Her foot, swung like a whip, drove into Wang Ho’s abdomen.

His figure shot away like a cannonball and flew more than ten jang.

Boom!

A cloud of dust rose with the force of the impact.

But Wang Ho was not the only one who had charged toward the Southern Heaven Demon Empress.

Pat-pat-pat!

Figures rushed in from every direction—front, back, left, and right—taking positions around the Southern Heaven Demon Empress.

The fewer than twenty remaining warriors of the Baekcheon Unit charged forward, squeezing out the last of their strength.

To end this fight.

To drive their spears and blades into that Fiend’s body, even if it cost them their lives.

Shk-shk-shk-shk!

At that moment, when the fierce sounds of weapons tearing through the air mingled with the wind—

Kraaaaaash!

Energy like a storm exploded outward, sweeping away everything flying in from every direction.

And from between the lips of the person standing tall at its center, blood that could no longer be held back began to flow.

Cough.

Through her fading vision, the Southern Heaven Demon Empress looked at the young man kneeling before her with trembling eyes.

His eyes were dim, as though they might go out at any moment.

But his hands, thrust forward while gripping the spear shaft tightly, did not tremble.

At their end was a transparent spearhead driven into the vicinity of the Southern Heaven Demon Empress’s chest.

“Guh…!”

The Southern Heaven Demon Empress vomited dark-red blood and gasped for breath.

She should have blocked it.

She thought she could block it.

But she had failed.

*How? How was he still able to move?*

Just before unleashing her palm Force toward the warriors, the Southern Heaven Demon Empress had clearly sent her internal energy into Jin Taekyung once more.

This time, she had made certain that his breath would stop, so he could never rise again.

But Jin Taekyung had neither fallen nor died.

Even though his heart meridian had undoubtedly been torn to shreds, he had driven the spear he had held until the very end into the Southern Heaven Demon Empress’s chest.

“Jin Tae…kyung.”

At the moment her broken voice slipped through her lips—

Slide. Thud.

Jin Taekyung’s blood-soaked hands slipped from the spear shaft.

His head tipped backward helplessly, and his eyes grew hazy.

At the same time, the Southern Heaven Demon Empress felt it.

She could hear it, too.

Death was approaching Jin Taekyung slowly but surely.

And she heard his voice, bright beyond belief for someone standing before death.

“I finally caught you, you goddamn bitch.”

“……!”

At that moment, a sensation like every hair on the Southern Heaven Demon Empress’s body standing on end seized her.

It was fear.

Terror of a human being who possessed an unwavering resolve that would not falter under any circumstances.

*…Afraid? I’m afraid? Me? Of that bastard?*

It was impossible.

It was impossible that she could fear anyone who was not the Lord of Heaven.

And it was impossible that the object of that fear could be a mere brat standing on the brink of death.

*I have to kill him. With this hand, I have to cut off his breath myself.*

Muttering the words in a daze, the Southern Heaven Demon Empress slowly raised her hand.

She would probably be unable to escape death either.

But if she did not cut off Jin Taekyung’s breath, she felt that she would never be able to close her eyes in peace, even after death.

*Die.*

*You monster.*

With that one word she did not have the chance to spit out, the Southern Heaven Demon Empress swung down her hand blade with the last of her strength.

Shk!

And at the moment the murky darkness was about to bore into the crown of Jin Taekyung’s head—

Screeeeeech! Crack!

A streak of light flew in from somewhere and swallowed the Southern Heaven Demon Empress’s only arm.

At the same time, a cold voice pierced her frozen ear.

“Just whose body do you think you’re laying a hand on, you fucking bitch?”

# Checkpoint Review — 1050–1054

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

# Chapters 1050–1054

## Plot

The Grand Mage reveals that the Lord of Heaven has watched Jin Taekyung and wants him to survive and grow stronger, though she does not know why. When she binds and chokes him, Jin severs his own heart meridians rather than submit. The Grand Mage desperately heals him; the System removes his injuries, and Jin breaks free and attacks. The Bow Saint’s Force arrow strikes the Grand Mage, who appears dead, but Jin finds signs that she escaped by Teleport.

Jin refuses the Blood-Sword Demon Lord’s offer of information and kills him. He suspects Sima Gong, Song Il, and Hwangbo Eom of treachery but, having seen their final acts against the Demon Lord, resolves to remember their honor without forgiving them. Jin returns to the ongoing battle with Jeok Cheongang and the Bow Saint as thousands of reinforcements arrive.

The Grand Mage reports to the Lord of Heaven that her plans went awry: the Kongtong Sect Leader and some survivors vanished, former allies turned against the Demon Lord, and Jin and his companions endangered her. The Lord reads her thoughts, rebukes her doubts, then reassures her and grants her new power. He sends her to Qinghai to join another servant on a new mission, saying the great plan is nearing completion. As she departs, he remarks that time is passing, and a mysterious green light glimmers in the darkness.

## Continuity

- The Grand Mage survived the Bow Saint’s attack, recovered her severed limbs, received new power from the Lord of Heaven, and departed for Qinghai on a new mission.
- The Lord of Heaven says the great plan is nearing completion; a mysterious green light remains unexplained.
- The Kongtong Sect Leader and some survivors who knew the truth vanished to an unknown location.
- The Grand Mage identifies Jin as the Chosen One and suspects his emergence as the Hidden Dragon is connected to the Lord of Heaven’s growing power; this is conjecture.
- Jin suspects a connection between the Lord of Heaven and the dead Demon King, Asmodeus; the truth is unknown.
- The battle at the Great Snow Mountain was still underway when thousands of reinforcements arrived.

## Translation Decisions

- Render 대마도사 and 대술사 as Grand Mage.
- Use Fire Ball, Stone Wall, and Magic Arrow for the named spells.
- Render 헬 파이어 as Hell Fire; use hellfire for descriptive 겁화.
- Render 쇄월검진 as Moon-Shattering Sword Formation.
- Render 배 째 as “Go Ahead, Gut Me!”
- Keep Teleport distinct from the short-range Blink spell.
- Render 詩聖 as “Poet Sage,” retain Kongtong, and continue rendering 天主 as Lord of Heaven and 青海 as Qinghai.
- Render 天上天下，萬魔仰伏 as “Heaven above and earth below, all demons bow in reverence.”

## Durable state

{
  "active_continuity": [
    "The Grand Mage survived her mortal wounds, recovered her severed limbs, received new power from the Lord of Heaven, and departed for Qinghai on a new mission.",
    "The Lord of Heaven says the great plan is nearing completion; a mysterious green light remains in the dispersing darkness.",
    "The Kongtong Sect Leader and some survivors vanished to an unknown location.",
    "Jin suspects a connection between the Lord of Heaven and the dead Demon King, Asmodeus; the truth is unknown."
  ],
  "continuity_sources": [
    1053,
    1054
  ],
  "open_questions": [
    "What are the identity and purpose of the Lord of Heaven?",
    "Why does the Lord of Heaven want Jin to survive and grow stronger, and is he connected to Asmodeus?",
    "Where did the missing Kongtong Sect survivors go?",
    "What is the new mission in Qinghai, and who is the other servant there?",
    "What is the mysterious green light?"
  ],
  "safe_through": 1054,
  "temporary_decisions": [
    "Render 대마도사 and 대술사 as Grand Mage.",
    "Use Fire Ball, Stone Wall, and Magic Arrow for the named spells.",
    "Render 헬 파이어 as Hell Fire; use hellfire for descriptive 겁화.",
    "Render 쇄월검진 as Moon-Shattering Sword Formation.",
    "Render 배 째 as “Go Ahead, Gut Me!”"
  ],
  "version": 1
}

## Reading copies

## Chapter artifact 1050

# Chapter 1050

When people faced a truth that went far beyond anything they’d expected, their reactions tended to fall into one of two camps.

They either fell into confusion, unable to understand it, or froze as they grasped the immense shock and weight it carried.

The Blood-Sword Demon Lord belonged to the first.

“What does that…?”

He muttered blankly, having forgotten even his pain.

Confronted with the despairing reality that the master he’d worshiped like a god had abandoned him, the fiend could hear the Grand Mage’s words from a moment ago ringing in his ears again and again.

*You can’t fall here. You have to get stronger than you are now.*

No matter how many times the Blood-Sword Demon Lord turned over the Grand Mage’s words about Jin Taekyung in his mind, he couldn’t understand them.

Used up and thrown away?

He couldn’t help feeling betrayed.

But if the strong wanted blood, the weak had to bleed.

That was a law of the world he knew well, having walked the Demonic Path all his life.

He still didn’t know why he, who had devoted himself to the Lord of Heaven and Dark Heaven, was being discarded. But now that things had come this far, he had no choice but to accept it.

And yet, quite apart from that…

Why? How? For what reason?

Why would the master he served entrust the execution of his loyal hunting dog to an enemy, even at such a great cost?

And not just any enemy, but a brat who wasn’t even thirty years old—someone who had thwarted Dark Heaven at every turn more than anyone else in the world.

And…

*Kill me, and get stronger?*

What on earth did his death—this one-sided execution—have to do with Jin Taekyung getting stronger?

The Blood-Sword Demon Lord couldn’t begin to guess what the Grand Mage’s final words meant. That was only natural.

There were limits to what he could imagine.

But at least one other person here knew the truth the Blood-Sword Demon Lord couldn’t.

“…You.”

The young man’s lips had gone white, and the muscles in his face had stiffened.

He stared at the woman before him with vacant eyes, having even forgotten to breathe. At last, he managed to squeeze out a voice.

“What are you even… talking about?”

This wasn’t a question. It was a denial.

He couldn’t bear to believe in a reality that couldn’t possibly come true, so he was desperately trying to deny it.

The Grand Mage looked at the young man—Jin Taekyung—and her eyes curved into crescents.

“You already know, don’t you?”

“…!”

“Do I have to spell out what I mean, right here?”

The words that turned his ominous suspicion into certainty reached his ears. Jin Taekyung felt his mind turning white.

Only one phrase remained in his empty head.

*Level Up.*

* * *

Was this what it felt like when all the blood in your body turned cold?

For that moment, it was as if the whole world had stopped.

No—maybe I really had mistaken it for that.

If not for my head, which had grown hot as if someone were searing it with a branding iron, while my body remained frozen.

*This… can’t be real.*

I floundered in a storm of confusion.

Question marks appeared and disappeared, over and over, while reason and emotion lost their bearings and crashed into each other.

The shock rocking my mind was like—or perhaps greater than—the shock I’d felt when I realized this strange world called Murim wasn’t a game, but another reality.

And yet this was undeniably real.

I forced down my undying shock with everything I had and squeezed out a voice.

“How? How is this possible?”

A hoarse, cracked voice, so unfamiliar it might have belonged to someone else, slipped between my lips.

Unlike me, the woman’s answer came back calm and composed.

“Who knows? I’m too insignificant to know everything. But…”

The Grand Sorceress—or the Grand Mage.

She had gained power that didn’t belong to this world. Now she stared straight at me. Her eyes and voice were filled with such steadfast faith that it could only be called fanaticism, and they set my senses reeling.

“The Lord of Heaven is great. I am merely a servant who conveys His will and His words.”

“The Lord of Heaven. The Lord of Heaven…”

Like a man under a spell, I muttered the damn name.

Ever since the day I’d taken my first steps in Murim, I’d heard it from countless people. And yet I’d never once encountered its true form.

The leader of Dark Heaven—or rather, their king and god, the absolute being who sought to defy heaven.

It was Him.

Only Him.

He knew one of my most closely guarded secrets as clearly as if he were looking at the palm of his hand.

But that still didn’t answer the question I’d asked before.

Because I—Jin Taekyung of the Jin Family of Taiyuan—had become someone else overnight.

“Were you watching me? From the beginning?”

“Watching you?”

Beneath the white veil covering her face, her red lips curved gently.

“To be honest, everyone knows that just a few years ago, you weren’t even worth worrying about.”

“Then that means…”

“It’s simple. We were looking down upon the world, and you shone on your own within it. Bright enough to see clearly, even from far away.”

“……!”

“It was fascinating. Watching the spoiled son of a declining frontier family become a Hidden Dragon, then gain the Fire King as his dragon pearl and become a Divine Dragon. And watching you grow at a pace without precedent.”

An imugi that had cultivated itself for hundreds of years could become a dragon if it obtained a dragon pearl. But Jin Taekyung of the Jin Family of Taiyuan had been, at best, an earthworm wriggling in muddy water.

And yet the System had given me boundless opportunities to grow. People had come up with reason after reason for my progress, without me having to offer a single excuse.

Heaven-given martial talent.

The Heavenly Martial Physique, a body as perfect as could be.

And the teachings of the great martial artist Jeok Cheongang, the Fire King.

They said all of that had brought me to my current level of strength.

So no one had suspected a thing.

No—they couldn’t have suspected.

Even in this world, with its primitive savagery, there were limits to what people considered possible.

But the Grand Mage was telling me now that someone outside their reach—at least, the Lord of Heaven—had been the exception.

And she’d revealed another unexpected truth, too.

“We continued to watch under His command, and at last we learned who the Chosen One was.”

My eyes trembled before I could stop them.

“What… did you just say?”

“Why? You don’t like the expression? I thought it was rather good.”

I didn’t answer the Grand Mage’s question.

I simply shut my mouth and repeated the words I’d just heard to myself.

*The Chosen One?*

There was only one reason I’d repeated her question without thinking.

This wasn’t the first time someone had called me that.

The first to call me the Chosen One was, even now, far off in the distance with his bowstring taut, aimed in this direction.

*The Bow Saint.*

A hero of the Great Faction War, who had protected the Nine Provinces from the hundred thousand members of the Demonic Cult.

A great martial artist who had always shone brilliantly, wherever he went, and was therefore called one of the Three Saints.

And the reason the Bow Saint had spent decades wandering the land, concealing his identity, was a letter left behind by one person.

*…The Martial God.*

Ten Kings. Three Saints.

Above them all, a heaven looking down on everything—the universe, or perhaps Murim itself.

The greatest hero and martial artist of all time, with no equal before or since.

The Martial God had left a letter for the Bow Saint.

He’d told him to find someone who might appear at any time, in any place.

The Chosen One—that is…

Me.

That only made it harder to understand.

I could accept that the Martial God had foreseen my appearance and left the Bow Saint a letter about me.

But why? How?

“Why would you—or the Lord of Heaven—keep me alive?”

I was the one who’d stood in Dark Heaven’s way more than anyone else.

I’d been directly involved in the deaths of four Demon Lords and the Demon Empress, his closest subordinates and limbs. I’d caused him countless other losses, too.

From the Lord of Heaven’s perspective, I was someone he could kill a hundred times and still not be satisfied.

And yet the Grand Mage had said it plainly.

Her master didn’t want me to die here.

He wanted me to survive, and grow stronger. Stronger than before.

I had to hear the answer to this question.

If the Lord of Heaven wanted me alive, then it meant my very existence would one day become a threat to everyone.

“Answer me. Now.”

The shock and trembling were long gone.

All that remained was the reality before me, and the coldness to face it.

I stared at the Grand Mage with icy eyes.

At the eyes glimmering dimly through the densely woven white veil, burning with loyalty to their master.

At last, her tightly closed red lips moved.

“No one in the world would dare presume to guess His deep intentions. But one thing is certain.”

She breathed out slowly.

The corner of her mouth lifted. The expression there was unmistakable scorn.

“Even if you heard the whole truth, could you resist? You?”

“……!”

“Let’s be honest with each other.”

As if she were throwing off some cumbersome garment, the Grand Mage cast aside her manners. Smiling, she continued.

“You think it rains because people pray for rain? It doesn’t. The clouds gather, and when the heavens will it, the rain falls. That’s the way of this world. Its natural order.”

Crack.

A sharp gleam flashed behind her veil. A thick vine crept up my body and tightened around my neck.

Slowly. And powerfully.

“If you want to die, I can kill you. But you have to survive, according to His will. You want to live, too. Don’t you?”

I couldn’t breathe.

My whole body was already bound. As the plant stem slowly tightened around my windpipe, I squeezed out my voice.

“Then… kill me.”

“What?”

“Go on. Kill me.”

“……!”

The Grand Mage’s gaze wavered.

She’d heard the sincerity in my breathless voice and seen it in my eyes, which were steady despite my labored breathing.

“You…”

Her words trailed off, and the pressure around my neck loosened. I looked at her and gave a short laugh.

“What? Can’t do it, you crazy bitch?”

Crack!

The vine tightened again, as hard as before.

Even so, I laughed aloud, gasping for breath.

Yeah, I was unquestionably the weaker one now.

But in this tug-of-war with our lives on the line, I was going to win.

If the Grand Mage was a crazy bitch, then I was a different kind of crazy bastard.

*Now that it’s come to this, I can do it.*

I smiled brightly at the Grand Mage, her eyes wide open.

Then I severed the heart meridians throughout my body with all my strength.

Using that faint power to heal me—the very power she had given me.

Crack!
## Chapter artifact 1051

# Chapter 1051

“You…”

The moment the Grand Mage saw a smile spread across Jin Taekyung’s face, which had been turning deathly pale, she instinctively realized how foolish a mistake she’d made.

*Shit.*

It was an irreparable blunder.

She’d loosened the binding spell without thinking, in response to the unmistakable sincerity of his *Go ahead and kill me if you can.*

And through that split-second mistake, Jin Taekyung had immediately seen the Grand Mage’s true intentions.

“What? Can’t do it, you crazy bitch?”

“……!”

The Grand Mage bit her lip. He’d hit the mark.

What he said was true.

A hunting dog could only cut its target’s throat when its master gave permission.

But she didn’t yet have that authority, and her earlier bluster about the laws of nature had already been exposed.

Of course, even so—

*Nothing changes. Nothing at all.*

The Grand Mage thought to herself, then poured her strength back into the Magic that had briefly faltered.

Crack!

As if nothing had happened, the thick, sturdy vines squeezed Jin Taekyung’s neck even tighter.

The overwhelming difference in power, now laid bare, was impossible to bridge.

Unlike him, with barely a trace of internal energy left, a tremendous force still lay coiled deep within the Grand Mage’s body.

And that wasn’t all.

Now that Jin Taekyung was her hostage, even the two giants—the Fire King and the Bow Saint—couldn’t dare act recklessly.

All she had left to do was make the young brat before her submit.

That was what the Grand Mage had been certain of.

Until she saw the smile on Jin Taekyung’s face, brighter than ever.

*…He’s smiling?*

She couldn’t understand what that smile meant.

No—more precisely, she instinctively guessed its meaning, but couldn’t accept it rationally.

There was only one variable Jin Taekyung could create in a situation where he’d been so completely subdued.

And there wasn’t a single lunatic in the world who’d choose a variable as insane as suicide.

But—

Crack!

There was one.

That lunatic.

Right here.

Before her very eyes.

*Splatter!*

In that instant, the Grand Mage’s eyes opened wide without her meaning to.

Everything was red.

And at the same time, she saw him.

Through the blood sliding stickily over her white veil, Jin Taekyung trembled all over and spat up blood.

“Th-This…”

The stunned gasp slipped between her red lips.

There was no doubt. He’d severed his own heart meridians.

Even a massive old tree, one that wouldn’t easily fall to a lumberjack’s axe, couldn’t withstand a colony of ants boring through its bark and into its core.

That was why, for a Murim martial artist, severing the heart meridians meant death.

A swift death, and an agonizing one.

*Why would he go this far?*

Frozen for an instant, the Grand Mage stared at Jin Taekyung in utter shock.

The truth she’d told him had been only half the truth.

A tiny truth, nowhere near enough to give him certainty—just enough to make him vaguely suspect something.

And yet, when he’d realized that his mere existence might threaten someone, how many people under heaven would give up their lives without hesitation?

None. Without question.

The strongest desire granted to a human being was the desire to live. Even if someone made this choice, it would take countless doubts and resolve to carry it out.

But Jin Taekyung had done it.

Without the slightest hesitation or fear.

Even smiling brightly as he did.

In his eyes, already dimming rapidly, lay absolute certainty. Not the slightest wavering.

The certainty that he’d chosen the right path.

And seeing Jin Taekyung like that, the Grand Mage finally realized what her most fatal mistake had been.

*The Chosen One.*

Having had her thoughts read earlier was nothing.

She should have understood what those five syllables meant. She should have guessed.

Why her great master had searched so desperately for the young man before her.

Why he’d ordered his loyal servants to watch his every move.

Jin Taekyung was that kind of person.

He could curse up a storm and still understand human decency. He could spit in someone’s face and still pursue the chivalrous path. He might walk along the edge of the road, but he’d never stray from the right one.

A chivalrous hero who led the way before everyone—and a lunatic beyond anyone’s imagination.

That was why he was the Chosen One.

Crack!

The Grand Mage clenched her teeth.

There was no more time to hesitate, no choice left to make.

Her master had already waited far too long. If Jin Taekyung died here today, he would have to wait once more, with no end in sight.

*I have to save him. Whatever it takes!*

As time seemed to slow, the Grand Mage reached out, more desperate and frantic than ever.

Swoooooosh!

An immense force surged up around her slender frame.

Not with the will to kill, but the will to save. The force surrounding her heart pulsed fiercely.

The power lying dormant in the air resonated with it, then burst into light, devouring everything around them.

*Fwoom!*

The swelling radiance swept over the hill.

No—it spread until it covered the entire hill.

Its dazzling brilliance bleached the eyes of the Bow Saint and Jeok Cheongang as they raced toward them, having realized something had happened to Jin Taekyung, who was being held hostage. It forced the eyes shut of the fiend, still writhing like an insect as he clung to life.

Even the Grand Mage herself, who had summoned that radiance.

*What happened?*

With her vision suddenly fading, the Grand Mage bit her lip.

When a pile of rocks collapses, it kicks up dust. But when Taishan crumbles, it causes an earthquake.

A Supreme Peak master who had severed his own heart meridians had suffered an injury that not even a Great Firmament Immortal could heal.

She’d unleashed the greatest healing power she could, but there was nothing she could guarantee. And the radiance that had erupted more fiercely than ever showed no sign of fading.

No—at that very moment, it seemed to flash even brighter.

Like a blade shining all the more beneath the sun.

“……!”

Just as the Grand Mage’s eyes widened when she realized something—

*Shwaaak!*

A chillingly low, razor-sharp whistle tore through the air. A silver-white spearhead, worthy of being called the White Flame, ripped through space.

And beyond the still-dazzling radiance came someone’s quiet voice.

“Got you.”

*Thud!*

* * *

My stomach’s churning.

My head’s spinning, and my vision is blurry.

Maybe that’s why.

Honestly, I still don’t know.

Is this moment a dream or reality?

If it’s neither…

*Hell? Or heaven?*

I couldn’t think of anything else.

Everything around me was so white I couldn’t even open my eyes properly.

Unless some enterprising Yama had gone and installed ridiculously powerful LED bulbs throughout hell to improve conditions for its prisoners, this had to be heaven.

But—

Ding. Ding. Diiiing!

The clear chimes ringing in my ears, like an echo returning from far away, were enough to tell me.

This was reality. I was alive.

And I’d won again in this insane gamble, where I’d staked my life.

> **System**
>
> Status Effect: Terrible Internal Injury has been removed!
>
> Status Effect: Severe Bleeding has been removed!
>
> Status Effect: Exhaustion has been removed!
>
> Status Effect: Ruptured Organs has been removed!
>
> Status Effect: Fracture has been removed…
>
> .
>
> .
>
> .
>
> A powerful healing force takes root in your body!
>
> You’ve earned the somehow-you-managed-it achievement: Go Ahead, Gut Me!

Translucent holographic windows floated one after another in midair.

Along with them, my blurry vision cleared as if it had never been blurred. My breathing steadied, and my senses sharpened, letting me feel and take in everything within a dozen or so *jang*.

Light. Air. Wind. Even things without physical form, like the thick stench of blood.

And the beings breathing among all of it, with the same vitality as me.

Now it was time to collect my winnings from the other side of the bet.

*Come.*

I whispered inwardly and sent out my will.

Toward the cold blade that held not a trace of life, yet had extinguished countless lives.

Toward my beloved weapon, which had left my grasp and lay alone on the ground, far away.

*Shwaaak!*

It all happened almost at once, and I murmured,

“Got you.”

At that moment—

*Thud!*

With the sound of bone and flesh bursting, the thick vines that had bound my entire body loosened.

*Now.*

I didn’t even need to pour in internal energy.

I simply put an immense force—one that the word *superhuman* couldn’t begin to describe—into my limbs and let it loose.

*Crack!*

The vines split, then burst apart.

Unable to withstand that hideous force, they snapped into pieces. At the same time, I broke free and reached out toward the White Flame, which was shooting my way like a streak of light.

Tap.

That cool sensation was more familiar than anything.

But the blood scattered across the silver-white spearhead was still warm, and the scream that burst out not far away was desperate.

“Aaaah!”

Could anything make a more perfect landmark than a sound on a battlefield where your vision was blocked like this?

Following the sharp scream ringing beyond the still-unfaded radiance, I took a long step forward.

*Bang!*

Compressed air exploded beneath my thrusting foot.

The radiance layered across my vision shattered, and the distance of three *jang* vanished in an instant.

And then…

*Shaaak!*

At the end of the spear’s slashing arc, there was someone who owed me my stake.

I couldn’t see her, but I could feel her clearly. In that instant—

*Fwoom!*

Dark red blood sprayed with a cold slicing sound.

But the person who’d screamed in pain only moments ago was no longer there.

*Fast.*

No—*fast* didn’t begin to describe the movement.

If any Murim martial artist had seen it, they’d have called it Shifting Form and Position, a technique only a Supreme Peak master could use.

But no matter what anyone else in this world thought, I was the one exception.

*Blink…!*

A Magic spell that made you disappear in an instant, like the literal blink of an eye—a short-range teleport.

In the hands of a Grand Mage, it was an incredible evasion ability, faster than Shifting Form and Position. But that was all.

*Three steps from my left. Five *jang*.*

I was the person who knew the limits of Blink better than anyone in the world.

*Crack.*

And I was a superhuman whose extraordinary strength and senses could catch up with Blink despite its limited range.

*Boom!*

One step.

In the space that vanished in an instant, I smiled brightly at the Grand Mage, frozen with her eyes wide open.

“See you again?”

*Shing!*
## Chapter artifact 1052

# Chapter 1052

“Fancy seeing you again.”

At the sound of his low voice, Jin Taekyung was suddenly right in front of her. The Grand Mage felt the blood in her body turn cold.

*How?*

His speed couldn’t be explained by simply calling him fast. It was far beyond anything she’d expected.

And as if he’d known exactly where she’d be, the silver spearhead came slashing down toward her body.

*Whoosh!*

The air split. No—it shattered.

As space warped around the Force coiling around the spearhead, the Grand Mage felt greater fear than ever before and cried out in her heart.

*O mighty power of protection!*

*Vwoom.*

In the slowed world, the energy gathered around her heart began to boil.

At the same time, layers of translucent shields rose up, surrounding her body and blocking the spearhead.

*Boom! Crash!*

The ground shook as if an earthquake had struck.

But in that moment, all the Grand Mage’s senses were focused on what lay before her eyes.

The spearhead had smashed through most of the dozens of layered shields, but at last it stopped—just barely.

*I blocked it.*

A shiver ran up her spine. Only then did the Grand Mage let out the breath she’d been holding.

Before she could fully feel the relief, she saw Jin Taekyung smiling faintly despite his sure-kill attack having failed. And suddenly, she realized something.

She’d forgotten something.

Or rather, some very important—and very dangerous—people.

But as with everyone, the realization came a moment too late on the battlefield.

*Whooosh!*

A vast flash of light flew across the space between them.

Beyond the dazzling light that filled her vision, she saw two figures—and the Grand Mage let out a silent scream.

*The Bow Saint…!*

*Boom!*

The enormous blast was followed by a swelling flash of light that swallowed the entire hill.

* * *

In the final moment, everything happened almost at once.

I’d backed away, anticipating the shock of the tremendous collision.

Far away, the Force arrow had left the bowstring and come hurtling toward us. At last, it struck the shield.

And then—

*Fwoom!*

The distant flash of light swelled, blocking everyone’s view and swallowing the Grand Mage’s figure, which had been hidden behind the crumbling shield.

*Rumble…!*

The earth shook. Light burst forth in an instant, tearing through the darkness and devouring everything.

The force of the blast was beyond words.

*Hngh…!*

I sucked in a breath and curled up as tightly as I could. A gale whipped past me like a blade, slashing through the air.

When that instant—which felt like an eternity—finally ended, I could hear again.

A familiar voice reached my muffled ears.

“Are you all right?”

I let out the breath I’d been holding and raised my head.

Beyond the slowly fading flash of light, I saw a white robe ripped to shreds, blood scattered everywhere, and someone’s limbs torn from their body.

They were slender and white—the limbs clearly belonged to a woman.

“It’s over. All of it.”

“…Ah.”

The Grand Mage was dead.

The moment I finally understood that, I felt all the strength drain from my body.

My mental strength had been at its limit for a long time. Exhaustion washed over me, and my vision blurred.

*Grab.*

A strong hand caught my swaying body.

Jeok Cheongang pulled me firmly to my feet, and a laugh escaped me.

“Sorry, Old Master.”

“For what?”

“Seven and a half minutes. That ran out ages ago.”

Jeok Cheongang laughed along with me.

“Still a hundred years too soon. Can’t you tell, seeing that damned bastard run all the way over here?”

His words said one thing, but he was covered in blood.

Jeok Cheongang answered nonchalantly and pointed toward a spot where an old fiend had somehow survived, like a cockroach.

Of course, there was a reason the Blood-Sword Demon Lord had survived the tremendous blast.

“You went a long way while I was gone. Recklessly far, too.”

So Gyo—or rather, the Bow Saint—looked at me with her usual calm gaze and spoke.

She must have crossed half the land without a moment’s rest, yet her presence still felt as sharp as a blade.

I knew better than anyone why the Bow Saint, despite the crushing fatigue she must have felt, was keeping up this front.

And why she’d gone out of her way to protect the Blood-Sword Demon Lord.

“But the rest will have to wait. There’s still a problem to deal with.”

The Bow Saint was right. The battle below the hill continued even now, despite the Grand Mage’s death.

But that wasn’t the only problem she meant.

“So this is how it ended.”

Her words were edged with cold killing intent. The Blood-Sword Demon Lord lay at her feet, breathing hard. He struggled to speak.

“Fine. Anything… I’ll tell you anything.”

*Anything,* huh?

I quietly rolled the word around in my mind. At the same time, I staggered toward him and raised White Flame.

*Shing.*

I pointed the spearhead at him instead of answering.

Faced with that icy gleam, the Blood-Sword Demon Lord’s voice grew louder, though he’d been trying to sound calm.

“There was a traitor among you!”

The fiend who’d once radiated such terrifying power was nowhere to be seen.

The Blood-Sword Demon Lord sprawled before me now was little more than a beggar, ruined at the end of a lifetime steeped in brutality.

Abandoned by his master. Betrayed by his allies. Now begging for his life by selling information to the very enemy he’d tried to kill.

“Are you afraid?”

“…What?”

“Can things like you feel fear?”

I looked down at his wide, bloodshot eyes and spoke softly.

“There’s no deal.”

The Blood-Sword Demon Lord was already a discarded dog.

Perhaps he’d been doomed to be cast aside after he’d outlived his usefulness long ago.

I didn’t know the exact reason, but this was the outcome the Lord of Heaven had intended. No master would lavish care on a hunting dog he planned to discard without mercy.

So I had no reason to listen to the dog’s words.

Especially if those words were about the traitors whose identities had finally come to light here today.

“Black Night King Sima Gong. The Roaring Fury Swordsman Song Il. And the Taeeul Merciless Sword, Hwangbo Eom.”

“……!”

The Blood-Sword Demon Lord didn’t answer, but his eyes shook violently in response.

That was enough to turn a suspicion close to certainty into certainty itself.

“You already… knew?”

His voice sounded like he’d barely managed to force it out.

I nodded at the Blood-Sword Demon Lord’s dazed face.

“To a certain extent.”

“B-But then why?”

“If you’re asking why… I don’t know.”

I raised my spearhead, feeling an unbearable exhaustion.

At the same time, something came to mind.

Why I’d been able to make it this far, even though I’d suspected there were traitors among them.

Why I’d fought for my life in this unfair situation and refused to give up until the end.

And maybe…

“I wanted to believe a little longer.”

“……!”

“You can’t win without believing in them. That’s why I came all this way like a fucking idiot.”

Yeah.

That was what made victory possible.

The difference between Dark Heaven and us.

The difference between the Lord of Heaven and me.

And I’d already seen the result of that slender thread of faith and hope with my own eyes.

Or, more precisely, the faith that began with one person.

*Sama Pyo.*

Quiet and gloomy, but someone who’d never once betrayed my trust.

A comrade who’d never stepped back first, no matter how dire the situation. We’d fought back to back, then laughed together, covered in each other’s blood.

No—he was my friend.

*If it weren’t for him, I wouldn’t have been able to place even this little faith in them.*

Not long ago, Jeok Cheongang had asked me what I’d do if it turned out Sama Pyo and Taishan had betrayed us.

I hadn’t answered.

Even as I walked down the Great Snow Mountain with Sama Pyo, I’d asked myself the same question. But I couldn’t bring myself to answer it.

I couldn’t kill them.

All I could do was believe. More desperately than anyone.

And I wasn’t the only one who’d put their faith in the traitors.

*A Junior Brother in his two Senior Brothers. A son in his father.*

In the end, their faith had been rewarded.

It had moved the traitors’ hearts and finally turned the tide of battle.

I’d seen it.

The Taeeul Merciless Sword and the Roaring Fury Swordsman throwing themselves at the Hell Fire. Sima Gong taking on the Blood-Sword Demon Lord in Jeok Cheongang’s place.

Of course, they wouldn’t be forgiven for their crimes.

At least, I had no right to forgive them.

Neither did Jeok Cheongang or the Bow Saint.

But I would remember that, in their final moments, the traitors had upheld at least the smallest measure of honor.

Unlike the discarded hunting dog, who would soon be forgotten by its master.

“That’s why we’re different. You and us.”

The Blood-Sword Demon Lord looked at me as I whispered in a small but clear voice. His eyes were red, their blood vessels burst.

“Jin Taekyung!”

Then, just as his cry erupted like a mouthful of blood—

*Thrust.*

The spearhead slid smoothly into his chest, as if cutting through tofu, swallowing the rest of his words.

No—swallowing the last faint traces of life left in him.

*Ding.*

A clear chime rang in my ears.

At the same time, a refreshing energy swept through my body like a mountain stream, once again filling me with new strength.

Unlike the person who’d met a gruesome death, pierced by a silver-white spearhead.

And just as someone who’d died a little earlier—so horribly she couldn’t even keep her body in one piece—had wanted.

*I mustn’t fall here? I have to get stronger than I am now?*

Feeling the crushing mental exhaustion weighing on my body, I turned to look toward the last trace of the Grand Mage, left behind where the Force arrow had swept through.

I murmured a word in my heart, one she could no longer hear.

*Don’t worry. I’ll do it. I promise.*

I didn’t know what the Lord of Heaven wanted.

But one thing was clear.

I had to keep going. To keep moving forward, I had to grow stronger.

Strong enough to far exceed the Lord of Heaven’s expectations—strong enough to make him regret this choice someday.

*Whatever gets in my way, I’ll just smash it to pieces.*

That was how I’d lived until now, and that was how I’d live from here on.

With that thought, I turned my unsteady body around.

Or at least, I tried to.

Until I saw the sharp, clean cuts on the slender arms and legs, one each, lying in a pool of blood, severed from a body.

No.

“……!”

Not until I spotted the traces of Teleport.
## Chapter artifact 1053

# Chapter 1053

Amid the tremendous shock, as if the world had stopped, Jin Taekyung caught his breath for an instant.

At the sight of this guess flashing through his mind—a guess he didn’t want to believe—a corner of his chest throbbed as if he’d been stabbed.

“What happened…?”

“Wait. Just a moment.”

At the sight of Jin Taekyung suddenly frozen like a statue, Jeok Cheongang realized something and raised a hand to stop the rest of the Bow Saint’s question.

Of course, he knew.

That every moment was precious.

A fierce battle was still raging below the hill.

But by now, they understood each other from a glance—or even without looking into each other’s eyes.

The old Master was certain that his young Disciple had a good reason for acting this way. He wasn’t wrong.

Step. Step.

Though staggering from extreme exhaustion, Jin Taekyung walked somewhere as if entranced.

The scene before him drew nearer little by little, imprinting itself sharply on his retinas.

Torn to shreds, the tails of a pure white robe fluttered in a breeze from somewhere. A small pool of blood lay nearby.

They were the last traces proving someone had been there. Jin Taekyung reached out with a trembling hand and touched the largest of them.

A woman’s arm and leg, slender and white enough to show the veins beneath her skin.

Even now, dark red blood was gushing from their cross sections. They were cut with unbelievable precision, smooth and sharp.

As if they hadn’t been cut off, but “separated.”

*This… definitely wasn’t a wound caused by Force.*

At last, faced with the truth, Jin Taekyung let out the breath he’d been holding.

There was no doubt. He couldn’t mistake it.

Because he belonged to two worlds.

He was a Murim martial artist and a Hunter.

That was why he could recognize better than anyone the marks left on these arm and leg, each severed from its owner’s body.

“Teleport…”

At Jin Taekyung’s sigh, which slipped past his lips without his even realizing it, Jeok Cheongang came up beside him and asked, his face rigid,

“Tell me the situation isn’t what this old man thinks it is.”

Jin Taekyung didn’t answer.

But Jeok Cheongang already knew that silence meant yes.

“That bizarre sorcery again. No, Magic?”

That was right.

Magic. That damnable Magic.

Overcome by an indescribable sense of helplessness, Jin Taekyung quietly nodded. A gleam flashed in Jeok Cheongang’s eyes.

He was already worn down by injuries, both large and small, and by exhaustion. Yet there wasn’t a trace of resignation in those eyes, where flames seemed to pour forth.

“This isn’t the time. Before it’s too late, we need to—”

“It’s already too late.”

“What?”

Jin Taekyung clenched his teeth instead of answering.

Teleport.

Among countless kinds of Magic, it was infamous for being exceptionally difficult: a spell that moved someone through space.

Unlike Blink, which was limited to short distances, Teleport could cover dozens or even hundreds of kilometers at once, depending on the mage’s Grade and how much mana they possessed.

Not hundreds of *jang*, but hundreds of kilometers.

Then how far could Grand Mages, who had reached the edge of the truth of Magic, go?

*If… all the conditions were perfectly aligned, maybe they could cross half the continent.*

Jin Taekyung didn’t know the exact distance.

What mattered was that the Grand Mage—a big catch—had already torn through the net and fled far away.

Jin Taekyung felt exhaustion weigh even more heavily on his whole body as he parted his lips.

“She’s beyond our range. By now, she must be at least dozens of *ri* away.”

“What do you mean…!”

Jeok Cheongang’s eyes widened, but he had no choice but to swallow the rest of his words.

To move dozens of *ri* in the blink of an eye—it was unbelievable, far beyond common sense.

But he already knew. He’d even seen it with his own two eyes.

The inexplicable phenomena connected to Dark Heaven.

The ghostly power called Magic, which couldn’t be explained by words or common sense.

“Goddamn it!”

*Boom!*

The ground split like a spiderweb beneath Jeok Cheongang’s foot as he slammed it down in rage.

Beyond the deafening crash, the Bow Saint’s low voice rang out.

“Even if you’re right, her limbs were torn apart. Her life must be in danger. Couldn’t she have lost her life?”

Jin Taekyung weakly shook his head.

“I don’t know. But I doubt that’s likely.”

“Why?”

“There must be people there, too, who are called mages—or sorcerers.”

“Then…”

“Yes. She returned to her allies. We can’t guess where that is, but the Grand Mage would have known exactly.”

Jin Taekyung added, staring at the arm and leg submerged in the pool of blood,

“She must have believed she could survive. That’s why she took a gamble like this.”

Teleport was a high-difficulty spell for long-distance movement.

The coordinates of the starting point and destination had to be accurate to the smallest margin, and the spell required more thorough preparation than any other.

Even high-ranking mages in modern society, who made a living specializing in Teleport, were no exception.

If anything, they were more on edge because they knew its dangers better than anyone.

If even the slightest figure went wrong as the spell took effect, they could die instantly, fused with a rock or a tree.

Or…

*Their limbs could be separated.*

The thought quietly surfaced in Jin Taekyung’s mind.

With a heavy gaze, he looked at the flesh severed from its owner’s body.

It no longer signified someone’s death.

It was proof that the Grand Mage had risked her life on a gamble—and succeeded.

*I made a mistake. I should’ve finished her off myself, made absolutely sure.*

He hadn’t expected it.

Not that the Grand Mage would attempt Teleport in the midst of that frantic situation, with the starting coordinates changing every moment.

And not that Teleport would succeed under such terribly unstable conditions.

But regret always came a step too late, and Jin Taekyung had to keep walking the path ahead of him.

The narrow, treacherous path that now seemed clearer and closer—and yet, for some reason, more distant and beyond reach.

Toward the being waiting at its end.

*Lord of Heaven.*

The name hovered on the tip of his tongue, never spoken. Jin Taekyung silently chewed it over, bitter as bear gall.

Who on earth was he?

What was he trying to do, staining the whole world with blood and beckoning to Jin from behind that dark red curtain?

And…

What connection did he have to the other being who’d been lingering in Jin Taekyung’s mind—not just now, but for a long time?

*The Demon King. Asmodeus.*

The ruler of the Demon Realm. The lord of demons.

An invader who’d torn through the boundaries between dimensions with his overwhelming power, shattered every convention and civilization, and driven billions of people to terror and death.

But in the end, he’d fallen to the hand of a single human—and would now be remembered forever as a part of history.

*Right. He’s dead. He definitely is.*

Then why?

Why on earth couldn’t that accursed being leave his mind?

*Crack.*

Jin Taekyung bit his lip until it bled.

In the years he’d spent moving between the modern world and Murim, he’d seen countless lights and shadows.

But the darkness cast by the name *Dark Heaven* was deeper and denser than any of them. And the existence of the Lord of Heaven, at the center of it all, had become too difficult to deny any longer.

After all the bizarre phenomena that tore common sense apart, now there was Magic, too.

*What on earth is waiting at the end of this?*

Jin Taekyung suddenly turned his head and looked somewhere far to the west.

The Demon King and the Lord of Heaven.

The Lord of Heaven and the Demon King.

He didn’t know whether they’d originally been one being or two entirely different people. The greatest enemy of his life was somewhere beyond the western horizon.

Beckoning to the Chosen One.

For some reason known only to him—one that no one else could yet understand.

And even knowing all this, Jin Taekyung had no choice but to keep walking this path.

Silently and desperately, giving his chosen path everything he had.

*Splash.*

Jin Taekyung rose, stepping in the pool of blood, and forced himself to take a step.

To finish the battle that still wasn’t over.

Toward the countless enemies still killing and dying, even now, like soulless puppets.

“Can you hold on?”

“No.”

Jin Taekyung gave a faint smile to his Master, who’d voiced concern at the sight of his Disciple looking ready to collapse at any moment.

“But I have to. Somehow.”

In the past and in the present.

Just as he always had.

*Whoosh!*

Jin Taekyung charged toward the enemy without hesitation.

At his side, shoulder to shoulder with his old Master.

And with Force arrows already streaking through the air above their heads.

They weren’t the only ones rushing to the battlefield to bring this vast, horrific battle to an end.

*Bwooo!*

At the sound of a horn that rang out without warning, those who turned their heads saw it.

A pale cloud of dust sweeping across the vast mountain range of the Great Snow Mountain as it charged toward the battlefield.

At the head of thousands of people and horses, a group fiercely waved a torn banner and roared as if coughing up blood.

“Subdue the Demons! Destroy Heaven!”

Hundreds of shouts, imbued with pure internal energy, burst through the air. The banner billowed in the wind as it advanced with them.

Not the blood spattered across the pure white cloth, nor the pieces torn away, could erase its meaning.

It was their pride.

Long ago, it had also been a line of verse written by an old man called the Poet Sage, praising the Daoists who lived in the remote mountain valleys.

“*With one long sword to guard the body, one would seek support from Kongtong.*”

After Jeok Cheongang’s voice scattered on the wind, the Bow Saint finally parted her tightly closed lips.

“To protect yourself with a single long sword, rely on Kongtong.”

And at that very moment—

*Rrrrrumble!*

In the brief span of less than two shichen, this cruel battle had swallowed more than ten thousand lives.

The scales that would decide its victor tilted completely.

No—they broke.

Just as some unknown person, somewhere thousands of *ri* away, had intended when they prepared today’s stage.
## Chapter artifact 1054

# Chapter 1054

“Awaken.”

Nothing more was needed.

At the brief whisper that roused her mind as it sank beneath the surface of sleep and took command of her thoughts, her tightly shut eyelids opened without the slightest movement.

“Ah.”

A short gasp, followed by an exhalation.

At last conscious again, the Grand Mage looked at the pitch-black darkness pressing in from every side and finally understood.

Her gamble in the final moment, taken at the risk of her life, had succeeded.

And that was why she, who had suffered a wound severe enough to kill her, was still alive.

“Heaven above and earth below, all demons bow in reverence!”

The Grand Mage poured out the eight characters of the sacred words engraved upon her soul, then hurriedly prostrated herself before the deep darkness.

First she dropped to both knees, then placed both arms on the ground, and finally struck her forehead against the stone hard enough to make it ring.

Thud. Thud. Thud.

Blood drops fell onto the cold stone floor as pain throbbed through her forehead, but the Grand Mage paid them no mind.

It was all thanks to one being’s grace that she could prostrate herself like this—and that she had recovered the arm and leg torn away when she was swept up in unstable space.

“This foolish and lowly servant presents herself before the great Lord of Heaven.”

At the Grand Mage’s voice, filled with utmost reverence, the darkness surrounding her rippled slowly.

“Speak. Everything you saw and heard.”

A short phrase echoed inside her mind.

But the Grand Mage knew better than anyone that her master wasn’t asking about the outcome of the battle.

Her master’s attention was fixed on only one person.

“I sought to carry out the Lord of Heaven’s command, even at the cost of my life.”

The Grand Mage continued, not daring to raise her face.

She told him roughly how many allies had fallen to Jin Taekyung, how many Black Ghosts had been brought down along the way, and how the battle had unfolded from beginning to end.

“So, shameful as it is, I had no choice but to flee in haste. Please, kill me.”

When she had finished speaking, the Grand Mage quietly bit her lip.

She had done her utmost, but not everything had gone perfectly according to plan.

Then, amid the Grand Mage’s fear, her mind echoed once more.

“You did not see the Blood-Sword’s life taken?”

“…No. And I failed to predict that the two Daoists of the Zhongnan Sect and Sima Gong would betray us again. Even if I had ten mouths, I would have no excuse.”

The Black Night King Sima Gong, who had been allied with the Blood-Sword Demon Lord.

And the Roaring Fury Swordsman Song Il and the Taeeul Merciless Sword Hwangbo Eom, whom he had drawn in as well.

The Blood-Sword Demon Lord, who had recruited the traitors starting with the Black Night King, had no idea. Under the original plan, they would all have been dead by now.

And Jin Taekyung should have killed them before the real battle even began.

“However, things went wrong in an unexpected way even before that.”

“What?”

“Kongtong.”

The Kongtong Sect.

They had been the first supporting players in the stage the Grand Mage had planned.

The survivors of the Kongtong Sect, driven from Dunhuang, were supposed to join the allies in the rear and reveal every detail of what they had seen and heard.

The overwhelming military strength of Dark Heaven. The strange power called Magic.

And, finally, the crucial seed of suspicion that would expose the traitors—that had been the Grand Mage’s intention.

“So I let word of the traitors reach their ears. Then I let them go, pretending I had failed to find them.”

She hadn’t merely lost track of them.

She had let them go. Deliberately.

It was an audacious claim, almost unbelievable when spoken of the Kongtong Sect, one of the Nine Sects and One Gang. Yet even now, the Grand Mage was certain.

Had she and the mages under her command joined the pursuit with the intent to kill, the Kongtong Sect would have been wiped out in Dunhuang.

But the Grand Mage had made no effort to capture and kill them.

Unlike the Blood-Sword Demon Lord, her goal hadn’t been victory.

Her only separate order from the Lord of Heaven had been to ensure Jin Taekyung’s survival and growth.

That was why at least some of the Kongtong Sect had survived.

When she heard that their survivors, including the Sect Leader, had shaken off the relentless pursuit and escaped the encirclement, the Grand Mage had smothered a laugh to keep the Blood-Sword Demon Lord from noticing. She had already been thinking of what would come next.

The survivors would return and reveal the truth. Jin Taekyung would execute the handful of traitors and become the enemy’s new rallying point, then win a sweeping victory in battle.

A plan that was both safe and perfect.

But…

“Some of the survivors who knew the truth, including the Kongtong Sect’s Sect Leader, vanished without a trace.”

At that, the darkness rippled violently.

“Vanished without a trace?”

“Yes. I beg forgiveness, but even the power of the sorcery you granted this servant could not find them. At some point, they disappeared to a place I cannot guess.”

The first unexpected crack had appeared, but even the Grand Mage could not follow their trail.

Time passed. The real battle began. New cracks appeared one after another.

The traitors, for some reason, had again chosen the foolish path despite the battle turning against them.

Jin Taekyung had severed his own heart meridian and gambled his life.

And the Grand Mage herself had been put in danger by the arrival of the Fire King and the Bow Saint.

“Please punish this lowly servant, who failed to carry out the mandate of Heaven.”

She had achieved her immediate objective, but that was all.

The Grand Mage bowed her head even lower.

She waited for her master’s fury to shake heaven and earth.

But contrary to her fears, the mind-voice that echoed from deep within her a moment later, as if resonating, was as emotionless as ever.

“Raise your head.”

The Grand Mage obeyed as if entranced. Beyond the dense veil covering her face, the darkness writhed as though alive.

It was deeper and denser than at any point in the past several decades.

“Can you see it? Can you feel it?”

The Grand Mage didn’t answer her master’s question.

No—she couldn’t answer.

Her pupils, which had rolled back until their whites showed at the sight of the darkness, were already turning black.

“I can see. I can feel. Everything hidden inside you. Clearly.”

*Whoooosh.*

The darkness that had completely consumed her retinas didn’t stop there. It continued to spread.

Faster. Deeper.

It seized the mind of its loyal servant, whose slender frame trembled as she lost her reason. It swept through her thoughts and shook her soul, then returned to its master.

As if nothing had happened.

*Thump.*

“Ah—h-hah. Hah!”

The moment the darkness left her eyes and their focus returned, the Grand Mage crumpled like a marionette with its strings cut, gasping for breath.

“M-My Lord of Heaven.”

Her voice trembled. Her eyes were full of fear.

The Grand Mage knew instinctively.

Just now, the Lord of Heaven had read and looked into every one of her thoughts and memories.

At the same time, an awe so intense it raised goose bumps drove out her fleeting fear and enveloped her whole body.

*That power…*

Remembering the force that had seeped into her body and seized her soul, the Grand Mage trembled.

She knew it had been no more than a tiny fragment of his power. That only made her wonder and shock all the greater.

*Just how far do his powers reach?*

Even a thousand-year-old tree could never touch the clouds.

But the Lord of Heaven was different.

From the moment she had first met him, he had been the absolute ruler, beyond compare. And day by day, he had grown stronger to a degree that made the very word *limit* meaningless.

So much so that even the Grand Mage, one of his closest confidants, was astonished.

And she already had an idea where this unbelievable change had begun.

*Jin Taekyung. No—the Chosen One.*

There could be no doubt.

A little more than two years ago, when bloodshed swept through Shanxi Province and the epithet Hidden Dragon became known throughout the land, her master had begun to change as well.

He had begun waking more often from deep slumbers that could last up to ten years and, even at their shortest, nearly a year. Each time, the Grand Mage could feel the Lord of Heaven’s power had grown stronger.

Even here, today.

*But what could that possibly have to do with—?*

The question came naturally.

But the next moment, a thunderous echo shook her mind, turning her thoughts blank.

“No question belongs to you.”

“……!”

“Do not forget what your master wants. Do not forget what you must do.”

The Lord of Heaven’s voice seemed to pierce her soul. The Grand Mage realized she had momentarily forgotten something.

That the being before her was an absolute ruler, transcending everything.

That, as his servant, she could not permit herself to question or doubt him.

“Please, please kill this irreverent servant!”

The Grand Mage cried out as if she were coughing up blood.

Prostrate, as though she would become one with the cold stone floor, she reaffirmed her loyalty—a devotion that could only be called fanatical—and praised her master.

She kept at it until her clear, calm voice, like the sound of a silver bell, grew hoarse and cracked.

Until her master finally issued his command to the lowly servant who had dared, even for an instant, to harbor a question.

“That is enough.”

*Rustle.*

The darkness rippled gently for an instant and wrapped around the Grand Mage.

As if caressing her tenderly.

“Nothing of the sort will ever happen. Your master knows that, unlike the foolish hound called the Blood-Sword, your loyalty is steadfast and pure.”

“My Lord of Heaven…!”

“Go. To the place waiting for you. Join forces there with another of your master’s loyal servants and complete a new mission. The completion of the great plan is now truly close.”

At the trust in her master’s words, conveyed more clearly than ever before, the Grand Mage couldn’t hold back her overwhelming emotion. Tears filled her eyes.

“I will risk my life to fulfill the mission entrusted to me.”

“I believe you. Just as I always have.”

As his quiet voice echoed in her mind, some of the darkness wrapped around the Grand Mage sank deep into her body.

No—it seeped into her as if they had always been one.

*Fwoosh.*

The Grand Mage shuddered as an unprecedented power surged from deep within her.

At the same time, she could sense what this immense new power her master had given her wanted at that very moment, and where it was leading her.

*Qinghai.*

At that instant—

*Whoooom!*

A brilliant white flash suddenly swelled and burst out, engulfing her slender body.

*Pop.*

It all happened in an instant, and ended in an instant.

At last, the Grand Mage had vanished without a trace. In the pitch-black space where she had disappeared, the absolute ruler remained alone and murmured quietly.

“Time is passing.”

As the darkness slowly dispersed, a mysterious green light glimmered faintly.

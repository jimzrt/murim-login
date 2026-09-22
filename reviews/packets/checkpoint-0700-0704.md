# Checkpoint Review — 700–704

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

# Chapters 700–704

## Plot

As the Nanman Beast Palace collapses, Jin Taekyung and the guardian spirit fight to prevent the rift’s demonic qi from mutating the trapped humans and beasts. Jin battles the Southern Heaven Demon Empress and her regenerative masked hunting dog, whose dark Force, lack of pain, and repeated recoveries make him nearly impossible to kill. Jin wounds the Empress severely, but she is continually stabilized and strengthened by the rift.

Jin uses One Annihilation to devastate the Inner Palace and destroy the surrounding mutants, yet the Empress survives at great cost, losing an arm, part of her side, half her face, and her cultivated youth. As the sacred stone, guardian spirit, and White Tiger weaken under the demonic qi, Jin orders the guardian spirit to save the people. The Empress prepares to execute them, but Yayul Cheok arrives and blocks her attack. Jin recovers enough to fight beside Yayul and the guardian spirit.

The Empress’s expected five hundred elite subordinates still have not appeared. Yayul summons reinforcements through a path in the darkness, and Wang Ho arrives with the white-armored Baekcheon Unit, addressing Yayul as Palace Lord.

## Continuity

- The Southern Heaven Demon Empress is Honglan and is fighting Jin Taekyung, Yayul Cheok, and the guardian spirit inside the corrupted Nanman Beast Palace.
- The Empress has lost one arm, part of her side, half her face, and her cultivated youth, but the rift’s demonic qi continues healing and strengthening her.
- One Annihilation caused massive destruction and erased the surrounding mutants but failed to kill the Empress. Jin survived with severe Internal Injury, Exhaustion, and Muscle Rupture.
- The masked man is the Empress’s trained hunting dog. The guardian spirit has killed him four times, but he repeatedly regenerates, recovers faster, and grows stronger.
- The rift’s demonic qi is spreading from the Inner Palace into the Outer Palace, corrupting Nanman tribespeople and weakening the sacred stone, guardian spirit, and White Tiger.
- Yayul Cheok has recognized the mutants as Nanman tribespeople he loves and is enraged by their corruption and deaths.
- Jin has expelled stagnant blood and recovered enough strength to fight alongside Yayul; his weapon hand is steady again.
- Nearly one thousand mutants remain in the battlefield, but they hesitate after sensing the changed balance and the Empress’s silence.
- The Empress’s approximately five hundred elite subordinates have not arrived despite the rift remaining open for more than half a shichen.
- Yayul refers to an unnamed person who foresaw the disaster, retained hope, and followed an irreversible path despite guilt. That person’s identity and actions remain unresolved.
- Wang Ho leads the white-armored Baekcheon Unit and has arrived as reinforcements for Yayul, whom he addresses as Palace Lord.
- It remains unresolved whether the combined forces can defeat the Empress, stop the mutants, and prevent Nanman’s destruction.

## Translation Decisions

- Retain **Southern Heaven Demon Empress**, **Honglan**, **guardian spirit**, **White Tiger**, **Force**, **demonic qi**, **sacred stone**, **One Annihilation**, **Fist Force**, **Moving Formation**, and **Baekcheon Unit**.
- Use **Palace Lord** for 궁주 and **Commander of the Baekcheon Unit** for 백천대주.
- Use **masked man** for 복면인 and keep his identity and connection to the Great Snow Fiend unresolved.
- Use **shichen** for 시진 and **the time it takes to drink a cup of tea** for 일다경.
- Preserve Jin Taekyung’s blunt, conversational profanity and the guardian spirit’s terse telepathic voice.

## Durable state

{
  "active_continuity": [
    "Yayul Cheok has arrived at the Inner Palace and joined Jin Taekyung and the guardian spirit against the Southern Heaven Demon Empress.",
    "Yayul Cheok recognizes the mutants as Nanman tribespeople he still loves and is consumed by grief and fury over their corruption and deaths.",
    "Jin Taekyung has expelled stagnant blood and recovered enough strength to fight alongside Yayul Cheok and the guardian spirit.",
    "The Southern Heaven Demon Empress has lost one arm and considerable strength and now faces the combined threat of Jin, Yayul, and the guardian spirit.",
    "The nearly one thousand mutants hesitate because their instincts sense the changed battlefield and the Empress's silence.",
    "The Empress's approximately five hundred elite subordinates have not appeared despite the rift being open for more than half a shichen.",
    "Someone foresaw the disaster and retained hope despite guilt and an irreversible path, but that person's identity is unstated.",
    "Wang Ho leads the white-armored Baekcheon Unit and has arrived as reinforcements for the Palace Lord."
  ],
  "continuity_sources": [
    704
  ],
  "open_questions": [
    "Why have the Southern Heaven Demon Empress's five hundred elite subordinates not arrived?",
    "Who is the person Yayul Cheok says foresaw the disaster and retained hope until the end?",
    "Can the Baekcheon Unit change the battle's outcome?",
    "Can Jin Taekyung, Yayul Cheok, and the guardian spirit defeat the Southern Heaven Demon Empress and stop the mutants?"
  ],
  "safe_through": 704,
  "temporary_decisions": [
    "Retain Fist Force, Force, Moving Formation, demonic martial arts, and Baekcheon Unit as established terminology.",
    "Render 궁주 as Palace Lord and 백천대주 as Commander of the Baekcheon Unit.",
    "Retain shichen for 시진 and the time it takes to drink a cup of tea for 일다경.",
    "Preserve Jin Taekyung's conversational profanity and the guardian spirit's terse, telepathic voice."
  ],
  "version": 1
}

## Reading copies

## Chapter artifact 700

# Chapter 700

Me, the Guardian Spirit, and the Southern Heaven Demon Empress.

Less than fifteen minutes had passed since the battle began, but so far, the best way to describe its flow was that we were evenly matched.

At least, until now.

Rumble, rumble, rumble!

“……For fuck’s sake.”

The curse slipped out of my mouth before I could stop it.

Not simply because the Inner Palace was collapsing. No matter how much it symbolized the Nanman Beast Palace and its pride, it was still just a building in the end.

The problem was that, at the same time the largest structure in the Nanman Beast Palace was crumbling like a sandcastle, the darkness flowing from the rift had grown even thicker.

Kraaaaaash!

Demonic qi. Also known as magical power.

That pure yet dangerous energy surged like a wave.

It covered the enormous cloud of dust, crossed the space, and reached the living beings that had not yet escaped the Inner Palace.

“Grrk, keugh!”

—Kyaaaaaa!

The screams of humans and beasts poured forth.

Their eyes, which had gradually begun to regain focus, flooded with white. Their trembling bodies twisted sharply with sickening sounds of splitting flesh.

Crack. Crrrunch.

The word *death* flashed through my mind, but no.

What awaited them was pain worse than death, and the changes that would soon come over them would make them forget even the pain.

*No. I should call it mutation, not change.*

There was no way I could fail to recognize it.

I had already seen it once. I had even experienced it firsthand.

The magical power from the rift was strong enough to corrupt a five-hundred-year-old imugi.

The Water God Dragon had endured the magical power alone, which made its situation different. Even so, ordinary beasts—and even most martial artists—could not shake off its influence through their own strength.

At least, not unless someone helped them.

*And apparently, that someone is me.*

For fuck’s sake.

My hesitation at having to leave the guardian spirit alone had lasted only a moment.

There were still several thousand humans and beasts left inside the Inner Palace.

Their safety was reason enough, but if those who had been completely consumed by the magical power became mutants, the hellscape the Southern Heaven Demon Empress had envisioned would be complete.

Putting everything else aside, a horrific slaughter would begin, with them killing one another over and over.

And in that moment—too brief to even be called an instant—I was not the only one to reach that conclusion.

—Go! Hurry!

It happened almost simultaneously.

The instant a single thought rang inside my head, I kicked off the ground.

Boom!

Compression. Then explosion.

The scenery changed along with the violent wind that swept over my entire body.

My body shot forward like a cannonball, creating a small crater as I crossed more than sixty yards in one bound. Flames of manifested qi shimmered beneath my toes as they touched the ground softly.

Flamefire Path.

Kraaaaaash!

In the slowed world, blue-white light-flames burst out like an explosion.

The guardian spirit charging toward the Southern Heaven Demon Empress with a roar that shook the heavens vanished from sight.

So did Muyaho, racing out of the Outer Palace with all his strength at the very rear of the survivors.

Whoooosh.

Wind carrying the scent of blood brushed across my entire body. By then, beneath the feet I had planted in midair, I could see countless beasts and humans writhing as darkness engulfed them.

And……

*I can feel it.*

After reaching the Supreme Peak realm and gaining insight again and again, I had come to understand.

Everything in the world had a flow. The fact that something could not be confirmed with the naked eye did not mean it could not be felt.

There was a flow—or perhaps a faint gap—in the formless wind, in solid rock that could repel steel, and on calm water.

That was the grain.

*Now!*

Fwoooosh!

With absolute certainty, I slashed my spear downward like a flash of lightning.

Three jiazi of Scorching Yang Qi coiled around the transparent spearhead, consuming the darkness as it cut through space.

I was cutting the grain within the pitch-black darkness that had wrapped around thousands of lives.

Severing the invisible, microscopic flow in a single stroke.

And then.

Whoooosh—boom!

With a roar that seemed to split the sky, the flames flowing along the White Flame spearhead exploded magnificently.

“……!”

My eyes widened before I knew it.

Despite the fatigue and injuries left by the battles I had fought one after another, this attack had been nearly full force.

I had been confident that, even if I could not disperse all of the demonic qi, I could at least scatter some of it.

*But…… it knocked this away?*

It had been only a brief moment, but I had seen it clearly.

The Force that flew from the darkness like a ray of light.

At the same time, it was far too dark and ominous to be called a ray of light.

Tap.

I landed gently on the ground and glared into the pitch-black darkness.

No—the hazy figure slowly walking out from the ruins of the Inner Palace, shrouded in a cloud of dust.

“……A mask? What the fuck are you supposed to be?”

The answer to my question was a single flash of light that glinted from more than thirty yards away.

Shwaaaak! Slash!

It was a matter of a hair’s breadth.

I twisted my head like lightning and glanced over my shoulder. A pavilion that had somehow retained its shape until now had been crushed and split in half.

Crack. Rumble!

Watching the pavilion collapse half a beat late, I muttered inwardly.

*Fast.*

I could also sense an unrefined, savage power.

That could be called rough, but in another sense, it meant destructive.

If I failed to evade it even once, there would not be enough of my corpse left to find.

But the same was true of me.

Thrust. Whoooosh!

There was no need to summon a weapon from my Inventory.

Countless weapons were scattered all around us. I pulled an iron spear from the ground, gripped it in reverse, and hurled it with all my strength.

Boom!

The iron spear was blocked by Force and bounced away helplessly.

But I had expected that.

The moment I sent the spear flying, I had launched my body forward as well. I thrust White Flame toward the masked man whose identity I did not know.

Shu-whoom! Boom!

Compressed air burst from the tip of the spear.

The masked man twisted his body by the width of a sheet of paper and evaded the attack, then grabbed the shaft and took a large step forward.

At the same time, dark sword-light flashed from his fingertips.

Slash!

A faint pain.

I had dodged, but not completely. Blood sprang from the bridge of my nose, grazed by the wind created by that powerful sword strike.

But a few drops of blood were a cheap price.

I would obtain something much greater in exchange for the blood I had shed just now.

*If you thought I was like other martial artists, you made a serious mistake.*

Martial artists treated their weapons like their lives.

Most of them had learned martial arts that involved weapons, and they knew that clumsy fist, palm, finger, and kicking techniques could not carry them through a fierce life-and-death duel.

But I was different.

Along with physical abilities that surpassed human limits, I possessed the Fire Gate Clan’s fist, palm, finger, and kicking techniques—martial arts so magnificent that calling them divine arts would not be enough.

And my Inventory, which possessed a capacity close to infinite, held countless weapons.

Crack!

No matter how divine or powerful a weapon was, it was useless if it could not reach the enemy.

The moment I released the spear shaft, I seized the wrist of the masked man holding the sword and thrust out my other hand like lightning.

Along with a command only I could understand.

*Inventory open. Summon.*

Whoosh!

The strike missed its mark—the heart—but the rusty dagger, glowing red from the Scorching Yang Qi, cut through a Body-Protecting Qi barrier harder than armor and drove into his chest.

Puhk!

“……!”

The masked man’s body went rigid without even being able to groan.

But I had no intention of stopping there.

*I have to finish this properly.*

I did not know the masked man’s name or sobriquet, but one thing was certain: he was under the Southern Heaven Demon Empress.

Before half measures brought about an even greater disaster, I had to snuff out his life right here.

Now. In this place.

Crack! Crunch!

Still gripping his wrist, I felt bones shatter beneath the tip of my knee as I drove it up like a flash of lightning.

His arm, with its elbow crushed, hung limply. As the strength left his hand, the sword hilt began to slip from his grasp.

Srrk.

At that moment, the masked man’s fingers moved ever so slightly, and a sound of something breaking through the air rang out from an invisible blind spot.

Whoooosh!

Just as everything in the world possessed its own grain and flow, the same was true of the sounds made by weapons.

*What is that?*

It was definitely a sound I had heard somewhere before.

A sense of incongruity flashed through my mind along with it, but I had no time to follow the thought any further.

I had only the briefest instant to make my choice.

Should I trust my instincts and the Fire Dragon Armor and finish off the masked man completely?

Or should I abandon the masked man, who had already suffered grievous injuries, and protect myself first?

At that moment of an irreversible either-or choice, I hardened my resolve and turned around while thrusting out my hands.

No.

I swung both palms.

Toward the masked man—and the two streaks of light that had rushed right up to my face.

Boom! Crash!

The masked man’s body, struck in the chest by the Flame Divine Palm, shot away like a cannonball and slammed into the ruins of the Inner Palace.

But……

Crrrunch!

Had trying to kill two birds with one stone been too greedy?

My body was forced backward by the tremendous impact. Only after retreating ten steps and carving deep furrows into the ground did I feel the pain, as though I had been burned.

Tap. Drip-drip.

Blood rolled down my fingers and fell to the ground.

After staunching the wound in my left hand, where flesh and muscle had been torn apart and left hanging in tatters, I bit down on my lip.

Was it because of the pain?

Wrong.

I had suffered pain and injuries like this plenty of times back when I was a Hunter.

Having one hand injured while I needed to conserve as much of my strength as possible was certainly a setback, but it was not so bad that I could not use the hand at all.

The real problem was not the injury or the pain.

It was the tremendous rebound force I had felt when my Flame Divine Palm struck the masked man’s chest—and the identity of the flash whose sound alone had caused that sense of incongruity.

*This is……*

The form and size were different, but there was no mistaking it.

It was a weapon I knew all too well.

I stared at the twin wheels clutched in my left hand and slowly turned around.

I thought of the old fiend who had left behind the words that he would be waiting for me in the afterlife.

“What’s your relationship with the Great Snow Fiend?”

Even as I opened my mouth, I hoped I would not receive an answer.

I also hoped the tremendous rebound force I had felt at the very end had merely been my imagination.

But my ominous suspicion had already become reality.

Rumble. Rustle.

Within the cloud of dust that had yet to settle, heavy rebar and timber shifted, and a pale figure rose to its feet.

Then a flashing streak of light crossed more than sixty yards and hurtled at me.

Whoosh! Crrrunch!

Its momentum was truly ferocious.

I caught the streak of light with a hand packed with internal energy and fell silent.

It was a dagger.

The very dagger I had driven into a man’s chest with this hand only moments ago.

Blood that was not mine stained the heavily rusted blade, which was about a handspan long.

Proof that my attack had succeeded.

*If so, he should have suffered a fatal wound…… How the hell?*

I knew this all too well—almost to the point of disgust.

Humans, especially Supreme Peak masters, did not die as easily as one might think.

They were monsters capable of fighting a hundred men alone even with a dagger buried in their chest.

But the situation changed when the person who had driven in that dagger was a Supreme Peak master of similar or greater ability.

*This isn’t a fight between street thugs.*

In a life-and-death duel between masters, the thing one had to be most wary of was not the sharp weapon itself, but the internal energy carried by it.

Internal energy that forced its way through a wound and tore apart the blood vessels inside the body.

Even the greatest Supreme Peak master could not avoid Internal Injury after suffering such an attack.

Even the Great Snow Fiend, who possessed superb martial arts and profound internal energy, had not been an exception.

And yet……

*Not only did he get up as if nothing had happened—he pulled out the dagger lodged in his chest and threw it? While it should have been difficult enough just to suppress his Internal Injury, he even put this much internal energy into it?*

Besides, the dagger was only one of the most serious injuries he had suffered.

One arm was crippled at the very least. And then he had taken a direct hit from the Flame Divine Palm.

Even a master at the level of the Ten Kings could not be that unharmed.

“……You. What the hell are you?”

A sense of incongruity had wrapped itself around my entire body by then, along with a chilly wariness.

But before the masked man could answer my question, a tremendous roar rang out.

Kraaa-boom!

A silver figure slammed into the ground like a meteor.

The guardian spirit, its body covered in wounds, gasped for breath.

And above its head in midair, the Southern Heaven Demon Empress stood with a smile.

“He’s my hunting dog. One I trained with a great deal of care.”
## Chapter artifact 701

# Chapter 701

“He’s my hunting dog. One I trained with a great deal of care.”

The Southern Heaven Demon Empress’s voice rang out softly. At the same time, the masked man took a step forward.

Thud.

Between the hazy clouds of dust, his advancing step did not waver in the slightest.

As the masked man’s form gradually came into focus, I muttered like a groan.

“……Fuck. What the hell is that?”

I wasn’t asking for an answer. I already knew the answer to this question.

*Regeneration.*

Those two words were enough to explain the bizarre sight unfolding before my eyes even now.

Crack. Slither.

Shattered bones joined together, while flesh and blood swelled into place.

Each time darkness that writhed like a living snake brushed across the masked man’s body, his wounds healed and new strength seeped into him.

—The power of defying heaven……

Defying heaven.

It was a sight that seemed to run counter to the will of heaven and the natural order.

As the guardian spirit let its thought flow out like a lament, the masked man, having finished recovering, bent his strangely twisted elbow.

Crack.

He broke the elbow that had already fused back together himself, then aligned it and healed it again.

It was an act accompanied by tremendous pain, yet the masked man did not even twitch an eyebrow. That was when I realized the source of the incongruity I had felt during the battle.

*That bastard can’t feel pain.*

Even someone with a dulled sense of pain would feel at least a little.

But the masked man had not groaned or screamed even once.

Not when the dagger pierced his chest or his elbow was crushed. Not when he was struck by the Flame Divine Palm, which carried horrific heat.

*What the hell did they do to him?*

Did he go and get a painkilling shot somewhere?

As I stared at the emotionless eyes visible above his mask and swallowed a low groan, someone’s small, snow-white foot stepped onto the damp earth.

Scuff.

From the sky to the ground.

At last, the Southern Heaven Demon Empress landed lightly on the ground and smiled.

“You look like you’ve seen a ghost. Then again, I suppose you weren’t all that surprised? You saw it once in Henan.”

Grrr.

Along with a low growl, the enormous body, stained with blood in several places, rose on tired limbs.

But its breathing was far rougher than it had been at the beginning. If it fought right now, it would lose without question.

I stepped in front of the guardian spirit and opened my mouth.

“Yeah, the Blood Lord. That lunatic was the same.”

“It’s a shame. If you hadn’t met the Blood Lord back then, I could have watched you faint dead away by now.”

“If I were that timid, I would’ve been dead a long time ago.”

“Maybe it’s because you’re young. You can’t help the bluffing.”

A bluff.

What the Blood Lord had shown during the Shaolin Bloodshed had certainly been surprising, but not enough to make me faint dead away.

I had seen and experienced far too much in the modern world where I had been born and raised for that.

“Think whatever you want.”

The Southern Heaven Demon Empress narrowed her brow, sensing something in my calm answer.

She slowly looked me up and down with narrowed eyes, then ran her tongue over her red lips.

“I don’t know whether you’re simply brave, or whether you have something no one else knows about…… But you really are strange. I think I’m beginning to understand why the Lord of Heaven is interested in you.”

“Interested?”

As I asked the question, I very slowly circulated my internal energy without letting the Southern Heaven Demon Empress notice.

Dealing with a monster like her was already too much, and now some drugged-up bastard who had apparently gotten a painkilling shot had joined the fight. I had to recover some of the Internal Injury I had suffered earlier and buy myself time.

“Come to think of it, that old man, the Great Snow Fiend, spouted the same nonsense.”

“Oh my. Then do you still think it was nonsense?”

The Southern Heaven Demon Empress smiled and took another step. Tightening my grip on the spear shaft, I answered.

“I wish it were nonsense.”

“Why?”

“To hell with the Lord of Heaven. I don’t want attention from some insane old man. That includes the crazy woman standing in front of me.”

Whoosh—pfft!

A stinging pain flashed across my face, and my cheek grew hot. The Southern Heaven Demon Empress let out a sigh of relief when she saw that I had evaded the Finger Qi by the narrowest margin.

“Phew. I almost killed you. Nice dodge. You’re better than I thought.”

Praise from an enemy. In a situation like this, no less.

It left a foul taste in my mouth, but thanks to it, I learned two things.

First, even if that monstrous woman gave it her all, I could withstand her so long as I suffered only the minimum damage, as I had just now.

Second, killing me would cause the Southern Heaven Demon Empress a greater loss than gain.

Instead of wiping away the blood running down my cheek, I tightened my grip on the spear shaft and replied.

“The Lord of Heaven. Looks like that old man is more interested in me than I thought. Seeing you worry that a crazy woman like you might kill me.”

“……!”

“Now I think I roughly understand why you only watched me in Hubei Province.”

The Southern Heaven Demon Empress possessed truly tremendous martial power. Even when I thought of everyone I had seen and encountered until now, only a very small number of people seemed capable of standing against her.

*At the very least, one of the Ten Kings. Maybe even higher.*

The enormous power I could feel simply from standing in front of her.

Excluding Jeok Cheongang, who was treated as an exception even among the Ten Kings, the Southern Heaven Demon Empress would be one of the ten strongest people in the world today.

*And yet nothing happened. Even though she had dozens, hundreds of chances to act in Hubei Province.*

It was a question I had carried in my heart ever since I realized the Southern Heaven Demon Empress’s identity.

Why had she left me alive?

Because I wasn’t worth killing? For simple amusement?

I didn’t know the details, but I had become certain that wasn’t the case. I was none other than the sole Disciple of Fire King Jeok Cheongang and the successor of the Fire Gate Clan.

If she got me into her hands, she could lure in Jeok Cheongang, who would become a major obstacle to Dark Heaven’s future movements, and kill him. Even if that attempt came to nothing, she could still obtain the Fire Gate Clan’s supreme arts.

There were many ways to pry open a tightly closed mouth.

Torture. Torture. And endless torture.

But the Southern Heaven Demon Empress had neither killed me, who had been completely fooled by her, nor kidnapped me.

She had merely watched me right before my eyes, then vanished without a trace. Like an observer sent on someone else’s orders.

My parched lips moved.

“Why is the Lord of Heaven so interested in me? What reason does he have to take this far, when there are others more worthy of his attention than me?”

Yet even in response to my question, the Southern Heaven Demon Empress’s lips, which had been pressed tightly shut at some point, did not open.

After a brief silence, she gave only a short answer.

“What could a worthless thing like you know of the will of that omnipotent, exalted person?”

*A worthless thing.*

I muttered inwardly as I watched the Southern Heaven Demon Empress’s tense face.

I did not miss the way her gaze had gone still or how she gently bit her lip.

At the same time, a single thought flashed through my mind and became a voice.

“You don’t know, do you?”

“……!”

I saw it clearly.

The Southern Heaven Demon Empress’s eyes shook violently for an instant. A derisive chuckle escaped me.

“Fucking idiot.”

“…What?”

“I said you’re a fucking idiot. You worthless fucking idiot of an old hag.”

And that single remark lit the fuse of the bomb known as the Southern Heaven Demon Empress.

Kraaaaaash!

An enormous storm of qi swept in every direction.

As the Southern Heaven Demon Empress wrapped layer after layer of pitch-black darkness around her entire body, the guardian spirit, which had steadied its rough breathing, sent out a thought.

—If you were going to do it, why didn’t you stall for a little more time?

I did feel a little regret, but there was no other way.

I had to bring this to an end before the humans and beasts remaining in the Inner Palace finished mutating. Who fell and who remained standing would come afterward.

I sent a Sound Transmission to the guardian spirit, which was still grumbling despite its battered body.

—Are you really a guardian spirit? Stop dragging yourself around like you’re about to collapse and fight with everything you’ve got.

—How dare you insult me. If this had been three hundred years ago, I would never have suffered such humiliation at the hands of a mere human.

—Sure. That crazy woman wouldn’t have been born yet, either.

—……Damn it.

The guardian spirit, cursing in a manner unbecoming of its name, raised every strand of fur on its body.

It swept a glance over the two figures approaching from ahead and behind, then muttered.

—The situation has gotten worse.

—Wow. I really had no idea. Amazing, I guess, being a guardian spirit. Thanks for letting me know.

—We’ll each take one. The human male and the human female. Choose one.

—Then I’ll take the male.

—……

*What the hell is wrong with this bastard’s conscience?*

The blue-white eyes staring straight at me seemed to be asking exactly that.

Even in this godforsaken situation, I let out a quiet laugh and started walking.

Toward the Southern Heaven Demon Empress.

Thud.

Maybe it was because I was tense.

The sound of my footsteps rang out unusually loudly. Her eyes had already turned blood red, and a chill settled in one corner of my chest.

“You intend to face me? You?”

Her voice was cold and eerie. I let out a deep sigh before answering.

“That hurts. Worthless creatures like us should help each other survive. Don’t you think?”

“……!”

“Choose. Kill me and get your ass kicked by the Lord of Heaven, or die nicely right here.”

Hack—ptoo.

I spat out phlegm mixed with dead blood and raised the spearhead.

A voice unlike my usual one slipped between my lips, cold enough to feel unfamiliar.

“For the record…… I’ll fight until I die.”

Fwoosh—boom!

Flamefire Path.

A single line of flame shot forward, consuming the air as it flew.

And at the end of that path stood a monster wrapped in deep darkness.

Shwaaaak—boom!

* * *

Bang!

The world shook with an immense shockwave.

The ground split apart beneath the spearhead Jin Taekyung had swung down, and horrific heat burst upward.

The Southern Heaven Demon Empress avoided the attack by a hair and extended her hand.

Kraaaaaash!

A palm strike carrying unprecedented qi collided with the spearhead slicing through space like a ray of light.

A tremendous clash of qi.

But the difference in strength was clear.

Boom!

Along with the sound of compressed air exploding, one figure was hurled backward.

Joy filled the Southern Heaven Demon Empress’s eyes.

*That wretch is nothing.*

Jin Taekyung’s martial power had clearly advanced at an unbelievable pace. He had changed so much that she found herself wondering whether he was truly the same boy she had met in Hubei.

She even wondered whether the greatest obstacle to this grand scheme might have become Jin Taekyung instead of the Beast Miao King.

But……

*I have grown even stronger.*

She could feel the unprecedented power boiling throughout her body.

*The denser the demonic qi flowing from the rift becomes, the stronger I become.*

Even at this very moment.

Pop!

A single step.

The Southern Heaven Demon Empress vanished like a ghost, then appeared in midair.

As she plunged downward like a meteor, Jin Taekyung, buried deep in the ground, opened his eyes wide.

Crack.

The solid ground crumbled like mud.

Jin Taekyung narrowly evaded the attack and flicked his sleeve.

The dagger that came flying from somewhere, as if he had created it out of thin air, was easily avoided by the Southern Heaven Demon Empress. She then thrust out her hand like a flash of lightning.

Slash!

It had only grazed him.

But her fingers, curled like hooks, tore through his martial uniform and sliced into his thigh.

Blood gushed upward, and Jin Taekyung staggered.

The Southern Heaven Demon Empress smiled brightly as she brought a knife-hand strike down toward him.

Shu-whaack!
## Chapter artifact 702

# Chapter 702

Shwaaak!

A straightened hand-blade sliced through the air and came crashing down.

A slender, snow-white hand—one that looked as though it had never had a single drop of water touch it in its life.

But Jin Taekyung knew.

He knew how much blood had flowed from that hand.

He knew what kind of darkness lurked behind the beautiful face of the Southern Heaven Demon Empress, smiling so brightly that it hurt to look at.

*Monster.*

Those two words surfaced in his mind once more.

At the moment the blood-red Force falling like a meteor sought to pierce the crown of Jin Taekyung’s head, his two legs, which had been frozen stiff as though nailed to the ground, finally moved.

Shhk!

The earth split apart like tofu. Jin Taekyung narrowly evaded the Force and thrust his spear forward like a flash of lightning.

Shwaaak!

Terrifying speed and power. Along with them, a spearhead shot toward a single point with frightening precision.

Even a fistfighter who had honed his hand-to-hand techniques for his entire life and reached the Supreme Peak realm would have been unable to meet that strike head-on.

But the Southern Heaven Demon Empress was different.

No.

At the very least, today’s Southern Heaven Demon Empress possessed enough power and qualification to do so.

Krrrkkk!

*Empty-Hand Seizes the Blade.*

The spearhead, hellfire flickering around it, trembled between the Southern Heaven Demon Empress’s palms, which she had brought together as though in prayer.

Her snow-white hands, which should have been reduced to ash long ago, held a tremendous concentration of energy.

The corners of her smooth lips, free of even a single wrinkle, slowly lifted.

“With only this much…”

The instant her voice, filled with mockery, emerged—

Plop. Plip.

The Southern Heaven Demon Empress noticed the drops of blood falling one by one and closed her mouth.

As the pain arrived half a beat late, she saw Jin Taekyung smiling sheepishly at her.

“Oh, I forgot to mention. This is Ten-Thousand-Year Cold Iron.”

“……!”

“But what were you saying?”

The Southern Heaven Demon Empress’s delicate brow twisted. At that moment, Jin Taekyung released the spear shaft in his hands and stretched out both arms.

*Palm Force?*

But the Southern Heaven Demon Empress’s guess missed its mark completely.

Shhk! Shhk!

Two daggers suddenly shot toward her throat and chest. They were too close for her to evade immediately.

Left with no choice but to release the spearhead she had been holding, the Southern Heaven Demon Empress shook her sleeves violently.

Whoooosh!

The wind that burst from her voluminous sleeves sent the daggers flying away.

At that instant, Jin Taekyung’s toe caught the end of the White Flame’s spear shaft, which had been slowly tilting.

No—he kicked it.

*…What?*

He kicked it?

And in a situation like this, he had kicked away the divine weapon that would have helped him most?

Along with that shockingly baffling question, a flash of light shot toward the Southern Heaven Demon Empress’s face.

Shwaaack! Slash!

It happened in the blink of an eye, and the attack was even more irregular than it was fast. Fully evading it was nearly impossible.

The Southern Heaven Demon Empress turned her head on instinct and felt pain shoot from her earlobe. Her eyes flew open.

“How dare you!”

She would not have been this furious if only her earring had shattered. It had been a possession she rather liked, but she could always obtain another one.

But her earlobe had been torn, and her hair had been cut as well.

Fully half of her thick, glossy hair—always a source of pride—had been cut away.

“Die!”

Kraaaaaash!

The unprecedented energy that had faltered for a moment surged through her slender body.

The pressure seemed capable of crushing even a massive boulder in an instant.

But the Southern Heaven Demon Empress did not know.

The young—no, the impossibly young—enemy before her had once climbed a cliff with iron balls weighing well over a thousand geun strapped to his body.

Crack. Crrrunch!

The earth sank beneath the pressure crushing everything within a radius of over ten jang, while the limbs of the humans and beasts struggling in the area twisted and snapped.

—Krrk, krrrk!

“Aaaaaagh!”

Amid the space overflowing with blood and dying screams, Jin Taekyung, who had endured the pressure, stamped his foot.

Boom!

Along with a line of flame that rose from his toe, his body shot forward.

At the same time, a spear that no one knew when he had taken hold of split the air like lightning as it swung fiercely from his fingertips.

Shwaaaargh! Boom!

A shockwave burst out with a deafening roar and shook the world. The Southern Heaven Demon Empress’s hand, which had caught the side of the spearhead with perfect precision, was filled with surging power.

Crack!

The Scorching Yang Qi surrounding the spearhead, along with the steel that a skilled blacksmith had folded and tempered more than a hundred times, crumbled like tofu.

A murderous smile formed at the corner of the Southern Heaven Demon Empress’s mouth.

*Foolish boy.*

Jin Taekyung’s mistake was that he had given up a peerless divine weapon made of Ten-Thousand-Year Cold Iron of his own accord.

From this moment on, the Southern Heaven Demon Empress intended to make that young brat pay the proper price—not only for daring to injure her beautiful body, but for cutting off her precious hair as well.

*I intended to take him back in the best condition possible. But I suppose that won’t do anymore.*

At first, after hearing that the exalted Lord of Heaven had taken an interest in Jin Taekyung, she had intended to act as the Lord’s faithful servant and capture the young man to offer him up.

But now she had changed her mind.

The Jin Taekyung reflected in the Southern Heaven Demon Empress’s eyes was no longer a sharp-tempered cat.

He was a proud beast.

Although he was young, he possessed teeth and claws as sharp as those of a great tiger.

And those were weapons that might inflict even more serious wounds on this beautiful body of hers if she made a mistake.

Jin Taekyung’s figure rushed into the Southern Heaven Demon Empress’s blood-red eyes like a flash of lightning.

*You should be prepared to lose a limb or two. I’ll reattach them later anyway.*

Muttering inwardly, the Southern Heaven Demon Empress shook both sleeves.

Papapapap!

The shattered spearhead split into dozens, then hundreds, of fragments and covered the air.

Before the wave of hidden weapons, each carrying Force, Jin Taekyung thrust out his tightly clenched fist without a moment’s hesitation.

Kraaaaaash!

The Flame-Extinguishing Divine Fist.

A fire dragon sprang from the end of his callused fist and swallowed hundreds of fragments.

The fragments, heated red-hot by the extreme temperature, melted into liquid iron and poured across the ground.

Hissssssss.

But beneath the molten iron raining down like a shower, what awaited Jin Taekyung as he shot through the air was the Southern Heaven Demon Empress’s slender, jade-like hand.

Whoosh!

Five fingers swept toward him, erasing the wind.

Curled like a rake, they swung toward his right arm.

Jin Taekyung twisted his body as though he had anticipated it from the beginning.

It was not an evasion meant to protect the right arm that would otherwise be torn away. It was a suicidal act in which he willingly offered his neck to the enemy.

But at the same time, it was also a lethal move that struck at an opening the opponent had never expected.

*What kind of lunacy is this…!*

A scream rang out in the Southern Heaven Demon Empress’s mind.

Now that the exalted Lord of Heaven had taken an interest in Jin Taekyung, he was someone who absolutely could not die.

Her original reason for capturing him had merely been an expression of loyalty to the Lord of Heaven.

If Jin Taekyung died by her hand before any particular order had been issued, she might have to bear the Lord of Heaven’s fury alone.

*No!*

Along with the cry that never escaped her mouth, the Southern Heaven Demon Empress hurriedly pulled back the internal energy that had been surging upward.

At the same time, the muscles and qi-blood throughout her body, which had moved solely toward that one purpose, twisted.

A wave of backflow overwhelmed her.

Urk!

“Kwaaaagh!”

A jet of blood surged up from deep within her body and spurted between the Southern Heaven Demon Empress’s lips.

At the final moment, the Force around her fingertips, whose direction she had barely managed to twist, veered past Jin Taekyung’s throat.

Shhk! Spit!

His skin was sliced away by wind as sharp as a blade.

But Jin Taekyung did not waver in the slightest.

No. He had no reason to waver from the beginning.

*I’ve been waiting for this moment.*

His mind, cold as ice, had already finished calculating everything.

Jin Taekyung estimated the Southern Heaven Demon Empress’s martial power to be at least that of the Ten Kings.

Perhaps she was even comparable to the Three Saints.

The level of the martial arts she used might have been equal to or even inferior to that of the Western Heaven Demon Lord, but she possessed overwhelming internal energy enough to more than make up for the difference.

And when facing a master of this level, there was only one possible method.

A single opening.

Jin Taekyung had placed his life on the table as his wager and obtained a chance that would come only once.

And…

*I’ll bet my life again.*

*Inventory Open. Summon.*

Along with the commands ringing through his mind, he thrust out his hand like a flash of lightning.

Shhk!

A slender wrist, impossible to believe belonged to such a powerful monster, was cleanly severed.

A scream burst forth.

“Aaaaaaaagh!”

It was louder and filled with more pain than the scream of any creature of the Nanman Beast Palace writhing under the demonic qi.

No—it was the loudest, most agonized scream Jin Taekyung had ever heard in his life.

In a way, it was only natural.

Humans were animals born to forget, and powerful people who had grown accustomed to inflicting pain inevitably forgot their own.

But even so, his opponent was the Southern Heaven Demon Empress.

“Jin Taekyung—!”

Shhk!

Along with her ripping cry, her body shot forward.

As Jin Taekyung met the Southern Heaven Demon Empress’s blood-red eyes, clouded with darkness, he realized on instinct.

This time, he would be unable to evade completely.

He would be unable to block completely.

Perhaps because of the massive Internal Injury she had suffered, her stance was unsteady. The internal energy she had forcibly dragged up while vomiting blood was rough beyond measure.

But that was precisely why she was more dangerous.

No.

The truly dangerous thing was the killing intent Jin Taekyung felt from the Southern Heaven Demon Empress.

“How dare you! How dare someone like you!”

Luck only came once.

A monster consumed by anger and pain, one that had even forgotten its loyalty to its master, thrust out a palm wrapped in powerful energy.

The world slowed.

A palm strike in which darkness and blood-red Force were muddled together rushed forward, erasing the space in its path.

Kraaaaaash!

It was an overwhelming force, as though a sea and a mountain had risen and come crashing down upon him.

Fear that made every hair on his body stand on end seized Jin Taekyung.

But he knew.

If he took even a single step backward here, everything would be over.

He had to move forward, even if he had to throw away his life to do it.

*Come.*

Along with the thought he muttered inwardly, though he did not know what he was calling toward him, Jin Taekyung’s foot stepped onto the blood-soaked earth.

Crush.

The ground sank beneath a single step carrying internal energy as heavy as life itself, then exploded while holding the heat within it.

Boom!

His body, crouched low enough to skim the ground, shot forward like a cannonball.

A snow-white palm filled his field of vision, carrying unprecedented energy that was impossible to believe belonged to a human.

A face distorted like a Fiend appeared within the blood-red flash as well.

“Die!”

Right then—

*Inventory Open. Summon.*

Jin Taekyung’s hand, spread wide as though it were about to unleash Palm Force, suddenly clenched.

A cold spear shaft appeared in his empty palm, and the spearhead extending from it erased the space between the two of them.

And then…

Shwaaaargh! Shhk!

The spearhead passed within a hair’s breadth of the back of the Southern Heaven Demon Empress’s neck with a harsh sound as it tore through the air.

At the same time, faint delight rose in her eyes.

*I read him. Perfectly.*

The technique Jin Taekyung used was certainly astonishing and threatening.

But amid the chaotic flow of battle, the Southern Heaven Demon Empress had accurately predicted everything.

Or so she believed.

Until the instant before she cut off Jin Taekyung’s head, when she suddenly felt a chill of wind blow from behind her.

Shhk.

“……!”

A faint sound of air being cut pierced her ears.

The Southern Heaven Demon Empress instinctively spun around.

Something as cold as ice and razor-sharp raked across her side.

Shhk!

Along with blood bursting out like a fountain, she felt her muscles and veins sever and her qi-blood become tangled.

*This… this is…*

Backflow.

A second backflow had struck before she could even settle the Internal Injury she had suffered earlier—and it was more fatal than any wound she had received until now.

*From the beginning… this was what he was aiming for.*

A flash of insight passed through her whitened field of vision.

The Southern Heaven Demon Empress swallowed the blood surging up her throat and turned around.

At last, she saw it.

Goooooong.

Blue-white flames whirled around the tip of a transparent spearhead in answer to its master’s call.

Beneath the deeply sunken eyes of one man, silently moving lips completed two words.

*One Annihilation.*

The moment the Southern Heaven Demon Empress’s eyes flew wide—

—Human!

Along with someone’s sudden, urgent thought, a massive vortex unlike anything anyone in Nanman had ever seen exploded outward.

Kraaaaaash!
## Chapter artifact 703

# Chapter 703

Kwoooooong…!

I couldn’t breathe.

The roar still hadn’t faded. It continued alongside endless reverberations, sounding impossibly distant.

And yet the System notifications continued ringing clearly in my ears.

> **System**
>
> *Beep! Beep-beep!*
>
> - **Status Effect:** Severe Internal Injury has been applied!
>
> - **Status Effect:** Severe Exhaustion has been applied!
>
> - **Status Effect:** Severe Muscle Rupture has been applied!
>
> - **Status Effect:** …

The System notifications—or rather, the warning sounds—continued without pause, methodically pointing out just how serious my condition was.

If the System had been a doctor, it would probably have looked at me with the gravest expression in the world and said:

*“Patient, I hate to tell you this, but… it looks like you’re really screwed this time. So why the hell do you keep using One Annihilation? Is dying young on your bucket list?”*

How considerate.

Just imagining it was enough to make me feel like shit, but strangely, I wasn’t experiencing much of a change in mood right now.

The reason was simpler than I expected.

A reality even shittier than anything I could imagine was waiting for me.

“Cough.”

Splatter. Drip, drip.

Blood burst from my mouth with the cough and scattered across the ground.

I’d even felt some chunks in it, so they were definitely pieces of my organs. Seeing that, I had to admit that One Annihilation was incredibly generous—

*Fuck. It wasn’t a convenience-store lunchbox.*

*Damn it.*

My vision was hazy. My senses, which had been sharp enough to rival a divine weapon only moments ago, had grown dull as an ax abandoned in a ruined cabin. White Flame, which I had always swung around like a pinwheel, had become the heaviest thing in the world.

But if there was one thing that was still relatively fine amid all this, it was the pain I could still feel in my forearm.

Crunch. Crunch.

I stared at *it* through my blurred vision.

It kept chewing on my flesh with teeth that jutted out like an animal’s, swallowing mouthfuls of blood. Its eyes were filled with nothing but greed and madness.

It was impossible to believe that it had once been human like me.

“Good?”

Crunch.

“Yeah. I guess it is.”

I didn’t know.

Why was I speaking to it when I knew perfectly well that it could no longer understand me? Why was I leaving this bastard alone while he livestreamed an eating show using my wrist?

Perhaps it was selfishness—the desire to borrow someone else’s hand.

Or perhaps it was the last shred of pity I had for something that had once been human.

Shwaaak! Slash!

Crunch…

Along with the sound of something slicing through the air, the teeth that had been chewing so ferociously went slack.

Just as I stared at the frozen young man with his red eyes wide open, a silver mane covered in blood and dust swept across my vision.

—Human. You do not appear to be all right.

The guardian spirit.

The moment I recognized its presence, the strength left my legs. I clutched its mane and answered weakly.

“Don’t people usually ask if someone’s all right first?”

—I am different from humans. Since you did not appear to be all right, I saw no reason to ask.

“I like that about you. What about that pitch-black bastard?”

—I killed him. That was the fourth time.

“What?”

—He kept getting back up. The longer time passed, the faster he recovered, and he grew stronger as well. This time may be no different.

The rift.

More precisely, it was the effect of the demonic qi flowing from the rift.

And as the Masked Man grew stronger from the demonic qi, the guardian spirit must have been growing weaker by degrees.

Just like the sacred stone in its mouth, which could no longer release the massive radiance it had possessed at the beginning.

*The guardian spirit shares its power with the sacred stone.*

Only now could I see the deep wounds scattered across the guardian spirit’s body. Its shoulders heaved with exhaustion, and its breathing was ragged.

Perhaps it noticed me looking, because it turned its massive body to hide the wounds from view.

“I’m sorry.”

At my weak words, the guardian spirit stared at me with its blue-white eyes before shaking its head.

—You did all you could.

“At the end…”

—I know. If those things had not interfered, you would have succeeded.

I looked around with exhausted eyes.

Torn corpses came into view.

They were the remains of the mutants who had completed their transformation first and rushed at me alongside the guardian spirit’s warning, just as I was about to fire One Annihilation.

*I didn’t anticipate it.*

No.

It would be more accurate to say that I hadn’t had the time to worry about it.

Unlike now, I had been in such a desperate situation that I couldn’t even look around. The mutants had charged at me with incredible ferocity.

*And then they died.*

What awaited roughly one hundred of them was the immense vortex created by One Annihilation.

But in that brief instant, split into smaller and smaller fractions of time, the mutants had instinctively stopped me and fulfilled their mission.

They had bitten into my forearm and changed the direction of my attack. They had blocked my view. They had thrown themselves in front of an enormous force that could not be stopped.

And that was how one person survived.

“Southern Heaven Demon Empress.”

At my voice, which sounded more like a groan, a figure standing tall amid the hazy cloud of dust took a step forward.

Scuff.

A section of the ground had been caught in the aftermath of One Annihilation, and everything there had been erased.

From the very center of it all, the only monster to survive emerged, her red eyes glowing.

* * *

Everything was red.

The sky. The ground. Everything in between.

At the same time, things that should never have been visible came into view.

*Ah.*

The Southern Heaven Demon Empress stared blankly down at her hand.

The smooth, snow-white hand she had gained by taking several jiazi’s worth of internal energy and vast amounts of vital essence was nowhere to be seen.

In its place was a withered hand covered in fine wrinkles and age spots, as dry and thin as the branch of a dying tree.

“Ah. Aah…”

Moisture gathered in her bloodshot eyes, stained red by ruptured capillaries.

This couldn’t be happening.

It couldn’t.

She had been more beautiful than anyone in the world. She was supposed to be beautiful.

But the grand art she had cultivated for nearly a century had been shattered, and the Southern Heaven Demon Empress had been forced to reclaim her original, old, and ugly appearance as though it were a curse.

Then, as her body trembled with distant shock and rage, she realized that the curse that had descended upon her was not merely the aging she had suppressed.

*It hurts.*

Only after examining herself in response to the sudden agony did she finally understand.

The flesh along her side had been torn away as though gnawed off by an invisible beast, and one of her arms had been blown away completely.

Half of her face had melted beneath the tremendous heat.

“……!”

The Southern Heaven Demon Empress’s eyes flew open.

It was impossible.

It was something that should never have happened.

The wound in her side could heal. Even her arm could be reattached without leaving a scar if she found a skilled enough practitioner.

But her face was different.

Unless she walked the same path as the Blood Lord, whom she despised so deeply, the face that had suffered such terrible burns would be scarred forever.

“No. This… this makes no…”

The Southern Heaven Demon Empress mumbled like a woman who had lost her mind, then suddenly stopped.

It was because of the person reflected in her blood-red eyes, now wet with tears.

Jin Taekyung.

She could see him.

She could feel him.

After the dazzling flash that had erased everything, he remained—a powerless shell of a man.

The pitiful creature that had stolen her youth and beauty.

At the same time, a single thought seized the Southern Heaven Demon Empress’s entire body.

*Kill him.*

At that moment, the mind that had been confused by countless emotions turned cold.

The monster who had lived for an age wrapped herself in darkness and moved forward without hesitation.

Scuff. Scuff.

Crack.

With every step, the energy flowing from the Southern Heaven Demon Empress’s body crushed the surrounding area.

She might have lost her youth, but she still possessed enough strength to kill him.

The blood flowing from her side and arm had already stopped, and her battered insides were slowly, but steadily, stabilizing.

If the sudden return of aging was a curse, then the demonic qi of the rift, which continued growing denser even now, was a blessing to the Southern Heaven Demon Empress.

A blessing that would allow her to tear apart Jin Taekyung, who could barely stand on his own, and the musty old beast standing in front of him.

—Stop.

Ssssss.

Along with the guardian spirit’s resonating thought, a halo of light spread from its center.

The thousand mutants packed tightly around it hunched down, but the Southern Heaven Demon Empress did not stop walking.

Bang!

A palm strike shot forward without the slightest hesitation. Darkness mixed with blood-red Force pressed down on the sacred stone’s light and engulfed Jin Taekyung.

Boom!

The ground exploded with a deafening roar.

In that instant, the guardian spirit bit Jin Taekyung by the nape and darted away like lightning, releasing a low growl.

—The sacred stone…

It swallowed the rest of its words, but the reality it had realized was cruelly clear.

Rumble…

It felt tiny tremors coming from inside its mouth.

Like an old man facing a young man in his prime, the power held by the sacred stone was diminishing even now.

And so was the strength of the White Tiger that had protected the sacred stone for ages.

*Even the spiritual energy left behind by the imugi wasn’t enough?*

The guardian spirit had never expected to fully recover all of its original strength from that alone.

Moreover, the Water God Dragon had been unable to leave behind much energy because of the effects of its previous mutation.

*The demonic qi is too strong.*

*Strong enough to suppress even the sacred stone’s power.*

The demonic qi flowing from the rift had already spread beyond the Inner Palace and begun encroaching on the Outer Palace.

The guardian spirit had brought the beasts of the Sacred Land with it, but if the beasts also fell under the demonic qi’s influence while even the sacred stone was weakening, the situation would deteriorate beyond control.

No.

It was already the worst possible situation.

Nearly a thousand mutants completely under the demonic qi’s influence surrounded them without leaving a single opening, while even the powerful Southern Heaven Demon Empress had survived to the bitter end and was now hunting them.

*If this continues…*

Just as the guardian spirit’s expression darkened at the unavoidable thought, Jin Taekyung spoke in a weak voice.

“Go.”

—What?

“You’ve worked hard. You’ve been through enough.”

—……!

As he looked into the guardian spirit’s wide blue-white eyes, Jin Taekyung used White Flame as a cane and struggled to stand.

“This is enough. Get out and save the people. Get out of this goddamn place as quickly and as far away as possible.”

—You’re saying that now…

“I guarantee it. No matter how fast you are, I won’t last long if you take me with you. I’ll probably start whining for you to put me down in less than half a shichen. I’ll die if I don’t circulate my qi.”

The guardian spirit fell silent at the playful but cold words.

Jin Taekyung continued with a crooked smile.

“So go. Before it’s too late.”

When he finished speaking, Jin Taekyung turned his head and stared at the Southern Heaven Demon Empress.

The young man’s eyes, which seemed as though they could go out at any moment, met the blood-red light burning with fury in midair.

“All right. I’ll come along quietly, so let’s stop this. Lord of Heaven or Lord of Fucking Dogs, whatever he is, let’s go see him.”

The Southern Heaven Demon Empress raised her hand instead of answering.

Swish, spit!

Finger Qi flew like a beam of light and tore into the back of his neck.

Jin Taekyung casually shrugged his shoulders.

“If you’re angry, why not say so? I’ve already lost a lot of blood. What if I die on the way?”

The Southern Heaven Demon Empress answered in a chilling voice.

“That would be troublesome.”

“Now we’re finally talking—”

“You mustn’t die this easily. I’ll tear you apart slowly with my own hands.”

“……I guess we’re not exactly communicating. What are you planning to do about the fallout?”

“It will be fine. The Lord of Heaven will be pleased if I bring him a divine artifact. The White Tiger’s pelt will be a bonus.”

The Southern Heaven Demon Empress spread her hand as she smiled brightly.

Kwoooong—!

A tremendous rumble swept across the Nanman Beast Palace.
## Chapter artifact 704

# Chapter 704

The Southern Heaven Demon Empress was certain.

She needed no more than *the time it takes to drink a cup of tea* to end this tiresome battle.

It would be the last stretch of time that brat she wanted to tear apart and that beast could remain alive and breathing.

But that unshakable certainty began to crack at the very moment she was about to unleash a palm strike.

Kwoooong—!

A tremendous rumble that had begun somewhere.

At the same time, the air rippled and the wind stopped. Sensing the powerful wave of qi coming from beyond the thick darkness, the Southern Heaven Demon Empress clenched her teeth.

*This is…!*

A master. And one powerful enough to remain free from the demonic qi’s influence.

The thought that flashed through her mind and the response that followed were both instantaneous.

Realizing that something had gone wrong, the Southern Heaven Demon Empress released the internal energy gathered in her only hand and shouted.

Not toward the direction from which she sensed the wave of qi, but toward the person whose throat she needed to cut before it was too late.

“Kill him!”

Kwooooooosh!

At that moment, it was not only an enormous palm force, tinged with murky light, that shot through the air and tore across space.

Nearly a thousand humans and beasts—mutants made even more vicious and powerful by the demonic qi—threw themselves forward in unison, shrieking.

Pap-pap. Shhhhhk!

—Krrk, kraaaah!

Teeth harder and sharper than steel glinted in the darkness.

Above the heads of the mutants charging forward with strength and speed far beyond their original physical abilities, a palm force filled with tremendous energy shot through the air like a meteor.

Toward the two figures standing amid the dense darkness beneath a hazy halo of light.

No—to tear apart the human who had inflicted an insult on the Southern Heaven Demon Empress that could never be washed away.

Yet as Jin Taekyung watched everything rushing toward him, he twisted the corner of his exhaustion-laden mouth.

“Too bad. You’re already too late.”

“……!”

That brief sentence, which had slipped from the Southern Heaven Demon Empress’s lips only one shichen earlier, came back to her in a voice full of mockery.

Boom! Fwoosh!

The dense darkness spread in every direction exploded sideways as though the demonic qi itself had detonated.

At the same time, a green Force resembling forest and vegetation burst through the gap and smashed apart everything in its path.

No.

It tore into them and devoured them with ferocity.

Like a wild beast.

Krrrunch!

The earth shook. Compressed air burst outward, and the wind mixed with bitter demonic qi was erased.

The green Force tore apart the limbs of the mutants charging in from every direction before opening its jaws toward the enormous palm force.

Kwaaang! Rumble!

Light intertwined in the collision.

After a deafening roar that made it seem as though the sky itself had split apart, a terrifying shock wave shook the surrounding space.

Beyond it, the Southern Heaven Demon Empress stared wide-eyed at her palm force as it faded away helplessly.

The capillaries in her eyes had burst.

*Mutual annihilation?*

Who was she?

She was the greatest and most exalted existence beneath heaven and earth. One of the most loyal servants who served the will of the Lord of Heaven—and a powerful figure trusted enough to be entrusted with South Heaven itself.

Even after losing a considerable amount of strength because of Jin Taekyung, she could still tear apart an ordinary Supreme Peak master in moments.

And yet mutual annihilation?

It was an unbelievable result—one she did not even want to believe—but the Southern Heaven Demon Empress was not foolish enough to deny the reality unfolding before her eyes.

Nor did she lack the judgment to infer the identity of the opponent who had appeared so suddenly.

*No doubt about it.*

That level of Fist Force. And the enormous silhouette visible through the dust cloud as it slowly settled.

A voice, cold as ice, escaped the Southern Heaven Demon Empress’s lips.

“……Yayul Cheok, the Beast Miao King.”

Boom!

The wind bursting from the sleeve the Southern Heaven Demon Empress swung aside cleared the air before her.

Amid the dispersing dust cloud, the face of a giant appeared. A half-gray beard hung from his chin like the mane of an old great tiger.

Behind his iron-tower-like frame, a young man leaned against the massive body of a White Tiger.

“You’re late. Very late.”

At Jin Taekyung’s hazy voice, the Beast Miao King opened his mouth with a calm expression.

“I am sorry. For being late.”

“I almost died out here.”

“That will not happen.”

The Beast Miao King answered quietly and thrust out his hand like a flash of lightning.

Bang.

With a sound like a drum exploding, Jin Taekyung’s body jerked.

As the guardian spirit hurriedly caught his collapsing body, instinctively baring its teeth, Jin Taekyung shook his head and opened his mouth.

“Urk. Ueeecch!”

Shwaaaaaak!

Dark red blood soaked the guardian spirit’s broad back.

Feeling the hot sensation of the stagnant blood pouring out like vomit, the guardian spirit muttered.

—What a wonderful feeling.

“……!”

—There is no need to look at me like that, large human. I—

The guardian spirit was about to continue, addressing the wide-eyed Beast Miao King, when Jin Taekyung, having vomited up the dead blood, raised himself and spoke.

His voice was far more lively than before.

“It’s not exactly the best atmosphere for introductions, but say hello first. This is Whitey. I just adopted him.”

—Adopted me? How dare you!

“Oh. So you’re okay with Whitey?”

—You bastard!

Jin Taekyung grinned as the guardian spirit forgot the situation and bristled furiously.

At that moment, the Beast Miao King abruptly swept both hands outward.

Boom!

Green Fist Force and the murky palm force collided in midair.

At the same time, the transparent spearhead that had been hanging limp moved.

Slash!

Around ten mutants that had rushed forward, seeking an opening, were sliced apart without even having time to scream.

Then another group of mutants charged toward Jin Taekyung’s back as he staggered for an instant.

They saw the enormous forepaw waiting for them.

Whoosh! Crunch!

Blood spurted like a fountain, and limbs severed from their bodies rolled across the ground.

With a low growl rumbling from its throat, the guardian spirit stood back-to-back with Jin Taekyung.

Jin raised the spearhead of White Flame and pointed in one direction.

“And that fucking bitch who interrupted while someone else was talking… You know who I mean, right?”

The Beast Miao King nodded.

His deeply sunken eyes reflected an old woman with an ugly appearance.

“Yes. The Southern Heaven Demon Empress.”

His voice seemed to boil with anger that could not be hidden.

Countless mutants still surrounded them.

Consumed by the demonic qi and stripped of their original forms, they were the tribespeople of this land whom the Beast Miao King had once cherished and loved more than anyone.

No.

Even now, his feelings for them had not changed.

The aching in one corner of his chest, which had begun the instant he saw the mutants, was proof of that.

*I had hoped I wouldn’t be too late.*

He had run until he could barely breathe. He had squeezed every last bit of strength from his body to reach this place.

And the moment he saw the Nanman Beast Palace in the distance, engulfed in darkness and flames, he had realized it.

He was already too late.

To reach this place, the Beast Miao King had crossed more than mountains and plains, rivers and valleys.

He had seen a hellscape.

The sight had brought back fragments of the horrific memories from several decades ago—the memories of the war that had been named the Great Faction War—and torn his heart apart.

The corpses of tribespeople who had been unable to evacuate were crushed beneath the debris of collapsed buildings, while the streets that had been filled with music and laughter until not long ago had been claimed by surging darkness and flames.

And at this very moment, the greatest cause of the hellscape stood at the end of the Beast Miao King’s gaze.

“I swear this as the Palace Lord of the Nanman Beast Palace.”

Flames streamed from his reddened eyes.

The man’s usual appearance—fond of alcohol and people, laughing loudly after getting thoroughly drunk—could no longer be found anywhere.

In the past, he had led ten thousand warriors north and faced the Demonic Cult’s hundred thousand demonic followers, earning the fearsome name of one of the Ten Kings.

Now, that giant continued in a chilling voice.

“I will tear your limbs apart piece by piece.”

Jin Taekyung poked his head out from behind the Beast Miao King’s broad back and added,

“Just in case it’s too much for you, I already cut off one of her arms.”

His complexion was still pale, but color was returning quickly. The hand gripping his favored weapon no longer trembled.

Jin Taekyung took a deep breath and stepped forward.

Scuff.

One step.

Yet the mutants still filling the surrounding area merely twitched. They could not bring themselves to charge recklessly.

Though their reason had been paralyzed, their instincts—heightened even further by the mutation—had noticed it.

The flow of the air had changed.

And for some reason, the master who should have been giving them orders had fallen silent.

The mutants’ instincts were close to the truth.

The Southern Heaven Demon Empress had felt a sense of crisis for the second time since coming to Nanman.

*This isn’t good…*

Under normal circumstances, she would have snorted.

Even if the Beast Miao King was one of the Ten Kings, he was still nowhere near strong enough to close the gap between them.

But this time was different.

Jin Taekyung’s One Strike had been powerful enough to freeze even the Southern Heaven Demon Empress with fear for an instant, and she had lost a considerable amount of strength along with one arm because of it.

The Beast Miao King’s appearance in such a situation was a genuine threat.

Jin Taekyung had recovered a small amount of strength with the Beast Miao King’s help, and the guardian spirit also possessed a considerable amount of qi. Neither of them was an opponent the mutants could handle.

But that was not the only reason the unease in her heart continued to grow.

*Why? Why haven’t they appeared?*

Just as the Western Heaven Demon Lord had done when he met his death in Sichuan several months earlier, the Southern Heaven Demon Empress had a considerable number of subordinates under her command.

Approximately five hundred.

It might not have been enough to call them a full unit, but they were elite soldiers who had lived in seclusion, hidden from the eyes of Nanman’s people, and were more than sufficient to prepare for any possible situation.

And yet…

*They haven’t come. Still.*

More than half a shichen had passed since the rift opened.

But the only one to appear at the appointed time had been the Masked Man.

Normally, more than half of them should have crossed over through the Moving Formation engraved on the mirror she had given Baeksang, while the remaining half should have sealed the Outer Palace’s gates from outside.

*Even if something had gone wrong with the Moving Formation, it would only make sense for them to appear somehow by now.*

At the moment the Southern Heaven Demon Empress bit down on her lips, the ground beneath her feet began to shake.

Creak. Creak-creak.

Realizing that her subordinates had finally arrived, the Southern Heaven Demon Empress wore a faint smile.

The five hundred soldiers approaching now were ones she had personally selected.

They had mastered demonic martial arts, and the demonic qi would make them even stronger than usual. No matter how many beasts remained in the Outer Palace, they would be unable to block their path.

“Tear my limbs apart piece by piece? You?”

The Southern Heaven Demon Empress let out a quiet laugh.

When she saw the now-stiff faces of Jin Taekyung and the Beast Miao King, she could not hold back her laughter.

“I admit it. You fought better than I expected. No—no one could have imagined things would turn out like this.”

*But it ends here.*

Swallowing the rest of her words, the Southern Heaven Demon Empress began walking lightly, as though nothing had happened.

And just as the taut tension began to loosen, the Beast Miao King abruptly spoke.

“There is.”

“What?”

“There is someone who foresaw that this would happen. Someone who did not let go of hope until the very end, even while walking down an irreversible path and writhing in guilt.”

Words she could not understand at all.

As the Southern Heaven Demon Empress blinked, the Beast Miao King spun around like a flash of lightning and thrust out one fist.

Kwoooooosh!

Green Force shot sharply forward, piercing the darkness and carving out a path.

And along that path came the reinforcements who would decide the ultimate outcome of the battle.

Thud-thud-thud-thud!

A group of people armed in pure white clothing and armor.

The man at their head bowed toward the Beast Miao King.

“Wang Ho, Commander of the Baekcheon Unit… pays his respects to the Palace Lord.”

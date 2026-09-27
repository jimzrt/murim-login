# Checkpoint Review — 1180–1184

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

# Chapters 1180–1184

## Plot

As the allied forces approach the Tianshan Mountains, Jin Wikyung and Jin Mukyung face a vast monster horde with the Jin Family of Taiyuan. Mae Jonghak and other Murim leaders join the battle. Elsewhere, the Son of Heaven fights alongside the Imperial Guards, Baek Yeon, and Jeong Hogun; he summons the Twelve Palaces against at least twenty Black Ghosts. The battles’ outcomes remain unknown.

Jin Taekyung’s group reaches the rendezvous point, but the Murim Alliance and Imperial Guards do not arrive by the agreed deadline. Jeok Cheongang announces that they will advance without waiting and reveals that Taekyung was secretly designated the main attack against Dark Heaven. Taekyung refuses to leave his missing companions behind and tries to turn back. The Slaughter Saint incapacitates him with a specially made medicine, and Jeok catches him as he collapses while the Bow Saint blocks his escape.

## Continuity

- The allied forces split into three groups near the Qinghai-Xinjiang border to rendezvous near Tianshan. The Murim Alliance and Imperial Guards missed the deadline; the whereabouts of the separated companions and more than one hundred thousand troops are unknown.
- Jeok Cheongang’s group intends to advance toward the Lord of Heaven without waiting. Taekyung is their concealed main attack; the Sword Saint, Emperor, and gathered allies agreed to keep the plan from him.
- Taekyung tried to turn back at least half a day to search for his companions. He is incapacitated and in Jeok Cheongang’s arms.
- Taekyung has unexplained chest pain and difficulty sleeping.
- The Lord of Heaven has awakened and regained strength, but says the process is incomplete. The Grand Mage awaits his command.
- The Main Quest “Rift and Collapse” failed; “The Foreordained Collapse” warns that player choices can cause irreversible consequences. Cheon Taemin remains unconscious in a secret facility beneath the Pentagon. An alert reported Alpha’s awakening; what Alpha is remains unknown.

## Translation Decisions

- Use **Great Sir** for 대인, **Dark Heaven** for 암천, **Lord of Heaven** for 천주, **the Adversary** for 대적자, and **fasting pills** for 벽곡단.
- Use **Black Ghosts** as the plural of **Black Ghost**.
- Render 일각 as **fifteen minutes** and 주공 as **main attack**.

## Durable state

{
  "active_continuity": [
    "The Murim allied forces split into three forces near the Qinghai-Xinjiang border, intending to rendezvous with the Imperial Army near Tianshan.",
    "Taekyung’s group reached the rendezvous, but the Murim Alliance and Imperial Guards missed the agreed deadline.",
    "Taekyung was secretly designated the main attack against Dark Heaven; the Sword Saint, Emperor, and gathered allies agreed to conceal this plan from him.",
    "Taekyung decided to turn back at least half a day to search for his missing companions, but the Slaughter Saint’s medicine and the Bow Saint’s intervention stopped him; he collapsed into Jeok Cheongang’s arms.",
    "The fate of the separated companions and the more than one hundred thousand allied troops is unknown.",
    "Taekyung experiences unexplained chest pain and difficulty sleeping.",
    "The Lord of Heaven has awakened and regained strength, but says the process is incomplete; the Grand Mage awaits a command.",
    "The Main Quest “Rift and Collapse” failed; “The Foreordained Collapse” warns that player choices can cause irreversible consequences.",
    "Cheon Taemin remains unconscious in a secret facility beneath the Pentagon; Jin knows he is the Martial God and a former Player.",
    "An alert reported Alpha’s awakening; what Alpha is and what its awakening means remain unknown."
  ],
  "continuity_sources": [
    1184,
    1183
  ],
  "open_questions": [
    "What happened to the separated companions and allied troops?",
    "Why did the Murim Alliance and Imperial Guards miss the rendezvous?",
    "What caused Taekyung’s chest pain and sleeplessness?",
    "What remains to be completed for the Lord of Heaven, and what command will he give the Grand Mage?",
    "What is Alpha, and what does its awakening mean?"
  ],
  "safe_through": 1184,
  "temporary_decisions": [
    "Render 대인 as Great Sir, following the established glossary."
  ],
  "version": 1
}

## Reading copies

## Chapter artifact 1180

# Chapter 1180

Great Sir’s final mutterings, heard only by the desert and the darkness, had been half right and half wrong.

As the dusky dawn mist receded and the first light began to spread, the sky unleashed a downpour with all its might, as if it had been waiting for this moment.

Not over the parched desert, but toward the western plateau.

*Whoooosh!*

Torrential rain poured down. Before the fierce wind and rain, people pulled their collars tight and lowered their rain capes over their heads. The beasts carrying them let out weary cries.

“It’s coming down like crazy. At this rate, forget the people—the horses won’t hold out.”

At the deep voice from beneath an oil-treated bamboo hat, the young man riding slowly at his right spoke up.

“We’re lucky they’ve held out this long. We’ll be clear of this wretched plateau in half a day, so we have no choice but to hang on a little longer.”

Wretched.

The man in the bamboo hat couldn’t help agreeing with the young man’s choice of words.

In fact, he was certain that not only he, but tens of thousands of martial artists trudging forward at that very moment, felt the same way.

“Yes. It’s been a hard road.”

The man in the bamboo hat muttered to himself and remembered what he’d seen on the way here.

Dry riverbeds and dead forests.

Villages and cities—proof that people had once lived there, yet so desolate it was hard to believe anyone ever had.

Every well was foul. They’d searched the surroundings thoroughly, but found no people—not even the carcass of a common gnat.

As if nothing had ever lived there at all.

*What on earth happened here?*

The man in the bamboo hat thought again of the question that had long gone unanswered. But he already knew that no matter how deeply he pondered it, he’d only be wasting his mental strength.

If he could have figured it out on his own, then the white-haired old man approaching now with a nod of greeting would surely have done so as well.

“Great Hero Song.”

At the man’s respectful salute, Song Ho, the Thousand-Faced Fox, smiled.

“Family Head Jin, you’re being so formal that this old man hardly knows where to put himself. Just call me Chief.”

The man in the bamboo hat—no, Jin Wikyung—shook his head awkwardly.

“Compared to you, I’m still a junior by a long way. Besides, I’m only the Lesser Family Head acting in the Family Head’s place.”

“I know that, of course. But these are precisely the times when a family’s unity matters most. And the Family Head of the Jin Family of Taiyuan…”

“He’s away. Still.”

At the young man’s abrupt interruption, Jin Wikyung clicked his tongue.

“Little brother.”

The second young master of the Jin Family of Taiyuan, the Heaven Shaking Sword, Jin Mukyung, replied, “Who’s your little brother?”

“…Fine. Commander of the Heaven Shaking Squad.”

“Give your order.”

“Pick some men and search the surrounding area. No—Commander, please see to it. I need to speak privately with Great Hero Song.”

“Commander Jin Mukyung acknowledges the Family Head’s orders.”

“You…”

“Then I’ll be off.”

Without giving Jin Wikyung a chance to say another word, Jin Mukyung answered as casually as could be and disappeared into the rain, his long robe whipping behind him.

“Whew. That boy…”

At Jin Wikyung’s sigh, the Thousand-Faced Fox let out a quiet chuckle.

“Don’t be too hard on him. From what I’ve heard, it’s good to see that the brothers are so close.”

“No, my younger brother needs a good scolding. He has no manners at all. Interrupting an elder while he’s speaking.”

“Don’t mind me. I’m quite all rig—”

“And he didn’t even bring an umbrella.”

“Pardon?”

“It’s pouring like this! I told him several times to use one, and he didn’t even listen! He didn’t even wear a bamboo hat!”

“…”

“I know he’s not going to lose his hair right this instant, but what if he catches a cold? What then, hm? Am I wrong?”

At Jin Wikyung’s sudden outburst, the Thousand-Faced Fox fell silent for a moment before replying.

“You really are… close. Closer than I’d heard.”

“When my younger brothers were little, they were frail. Taekyung must be having a hard time now, too. I worry whether he’s taking good care of himself.”

By this point, even the Thousand-Faced Fox was beginning to worry.

He was starting to wonder whether there was something wrong with Jin Wikyung’s mind.

Who was the Heaven Shaking Sword, Jin Mukyung?

Since childhood, he’d been counted among the finest rising martial artists in Murim on the strength of his extraordinary talent alone. And after One-Ride Heavenly Dragon Murong Yeonghwi vanished with the downfall of his family, no one had denied Mukyung his place at the head of the Ten Dragons and Phoenixes.

To be precise, he’d long since surpassed the level of a rising martial artist.

In the recent Battle of Eight Spring Gorge, which decided the fate of the entire northern region, that young Sword Demon of the Jin Family of Taiyuan had defeated the Blood Soul Fat Demon, a great fiend of the previous generation, announcing the birth of a new Supreme Peak master to the world.

And yet Jin Wikyung was worried he’d catch a cold.

When he’d even brought up the monster among monsters, Jin Taekyung, the Thousand-Faced Fox had nearly been too dumbfounded to speak.

*Is he joking right now?*

The Thousand-Faced Fox briefly wondered whether he ought to laugh. Then, with the practiced skill of the Chief of the Hidden Shadow Pavilion, he kept his expression in check.

“Young Hero Jin is doing well. Even if he’s run into a little trouble, I’m sure it’s nothing serious.”

“That part doesn’t worry me at all.”

Jin Wikyung, who doted on his two younger brothers—and especially his youngest, who’d long been his sore spot—agreed with heartfelt sincerity for once.

The force they’d sent was tiny, given the terrain and the need for speed. But it included no fewer than six Supreme Peak masters, an elite force by any measure.

Three of them were hardly inferior to Mae Jonghak, the current Alliance Leader of Murim. Even if a major threat arose, each of them should be more than capable of protecting himself.

If Jin Wikyung had one concern, it was a single person.

*The Big Man, was it?*

He’d heard the rumors.

The appearance of a new Supreme Peak master always drew the world’s attention, and that was no different even as Dark Heaven’s schemes shook the land.

If anything, the interest was greater.

A mysterious master who’d appeared in such troubled times, with wild hair and half his mind seemingly somewhere else?

A chivalrous hero who’d single-handedly crushed the mounted bandits running rampant in Gansu more than a decade ago?

That was all it took.

The martial world’s gossips couldn’t resist. They talked about the Big Man until their mouths were dry, and rumors about him spread across the land.

*But rumors aren’t worth much in the end.*

As the man responsible for leading a family, Jin Wikyung was cautious in all things—and when it came to his younger brothers’ safety, he was practically allergic to risk.

So of course he’d decided to meet the suspicious eccentric who’d joined his youngest brother’s group himself.

Though, in the end, he’d failed.

*I wish I’d had a little more time.*

The Big Man was like a wind blowing across the Great Steppe.

Jin Wikyung had seen him only briefly, standing beside Jin Taekyung atop the city wall. After that, he was always vanishing somewhere, then suddenly turning up somewhere else.

If the Big Man had ever gone missing for a while, Jin Wikyung might have seriously suspected he was a spy. But after conducting a fairly thorough investigation, he’d found that wasn’t the case.

The Big Man made his presence known to the whole world with his booming shouts of nonsense and his foul stench.

Just before the army set out, Jin Wikyung had been so busy he could barely find a moment to visit his quarters. The Big Man had been elsewhere, drinking with the Beggars’ Sect Leader and being invited to join the sect. When even that hadn’t worked out, he’d sent Jin Mukyung and other family members in his place, only to find the Big Man hiding with Cheongpung in the military supply warehouse, looking for snacks.

And most people liked the Big Man.

Even his youngest brother, whom Jin Wikyung thought just as finicky as his master, liked him.

“The Big Man? I don’t know him that well, but from what I’ve seen, he seems like a good person.”

“Come now, youngest! How many times have I told you to be careful around people you don’t know—”

“I’ve been watching him since Gansu, and, well, I’ve thought it over from every angle. I’ve got a good feeling about him. Like I do about you, hyung.”

“…Like me?”

“Don’t make that face. Of course I like you more, hyung. There’s no comparison.”

“Oh, right.”

“Of course. But, hyung, would you like some candy? Cheongpung left it behind.”

“Hm? Sure!”

That was the last time.

Time was pressing; a quarter hour felt like three autumns. Jin Wikyung grew busier still, while the Big Man continued darting all over the place like the wind.

And before long, the unprecedented combined army of the government and Murim split into three forces at the border between Qinghai and Xinjiang.

Two like enormous waves, and one like a sharp awl.

“…The candy was good.”

Jin Wikyung found himself murmuring aloud. Then he noticed someone’s hot gaze on his cheek and straightened his expression.

“Ah, pardon me. I was deep in thought about where the Imperial Army might be by now.”

At that remarkably shameless answer, Song Ho fell silent for a moment.

He was old, and even missing a leg, but he still had both ears, and his hearing was as sharp as ever.

He wanted to ask what candy Jin Wikyung had been enjoying so much, but the Thousand-Faced Fox once again put his years of experience to work and answered as calmly as he could.

“If all has gone according to plan, they crossed Lop Nur fifteen days ago and should be reaching Hejing about now.”

“Then…”

“Yes. The Tianshan Mountains are close. There may be a slight difference of a day or so, but they should be able to meet us at the foot of the range before sunset the day after tomorrow.”

“…”

Tianshan Mountains.

The moment he heard the name, Jin Wikyung felt his hand tighten around the reins.

Tianshan, a giant of earth reaching closer to the heavens than any other.

The lair of darkness, an unfathomable demon-slaying battleground that had poured forth countless evils over a thousand years, yet whose depths remained impossible to gauge.

*But at last.*

They had arrived. At the end of this long journey, *he* was waiting.

But before Jin Wikyung could calm the shiver of awe and fear that thought sent through him, a familiar voice rang out in the distance.

“Hyung!”

Jin Mukyung. It was him.

Jin Wikyung’s eyes widened as his younger brother came hurtling toward him like an arrow, using his lightness skill. Where had he left the horse he’d treated like an extension of himself until now?

And then Jin Wikyung saw it.

A strange landscape spread behind Jin Mukyung’s approaching shoulder.

*A mountain range?*

A natural formation that even the deep darkness couldn’t hide.

It loomed vast and immense beyond the driving rain.

*Is that Tianshan? The one I’ve heard so much about?*

But why?

Why was his heart pounding so hard? Why did Jin Mukyung’s voice sound so urgent?

The next moment, Jin Wikyung understood.

Or rather, a single enormous bolt of lightning, slashing down through the distant sky, showed him.

*Rumble!*

As the thunder boomed and a flash of light flared for an instant, the roars of countless monsters rang out.
## Chapter artifact 1181

# Chapter 1181

For a brief moment, it was as if the world had stopped.

Eyes wide with shock. Lips hanging open in a daze.

At the end of countless gazes, a wave of calamity poured over the distant, winding hills of the plateau, blackening them beneath its tide.

*Graaah!*

A deep rumble, as if rising from the depths of an abyss.

The vast shadow everyone had believed to be a mountain roared—the countless monsters crouched within it.

The earth shook. Torrential rain burst from the sky. They planted a chill in their enemies even deeper than the cold air of the plateau that touched the heavens.

And the name of that chill was fear.

*Rumble, rumble, rumble!*

Frozen in place, people stared at the unbelievable sight.

Tens of thousands. Perhaps hundreds of thousands.

An unfathomable number of monsters charged forward, their eyes gleaming red.

Some had human faces and the limbs of tigers. Others had bodies larger than pavilions, with dozens of faces hanging from them. One shadow even spread wings unmistakably like an eagle’s and swept across the sky.

“…Primordial Heavenly Venerable.”

The dazed mutter that slipped from one Daoist’s lips spoke for everyone.

Anyone who’d glimpsed the enemy in that flash of lightning couldn’t help but think of the gods.

They didn’t know the exact name or form of that mighty being who must exist somewhere among the clouds and stars. What did such a trivial detail matter?

The moment you long for light most desperately is when you’re trapped in pitch darkness.

Just like now.

*So this was it…!*

Jin Wikyung gritted his teeth.

The ruined city. The absence of any trace of life.

The answers to every question he’d asked came rushing toward them, hundreds of zhang away, so clear and horrifying that they became reality.

Straight toward the Murim allied forces’ vanguard. Straight toward where they stood.

“Great Hero Song.”

The meaning in the quiet call was clear. Song Ho, the Thousand-Faced Fox, nodded and hurled a small cylinder with all his might. No one knew when he’d taken it from inside his robes.

*Boom!*

A signal firework made by the artisans of the Sichuan Tang Clan burst in a dazzling explosion.

Through the sparks drifting slowly down and painting the sky, the hideous monsters appeared once more.

Yet the light was bright enough to reach the rear of the army, more than ten li away, and the fierce blast briefly washed away the people’s fear.

Jin Wikyung knew what he had to do now.

*We have to buy time until reinforcements arrive.*

Even the tightest net loosens as time goes by.

The Murim allied forces had set out with enough momentum to bring down Tianshan in a single stroke. But after a month of nonstop advance with no chance to catch their breath, the people were already exhausted. The barren land and lack of food had pushed them to their limits.

Their fatigue had naturally piled up, and their march—once as steady as an unobstructed river—had begun to falter.

It was a terrible stroke of misfortune that this happened when the Jin Family of Taiyuan, one of the weaker forces in the alliance, had taken the vanguard for a short time. But the fact that Jin Wikyung was leading them was one small piece of good fortune amid the bad.

Though his martial arts weren’t on the same level as his two younger brothers’, he was a leader everyone acknowledged.

“I, Jin Wikyung, Lesser Family Head of the Jin Family of Taiyuan, ask you this!”

His shout, infused with Peak internal energy, shook the plateau. His blazing eyes poured fire.

“What are you so afraid of!”

The people who’d instinctively started to retreat stopped in their tracks.

But that alone wouldn’t overcome all the fear gripping them. Facing the gazes turned toward him, Jin Wikyung shouted again.

“What did you come here for!”

The halted feet began moving forward again. Trembling fingers closed around sword hilts.

They all knew the answer.

For the world. For the greater cause.

To protect what they held dear, or to avenge what they’d already lost.

That was why they’d stood beneath one banner and prepared to face death.

“Neither I nor any of you came here as martial artists!”

The ground trembled harder. Jin Wikyung’s voice rang out with rising force.

“We stand here as human beings! As someone’s children, as someone’s parents, here to protect what’s ours!”

The frightened horses snorted fiercely. Faces muddled by exhaustion of body and mind came into view.

And yet—

Even so—

“Face them with your heads held high! If you can’t cast off your fear, then cut it down along with the enemy!”

*Clang, clang, clang!*

As if breaking chains that had bound their wrists, they drew their weapons.

Together, they pointed them toward the wave of monsters, now less than a hundred zhang away.

Their breath came fast, white puffs spilling from their mouths.

Their mouths felt gritty, as if they’d chewed a handful of sand. Their hearts hammered as though they might burst at any moment.

But now, not a single person retreated.

Even as the horses that couldn’t overcome their fear broke free of their masters and bolted in every direction.

Even as the hundred zhang between them shrank by half, then half again.

Even when a giant monster, its height level with the pavilions of a great city, uprooted a massive boulder that had lain deep in the plateau and hurled it at them.

*Whoooosh!*

For an instant, the rain stopped.

No—in truth, a great boulder high in the air had blocked the rain falling over their heads.

“Ah…!”

As someone let out a cry, Jin Wikyung’s tightly closed lips parted.

“Little brother.”

*Shing!*

A ray of blue, bluer than a cloudless sky, shot upward.

It was quiet, and it was sharp.

Raindrops, wind, air—

Even a boulder weighing a thousand geun, holding centuries of history, was cut through in an instant without a sound.

*Slice!*

A flash like lightning blazed—and that was all.

**Blue Wave, Falling Bird.**

The blue wave that overflowed from one man’s sword split the enormous boulder—not a bird—into dozens of pieces and sent them tumbling down the hill.

*Rumble!*

Through the torrential rain, too heavy for even a cloud of dust to rise, the young Sword Demon of the Jin Family of Taiyuan had finally shaken off the monsters’ pursuit and returned. He muttered under his breath,

“I told you I’m the Commander of the Heaven Shaking Squad.”

Jin Wikyung smiled faintly.

“I thought you called me ‘hyungnim’ a moment ago.”

“…You must have imagined it.”

“Oh dear. I must have misheard.”

Jin Wikyung answered gently, as if soothing a child, and handed him a bamboo hat.

“Put it on. You’ll catch a cold.”

With a small sigh at his older brother’s tone, Jin Mukyung accepted the hat.

He tied the chin strap of the oil-treated bamboo hat tight. The fierce raindrops no longer obscured his vision.

But why did the world look so pitch-black now that he could see it clearly?

*Rumble!*

The earth shuddered beneath the darkness pouring in from every direction.

The monsters’ momentum hadn’t diminished. Staring at the countless creatures charging ahead without hesitation, Jin Mukyung tightened his grip on his sword hilt.

His breathing was steady, his gaze composed.

There wasn’t a trace of fear in him.

Not because he was confident he’d win this battle.

He simply had a reason to fight—and believed in that reason. That was why he didn’t waver.

*That’s right. I believe in him. And so does everyone else.*

Jin Mukyung thought of one person.

His younger brother, whose whole life had changed overnight—and who had then changed everything around him.

He wasn’t here, but that was a good thing.

The more monsters filled the view before them, the smaller the threat to Jin Taekyung would be.

*That guy, at least, has to survive to the end.*

Jin Mukyung took a deep breath, stepped out of the tightly formed defensive formation, and walked forward.

That single step was the last distance between humans and monsters.

*Whoooosh!*

A monster’s enormous fist plunged down with a fierce burst of air. Its horrible stench seeped deep into his nose, but he didn’t care.

Whatever the outcome of this battle, by the time it was over, the stench of blood would blanket the entire plateau—worse than anything he smelled now.

*Shhhhh.*

Blue Wave.

True to its name, a blue wave of Force surged up once again.

It silently carved apart the fist bearing down on them, swallowing the monsters at the front whole.

*Crunch!*

Severed limbs and blood sprayed in every direction.

The monsters, no longer human or beast, collapsed with mournful final cries.

But why?

The stench rising from their rotting bodies wasn’t as foul as the one Jin Mukyung had smelled before. And a new light was layered over the blue Sword Force that blazed through the surroundings, illuminating and tearing through everything in its path.

Like the sunset, gently coloring the world as the sun slowly sank.

Or like a flower petal surrendering itself to a breeze from nowhere.

*Ah.*

With a cry echoing in his heart, Jin Mukyung understood what this strange yet warm power was.

He also understood who had given rise to that purple Force, which had slipped quietly onto the battlefield like a passing breeze.

*Swish.*

The hem of a robe fluttered in midair.

No one had noticed exactly when he appeared, or how he’d moved.

Not even Jin Mukyung.

All that remained was the rich scent of plum blossoms, lingering at the tip of his nose and erasing even the monsters’ stench.

“Good. I’m not too late.”

Having reached the pinnacle of the sword long ago, he was the Number One Sword Under Heaven. With no one beneath this vast sky who could compare to him, he was the brightest star above the clouds.

The Sword Saint, Mae Jonghak, spoke, his eyes sinking deep.

“Then let’s begin.”

At that moment—

*Fwoosh!*

Above the purple plum blossoms that finally bloomed and scattered, the leaders of the Nine Sects and One Gang and the heads of the Five Great Families plunged down like meteors, led by four of the Ten Kings.

*Boom!*

Deep darkness and dazzling beams of light began tearing into each other with all their might.
## Chapter artifact 1182

# Chapter 1182

The thick mist of blood spreading in every direction wasn’t found only on the plateau west of the desert.

The brutal scene unfolding in a basin a thousand li to the east was no different.

No—it was all too similar.

*Crack!*

The battle was fierce.

And desperate.

Through the torrential rain, heavy enough to obscure the field, blood and chunks of flesh flew—no one could tell whose. Long, razor-sharp claws like scythes and finely honed spears and blades rushed at one another.

*Clang!*

Sparks flew. Monsters twice the size of grown men charged with furious roars.

*Graaah!*

Arms and legs thick as logs. Three or four heads hanging from rotting bodies.

Their grotesque appearance inspired a primal fear, chilling the spine at a glance. But the low, deep sound that rang out the next moment snapped them back to their senses.

*Boom. Boom. Boom.*

A war drum.

Dozens of strongmen poured all their strength into its thunderous beat, shaking the vast basin.

It thawed frozen hands and feet and breathed life into courage that had begun to fade.

“Defend!”

At the forceful shout, a flag flapped in the rain.

The tens of thousands of troops moved as one.

The monsters’ claws tore into iron-plated shields instead of human flesh and bone. Spearmen arranged in a bristling formation thrust their long spears, each a zhang from end to end.

*Crack! Splurt!*

Fountains of blood erupted here and there.

But it wasn’t only the enemy’s blood.

Many monsters remained unmarked even by the sharpened spearheads. They smashed through the shield wall in their path and leaped into the gaps in the broken ranks.

*Whoosh! Boom!*

Clods of earth burst into the air.

Bodies that had been full of strength a moment ago were flung away as mere chunks of flesh. Those who witnessed the unreal sight remembered the fear they’d briefly forgotten.

And right then—

*Shing!*

Dozens of streaks of light plunged down from the sky, blocking the monsters’ endless charge.

No.

They cut them down.

*Slice! Splatter!*

The soldiers at the front, who’d only just escaped death, stared wide-eyed at the green blood spreading like mist.

More precisely, at the shadows descending over the monsters’ mangled corpses.

At the golden armor shining almost unnaturally bright—and at the man standing tall in the midst of those Embroidered Uniform Guards.

“Your Majesty!”

They cried out, unable to hide their loyalty and reverence.

They called to the sole ruler of the Nine Provinces and Eight Wastes, the Four Seas and Five Lakes, the father who governed all under heaven in accordance with the will of Heaven.

And the Son of Heaven of the Great Ming Empire, Zhu Di, answered their call.

In the most effective way possible for this urgent moment.

*Thud!*

The monster’s body shuddered. Its wings, unmistakably those of a hawk, were folded tight as it plunged from the sky like a bolt of lightning.

“How dare you charge at me?”

The Son of Heaven spoke with astonishing calm as he twisted the sword buried deep between the monster’s brows.

“But you, too, were once one of my people.”

*Crack.*

“Rest in peace.”

With one final, wet crunch, the monster stopped moving. The tens of thousands of Imperial Guards watching felt something hot rise from deep in their bellies.

Who was the Son of Heaven?

Their lord. The master of the continent.

And yet this supreme being, someone they scarcely dared look up to, was fighting alongside them.

Shoulder to shoulder, drenched in the enemy’s blood.

Someone else might scoff and ask if that was all it took. But to them, it was everything.

Everything they needed to be willing to give their lives.

“Long live Your Majesty!”

“Long live the Great Ming Empire!”

Hundreds became thousands, then thousands became tens of thousands. At last, one unified roar rose up as the Imperial Army charged.

The Son of Heaven watched them go in silence.

Until a young officer guarding him nearby spoke.

“Your Majesty, may this humble officer dare to say something?”

The Son of Heaven shook his head.

“Denied.”

The answer came without a moment’s hesitation.

But the young officer didn’t back down.

“Please return. It’s dangerous here.”

“Did you not hear what I said?”

“I heard you clearly.”

“Then how do you intend to answer for this crime?”

“I will accept any punishment. But I beg Your Majesty to preserve your sacred person first, and carry out the sentence afterward.”

The young officer’s manner was respectful yet unflinching. The Son of Heaven let out a quiet laugh.

“A mere Thousand Captain of the Embroidered Uniform Guard dares to defy my word. The laws of the imperial house must have fallen into disarray. Wouldn’t you agree?”

A middle-aged man who had appeared out of nowhere spoke up.

“Wouldn’t it be a hundred times better for the laws of the imperial house to fall into disarray than for the imperial house itself to fall?”

It was a disrespectful answer that could have seen him branded a traitor on the spot. Yet the Son of Heaven didn’t so much as raise an eyebrow.

The middle-aged man holding a silver crescent-bladed halberd was the most loyal subject in the world when it came to protecting the imperial house.

“You came, Baek Yeon.”

Baek Yeon, Commander of the Embroidered Uniform Guard, gave a simple military salute and corrected the Son of Heaven’s earlier words.

“I had no choice.”

“How strange. No one called for you—not even me.”

“Then why is Your Majesty, who ought to be in the safe rear, here?”

“For the same reason you came here of your own accord.”

Baek Yeon paused, then gave a dry laugh.

“You’ve turned a foolish question into a wise answer. I have nothing more to say.”

Yes. It had been a foolish question.

Just as Baek Yeon had come here to protect the Son of Heaven, the Son of Heaven had moved to protect the people who followed him.

Not for some grand cause, but out of compassion for his people.

*Compassion. Compassion…*

It was a word he hadn’t thought of in a long time.

The Empire’s fourth prince, who’d once raced across battlefields on the strength of his burning blood and innate military talent, had disappeared after the dark shadow of Dark Heaven fell over the imperial house.

The Son of Heaven had to be cold. He had to be heartless. He’d believed that was the right course—the only key that could solve every problem.

At least, until a few months ago, when he met one man.

*Jin Taekyung.*

He was utterly free-spirited.

No matter what stood in his way, he simply pushed forward with all his strength.

Was it because he was brave?

Wrong.

He felt fear and pain just like everyone else—perhaps even more than they did. But he pressed on because he believed it was the compassionate thing to do.

The path Jin Taekyung walked was narrow, but straight.

And in the end, it had reached everyone. It had led countless people all the way here.

“He’s better than I am. Enough to make me ashamed to be the Son of Heaven.”

With that mutter—one that would have sent the court into an uproar had the civil and military officials heard it—the Son of Heaven raised the sword he’d let hang at his side.

Then he turned to the young Embroidered Uniform Guard officer who’d tried to stop him.

“Has your resolve still not changed?”

The officer replied in a steady voice.

“With all due respect, no.”

“Very well. I will withdraw in accordance with your wishes, at once. In return, you are not to leave my side for even a moment.”

The officer faltered at the unexpected words. The Son of Heaven added, his voice strong,

“But the direction we withdraw will be forward—not back.”

“Your Majesty.”

“I am the Son of Heaven. The father of all the people. A father never turns away from his children when they’re bleeding. That is the will of Heaven.”

“……”

“I ask you again. Has your resolve still not changed?”

After a moment’s silence, the young officer went down on one knee.

“I, Jeong Hogun, Thousand Captain of the Embroidered Uniform Guard, receive the command of Your Majesty, the august Emperor.”

“Follow me. We’ll open a path.”

“As you command!”

Jeong Hogun wasn’t the only one to answer.

The thousand Embroidered Uniform Guards who had now closed ranks around the Son of Heaven let out one mighty roar, and the battlefield shook.

Their cry swept over the heads of the Imperial Guards, whose lines were rapidly collapsing under the overwhelming odds, and reached even the true enemy lying in wait beyond them.

A dull thud rang out with each movement of the pitch-black armor that reflected no light.

Red eyes glowed beneath deeply lowered helmets. From the mouths visible below them came the stench of the dead.

“Black Ghosts…!”

Each one of them was a true monster, no different from a Supreme Peak master.

When countless eyes began to tremble at the sight of no fewer than twenty of them, a thunderous cry burst from the Son of Heaven’s lips.

“I command the Twelve Palaces!”

At that very moment—

*Crack!*

More than ten streaks of light shot up from across the battlefield.

Twelve men and women reached the Son of Heaven in an instant, crushing the monsters that stood in their way. They bowed deeply before him.

The pillars and stars that upheld and illuminated the imperial house: the Twelve Palaces of the Zodiac.

After the bloodshed in the imperial palace, these Supreme Peak masters had been newly organized under the Son of Heaven’s command as a force directly under the imperial house. Their eyes shone brightly as they looked to their lord.

“Give your command.”

The Son of Heaven took a deep breath.

When this battle was over, how many of them would still be alive?

No—could anyone even dare to predict victory against enemies so terrifyingly powerful?

*What would the old me have done?*

The Son of Heaven already knew the answer to the question that had suddenly come to mind.

He would have retreated without hesitation.

Even if that meant sending tens of thousands of Imperial Guards to their deaths.

But the actions of one man had changed more than just this world.

The Son of Heaven had been reborn, too.

Though he’d taken up the Maoshan Sect’s martial arts and his body was now no different from a dead man’s, his heart and blood burned hotter than ever.

Just like everyone gathered here.

Just like the man who’d awakened him once again: Jin Taekyung.

And if that man were here, he would surely say this:

“Wipe them all out.”

Feeling a freedom all the clearer for its utter lack of decorum, the Son of Heaven raced across the blood-soaked earth.

*Whoooosh!*

A brilliant golden wave stretched long behind him, like the tail of a meteor.

* * *

Jin Taekyung suddenly raised his head.

Two streaks of light had just passed across the sky, now black with night.

*A meteor?*

It wasn’t exactly common, but it wasn’t all that rare, either.

And yet, why?

Jin Taekyung pressed down on his throbbing chest.

For a long time, he couldn’t manage a proper night’s sleep.

Not after night gave way to dawn and the first light appeared. Not after he and his companions finally left that damned desert behind.

Not even after they passed through mountains and fields blanketed in perennial snow, and reached the place where all the allied forces were supposed to rendezvous.

No one came.

A day passed, then another.
## Chapter artifact 1183

# Chapter 1183

It was a nameless ruin.

Judging by its area and the number of buildings, it had once been a small city where several thousand households lived together. But, as everyone had expected, not a single person could be found anywhere.

Only the mountain range stretching without end along the distant horizon remained, watching over the ghost town.

A giant of nature with a crown of snow that never melted, white in every season, pressed down like a bamboo hat: the Tianshan Mountains.

*The mountains of heaven, huh.*

Muttering to myself, I gazed through the window at the vast landscape.

Overwhelming. Almost awe-inspiring.

It was a sight that could only be called Tianshan.

The peaks rose through the clouds. They were so high that I could almost imagine immortals dwelling somewhere up there.

No, that wasn’t an absurd fantasy at all.

Just replace *immortal* with *Demon King*, and fantasy became reality.

A very horrifying reality, at that.

“Captain?”

A voice suddenly pierced my ear.

Plenty of people called me their benefactor. Only one called me Captain.

Keeping my eyes on the view outside, I answered.

“Yeah.”

Maybe it was because my thoughts were tangled like a ball of string. My voice came out subdued, and Hyuk Mujin hesitantly opened his mouth.

“Um, have you eaten?”

“Sort of. Why?”

“Slau—no, Great Hero Mungyeong told me to stop by if I had a chance. He wanted to make sure you weren’t skipping meals.”

“That guy? That’s unusual.”

It was a little surprising.

We’d spent a fair amount of time together and grown close, but I hadn’t thought he was the sort to worry about whether I’d eaten.

“He said it’s a special batch of fasting pills he made before we set out, just in case. We’re already running low on food, and he said he’d kill you if you left any.”

“…Yeah, that sounds about right.”

I shook my head and took the fasting pill I’d tucked away in my clothes. Hyuk Mujin’s eyes turned cold.

“You said you ate.”

“I said I sort of did. I didn’t say I ate.”

“Honestly. I knew it.”

Maybe he was acting up because he hadn’t been hit enough lately.

Ignoring his grumbling, I popped the fasting pill into my mouth.

I chewed and swallowed, enduring its utterly inexplicable bitterness. A surprising fullness spread through me, and a System notification rang out.

*Ding.*

> **System**
>
> You have consumed Mungyeong’s Special Fasting Pill.
>
> Fullness will be maintained for one day.
>
> A small amount of fatigue has been recovered.
>
> All stats increase by +3 for one hour.

It tasted like shit, but its effects were undeniable.

For something made by the Divine Physician, the performance was a little disappointing.

I grimaced and smacked my lips. Then I met Hyuk Mujin’s gaze as he stared at me with an almost uncomfortable intensity.

“What are you doing?”

“Y-yes?”

“What are you staring at me for? Is there something on my face?”

“Uh, no. You just look really… handsome today. Hehe.”

I couldn’t help a bitter smile at his ingratiating flattery.

Obvious.

He was trying to cheer me up somehow. My mood had been low lately.

But I didn’t let on. I clicked my tongue.

“Enough with the nonsense. If you’re done, get out. Don’t bother me just to make sure I eat.”

“Hey, ‘just’ make sure you eat? We’re all doing this to stay alive. What’s more important than food?”

“You sound just like someone.”

“Are you seriously comparing me to that glutton Taishan—”

His words trailed off.

Hyuk Mujin only moved his lips for a while, as though he’d said something he shouldn’t have. I turned my gaze back out the window, too.

After a brief silence, a voice quieter than before rang through the dust-covered room.

“Captain.”

“Go ahead.”

“Taishan… he’s doing all right, isn’t he?”

I answered in a low voice.

“He should be.”

“He eats so much, he might’ve already wiped out their food supply. He’s probably been sneaking food whenever he gets the chance, taking a few whacks from Old Man Nam, and getting scolded by Sama Pyo.”

“Could be.”

“I’m sure that’s what’s happening. Want to bet?”

“No.”

“Why not?”

“Because we’d both bet on the same thing anyway.”

“Oh. Right.”

“Yeah.”

Silence returned.

Longer than before, and much heavier.

And this time, too, it was Hyuk Mujin—not me—who broke it first.

“Captain.”

“Yeah.”

“Everyone’s… doing okay, right?”

I didn’t answer.

Instead, I took in the landscape I’d been staring at for the past two days, a view that hadn’t changed for even a moment.

It was overwhelming and awe-inspiring, yet somehow felt completely empty.

At the same time, I thought about why this perfectly filled-in landscape seemed as blank as a sheet of paper.

No.

I thought about the people.

Jin Wikyung, who would run toward me without a care for who was watching, shouting, “Youngest!” at the top of his lungs.

Jin Mukyung, watching his eldest brother stride ahead with a sullen expression.

Sama Pyo, now commanding hundreds of subordinates like a proper Sect Leader, and Namho and Taishan, who had somehow become inseparable.

A Thousand Captain of the Embroidered Uniform Guard who’d thanked me with a face stiff as a block of wood—and the ruler of the continent, whose body was dead yet who seemed more full of life than before.

I thought of all of them, everyone we’d parted from with a smile in Qinghai.

I thought of the past, already gone, and the future, soon to come.

But why?

I’d left the desert behind, and now, two days later, the sun was sinking. Still, they were nowhere to be seen.

Not the Murim Alliance’s banners rising like mountains in the west, nor the golden armor that should have flowed in like a tide from the east.

That was right.

I hadn’t been looking at the landscape. I’d been looking for the people who were coming from somewhere far away.

Yet even now, as the last day we’d firmly agreed on was drawing to a close, I couldn’t find them.

*…Maybe.*

I suppressed the three syllables that had risen unbidden in my mind.

Then, as though a wave could erase the disordered sand on a beach, I repeated to myself:

*No. That can’t be.*

They were strong.

Their blades and spears were sharp, and their conviction burned bright.

They were Murim. They were the Nine Provinces and all under Heaven.

So I held tight to the belief clenched in my fist.

This wait would surely be rewarded.

Even if they were worn out from an endless forced march and covered in dust, we’d see each other again soon, smiling.

I believed it.

Believing was all I could do.

“Let’s do it.”

Hyuk Mujin had come up beside me without a word and was looking out the window with me. He glanced over.

“Do what?”

“That bet from earlier. Let’s do it after all.”

I watched the world slowly turn red and went on.

“They’ll come before midnight. They will.”

Hyuk Mujin stared at me with wide eyes, then let out a quiet laugh.

“That can’t be a bet.”

“Why not?”

“We’d both bet on the same thing anyway. Then it’s not a real bet.”

“Damn. You’re right.”

“See?”

“So, you’re not doing it?”

“No.”

He added, with conviction,

“Of course I’m doing it.”

His voice drifted out the window on the wind.

As the sunset pressed down on the world, darkness gradually fell.

A darkness so still it was suffocating.

* * *

“We leave in fifteen minutes.”

A draft blew in from somewhere, making the candle flicker precariously. Jeok Cheongang’s voice and tone, however, were calm and composed.

“If we wait another day for these fools who forgot the agreed date—whether they’re from the Murim Alliance or the Imperial Guards—I’ll start producing relics inside my own body. It’d be a hundred times better for us to move ahead as scouts and vanguard.”

On the surface, it made sense.

Perhaps it felt even more convincing because Jeok Cheongang spoke so calmly, as though he’d expected this situation from the start.

The Slaughter Saint and Bow Saint, nodding on either side of him.

The rest of the group, listening quietly.

But one person was different: Jin Taekyung.

“You want us to move ahead?”

“Is there another way?”

“It’s not that there’s another way. We can’t take that one.”

“Go on.”

“If we head back west and east—even just a day, or half a day—we might run into our scouts…”

“Midnight has passed. The agreed date is already behind us. We discussed what to do after that in advance.”

“But…”

“Fool!”

*Whoosh!*

The air abruptly heated. His master’s sharp rebuke rang out, and he fixed his Disciple with a level gaze.

“I know what you’re worried about, but moving a great army like that comes with countless complications. We’re simply going one step ahead according to the plan we already made. Don’t argue about it any further.”

Normally, Jin Taekyung would have followed Jeok Cheongang’s words.

Their master-and-Disciple relationship might have been more informal than most, but Taekyung trusted and followed him more than anyone.

That was, if this had been a normal day.

But today—at least right now—was different.

A sense of déjà vu came over Jin Taekyung as he thought:

*What is this?*

Something was wrong. No—this was more than just wrong.

Xinjiang had long been treated as a deathtrap under the Demonic Cult’s rule, but that didn’t mean it was unknown territory.

Where had the cult’s immense power, fit to be called a theocratic kingdom, and the strength to fight the Murim of the Central Plains come from?

Xinjiang had abundant manpower and resources, just as you’d expect from a region so vast. It had once been one of the most important trade routes under Heaven, too.

In other words, the Hidden Shadow Pavilion had long since obtained all kinds of information, including details on Xinjiang’s geography.

After all, just a few months ago, they’d sent in dozens of spies—even if only one had made it back alive.

But the Tianshan Mountains were different.

If the Demonic Cult’s shadow covered Xinjiang, Tianshan was its Sacred Land, where the cult had first risen and put down roots.

The true unknown land within Xinjiang, itself a deathtrap.

*And no one had ever been able to reach its roots.*

But a moment ago, Jeok Cheongang had said they were merely going one step ahead according to a “plan already made”—a plan Taekyung had never even heard of.

*That can’t be. Once we enter Tianshan, joining up with our allies will be next to impossible.*

Maybe it was the thoughts clouding his mind.

Jin Taekyung felt his heart pounding hard and heat rising inside him.

At the same time, he realized one truth he could hardly believe.

“You were lying. Just to deceive me.”

Jin Taekyung’s voice trembled. Jeok Cheongang answered him.

“From the beginning, there was only one thing decided: if we couldn’t rendezvous on the agreed date, we’d advance without hesitation.”

His master’s heavy voice came crashing down like a war hammer.

“We… No. You’re the main attack.”

His master’s heavy voice came crashing down over his Disciple’s head like a war hammer.
## Chapter artifact 1184

# Chapter 1184

“We… No. You’re the main attack.”

“……!”

The moment Jeok Cheongang’s quiet voice pierced his ears, Jin Taekyung’s body went rigid.

At the same time, the fog clouding his mind finally began to lift.

But contrary to his hopes, the reality emerging beyond that fog was neither hopeful nor beautiful.

“What… what do you mean?”

A question was meant to express uncertainty, to seek a clear answer that would resolve it.

But Jeok Cheongang knew.

There was no uncertainty in the question Jin Taekyung had just asked. Only denial.

He was trying to use his own words to deny a reality he didn’t want to believe.

“You already know what this old man means.”

The old master looked at his Disciple with a grave expression.

Then he slowly continued, putting weight behind each word.

“Everything was for us. For you.”

“……You mean—”

“Xinjiang is Dark Heaven’s domain. No, it wasn’t only this land. Their eyes and ears have been hidden everywhere under Heaven. We had to consider every possibility.”

Things gathered together are strong; things scattered apart are weak.

Even so, they hadn’t divided their mighty army of more than a hundred thousand into three forces solely for practical reasons like supplies or marching speed.

“We had to keep it hidden until the very end, in case of the worst. We had to save one last dagger.”

That dagger was Jin Taekyung.

Not the sharpest in the world, nor the most precious—but against Dark Heaven, a weapon more lethal than any other.

No. Perhaps the Lord of Heaven’s only Adversary, chosen by Heaven itself.

“That’s why everyone agreed. The Sword Saint, the Emperor. And…”

Jeok Cheongang looked around at the silent group and added,

“We did, too.”

Only then did Jin Taekyung suddenly realize that not one person gathered here had objected to what was happening.

The Slaughter Saint and the Bow Saint. Ju Hwaran and Song Ilseom. Cheongpung, Gung Gibang, even Hyuk Mujin.

They either looked at Jin Taekyung in silence, faces dark, or lowered their heads, unable to meet his eyes.

“You deceived me. From the very beginning.”

“I’m sorry.”

Jeok Cheongang apologized with such sincerity that anyone who knew him even a little would have doubted their own eyes and ears.

But an apology wasn’t enough to make this right.

A hundred thousand.

More than a hundred thousand lives were still out there, beyond the darkness outside the window.

Among them were people whose bonds with him ran deeper than time itself—people whose fate was now unknown.

Comrades he could trust with his back. Friends he’d gladly lay down his life for. Brothers who weren’t related by blood, but had become true family all the same.

“I’m going back.”

With a strained voice, Jin Taekyung rose from his seat.

Shock from the unexpected revelation churned his stomach and made his head spin, but he gritted his teeth.

He had to go back now and save them. Find them.

……Even if all he could find were their bodies.

But before he could take a step, Jeok Cheongang’s voice stopped him again.

Or rather, it struck his frozen heart.

“Did we have time to do that?”

“……!”

“The agreed date has passed. We can’t hesitate any longer. If we delay even a little more, what comes after will be even more impossible to control.”

It wasn’t just something he’d said. It was reality.

A merciless reality Jin Taekyung understood better than anyone.

Everything was already collapsing, like a massive dam giving way.

The modern world. Murim.

Until the Quest was cleared, the bridge between the two worlds wouldn’t be connected. And the flow of time, already thrown far out of alignment, couldn’t be turned back.

No. There was only one way left.

Close his eyes, keep his mouth shut, and move forward.

Then, at the end of this journey, defeat the source of every disaster waiting there: the Lord of Heaven.

But…

*Even if I bring everything to a successful end, I’ll regret this for the rest of my life.*

That wouldn’t change even if he were hailed as the savior of a new humanity and seized immense wealth and fame.

He might gain everything in the world, but it would all slip through his fingers like sand.

Even now, after achieving so much, Jin Taekyung still sometimes had nightmares.

He still trembled at the roar of the Black Wyvern, which he could now kill with a single strike. He still wandered through that dark cave, where the screams of his companions had echoed without end.

And so, Jin Taekyung made his decision.

“I’m sorry.”

He steeled himself.

He would go back, even if only half a day or a day’s distance.

Even if that half day threw everything into disarray, he would accept it as a damnable twist of fate.

If he couldn’t save even the few people closest to him, then it would be nothing but the insane game of a being called a god.

Watching his Disciple, Jeok Cheongang muttered in a bitter voice,

“So, in the end, this is how it happens.”

“You know what I’m like.”

“I do. That’s why I took you as my Disciple.”

Feeling the sincerity in his master’s voice, Jin Taekyung smiled faintly.

“I’ll be back soon.”

“I’m sorry.”

Jin Taekyung shook his head.

He wanted to tell his master that none of this was anyone’s fault. It was simply a matter of choice; there was no need to apologize.

But for some reason, the words wouldn’t pass his lips. And the step he’d already taken wasn’t followed by another.

*What’s going on?*

The question came naturally, and Jin Taekyung breathed hard.

At some point, his heart had started pounding like mad.

His eyes burned as if torches were being pressed against them, and his vision shimmered with heat haze more intense than in the midday desert.

Then, in that world, warped and rippling all around him, an unexpected voice echoed like a distant call.

“No need to get worked up. You’ll feel peaceful soon.”

A calm tone. A troubled look.

Though he was in the middle of overwhelming confusion, it wasn’t hard to recognize the speaker.

“Why…?”

In answer to the question he’d barely managed to force out, the Slaughter Saint returned the very words Jin Taekyung had spoken a moment ago.

“Because I knew what kind of person you are.”

“……!”

“And don’t blame that Hyuk brat later. He was just as stubborn as his superior. It took me ages just to convince him.”

When Jin Taekyung saw Hyuk Mujin with his head bowed over the Slaughter Saint’s shoulder, he finally understood what was going on.

The strange way Mujin had insisted on checking that he’d taken the pill. The special fasting pills the Slaughter Saint had made.

*Poison?*

But something didn’t feel right.

If he’d been poisoned, the System would have warned him immediately, and the detoxification effect of the Myriad-Poison Ring on his finger would have activated.

His suspicion was entirely reasonable.

The problem was that his opponent, who was also known as the Divine Physician, knew that all too well.

“Poison and medicine are one and the same. It takes a very fine line to separate them.”

The man who’d used that “very fine line” to make a medicine almost indistinguishable from poison sighed softly and added,

“I didn’t want to go this far. I truly didn’t.”

Jin Taekyung answered in a hoarse voice.

“I understand.”

“I’m glad you can say that.”

“Then I hope you’ll understand me, too.”

“What do you—”

The Slaughter Saint was about to ask what he meant when—

*Whoom!*

With a heavy rush of air, Jin Taekyung’s fist came hurtling toward his face.

*Boom!*

The compressed air exploded as his fist struck through the space like lightning. The resulting gust whipped up the dust that had settled on the floor.

The Slaughter Saint twisted around just in time to evade the attack, his eyes wide.

*He can barely keep his body steady. How could he—?*

The strength and speed were hard to believe from someone practically in a poisoned state.

But unlike the Slaughter Saint, Jin Taekyung had no intention of answering his question.

To be exact, he didn’t have the time.

Another figure blocked his way as he rushed toward the window, cutting through the thick cloud of dust behind the startled Slaughter Saint.

*Shing!*

Two streaks of light flashed.

At their tips lay enough force and momentum to cleave through a boulder of solid iron in a single stroke, but Jin Taekyung twisted his upper body without a moment’s hesitation.

As if he’d predicted it all.

*Shhk.*

A blade passed by with a sound low enough to raise goose bumps.

And in the same instant, he struck back.

*Crash!*

Both his palms slammed into her twin sabers.

With a boom like an exploding cannonball, the Bow Saint’s sunken eyes appeared reflected on the trembling blade of her curved saber.

“Stop.”

Jin Taekyung answered by gritting his teeth.

*Crk.*

The pain in his jaw jolted his fading consciousness awake. It set fire to a body that had yet to fall asleep.

*Grind.*

His palm pushed against the blade.

At the same time, the Bow Saint began to slide backward with her treasured weapon as Jin Taekyung’s perfect, massive muscles flexed—too large to hide even beneath his thick robe.

It was a strength worthy of an ancient giant. A will that refused to die.

But that was as far as he could go.

As far as his heart and body could endure.

“I’m sorry. Truly.”

The moment Jeok Cheongang’s tearful voice came from behind him, Jin Taekyung felt every bit of the strength boiling inside him like lava turn cold.

At the same time, faces blurred like his vision, and memories of the time they’d spent together rose one after another, clouding his eyes.

Thicker and whiter than any fog or cloud of dust.

*Drip. Drip.*

Rainwater fell from somewhere, wetting the floor, and the old master finally caught his Disciple as his body collapsed.

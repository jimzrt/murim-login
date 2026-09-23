# Checkpoint Review — 910–914

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

# Chapters 910–914

## Plot

After Jin Taekyung’s attack, half-burned pursuers rise without pain or signs of life. Recognizing them as undead, Taekyung leads the group in retreat. Meanwhile, Jeok Cheongang surpasses his limits, defeats the Eastern Heaven Demon Lord, and then suffers unexplained cold pain. The Demon Lord survives and grievously wounds Jeok before they clash again.

The Demon Lord reveals that he was the lone survivor of the Maoshan Sect, destroyed by Taizu after it resisted the capital’s relocation. He used the Cang Gong identity to gain power within the Great Nation, and his bell raises the dead—including Ma Sanbao and more than a thousand Imperial Guards—as agile, fearless corpses. As the undead advance on the Emperor, So Gyo halts the Demon Lord’s attack with immense power. Baek Yeon and So Gyo defend the Emperor until Jeok and Taekyung return to confront the Demon Lord.

## Continuity

- The Eastern Heaven Demon Lord survived Jeok Cheongang’s seemingly fatal attack. Jeok is grievously injured and still suffers unexplained cold pain.
- Jeok Cheongang has surpassed the Three Saints and is committed to killing every member of Dark Heaven in vengeance for Hong Dao.
- Taizu ordered the Maoshan Sect destroyed after it resisted the capital’s relocation to Nanjing. The Demon Lord blames the rulers and the world for the loss of his family, Master, and fellow disciples.
- The Demon Lord became a eunuch to infiltrate the Great Nation, accepted an offer from an agent of the Lord of Heaven, and used Cang Gong’s identity to rise to power.
- The Demon Lord’s bell raises the dead as powerful, agile corpses that do not fear injury or death. Ma Sanbao is among the risen dead following his Master.
- More than a thousand dead Imperial Guards are advancing on the Emperor. Baek Yeon and So Gyo are defending him; Jeok Cheongang and Jin Taekyung have returned to face the Demon Lord.
- So Gyo has revealed power comparable to Jeok Cheongang’s and stopped the Demon Lord’s attack. Her identity and allegiance remain unknown.

## Translation Decisions

- Keep “undead” as Jin Taekyung’s general term distinct from “jiangshi,” Jeok Cheongang’s Maoshan-related term.
- Render 무림서열록 as the italicized book title “Murim Ranking Record.”
- Use “fourth star” for the Eastern Heaven Demon Lord’s description of Jeok Cheongang’s place beyond the Three Saints.
- Render 극염 as “Extreme Flame,” distinct from “Extreme Yang.”

## Durable state

{
  "active_continuity": [
    "The Eastern Heaven Demon Lord survived Taizu's destruction of the Maoshan Sect and blames the rulers and the world for the loss of his family and sect.",
    "The Eastern Heaven Demon Lord used Cang Gong's identity to rise to power within the Great Nation.",
    "The Eastern Heaven Demon Lord's bell raises the dead as powerful, agile corpses that do not fear injury or death.",
    "Ma Sanbao is among the risen dead following the Eastern Heaven Demon Lord.",
    "The Eastern Heaven Demon Lord has raised more than a thousand dead Imperial Guards and is advancing on the Emperor.",
    "Baek Yeon and So Gyo are defending the Emperor against the risen dead.",
    "So Gyo has revealed power comparable to Jeok Cheongang's and stopped the Eastern Heaven Demon Lord; her identity remains unknown.",
    "Jeok Cheongang and Jin Taekyung have returned to confront the Eastern Heaven Demon Lord.",
    "Jeok Cheongang still suffers unexplained cold pain."
  ],
  "continuity_sources": [
    914
  ],
  "open_questions": [
    "What caused Jeok Cheongang’s unexplained cold pain?",
    "What is So Gyo's identity and allegiance?",
    "Can Jeok Cheongang and Jin Taekyung stop the Eastern Heaven Demon Lord and protect the Emperor?",
    "What will happen to the Emperor and Prince Shangshan as the battle continues?"
  ],
  "safe_through": 914,
  "temporary_decisions": [
    "Keep “undead” as Jin Taekyung’s general term distinct from “jiangshi,” Jeok Cheongang’s Maoshan-related term."
  ],
  "version": 1
}

## Reading copies

## Chapter artifact 910

# Chapter 910

Just as a dog in a village school can recite poetry after three years, a few years of working as a Hunter—a specialized profession—can make you stop batting an eye at most situations.

The awful stench coming off a monster’s corpse? That’s nothing.

If you see blood spraying like a fountain and someone’s limbs getting chopped off—not in a game or a movie, but in real life—

And if that someone is you or one of your companions… well, there’s no need to say more.

The fear of death you feel before even stepping onto a battlefield. Then, after watching all kinds of brutal scenes as often as you eat, every nerve and sense starts to grow numb. Only then do you become a Hunter in the truest sense.

That’s how it was for me.

But even I, with a fair amount of hard-earned experience under my belt, couldn’t hold back the nausea rising from the pit of my stomach right now.

“That’s…”

*What the hell is that?*

I couldn’t bring myself to say the rest aloud. I had to clamp my mouth shut to settle my churning stomach.

And I wasn’t the only one reacting that way.

“Ugh.”

Ju Hwaran was the first to bend over. Her face had gone pale as she covered her mouth.

As the heir to the Yongbong Escort Bureau, she’d had far more experience than other young prodigies her age. But compared to everyone else here, she still lacked real combat experience. It was only natural.

No, the fact that she hadn’t thrown up was impressive all by itself.

Everyone here—including me, who’d fought my way through all kinds of hellish situations—was barely holding back a gag, our faces twisted.

“What… What is this?”

The Divine Physician muttered in a strangled voice.

The old physician’s eyes trembled. They held undisguised shock and the fear of someone who’d glimpsed something beyond comprehension.

Along with a sight before us that was impossible to believe.

*Sizzle. Hissss.*

The distance was short—not even a dozen *jang*. We could hear flesh burning, and a horrible stench wormed its way into our noses.

Then, amid the remnants of the flames and the blackened ashes, shapes began to stagger to their feet.

“Grrr… Gaaah.”

Their voices were neither screams nor words.

The black-clad figures—no, the things we could no longer call people—let out strange, unrecognizable cries through their melted lips and staggered forward.

As though they couldn’t feel even the slightest pain.

As though they didn’t even know what state their bodies were in.

*Crack. Crumble.*

Arms, legs, or something else entirely—blackened by the scorching heat that had swept through once already—broke apart and scattered as ash.

One of the things that lost its balance and fell tilted its head.

“Grr…?”

Watching that gesture, as if it were asking why its body wouldn’t move, sent a shiver down my spine.

*They’re moving? Even after taking a blow like that?*

Of course, not all of them had been caught in my attack.

But at least a hundred black-clad figures at the very front had taken the flames pouring from my spearhead full on.

That terrible heat. That devastating strike made of Scorching Yang Qi.

I’d seen it with my own eyes. Everyone here knew it.

That was exactly why it was even harder to believe.

*It had enough power to kill them outright. No—it should’ve been impossible for them to survive.*

My body might not have been in good shape, but I’d given it everything I had.

I’d poured in most of my remaining internal energy, and I’d been sure of the result. I was certain that strike would kill at least one in ten of them.

But it hadn’t.

Right before my eyes, nearly half of the hundred figures at the front were getting back up, trampling the ashes of what had once been their comrades.

And in a state that made it impossible to think of them as anything that still had a breath of life in it.

“…This is insane. What am I looking at?”

Namho’s groan, from someone who’d personally lived through the terrible history of the Great Faction War, spoke for everyone. But not for me.

Or, to be more precise, at that moment I was seeing something else the others didn’t know.

*How is this possible?*

Death was fair to everyone in the world.

A Supreme Peak master could be cut down by a weapon just like a Third Rate knife-fighter. If your skin melted and your insides burned like theirs, you couldn’t get back up again.

But they had survived.

Even in a situation like this, they neither screamed nor showed any agitation—not even a sign of the pain they should’ve been feeling.

*This is…*

That was when it happened.

A word I desperately didn’t want to believe, but which had naturally surfaced in my mind, struck me like lightning.

Then it slipped through my parted lips.

“Undead…”

Not dead, but not alive either.

Supernatural beings who carried on existing at the end of death instead of finding rest. Monsters that should never have appeared in this world.

There could be only one answer. And from that moment on, I knew what I had to do.

“Eom Dae-du? What does that mea—”

“Run.”

“What?”

I looked at Hyuk Mujin, his eyes wide, and spoke in a low, tight voice to him and everyone else.

“If you want to live, run. Right now.”

“……!”

“……!”

And the next moment—

*Rumble!*

Through the ringing air, the dense smoke still hanging all around us, and the blazing piles of ash, an army of the dead came marching out and surged forward as one.

“Grrraaaaa!”

Their cries carried the chill of death.

* * *

From time immemorial, the Murim had been a fascinating subject for the gossips of this continent.

And why wouldn’t it be?

Another world within a boundary without borders or laws.

A place where outlaws who lived beyond the confines of nation and citizen ran rampant.

A world teeming with people who could be righteous heroes, fiends, or—depending on the moment—neither. A true mountain of sabers and forest of swords, where even the greatest master could meet his death at any time.

For those reasons, the people of the Murim had been scorned and admired in equal measure. The gossips, who loved to chatter about everything, gathered every bit of information they could see and hear, then ranked them.

That was how the book with the ridiculous title *Murim Ranking Record* came into being.

But even the gossips, with their far-reaching connections and keen ears, couldn’t overcome the obvious limits of what they knew.

Who was stronger than whom?

Everyone whose name had appeared in the *Murim Ranking Record* was a formidable master. And the closer you got to the last page, the more often you came across those called superhuman.

Supreme Peak masters from the orthodox faction, the unorthodox faction, the Demonic Cult, or somewhere between orthodox and unorthodox.

Among them were wandering martial artists who roamed the Murim alone like lone wolves, heirs to mysterious and little-known sects, leaders of great powers, and people called Cult Leaders. Most of them shared one thing in common.

Nonaggression. A ban on fighting.

They didn’t confront one another lightly, and they didn’t fight easily.

It was only natural, since every one of them was a giant who could move the Murim. But for the gossips, it was a real disappointment.

If a life-and-death duel broke out between Supreme Peak masters, they’d learn for certain who outranked whom—and gain a rare story they could dine out on for the rest of their lives.

But conflict in the Murim didn’t erupt so easily, and for a long time the last page of the *Murim Ranking Record*, where the names of the greatest warriors were written, went unchanged.

That is, until the storm of the Great Faction War swept through more than fifty years ago.

And as if to mock the long stretch of peace, countless things no one could have imagined began to change.

One revered master died, then another, and another.

With news arriving every day as the sun rose and set, the gossips’ brushes were nearly worn to nothing.

But just as the sun rose and set, new names appeared as well.

“Have a look at this. I think the information must be wrong.”

“Wrong? That can’t be right.”

“Read it. It says a thousand Demonic Cult members were massacred in Anhui. I can’t believe that’s true.”

“A thousand? That’s quite a large number. But I don’t see any reason to doubt it. Looks like the Murim Alliance finally landed a proper blow this time.”

“It wasn’t the Murim Alliance.”

“What?”

“It says it was all done by one person. He wiped out a thousand Demonic Cult members alone, without anyone’s help. Not a single one was spared.”

“…What?”

The name Jeok Cheongang was first made known that way. A few years later, he acquired the title Fire King. By the end of the Great Faction War, which had shaken the world of the Murim, his name had made it to the last page of the *Murim Ranking Record*.

The Martial God and the Three Saints.

And among the ten Supreme Peak masters who followed them, he was the fiercest and strongest of the kings: the King of Kings.

The name Fire King Jeok Cheongang.

But the man himself wasn’t proud of any of it.

“*Murim Ranking Record*? The world’s gone mad. These days, do they give firewood some grand name like that?”

In response to Jeok Cheongang’s indifference, the monk who’d first told him about it smiled and sipped some suspiciously warm grain tea.

“Is that so? Still, when I looked it over, I found it surprisingly accurate for firewood.”

“That’s just a bunch of fools talking nonsense. Are there only orthodox martial artists in the world? Plenty of powerful fighters practice demonic and heterodox arts, too.”

“Even so, in the orthodox Murim, you’re ranked fourth. After the Martial God and the Three Saints. You’re quite something.”

“Enough. That’s quite enough of your nonsense. Now pour this old man a drink. What did you brew it with this time?”

“Amitabha. You mustn’t say such things. This is grain tea, not alcohol.”

“What the hell’s grain tea? You sound like you’re kicking the Buddha in the ribs.”

“Now, watch your mouth. Do you want to suffer in tongue-pulling hell[^1] later?”

“Fine, fine. Give me a cup before I break that Green Jade Buddha Staff you’re holding. I don’t want to set fire to the Shaolin Temple at my age.”

“Ha ha! What a joke. In any case, judging by my guess, within ten years at most, you’ll overturn the order of this *Murim Ranking Record*.”

“Hmm. I probably will. I’m old enough that it wouldn’t be strange if I kicked the bucket within ten years.”

“…Amitabha. You say unlucky things so casually.”

“Well, I’ve lived a long time. I don’t know when we’ll meet again, but if you haven’t heard from me in ten years, come to Mount Jiuhua and cremate my body. Better yet, scatter my ashes from the highest peak.”

“Hm. You’re more extravagant than you look. Asking the Abbot of Shaolin to come chant sutras for you.”

“I don’t need sutras or a fortunate rebirth in paradise. That’s the way I’ve lived.”

“Then how about a wager?”

“A wager? What kind?”

“Whether you’ll surpass even the Three Saints in ten years or die as you said. For the record, I’m betting on the former.”

“……”

“Trust me. And in ten years, let’s meet here and have another drink.”

It had happened a long time ago.

Three sets of ten years had passed since they made that promise. He’d sent off an unworthy Disciple he’d taken in by mistake, and even the friend he’d sat across from and shared drinks with had returned to the earth.

Yet at this very moment, Jeok Cheongang suddenly remembered that long-forgotten memory.

The words Hong Dao, the Dharma King, had once spoken to him with a serious expression, though he’d always smiled so amiably.

*You’ll surpass the Three Saints.*

*Boom!*

His departed friend’s faint voice didn’t fade, even beneath the blast of air released by the powerful Palm Force.

No—instead, it sounded even clearer.

*Trust me.*

*Shh-shh-shh-shing!*

Wind sharp as blades whipped around him. But the Eastern Heaven Demon Lord’s fierce attack—the pale-skinned old man’s—didn’t touch a single part of Jeok Cheongang’s body.

And that felt entirely natural to him.

*Ah.*

Jeok Cheongang suddenly felt elation well up from deep in his chest.

He had lived a hundred years and then some. All his life, he’d inflicted pain on others, suffered pain himself, and, for the first time, shared that pain with someone.

His advanced age. The Heart Demon that had filled his mind.

*I thought this realm, which fortune brought me to, would be the last limit I could reach.*

Now he knew.

He had been wrong. His departed friend had been right.

*Though I haven’t surpassed them yet…*

I’ll try.

As the words scattered from the tip of his tongue, a faint smile formed on Jeok Cheongang’s lips.

And at that moment—

*Fwoosh.*

A massive blaze unlike anything he’d shown before slammed into the Eastern Heaven Demon Lord’s chest.

[^1]: A Buddhist hell associated with punishment for liars and slanderers.
## Chapter artifact 911

# Chapter 911

He could feel it.

His body and mind both felt light enough to take flight.

A power boiling deep within him, and the joy of having taken even a small step into a higher realm, engulfed Jeok Cheongang.

And the little insight that had come to him so suddenly was blooming into an even more powerful, tremendous blaze.

Just like now.

*Fwoosh.*

A dazzling white flame, shining like a flash of light, roused the darkness. It devoured and tore its way forward.

Toward the enemy before him. Heating the Eastern Heaven Demon Lord’s gray eyes.

“……!”

The Eastern Heaven Demon Lord’s eyes widened as a fist came crashing toward him, erasing the space between them.

*What is this?*

He realized it instinctively.

The power contained in that fist was qualitatively different from the countless attacks he’d clashed with and evaded until now.

That great martial artist known as the Fire King had taken another step forward.

And for the Eastern Heaven Demon Lord, that meant only one thing.

*I can’t dodge it.*

At that moment—

*Kwaaaang!*

The earth shook as a deafening roar split the sky.

A terrifying tremor and the force of the impact swept over everything. Through the smoke and steam, heavy with dreadful heat, a figure was hurled away.

*Whooosh!*

As the Eastern Heaven Demon Lord’s view spun around and around amid a fierce rush of air, Jeok Cheongang stepped toward him. It was the Demon Lord who had been hurled away like a cannonball by the impact.

*Crack—boom!*

A movement that outstripped sound.

Jeok Cheongang shot forward like a streak of flame and reached out his hand.

The Flame-Extinguishing Divine Fist, brought to full mastery—or perhaps now beyond even that—washed the space in white.

*Bang!*

The first strike broke the Eastern Heaven Demon Lord’s sword.

*Boom!*

The second barely grazed past him, melting the ground.

*Kaaa-bang!*

The final, third strike slammed into the staggering Eastern Heaven Demon Lord’s chest once more.

It shattered even the formidable Body-Protecting Qi that had enveloped him.

*Krrrunch!*

The hard bluestone covering the grand banquet hall crumbled like tofu.

At the sight of the Eastern Heaven Demon Lord being hurled away, his body smashing through more than ten *jang* of ground, those who registered the unbelievable reality unfolding in an instant all moved at once.

“Kill him! Kill that bastard!”

“The Demon Lord is in danger!”

“Stop him!”

Shouts rained down from every direction. Blades flashed.

But nothing could stop Jeok Cheongang now.

“Who dares—”

*Crack!*

“—to stand in this old man’s way?”

*Boom!*

No one could reach Jeok Cheongang. No one could even come close.

Blades carrying gleaming Sword Energy melted in the flames of the Flame-Extinguishing Divine Fist, while the Flame Divine Palm shot across the space and swept fiercely over the approaching enemies.

“Urk—cough!”

“Aaargh!”

Those who summoned up their courage and charged him head-on were the lucky ones.

Anyone who so much as touched the flames had to howl as their own flesh burned away while they were still alive.

Those screams, like cries of agony, soon became their last words.

*Rustle. Thud.*

In their brief but horrific agony, the corpses of the dead sprawled like rotting trees.

Over the bodies of the traitors, fused with their golden armor as it melted and stuck to them, armor that had yet to lose its shine gleamed.

“Execute the traitors!”

“Long live His Majesty the Emperor!”

*Shh-shh-shing! Slash!*

Jeong Hogun was the first to cut down an enemy frozen by the unbelievable might Jeok Cheongang had displayed. The Embroidered Uniform Guards who charged after him swept over the traitors like a wave.

*Clang-clang!*

*Thwack!*

Weapons clashed fiercely, spitting sparks. Blood sprayed in every direction.

And at the center of it all, the giant known as the Fire King did what he had always done: smashed and burned everything in his path as he pressed forward.

To end this fight.

Toward the Eastern Heaven Demon Lord, who was staggering back to his feet behind the countless moths still rushing at him.

*Boom!*

Scorching Yang Qi, hot as lava, swallowed dozens of enemies.

The bluestone had lost its smooth, original sheen and melted into a wretched mess. Corpses still smoldered like firewood, flecks of flame clinging to them.

As Jeok Cheongang approached, forging a path of fire no one dared block, the Eastern Heaven Demon Lord spoke in a voice mixed with a sigh and admiration.

“You attained… cough. You attained enlightenment?”

Jeok Cheongang stopped just a few steps away and stared at him without a word.

His condition was pitiful by anyone’s standards.

His beard, once white as snow, was soaked with blood. One arm and one leg were broken. His clothes had already been reduced to ash, leaving his chest exposed and blackened with burns.

His injuries were so grave that not even Hua Tuo—or a Great Firmament Immortal—could guarantee he would survive.

Yet the Eastern Heaven Demon Lord only kept coughing roughly and continued to speak.

As if doing so could ease, if only for a moment, the terrible pain he was feeling.

“The Three Saints… are a thing of the past now, I see. A fourth star has risen right here, today.”

Jeok Cheongang answered in a low voice.

“Call it whatever you want. I don’t care about things like that. But…”

*Step.*

The footsteps that had paused began moving again. White hellfire rippled over his body, ready to bring this brief, ill-fated encounter to an end.

“You know one thing, at least. The third Demon Lord is about to die.”

Jeok Cheongang’s gaze on the unsteady Eastern Heaven Demon Lord was cold and clear, unlike the energy he wielded.

Not a hint of carelessness. He would make certain the man died.

Until now, the members of Dark Heaven had demonstrated unbelievable abilities time and again, directly contradicting the laws of the world Jeok Cheongang had believed in for more than a hundred years.

But all of it had been trial and error, not failure.

A process of moving toward somewhere broader and higher.

Each time he survived an unpredictable turn of events, Jeok Cheongang gained new experience and insight. He grew stronger, little by little.

The old monster of Mount Jiuhua was still growing.

Just as his Disciple was.

Just as his close friend, now dead, had once promised he would.

“A certain bald monk once said, long ago, that before long, this old man would surpass the Three Saints.”

*Step.*

Watching Jeok Cheongang tread carefully toward him, the Eastern Heaven Demon Lord gave a faint smile.

“That monk was right.”

“Yes, he was. Thinking back on it now, I wonder if that monk had some trick for reading the heavenly patterns… but I’ll never be able to find out. Do you know why?”

The Eastern Heaven Demon Lord didn’t answer. From the mention of reading the heavenly patterns, he’d realized who the bald monk Jeok Cheongang meant.

And Jeok Cheongang wasn’t expecting an answer.

“He’s dead. Killed by you people of Dark Heaven.”

“…Hong Dao, the Dharma King.”

“If I’d been at Mount Jiuhua, I wouldn’t have been this angry. There would’ve been nothing I could do about it.”

But that wasn’t what had happened.

Hong Dao, the Dharma King and Jeok Cheongang’s friend, had met his death at the hands of the Blood Lord within the grounds of Shaolin Temple.

Somewhere Jeok Cheongang could have reached in a matter of moments.

“The monk died like that. By the time I got there, it was already too late.”

There had been a time when Jeok Cheongang was afraid.

Afraid that the damned infirmities of old age that had come for him would someday wipe away even the final image of his dying friend. That they would make him forget the vow he’d made, biting his lip until it bled.

“That day, I made a vow.”

*Step.*

Taking another step, Jeok Cheongang continued.

“I swore I’d kill every last one of those bastards with the name Dark Heaven attached to them.”

*Rumble, rumble.*

The ground shook. The air boiled.

An energy so hot it seemed to erase even the air itself—an energy worthy of being called Extreme Yang, no, Extreme Flame—flowed from Jeok Cheongang’s entire body like lava.

As if ready to swallow the Eastern Heaven Demon Lord at any moment.

“And today, I’ll send one more of them to the afterlife with my own hands.”

Five steps.

That was the distance between Jeok Cheongang and the Eastern Heaven Demon Lord. At such close range, one of them could be dead in an instant.

“Save your last words for Yama.”

At that moment—

*Fap.*

The Eastern Heaven Demon Lord lunged. His body vanished. There was not the slightest hint in his speed or movement of the man who, moments ago, had seemed to be waiting for death to draw near.

*Shh-shing!*

Jeok Cheongang reacted to the sound piercing his ears.

There were two overlapping rushes of air. No—three.

“*Hah!*”

*Paaang!*

As the azure dragon’s roar shook the battlefield, the internal energy carried in his shout burst the compressed air.

At the same time, two streaks of light shot toward Jeok Cheongang’s back as if guided by an invisible hand—then were knocked away.

They were the Eastern Heaven Demon Lord’s two swords, drawn toward him by the power of his Middle Dantian. Jeok Cheongang brought up the energy from his entire body, poured it into both hands, and swung upward as if scooping something from below.

Toward the sky above him. Toward the Eastern Heaven Demon Lord, plunging down like a meteor.

*Whoom.*

Two white energies—clearly similar, yet astonishingly different—raced toward each other.

To their eyes, they moved slower than an ant. Yet they were moving too fast for anyone else to see.

And the moment the two palms, each monster swinging with everything he had, collided—

*Kaaaang!*

*Rumble, rumble, rumble!*

A blinding flash obscured everyone’s vision. An unbearably vast, unprecedented force burst outward, engulfing everything in light. It swelled, swallowing the sprawling grand banquet hall that had already become a battlefield.

*Whooosh.*

The darkness vanished. The unsteady torches disappeared, along with the people thrusting blue blades at their enemies and the angry shouts they’d been roaring.

No—in that instant, it was more accurate to say that everyone’s sight and hearing had been swallowed by the flash and roar.

……!

……!!

A white world where nothing could be seen or heard.

Those trapped inside it forgot friend and foe alike, frozen in utter confusion. Only a tiny handful were exceptions.

*Papapat!*

Jeok Cheongang and the Eastern Heaven Demon Lord charged at each other without pause.

They moved faster than sound, redirecting their opponent’s attacks, counterattacking, then shooting at each other again.

To the world, it all lasted but an instant. But to those superhuman beings who had cast off the limits of humanity, it was different.

Within time that seemed to have stopped, they fought hundreds of exchanges, faced danger dozens of times, and finally reached the end of their seemingly endless life-and-death duel.

*Thwack!*

With the sound of bone and flesh crushing, someone staggered.

But the fist that had pierced his chest and burst out his back—and the white flames that licked around it—wouldn’t even let him fall.

“Truly… truly incredible…”

His voice trailed off, drained of strength.

In Jeok Cheongang’s deeply shadowed eyes, the Eastern Heaven Demon Lord’s two arms hung limp, shattered beyond recognition.

“If Yama asks why you died…”

*Shunk.*

Jeok Cheongang’s fist slowly pulled free. Only then did the other man’s body begin to crumple.

“…Tell him a friend of that bald monk sent you.”

*Thud.*

Jeok Cheongang silently looked down at the fallen Eastern Heaven Demon Lord, the corpse in which not a trace of life remained.

Then, just as he let out the breath he’d been holding and turned away—

*Crack.*

A cold pain that shouldn’t have been there, a pain he couldn’t begin to understand, swept through his entire body.
## Chapter artifact 912

# Chapter 912

Everything happened in a flash.

Jeok Cheongang sensed the sinister energy flying at him from behind. The red alarm bells in his mind rang, and he twisted his body.

But even instinct, faster than reason, couldn’t help him fully evade that strike.

*Crunch.*

It was hot. And cold at the same time.

A pain that made no sense, beginning in his side, spread through his entire body like a wildfire.

Along with an impossible question.

“……!”

Jeok Cheongang looked down, his eyes trembling, at something buried halfway in his side.

It had crushed flesh and bone, severing the vital points and internal energy inside him strand by strand. The hand was as pale as a corpse’s—or rather, it belonged to someone who should have been lying dead.

“How could you… how could you…”

Jeok Cheongang lifted his head, squeezing the words out. In his field of vision was a face that should never have been there.

“You had… stopped breathing.”

The owner of the hand, the Eastern Heaven Demon Lord, replied.

“Yes. I had.”

Then he added, his voice as calm as if nothing had happened, his expression numb and free of even a hint of pain:

“But who in this world can lose his one and only life twice?”

“……What?”

Jeok Cheongang stared at the Eastern Heaven Demon Lord, eyes wide with an incomprehensible question. But instead of an answer, an icy energy burrowed into his body.

*Danger!*

It happened almost at the same time.

Powerful force from the palm drove deep inside him at almost the same instant Jeok Cheongang twisted away in a flash.

But his body, caught off guard by the unexpected blow, couldn’t evade the attack completely.

*Boom!*

Jeok Cheongang bit his lip as his vision blurred for an instant.

*Damn.*

The pain was intense.

Feeling the Body-Protecting Qi around him scatter like smoke, Jeok Cheongang shot backward.

*Whoooosh!*

His vision blurred. The sky and earth flipped over and over.

An unknown person’s scream rang out. Fragments of something that had struck his body as it shot away flew in every direction.

It was enough to knock even a Supreme Peak master out of a fight in one blow.

But he wasn’t just anyone.

He was Jeok Cheongang, the Fire King.

*Crack! Bang!*

He twisted in midair, righted himself, and landed on his feet.

Jeok Cheongang carved a deep furrow several *jang* long into the ground, absorbing the remaining force. Then his body suddenly staggered.

*Hack.*

Dark red blood spilled from between his lips.

Unable to hold back the congested blood that had risen with his internal injuries, Jeok Cheongang spat it out. That was when a faint whistle reached his ears.

*Whoosh.*

He hadn’t seen it. But he could feel it.

A strike plunging down toward his head. The Eastern Heaven Demon Lord reaching out with a hand that shone an icy, glacial white.

Picturing the scene that had formed in his mind half a beat ahead, Jeok Cheongang pushed off the ground.

*Shwaaack! Boom!*

In a brief moment split into ever smaller fractions, the strike narrowly missed him. It cleaved through the ground like tofu, then exploded, leaving a gigantic crater.

A few Embroidered Uniform Guards nearby were unlucky enough to be swallowed up by it.

But the pursuit of a predator that had missed its prey didn’t end there.

*Swish.*

The movement was as smooth as a snake’s.

The Eastern Heaven Demon Lord rose from the crater and stepped toward the retreating Jeok Cheongang.

*Papap!*

In an instant, he erased the distance between them. A dazzling, icy white light burst from his fingertips.

*Fwoosh.*

Watching that brilliant yet dreadful light swallow the darkness and swell, Jeok Cheongang gritted his teeth.

*Crack.*

A faint pain, and the taste of blood in his mouth.

Only then did his blurred vision come into focus. His dulled senses returned, and the pain from his internal injuries grew more severe. Jeok Cheongang paid it no mind and drew up the internal energy throughout his body.

*Wooooong.*

The air, chilled moments ago, grew hot. His torn meridians screamed.

Within his unsteady control, the fire dragon inside him writhed violently.

As if it would burn even its master’s body.

As if it would devour everything and reduce it to ashes.

And yet—

“I don’t know what kind of bizarre power brought you back to life.”

Jeok Cheongang stared straight at the Eastern Heaven Demon Lord, his gaze utterly unwavering. His voice burned like lava as he continued:

“But I’ll put an end to that stubborn life of yours.”

Even if he had to do it dozens, hundreds of times.

His tightly closed lips held back the words he left unsaid. But they could not hold back several *jiazi*’ worth of Scorching Yang Qi as it surged through his body, setting every limb and meridian ablaze.

*KWAOOOOO!*

Amid a roar like a dragon’s bellow, light-flames and white light shot toward each other. At last, they collided.

At the center of that space, warped by unprecedented energy—

Even Jeong Hogun’s scream-like cry for a retreat was swallowed up.

*Fwoosh.*

And in the blinding flash that filled his vision, Jeok Cheongang heard someone’s voice reach his ears.

“Old Master!”

The next moment—

*Rumble, rumble, rumble!*

The entire world—the sky and the earth—shook.

* * *

There are moments like that.

Moments when it feels as if the world has stopped.

Moments when every sense goes numb from the shock and roar reverberating in every direction.

That was exactly how it felt to me right then.

“……!”

If the sun fell from the sky one day and landed right in front of you, would it feel like this?

With the flash and roar blinding and deafening me, all I could do was protect the people nearby as best I could from the enormous impact about to hit us.

“Get down, ri—!”

I didn’t know. I didn’t know if my frantic shout had reached the Fire Dragon Pavilion members, or if they had immediately followed my order and dropped low.

There was just one thing I knew for certain: if they’d hesitated for even a moment, not one of them would still be standing.

*KWAaaaaa!*

*Rrrrcrack!*

My body was shoved back by the wildly raging gale. The ground overturned like a volcanic field, and the bluestone broke into dozens, hundreds of fragments that rained down in every direction like hidden weapons.

Along with the corpses of the dead, and the countless weapons that had been scattered all around like their gravestones.

*Sh-sh-sh-shik! Thud!*

“Aaargh!”

Someone’s blood and screams scattered on the wind.

But I drove both feet deep into the ground and endured the shock wave with my whole body.

I squeezed out the last of my internal energy, batting away and cutting through everything that came flying at us.

*Pit-pit!*

Even when small, thin fragments of blades and bluestone swept in with the gale and grazed me all over, I didn’t care.

*If I dodge, the others will get hurt.*

If someone was bound to get hurt, it was a hundred, a thousand times better for that someone to be me.

*Old Master must have felt the same way.*

At the very last moment, I’d seen it clearly.

He’d heard my shout and suddenly shifted to place himself across the path we were headed down.

*KWAaaaaa……*

How much time had passed?

Beyond what felt like an eternity, the roar and impact began to subside.

Then, one by one, the things that had been carried into the air by the wind fell back down. The muffled sounds around me, silenced for a moment, began to filter back into my ears.

“Ungh……”

“P-please. Someone, please……”

The groans of the fallen, tangled together, from both sides. Someone’s desperate plea as death approached.

And finally, the familiar voices behind me.

“Is everyone—everyone all right?”

“Cough. I’m fine.”

“Taishan gritted his teeth and held on while thinking about two hundred plates of five-spice pork.”

“I’m really sorry to ask at a time like this, but is there anyone who can break that bastard’s teeth?”

I wanted to answer Namho, but my strength had given out, and even that was difficult.

When I staggered, two people hurried over and grabbed me by both arms.

“Benefactor—no, Young Master Jin—no, Pavilion Master.”

“Captain, are you all right?”

I told Ju Hwaran to pick one form of address and stick to it. Then I gave Hyuk Mujin a pointed glare that meant, *Do I look all right to you?* After that, I looked beyond him and saw the undead army climbing over the stone wall several dozen *jang* away.

The Imperial Guards, who had changed sides to avoid being branded traitors, were now falling in droves, blood spilling beneath the sudden attack of those monsters.

*Damn it. Maybe I should’ve lured them here after all.*

I couldn’t help wondering if we might have done some damage to them if I had, but there was no way to know what would’ve happened.

Those things were undead, plain and simple.

Monsters that got back up even when their arms and legs were torn off, or their chests were pierced.

But the word *monster* wasn’t reserved only for those with grotesque appearances or strange powers.

When people see something that can’t be judged by common sense, they call it a monster.

And among those monsters was the man known as the Fire King.

*Papap!*

I pushed Hyuk Mujin aside as he tried to stop me, and hurried toward Jeok Cheongang as fast as I could.

No—I tried to.

If not for the one thing Jeok Cheongang said next.

“Stand back.”

His voice was far deeper than usual.

His entire body was covered in blood and soot, but he kept his eyes fixed ahead without even glancing at me, though I stood a few steps behind him.

At the solitary figure standing upright beyond the dust cloud as it slowly settled.

And right then—

*Fwoosh.*

A breeze blew from somewhere, sweeping away the dust cloud. Beyond it, the figure came into view, walking slowly over countless corpses and pools of blood.

“……!”

I instinctively caught my breath. Only then did I understand.

Why Jeok Cheongang had told me to stand back.

And why I hadn’t sensed even the slightest sign of life from someone who had been right beside us, if only for a moment.

“Impressive, Fire King Jeok Cheongang. Truly impressive.”

*Squish.*

With each step, blood that had pooled to his ankles sprayed in every direction.

Arms and legs that had belonged to someone unknown bobbed in the blood as it pushed them along.

But none of it created as dreadful an atmosphere as *that thing*.

“I very nearly died, you know.”

*Crackle. Sizzle.*

Beneath his face, still burning in the flames, the only part that had kept its shape—his lips—curved into a gentle smile.

Cang Gong—the Eastern Heaven Demon Lord—or rather, the man who could no longer be called human, was smiling.

His melted skin and the bones that should have been hidden beneath it were exposed for all to see.

His appearance was so horrific that anyone made of flesh and blood would have died several times over. He looked at Jeok Cheongang, then at me, frozen behind his shoulder.

Then he spoke without warning.

“You two seem very close, master and disciple. Don’t you think?”

At that moment, I heard a voice I’d thought I’d never hear again.

“Yes, Master.”

“You’re late.”

“Forgive me. Your unworthy Disciple’s training wasn’t sufficient.”

As he answered, another figure staggered to his feet.

Ma Sanbao pulled the short spear I’d driven deep into his body and approached. Jeok Cheongang murmured:

“Master?”

“Why? Is that strange?”

The Eastern Heaven Demon Lord stepped forward and continued:

“I once had a sect, too. A Master who became a parent to me, and countless Senior and Junior Brothers who became my family.”

“……You bastard. Don’t tell me…”

“But they all died. They bled and fell while trying to protect their sect’s home, fighting against an oppression that made no sense.”

The Eastern Heaven Demon Lord slowly turned his head. At the end of his empty gaze sat the Emperor, on a tall, ornate throne.

No—what lay there was a past that had long since slipped away.

“Under the pretext of moving the capital, I had to lose them all.”

“……!”

“……!”

At that moment, I realized who he really was. Before he became the Eastern Heaven Demon Lord of Dark Heaven, before he became Cang Gong of the East Depot, where had he belonged?

Jeok Cheongang realized it, too.

“……The Maoshan Sect.”

As those words, like a groan, slipped between his lips—

*Crick. Crrrick.*

At last, the army of the dead breached the stone wall and poured into the grand banquet hall.
## Chapter artifact 913

# Chapter 913

A sea of corpses and blood.

That was exactly what it was.

Everywhere the eye could reach, corpses piled up and blood pooled in overflowing streams.

This vast space had been built to celebrate the imperial family’s good fortune. Now it had become a battlefield where countless people killed and died. Even though the Embroidered Uniform Guard led by Jeong Hogun had finally put down most of the traitors, they couldn’t fully enjoy the taste of victory.

No—instead, fear gripped them, and they had to stand back-to-back.

Their battle wasn’t over yet.

And now, the enemies they had to face were monsters far beyond the bounds of common sense.

*Grrk. Grrrr.*

A foul stench so vile it drowned out even the thick smell of blood.

Jeok Cheongang stood back-to-back with Jin Taekyung, watching the creatures circle them and shriek in a language no one could understand. Then he suddenly spoke.

“Let me ask you one thing.”

“You can ask me all day and night for three days straight. No limit.”

Jin Taekyung spat out the blood pooling in his mouth, picked up a spear and sword lying on the ground, and added:

“If those bastards are willing to wait that long, of course.”

Naturally, Jin Taekyung knew it, too.

There was no chance of that happening.

*They’re all thinking the same thing.*

The faces of the Fire Dragon Pavilion members and the Embroidered Uniform Guards, now standing back-to-back in a circle, showed the same feelings swirling inside him. And then Jeok Cheongang’s subdued voice came from behind him, tense in a way he couldn’t hide.

“The realm of immortals… In other words, your homeland. Does it have things like those?”

Jin Taekyung answered without hesitation.

“Of course. There are tons of them.”

“Tons? Just how many?”

“Uh, Old Master, how many meals do you think Taishan’s eaten in his whole life?”

“An awful lot, I’d imagine. Too many to count.”

“I think so, too. Now imagine at least dozens—no, hundreds of times that many.”

Jeok Cheongang let out a sigh as understanding dawned.

“Fuck, that’s a lot.”

“Yeah. A fucking lot. Some lunatic must’ve even taken different tastes into account, because there are all kinds.”

“Damn it. So it wasn’t the realm of immortals. It was the Demon Realm.”

“Oh, that’s a separate place. I think I told you about it before.”

“……For fuck’s sake. What kind of world is that?”

“What kind? A shitty one. But do you know what?”

“What?”

“This place seems to be getting just as shitty as my homeland.”

Jeok Cheongang was silent for a moment after Jin Taekyung answered. Then he spoke.

“Yes. I think so, too. I suppose I’ve lived too long. To see a miserable sight like this.”

“Why say you’ve lived too long? Don’t jinx it.”

“Enough with the pointless worrying. I plan to live another fifty years.”

“That’s much better. Yes. You’d better.”

He forced a bright reply, but a massive boulder was already weighing down one corner of Jin Taekyung’s heart.

*Damn it.*

He silently surveyed the area. Familiar and unfamiliar faces alike filled his vision.

On every face, the whirlpool of complicated emotions they were feeling showed plainly.

Tension. Shock. Fear.

And, squeezed out with difficulty from those heavy, dark feelings, a handful of courage.

*How many of them will make it out alive?*

Jin Taekyung forced himself to erase the ominous question that had suddenly crossed his mind.

At least for now, even keeping every nerve trained on the enemy before him was more than enough.

“I have truly waited a long time for this day.”

The Eastern Heaven Demon Lord stood tall at the head and center of the army of the dead encircling the battlefield. He spoke slowly.

To everyone gathered there.

No—to the Emperor.

“Today, in this very place, the Great Nation will disappear.”

At that moment—

*Shhhhh.*

An inexplicable chill spread out.

A pale aura flowing from the Eastern Heaven Demon Lord’s entire body seeped like smoke into every corner of the battlefield.

No—it swallowed it up.

All in time with the sound of a bell, held in the Eastern Heaven Demon Lord’s hand.

*Jingle.*

The eerie chime rang out clearly. It reached not the ears, but the mind, and it was closer to a sound wave than a sound.

Most people whose martial arts realm was insufficient couldn’t hear it.

At the same time, the sound wave raised those who were no longer alive from the dead.

And by the time Jin Taekyung realized what was happening, he was already a step too late.

*Thump.*

“Old Master!”

“Stop.”

Jeok Cheongang grabbed Jin Taekyung by the shoulder as he was about to shoot toward the Eastern Heaven Demon Lord, and continued in a sunken voice:

“It’s already too late.”

“……!”

The next moment, Jin Taekyung’s eyes widened.

He understood what Jeok Cheongang meant by “too late” when the change began.

*Crick. Crrick.*

The ground trembled. As the vibrations grew stronger, the pools of blood rippled and the air turned cold.

*No, that’s not it.*

Jin Taekyung swallowed the gasp trying to burst out of him. His trembling eyes were fixed on the unknown corpse at his feet, shifting little by little.

*It’s not the ground that’s trembling… It’s the corpses.*

The countless corpses filling the battlefield. Thousands of them were waking up.

Returning to the world of the living, where they did not belong. Becoming something other than human.

“Hh…”

“W-what is this?”

“Attack before they—before those monsters get up! Hurry!”

*Thwack! Slice!*

The air grew colder, and with it the terror grew denser.

Yet the corpses refused to go down easily, even under the madly falling spears and swords.

Amid that chaotic turmoil, Jeok Cheongang thought of the legends of the Maoshan Sect, erased from Murim long ago, and looked at his Disciple.

“What do you call things like this, where you live?”

*Crunch!*

Jin Taekyung stomped on the corpse beneath his feet and answered through gritted teeth:

“Undead.”

*Grrr…*

A corpse with a throat split open lifted its head from a pool of blood. Even with its spine crushed beneath Jin Taekyung’s foot, it was still trying to rise.

“They’re monsters that aren’t dead, but aren’t alive, either.”

Jeok Cheongang nodded.

The pronunciation was unfamiliar, but the meaning was similar.

It was the perfect word for the monsters from the almost legendary stories that only the Maoshan Sect, among the countless sects and martial families spread across the land, had preserved.

*Monsters that aren’t dead, but aren’t alive, either.*

When he first heard stories about them, Jeok Cheongang had also thought they were baseless nonsense invented by gossipmongers.

It was simply impossible.

A grotesque legend that went directly against the natural order set by Heaven.

But now, that was no longer the case.

The unbelievable legend was right before his eyes.

“……Jiangshi.”

Jeok Cheongang murmured the word like a groan and reached toward the corpse twitching as it rose.

*Fwoosh. Boom!*

Despite the serious Internal Injury he had suffered, the blazing light-flames burst forth without dimming in the slightest. They dug into the skin of the thing that had crossed the river it should never have returned from, burning its bones and organs.

*Psssh. Splash.*

Jeok Cheongang stamped on the corpse as it crumbled to ash and melted into the pool of blood. Then he turned his head toward his Disciple.

“What in this world could remain unharmed by the Fire Gate Clan’s flames?”

“……!”

“Keep burning them. If they won’t die, burn them to ash until they do. Just as our sect’s ancestors did.”

Jin Taekyung stared at Jeok Cheongang with wide eyes, then replied with a deliberately serious expression:

“How did you know? That’s exactly what I’m best at.”

Master and Disciple smiled at each other, neither one waiting for the other.

Then they shot toward the corpses surging in from every direction.

One streak of flame. No—two streaks of flame.

As they listened to the eerie bell toll without end.

*Jingle. Jingle.*

*KWAaaaah!*

* * *

It was a clash between the dead and the living, a sight like a boulder falling toward an egg.

*GRAAAH!*

Undead. Jiangshi.

Or perhaps something else entirely. The corpses shot at the surviving humans from every direction, like spikes.

They weren’t stiff or slow like jiangshi, nor were they weak like undead.

That was precisely why they were strong.

*Crunch!*

“Hold the line!”

“For His Majesty the Emperor—!”

*Clang! Slice!*

Their loyal cries were swallowed without a trace.

The thousands of corpses that descended on the people forming a defensive circle like a shield moved as nimbly as they had in life. Their souls, captured by the sound of the bell, no longer feared injury or death.

*Crunch!*

“Aaagh!”

Crimson blood spurted like a fountain. The screams, as if wrenched from someone’s lungs, belonged only to the living.

Even when Sword Energy severed their arms, cut through their legs, or pierced their chests, the dead kept rising and advancing. Little by little, they were tearing down the humans’ formation.

Following the bell as it rang faster and more sharply. Carrying out the orders of its master.

*Jingle, jingle.*

The Eastern Heaven Demon Lord moved forward at a slow walk. Hundreds of dead, including Ma Sanbao, followed him. At the end of their path stood a high dais.

No—the Emperor.

“When the long and fierce age of warring heroes was drawing to a close, I was only thirteen.”

The Eastern Heaven Demon Lord muttered in a voice that hummed like a song.

His gray gaze drifted to the young king trembling beside the Emperor.

Barely in his early teens.

Even he, an old man and a monster who had ceased to be human, had once been called a boy.

“I was a sinner from the moment I was born. A sinner guilty of being born in an age of chaos—a sin that could never be washed away.”

The day his father, an ordinary farmer, and his two older brothers, both barely in their teens, were dragged onto the battlefield, the Eastern Heaven Demon Lord understood for the first time.

Misfortune didn’t come only to those who had sinned.

That having no wealth, no strength, and no spear or sword with which to fight back was itself a crime.

“And yet the rulers who put innocent commoners in front of spears and swords were not sinners. They were Heaven itself. Even as thousands and tens of thousands died on the battlefields they had created, they filled their bellies with rice and meat.”

The final blaze of that age of chaos had been magnificent. Those who proclaimed themselves kings of their own nations and Sons of Heaven fought most fiercely at the edge of the precipice.

And among the countless lives reduced to ash in that blaze were the father and two older brothers of the young Eastern Heaven Demon Lord.

His mother, too, who had been raped and killed after resisting the soldiers who came to conscript the boy, barely thirteen.

From that very day, the boy stopped crying.

Even a year later, after the final victor—who had ended the age of chaos with the sharpest and strongest spears and swords—ascended the throne.

Even when a Daoist recognized the wandering boy’s aptitude, took him as a Disciple, and brought him to the sect.

That was how he met his Master. He came to know his Senior and Junior Brothers.

What he found in the Maoshan Sect was not tears, but laughter. Happiness.

And that happiness ended in just a few years.

“Did you know?”

The Eastern Heaven Demon Lord stopped walking. Then he asked his enemy’s descendant, who was looking down at him from hundreds of steps above:

“What your grandfather, Taizu, did to us?”

*Jingle.*
## Chapter artifact 914

# Chapter 914

*Jingle.*

At the clear chime, which seemed to ring inside his head, the Emperor was suddenly seized by a splitting headache.

The Maoshan Sect.

It was a name that remained, however faintly, in his memory.

He and every other prince had studied the art of ruling, and they were expected to know the history of the Great Nation and the imperial family inside and out.

That history included records concerning the Maoshan Sect.

More precisely, the event known as the “Maoshan Rebellion.”

> **Third year of Pyeongjeong.**
>
> When His Majesty Taizu declared Nanjing in Jiangsu the imperial capital, the treasonous Maoshan rebels opposed the decision, rallied their forces, and rose against him.

The event received only a brief mention in the histories written by court historians, but its repercussions had been considerable.

It was an open revolt against the first Emperor, who had ended the long, fierce age of warring heroes and established himself as the continent’s final victor and an absolute ruler with boundless power.

*That was why he’d been more merciless than ever.*

Taizu, founder of the unified dynasty, was as cruel as he was great.

The day the imperial court received word that the Maoshan Sect, facing the loss of its ancestral home after generations of inhabiting it, had gathered its forces to oppose the relocation of the capital, Taizu immediately ordered his troops to march.

And three days later, the Maoshan Sect had disappeared from the world.

The mountain they had risked their lives to protect was engulfed in flames. Everything connected to those three characters—Maoshan Sect—was hacked apart by wave after wave of soldiers and thrown onto the pyres.

No distinction between humans and livestock.

No distinction between the living and the dead.

But…

*The records were wrong. Someone survived.*

The Emperor endured the pain stabbing through his skull and looked down the seemingly endless flight of stairs.

There, gazing back at him, stood the Maoshan Sect’s last surviving root—the one who had endured through the ages for this day alone.

His eyes burned with a hatred that could belong only to someone who had never once forgotten his grudge.

“I’ve always wondered why you wanted to destroy the imperial family and the Great Nation.”

The Emperor slowly rose from his throne. The hem of his long, ornate dragon robe brushed the ground.

*Swish.*

He walked forward at an unhurried pace. Baek Yeon, standing beside him, blocked his path with a rigid expression, but the Emperor did not stop.

*Step. Step.*

One step. Then another.

The Emperor descended the stairs, carpeted in crimson silk, and the two men who had once been bound together as ruler and subject drew closer to each other.

Until the Emperor stopped halfway down.

Until a quiet voice slipped through his cracked lips.

“So you betrayed the late Emperor—my father?”

“Betrayed?”

At the abrupt question, the Eastern Heaven Demon Lord laughed aloud.

His face twisted into a monster’s, at odds with the sound of his laughter.

“Who betrayed whom? I never gave you bastards my loyalty for even a single moment.”

He had waited an awfully long time for this day.

How many nights had he spent reliving his sense of betrayal and thirst for revenge?

How many buckets of blood had he spilled mastering the martial arts manuals his Master had entrusted to him as the sect faced destruction?

The boy had chosen to become a eunuch so he could bring down the impregnable fortress of the Great Nation by the surest means possible. Then one day, when he was a young man, an unwelcome visitor had appeared and made him an offer.

*“I bring you the words of the almighty and great Lord of Heaven.”*

And that day, the young man became part of the demonic army.

“Do you still not understand?”

The Eastern Heaven Demon Lord stared at the Emperor with cold, gray eyes.

“You’re not the ones who were betrayed.”

His father had often said that an age of peace and prosperity would come someday. His two older brothers had been dragged off to the battlefield as though they were captives, yet they had promised they would return alive.

And their mother, who had lost her husband and two sons, had believed that at least her youngest boy—far too young to be on his own—would survive.

But she had been wrong.

Every last one of their hopes had been betrayed.

The boy had lost his entire family. He had barely survived the battlefield he’d been forced into, only for a second happiness—one that had miraculously found him—to be stolen away.

“You betrayed me first.”

All of them.

“No—the whole world.”

*Jingle.*

“You betrayed us.”

The Eastern Heaven Demon Lord’s voice, cold from beginning to end, and his gaze alike began to seethe like molten lava.

To him, he was the one who had been betrayed first. The common people. The world.

His family had been lost in the desperate struggles of heroes dreaming of becoming kings and ministers. His Master and fellow disciples, who had become another family to him, had been hacked apart by countless spears and swords.

And there had been only one reason.

They had tried to protect their ancestral home, passed down through generations, in defiance of Taizu’s decree that no martial artists could live near the imperial capital.

That was all.

“That is why you must die.”

In the most miserable, most horrific way possible.

“For that one wish alone, I have endured and waited all this time.”

It had taken a very long time for the boy to become a young man, the young man to become middle-aged, and finally for his hair to turn white. But those years had not been wasted.

The mask of Cang Gong, which the Eastern Heaven Demon Lord had worn, was magnificent and powerful.

The East Depot’s intelligence network stretched across the world, and few among the civil and military officials who upheld the Great Nation had no connection to him.

As the Eastern Heaven Demon Lord and Cang Gong, he was second in power only to the Emperor.

He might not have worn a dragon robe, but he was another absolute ruler—second to one, above all others—and most of the court lay in his grasp.

Even the imperial family.

“I—or rather, we are…”

The Eastern Heaven Demon Lord’s voice boiled as he spoke to the Emperor looking down at him.

“The Great Nation.”

“……!”

“……!”

The air around them froze. At the same time, the worn bell in the Eastern Heaven Demon Lord’s hand began to tremble wildly.

*Jingle. Jingle. Jingle.*

Waves of sound, like the wails of ghosts, spread in every direction.

Louder. Farther.

Until they crossed the vast banquet hall and reached the stone walls covered in the bodies of the Imperial Guards.

Until they could raise those who already lay there in a pitiful state from the dead.

*GRAAAH!*

A roar that chilled the spine alone shook the night air. The monsters, now more ferocious and powerful, advanced in response to the sound waves ringing through their minds.

Toward the towering stairs. Toward the Emperor standing at their center.

And at the head of the surging wave of the dead was a man who had waited for this day alone.

“Now, let’s see it through to the end.”

With those words, muttered as if making a vow to himself, the Eastern Heaven Demon Lord took a step.

No—he shot forward in an instant, intent on tearing the Emperor to pieces.

If not for the voice that pierced his ear at that very moment.

“Stop.”

“……!”

“I know what you’re trying to do, but you’d better leave it at that.”

*Hummm.*

The air shuddered.

There was clearly only one speaker, but the voice came from several directions.

The Six-Harmonies Voice Transmission technique—one beyond the reach of all but the most exceptional Supreme Peak masters.

Feeling the terrifying internal energy behind it, the Eastern Heaven Demon Lord bit down on his lip.

He remembered the bitter events of more than a decade ago.

Then he fixed his gaze on the woman looking down at him from just behind the Emperor’s shoulder.

*So Gyo.*

She looked, on the surface, like nothing more than a beautiful, elegant woman. But the Eastern Heaven Demon Lord had already suffered a bitter defeat once before because of her intervention. He could feel it clearly.

Just how much power was contained in that slender body.

And, along with that, how much he himself had grown over the years.

But there was one thing he still had no way of knowing.

“Who the hell are you, woman?”

So Gyo’s image was reflected in the Eastern Heaven Demon Lord’s sunken gaze.

An unknown superhuman whose identity had eluded even the intelligence networks of Dark Heaven and the East Depot.

His greatest enemy, who had suddenly appeared one day and inflicted a wound on his body and soul that would never heal.

Even after the grave Internal Injury she had given him refused to heal, forcing him to turn himself into a jiangshi, he still could not be sure who So Gyo was.

“Answer me. Who are you?”

If she were a spy for the orthodox factions, she would not have stood by and watched while things reached this point. If she were a master secretly raised by the imperial family, she should have appeared to stop him long ago.

But So Gyo was neither.

Holding a weapon in each hand, its shape reminiscent of a curved saber, she continued to look straight at him with an untroubled gaze.

She had cast off the black robes that had once covered her from head to toe.

She had freely unleashed the immense power she had kept confined within her body.

*Fwoooosh.*

It was unmistakable. Overwhelming.

An unprecedented energy, made visible, rose strand by strand from all over So Gyo’s body. Her calm voice, at odds with the situation, rang out from all six directions.

“Well, I have my own circumstances, just like you do, so I’m not sure I should tell you for free…”

*Step.*

She walked forward slowly. At the same time, So Gyo’s gaze turned cold.

“If you bite down on a sword and kill yourself right now, I might think about telling you.”

“……!”

“Oh. Would that not kill you anymore?”

*Crack.*

The Eastern Heaven Demon Lord clenched his teeth without realizing it, but his feet, stopped in their tracks, would not move easily.

*Why?*

By now, he had achieved Great Completion in all of his sect’s supreme techniques.

The Maoshan Sect’s arts might have focused on various forms of sorcery, including the art of controlling jiangshi, but the Eastern Heaven Demon Lord had accepted death as his own and become a superhuman in a different sense.

And yet…

*She’s dangerous.*

He knew it instinctively. If he moved carelessly now, So Gyo would get the better of him.

Even though his body could not die or feel pain, his Qi Sense kept sending its master warning after warning.

“Master.”

His Disciple Ma Sanbao’s low voice pierced his ear, but the Eastern Heaven Demon Lord did not move. He simply stared at So Gyo without a word.

The aura he felt from her now was on a level with the Fire King, Jeok Cheongang.

Considering the full strength of the Eastern Heaven Demon Lord, even with the Emperor, Baek Yeon, and the Emperor’s hidden guards present, he still had a good chance of winning.

Strictly speaking, he judged his own martial prowess to be half a step below the Fire King’s or So Gyo’s. But he and all his forces could keep launching attacks as tenacious as a mutual death strike, thanks to their horrifying vitality.

Even if their arms and legs were cut off, even if their chests were pierced, they would not stop.

Not until every living person had fallen.

Not until the bodies of their enemies and the blood flowing through them had gone cold as ice.

*If I capture the Emperor and Prince Shangshan—or kill that woman—this will all be over.*

The battle to the death was not taking place in this hall alone. By now, the armies of the Great Nation, divided into two, would be fighting a bloody battle around the imperial capital, and his side would win.

The Eastern Heaven Demon Lord opened his tightly shut mouth.

“Go.”

*Jingle.*

At the moment the worn bell, a divine artifact of the Maoshan Sect, gave off a strange chime—

*Rumble!*

More than a thousand of the dead, once the elite soldiers of the Great Nation known as the Imperial Guards, charged across the banquet hall.

*GRAAAAH!*

And two streaks of light burst out toward the army of the dead surging like a wave, shrieking as it came.

*Shwaaah!*

Brilliant light flashed.

At the same time, the overwhelming Force unleashed by two superhumans who had stepped in front of the Emperor crushed and smashed the flesh and bones of the dead.

*CRUNCH!*

Their power was enough to crush the vanguard in an instant. But the Eastern Heaven Demon Lord, who knew their abilities well, was not the least bit surprised.

*I expected this.*

But humans, made of flesh and blood, were ultimately fated to perish.

Even those called superhuman had limits set for them as humans, however far beyond ordinary those limits might be.

*I’ll wait for an opening and kill them in one strike.*

With his gaze sunken deep, the Eastern Heaven Demon Lord moved forward.

His Disciple Ma Sanbao and a master of the Twelve Palaces of the Zodiac, returned from the dead, flanked him on either side as he climbed the stairs, now covered in rotten blood and shattered corpses.

*Splash.*

And at that very moment—

“Are you busy right now?”

At the voice from behind him, from quite a distance away, he suddenly realized that the howls of his followers, which had been ringing out in the distance, were beginning to die down.

He also realized that the limits he had assumed applied to superhumans might, perhaps, go even further.

*Swish.*

The Eastern Heaven Demon Lord turned around, his expression rigid. Reflected in his eyes were the faces of two men he hadn’t expected to see again so soon.

“Hey, ugly-ass big bro. If you’re not too busy, make some time for me.”

“Indeed. This old man will take very good care of you.”

Jeok Cheongang and Jin Taekyung, both looking like blood-soaked men, bared their white teeth and grinned.

They looked so much alike.

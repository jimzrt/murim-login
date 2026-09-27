# Checkpoint Review — 1030–1034

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

# Chapters 1030–1034

## Plot

The Blood-Sword Demon Lord uses the Three Elders of Tianshan as bait to draw Jin Taekyung’s forces from the Great Snow Mountain, then advances with tens of thousands of soldiers and seven soulless Death Knights called Black Ghosts. Taekyung, Jeok Cheongang, and Sama Pyo fight the Black Ghosts as the armies collide. Two Black Ghosts break through the Zhongnan Sect’s formation; one is the supposedly dead Black Axe Fiend, and the Wind-and-Cloud Sword Lord’s sword is shattered. Four Black Ghosts engage Taekyung and Jeok, while two likely head toward Zhongnan and one remains unaccounted for. The Black Ghosts regenerate from severe injuries, and some alter their attacks to avoid killing Taekyung, following the Blood-Sword Demon Lord’s orders.

An unnamed white-robed woman, who serves the Lord of Heaven more closely than the Blood-Sword Demon Lord, keeps him from joining the fight, saying the Lord wants him safe. He takes this as distrust and resolves to prove his devotion. Jeok Cheongang and Taekyung unleash Heavenly Strike, destroying the four Black Ghosts fighting them and the followers attacking them. The Blood-Sword Demon Lord draws his sword.

## Continuity

- The Blood-Sword Demon Lord commands more than thirty thousand soldiers and seven Black Ghosts. His new master, the Lord of Heaven, has ordered that Taekyung must not be killed.
- The Black Ghosts are powerful, emotionless fighters with extreme regeneration. One is the Black Axe Fiend, formerly one of the twenty-four great fiends who served the Heavenly Demon and believed long dead.
- Four Black Ghosts and the followers attacking Jeok Cheongang and Taekyung were destroyed by Heavenly Strike. Two Black Ghosts likely went toward Zhongnan; the seventh’s whereabouts remain unknown.
- The Wind-and-Cloud Sword Lord’s lifelong sword was shattered fighting a Black Ghost.
- Roughly twenty white-robed followers take orders from the Lord of Heaven through an unnamed woman. She says the Lord wants the Blood-Sword Demon Lord to avoid harm; he interprets this as distrust and is resolved to prove himself.
- The Lord of Heaven’s identity and purpose remain unknown; whether Dark Heaven caused the Great Faction War is unresolved.

## Translation Decisions

- Render 흑귀 as “Black Ghosts,” 흑부괴마 as “Black Axe Fiend,” 쇄겸 as “chain sickle,” and 천격 as “Heavenly Strike.”
- Retain “Supreme Mastery” for 등봉조극 and “Heavenly Vault Finger Qi” for 천궁지.

## Durable state

{
  "active_continuity": [
    "The Blood-Sword Demon Lord serves the Lord of Heaven and commands the invading army.",
    "The Blood-Sword Demon Lord commands more than thirty thousand soldiers and seven Black Ghosts.",
    "Four Black Ghosts and the followers attacking Jeok Cheongang and his disciple were destroyed by Heavenly Strike.",
    "Jeok Cheongang and his disciple are fighting on the battlefield.",
    "Roughly twenty white-robed followers take orders from the Lord of Heaven through an unnamed woman who served him more closely than the Blood-Sword Demon Lord.",
    "The Blood-Sword Demon Lord believes the Lord of Heaven distrusts him and is resolved to prove himself."
  ],
  "continuity_sources": [
    1034
  ],
  "open_questions": [
    "Who are the seven Black Ghosts, and what were their identities before becoming Black Ghosts?",
    "What is the Lord of Heaven’s identity and purpose?",
    "Did Dark Heaven cause the Great Faction War?",
    "Who is the unnamed white-robed woman, and what are the white-robed followers’ purpose?"
  ],
  "safe_through": 1034,
  "temporary_decisions": [],
  "version": 1
}

## Reading copies

## Chapter artifact 1030

# Chapter 1030

The day when common sense was invaded by the absurd had come and gone long ago.

Laws were broken, truths were torn down, and the word *death* had become cheap.

At least, that was the world in which one young man had been born and raised.

Monsters. Hunters.

Monsters and humans killing one another inside the boundaries between dimensions known as Gates.

Mana and magical power.

Miraculous forces that shattered the truths Earth had held since ancient times, and the laws discovered by a handful of geniuses who had shaped human history.

And a war that still hadn’t ended.

The young man was part of that world.

A world where people overturned the earth in the name of Magic, unleashed fire and lightning, and defied gravity.

Hunters who poured out dazzling auras as they faced monsters with grotesque forms and unimaginable strength—creatures described only in ancient myths, or beyond anything anyone could imagine.

Humans were adaptable creatures.

By the time the little child born on the day humanity won its great victory was approaching thirty, the absurdity that had overturned the world in the Great Cataclysm had become the new common sense.

That is, until another absurdity changed everything.

On a steep hill in the middle of summer, outside a goshiwon[^1], stood a recycling area.

A massive hunk of scrap metal had been dumped there.

No—it was a VR capsule, an entrance to another world.

With nothing to his name, one young man had stepped into that new world.

So much awaited him beyond the invisible veil.

Dangers and opportunities unlike any he’d known, and rewards.

He had formed bonds with good people, fought countless enemies, and grown because of it.

That was why the young man had wished so desperately for one thing:

That nothing out of the ordinary would happen here.

Perhaps that wish was why, as time passed, he kept trying to downplay and ignore the one suspicion growing stronger by the day.

At least, until this very moment, when he came face-to-face with the truth he didn’t want to believe.

“Death Knights…?”

The vacant words slipped from his lips.

The young man—or rather, Jin Taekyung—blankly lifted his head to look.

Entranced by the word he’d just spoken.

Overwhelmed by the unbelievable sight before his eyes.

Sssaaaaa.

Beneath the dark clouds hanging over the snow-covered mountains, a murky haze spread.

At its center, seven ghost horses soundlessly charged forward, stepping on empty air. On their backs sat seven men dressed not in armor that covered them from head to toe, but in black clothes as dark as pitch.

No—what he sensed was a presence of death as familiar as could be.

Its essence didn’t change, no matter what shape it took.

A deep, cloying aura of death, and its stench, seeped into every one of Jin Taekyung’s senses—even his soul.

*No mistake.*

For a moment, Jin Taekyung trembled without realizing it.

He’d been right. It was them.

Death Knights.

Knights who had given up their souls and forsaken their rest.

The absurdity of another world was invading common sense once again.

And yet, amid the two vast armies advancing toward each other even now, Jin Taekyung was the only one who had noticed.

“Retreat! Fall back, now—!”

Whoosh!

As he shouted at his allies, Jin Taekyung suddenly felt every hair on his body stand on end. He spun around.

A movement he’d repeated a thousand times—no, more than ten thousand.

Urgent, yet perfectly practiced, it followed the turn of his waist and arms. Dark-blue Force rose like a tidal wave.

KWAANG!

A deafening boom shook the air. Beyond the gray-white blade trembling where it met the spearpoint, a fiend gone mad with blood grinned at Jin Taekyung.

“Why not surrender while you still can?”

“I’ll return those words to you.”

The reply hadn’t come from Jin Taekyung.

Jeok Cheongang’s palm shot ahead of his quiet voice, flashing like a streak of light as it struck at the Blood-Sword Demon Lord’s flank.

Whooosh.

A blaze erupted in an instant, dazzling and scorching all at once.

Faced with the terrible heat of the Flame Divine Palm, which burned the air and melted ten-thousand-year snow, the Blood-Sword Demon Lord twisted aside without hesitation.

BOOM!

Compressed air exploded. No—it vaporized on the spot.

The Blood-Sword Demon Lord narrowly evaded the palm strike, leaping backward off the ground. It had been a successful dodge, by any measure, but the heat had still taken its toll. His collar and the skin beneath it were scorched black.

“Whoops. Well, look at that.”

Of all the pains in the world, burning pain was said to be the worst.

Yet even with his skin charred and parts of it melted into a mess, a smile still lingered on the Blood-Sword Demon Lord’s lips.

“Just as they said, you’re a fiery one, Senior.”

“You bastard…!”

“Don’t be so angry. I may speak this way, but it stings me too.”

The Blood-Sword Demon Lord wasn’t trying to provoke him. He meant it.

They’d clashed only once, but he’d felt it clearly.

He couldn’t defeat the Fire King, Jeok Cheongang, alone.

Even without Jeok Cheongang, a master half a step above him, capturing Jin Taekyung alive rather than killing him would be very difficult.

Of course, that was only true of how things stood now.

“I should ask your understanding in advance for what’s about to happen, Senior. And you as well, my friend. I’m not entirely fond of doing things this way, either…”

The Blood-Sword Demon Lord had furrowed his brow as if he were troubled, but soon he burst into hearty laughter and continued.

“What can you do? This, too, is part of proving that person’s greatness.”

At that moment—

Rumble, rumble, rumble!

The vast army of Dark Heaven had already charged to within roughly three hundred thirty yards. More precisely, the seven pairs of riders at the head of the countless fanatics rose into the air, stepping on empty space.

No—they ran.

Screee!

Everyone advancing to oppose them could see it plainly.

Tens of thousands of eyes widened. Lips that had been tightly shut fell open on their own.

Shock. Fear.

Only those two emotions showed on their faces and in their eyes.

What could they call this sight?

Stepping on Empty Air? Or Traversing the Void?

None of the words in anyone’s mind could easily explain it.

There were several masters on the Murim Alliance’s side who could use body-lightness techniques well enough to step on empty air. But no one had ever imagined running through the sky on horseback. It was an unprecedented wonder.

But one person was different.

*They’re coming.*

Jin Taekyung gripped White Flame.

He was more shocked than anyone else on the battlefield, yet he was also the one seeing reality most clearly.

A feeling both familiar and unfamiliar.

Called Death Knights in the modern world, these beings—whatever the Murim might call them—were closing in at blinding speed.

*They’re strong. Not ordinary ones.*

Jin Taekyung had sensed it. Their appearance wasn’t the only thing that had changed.

The closer they came, the stronger the stench and aura of death grew. They far surpassed the ordinary Death Knights he knew.

*Right, this is just like…*

Lei Fei.

Jin Taekyung suddenly remembered another hero, not so long ago, whose soul had been forcibly corrupted by an Arch Lich.

*The Death Knight Lord.*

Lei Fei had been an S-rank Hunter and a hero, but while corrupted, he had been the most powerful enemy around after the Arch Lich itself.

A chosen leader among Death Knights, one who’d kept all his strength from life—and grown even stronger.

A named monster who deserved the title of Lord without the slightest reservation.

But the seven men in black, leading ghost horses at the head of the enemy forces, each exuded an aura that was no weaker than Lei Fei’s had been.

*No. Stronger.*

It was already too late to turn back.

Fear was contagious.

The morale of Jin Taekyung’s allies, which had soared as they watched him defeat the Three Elders of Tianshan in an instant, was fading like a bubble before this sight no one had ever heard of or seen before.

*He drew the whole army out of the Great Snow Mountain. He used the Three Elders of Tianshan as bait.*

Jin Taekyung understood at last.

The Three Elders of Tianshan had been used as bait from the very beginning, for this exact moment.

And the Blood-Sword Demon Lord’s plan had worked perfectly.

Even if their allies retreated now, the enemy would reach them all the faster.

In the end, Jin Taekyung was left with only two paths.

Hold this position so their shaken allies could retreat before they even crossed weapons with the enemy.

Or…

*Risk everything and turn this around.*

And at Jin Taekyung’s side stood someone he could trust and follow more than anyone.

“How many will you take?”

“All eight.”

At Jeok Cheongang’s calm reply, Jin Taekyung gave a quiet laugh.

“That’ll be tough. You’re getting old.”

“Don’t worry. I’ve got energy to spare since I got younger.”

“I’m glad that Thousand-Year Snow Ginseng I brought you was worth it.”

“What was I supposed to do with that? Bring me Ten-Thousand-Year Snow Ginseng next time.”

“Do you have any shame?”

“Want to open me up and check?”

The Fire Gate Clan’s master and disciple stood at the heart of the battlefield like iron towers, waiting for the enemy.

About a hundred sixty-five yards away, the vast army that had gathered behind the Blood-Sword Demon Lord—whose face was flushed with excitement as he stared at them—surged past its commander and poured toward them.

“They’re swarming like a pack of dogs. Even the unorthodox faction would be impressed.”

At Jeok Cheongang’s mutter, Sama Pyo gave a dry laugh.

“Yes. I think so too.”

“Come to think of it, there’s one unorthodox brat right here.”

“I can’t deny that.”

“The unorthodox faction, is it? Do you truly think of yourself that way?”

“It doesn’t seem like the time for that question, but what can I do? I was born, and the whole world called me unorthodox. I suppose that’s just my lot.”

About a hundred yards.

The enemy’s shouts shook the air from every direction, making their ears ring. Sama Pyo tightened his grip on the sword and saber that had once belonged to the Three Elders of Tianshan, one in each hand.

“Listening to that is ridiculous. Are you an idiot?”

At the quiet voice in his ear, Sama Pyo’s body stiffened.

“What… did you say?”

“I asked if you’re an idiot. You.”

About sixty-five yards.

With tens of thousands of enemies making the air tremble with their auras, Jin Taekyung continued in a calm voice.

“You live the way you were born, let other people decide what to call you, and just go along with it—is that your life?”

“That’s…”

“Just live however the hell you want. Protect what matters to you. Do something good now and then. Then what does it matter if you’re orthodox, unorthodox, or part of the dark-path figures?”

Sama Pyo’s face went stiff.

Those unrestrained words.

That made them hurt all the more—and made him envy Jin Taekyung.

Unlike him, Jin Taekyung had been born with a path already laid out for him.

“What do you know about me to say something like that?”

“Of course I don’t know shit. How would I know what kind of life you’ve lived? You’ve never told me.”

“What?”

“But I know what kind of person you are.”

About thirty yards.

Clouds gathered; darkness fell.

Watching the shadows descend through the empty air, Jin Taekyung tossed out one short sentence.

“We’re here together now.”

“……!”

“I guess I’m pretty good at judging people. Right, Old Master?”

Jeok Cheongang didn’t answer, and Jin Taekyung didn’t wait for one.

About a year earlier, the Pavilion Master who had gladly accepted the Young Sect Leader of the Black Dragon Demon Gate when he’d come calling out of the blue swung the spear in his hand.

Whooosh.

A dark-blue tidal wave surged up, hot as hellfire and swift as a thunderbolt.

And as Jin Taekyung advanced without hesitation, Sama Pyo suddenly thought:

He looked dazzling.

KWA-BOOM!

[^1]: A goshiwon is a very small, inexpensive room-for-rent arrangement in South Korea.
## Chapter artifact 1031

# Chapter 1031

I didn’t wonder if I could do it.

I had to. I had to see it through.

Power came with responsibility, and the weight of that responsibility left no room to retreat.

That was why I was moving forward now.

Whoosh.

I lowered the First Elder, still in my grip, and planted my foot on the ground. In the same instant, I shot forward.

Ghost Illusory Slaughter Step.

The subtle art I’d learned from the greatest assassin of all time flowed through my feet.

My legs felt impossibly light. The wind brushed past me, then vanished without a trace in the heat radiating from someone nearby.

And the moment I tightened my grip on the shaft—

Swaaash!

The world slowed.

As seven streams of Force fell like lightning from the sky above, Jeok Cheongang and I flung out our hands at the same time.

KWA-BOOOOM!

With a deafening crash that seemed to split the sky, time—which had paused for a moment—burst forth like a raging torrent.

KRRRUNCH!

The ground flipped over from the force of the collision. My feet, light as air only moments ago, were driven back under a pressure of tens of thousands of pounds.

*Damn it.*

The instant our forces collided, I felt the difference in strength and clenched my teeth before I could stop myself.

I’d expected them to be strong, but this was beyond that.

Seven.

Not one, not two, not three—but seven Death Knights.

No, the men in black were far too powerful. They hadn’t merely kept all their former strength; they’d grown stronger still.

Their power was too much to withstand, even with Jeok Cheongang at my side.

“Hngh…!”

A muffled breath came from right beside me.

Jeok Cheongang was holding off four enemies alone, proving his title as the Fire King. But this momentary standoff was like a glass bottle on the verge of shattering.

Just as it was now.

SHWING! KRAANG!

The three spears and swords, shrouded in pitch-black Force, met the White Flame’s blade once more. The impact left me gasping, and I felt my knees bend on their own.

*They’re strong. The Three Elders of Tianshan don’t even compare.*

The Three Elders were certainly masters worthy of being called powerful. But my ability to defeat them alone hadn’t come from inheriting the Thunderbolt Saber King’s internal energy and gaining insight alone.

Sometimes a pack of wolves is more frightening than a single tiger.

The Three Elders’ infamy, built over all these years, came from the same reason as the wolves’.

Just like the Qilian Three Fiends, who had once followed the Western Heaven Demon Lord and drenched Sichuan in blood.

But the men in black, closing in on me with tremendous strength and momentum even now, were different.

They were tigers.

Unlike the Three Elders of Tianshan, each one could command an entire mountain range—or, at least, they must have been able to in the past.

And the worst part was that these tigers had lost their souls, grown even stronger, and were now moving as a pack at the command of one man.

“How do they seem, now that you’ve faced them yourself? Impressive, aren’t they? I call them Black Ghosts.”

Even with the enemy’s enormous roar drawing ever closer behind the vanguard of men in black—the seven Black Ghosts—the Blood-Sword Demon Lord’s voice rang clear.

So did his aura, growing more intense with each slow step.

“Don’t struggle too hard. I regret what must happen to Senior Jeok, but you’re a very important prize.”

I couldn’t see his face behind the Black Ghosts, but I could picture it, if only faintly.

The Blood-Sword Demon Lord smiling. His eyes shining with excitement at the sea of corpses and blood about to unfold.

“Who knows? If you surrender peacefully now, perhaps both master and Disciple can survive.”

Grrk. Grrrk!

Under the crushing pressure, I barely managed to force out my voice.

“Fuck… off!”

KWAANG!

I thrust the spear shaft upward. All three of their spears and swords flew into the air at once.

As much as four jiazi of internal energy and a body far beyond human limits let me repel the Black Ghosts’ combined attack, strengthened at the cost of their souls, if only for a moment.

And that brief opening was a chance that wouldn’t come again.

SHHK!

I swung with all my strength and cut them down.

More precisely, I cut three huge black horses in half—ghost horses, monsters powerful enough to be considered terrifying in their own right.

FWOOOSH!

Instead of the blood any living creature should have had, a dark mist burst out. Jeok Cheongang, who’d been barely holding on, gaped at the unbelievable sight.

“What kind of fucked-up—!”

I’d love to explain, but now wasn’t the time.

Taking advantage of the Black Ghosts’ brief loss of balance after suddenly losing their steeds, I charged the four who’d been facing Jeok Cheongang.

SHK-SHK! KAKAKANG!

I slashed, stabbed, and swung.

The men blocked all three lightning-fast attacks without difficulty. Waiting for them was Jeok Cheongang’s palm strike, wreathed in brilliant white flames.

“Die.”

Whoosh—BOOM!

The Flame Divine Palm shot forward, erasing even the sound of its passage. It struck one of the Black Ghosts.

The man took the blow square in the chest and flew back like a cannonball. Jeok Cheongang bared his teeth in a grin.

Or, at least, he tried to.

“Good. That’s one—”

—Grrr.

But then the Black Ghost, who should have died with his whole body scorched black, let out a strange groan and straightened up.

“…No, it isn’t.”

Perhaps the Flame Divine Palm’s force still lingered. Jeok Cheongang stared blankly as the Black Ghost staggered to his feet, then blinked at me.

“What the hell are those things?”

KWAANG!

I parried the sword of one of the Black Ghosts and let out a breath before answering.

“Death. Death Knights.”

“Great Hand, Great Hand, Shift-Head? What the hell are you talking about?”

Unfortunately, I couldn’t clear up Jeok Cheongang’s confusion.

Before I could say anything, every Black Ghost—including the one who’d just been knocked away—charged at once.

KWA-BOOOOM!

My ears rang. Pain shot through my wrist, and both my legs sank deep into the ground.

A terrifying pressure, as if Taishan itself were bearing down on me.

And just as Jeok Cheongang and I were trapped in a forest of steel, a fierce rush of air sounded from somewhere.

Whoosh—CLANG-CLANG!

A large saber swung by one of the Black Ghosts knocked away a dozen or so throwing knives. I could guess who had fearlessly jumped into this fight.

*Sama Pyo. You idiot. What the hell are you doing here?*

But there was only a hair’s breadth between courage and stupidity.

Sama Pyo was an idiot, but he was brave. He’d only distracted one of them, but even that gave us a little room to breathe.

“Old Master, now!”

“Damn it!”

Jeok Cheongang spat a curse and shot out his fist like lightning.

KRRRUNCH!

Flame-Extinguishing Divine Fist.

Flames erupted like an explosion, pushing back the weapons wrapped in black Force, if only for a moment.

Its earth-shaking power reached hundreds of feet in every direction. It was enough to hide, for a moment, the streak of light racing through the flames.

SHWING! THUNK!

A throwing knife had left Sama Pyo’s hand and sunk into one Black Ghost’s throat. The blade quivered.

Of course, I knew better than anyone that even that wouldn’t be enough to bring him down.

Pshk.

The Black Ghost pulled the knife out as if it were nothing. Taking advantage of the brief gap in the encirclement, I leaped back and spoke.

“You asked earlier, didn’t you? What exactly a Death Knight is.”

“……”

“They’re bastards like that.”

“……Shit. This is a fine mess.”

Jeok Cheongang sighed. Sama Pyo, who’d come up beside us, remained calm.

“What monsters.”

“Idiot. You should’ve fallen back earlier. What, did you come all this way for a good view?”

“I already regret it. But what exactly are they? Some kind of jiangshi?”

“Similar, but let’s say they’re a bit worse.”

Jiangshi would be a thousand times better.

If they were a Maoshan Sect specialty, then at least from the point of view of people in this world, they’d be native creatures.

But those Black Ghosts—the Death Knights—were an invasive species.

They would destroy the ecosystem and shatter every law and bit of common sense.

No—they already had.

*How could this happen…?*

I swallowed back a quiet groan.

How such a thing was possible no longer mattered.

The rules everyone had believed in had already crumbled, and we had to deal with the rubble.

That’s right. Not just a handful of individuals. *We* did.

Rumble, rumble.

The ground trembled. The roar that had shaken everything around us was now behind me, beside Jeok Cheongang and Sama Pyo.

“Infinite Life Buddha.”

The one approaching with a low invocation was the Wind-and-Cloud Sword Lord.

At his sides were the Roaring Fury Swordsman and the Taeeul Merciless Sword, fellow disciples under the same master, along with nearly a thousand disciples of the Zhongnan Sect.

And another man, his face set hard.

“So it comes to this.”

The Black Night King, Sima Gong.

With countless martial artists from Gansu at his command, his numbers were in no way inferior to the enemy’s. His eyes were fixed on us, cold and sunken.

No—more precisely, they were fixed on Sama Pyo.

His lips moved as though he wanted to say something, but in the end he shut his mouth without a word and looked straight ahead.

He looked straight at the rulers from beyond the desert, whom we had finally met on this vast snowy plain.

“Enough.”

The Black Ghosts, who’d been silently advancing toward us, all stopped at once. The Blood-Sword Demon Lord stepped forward, with an army of tens of thousands behind him.

Thud.

“Good. This is how you should meet me.”

Vrrrrm.

The gray-white blade trembled. Its color hardly suited the Blood-Sword Demon Lord’s title, though it had reaped carnage that ranked among the worst of the Great Faction War.

Dark-red Force surged from the blade, linking and binding together without pause as he leveled it at the men in his way—men who could no longer turn back and had no choice but to press forward with all their strength.

Aaaaaah!

Shouts and killing intent, fear and anger—all mixed together and swelled.

In the midst of that violent whirlpool of emotion, I took a slow step forward.

Crunch.

Cold. Frost broke beneath my toes.

Thump.

My heart pounded.

With each harsh, pounding beat, I quickened my pace.

Whoosh. SHWAAAAA!

The wind blew. The mild breeze became a raging gale, and I summoned that gale.

No—the whole battlefield did.

WAAAAAH!

Shouts, clouds, wind.

Beyond them, countless blades flashed.

And two vast armies raced across the dazzling white snowfield, colliding at last in its center.

KRRRUNCH!

The white snow turned red.

In the blood mist, swelling and spreading, superhumans shot toward one another, cutting through countless screams and deaths.
## Chapter artifact 1032

# Chapter 1032

It was like two enormous waves trying to swallow each other.

There were only a few differences: the setting was a vast snowy plain instead of the sea; the waves were made of countless people and flashing blades instead of water; and the spray that burst from their collision was red as blood.

No—it was blood itself.

KRRRUNCH!

Tens of thousands clashed with tens of thousands.

Like warhorses that had never learned how to back down, the two armies charged toward each other and, in an instant, became entangled. Weapons flashed in every hand.

CLANG! THUNK!

SHING!

With dreadful slicing sounds, a dense mist of blood spread through the air.

And through the snowy plain, swiftly blanketed in blood and screams, there were awls cutting fiercely through the heart of the battle.

“Infinite Life Buddha…”

Whoooosh.

The hem of a Daoist robe whipped violently, as if caught in a storm, under the force of an overwhelming aura.

The Wind-and-Cloud Sword Lord had split five enemies apart with a single sword strike. Now he brought down his blade at an angle, its body enlarged by milky-white Force.

Swaaash!

The sheer pressure warped the space around it. A towering blade of Sword Force swept through the enemies clad in black armor.

KWA-BOOOOM!

The ground flipped over with a deafening crash, and flesh and bone scattered in every direction.

Yet even after witnessing the grisly sight from point-blank range, the followers who had begun worshiping a new god called the Lord of Heaven didn’t so much as blink.

No—more precisely, they kept advancing, gazing at the Wind-and-Cloud Sword Lord with hazy eyes, as if entranced.

All the while murmuring the eight-word creed without pause.

“In heaven and on earth.”

“All demons bow in submission…”

CRUNCH!

Their hollow, almost chilling voices ended only when they died.

At least, that was what the Wind-and-Cloud Sword Lord believed in that moment.

Gurgle.

Blood bubbled between the man’s gaping throat and neck.

The follower, his throat cut by the Wind-and-Cloud Sword Lord’s strike, muttered as the light slowly faded from his eyes.

“Heaven above… gurgle… hea…”

THUNK!

The follower’s words stopped only when the Wind-and-Cloud Sword Lord drove his sword into the man’s chest. Watching him, the Wind-and-Cloud Sword Lord felt a chill creep down his spine.

*They’re no ordinary people.*

Of course they weren’t. Even back when the Heavenly Demon swept across the Central Plains, the hundred thousand members of the Demonic Path gathered under him had been half-mad fanatics.

But the enemies the Wind-and-Cloud Sword Lord had faced back then had at least known fear.

They, too, had possessed the emotion every human ought to have.

*But what in the world…*

Then, at last, the Wind-and-Cloud Sword Lord understood why this felt familiar.

Fear.

They had no fear.

Though they clearly knew he was a superior opponent they couldn’t defeat, the followers of Dark Heaven kept surging toward him, as though they had been born for this very moment.

Spraying blood-red gore instead of white sea foam.

Screeeee!

The tip of his sword swept toward the enemies closing in from every direction.

The Heavenly River Thirty-Six Swords.

The Zhongnan Sect’s emblematic supreme sword art swept across the battlefield. Faced with its razor-sharp Force, the enemies’ weapons and bodies were sliced apart like tofu, their pieces scattering across the snow.

SHING! THUD-THUD!

Corpses collapsed with sickening sounds of torn flesh.

Yet one enemy, his chest deeply cut along with one arm, didn’t crumple with a groan of pain. He reached out with his one remaining hand.

BOOM!

A sharp whistle split the air, and the hem of the Wind-and-Cloud Sword Lord’s robe burst apart.

He narrowly avoided the enemy’s palm strike, then thrust out his hand at blinding speed.

THUNK!

Only after the Zhongnan Sect’s famed Heavenly Vault Finger Qi pierced the man between the brows did his body crumple.

But even after dispatching dozens of enemies in less than a moment, the Wind-and-Cloud Sword Lord’s face remained rigid.

*This is…*

There was no doubt. They had no fear—and they barely felt pain, either.

He didn’t know whether they had used some kind of secret technique or a drug to cloud their minds, but this was clearly far beyond what common sense could explain.

And there were tens of thousands of them.

They felt neither fear nor pain, and each one was highly skilled. They were battle weapons made to sweep across a battlefield.

*This is bad. No—this is the worst.*

The Wind-and-Cloud Sword Lord bit his lip, feeling a fear he hadn’t known since the Great Faction War. Then—

Swoooosh!

Along with a rush of overlapping whistles, an immense force tore into one side of the battlefield.

KWA-BOOOOM!

A sudden crash sent countless scraps of flesh flying in every direction.

The Wind-and-Cloud Sword Lord’s eyes widened as he watched the scene. The Zhongnan Sect Disciples, who had formed a tight sword formation around the Roaring Fury Swordsman and the Taeeul Merciless Sword, had their formation shattered in an instant.

“No!”

“J-Junior Sister!”

Their cries were like screams.

Shocked beyond measure by the loss of a fellow sect member they’d known since childhood, they stared blankly at the enemy who had broken their steadfast formation in a single blow.

Two men, covered in pitch black from head to toe.

No—the Blood-Sword Demon Lord had called them Black Ghosts, and the name suited these unknown beings all too well.

Sssaaaaa.

Black energy curled around their bodies and rose in threads, swallowing the air.

Without realizing it, the Zhongnan Sect Disciples began to tremble. The energy clutched at their hearts and bound their limbs.

“Hngh…”

Strained breaths escaped from all around.

Everyone was crushed beneath their chilling aura—an overwhelming force known as *Fear* somewhere far away.

No—almost everyone.

SHWOOF!

The Wind-and-Cloud Sword Lord erased the space between them in an instant, his fury more violent than ever.

Dozens of Disciples had died in the blink of an eye.

The people he was duty-bound to protect as Sect Leader—the future pillars of the Zhongnan Sect whom he’d watched grow since childhood—had been mercilessly cut down in an instant.

“How dare you!”

SHWING-SHWING-SHWING!

The sword tip, charged with fury, cut through the air. The Heavenly River Thirty-Six Swords had reached nine-tenths of its mastery. Dozens of sword images poured forth.

Then vanished without a trace.

Whoooosh! CLANG!

The moment the enormous forces collided, the Wind-and-Cloud Sword Lord’s eyes widened.

His beloved sword, which had cut through the wind, was being knocked aside by an axe blade swinging with the wind, erasing his sword images as it swept through them.

“What is this…!”

GRRRK. KWAANG!

Before the Wind-and-Cloud Sword Lord could finish his cry of shock, the blade finally gave way to the immense force and was sent flying. It trembled violently.

KRRUNCH!

The Wind-and-Cloud Sword Lord slid back, his foot carving a deep furrow in the ground. He barely steadied himself, pain stabbing through his wrist.

Far worse than the pain was the shock.

“Y-You…”

The words stumbled from his parted lips.

He stared at the Black Ghost gripping a massive battle axe as large as a grown man. The Wind-and-Cloud Sword Lord’s eyes bulged as though they might pop out.

*No. It can’t be.*

He tried to deny it, but the reality before him said otherwise.

That Black Ghost had stopped the Zhongnan Sect’s Sect Leader single-handedly. The face was unmistakably familiar.

He hadn’t recognized it at first. Now he did.

The crude weapon, so strange it was almost grotesque. The features, horribly twisted and discolored, but still bearing faint traces of what they once were.

“…Black Axe Fiend.”

The Wind-and-Cloud Sword Lord murmured, stunned.

A great fiend of the Demonic Cult who had once faced him and his Master on the battlefield, long ago. A Supreme Peak master who had first instilled in him the fear of death.

And…

“He should have died.”

One of the twenty-four great fiends under the Heavenly Demon, who had met his end right there on that day.

“Then, then how…?”

It was impossible. It should never have happened.

But the Wind-and-Cloud Sword Lord’s questions went unanswered.

The next moment, a fierce rush of air came sweeping toward him, dragging him back to reality.

Screeeee—CRUNCH!

A head. Blood spraying into the air.

A middle-aged first-generation Disciple—one regarded as a future Elder—was beheaded in a single stroke. Gritting his teeth, the Wind-and-Cloud Sword Lord kicked off the ground.

“Senior Brothers!”

At his shout, strengthened by internal energy, the Roaring Fury Swordsman and the Taeeul Merciless Sword finally moved. They had been frozen after belatedly recognizing the Black Axe Fiend.

Fwoosh!

Their figures blurred. Their movement techniques made their feet as light as feathers.

But the Wind-and-Cloud Sword Lord’s heart was heavy as he shot toward the Black Axe Fiend, returned from death under the new name of Black Ghost, and another Black Ghost radiating an aura no less immense.

*Could it be? Could it be…*

*Today might be that day.*

He had long since entered the ranks of the superhuman. And though the two Senior Brothers were poor Daoists, they were fine martial artists.

So why?

Why did he fear those two, even with his Senior Brothers and nearly a thousand Disciples at his side?

*…Infinite Life Buddha.*

The Wind-and-Cloud Sword Lord thought of death, a word he’d prepared himself for when he left Mount Zhongnan, yet still struggled to accept. Then he thrust out his sword.

SHWAAASH!

And as a murky-black axe blade swung down to meet the sword strike that warped space—

KWA-BOOOOM!

A colossal impact far beyond his expectations struck. Suddenly, the Wind-and-Cloud Sword Lord understood.

His fears had not been mere fear.

He was not the one who could decide the outcome of this battle.

KRRUNCH.

In a world that had slowed, the Wind-and-Cloud Sword Lord watched his beloved sword, which had been with him all his life, shatter to pieces. An image of someone came to mind.

Someone who wasn’t the strongest person in the world, but who had always brought winds of change no one could have predicted.

And a young man who was moving ahead of everyone else.

*Jin Daoist Friend.*

At that very moment—

KWA-BOOOOM!

A wave of magical power, darker than storm clouds and thick as blood, swept in every direction.

* * *

Rumble…

At some point, a distant crash rang out from somewhere behind me. I forced my head to stay facing forward, even as instinct urged me to turn.

Swoosh—thunk!

An arrow passed my side by a finger’s breadth and buried itself in an enemy approaching from my blind spot.

The shot had clearly been infused with internal energy, but the bastard charged at me as if he hadn’t felt a speck of pain, swinging his curved saber with a crimson blade of Saber Force forming along it.

No—he tried to swing it.

Thwack!

Following the foot I’d snapped out a beat earlier, I felt the bones shatter.

He was obviously out of the fight.

But I didn’t stop there. I flung out one hand at the bastard, slumped to the ground with his shin crushed.

*Inventory open. Summon.*

A dagger appeared in my empty hand. I hurled it the instant my fingers closed around it. The flash of its blade flew straight for the spot between the enemy’s brows.

Thud. Thump!

By the time I heard him fall, I’d already moved another three *jang* ahead.

And beside me was the Fire King, Jeok Cheongang.

KWA-BOOOOM!

Flames hungrily devoured everything in their path. Flesh melted in the terrible heat.

All around us, screams gave way to steam and a stench that filled the air. Just then, a fierce rush of air reached my ears.

Screeeee!
## Chapter artifact 1033

# Chapter 1033

Every martial art contains at least dozens of movements, each with its own underlying principles.

But no matter what martial art you’ve learned, there are ultimately only two ways to deal with an enemy’s attack.

Block it, or dodge it.

And in this moment, I chose the latter.

KWA-BOOOOM! KRRRUNCH!

A flash of light came hurtling in with a fierce whistle and slammed into the ground.

The earth’s surface flipped over as if an earthquake had struck, and a tremendous shock wave swept through the area.

At least a dozen enemies were caught in its wake and vanished without a trace. Yet all I’d suffered was a few scratches from flying bits of rock—and my spine still went cold.

*Fast. And powerful.*

It was hard to believe a javelin could move that fast and hit that hard after being thrown from so far away.

In that sense, dodging had hardly been a choice. I’d had no other option.

If I’d counterattacked at once, even that would have cost me a considerable amount of strength.

Jeok Cheongang, standing beside me, knew that too.

“I suspected as much, but those bastards certainly don’t have ordinary internal energy.”

Jeok Cheongang muttered in a low voice and clenched his fist.

In the distance, in the direction of his gaze, four ghost horses were approaching us, each carrying a rider. They stepped through the air as they came.

“Four, huh? How many passed us by earlier?”

The Great Snow Mountain region might not be as vast as the Qilian Mountains, but it was still enormous.

The land at the foot of the mountain, lightly covered in frost, was broad enough for a massive battle like this one, with countless enemies and allies tangled together. Jeok Cheongang and I had broken through the enemy lines ahead of everyone else like a single awl, but we couldn’t stop them all.

Besides, the most important thing in winning a battle was cutting off the head, not the body.

“If I saw right, two.”

I recalled the distant crash and tremor I’d felt before the javelin came flying.

Judging by their direction and distance, they were…

“I think those two headed toward the Zhongnan Sect.”

The Zhongnan Sect had only a thousand soldiers among our army of thirty thousand, but every one of them was an elite of the main sect, not an affiliated branch. With three Supreme Peak masters among them, they were a formidable force.

If the enemy wanted to secure victory, stopping them would be crucial.

“Then that makes five, counting the ones who’ve just appeared.”

We’d already let two slip past, and now four more had shown up.

But the monsters called Death Knights—or Black Ghosts—numbered seven in all, as far as we knew.

I adjusted my grip on White Flame and murmured, “One’s unaccounted for.”

“Then the last one…”

“Either guarding the Blood-Sword Demon Lord, or headed toward the Gansu martial artists led by Sima Gong. Unless it’s the latter…”

I let my voice trail off, but Jeok Cheongang already knew about Sima Gong’s suspicious behavior. No more explanation was needed.

“So that means Sima Gong, that damned unorthodox bastard, has thrown in his lot with Dark Heaven.”

That was right.

The fact that a Black Ghost hadn’t gone to Sima Gong’s side didn’t prove anything on its own, but there was no denying the likelihood of betrayal had risen sharply.

If I were the Blood-Sword Demon Lord, I wouldn’t bother sending a Black Ghost to Sima Gong if he was already an ally.

And besides…

*With power like that, all the more reason.*

I watched the Black Ghosts draw closer, radiating a terrifying aura.

They carried a saber, a sword, a spear, and a kusari-gama—a sickle attached to a chain. They sprang over the heads of the advancing enemy soldiers and shot toward us.

Each one was a Supreme Peak master powerful enough to shake an entire city.

On top of that, they felt neither pain nor emotion, and their ability to recover was beyond human. No—they were already complete monsters.

The likes of which no one in Murim had ever encountered.

“Old Master.”

“Nothing more to say.”

KRRUNCH!

Even now, Jeok Cheongang smashed the head of an enemy charging at him with soulless eyes in a single punch. Then he continued,

“I don’t know what kind of monsters those things are, but all we have to do is keep killing them until they’re dead.”

The instant those words slipped quietly from his lips—

Pop.

We kicked off the ground and shot forward, swinging and thrusting with all our strength.

I drove the spearhead of White Flame, its dark-blue Force surging around it. Jeok Cheongang thrust out a palm wreathed in pure white flames.

FWOOOOSH!

A brilliant flash enveloped everything within a radius of more than ten *jang*. The waves of fanatics that had been flooding in from every direction split apart.

No—they evaporated.

KWAANG! KRRRUNCH!

The ground shook with a crash that sounded as if the sky itself had split.

Bodies charred in an instant beneath the Flame Divine Palm’s terrible heat crumpled lifelessly. Others were cut apart along with their weapons, then flung in pieces through the air.

Even though they’d been stripped of pain and emotion, death came equally to the hundred or so enemies whose lives ended in that moment.

And through the gap in the battlefield, blanketed in death in an instant—

Ssshh…

Four Black Ghosts came rushing toward Jeok Cheongang and me, shrouded in a deathly energy like twilight fog.

SHWING!

The wind split around the blades as they swept through the air with crushing force.

Each of them took one of the four directions and struck. Their attacks meshed like the teeth of finely crafted gears, leaving not even the slightest opening.

But…

*There is an opening. There has to be.*

I took a bold step forward against the sword blade and spearhead rushing toward me, leaving faint afterimages.

Toward those two chilling flashes, aimed straight at my neck.

I steadied the conviction in my heart even as fear of death chilled my spine.

“What are you—!”

And just as Jeok Cheongang’s urgent shout rang out—

Pshk!

The two blades grazed the sides of my neck, cutting them so slightly that I felt no more than a moment’s pain. I curled up the corners of my mouth.

*Just as I thought.*

I hadn’t dodged their attacks.

In the life-or-death moment just now, the two Black Ghosts had forced their weapons to twist and change course.

Why?

Simple.

They weren’t allowed to kill me.

Their commander on this battlefield—the Blood-Sword Demon Lord—had given them that order.

*The Three Elders of Tianshan wouldn’t have been able to do that.*

No, I take that back.

They wouldn’t have done it.

Unlike the Black Ghosts, they still had their emotions and reason. Their own lives would have mattered a hundred, a thousand times more to them than carrying out an order.

They would have known that making even a tiny mistake like this to capture me would lead straight to their deaths.

Just like now.

SHWOOOSH!

I didn’t miss the opening that had been invisible until they exposed it themselves.

THUD!

The Black Ghost’s body went rigid, like a statue.

As White Flame’s spearhead pierced its throat, the four jiazi of Scorching Yang Qi I’d poured into it erupted.

KABOOOM!

Flames exploded.

Before the Black Ghost’s body, its head blown clean off, could fall from the saddle, another Black Ghost belatedly realized its comrade was in danger. It twisted the saber that had just passed beside my neck and swung it at me.

SHNK!

Hot. Even the force of the wind sliced into my shoulder, and red blood gushed from the wound.

But when you lose something, there’s always something to gain, too.

KRRUNCH.

A touch so cold it sent a shiver through me.

I seized the wrist of the Black Ghost, its body encased in jet-black armor, with my other hand. Without hesitation, I twisted it as if to wring it out.

CRACK. KRRUNCH.

Flesh and bone crushed with a sickening, wet sound.

If the Black Ghosts had gained greater strength by dying and being reborn, then I’d surpassed human limits by surviving countless brushes with death.

So the Black Ghosts weren’t the only monsters standing here.

KRRRUNCH!

I tore off its wrist, weapon still gripped in its hand, and punched the Black Ghost as it stood frozen in confusion.

KWAANG!

The body went flying, trailing a foul, burnt stench as its black armor shattered.

But I knew.

I knew what kind of monsters they were.

I knew how tenacious and dreadful the cursed life they’d been given was.

Step.

Leaving Jeok Cheongang behind as he fought two other Black Ghosts, I walked toward the ones now staggering back to their feet.

“Fine. Let’s see how this goes.”

Ssshh…

The monsters were wrapped in a rising, dusky mist that regenerated their arms, torn brutally away; their flesh and bones, melted and crumbled by the flames; even their missing necks.

“Let’s see which of us is the bigger monster.”

SHWOOOOSH—SHNK!

Fire Dragon’s Single Tail.

The dazzling white spearhead blazed like a flame. Its strike cut through the mist like a bolt of lightning, turning into a dark-blue wave that cleaved through the Black Ghosts.

* * *

“Magnificent. Absolutely magnificent!”

Like a child who’d just been given a toy he loved on his birthday, the Blood-Sword Demon Lord watched the battlefield spread before him, his face flushed with excitement.

CLANG-CLANG-CLANG!

From the high hill to the snowy plain in the distance, a mountain of sabers and a forest of swords stretched for hundreds of *jang*. They danced. Those gleaming blades, forged and tempered for one purpose alone, were finally playing their part.

THUD!

“AAAGH!”

Shouts and screams poured in from every direction as crimson blood sprayed over everyone’s heads like a fountain.

Dozens of lives vanished with a single breath in—and the gaps they left were filled with a single breath out.

Even now, death followed death without end across the horrific battlefield. It was enough to stir the nostalgia of someone who’d spent so many years confined to the lands beyond the desert.

“This is it. This is what I wanted…”

The Blood-Sword Demon Lord murmured in a half-dazed voice. His eyes had grown hazy and moist.

How he’d missed it.

How he’d longed for it.

In the distant past, he’d led a hundred thousand followers of the Demonic Path across the land at the side of the one called the Heavenly Demon. But those memories weren’t especially pleasant for the Blood-Sword Demon Lord.

Even back then, he’d been nothing more than a hunting dog mad for blood, and the Heavenly Demon had given him little authority to command.

But now things were different.

His new master had given the Blood-Sword Demon Lord the power to decide the lives and deaths of tens of thousands.

All he’d been given was one simple condition: under no circumstances was he to kill Jin Taekyung.

*To show me such absolute trust…*

The decisive proof was the seven Black Ghosts he’d been given.

And besides…

*With them there, there’s no way we can lose this battle.*

The Blood-Sword Demon Lord finally looked away from the battlefield and turned his gaze toward the white-robed figures under heavy guard not far away.

They were no less powerful than the Black Ghosts. If anything, they might be an even greater force.
## Chapter artifact 1034

# Chapter 1034

From head to toe, they were dressed in white so pure it felt out of place. Among the followers of Dark Heaven, clad in pitch black, they stood out at once.

Their sleeves were not merely voluminous—they trailed so long they dragged on the ground. A veil hid most of each face.

Wrapped head to toe in garments less like clothes than great swaths of silk, they silently watched the battlefield. Even to the Blood-Sword Demon Lord, they were unfamiliar.

No—in a way, they made him uncomfortable.

Unlike the Black Ghosts, his former comrades who had shared a bowl with him before becoming blind killing machines, those people took their orders not from the Blood-Sword Demon Lord, but from “that person.”

*If that had been all there was to it, perhaps I could have lived with it.*

The Blood-Sword Demon Lord’s eyes had been alive with excitement as he watched the battlefield turn red with blood. Now, a trace of displeasure crossed them.

*To have such a magnificent battlefield right before me, and do nothing but watch.*

It was more than displeasure. He was beginning to feel downright offended.

His gaze passed over the twenty or so white-robed figures, then came to a sudden stop on one of them.

And at the same moment, the Blood-Sword Demon Lord remembered.

A mere fifteen minutes earlier, he had eagerly stepped to the front, only for a quiet voice to stop him.

*“Demon Lord, please be patient a little longer. The time is not yet ripe.”*

If anyone had said that to the Blood-Sword Demon Lord during the Great Faction War, he would have torn the mouth off the fool spouting such nonsense and ripped out his tongue.

But fifty years was a very long time, and in the meantime, the Blood-Sword Demon Lord had grown a little more mature.

More precisely, fear and reverence for his new master, the Lord of Heaven, had held him back and suppressed his murderous impulse.

*Damn it.*

The reason that slender white-robed figure—whom the Blood-Sword Demon Lord was still glaring at—had survived after daring to interfere with him was simple.

*If not for that person.*

The figure led the white-robed group and had served the Lord of Heaven even more closely than the Blood-Sword Demon Lord himself.

So even a born killer like him couldn’t easily strike over a mere slight.

Of course, that didn’t mean the Blood-Sword Demon Lord had the patience to swallow down the irritation festering inside him.

“They’re holding up rather well. If I’d stepped in sooner, the tide of battle would already have turned.”

The words dripped with open mockery.

But neither the white-robed figure he’d singled out nor anyone nearby answered.

That was more than enough to stir the anger he’d been struggling to keep in check.

“Isn’t it strange? When you shouldn’t have stepped in, you did so without a care. But now you’re acting like you’ve swallowed your tongue.”

His pupils, slit vertically like a snake’s, narrowed further at the white-robed figure he’d been watching all along.

“Or does that mean you’d like to stay silent forever?”

At the sound of his low, flat voice, the figure’s tightly closed lips finally parted.

No—*her* lips.

“What answer do you want from me, Demon Lord?”

Her reply was calm, not a tremor in her voice.

Her composure was the opposite of his, and the Blood-Sword Demon Lord’s brow twitched.

“I’m in command here. I came this far to carry out that person’s will.”

“I know. I was there, too.”

“And yet you, a mere woman, dare to give me orders?”

“I did not give you an order. I only tried to dissuade you.”

Beneath the pure-white silk veil covering her face, her cherry-red lips moved again.

“And that is what that person wants, too.”

“……!”

At the unexpected reply, the Blood-Sword Demon Lord’s face went rigid.

“What…… did you say?”

“I said that is what that person wants.”

“That person—the great Lord of Heaven—doesn’t want me to step in? What in the world does that……?”

The Blood-Sword Demon Lord trailed off, unable to believe what he was hearing. The woman gave a small shake of her head.

With the motion, the pure-white veil, its beautiful yet uncanny pattern embroidered in colored thread, swayed softly.

“You misunderstand. That person only wishes for you to avoid harm, if possible.”

“Avoid harm? Me, of all people?”

For a moment, the Blood-Sword Demon Lord thought he’d misheard.

It was an unbearably humiliating thing to hear—as a martial artist, and as a subordinate who had devoted himself wholeheartedly to serving someone.

He commanded more than thirty thousand demonic soldiers and, though they were useless now, the Three Elders of Tianshan—the three hunting dogs.

On top of that, he had seven Black Ghosts at his command.

And that wasn’t all.

He hadn’t yet revealed the full extent of his strength, but the Blood-Sword Demon Lord himself had reached the realm of Supreme Mastery, making him one of the greatest masters alive.

And the enemy?

They were inferior in every way, with nothing that could compare.

The number of Supreme Peak masters who could turn the tide of battle. The quality of each soldier. And, finally, their momentum.

The scales had already tipped.

They had been tipping rapidly before the battle began, and they were still tipping rapidly now.

So why was that woman saying such nonsense?

Why was she hurling a boulder into his heart, cracking his conviction that he had his master’s complete trust?

“Can you stake your life on what you just said?”

His voice and gaze had gone cold.

But the woman’s reply was hardly different from before.

“That person’s care for you is as vast as the sea. Please try to understand their intentions.”

It was as good as an admission.

A faint smile came to the Blood-Sword Demon Lord’s lips.

“That person cares for me. Fine. Then I ought to understand.”

The smile on his face didn’t look like a smile at all. The woman’s voice turned urgent.

“As you know, four Demon Lords and Demon Empresses have already met their ends. That person needs at least one more loyal servant to carry out their great cause…….”

“Enough. All you’re trying to say is that I shouldn’t rush in.”

“……Demon Lord, that isn’t what I—”

“Enough. Hold your tongue. I understand that person’s wishes perfectly well now.”

The Blood-Sword Demon Lord spoke calmly, but his thoughts, after the storm that had swept through his mind, were anything but.

*You are watching me yourself, and this is all you think I’m capable of?*

Crack.

The joints in the hand he’d clenched with all his strength popped. His nails began to dig into his skin, drawing blood from his whitening fist.

*I…… have been loyal to you with everything I have. I followed you more faithfully than anyone.*

He remembered the day he first met the Lord of Heaven.

He remembered as clearly as if it had happened yesterday the tremor brought on by a fear and reverence beyond imagining, the shock so great it felt as if his heart might stop.

*Though I never received the important post I wanted, I spent more than fifty long years living solely to serve your great cause.*

The Great Faction War.

When the Heavenly Demon met his end at the Martial God’s hands, near the close of that long war, the Blood-Sword Demon Lord hadn’t been shaken in the slightest.

Of course he hadn’t.

The Heavenly Demon he’d watched was only human, after all.

The grand ambition that had once seemed so vast, the formidable martial might that had crushed the young Blood-Sword Demon Lord to his knees—it had all faded after he met the Lord of Heaven.

That was why he hadn’t felt even a trace of sorrow.

He’d been glad, instead, to have found a master truly worthy of his service.

Until, in the new power that had arisen under the name Dark Heaven, five other great fiends had taken seats above him.

*Even then, I simply obeyed you.*

He’d understood without a word.

The Western Heaven Demon Lord had once outranked him within the Demonic Cult, and had a valid claim to his position. The Eastern Heaven Demon Lord and North Heaven Demon Lord were daggers planted deep in the Central Plains, and deserved their high standing for the importance of their roles.

He understood the Southern Heaven Demon Empress, too. And the Blood Lord.

Discontent had taken root in his heart, but that had been his master’s will.

But……

*Now, before it was too late, you should have trusted me at least a little.*

The four Demon Lords and Demon Empress the Lord of Heaven had trusted so deeply had all met their ends. They had failed their missions spectacularly, then left this world before anyone could even call them to account.

At last, it was the Blood-Sword Demon Lord’s turn.

Together with the Blood Lord, who had stubbornly survived, he had finally become one of the Lord of Heaven’s two arms.

Whether he was the right arm or the left didn’t matter much.

What mattered more than anything to the Blood-Sword Demon Lord was his master’s trust and the opportunity he’d been given.

That was all.

*But what was there to worry about so much?*

None of the Demon Lords and Demon Empresses who were now dead had commanded an army like the one he led. They hadn’t had seven Black Ghosts, or tens of thousands of soldiers.

Yet their master didn’t fully trust him—the one who had everything needed for victory, conditions none of them had possessed.

Through the mouth of that woman in snow-white robes, he could read his master’s distrust of him.

“Was I really so unworthy of your trust?”

The sigh that should have stayed in his heart finally became a sound, slipping between his lips.

KWA-BOOOOM!

A pillar of fire shot skyward with a roar that seemed to split the heavens.

It was visible even from dozens of *jang* away, where the Blood-Sword Demon Lord stood. In fact, there was nowhere on the battlefield it couldn’t be seen. It was immense and raging.

And more merciless than anything else.

GRRRRRR!

A violent tremor traveled through the ground.

Before the roar even reached him, the Blood-Sword Demon Lord sensed a sudden wave of power and turned his head. He took in the scene and murmured calmly.

Once again, he spoke to the master who wasn’t there.

“If you’d trusted me just a little more, this battle might already have been over.”

“Demon Lord……!”

“Why? Am I not allowed to grumble this much?”

Without turning at the woman’s urgent cry behind him, the Blood-Sword Demon Lord replied as he watched the distant haze rising into the air.

More precisely, he watched the two figures streaking through the terrible heat that had given rise to all that haze.

KRAK, BOOM!

Fire King Jeok Cheongang.

With each punch and palm strike, the murky black fog burst apart.

The moment the fog gathered to recover from those devastating blows, dark-blue Force slashed in every direction.

SHHK—KWA-BOOOOM!

Four Black Ghosts staggered without pause.

Dark energy welled from the severed ends of their limbs like blood of a different color. Their appearance was unmistakably that of humans on the verge of death.

No—the Blood-Sword Demon Lord realized it instinctively.

Eternal death was finally coming for them, too.

Goooooong.

Space suddenly began to distort. Great Force surged around the white spearhead, rising and rolling in waves.

Like……

*A dragon.*

And at the moment the Blood-Sword Demon Lord muttered those words to himself, the spear, now one with its master, fell toward the Black Ghosts like a bolt of lightning.

SHWAAASH!

Heavenly Strike.

When that distant flash and its devastating force had passed, painting and shaking everything within dozens of *jang*, nothing remained.

Not the four Black Ghosts. Not the followers who had kept charging at the master and his disciple without pause.

And yet something remained: the resolve of a certain born killer, determined to prove himself to his master.

SHING.

A sharp sound brushed the Blood-Sword Demon Lord’s ear.

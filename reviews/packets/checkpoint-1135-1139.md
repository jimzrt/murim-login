# Checkpoint Review — 1135–1139

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

# Chapters 1135–1139

## Plot

The Son of Heaven and Zhuge Feng reveal their trap against Ma Sanbao’s forces. The Son of Heaven kills Ma, explaining that Jin Taekyung gave him the White Illusion Jiangshi Art and that he accepted it to remain with Zhu Bao. The allied forces then crush the Dark Heaven troops attacking the Moving Formations. The Emperor declares the nation Great Ming and orders a personal expedition to Xinjiang.

Seven days after the battle, the coalition prepares to march west against the Lord of Heaven. The Slaughter Saint remains troubled by the Bow Saint’s conduct when Taekyung was near death; the search for an unnamed target also continues, with fewer people assigned to it. Taekyung awakens after seven days unconscious, reunites with the surviving Fire Dragon Pavilion members, and mourns those they lost. Three days later, the Son of Heaven arrives in Xining with a hundred thousand Imperial Guards. As Murim forces gather there, Taekyung and Mae Jonghak affirm their intent to avenge the fallen. The Emperor tells Taekyung he should now be called Prince Shangshan. Taekyung identifies Cheon Taemin as the Martial God, though their connection remains unclear.

## Continuity

- Ma Sanbao was killed by the Son of Heaven; the Moving Formation trap destroyed Ma’s forces. The Son of Heaven used the White Illusion Jiangshi Art, given to him by Jin Taekyung, to survive and remain with Zhu Bao.
- The Emperor declared the nation Great Ming and ordered a personal expedition to Xinjiang, vowing not to return to the palace until the traitors were rooted out.
- The coalition is gathering in Xining for a campaign against the Lord of Heaven. The Son of Heaven arrived with a hundred thousand Imperial Guards.
- Taekyung awoke after seven days unconscious. The survivors are grieving their dead; some remain injured.
- The search for an unnamed target remains unresolved and will continue with reduced manpower.
- The Slaughter Saint suspects the Bow Saint had another motive when Taekyung was in mortal danger.
- The Emperor now addresses Taekyung as Prince Shangshan, formerly Marquis of Shangshan.
- Taekyung identifies Cheon Taemin as the Martial God; their connection is unknown.
- Taekyung’s dream of a modern battle and a colossal winged being remains unexplained.

## Translation Decisions

- Render 大明 as “Great Ming,” 親征 as “personal expedition,” and 滅魔正天 as “Exterminate the Demons and Set Heaven Right.”
- Render 上山王 as “Prince Shangshan.”

## Durable state

{
  "active_continuity": [
    "The Son of Heaven survived by accepting the White Illusion Jiangshi Art and arrived in Xining with a hundred thousand Imperial Guards.",
    "Murim forces from across the realm have gathered in Xining to fight the Lord of Heaven.",
    "Jin Taekyung is now addressed by the Emperor as Prince Shangshan, formerly Marquis of Shangshan.",
    "Jin Taekyung identifies Cheon Taemin as the Martial God; their connection remains unclear."
  ],
  "continuity_sources": [
    1138,
    1139
  ],
  "open_questions": [
    "What was the Bow Saint’s motive when Jin Taekyung was in mortal danger?",
    "What will happen in the campaign against the Lord of Heaven?",
    "What did Taekyung’s dream of the winged being and battlefield signify?",
    "What is the connection between Cheon Taemin and the Martial God?"
  ],
  "safe_through": 1139,
  "temporary_decisions": [
    "Render 大明 as “Great Ming” and 親征 as “personal expedition.”",
    "Render 滅魔正天 as “Exterminate the Demons and Set Heaven Right.”"
  ],
  "version": 1
}

## Reading copies

## Chapter artifact 1135

# Chapter 1135

On a hill washed in faint moonlight, his sudden appearance seemed utterly out of place.

Not just to Ma Sanbao. To all of them.

And the next moment, the voice that slipped between pale lips revealed the source of that unease.

“So, traitor—have you enjoyed your rebellion?”

His tone was as calm as still water.

But within it lay the imposing authority only a ruler could possess.

It was dignity.

A dignity that even a black robe blending into the darkness and a bamboo hat pulled low couldn’t conceal.

A born dignity that shone through naturally, without the need for an elaborate imperial robe or a crown of hanging beads.

“Long time no see, Eunuch Ma.”

He spoke down to Ma Sanbao as if gazing from a dizzying height.

At the unexpected appearance of the Son of Heaven, Ma Sanbao stifled a groan, then spoke in a low voice.

“What brings Your Majesty all the way here?”

“I came to take care of some urgent business.”

“Was it important enough to leave the Imperial Capital?”

“How curious. Why don’t you think I prepared thoroughly enough to leave the capital?”

“……!”

“A mere traitor like you needn’t worry about the capital’s safety. Not while the Twelve Palaces of the Zodiac are guarding it.”

The Son of Heaven fixed his deep, sunken gaze on Ma Sanbao, who had fallen silent.

The Twelve Palaces of the Zodiac.

Twelve Supreme Peak masters who protected the imperial household.

Though few remained after the rebellion led by the Eastern Heaven Demon Lord, if they knew the location of the Moving Formation, they and the Imperial Guards under their command were more than enough.

But only on the assumption that their enemies would attack the capital.

“Stop bluffing. If you’d planned to strike the capital in the first place, you and I wouldn’t be facing each other like this. Isn’t that right?”

The remark hit home. Ma Sanbao quietly licked his dry lips.

The Son of Heaven was right.

The instant he received information from the strange birds, Ma Sanbao had erased the Imperial Capital from his mind.

If he captured the capital and took the Son of Heaven, he could bring the world to its knees. But the Murim of the Central Plains, already left with a massive gap in its defenses, was far more tempting prey.

There was no reason to take the hard road when an easier, faster one lay open.

And that mistake had been Ma Sanbao’s greatest blunder.

“……Not bad, Zhu Di.”

Speaking the Son of Heaven’s personal name was high treason in itself.

Ma Sanbao didn’t care. He continued.

He had never once thought of himself as the Son of Heaven’s subject.

Now, with nowhere left to retreat, he wanted only an answer to the question that still remained.

“How did you find out where this place was?”

It wasn’t the Son of Heaven who answered, but Zhuge Feng.

“Two years.”

“What?”

“Ah, don’t misunderstand. I wasn’t calling you a bitch. I know you’re a eunuch, but you look unmistakably like a man.”

Zhuge Feng smiled at Ma Sanbao, whose face had stiffened, and continued.

“Since we discovered the Moving Formation, we’ve turned the whole world upside down looking for them. Not quite two years—more like a year and a half.”

“……!”

“Oh, right. When I first started this lunatic undertaking, I had exactly the same look on my face as you do now. My retainers looked even worse. Even my seniors, Sword King and Fist King, tried to strangle me. The late Blade King was worse still.”

Zhuge Feng rubbed the back of his neck, recalling those unpleasant memories. Ma Sanbao stared at him in disbelief.

“You searched for them? And even brought in the Ten Kings?”

“I understand how you feel. But what else could we have done?”

With a sigh, Zhuge Feng gently waved the feather fan in his hand.

The first month or two had been nothing short of hell.

No, worse than that.

At least hell had sulfur fires burning here and there. They’d felt like they were adrift in the middle of an endless ocean.

But it hadn’t taken long to see their first results.

“We found one after three months. It was hidden deep in Mount Huang in Anhui. Fortunately, after that, we found the others much faster.”

The entire operation had been conducted in the utmost secrecy, using only people vetted through the Hidden Shadow Pavilion’s screening process.

Even members of the Nine Sects and One Gang and the Five Great Families were no exception.

Not even a Sect Leader was exempt.

They answered to one person alone—the Alliance Leader—and faithfully carried out the tasks assigned to them.

Myriad-Mile Pursuit, Gung Gibang’s master and the Beggars’ Sect Leader, mobilized all his trusted subordinates alongside the Lower District Sect to find places where a Moving Formation might be located. The wise men of the Zhuge Clan and the Hidden Shadow Pavilion then used the information they brought back to narrow down the locations.

“No matter how difficult the problem, if you know how to solve it, you can find the answer. Fortunately, finding the Moving Formations worked the same way.”

It had been an extremely difficult problem even for Zhuge Feng, who had been renowned as a prodigy since childhood. But before long, he had worked out how to solve it.

Places where few people ventured, the flow of qi was unusually strong, the area could hold at least several hundred people, and grass didn’t grow.

Zhuge Feng selected only places that met those specific conditions. Once he made his decision, famed formation masters from the Zhuge Clan and experts with an exceptional Qi Sense went to investigate in person.

Among them were Supreme Peak masters like the Azure Sky Sword King, Grand Family Head of the Nangong Family, and the Fist King.

“But no matter how hard we tried, it wasn’t enough. We had a fair number of people, but we couldn’t thoroughly search this vast Nine Provinces while keeping the secret completely safe.”

Not a single mistake could be allowed.

Even the sturdiest wall could begin to collapse with one tiny crack.

In that sense, the Moving Formations were nothing less than vast powder kegs.

One explosion could set the whole world ablaze.

But a few months ago, help had arrived from an unexpected source. With it, Zhuge Feng could finally put to rest the last of his worries.

“I heard a very high-ranking person told the Alliance Leader that they would do anything they could to help. That was a tremendous help.”

At Zhuge Feng’s words, the “very high-ranking person” spoke up.

“Wouldn’t you say the highest-ranking person?”

“Ah, forgive my discourtesy, Your Majesty.”

“Of course I forgive you. Anything but high treason.”

Ma Sanbao had been listening blankly to the exchange between Zhuge Feng and the Son of Heaven. Now he clenched his teeth.

*They got me. Completely.*

The enemies in the Central Plains must have been waiting for this very moment.

Even though they could have shut down the Moving Formations they found, they’d left them alone and laid a perfect trap instead.

A trap their prey would rush into, salivating.

A trap that would root out even their final concern.

“Was that how you dealt with the advance party, too?”

Zhuge Feng gently waved his feather fan.

“They were wiped out as soon as they arrived, by the Huashan Sect. The Murim Alliance’s elite, led by the Alliance Leader, filled their ranks.”

“The information we obtained clearly said they’d joined up with those two bandit bastards.”

“What’s so hard about that? We put on black clothes and got together a similar number of people. Rumors about it were bound to spread on their own. And they did.”

The ten thousand fanatics who were supposed to join the Green Forest Alliance and the Yangtze River Channel League had died before ever boarding the league’s ships.

And Seafaring King Pa Ryun had kept the truth thoroughly concealed.

Even the fact that he had subdued his Disciple, Ship-Fire Boy Mu Song, had only been a way to protect the secret. If his Disciple, unaware of the plan, had acted on his sense of justice, he might have exposed the fact that those aboard the rear ships—deliberately kept separate—belonged to the Murim Alliance.

“But then what about the hundreds of ships the river bandits supposedly destroyed……?”

Ma Sanbao trailed off.

The Son of Heaven’s cold smile had given him the answer to his last question.

“I see. So that’s what happened.”

At last, Ma Sanbao understood everything. A hollow laugh slipped from his lips.

He’d forgotten for a moment.

Beneath the Son of Heaven’s pale skin, instead of hot, red blood, ran cold iron and blood.

“The underground prison in the palace must be empty by now. Zhu Di, was this your doing?”

The Son of Heaven answered in an even tone.

“There were so many traitors who had been eating away at the nation that killing them one by one became a chore. They paid a price of their own, so it wasn’t such a bad end for them.”

In the aftermath of the Eastern Heaven Demon Lord’s rebellion came a purge without precedent in the history of the Great Nation.

Among the many criminals who had survived it and awaited their punishment, the Son of Heaven made an offer.

They could die with their families, as the law required, or live out their lives as slaves. Or they could do something to lift even a little of the stain from their family name.

Naturally, most chose the latter.

They were freed from the chains and swords that had bound them, and with trembling hands, accepted spears and blades before boarding the ships of the Great Nation.

They clung to the Son of Heaven’s promise in their hearts: that this choice would let at least one of their kin survive and carry on the family name.

“Right. No wonder it all went more smoothly than I expected. Even if their forces were rotten to the core, it was strange for them to suffer such a crushing defeat.”

They were untrained soldiers. Even with hundreds of ships and cannons, their annihilation had been inevitable.

Learning the full details of this audacious plan, one only the Son of Heaven could have carried out—using so many criminals as bait—Ma Sanbao could only laugh in disbelief.

No. He had to.

Only a hollow laugh that made it seem he’d given up on everything could hide the last chance he had left.

*Not yet. It’s not over yet.*

His lips were smiling, but not his eyes.

Ma Sanbao quickly swept his sunken gaze around.

On the hills surrounding them, he saw countless arrowheads quietly poking through the thick grass. He sensed the breathing of his subordinates, holding their breaths as they waited for his command.

*We’re outnumbered by at least five to one. Maybe more.*

But it didn’t matter.

If he could capture just one of the enemies who had already made every preparation, he could turn this desperate situation around.

No—he might do more than turn it around. He might seize everything.

That was what the Son of Heaven represented.

Besides, Ma Sanbao and his men had no other choice left.

“Now—!”

It all happened in an instant.

Ma Sanbao’s mighty shout as he kicked off the ground and shot upward.

The tightly drawn bowstrings releasing their arrows all at once.

And—

Before the countless arrows that couldn’t keep up with his lightning speed had even finished sweeping across the ground, a low whistle of air split through the space above Ma Sanbao’s head.

*No Shadow……!*

Ma Sanbao clenched his teeth at the masked figure who had suddenly appeared in his way.

It was him.

Ma Sanbao had never seen his face clearly, but he knew he existed: the Son of Heaven’s hidden bodyguard.

The imperial household’s greatest assassin, who never even revealed his shadow, was bringing down a dagger wrapped in Force beneath the faint moonlight.

Just as Ma Sanbao had expected.

*Shhk!*

With a gruesome sound of flesh being cut, the blade sank into his forearm.

But Ma Sanbao didn’t flinch. He thrust out his half-severed left hand and struck No Shadow.

*Crack!*

No Shadow went flying from the force of the blow. Ma Sanbao drove internal energy into the tips of his feet and released it.

*Boom!*

Ma Sanbao shot toward the hill like a falling star.

The White Illusion Jiangshi Art, made even stronger after the bloody battle at the imperial palace, was enough to make him forget pain and fear.

“Zhu Di!”

Ma Sanbao roared.

A dozen or so arrows shot from his blind spots and buried themselves throughout his body. Then Zhuge Feng and Baek Yeon blocked his path. But Ma Sanbao’s corpse-gray eyes remained fixed on just one person.

The Son of Heaven, his pale face still showing the unmistakable signs of illness, just as it had the last time Ma Sanbao saw him.

*Shhk! Thud!*

*Crack!*

There was no blood left to spill from a body that was already no different from a jiangshi. Only chunks of flesh and pieces of bone flew through the air.

But his will remained, desperate and unyielding.

*Slash!*

Baek Yeon’s crescent-bladed polearm sank into Ma Sanbao’s left shoulder and sliced diagonally through his upper body.

*Crack!*

Ma Sanbao’s one remaining hand finally grasped what he wanted.

The Son of Heaven’s throat.

“Everyone, stop.”

Silence fell all at once.

Before the Son of Heaven could even draw the sword at his waist, Ma Sanbao had pinned him down like a bolt of lightning. He gave a faint smile.

Then he whispered into the ear of the Son of Heaven, whose pressure points he had struck.

“Thank you. You came all the way here yourself, so—”

*Thud.*

Ma Sanbao blinked.

Why?

How could the Son of Heaven move after his pressure points had been struck?

And why, now that he was finally face-to-face with him, was the Son of Heaven’s skin so similar to his own?

“……You. Don’t tell me—”

*Crack.*

The Son of Heaven slowly twisted the hand that had pierced the center of Ma Sanbao’s chest and spoke.

“A few months ago, I received a great gift from someone. Something you know well.”

“……!”

“I thought long and hard about it. It was as much a curse as it was a blessing.”

But the Son of Heaven’s deliberation hadn’t lasted long.

His only remaining blood relative, the sole heir who would inherit the realm, had made him a request.

“He told me to live a thousand years. Not as the Son of Heaven, but as family—as someone he wanted to stay with for a long time.”

Moved by Prince Shangshan Zhu Bao’s sincerity—no, Imperial Younger Brother Zhu Bao’s—the Son of Heaven made his choice.

Even if it meant breaking a taboo. Even if he might one day regret it, he would stay with his younger brother for as long as he was allowed.

And that choice had brought them to this moment.

“Now I understand why Jin Taekyung gave me the White Illusion Jiangshi Art. It wasn’t only for me…… It was for my brother, so he wouldn’t be left alone again.”

At that moment—

“By the law of the Great Nation, I punish this traitor.”

*Crack!*

As Ma Sanbao heard the Son of Heaven’s voice for the last time, the world before his eyes went black.
## Chapter artifact 1136

# Chapter 1136

No one could survive having their heart crushed.

And this simple, clear fact was no exception—not even for someone who had mastered the White Illusion Jiangshi Art, one of the foremost among the countless monstrous martial arts and supreme techniques in the world.

Thud.

His body crumpled like a rotten old tree.

The Son of Heaven silently looked down at the traitor who had finally met his end. Then he pulled his hand from deep inside the man’s chest and spoke.

“Commander.”

It was a brief call, without a single detail.

But it was enough for Baek Yeon, Commander of the Embroidered Uniform Guard.

“At your command.”

It was as natural as water flowing.

So was the reverence for the Son of Heaven, who had personally executed the traitor with his own hand.

And so was the crescent-bladed polearm that flashed down in a streak of light.

*Shhk!*

Flesh and bone parted with a chilling slice.

Baek Yeon carried out the beheading in a single stroke, then lifted the severed head on the tip of his polearm.

The traitor’s eyes were still wide open, frozen before they could close. He would watch to the very end the scene spread out below the hill.

*Shh-shh-shh-shh-shhk!*

The sudden feeling that the sky had darkened was no one person’s mistake.

Thousands of Imperial Guards, each an elite chosen to match the Son of Heaven’s name.

With internal energy behind each shot, arrows from their powerful bows filled the sky and rained down with astonishing speed and force.

They fell upon enemies struggling with all their might in the shallow basin hundreds of feet away.

*Thwup-thwup-thwup!*

“Gaaah!”

Blood and screams burst forth without pause.

At the very start of the battle, many of the fanatics had taken Temporary Strength Pills and swung Sword Energy as they closed the distance. But even their desperate strides could never reach the hill.

“Open.”

*Fwoosh.*

At Zhuge Feng’s quiet command, a strange energy drifting through the air rose like heat haze.

The base of the hill was instantly swallowed by thick fog.

As the fanatics were thrown into confusion by an illusion unlike anything they had ever seen, a second command rang out.

“Close.”

*Clack.*

With the cold sound of metal, countless hidden weapons and arrowheads emerged from all around them.

The Zhuge Clan’s mechanisms and formations, hailed as the finest in the world, had finally revealed themselves.

And the result was a horrible death.

*Fwoosh, splat!*

The fog turned red.

Everything inside was pierced, cut, and smashed to pieces.

From between rocks, from beneath the earth, from the knots in trees.

The traps, triggered in unexpected gaps all around them, sent the fanatics to their deaths in an instant.

A few fanatics managed to escape the fog by using the corpses of their allies as shields, but Zhuge Feng had prepared more than that.

*Fwoosh!*

The Zhuge Clan retainers numbered a mere hundred, but the terrifying rate of fire of the Zhuge Repeating Crossbows in their hands more than made up for their small numbers.

No—their firepower was greater still.

*Crack-crack-crack!*

In the blink of an eye, bodies piled up, riddled with holes.

The battle that had begun in the dead of night still raged on, but the scene before everyone’s eyes made even the word “battle” seem inadequate.

A slaughter this one-sided could hardly be called a battle.

And this hellscape wasn’t unfolding only in Henan.

“Looks like it’ll be a long night.”

At the Son of Heaven’s sudden murmur, Zhuge Feng answered.

“And soon, the sun will rise.”

That was right.

No matter how long the night, day would dawn.

Another day would begin beneath a sun as bright as ever—or brighter.

Tonight, they would eliminate one of the great threats hanging over the Central Plains.

“Though certainty is a dangerous thing for a wise man…… I, Zhuge, have no doubt.”

He had built the plan with all his might.

Zhuge Feng had waited a long time, deceiving not only the enemy but even his own allies.

All for today. For this very moment.

“Wherever the traitors go, they won’t escape death.”

Zhuge Feng spoke with conviction.

They had gathered the elite of every province at every Moving Formation they had found. No matter where Dark Heaven’s dagger went, once tonight was over, they would all be dead, never to return.

That went especially for Shanxi, which Zhuge Feng had judged—alongside Henan—to be the enemy’s most likely target.

A giant called the Azure Sky Sword King was leading the forces there.

“It is all thanks to Your Majesty’s help.”

At Zhuge Feng’s most respectful expression of gratitude, the Son of Heaven let out a quiet laugh.

“Is that so?”

Then he spoke.

“I wonder if the Commander thinks so, too.”

Baek Yeon, standing beside him, answered without the slightest hesitation.

“Of course not. They did all the hard work. The Imperial House only lent a hand at the end.”

Zhuge Feng’s mouth fell open at the unexpected answer, but the Son of Heaven’s smile only deepened.

“Why?”

“Don’t ask when you already know, Your Majesty.”

“That’s a rather irreverent way to speak. You couldn’t even stop the traitor just now.”

Baek Yeon frowned at the Son of Heaven’s remark.

“That was because Your Majesty repeatedly insisted that you would deal with him yourself. What, are you going to strip me of my office?”

“That would be inconvenient. I still need you.”

“Your Majesty’s wisdom grows deeper by the day. This servant can only be glad. Though I do regret that my salary has been stuck in place for years, despite all the trouble I go through.”

“My, my. Is that any way for the Commander of the Embroidered Uniform Guard to speak? We’ve recovered the traitors’ wealth, so I’ll double your salary.”

“Perhaps I’m getting old. My armor feels heavy today.”

“Triple it.”

“I am overwhelmed by Your Majesty’s grace.”

Baek Yeon gave a crisp salute, then glanced up at the Son of Heaven.

And as if on cue, the two sovereign and subject burst out laughing.

It was such a hearty laugh that Zhuge Feng, watching this absurd scene unfold before his eyes, was left speechless.

But the man born of the most noble bloodline in the world didn’t mind in the slightest.

The old general who had guarded the Imperial House for decades had every right to speak that way. And apart from that, everything he had said was true.

“Yes. The Commander is absolutely right. I only lent a hand at the end. That’s nowhere near enough to repay even a tenth of what I’ve owed all this time.”

The Son of Heaven smiled at Zhuge Feng, who was staring at him in bewilderment.

In the past, when danger lurked on every side and he fought against illness, laughter like this had been denied him.

But now it was different.

No—Jin Taekyung had made it different. He had changed everything and given the Son of Heaven back the laughter he’d lost long ago.

The Son of Heaven knew that better than anyone. He couldn’t accept Zhuge Feng’s formal praise, even as a courtesy.

The reason he was still alive, the reason the world had overcome another crisis, was all thanks to him.

“It’s troubling. How am I supposed to repay this debt that keeps growing?”

At the Son of Heaven’s rueful murmur, Zhuge Feng’s eyes had grown serious.

“Perhaps…… we’re all wondering the same thing.”

They turned and looked west.

Though nothing could be seen, the three of them seemed to glimpse the figure of one man somewhere thousands of miles away.

Like the faint light spreading dimly over their shoulders at this very moment.

“The sun’s risen.”

“Yes. Day is breaking.”

The Son of Heaven blinked as if he were seeing the light for the first time.

Perhaps it was only his imagination.

On the basin, now steeped in silence and pools of blood, the sunlight advancing over mountains of thousands of corpses shone brighter than ever.

“Bright.”

Darkness scattered. Light blazed.

The Son of Heaven fervently hoped that the countless days ahead would be the same.

And that Jin Taekyung’s fate, which would surely once again leave him standing at the edge of life and death, casting everything he had aside, would be bright as well.

“Great Ming.”

With the new name of the nation that would light the way for everyone’s future, the Son of Heaven of the Great Ming Empire let out a breath that had been swelling in his chest.

“Baek Yeon.”

“Your orders, Your Majesty?”

“I think I’ll have to quadruple your salary. This is going to be a difficult undertaking.”

“What do you mean……?”

“I will not return to the palace.”

“……!”

“Tell all the people of the realm: I will not sit on the throne until those vile traitors lurking beyond the desert have been rooted out.”

The old general stared at the Son of Heaven, eyes wide. Then, smiling, he lowered one knee to the ground.

“I, Baek Yeon, Commander of the Embroidered Uniform Guard, accept Your Majesty’s imperial decree.”

That day, countless messenger pigeons and mounted couriers crossed the land and skies of the realm.

* * *

The imperial decree, carried by hooves and wings, spread across the realm in just a few days.

No—it shook it to its core.

Murim, the common people, and even the government.

“By imperial decree!”

The messengers sent across the realm hung notices bearing the Imperial Seal everywhere they went. At last, everyone learned of the blade that had been closing in on their throats.

And of the one-sided, momentous victory that had begun and ended in a single night.

But victory was not all the Son of Heaven wished to announce.

A personal expedition.

Back when he was known as the Fourth Prince, the Son of Heaven had already been judged to have the makings of a conqueror. Now, under the new name of Great Ming, he ordered the Imperial Guards to assemble, and his destination was exactly what everyone had expected.

Xinjiang.

The former stronghold of the Demonic Cult, beyond the scorching desert.

The spearheads of the whole realm were aimed at the leader of the traitors, who dared to call himself the Lord of Heaven.
## Chapter artifact 1137

# Chapter 1137

Many people call the Central Plains the center of the world, but the phrase has a more precise meaning.

The true center of the world is the Imperial Capital.

Because that is where the Son of Heaven resides—the father of all his people, wielding absolute authority.

And in that same sense, Henan, which had shared in Murim’s earliest beginnings and history, could no longer be called the Murim Alliance’s headquarters.

What mattered was not the place, but the people.

The symbolism attached to a place was created by people.

Sword Saint Mae Jonghak felt that truth keenly every day, through the letters arriving from every corner of the realm.

And the more the piles of papers all around him grew, the more desperately he found himself hoping for a visitor.

“Come in.”

Beyond the firmly shut door, the owner of a faint presence hesitated briefly before entering the study.

“Pardon me for a moment…”

The visitor trailed off, glancing between Mae Jonghak’s sunken eyes and the piles of papers that filled the room.

“Hmm. You seem busy.”

“It’s all right. Have a cup of tea before you go.”

“No. I’ll come back later, urk.”

*Whoosh. Grab!*

Mae Jonghak moved at the speed of a flash.

Using Huashan’s secret technique, Dark Fragrance Drift, he crossed the room in an instant and seized the visitor’s sleeve.

Then he spoke, his eyes and voice filled with desperate longing.

“Have a cup of tea before you go.”

“……”

“Please.”

If the sleeve wasn’t enough, he looked ready to grab the man by the collar.

The visitor sensed a disturbing madness in Mae Jonghak’s glittering eyes and swallowed nervously.

“All right. All right, just let go so we can talk.”

“If you’re lying, I’ll resent you even after I’m dead.”

“What good would resenting me do? You’d be dead.”

“That’s true. Then what kind of tea would you like?”

“Longjing, please.”

“To be honest, it’s the only kind I have. Just drink that.”

Worried the man might change his mind, Mae Jonghak hurriedly let go of his sleeve. As he watched him prepare the teapot, the visitor thought to himself:

*Then why did you even ask…?*

Of course, he already knew. With some people, the more you tried to understand them, the more you only hurt yourself.

It was a lesson he’d learned over the past few months, spent with a certain madman.

“……You’re the spitting image of him. I could’ve sworn I heard he wasn’t your biological grandson.”

“Hm? What did you say?”

“Nothing. Just talking to myself.”

“I understand. The older you get, the more you talk to yourself.”

It was hard to believe this conversation was between a young man who still looked fresh-faced and a boy who looked several years younger still. But appearances weren’t everything.

The Slaughter Saint knew that better than almost anyone.

“So the Alliance Leader does it too. I suppose we’re all much the same.”

“Hm? Much the same?”

“Didn’t you just say that people talk to themselves more as they get older?”

“Oh, that. I meant people in general. I’ve talked to myself since I was a child, so I can’t say I relate.”

“……Is the tea going to take much longer?”

Just as the Slaughter Saint was feeling his energy rapidly drain away, Mae Jonghak finally set a steaming cup on the table.

“Drink. It isn’t mine, but the aroma should be quite good.”

Mae Jonghak was right.

Perhaps because it was the tea enjoyed by a man who had been a City Lord, both its aroma and quality were excellent.

The man, who had committed countless acts of corruption, had vanished like dew on the execution grounds. But his tea leaves—and his lavish study—remained.

The room now served as the Murim Alliance’s temporary Alliance Leader’s Hall.

“I hope I’m not taking up too much of your precious time.”

The Slaughter Saint glanced at the towering piles of papers, which looked ready to collapse at any moment. Mae Jonghak tilted his hot teacup and answered.

“Time is always precious. If we’d lost the battle seven days ago, I wouldn’t be enjoying this luxury.”

Watching the wisps of steam rise like heat haze, the Slaughter Saint murmured as if to himself.

“Seven days. Has it really been that long?”

Mae Jonghak wasn’t the only one who’d been busy.

The past week had been a whirlwind for everyone, the Slaughter Saint included.

They’d had to begin dealing with the aftermath before they could properly recover from the physical and mental exhaustion.

And Mae Jonghak already knew that the Slaughter Saint, busy treating the wounded, wouldn’t have come for no reason.

“You seem to have enjoyed the tea’s aroma. What do you think?”

Naturally, he wasn’t asking whether the man liked the tea.

The Slaughter Saint silently watched Mae Jonghak smile, then awakened the internal energy that had lain deep within him.

*Wooooom.*

A wave spread out, making the air tremble.

Only after an invisible barrier that cut off sound had completely enclosed the two of them did the Slaughter Saint part his tightly closed lips.

“I came to see you about the matter I mentioned before.”

Mae Jonghak’s eyes immediately turned grave.

“Since you came all this way yourself…… I take it the result wasn’t good.”

The Slaughter Saint answered, his voice heavy as well.

“That’s right.”

“You couldn’t find it after all?”

“Based on what we know so far.”

There was still a faint possibility, but both Mae Jonghak, who was listening, and the Slaughter Saint, who had spoken the words, looked doubtful.

As soon as the battle ended, the surviving martial artists, government troops, and countless civilians had all thrown themselves into dealing with the aftermath.

It had been a massive clash, leaving more than a hundred thousand dead or wounded on both sides. But if they hadn’t found *it* in the seven days since, the chances of finding it later were slim.

“Further searches would be pointless.”

“You mean…”

“I’m not saying we should call them off entirely. We should keep looking, but cut down on wasting manpower.”

The Slaughter Saint nodded quietly.

Mae Jonghak was right.

He, too, thought it better to focus on what lay ahead than to cling to something that showed little sign of success.

And yet, the unease pressing down on his heart remained.

“I can’t say I’m not worried either. But…”

Seeing the shadow on the Slaughter Saint’s face, Mae Jonghak continued.

“The tide has already turned. The blades of the Central Plains—or rather, the whole realm—have finally converged.”

At Mae Jonghak’s quiet words, he reached out. Dozens of missives suddenly rose from between the piles of papers and flew before them.

From the Nine Provinces and Eight Wastes to the Four Seas and Five Lakes.

The missives had crossed the vast sky and earth to reach Xining. Each bore a different seal, but the final words at the end were the same.

“Exterminate the Demons and Set Heaven Right.”

Exterminate the demons and set heaven right.

It was the banner raised by the old Murim Alliance, and the four words that now ran through the whole realm.

Even the empire, newly reborn under the name Great Ming, had embraced them.

“They’re coming. For the same purpose as us—one and only one.”

Seven days had passed since their decisive victory after a fierce battle.

But those who had spent the time since living each day as if it were a mere moment were not only the people in Xining.

On the day rivers of blood had flowed through Xining, the enemies’ corpses had piled up like mountains in Henan Province and Shanxi Province.

Ma Sanbao’s head had been taken back to the Imperial Capital, while the rest of his body had been torn to pieces and scattered across the realm.

The Azure Sky Sword King, who had already made every preparation, had wiped out the enemies without a single casualty. The dozen or so remaining Moving Formations had also been shut down before daybreak.

As long as the Demon-Sealing Formation cast by the Zhuge Clan’s formation masters remained in place, the danger posed by the Moving Formations had effectively been eliminated.

After all, the formation’s power had been what allowed them to seal the first rift that had opened in Hubei.

And the safety that brought had lit the fuse that had lain cold.

Under the banners of the Imperial House and the Murim Alliance, the westward advance had begun in earnest.

At the Son of Heaven’s imperial decree that he would personally lead a great army to punish the rebels, a hundred thousand elite Imperial Guards assembled. And it went without saying that martial artists were gathering too, led by the Nine Sects and One Gang and the Five Great Families.

That wasn’t all.

Even the powerless common people formed volunteer militias to stand against injustice. At last, the will of the realm had become one.

“Xinjiang. We can end everything in that accursed land beyond the desert.”

Mae Jonghak spoke in a low but powerful voice.

“The only way to stop this wheel from turning is to defeat the Lord of Heaven.”

The beginning and end of it all. Its very center.

That was what the Lord of Heaven was.

An absolute being who had never once revealed his true form, yet whose immense shadow had spread across the whole realm.

But now that the realm had joined forces and pointed its blades at the Lord of Heaven, heaven’s will was already on their side.

Or so they believed.

*……But why?*

For some reason, the words “Son of Heaven” filled him with an inexplicable sense of foreboding.

The Slaughter Saint tilted his teacup, now gone cold.

Perhaps to keep the unease deep in his heart from showing.

And as he did, he turned over the other reason he’d come to see Mae Jonghak today.

*I can’t understand the Bow Saint’s behavior back then.*

To be precise, no one else would have been able to understand it either.

That was why the Slaughter Saint found it even harder to shake from his mind.

The way she’d stood by, almost indifferent, even when Jin Taekyung was in mortal danger.

Her inscrutable actions, as if she had some hidden purpose no one else knew about.

*She’s hiding something. She definitely is.*

Yet even though seven days had passed, the Slaughter Saint still hadn’t found an answer.

The Bow Saint had been hard to find since the battle ended, and Jin Taekyung himself still hadn’t regained consciousness.

*What should I do?*

With his thoughts growing heavier, the Slaughter Saint drained the rest of his tea.

Then he carefully opened his mouth to speak to Mae Jonghak, who was watching him in silence as though he had sensed something.

Or tried to.

*Thud-thud-thud-thud!*

Then heavy, hurried footsteps sounded, and a massive man burst into the study.

*Crash!*

The brute smashed through the door and shouted.

“Alliance Leader! Taishan saw it! I saw it with these two eyes!”

Recognizing the familiar face, the Slaughter Saint sighed and fell silent. Mae Jonghak felt in every inch of his skin that his brief respite had come to an end, and replied in a sorrowful voice:

“I see. What did you see?”

At Taishan’s next words, both men’s eyes widened.

“The Pavilion Master! The Pavilion Master woke up!”

“……!”

“……!”
## Chapter artifact 1138

# Chapter 1138

Jin Taekyung slowly blinked.

Where was he?

Everything was dark and hazy.

His small body raced forward, wings spread wide, but his senses felt so dull and чуж-like that he couldn’t clearly feel even the wind brushing over him.

That’s right.

He was a bird now.

And before long, he would escape these damp, hazy clouds swirling all around him.

No—right now.

*Whoosh.*

With one powerful flap of his wings, the clouds that had filled the air around Jin Taekyung like bars vanished.

At the same time, a night sky so dark it looked cold spread before him.

And brilliant, multicolored flames painted across the vast open sky.

*Boom-boom-boom!*

Explosions began without warning, erupting all at once and swallowing the night sky.

From far away, it might have looked beautiful.

But with a bird’s naturally keen eyesight, Jin Taekyung could see what lay beyond the dazzling lights.

Countless fighter jets tore through the sky, rupturing the compressed air around them. Bullets and beams of light shot ceaselessly from the ground and sky.

And—

*Shriek!*

Even the gigantic monsters streaking through the dense web of fire.

*—Kieeeek!*

With a chilling roar, more monsters than the eye could count crossed the dark night sky.

Killing intent tangled with killing intent. At the tail end of every thunderous blast, someone died.

*Kwa-gwa-gwang!*

A blinding flash swallowed the sky.

Jin Taekyung was nothing more than a bird. All he could do was stare, dumbfounded, at the scene before him.

At the humans and monsters falling helplessly like scattered embers amid the ceaseless clash of steel and magic.

Then, suddenly seized by the sense that the whole world had gone dark, he looked up.

*Hsssss.*

At first, he thought it was a storm cloud.

A huge, dark cloud, big enough to blot out even the moonlight.

But it wasn’t.

It was a wing.

The wing of a powerful being, so enormous that anyone who saw it would forget how to breathe—and, in a way, so beautiful.

The moment he faced that overwhelming presence, Jin Taekyung felt his senses sharpen with astonishing clarity.

Perhaps that was why he thought he met the gaze of two eyes like black obsidian, looking down imperiously on everyone below, blotting out even the moonlight.

*Fwoooosh!*

The space warped in an instant.

A terrifying pressure, too much for a mere bird to withstand, crushed the air.

No. It wasn’t only Jin Taekyung.

*Crack-crack-crack!*

Countless fighter jets crumpled under the pressure.

Amid the steel engulfed in flames and falling like a meteor shower, Jin Taekyung felt his consciousness fading.

At the same time, an incomprehensible noise grew ever clearer in his ears.

*Tick.*

A streak of pure white light raced from far away and swallowed him.

* * *

The human brain is much like iron.

Just as iron needs enough heat before it can be reshaped, a human brain that has only just awakened needs a little time before it can function.

But the moment I regained consciousness, I could feel everything around me with a clarity sharper than ever before.

Even what had woken me from that deep sleep.

*Ding.*

> **System**
>
> Sleep status has been lifted.

A clear chime rang softly in my ears.

I raised my eyelids, now lighter than down. A face filled my vision, watching me from above as it half-obscured the unfamiliar ceiling.

“A-Are you awake?”

When my eyes met his, trembling with emotion, a thought came to me.

I realized how long I’d been waiting for this moment.

As that truth sank in, a gentle smile spread across my lips.

The nightmare from moments ago, still clinging to me like the sticky residue of glue, had already been washed away without a trace.

“Yes, Master.”

“……!”

Jeok Cheongang paused at the effortless way I’d addressed him without a moment’s hesitation. Then he answered in a choked voice.

No.

He tried to answer.

Until a crowd of uninvited guests came rushing in with a clamor of heavy footsteps.

“That’s it, my—”

*Crash!*

A deafening crash swallowed the rest of his words.

A burly man smashed the door to pieces and charged into the room. Familiar faces streamed in behind him.

“He’s awake!”

“He woke up!”

“He really woke up!”

“Wow! I’ve never seen anyone wake up after seven days!”

It must have taken about one second.

That was all the time it took for the people staring at me with wide eyes, as if they couldn’t believe what they were seeing, to start screaming like mad and pounce on me.

“Aaah! Benefactor!”

“Pavilion Master!”

“Captain!”

“……”

Yeah. It was nice.

But maybe I should’ve stayed asleep a little longer.

* * *

It took quite a while for everyone who’d rushed over to hear I was awake—especially the members of the Fire Dragon Pavilion—to calm down.

“I really wasn’t worried at all. I knew you’d wake up, Young Master Jin… I mean, Pavilion Master.”

Ju Hwaran sniffled as she spoke, her words at odds with the tears and runny nose. Beside her, Song Ilseom added in his usual calm tone:

“She cried like crazy. Kept saying you might never wake up.”

“I-I never did!”

“Yesterday. The day before. All seven days.”

Song Ilseom delivered that merciless barrage of facts to Ju Hwaran, whose face had turned bright red. Then, in an instant, he changed his tune.

“Ah. I must have mistaken you for someone else.”

“You heard him, right? I didn’t cry at all.”

“……”

Ju Hwaran said it so confidently, as though nothing had happened. I could only pretend not to notice the heavy pouch of money she’d slipped Song Ilseom a moment ago.

Even without that cute little farce, voices were pouring in from all sides, leaving me no time to catch my breath.

“I’m glad you’ve regained consciousness, Pavilion Master.”

Sama Pyo, whose emotional expression was about as sophisticated as artificial intelligence, fell silent after that awkward remark. By contrast, Taishan’s emotions were as lively as a beast’s. He burst into tears.

“Taishan glad Pavilion Master awake. Worried so much, only ate three meals a day for seven days.”

“That’s incredible.”

I wasn’t being sarcastic. I was genuinely impressed.

It sounded insane at first, but considering Taishan’s usual appetite, it was practically a hunger strike.

The old man perched on Taishan’s shoulder as if it were his assigned seat sighed.

“Three meals a day is normal, you crazy bastard……”

“I cried so much, now hungry. Pavilion Master, I go eat.”

“Put me down before you go, you walking disaster.”

Of course, those words went in one ear and out the other.

Taishan vanished like the wind. The old man, who’d grabbed him firmly by the nape just to stay alive, let out a scream that quickly faded into the distance.

The next person to fill the empty space had been waiting his turn, his whole body wrapped in bandages like a mummy.

“Captain……”

His voice was thick with tears.

I looked at him with misty eyes.

“You……”

“Yes. It’s me. Your right arm. Your heart. Hyuk Mujin.”

“Right. You’re still alive, my little toe.”

“……”

“You look half-dead, but somehow you’re still breathing.”

Beyond the bandages, Hyuk Mujin’s eyes, which had looked ready to spill over with tears, turned cold.

“What? What’s with that look?”

“……You know you’re really too much, right?”

At his obvious hurt, I frowned.

“Too much? You’re the one who was about to throw our promise away like it was worthless.”

“What?”

“You forgot? The promise we made before the battle started.”

“Oh.”

I’d told him plainly: if he was going to die, he had to do it in front of me. Then I’d make sure to avenge him.

But Hyuk Mujin apparently hadn’t planned to keep that promise.

He’d fought recklessly, stubbornly, even throwing away his own life.

So there was only one thing I could say to him now.

“You’ve been through a lot.”

Hyuk Mujin had been about to answer my sudden remark, but his eyes widened.

Or perhaps it was the look on my face, and the subdued tone of my voice, that stopped him.

So I forced a smile and continued.

“And…… thank you. For staying alive.”

“……!”

“……!”

The air in the room quivered.

Everyone who’d been chattering noisily a moment earlier fell silent as if on cue and looked at me.

They knew, too.

That my brief words weren’t meant only for Hyuk Mujin. They were for all of them.

And that this clumsy expression of emotion was the best I could manage right now.

“Well, that’s all. I just felt like I had to say it.”

Something stirred in a corner of my heart.

I smiled faintly to hide my joy, my sorrow, and a swelling emotion I couldn’t name.

It seemed the others felt the same.

Some smiled back at me. Some quietly cried. Others simply watched them in silence.

The ones who’d been through all of this long ago were like that. They hadn’t grown used to it. They’d grown numb.

“Come to think of it, I have something urgent to take care of.”

Jeok Cheongang rose to his feet, muttering as if to himself, then added:

“I think it’ll take about half a shichen.”

With that, Jeok Cheongang left the room.

Two other people had appeared at the door at some point, quietly watching us. They went with him.

*There are times when that thought comes to me.*

Sword Saint Mae Jonghak, who had been about to turn away with the Slaughter Saint, moved his lips.

*Being able to laugh when you want to laugh, and cry when you want to cry, may be a great blessing.*

The old men had walked that road before. Now the young were walking it.

That was why they were giving us some space, at least for a little while.

So we could fully experience the emotions of this moment, which might be our last.

So we could accept both the joy of surviving and meeting again, and the grief for those who had left us, and continue along the journey ahead.

“Get some rest. I’ll be back.”

I quietly nodded.

And by the time the conversation with them, who had returned, was over, the whole world had sunk into darkness.

Just like the nightmare I’d had before regaining consciousness.
## Chapter artifact 1139

# Chapter 1139

As I listened to the unending account, I had to hold my breath again and again.

The Central Plains Murim—or rather, the whole realm—was coming together.

It had been all but inevitable, but hearing the news from the current Alliance Leader himself gave it a weight unlike any other.

Of course, the sheer numbers were part of what made it so weighty.

A hundred thousand.

No fewer than a hundred thousand elite Imperial Guards were racing north along the Yellow River, swift as shafts of light.

Under the command of none other than the Son of Heaven.

*Looks like that old man managed to stay alive after all.*

I suddenly remembered the last time I’d seen the Son of Heaven.

His aged appearance belied his youth, and his face was as pale as a sheet. The ruler of a vast continent had been on the brink of death. He surely would have died before long.

If not for the worn-out old book I’d given him as a parting gift.

*White Illusion Jiangshi Art.*

A secret art of the Maoshan Sect—and, at the same time, demonic martial arts that defied all common sense.

The more one practiced it, the more one became a jiangshi. It was no better than a poisoned Holy Grail, but the Son of Heaven seemed to have drunk from it willingly.

A Holy Grail was still a Holy Grail, after all.

Even in an age when the Three Bonds and Five Relationships were held sacred, they meant nothing if you couldn’t breathe.

Not when he had only one blood relative who could take on all the burdens he carried.

And the Son of Heaven wasn’t the only one who had someone to protect.

“The Yangtze and the Yellow River are packed from bank to bank. Everyone’s coming here.”

Mae Jonghak hadn’t exaggerated when he said “everyone.”

The hundred thousand Imperial Guards led by the Son of Heaven were only part of the enormous force gathering.

From the great Murim sects to reclusive masters hidden deep in the mountains, all the way down to Third Rate swordsmen.

Once the blade at their throats—the Moving Formation—had been broken, they all smashed through the fence and poured out.

Countless ships covered the rivers, while the thunder of galloping hooves shook the earth.

All for one goal.

To cool the heat raging in their hearts like molten lava.

“The sacrifices made by you and so many others are what made them rise up.”

Some of those who had cowered in fear must have felt ashamed. Others must have blamed themselves for not being there to fight alongside us.

Of course, people weren’t as righteous as they liked to think. Some might have taken up arms simply to make a name for themselves.

But the reason didn’t matter.

At least now, we could come together as one.

That was why I could understand the position the Alliance Leader before me had been in.

“You don’t have to apologize.”

At my sudden words, Mae Jonghak—whose face had been stern the entire time—bit his lip.

“…My friend.”

“To be honest, yes. There were times when I thought we’d been abandoned.”

To catch a big fish, you needed bait.

This time, Xining had been the bait.

The kind so tempting that Dark Heaven couldn’t help but bite.

But the Murim Alliance hadn’t thought of us as mere bait or pawns to be discarded.

They’d drawn up an elaborate plan in the strictest secrecy. Though they’d been a step too late, they’d sent powerful reinforcements—and even uprooted the last lingering threat the Blood Lord had left behind.

“So please, don’t apologize.”

I met Mae Jonghak’s wavering gaze and added quietly:

“If only for the sake of those who are gone.”

“……!”

“They chose their path. They’d already accepted that they might die, and they fought as though they meant it. More bravely than anyone.”

Mae Jonghak had no reason to apologize.

No. If he did, it would be no different from insulting the dead.

Jeong Hogun and a thousand Embroidered Uniform Guards. Countless martial artists and government troops. Even the common folk who’d taken up rusty axes and sickles to hold back the invaders.

Every one of them had been a hero.

And so had those who, like Mae Jonghak before me, had struggled behind the scenes for this great victory.

That left us with only one goal.

“We have to repay this blood debt many times over. All of us, together.”

Everyone here knew who we had to collect that debt from. So did the whole realm.

The Lord of Heaven.

Or—

*Asmodeus.*

The supreme demon. The king of the Demon Realm.

The name of the being that had finally intruded into reality lingered on my tongue like a bitter poison.

And someone else, bound up with him.

*Cheon Taemin.*

No.

The Martial God.

* * *

Time flew by.

One day, thick snow fell like it was the middle of winter. The next, a storm of wind and rain swept through as if it meant to swallow the whole world.

Then, three days after I regained consciousness, a sight I’d never seen before came into view beyond the shimmering heat haze raised by the blazing sun.

Boom. Boom. Boom.

The war drums of Xining City, silent for ten days, began to toll with a deep resonance. But not a trace of fear showed on the faces of the people crowding the walls.

Everyone in Xining simply watched, their hearts swelling.

North, south, east, and west.

Across the winding hills, the vast plains, and along the Yellow River—a wave of countless banners surged toward us.

“The enemy! The enemy’s here!”

“……”

Take that back about everyone.

There’s always some lunatic who can’t read the room, wherever you go.

“Are you not listening to me? Prepare for battle at once!”

Jeok Cheongang watched the Great Sir hopping up and down, then turned to me.

“Er, would you happen to…”

I felt his gaze on my cheek and cut him off before he could finish.

“No.”

“I haven’t said anything yet.”

“You were about to ask if you could kill him.”

“Hmm.”

“You can’t break his arms and legs, either.”

“Ah.”

“Just leave him alone. Best to leave a madman be. Besides, he’s a useful madman.”

“So what if he’s useful in battle? Every time that man opens his mouth, I feel like I’m about to suffer qi deviation.”

Honestly, I couldn’t disagree.

They said he’d been darting all over the battlefield like Hong Gil-dong, saving a whole lot of our people. But after the battle, he’d become plain old Gil-dung.

Like a pile of shit right in the middle of the road, he was someone everyone edged around.

The one saving grace was that even ordinary people now knew the Great Sir wasn’t just any lunatic.

“That old man’s at it again…”

“Whew, I thought something serious had happened. When he shouted ‘enemy,’ I nearly had a heart attack.”

He was so well-known that even the people who’d jumped at the shout calmed down as soon as they saw him.

“But what happened to that Great Hero? He looked perfectly fine when he fought those Dark Heaven bastards.”

“Who knows? Maybe he fell off a cliff looking for a fortuitous encounter.”

“……”

I was listening to a conversation between commoners who knew a suspicious amount about martial-arts clichés when—

Thud-thud-thud-thud!

The pounding of hooves shook the earth, and an enormous cheer erupted, swallowing up the scattered murmurs in an instant.

“Waaah!”

The flags swelled as the wind that had just blown in from far away caught them, carrying that feverish roar with it.

The fifteen pillars that upheld the realm’s Murim.

The Nine Sects and One Gang. The Five Great Families.

The overlords of the various provinces, the large and small Murim sects that followed them—and five words unfamiliar to some: Nanman Beast Palace.

And among all those names fluttering fiercely toward the sky, two banners rose higher and larger than the rest.

“The Murim Alliance…!”

The martial artists of Xining were moved at the sight of the banner that represented them. The government troops and commoners, meanwhile, stared wide-eyed at the sight of a man they’d thought they would never meet in their lives.

“T-The Emperor!”

“So the rumors that he’d lead a personal expedition were true!”

The people who spotted the brilliant golden dragon embroidered on a banner, impossible to hide even behind the thick heat haze, all dropped to their knees and bowed.

To the ruler of the Great Nation.

No, to the ruler of Great Ming—their father.

“This is a sight. What a sight.”

As if to prove Jeok Cheongang’s muttering right, the whole place was in an uproar.

Some people slammed their heads against the wall until blood ran down. Others wailed as though they were about to faint.

They weren’t even close enough to see his face yet, and this was how they were acting.

At this rate, you could call him the three-generation ruling family of North Korea—or an unlucky Lord of Heaven—and no one could argue.

“Come to think of it, he’s only one character away from the Lord of Heaven.”

Jeok Cheongang heard me mutter and spoke in a slightly uneasy voice.

“Keep your voice down. There are plenty of ears around.”

“That’s why I kept it down.”

“Lower.”

“Come on, this is fine. Since when have we worried about stuff like this?”

“No, you’re not wrong, but you should still watch it…”

“What did I do? You’ve always taught me, Master, to speak my mind—even if I’m dragged before Yama.”

“……!”

“What?”

Jeok Cheongang silently twitched his nose for a moment, then turned away.

Watching the procession rapidly draw nearer, he muttered as though to himself.

To himself, mind you.

“That sounds nice.”

“Huh?”

“But the more I hear it, the more I think ‘Master’ sounds a bit too stiff…”

“Are you talking to me?”

“God, what a nice day. It’s a beautiful day, but my one and only Disciple is so damn clueless…”

“Yeah. Really beautiful out.”

“……”

“What?”

Maybe I should stop teasing him before he got annoyed.

I was just about to let out the snicker I’d been holding back at the sight of his nostrils flaring now too, when—

Grrrummmble.

With a heavy rumble, the bridge lowered across the moat.

At the same time, a dazzlingly white horse stepped forward.

Beneath the people’s cheers, joy and tears mingled together.

“Long live the Emperor! Long live Great Ming!”

The Son of Heaven.

At last, he had arrived.

The ruler of the continent, who could drive both fans and haters—or rather, the common people—mad just by showing up.

But unlike some miserable bastard lurking beyond that desert, this ersatz Lord of Heaven was on our side. That was what mattered.

His baby brother, whom he doted on, was the president of my fan club, and the entire Imperial House owed me a very big debt.

“It’s been a long time, Marquis of Shangshan Jin Taekyung.”

At last, he crossed the city gates and stepped into Xining. He smiled gently at me as I stood there with my back impudently straight.

“No, I suppose I should call you Prince Shangshan now.”

“……?”

*Mom. I’m a king now.*

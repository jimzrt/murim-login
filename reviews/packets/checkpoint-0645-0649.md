# Checkpoint Review — 645–649

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

# Chapters 645–649

## Plot

Baeksang attacks Jin Taekyung during the Tribal Grand Council but is defeated while Jin remains seated. The Beast Miao King intervenes, and Baeksang withdraws with Yohi, Heugung, and nearly half the chieftains, deepening the political division. The Beast Miao King sends scouts toward Guizhou to investigate the Blood Monk and possible Dark Heaven involvement. Jin also dispatches Ju Hwaran, Song Ilseom, and Hyuk Mujin with the mission.

At the Inner Palace banquet, the Beast Miao King recounts witnessing the Martial God defeat five Supreme Peak fiends and five hundred Blood Ghost Squad members, then meeting him again as a young boy. Jin recognizes similarities to Cheon Taemin, but their connection remains unconfirmed. Meanwhile, the Southern Heaven Demon Empress and her subordinates monitor the Blood Monk investigation.

The Beast Miao King tries to reconcile Jin and Baeksang, but Baeksang refuses to explain his hatred of the Central Plains and demands that Jin and the other Central Plains guests leave Nanman. Jin repairs Baeksang’s broken cup as a plea to restore trust. Elsewhere in Guizhou, the unidentified Zen-staff wielder kills roughly two hundred avengers and continues south.

Jin is later attacked by an arrow while in the palace latrine. The arrow carries a leather missive reading, “Today. Insi. West Gate.” Jin retrieves it through the System’s Inventory and treats it as an invitation from an unknown sender, despite the attack and the humiliating pursuit that follows.

## Continuity

- Jin defeated Baeksang, but Baeksang remains openly hostile and has taken roughly half the chieftains—including Yohi and Heugung—away from the main faction.
- Chief Jang and Chief Go are organizing a fast scouting party toward Guizhou.
- Ju Hwaran, Song Ilseom, and Hyuk Mujin are investigating the Blood Monk and may engage him if necessary.
- The Blood Monk remains unidentified; he is a bald, beardless martial artist who uses a steel Zen staff and has killed hundreds in Guizhou while traveling south.
- Dark Heaven may be supporting or directing the Blood Monk, but this remains unconfirmed. The Southern Heaven Demon Empress’s faction is monitoring the investigation.
- The Beast Miao King personally witnessed the Martial God’s extraordinary feats and later saw him as a young boy. Jin suspects a connection between the Martial God and Cheon Taemin, but has no proof.
- Baeksang’s hatred of the Central Plains remains unexplained. The Beast Miao King is his sworn elder brother and is attempting to reconcile them.
- Approximately two hundred Ailao Mountain warriors remain trapped in webs protected from the Poison Mist. The missing ferocious beasts, Ailao Mountain’s Wraith, and the pure-white eggs remain unexplained.
- An unknown assailant sent Jin the message: “Today. Insi. West Gate.” The sender, purpose, and danger at the West Gate are unknown.
- Jin can store and retrieve physical objects through the System’s Inventory.

## Translation Decisions

- Use **Tribal Grand Council**, **Blood Monk**, **Blood Ghost Squad**, **Southern Heaven Demon Empress**, **Martial God**, **Inner Palace**, **Outer Palace**, and **West Gate**.
- Use **Insi** for 인시, **Pavilion Master** for 각주, and **missive** for 전서.
- Retain **Flame Divine Palm**, **Finger Qi**, **Force**, **Scorching Yang Qi**, **Sound Transmission**, **Fire Dragon Pavilion**, **Fire Courtyard**, **Soul-Chasing Guest**, **Killing Buddha**, **Hyukroach**, and **Water Style**.
- Preserve the cup-and-wine metaphor: the repaired cup represents trust, while spilled wine represents lost people.

## Durable state

{
  "active_continuity": [
    "Jin Taekyung is staying in the Nanman Beast Palace’s Inner Palace as the Third Young Master of the Jin Family of Taiyuan and head of a Murim Alliance pavilion.",
    "An unidentified assailant fired an arrow through the latrine door at Jin Taekyung.",
    "The arrow carried a rolled leather message reading “Today. Insi. West Gate.”",
    "Jin can store and retrieve physical objects through the System’s Inventory.",
    "The message appears to be an invitation from an unidentified sender."
  ],
  "continuity_sources": [
    649
  ],
  "open_questions": [
    "Who fired the arrow and sent the leather message?",
    "Was the arrow intended as an attack, an invitation, or both?",
    "What awaits Jin at the West Gate during Insi?"
  ],
  "safe_through": 649,
  "temporary_decisions": [
    "Use Insi for 인시.",
    "Use West Gate for 서문.",
    "Use Pavilion Master for 각주.",
    "Use missive for 전서."
  ],
  "version": 1
}

## Reading copies

## Chapter artifact 645

# Chapter 645

Who had crossed the line first?

Me? Or Baeksang?

And among the words he and I had exchanged, which had been true and which had been lies?

Several questions flashed through my mind in that brief moment, but they no longer mattered.

From this point on, it was time for true martial artists to settle the result with nothing but force.

*Whoosh!*

A sharp sound of something slicing through the air pierced my ears.

Before I could even hear it properly, I twisted my head aside and dodged the Finger Qi flying toward me. Without a moment’s hesitation, I braced one hand against the stone table in front of me.

*Boom!*

The table, carved from a massive boulder, trembled.

At the same time, thirty-three wine cups sprang into the air as though they had been bounced upward. I smoothly thrust out my hand and knocked several of them away.

*Thwack.*

Toward one person alone.

Baeksang.

*Whoosh-whoosh-whoosh!*

They were nothing more than crude wooden cups that had been roughly carved, but the moment they were filled with the internal energy I had sent into them, they transformed into terrifying weapons.

They flew faster than arrows and possessed enough destructive force to shatter stone.

But my opponent was calm—and before he was calm, he was strong.

*Whoomph! Slash!*

Baeksang swung his straightened hand blade horizontally. Invisible, intangible qi split through the air and sliced apart the cups flying toward him.

Before the fragments of the cups, shattered after losing their momentum, could even reach the ground, Baeksang’s body shot upward from his seat and blurred.

*Papapat!*

Beyond the darkness that had settled over the main hall, the hem of his white robes fluttered like a ghost.

In the time it took him to cross the stone table and erase a distance of nearly five zhang, he raised one fist to drive it down onto the crown of my head.

“You’re crossing the line again.”

As I muttered those words under my breath, I thrust my palm upward.

*Fwoosh!*

Flame Divine Palm.

The flames blazing as they devoured the darkness met Baeksang’s fist, which was wrapped in dazzling Force.

The white and blue energies tangled together, then exploded in a flash of light that shook the entire hall.

*Boom! Rumble-rumble!*

A descending fist and an upward palm.

An old man and a young man.

A collision of raw, pure strength.

The violent tremors and thunderous roar rocked the main hall, and I saw it clearly.

*Fwoosh!*

Beyond the radiance that burst outward from the single point where our attacks met, I saw a pair of eyes opened wide.

“……!”

Baeksang’s eyes, which had always shone with a cool light, held unmistakable surprise.

*How?*

It was a familiar emotion. A familiar look.

Most of the people I had faced until now had made the same expression.

Before my name and sobriquet had begun spreading through the Murim, and even afterward, they would sometimes seem to forget that fact and underestimate me too soon.

Because I was young.

Because my family was insignificant.

Or because I was an inexperienced brat who had never experienced war.

And whenever that happened, I kindly taught them the truth.

Not with words, but with force.

*Just like now.*

Along with the mutter that never escaped my lips, I drew up the energy filling my entire body even more forcefully.

*Waaaaaah!*

The tremendous internal energy of no less than three jiazi stirred to life and stretched.

The terrible heat radiating from the Scorching Yang Qi evaporated the moisture in the surroundings, and red heat haze rose into the air.

*Tsss-tsss-tsss!*

The fist blocked by my fully opened palm began to be pushed backward little by little.

In Baeksang’s trembling eyes, his burning white robes and my calm face appeared in turn.

A cool voice flowed between Baeksang’s lips, cracked from the heat.

“You bastard……”

What remarkable composure.

Most of the things I had heard from people in situations like this were usually “fucking bastard,” “son of a bitch,” or “crazy bastard.”

But whether he had been tempered by a hundred battles or because he was the great chieftain leading tens of thousands of tribespeople, Baeksang’s emotions might have surged, but they never overflowed.

And his martial prowess was far greater than I had expected.

*Swish!*

A blackened collar brushed against my forearm. At some point, the fist he had clenched tightly had spread open like an eagle’s talons and seized my wrist with lightning speed.

No, he almost certainly would have seized it.

If my movements had not been faster and stronger than his.

*Crack!*

This was strength that had already gone far beyond the limits of a human being.

When I tightened my grip around his wrist with terrifying force, Baeksang’s brow twitched from the pain, and a short groan escaped him.

“Ghk!”

And I did not miss that brief opening.

*Now.*

I twisted Baeksang’s wrist aside, simultaneously pinning his other hand and throwing him off balance. Then I struck his flank with my free palm.

*Thud!*

Before the heavy sound of something tearing through the air could even reach my ears, I released his wrist.

In front of dozens of pairs of watching eyes, the palm strike to his side sent Baeksang flying. He twisted his body in midair and landed on the stone table.

*Swish.*

His movement had been light enough not to make a sound, but his expression was the exact opposite.

Just as Baeksang glared at me with heavily lowered eyes and moved to attack again—

“Enough.”

The voice was not loud, but it held a deep resonance and authority. The Beast Miao King had risen from his seat and opened his mouth with a hard expression.

“Stand down. Both of you.”

Baeksang’s figure wavered, while I shrugged.

“I didn’t move.”

That was an undeniable fact. I had pulled my chair back a little, but Baeksang had been the one to charge first. I had exchanged moves with him while remaining seated.

And the result was, well……

The other chieftains were staring at me as though they had seen a ghost.

Their eyes were proof enough.

The result, too.

“Jin Taekyung.”

I did need to show at least a minimum degree of propriety. This was Nanman, not my home ground, and my opponent was the great chieftain of the Bai people.

At the Beast Miao King’s reproachful call, I raised both hands.

“I’m sorry. It was a situation where I couldn’t help using my hands. I just acted without thinking.”

Of course, I still had to make one thing clear.

Even if I conceded that I might have started the whole thing, Baeksang’s attack had still been dangerous enough to kill me.

“……Hoo.”

Perhaps he understood what I meant. The Beast Miao King let out a quiet sigh and turned his gaze toward the other man.

“Baeksang, do not act rashly.”

Conflict flickered in Baeksang’s cold eyes.

Without answering the Beast Miao King’s call from behind him, Baeksang continued to stare at me. Then he suddenly looked around.

More than thirty chieftains.

Their reactions were divided into three camps. Some shifted in their seats as though they might rush at me at any moment. Some twitched at the corners of their mouths, as if trying to hold back laughter. Others, after witnessing my martial prowess, looked half dazed.

This was proof that factions existed within the Nanman Beast Palace.

And before everyone’s eyes, Baeksang’s standing and Fame had suffered a blemish that would not be easily erased.

By none other than a Han Chinese brat from the Central Plains.

“……”

Baeksang could not have been unaware of that fact. He pressed his lips together, then bowed his head toward the Beast Miao King.

His voice was restrained.

“I apologize for causing a disturbance. I will see you again after I have calmed my mind.”

With that, he immediately left the main hall, his blackened robes fluttering behind him.

Yohi rose naturally and followed him. Heugung also hurried after them, while nearly half the chieftains rose from their seats after carefully watching the situation.

“Palace Lord, I’m sorry, but then……”

“Let’s go together.”

They were probably the people who belonged to the pro-Baeksang faction. Unlike the ordinary moderates, they were the ones who absolutely opposed Nanman joining the Murim Alliance.

When roughly half of the thirty-two chieftains left, Yayul Mok knitted his brows in anger, while the Beast Miao King muttered in a weary voice.

“So this is how it ended up.”

I watched the Beast Miao King’s expression and cautiously opened my mouth.

“I’m sorry. It seems this happened because of me.”

“Hoo. This is not something you need to apologize for. It was a problem that was bound to explode sooner or later.”

“Ah, then that’s a relief. To be honest, I thought so too.”

“……”

At that moment, not only the chieftains who remained but also Yayul Mok and the Beast Miao King looked at me with utterly dead eyes.

—It’s definitely because of you, you bastard.

*What? An auditory hallucination? It definitely wasn’t Sound Transmission.*

Baffled by the strange phenomenon, I tilted my head and spoke again.

“The grand council isn’t over just like this, is it?”

“The grand council will continue for three days along with the festival. You must have heard that before attending.”

“I did hear it, but I thought I’d ask just in case.”

At my shameless answer, the Beast Miao King slowly shook his head.

“Did you really have to take it that far?”

“Still, it felt too suspicious to just let it go. I was curious about his genuine reaction too.”

“Because of that curiosity, you made more than ten thousand members of the Bai people your enemies. If you include Yohi and Heugung, the two great chieftains who follow Baeksang, along with the others, it would not be an exaggeration to say that half of Nanman is now against you.”

*Hmm. Half of Nanman.*

“That’s not as bad as I expected.”

“What?”

“Just two days ago, all of Nanman was my enemy. I was about to be kicked out before the grand council even started.”

“……Huh. Well, I’ll be damned.”

The Beast Miao King gave a hollow laugh, then shifted his gaze to the chieftains who remained.

“Chief Jang. And Chief Go.”

“Yes.”

“This time, I will need your help. First, organize a scouting party of fast-moving warriors and have them watch the area toward Guizhou.”

“Is this because of the Blood Monk?”

The Beast Miao King nodded and continued.

“Both Baeksang’s and Jin Taekyung’s opinions have merit. There is no reason for him to deliberately head toward Nanman, but if he is a man of Dark Heaven, then we would be wise to prepare accordingly.”

“We will obey your command, Palace Lord.”

“As you command.”

If the chieftains who had left earlier belonged to Baeksang, most of those who remained either pledged their loyalty to the Beast Miao King or belonged to the moderates who were quite favorably disposed toward him.

When the two chieftains who led middle-sized tribes silently obeyed his command, the Beast Miao King’s expression relaxed slightly.

“Tonight, we will erect a memorial stele for those who lost their lives and hold a banquet in their honor. The grand council will resume afterward, so you may withdraw for now.”

* * *

“What happened?”

The moment we returned to our quarters, Namho came charging over and asked.

“You didn’t cause another incident, did you?”

His voice was filled with suspicion. Just as I was about to answer, Hyuk Mujin erupted in anger.

“Look here, old man Nam! What do you take our Captain for?”

“What else would I take him for? A lunatic.”

“What? Even if our Captain is a lunatic, he wouldn’t do that! Do you really think it makes sense for him to cause a scene at such an important place, of all places?”

“I think it makes perfect sense.”

*If I feel guilty, does that mean I’m normal?*

I hesitated before opening my mouth.

No, I was about to open it.

At least, I was until Ju Hwaran joined the battle.

“Elder Namho, that’s too harsh. How can you call our Pavilion Master a lunatic?”

If Taishan was the reason Namho had aged so rapidly, then Ju Hwaran was his only weakness.

At her appearance, Namho, who had been so bold just moments earlier, scratched at his thinning crown.

“No, well. That’s……”

“Our Pavilion Master came here representing the Murim Alliance. He may be a little rough around the edges, of course, but when he should be doing everything possible to secure Nanman’s entry into the alliance, he isn’t the kind of person who would cause a disturbance at a gathering as important as the grand council.”

“……”

*Please, kill me.*

My conscience was not merely pricking anymore. It was actually painful.

Meanwhile, Ju Hwaran was asking everyone else for their votes like an enthusiastic campaigner.

“What does everyone else think? Why aren’t you answering?”

Song Ilseom, who was always quiet, smacked his lips.

“Hmm. Young Bureau Head, surely we should hear the person in question’s answer first……”

“Add a special bonus.”

“On second thought, I think you’re right. There’s no way our Pavilion Master would do that.”

*Money-crazed bastard—out.*

“Why are the other two of you silent?”

“Taishan. Hungry……”

“I heard there’s a banquet tonight.”

“Taishan. Strongly agrees with what Young Lady Ju said.”

“……I agree as well.”

*Glutton—out. Former fiancé I could chew to bits and still not feel satisfied—out.*

The petition drive proceeded with the speed of Quick Attack, and Ju Hwaran looked at me with eyes sparkling like the Milky Way.

“Pavilion Master, say something too. So, have they decided to join the alliance?”

One second felt like an hour.

After a long silence, I finally opened my mouth.

“Um. Everyone. Well. There was, uh…… a minor problem.”

Ju Hwaran froze, while Namho nodded as though he had expected it.

“See? Crazy Pavilion Master.”

“……”

“Did you kill someone?”

“No.”

“Then you beat someone up.”

“……”

“Who was it? Some chieftain who recklessly picked a fight without knowing better? Or someone else who said something irritating? Surely it wasn’t the great chieftain of the Bai people.”

“Ah.”

“Pavilion Master?”

“……”

“……Pavilion Master?”

As Ju Hwaran’s voice gradually faded, I kept my mouth firmly shut and gazed at a distant mountain.

Namho chuckled and said,

“See? Crazy bastard.”
## Chapter artifact 646

# Chapter 646

If this continued, I was liable to be branded a traitor guilty of high treason, so in the end, I had to explain everything that had happened at the tribal grand council from beginning to end.

Of course, I also had to answer the questions that came up along the way.

“More than half of the chieftains acknowledged you?”

“Yes. They even gave me cupped-fist salutes. They thanked me for saving their tribespeople and blood relatives.”

“My goodness. When you didn’t come even after we waited for you, I had a good idea of what must have happened… But for an outsider—especially a Han Chinese person—to attend the tribal grand council is probably a first in the history of Nanman. No, in the history of the Murim.”

At Ju Hwaran’s astonished expression, Namho, who was sitting beside her, added with a warm smile.

“Of course it’s a first. An outsider attending the tribal grand council was a first, and that outsider getting into a fight with the great chieftain of the Bai people was a first too. Yes, indeed.”

“……”

“……”

“Hoho. I’m simply laughing because I’m so proud and happy. Don’t mind me. Please continue.”

It bothered me a great deal, but I continued for the moment.

“Anyway, that’s how the grand council began, and then…”

Ju Hwaran’s eyes grew round as she listened to my explanation.

“The Blood Monk?”

“Yes. Apparently, he’s rampaging through Guizhou right now. I heard he’s already beaten several hundred people to death and is running wild. This was the first time I’d heard that sobriquet, so I was wondering if Young Lady Ju had ever heard of him.”

The Yongbong Escort Bureau’s headquarters was in Sichuan, and Guizhou bordered Sichuan to the southeast.

Furthermore, although its fortunes had declined for a while, it had once been one of the most renowned escort bureaus in the world, so its intelligence network was considerable.

*So Young Lady Ju might know something.*

But that hope quickly faded.

After hearing the Blood Monk’s characteristics from me, Ju Hwaran shook her head.

“I’m sorry. A few sobriquets vaguely come to mind, but none of them belonged to a master of that caliber. Besides, there’s no specific sketch or description of his appearance.”

“Hmm. Is that so?”

I was admittedly a little disappointed, but I did not show it too much.

As Ju Hwaran had said, narrowing down one person based only on a few characteristics, without even a sketch of his appearance, was difficult.

All I had been able to tell her was that he was probably a middle-aged man, that his martial arts were expected to be at the Supreme Peak level, and that his unique weapon was a Zen staff.

*Well, the Murim is a huge place.*

And it wasn’t only the land that was vast. There were countless people, too.

Even men who carried cheap swords made of scrap iron went around puffing out their chests after giving themselves sobriquets like Soaring Dragon Guest or Sword Fiend.

*Finding him would be like searching for one grain of sand on an endless beach.*

Just as I was clicking my tongue, Ju Hwaran, who had been wearing an apologetic expression, suddenly spoke up as though she had remembered something.

“Oh, but Song Captain would know more about that than I do. Right, Captain Song?”

Oh. She was right.

Everyone’s eyes, including mine, turned toward one person.

As always, Song Ilseom remained silent for a moment before muttering,

“Hmm. I don’t know.”

*Like hell you don’t.*

Having already figured out exactly what kind of person he was, I tossed him a silver nyang and spoke.

“Hey, Soul-Chasing Guest. If you know something, why don’t you lay it all out?”

Although he currently pretended to be nothing more than an escort, Song Ilseom was a martial arts prodigy descended from the Guangdong Chen Family. At an absurdly young age, he had won more than a hundred life-and-death duels and become a legend among wandering martial artists.

In some ways, there were few professions more sensitive to people and rumors than wandering martial artists. Their lives could depend on it from one day to the next.

*Clack.*

Song Ilseom snatched the silver out of the air and frowned.

“What kind of person do you take me for? Someone obsessed with money?”

“Yes.”

“……”

“So, you don’t like it?”

“I don’t dislike it.”

“What if I give you more money?”

“That would be even better.”

“Here. Take more silver, you money-crazed bastard.”

*Whoosh. Clack.*

“……Somehow, this feels even worse.”

After securing a generous bonus, Song Ilseom opened his mouth with an uneasy expression.

“A middle-aged man who uses a Zen staff?”

“Yeah. I heard it was made of steel.”

“What does he look like?”

“I don’t know that much. Aside from the fact that he’s bald and has no beard. I heard the survivor who escaped all the way to Nanman only managed to tell them that much before he died.”

“This is a complete mess. Still, I can think of about three people. There aren’t many martial artists who use a Zen staff as their unique weapon.”

“Oh, there are three?”

“There is one small problem, though……”

“That’s fine. Tell me.”

Then, amid the expectant gazes of everyone present, including mine, Song Ilseom opened his mouth.

“They’re dead.”

“Huh?”

“More precisely, I should say I did the killing. I happened to cross paths with my quarry on a battlefield while carrying out a commission.”

“Hmm… Well, that can happen. What about the other two?”

“What are you talking about? What other two?”

“You just said you killed one.”

“I killed all three.”

“……?”

“I killed two on battlefields and one in a life-and-death duel. The last one I met was the strongest.”

“……!”

A heavy silence descended over the room. Then Namho’s mutter spoke for everyone.

“There was another crazy bastard.”

I didn’t know who the other crazy bastard was, but I wholeheartedly agreed.

I stared at Song Ilseom, who was standing there with a blank expression, and considered my options.

Should I take back the silver first and then beat him up? Or beat him up first and then take back the silver?

Then I noticed someone looking at Song Ilseom with an expression of utter contempt and spoke up.

“Hey, you unorthodox grunt over there.”

“……Unorthodox grunt?”

“Yeah. Do you know anything?”

Sama Pyo, the Young Sect Leader of the Black Dragon Demon Gate—the most powerful unorthodox faction in the world at present and the self-proclaimed hegemon of Gansu—knitted his brows.

“I have three things to say. First, I am not an unorthodox grunt. Second, Gansu and Guizhou are nearly a thousand li apart, making travel between them difficult. And third. Why did you think I would know something like that?”

“Because you’re part of the unorthodox faction.”

“……?”

“Bad people all know one another, don’t they?”

“……!”

“Well, maybe not.”

I waved a hand at Sama Pyo, who had frozen like a stone statue, and looked toward the other enormous unorthodox grunt standing beside him.

Before I could even say anything, a booming answer reached my ears.

*Grrrrowl. Grrrrrrrrowl.*

“……”

*What the fuck?*

This wasn’t some World Cup final. Yet a vigorous vuvuzela blast rang out in the middle of Nanman, and Namho burst out laughing.

“Hoho. What a bastard. If only I’d learned martial arts, I’d split open that goddamn gut. Hahaha!”

Judging by how much he had been laughing, he seemed to be half out of his mind.

Hyuk Mujin, who was staring at Namho with fear in his eyes, opened his mouth.

“Captain.”

“Put your head down.”

“What?”

“Ah, sorry. That was just a habit. But if you start talking nonsense like the others in this situation, I’ll kill you.”

“No, that’s not what I meant. That Blood Monk fellow. There’s too little information about him for a martial artist, isn’t there?”

Of everything that had been said so far, it was the second most sensible thing after Ju Hwaran’s comment.

I scratched the back of my head in frustration and clicked my tongue.

“That’s true. How fucking old is he, anyway? How is there not a single person who knows him?”

Namho, who had been glaring at Taishan with a murderous look, cut in.

“Speaking as someone who’s eaten more years than I care to count, I can say that there is no such man as far as I know. There was a fiend called the Killing Buddha during the Great Faction War, but his characteristics differed quite a bit from those of this Blood Monk. He was already an ancient monster even back then, so it’s questionable whether he could still be alive.”

Namho might have been an old foreigner, but he had once held a fairly important position in the Hidden Shadow Pavilion, so he was probably right.

*Then what the hell is his identity? At this point, he’s practically a hermit master.*

If even Namho, a man from the distant past, and the Fire Dragon Pavilion members of the current generation had never heard of him, then he was truly a freak.

But the most important thing in this situation was not the Blood Monk’s true identity. It was the power behind him and his purpose.

Namho tapped his knees as though he had read my thoughts and spoke.

“I cannot be certain yet, but there is a strong possibility that Dark Heaven is behind the Blood Monk.”

“I agree. I said as much at the grand council.”

“What do the Beast Miao King and the other chieftains think?”

“We decided to send some scouts and warriors toward Guizhou first, but before that… Baeksang’s reaction bothered me.”

“He must have told you not to concern yourselves with it because it was a matter involving the Central Plains.”

“Huh?”

“It isn’t as though this is the first or second time something like that has happened, so you shouldn’t be surprised. Ever since the Great Faction War, Baeksang has shuddered whenever the matter involved the Central Plains. Even the few trade routes Nanman had were closed because of opposition from several tribes, led by the Bai people. However, the question that occurs to me now is……”

Namho continued with a low sigh.

“Was Baeksang’s behavior caused by the grief of losing his only child after being caught up in a war between Han Chinese people? Or did he develop some kind of grudge against the orthodox Murim in the process?”

“Hmm.”

“If it was the former, then it would amount to nothing more than the resentment of a father who had lost his child. But if it was the latter……”

Ju Hwaran, who had been quietly listening to the conversation, murmured,

“It would be betrayal. The kind that could place all of Nanman in danger.”

“Yes, exactly. If he has joined hands with Dark Heaven, this situation will grow beyond control.”

More dangerous than an enemy from outside was an enemy from within.

No matter how impregnable a fortress was, if it collapsed from the inside, it was no different from a sandcastle swept away by the waves.

And if that traitor was a great chieftain who shared control of Nanman with the Beast Miao King—

*Then it was all over.*

I had to uncover it and stop it somehow.

The identity of the sinister plot unfolding within Nanman. And the destination of the Blood Monk, who by now would be heading somewhere else in the distant land of Guizhou.

But even the System that had raised me from an F-rank Hunter to my current position could not split my one body into two.

*In that case……*

I raised my head and slowly looked over everyone around me.

I recalled their martial arts, characteristics, and personalities one by one as I considered who was best suited for the task. Who could return alive from an unknown danger?

And just as I was sinking into a deep train of thought with no end in sight, one person suddenly spoke.

“I’ll go.”

“……!”

“Please send me. I will complete the mission and return without fail.”

I was shocked.

First, because she had read my mind even though I had not said a single word. And again because that person was none other than Ju Hwaran.

My answer burst out as though it had been decided from the beginning.

“No.”

“Why? Do you think I’ll be harmed by that old monster called the Blood Monk?”

“That’s……”

“My martial arts may be meager compared to yours, Pavilion Master, but I believe I am strong enough to protect myself.”

“Young Lady Ju.”

“I know what you’re worried about. Of course, I would be no match for the Blood Monk. But handpicked warriors from the Nanman Beast Palace will be accompanying us, and some of the members here will come too. Tell me if I’m wrong.”

Instead of answering, I pressed my lips together.

What Ju Hwaran had said was undeniably true.

I intended to select some of the Fire Dragon Pavilion members and add them to the scouting party that would soon depart, having them uncover the Blood Monk’s identity and objective. I was taking into account the possibility of a battle in the worst-case scenario.

But the one thing I had not considered was Ju Hwaran’s participation.

“Pavilion Master. No, Benefactor.”

*Benefactor.*

That was what she had first called me several months ago, right after the Yongbong Escort Bureau’s business in Sichuan had ended.

For a moment, the scent of flowers from the Fire Courtyard, where we had taken our last walk before leaving, seemed to drift past me.

And the eyes that had been moist beneath the moonlight were now shining with firm determination.

“Please send me. Send me.”

“……!”

“I can do it.”

A thought suddenly occurred to me.

*Those eyes. That voice.*

I would never be able to refuse a request made in that voice and with those eyes.

*Whew.*

The wind was hot, and my mouth tasted bitter.

I let out a small sigh and finally nodded.

At the same time, Ju Hwaran’s face lit up brightly.

From somewhere in the distance, music announcing the beginning of the banquet had begun to play.
## Chapter artifact 647

# Chapter 647

The banquet was being held in a large training ground inside the Inner Palace.

The place was large enough to accommodate more than a thousand warriors. Every kind of delicacy had been laid out, and the grounds were packed with people, including the tribal chieftains.

And at the most honored seat in the training ground, someone was waiting for me.

“You’ve arrived.”

The Beast Miao King, seated in a tiger-skin-decorated high-backed chair, spotted me and beckoned.

“Come sit. I had a place prepared for you.”

The seat assigned to me was directly beside the Beast Miao King, on his left.

It was an extravagant show of favor for an outsider, but when I considered my status and what I had accomplished the previous night, it wasn’t all that strange.

Of course, that didn’t mean every member of the Fire Dragon Pavilion was being treated the same way.

“I’ve prepared places for all of you at this banquet as well. Eat, drink, and enjoy your—”

“Taishan! Meat!”

Grab! Chomp, chomp, chomp!

At the sight of Taishan suddenly sweeping up all the meat in front of him, the Beast Miao King stared at me with an utterly baffled expression.

“……What in the world is that fellow?”

“……He’s just insane. Don’t pay him too much attention.”

At my glance, Taishan’s mom—no, Sama Pyo—let out a deep sigh, grabbed Taishan, and dragged him away. Meanwhile, Namho, who had been lurking like an assassin and watching for an opportunity, seized a nearby wine bottle and smashed it against the top of Taishan’s head.

Crash!

*Water Style without any water……?*

He had really put his whole body into that swing.

But Taishan drank from the fountain of wine bursting over his head and shouted brightly,

“Namho! Thank you! Taishan was thirsty!”

“Just die. Please, just die……!”

The Beast Miao King watched the scene with an uncomfortable look.

“Hmm. Your subordinates are very close.”

“They are. Close enough that neither of them would notice if the other died.”

“Is that why you didn’t send them?”

I paused for a moment before answering.

“You heard about it? News travels fast.”

“I may not involve myself in every matter, but I can hear every piece of news. That is the position of the Palace Lord of the Nanman Beast Palace.”

He had a point. Since outsiders had joined the scouts, it wouldn’t have been strange for a report to have already reached him through the great chieftains.

I thought of the three people who should be heading somewhere northeast by now and muttered inwardly.

*I wonder if they’re all right.*

After much deliberation, I had selected three people in total.

Ju Hwaran. Song Ilseom. And Hyuk Mujin.

Regardless of my concerns, Ju Hwaran possessed exceptional martial prowess and experience compared to other young prodigies. Song Ilseom needed no explanation, and the last member, Hyuk Mujin, was……

*Whatever else you could say about him, he had the survival instincts of a cockroach.*

Despite how he looked, Hyuk Mujin had survived countless battlefields alongside me, from Shanxi Province to the present day, escaping death at every turn.

He was so good at wriggling his way out of danger that Jeok Cheongang had once said,

*How has someone so weak and cowardly managed to survive this long?*

And I had answered,

*Because he’s weak and cowardly.*

It was true that Hyuk Mujin’s martial arts were inferior to those of the others. And it wasn’t wrong to call him cowardly.

But that could also be interpreted as being extremely cautious.

*He avoids the most dangerous places as though he has eyes in the back of his head, and when he can’t avoid them, he fights with everything he has.*

That was why he always came back alive. It wouldn’t have been strange to change his nickname to Hyukroach.

“They’ll do well. No matter what happens.”

I muttered that with a personal wish behind it, then glanced over the Beast Miao King’s shoulder.

“By the way, there are quite a few empty seats. Even though the banquet has already begun.”

“They’ll be here soon.”

He said it casually, but the Beast Miao King’s eyes had grown heavy and dark. This was especially true whenever he looked at the empty seat directly to his right.

*Baeksang.*

The chieftains who had left the main hall following him were already seated, but Baeksang, Yohi, and Heugung had yet to return.

The Beast Miao King stared at their empty seats for a while before silently tilting the wine bottle.

Drip.

The sun had already sunk behind the western mountains long ago.

Yet the entire Nanman Beast Palace shone brightly even in the darkness. Festivals were taking place everywhere.

The Tribal Grand Council, held only once a year, was also an occasion for unity, and the countless tribespeople who had poured into the streets were laughing and talking with bright faces as they enjoyed themselves.

Or, at least, they probably were. I couldn’t see them from here, but the cheers and firecracker explosions drifting over from the Outer Palace were more than enough to tell me.

Whoosh! Boom!

Waaaaaaah!

If I only listened to the noise, I would have thought it was at least a Samba Festival.

I asked the Beast Miao King with an uneasy expression,

“So, um…… Is this really okay?”

“What do you mean?”

“You know. Everyone seems to have amnesia. They all know what happened at Ailao Mountain barely a day ago.”

The Beast Miao King answered with an unconcerned expression.

“They know. That is why they are holding an even grander festival.”

“That?”

“Yes. Every one of them was a brave warrior who fought and died for Nanman. So they believe that each of them has returned to the arms of the god their tribe worships. Though they died in this world, they believe they were reborn as warriors of their god.”

“……”

I had heard something very similar somewhere before.

Suddenly, I thought of the Middle Eastern terrorist group I had beaten up before logging in.

*They aren’t Crusaders or ancient Vikings.*

All kinds of superstitions ran rampant in the Central Plains as well, but Nanman was clearly different. Perhaps it was because so many indigenous faiths existed here.

Of course, as someone born and raised in the twenty-first century, I couldn’t understand it at all.

“Great Hero Yayul, do you believe that too?”

At my question, the Beast Miao King, who had been about to raise his wine cup, let out a short laugh.

“That is amusing.”

“What is?”

“Isn’t it only natural? You asked that question of an old Miao man born and raised in Nanman—and of the Palace Lord of the Nanman Beast Palace, at that.”

“Oh.”

“But I laughed for another reason. It reminded me of someone else who asked me the same question a very long time ago.”

I had a pretty good idea by then. I opened my mouth with an expression that said *of course*.

“My Old Master—no, my Master?”

“Old Jeok? No. He had no interest in whether the indigenous gods existed or not. He once told me to call him if those Demonic Cult bastards ever set Nanman on fire, though. He said he would gladly come help at least once.”

“……”

That old man, who hated going anywhere, had actually promised to travel out and slaughter people. His grudge against Mount Jiuhua must have been carved into his bones.

I reflexively nodded and asked,

“Then who asked you that question?”

The Beast Miao King’s answer, which came the next moment, was simple and clear—and filled with questions.

“God.”

“Sorry? What?”

As I stood there, momentarily dumbfounded by the incomprehensible answer, the Beast Miao King continued while stroking his full wine cup.

“The Martial God. Someone whose name, age, and even face are not properly known. A divine man who was born human and became something beyond humanity. That person asked me whether I truly believed my god existed.”

“……!”

“So I answered, ‘I honestly don’t know. But I think I may be looking at one right now.’”

The crescent moon reflected in his wine cup rippled. The Beast Miao King downed the wine and moon together, then burst into laughter.

“It was a foolish answer, but I had no choice. That day, the Martial God defeated five fiends who had reached the Supreme Peak realm and five hundred members of the Blood Ghost Squad all by himself. That was my first meeting with him, when he wore a white beard that fluttered like an immortal’s. During our second and final meeting, he had the appearance of a young boy.”

“……”

“More than fifty years have passed, but I still remember that day as clearly as ever.”

I listened with my mouth hanging open, unable to speak.

The Blood Ghost Squad. It was a name I had heard many times before. It also came up whenever Jeok Cheongang launched into one of his “back in my day” stories.

The Blood Ghost Squad had been the Demonic Cult’s premier strike force, sweeping across the Central Plains at the head of a hundred thousand demonic troops. Every single member was said to have been a Peak master.

*Five hundred Peak masters. And on top of that, five fiends who had reached the Supreme Peak realm.*

And the Martial God had annihilated that overwhelming force alone.

Even coming from the Beast Miao King, I would have dismissed it as sheer nonsense—if not for the title *Martial God*.

*……Just how powerful was he?*

Jeok Cheongang. Mungyeong. Mae Jonghak. And others.

I had heard stories about the Martial God until my ears bled from people who deserved to be called giants in the long history of the Murim.

And yet I still didn’t know. What kind of realm had that master reached? No—was he even human at all?

And…… why had such a great and extraordinary being suddenly vanished without a trace one day, and where was he now? What was he doing?

My thoughts followed one another in an endless chain. Along with them, another person’s name suddenly came to mind.

*……Wait.*

The fingers tapping against the table stopped dead.

My eyes flew open, but they were not looking at the banquet hall before me. Nor were they looking at the Murim.

They were looking beyond the hot, heavy air blowing in from far away—beyond some unknown realm that could not be explained in words—to another world and the person who existed there.

*Cheon Taemin.*

The savior who had rescued humanity from the Demon King Asmodeus. An immortal legend and a living god to his followers.

And yet he was a being who had become cut off from the world one day and fallen into a deep sleep.

The reason Cheon Taemin had come to mind at that moment was obvious.

*They were alike. Cheon Taemin and the Martial God.*

It might have been a simple mistake, but there were too many similarities between them to dismiss it as nothing.

The Martial God’s exploits in the Great Faction War and Cheon Taemin’s in the Great Cataclysm—even their actions immediately afterward.

*No way. No. No, that’s impossible.*

But my thoughts could go no further.

The lively music of the musicians had stopped. So had the dancers’ movements. Everyone’s attention had turned toward one person as he climbed the stairs.

“Welcome, little brother.”

In response to the Beast Miao King’s welcome, Baeksang answered from between the great chieftains on either side of him, as though he were the Palace Lord himself.

“I’m late, Palace Lord.”

Snapping out of my thoughts, I finally met his cold gaze, which seemed capable of freezing everything around him.

* * *

*The banquet has begun.*

*The Outer Palace’s security has been reinforced.*

*More than two hundred elite warriors belonging to the Inner Palace are moving through the North Gate.*

As the Sound Transmissions from his subordinates pierced the darkness one after another, someone buried in the shadows rose from their seat.

*Final report. What is the target?*

*The Blood Monk of Guizhou. The targets are moving for reconnaissance and possible combat. At Jin Taekyung’s order, the group includes Ju Hwaran, the Young Bureau Head of the Yongbong Escort Bureau; Song Ilseom, the Soul-Chasing Guest; and Hyuk Mujin of the Jin Family of Taiyuan.*

Knowing Song Ilseom’s past, which only a select few knew, would have been remarkable—but not when it came to the Shadow and his subordinates.

“Ha.”

After letting out a quiet laugh, the Shadow turned around in one smooth motion.

Snap.

As fingers clicked together in the darkness, a strand of flame blossomed and illuminated the shadows.

Fwoosh.

It was a dark, ominous reddish-brown flame.

Watching it flicker, the Southern Heaven Demon Empress smiled.
## Chapter artifact 648

# Chapter 648

It was as though the world had stopped.

The music and movements had cut off all at once, as if by prior agreement, and the people had frozen in place.

And in the silence that descended in an instant, it was a single remark from the Beast Miao King that blocked Baeksang’s cold gaze as he stared fixedly at me.

“Little brother, take your seat now.”

The gaze that had been nailed to me slowly pulled away.

Perhaps he had changed his clothes in the meantime, because Baeksang swept his snow-white sleeves through the air and resumed his halted steps.

“Very well.”

Step. Step.

In the main hall, his clothes were neat and his voice calm, as though nothing had happened.

The Beast Miao King’s eyes seemed tinged with bitterness as he watched Baeksang climb the stairs with two great chieftains on either side of him.

*I suppose that’s understandable.*

One called him little brother, while the other replied, “Palace Lord.”

Although they shared no blood, I had heard that the two had grown up together as sworn brothers from childhood.

But I had never once heard Baeksang call the Beast Miao King hyung.

At the same time, a thought suddenly occurred to me.

*What kind of person was the Beast Miao King to Baeksang?*

Was he still a sworn elder brother, with a single thread of affection left in his heart?

Or merely the Palace Lord of the Nanman Beast Palace, bound to him by a simple hierarchy?

Or perhaps……

*An enemy who had joined the Great Faction War and caused him to lose his only son?*

Who knew? I didn’t.

But I had a feeling I would find out before long.

Whether in a good way or a bad one.

As far as I was concerned, I hoped it would be the former. And it seemed the Beast Miao King felt the same.

“For the first time in a long while, I’ll fill your cup myself. Your foolish elder brother will.”

Baeksang silently stared at the wine bottle in the Beast Miao King’s hand before answering in a dry voice.

“I have kept away from wine and women for decades now. I must respectfully decline.”

Even though the Nanman Beast Palace was a tribal society maintained through a kind of divided rule, the Palace Lord still wielded enormous authority.

That refusal was possible only because he was Baeksang.

Before he was the great chieftain of the Bai people, he was the Beast Miao King’s sworn younger brother.

“You liked fruit wine when you were young. But are you saying you won’t accept even wine poured by me now? I made this fruit wine myself for your sake.”

“……”

“Baeksang.”

At the quiet call filled with disappointment and bitterness, Baeksang slowly closed and opened his eyes before lifting his cup.

“If you insist, I suppose I have no choice.”

“Then……”

“I will accept the cup, at least.”

Only then did the Beast Miao King’s expression brighten. He filled Baeksang’s wine cup to the brim, then whispered in a voice soft enough for only Baeksang and me to hear.

“I hope you will both forget what happened in the main hall. It would be wrong to blame either one of you, since you both wronged each other.”

To me, Baeksang was still suspicious and thoroughly unlikeable. But I wasn’t stupid enough to hit the gas even in a situation like this.

“All right. I admit I went a little too far.”

“……”

Baeksang stared at me with an inscrutable look, then gave a small nod.

“I apologize for showing such an ugly side of myself, Palace Lord.”

It was a surprisingly compliant answer.

The Beast Miao King beamed with satisfaction, turned around, and called out,

“Today is a joyous occasion shared by every tribe of Nanman and our honored guests who have traveled all the way from the Central Plains. Eat and drink to your heart’s content!”

At the Beast Miao King’s shout, which rang across the quiet training ground, the music that had stopped began again. Dancers, both men and women, resumed their movements.

The atmosphere finally began to soften.

But the Sound Transmission that pierced my ear the next moment was anything but gentle.

—Honored guests from the Central Plains, are we? How amusing.

*Aha.*

*I knew it. I thought things were smoothing over too easily.*

I scratched the bridge of my nose and looked toward the Beast Miao King. He had risen from his seat and was encouraging the various chieftains around him and the warriors they had brought along.

Without knowing what was happening behind him.

—Leave. There is no place for you to remain in this land.

As the Sound Transmission continued to reach my ears, I drained my cup in one gulp and moved my lips.

—Our great chieftain is rather stingy. I mean, I know you hate the Han Chinese, but still. Do you have any idea how many people I rescued at Ailao Mountain last night?

—I will compensate you.

—What?

—What do you want? Gold? Silver? Speak. I will give you treasures heavier than your own body.

—……Hmm.

The sweet fragrance of the fruit wine turned bitter.

Much like my mood.

*Gold and silver treasures, huh.*

Well, this was something.

I had expected a cold reception, but it felt far worse than I had imagined. I refilled my empty cup and sent another Sound Transmission.

—I wasn’t doing it for something like that. Do people in Nanman really compare a person’s life to material wealth?

—Of course not. The life of a tribesman cannot be exchanged for anything. But if the other party is Han Chinese, that is a different matter.

—Why?

—That is because you people……

The Sound Transmission that had been about to continue faded away. Baeksang stared at his full wine cup with gloomy gray eyes, then shook his head.

—I said something unnecessary. Stop arguing and leave.

—If you stop there, I don’t think I’ll be able to sleep tonight. Why not get it all off your chest and see if we can find a solution?

—A solution?

Pfft.

It was the first time I had seen Baeksang laugh.

And the emotion contained in that quiet laugh was unmistakable: contempt and ridicule.

Thud. Crash!

The sound was swallowed by the noisy banquet, but I saw and heard it clearly.

The porcelain cup fell to the ground and shattered, and the wine that had filled it splashed in every direction.

Trickle. Drip.

As the spilled fruit wine soaked the stone steps and fell drop by drop, Baeksang’s Sound Transmission continued in my ear.

—It is already too late to turn things back. Just like those.

—Hmm.

Too late? Was it really?

As I gazed blankly at the scene, I suddenly reached out.

Fwoosh!

A thread of internal energy sent from my fingertips swept gently across the floor around us.

At the same time, as though time were running backward, the things that had lost their shape moments earlier shot upward and flew into my wide-open hand.

Sss. Tick, tick!

Dozens of fragments clung to one another like magnets. Using internal energy as adhesive, I joined the broken edges. After clumping together, they finally became a single cup.

“……!”

“……!”

The air around us stirred.

I subtly turned my head to look around. The reactions of those who had been watching us from earlier were quite a sight.

Namho and Heugung stood frozen with their mouths hanging open. A strange light flashed through Sama Pyo and Yohi’s eyes. Taishan had even forgotten to chew his meat and was staring blankly.

*Not bad. Ever since I opened my Middle Dantian, my control over internal energy has definitely become more precise.*

Even setting everything else aside, I had managed to stop Taishan from eating. That alone made it a satisfactory result.

“Hmm, good. Seizing an Object Through Empty Space at this level is excellent.”

Baeksang watched me praise myself and spoke in an even voice.

“Did you want to show off your martial arts? For all that, it is an absurdly pathetic cup.”

“Pathetic?”

“You cannot put anything in that. It will leak out before you can even pour in the wine.”

He wasn’t entirely wrong. I wasn’t some kind of god, and unless I completely reversed time, a perfect restoration was impossible.

As Baeksang had said, the cup was covered in hairline cracks, perhaps because I hadn’t found every fragment. And even I couldn’t retrieve the wine that had already seeped into the floor and stairs.

But……

“You’re so damn picky. Just drink it.”

I tossed out the words, then lifted the wine bottle without hesitation and filled the cup.

No—I poured until it overflowed.

Then I wrapped my entire hand around the gaps where the wine was leaking and tipped it straight into my mouth.

Gulp.

My throat burned as though I had swallowed fire. When I opened my mouth, my voice came out heated along with the fragrant scent of fruit wine.

“What’s the big deal? Even if it’s cracked or broken, if it can hold something and let you drink it, then it’s a cup.”

“……!”

Baeksang’s eyes sank deeply.

—What are you going to do about the wine that was spilled onto the ground long ago?

Anyone else who heard that might have wondered what kind of nonsense he was talking about.

But it sounded different to me after our earlier exchange of Sound Transmissions.

*The cup was trust. The spilled wine was people.*

During the Great Faction War, the Nanman Beast Palace had been forced to lose countless tribespeople. Afterward, because of some matter he did not even want to mention, Baeksang had completely lost his trust in the Central Plains.

So I had conveyed my meaning by piecing together the shattered cup.

*I don’t know whether he’ll take this as a plea to trust once more or as a final warning……*

Either way, I had made my meaning perfectly clear.

I looked out over the training ground, where the lively banquet was in full swing.

At the center of the countless cheering people stood the Beast Miao King, watching me with profound eyes.

*That startled me. The man certainly notices everything.*

For some reason, I felt like a high school student who had been caught causing trouble.

I deliberately shrugged at the Beast Miao King, then rose from my seat and ambled away.

“Where are you going?”

Baeksang’s voice came from behind me.

I threw back a brief answer in a deep voice.

“To take a piss!”

That fruit wine was surprisingly potent.

* * *

“Kh…… Urk!”

He was a bear of a man.

But even his towering, eight-foot frame and more than one jiazi’s worth of internal energy were not enough to escape the death rushing toward him.

Crunch!

“Urk…… Y-you. Who are you?”

A hand had clamped tightly around his throat. Blood flowing from the crown of his head and the lack of air had left his vision red and blurry.

The man squeezed out every last bit of strength he had and continued speaking.

“P-please…… s-save me……”

He wanted to live.

Desperately.

But the strange man gripping his throat thought otherwise.

Crack!

The whites of his eyes showed as his bones broke.

When the life drained from his body and he went limp, the strange man released his grip.

Thud!

The heavy body rolled across the ground. The man who had taken his life without a moment’s hesitation muttered inwardly.

*Ah. Was the man I just dealt with the last one?*

It had been only half a shichen earlier when enemies had suddenly appeared at both ends of the gorge.

Then they had immediately shouted,

“I’ll tear you apart and kill you to avenge my martial brothers and friends!”

“Kill him!”

That was how a one-against-many battle began. After endlessly killing the men rushing at him from every direction, he had forgotten to keep count.

*There must have been about two hundred.*

They had assembled quite a force.

The result had practically been decided from the beginning anyway.

A sea of corpses and blood.

It was a sight that only that four-character idiom could describe. The strange man, who had once again left his mark in an unnamed gorge in Guizhou, picked up the weapon he had left leaning against a rock.

Clang. Clatter.

His Zen staff swayed with a metallic sound.

Stepping through the pool of blood, he headed somewhere to the south.
## Chapter artifact 649

# Chapter 649

Magic and machines.

Compared to the modern world, where all kinds of conveniences born from civilization had developed, the Murim was certainly filled with conditions that made daily life inconvenient.

Natural, unpaved roads that could wreck your hips and back even while you were merely sitting in a carriage.

Smartphones and Wi-Fi were obviously out of the question, and there wasn’t even any electricity.

The only way to get some would have been to take a direct lightning strike, but that didn’t offer much value for money when you had to exchange your life for electricity.

Still, none of that caused any real trouble when it came to living.

No—my own life had always been so precarious that it would be more accurate to say I’d never had time to worry about such things.

After that, things were more or less fine.

Someone once said that food, clothing, and shelter were the three most important things in a person’s life. In that sense, I was able to enjoy a fairly luxurious lifestyle as the Third Young Master of the Jin Family of Taiyuan.

*Except for one thing.*

I glared with a grave expression at the non-Han servant belonging to the Inner Palace. Even giving him the benefit of the doubt, he looked about middle-school age.

“I’m going to ask you just one thing. Think carefully before you answer.”

“Yes?”

“Are you looking down on me because I’m Han Chinese?”

The servant’s eyes went round as he waved both hands.

“N-no, sir. How could this lowly one dare…”

“Then why did you bring me to this shithole? I’m pretty sure I asked you to take me to the latrine.”

“T-this is the latrine, sir.”

“I told you to think carefully before answering. If you lie to me one more time, I’ll fill your entire house with shit. You’ve heard of the Beggars’ Sect, one of the Central Plains’ sects, right?”

“Yes? Yes. Isn’t that the sect made up of beggars?”

“You know it well. With one word from me, I can bring several thousand beggars… Okay, maybe not several thousand. Around a hundred. And there’s one fellow named Gung Gibang whose smell is absolutely monstrous. They’ll shit-dismember you and all nine degrees of your kin. So take me to a proper latrine right now!”

The servant flinched at my roar, his eyes filling with tears.

“I-I’m sorry. I’m truly sorry, but this is the cleanest latrine we have.”

Damn it. I’d thought there was no way, but this shithole really was the latrine.

After realizing the truth I had desperately wanted to avoid, my vision went dark. The Central Plains had never been this bad.

“These savages…”

“Yes?”

“Never mind. You can go.”

After sending the innocent servant away, I stared at the narrow space filled with a horrifying stench, then carefully set one foot inside.

*Creeeak.*

The plank beneath my foot let out a shriek. Once I closed the door, it felt as though I had entered a chemical-warfare chamber for one. With a stiff expression, I muttered inwardly.

*Could this be a trap Baeksang dug for me?*

I had seen it plenty of times in martial-arts novels. A scene where some incredible master gets assassinated in a latrine, or something like that.

But after checking between the gaps in the planks, even that suspicion disappeared. No matter how devoted an assassin might be to his profession, I didn’t think anyone would hide in here.

*Please. God. Buddha. Namu Amitabha, Guanyin, amen…*

One second felt like ten years.

It was just as I had accepted reality and was holding my breath while doing my business.

*Whoosh—thud!*

Everything happened in an instant.

I reflexively reached out and seized the object that had punched through the old door with a sharp whistle.

*An arrow?*

The instant I recognized it, I shot into motion like lightning.

*Boom!*

The door shattered, and fresh night air welcomed me.

But that was all.

There was nothing around me. Nothing except the cheers and musical instruments I could hear from somewhere not too far away.

But…

*Southeast.*

For someone at my level, it wasn’t difficult to work out the direction from which the arrow had come. Once I had a general idea, I kicked off the ground without hesitation.

*Boom! Whoosh!*

The wind swept across my entire body.

I stepped onto a wall and leaped up, climbing onto the highest pavilion. From there, the whole Inner Palace spread out below me.

Torches brightly illuminated every corner. People enjoyed the banquet in the training ground. Warriors stood guard throughout the area.

*Who the hell was it?*

No matter how far one had risen into the Supreme Peak realm, there were limits.

The Inner Palace was too vast to take in at a glance, and there were several times more people moving through it than usual.

And unfortunately, the warriors of the Nanman Beast Palace, who had been on alert against any possible situation, took their professional duties very seriously.

“Southwest! On the pavilion!”

“What kind of bastard are you?”

*Peeeep!*

Along with the sharp sound of a whistle, the warriors patrolling the Inner Palace swarmed in like ants.

Of course, something arrived before the people did.

*Whoooosh! Boom!*

Hmm. Things seemed to have gotten a little complicated.

I glanced at the arrow and spear embedded near my feet, then checked the arrow in my hand once more.

Compared to the ones that had just flown at me, its size and shape were identical.

But there was one major difference I hadn’t noticed.

*This is…*

A small leather bundle hanging from the arrow’s fletching.

The moment I realized it was there, dozens of torches flared to life beneath the pavilion where I stood.

“You are surrounded!”

“Reveal your identity and surrender immediately!”

The timing was incredible.

After a very brief moment of thought, I made my decision and silently recited a command in my mind.

*Open Inventory. Store.*

*Ding.*

With the System’s distinctive clear chime, the arrow in my hand vanished as if it had never existed.

Unable to make out what had happened in the darkness, the warriors of the Inner Palace shouted again.

“This is your final warning! Disarm yourself and surrender!”

“Put both hands above your head right now! Otherwise, we’ll put an arrow hole through your skull!”

“…”

That was a pretty savage script.

Was this what they called a local patch?

I uneasily smacked my lips at the threats from the Nanman version of the NYPD, then raised both hands above my head as instructed.

Once they learned my identity, the misunderstanding would be cleared up quickly. A few reasonable excuses should be enough to end the matter.

If I caused any more trouble, I would only be the one in a worse position…

But why did all of them look like that?

*They look as though they’ve seen a ghost.*

Then, in the next moment, I realized.

*Fwoosh.*

A breeze blew in from somewhere, and I noticed that my lower half felt particularly cool tonight.

*Whoosh.*

“A-ah!”

“Good heavens…”

Dozens of torches shone on me like spotlights.

As I heard the gasps of the warriors who had temporarily forgotten their duties, I thought,

*I’m really screwed.*

I’d forgotten to get my pants back in order.

* * *

“I’m asking this because I’m genuinely curious.”

Namho, whom I met approximately half a shichen later, spoke calmly with a composed expression.

“You bastard, are you Dark Heaven?”

“…”

“You keep doing this because you’re Dark Heaven, right? Huh?”

“…”

“Of course. There’s no way you’re not Dark Heaven. Otherwise, why would the head of a Murim Alliance pavilion come all the way to Nanman, punch a great chieftain in the solar plexus, then climb onto a pavilion in the middle of the night and expose his lower half? You came here determined to screw up the alliance admission from the start, didn’t you? Am I wrong?”

Taishan, who occupied one place at the table and was chewing on something, suddenly raised his hand.

“Namho, what is Dark Heaven? Taishan is curious.”

Namho stared deeply into Taishan’s eyes before turning his head toward Sama Pyo.

“I’m asking this from the bottom of my heart. How do I padlock that fucking bastard’s mouth shut?”

“Hmm.”

After thinking for a moment, Sama Pyo rose from his seat.

“I’ll bring more food.”

“Good idea. But as an agent of the Hidden Shadow Pavilion with sharp insight, let me add one thing. Don’t bring the food here. Take that bastard to the food instead. I think I’ll go insane if I have to listen to even one more word of his bullshit.”

“…”

“…”

Namho was a fairly eccentric man even under normal circumstances, but today, he was more than eccentric.

He was razor-sharp.

He was so frightening that even clueless Taishan looked scared and apologized.

“Taishan… was wrong…”

Namho glared at Taishan with a terrifying gaze, then steadied his breathing.

I instinctively realized it was my turn and spoke first.

“Well… there was a bit of a misunderstanding.”

“A misunderstanding? What kind of dogshit misunderstanding?”

“Please don’t put it like that. Just listen to what I have to say…”

“I heard everything! I heard every last bit of it! There are even witnesses! More than two hundred people saw it! Did you send Young Lady Ju here for this? Is that your thing?”

“Wow, now that you mention it, it would’ve been a disaster if Young Lady Ju had been there. It’s a real blessing she wasn’t…”

“You little baaaastard!”

*Boom! Crack!*

That old man was over eighty, but he sure was strong. He had smashed apart that sturdy table with one blow.

I barely managed to stop myself from applauding on instinct.

If I provoked Namho one more time in this situation, he looked like he might die of anger.

“Elder Nam, calm down. Calm down.”

“Huff. Hah.”

“Take a deep breath, then let it out. Good. That’s it.”

Sama Pyo soothed Namho with a concerned gaze that didn’t suit an unorthodox faction, then turned to me.

“Regardless, Pavilion Master, is what you just said true?”

“Yeah, damn it. There was a very slight misunderstanding that I can’t exactly tell anyone else about…”

“Did you really send Young Lady Ju here for this?”

“You fucking bastard.”

How had things ended up like this? At this rate, my nickname would change to the *Naked Divine Dragon*.

I looked up at the ceiling and lamented before finally opening my mouth.

“That’s not it. I was attacked beforehand.”

“What?”

“An attack?”

“Oh, Taishan knows what an attack is.”

Three pairs of eyes focused on me at once.

Namho’s eyes widened as he hurriedly asked,

“When? Where?”

“In the latrine. I was doing my business when an arrow came flying from outside. I came out immediately to find the culprit, and this is how things ended up. I didn’t even have time to pull up my pants.”

“Then the culprit! Did you catch the culprit?”

“Do you think I did? It was shot from far away, and there were so many people in the Inner Palace that I failed to find him.”

It would have been easier if a dagger or poisoned needle had flown at me instead. Weapons like those had a much more limited range.

But a bow was a long-range weapon capable of attacking from quite a distance, which made finding the culprit that much more difficult.

“But why didn’t you tell us from the beginning? If it was an attack, you could have immediately reported it to the Palace Lord and had the culprit tracked down.”

Namho had a point. In fact, I had considered telling them the truth.

It would have been much better than being treated like a pervert wandering around at night with his pants off.

But…

“It was an attack, but I don’t think it was an attack.”

“What?”

“What does that mean?”

“Taishan knows about attacks, but Taishan does not know about attacks that are not attacks. Explain so Taishan understands.”

“Die. Please die.”

Namho silenced Taishan in a single stroke, then frowned.

“It wasn’t an attack?”

“Yes.”

“Then there was something hidden. Tell me in more detail.”

“I only found out later, but there was something strange attached to the arrow.”

As I answered, I spread my Qi Sense over a wide area.

After confirming that there was no one nearby, I silently recited another command in my mind.

*Open Inventory. Summon.*

*Ding.*

I felt something land in my hand.

I naturally pulled out the hand I had kept inside my robes.

Then I took out the arrow that had flown into the latrine and untied the small leather pouch hanging from its fletching.

The leather, which had been rolled up, unfurled across the table.

It was smaller than a child’s palm, and tiny letters had been written across it.

> Today. Insi[^1]. West Gate.

It was a missive—an invitation from someone whose identity I did not know.

[^1]: Insi is the traditional time period from three to five in the morning.

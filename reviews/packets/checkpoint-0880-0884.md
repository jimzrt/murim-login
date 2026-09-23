# Checkpoint Review — 880–884

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

# Chapters 880–884

## Plot

As rumors spread that Prince Shangshan has returned and the Emperor has an heir, Jeong Hogun stops the Embroidered Uniform Guard’s interrogations and orders the prisoners released. He tells another officer the rumors are true and that the court will soon announce them publicly. Jin Taekyung learns Ma Sanbao spread the rumors using information Taekyung supplied. Taekyung, Hong Jin, and Hyuk Mujin worry the imperial banquet may be a trap.

Ma Sanbao meets secretly with allies from a faction of survivors and signs a pact to overthrow the Emperor. He and the Grand Secretary expect the banquet to bring the rival factions into conflict. Ma says the person his allies asked about is safe and predicts Taekyung will help them; he believes Taekyung’s master could change the balance.

Taekyung’s group enters the palace under false identities as the Blazing Flame Troupe, with papers and disguises arranged by the East Depot. The Divine Physician gives them Energy-Dispersing Poison to conceal their martial skill during screening; Jeok Cheongang can conceal his aura without it. During the screening, Jeong Hogun discovers poison on a courtesan. She kills herself after confessing that she sought revenge for her family’s deaths twelve years earlier, and her companions are taken to prison. Taekyung intervenes when Hogun turns to question Taishan, claiming he is helping protect Shangshan and the Emperor from an attack. With help from one of Ma Sanbao’s allies among the officials, the troupe is allowed through.

## Continuity

- The Emperor has confirmed the rumors of Shangshan’s return and an heir, and plans to announce them at a banquet attended by Shangshan and civil and military officials. The Emperor’s intentions and whether the banquet is a trap remain unclear.
- Ma Sanbao spread the rumors using information from Taekyung. He leads a covert faction seeking to overthrow the Emperor; its members have signed a pact and expect the banquet to become a confrontation.
- Ma says the person his allies asked about is safe and expects Taekyung to help. He considers Jeok Cheongang potentially decisive. The person’s identity and the faction’s preparations remain undisclosed.
- Taekyung’s group has an official invitation to perform as the Blazing Flame Troupe. They are inside the palace’s Outer Palace under circus-performer disguises arranged by the East Depot.
- The Divine Physician gave the group Energy-Dispersing Poison for screening; Jeok Cheongang can conceal his aura without it. Taekyung cannot currently use Qi Sense.
- A courtesan who sought revenge against the Emperor died during screening; her companions were taken to prison.
- Taekyung suspects the Emperor is connected to Dark Heaven, but this is unconfirmed. The late Emperor’s suspected connection to Blood Soul Gu and the City Lord of Sichuan Province’s death also remain unresolved.

## Translation Decisions

- Use “Hongmen Banquet” for 鴻門宴, retaining its implication of a banquet that may conceal an assassination attempt.
- Render 연판장 as “a pact bearing their signatures” and retain “Hongmen Banquet” for 홍문연.
- Retain “Blazing Flame Troupe,” “circus troupe,” and “Energy-Dispersing Poison.”
- Treat Geosan as Taishan’s uncertain name variant, not a confirmed separate person.

## Durable state

{
  "active_continuity": [
    "The Emperor has confined Prince Shangshan in Qianqing Palace; Taekyung returned without him.",
    "The Emperor plans a banquet attended by Shangshan and civil and military officials; Hong Jin suspects it could be a trap.",
    "Ma Sanbao spread rumors using information Taekyung gave him; the Emperor ordered the arrested rumor-spreaders released.",
    "Ma Sanbao leads a covert faction of survivors seeking to overthrow the Emperor; they have signed a pact and expect the banquet to become a confrontation.",
    "Ma Sanbao says the person his allies asked about is safe and expects the young martial artist to help; he believes the martial artist’s master could be decisive.",
    "Taekyung suspects the Emperor is connected to Dark Heaven, but this is unconfirmed.",
    "The late Emperor died after a period of mental confusion while confined; Taekyung suspects Blood Soul Gu may have been involved, but this is unconfirmed.",
    "The City Lord of Sichuan Province showed strange symptoms before his death, and Blood Soul Gu was found in his corpse.",
    "Jeok Cheongang received two letters, burned them, and said the group was formally invited to the imperial palace; their contents remain unknown.",
    "Taekyung’s group has an official invitation to perform as the Blazing Flame Troupe at the imperial banquet.",
    "Jeok Cheongang’s group entered the Outer Palace disguised as a circus troupe; the Divine Physician gave them Energy-Dispersing Poison to conceal their martial skill during screening, while Jeok can conceal his aura without it.",
    "A courtesan seeking revenge against the Emperor died by her own hand during Jeong Hogun’s screening; her companions were taken to prison."
  ],
  "continuity_sources": [
    884
  ],
  "open_questions": [
    "Is Aehyang pregnant, and what does the Emperor intend for her and Shangshan?",
    "Will the banquet become a confrontation, and what does the Emperor intend?",
    "Did the Emperor or Dark Heaven use Blood Soul Gu against the late Emperor and the City Lord of Sichuan Province?",
    "Who is the person Ma Sanbao’s allies asked about, and what preparations has the faction made?",
    "Who is the familiar young man who approached Jeong Hogun, and what will happen when Hogun questions Taishan?"
  ],
  "safe_through": 884,
  "temporary_decisions": [
    "Render 기관진식 as “mechanisms and formations”; retain “Third Shadow,” “First Shadow,” “No Shadow,” and “Marquis Within the Passes.”",
    "Use “imugi,” not “dragon,” for the creature Taekyung killed at Dongting Lake.",
    "Render 연판장 as “a pact bearing their signatures”; retain “Hongmen Banquet” for 홍문연.",
    "Treat 거산 as Taishan’s uncertain name variant, not a confirmed separate person; render 열화단 as “Blazing Flame Troupe” and 마희단 as “circus troupe.”"
  ],
  "version": 1
}

## Reading copies

## Chapter artifact 880

# Chapter 880

A fire that sprang up in a dense bed of reeds could not easily be stopped, even by a fierce storm.

Neither could the rumors that had suddenly begun sweeping through the imperial capital.

“Have you heard? It’s about His Highness, Prince Shangshan. He’s in the imperial palace right now…”

“They say His Majesty the Emperor has finally had an heir.”

“I heard they’ll hold a great banquet soon. That must be why His Highness, Prince Shangshan, returned after more than ten years.”

“But an heir? Does that mean Her Majesty the Empress is pregnant?”

“Who knows for sure? All I heard from Zhang next door is that it’s a new concubine the Emperor recently took…”

“Zhang next door? The butcher, Zhang?”

“That’s the one. You know him too?”

“Of course. He’s incredible at slaughtering livestock. But where on earth did Zhang hear something like that?”

“From someone, what was his name… Oh, right. Mr. Wu, who runs a shop across the street.”

“Then who did Mr. Wu hear it from?”

“Li the woodcutter.”

Even the Embroidered Uniform Guard, who could catch a bird in flight and drag it off to prison, found it all but impossible to silence so many tongues.

The rumors spread so fast that the towering, impregnable walls of the imperial palace might as well have been nothing. In a single night, the Embroidered Uniform Guard dragged away hundreds of people.

“If you want to live, tell us everything. Which bastard has been spreading this nonsense?”

“Eek! I’ll tell you! I’ll tell you everything!”

What kind of place was the Embroidered Uniform Guard?

Once you were dragged in, you were as good as dead. It was a terrifying organization that cut down even the most prominent high officials like weeds.

The accused knew its reputation well. Before the guards even brought out the torture devices, they confessed everything they knew. Yet despite these smooth interrogations, the Embroidered Uniform Guard had gained nothing.

“What did they say?”

“They’re all saying the same thing. They heard the rumors from ordinary neighbors with no ties to the imperial palace, street vendors, or strangers they met at inns and pleasure houses.”

“Damn it.”

During the interrogations, countless names of ordinary people had come up, but every one of them was a dead end.

The people named by the accused were as ordinary as they came, and the true source of the rumors—which had begun spreading far and wide from somewhere—remained elusive.

But they were the Embroidered Uniform Guard.

In this vast realm, they gave their absolute loyalty to one person alone: the Emperor.

The Embroidered Uniform Guard, who had to produce meaningful results under any circumstances.

“Begin the real interrogation.”

“Pardon?”

“It doesn’t matter what methods you use. We must find the culprits as soon as possible.”

“B-But they…”

“They caused turmoil throughout the Great Nation with that sort of baseless rumor, and tarnished His Majesty the Emperor’s most august reputation. Are they subjects of this country—or traitors?”

At their superior’s shout, the Embroidered Uniform Guard officers fell silent. They knew the trembling prisoners in the cells were simply ignorant commoners.

This was little different from being told to find a gold vein in an abandoned mine that had been stripped bare.

Just as no storeroom was so clean that shaking it wouldn’t stir up dust, countless high officials had passed through the Guard’s prison, each with a crime or two to their name, great or small.

But these people were just ordinary subjects. When strong winds blew, they bent; when it rained, they got wet.

And now they were to be tortured.

They had to produce results for their superiors—even if that meant killing the prisoners horribly or leaving them half-crippled.

The Embroidered Uniform Guard took pride in punishing corrupt or disloyal officials to set the Great Nation in order. They could hardly help feeling uneasy about this.

But…

“Answer me!”

At their superior’s renewed roar, those who had remained silent realized there was nowhere left to retreat.

The rules of the military were strict by nature, and that was doubly true of the Embroidered Uniform Guard, one of the most powerful institutions in the realm.

“We obey the Thousand Captain’s orders.”

They answered reluctantly and were about to return to the prison to carry out the torture when—

“Everyone, stop.”

A middle-aged man appeared with a quiet voice and swept his gaze across the room.

His golden armor was spotless, and his build was imposing. The Embroidered Uniform Guard Thousand Captain recognized him at once, his eyes widening.

“Thousand Captain Jeong?”

Jeong Hogun gave a curt nod and spoke.

“It’s been a while, Thousand Captain Hong. How are the interrogations of the prisoners brought in last night going?”

“We’ll have proper results soon. But what do you mean, stop?”

“Exactly what I said. Stop here. There’s nothing more to dig up.”

At Jeong Hogun’s firm reply, the Thousand Captain, who had been shouting at his subordinates moments earlier, furrowed his brow.

“You’re interfering more than usual today. Are you planning to overstep your authority now?”

“Of course not.”

“Then what is this? No matter how much the Guard Commander favors you, this is clearly—”

“An imperial order.”

“What?”

“I said it’s an imperial order. The moment you receive it, you are to stop interrogating and torturing the prisoners taken last night, and release every one of them within half an hour at the latest. That is His Majesty the Emperor’s command.”

“……!”

“What are you all waiting for? Hurry up and obey the imperial order.”

Jeong Hogun had appeared out of nowhere and settled the matter in an instant.

The Embroidered Uniform Guard officers knelt and formally received the imperial command, then streamed away like the tide to release the hundreds of prisoners. Their superior, the Thousand Captain, asked Jeong Hogun with a stony expression,

“What’s going on? And what about our report on this incident?”

“Forget the whole thing. That is His Majesty’s will.”

Jeong Hogun answered in his characteristically flat voice, betraying no particular emotion, then continued.

“I’ll get straight to the point. The rumors are true.”

“What?”

“I said they’re all true. The imperial court will make an official announcement soon. The Embroidered Uniform Guard will be responsible for the task.”

“……!”

“His Majesty can well guess where the rumors originated, but he said there’s no point in uncovering the precise facts. They planned and spread them so thoroughly that there’s almost certainly no evidence left.”

“T-Then…”

“There’ll soon be a banquet in the imperial palace to celebrate. His Highness, Prince Shangshan, will be there, along with every civil and military official. Until further orders arrive, secure the palace and its surroundings.”

Only a handful of people knew the closely guarded secret concerning the Emperor’s heir.

The Thousand Captain had heard that Prince Shangshan had returned, but not this. His face stiffened like stone.

“You mean to confirm all of that—and announce it to the people? At this point?”

“Exactly.”

“Do you understand what that means, Thousand Captain Jeong? Or do you understand and pretend not to?”

“I understand it well enough. Including something else you’re overlooking.”

“Something I’m overlooking? What do you mean?”

“What a mere military officer like me can guess, surely His Majesty the Emperor knows.”

“……!”

“Obey the order.”

Leaving the speechless Thousand Captain behind, Jeong Hogun turned and walked away. Passing through the dark prison and the people emerging from it one by one, he thought:

*This is where it begins.*

He could feel it.

A great storm would soon sweep through this splendid city called the imperial capital—or, rather, across the whole realm.

And the imperial court’s official announcement would be the arrow that heralded the start of everything to come.

*So many people will gather, and so many words will be exchanged.*

Those who appeared from this point on would not be ordinary people by the dozen.

They were the so-called literati and educated classes—the powerful, who could understand what was unfolding and respond with action, beginning to move.

And in the process…

*At last, friend and foe will be divided.*

Until war begins, it’s impossible to tell who’s an enemy and who’s an ally.

But once each side draws its weapons and a battle begins from which there’s no retreat, the truth finally shows itself.

In whatever form it takes.

*What choice will that bastard make in this war?*

Jeong Hogun suddenly thought of a young man he could never quite figure out.

A reckless young ruffian of the martial world who had thrown himself into the eye of the storm.

* * *

“As daring as ever. Just like a little over ten years ago.”

At Hong Jin’s sudden remark after a long silence, I quietly nodded.

I felt the same way.

*This is more than I expected.*

As soon as Ma Sanbao received the information I’d given him after visiting Qianqing Palace, he acted. He sent out trusted subordinates and spread the rumors across the entire imperial capital.

Everything about Prince Shangshan’s whereabouts, and the Emperor’s heir—something that had yet to be confirmed for certain.

But the Emperor’s actions right afterward were astonishing.

*I can’t believe he admitted it outright.*

Even celebrities caught red-handed by Daspatch tend to keep quiet for a day or two and deny the dating rumors. The Emperor had gone beyond admitting them—he’d immediately announced them.

In less than a day.

*He sure is quick to act, but what on earth is he up to?*

No matter how I looked at it, the more people learned about this situation, the worse it was for the Emperor.

Unless the thing on his shoulders was purely decorative, anyone with a drop of ink on their hands and a working brain would come to roughly the same conclusion.

—Huh? The Emperor secretly brought Prince Shangshan into the imperial palace?

—Huh? The Emperor’s got a junior now, and he hid it until people found out?

—Huh? That pisses me off.

There was only one conclusion to draw from all that.

—The Emperor might eliminate Prince Shangshan!

It would be one thing if he had a good reputation to begin with. But wasn’t the current Son of Heaven the one who’d come to the throne after unleashing a river of blood?

A first-time offender might get probation for a minor crime, but no one would trust a murderer with a criminal record.

*Unless they’re too afraid of the Emperor’s power to say anything.*

In terms of Go, he’d played a terrible move.

Still, this had given us some breathing room.

Our attempt to buy time so the Emperor couldn’t recklessly threaten Prince Shangshan’s safety had become all the more certain.

“Isn’t this a decent situation? Whatever else, the imperial court has acknowledged everything in its own name. For now, the threats surrounding His Highness, Prince Shangshan, will disappear.”

Hong Jin nodded at Hyuk Mujin’s cautious suggestion.

“That’s not wrong. But you should always consider the worst-case scenario.”

“And the worst case would be…”

“Young Master Jin, you can probably guess. You’ve experienced for yourself what the current Emperor is like.”

At their gaze, I smacked my lips and slowly began.

“I can think of two possibilities. One good, one bad. Which do you want to hear first?”

“Hmm. I think it’d be better to hear the bad one first.”

“Mujin.”

“Yes?”

“Read the room.”

“Yes.”

Hong Jin looked sympathetically at Hyuk Mujin, who had quietly shut his mouth, then spoke.

“Start with the good one.”

The good possibility.

I sorted through my thoughts once more, then slowly parted my lips.

“First: now that he’s made it public, the Emperor will find it hard to lay a hand on his only younger brother, and he’ll send him back safely after the banquet.”

“I like that conclusion, but… what’s the bad one?”

“Second: since things have come to this, he’ll accept getting cursed out one more time and slaughter every remaining dissident.”

Hong Jin fell silent. After a long while, he murmured, his expression dark.

“This banquet… could become a Hongmen Banquet.[^1]”

[^1]: At the historical Feast at Hong Gate, a banquet became the setting for an attempt on Liu Bang’s life.
## Chapter artifact 881

# Chapter 881

They say rats hear what you say at night, and birds hear what you say by day.

But the guests who had gathered in a secret room early that morning at someone’s invitation weren’t the least bit troubled by such an old, tired saying.

Rats could be trampled to death. Birds could be shot down.

The only ones they had to worry about were the Embroidered Uniform Guard.

The Guard, little more than the Emperor’s watchdogs, wore golden armor the same yellow as a mongrel’s coat. Their specialty was combing every corner as if hunting for lice.

They sniffed out their target, tracked it down, sank their foul-smelling teeth into its neck, then ran back to their master, wagging their tails.

And with so many eyes and ears throughout the imperial capital, even the most secretive movements were bound to nag at them like a fish bone caught in the throat.

Perhaps that was why.

Though a dozen or so people had gathered in one place, an uncomfortable silence lingered in the secret room for some time.

Until the last person they were waiting for appeared with a faint noise.

Creeeak.

The old hatch overhead opened, and a dim shaft of light spilled in. Their eyes, accustomed to the darkness, narrowed reflexively, but they didn’t let down their guard.

They weren’t sure the unfamiliar man who had just stepped into the room was the ally they knew so well.

The newcomer immediately understood what their eyes were asking.

“Ah, my apologies. I was in such a hurry to get here that I forgot for a moment.”

Krrk. Crack.

“Hmm.”

A low groan rose from them all at once. The dozen or so guests watched the changes around the man with grave expressions.

Shhhk.

His features twisted like a wave.

His long philtrum shortened, his unusually prominent bulbous nose grew sharp, and an odd light appeared in his once-dull, unfocused eyes.

That alone was astonishing enough, but the changes didn’t stop there.

Crack.

With the sound of hundreds of bones shifting out of place, his body alternately shrank and stretched.

The transformation happened in an instant. In the time it took for a blink, not a trace of the man they’d just seen remained.

In his place stood a handsome man in his thirties or forties, with a lean build.

At last, the guests recognized the face before them and let go of the tension that had kept them taut.

“Your skill is as wondrous as ever.”

“We ought to be used to it by now, but we still tense up every time. Brush-Holding Eunuch Ma, your talent truly is remarkable.”

At the admiring remarks from all around, Ma Sanbao, the East Depot’s Brush-Holding Eunuch, smiled faintly.

“It’s just a parlor trick I happened to pick up.”

After modestly brushing off his astonishing disguise technique and Bone-Shrinking Technique, Ma Sanbao continued.

“More importantly, it seems everyone arrived at the appointed time. I hope the journey here wasn’t too inconvenient.”

The guests answered in more relaxed voices.

“It wasn’t as bad as I expected. Your loyal subordinates helped us, and we disguised ourselves much more thoroughly this time.”

“Of course, this ghastly thing is unpleasant and stifling, but what wouldn’t we endure to evade those Embroidered Uniform Guard bastards?”

Someone pointed to the human-skin mask stretched over his face. The others nodded in agreement.

That was right.

What mattered wasn’t whether this skin belonged to a person or an animal.

Their only goal was to overthrow the man sitting on the throne now—the Emperor who had brutally slaughtered countless friends with whom they had shared their affection for so long, and comrades with whom they had stood side by side in pursuit of their ideals, before turning that fearsome blade on them.

“We can’t let ourselves be crushed so easily again. Not if we want to save our families and our people.”

“What can we do? There’s no taking back water once it’s spilled. We were all at fault for underestimating the Emperor—or rather, the Fourth Prince.”

“Indeed. But that doesn’t mean we have to scoop up water that’s already dirty.”

“Couldn’t agree more. We can refill the vessel as it empties, and replace the cracked, bloodstained one with a new one.”

For a while, they spoke in measured voices.

They had ridden the tiger and were now clinging to its back. Only two choices remained: let fear drive them to climb down and be eaten alive, or hold on with all their might until the exhausted tiger could take no more—and plunge a dagger into the back of its neck.

Everyone gathered here had chosen the latter.

For survival, in the narrowest sense. And for a great and glorious future, in the broadest.

Thus, their fervent hopes and wishes came together, and at last a document bearing all their signatures was born.

They would wait for the day when the time came to defy heaven.

Fortunately, they didn’t have long to wait.

More than a decade had passed since the day the imperial capital ran red with blood.

White frost had settled on the heads of the old ministers who had barely survived, but the faction they’d secretly built with painstaking effort had grown even stronger and larger. The child who had left for the frontier, bundled in swaddling clothes, had returned as a boy. And an ominous air was slowly gathering over the imperial capital.

“Now everyone is watching the Emperor. The civil and military officials, and even the ignorant common folk.”

“We only meant to buy ourselves a little time by spreading the rumors, but instead of denying them, he announced them to the whole world.”

“For once, that cunning Emperor has made a blunder. Now that he’s made the announcement, the flames will grow beyond anyone’s control.”

“Scandalous stories about the Emperor keep surfacing everywhere. It’s hard to guess what he’s planning.”

“Ten years can change even mountains and rivers, but people don’t change easily. Just look at me. I was already past seventy back then, and I’m still going strong.”

“What do you mean…?”

“The Emperor is the same. This is one of his schemes. Perhaps he means to unleash another storm of blood.”

At the old-sounding voice of someone wearing a precise human-skin mask that made him look middle-aged, the others let out low groans.

Was it because they hadn’t expected it at all?

No. It was because his words had sharply pointed to the truth they were all trying to ignore.

They too had stumbled and rolled around in the filth of politics, and lived to tell the tale.

They knew firsthand just how ruthless and daring the Emperor was.

Still, it was hard to shake the question: would he really go that far?

“Isn’t that an overstatement? If the Emperor really intends to do that, rebellions might break out throughout the realm. No—they certainly will.”

At that, the old minister disguised as a middle-aged man burst into a hearty laugh.

“His own home, with all its furnishings and storehouses, is about to go up in flames. Why should he care about a fire approaching from a thousand *li* away?”

“……!”

“Stop saying foolish things and face reality. Like Brush-Holding Eunuch Ma.”

Every head turned toward him at once. Ma Sanbao, who had been listening quietly to the conversation, broke his long silence and spoke.

“It’s just as I’d expect from the man who nurtured so many pillars of the Hanlin Academy. Your mind is as sharp as ever, even past eighty.”

“Brush-Holding Eunuch Ma. Then…”

“I agree with His Excellency the Grand Secretary.”

“……!”

“This is not merely my personal judgment. It is my judgment as the East Depot’s Brush-Holding Eunuch.”

The others fell silent for a moment. Ma Sanbao had invoked his title as Brush-Holding Eunuch for a reason.

“Then a storm of blood will sweep through the court.”

“It will.”

Even as someone groaned, Ma Sanbao continued in an unwavering voice.

“But it’s already clear whose blood will be mixed into that wind. The storm is almost upon us, and both sides will have to throw everything they have into the clash.”

“Brush-Holding Eunuch Ma. Forgive me for asking, but can we really stand against the Emperor? From what we’ve learned so far, their forces are far beyond what we expected…”

The one who’d cautiously spoken regretted it at once.

Ma Sanbao’s eyes had shot toward him, cold and keen as a blade, making his heart sink.

“I—no, forgive me. I misspoke.”

He forced out his apology in a voice that would barely come. Ma Sanbao withdrew his gaze as if nothing had happened and replied calmly.

“That was unusually careless of you.”

“……”

“We’ve trusted one another and boarded the same boat. We have to row together if we’re going to get anywhere. Isn’t that right?”

“Let me apologize once more. I’m truly sorry.”

For a moment, Ma Sanbao’s response had chilled the air in the room. But he was also the one who warmed it again.

“Don’t worry. We have more than enough justification and strength to bring the Emperor down.”

“What do you mean…?”

“I can’t tell you everything, but we’ve made sufficient preparations for this great undertaking. Please understand that I can’t say more than that.”

When Ma Sanbao put it that way, the others quietly folded away the questions lingering on their tongues and tucked them into a corner of their hearts.

The fewer people who knew a secret, the better.

Besides, though each of them had contributed some measure of influence and power, Ma Sanbao was one of the key figures at the very heart of this plan.

Much like a certain old minister, once a Grand Secretary of the Hanlin Academy—the cradle of the realm’s talent—who still held sway over the court even after retiring from office.

“By the way, how is that person doing?”

Ma Sanbao immediately understood the meaning behind the sudden question and answered.

“That person is still safe.”

“I’m worried. The Emperor must be watching for an opportunity every chance he gets.”

“But he won’t get what he wants. I’ll say this with confidence: for now, even the Emperor won’t find it easy to reach that person with his evil designs.”

“The whole imperial capital is boiling like a pot left over a fire. Before long, it’ll spill over in every direction.”

“When do you think that will happen, Your Excellency?”

The old minister answered without the slightest hesitation.

“The banquet. The one the Emperor announced when he acknowledged the rumors.”

“I think so too.”

“It’ll be a Hongmen Banquet.[^1] Their spears and swords will decide who lives and dies.”

“It won’t be the same as Hongmen. Xiang Yu was foolish enough to let Liu Bang live, but the Emperor won’t make that mistake.”

The old minister quietly nodded, lost in thought. Then he suddenly spoke.

“What about that young martial artist? What do you think he’ll do?”

“He’ll help us. Just as we expected.”

“I’ve heard he possesses martial arts far beyond what you’d expect for his age. But there are several masters around the Emperor who are just as strong. Do you think he’ll be much help?”

“Who knows?”

Ma Sanbao continued with a faint smile.

“But if he has his master, that changes things.”

[^1]: At the historical Feast at Hong Gate, a banquet became the setting for an attempt on Liu Bang’s life.
## Chapter artifact 882

# Chapter 882

From the day the imperial proclamation was posted in the streets, the area around the imperial palace grew busier than ever.

The people, and their reasons for coming, were all different.

Commoners lingered outside the palace, hoping to catch even a glimpse of the ill-fated young prince they’d heard about only in rumors. Confucian scholars who fancied themselves men of loyalty and righteousness shouted at the top of their lungs, demanding to know why Prince Shangshan had been summoned in secret at a time like this. And poets and writers hoping to land themselves a position took the opportunity to compose and recite poems for the Emperor, who had finally secured an heir.

“How long are we supposed to wait? We can’t see a damn thing from here, Prince Shangshan or no Prince Shangshan.”

“You fool. Did you think His Highness would come out and say, ‘Oh, you’re here,’ just because we’re waiting? We’re only here because you never know.”

“Fair enough. But why are those high-and-mighty people so desperate to tear each other apart?”

“Perhaps because they don’t share the same beliefs.”

The commoners murmured as they watched two groups of scholars argue, their faces flushed red.

“What? The Emperor having an heir is the Great Nation’s good fortune and a joy to all its people? It’s men like you, you toadies, who are ruining this country!”

“Shut your mouth! How dare you say that in His Majesty’s presence… Right outside the imperial palace, of all places!”

“Disgraceful nonsense? Is that all you can say, you vermin who pretend not to see what’s happening right in front of you?”

“What did you say? Vermin? I’ve heard enough from you, you backwater scholar!”

“You bootlicking son of a bitch! Which academy are you from?”

“So what if you know? What are you going to do about it?”

“You son of a—Everyone! Words won’t settle this! Let’s drive those toadies out of the capital!”

“Yeah!”

The sight of hundreds of scholars hurling fists and inkstones at one another was quite a spectacle all on its own.

“Hit him! Get him!”

“Grab that one first!”

Shouts and screams rang out from every direction. Someone watched the scene with their mouth hanging open, then muttered,

“This is the greatest contest since the founding of the nation.”

But the fierce brawl ended as suddenly as it had begun.

And it wasn’t the imperial guards watching the fight from up close with keen interest who stopped them.

Thud.

Amid the chaotic brawl, a scholar backing away with a brush gripped like a dagger felt something strange touch his back.

*Have I already been driven up against a wall?*

That couldn’t be right.

The main road in front of the imperial palace was so wide that a hundred grown men could walk abreast without bumping shoulders. Besides, there wasn’t anything nearby that could be called a wall.

*And it doesn’t even feel completely hard.*

So what was it?

The scholar started to turn around cautiously. At that very moment—

“You rat!”

“Gah!”

“I’ve finally got you—!”

One of the poets and writers, a pair of inkstones in his hands as he raced through the battlefield, charged toward the scholar—and suddenly froze. His mouth slowly fell open as he lifted his head.

Not toward the scholar’s face, only a few paces away, but far above it.

“Uh, uhh. Uh…”

A dazed voice escaped his lips. At the same time, a huge shadow fell over him.

Step.

With a particularly heavy footstep, the scholar was shoved forward. He gulped, then turned around and finally understood.

The thing behind him hadn’t been a wall at all.

It was a monstrous man, tall as a wall and hard as a boulder.

“……!”

“……!”

The air, just moments ago burning with the heat of a brawl, froze in an instant. By now, everyone gathered along the road in front of the imperial palace was staring, mouths agape, at the giant who had suddenly appeared.

*What kind of monster is that…?*

A shock flashed through everyone’s minds like a bolt of lightning.

They had long since forgotten the sharp disagreement they’d been having only moments before.

People stared in stunned disbelief at a giant unlike any they had seen before—or would ever see again.

Even from a rough glance, he stood well over nine feet tall.

His limbs were like pillars; a single swing of his arm looked as if it could raise a gale. The muscles covering his entire body like armor made people’s knees go weak just looking at him.

And what about that head, perched on his thick neck like a boulder?

Never mind that it was as big as a well-grown pumpkin. Every time those enormous eyes blinked, people felt as if their lives were being shortened.

The scholars who, only moments ago, had dared to demand an explanation from the Emperor were especially beside themselves.

*Could he be an Embroidered Uniform Guard?*

*No. The Guard recruits from among ordinary people. That thing isn’t human.*

*A secret weapon! The Emperor raised a secret weapon to wipe out his opposition!*

To hell with loyalty and righteousness. At the sight of that terrifying giant, their hands and feet trembled and their heads went numb.

If they were formally sentenced to drink poison or be beheaded, at least people would call it an honorable death. But if they took even one slap from that hand larger than a pot lid, they’d die like dogs.

And yet…

“Y-You think we’ll back down just because of that?!”

The scholar who would go down as the first person to discover the giant—and probably the first person to die at his hands—in the annals of the Great Nation’s scholarly world, barely managed to force out a voice that wouldn’t come.

“J-Justice still lives! Even if you kill everyone here, the whole world will learn of your wicked plot!”

He addressed the giant in front of him, and the Emperor as well.

How many years had he spent committing the words of ancient sages to heart, beginning with the Four Books and Three Classics?

There was right and wrong in all things, and a nation could stand only if it upheld the Three Bonds and Five Relationships. The scholar bit down so hard his lips bled as he thought,

*I’d rather die here than spend what remains of my life cowering beneath the Emperor’s power!*

If he died for a great cause, protecting Prince Shangshan and the world, it would be worth it.

His body trembled like an aspen, but his steadfast heart would break before it bent. He forced down his fear and looked up at the giant.

Then he realized that hundreds of imperial guards had surrounded them. He knew death was coming.

At least, until the commander of the guards shouted in a trembling voice:

“W-Who goes there?!”

“……?”

“……?”

“St-Stand there and identify yourself!”

The scholar, along with everyone watching, blinked and thought:

*What the hell?*

*Weren’t they on the same side?*

*Then what’s that monster?*

And then—

The giant, who had stood there like an iron wall without saying a word, finally spoke.

In a voice as innocent as a child’s, he said,

“I am Taishan—no, Geosan. I don’t want to get in trouble. I don’t know what I did wrong, but I’m sorry.”

“……!”

“……!”

“I just heard a noise and came to watch. Can I go on my way?”

In an instant, the tense atmosphere crumbled like a bowstring snapping.

*He came to watch? He just came to watch?*

*He’s sorry? He doesn’t want to get in trouble? He apologizes that easily?*

*And what’s with the way he talks?*

Everyone was at a loss for words as the giant blinked slowly, like a young calf.

“Y-You little bastard, I finally found you! Hey! Stand right there! You’re built like a damn mountain, so why the hell do you vanish like a squirrel the moment I look away?”

The voice rang through the hushed crowd. An old man with dark skin, barely five feet tall, shoved his way through the throng and ran over. He delivered a fierce whack to the giant’s thigh, then noticed all the eyes fixed on him and froze like a statue.

“……”

“……”

In the awkward silence, the commander of the guards looked back and forth between the young giant and the old dwarf, his eyes gone cold.

“Who exactly are you, old man?”

After a brief silence, the old dwarf answered,

“Just an ordinary traveler passing by.”

“You look awfully suspicious. Do you know each other?”

“Unfortunately, yes.”

“Then what’s your relationship?”

“I’ve no idea what that idiot thinks of me, but whenever he falls asleep, I try to strangle him. Sadly, I’ve failed every time.”

The commander of the Embroidered Uniform Guard looked at the giant’s neck, thicker than a bull’s, and murmured in understanding.

“You sound even more suspicious now.”

“I hear that a lot. It’s because of the big fellow next to me.”

“Have you ever been arrested by the local authorities because of him?”

“Not once.”

“Then let’s make this your first time. Guards!”

Clang!

Sharp spears and swords flashed in the tightly clenched hands of the guards. The old man let out a deep sigh at their menacing show of force, then spoke.

“Could you wait just a moment?”

The commander answered firmly, his expression and tone hardening.

“Not a chance. Hand over your identity tag before blood is spilled.”

“My companion has it, so that’s going to be a bit difficult.”

“Then you’ll learn what a truly difficult situation is. And you say you have a companion? Is there another accomplice?”

“He’s not an accomplice… Hey, don’t just stand there like an idiot. Go call your wet nurse.”

“Wait! Don’t try anything!”

The guards nearby sensed trouble and hurried to stop him, but they were too late to prevent the giant’s shout.

“Fiiive-spiiice poooork!”

The people filling the street outside the imperial palace were startled once by the immense shout that battered their ears, then twice by the strange words it contained.

*Why is he suddenly asking for five-spice pork?*

*Is he really crazy?*

Even the commander of the Embroidered Uniform Guard was thrown into confusion.

Why was he shouting about five-spice pork out of nowhere? Was the name of those suspicious men’s accomplice Five-Spice Pork? Or had something gone wrong with his ears?

But it was none of those things.

The giant had simply shouted because he wanted to eat five-spice pork right then and there, and his companions had been through this kind of situation so many times they were sick of it.

Put simply, they knew better than anyone that there was only one man in the world crazy enough to shout so loudly and desperately for five-spice pork on the road outside the imperial palace.

And that this very man was their companion, who had wandered off while they’d looked away for a moment.

“Tai… no, Geosan!”

At the urgent shout, the crowd parted like the sea drawing back.

At the same time, the people who’d thought nothing could surprise them anymore had to rub their eyes once more.

A carriage pulled by two horses was racing toward them at a mad pace.

“Whoa! Whoaaaa!”

“Move! Get out of the way!”

The scene became a complete uproar. The carriage didn’t manage to stop until it reached the tense guards.

A young man jumped lightly down from it and hurriedly felt over the giant’s body.

“Are you all right? Are you hurt anywhere?”

“Hehe, I’m fine. Everything’s good except I’m hungry.”

The giant answered with a goofy grin, like a five-year-old child. The onlookers shuddered again, but not the commander of the guards.

He watched as people spilled out of the little carriage and thought,

*What is this group?*

There were seven of them in all.

A pretty girl with noticeable freckles, and a young man beside her with a face stiff as a log.

A giant who looked like a walking natural disaster, and a young man who handled that mountain of muscle as if it were a delicate piece of porcelain. An old man smiling placidly like an immortal amid all the chaos, and a short, dark-skinned old man beside him muttering curses.

And finally…

*Is that a monk?*

For some reason, even his eyebrows had been shaved clean off. He was a mean-looking, thoroughly disreputable monk.

*What the hell is going on?*

He guarded one of the imperial palace’s twelve gates and had seen all kinds of strange things, but he swore he’d never seen anything like this.

As the commander hesitated, bewildered, the mean-looking monk who had been the last to climb down from the carriage approached and held something out to him.

“What is this?”

“What is this? You son of a—”

“……?”

“Ah, that came out wrong.”

As if trying to hold back his anger, the disreputable monk took a deep breath and continued.

“We’re the circus troupe performing at the banquet. That’s our official letter of introduction.”

“A circus troupe?”

“That’s right. To liven things up, some bigwig or other invited us.”

The commander hurriedly unfolded the letter in his hand. His eyes widened when he saw the seal of a high official—someone far beyond his station to question.

“This is…”

“You’ve seen it, so you know. Open the gate already.”

He might only be a junior officer, but he was a hundred-man commander in the imperial guard, responsible for protecting the capital. To be spoken to like that by a troupe of traveling performers—

But whoever backed this troupe was beyond anything he could handle. The commander swallowed his anger and ordered his men to open the gate, committing the troupe’s name, written on the letter, to memory.

*The Blazing Flame Troupe? What a tacky name.*

Of course, it never crossed his mind that if he’d said that out loud, the monk would have beaten him half to death.
## Chapter artifact 883

# Chapter 883

It was only natural for the imperial palace to be heavily guarded.

But ever since the current Son of Heaven took the throne, the palace had become an impregnable fortress unlike anything in the past.

Ten times as many guards, and security that kept outsiders out without exception.

Even a government official whose face was well known couldn’t enter or leave without an authorized pass.

Some gossips had even dared to call the palace:

The largest, most splendid prison in the world.

But today, even that derisive nickname aimed at the Emperor felt out of place.

“Affiliation and name.”

“I’m Hong, from Seok Family Manor. Here are the identity tags and inventory of the belongings of the people who came with me.”

“Ah, forgive me. I wondered who it was, and it turns out you’re the steward of Seok Family Manor. Is your Family Head keeping well?”

“Thanks to Your Excellency’s concern, he’s as hale as ever.”

“Ha ha, I’m glad to hear it. I’m afraid we’ll have to continue our conversation later. All right, next!”

“Good day. I’m from the Continental Escort Bureau…”

A grand banquet of such enormous scale required a great many supplies and people.

The imperial palace. The Outer Palace, to be precise, was bustling with outsiders—people rarely seen there over the past decade. Officials drafted from various departments to prepare for the banquet sorted the assorted crowds into groups.

Naturally, people were treated differently according to their status and importance.

The wealthy merchants, who would provide a generous boost to the imperial treasury and the banquet, were welcomed most warmly. Those who had brought rare tribute gifts in hopes of making an impression came second. Far behind them were the performers who had come to lend the banquet some color.

Circus troupes, for instance, whose livelihoods depended on performing all sorts of feats.

“Damn it. A circus troupe at my age…”

The Fire King, Jeok Cheongang, muttered as if lamenting his fate.

If the proud ancestors of the Fire Gate Clan had seen this, they would have wept underground… or maybe not.

Unlike those inflexible bastards from the Nine Sects and One Gang, perhaps they were all gathered up in the heavens by now, peering down from beneath the clouds and laughing.

—Hey, hasn’t that Jeok Cheongang fellow passed a hundred?

—A long time ago. He’s probably lived longer than anyone in our sect’s history. Isn’t dying young practically a tradition in our Fire Gate Clan?

—We’re a one-disciple lineage, but we keep picking out and teaching the most hotheaded bastards in the land. No wonder. Anyway, the imperial palace. That ought to be interesting. Who was that fellow’s Master?

—Me.

—Me? You still haven’t learned your lesson? When an ancestor as exalted as me calls on you, how are you supposed to answer?

—I-I’m sorry.

—Again.

—The seventeenth Sect Leader, Hong. Wi. Ryang!

Something like that, probably.

Imagining his Master standing at attention, Jeok Cheongang felt a lump rise in his throat.

“I’m sorry. Because I raised my Disciple so poorly, even you, Master…”

At the sorrowful sound of his voice, Taishan, standing beside him, spoke with a solemn expression.

“I want five-spice pork.”

“Namho, kill that bastard right now. I’ll allow it.”

“Really? You mean it? I can really do that?”

“No, you can’t!”

Namho eagerly reached to strangle Taishan, but Sama Pyo hurriedly stopped him.

A few steps away, the Divine Physician watched the scene and chuckled.

“It seems there’s no danger of our identities being exposed. Anyone can see we’re a fine circus troupe.”

Jeok Cheongang answered with a disgruntled look.

“Good, my ass. Does it make any sense for me to be in a circus troupe at my age?”

“And what about at my age? At least you look young. I’m an old man through and through.”

“……”

“Now that we’re in this situation, what can we do? Taishan—no, Geosan—that fellow is enormous. A circus troupe is about the only cover that won’t make people suspicious.”

Jeok Cheongang had been full of complaints, but he couldn’t disagree with that.

“That… is true.”

Though the East Depot wasn’t as powerful as it once had been, it could still provide a wide variety of thoroughly prepared false identities.

But half a day before they entered the imperial palace, when an East Depot specialist had come to deliver the human-skin masks and identity tags they needed for the job, he’d taken one look at Taishan and fallen silent for a long while before asking:

“D-Does this man really have to come too?”

“I’d love to leave him behind, but we have no choice. If we left him here, I swear he’d cause trouble. If the Embroidered Uniform Guard caught him, he’d spill everything for one plate of five-spice pork.”

“Taishan not that kind of traitor! Taishan wouldn’t sell out friends for just one plate!”

“Fine. Ten plates, then. Extra meat and spices.”

“Hmm. Hmmmmm. Taishan needs a little time to think.”

“See? That’s what I’m dealing with.”

“Ah…”

“What are we going to do?”

“We’ll have to change his identity. A merchant with that build is out of the question. A circus troupe would be best.”

“A circus troupe? You want to turn this old man into a street clown?”

“I-I’m sorry, but there’s no other answer. You’re all highly skilled masters, so showing even a few tricks should be enough to pass you off as a circus troupe.”

“Tricks? You mean gathering oil in your mouth and breathing fire?”

“That’s right.”

“But for a grand banquet at the imperial palace, that won’t be enough.”

“We’ve already taken some steps on our end, so it’ll be fine as long as you look convincing. But that huge fellow over there will attract particular attention. To be safe, he should practice a few tricks before you go.”

“Tricks. Such as?”

“Like I said, gathering oil in your mouth and…”

“That bastard doesn’t leave anything in his mouth. He chews and swallows everything that goes in, without mercy.”

“Then… tearing apart firewood with his bare hands…”

“That won’t be a problem. He tears people apart with his hands.”

“…Please never say things like that inside the imperial palace. You absolutely must promise me.”

After the specialist’s desperate, repeated warnings, Jeok Cheongang, the Divine Physician, and the Fire Dragon Pavilion members had received new names and faces and been allowed into the imperial palace.

Of course, there was no doubt the East Depot’s immense power had made it possible.

“So everything in the letter was true. I can’t believe we got into that magnificent imperial palace so easily.”

At Jeok Cheongang’s mutter, the pretty, freckled girl beside him—who had been looking around carefully—answered.

“It must have been easier because we’re in the Outer Palace. The Inner Palace is guarded so heavily it can’t even be compared. The Imperial Guard protecting the Outer Palace is elite enough, but the Inner Palace is guarded by the Embroidered Uniform Guard—the Emperor’s personal guard.”

“How do you know so much?”

“My grandfather told me. The imperial family hired him for several important jobs a long time ago.”

“Huh. I suppose that makes sense, given that your grandfather is the Escort King. And you remember stories you heard as a child remarkably well.”

A hint of a smile touched Ju Hwaran’s face, which had been tense under Jeok Cheongang’s proud, affectionate gaze—the kind he never showed anyone else.

That was when it happened.

“Is everyone here?”

A government official with a belly that bulged like a well-fed pig swept his gaze over the group with an arrogant expression. His loose official robes couldn’t hide his girth.

“As the official in charge of the music for this grand banquet, I will inspect and sort you all before the festivities begin.”

Clank. Clank.

The moment the official finished speaking, a heavy metallic clamor rang out.

The golden armor and imposing aura of the newcomers were nothing like those of the Imperial Guard they had seen so far. The various circus troupes who, like Jeok Cheongang’s group, had come to perform at the banquet—along with courtesans and musicians—swallowed nervously.

“The Embroidered Uniform Guard…”

There was no mistaking them.

They had been granted the right to wear gold, one of the Son of Heaven’s symbols. They were the Great Nation’s finest, and, alongside the East Depot, among its most powerful enforcers.

Unlike the Imperial Guard, who could be seen anywhere in the capital, the Embroidered Uniform Guard rarely appeared—and when they did, their authority was formidable.

As formidable as the man who now stepped forward, his eyes gleaming.

“I am Jeong Hogun, a Thousand Captain of the Embroidered Uniform Guard.”

His voice was calm, but a heavy aura pressed down in every direction.

Jeok Cheongang realized his intentions long before the aura hanging over the crowd reached them, and promptly sent a message by Sound Transmission.

—Everyone, be on your guard.

The inspection and sorting the fat official had mentioned were no ordinary, easygoing affair.

*He’s using the Embroidered Uniform Guard to weed out anyone who doesn’t belong. Possible assassins.*

Flies always swarmed around a well-laid feast.

It would be bad enough if they were only a nuisance. But flies carrying swords and spears, seeking the Emperor’s life, were another matter entirely.

Fortunately, this was exactly what Jeok Cheongang’s group and the East Depot had anticipated.

*I knew it.*

Know your enemy and know yourself, and you can fight a hundred battles without peril.

That was the old saying.

To prepare for a situation like this, the Divine Physician had personally made Energy-Dispersing Poison to disrupt their internal energy and had given it to everyone in the group. Jeok Cheongang, who had already reached the realm of Returning to Simplicity, could conceal his aura at will even without the poison.

*The only problem is that there’s just one Taishan…*

But contrary to that concern, Jeong Hogun’s gaze, which had briefly turned toward Taishan, soon moved away.

Or rather, it would be more accurate to say the trouble started somewhere else before he had a chance to examine Taishan closely.

“You there. Step forward.”

“M-Me, sir?”

The sparrow-moustached man who looked like the steward of a pleasure house asked in a trembling voice. Jeong Hogun shook his head.

“No. I mean the courtesan behind you.”

“W-Whatever could be the reason…”

“That girl knows better than I do. Isn’t that right?”

The courtesan, who looked barely twenty, had a pure, lovely face. She blinked in surprise, then threw herself face-first onto the ground.

“T-This girl has done nothing wrong!”

Jeong Hogun replied in a flat voice.

“I think so too.”

“Th-Then why…”

“But the scent of bitter poison is coming from the sachet at your waist.”

“……!”

“Will you explain yourself?”

The courtesan raised her head and stared up at Jeong Hogun in bewilderment.

Then, in the next instant, she yanked the hairpin from her head and swung it like a streak of light.

Whoosh! Thunk!

A faint whistle, then a spray of blood.

Jeong Hogun watched with a lowered gaze as the courtesan plunged the hairpin into her own neck.

“Why?”

“T-Twelve years ago. Grrk. My father and mother, my younger sibling… Cough.”

“Revenge. Yes, I suppose so.”

“I have to k-kill the Emperor…”

Thump.

The courtesan’s body, coughing up blood again and again, went limp and collapsed.

Jeong Hogun stared down at the corpse in silence for a while, then spoke abruptly.

“Remove the body, and take everyone who came with her to the prison.”

“Yes, sir!”

“W-Wait! We didn’t know anything about this! We really don’t know a thing…”

Clang-clang!

The cold sound of drawn blades drowned out their desperate excuses.

Realizing they had no choice, they disappeared somewhere under the Embroidered Uniform Guard’s escort, faces filled with despair.

Jeong Hogun watched them go, then turned to someone he’d put off questioning.

“You there.”

“Huh?”

“You said you belonged to a circus troupe.”

“Yeah.”

As Taishan looked around blankly, Jeok Cheongang lowered his head and thought. Should he wait and see a little longer, or step in himself?

And just as he cautiously curled his hand into a fist—

Someone’s voice from far away reached his ears.

“Hey, Hogun. What are you doing here?”

At that familiar voice, Jeok Cheongang reflexively lifted his head.

A young man was walking toward them with a wide grin.
## Chapter artifact 884

# Chapter 884

The moment I saw the situation spread out before me, I thought:

*I knew this would happen.*

Of course, I wasn’t some gifted shaman who’d been summoned here by a divine message. I hadn’t suddenly rushed over on a hunch, either.

The thought that I should probably go see for myself had come right after I heard the news from Hong Jin.

“People from Young Master Jin’s group entered the palace a little while ago. Disguised as a circus troupe. But…”

“Did something go wrong?”

“That’s right. I guess they attracted more attention than we expected. You know that huge guy in the group?”

“Ah, shit. I told them not to do that.”

“…I haven’t even said anything yet.”

“What’s the point of hearing it? Given the way they usually act, I can guess. This won’t do. I’m going out for a bit.”

“Wait. Eunuch Ma must have taken some measures. Let’s wait a little longer.”

“I know my companions better than anyone. Even if it’s just to be safe, I should go see for myself.”

“Captain, you’re absolutely right. I’ll escort you and bring you back in no time, so Comrade Hong can relax.”

“Mujin.”

“Yes, Captain.”

“Don’t go picking a fight. Stay here.”

“……”

“That bastard’s going to go start another mess.”

I’d left the pavilion without a moment’s hesitation half an hour ago.

For some reason, ever since I’d met the Emperor two days earlier, the Embroidered Uniform Guard surrounding the pavilion had only watched from a distance and hadn’t tried to stop me. The place Hong Jin had told me about was much closer than I’d expected.

The downside was that I had to take a long detour so I wouldn’t look suspicious, but fortunately, I made it just in time.

Right now.

“Oh, Hogun. What are you doing here?”

At my casual greeting, the tension in the air—which had been pulled taut as a bowstring—eased.

Then eyes came pouring down on me.

Among them were a few faces that looked both unfamiliar and familiar.

*I don’t know if those are human-skin masks or what, but they did a hell of a job with the disguise technique.*

People’s impressions could change completely with the smallest alteration to their features.

I naturally pretended to sweep my gaze over the crowd and spotted my companions huddled together in one corner. Then I waved to Jeong Hogun.

“There’s an old saying that you can’t spit in the face of someone who’s smiling, but looking at you, Hogun, I guess that’s not always true. When someone talks to you, could you at least answer?”

Jeong Hogun’s face remained still as he spoke.

“Who are you calling ‘our Hogun’?”

“Fine, then. Your Hogun.”

“As always, it’s impossible to have a sensible conversation with you.”

“What’s the point of a bunch of smelly, black balls understanding each other? Are you interested in me, by any chance?”

“Not at all. But I am curious why you suddenly appeared here.”

That was the Embroidered Uniform Guard for you.

His tone was blunt, but the meaning behind it was sharp as a needle. Still, I hadn’t spent all my time stumbling around Murim training only my martial skills.

And the half-hour I’d just wasted had been more than enough to think through how to avoid the enemy’s suspicions—and how to respond if I drew them anyway.

“What the hell do you mean, ‘why’? I was bored, so I was taking a walk around the area. The mood seemed strange, so I came to see what was going on.”

I pointed to the blood splattered across the ground—blood that had to have flowed from someone—and continued.

“I had a feeling I’d find something, and look at that.”

“……”

“On the way here, I saw about fifteen people being dragged off in a line. Did they commit treason or something?”

Jeong Hogun stared at me for a long while without answering, then abruptly spoke.

“They were trying to attend the banquet disguised as courtesans.”

It was no lie that I’d seen people being dragged off on my way here.

I suddenly remembered a corpse that one of the Embroidered Uniform Guard had been hauling away, rolled up in a straw mat.

The courtesan Jeong Hogun had just mentioned was probably that corpse.

*I wonder why she did it.*

I had no way of knowing.

She could have been a survivor of a family destroyed by the Emperor, or an assassin sent by someone who fancied themselves a champion of loyalty and righteousness.

There were plenty of possibilities. The problem was that this incident had put Jeong Hogun even more on edge, and he might start suspecting our allies.

*This can’t be how things go from the start.*

I spoke as naturally as I could, with the same hint of contempt in my eyes and voice I’d used until now.

“You brought down a traitor who dared raise a blade against His Majesty the Emperor. You’re definitely getting promoted this time, Thousand Captain Jeong.”

“I didn’t kill her. She took her own life.”

“It’s basically the same thing. Why do you think she killed herself? Because being dragged off and tortured to death would’ve been worse. She’d failed anyway, so dying cleanly was a hundred, a thousand times better. You know that too, don’t you?”

Jeong Hogun was silent for a moment, then answered in an even voice.

“Yes. You’re right.”

What?

He’d always been like that, but there was something strange about how little my sharp words seemed to affect him. I wondered to myself,

*Has he noticed something?*

He seemed sharper than the other members of the Embroidered Uniform Guard. It wasn’t impossible. If so, I couldn’t let things continue like this.

I walked forward with a broad smile.

“It’s nice to see you admit I’m right for once. How about I lend you a hand while I’m here?”

“You want to help?”

“It’s easy enough. Who knows? If I catch a traitor even the Embroidered Uniform Guard couldn’t weed out, maybe His Majesty the Emperor will grant me a wish.”

“What are you up to?”

“There you go again. Hey, that’s a professional habit. You’re so bad, even the Divine Physician couldn’t cure you.”

It was a good thing everyone’s attention was on me right now.

I pretended not to notice the Divine Physician flinching on reflex among the crowd, then shrugged at Jeong Hogun.

“Anyway, if you don’t want me to, just say so. If you’re fine with it, I’ll take a quick look around. I know a thing or two about that sort of thing—more than you do, anyway. You know that.”

I wasn’t just saying that.

Jeong Hogun was far better at surveillance and interrogation, but when it came to simply judging someone’s martial skill, I was definitely a step ahead of him. I’d crossed the threshold of Supreme Peak, after all.

No—if I could use Qi Sense, which I couldn’t right now, to get precise information, I’d be the perfect person for the Embroidered Uniform Guard.

Of course, my offer probably sounded a little strange to everyone else.

—Is this guy out of his mind…?

—What are you plotting?

Two messages reached me one after the other through Sound Transmission.

The first had come from Jeok Cheongang. The second was from Jeong Hogun.

I gave a quiet laugh and replied the same way, looking only at Jeong Hogun, who was staring at me as if he didn’t want to miss a single opening.

—Why are you sending a message through Sound Transmission? It’s not that big a deal.

—Answer me properly. Why are you doing this?

—Why? Isn’t it obvious?

I stared straight at Jeong Hogun and moved my lips.

—What if some lunatic starts swinging a sword at the banquet? And what if that stern Emperor you love so much gets hurt? Who do you think’s going to take the blame for it all?

—……!

—This isn’t for the sake of the master you serve. I’m doing this to protect His Highness Prince Shangshan. You idiot.

It was the perfect explanation. Anyone who heard it would think it made complete sense.

I’d come up with the alternative in a hurry on the way here, but it had worked.

I saw the muscles in Jeong Hogun’s stiff face relax, just a little.

*Success.*

But it wasn’t over yet.

I swallowed the sigh of relief that was about to escape me, clicked my tongue, and turned away.

With one last message to drive the point home.

—Well, there doesn’t seem to be anyone particularly suspicious right now, but do your job properly from here on out. Both of us. We each have someone to protect, don’t we?

That was it.

I walked back the way I’d come, at an easy pace, crossing through the now-quiet crowd. I didn’t forget to pause and react when I reached Taishan, whose face had changed but whose massive build hadn’t.

“Whoa, damn. Look at the size of you. What on earth do you eat to get that big?”

Taishan answered haltingly.

“I like five-spice pork.”

“Liar.”

“…Huh?”

“You look like you’d eat anything.”

“Oh. Uh-huh. I like it.”

“Your muscles and bones are completely ridiculous. You’ve trained in external arts, haven’t you?”

“Geosan. Sold to circus troupe when young. Had to learn to survive.”

A circus troupe was a kind of traveling show that wandered the land performing for people.

You could find one in just about any sizable city, so it wasn’t strange for performers who put their bodies through the wringer to learn external arts.

*The strange part is how naturally huge he is.*

I thought to myself, then ran my hands over Taishan’s arms and legs, which were packed with muscle.

“With a build like this, you could beat most First Rate masters with your bare fists… Where are you from?”

Namho, an old man with dark skin standing beside us, promptly bowed and answered.

“We’re based north of the Yangtze, sir. We mostly perform in Hebei and Liaoning.”

“Oh, that’s close. If you’re interested, stop by the Jin Family of Taiyuan in Shanxi Province sometime. He may have missed his chance, but if he has enough internal energy to back it up, he could still become a great martial artist.”

“We’re grateful for the offer, but we’d rather not. As you can see, he’s not as bright as other people, but he’s the treasure of our circus troupe…”

He certainly had a talent for improvisation, probably thanks to his Hidden Shadow Pavilion background.

Namho was showing the kind of acting that could kick one of Chungmuro’s rising stars in the shins. After exchanging a few more words with him, I left with an exaggeratedly disappointed look.

Feeling certain inside.

*Good.*

Anyone who’d heard that conversation would now know that the enormous man had trained in external arts to the point where he could take down a First Rate master, that his circus troupe operated north of the Yangtze, far from the imperial capital, and that there was little reason to suspect them.

And, most importantly, the potbellied official was an ally I hadn’t even known about.

“If there’s nothing else to investigate, let them through. They’ve already been thoroughly vetted several times, and I have a mountain of things to take care of.”

Hong Jin’s words came to mind at the same time.

“Wait. Eunuch Ma must have taken some measures. Let’s wait a little longer.”

Those words hadn’t been a lie.

Rather than mobilize the East Depot and draw attention, Ma Sanbao must have planted allies where no one would notice them.

*And fortunately, my appearance seems to have fit right in with that.*

After I’d walked several dozen yards, I heard Jeong Hogun’s blunt voice with my keen hearing.

“Let them through.”

I cheered inwardly, then fell momentarily speechless at the Sound Transmission that came flying in from Jeok Cheongang.

—As expected, you had everything planned out. This old man believed in you all along.

—……

No, Old Master.

A moment ago, you called me crazy.

# Checkpoint Review — 935–939

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

# Chapters 935–939

## Plot

Baek Yeon visits the Emperor, who has prepared for his death by entrusting Zhu Bao with his loyal retainers and power. He tells Baek that Taekyung promised to save him, a promise that has given him hope despite the Divine Physician’s grim prognosis: the Emperor may not survive another two months. Taekyung’s Myriad-Poison Ring fails against the Blood Soul Gu, which reacts violently to its energy. The System gives Taekyung a quest to remove the gu from the Emperor’s head and successfully treat him. Taekyung confides in Mujin, but has no solution yet.

Hong Jin brings Taekyung the Eastern Heaven Demon Lord’s hidden iron chest, which he had kept unopened as promised. Among its contents, Taekyung finds a paper titled “Shanxi Annihilation Plan.” It warns that Dark Heaven’s main force will cross the northern grasslands and invade Shanxi before the Double Ninth Festival, about half a month away. Taekyung considers the warning highly credible, though its sender and accuracy are unconfirmed. The scene shifts to Temur and Chinggen, ruling together over a prosperous grassland. Chinggen worries about missing scouts and disturbances in the west, but Temur dismisses the danger; a cold, dust-laden wind blows open their ger entrance.

Jeok Cheongang and the Bow Saint discuss her decision to put Taekyung at risk during the recent banquet-hall battle. She says the test was necessary to confirm he was the chosen one and understand his power and character, for the sake of far more lives. She also says the Martial God chose her. Jeok is furious, but falters when she names the 2,562 allies killed in the battle and says acting sooner could have saved at least half. Messenger eagles sent across the night sky signal that the Great Nation’s imperial court is responding to urgent news.

## Continuity

- The Emperor’s Blood Soul Gu has reached his marrow. The Divine Physician says his vitality is at its limit and cannot guarantee he will survive another couple of months.
- Taekyung’s System quest requires him to remove the Blood Soul Gu from the Emperor’s head and successfully treat him. Its reward and failure consequence are unknown. The Myriad-Poison Ring failed against the gu; it thrashed more violently when it sensed the ring’s energy.
- The Emperor has transferred his loyal retainers and power base to Zhu Bao in preparation for his death, and avoids meeting his younger brother to spare him the grief of an impending farewell.
- Taekyung found and opened the Eastern Heaven Demon Lord’s hidden iron chest. It contained about a dozen decaying bamboo slips, recent papers, and a small silk pouch; the significance of the slips and pouch is unknown.
- A paper among the chest’s contents warns that Dark Heaven’s main force will cross the northern grasslands and invade Shanxi before the Double Ninth Festival, about half a month away. Its sender is unknown, and the warning has not been confirmed.
- The Bow Saint says the Martial God chose her. She deliberately tested Taekyung in the banquet-hall battle to confirm he was the chosen one and assess his power and character.
- The Bow Saint counts casualties after every battle and remembers the dead. She cites 1,319 orthodox fighters killed at Mount Small Hua more than fifty years ago and 2,562 allies killed at the banquet hall; she says acting sooner could have saved at least half of the latter.
- Jeok Cheongang is furious that the Bow Saint endangered Taekyung, whom he considers his one and only Disciple.
- Temur and Chinggen rule the grassland together. Chinggen is concerned about missing scouts and disturbances in the western grasslands; Temur dismisses the danger.

## Translation Decisions

- Render the iron chest’s System item name as “Very Sturdy Iron Chest.”
- Render 산서멸계 as “Shanxi Annihilation Plan.”
- Keep established terms including Blood Soul Gu, Myriad-Poison Ring, and Double Ninth Festival.

## Durable state

{
  "active_continuity": [
    "The Emperor was poisoned with Blood Soul Gu after the coup; it has reached his marrow, and the Divine Physician says his vitality is at its limit and cannot guarantee he will survive another couple of months.",
    "Taekyung’s System quest requires him to remove the Blood Soul Gu from the Emperor’s head and successfully treat him; its reward and failure consequence are unknown.",
    "The Emperor prepared for his death by transferring loyal retainers and his power base to Zhu Bao, and avoids meeting his younger brother to spare him the grief of an impending farewell.",
    "The Emperor has publicly exposed Dark Heaven and declared his intent to crush it; war against Dark Heaven has begun.",
    "Ma Sanbao escaped and evaded the Imperial Army’s three-day search.",
    "Taekyung found and opened the Eastern Heaven Demon Lord’s hidden iron chest; it contains old bamboo slips, recent papers, and a small silk pouch of unknown significance.",
    "The System update reward is a durable pocket watch that appears broken and bears the faint inscription “A broken clock is right twice a day.”",
    "The Bow Saint says the Martial God chose her; she tested Taekyung in the banquet-hall battle to confirm he was the chosen one and assess his power and character.",
    "The Bow Saint remembers the dead and counts casualties after every battle; she says 1,319 orthodox fighters died at Mount Small Hua and 2,562 allies died in the banquet hall.",
    "Jeok Cheongang considers Taekyung his one and only Disciple and is furious that the Bow Saint put him in danger.",
    "A missive found among the Eastern Heaven Demon Lord’s belongings warns that Dark Heaven’s main force will cross the northern grasslands and invade Shanxi before the Double Ninth Festival, about half a month away; the sender is unknown and the warning is not yet confirmed."
  ],
  "continuity_sources": [
    938,
    939
  ],
  "open_questions": [
    "What is the Martial God’s identity, and what is the full nature of his connection to the chosen one and the Bow Saint?",
    "How far has Dark Heaven infiltrated the Great Nation, and which officials or commanders are involved?",
    "Where is Ma Sanbao, and what is his current status?",
    "Who sent the Shanxi Annihilation Plan missive, and will Dark Heaven’s invasion proceed as described?",
    "What do the papers, bamboo slips, and silk pouch from the Eastern Heaven Demon Lord’s chest contain, and what is their significance?"
  ],
  "safe_through": 939,
  "temporary_decisions": [
    "Taekyung intends to keep the pocket watch for half a month before deciding whether to give it to Mujin."
  ],
  "version": 1
}

## Reading copies

## Chapter artifact 935

# Chapter 935

“I heard Jin Taekyung came by.”

The Emperor, alone in his vast bedchamber and lost in thought, wasn’t startled by the man’s sudden voice.

He was one of the very few—perhaps the only one—who could come and go freely in Qianqing Palace, inside or out, without asking permission.

“You’re a step too late, Baek Yeon. He left half a shichen ago.”

“That doesn’t matter. I came only to see Your Majesty.”

At Commander Baek Yeon’s calm reply, the Emperor affected a frown.

“I’d rather decline. I’ve already seen your face more than enough.”

“Then have you been at peace these past three days?”

“What kind of question is that? It’s been a relief not having a nag around.”

“I’m hurt.”

“Don’t sulk too much. Someone who used to keep an eye on me around the clock is in much the same position as you.”

“If No Shadow heard that, he’d be even more hurt than I am.”

“That’s why I’m saying it while he’s not here. He’s no longer my bodyguard, so I can indulge in the occasional bit of gossip behind his back.”

“Well. I can’t win against Your Majesty.”

Baek Yeon shook his head as if conceding, and the Emperor let out a quiet laugh.

“So, is Bao’er doing well?”

“Of course. He couldn’t be doing better.”

Yet even Baek Yeon’s answer couldn’t banish the worry from the Emperor’s face.

“He’s still young, and he’s been through something like this. He must be unsettled, body and mind alike. You all need to stay by his side.”

There was concern in his voice.

Baek Yeon understood how the Emperor felt.

His own flesh and blood had returned after more than a decade.

Though it had been for his safety, the youngest brother he’d all but abandoned deserved all the love and worry he could give him.

That was why he had assigned No Shadow, his hidden bodyguard, and Baek Yeon, his closest confidant, directly to the Crown Prince.



*“Look after him. I can trust him to you.”*



Remembering the Emperor’s request—not an order—from three days ago, Baek Yeon spoke.

“Though His Highness hasn’t even turned fifteen, he has the second strongest and most upright spirit of anyone I’ve ever met. It’s hard to believe he’s so young.”

“Second?”

“First is Your Majesty.”

At Baek Yeon’s immediate answer, the Emperor couldn’t find a response for a moment. Then he raised both hands.

“I’ll concede this one. You’re flattering me when you never used to. You’ve changed a lot, Baek Yeon.”

“That’s true. Much like how Your Majesty has started making jokes.”

“Come now. I already said I conceded. Enough with the nonsense.”

“Do the words I just spoke sound like empty flattery or nonsense to you?”

Baek Yeon continued with a faint smile.

“I meant every word. I’ve always admired and respected Your Majesty. You kept walking down a brutal, thorn-covered road that others would have given up on time and time again, your feet covered in blood.”

Faced with the sincerity in his words, the Emperor fell silent.

Something surged up inside him and caught in his throat. He didn’t think he could say anything just then.

All he could do was fight down the rising emotion and force his voice out.

“If I’d had to walk that road alone, I would have given up along the way. I couldn’t have done it without you all.”

“I don’t believe that.”

Baek Yeon shook his head and continued slowly.

“It was because it was Your Majesty, and no one else, that we were able to trust and follow you. It’s because you alone bore the greatest responsibility and pain that a day like this is even possible.”

“……!”

“Even while watching out for rebels with blades hidden up their sleeves, did you ever neglect the affairs of state? The Your Majesty I saw always cut back on sleep to practice martial arts, handle memorials, and fight your illness all at once.”

A jumble of emotions crossed the Emperor’s face.

Yes. That was how it had been.

There had been such days—days when it could be no other way.

“It was only natural. Sleep was a luxury.”

For more than ten years, he had never slept for more than one shichen in a day.

No—even then, he had never slept peacefully.

He had to keep his mind alert, even as he felt his body slowly dying.

That was what it meant to be the Son of Heaven.

The highest person under heaven had to face the fiercest storms before anyone else, while looking down on and caring for everything spread out beneath him.

That was where the Emperor believed he stood. And that was why Baek Yeon could do nothing but respect him from the bottom of his heart.

“Making a decision is as easy as turning your hand over, but showing that decision through your actions is as hard as moving a mountain.”

At first, Baek Yeon hadn’t been certain, either.

Whether the Great Nation’s fourth prince, their last remaining choice, was someone with whom they could pursue their great undertaking.

Whether he was fit to ascend to the Son of Heaven’s all-powerful position.

But he had done it.

Better than anyone.

Though the Imperial treasury was piled high with mountains of gold and silver, he had always lived frugally. Though peerlessly beautiful women had been presented before him, he had never indulged in women. He had even chosen not to produce an heir, for fear of putting his youngest brother in danger.

That way, Dark Heaven wouldn’t be able to harm Zhu Bao.

They couldn’t recklessly kill a child with the legitimacy and right to replace the Emperor, or inject him with Blood Soul Gu, which would quickly kill its host.

“Everything Your Majesty took for granted was something that could never have been taken for granted.”

“……!”

At the quiet ring of Baek Yeon’s voice, the Emperor’s eyelids trembled.

He hadn’t known.

He hadn’t known Baek Yeon thought of him that way.

Looking back over the road he’d traveled, the Emperor realized he wasn’t the only one who had kept his true feelings hidden. Baek Yeon had, too.

“I…… don’t know what I should say.”

At the Emperor’s choked voice, Baek Yeon burst into hearty laughter.

“You don’t have to say anything.”

“Wouldn’t it be better to say something, though?”

“I’m not sure. I think it would only make things more awkward.”

The Emperor shook his head and clicked his tongue.

“Baek Yeon, are you really the same person I’ve always known?”

“What on earth do you mean?”

“Do you really have to ask? You’ve always been merciless.”

“Are you talking about when you were learning martial arts?”

“I am. You said, ‘Please forgive me for laying hands on Your Majesty’s precious body,’ then proceeded to beat me all over.”

“Why are you bringing that up all of a sudden?”

Baek Yeon frowned at the unexpected reminder of the past.

“And as I told you back then, the way to improve at martial arts is to get hit. So Gyo…… I mean, the Bow Saint agreed with me, didn’t she?”

“Yes, she did. The two of you even teamed up to beat me later. It hurt so much I spent ages wondering if I should quit right then and there.”

“Did I threaten you with a sword? You were the one who asked me to teach you.”

“Your manner of speaking now is just the same. Whenever I struggled, you’d come by without fail and lay into me, and you’d push me around using the familiar *hao* form of address, as if you’d forgotten every bit of etiquette due to the Son of Heaven.”

“That was……”

Baek Yeon trailed off and glanced away at the empty air.

During martial arts training, he could excuse laying hands on the Emperor’s person as instruction. But this was different.

Even if it had been to encourage the Emperor, Baek Yeon himself had to admit that some of his words and actions had been entirely unbecoming of a loyal subject.

“Your Majesty……”

“Don’t pretend you don’t remember. You were like that until just recently. It wasn’t even a few days after Bao’er entered the palace that you came to see me and gave me a thorough tongue-lashing.”

“You were taking poppy with the great undertaking right in front of us. I was worried it would destroy you, body and mind.”

“What does that have to do with using the familiar form of address? I’d been bedridden and suffering for days, and had only just recovered some strength. I had to take poppy to ease the pain, even a little.”

“I know. I did know, but I was worried about you, Your Majesty.”

Baek Yeon’s eyes darted around as he kept talking to the empty air. Then he suddenly fell silent.

At the edge of his vision, he caught sight of the Emperor’s smiling face.

“……I see.”

“Do you concede defeat?”

Realizing that the Emperor had been teasing him the whole time, Baek Yeon sighed.

“I do.”

“Then you’ve won once, and I’ve won twice.”

“Are you keeping score now?”

“I used to be a general, just like you. What matters more to a general than victory or defeat?”

At the sight of the Emperor laughing with evident delight, Baek Yeon couldn’t help joining in with a hearty laugh.

What else mattered?

If the Emperor was happy, that was enough.

What mattered was that the Emperor’s face, still shadowed by the approaching specter of death just three days earlier, now shone as brightly as a full moon.

And yet…… a part of him felt bitter.

The Emperor looked as though he had already accepted, deep in his heart, the death that was waiting for him.

All Baek Yeon could do was look at him and laugh along.

*I know why you sent No Shadow and me to serve His Highness.*

It wasn’t only because the Emperor feared something might happen and wanted to protect his one and only younger brother and heir.

The Emperor was preparing for what would come after his death.

Before it was too late, he was handing over his loyal retainers and his power base to Crown Prince Zhu Bao.

All while not showing his face even once to the younger brother he cherished and loved so dearly these past three days.

*You don’t want him to see you like this.*

For the two brothers who had reunited after more than a decade, the death drawing near wouldn’t be a parting that only the Emperor had to face.

Zhu Bao.

The Great Nation’s new heir would have to endure a parting, too.

He would have to say goodbye to the only blood relative he had, now that he had finally come to know the affection and sincerity of family.

The Emperor must have known that, too.

Even though he had to tell his younger brother to prepare for their parting, he was afraid to face him in his grief and so refused to meet.

*……I see.*

Baek Yeon forced the corners of his mouth back up.

Then, to keep from spoiling the brief joy the Emperor was feeling at that moment, he opened his mouth in as bright a voice as he could manage.

“By the way, something good must have happened today. Did Jin Taekyung bring you some amusing news?”

“Amusing news? There was some.”

“I’d like to hear it, too.”

“It was nothing special.”

And the next words the Emperor added with a smile caused the smile on Baek Yeon’s lips to vanish completely.

“He said he’d save me. No matter what it took.”

“……!”

“It was amusing. He doesn’t know the first thing about medicine, yet he made such a bold promise. But Baek Yeon, do you know what’s even more amusing?”

Without waiting for an answer, the Emperor continued.

“Those few absurd words made me feel hopeful.”

It was strange.

How could Taekyung make such a bold claim, with such certainty on his face and such a gleam in his eyes?

And the Emperor had found the sight of Jin Taekyung like that rather delightful. He was grateful to him, too.

His own life was something he had already given up on, yet that irreverent martial artist was determined to bring him back to life somehow.

But separate from that, the Emperor was fully aware of reality.

*It’s probably impossible.*

How cruel was hope to someone standing before a death that had already been foretold?

He had folded away that brief surge of hope and put it somewhere deep in his heart. For now, he simply wanted to speak to the loyal subject before him with a much lighter heart.

“You look troubled. I’m fine, so don’t worry about me.”

“But if this were to get out……”

The Emperor smiled and waved a hand at Baek Yeon’s worried expression.

“I’ve already made a promise with him that he won’t tell anyone else. Jin Taekyung is a man I can trust.”

* * *

“So……”

Jeok Cheongang spoke in a heavy voice after hearing me out.

“The Emperor’s been poisoned with the Blood Soul Gu?”

I nodded without hesitation.

“Yes.”

A promise is there to be broken.
## Chapter artifact 936

# Chapter 936

Jeok Cheongang’s reaction to the truly grave news that the Emperor had been poisoned with Blood Soul Gu was short and to the point.

“That must hurt.”

“……?”

“What? Am I wrong?”

“Well, no, but it’s not just a matter of being in pain.”

Anyone listening would think the Emperor had a cold instead of Blood Soul Gu.

At my baffled expression, Jeok Cheongang shrugged.

“Same difference. He’s in so much pain he’s on the verge of dying, isn’t he? Bad enough that even that tight-lipped quack can’t cure him.”

At Jeok Cheongang’s sudden jab, the Divine Physician—who’d worn a troubled expression the whole time I’d been talking—spoke up.

“I was told not to tell anyone until you spoke of it yourself, so I simply respected the patient’s wishes. And why am I a quack?”

“If a physician can’t cure an illness, he’s a quack. Take that Divine Physician name tag off today.”

“I never put one on. It wasn’t mine to begin with.”

“Since we’re on the subject, let me ask you something. What if……”

“I know what you’re thinking, but even if my Master came, it wouldn’t change anything.”

It was something I’d wanted to ask, too. But the Divine Physician’s answer came a beat ahead of me, calm and firm.

“Blood Soul Gu…… is in a class of its own, unlike any of the many deadly poisons known to us. It’s almost as if it was created for the sole purpose of killing its host.”

Jeok Cheongang let out a low groan.

“So you’re saying there’s no antidote?”

“Poison and medicine are two sides of the same coin, so there must be a way to treat it. The problem is time.”

He was right. The Emperor was dying even now.

The fact that he’d looked especially exhausted and drained after the battle in the grand banquet hall three days ago hadn’t been my imagination.

“From what I’ve seen, his vitality is already at its limit. I can’t even guarantee he’ll last another couple of months.”

For the Divine Physician to say that much meant the poison had advanced beyond anything even elixirs or internal energy could hold back.

Like a jar full of holes that wouldn’t fill no matter how much water you poured into it, the Emperor’s life force was draining away fast.

*At this rate, he’ll die before long. If the Emperor dies suddenly, the Great Nation will be thrown into chaos.*

Personal feelings aside, the Emperor couldn’t die.

He’d borne every kind of humiliation and ruled the Great Nation for over ten years without any serious disturbance.

And the fact that he’d held on to the throne despite facing a powerful opposition led by the Eastern Heaven Demon Lord proved what an exceptional ruler he was.

*I have to save him. If only for what’s coming.*

I’d heard the Imperial Capital was already simmering like a cauldron over hot coals.

Two days before I woke up, the Emperor had carried out another large-scale purge, then posted hundreds of proclamations across the capital.

Those huge sheets of paper, stamped clearly with the Imperial Seal, laid out the whole truth in detail.

They also carried the Emperor’s declaration that he would crush the vile traitors known as Dark Heaven.

*The war is about to begin.*

No—it had already begun.

The Emperor’s resolve was clear, and the people’s anger toward Dark Heaven was spreading like wildfire.

To them, Dark Heaven was nothing more than a foreign enemy threatening their homes and their lives. No one wanted war, but they had to fight to protect the peace.

And this war needed a leader to guide them all.

A powerful leader—cool-headed and meticulous, with the authority to make bold decisions when the time came.

Someone with experience on many battlefields would be ideal.

“What do you intend to do, Young Master Jin?”

I answered the Divine Physician, who’d spoken with a grave expression, as calmly as I could.

“We have to save him somehow.”

“But there is no way to do that. As I said, we don’t have enough time.”

“That’s all right. The method I’m going to try probably won’t take long.”

“The fact that you speak so confidently…… suggests you have some plan I don’t know about.”

“Right. I do. A brilliant plan.”

At my confident reply, Jeok Cheongang, who’d been listening to our conversation in silence, suddenly widened his eyes.

“Wait. The plan you’re talking about wouldn’t happen to be……”

“You’re thinking of the right thing.”

“I’d forgotten all about it. Yes, that precious treasure changes everything.”

Jeok Cheongang tapped his forehead. Only then did the Divine Physician blink in apparent surprise.

“Don’t tell me you have the Myriad-Poison Ring in mind?”

“Of course. What else?”

“Huh……”

At the Divine Physician’s low sigh, I gave a short laugh and continued.

“Even against Blood Soul Gu, the Myriad-Poison Ring gives us a good chance. No—it can definitely cure him.”

The Myriad-Poison Ring had effortlessly absorbed even the Formless Ultimate Poison, which had once threatened Jeok Cheongang.

The Divine Physician had treated Jeok Cheongang alongside the Slaughter Saint back then. He knew better than anyone what the ring could do, so I found it strange that he hadn’t thought of it until now.

“I guess you’ve had a lot on your mind, given the circumstances. I understand. It happens.”

“Y-Young Master Jin.”

“It’s fine. As you know, I left it with Prince Shangshan—or rather, the Crown Prince. I’ll go get it right away. It’ll only take a moment, so you can start preparing the treatment in the meantime.”

“Young Master Jin?”

“Oh, come on. Anyone can forget something now and then. Why are you making such a big deal of it? I’ll be off, then.”

I turned with a friendly smile.

Or, more precisely, I was about to turn—until I noticed the object in the Divine Physician’s hand.

“……?”

Wait a second. What’s that?

I stared at the very familiar-looking ring in silence, then broke it.

“That’s strange. It looks a lot like something I know.”

The Divine Physician replied with a flat stare.

“It would have to. It is the same thing.”

“I guess they make great knockoffs on this continent. Where’d you buy it?”

“I didn’t buy it.”

“Oh, someone gave it to you as a gift?”

“It wasn’t a gift, either. I borrowed it for a while.”

“From whom?”

“I told His Highness the Crown Prince the general situation and borrowed it from him. I said I’d come on your behalf because it was needed for something important. He handed it over without asking for details.”

My vision swam.

I drew a breath and managed to speak.

“Th-this important matter wouldn’t happen to be……”

“What else could it be? I’ve been to Qianqing Palace twice today.”

“I didn’t hear anything about that from His Majesty……”

“Was there any need to tell you?”

“Then the result was……?”

“Just as I told you earlier.”

Silence fell once again.

Heavier and more suffocating than before.

No one dared to speak out of turn. Then Jeok Cheongang’s low voice rang out.

“Quite a plan. It was so brilliant it plugged up your nose, too.”

“……”

“……”

Yeah.

What now?


* * *


> **System**
> 
> **Quest**
> 
> **Dr. Choi Taekyung**
> 
> You made a profound impression on the Emperor, who suffers from illness, by promising to treat him.
> 
> But for someone standing at death’s door, nothing is crueler than giving them hope too soon.
> 
> A man’s word is worth a thousand gold. Keep your promise.
> 
> Remove the Blood Soul Gu lodged in the Emperor’s head and free him from the pain that has tormented him for so many years.
> 
> If you fail to treat the Emperor……
> 
> **Grade:** Supreme Peak
> 
> **Restriction:** Jin Taekyung
> 
> **Mission:** Successful treatment (Incomplete)
> 
> **Reward:** ???
> 
> **Failure:** ???

I stared at the air in silence, then quietly closed the holographic window.

There was only one thought filling my head.

*I’m screwed.*

Really screwed.

Who could’ve guessed even the Myriad-Poison Ring wouldn’t work?

No matter how much I pressed him, unwilling to accept reality, the Divine Physician gave me the same answer every time.

*“It failed.”*

*“Huh? But it looked like it was going to work.”*

*“No. It failed.”*

*“So it almost worked, but missed by a hair?”*

*“That’s not what I mean. It failed completely. It just doesn’t work. In fact, the Blood Soul Gu sensed the Myriad-Poison Ring’s energy, felt threatened, and started thrashing around even more. I still break into a cold sweat whenever I think about it.”*

*“Liar. Playing such a nasty prank on me. You little rascal.”*

*“……Young Master Jin. Would you care to speak with me over there for a moment?”*


I’d noticed something glinting inside the Divine Physician’s sleeve. It turned out to be a huge needle that looked like it could pierce an elephant’s foot.

A chill ran down my spine, and I fled back to my quarters. That had been barely fifteen minutes ago.

*Damn it.*

What nerve had I had to promise the Emperor he’d make a full recovery?

I’d said it because I trusted the Myriad-Poison Ring, that overpowered item. It had dealt with the Formless Ultimate Poison without any trouble. Surely it could kill one lousy bug.

And yet.

“I’m screwed.”

Yeah. Screwed.

And not just a little.

Forget the quest—the Emperor’s death had to be prevented. But with my last hope, the Myriad-Poison Ring, gone, my vision had gone yellow.

“What the hell…… am I supposed to do now?”

I stared blankly at the ceiling I’d grown accustomed to, muttering to myself. Then Hyuk Mujin—who seemed to have claimed one corner of the room as his own—came over and patted my shoulder, as if this were only natural.

“It’s all right, Captain. Everything’s all right.”

“Mujin.”

“Yes?”

“Do you even know what the hell you’re talking about?”

“I do.”

Hyuk Mujin nodded confidently and continued.

“You got dumped by Young Lady Zhu, didn’t you?”

“……”

“Ah. Guess not. I’m sorry for overstepping.”

At least when it came to apologizing, he was a Supreme Peak master.

The guy bowed at the speed of light. Then he looked wistfully at the pocket watch hanging from my neck and asked,

“But seriously, what happened?”

“Mujin. When you’re talking to someone, you should look them in the eye. Not at their watch.”

“It was so radiant, I couldn’t help myself.”

I desperately wanted to whack him on the back of the head, but I didn’t have the energy for it right now.

I let out a long sigh and explained the situation in broad strokes, taking care not to reveal that the Emperor was the person at the center of the story.

“So someone with a serious illness had another person promise to treat them.”

“Yeah.”

“But after making all those grand claims, that person had no plan or method at all.”

Every word hit hard.

I flinched from the blow and cautiously added,

“That’s right, but it’s more accurate to say there was a plan and then it disappeared.”

“Either way, that still means there’s no way to treat them, right?”

“Right.”

“Hmm. Got it. I see what’s going on.”

Hyuk Mujin nodded and announced in a stern voice,

“What a total piece of shit.”

“……!”

“Don’t you think so too, Captain? How could someone give a person who’d finally made peace with death that kind of hope? When they haven’t got a single thing figured out. Whoever the hell that bastard is……”

Seeing me tremble, Hyuk Mujin continued in a much quieter voice.

“I think he’s a very handsome and dignified young man who always gives others hope and does the right thing.”

“……”

“……”

“……You done?”

“……Want me to keep going?”

“……No.”

Don’t make me feel any worse, you bastard.

I gave him a silent word with sad eyes, then lowered my head, unable to look Hyuk Mujin in the face.

Tap-tap-tap.

Fast approaching footsteps came with an opening door, and a familiar face appeared.

“I heard it was important, so I took care of it as quickly as I could…… Oh my, why’s the mood so grim?”

It was Hong Jin.
## Chapter artifact 937

# Chapter 937

“I heard it was important, so I took care of it as quickly as I could…… Oh my, why’s the mood so grim?”

The moment Hong Jin entered the room, he sensed the strange tension and asked about it. I answered with a troubled expression.

“It’s nothing.”

“Nothing? It sure looks like something happened.”

Hong Jin glanced between Hyuk Mujin and me, then murmured, his expression suddenly growing serious.

“Oh, that’s what it is? Hmm. But there’s nothing you can do about that.”

“……?”

“It’s all right, so don’t take it too hard. These things happen sometimes. It’s part of life.”

What was he talking about? Could Hong Jin know, too?

Thinking it over, he was now the East Depot eunuch, so it was entirely possible he knew about the Emperor’s illness.

*Maybe he’d heard something about it while enthusiastically torturing rebels for the last three days.*

Having reached a reasonable conclusion, I cautiously asked, “You already knew?”

Hong Jin hesitated for a moment, then nodded.

“Yeah. I happened to hear.”

“It’s supposed to be top secret…… More people know than I expected.”

“Eyes and ears are everywhere. No matter how tightly you try to wrap something up and keep it hidden, it’s bound to leak out eventually.”

Fair enough. The Emperor keeping quiet couldn’t protect every secret.

Every incident had victims and perpetrators, and perpetrators had mouths, too.

The rebels who were already dead—or waiting for death.

Some of those who’d passed through Hong Jin’s and the Embroidered Uniform Guard’s hands must have been close aides to the Eastern Heaven Demon Lord, and known the Emperor had been poisoned with Blood Soul Gu.

“You must’ve found out while interrogating the prisoners. Which ones knew?”

“What?”

“The prisoners who knew about it. They must have been closely connected to the Eastern Heaven Demon Lord.”

“Uh, well……”

Maybe that was a sensitive thing to bring up.

I realized my mistake too late and was about to wave my hands to take it back when Hong Jin, who’d been blinking quietly, continued.

“I heard it from Young Hero Taishan.”

“Ah. I see…… Wait. Who?”

“Young Hero Taishan. That huge guy.”

“……?”

No, something wasn’t right here.

Hyuk Mujin spoke up in my place.

“You mean the Taishan I know?”

“Yeah.”

“Built like a mountain, just like his name?”

“That’s right.”

“Usually an idiot, but smart whenever food comes up?”

“I don’t know about that part.”

“Obsessed with five-spice pork?”

“That part’s definitely true. Actually, some intelligence came in yesterday. According to my men, the imperial cooks tried to poison his food.”

If he was the number one target for assassination among the imperial cooks, then it had to be the Taishan I knew.

I asked, utterly confused, “How would he know that?”

“How would he know? He saw it.”

“That can’t be right. He wouldn’t have seen it.”

“He said he saw it clearly.”

“……What are you even talking about?”

“……That’s what I’d like to ask you. What’s all this about prisoners and interrogations?”

Hong Jin frowned at me, then went on.

“Weren’t you talking about ‘that thing’ that happened right after Young Master Jin woke up?”

“W-what?”

“You look really unsettled. Is that why? I told you it’s fine, so why are you still worrying? You just have a little more energy than other people.”

“……!”

Oh, shit.

My vision went dark in an instant, and my whole body trembled.

“How…… how did you know?”

“It’s all over the palace. Didn’t you know?”

“It’s all over……?”

“I’m one of the last to hear, since I was away for a while. Less than two shichen after you woke up, half the people in the Inner Palace probably knew.”

I couldn’t breathe. My hands and feet shook, and I felt like I was about to cry.

It was like turning on the TV one day out of boredom and finding a national broadcast channel throwing a wet-dream party for me.

Twitching like I was sick, I barely managed to force the words out.

“Taishan. Bring that bastard here right now.”

Hyuk Mujin, who’d frozen with his mouth hanging open, answered.

“I’m really sorry to say this, but Taishan’s stronger than I am.”

“Bring him here, no matter what!”

“Come on, Captain. You know he tears people apart with both hands.”

“I can tear you apart with one.”

“Ah. Aah.”

Hyuk Mujin let out a brief yelp and dashed out. Feeling the air grow heavy, Hong Jin spoke with a troubled expression.

“Young Master Jin. Don’t take it so hard.”

For the moment, even my worries about treating the Blood Soul Gu had been completely driven from my mind.

I replied to Hong Jin’s attempt at comfort with a groan. “Don’t say that so casually when it’s someone else’s business.”

“I told you it’s fine.”

“What’s fine? Have you ever been in a situation like mine?”

At my sharp question, Hong Jin answered with a sad smile.

“Of course not. I had it cut off a long time ago.”

“……”

“Just look on the bright side. I’m actually jealous of you, Young Master Jin. Especially during the rainy season, it aches so much down there that sometimes I can barely walk without poppy……”

“Okay, I get it. I get it, so please stop.”

Using his eunuch trump card—one he pulled out whenever he was bored—to shut me up, Hong Jin held out something he’d been carrying and continued.

“I was going to do that anyway. I’m a busy man, too. I only came to hand over the item I was asked to deliver.”

Realizing how badly my question had backfired snapped me to my senses. Only then did I notice the small iron chest in Hong Jin’s hand and remember why he’d come back.

The mysterious place the Eastern Heaven Demon Lord had told me about in his final moments.

The item he’d said to find there.

“This is……”

“It’s an iron chest, as you can see. I don’t know what’s inside or who left it there, though.”

“You didn’t open it?”

“Obviously not. That’s what I promised you.”

Hong Jin shrugged and added with a smile, “Besides, I wasn’t confident I could open it myself.”

He’d said it as if it were a joke, but the moment I took the chest from him, I realized it wasn’t entirely one.

*Ding.*

> **System**
>
> Very Sturdy Iron Chest acquired.
>
> New Item acquired. Would you like to appraise the Item and view its information?

I gave a slight nod, and a translucent holographic window opened between Hong Jin and me.

> **System**
>
> **Item Window**
>
> **Very Sturdy Iron Chest**
>
> **Grade:** Peak  
> **Restriction:** None  
> **Description:** An iron chest made by mixing in a small amount of Ten-Thousand-Year Cold Iron. As you’d expect, it’s incredibly durable—perfect for use as a shield or for storing precious belongings.
>
> However, it has no fewer than five locks, so using it often may be a bit of a hassle.

After quickly reading through the text, I swallowed a dry laugh.

*Seriously? Even if it’s only a little, why use Ten-Thousand-Year Cold Iron in an iron chest……?*

Ten-Thousand-Year Cold Iron was incredibly rare—and filthy expensive to match.

If a renowned smith used even four nyang of it to forge a weapon, people would call it a fine sword. Use any more than that, and masters with foul tempers and a knack for spitting would descend on it like starving demons.

In short, it wasn’t something you could easily get just because you had money. And no matter how rich you were, any sane person would use it to forge a weapon.

And there weren’t many crazy people rich enough to mix Ten-Thousand-Year Cold Iron into an iron chest that was nothing more than a storage box.

Of course……

*I can think of someone right away.*

I gave a bitter smile and ran my hand over the iron chest.

As if to prove it had been buried deep underground, its surface was damp, and patches of soil that hadn’t been brushed off gave off a strong earthy smell.

*What could it be? What did you want to hide away so badly?*

I was thinking of the chest’s former owner, the Eastern Heaven Demon Lord, when Hong Jin rose to his feet with a wink.

“I’ll get going. There’s no point sticking around and getting in your way.”

He didn’t wait for my answer before leaving the room.

Before closing the door, he remembered to pass along one more message.

“Oh, His Highness the Emperor’s Brother and Heir asked me to tell you this.”

“What is it……?”

“He misses his one and only friend. He can’t come see you right now because of the circumstances, but he wants to make sure he sees you before he leaves.”

His one and only friend.

Remembering what he’d said when he gave me the Myriad-Poison Ring at Qianqing Palace, I couldn’t help letting out a quiet laugh.

“Tell him I feel the same way.”

Hong Jin answered with a slight smile of his own, then left. Once I’d confirmed that all signs of life around me had disappeared, I set the iron chest on the floor and abruptly held out my hand.

*Inventory open. Summon.*

*Ding.*

Along with the brief command I recited in my mind, the familiar, cold feel of metal wrapped around my hand.

White Flame.

My personal weapon, and a divine weapon forged by the world’s greatest smith after a year of hardship.

And, at the same time, the key—of the physical sort—that could open that tightly locked iron chest and its five padlocks.

“Let’s see what you were so determined to keep hidden.”

I murmured, then brought the spearhead down without hesitation.

*Slice.*

A flash of light, and the metal split apart.

With no loss of form at all, I cleanly cut through all five padlocks in a single stroke and looked inside the chest.

*This is…….*

I’d known from the moment I first picked up the iron chest, but its contents were as spare as its weight was light.

A dozen or so bamboo slips, so old they were practically rotting away.

Along with them, a bundle of papers that looked relatively recent, still white and clean, and a small silk pouch.

*What is this?*

For some reason, the moment I saw them, an inexplicable shiver ran down my spine.

These were the Eastern Heaven Demon Lord’s—or, to put it another way, his keepsakes.

They had to be worth more than gold and more dangerous than gunpowder, in ways that couldn’t be measured by their weight or shape alone.

And it didn’t take long for me to realize my instinct was right.

No—it took only moments.

*Rustle.*

The moment I untied the string around the bundle of papers on top, still pristine white, a bolt of lightning shot through the crown of my head.

“……!”

My entire body went rigid before I knew it.

As I read the lines of text filling the page with trembling eyes, Hyuk Mujin’s voice reached my ears. I didn’t know when he’d come back.

“Um, Captain. I don’t think I can bring him……”

His voice rang out like an echo, as if coming from far away.

Suppressing the surge of emotion, I spoke.

“……Go get them.”

“What?”

“Bring everyone here. Now!”

“……!”

Sensing that something was wrong, Hyuk Mujin’s face went stiff.
## Chapter artifact 938

# Chapter 938

“Has it been about fifty years?”

Jeok Cheongang murmured as he looked out over the garden, filled with flowers and rare plants of every color.

“Back then, Mount Li in Shaanxi looked just like this. It was the height of spring, and all kinds of plants were in full bloom.”

It wasn’t simply an old man talking to himself as he reminisced.

He was also speaking to someone sitting with their back against a moss-covered wall.

“Mount Small Hua.”

“Hmm?”

“It was Mount Small Hua, not Mount Li.”

Her voice was calm and clear.

Jeok Cheongang shook his head at the Bow Saint’s correction.

“That can’t be right. I remember soaking in steaming hot spring water. Mount Li has been famous for its hot springs since ancient times.”

“It wasn’t a hot spring. It was a small pond—until someone heated it with Scorching Yang Qi, claiming he couldn’t stand cold water.”

“Was it?”

“You seem to have completely forgotten how the Thunderbolt Saber King went berserk and nearly started a fight.”

“That Peng bastard?”

The Bow Saint nodded. Jeok Cheongang furrowed his brow.

“I don’t remember it, but he’s been an idiot then and now. Making a fuss because someone warmed up a little water.”

“He had every reason to. The Thunderbolt Saber King was already in the pond.”

“He was so big I must’ve mistaken him for a bear.”

At Jeok Cheongang’s shameless reply, the Bow Saint let out a small sigh.

“You haven’t changed.”

“People aren’t so different from those flowers. They’re battered by wind and rain, day and night, and die when their surroundings suddenly change. To live even one day longer, you have to stay the same—like this old man.”

“So, did you come to tell me the secret to a long life?”

“Does this old man look like he has that much free time?”

“You showed up out of nowhere and brought up old stories I’d rather not remember. You don’t look that busy, either.”

Jeok Cheongang wore a bitter smile at the dry voice reaching his ear.

This time, he couldn’t help agreeing with the Bow Saint.

No matter how he looked at it, those weren’t happy memories.

It was a spring day more than fifty years ago, though he couldn’t remember exactly when. They hadn’t gathered there simply to laugh and talk.

“Three thousand members of the death squad climbed the mountain together. Before even a day had passed, half of them had been buried there.”

And Mount Small Hua, green beneath the bright spring sky, became a mountain of fire, dyed entirely red.

He could still see it clearly.

Flames surging up the mountainside.

Blood mingling with the stream water, and countless bodies scattered in every direction.

The Zhongnan Sect. The Huashan Sect. The Hebei Peng Family.

Alongside them were the smaller orthodox factions, whose names had not been etched in people’s memories for nearly as long.

Among them was the Blade of Flowers, Jin Baekyang, then the Second Young Master of the Jin Family of Taiyuan.

The three thousand elite members of the death squad surged like a wave toward ten thousand Demonic Cult followers led by five great fiends—and fell, spraying blood instead of white foam.

At dawn, as they stood atop a mountain of Demonic Cult corpses and roared their victory, two kings and one star stood at their center.

“One thousand three hundred and nineteen.”

“……!”

“That’s how many people died that day.”

A quiet voice suddenly rang through the night air.

Jeok Cheongang paused, then slowly turned around.

“You remembered? Every one of them?”

Though his body had grown young again, the years in his eyes remained unchanged.

In Jeok Cheongang’s seasoned eyes was reflected a woman whose gaze resembled his own.

“I never forgot. Not for a moment.”

“……I didn’t know you were like this.”

“Knowing doesn’t change anything. Just as remembering them is all I can do.”

The Bow Saint fell silent for a moment, then added,

“That was simply the kind of time it was.”

Jeok Cheongang nodded faintly and muttered, “Yes. It was.”

The Demonic Cult’s momentum had been terrifying back then.

No—it had been overwhelming.

The hundred thousand of the Demonic Path swept in like a wave, crushing the Kunlun Sect as they crossed Qinghai. Then they split into three forces and advanced without resistance.

Toward Sichuan. Toward Gansu. And through Shaanxi toward the very heart of the continent, the land known as the Central Plains.

It was a massive wave that not even the Nine Sects and One Gang and the Five Great Families could stop. The orthodox factions, unable to unite and each guarding its own territory, crumbled in an instant.

The Demonic Cult’s long-coveted dream of ruling the world through the Demonic Path was no longer some far-fetched fantasy.

Not until one man appeared.

“Do you know what I was thinking the day I came down from Mount Jiuhua, having killed every last one of those bastards who dared set it ablaze?”

Jeok Cheongang continued without waiting for the Bow Saint to answer.

“I swore deep in my heart that I’d kill as many Demonic Cult followers as I could until the very last moment of my life.”

With the tide of war already turned against them, facing the Demonic Cult alone was madness.

Madness that no one but Jeok Cheongang, the Fire King, could pull off.

“But there was someone even crazier than this old man.”

Jeok Cheongang laughed heartily.

He was remembering how he’d been about to charge straight at the Demonic Cult forces occupying Anhui after driving even the Nangong Family from their territory.

“I just couldn’t believe it. Three thousand Demonic Cult followers defeated by one man.”

Those three thousand weren’t a ragtag bunch who’d only just advanced beyond Third Rate.

They were elites forged through the Demonic Cult’s brutal training, fanatics who’d sworn absolute loyalty to the Heavenly Demon.

And among them were two great fiends who’d reached the Supreme Peak realm.

“Of course, I had no choice but to believe it eventually.”

The story was too incredible to accept, so he’d caught several Demonic Cult followers as they fled and interrogated them. He confirmed that their two leading great fiends and nearly half their forces had vanished.

At the hands of someone whose identity was unknown.

“In that moment, I suddenly remembered something my late Master used to say. The world is vast and there are many masters, so you must keep striving.”

But it hadn’t taken long for him to learn the truth.

It wasn’t that Jeok Cheongang was lacking. That unknown man was simply exceptional.

No—compared to him, anyone would seem ordinary.

“The Martial God.”

No one knew his origin, his name, or his age.

Even his face was scarcely known.

He could freely use every kind of martial art, and the disguise technique was no exception.

And yet everyone believed in and followed the Martial God.

That was the kind of person he was.

He was the only lamp illuminating a world steeped in darkness, the sun shining alone above the heavens.

And that was precisely why they could never approach him on instinct. They could only circle around him.

They feared that the wind from a cautious outstretched hand might snuff out their only light.

They worried that if they took just one more step, the sun’s fierce heat might burn them alive.

“So the Martial God’s identity remained a mystery to the very end. No—no one could even dare imagine it. Not even the Thousand-Faced Fox, who served him more closely than anyone.”

But now he knew.

The secret of the Martial God that had never been revealed to the world.

And at last, Jeok Cheongang understood.

How he could have been called the Martial God.

“Was it divine strength? That incomprehensible power.”

At Jeok Cheongang’s muttering, which sounded almost like he was talking to himself, the Bow Saint slowly rose to her feet.

“Why? Planning to spread rumors about it?”

“This old man’s only just started acting like a proper person again in his old age. I can’t have people thinking I’ve lost my mind.”

Jeok Cheongang let out a quiet laugh.

“So you kept talking even though you knew full well I was listening. Just because I’m that brat’s Master?”

“I just didn’t see any reason to hide it.”

The Bow Saint looked at Jeok Cheongang and continued.

“I already saw it on the battlefield. A Master and Disciple willing to throw away their lives for each other.”

“……!”

“That’s when I understood how much trust there was between you two. So there was no point hiding the truth.”

There was nothing hidden, so there were no secrets.

The Bow Saint had seen the bond between Master and Disciple clearly. And as the unbelievable story unfolded, she sensed Jeok Cheongang’s qi remain steady while he silently watched, confirming what she had understood.

“When did you know your Disciple was special?”

Jeok Cheongang answered in a calm voice.

“From the beginning to now. Always.”

“I think there’s been a slight misunderstanding. I meant, when did you learn the truth about that boy……?”

“Does that matter?”

Jeok Cheongang cut her off and looked at the Bow Saint.

Her reflection appeared in his eyes, which had grown dark and solemn.

“Nothing changes. From the day I took that brat as my Disciple, we’ve shared everything and faced it all together.”

The Bow Saint’s brow drew together.

Not because she hadn’t gotten the answer she wanted, but because she felt the air around them slowly heating up.

*Rumble.*

The wind stopped. The air trembled.

And at the center of it all stood Jeok Cheongang, the Fire King.

“Still……”

The head that had been turned toward the garden slowly swung around.

His eyes glowed red, flickering in the darkness like ghost fires.

“Did you put my Disciple in danger just to make that trivial confirmation?”

Jeok Cheongang had not forgotten the rage and despair that had seized him when Jin Taekyung collapsed, spraying blood.

Even if his Disciple had grown strong enough to stand shoulder to shoulder with Elders of great sects—or perhaps even their Sect Leaders.

Even if he were no longer a young man acting on the rashness of his peers, but someone with the stature to call himself a Sect Patriarch.

Jin Taekyung was his one and only Disciple.

*Whoosh!*

White hellfire surged upward in a spiraling column.

Through the heat haze rising from its terrible warmth, the Bow Saint spoke calmly.

“Two thousand five hundred and sixty-two.”

Jeok Cheongang’s steps toward her came to an abrupt halt.

He thought he knew what that incomprehensible answer meant.

“That’s how many of our people died in the grand banquet hall three days ago.”

“You know the number well. But……”

A cold voice, unlike the energy he wielded, slipped between Jeok Cheongang’s lips.

“If someone had acted first, not even half of them would have died.”

“Yes. That’s surely true.”

“What!”

*Whoosh.*

The flames rising from Jeok Cheongang grew hotter, but the Bow Saint continued steadily.

“Even so, I had to see it with my own eyes. Whether that boy truly was the chosen one. What kind of power he had—and what kind of heart.”

“How dare you……!”

“After every battle, I counted the dead. It was my way of remembering them.”

“Will you shut your mouth!”

“But if ten times as many people died as they did three days ago—one hundred times as many…… No, more than a thousand times—would you still be able to be this angry?”

“……!”

“To you, it may have been a trivial confirmation that put your precious Disciple in danger. But it wasn’t trivial to me.”

The Bow Saint looked at Jeok Cheongang’s trembling eyes and spoke.

“It was a decision I made for far more people than that. Perhaps even for everyone in this world.”

“That was also why that person—the Martial God—chose me.”

Her quiet murmur spread through the cold night air.

*Step.*

From far away in the darkness came the faint sound of someone approaching.

At the same moment, both of them turned. Hyuk Mujin was running toward them with all his might.
## Chapter artifact 939

# Chapter 939

*That guy……*

Recognizing a familiar face rapidly approaching from beyond the deep darkness, Jeok Cheongang gathered in the aura that had been surging through his entire body.

Was it because the unexpected, unwelcome visitor was Hyuk Mujin?

No.

It was because he sensed something was wrong in the way Mujin looked—so unlike himself.

*Huff, huff.*

His legs wouldn’t stop moving, and his breathing was ragged.

Who knew how far he’d run? Sweat glistened on his face, which was taut with urgency.

*……Something must have happened.*

Hoping the ominous feeling creeping over him at that very moment was a mistake, Jeok Cheongang called out to Hyuk Mujin, who had briefly lost his way in the darkness and hesitated.

“What are you dawdling for?”

“Ah. Great Hero Jeok!”

Hyuk Mujin came rushing over, then stopped short when he spotted the Bow Saint.

“Th-this junior of Murim, Hyuk Mujin……”

With a light gesture, the Bow Saint stopped him from continuing and spoke.

“Save the formalities. Tell us why you’re here.”

“It’s…… Captain. I mean, my lord ordered me to bring the two of you to him at once.”

“The two of us?”

“Yes. I searched everywhere, but couldn’t find either of you. When I asked my lord, he told me where you were……”

The Bow Saint’s brow furrowed.

But it wasn’t because a junior so far below her—Jin Taekyung, who was practically still a child—had dared to summon her as if he could order her around.

“He said he’d explain the details in person. Everyone else is already gathered.”

At Mujin’s words, the Bow Saint clicked her tongue softly.

“Something more serious than I thought must have happened. Serious enough that he sent for not just you, but me as well.”

Jeok Cheongang nodded, his face grave.

He knew Jin Taekyung. The brat could be reckless, but he was meticulous about observing the proper courtesies—at least within certain bounds.

And if he’d even sent a subordinate to summon the Bow Saint, an outsider as far as he was concerned, it was hard to guess just how serious the matter was.

—Unfortunately, I think we’ll have to end our conversation here.

The Bow Saint’s Sound Transmission slipped quietly into his ear.

Jeok Cheongang regarded her impassive face with a heavy gaze. He didn’t detect a trace of regret in it.

—So it seems. For tonight.

His reply promised they’d continue their conversation another time.

There were still things Jeok Cheongang hadn’t said, and questions he hadn’t dared to ask. He had no intention of leaving things as they were.

—I hope our next conversation will be more meaningful than this one.

Even at Jeok Cheongang’s pointed words, the Bow Saint remained composed.

—It will be. There will be plenty of chances, even if not the next time we meet.

—What does that……

Jeok Cheongang faltered at the many possible meanings in her answer. He was just about to continue when—

*Flap, flap.*

The sound of powerful wings suddenly rang overhead.

*That’s……*

Jeok Cheongang looked up and saw it clearly.

So did the Bow Saint, who turned her gaze at the same time, and Hyuk Mujin, who reflexively followed their eyes.

*Whoosh!*

Dozens of birds flew across the distant sky, black against the darkened heavens.

The sight of the creatures in flight moving in separate formations, each heading in a different direction as if thoroughly trained, was reflected in their eyes.

“Messenger eagles……!”

Jeok Cheongang murmured the words like a groan, and felt his heart grow heavy.

Sending out so many precious messenger eagles—not ordinary messenger pigeons—meant the Great Nation’s imperial court was on the move.

Probably because of the news his Disciple had delivered.

*What could have happened?*

At least one thing was certain.

There was no time left to hesitate.

“Lead the way. Hurry.”

It was a night far too deep for dawn to be near.

And now, an invisible unrest was sweeping through the Imperial Palace.

* * *

“What happened?”

Those were Jeok Cheongang’s first words as he burst in like the wind. Instead of answering, I held out what I had in my hand.

*Swish.*

Jeok Cheongang’s eyes sank as he examined the several sheets of paper, slick with oil.

“A missive?”

A veteran martial artist whose experience was second to none in the world, he had immediately recognized the papers. He took the stack from me and skimmed through it quickly.

Before even a few moments had passed, he looked up.

His face had gone as hard as stone.

“Is everything written here…… true?”

If it had been half an hour ago, I might not even have heard Jeok Cheongang’s voice.

I’d been too distracted to think straight.

But now I’d explained the situation to the Fire Dragon Pavilion members and passed along a general outline to Hong Jin and Qianqing Palace. I managed to answer calmly, though the answer itself was still hazy as mist.

“I don’t know.”

“What do you mean!”

“To be precise, none of it has been confirmed yet. But……”

I looked in turn at Jeok Cheongang, rigid with tension; the Bow Saint, who had just begun reading the missive; and the Fire Dragon Pavilion members gathered inside the hall.

“It’s highly credible information.”

“On what grounds?”

This time, it was the Bow Saint. She set down the missive, her gaze more grave than ever.

“No, before that—who sent it?”

“I don’t know that, either. All I know is that it came from someone in a fairly high position in Dark Heaven.”

“How could someone like that send it to you……”

The Bow Saint let her words trail off and gave a low, thoughtful murmur.

“They weren’t sending it to you in the first place.”

Exactly.

Whoever had sent this missive must have written it intending to pass the information to someone other than me.

“Could it be?”

Jeok Cheongang murmured under his breath. I nodded.

“That’s right. It was among the things the Eastern Heaven Demon Lord had kept.”

“……!”

“……!”

Jeok Cheongang and the Bow Saint’s eyes widened.

The Fire Dragon Pavilion members, who had heard the general outline before the two of them arrived, couldn’t hide their agitation, either.

Anyone who had seen even a single line of those missives would have reacted the same way.

The four or five sheets of paper, still slick with oil, held information that could determine the fate of tens of thousands of lives. Maybe even hundreds of thousands.

And one of those sheets was lying at my feet right now.

*Tap.*

I picked up a sheet of paper with trembling fingertips.

Four characters leaped into my eyes at once.

*Shanxi Annihilation Plan.*

At some point in the past, someone had written this missive to the Eastern Heaven Demon Lord. The message was clear: before the Double Ninth Festival, Dark Heaven’s main force would cross the vast northern grasslands and invade Shanxi Province.

*Crack.*

I clenched my teeth. Swallowing the groan that threatened to escape, I closed my eyes.

If—if this information was true……

*Just half a month.*

That was how long remained until the Double Ninth Festival.

The time left to Shanxi Province.

No—the time left to the Jin Family of Taiyuan.

* * *

Peace and turmoil went hand in hand.

Even in times of peace, disturbances great and small broke out somewhere in the world. And even amid the chaos of war, there were people who enjoyed peace.

That had been true after the long, fierce age of rival warlords, when the Great Nation rose to power and achieved the unification of the world.

It had been true until now, was true in the present, and would remain true in the future.

And if you had to name the place in this vast world where turmoil broke out most constantly, it was none other than the northern grasslands.

A place filled with grass, earth, and horses.

By day, birds soared through the blue sky. By night, wild beasts huddled in the darkness and wandered in search of corpses.

Before the age of rival warlords, the descendants of a nomadic people who had once conquered a vast territory and claimed the title of rulers of the world had lived there.

They still lived there now, in gers made of cloth and grass rather than splendid palaces or towering walls, alongside the horses they’d been as inseparable from as their own bodies since they first learned to walk.

And yet, the shining glory of the great past their ancestors had built was slowly fading from their memories.

“Hmm. Not bad. No—excellent.”

The man murmured with satisfaction, taking another sip from his cup.

Like any other nomad, he had shaved the crown of his head clean and braided his hair into a long queue down his back. But his imposing build and the golden crown on his forehead made him stand out more than anyone.

Or he would have, if not for the other man seated beside him in the place of honor.

“Temur, my brother. Have you forgotten that too much of anything can become poison?”

He had deep-set eyes and a lean build. As he looked at the hulking Temur beside him and clicked his tongue softly, the golden crown on his own forehead gleamed. Two horses were engraved upon it.

“You’re right, Chinggen. You always have been.”

Temur nodded at Chinggen, who looked displeased, then grinned, baring yellow teeth.

“But remember one thing. Alcohol is medicine in and of itself. It can never be poison.”

“Oh, Temur.”

“Come on, don’t be like that on a fine day. Why don’t we raise a cup together, hmm?”

Temur jabbed the head-shaking Chinggen in the waist, then raised his cup high and called out:

“What do you say, proud brothers of the grasslands!”

“Waaah!”

Hundreds of warriors gathered inside the vast ger cheered in response, and Temur roared with laughter.

“That’s more like it!”

He was genuinely happy in that moment.

Only two years ago, Temur had led a tribe with fewer people than the number of warriors now gathered inside this ger.

But look at him now.

He wore a crown of gold and drank his fill of fine liquor imported from the distant Central Plains, instead of mare’s-milk wine made by milking and boiling horses alongside his followers.

All while hearing the cheers pouring down on him.

“Long live Khan Temur! Long live Khan Chinggen!”

“May you live to a ripe old age!”

Khan.

Ruler of the vast grasslands, king of tens of thousands of horses and warriors.

What a wonderful title to hear.

Once only a dream, it now belonged to him.

The two brothers, who had shared life and death together since childhood, had brought peace and prosperity to the endlessly turbulent grasslands—and at last earned the title of Khan.

“Can you hear them? Hm? I said, are you listening?”

Temur, who had been mingling with his warriors, filled Chinggen’s empty cup.

The silver cup imported from the Central Plains—not carved from wood or animal bone—shone brilliantly, reflecting the faces of the two men.

Temur’s was grinning from ear to ear; Chinggen’s was plainly uncomfortable.

“Of course I can hear them. But now isn’t the time to laugh and drink, Temur.”

“Good grief, there you go again. Since when does laughing and drinking need a special occasion?”

“My brother, didn’t I send a messenger with news?”

“Ah, that? I heard.”

Temur chewed noisily on a piece of meat as he continued.

“But don’t worry too much. We may be Khans now, but the grasslands are vast. We can’t do anything about what happens beyond our reach.”

Of course, Temur knew about it, too.

Scouts had occasionally gone missing, and there had been a few disturbances in the westernmost reaches of the grasslands.

But to Temur, it was nothing much.

Not enough to make him forget the indulgence of the moment.

“Come on, my ever-worried brother. Let’s empty our cups first, then talk.”

Temur laughed heartily and was about to offer Chinggen another drink when—

*Flap.*

A cold wind carrying sandy dust pushed open the entrance to the ger.

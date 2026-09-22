# Checkpoint Review — 650–654

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

# Chapters 650–654

## Plot

Jin secretly meets Heugung at the Outer Palace West Gate after receiving a missive. Heugung alleges that Baeksang has colluded with Dark Heaven, citing decades of surveillance, a destroyed secret refuge, unexplained missive exchanges, and Baeksang’s monthly disappearances. He offers to testify at the next Tribal Grand Council if Jin and the Beast Miao King guarantee his and Yohi’s safety, while insisting that his love for Yohi is genuine despite believing her efforts to revive the Yao people are misguided.

That night, roughly thirty masked attackers assault the Fire Dragon Pavilion while Jin and several companions are absent. Sama Pyo kills twenty, including seven Peak masters, using his Black Dragon Saber, concealed weapons, mechanical devices, poison, and ruthless combat methods. Jin returns to defeat the remaining attackers, while Taishan kills two after Namho tells him they ate both chicken legs. The final attackers sever their own heart meridians; Jin briefly revives one with Scorching Yang Qi but learns that all three are Nanman infiltrators whose tongues were cut out long ago.

The assault leaves the pavilion and nearby patrols devastated. Jin concludes that Dark Heaven likely knew he possessed the Myriad-Poison Ring and arranged the infiltrators’ deaths to prevent interrogation. Baeksang, Yohi, and Heugung remain possible organizers. Yayul Mok then reports that Heugung and Yohi have disappeared from the Inner Palace.

## Continuity

- Jin remains in the Nanman Beast Palace’s Inner Palace as the Third Young Master of the Jin Family of Taiyuan and head of the Fire Dragon Pavilion.
- Heugung alleges that Baeksang colluded with Dark Heaven but has no conclusive proof. He claims Baeksang monitored him for over twenty years, exchanged unexplained missives between Insi and the hour of the Rabbit on the first day of each month, and disappeared alone monthly since last year.
- Heugung genuinely loves Yohi and had promised to cooperate with Jin before the attack.
- The Fire Dragon Pavilion was attacked less than half a shichen after Jin left; patrol warriors were also killed.
- The three surviving masked attackers were Nanman infiltrators with tongues severed long ago. They died by severing their own heart meridians, leaving the organizer unidentified.
- Jin suspects Dark Heaven orchestrated the assault to protect the Myriad-Poison Ring’s secrecy, but Baeksang, Yohi, and Heugung remain possible direct suspects.
- Heugung and Yohi have disappeared from the Inner Palace. Their location and involvement in the assault are unknown.
- Sama Pyo survived despite severe blood loss, and Taishan remains fiercely protective of him.
- The Beast Miao King has not yet heard Heugung’s accusations or decided whether to protect him and Yohi as witnesses.

## Translation Decisions

- Use **Outer Palace**, **Inner Palace**, **Tribal Grand Council**, **West Gate**, **Insi**, and **the hour of the Rabbit**.
- Use **Bone-Shrinking Technique**, **Black Dragon Saber**, **Scorching Yang Qi**, **Myriad-Poison Ring**, **Dark Heaven**, and **Blood Monk**.
- Use **sever one’s own heart meridian** for 심맥을 끊다 and **final rally** for 회광반조.
- Retain **Force**, **Finger Qi**, **heart meridian**, **moon saber**, and **Dark Heaven hound**.
- Use **Peak master**, **upper First Rate**, **short spear**, **mechanical device**, and **hidden weapon**.

## Durable state

{
  "active_continuity": [
    "Jin remains in the Nanman Beast Palace's Inner Palace as the Third Young Master of the Jin Family of Taiyuan and head of the Fire Dragon Pavilion.",
    "Heugung alleges that Baeksang colluded with Dark Heaven, has secretly evaded Baeksang's surveillance for more than twenty years, and used the Bone-Shrinking Technique to meet Jin.",
    "Heugung genuinely loves Yohi and had promised to cooperate with Jin before the assault on the Fire Dragon Pavilion.",
    "The Fire Dragon Pavilion was attacked at night less than half a shichen after Jin left, and patrol warriors were also killed.",
    "Three masked Peak masters attacked the pavilion; they were Nanman infiltrators with tongues severed long ago and died after severing their own heart meridians.",
    "Jin could not identify the attack's organizer because the surviving infiltrator could not speak before dying.",
    "Jin suspects Dark Heaven knew he possessed the Myriad-Poison Ring and arranged the attackers' self-destruction to prevent interrogation.",
    "Baeksang, Yohi, and Heugung remain possible suspects, while Dark Heaven appears to be the broader force behind the assault.",
    "Sama Pyo survived the attack, and Taishan remains fiercely protective of him.",
    "Heugung and Yohi have disappeared from the Inner Palace.",
    "Yayul Mok arrived after the attack and reported the dead patrol warriors and the disappearance of the two great chieftains."
  ],
  "continuity_sources": [
    654
  ],
  "open_questions": [
    "Who ordered the assault on the Fire Dragon Pavilion, and how was Dark Heaven involved?",
    "Where are Heugung and Yohi, and were they involved in the attack or taken by its organizers?",
    "Is Baeksang truly colluding with Dark Heaven, and what evidence can Heugung provide?",
    "Will the Beast Miao King accept Heugung as a witness and guarantee Heugung's and Yohi's safety?"
  ],
  "safe_through": 654,
  "temporary_decisions": [
    "Use Finger Qi for 지풍.",
    "Use heart meridian for 심맥.",
    "Use Dark Heaven hound for 암천의 주구.",
    "Use Force for 강기.",
    "Use moon saber for 월도."
  ],
  "version": 1
}

## Reading copies

## Chapter artifact 650

# Chapter 650

The banquet held in the Inner Palace alongside the Tribal Grand Council that day didn’t start winding down until around the Ox hour.

For me, that was a great relief.

Otherwise, I would have had to listen to the whispers and feel the stares coming from every direction all night.

“That Han Chinese fellow—wasn’t he up on top of a pavilion with his pants off?”

“What? What are you talking about?”

“My wife’s sibling’s kid is with the Inner Palace guard, you know. Apparently, the brief alert one shichen ago was because of that fellow.”

“Now that you mention it, I did hear a whistle… But if it was one shichen ago, wasn’t that when he disappeared to go take a leak?”

“Maybe he didn’t go take a leak. Maybe he wanted to show everyone something else. People have all kinds of tastes, you know. Could be a Central Plains custom.”

“Good heavens. I had no idea the Central Plains had such a barbaric custom.”

“Barbaric as it gets. But separate from that, he does seem pretty impressive.”

“What does?”

“You know. That thing.”

“Ah…”

“According to the kid, they nearly attacked him because they thought he was holding a weapon. Until they shone a torch on him, they thought it was a spear.”

“What? Even so, how could she mistake it for a spear? Is that even possible?”

“Now, now. Do you think the word ‘dragon’ was added to his sobriquet for no reason? A dragon is a dragon.”

“Whaaaaaaaaaat!”

> **System**
>
> - Rumors about you are spreading far and wide!
>
> - A considerable number of influential figures are reacting to the rumors!
>
> - Fame has increased slightly!
>
> - Fame has increased slightly!

“…”

Please stop. And why does my Fame keep rising?

*My fucking life…*

I did my best to ignore the whispers around me as I tipped back the last of my drink. Seeing me like that, the Beast Miao King laughed heartily and patted me on the shoulder.

“Don’t take it too much to heart. Things like that happen to a man every now and then.”

“No, when you put it that way, it sounds like I did it on purpose. It was really just an accident. I was in such a hurry to get out that I forgot to fasten my trousers…”

“Hm? What was there to hurry out for?”

“Ah, well…”

Damn it. That had slipped out by accident.

I still hadn’t told even the Beast Miao King about the missive sent by the unidentified figure.

After a brief silence, I spoke with the abandon of a man who had given up.

“Actually, I did do it on purpose.”

“Oh my.”

“I’ve been like that since I was young. I still do it from time to time.”

“Good grief.”

“It’s both a hobby and a special talent. You thought I only used one spear, didn’t you? I actually use two.”

“Whaaaaaat…”

If I died in Nanman, no matter how I died, the cause of death would definitely be humiliation.

But there was nothing I could do about it now. The fact that the other party had made secret contact in this manner also meant that I wasn’t supposed to tell anyone else.

*At the very least, it means no one in the Nanman Beast Palace can know.*

I certainly trusted the Beast Miao King, but there was no place where the words *trust* and *faith* were treated more cheaply than the Murim.

No one knew what might happen.

Another reason I had made this decision was that if the Beast Miao King found out, someone else might notice something was wrong.

For example…

*That man.*

My eyes met Baeksang’s as he stared this way with emotionless eyes. The longer I looked at him, the less I could understand what was going on behind those eyes.

He had spent the entire banquet sitting without lifting a finger to touch the food or alcohol. Now, after meeting my gaze, he smoothed his immaculate white robes, rose from his seat, and spoke.

“Palace Lord, it is already late. We should end the banquet here.”

“Hm. Let us do so.”

The Beast Miao King nodded without much hesitation.

Considering that the Tribal Grand Council would continue tomorrow, it was only natural.

Of course, since everyone present was a Peak master who practiced martial arts, none of them would suffer from a hangover. Even so, drinking in an atmosphere like this was bound to dull the mind.

Pop. Pop.

The Beast Miao King expelled the alcohol from his body through his fingertips. His face instantly returned to normal, and when he announced the end of the banquet, disappointed voices rose from every corner.

*It isn’t any of them, at least. If they’re disappointed that the banquet is ending when the promised time is almost here, they can’t be the ones involved.*

After quickly checking the faces of those who looked disappointed, I spoke to the Beast Miao King.

“Sir Yayul, I should probably head in as well.”

“Of course. But which pavilion are you planning to go to this time?”

“…”

Seriously?

Seeing my expression, the Beast Miao King slapped his knee and laughed. I sighed and left with Namho and the other unorthodox faction underlings.

By then, the night had deepened, and the time had entered Insi.[^1]

It was time to meet the owner of the missive.

* * *

“Are you sure you’ll be all right going alone? It could be a trap.”

On the way to the quarters assigned to the Fire Dragon Pavilion, I reassured Namho, who was looking at me with concern.

“I’ll be fine. And Elder Nam, you’d only be a burden if you came along anyway.”

“…”

“Did you actually plan to follow me?”

“I’ve lived a fairly long life, but I have no desire to die like a stray dog.”

“Then stay in the quarters. Along with the other two deadweights.”

Taishan, as usual, didn’t give it much thought. Sama Pyo, who was arguably the greatest young prodigy of the unorthodox faction, showed some displeasure at being treated like a deadweight, but he shut his mouth after hearing my next words.

“Ah. If you’re upset, reach Supreme Peak.”

“…”

“I can somehow survive, but you two can’t. Keep watch around the quarters until I return. And swing your swords at least one more time while you’re at it.”

We entered the quarters together as if nothing had happened. After waiting for fifteen minutes, I slipped out in secret and melted into the darkness.

*Around Insi. It said the West Gate, right?*

I had no idea whether the contents of the missive tied to the arrow were a trap or an attempt to make contact in order to share information.

There was nothing to do but go and find out.

Whoosh—whoosh!

I moved while evading the notice of the warriors on patrol. After some time, the cheers and assorted noises echoing in the distance began to grow closer.

Shiiiiing! Boom!

“Waaaaaaah!”

The banquet in the Inner Palace had already ended, but the night in the Outer Palace was still going strong. And it wouldn’t end tonight. The same would be true tomorrow and the day after.

The ordinary tribespeople—neither the chieftains attending the Tribal Grand Council nor the warriors standing guard—were completely immersed in the festival atmosphere.

*So that’s why he chose the Outer Palace. There will be more people here than at any other time of year.*

I murmured inwardly and naturally melted into the crowd.

The streets were packed with people wearing animal masks to match the festive mood, and no one suspected me as I wore the tiger mask I had used last time.

*If he said the West Gate… would it be over there?*

The Outer Palace was in the middle of a festival, but that didn’t mean the guards had let their vigilance slip.

Evading the eyes of the warriors stationed throughout the area, I reached the West Gate before long.

To be more precise, I reached somewhere around the West Gate, which was just as crowded with people as everywhere else.

*I came here exactly as the missive instructed, but…*

There were too many people around me. And since this was near the West Gate, there were plenty of warriors stationed nearby as well.

If I simply stood there like some Great General, I was bound to attract attention.

*What happens next?*

Just as I began looking around in puzzlement, someone called out to me.

“Hey, tiger-mask fellow. If you’ve got nothing better to do, come have a bowl of somyeon before you go.”

At the mention of the tiger mask, I turned my head and met the eyes of a middle-aged man sitting at a nearby food stall.

His eyes and features were ordinary, and his body was painfully thin. He gave me a crooked grin and lifted the bowl in front of him.

“I’m not usually the type to talk to strangers, but the broth here is incredible.”

“…Hm.”

I wasn’t sure the broth was the only incredible thing here.

For a moment so brief it could hardly be called an instant, I silently stared at the middle-aged man. Then I nodded, sat down beside him, and finally sent a thread of Sound Transmission to the unexpected contact before me.

—Funny, you’ve lost quite a bit of weight in such a short time. You seemed to be eating quite a lot at the banquet.

“…”

Pop!

His scrawny body flinched in agitation. I could feel him trembling.

I picked up the chopsticks he had dropped and continued the Sound Transmission.

—So, what brings a great chieftain of the Yi people here?

The Sound Transmission pierced his ear, and Heugung’s eyes widened.

* * *

Perhaps the shock of having his identity recognized so quickly had left Heugung stunned, but I was just as surprised.

*The person who sent the missive was him?*

Although we had met only a few times and not for very long, I had already formed my own assessment of Heugung.

A pathetic man who had fallen head over heels for Yohi’s beauty and would give her his liver and gallbladder. A spineless puppet who moved according to Baeksang’s will.

That was probably why I was even more surprised.

The Heugung I was seeing now, in both appearance and behavior, was completely different from the man I had known. Not even after scrubbing my eyes could I find the enormous belly that looked fit for a pilgrimage to a holy site.

*If not for the System, I would have been completely fooled.*

I clicked my tongue inwardly and placed the chopsticks back in Heugung’s hand, speaking naturally to keep the attention of those around us away.

“What’s with you dropping your chopsticks all of a sudden? Even if you’re feeling weak, that’s no excuse.”

Heugung came to his senses and hurriedly composed his expression.

“Ah, thank you.”

But only Heugung and I knew that, beneath that ordinary conversation, Sound Transmissions were passing between us without anyone else hearing them.

“Master, one bowl of somyeon, please.”

I placed my order and moved my lips.

—You sent the missive tied to the arrow, didn’t you?

When the hunched old owner didn’t move at all, Heugung slammed his fist against the stall.

“Master! One bowl of somyeon!”

Then he gave me a grin and said,

“You’ll have to understand. The owner here is over ninety, so his hearing isn’t very good.”

—…That’s right. By the way, I changed my appearance using the Bone-Shrinking Technique. How did you recognize me at a glance?

Ah. The Bone-Shrinking Technique.

One of my questions about Heugung’s sudden transformation had been answered.

According to what Jeok Cheongang had told me in the past, the Bone-Shrinking Technique was a martial art that allowed its user to stretch and shrink bone and flesh like rubber bands. But because the process of learning it was difficult and painful, almost no one in the Central Plains practiced it.

*Even so, it can’t be a common martial art in Nanman either.*

There were still many questions left unanswered. As I waited for the somyeon to arrive, I spoke aloud.

“I was craving some hot broth anyway. This worked out nicely.”

—Whether I recognized you isn’t important, so let’s move on. Why did you send that missive?

As Heugung made sure I had chopsticks, he answered.

“The broth really is to die for. The owner has been running this stall almost as long as he’s been alive.”

—I had information I absolutely needed to tell you.

“Oh, really? Then I suppose I have something to look forward to.”

—Was it meant to kill me or tell me something? I nearly ended up with an arrow through my head.

—I thought you’d dodge it. Even Great Chieftain Baeksang suffered a setback at your hands. How could you fail to dodge a single arrow?

“…”

I wondered if he even knew that was how I had become the Naked Divine Dragon.

I considered smacking Heugung over the head, but held back out of sheer generosity and asked,

—So, what is this information you absolutely had to tell me?

Heugung stared at the steaming bowl in front of him and moved his lips with difficulty.

—Great Chieftain Baeksang… has colluded with Dark Heaven.

“…”

Crack.

The chopsticks snapped uselessly in my clenched hand.

[^1]: Insi is the traditional time period from three to five in the morning.
## Chapter artifact 651

# Chapter 651

There are many things in this world that cannot be resolved with mere suspicion.

That was true both of the modern twenty-first century where I had lived my entire life and the Murim, which was practically a lawless land by comparison.

All the more so if the matter concerned someone occupying a position second only to one person and above ten thousand others in the vast land of Nanman.

But…

—Great Chieftain Baeksang has colluded with Dark Heaven.

“…”

That changed things.

I muttered inwardly and set down the chopsticks I had unconsciously snapped in half.

The old owner of the food stall saw what I had done and grumbled with an unhappy expression, but all my attention was focused on a single person: Heugung.

—Are you certain?

—I am. No, at least, I believe I am certain.

What?

I barely managed to stop myself from frowning.

—That sounds like you’re saying there’s no concrete evidence. In that case, this cannot be something you merely believe to be true. It has to be true.

—Ha, but…

Heugung swallowed hard before continuing his Sound Transmission.

—This is the best I can tell you. Great Chieftain Baeksang is a man with that many secrets. I may also be a great chieftain leading one of Nanman’s four great tribes, but… he never discusses anything important with me in depth.

It lasted only a brief moment, but I saw it clearly—the emotion that passed over Heugung’s face when he uttered those last words.

It was unmistakably humiliation.

Perhaps it had been piling up inside him for a very long time.

As I stared at him, my lips parted.

—Is that why?

—Why? What do you mean?

—Is your resentment toward Baeksang the reason you betrayed the person you followed, sent me a secret missive, and told me all of this?

—Betrayal? That’s…—

—If this isn’t betrayal, then I’m not Han Chinese—I’m a Nanman native. So don’t try to deny it.

As if I had hit the mark, Heugung bit his lip hard and gave a small nod.

—Yes. I won’t deny it. After my late father died in the Great Faction War, I grew up under Great Chieftain Baeksang’s shadow, from the time I was a little child with a runny nose until now. No, it would be more accurate to say that I was dragged around with an invisible collar around my neck. But that isn’t the only reason I decided to meet you.

—Then what is?

—I want to protect Nanman. I want to protect my people.

“…”

—The Great Chieftain Baeksang I remember was always coolheaded and exceptional. That is why he will never bend his will. He must believe that his own choices are correct. But if this continues… Nanman is finished.

I silently stared at Heugung.

I had no idea how much of this secret conversation, held at a tiny food stall on a crowded street, I should believe.

*Can I trust him?*

The object of my doubts wasn’t just the information. It also included Heugung himself, who had suddenly contacted me in secret.

No—in some ways, whether I could trust him was the most important thing of all. Only then could I trust the information he had yet to reveal in detail.

*Everything he’s shown me so far seemed sincere. But what if all of it was an act?*

The Murim was a fierce and unpredictable world, too volatile to foresee.

Heroes. Third Rate thugs. Fiends and hypocrites. Countless kinds of people mixed together, deceiving and being deceived, drawing hidden blades and stabbing one another in the back.

*In the Murim, nothing is impossible.*

Just as I was quietly weighing the situation, the old owner broke the silence.

Clack.

The effort seemed almost too much for him; broth spilled over the rim as he set the bowl down with a trembling hand.

The cheap somyeon, which cost no more than a few iron coins, was tangled chaotically inside the bowl.

Just like the thoughts in my head.

“It’s finally here. Try the broth first. That’s the real specialty.”

Heugung spoke in an artificially cheerful voice, but his eyes darted around anxiously as he quickly swept his gaze over the surroundings.

—Be careful. Great Chieftain Baeksang has many unseen eyes and ears. I need to return within half an hour at the latest if I’m to avoid suspicion.

—Did you slip away while you were with him?

—No. But there is always an observer nearby. A plant he placed there long ago to keep track of my movements. Today, at least, you needn’t worry.

He didn’t say who had planted that observer, but there was no point asking.

I already knew the answer.

*Baeksang.*

Nothing would have drawn more attention than staring blankly at a bowl of steaming somyeon.

I ate as naturally as possible while sending him a Sound Transmission.

—How long have you been watched?

—I don’t know the answer to that myself. I first noticed it around the time I came of age, and I’ve been wary of Great Chieftain Baeksang for more than twenty years since then. That is also why I secretly learned the Bone-Shrinking Technique. The process is difficult, but unlike other martial arts, it leaves almost no trace of training.

At this point, I had no choice but to revise my assessment of Heugung.

*Not bad.*

It was funny for me to make that judgment about a man well past forty, but the difference between this Heugung and the man who had been walking around grinning foolishly in front of everyone only a few hours earlier was like the difference between heaven and earth.

*So he found a way to survive on his own terms?*

Heugung’s sudden contact was still suspicious, but after hearing his story, I trusted him more than I had at first.

The fact that the somyeon tasted much better than I had expected probably helped, too.

Slurp.

After drinking down the rich broth, I took a few iron coins from my clothes and placed them beside the empty bowl.

Then I rose without hesitation and patted Heugung’s startled shoulder.

“You were right. This place does make good broth.”

“I-I’m glad to hear it. But where are you going…?”

“Why? If we’ve finished eating, we should get moving. You look like you’re in a hurry to get somewhere, too. Aren’t you?”

At that moment, Heugung’s eyes widened slightly.

He had probably heard the Sound Transmission I let slip along with my words.

—Follow me. Slowly, and keep your distance.

I had dealt with the appetizer using somyeon.

Now it was time to taste the main course.

—Let’s hear it. Everything you’ve seen and heard while standing beside Baeksang all this time.

* * *

The streets were packed so tightly that there was barely room to set foot anywhere.

Heugung and I melted into the crowd and began moving slowly, keeping about ten feet between us.

Now and then, we watched fireworks bursting overhead or casually turned our heads to take in the street.

But the Sound Transmission passing between our moving lips never turned toward anything else for even a moment.

—Let me get straight to the point. Is there any indication that Baeksang has colluded with Dark Heaven?

—Although I have no concrete evidence, I am certain from everything I’ve observed until now.

—That isn’t enough without evidence.

—I had no choice. Until now, I’ve been in the position of livestock living inside the fence Great Chieftain Baeksang built around me.

—Then tell me the exact timing, and why you came to that conclusion.

—Although I was raised like livestock inside that fence, it isn’t as if I was unable to see even a glimpse of what lay outside. I may be a great chieftain in name only, but I still lead one of the tribes, so I was occasionally able to be in his company. No—perhaps he simply thought I was someone not worth worrying about. He wouldn’t have been wrong.

Heugung’s Sound Transmission continued with a self-deprecating edge.

—Do you know what kind of person Great Chieftain Baeksang is? What about the Bai people?

—I don’t know much about Nanman, but I’ve heard various things from a reliable source. I’ve also formed a certain judgment of Baeksang myself.

—A judgment. Interesting.

—What’s interesting about that?

—It’s simple. I’ve known Great Chieftain Baeksang since I was very young, but I had to revise my judgment of him every time. The older I got, the more mature I became, and the more I thought about things, the more often that happened.

“…”

—That is the kind of person he is. This land is made up of dense forests, deep swamps, and all kinds of difficult terrain. It does not tolerate secrets leaking out. For example…

His voice trailed off.

The next moment, I felt someone’s gaze and turned my head.

Heugung’s eyes shone clearly as they met mine.

—The Bai people’s finest warriors, who must even now be waiting for the right moment in some secret refuge somewhere in Nanman.

My feet stopped before I could help it.

I turned my head toward a nearby street stall as naturally as possible and moved my lips.

—Continue.

—Have I ever told you what kind of person my late father was? He was a great chieftain with tremendous popularity, and an outstanding warrior. The loyal retainers who followed him from the bottom of their hearts helped me even at the cost of their own lives. It was thanks to their sacrifice that I learned about the secret refuge.

—Do you know its exact location?

—I did. Twenty years ago.

—…Twenty years ago?

—The only thing that returned that day was not one of my loyal retainers, but a messenger pigeon carrying a missive written in blood. I grew desperate, and a few days later, I used a hunt for ferocious beasts as an excuse to head to the location written in that message. Before I had even reached the foot of the mountain, I saw a massive fire swallowing the entire mountain.

“…”

—The flames did not die down until a month and seven days had passed. Nothing remained there but ashes. What do you think? Isn’t it a truly strange thing?

Heugung continued his Sound Transmission in a bitter tone.

—Every time one of my loyal retainers died, I learned something new. Great Chieftain Baeksang exchanges missives to unknown destinations on the first day of every month, between Insi and the hour of the Rabbit.[^1] He also disappears somewhere alone once every three months… Ah, since last year, that changed to once a month. The person who followed him then was the last subordinate I could trust. I never saw him again after that.

When his story ended, a heavy silence settled between us.

The surroundings were filled with cheerful voices and shouts of excitement, but Heugung and I were exceptions.

*Baeksang and Dark Heaven. Dark Heaven and Baeksang. And…*

*Heugung.*

Which of these was true, and which was false?

My thoughts were hazy, as though I had been swallowed by Poison Mist.

But beyond that haze, I could clearly see the silhouette of one person I had followed with my eyes and heart from the beginning until now.

*Baeksang.*

And one other person who had yet to show themselves.

A name suddenly flashed through my mind, and I sent a Sound Transmission toward Heugung.

—What about the other person?

—The other person? Who are you talking about?

—The other great chieftain. Yohi.

“…”

—I’ve been curious about that for a while. You haven’t said a single word about her.

Beyond the people passing by, I saw Heugung’s gaunt frame jolt. His gaze met mine across the open air, trembling faintly.

—She hasn’t done anything wrong.

—What?

—She merely made the wrong choice. She did it solely out of her determination to revive the Yao people…

His voice gradually faded.

I blinked blankly at Heugung, and the back of my head began to tingle.

*For fuck’s sake. Surely this man didn’t…*

—Don’t tell me none of that was an act. Do you really like Yohi?

—I don’t like her. I love her.

—Excuse me, but are you some kind of crazy bastard?

“…”

This was driving me crazy.

I had suspected as much, but all those foolish grins whenever Yohi appeared had really been genuine.

He had even put up a soul shield strong enough to make Magic Johnson cry.

I barely managed to restrain myself from pushing through the crowd and marching over to him. Instead, I sent a Sound Transmission that was almost a shout.

—Would you say that in front of Sir Yayul, too? That Yohi did nothing wrong?

—That is why I came looking for you. First, I guessed that the Palace Lord would not trust me more than Great Chieftain Baeksang. Second, I thought he would not forgive our Yohi.

—Wow. Listen to this “our Yohi” bullshit.

“…”

—Ah, sorry. But you really are an idiot. Anyway, I understand now. Your Yohi defected to that side.

Heugung’s complexion hardened rapidly, as if he disliked my choice of words.

He moved his lips as though he intended to say something, then let out a sigh.

—Before I came here, I had already made up my mind. If you and the Palace Lord wish it, I can appear as a witness at tomorrow’s Tribal Grand Council. But you must promise to guarantee Yohi’s safety and mine.

The first was a good offer. The second left a bad taste in my mouth.

And if those two offers had one thing in common, it was that neither was something I could decide on my own, here and now.

Heugung was one thing, but in Yohi’s case, granting her safety would essentially mean giving a defector a get-out-of-jail-free card. I wasn’t Syngman Rhee, who had welcomed pro-Japanese collaborators, so how could I decide that alone? At best, I was the U.N. forces.[^2]

*But if the Beast Miao King gave his permission…*

If that happened, everything that followed would proceed at a breakneck pace.

If Heugung’s words were true, we could not only root out Dark Heaven’s threat from Nanman, but might even drag the Nanman Beast Palace into the Murim Alliance as one enormous headache.

But all of that depended on this being true.

—It had better be true. It absolutely must be.

Fsssh!

A wave of qi unleashed solely to bear down on one person.

Heugung felt power that he could not possibly resist. His face turned pale as his lips moved.

—My life. I stake my life on it.

I stared at Heugung in silence, then withdrew my aura.

He stood there panting, looked around, and gave a small nod before melting into the crowd and disappearing.

The half hour he had mentioned had passed.

“…Phew.”

Only then could I breathe freely. I took a deep breath and began walking.

Before reporting this to the Beast Miao King, I planned to stop by the quarters and discuss it with the members of the Fire Dragon Pavilion.

*Those damn men. I’ll consider it a success if they haven’t caused any trouble.*

* * *

Sama Pyo had come out to the clearing in front of the quarters to train when a thought suddenly occurred to him.

Was he simply born unlucky, or had the karma from that damn Pavilion Master’s misdeeds flowed all the way here like a stream?

“And so I ask you…”

Shing.

The Black Dragon Saber emerged with a cold ring.

Sama Pyo took a step forward with his treasured weapon in hand and continued.

“What do you lot think?”

Rustle.

The grass surrounding the clearing shook.

[^1]: Insi is the traditional time period from three to five in the morning; the hour of the Rabbit follows it, from five to seven.

[^2]: Syngman Rhee is often criticized for allowing many collaborators with Imperial Japan to retain influence in post-liberation South Korea.
## Chapter artifact 652

# Chapter 652

Rustle.

Sama Pyo knew that what was shaking the dense grass was not merely a passing breeze.

The killing intent of dozens of enemies was aimed at him like invisible blades.

“They come without being invited. And when I ask them something, they don’t even answer…”

There were no more unwelcome guests than these.

Clicking his tongue softly, Sama Pyo lowered his Black Dragon Saber, his personal weapon, and spoke.

“Come out. Let’s talk face-to-face.”

The answer that came instead was a volley of a dozen or so throwing blades.

Whoosh! Clang!

Sama Pyo swung the Black Dragon Saber like lightning and knocked the blades aside, smoothly twisting his body.

At the same time, the saber energy coiling around the dark blade became a gale that tore through the grass.

Sh-sh-sh-shk! Slash!

Hundreds of leaves were sliced into pieces and scattered through the air, while a faint line was carved across the trunk of a massive tree.

Sss, crash!

The giant tree slid to the ground. Sama Pyo vaulted over it and stared at the figures approaching the clearing.

East, west, north, and south. The roughly thirty enemies slowly moved into position, surrounding the pavilion from every direction.

Every one of them concealed their face behind a black mask.

“Getting a look at your faces is difficult. If you came here without permission, common courtesy would dictate that you at least remove your masks and apologize… but I suppose that’s not going to happen.”

Sama Pyo calmly accepted the situation.

Unwelcome guests arriving in masks at this late hour. The fact that they had greeted him with throwing blades made their purpose absurdly clear.

Moreover…

*Of all times, this had to happen while he was away.*

He suddenly thought of that Pavilion Master bastard, whose mouth was filthy as a Third Rate thug and whose hands itched to punch someone whenever he got the chance.

*Jin Taekyung.*

He was impossible to predict and constantly caused trouble, but in a situation like this, he was also more reliable than anyone.

After all, he was a monster who had left his mark on the Murim at the age of only twenty-two.

But whether by coincidence or fate, Jin Taekyung was currently away. Song Ilseom and Ju Hwaran, who would have been a great help if they had remained, were absent as well. Hyuk Mujin was gone, too—although he might not have been able to match them, he was at least worth one person.

Those who remained were Sama Pyo himself, Taishan, who had gone to sleep early, and Namho, an ordinary old man who could not even be counted as fighting strength.

Meanwhile, the enemies numbered nearly thirty.

*No, the numbers aren’t the problem.*

Sama Pyo muttered inwardly and quickly swept his gaze across the surroundings. The killing intent radiating from the enemies slowly tightening around him like a net was not that of some clumsy martial artists.

*By Central Plains standards, every one of them is between upper First Rate and Peak. Where in Nanman did these people come from?*

The Central Plains Murim was truly vast, but even among the countless martial artists scattered across it like grains of sand on a beach, Peak masters were not common.

Yet in Nanman, which could not compare to the Central Plains in size or population, someone had mobilized thirty warriors of this caliber to launch an attack.

Fortunately, they were not at an especially high level, but it was hardly strange that Sama Pyo found their appearance surprising.

Especially since this area, despite being far from the center, still clearly belonged to the Inner Palace of the Nanman Beast Palace.

“Who are you?”

Whoosh! Crack!

Instead of an answer, a short spear skimmed dangerously past his neck and smashed through the pavilion door.

That was the signal that began the battle.

Papapat!

Hidden weapons and arrows flew through the air, blocking out the faint moonlight. Shadows rushed forward like rays of light.

At the same time, the Black Dragon Saber in Sama Pyo’s hand moved, cleaving through the wind.

Whiiiiing! Slash!

Powerful saber energy split the air and swept away the hidden weapons and arrows. The instant Sama Pyo broke through the net of projectiles, blades came slashing in from both sides.

Whoosh!

The attackers’ hands showed not the slightest hesitation as they aimed for his vitals. Their coordinated attack was exquisitely timed.

If Sama Pyo had been an ordinary Peak master, this attack would have inflicted a serious wound—or taken his life.

But Sama Pyo was different.

He was not a young prodigy lacking real combat experience, nor was he as rigid as a Peak master from an orthodox faction.

The greatest value of demonic, heterodox arts was survival.

Click, crunch!

With a dull sound, the two Peak masters who had charged in from either side collapsed like rotten trees.

Their eyes were wide behind their masks, and a small arrow a span long was buried deep between their brows.

*It worked.*

There was a simple reason Sama Pyo had worn a thin robe instead of the lighter martial uniform suited to such hot weather.

It allowed him to hide hidden weapons inside its voluminous sleeves.

The principle behind the mechanical device was simple. A loaded arrow was fired when he twisted his wrist at a predetermined angle. But in an unexpected situation, it was more lethal than anything else.

“Idiots.”

Sama Pyo spat the word out, then pulled the two collapsing bodies toward him and propped one in front of himself and the other behind him.

Thud-thud-thud!

The hidden weapons that flew from nowhere turned the bodies of men who had been allies only moments earlier into pincushions. Using them as shields, Sama Pyo aimed his sleeve through the gap beside one corpse’s ribs.

Click, thud!

But the enemies had recognized what was happening by then.

Instead of striking the space between the brows he had originally targeted, the arrow embedded itself in a forearm. He had already shown the trick twice. It would not work again.

*In that case…*

Snap.

Sama Pyo made his decision swiftly.

He disengaged the mechanical device hidden in his sleeve, let out a shout like a battle cry, and charged toward the enemies.

“Taishan!”

Sh-sh-sh-shk!

The masked men, reduced to twenty-seven, surrounded Sama Pyo like wolves.

* * *

Bang!

Namho had tossed and turned for a long time before finally falling asleep. The instant he opened his eyes, he thought:

*What fucking bastard is this?*

There were countless disadvantages to growing old, but the most miserable of them was that one’s sleep became shorter.

And yet someone had dared to disturb the sound sleep of an eighty-year-old man. As Namho pushed himself upright, his joints creaking, he made a firm resolve.

*If that gluttonous bastard Taishan woke me up because he was eating a midnight snack… this time, I absolutely will not let it slide.*

Even if it did not look that way, he had fifty years of experience in the Hidden Shadow Pavilion.

He had devoted himself body and soul during the Great Faction War. Even if he sent a letter to Henan and had Taishan declared an enemy of the Murim, he thought the Thousand-Faced Fox might overlook it just this once.

*Would he believe me if I said the bastard was a Dark Heaven spy?*

But Namho’s worries soon vanished like a bubble. The reason was the uproar coming from outside the window.

“Taishan!”

Sh-sh-sh-shk! Clang!

Cha-cha-cha-chang!

Namho had been staring blankly down at the clearing from the window when he rubbed his eyes, wondering for a moment if he was seeing things.

But what was happening before him was not a dream. It was unmistakably real, and the Sword Energy of someone whose attack Sama Pyo had evaded swept past the window where Namho stood.

Slash! Crash!

Namho finally understood the situation.

*An ambush!*

And not just any ambush. This was a thoroughly planned attack. The fact that they had struck while that madman—no, while Jin Taekyung—was away made that obvious.

*What the hell is this? Who in the world…!*

The unpleasantness of being woken up was no longer a problem for Namho. Soon, it would not be his sleep but his head that was in danger of being lost.

Sama Pyo was fighting better than Namho had expected, but if this continued, it was obvious that he would eventually fall beneath the overwhelming numbers.

And then—

Papapat!

When Namho spotted several masked men approaching the pavilion while leaving Sama Pyo behind, he no longer had even a moment to hesitate.

“Gah!”

Terrified, Namho dashed from the room with a speed that belied his eighty years.

He raced across the corridor at the end of the room and threw open the tightly shut door.

Bang!

“Ambush! It’s an ambush! Your master is outside right now—!”

The owner of the room, Taishan, answered in a booming voice.

“Grrrrrrrk. Hooooooonk!”

“You damn piece of shit!”

“Guh-hoooooonk!”

Namho could not believe it.

*He can sleep through even this? Is this thing really human?*

Parts of the pavilion were collapsing, and the noise of clashing weapons was loud enough to be heard all the way to Henan.

And yet Taishan was actually sleeping inside the pavilion, snoring loudly.

“Wake up, you bastard! Get up at once!”

Thud! Thud-thud!

With a soul-rending cry, Namho’s fist—its strength diminished by the passing years—slammed into Taishan’s jaw.

As if the heavens had been moved by Namho’s devotion, Taishan finally tossed and turned.

“Umm. Taishan.”

“Yes! Now get up! Quickly!”

“Mmmm. Taishan doesn’t like mosquitoes. Go away…”

“You son of a bitch!”

The cry that came from Namho was almost a wail.

Just as tears were beginning to glimmer in his eyes, the moonlight streaming through the wide-open window cast a black shadow across the floor.

“…”

Namho’s body went rigid.

He slowly turned his head. Three masked men who had already infiltrated the pavilion appeared in his gray eyes.

*Those, those bastards…*

Their movements were almost ghostlike.

At that moment, the weapons in the masked men’s hands caught the moonlight and gleamed white. Namho, who experienced a sweeping panorama of his eighty-odd years, realized the only way to wake Taishan.

“Taishan! You bastard!”

Sss.

The masked men raised their weapons as Namho shouted. Thinking of death, Namho squeezed his eyes shut and continued yelling.

“They’re going to eat all your meat!”

And in the next moment—

“No! Taishan’s meat!”

Taishan’s eyes flew open as if by magic, and he thrust one fist toward the masked men.

Wham! Krrrra-boom!

* * *

Hoo. Hah.

Sama Pyo steadied his ragged breathing.

His upper body was drenched in blood, and the gazes of the masked men watching him now contained a faint trace of fear.

Sama Pyo’s desperate struggle had been harsher, fiercer, and more brutal than they had imagined.

Hidden weapons and poison concealed throughout his body, along with martial arts built entirely around practical combat for the purpose of killing.

But even more frightening was that he showed no fear of death.

“Come, whoever you are. I swear I’ll stake everything I have and kill you.”

As Sama Pyo charged at them, panting heavily and drenched in blood, the masked men fell one after another beneath his hands.

By then, twenty bodies lay scattered across the ground. Seven of them had been Peak masters recognized anywhere in the Central Plains.

*What kind of monster is this?*

At the moment the masked men all reached the same conclusion—

“No! Taishan’s meat!”

Crack! Krrrra-boom!

A true monster emerged from the collapsing pavilion.

A madly enormous body standing nearly eight feet tall. An immense frame. And…

“Taishan’s meat! Where’s the meat!”

A madness that seemed not of this world.

Gulp.

*What the hell is that?*

Just as the masked men swallowed nervously, a tiny old man poked his head out from behind the monster and pointed at them.

“You see those guys?”

“Taishan! Sees them!”

“I saw everything earlier, and those bastards ate all your meat.”

“Taishaaaaaan! Cannot forgive them!”

What did meat have to do with anything, and what did they mean by stealing and eating it?

As the flustered masked men cautiously stepped back, Sama Pyo revealed bloodstained teeth and smiled.

But he was not looking at Taishan.

His gaze was fixed on a hill overlooking the clearing.

More precisely, he was looking at someone trudging down the hill.

“I had a feeling this might happen even while I was away for a little while.”

Step. Step.

The young man approached at a leisurely pace and asked Sama Pyo:

“Are those your friends?”

Sama Pyo burst into laughter and shook his head.
## Chapter artifact 653

# Chapter 653

“Are those your friends?”

Sama Pyo burst into laughter and answered in a tired voice.

“No way.”

“Then again, you all seem to be on pretty bad terms for friends.”

I scratched my chin and slowly looked around.

The already ancient pavilion had collapsed, and the weeds growing thickly across the clearing were stained red with blood.

*All right. Situation assessed.*

*What a complete fucking mess.*

In the short time I had been away from the residence, more than twenty corpses had appeared. Even if a snail bride had come to clean the place, she wouldn’t have been enough.[^1] And now we had a nighttime ambush on top of it.

I glanced at the assassins, who had hesitated at my appearance, then shrugged at Sama Pyo.

“Oh, you’re doing a little better than I expected.”

Sama Pyo’s upper body was drenched in blood. He answered between rough breaths.

“Yeah, I’m doing pretty well. For an unorthodox goon.”

In truth, I felt bad calling him an unorthodox goon anymore.

They had been completely outnumbered. And the fact that they had fought this hard against enemies of considerable skill meant they had truly staked their lives on it.

I nodded inwardly, impressed.

“You’ve done enough that it feels wrong to keep treating you like some lowly goon from the unorthodox faction… From now on, I’ll call you an unorthodox hardcase.”

“Unorthodox hardcases. How kind of you.”

“Oh, you’re grateful? Unexpected. I thought you’d start cursing me the moment you heard it.”

“You need energy to curse. And I feel like I’m about to collapse, so stop talking to me.”

I let out a short laugh at his honest answer and opened my mouth.

“Then collapse.”

“What?”

“I said collapse. Don’t worry about what comes after.”

“Damn it. You should’ve said that sooner…”

His words trailed off as his eyes began to close. At the same time, Sama Pyo’s body slowly tilted to the side, and I stepped toward him.

Whoosh. Thud.

The three-zhang gap vanished in an instant.

The moment I caught him before he could pitch face-first into the ground, a sharp whistle split the air and a gust of wind whipped up.

Whoosh!

It happened behind me, but I could see it. No—I could sense and read everything through my sharpened instincts.

Now that I had stepped into a new space, this place was practically my domain.

Crack!

Without even turning around, I swung one fist. Something shattered beneath it. A masked man whose head had been crushed like tofu slammed into a pool of blood.

Splash.

Sticky blood sprayed through the air and soaked my back. Ignoring it, I laid Sama Pyo down on relatively clean ground, then suddenly raised my head.

The masked men stood frozen like stone statues.

“But why are you all standing there? That was your last chance, at least.”

“……”

“……”

“Why are you so surprised? Were you planning to ding-dong ditch me, you fucking bastards?”

In the suffocating silence, the ten pairs of eyes visible above the masks shook violently.

Then—

Papapap!

Whiiiiing!

A gale far fiercer than the first swept out in every direction.

The masked men who remained were all Peak masters at the level of injuring others with Sword Energy.

Sword, saber, spear, sickle…

Destructive energy poured from each of their weapons, cutting through the air and targeting the vital points throughout my body.

But I watched and read all of it without the slightest fear.

The flow of qi. The direction their weapons were aimed.

And even the faint fear reflected in their wide-open eyes.

That was the end of it. They had already lost this fight.

They had realized that they were nothing more than wolves. And yet they had refused to accept it and charged at a tiger.

*Then I’d better teach them. Teach them that they should have run somehow.*

Dozens of forms flashed through my mind in the span of an instant. I chose the cruelest and most destructive one and moved.

Whoosh! Crunch!

I smoothly twisted my body, and the four weapons that had barely missed me tangled together as they crossed toward one another. I brought down a straightened hand blade on their center.

Slash!

The weapons were cut into pieces by Force.

I slammed my palm into the abdomen of one of the masked men who stood frozen, still clutching his now-useless favored weapon.

*Flame Divine Palm.*

Boom!

Terrible heat burned away the life force inside his body. I lowered my head as he crumpled behind me, smoke pouring from his seven apertures.

Shaaak! Whoosh!

A blow flew from behind me without warning.

But the long sickle that had tried to reap my neck passed through empty air, while the elbow I thrust backward struck the enemy squarely in the chest.

Crack!

The sound of more than a dozen ribs breaking rang out, followed by a dying gasp.

But it was not my strike that took his life. It was the spear thrust by his comrade.

Thrust!

*Look at these bastards. Not a shred of comradeship.*

Clicking my tongue, I grabbed the spearhead protruding from his chest and applied force.

Crack!

If my opponent was a Peak master who had reached the level of injuring others with Sword Energy, then I was a Supreme Peak master who had entered the realm where Sword Energy became Force.

I casually snapped the spearhead off as if breaking a pair of wooden chopsticks, then immediately returned it to its owner.

Whoosh! Thunk!

The result was obvious: instant death.

The masked man with the spearhead embedded between his brows collapsed without even managing to scream. The remaining masked men swallowed their gasps after losing three comrades in a span too short to even call a moment.

*Seven left.*

I calmly counted the enemies and stepped forward.

Whoosh!

Space disappeared along with the wind, and a new enemy appeared right in front of me.

No—I was the one who had approached.

“……”

His wide eyes seemed to be trying to say something, but it was already too late. I tightened the hand clamped around his neck.

Crack!

*Six.*

I felt the life drain from his body as it went limp all at once.

I naturally snatched the sword from his hand and sent it flying toward the nearest enemy.

“Hng!”

With a breath that sounded like he had been scared out of his soul, the enemy raised a curved moon saber diagonally.

The sword I had fired in a straight line collided with the moon saber, which was imbued with saber qi.

Boom!

The ground flipped over with a deafening roar. A staggering figure emerged through the dust billowing into the air.

The moon saber had shattered because it could not withstand the energy contained in the sword, and dozens of fragments were embedded throughout the man’s body.

“Grrk. Grrr…”

Thud.

Perhaps because the largest fragment had pierced his throat, he collapsed with blood bubbling in his throat without managing to leave even a last word.

I pushed aside the corpse of the enemy whose neck I had broken and spoke quietly.

“Five left.”

“……”

“……”

I could feel it—the fear filling the suffocating silence.

Five Peak masters had fallen in the span of mere moments, and I was stalking my next prey without a single wound.

“Who wants to come next?”

No one answered my question.

Then the masked men, frozen in place and staring at me with eyes wide as if they had seen a ghost, chose to target someone else instead of me.

Papap!

Of the five remaining men, three targeted me, while the other two targeted Namho and Taishan.

I admitted it. That was probably the best choice available to them.

But regardless of my opinion, the result of that choice could not be called their best.

“I saw it clearly! Those bastards ate both chicken legs!”

“Legs? Not wings, but legs? And both of them?”

Taishan blinked in disbelief at Namho’s shout, then pulled the two-section staff hanging at his side free.

“Two chicken legs! You crossed the line! You are not human!”

We would have needed to hold a vote to determine who was not human, but Taishan made the vote itself meaningless with his enormous two-section staff.

Wham! Crack!

His innate divine strength was more than enough to render even a defense useless.

One of the masked men instinctively raised his sword to block the two-section staff. Both his wrists broke, and before he could even scream, his head was smashed together with that of the other man.

Crack!

Two corpses rolled across the ground without managing to utter a dying cry.

Namho, who had been hiding behind Taishan, clenched his fist and shouted.

“That’s right! You commendable bastard I could just kill!”

“Uaaaaaah! Taishan is commendable!”

“Well done! You goddamn bastard! You’ve done nothing but stuff yourself to death every day, and you finally decided to earn your keep!”

I let out a short laugh as I watched Namho heap abuse on him—though I could not tell whether it was an insult or praise—then spoke to the remaining enemies.

“All right. Three left.”

“……”

“……”

“……”

The corners of the masked men’s eyes trembled as they understood what I meant.

Even while their comrades were dying one after another, they had been backing away without daring to attack me.

“I’m telling you this just in case, but if you run, you’ll die. Of course, unlike your friends who went sightseeing at Mount Beimang first, you’ll die much more painfully after lingering a long time before your breath finally stops.”

Someone’s throat bobbed visibly.

The men had all watched with their own eyes as their comrades died in front of them. But if they ran, they would end up wishing they could die that way instead.

“But if you surrender here and tell me what I want to know… I’ll keep you alive, no matter what it takes. If you don’t believe me, I’ll even stake my life on it.”

I had no desire to let men who had come here with such intentions live, but I had to uncover who was behind this.

I slowly recited the names that came to mind.

“Baeksang. Heugung. Yohi. If one of them is your master, confess right now. And if someone else ordered you to do this, tell me everything you know about that, too.”

*Who could it be?*

I had suspicions, but there was no one I could identify for certain.

Still, only a handful of people were bold enough to cause something like this in the Inner Palace, powerful enough to mobilize warriors of this caliber for an assault, and well-informed enough to notice my absence.

*It has to be one of the three great chieftains.*

They had moved so secretly, and yet someone had noticed.

I did not know who had learned of it or how.

And on top of that, the ambush had come at an incredibly precise moment.

Given the circumstances, I could not help but suspect Heugung, whom I had parted from barely fifteen minutes ago after he promised to cooperate.

*Did he ask to meet me so he could stab me in the back like this? Was he planning to deceive me first, seize the Fire Dragon Pavilion members, and use them to threaten me?*

Or it could have been Baeksang, who had been watching Heugung, or Yohi.

And one thing was certain: whatever name spilled from the mouths of these masked attackers would belong to a Dark Heaven hound.

“Who is it? Speak.”

Ssssss.

I pressed down on them with overwhelming qi, and the exposed foreheads above their masks creased in pain.

Then, in the next moment, I saw the corners of the masked men’s mouths twitch.

Crunch.

“……!”

A chill swept over me. I hurriedly fired Finger Qi and struck their pressure points, but dark-red blood burst from the mouths of the men who had severed their own heart meridians.

“Grrrk. Cough.”

*Fuck.*

[^1]: A snail bride is a figure from a Korean folktale who secretly does housework for a poor man.
## Chapter artifact 654

# Chapter 654

If someone asked whether I could kill three Peak masters with a single move, I would nod without much hesitation.

But if they asked whether I could subdue three Peak masters in a single move, and those three had the mindset of assassins, the answer would be different.

In that situation, the right approach was to subdue them through persuasion rather than force. To prevent them from committing suicide, I had to give them confidence that they would survive—not let them suffer through torture before dying painfully.

But…

Crack.

Apparently, my promise had failed to give them that confidence. Or perhaps their fear of their master was even greater.

Ssshhh! Thud!

The Finger Qi fired from my fingertips a half-beat too late struck their acupoints, but it was already impossible to turn things around.

The three bodies, stiffened after their Paralysis Acupoints were struck, were already collapsing as blood sprayed from their seven apertures.

Papap! Grab.

I closed the distance of several zhang in an instant, caught the three falling figures, and laid them on the ground.

Sticky blood bubbled up from the corners of their mouths beneath their masks.

“Grrrk, cough…!”

Damn it. The situation was bad.

No, it was the worst.

Severing one's own heart meridian was like setting off an explosion inside the body.

If the Eight Extraordinary Meridians—the most important meridians in the human body—as well as the hundreds of acupoints throughout the body were severed and blocked, there was no way to survive.

*Especially for a Murim practitioner.*

The so-called high risk, high return.

Through qi accumulation, a Murim practitioner gained abilities that surpassed those of ordinary people. But if their heart meridian was severed, they also got a bonus one-plus-one event called qi deviation.

Just like now.

“Cough. Kueeegh!”

Splaash!

Eyes, nose, mouth.

Ears.

Dark-red blood and pale lumps that looked like internal organs poured endlessly from every opening I could see.

At the sight of this horrifying scene, Namho and Taishan hurried over, then stopped short.

“Ugh. Taishan. I don’t want to look at this. I’m losing my appetite.”

“W-What is this?”

Namho swallowed dryly and asked in a lowered voice.

“Can they be saved?”

It was a meaningless question. The situation had already reached the point of no return.

Before I could answer, the heads of two of the men, whose entire bodies had been twitching and convulsing, fell limply to the side.

Thud.

There was no need to check. They were dead.

But it was still too early to give up. I grabbed the last masked man's wrist and poured my internal energy into him with all my strength.

Sssaaaaah.

As the Scorching Yang Qi carrying intense heat flowed into his body, I could feel his ruined insides.

Not a single internal organ remained undamaged, and the qi pathways that should have been broad and sturdy in a Peak master had collapsed like the walls of a dilapidated house.

*And on top of that, qi deviation…*

Even if Mungyeong, the greatest Divine Physician under Heaven, came here, he could not guarantee the man's life.

Realizing that he was beyond saving, I clenched my teeth.

*I have to find out. No matter what.*

I only needed one name. The name of the one person who had ordered today's attack.

I poured out my internal energy without restraint—not to control the masked man's insides, which had entered an irreversible state of rampage, but to fan his final ember into flame.

Rumble!

His entire body struggled violently as an even greater flow of internal energy entered him.

But just as the surface of a body of water grows calm after a violent storm has passed, the masked man on the threshold of death regained a brief moment of peace and reason.

A final rally.

This was truly the end. I stared into the masked man's eyes, which had regained their focus, and asked,

“Who was it? Speak.”

And then, as I pulled down the mask around his mouth to hear his final answer, I realized that this last attempt and question had been meaningless.

“Cough. Hhh. Haaah.”

“……!”

“Grrk. Uhh…”

His jaw moved up and down as though he were trying to say something. But no words came out.

No. The more accurate way to put it was that he could not speak.

As my mind froze like a stone statue, I heard Namho mutter with a groan.

“Such vicious bastards. Their tongues…”

His voice did not reach the end, and the masked man had been given far too little time.

“Grrk.”

With a death rattle that served in place of a last will, his pupils went blank. His mouth hung open, and the short tongue that had moved as though it were trying to say something went limp.

I stared silently at the man who had finally met his death, then spat out the curse I had been holding back.

“…Fuck.”

I had known they were no ordinary men, but I never imagined their tongues had been cut out.

There had been a reason they had not said a single word from beginning to end apart from their screams.

No. Even if they had wanted to speak, they couldn't.

“Hmm. The others are the same. Judging by how the severed ends of their tongues have healed, it looks like this was done a long time ago.”

Namho quickly examined the corpses like the Hidden Shadow Pavilion agent he was, then let out a low groan.

“These men… They’re all Nanman.”

“Are there no Han Chinese among them?”

“Not one. Their clothes are all identical, so we can’t even tell which tribe they belong to.”

The most reliable way to distinguish the Nanman was by their clothing and eating habits. But since every one of them wore black clothes and a mask, it was only natural that they were difficult to identify.

Besides, there was only a subtle difference between the appearances of Han Chinese and Nanman. Trying to identify their tribe at a glance was practically absurd.

“…Damn it.”

As I muttered a curse mixed with a sigh, Namho fixed me with a deeply serious gaze.

“When you were trying to persuade those men, you mentioned three great chieftains as possible culprits. So was the person who sent the missive Heugung?”

I looked at Namho in surprise.

That was answer enough.

“I see. So that’s what happened.”

“How did Elder Namho know…?”

“Baeksang and Yohi were both people who could reasonably be named as culprits. But Heugung was different. Thinking about it, there could only be one reason you would have thought of him in this situation.”

Namho finished speaking in a calm yet cold tone, then opened his mouth again.

“Was it him?”

“Yes.”

I nodded and continued.

“He was waiting for me at the place written in the missive.”

“He chose to hide in the forest rather than behind the rock. But no matter how many people there were, someone with Heugung’s build would have stood out. You mean he came out himself?”

“He had learned the Bone-Shrinking Technique. At first, I didn’t even suspect that he was Heugung.”

“Hah, the Bone-Shrinking Technique. He was a man with more secrets than he let on. He fooled everyone completely. Well, if he were really the man the world believed him to be, he wouldn’t have sent you a missive in the first place.”

Namho muttered as if to himself, then continued with a heavy expression.

“Go on.”

The story about Heugung had been short, but its contents were not something that could be dismissed.

Namho listened to the entire story without saying a word. Then he furrowed his already wrinkled brow even more deeply.

“What a goddamn mess.”

I agreed.

Something had happened, but I still could not narrow down the suspects.

Baeksang, Yohi, and Heugung. Given the circumstances, it was difficult to rule out any of them.

On top of that, the true force behind today's attack could be summed up in two words: Dark Heaven.

*I can tell just from the fact that they severed their heart meridians instead of taking a poison pill.*

Because of Nanman's characteristics, obtaining a deadly poison that could be used for suicide was incredibly easy. This was the sort of place where all kinds of venomous beasts swarmed even if you simply went on a picnic in the grass outside the Outer Palace.

But the masked men had chosen to sever their own heart meridians.

Compared to a fast and easy poison pill, severing one's heart meridian was a way to die after suffering several times more intense pain.

I had no choice but to assume that they already knew about it.

*The Myriad-Poison Ring. Dark Heaven must already know that I have it.*

Dark Heaven had sent the Blood Lord to cause the Shaolin Bloodshed, and in Sichuan, they had sent the Western Heaven Demon Lord to steal the sacred treasures of the Emei Sect and the Sichuan Tang Clan.

They had poured Supreme Peak masters who were no weaker than the Ten Kings—perhaps even comparable to the Three Saints—along with elite forces into the operation for the sake of those treasures.

*But even immediately after the Sichuan Blood Tragedy ended, nothing happened to the Sichuan Tang Clan.*

The Sichuan Tang Clan had staggered after suffering more severe damage than any other sect in Sichuan during its battle with the Western Heaven Demon Lord. But the follow-up attack from Dark Heaven that everyone had feared never came.

And I suspected that the decisive reason was whether or not they had the Myriad-Poison Ring.

*So instead of a poison pill, they severed their heart meridians to eliminate even the slightest possibility.*

A single drop of cold sweat ran down my spine.

My enemies were watching my every move, while I could not even identify the person hiding in the darkness.

The mere fact that an attack like this had taken place in the Inner Palace of the Nanman Beast Palace—the heart of Nanman—was threatening enough.

“When did the attack begin?”

Namho answered my question in a heavy voice.

“I don’t know exactly. I woke up in the middle of it, but… It seems to have started less than half a shichen after you left. I went to check because I wondered what was happening, and everything outside was in chaos. That bastard Sama Pyo was fighting while covered in blood.”

Namho pointed toward Sama Pyo, who was lying on the ground, then asked with concern in his eyes,

“But is he all right? He seems to have lost a lot of blood fighting them.”

“I stopped the bleeding, so he should be fine. From what I could see, he didn’t have any immediately dangerous wounds. Most of the blood on him seems to belong to the enemies.”

Taishan returned after dragging the corpses into one place and blinked his enormous eyes.

“Pavilion Master, true? Is Taishan’s Lord okay?”

“Yes. He only collapsed because he used too much strength.”

Apparently satisfied with the answer, Taishan's eyes filled with a cloudy film of tears.

“Sniff. Taishan was worried. If Lord died, Taishan would not eat meat for three years. Sniff.”

“……”

“……”

I had heard of a three-year mourning period, but this was the first time I had heard of a mourning custom that involved giving up meat for three years.

At that rate, he might become the strongest vegan in the Murim.

I swallowed the words rising in my throat and patted his Ural-Mountains-sized shoulder.

“Yes. You worked hard too.”

“Sniff. Taishan used lots of strength. Taishan hungry.”

“…Yeah. Okay.”

Should I just punch him?

But as I was deep in thought, countless footsteps began approaching from far away, accompanied by torchlight.

And with them came the familiar roar of a beast.

—Rooar!

Ssshhh! Pap!

A silver figure that stood out clearly in the darkness reached the clearing first.

Yayul Mok's face, as he rode atop the White Tiger, was stiff as a wooden doll.

“…I’m late.”

I answered calmly.

“Yeah. Late enough that it’s hard to believe something like this happened in the Inner Palace.”

Collapsed pavilions. Pools of blood gathered here and there. Corpses piled up in heaps.

Yayul Mok clenched his lips tightly before speaking.

“The warriors on patrol were dead. We only found out half a gak ago. And…”

The next moment, after hearing Yayul Mok's words, I could not help wondering whether I had heard correctly.

“Heugung and Yohi. Two great chieftains have disappeared.”

…What?

# Checkpoint Review — 665–669

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

# Chapters 665–669

## Plot

Jin Taekyung remains imprisoned beneath the Nanman Beast Palace, bound by iron balls and a Force-Sealing Pill, while Taishan is held in the cell above him. The System issues the **Escape from Namshank** Quest, requiring Jin to escape before his execution in two days. Encouraged by Taishan’s loyalty, Jin discovers that the Middle Dantian responds to Will rather than internal energy.

The Beast Miao King confronts Baeksang over Jin’s execution and urges him to oppose the Demonic Cult and Dark Heaven instead of destroying Nanman over past betrayals. He offers to surrender the position of Palace Lord if Baeksang allows rescuers to enter. Baeksang cannot stop him, and Yayul Mok and the Seven Miao Tigers infiltrate the underground prison disguised as Bai warriors. Their rescue attempt is discovered at the fourth-floor checkpoint, forcing them to fight through more than fifty guards without killing fellow Nanman people.

Jin breaks free and defeats the Bai captain and several Peak-level squad captains using the mysterious force of his Middle Dantian. With Taishan’s hunger-driven rampage, the remaining guards surrender and are confined rather than killed. Yayul Mok opens the prison and reveals that Namho and the unconscious Sama Pyo have been rescued from the Inner Palace. Jin completes the Quest, receives a Level Up and partial recovery, gives antidote pills to Taishan and Sama Pyo, and accepts the spiritual creature Muyaho from Yayul Mok.

Jin heads northeast toward the reconnaissance squad with Taishan, Namho, Sama Pyo, and Muyaho. Yayul Mok and the Seven Miao Tigers remain behind to delay pursuit, while Wonhu entrusts the collapsed Young Palace Lord to Jin. The rescue exposes Baeksang’s defiance of the Beast Miao King and leaves the execution order and Tribal Grand Council’s response unresolved.

## Continuity

- Jin has escaped the underground prison and completed the **Escape from Namshank** Quest before the scheduled execution.
- The Quest Reward granted Jin a Level Up, removed some injuries and Status Effects, and released the force constricting his Lower Dantian.
- Jin can use an incompletely understood Middle Dantian force despite the former seal on his internal energy; its source and limits remain unresolved.
- Taishan, Yayul Mok, and the Seven Miao Tigers enabled the escape. The surrendered Bai warriors survived and were confined.
- Namho and Sama Pyo were rescued from the Inner Palace. Sama Pyo received an antidote but remains unable to fight at full strength.
- Yayul Mok gave Muyaho to Jin and directed him northeast toward the reconnaissance squad.
- Yayul Mok and the Seven Miao Tigers remain behind to delay discovery and pursuit; Yayul Mok collapsed as Wonhu caught him.
- Wonhu entrusted the collapsed Young Palace Lord to Jin’s care.
- Baeksang and the Tribal Grand Council must respond to Jin’s escape and the defiance of the execution order.
- Jin, Taishan, Namho, Sama Pyo, Muyaho, and the Young Palace Lord still need to reach the reconnaissance squad and escape Nanman.
- The survival of Yayul Mok and the Seven Miao Tigers remains uncertain.

## Translation Decisions

- Use **Escape from Namshank** for 남생크.
- Use **Great Chieftain** for 대족장, **Deputy Stronghold Lord** for 부채주, and **Stronghold Lord** for 채주.
- Retain **underground prison**, **Dizziness Acupoint**, **Middle Dantian**, **Lower Dantian**, and **Will**.
- Use **Seizing an Object Through Empty Space** for 허공섭물, while keeping Jin’s Middle Dantian ability explicitly distinct from it.
- Use **half a shichen** for 반 시진 and **antidote** for 해약.
- Preserve the established food names and the informal comic references to the Hulk, Saiyans, and Kamehameha.
- Use **hyung** for 형 when referring to the Miao speaker’s older brother.

## Durable state

{
  "active_continuity": [
    "Jin has escaped the underground prison and completed the Escape from Namshank Quest before the scheduled execution.",
    "The Quest Reward granted Jin a Level Up, removed some injuries and Status Effects, and released the force constricting his Lower Dantian.",
    "Jin still has not fully understood the insufficient power of his Middle Dantian.",
    "Taishan, Yayul Mok, and the Seven Miao Tigers enabled the escape, while the surrendered Bai warriors survived and were confined.",
    "Namho and Sama Pyo were rescued from the Inner Palace; Sama Pyo received an antidote but cannot yet fight at full strength.",
    "Yayul Mok gave Muyaho to Jin and directed him northeast toward the reconnaissance squad.",
    "Yayul Mok and the Seven Miao Tigers remain behind to delay discovery for as long as possible.",
    "Yayul Mok collapsed as Wonhu caught him and entrusted him to Jin's care.",
    "Baeksang and the Tribal Grand Council's response to the defiance of the execution order remains unresolved."
  ],
  "continuity_sources": [
    669,
    668
  ],
  "open_questions": [
    "Can Jin, Taishan, Namho, Sama Pyo, and Muyaho reach the reconnaissance squad and escape Nanman?",
    "Will Yayul Mok and the Seven Miao Tigers survive after remaining behind to delay pursuit?",
    "What punishment will Baeksang and the Tribal Grand Council impose after the rescue is exposed?",
    "What is the exact source and limit of Jin's Middle Dantian force?",
    "How fully will Jin's restored condition affect his ability to fight and escape?"
  ],
  "safe_through": 669,
  "temporary_decisions": [
    "Use Great Chieftain for 대족장 and Escape from Namshank for 남생크.",
    "Use Deputy Stronghold Lord for 부채주 and Stronghold Lord for 채주.",
    "Use underground prison for 뇌옥 and Dizziness Acupoint for 훈혈.",
    "Capitalize Will for 의지; use Middle Dantian for 중단전 and Seizing an Object Through Empty Space for 허공섭물.",
    "Use half a shichen for 반 시진, Lower Dantian for 하단전, and antidote for 해약."
  ],
  "version": 1
}

## Reading copies

## Chapter artifact 665

# Chapter 665

Tap. Drip.

The quiet sound of water droplets echoed softly through the silence. I sidestepped the liquid falling from the cracked ceiling of the underground prison and looked up into the air.

> **System**
>
> **Quest**
>
> **Escape from Namshank**
>
> You have ended up imprisoned in the underground prison of the Nanman Beast Palace after all. Dark, damp, and silent, this place resembles the future that awaits you. But it is still too soon to give up on life.
>
> **Time remaining until execution:** Two days
>
> You must escape the underground prison within the allotted time limit.
>
> Whether you survive alone or survive together is entirely up to you. If you fail, only death awaits.
>
> But remember this. As long as you possess a strong Will and even a single thread of goodwill, a path to life will open.
>
> **Grade:** Supreme Peak
>
> **Restriction:** Jin Taekyung
>
> **Mission:** Escape the underground prison before the execution (Incomplete)
>
> **Reward:** Linked Quest
>
> ???
>
> **Failure:** Death

I had already checked the Quest window countless times.

I stared at the translucent holographic window as if I could bore a hole through it, but no miracle occurred that changed the words written on the final line.

*Failure: Death.*

This was not the first time.

From the moment I first set foot in the Murim until now, I had received this kind of goddamn Quest several times. Of course, in the beginning, I had been utterly dumbfounded.

*Back then, I really thought I was going to die a dog’s death.*

I had fought countless battles while working as a Hunter, but death had always frightened me.

More precisely, it would be more accurate to say that I was afraid of everything I would have to leave behind, rather than death itself.

At least if I died in a Gate, my family would receive some kind of death benefit. If I died in the Murim, there would be nothing.

Of course, there was an unbridgeable gap between the me of those days and the me I was now.

With every crisis, my guts were forcibly injected with Botox and grew bigger by the day, while my body and mind toughened in proportion.

But…

*I’ve never been in a situation like this before.*

The reason I had managed to survive every time I stood at the crossroads between life and death was simple.

There had always been someone beside me who would fight alongside me, and whenever I had to face something alone, I had been ready to fight with my life on the line.

And after struggling and thrashing until the very end, I had survived.

Clatter.

At the very least, I had never been in a situation where I had enormous iron balls hanging all over my body while my internal energy was sealed.

“……Damn it.”

I muttered under my breath and closed my eyes. The text written in the Quest description seemed to rise clearly in the darkness.

> **As long as you possess a strong Will and even a single thread of goodwill, a path to life will open.**

The System occasionally sent me messages that I could not tell were hints or complete nonsense.

In that sense, was this merely a word of encouragement? Or was it a decisive clue telling me how to escape the underground prison?

Just as I was deep in thought with my eyes closed, the liquid falling from above struck the floor and splashed onto the back of my hand.

Tap. Splatter.

It was too sticky to be groundwater, and its temperature was warm enough to make me feel grimy.

I opened my eyes at once, but without even looking at the ceiling, I spoke.

“……You crazy bastard. I told you not to drool so much.”

Along with the sound of someone swallowing saliva—*slurp*—Taishan’s voice rang out.

“Sorry. Taishan did that because Taishan too hungry.”

“Then why is someone who’s hungry pressing his mouth against a hole in the floor? Just sit there quietly.”

“But if Taishan keeps licking, it’s surprisingly salty.”

“Licking? Licking what?”

“Rock. This place is a rock restaurant.”

“Oh, for crying out loud.”

“Crying out loud? Is that some kind of seasoning?”

*This crazy bastard……*

I swallowed the curse that had risen to my throat. Getting angry at him now would only drain my energy. It would not change anything.

Besides, Taishan’s situation was not very good, either.

I had no idea what kind of creature he was, but his vital points were so thick that the Pressure-Point Strike had not worked. Even so, his internal energy had been sealed, and his entire body was bound.

No matter how naturally strong Taishan was, there was no answer to be found in a situation like this.

“Pavilion Master. Taishan hungry. Taishan wants to get out soon.”

As I listened to his quiet whining echo through the prison, a thought suddenly occurred to me.

A thought that could be called guilt.

*All of this is my fault.*

“……Hey, Taishan.”

“Pavilion Master called Taishan?”

“I’m sorry.”

“Huh?”

“I’m sorry. I mean it.”

As I spoke, I looked up at the ceiling. Through a hole about the size of a child’s fist, I saw one large, clear eye like a calf’s.

It held a look of complete bewilderment.

I had always thought this, but Taishan possessed a pure heart that did not match his age or size. Like a clean, blank sheet of paper.

I opened my mouth with a sigh.

“I should have made a better judgment. But I didn’t. It was my mistake.”

It had been a painful miscalculation. In terms of baduk, it had been a terrible move.

I had locked myself inside the underground prison to clean up the consequences of that mistake, but… damn it. I still had doubts about whether it had really been the right choice.

Taishan, who had been staring at me as though I were strange, answered.

“Taishan okay.”

“You’re okay?”

“Mm-hmm. Taishan really okay.”

“…….”

I closed my mouth and lowered my head. Taishan probably did not even understand how the current situation was unfolding.

The most important fact to him right now was that he was hungry. The second most important fact was probably that there was no way for him to solve that hunger.

*Yeah. Maybe that’s better for him.*

But the next moment, when I heard what he said afterward, I realized something.

Taishan was far cleverer than I had thought.

“Pavilion Master doesn’t need to be sorry to Taishan.”

“……?”

Startled, I raised my head and looked at the ceiling. Taishan met my gaze and continued in a clear voice.

“Taishan knows. Taishan is stupid.”

“What?”

“Since Taishan was very young, people teased Taishan and called him stupid. Whenever they were bored, they came and hit Taishan. If Taishan hadn’t met Lord…… Taishan might still be getting hit and crying every day. Taishan had a very hard time.”

His mood and manner of speaking were completely different from usual. I widened my eyes at this unfamiliar side of Taishan as his voice continued to reach me, smooth as flowing water.

“But Lord was different. Even when Taishan said things wrong, Lord understood everything. When Taishan ate too much, Lord would even pat Taishan on the back and tell Taishan to eat slowly. So Taishan made a promise. Taishan decided to give his life to Lord.”

“You……”

“But a little while ago, Lord said this to Taishan. He said we should trust the Pavilion Master. He said the Pavilion Master seemed different from the other orthodox-faction people. Looking back now, Lord was right. A few days ago, it was the Pavilion Master who saved Lord in stupid Taishan’s place.”

“……!”

“Taishan likes the Fire Dragon Pavilion now. Taishan likes little and cute Namho, Hyuk Mujin, who sometimes bothers Taishan, fierce Song Ilseom, and Ju Hwaran, who is as pretty as a flower. And Taishan likes the Pavilion Master second-most after Lord.”

The eyes looking at me from beyond the hole curved gently.

“Taishan trusts Lord, and Lord trusts the Pavilion Master. So Pavilion Master, trust yourself. The Pavilion Master will definitely find a way. Just like always.”

I only stared blankly for a while as Taishan finished speaking and giggled.

It felt as if someone had struck me in the back of the head with a club.

I had never imagined that Taishan, of all people, would say something like this to me.

Nor had I imagined that his words would become the greatest source of strength I had right now.

*Yeah. When I think about it, there was always a path somewhere.*

In the Murim, I seemed to have lived a life rather close to death.

Jopil. The Head Elder. The Roaring Fury Swordsman and the Blood Lord. The Western Heaven Demon Lord……

Everywhere I went, a crisis had been waiting for me. And each time, I had taken out the word *death* hidden inside my heart, toyed with it, and made a vow.

I would never die. I could never die here.

*A strong Will.*

Was this what part of the Quest window had meant?

Or was it…

*Something else that ran parallel to a strong Will.*

That was when it happened.

A certain thing the Slaughter Saint had said to me in Hubei just a few months ago flashed through my mind like lightning.

> “Huh. You monstrous bastard. You finally opened your Middle Dantian, so you can handle your qi properly now.”

And I had answered him like this.

> “I already know how to handle it. Don’t you know how much internal energy I have?”

The Slaughter Saint had merely let out a short laugh without answering. Then he had shaken his head and disappeared.

Along with a single remark that there was no point in explaining it to me now, because I would not understand.

But now, I thought I was beginning to understand.

Why the Slaughter Saint had spoken and acted that way back then.

How ridiculous the young fool must have seemed in his eyes—a brat bragging that he knew how to handle qi simply because he possessed several jiazi of internal energy.

*The Three Dantians.*

The three greatest and most important passages in the human body.

But the Lower Dantian was merely a vessel that continued to fill with and empty out internal energy.

Until now, I had not understood even a quarter of the function and mysteries of the Middle Dantian.

But now I was different.

No. I understood a little.

What moved the Middle Dantian was not internal energy.

It was Will.

*An unwavering, powerful Will.*

The Middle Dantian had never been a matter of internal energy in the first place. It belonged to the realm of enlightenment.

Somewhere in an unknown domain that stood half a step beyond even the land of the chosen—those who were no longer governed by the size of their internal energy.

A sacred realm that every human had to pass through to rise from being born a human toward the realm of the gods.

Since martial arts first came into existence in this world, countless powerful figures must have experienced their own failures and successes along this path.

They either crumbled like dry leaves, or became giants who left their footprints in this distant history of martial arts.

And today, I had…

Taken half a step closer to those giants.

Whoosh.

Following the fingertips I extended as if entranced, the qi of the world hidden within the air rippled.

* * *

Baeksang realized that an uninvited guest had arrived before him just as he was about to enter his quarters.

*This is……*

It was faint but unmistakably familiar qi, something it would have been stranger for Baeksang not to recognize.

Perhaps the uninvited guest waiting for him had been hoping for exactly that.

“You may all return now.”

The guards who had been about to open the door ahead of him stopped at Baeksang’s words. The graying Captain of the Guards, who had served at his side for some thirty years, spoke.

“My lord. Even so…”

“That is enough. Just guard the surroundings well.”

After staring at Baeksang for a moment at his cold words, the captain scattered throughout the manor with his subordinates.

Baeksang glanced at them, then gripped the door handle firmly and pushed.

Sss.

It was already dark outside, but the interior of the quarters was brightly lit.

As befitted the residence of a great chieftain, it was spacious. Yet despite its size, it was almost painfully sparse.

One person was waiting for Baeksang inside.

“You’re late. Where have you been?”

Baeksang answered calmly.

“You already know, don’t you, Palace Lord?”

A bitter smile formed at the lips of the uninvited guest, the Beast Miao King.
## Chapter artifact 666

# Chapter 666

Despite the Beast Miao King’s sudden appearance as an unexpected guest, Baeksang’s voice remained calm.

“You already know, don’t you, Palace Lord?”

The Beast Miao King smiled bitterly.

Baeksang’s words were true. Although a considerable number of tribal chieftains had turned against him, he was still the master of the Nanman Beast Palace.

At least within the Inner Palace, he knew Baeksang’s every movement.

“You spent quite a long time in the underground prison. What did you talk about with that boy for so long?”

“……”

Remembering his conversation with Jin Taekyung, Baeksang involuntarily hesitated. But his hesitation was brief.

“I told him that he would be executed at noon two days from now, in front of everyone.”

“And?”

“I also told him that no one could stop it.”

At the precisely aimed remark, the Beast Miao King’s eyes grew dark.

“Do you truly believe that?”

“Of course.”

“And if I refuse to let that happen?”

“The Palace Lord is merely the one standing at the forefront. The authority to decide Nanman’s great affairs belongs solely to the Tribal Grand Council.”

Baeksang recited the words in a low voice, then continued.

“Have you forgotten? The oath our ancestors made hundreds of years ago, when they gathered beneath a single banner on this land.”

“……!”

“The result will not change. Tomorrow, the agenda of the final Tribal Grand Council will be the execution of the Han Chinese Jin Taekyung.”

The Beast Miao King stared at Baeksang with heavy eyes. He knew as well as anyone that the scales of power had already tipped.

But if he had given up on Jin Taekyung, he would never have come here.

“Is that all?”

“Twenty tribal chieftains, including myself, have already united behind this decision. If you abandon the will of the Tribal Grand Council and choose another path…”

“That is not what I am asking.”

The Beast Miao King cut off Baeksang’s words and continued with a sigh.

“Did you not tell Jin Taekyung, that boy, about Hwi?”

“……!”

A crack appeared in Baeksang’s unshaken expression. It had been the same in the past, and it was the same now.

The only person who could shake a man who had lived behind an iron mask for several decades was the child he could no longer keep by his side.

And the Beast Miao King knew that better than anyone.

“I did not plant someone in the underground prison. I merely guessed. Seeing you shaken unlike your usual self confirmed it.”

“How…”

“How could I not know? We have spent our entire lives together.”

Baeksang closed his mouth. The single word *we* struck him with unusual force. A word that had once come naturally to both of them, but had now become unfamiliar.

But then…

Grind.

“That was when the Palace Lord and I stood on the same path.”

The Beast Miao King shook his head.

“It is the same now. We have never parted ways even once.”

“It is already too late.”

“It is not too late. We are still sworn brothers bound together in our hearts. We can turn back the wrongs of the past even now.”

“To me, they are nothing more than ties from a distant past.”

“Then you have been shackled to that past all this time, little brother.”

“……!”

“I remember that day too. How could I forget the day that child, who was more upright and radiant than anyone, disappeared from this land?”

Baeksang clenched his teeth. Merely recalling that day was agonizing.

At the same time, he knew that when all the truth surrounding that day had come to light, someone else had been as furious and grief-stricken as he was.

But it had all been in vain.

“Both the Palace Lord and I were powerless. The evidence proving their crimes had vanished, and everything was buried beneath the peace that came afterward.”

The countless footprints left in a sandy shore were bound to disappear beneath the waves that rolled in afterward.

But Baeksang remembered. He had carved the faces of those who had turned away from his child in danger into his flesh and bones, then chewed over them in his heart.

Baeksang had believed they were all walking side by side across the vast sandy shore called the Central Plains. But in truth, his people had merely been sent to the front because they were foreigners.

“I cannot forget any of it, nor can I turn it back. So why are you…!”

Baeksang, who had been about to raise his voice, suddenly stopped.

He had seen the sorrow clouding the Beast Miao King’s face.

“Do you think I forgot? This useless father, who had no choice but to send his children on ahead?”

More than fifty years ago.

The Beast Miao King’s children had been among the ten thousand warriors who headed for the Central Plains, and they never set foot on Nanman soil alive again.

“I still regret it. I wonder what would have happened if I had not become the Palace Lord of the Nanman Beast Palace, if I had not gone to the battlefield. What if I had at least rejected those children’s request to fight alongside their father?”

“……”

“Your words are right, little brother. We were powerless. We were consumed by fury and howled with grief, but there was nothing we could do. Yet we had to return to Nanman. Everyone was exhausted. We could not push away the peace that had come after ten years and begin another war.”

The Beast Miao King let out a hollow laugh. At the time, the gap between Nanman, which was merely one of the powers of the Outer Lands, and the Central Plains had been overwhelming.

No—even compared with the Zhongnan Sect alone, Nanman had been at a relative disadvantage.

Venerable Wusang, who had been the Sect Leader at the time, was respected by many for his bearing as a Great Hero. When that man lost his life in the final battle at Great Snow Mountain, countless sects and martial artists came to Mount Zhongnan.

“I merely made a choice. Between the dead and the living, between revenge and the greater cause.”

Everything that happened afterward was known to everyone.

The Beast Miao King led the survivors back to Nanman, where he faced the countless accusations poured out by those who had lost their families.

“My life was filled with regrets. But I never regretted that choice—not even once. Because we united as one, grew stronger and more prosperous than before, and gained the power to hold the criminals of the past to account.”

Baeksang’s face hardened at the story he had never heard before. Yet at the same time, an emotion he could not understand was mixed into his gaze as he looked at the Beast Miao King.

“But you will side with the Central Plains again this time.”

The Beast Miao King answered without a moment’s hesitation.

“Yes. I will.”

“Why in the world…”

“Just because one tree is diseased, burning down the entire forest would be foolish.”

“……!”

“What must be uprooted is the cause that made the tree diseased. If we recklessly burn the forest, the next place those flames will reach is us.”

The Beast Miao King continued as though lamenting.

“That was what the Demonic Cult did in the past, and what Dark Heaven is doing now. We fought to protect the forest. This land is part of that forest too.”

Neither the people of the Central Plains nor the people of Nanman acknowledged it, but the Beast Miao King knew.

Though they lived far apart, they shared the forest called the world.

And…

“You know that too, Baeksang.”

The person who understood it best was his sworn younger brother—the man now looking at him with shaken eyes.

“I know. I know that no matter what this foolish older brother says, none of it will reach your ears. You will say that it is an old affair you no longer even remember, and that the Baeksang of that time died a long time ago.”

The Beast Miao King’s children had been killed by the Demonic Cult, but Baeksang’s only child had been sacrificed because people he had believed were allies turned their backs on him.

The scale and depth of their anger toward the Central Plains could not possibly be the same.

But the Beast Miao King had watched Baeksang for a long time. He had already guessed.

“If you do not stop walking down this path… you will regret it. You will regret it as you did in the past, as you do now, and as you will in the future.”

Baeksang wanted to answer.

*I will not regret it.*

For Hwi, the child who was no different from his entire world, he could do anything.

While alive, he was willing to be called a vengeance fiend. Even in death, he would gladly smile and walk this path if people called him a Fiend.

*Then why…*

Why? Why in the world?

Why would the thought he had repeated hundreds and thousands of times in his heart over the years refuse to pass through his lips at this very moment?

Even though he had already walked down a path from which he could never return, why?

*Why are you doing this, Baeksang?*

And at the moment Baeksang asked that question, unable to answer it within his hollow heart, the Beast Miao King’s quiet voice pierced his ears.

“I can step down from the position of Palace Lord.”

Baeksang’s pupils shook at the unexpected words. But the Beast Miao King continued in a calmer voice than ever.

“You did not hear me wrong. If you want it, I will give up the position of Palace Lord right now.”

Baeksang was confused. If the position of Palace Lord became vacant, one of the remaining great chieftains would become the new Palace Lord through the Tribal Grand Council.

But with Heugung and Yohi, the two great chieftains, gone, the meaning of the Beast Miao King’s proposal was obvious.

“You would appoint me, of all people, as the new Palace Lord?”

“Yes. You heard me correctly.”

“Palace Lord. Have you gone mad?”

“Could that be possible?”

The Nanman Beast Palace was truly governed by thirty-two tribal chieftains, but the authority carried by the name of Palace Lord could not be ignored.

And yet, in a situation like this, he was making such an absurd proposal.

“What in the world is this…”

Baeksang stared at the Beast Miao King in incomprehension, then suddenly closed his mouth.

For a moment, he had realized something from the man’s unusually calm, almost detached manner.

*No way.*

A thought flashed through his mind like a streak of lightning.

At the same time, the Beast Miao King slowly opened his mouth.

“Half a shichen. Half a shichen will be enough. Open a path for them.”

The amount of time called half a shichen, and the two words *for them*.

That alone was enough to turn his guess into certainty.

Baeksang asked in a voice boiling with emotion.

“Why in the world? What reason could you possibly have to go this far?”

The Beast Miao King’s answer came without the slightest tremor or hesitation.

“Because they came to help us. Just as we once did.”

“……!”

“And I will help you. As I always have.”

*It is already too late for that.*

Baeksang muttered the words inwardly as though spitting them out, then called for the Captain of the Guards waiting outside.

Or tried to.

For some reason, neither his feet nor his lips would move.

Baeksang slowly closed his eyes. The voice he should have let go long ago still lingered in his ears.

*How much more blood do you intend to spill, Baeksang?*

* * *

The figures moving through the darkness were quiet and stealthy.

Sssshh!

The figures shot toward a single destination at blinding speed, splitting the wind and shaking the leaves.

And by the time someone noticed what was happening, everything was already too late.

Sssht—thud!

A body stiffened and fell. One of the figures caught the torch from his hand and moved his lips.

“Open the underground prison.”

Fwoosh.

Above the wavering torch flame, Yayul Mok’s face appeared.
## Chapter artifact 667

# Chapter 667

Infiltration. Assault. Cleanup.

The sequence of events could only be described as a Quick Attack. It lasted no more than a few moments, and the twenty warriors guarding the area around the underground prison collapsed helplessly before the unexpected ambush.

“I-I—intruders…!”

Sssht—thud!

The urgent voice that burst from someone’s lips died out before it could become a shout.

Moving with the speed of a streak of light, Yayul Mok struck the Mute Acupoint and Dizziness Acupoint one after another. Then he caught the collapsing Bai warrior and quietly lowered him onto the ground.

Sss.

It had truly been a close call. The entire operation had nearly gone badly.

“Whew.”

Yayul Mok exhaled the breath he had been holding and swiftly scanned his surroundings.

Around twenty black-clad figures, each wearing a different mask, kept watch in every direction while hiding those whose pressure points had been sealed among the grass.

—Report.

—Everyone has been subdued.

A man wearing a monkey mask answered Yayul Mok through Sound Transmission.

The fact that he and six of the other men in black were the Seven Miao Tigers, the most outstanding warriors among the Miao people, was a secret known only to them and the Beast Miao King.

—I thought one person was missing. But after counting the numbers, the last one was the man the Young Palace Lord subdued a moment ago. He must have gone nearby to relieve himself.

—Any casualties on our side?

—None.

—Good. We nearly ruined everything before we even began.

—It would have caused quite a problem.

In truth, considering what they were doing, even calling it a problem was an understatement.

On the surface, Jin Taekyung was a criminal imprisoned in the underground prison after committing an unforgivable felony.

If it became known that they had tried to help him escape, even Yayul Mok, the Young Palace Lord of the Nanman Beast Palace, would not escape unscathed.

*But we have to do it.*

Yayul Mok wiped the cold sweat from his forehead and muttered inwardly.

He was still young, but he understood how audacious—and dangerous—this was.

At the same time, he believed it was right.

*Jin Taekyung is an ally. He came here to help us, and he even rescued warriors who were in danger on Ailao Mountain.*

Like any Nanman native, Yayul Mok had disliked the Han Chinese from a young age.

At least, he had until he met Jin Taekyung and the members of the Fire Dragon Pavilion.

Of course, thinking well of Jin Taekyung did not mean he trusted all the Han Chinese. An individual was an individual, and a group was a group.

But in a situation like this, he was certain of what was right and wrong.

Just like his own father, the Beast Miao King, whom he respected beyond measure.

—Did you secure the keys to open the underground prison?

—Of course.

The man in the monkey mask nodded and handed over the bundle of keys in his hand.

To enter the underground prison, five keys had to be inserted in the correct order without a single mistake to activate the mechanism. They already knew how to do it.

Click. Groooan.

A massive iron door moved with a heavy rumble.

At last, when the staircase leading underground was revealed, everyone—including Yayul Mok and the Seven Miao Tigers—quickly turned their clothes inside out.

Sssht. Flutter.

Torchlight swaying in the wind illuminated their pure-white clothes. In an instant, they had transformed into Bai warriors, and they stood guard around the underground prison as though nothing had happened.

They would guard this place for at least half an hour, until the next shift arrived.

*All we can do is hope nothing happens in the meantime.*

Even though they had studied every route and position in advance, no one knew how things would unfold.

Muttering quietly to himself, Yayul Mok descended underground with the Seven Miao Tigers, wearing the white uniform that felt especially unfamiliar today.

*Jin Taekyung is on the fourth floor.*

He already knew the location. He also knew that some of the wardens and guards were stationed inside the underground prison.

Just as they moved with even their footsteps suppressed as much as possible, faint voices began to reach them from far away.

“Damn it. Did you cheat somehow?”

“Don’t talk such ridiculous nonsense. Just humbly admit defeat.”

“Shit. I’m only saying this because I don’t understand. How can someone lose five games in a row? I’ve already lost two nyang.”

It was common for wardens to gamble to pass the time, and their carelessness was welcome news for the infiltrators.

“Damn it. Turn your palm over.”

“Good grief. What a sore loser. Stop feeling wronged and lower your voice. The higher-ups are already on edge because of that Han Chinese bastard. If they find out we’ve been slacking off…”

Sssht—thud!

The voices coming from the hazy darkness abruptly stopped.

The Seven Miao Tigers were warriors counted among the very best of the Miao people, and even the Central Plains recognized them as Peak masters.

The wardens failed to notice their silent approach. After being subdued in an instant, they were stripped of their keys and locked inside an empty cell.

—Gisan. Dogok. Stay here.

—Yes, sir.

—We won’t let even a single ant slip through.

Leaving the post unattended would naturally arouse suspicion.

Yayul Mok left two of the Seven Miao Tigers behind and increased his pace. Faster than an ordinary walk, but not so fast as to invite suspicion.

Step. Step.

Six figures crossed the underground prison, which twisted like a massive maze.

But contrary to Yayul Mok’s hopes, not everything could go according to plan.

“Hmm? Who are those men?”

The security on the fourth floor, where Jin Taekyung was imprisoned, was incomparably tighter than usual. In addition to the wardens, there were quite a few warriors guarding the interior of the underground prison.

“You there. Stop.”

Yayul Mok obediently halted and counted the men blocking their path while steadying his breathing.

*Twenty in total.*

Five of them were even Peak masters.

Realizing that his opponents were elite Bai warriors, Yayul Mok answered in a calm voice.

The mask Yayul Mok had been wearing was already off, and with only a few torches burning, the dim underground prison was ideal for concealing his identity.

“We came at the command of the Great Chieftain.”

“The Great Chieftain?”

The Bai warrior who appeared to be their captain deliberately furrowed his brow.

“He only left a short while ago. What is this about?”

“It is nothing particularly important. He told us to make the criminal take another Force-Sealing Pill, just in case.”

“Hm. Is that so?”

“He must be worried about an escape attempt. I have only heard rumors myself, but apparently the man is a monster.”

The Bai warrior let out a short laugh at Yayul Mok’s answer.

“That is what I’ve heard. But now he is merely a man waiting for the day he dies.”

“I think so as well, but no one knows how things will turn out in this world, do they?”

“Well, that is true. In any case, judging by your voice, you seem young. If you are not here to take over our shift, hurry along. I’ll give you a quarter of an hour.”

“That was our intention.”

Yayul Mok casually shrugged and approached them with his head slightly lowered so they would not see his face.

And then he saw the hand of one of the warriors gripping his scabbard tightly.

*They already noticed us…!*

Shing! Slice!

At the same instant he realized it, a flash of light grazed his shoulder.

A few drops of blood sprang into the air along with a faint sting. Yayul Mok twisted his body and evaded two swords. Then an explosive shout shook the entire underground prison.

“Intruders! We have intruders!”

Peeeeep!

A sharp whistle burst out alongside the shout. The urgent footsteps of warriors waiting throughout the underground prison shattered the silence.

Feeling countless presences, Yayul Mok clenched his teeth and shouted.

“Attack!”

At the same time—

Sssshh-shing!

Brilliant sword light poured down from behind Yayul Mok. Weapons tangled dangerously beneath the dim torchlight.

Clang! Clang-clang!

Slice!

“Gah!”

Around ten weapons collided in an instant, followed by bursts of blood and screams.

Soon, the two men they had disguised as wardens realized how dire the situation was and joined the battle. In the space of a few moments, half of the nearly twenty Bai warriors had been wounded and knocked down.

But…

Peep! Peeeeep!

“Stop them by any means necessary! Their target is Jin Taekyung!”

“There aren’t many of them! Capture them if possible!”

The security was far tighter than the information they had obtained suggested.

Whenever one man fell, five more appeared. Whenever five were knocked down, ten took their place.

What was more, Yayul Mok and his men had sworn not to kill fellow Nanman people while rescuing Jin Taekyung. For them, it was one impossible hurdle after another.

Sssshh-shing!

“Keep pressing forward!”

Bai warriors charged in from every direction, their weapons sharpened to deadly points.

Yayul Mok and the Seven Miao Tigers were surrounded by more than fifty enemies in an instant, but they gritted their teeth and fought back.

Clang-clang-clang!

Slice!

But the difference between their hopes and reality was obvious.

The enemies continued to pour in without end, bringing the four characters *the many defeat the few* to mind. And the attacks launched by the Peak masters mixed among them were terrifyingly dangerous.

Sssht—thunk!

“Ugh!”

Small wounds continued to accumulate, and the bleeding continued.

Yayul Mok and the Seven Miao Tigers had knocked down no small number of Bai warriors, but even now, the enemy’s numbers kept growing.

At last, the guards stationed on the other floors had joined the fight as well.

*Damn it.*

By then, Yayul Mok’s back was damp with cold sweat.

He had already known that things would not go as smoothly as he hoped. But they had been discovered far too early, and the security around the underground prison was much tighter than the information he had received indicated.

*If we get captured here…*

Then the entire situation would spiral into the worst possible outcome.

As the Young Palace Lord of the Nanman Beast Palace, Yayul Mok would not lose his life. But his father, the Beast Miao King, would lose his political standing, while Jin Taekyung and the Fire Dragon Pavilion members—the original targets of the rescue—would be sent to the execution ground.

*And war will begin.*

Not the Great Faction War in which they had once fought against the Demonic Cult, but a war against the Murim of the Central Plains.

If Jin Taekyung died, nothing could be undone after that.

And that was one of the greatest reasons the father and son were risking their lives to rescue him.

*There’s no other choice.*

Yayul Mok bit his lips until they bled and moved them.

—Wonhu. I’m counting on you.

It was a short message through Sound Transmission, but it was enough.

The middle-aged man wearing the monkey mask—the eldest brother of the Seven Miao Tigers—scattered his sword strikes and shouted.

“Open a path!”

Now that things had come to this, there was only one answer.

A breakthrough that disregarded their lives. And Jin Taekyung’s rescue.

That was why everyone here had come despite the danger, and the only way Yayul Mok could think of to overcome this situation.

*Jin Taekyung. If he gets out of the underground prison, everything can be resolved.*

Yayul Mok felt the solid wooden case inside his robes.

The claim he had made just before the battle broke out—that he had come to give Jin Taekyung a Force-Sealing Pill—had not been entirely false.

It was simply not a Force-Sealing Pill. It was an antidote that would release the seal on his internal energy.

Clang-clang-clang!

Thrust! Slice!

“Gah!”

The fact that the underground prison’s corridors were narrow was their only advantage in their increasingly desperate situation.

Ignoring the attacks pouring in from every direction, Yayul Mok and the Seven Miao Tigers forced their way toward a single point. At last, a dark corridor appeared before them.

“Go! Hurry!”

Leaving behind the urgent cry of their loyal retainer, Yayul Mok drew up every ounce of his strength and launched himself forward.

Or he tried to.

Sssshh-shing! Grab!

The next moment, someone’s hand reached out of the darkness and caught him by the shoulder.

Without that, he would have.

“Where are you going? Got somewhere to be?”

“……!”

For a brief moment, Yayul Mok fell silent, ignoring everything happening around him. Then he opened his mouth.

“…Why are you coming out of there?”
## Chapter artifact 668

# Chapter 668

Sometimes, inexplicable things happen in life.

Just like now.

“Where are you going? Got somewhere to be?”

“……!”

For the briefest moment, time seemed to stop in the middle of its steep descent.

The Seven Miao Tigers, who had been rampaging like beasts despite wounds all over their bodies; the Bai warriors, who now filled the underground prison’s corridors; and Yayul Mok—all stood frozen like statues, staring blankly at the person who had emerged from beyond the thick darkness.

*How?*

The question that filled everyone’s mind at that moment was only natural.

Because *he* was someone who could not—and should not—have appeared here.

But while everyone inside the underground prison wore the expression of someone who had seen a ghost, only Yayul Mok, whose shoulder was caught in *his* powerful grip, realized that this unbelievable situation was real.

At the same time, he could not help asking.

“…Why are you coming out of there?”

Yayul Mok’s eyes were vacant, and his voice was dazed. But the answer he received was unbelievably short and simple.

“I just came out.”

“……?”

“I was trapped in here, right? So I came out through here.”

“……!”

*What the fuck is he talking about?*

Yayul Mok and everyone else thought the same thing, left speechless.

*So what the hell? We’re asking how the bastard who was supposed to be locked in the underground prison crawled out.*

He had not merely been sitting quietly in confinement, either. They had said that he had been forced to drag around iron balls weighing more than ten thousand geun like accessories, with his internal energy sealed as well.

And that was not all. The iron bars blocking the prison on every side had even been made with meteorite iron mixed into them.

It was a prison built for one monster alone.

*But how?*

It was a realm of incomprehensibility that no one could possibly understand.

Faced with this unbelievable sight, the Bai warriors instinctively thought of betrayal by an insider. Yayul Mok and the Seven Miao Tigers wondered whether the information they had obtained had been wrong. And *he* casually took a step forward.

Step.

The sound of his footsteps shattered the silence.

At last, the man who had been submerged in darkness—or rather, Jin Taekyung—walked beneath the flickering torchlight and frowned.

“Ugh, that’s bright. Hey, you over there.”

At Jin Taekyung’s pointed finger, the Bai warrior holding his torch high asked with a vacant expression,

“Me?”

“Yeah, you.”

“Wh-why?”

“Why do you think, you clueless bastard? My eyes hurt, so lower your arm. What are you doing, giving a presentation? Crossing a crosswalk without your parents?”

“No, sir.”

The Bai warrior answered with a blank face, even though he could not understand what Jin Taekyung was saying.

Somehow, it felt as though he was supposed to answer that way. Using polite speech also felt perfectly natural.

“This bastard’s still crossing on a green light. I’ll give you three seconds to lower your arm. When it turns red, you’re dead. Three.”

“Ah, I’m sorry.”

“To hell with sorry. Just lower your arm already. Two.”

“Yes, sir.”

Whoosh!

The Bai warrior hurriedly lowered his arm. The already faint torchlight grew even dimmer, and only then did Jin Taekyung nod with a satisfied expression.

“Hmm. Much better. Good job.”

“It was nothing……”

The Bai warrior, who had felt a strange sense of pride at Jin Taekyung’s praise, suddenly froze.

*Huh?*

What? This wasn’t right.

And just as the realization struck him, a mysterious sound of splitting air pierced his ears.

Thwack! Thud.

Sizzle.

The warrior’s body crumpled helplessly, and the torch fell into a puddle.

The captain of the Bai warriors, who had struck his stupid subordinate across the jaw without hesitation, growled.

“You useless fool.”

At that icy voice, the Bai warriors who had merely stood there watching the scene unfold as smoothly as flowing water suddenly came to their senses.

*What is this?*

It felt as though they had awakened from a deep sleep. At the same time, they suddenly realized the truth.

This situation they had found themselves in was unbelievably real.

And the battle was not over yet.

And…

“Now he’s even putting out the fire for us. How considerate.”

They had to subdue that monster who had somehow freed himself from his restraints.

The realization flashed through their minds as quickly as lightning, and the cry that followed was like thunder.

“Attack!”

The shout, filled with powerful internal energy, shook the underground prison.

At the same time as he ordered the attack, the captain of the Bai warriors was the first to leap forward. He kicked off the wall and shot toward Jin Taekyung.

Tap-tap—whoosh!

His movement was so fast that it rivaled a Peak master from one of the major sects.

The Seven Miao Tigers, who had come to their senses half a beat late, tried to block him, but weapons charging in from every direction got in their way.

Swish-swish-swish—clang!

Wonhu, the eldest of the Seven Miao Tigers, blocked the incoming attacks and shouted.

“Quickly, give him the antidote…!”

Clang!

His shout was cut off before he could finish.

Seeing Yayul Mok hurriedly reach inside his robes for something, the captain was certain.

*As I thought. Not yet.*

Jin Taekyung.

He did not know how that young monster from the Central Plains had escaped the underground prison, but there was no doubt that the boy had not yet released the seal on his internal energy.

If so…

*It can be done.*

No matter how powerful a Supreme Peak master was, if he could not use his internal energy, he was nothing more than an exceptionally capable commoner.

Of course, the martial arts he had learned and the martial principles he had realized had not vanished in an instant. But with no weapon in hand, facing someone who had reached the Peak realm long ago while fighting bare-handed was nearly impossible.

*I will capture him with my own hands.*

The desire to make a great achievement that no one else could approach, along with his confidence that he could win, made the captain’s body and mind lighter than ever.

At the same time, the sword in his hand began to emit a dazzling halo of light.

Ssssss!

Sword Energy surged along the sharp blade.

The captain instinctively looked back and saw Yayul Mok’s pupils tremble.

He was certain.

This strike would become the sharpest and most powerful move of his entire life.

*Now!*

Ssshhhiiing!

An utterly flawless flow.

A perfect draw.

The Sword Energy released from the blade sliced through the darkness and rushed toward the two men, and the captain let out a cry of joy.

“It’s done—!”

Slice!

At least, that was true until his Sword Energy cut through the air.

*What?*

The captain blinked at the incomprehensible sight.

They were gone.

Nothing remained where his Sword Energy had swept through.

Not Yayul Mok.

Not Jin Taekyung.

Everything had vanished like an illusion.

*How?*

And then, the next moment.

An answer came to the question that had echoed only inside the captain’s heart.

“Oh. You were just wondering how, weren’t you?”

“……!”

A voice came unexpectedly from behind him.

Feeling goose bumps crawl up his spine, the captain spun around. His sword moved with him, completely ingrained in his body after countless hours of training.

Whoosh!

But the captain’s sword once again cut through the air.

No—that was not quite accurate. It had almost cut through the air.

Grgrgrk.

The tip of the sword trembled ever so slightly. Another question rose in the captain’s emptied mind.

*What… is this?*

His confusion was only natural.

The blade, packed with Sword Energy, had been stopped by a bare palm that held no weapon at all.

*No. He didn’t even stop it with his hand.*

There was barely one inch of space between the trembling blade and the palm.

In that empty air, an invisible force was pushing his sword away.

Slowly.

But powerfully.

With eyes trembling as fiercely as his sword, the captain squeezed out his voice.

“S-Seizing an Object Through Empty Space?”

The carefully polished blade glinted in the darkness.

Beyond it, someone’s white teeth appeared in a faint grin.

“Seizing an Object Through Empty Space? Well, something like that.”

“H-how? Your internal energy was clearly sealed—”

“Something like it. I never said it was the same.”

“What?”

“Don’t try to understand it. You couldn’t even if you tried.”

Jin Taekyung’s words were a cruel truth.

Even if the captain devoted the rest of his life to martial arts, he would never reach the entrance to the Middle Dantian.

That was a realm the captain, who had devoted his entire life to martial arts, could not understand. Unfortunately, Jin Taekyung was not the sort of kind person who would patiently tutor a dunce.

“Get lost.”

“……!”

At the moment the captain’s wide eyes reflected Jin Taekyung’s fist, wrapped tightly in chains—

Bam!

An immense pain he had never experienced before surged through his abdomen and spread across his entire body.

“Guh-heok!”

It was a powerful punch that could only mean Jin Taekyung had recovered his internal energy.

The blow contained monstrous strength and speed that far surpassed human limits. The captain was nothing more than a slightly superior human. He had no chance of enduring it.

Whoosh!

He could feel it.

His body shooting backward with a sharp sound of splitting air.

His consciousness fading amid the overwhelming pain.

*This insane… monster.*

That was his final thought.

The captain’s already unconscious body grazed past the Seven Miao Tigers, who were still fighting desperately, then crashed like a cannonball into the Bai warriors filling the underground prison’s corridor.

Boom! Crack!

“Argh!”

“Wh-what the hell?”

The underground prison became a chaotic mess in an instant.

Soon, the warriors of the Maek people realized the identity of the monster that had crashed into them and stared with their mouths hanging open.

“C-Captain?”

“No, how could…”

The spreading commotion quickly died down.

There was only one person who could have defeated him—the Peak master who held a high position even among the Bai people and was the strongest person gathered here.

“J-Jin Taekyung.”

The name slipped from someone’s lips.

At the same time, countless gazes shot toward one direction.

Splash. Clatter.

One man walked through a puddle of filthy water, the chains whose iron balls had broken off dangling from both hands.

“Yeah, that’s me. Did someone call?”

In complete contrast to the dark atmosphere of the underground prison, the smile around Jin Taekyung’s lips was as bright as sunlight.

Like a beast that had found its prey.

No.

Like a fiend.

“Anyone want to get the shit beaten out of them with a chain? Hands?”

“……!”

“……!”

The Bai warriors froze as a chill swept through their bodies.

But not everyone reacted that way.

“Attack him!”

“We have the numbers! Push them back!”

Swish-swish-swish!

At the shouts, a dozen or so figures charged forward, kicking off the walls.

They were not as strong as the captain, but each squad captain was a Peak master. Once they stepped forward, the Bai warriors regained the courage they had briefly lost.

No.

They almost regained it.

Whoooosh!

A chain flew through the air with a heavy sound of splitting wind.

Bam-bam-bam-bam-bam!

The chain swept through the dozen or so squad captains charging forward, knocking them away all at once.

Boom! Crash-crash-crash!

The underground prison shook with the thunderous impact.

Everyone swallowed hard as they stared at the thick cloud of dust rising into the air.

Then a low voice reached their ears.

“Is it summer already? Why are there so many damn flies…”

“……!”

“……!”

“Anyway. Who’s next? Hands?”

This time, no one stepped forward.

The Bai warriors stared blankly at the man standing tall like the Grim Reaper, then took a step backward as though they had all agreed to do so.

But then…

Boom.

Boom.

An ominous sound came from the stairs behind them, erasing even the slightest possibility of escape.

“Oh, right. I forgot to mention something.”

Jin Taekyung grinned and pointed toward the stairs.

“Something big is coming.”

The next moment—

The Bai warriors heard a chilling roar.

“Taishan. Hungryyyyyyyyy!”

A starving beast.

No—Taishan’s roar.
## Chapter artifact 669

# Chapter 669

The time it takes to drink a cup of tea.

No, perhaps mere moments.

It had taken less than the time needed to drink a cup of tea for everything in the underground prison to be settled.

With Taishan—half-maddened by hunger—blocking the stairs, and Yayul Mok and the Seven Miao Tigers advancing with me at the front, the Bai warriors lost their will to fight.

It was a very fortunate development for me.

We needed to escape the underground prison as quickly as possible, but I was also beginning to feel my limits. I still had not completely grasped the full utility of the Middle Dantian.

I had already expended a tremendous amount of mental strength breaking my restraints, and then there had been one short battle on top of that. My stomach was churning, and pain had begun to spread through my chest.

Taishan’s appearance at that precise moment was like having an entire army at my side.

“Gwoooooooh!”

Hmm. Actually, at this point, he was closer to the Hulk.

And the eerie muttering Taishan kept spouting had played a major role in the enemies’ quick surrender, along with my presence as a Supreme Peak master.

“%#$%&^&%^&%^#$!”

“Gasp!”

Eyes gleaming with hunger.

To the Bai warriors, Taishan approaching while rattling off incomprehensible words at machine-gun speed must have been the very embodiment of terror.

But I knew the true nature of his incantation all too well.

“Roast duck! Maechae Guyuk[^1]! Fish-Fragrant Shredded Pork! Beijing Sauce Shredded Pork! Garlic Pork! Twice-Cooked Pork! Sweet and Sour Pork! Soy-Braised Beef! Dongpo Pork! Mapo Tofu!”

“……”

“Kung Pao Chicken! Stir-Fried Mushrooms and Vegetables! King-Size Dumplings! Beggar’s Chicken! Sweet-and-Sour Carp! Aaaaaaah!”

Hmm.

It was a good thing they could not understand Han Chinese. Although perhaps approaching slowly while chanting the names of food like a man possessed was even more frightening.

“Hungryyyyyyyyy!”

“Eek! It’s dark arts! That monster is about to use dark arts!”

“Surrender! I surrender!”

That bastard was a Saiyan, at least by Nanman standards.

Judging by their reactions, you would have thought he was shouting “Kamehameha!” instead of “I’m hungry!”

Regardless of what I thought, “hungry” clearly worked. Even the few brave men who stepped forward undaunted got wrecked by Taishan, bringing the situation to an end.

“Do not fear! Charge!”

“We can do this! Strike him!”

The men who stepped forward were skilled enough to be regarded as fairly capable First Rate masters even in the Central Plains.

Their only problem was that their opponent was a particularly bad match for them.

Thud! Craaack!

Crack-crack!

As Taishan swung his log-thick limbs, bodies went flying in every direction.

The sight made the Bai warriors swallow hard and lower their weapons. Yayul Mok and the Seven Miao Tigers stared at me in stunned disbelief.

“What? Why are you looking at me?”

“No, it’s just… weren’t you hit by a restriction on your internal energy?”

“Ah. I was. I still can’t use it.”

“……Then how?”

“Explaining mine would take a while. That guy was simply born that way.”

The human body naturally had limits. Unlike me, who had surpassed those limits by a tremendous margin through the System, Taishan was a naturally occurring monster.

Even without internal energy, he could beat a First Rate master as easily as swatting a rat.

*Was he exposed to gamma radiation as a child or something?*

It was a fairly reasonable suspicion, but that was not important right now.

I looked at the Bai warriors who had lost their will to fight and disarmed themselves, then muttered quietly.

“All right. Let’s clean things up here first.”

* * *

To give you the conclusion first, the Bai warriors who surrendered survived.

More precisely, Yayul Mok spared them.

Thud. Collapse.

A body struck by a Pressure-Point Strike lost consciousness and collapsed.

The Seven Miao Tigers, whom I had gotten acquainted with a few days earlier on the way to Ailao Mountain, gathered them in one place and locked them inside the underground prison. We did not waste any time before heading toward the staircase leading to the surface.

Squelch.

“I told you before… you’ll regret this.”

The words came abruptly as we walked. Understanding what I meant, Yayul Mok shook his head.

“That will not happen.”

“Our faces were fully exposed. Once they regain consciousness, whose name do you think they’ll give first?”

Yayul Mok was the Young Palace Lord of the Nanman Beast Palace, so there was no need to say more. The Seven Miao Tigers were also well-known warriors who represented the Miao people.

Though their tribes were different, some of the prisoners had probably already realized who they were.

“It’s only a matter of time before this comes to light. We should have silenced them.”

“It does not matter.”

“Like hell it doesn’t. You said we weren’t going to flee along this path, so why wouldn’t it matter? If we remain here…”

“Our identities will be revealed. Our lives will not be in immediate danger, but we will pay dearly for defying the Tribal Grand Council’s decision.”

“I hate to ask this, but do you have some kind of hobby where you enjoy getting fucked? Is getting locked in an underground prison on your bucket list?”

“Bucki… It is difficult even to pronounce. I do not know what it means, but I already took that risk when I did this.”

Yayul Mok continued in a low voice.

“Our tribes may be different, but we are all Nanman people who have lived together on the same land for countless years. If we kill our own kind, we will become monsters as well.”

Listening to Yayul Mok, I suddenly thought of someone.

A man who had become a monster for the sake of revenge alone.

*Baeksang.*

Yes. Perhaps this was the difference between humans and monsters.

Not sacrificing fleeting lives to accomplish one’s own purpose.

But I opened my mouth with a heavy heart.

“We should have killed them all.”

“You like killing. Are all Han Chinese like you?”

“You crazy bastard. Do you think I’m some kind of fiend? It’s just…”

“That is enough. I already know, even without you saying it.”

“What?”

When I turned my head, Yayul Mok was smiling soundlessly.

“You are worried about us. You feel guilty because we got ourselves into trouble trying to save you.”

“……”

“Though our languages are different from those of the Central Plains, the word ‘friend’ exists in Nanman as well. Perhaps you and I have become friends without realizing it. Or perhaps that is merely my own delusion.”

“……!”

Damn it. I had no idea what I was supposed to say to that.

Just as I lost my words, the staircase that had stretched endlessly upward finally came to an end, and the entrance to the underground prison appeared before us.

“Wonhu.”

At Yayul Mok’s call, a middle-aged man nodded and stepped forward.

Looking like a monkey, he inserted a large ring of keys one after another. With a deep, heavy rumble, the enormous iron door began to open.

Grooooan.

Faint moonlight seeped through the slowly opening door. At that moment, Yayul Mok took two small wooden cases from inside his robes.

“This is an antidote that can release the restriction on your internal energy. It was made using a secret Bai technique, so I was only able to obtain two. Once your internal energy is restored, you should be able to lead the others out of Nanman.”

“The others, you mean…?”

“I do not know whether it is because they are old and injured, but the security there was extremely lax. At least in that respect, Uncle Baeksang was not as thorough as usual.”

At the same time as Yayul Mok answered, I saw them.

Beyond the fully opened iron door, two unconscious people were being carried on the back of a White Tiger.

“Lord! Namho!”

Seeing the familiar faces, Taishan hurriedly ran out of the underground prison. I stared at Yayul Mok with complicated emotions.

“You…”

“Go. We will hold them off for as long as we can. Of course, we will be discovered within half a shichen at most, but even that should help.”

I did not know.

I had no idea what I was supposed to say in this situation.

What would have happened if I had not had their help?

Taishan and I might have been able to escape the underground prison on our own, but without their help, we never would have been able to flee the Nanman Beast Palace as swiftly as we could now.

Namho and Sama Pyo, who had been detained somewhere inside the Inner Palace, had been restraints more powerful than ten thousand geun of iron balls.

*Perhaps I would have been captured again in the process.*

But they had helped me with everything they had, even while accepting that they might be placed in danger themselves.

Because of that, I had been given a second chance to take back a bad move.

“……Thank you.”

At the thanks I had not managed to offer until now, Yayul Mok and the Seven Miao Tigers—as well as the men disguised as Bai warriors outside the underground prison—smiled faintly and shook their heads.

“You do not need to thank us.”

“Indeed. We merely repaid the debt Nanman owed you.”

“My hyung was on Ailao Mountain. Thanks to you, I can meet him again.”

People whose faces and names I did not know had helped me, and one of them called me his benefactor.

I committed each of their faces to memory, one by one.

Then I accepted the wooden cases from Yayul Mok and stepped beneath the dim moonlight.

Squelch.

The moment my foot landed on the damp earth—

Ding!

> **System**
>
> - Escape from the underground prison before the execution (**Complete**)
>
> - You have fulfilled the Quest success conditions!
>
> - You have successfully completed the Quest, **Escape from Namshank**!
>
> - Issuing the Quest completion Reward!
>
> - You obtained a massive amount of EXP!
>
> - Level Up!
>
> - Some injuries and Status Effects have been removed!

Along with the Quest notifications piercing my ears, a refreshing breeze that only I could feel swept through my entire body.

Whoooosh!

My muscles had been stiff for more than a full day. The fatigue that had accumulated throughout my body from forcibly drawing up the still woefully insufficient power of the Middle Dantian began to fade.

Finally, the force constricting my Lower Dantian melted away helplessly.

Hoo.

Heat from the Scorching Yang Qi mingled with the breath I exhaled deeply.

Yayul Mok and the Seven Miao Tigers widened their eyes, as if they had sensed something from my appearance.

*Of course they’re surprised. I haven’t even taken the antidote yet.*

But I had neither the time nor the intention to explain every little detail.

I tossed Taishan one of the pills from the wooden case, telling him it was a snack, then fed the other one to the unconscious Sama Pyo.

Fwoosh. Sssslip.

The pill melted like water under the influence of the Scorching Yang Qi. Once it transformed into liquid and passed down Sama Pyo’s throat, color returned to his slightly pale face.

*He’s in better shape than I expected, but he can’t afford to overexert himself for the time being.*

Leaving Namho aside, the fact that Sama Pyo—our reliable fighter—could not fight at full strength was a major disadvantage.

But that did not mean our chances of escaping had vanished.

No. We were in a better position than before I surrendered.

*We’ve secured the others apart from the reconnaissance squad, and I’ve gained a little insight as well.*

On top of that, Yayul Mok had shown me another unexpected kindness.

“Go with this one.”

Grrrr.

A familiar growl.

The White Tiger, looking at its lifelong friend and master with sad eyes, held out its back toward me.

“Muyaho is a spiritual creature even among the White Tigers of Nanman. He is like a sibling to me, so I trust you will take good care of him.”

As if it understood Yayul Mok’s low voice, the White Tiger licked my hand, then pressed its nose against me and sniffed.

Yayul Mok smiled faintly as he watched it, then pointed in one direction.

“Go now. If you run straight northeast from the place where we first met, you will encounter the reconnaissance squad.”

And it was precisely then.

Thud.

A body jolted with the sound of an impact. Wonhu caught Yayul Mok as he collapsed, then grinned at me.

“I trust you understand without us saying it.”

“You people…”

“Please look after the Young Palace Lord.”

[^1]: Maechae Guyuk is pork belly served with preserved mustard greens; the Korean name is a shortened rendering of the Chinese dish name.

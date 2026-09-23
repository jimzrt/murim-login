# Checkpoint Review — 775–779

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

# Chapters 775–779

## Plot

Jin confronts Michael Silbert at the World Hunter Federation’s inaugural ceremony, rejects his intimidation, and refuses to submit. As the ceremony’s leadership vote begins, Team Leader Choi reveals that Cheon Taemin is in a coma and cannot join the coming war. Jin tells the Skeleton King he plans to take a dangerous risk, asking him to trust their friends and reminding him that they are friends.

Jin disrupts the leadership gathering by destroying the central seat and publicly declaring that the Stone King is a monster. When the Hunters turn their weapons on the King, Jin stands between them and calls him his friend and comrade-in-arms, saying the King saved his life. Fabian, Kronos’s Guild Master, threatens to revoke Jin’s Hunter status and execute him; Magic Johnson, Chuck Hagel, Faye Chen, Felix, and Choi Minwoo openly side with Jin. Michael threatens to put Jin’s permanent expulsion to a Federation vote and promises legal proceedings or summary execution for those who resist. Jin challenges Michael by asking whether he is already no different from a monster, then asks if the wound on his neck has healed.

## Continuity

- Cheon Taemin is in a coma and too ill to participate in the coming war; Team Leader Choi revealed this publicly, and Magic Johnson confirmed it.
- The World Hunter Federation leadership vote has begun, but its outcome remains unknown. Michael seeks leadership and threatens to put Jin’s permanent expulsion to a vote.
- Jin intends to attempt a dangerous plan with odds close to fifty-fifty, trusting his friends and the Skeleton King.
- The Skeleton King says Jin was the first friend he made after coming into this world. He once sacrificed himself to save Jin from the Arch Lich.
- The Stone King’s identity as a monster is now public. Jin protects him as a friend and comrade-in-arms who saved his life.
- Magic Johnson, Chuck Hagel, Faye Chen, Felix, and Choi Minwoo openly support Jin after Fabian threatens him.
- Fabian is the Guild Master of Kronos, an S-rank Hunter active since the Great Cataclysm.
- Michael’s nature remains unconfirmed. Jin’s reference to a wound on Michael’s neck leaves its status and significance unresolved.
- Cheon Taemin’s recovery remains uncertain.

## Translation Decisions

- Render 외조부 as **maternal grandfather**.
- Keep Jin’s uncertainty between 도편추방제 and 도편추첨제 as **ostracism by lot** and **ostracism by ballot**.
- Preserve the distinction between **Skeleton King** and the final declaration’s **Stone King**.
- Render 파비안 as **Fabian**, 크로노스 as **Kronos**, 척 헤이글 as **Chuck Hagel**, and 파이 첸 as **Faye Chen**.

## Durable state

{
  "active_continuity": [
    "The Stone King’s identity as a monster has been revealed at the World Hunter Federation gathering, and Jin is protecting him as a friend and comrade-in-arms who saved his life.",
    "Magic Johnson, Chuck Hagel, Faye Chen, Felix, and Choi Minwoo openly side with Jin after Fabian threatens him.",
    "Fabian is the Guild Master of Kronos and an S-rank Hunter active since the Great Cataclysm.",
    "Michael intends to lead the World Hunter Federation and has threatened to seek Jin’s permanent expulsion; Jin suspects Michael may himself be no different from a monster.",
    "Cheon Taemin remains in a coma and too ill to join the coming war."
  ],
  "continuity_sources": [
    779,
    778
  ],
  "open_questions": [
    "Who will lead the World Hunter Federation, and will its members vote to expel Jin?",
    "Will Michael act on his threat against Jin, and what does Jin’s reference to Michael’s neck wound imply?",
    "Can Cheon Taemin recover from his coma?"
  ],
  "safe_through": 779,
  "temporary_decisions": [],
  "version": 1
}

## Reading copies

## Chapter artifact 775

# Chapter 775

Every now and then, something I genuinely mean slips out before I know it.

Like right now.

“What a load of shit. What a load of shit.”

But even in the face of my biting tone, Michael Silbert showed no particular emotion.

Instead, he greeted me with a look still carrying the afterglow of ecstasy.

“You arrived earlier than I expected. I’ve been waiting.”

“While practicing a musical by yourself?”

“A musical?”

Michael Silbert thought for a moment before letting out a dry laugh.

“Well, I suppose that isn’t entirely wrong. Today’s gathering is ultimately a musical as well. One person handling the directing, production, and starring role.”

“My mother used to say that if you ate anything without being choosy, you’d end up sick.”

“There’s no need to worry. This is a show guaranteed to be both trouble-free and successful.”

“That line you delivered earlier was pretty terrible. Do you really think it’ll be a hit?”

“Though it was only a rehearsal before the main performance, I’ll take your opinion into consideration.”

His relaxed attitude. The faint smile hanging around his lips.

With every step he took toward me, I felt my insides twist tighter. Every time I drew in and let out a breath, it felt as though a giant needle were rummaging around inside my stomach.

Was this the effect of **Broken Body**? Or was it because I was standing face-to-face with the lunatic now right in front of me?

Maybe it was both.

“Did that friend come with you?”

“Find out for yourself.”

“That wouldn’t be a bad idea.”

Michael Silbert gazed steadily at the firmly closed door over my shoulder, then nodded.

“I’ve confirmed it. You brought him here safely.”

If an ordinary civilian had witnessed this scene, they might have wondered what kind of nonsense he was talking about.

But I knew exactly what he meant.

*Shhhhh.*

There was no sound.

No shape, either.

And yet I definitely felt it.

The instant the desired target was found, his qi wave was drawn back into his own body.

It was completely natural, carried out with practiced skill. He looked less like a Hunter and more like a Supreme Peak master of the Murim.

Someone who had already stepped outside the boundaries of every ordinary Hunter I had encountered so far.

At the same time, the fact that even I still couldn’t easily measure the true strength he had yet to reveal made my thoughts grow complicated.

But…

I couldn’t let him see even the slightest sign that something was wrong.

Just as a brief silence settled between us, I abruptly opened my mouth.

“He came with me.”

“Hmm?”

“I didn’t bring him. We came together.”

Michael Silbert looked at me with a puzzled expression for a moment, then laughed out loud.

“Very well. If the person involved insists on putting it that way, perhaps there is a difference. But what possible difference could it make?”

“A huge one. Though a person like you would never understand it, even if you died and came back to life.”

“Not at all. The only thing that matters is that you and your friend are here. If there is anything more important than that…”

The voice reaching my ears suddenly dropped into a low murmur.

“Your intention.”

“My intention?”

“Yes. The intention behind coming here today.”

As though he had suspected it from the very beginning, he watched me with narrowed eyes. After a brief silence, I spoke.

“Let me ask you one thing.”

“I’m the one who should hear an answer first, but very well. I’ll permit the question.”

“And what is your intention?”

“What?”

“The intention behind all these unbelievable atrocities you’ve committed. What is it that you’re trying to obtain, even after sacrificing so many people and pushing the entire world into a pit of fire?”

*Tap.*

The distance between us, only a few steps to begin with, narrowed.

We stood so close that the tips of our noses nearly touched. I could clearly sense his faintest expression, the tiny hairs on his skin, and even the breath he exhaled.

A human being.

Considering everything he had done, it was difficult to believe, but Michael Silbert was undeniably human, just like me.

A human being made of blood, flesh, and bone.

And yet, why?

“Why did you do those things? What in the world were you doing it for?”

From the very first moment I had met Michael Silbert, my feelings toward him had always been anger.

But not now.

I was genuinely curious. I couldn’t understand him.

The more I pursued the clues surrounding him, the deeper my questions became.

“Born on March 18, 1994, in Paris’s Tenth Arrondissement. His father ran away before he was born, and his alcoholic single mother, who lived with him, died in 2012.”

The life story of one man I had pieced together spilled from my lips.

I turned away from Michael Silbert and began to walk.

*Tap. Tap.*

One step.

Then another.

I was walking while retracing someone’s past.

Crossing the First National Assembly Hall, which had since become a World Heritage site, I walked alongside the trail he had left behind.

A childhood in which he had been polite and exemplary despite his harsh family circumstances.

But after his mother’s death came a late descent into delinquency, followed naturally by several criminal convictions.

And finally, the event that completely overturned his life.

“In 2020, when the Great Cataclysm began, he awakened in his mid-twenties.”

I suddenly stopped walking.

I raised my head. In the stained glass set into the wall, a young man stood alone amid countless heaps of corpses, tears running down his face.

Beside him was a short inscription.

*December 25, 2020 — The Great Battle of Paris*

It was said to have been one of the fiercest battles of the entire Great Cataclysm—easily among the ten most intense.

Instead of bells ringing through the streets to celebrate Christmas, screams and thunderous explosions echoed through Paris. A thousand Hunters stationed in the city waged an urban battle against monsters that outnumbered them dozens of times over.

For an entire week.

Without any support.

A desperate struggle in every sense of the word.

And when seven days and nights had passed, when even the final sun of 2020 had fully set, the support troops that arrived late after finishing another battle found a young man standing amid countless corpses and pools of blood.

“That was you.”

I turned around slowly.

The face of the young man in the stained glass was there—the young man who had survived alone in that ruin, more than thirty years ago, while the stench of blood hung thick in the air.

“Michael Silbert.”

At my quiet call, Michael, who had been listening to the story without a word, finally opened his mouth.

“First, I’ll compliment you on the effort you put in. You certainly worked hard. The records from before my awakening must have been difficult to find, since they had already been erased.”

“To be precise, you erased them. There was nothing to gain from people learning that you had been a convicted criminal.”

“I won’t deny it. I thought those records might someday stand in my way. As luck would have it, everyone was confused at the time, so it was easy to take care of.”

Michael Silbert answered calmly, then stared at me.

“But… if that’s all you found, I’m a little disappointed.”

“What?”

“The Tenth Arrondissement of Paris, where I was born, was a dump. Fights broke out several times a day, and gunshots rang out every night. The walls of the alleyways I passed through on my way to and from school were always dark red. But no one ever wiped the blood from them. It would be red again the next day anyway.”

“…”

“That was my hometown. During the day, gangs made up of every kind of ethnicity roamed the streets, and at night, the neon lights of the entertainment districts shone brilliantly. You called my mother an alcoholic earlier, didn’t you?”

Michael Silbert asked the question without emotion, then answered it himself.

“You didn’t know she was a drug addict as well, I take it. Whenever I came home after class, she was always sprawled limply across that worn-out sofa. With strange men I had never seen before.”

Everyone had a painful past.

But strangely, a faint smile appeared around Michael Silbert’s lips as he recalled his old days.

“A man called my father, who only planted his seed and ran away. A woman who was my mother in name alone. And the child born between them, continuing a life stained by assault and theft. That was me. But at the same time, I was also the hero who saved Paris twice, and the pioneer who was always the first to raise his voice for people facing a crisis.”

“…”

“Long ago, I was ashamed of that past. But not anymore. From a child in the slums to a hero of the world. Isn’t that excellent marketing?”

For a moment, I forgot how to speak as I stared at Michael Silbert.

*What could someone possibly have gone through to become that worn down?*

The clock of his life, which had never stopped for even a moment from the instant he was born until now, looked as though it had been running for six hundred years instead of sixty.

Just like his heart.

And beneath my gaze, the smile at the corners of Michael Silbert’s mouth deepened.

“You’re looking at me as though I were a monster. Now you’re afraid of me too?”

“Me too?”

“Everyone who knows me looks at me with fear and respect. You aren’t the first to look at me that way.”

“Some of them are already dead, I assume.”

“If they won’t bow their heads on their own, shouldn’t they be forced to yield? They were fools.”

Those words were no longer aimed at enemies from a past that no longer existed in this world.

They were aimed at me.

A warning to lower my head before he crushed me by any means necessary. A meticulous attempt to make sure not even the slightest possibility of things going wrong remained.

I quietly took in Michael Silbert’s appearance, then broke the brief silence that had settled between us.

“You’re half wrong and half right.”

“What does that mean?”

“It’s true that I see you as a monster. But this isn’t fear. It’s pity. You could call it disgust, too.”

“…”

“I just wanted to ask. Whether this could be cleaned up before irreversible sacrifices occurred. Whether any trace of humanity remained in this lunatic. And…”

I continued in a voice that had sunk low.

“I’m a little disappointed. That you thought I could hold you back with nothing more than a few criminal convictions.”

“What?”

Without waiting for Michael Silbert to understand what I meant, I turned around and reached out my hand.

*Whoosh. Bang!*

The qi that shot from my fingertips gently pushed open the door that had been firmly closed.

At the same time, beyond the two doors now standing wide open, I heard the sound of people slowly approaching by way of the stairs.

I nodded toward Michael Silbert, his face stiff.

“Don’t keep busy people waiting. Start the inaugural ceremony you were planning, you fucking bastard.”

“…”

“You haven’t even transferred the deed, and you’re already acting like the landlord. What a fucking asshole.”

Ignoring Michael Silbert’s icy stare, I leaned back against the nearest seat and sat down.

The die had already been cast.

Which face this still-rolling die would show—one or six—would be decided soon.

Along with who would die and who would survive.

And I had not the slightest intention of dying in a place like this.

Especially not at the hands of a monster instead of a human being.

*Tap. Tap. Tap.*

Hundreds of footsteps finally entered the now-silent conference hall.

At long last, the first page of the new World Hunter Federation—the page that would be recorded in history—was turning.
## Chapter artifact 776

# Chapter 776

There are several unanswered questions in this world.

The relationship between troubled times and heroes was one of them.

Did heroes appear, and then troubled times begin?

Or did heroes emerge because the world was already in turmoil?

Even after many years had passed, no clear answer had emerged that could satisfy everyone. But when faced with the history of the Great Cataclysm, even those who had argued for the former were forced to turn toward the latter.

A Great War unlike any other in human history.

The catastrophe known as the Great Cataclysm had torn down every common assumption people had held until then. It gave birth to countless heroes, then promptly shoved them into the pit of death.

Leaving behind nothing but their names and achievements.

But there had also been no shortage of heroes who survived.

Just like the people now gazing blankly at the National Assembly Hall, filled with traces of glory, and the enormous round table standing at its center.

“Hmm. This place hasn’t changed. It still has the same air it did that day.”

“It’s changed a little. When did that painting get there?”

“What are you talking about, hyung? It’s been almost thirty years. Didn’t you attend the commemorative event back then?”

“I didn’t.”

“Why not?”

“Because I never wanted to remember those days again.”

Gaining power beyond that of ordinary humans did not mean everyone could maintain their youth.

Time had passed, and an old man with a head full of white hair muttered in a husky voice.

“So many seats are empty.”

The survivors had been forced to endure losses as immense as their glory.

Where had the comrades who had once sat around this very table and raised their voices gone? Where were the people who had fought back-to-back against monsters surging in from every direction?

“I never thought I’d have a reason to come back here….”

Like some cruel joke played by fate, they had eventually returned.

Back to this place that bore the traces of glory and pain. Back to swear once more that they would become the sword and shield of humanity.

And the empty seats left by those who had already departed were being filled by new faces.

“Greetings, Senior.”

“Who are you?”

“My name is Liam. We met during the Defense of Frankfurt, though I suppose you don’t remember me, haha.”

“My apologies. Perhaps it’s because I’m old, but I can’t even recognize the comrades I fought beside.”

“Not at all. It’s only natural that you don’t remember. I was fifteen at the time.”

“Fifteen? Then perhaps…?”

“Yes. I was one of the citizens in the bunker. You may not remember, Senior, but you saved my life back then.”

“Good heavens.”

The only things to survive a typhoon were not the great trees with their sturdy roots.

Those who had once been saplings, weeds, or nothing more than seeds had also grown strong and earned the right to sit at the round table.

However, among the heroes of the past and present, only a small number exchanged such warm greetings.

Partly because humanity was facing another grave crisis, but also because their values and the directions they wished to pursue were different.

Whom should they choose as their representative?

That was the most important question before them today, and the old and young heroes naturally formed groups according to their respective intentions.

At the center of it all were two people who could not be left out.

Michael Silbert, who possessed tremendous fame and achievements, and who had been the first to call for the World Hunter Federation to be reestablished.

And…

*Jin Taekyung.*

Michael Silbert silently repeated one person’s name in his mind.

He continued shaking hands and exchanging greetings with the followers surrounding him, but his deeply sunken eyes remained fixed on the young man beyond their shoulders.

*What exactly did you mean by those words?*

The voices flattering him from all around seemed distant.

The only thing echoing in Michael Silbert’s ears was the single line he had heard moments ago.

> *“I’m a little disappointed. That you thought I could hold you back with nothing more than a few criminal convictions.”*

The voice had already faded, but the memory remained vivid.

So did the shock he had felt before he even realized it.

At the same time, the heart that had always remained calm and still began to beat faster and faster.

*Wait. Could it be?*

The gray eyes watching Jin Taekyung trembled faintly.

After passing through countless deductions, one hypothesis had surfaced in his mind.

It was also the only way that man could stop Michael as he was now.

But… no. That couldn’t be. It made no sense.

*It’s nearly impossible for anyone else to realize it. No—it is impossible.*

Only one person could have done it.

Cheon Taemin.

Even he, who had reached a one-of-a-kind realm, had merely sensed something in passing at the time. Michael Silbert, who had immediately noticed the warning sign, had been forced to lie low like a wanted criminal for a long time.

Until Cheon Taemin disappeared from the public eye.

Until Michael became certain that Cheon Taemin’s attention had shifted away from him.

*But in this situation, Jin Taekyung? Not even Sky?*

As the unease slowly swelled inside him, Michael Silbert shook his head inwardly.

No. The things that man had said were nothing more than empty bravado.

Bravado meant to search for one final opening after everything was already over. The last desperate struggle of someone who had sensed his defeat.

But why?

Even while telling himself it was only a bluff, the image of Jin Taekyung from moments ago kept rising like a haze, blocking Michael’s eyes and ears.

> *“Then what is your intention?”*

One sentence.

> *“Why did you do those things? What in the world were you doing it for?”*

Another sentence.

> *“This isn’t fear. It’s pity. You could call it disgust, too.”*

That expression and those eyes. That calm voice.

What Michael Silbert had felt from that young man—who had lived barely half as long as he had—was unquestionably close to genuine emotion.

*And if that’s true….*

Crack.

A sound rang out from his unconsciously tightening grip as bones shifted out of place. Someone’s strained voice finally broke through his thoughts.

“G-Guild Master?”

“Hmm?”

“W-Why did you suddenly…?”

“Ah.”

Realizing the mistake he had made without thinking, Michael Silbert released the pressure in his hand.

One of the followers who had been shaking his hand forced a smile through the pain.

“As expected, your reputation is well deserved. I used to be a tank myself, so I’m not lacking when it comes to pure strength, but you really are incredible, Guild Master.”

The S-rank Hunters and heads of the great Guilds who had been watching the situation warily chimed in.

“Of course. Absolutely.”

“Haha. Do you think Odin Guild became the best for no reason? The name Michael Silbert has been famous since the Great Cataclysm.”

“Paul was the one at fault here, actually. I clearly saw that he was the one who used force first. Hahaha.”

Flattery disguised as praise mingled with laughter.

Michael Silbert watched them for a moment, then suddenly curled up the corners of his mouth.

Yes.

This was power.

This was why he had to obtain authority by any means necessary.

The actions of the strong were always justified by the weak who feared their power.

It did not matter if they did not respect him. It did not matter if they did not love him.

If he could make them afraid—if he could reign over them instead of merely leading them—then he would finally possess everything in the world.

Michael Silbert had first realized this truth in the back alleys of Paris’s Tenth Arrondissement.

From the gangs who walked the streets with guns tucked into their waistbands, and the people who feared them yet did not dare report them, he had realized which path he needed to take.

*This is what the world is.*

Michael Silbert gave his followers a gentle smile, then turned his head.

He spotted Jin Taekyung, seated mostly with the elders who had already retired once or who remembered Cheon Taemin’s presence.

There were also several familiar faces among them.

Grand Mage Magic Johnson. Chuck Hagel, who had resigned as United States Secretary of Defense after the vigilante incident. Faye Chen of Hong Kong. Even Prince Felix of the United Kingdom.

They were all impressive figures, even among the central figures from around the world gathered here, but they made up no more than half of the three hundred attendees.

*The old generation must have come here looking only toward Sky, while the new generation followed Jin Taekyung.*

But if Cheon Taemin’s condition became known, whom would they support?

His maternal grandson, whose only claim was sharing Cheon Taemin’s blood?

Or Jin Taekyung, who was absurdly young and had often shown himself to be reckless?

Even Magic Johnson, despite his remarkable achievements and widespread popularity, could not compare to Michael Silbert in fame or reputation.

*Whether you wanted it or not, only one person remains in the end.*

Michael Silbert himself.

The man who had harbored the greatest ambition and spent years preparing more thoroughly than anyone else.

In Michael Silbert’s eyes, they looked like sandcastles about to collapse.

*But… one should always prepare for contingencies.*

Michael Silbert casually slipped a hand into his pocket.

The moment he pressed the pager inside and sent a signal to someone, his eyes met Jin Taekyung’s.

A pair of reddish, heated eyes.

The heat contained within them reached him in full, and a searing pain, as though his skin were being scorched, spread from the back of his neck beneath his armor.

“…Hmm.”

“Oh. Is something wrong?”

“Mr. Silbert, are you feeling unwell?”

“I brought a potion, just in case. Fortunately, I happened to have it with me….”

“I’m fine. It’s nothing, so there’s no need to make a fuss.”

Michael Silbert answered his followers firmly, then stared at Jin Taekyung.

He wondered if Jin had seen what had happened.

He desperately suppressed the unease rising inside him.

But Jin Taekyung’s gaze had already shifted elsewhere, and Michael Silbert found himself calming down when he saw the person sitting beside him.

No.

The more accurate description would be a monster in human form.

*Stone King.*

As long as that creature was here, Michael would be the center of the round table.

He had to be.

> —All attendees have arrived. Please take your seats.

Finally hearing the voice flow through the speakers, Michael Silbert clenched his fist tightly.

* * *

Even after the inaugural ceremony began, the attendees did not fall silent.

No—instead, the voices of those who had been whispering quietly grew louder and louder.

“All attendees have arrived?”

“That can’t be right. You must have misheard.”

“There must have been some minor mistake.”

The old generation, classified as elders, and the newly arrived younger generation were no different. One person who absolutely had to attend was nowhere to be seen.

Yet even after everyone had taken their seats, the announcement that had come through the speakers was not corrected.

Only then did the attendees realize.

Cheon Taemin—the savior of humanity—would not appear.

Not today. Not tomorrow. Not the day after that.

Perhaps not even until the second Great War came to an end.

“What is going on…?”

“Where is Sky? Where is that person?”

What everyone had assumed was merely a small mishap spread into a murmur, then soon brought shock and confusion.

And then, at some point—

Step. Step.

One person rose from their seat and began walking toward the center of the round table.
## Chapter artifact 777

# Chapter 777

So it’s finally starting.

I muttered to myself as I watched the back of someone walking alone.

Then again, it wasn’t just me. Everyone here was doing the same.

The cameras installed throughout the hall and the three hundred pairs of eyes around the round table followed one man—or, to be precise, Michael Silbert.

*Clop. Clop.*

His footsteps carried him forward without the slightest hesitation.

The murmuring around us had died down long ago. As if they’d all agreed to it, everyone had fallen silent at once, watching Michael Silbert with a different emotion in their eyes.

Some couldn’t hide their confusion at the sight of him suddenly stepping forward. Others looked thoughtful, their eyes growing serious. A few nodded as if the whole situation were only to be expected, or wore faint smiles.

I took in every one of them.

I saw every emotion they let slip in that moment, every subtle twitch at the corners of their mouths, and etched their many faces into my memory.

Then, the next moment—

*Swish.*

Michael Silbert stopped.

Right in front of the center of the enormous round table, a space that had existed for decades solely for one man.

But his final step wouldn’t come. It was as if something invisible stood in his way. His firmly closed lips parted.

“Everyone. Today, I received truly shocking news.”

His voice was choked. Moisture glimmered around his eyes in the light.

After looking in turn at the people shaken by this unexpected turn of events and at the cameras recording it all, Michael Silbert continued.

“Just before the inaugural ceremony began, two young men came to see me and gave me the news. At first, I found it hard to believe. But in the end, I had no choice but to accept reality. I needed some time to compose myself.”

“Could you tell us who the two young men were, and what news they brought?”

Someone’s question came at exactly the right moment.

Perfectly timed, as if it had been planned in advance.

No—as a matter of fact, it had been planned.

And in this musical playing out according to its script, the leading man delivered his next line in response to the bit player’s perfectly placed question.

“It won’t be difficult to reveal the identities of the two young men who came to see me. They’re both well-known figures, and they’re here with us now. But I’m afraid it wouldn’t be appropriate for me to tell you the news myself.”

“Why not?”

“Because I’m not qualified to do so.”

Michael Silbert answered calmly, then turned to look at me—or, more precisely, at Team Leader Choi, seated to my right.

“Unless you’re family by blood, of course.”

“……!”

It would have been strange for anyone, no matter how obtuse, not to understand what he meant.

Hundreds of gazes closed in around us from every direction, leaving no room to escape. Amid them, a voice reached my ear in secret.

*I don’t know what you came here intending to do, but from now on, remember one thing.*

Michael Silbert.

He was looking at me. Not with the crocodile tears he’d shed a moment ago, but with eyes lit only by ambition.

*Every choice comes with consequences to match.*

“……”

*So please, choose carefully. It will be a choice you can make only once—a choice you can never take back.*

His final warning came with a stare, and the gazes pouring in from all around were so hot that I ended up closing my eyes.

And I thought:

*Yeah. So this is how it ends up.*

*From the start…*

*There was no other way.*

I opened my eyes with a hollow emptiness inside me. At the same time, Team Leader Choi met my gaze. He read what was in my eyes and stood up.

*Rrrr.*

The chair, which had endured for ages longer than its new master, slowly scraped backward. At that moment—

“Before we elect a representative, the purpose of today’s inaugural ceremony, I must inform you that my maternal grandfather, Hunter Cheon Taemin…”

At last, the name of one man rang out. In the suffocating silence that followed, the savior’s only blood relative continued in a low voice.

“…has become seriously ill and will be unable to take part in this war.”

“……!”

“……!”

An enormous, unseen shock swept through the room.

* * *

Suffocating silence fell over the First National Assembly Hall.

In that moment, the people frozen by confusion and shock could do nothing but repeat the words they had just heard over and over in their minds.

*“My maternal grandfather, Hunter Cheon Taemin, has become seriously ill and will be unable to take part in this war.”*

A bomb had gone off barely ten minutes after the inaugural ceremony began.

No—perhaps it was a different kind of catastrophe.

*Sky is sick? What on earth does that mean?*

*How could he…? That can’t be right. It’s impossible.*

Those who rejected reality most fiercely were mostly the old-generation Hunters known as the elders.

They remembered Cheon Taemin—the great hero who had saved humanity from the Demon King—better than anyone. And so they felt the shock more deeply than anyone else.

It was only natural.

In their memories, Cheon Taemin was more than human, almost a living god.

He had single-handedly wiped out monster armies tens of thousands strong, and torn the limbs from S-rank monsters of incredible strength.

His overwhelming prowess had been matched by an equally overwhelming presence.

With Cheon Taemin at their side, they had been willing to march into the jaws of death.

They had stood shoulder to shoulder, cutting through monsters surging toward them like waves, advancing again and again.

The elders could bear to recall those horrific battlefields because Cheon Taemin had been there in their memories.

Because those memories were suffused with the shining glory of having led humanity to victory alongside him.

But he was sick?

The savior of humanity, the man who had even defeated the Demon King Asmodeus, had become too ill to take part in the war?

The shock soon gave way to a hollow sense of loss, and some of the elders even felt anger.

“What on earth—what on earth is this supposed to mean?”

“Gravely ill? Even for someone like your maternal grandfather, that’s too much to believe!”

“Explain this properly. There’s no way he could be sick!”

But contrary to the elders’ desperate wishes, Cheon Taemin’s only maternal grandson merely shook his head, calm and composed.

“Everything I’ve told you is absolutely true.”

“Young man!”

“I understand how you feel, Seniors. I felt the same way a few months ago.”

“What… what do you mean?”

“I always wondered where my grandfather was. Why he wouldn’t show himself to his only grandson for so long, no matter what the reason was.”

Choi Minwoo looked around at everyone and continued.

“I only found out after Vice Guild Master Lee Jungryong and Go Jun died. One day, for reasons unknown, he fell into a coma—a state of unconsciousness—and a tiny handful of people had been hiding the truth.”

“……!”

Another enormous shock swept through the room. But the silence it brought didn’t last long.

“It’s hard to believe, but it’s all true. I can vouch for it.”

At the sudden low voice, everyone’s eyes turned in one direction.

A towering Black man, who had been watching the situation in silence, was looking at them.

“Magic Johnson!”

“Y-You knew about this too?”

Magic Johnson nodded before answering.

“I came to this country a few months ago after those friends contacted me. I didn’t expect to see Sky unconscious when I got there, though.”

“Th-Then it really is…”

“That’s right. Even with all the knowledge and Magic I could draw on, I couldn’t find a way to bring him back to consciousness. Of course, I couldn’t tell anyone else. If this incredible secret got out, it would cause even greater chaos.”

People suddenly remembered the situation at the time.

The magical power readings that had begun to rise, and the strange events that had begun to occur.

In China, an Arch Lich had led a monster army and drenched Sichuan in blood. People’s anxiety had only continued to grow.

“But we can’t keep it hidden any longer. The whole world is looking for Sky now, and the World Hunter Federation, which took its first step today, has to give people the answers they want—just as the UN did.”

In that moment, one word crossed everyone’s mind.

*Leader.*

With Cheon Taemin down, they needed a new leader, one way or another.

A new hero who could fill the savior’s absence as much as possible. Someone who could win the support of a majority of the three hundred people gathered around this enormous round table.

*Then…?*

By the time most people reached that thought, they had already made up their minds.

Strength. Fame. Popularity. A spirit of sacrifice and courage. Leadership…

They each had their own standards for judging a leader. And even among those already called heroes, only a handful could meet those requirements.

And in that regard, there was one person who could not be overlooked.

Michael Silbert.

Countless eyes passed over him.

Some smiled triumphantly, as if the moment they had waited for had finally arrived. Others watched with cautious thoughtfulness.

But even with the situation turned upside down, Michael Silbert gave nothing away.

He had only one final step left to take. His thoughts were already on what came after.

*It’s sooner than I expected, but… I’ll have to get rid of him. As soon as possible.*

The absolute power of the World Hunter Federation already seemed within his grasp, but an obstacle that would keep troubling him had to be removed.

Michael Silbert fixed his sunken eyes on one man.

Even as the vote began, Jin Taekyung remained silent, his lips firmly closed. Beside him sat a blond monster with a calm expression.

* * *

I looked down at the scrap of iron in my hand and thought:

*What was this called again?*

Ostracism by lot? Ostracism by ballot?

I thought I’d heard it originated in the method used to banish tyrants in ancient Athens, but I wasn’t sure.

One thing I did know: what I held wasn’t a piece of pottery, but a fragment of a tower shield. And the person whose name appeared on the most fragments wouldn’t be banished—they’d become the leader of the World Hunter Federation.

*Would’ve been nice if it worked the other way around, huh?*

The Sound Transmission I sent off on a whim got an answer I hadn’t expected.

*What the hell are you talking about all of a sudden?*

*Just saying. Anyway, you’re answering me this time.*

*Because this will probably be the last time.*

I fiddled with the piece of iron.

*You crazy bastard. I wondered why you’d answered me, but you’re still on about that.*

*I know what you’re thinking. But that’s too…*

*Dangerous?*

After a brief silence, the Skeleton King answered.

*Yes. Even now, this body cannot be certain.*

*The odds are close to fifty-fifty. And this is only my guess, but the chance of success is a little higher.*

*Do you understand what that means? There’s a fifty percent chance you could lose everything.*

*Really? To me, it sounds like there’s a fifty percent chance I could protect everything.*

*……!*

*Trust me.*

I looked around. Familiar faces. People I could trust, right beside me. They were all my comrades, my friends.

*If you really can’t trust me, then trust us.*

This silence lasted even longer than the first. And for the first time in a long while, I was able to meet the Skeleton King’s eyes.

*Why go this far? Take that risk, even though your family and friends could get hurt?*

I answered with a truth that might have been settled the day I first met him.

*Because you’re my friend, too.*
## Chapter artifact 778

# Chapter 778

“Because you’re my friend, too.”

At those quiet words, the Skeleton King’s eyes trembled faintly. I looked straight at him and continued.

“That’s all there is to it. You’re my friend, too. If I lost you like this, I’d feel like shit for the rest of my life. That’s why I can’t give up.”

“……”

“Remember when we fought the Arch Lich in China?”

The Skeleton King silently nodded at my question.

Yeah. How could I forget?

The memory of that fierce day was still etched vividly in my mind.

“I really thought I was going to die. No—if things had kept going the way they were, I’d probably have died nine times out of ten.”

It had been that hard of a fight.

The countless monsters blocking our path—and the Arch Lich we’d finally faced after putting down Lee Jungryong and Wu Heixing, who had chosen to betray us—had been too much for me at the time.

But…

“You saved me. Even knowing you might be erased.”

I could still picture it clearly. In that life-or-death moment, he had leaped out of my Inventory without even asking permission and taken the Arch Lich’s strike in my place.

It was a sacrifice.

A purely selfless and noble sacrifice.

At the same time, it was a great deed that allowed an ordinary someone to finally become a new being.

And so the Skeleton Warlord, who had ruled the Black Forest, received a crown.

He returned from the brink of Erasure, took up the radiant [Hero’s Sword], and drove it into the Arch Lich’s chest.

“Why did you make that choice back then?”

“……Who knows. I don’t.”

The Skeleton King gazed up at empty space and muttered.

“All I know is that I had a very stupid, very trivial reason.”

“A reason?”

“There was something I’d always wondered. Who am I? Where was I born, and what sin did I commit to become the monster I am now? Surely I wasn’t always like this.”

His hollow thoughts echoed in my ears.

“But no matter how hard I tried, I couldn’t remember anything from when I was alive. Even in the human world, every moment I spent with humans left me confused. I felt like something that was neither a monster nor a human. As if I were being punished without end for a sin I’d committed in the past.”

Yeah. Back then, that was how the Skeleton King had been.

He was always lost in thought with a troubled look on his face. Sometimes, he’d go into my Inventory and not say a word for days.

Then one day, I’d casually said to him:

*I bet you were a pretty decent guy.*

I didn’t know for sure, but I was sure he had been.

“That was why. I wanted to believe those words, which might have been nothing more than comfort. And, in a way, I wanted to prove them. If I really had been a decent guy in the past…”

The Skeleton King slowly tilted his head. His gaze dropped from the empty space and slid toward me.

“Then I might be able to sacrifice myself for someone else… for a friend.”

“……!”

“Yes, that’s right, you damn crafty human.”

A faint smile touched the Skeleton King’s lips.

“You were the first friend this body made after coming into this world.”

For a moment, I couldn’t speak.

I had to say something. I should have. But not a single word or phrase came to mind.

So I just smiled.

I lifted the corners of my mouth and laughed silently, then let out a few short chuckles before I couldn’t hold back any longer and burst out laughing.

Loud enough for everyone to hear across the enormous round table. Loud enough for hundreds of pairs of eyes to turn toward us.

Then I looked at the Skeleton King, who was blinking in surprise.

“You only figured out something that simple now, you dumbass?”

“C-Could you keep your voice down?”

“Just say it out loud. Don’t whisper behind everyone’s backs.”

“No, what is this—”

“It’s too late anyway. Can’t you see everyone’s already staring?”

The Skeleton King looked around, then muttered in a half-resigned voice.

“You lunatic.”

“What, a lunatic? Are you finished?”

“I wasn’t finished. Attention-seeking bastard.”

“Listen to the way this guy talks. Team Leader Choi, aren’t you going to manage him?”

“Man—what?”

Suddenly singled out, Team Leader Choi clenched his teeth, looking as if grim reality had just hit him.

“Yes, that’s right. I’m sorry. This is all my fault for failing to manage Jin Taekyung.”

“Come on, Team Leader. You’re going to hurt my feelings if you pile on, too.”

“I’m the one who should be hurt. If things had gone according to plan, in a little while… No, why even call it a plan if you’re going to do this?”

Fair enough.

But what could I do? Things had gone this way.

People’s affairs often took turns no one could predict. Just like right now.

Even so, not a trace of unease crossed my mind about the plan going out of order.

Yeah. If that was how it turned out, then so be it.

I burst out laughing again, then lowered my voice as if I meant business and addressed Team Leader Choi.

“Team Leader Choi, haven’t you heard the saying, ‘It doesn’t matter how you get there as long as you get to Seoul’?”

“I don’t want to hear it. And we’re already in Seoul.”

“Come on, try saying it with me. Heave. Ho. Heave. Ho.”

“To hell with heaving and ho-ing. I think we’re royally fucked.”

“You’re putting up a front for no reason. You’re seriously sulking, aren’t you? This was going to happen anyway.”

“The order is wrong! The order! Do you put the ramen in before the water boils?”

“No. Today, I’m going to crush it up and eat it without boiling it.”

“You little shit—!”

The man who could make Team Leader Choi swear like that.

That was me.

And just as Team Leader Choi’s eyes rolled back and he lost control, about to spring to his feet, two enormous hands reached out from behind him and grabbed him.

“Hey, Choi! Calm down!”

“Let go! You hear me? Get your hands off me right now!”

“Please, get a grip! I know Jin made a mistake, too, but… Wait. Have you been bulking up lately?”

This was a mess beyond all messes.

Seeing my chance, I gave Magic Johnson a thumbs-up as he felt Team Leader Choi’s lean muscles, then stood and looked around.

Wide-open mouths. Faces asking what the hell was going on. Eyes gone unfocused.

A commotion had erupted out of nowhere at this important meeting to elect the World Hunter Federation’s representative as humanity faced a crisis. Everyone looked as if they’d just seen Demon King Asmodeus brought back with Edo Tensei[^1].

[^1]: A technique from *Naruto* that summons the dead back to life.

Except for the few who already knew what was going on.

“Ah, I’m sorry. I wasn’t planning to spring it on you right now.”

It was a sincere, polite apology. But sometimes sincerity just didn’t get through.

“You damn bastard. This might be the last cigar of my life.”

Chuck Hagel pretended to answer with the bleak resignation of a terminal lung cancer patient, all while puffing on his cigar twice as fast.

“It’s okay. I trust you. But go fuck yourself, Jin.”

Faye Chen gave me a warm smile and raised her middle finger.

“I’m sorry, Your Majesty. I trusted that lunatic and made a rash choice…”

Prince Felix, third in line to the British throne, muttered with a look of regret.

But if I had to name the one person among the three hundred gathered here who was the most confused, it would be Michael Silbert.

*What on earth… are you up to?*

His voice slipped through space and into my ear.

Seeing his face, stiffer than I’d ever seen it, I couldn’t help but let out a laugh.

*You’re laughing?*

It was only natural to answer someone who was curious.

I opened my mouth without a care.

“Yeah, I laughed. What are you going to do about it?”

*You…!*

The voice in my ear cut off. By now, everyone in the room was looking back and forth between me and Michael Silbert, following my gaze.

“If you have something to say, say it out loud so everyone can hear. Don’t whisper in people’s ears at your age.”

After saying that, it struck me as a little too rude, so I shyly added one more thing.

“You son of a bitch.”

“……!”

“……!”

The whole room fell silent, as if hundreds of nuclear missiles had swept through it. The air surrounding us froze.

But unlike the others watching this unbelievable scene, to me that cold air felt like it had finally cleared the blockage in my throat and chest.

*I can finally breathe.*

How long had it been since I’d felt this relieved?

After taking a deep breath, I started walking at a leisurely pace. I passed between the round tables, then got tired of even that after a few steps and leaped over everyone’s heads.

*Whoosh. Tap.*

I landed lightly in the empty center of the round table.

I saw Michael Silbert clench his teeth, unable to bring himself to step into that space, as though an invisible wall held him back.

“What… is this insolence?”

His voice was tightly restrained.

In the eyes of the man glaring at me, there was anger he couldn’t hide. And I knew exactly why he was angry.

“What, you spent half your life wishing for that seat, and now some nobody gets there before you? That piss you off?”

“……!”

“Honestly, I understand to some extent. I’ve been through something similar before. One day, I was looking for the ice cream I’d saved to eat after a bath, but when I came back out, my little sister had eaten all of it and left me the wrapper. I was pretty pissed. But…”

I trailed off, gazing at Michael Silbert’s rigid face, and continued slowly.

“Then I suddenly thought, what am I getting so mad about over something this trivial? Is it really worth throwing a fit over?”

I looked around. Just as I’d expected, most people were staring at me like I was crazy.

Naturally. I’d caused a scene at the most important moment, hurled curses at a Senior, and now I was telling an ice cream story nobody had asked for.

But their expressions were so funny that I ended up laughing.

“Anyway, that’s all.”

At the same time, I drew up my internal energy and stamped my foot down hard.

“Don’t—!”

*Crack! Rumble!*

Michael Silbert’s belated shout was swallowed by the roar.

In the split second when nobody could stop me, I completely crushed the center of the round table, a place set aside for just one man. Then I looked at the faces staring at me in shock.

“After thinking about it, I realized that seat was just like that ice cream. If nobody was greedy, there’d be nothing to get angry about. But the greedy ones always step forward and cause trouble.”

Of course, there was an incomparably vast difference between ice cream and the World Hunter Federation.

The importance of each in this world. And…the scale of the fallout caused by that greed.

People had died because of that greed.

Hundreds of thousands of people had lost their families and friends, their homes and their hopes.

After paying such a high price, all they’d gained was despair and fear.

So what was the difference between that seat and ice cream?

It was ridiculous. It was hollow.

Then I spoke to the hundreds of people looking at me in shock.

“Everyone, listen.”

No. I was speaking to Michael Silbert.

“The Stone King is a monster.”

That one casually tossed-out line swallowed everyone whole and exploded.
## Chapter artifact 779

# Chapter 779

For a moment, it was as if the world had stopped.

If not for the camera flashes blinking at regular intervals and the second hands ticking, people might really have thought time had frozen.

But the silence didn’t last long.

“Crazy.”

Someone’s voice burst out.

Plenty of people looked back and forth between Jin Taekyung and the Stone King with incredulous smiles on their faces.

They couldn’t help it. Everyone here knew who the Stone King was.

No—ask anyone on the street, and they’d know, too.

An S-rank Hunter with United States citizenship who had appeared like a comet one day.

As skilled as he was handsome, he’d always been by Jin Taekyung’s side. That had drawn considerable attention from the start, and he’d distinguished himself in several major incidents.

He’d once become a target of criticism alongside Jin after taking part in an operation to eliminate terrorists—the one often called the “vigilante incident.” But the general consensus was that, on balance, his contributions far outweighed his faults.

And now the Stone King—by this point recognized as one of the young heroes representing a new generation, and granted a seat at the round table—was a monster?

Instead of confusion, incredulous laughter spread through the crowd.

“Don’t talk nonsense.”

It was hard the first time. After that, it got easier.

The people who had held their tongues out of consideration for Jin Taekyung’s extraordinary skill and standing gradually began to raise their voices.

“Now that we’ve let you go on this long, aren’t you taking things a little too far, young man?”

“Mr. Jin. I respect you as a Hunter, but… you’ll need to give a reasonable explanation for the things you’ve done here today.”

“They said he was suffering from post-traumatic stress disorder. Looks like that was true.”

The fuse was burning down fast.

Even the elders who had looked favorably on Jin from the start let out troubled sighs, while those already on the other side took the opportunity to criticize him openly.

“Everyone, look at what he’s done. He caused a disturbance during this crucial moment when we’re electing the leader of the Federation that will save humanity, and he even damaged the round table.”

“And now he’s spouting nonsense on top of that.”

“What kind of disrespect is this?”

Criticism poured in from every direction.

But the man at the center of it all, Jin Taekyung, opened his mouth to address the room as if he hadn’t heard a thing.

Once again.

Without changing a single word from what he’d said before.

“The Stone King is a monster.”

“That’s all you’ve got? That same nonsense again?”

“He’s crazy. Completely crazy.”

Jin Taekyung slowly looked around.

There were those who laughed in disbelief, those who frowned, and those who watched with grave, steady eyes.

Their reactions varied, but the words that slipped between Jin Taekyung’s lips the next moment remained unchanged.

“The Stone King is a monster.”

“What is this—!”

“Strip him of his qualifications at once!”

The voices of criticism had become shouts. But Jin paid them no mind and opened his mouth again.

“The Stone King is…”

As if those were the only words he knew. As if imprinting those words on people’s minds were the sole purpose of his life.

Without pause, ignoring every gaze and every accusation pouring toward him.

Once again, Jin Taekyung calmly repeated the fact that might become his greatest weakness.

While looking at Michael Silbert, the one man who remained silent amid the commotion that had swallowed the enormous round table.

“A monster.”

That was the third time.

The mocking smiles on people’s lips faded as he repeated the same words like a machine.

The shouts ringing through the room stopped. So did the pointing fingers. Now, no one moved or spoke.

Silence had settled in before anyone knew it.

And in that perfect silence—not even the sound of someone swallowing—a realization suddenly came to them.

Jin Taekyung was telling the truth.

His expression, his voice, his eyes. Every last thing about him was utterly unlike a lie.

And they realized what that meant.

*…No way.*

An unbelievable question crossed everyone’s mind.

At the same time, hundreds of pairs of eyes turned toward one person.

No—toward something that might not even be human.

The Stone King.

The handsome American was still sitting right where he had been from the beginning. But people could see it. They could feel it.

The slight trembling of his eyes and the faint fear seeping through them. The certainty that this was the answer to their question.

Then the truth they had finally accepted came with an enormous unseen shock that swept through the room like a wave.

No—a hammer blow.

“……!”

“……!”

Faced with this unbelievable truth, everyone stared with their mouths agape.

What was reflected now in the wide-open eyes of more than three hundred people was neither a handsome young man nor an S-rank Hunter with outstanding skills and Fame.

There stood a cursed being who could never coexist with humanity, one who had once driven mankind to the brink of disaster.

“…A monster.”

At that moment, someone’s muttered words—more of a groan—broke the silence.

*Clang, clang, clang!*

Beneath the lights illuminating the vast room, hundreds of weapons flashed as they caught the light.

The radiance of Aura, the power God had gifted to humanity, spread in every direction, then turned toward one being.

Along with killing intent so vivid it seemed tangible.

*Ssssss.*

A wind whipped up from somewhere. In the freezing air, countless needle-sharp gazes pierced the Stone King.

Everyone here had been chosen by God for the sole purpose of fighting monsters, and given the name Hunter by humanity.

From the very beginning, they had been given only one duty.

*Kill monsters.*

*Whoooosh.*

And just as hundreds of powers and murderous intentions converged, bearing down on the room and shooting toward their target—

“Stop!”

*Bang!*

A roar like a wild beast’s, its deep resonance wedging into that split-second gap, scattered everything like mist.

At the same time, the faces of the people who had looked ready to swing their weapons at any moment went rigid.

*What the hell…*

A place where immense killing intent and mana were surging was as good as a death trap.

But the voice’s owner had broken that flow. At the very last moment, just as an attack was about to be unleashed, he had slipped through an invisible gap.

And he’d done it so easily it seemed effortless.

*Step. Step.*

The low thud of footsteps broke the suffocating silence.

As one young man cut through the mountain of sabers and forest of swords formed by countless weapons and stood in front of everyone, an elder Hunter with a full head of white hair spoke with a stern expression.

“What do you think you’re doing?”

Recognizing him, Jin Taekyung answered with due respect.

“I’m doing what I have to do, Senior.”

“And what you have to do is… protect that monster?”

“That’s right.”

At Jin’s unhesitating reply, the elder Hunter asked with an expression of disbelief.

“Why?”

“Because he’s my friend.”

“…Your friend?”

“And he’s a comrade-in-arms who saved my life. So I have to protect him. Just as he did for me.”

Friend? Comrade-in-arms?

Everyone was at a loss for words at terms they’d never imagined hearing used for a monster. Then, from within the encirclement that had naturally formed, someone spoke up.

“If you’re going that far, there’s no need to hear anything more.”

A shining suit of full-body armor. A massive war hammer in his hand.

The middle-aged man stepped forward, trailing a heavy aura and an oppressive presence. His eyes were fixed on Jin Taekyung, but his voice was aimed at everyone.

“This is treason against humanity. An unforgivable act of betrayal. You know the punishment for that, don’t you?”

Jin Taekyung nodded.

“Of course.”

“Good. Then you already know. As of this moment, your Hunter license is revoked, and the traitor will be summarily executed.”

*Rumble.*

A thick glow layered itself over the war hammer.

An S-rank Hunter who had fought since the Great Cataclysm, and a heavyweight who had made the name Kronos known as one of the world’s top ten Guilds.

But the reaction Jin Taekyung showed the next moment far exceeded everyone’s expectations.

“Fuck, don’t be so damn ridiculous.”

“What?”

“That speech was so long-winded I couldn’t even follow every stupid point. But first, I want to ask you one thing.”

Jin Taekyung fixed his lowered gaze on the Guild Master of Kronos.

“If you were going to throw this kind of fit, why did you treat me like a lunatic a minute ago?”

“That’s…”

“That’s what?”

The Guild Master of Kronos suddenly found himself at a loss for words.

And not just him. Everyone who had heard Jin’s words was the same.

A remark that struck unexpectedly close to the mark.

That was right. They’d treated Jin Taekyung’s words as nonsense from the start. And even as people criticized him, he’d silently repeated them three times, as if making sure they understood.

Until the mocking smiles vanished from their lips. Until they realized all of it was true.

But even though he’d spoken with such sincerity, why hadn’t they believed that young man?

The answer was simple.

No, perhaps it was a truth they had already known, but had been forced to pretend they didn’t.

“Let’s be honest. Now that you’ve learned the truth, you don’t want to accept it. That the guy sitting over there—some lowly monster, for God’s sake—has fought harder for humanity than some of the assholes who don’t even have any real business being here.”

“……!”

“Of course, I can understand that much. Who’d just take it on faith that the Stone King was a monster? Right?”

No one answered from anywhere in the room. Jin Taekyung smiled.

“This is a black comedy if I’ve ever seen one. There are assholes everywhere who aren’t even human, but the guy who nearly worked himself to death trying to save one more person is standing at death’s door the moment his identity comes out.”

Cold flames flickered in the young man’s eyes, visible above his raised smile.

Countless weapons surrounded them. As he looked at that forest of blades, poised to come flying at any moment, the emotion rising inside him had a name: anger and bitterness.

“I didn’t want things to turn out like this. I wasn’t asking for that much. I just… thought you’d give me enough time to explain.”

Jin Taekyung muttered hollowly.

Of course he understood. Surely many of them had lost someone close to them to a monster.

Just as he had.

But… even so, something churned inside him.

He felt sorry for the Skeleton King, who had fought while sacrificing himself for humanity. He felt bitter watching those people try to kill him without a moment’s hesitation, and his anger rose when he realized how many of them still showed outright hostility, even in this situation.

Because he knew their hostility wasn’t just because he thought of the Skeleton King, a monster, as his friend and comrade-in-arms.

And all the more so because he knew where that hostility was aimed, what its purpose was, and who was behind them, pulling their strings like puppets.

*Step.*

Jin Taekyung suddenly started walking.

The Guild Master of Kronos, the first to realize what that sudden movement meant, swung his war hammer like a bolt of lightning.

No—he tried to swing it.

If not for a voice that suddenly slipped into his ear.

“You’d better stop there, Fabian.”

*Rumble.*

The air quivered.

The Guild Master of Kronos looked at the towering Black man who had risen from his seat, his expression hardening.

“Johnson.”

“It’s been a while. You’ve gotten even more charming with age.”

Magic Johnson gave him a playful wink and flicked his staff toward the war hammer rippling with Aura.

“Whoa. Don’t do anything rash. This is advice from a comrade-in-arms who’s risked his life fighting alongside you.”

“Do you know what your actions mean right now?”

“Of course. So there’s no need to explain it to me. We know exactly where we need to go from here.”

“…We?”

The instant he echoed the word without thinking, he saw the answer with his own eyes.

*Rustle. Thud.*

One after another, people rose from their places quietly, noisily, or with an air of dignity.

The Guild Master of Kronos’s gaze sank as he faced those familiar yet splendid faces.

Starting with Magic Johnson: Chuck Hagel. Faye Chen. Prince Felix.

And then Choi Minwoo, whose symbolic significance as Cheon Taemin’s only blood relative was unmistakable. Finally, even the Stone King, who had been watching the weapons aimed at him with a hard expression, stood up.

*This is bad. It’s already beyond the range Michael predicted.*

But what exceeded his expectations the most was the young man now standing right in front of him.

“Move.”

“I can’t—”

“I said move.”

“……!”

In that moment,

the Guild Master of Kronos felt a chill pierce him to the bone for the first time in a long while.

It was the presence of a young man who hadn’t even lived half as long as he had.

At the same time, the warning he’d heard from Magic Johnson came back to him.

It would be better to stop there. Not to do anything rash.

He understood, too, who that warning had been for.

*Step.*

By the time he came to his senses, it was already too late. The Guild Master of Kronos instinctively shifted to the side, and Jin Taekyung walked on as if that were only natural.

Of the three hundred people packed tightly around them, half had tried to stop him, but soon found themselves moving aside without knowing why. Half of those remaining either watched or surrounded Jin as if to protect him.

And amid the cold air and taut tension, the two finally faced each other again at the center of the round table.

Jin Taekyung and Michael Silbert.

Michael Silbert and Jin Taekyung.

Their gazes met and flared—cold yet fiery, fiery yet cold.

Then came a voice clear enough to pierce everyone’s ears.

“Do you know what consequences your actions and this truth will bring, after what you’ve done here today?”

“Who knows. I don’t know exactly. Maybe a whole lot of assholes will come after me now?”

Jin Taekyung added calmly,

“And the nastiest one of them all is standing right in front of me.”

The muscles in Michael Silbert’s cheek twitched.

From the moment Jin Taekyung had revealed the truth in front of everyone, Michael’s composure had already begun to falter.

But it was fine. It was fine.

The throne was still intact.

Once the vote began, the place where he sat would become the throne.

But Jin Taekyung wouldn’t be fine. Not him.

There was no seat for him anywhere at this round table now.

Soon, there wouldn’t be anywhere in the world for him.

“I’ll tell you one thing for certain. Now that the Stone King’s identity has been revealed, I’m afraid the first vote of our World Hunter Federation will be to expel you permanently.”

“Really? Why?”

“If he truly was unlike any ordinary monster, and you’d told us right away, everyone—including me—would have considered the matter carefully. But it’s too late. After you hid such a grave secret, no one can trust you.”

“Too bad. Go on.”

“Everything will proceed through legal channels. Those involved in this matter will be formally indicted and brought to trial. And if you resist…”

Michael Silbert continued, his voice raised as if to call out to everyone.

“Summary execution.”

A suffocating silence followed.

But the moment he slowly turned his head toward Jin Taekyung, Michael Silbert could hear a thunderous sound echoing through it.

*Thump.*

His heart lurched.

*Thump. Thump-thump.*

His heartbeat quickened. Jin Taekyung’s eyes, curved like crescents, seemed to drive an awl into the middle of his chest.

What was it? Why was it?

Why was that bastard smiling even in a situation like this?

Why?

“There’s one thing I want to ask.”

Suddenly, the world slowed down.

His heart pounded, his pulse trembled, and his five senses, all focused on one person, took in the words that followed.

“What if you hadn’t colluded with a monster, but…”

Michael Silbert swallowed as Jin’s words trailed off. Then a quiet remark shook his world.

“You were already no different from one? What would happen then?”

“……!”

No—it shook everyone’s world.

With a contemptuous gaze fixed on something neither human nor monster, Jin delivered one final line.

“Has the wound on your neck healed, Michael?”

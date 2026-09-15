# Checkpoint Review — 105–109

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

# Chapters 105–109

## Plot

At the Phoenix Inn, Jin Taekyung and Hyuk Mujin subdue six mounted-bandit scouts bearing running-horse tattoos. Wolhwa, the inn’s proprietress, a courtesan, and the Lower District Sect’s Shanxi Branch Leader, explains that Lee Cheonbaek hired mounted bands during the war with the Mount Heng Sword Sect. She proposes accompanying Taekyung to Mount Heng to collect the Lower District Sect’s promised compensation and expand its influence in northern Shanxi. Taekyung accepts after Jin Mukyung’s training damages the inn’s private residence and leaves them unable to pay the resulting bill. Wolhwa cancels her sect’s investigation into Taekyung’s unexplained transformation and orders a gag order.

The group travels toward Mount Heng with Chunsam, a Level 50 First Rate martial artist serving as coachman and bodyguard. At an abandoned Guandi Temple, they encounter human traffickers transporting the Five-Colored Ghosts, former subordinates of Jang Sam who had abandoned banditry but recently turned to theft. Taekyung frees them, and Mukyung cripples the traffickers’ leader, Lee Sam, destroying his dantian. The Five-Colored Ghosts reveal that the Red Wind Band is preparing to leave for Saneum.

A messenger hawk from the Lower District Sect’s Sakju Branch reports that roughly two hundred Red Wind Band members are moving south. Wolhwa interrogates captured mounted bandits lethally, while the group rides day and night toward Mount Heng. Pung Yang, the Red Wind Band Leader, has already destroyed the Mount Heng Sword Sect’s Datong Branch and ordered that no prisoners be taken. The weakened sect, having lost nearly eighty percent of its strength in the war with the Jin Family of Taiyuan, learns that an attack may come within one or two days. As its leaders despair, the main hall doors suddenly explode, marking the attack’s beginning.

## Continuity

- Taekyung, Mukyung, Mujin, and Wolhwa are riding toward the Mount Heng Sword Sect without resting.
- Chunsam is a First Rate Lower District Sect martial artist who served as their carriage driver and bodyguard.
- Wolhwa is the Phoenix Inn’s proprietress, a courtesan, Shanxi Branch Leader, and major information broker.
- The Lower District Sect assisted the Jin Family during the war under a secret compensation pact. Wolhwa intends to collect its compensation and expand into northern Shanxi.
- Wolhwa has stopped investigating Taekyung’s transformation and ordered her organization to keep the matter confidential.
- The Five-Colored Ghosts and surviving mounted bandits are being transported to a nearby Lower District Sect branch.
- The Red Wind Band numbers approximately two hundred and is led by Pung Yang, who places his personal orders above plateau customs.
- Pung Yang’s forces destroyed the Mount Heng Sword Sect’s Datong Branch with no survivors and are moving south toward the sect’s headquarters.
- Mount Heng has lost nearly eighty percent of its strength since the war with the Jin Family. Its attack is expected within one or two days, and its main hall doors have been destroyed.
- Taekyung’s Quest difficulty has risen to Peak.
- Unresolved hooks remain: the identity of the surveillance property near Taekyung’s former home; whether the black Familiar and Kim Gwondong share instructions; Kim Hwajong’s reason for arriving and his current butler position; the Security Team’s final punishment; how Seong Jinho entered the capsule; Mount Heng’s response to the merger and Wolhwa’s compensation; and what follows the destruction of the main hall doors.

## Translation Decisions

- Retain **Familiar**, **Logout**, **Inventory**, **Qi Sense**, and **Fire Wall**.
- Render **마적/마적단** as **mounted bandits/mounted-bandit groups**, **적풍단** as **Red Wind Band**, **적풍단주** as **Red Wind Band Leader**, and **토호단** as **Earth Tiger Band**.
- Render **오색귀** as **Five-Colored Ghosts**, **전서응** as **messenger hawk**, and **관제묘** as **Guandi Temple**.
- Render **추종향** as **tracking scent**, **대동** as **Datong**, **산음** as **Saneum**, **풍양** as **Pung Yang**, and **춘삼** as **Chunsam**.
- Retain **Peak**, **First Rate**, **master beyond First Rate**, and **One Strike** for the established martial ranks and technique.
- Preserve Wolhwa’s addresses **Young Master**, **Young Master Jin**, and **Young Hero Jin**; render **대형** as **Boss**.

## Durable state

{
  "active_continuity": [
    "Taekyung, Mukyung, Mujin, and Wolhwa are riding toward the Mount Heng Sword Sect.",
    "The Five-Colored Ghosts and surviving mounted bandits are being taken to a nearby Lower District Sect branch.",
    "A messenger hawk from the Lower District Sect's Sakju Branch delivered intelligence to Wolhwa.",
    "The Red Wind Band is moving south with approximately two hundred members.",
    "The Red Wind Band has crossed Datong and destroyed the Mount Heng Sword Sect's Datong Branch with no survivors.",
    "Pung Yang is the Red Wind Band Leader and commands his force with ruthless authority.",
    "Chunsam is a First Rate Lower District Sect martial artist who served as the group's carriage driver.",
    "Wolhwa uses lethal interrogation to obtain information from hostile mounted bandits.",
    "The Mount Heng Sword Sect has lost nearly eighty percent of its strength in the war with the Jin Family of Taiyuan.",
    "The Red Wind Band's attack on Mount Heng is expected within one or two days.",
    "The Mount Heng Sword Sect's main hall doors have exploded as the attack begins.",
    "The Quest difficulty has changed to Peak."
  ],
  "continuity_sources": [
    109
  ],
  "open_questions": [
    "Which of the three recently traded properties is being used by the surveillance personnel?",
    "Whether the black Familiar and Kim Gwondong are operating under the same immediate instructions remains unresolved.",
    "Why Kim Hwajong arrived at the confrontation remains unknown.",
    "Why Kim Hwajong now works as a butler despite his former instructor status and exceptional ability remains unexplained.",
    "What final disciplinary action will be taken against the Security Team remains unknown.",
    "How and why Seong Jinho entered the capsule and emerged inside Taekyung's new house remains unknown.",
    "How Lee Seowol and Mount Heng will respond to the merger proposal, and what compensation or territorial concession Wolhwa will receive, remain unresolved.",
    "What will happen inside the Mount Heng Sword Sect's main hall after its doors are destroyed remains unknown."
  ],
  "safe_through": 109,
  "temporary_decisions": [
    "Use mouth-sealing technique for 아가리 봉인술 and keep Fire Wall as the spell name.",
    "Render Im Chunsoo's 자네 as you; 김화종's 춘수 and 교관님 as Chunsoo and Instructor; 1번 훈련생 as Trainee Number One; and 열양공 as heat-yang technique.",
    "Render 원단 as Lunar New Year; 봉황객잔 as Phoenix Inn; 계용옥미갱 and 계용옥미앵 as chicken-and-corn soup; and 곡도 as curved saber.",
    "Render 마적 and 마적단 as mounted bandits and mounted-bandit groups; 적풍단 as Red Wind Band; 적풍단주 as Red Wind Band Leader; and 토호단 as Earth Tiger Band.",
    "Render 초일류 as master beyond First Rate; preserve Wolhwa's Young Master forms for Taekyung and Young Hero Jin for Mukyung; render 관제묘 as Guandi Temple and 흑도 as dark-path figures.",
    "Render 오색귀 as Five-Colored Ghosts, 이삼 as Lee Sam, 전서응 as messenger hawk, and 대형 as Boss.",
    "Render 추종향 as tracking scent, 대동 as Datong, 풍양 as Pung Yang, 춘삼 as Chunsam, 철검대주 as Iron Sword Squad Leader, 대항산검문 as great Mount Heng Sword Sect, and 대동지부 as Datong Branch.",
    "Render 절정 as Peak, 일류 as First Rate, 일격 as One Strike, and 단주 as Leader."
  ],
  "version": 1
}

## Reading copies

## Chapter artifact 105

# Chapter 105

Crack!

The instant my fist sank into that foul-smelling snout, I knew.

The only thing that bastard would be able to eat from now on was chicken-and-corn soup.

Crash! Bang!

The first man shot backward in a straight line and lost consciousness before his body even hit the ground.

Level 31. He was a martial artist at the entry level of First Rate, but he still couldn’t dodge my punch.

“Where the hell do you get off stinking up the place with your breath and ruining my appetite?”

Every sound in the inn stopped.

But only for a moment.

“Gwangsu’s down!”

“You little brat!”

“Kill him!”

Shing, shing, shing!

Five curved sabers were drawn at once. Five pairs of eyes gleamed with killing intent. The inn’s guests scattered with screams.

I suddenly remembered the smell of blood coming from the man who had just fallen.

*Huh. Look at these bastards.*

They were used to killing. I could tell just from the fact that they had started the fight and still hadn’t hesitated to draw their weapons.

“What kind of people are you?”

“The Grim Reaper.”

The answer came at the same time as their attack.

Four curved sabers stabbed straight at my limbs, while the remaining one aimed precisely for my chest.

Whoosh, whoosh, whoosh!

Too slow.

One of the five was First Rate. The other four were Second Rate.

Their confidence in taking me down was impressive, but their feet were slow, and the net of sabers they spread from the front was full of gaps.

“Next time, at least try surrounding someone.”

Along with that friendly advice, I flicked both hands toward them.

For a very brief moment, two daggers summoned from my Inventory cut through the air.

Whoosh!

*Throwing daggers. Is that what they call it in Murim—flying-dagger arts?*

I had never learned it for actual combat, but it didn’t matter. Whether they were hit by the blade or the hilt, a hit was a hit.

Crack! Thud.

Yes, just like that.

One man’s forehead split open against the hilt of a dagger, and he crumpled without even managing to scream.

What about the other one?

Clang!

“What a cheap trick!”

Whether he was lucky or had better eyes than I expected, he had somehow blocked it.

I gave him a wide smile.

“Is that dagger yours?”

“You threw it at me, so what kind of bullshit are you talking about?”

“What an honest child. As a reward, I’ll give you both of them.”

Thud, thud!

“Ghk. But your hands were clearly empty—”

Thud.

“My daggers multiply infinitely.”

It had been a good idea to stop by the armory before leaving the Jin Family of Taiyuan.

I had gone in empty-handed and come out empty-handed, but my Inventory was now filled with dozens of weapons looted as spoils.

“What… what is this?”

It had all happened in the blink of an eye. The remaining three stopped in the middle of their charge, hesitated, and backed away.

“Not coming? Then I’ll go to you.”

“W-Wait, Young Hero! We were rude. We sincerely apologize and will compensate you—”

Look at how quickly they changed tactics.

Just a moment ago, they had been calling me a brat. Now they were calling me Young Hero.

“An apology?”

“Yes, yes!”

“Don’t need it!”

I clenched my fist and charged at them. I didn’t need martial arts to deal with trash like this.

“Damn it, attack!”

Whoosh!

One step to the side.

I dodged the curved saber that came crashing straight down toward the top of my head, then drove a single punch into the exposed side of his body.

Crunch.

Leaving the man who collapsed with a strangled groan behind me, I charged at the next opponent.

Above his head, I saw a System window displaying Level 35.

“You bastard!”

Whoosh!

As befitted a First Rate expert, he had clearly learned a fair amount of martial arts. His movements were clean, and the curved saber was swung with precision toward my vital points.

But…

*All of that is useless before overwhelming strength and speed.*

My level and internal energy were low, but in terms of stats, I far surpassed First Rate. On top of that, I had all the combat experience I had built up in Murim.

This man could never be my opponent.

Crack!

The focus vanished from his eyes. The curved saber slipped from his grip before he could finish his swing.

Clang.

The last man, who had watched everything unfold, was half out of his mind.

“T-The squad leader fell in a single exchange… Who are you?”

“You should exchange names with my fist. Here, this one’s called Right Hand. And you?”

I approached with my right fist clenched. The man swung his curved saber wildly through the air.

“D-Don’t come any closer!”

“You should make a request more politely.”

“Please, don’t come any closer!”

“You really did it.”

Since he had asked so politely, I supposed I had to honor his request.

When I stopped walking, color returned to the man’s face.

“T-Thank you! I’ll live a good life from now on!”

“No need to thank me. And you don’t have to live a good life.”

“Huh?”

“Turning over a new leaf isn’t something that happens so easily. Isn’t that right, Mujin?”

Hyuk Mujin was standing behind the man before I knew it.

“Of course.”

“Hic!”

The man sucked in a startled breath and turned around, but it was already too late.

Hyuk Mujin was in the middle of bringing the wooden chair in his hands down on the top of the man’s head with all his strength.

Crack!

With a heavy thud, the last man collapsed. Hyuk Mujin set the chair down and muttered,

“Thank you, and I’m sorry.”

“What are you thanking those bastards for?”

“There are things.”

That look in his eyes was awfully cocky.

I was wondering whether I should give him a smack after such a long time when Hyuk Mujin, who had been searching through the fallen men’s clothes, tilted his head.

“Huh? Squad Leader, these men are suspicious.”

“What about them?”

“Look at this.”

Hyuk Mujin rolled up one man’s sleeve, revealing a scar that looked as though it had been branded into the flesh.

No, it wasn’t simply a scar.

It looked like…

“A tattoo?”

It was crude and savage, but it was definitely a kind of tattoo.

A running horse.

“Is this the only one with it?”

“I don’t know. I haven’t checked all of them yet.”

“Check the others.”

“Yes, sir.”

Hyuk Mujin gathered the unconscious men in one place and stripped off their shirts.

Their arms, chests, and necks. The locations differed slightly, but every one of them had a tattoo of a horse.

*So they belong to some kind of organization…*

I already knew they weren’t simple thugs. Two of them were First Rate masters, and I couldn’t stop thinking about the word the last man had let slip without meaning to.

*He definitely said captain, didn’t he?*

Martial artists belonging to another sect?

No. Their aura was too rough for that, and their clothing wasn’t uniform.

It was more likely that they belonged to a fairly large group of wandering martial artists.

*A horse tattoo. A horse tattoo…*

Then a word suddenly flashed through my mind.

It was a name I had first heard during the war with the Mount Heng Sword Sect.

“Mounted bandits?”

Someone answered my mutter from somewhere nearby.

“There are dozens of mounted-bandit groups on the northern plateau. It was a great mistake for Lee Cheonbaek to hire them.”

I turned toward the owner of the languid yet alluring voice.

A woman stood on the stairs leading to the second floor, a veil draped across her face.

“Long time no see, our Young Master.”

*Our Young Master?*

The moment I heard those words, I knew who she was.

*Wolhwa.*

It was her.



* * *



Hyuk Mujin and I were led to a guest room on the top floor of the Phoenix Inn.

Calling it a guest room didn’t really do it justice. We had the entire floor to ourselves, so it was more accurate to call it a penthouse.

“It’s my first time bringing a man here. And two of them, no less.”

Wolhwa’s smile, bathed in the soft light, was dazzling.

I had felt it from the moment we first met, but there really was no better example of a femme fatale.

Even though I had met her several times already, my stomach still churned whenever I looked at her.

Hyuk Mujin was beyond saving.

“It’s an honor beyond three lifetimes.”

“……”

Look at that bastard’s unfocused eyes.

He was completely smitten.

Wolhwa gave him a bright smile before turning her gaze toward me.

“Have you been well, Young Master Jin? Ah, I suppose I can’t call you Young Master the way I used to anymore?”

Judging from Wolhwa’s mischievous expression, I could easily guess what she was about to say.

I hurriedly waved my hands.

“Just call me whatever you like. Like before.”

“Hmm. Then how about Young Master Sleeping Dragon?”

“……That’s horrible.”

“Why? Sleeping Dragon of Shanxi sounds wonderful. If you’ve earned that much martial fame at such a young age, you could stand to be a little prouder.”

Sleeping Dragon of Shanxi or Flaming Charisma Taekyung—they were equally terrible.

Seeing my expression, Wolhwa chuckled and put her long-stemmed tobacco pipe to her lips.

“I’m only joking. Anyway, teasing Young Master Jin is so much fun.”

“Excuse me for interrupting.”

Hyuk Mujin had finally regained some of his senses. He looked back and forth between Wolhwa and me.

“May I ask what kind of relationship the two of you have?”

“None of your business.”

It was too embarrassing to explain our relationship in detail.

I cut him off sharply, then glanced at Wolhwa. It was a signal asking her to play along.

She immediately understood and nodded.

“He used to be a regular at my establishment. Not anymore, though.”

“……”

Like hell she did.

Still, it was a little ridiculous for her to hide it now. She had been completely open about it in front of Jin Wikyung and Wipeng.

Hyuk Mujin, meanwhile, seemed only half-convinced by Wolhwa’s answer.

“By ‘establishment,’ do you mean the Phoenix Inn?”

“No. This is just a side business. My real profession is something only a beautiful and charming woman like me can do.”

“Then perhaps…”

“It’s probably what you’re thinking, Young Martial Artist.”

“A pleasure house?”

“Correct.”

Hyuk Mujin’s eyes widened.

“So the proprietress of the Phoenix Inn, whom I had only heard about in rumors, was a courtesan.”

“Young Martial Artist, you should watch your words. It’s unpleasant to hear that from the other side.”

“If I offended you, I apologize. However, your words and behavior don’t exactly appear in a favorable light either.”

The sudden change in his expression caught me even more off guard.

“Hey, what’s with you?”

“Squad Leader—no, Young Master—is a direct descendant of the Jin Family of Taiyuan. Even the most beautiful woman under heaven cannot treat the Young Master so casually. As a retainer of our family, I could not stand by and let it happen.”

“A moment ago, you said it was an honor beyond three lifetimes.”

“……In any case, how could a mere courtesan treat Young Master—”

Smack!

I gave him a satisfying whack on the back of the head and opened my mouth.

“She’s the Shanxi Branch Leader of the Lower District Sect.”

“Whether she’s the Shanxi Branch Leader or not, huh? What?”

“Are your ears clogged? I said she’s the Shanxi Branch Leader of the Lower District Sect. She gave us extremely—very, very—decisive help in the recent war with the Mount Heng Sword Sect.”

“I’m fine, Young Master Jin.”

Wolhwa lowered her eyes sadly.

“I’m only a mere courtesan, after all.”

Hyuk Mujin was silent for a moment before bowing his head.

“Young Lady—no, Branch Leader. I apologize—”

“Then keep your mouth shut.”

“Yes, ma’am.”

Wolhwa let out a quiet laugh.

“You have an interesting subordinate.”

They say the squid is what disgraces the fish market. In the same way, that bastard Mujin was doing all the disgracing for the Jin Family of Taiyuan.

I was too embarrassed to look Wolhwa in the eye.

“……I apologize for all of this.”

“You’re not the one who needs to apologize, Young Master. And he wasn’t entirely wrong.”

Thankfully, she let it slide without a fuss.

After exhaling a stream of smoke, Wolhwa spoke.

“You’re on your way to the Mount Heng Sword Sect, aren’t you?”

“Yes.”

“May I ask what your purpose is?”

“You already know, don’t you?”

She was the greatest source of information in all of Shanxi. There was no need to ask how she knew.

“I wanted Young Master Jin to tell me himself, though. I’m disappointed.”

“Business and personal matters should be kept separate.”

“How cold. Then may I make you a proposal? You can call it a deal, if you prefer.”

“I’ll decide after I hear it.”

Wolhwa tapped the ash from her pipe.

“Let’s go together. To the Mount Heng Sword Sect.”

“What?”

What the hell was she talking about?
## Chapter artifact 106

# Chapter 106

“Let’s go together. To the Mount Heng Sword Sect.”

“What?”

“You heard me, Young Master Jin. I have business at the Mount Heng Sword Sect too.”

“What kind of business?”

“I don’t think I can tell you that. I’m rather clear about keeping business and personal matters separate.”

*Talk about getting paid back tenfold.*

What I had just said had come back to bite me. Wolhwa’s smile deepened as she watched me grow awkward.

“I’m only joking. I happen to have something to collect from the Mount Heng Sword Sect. More precisely, something I’m supposed to receive from the Jin Family of Taiyuan.”

“What… Oh.”

A memory suddenly came to me. Back when the war with the Mount Heng Sword Sect was in full swing, the Jin Family of Taiyuan and the Lower District Sect had made a secret pact.

*Hadn’t we promised to give them ownership of the Mount Heng Sword Sect’s properties and such in exchange for information?*

The Lower District Sect—or rather, Wolhwa—had kept her promise. It was thanks to her help that we had been able to annihilate the Mount Heng Sword Sect’s vanguard in the early days of the war.

The Jin Family of Taiyuan had continued receiving help from the Lower District Sect afterward and had eventually won the war, but that was when the trouble began.

“As you know, Young Master Jin, our position has become rather awkward. We won the war, but we can’t lay our hands on the spoils.”

The strong devouring the weak. That was the law of Murim.

But the appearance of the Head Elder had ruined everything. The moment it came to light that the Jin Family of Taiyuan and the Mount Heng Sword Sect had both been manipulated by him, the justification for claiming the spoils had grown faint.

*So that’s why we’re pursuing a merger.*

Now was the time to put away our swords and negotiate with a brush. Jin Wikyung’s vision was to quietly and amicably absorb the Mount Heng Sword Sect within limits that would keep the world from condemning us.

Wolhwa wanted to receive her reward before that happened.

“If the Mount Heng Sword Sect accepts our proposal, couldn’t you demand your reward then?”

“That would only be possible if the Jin Family of Taiyuan were Shanxi’s hegemon rather than its Alliance Leader. If we tried to snatch things away carelessly in the current situation, the other mid-sized and small sects would withdraw too. And on top of that…”

For a moment, she looked at me with meaningful eyes before shaking her head.

*What was that supposed to mean?*

“And on top of that, what?”

“No, it’s nothing. Anyway, I did receive a proposal from the Lesser Family Head.”

Wolhwa took a puff from her long-stemmed tobacco pipe before continuing.

“He said he would transfer wealth equivalent to what he had promised, or hand over some of the areas managed by the Jin Family of Taiyuan.”

That sounded like a reasonable offer, but it looked different when viewed from the perspective of someone leading an organization rather than acting as an individual.

*She wants to expand her territory.*

Wolhwa’s true nature was neither that of a courtesan nor an innkeeper. She was an information merchant.

There was no doubt that she wanted to use this opportunity to expand the Lower District Sect’s influence into northern Shanxi, where it had been relatively weak because of the Mount Heng Sword Sect’s blockade.

*Jin Wikyung, naturally, wants the Jin Family of Taiyuan to encompass all of Shanxi.*

The Jin Family of Taiyuan had already wielded enormous influence over central and southern Shanxi for a long time. Handing over a few prime areas wouldn’t diminish the influence they had built up until now.

*This is exactly like a redevelopment district.*

The Mount Heng Sword Sect, which had held a firm grip on the north and blocked outside forces from entering, was collapsing. The greenbelt had been lifted and the area had become open for redevelopment, so the tug-of-war between Jin Wikyung and Wolhwa had begun.

*They’re both something else.*

Yesterday’s ally had become today’s competitor.

Once again, I felt that people were never everything they appeared to be.

“So I thought I’d meet our adorable new Sect Leader and collect what I’m owed while I was at it. How about we travel to the Mount Heng Sword Sect together?”

I answered without needing to think any further.

“I’ll have to decline.”

“Wow, aren’t you being a little too decisive? You cut me off without even hearing the terms.”

“As his younger brother, I can’t go around splashing filth on my hyung’s path.”

We weren’t related by blood, but I had long since accepted his existence—and this Murim—as my own.

“Hmm.”

Wolhwa stared at me for a moment before setting her pipe down with a sharp tap.

“All right, then.”

“Ah. Yes.”

I had expected her to tempt me a few more times, but she gave up right away.

Well, at least the conversation had ended quickly. That made things easier for me.

“Then we’ll be going.”

I gave Hyuk Mujin, who was still sitting there with his mouth sealed shut, a light tap and rose from my seat. That was when Wolhwa smiled strangely and spoke.

“Oh, could you tell Young Hero Jin something for me? The old pine in the rear courtyard is expensive, so please be careful with your training.”

This was an inn run by the greatest information merchant in Shanxi. Ever since we entered this place, she had probably seen right through us, down to our innards.

“Sure.”

“And tell me if you need anything. It’s a request from our Young Master Jin, so I have to procure anything you might need.”

She gave me a wink. I merely glanced at her and left the room, only to remember something I had momentarily forgotten.

“Mujin, why do you run your mouth so carelessly?”

Whack! Whack! Whack!

“Argh! Argh! Argh!”

One of us hit, and the other took the hits.

When we returned to the private residence, we found several old pine trees neatly cut down and Jin Mukyung waiting with a satisfied expression.

“There’s a certain satisfaction to cutting.”

“……”

“……”

*One day, I really want to cut that bastard down.*

* * *

The guest room had grown quiet. Wolhwa smoked her long-stemmed tobacco pipe for a long while before finally speaking, long after Jin Taekyung had left.

“Did you look into what I instructed you to investigate?”

A member of the Lower District Sect, who had been waiting outside the guest room, answered in a low voice.

“What you confirmed four days ago is all we have. We’re still gathering additional information, but…”

“Nothing else is going to turn up?”

“It’s unlikely.”

“Unlikely? Then there’s still a chance. Keep digging. I’ll give you plenty of time, so don’t rush. You know that if we provoke the Jin Family of Taiyuan right now, we won’t fare well either.”

“Yes, Branch Leader.”

The Lower District Sect member was about to withdraw when Wolhwa stopped him with one more question.

“A Third Rate wastrel became the Sleeping Dragon of Shanxi in less than two months. What do you think?”

“It’s possible, if the rumors are true.”

“Ah, that.”

Wolhwa let out a short laugh. It was a rumor that had begun spreading after Jin Taekyung defeated Jopil, One Question, One Kill.

According to the rumor, everything Jin Taekyung had shown until now had been an act. In truth, he had learned martial arts since childhood under the full support of the family.

By now, the story had spread throughout Shanxi to the point that there was hardly anyone who hadn’t heard it.

“Do you believe it?”

“It’s ridiculous nonsense. But…”

“People believe it. Not because they’re stupid, but because they have no choice but to believe it. But we’re different.”

Shanxi was already a frontier region that the Central Plains hardly even acknowledged, but the Lower District Sect had continued gathering information there without pause.

When it came to the direct descendants of the Jin Family of Taiyuan, one of Shanxi’s most powerful families, there was no need to mention it. Their only mistake had been failing to accurately assess the Head Elder, who had been active during the chaotic period of war.

But their information on Jin Taekyung was nearly perfect.

“Alcohol, women, gambling. He had been lazy since childhood and obsessed with nothing but having fun. He was so out of place that you would have wondered whether someone like him had ever existed in the history of the Jin Family of Taiyuan.”

“That was the first order you gave after taking office as Branch Leader two years ago.”

“That’s right. Monitor the entire situation in Shanxi. And investigate Jin Taekyung in depth.”

Talent was normally passed down through the generations. The direct descendants of the Jin Family of Taiyuan had possessed exceptional martial talent for generations, and the current Family Head and his two sons, all regarded as eccentrics, were no exception.

Jin Taekyung’s existence stood out so sharply among them that he seemed almost alien. That was why the Lower District Sect had begun its investigation.

“The result was anticlimactic.”

“He was exactly what he appeared to be.”

Other than having slightly superior bones and meridians, perhaps thanks to his family bloodline, there had been nothing special about him.

“Did we miss something back then?”

“He was the kind of bastard who spent the night at a pleasure house every other day. Martial arts already demands more time than a person has, even if they cut back on sleep.”

“I know. I know very well.”

Wolhwa had cultivated her martial arts to a fairly mature stage of the First Rate realm. There was no way she didn’t understand that.

She continued drawing on her pipe, exhaling long breaths in frustration before finally letting out a deep sigh.

“In the end, there’s only one answer.”

“That’s right.”

Jin Taekyung had gone from Third Rate to a master beyond First Rate in a little over two months. Wolhwa was dumbfounded by the conclusion she had reached herself, but there was nothing she could do about it.

“Cancel the order I gave earlier. Don’t ask about him anymore, and don’t try to find out anything else. Issue a gag order so that no one even mentions him.”

“Yes, Branch Leader. I’ll make sure they understand.”

“Oh, and one more thing. I’ll be leaving early tomorrow, so prepare everything.”

“Who are you planning to take with you?”

“No one. I’ll go alone.”

“Branch Leader, that…”

“It’s an order.”

“Understood.”

Once her subordinate withdrew, silence settled over the guest room. Wolhwa shook the completely burned tobacco leaves from her pipe and thought.

*Jin Taekyung.*

If everything he had done until now was true, then the northern interests she was supposed to extract from the Mount Heng Sword Sect were nothing.

*Has anyone in all history ever grown this quickly?*

Her gaze, fixed on the place where Jin Taekyung had been sitting, sank into deep contemplation.

* * *

The next morning.

I began to feel that something had gone wrong after meeting the person in charge of the private residence.

“The lodging fee is twenty-five nyang, the food comes to five nyang, and the property damage fee is fifty nyang. The total is eighty silver nyang.”

Hyuk Mujin, who had been rejoicing yesterday over emptying the pockets of those mounted bandits, gaped.

“Property damage? Fifty silver nyang?”

“When I went to the rear courtyard, I found that five old pine trees had fallen.”

They were the trees Wolhwa had said were expensive.

Hyuk Mujin and I turned our heads at the same time. Jin Mukyung, whose eyes met ours, flinched before opening his mouth.

“I got carried away while practicing my swordsmanship.”

“……No, fuck. If you get carried away, does that mean you can cut down anything in your way? Huh?”

“Hoooo.”

Hyuk Mujin couldn’t say anything. He merely kept letting out furious sighs.

At a glance, it was obvious that the bill exceeded the amount we had on hand. If it had only been a little over, we might have been able to talk things out and find a compromise…

“Mujin, how much money do you have right now?”

“Forty nyang.”

*To hell with a compromise. We’re nowhere close.*

“Could we put it on credit?”

That was the exact moment the kind smile around the private-residence manager’s lips disappeared.

“Young Master Jin, what are you doing here?”

A beautiful woman in a light, flowing palace-style dress was approaching us.

Wolhwa’s appearance was nothing short of a lifeline.

I felt bad about turning down her proposal so decisively the night before, but this was no time to be picky.

“Well, you see…”

When I explained the situation, Wolhwa’s eyes grew round.

“Eighty nyang? That can’t be right.”

“Exactly. I knew something was wrong.”

“Give me that.”

She took the bamboo slip from the manager and began to read.

The deeper her frown grew, the clearer it seemed that the arithmetic had been badly botched.

*Knew it.*

At last, Wolhwa finished reading the bamboo slip. A chill entered her voice.

“Are you not doing your job properly?”

“I-I’m sorry.”

“Who do you think these gentlemen are, to dare pull this kind of stunt? Write the prices correctly.”

Hyuk Mujin whispered in a small voice.

“What a relief.”

“Yeah. We almost had to wash dishes before leaving.”

“What kind of hardship is this because of the Second Young Master?”

“Don’t even mention that man. Just hearing about him gives me cancer.”

“What’s cancer?”

“……It’s something bad.”

Meanwhile, the manager revised the prices while sweating profusely. Then he bent deeply at the waist and apologized to us.

“I’m sorry. I was thoughtless and committed a grave discourtesy.”

Hyuk Mujin accepted the apology with an arrogant air.

“Don’t do that again. You have to know who you’re dealing with before pulling a prank. So how much is it?”

“One hundred and five nyang, along with twenty-three iron coins.”

“……”

“……”

*What the hell? Is this a dream?*

My head turned toward Wolhwa of its own accord.

“What is that supposed to mean?”

“He arbitrarily lowered the price because you were my acquaintances. How dare he take the young masters of the Jin Family of Taiyuan for fools? Apologize to them again.”

“I’m sorry for failing to recognize your identities!”

“But…”

I asked in a thoroughly choked voice.

“We can put it on credit, right? Of course.”

“No, you can’t. Of course not. We haven’t allowed that even once in the past two years.”

“How about making an exception and setting a precedent this time?”

“I don’t have any plans to do that yet. You’ll have to aim for the next opportunity.”

Wolhwa added with a bright smile,

“Was there something else you wanted to say?”

“……M-Mount Heng.”

“What was that?”

I squeezed my eyes shut and continued.

“Would you like to come with us to the Mount Heng Sword Sect?”

“Wow, I’d love to.”

*That hateful smile.*

At Wolhwa’s gesture, the manager snatched up the bamboo slip and vanished at the speed of light.

“We won’t have to worry about travel expenses anymore.”

While Hyuk Mujin was the sort of person who simply accepted reality, someone else was shouting vehement opposition.

“Nonsense! How can you bring a woman along while carrying out a family mission?”

“Then stay here and wash dishes.”

“……”

“Who here cut down the old pine trees? Raise your hand.”

Jin Mukyung didn’t raise his hand. Wolhwa slightly lifted the hem of her skirt and greeted him.

“Please take good care of me, Young Hero Jin.”
## Chapter artifact 107

# Chapter 107

The four-horse carriage moved smoothly toward its destination. Even though it was the same carriage pulled by the same horses as yesterday, the ride was on an entirely different level.

The driver had been replaced.

Hyuk Mujin, who had finally escaped the driver’s seat and settled beside me, said with a relaxed expression,

“People really must be born with different talents. I’m hopeless at driving a carriage.”

*What a load of crap.*

He was someone Wolhwa, the Lower District Sect’s Shanxi Branch Leader, had brought with her. Naturally, there was no way he was an ordinary coachman.

The man quietly holding the reins was a Level 50 First Rate martial artist. A coachman and a bodyguard. The picture fit perfectly.

“Mujin.”

“Yes?”

“Please just travel quietly. Then you’ll at least do okay.”

“……Why am I always the one you pick on?”

“Because you’re always spouting nonsense, you idiot.”

Wolhwa, who was sitting across from us and watching, let out a quiet laugh.

“You two seem very comfortable with each other.”

“He’s just rude.”

“Rude? I wasn’t going to say this, but I’m two years older than the squad leader. My friends have children.”

“You don’t.”

“Well, no. That’s true.”

“And even if you were twenty-two, you’d still be younger than me. Anyway, you’re younger.”

“What are you talking about? Even the stray dogs of Shanxi Province know that the squad leader is barely twenty.”

“If you don’t believe me, then let’s have a match.”

“……Since there are other people here, I’ll stop at this point.”

Wolhwa smiled brightly at Hyuk Mujin’s ugly excuse.

“Oh, I don’t mind. Though I can’t speak for Young Hero Jin.”

Everyone’s eyes naturally turned toward one person.

Jin Mukyung, who had kept his mouth tightly shut until then, flinched and opened it.

“I—I don’t mind.”

“……?”

*What the hell? Did he just stutter?*

I stared at him with my eyes wide open at the unexpected response. Jin Mukyung subtly looked away.

*Oh, this is getting worse.*

He wasn’t usually like this. Normally, he would have glared and asked what I was staring at.

I asked him sincerely,

“Are you sick?”

“……Not at all.”

“When you’re talking to someone, you should look them in the eye.”

“……Be quiet. Don’t talk to me.”

He was acting really strange today.

There was no way a Peak master like him had gotten motion sickness.

He had been full of energy until this morning, but now he was clearly not himself.

*Come to think of it, he seems to have been like this ever since we got into the carriage.*

Just as I was narrowing my eyes and watching Jin Mukyung—

*Poke, poke.*

Hyuk Mujin nudged me in the side and whispered so quietly that only I could hear him.

“Look at the Second Young Master.”

“Look at what…… Ah.”

Only after hearing Hyuk Mujin did I notice the bizarre sight.

I couldn’t believe I hadn’t noticed it until now.

*What is he doing?*

The four-horse carriage brought from the Jin Family of Taiyuan was quite luxurious. The inside was about the size of an ordinary room, and the seats were spacious too. It could have carried twice as many people as we had without any trouble.

And yet…

*Why is he sitting like that?*

Jin Mukyung had ignored the spacious seats and folded himself into the corner at the very end of the carriage.

No, “folded” didn’t quite cover it. He was practically compressed.

*What is this, Platform Nine and Three-Quarters?*

Was he attending a magic school instead of Heaven’s Gate Temple?

I wasn’t the only one watching this strange behavior.

“Young Hero Jin, you look very uncomfortable. Why don’t you come over here? There’s plenty of room.”

Jin Mukyung’s body went rigid at the sound of Wolhwa’s alluring voice.

A creaking reply came a moment later.

“I—I’m fine.”

“……”

He didn’t look fine at all.

I whispered quietly to Hyuk Mujin, whose expression was similar to mine.

“You think he’s acting strange too, right?”

“It’s more than strange.”

“Yeah. I thought so too.”

We exchanged meaningful glances.

“My goodness. Who could have imagined this?”

“Exactly. Who knew the Heaven Shaking Sword was so shy around people?”

“That’s exactly what I mean…… Huh?”

“Why are you reacting like that? You shouldn’t criticize someone’s personality. If there are thick-skinned guys like me, then there can be timid people too.”

“No, wait. Just wait a moment.”

Hyuk Mujin stumbled over his words.

“What exactly are you talking about?”

“Obviously, Jin Mukyung……”

An eerie voice suddenly cut in.

“Shut up.”

No matter how spacious the carriage was, everyone inside could hear everything.

Under Jin Mukyung’s murderous glare, Hyuk Mujin and I shut our mouths at the same time.

Wolhwa was the one who changed the grim atmosphere.

“Where are my manners? I haven’t even properly introduced myself yet. I’m Wolhwa, Shanxi Branch Leader of the Lower District Sect.”

“……I am Jin Mukyung of the Jin Family of Taiyuan.”

“What a dull reaction. That Young Master Jin over there was extremely surprised when he first heard about my identity.”

“I heard the general details from him. I also heard that you did a great deal for our family.”

Jin Mukyung politely clasped his hands.

“I realize this is late, but allow me to express my thanks.”

“Not at all. It was a fair trade.”

Wolhwa smoothly added,

“Though I haven’t received the proper compensation yet.”

“Our family will not forget the Lower District Sect’s goodwill.”

His behavior and speech were still awkward beyond belief, but he was doing much better than when they had first met.

Looking at the handsome man and beautiful woman sitting together like a picture, Hyuk Mujin exclaimed,

“A promising young martial arts master and a peerless beauty… Whew, just looking at them makes my heart race. Don’t you agree?”

I turned my head away and pretended not to hear him.

Judging by the killing intent prickling my skin, Hyuk Mujin’s heart wouldn’t be racing for much longer.

* * *

Winter days were short-tempered.

How long had we traveled along the mountain road? The sun quickly set, and darkness descended. The carriage stopped four hours later, around midnight.

“We’ve arrived.”

The first thing I saw after stepping out of the carriage was a moderately sized wooden building.

The moment I stepped inside, I felt a chill in the air. A statue shaped in the likeness of a person looked down at us with solemn dignity.

*What did they call places like this again?*

*Oh, right. A shrine.*

I had heard that it was a place where the spirit tablets of the dead were kept and memorial rites were performed.

The Guandi Temples that appeared so often in martial arts novels came to mind. I looked closely at the statue, but I couldn’t tell who it represented.

“It’s a shrine that was abandoned after a famine several years ago, though it seems local commoners still come here from time to time.”

Just as Wolhwa had said, the inside of the shrine was empty, but traces of human presence remained. For example, there were footprints pressed into the dust-covered floor.

“I’ll prepare the place.”

At the words of the coachman and bodyguard, whom I assumed was a member of the Lower District Sect, we went outside the shrine.

More precisely, one of us was dragged out by someone.

“Follow me.”

“Gah! Squad Leader! Squad Leader!”

I ignored Hyuk Mujin as Jin Mukyung dragged him away by the collar and looked up at the sky.

*The moon is awfully bright tonight.*

“What are you doing?”

“As you can see.”

Wolhwa smiled faintly.

“You seem to enjoy looking at the scenery.”

“I’ve been starting to enjoy it lately.”

The only scenery available in the modern world was a night view seen from some high place. Even that consisted of sad lights created by office workers working overtime.

*This is real scenery.*

There were no dense forests of skyscrapers, no apartment complexes, and no factories.

In place of asphalt roads, damp dirt paths and crisp air filled the entire world.

*Living in a place like this would be genuinely healing.*

The problem was that it was also an easy place to get killed.

Somehow, people were more frightening here than monsters.

I didn’t even need to go as far as the Head Elder or Jopil. What had happened at the Phoenix Inn just yesterday was enough.

“Oh, right. What happened to those guys?”

“If you mean the mounted bandits from the Red Wind Band, they’ve been detained. Of course, we had to call a physician first.”

I’d beaten the shit out of them, so of course they’d needed treatment.

But there was another word that caught my attention more than that.

“The Red Wind Band?”

“They’re a rising power from the plateau. They’re fairly large, and more than anything, the leader of the Red Wind Band is said to possess formidable martial arts.”

The Northern Plateau.

I had first learned of that place through the map during the war with the Mount Heng Sword Sect.

One thing struck me as strange: the plateau was a considerable distance from Honju, where the Phoenix Inn was located. As far as I knew, it took more than a week even if one rode day and night.

“How did people like that end up all the way here?”

“Toward the end of the war, Lee Cheonbaek hired countless wandering martial artists and mounted-bandit groups. Many of them met their end at Eight Spring Gorge, but some survived and fled.”

“So the Red Wind Band was among them?”

Wolhwa shook her head.

“The leader of the Red Wind Band…… He was quicker-witted than I expected.”

“What do you mean?”

“He watched the situation until the very end. He kept a close eye on Eight Spring Gorge from only four hours away, then turned his horse around when he heard the outcome of the battle.”

“With the two hundred subordinates who followed him.”

Two hundred people.

What would have happened if the Red Wind Band had joined the battle at Eight Spring Gorge that day? There would have been an enormous number of casualties, and it might even have affected the outcome of the battle.

“We were lucky.”

“We were. For the Mount Heng Sword Sect, it was incredibly unlucky.”

Wolhwa continued as she packed tobacco into her long-stemmed pipe.

“The Red Wind Band headed north immediately. They targeted the Mount Heng Sword Sect’s main base after most of its forces had withdrawn.”

“……Huh.”

They were natural-born plunderers.

The moment the tide of the war turned, they headed north and bit into the throat of the Mount Heng Sword Sect, whose main forces had already withdrawn.

They had preserved their forces by not participating in the battle, and they must have gotten plenty of rest as well. Their condition would have been at its peak.

“Young Master Jin, you heard what happened, didn’t you?”

“Yes.”

The fierce battle that continued for two days ended with the Mount Heng Sword Sect’s victory.

It also left behind the death of the Young Sect Leader, who was supposed to succeed his father.

“But the rumors I heard said that wandering martial artists and mounted bandits were mixed together.”

“A tiger doesn’t become a dog just because it has lost its teeth. The wandering martial artists the leader of the Red Wind Band drew in were fairly numerous as well. They would have been perfect for use as shields.”

*Tap, tap.*

Wolhwa took out a fire starter, lit it, and drew on her long-stemmed pipe.

“The mounted bandits Young Master Jin defeated were probably the ones who fled at that time. Even if the Red Wind Band is unusually disciplined for a mounted-bandit group, it doesn’t mean they have no deserters at all. I’m not sure what they were doing in Honju, though.”

“Deserters……”

“That’s why things have been chaotic around here lately. Wandering martial artists, bandits, mounted bandits, and even dark-path figures are starting to raise their heads, while the Mount Heng Sword Sect’s strength has been reduced to almost nothing.”

“They’ll have no choice but to accept our proposal.”

Wolhwa smiled demurely.

“To be precise, it isn’t *our* proposal. It’s the Jin Family of Taiyuan’s, isn’t it? Still, from my perspective, this is indeed a good time to pressure the new Sect Leader.”

“By the way……”

“Yes?”

“Do commoners really come to this shrine in weather like this?”

“Of course not. Hunters, perhaps. Why do you ask all of a sudden?”

I pointed toward the mountain path.

Through the thin snowstorm that had begun to swirl, I could see torches climbing toward us.
## Chapter artifact 108

# Chapter 108

*Hunters?*

Wolhwa’s guess was only half right. They were hunters, all right—but the uninvited guests were something more special and far more vicious.

“Move it, you bastards.”

“Who can do anything with men as scrawny as you?”

There were ten of them in all. Every one had a rough-looking face and was armed with a weapon. At the front of their group, prisoners tied together with rope like a string of dried fish staggered along.

*Thud! Thud-thud!*

“Ugh, Boss!”

“We’re coming, we’re coming, so please stop already…”

“Huh, stop? These bastards still haven’t come to their senses.”

“Hey, take it easy. If you break something, their price drops. They’re small to begin with, so it looks like we won’t get full value for them.”

“We should get a decent price if we sell them to a circus troupe. Let’s hurry inside and have a drink.”

“Ah, my mouth waters just thinking about it… But what’s that?”

The human hunters came to an abrupt stop. Their eyes, which had been fixed on the four-horse carriage parked in front of the shrine, slowly shifted to the side.

At the end of their gazes stood Wolhwa and me.

“…Who are you?”

I stepped forward at the question from the man who appeared to be their leader.

“Just a traveler passing through.”

“A traveler. It’s dangerous to be wandering around at a time like this.”

The gleam in his eyes told me he was a dangerous man.

Of course, at Level 25, he didn’t even qualify as a threat to me.

“Wow, a four-horse carriage and a gorgeous woman. You must be a Young Master from a wealthy family, huh?”

If he had come closer to inspect it, he could have seen the crest of the Jin Family of Taiyuan carved into the carriage. But it was pitch-black outside, and he didn’t possess particularly sharp eyesight.

“I’m not from a poor family.”

“Well now. You’ve been awfully informal with me from the start.”

The leader licked his split lips. He seemed to be getting irritated, but he still hadn’t let down his guard around me.

“Whatever. This is a place we’ve been staying in for several days… What are you going to do?”

“Do about what?”

“What do you think? If you show us a little sincerity, we might let you have the place.”

“Anyone listening would think you owned this shrine.”

“It’s abandoned. Doesn’t that mean whoever claims it first owns it?”

“Then go get a certified property document.”

“What?”

The leader turned toward his men with a bewildered expression. Naturally. They had probably never heard the term in their lives. But it wasn’t as though any of them would know what it meant.

I clicked my tongue at the men whispering among themselves about the certified property document.

“If you can’t prove it, then leave quietly. And release the people you’ve tied up.”

“…You’re crossing the line. Are you waiting for bodyguards?”

“I don’t have any.”

“Then what are you relying on?”

“Me.”

The leader’s gaze shifted to my two empty hands.

“Without even a weapon?”

“People at your level? My fists are enough.”

“Looks like the Young Master learned a move or two somewhere… But aren’t you taking Murim a little too lightly?”

“Murim isn’t something to laugh at. You are.”

The moment I stepped toward the brightly burning torch, the prisoners who had been quietly restrained began screaming.

“Wh-what?”

“Boss! Boss!”

“You bastards gone crazy? Shut your mouths!”

The men in the rear drew daggers and held them to the prisoners’ throats in response to their violent reaction. The leader stared at me with wary eyes.

“Do you know them?”

“No. I’m seeing them for the first time in my life.”

Their sudden reaction had even caught me off guard. And why were they suddenly calling me Boss?

“Bosss! It’s me! It’s us!”

“These men seem to know you.”

“They’re just asking me to save them… Huh?”

I looked closely at the prisoners. They were all short as children and had uniformly ugly faces. They looked vaguely familiar.

*Is it because their body shapes resemble goblins?*

Wait. Goblins?

A memory from long ago suddenly came to mind. No, it wasn’t actually that long ago. It had happened only a few months earlier, during the tutorial Quest.

“Don’t tell me… You were with the Heavenly Axe?”

The prisoners—or rather, the Five-Colored Ghosts[^1] who had once been Jang Sam the Heavenly Axe’s subordinates—nodded frantically.

“That’s us!”

“Boss! Please save us!”

I never expected to run into these bastards here. As I stood there dumbfounded, Wolhwa, who had been watching the situation from behind, asked,

“Are these people acquaintances of Young Master Jin?”

“We’ve met before, at least.”

Human traffickers and bandits. It was hard to say which was worse.

Until a moment ago, I had been thinking of saving them. Now I was having second thoughts.

“Bosssss!”

“Are you planning to abandon us?”

“We quit being bandits after that day and have lived good lives ever since!”

“…”

Their ability to read the situation was almost supernatural. No wonder. They had surrendered immediately when the Heavenly Axe died, after all.

“Are you going to save them?”

“Tsk. I think we have to, at least.”

They said they had become new men after that day, and it felt wrong to leave them like this. More importantly, former bandits were far better than active human traffickers.

The leader, who had overheard our conversation, interrupted with a growl.

“Save them? You?”

“You heard the whole thing. Why ask again? You must live a tiring life.”

“You little shit, I’ve been letting you run your mouth, but…”

*Clang!*

The leader leveled his spear at me, and his men drew their weapons as well. Wolhwa clung to my side with a deliberately frightened expression.

“Oh my, I’m scared. You have to protect me, don’t you?”

Her moist eyes stirred a man’s protective instinct. Her expression was pleading.

To someone who knew Wolhwa’s true nature, it was an absurd sight. But the men swallowed hard.

“There’s one more reason I have to kill you.”

At the leader’s lecherous gaze, Wolhwa let out a shriek.

“Oh no, oh no! This maiden is so scared!”

“Ho ho, don’t be so frightened. Though I may have lived a rough life, you’ll soon learn that I’m a man with a heart as soft as silk. In a little while, we can have a conversation with our bodies.”

“Before that, deal with me.”

I needed to rip that filthy mouth open so he would never say anything like that again.

I strode toward him, then suddenly stopped. Seeing that, the leader burst out laughing.

“What’s wrong? Are you scared now that we’re actually going to fight? But it’s already too late.”

“Yeah. You’re really screwed.”

“…What?”

I gave the bewildered man a broad smile.

“I said you’re fucked, asshole.”

The moment I finished speaking, the ground shook, and a powerful wind whipped through the area.

*Boom—whoosh!*

It lasted no more than an instant.

The figure that swept past Wolhwa and me at terrifying speed was already standing in front of the leader.

“Say that again.”

Jin Mukyung.

An overwhelming wave of qi poured from his entire body and crushed the entire scene. The leader’s face turned deathly pale, and his hands began to tremble.

“F-forgive me. Please…”

The cold voice answered.

“You’re far too late.”

* * *

Perhaps Jin Mukyung was the greatest pacifist among us. In just over ten seconds, he had put an end to all the unnecessary fighting that would have followed.

“S-surrender! We surrender!”

“Please spare us! Please, just spare our lives…”

Their faces were frozen with terror. Everyone’s legs gave out, and they collapsed where they stood. Someone’s urine trickled down the hill.

The Five-Colored Ghosts were no different.

“Quiet.”

Jin Mukyung wiped the blood from his face and tossed out a single word. A deathly silence descended.

Hyuk Mujin, one eye bruised deep blue, whispered to me,

“Am I actually alive right now?”

“Yeah. Your breath against my ear is giving me goose bumps, so move away.”

“Just a moment ago, I was thinking, *How can someone get beaten like a dog this badly?* But now…”

*Gulp.*

Hyuk Mujin swallowed dryly, his gaze fixed on the fallen leader.

“Hng… Hng…”

With all four limbs broken and his dantian destroyed, the man struggled for breath. If he received proper care, he might be able to walk again, but his life as a martial artist was over.

The Level window I sensed through Qi Sense was proof.

> **System**
>
> **Level 2 — Lee Sam**

*The dung flies the watchers used as Familiars were Level 1, if I remember correctly.*

The culprit who had turned a Level 25 martial artist who had once been close to First Rate into a living corpse had been sneaking glances in our direction for a while.

“Captain, please save me. I think the Second Young Master is still short on blood.”

“Stop talking nonsense and move that guy somewhere suitable. He’ll die if you leave him like that.”

“Isn’t he a bastard who deserves to die? They were selling perfectly innocent commoners.”

“Even so, move him. He’s still alive.”

One of the greatest sources of dissonance I had felt while moving between Murim and the modern world was the issue of killing people.

For twenty-seven years, I had lived in a society where law and order existed.

I had trained to kill enemies with bladed weapons, but my targets had been monsters, not living humans.

*I was sure that was the case…*

Now I couldn’t even remember how many people I had killed. Even when I realized that the enemies who had died by my hand might have been real people rather than NPCs, I hadn’t felt particularly guilty.

*They were enemies. They were trying to kill me too.*

I didn’t know whether it was because I had lived as a Hunter or because I had grown accustomed to Murim’s ways. I was only surprised by my own numbness and the simplicity of my self-justification.

*For now, maybe this much is okay.*

I was living in two entirely different worlds. This wasn’t a situation where I had the leisure to put on an awkward act as a Buddhist.

Shaking off the thoughts clinging to me, I approached the men cowering on the ground.

“Eek!”

“Uaaagh! Save me, Boss!”

“These guys cause a commotion even when I’m trying to save them. Hold still.”

I untied the ropes, and the Five-Colored Ghosts were free. They stood on trembling legs.

“Th-thank you.”

“We’ll regard you as our Benefactor for the rest of our lives!”

“Like hell you will. Anyway, how did you end up getting caught by men like these? All five of you at once?”

The Five-Colored Ghosts were small, but they were grown men, at least in name. They had been strong enough to commit banditry alongside the Heavenly Axe.

“Um, well…”

“…?”

What was wrong with these guys?

Sensing something strange in their hesitation, I grabbed the nearest human trafficker by the collar and hauled him up.

“How did you catch these men?”

“We caught them trying to steal our money pouches in the marketplace.”

“…”

What the hell, these Ten-Colored Ghosts. I thought they had quit being bandits and might have taken up farming, but they had only changed occupations?

“Explain yourselves.”

Under my sharp gaze, the five men rolled their eyes back and forth.

“W-well…”

“Boss, people like us only know how to do this.”

“Even so, we only started recently!”

“We tried to work honestly, but things didn’t go very well… We said we’d pull just one job and get out, but then…”

“If we’d known they were mounted bandits, we wouldn’t have touched them. We’re victims too. Boss, please forgive us just this once!”

As I wondered what to do with these men, a familiar word made me pause.

“What did you say?”

“We’ll live honestly if you forgive us just one more time!”

“No, not that. What did they say?”

“Ah, do you mean the mounted-bandit group?”

“Yes. That.”

“We only heard after we were captured. Some bunch of ruffians were throwing silver around at a pleasure house, so we followed them… But they turned out to be members of the Red Wind Band, infamous for their viciousness even among mounted bandits.”

“The Red Wind Band? Are you sure?”

“Yes. I heard it clearly with my own ears. Didn’t I?”

The others began eagerly adding their own pieces.

“They said they were leaving as soon as dawn broke tomorrow.”

“They said they’d have to travel nonstop to reach Saneum. They were even worried that they might lose their heads if they arrived late.”

“So that’s how it is.”

Yesterday and today.

It was already an uncanny coincidence that the mounted bandits I had encountered two days in a row happened to belong to the Red Wind Band. On top of that, Saneum was close to Eung-hyeon, where the Mount Heng Sword Sect’s headquarters was located.

“Are these men telling the truth?”

The human trafficker held by the collar in my right hand—or rather, the mounted bandit from the Red Wind Band—nodded with a trembling head.

That was when it happened.

*Shriek!*

A hawk landed in front of the shrine with a sharp cry. A small cylinder tied to its ankle caught my eye.

*A messenger hawk.*

This was getting strange.

[^1]: A nickname meaning “Five-Colored Ghosts.”
## Chapter artifact 109

# Chapter 109

A messenger hawk.

I’d heard the Jin Family of Taiyuan had only two of them. They were messenger birds, but difficult to train, so they were used only to deliver important information…

*Who sent it?*

Just as I was about to approach the messenger hawk, Wolhwa called out to me.

“You’d better keep your distance. It’s a very wary bird. If Young Master Jin tries to catch it, it’ll fly away.”

“Ah, could it be?”

“It’s a messenger hawk sent from our sect. It was trained to follow a specific tracking scent.”

Wolhwa pulled a small pouch from her robes and shook it. The messenger hawk cautiously approached and rubbed its beak against it.

In that moment, a Lower District Sect member who had somehow already slipped outside untied the cylinder from the hawk’s ankle.

“Where’s it from?”

“A letter sent yesterday from the Sakju Branch to the Branch Leader.”

“Give it to me.”

Wolhwa accepted the letter and read it. Her expression turned complicated.

It took a while before her tightly closed lips finally parted.

“The Red Wind Band Leader… He’s more than I expected.”

“Is this about the Red Wind Band again?”

Wolhwa gave a small nod and handed me the letter.

There was no reason to refuse when she was telling me to read it. Jin Mukyung and Hyuk Mujin, who had been hesitating nearby, cautiously leaned in as well.



The Red Wind Band is moving south across the plateau. Their numbers are estimated at approximately two hundred.



The short line made its meaning clear.

“They’re planning to attack the Mount Heng Sword Sect again.”

“There’s no doubt about it. This news is already a day old, so they must have narrowed the distance by that much—or more.”

We were currently a day and a half away from the Mount Heng Sword Sect.

As a mounted-bandit group, they would be advancing toward their destination with exceptional mobility.

“Unfortunately, our branch doesn’t have a proper intelligence network in the northern region. The one fortunate thing is…”

Wolhwa’s gaze shifted toward the mounted bandits of the Red Wind Band. They had lost the will to fight long ago, and flinched as they lowered their heads.

“We have valuable sources of information right here. I don’t know whether they have any useful information, though.”

After looking over the mounted bandits, she suddenly pointed at one of them.

“You. Stand up.”

“……M-me?”

The man rose with a thoroughly terrified expression. He was younger than I expected. The youngest and weakest of the mounted bandits, he couldn’t even meet Wolhwa’s gaze.

“How old are you?”

“I-I passed twenty this year.”

“Twenty? You’re young. Then again, being young doesn’t stop someone from becoming a mounted bandit.”

“I’m not a mounted bandit! I only became a wandering martial artist recently, but then they said they’d give me a big cut, so I…”

“Ah, so you’re one of the wandering martial artists the Red Wind Band Leader gathered for the last attack?”

“Y-yes! I’ll tell you everything I know!”

“No, it’s all right.”

“Pardon?”

“You don’t look like you know much anyway. What would be the point? Isn’t that right, Chunsam?”

The Lower District Sect member who had silently played the part of our carriage driver until now.

Instead of answering, he pulled a small knife from his robes and drove it into the young man’s chest.

*Thunk—*

A First Rate martial artist’s fast, precise One Strike split the young man’s heart. He opened and closed his mouth soundlessly before collapsing like a puppet with its strings cut.

*Thud.*

A frigid silence pressed down on the scene. While the mounted bandits stared in horror and fear, Wolhwa’s slender finger moved once more.

“You.”

“I-I’ll talk! I’ll tell you everything! I’ve been with the Red Wind Band for a year…”

“Chunsam.”

*Whoosh! Slash!*

“Grrk… Gurg…”

The mounted bandit staggered backward, making a wet, blood-choked sound. He tried to cover his gaping throat, but couldn’t stop the fountain of blood spraying between his fingers.

“You only need to remember two things.”

From head to toe, Wolhwa was covered in crimson blood. She continued in a dry tone.

“Answer only what you’re asked, and tell the truth exactly as it is.”

“……!”

In mere moments, we learned everything there was to know about the Red Wind Band.



* * *

Once we learned that every second mattered, we abandoned the carriage and each chose a horse. Me, Jin Mukyung, Hyuk Mujin, and Wolhwa.

The Lower District Sect member would take the Five-Colored Ghosts and the surviving mounted bandits to a nearby Lower District Sect branch and report what had happened.

“Was that too cruel?”

Wolhwa asked as she lifted a saddle onto her horse. I scratched my chin.

“To be honest, I was a little surprised.”

I had temporarily forgotten because I had only ever seen her relaxed and playful. She was a martial artist too.

*And an experienced one at that.*

How old was Wolhwa, anyway?

I’d never asked, so I didn’t know for sure, but she couldn’t have been over thirty.

To become the Branch Leader overseeing all of Shanxi at such a young age, she had to possess the decisiveness to match the position.

*Cruel, but effective.*

She had killed two people without hesitation. Just as casually as swatting flies.

Jin Mukyung’s display against the leader must have terrified the mounted bandits, but the fear of death was even greater.

Driven to the edge of a cliff, they had no choice but to pour out information desperately.

“I think I would’ve spilled everything too.”

“I’m saying this in case Young Master Jin gets the wrong idea, but I don’t enjoy killing people. They weren’t innocent commoners, either… Ah, this bastard’s blood just won’t stop, even when I wipe it.”

The blood streaming down her belonged to the second mounted bandit she had killed.

As she wrinkled her nose, someone held out a piece of cloth to her.

“U-use this to wipe it off.”

“Oh my.”

“Huh?”

“Hmm.”

At the reactions from Wolhwa, me, and Hyuk Mujin, Jin Mukyung cleared his throat repeatedly.

“I thought you might need it.”

“Thank you, Young Hero Jin. I needed it.”

“It’s nothing.”

His expression, however, looked quite pleased.

*No way. Is he…*

*The type who’s only nice to women?*

There was always at least one guy like that wherever you went. Even the Heaven Shaking Sword wasn’t any different, apparently.

After wiping away the blood, Wolhwa pulled a rolled-up piece of leather from her robes and spread it out.

“This is a rough map of the entire Shanxi region. Our location is here. The Red Wind Band has probably… If they’ve been moving without rest, they may have already broken through Datong.”

“They’re faster than us.”

“By half a day for now. But the roads along our route are well maintained, so if we ride day and night, we can narrow the gap enough.”

In short, she was telling us not to expect any rest.

I followed the others and leaped onto my saddle.

*Why does something always happen the moment I arrive?*

I wanted to sigh, but what could I do? It wasn’t as though this was my first hardship—or my second. I’d just have to accept it.

*Wasn’t this supposed to be a really simple Quest?*

*Ding.*



> **System**
>
> Quest difficulty has changed to **Peak**.



“……”

Right. I guess it wasn’t simple anymore.



* * *

He was a man who resembled a fox. His pointed chin and ears, along with his sharp, slanted eyes, watched and observed everything around him at once.

“Graaah!”

“Kill them! Kill every last one of them!”

“Aaaah!”

Smoke billowed from a large manor, accompanied by screams.

The man sitting on horseback and gazing down from the hill was Pung Yang, the Red Wind Band Leader. He didn’t speak until the manor had fallen silent.

“Is it over?”

A mounted bandit who had just climbed the hill to deliver his report answered.

“We killed all the men and gathered the women and children together.”

“Why?”

“Pardon? Why, because it’s the plateau’s tradition, of course…”

Any male taller than a cartwheel—even a child—was killed without mercy, while the women were taken or sold as slaves. It was a tradition—or something close to one—passed down from the nomads.

At the mounted bandit’s words, Pung Yang quietly crooked one finger.

“Come closer.”

The mounted bandit approached hesitantly and asked carefully,

“Leader, did I perhaps make some serious mistake…”

“Where did you belong before?”

“Until recently, I was the deputy leader of the Toho Band.”

“The Toho Band? Ah, I remember. You were their deputy leader.”

“Y-yes! I was so impressed by your formidable martial arts and noble character that I swore to become your loyal subordinate!”

Pung Yang scratched his nose with an ambiguous expression.

*Was that so?*

All he remembered was killing a piece of trash in a single strike—the man who had swaggered around calling himself a bandit leader while commanding some thirty subordinates.

“My memory differs a little, but thank you anyway.”

“Not at all! It’s an honor!”

“However, the Earth Tiger Band may have been different. The Red Wind Band has its own way. Those petty matters about plateau traditions, for example.”

“Ah, I didn’t realize.”

“My orders as leader take priority. Do you understand?”

“I’ll keep that in mind—over and over again!”

“Those fellows probably followed the plateau’s traditions because they didn’t know any better. They all joined recently, just like you. So go and convey my wishes to them, will you?”

“Understood. I won’t leave a single one alive.”

The mounted bandit even gave an awkward military salute, though there was nothing military about a mounted bandit. Pung Yang waved him away.

“Yes, go on.”

“Yes, Leader!”

Pung Yang watched him ride away, then suddenly flicked his sleeve.

With a sharp sound as the air split, a streak of light shot out and pierced its target ten jang away—about thirty meters.

*Thud!*

*Clatter.*

The horse continued racing forward.

Its rider was already dead, but his foot remained caught in the stirrup. Unaware that his body was being dragged and battered to shreds, the horse galloped on.

“Go and tell them. There are no prisoners. Kill them all and burn the place.”

“Yes, Leader.”

Not long after Pung Yang’s subordinate departed, the entire manor was engulfed in flames. As he watched the signboard burn away in an instant, a faint smile touched the corners of his mouth.

The Datong Branch of the Mount Heng Sword Sect.

The moment the Red Wind Band crossed the plateau once more.



* * *

The people gathered in the spacious main hall had been arguing back and forth when the messenger’s report left them speechless.

“They’ve broken through Datong!”

“A-already?”

“What about the Datong Branch? What happened to the men who went out to stand guard?”

“Everyone was wiped out. Everyone. The Datong Branch was reduced to ashes, and there were no survivors.”

“What?”

“Could the report be wrong? They must have suffered heavy losses last time, so how could they have come this far so quickly…?”

“They appear to have absorbed another mounted-bandit group. At least two hundred men—possibly more.”

“Is that certain?”

“Yes, without a doubt.”

“Th-then when will they reach us…?”

“If they’re fast, the attack will begin within a day. At the latest, we expect it within two days.”

“We’re finished.”

The muttered words were not much different from what most of the people gathered there were thinking.

There were a little over ten of them, all senior figures holding important positions in the Mount Heng Sword Sect. Yet every one of them was already turning the word *defeat* over in their minds.

“Iron Sword Squad Leader, are you confident in this fight?”

“Why are you asking me, when you’re a Pavilion Leader? Am I the only martial artist here?”

They were squad leaders, hall leaders, and pavilion leaders of the great Mount Heng Sword Sect.

There had been a time when he had desperately wanted to rise to that position. Once upon a time, that was.

*To hell with being a commander of the Mount Heng Sword Sect. What good is a promotion now, with the sect in this state?*

*We were already doomed if left alone, and now a mounted-bandit group has come to make a mess of everything. Let’s see… If we scrape together every man we have left, there might be a hundred of them.*

The war with the Jin Family of Taiyuan had cost them nearly eighty percent of their strength.

The loss of the elite martial artists they had painstakingly trained and the seasoned senior figures who had weathered the martial world was painful enough. Most devastating of all was the loss of the Peak masters who represented the sect’s power—and its financial resources.

“Damn it. If only the Sect Leader were still alive.”

Lee Cheonbaek had started as a mere wandering martial artist and built the Mount Heng Sword Sect into what it was now. With his martial arts and resourcefulness, he could have turned this situation around.

But the Blood Wolf Sword, Lee Cheonbaek, was already dead. Of his bloodline, only one person remained alive.

“To think we have to serve some little girl who isn’t even twenty as Sect Leader at a time like this.”

At that moment, someone spat out the words in a fit of anger.

*Boom!*

The tightly closed doors of the main hall exploded.

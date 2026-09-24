# Checkpoint Review — 925–929

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

# Chapters 925–929

## Plot

After killing Wei Zhong, Jin Taekyung tells the Emperor that he spared Wei the regret of dying without making peace with his past. The Emperor announces memorials for the battle’s dead and names Crown Prince Zhu Bao as their sponsor. He reveals that he kept the succession seat empty to protect Zhu Bao, who accepts the crown princehood. The Emperor also declares that Aehyang and her unborn child have no connection to him. As the Emperor and Zhu Bao reconcile, Taekyung and Hong Jin stop the Grand Academician from escaping.

The Emperor orders Baek Yeon to arrest the treasonous officials, promising to honor Zhu Bao’s request to spare the innocent. The Bow Saint tells Taekyung that the Martial God’s letter described a chosen one who would bring a new dawn. She had considered both Taekyung and Cheongpung, but Taekyung’s return from apparent death convinced her he was the one. She also reveals that Aehyang was a Dark Heaven agent who poisoned the City Lord of Sichuan Province with the Blood Soul Gu. Taekyung realizes the Martial God was a Player, then collapses; Jeok Cheongang carries him away to rest.

As rebellion spreads through the capital, Jeong Hogun reveals that his marketplace appeal and song were made under the Emperor’s orders. He brings the Emperor’s decree to the former Grand Preceptor, who rallies thousands of Zhu Bao’s supporters to join the Embroidered Uniform Guard. Their united forces rout the rebels. Three days later, an unidentified person awakens.

## Continuity

- Zhu Bao is Crown Prince, and the Emperor is his older brother. The Emperor kept the succession seat empty to protect him and supports his compassionate vision of rulership.
- The Emperor ordered a purge of treason suspects, promising to distinguish the guilty from the innocent.
- Jeong Hogun’s marketplace appeal and song were made under the Emperor’s command. The former Grand Preceptor and thousands of Zhu Bao’s supporters joined Hogun’s Embroidered Uniform Guard against the traitors.
- The fighting in the imperial capital ended with the rebels routed and scattered. An unidentified person woke three days later; their identity and condition are unknown.
- The Bow Saint believes Taekyung is the chosen one described in the Martial God’s letter. The letter called for the chosen one to press onward with their divine strength and Will; Taekyung concluded that the Martial God was a Player.
- Aehyang was a Dark Heaven agent who infected the City Lord of Sichuan Province with the Blood Soul Gu. The Bow Saint sent the gravely ill City Lord back to Sichuan, expecting someone around Taekyung might uncover the truth.
- The Bow Saint says Dark Heaven has infiltrated local officials and military leadership in the Great Nation, potentially including provincial City Lords. The extent of the infiltration remains unknown.
- Taekyung collapsed after hearing the Martial God’s message; Jeok Cheongang took him away to rest.

## Translation Decisions

- Render 反正 (*반정*) as “restoration” in this political context.
- Use “Crown Prince” for Zhu Bao’s succession title.
- Render 플레이어 as “Player” when Taekyung recognizes the Martial God as a System user.

## Durable state

{
  "active_continuity": [
    "Zhu Bao is Crown Prince; the Emperor is his older brother and supports his compassionate vision of rulership.",
    "The Emperor ordered a purge of treason suspects, promising to spare the innocent after their connections are established.",
    "Jeong Hogun’s marketplace appeal and song were made under the Emperor’s command; the former Grand Preceptor and thousands of supporters of Zhu Bao joined Hogun’s Embroidered Uniform Guard against the traitors.",
    "The fighting in the imperial capital ended with the rebel forces routed and scattered; an unidentified person woke three days later.",
    "The Martial God’s letter to the Bow Saint described a chosen one who would bring a new dawn; Taekyung concluded that the Martial God was also a System user, a Player.",
    "The Bow Saint believes Taekyung is the chosen one, tested him, and relayed the Martial God’s message; she used the Imperial Palace’s information network while disguised as an attendant.",
    "The Emperor knows nothing of the Bow Saint’s mission beyond a vague suspicion.",
    "Aehyang, the City Lord of Sichuan Province’s favorite concubine, was a Dark Heaven agent who infected him with the Blood Soul Gu while he was in the Imperial Capital.",
    "The Bow Saint sent the gravely ill City Lord back to Sichuan so someone around Taekyung might discover the cause.",
    "The Bow Saint says Dark Heaven has infiltrated Great Nation local officials and military leadership, potentially including provincial City Lords.",
    "Taekyung collapsed after hearing the Martial God’s message; Jeok Cheongang took him away to rest."
  ],
  "continuity_sources": [
    928,
    929
  ],
  "open_questions": [
    "What is the Martial God’s identity, and how did he know a chosen one would appear?",
    "How far has Dark Heaven infiltrated the Great Nation, and which officials or commanders are involved?",
    "What story has So Gyo kept to herself?",
    "Where is Ma Sanbao, and what is his current status?",
    "Who woke three days after the fighting ended, and what is their condition?"
  ],
  "safe_through": 929,
  "temporary_decisions": [
    "Keep “Force” for 강기 distinct from “death energy” for 사기.",
    "Render 황태제 as “Crown Prince” in this succession context.",
    "Render 반정 as “restoration” for the political movement in this chapter."
  ],
  "version": 1
}

## Reading copies

## Chapter artifact 925

# Chapter 925

Flames surged upward.

They carried a fierce, terrible heat—and yet, somehow, they felt strangely warm.

*Fwoosh.*

The blue-white flames that had pierced his body along with the spearhead burned everything, melted everything, and, at the same time, embraced it all.

A man’s unhappy life.

A monster who had realized his mistake only at the very end.

*Goodbye, Wei Zhong.*

That was when I murmured the name I’d seen on the pledge the day before.

The chains of immortality that had bound one man as both an imperfect blessing and a curse shattered.

*Ding. Ding. Ding.*

As I listened to the clear chimes announcing the arrival of eternal rest, I drew back the Scorching Yang Qi I’d been pouring endlessly through White Flame’s spearhead.

All that remained in the thoroughly scorched spot was less than a handful of ash.

*Whoosh.*

Was it a wind that had blown by chance, or the mercy of someone above who had watched over everything?

I gazed blankly at the ashes carried far, far away on the wind.

The next moment, a man’s voice broke the brief silence.

“Privately, he was a traitor who tried to bring down the imperial family, and a criminal who colluded with foreign enemies and plunged the Great Nation into ruin.”

Without taking my eyes off the ashes, I asked, “Do you think that was too peaceful an end for a man like that?”

“I do.”

“I think so, too.”

No matter how much he’d reflected and repented, the crimes he’d committed would not disappear. Everything he had done as the Eastern Heaven Demon Lord, not Wei Zhong, was a burden he would have to carry even in Hell.

“Then why did you do it?”

“Why didn’t you stop me, Your Majesty?”

The Emperor, the owner of that voice, answered.

“Because I didn’t want to.”

It was a short answer, but it held every meaning. I let out a dry laugh.

“I see.”

“Now it’s your turn to answer.”

“I…”

I paused for a moment and bit my lip.

“…There were just some people who suddenly came to mind.”

“Those people were sinners like Wei Zhong, then. People who committed unforgivable wrongs.”

“Yes. And at the same time, they were people who regretted the wrong choices they’d made.”

The Head Elder of the Jin Family of Taiyuan had been like that. So had Baeksang of the Nanman Beast Palace.

Following the guiding light of Dark Heaven, they’d chosen the wrong path and could never turn back.

Sometimes they looked behind them and regretted the road they’d taken, but they’d already come too far to turn around.

And even as I poured my anger onto people like that, I couldn’t help feeling sorry for them, too.

*They could have made a better choice.*

*If they had, innocent people wouldn’t have had to die.*

*But it was always too late.*

It wasn’t self-reproach or regret.

What’s spilled is spilled. Nothing can be done about it.

I could condemn the consequences of their choices, but I couldn’t presume to condemn the choices themselves.

Revenge is easy. Forgiveness is hard.

That’s simply what people are like.

“I will erect memorials.”

In the silence that settled over us again, the Emperor suddenly continued.

“One for those who fell here today, another for the people sacrificed in the battles among the heroes of the realm. And the last one…”

The Emperor paused. His gaze turned toward the west, far away, where the wind had gone.

“The Maoshan Sect. Yes, the Maoshan Sect would be fitting.”

*Gasp.*

At the Emperor’s unexpected declaration, the officials gathered around us sucked in their breath.

Erecting a memorial at the Maoshan Sect was tantamount to tarnishing the dignity of Taizu, the founder of the Great Nation, and of the imperial family.

But before anyone could hurriedly open their mouth, an even greater shock swept through those gathered.

No—struck them.

“And all of this shall be done in the name of the Crown Prince, not Mine.”

“……!”

“……!”

The air around us trembled. Everyone’s eyes flew wide.

The Crown Prince.

The new ruler who would one day inherit this vast continent.

I’d completely forgotten, too.

What this gathering had been arranged for.

What awaited us at the end of this blood-soaked, brutal banquet.

And how the seat of Crown Prince, vacant for more than a decade, was about to find its rightful occupant at this very moment.

“Prince Shangshan Zhu Bao, receive the imperial command!”

The Emperor no longer looked exhausted.

His voice, filled with the majesty only the sovereign of a nation could possess, pierced the air. Riding the wind, it enveloped the entire grand banquet hall.

*Clang! Clang! Clang!*

Starting with Baek Yeon, Commander of the Embroidered Uniform Guard, thousands of guards drew their swords and pointed them toward the sky.

Their golden armor and blood-soaked blades flashed.

That splendid tide of steel shone for one boy alone.

For the young prince who had chosen forgiveness over revenge, even in front of his enemy—the boy who dreamed of an age of peace that no ruler in the past thousand years had ever achieved.

“Ah. Ah…”

The Emperor calmly addressed the younger brother who didn’t know what to do in the face of this sudden turn of events.

“Do you intend to defy the imperial command?”

“Y-Your Majesty.”

“Come closer.”

“But, but Your Majesty already…”

At that moment, no one failed to understand what Prince Shangshan Zhu Bao meant to say, or where his gaze had turned.

A woman stood surrounded by palace attendants, one hand clutching her swollen belly.

I already knew her name. She’d gone from being the favored concubine of the City Lord of Sichuan Province to a consort of the Emperor.

*Aehyang.*

Her eyes, fixed on us through clenched teeth, held an unmistakable anger.

But the Emperor’s expression as he looked at her held not a trace of emotion.

As though she were a tool he had kept at his side only because he needed her.

*Wait. Could it be?*

Just as the thought crossed my mind, the Emperor spoke.

“That child, who will one day be born into this world, carries the blood of the late City Lord of Sichuan Province.”

“……!”

“Therefore, neither that woman nor the child in her womb has anything to do with Me. No one is to raise questions about this.”

The court officials were visibly bewildered by the Emperor’s astonishing declaration. But a few of us, myself included, were certain.

There wasn’t a trace of a lie in what the Emperor had just said.

*I suspected it, but I can’t believe it was true.*

The Emperor hadn’t produced an heir in more than ten years, despite having an Empress and consorts.

But looking back now, it wasn’t that he couldn’t have an heir. He had chosen not to.

For the sake of his one and only younger brother, Prince Shangshan Zhu Bao.

*He must have wanted to protect him from every threat. The throne—and his younger brother.*

The only direct descendant of the orthodox imperial lineage.

And, at the same time, a perfect puppet for Dark Heaven—a figure who gave them every justification they needed to overthrow the Emperor.

On the surface, it had looked as though the Emperor couldn’t bring himself to kill his young brother, so he’d sent him away into exile. But the reason Prince Shangshan Zhu Bao had survived all this time was because of the Emperor’s far-reaching plan.

“Do you still not understand?”

The man who had given up the possibility of an heir for his younger brother, who had been forced to become a coldhearted older brother for his sake, continued slowly.

“I kept that seat empty for you from the very beginning. It was a seat only you could take.”

Though he had ascended the most exalted throne under Heaven, he had been branded a traitor and a monster who had betrayed his own family.

Though he tended to the affairs of state day and night, that brand had made people call him a tyrant.

“I wanted you to survive. I didn’t want you to become My one weakness.”

Perhaps when the infant, not yet weaned, left the imperial palace, the Eastern Heaven Demon Lord hadn’t been the only one watching his retreating figure from afar.

“I had to send you away to protect you. To root out the traitors I hadn’t been able to eradicate completely in the past, I had to bring you back into this deadly place.”

More than a decade was no short stretch of time.

It had been long enough for the Eastern Heaven Demon Lord to shore up his weakened foundations. Long enough for the Emperor to prepare for the decisive battle that would end everything.

And the Emperor had secretly brought his only younger brother back with the help of the Embroidered Uniform Guard, then protected him by keeping him confined.

He’d even made an invincible master known as the Bow Saint serve as a mere bodyguard.

“Bao’er.”

The Emperor’s voice, slipping between his dry lips, was surprisingly warm.

Warm enough to make even Baek Yeon, who had stood by him longest as a comrade and subject, widen his eyes.

Warm enough to make the body and heart of a boy who had longed for his family for so long suddenly go rigid.

“It’s time.”

“……!”

At that quiet sentence, the boy’s clear, river-bright eyes trembled.

But there was no hesitation in his gaze—only resolve, the kind of determination possessed by someone moving toward a dream.

“I, Prince Shangshan Zhu Bao…”

*Swish.*

The long hem of his robe brushed a pool of blood. Yet even on a battlefield stained red in every direction, the light within the young prince had not dimmed in the slightest.

“…humbly accept the command of His Majesty the Emperor.”

A vivid smile, unlike any anyone had ever seen, spread across the Emperor’s wrinkled lips.

“Granted.”

“Waaaaah!”

Amid the earth-shaking roar that resounded through Heaven and Earth, the two men, who had finally found each other after wandering such a long road, embraced.

Not as ruler and subject, but as brothers.

* * *

The Emperor and the newly named Crown Prince of the Great Nation, the two brothers, were embracing at the very place where a new Crown Prince had been born. Those gathered could no longer contain their swelling emotions and trembled.

“Ah…”

For more than a decade, how desperately they had hoped for this.

That all of it was a lie.

That the natural order, twisted and blackened like a monster, would one day return to its proper place.

And yet.

And yet, it had.

The thing they had desperately wished for in their hearts, unable to speak it aloud, had become reality before their eyes.

In the hearts of those who had witnessed the end of one era and the beginning of a new one, an indescribable whirlpool of emotion surged.

Before long, it overflowed in every direction as a tremendous roar.

“Long live His Majesty the Emperor!”

“May His Highness the Crown Prince live a thousand years!”

“Please, please kill me!”

Countless cheers and cries rang out.

Some who knew the truth laughed and wept like children. Others, who had been deceived by lies and had condemned the Emperor, staggered under the weight of their guilt and regret.

But there were also those who belonged to neither group.

“Long live! Long live! Long, long live!”

Dry lips ceaselessly called for the Emperor’s long life; wrinkled cheeks were drenched with tears.

But as his canny gray eyes took in everything unfolding before him, their gaze remained dark and still.

*I never thought things would go this wrong.*

The old man quietly swallowed those words, which he must never let escape his lips.

He turned over the last chance he still had.

*But it’s not over yet.*

The old man had known the whole truth from the beginning and joined hands with the Eastern Heaven Demon Lord solely for wealth and glory. But he had no intention of becoming a traitor and letting his entire clan be slaughtered.

*The pledge. If I can just make the pledge disappear and get rid of the few people who know who I really am…*

The saying “Succeed and you’re a king; fail and you’re a traitor” was wrong.

Even if you actually plotted treason, it wasn’t a crime as long as you weren’t caught.

And the old man, who had once tutored the former Crown Prince and risen to the rank of Grand Academician while earning the reverence of Confucian scholars throughout the realm, had been meticulous about such things.

*I will survive. Just as I always have.*

Repeating that resolve to himself, the old man cried out “Long live!” amid the confusion of the crowd, inching backward.

He had to meet his subordinates waiting outside the imperial palace as quickly as he could.

If he eliminated the handful of key figures who knew his identity and took possession of the pledge, he could keep his current position. And even if things became difficult, he could take his family’s wealth and flee.

No—he believed he could.

Until someone’s voice, strangely clear amid the deafening roar, pierced his ears.

“Where are you off to in such a hurry? At a time like this, you should be sharing in the joy.”

“……!”

The old man’s body went rigid.

He slowly turned his head. A young man was approaching at an unhurried pace.

“Jin… Taekyung.”

“Come on, don’t call me Jin Taekyung. That’s so cold.”

The young man, Jin Taekyung, smiled broadly and added, “You should call me Comrade Jin Taekyung.”

“What, what are you…”

“You didn’t know? I signed the pledge, too.”

“……!”

“Wait, have I got the wrong person?”

Just as Jin Taekyung tilted his head, a chilly voice rang out from behind the old man.

“It’s been a while, Grand Academician.”

*Thwack!*

With the blow to the back of his neck, the old man’s vision went black. As he sank into darkness, one name came to mind.

*Hong Jin.*

It was over.

Everything was over.
## Chapter artifact 926

# Chapter 926

Everyone makes the wrong choice sometimes.

At least a few times in life.

No—if you include all the little things in everyday life, maybe thousands of times.

But making the wrong choice doesn’t mean your life is over.

You regret it, reflect on it, and use it as a stepping stone to take a better path next time.

Of course, that only applies if you’re given a “next time.”

“I—I’ve done nothing wrong! This is a misunderstanding!”

“Your Majesty! Your Majesty!”

“You scoundrels! How dare you lay hands on me!”

Fear. Desperation. Anger.

Dozens of people raised their voices, each swept up in their own emotions.

Their silk robes had lost none of their sheen, and their plump bodies spoke to just how high their station had been—even in a place death had just torn through. But all the wealth and glory they had enjoyed until now were over, effective this very moment.

That was the fate of those guilty of high treason.

“Arrest every last one of them!”

“Loyalty!”

*Shing!*

At Baek Yeon’s stern command, the Embroidered Uniform Guards surrounding the area swung out their ropes and scabbards.

One civil official had already given up and was quietly bound. An old general clad in dazzling armor put up a fight, displaying a fair amount of skill in martial arts.

And then his head got cracked open.

*Whack!*

“You bastards, how dare you—Guh!”

“Let’s not wear ourselves out this early. Come quietly. You’ll have plenty of chances to shout later.”

“W-what are you going to do with me?”

“You already know, don’t you, old Assistant Military Commissioner?”

“……!”

At the Embroidered Uniform Guard’s cold smile, the old general sank to the ground, his face blank.

He’d realized that the blood now running warm from the crown of his head was a mere drop compared to what he’d be forced to shed from here on.

And one man was weaving his way through the chaos.

“It’s been a while. Last time we met, I think you called me a eunuch bastard with no balls.”

One man.

“You haven’t forgotten me, have you? Oh, you’ve never seen me before? Cut the crap. I remember everything.”

Two men.

“Oh, look who it is. You’ve gotten so fat I almost didn’t recognize you. Don’t worry. I’ll slim you down this time.”

“……”

Talk about making every line sound murderous.

Whenever Hong Jin greeted someone with the enthusiasm of a man attending his first school reunion in ten years, gold-armored diet supplements came marching over and dragged the person away.

Their faces were flushed with excitement at the prospect of filling the Embroidered Uniform Guard’s jails, which had been empty for a while, with a fresh batch of prisoners.

“W-wait! Torturer Hong!”

“I’m not a torturer anymore. It’s been ages since I was appointed Deputy Military Commissioner of Shanxi Province. Don’t make a scene calling me over. Go on ahead. Oh, and make sure you wash your balls.”

As one of the people who’d once slandered Hong Jin by calling him a eunuch with no balls was dragged away, the second man—the one who’d claimed they’d never met—swallowed hard before speaking.

“Um, Comrade Hong. I think there’s been some misunderstanding…”

“Who’s your comrade?”

“Pardon?”

“Do you know me? And what do you mean, a misunderstanding? Drag this traitorous bastard to the jail and throw him in.”

Watching everything unfold at lightning speed right before my eyes, I murmured to myself.

*There’s going to be a bloodbath.*

I couldn’t even guess how many would die. Hundreds? Thousands?

Or tens of thousands, like last time?

Even so, if you counted the traitors who weren’t here today, along with their families, this would be a massive purge.

“Do you pity them?”

At the Emperor’s sudden question, I gave a small shake of my head.

“They deserve whatever they get. They committed crimes worthy of death. It’s just that what bothers me is…”

“You’re worried that people with nothing to do with the treason will be sacrificed.”

“……”

“It cannot be helped. The law of the land is solemn. All the more so when it concerns treason.”

“I know. I understand.”

Revenge begets revenge.

If someone with a grudge survived this purge and plotted for the future, they could become the seed of another disaster.

Just as the Eastern Heaven Demon Lord had.

“But there can be exceptions now and then.”

My eyes widened at that unexpected declaration.

“You mean…”

“Make the truth of every connection clear and spare at least those who are innocent. That was what Bao’er asked of Me just now.”

The Emperor added with a faint smile, “It was also the first request he made of Me as Crown Prince and as My younger brother.”

“……!”

“That boy will become a sage king and usher in an age of peace. A king who cares for his people more than anyone and is loved by them in return.”

Had this man always smiled so much?

The Emperor, whose face had always been cold and gloomy, looked much brighter now.

His eyes rested on Prince Shangshan—or rather, Zhu Bao, now Crown Prince—as the boy met his gaze and awkwardly bowed his head. The warmth in the Emperor’s eyes was impossible to hide.

*Even the Emperor is still just an older brother, in the end.*

I let out a quiet snort and said, “That’s right. He’ll definitely be a sage king.”

“He is also a peerless martial artist. One day he’ll cross that Great Wall and conquer the vast grasslands, the lost lands of the Northern Sea, and even the deserts.”

“Huh?”

“Why?”

“Um. Nothing. He could.”

I wanted to ask what martial arts had to do with any of that, but I held back.

Why was I starting to think of Jin Wikyung?

“That’s right. He absolutely could.”

“Of course.”

“Not only that. He’ll build cities of gold and establish a great empire that will endure for a thousand years.”

“……A thousand years is a bit much.”

“Do you think that’s impossible right now?”

No, even if I thought about it as hard as I could, that seemed a bit much.

But the Emperor’s eyes narrowed, and I swallowed the words that had risen to the tip of my tongue, showing off my dazzling reflexes.

“I just thought you were aiming a little low. I was thinking ten thousand years.”

“Ten thousand years is impossible.”

“……”

“Perhaps it’s because you’re a Murim practitioner, but you do have a rather fanciful streak. You should try to develop a more realistic outlook.”

This son of a—

I was so stunned that I couldn’t speak. I’d gone along with him, and now he was being dead serious. Just then, someone’s hand slipped discreetly into my side.

*Poke.*

I didn’t need to turn around to know who it was.

Suppressing my anger toward the Emperor, I moved my lips.

—Don’t worry. Even if I am crazy, do you really think I’d beat up the Emperor?

Jeok Cheongang replied through Sound Transmission.

—It’s true you’re the kind of fool who’d do exactly that, but that’s not what I meant.

—If that’s not it, then… don’t tell me—

I turned, eyes wide, and Jeok Cheongang nodded gravely.

—You’re going to hit him yourself, Old Master?

—……

—Good heavens, have you gone senile again? You can’t. If you lay a hand on the Emperor, it’s over for all of us. If he gets pissed off at us and takes a liking to Dark Heaven, we won’t have a Great Nation anymore. We’ll have the Dark Heaven Nation instead. With Hell thrown in.

I was still desperately trying to talk him out of it, like a missionary at Yeongdeungpo Station shouting that believers go to Heaven and unbelievers go to Hell, when Jeok Cheongang gave me a withering look and jerked his chin over my shoulder.

—Before I pluck those dog eyes out, look and see who’s waiting behind you.

I turned and saw a person standing in the distance, watching us with eyes that were calm and still.

*The Bow Saint.*

The moment our gazes met, the relief and joy that had wrapped around me seemed to wash away in an instant.

Along with an inexplicable chill seeping into my lungs.

—So it was you.

The question remained unresolved, and that voice lingered faintly in my ears like a breeze at dawn.

—The chosen one the Martial God spoke of.

What had that meant? What truth was hidden behind it?

My eyes trembled before I could stop them.

The Bow Saint gave me a slight nod, then quietly turned and began walking.

Toward somewhere beyond the eyes of the crowd.

Toward a secluded place where she could reveal the secret she’d kept hidden all this time.

* * *

I followed the Bow Saint without a word.

As if to prove that the battle in the grand banquet hall wasn’t the whole story, the clean, spacious grounds of the imperial palace were filled with blood and bodies that no one had yet managed to clear away.

Still, no one stopped me and the Bow Saint as we crossed the palace at an unhurried pace.

If anything, people hesitated, then bowed and stepped aside.

They recognized us.

They knew who we were.

And which side we had fought on—the Emperor’s or the Eastern Heaven Demon Lord’s.

But unlike them, I still didn’t know.

I didn’t know what the Bow Saint’s cryptic words meant. And I knew almost nothing about the one whose existence was shrouded in mystery.

*The Martial God.*

The peerless hero born of the Great Faction War, who had appeared one day and vanished just as suddenly.

No—he was the very sky that looked down upon all of Murim.

People used to say there had never been anyone like the Martial God, and there never would be again.

There were powerful figures known as the Three Saints and the Ten Kings, but the Martial God stood in a realm no one could reach.

That was why he was called the sky. That was why he was called a god.

But…the Martial God was gone now.

The symbol and center of Murim had vanished like a phantom shortly after disbanding the Murim Alliance.

As though he had never existed.

As though he’d been waiting for this to happen from the beginning.

When the Martial God disappeared in an instant and the years passed, all kinds of rumors sprang up like weeds.

Some said he died because the Internal Injury he sustained in his final life-and-death duel with the Heavenly Demon never healed. Others said he was spending the rest of his life in some remote mountain valley.

And that wasn’t all.

There were rumors that, after gaining enlightenment, he had finally become an immortal.

There were also plenty of outlandish rumors that the Martial God was, by nature, something like a divine beast protecting the Central Plains, and that he no longer appeared in human form.

The Martial God, surrounded by questions on all sides, had always made for fascinating stories.

The heroic tales about him were enough to feel like myths and legends.

Even to those who had seen and encountered the Martial God up close—and to me.

And yet…

*For the Martial God himself to come up so suddenly.*

I hadn’t even seen the Martial God’s little finger, but just hearing his title made every hair on my body stand on end.

Now that we’d reached our destination and stopped, I felt it more than ever.

*Rustle.*

Night had already given way to the early dawn.

The sound of wet grass brushing against us rang out with a chill. The Bow Saint slowly looked around, then spoke without turning.

“You’ve been here before, haven’t you?”

She looked like a young woman who had only just entered her early thirties, but the Bow Saint was an old master who had lived through an age beyond measure.

I answered with the respect she was due.

“Yes.”

“I remember you charging at me like you meant to kill me. It left quite an impression.”

The Bow Saint reached out and gave an unopened flower bud a light tap.

This place was filled with countless rare and beautiful plants. It was the same abandoned area where she and I had met a few days ago.

“Whenever I felt restless, I used to come here and walk. People treated it like a forbidden ground, so there wasn’t even an ant around.”

“Then that day, too…”

“That’s right. I had something on my mind. I couldn’t come to a conclusion, no matter how I looked at it, so I thought I’d walk around here and think it over.”

The Bow Saint turned around. Her crescent-shaped eyes, and the gaze hidden within them, were deeply still.

“You were the chosen one the Martial God spoke of, someone who was supposed to possess the supernatural powers to escape even death…so why are you in an irrecoverable state?”

“……!”
## Chapter artifact 927

# Chapter 927

An inexplicable shiver ran down my spine.

The power of supernatural forces—the kind that could even evade death.

I knew better than anyone what that power was, the only way to define it being as something uncanny, like the work of ghosts.

*The System.*

A stroke of luck that had come to me when my life was slowly sinking like a boat with a hole in its hull.

A power that had given me both my greatest crisis and my greatest opportunity.

And yet, in this world called Murim, there was only one person besides me who knew the System existed.

The Fire King, Jeok Cheongang.

No one else could know the true nature of the power I possessed.

That included not only the Imperial Palace, but also the handful of people who had been at my side, even up close.

*They might have some vague sense that there’s something there, but that’s as far as it goes.*

I’d crossed the line between life and death more times than I could count.

I’d survived situations that would have killed an ordinary person several times over, and I’d grown at a pace without precedent in Murim’s history.

Even so, no one knew exactly what my power was.

No—not unless I told them the truth myself.

That was the kind of power the System was.

A supernatural ability no human could even begin to imagine, one that couldn’t be contained by the four characters of *supernatural powers*.

*Even if that person is the Bow Saint, she’s no exception.*

The shock I’d felt in that fleeting moment had long since settled.

But one question remained, one I couldn’t answer on my own: how had *they* learned about something only a handful of people knew about me?

*The Bow Saint. And…*

The Martial God.

The shadows of two giants who had vanished from the world long ago were falling over me at this very moment.

Not like shade cooling me from the sun, but like a kind of darkness.

It was enough to make my skin crawl.

I licked my dry lips. My mouth felt as rough as if I’d swallowed a fistful of sand.

*What on earth do they know, and how much?*

Just as I sent the unspoken question drifting through my mind, the Bow Saint—who had been watching me in silence with deeply shadowed eyes—suddenly spoke.

“You’re calmer than I expected. I thought you might ramble on with excuses. Or pretend you didn’t know.”

I forced myself to answer evenly. “Would that change anything?”

“No. Nothing at all. You know that, too, don’t you?”

The moment I heard that reply, I knew for certain.

This woman before me—the Bow Saint—had been watching me all along.

And she knew more than I’d imagined.

*Then could it be…? No. That can’t be.*

I pushed away the question that had suddenly flashed through my mind and spoke in a sharp voice.

“Since when?”

“That short question seems to hold several meanings. Let’s see… I’m not sure how to answer it. Why don’t I start with what happened today?”

The Bow Saint gently brushed the flowers lining either side of the path as she continued.

“Blazing Flame Divine Dragon Jin Taekyung. The moment I saw you rise when you should surely have been dead, I finally became certain who the chosen one the Martial God spoke of was.”

“How could that man—no, how could the Martial God…”

“How does he know about you?”

I nodded, keeping my agitation in check.

It felt as if every nerve in my body were drawn taut.

Everything could change completely depending on this answer. The course of what came next could twist in a direction even I couldn’t predict.

The Bow Saint’s brief reply the next moment was enough to bring my thoughts to a halt.

“Why would I know?”

“What does that—”

“Neither I nor he could have known. It’s only natural. I found that letter before you were even born.”

“…A letter? Before I was born?”

“Yes. I first found it one day, after many years had passed since the Great Faction War ended—after the mountains and rivers had changed more than once.”

The Bow Saint’s calm voice mingled with the early morning air and drifted into my ears.

“At first, I thought it was simply the trace of some unknown ancient. But I was wrong. The letter had been left for me by the Martial God.”

“Then what, exactly, did the letter say?”

“An arrangement he had made. No—perhaps a kind of prophecy.”

“……!”

“And there was one word that always appeared in its contents.”

My chest felt tight, as though a great stone had been placed in the hollow there.

I forced the words out.

“The chosen one.”

“That’s right. And ‘the chosen one’ didn’t point to any one specific person.”

*Step. Step.*

Her careful footsteps moved through the grass, avoiding each blade.

Faint moonlight poured over the Bow Saint’s head as she walked through the garden.

“I couldn’t believe it, but I had no choice.”

Because he was the Martial God.

Her voice held an awe she couldn’t conceal.

The Bow Saint added, in a voice as faint as the moonlight, and continued slowly, matching her steps.

“So, after several decades, I went out into the world and traveled the land. I spent most of my time in the Central Plains, but at one point I went to the endless desert in the west, and at another I crossed the grasslands and traveled as far as the Northern Sea, full of moss and ice.”

The journey to find the “chosen one” mentioned in the Martial God’s letter was like searching a field of sand for one special grain. The Bow Saint had to shoulder the entire burden alone.

“I couldn’t ask anyone for help. The letter said that not a single detail related to the mission could be revealed before it was completed.”

But the Bow Saint never gave up.

The Martial God’s arrangement, which was almost like a prophecy, required someone called the chosen one.

“When the whole world is covered in darkness, they will become a lamp and light the way. They are the one person who will finally open a new sky and bring the dawn.”

The Bow Saint murmured those words, then turned her head toward the sky.

“But even after I searched and searched for someone whose age, face, name, and even gender I didn’t know, the chosen one never appeared.”

Of course not.

Finding a single person in this vast land—someone who might not even have been born yet—was almost impossible.

“But it wasn’t completely impossible. If what he wrote in the letter was true, the chosen one would be able to distinguish themselves at a dazzling pace.”

A needle in a bag.

A needle in a pouch was bound to poke out eventually.

No matter where it was, or how deeply it was buried in a crowd.

“I followed the rumors and sought out the people I thought might be the chosen one. But even at Heaven’s Gate Temple, where the brightest talents in the land gather, I couldn’t find any real certainty.”

Heaven’s Gate Temple was where my second older brother, Jin Mukyung, had spent some time as the Second Young Master of the Jin Family of Taiyuan.

It was a cradle of talent, overflowing with gifted people of every kind, along with the heirs of the most prominent sects.

But even the cadets of Heaven’s Gate Temple, each with their own remarkable talents, fell far short of the Bow Saint’s idea of the chosen one.

“They were all outstanding, but that was all. Every one of them had an obvious limit. They had limits, and so did I.”

I’d been listening to the Bow Saint in silence until then. At last, I understood why she—like the other Three Saints—had disappeared from public view, hidden in the vast shadow cast by the Martial God.

And why she had been staying in the Imperial Palace.

“You were using the imperial information network.”

“‘Cooperating with’ would be more accurate than ‘using.’ That was before the current Emperor, then the Fourth Prince, launched the restoration.”

“Then does the Emperor know…?”

“No. He only has a vague suspicion. He knows nothing. That was one of the conditions I set. And it matters that after he ascended the throne, I gained access to information from every corner of the land.”

The Bow Saint was a weighty counterbalance—one powerful enough to tip the balance of power in an instant.

Disguised as a palace attendant, she stayed by the Emperor’s side and learned every detail of the large and small events unfolding across the land. The existence of an unidentified Supreme Peak master also had the effect of restraining the Eastern Heaven Demon Lord’s movements.

“In many ways, it was the right choice. Staying in the Imperial Palace let me learn things I’d never seen or heard before.”

One of those things was Dark Heaven, which had sunk its roots deep into the imperial court. And the other was…

“Someone who was growing beyond the reach of my eyes.”

The Bow Saint had been looking up at the sky, but now she turned her gaze toward me. Our eyes met in midair, and I quietly swallowed.

“The Jin Family of Taiyuan. Jin Taekyung. At first, the names were unfamiliar, and they didn’t interest me. At least until the second report from Shanxi.”

“What second report?”

“The unbelievable news that the Fire King, Jeok Cheongang, had taken on a Disciple.”

The Bow Saint added a faint smile.

“Of course, the reports that came in quite some time after that were far more surprising.”

A year after the Jin Family of Taiyuan conquered Shanxi Province, I finished my secluded training on Mount Jiuhua and came down from the mountain.

I was incomparably different from before.

In my martial prowess. In my state of mind.

And in the major events waiting for me.

“Every time I heard news about you, I became more and more interested. No—that wasn’t just interest.”

The chosen one.

A lamp to light the night, the one who would open the way to a new dawn.

The unknown person the Bow Saint had long searched for was gradually emerging from behind the curtain.

“That’s why I had to see for myself. I needed to know which of the two people I’d been weighing in my mind was the chosen one.”

Two people.

The word cut through my ears with unusual clarity. A name flashed through my mind like lightning.

“…Cheongpung.”

At the word that slipped out of me, the Bow Saint gave a small nod.

“That’s right. Cheongpung, the Huashan Divine Dragon. He, too, had every chance of being the chosen one. If I hadn’t seen you at the grand banquet hall, I would have believed the Sword Saint’s Disciple was the chosen one.”

But the Bow Saint wouldn’t have needed to call both of us here.

She was already fairly certain that one of the two was the chosen one.

And I had plenty of connections that might have tied me to the events that had just taken place.

“I already knew about your connection with Prince Shangshan—no, the Crown Prince. When Dark Heaven reached out to Hong Jin first, pretending to be an ally, I thought it might actually work out well. But I needed something more conclusive.”

Just then, something suddenly came back to me.

Ma Sanbao had been the one who first contacted Hong Jin.

And I hadn’t thrown myself into the deadly place that was the Imperial Palace only to save Zhu Bao.

“Blood Soul Gu…”

Was this what it felt like to get hit in the back of the head with a sledgehammer?

I continued as if groaning.

“Were you the one who planted the Blood Soul Gu in the City Lord of Sichuan Province?”

The Bow Saint’s bitter smile branded itself into my eyes.
## Chapter artifact 928

# Chapter 928

Blood Soul Gu.

A cursed venomous creature created by the Five Poisons Sect, which had once drenched Nanman in blood.

When I realized what had driven the City Lord of Sichuan Province to his death, everyone—including me—had been certain it was Dark Heaven’s doing, and that it had deep ties to the Emperor.

But now, I wasn’t so sure.

What was true, and what was false?

Where should I begin—and where should I stop—believing?

And right now, was this woman before me, looking at me with a bitter smile, really an ally?

And…

*If the Imperial Palace was the one that planted the Blood Soul Gu, then what kind of being is the Martial God behind her—the one who foresaw my appearance?*

That was only one of the endless questions I had about the Martial God, a man shrouded in mystery.

*Grind.*

I clenched my teeth and glared at the Bow Saint.

“I asked you. Who planted the Blood Soul Gu in the City Lord of Sichuan Province?”

The Bow Saint watched me in silence, then abruptly spoke.

“What would you do if I were the one who did it?”

“……!”

A shiver ran down my spine.

Suppressing my agitation, I forced myself to answer in a calm voice.

“You’d have to give me an explanation. One that could convince everyone, myself included.”

“And if it still doesn’t convince you?”

“Then…”

I drew a quiet breath.

At the same time, instinctively, I lowered my stance ever so slightly and readied myself to strike at any moment.

There is no absolute good or absolute evil in this world.

But Dark Heaven—Lord of Heaven—was unquestionably close to absolute evil.

If the Bow Saint had used the Blood Soul Gu, which was deeply connected to Dark Heaven, and it had close ties to Dark Heaven, there was only one thing I could do.

“I wouldn’t be as polite as I am now.”

At that moment—

*Whoosh.*

A powerful gust of wind swept around the Bow Saint and me.

No—our winds collided.

Our opposing waves of qi met head-on, poised to swell. Just then, the Bow Saint’s narrowed eyes curved like a full moon.

“Good. That’s how it should be.”

“What…does that mean?”

“You exceeded my expectations. In every way.”

It didn’t take me long to understand the meaning in those softly curved eyes and the brief words she’d spoken.

*A test.*

The word suddenly flashed through my mind, and the tension constricting my whole body snapped loose.

“Damn it.”

At my sigh, the Bow Saint furrowed her brow in mock disapproval.

“Hm. Still wet behind the ears, and you talk to your elders like that?”

“If you were really an elder, you wouldn’t toy with someone who’s still wet behind the ears.”

“I’ve spent decades searching for you. What does it matter if I tease you a few times?”

The Bow Saint smiled faintly. As she looked at me, there was a hint of approval in her eyes.

“So, in the end, you had nothing to do with the City Lord’s death or the Blood Soul Gu?”

“I had something to do with it.”

The Bow Saint tossed out the bombshell as if it were nothing. She stroked a flower and continued.

“Knowing full well he would die soon, I sent him back to a place of death. I thought that if he died in Sichuan, at least one of the people around you there would notice.”

“You knew he was going to die?”

“The City Lord of Sichuan Province was already infected with the Blood Soul Gu while he was staying in the Imperial Capital. Naturally, it was Dark Heaven’s doing—or, more precisely, the doing of the City Lord’s favorite concubine.”

“Don’t tell me…Aehyang?”

“That’s right.”

My eyes widened at this unexpected revelation. The Bow Saint continued in an even tone.

“Don’t be surprised. If you need to control someone and that someone is a man, there’s no surer method than using a beautiful woman.”

“But how did you know she was working for Dark Heaven just from that?”

“I discreetly investigated her myself. She had mastered an impressive level of Soul Bewitchment. I’d heard he was neglecting his duties, besotted with women, so I summoned him to the Imperial Capital while I was keeping an eye on him.”

An old memory, not so long ago, came back to me.

The City Lord of Sichuan Province, half naked even when I’d first met him—before the incident that came to be known as the Sichuan Blood Tragedy.

*So even back then…?*

A chill suddenly crept down my spine.

It wasn’t because I hadn’t realized Aehyang, an agent of Dark Heaven, was right beside him.

It was because I couldn’t even begin to guess how far Dark Heaven’s shadow—its dark hand—had reached.

“Then, could it be…”

“Yes.”

The Bow Saint nodded before I could finish and spoke.

“Dark Heaven has infiltrated the Great Nation down to its roots. Thoroughly, into every corner, so deeply that no one knows where it ends.”

“……!”

“The death of the Eastern Heaven Demon Lord wasn’t the end of everything. A considerable number of local officials wielding various degrees of real power, along with generals commanding armies, are likely still working with Dark Heaven. Of course, that probably includes the City Lords who govern the provinces.”

I swallowed.

A province was more than just a word. Its land and population were enormous.

Why else, in the chaotic age of the past, had dozens of warlords proclaimed themselves kings and fought for supremacy?

Was it only because they wanted to claim legitimacy by calling themselves kings?

That was half right, and half wrong.

If you conquered a region and absorbed all the strength of its land, you could build enough power to claim the title of king of an entire nation.

Of course, these days they were nothing more than officials following orders from a powerful central government. But if those City Lords harbored treasonous ambitions and rose up in earnest, they could inflict tremendous harm on the Great Nation.

*So it wasn’t an exaggeration or a lie.*

Before he accepted everything and let go, the Eastern Heaven Demon Lord had poured out a curse filled with rage.

*This is only the beginning. Even if you protected the Imperial Capital, the flames will sweep across the land.*

But that hadn’t been a curse he’d spat out at random, blinded by anger.

It held a grain of truth—perhaps it was a time bomb that would explode in the not-too-distant future.

*Damn it.*

My head was burning.

My breathing had grown ragged, though I hadn’t done anything, and my heart was pounding.

It felt as if I could see the flames that threatened to swallow two worlds—modern society and Murim—flickering right before my eyes.

And with them, amid a situation no one could have foreseen, came the shadow of a giant who had suddenly swept aside the curtain and appeared.

“Then what should we do now? From this point on?”

I asked the Bow Saint, drawing in a ragged breath.

No—it was more like a question for the person who had led her to this very moment by leaving a letter long ago.

The Martial God.

A man born human, yet called a god.

A man who had saved the world once, then left behind an arrangement to save it again.

I was asking him now.

I wanted another prophecy from the Martial God’s letter to the Bow Saint—one ray of light to illuminate this pitch-black road.

“What am I—fuck—what am I supposed to do?!”

But the Bow Saint’s reply held not even a glimmer of light as it reached me, shouting in desperation.

“I don’t know. Neither do I, nor does he.”

“……!”

In an instant, the strength drained out of my whole body.

As my vision blurred, I lowered my head helplessly.

I’d been sure there was something more. Something more to it.

If it was the Martial God…

I thought he would be different, if anyone could. He was the one who had been certain that a person like me would appear someday.

I’d even entertained a thought that should have been impossible.

*What if the Martial God—the greatest of all time, with his dazzling achievements and divine authority—*

*Maybe…*

I clenched my teeth and was about to follow that unbelievable thought to its conclusion when a quiet voice reached my lowered head.

“But there is one thing.”

At that moment, I slowly lifted my head as if I were under a spell.

The Bow Saint was there, gazing at me with eyes sunk deep.

“He left a message for the chosen one.”

“What…what do you mean?”

“Divine strength.”

Why?

At those two brief words, my body stiffened without my knowing why. An inexplicable chill ran down my spine.

The Bow Saint’s voice reached my ears. Her calm, quiet words rang out like thunder.

“He said to forge ahead with the divine strength and Will that only the chosen one can possess. Just as…”

In that instant, her voice faded, and the world slowed.

An invisible curtain had fallen, blocking my sight and muffling my ears.

There was only one person.

I could see no one but the Bow Saint. I could hear nothing but her lips moving slowly and the voice slipping between them.

“Just as you did.”

“……!”

Time, which had stopped, began to flow again.

But I still couldn’t move. I could only stare blankly at the Bow Saint, frozen as if trapped in a glacier.

*I…what did I just…*

What on earth had I heard?

My mind felt as though it had emptied completely. A few words floated there, bright against the blankness.

Then, in an instant, they became a great bolt of lightning and pierced the crown of my head.

*Just as you did.*

Just as *you*, the Martial God, did.

There was only one meaning this could have.

The Martial God had also been a chosen one like me.

No. To be precise…

*System user.*

*Player.*

The word filled my empty mind, swelling until it felt like it would burst. A clear chime rang out.

*Ding.*

And at that moment—

*Slip.*

I felt the sky and the ground slowly turn over as I fell into pitch-black darkness.

* * *

It all happened at once.

Jin Taekyung’s trembling form crumpled like a puppet with its strings cut. The Bow Saint’s hand shot out and seized his collar. And finally, the cold dawn air that had drifted through the abandoned garden suddenly grew hot.

*Grab. Fwoosh!*

The Bow Saint steadied Jin Taekyung, then spoke to the uninvited guest who had suddenly appeared.

“How strange. I don’t remember inviting you, too.”

The uninvited guest answered in a low voice.

“I do call him my Disciple, after all. How could I not worry when he’s alone with some nasty old hag?”

The Fire King, Jeok Cheongang.

Despite his calm voice, fire flickered in his eyes.

“Fine. Let’s hear what kind of nonsense you’ve been up to.”

The Bow Saint let out a soft laugh and shook her head.

“A lot of years have passed. You could have changed, but you’re still the same. Still acting without thinking.”

“Do I have to say it twice?”

“You were hiding like a rat and listening, so you should know. That’s all there is to it. This child was simply more exhausted than he could handle.”

The Bow Saint gazed at the unconscious Jin Taekyung.

Dried blood clung to his face in several places, and his features bore the marks of a fierce struggle.

They were proof of the dazzling fight and nobility he had shown.

“Take him with you. Let him get a little more rest.”

Jeok Cheongang didn’t hesitate for long. He carried Jin Taekyung on his back as if he’d been waiting for the chance, then used his movement technique to hurry away. The Bow Saint watched him until he was gone.

Then, suddenly, she saw a flower bud slowly opening in the light.

The first light of dawn.
## Chapter artifact 929

# Chapter 929

That night was unusually dark and long.

It was long for the soldiers on both sides, who clashed again and again, wielding blazing torches and keen weapons.

It was long for the people, trembling with fear as they waited for the sudden upheaval to end.

*Clang! Clang! Clang!*

“Gah!”

The battle that night was not confined to the Imperial Palace.

The chilling clash of blades and the screams covered the entire imperial capital for hours. Countless people who heard them were reminded of a not-so-distant past: the fourth prince’s coup, which had overturned the Great Nation’s proper order and history from top to bottom.

And amid this utter chaos, some were gripped by greater anger and fear than anyone else.

“These bastards could be chewed to death and it still wouldn’t be enough…!”

“It’s over. The Embroidered Uniform Guard must have discovered us!”

Dozens of people faced one another across a table inside an abandoned shrine, filled with dust and cobwebs. The shadows of a dim oil lamp flickered between them. Their clothes and ages varied widely.

Listening to their cries, an old man suddenly spoke.

“You’re making too much noise.”

His voice was low, but forceful. At once, as if on cue, everyone fell silent and turned to look at him.

His skin was covered in deep wrinkles, and his frame was slight—proof of the long years he had lived.

But his experienced eyes were clear and deep. His clothes showed signs of mending here and there, yet his bearing was perfectly composed. Both told the story of the life he had led.

“Don’t be swept up in the commotion. The path we must take was decided long ago.”

The old man lifted his lukewarm teacup.

He seemed not to care in the least about the trail of torches drawing closer outside, or the great roar of the crowd.

“I don’t know what disaster is unfolding out there, but it’s worked out well for us. Now that chaos has broken out, this is exactly when we must act.”

The time had come.

At the old man’s brief words, some eyes lit up. Others trembled, unable to suppress their fear.

Restoration.

It was why they had gathered here today—and their justification for saving one person alone.

“Now…we must set everything back where it belongs.”

The old man’s eyes flashed with a strength unimaginable at ninety years of age. And with a conviction more unwavering than anyone’s.

“We will drive those cruel, ruthless traitors—who have strayed from what is right and overturned the natural order—out of the Imperial Palace, and raise His Highness Prince Shangshan to the throne with the strength of the people.”

“……!”

“……!”

An unseen surge swept through the shrine like a wave.

Though they had come here with their own resolve and determination, for a moment they had forgotten, in their rising excitement and fear, what the great undertaking they meant to pursue truly signified.

*With the strength of the people. Raise a ruler of the people.*

They looked at one another.

They differed in age, status, and gender.

But now they were comrades in the same boat.

They had each lived their own lives in their own places. Now they had gathered together to set the Great Nation’s enormous ship on the right course.

A few days earlier, an unknown person’s words had lit the fuse hidden deep in their hearts.

“The azure heaven that once shone blue is fading, and dark clouds are rolling in.”

At the tune that suddenly slipped from someone’s lips, a young Confucian scholar spoke as though entranced.

“The storm soon to come will swallow the world.”

“But, people, do not tremble. Do not be afraid.”

An old laborer, his skin darkened by the sun, muttered in a rough voice. In his hand was an axe with a keen, blue-steel edge. Once, he had led an army.

“For there is a mountain, the highest in all the world.”

“There, a stream that never runs dry.”

“Luscious fruit, and beasts that frolic.”

“And a home to keep out the storms, and a forest to provide firewood.”

It could no longer be called the voice of just one person.

Reciting the tune that had wandered through the imperial capital’s marketplaces these past few days, they rose to their feet.

“It can shelter all the people—and more.”

*Step. Creak.*

The old shrine groaned as the people filed out.

But the tune that rang on grew louder and stronger.

“So, people. Do not tremble. Do not be afraid.”

The old man, leading the way with his white robes fluttering, stepped onto the damp earth.

And whenever his slight frame moved along the rugged mountain path, shadows crouched beyond the darkness rose and followed him.

From dozens to hundreds.

From hundreds to thousands.

Before long, they had become an army. In their hands were dirt-stained sickles, and spears, swords, and axes red with rust.

*Step. Step.*

They marched toward the faint light of dawn shining from the east, toward the trail of torches creeping up the mountain like a living dragon.

And the song rising from their lips became a fervent prayer, a mighty roar.

“Go to Mount Shangshan, go to Mount Shangshan.”

Thousands of pairs of solemn eyes gleamed in the darkness.

“Though the raging storm should swallow the Five Sacred Mountains of the Central Plains, it will never dare reach Mount Shangshan.”

*Thud-thud-thud-thud.*

The low mountain trembled. Those torches drawing closer by the moment were likely the punitive force sent by the Emperor, who had realized a restoration was underway.

But…

“The lord of Mount Shangshan is one who has Heaven’s protection!”

They raised their voices even higher.

Regardless of status, they strained their throats, fighting to suppress the fear welling up even now.

On an ordinary day just a few days earlier, a man in a bamboo hat whose identity they did not know had cast a single sentence into their hearts. Now they shouted it with all their strength.

“He is the descendant of the dragon who commands rain and lightning, and a vessel fit for a righteous and benevolent ruler!”

And just as their great shout shook the land around them—

*Whoosh.*

With a gust of wind that felt unusually sharp, a man suddenly appeared through the gray dawn mist and spoke.

“That’s quite a good tune.”

“……!”

“……!”

Everyone’s eyes widened.

The golden armor on him could not be concealed, even beneath the dried blood in several places.

It meant only one thing.

“The Embroidered Uniform Guard…!”

At someone’s groan-like whisper, trembling eyes turned toward the torches undulating a few hundred *jang* below.

The moment suspicion became certainty.

There was no doubt.

Those were the Embroidered Uniform Guards sent by the Emperor to put down the restoration.

And perhaps Prince Shangshan had already…

“You shameless bastards! Aren’t you afraid of Heaven?”

Some of the restoration army, consumed by rage, were about to rush at the man who was clearly an Embroidered Uniform Guard when the old man, who had led them all despite his age, suddenly spoke.

“The blood on your armor—whose is it?”

The restoration army, poised to charge, stopped moving. The man answered in an even voice.

“It belongs to traitors who endangered the ancestral temples and the state.”

“Then who are these traitors you speak of?”

“On the small scale, Wei Zhong, the East Depot’s Seal-Holding Eunuch, and those in league with him. On the larger scale, the foreign enemy called Dark Heaven.”

“……Dark Heaven. Dark Heaven, is it?”

The old man murmured softly. That name, which had recently drenched the martial world in blood, was not unfamiliar to him.

Neither was the voice of the man standing there in bloodstained golden armor.

“Was it you?”

The words were cryptic.

But unlike the restoration army, who could make no sense of this strange exchange, the Embroidered Uniform Guard understood what the old man’s brief question meant.

“It was.”

“Then what you said and did in the marketplace that day…”

“It was all done at His Majesty’s command—the imperial decree.”

“Ah.”

The old man sighed. Some among the restoration army belatedly recognized the man, and their eyes widened.

“Could it be…?”

“Th-that’s right. It was that voice.”

They still remembered it clearly.

The voice that rang out distinctly even among hundreds of people.

The man in a bamboo hat who had cast a great stone into their hearts, then vanished without a trace.

“I am Lee, once Grand Preceptor to the late Emperor. What is your name?”

At the old man’s question, the man—now wearing a golden helmet instead of a bamboo hat—answered.

With the respect due to an elder official driven from his post decades ago after being falsely accused for repeatedly advising the Emperor to keep eunuchs at a distance.

“Jeong Hogun, Thousand Captain of the Embroidered Uniform Guard. I have come to deliver His Majesty the Emperor’s command.”

His voice, charged with internal energy, pierced the dawn air and reached everyone’s ears.

“I was unwise and failed to bring about an age of peace and prosperity; I was unfilial and lost the late Emperor and the elders of the imperial family. Yet I have never once been disloyal. Now, at long last, I seek to set the natural order right. Raise the banner of Crown Prince Zhu Bao, and together with those who follow you, eliminate the traitors.”

“……!”

“……!”

The air stopped.

An unseen shock swept over the restoration army like a giant wave.

Crown Prince Zhu Bao.

Everyone knew what that meant.

Jeong Hogun walked slowly toward them, carrying a banner. Beside the dragon embroidered in gold thread was the name Zhu Bao. At the sight of it, even the slightest doubt vanished.

“Ah…”

As cries of wonder rose all around him, the old man swallowed. He fought back the tears welling in his wrinkled eyes.

Then, in the next moment, he fell to both knees and accepted the Crown Prince’s banner with trembling hands.

“I receive and obey His Majesty’s most solemn imperial command.”

With the light of dawn growing clear in the far west, the roar of thousands who had joined forces with the Embroidered Uniform Guard woke the early morning.

They roused the people who had been paralyzed with fear, and the loyal men who had already lost all hope. Then they fell upon the traitors, who were still fighting bloody battles throughout the imperial capital.

They became a wave of people numbering tens of thousands—no, hundreds of thousands.

“Waaah!”

“Long live His Highness Prince Shangshan!”

“Long live the Emperor!”

*Crack!*

“Gah!”

“Retreat! Retreat!”

That dawn was painted with countless screams and blood.

And when the unusually dark, long night ended and daylight broke, no more battles were fought.

Only the shouts of those pursuing the rebel forces, who had lost the will to fight and scattered in every direction, and their overflowing joy remained.

One day. Two.

Then three days passed in the blink of an eye, and one person opened his eyes.

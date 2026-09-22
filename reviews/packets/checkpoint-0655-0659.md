# Checkpoint Review — 655–659

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

# Chapters 655–659

## Plot

A Supreme Peak master devastates Yohi’s Western Yao Estate, killing more than a hundred Yao warriors and beasts. Jin and Yayul Mok conclude that Dark Heaven likely deployed the attacker. Heugung’s guards are found dead, and a severed wrist believed to be his is recovered, but footprints indicate that a third party intervened and abducted Yohi and Heugung rather than staging their deaths.

Baeksang publicly accuses Jin of the massacre. Utu-ri testifies that he saw Jin, masked, dining near the West Gate with an unfamiliar middle-aged man shortly before the attack. Baeksang uses the testimony and Jin’s unexplained movements to order his capture dead or alive, but the Beast Miao King blocks the arrest and defends Jin. Baeksang proposes that the Tribal Grand Council decide Jin’s fate on its second day.

The System generates the Either-Or Quest, requiring Jin to choose between resistance and surrender while warning that the choice may kill someone. Unable to escape with his companions, Jin obtains the Beast Miao King’s promise to protect them and clear his name. He punches Baeksang, then declares that he surrenders.

Meanwhile, a reconnaissance squad racing south through Guangxi to stop the Blood Monk receives a sealed order from the Nanman Beast Palace. The squad turns against Song Ilseom and Hyuk Mujin; Ju Hwaran is alive but subdued with a Pressure-Point Strike, while Song Ilseom and Hyuk Mujin surrender their weapons and are bound.

## Continuity

- Jin remains the Third Young Master of the Jin Family of Taiyuan, head of the Fire Dragon Pavilion, and an ally of the Nanman Beast Palace and Fire Gate Clan.
- Yohi’s Western Yao Estate was destroyed by an unidentified Supreme Peak master. Dark Heaven is suspected, but the attacker’s identity and motive remain unknown.
- Heugung and Yohi are missing. Heugung’s apparent death is unconfirmed, and a third party was present at the estate.
- Baeksang has accused Jin of the Inner Palace massacre and arranged circumstantial evidence against him, including Utu-ri’s testimony.
- The Beast Miao King prevented Jin’s immediate arrest and promised to protect Jin’s companions and clear his name.
- Jin chose surrender under the System’s Either-Or Quest after punching Baeksang. The consequences of his surrender and the second-day Council judgment remain unresolved.
- The reconnaissance squad is traveling south through Guangxi to intercept the Blood Monk, expected to arrive within two or three days.
- A palace-sealed order caused two tribal chieftains to turn the squad against Song Ilseom and Hyuk Mujin. The reason for the order is unknown.
- Ju Hwaran is alive but captured separately after being subdued with a Pressure-Point Strike.
- Song Ilseom and Hyuk Mujin are disarmed, bound, and held by the reconnaissance squad. Song Ilseom suspects that Jin caused a major incident in the Inner Palace.

## Translation Decisions

- Use **Western Yao Estate**, **Eastern Yi Estate**, **Southern Bai Estate**, **Tribal Grand Council**, **West Gate**, **Outer Palace**, and **Inner Palace**.
- Retain **Force**, **Supreme Peak**, **Sound Transmission**, **Dark Heaven**, **Blood Monk**, **Myriad-Poison Ring**, **Fire Dragon Pavilion**, and **Fire Gate Clan**.
- Use **Either-Or** for 양자택일, **Pressure-Point Strike** for 점혈, and **messenger eagle** for 전서응.
- Use **Chief Jang** for 장 족장, **Great Hero** for 대협, and **Captain** for 조장님.
- Retain **underground prison**, **iron balls**, **Bone-Shrinking Technique**, **Black Dragon Saber**, **Scorching Yang Qi**, and **sever one’s own heart meridian**.

## Durable state

{
  "active_continuity": [
    "Jin remains in the Nanman Beast Palace's Inner Palace as the Third Young Master of the Jin Family of Taiyuan and head of the Fire Dragon Pavilion.",
    "The Fire Dragon Pavilion was attacked after Jin left, and Dark Heaven is suspected of organizing or enabling the assault.",
    "Yohi's Western Yao Estate was attacked by a Supreme Peak master, and Heugung and Yohi remain missing after a third party apparently abducted or confronted them.",
    "Baeksang has accused Jin of the Inner Palace massacre and demanded his arrest, while the Beast Miao King halted the attempted arrest.",
    "Jin chose apparent surrender to protect his companions and punched Baeksang immediately beforehand.",
    "The reconnaissance squad is racing south through Guangxi to stop the Blood Monk, who may cross the region and head south.",
    "The Nanman Beast Palace sent a palace-sealed missive ordering the two tribal chieftains to turn the reconnaissance squad against Song Ilseom and Hyuk Mujin.",
    "Ju Hwaran is alive but has been subdued with a Pressure-Point Strike.",
    "Song Ilseom and Hyuk Mujin have been disarmed, bound, and captured by the reconnaissance squad.",
    "Song Ilseom suspects that a major incident occurred in the Inner Palace and blames Jin Taekyung for it."
  ],
  "continuity_sources": [
    659
  ],
  "open_questions": [
    "What happened in the Inner Palace, and why did the Nanman Beast Palace issue the sealed order?",
    "Where is Ju Hwaran being held, and what will happen to her?",
    "Can Song Ilseom and Hyuk Mujin escape captivity?",
    "What consequences will follow Jin's apparent surrender and the accusation surrounding the Inner Palace massacre?"
  ],
  "safe_through": 659,
  "temporary_decisions": [
    "Retain Force for 강기 and Supreme Peak for 초절정.",
    "Retain Sound Transmission for 전음 and Either-Or for 양자택일.",
    "Retain underground prison for 뇌옥 and iron balls for 철구.",
    "Use Chief Jang for 장 족장."
  ],
  "version": 1
}

## Reading copies

## Chapter artifact 655

# Chapter 655

Nanman was like a small country separated from the Central Plains, and the Nanman Beast Palace could be considered the royal palace at the heart of that country.

Naturally, the Inner Palace was enormous as well.

When the warriors, cooks, servants, beast keepers, and everyone else who lived in the Inner Palace were counted together, their number reached a thousand. And whenever the Tribal Grand Council was held, that number swelled several times over.

But even among all those people, there were some who mattered more than the rest.

The four great chieftains.

They led the four strongest tribes among the thirty-two tribes of Nanman and possessed enough power to become the next Palace Lord of the Nanman Beast Palace.

As befitted their position, the great chieftains wielded tremendous influence. Apart from the Palace Lord, the other three great chieftains had been guaranteed special privileges for generations.

Whoosh!

Just as Yayul Mok, running beside me, was explaining.

“Every chieftain other than Father remains at their tribe’s main base and must notify the palace in advance before entering the Inner Palace. But the great chieftains are exceptions. They have free passage, as well as residences within the Inner Palace.”

East, west, south, and north.

The northern residence had traditionally belonged to the Palace Lord of the Nanman Beast Palace, while the other great chieftains had each established their own residence in a different direction.

They were a kind of official residence granted to high-ranking figures. In Central Plains terms, it was as though the Son of Heaven had allowed his vassal princes to establish their own princely residences.

But what awaited me at that moment, after I had run there at full speed, was a pool of blood spread across the ground, corpses, and the wreckage of buildings destroyed by someone.

“What the…”

Namho’s groan pierced my ears. I raised my head, feeling as though all the blood in my body had turned cold.

A wooden plaque tilted over the shattered gate, with three characters written on it.

Western Yao Estate.

The three words revealed who owned the estate. For a moment, the image of a woman with captivating eyes curved into a smile flashed before me.

*The great chieftain of the Yao people. Yohi.*

She was a woman for whom the word bewitching suited her better than beautiful.

I did not know whether she was truly the culprit behind the attack that had taken place tonight, but two things were certain.

The splendid estate, so thoroughly filled with Yohi’s tastes, was no longer beautiful as it had once been.

And she had vanished without a trace.

Step.

As I crossed the half-destroyed gate, I saw corpses scattered everywhere, along with the bodies of beasts.

The colorful flower beds, which must once have possessed every shade imaginable, had been soaked in red blood.

“…Damn it.”

Just as I muttered the curse under my breath, one of the warriors who had spotted Yayul Mok walking beside me approached.

“Have you arrived, Young Palace Lord?”

Yayul Mok nodded with a grim expression.

“You’ve worked hard. Have you found anything else?”

“No. Apart from the number of corpses increasing.”

Beyond the warrior’s back, I saw bodies lying side by side. Not far away, three or four warriors were pulling a tiger out of a well, its drenched body hanging limp.

“To tell you only the number confirmed so far, there are at least a hundred Yao warriors and beasts under their command.”

“Any survivors?”

The warrior was silent for a moment before answering Yayul Mok’s question.

“…At present, there are none.”

*At present?*

*Well. I think there won’t be any in the future either.*

I muttered inwardly as I approached the bodies.

One of the warriors reflexively tried to block my path, but when our eyes met, he flinched and stepped aside. I examined the wounds on the corpses.

How they had fought the mysterious attackers.

And how they had met their deaths.

Then, just as I realized something, I heard Yayul Mok’s voice.

“Did you find anything?”

At the same time, I felt dozens of pairs of eyes turn toward me and answered briefly.

“Force.”

“……!”

“……!”

Invisible agitation spread through the crowd. I continued in a rigid voice.

“The attacker was undoubtedly a Supreme Peak master. Most of these people probably didn’t notice the ambush until the very last moment. That’s how vast the gap in martial arts must have been.”

The Supreme Peak realm was a domain granted only to a tiny number of chosen individuals.

After countless hardships, Supreme Peak masters crossed the wall and rose into a great realm. They became superhuman in the truest sense of the word.

With a single swing of the sword, they could kill dozens of First Rate masters. Even with their bare hands, they could turn a dozen Peak masters into bloody pulp.

The culprit who had attacked this place tonight had been exactly that kind of person.

*Extremely fast and simple, yet utterly lethal.*

I had realized it the moment I saw the wounds left on the bodies. The culprit was a thoroughly seasoned killer.

With neither too little nor too much force, they had slaughtered every living thing inside the estate.

Everyone in the Murim knew that a depth of one inch was enough to take a life. But only a Supreme Peak master could massacre a hundred warriors and beasts.

And what that meant was clear.

—Are you saying Baeksang did all this?

A low Sound Transmission slipped into my ear. I looked at Yayul Mok’s face, stiff with shock among the gathered people.

—Who knows?

—What do you mean, who knows?

—There are only two masters in Nanman who have reached this level. One is Baeksang, as you know. The other is… someone everyone in Nanman knows well.

For an instant, I saw Yayul Mok’s face turn deathly pale. He opened his mouth as though he were about to shout, then bit down hard on his lip.

—Are you saying Father is the culprit behind this?

—No way.

—Then why…

—I’m saying it would be too obvious if it were that simple. At the very least, Dark Heaven’s direct involvement is certain.

A Supreme Peak master was exceedingly rare even in the Central Plains, but even more so in Nanman. Even if I personally suspected Baeksang, he wasn’t this much of a blockhead.

They had probably mobilized at least one Supreme Peak master belonging to Dark Heaven.

*They seemed content to watch the situation from a step away. Have they finally decided to act directly?*

*But what are they after?*

I muttered the question inwardly, then asked aloud instead of using Sound Transmission.

“There’s something I want to check personally. Should we move somewhere else for a moment?”

Yayul Mok understood what I meant and gave a signal with his eyes. The surrounding gazes fell away.

The three of us—Yayul Mok, Namho, and I—entered the pavilion at the center of the estate.

And the interior, which everyone had expected to be filled with all kinds of rare furnishings, was a complete mess, as though a storm had swept through it.

“Looks like they had a proper fight.”

At Namho’s mutter, Yayul Mok answered with a grim expression.

“But the battle ended in a matter of moments. That was only natural, since the opponent was a Supreme Peak master.”

“How do you know?”

“Because I heard a short but unmistakable boom. By the time I heard the report and arrived, everything was already over. All that remained in the Western Yao Estate was blood, corpses, and…”

Creak.

Yayul Mok flung open a large sliding door and continued in a subdued voice.

“Those.”

The things he called “those” were two objects.

A scent pouch lying on the floor of the wrecked room.

And something whose use was more valuable than the pouch’s, and which gave off a terrible smell.

“Hmm.”

Namho groaned, while I walked over without hesitation and touched *it*. The cold sensation of flesh gone cold met my fingers, and sticky blood dampened them.

*This is…*

Anyone with eyes could identify the object.

*It* was a wrist.

Someone’s wrist, cleanly severed.

“Can you tell whose it is?”

How could I not?

I stared silently at the plump wrist as Yayul Mok asked the question, then muttered in a low voice,

“It’s probably Heugung’s.”

“You’re right. I heard he came to find the great chieftain Yohi with four guards. The Eastern Yi Tribe confirmed it.”

If the Yao people had established the Western Yao Estate in the west, then the Yi people led by Heugung must have settled in the east and established the Eastern Yi Estate. I set down Heugung’s wrist and asked,

“What time was that?”

“They said it had been less than half a shichen, but at least half an hour had passed.”

I roughly calculated the time. It had been right after Heugung and I parted. He must have gone straight to the Eastern Yi Tribe first, then come to find Yohi.

*…That lovesick bastard. He couldn’t even wait that long.*

I had to struggle to keep the curse from bursting out of my mouth. This was no time to lose my composure.

I still did not know why Heugung had gone to find Yohi. And until his death had been confirmed, I had to suspect everyone.

“What about the guards Heugung brought?”

“They’re dead. Along with the other Yao warriors.”

*Of course they are. Fuck.*

I had asked just in case, but the expected answer was still the expected answer.

“Phew.”

After letting out a deep sigh, I slowly surveyed the room.

Signs of resistance remained throughout the wrecked interior. Beyond a wall that had probably collapsed beneath powerful palm force, I could see a rear garden that had retained its splendid appearance.

And faint footprints remained there as well.

*They subdued the two of them quickly, then escaped through the rear garden.*

The traces were too faint to identify their owner, but they made one thing certain.

This had not been a staged attack carried out by either Heugung or Yohi. A third party had intervened.

Less than half an hour ago, there had been at least three people in this place.

*One of them was naturally a Supreme Peak master.*

Then who did the footprints belong to?

The Southern Heaven Demon Empress?

Or one of the Dark Heaven masters under her command?

After thinking for a moment, I shook my head.

I was not some battle-hardened old veteran of the martial world, and there was a limit to how much information I could obtain from clues like these.

Namho, who had spent his time as an agent of the Hidden Shadow Pavilion and encountered countless pieces of information, was beside me. But his knowledge was limited to descriptions of fiends’ appearances and outward characteristics.

*In the end, I need someone with both a high level of martial arts and a high level of insight.*

Only two names came to mind immediately, and one of them was someone I could never bring myself to trust.

After finishing my thoughts, I turned to Yayul Mok.

“When will Great Hero Yayul arrive?”

“I’ve already sent someone to notify him. By now, he should be on his way with the other chieftains.”

That was welcome news.

For the sake of preserving the scene, I returned Heugung’s wrist to its original place, then smelled the pouch Yohi had left behind.

Perhaps because the side of the silk pouch had split, only the faintest scent lingered. It was almost odorless.

*I’ll uncover the truth. I have to.*

And at that very moment, when I was muttering inwardly—

A commotion arose outside the pavilion.

“Father must have arrived at last. If it’s him, he may know the culprit’s identity.”

But before I could even leave the pavilion, I realized that Yayul Mok was wrong.

The first person to arrive was not the Beast Miao King, and the identity of the culprit he mentioned belonged to someone I had never expected.

“The guilty party is coming out on his own.”

The moment I heard Baeksang’s emotionless voice, I understood.

The Supreme Peak masters capable of carrying out something like this in Nanman were not limited to Baeksang and the Beast Miao King.
## Chapter artifact 656

# Chapter 656

Everything was silent.

The warriors gathering the corpses.

The tribal chieftains who had clearly just arrived.

Not a single person was the exception. Everyone in the Western Yao Estate had stopped moving and was staring at this place.

No—their gazes were focused on only one thing.

Me.

And then, the next moment—

“The culprit is walking out on his own two feet.”

A cold voice rang out, shattering the silence.

The instant I met Baeksang’s deeply sunken eyes, a hollow laugh escaped me before I knew it.

“Ha.”

The realization came like a flash of light. I no longer needed to think about how this situation was unfolding.

Everything was contained in the one sentence Baeksang had offered in place of a greeting.

*The culprit.*

For a moment, I had forgotten.

I, too, fit every condition of the culprit.

I should not have been holding up a lantern and searching the distance. I should have been looking at the ground beneath my own feet.

“Uncle Baek, what do you—”

Yayul Mok was looking at Baeksang with a puzzled expression when he realized something and fell silent. Namho, who had perhaps grasped the situation even faster than I had, let out a quiet sigh.

“Huh. I must be getting old. I can’t believe I fell for such a shallow trick.”

Namho was only half right.

This was undoubtedly a shallow trap, but the pit dug beneath it would be deep.

Deep enough that once I stepped inside, I would not be able to climb out easily.

*Damn it.*

I felt as though I had sunk into a swamp. My chest felt tight, and my mouth was gritty, as though I were chewing sand.

I closed my eyes briefly, then opened them again. The situation around me had transformed into a courtroom, and I could see it all with perfect clarity.

“Did you hear what Great Chieftain Baeksang just said?”

“He called him the culprit. Then could that Han Chinese man really be…?”

The warriors whispered in low voices here and there. In this place, they were the spectators.

“I knew this would happen. Didn’t I keep saying from the beginning that we should drive the Han Chinese out?”

“Hm. Even so, it’s too early to jump to conclusions.”

“Too early? How can you say that in a situation like this? The only person capable of committing such a crime is that man, Jin Taekyung!”

Unlike the whispering warriors, the chieftains raising their voices to denounce my crimes were the jury.

And then—

“How bold. As if you haven’t done anything wrong.”

Baeksang, who had opened his mouth before everyone, was the judge of this damn trial.

I looked at his utterly impassive expression and parted my lips.

“I have no choice but to be bold. I haven’t done anything wrong.”

At this point, it was laughable to discuss manners.

One of the chieftains flared up at my brief answer and shouted,

“You bastard! How dare you—!”

“How dare I what?”

Ssshhk!

As I spoke, the wave of qi I released shot toward the chieftain. The chieftain who had stepped forward went as pale as a sheet.

“Ghk.”

I was already balanced atop a hundred-foot pole.

One wrong step, and I would fall.

If I surrendered the initiative to the flow of events, it would all be over.

I quietly released an overwhelming wave of qi and spoke.

“This isn’t a place where any dog or cow can butt in. Sit down and stay out of it.”

“……!”

Gulp.

And it was at that moment, when someone’s throat bobbed heavily, that—

“This is noisy.”

A deep voice carried over the wind.

At the end of the gazes of the people who turned their heads reflexively, a man everyone knew was walking through the gate of the Western Yao Estate.

*The Beast Miao King.*

His tiger-like eyes were wide open, and his body was as immense as a mountain ridge.

He radiated pressure as imposing as Mount Tai itself. At his appearance, everyone present hurriedly dropped to one knee.

“We pay our respects to the Palace Lord!”

Their voices rang out as one.

Amid the reverence of everyone present, the Beast Miao King slowly advanced with several other chieftains behind him. Then he suddenly opened his mouth.

“Am I included among those dogs and cattle you mentioned?”

It was obvious who he was asking. I shook my head.

“No.”

“Then I have a question.”

The Beast Miao King’s deeply lowered voice pierced my ears.

“Jin Taekyung of the Jin Family of Taiyuan. What connection do you have to this tragedy that occurred here today?”

The Beast Miao King had asked the question not to interrogate or suspect me, but to help me.

I knew that better than anyone, so I answered without hesitation.

“None whatsoever.”

My immediate answer drew whispers from all around us.

And then, the next moment, one person who had been silently paying his respects to the Beast Miao King rose to his feet.

“Last year, a fire broke out in the western forest. It happened because of the carelessness of drunken Bai warriors, and as a result, more than two hundred livestock and more than thirty houses burned down.”

Baeksang continued in a dry voice.

“If a crime has been committed, punishment must follow. Thus, I had to cut down seven of my fellow warriors with this hand. But when I told them to leave their final words before their executions, every one of them said the same thing.”

His emotionless eyes were looking at me, but his next words were directed at the Beast Miao King.

“I am innocent. I did not drink, and I did not start the fire.”

“……!”

“Two great chieftains have disappeared from the Inner Palace, and more than a hundred warriors have been massacred. This is not a situation that can be escaped with a single shallow excuse.”

The Beast Miao King slowly closed his eyes. I stared at Baeksang and opened my mouth.

“Listening to you, I’m starting to feel rather strange. It seems I’ve already become the culprit without even knowing it.”

“If you are truly innocent, prove it.”

“Prove it?”

“That’s right. It is the simplest and easiest method. If you produce evidence that you are not the culprit, then the matter will be resolved.”

I did not even have time to answer.

The moment Baeksang finished speaking, he turned around and shouted toward the crowd, which had been murmuring over the exchange.

“I, Baeksang, great chieftain of the Bai people, wish to establish my own innocence before interrogating the culprit. Heaven and earth, along with the fifteen chieftains and the hundred warriors who were with me, will all attest to it!”

“……!”

*Damn it. Was this what he had been aiming for from the beginning?*

I had fully expected Baeksang to have established a sufficient alibi, but the timing and flow with which he revealed it were too perfect.

As though they had been waiting for this very moment, the chieftains following Baeksang raised their voices more loudly than anyone.

“Palace Lord, I report to you. Every word spoken by Great Chieftain Baeksang is the complete truth. He remained with us at the Southern Bai Estate immediately after the banquet ended.”

“The Jingpo Chieftain is correct! I, along with the Lahu people, swear it before Heaven!”

“The Wa people will also vouch for Great Chieftain Baeksang! Around the time the tragedy occurred, we were meeting to prepare for tomorrow’s Tribal Grand Council!”

The chieftains’ responses erupted from every direction. Namho, standing behind me, let out a low groan, while the Beast Miao King’s expression grew heavy.

Nearly half the chieftains were openly declaring that they had joined a particular faction, but at this moment, no one—not even the Beast Miao King—could point it out.

Two great chieftains had disappeared from the Nanman Beast Palace.

And close to a hundred people had been brutally slaughtered in the Inner Palace, of all places.

This was an enormous matter of state—serious enough that the factional struggle, which had become an open secret, could be treated as nothing more than a ripple on the water.

And then…

At last, the moment arrived.

“Jin Taekyung of the Jin Family of Taiyuan. Now I will ask you. Where were you at that time?”

An unavoidable question.

An answer I could not refuse to give.

I could feel Baeksang’s question, along with the gazes of the people around me, wrapping around my entire body like an invisible noose.

And at the same time, someone’s hand touched my waist.

Tap.

I did not make the foolish move of turning my head to check.

I already knew that the owner of that hand was Namho, who had been standing behind me all this time.

*But why?*

There had to be a clear reason for Namho’s actions.

I sharpened my senses to their limit and continued to feel the movement of his fingers.

It lasted only a short while, and the movement was so faint that it merely brushed against my clothes, but I soon understood what he was trying to convey.

*This is…*

He was writing.

Two short characters with a clear meaning.

*No words.*

Namho was telling me not to say anything.

Or perhaps he meant for me to think one more time about what I was about to say.

That was how ominously the situation was unfolding.

*What if I tell them the truth about meeting Heugung?*

Would they even believe me?

No. There was a strong possibility that Baeksang and the chieftains following him would counterattack instead.

Heugung had said he slipped out of his residence without anyone noticing, and he had even changed his appearance with the Bone-Shrinking Technique.

*In short, I can’t prove it.*

If Heugung were here, it might be different. But unless the wrist he had left behind could testify for me, I had to consider proving my alibi impossible.

But saying that I had left my quarters for no reason would be like digging my own grave.

In the end, the answer I could give had been decided from the very beginning.

“My quarters.”

Countless thoughts flashed through my mind, but little time passed. I answered without much delay, then took a deep breath and continued.

“I remained in my quarters immediately after the banquet ended. Then I was attacked.”

“Attacked?”

There were still more people who had not heard about it than those who had.

The crowd began murmuring at the new information, and the Beast Miao King spoke with a stiff expression.

“What Jin Taekyung says is true. I, too, heard a report that assassins whose tribe could not be identified had targeted them.”

Yayul Mok, who had been shaken by this sudden turn of events, followed up in a voice that was deliberately calm.

“That is correct. Some of the Inner Palace guards, myself included, arrived at the scene about half an hour ago. We also confirmed that the warriors patrolling the area had been killed.”

After the Beast Miao King, Yayul Mok also came to my aid, and the murmuring around us grew louder.

But I had been staring at one person the entire time—Baeksang. And I realized once again that things had gone wrong.

“I also heard that another tragedy occurred in the Inner Palace.”

Baeksang murmured in a cold voice, his eyes utterly impassive, then continued toward Yayul Mok.

“But to infiltrate the Inner Palace so easily, eliminate the patrolling warriors, and launch an attack… Those unidentified assassins must have been quite strong. Wouldn’t you agree?”

Before I had time to stop him, Yayul Mok’s lips parted.

“That’s right. There were around thirty assassins, and every one of them was as skilled as an elite warrior—”

Yayul Mok’s words did not reach the end.

No—they could not.

Because Baeksang’s voice pierced everyone’s ears in the next moment.

“Strong enough to kill a Supreme Peak master who inherited the Fire King’s legacy?”

“……!”

“……!”

“If this clumsy assassination attempt was intended to tie Jin Taekyung down, that would be just as difficult to understand. He was going to remain in his quarters even if left alone, so they deliberately attacked him and drew everyone’s attention. Isn’t it strange the more you think about it?”

The air around us churned. Dozens of pairs of wide-open eyes shot their gazes at me, and my face prickled beneath them.

But in contrast, my heart grew calmer.

Was it because I was confident I could escape this crisis?

No.

I had already half accepted the situation.

This trap was large and deep—far beyond anything I had imagined.

*When did it begin? How much of this was part of the plan?*

I stared at Baeksang, my unanswered questions weighing on me, then suddenly opened my mouth.

“I don’t think this is the end.”

Baeksang immediately understood what I meant and nodded.

“Good instincts.”

“Do you still have something to say?”

“No. But I do have something to show you.”

Snap.

With his dry answer, Baeksang snapped his fingers. From the half-destroyed gate of the Western Yao Estate, a faint presence began to draw closer.

Step. Step.

The footsteps were slow, with short and irregular strides.

Like someone who was ill.

Or perhaps—

*Like an elderly man.*

I recognized the owner of the strangely familiar presence and slowly closed my eyes. Then, when I opened them again to the sound of an old man’s voice—

“B-Bai people’s Utu-ri. I came at the great chieftain’s summons.”

The old owner of the noodle shop was standing in front of the Western Yao Estate’s gate.
## Chapter artifact 657

# Chapter 657

*Something big is coming.*

The instinct that flashed through my mind was not wrong. The old owner of the thin-noodle shop where I had been sitting with Heugung just moments ago had appeared.

*Fuck.*

Something really big had come.

I cursed inwardly as I stared at the old shopkeeper.

No, I was not the only one looking at him. As countless gazes instantly converged on him, a trembling voice emerged from between his age-spotted lips.

“U- Utu-ri of the Bai people. I came at the great chieftain’s summons.”

The Beast Miao King spoke with a grim expression.

“I’ve never seen this face before. Who is he?”

At Baeksang’s signal, the old shopkeeper hurriedly answered.

“I sell thin noodles near the West Gate of the Outer Palace. I’ve made a living at it for more than half my life.”

From the old shopkeeper’s words and actions, I learned several new things.

First. The old shopkeeper’s name was Utu-ri, and he was a member of the Bai people.

Second. Unlike when I had seen him at the noodle shop, Utu-ri spoke clearly and had excellent hearing. In short, he was full of energy. If Jirisan had its baby hero Utu-ri, Nanman had a noodle-selling Utu-ri.[^1]

Third. This Bai elder, whose vitality belied his age, had probably told Baeksang everything he had seen and heard.

And fourth. I was probably completely screwed.

*You have to understand. The owner here is over ninety, so his hearing is bad.*

*You fucking bastard, Heugung.*

What he had said at the noodle shop had been wrong. Very wrong.

*His hearing is bad, my ass.*

The thing that had grown dim was my future.

The shopkeeper, who was supposedly over ninety, had hearing sharp enough to catch every word spoken by the Beast Miao King ten paces away.

“Utu-ri, there is one reason I called you here. I wish to confirm one fact. Do you recognize anyone among those gathered here?”

“Yes.”

The old shopkeeper nodded without hesitation at Baeksang’s question, and I realized I had to add one more item to the list of things I had learned.

Fifth. Utu-ri possessed not only excellent hearing, but also remarkable eyesight and memory.

The reason I could guess that much was simple.

From the moment the old shopkeeper had first set foot in the Western Yao Estate, his gaze had kept darting toward my face.

“That young man standing over there. The tallest one, with the largest build.”

The hand that had trembled like an aspen tree when he set down the bowls of noodles was, for some reason, perfectly still this time.

*Damn it.*

His finger pointed directly at me. I shut my mouth, the atmosphere around us began to stir, and the script Baeksang had meticulously prepared raced toward its conclusion.

“Are you certain it was him? There must not be the slightest lie in your answer.”

The old shopkeeper swallowed hard before answering Baeksang’s question.

“Yes, without a doubt. I may be old and worn-out, but I’m not so blind that I can’t recognize a customer standing right in front of me. His build was exceptionally large, and he was wearing a tiger mask, so he stood out in my memory.”

“Half the people in the Outer Palace must be wearing masks right now. Did you report him as suspicious for no reason beyond that?”

“N-No, that wasn’t it. He lingered nearby, then sat down and ordered noodles. That was when I began to feel something was strange.”

“Strange? What exactly was strange?”

The old shopkeeper, who had been glancing at me, continued cautiously.

“It was because of the mask, sir.”

“The mask?”

“Yes. Even while eating the noodles, he never took it off. It was as if something terrible would happen if he showed his face.”

“I see. Continue.”

“But later, when he drank the broth, the mask must have felt too restrictive, because he raised it slightly. That was the first and only time I saw his face.”

So that was when it happened.

If I openly revealed my face, they might realize I was Han Chinese. But if I never removed the mask, I would arouse suspicion.

So I had deliberately raised it only to just below my nose while eating the noodles, then lifted it properly for a moment at the very end…

*Who would have thought that old man, who looked like he could die tomorrow, would notice and remember that?*

At first, my excessive caution had drawn suspicion. Later, overlooking the existence of the old shopkeeper had brought me to this situation.

And now Baeksang was putting an end to it all in his uniquely calm voice.

“Were you alone?”

“No. He was sharing a table with some middle-aged man.”

“Another middle-aged man. What happened after that?”

“They left almost at the same time, then headed toward the main road by the West Gate.”

“Do you remember that man’s face?”

“Yes, of course. I’ve lived in the Outer Palace all my life, but he was a stranger I had never seen in the area, so I remember him vividly. The same goes for that young man.”

“Then they were certainly outsiders who entered during the Tribal Grand Council. If we make likenesses of them and investigate, it should be easy to identify them. When did they leave?”

“It was around Insi, and they stayed for about the time it takes to drink a cup of tea before leaving. The Outer Palace has been setting off firecrackers at regular intervals, so I remember the time clearly.”

The old shopkeeper answered without a single hesitation. His eyes and voice were filled with certainty.

Having obtained every answer he wanted through the old man, Baeksang gave a small nod.

“Thank you for your cooperation. You may withdraw now. I’ll have someone give you a reward separately.”

“Th-Thank you. Thank you, Great Chieftain!”

The old shopkeeper bowed repeatedly as he disappeared.

He would probably receive an extremely generous reward for what he had done here. The small stall that had been packed whenever three or four customers showed up would become a large inn, and the wrinkled hands that had boiled noodles would soon be counting silver nyang.

But the opportunity he had seized in his old age had returned to me as the worst crisis of my life.

“What a strange matter. Someone who should have been in the Inner Palace secretly slipped out, made contact with an unidentified figure, and then this tragedy occurred immediately afterward.”

“……”

“Your earlier statement has already been exposed as a lie, but even considering what happened at Ailao Mountain, I will give you one final opportunity. Do you wish to make a defense?”

In the brief moment Baeksang’s low voice pierced my ears, countless thoughts flashed through my mind.

By then, the Western Yao Estate had fallen into suffocating silence, and everyone’s gaze was fixed on my face.

That was when it happened.

Namho’s finger brushed against my back once again.

Sssrk.

*Escape.*

It was only one word, but I understood exactly what Namho meant.

*Get out of here first. We’ll make plans for later.*

If Namho had known martial arts, he would have sent me this kind of Sound Transmission. If I had been in his position, I probably would have done the same.

*Would things have improved if I had simply told them the truth?*

I answered my own sudden question.

No.

Of course, things might have been a little better than they were now. But Baeksang had prepared thoroughly. He would have driven me into a situation like this somehow.

I could insist that the old noodle-shop owner’s statement was a lie, but… please. If Baeksang were stupid enough to fall for that so easily, he never would have made it this far.

*Besides, a master like Baeksang would realize just by looking at the wounds on the assassins who attacked us that most of them weren’t my handiwork.*

Without Heugung there to corroborate my statement, telling the truth would only make me a shameless culprit.

*Though I suppose that would still be better than being a culprit caught lying.*

Either way, I was trapped. There was no way to avoid it.

And even now, the situation was racing toward the edge of a cliff.

Sssrk.

A faint sound pierced my ears through the brief silence.

Blood-soaked grains of sand were crushed beneath leather shoes, while dozens of fluttering hems brushed against the flowers in the garden.

An encirclement had formed around me in an instant.

At its head stood Baeksang.

“I’ll ask you again. Do you wish to make a defense?”

A defense.

After thinking long and hard, I answered.

“I’m not doing it. This whole thing is too damn filthy, you fucking bastard.”

“……!”

“……!”

They probably had not expected an answer like that. Baeksang looked at me with surprise, then nodded.

“Are you admitting your guilt?”

“I admit only that I lied. I was stupid.”

“So in the end, you mean to deny it to the very end.”

“If you were me, would you admit it? No. I didn’t commit a crime in the first place, so there’s nothing to admit. It just pisses me off that I stepped into an inescapable trap.”

“If you believe you have been wronged, surrender quietly. I will determine right and wrong.”

“Yeah, fucking right, you right-and-wrong bastard.”

At my scornful reply, Baeksang’s eyes sank into darkness.

“Then it cannot be helped.”

At the same time—

Shing. Tsstststst!

A dazzling radiance surged from the pure-white blade he drew in a flash. Baeksang lowered his treasured sword, infused with Sword Force, and slowly stepped forward.

“The warriors of the Nanman Beast Palace, listen. From this moment onward, we will use our full strength to take the criminal Jin Taekyung into custody. Not a single mistake will be tolerated—”

At that moment, a roar-like shout erupted from somewhere, drowning out the words that were about to leave Baeksang’s mouth.

“Baeksang!”

Only one person in all Nanman could address the great chieftain of the Bai people that way.

“Will everyone stop this at once!”

Whoosh!

A powerful wave of aura pressed down from every direction.

The Beast Miao King halted the slowly tightening encirclement with a single command, then glared at Baeksang with blazing eyes.

“What do you think you’re doing?”

Everyone trembled beneath his fierce aura, but Baeksang did not. He answered in a calm voice.

“You can see exactly what I’m doing, Palace Lord. I intend to take the criminal Jin Taekyung into custody here.”

“Have you forgotten? He is a pavilion master of the Murim Alliance and a member of the Fire Gate Clan, our longtime ally.”

“Are you, of all people, the Palace Lord of the Nanman Beast Palace, shielding the culprit for no reason beyond that?”

“Ridiculous! That boy is not the culprit. Have you already forgotten what happened at Ailao Mountain? He has neither the justification nor the reason to do something like this!”

“But we have a witness who saw him, as well as clear circumstantial evidence.”

“But—”

“Everyone here remembers what happened at Ailao Mountain clearly, myself included. That is why I am taking the trouble to place him under arrest. Of course, if he resists, the order will be to take him dead or alive.”

“Baeksang!”

“We are not finished yet.”

Baeksang’s cold voice continued.

“If Jin Taekyung leaves this place by force, I will spread a net over heaven and earth across all Nanman and pursue him with everything we have. Before that happens, the other Han Chinese under his command will make excellent examples.”

“……!”

The Beast Miao King’s eyes widened at the meaning behind Baeksang’s words—he was prepared to risk war with the Central Plains.

Yayul Mok shouted with a twisted expression.

“Uncle!”

“This is a conversation between tribal chieftains, not between lord and subject. The Young Palace Lord, who has no authority here, should withdraw.”

“But how could you! How could you dare make such a unilateral decision on your own!”

“A unilateral decision…”

Baeksang muttered the words softly, then suddenly raised his head and looked at the sky.

The thick darkness that had settled over the surroundings had begun to disperse, and bright light was slowly spreading from the east.

“Can you see it? It is already the hour of the Rabbit. Dawn is breaking.”

“What does that have to do with this all of a sudden?”

“What would you say if we began the second day of the Tribal Grand Council right here and now? Of course, the new agenda would be…”

Tsst.

The sword in Baeksang’s hand blazed with even more intense light.

“Whether Han Chinese Jin Taekyung lives or dies.”

At that moment, a sound like a bell that only one person in this world could hear pierced my ears.

Ding.

> **System**
>
> An unexpected **Quest**, **Either-Or**, has been generated!

[^1]: Utu-ri is a legendary Korean child hero associated with Jirisan. Jin is comparing that figure to the elderly noodle seller who happens to share the name.
## Chapter artifact 658

# Chapter 658

Ding.

A System notification suddenly rang out. At the same time, a translucent holographic window shot up into the air.

> **System**
>
> An unexpected **Quest**, **Either-Or**, has been generated!
>
> **Quest**
>
> **Either-Or**
>
> Only two choices remain to you now.
>
> Will you resist with all your strength and escape this place? Or will you surrender quietly and allow yourself to be captured by them?
>
> The choice is entirely yours, and every choice will be followed by a corresponding result.
>
> **Grade:** None
>
> **Restriction:** Jin Taekyung
>
> **Mission:** Surrender or Resist (Incomplete)
>
> **Reward:** ???
>
> **Failure:** ???
>
> - This Quest contains two choices, and you must select exactly one of them.
>
> - Various factors around you will change depending on your choice. A certain person may die in the process.
>
> How will you proceed?
>
> Surrender / Resist

I had only one thought after checking the System window.

*What a shitty situation.*

Either-Or.

The Quest that had suddenly activated contained exactly what its title said.

Would I surrender? Or would I resist?

There were only two choices, and I had to choose one of them.

The current situation—and the owners of the voices rising from every direction—demanded it.

“I agree with Great Chieftain Baeksang.”

“Exactly! If the Palace Lord thinks this is an arbitrary decision, then let us convene the Tribal Grand Council right here and now!”

“If he is innocent, he should surrender quietly and submit to an investigation. What is the problem?”

As I listened to the shouts of the tribal chieftains who belonged to the pro-Baeksang faction, a hollow laugh escaped me.

*What is the problem?*

The biggest problem was that this was Murim, not the modern world.

Even in the twenty-first century, where all kinds of judicial corruption took place, it was obvious what would happen to me if I were detained under Baeksang’s orders.

*They’ll brand me a criminal from the beginning and force the entire process to end that way.*

There would be no fairness or impartiality to be found anywhere along the way. The lie I had told without thinking had already been exposed, and Baeksang had produced both a witness and clear circumstantial evidence.

This was a carefully dug trap. Once I stepped into it, I could only fall.

Of course, even in this situation, there were those who reached out to me.

“You’re all insane. Have you lost your minds? You intend to execute Jin Taekyung? Are you planning to start a war with the entire Murim of the Central Plains?”

“Moreover, it has not even been established that he is truly the culprit. Why would the Pavilion Master of the Murim Alliance and the Fire King’s Disciple do something like this?”

“He rescued no fewer than two hundred warriors from Ailao Mountain. And you claim he is the culprit? Even if you hate the Han Chinese, how can you act like ungrateful beasts?”

This time, the shouts of the tribal chieftains who followed the Beast Miao King rang out.

But among the dozen or so of them, only a few actually stepped forward. Quite a few chieftains chose to watch the situation with confused expressions or kept their mouths firmly shut.

*Of course. In the end, I’m still an outsider.*

The Nanman people had never held particularly favorable feelings toward the Han Chinese.

The only reason I, a Han Chinese man, had been allowed to attend the Tribal Grand Council in the first place was because of what I had accomplished at Ailao Mountain. That was exactly where the extent of what they were willing to permit ended.

I had no intention of blaming them. They were simply reading the way the tide was turning.

Even if the Tribal Grand Council were convened here and now, as Baeksang had suggested, there was no way to overturn this situation.

Not even for the Beast Miao King.

*I think I’m pretty fucked.*

The Beast Miao King’s brow furrowed deeply as he heard the Sound Transmission I had sent him.

*You crazy bastard.*

*Why?*

*You can still joke at a time like this?*

*I’m just telling the truth. It’s not like I can sit here bawling like a child. It won’t make the situation any better.*

At my Sound Transmission, which calmly faced reality, the Beast Miao King bit down hard on his lip.

*I’m sorry. If the Tribal Grand Council is held as Baeksang says… there will be nothing I can do.*

*Still, it’s a relief that Great Hero Yayul seems to believe me.*

*Of course I believe you. That is why I am even more sorry.*

*Then don’t just be sorry. Could you punch those bastards in the mouth once each? If that makes you uncomfortable, I’ll do it.*

*……*

*Or maybe use Flame Divine Palm.*

*Hah. At this point, you may as well be Old Master Jeok’s flesh and blood rather than his Disciple.*

Jeok Cheongang.

At the three syllables of his name, a familiar face suddenly flashed before my eyes, and my mouth turned bitter. If Jeok Cheongang were in this situation, how would he have handled it?

*No. If it were Old Master Jeok, things never would have reached this point.*

I was nowhere near as strong as Jeok Cheongang. I was still so inexperienced that my belief I had grown accustomed to Murim seemed laughable, and my enemies had been more thorough and cunning than I had imagined.

*If this were Go… my actions would probably count as a bad move.*

I didn’t know how to play Go. But when I was young, my father would sometimes sit in front of the computer and play online.

His username was Jin Sedol, but his win rate was terrible. Whenever he lost to a user from China, he would mutter, “That Chink bastard plays Go like shit… Taiwan number one,” before Mom smacked him across the back.

She told him not to swear in front of the kid.

It was all a stale memory from the distant past.

A few years later, my father died suddenly in a monster wave, and the Go account he had kept playing on despite its long record of defeats fell dormant.

But why was it that, all of a sudden, I remembered that day when I had watched my father losing at Go?

*Dad. Are you losing again?*

*What do you mean, “again”? Dad only lost this game. No, it isn’t even over yet.*

*But you lost yesterday and the day before that, too. And I saw you losing earlier!*

*……My adorable boy. You’ve grown up so fast, and now you’re driving a nail into your father’s heart.*

*But why do you always lose, Dad?*

*Well. I made a bad move.*

*A bad move?*

*Not that kind of move. It means a bad play. It’s like when Taekyung played soccer at the sports festival yesterday and lost the game because he accidentally kicked Minjun’s leg instead of the ball. A bad choice. Do you understand?*

*Uh-huh, uh-huh. I understand. So if you make a bad move, you lose at Go?*

*Not necessarily.*

*Why?*

*The match doesn’t end just because you make one bad move. You lose because you keep making bad moves. Hmm. I shouldn’t have done that.*

*But I got sent off right away yesterday.*

*Son. Wasn’t that because Minjun’s leg was fractured?*

*Oh.*

*……What do you mean, “oh”? Your father nearly broke his back apologizing to Minjun’s parents. Anyway, the important thing is not to keep making bad moves.*

*What happens if you keep making bad moves?*

*In Go, you lose your precious stones and eventually lose the game. It’s the price you pay for making bad choices.*

*I know! That’s why you always lose, Dad!*

*……Honey! Take Taekyung away! Honey!*

I didn’t know why this memory had suddenly come back to me.

No. Maybe I did.

Because it had allowed me to make up my mind.

*Can you promise me just one thing?*

*Why are you suddenly quiet… Promise?*

*Yes. A promise.*

I stared straight at the Beast Miao King as I sent him another Sound Transmission.

*No matter what happens from this point on, promise me you’ll make sure the others can return safely to the Central Plains.*

*……!*

*That’s all I need.*

*You… Don’t tell me…*

*I’ll take that as a promise.*

The Beast Miao King had stared at me with widened eyes, as if he had guessed what I was planning. Then he nodded with a troubled expression.

*I promise. I will protect your subordinates with every bit of strength I possess. And I will also clear your name.*

*All right. That’s enough.*

I muttered inwardly and began walking toward Baeksang.

No.

I was about to walk toward him.

Grab!

If two hands had not reached out from behind me at that moment and seized the hem of my clothes, I would have.

“Jin Taekyung. What exactly are you planning to do?”

Yayul Mok asked the question with a rigid expression. Then Namho, who had already read my mind, added a single sentence.

“You foolish bastard. Are you planning to walk into a tiger’s mouth on your own?”

“I’m not sure whether it’s a tiger’s jaws or a fucking mutt’s.”

I shrugged and continued.

“But things have come to this. What else can I do?”

Namho’s gaze sank more deeply than ever as he looked at me.

“Is this because of me and the other members? Because you’re afraid we’ll be harmed if you flee from here?”

“Hmm. I don’t know.”

“If that is what you’re thinking, then throw it away at once. None of us wants—”

“I know. I know you all feel that way.”

I interrupted Namho gently and continued.

“But it would be the same if our positions were reversed. If the other members were in my place, or if Elder Namho were me right now, you wouldn’t run away alone either.”

“……!”

“See you later.”

Instead of answering, Namho’s eyes trembled.

I freed my clothes from their grip, met both of their eyes in farewell, and began walking.

Step. Step.

Silence had settled over the surroundings.

The sound of my footsteps as I moved alone seemed to thunder through the area, while Baeksang, watching me, remained as calm as an undisturbed lake.

“Have you finally come to your senses?”

“Someone told me a long time ago that if you make too many bad moves in Go, you lose your precious stones and have no choice but to lose.”

If this had been an actual Go match, I would have played however I pleased—to hell with bad moves.

Even if I lost, so what? A famous professional Go player had once said, “It’s still just Go—in the end, it’s only Go.” To me, it really would have been nothing more than Go.

After losing, I could simply smash Baeksang’s head open with the Go board while saying, just like my father had, “That Chink bastard plays Go like shit.”

But this was not a simple game, and when I made a bad move, I would lose my people instead of stones.

*Ju Hwaran. Hyuk Mujin. Song Ilseom. Sama Pyo. Taishan. Namho…*

Even if I escaped this place, breaking through the net over heaven and earth of the Nanman Beast Palace with all of them would be nearly impossible.

They had trusted me and followed me this far.

I had to keep them alive.

No matter what method I had to use.

“If you continue making bad moves, you lose your precious stones and suffer defeat… Whoever that person was, he was wise.”

“He was a good man. At least he wasn’t a piece of shit like you.”

Shing! Shing! Shing!

As if they had made an agreement beforehand, weapons were drawn from every direction.

At the same time, Baeksang glanced at the tightening encirclement and waved his sleeve.

“For once, I will commend you for not making a bad move. Even if you are the Fire King’s Disciple, you could not have done otherwise.”

“I’m not doing this to hear praise from a piece of shit like you.”

“It matters not. You will be confined in the underground prison.”

“An underground prison. That’s not exactly a pleasant thing to hear.”

“Several thousand pounds of iron balls will be prepared as well, so you may look forward to it.”

“Sure. My balls are already trembling from anticipation.”

It was more or less what I had expected.

I answered calmly, then continued speaking to Baeksang, who was slowly sheathing his sword.

“But why aren’t you looking forward to it?”

“What?”

“Didn’t you say so earlier? That if I ran away, you would kill every one of my people.”

“Why are you suddenly bringing that up—”

I had no reason to hear the rest of his words. Nor did I need to.

*If you said that kind of bullshit to me, you should have known you’d get punched.*

Along with a final word he could not hear, I thrust out a single fist like a ray of light.

Crack!

And without even checking the result, I hurriedly shouted,

“Ah, I surrender! I surrenderrr!”

What are you going to do about it, you fucker?
## Chapter artifact 659

# Chapter 659

Crack.

A large, fur-covered paw stepped on a brittle leaf.

Sharp fangs briefly showed between parted jaws. The sleek body crouched low among the grass had already finished preparing for the hunt.

*What kind of meat will I eat today?*

Once it spotted a noticeable target, all it had to do was sprint over and sink its fangs into the prey’s neck.

As long as it avoided venomous beasts that appeared without warning, finding prey in Nanman was not particularly difficult.

At least, that was true for the black leopard, which occupied the upper levels of the brutal food chain.

Grrrr…

The black leopard scanned its surroundings with bright yellow eyes before suddenly letting out a low growl.

It had sensed countless presences in the distance and caught a scent carried on the wind.

Sniff, sniff.

Like any predator, the black leopard possessed keen senses. It did not take long to identify the prey that had wandered into its territory earlier than expected.

Humans.

More accurately, it was a group of humans. Roughly a hundred of them were approaching this place.

Grrr.

The black leopard unconsciously let out an irritated growl.

Humans were not particularly welcome creatures in the black leopard’s eyes.

Despite their small bodies, they sometimes hunted predators much larger than themselves. And the more numerous they were, the greater their strength became.

Just like now.

Swish.

The black leopard rose from its crouch.

Only fools hunted humans alone. At times like this, it was much smarter to change locations and search for other prey.

The black leopard reached that conclusion and was just about to move when—

“Whew. Whew…”

The black leopard stopped and stared beyond the grass.

One human came running up, making a strange noise, then squatted down among the weeds.

“Ahh. I almost died.”

At the same time, sounds and smells that would have made even predators recoil filled the air. A glint flashed through the black leopard’s vertically slit pupils.

There was no doubt. That human had separated from the group to relieve himself.

Without realizing that this place would become his grave.

Grrr.

One target. And, what was more, a human who looked stupid.

The black leopard’s judgment and movements were swift. The muscles connecting its four legs contracted to their limit, and a moment later, its black body shot forward like an arrow.

Tap—whoosh!

Several dozen feet vanished in an instant. Only then did the human notice something and turn his head toward the leopard.

But his reaction was a beat too slow, and the sharp fangs inside the black leopard’s wide-open jaws flashed.

—Raaaar!

Thud! Crunch!

The sound of flesh being torn rang out beneath the beast’s thunderous roar. Large and small bodies tangled together and rolled across the ground.

Then, a short while later, the survivor of that brief but fierce battle announced that he was still alive.

“Phew!”

The face of the man emerging from among the black fur was drenched in blood.

The black leopard’s blood.

At the final moment, the man had driven his sword into the head of the predator that ruled this area. Now he was breathing heavily.

“Huff. Hah. Fuck. I almost died while taking a dump.”

Being ambushed while relieving himself. Even thinking about it again, it had been incredibly close.

If this had been him one or two years ago, he would have helplessly become the black leopard’s meal.

But just as a seed sprouted, the man had also grown tremendously compared to the past.

“I’ve been beaten so much that my reflexes have improved… But how am I supposed to get out of here?”

The man—Hyuk Mujin—was still trapped beneath the impossibly heavy carcass of the black leopard, struggling and grunting, when—

“That is strange. Was this the errand you said you were stepping away to take care of?”

At the familiar voice that pierced his ears, Hyuk Mujin’s face brightened.

“Oh! Great Hero Song!”

Song Ilseom, the owner of the voice, sighed.

“I told you not to call me Great Hero.”

“Why not? If you help someone in trouble, doesn’t that make you a Great Hero?”

“Perhaps you resemble your superior. Your words certainly flow like a mountain stream.”

“That’s a compliment, so I appreciate it. But please don’t say things like that in front of Captain. Even you, Great Hero Song, might get beaten into a babbling stream.”

Song Ilseom nodded at the advice that came straight from Hyuk Mujin’s soul.

“…I’ll keep that in mind.”

“Good thinking. But could you move this thing for me? I’m starting to feel like I’m about to stop breathing. I keep seeing my father’s face.”

“Really? When did he pass away?”

“What are you talking about? He’s still alive and well.”

“…?”

*Is this man insane?*

Song Ilseom seriously considered the question for a moment before giving up and grabbing the black leopard’s corpse.

There were few sane people in the Fire Dragon Pavilion he had somehow ended up joining.

Of course, the Pavilion Master was the craziest of them all.

Swish. Thud.

Hyuk Mujin barely escaped the threat of being crushed to death. He brushed the dirt from his clothes and asked,

“Whew, I almost died. Where are the others?”

“They’re preparing camp. The Young Bureau Head is there as well. We’ve already been running for nearly ten shichen without rest, so she seems to have decided we need a break. A missive arrived just as you stepped away.”

“A missive?”

“Yes. It seems the Nanman Beast Palace sent a messenger eagle. They must have had additional instructions for us.”

“Either way, that’s good news. The beasts have been moving so violently that I nearly shattered my rear end.”

“They need to rest too. Still, the Nanman people must train them well. Their stamina is impressive. They’re no worse than grassland horses.”

About a day earlier, they had left the Outer Palace with the reconnaissance squad and continued their forced march.

Since they had no idea when the unidentified old monster known as the Blood Monk might cross through Guangxi and head south, it was the obvious choice.

“When do they say we’ll arrive?”

“According to the two tribal chieftains, the earliest would be two days. At the latest, we should arrive within three. The Young Bureau Head seems to think the same.”

“It sounds like we absolutely have to get there within two days. Is that just me?”

“You heard correctly. To stop the Blood Monk, we need to move as quickly as possible.”

“Like this?”

“Perhaps even faster.”

“…Anything faster than this is a bit much.”

Hyuk Mujin made a displeased face, then nodded.

“Damn. It can’t be helped.”

“You give up quickly.”

“Follow Captain around for about two years, Great Hero Song. After that, you’ll give up on everything. Your life included.”

“Unfortunately, that won’t happen.”

“Why not?”

“If it weren’t for the Young Bureau Head, I wouldn’t have come this far. That is the sole reason I’m in this wretched Nanman.”

At that sharp reply, Hyuk Mujin shrugged.

“Hmm. Then I guess we’ll be seeing you often.”

“What?”

“You just said it yourself. The reason you followed us this far was Young Lady Ju. And Young Lady Ju will be with Captain from now on too, won’t she?”

“……!”

“Great Hero Song, you seem dumber than I expected.”

Song Ilseom stood frozen for a moment before asking in a calm voice,

“Do you want to die?”

“No. I’m sorry.”

Hyuk Mujin answered promptly, then cautiously watched Song Ilseom as he pulled the sword from the black leopard’s head.

Fwoosh.

Blood spurted from the gaping wound. Hyuk Mujin roughly wiped the blade clean, sheathed it, and suddenly raised his head to look at the sky.

“It’s already night.”

They had apparently set out at night, but while moving without a moment to think, the second night had already arrived.

And several more nights would have to pass before they could return to the Nanman Beast Palace.

“Still, I’d rather not meet the Blood Monk if possible. I’m uneasy without Captain here. You feel the same way, right, Great Hero Song?”

But no answer came.

And shortly afterward, following a brief silence, the sound that reached his ears was not Song Ilseom’s voice but the cold scrape of a blade.

Shing.

Hyuk Mujin recognized the sound coming from behind him and swallowed dryly.

“Uh, about that. I’m sorry for saying you were dumb. Are you very angry?”

A voice, cold as ice, came from behind him.

“…Shut up and turn around.”

“Great Hero Song. Please. I’m begging you.”

“I’m begging you too. Shut up and turn around. Draw your sword again.”

*This guy’s really lost his mind.*

With tears in his eyes, Hyuk Mujin turned around on trembling legs.

And in that moment, he realized why Song Ilseom’s voice had been so cold. He understood why Song Ilseom had told him to draw his sword.

“I was sure they were allies… Was I mistaken?”

Rustle, rustle.

The grass, cloaked in darkness, shook.

The hundred-strong reconnaissance squad had traveled with them until now. At its head, the two tribal chieftains emerged and stared at them with grim expressions.

“It wasn’t just your mistake. But I regret that things have come to this.”

“We received a missive. It bears the Palace’s seal. It is an order we cannot refuse.”

A missive.

The moment Song Ilseom heard those two words, he had a vague intuition that something serious had happened in the Inner Palace they had left behind.

But more important than anything else was the existence of a single person.

“Where is the Young Bureau Head?”

Killing intent seeped into his voice.

Chief Jang, who belonged to the pro-Palace Lord faction and had favored Jin Taekyung since the Tribal Grand Council, sighed as he answered,

“Her sword was fiercer than I expected. She was quick to catch on, too.”

“I’ll ask one last time. Where is she?”

Whoosh!

Fierce killing intent overflowed from Song Ilseom’s entire body. His brutal aura was so vicious that even the beasts among the reconnaissance squad took several steps back.

Another tribal chieftain, sensing his fury, hurriedly opened his mouth.

“Sh-she’s safe. We only subdued her with a Pressure-Point Strike.”

Song Ilseom clenched his teeth before he even realized it. Relief and regret surged through him at the same time.

*I should have stayed by her side, no matter what.*

Considering the size of the reconnaissance squad that had turned from allies into enemies, the result probably would not have changed much even if Song Ilseom had remained behind.

But… he could not stop picturing Ju Hwaran fighting alone.

“…Damn it.”

As he spat out the curse, Song Ilseom slowly lowered the cherished weapon in his hand.

Hyuk Mujin, who had realized what was happening slightly later, did the same.

Swish. Thud.

The carefully forged blade pierced the ground.

Chief Jang watched the scene with a troubled gaze, then gestured. Warriors from the reconnaissance squad obeyed his command, rushing over to retrieve the weapons and bind the two men.

“…Great Hero Song. I think we’re seriously fucked.”

Song Ilseom did not answer Hyuk Mujin’s mutter this time either.

No, he could not answer.

Tap, tap, tap.

Someone’s fingers tapped all over his body. As he felt his body stiffen under the Pressure-Point Strike, Song Ilseom muttered inwardly,

*What on earth have you done, Jin Taekyung?*

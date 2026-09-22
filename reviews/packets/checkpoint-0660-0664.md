# Checkpoint Review — 660–664

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

# Chapters 660–664

## Plot

Chief Jang and Chief Go secretly follow the Beast Miao King’s order to keep the three Han Chinese reconnaissance-squad captives away from the Inner Palace, protecting them from being used as hostages. Jin Taekyung is imprisoned in the deepest part of the Nanman Beast Palace’s underground prison, bound with enormous iron balls and incapacitated by a Force-Sealing Pill. Baeksang announces that twenty tribal chieftains have united to place Jin’s execution before the Tribal Grand Council, scheduled for noon in two days.

Baeksang recounts the Great Snow Mountain battle, where Nanman warriors under his and the Beast Miao King’s command fought alongside the Zhongnan Sect against the Demonic Cult. He claims that allied forces deliberately withheld aid, killed the messenger, pursued retreating enemies for military credit, and erased the evidence. Baekhwi, Baeksang’s only child, and Venerable Wusang were later killed by the Great Snow Fiend. Baeksang attacks Jin, blaming the Central Plains and Han Chinese for his decades of grief and revenge.

Jin acknowledges Baeksang’s original anger but condemns his alliance with Dark Heaven and the innocent Nanman deaths it has caused. He compares Baeksang’s revenge to the Head Elder’s destructive path and demands that he stop spilling blood. Baeksang leaves certain of Jin’s execution but begins to waver after remembering his dead child. Jin remains determined to escape rather than submit.

A damaged ceiling connects Jin’s cell with Taishan’s cell above. Taishan reports that Namho and Sama Pyo are detained separately and safe, while Ju Hwaran, Song Ilseom, and Hyuk Mujin are held elsewhere. The System generates the linked Quest **Escape from Namshank**. Meanwhile, Sudal leads three swift ships toward Guizhou, where they find a crewless Yangtze River Channel League ship occupied by the Blood Monk. The Blood Monk asks whether the ship travels to Nanman.

## Continuity

- Jin Taekyung remains imprisoned in the Nanman Beast Palace’s underground prison, bound by iron balls and unable to use internal energy because of the Force-Sealing Pill.
- Jin’s public execution is scheduled for noon in two days, but he intends to escape and stop Baeksang.
- Baeksang has secured the support of twenty tribal chieftains and is using Jin’s execution as the final-day agenda of the Tribal Grand Council.
- Baeksang’s only child, Baekhwi, was killed during the Great Snow Mountain battle; Baeksang blames the Zhongnan Sect and other Central Plains allies for abandoning Nanman forces.
- Baeksang claims the Great Snow Fiend killed both Baekhwi and Venerable Wusang.
- Baeksang has allied with Dark Heaven, and Jin connects that alliance to the Miao village massacre, the Thousand-Year Spiders’ escape from the Poisonblood Grounds, and the Western Yao Estate incident.
- Chief Jang and Chief Go are secretly protecting the three Han Chinese reconnaissance-squad captives from being taken to the Inner Palace.
- Ju Hwaran, Song Ilseom, and Hyuk Mujin remain captured and are being held separately from Jin’s companions; Song Ilseom and Hyuk Mujin were previously bound and unconscious.
- Namho and Sama Pyo are detained separately and are reportedly safe.
- Taishan is imprisoned in the cell above Jin and can communicate through the broken ceiling. He was confined after breaking both wrists of a Nanman attendant who underfed him.
- The System has generated the linked Quest **Escape from Namshank**.
- Sudal is leading three swift ships toward Guizhou and has encountered the Blood Monk aboard a crewless Yangtze River Channel League ship.
- The Blood Monk has asked whether the ship travels to Nanman.
- It remains unresolved whether the Blood Monk serves the Southern Heaven Demon Empress, whether he will attack Sudal’s ships, and whether he will threaten the reconnaissance squad.

## Translation Decisions

- Use **Tribal Grand Council**, **Southern Army**, **Western Army**, **Great Snow Mountain**, **Great Snow Fiend**, and **Venerable Wusang**.
- Retain **Force-Sealing Pill**, **Force**, **Supreme Peak**, **Dark Heaven**, **Demonic Cult**, **Inner Palace**, **Outer Palace**, **underground prison**, and **iron balls**.
- Use **Escape from Namshank** for 남생크, preserving the Shawshank pun.
- Use **Chief Jang**, **Chief Go**, **Deputy Stronghold Lord**, and **Stronghold Lord**.
- Use **Yangtze River Channel League** and **swift ships**.
- Retain **Baekhwi**, **Taishan**, **Namho**, **Sama Pyo**, **Sudal**, and **Blood Monk**.

## Durable state

{
  "active_continuity": [
    "Jin Taekyung remains imprisoned in the Nanman Beast Palace's underground prison with sealed internal energy and iron balls, and his execution is scheduled for noon in two days.",
    "Jin intends to escape before execution and ultimately stop Baeksang.",
    "Taishan is imprisoned in the cell above Jin and can communicate through a broken ceiling; he was confined after breaking both wrists of a Nanman attendant who underfed him.",
    "Namho and Sama Pyo are detained separately and are reportedly safe according to Yayul Mok's information.",
    "Ju Hwaran, Song Ilseom, and Hyuk Mujin have been captured but are being held elsewhere, which is currently considered safer.",
    "Jin suspects the Blood Monk may be a subordinate of the Southern Heaven Demon Empress and may endanger the reconnaissance squad.",
    "The System generated the linked Quest Escape from Namshank.",
    "Sudal is leading three swift ships toward Guizhou and has encountered the Blood Monk aboard a crewless Yangtze River Channel League ship.",
    "The Blood Monk has asked whether the ship travels to Nanman."
  ],
  "continuity_sources": [
    664,
    663
  ],
  "open_questions": [
    "Is the Blood Monk truly a subordinate of the Southern Heaven Demon Empress?",
    "Will the Blood Monk attack Sudal's ships or use the captured ship to travel to Nanman?",
    "How will Jin escape the underground prison before his execution?",
    "Will the captured reconnaissance members encounter the Blood Monk?",
    "Will Baeksang's wavering alter the planned execution or his alliance with Dark Heaven?"
  ],
  "safe_through": 664,
  "temporary_decisions": [
    "Use Escape from Namshank for 남생크.",
    "Use Deputy Stronghold Lord for 부채주 and Stronghold Lord for 채주.",
    "Retain underground prison for 뇌옥."
  ],
  "version": 1
}

## Reading copies

## Chapter artifact 660

# Chapter 660

“We’ve subdued them all. I struck their Sleep Acupoints as well, so they won’t regain consciousness for at least a day.”

“…Good work.”

Chief Jang nodded with a troubled expression as he listened to his warrior’s report.

Song Ilseom and Hyuk Mujin lay motionless, and their figures were reflected in his eyes.

“We don’t know what might happen, so keep a close watch on them. We’ll move again after resting for two shichen.”

“Does that mean…?”

“Yes. We’ll be traveling with them.”

“Chief… Forgive me for speaking out of turn, but wouldn’t it be better to select a few warriors and escort the prisoners to the Inner Palace separately?”

The warrior who had gathered up the courage to ask immediately regretted it. Chief Jang was staring at him without saying a word.

“I’ll carry out your orders.”

After answering hurriedly, the warrior turned and left.

Chief Jang watched him go, then suddenly let out a sigh. The contents of the letter delivered by messenger eagle had come back to him once more.

*Heugung and Yohi, two great chieftains, have gone missing, and the Western Yao Estate has been wiped out. And now they’re saying Jin Taekyung was responsible?*

He had reread it several times because he could not believe what he was seeing.

But the writing in the missive did not change, and Chief Jang had been left with only one choice.

*I’m sorry, everyone.*

Chief Jang repeated the apology silently, knowing it would never reach them. But they would understand soon enough. They would come to know that, under the circumstances, this had been the best course of action.

*This was a thoroughly prepared plot. He was merely caught up in it unexpectedly.*

Chief Jang did not believe the contents of the missive.

Everything Jin Taekyung had shown until now resembled what the Han Chinese of the Central Plains called a Great Hero. If he had not risked his life fighting in the Poisonblood Grounds, more than two hundred warriors would never have returned to their families.

Among those who had made it back alive were the warriors of the Zang people under Chief Jang’s command—and his own blood relatives.

*And regardless of the debt I owe him, there isn’t even a proper justification for this.*

Although Nanman and the Central Plains had fallen out after the Great Faction War, it was closer to one-sided hostility born from the immense sacrifices of that conflict.

So what possible reason could Jin Taekyung, who had been sent to Nanman as the representative of the Murim Alliance, have had for causing such a tragedy?

*Unless he intends to turn Nanman against him as well, on top of Dark Heaven…*

But there was nothing he could do. The course of this incident had already fallen into Baeksang’s hands and those who followed him.

However, the Palace Lord, the Beast Miao King, had secretly conveyed his intentions through a messenger eagle.



> Hold the Han Chinese within the reconnaissance squad, but do not escort them to the Inner Palace.



Chief Jang understood exactly what the Beast Miao King meant.

*If we escort them to the Inner Palace, they’ll undoubtedly become hostages.*

Fortunately, Chief Go, who was leading the reconnaissance squad alongside him, also followed the Beast Miao King. Since the two men shared the same opinion, they had their warriors subdue the three of them.

Not as hostages, but so they could keep them in their hands and protect them somehow.

The circumstances had also worked in their favor. They were already traveling to keep watch for an old monster known as the Blood Monk.

Since it was effectively a wartime situation, even if Baeksang’s faction learned about this, there was nothing they could use against them.

*So please bear with it for a little while. At least until everything is resolved.*

Chief Jang muttered inwardly and stepped toward the two men who were being carried away by the warriors, unconscious.

He intended to loosen their bindings a little, as an apology.

“Stop for a moment. Aren’t those ropes tied too tightly?”

“Chief! You can’t!”

“What do you mean, I can’t? It’s fine—”

Squelch.

Ignoring the warriors’ cries, Chief Jang reached behind Hyuk Mujin’s back, then suddenly frowned.

*What is this?*

A damp, sticky sensation.

Then came a foul stench, followed by a warrior’s voice.

“Uh. There was… feces on his back.”

“…!”

“That’s why we told you not to come any closer…”

The warrior’s voice trailed off. Chief Jang silently looked back and forth between his hand and Hyuk Mujin, then spoke in a low voice.

“The prisoner might shit more—no, escape. Tighten the ropes.”

“Yes, Chief.”

* * *

In the modern world, I had been a model citizen with a strong sense of civic duty.

Until middle school, whenever the traffic light turned green, I would raise my hand high and cross the street. After becoming a Hunter, I paid all my insurance premiums and taxes on time, without ever delaying a payment or evading a cent.

I did not even complain much about the national pension, despite how little I would receive by the time I grew old.

*In short, prison and I had never had anything to do with each other.*

And yet, why was it that in the Murim, I had grown increasingly familiar with a place called an underground prison despite never committing a crime?

It had been the same at the Jin Family of Taiyuan when I was still an aspiring martial artist. At the Sichuan Tang Clan, I had even spent several days there to stand guard beside Jeok Cheongang.

This was my third visit to an underground prison, but it was quite different from the previous two.

*At the Jin Family of Taiyuan, it was practically a training hall rather than a prison. At the Sichuan Tang Clan, I was there to care for Jeok Cheongang.*

This time was different.

Not only was I imprisoned against my will, but anyone would have thought as I did if iron balls weighing more than a thousand geun each were hanging all over their body like accessories.

Clank.

“…Fuck, this is heavy.”

I muttered a curse. The enormous chains binding my limbs and the iron balls attached to them were unbelievably heavy.

Even I, who possessed Strength far beyond human limits, could barely move.

*If I could only use my internal energy, I might be able to think of some way out of this…*

Maybe I shouldn’t have punched him at the end.

I felt a pang of regret, but if Baeksang had been that easy to deal with, I would have been in my quarters instead of an underground prison by now.

Besides, even after taking a punch to the face hard enough to break his nose, Baeksang had personally bound me as I stood there without so much as batting an eye or resisting, then issued this order to the tribal chieftains under his command:



*“Lock the Han Chinese Jin Taekyung in the underground prison and bind him with ten thousand geun of weight.”*



And this was the result.

I had been thrown into the deepest part of the Nanman Beast Palace’s underground prison, then given a special pill that left me unable to use my internal energy for several days.

*At least I should be grateful they didn’t use a Pressure-Point Strike on me.*

The reason they had been unable to strike my acupoints was simple.

They kept coming undone.

My perfect body, which had been recognized as a Heavenly Martial Physique by countless powerful masters, had simply performed its function to the fullest.

Of course, that did not mean my attempts to raise my internal energy had succeeded.

“Ungh.”

I poured all my strength into my body, then took a deep breath and focused my mind on my lower dantian, just as I had done hundreds and thousands of times before.

The next moment, the System alert I had been forced to hear repeatedly for the past half a day pierced my ears again.

Beep.



> **System**
>
> - The energy of the **Force-Sealing Pill** is blocking your dantian!
> - You cannot use **internal energy**!



“Ah.”

I had lost track of how many times I had failed.

After passing fifty attempts, I had given up counting.

“…Damn it.”

Just as I let my body sag with a curse mixed into my sigh, someone’s footsteps began approaching from far away.

Step. Step.

The sound echoed through the damp, dark space.

The Force-Sealing Pill kept me from using my internal energy for the moment, but my physical senses remained as sharp as ever.

I raised my head and looked toward the murky darkness beyond the bars.

Splash.

The footsteps stopped in front of the iron bars. At the same time, the filthy water pooled on the floor splashed against my knees.

There was not a single light in the darkness, but my eyesight—good enough to rival a Mongolian’s—was more than sufficient to identify the other person.

“What is it? Are you a new jailer?”

“…”

“You’ve got no basic manners. You splash dirty water on someone the moment you arrive, then don’t even answer when spoken to.”

The unwelcome visitor looking down at me in silence, Baeksang, replied in a low voice.

“For a criminal, you complain quite a lot.”

“Well, this much is practically cute.”

I tried to shrug, then flinched at the weight of the iron balls before continuing.

“Somebody’s nose bone collapsed, and he still held out pretty well. Wouldn’t you say?”

I could see Baeksang’s brow furrow in the darkness. The bandage wrapped around his straight, prominent nose was visible as well.

“That must have hurt quite a bit. You took it better than I expected. Honestly, you shed a single tear after sending me to prison, didn’t you?”

But his agitation lasted only a moment. Baeksang’s calm voice returned.

“It tickled. Perhaps because I sensed fear in your punch.”

“What?”

“It contained no internal energy, and it was not a full-force blow. It was nothing more than a child’s fit of frustration.”

“…”

“I understand. You must have been afraid. If you had given it everything you had, neither you nor your subordinates would have remained unharmed.”

*Damn. I got absolutely screwed in that exchange.*

His one sentence had struck the exact center of the target. I had been about to say something in reply, but I closed my mouth.

Baeksang’s eyes remained as calm and unwavering as ever as he watched me.

“Why didn’t you leave that place? If you had fled alone, you might have survived.”

I answered with an incredulous expression.

“You said you’d cast a net over heaven and earth, you bastard.”

“Of course, I would have done so. But there was still a sufficient possibility. At the very least, the Palace Lord would not have pursued you. No—he might even have interfered.”

Baeksang’s guess was not baseless.

Judging from everything I had seen and experienced of the Beast Miao King, and from what I had heard directly from Jeok Cheongang, he was more than capable of doing exactly that.

He was the kind of person who would throw out a lifeline at least once in the worst possible situation.

But I did not foolishly nod along.

It might already have been too late, but if I readily admitted that fact in front of Baeksang, his wariness toward the Beast Miao King would only grow stronger.

“I don’t know. I didn’t get that impression. We aren’t even particularly close.”

“You’re putting that head of yours to work. But you’re still far too green.”

“Whether you believe me or not is up to you. Be grateful Old Master isn’t here right now. In two or three months, your head will be rolling around here.”

“You really are still a child who hasn’t outgrown his impetuousness.”

I let out a short laugh.

“Your mouth reeks of shit. Stop sucking Dark Heaven’s asshole. At least I’m here to protect my people.”

“…”

“No one else is around, so let’s be honest. You know too, don’t you? You know what you’re doing right now.”

This time, Baeksang was the one who fell silent.

Of course, he had no choice. Cooperating with Dark Heaven meant taking all of Nanman and offering it up to the Lord of Heaven.

“You betrayed even your sworn brother of several decades. You deceived more than thirty tribal chieftains and countless Nanman people. No matter what excuse you make, none of this can be justified.”

At that moment, Baeksang, who had been watching me with a deep, unreadable gaze, suddenly spoke.

“Two days.”

“What?”

“Two days. At noon, two days from now. You will be executed in front of everyone.”
## Chapter artifact 661

# Chapter 661

Two days later, at noon.

And then, execution.

The two short words that slipped between Baeksang’s lips shot through my mind like bullets.

*Execution in two days? Me?*

I swallowed the question rising up my throat. At least here—not in front of Baeksang—I couldn’t afford to show him that he had shaken me.

Rather than despair, I once again knocked on the escape route that had already been blocked several times.

*Logout.*

Beep!



> **System**
>
> - **Logout** failed!
>
> - **Logout** is unavailable in certain situations!

*I’m fucked. Still not working.*

I forced myself to speak in a calm voice.

“Two days. That’s sooner than I expected.”

“My late father always used to say this: once you have made up your mind, draw your sword without hesitation.”

“You’re not drawing that sword alone, are you?”

“I may be the first to take hold of the hilt, but when the sword swings for your neck, I will not be alone. Not even the Palace Lord can stop it.”

*I will not be alone when I swing it.*

I quietly mulled over the meaning of those words, then muttered as if speaking to myself.

“You must have been awfully busy running around. Judging by how many places you’ve reached out to in the meantime.”

Baeksang answered in his dry voice.

“Twenty tribal chieftains, including myself, have already joined forces. And the matter on the agenda for the final day of the Tribal Grand Council will be…”

“Jin Taekyung of the Jin Family of Taiyuan. No—my execution, now that I’ve become a criminal guilty of a crime that outrages heaven and humanity.”

“You understand quickly.”

“I’d have to be a fucking idiot not to, with things already this far along. Anyway, is that why you threw me into the underground prison first?”

“Of course. It was the easiest way. I didn’t expect you to surrender so readily, though.”

Baeksang did not deny it. Like a hunter looking down at captured prey, he gazed at me, bound by iron balls weighing nearly ten thousand geun, and continued in a low voice.

“To catch a tiger, you have to venture into the mountains and take the risk. But a tiger locked inside a cage is a different matter, wouldn’t you say?”

“I suppose it is. Especially when the hunter isn’t alone, and there are twenty of them.”

The number of tribal chieftains following Baeksang had never been small. But twenty?

That was more than half of the thirty chieftains remaining after Heugung and Yohi disappeared. It meant that some of the chieftains who had stood on the Beast Miao King’s side had switched allegiances.

“What exactly did you promise them?”

“Revival for their tribes. Greater influence and enormous wealth.”

“Well, that’s something. I expected as much, but it’s damn simple.”

“But more than anything, it is effective.”

Perhaps because he was certain we were truly alone.

Baeksang’s answers today were more honest than ever. At the same time, they consisted of facts I could not deny.

Unfortunately, he was right. The Nanman Beast Palace was, after all, an alliance of tribes, and the tribal chieftains—each of whom had assessed the situation in his own way—had bet on the side with the greatest chance of victory.

For the future of the tribes they ruled.

For the riches and glory they would gain.

And…

“Among them, the person who will receive the greatest reward is standing right in front of me. You’ll take all of Nanman for yourself. Isn’t that right?”

Baeksang said nothing in response. I let out a hollow laugh.

“Interesting. It’s rotten right down to the roots.”

That was when Baeksang, who had been staring at me as if he could see straight through my heart, suddenly spoke.

“Have you ever experienced a war?”

“What?”

“I asked whether you have ever experienced a war.”

Why had he suddenly started talking about this?

But whether I understood Baeksang’s intentions or not, I had little choice but to listen. I was a tiger trapped inside a cage, after all.

“I experienced all of it firsthand. More than fifty years ago, when I arrived in the Central Plains with the Palace Lord and ten thousand warriors, the first thing I saw was hell brought into the human world.”

Baeksang continued slowly and calmly.

“Farmlands were trampled, and blue rivers were choked with blood and corpses. Every day—or sometimes every moment—people died all across the land. Children who had lost their parents to the war and been consumed by hunger tore at tree bark and ate it without even realizing that their own teeth were being torn out.”

War was always horrific. Even if someone ultimately emerged victorious, the process was built upon countless screams and deaths.

It was the one path neither victor nor loser could avoid.

“It was a hellscape unlike anything I—or even the Palace Lord—had ever seen before. But we had a reason to fight, so none of us retreated. If the Demonic Cult took control of the Central Plains, Nanman would be next. We were there to protect the homeland where my family and friends lived.”

Baeksang’s voice echoed through the dark underground prison.

“An uncountable number of lives disappeared. Some died fighting the enemy on the battlefield. Others stared blankly at the sky after the fighting ended, then took their own lives. At times, we even had to strike the lethal acupoints of comrades writhing in pain.”

“…”

“Someone died in one battle after another, while others grew exhausted. But as the tide of war gradually turned in our favor, the hope held in a corner of our hearts only grew stronger. Soon, we would be able to return home. Soon, we would see the women we loved and our aging parents. Or the children who had grown so much in our absence.”

I had never experienced it, yet I could feel it.

I had never seen it, yet it appeared before my eyes.

Their figures as they crossed the jungles, passed over the Yangtze, and crossed plains and mountains before finally arriving in the distant Central Plains. The battlefield where they fought the Demonic Cult’s hundred thousand practitioners of the Demonic Path, who came rushing from every direction day after day.

“When I stopped to count, fewer than one-tenth of the ten thousand warriors were still alive. Even the tide of battle, which had been slowly turning in our favor, eventually fell into a stalemate. The Palace Lord and I began to wonder why we had to remain there.”

Time was a law no one could oppose. Before that absolute law, which could move mountains and dry up rivers, even a master who had reached the Supreme Peak realm could do nothing.

*Their hearts must have been worn away. Slowly. Until they could no longer endure any more.*

Just as I muttered that inwardly, Baeksang’s voice continued.

“More than a decade had passed when, one day, the Martial God defeated the Heavenly Demon.”

The clash between two absolute beings.

The result of that life-and-death duel that shook heaven and earth was the Martial God’s victory. Once the Demonic Cult—which had devoured half the world—lost its central figure, the Heavenly Demon, it collapsed like a sandcastle.

“The remnants of the Demonic Cult retreated west, and the Murim Alliance sought to pursue and annihilate them to the very end. Led by the Martial God, whom no one could stop anymore, the Three Saints and the Ten Kings advanced from every direction, along with countless orthodox martial artists belonging to the Murim Alliance. We were no exception.”

The scales, which had already been gradually tipping toward the orthodox factions, lost all meaning with the Heavenly Demon’s death.

All that remained was to pursue the hundred thousand practitioners of the Demonic Path, now reduced to defeated soldiers, annihilate them, and uproot them from the Central Plains.

“The war was as good as over. No—it should have been.”

Baeksang suddenly stopped speaking and stared blankly at some point in the air.

A drop of water leaked through a tiny crack in the ceiling and fell onto the cold floor.

Drip. Drip-drip.

A heavy silence settled over the underground prison.

I quietly watched Baeksang, who did not open his mouth even after I waited for him to continue. Then, all at once, I spoke.

“Baekhwi. That was his name, wasn’t it?”

“……!”

Baeksang’s body went rigid, and his eyes began to tremble. Seeing him more shaken than ever before, I gave a small nod.

“So I got it right. I wondered if I had mixed up the name.”

Crunch.

Something broke between Baeksang’s tightly closed lips. He opened his mouth, his eyes cold and sunken.

“Who told you that name?”

Yayul Mok was the one who had told me, but there was no reason to reveal that.

I answered calmly.

“Does that really matter? What matters is that there’s still someone who remembers the name Baekhwi.”

“Someone like you has no right to speak that name.”

Whoosh!

Killing intent as sharp as a blade erupted from Baeksang’s entire body and shot through the gaps between the iron bars.

But why?

Strangely, I wasn’t afraid.

Perhaps it was a thread of compassion for a father who had lost his young child long ago.

At least, that was how I felt in this moment.

*Baekhwi.*

*Baek, white. Hwi, shining.*

It was one person’s name. The name of Baeksang’s only child, whom he had cherished terribly—the name of someone who, had he lived, would have become the Beast Miao King’s son-in-law.

*If he had lived.*

I muttered the words inwardly, then ignored the killing intent pouring from Baeksang and asked,

“Did he lose his life while pursuing the Demonic Cult? Or…”

Boom! Rumble!

The roar swallowed the words that were about to follow.

At the same time, the underground prison shook violently beneath an immense shock wave.

Baeksang had pulverized part of the prison wall with a single punch. He stared at me with eyes cold as frost.

“Do you want to die here and now?”

Considering my current situation, it was a fairly threatening statement. If Hyuk Mujin had been in my place, he probably would have pissed himself and begun practicing silent meditation.

But there were exceptions to everything.

There was also Cheongpung, who might even have been a little excited at the thought of dying because it would be his first time…

And then there was me, whose liver had probably enlarged from being knocked around everywhere.

“That wouldn’t be so bad. Though you can’t kill me right now anyway.”

“What did you say?”

“There must be a reason you put off my execution for two days. Of course, that wasn’t a decision you made alone, either. Was it an order from the Southern Heaven Demon Empress? I heard you exchange missives on the first day of every month.”

“……!”

“So stop posturing and tell me the story. Being locked alone in an underground prison gets lonely and boring. The Sichuan Tang Clan at least had other prisoners, so it wasn’t so bad.”

“You bastard!”

His roar rang out like thunder, echoing through the prison.

Baeksang’s body trembled with rage as he reached out and gripped the iron bars.

Groan!

The steel, as thick as an adult’s forearm, bent like taffy. Baeksang stepped through the opening, and his eyes shone with a chill that stung my skin.

“Hwi. Is the death of that child so amusing and intriguing to you?”

His aura was so vicious that it seemed he might draw his sword and cut me down at any moment.

But I did not care.

He could not kill me here and now, if only because he feared the Southern Heaven Demon Empress. And there was something I needed to know.

“I don’t know if amusing is the right word. But there is one thing I’m curious about.”

“You really are…”

“Tell me.”

I cut him off in a flat voice, then continued slowly.

“Not how your only child died. What I want to know is what kind of lunatics turned a lunatic like you into what you are.”

“……!”

“Tell me that.”

After a heavy silence in which every second felt like fifteen minutes, Baeksang’s lips finally parted.

“Gansu. Great Snow Mountain.”

Haa…

His breath trembled. White vapor spilled from his mouth in the ice-cold underground prison, like the heavy snow that must have fallen that day.

“At that time, we were leading the Southern Army alongside the Zhongnan Sect.”

At the single sentence that pierced my ears, I instinctively swallowed the words trying to burst from my mouth.

*Oh, fuck. The Zhongnan Sect.*
## Chapter artifact 662

# Chapter 662

Was it about ten years ago? Back when I was still devouring martial-arts novels, I would occasionally find myself thinking about something.

No—maybe I thought about it fairly often.

*What would I do if I were the protagonist of this novel?*

Looking back, it was a little embarrassing, but I couldn’t help it. For anyone who had read web novels, that was practically a standard feature.

It happened whenever some idiot protagonist used a System window without raising his Intelligence. Or whenever a female character appeared and he made a complete fool of himself.

*If it were me…*

That was how the fantasies always began.

But after actually becoming a martial artist in the Murim, I learned that fantasies were fantasies, and reality was reality.

The many masterpieces of martial fiction I had read were nothing more than brilliantly arranged letters on a page, and the protagonists I had thought were so cool did not exist in this world.



*Old Master.*

*What.*

*There’s something I’m curious about regarding the Heavenly Demon. By any chance, isn’t his surname Muk?*

*…What the hell are you talking about all of a sudden? Not long ago, you were spouting off about things like the Wudang Demon Sword and the Huashan Gale Sword—titles I’ve never heard of in my life.*



At first, I was sorry I’d never get to meet the protagonists from those novels, but I wasn’t disappointed. The martial artists of this world were every bit as cool as those characters.

However, if there was one thing that had thoroughly shattered my fantasies, it was…

“We were leading the Southern Army alongside the Zhongnan Sect at the time.”

That was right. Those three words that had just slipped from Baeksang’s mouth.

*The Zhongnan Sect.*

A towering pillar of the orthodox Murim, one of the Nine Sects and One Gang. A prestigious great sect that had carried on its legacy for hundreds of years and divided Shaanxi Province between itself and its eternal rival, Huashan.

No—by now, I should probably say they *had* divided it.

The Sword Saint, Mae Jonghak, who had remained hidden from the world for so many years, was now the Alliance Leader. The Disciple he had taken in during his later years had gained tremendous fame, and as a result, the influence of their sect, Huashan, had grown to an extent that could not be compared to the past.

What about the Zhongnan Sect?

*Two of its three Supreme Peak masters are laid up and wheezing.*

The Roaring Fury Swordsman had been crushed by Jeok Cheongang, while the Taeeul Merciless Sword had been crushed by me.

At least Hyuk Sopyung, the young prodigy around my age known as the Zhongnan One Dragon, was a fairly decent guy. But so far, my impression of the Zhongnan Sect had been anything but good.

No. At least among the orthodox factions, it was the worst.

*If the upper reaches are that rotten, they can forget about ruling the world.*

At this point, calling it the *Fucknam Sect*—or the *Zhong-fucking-na Sect*—would hardly be an exaggeration.

Well, the current Sect Leader, the Wind-and-Cloud Sword Lord, might be different. But from everything I had seen and heard in the Murim so far, my personal opinion of the Zhongnan Sect did not seem to be all that different from the general public’s.

*But if the word Zhongnan came up at this point…*

I could feel it. I could feel something coming.

Just as I unconsciously furrowed my brow, Baeksang continued speaking.

“The Sect Leader of the Zhongnan Sect at the time, Venerable Wusang, was a righteous and wise man. He remained calm in every situation and treated people fairly regardless of their background. That was why the Palace Lord and I agreed that he should become the commander-in-chief of the Southern Army.”

“Venerable Wusang…”

“That’s right. He was the master of the current Sect Leader of the Zhongnan Sect, the Wind-and-Cloud Sword Lord.”

It was a title I had heard several times from Jeok Cheongang.

Of course, when Jeok Cheongang referred to the Zhongnan Sect, he usually called them “a bunch of rude, worthless bastards.” But even he had described Venerable Wusang as “soft, but a fine man.”

“The problem occurred right after we entered Gansu. The defeated soldiers from the surrounding areas, who had been retreating in a daze, gathered at Great Snow Mountain. There were no fewer than two thousand of them.”

“…How did two thousand defeated soldiers from the surrounding area suddenly appear?”

“Do you think the phrase ‘a hundred thousand practitioners of the Demonic Path’ existed for no reason? Even though they had lost their central figure, the Heavenly Demon, their numbers were not something that could be ignored.”

“So what happened? Was there a battle at Great Snow Mountain?”

Baeksang slowly nodded.

“It was a battle we had every reason to win. At the time, the Western Army we belonged to had Venerable Wusang, a Supreme Peak master, as well as the Palace Lord, who had only just begun to be called the Beast Miao King. We were not inferior in either the number or the quality of our troops. If anything, we had a considerable advantage.”

“From the way you’re talking, the Western Army must have been pretty large.”

“More than four thousand in total. The enemy did not have any notable Supreme Peak masters, either, so there was no reason for us to avoid the battle.”

“Hmm.”

Two Supreme Peak masters the enemy did not possess. Twice as many soldiers. And the enemy they had to fight consisted of defeated soldiers already worn down by exhaustion and despair.

Anyone could see that the outcome of the battle had already been decided.

But if it had been such an easy fight, Baeksang would not have lost his only son.

“There was a trap?”

At my sudden question, Baeksang answered in a voice as dry as sand.

“Yes. We divided our forces into three groups and advanced into Great Snow Mountain. What awaited us there was not a group of defeated soldiers, but an elite strike force of the Demonic Cult.”

“…”

“It was chaos from beginning to end. Arrows poured down like rain from above the gorge, while rocks weighing hundreds or thousands of geun crushed people and blocked the narrow paths.”

“…”

“By the time we realized it was a trap, everything was already too late. We fought the enemy in a frenzy, and then, at some point, I looked up and realized that the person who should always have been beside me was gone.”

He did not say the name, but I immediately understood.

The person Baeksang was talking about was not the Beast Miao King.

*Baekhwi.*

Baeksang’s only child, and the heir who was meant to inherit everything from him.

To set an example as a great chieftain, he had taken his young child with him to the battlefield. But he had probably cherished his son more than his own life.

And then, on a battlefield painted with corpses and blood, the fine young man he had raised had vanished without a trace during the final battle.

“I was afraid for the first time. Hwi. That child was my entire world. No—he was more than that.”

Baeksang’s voice was hollow as he continued.

“But I had to regain my composure, if only for the warriors under my command. First, I requested support from the Zhongnan Sect and the other orthodox martial artists who had entered the area not far away. Then I helped the Palace Lord fight the enemy.”

It had been an unexpected ambush. The battle had been fierce, but the Beast Miao King, Baeksang, and the Nanman warriors had not retreated.

They fought more violently than ever, and at last, after suffering countless casualties, they achieved victory.

“It was only after the battle in the gorge ended that I learned what had happened. That child had gone down a side path with dozens of warriors, pursuing some of the enemy. And I felt relieved.”

I had been listening in silence when I asked,

“Why?”

“The path connected to territory that definitely belonged to our allies. I believed that the people who had received my request for support would have saved Hwi—that child.”

“…”

I closed my mouth.

It was not anger or sorrow that destroyed a person. It was belief.

And when that belief was betrayed, a person finally fell into despair.

Just like Baeksang now.

“What do you think happened?”

I did not answer, and Baeksang probably had not expected me to. After a brief silence, he slowly continued.

“That child… did not even leave a corpse behind. The bodies of the warriors who had been hacked apart by an unidentified enemy were scattered everywhere. Only later did I learn that the culprit was the fiend who ruled Great Snow Mountain—the Great Snow Fiend.”

“…”

“Reinforcements? There were no such things. They said the messenger who had set out to request support had been killed by the enemy while on his way to the other allied forces. I was overwhelmed by grief and despair, unable to do anything. And it was only later that I learned the truth.”

At that moment, Baeksang’s entire body trembled.

And I saw it.

An emotion had been layered over his eyes, which were always cold and subdued.

“The ones who killed the messenger were not the enemy. They were our allies.”

It was anger.

Hatred.

“They had not been unable to provide support. They had simply chosen not to.”

It was also the quiet, desperate scream of a man whose faith had been betrayed.

“If they had come, he could have lived. But they did not come. They killed the messenger, ignored my desperate request, and chose to pursue the retreating enemy instead. Do you know why?”

Anything that pools will overflow when the time comes.

Though Baeksang had spent decades emptying it out, hatred and a sense of betrayal had kept welling up in his heart until they burst forth once again.

Just as they did now.

“Because we were nothing more than savages from the Outer Lands!”

“…”

“Because we weren’t Han Chinese like them, could never become Han Chinese, and they couldn’t sacrifice themselves for savages like us!”

Boom! Crash!

A powerful, violent wave of energy whipped through the underground prison.

The floor and walls, made from solid rock, crumbled. Streams of tangible internal energy poured from his fist and grazed my face.

Sssht!

A sharp, stinging pain.

I felt hot blood run down my forehead.

But I did not move. I merely stared at him.

Until Baeksang’s eyes, flashing with killing intent, turned toward me.

“The Central Plains—the Han Chinese—betrayed us. We willingly reached out our hands when they were at their most desperate, but they betrayed us after we fought with our lives on the line for ten years!”

The hatred of decades ago was directed entirely at me.

Only then did I part my tightly closed lips.

“Why didn’t you tell Venerable Wusang? If it had been him, he would have brought everything to light.”

“Venerable Wusang?”

Baeksang laughed aloud.

The first laugh I had ever heard from him was hollow. It was so empty that it could hardly be called laughter.

“Yes. He would have. If he had been alive.”

“That means…”

“He entered the battle while suffering from a recurrence of his Internal Injury, and the Great Snow Fiend eventually killed him. The Zhongnan Sect, enraged by his death, pursued the enemy after killing the messenger we had sent and ignoring our request for support. The dozens of large and small sects that had been assigned to the Western Army alongside us were no different.”

“What?”

“You don’t believe it? Neither did I. There was only one person—the Palace Lord—who tried to uncover the truth behind everything that had happened. But every false front and every stain was buried when the Great Faction War ended.”

“…”

“And while everyone except us was basking in victory and peace, the messenger’s corpse, which had been kept in storage, also disappeared. Even the last evidence bearing traces of the Zhongnan Sect’s martial arts was gone.”

*These fucking lunatics.*

I swallowed a groan.

I felt suffocated.

If Baeksang’s words were true, then no one—not even me—could condemn his anger.

*He had fought with his life on the line, and all he received in return was betrayal.*

The most fucked-up part of all this was the instinctive certainty that this long-ago incident, which had left behind not even a shred of evidence, had probably really happened.

*Damn it.*

After coming to the Murim, I had been included within the boundaries of the Han Chinese myself, so I knew.

I knew how the people of the Central Plains looked at them.

And I knew how shallow human emotions and greed could be.

Baeksang had fought the enemy for the sake of victory even after his son disappeared.

But the allies he trusted had not.

The Zhongnan Sect, enraged by Venerable Wusang’s death, had ignored the Nanman Beast Palace’s request and pursued the enemy. The other sects belonging to the Western Army had been blinded by their fear of losing troops and their greed for military credit.

And the result of everything they had done was standing before my eyes right now.

“You said earlier that this land—Nanman—was rotten.”

Drip. Trickle.

In the aftermath of what had just happened, foul-smelling water poured from the cracked ceiling.

Beyond it, Baeksang’s eyes gleamed coldly.

“That day, you people showed me what I had to do.”
## Chapter artifact 663

# Chapter 663

“That day, you people showed me which path I should take.”

With those words spat out in a bitter voice, his story—neither short nor long—came to an end. I silently stared into Baeksang’s coldly gleaming eyes.

What did I want to say to him?

*Well… I don’t know.*

This man standing before me in dazzlingly white robes had lived through a darkness I could not even begin to imagine.

He had fought for a righteous cause, only to be betrayed in the end. He had lost the child he cherished more than his own life.

There could only be one reason he had continued living all this time.

*Revenge.*

Baeksang wasn’t wrong. After losing his only child and wandering through pitch-black darkness, he had been shown a torch by the cold betrayal of the Central Plains people. And with that light, Baeksang had discovered the only path laid out before him.

The path of revenge.

He had walked a thorny road of pain and fury to reach this place, and seeing him suddenly reminded me of someone else from my memories.

“…The Head Elder.”

A flicker of confusion crossed Baeksang’s eyes when he heard the mutter that escaped me before I could stop it. I bitterly smacked my lips and continued.

“It’s nothing. Looking at you just reminded me of someone I used to know.”

“For what reason?”

“He was an idiot, too. Just like you. A puppet controlled by Dark Heaven.”

“What?”

“But at the same time, I could understand him well enough. He had his reasons.”

“…He was betrayed.”

“Yeah. By someone who shared his own blood.”

Baeksang silently looked down at me before parting his lips.

“What became of him?”

“I killed him. With my own hands.”

“…!”

“He was one of the senior figures in my family, but I had no choice. Things had already gone too far.”

“Do you wish to condemn me?”

I let out a short laugh.

Condemn him? What would condemning him accomplish now?

“Condemnation that ends with words has no effect. Someone like that won’t stop over something so trivial. That was the biggest reason I cut the Head Elder’s life short.”

That was how revenge fiends met their end.

They stepped onto a path they had never wanted to take, then lost their way forever. They were like moths rushing toward a single torch—the torch of revenge.

“After killing the Head Elder, I suddenly had a thought. If I and the Jin Family of Taiyuan had been the ones to lose that battle… after succeeding in his revenge, would he finally have become happy?”

“That…”

“Probably not. He lived only for revenge, but at some point, his anger must have dulled, and watching innocent people be sacrificed must have left him feeling guilty.”

I continued without waiting for an answer.

“Just like you do now.”

“…!”

I calmly looked into Baeksang’s twisted face.

“I definitely don’t understand you. I’ve never gone through what you did, and I’ve never burned with revenge for decades. But at the same time, I admit it. At least as far as I’m concerned, your anger toward the Central Plains people and the Han Chinese is justified.”

“Justified?”

Baeksang asked again with a rigid expression. It was probably an answer he had not expected, but everything I had said a moment ago had been sincere.

And so were the words leaving my mouth now.

“Yeah. I would’ve done the same thing if I were you. No—if I had been in your place, perhaps the entire Central Plains would already have been my enemy.”

Suddenly, I remembered the day I had headed for the Ares Guild.

Back then, I had been alone, but there had not been even a trace of hesitation in my steps.

It wasn’t because I had possessed enough strength to make that choice. It was because I had been genuinely furious over Kim Hwajong’s death.

That was how I brought down the Ares Guild.

If I had been Baeksang instead of Jin Taekyung, I would have fought to bring down the Central Plains.

But…

“Is that anger of yours justified toward the Nanman people living on this land, too?”

“…!”

“Of course, there must be people who understand you. But what crime did the victims created by your alliance with Dark Heaven commit? What about their families? Their lovers and friends?”

Baeksang’s entire body jerked. I continued in a calm voice.

“When I first set foot in Nanman, I heard some news. A Miao village had been massacred by a group of Han Chinese. Those Han Chinese had slaughtered a hundred people, men, women, and children alike, but in the end, both sides had been destroyed by poison.”

Being locked alone inside an underground prison meant having a great deal of time to think.

As I went over everything that had happened from beginning to end, I could reach only one conclusion.

“It’s strange, no matter how I think about it. Even if a battle had taken place, how could there not have been a single survivor among all those people?”

It had been a sinister plot planned from the very beginning.

By wiping out a single Miao village, they had caused hostility toward the Han Chinese to boil across all of Nanman.

“And that isn’t all. The Thousand-Year Spiders that suddenly escaped the Poisonblood Grounds, and what happened at the Western Yao Estate. Add the Miao village to that, and the number of dead easily exceeds three hundred.”

All of that had happened in a mere seven days and nights since I arrived at the Nanman Beast Palace.

Compared to the several decades Baeksang had spent living as a revenge fiend, it was barely a moment. And what frightened me even more was what lay ahead.

For him to complete his revenge, a war with the Central Plains was not a possibility born of chance.

It was inevitable.

“Just how…”

I looked at Baeksang with pity and anger.

“How much more blood do you intend to spill, Baeksang?”

* * *

Splash. Splash.

With every step he took, stagnant, foul-smelling water that had been pooled on the floor of the underground prison for a long time splashed in every direction.

But the owner of those footsteps did not care that the hems of his snow-white robes were getting dirty.

No. It would be more accurate to say that he failed to notice because his mind was filled with other thoughts.

Splash…

The leather shoes, already soaked through, suddenly stopped moving.

While crossing the underground prison alone, the middle-aged man, Baeksang, suddenly looked back over his shoulder.

Dark, cold, and silent.

Just like the path he had walked.

And just like the path the one imprisoned beyond this point would have to walk from now on.

But he—Jin Taekyung—would not be able to walk the same path.

There were only two days left until the public execution.

Unlike Baeksang, who had walked for several decades, Jin Taekyung had a path that was far too short and clear.

*It is already as good as over. He will not escape.*

Baeksang already knew roughly how great Jin Taekyung’s martial prowess was.

A Supreme Peak master who stood out even in the Central Plains, where countless prestigious sects had taken root.

Though Baeksang himself had not fought at full strength, he had instinctively realized it when they had briefly exchanged moves several days earlier.

*Half a move above me. No… perhaps an entire move.*

Jin Taekyung was a monster beyond imagination. But with his internal energy sealed and his body restrained by iron balls of enormous weight, he could not survive even if his master, the Fire King, came to save him.

And there was an even greater restraint binding him than the iron balls.

*The Han Chinese under his command.*

Jin Taekyung cared about his people. That was why he had chosen to surrender and be locked inside the underground prison instead of fleeing.

*What a fool.*

The greatest weakness of that monstrous young man Baeksang had observed was his human compassion.

The very thing that made a martial artist unlike a martial artist more than anything else.

But…

More than anything, it was the thing that made a person human.

And on that day when the snow-covered Great Snow Mountain had been dyed red with blood, it was the very thing Baeksang had desperately wanted from his allies.

*Come to think of it, Hwi was about that age then, too.*

Baeksang stared blankly into the empty air. In the darkness where nothing existed, a face briefly passed through his mind.

From an infant to a boy, and from a boy to a young man.

His only child, who had been more upright than anyone and shone as brightly as his name, Hwi.[^1]

And the smiling face of the child he would never see again.

Crunch.

Without realizing it, Baeksang clenched his fist tightly. His neatly trimmed nails dug into his flesh, and blood began to flow.

Drip. Drip-drip.

Baeksang lowered his gaze toward his feet. He saw red drops of blood spreading across the stagnant water.

Each small ripple that formed drew the outline of one person’s face.

*How much more blood do you intend to spill, Baeksang?*

Jin Taekyung’s final words continued to echo in his ears.

But Baeksang’s answer had been the same then as it was now.

*I have already crossed the river. I can never go back.*

He had crossed that river a long time ago.

Baeksang had been half-mad with despair and rage when he met a beautiful woman whose identity he could not discern one day. She offered him something even more captivating than her appearance.

No.

She offered him something he could not refuse.

*Choose. If you do it, it will definitely come to pass.*

Baeksang had not hesitated.

Once he had found a goal in life, he had gladly taken the hand she held out to him, and he had never regretted that decision.

No.

He must not regret it.

*But why…?*

Now that he was standing on the verge of finally reaping the fruits of several decades, why was he wavering?

Baeksang swallowed the voice trying to escape him and clenched his teeth. Then, as he looked at his already filthy leather shoes and the hems of his robes that could no longer be called white, he repeated the words to himself.

*In two days. Everything ends. Everything.*

At Baeksang’s feet, drops of blood spread across the stagnant water.

The water had been dirty for a long time already, and as it absorbed the blood, it slowly turned red.

Just like the path he had walked.

Just like the path he would walk from now on.

Splash.

Baeksang roughly stomped through the puddle and began walking again.

In the silent space where no one opened their mouth, he listened to Jin Taekyung’s voice still echoing in his ears.

* * *

Baeksang had left, and I was alone again.

My entire body, restrained by tightly drawn chains and iron balls weighing ten thousand geun, was gradually growing stiff.

*Damn.*

Now that Baeksang was gone, I felt a little disappointed.

Maybe I should have begged him to spare me. But even so, I didn’t regret it. I had said everything I needed to say.

There was nothing to gain from begging for my life in such an ugly manner.

Baeksang had lived while looking at nothing but revenge. Even if I begged and pleaded, he wasn’t going to tear up like some middle-aged woman who had just watched a human-interest documentary.

Of course, that didn’t mean I intended to be dragged out two days from now and quietly accept my death.

*Are you crazy? I have to survive somehow.*

It was true that I acknowledged Baeksang’s anger.

But that didn’t make it a good enough reason for him to kill me. From my perspective, both the Head Elder and Baeksang were just idiots with sad stories.

And I intended to stop this new idiot I had met after traveling all the way to a foreign land, no matter what it took.

*But how do I get out?*

After talking so much and thinking so much, my throat was parched.

I was swallowing dryly when something cold touched the crown of my head from above.

Tap.

“Huh?”

It was water. It might have been stale and tasteless, but the important thing was that it was water. The ceiling had probably opened up farther when Baeksang smashed the surrounding walls.

*That’s useful.*

I muttered inwardly and tilted my head back toward the ceiling.

The next moment, my eyes met someone’s completely unexpected gaze through a crack in the broken ceiling.

Huge, clear eyes like a calf’s.

“…Why are you up there?”

The owner of those eyes answered.

“Taishan. Hungry. Got locked in underground prison because they said Taishan eats too much.”

“Ah.”

Then that checks out.

[^1]: *Hwi* (輝) means “shining.”
## Chapter artifact 664

# Chapter 664

Unlike modern prisons, where the concept of human rights has been mixed in just enough to make them palatable, the underground prisons found throughout the Murim served their purpose exceptionally well.

The word *human rights* did not exist here in the first place.

The underground prison of the Sichuan Tang Clan, for example, had been closer to a torture chamber than a place meant merely to lock up criminals.

Even the old guard who had died during Dark Heaven’s attack had been a torture expert with several decades of experience. He would often reminisce about his prime with a pleased smile.

“Those days right after the Great Faction War were wonderful. We caught three or four notorious fiends every day—counting them like animals, of course.”

“…Like animals? Not people?”

“Yes. When we lined up fifteen or so of the beasts and got to work, the response was incredible. They were so happy they nearly passed out.”

He even counted people the way one counted animals.

I had never bothered to ask for details about what had happened back then, but it was difficult to imagine prisoners nearly passing out from happiness just because he had given them pretty tattoos with the small knife he kept so carefully tucked into his belt.

*Like hell they were tattoos.*

It was obvious.

Bones and flesh splitting apart, blood spraying everywhere—something like that.

I had gone a little off track, but in any case, most underground prisons in the Murim were more or less the same, with only minor differences.

Cold, damp, and nine times out of ten, buried deep underground.

Just like the underground prison of the Nanman Beast Palace where I was currently locked up. And…

“Pavilion Master. Taishan hungry. Got locked in underground prison because Taishan eats too much.”

“Ah.”

The difference between me and that accursed bastard was only one floor.

The third and fourth underground floors, for example.

*So this is how it turned out.*

In a way, it was the result of an old, poorly built prison and a considerable impact coming together in one incredible coincidence.

I stared blankly at the ceiling. Then I gave a quiet laugh toward Taishan, who was blinking his enormous eyes through the small hole above me.

“Pavilion Master, why laugh?”

“Because I’m happy to see you.”

“Happy? Pavilion Master happy to see Taishan?”

“Yeah, you bastard. I’m so happy I could die.”

“Oh. Then Taishan happy to see Pavilion Master too.”

It might have seemed like a completely pointless conversation, but every time I saw his eyes peering through the gap, I couldn’t stop a laugh from escaping.

Meeting a familiar face was one thing. More importantly, I might be able to get out of here sooner than expected.

Of course, there was also the fact that he was the only person who could answer the question that concerned me most.

“What about everyone else? They’re all doing okay, right?”

At my question, his enormous calf-like eyes grew damp.

“Are you… crying?”

“Sniff. Pavilion Master.”

*No way.*

A sense of foreboding rushed over me. I hurriedly opened my mouth.

“Don’t just bawl. Tell me properly. What happened?”

“Taishan… sniff. It couldn’t be helped. It’s so unfair.”

“……!”

Damn it. My vision went dark. I could already see the members of the Fire Dragon Pavilion lying before me as cold corpses.

*Or torture? But how could they do that?*

It had only been half a day since I surrendered on the condition that the Fire Dragon Pavilion members would be kept safe.

This was something the Beast Miao King himself had promised. No matter how powerful Baeksang’s faction had become, this was impossible.

*If they were harmed, then what the hell did I surrender for…?*

Just as I was muttering those words hollowly inside my head, Taishan spoke in a damp voice.

“I still can’t believe it. By now, everyone must be eating without Taishan.”

“……?”

“I hate Lord too. I hate Namho too. Taishan is so unfairly treated.”

“……!”

“Pavilion Master. In that case, do you have anything to eat?”

What the hell was going on?

After remaining silent for a moment, I answered with all the sincerity in my heart.

“No, you fucking bastard.”

“Aw. Taishan hungry.”

“…Come down. Come down right now.”

That son of a bitch. He really wanted to die.

As my blood pressure soared, rage took control of my entire body. Since being locked in the underground prison, I had never thrashed around so violently in anger.

Clatter! Clank!

If not for these goddamn heavy iron balls, I would have started by punching that bastard in the mouth.

Taishan watched me panting with interest before speaking.

“Namho and Lord are safe. They are being held in different places, so Taishan doesn’t know much, but the White Tiger’s master told Taishan.”

“The White Tiger’s master? Yayul Mok?”

“Oh. Taishan remembers. Right. Yayul Mok.”

It seemed the Beast Miao King had made arrangements after all. I stopped thrashing around in anger and let out a sigh of relief.

“You should’ve said that first, you lunatic. You nearly gave me a heart attack.”

“Taishan has been hungry for two shichen already. Taishan’s mind is hazy.”

“…People don’t usually call it hunger after two shichen. More importantly, how did you end up locked in here? Great Hero Yayul would’ve stopped it before it got this far. There’s no way you were locked up just for eating too much.”

“Taishan was treated unfairly. A Nanman man was going to leave after giving Taishan food the size of mouse droppings, so Taishan grabbed his wrist and asked for more. His bone broke.”

“……”

“Taishan was surprised and grabbed his other wrist. That one broke too. This was obviously a trap.”

Clatter! Clank! Clank!

“Pavilion Master, calm down. Taishan was angry too, but Taishan held it in and surrendered, just like Pavilion Master.”

“…Come down. This time, really come down.”

I was already struggling to keep a low profile, and this bastard had broken both arms of the man who came to feed him?

At this rate, I was going to die of rage before noon two days from now.

*I entered the tiger’s den to save a bastard like that?*

After barely calming my fury, I asked,

“Then what about the others? Not Namho or Sama Pyo. Everyone else?”

“Hmm. Ah.”

Taishan rolled his enormous eyes around as he thought, then answered.

“I heard they were captured.”

“Captured?”

“Yes. But they said they weren’t coming here. Taishan doesn’t know why, but the White Tiger’s master said it was safer that way.”

Ju Hwaran, Song Ilseom, and Hyuk Mujin.

Hearing that even the three members of the reconnaissance squad had been captured made my heart feel heavy for a moment. But I agreed with Yayul Mok that they would be much safer there.

*Baeksang’s influence can’t reach that place for now.*

The two tribal chieftains leading the reconnaissance squad were loyal to the Beast Miao King.

What was more, some of the Nanman people I had rescued from the Poisonblood Grounds were their kinsmen. Unlike the other chieftains who had turned to Baeksang’s side, they wouldn’t easily switch allegiances.

*The three of them are more likely to be in danger than they are now if the reconnaissance squad runs into the Blood Monk.*

The Blood Monk was an unidentified old monster who had stained Guizhou with blood all by himself, wielding Supreme Peak martial prowess.

Almost nothing was known about him. But if he really was a subordinate of the Southern Heaven Demon Empress, as I suspected, then the situation would become the worst it could possibly be.

He would certainly head south on the Southern Heaven Demon Empress’s orders. And if he encountered the reconnaissance squad, the three people among them would fall into his hands as well.

“…Damn it.”

But for now, I had no time to worry about that.

They were still on the move at that very moment, while I was trapped in a prison deep underground, unable to move an inch.

*All I can do is hope my guess about the Blood Monk is wrong.*

So there were only two things I could do right now.

The first was prayer.

The second was…

*Escape.*

Ding.

> **System**
>
> A new Quest has been generated!
>
> Would you like to check the linked Quest, **Escape from Namshank**?[^1]
>
> **Y** / **N**

I nodded and thought,

*I have no idea who developed the System, but they came up with one hell of a shitty Quest title.*

“So, Pavilion Master. Do you have anything to eat?”

…Correction. *That* bastard was the shittiest of all.

[^1]: A pun on *The Shawshank Redemption*, replacing “Shaw” with “Nam,” referring to Nanman.

* * *

Among the countless martial artists in the continent, river pirates were an especially rough and free-spirited bunch.

They didn’t want to be oppressed by various laws, didn’t want to be arrested by the authorities, and didn’t particularly want to live decent lives, either.

Sudal, the Deputy Stronghold Lord of the Water Dragon Stronghold, had become a river pirate for exactly those reasons.

Unlike his father, who had ended his life as a good fisherman, Sudal had boldly resolved to live and die as a man of adventure.

He had lived the life of a fairly successful river pirate.

But lately, he had begun to feel increasingly doubtful about what he was doing.

*What the hell am I doing?*

He wasn’t doing anything.

Every day, he sat at the bow and stared at the calm river. When the sunlight became too hot, he went swimming.

That was all.

His immediate superior, who lorded over the Yangtze in Sichuan, had been summoned to League headquarters by the venerable Alliance Leader. Meanwhile, Sudal and his men had drifted down the tributaries all the way to the backwater of Yunnan, wasting their time.

*By now, merchant ships loaded with all kinds of valuable goods must be traveling through Sichuan.*

The Yangtze was a gold mine right now.

All kinds of supplies were moving back and forth as the clouds of war gathered.

Sudal knew that and desperately wanted to return immediately. But every time he did, one man’s presence kept flashing before his eyes.

“I’ll come running whenever you call!”

That was the boast he had made seven days and nights ago.

Naturally, it had been empty words without even a single ounce of sincerity behind them.

But the much younger man had merely smiled warmly and answered,

“Oh, good. Then stay nearby.”

“Excuse me?”

“Heh heh. Did someone stick a marlin in your ear? I said stay here. I’ll need to ask you for another favor when we head back, too.”

“Great Hero Jin, forgive me, but we have a livelihood to maintain…”

“A livelihood. That’s nice. But you need to be alive to make a living, don’t you?”

“……!”

“Come on, I’m asking a favor! Just a favor!”

“Gasp.”

“For fuck’s sake. I might just snap every mast and burn the whole lot down. Want to swim to Sichuan?”

It was called a favor, but in reality, it was a threat.

But what could Sudal do? In the Murim, the one with stronger martial arts was king.

And to make matters worse, that monstrous young man’s Master was a crazy old monster who was actually called a king.

*Jin Taekyung, you bastard…*

Swallowing his tears, Sudal had nodded. In the end, he had spent more than seven days and nights catching fish in a tributary at the edge of Yunnan where not even a small boat could be seen.

That was how things had been until an idea occurred to him just yesterday.

*Wait a minute. Do I really need to do this? There’s still plenty of time before that Jin Taekyung bastard comes back.*

Although he had only operated along the Yangtze, Sudal knew what a godforsaken dump Nanman was.

He didn’t know exactly what Jin Taekyung’s mission was, but considering that he had come all the way here, it could not possibly be simple.

But did he really need to worry about someone who wasn’t even here and whine like a dog that needed to shit?

Sudal seriously reflected on the adventurous life he had lived. Then he gave his men an order.

“Hey, boys. Let’s go get some fresh air.”

“Excuse me?”

“Where?”

“Guizhou’s right next door. It’s close, so let’s make a sweep through it, raid the place, and come back.”

Sudal’s ambitious plan was not well received by his subordinates.

“Deputy Stronghold Lord, have you lost your mind?”

“Fuck. If you want to die, die alone. You’re not even the boss—why should we all end up cremated?”

But Sudal had already formed a grand plan.

“Dunk that bastard. In the Yangtze. The Yangtze…”

“The Yangtze dip?”

“Yeah. That thing Jin Taekyung does all the time.”

After sending two of them into the water one after another, the complaints disappeared. Under Sudal’s spirited command, three swift ships traveled along the western tributary toward Guizhou.

At last, after all this time, they found a target.

Just like now.

“There’s a ship roughly two hundred zhang ahead!”

“Seize it! Don’t let it get away!”

How long had it been since their last raid?

Sudal stood tall at the stern like a Great General, smiling with satisfaction as the ship drew rapidly closer.

Then, before fifteen minutes had even passed, he realized that something was wrong.

Whoosh!

The ship had drawn so close that it was almost right in front of them. There was no crew. No captain.

Only one person was waiting for them.

“A swift ship of the Yangtze River Channel League. How fortunate.”

“……!”

The bald, middle-aged man holding a blood-soaked Zen staff smiled broadly at the frozen Sudal.

“Does this ship go to Nanman too?”

# Checkpoint Review — 245–249

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

# Chapters 245–249

## Plot

The Star-Array Grand Banquet opens at Mount Song. Hong Dao warns that darkness is coming, while Jeok Cheongang urges Jin Taekyung to win and defeat anyone from the Peng Family. During the preliminaries, Taekyung’s restrained strike is eclipsed by the Iron-Water Divine Dragon’s overwhelming Ship-Breaking Fist, but Taekyung responds with the Flame-Extinguishing Divine Fist and wins every assessment.

Taekyung takes unanimous first place, defeating the Iron-Water Divine Dragon, Kunlun Cloud Dragon, Divine Marvel Dragon, Successor Beggar, and Hunroe Leg. During the free day, Jeok conceals his pride beneath stern advice. At Shaolin, Hong Dao reveals that heavenly patterns identify Taekyung as the Morning Star that rose while Jeok’s star was fading. Hong plans to step down as Abbot after the banquet and may have roughly one year left to live.

More than five hundred finalists travel to Luoyang for the main event. Taekyung meets the three eccentric finalists Baek Woo, Gung Gibang, and Zhuge Gyun, forcing the first two to behave respectfully while Zhuge chooses a cryptic third option. Song Ho, the Thousand-Faced Fox, arrives and identifies himself to the finalists. He recognizes Taekyung as Jeok’s Disciple and says Taekyung’s destruction of the mechanism core allowed about one hundred additional applicants to qualify.

## Continuity

- The preliminaries lasted three days and reduced more than fifty thousand applicants to approximately five hundred finalists.
- Jin Taekyung won unanimous first place with perfect scores in all five assessments.
- Taekyung defeated the Iron-Water Divine Dragon, Kunlun Cloud Dragon, Divine Marvel Dragon, Successor Beggar, and Hunroe Leg.
- The Iron-Water Divine Dragon abandoned the banquet and returned to the Yangtze.
- The Star-Array Grand Banquet main event will use a different format, with spectator stands for the duels, and is about to begin in Luoyang.
- Jeok Cheongang is publicly Taekyung’s Master and is proud of Taekyung’s victory, despite hiding it behind harsh advice.
- Hong Dao identifies Taekyung as the Morning Star that rose in the northern lands while Jeok’s star was fading.
- Hong Dao entrusted the Green Jade Buddha Staff to Unnamed, appointed an interim successor, and intends to step down as Abbot after the banquet. Unnamed remains in Arhat Cave.
- Hong Dao may have approximately one year of life remaining.
- The Ten Kings were the ten Supreme Peak masters of the Great Faction War; the Spear King and Wave King are dead, leaving eight effective survivors.
- Baek Woo, Gung Gibang, and Zhuge Gyun are finalists from Kunlun, the Beggars’ Sect, and the Zhuge Clan respectively.
- Song Ho is an elderly Peak master with a genial public manner and predatory attentiveness beneath it. He recognizes Taekyung and knows about the mechanism-core incident.
- Open hooks include Taekyung’s performance in the main event, the identity of the Gold-Faced Young Master who bet on him, the concealed strength of other finalists, Hong Dao’s chosen successor, and whom Song Ho was studying.

## Translation Decisions

- Use Iron-Water Divine Dragon for 철수신룡 and Seafaring King for 해상왕.
- Use Dogon for 도곤.
- Use Flame-Extinguishing Divine Fist for 멸염신권 and Ship-Breaking Fist for 파선권.
- Use Kunlun Cloud Dragon, Successor Beggar, Divine Marvel Dragon, and Hunroe Leg.
- Use Wave King for 낭왕 and Arhat Cave for 나한동.
- Use Benefactor Jeok for 적 시주 and Fellow Daoist for 도우.
- Use the three idiots for 세 얼간이.
- Use Eighteen Dragon-Subduing Palms for 항룡십팔장.
- Use Three Visits to the Thatched Cottage for 삼고초려.
- Retain hyung in Jin hyung.

## Durable state

{
  "active_continuity": [
    "The Star-Array Grand Banquet preliminaries ended after three days, and approximately five hundred of more than fifty thousand applicants advanced to the main event.",
    "Jin Taekyung took unanimous first place overall with perfect scores in all five preliminary assessments.",
    "Taekyung defeated the Iron-Water Divine Dragon, Kunlun Cloud Dragon, and Divine Marvel Dragon, all members of the Ten Dragons and Phoenixes.",
    "The Beggars' Sect's Successor Beggar was comparable to those young prodigies, and the Hunroe Leg was a renowned Peak master.",
    "The Iron-Water Divine Dragon abandoned the Star-Array Grand Banquet and returned to the Yangtze.",
    "Jeok Cheongang is publicly Taekyung's Master and is proud of Taekyung's result.",
    "Hong Dao's heavenly-pattern reading identifies Taekyung as the Morning Star that rose in the northern lands while Jeok's star was fading.",
    "Jeok Cheongang's will to live was rekindled by meeting Taekyung, and he advanced through the past year's training and contemplation.",
    "Hong Dao entrusted the Green Jade Buddha Staff to Unnamed and chose someone to serve as Abbot until Unnamed returns from Arhat Cave.",
    "Hong Dao intends to step down as Abbot after this Star-Array Grand Banquet and may live for approximately another year.",
    "The Ten Kings were ten Supreme Peak masters of the Great Faction War; the Spear King and Wave King are dead, and eight effectively remain.",
    "Baek Woo, Gung Gibang, and Zhuge Gyun are three eccentric finalists who advanced to the Star-Array Grand Banquet's main event.",
    "Song Ho has arrived at the Star-Array Grand Banquet and identified himself as the Thousand-Faced Fox.",
    "Song Ho is an elderly Peak master with a genial appearance, a large build, and a predatory attentiveness beneath his public warmth.",
    "Song Ho recognizes Taekyung as Jeok Cheongang's Disciple and says Taekyung's destruction of the mechanism core added approximately one hundred qualifiers.",
    "The finalists have traveled from Mount Song to Luoyang and arrived at the Murim Alliance for the main event."
  ],
  "continuity_sources": [
    249
  ],
  "open_questions": [
    "How will Taekyung fare in the Star-Array Grand Banquet's main event?",
    "Who is the Gold-Faced Young Master who bet on Taekyung?",
    "Which powerful martial artists concealed their abilities during the preliminaries?",
    "Who has Hong Dao chosen to serve as Abbot until Unnamed returns from Arhat Cave?",
    "Whom did Song Ho observe with his predatory gaze, and what did he notice?"
  ],
  "safe_through": 249,
  "temporary_decisions": [
    "Use Wave King for 낭왕.",
    "Use Arhat Cave for 나한동.",
    "Use Benefactor Jeok for 적 시주.",
    "Use Fellow Daoist for 도우.",
    "Use the three idiots for 세 얼간이.",
    "Use Eighteen Dragon-Subduing Palms for 항룡십팔장.",
    "Use Three Visits to the Thatched Cottage for 삼고초려."
  ],
  "version": 1
}

## Reading copies

## Chapter artifact 245

# Chapter 245

Waaaaaaah!

The deafening roar of tens of thousands of martial artists made my ears ring.

Carrying dreams of rising to prominence, they had gathered here to attend the Star-Array Grand Banquet and were unleashing an endless wave of cheers.

The noise, which seemed as though it would never end, gradually died down the moment Dharma King Hong Dao raised his hand.

In that hand was the Green Jade Buddha Staff, a symbol of a thousand years of Shaolin. Shaolin Temple—the supreme authority of the Murim. Faced with its formidable prestige, the crowd fell silent.

Then the deep, resonant voice of the old monk, infused with powerful internal energy, spread across the grounds.

“I often look up at the sky. Over the years, I have seen, read, and watched countless stars.”

I had heard this before, at some point.

They said the greatest reason Dharma King Hong Dao had been able to become the Abbot of Shaolin was not his formidable martial arts, but his learning and wisdom.

“The Star-Array Grand Banquet. If you wish to become the brightest star at this banquet, think brightly and act brightly.”

After a brief silence, he added one short sentence.

“That is how one survives even in darkness.”

A congratulatory speech was better the shorter it was. It was even better if it contained a hint of profound wisdom, and better still if the person delivering it was the Abbot of Shaolin.

Another roar of cheers and applause erupted.

“Waaaaaaah!”

As I watched, I suddenly wondered how many of the tens of thousands gathered here had actually understood what he meant.

Probably one in ten.

No, not even one in a hundred.

But I understood. I knew what Hong Dao’s words were referring to.

*Dark Heaven.*

The training in the Fire Gate Cavern had been harsher than everything I had experienced up to that point combined.

Jeok Cheongang had pushed me relentlessly, to the point where he no longer seemed merely impatient. He looked downright anxious.

At first, I had thought it was because of his infirmities of old age.

But not long afterward, Jeok Cheongang finally revealed something after much deliberation. Only then did I understand the reason for his urgency.

Dark Heaven. A powerful enemy that had not yet fully revealed itself.



*We don’t have much time. Keep training and preparing. That is the best thing you can do.*

I looked at the old man standing to Hong Dao’s right.

His small frame was noticeably different from Hong Dao’s, yet he gave off an overwhelming presence. Jeok Cheongang somehow spotted me and flashed a crooked grin.

He was visibly older than he had been a year ago. My chest churned before I knew it.

*You’d better know that you’ll die if you don’t win.*

“……”

*Especially if you run into some bastard with the surname Peng, beat the shit out of him. Break him and tear him apart!*

A cold wind swept through my queasy chest.

One dose of the Fire King’s motion-sickness medicine delivered through Sound Transmission had cured me completely. I quietly averted my gaze.

Until I arrived, I had been fairly confident. But after seeing the enormous number of martial artists in person, I began to think that guaranteeing victory would be difficult.

*I’d better not answer. If I give him a definite answer and then lose, he’ll ride my ass even more.*

In any case, the opening ceremony was over, so the preliminaries would begin soon.

Like a salmon swimming upstream against a flowing river, I pushed my way through the tightly packed martial artists toward the back. Then I spotted a familiar face.

“Huh?”

What was that guy’s name again?

Oh, right. Jongni Chu of Yunnan. The man with the self-styled epithet Always-Victorious Sword.

I had wondered why he had come all the way here from some remote backwater. Apparently, he had come to attend the Star-Array Grand Banquet after all.

*With that level of skill, he should make it pretty far.*

I considered saying hello, but decided against it. It seemed like it would only become a hassle.

Instead, I sent a greeting to the guy standing blankly and looking around, one he could not hear.

*Yeah, you too. Good luck.*

And prayed that, if possible, he wouldn’t run into me.

* * *

“I like duels. There are only winners and losers, and no draws. How clear-cut is that?”

The middle-aged man muttered in a relaxed voice.

A pair of glasses imported from the Western Regions rested on his nose. They had the marvelous ability to make objects appear several times larger, which naturally made them extremely expensive.

“That’s why people bet money on them. The result is certain.”

One of the things that could not be left out of the Star-Array Grand Banquet was gambling.

From the preliminaries, which filtered out the unqualified among tens of thousands of applicants, all the way to the finals, there would be hundreds of duels.

For that reason, the Star-Array Grand Banquet was not only a feast for the martial artists of the world. It was also the greatest season of the year for gamblers across the continent.

“So, who would you like to bet on, and how much?”

The bald man sitting across from the middle-aged man asked the question. At a glance, he looked like someone with one foot in the underworld, but his manner was polite.

“You’re still as impatient as ever.”

“There are a lot of customers waiting.”

“I see. Well, let’s see…”

After pausing for a moment, the middle-aged man pulled a money pouch from inside his robes and tossed it onto the table.

Unable to withstand the weight, the pouch opened, and gleaming silver yuanbao spilled across the tabletop with a clatter.

“A thousand silver nyang on the Iron-Water Divine Dragon of the Yangtze River Channel League.”

“……”

It was an enormous sum.

Even more so considering that the preliminaries had not yet begun.

The middle-aged man clearly had nerve to spare.

The bald man’s eyelids trembled as he stared at the silver yuanbao.

“Are you betting on the Iron-Water Divine Dragon to win the whole thing?”

“Not at all. Cheol Soo may be one of the Ten Dragons and Phoenixes, but he’s not in that league yet. His Master, the Seafaring King, would be another matter.”

“Then…?”

“I’m betting that he’ll take first place in the preliminaries.”

“Hmm.”

The bald man let out a low groan.

The preliminaries of the Star-Array Grand Banquet were known as a “sieve.” There were so many applicants that the unqualified had to be filtered out.

Naturally, with tens of thousands of applicants being judged, there were countless possible outcomes at this stage.

And that meant the odds would be enormous.

“That’s different from what you said earlier.”

“What is?”

“You said you liked duels because there were only winners and losers, and the result was clear-cut.”

“You really shouldn’t gamble.”

The middle-aged man laughed heartily before continuing.

“That’s the kind of thing only third-rate gamblers do. All or nothing. Since one of the two sides is bound to win, the amount you can earn is limited. But who am I?”

“Dogon.”

“Exactly. That’s why I like duels. People want to take the easy road. They don’t want to take the difficult one.”

“Oh.”

A gambler among gamblers. A gambler who had reached the Peak of his craft was called a Dogon.

The middle-aged man before him had come armed with a conclusion reached through meticulous research and calculation.

The bald man bowed deeply, his respect showing clearly.

“I’ve learned a great deal, Great Hero Kwak.”

“If you’ve learned something, you should pay the tuition.”

“What would you like?”

“Keep your mouth shut. Just as you have until now.”

“Of course.”

“Then that’s enough. Let’s see… The preliminaries should be starting soon. I’ll have a drink and come back to collect my money.”

He was completely confident that his prediction would turn out exactly as expected.

That was a Dogon for you.

The middle-aged man pushed up his glasses and left.

A swordsman guarding the door asked in a voice full of curiosity.

“Boss, who was that man?”

“That gentleman? A Dogon.”

“Gasp! A Dogon?”

“And one of the most famous Dogons in the world.”

“Is he really that incredible?”

“There are exactly three legendary Dogons.”

The bald man spread three fingers.

“A-Gwi in Sichuan. Jjak-Gwi in Guangdong. And the last one…”

One of his fingers folded down.

“On a continental scale, that gentleman there. Kwak Cheolyung.”

“Kwak Cheolyung…!”

“So go keep an eye on the Iron-Water Divine Dragon. Now that I think about it, that rookie’s gotten pretty damn cocky.”

Whack!

The bald man kicked the swordsman in the shin.

A short while later, he welcomed his next customer. This one was rather strange, with a mask pulled up over his nose.

“Where would you like to place your bet?”

“Is this confidential?”

The masked man asked in an anxious voice.

He flinched like someone who got beaten whenever an opportunity arose. Anyone could see that he was a Third Rate martial artist.

*The area around his eye is all purple. Wherever he got beaten, it must have been nasty. Well, as long as I get paid, that’s all that matters to me.*

A gentle smile spread across the bald man’s lips.

It was his own professional smile, the kind that appeared automatically whenever he saw a sucker.

“Of course. Go ahead.”

The masked man looked around nervously before pulling out a money pouch.

“A hundred silver nyang on Jin Taekyung, the Sleeping Dragon of Shanxi, taking first place in the preliminaries.”

* * *

“Those from there to here. Follow me.”

There were so many participants in the Star-Array Grand Banquet that there were hundreds of supervisors, and the test grounds had been divided into multiple sections.

The hundred-plus applicants began walking after their assigned supervisor. Naturally, I was among them.

*There really are a lot of people.*

Not only were there many of them, they were incredibly diverse.

There were skinny people and fat people, fresh-faced youths with downy hair and wandering martial artists who looked as though they had been through every hardship imaginable. There were women who immediately drew the eye and handsome men with flawlessly smooth features.

It was a perfect example of how a hundred people could have a hundred different appearances.

Among them, one massive man who looked like the definition of a real man stood out in particular. Judging by our eye levels, he was at least a head taller than me.

*Fuck, is this the continent or Norway?*

He was over two meters tall. His forearms were so swollen with muscle that they looked ready to burst, and a salmon pierced by a harpoon had been tattooed across one of them.

His features were strangely Western as well. He looked so much like a Norwegian that I began to wonder if he really was one.

I stole another sideways glance at him, and our eyes met.

“……”

“……”

I carefully opened my mouth.

“A-Aim fine, thank you. And you?”

“……?”

That wasn’t right. What was it again?

I had stopped studying English after the red pen workbooks of elementary school, so the words barely came out because I was nervous.

“Ah! Where are you from?”

Norway answered.

“You fucking asshole, what are you doing?”

“Oh, I’m sorry.”

“You little shit, are you picking a fight with me right now?”

A hearty string of curses and the gazes of the surrounding people came flying at me.

Just as I was about to answer, the supervisor shouted in a stern voice.

“Anyone who causes trouble will be forcibly disqualified!”

Norway, who had been opening and closing his mouth like a salmon, glared at me.

The transmitted words came with a rough aura and killing intent as sharp as a harpoon.

*I’ll make you regret this.*

Talk about vicious. A true descendant of the Vikings.

*But whatever. I was in the wrong.*

I bowed my head in apology and continued walking. A powerful snort sounded from behind me, but I pretended not to hear it.

*He’s pretty strong, though.*

He looked to be in his twenties, and my heart fluttered at the thought that I had encountered such a formidable opponent right from the start.

*The world really is wide.*

If the preliminaries were already this intense, genuine monsters might come crawling out during the main event. Remembering Jeok Cheongang’s warning, I steeled my resolve.

* * *

“The first thing we will assess is your fists and feet.”

The place we reached after following the supervisor was an unnamed cliff.

I did not need to ask how the test would be conducted.

Other people were already taking it.

Whack! Crack!

“Graaagh!”

A foolish martial artist with his wrist twisted rolled across the ground. The supervisor sighed and broke a bamboo marker.

“Jangyu of the Butterfly Sect, eliminated. Next!”

The next martial artist stepped forward and threw one punch at the cliff.

Boom!

This martial artist was around the First Rate level. At least he knew how to put internal energy behind his strike.

A clear mark appeared on the cliff, which was a hard-packed mixture of roughly equal parts rock and soil.

The supervisor measured the mark’s depth and width, then nodded.

“Gobul of the Sodang Sect, passed. Next!”

Those who passed stepped aside, while the Third Rate martial artists whose punches left weak marks or whose hands hurt after a single strike were eliminated in droves.

“You can probably tell how this works by now. Then let’s begin. Now, let’s see…”

The supervisor pulled out a bamboo marker.

Then a name rang out.

“Jin Taekyung of the Jin Family of Taiyuan.”

As the gazes of the people around me turned toward me, a System notification rang out.

Ding.

> **System**
>
> - **Quest:** **Star-Array Grand Banquet** has been created.
## Chapter artifact 246

# Chapter 246

> **System**
>
> **Quest**
>
> **Star-Array Grand Banquet**
>
> What more needs to be said?
>
> Go forward without hesitation. Become the winner of this banquet watched by all under heaven, leave your mark on the Murim, and enjoy the glory!
>
> **Grade:** Supreme Peak
>
> **Restriction:** Jin Taekyung
>
> **Mission:** Win the Star-Array Grand Banquet (Incomplete)
>
> **Reward:** ???
>
> **Failure:** Fire King's Wrath

“……”

I paused at the penalty I would receive for failing.

*I mean, it’s possible I might not win the Star-Array Grand Banquet. Is he really going to get angry over that, too?*

Imagining Jeok Cheongang throwing a tantrum, I began to feel wronged.

*And after teaching me for barely a year.*

Of course, my case was extremely unusual.

Even so, the fact that the Quest window went out of its way to spell it out suggested just how much Jeok Cheongang expected of me.

“Jin Taekyung of the Jin Family of Taiyuan. Where are you?”

“Oh, here.”

I closed the Quest window at the supervisor’s call and started walking.

With every step I took, I felt the people’s gazes on me. Along with them, murmuring voices pierced my ears.

“Jin Taekyung of the Jin Family of Taiyuan…”

“The Sleeping Dragon of Shanxi?”

“Is that the young man? The one who was taken in as the Fire King’s Disciple?”

“That’s him. Definitely.”

I could also hear the same gruff voice from Norway that I had heard earlier.

“Hmph. So you had something to rely on after all. You may look the part, but you’re still a weakling.”

I ignored the whispers coming from every direction and stopped in front of the cliff.

The supervisor, who had been looking at me with an astonished expression, spoke in a suddenly more polite tone.

“If the depth is at least three Korean inches, you pass. Anything shallower is a failure.”

“Yes.”

Three Korean inches was roughly ten centimeters.

An ordinary First Rate master who had steadily trained in fist techniques could pass without much trouble at that level.

But now that I was actually about to do it, tension began to build.

*Damn. I have no idea how much force to use.*

I honestly had no clue. Exactly how much strength did I need to apply to leave a mark three Korean inches deep?

After staring at the cliff for a while, I decided to use the Help function.

“Excuse me, Supervisor.”

“Yes?”

“As long as the depth is at least three Korean inches, I pass, right?”

“That is correct. However, once your fist lands, the test is over.”

“Oh, I see.”

*Well, that makes it easy.*

I nodded and immediately placed my fist against the cliff. Then I gave it a gentle push.

Thump! Rumble-rumble-rumble!

The surface of the cliff split as softly as tofu. Crumbled pieces of rock and dirt poured down.

With my arm embedded all the way to the elbow, I looked at the supervisor.

“I pass. Okay?”

“……”

The supervisor’s expression was a sight to behold.

He stared at my face, then at the arm stuck in the cliff, his mouth hanging open. Finally, he stammered out a question.

“H-How did you do that?”

“I pushed.”

“I mean, how did you…”

“I just put some strength into it and pushed.”

“……”

“Anyway, I passed, right? My fist didn’t even land, and it went in plenty deep.”

“W-Well…”

The supervisor’s pupils wavered.

“I-I’m not entirely sure. Nothing like this has ever happened before.”

“Then it’s settled. From now on, we can do it this way.”

“Y-Young Hero Jin, I’m sorry, but could you do it a little more normally? It’s somewhat difficult for me to make a judgment…”

“Normally?”

*I did it this way because I don’t think I can do it normally, you idiot.*

I was wondering whether I should just throw out a moderately powerful punch when—

“Bwahahaha!”

The sudden burst of laughter made everyone, myself included, turn their heads.

Norway, the massive man who stood out from the crowd, was looking at me with a mocking grin spread across his face.

“You’re desperate to stand out, aren’t you?”

I scratched my chin and answered.

“Not particularly. But why are you so desperate to pick a fight with me?”

“You?”

“Yeah. You.”

A vein bulged on Norway’s forehead.

“I heard the Fire King’s Disciple has only just passed the age of twenty.”

“I’m twenty-two. I’m all grown up.”

“I am thirty.”

“Thirty? That’s pretty close to my age. Wanna be friends?”

“How dare this fresh-faced brat…”

*Does he have a fetish for honorific speech or something?*

The supervisor tried to stop him as he glared and took a step forward.

“Control yourself!”

“To hell with self-restraint. The only person who can talk to me like that is my Master.”

I leisurely folded my arms and asked, “So, it seems that’s what you’ve been wanting to say all this time. Let’s hear who your Master is.”

“The Seafaring King.”

*The Seafaring King? Could it be…?*

I cried out in shock.

“Jang Bogo!”[^1]

“What the fuck are you talking about! My Master’s name is Pa Ryun! Seafaring King Pa Ryun!”

“Oh. Right. Of course not.”

Unlike my disappointment, the name that came from Norway’s mouth had a tremendous impact.

A stir spread among the applicants and supervisors in our group. Even the people being tested more than ten jang away began to murmur.

“Seafaring King Pa Ryun!”

“Pa Ryun, the Alliance Leader of the Yangtze River Channel League and one of the Ten Kings?”

“Then that young man must be the Iron-Water Divine Dragon. That explains why he dared to pick a fight with the Fire King’s Disciple.”

“What in the world is going on over there? There are two disciples of the Ten Kings…”

Norway—or rather, the Iron-Water Divine Dragon—snorted at the reaction.

He was probably proud to have such an impressive Master, but pride in his own abilities also showed in every one of his actions.

*Well, he really is strong enough to justify that much confidence.*

Perhaps that was only natural for a Disciple of one of the Ten Kings.

And unlike me, he seemed to have received guidance from the Seafaring King, Pa Ryun, since childhood.

I didn’t know how formidable the Yangtze River Channel League was, but there was no doubt that he had received lavish support in martial arts, elixirs, and everything else.

When I watched him with my arms folded, the Iron-Water Divine Dragon let out a quiet laugh.

“So you’re the Fire King’s Disciple? Don’t get cocky just because you come from a provincial martial family and received a mere year of instruction.”

He wasn’t exactly wrong. Shanxi Province was a remote region far from the Central Plains, and the Jin Family of Taiyuan was indeed a provincial martial family.

*That may be true, but…*

“You’re a pirate. Your Master is a pirate chief.”

“Pirate? Are you insulting the Yangtze River Channel League? We are heroes who roam the rivers and the open sea!”

“Sure. But boil that down to two syllables and you get ‘pirate,’ don’t you?”

“You insolent wretch! What kind of vile nonsense is that? The heroes of our League are worlds apart from scum like that!”

“Worlds apart? Do you guys eat those weird-looking fruits, too? The ones that make you unable to swim?”

“You son of a—!”

“You ate the Son-of-a-Bitch Fruit.”

Crack-crack-crack.

A dangerous sound came from the Iron-Water Divine Dragon’s enormous fist.

He glared at me with killing intent in his eyes and took a step forward. The supervisor hurriedly moved between us.

“Wait! If you fight here, you’ll be disqualified—!”

“Move.”

“Gasp!”

The scale of the Star-Array Grand Banquet was so enormous that every supervisor overseeing the examinations was a formidable martial artist, ranging from the upper reaches of First Rate to Peak.

The supervisor assigned to our group was at the upper reaches of First Rate, but the moment the Iron-Water Divine Dragon gripped his shoulder, the supervisor’s face turned deathly pale.

“W-What is this…”

“There’s no need to stop me. My Master gave me a strict order to win the Star-Array Grand Banquet, after all.”

“Th-Then…”

“I’m not going to fight. I’m only going to show that brat one of my moves.”

The Iron-Water Divine Dragon released the supervisor and strode toward the cliff. Without hesitation, he pushed his fist into the cliff.

Craaaack!

He shattered the solid rock and drove his arm in up to the forearm. Then he clicked his tongue as he looked at me.

“This is all you managed.”

I had known it from the moment I first saw him, but the Iron-Water Divine Dragon had trained in exceptionally advanced external martial arts.

His size and strength could not be explained simply by saying he had been born with them.

It was clearly the result of martial arts—an extremely advanced external qigong technique that had tempered his body.

“Whoa…!”

“As expected of the Iron-Water Divine Dragon!”

Exclamations poured forth at the strength worthy of being called divine.

Even an ordinary Peak master could not have done something like that without using internal energy. Yet the Iron-Water Divine Dragon had accomplished it as easily as breathing.

And he had done so while creating a hole much deeper than mine, as if to make a point.

“The Fire King’s Disciple is impressive, too, but is he still outmatched?”

“That’s understandable. He’s much younger, and it’s only been a year since the Fire King took him in as a Disciple.”

“The Sleeping Dragon of Shanxi must have been aiming for the victory himself, but… this will be difficult for him.”

Whatever the people around me whispered, there was no denying that the Iron-Water Divine Dragon was impressive.

Regardless of who his Master was, he was unquestionably a master who could boast wherever he went in the Murim.

Clap, clap, clap.

“Now that’s some strength. Congratulations on passing.”

“Pathetic. There’s no need to force yourself to pretend you’re calm.”

“I’m being sincere.”

The Iron-Water Divine Dragon snorted at my applause and turned toward the supervisor.

The supervisor was still stunned by the successive anomalies.

“Did I pass?”

“Ah. W-Well…”

“It doesn’t matter. I had no intention of stopping at this level anyway.”

Rumble-rumble-rumble.

The Iron-Water Divine Dragon pulled his arm out with absurd ease and looked around.

He read the envy, jealousy, and despair in the gazes fixed on him—gazes reserved for the strong—and bared his teeth at me.

“Brat, consider it an honor to witness the Ship-Breaking Fist.”

“The Ship-Breaking Fist?”

He did not answer.

Instead, internal energy as vast as the open sea rose in waves from the Iron-Water Divine Dragon’s entire body.

His waist, thicker than a bear’s, and his pillar-like arms bent far backward. Blue internal energy, like a flowing river, already surged around his fist.

Gooooong.

The air around us trembled.

Then—

Kkwaaaang!

The Ship-Breaking Fist.

A single punch capable of splitting a large sailing ship struck the cliff.

A deafening boom rang out, followed by a storm. People covered their faces with both arms and groaned as dirt and fragments of rock rained down.

“Gasp!”

“Urgh!”

In the midst of the chaos, I stood perfectly still and watched the scene without missing a thing.

That was why, a short while later, I fully understood the cries of astonishment that erupted after the cloud of dust settled.

*Wow…*

The cliff, a natural formation that had stood in place for countless years, stretched more than a hundred jang in both height and width.

Now, a massive hole had appeared where there had been nothing before.

No. It was more accurate to call it a small cave.

It was more than ten jang wide and tall, and its depth reached five jang.

“I-I can’t believe this.”

“This is the Seafaring King’s unique martial art…”

An unmistakable tremor passed through the crowd.

Everyone gathered here revered martial arts more than anything in the world and yearned to become stronger.

Their awe-filled gazes focused on the martial artist who had displayed martial arts they could never hope to approach.

“Haah. Haaah.”

His broad back heaved. Muscles swollen to the point of tearing rippled beneath his skin.

After taking some time to catch his breath, the Iron-Water Divine Dragon turned around with a composed expression.

A single short word slipped between his thick lips.

“What’s the result?”

Only then did the supervisor come to his senses and barely manage to force out his voice.

“P-Passed. You passed.”

“I see.”

The Iron-Water Divine Dragon raised the corners of his mouth and swept his gaze across the crowd.

The heat in his eyes had not yet faded. They stopped on my face.

“Did you see that?”

I gave a small nod.

“How was it?”

“It was impressive.”

“And?”

“Um. Congratulations on passing.”

“That’s all?”

“What else? Do you want me to pat you on the ass?”

Grind.

At the sight of the Iron-Water Divine Dragon grinding his teeth, my head instinctively shook from side to side.

*I already told him it was impressive. What more does he want?*

*What is he, a fucking child?*

Maybe it was because he was a pirate, but he was as simpleminded and ignorant as they came. The fact that he had already expended enough strength to leave himself breathless during the preliminary round was just as ridiculous.

I clicked my tongue inwardly and spoke to the supervisor.

“Let’s move things along. I think we’ve already wasted quite a bit of time.”

“Ah, yes. Understood. Then, next…”

I was turning around as the supervisor called the next name when the Iron-Water Divine Dragon spoke.

“Looking at you, I can tell what level the Fire Gate Clan is.”

“What?”

I stopped without meaning to. The Iron-Water Divine Dragon continued in a voice filled with mockery.

“Single-heir succession. No teaching to outsiders. It sounds grand, but in the end, didn’t you run away like a fucking dog with its tail between its legs to avoid me?”

“That’s your opinion.”

“Is it only my opinion?”

“What?”

I suddenly looked around.

Countless gazes surrounded the Iron-Water Divine Dragon and me.

I could read the emotions in their eyes.

*Disappointment. Contempt.*

Beep.

> **System**
>
> - People are whispering at the sight of you looking terrified!
> - People are beginning to doubt the reputation of the **Fire Gate Clan**.
> - People are beginning to doubt the reputation of **Jeok Cheongang**.
> - **Fame** decreased by 18!
> - **Fame** decreased by 20!
> - **Fame** decreased…

The System notifications pierced my ears.

At that moment, I came to my senses as if waking from a long sleep.

*So that’s how it is.*

I had forgotten for a moment.

No—I had known, but had failed to realize what it meant.

Even though the curtain had risen on the Star-Array Grand Banquet, this magnificent and dazzling stage where the martial artists of the world had gathered in one place…

*This is the Central Plains. This is the world.*

A world where everything was proven through strength alone. Winners and losers. A world divided into two kinds of people.

That was the Murim.

“Hoo.”

Seeing me heave a tremendous sigh, the Iron-Water Divine Dragon taunted me.

“Looks like you’re finally ready to give it a try.”

“Yeah. Thanks. That really woke me up.”

“I heard you’re fairly skilled with a spear. I’ll graciously permit you to…”

“You called it the Ship-Breaking Fist, right?”

“Huh?”

“That thing may be able to split a ship, but a cliff is beyond it.”

Whoosh.

With a single step, I erased a distance of five jang.

By the time my raised foot touched the ground, I had already passed the Iron-Water Divine Dragon.

A belated cry of astonishment came from behind me.

“You—!”

Instead of answering, I looked up at the cliff spread out before me.

The fire dragon sleeping in my dantian awakened and spread through every limb and bone in my body. Hundreds of acupoints grew scorching hot.

“Jin Taekyung!”

“You fucking weakling. Consider it an honor to witness the Flame-Extinguishing Divine Fist.”

Blue flames filled my vision.

[^1]: Jang Bogo was a famed ninth-century Korean maritime commander and trader.
## Chapter artifact 247

# Chapter 247

A gloomy underground gambling den. A middle-aged man sitting in a corner lowered his head.

“……I’m done for.”

A pair of glasses—an item imported from the Western Regions—rested on his nose. Until a few days ago, they would have easily cost dozens of silver nyang. But not anymore.

The lenses, which were said to magnify objects several times over, were cracked all over like a rice paddy in a drought.

Two men were watching the middle-aged man from a distance.

“Is that him? Is he really the one…?”

“That’s Kwak Cheolyung. No doubt about it.”

“Good heavens. I never thought I’d live to see one of the legendary Dogons in person.”

The two men, one with narrow, birdlike eyes and the other with a goat’s beard, were ordinary gamblers of the sort one could find anywhere.

As they watched Kwak Cheolyung deal the bone tiles again, the goat-bearded man asked, “But what happened to him?”

As his question suggested, Kwak Cheolyung was in a pitiful state.

His complexion was haggard, and his beard had gone untrimmed. His silk clothes were filthy black with grime and torn in several places.

They said he had spent his entire life roaming from one gambling table to another and amassed an enormous fortune.

But now, he looked like nothing more or less than a gambler who had lost everything.

“Did something happen?”

“It did. Something very serious.”

The narrow-eyed man nodded. Unlike the goat-bearded man, who had arrived in Henan late, he knew exactly what had happened to Kwak Cheolyung recently.

“What was it? Don’t keep me in suspense. Tell me.”

“He lost a gamble.”

“Winning and losing are common in this business, aren’t they?”

“They are. But what if it was a game worth a thousand silver nyang?”

“Gasp! A thousand silver nyang!”

The goat-bearded man’s eyes widened.

That was enough money to live in luxury for the rest of one’s life—or even enough for three generations to live like kings.

He clicked his tongue regretfully, lamenting that he had never seen such a massive game, and asked, “It must have been the biggest wager since the founding of the country. Who was his opponent? A-Gwi? Or Jjak-Gwi?”

“My friend, I knew you were hard of hearing, but you really are completely out of touch with recent news. A-Gwi had his wrist cut off by a fellow called the Qingcheng Mountain Guillotine a couple of months ago, and Jjak-Gwi disappeared a long time ago.”

“Then who besides those two could possibly have beaten Kwak Cheolyung?”

“The Sleeping Dragon of Shanxi.”

“Who?”

“Jin Taekyung of the Jin Family of Taiyuan. He’s the Fire King’s Disciple.”

The Fire King was one of the Ten Kings and a Supreme Peak master whose reputation resounded throughout the world. There was no reason for such a man’s Disciple to gamble with a Dogon.

The goat-bearded man thought for a moment before crying out as if in a groan.

“Dodo![^1] He played Dodo at the Star-Array Grand Banquet.”

“Correct.”

The Star-Array Grand Banquet’s betting games were considered the greatest gambling matches held anywhere under heaven, and were therefore called Dodo.

At last, the goat-bearded man understood what had happened and clicked his tongue.

“Tsk, tsk. Kwak Cheolyung did something stupid. The odds on the preliminaries may have been high, but he should have considered that meant they were dangerous, too.”

“Do you think he bet without thinking? He must have been confident for his own reasons.”

“What did he bet on, and against whom?”

“The Iron-Water Divine Dragon taking first place in the preliminaries.”

“I suppose he’s strong, since he’s the Seafaring King’s Disciple, but I don’t think he’s quite that good.”

The narrow-eyed man shook his head.

“He seems to have gained some insight recently. I heard one-tenth of a cliff was blown away by the Iron-Water Divine Dragon’s Ship-Breaking Fist.”

“……Is that even possible?”

He had heard rumors of Murim masters breaking apart the earth and cleaving the sky, but he had never imagined it could be to this extent.

Just as the goat-bearded man was struggling to contain his astonishment, another unbelievable statement followed.

“What’s so impossible about it? Immediately afterward, the Sleeping Dragon of Shanxi even brought the cliff down.”

“……!”

The goat-bearded man asked haltingly, his eyes as wide as plates.

“Y-You mean he collapsed a cliff?”

“That’s right. According to the witnesses, it came down with an enormous roar.”

“…….”

The goat-bearded man did not answer. Instead, he stared at his friend with distrustful eyes.

“Isn’t that just a wild rumor?”

“Everyone else, myself included, dismissed it as a wild rumor at first. A person made of flesh and blood bringing down a cliff with his bare hands—it didn’t seem possible.”

“Exactly.”

“But what can we do when it’s true? Kwak Cheolyung sitting over there is living proof.”

“Why would Kwak Cheolyung be proof…? Ah. He must have lost a thousand silver nyang.”

“Five thousand.”

“What?”

“What do you think it feels like to lose money in a game you were certain you’d win?”

“C-Could it be…?”

“Is Kwak Cheolyung any different? In the end, he’s just as crazy about gambling as anyone else.”

The narrow-eyed man looked at Kwak Cheolyung with pity.

The disheveled man was staring blankly at the tiles in his hand.

“On that day three days ago, when the Iron-Water Divine Dragon gave up on the Star-Array Grand Banquet and returned to the Yangtze, Kwak Cheolyung completely lost his mind.”

“Did he keep playing Dodo?”

The narrow-eyed man nodded.

“After the Iron-Water Divine Dragon, Kwak Cheolyung chose Jong Sam of the Hunroe Leg. He bet on him receiving the highest score in the leg-technique assessment.”

“That Supreme Peak master who was said to have no equal in kicks throughout Guangxi?”

“Yes. Though by now, he probably has quite a few equals. One of his legs was broken.”

“Don’t tell me that was the Sleeping Dragon of Shanxi, too?”

“Are you starting to understand? That’s right. The two of them got into a minor dispute and agreed to exchange one clean blow each before calling it even. But one kick from the Sleeping Dragon of Shanxi supposedly broke Jong Sam’s shin.”

“H-How?”

“I don’t know. They say he gave it a casual kick, and the shin snapped with a crunch.”

“…….”

“And even though the Hunroe Leg struck first, the Sleeping Dragon of Shanxi apparently only scratched his calf a few times before finishing the fight. After that, there was probably…”

The stories that continued to pour from the narrow-eyed man’s mouth about the Sleeping Dragon of Shanxi were nothing short of shocking.

The Kunlun Sect’s Kunlun Cloud Dragon, said to have the finest lightness technique among all the young prodigies under heaven, leaped five jang straight up from a standing position—only to fall with Jin Taekyung’s foot planted on his face.

The Beggars’ Sect’s Successor Beggar became furious when he could not close the gap between himself and Jin Taekyung during the movement-technique assessment. Unable to contain his anger, he grabbed Taekyung by the back of the neck and was beaten like a dog.

“The fifth assessment was mechanisms and formations. Everyone believed that this time, the Zhuge Clan’s Lesser Family Head would take first place, but…”

The goat-bearded man, who had been listening with a vacant expression, cut him off.

“It was the Sleeping Dragon of Shanxi again, wasn’t it?”

“You got it right.”

“But seriously, how? What kind of freak is he to be proficient in mechanisms and formations, too?”

“No. He’s just proficient in martial arts. Since the ignorant bastard didn’t know what anything was, he simply smashed his way through everything and passed.”

“…….”

“Anyway, the Sleeping Dragon of Shanxi took first place in the preliminaries, and Kwak Cheolyung, who bet on someone different every time, was left completely penniless. I heard he sank all the money he’d earned into it, then even mortgaged the estate and land where he’d planned to retire to borrow from loan sharks… Tsk, tsk.”

The narrow-eyed man looked at Kwak Cheolyung with sympathy.

In front of the legendary Dogon, who had once amassed a tremendous fortune, only a few silver nyang remained. And those were probably his entire fortune.

“Whether you earn it or lose it, it all happens in one shot. Isn’t that right?”

Only then did the goat-bearded man come to his senses and lick his parched lips.

“Five thousand silver nyang. Whoever won that must have hit the jackpot.”

“He really struck it rich. Why else would they call him the Gold-Faced Young Master?”

“The Gold-Faced Young Master? Did he bet on the Sleeping Dragon of Shanxi?”

The narrow-eyed man nodded.

“He has incredible foresight. He must have won tens of thousands of silver nyang in this Dodo alone. Why else would he go around wearing a mask made of gold?”

“Good heavens.”

“They say he’s still a young man who hasn’t even turned thirty… I suppose people who are destined for greatness really are destined for greatness.”

“Damn it. Some of us don’t even have a proper house at this age. Hoo…”

The two men let out a deep sigh.

At that moment, someone stood up with the sound of a chair scraping across the floor.

Kwak Cheolyung staggered out of the gambling den. The only thing in his hand was a few iron coins he had been given as a consolation handout.

* * *

The Star-Array Grand Banquet was a long race that lasted at least half a month and, at most, a month.

Once the three-day preliminary assessments ended, the applicants were given one day of free time. That applied to me, too.

“Ahem. Ahem!”

“Youngest! Youngest!”

“Captain! Captain!”

“……Oh, please.”

*Don’t. Don’t shout in a place this crowded. I’m already dying from all the attention, and now you’re making everyone stare even more.*

Tap-tap-tap-tap!

I hurried toward the group as quickly as I could.

As if he had been waiting for me, Jin Wikyung’s bear-like bulk came charging forward with his arms spread wide.

“Youngest! My wonderful little brother!”

Whoosh! Grab!

The moment his bear paw locked around my upper body, Hyuk Mujin grabbed the back of my hand and rubbed his cheek against it.

“Ohhh, Captain! First place in the Star-Array Grand Banquet! The pride of the Jin Family of Taiyuan! The beacon of Shanxi Province! Our Captain! My lord!”

“…….”

*Jin Wikyung is my brother, so I’ll let it slide. But what the hell is wrong with Hyuk Mujin?*

I did my best to hide my bewilderment and asked, “Are you out of your mind?”

“Yes. I’m insane! I’ve gone insane over your strength!”

“Are you seriously crazy? Let go. Aren’t you going to let go?”

Whack! Whack! Whack!

Even after I struck him three times on the crown of his head at lightning speed, Hyuk Mujin did not budge.

Tears welled up in his eyes from the pain, but he refused to let go of my hand.

“Thank you! Thank you for hitting me!”

“……Are you into that kind of thing?”

I had only heard about it. That there were people who felt pleasure from being hit.

I had wondered why he had not left even after being hit by me countless times. But now that I considered the possibility that he was one of those people, a chill ran down my spine.

“Respect-Your-Preferences Fist!”

Thump!

Hyuk Mujin, struck precisely in the temple, collapsed onto the ground.

At the same time, something that glinted brightly slipped from inside his robes and landed on the floor.

“Huh? A gold mask?”

*What is this now?*

*Is it a prop used for that kind of play?*

With a serious expression, I tucked the mask into my robes.

*That dangerous bastard Hyuk Mujin. This mask is confiscated for life.*

*Not a chance.*

As I steeled my resolve, I noticed someone I had momentarily forgotten.

“Ahem. Cough, cough!”

“Do you have a throat problem?”

Jeok Cheongang, who had been staring at a distant mountain and repeatedly clearing his throat, flinched.

“W-What nonsense are you talking about?”

“You’ve been coughing this whole time.”

“Ahem!”

Watching Jeok Cheongang act distractedly, as though he wanted to say something but could not bring himself to do it, made the corners of my mouth rise on their own.

“I did well, didn’t I?”

“……”

“I got perfect scores in all five assessments. Unanimous first place overall. At this point, that says it all, doesn’t it?”

“Ahem. Don’t get so pleased with yourself over something so minor. Anyone could do it, so don’t make a fuss.”

“I heard it was the first time in the history of the Star-Array Grand Banquet.”

“It’s only the preliminaries. Have you forgotten what this old man told you? The world is vast, and there are many masters.”

“I beat three of the Ten Dragons and Phoenixes.”

The Iron-Water Divine Dragon of the Yangtze River Channel League. The Kunlun Cloud Dragon of the Kunlun Sect. And finally, the Divine Marvel Dragon of the Zhuge Clan.

The Beggars’ Sect’s Successor Beggar was a master comparable to them, and the Hunroe Leg was a Peak master who had already made a brilliant name for himself throughout Guangxi.

Their backgrounds and specialties were all different, but the five of them now shared one thing in common.

“I beat them all.”

“That…”

For a moment, Jeok Cheongang was at a loss for words. Then he shook his head again and again.

“Pathetic weaklings.”

“I’m the strong one.”

“There you go, acting cocky again.”

“Could you just tell me I did well? I raised your honor—Old Master, no, Master—and the name of the Fire Gate Clan.”

“You still have a long way to go!”

He spoke sternly, but the corners of his mouth were twitching.

It was obvious that he was barely holding back laughter.

Even if I had not heard the Sound Transmission that Jin Wikyung sent me the next moment, I could have guessed as much.

—Don’t let it bother you too much. It seems he already went and bragged about you to the higher-ups to his heart’s content.

“Ahem!”

As if he had overheard us, Jeok Cheongang cleared his throat again at the perfect moment and spoke with an artificially stern expression.

“Do not get cocky just because you defeated a few nobodies. Compose your body and mind and prepare for the main event. Understood?”

He was right. Only the preliminaries had ended. The main event, where the true masters would reveal themselves, had not even begun.

Among those who had survived the sieve of the preliminaries, there would be quite a few masters comparable to the Ten Dragons and Phoenixes—or even stronger than them.

I had already encountered several such people while watching the preliminaries.

*The world really is vast.*

If someone had not revealed their true ability in the preliminaries, that meant they were both strong and clever.

I grinned and gave Jeok Cheongang a fist-and-palm salute.

“I’ll keep it in mind, Master.”

“That boy. Ha ha. Ahem!”

Even the wrinkled corners of Jeok Cheongang’s mouth held an unmistakable smile.

[^1]: “Dodo” is the Star-Array Grand Banquet’s term for a gambling match; the name repeats the Chinese character for “gamble” (賭賭).
## Chapter artifact 248

# Chapter 248

Hong Dao, the Dharma King, was sitting in the main hall, nodding off, when he suddenly opened his eyes.

The first thing he saw upon waking was the small back of someone standing motionless and gazing up at the Buddha statue.

“When did you get here?”

“About fifteen minutes ago, I suppose.”

“So, did you go see your proud Disciple?”

Jeok Cheongang answered in a gruff voice without turning around.

“What do you mean, Disciple? How many times do I have to tell you? He isn’t.”

“Oh, so you must be proud of him.”

“Ahem. Of course he should be able to manage at least that much. What’s so special about the Star-Array Grand Banquet’s preliminaries?”

“You never did anything like that yourself.”

“There was nothing like that in my day. Back then, even the orthodox factions fought each other, calling themselves the Southern Murim and Northern Murim.”

“That’s true.”

Hong Dao stretched. Cracks echoed from all over his body.

“Still, this is enough to make a ghost wail. I didn’t sense your presence at all. Have you gotten even stronger while I wasn’t looking?”

“Why would ghosts be crying? Buddha would be furious. The Abbot of Shaolin is dozing in the main hall like a sick chicken.”

“Don’t be so hard on me. We’re growing old together.”

Jeok Cheongang turned around and shouted.

“Who says I’m old? You should have kept up with your martial-arts training. Look at me. Don’t I look like I can stay spry for another ten years?”

Hong Dao looked Jeok Cheongang over carefully, then rolled his prayer beads between his fingers.

“Benefactor Jeok. May you be reborn in the Pure Land.”

“Look at this damn bald monk!”

Hong Dao let out a quiet laugh at his old friend’s reaction.

“I don’t know about ten years, but three years should be fine.”

“Was that the heavenly patterns or whatever telling you that?”

“Heavenly patterns? According to what this poor monk saw long ago, you should have died years ago.”

“What?”

Jeok Cheongang’s face suddenly hardened. He had read the sincerity in Hong Dao’s expression and manner.

“Why didn’t you tell me sooner?”

“Because the flow changed.”

“The flow changed?”

“The heavens are vast, yet ever-changing. Just as your star was beginning to lose its light, a Morning Star rose in the northern lands.”

“……Jin Taekyung. So it was that boy.”

“The heavenly patterns told this poor monk that a Fire King stood in the Morning Star’s path. I’ve watched for the past year, and sure enough, it proved true. Your star was brighter than ever.”

The events of the past flashed through Jeok Cheongang’s mind.

He had grown old and suffered from infirmities of old age. He had begun searching for Jangcheon, whom he had sent away long ago, to settle his final affairs before he left this world.

He intended to personally deal with his former Disciple, who might still be committing evil somewhere in the world, and entrust the Fire Gate Clan’s future to the Sword Saint of Huashan.

And then…

*I met him.*

Infirmities of old age were both the curse of passing years and an illness of the heart.

When Jeok Cheongang was about to let go of the word *life*, a hand named Jin Taekyung reached out and caught it.

That was how Jeok Cheongang changed.

The more he watched that talkative, reckless boy, the more the ember lingering in a corner of his heart came back to life.

*Longer. I want to live longer.*

To do that, he had to escape the infirmities of old age that gnawed at his mind every moment.

Over the past year, he had immersed himself more deeply in martial arts. He learned while teaching, and gained insight through contemplation.

Jin Taekyung was not the only one who had grown in the Fire Gate Cavern. Jeok Cheongang had also taken a step forward.

“Three years…”

Jeok Cheongang’s low voice echoed through the main hall.

“Before long, I’ll turn those three years into ten. No, a hundred.”

Hong Dao burst into hearty laughter.

“That’s excessive greed. How long exactly do you intend to live?”

“I don’t know. I’ll somehow keep dragging myself along and live.”

“You’d have to undergo Bone Transformation about three times.”

“Damn it. Then I’ll just have to settle for ten years. So you hang on until then, too. You still need to show that you’re going strong.”

Hong Dao silently rolled his prayer beads.

“We are already waves that have flowed past. The Spear King, who was once so robust, and the Wave King, who was more spirited than anyone, have already left this world. The others have grown old enough, too. Someone whose whereabouts are unknown may already be dead.”

The Ten Kings was the name given to the ten Supreme Peak masters who had swept across the Murim during the Great Faction War.

Some of them had withered away with the passing years. Others had died at the hands of their enemies.

Though they were called the Ten Kings, there were only eight in reality, and they were now old enough to prepare for death.

Jeok Cheongang let out a groan and shouted.

“Cut the defeatist talk! What is this gloomy nonsense?”

But Hong Dao opened his mouth with a peaceful expression.

“Unnamed. I entrusted him with the Green Jade Buddha Staff last night.”

“……!”

“By the time he finishes his preparations in Arhat Cave and comes out, he should have grown into a suitable vessel. I’ve already chosen someone to serve as Abbot until then.”

“W-What did you say?”

Jeok Cheongang found himself stammering.

The Green Jade Buddha Staff was Shaolin’s sacred treasure, handed down for a thousand years. Hong Dao had not only entrusted such a treasure to his Disciple—he had even chosen the next Abbot.

The Hong Dao before Jeok Cheongang’s eyes looked exactly like a man preparing to lay down everything and leave.

“You bald monk. Are you, by any chance…”

Jeok Cheongang let the end of his sentence trail off, but what he meant to say was easy enough to guess.

A faint smile appeared around Hong Dao’s lips.

“This poor monk intends to step down after this Star-Array Grand Banquet. If the heavens allow it, I may cling to life for another year or so. But that will be all.”

“The heavenly patterns… Did they say that?”

“I need to rest. Please leave me for now.”

“Hong Dao!”

“Amitabha.”

Hong Dao picked up a wooden fish and began striking it. At the clear sound echoing through the main hall, Jeok Cheongang fell silent. Only after a long while did he finally turn and leave.

* * *

The three days of preliminary assessments had done their job admirably.

Of the more than fifty thousand applicants, only 1 percent—barely five hundred people—had earned the right to advance to the main event.

The organizers gathered them all in one place.

Of course, I was among them.

“Look over there. It’s Jin Taekyung, the Sleeping Dragon of Shanxi.”

“What? That greenhorn? He looks younger than my youngest Junior Brother.”

“What does age matter? Martial talent is what counts. Still, he’s incredible. He reached this level after becoming the Fire King’s Disciple only a year ago…”

“For fuck’s sake. Is he supposed to have a Heavenly Martial Physique or something?”

I turned toward the voice. A man who looked to be in his early thirties flinched and quietly avoided my gaze.

He must have thought I was going to say something to him, but he had read me completely wrong.

*The kid’s got good instincts.*

The possibilities of the System were endless. My Muscles and Bones, which had once been so exceptional that Jeok Cheongang had called them a Heavenly Martial Physique, had developed even further during my training on Mount Jiuhua.

Eventually, even Jeok Cheongang had shaken his head again and again.

“Monster. How much higher are you planning to climb?”

“I have to see how far I can go.”

“If this old man had possessed even half the Muscles and Bones you have, there would have been Two Gods in the martial world by now instead of One God.”

“But you don’t have them.”

“……Add another hundred geun to the iron ball.”

I had suffered more for acting cocky, but in the end, even those experiences had helped me tremendously.

After all, effort—no, the System—never betrayed me.

The System paid out points and EXP with perfect precision, and my basic stats were absurdly high, so any martial art I used was several times more effective.

*That was how I managed to defeat three of the Ten Dragons and Phoenixes, each said to be the best in their respective fields.*

The Iron-Water Divine Dragon of the Yangtze River Channel League had even voluntarily withdrawn from the Star-Array Grand Banquet.

When I asked why he was going that far, he said that as long as I was there, he couldn’t win anyway, so he wanted to go home as quickly as possible.

I couldn’t decide whether to call him simple or smart, but he was definitely a cool guy.

On the other hand…

“Alas, the martial world’s sense of decency has fallen to the ground. How could such a frivolous and violent man gain power? Oh, heavens!”

“You bastard who’d mix rice with dog shit and eat it.”

“This is impossible. Are you saying this Young Master’s knowledge is inferior to that man’s martial arts? That cannot be. I must establish a new theory of mechanisms and formations.”

Those three were simply beyond saving.

I had been listening to their endless muttering from behind me when I spun around.

“Hey, you three idiots.”

Their muttering stopped dead at my call.

A moment later, the three idiots raised their heads sharply and expressed their anger one after another, each in his own way.

“Alas, an idiot? How vulgar.”

The Daoist wearing spotless white robes was Baek Woo, the Kunlun Cloud Dragon. I had sent him plummeting during the third assessment after stepping on his face.

I learned later that he had severe cleanliness issues and spent two shichen showering as soon as the assessment ended.

“I’ll stuff shit into your mouth, you bastard.”

Unlike Baek Woo, whose mere presence suggested cleanliness, this man reeked of piss and was a beggar to the bone.

Born and raised in the Beggars’ Sect, he had eventually risen to the position of Successor Beggar—the man who would one day lead the sect.

His name was Gung Gibang.

The so-called Beggar Prince, pure-blooded beggar, ultimate beggar.

In the fourth assessment, Gung Gibang had grabbed me by the back of the neck and been rewarded with a punch to the solar plexus.

“Idiot? Were you referring to this Young Master? If you could explain the intent behind those words—and if you happen to know the exact meaning of the word *idiot*—I would appreciate an explanation.”

The last one was Zhuge Gyun, the Divine Marvel Dragon of the Zhuge Clan.

He wore the neat clothes of a scholar and a tidy hero’s headband. Judging by his clothes alone, he looked like the most sane of the three.

That was only natural, considering he was wedged between a cleanliness-obsessed Daoist who couldn’t stand a single speck of dust on his clothes and a beggar who looked as though he would happily eat filth even if it splashed into his mouth.

But as I had guessed, he was no ordinary eccentric.

He had expressed considerable regret over losing in the mechanisms-and-formations assessment, the fifth one.

*Look at this lineup…*

A group more stacked than Manchester United’s squad under Sir Alex Ferguson.

Standing those three side by side made my breath catch and my eyes go dark. After taking a moment to steady my breathing, I opened my mouth.

“Everyone shut your mouths. Stop chattering and making a racket.”

“Alas, did you just say ‘shut your mouths’? Fellow Daoist Jin Taekyung, how can every word you speak be so vulgar?”

“A bastard who wouldn’t feel satisfied even after being rolled up in a mat, hung from a post, and beaten with a dog cudgel for forty-five days.”

“‘Shut your mouths. Stop chattering…’ Those aren’t terms commonly used in our family. I was personally curious, so could you write down some of the words you use often and give me a copy?”

“……”

I wanted to beat the crap out of all three of them.

Regretting that reality prevented me from doing so, I spoke to the three idiots.

“You three had better consider yourselves dead if we meet in a duel.”

“……!”

“……!”

“……!”

As expected, a cudgel was the best medicine for lunatics.

The three idiots had just clamped their mouths shut and begun exchanging glances when it happened.

Click. Click.

The sound of something hard striking the floor pierced everyone’s ears.

An old man soon appeared on the dais. One of his legs was a wooden prosthetic.

“Sorry for being late. As you can see, my leg’s in this state.”

He grinned, exposing yellow teeth, and introduced himself.

“Nice to meet you. I’m Song Ho, the Thousand-Faced Fox.”
## Chapter artifact 249

# Chapter 249

The Thousand-Faced Fox. A fox with a thousand faces.

I had never seen a nickname that suited someone so poorly.

The old man, Song Ho, the Thousand-Faced Fox, had a build larger than that of most burly men, while his expression was as warm and genial as the grandfather next door.

He was about as far from a fox as a person could get—in fact, he was practically the exact opposite.

*He looks like that grandpa. The one who stands in front of the chicken shop whether it rains or snows.*

Put a pair of glasses on him, and they could have been twins.

But unlike me, who was thinking such carefree thoughts, everyone around us was tense as a drawn bowstring.

Anxious faces. I could hear people swallowing nervously.

*The Thousand-Faced Fox…*

*He must not have gotten that nickname for nothing.*

Once I corrected my thinking, everything began to look different.

The aura I sensed from Song Ho was that of a Peak master—nothing more, nothing less—but there was something else.

Something that had nothing to do with martial arts. Something else that only he possessed.

*What is it?*

As I stared at Song Ho’s profile, his head suddenly turned, and our gazes met in midair.

He beckoned me over, so I took a step toward him.

“So it’s you?”

“Pardon?”

“Jin Taekyung, the Sleeping Dragon of Shanxi. I’ve heard plenty about how the Disciple of Great Hero Jeok Cheongang, the Fire King, performed exceptionally well in the preliminaries.”

Judging by the way he spoke, he seemed to have known Jeok Cheongang to some extent. I quickly bowed my head.

“Thank you.”

“And you’re also the reason there are so many more finalists in this Star-Array Grand Banquet.”

I had heard plenty of things about myself, but that was the first time I had heard anyone say that.

I tilted my head and asked, “Because of me?”

“Of course it’s because of you.”

A deep smile spread across Song Ho’s lips.

“Aren’t you the one who destroyed every mechanism and formation we had set up during the final assessment?”

“Oh.”

“Thanks to you, there must be a hundred more qualifiers. Because you destroyed the core, everyone else was able to pass much more easily.”

*That happened?*

Thinking back, it did seem like everyone had passed unusually quickly.

At the time, I had simply assumed that the locals were well versed in mechanisms and formations, unlike a foreigner like me.

“You didn’t know, judging by your expression.”

“Yeah, well. I’m completely clueless when it comes to that stuff.”

“Don’t you regret it?”

“Regret what?”

“Destroying the core of the mechanisms and formations. There could have been far fewer competitors than there are now.”

“Four hundred or five hundred. What’s the difference?”

“‘What’s the difference’…”

At my blunt response, Song Ho pointed behind me.

“That won’t be easy.”

I turned my head in the direction he pointed.

The martial artists filling the training ground—including the three idiots—were all looking at me.

There were more than five hundred of them.

Every single one was either a top-tier First Rate martial artist recognized anywhere under heaven or a Peak master.

Some were scions of prestigious families who had learned martial arts with every possible advantage. Others were wandering martial artists whose bodies were covered in scars, each one worn like a medal.

*There really are a lot of them.*

But it didn’t matter. Four hundred, five hundred, even a thousand—the answer would not change.

I looked at Song Ho and slowly opened my mouth.

“It doesn’t matter. All I have to do is win.”

“What? Ha! Hahaha!”

Damn, now that I had actually said it, I was embarrassed.

Song Ho must have loved my answer, because he threw his head back and laughed loudly. At the same time, though, I had drawn plenty of aggro.

I scratched the back of my head, which was beginning to prickle.

*Everyone was thinking the same thing anyway. Why pretend otherwise?*

Everyone had gathered at the Star-Array Grand Banquet with only one goal: victory.

In a situation like this, pretending otherwise was even more ridiculous.

“You’re an interesting young friend. Great Hero Jeok really raised quite a one.”

Song Ho patted me on the shoulder and laughed with satisfaction.

That was when a middle-aged supervisor, who had been on his way up to the dais, spotted him and stopped.

“Is that you, Sir Song? What brings you here…”

Song Ho’s hand slid from my shoulder.

“I heard the qualifiers had arrived, so I stopped by to see their faces. Aren’t they future pillars of the world?”

After looking over everyone with a satisfied expression, he turned around.

“Then this old relic will take his leave. It was a pleasure, everyone.”

“…”

I didn’t answer.

It had only lasted for the briefest moment, but I had definitely seen it.

His eyes had narrowed thinly like a fox stalking its prey, and his gaze had turned sharp.

*The Thousand-Faced Fox.*

I was beginning to understand why that genial-looking old man had been given such a nickname.

*What was he looking at?*

And who had he seen—and what had he seen in them?

That gaze had flashed past in an instant, but it had definitely not been the gaze of a Senior looking at juniors far below him.

I was quickly scanning everyone’s faces when—

“Hey! Friend!”

At first, I wondered what kind of lunatic was shouting.

One person was waving enthusiastically, his booming voice echoing through the quiet training ground.

I recognized his face from somewhere and let out a deep sigh.

*What? That bastard passed too?*

The Always-Victorious Sword, Jongni Chu.

The sight of his broad smile made my curiosity vanish in an instant.

* * *

“All qualifiers, follow me.”

I had no idea how long we walked behind the middle-aged supervisor before we arrived at a long line of carriages stretching into the distance.

“Wait. Where are we going?”

I didn’t know who had asked the question, but whoever it was had surely drawn irritated looks from everyone around him by now.

The schedule after the preliminaries had already been explained several times.

The middle-aged supervisor answered in a curt voice.

“Luoyang.”

The Star-Array Grand Banquet’s preliminaries had been held on Mount Song with outsiders barred from entering, but the main event would take place in Luoyang, and the format would be different as well.

I had heard that spectator stands had even been prepared so people could watch the duels.

That was probably why people called the main event the true beginning of the Star-Array Grand Banquet.

“Everyone, board the carriages. It isn’t a particularly long journey, so we’ll arrive soon enough.”

Clip-clop-clop!

The instant the carriage doors closed, the horses’ hooves struck the ground with force.

I gazed out the window at Mount Song receding into the distance.

Three days of beautiful memories…

I wish that had been the reason.

The truth was that I simply didn’t want to look at the faces of the idiots riding with me.

“It’s been a while. Have you been well?”

“Fuck off. Don’t talk to me.”

The first to start was Jongni Chu.

But it was too soon to relax. The war had only just begun.

“Good heavens, gentlemen. Did you hear what that Fellow Daoist just said? ‘Fuck off’! What is he, some common street thug? How vulgar and undignified…”

It was Baek Woo, the Kunlun Cloud Dragon, one of the Ten Dragons and Phoenixes.

Without taking my eyes off the window, I said, “Shut your mouth. I won’t say it twice. And this ‘Fellow Daoist’ shit—I’ll turn you into cheese crust with the Flame Divine Palm.”

“What? ‘Shit’? You were speaking to this poor Daoist?”

“Yep.”

“You seem awfully high and mighty just because you happened to get ahead of me once in lightness skills…”

“Hey, you.”

I turned my head and stared at Baek Woo.

“I told you to shut up.”

Our gazes collided in midair. A brief silence passed, and we both reached out at the same time.

No—Baek Woo was half a beat faster. He made the first move.

Whoosh! Rattle-rattle-rattle!

And then everything was over in an instant.

Baek Woo’s eyes widened as both his wrists were immobilized.

“M-Moving second, yet taking control first?”

“Where do you think you’re going, throwing the first punch, you bastard?”

What mattered in a fight was not who moved faster.

The result. Only the result mattered.

I had definitely started later than Baek Woo, but I reached my target faster. That was all there was to it.

“Your grappling technique is a mess. Did you go all-in on lightness skills?”

“H-How did you…”

“What do you mean, how? You were weaker than me, and I was stronger than you.”

I grinned at his stunned face and continued.

“Now, you have three choices. Number one: take one hard hit from the Flame Divine Palm right now.”

“…”

“Judging by your expression, you don’t like that one. Number two: take the Flame-Extinguishing Divine Fist gently. For your information, I used it to bring down a cliff. If you think your body is tougher than a cliff, give it a try.”

“D-Does that mean there is no third option?”

“‘That mean’? What’s with the formal *-so* ending? You’re using haoche.[^1] Are you from the Lower District Sect? I thought you were from the Kunlun Sect.”

Baek Woo bit down hard on his lip.

“I-I am twenty-six years old this year. I am four years older than you.”

“Oh, four years. Then do you want to take four Flame Divine Palms?”

“Gasp!”

Baek Woo shook his head vigorously.

“All right. Say it again.”

“Is there no third option, please?”

“There is. Number three: keep your mouth shut in front of me from now on.”

“I’ll take that one!”

“Good. Let’s travel in silence.”

I released Baek Woo’s wrists.

A flicker of conflict passed through his eyes, but soon his expression fell, and he lowered his head.

Unless he was exceptionally stupid and shameless, that was the obvious response.

*That takes care of one, at least.*

I looked over the rest of them one by one.

Jongni Chu stared wide-eyed at me and Baek Woo in turn.

Gung Gibang stopped scratching his thigh, while Zhuge Gyun closed the book he had been reading so intently.

“Hey. Beggars’ Sect.”

“…”

“Does this bastard only open his mouth when he’s talking about shit?”

Gung Gibang was the quietest of the three idiots. Whenever he did speak, it was usually some curse-like remark that began with dog shit, continued through cow shit, and ended with horse shit.

He was filthy beyond belief.

“Anyway, I’m giving you a choice too. The same three choices I gave him. You heard them, right?”

Gung Gibang’s matted hair bobbed up and down.

“Pick quickly. This is a hassle.”

After remaining silent for a while, Gung Gibang finally opened his mouth.

“The Beggars’ Sect’s Eighteen Dragon-Subduing Palms is one of the five greatest martial arts in the world. Even if one masters only eight-tenths of it, there are few beneath heaven who can stand against him.”

“So?”

“Unfortunately, I have only mastered fifty percent of the Eighteen Dragon-Subduing Palms.”

“…”

Gung Gibang continued with eyes shining with determination.

“Therefore, I choose number three.”

“…”

I almost smacked him on the head, but I held back. It looked like my hand would get dirty if I hit him.

“Then keep your mouth shut from now on, Gibang. And use polite speech every time.”

“G-Gibang? Polite speech?”

“Might Makes Right. Haven’t you heard of it?”

“Even so, that’s a bit much…”

“Oh, right. You’re twenty-six too, aren’t you? You’re four years older than me, so do you want to take four Flame-Extinguishing Divine Fists?”

“…”

The wavering light in Gung Gibang’s eyes slowly settled.

He clenched his fists and shook out both hands.

Swish! Clack!

With lightning-fast movements, Gung Gibang formed a fist-and-palm salute and lowered his head.

“From now on, I shall call you Jin hyung.”

“Good.”

After neatly dealing with two of them, I turned toward the last idiot.

Zhuge Gyun had closed his book and was stroking a spotless white crane-feather fan.

“Galgyun.”

“My surname is Zhuge. My given name is Gyun.”

“Fine. Galgyun. You’ve already chosen, haven’t you?”

“Choosing is difficult.”

“If you still haven’t decided after watching the two Seniors in front of you, then you’ll end up a corpse.”

Zhuge Gyun looked at me calmly.

“My honored ancestor, Zhuge Wuhou, decided to enter public service after Liu Bei’s Three Visits to the Thatched Cottage.[^2]”

“What the hell? I told you to give me a number, and this lunatic starts talking about *Romance of the Three Kingdoms*. So what am I supposed to do?”

“Three Visits to the Thatched Cottage. Since Wuhou opened his heart after three visits, this Young Master chooses option three.”

“…”

As expected of the Zhuge Clan.

Just look at the strategic buildup, dragging even his ancestor into it.

*I might have to turn that crane-feather fan into a blood-feather fan.*

Only one person remained, but Jongni Chu raised both hands as if surrendering with a sheepish laugh.

“This is frightening. I’ll keep my mouth shut the whole way.”

“Don’t keep pestering me. Understood?”

“I understand. If that is your wish, then so be it.”

I had no particular grudge against Jongni Chu, so I decided to leave it at that.

Just as I began enjoying the peace I had won after subduing the three idiots, the carriage slowed while racing along and soon came to a stop.

“We have arrived at our destination.”

I looked out the window.

Lofty walls dozens of jang high. A massive iron gate. And a signboard bathed in the gentle light of the sunset.

**Murim Alliance**

[^1]: *Haoche* is a formal speech register traditionally marked by sentence endings such as “-so.”

[^2]: “Three Visits to the Thatched Cottage” refers to Liu Bei’s repeated visits to recruit Zhuge Liang as his strategist.

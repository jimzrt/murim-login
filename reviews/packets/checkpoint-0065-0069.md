# Checkpoint Review — 65–69

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

# Chapters 65–69

## Plot

Jin Mukyung is astonished that Jin Taekyung has become a First Rate martial artist approaching the Peak realm. When Mukyung uses internal energy, he defeats Taekyung and destroys the pavilion. Taekyung and the badly injured Hyuk Mujin are taken to the Medicine King Hall, while the Jin Family mistakes the incident for an assassin’s attack and begins a pursuit for the Head Elder’s possible hidden disciple. Mujin receives public credit for protecting Taekyung, leading to speculation that he may become the next Master of the Gatekeeper Pavilion.

Mukyung reunites with Jin Wikyung after three years but remains detached and focused on training. Wikyung sends Wipeng and thirty elites south under the cover of pursuing the nonexistent assassin, while secretly preparing to summon every sect in Shanxi Province on New Year’s Day and potentially seek the Alliance Leader position. Wikyung finds no mention of Dark Heaven in the family records. Gong Yacheong continues recovering and will oversee the rebuilt Sakju Branch, with Socheon and Soyul planning to join him in six months.

While Taekyung’s residence is rebuilt, Wikyung places him and Mukyung together temporarily. Mukyung imposes rules of polite speech, silence, and obedience regarding the training hall. After Mukyung harshly beats Taekyung with his scabbard, Taekyung sincerely asks to become stronger. Mukyung agrees to rebuild his martial arts from the fundamentals through practical, real-combat training.

The System grants Taekyung the Return achievement and Returnee title, activating Login and Logout and increasing all stats by ten. It then creates the Peak-Grade Quest “[Trial? Training?],” requiring Mukyung’s recognition before the remaining cohabitation period ends. Logout is restricted, and Mukyung orders Taekyung to bring his spear for training.

## Continuity

- Jin Mukyung defeated Taekyung in their spar, destroying Taekyung’s pavilion. Taekyung survived; Hyuk Mujin remains badly injured and under treatment.
- The Jin Family is pursuing an unidentified assassin believed possibly to be the Head Elder’s hidden disciple. The assassin’s identity, sponsor, and possible connection to Song Sword Sect remain unknown.
- Jin Mukyung has begun training Taekyung harshly and intends to reconstruct his inadequate martial arts from the basics.
- The Peak-Grade Quest “[Trial? Training?]” requires Jin Mukyung’s recognition. Its reward and failure conditions remain unknown, and Logout is restricted for its duration.
- Taekyung is Level 50 with fifty unspent points and fifteen years of Internal Energy after investing fifty points in Agility. The Returnee title grants All Stats +10 and activates Login and Logout.
- Jin Wikyung plans a New Year’s Day summons for all Shanxi sects and may pursue the Alliance Leader position; whether the sects will attend and whether he will become Alliance Leader remain unresolved.
- Wipeng is traveling south with thirty Jin Family elites under the pretext of pursuing the assassin.
- Gong Yacheong will lead the rebuilt Sakju Branch; Socheon and Soyul intend to accompany him in six months. Soyul still does not know that her parents are dead.
- Mukyung has spent three years attempting to open the Ren and Du meridians.
- Hyuk Mujin’s possible promotion to Master of the Gatekeeper Pavilion remains unresolved.

## Translation Decisions

- Use **First Rate**, **Peak**, **Internal Energy**, **Medicine King Hall**, **Master of the Gatekeeper Pavilion**, and **Alliance Leader** consistently.
- Render **삼재검법** as **Three Calamities Sword Technique**.
- Use **gongcheong seokyu** for 공청석유, with a footnote explaining the rare-elixir and petroleum wordplay.
- Use **junzi** for 군자, with a footnote explaining the Confucian ideal of a morally upright gentleman.
- Retain **Hyung-nim** for Taekyung’s deferential 형님, distinct from casual **hyung**.
- Use **Sleep Mode**, **Return**, **Returnee**, **Login**, **Logout**, **Ren and Du meridians**, **Heart Demon**, and **Quest** for established System and cultivation terminology.
- Render **두 시진** as **two hours**, **권각술** as **fist-and-kicking technique**, and **인정** in the Quest mission as **recognition**.
- Retain **Asmodeus** for 아스모데우스 and **Demon King Asmodeus** for 마왕 아스모데우스.

## Durable state

{
  "active_continuity": [
    "Jin Mukyung recognizes Taekyung as a First Rate martial artist standing before the Peak realm and is astonished by his transformation over three years.",
    "Taekyung's spar with Mukyung ends with Mukyung's victory and the destruction of Taekyung's pavilion; Taekyung survives and recovers in the Medicine King Hall.",
    "Hyuk Mujin is badly injured in the incident and remains under treatment after Taekyung is discharged.",
    "The Jin Family is pursuing an unidentified assassin believed possibly to be the Head Elder's hidden disciple.",
    "Jin Mukyung reunites with Jin Wikyung after three years but remains detached and prioritizes sword training.",
    "Jin Wikyung plans to summon every sect in Shanxi Province on New Year's Day and may seek to become Alliance Leader.",
    "Wipeng leads thirty elites south under the pretext of pursuing the nonexistent assassin.",
    "Jin Wikyung searched the family's records for Dark Heaven but found no information.",
    "Gong Yacheong is recovering and will take charge of the rebuilt Sakju Branch; Socheon and Soyul will accompany him in six months.",
    "Soyul is five years old and does not know that her parents are dead.",
    "Taekyung is Level 50 with fifty remaining points and fifteen years of internal energy after investing fifty points in Agility during the duel.",
    "Taekyung's bruises largely disappear overnight after circulating his qi and sleeping, which he attributes to Sleep Mode.",
    "Jin Wikyung arranges fifteen days of temporary cohabitation between Taekyung and Jin Mukyung while Taekyung's residence is rebuilt.",
    "Jin Wikyung publicly maintains a formal image but is openly recognized within the family as excessively devoted to Taekyung.",
    "Jin Wikyung stops Taekyung and Mukyung from fighting and requires both brothers to apologize and cooperate.",
    "Mukyung imposes rules of polite speech, silence, and obedience over the training hall during the cohabitation.",
    "The Returnee title grants Taekyung All Stats +10 and activates the Login and Logout functions.",
    "Mukyung has spent three years attempting to open the Ren and Du meridians.",
    "Wipeng visits Song Sword Sect with thirty retainers, delivers Wikyung's New Year's Day summons, and implies that the summons is also a warning.",
    "Mukyung now trains Taekyung harshly, and the System has created a Peak-Grade Quest requiring Taekyung to earn Mukyung's recognition while Logout is restricted."
  ],
  "continuity_sources": [
    69,
    68
  ],
  "open_questions": [
    "The identity and sponsor of the assassin who attacked Taekyung and Hyuk Mujin remain unconfirmed.",
    "It remains unresolved whether Hyuk Mujin will actually become the next Master of the Gatekeeper Pavilion.",
    "It remains unresolved whether the Shanxi sects will answer Jin Wikyung's summons.",
    "It remains unresolved whether Jin Wikyung will become Alliance Leader.",
    "It remains unresolved whether Song Sword Sect has any connection to the attack."
  ],
  "safe_through": 69,
  "temporary_decisions": [
    "Use gongcheong seokyu for 공청석유 with a footnote explaining the elixir and petroleum pun; use junzi for 군자 with a cultural footnote.",
    "Retain Hyung-nim for 형 and 형님 in Taekyung's deferential speech; use Three Questions Gorge for 삼문협.",
    "Use Alliance Leader for 맹주 and summon for 소집 to preserve the distinction from an invitation.",
    "Retain Great Hero for 대협 and Ghost Sword for 귀검.",
    "Use Sleep Mode for 수면 모드 and Medicine King Hall Master for 약왕당주.",
    "Use Return for 귀환, Returnee for 귀환자, Ren and Du meridians for 임독양맥, and Heart Demon for 심마.",
    "Use fist-and-kicking technique for 권각술 and recognition for 인정 in the Quest mission.",
    "Render 두 시진 as two hours and 아스모데우스 as Asmodeus."
  ],
  "version": 1
}

## Reading copies

## Chapter artifact 65

# Chapter 65

Jin Mukyung wondered.

*What happened over the past three years?*

He hadn’t felt this bewildered in a long time, and with every passing moment, his bewilderment snowballed.

Whoosh!

Boom! Crash!

The air exploded. The bedroom furniture—and even the walls—shattered to pieces.

But that was all. Jin Taekyung was narrowly dodging every one of his attacks.

*He’s dodging this? That guy?*

Mukyung could hardly believe his eyes.

Jin Mukyung knew Jin Taekyung well. A scion of a martial family in name only, he was a pathetically weak man in both mind and body.

Mukyung had been willing to overlook it when they were snot-nosed children, but Taekyung’s behavior had only grown more absurd with each passing year.

*I used to wonder how someone like that could possibly be my little brother.*

Had Taekyung been fifteen? Mukyung still remembered the day he brought a chair to the training hall with perfect clarity.

“Little brother, what’s that?”

“A chair.”

“You left off the last syllable.”

“A chair, sir…”

“Why did you bring it?”

“To use during horse-stance training.”

“Ah. Because horse stance is too hard?”

That groundbreaking idea had made Jin Mukyung smack his forehead.

At the same time, he had attained enlightenment.

*Ah. Words won’t work on this one.*

“Get down.”

And so the Reformation Fist had been born.

*And now that same guy is what? The Sleeping Dragon of Shanxi?*

When Mukyung first heard the story at an inn, it was so ridiculous that he couldn’t even bring himself to snort. If the storyteller had been twenty years younger, Mukyung would have beaten him senseless.

That was also why he had gone straight to Taekyung’s room as soon as he arrived at the family.

*Has he gone so far as to fabricate rumors now?*

It was obviously the Three Calamities Sword Technique. Mukyung could already picture the whole thing.

The only thing Taekyung knew how to do was chase women. He must have decided he wanted a taste of fame and started pretending to be a Peak master.

*You’re in for it today.*

He had barged in with exactly that attitude.

But then…

*He’s different.*

Mukyung had realized it the instant he saw Taekyung.

His bones and muscles had grown larger and harder. Deep within eyes that still looked like those of a Third Rate wastrel, there was a sharp, piercing aura.

The hand they clasped afterward was rough and strong.

*Peak? No. Not yet. He’s at the upper reaches of First Rate.*

Mukyung knew because he had already walked that path himself. Jin Taekyung was still unrefined. He merely stood before the wall of the Peak realm.

That made it all the more astonishing.

*How on earth?*

Water and sunlight alone did not make everything grow. Just as a sprout needed spring to emerge, there was a proper time to learn martial arts.

Jin Taekyung had been born with a decent physique, as befitted the bloodline of the Jin Family of Taiyuan, but he had squandered those years and missed his chance.

And yet that same man had grown this much in only three years.

*Unless he’s undergone a complete transformation…*

Whoosh!

The sharp sound of splitting air shattered Jin Mukyung’s thoughts. He narrowly avoided Taekyung’s fist, his face hardening.

*He’s getting faster.*

It wasn’t his imagination. The more time passed, the faster Taekyung became.

Whoosh!

Even now.

Thud!

Jin Mukyung raised an arm to block the attack, and his feelings were nothing but bewilderment. Watching him, Jin Taekyung snickered.

“You didn’t think you could dodge that, did you? That’s why you blocked.”

“You…”

“I told you. I’m catching up.”

“What happened to you? Did you drink *gongcheong seokyu*[^1] or something?”

“Why would I drink oil? You’re completely insane.”

“…”

Jin Mukyung trembled at the first verbal abuse he had ever heard in his life.

Who was he? A youthful Peak master and a martial-arts genius! Even the scions of prestigious families throughout the Central Plains who envied him would never dare speak to him so rudely.

And yet his own younger brother, only three years apart in age, had called him a crazy bastard.

“You’re dead.”

Jin Taekyung had flinched for a moment at the ominous aura, but then he let out a quiet laugh.

“Getting pretty casual, aren’t you?”

“What?”

“Didn’t you say that if I lasted a quarter of an hour, I’d be your hyung? It’s been a quarter of an hour. Right, Mujin?”

Hyuk Mujin, crumpled in a corner and barely able to breathe, cautiously answered.

“Yes, I think it probably has.”

But when he saw Jin Mukyung glaring at him as though he meant to kill him, he answered again, nearly in tears.

“Though maybe not… Could I just go outside?”

“No.”

Jin Mukyung muttered the word in a sinister voice and drew up his internal energy.

The aura of a Peak master pressed down on the air. Cracks split the floor, and the atmosphere swelled as though it might burst.

Gr-r-rk.

The smile vanished from Jin Taekyung’s face.

“Hyung-nim. I don’t think that’s quite fair.”

In contrast, a broad smile filled Jin Mukyung’s face.

“Just keep doing what you were doing, you little bastard.”

Bang! Cra-crash!

A deafening roar.

Then, collapse.

Jin Wikyung arrived too late and dropped to his knees before the ruined pavilion.

“Youngest—!”

Rustle. Thump!

At that moment, someone emerged through the wreckage. Wearing a wind cloak, he tossed out a shapeless lump like a piece of luggage. It was impossible to tell whether it was alive or dead.

“He’s not dead yet.”

After thinking for a moment, he continued.

“One of them might be dead.”

As if answering him, a groan rose from the pile of rubble.

“Ghhhh…”

“That’s the Captain of the Gatekeepers!”

“Save him! Take him to the Medicine King Hall!”

Looking refreshed, Jin Mukyung gazed up at the sky.

“Ah. Beautiful weather.”

A rude younger brother needed a good beating now and then.

* * *

The distinctive smell of medicinal herbs stung my nose. I slowly opened my eyes.

The room had been cleaned up. A dozen or so people hurried back and forth outside the door, and Hyuk Mujin lay asleep in the bed beside mine, swathed in bandages.

*The Medicine King Hall.*

At this point, it was practically my second home. Come to think of it, I had probably woken up here more often than I had in my own pavilion.

Oh, right. The pavilion had collapsed too.

Great.

“Goddammit.”

That ignorant bastard, Jin Mukyung. Where was I supposed to sleep now?

As I stared blankly at the ceiling, something began squirming beneath my blanket.

*What the hell is this?*

I lifted the blanket, revealing a small, round, white life-form clinging tightly to my side.

A brief silence passed before I opened my mouth.

“What are you doing here?”

“Shh! Quiet! Quiet!”

It was Soyul, Socheon’s little sister. The five-year-old stared at me with the most desperate eyes in the world.

“What are you doing?”

“Be quiet!”

“Your voice is the loudest one here.”

“Shh!”

Whatever she was doing, she certainly knew how to live an interesting life.

I sighed and pulled the blanket back over us. That lasted only a moment.

Squirm, squirm.

“Pwah!”

Soyul poked her face out and huffed.

“I can’t breathe!”

Was this really the Medicine King Hall? Could just anyone wander in and out of a patient’s room while he was supposed to be resting?

“Are you sorry or not!”

She tapped my chest with her tiny hands, and her expression was surprisingly stern.

“All right. So what were you doing here?”

“Playing hide-and-seek.”

“With whom?”

“With my big brother!”

Soyul smiled sweetly.

“He’ll never dream I hid here!”

“We’ll see.”

I glanced at the closed door. I had sensed someone hovering outside for a while now. It was obvious who it was.

“Come in.”

“…”

“It’s all right. Come in.”

Only then did the door cautiously open. Looking deeply humbled, Socheon said,

“Please excuse the intrusion, Benefactor.”

At the appearance of her brother, Soyul stared at me in shock.

“You betrayed me!”

I answered with a benevolent smile.

“Life is a series of betrayals.”

“That doesn’t count! It was a dirty conspiracy!”

“Where did you learn words like that?”

At the sight of his five-year-old sister showing off such sinister vocabulary, Socheon’s face turned red.

“Yul, you mustn’t say things like that!”

“Big brother’s a whole heap too!”

“You mean he’s in on it.”

At this point, any chance of getting some rest had gone out the window.

Suppressing a sigh, I sat up.

“Urgh.”

“Benefactor, are you all right? You haven’t recovered yet…”

“It’s not that bad. I’m just bruised.”

I had been beaten a little—or rather, quite a lot—but all that had happened was that my bones ached and my entire body was covered in bruises.

Jin Mukyung must have held back because I was his only younger brother. I’d counted on that, which was why I’d acted so recklessly.

“Oh, I see. That’s a relief.”

“But how did you know? Have the rumors already spread?”

“Everyone in the family knows.”

Naturally. A two-story pavilion had collapsed early in the morning.

Curious to hear what was being said, I asked,

“So what are people saying?”

*The Sleeping Dragon of Shanxi got beaten like a dog by the Heaven Shaking Sword. Turns out he was nothing but hype.*

Surely rumors like that had spread everywhere.

*I can already see it…*

“Everyone is furious. What a treacherous scheme!”

“Huh?”

A treacherous scheme? What was he talking about? Had Jin Mukyung used poison without my knowing? Had I been poisoned?

As I searched my memory in bewilderment, Socheon ground his teeth, his face full of rage.

“If he had crossed my path, I would have torn him apart, even if it meant dying with him.”

“Thanks for caring, but isn’t that a little excessive? Calm down. Seriously, calm down.”

Jin Mukyung probably wouldn’t simply laugh that off if he heard it.

But despite my attempts to stop him, Socheon’s anger did not subside.

“How could I? The Lesser Family Head himself has proclaimed the man’s immediate execution.”

“…”

*What the hell? That’s terrifying.*

*Was this the kind of place where the second son got the death penalty for hitting his youngest brother?*

*Is this what Murim is like?*

I asked in a trembling voice.

“Did they kill him?”

Socheon shook his head regretfully.

“He escaped. The pursuit team should be tracking his trail by now.”

“Are you kidding me?”

They had even formed a pursuit team. I barely restrained the urge to split open Jin Wikyung’s and Socheon’s heads and inspect their brains.

“Was all that really necessary?”

“Pardon?”

“I mean, the guy was a little rough with me, but he didn’t seem like such a bad person.”

“He tried to harm you, Benefactor!”

“That happens. I understand.”

I had a younger sister too, so I knew how it was. Sometimes I wished Hayeon had been a younger brother. If she were some hulking bastard of a man, I could beat him half to death without worrying about social criticism or pangs of conscience.

“Look. I’m barely hurt. Spit on it, give me a day or two of rest, and I’ll be completely fine.”

Socheon’s eyes trembled violently.

“Benefactor… You are truly a *junzi*.[^2] I, Socheon, am sincerely moved.”

Thump.

This was driving me crazy.

I pressed a hand to my forehead as Socheon abruptly dropped into a full bow.

“Enough. Go tell them to call off the pursuit. No—going myself would be faster. Where’s my eldest brother?”

Socheon immediately answered.

“He should be in the office with the Second Young Master.”

“Huh?”

“Pardon?”

“No, what did you say?”

“The Lesser Family Head is in the office with the Second Young Master.”

My thoughts became tangled. I barely managed to speak.

“Then who is the pursuit team chasing?”

Socheon tilted his head.

“The assassin, of course.”

“An assassin?”

“What assassin?”

Another voice suddenly cut in. Hyuk Mujin had woken up and spoke in a tone that clearly meant *What kind of bullshit is this?*

“What is he talking about?”

I ignored Hyuk Mujin and gestured for Socheon to continue.

“For now, we suspect he may be the Head Elder’s hidden disciple. His martial arts were so formidable that if the Second Young Master hadn’t happened to arrive, you would have suffered a grave calamity… Isn’t that right?”

Hyuk Mujin’s mouth fell open at the unbelievable story.

“Are you crazy? Do you want me to tell you why I ended up like this?”

Just as the shrimp whose back had been broken in the fight between two whales was about to tell the truth, Socheon spoke up.

“Ah, I left out Warrior Hyuk. I heard that you fought bravely against the assassin.”

Hyuk Mujin’s ears perked up.

“Me? Who said that?”

“The Lesser Family Head. You distinguished yourself in battle this time, and you were badly injured while protecting the Benefactor. Everyone is envious, saying your reward will be enormous. They say you’re a shoo-in to become the next Master of the Gatekeeper Pavilion.”

“T-The next Master of the Gatekeeper Pavilion!”

“But what were you going to tell us?”

“That…”

Hyuk Mujin flinched for a moment, then continued in a resolute voice.

“About the assassin.”

“Ooooooh!”

“He was strong. Even I, the next Master of the Gatekeeper Pavilion, fought him for a hundred-odd exchanges without settling the match…”

What a bumper crop of bullshit.

[^1]: *Gongcheong seokyu* is a rare martial-arts elixir; *seokyu* is also the Korean word for petroleum.

[^2]: A *junzi* is the Confucian ideal of a morally upright and virtuous gentleman.
## Chapter artifact 66

# Chapter 66

Step. Step.

Each time the young man took a step, people hurriedly moved aside.

His sculpted, handsome features were part of it, but more than that, they were overwhelmed by the intense presence radiating from him.

He stood out even from a distance.

“Wow, he’s handsome.”

At the thoughtless remark from a maid who had joined the household the previous year, an old servant gave a quiet laugh.

“Wake up from your dream.”

“Who said anything? It’s just because I’ve never seen his face before.”

“Didn’t you see him earlier? When the Third Young Master’s pavilion collapsed?”

“With all that chaos, do you think I only saw one or two people? Still, I don’t think I’d ever forget that man, even if I’d seen him in the middle of a war. Hehe.”

“True enough. His appearance was a complete disaster back then.”

The maid thought about it for a moment, then her eyes went round.

“Oh, no way?”

“That’s right. He’s the Second Young Master. So stop dreaming nonsense and go do your work.”

Jin Mukyung ignored the whispers around him with an indifferent expression and continued walking.

When he reached the stately, traditional pavilion, the martial artists guarding the entrance opened the doors for him. The looks of awe came free of charge.

“The Lesser Family Head is waiting for you.”

“Thank you.”

The moment Jin Mukyung entered the Lesser Family Head’s office, he was greeted by the rich scent of tea—and by his older brother, Jin Wikyung, charging toward him with heavy, pounding footsteps.

“Little brother!”

Jin Wikyung spread his arms wide and pulled Jin Mukyung into a tight embrace.

For a moment, Mukyung considered dodging, but if he did, he would have to watch that hulking body whine like a child.

“I can’t breathe.”

His tone was as stiff as a wooden puppet’s.

“Is that what you say to your brother after not seeing him for three years?”

“Even if we had not seen each other for thirty years, my answer would be the same.”

“You’ve grown cold. You’ve changed so much.”

“Yes. I’m a cold-blooded man without blood or tears.”

“That’s all right. I naturally run hot.”

“……Let go.”

A short while later, the two brothers sat across from each other and began to talk.

“Sir Wipeng is nowhere to be seen.”

Wipeng, who was supposed to remain at the Lesser Family Head’s side like a shadow, was absent.

After taking a sip of tea, Jin Wikyung answered.

“I put him in charge of a pursuit team and sent him out. It’ll take at least half a month to go all the way to Three Questions Gorge and back.”

“That far?”

If Taiyuan, where the family was located, was the center of Shanxi, Three Questions Gorge was practically at its entrance and far edge. It was also a crossroads leading to Shaanxi and Henan, so even fifteen days was a tight schedule.

“It’s only a formality anyway. Aren’t you making him work too hard?”

“Why? Feeling sorry for him?”

“I didn’t expect things to get this big.”

“Neither did I. I didn’t expect you to cause such an incident the moment you arrived.”

“That’s not—”

“Mukyung.”

Unlike before, Jin Wikyung’s eyes held a light reproach. Jin Mukyung sighed.

“I didn’t intend to take it that far. At first, I only meant to exchange a few moves.”

“And then?”

“He was pretty good. I got heated and used too much force.”

“Of course you did. He wasn’t the youngest brother you remembered.”

Jin Mukyung nodded reluctantly.

He had personally exchanged blows with Jin Taekyung only an hour or two earlier. By now, he could no longer refuse to acknowledge the truth.

“Since we’re on the subject, what on earth happened?”

“The youngest?”

“Everything. The letter I received only said that the Mount Heng Sword Sect bastards were invading.”

A carrier hawk had been sent immediately after the Mount Heng Sword Sect declared war, so there had been no way for him to learn the details.

The rumors he had heard on the way to the Jin Family of Taiyuan were all he knew.

“Is it true that the Head Elder betrayed us?”

“Yes. It’s a long story.”

“How long?”

“It goes all the way back to the Great Faction War forty years ago.”

Jin Wikyung’s expression hardened as he began to speak.

“Then never mind.”

“Back then, the Head Elder… Wait, what did you say?”

“Never mind. It’s already over. What good would hearing about it do me?”

Jin Mukyung emptied his teacup in one gulp, and Jin Wikyung’s face filled with disbelief.

“You little bastard!”

It was, after all, the hidden history of the family. Jin Mukyung had always been a man who cared about nothing but martial arts, but Jin Wikyung had never imagined he could be this bad.

“You need to know! The direct line of our family—”

“The Head Elder betrayed us. Then he died. The Mount Heng Sword Sect was destroyed in the process. The Jin Family of Taiyuan was the final victor. Did I misunderstand anything?”

“No, that’s right, but…”

Jin Wikyung began to wonder which of them was the abnormal one.

Then he suddenly remembered something.

“You were the one who said you wanted to hear everything!”

“Ah, I take that back. If I listen to things that happened before I was even born, I’ll grow old and die right here. I’d rather spend that time swinging my sword one more time.”

“……”

“Then I’ll be going.”

“You’re leaving? Where?”

“To train, obviously.”

“Training? Right now?”

“I came to spar with Sir Wipeng after so long, but he’s gone. Shouldn’t I train by myself, at least?”

Jin Wikyung was speechless.

*Is that how a younger brother is supposed to act after seeing his older brother for the first time in three years?*

His heart ached with betrayal.

“Mukyung!”

Jin Mukyung answered the heartfelt call coldly.

“The tea was good. Thank you.”

He left the office without even looking back.

Jin Wikyung stared at the back of his departing younger brother, stunned.

*After everything I did to raise you…*

Both his second and youngest brothers had grown up so much. He was proud of how wonderfully they had each matured, but sometimes, moments like this still hurt.

*Yes. This is the natural order of things.*

Jin Wikyung let out a sigh that seemed to drain the earth itself, then sat down in front of his worktable.

He carefully began piecing together the unfortunate masterpiece that had been torn apart earlier: *The Birth of a Hero*.

* * *

“We haven’t found a single trace.”

“He left behind no witnesses or footprints. He’s an elusive bastard.”

At his subordinate’s report, Wipeng swallowed a bitter smile.

There had never been an assassin in the first place. Naturally, there would be no traces to find.

*I have to put on an act I was never meant to perform.*

A conversation he had shared with Jin Wikyung an hour earlier flashed through Wipeng’s mind.



*An assassin? Haven’t you made this affair too big?*

*An opportunity has presented itself. We have to use it.*

*You don’t mean the opportunity to rebuild the Third Young Master’s pavilion even more lavishly, do you?*

*Oh, that’s a good idea. Make it happen.*

*My lord!*

*I’m joking. Just joking.*

*Then what opportunity are you talking about?*



That was when the smile disappeared from his lord’s face.

*An opportunity for our family to encompass all of Shanxi Province.*

*……!*

*I spent the past five days searching through every record in the family. There was a name I needed to find. You know what it is, don’t you?*

*Dark Heaven.*

*Don’t you want to know what I found?*

*You didn’t find it.*

*Clouds are gathering. Clouds that have never shown themselves before. We need to prepare before they appear.*

*Give me your orders.*

*I’ll assign thirty elites to you. Head south immediately. The official objective is to capture or kill the assassin, but your true mission is something else.*



Wipeng unconsciously touched his chest. His fingers brushed against the thick bundle of papers Jin Wikyung had handed him.

*What is this?*

*On the coming New Year’s Day, I intend to summon every sect in Shanxi Province to our family.*



This was no invitation. It was a summons.

Wipeng was not foolish enough to misunderstand what that meant.

*Are you trying to become the Alliance Leader?*

*If necessary.*



Until recently, Shanxi Murim had appeared to the outside world as two towering peaks: the Jin Family of Taiyuan and the Mount Heng Sword Sect.

But the reality was different. Shanxi Murim was shaped like a three-legged cauldron.

*The Jin Family of Taiyuan, the Mount Heng Sword Sect, and the smaller sects.*

The Jin Family of Taiyuan held the central region, and the Mount Heng Sword Sect held the north. The south belonged to more than twenty mid-sized and small sects.

The Five Gates of Shanxi, which had vanished in the recent war, was merely the name given to the five especially powerful sects among them.

*Their alliance is strong. They may refuse to comply.*

*They might have, if this had been before the war.*



The three-legged cauldron had begun to tip.

And the Jin Family of Taiyuan had both the strength and the justification to support Shanxi Murim’s cauldron alone.

*Can you do it?*



The answer had already been decided.

Wipeng muttered in a low voice.

“I shall obey.”



At that same moment, Jin Wikyung was piecing together *The Birth of a Hero* and cursing Wipeng.

* * *

> **System**
>
> **Status Window**
>
> **Lv.50 Jin Taekyung**
>
> **Job:** First Rate martial artist
>
> **Fame:** 1,180 (+150)
>
> **Titles:** 4 (Title effects active)
>
> - **Sleeping Dragon of Shanxi** (All Stats +10, Fame +100)
>
> - **Scion of a Prestigious Family** (All Stats +5, Fame +50)
>
> - **Novice Trainee** (Training speed +10%)
>
> - **Gambler** (Combat-related stats +10% in one-on-one combat)
>
> **Strength:** 135 (+15)  
> **Stamina:** 142 (+15)  
> **Agility:** 180 (+15)  
> **Intelligence:** 25 (+15)  
> **Charm:** 25 (+15)  
> **Internal Energy:** 15 years
>
> **Remaining Points:** 50
>
> - Distribute your remaining points.

I stared at the Status Window and regretted it.

*Damn it. I spent too many points.*

While fighting Jin Mukyung, I had dumped no fewer than fifty points into Agility. The balance between my stats, which I had worked so hard to maintain, had collapsed. Naturally, it left a bitter taste in my mouth.

*I thought twenty or thirty points at most would be enough.*

The wall posed by a Peak master was high.

No—perhaps Jin Mukyung was simply stronger than I had expected. The title of genius was not something people handed out easily.

“When I lasted fifty exchanges, even the assassin looked visibly flustered. I had devoted myself to training until recently, so I was an unknown master in Shanxi—”

Smack!

“Ghk!”

Hyuk Mujin, who had been struck on the back of the head, let out a scream.

“What was that for?”

“Stop filling the kids’ heads with nonsense. Unless you want to croak.”

But Socheon was waiting for the rest of the story with shining eyes.

“I’m fine.”

“What does ‘croak’ mean? Soyul wants to croak too!”

“……You’ve still got a long time before that.”

I stroked Soyul’s head as she tugged on my sleeve and pestered me.

My connection with these little siblings had grown fairly deep. As I watched them quietly, someone suddenly came to mind.

“How is Great Hero Gong these days?”

Gong Yacheong—the middle-aged man Socheon and Soyul called their uncle.

Even now, Murim terminology felt awkward to me, but whenever I addressed Gong Yacheong, I always called him Great Hero. He was someone who deserved it.

“He’s recovering smoothly. He still has trouble moving around, though.”

“Really? That’s good to hear.”

“He said he wanted to see you before he left.”

I was about to nod without thinking when I stopped.

“Before he leaves?”

“Yes. He’ll be put in charge of the Sakju Branch, which is being rebuilt this time.”

“Then…”

“We’ve decided to go with him.”

War took many things away.

Socheon and Soyul had lost both their home and their parents in the Mount Heng Sword Sect’s attack. They could not turn back the years that had passed, but now that everything had been settled, they would return to the place steeped in precious memories.

“Thank you for everything, Benefactor.”

The sincerity in his farewell made something tickle in a corner of my chest. There was still a reality far too cruel for these young siblings to bear.

What was worse, Soyul did not even know that her parents were dead.

*She’s five…*

She was far too young to recognize and accept the present for what it was.

I suddenly recalled a memory from twenty-two years ago.

It was hazy.

“……I hope it will be that way for you, too.”

Soyul only smiled shyly at the words she did not understand.

I turned toward Socheon.

“Would it be all right if I came to see you from time to time?”

Socheon beamed as if he had been waiting for me to ask.

“You’re always welcome, Benefactor.”

Hyuk Mujin, who had been listening quietly, broke through the warm atmosphere between us.

“Then when are you leaving?”

“Half a year from now.”

“……”

*There went my touching moment. I should’ve saved it.*
## Chapter artifact 67

# Chapter 67

“Ugh, every bone in my body hurts.”

Hyuk Mujin groaned. His exposed upper body was stained dark reddish-black all over.

At the sight, the cantankerous-looking old man—the Medicine King Hall Master—clicked his tongue.

“What the hell did you do to your body?”

When he untied the bundle he had brought with him, stake-like acupuncture needles were revealed. Hyuk Mujin asked in a trembling voice:

“You’re going to stick those in me?”

“What, scared?”

“They look like they’ll hurt like hell… Please go easy, if possible.”

“Sure, why not.”

The Medicine King Hall Master answered cheerfully and took out two large needles.

“I’ll put one in the crown of your head and one in your perineum. If you die, you won’t have to worry about pain anymore.”

“……”

“Now you’re finally ready to be treated.”

After silencing Hyuk Mujin with a single sentence, the Medicine King Hall Master got to work. In the blink of an eye, dozens of large and small needles pierced Hyuk Mujin’s skin.

Thuk-thuk-thuk.

“Argh! Argh!”

“A young punk like you, making such a fuss. From the sound of that voice, you’ll be hale for another fifty years.”

Leaving Hyuk Mujin, who had turned into a porcupine, behind, the Medicine King Hall Master turned his head toward me.

“Take it off.”

“What, what?”

“Are you deaf? Take off your shirt.”

When it came to age, to hell with being the Sleeping Dragon of Shanxi or anything else. I shot a sidelong glance at the blue-glinting needles and took off my top.

Rustle.

“Hm?”

The Medicine King Hall Master’s eyes widened when he saw my body.

“What are you made of?”

His voice was filled with astonishment. It was understandable. Until yesterday, my body had been covered in bruises, but now it was clean.

*I didn’t expect this much, either.*

After sleeping through the night, most of the bruises had disappeared, and even the bones that had been aching felt fine.

*Is this the power of Sleep Mode?*

It seemed that simply sleeping now let me recover quickly from most ordinary bruises. Even the Medicine King Hall Master, who had spent years as a physician, found me fascinating and examined me for quite some time.

“Did you take an elixir during the night?”

“No. I just circulated my qi all day and slept deeply.”

“Is it the effect of the hundred-year snow ginseng? No, that’s too much…”

The Medicine King Hall Master glared at me suspiciously, as if wondering whether I had raided the medicine storeroom again, then shook his head.

“The Third Young Master may be discharged.”

Hyuk Mujin, who had been groaning, brightened.

“What about me? What about me?”

“I swear, if you run off again without permission, I’ll jab your perineum with a large needle.”

The gaunt old man muttered in a sinister voice as he raised a large needle and stabbed it through the air. He looked like something straight out of a horror movie.

*That’s going to be one bloody opening ceremony.*

“Third Young Master, get out. Unless you want to be needled.”

*Thanks…*

That was the moment I jumped to my feet to escape those eyes gleaming with madness.

A sudden flash of insight crossed my mind.

*Where am I supposed to go now?*

The pavilion had collapsed, so I had nowhere to return to. I had become homeless overnight, and was hesitating when—

“Ahem. Medicine King Hall Master, are you inside?”

A familiar voice came from outside the door. I opened it, half expecting the impossible, and saw the face I had anticipated.

“Hyung?”

Jin Wikyung jumped a beat late.

“No, what are you doing here? I came because I had something urgent to discuss with the Medicine King Hall Master during my duties. What an incredible coincidence!”

“……”

*Nice try.*

* * *

After hearing my situation, Jin Wikyung led the way with a solemn expression.

“I know of a place you can use as a residence for a while. Follow me.”

His behavior was clearly influenced by the eyes around us. The image he had built over the years was that of a cold, capable Lesser Family Head who strictly separated public and private affairs.

The problem was…

“The Lesser Family Head!”

“Isn’t that the Third Young Master beside him? What are those two doing together in broad daylight?”

“Maybe he can’t stand being apart from him for even an instant. He absolutely dotes on the Third Young Master.”

Anyone who paid attention already knew: Jin Wikyung was a complete fool for his little brother.

*Of course they did. Anyone who didn’t know would be the abnormal one.*

He was still like this in his mid-thirties. I could only imagine what he had been like when he was younger. After the battle ended, he had even been so happy that he carried me around on his shoulders.

*My youngest! My little brother!*

After making such a spectacle in front of hundreds of people, there was no way anyone could have missed it.

As I sighed inwardly, a thread of Sound Transmission slipped into my ear.

—How was that? Hyung can act, too, huh?

I nodded, thinking that if there were an Academy Award for terrible acting, he might even contend for Best Actor.

—Are you all right? Mukyung didn’t do it out of malice, so I hope you’ll understand him.

“……”

His fists had been overflowing with malice. It was only thanks to my rapid recovery that I had not spent several days staring at the Medicine King Hall ceiling.

*I should avoid running into him whenever possible.*

That kid had a nasty temper, and the martial arts to back it up. There was no dealing with him.

Jin Mukyung had shot straight up to the number-one spot on my internal watch list the moment he appeared.

“Still, see him often enough and you’ll grow fond of him.”

*See him often enough and I’ll grow black-and-blue.*

Jin Wikyung, unaware of my inner thoughts, laughed heartily and continued walking.

We passed through the bustling center of the Jin Family of Taiyuan and kept going. The farther we went, the fewer people we saw.

*Where are we now?*

The area occupied by the Jin Family of Taiyuan was enormous, a reminder of its former glory. Even from a distance, it looked as though several soccer fields had been joined together, so it was only natural that I couldn’t see everything. There were still unfamiliar places everywhere my feet took me.

*Everything’s run-down.*

Now the people had disappeared completely, leaving the road empty. The occasional pavilion and the buildings whose purposes I couldn’t identify were old and gloomy.

It had the kind of atmosphere where rats could hold a sports festival during the day and ghosts could play go-stop at night.[^1]

When I looked around, Jin Wikyung hurriedly began to explain.

“Given how things have been for our family, even maintaining this much has been more than we could manage. We’ll need to carry out extensive renovations now, of course.”

“I don’t really care.”

“Really?”

“Yes.”

I meant it.

I had lasted five whole years in a cramped, three-pyeong goshiwon studio.[^2] Rats could be dealt with, and ghosts… Well, it wasn’t as if real ghosts would actually show up.

“As long as it’s spacious, I don’t mind.”

“So, no matter what the circumstances are, you don’t care as long as it’s spacious?”

The premise sounded slightly ominous, but I nodded anyway. Jin Wikyung’s face brightened.

“That’s a relief. I was worried you might dislike it.”

“Where exactly is this place?”

“We’re here. This is the building.”

“Oh.”

We stopped in front of a large three-story pavilion. Compared to the other buildings we had passed, it was much cleaner and had a distinctly elegant, old-fashioned charm.

I also liked the tall stone wall surrounding it.

“It’s nice.”

There was no reason at all to dislike a place like this.

Jin Wikyung smiled brightly, looking pleased by my reaction.

“Do you like it?”

“Yes. It’s much cleaner than I expected. And it looks incredibly spacious.”

“That’s right. I had the training hall built large.”

“A training hall!”

“I had another one built underground in case the weather was bad.”

“Oh. Two training halls!”

“If we divide them up, there shouldn’t be any problem.”

“Whoa. If we divide them up, that’d be perfect… Huh?”

Wait. What had he just said?

“I’m not supposed to use it alone?”

“Oh, well…”

Jin Wikyung gave an awkward smile.

“It’s spacious enough for two people to use it together, isn’t it? You might grow closer while you’re at it.”

“Who?”

Unease began to creep up my spine.

And a bad premonition was never wrong.

Instead of answering, Jin Wikyung strode into the pavilion.

“Mukyung! Your big brother’s here!”

*Oh, damn it.*

* * *

“So, I’d like you to live together until your residence is rebuilt.”

After hearing the situation, Jin Mukyung readily nodded.

“Let’s do that.”

I hadn’t expected him to accept so readily.

His unexpected response surprised both me and Jin Wikyung.

“Wait, are you serious?”

“Yes. But please send one person tomorrow.”

“Of course. I was worried about you shutting yourself away in the training hall all alone anyway, so this works out well. I’ll find you a capable servant who’s quick on the uptake. Or should I hire a cook while I’m at it?”

“A servant or a cook is unnecessary.”

“Then what?”

Jin Mukyung gazed at me with deep, intent eyes.

“Please call a physician.”

“……”

“……”

The scenery I had seen on the way here suddenly rose before my eyes.

An empty street with no people around. An underground training hall where not even a scream could escape. The perfect conditions for committing a crime.

*He’s really made up his mind to beat me senseless.*

As I shivered, Jin Wikyung stammered out:

“M-Mukyung. No, that’s not it, right? It’s not what I’m thinking, right?”

“It’s exactly what you’re thinking. It might be worse.”

“If it’s worse…”

“Then you’ll need to call an undertaker instead of a physician.”

I threw myself toward the exit without delay.

Whoosh! Grab!

*Goddammit.*

Jin Wikyung caught me by the nape and dragged me back. Jin Mukyung gave a short laugh as he watched.

“What a pathetic movement technique. Even a back-alley dog would be faster than you.”

This time, I fired back without holding anything in.

“If something’s faster than me, is it really a dog? It’s Red Hare, isn’t it?”[^3]

“Even after taking that beating, you still haven’t come to your senses.”

“Hit me! Come on, hit me!”

Of course, I had no intention of actually being hit. I had a dependable protector on my side.

“Enough!”

The booming shout shook the underground training hall. Unlike before, Jin Wikyung’s face had hardened.

“What do you two think you’re doing?”

I had never seen him like this. They said it was frightening when a good person got angry, and looking at Jin Wikyung now, I understood exactly what they meant.

“Instead of getting along as brothers, you’re trying to start a fight in front of me?”

Under his fierce glare, both Jin Mukyung and I fell silent.

“It isn’t half a year or a year. It’s only fifteen days. I’m asking you to live together just until the pavilion is finished. Was that such a difficult request?”

Jin Mukyung flinched. As the one who had demolished the pavilion, he had every reason to feel guilty.

“That was because that guy was being rude…”

“And that gives you the right to demolish a pavilion and beat up your little brother? You call that an excuse?”

Jin Mukyung lowered his head.

“I’m sorry.”

This time, the arrow turned toward me.

“Taekyung, what about you?”

I wanted to whip out my ID card, but I held myself back.

This body was only twenty, and Jin Mukyung was my blood brother, three years older than me.

“Answer!”

“……I’m sorry.”

Jin Wikyung glared at us with a stern expression.

“This was a decision I reached after careful consideration. If you dislike each other that much, say so now. I’ll respect your wishes.”

Jin Mukyung and I locked eyes in midair.

Our answers came out at the same time.

“But I don’t want to.”

“I don’t want to either.”

“……”

After a heavy silence, Jin Wikyung finally managed to speak.

“I’m glad you two are willing to follow your big brother’s wishes.”

*Was that even a question? He’d already decided on the answer.*

[^1]: Go-stop is a Korean card game commonly played with hwatu cards.

[^2]: A goshiwon is a very small, inexpensive room-for-rent housing arrangement; three pyeong is roughly ten square meters.

[^3]: Red Hare is the legendary swift horse associated with the historical warlord Lü Bu.
## Chapter artifact 68

# Chapter 68

In the end, Jin Wikyung was the winner. He kept pleading with moist, puppy-dog eyes, saying, “Just half a month. No, just ten days. Can’t you two live together?” until Jin Mukyung and I threw up our hands and surrendered.

And that was how we ended up in this situation.

After Jin Wikyung left, the underground training hall was quiet with just the two of us remaining.

Jin Mukyung was the first to break the silence.

“I’ll tell you the rules.”

“Rules? What rules do two men need to live together?”

“First. From now on, you will treat me with respect and use polite speech.”

“What if I refuse?”

Jin Mukyung struck the steel training dummy standing beside him.

Boom! Crack!

The steel dummy went flying and slammed into the wall of the training hall. A distinct handprint was stamped into its caved-in chest.

“What did I say the first rule was?”

I glared at Jin Mukyung. I had been through all kinds of hardship. If he thought he could crush my spirit with something like this, he was seriously mistaken.

“You said I was to use polite speech, sir.”

…

But a mature member of society knew how to avoid unnecessary fights.

This was the adult way to fight. Heh.

*Then why do I feel like crying?*

Ah, I miss Mom.

“Good. Second. You will live as quietly as a dead mouse. If you make enough noise to wake me up or interfere with my training…”

Boom! Crack!

As the second steel dummy went flying, I nodded frantically.

“Last, the third rule. You may use the training hall freely, but if I tell you to move, you will do so without complaint. Understood?”

“Yes, yes.”

“You’re finally coming to your senses.”

Jin Mukyung nodded with satisfaction and pointed toward the exit.

“Now leave. Your room is on the third floor.”

As I hurried out of the underground training hall, the sound of someone shouting through a training exercise echoed behind me. The way he treated me like a piece of luggage made my competitive spirit flare up. I turned around for a moment and made a vow.

*Wait for me. I’ll catch up soon.*

Whoosh! Slash!

Sword Energy cleaved through the third steel dummy. As I watched its head fall limply to the floor, I slightly revised my vow.

*Wait for me. I’ll catch up someday.*

* * *

The room was bleak. Unlike my previous room, which had been decorated so lavishly that it bordered on gaudy, this one contained only a few pieces of absolutely necessary furniture.

“This is a bit much, even for him.”

Or should I say this was just like Jin Mukyung?

We had only met the day before, but that had been enough to figure out his personality. He hated anything superfluous and valued efficiency. He was also the sort of diligent person who never neglected his training.

“…”

What the hell? The more I thought about it, the more impressive the bastard seemed.

He had a violent side, beating his own little brother like a dog for failing to use polite speech, but when I thought about it carefully, that had been self-defense.

Put yourself in the other person’s shoes. Wasn’t that the basis of human relationships?

*If I had a little brother like this, I would’ve beaten him too—and then some.*

His older brothers were working their asses off to rebuild the family, while the youngest was neglecting martial arts and going crazy over alcohol and women.

Jin Wikyung only let it slide because he was a saint. Reacting with his fists like Jin Mukyung did was perfectly normal.

*And he’s strong, too.*

Who knew? Maybe seeing his younger brother reform would move him to personally teach me martial arts.

*This is an opportunity.*

My eyes lit up.

Unlike Jin Wikyung and Wipeng, whom I only occasionally saw because they were so busy, Jin Mukyung was holed up in the training hall all day.

If I received one-on-one lessons from a Peak master during the ten days we lived together, wouldn’t my martial arts improve by leaps and bounds?

*More than now. Much more.*

Greed suddenly raised its head from deep inside me.

No, this wasn’t greed. It was hunger—the hunger for everything I had never been able to possess.

Wealth and fame? I wanted them. But they were only a part of what I truly sought.

*I want to become stronger.*

I had thought I had become strong enough, but I hadn’t.

I was still woefully inadequate when it came to protecting the people who mattered to me. I had felt it when I faced Jopil, and again when I watched the Head Elder.

The overwhelming difference in power.

At my current level, protecting even my own life would be difficult, let alone the lives of the people around me. I was nothing more than a frog that had just poked its head out of a well.

*I don’t know how long it’ll take, but I’ll catch up soon enough.*

It had taken only two months to rise from Third Rate to First Rate, from F-rank to C-rank. The resolve I felt now was not empty talk.

The war was over, and I had plenty of time now. I intended to raise my abilities as much as possible before logging out.

*Should I get myself measured again as soon as I return?*

If my internal energy could support it, I thought reaching B-rank would be easy.

That was when I was smiling contentedly at the happy thoughts chasing one another through my mind.

“Huh?”

What was this?

I felt as though I had forgotten something important. As if I had overlooked something I absolutely could not afford to miss. It was the same sense of wrongness I had felt before meeting Jin Mukyung yesterday.

It did not take long to realize what that wrongness was.

“Q-Quest Window, open.”

Ding.



> **System**
>
> - There are no quests currently in progress.

There were no quests in progress?

The instant I saw the System message, my vision swayed. I knew exactly what that meant.

*…What about the Logout Quest?*

The Logout Quest—the only way to travel between Murim and reality—was nowhere to be seen.

I was staring blankly at the System message, unable to process this unexpected situation, when—

Ding.

A new window unfolded in midair to the sound of a clear chime.



> **System**
>
> - Achievement **Return** achieved!
> - Title **Returnee** acquired!
> - A new feature has been activated!

“Returnee? A new feature?”

What was this?

I hurriedly opened my Status Window, and sure enough, the word *Returnee* was sparkling brightly.

“Check Title.”

Ding.



> **System**
>
> **Item Window**
>
> **Returnee**
>
> **Description:** Leaving is easy, but returning is difficult. Your sacrifice and courage deserve praise.
>
> **Effect:** All Stats +10; **Logout** and **Login** functions activated.

At that moment—

Boom, boom, boom!

Fireworks exploded inside my head.

* * *

Jin Mukyung breathed.

He breathed through his nose and mouth—and with his entire body opened wide. The internal energy in his dantian mingled with the qi of heaven and earth flowing into him.

Whoosh.

Another name for the dantian was the qi sea—the sea of qi, the place where energy gathered and flowed. Jin Mukyung felt the waves of qi running along the tiny meridians throughout his body.

And he rejoiced.

*This is it.*

He had first picked up a sword at the age of five. It had been a wooden sword Jin Wikyung carved with clumsy hands. He had liked the rough texture, and he had liked the sound of wind scattering every time he swung it. From that day onward, he had never taken even a single day off from training.



*He’s a genius. A true genius.*

*That boy was simply born with it. Otherwise…*



Some people had admired him. Others had envied him. Their intentions had been different, but they all said the same thing.

A genius of martial arts. A born talent.

Even while people chattered about him, Jin Mukyung remained shut away in the training hall, continuing his practice. To him, training was not painful. It was the process of becoming stronger, and it was a source of joy.

Whoosh.

What escaped with his breath was not only turbid qi. Jin Mukyung exhaled the distracting thoughts in his mind along with it.

From this point on, he had to focus solely on circulating his qi.

*Can I do it today?*

It was time to face the enemy he had fought every day for the past three years.

The enemy known as the Ren and Du meridians.

Until now, he had been forced to retreat every time, but Jin Mukyung had not given up. If he won just once, he could open the Ren and Du meridians and set foot in a new realm.

*Let’s give it a try.*

Just as Jin Mukyung resolutely drew up his internal energy with all his might—

“Hoooooowuuuuuuuu!”

What was that? A Heart Demon?

The howl was chilling enough to raise goose bumps just by hearing it. It sounded like a demon laughing in delight. Jin Mukyung hurriedly tried to suppress his internal energy when the demon shouted again.

“Take off your voice and shout your underwear! Hoooooowuuuuuuuu!”

It wasn’t a demon.

There was only one person who could spout such bullshit from an off-limits pavilion.

“Jin Taekyung, you fucking—urk!”

His rising fury caused his internal energy to scatter in all directions.

* * *

“What? The Jin Family of Taiyuan?”

The Sect Leader of Song Sword Sect had just been about to lie down. It was the middle of the night, and the unexpected report from the general steward jolted the Sect Leader of Song Sword Sect wide awake.

“Are you sure?”

“How would I know? I’m not even a martial artist.”

The general steward was a former scholar who had retired to the provinces, and his response made the Sect Leader of Song Sword Sect clutch the back of his neck.

He had made the mistake of asking someone whose head contained nothing but ink and shit.

“Then how do you know they’re from the Jin Family of Taiyuan?”

“The gate guards came running and said there were people from the Jin Family of Taiyuan outside. And, uh, what was his name? They said some fellow called Wi… Wi-something asked if he could meet you.”

Wi-whatever?

The Sect Leader of Song Sword Sect swallowed.

“His name wasn’t Wipeng, was it?”

“Ah, yes. Wipeng.”

The Sect Leader nearly smashed the steward’s head with his wooden pillow.

*Ghost Sword Wipeng came here in person?*

He was the right hand of the Lesser Family Head, Jin Wikyung, and one of the core masters of the Jin Family of Taiyuan.

The visit from a Peak master who had made outstanding contributions in the recent war made the Sect Leader feel as though his soul were leaving his body.

“Wake up everyone who’s sleeping! Right now!”

This was an emergency.

Even as the Sect Leader rushed outside, all kinds of thoughts raced through his mind.

*Is this retaliation?*

Song Sword Sect was a small- to medium-sized sect in central Shanxi Province. It had fewer than fifty disciples in total, and most of them were only Second or Third Rate.

They had received various forms of assistance because of their close relationship with the Jin Family of Taiyuan, but when war had actually broken out, they had quietly withdrawn.

Perhaps this visit was only natural.

*Even so. Why did Ghost Sword come personally? At this hour?*

Though the Jin Family of Taiyuan was famous for its fairness and integrity and unlikely to do such a thing, if they had come to annihilate his sect, he had no power to stop them.

Even he, the strongest martial artist in Song Sword Sect, might not last three moves against Wipeng.

“Sect Leader!”

The moment their leader appeared, the gate guards—who had been whimpering like puppies desperate to pee—brightened.

But the Sect Leader could not share their joy.

With his face stiff, he politely clasped his hands toward the unexpected visitors.

“I am Huang, the man leading Song Sword Sect.”

At the same time, the thirty unexpected visitors wearing bamboo hats split to either side. Beneath the hazy moonlight, one man stepped forward.

“Good to meet you. I’m Wipeng.”

He was young, just as the Sect Leader had heard, and more impolite than expected.

Song Sword Sect might have been an insignificant sect, but how could he treat its Sect Leader like that?

Still, the Sect Leader did not dare show his displeasure. The rude young man was Ghost Sword, and behind him stood the name of the Jin Family of Taiyuan.

If this was the price for turning a blind eye to an ally’s crisis, then it was a bargain.

The Sect Leader licked his parched lips.

“I have heard plenty about Ghost Sword’s reputation. If you had sent word in advance, I would have come out to greet you…”

“Please do not trouble yourself, Sect Leader. I only intended to deliver a letter from the Lesser Family Head and leave.”

“A letter?”

Wipeng nodded and handed him a sealed letter. The seal of the Jin Family of Taiyuan was clearly visible in the torchlight held by one of the gate guards.

“This is…”

“An invitation. The Lesser Family Head requests that you visit our family on New Year’s Day.”

The Sect Leader of Song Sword Sect had lived in Murim for many years. He immediately understood the hidden meaning.

*What invitation?*

This was a summons, and a warning at the same time.

It was a warning that if they failed to answer the summons, they would be pushed out of the future course of Shanxi Murim.

New Year’s Day would be the day the victorious lord accepted new vassals.

*The Jin Family of Taiyuan has drawn its sword.*

After a brief silence, the Sect Leader finally spoke.

“I have wanted to meet the Lesser Family Head for some time… This will be an excellent opportunity.”

“It is an honor that you are willing to visit.”

Wipeng clasped his hands politely. The sudden change in his attitude made the Sect Leader bite his lip.

“You must be tired from your journey. Rather than standing here, why don’t you come inside and rest?”

“Thank you for the kind offer, but I think we should be leaving. There is someone we need to catch.”

“The man Great Hero Wipeng is pursuing? He must be quite the villain.”

“He is a vicious assassin. He dared to attempt to harm the Third Young Master.”

“T-The Third Young Master? Who would dare attack the Sleeping Dragon of Shanxi?”

“Well, we assume the assassin was sent by someone hostile to our family.”

“Oh dear.”

“But…”

Wipeng’s eyes flashed.

His sharp gaze swept through the interior of Song Sword Sect.

“Wouldn’t you know it, our pursuit led us all the way to Song Sword Sect.”

“T-That’s impossible. Surely there has been some misunderstanding?”

The Sect Leader’s heart dropped as he hurriedly began to make excuses, but Wipeng smiled and waved his hand.

“Haha. Of course it must be a mistake. The whole world knows that the Jin Family of Taiyuan and Song Sword Sect share a close friendship. How could that be the case?”

“…”

“Thank you for your hospitality. I’ll see you again on New Year’s Day. Hyah!”

Wipeng and his subordinates disappeared into the darkness.

The Sect Leader of Song Sword Sect remained standing in the same place for a long time.
## Chapter artifact 69

# Chapter 69

In the dead of night, while everyone else slept, Jin Wikyung awoke with a scream.

“Graaah!”

He flailed both arms with startling force, then soon realized that he had returned to reality.

The flickering lamplight and the documents covering his desk. The familiar sight of his study.

“Phew.”

After letting out a sigh of relief, Jin Wikyung rubbed the back of his neck. It was damp with cold sweat, probably because of the nightmare.

*I thought I was going to die.*

It had been a dream in which the earth split apart and the sky collapsed. He had run from a deafening roar that shook heaven and earth until he was gasping for breath, and his last memory was of falling.

*Maybe I’ve been pushing myself too hard.*

There was more work than he could handle, but nowhere near enough people to do it. Each day was a nerve-racking struggle, and the fatigue kept piling up.

“Ugh. I need to hire more people soon. At this rate, I’ll die before my time.”

The world was vast, and there were plenty of talented people in it. And yet the Jin Family of Taiyuan still did not have a single decent strategist. That was because the family’s capabilities were lacking.

Why would any talented person choose to join the Jin Family of Taiyuan in Shanxi when they could go to one of the great sects or renowned clans of the Central Plains, where people would welcome them with open arms?

From their perspective, it was an obvious choice.

*Until now, that is.*

Everything was about to change. If the Jin Family united Shanxi Murim on New Year’s Day and continued expanding its influence…

Before long, talented people from across the land would come flocking beneath the Jin Family of Taiyuan’s banner.

*Although I’ll probably die of overwork before then.*

Jin Wikyung let out a deep sigh as he stared at the terrifying mountain of paperwork.

That was when it happened.

Rumble.

It was an extremely faint sound, so quiet that only a Peak master like Jin Wikyung could have noticed it.

*What was that?*

He sharpened his senses. When he focused his internal energy on his ears, the sound became clearer.

Rumble. Clang.

Small, but unmistakable.

The sound of steel striking steel.

Someone was fighting. At this hour of the night, no less.

That was not the only reason Jin Wikyung’s face hardened.

*That direction is…*

It was where Jin Mukyung’s residence was located. And, as of yesterday, there was one more person living there.

*Surely Mukyung isn’t beating up the youngest… No, of course not.*

He had repeatedly urged them to get along. Surely they would not already be beating each other senseless.

He trusted his beloved younger brothers.

Clang. Clang!

“…”

Jin Wikyung quietly rose from his seat.

* * *

Once he fully unleashed his movement technique, Jin Wikyung reached Jin Mukyung’s residence in no time.

The problem was that the closer he got, the more ominous the sounds became.

*…He’s probably training alone in the training hall, right?*

Jin Wikyung hesitated over whether he should enter the pavilion. In the end, he cautiously poked his head over the wall.

And witnessed a shocking sight.

“I told you. Rule number two. Huh?”

Boom! Crash!

Jin Mukyung swung his scabbard without pause. One person fled desperately, trying to escape him.

“Lo, Logout!”

Before Jin Taekyung could even finish his desperate cry, the scabbard flew toward him. It narrowly missed him and smashed into the bluestone floor of the training hall.

Bang!

“I told you, you bastard—qi deviation! Ren and Du meridians!”

“Logouuuut!”

“…”

What was “Loguawk,” and why were qi deviation and the Ren and Du meridians suddenly coming up?

The flow of the conversation made absolutely no sense, but one thing was certain.

*Something bad is going to happen if this keeps up.*

At this rate, they might really need to call either a physician or an undertaker.

*I’ll protect the youngest!*

Jin Wikyung was just about to charge in with determination on his face when—

“Why is your side open again? Are you that desperate to get hit?”

Whack!

“Guh!”

Jin Taekyung staggered after taking a blow to the ribs. Jin Mukyung did not miss the opportunity and followed up with another swing of his scabbard.

Thwack-thwack-thwack!

“Argh! Argh! Argh!”

“Don’t shrink back just because you got hit. Especially with your lower body!”

Thwack!

“Grrr!”

“Oh, look at you.”

Jin Mukyung smiled disdainfully at the sight of his younger brother charging at him with his teeth clenched.

“You’re an idiot who doesn’t even have the basics down. Fix that habit of throwing out your hands and feet on instinct first. Martial arts are learned by people, not beasts.”

“Shut up!”

“You have a terrible memory, too. Sleep well. When you wake up, I’ll explain the rules again.”

Whoosh! Thud.

Jin Taekyung took a direct hit to the chin, and his body crumpled. Jin Mukyung silently looked down at him lying spread-eagled on the floor, then slowly spoke.

“Please come out.”

There was no question who he was speaking to. Jin Wikyung emerged from behind the wall with an awkward expression.

“You knew I was here?”

“It would be strange if I didn’t. Every time that kid got hit, I could hear you swallowing from here like thunder.”

Jin Wikyung examined Jin Taekyung’s fallen body with worried eyes.

“The injuries aren’t too severe. That’s a relief.”

“It’s not like he’s going to die.”

“Mukyung!”

“Don’t worry. His bones and sinews are unbelievably sturdy.”

“Really?”

“He lasted four hours while taking a beating like that. With that kind of stamina and grit, he’ll soon… Why are you laughing?”

Jin Wikyung gazed at his younger brother’s face with a strange smile and answered cheerfully.

“It’s fascinating. Isn’t this the first time you’ve ever praised the youngest?”

Jin Mukyung stiffened.

*Praise? I praised that bastard?*

It was impossible. Wasn’t he a younger brother without a single redeeming quality? Jin Mukyung had praised the man who had spent his days drowning in alcohol and chasing women, heedless of what happened to the family?

Jin Mukyung forced himself to shake his head.

“…I have never done such a thing.”

“I see.”

“I really haven’t.”

“All right. Who said otherwise?”

“No, you’re still laughing!”

“I have never done that.”

“Hyung!”

Jin Wikyung tried to suppress the laughter welling up inside him. It pained him to see his beloved youngest brother hurt, but this was something he would have to experience someday.

*I can’t keep him under my wing forever.*

Sleeping Dragon of Shanxi.

Another genius produced by the Jin Family of Taiyuan.

Jin Wikyung felt both joy and unease as he looked at his younger brother, who had grown so much in such a short time.

No. Perhaps it was fear.

*Is this even possible?*

It was far too fast. Even to someone who had watched the genius Jin Mukyung from closer than anyone else, Jin Taekyung’s rate of growth was beyond comprehension.

*I can’t even begin to gauge it.*

As a child, Jin Wikyung had been a promising talent, but he had never been a genius. How could an ordinary man like him understand a genius, let alone teach one?

His thoughts were growing deeper when Jin Mukyung returned.

Jin Wikyung had known at once that this was the moment, and put the two of them together.

*I was so worried because they got along so poorly…*

Now that he had seen them together, those worries had been pointless. The method was rough, but this was clearly not one-sided beating. It was training.

Training that would make the fast-growing but still inexperienced Jin Taekyung stronger and sharper.

His body would suffer, though.

*It’s all for your sake.*

Jin Wikyung looked down at the fallen youngest with boundless tenderness and spoke.

“I’ll be going now.”

But Jin Mukyung was not about to let him leave like that.

“Where are you going alone? Take that kid with you. I can’t live with him.”

“It’s ten days. Can’t you endure that much?”

“I stopped at this much today out of respect for you. If you insist, call an undertaker tomorrow.”

“Are you serious?”

“Yes. So taking him with you right now would be better for him, too.”

“If that is truly what you want…”

Jin Wikyung nodded and continued.

“Then do so.”

“Yes, yes?”

“Do as you wish.”

After tossing out that one sentence, Jin Wikyung turned and began walking away.

Imagining what expression Jin Mukyung must be wearing, he let out a quiet laugh.

*This will be good experience for you, too.*

This uncomfortable arrangement was not only for the youngest.

Geniuses were always lonely. Jin Wikyung had no doubt that the two geniuses would greatly spur each other on.

“Get up, you bastard!”

Whack!

“…”

Jin Wikyung had to suppress the urge to look back the entire way home.

* * *

“Are you awake?”

“…”

“I know you’re awake. Answer me.”

“…”

“I’ll give you one last chance. If you’re not up by the time I count to three, this training hall will be your grave.”

“…”

“One, two.”

*Bastard. He counts ridiculously fast.*

I quietly got up and stretched.

“Whew, I slept well.”

I casually turned my head and found Jin Mukyung glaring at me.

The moment I saw that face, yesterday’s memories came flooding back.

A man without blood or tears. A bastard who deserved to be beaten to death.

I addressed him in a nonchalant voice.

“Oh? Hyung-nim. When did you get here?”

“…Just now.”

Seeing Jin Mukyung smack his lips with disappointment, I decided that switching to formal speech had been a stroke of genius. If he found even one thing to nitpick, he was the type to beat me like a dog.

*Fuck… Being weak is a sin. A sin.*

I had my pride, too. But in an unarmed fight, I could not beat Jin Mukyung even if I died and came back to life.

While that bastard had been learning systematic fist and kicking techniques, I had been watching UFC matches. He was not someone I could overcome through sheer stubbornness.

That was why I had chosen Logout as a last resort.

Of course, it had failed spectacularly.

*You can’t Logout during combat? What kind of ridiculous rule is that?*

They could have told me beforehand. I had charged in without knowing and nearly logged out of life.

I cast a sidelong glance at Jin Mukyung.

“Hey.”

“Yes?”

“Why are you looking at me like that?”

“Me?”

At his icy tone, I made my eyes look as bright and innocent as possible.

Now I even had to watch how I looked at him if I wanted one less beating.

“You… Hah. Be careful.”

“Yes, Hyung-nim.”

Jin Mukyung looked displeased by my sudden politeness. But he could hardly hit me just for having good manners.

“About yesterday…”

I quickly bowed my head.

“It was my fault. I was making so much noise while you were training. I deserved to get hit.”

“No, hey.”

“Oh, no. Your hand must hurt from hitting me yesterday. Would you like me to blow on it?”

“You’re completely insane.”

Jin Mukyung looked as though he was debating whether to hit me, but eventually gave up and lowered his fist.

“Enough. Follow me.”

“…Where?”

“The training hall.”

Retract what I said earlier. He planned to beat me in the training hall.

There was no way he could turn my room into a wasteland again, after all.

Seeing my expression stiffen, Jin Mukyung clicked his tongue.

“It’s not that. Follow me. Training starts today.”

“Training?”

“Yes. I’ll tear apart your horrible martial arts and rebuild them from the beginning.”

The man who had beaten me senseless every time he saw me was suddenly offering to help me train? And he was even carving out time from his own schedule?

*I’d sooner believe that the Demon King Asmodeus had repented.*

Perhaps he noticed the suspicion in my eyes, because Jin Mukyung let out a deep sigh.

“Hyung came by yesterday.”

“Ah.”

His personality might have been foul, but he had a clear sense of rank and propriety. If Jin Wikyung had personally asked him, the current situation made sense.

“There are several empty buildings. Why do you think he sent you to me? Damn it. I should have refused from the beginning.”

…I suppose he really did not want to teach me.

But I desperately needed his help. If nothing else, there had to be some use for learning even one decent fist-and-kicking technique from him.

“Please teach me.”

Jin Mukyung shook his head.

“Think before you speak. Meeting my standards will be difficult. If you’re going to give up as soon as things become hard, quit now.”

If I had given up every time things became difficult, I would never have made it this far.

“I want to become stronger.”

Perhaps he sensed the sincerity in my voice. After staring at me for a long time, he finally opened his mouth.

“Come out to the training hall.”

Ding.



> **System**
>
> **Quest**
>
> **Trial? Training?**
>
> Train under Jin Mukyung’s guidance for the designated period. No matter how strong you become, the Quest will fail if Jin Mukyung is not satisfied!
>
> **Grade:** Peak
>
> **Restriction:** Jin Taekyung
>
> **Mission:** Jin Mukyung’s recognition (Incomplete)
>
> **Reward:** ???
>
> **Failure:** ???
>
> **Time Remaining:** 9 days 23 hours 51 minutes 10 seconds

*Jin Mukyung’s recognition.*

It was an abstract mission, but I was confident enough. If I combined the System’s cheat-like advantages with my own effort, I could grow so quickly that Jin Mukyung’s eyes would pop out.

*I can do this.*

That was when I was steeling my resolve.

“Oh, right. You use a spear, don’t you?”

“Ah, yes.”

“Bring that with you, too.”

Jin Mukyung was a swordsman. Naturally, I had assumed he would primarily teach me fist techniques. Puzzled, I cautiously asked:

“Why the spear all of a sudden…?”

“Train as if it were real combat. Haven’t you heard that saying?”

Jin Mukyung smiled brightly and added:

“I even got Hyung’s permission. He said he doesn’t mind if we have to call an undertaker.”

I stared blankly at his back as he walked away with light, cheerful steps. At last, I managed to open my mouth.

“…Logout.”

Beep.



> **System**
>
> - Logout is restricted during this Quest.

*Fuck.*

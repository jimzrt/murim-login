# Checkpoint Review — 165–169

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

# Chapters 165–169

## Plot

Jin Taekyung travels with Hyuk Mujin and Cheongpung to meet Jang Taebo, the retired former Guild Leader of the Ironcraft Guild and one of the world's greatest smiths. Jang initially refuses to forge Taekyung's Ten-Thousand-Year Cold Iron and demands the Herb of Eternal Youth, then adds gongcheong seokyu, a dragon's claw, and a dragon pearl. Taekyung rejects the resulting *In Search of the Herb of Eternal Youth* Quest and nearly gives up when Jang threatens to pressure the Nine Sects and One Gang against the Jin Family. However, after seeing Taekyung's enormous supply of Ten-Thousand-Year Cold Iron, Jang agrees to personally forge his spear. The *Find the Master Artisan* Quest is completed, and a linked Quest is generated.

Meanwhile, more than four hundred Heavenly Wind Band mounted bandits head south from Datong to attack and plunder the Jin Family of Taiyuan. An unidentified old man annihilates them with Scorching Yang Qi. The Datong Branches of the Jin Family and the Lower District Sect identify the attacker as a merciless Supreme Peak master. The old man then meets a woodcutter named Jang-pal, accepts his rice ball, and travels toward Jang Family Village on a wooden carrying frame.

## Continuity

- Jin Taekyung is a Level 71 Peak Master with forty-five years of internal energy and seventy unassigned Stat Points.
- Jang Taebo is over eighty, has lived anonymously near Jeongyang for more than ten years, and spent a full jiazi as a smith. He is the retired former Guild Leader of the Ironcraft Guild; his disciple is the current Guild Leader.
- Jang Taebo has agreed to personally forge Taekyung's Ten-Thousand-Year Cold Iron into a spear. The linked Quest generated after *Find the Master Artisan* remains unresolved.
- Jang Taebo receives a Fifty-Year-Old He Shou Wu from the Nine-Room Escort Bureau every four months, and its leader owes him a favor.
- Taekyung promised to keep Jang Taebo's residence secret and will need to explain the matter to Jin Wikyung.
- Taekyung rejected *In Search of the Herb of Eternal Youth*. Jang's additional demands are gongcheong seokyu, a dragon's claw, and a dragon pearl.
- The Datong Branches of the Jin Family of Taiyuan and the Lower District Sect were established about one month ago and had tracked the Heavenly Wind Band for nearly half a month.
- The unnamed old man killed more than four hundred Heavenly Wind Band bandits with Scorching Yang Qi. The surviving Band Leader described him as a demonic old man rising from a pit of fire before dying nearly two days later.
- The unnamed old man is a senile Supreme Peak master nearing one hundred years old, searching for an unidentified Peak master skilled mainly in sword and palm techniques. His periods of unconsciousness are growing longer.
- The old man met the woodcutter Jang-pal on an unnamed mountain, accepted his rice ball, and is being carried toward Jang Family Village.
- Taekyung still seeks information about the Fire King before deciding whether to learn the Flame Divine Palm. Wipeng has recognized that Taekyung crossed the wall and reported unusual bandit activity near Datong.

## Translation Decisions

- Render **철기방** as “Ironcraft Guild,” **철기방주** as “Guild Leader of the Ironcraft Guild,” **장태보** as “Jang Taebo,” and **장 노인** as “Old Man Jang.”
- Render **하수오** as “He Shou Wu,” **오십 년 묵은 하수오** as “Fifty-Year-Old He Shou Wu,” **불로초** as “Herb of Eternal Youth,” and **불로초를 찾아서** as “In Search of the Herb of Eternal Youth.”
- Render **공청석유** as “gongcheong seokyu,” **용의 발톱** as “dragon's claw,” **여의주** as “dragon pearl,” and **신병이기** as “divine weapon.”
- Retain “Peak Master,” “Supreme Peak master,” “Scorching Yang Qi,” “Samadhi True Fire,” “Ten-Thousand-Year Cold Iron,” “Find the Master Artisan,” “Heavenly Wind Band,” “Jang-pal,” and “Jang Family Village.”
- Preserve Jang Taebo's curt, cantankerous voice, the unnamed old man's gruff senility, and Jang-pal's plain, deferential speech.

## Durable state

{
  "active_continuity": [
    "The unnamed old man is a Supreme Peak master nearing one hundred years old whose old age causes increasingly long periods of unconsciousness; he delayed its effects for roughly twenty years with two jiazi of internal energy and can use Samadhi True Fire and overwhelmingly potent Scorching Yang Qi.",
    "The old man is searching for an unidentified Peak master who mainly uses a sword and palm techniques; Black Sand attempted to manipulate his senility to obtain his martial arts, but the old man killed Black Sand with a single palm while Chinggen and Temur survived.",
    "The old man left the Northern Gaoyuan for Datong on the Shanxi–Gaoyuan border and said he would return in about a month.",
    "Jin Taekyung is a Level 71 Peak Master with forty-five years of internal energy and seventy unassigned stat points.",
    "Taekyung completed the Find the Master Artisan Quest after Jang Taebo agreed to personally forge his Ten-Thousand-Year Cold Iron into a spear; a linked Quest was generated.",
    "Jang Taebo is the retired former Guild Leader of the Ironcraft Guild and a renowned smith over eighty years old who spent a full jiazi at the forge.",
    "Jang Taebo has lived anonymously near Jeongyang for more than ten years, refuses commissions, and now agrees to personally forge Taekyung's weapon after seeing his enormous supply of Ten-Thousand-Year Cold Iron.",
    "Jang Taebo receives a fifty-year-old He Shou Wu from the Nine-Room Escort Bureau every four months; its leader owes him a favor.",
    "The current Guild Leader of the Ironcraft Guild is Jang Taebo's disciple, learned by watching Jang Taebo work, and the guild has close ties to the Nine Sects and One Gang.",
    "Taekyung seeks information about the Fire King and will consult Jin Wikyung before deciding whether to learn the Flame Divine Palm.",
    "Hyuk Mujin knows that Taekyung obtained the Flame Divine Palm martial arts manual after the Eight Spring Gorge battle and once offered it to him.",
    "Wipeng has recognized that Taekyung crossed the wall and reached the Peak realm.",
    "Wipeng reported unusual mounted-bandit activity near Datong.",
    "More than four hundred Heavenly Wind Band mounted bandits led by an unnamed giant turned south to attack and plunder the Jin Family of Taiyuan before an unidentified old man confronted them.",
    "Cheongpung joined Taekyung and Mujin on the journey to Jeongyang and has never seen a blacksmith before.",
    "Hanga is a local boy living near Jang Taebo and Jang Taebo's only conversational companion.",
    "The System generated In Search of the Herb of Eternal Youth after Jang Taebo named the Herb of Eternal Youth, and Taekyung rejected it.",
    "The Datong Branches of the Jin Family of Taiyuan and the Lower District Sect were established about one month ago and had tracked the Heavenly Wind Band for nearly half a month before finding its annihilated force.",
    "The unnamed old man annihilated the Heavenly Wind Band, primarily using Scorching Yang Qi; the Heavenly Wind Band Leader survived nearly two days, identified the attacker as an old man, and then died.",
    "The old man met the woodcutter Jang-pal on an unnamed mountain, accepted his rice ball, and is being carried toward Jang Family Village."
  ],
  "continuity_sources": [
    169
  ],
  "open_questions": [
    "Who is the unnamed Supreme Peak master, and what is his relationship to the Peak master he seeks?",
    "Who is the unidentified Peak master being sought, and where is that person?",
    "Where can Taekyung find the Herb of Eternal Youth?",
    "Is the Fire King alive or dead, and where can he be found?",
    "Who is the unnamed giant leading the Heavenly Wind Band?",
    "Who is the unidentified old man who confronted and annihilated the Heavenly Wind Band?",
    "What is the linked Quest generated after Find the Master Artisan?"
  ],
  "safe_through": 169,
  "temporary_decisions": [
    "Render 삼매진화 as “Samadhi True Fire.”",
    "Render 정기신 as “essence, qi, and spirit,” 백염 as “white flames,” and 입신지경 as “a transcendent realm.”",
    "Render 어르신 as “elder” and 형님 as “big brother” when Black Sand addresses the old man, preserving the old man's rejection of both forms.",
    "Render 명장 as “Master Artisan,” 장인을 찾아라 as “Find the Master Artisan,” 가공되지 않은 만년한철 as “Unprocessed Ten-Thousand-Year Cold Iron,” 하수오 as “He Shou Wu,” and 오십 년 묵은 하수오 as “Fifty-Year-Old He Shou Wu.”",
    "Render 철기방 as “Ironcraft Guild” and 철기방주 as “Guild Leader of the Ironcraft Guild.”",
    "Render 오향장육 as “five-spice pork,” 집성촌 as “clan village,” 야장 as “smith,” 항아 as “Hanga,” 여의주 as “dragon pearl,” and 신병이기 as “divine weapon.”",
    "Render 구방표국 as “Nine-Room Escort Bureau,” 영초 as “Spirit Herb,” 불로초 as “Herb of Eternal Youth,” 불로초를 찾아서 as “In Search of the Herb of Eternal Youth,” and 공청석유, 용의 발톱, 여의주 구하기 as “Get Gongcheong Seokyu, a Dragon’s Claw, and a Dragon Pearl.”",
    "Render 천풍 as “Heavenly Wind,” 장팔 as “Jang-pal,” 장가촌 as “Jang Family Village,” 홍가촌 as “Hong Family Village,” and 신령님 as “Mountain Spirit.”"
  ],
  "version": 1
}

## Reading copies

## Chapter artifact 165

# Chapter 165

Knock, knock, knock.

The information I had asked Jin Wikyung for arrived faster than expected.

What surprised me was the identity of the errand runner.

“Eh? What brings you here?”

“My lord said there was a letter he needed delivered, so I came.”

“Personally?”

The person who had come to deliver Jin Wikyung’s letter was none other than Wipeng.

After silently staring at me for a while, he tossed out a single remark.

“So it was true. You really crossed the wall.”

From a low hill, one could not know what lay atop a high peak. But someone standing on that peak could see everything beneath their feet.

The same was true of Wipeng now.

As an outstanding Peak master, he noticed the change in me at a glance. He looked at me with an expression mingling awe and disbelief.

“How is such a thing possible?”

“Uh…”

What was I supposed to say to that?

Most people believed the ridiculous rumors about me without question, but Wipeng was different.

Along with the brothers of the Jin Family of Taiyuan, he was one of the very few people who knew the truth.

*It really is impossible to explain.*

A Third Rate thug had become a Peak master in only two or three months.

Even for someone with an open mind, that was an incomprehensible realm. Perhaps that was also why people believed the rumors.

*Because the rumors are more believable.*

When I hesitated, unable to answer, Wipeng waved his hand. He was probably also conscious of Hyuk Mujin’s ears nearby.

“It would be best to postpone that discussion until later.”

Still looking troubled, Wipeng pulled a letter from inside his robes. It contained the information I had asked Jin Wikyung for earlier.

As soon as I accepted the letter and unfolded it, Wipeng began explaining.

“His name is Jang Taebo. Until more than a decade ago, he belonged to the Ironcraft Guild.”

“The Ironcraft Guild?”

“It is a guild located in Hubei. Most of its members are not martial artists, but skilled craftsmen.”

In other words, it was a blacksmiths’ Guild.

I asked about the most important thing.

“How skilled is he?”

“He was the Guild Leader of the Ironcraft Guild.”

“Oh.”

That brief answer was enough.

If he had risen to become Guild Leader in the Ironcraft Guild, which was packed with skilled craftsmen, then he was practically a Master Artisan already.

I carefully read through the letter containing information about Jang Taebo.

“His home is fairly close, too?”

“A village near Jeongyang. Do you remember? The place where we received Prince Shangshan’s invitation…”

“Oh, that place.”

Was it about fifteen days ago? That was where I had marched alongside the Jin Family of Taiyuan’s elites like a victorious general.

Hyuk Mujin, who had been quietly listening beside us, spoke up.

“If we don’t slacken the reins, we should arrive around sunset.”

“Right?”

“Yes.”

“But what are you doing?”

“What do you mean?”

“Go get ready to leave. Set aside two strong horses, and pack some food for the road.”

“Wait, what… Am I a servant?”

“There’s no high or low in honest work. Are you looking down on servants now? Should I call every servant in the Jin Family of Taiyuan and give you a lecture?”

“Oh, fine! I get it, so stop already!”

Unable to withstand my nagging, Hyuk Mujin grumbled as he left the room. Wipeng clicked his tongue.

“Your subordinate’s attitude is extremely insolent.”

“…”

Well, from where I was standing, you weren’t exactly harmless yourself.

The way you constantly hounded people to work whenever you had the chance was enough to make even a mother-in-law slap someone across the face with a bundle of kimchi.

*Look at the hypocrisy.*

Of course, Wipeng had no idea what I was thinking. He continued,

“In any case, you must return by noon tomorrow at the latest. You haven’t forgotten that New Year’s Day is in two days, have you?”

“Ah, yes.”

The entire Jin Family of Taiyuan was already in an uproar because of it. The sight of servants and maids rushing around in a frenzy had become so familiar that I was nearly used to it.

That was only natural. This was a grand banquet that would last at least three days, not something that would end in a single day.

*It really is a major event.*

It was an occasion to reaffirm that the Jin Family of Taiyuan was the ruler of Shanxi Province.

With so many people arriving, everyone in the family was working day and night to ensure that nothing went wrong.

Everyone except me, of course.

“Do you really think I’ll be late? It’s only half a day away at most.”

Wipeng’s eyes narrowed.

“It is an important matter, so I trust you will conduct yourself appropriately.”

“Your eyes say you don’t trust me at all.”

“That is a misunderstanding. A misunderstanding.”

“I’m only going to make one request and come right back, so don’t worry.”

“Looking at the Third Young Master’s record so far, I cannot help but worry.”

“…”

Since trouble and accidents never seemed to stop wherever I went, he wasn’t entirely wrong.

But I was a full-fledged Peak master now. I was far too grown-up to be treated like a young child left by the water’s edge.

“Even if I look like this—”

“I trust you were not about to say, ‘I’m a Peak master now, so stop treating me like a child beside the water.’”

Was he a ghost or something? I hurriedly swallowed the rest of my words.

“Of course not.”

“The Murim is a place where no one knows what lies one inch ahead. Be respectful toward Jang Taebo—Guild Leader Jang—as well. The Ironcraft Guild has close ties with the Nine Sects and One Gang, and its current Guild Leader is Jang Taebo’s Disciple. It would be unwise to get on his bad side.”

“My hobby is filial piety, and my specialty is respecting the elderly.”

“I can still vividly recall the Third Young Master hurling every kind of profanity at the Head Elder.”

“Hey, that was a different matter!”

“Of course. That is all I meant. Why are you getting so angry? Now that you’re a Peak master, do you think I’m easy to deal with?”

Look at those eyes. He looked ready to challenge me to a duel.

Of course, if we actually fought, I would be the one getting beaten. I subtly changed the subject.

“But aren’t you busy? You must have a lot of work piled up.”

Wipeng frowned.

“I need to return as quickly as possible. The movements near Datong are unusual.”

“Datong… the northern Gaoyuan?”

“I hear those mounted bandits are prowling around again.”

“How long has it even been since the Red Wind Band was crushed?”

“Exactly.”

Rubbing his dry eyes, Wipeng rose from his seat.

“Then I will be off. I suppose we will see each other again at noon tomorrow.”

Wipeng put unusual emphasis on *noon tomorrow* to the very end. He was about to leave the room when he suddenly stopped.

“And there is something I have been meaning to ask you…”

“Yes?”

With an utterly bewildered expression, Wipeng pointed at the badly mangled door.

“What happened to this? It can’t have been more than a few days since it was completed.”

“Who do you think did it?”

The one person you, I, and everyone else would suspect, of course.

Wipeng seemed to realize who the culprit was. He let out a long sigh and left the room. Judging by his murderous back, he was clearly going to lay into Jin Wikyung.

“Well, I suppose I should head out, too.”

I was on my way to have a custom weapon made just for me. My steps felt light enough to fly.

* * *

“Are you ready?”

In front of the stables, Hyuk Mujin was inspecting the saddles. He answered curtly,

“Not yet.”

“Still?”

“Yes.”

Why was it taking so long?

When I approached, I saw that the horses’ sides were loaded with bundles. I sniffed one. They were all food. It was still warm, as though it had been cooked only recently.

“What’s all this?”

“What do you think? Food.”

“You think I’m asking because I don’t know that? Huh? I’m asking why you packed so much. Jerky and water would have been enough.”

Hyuk Mujin answered with a wounded expression.

“I didn’t pack it.”

“If you didn’t, who did?”

“Who do you think?”

Hyuk Mujin pointed behind me. A young man was running toward us, burdened with bundle after bundle.

The moment Cheongpung spotted me, he beamed.

“Oh! Hello, Benefactor!”

“Ah… yes.”

Hello, sure, but why are you here?

I stared at Hyuk Mujin with a demanding look, and he began explaining.

“I ran into him on the way to the stables. He said he wanted to come along. What could I do?”

Cheongpung shouted enthusiastically,

“Benefactor! Take me with you! I want to travel, too!”

“This isn’t a trip.”

“Oh, really? I heard we were going today and coming back tomorrow…”

If you went somewhere today and came back tomorrow, did that make it a trip?

When I explained that I was going to meet a blacksmith in Jeongyang, Cheongpung’s eyes lit up.

“Wow! A blacksmith!”

Hyuk Mujin and I spoke at the same time.

“You’ve never seen a blacksmith before, have you?”

“Looks like this is your first time seeing a blacksmith.”

“Yes, that’s right! How did you know?”

“…”

“…”

It was more surprising that he didn’t know.

Anyone who had spent even a single day dealing with Cheongpung would understand how I felt.

“Anyway, take me with you.”

“Well, I don’t really mind if you come along, but…”

“Woohoo!”

“Let people finish speaking, you idiot.”

Ugh, this was exhausting. *Was this what extrovert energy felt like?*

Already feeling tired, I leaped onto my saddle. I also made sure to remove the securely tied food bundles ahead of time.

When one of the bundles dropped to the ground with a thud, Cheongpung screamed.

“Ah! That’s five-spice pork!”

“Why did you pack five-spice pork? I told you we’d be back soon!”

“No! My five-spice pork!”

“…Fuck.”

It wasn’t even mine.

After stubbornly gathering all the food again, Cheongpung grinned.

“Now let’s go!”

*I really want to leave. Just without you.*

I clicked my tongue inwardly, took hold of the reins, and set off.

Then I had to listen to the sound of someone chewing behind me until the sun went down.

* * *

Winter days were short.

As the sun disappeared beyond the horizon of the plateau, a dry voice came from the giant.

“It is time.”

No sooner had he finished speaking than hundreds of silhouettes stirred in the darkness.

Draped in the hides of all kinds of beasts, they mounted their horses armed with curved sabers, sandalwood bows, and charging spears.

In the blink of an eye, a cavalry force of more than four hundred riders had appeared. They stared at the giant.

That same parched voice rang out again.

“Our task is simple.”

The giant’s eyes gleamed dangerously. The veins standing out on his forearms and the breath escaping his lips made him look like a wild beast.

“To kill and trample.”

Low laughter drifted from here and there.

Their leader had given them permission to run wild as they pleased. The more than four hundred mounted bandits belonging to the Heavenly Wind Band trembled with excitement.

The sight made the giant smile in satisfaction.

*At last, I can do this properly.*

The plan proposed by his sworn elder brother, Black Sand, was brilliant.

Of course, what he liked best was that all he had to do was kill and plunder the enemies in front of him without thinking.

His role was the most important—and the simplest.

*My blood is boiling.*

This was on an entirely different level from the ragtag forces like the Red Wind Band that had been scraped together from here and there.

The men before him had shared meals and fought battles together for more than ten years. They were seasoned elites who had fought a hundred battles.

*Heh heh. Just wait. Jin Family of Taiyuan or not, I’ll trample every last one of you.*

A thunderous roar erupted from the mouth of the giant, the Heavenly Wind Band Leader.

“Go! Kill and plunder everything! Slaughter and burn everything in sight!”

“Waaaaah!”

“Let’s go!”

The more than four hundred mounted bandits, brimming with excitement, had just turned their horses south when—

“You goddamn sons of bitches. Burn what, exactly?”

A shrill voice accompanied the appearance of a diminutive silhouette.

The hand of an unidentified old man shone an icy white.
## Chapter artifact 166

# Chapter 166

Old Man Jang’s daily routine was simple: eat, sleep, and shit.

Every now and then, he stopped by a pleasure house or an inn for a drink, or joined a gambling game and handled domino tiles, but he spent most of his time at home.

The villagers, who had grown fairly accustomed to him by now, would sometimes ask,

“Don’t you get lonely?”

But Old Man Jang’s answer was always firm.

“Don’t talk nonsense.”

People whispered that the solitary old man was only answering that way out of pride, but he meant every word.

*It couldn’t be more comfortable than this.*

Sleep when he was tired, eat when he was hungry, and shit when he needed to.

Some might mock it as a beast’s life, but Old Man Jang had more than earned the right to live that way.

No—he felt even that was insufficient.

*After the life I’ve lived.*

He had spent a full jiazi standing before vats of boiling molten iron.

Once he started something, he had always seen it through to the end. He had forgotten people and love alike. The anvil and hammer had been his friends and lovers.

*I lived like a man possessed.*

Then one day, he came to his senses and found that his hair had turned white and his vision had grown dim.

He had become one of the most renowned smiths in the world and the Guild Leader of the Ironcraft Guild, but that was all.

No matter how many times he brought down his hammer, the heart that had once been emptied could not be filled.

In the end, he decided to retire, and Jang Taebo, the Guild Leader of the Ironcraft Guild, became Old Man Jang.

“Grandpa!”

“Uh, hm?”

Old Man Jang had been squatting in the yard, staring blankly into space, when he suddenly came to himself.

A little boy from the neighboring house was staring at him with enormous eyes.

“What are you thinking about?”

“I was thinking that if you used polite speech, I might give you a piece of candy.”

“What are you thinking about, Grandpa?”

“…What a sly little brat. Here.”

“Thank you!”

Old Man Jang stared at the boy, who was busily sucking on the candy.

He had watched the boy grow since he was a newborn. The child had been a nuisance when he clung to him, constantly calling him Grandpa, but at some point, Old Man Jang had found himself carrying snacks around for him.

*Well, this isn’t so bad either.*

For a blunt and prickly old man like him, this boy was his only conversational partner.

Whenever he looked at the child, he sometimes wondered what it might have been like if he had had a family of his own.

“Would you like another one?”

“Yeah, yeah!”

“Ahem. Polite speech.”

“Yes!”

“You need to eat slowly so you don’t damage your teeth. Understand?”

“Yeah!”

“…That polite speech lasted all of two seconds.”

After licking two pieces of candy clean in no time, the boy suddenly spoke.

“Oh, right. Grandpa.”

“What is it?”

“What’s your name?”

“You should say ‘honored name’ when asking an adult… No, never mind. Why are you suddenly asking?”

“Hmm, I was just curious.”

“Hmm.”

“I asked Mom and Dad, too, but they said they didn’t know Grandpa’s name. Nobody knows.”

Though he had settled here more than ten years ago, Old Man Jang had never revealed his name to anyone.

He had been worried that unwanted flies might gather around him. No—flies would have been the least of his problems.

A great smith was needed everywhere, especially by Murim sects that would risk their lives over weapons. If his identity became known, his remaining years would become difficult.

“Grandpa, aren’t you going to tell me your name?”

Looking at the boy’s large, innocent eyes, Old Man Jang thought,

*Well, it should be all right to tell this one a little.*

He was too young to understand what any of it meant, wasn’t he? Besides, if Old Man Jang gave him a few pieces of candy, the boy would surely become distracted and forget it soon enough.

He only had to conceal enough that his identity would not be exposed.

“I’ll tell you one character of my name. It’s Bo.”

“Your family name is Jang, so… are you Jang Bo?”

“No. I said my name ends in Bo.”

“What’s the other character?”

“Curious, are you?”

“Yes!”

“Fine. If you use polite speech properly for the next month, I’ll think about it.”

“Wow, that’s mean.”

Old Man Jang let out a quiet laugh at the boy puffing out his cheeks.

“Hng. Can’t you just tell me? That way I can eat something tasty.”

“…?”

“Whew. I suppose it can’t be helped.”

What was that supposed to mean?

While Old Man Jang was wondering, the boy let out a deep sigh like an old man and sprang to his feet.

“Where are you going?”

“I’ll come back later!”

“Don’t bother coming back. The sun has set, you brat. Go home and get some sleep!”

“I don’t want to!”

The boy had short legs, but he was overflowing with energy. He quickly disappeared in the opposite direction from his house.

“Honestly, that boy never listens.”

Muttering under his breath, Old Man Jang rose, his stiff body creaking.

He felt as though he had been able to manage fairly well until ten years ago, but once his muscles began to waste away, his joints started aching here and there.

“Good grief. I’d better heat up the room.”

He fed firewood into the room’s firebox and lit the brazier.

After passing the time for a while, he went outside to use the privy before going to bed.

That was when—

“Grandpa!”

The boy’s innocent cry rang out.

But Old Man Jang did not hear it.

His seasoned gaze was fixed on the three imposing figures standing behind the child.

*Martial artists?*

It was already dark, so he could not make out their faces clearly. But he could unmistakably identify the sword sheaths protruding from their waists.

He had made countless such objects himself.

Without taking his eyes off them, Old Man Jang beckoned to the boy.

“Hanga, come here.”

“Yes!”

Now that he looked, the boy was clutching a large bundle to his chest. Along with its warmth came an appetizing smell.

Realizing the general situation, Old Man Jang glared at the figures in the darkness.

“Who might you be?”

Crack!

A spark flew in the darkness, and a flame soon caught. A fire starter in someone’s hand illuminated the faces of the three men.

They were all young men around twenty years of age. One of them stepped forward.

“My goodness. Good evening.”

He had a handsome face and a sly smile.

Old Man Jang stared intently at the vaguely familiar face before speaking.

“Sleeping Dragon of Shanxi?”

He had seen that face from a distance about half a month ago.

The young man, Jin Taekyung, broke into a wide grin.

“Oh, you know the Sleeping Dragon of Shanxi. That’s me. Hahaha.”

* * *

“An old man named Jang?”

“Yes. I was told he definitely lived in this village.”

“Well, there are so many of them. There must be twenty old men with the family name Jang.”

“He’s around eighty…”

“They all suffered when they were young, so they’ve all aged pretty similarly. The Jang next door is fifty, but if you look at his face, he’s a hundred and fifty.”

“…”

“Anyway, they’re all like that.”

“Um, he lives alone, and his name is…”

“Who remembers everyone’s name individually? Once they get old, they’re all just Old Man Jang. And there are plenty of people who live alone, too. War, drought, epidemics… Whew.”

“…”

Damn it. We had arrived before sunset, but we had run into trouble immediately.

I had wondered why there were so many old men named Jang in such a tiny village, but it turned out to be a clan village.[^1] Half the people we passed on the road had the family name Jang.

“Do you not know where he lives?”

Hyuk Mujin was growing frustrated, so I waved the letter containing the information in front of him.

“I don’t. It only says he lives here. I suppose they thought we’d find him quickly since it’s a small village.”

Cheongpung took some meat out of his bundle and began tearing into it.

“Chomp, chomp, chomp.”

“Then how are we supposed to find him? Jang is already a common family name.”

“We’ll have to find out for ourselves. There are only a few hundred people here, and he’s an old man, so we should locate him quickly.”

“Chomp, chomp, chomp.”

“…”

“…”

That bastard Cheongpung had done nothing but eat from start to finish.

Still, that might actually help us. I was just about to ask him for a piece of meat in quiet desperation when—

“Oh, the Grandpa who lives three houses down from us is named Jang, too.”

The speaker was a little boy whose head came almost up to my waist. He had big eyes and a fairly cute face.

I gently ruffled his shaggy hair.

“Really?”

“Yeah. He’s Grandpa Jang.”

“Really?”

I responded, though I did not hold out much hope. The woman selling vegetables at the roadside stall was named Jang, and so was the butcher over there. In a clan village teeming with people named Jang, what were the odds?

The boy sniffed and continued,

“Grandpa is always alone. He doesn’t have a family, so I go and play with him.”

“Oh, you little rascal. That’s kind of you—wait. He doesn’t have a family?”

“Yeah! I asked my mom, and she said he’d been like that since he first came here.”

“Since he first came? He wasn’t originally from here?”

The boy nodded vigorously.

“I heard this from my dad, but Grandpa came from somewhere outside. He came from outside, so he doesn’t have any friends or family.”

“I see.”

Hyuk Mujin and I exchanged glances. This sounded like a possibility, but it might not be.

“Little one, do you know his name?”

“Do you know anything else about him?”

“I don’t know his name. He’s just Grandpa Jang.”

It seemed that was all the boy knew. Hyuk Mujin asked with an eerily kind smile,

“Little one, do you happen to know where he lives?”

“Over there. At the edge of the village.”

As expected of the continent. This damn village was absurdly huge compared to its population.

Hyuk Mujin gauged the distance roughly with his eyes and spoke to me.

“It should take about fifteen minutes.”

It would take that long even on horseback. I shook my head.

“What if it isn’t him? Let’s start by searching the nearby area and work our way along.”

“Yes, that probably is the better approach. Aside from being from somewhere else, there’s nothing that makes him stand out as the one we’re looking for.”

Cheongpung nodded.

“Chomp. Chomp. Chomp.”

“…”

“…”

While I wondered whether I should simply hurl away that food bundle, the boy boldly held out both his little hands toward Cheongpung.

“Hmm?”

“Grandpa Jang said there’s no such thing as a favor with no price.”

That child already understood the world.

He had given us information and wanted a bite in return. That Jang grandfather or whatever. What a thing to teach a child who couldn’t have been more than five or six years old.

“Wow. My grandfather said something similar. Here.”

“Wow! Thank you!”

Look at that. Grandfathers united everyone.

Cheongpung coolly handed over a large leg of meat. Since he had periodically heated the food with the Zaha Divine Technique, which was based on Scorching Yang Qi, the meat was still warm.

*What kind of Zaha Divine Technique do you use to cook meat?*

After happily tearing into the meat, the boy looked at us with a gaze full of lingering regret.

“By the way, I have to go home anyway. On my way back, I’m going to see Grandpa Jang who lives three houses down from us.”

“Oh, really?”

I understood what he meant immediately. When you were desperate, you could borrow even a cat’s paw. There was no reason we couldn’t borrow a child’s.

“Then could you ask Grandpa Jang his name? Come back here in half a shichen.”

“Hmm. I think I’ll be hungrier by then.”

“You see those food bundles? I’ll give you one whole bundle.”

“Really?”

The boy’s eyes lit up, but then he suddenly hesitated.

“Why are you looking for Grandpa Jang?”

“It’s nothing serious. I just have a favor to ask him.”

“You’re not bad people, are you?”

If I introduced myself as the Sleeping Dragon of Shanxi from the Jin Family of Taiyuan, all it would do was draw a crowd for no reason. I answered with the most innocent smile I could manage.

“Of course not.”

“Ugh, why are you smiling like such a bad person?”

“…”

Should I just smack him on the head and send him away?

Hyuk Mujin stepped in on my behalf.

“I’ll give you two bundles.”

“So you were good people after all. I’ll be back!”

The child was already becoming a monster born of capitalism.

Hyuk Mujin shrugged.

“Where should we start looking?”

“Search everywhere, starting from the nearest entrance.”

“That’ll take half a shichen.”

Hyuk Mujin was wrong. It took more than half a shichen to search half the village, and then the boy returned.

With an extremely valuable clue.

*If the name starts with Jang and ends with Bo…*

The former Guild Leader of the Ironcraft Guild, Jang Taebo.

That had to be him.

* * *

“Sleeping Dragon of Shanxi?”

“Oh, you know the Sleeping Dragon of Shanxi. That’s me. Hahaha.”

The fact that he knew who I was was a good sign. It felt strange to say this about myself, but wasn’t the Sleeping Dragon of Shanxi practically Shanxi’s idol?

If this were a world with internet access, I would already have a fan club.

“I’m sorry to visit so late at night. The thing is, I have a favor to ask…”

“There’s no need to ask.”

“Pardon?”

Jang Taebo was over eighty, but he was a sturdy old man. He stared at me with a cantankerous gaze.

“I won’t accept the commission anyway.”

“Still, you should at least hear what it is…”

“No!”

Talk about a flat-out rejection.

[^1]: A clan village is a settlement where many households share the same family name and ancestral lineage.
## Chapter artifact 167

# Chapter 167

“No!”

What a set of lungs.

The shout rang out so loudly that it belied the speaker’s eighty years, and Cheongpung gulped down whatever was in his mouth.

“Benefactor, he really doesn’t want to do it, does he?”

I heard him, you idiot.

I’d heard he was a pretty cantankerous man, but I hadn’t expected this.

Still, if a few shouts were enough to make me back down, I never would have come this far in the first place. I calmly opened my mouth.

“Elder, please calm down first and let me explain—”

“What is there to explain? In the end, you’re asking me to make you a weapon, aren’t you?”

“Uh, well, that’s true.”

“You come barging in on an old man who retired ten years ago, in the middle of the night no less, and demand that he make you something meant to kill people?”

Jang Taebo glared and shouted,

“Get out of my sight this instant!”

“Waaah!”

As the loud shouts continued, the little boy in Jang Taebo’s arms burst into tears.

Hyuk Mujin, who was holding a fire starter, muttered in a voice only I could hear,

“What a temper on that old man…”

I agreed, but it was also true that I had been in too much of a hurry.

Judging by the way things were going, he wouldn’t accept my commission even if I died and came back to life.

*This is a problem.*

I had to return by tomorrow for the banquet on New Year’s Day.

As I hesitated, the villagers, alarmed by the commotion, began poking their heads out of their doors one by one.

“What’s all this racket?”

“That was Old Man Jang’s voice, wasn’t it? I heard Hanga crying next door, too.”

“Elder, is something wrong over there?”

There was nothing to gain from having our identities exposed here. No—in fact, they were the ones who stood to lose.

Jang Taebo frowned.

“It’s nothing. Seems some young men got dead drunk and came to the wrong house.”

“Tsk, tsk. Young people these days are all like that. If you need any help…”

“Your concern is enough.”

His firm reply made the open doors close one by one, and the murmuring voices abruptly fell silent.

When the surroundings grew quiet, Jang Taebo fixed us with his bulging eyes.

“Go home. And don’t come back.”

His tone was gentler than before, and his voice had dropped, but icicles still seemed to fall from every word.

There was nothing to be done. I turned away and bowed toward Jang Taebo’s back as he soothed the whimpering child.

“I’ll come see you again tomorrow.”

“You’re hard of hearing, aren’t you? Didn’t you hear what I just said?”

“…Then we’ll be going.”

I was about to turn around when I suddenly opened my mouth.

A thought had occurred to me—something that might move him, even a little.

“I really do need the help of a Master Artisan. That’s why I came to find you, elder.”

But Jang Taebo answered without even turning around.

“If you go west for one shichen, you’ll find a large village with a smithy. The owner there has some decent skill.”

“Is he skilled enough to forge Ten-Thousand-Year Cold Iron?”

Ten-Thousand-Year Cold Iron: a mysterious mineral infused with a supernatural power that made it the hardest and sharpest material in the world, capable of withstanding even Sword Energy.

It was so valuable and rare that even most highly skilled blacksmiths never got to see it once in their entire lives.

*If it were that Ten-Thousand-Year Cold Iron, maybe it would pique his interest.*

But Jang Taebo’s reaction was nothing like what I had expected.

“Ten-Thousand-Year Cold Iron? Then you should go to the Ironcraft Guild. Give it to that Guild Leader fellow, and he ought to manage it well enough. He learned a thing or two by watching me work.”

The moment I heard his indifferent voice, I realized it.

To him as he was now, even a metal as peerless as Ten-Thousand-Year Cold Iron was no different from copper.

“It’s late.”

That was an unmistakable dismissal. I had no choice but to turn around. Hyuk Mujin and Cheongpung followed me, speaking as we left.

“What are you going to do?”

“What do you mean, what am I going to do? I’ll keep trying until tomorrow.”

“Chomp, chomp, chomp.”

“He’s not just stubborn… But anyway, where did you get the Ten-Thousand-Year Cold Iron?”

“That’s a long story.”

“Chomp, chomp, chomp.”

“…”

“…”

Cheongpung cautiously studied the looks Hyuk Mujin and I were giving him before holding out a bundle.

“Would either of you like some? There’s still plenty left.”

We shouted at the same time.

“We’re not eating it!”

* * *

We spent the night at a half-collapsed inn. As the only inn in the small village, it was old and shabby in every possible way, but it did have one advantage.

The innkeeper was a native of the Jang clan village who had lived there for forty years.

He had been wary of the three of us, dressed like martial artists, but the moment I pressed a silver nyang into his hand, his smile stretched from ear to ear.

“Old Man Jang?”

“Yes. The man who lives over the hill.”

The innkeeper immediately nodded.

“Ah, of course I know him. He comes to our inn from time to time.”

“Does he?”

“Yes. Sometimes he drinks by himself, and sometimes he joins a gambling game.”

“He likes gambling?”

“Not exactly. I think he does it just to pass the time. Usually, he hardly ever leaves his house more than once every seven days.”

“He’s a homebody.”

“Pardon?”

“Ah, I was just talking to myself. Is he any good at gambling?”

The innkeeper thought for a moment before answering.

“He’s about average. If you really want to split hairs, he always loses a little at a time. But seeing as he comes every time despite not having a job, I suppose he must have saved a fortune when he was young.”

I suppose so. Geeks never spare money when it comes to their obsessions.

Every martial artist was a weapon geek in one way or another, and Jang Taebo was one of the best custom weapon makers in the world.

He had clearly earned more money than most.

*Can I lure him with money after all?*

I had gotten a rough idea from what happened last night, but the man really was difficult.

A transaction only worked when you satisfied the other party’s desires. And Jang Taebo seemed quite satisfied with his current life.

“Is there anything else? For example, does he ever make anything?”

“Make something?”

“You know, like a kitchen knife. Or a pickaxe.”

A repetitive life hardened into habit. That was especially true for someone like Jang Taebo, who had spent his entire life handling fire and iron.

If I were in his place, I wouldn’t be able to stand sitting still. I’d be too restless.

But the innkeeper pulled a strange face.

“Old Man Jang? He hates moving so much that he pays the Escort Bureau extra to deliver the firewood he’ll need for winter. I’ve never heard of him making anything.”

“…”

Escort Bureau rocket delivery, huh?

A homebody with a severe case of laziness. There wasn’t a single opening to exploit.

Hyuk Mujin and Cheongpung, who had been listening to the conversation while eating breakfast, suddenly joined in.

“He’s completely impossible to get through to.”

“Chomp, chomp. Wow, I’ve never seen anyone like that before.”

“…I’ve never seen anyone like you before, either.”

One of the inn’s major flaws was that the food was absolutely terrible.

The owner’s hands alone raised serious questions about the place’s hygiene, but Cheongpung swept up the remaining food as though none of that mattered.

“Is it good?”

“Yes! When I lived with Grandpa, I ate nothing but grass and fasting pills every day.”

“Ah, fasting pills.”

I could understand that. I’d rather make pancakes out of Jinho hyung’s vomit than eat those.

“…”

“Captain, why do you look like that?”

“Munch, munch. Benefactor, is something wrong?”

“…No. My stomach just feels a little queasy.”

Now that I thought about it, even that was going too far.

I rose from my seat after watching Cheongpung clean out the last plate.

“All right, let’s go.”

“Already? It’s only between seven and nine in the morning.”

“Can I have just one more dumpling?”

The innkeeper quickly cut in.

“Old Man Jang is getting on in years, so he doesn’t sleep late in the morning. And I’ll pack the dumplings for you right now.”

“There. Happy?”

I handed the innkeeper another silver nyang. He waved to us from in front of the inn until we disappeared from view.

* * *

“Elder, did you have a comfortable night?”

Jang Taebo was standing in the courtyard. When he spotted us, he frowned. More precisely, he frowned when he saw me.

“I believe I told you not to come back.”

“Could I really just leave after coming all this way?”

I gave him an easygoing smile.

Back when I was a lowest-level Hunter, there had been people who hurled profanity straight into my face. This was nothing.

“It felt wrong to come empty-handed, so I brought you a small gift.”

“Hmm?”

“The innkeeper was quite talkative. He said an acquaintance of his had dug up a thirty-year-old He Shou Wu[^1] not long ago.”

He Shou Wu was still used as a medicinal herb in the modern world.

In martial arts novels, century-old and millennium-old He Shou Wu appeared all the time, but here, even finding a thirty-year-old specimen was said to be as difficult as plucking a star from the sky.

In other words, even if you had money, it was difficult to find one in this area.

“A thirty-year-old He Shou Wu… So?”

“I was worried you might be feeling weak lately. It made me think of you, so I brought it along.”

Jinho hyung was always saying that a person’s body started breaking down once they passed thirty.

Your eyes got dry, your stomach started burning, and the day after you lent someone a USB, your legs stopped working properly.

If that was what happened to Jinho hyung in the prime of his life, how much worse must it be for old people? A thirty-year-old He Shou Wu was the perfect thing for maintaining one’s health.

“Hm. Why don’t you eat it?”

“Oh, goodness, me? No, no. I brought it for you, elder.”

The bait had caught his interest.

Feeling the fishing rod tug, I held out the He Shou Wu.

If properly consumed, it could build up about a year’s worth of internal energy, but I didn’t regret giving it away for a second.

“Please eat it. They say the best way is to chew it raw, roots and all.”

“Hmm. Should I?”

Yes, hurry up and eat it, then spit out a spear made of Ten-Thousand-Year Cold Iron.

At my bright smile, Jang Taebo popped the He Shou Wu into his mouth and began chewing noisily. The atmosphere was completely different from last night.

*Oh, this is looking good.*

If I coaxed him gently while the atmosphere was this pleasant, then submitted my commission…!

But the next moment, I heard the sound of my hopeful future being abruptly cut off.

“Ptooey!”

“...?”

“...?”

“...?”

Hyuk Mujin, Cheongpung, and I stared at the half-chewed He Shou Wu lying on the ground.

He spat it out? A thirty-year-old He Shou Wu? Why?

When we stared at him in confusion, Jang Taebo asked as though nothing had happened,

“Why are you looking at me like that? Is something wrong?”

“…Why did you spit it out?”

“It’s bitter.”

“Pardon?”

“It’s bitter.”

His unabashed answer left me speechless.

What kind of nonsense was that?

“Of course it’s bitter. It’s good for your health.”

“Tsk, tsk. You’ve never eaten He Shou Wu before, have you?”

“…No.”

I had eaten Hundred-Year Snow Ginseng once, but I hadn’t been in my own body at the time, so I couldn’t say.

When I awkwardly admitted it, Jang Taebo rummaged through his robes and tossed something at me.

“What is this?”

I caught it and found myself holding a wooden box about the size of a pencil case. Jang Taebo gave me a contemptuous smile.

“Open it.”

He supposedly gambled sometimes, but that sounded exactly like something a cardsharp would say.

I opened the wooden box with a strange feeling of tension.

“A fake! …No, it’s He Shou Wu?”

He Shou Wu?

And not just any He Shou Wu.

Its body and roots were thicker than the He Shou Wu I had given Jang Taebo moments ago.

A fragrant scent stabbed at my nose.

*Item check.*

Ding.

> **System**
>
> **Item Window**
>
> **Fifty-Year-Old He Shou Wu**
>
> **Type:** Spirit Herb
>
> **Grade:** First Rate
>
> **Restriction:** None
>
> **Description:** He Shou Wu that grew in nature for fifty years and has finally begun to hold spiritual energy. If absorbed by a martial artist who has learned a cultivation technique, it can provide up to about two years of internal energy.

“…”

They said even a thirty-year-old specimen was difficult to obtain. Where on earth had he gotten one fifty years old?

I was too dumbfounded to speak, and Jang Taebo gave me the smile of a victor.

“It comes in through the Nine-Room Escort Bureau once every four months. The head of the bureau owes me a favor. And he knows how to keep his mouth shut.”

“…I see.”

So it was a regular delivery from the Nine-Room Escort Bureau. No wonder the old man looked healthier than most young men.

“Stop with these transparent tricks. I’m a man who no longer needs anything.”

“You certainly seem that way.”

He had money saved up and had achieved professional success.

He even had a full head of hair.

The only thing he lacked was a family—but if I offered to introduce him to a pretty old lady, he’d probably try to kill me.

“What do I have to do for you to accept my commission?”

Jang Taebo scratched inside his ear with his pinky.

“If you bring me the Herb of Eternal Youth, I’ll think about it.”

“Pardon?”

“You didn’t hear me? The Herb of Eternal Youth—the spirit herb said to grant eternal youth and immortality.”

Ding.

> **System**
>
> Quest **In Search of the Herb of Eternal Youth** has been created.
>
> **Would you like to accept the Quest?**
>
> **Y / N**

This time, I shouted,

“No!”

[^1]: He Shou Wu is a traditional medicinal herb made from the tuberous root of *Polygonum multiflorum*.
## Chapter artifact 168

# Chapter 168

**Quest**

> **System**
>
> **In Search of the Herb of Eternal Youth**
>
> This is a Spirit Herb passed down only through legend.
>
> Rulers who dreamed of immortality and eternal youth poured enormous amounts of wealth and manpower into searching for the Herb of Eternal Youth, but no one has discovered it to this day.
>
> However, if you have about a thousand years left to live, it might not be a bad idea to give it a try.
>
> **Grade:** ???
>
> **Restriction:** Jin Taekyung
>
> **Mission:** Acquire the Herb of Eternal Youth (Incomplete)
>
> **Reward:** ???
>
> **Failure:** ???

“No!”

Beep.

> **System**
>
> You rejected the Quest.

What the hell kind of quest was this? The Quest Grade had even been replaced with question marks.

*What? “If you have about a thousand years left to live, it might not be a bad idea to give it a try”?*

What kind of bullshit was that?

At my incredulous stare, Jang Taebo stroked his beard.

“What? Can’t you do it?”

“…How exactly am I supposed to do that?”

“Then forget it. Give me back the He Shou Wu.”

Jang Taebo snatched the He Shou Wu from my hand and began chewing it with a crisp crunch.

“Oh, it’s sweet. Just as you’d expect from one that’s grown for fifty years.”

“…”

“Hm? Are you all still standing there? Did you need something?”

“No, elder.”

“Why?”

“Is it really reasonable to ask someone to bring you the Herb of Eternal Youth?”

“It’s been a long time since I met someone who cared about common sense in the Murim. There’s Hundred-Year Snow Ginseng, so why wouldn’t there be an Herb of Eternal Youth?”

“…”

That sounded surprisingly plausible.

I almost let myself be persuaded, but I quickly came to my senses. Somehow, I had to convince this old man who looked like even a needle couldn’t get through him.

“If there’s something else you need, I’ll get it for you. Anything you want. Just not something like the Herb of Eternal Youth.”

“Really?”

“Of course. If necessary, I’ll mobilize the full strength of my family.”

“Hm. I’ve heard plenty about how impressive the Jin Family of Taiyuan’s influence has become these days.”

Jang Taebo nodded and opened his mouth.

“Then I’m thirsty. Bring me a bottle of gongcheong seokyu.[^1]”

“Pardon?”

Gongcheong seokyu? The stuff said to grant a jiazi of internal energy with a single drop?

I barely stopped myself from letting loose a stream of profanity. Jang Taebo continued with a sly grin.

“You said you wanted to make a weapon out of Ten-Thousand-Year Cold Iron, didn’t you? Then you’ll need a fine scabbard, too. I hear there’s a dragon at the end of the world. Pull out one of its claws and bring it back. And while you’re at it, bring me a dragon pearl, too.”

Ding.

> **System**
>
> Quest **Get Gongcheong Seokyu, a Dragon’s Claw, and a Dragon Pearl** has been created.
>
> **Would you like to accept the Quest?**
>
> **Y / N**

…Was I going to?

Feeling my insides boil, I closed the Quest window. Hyuk Mujin covered his mouth and whispered,

“I think the old man’s senile.”

“I can hear you. You wet-behind-the-ears brat has a lot to say.”

Just as Jang Taebo was waving a fist the size of a cast-iron pot, Cheongpung suddenly raised his hand and shouted,

“I’ll go find them! Let me do it!”

“What?”

“The Herb of Eternal Youth! Gongcheong seokyu! A dragon!”

At last, the neighborhood’s resident lunatic had stepped forward.

His eyes sparkled like morning stars, and his every gesture burned with enthusiasm. Jang Taebo flinched and took a step back from Cheongpung’s forcefulness.

“Who are you?”

Cheongpung answered energetically,

“I’m my grandpa’s grandson!”

“Who’s your grandfather?”

“My grandpa!”

“…What a lunatic.”

Welcome. First time dealing with Cheongpung?

As Jang Taebo shook his head from side to side, I casually added,

“Do you happen to know Great Hero Mae Jonghak?”

“Though I’m not a martial artist, I’ve spent my entire life with one foot in the Murim. Do you think I wouldn’t know the Sword Saint, whom even butchers have heard of?”

“That friend is the disciple personally raised and taught by the Sword Saint.”

“What? Is that true?”

“Why would I lie? Especially while staking the name of someone as distinguished as the Sword Saint?”

“Hah. So he’s the Sword Saint’s successor…”

Had that worked? No matter where you went in the world, connections were king: school ties, hometown ties, and blood ties.

In the Murim, the Sword Saint Mae Jonghak’s very existence was an object of respect and awe.

Jang Taebo stared at Cheongpung with clear surprise before opening his mouth.

“So what do you want me to do about it?”

“Ah…”

“I have nothing to do with Huashan. Well, I did make a sword at the request of the current Sect Leader of Huashan, Heavenly Sword True Person[^2], about thirty years ago. But that’s all.”

His firm voice continued.

“I’m eighty years old. I’m still in good health, and I’ve accumulated plenty of wealth. As someone who has worked with iron, I can proudly say that I’m among the top three in the world.”

“That’s why I’m asking you.”

“That’s why I’m refusing you. I’ve finished all the work I care to do. I’ve made swords until I’m sick of them.”

“I use a spear.”

“Oh, did you?”

“Yes.”

“If it’s a spear, it’ll require even more work. Swords are better.”

“Elder!”

I grabbed Jang Taebo’s hand with an earnest look.

“Couldn’t you think of it as a pastime after so long and help me just this once?”

“When did I say I wouldn’t?”

“You just said you wouldn’t.”

Jang Taebo roughly shook my hand away.

“I said I’d help you. If you bring me the Herb of Eternal Youth.”

“Oh, please.”

“Bring me the gongcheong seokyu and dragon pearl while you’re at it. I hear that when fighting a dragon, you should avoid its tail, circle around behind it, and choke its neck. I’m telling you so you don’t get hurt.”

“…A dragon isn’t a person. How am I supposed to kill it by choking it?”

“Then burst its balls.”

“What if it’s female?”

“See you in the next life.”

I had finally met a formidable opponent.

His way of screwing with people had been honed over decades. My fists trembled, and the back of my head throbbed.

“Are you really going to be like this?”

“That is precisely how I’m going to be.”

“I didn’t want to go this far…”

“Go on, spit it out.”

“Should I spread the word? That the former Guild Leader of the Ironcraft Guild lives here?”

I was only saying that. Obviously, I had no intention of doing it.

But Jang Taebo merely grinned at my threat to make his life difficult.

“Then I suppose I have no choice. I’ll have to return to the Ironcraft Guild before all sorts of gnats start swarming around.”

“Huh?”

This wasn’t how it was supposed to go. Just as I was thinking that, Jang Taebo asked,

“If I return to the Ironcraft Guild, what do you think I’ll do?”

“…How would I know?”

“I’ll devote the rest of my life to making ten weapons. Then I’ll distribute those weapons, each made with all my heart and soul, to the leaders of the Nine Sects and One Gang, while having in-depth conversations with them about the Jin Family of Taiyuan. Your name will come up quite a lot, especially.”

“W-What are you planning to tell them?”

“I’ll leave that to your imagination. Oh, and you do know that martial artists will stake their lives on their weapons regardless of the level of their martial arts, right? I’m sure they’ll be happy to grant a small request of mine.”

“…”

It might be a small request to the leaders of the Nine Sects and One Gang, but it was anything but small to me or the Jin Family of Taiyuan.

If he bad-mouthed us with even a few words in front of them, a hit to our reputation would be the least of it. We might even face real pressure from them.

“Well, I suppose I should start preparing to leave. Let’s see, what should I pack…?”

As he turned to go into his room to pack, I grabbed his wrist. Jang Taebo asked innocently,

“What is it?”

I lowered my head helplessly.

“Please stop. I admit defeat.”

“Is that all?”

“I’m sorry for acting cocky.”

“And?”

“I won’t tell anyone that you’re living here.”

“Given that you came looking for me like this, it can’t be something only you know, can it?”

“I’ll explain everything properly to my eldest brother, too.”

“You’re sure?”

“Of course.”

“Hm. You’re not completely ill-mannered, then.”

Having gotten every answer he wanted, Jang Taebo smiled with satisfaction.

I had defeated enemies stronger than me all this time, but I couldn’t break the will of an old man enjoying a quiet retirement.

*So where am I supposed to have the Ten-Thousand-Year Cold Iron forged?*

I’d finally thought I was about to have my first cherished weapon…

I was staring at the He Shou Wu Jang Taebo had half-chewed and abandoned, my spirits sinking, when he spoke.

“You said you were making a spear?”

“Pardon?”

“Are you deaf? Why do you keep asking me to repeat myself?”

I hurriedly raised my head and saw Jang Taebo’s gruff face. He continued,

“Well, if you ask me to make it myself, I’ll obviously refuse. But I can at least give you an introduction.”

“You mean the Guild Leader of the Ironcraft Guild, your disciple…”

“Do you think the Guild Leader has that much time on his hands? He’s busy, too. Someone of your standing will have to wait several years at the very least.”

“Several years?”

“What, did you think a weapon could be completed overnight? He’s not as good as me, but he has some skill of his own, so obviously his orders are backed up. Even if he picks and chooses what to accept, it still takes that long.”

Even so, several years?

The unexpected long-term project left me short of breath.

“T-Then what do I do?”

“What do you mean, what do you do? I’ll write you a letter of introduction. Take it with you. You’ll be going there with a recommendation from his master, so he’ll probably do it a little sooner. That fellow can make one hell of a spear.”

“Ooh. Ooooh.”

“The village was in an uproar because of those mounted bandits, and I heard you were the one who dealt with them. I’ll do this for you as a special favor. Do you have paper, ink, and a brush?”

Hyuk Mujin, suddenly singled out, answered with a bewildered expression,

“No.”

“Yeah. You don’t look like someone who carries them. Then you there…”

“Chomp, chomp, chomp.”

He’s eating that now?

Jang Taebo sighed at the sight of Cheongpung stuffing the dumplings we had bought at the inn into his cheeks until they looked ready to burst.

“…Are the dumplings good?”

“Chomp, chomp. Yes.”

“Mae Jonghak took in a strange one in his later years. Fine, wait here a moment.”

*When you’re old, you should just die. Young people these days have no manners.*

Jang Taebo muttered loudly enough for us to hear and returned from inside with paper, ink, and a brush.

“First, the weapon is a spear… Do you have any thoughts about its shape or weight?”

“Ah, yes.”

“Tell me.”

I began describing in detail the weight and shape that had become thoroughly familiar to me after using a spear for seven years.

Each time, Jang Taebo either nodded silently or added advice on how to make a spear better suited to me.

*He really is an expert.*

Sixty years in the trade had not gone to waste.

He took a quick look over my body, then reeled off one correction after another. He somehow estimated the size of my hands and the length of my arms and legs, then adjusted the thickness and shape of the spear shaft little by little.

“All right, this is the last thing. Where are you planning to put the Ten-Thousand-Year Cold Iron? In the spearhead, presumably?”

“…?”

“Why are you making that face? You said you had Ten-Thousand-Year Cold Iron. You’re not planning to leave it out, are you?”

“No, I’m going to use it…”

“Do you not have much? In my estimation, ten nyang should be enough to make something worthy of being called a renowned spear. It wouldn’t be embarrassing to pass down as a family heirloom.”

How much was ten nyang? I still wasn’t used to the unit of weight, so I had no idea.

When I hesitated, Jang Taebo shouted,

“Ah! How much of it are you going to put in?”

“That’s… Just a moment.”

Seeing was believing. It would be faster to show him directly.

I pretended to rummage through my travel bag and casually held out the Ten-Thousand-Year Cold Iron I had taken from my Inventory.

“It’s about this much.”

“…”

“Elder?”

Jang Taebo didn’t answer. He stared intently at the Ten-Thousand-Year Cold Iron, which was larger than an adult’s head, for a long time before asking in an intensely hoarse voice,

“This… This is all Ten-Thousand-Year Cold Iron?”

“Yes. This isn’t your first time seeing it, is it?”

“I-I can’t believe this.”

His wrinkled hands trembled faintly. Jang Taebo stroked the cold, bluish Ten-Thousand-Year Cold Iron as though he had been reunited with a child after sixty years. A sharp light flashed in his eyes.

“Entrust it to me.”

The old man who had found everything a nuisance was nowhere to be seen. His voice was brimming with passion and vitality.

“I’ll make you the greatest divine weapon in the world.”

Ding.

> **System**
>
> The Quest mission has been completed.
>
> Quest **Find the Master Artisan** has been successfully completed.
>
> A linked Quest has been created.

[^1]: Gongcheong seokyu is a rare martial-arts elixir said to grant a jiazi of internal energy with a single drop; its name also carries a petroleum-related pun in Korean.

[^2]: “Heavenly Sword True Person” is a Taoist-style title meaning a true person of the heavenly sword.
## Chapter artifact 169

# Chapter 169

At the dim break of dawn, a group of people was making its way through the thick fog.

Two middle-aged men at the front exchanged words in low voices.

“Are you sure that information is reliable?”

“More than ninety percent.”

“More than ninety percent?”

“I can’t be certain until we confirm it ourselves.”

“Then what about the remaining ten percent…?”

“They could have leaked the information on purpose.”

“Then it’s a trap.”

“That’s why we’re taking every precaution in case something happens, isn’t it?”

The two middle-aged men swallowed hard. They weren’t the only ones. The people following behind them did the same.

Each of them gripped their weapons tightly, their eyes dripping with anxiety and tension.

“Damn it. We’ve stepped in shit.”

“Same here. I had a bad feeling from the moment I took charge of the Datong Branch.”

The two middle-aged men exchanged sympathetic looks. They led the Datong Branches of the Jin Family of Taiyuan and the Lower District Sect, both of which had been established only a month earlier.

“I was bragging to my wife about getting promoted just the other day. At this rate, I might end up making her a widow.”

“Stop whining. It’s more than ninety percent.”

“What happens if we hit the ten percent?”

“We die surrounded by more than four hundred mounted bandits.”

“…”

“Look at your face. Stop saying unlucky things and watch the path. We’ll be there soon.”

After the Lower District Sect Branch Leader finished speaking, silence descended.

They moved forward slowly and steadily, suppressing even the sound of their footsteps. The dense fog blanketing every direction concealed both their figures and their voices.

How long had they been walking?

By then, everyone’s bodies were soaked with sweat and moisture.

“Stop!”

The low, restrained shout came from the Datong Branch Leader of the Jin Family of Taiyuan. Gripping the hilt of his sword hard enough to crush it, he asked the Lower District Sect Branch Leader,

“Didn’t you hear something just now?”

“What…? Ah!”

The Lower District Sect Branch Leader’s face stiffened.

Some kind of noise coming from beyond the fog had pierced their ears.

*This is…*

The sound of horses snorting. And not just one or two.

The two men raised their tightly clenched fists. At the same time, dozens of sword blades blackened with soot emerged.

Beyond the thick fog, where they could barely see a zhang ahead, it felt as though hundreds of mounted bandits armed with bows and charging spears might burst through at any moment.

Gulp.

Just as someone’s throat bobbed loudly, a sudden gust swept across the grassland and brushed away the fog.

When the scene beneath it was revealed, everyone’s eyes widened.

“Gasp!”

“W-What in the world…?”

Beneath the blue sky of the grassland lay red earth. The ground was blackened all over, and the stench of blood and death hung in the air.

The Lower District Sect Branch Leader let out an involuntary groan.

“So the information was true.”

Dozens of bewildered gazes swept across the surroundings. Hundreds of men and horses lay sprawled on the ground, all life already gone from them.

Severed limbs rolled about like weeds, while eyes frozen wide with terror and shock stared blankly at nothing.

The few horses that remained alive let out hungry snorts as they trampled a flag covered in hastily scrawled red characters.

<br>

**HEAVENLY WIND**

<br>

There was no mistake. It was the flag of the Heavenly Wind Band.

The annihilation of the Heavenly Wind Band, which had once made a name for itself throughout the northern Gaoyuan through its brutality. The ninety-percent guess had finally become a hundred-percent certainty.

The Jin Family of Taiyuan and the Lower District Sect had been watching the Heavenly Wind Band’s movements closely for nearly half a month. They should have felt relieved, as though a rotten tooth had finally fallen out, but as time passed, the two Branch Leaders’ faces grew darker and darker.

“T-This…”

“That’s right. All of this was done by one person.”

The scattered corpses seemed to speak for themselves.

They had all been defeated by a single person.

“What an incredible master. I can’t even begin to guess how powerful he is.”

The Jin Family Branch Leader, who possessed the highest martial arts among them, continued in a trembling voice.

“Every one of them died in a single move. Judging by the way their insides were burned through, the killer must have trained Scorching Yang Qi to its utmost limit.”

“T-Then what about the martial arts? Can you tell what kind he used?”

“Not at all. He didn’t even use any distinctive martial art. This was… nothing more than overwhelming force crushing everything in its path.”

One person had slaughtered more than four hundred mounted bandits. And he had done it as easily as killing ants.

The corpses scattered in every direction bore the traces of an attempted escape, while the horribly twisted faces bore the marks of terror.

Not one person had survived the hands of this unidentified master who possessed such terrifying martial arts.

“C-Could something like this really happen?”

“It must be possible. We’re looking at it with our own eyes.”

That was true. The sight spread before them was both evidence and witness.

The two men stood in silence, unable to continue the conversation.

“Here! We have a survivor over here!”

A survivor?

Their eyes snapped open at the sudden shout. The two Branch Leaders immediately displayed their movement techniques and ran like the wind. As they arrived, they muttered like men groaning in disbelief.

“A survivor?”

“He’s still breathing. Though it won’t be for long.”

Just as the man had said, the only survivor was already little more than a corpse.

His left arm had been torn apart as though devoured by a beast, and the smell of burning flesh rising from the gaping hole in his side was nauseating.

The Lower District Sect Branch Leader stared intently at the man’s face, which was relatively intact, and spoke.

“This man is the Heavenly Wind Band Leader.”

“Is that really true?”

“I’m certain.”

The Heavenly Wind Band Leader had distinguished himself as far back as ten years ago, and his face was widely known.

The Lower District Sect’s Datong Branch Leader had been appointed only recently, but he had memorized the faces of all the major figures.

In particular, lately he had seen the Heavenly Wind Band Leader’s face more often than his own children’s.

“He was at least among the top five in the Gaoyuan—no, the top three… I never imagined he’d end up like this.”

The leaders of the mounted-bandit forces ruling the Gaoyuan all possessed outstanding martial arts, but the Heavenly Wind Band Leader had stood above the rest.

His head was dull, but his innate talent for combat alone had allowed him to become one of the major powers of the Gaoyuan—a Peak master.

But now he was nothing more than a defeated man on the verge of death.

“Being a Peak master at least made his attacker use two moves: one to tear off his arm and another to land a punch.”

He had defeated a Peak master in only two exchanges?

At this point, it was beyond belief.

Everyone had lost the ability to speak when—

“Khrrk. Khrrrk.”

The Heavenly Wind Band Leader’s body writhed as he made a phlegmy sound.

He soon forced his eyes open, and a dry voice leaked from between his lips.

“Save… save me.”

“Heavenly Wind Band Leader. Is that who you are?”

“Y-Yes. That’s me.”

The Jin Family Branch Leader sent internal energy toward his wrist. The man’s eyes became a little clearer. Just a little.

“Don’t worry. You can survive.”

It was a lie.

They desperately wanted to save him, but it was already too late. There was a mountain of things they needed to ask before his breath stopped altogether.

“Who did this?”

The instant the question ended, the Heavenly Wind Band Leader’s body jerked like a bird struck by an arrow. At the same time, his one remaining hand seized the Branch Leader by the collar.

The strength was too powerful to believe it came from a dying man. The open mouth reeked of death.

“An old man. It was an old man. He’s a demon who rose from a pit of fire.”

“Let go!”

“They’re all dead. I’m dead too. I’m already dead. The demon killed me.”

“You—!”

The horrified Branch Leader hurriedly tried to pull away, but the strength slowly drained from the Heavenly Wind Band Leader’s grip.

The body, its life force gone, gradually tilted before finally collapsing. His wide-open eyes glared up at the blue sky.

“Hah… hah… Is he dead?”

The Lower District Sect Branch Leader nodded and let out a sigh.

“He was completely out of his mind.”

“No wonder. It’s a miracle he was still alive. He lasted nearly two days in that condition.”

“At least it’s fortunate that we gained something from this.”

“Besides the fact that he was old, what do we know?”

“He was an old master in the Supreme Peak realm who primarily used Scorching Yang Qi. Judging by the fact that he didn’t leave a single person alive, he’s merciless as well. If he came this way past Datong, he’d attract attention in no time.”

After hesitating for a moment, the Lower District Sect Branch Leader added,

“…One way or another.”

Whether he was simply an old master who showed no mercy, or the appearance of a great demon beyond their imagination, they had no way of knowing.

To prepare for the possibility of the worst, there was only one thing the two of them could do.

“We need to send a dispatch to our family.”

“So do I.”

The two men looked at each other with dark expressions and simultaneously thought similar thoughts.

*Who exactly was the old man the Heavenly Wind Band Leader mentioned? And also…*

*Where could he be now?*

* * *

The woodcutter met the old man halfway up an unnamed mountain.

The first time he saw the old man leisurely walking along the rugged mountain path, only one thought crossed his mind.

*Is he a mountain spirit?*

In all his life, he had never seen anyone so old. Looking at the woodcutter awkwardly prostrating himself, the old man asked,

“What is it?”

“My name is Jang-pal.”

“…So?”

“I’ve come to pay my respects to you, Mountain Spirit.”

After a brief silence, the old man opened his mouth.

“What kind of lunacy… Are you trying to make a perfectly healthy living man ascend to immortality?”

“Y-You’re not one?”

The woodcutter, Jang, looked the old man up and down.

Now that he thought about it, there were more than a few strange things about him. For one thing, an immortal should radiate a divine aura at first glance and speak in an elegant tone of voice…

“Have you ever seen an immortal dressed like this? My robes are so open that cold wind keeps blowing right in.”

That eccentric way of speaking, those loose clothes torn in places…

The only thing he had in common with an immortal was his extraordinary age.

“I’m sorry. I’m completely uneducated.”

Jang gave an awkward smile, and the old man waved his hand.

“If you understand, be on your way.”

“Yes.”

Jang bowed politely and continued walking.

“…”

“…”

“You there.”

“Yes?”

The old man frowned deeply.

“Why do you keep following me?”

“Ah, this is the road to the village.”

“What’s ahead if you keep going this way?”

“Jang Family Village. It’s a small village. I live there too.”

“Jang Family Village? Judging by the name, I suppose it’s a clan village.”

“That’s right.”

The old man clicked his tongue.

“Why are there so many clan villages around here? Less than half a shichen ago, there was something called Hong Family Village or whatever.”

“Hong Family Village?”

“What? You know the place?”

“Yes. Of course I know it. I do. But…”

Jang tilted his head.

“Hong Family Village should be at least three hundred li from here. Are you perhaps confusing it with somewhere else?”

“Do I look like some idiot who can’t even remember something that happened half a shichen ago?”

Three hundred li was a distance that even Jang, whose legs were quite sturdy, would need a full two days to walk.

But three hundred li in half a shichen?

Jang, a simple country bumpkin, clicked his tongue inwardly in pity.

*He’s a senile old man.*

His appearance certainly suggested as much. A painfully thin body and disheveled hair.

Why had the old man come to this mountain, where only woodcutters like Jang climbed?

*Ah, perhaps?*

A story suddenly came to mind. There were unfilial sons who abandoned their parents in the mountains to reduce the number of mouths they had to feed. Perhaps this old man had suffered something similar.

Jang looked at the old man with simple, kind eyes before taking something out from inside his clothes and holding it out politely.

“Elder, please have this.”

“Hm? What is it?”

Jang scratched the back of his head.

“I brought it along just in case… but I’m full.”

It was a rice ball his wife had prepared early that morning. He was hungry after working so hard, but surely the old man before him must be even hungrier.

“It’s nothing much, but please eat it.”

“It really does look like nothing much.”

“…”

“I’m joking.”

The old man looked back and forth between Jang and the crude rice ball before speaking.

“I was feeling empty, so this is perfect.”

The old man devoured the palm-sized rice ball in the blink of an eye. Jang offered him the wooden carrying frame on his back.

“Please climb on. If you sit on top of the bundle of firewood, you should be able to make it down comfortably.”

“Hm? You want me to ride that?”

“Yes. The mountain path is rugged. You’re going down anyway, aren’t you?”

“That’s true, but…”

Jang smiled simply.

“You reminded me of my father, who passed away a long time ago.”

The old man wore a complicated expression for a moment before clicking his tongue and climbing onto the carrying frame. He was light enough for Jang to lift with one hand.

“Are you comfortable?”

“My backside is being poked to death.”

“Should I go a little more slowly?”

“Slowly? You should be running as if you were flying. Ah, and about that father of yours who passed away…”

“Yes?”

“What sort of person was he? If looking at me reminded you of him, he must have been quite handsome and strapping.”

“…”

Jang suddenly became much quieter.

Jang Family Village began to come into view ahead of him.

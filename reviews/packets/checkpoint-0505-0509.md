# Checkpoint Review — 505–509

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

# Chapters 505–509

## Plot

Jeok Cheongang achieves Returned to Youth, becoming a tall, muscular, red-haired man while retaining his gruff personality. He confronts Zhuge Feng over the Demonic Cult’s attack on Mount Jiuhua and demands that the Zhuge Clan support the approaching war as effectively as it did during the Great Faction War. Taekyung’s party departs for Henan and the New Murim Alliance.

At Wudang, Sect Leader Hyeoncheon learns of the approaching war and decides to travel to Henan. A pursuit party claims to have captured the Killing Ghost, but the remains they bring back are neither beast nor human, leaving the identity and nature of the captive unresolved.

Taekyung’s group travels by swift ship along the Yangtze. Mu Song explains that he wants to aid the New Murim Alliance but lacks authority over the Yangtze River Channel League, whose major decisions belong to the Seafaring King. The League, the Green Forest Alliance, the North Sea Ice Palace, and the Nanman Beast Palace may all influence the alliance’s prospects. Jeok expects the Nanman Beast Palace to favor orthodox Murim because of the Fire Gate Clan’s historical aid, but doubts the isolationist North Sea Ice Palace will participate.

Mungyeong reveals that Mu Song and five Water Dragon Stronghold subordinates recognize him as an extraordinary Supreme Peak master. He forces them to keep his identity secret, even from the Seafaring King, then sends Taekyung into the Yangtze. The Linked Quest **Fake Murim Martial Artist—Stage 2** begins.

Mungyeong explains that Taekyung’s unstable movement across the water results from the Fire Gate Clan’s excessively violent internal energy. He assigns Taekyung to practice **Rising on Duckweed, Crossing Water** behind the ship for ten days or until they reach Henan. The training is intended to improve his internal-energy control, reduce energy consumption, strengthen amplification, and enable further technical growth.

## Continuity

- Jeok Cheongang has achieved Returned to Youth and now appears as a tall, muscular, red-haired man.
- Jeok has demanded that the Zhuge Clan support the approaching war at least as effectively as it did during the Great Faction War.
- Taekyung’s party is traveling by swift ship along the Yangtze toward Henan and the New Murim Alliance.
- Hyeoncheon is Wudang’s Sect Leader and has decided to travel to Henan after learning of the approaching war.
- The remains attributed to the Killing Ghost are neither beast nor human; their identity and nature remain unresolved.
- The Yangtze River Channel League and Green Forest Alliance may become rear threats to the New Murim Alliance. The North Sea Ice Palace remains isolationist, while Jeok expects probable support from the Nanman Beast Palace because of the Fire Gate Clan’s historical relationship with Nanman.
- Mu Song and five Water Dragon Stronghold subordinates know that Mungyeong is an exceptionally powerful Supreme Peak master but do not know or have not inferred that he is the Slaughter Saint. Mungyeong has threatened them into silence.
- Mungyeong is training Taekyung to stabilize the violent internal energy produced by the Fire Gate Divine Technique.
- **Fake Murim Martial Artist—Stage 2** requires Taekyung to practice **Rising on Duckweed, Crossing Water** behind the ship for ten days or until arrival in Henan. The System’s countdown has begun.

## Translation Decisions

- Retain **Returned to Youth**, **New Murim Alliance**, **Yangtze River Channel League**, **Green Forest Alliance**, **North Sea Ice Palace**, **Nanman Beast Palace**, **Supreme Peak**, **Slaughter Saint**, **Fire Gate Clan**, **Fire Gate Divine Technique**, and **Rising on Duckweed, Crossing Water**.
- Render **새외무림** as **Outer Murim**, **새외** as **Outer Lands**, **야수묘왕** as **Beast Miao King**, **소뢰음사** as **Small Thunderclap Temple**, **광풍사** as **Mad Wind Society**, **포달랍궁** as **Potala Palace**, **오독문** as **Five Poisons Sect**, and **독곡** as **Poison Valley**.
- Render **궁예** as **Gung Ye**, with a brief explanatory footnote for the mind-reading joke.
- Render **연계 퀘스트** as **Linked Quest** and **가짜 무림인-2단계** as **Fake Murim Martial Artist—Stage 2**.
- Use **oar** for 노, **throwing blade** for 비도, **stern** for 선미, **fire qi** for 화기, and **stagnation** for 답보.
- Preserve the established renderings **Energy-Dispersing Poison**, **Seven-Step Soul-Chasing Powder**, **Blood Fish**, **Mutated Minnow**, **innate qi**, **true-origin qi**, **Heart Demon**, **Demon-Sealing Formation**, and **New Murim Alliance**.

## Durable state

{
  "active_continuity": [
    "Jeok Cheongang's Heart Demon and the dark memories binding him have been expelled; he has entered a new realm and achieved Returned to Youth.",
    "Mungyeong is the Slaughter Saint and former Divine Physician, a Returned to Youth Supreme Peak master and the greatest assassin in history; Mu Song and five Water Dragon Stronghold subordinates know he is an exceptionally powerful master but not that he is the Slaughter Saint.",
    "Mungyeong is training Taekyung to refine the stability and precision of the violent internal energy produced by the Fire Gate Divine Technique through Rising on Duckweed, Crossing Water.",
    "Zhuge Feng's Demon-Sealing Formation blocks all mana from the exposed Gate by drawing in natural qi, but whether it is permanent and repeatable remains unresolved.",
    "Jang Taebo is the Jin Family of Taiyuan's Master of Ironcraft Hall and is summoning renowned artisans to process the Water God Dragon's remains.",
    "War has begun and the New Murim Alliance is being formed at Mount Song; Taekyung believes Dark Heaven planned the Gate incident, while Jin Wikyung's Hubei arrangement was designed to create an opening among rival unorthodox factions.",
    "Around one hundred Level 5 Mutated Minnows, locally called Blood Fish, were captured in the Gate's entrance waterways; the remaining population is unknown, and the fish kill one another.",
    "The Southern Heaven Demon Empress is traveling toward Yunnan and expects to cause further deaths.",
    "Jin Mukyung remains secluded in the training hall after losing to Cheongpung, refusing to emerge until he achieves a great accomplishment.",
    "Taekyung's party is traveling by swift ship along the Yangtze toward Henan; Taekyung must practice Rising on Duckweed, Crossing Water behind it for ten days or until arrival.",
    "Mu Song wants to aid the Murim Alliance, but the Seafaring King alone decides the Yangtze River Channel League's major matters; the League and Green Forest Alliance may become rear threats.",
    "The North Sea Ice Palace remains isolationist, while Jeok Cheongang believes the Nanman Beast Palace will probably support orthodox Murim because of its historical goodwill toward the Fire Gate Clan."
  ],
  "continuity_sources": [
    509,
    508
  ],
  "open_questions": [
    "Will the Demon-Sealing Formation remain effective permanently, and can equivalent formations be installed repeatedly if more Gates appear?",
    "What is the Lord of Heaven's identity, and how is he connected to the dangerous force Taekyung associates with his original world?",
    "Where is the Southern Heaven Demon Empress ultimately headed, and what does she intend to do in Yunnan?",
    "Will the Nanman Beast Palace, North Sea Ice Palace, Yangtze River Channel League, and Green Forest Alliance support, ignore, or oppose the New Murim Alliance?",
    "Will Taekyung complete the ten-day Rising on Duckweed, Crossing Water training successfully?"
  ],
  "safe_through": 509,
  "temporary_decisions": [
    "Render 새외무림 as Outer Murim, 새외 as Outer Lands, 북해빙궁 as North Sea Ice Palace, 야수묘왕 as Beast Miao King, and retain Nanman Beast Palace for 남만야수궁.",
    "Render 소뢰음사 as Small Thunderclap Temple, 광풍사 as Mad Wind Society, 포달랍궁 as Potala Palace, 오독문 as Five Poisons Sect, 독곡 as Poison Valley, 천축 as India, and 갠지스강 as Ganges River.",
    "Render 파사국 as Persia, 회교도 as Muslims, 영웅건 as hero headband, 대막 as great desert, 귀염권 as Ghost Flame Fist, and 장성 as Great Wall.",
    "Retain established renderings including Energy-Dispersing Poison, Seven-Step Soul-Chasing Powder, Blood Fish, Mutated Minnow, innate qi, true-origin qi, Heart Demon, Returned to Youth, Demon-Sealing Formation, and New Murim Alliance; use oar, throwing blade, stern, and fire qi for this chapter's newly established terms.",
    "Render 궁예 as Gung Ye with an explanatory footnote, and render 연계 퀘스트 as Linked Quest and 가짜 무림인-2단계 as Fake Murim Martial Artist—Stage 2."
  ],
  "version": 1
}

## Reading copies

## Chapter artifact 505

# Chapter 505

Returned to Youth was the realm every martial artist in the Murim dreamed of reaching.

When immense internal energy combined with enlightenment, the human body would be reconstructed, granting its owner the youth of the past.

But if Returned to Youth were that easy, countless martial artists would not have died after spending their whole lives dreaming of it.

It was something impossible without Heaven’s help, and walking beside me now was someone who had earned that heavenly luck after years of painstaking effort.

“Zhuge Clan, assemble.”

His blazing red hair fluttered in the wind.

His solid frame was made of taut muscle, and he stood nearly seven feet tall. His voice was as heavy as an iron club.

*…I really can’t get used to this.*

Could a person really change this much?

No matter how long I stared at him, I couldn’t help feeling strange.

The Fire King Jeok Cheongang I knew had been a short, impossibly old man who stood barely five feet tall. He had looked like he could hardly grow any older—not like a fit middle-aged man who appeared to be in his mid-to-late forties.

Jeok Cheongang noticed me staring, stopped walking, and muttered under his breath.

“Why? Why again?”

“No, but seriously. How did this happen? How old were you when you looked like this?”

“I must have been just shy of sixty. Of course, my hair was never red, not even once.”

“How did you get so old, then? I know it’s natural for people to get shorter as they age, but… Did someone cut off your legs when you were around eighty?”

“They weren’t cut off. But if you mean the legs of some bastard who’s been nattering at me since earlier, I might be able to cut those off.”

Jeok Cheongang glared at me, then suddenly smacked his lips.

“Regardless, stop staring at me like that. Even this old man still finds it awkward.”

“Old Master himself finds it awkward, but—no. Calling you Old Master feels weird too.”

“Then what will you call me?”

“Mister?”

“……”

“Hey, Mr. Jeok?”

“……”

“Do you want to fucking die?”

Good. With that murderous way of speaking, he had to be Jeok Cheongang.

As I felt a strange sense of relief, several familiar faces approached and looked between Jeok Cheongang and me with puzzled expressions.

“Huh?”

“Captain, who is the person beside you?”

It was an entirely normal reaction. But Mungyeong and a few others who knew the whole story reacted differently.

“M-my youngest.”

“B-Benefactor. Could the person beside you be…”

Jin Wikyung and Cheongpung grasped the situation quickly.

Jin Wikyung was always the sort of person who remained calm while assessing the circumstances, and Cheongpung was the second-strongest Supreme Peak master among them after Mungyeong. It was hardly strange that they had figured it out.

And then there was the last person, Zhuge Feng, who stared at me with a heavy gaze.

“Red hair and a red beard. According to the reports I received, no martial artist with such distinctive features has entered or left this place until now. What concerns me most is that, judging by the way he is walking beside you, the two of you appear to be quite close. You don’t have any friends, do you?”

“Your words are seriously pissing me off, but you’re not wrong. So?”

“Therefore, using my brilliant intellect, I have reached the conclusion that the martial artist beside you might be Senior Jeok, who has Returned to Youth… Heh. What do you think? Isn’t that a fairly plausible piece of nonsense?”

“He is.”

“No. It’s nonsense.”

“What do you mean, no? I’m telling you it’s true.”

“Please say it’s nonsense. I beg you.”

“It is.”

This time, the answer had not come from me.

With that short, weighty declaration, Jeok Cheongang stepped forward, and the air around us began to tremble.

“Gasp!”

“He’s Returned to Youth?”

“Then could that man truly be…!”

There was a truckload of Wudang and Zhuge Clan martial artists stationed around the makeshift wharf to guard and investigate the area.

On top of that, Ship-Fire Boy Mu Song and the river bandits of Water Dragon Stronghold were there to take us outside.

With everyone around us staring wide-eyed, Zhuge Feng’s pupils shook.

*Why is the Fire King here…?*

That was exactly what his eyes seemed to say.

While everyone else was thrown into an uproar, Zhuge Feng silently looked at Jeok Cheongang, then respectfully raised his cupped hands.

“It is an honor to meet you, Senior. I have been terribly worried, wondering whether something had happened to you…”

“I wondered why those Demonic Cult bastards had come to Mount Jiuhua despite having so many other roads available. So that was the reason.”

At Jeok Cheongang’s razor-sharp tone, Zhuge Feng gave an awkward smile.

“I’m afraid I don’t understand what you mean.”

“Pretend not to know one more time, and you won’t like what happens.”

“May I ask how much you have heard?”

“Starting with, ‘If it hadn’t been for your wise and perceptive grandfather’s judgment.’”

“Ah. So you heard everything.”

“I heard all of it.”

“If I were to say that everything I told you was a misunderstanding…”

“I’ll burn the Zhuge Clan to the ground.”

“Ah!”

“I wondered why those goddamn Demonic Cult bastards had come this way despite having so many roads available.”

Jeok Cheongang slowly clenched his fists, his eyes cold and eerie.

Even when he had looked like an old man who might die at any moment, everyone had backed down whenever he gave them that look. Now that he had Returned to Youth, the force of his aura was enough to make my knees go weak.

“I woke up from my nap and found Mount Jiuhua burning. What do you think of this situation?”

“I don’t think it is a good one.”

“And?”

Zhuge Feng swallowed hard.

“I presume it must have been displeasing.”

“It was fucking awful. If I hadn’t rushed there, even this old man’s residence would have been reduced to ash.”

“Your residence survived, then. That is fortunate.”

“Everything except the residence burned. Including this old man’s heart.”

“Ah!”

“Now, I will give you two choices.”

Jeok Cheongang raised one finger and continued.

“First, I seize every bastard with the Zhuge surname, line them up five abreast, and smack them across the ears.”

*That would be quite a sight.*

While I was thinking that, Zhuge Feng answered without even pausing for breath.

“I will accept the second proposal.”

“Do you know what it is?”

“Whatever it is, I will choose the second one.”

Even I would have picked number two.

One of the things martial artists valued almost as much as their lives was their pride.

If word spread that the entire Zhuge Clan had been slapped in a line by the Fire King Jeok Cheongang, the clan would have to take down its sign from that very day onward.

Even the Zhuge Clan, one of the Five Great Families, would not be exempt.

In that sense, Zhuge Feng had made a wise choice. But even he could not help feeling a trace of unease.

“But what is it?”

“You mean this old man’s second proposal?”

Jeok Cheongang stroked his short red beard. After slowly taking in everyone present, including me, he tossed out a single sentence.

“Do better from now on.”

“Senior, I apologize, but what exactly does that mean…?”

“The war has already begun. So do as well as the Zhuge Clan did during the Great Faction War—no, do even better. Like your grandfather.”

“……!”

“Come to think of it, your grandfather didn’t conspire with the Demonic Cult to order them to set Mount Jiuhua on fire. And getting angry at someone who is already dead and buried is ridiculous. It isn’t as if we can go to his grave and dig it up just to turn it over again.”

Jeok Cheongang looked at me and continued.

“And if those Demonic Cult bastards hadn’t set Mount Jiuhua on fire that day, we would never have formed another connection either… But why do you look like that?”

I hurriedly composed my expression before answering.

“This is my usual expression.”

“……I may have an inkling, but I’ll let it go.”

In truth, if I answered that I had expected him to go to the previous Family Head’s grave and piss on it, Jeok Cheongang would try to kill me.

Judging by everyone else’s expressions, it seemed I was not the only one who had thought of it.

*Still, for him to think this much about it. I’m a little touched.*

As Jeok Cheongang had said, if he had remained a reclusive master in Mount Jiuhua, we would never have ended up working together.

We would have lived in our own worlds, unaware of each other’s existence.

But the pendulum of fate had led me to the Murim and connected me with Jeok Cheongang.

And whether this was fate as well or not, we had to move toward our next destination once more.

*Henan.*

The instant that single word filled my mind, Mungyeong, who had been standing apart with an unreadable expression, suddenly spoke.

“It looks like the sun is about to set.”

The western mountains had already turned red.

And Jeok Cheongang, his hair redder than the western mountains, grinned at me.

“Let’s go now.”

“Yes.”

Right. Let’s go.

To Henan. To the New Murim Alliance.



* * *



“So everyone has left?”

The first person to speak was a refined-looking old Daoist.

His skin was taut and youthful, without a single age spot, and the long hem of his robe was dazzlingly white.

The man who had brought him the news was old as well, but his heavily patched clothes were one indication of his unpretentious character.

Clack.

The shabbily dressed Daoist set down his teacup and answered.

“Yes, Sect Leader Senior Brother.”

The two boys who had studied under the same master since childhood had, before they knew it, become respected Perfected Beings and pillars of Wudang.

Perfected Being Hyeongong, who had loved nothing but martial arts, had reached the Supreme Peak realm and made a name for himself. His Senior Brother, seven years older than him, had succeeded their master and become the Sect Leader of the great Wudang Sect.

He was the refined-looking old Daoist, Perfected Being Hyeoncheon.

“I wanted to meet them at least once before they left.”

At his Senior Brother’s regretful mutter, Hyeongong answered.

“It could not be helped. It was not as if you sent me in your place because you did not wish to meet them.”

“That is true, but I cannot help regretting it. The Two Dragons whom the Jin Family of Taiyuan and Huashan boast of are one thing, but I heard Senior Jeok gained enlightenment as well. I truly should have met him. Sigh.”

“Haha. Please do not regret it too much. We will see him again soon.”

“Yes, I suppose we will. If the contents of this letter are true.”

Hyeoncheon stared down at the letter resting on the table.

Written across the outside of the envelope in a bold, soaring hand were three characters:

**Murim Alliance.**

It was only three characters, but the weight they carried was beyond question.

The Murim Alliance represented orthodox Murim itself. It was also proof that a war rivaling the Great Faction War was approaching.

*Is it truly… beginning like this?*

Hyeoncheon’s expression was heavy.

It seemed as though the screams of the countless Senior and Junior Brothers who had fallen bleeding during the Great Faction War were brushing against the old Daoist’s ears.

The horrific memories he had experienced in his youth were about to repeat themselves.

*This unworthy Disciple finally understands your heart, Master.*

Hyeoncheon was thinking of the master who had died after failing to overcome the injuries he had suffered during the Great Faction War when—

“S-Sect Leader!”

A desperate shout rang out from outside the pavilion.

Hyeoncheon sensed something strange and flicked his sleeve. A soft stream of internal force shot out and flung open the pavilion door.

Hyeongong recognized the familiar face and furrowed his brow.

“You…”

The owner of the desperate cry was a second-generation Wudang Disciple who had been included in the pursuit party chasing the Killing Ghost.

As Hyeongong looked at the second-generation Disciple, who was breathing heavily, his eyes suddenly widened.

“Could it be?”

“Yes. We caught him.”

“Well done! You finally captured the Killing Ghost, who committed such heinous atrocities—”

Hyeongong stopped speaking.

Unlike his own delighted expression, his Senior Brother Hyeoncheon’s face was grim.

And Hyeongong’s suspicion was exactly right.

Hyeoncheon silently stared at the second-generation Disciple, who seemed not to know what to do, then spoke in a low voice.

“We should be celebrating now that the Killing Ghost has been captured, yet your expression is so dark. What happened?”

“Th-that is…”

“Did someone else die or get injured?”

“No. It is not that…”

The second-generation Disciple lowered his head, unable to continue.

“We are bringing the Killing Ghost’s remains here now. I believe it would be best if you saw them and judged for yourself, Sect Leader.”

“What is this supposed to—”

Hyeoncheon’s question did not remain unanswered for long.

Half an hour later, after confirming the true form of the Killing Ghost, whose remains had been carried over by Wudang Disciples, Hyeoncheon remained silent for a long while before finally speaking.

“It seems… I have one more reason to go to Henan.”

Reflected in the old Daoist’s clear eyes was something else entirely—neither beast nor human.
## Chapter artifact 506

# Chapter 506

Fwoooooosh.

A northwest wind blowing in from far away made the sail billow wide.

The rough, muscular river bandits rowed powerfully in rhythm, and the waves splitting to either side of the swiftly moving bow repeatedly formed white foam before vanishing.

*Peaceful, as if nothing ever happened.*

Perhaps because of the many tragedies that had taken place recently, the seemingly endless expanse of the Yangtze looked beautiful today.

As though he had read my mind, Jeok Cheongang, who had been standing beside me, opened his mouth.

“Same shitty scenery as ever.”

“……”

“If I had to name only two things in the world that should disappear right now, they would be Dark Heaven and the Yangtze.”

So much for reading my mind.

What could I say? In many ways, it was nice that he had not changed.

I sighed as I looked at him, his red hair flying in the wind.

“Don’t sigh so loudly. The ground—”

“The ground won’t sink just because I sigh.”

“No. You’ll be dead by this old man’s hand before you even set foot on land.”

“Wow. You keep exceeding my expectations.”

“You seem to have forgotten how to use your eyes since it’s been so long since you last saw me. Your two eyeballs have ‘dis’ and ‘respect’ written on them. What should I do about that?”

“They say ‘re’ and ‘spect,’ actually.”

“Want me to beat some ‘feet-spect’ into you?”

“N. O.”

Whoom—whack!

“Ugh!”

Lightning flashed before my eyes.

At my short cry and the sight of me clutching the back of my head, Jeok Cheongang flinched.

“I-I barely hit you. What a crybaby.”

“Does this look like I’m exaggerating? My skull is ringing.”

“Your skull is… ringing?”

“Even if I’m sturdy, I’m still human. Isn’t that only natural?”

“……Did it hurt a lot? I didn’t mean to hit you that hard. Let me see.”

I let out a quiet laugh at the sight of Jeok Cheongang fidgeting like a puppy that needed to poop.

“Why—why are you laughing?”

“For no reason.”

“……?”

“Ah, I’m all better. More importantly, how long will it take us to reach Henan at this rate?”

At my attempt to casually change the subject, Jeok Cheongang’s face turned bright red.

“H-how dare you toy with this old man!”

Whack!

“Ah, that really hurt!”

“Just take it!”

It hurt. It really did.

And yet, I couldn’t understand why I kept wanting to laugh even while being beaten.

*Maybe I missed this.*

Yes. That was probably it.

There were moments when I missed ordinary things that had once seemed insignificant.

For me, it had been my father’s rough, prickly beard, which had irritated me so much when I was young.

And it had been the palm of Jeok Cheongang’s hand, which had gradually grown slower and weaker.

But it was all right now.

Although my father had died long ago and I could only see him in photographs, Jeok Cheongang, whose body had been gradually weakening, had regained his strength.

Whack!

Feeling the strength and speed Jeok Cheongang had recovered along with his youth made laughter keep spilling from my mouth.

*This is nice, too.*

Whack! Whack! Whaaack!

“……Wait a second.”

“How dare you mock this old man!”

“Ugh!”

Come to think of it, it wasn’t that nice.

There should be a reasonable limit to how much something hurt. This was crossing the line.

The grin I had been wearing like a lunatic had vanished without a trace long ago.

Just as I was desperately twisting my body to avoid Jeok Cheongang’s thick palms, a voice suddenly cut in.

“Um… would it be all right if I came back later?”

Jeok Cheongang’s movements stopped abruptly.

Taking advantage of the opening, I quickly slipped away and hid behind the owner of the voice, using him as a shield.

Caught in the sudden situation, my precious meat shield—no, Ship-Fire Boy Mu Song—cried out in dismay.

“H-hey, Junior!”

“Junior. That sounds especially nice today, Senior.”

“What are you doing?”

“I’m in the middle of inheriting the Stronghold Lord position.”

“If you’re going to get beaten, get beaten alone!”

“You’re supposed to help me at times like this. Don’t you want to become a Senior who looks after his Junior?”

“Why the hell should I—gasp, Great Hero Jeok!”

Unfortunately, the image of Mu Song and me getting beaten together never came to fruition.

His momentum interrupted, Jeok Cheongang lowered his clenched fist instead of bringing it down and smacked his lips as he looked Mu Song up and down.

“Never mind that. What is it?”

Mu Song had squeezed his eyes shut, expecting merciless violence. He hurriedly pulled me away before answering.

“I came because I heard you summoned me. One of my subordinates told me you were looking for me…”

“This old man summoned you? When?”

“I-I was told you had asked when we would arrive in Henan.”

I had been quietly assessing the situation. Now I raised my hand.

“Oh, I think that was me.”

When I had been muttering to myself while pretending nothing was happening, one of the river bandits must have heard me and passed the message on to Mu Song.

“……It was Junior?”

“Yes. I was just thinking aloud.”

“I see. I see.”

Judging by Jeok Cheongang’s grim voice, the river bandit who had passed along the wrong information probably would not escape a taste of the Yangtze today.

I turned toward Mu Song, who was glaring somewhere with a dangerous look in his eyes.

“To be honest, I did want to ask you. When do you think we’ll arrive?”

Although Mu Song was startlingly young compared with the other old martial-world veterans, he was still an experienced river bandit who had spent his entire life on the Yangtze.

After judging the situation for a short while, he opened his mouth.

“We should be able to cut the travel time considerably. If weather like today’s continues, we’ll reach Xixia within ten days at the latest.”

“Xixia?”

Although I had spent plenty of time roaming all over the place, I was nowhere near knowledgeable enough to know the names of every location throughout the land.

In the Murim, I had been too busy to look up every place name. In the modern world, I had tried studying them online, but it was difficult because the place names and the locations of specific sites were different.

*Dongting Lake alone is like that.*

The Dongting Lake right here was in Hubei Province, but on modern Chinese maps, it was located in Hunan Province.

Discrepancies like this were among the decisive proofs that the two worlds were similar, but definitely different.

“Is Xixia in Henan?”

Jeok Cheongang nodded at my question.

“It’s on the southwestern edge of Henan. If this old man remembers correctly, a tributary of the Yangtze ends around there. From then on, we’ll have to travel by land. Is that correct?”

“Yes. You are exactly right, Great Hero Jeok.”

“I passed near Xixia during the Great Faction War. Good. Very good.”

I couldn’t tell whether he was pleased that his memory had become far more accurate after his infirmities of old age had been cured through Returned to Youth, or because we would be able to leave the Yangtze within ten days at the latest.

Perhaps it was both.

With a satisfied smile on his lips, Jeok Cheongang suddenly looked at Mu Song.

“Come to think of it, you’ve had a hard time as well. You went from Sichuan to Hubei, and now you’re going all the way to Henan.”

Mu Song shook his head with a bitter expression.

“How could this be called hardship? Thanks to it, I can lay Uncle Hwang and the countless brothers who died untimely deaths to rest. It’s something I should do, whether anyone asks me to or not.”

After the Water God Dragon fell, Mu Song and the other river bandits of the Yangtze River Channel League gathered the remains of the dead and scattered them across the Yangtze.

They had lived on the Yangtze and died on the Yangtze. It was a fitting end for the river bandits of the Yangtze River Channel League.

“They must be thanking you from the afterlife.”

“Did you say your name was Mu Saeng? For a disciple of the Seafaring King, you have quite decent manners. Yangtze One Saber raised you well.”

“He was like family to me. And my name isn’t Mu Saeng. It’s Mu Song, Great Hero Jeok.”

“Right, Mu Saeng.”

“……”

Had Jeok Cheongang’s infirmities of old age not been completely cured after all?

The thought crossed my mind for a moment, but seeing his bulging eyes made it clear that he was simply being stubborn.

Whatever Mu Song’s actual name was, Jeok Cheongang’s eyes clearly said that if Jeok Cheongang called him Mu Saeng, Mu Song had better change his name to match.

Mu Song swallowed hard under the imposing aura of a master steeped in the Three Bonds and Five Relationships.[^1]

“What? Why?”

“N-no, it’s nothing.”

“Right, Mu Saeng.”

Could anyone else hear the clacking of dentures somewhere?

Unable to watch any longer, I extended a helping hand to Mu Song, who had lost his name.

Actually, I was more interested in asking something that had been on my mind.

“By the way, Senior, are you planning to return to Sichuan?”

“Hm?”

“You know why we’re heading to Henan, don’t you?”

Understanding what I meant, Mu Song’s expression grew somber.

“You’re wondering whether I’ll participate in the Murim Alliance.”

“To be honest, yes.”

“Dark Heaven’s scheme caused the death of the person I revered like a parent, along with countless brothers. What would you do in my place?”

“I’d do whatever it took to avenge them.”

“I feel the same. I want to rush there and lend a hand to the Murim Alliance right now. But…”

Mu Song bit down hard on his lip and continued with a sigh.

“I’m only a Stronghold Lord belonging to the large umbrella of the Yangtze River Channel League. I have no authority to make decisions. Only one person can decide the League’s major matters: my Master and Alliance Leader, the Seafaring King.”

It was common in the Murim, where the strong were treated with respect.

The authority possessed by the Sect Leader of a sect or a Family Head was even greater than that of the owner of a conglomerate family who held ironclad control over a corporation in the modern world.

The problem was—

“Typical of a rootless bandit organization. Then again, expecting anything from men who weighed their profits and losses even during the Great Faction War is ridiculous.”

Yes. That was exactly the part Jeok Cheongang had pointed out.

The Yangtze River Channel League had never been an orthodox faction.

The river bandits scattered throughout the land like grass roots had gathered beneath the banner of the League because of the leadership of a strong man named the Seafaring King and the guarantee of each group’s interests.

*I’ve heard the Green Forest Alliance is the same.*

The Yangtze River Channel League and the Green Forest Alliance had both originated as bands of thieves who gathered to take what belonged to others.

The only reason they had maintained their power and grown even larger was that they had sided with orthodox Murim during the Great Faction War and emerged victorious. As a reward, their activities had been recognized.

They were treated far better than the other unorthodox factions that had survived the Great Faction War, at least.

But that didn’t mean grass roots could become tree roots.

Jeok Cheongang gazed at the waves of the Yangtze with displeasure and muttered,

“Before this old man dies, I hope this goddamn Yangtze dries up and withers away. Then that bastard Seafaring King’s face will be a complete mess. Tsk, tsk.”

“……”

“You should think carefully too, Mu Saeng. Your Master might make the wrong choice.”

“……That seems unlikely.”

Despite hearing his Master insulted to his face, Mu Song did nothing more than offer a bitter smile.

From his reaction, I had a vague feeling that his relationship with his Master, the Seafaring King, was not particularly warm.

*But what would happen if the Yangtze River Channel League and the Green Forest Alliance sided with Dark Heaven at a time like this?*

The answer came quickly.

It would become a real headache.

If Dark Heaven was a blade approaching from the front, those two factions were daggers stabbing in from behind.

If they decided to harbor ulterior motives, even the mighty orthodox Murim would inevitably suffer a blow.

“The Sword Saint is going to have quite a headache. I wonder what those two will choose…”

Jeok Cheongang was muttering as though to himself, apparently thinking along the same lines as me, when a calm voice interrupted him.

“Not two. Four.”

I turned my head.

Mungyeong was standing there with a composed expression.

[^1]: The Three Bonds and Five Relationships are a traditional Confucian framework of social and familial duties.
## Chapter artifact 507

# Chapter 507

I knew Mungyeong was approaching. Seven days and nights of grueling—no, blood-shitting—training had sharpened my usual Qi Sense considerably.

The realm stage displayed by the System had not increased yet, but I could vaguely sense that I would have to break through the wall blocking my path before that happened.

*But what does he mean, not two, but four?*

My question lingered only briefly.

The Yangtze River Channel League and the Green Forest Alliance were both powerful enough that even orthodox Murim could not afford to dismiss them easily. And there was only one place that could be grouped together with those two factions.

Vaguely recalling what I had once heard from Jeok Cheongang, I murmured,

“The Outer Murim.”

The Murim beyond the Central Plains. The Murim outside the Murim.

Some people called the barbarians beyond the Great Wall built by an ancient emperor the Outer Lands, but Jeok Cheongang had always dismissed such talk with a snort.

*“Does the Great Wall surround the whole world? The world beneath the heavens is exactly that—the world beneath the heavens. The lands beneath the sky are boundlessly vast, and each has its own Murim.”*

Whether it was because of his innate temperament or not, Jeok Cheongang’s outlook had been far removed from the stale, old-man Zhonghua chauvinism of his era.

Part of the reason he had gained such insight was the records left behind by previous Sect Leaders, who had indulged their social-butterfly tendencies to the fullest. That was in contrast to Jeok Cheongang, who had been a Lü Bu living at the foot of a mountain whenever he was not active during the Great Faction War.

Though, to be honest, those records were less like documents written for future generations and more like diaries written for their own satisfaction.

*They had been shocking.*

I recalled a few of the records I had read in Fire Gate Cavern.

---

Year xx, Month x, Day x. Cheonbong, Third Sect Leader of the Fire Gate Clan.

I had grown sick of the Central Plains. War continues on all sides, and the Murim is a complete mess. So, to broaden my horizons, I went to India.

After a long journey, I arrived at a river called the Gan… something.

It is not as large as the Yangtze, but it is wide… Anyway, to all the younger disciples of the Fire Gate Clan: if you ever go to India, wash yourselves in that Ganges-whatever river first. Do not ask questions. Do not argue.

I was sightseeing here and there when a group of bald monks suddenly rushed over, shouted things I could not understand, and thrust swords at me. So I beat them senseless.

A Central Plains interpreter who happened to be passing by was horrified and told me that they were from the Small Thunderclap Temple of India.

I had assumed it would be similar to Shaolin Temple from the name alone, but the bald monks here were indescribably violent.

I crippled every monk who came with an even larger gang and burned down every strange-looking temple.

It was quite a pleasant sight.

---

Year xx, Month x, Day x. Songhak, Fifth Sect Leader of the Fire Gate Clan.

I have always held my Grandmaster, the Third Sect Leader, in the deepest respect. Following in his footsteps, I have traveled throughout the world and explored the Outer Murim.

I crossed blades with the Mad Wind Society of the great desert beyond the scorching sands, then traveled to the Potala Palace in Tibet and pulled out its pillars.

As a result, every man and beast in Tibet flew into a rage and chased after me.

But who am I? Songhak, the Ghost Flame Fist and Fifth Sect Leader of the great Fire Gate Clan.

Without suffering so much as a scratch, I… avoided them and returned safely to the Central Plains.

To whoever inherits the Fire Gate Clan’s true legacy in the distant future, remember this well.

If your opponent is one hundred First Rate masters, fight them head-on. If there are one thousand, unleash the Dance of the Fire God and Demon. If there are more than that, live to fight another day.

Of course, if you who are reading this are stronger than I am, just fight them.

Ah, and if you go to that Gan-whatever river in India, jump in and wash yourself immediately. Wash yourself twice.

---

Year xx, Month x, Day x. Gu Jincheon, Ninth Sect Leader of the Fire Gate Clan.

I went to Nanman. I destroyed the Five Poisons Sect.

I went to Persia. I met people who wore something called turbans instead of hero headbands.

They were called Muslims, and they said they believed in a messenger and a prophet.

When I said I wanted to meet the prophet, they told me he was already dead. I could not understand this at all, so I asked several times. They drew their swords.

I had no choice but to send them to the prophet’s side.

Next, I went to the Ice Palace in the North Sea. It was surrounded by nothing but ice and water, so I simply returned.

To the future disciple who will read this, you go.

Ah, and I finally learned the name of that Gan-whatever river. The Ganges River. If you go to India, make sure you wash yourself there first. Be sure to wash.

---

Year xx, Month x, Day x. Han Xin, Twelfth Sect Leader of the Fire Gate Clan.

I am an unworthy Disciple. Following the records of several ancestors, I arrived in India and immediately entered the Ganges River.

While washing my hair, I saw a corpse being carried down from upstream.

I moved to another spot and saw a turd floating past while I was washing my body.

When I went upstream, I saw several hundred people throwing corpses into the river and defecating.

For fuck’s sake, how could you pull this kind of bullshit on me?

---

“……”

Even after thinking it over again, all I could find were astonishing stories.

I only had to skim through the records to see that whenever something displeased them, they smashed their way through anything and everything, whether in the Central Plains or the Outer Murim.

And telling their successors to bathe in the Ganges was no different from a sergeant about to be discharged writing “more field training” on a barracks survey out of pure spite.

In other words: *You get fucked too.*

There were not many more records about the Outer Murim after his shit-water bath in the Ganges left the Twelfth Sect Leader royally pissed off. But once trade routes connecting the Central Plains to the outside world opened, information about the Murim beyond the Central Plains began to flow in.

And the two factions currently coming from Jeok Cheongang’s mouth were precisely the ones that were geographically closest to the Central Plains and most closely connected to it.

“The North Sea Ice Palace and the Nanman Beast Palace.”

Even when I heard them again, the names clearly revealed their respective locations and character.

At Jeok Cheongang’s words, which had finally opened the floodgates, Mungyeong nodded with an infuriatingly bright smile.

“Yes, that’s right. My Master told me. He said he had visited them long ago, and from what he had confirmed, they were in no way inferior to the renowned great sects of the Central Plains.”

“……”

“……”

I would stake everything Hyuk Mujin had on the fact that he had gone there to kill people.

The instant Jeok Cheongang and I exchanged similar looks, Mungyeong’s eyes slowly narrowed.

“Why are you looking at me like that?”

“……Huh? Oh, nothing.”

“Ahem. Nothing at all. You truly are a Divine Physician, rushing anywhere there are patients.”

Naturally, I had to play along. Jeok Cheongang had also received considerable help from him, so he had no choice but to do the same.

As if he had never done anything suspicious, Mungyeong returned to his medical-apprentice persona and continued.

“My Master said that during the Great Faction War, the Demonic Cult tried to recruit those two factions before anyone else. Is that true, Great Hero Jeok?”

“Hmm? Ah.”

Jeok Cheongang answered with a sour expression.

“It is true. To the Demonic Cult, the wicked and unorthodox factions of the Central Plains were branches grown from the same root, so they naturally brought them into the fold. If the North Sea Ice Palace had accepted the Demonic Cult’s offer and moved south while the Nanman Beast Palace moved north, the Great Faction War would have taken a very difficult turn.”

But neither of the two factions accepted the hand extended by the Demonic Cult.

The North Sea Ice Palace declared its isolation from the outside world, as it always had. The Nanman Beast Palace, which was geographically closer to the Central Plains, weighed its options and ultimately sided with orthodox Murim.

“The Beast Palace bastards only intended to pretend to fight at first, but they ended up being quite a great help. Every one of the countless ferocious beasts they brought was worth several First Rate masters, and the messenger eagles the Demonic Cult sent flying throughout the land were captured by Heavenly Eagles trained through the Beast Palace’s secret martial arts.”

The Nanman Beast Palace was practically the public enemy of modern-day animal lovers.

For a very long time, its people had captured and trained every kind of creature living in Nanman’s jungles. They had also created and practiced martial arts modeled after the movements of ferocious beasts.

“Oh, wait. Come to think of it, didn’t you say you were close to someone over there?”

When I asked about the thought that had suddenly occurred to me, Jeok Cheongang frowned.

“Who?”

“The Palace Lord. The Palace Lord.”

“The Palace Lord? Ah, you mean the Beast Miao King?”

“Yes, him.”

The Beast Miao King was both the lowest-ranking and the most unusual of the Ten Kings.

For one thing, he was the leader of the Miao people, the indigenous people of Nanman. For another, he was the master of the Nanman Beast Palace, which could be called the overlord of Nanman.

He had entered the Ten Kings because of his accomplishments during the Great Faction War and his outstanding martial arts. But from the outside, it was almost like an honorary medal given to a foreigner, and perhaps because of that, people within Central Plains Murim were reluctant to mention him.

*Why raise up some southern barbarian when we could just add another member of orthodox Murim?*

That was supposedly how the theory that the Beast Miao King was being overhyped had begun.

“I merely met him face-to-face a few times.”

“But I heard the Beast Miao King even came to pay his respects to you in person.”

“That is true. One day, a black-skinned man with his upper body bare came to my residence in broad daylight. I almost sent a Flame Divine Palm at him.”

For some reason, Mu Song, who had been standing awkwardly with an anxious look in his eyes for a while now, opened his eyes wide.

“Is that really true?”

“Would this old man start making up lies at my age?”

“N-no, that’s not what I meant. I was surprised. My Master has mentioned the Beast Miao King before as well, but I heard that he was short-tempered and arrogant, and showed courtesy only to the Martial God……”

“The Seafaring King? Has that young whelp already gone senile? The Beast Miao King only refused to show him respect because he was such a damned fool. Tsk, tsk.”

Jeok Cheongang clicked his tongue with an expression of utter disdain and continued.

“The Beast Miao King may look that way on the surface, but he knows how to show courtesy when necessary. If he were merely an ignorant man with nothing but brute strength, do you think the Miao people would have gathered beneath a single banner?”

That was something I could only nod along with.

Even small- and mid-sized sects with only a few dozen Disciples vanished and reappeared countless times because they could not find enough Disciples. The Beast Miao King, on the other hand, was a tribal chief ruling over several thousand Miao people at the very least.

“So?”

At my question, Jeok Cheongang stroked his gleaming red beard.

“What do you mean, ‘so’? There was nothing special about it. He came to visit and spoke in a soft, ingratiating tone while bringing up a connection with the previous generation.”

“A connection with the previous generation?”

“Good grief. Have you always been this unworthy a fellow? You should know better than anyone else!”

“Whoa. What’s wrong?”

Our Old Master had suddenly floored the accelerator and rocketed off.

After unleashing a tirade, Jeok Cheongang continued in an irritated voice.

“More than two hundred years ago, the Fifth Sect Leader of our sect destroyed the Five Poisons Sect of Nanman.”

“Why would that…… Ah, could it be?”

“At the time, Nanman was like a cauldron balanced on three legs. The Five Poisons Sect was the strongest, followed by the Nanman Beast Palace, with Poison Valley in last place.”

“So after the Five Poisons Sect was destroyed, the Nanman Beast Palace rose to the top?”

“That’s right. It also absorbed Poison Valley and conquered Nanman.”

“Wow, that’s insane. So that’s how it turned out.”

“For that reason, the Beast Miao King held goodwill toward our sect. It was also one of the reasons he participated in the Great Faction War. But how dare you speak to me informally just now?”

“……I’ll correct myself. It slipped out before I realized it.”

It was impossible not to marvel at how the thug-like behavior of a Sect Leader from generations ago had come back around like this.

But more importantly, the Beast Miao King held goodwill toward the Fire Gate Clan, and because of that, he had sided with orthodox Murim during the Great Faction War……

“The Nanman Beast Palace is probably quite likely to participate in this New Murim Alliance.”

“I can’t say for sure. Even this old man cannot make an easy judgment about that. But if the Beast Miao King I remember is still the same, he will help orthodox Murim.”

“Then what about the North Sea Ice Palace?”

“If the envoy sent from Henan hasn’t frozen to death on the way, they will probably read the letter at least. But it would be better not to get your hopes up.”

The eyes of the seasoned old martial-world veteran, rich in knowledge and experience, turned toward Mu Song.

“But this is the urgent matter right now. What will the Seafaring King do?”

At that moment, Mu Song flinched.

Mungyeong quietly opened his mouth.

“There’s something I’ve been wanting to ask Great Hero Mu Song for a while.”

“Uh, yes?”

Mungyeong silently watched Mu Song’s trembling eyes, then suddenly clicked his tongue.

“You know who I am, don’t you?”

“……!”
## Chapter artifact 508

# Chapter 508

“You know who I am, don’t you?”

“……!”

“……!”

The air around us froze. I doubted my ears, while Mu Song’s pupils trembled.

He had been staring at Mungyeong with an expression like he was about to wet himself. Now he squeezed out a hoarse voice.

“I-I don’t know anything.”

“Is that so?”

Mungyeong stared at Mu Song with a dry gaze.

“Then why are you speaking formally to me, Great Hero Mu Song?”

“……!”

“What a fearless bastard. How dare you lie to me right to my face?”

“Gasp!”

He had fallen for it hook, line, and sinker.

But how had Mu Song figured out Mungyeong’s identity?

*No wonder he kept flinching like a dog that needed to shit.*

Judging by his behavior, Mu Song had known Mungyeong’s identity for some time. But based on the level of martial arts I had seen from him so far, that should have been nearly impossible.

Mungyeong had already reached the realm of Returning to Simplicity and achieved Returned to Youth.

To see through it, someone had to be a master in a similar realm. At the very least, they had to have surpassed the early stages of Supreme Peak before they could sense even the slightest hint of anything unusual.

*Mu Song had noticed that?*

That was absurd. I would sooner believe Hyuk Mujin had taken Cheongpung down with a one-punch, three-teeth combo.

Just as I was pondering the matter, Jeok Cheongang opened his mouth in a bored tone.

“That’s enough. From the fact that the fool kept his mouth shut, it seems he was trying to pretend he didn’t know and let the matter pass. It’s not a good look for an old man to threaten a child.”

“Old man? Threaten?”

Mungyeong let out a derisive snort.

“The old man who was moping around as though he could die any day until yesterday has gotten a little younger and suddenly found his tongue. Outsiders, stay out of this.”

“……What did you say?”

A deep furrow appeared on the forehead that Returned to Youth had made smooth and free of wrinkles.

I hurriedly stepped between Jeok Cheongang and Mungyeong to stop them.

“Wait. Both of you, calm down. Calm down.”

“You, get out of here.”

“Get out.”

“Yes, sir.”

I slipped away without a moment’s hesitation. Mu Song, who had been wedged between the two monsters like a piece of lettuce between sandwich slices, sent me a pleading look.

It seemed to mean, *Save me.*

But was I supposed to let my guts burst in a fight between two whales?

*I need to save myself first. It doesn’t look like they’re about to have a life-and-death duel.*

My judgment was correct. Jeok Cheongang and Mungyeong glared at each other in silence, then lowered their auras simultaneously, as if they had planned it.

“Hmph. I’ll let it pass since you helped me.”

“What an ungrateful old man.”

The two of them exchanged a word each like a pair of prim old men in a nursing home. Then their gazes turned toward Mu Song, who had gone stiff as a stone statue.

“Come to think of it, you’re quite a remarkable fellow. How on earth did you know?”

That was what I was most curious about, too.

I waited for Mu Song’s answer, staring at his lips. But the answer came from Mungyeong instead.

“So it was them. The waterway men who were with you when you moved after the imugi. Or rather, the river bandits of Water Dragon Stronghold, I suppose. Am I right?”

Mu Song swallowed dryly.

“Y-yes, sir. They said the young medical apprentice named Mungyeong was actually a Supreme Peak master with formidable martial arts, and that his standing seemed high enough for him to order even the Zhuge Family Head around…”

*Did that happen without me knowing?*

Actually, when I thought about it, it made perfect sense. There was no way he could have found me by running across the surface of the vast Dongting Lake with Rising on Duckweed, Crossing Water.

*So this is how his identity gets exposed.*

Mungyeong had kept his true identity hidden for decades.

Even after the Sichuan Blood Tragedy, the people who knew his identity could be counted on one hand, including Jeok Cheongang and me, apart from his Disciple, the Divine Physician.

Mu Song did not seem to have inferred that Mungyeong was the Slaughter Saint yet, but from Mungyeong’s perspective, having more people learn his secret could hardly be pleasant.

Jeok Cheongang, of course, did not care about any of that. He looked ready to start eating popcorn right then and there.

“You stupid old man. You should have used a disguise, at least. Ha ha ha.”

“I had no time. Every moment counted while I was going to save your Disciple.”

“……Ahem. I do appreciate that.”

Jeok Cheongang stopped laughing abruptly. Mungyeong clicked his tongue softly and stared at Mu Song.

“I clearly warned you through Sound Transmission, but it seems you have more loyal subordinates than I expected.”

“Gasp!”

At Mungyeong’s chilly voice, Mu Song’s eyes flew wide.

The next moment, a shout so loud that everyone nearby would have turned to look burst out—if a screen of internal energy had not been enclosing the area.

“N-no, you can’t!”

“What can’t I do?”

“My subordinates haven’t done anything wrong! Take my head instead!”

“……Why would I kill you?”

At that moment, Mu Song, Jeok Cheongang, and I all stared at him with our eyes wide.

“What? Ah, you’re not?”

“You’re not going to kill me?”

“That old man’s gone mad—wait. Are age-related infirmities contagious?”

After briefly considering whether infirmities of old age were contagious, Jeok Cheongang shouted with a triumphant expression,

“I see now! This old man has figured it out! Instead of killing him, you’re planning to cripple his dantian or cut off one of his limbs!”

“……!”

Mungyeong looked at us with trembling eyes and muttered in a voice filled with regret,

“I can feel the urge to kill rising on its own.”

Mu Song spoke with an expression that mixed fear and resolve.

“My subordinates are innocent. Please, be satisfied with taking only me…”

“Please shut your mouth before I tear it apart.”

“Gasp. Yes, sir.”

Mungyeong looked down at Mu Song with an utterly incredulous expression, then sighed.

“Six, including you. Correct?”

“Y-yes, Senior. We have all been together for many years, and they know how to keep their mouths shut.”

“I have never had a junior like you, and I am no longer a martial artist. But if you fail to keep them quiet, I can make all six of you disappear without leaving a trace.”

“……!”

“If you want to live out your natural span in peace, you would do well to seal those mouths forever. Do not tell the Seafaring King—or anyone else. Understood?”

Mu Song pressed his lips together and gave a small nod. Mungyeong jerked his chin toward the rear of the ship.

“Go. And tell your subordinates not to come anywhere near the stern until we reach Henan.”

“What?”

“Why? Is there something else you want to ask?”

“N-no, sir. If you need anything, please call for me at any time.”

Mu Song bowed deeply and hurried away.

That left three of us: me, Jeok Cheongang, and Mungyeong.

Jeok Cheongang smacked his lips, his face full of disappointment, and poked me in the side.

“It would be more fun if that fool went around blabbing to everyone. Don’t you agree?”

“I adm—cough.”

I hurriedly buried the word *admit* in a cough.

Mungyeong was glaring at us with an expression that said he was having absolutely no fun at all. He looked ready to grab the nearest person and beat him senseless just because what he had overheard was so irritating.

“I didn’t say anything.”

“Neither did I. Unless you have something to feel guilty about?”

“That’s not it. I was just giving you a little advance notice.”

“That’s why I was wondering whether to give you a little advance beating.”

“I really didn’t mean anything.”

“I heard you say ‘admi.’ What came after that?”

At times like this, panicking was the worst thing I could do. I calmly opened my mouth.

“I meant, ‘Admittedly, I have a conscience. How could I do such a thing?’”

“That doesn’t sound like what you said.”

“But it’s true.”

“No, it isn’t.”

“It is. Why are you playing Gung Ye?[^1]”

Mungyeong clearly did not know what Gung Ye was, but he had realized that it was not a compliment.

I deliberately ignored his suddenly chilling gaze and hurriedly changed the subject.

“By the way, why did you tell him not to go anywhere near the stern?”

“Don’t change the subject.”

“……”

I was completely speechless.

When I awkwardly shut my mouth, Mungyeong clicked his tongue.

“You’ve done well raising a man like this as your Disciple.”

Jeok Cheongang, who had been watching with his arms folded as though none of this concerned him, let out a quiet laugh.

“That’s exactly why I raised him.”

“You raised that utterly ill-mannered man?”

“Is that so? I thought we were close enough not to stand on ceremony. It seems we see things differently. Or perhaps someone is deliberately ignoring that thought.”

Mungyeong silently looked back and forth between Jeok Cheongang and me, then muttered,

“……You’re as smooth as flowing water. Returned to Youth, and now only your mouth has gotten lively.”

I had no idea what kind of conversation this was supposed to be.

Just as I was staring blankly, unable to follow its flow, Jeok Cheongang pushed himself away from the wooden railing of the swift ship.

“I should go into the cabin. Looking at this goddamn river is getting tiresome.”

“Wow, that’s excellent news. Are you sure your surname isn’t Zhuge instead of Jeok?”

That was the best thing I had heard all day.

But the moment I took my first step to follow him, Jeok Cheongang blocked my way with his hand.

Thud.

“Huh?”

“‘Huh?’ What do you mean, ‘huh’? Why are you following me?”

“You said you were going to the cabin.”

“So?”

“I was just about to go there myself.”

“How can two men fit inside that cramped cabin?”

“It’s a five-person cabin in the first place. Where did your conscience—”

“I’m going there to circulate my qi and organize the enlightenment I’ve gained recently. There’s no need for you to follow me.”

“Oh, you’re going to circulate your qi. Then I’ll stand guard—”

“Not necessary. Stay here.”

“What?”

When I asked again, Jeok Cheongang suddenly shouted.

“I said stay here!”

“Whoa, you startled me. Why are you shouting?”

“Shut up. If you follow me, you’ll be in for it!”

“……?”

I stared blankly at Jeok Cheongang as he walked away. Then I slowly turned my head at the prickling sensation of someone’s gaze.

I met Mungyeong’s stare. It was drier than the sand near a Sphinx’s forepaws.

*Fuck. I should have followed him.*

What did it matter whether Jeok Cheongang caught hell or rang a bell?

Rather than remain alone with a man who might cut off my head, I would have been better off jumping into the vast Yangtze—

“The river looks unusually clear today. Don’t you want to go in?”

“What?”

What the hell was this mind-reading? Was he actually Gung Ye?

A suspicion suddenly flashed through my mind. Without thinking, I looked around for a palace guard carrying a mace.

That was when—

Whoom!

A mace came swinging at me.

No. It was a single, swift, and stealthy wave of palm force.

I hastily crossed both arms to block it when the sound of splitting air pierced my ears, but the palm force fired by a once-in-an-age master known as the Slaughter Saint was not something I could block so easily.

Boom!

*Fuck, that really is like getting hit with a mace.*

I felt a dull pain in my chest as I was blasted off the swift ship.

Just before I plunged into the water, I twisted my body around, sent the internal energy in my lower dantian into my legs, and stepped onto the surface of the river.

Splash!

The calm surface exploded violently, as though I had stepped into a puddle.

I stood upright using Rising on Duckweed, Crossing Water, then glared at Mungyeong with an incredulous expression.

“What are you trying to do all of a sudden?”

“The calm river has been disturbed.”

“What does that even—what?”

“I mean your rough movements look as though they might cause a storm.”

I had no time to say anything else. Mungyeong looked at me and clicked his tongue softly before continuing.

“Then… we should begin.”

> **System**
> 
> - Linked Quest **Fake Murim Martial Artist—Stage 2** has begun!

[^1]: Gung Ye was a Korean ruler traditionally portrayed as claiming to read people’s minds.
## Chapter artifact 509

# Chapter 509

Ding.

> **System**
>
> - Linked Quest **Fake Murim Martial Artist—Stage 2** has begun!
> - This Quest will proceed forcibly regardless of whether it is accepted!
> - Quest forcibly accepted!

“……?”

*What the fuck?*

It seemed my thoughts had shown plainly on my face. Mungyeong’s eyebrows twitched as he looked at me.

“I clearly told you there would be another training session. Don’t tell me you forgot?”

“Excuse me?”

*Forgot what? Is he messing with me right now?*

Dumbfounded, I looked back at Mungyeong.

“How could I forget after shitting blood so many times? Even thinking about it makes my asshole twitch.”

“……I understand, so stop there. You’re disgusting.”

“Ha. Seriously.”

The head might forget, but the asshole—no, the body—remembered.

Even now, whenever I closed my eyes, memories of shitting blood day and night came flooding back.

To exaggerate a little, if all the bloody liquid I’d passed over the past seven days and nights were collected in a tub, every mosquito in Hubei Province could gather for a feast.

*It was horrible.*

No matter how hard I tried to forget those memories, they refused to disappear.

The same went for the Linked Quest the System had announced on the day of my last duel with Mungyeong.

It had not been long ago, and it was far too important to forget. If I had forgotten it, I would have had to question my sanity.

“Anyway, I haven’t forgotten. I remember every single thing you said back then.”

“Is that so?”

Mungyeong stared at me intently.

“Then your reaction makes even less sense. I even warned you in advance. Why do you look as though someone just hit you in the back of the head?”

“……Uh.”

*Because it really does feel like I was hit in the back of the head.*

I knew another training session was coming, but I had been certain that it would not happen right now.

There was only so much he could teach me aboard this swift ship, which was even narrower than an ordinary vessel.

*At most, a cultivation technique?*

But a cultivation technique, the foundation of martial arts and internal energy, was not something that could be swapped out as easily as a machine part.

*Especially not in my case.*

The Fire Gate Divine Technique was the very root of the Fire Gate Clan.

Because it focused on transforming the nature of internal energy into fire qi and amplifying its power, the cultivation technique played a far greater role in the Fire Gate Clan’s martial arts than it did in those of other sects.

Mungyeong of all people could not possibly be unaware of that fact.

I asked, just in case.

“Um, you’re not planning to teach me a cultivation technique, are you?”

Whoosh! Slash!

I turned my head at the sound of the wind. A throwing blade shot past like a streak of light, missing my neck by a hair before slicing through the river behind me.

“……I heard your answer loud and clear.”

“Don’t waste my time with that kind of nonsense.”

“Of course. I was just asking on the off chance.”

*Then what is it? Another poison-tasting session?*

A sense of foreboding and curiosity struck me at the same time, but I decided to put it aside for now.

Not for any particular reason. Mungyeong had simply grown much farther away before I knew it.

Whoosh!

The favorable wind and the presence of waterway men who were thoroughly accustomed to sailing certainly helped, but the swift ship was unquestionably several notches faster than an ordinary vessel.

We had barely exchanged a few words, yet he had already gotten that far. I almost wondered whether the bastards from the Yangtze River Channel League had installed a motor.

*Damn, it’s fast.*

Even a model student who routinely came first in the entire school was bound to have at least one weak subject.

For me, it was movement techniques.

As befitted a Supreme Peak master, I was able to keep following him using Rising on Duckweed, Crossing Water, but I was not accustomed to it, and it consumed a considerable amount of internal energy.

Besides, unlike Dongting Lake last time, there was nothing here I could step on as I moved.

“I’ll climb aboard first and listen. I can’t keep staying like this.”

Mungyeong readily nodded.

“Do that.”

“You’re not going to throw a hidden weapon at me as a surprise, are you?”

“Stop talking nonsense and come up.”

“Yes, sir.”

I gathered the internal energy I had drawn up and concentrated it in my toes.

The greatest advantage of the Fire Gate Divine Technique was its ability to draw out explosive force. A single leap would be more than enough to get me back onto the swift ship.

*One, two.*

*Now.*

Bang!

The internal energy released from my toes slammed into the water. The river surged upward like a massive wall from the shockwave, and a fierce wind swept across my entire body.

In a moment so brief it could not even be called an instant, I covered over a hundred feet and landed on the stern of the swift ship—

Thwack!

*What the fuck?*

I was sent flying at a speed even greater than when I had first closed the distance. I hurriedly sent internal energy through the soles of my feet and flipped my body around.

As my body plunged headfirst toward the water, I regained my balance and barely managed to stand on the surface.

*What is this? Déjà vu?*

I looked at Mungyeong, who stood tall on the stern, with a thoroughly displeased expression.

“What was that just now?”

“What was what?”

“That thing in your hand. You hit me with it.”

“Oh, this.”

Mungyeong shook the large object in his hand.

“This is an oar. It is mainly used to row a boat.”

“I wasn’t asking because I didn’t know that.”

“I thought you were.”

“Didn’t you promise not to do anything strange?”

“To be precise, I said I wouldn’t throw a hidden weapon. This is not a hidden weapon.”

“Oh, I see. You used a lethal weapon instead of a hidden weapon.”

“Something like that.”

*Is he insane? Seriously.*

Mungyeong stared at me with a profound gaze. No—with a profound gaze at the water rippling around me.

“The Yangtze River is still calm, yet chaos breaks out wherever your feet touch.”

“If you keep pulling stunts like this, I’ll be the one making a scene. Seriously.”

“Do you know why this happens only to you?”

“I don’t know that, but why are you doing this?”

Mungyeong ignored my question and continued.

“It is not because your movements are clumsy and rough.”

“You’re making my personality rough.”

“The movements of a master who has reached a certain realm each have their own reason and meaning. In your case, the cause is that your internal energy itself is too violent. That is one of the chronic problems of the Fire Gate Clan’s martial arts.”

“Ah, now I’m pissed. I’ll climb aboard again, so put down that oar first and—”

I stopped halfway through my sentence.

I had realized this was not merely a case of Mungyeong being spiteful or playing a prank.

“Wait. What did you just say?”

“At last, your ears seem to have opened. I said that the reason your movements are rough on the water is a chronic problem with the Fire Gate Clan’s martial arts.”

*A chronic problem…*

This was not something I could casually dismiss.

After thinking for a moment, I opened my mouth again.

“What does that have to do with Rising on Duckweed, Crossing Water? I’m simply clumsy because I’m not accustomed to it. Aren’t you judging too quickly?”

“You fool. It is not that simple.”

“You mean…”

“The stability and precision of your internal energy.”

“Stability and precision…”

“Rising on Duckweed, Crossing Water is merely one measure of those two qualities. The more stable and precise a person’s internal energy is, the more freely they can perform it. Though it is an advanced movement technique, even among Peak masters, those with deep attainment can perform it without much difficulty.”

Mungyeong continued without pause, then suddenly leaped down from the stern.

The distance was great enough that an ordinary person would not have been able to distinguish his features properly. But with my extremely keen senses, I could see and hear him clearly.

I saw Mungyeong land on the surface of the water as lightly as air.

I heard no splash.

Not even a ripple rose from the water, as though nothing had happened.

Mungyeong’s dry gaze turned toward me.

“What about you?”

“……!”

I instinctively lowered my head and looked at the water beneath my feet.

But there was no point. The path I had taken while chasing the swift ship was covered in white foam, as though another ship had passed through it.

Splash.

Dozens of ripples overlapped one another around the cautious step I took.

Even with Mungyeong as the comparison, the difference was simply too extreme.

“You seem to know the answer yourself.”

I would have been less embarrassed if his voice had contained disdain or mockery.

But when I heard Mungyeong’s toneless voice, which seemed to say, *Yes. That is about your level,* my face heated up.

“Do you understand the meaning of what I said now?”

“……I think I understand it to some extent.”

As Mungyeong had said, Rising on Duckweed, Crossing Water was an important measure of the stability and precision of one’s internal energy.

Depending on how well a person distributed and controlled their power, the water beneath their feet could churn as though caught in a storm or remain as still as an unfrequented lakeshore.

“Then tell me, in your own words, what you should gain from this.”

“Hmm. I’ll be able to handle my internal energy more efficiently.”

“I do not like that answer.”

“Besides stability and precision, I’ll be able to reduce my internal energy consumption while producing the same amount of force.”

“That is a little better. But it is still lacking.”

With one second stretching into a minute, I thought hard. Then, suddenly, I parted my lips.

“Amplification.”

“Explain further.”

“What I said earlier describes the conditions needed to produce the right amount of force in the right place at the right time. And if I can control my internal energy that precisely… it also means I can amplify it more powerfully than I do now.”

“So?”

“Rather than simply pursuing stability and precision, the power of the martial arts I’ve learned will become even stronger. Is that right?”

Mungyeong stared at me in silence before tossing out a single remark.

“……You are not a complete idiot.”

*That’s it. I got the answer right.*

But the reason I felt a strange thrill was not because I had received a small measure of Mungyeong’s approval.

*If I can complete this training successfully, I can become stronger than I am now.*

At present, I was in a kind of stagnant state.

Perhaps it was because I had grown too quickly. The martial arts that had once advanced by leaps and bounds had stagnated at some point, and I could feel a tall wall blocking my path.

But with this method, I could make technical progress even without gaining some new enlightenment.

*So there was still plenty of room for me to grow without enlightenment.*

When had I begun thinking incorrectly?

I had failed to consider filling in what I already had and instead kept wanting something newer and greater.

*What a stupid thing to do.*

It was like owning a one-terabyte external hard drive, filling only five hundred gigabytes of it with porn, then whining that the storage was insufficient.

Mungyeong had shown me exactly that.

*You still have another five hundred gigabytes of porn—no, another five hundred gigabytes left to fill. There’s no reason to buy another external hard drive when you still have capacity.*

*Ah, Great Lord Mun.*

A halo seemed to shine over Mungyeong’s shoulder.

At the sight of my eyes brimming with those feelings, Mungyeong opened his mouth.

“Watch where you’re looking before I gouge your eyes out.”

“……Ah, yes.”

“Anyway, you seem to have finally grasped the general idea.”

“Yes. I think I understand.”

“Then you have also figured out what kind of training you should do from now on, correct?”

Of course I had. I gave the answer I had expected.

“Rising on Duckweed, Crossing Water. Am I right?”

“That is correct. Experiencing something directly with your body is better than hearing and thinking about it a hundred times. And the Yangtze is the perfect place, so begin immediately.”

So that was why he had knocked me into the water without warning. He must have been planning this from the beginning.

But I was not annoyed or indignant.

Nothing could be gained without paying a price.

*It’s a little daunting with nothing but river all around me, but I’ll get used to it if I keep practicing.*

Having finished my thoughts, I answered without the slightest hesitation.

“Understood.”

“You are more obedient than I expected. Keep that attitude from now on.”

“Yes.”

If it meant becoming stronger than I was now, what wouldn’t I do?

I bowed my head toward Mungyeong, then realized I had forgotten the most important question.

“Um, by the way.”

“Hmm?”

“How long do I have to do this?”

“What a foolish question.”

Mungyeong spread both hands, looking as though he could not understand why I would ask something so obvious.

*Ten stars… no, ten shichen?*

“W-wait a minute. Even for me, ten shichen is impossible. As you know, I have to follow the swift ship using Rising on Duckweed, Crossing Water, and if I do that, the internal energy consumption will—”

“What are you talking about? Ten days.”

“Excuse me?”

“Not ten shichen. Ten days. Follow me the entire way until we reach Henan.”

“……Excuse me?”

The instant I froze like a stone, a familiar notification pierced my ears.

Ding.

> **System**
>
> - The training method for **Fake Murim Martial Artist—Stage 2** has been newly established!
> - The Instructor has set the training period to **10 days**! This period may become shorter or longer depending on how long it takes to reach the destination!
> - The countdown begins now! Hang in there—argh!
> - **Time limit:** 9 days 23 hours 59 minutes 59 seconds.

“……”

*Fuck. I have no words.*

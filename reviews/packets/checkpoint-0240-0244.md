# Checkpoint Review — 240–244

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

# Chapters 240–244

## Plot

Jeok Cheongang reaches the Five Qi Returning to Origin realm, and he and Jin Taekyung leave the Nangong estate for the Star-Array Grand Banquet after Nangong Cheon enters seclusion. Nangong Cheon tells Namgung Ryong that Taekyung is a Hidden Dragon with the Heavenly Martial Physique and that Jeok is the dragon pearl who recognized him. He has mastered nine-tenths of the Emperor’s Sword Form, while Taekyung has withstood all three of his moves. He orders Namgung Ryong to keep Nangong Ok away from the banquet.

On the road to Henan, Jeok and Taekyung interrupt Black Mountain Stronghold’s ambush of the Geumwa Merchant Group. Heuk Jongpil and his bandits are later found defeated, with Heuk Jongpil beheaded by an unidentified master in One Strike. Jeok then separates from Taekyung, taking his coin purse and going alone to Shaolin. He orders Taekyung to remain away until the Kaifeng preliminary competition.

Taekyung struggles to find lodging while dressed in rags, meets the unusually friendly Jongni Chu, and learns rumors that Nangong Ok will not attend the banquet. At a cloth shop, Hyuk Mujin intervenes when the staff mistake Taekyung for a beggar, only to be recognized and ordered to put his head on the ground. Taekyung reunites with Jin Wikyung at the Jin Family’s rented estate and learns that Lee Seowol is rebuilding the Mount Heng Sword Sect, Wolhwa is establishing an entertainment city, and Cheongpung disappeared while being escorted toward Huashan. Jin Mukyung remains in closed-door training until he achieves Great Completion.

Jang Taebo’s completed spear reaches Taekyung through Hyuk Mujin. After another year in the Fire Gate Cavern, Taekyung reaches the sixth stage of the Scorching Sun Divine Arts and uses the spear, White Flame, to break the shackles and chains that have bound him for a year. He travels to Mount Song with Wikyung, Hyuk Mujin, and fifty Jin Dragon Squad members. The Star-Array Grand Banquet begins before tens of thousands of spectators, with Jeok, Hong Dao, and leaders of the major Murim powers present. Jeok trades provocations with Gong Iljung and the Thunderbolt Saber King of the Hebei Peng Family before the assembled leaders appear before the crowd.

## Continuity

- Jin Taekyung has reached the sixth stage of the Scorching Sun Divine Arts after approximately a year in the Fire Gate Cavern.
- White Flame is Taekyung’s approximately two-meter spear, forged from Ten-Thousand-Year Cold Iron by Jang Taebo.
- Taekyung has removed the Ten-Thousand-Year Cold Iron shackles, chains, and iron ball that bound him during training.
- Jeok Cheongang has reached the Five Qi Returning to Origin realm; his dementia and infirmities of old age remain unresolved.
- Nangong Cheon has mastered nine-tenths of the Emperor’s Sword Form, has not reached Great Completion, and regards Taekyung as a Hidden Dragon and Jeok as the dragon pearl.
- Heuk Jongpil is dead after an unidentified master defeated him in One Strike; the surviving Black Mountain Stronghold bandits were turned over to the authorities.
- Song Ho, the Thousand-Faced Fox, took the Geumwa merchants away for questioning about the unidentified young master.
- Jeok has gone alone to Shaolin and ordered Taekyung not to follow until the Kaifeng preliminary competition.
- Jongni Chu is a young Peak martial artist from Yunnan who calls himself the Always-Victorious Sword and is pursuing friendship with Taekyung.
- Hyuk Mujin is Vice Squad Leader of the Jin Dragon Squad under Wipeng; he and Wikyung accompanied Taekyung to Mount Song.
- Cheongpung disappeared after fleeing while being escorted to Huashan with the Three Plum Blossom Elites.
- Jin Mukyung has remained in closed-door training for roughly one year and six months and will not leave before achieving Great Completion.
- The Star-Array Grand Banquet is underway at Mount Song. Jeok Cheongang and Hong Dao are attending, along with Gong Iljung, the Thunderbolt Saber King, and other major Murim leaders.
- Gong Iljung is Sect Leader of the Zhongnan Sect and the Senior Brother of the Roaring Fury Swordsman.
- The Thunderbolt Saber King of the Hebei Peng Family is a long-standing rival of Jeok Cheongang.
- Open hooks include Jeok’s worsening illness, his visit to Shaolin, the reason Nangong Ok was barred from the banquet, the identity and purpose of the master who killed Heuk Jongpil, Cheongpung’s whereabouts, Jin Mukyung’s breakthrough, and the Jin Family Head’s unexplained absence.

## Translation Decisions

- Render 오기조원 as Five Qi Returning to Origin, 잠룡 as Hidden Dragon, 대성 as Great Completion, and 제왕검형 as Emperor’s Sword Form.
- Use White Flame for 백염.
- Use Always-Victorious Sword for 상승검 and Jongni Chu for 종리추.
- Use Thousand-Faced Fox for 천면호리, Yeoahong for 여아홍, and Red-Killing Axe for 적살부.
- Use Vice Squad Leader for 부대주 and Jin Dragon Squad for 진룡대.
- Use Gan Jiang and Mo Ye for 간장 and 막야.
- Use Wind-and-Cloud War God for 풍운전신 and Wind-and-Cloud Sword Lord for 풍운검군.
- Use Virility Saber King for 정력도왕 and Thunderbolt Saber King for 벽력도왕.
- Use Put your head on the ground for 대가리 박아 and Yes, sir! Yes, sir! for 존명존명.

## Durable state

{
  "active_continuity": [
    "Jin Taekyung has reached the sixth stage of the Scorching Sun Divine Arts after approximately a year of training in the Fire Gate Cavern.",
    "White Flame is Taekyung's approximately two-meter spear, forged from Ten-Thousand-Year Cold Iron by Jang Taebo.",
    "Taekyung, Jin Wikyung, Hyuk Mujin, and fifty Jin Dragon Squad members are traveling from Taiyuan to Mount Song for the Star-Array Grand Banquet.",
    "The Star-Array Grand Banquet has begun at Mount Song, with Jeok Cheongang and Hong Dao among the attending senior Murim figures.",
    "Gong Iljung is the Sect Leader of the Zhongnan Sect and the Senior Brother of the Roaring Fury Swordsman.",
    "The Thunderbolt Saber King of the Hebei Peng Family is a long-standing rival of Jeok Cheongang."
  ],
  "continuity_sources": [
    244
  ],
  "open_questions": [
    "Where has the Jin Family Head been during his years of unexplained absence?",
    "When will Jin Mukyung achieve Great Completion and leave closed-door training?",
    "Where did Cheongpung go after fleeing on the way to Huashan?"
  ],
  "safe_through": 244,
  "temporary_decisions": [
    "Use Vice Squad Leader for 부대주 and Jin Dragon Squad for 진룡대.",
    "Use Gan Jiang and Mo Ye for 간장 and 막야.",
    "Use Put your head on the ground for 대가리 박아 and Yes, sir! Yes, sir! for 존명존명.",
    "Use White Flame for 백염.",
    "Use Wind-and-Cloud War God for 풍운전신 and Wind-and-Cloud Sword Lord for 풍운검군.",
    "Use Virility Saber King for 정력도왕 and Thunderbolt Saber King for 벽력도왕.",
    "Use Repentance Cave for 참회동."
  ],
  "version": 1
}

## Reading copies

## Chapter artifact 240

# Chapter 240

Smoke rose from the old man’s seven apertures.

It was Scorching Yang Qi so dense that it could be seen with the naked eye, endlessly coiling around his small frame and circulating without pause.

And then, soon after—

Sssssss.

Five rings rose one after another above the crown of the old man’s cross-legged body.

Some were blue and red, while others were black and white.

When the final yellow ring took shape, a vivid ring in the five colors of the five directions was complete.

Five Qi Returning to Origin.

Jeok Cheongang, the small-framed old man who had displayed the dream realm desired by every martial artist in Murim, suddenly opened his eyes.

“Come in.”

The door opened as soon as the words left his mouth.

A young man dressed in rags entered without hesitation, as though he owned the place, and looked around.

“Weren’t you circulating your qi?”

“There was some bastard pacing outside the door. Do you think this old man could concentrate with him distracting me?”

“Fair point. Ah, I should’ve just come in and watched the Olympics.”

“It wasn’t the Olympics, or whatever you called it. It was Five Qi Returning to Origin.”

“What does it matter? As long as you got the meaning across.”

Jeok Cheongang gazed silently at the young man, Jin Taekyung.

“Where have you been?”

“You know where. I went to see Great Hero Namgung Ryong, the Family Head.”

“The Family Head of the Namgung Family. Right. You did.”

After muttering under his breath, Jeok Cheongang asked,

“What did he say?”

“Oh, that.”

Jin Taekyung stretched and continued.

“They said the banquet was canceled.”

“The banquet was canceled? What does that mean?”

“Well, apparently the Azure Sky Sword King entered seclusion.”

“Seclusion?”

“They say he suddenly gained some minor insight or something. Anyway, that’s how it turned out.”

“Enlightenment…”

Jeok Cheongang gave a small nod.

“How curious.”

Jin Taekyung, who had been twisting the thick hairs of his beard around one finger, stopped.

“What is?”

“The Azure Sky Sword King had waited more than twenty years for today. Yet, of all days, this happened today. How could it not be curious?”

“……Maybe he got a little nervous when it was finally time to fight you?”

“Who knows?”

“Come on, I know exactly what happened. Don’t you think you’re overthinking it?”

“You think so?”

“Yes. Absolutely.”

Jeok Cheongang silently stared at Jin Taekyung, who was nodding vigorously.

“W-why?”

“No reason.”

“There’s no such thing as ‘no reason’!”

“Do I need your permission just to look at your face once?”

“Have you never heard of image rights?”

“I haven’t. Shut your mouth before I use a lightness technique to stomp on your head.”

“Yes, sir.”

But the silence did not last long. Jin Taekyung glanced around to gauge the old man’s mood before speaking again.

“Old Master.”

“What?”

“This whole thing worked out okay, right?”

“There is nothing to call ‘working out.’ The date has merely been postponed for a little while.”

“But we bought some time.”

“Did you think this old man would lose?”

Jin Taekyung hurriedly waved his hands.

“That’s not what I meant. Given the situation, even if you win, it wouldn’t really count as a victory.”

Even if I win, it wouldn’t really count as a victory…

Jeok Cheongang repeated the words silently.

They were true. If the duel had taken place, he would have suffered a serious blow regardless of the outcome.

The Azure Sky Sword King was an opponent who would have to fight with everything he had.

If Jeok Cheongang suffered an Internal Injury in a fierce duel against him, the essence, qi, and spirit he had barely managed to bring into balance would collapse.

“Old Master?”

Jeok Cheongang, who had fallen into thought, raised his head. Jin Taekyung was looking at him with concern.

“Why did you call me?”

“No reason. Do I need permission even to call you once?”

“What a tiresome brat.”

Under normal circumstances, Jeok Cheongang would have rapped him on the head. But today, he decided to let it slide.

He gave a quiet snort of laughter and rose from his seat.

“Let’s go.”

“Where?”

“Henan.”

The Star-Array Grand Banquet.

Even now, the most renowned masters of Murim would be gathering in Henan one after another.

After spending a full cycle of four seasons, they had taken a rather long detour to get there.

“The Nangong Family has no reason to keep us here, and we have no reason to remain. Leaving is only natural.”

“Leaving sounds good, but can’t we soak in some hot water before we go? I’ve got so much dirt on me that my body feels heavy.”

“You should have brought that up much earlier. Don’t pretend to care about cleanliness now. Go out and get some travel money. We are unwelcome guests, but they should at least do that much for us.”

“Wow. Now you’re even telling me to shake people down.”

“Hey, you!”

“I’m going. I’m going.”

Grumbling, Jin Taekyung left the pavilion.

He did not know that Jeok Cheongang was silently watching him.

Watching the shackles that had been hastily forced shut.

Watching the sharply cut ends of his sleeves.

The old man watched the young man’s back as it disappeared into the distance, then muttered,

“……That brat. He did something I never even told him to do.”

His seasoned gray eyes swept toward a small mountain in the distance.

A faint cloud of dust was dispersing above the ridge covered in blue-green light.

* * *

The bright sun disappeared behind the mountain, and darkness descended.

Standing motionless as the mountain wind brushed between the trees, the old man, the Azure Sky Sword King Nangong Cheon, suddenly opened his mouth.

“Who was that child?”

Namgung Ryong, the Family Head of the Nangong Family, was standing quietly behind the Azure Sky Sword King. He answered,

“They say he is Jin Taekyung of the Jin Family of Taiyuan, Shanxi.”

“The Jin Family of Taiyuan?”

“Yes.”

“So a Hidden Dragon was crouching in the borderlands.”

“And the Fire King took that very Hidden Dragon under his wing.”

“You’re wrong.”

The Azure Sky Sword King shook his head.

“The Fire King is the dragon pearl. It wasn’t that he took the Hidden Dragon into his embrace. He became the dragon pearl himself.”

“……!”

Namgung Ryong could not hide his astonishment. Their relationship might have been a bleak one between father and son, but he knew his father well.

One of the things he knew was that his father was a man of few words who was exceedingly stingy with his judgments of others.

Yet the word Hidden Dragon had come from his lips.

He had even said that the Fire King, Jeok Cheongang, whose name shook all under heaven, had become the dragon pearl himself.

*The man who had never once praised even his own grandson…*

Along with a pang of hurt, curiosity rose in Namgung Ryong’s heart.

“Is he really that extraordinary?”

The Azure Sky Sword King did not answer his cautious question. Instead, he abruptly asked one of his own.

“How far have you mastered the Emperor’s Sword Form?”

“……I still haven’t broken through the barrier of three-tenths mastery.”

“At your age, this father had achieved seven-tenths mastery of the Emperor’s Sword Form. I believe it was around then that the world began calling me the Sword King.”

“I apologize.”

His answer was filled with shame, but the Azure Sky Sword King did not care.

He had not said it to rebuke his son, who was now sixty years old.

“More than twenty years ago, when my proficiency in martial arts reached eight-tenths, a question suddenly occurred to me. I wanted to test my sword.”

“……”

Namgung Ryong silently lowered his head. He knew well what had happened afterward.

The clash between the Fire King and the Sword King.

The winner of that earth-shaking battle between two Supreme Peak masters had been the Fire King.

“During my secluded training, I faced countless towering walls. I struck and hammered at them endlessly, and at last, one of those walls collapsed.”

“Then…!”

“I barely crossed one wall. I have not yet achieved Great Completion.”

“Congratulations!”

Namgung Ryong bowed deeply to his father and trembled.

The Emperor’s Sword Form was the beginning and end of the dozens of secret arts possessed by the Nangong Family.

In the history of the family, only its founding Family Head had ever achieved Great Completion of the Emperor’s Sword Form.

True to his greatness as a martial artist, the Azure Sky Sword King had become the first in roughly a century to reach nine-tenths mastery of the Emperor’s Sword Form.

“Congratulations, is it?”

But the Azure Sky Sword King’s expression remained calm. No—he even looked hollow.

“Then let me ask you one thing. Can you withstand three moves of the Emperor’s Sword Form this old man unleashes?”

“How could I possibly dare… Surely?”

The Azure Sky Sword King quietly nodded.

Namgung Ryong’s eyes widened until they were as large as lanterns.

It was something that should never have happened and could not have happened.

Yet his father had confirmed it: the young man had withstood the Emperor’s Sword Form unleashed by none other than the Azure Sky Sword King himself.

Even Namgung Ryong, who rarely lost his composure, spoke with a trembling voice.

“B-but he is only twenty-two years old.”

“Yes, twenty-two. He possesses the Heavenly Martial Physique and has the Fire King Jeok Cheongang as his Master.”

The Azure Sky Sword King raised his head and stared at the dark night sky.

For many long years, from the moment he first entered the world, he had lived under the name Nangong. He had carried the two characters *Azure Sky* in his heart and learned a sword that resembled the azure heavens.

But today, he had met a dragon surging into the sky.

*I thought one move would be enough.*

He had poured two-tenths of his strength into his sword, intending to teach the young man a thorough lesson.

Then came three-tenths.

Then six-tenths.

And yet…

“Three moves. That’s it, right? Thanks for going easy on me.”

The young man had slung the iron balls over his shoulder and left.

All that remained where he had departed were hundreds of trees and rocks hewn down, one sword stroke after another, and the sorrowful cries of birds that had suddenly lost their homes.

*A Hidden Dragon. A Hidden Dragon.*

The Azure Sky Sword King repeated the single phrase in his mind before opening his mouth.

“Have they left?”

Namgung Ryong, who had only just gathered his wits, answered,

“Yes. They left five shichen ago.”

“Where did they say they were going?”

“Henan. They said they would attend the Star-Array Grand Banquet held there in one month.”

“The Star-Array Grand Banquet?”

The Azure Sky Sword King let out a hollow laugh.

“Tell your son in no uncertain terms not to show his face at this Star-Array Grand Banquet.”

* * *

The Black Mountain Stronghold was a bandit organization located at one of the major routes connecting Henan and Anhui.

Its leader, Heuk Jongpil, was an illiterate former butcher. But he was a natural-born plunderer and a master who had honed his axe techniques to the Peak realm.

Thanks to that, he commanded more than three hundred underlings and could lord it over them like a king.

*Of course, the Green Forest Alliance took nearly all of it from him.*

No matter how capable Heuk Jongpil was, he could never defeat the Green Forest Alliance.

The only reason he had been able to grow the Black Mountain Stronghold into what it was today was that he paid four-tenths of his profits to the Green Forest Alliance every month in exchange for various forms of assistance.

For instance, the valuable information delivered by the subordinate who had just entered.

“Boss, a letter has arrived from the Green Forest Alliance headquarters! Here—”

Whack!

“You bastard! Don’t you know I can’t read at all? Read it aloud!”

“It’s information about the goods being transported by the Geumwa Merchant Group and the route they’re taking. They say it should arrive within two days.”

“What are you waiting for?”

“Yes?”

“Call everyone!”

The Star-Array Grand Banquet was an important event for martial artists and bandits alike.

Heuk Jongpil gathered all three hundred of his underlings and set up an ambush along the route the Geumwa Merchant Group would take.

*Let us catch one big haul. Just one.*

If they managed to get even a single top-grade cat’s-eye stone, they would still have a fortune left over after paying tribute to the Green Forest Alliance.

Feeding and arming more than three hundred able-bodied men was no small task.

“They should be arriving soon… Why haven’t the scouts come back?”

“Who knows? We sent them out a shichen ago, but there hasn’t been any word.”

“Ugh. Trying to run a bandit operation with idiots like these is hard on the body. Hard on the body.”

The next moment, Heuk Jongpil’s grumbling body went rigid.

With a trembling hand, he pointed toward something approaching from the darkness at an incredible speed.

“……Hey. What is that?”

“I-I’m not sure either.”

Whoooosh!

Two silhouettes—one large and one small.

A long streak of red qi remained in their wake, like the tail of a meteor shower.

*Are they ghosts?*

Heuk Jongpil was crouching in the grass and watching the scene when it happened.

The two silhouettes, which had been racing along the mountain road at an unbelievable speed, abruptly came to a stop.

Soon, low voices drifted over.

“What’s with the meddling?”

“It feels wrong. They seem to be in the same group as those two who were skulking around earlier.”

“We’re going to be late at this rate, you brat.”

“No matter how late we are, whoever sees trash first should be the one to clean it up.”

“Where did you learn to talk back to this old man every single time I say something?”

“People like that always set fire to mountains.”

“You little shit! Go break all four of their limbs.”

“Yes, sir.”

Heuk Jongpil had been listening intently to their conversation.

His eyes flew open.

“W-we’re fucking screwed! Everybody—!”

But his cry could not continue.

Whoosh!

A short gust of wind.

Then someone’s enormous hand wrapped familiarly around his shoulder.

“Everybody, what?”
## Chapter artifact 241

# Chapter 241

The Star-Array Grand Banquet.

With the most renowned masters in the world gathering in one place to pit their martial arts against one another, the name truly could not be more fitting: a banquet of stars.

An old man with deep wrinkles around his eyes packed tobacco into a long-stemmed tobacco pipe as he spoke.

“It could also be called a festival of victory.”

The place was a large inn in the southern part of Henan Province.

From among the people crowding around the old man, someone asked,

“Why is that?”

“Why else? If the Central Plains Murim had lost, would there have been a Star-Array Grand Banquet? The Demonic Cult would have ruled the world by now, and they would be holding the Demonic Grand Banquet instead.”

“Ah, that is true.”

“But because we won, the Star-Array Grand Banquet can be held, and the great sects from across the world can gather in one place to strengthen their resolve. Speaking of which…”

The old man fumbled around inside his robes, then waved his pipe.

“Does anyone have a light?”

The middle-aged man beside him quickly pulled out a flint and lit it for him.

Crack, crackle! Ssssss.

As the dry grass burned, the old man puckered his lips. After blowing out several streams of smoke, he leaned back leisurely in his chair.

“If there is anything you are curious about, ask me anything. This old man will tell you everything he knows.”

The people whose eyes had been shining eagerly began raising their hands all at once.

“Me! May I ask first?”

“Great Hero Song, then perhaps…”

“Hey, didn’t you hear me say I was going first?”

“I didn’t hear shit, you unorthodox-faction bastard!”

Wham! Crash!

Fists flew in an instant, and a table broke apart. The onlookers cheered at the sudden fight.

The guests who had been sitting well away from the old man shook their heads.

“Tsk, tsk. Martial artists.”

“Just let them be. It’s not as if this is the first time we’ve seen it.”

“That’s the problem—they never get a moment of peace. With the Star-Array Grand Banquet right around the corner, every kind of bastard is flocking to Henan.”

“Our trading run is over anyway. We might as well watch the show and enjoy the benefits.”

Two merchants chatted quietly.

They were wearing fine-looking blue silk robes and passing cups of liquor between them when a voice suddenly cut in.

“Is that Yeoahong[^1]?”

[^1]: Yeoahong, literally “Daughter’s Red,” is a traditional Chinese rice wine.

“Hm?”

The merchants stared at the owner of the voice with bewildered expressions.

A young man had somehow approached their table without them noticing. He was flaring his nostrils as he stared intently at the cups in their hands.

“Isn’t that Yeoahong? It looks like it…”

“It—it is. Yeoahong.”

“I knew it.”

As though he had achieved some great enlightenment, the young man slapped his knee and dragged over an empty chair.

“But the color looks a little weak. How much did you pay for this bottle?”

His actions were so smooth and natural that the merchants could only stare blankly at each other.

“H-how much was it?”

“T-two silver nyang.”

The young man sighed.

“What a shame.”

“What do you mean, a shame?”

“This is mixed with water. Can’t you tell at a glance? Looks like the owner played a little trick on you.”

“What?”

The merchants’ eyes flashed.

Was Yeoahong normally that expensive?

Two silver nyang was enough to buy two seom of rice and drink strong liquor like water for several months. Mixing water into it was nothing short of outrageous.

“I’m going to—”

One of the merchants was about to spring to his feet, but his companion stopped him.

“Forget it. Nothing good will come from making a fuss. Besides, aren’t we taking advantage of people a little at a time in times like these?”

“Ugh.”

The merchant groaned and sat back down.

Meanwhile, the young man was filling his cup to the brim with Yeoahong and gulping it down.

Gulp, gulp, clack!

“Ahh. That’s good.”

The merchants had been staring at him dumbfoundedly. Only after a moment did they finally come to their senses.

“What do you think you’re doing?”

“That’s our liquor…”

“My throat was a little dry, so I tried a cup. Is there some problem?”

His answer was so shameless that the two men were speechless. They only managed to speak after the young man had emptied his third cup.

“Have we met before?”

“Of course.”

“When? Where?”

“Today, here.”

“……”

“They say even brushing sleeves with someone creates a connection. Let’s be friends from today.”

“Friends?”

The merchants glared at the young man in disbelief.

He was slender and had an approachable expression. He looked no older than his mid-twenties—just a ridiculously young brat.

*What the hell does he mean, friends?*

They were about to give him a proper tongue-lashing when they noticed the iron sword tucked into his waist.

*A martial artist!*

People had always said that there was barely a difference between a rogue and a martial artist.

They were also separated from the guards accompanying their merchant group. If a dispute broke out, they would unquestionably be the ones to suffer.

The merchants swallowed the reprimand that had been about to leave their mouths.

“Hey, Young Brother.”

“Young Brother? I like that form of address.”

“R-really? That’s good, then.”

There was something strangely relaxed about the young man’s grin. Forced smiles appeared on the merchants’ faces.

“Are you a martial artist too, Young Brother?”

“Hmm. I have learned some trifling tricks people call martial arts.”

*What? He learned ‘tricks’ called martial arts?*

*The brat’s already drunk on his own swagger.*

The merchants cursed him inwardly before speaking.

“You must be a future pillar of the martial world. If you don’t mind, may I ask which sect you are a Disciple of?”

“Does that matter between friends?”

The young man artfully dodged the question, so one of the merchants revealed their own identity.

“We are merchants belonging to the Geumwa Merchant Group.”

“The Geumwa Merchant Group?”

“It is nothing to boast about, but we are one of the top three merchant groups in Zhejiang Province. We came a long way to deliver supplies needed for the Star-Array Grand Banquet being held three days from now.”

The other merchant, who had been nodding beside him, eagerly added,

“We even brought a hundred merchant-group guards.”

“Warriors as brave as tigers.”

*We aren’t alone. Get lost before you get taught a lesson.*

The words carried an unspoken threat, but the young man paid no attention.

More precisely, he was so absorbed in his own thoughts that he let their words go in one ear and out the other.

“The Geumwa Merchant Group… I definitely heard that name this morning.”

The young man thought hard for a moment, then exclaimed,

“Ah!”

“Isn’t that the group that captured hundreds of bandits?”

“That’s right.”

The merchant who had answered with his chest puffed out mumbled an additional clarification.

“To be precise, we didn’t capture them. We picked them up.”

“Picked them up? What does that mean?”

When the young man showed interest, the merchants lowered their voices as much as possible.

The events they had gone through before encountering this young brat were far more troubling.

“Well, there were a bunch of bandits lying in the alley the merchant group was passing through, all with broken legs and groaning. As it turned out, they were from Black Mountain Stronghold, which is notorious in the area.”

“Their leader, the Red-Killing Axe Heuk Jongpil, had been turned into a headless corpse.”

“Oh?”

The young man rubbed his smooth, hairless chin.

“So what did you do?”

“What else could we do? We couldn’t exactly kill them all, but leaving them there would have been like throwing silver nyang onto the road. So we tied them all up in a line.”

In the end, the Geumwa Merchant Group handed the remnants of Black Mountain Stronghold over to the authorities and collected a huge bounty. The rumor spread quickly.

“People have been saying all kinds of things. That they angered a hidden master, that a war broke out between bandit strongholds…”

“It probably was a hidden master. How many people can kill a Peak master like the Red-Killing Axe in One Strike?”

The young man listened quietly, then asked with keen interest,

“With One Strike?”

The two merchants nodded together.

“That’s right. You’re a martial artist too, so you must know how remarkable that is.”

“What was it? The underlings said whoever it was had chunks of iron dangling all over them. It was so late at night that they couldn’t see their face properly. They just saw a flash, and then the Red-Killing Axe fell.”

“Hmm.”

The young man fell silent for a moment, as though considering something. Then he suddenly spoke.

“That hidden master must be much younger than you think.”

“Good heavens. Do you have some idea who he might be?”

“More or less. He was probably dressed shabbily, with his hair all over the place.”

“Oh! Who was he? Who is that master?”

“But I don’t know his name.”

“……”

“Well, I suppose I can get to know him little by little from now on. Thanks for the drink.”

It happened in an instant.

After tossing out that one remark, the young man rose from his seat and disappeared into the bustling crowd.

Soon, the inn’s door closed with a tinkling bell.

“What was that?”

“Did he really leave? After gulping down all that Yeoahong?”

“He called us friends. Damn it.”

The two merchants stared at each other blankly when someone spoke to them.

“Excuse me, gentlemen.”

“What is it?”

A broad-shouldered waiter held out a wooden tablet with an impassive expression.

There were scars across his face, enough to make one suspect that he moonlighted as a dark-path knife fighter.

No, with a face like that, it was practically certain.

“The gentleman who just left didn’t pay his bill. From what I just heard, it seems you two are friends.”

“Huh?”

“Two roast ducks and five bottles of Yeoahong. The total comes to ten silver nyang and twenty nyang in iron coins.”

“……!”

The merchants’ mouths fell open as though they had been struck squarely in the back of the head.

*What the fucking hell?*

*He drank five bottles of Yeoahong?*

But what could they do? If you could tell ten things from one, then the waiter’s face made it clear that this establishment was managed by a dark-path faction.

The merchants were rummaging through their coin purses with miserable expressions when—

“I’ll pay.”

Clink.

A silk pouch flew from somewhere and landed on the table.

The people inside the inn had fallen silent. Through the crowd, which had split cleanly down the middle, an old man came limping forward.

Tap, tap.

The sound of a wooden prosthetic leg striking the floor pierced everyone’s ears.

“Twenty silver nyang. Use it to pay the bill and get me a quiet room.”

The waiter looked back and forth between the silk pouch and the old man, then bowed politely. He already knew who the man was.

“Yes, Great Hero Song.”

“Well, that settles one matter.”

The old man wrapped his rough hands around the merchants’ shoulders.

His strength was so great that it was impossible to believe he was a man in his seventies. He seized the two men and hauled them to their feet.

“Now, the two of you and I are going to have a little talk. About that friend who just left.”

“Why, why are you doing this?”

“We have absolutely nothing to do with him!”

The old man smiled broadly at the two merchants, who were almost whimpering. But he could not hide the deeply sunken look in his eyes.

“Heh heh. Isn’t that something for this old man to decide?”

At the words of Song Ho, the Thousand-Faced Fox, the merchants drew a sharp breath.

* * *

As if to announce that the Star-Array Grand Banquet was only three days away, every street in Henan Province—and even every inn—was packed with people.

The problem was that, thanks to that, there was not a single inn left for me to stay in.

“We have no rooms.”

I had already been turned away from more than twenty inns.

With nowhere left to go and no reason left to retreat, I glared at the waiter and asked,

“You’re sure there really isn’t one?”

“I told you, there isn’t.”

“I have money.”

I pulled out a filthy silver coin and held it up. It was my entire fortune and my last hope.

If I hadn’t secretly hidden it away in advance, I wouldn’t even have this.

Jeok Cheongang had run off with my entire coin purse.

*Damn old man.*

At the very first inn we entered, Jeok Cheongang had been showered with salt by the waiter. After agonizing over whether to set the waiter or the inn on fire, he had come up with a peaceful and spectacular solution.

The Abbot of Shaolin card.

*I’m going to Shaolin.*

*Wow. That option was available? Was dementia the driving force behind becoming a genius?*

*Shall I use that driving force to snap your neck?*

*I shouldn’t have run my mouth. Anyway, that’s great. Let’s hurry there, scrub the dirt off with hot water, and eat some Shaolin wild-greens bibimbap.*

*I’m going alone.*

*What?*

*A year ago, you ran your mouth about going to the Star-Array Grand Banquet, and this old man suffered for it despite having no reason to. The preliminary competition will be held in Kaifeng anyway, so don’t let me see your face until then.*

*No way! How is that fair?*

*Oh, and hand over your coin purse.*

*Why do you need my coin purse?*

*The Fire King has his dignity to consider. Do you expect me to arrive looking like a beggar and eat and bathe for free? I should at least be able to make a small donation.*

*……*

*Oh, and if you come looking for Shaolin, I’ll kill you. Understood?*

He wasn’t the Fire King. He was a highway robber. A highway robber.

After having my coin purse stolen right in front of my eyes, I stood there blankly for a long while before wandering aimlessly in search of a place to sleep.

And this was the last inn anywhere nearby.

“This is real silver. Want to bite it and see?”

The heavily built waiter scowled.

“……Didn’t you just pull that out of your underwear?”

“I was hiding it.”

I quickly rubbed the silver coin with my sleeve before holding it out again.

“Want to bite it?”

“Get the hell out of here, you filthy beggar!”

*You son of a bitch…*

I considered punching him in the face, but turned away weakly.

Nearby, several children were huddled together playing jacks with small stones.

“Kids, do any of your families run a guesthouse?”

The chubby-cheeked children shook their heads.

“N-no.”

“My family does, but it’s already full.”

“Oh, I see. All right.”

“And my mom said not to bring in beggar bastards like youuu.”

“……”

*Listen to the way that little brat talks.*

I wanted to storm into his house and shout at his parents to teach him some proper manners, but I held myself back.

*Where do I go now?*

I was slowly walking through the streets, wondering whether I should go wash myself in a nearby stream, when someone called out.

“Young Hero!”

At first, I didn’t realize they were calling me. Given my current appearance, it was far too absurd to think that someone would address me as a Young Hero.

My clothes were no better than rags, and my hair was a tangled mess. At that moment, I was an excellent specimen of a beggar.

At least I had avoided looking like a prisoner by winding the chains around my body and covering the whole lot with cloth.

But who would call someone like me a Young Hero?

“Me?”

When I turned around, I saw a young man with an approachable expression smiling brightly.

“That’s right. You.”
## Chapter artifact 242

# Chapter 242

He was a young man with an approachable expression.

He looked to be in his mid-to-late twenties at most, and there was a strangely friendly smile playing around his lips.

“Whew. Why are you walking so fast?”

“Do I know you?”

“No.”

“Then why?”

“They say even brushing sleeves with someone creates a connection, don’t they?”

“We haven’t even brushed sleeves.”

“But we exchanged words, so that counts. Let’s be friends.”

“……”

It was one of two things. He was either crazy or a crazy social butterfly.

I took my time looking the young man over. Beneath his loose robe, I spotted well-developed muscles, as well as the hilt of a sword poking out from his waist.

At the same time, I sensed the qi lying dormant within his body.

*A Peak master?*

I had no idea how old he actually was, but his attainment was fairly impressive.

No, at this level, it could even be called remarkable. Reaching the Peak realm in your twenties was no easy feat.

But how should I put it? At that moment, the qi I sensed from the young man before me seemed to amount to no more than that.

If I had to put it into words…

*An ordinary Peak master?*

The Peak realm was already an incredible level, so why did he feel ordinary? Because I was surrounded by too many monsters.

After getting hit by the insane three-hit combo of Jin Mukyung, Cheongpung, and the Fire King, side effects like this were bound to develop.

Regardless, I had more or less figured him out. I spoke politely to the young man.

“Don’t worry about me. Go on your way.”

“Good heavens, isn’t that too cold between friends?”

“If we’re friends, can I drop the formal speech?”

“Haha. Of course!”

“Then fuck off, asshole.”

“……”

I left the young man behind and started walking. After standing frozen for a moment, he hurried after me with quick little steps.

“That was the first verbal abuse I’ve ever heard in my life. It stunned me for a moment. Yes, this is what true friendship is!”

“Go while I’m still asking nicely.”

“What’s your name?”

“Michael Johnson.”

“That’s an unusual name.”

“……You believe that?”

“Jang Sam? Or Yu Pil? Are you perhaps a Disciple of one of the Nine Sects and One Gang or the Five Great Families?”

“Why are you curious?”

“Because I’m interested, of course. I heard you killed the Red-Killing Axe with One Strike.”

I stopped dead at the unfamiliar epithet.

“Who?”

“The leader of Black Mountain Stronghold. Was that your doing?”

I recalled the hairy bandit chief I had dealt with on the way here. He had been the first one I took out to establish dominance, since there had been so many bandits.

I had thought he was unusually strong for a bandit. It seemed he had actually been somewhat famous.

“But how did you find out?”

“I heard it from the Geumwa Merchant Group’s merchants at the inn earlier. They said the surviving bandits claimed it was the work of a strange man carrying iron balls and chains.”

The young man beamed as he pointed at the iron balls strapped to my back.

I had covered them with cloth to disguise them as luggage, since I did not want to attract any strange misunderstandings. But it seemed I could not fool the eyes of a Peak master after all.

“And then you happened to walk by. My curiosity got the better of me, so I followed you right away.”

“Hmm.”

“So, what’s your name?”

Should I tell him or not?

After a moment’s thought, I opened my mouth. I was beginning to grow curious about which sect this eccentric young man belonged to as well.

“Jin Taekyung. That’s my name.”

“Are you the Jin Taekyung of the Jin Family of Taiyuan in Shanxi Province?”

“You know me?”

“Of course I do. I’ve heard so much about the Sleeping Dragon of Shanxi becoming the Fire King’s Disciple that my ears are ringing.”

A year was short if you looked at it one way, and long if you looked at it another.

But it was more than enough time for rumors about me and the Fire King to spread throughout the continent.

“What about you?”

“Ah, I am…”

The young man grinned and continued.

“Jongni Chu. I’m Jongni Chu from Yunnan. I have my reasons for not revealing my sect, so I hope you’ll understand.”

“Jongni Chu from Yunnan?”

“My epithet is the Always-Victorious Sword. Have you ever heard of me?”

I knew the name of Yunnan, but this was my first time hearing his name or epithet.

Considering I had spent the past year holed up in Fire Gate Cavern, that was only natural.

“Sorry, but I haven’t.”

“Is that so? Well, it’s understandable that you wouldn’t know.”

What a positive attitude. Normally, someone around his age would be disappointed, but he showed no such signs at all.

The freakishly positive guy continued with a serious expression.

“That’s because I just came up with the epithet. A swordsman who always wins. Isn’t it cool?”

“……”

*Is he crazy?*

As I stood there speechless, Jongni Chu made a motion of twisting his wrist.

“How about it? Shall we have a drink to celebrate becoming friends?”

“Not interested. Besides, there aren’t any seats at the nearby inns.”

“What are you talking about? I’ve been following you and watching the whole time. Every inn had at least one or two seats open.”

“……The waiters said there were no seats.”

“Hm? Then why did they tell me there were empty seats and invite me in?”

“……”

Damn it. Of course.

Even with the Star-Array Grand Banquet right around the corner, was it really possible for every single seat in dozens of inns to be taken?

*I’m washing because I’m filthy. Because I’m filthy.*

I would have to draw water from a stream and wash myself. At this rate, I would end up sleeping on the street despite leaving perfectly good inns unused.

“I know a decent inn, so come with me. I’ll pay for the drinks to celebrate becoming friends.”

“What do you mean, friends? You said your name was Jongni Chu, right? You go on your way too.”

It was not as though I was a penniless beggar. I had no desire to get entangled with some strange man and waste time chatting.

Hadn’t I heard that a stream ran straight ahead along this road?

As I searched my memory and walked on, Jongni Chu asked,

“Hey, where are you going?”

“None of your business. Don’t follow me.”

“Then answer me one last thing! Where can I see you again?”

“The Star-Array Grand Banquet.”

That was my final answer. I used light-body arts and quickly left the area. After covering a distance of more than a hundred zhang in an instant, I heard Jongni Chu shouting behind me.

“See you next time!”

*Not a chance, punk.*

* * *

One man left, and one man remained.

Jongni Chu stared in the direction Jin Taekyung had disappeared and muttered,

“The Sleeping Dragon of Shanxi, Jin Taekyung…”

Before long, dimples appeared in the smooth skin around his mouth, which was entirely free of wrinkles.

He stood there alone for a while, chuckling to himself, then turned toward an inn not far away.

A quarter-hour earlier, the waiter who had driven Jin Taekyung away bent at the waist with a broad smile.

“Welcome!”

“Do you have any seats left?”

“Of course, sir!”

Jongni Chu’s smile grew even wider.

* * *

Splash!

When I sat up, the hot water filling the wooden tub sloshed around.

I had picked up the battered wooden tub after finding it lying in the grass. Then I had filled it with cold stream water and heated it using Scorching Yang Qi.

After dumping out and refilling the water several times to scrub away the accumulated grime, I felt as if I had lost several kilograms.

“I feel like I’ve undergone Bone Transformation.”

I finally felt alive again.

It would have been nice to have shampoo or body wash, but this was more than enough to satisfy me.

The inventories for the Murim and modern worlds were separate, so bringing those things here had been impossible from the start.

*But these clothes are a problem.*

As soon as I put the rags back on—the kind of clothing that made it difficult to tell whether they were clothes or garbage—I frowned.

The discomfort was one thing, but at this rate, washing myself had been completely pointless.

I wandered through the streets, intending to buy at least one cheap set of clothes.

The streets of Henan had been crowded with people from all walks of life and every profession even a year ago, but given the timing, martial artists were especially conspicuous now.

Naturally, snippets of their conversations began to reach my ears.

“Have you heard? The Sword Dragon of the Nangong Family won’t be participating in this year’s Star-Array Grand Banquet.”

“Good heavens. Why did the Sword Dragon suddenly drop out? Is there some problem?”

“Who knows? It’s a shame. He was one of the strongest candidates to win. Things are getting harder and harder to predict.”

“Among the young rising martial artists, the Ten Dragons and Phoenixes probably have the best chance, but…the age limit is thirty-five. It’s impossible to say what will happen.”

“That’s a fair point. The world is vast, and there are many masters. There’s always a chance that a rising powerhouse from outside the Nine Sects and One Gang or the Five Great Families will appear.”

“You mean someone like the Heaven Shaking Sword of the Jin Family of Taiyuan and the Sleeping Dragon of Shanxi?”

“Exactly. Though I don’t know whether either of them will attend this year’s Star-Array Grand Banquet.”

Listening to this was embarrassing for no reason.

I quickened my pace and left the road behind.

As soon as I reached a main street lined with large buildings, a cloth shop displaying silk and dozens of kinds of clothing caught my eye.

“Excuse me.”

“Wow, they say clothes make the man, but they suit you so well. Are you perhaps a fairy? A fairy…what do you want?”

The cloth-shop employee, who had been enthusiastically showering pretty female customers with flattery, frowned at me when I called out.

The change in his expression was so extreme that I barely managed to resist punching him in the face.

“Why do you think I came to a cloth shop?”

“To beg, obviously.”

“……”

No matter how ragged my clothes were, there was no way to hide my massive frame.

No, more of my body was exposed than covered, so my muscles stood out even more.

When I stared at him while subtly tensing my body, the employee flinched.

“W-why are you looking at me like that? Was I wrong?”

“That’s enough of the kind of remark you’ll regret. Let’s look at some clothes.”

“Y-you want clothes?”

“Here, I have money, so don’t treat me like a beggar.”

The employee’s expression changed when I pulled out a silver nyang and waved it around.

Contrary to my expectations, it changed in a very bad direction.

“That’s all?”

“It is. Is there a problem?”

“Good grief. What kind of clothes do you think you can buy with one lousy silver nyang?”

“……One lousy silver nyang?”

Had there been a major currency reform in the past year that caused the price of silver to collapse?

As I stood there momentarily confused, the employee snorted.

“Did you even read the price list before coming in?”

I turned around without thinking and checked the sign.

A wooden board at the front of the shop had these words written across it in huge letters:



> **The owner has gone mad. Star-Array Grand Banquet special discount! Martial-artist’s outfit—two silver nyang!**

“……Two silver nyang? For a martial-artist’s outfit?”

“With that, you can buy underwear at best. Our cloth shop only handles the finest silk. Even our martial-artist’s outfits are made from Shu brocade.”

“……”

*So this was a department-store brand.*

Of all the places I could have entered, I had chosen this one. What an embarrassment.

The other employees and customers inside the shop began whispering as they watched me.

“Oh my, he must be a beggar. How pitiful. Don’t you agree, dear?”

“He certainly looks like one. He seems strong enough to put his muscles to good use, though. Should we take him in and use him as a servant while we’re at it?”

“You’re so merciful, dear. That beggar must be delighted.”

It was irritating enough when they simply called me a beggar, but hearing a couple say something like that made me twice as angry.

I shouted with all the anger I could muster.

“Who are you calling a beggar?”

“Gasp!”

“Eek!”

“H-how dare you!”

People recoiled in fright at my booming shout.

At the same time, several burly employees came rushing over from somewhere and surrounded me. The clubs in their hands waved threateningly.

“You bastard! How dare you make a scene here!”

“Do you even know where you are, you filthy beggar?”

“What? A beggar? Oh, these sons of bitches…”

*Fine. You said it.*

I rolled up the sleeve that was already half torn off.

“All right, let’s be a real pain in the ass today. Who’s the owner here?”

That was when it happened.

“You’re the kind of bastard who won’t come to his senses until he sees a coffin. How dare you make a scene here?”

A serious voice cut into my ears.

I slowly turned around, and a man came into view.

He wore a deeply pulled-down bamboo hat and black silk clothes embroidered with dragons. One hand rested on the hilt of his sword, as though he might draw it at any moment.

The edge of his mouth, visible beneath the bamboo hat, lifted in a quiet laugh.

“You seem to have learned a move or two somewhere, but if you don’t want to see blood, step aside.”

I tilted my head to one side.

“And if I don’t?”

“Nameless martial artist. The price of reckless bravado is death.”

When a line that sounded like it belonged in a martial-arts movie came out, the people nearby erupted in cheers.

Once the cheers had died down, I opened my mouth.

“Hey, can I ask you one thing?”

The martial artist answered casually,

“Speak. They will be your last words.”

I stared into the shadow beneath the martial artist’s bamboo hat and continued.

“You’re Hyuk Mujin, right?”

“……!”

I let out a deep sigh and looked up at the sky. A signboard written in vigorous, soaring calligraphy caught my eye.



Hyuk Family Cloth Shop



“You have three seconds. Put your head on the ground.”
## Chapter artifact 243

# Chapter 243

Hyuk Mujin had been living through days that felt like a dream. Every now and then, he even pinched his own cheek.

*“Mujin, are you really allowed to be this happy? This isn’t a dream, is it?”*

He had every reason to feel that way.

Just over ten years ago, he had been nothing more than a boy who admired martial artists.

*“No, I don’t need to go back that far.”*

Even two years ago, he had thought his life was a cesspool.

His work hours were long and boring, and his martial arts had stagnated.

If the person he encountered most often on top of all that was a drunken, good-for-nothing Third Young Master, then anyone who wasn’t the Buddha would have looked at the world pessimistically.

*“I held it in and held it in, then finally threw one punch.”*

The day he drove his fist into the Third Young Master’s jaw, Hyuk Mujin’s life changed.

Countless battles, one death-defying crisis after another…

The Third Young Master—or rather, his Captain—was like a magnet that drew every danger in the world toward him.

Hyuk Mujin fought through the dangers flying at them from every direction alongside him, and when he finally came to his senses, he discovered that he had grown tremendously.

*“Ohhh, power! Power is surging through me!”*

*“…Patient, come over here. Your crazy spell has flared up again, so it’s time to get punched.”*

Bam! Ba-ba-bam!

He had been hit an awful lot, too. There had even been times when he secretly set out a bowl of pure water and prayed without Jin Taekyung knowing.

*“Please, please don’t let the Captain hit me anymore. Just take him far away from me.”*

Had his prayer been answered?

One day, Jin Taekyung left without warning.

As Hyuk Mujin watched him depart with the Fire King, he felt both sad and liberated.

And at last, the prime of his life arrived.

*“You’re Hyuk Mujin?”*

*“Gasp! Great Hero Wipeng, how do you know me…”*

*“Draw your sword. Let’s see what you can do.”*

He began receiving instruction from the Peak master known as the Ghost Sword, Wipeng.

*“Did you say the Jin Dragon Squad?”*

*“That’s right. It’s where the family’s finest are gathered. I’ve been appointed its Squad Leader.”*

*“Wow! The Jin Dragon Squad! Congratulations!”*

*“Pack your things.”*

*“Pardon?”*

*“You’re the Vice Squad Leader. This is our lord’s command, so there must not be a single mistake.”*

*“Gasp. I pledge eternal loyalty to the Jin Family of Taiyuan. Yes, sir! Yes, sir!”*

He had become the Vice Squad Leader of the Jin Dragon Squad, the Jin Family of Taiyuan’s finest unit.

A young man who had once dreamed of becoming the Master of the Gatekeeper Pavilion had, in just a year or two, become a martial artist skilled enough to stand shoulder to shoulder with the family’s leading figures.

They truly had been days like a dream.

…At least, until a moment ago.

“You’re Hyuk Mujin, right?”

“……!”

A wild head of hair and a thick, unkempt beard. At the words that spilled from the mouth of a broad-shouldered beggar dressed in rags, Hyuk Mujin’s hands and feet went numb.

That voice was utterly familiar. How had he failed to recognize it immediately?

No wonder the back of his head had been itching strangely…

*Where did everything start going wrong?*

Was it when he had come to Henan as Jin Wikyung’s escort?

Or when he had accepted his father’s request to inspect the Henan branch of the Hyuk Family Textile Shop?

He didn’t know. There was only one thing he could be certain of right now.

*I’m fucked.*

As cold sweat slid down his back, he heard the one sentence that turned his journey to Henan into a journey to hell.

“I’ll give you three seconds. Put your head on the ground.”

Unlike the voice in his head screaming that he didn’t want to, his body was honest.

Hyuk Mujin, a rising talent of the Jin Family of Taiyuan and the Vice Squad Leader of its finest unit, slammed his head into the ground with a thunderous cry.

“Yessssss, sir!”

Crash!

* * *

A white stone wall, with five or six rooftops visible beyond it.

The large estate where the Jin Family of Taiyuan was currently staying began to draw closer.

“Is this the place?”

“…Yes.”

Hyuk Mujin answered in a half-dead voice. His once-impressive martial uniform was in tatters, and one of his eyes was swollen and dark with bruising.

To borrow the words he had uttered about half an hour earlier, this was the price of blind bravado.

“Oh. You found a nice place to stay. Business must be going well these days.”

I wasn’t the only one who had changed over the past year. Hyuk Mujin had changed, too, as had the Jin Family of Taiyuan’s standing.

The fact that they had rented an entire estate this large with the Star-Array Grand Banquet just around the corner was proof enough.

“Lead the way, punk.”

“Urgh! It hurts, it hurts!”

“I’m kicking you because it’s supposed to hurt, punk.”

I walked along, kicking him in the rear.

Two Jin Family martial artists standing guard in front of the estate snapped to attention. When they saw their superior, their jaws dropped.

“Gasp!”

“Vice Squad Leader!”

Hyuk Mujin subtly looked away and cleared his throat.

“Ahem. Have you been standing watch properly? This gentleman is…”

Shing! Shing-shing!

“You bastard!”

“How dare you do this to our Vice Squad Leader!”

So he really did have some standing among his subordinates, despite being the Vice Squad Leader of some newly formed unit called the Jin Dragon Squad.

I smiled amiably as I looked at the Jin Dragon Squad members pointing their swords at me.

“Put the swords away. I’m with the Jin Family of Taiyuan.”

“Vice Squad Leader, are you all right?”

“Where did this beggar bastard come from, spouting nonsense?”

Hyuk Mujin nodded grimly at his subordinates’ response.

“Not a beggar bastard. He’s the Third Young Master.”

“Pardon?”

“But no matter how you look at him, he’s a beggar…”

I could let it go once, but not twice.

Hyuk Mujin noticed the change in my expression and spoke in a gloomy voice.

“Hocheol.”

The martial artist called Hocheol quickly answered.

“Yes, Vice Squad Leader.”

“Put your head on the ground.”

“……”

Right. That was the bare minimum I could expect from my right-hand man.

Leaving Hocheol behind to converse with the earth, I stepped into the estate. Almost at the same time, I came face-to-face with someone strolling through the courtyard.

“……!”

“……!”

His eyes trembled with emotion.

Even if ten years passed instead of one, he would recognize me. It wouldn’t matter how disheveled I looked.

Blood ties, brothers—that was what they were.

“Well, look who it is.”

The massive man who had been staring at me, frozen like a statue, was Jin Wikyung. A bright smile spread across his entire face.

He strode toward me and opened his mouth.

“Are you a member of the Beggars’ Sect?”

“……”

Brother, my ass.

* * *

“I recognized you at a glance, actually.”

“Are you kidding me?”

“I’m serious. Did you really think I wouldn’t recognize you, my youngest brother?”

“Do I look like a complete idiot?”

Don’t try to pull that on me. He had even asked what position I held in the Beggars’ Sect.

Jin Wikyung, who had been fidgeting at my reaction, turned to Hyuk Mujin.

“Hyuk, Vice Squad Leader. Didn’t I send you a Sound Transmission earlier? I said I was going to pretend not to recognize him, and asked you to play along.”

“Ah, well, you see…”

“My memory is correct, isn’t it? Right?”

Hyuk Mujin furrowed his brow.

“Ow. Lesser Family Head, why are you stepping on my foot all of a sudden?”

“V-Vice Squad Leader!”

“Aagh! It hurts!”

“……”

He was trying. Really trying.

I didn’t have to look beneath the table to know exactly what was happening.

As I watched the two of them, I suddenly let out a quiet laugh.

*They haven’t changed.*

Jin Wikyung and Hyuk Mujin.

They were the same two people I had known. They had gained experience and composure after everything they had gone through over the past year, but their core remained unchanged.

The fact that they hadn’t changed was enough.

*I wonder what happened to everyone else.*

My curiosity was answered before long.

Jin Wikyung explained in detail what had happened from the moment I left, including the whereabouts of those I had yet to meet again.

Lee Seowol was still struggling to restore the glory of the Mount Heng Sword Sect, while Wolhwa was building an entertainment city in the relatively desolate northern region of Shanxi.

And then…

“Cheongpung is missing?”

“That’s right. Not long after you left, he headed to Huashan with the Three Plum Blossom Elites, but apparently ran away along the way.”

That wasn’t going missing. That was desertion.

From what I heard next, Cheongpung’s disappearance had caused quite an uproar.

An Elder with some influence in Huashan had even come personally to ask them for a favor. He had told them to contact him if they saw that Cheongpung bastard.

“The sect’s foremost elder and its young prodigy disappeared one after another, so it was understandable. My heart ached just watching them.”

The Sword Saint and Cheongpung… At this point, shouldn’t I start wondering whether they were actually related by blood?

“Huashan is really doing well for itself.”

“It’s still doing better than our family.”

“Why? Didn’t they wipe out the mounted bandits in the north and continue to prosper? That sounds like they’re doing pretty well to me.”

Jin Wikyung shook his head gloomily.

“Huashan at least has a Sect Leader and plenty of disciples. Our Family Head’s seat is vacant.”

“Oh.”

“Perhaps that’s why it didn’t feel like someone else’s problem. We decided to help each other from now on. Struggling martial factions have to help one another survive.”

So that was how they were helping each other.

I thought of the man who had been missing for years—the Family Head—and soon erased him from my mind.

In this Murim, he might be my father, but I had never even seen his face. He was a complete stranger.

I felt no familial affection for him, much less any desire to see him.

*If I see him, I see him. If not, whatever.*

Instead, I was far more concerned about Jin Mukyung, whom I’d traded snarls with every chance we got.

“Come to think of it, where’s Second Hyung? Has he gone somewhere?”

Quite a bit of time had passed, but he still hadn’t appeared.

Even if Wipeng was considered to be staying behind to protect the Jin Family of Taiyuan in Jin Wikyung’s place, Jin Mukyung should surely have come…

“He’s in closed-door training.”

“Huh? Again?”

“Still, would be more accurate.”

“…You mean he’s been there this whole time?”

I was dumbfounded when Jin Wikyung nodded.

In martial-arts novels, everyone and his dog spent decades in closed-door training or facing a wall in meditation, but if you actually tried it, you would realize it was almost impossible.

Even a single year would be impossible to endure without extraordinary mental fortitude.

*When did Jin Mukyung enter closed-door training?*

It had been right after he lost his duel with Cheongpung, so he must have been there for a year and six months by now.

For all that time, he had not taken a single step out of the dark training hall, devoting himself to ceaseless training.

He had survived on water and fasting pills for three meals a day.

“Could the closed-door training have gone on so long that he forgot the date? He might not even know about the Star-Array Grand Banquet.”

“I went to see Mukyung before we left and told him about it. I asked whether he wanted to come with us.”

I didn’t need to hear his answer. The fact that Jin Mukyung wasn’t here was answer enough.

Jin Wikyung continued in a low voice.

“He said he wouldn’t leave until he achieved Great Completion. He told me to pass that on to you.”

Great Completion…

To Jin Mukyung, the Star-Array Grand Banquet was a fruit he could reach simply by stretching out his hand.

As one of the most renowned young prodigies in the Central Plains, if he participated, he could prove his martial arts and gain even greater fame.

But Jin Mukyung had chosen martial arts over the sweet fruit.

*He’s an incredible guy.*

While everyone else was reaching for the fruit and climbing the tree, Jin Mukyung had turned his back to the tree and devoted himself to training.

And when his training was finally complete, he would possess not the fruit, but the tree itself.

A tree bearing an abundance of fruit.

*Yeah. That’s a true martial artist.*

I respected his choice. I didn’t know what lay at the end of the path Jin Mukyung had chosen, but I believed its direction was more correct than anyone else’s.

That was enough.

I muttered like a sigh.

“So that’s how it turned out.”

“Are you disappointed?”

“A little. I was hoping the three of us would get together again.”

“Even if those two aren’t here, there are plenty of outstanding masters in the world. Don’t we have the Ten Dragons and Phoenixes right in front of us?”

“I guess.”

At my lukewarm answer, Jin Wikyung smiled faintly.

“Then I’ll have to turn that disappointment into joy.”

“Pardon?”

“I brought you a present.”

A present? I was still staring at him in confusion when Hyuk Mujin rose from his chair.

A short while later, he returned carrying something long, tightly wrapped in thick cloth.

“Do you know what it is?”

Of course I did. The moment I saw it, my heart began to pound, and my fingertips twitched.

It was instinct.

Not the instinct of Jin Taekyung, but of a spearman.

“This is…”

“Fifteen days ago, Elder Jang Taebo handed me this item and said something.”

Shrrk.

As Hyuk Mujin peeled away the cloth, Jin Wikyung’s voice pierced my ears.

“He said he finally understood the hearts of Gan Jiang and Mo Ye.”[^1]

Vrrrrm.

The spear let out a low hum.

[^1]: Gan Jiang and Mo Ye are a legendary husband-and-wife pair of swordsmiths from Chinese lore.
## Chapter artifact 244

# Chapter 244

I had loved the sea ever since I was a child. I loved its distinctive salty scent that pierced my nose, and I loved standing still and watching the waves crash against the shore.

And now, there was a sea inside me.

The qi sea.

Another name for the dantian.

As usual, I swam through the endless sea of qi today.

I grabbed the horn of the Fire Dragon curled up inside my dantian, leisurely circulated through hundreds of acupoints, and opened my eyes.

Ding.

> **System**
>
> - You have successfully completed **circulating your qi**!
>
> - The realm of the **Scorching Sun Divine Arts** has risen to the sixth stage!
>
> - All **Fire Gate Clan** martial arts have become more refined and powerful!
>
> - All fatigue has been cleared, and all stamina has been restored!
>
> - **Level Up!**

*Finally, the sixth stage?*

I neither saw nor heard any of the other System notifications. The only thing that mattered to me was that the realm of the Scorching Sun Divine Arts had reached the sixth stage.

*This is where the real thing begins, right?*

The Fire Gate Cavern was a place created by the first Sect Leader of the Fire Gate Clan for his successors.

Filled with fire energy, it was ideal for absorbing Scorching Yang Qi—and especially optimized for learning the Fire Gate Clan’s greatest martial arts.

In other words, it was a double-EXP event zone.

But even that place had a very clear limit.

*Hmm.*

*“Why are you groaning like a dog that needs to take a dump?”*

It was a conversation I had shared with Jeok Cheongang about six months after entering the Fire Gate Cavern.

At the time, I was brimming with confidence after accomplishing the feat of reaching the third stage of the Scorching Sun Divine Arts.

*“Oh, it’s nothing. I was just wondering whether I should spend another year in closed-door training here.”*

*“Here? In the Fire Gate Cavern?”*

*“Yes.”*

*“What about the Star-Array Grand Banquet?”*

*“I’m improving by leaps and bounds here. Why would I leave? If I spend just one more year… Why are you looking at me like that?”*

*“It’s nothing. I was merely marveling at the size of your blockhead.”*

*“That sounds like a pretty big deal to me.”*

Jeok Cheongang looked at me as though I were pathetic, then let out a deep sigh.

*“Do you know how old this old man is?”*

*“If even you don’t know, how would I?”*

*“I am one hundred and one years old this year.”*

*“Oh. One hundred and one Dalmatians.”*

*“I swear by the ancestors of the Fire Gate Clan, if you spout one more piece of nonsense, I’ll throw your body into the sacred flame as firewood.”*

*“…Yes, sir.”*

*“Regardless, even this old man, who has lived through such a long span of years, remains at the eighth stage. And what was that you said?”*

*“Wait a minute. The eighth stage? Haven’t you already achieved Great Completion?”*

*“Do you think a divine art is called a divine art for no reason? Although your progress is fast, even the martial arts that can be learned in the Fire Gate Cavern have their limits. In the case of the Scorching Sun Divine Arts, that limit is precisely the fifth stage.”*

*“…Then what comes after that?”*

*“Martial arts are like weapons. Sharpen and hone them without end. The only answer is to gain insight through countless hardships and experiences.”*

*“Then I should at least learn the Scorching Sun Divine Arts up to the fifth stage before our remaining time is up.”*

*“Would you look at this greedy brat. Reaching the third stage in a mere six months is already an incredible achievement. Don’t rely on your Heavenly Martial Physique and start spouting nonsense.”*

*“How long do you think it’ll take me?”*

*“Who knows? It took this old man exactly five years to go from the third stage to the fifth… No matter how much you possess the Heavenly Martial Physique, it will take you two years.”*

And exactly six months later, I was able to see Jeok Cheongang’s face, half-drained of its spirit.

*“T-This can’t be happening. It makes no sense.”*

*“But it is happening. Did it really take you five whole years?”*

*“You little bastard! I was a genius counted among the best of my generation!”*

*“Yeah. Heavenly Martial Physique.”*

*“This is impossible! Why did it have to be someone like you!”*

Remembering Jeok Cheongang howling in despair, I let out a quiet laugh.

I put the old memories behind me, stood up, and faced the large full-length mirror.

It reflected a perfectly balanced body, compact muscles filled with power and elasticity, hair twisted up and tied without much care, and a smooth chin.

*It wasn’t as if leaving it alone would have caused any problems.*

Now that the thick growth was gone, I felt oddly empty. But there was no arguing with Jin Wikyung’s forceful insistence.

*“The Star-Array Grand Banquet is a gathering watched by every martial artist under heaven. The Sleeping Dragon of Shanxi is appearing in the Central Plains, and you plan to go out looking like this? It’s a crime!”*

I had thought he was being a little dramatic, but after getting it cut, I liked this better.

Whatever else could be said about this body, the face was exceptionally handsome.

*You look like a gisaeng’s brother.*[^1]

I was inwardly muttering the highest compliment one man could give another when I suddenly realized I had forgotten something.

Clink.

“Oh, right. I had this.”

The shackles, iron chains, and iron ball I had continued to drag around even after arriving at the estate of the Jin Family of Taiyuan.

I gazed silently at the objects that had practically become parts of my body, then opened my mouth.

“Inventory open. Summon.”

Whoosh!

The next moment, a solid spear shaft was grasped in my hand.

The object summoned from my Inventory was a spear approximately two meters long.

Perhaps because it had been made from an enormous amount of Ten-Thousand-Year Cold Iron, it shone with a beautiful, transparent light from the spearhead all the way to the end of the shaft.

“White Flame.”

Vrrrrm. Vrrrrm.

As though it had recognized its own name, a faint vibration traveled from within the shaft.

White Flame was a weapon made exclusively for me by Jang Taebo, the former Guild Leader of the Ironcraft Guild, who was known as the greatest smith under heaven.

Perhaps that was why White Flame was special.

Whether viewed with the naked eye or through the System window.

However…

“Captain. It’s time for us to leave.”

As Hyuk Mujin’s voice from outside the door made clear, it was time to go.

Sunlight flooded the world outside the window, and the people of the Jin Family of Taiyuan—including Jin Wikyung—were moving about busily.

“All right.”

As I answered, I choked up on the spear and slashed.

With four streaks of light, everything that had bound me for the past year fell away. The shackles, chains, and iron ball rolled noisily across the floor.

Clatter. Boom!

Bang!

Startled by the tremendous noise, Hyuk Mujin opened the door and rushed in.

“What was that?”

“Nothing. Let’s go. Oh, make sure to bring the chains.”

“……You’re planning to tie me up with those, aren’t you?”

“Those chains are made of Ten-Thousand-Year Cold Iron.”

“Gasp! They’re mine. Mine!”

Clicking my tongue, I stepped outside. Jin Wikyung, mounted on a large black horse, spotted me and grinned.

“Let us go.”

“Yes.”

Our destination was Mount Song.

That was where the Star-Array Grand Banquet, the event drawing the attention of all Murim, would begin.

“Yah!”

With Jin Wikyung and me at the front, fifty members of the Jin Dragon Squad followed behind.

Through the wind rushing past us, someone’s distant shout echoed faintly.

“Wait! Wait! Don’t leave me behind!”

“……”

I still couldn’t believe that man was the Vice Squad Leader.

* * *

The Fire King, Jeok Cheongang, muttered with an annoyed expression.

“…Do I really have to attend something like this?”

The Dharma King, Hong Dao, was sitting with an endlessly benevolent expression.

“This old monk is bored enough to reach Buddhahood, so keep your mouth shut and sit still.”

“Why? You said you were bored, too.”

“I am already bored. What do you think happens when an old man with little time left starts whining like a seven-year-old child beside me?”

“I would get annoyed.”

“Exactly. If I am bored and become annoyed as well, I may break my wooden fish and return to my quarters.”

“You have attained enlightenment.”

“Amitabha. Amitabha.”

Tok. Tok. Tok-tok-tok-tok…

The clear sound of a wooden fish echoed through the room. Those who had been listening with their ears perked up wore utterly dumbfounded expressions.

*They say the Fire King and Dharma King are famous for their eccentric behavior. They certainly are.*

*Those two haven’t changed at all.*

*Does that old bastard ever die?*

Their thoughts were different, as were their clothing and the auras they gave off.

They ranged from middle-aged men without a single strand of white hair to old men with heads of pure white.

The dozen or so people gathered there, each so different from the others, were not ordinary mortals.

They belonged to the fifteen pillars supporting the current Murim: the Nine Sects and One Gang and the Five Great Families.

The Fire King, Jeok Cheongang, was already familiar with some of them.

“Oh, isn’t that the Nangong Family Head?”

Namgung Ryong, the Family Head of the Nangong Family, rose and performed a fist-and-palm salute.

“Please forgive me for greeting you so late. The two of you were having such an entertaining conversation that I hesitated to interrupt.”

“It’s fine. I left in a hurry last time and didn’t even get to see your face. My apologies.”

“Not at all. I am the one who should apologize.”

“So, is your son competing in this Star-Array Grand Banquet?”

“He won’t be able to this time.”

“That’s unfortunate.”

Jeok Cheongang’s face showed not the slightest trace of regret as his gaze shifted to the man beside Namgung Ryong.

“Who are you?”

The man with the sycophant’s beard asked sourly,

“Are you speaking to me?”

“Yes. You, with the beard like a sycophant’s.”

“I am Gong Iljung, the Sect Leader of the Zhongnan Sect.”

“Ah. Are you that fellow they call the Wind-and-Cloud War God or whatever?”

“Wind-and-Cloud Sword Lord.”

“What does that matter? Young man, why are you so rigid?”

Gong Iljung, a “young man” who had long since passed sixty, had to steady his breathing.

Only a year earlier, he had been shocked when the Roaring Fury Swordsman, his Senior Brother who had studied under the same Master, arrived with a severe Internal Injury.

But he had to endure this. The Fire King, Jeok Cheongang, was quite literally no different from a mad tiger.

“Did you hear from your Senior Brother?”

“…Yes.”

“Keep him under control so he doesn’t come to my attention. Shoving him into the Repentance Cave for about twenty years might not be a bad idea.”

Gong Iljung barely managed to swallow the curse rising to his lips.

What Jeok Cheongang meant was that he could easily live another twenty years, so Gong Iljung had better not act up.

Even those who normally held Jeok Cheongang in low regard inwardly clicked their tongues at his words.

*What a vicious old man…*

*Is he planning to enjoy immortality?*

*You’ve caused enough trouble. Go already, old man. We need to breathe, too.*

*I should have brought my Master.*

Although they belonged to different sects, there was still a strict order of seniority in the Murim.

Jeok Cheongang was a figure from two generations earlier, and his seniority was naturally tremendous.

That was one reason the leaders gathered there could do nothing but tremble before him, no matter how much they dominated the world.

In martial arts, seniority, or verbal skill, there was not a single area in which they could defeat him.

“Ahem. Ahem.”

“Erhm.”

Several people were clearing their throats to avoid Jeok Cheongang’s questions when a booming voice rang out.

“Hahahaha! With the tiger away, the fox has been playing king. Jeok Cheongang, have you been well?”

Jeok Cheongang turned his head at the thunderous voice. His brow was already deeply furrowed, because he knew exactly who had arrived.

“Goddammit. You’re not dead yet?”

“Listen to the way this little old man talks.”

An enormous old man threw back his head and laughed. Although his mouth split open in a broad grin, his sharp eyes swept over Jeok Cheongang.

“I welcomed a great-great-grandson not long ago. There’s no way I’m dying before I see that boy get married.”

“Your great-great-grandson?”

“What, are you jealous? My great-grandson’s wife is Hebei’s greatest beauty, and the boy takes after his mother to a tee. He’s absolutely adorable.”

Jeok Cheongang replied with an indifferent expression.

“The greatest beauty in that neighborhood can’t be trusted. Isn’t Hebei the place where anyone with fists this big and a thick waist gets called Yang Guifei?”

“What!”

“Anyway, congratulations. With ten children, you don’t need to worry about heirs.”

“…What kind of bullshit are you pulling?”

“What do you mean, what kind? To commemorate seeing your great-great-grandson, why don’t you change your title? Not Thunderbolt Saber King. How about Virility Saber King? What do you think?”

“GRAAAAGH! You old man!”

“Sit down while I’m asking nicely. Don’t you remember breaking your bones when you challenged me during the Great Faction War?”

Sssshhhh!

Powerful auras poured from the bodies of the two Supreme Peak masters. Their momentum was so overwhelming that everyone present felt a chill run through them.

If the Dharma King had not been there to mediate, the situation might have turned bloody.

“Now, now. Amitabha, Amitabha… Both of you, calm your anger. The heroes outside are waiting. How can you make such a disgraceful spectacle? Do you perhaps wish to smear the names of the Fire Gate Clan and the Hebei Peng Family with shit here today?”

His final words had a definite effect. The two men hesitated before withdrawing their auras.

“Ahem. Jeok Cheongang, I will teach you a lesson next time.”

“I’ll be waiting, Virility Saber King.”

Having delivered the final blow to the Thunderbolt Saber King’s title, Jeok Cheongang leisurely walked away.

The Dharma King, the Thunderbolt Saber King, and the overlords of the various regions followed behind him.

They passed through a corridor covered in blue cloth and stepped out into the glaring sunlight.

Three zhang below them, tens of thousands of people gathered at the foot of Mount Song greeted them with a tremendous roar.

“Waaaaaaah!”

[^1]: Gisaeng were traditional Korean entertainers who were trained in music, dance, and the literary arts; the phrase refers to a handsome, delicate-looking man.

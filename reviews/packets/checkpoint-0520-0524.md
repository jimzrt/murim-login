# Checkpoint Review — 520–524

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

# Chapters 520–524

## Plot

At the New Murim Alliance, Sword Saint Mae Jonghak serves as acting leader and processes its affairs despite lacking ambition for the position. Jeok Cheongang refuses Mae’s request to become Alliance Leader, leaving Mae to continue carrying the burden because someone must.

Taekyung, Jeok, and Song Ho enter the Alliance’s Inner City. Taekyung detects five concealed Hidden Shadow Pavilion agents, demonstrating how his Yangtze training improved his qi control and Qi Sense. An emergency Heaven Grade report from Wudang reveals that the Killing Ghost was Jang Sam, an ordinary fisherman who disappeared near Mount Wudang. Taekyung suspects that the Blood Fish transformed him and warns that similar incidents could ignite the Murim’s existing powder keg.

The Hidden Shadow Pavilion resumes operations, and the Murim Alliance mobilizes. Nangong Cheon and Peng Cheolhu are allowed to share the threat with their families, while Mae again asks Jeok whether he will take the Alliance Leader position; Jeok’s answer remains unstated.

Taekyung cultivates the Fire Gate Divine Technique, reaches Three Flowers Gather at the Crown, and fails to break through to Five Qi Returning to Origin after Mungyeong interrupts him. Mungyeong gives him a custom fire-qi pill, ends his direct training, and assigns him to incorporate the martial principles he learned into his existing techniques. Taekyung recognizes that he seeks strength sufficient to protect everyone around him simply through his existence.

Hyuk Mujin reports that Jin Mukyung is meeting faction leaders, the Three Fiend has been transferred to the Alliance for interrogation, Gung Gibang is staying with the Beggars’ Sect’s Henan branch, and Cheongpung is away buying food. With his companions temporarily absent, Taekyung feels an unexpected emptiness. The Murim world is now gathering beneath a single banner at the Alliance.

## Continuity

- Mae Jonghak remains the New Murim Alliance’s acting administrator because Jeok Cheongang refused the Alliance Leader position; Mae accepts the burden out of responsibility.
- Song Ho is the reinstated Chief of the Hidden Shadow Pavilion and commands a vetted intelligence network, including five concealed agents detected by Taekyung.
- Taekyung’s Yangtze training greatly improved his internal-energy control and Qi Sense.
- Wudang’s report identifies the Killing Ghost as Jang Sam, a fisherman who disappeared near Mount Wudang. The Blood Fish may have caused or participated in his transformation; similar incidents elsewhere remain possible.
- Dark Heaven has not opened a second Gate. Taekyung believes its ability to open Gates is limited but warns that another outbreak could trigger a catastrophe across the Murim.
- Taekyung has achieved Three Flowers Gather at the Crown but not Five Qi Returning to Origin.
- Mungyeong has ended Taekyung’s direct training, given him a custom fire-qi pill, taught him martial principles rather than another martial art, and assigned him to integrate those principles into his existing techniques.
- Jin Mukyung is consulting faction leaders; the Three Fiend is in Alliance custody; Gung Gibang is temporarily at the Beggars’ Sect’s Henan branch; and Cheongpung is temporarily away.
- The outcome of Jeok Cheongang and Nangong Cheon’s duel remains unresolved, as does Jeok’s answer to Mae’s renewed request.
- The Lord of Heaven’s identity, Dark Heaven’s connection to Taekyung’s original world, the mechanics of opening Gates, the Southern Heaven Demon Empress’s intent in Yunnan, and the Blood Fish’s wider role remain unresolved.

## Translation Decisions

- Retain **New Murim Alliance**, **Murim Alliance**, **Alliance Leader**, **Alliance Leader’s Office**, **Inner City**, **Hidden Shadow Pavilion**, **Heaven Grade**, and **Earth Grade**.
- Render **가짜 무림인 2단계** as **Fake Murim Practitioner, Stage 2** and retain **Single Reed Crossing the River**.
- Render **삼화취정** as **Three Flowers Gather at the Crown** and **오기조원** as **Five Qi Returning to Origin**.
- Render **화약고** as **powder keg**, **무적자** as **The Invincible**, and **무리** as **martial principles**.
- Retain **Fire Gate Divine Technique**, **Mungyeong Special Jin Custom Pill**, **The Dream of the Nine Clouds**, **Grim Reaper**, **Zerg**, and **Niagara Falls**.
- Preserve Taekyung’s blunt profanity, teasing humor, and monster comparisons.

## Durable state

{
  "active_continuity": [
    "Jeok Cheongang's Heart Demon and the dark memories binding him have been expelled; he entered a new realm, achieved Returned to Youth, and began his long-promised duel with Nangong Cheon, the Azure Sky Sword King.",
    "Mungyeong is the Slaughter Saint and former Divine Physician, a Returned to Youth Supreme Peak master and the greatest assassin in history; he has ended Taekyung's direct training, given him a custom fire-qi pill, taught him martial principles, and assigned him a final task.",
    "Zhuge Feng's Demon-Sealing Formation blocks all mana from the exposed Gate by drawing in natural qi, but its permanence and repeatability remain unresolved.",
    "Jang Taebo is the Jin Family of Taiyuan's Master of Ironcraft Hall and is summoning renowned artisans to process the Water God Dragon's remains.",
    "Mae Jonghak remains the New Murim Alliance's administrator after Jeok Cheongang refused the Alliance Leader position because it was troublesome; Mae accepts the burden because someone must do it.",
    "Song Ho is the reinstated Chief of the Hidden Shadow Pavilion and commands a vetted intelligence network, including five concealed agents whom Taekyung detected inside the Alliance.",
    "The Southern Heaven Demon Empress is traveling toward Yunnan and expects to cause further deaths.",
    "Unnamed, Hong Dao's practical Disciple, endured three months in Repentance Cave, achieved enlightenment, received Shaolin's Great Restoration Pill, and is now a scarred Supreme Peak master and Jung Ho's young Martial Uncle.",
    "The Black Dragon Demon Gate is an ancient unorthodox faction that once belonged to the Demonic Cult's Twelve Branches and now ranks among the Central Plains' strongest unorthodox powers.",
    "Jin Taekyung completed Stage 2 of Fake Murim Practitioner, achieved Single Reed Crossing the River, improved his internal-energy control and attributes, gained 50 bonus points and substantial EXP, leveled up, and achieved Three Flowers Gather at the Crown but not Five Qi Returning to Origin.",
    "Wudang's second report identifies the Killing Ghost as Jang Sam, a fisherman who disappeared near Mount Wudang; Taekyung suspects the Blood Fish caused or participated in his transformation.",
    "Dark Heaven has not opened a second Gate yet, and the Murim Alliance and Hidden Shadow Pavilion are mobilizing against future outbreaks; the Murim world is now gathering under one banner while Jin Mukyung consults faction leaders."
  ],
  "continuity_sources": [
    524,
    523
  ],
  "open_questions": [
    "What is the Lord of Heaven's identity, how is he connected to the dangerous force Taekyung associates with his original world, and how can Dark Heaven open Gates?",
    "Where is the Southern Heaven Demon Empress ultimately headed, and what does she intend to do in Yunnan?",
    "What is the outcome of the duel between Jeok Cheongang and Nangong Cheon, the Azure Sky Sword King?",
    "Did the Blood Fish cause Jang Sam's transformation, and could similar Blood Fish or Gate-related transformations occur elsewhere?",
    "How will Taekyung incorporate Mungyeong's martial principles, and what effect will the custom pill have on him?"
  ],
  "safe_through": 524,
  "temporary_decisions": [
    "Render 새외무림 as Outer Murim, 새외 as Outer Lands, 북해빙궁 as North Sea Ice Palace, 야수묘왕 as Beast Miao King, and retain Nanman Beast Palace for 남만야수궁.",
    "Render 소뢰음사 as Small Thunderclap Temple, 광풍사 as Mad Wind Society, 포달랍궁 as Potala Palace, 오독문 as Five Poisons Sect, 독곡 as Poison Valley, 천축 as India, 갠지스강 as Ganges River, and 대환단 as Great Restoration Pill.",
    "Render 파사국 as Persia, 회교도 as Muslims, 영웅건 as hero headband, 대막 as great desert, 귀염권 as Ghost Flame Fist, and 장성 as Great Wall.",
    "Retain sa-eo for 사어, shark for 상어, Old Master for 노야, this old man/I for 노부, Shark Water-Ski Team for 수상스키단, and swift ship for 쾌조선.",
    "Render 화약고 as powder keg, 칠공 as seven apertures, 단환 as pill, 무적자 as The Invincible, 무리 as martial principles, and 구운몽 as The Dream of the Nine Clouds; preserve the chapter's blunt profanity and monster-comparison humor."
  ],
  "version": 1
}

## Reading copies

## Chapter artifact 520

# Chapter 520

The young man gazed blankly out the window.

It was a truly beautiful spring day.

The sunlight was just right, and the breeze drifting through the half-open window was pleasantly cool. Even the flowers, now in full bloom, filled the air with a sweet fragrance.

It was nothing short of a Wuling Peach Blossom Spring in the mortal world.[^1]

Everything would have been perfect if not for the voice that suddenly came from behind him.

“It’s a beautiful day.”

The young man did not startle. He had sensed the approaching presence a long time ago.

And that was not limited to the owner of the voice he had just heard.

Front, back, left, right. Above and below.

The young man perceived and accepted everything happening around him.

It was not something he did out of necessity or conscious will. It came as naturally as breathing.

*How frustrating. I can’t even enjoy the spring scenery properly anymore.*

After muttering inwardly, the young man turned around.

An old man with the imposing bearing of a young man was looking at him with a genial smile.

“I stopped by for a moment out of an old man’s needless concern, only to find you slacking off.”

The old man’s voice was aged enough to convey his years at a single hearing.

His tone was gentle, like a grandfather speaking to his young grandson, but the young man knew from experience that the old man standing before him concealed an extremely stealthy, razor-sharp blade.

“What are you thinking about so intently?”

“I was briefly thinking how fortunate it is that I am not your enemy.”

The old man gave a low chuckle.

“If anyone heard that, they might think I was a frightening man.”

He could not afford to be fooled by that good-natured laugh.

No one knew how many deep schemes and long-term plans lurked behind that smiling face and inside that head.

During the upheaval of the Great Faction War, the leader of the Murim Alliance’s Hidden Shadow Pavilion had seen through the situation across the world as easily as his own palm and eliminated countless fiends. There was no way he could be an ordinary man.

“Other people would never agree with you, Thousand-Faced Fox.”

Thousand-Faced Fox Song Ho.

The old fox of the Hidden Shadow Pavilion, said to possess a thousand faces, shrugged at the young man’s words.

“Of course, there are people who fear this old man. But I do not believe that applies to the person standing before me.”

“Me?”

“Does it not?”

The young man fell into deep thought for a while, then suddenly opened his eyes wide.

“Oh. You’re right.”

“Isn’t it?”

“I suppose you are right. Now that I think about it, you aren’t particularly frightening.”

If ordinary Murim practitioners who staked their lives on their pride had exchanged those words, blades would have been drawn long ago.

But the two men facing each other did not belong to the category of ordinary people.

The reason Thousand-Faced Fox Song Ho was not offended in the slightest had a great deal to do with the identity of the person before him.

“Be wary of your surroundings, but fear no one. That is what an Alliance Leader must always do.”

The young man—Sword Saint Mae Jonghak—answered with a sour expression.

“I’d prefer it if you didn’t call me Alliance Leader whenever possible.”

“You must accept it now.”

“I simply haven’t gotten used to it.”

“But you will soon become the Alliance Leader.”

“Not yet.”

“They say it is better to take the whipping sooner rather than later.”

“I’ve always wondered why I have to be the one taking that whipping.”

Thousand-Faced Fox’s answer was concise.

“Because the Martial God is not here.”

The title Martial God had once meant perfection. No—not once. It still meant the same thing.

Everyone who had met him even once had praised him in unison, and even after the passage of many long years, that vast and brilliant Fame still illuminated the world.

But…

“We could not find him.”

The Martial God had disappeared. No one knew whether he was alive or dead, or what had caused him to vanish without a trace.

Back when the Murim Alliance still existed, Thousand-Faced Fox had mobilized the Hidden Shadow Pavilion’s entire intelligence network to scour the world. Yet he had found no trace of the Martial God anywhere.

Like sunlight that shone down only briefly during a raging storm. Like a meteor that streaked across the night sky for a fleeting instant.

The Martial God had disappeared like that, leaving his own title—which had become the heavens—spread across the world.

“As long as he is not present, Great Hero Mae Jonghak is the only person who can take up the position of Alliance Leader.”

“Hah. There must be plenty of other suitable candidates besides me.”

“If you are referring to the other members of the Three Saints and the Ten Kings, I will pretend I did not hear that.”

“No, why?”

“For one thing, the Bow Saint’s whereabouts are unknown.”

“Isn’t the Hidden Shadow Pavilion still looking for him?”

“Do you think Dark Heaven will wait for us? Should I send a messenger pigeon saying, ‘We are looking for the Bow Saint, so please wait a little longer’?”

“Oh. Now that you mention it, I suppose not.”

“…”

Thousand-Faced Fox held back the urge to bring his fist down on Mae Jonghak’s head and continued.

“And, as you know, his personality is somewhat…”

“I liked him because he was so fiery.”

“If he runs the Murim Alliance into the ground with that fiery personality, other people will not be pleased.”

“Hmm. Is that so?”

“And the Slaughter Saint… There is no point talking about him.”

“That fellow might be more suitable than you think. His martial arts are one thing, but his presence was overwhelming. He seemed to have the ability to command others.”

“People would certainly follow him. Anyone who refused would already be dead.”

“Are you viewing him a little too much as a Killing Ghost?”

“His title is the Slaughter Saint. What exactly do you expect from me?”

“That is true, too.”

Should I really hit him?

Thousand-Faced Fox looked at Mae Jonghak with exactly that thought in his eyes, then sighed.

“The other members of the Ten Kings are unsuitable for similar reasons. Some have already passed away, while others are unfit for the position of Alliance Leader for one reason or another.”

The Alliance Leader could not be someone who was merely strong in martial arts.

He needed the decisiveness to make important choices, as well as the virtue and magnanimity to lead and embrace others.

In that regard, Sword Saint Mae Jonghak was the Martial God’s only true replacement.

“Great Hero, you have received the recognition of the leaders of the Nine Sects and One Gang and the Five Great Families. Your character is upright and fair. You do not give special treatment even to your own sect, Huashan, and you listen to what others have to say. You are more than qualified to become Alliance Leader.”

Along with the birth of the New Murim Alliance, the Hidden Shadow Pavilion had officially been resurrected, and Thousand-Faced Fox had regained his former status. But the position of Alliance Leader was not something one could obtain through a single person’s support.

Only someone recognized by all and possessing the qualities of a leader as well as exceptional martial arts could rise to the position of Alliance Leader.

*Of course, there had been no shortage of voices in opposition.*

Thousand-Faced Fox scattered the thought that had just come to mind and suddenly hardened his expression.

“And yet someone like you is leisurely enjoying the spring weather.”

Mae Jonghak glanced at the window with a regretful expression.

“The weather was nice, so I was only looking outside for a moment.”

“There are so many matters waiting for you right now…”

“Oh, that’s right. Take them with you. I put them all together in one place.”

Thousand-Faced Fox, who had been preparing to give him a thorough scolding, stopped short.

“What do you mean?”

“The bamboo slips brought in from the Hidden Shadow Pavilion earlier. More precisely, there were seventy-eight matters. I handled them all.”

“...?”

He handled them? All those matters in such a short time?

Thousand-Faced Fox silently stared at the bamboo slips piled up like a mountain in one corner of the office. Then his eyes narrowed.

“Did you read the letter from Qinghai?”

“You mean the Kunlun Sect? Of course. It said they were pressed for time because they had to suppress bands of bandits and mounted bandits. It would be good if they arrived on time, but it should not matter much if they are a little late.”

“And the news from Sichuan?”

“It said they were all joining forces and speeding up the reconstruction of the Tang Clan. Oh, tell the Inner Hall to prepare an elixir with exceptional medicinal effects. I heard the Family Head’s condition is poor. Large-scale aid aside, we should at least help in this way for now.”

“Then what about the letter that arrived from the Nanman Beast Palace…?”

“Was there one? I did not see anything related to the Nanman Beast Palace among today’s matters.”

There was no other possibility. Just as Mae Jonghak had said, none of the matters submitted that day contained anything related to the Nanman Beast Palace.

Only then did a faint smile form around Thousand-Faced Fox’s lips, after he had spent all this time half believing and half doubting him.

“Hm? Why are you smiling?”

“Nothing. It simply warms my heart to see you so devoted to your duties…”

“Do not smile so slyly. Someone else might be horrified if they saw you.”

“…”

“In any case, the breeze feels nice. It really is a beautiful day.”

After ruining Thousand-Faced Fox’s mood, Mae Jonghak gazed aimlessly out the window and spoke.

“Would you like to take a walk outside with me? We may not have another day like this after today.”

“I would rather not.”

Thousand-Faced Fox answered curtly, then continued.

“I will send up another matter shortly, so do not do anything pointless, Alliance Leader. Get to work.”

“Even so, an honored guest is arriving. As a matter of basic decency, I should go out to greet them.”

“Did you say greet them?”

Thousand-Faced Fox paused, then limped toward the window on his prosthetic leg.

“Look over there.”

“...!”

Beyond the city wall, an object was slowly drawing closer.

It was blurry because of the considerable distance, but once he focused his internal energy, it was easy to identify the object as a carriage.

The problem was why a familiar face was sitting on the driver’s bench of that four-horse carriage.

*Why is Shadow Killer there?*

Shadow Killer was one of the Hidden Shadow Pavilion’s finest elite agents.

During the Star-Array Grand Banquet, he had tracked Mae Jonghak’s movements while Mae was concealing his identity. During the Great Faction War, he had taken the heads of countless fiends.

“It looks like a familiar face. Don’t you agree?”

“Yes. I sent Shadow Killer because there was trouble on the main road, but…”

He had sent the man to capture them, and now he was bringing them here like honored guests.

Thousand-Faced Fox swallowed the rest of his words as Mae Jonghak’s voice reached his ears.

“An urgent report came while you were away for a moment.”

“An urgent report?”

“Yes. I heard that some welcome faces were on their way.”

Mae Jonghak patted Thousand-Faced Fox’s shoulder twice, then leaned out the window and muttered,

“Come on. Let’s go.”

* * *

“Welcome.”

The carriage entered the Murim Alliance’s Inner City and came to a stop. The voice that greeted us as soon as we got down was fairly familiar.

*Sword Saint Mae Jonghak.*

I had once known him by the name Always-Victorious Sword Jongni Chu. He spotted me and gave a short laugh.

“How have you been, my friend?”

“…”

*That persona is really sticking around.*

When I dipped my head in greeting, Mae Jonghak smacked his lips in disappointment, then turned to Jeok Cheongang.

“It’s good to see that you look healthy.”

Jeok Cheongang, who had been yawning extravagantly while looking around, furrowed his brow.

“Were you speaking to this old man?”

“It has truly been a long time. I am glad to see you again.”

“You must have mistaken me for someone else. This old man has no particular connection with some brat whose blood hasn’t even dried on his head…”

Jeok Cheongang stopped mid-sentence.

His eyes grew wide as he looked Mae Jonghak up and down.

“Could it be you?”

“It is. It’s me.”

Mae Jonghak beamed and continued.

“Since we are meeting again, let me ask. Would you consider becoming the Alliance Leader?”

“...?”

“...?”

*Is this the Murim version of picking a group-project captain?*

[^1]: The Wuling Peach Blossom Spring is a classical image of an idyllic utopia.
## Chapter artifact 521

# Chapter 521

“Since it’s good to see you again, let me ask you something. Would you consider becoming the Alliance Leader?”

“...?”

“...?”

If the captain of a group project announced that he was quitting, it was only natural for the other members to panic.

Mae Jonghak’s words had gone far beyond anything I could have expected. The Thunderbolt Saber King’s mouth fell open, while the Azure Sky Sword King and Unnamed stared at Mae Jonghak in stunned silence.

*What does seeing each other again have to do with that...?*

*And this guy is the Alliance Leader?*

They had not said it aloud, but their expressions said exactly that.

In the middle of this situation, the last person present—Jeok Cheongang—opened his mouth with an astonishingly calm expression.

“An ordinary person would be unable to continue speaking at a moment like this. But this old man is different. I have met an awful lot of crazy bastards lately.”

The moment my eyes met Jeok Cheongang’s, I turned around.

By an incredible coincidence, there was no one behind me. Except for a sparrow pecking at something on the ground.

*I see. So that’s why Jeok Cheongang was looking this way.*

“I didn’t know you liked birds. Sparrows are cute, though.”

“I was looking at you.”

“Me? Why are you suddenly looking at me?”

“Are you asking because you don’t know?”

“Usually, people ask because they don’t know. Why would they ask if they already knew?”

“Seeing that mouth flap so happily makes me want to bury you.”

*That would be a problem.*

After thinking for a moment, I asked with a doubtful expression,

“I’m only asking this in case of a genuine maybe, perhaps, one-in-a-million possibility. Was my name included among the crazy bastards you mentioned?”

“Without question. Absolutely. Beyond the slightest doubt, your name is at the very front of the list.”

“...”

I had come in dead last a few times during my school days, but this was the first time I had ever come in first.

*I should be happy that I managed to come in first somehow...*

*No, forget that. This is ridiculous.*

*To hear something like that from Jeok Cheongang of all people. And I ranked higher than Cheongpung.*

The psychological damage made my vision swim. I stared at Jeok Cheongang and opened my mouth.

“I have an older friend named Tess hyung. He once said something like this: ‘Know thyself.’”

“Was that directed at this old man?”

“Are you asking because you don’t know?”

“You little son of a—”

The fist he had raised halfway suddenly stopped.

Jeok Cheongang sensed the gazes gathering around us, let out a pained groan, and turned back toward Mae Jonghak.

“In any case, to give you a clear answer, I refuse.”

“Ho. Why?”

“Because it’s a pain.”

The answer was a masterpiece. He could at least have been tempted once, but he had rejected the position of Alliance Leader simply because it was bothersome.

“Ah. That is an undeniable fact.”

“...”

That was an even greater masterpiece.

*Please don’t agree with him. Can’t you see people slowly gathering around us?*

*We’re screwed.*

If this conversation spread, there was a growing chance that the group project—or rather, the Murim Alliance—would fall apart.

Unfortunately, the two masterpieces facing each other were both shamelessly manly men who did not care about such things.

“That sort of title doesn’t suit my temperament, and I dislike dealing with people.”

“Ah. I’m the same.”

“Then quit.”

“That would be difficult.”

“Why?”

Mae Jonghak scratched his chin and casually tossed out a single sentence.

“Because someone has to do it.”

“...!”

A man who had taken up the sword simply because he loved martial arts, and who had earned the title of Sword Saint.

A true martial artist who, at the end of a brutal war, abandoned wealth and glory, chose to live as a recluse, and returned to the mountains.

But Sword Saint Mae Jonghak was a Great Hero before he was a martial artist.

He had not accepted the title of Alliance Leader out of shallow vanity.

He had accepted it because he was both a martial artist and a Great Hero.

*Because someone has to do it.*

It was a short sentence, but it carried a deep resonance. Jeok Cheongang stared at Mae Jonghak and let out a quiet laugh.

“Many long years have passed, yet you haven’t changed. It feels as though the day we met at Mount Jiuhua was only yesterday.”

Mae Jonghak’s eyes widened.

“Yesterday? What are you talking about? That happened at least several decades ago.”

“...”

“...”

*Give me back my touching moment, you bastard.*

I was not the only one who felt wronged. Under the pointed gazes pouring down on him, Mae Jonghak tilted his head.

“Did I remember incorrectly?”

All traces of laughter vanished from Jeok Cheongang’s face.

“...You really haven’t changed. It feels like my internal organs are rotting.”

“Are you still unwell? I heard you had recovered fully from the poisoning.”

“Shut that mouth of yours. If you keep talking, I don’t know what this old man might do.”

“Now that I think about it, Great Hero Jeok was the first person to say something like that to me. This is why I like you.”

“...Are you and that brat Cheongpung really just Master and Disciple? Are you not related by blood?”

That was a question worthy of being counted among the Seven Great Mysteries of the Murim.

Just as everyone, myself included, waited for Mae Jonghak’s answer with pounding hearts, an old voice came from behind us.

“As far as I know, there is no blood relation between the Alliance Leader and the Huashan Divine Dragon.”

The face of the old man limping toward us on a prosthetic leg was familiar.

*Thousand-Faced Fox Song Ho.*

The former Chief of the Hidden Shadow Pavilion of the Murim Alliance—and now its reinstated Chief—gave a slight bow and opened his mouth.

“Please come upstairs. I have prepared some refreshments.”

* * *

The Murim Alliance was crowded with people.

People bearing the character *Alliance* embroidered in silver thread on their chests moved around in every direction. Among them were not only martial artists carrying weapons, but also quite a few people dressed in neat scholars’ robes.

*Those people...*

The post of Chief of the Hidden Shadow Pavilion was not something Song Ho had won at a card table.

As if he had immediately noticed the question in my gaze, he gave me a brief explanation while walking beside me.

“They are directly under the Alliance Leader’s Office.”

“They don’t look like they’re from the Nine Sects and One Gang or the Five Great Families.”

“You observed correctly. Since they are directly under the Alliance Leader’s Office, we did not select anyone who belonged to another sect or whose identity had not been thoroughly verified, in order to maintain confidentiality. Come this way.”

The interior of the Murim Alliance was as vast as a plain and as complicated as a maze.

Everywhere I turned, pavilions and other buildings rose densely around us. From the training ground in the distance came the shouts of people practicing.

When I first got down from the carriage, I had thought the place belonged to the Inner City. But the farther inside we went, the tighter the security became, and the fewer people we saw.

*No. More accurately, it would be better to say that they had become invisible.*

No matter how completely they suppressed their breathing or how advanced their concealment techniques were, I could still sense them.

On the walls. Above the ceiling. Hidden in the darkness, watching this place.

I could sense the gazes and energy of those concealed around us.

“I’ve been curious about this for a while. Are they members of the Hidden Shadow Pavilion?”

Song Ho’s eyes widened slightly at my sudden question.

“When did you realize?”

“When we passed the fifth door.”

“Can you still sense them?”

“Yes.”

“Impressive. Truly impressive. Those four were raised as assassins within the Hidden Shadow Pavilion. To detect their presence perfectly...”

As Song Ho exclaimed in admiration, I scratched my chin.

“Are you really asking because you don’t know, or is this a test?”

“Hm? What do you mean?”

“If it’s a test, it’s not very fun. There are five of them, not four.”

Ssss.

The torch hanging on the wall trembled slightly, then quickly became still.

It was the only evidence of the agitation among the Hidden Shadow Pavilion agents concealed nearby. The gaze of their leader, Thousand-Faced Fox Song Ho, sank deeply.

“I suspected as much, but it wasn’t a coincidence.”

“Honestly, I just took a guess.”

“...”

“I’m kidding. Your subordinates are all very skilled. I almost failed to notice them and walked right past.”

A flash passed through Song Ho’s eyes.

Unlike the look he had given me when testing me moments earlier, this one contained genuine admiration and curiosity.

“That is truly astonishing. Based on the information I had gathered, I thought I had made a reasonably accurate prediction of your martial ability... Have you gained new insight recently?”

*Insight.*

I recalled the ten-day training session spent drifting down the Yangtze and nodded.

The greatest gain I had obtained from the training Mungyeong had assigned me was the ability to handle qi—the source of martial arts—with far greater precision than before.

If I had been handling a rope before, I was now handling a single strand of thread.

As a result, my understanding of controlling internal energy had naturally improved, and my Qi Sense had sharpened as well.

“Perhaps. A little.”

“Your growth is terrifying. It’s almost impossible to believe.”

At Song Ho’s words, the Thunderbolt Saber King, who had been glancing at me for some time, muttered,

“Indeed... In all the years I’ve lived, you’re the first monster I’ve ever seen like this. You’ll make a good rival for my eldest grandson.”

“Your eldest grandson’s name is...?”

“Peng Dojin.”

“Pengdori? That’s a great starter Pokémon. Cute, too.”

“What the hell are you talking about? Peng Dojin! Peng Dojin! The one who gave you a close fight at the Star-Array Grand Banquet!”

Jeok Cheongang, who had been swaggering along like a back-alley thug, kindly added an explanation.

“The one you beat like a dog for fifteen minutes until he surrendered. Was he thirty?”

“Ah. Now I remember. He used his saber as a cane at the end.”

“Y-you... You...!”

“It’s all right. When people are young, they get beaten here and there, and they lose sometimes.”

Jeok Cheongang accepted my words with a bright expression, like a child who had just received a Christmas present.

“Peng boy, it’ll still be the same when he gets older, so don’t get your hopes up. No matter how hard he tries, he’ll just end up like his grandfather—unable to Return to Youth, growing old and dying.”

“You son of a—!”

“Ahem.”

No matter how I looked at it, the greatest victim here was the Azure Sky Sword King.

Even though he said nothing, he kept taking solid hits from every direction. The skin beneath the old swordsman’s eyes trembled.

Mae Jonghak’s next comment drove in the final nail.

“Don’t be so impatient, everyone. If you just keep at it, it happens naturally.”

“...!”

“...!”

*Was that supposed to be words or a fart?*

If Returning to Youth happened naturally, half the martial artists in the world would have already Returned to Youth.

Just as the Thunderbolt Saber King and the Azure Sky Sword King fell silent, unable even to get angry at Mae Jonghak’s completely unmalicious words, the largest and tallest pavilion I had seen in the Murim Alliance came into view.

“Please come inside.”

At first, I thought it was where the Alliance Leader lived, or something like that.

But that assumption was proven wrong before we even opened the door.

Tap-tap-tap-tap!

“A letter has arrived from Jiangsu!”

“What’s the Grade?”

“Earth Grade.”

“Organize the related matters and relay them. Have So Pyeong, Hwangso, and Jang Il-pal submit their reports within half an hour.”

Whoosh, whoosh, whoosh!

People hurriedly moved around the pavilion. Bamboo slips and documents traveled through mysterious cylinders intricately connected throughout the building.

Thousand-Faced Fox Song Ho watched the entire chaotic scene carefully before opening his mouth.

“Hubei. Wudang. Heaven Grade.”

Someone in scholars’ robes heard the short string of words and pulled on a ring.

The next moment—

Whoosh! Thunk!

A bamboo slip that had fallen through the cylinder hanging beside us unfurled.

“This is why we summoned you here. It is an urgent report that arrived from the Wudang Sect of Hubei five days ago.”

I could not hear what he said.

I stared at the contents written on the bamboo slip—or rather, at the picture—and muttered inwardly.

*The Water God Dragon... wasn’t the whole story.*

Something unidentifiable had been drawn in black ink.

It was a monster unfamiliar to some, yet strangely familiar to others.
## Chapter artifact 522

# Chapter 522

“Fuck. It’s one problem after another.”

It felt like I had been struck hard in the back of the head.

Nothing in this world was absolute, but I had still thought the events in Hubei had been wrapped up properly…

*The Water God Dragon wasn’t the only thing affected by mana.*

Had another Gate opened somewhere else? Or had some of the mana the Water God Dragon failed to absorb leaked out and affected something else?

Looking at the picture made my mouth feel gritty, as if I were chewing sand.

I was not the only one who understood how serious the situation was.

“What in the world is that?”

“One thing seems certain. It is something that cannot be called human.”

The Thunderbolt Saber King and the Azure Sky Sword King muttered to themselves. Mae Jonghak then opened his mouth.

“According to what Wudang told us, that bizarre existence is the true identity of the Killing Ghost that had been spreading terror across Hubei recently.”

“The Killing Ghost?”

Jeok Cheongang narrowed his brow and looked in my direction. I understood the meaning in his eyes and nodded.

“It’s probably the one you know.”

“Damn it. They say it’s darkest beneath the lamp.”

He was right. This was exactly what they meant by darkness beneath the lamp.

But in this case, we could not have recognized it. The lamp had been so bright that we could barely open our eyes.

With hundreds of people dying all over Hubei Province, it would actually have been strange to focus on the Killing Ghost already being pursued by Wudang.

That was even more true when the culprit finally revealed was an imugi driven mad by mana.

*We didn’t have time to worry about anything else.*

I had never imagined that another monster would appear. I had assumed the Killing Ghost was nothing more or less than the sort of lunatic commonly found in the Murim.

*Come to think of it, what kind of monster is this bastard?*

The pictures from this era were exactly the sort of crude drawings one saw in history textbooks. The same was true of the picture drawn on the bamboo slip.

There were signs that someone had tried to depict it as accurately as possible, but it was obviously lacking in many ways, including any sense of depth.

There was only one thing we could determine from the picture.

Just as the Azure Sky Sword King had said, it was another existence that was not human.

The horn jutting from the center of its forehead. Its arms and legs, absurdly long and thick.

Its red eyes were the only part drawn in color, and they were beyond anything the four words *demonic, heterodox arts* could explain.

*It’s definitely a monster. But was it mutated by mana, like the Water God Dragon?*

Tap. Tap.

I had been anxiously drumming my fingers against the wall when I asked,

“Are there any other pictures?”

The Thousand-Faced Fox, who had been watching me closely, nodded.

“Unfortunately, there are not. That was the best Wudang could do.”

“That’s a shame. But I don’t think this is everything.”

“You’re quick. A second letter arrived from Wudang two days ago.”

At the Thousand-Faced Fox’s signal, the middle-aged scholar pulled on the ring again.

Whoosh—thunk!

An oval wooden case came sliding down through the round tube. Inside was a letter covered in densely packed writing.

“Read it yourself. You were at the center of the incident in Hubei, so you may notice something that I and the Hidden Shadow Pavilion failed to discover.”

“I was planning to do that anyway.”

“This old man will read it with you.”

Jeok Cheongang and I put our heads together and read through the letter.

Once did not seem sufficient, so we read it a second time, then a third. Only after fifteen minutes had passed did we finally take our eyes off the letter.

“What do you think?”

At the Thousand-Faced Fox’s question, Jeok Cheongang furrowed his brow.

“Who knows?”

“I see.”

“…Why aren’t you asking anything else?”

Because you never expected much in the first place.

But I had nothing particularly useful to say either. If the letter contained everything it claimed to, then the Thousand-Faced Fox and the Hidden Shadow Pavilion had already managed to uncover most of the circumstances that led to the monster’s appearance.

“As you can tell from the letter, this monster was originally a fisherman who lived at the mouth of the Yangtze.”

I pointed to the first line of the letter and continued.

“It says his name was Jang Sam, that he was in his fifties, and that he had a family.”

Wudang had not thought that a monster like this had simply fallen from the sky.

After carefully examining the corpse of the dead monster, they had discovered several distinguishing features.

They immediately began an investigation based on those findings and determined that the monster had been a fisherman who lived in a village less than a hundred li from Mount Wudang.

“They say he went out alone to fish more than a month ago and vanished without a trace. When he failed to return after several days, his children petitioned the local authorities.”

The local authorities probably had not been able to find him either.

Fishermen dying was not common, but it did happen from time to time. Besides, Hubei Province had been drowning in fear and chaos because of the succession of disasters.

With high-ranking people dropping dead here and there like minions in some canyon, who would have spared any thought for a mere fisherman?

*Even if they had actively searched for him, they probably couldn’t have found him.*

Even Wudang’s masters had needed quite some time to capture Jang Sam. Under those circumstances, the local authorities would have accomplished nothing even if they had joined the search.

And in truth, there was something far more important than those circumstances.

How had an aging fisherman, once as ordinary as they came, become a hideous monster known as the Killing Ghost?

“Do you have any idea what caused this?”

At the Thousand-Faced Fox’s question, I opened my mouth.

“I think the Blood Fish is the most likely culprit.”

“I have already received a report regarding the Blood Fish. In fact, I have dispatched several Hidden Shadow Pavilion agents to Hubei and ordered them to capture a live specimen.”

“Good call. Jang Sam, who became a mon—who became a monster, was originally a fisherman, and Dongting Lake is connected to the tributaries of the Yangtze…”

Mae Jonghak, who had been listening quietly, nodded and muttered,

“There is a chance Jang Sam ate one of the Blood Fish that flowed out through those tributaries.”

“Or was eaten by one.”

“……!”

“……!”

“In any case, that seems the most likely explanation for now. His hideous appearance, as well as his ability to evade Wudang’s pursuit for several days, was probably because the change made him stronger.”

The Thousand-Faced Fox added in a stiff voice,

“Just as the imugi you defeated appeared, what do you think of the possibility that the same thing occurred somewhere else? The phenomenon known as a ‘rift.’”

“…”

“Tell me. I wanted to hear it directly from you.”

In our terminology, it was a rift. In other words, a Gate.

I had thought about the possibility before.

But I did not want to think about such a situation, much less say it aloud.

I did not believe in superstitions, but people said that speaking of something could make it happen. If I was being honest, I wanted to rule out even the smallest possibility.

Still, I could not avoid answering. I opened my mouth with an uncomfortable expression.

“I can’t say for certain, but I think the possibility is fairly low.”

“Why?”

“If the same thing had happened, it wouldn’t have ended with something this minor.”

The second Gate had not erupted yet. That was my conclusion.

It was certainly something we should have been relieved about, but the expressions of several people who already knew the circumstances—including me—remained grim.

They must have realized the true meaning behind my words.

Put simply:

*It hasn’t happened yet. But if another Gate blows, we’re truly fucked.*

“A powder keg. There is no better way to describe it than a powder keg.”

The Thousand-Faced Fox muttered the words under his breath.

A powder keg was safe as long as no fire touched it. But that also meant it became more dangerous than anything else the moment someone set it alight.

You might wonder what kind of lunatic would do such a thing, but unfortunately, the lunatics known as Dark Heaven had already lit the powder keg that was Hubei Province once before.

The Murim of today was no different from a gigantic powder keg on the verge of exploding.

And the second and third Gates would be the enormous sparks that set it off.

*There is at least one thing we can be thankful for.*

I did not know the true identity of that bastard, the Lord of Heaven. I also did not know how the Southern Heaven Demon Empress had opened the Gate.

But there was one thing I could guess.

*Opening a Gate isn’t easy for them either.*

A Gate was not the front door of an inn. If they could fling them open whenever they wanted, the entire Murim would already have descended into complete chaos.

Orcs would have founded sects, while Lycanthropes and ogres would be walking arm in arm down the main roads of Henan.

Before the Murim Alliance could even be formed, everyone would be shouting, *Uh, fuck, what are those things?* Then we would have fallen apart completely.

But Dark Heaven had not done that.

Why?

Because it was difficult.

That was why we needed to hurry even more. We had to stop them before another powder keg exploded.

The second thing we could be thankful for was that this enormous group, united beneath the banner of the Murim Alliance, had more than enough ability to do so.

“A calamity has befallen the Murim. Something far more enormous than I imagined.”

Mae Jonghak muttered the words like a sigh. The Thousand-Faced Fox opened his mouth with a rigid expression.

“There is something we need to investigate immediately. Alliance Leader, I apologize, but would you move elsewhere with the others?”

“Of course.”

“Understood. I will report to you later. Then I will see you all next time.”

Those were the Thousand-Faced Fox’s final words.

Before we had even left the pavilion, urgent shouts rang out from every direction. The people who had been worn down by exhaustion opened their eyes wide as though they had never been tired and began moving according to their orders.

The Hidden Shadow Pavilion, which had maintained its existence even after the dissolution of the Murim Alliance, had begun moving once again.

And they were not the only ones who suddenly became busy.

“I should go as well. I’ll soon be buried under a mountain of work.”

At Mae Jonghak’s words, the Azure Sky Sword King nodded.

“I am in the same position. Would it be all right if I told my good-for-nothing son what I heard here today?”

“You seem to have forgotten who brought you here.”

If this had been classified information that could not be told to anyone, the Alliance Leader and the Chief of the Hidden Shadow Pavilion would never have brought them here themselves.

Understanding the meaning in Mae Jonghak’s words, the Azure Sky Sword King clasped his hands in a formal salute.

“Thank you.”

“It will be public knowledge in a few days. Until then, be careful not to let anything slip.”

“Of course. I will bear it in mind.”

The Thunderbolt Saber King seemed to have grasped the seriousness of the situation as well. He opened his mouth with a stiff expression.

“Hey, Sword Saint. There is something I would like to ask you, too.”

“The same goes for the Hebei Peng Family. It doesn’t matter if you tell them—”

“No, not that. What in the world did you talk about in there?”

“…”

“…”

*Is this really the Intelligence level of the Grand Family Head of the Hebei Peng Family? My pecs are getting majestic…*

When everyone, myself included, gave him a thoroughly cold look, the Thunderbolt Saber King mumbled as if making an excuse.

“You have to talk about things people can actually understand. I know a great pleasure has befallen the Murim, but…”

“Peng.”

“Yeah?”

“Then keep your mouth shut for a while. This old man thinks that would be helping.”

“What did you say?!”

Jeok Cheongang let out a deep sigh and looked at Mae Jonghak.

“I’ll take care of this stupid old man, so go on. You must be busy.”

“Thank you. By the way, Great Hero Jeok.”

“Speak.”

Mae Jonghak clasped Jeok Cheongang’s hand tightly and continued.

“Do you really have no intention of becoming the Alliance Leader?”

“…”

“…”

*Be honest. You and Cheongpung are related by blood, aren’t you?*
## Chapter artifact 523

# Chapter 523

Ssssss.

It was hot. The Scorching Yang Qi surging from my dantian spread through my limbs and bones, racing along my acupoints. Everything felt quiet and vivid.

I circulated my internal energy along the Eight Extraordinary Meridians.

Once, twice, three times…

Circulating qi was like rolling a snowball down a high hill. With every repetition, the snowball grew larger.

But it could also pick up foreign matter along the way—dirt, stones, twigs, and the like.

That was turbid qi, which muddied the purity of one’s internal energy. Repeating the circulation burned away that turbid qi and refined the internal energy.

*More. More. More.*

I muttered the words in a daze as I continued circulating my energy.

Internal energy amounting to no less than three jiazi transformed into the shape of a fire dragon and swam fiercely through my body.

Within the mental image I had created, the fire dragon grew larger, its heat blazing hotter and hotter.

Then, at some point, I realized it.

*Now.*

Fwoosh.

At my command, the Scorching Yang Qi surged in every direction. It was truly overwhelming heat. It felt as if a small sun had exploded inside my body.

My closed eyes grew hot, and it felt as though flames were flowing from my nose instead of breath.

No. It wasn’t merely a feeling. That was certainly what was happening.

Just as too much water overflowed, the internal energy filling my body was flowing outward.

The heat flowing from the seven openings known as the seven apertures—my eyes, nose, mouth, and so on—scorched the air around me.

The same thing was happening in the countless pores covering my entire body.

Ssssss.

I could feel it—the enormous flow of qi gathering above my crown. At the same time, I began drawing a picture on the clean, blank canvas spread across my mind.

I was the master of myself. Every acupoint inside my body and every strand of energy that had flowed outside belonged to me as well. None of it could defy its master’s will.

I could not see it, but I could feel the Scorching Yang Qi gathered above my head taking the shape I wanted.

One, two, three.

Three petals, colored red as if they were burning.

*Three Flowers Gather at the Crown.*

It was the result of adding enlightenment to the Supreme Peak realm.

Any martial artist in the world would dream of reaching this realm, but I had merely crossed one hill.

Hoo.

The short breath escaping my lips carried the remnants of turbid qi filtered out through circulating my internal energy.

After expelling even the last handful of turbid qi and clearing my internal energy and mind, I took a step toward the next hill.

*Five Qi Returning to Origin.*

Even after opening my Middle Dantian, I had tried to reach this realm several times, but I had never succeeded. It was another wall blocking my path.

*I’ll cross it. Right now.*

Along with my firm resolve, a corner of my chest gave a sharp, tingling thrum.

I could not let go of the thread of tension I was holding. Even if I recklessly punched the wall without considering the consequences, all I would accomplish was injuring my fist.

To put even a hairline crack in the wall, I had to read the exact flow of energy while maintaining that tension.

*If I let my guard down even slightly, my internal energy could reverse its flow.*

Walking along an existing road was easy.

But this was the process of carving out a new path of my own. I had to move boulders and hack through the undergrowth. I could also slip while climbing a cliff.

A reversal of internal energy led to an Internal Injury, and if I continued recklessly forcing my way forward while injured, I would be practically asking for qi deviation.

According to Jeok Cheongang, more than a few martial artists had died or been left half-crippled that way.

I had no intention of ending up in a wheelchair while Dark Heaven was taking a gigantic dump all over the Murim.

*Slowly. Carefully.*

Fortunately, my training with Mungyeong had helped immensely.

The Scorching Yang Qi built through the Fire Gate Divine Technique, the cultivation technique at the foundation of the Fire Gate Clan, possessed power and explosiveness at least on par with the cultivation techniques of other prestigious sects.

But its movements were just as rough.

Through this training, I had managed to make up for some of that imperfection.

*I can do this. As long as I keep my head straight, it’s entirely possible.*

It was warm. The Three Flowers Gather at the Crown trembled above my head.

*But don’t worry. Internal energy is faster than hands.*

*First ring.*

That was when I began moving my internal energy carefully.

“Rein in your internal energy. It’s a waste of effort for now anyway.”

“……!”

Crack!

My concentration shattered at the sudden voice, and the internal energy that had been taking shape as Five Qi Returning to Origin scattered to pieces.

At the same time, my internal energy reversed its flow. Gastric juices surged up from deep inside my body, and I vomited.

“Oooooogh!”

Splash!

Vomited matter mixed with a small amount of blood spilled onto the floor.

*Fuck. So this is where the Niagara Falls I saw in pictures were hiding.*

After spewing out everything that had surged up and panting for breath, I saw the side dishes I had eaten that morning waving at me from the floor.

“Uweeegh! Bleeegh!”

Ah, I couldn’t hold that back.

Only after emptying my stomach several more times did my mind finally clear. I glared at the owner of the leather shoes who had already moved a considerable distance away.

“What are you doing right now?”

Mungyeong, who was carefully examining the leather shoes he was wearing, answered,

“I bought these shoes only three days ago. It would be troublesome if they got dirty.”

“That’s not what I meant. Why did you speak to me while I was circulating my qi?”

“I didn’t even touch you, so what’s the problem? You’ve reached that realm, yet your composure is shattered by a few words. That is your deficiency.”

“You startled me!”

“I was startled too. What the hell did you eat yesterday and today to produce that much…?”

Mungyeong frowned as he looked at the mess of vomit covering the floor.

“The more I look at it, the filthier it becomes. Judging by the shape, it does vaguely resemble Five Qi Returning to Origin.”

“Hey, Mr. Moon!”

“Did you just call me ‘Mr. Moon’?”

I met Mungyeong’s cold stare without flinching.

One second. Two seconds. Three seconds.

*Hmm. That should be enough.*

“I misspoke. I must have suffered a serious Internal Injury.”

“Looking at you is making my qi-sea acupoint throb.”

I avoided Mungyeong’s completely deflated stare and hurriedly changed the subject.

“But what brings you here all of a sudden? No, before that, how did you get in?”

“Why do you think there is a door?”

“But Mujin was guarding the door…”

That was when my voice trailed off.

Slide. Thump!

A figure collapsed with a faint flop through the half-open doorway.

The back of the head was so familiar that my eyes widened before I could stop them.

“Mujin! Hyuk Mujin!”

As I shouted, Mungyeong spoke in a grim voice.

“Leave him. He won’t wake up even if you shake him.”

He wouldn’t wake up even if I shook him?

This blood-crazed Killing Ghost had finally done something.

I roared furiously.

“You cold-blooded murderer! You’re just like that bastard the Slaughter Saint!”

“I tried to wake him because he was sleeping in front of the door, but he didn’t move at all… What did you just say?”

“Huh?”

“I asked what you said.”

“What?”

*What the fuck?*

Right on cue, Hyuk Mujin’s corpse—or rather, his body—twitched.

Along with a vigorous snore.

“Grrrrrr.”

“……”

“……”

Our gazes collided silently in midair. I opened my mouth with a charming smile.

“There seems to have been a very slight, insignificant misunderstanding.”

Mungyeong answered with a dry expression.

“It doesn’t seem to have been a misunderstanding. Nor does it seem insignificant.”

“Can’t we just agree that good is good?”

“You mean dead is dead?”

“Oh… How did you get that from what I said?”

“There’s no reason it couldn’t be. Do you have a problem with it?”

I did have a problem with it, and his cochlea also seemed to have a serious problem, but I lacked the courage to point that out.

“I was wrong.”

“Does apologizing make everything end?”

“I believe sincere conversation can untangle every knot.”

“Good. Then go talk things out with Dark Heaven’s Lord of Heaven. And wipe that irritating smile off your face before I tear your mouth apart.”

“Our ancestors used to say that you can’t spit in a smiling face.”

“Ptui.”

Smack.

Hmm. Our ancestors had been wrong.

But the more important the moment, the more important it was to regain my composure. I calmly wiped the spit from my cheek.

“You have an incredible launch speed. I thought it was a hidden weapon.”

“If I spit while infusing it with internal energy, I can burst out a person’s eyeballs.”

“That’s impressive. Are you a member of the Zerg by any chance?”

“I’m the Grim Reaper.”

“……As I said, I’m deeply sorry.”

Mungyeong looked at me as though he were wondering how many pieces he would have to cut me into for people to say I had died properly, then clicked his tongue.

“Enough. Every time I talk to you, I feel my energy being sucked away.”

“……”

*Who does he think he’s talking about? My life force is draining away by the second.*

I would bet Hyuk Mujin’s left atrium that the conversation just now had shaved at least three days off my life.

*That bastard Hyuk Mujin. I told him to stand guard, and he couldn’t even resist going back to sleep.*

Mungyeong was something else, but Hyuk Mujin was no less impressive.

“But what brings you here…?”

“You make it sound as though you’re asking why I came here to do some other dogshit thing.”

“Oh.”

“Oh?”

“Oh… no. I was just curious.”

“It must be my imagination, but I think your pronunciation has become rather strange since we last met.”

“Of course. It’s your imagination.”

Mungyeong let out a small sigh and threw the bundle in his hand.

Thump.

I caught it reflexively and stared at it with wide eyes.

“What is this?”

“A pill.”

“A pill?”

*Is this Santa Claus in spring? Why is he suddenly giving me a present?*

I undid the bundle with mixed feelings and found a small, solid-looking wooden case inside.

At the same time, a strange fragrance seeped deep into my nose.

*This is…*

They said that with elixirs like this, you could recognize their effects before even seeing them. This was exactly such a case.

Before opening the wooden case, I realized that the pill inside possessed considerable efficacy.

Click.

When I opened the case, a reddish pill came into view. Even at first glance, it was clearly no ordinary pill.

I stared blankly at it, then raised my head and looked at Mungyeong.

“What are you staring at?”

“I was wondering why you suddenly decided to give me something like this.”

“It contains a considerable amount of fire qi. It will help you.”

“What?”

“Do you have a hidden weapon stuck in your ear? Don’t make me say it twice.”

“No, I wasn’t asking about its efficacy…”

Mungyeong’s face crumpled. It was such an expressive display of emotion that I could hardly believe it was the same Mungyeong whose expression was usually bleak.

“I found it on the way here.”

“……?”

“Correction. I saw it while passing by and bought it. Satisfied?”

*What do you mean, satisfied, old man?*

I touched the red pill inside the wooden case.

*Item check.*

Ding.



> **System**
>
> **Mungyeong’s Specially Crafted, Custom-Made Pill for Jin Taekyung**
>
> Would you like to view more detailed information?
>
> **Y / N**

*Yeah. No. That’s enough.*

I closed the simple System window and stared at Mungyeong with a tepid gaze.

“‘I saw it while passing by and bought it.’ Yes, I see.”

“……What is that look?”

“Nothing. In any case, I’ll accept it gratefully.”

What I felt toward Mungyeong right now was exactly half gratitude and half fear.

*Thanks for the good pill, but what in the world is the next training session going to be…?*

When someone suddenly treated you this well, it felt like they were feeding a condemned man a proper meal.

As if he had sensed the meaning behind my trembling gaze, Mungyeong opened his mouth.
## Chapter artifact 524

# Chapter 524

Hyuk Mujin woke up fifteen minutes after Mungyeong left.

He poked his head through the gap in the open door. The moment our eyes met, he spoke with a solemn expression.

“Your qi circulation is complete.”

“Yeah. Your life is about to be over, too.”

“Hyuk Mujin, Vice Squad Leader of the Jin Dragon Squad of the great Jin Family of Taiyuan. As the Captain ordered, I was guarding the door so that not even a single ant could get inside.”

“…Are you seriously insane?”

Look at this bastard, acting proud after letting everyone but the ants inside.

It was utterly ridiculous, but I decided to give him high marks for the sheer nerve it took to lie so brazenly while snoring his head off.

“Close the door and get lost.”

“Yes, sir.”

Perhaps he felt guilty, because he didn’t offer even a word of protest before scampering away.

Just as Hyuk Mujin was about to shut the door, I asked him something that had suddenly occurred to me.

“Wait. What about the others?”

“Who do you mean by ‘the others’…?”

“All of them.”

Hyuk Mujin thought for a moment before answering.

“First, the Lesser Family Head is meeting with the Sect Leaders and Family Heads of the other factions.”

“The Sect Leaders and Family Heads?”

“Yes. It seems he’s been meeting with them more often for the past two days.”

Two days ago. That would be the day a few of us, including Jeok Cheongang and me, had gone to the Murim Alliance.

*It was about time the subject came up.*

At the very least, the heads of the Nine Sects and One Gang and the Five Great Families should have received some warning.

With all sorts of information and problems related to Dark Heaven coming to light, it was only natural for them to put their heads together and devise a countermeasure.

“Oh, and we handed the Three Fiend over to the Murim Alliance. I heard they were going to summon some master to interrogate him…”

“Really?”

The third of the Qilian Three Fiends, who had stained Sichuan with blood under the command of the Western Heaven Demon Lord, had a remarkably tenacious life.

A lot had happened while he was bound and brought all the way to Henan, yet unlike his two brothers, his head was still attached to his neck. That alone proved how lucky the bastard was.

It was just a different part that had fallen off instead.

*If he kept saying he didn’t know anything even while they were cutting off his balls, I doubt there’s much more they can learn through interrogation.*

Even for a Supreme Peak master—hell, for anyone—one’s balls were precious.

Gung Gibang and Hyuk Mujin had once held a hundred-minute debate over which mattered most: one’s life, one’s dantian, or one’s balls.

*In any case, I did as ordered and handed the Three Fiend over. The Murim Alliance can handle the rest.*

Well, what happened after that was none of my concern. I could only hope the Murim Alliance managed to obtain more information about Dark Heaven through further interrogation.

“Forget my eldest brother. What about the others? I haven’t seen them anywhere.”

“Young Hero Gung moved to a different lodging.”

“He moved? When?”

“About one or two shichen ago. You were busy circulating your qi, so I took the message for you.”

“…You weren’t asleep then?”

“What are you talking about? I told you I stood guard like an iron wall.”

“Ugh. This bastard really can’t open his mouth without—”

When I raised my fist, Hyuk Mujin hurriedly continued.

“The Beggars’ Sect! He said he would be staying at the Henan branch of the Beggars’ Sect, so we should come find him anytime something happens.”

I stopped just before punching him.

“The Beggars’ Sect? Why would he go there?”

“What?”

Hyuk Mujin looked at me as though I had said something absurd.

“May I ask which faction you belong to, Captain?”

“What kind of stupid question is that? Obviously, the Jin Family of Taiyuan or the Fire Gate Clan.”

“And Young Hero Gung?”

“…Oh, shit. Right. That guy was the Beggars’ Sect Successor Beggar.”

I had forgotten because he clung to me like a burr. Come to think of it, he had a master and a sect of his own. It would be unreasonable for him to stay with us even in Henan.

“Wait. Did Cheongpung leave too?”

“Of course.”

“…Really?”

*Things should be quiet for a while, then.*

And yet, for some reason, I felt both relieved and disappointed. Of course, I would continue seeing both of them in the future, but the place felt strangely empty without those two who were always making a racket.

“They could’ve at least said goodbye before leaving.”

At my mutter, Hyuk Mujin looked me up and down as though I were some strange creature.

“Why would they say goodbye?”

“Why are you so devoid of sentiment? We’ve spent all this time together, and they just left without saying goodbye?”

“Do they really need to say goodbye when they’re only stepping out for a bit?”

“…?”

“They went to the marketplace for sweetmeats and dumplings.”

“…”

*Shit. Give me back my sentimentality.*

I was momentarily speechless. Hyuk Mujin cast me a meaningful look.

“Captain.”

“Shut up.”

“I haven’t said anything yet.”

“That’s why I’m telling you to shut up.”

“I’ll stay by your side no matter what happens, Captain.”

“…Please get away from me.”

“Come on. You like it, so why are you acting like this?”

I was annoyed, but more than that, I was mortified as hell.

As I sighed, Hyuk Mujin, who had been needling me from the side, suddenly asked as though he had just remembered something.

“By the way, you haven’t asked about Mungyeong.”

“I already saw him.”

“You did? He’s seemed pretty busy lately, too. He’s been gathering strange medicinal ingredients, boiling them, pounding them… He looked completely swamped. When did you see him?”

“When you were sleeping, you bastard!”

Wham! Wham! Wham!

“Urgh! Oof! Ugh!”

“Go! Get out right now!”

After taking a thorough beating, Hyuk Mujin looked at me with tears welling in his eyes.

“Do you hate me that much?”

I immediately shook my head.

“No. I want to kill you.”

“That’s too harsh. Really.”

“You were told to stand guard for a moment, and you went straight to sleep! After sleeping that long, you must’ve dreamed the entire *Dream of the Nine Clouds*.[^1] You bastard.”

“Why do you hate only me, Captain?! I hate you too!”

“…”

Tap-tap-tap. Slam!

I was left speechless as Hyuk Mujin vanished, scattering tears behind him.

*What the hell.*

A man well past his mid-twenties, and this was the level of his dialogue? My fists were attaining grandeur.

I was letting out a heartfelt sigh when the door opened again, and Hyuk Mujin poked his head through the gap.

“Um…”

“Welcome back. Our Mujin has come to pick out his burial plot.”

“No. That’s not it. I came because I was worried you might misunderstand.”

“What?”

“I didn’t shut the door that hard on purpose. The wind was strong.”

“…”

“Well, I’ll be going now. Good work, sir. Loyalty.”

Should I really kill him?

He was acting exactly like an elementary school student who had just been scolded by his mother. I stared at the door, which had been closed again with the utmost gentleness, then shook my head.

Then I turned my gaze back toward the empty space I had been watching until Hyuk Mujin woke up.

**Item Window**

> **System**
>
> **Mungyeong’s Specially Crafted Custom Pill for Jin Taekyung**
>
> **Type:** Elixir  
> **Grade:** Peak  
> **Restriction:** None (but the effect increases if the user is **Jin Taekyung**)  
>
> **Description:** A pill focused on stability and recovery rather than increasing internal energy. If taken while internal energy is unstable, it stabilizes the user’s energy and greatly increases their recovery.
>
> **Special Note:** Since it was made with **Jin Taekyung** in mind, that individual will receive an even greater effect upon taking it.

“…Hmm.”

I quietly caressed the reddish pill—the so-called *Mungyeong Special Jin Custom Pill*—then placed it back inside the wooden case.

*Inventory open. Store.*

A System notification appeared, informing me that the item had been stored.

But I was already thinking back to the conversation I had shared with Mungyeong before he left.

*Training ends here.*

*Pardon?*

*Why? Are you disappointed?*

A lot of emotions seemed to pass through me in that moment. After hesitating, I answered,

*…To be honest, I can’t say it’s welcome news.*

*Why?*

*I want to become stronger. Much stronger than I am now.*

*What a greedy bastard. Aren’t you already strong enough?*

*Isn’t that just how people are? No matter how much we fill ourselves, there’s never an end to what we want?*

Mungyeong stared at me for a long time after I questioned him in return, then let out a quiet laugh.

It was the first smile I had seen from him since meeting him.

*You’re finally starting to sound like a Murim practitioner.*

*I am a Murim practitioner.*

*Then let me ask you again. Do you want to become an assassin, or a Murim practitioner?*

*I want to become strong. Strong enough that no one would dare touch me. Strong enough that everyone around me would be safe simply because I exist.*

*The Invincible… That’s an ambitious dream.*

The Invincible. It was a distant and grandiose word.

Even the Martial God had enemies. The Heavenly Demon, master of the Demonic Cult, and his hundred-thousand-strong army of the Demonic Path had been the Martial God’s adversaries.

*You really do dream big.*

*Even if reality is a cesspit, your dreams should be big and lofty.*

*How amusing. It’s obviously ridiculous bluster, yet when it comes from your mouth, it sounds surprisingly plausible.*

*Pardon?*

*Nothing. And if that’s your reason, then you must not learn my martial arts.*

*Why not?*

*Anything becomes poison in excess. You don’t need two wells right now.*

*…Dig only one well?*

*Did you just speak informally to me?*

*No, that’s not what I meant.*

*I made this decision after a great deal of thought. Keep that in mind.*

*Is it because my talent is lacking?*

That was the question I threw at Mungyeong as he was about to leave.

His answer was brief and concise.

*The opposite.*

*Pardon?*

*If you were a weak man lacking talent, I would have taught you even more. To survive, you would have needed to learn whatever you could.*

Those words suddenly brought back my days as an F-rank Hunter.

No matter how carefully you chose your position and entered battle, danger could be hiding anywhere.

Without a tank’s protection or cover from a mage or archer, you were ultimately on your own.

If I dropped my spear by mistake, I cut a goblin’s throat with the dagger I carried. If the dagger broke, I picked up a rock and smashed in its head.

I did whatever it took to survive.

The reason I carried a spear wasn’t because I had any particular talent for using one. I simply thought that keeping more distance from monsters might increase my odds of survival.

*Judging by your expression, something seems to have clicked.*

*…I think I understand some of what you mean.*

*The martial arts I learned and the martial arts of the Fire Gate Clan are fundamentally different. I was raised as an assassin from the beginning, and I lived as one for more than half my life. Our starting points are different. Even if I taught you my martial arts, there’s a good chance you wouldn’t be able to make them your own merely by following the formulas.*

*Is that why you’re stopping my training? I thought we were only just getting started.*

*Started? You already know everything.*

*Pardon?*

*What matters is not martial arts, but martial principles. That is everything I possess, and the foundation behind the title Slaughter Saint.*

I could still remember the look in his eyes at the time. That inscrutable gaze whose meaning I could never understand.

And I could still remember his voice.

*There were three hundred of us at first. We all learned the same martial arts and underwent the same training. After ten years, only twenty of the three hundred raised as assassins remained. After another ten years, only one person remained.*

I didn’t need to ask who the last person in that story was.

Mungyeong, his inscrutable gaze reaching back through the distant past, turned away.

Then he left me with one final sentence.

*I taught you the martial principles you needed more than anything. Combining martial arts with different textures is nearly impossible, but principles have no texture. Try incorporating those principles into the martial arts you’ve learned. This is your final task.*

Thump. Thump.

I suddenly came back to myself.

Someone outside was knocking on the door, and I recognized the presence immediately.

“Hyuk Mujin?”

“Captain. It’s time. You should come out.”

*It’s time?*

The question that rose in my mind vanished almost immediately.

I suddenly realized what day it was.

*The Murim Alliance.*

Today was the day the Murim of the world would stand beneath a single banner.

[^1]: *The Dream of the Nine Clouds* is a classic Korean novel in which a man experiences an entire lifetime within a dream.

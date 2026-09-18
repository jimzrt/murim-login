# Checkpoint Review — 320–324

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

# Chapters 320–324

## Plot

At Tengwang Pavilion, Jin Taekyung confronts Hwangbo Eom, the Taeeul Merciless Sword, and accuses the Zhongnan Sect of using a substituted Hundred-Year-Old Snow Ginseng shipment to destroy the Yongbong Escort Bureau. Hwangbo threatens Taekyung and orders him to withdraw, but Taekyung refuses and protects Ju Hwaran.

Taekyung’s preparations bring Xi’an Beggars’ Sect records and Lower District Sect intelligence to the pavilion. Wolhwa confirms that she accepted his commission, while Heukgeol and Gung Gibang mobilize their organizations. The records show that Zhongnan covertly manipulated the Yongbong Escort Bureau’s failures for two years, including the failed Geumo Merchant Guild transaction and the disappearance of the Thousand-Year Snow Ginseng.

Hwangbo responds by attacking Taekyung and ordering the Taeeul Sword Unit to seal the pavilion. Hyuk Sopyung obeys after Hwangbo produces the Zhongnan Sect Leader’s Command Token. Hwangbo also threatens the seriously ill Jeok Cheongang and the Fire Gate Clan. Taekyung orders the others to prevent anyone from leaving and fights Hwangbo inside the pavilion.

Although Taekyung remains below the Supreme Peak realm, his extraordinary physical abilities and Fire Gate techniques allow him to counter Hwangbo’s Heavenly River Thirty-Six Swords, Taeeul Light-Dividing Sword, and Taeeul Formless Sword. During the duel, Taekyung’s Flamefire Path advances to seven stars. Applying Jeok Cheongang’s instruction to see with his heart, he senses Hwangbo’s invisible attacks, then destroys Hwangbo’s treasured sword with Heavenly Strike and gravely wounds him. Taekyung condemns Hwangbo for insulting Jeok Cheongang, but the confrontation’s immediate consequences remain unresolved.

## Continuity

- Hwangbo Eom is gravely injured, and his treasured sword was destroyed by Heavenly Strike. He remains alive; his next action and Zhongnan’s response are unknown.
- Taekyung’s Flamefire Path is now seven stars. He is still below Supreme Peak but can defeat Supreme Peak masters through his physical ability, martial skill, and Fire Gate techniques.
- Taekyung has publicly identified himself as the Fire Gate Clan’s nineteenth successor.
- Hwangbo knows Jeok Cheongang’s illness is serious and has threatened Taekyung and the Fire Gate Clan.
- Jeok Cheongang remains unconscious and concealed beneath leather on Taekyung’s pack frame in a suspended-animation-like state.
- Hyuk Sopyung and the thirty-member Taeeul Sword Unit are sealing Tengwang Pavilion’s entrance under the Zhongnan Sect Leader’s Command Token.
- Taekyung has ordered Baek Museong, Cheongpung, Gung Gibang, Heukgeol, Wolhwa, Hyuk Mujin, Ju Hwaran, and the other attendees to prevent anyone from leaving.
- Wolhwa is the Shaanxi Branch Leader of the Lower District Sect and is providing intelligence and personnel under Taekyung’s commission.
- Heukgeol leads the Xi’an Beggars’ Sect branch as a three-knot disciple. Gung Gibang is the sect’s unique eight-knot Successor Beggar; they have been close friends since childhood.
- Beggars’ Sect and Lower District Sect records establish that Zhongnan manipulated the Yongbong Escort Bureau’s failures for two years. The specific participants, the timing of the ginseng substitution, and the full scope of the scheme remain unknown.
- Ju Hwaran suspected Zhongnan’s interference but could not oppose a member of the Nine Sects and One Gang. She intends to postpone accepting Taekyung’s praise until the escort mission is complete.
- The Yongbong Escort Bureau must still complete its current escort mission despite the exposed conspiracy, lost escorts, and Hwangbo’s attack.

## Translation Decisions

- Use **Taeeul Sword Unit**, **Taeeul Merciless Sword**, **Taeeul Light-Dividing Sword**, and **Taeeul Formless Sword**.
- Use **The First Sword of Zhongnan** for 종남제일검 and **Tengwang Pavilion** for 등왕루.
- Use **Flamefire Path**, **Heavenly Strike**, **hellfire**, **Force**, **Palm Force**, and **Sword Force** for the established technique terminology.
- Use **Blue Cloud Heavenly Force Palm** and **Fire Dragon Claw**.
- Use **Heukgeol Beggar**, **three-knot disciple**, **eight-knot disciple**, **Dragon-Head Gang Leader**, and **Law Beggar** for the Beggars’ Sect ranks and titles.
- Retain **Thousand-Year Snow Ginseng**, **Hundred-Year-Old Snow Ginseng**, **Lower District Sect**, and **Shandong Seongsu Jang Family**.

## Durable state

{
  "active_continuity": [
    "Taekyung's clash with Hwangbo Eom ended with Hwangbo gravely injured and his treasured sword destroyed by Heavenly Strike; the immediate fallout remains unresolved.",
    "Taekyung's Flamefire Path advanced to seven stars through enlightenment gained during the duel.",
    "Taekyung applied Jeok Cheongang's instruction to see with his heart, allowing him to sense and evade Hwangbo's invisible sword strikes.",
    "Taekyung remains below the Supreme Peak realm but can overpower Supreme Peak masters through his extraordinary physical strength, martial ability, and Fire Gate techniques.",
    "Wolhwa has accepted Taekyung's commission and is providing Lower District Sect intelligence and personnel for the investigation.",
    "Heukgeol is the three-knot head of the Beggars' Sect's Xi'an branch, while Gung Gibang is the sect's unique eight-knot Successor Beggar; the two have been close friends since their youth as beggars.",
    "Gung Gibang's order has brought approximately one hundred bamboo slips from the Beggars' Sect, alongside a comparable volume of Lower District Sect records.",
    "The Zhongnan Sect secretly manipulated the Yongbong Escort Bureau's failures for the past two years.",
    "Ju Hwaran suspected Zhongnan's interference but could not resist a member of the Nine Sects and One Gang; she will postpone accepting Taekyung's praise until the escort mission is complete.",
    "Jeok Cheongang remains concealed beneath leather at Tengwang Pavilion in a suspended-animation-like state.",
    "Hyuk Sopyung and the Taeeul Sword Unit are sealing Tengwang Pavilion's entrance under the Sect Leader's Command Token.",
    "Taekyung has publicly identified himself as the Fire Gate Clan's nineteenth successor."
  ],
  "continuity_sources": [
    324
  ],
  "open_questions": [
    "Who replaced the contracted Thousand-Year Snow Ginseng, and when did the substitution occur?",
    "Which Zhongnan figures participated in manipulating the Yongbong Escort Bureau's failures and arranging the shipment trap?",
    "What will Hwangbo Eom do after his defeat, and what immediate fallout will the confrontation cause?",
    "What further details will the Beggars' Sect and Lower District Sect records reveal about the two-year conspiracy?",
    "Can the Yongbong Escort Bureau complete the current escort mission after the conspiracy and Hwangbo Eom's attack have been exposed?"
  ],
  "safe_through": 324,
  "temporary_decisions": [
    "Use Tengwang Pavilion, The First Sword of Zhongnan, and Xi'an Branch Leader for 등왕루, 종남제일검, and 서안 분타주.",
    "Use Heukgeol Beggar, three-knot disciple, eight-knot disciple, Dragon-Head Gang Leader, and Law Beggar for 흑걸개, 삼결제자, 팔결제자, 용두방주, and 법개.",
    "Use Taeeul Formless Sword for 태을무형검 and Blue Cloud Heavenly Force Palm for 벽운천강수; render 강기 as Force and 수강 as Palm Force."
  ],
  "version": 1
}

## Reading copies

## Chapter artifact 320

# Chapter 320

The old man possessed an immortal-like bearing. I had heard that he was already nearing eighty, yet as befitted a Supreme Peak master with profound internal energy, his clear, refined face had not a single age spot, and his back was perfectly straight.

And then there were his eyes.

The old man, Hwangbo Eom, the Taeeul Merciless Sword, opened his mouth with that dark gaze that made people uncomfortable simply by meeting it.

“An interesting fellow has appeared.”

I did not avoid his stare as I answered.

“I hear that pretty often.”

“You have plenty of nerve, too.”

“That’s true as well.”

The corners of Hwangbo Eom’s mouth rose.

“You know who this old man is. Stop with the pointless wordplay.”

“Who are you?”

“What?”

“I’ve never met you before. How am I supposed to know who you are or where you’re from? You have to tell me. That’s basic etiquette.”

At my calm reply, startled gasps escaped from all around us.

“Y-Young Hero Jin.”

Ju Hwaran and the others from the Yongbong Escort Bureau stood there with their mouths hanging open, while the Zhongnan Sect disciples who understood what was happening reached for their sword hilts as if they had planned it beforehand.

“How dare he be so arrogant!”

“Can you not show proper respect at once?”

Hwangbo Eom raised a hand, calming the situation.

Normally, this was the point when someone would start foaming at the mouth and check their blood pressure as it shot through the roof.

But he was clearly different.

“So that’s how it is.”

Hwangbo Eom stared at me with a faint smile, then slowly turned his head.

His gaze passed over me, Cheongpung, and Hyuk Mujin before settling on the other two people.

“You don’t know this old man? The pillar of Huashan and the Successor Beggar of the Beggars’ Sect should have told you long ago. Excessive joking is unpleasant.”

At his words, Baek Museong and Gung Gibang flinched, stepped forward, and performed a clasped-hands salute.

“I am Baek Museong, a junior of the Murim. I pay my respects to Great Hero Hwangbo.”

“B-Beggars’ Sect’s Gung Gibang…”

“Enough.”

Hwangbo Eom waved a hand, his robe fluttering, and turned his gaze back to me.

“I believe I have indulged a child’s tantrum sufficiently. Is that still not enough?”

He really was no ordinary old man.

He was a completely different kind of person from his Senior Brother, the Roaring Fury Swordsman.

His martial arts and his personality were both a level above.

*He’s troublesome.*

Still, this was within the range I had expected.

Without letting my thoughts show, I calmly shrugged.

“No, that’s enough. Great Hero Hwangbo Eom, the Taeeul Merciless Sword.”

“You’re certainly bold. Why not make an excuse about failing to recognize me?”

“It’s a better look to admit it cleanly.”

“Hahaha. What an insolent brat.”

Hwangbo Eom burst into a hearty laugh. There was both interest in my existence and disbelief at the same time.

The Zhongnan Sect disciples under him, however, seemed to find this situation more than merely absurd. They seemed to consider it insulting.

It would have been one thing if I truly had not known who he was.

But I had known and pretended otherwise.

Apparently, Hwangbo Eom held an extraordinarily high position within the Zhongnan Sect if they could not simply laugh it off.

“You bastard!”

Was it called the Taeeul Sword Unit?

It began when a middle-aged man who appeared to be the oldest among the Zhongnan Sect disciples shouted and drew his sword.

*Clang-clang-clang!*

Thirty well-maintained swords pointed toward me. As disciples of the Zhongnan Sect, one of the Nine Sects and One Gang, every one of them was at least a First Rate master.

Of course…

*They’re hopelessly weak.*

At this level, they posed no threat to me whatsoever.

First Rate? Peak? It made no difference.

In my eyes, they were nothing more than thirty men with swords.

*I am strong.*

*Might Makes Right.*

One of the absolute laws governing the Murim.

By now, I had become strong enough to remain at ease within that law. That was why I could walk forward without hesitation.

“This is a fateful meeting and all. Would you mind if I joined you?”

I asked Hwangbo Eom that while ignoring the thirty blades surrounding me. The face of the middle-aged swordsman in charge flushed red.

“H-How dare this insolent bastard!”

“*Bangjajeon*[^1] is fucking great.”

[^1]: *Bangjajeon* (*The Servant*) is a Korean film title that echoes the word just used for “insolent.”

“Taeeul Sword Unit, listen up! Take this bastard—”

That was when Hwangbo Eom, who had been silently watching me, opened his mouth.

“Join us… Very well.”

“……!”

Everyone stared at Hwangbo Eom in surprise.

“S-Senior Martial Uncle?”

“Put away your swords.”

“But that bastard—”

“Are you planning to defy this old man’s command?”

At his icy voice, the middle-aged swordsman bit his lip and lowered his sword.

As the weapons that had brightly illuminated the inside of the teahouse disappeared, nothing remained to block my way.

“Thank you. They were a little hard on the eyes.”

*Scrape. Thump.*

I passed through the rigidly frozen people and dropped into the seat beside Ju Hwaran. Seeing how pale she was, I gave her a slight smile.

“Long time no—well, not really. It’s been two days. How have you been?”

“Young Hero Jin…”

“You don’t have to answer. I was only saying it as a courtesy. To be honest, Young Lady Ju, judging by your expression, you don’t look like someone who’s been doing well.”

“That’s not it. How did you even—?”

“I happened to be passing by and stopped in by chance. Young Hero Cheong here insisted that he absolutely had to have a cup of tea. Of course, that was also a coincidence.”

Unlike Baek Museong, Gung Gibang, and Hyuk Mujin, Cheongpung—whose twelve internal organs were apparently all livers—sat down beside me without hesitation and pouted.

“Benefactor, when are the candied sweets coming out?”

“Wait just a little longer. I’ll build you a whole mountain.”

“Wow! A mountain of sweets!”

Cheongpung looked ecstatic, as though he had discovered a mountain of candied sweets right in front of him.

Ju Hwaran, on the other hand, looked as if a mountain had collapsed.

Of course, most of the reason was probably Hwangbo Eom sitting across from her.

After looking back and forth between Cheongpung and me with an odd gaze, he suddenly spoke.

“You have a big liver. To the point of recklessness.”

“It used to be small. But after going through one thing and another, it suddenly grew a lot.”

“One thing and another, is that it? I suppose going through the Shaolin Bloodshed would do that.”

“……!”

“Why are you so surprised?”

Hwangbo Eom curled his lips into a smile and continued.

“I have heard all about the rumor that the Fire King took a Hidden Dragon under his wing. I also heard that you left the Murim Alliance seven days and nights ago.”

What a slippery old man.

He had known from the start.

Unlike Ju Hwaran, who had merely guessed our identities two days ago, he already knew everything.

*How?*

This operation had been carried out quickly and in secret, yet he knew everything as if he could see the palm of his hand.

*Did the Zhongnan Sect Leader, who should still be staying at the Murim Alliance, send a messenger pigeon?*

*Then could he also know about Old Master’s condition…?*

Just as I was wondering that, Hwangbo Eom’s gaze briefly passed over the pack frame I had entrusted to Baek Museong before sitting down.

Then he casually tossed out a single remark.

“I didn’t expect the Fire King’s heir to be dressed as a leather merchant like this.”

Was he pretending not to know, or did he truly not know?

There was no way to read his thoughts from his expression alone.

Jeok Cheongang was currently in a state resembling suspended animation. His heartbeat, breathing, and everything else had slowed to an extreme degree, making it extraordinarily difficult to sense his presence.

It was similar to the Turtle Breath Technique Cheongpung had mentioned before.

*And with all those layers of leather piled over him, even a Supreme Peak master would have trouble noticing him.*

There was a reason we had covered him with so many hides beyond maintaining his body temperature.

We had done it to hide his appearance, as well as his sounds and presence, so that no one would discover Jeok Cheongang’s existence.

“……”

“Is something wrong?”

“Nothing. But my throat is parched.”

I hurriedly redirected Hwangbo Eom’s attention. Without saying anything else, he picked up the tea service and held out a cup to me.

“Take it.”

“Then I won’t refuse.”

*Pour.*

Hwangbo Eom was no pushover.

I could feel the profound internal energy carried by the tea, and inwardly clicked my tongue.

*So this is Zhongnan’s greatest master.*

The tea fell in a slow, graceful arc. Yet the force carried within it was heavy and powerful enough to shatter a boulder.

*Still, it’s not as much as Old Master’s.*

Jeok Cheongang had a mischievous personality and had played all sorts of tricks on me before. What Hwangbo Eom was doing now was no different.

I had broken more than one or two cups this way.

Besides, Jeok Cheongang was the foremost among the Ten Kings, an absolute master who was sometimes even compared to the Three Saints.

*This much is nothing.*

When I did not even blink, Hwangbo Eom’s eyebrows twitched. At the same time, the internal energy carried by the tea grew stronger and stronger.

“Great Hero Hwangbo.”

“Hm?”

“The tea’s about to overflow.”

“……”

“You can stop pouring now.”

As I said, the cup was already full. I lifted the flawless cup, without even a hairline crack in it, and emptied it in one gulp.

“Ahh. That was good.”

“You seem to like tea.”

“Not really. Anyway, this time I’ll pour you a cup.”

When I reached out, the tea service containing the pot flew smoothly into my hand.

It was the technique martial artists called Seizing an Object Through Empty Space.

I possessed nearly two jiazi’s worth of internal energy and insight that had reached the brink of the Peak realm. I did not use the technique often because it consumed so much internal energy, but I could perform it whenever I wished.

*I have to put on at least this much of a show.*

Old Master had once said something in passing.

*“There are idiots everywhere in the Murim. You have to show those bastards something flashy before they’ll listen. Look at this old man. All I did was beat the Demonic Cult bastards because they pissed me off, and they still call me a king.”*

King Cheongang indeed. He had overturned the Murim by racking up a thousand kills single-handedly.

*Seizing an Object Through Empty Space isn’t quite on that level, but it’s still an impressive technique.*

As expected, the people watching opened their eyes wide.

“He used Seizing an Object Through Empty Space that easily…”

“Good heavens.”

Few people could use Seizing an Object Through Empty Space as casually as I did. Especially among people my age.

But I did not stop there. I drew up my internal energy.

I circulated the Fire Gate Divine Technique to seven-tenths, and Extreme Yang energy seeped into both my hands.

*Fwoosh!*

Heat burst forth, and the tea inside the tea service began to boil violently. I calmly filled Hwangbo Eom’s cup and spoke.

“The tea had gone a little cold. Since you’re going to drink it anyway, wouldn’t it be better warm? The weather has been cold lately, and older people need to be more careful.”

“……!”

Hwangbo Eom’s face hardened.

Heating tea with internal energy was not particularly difficult for him, either. He possessed a technique called Samadhi True Fire.

However, the Fire Gate Divine Technique was known as the greatest divine technique in the world when it came to handling Scorching Yang Qi.

No matter how powerful a Supreme Peak master Hwangbo Eom was, he could not match the Fire Gate Divine Technique.

And… No. It was too soon to jump to that conclusion.

I cut off the thought that was about to continue and offered him the cup.

“Please drink.”

“Ahem.”

“Here comes the tea! Chug, chug, chug-chug!”

“……I shall drink it properly.”

“Look at my internal organs! I’ve suffered internal injuries!”

“……”

Hwangbo Eom shot me a glare, then emptied the cup.

When he set it down, his gaze had changed considerably from the way he had looked at me when he first treated me as a mere youngster.

“Your martial arts are quite something.”

I waved a hand with a smile.

“Oh, no. Not at all.”

“Do you intend to deceive this old man’s eyes?”

“No. I meant that my martial arts aren’t merely ‘quite something.’ They’re at a very impressive level.”

“Your arrogance is excessive—”

“Oh, and for the record, my Master told me that. The Fire King, Jeok Cheongang. You know him, right?”

Now I was the only one smiling.

There was not a trace of amusement left on Hwangbo Eom’s face.

After remaining silent for a moment, he suddenly spoke.

“What are you plotting?”

“Pardon?”

“Your insolence reaches the heavens. I have heard enough of your nonsense about this being a coincidence. Tell me the truth.”

“You’re refreshingly direct. In that case, sure.”

I continued with a faint smile.

“I just happened to be passing by and came to see what kind of dirty trick the Zhongnan Sect was trying to pull.”

At those words, the eyes of Hwangbo Eom, the Taeeul Merciless Sword, turned cold.
## Chapter artifact 321

# Chapter 321

“What… did you just say?”

Hwangbo Eom’s voice was so strained it seemed ready to snap at any moment.

The snow-white beard that made him look like an immortal had puffed up, and the pair of eyes staring at me had turned cold and rigid.

I answered with a gentle smile.

“Didn’t I just tell you? I came to see what kind of dirty trick you were pulling. By. Chance.”

At that moment, blue sparks flew from Hwangbo Eom’s eyes.

“Gaaah!”

With his roar, an immense wave of qi burst outward from Hwangbo Eom.

The momentum released by a Supreme Peak master made the table—or rather, the ground itself—begin to rock like a ship caught in a storm.

Rumble-rumble-rumble!

The inside of the pavilion turned into complete chaos amid the violent vibrations. Dozens of tea utensils shattered with a cacophony of noise, and tea splashed in every direction.

With a shriek, the proprietor, who had been nervously watching the situation from the corner, collapsed onto the floor.

I instantly raised my sleeve to block the tea splashing toward Ju Hwaran, then clicked my tongue.

“Someone your age shouldn’t cause a scene in someone else’s shop. Not with other people around, either.”

“How dare you…”

The aura radiating from Hwangbo Eom grew even stronger.

It was the aura of none other than The First Sword of Zhongnan. Even the swordsmen of the Taeeul Sword Unit surrounding him like guards flinched as if they had been burned and stumbled backward, while the people from the Yongbong Escort Bureau, including Ju Hwaran, went pale.

“Hngh!”

“Gasp!”

No matter how talented a young prodigy was, the difference in level between them and Hwangbo Eom was like the difference between heaven and earth.

Baek Museong, known as a pillar of Huashan, and Gung Gibang, the Successor Beggar of the Beggars’ Sect, which commanded a hundred thousand beggars, were no different from Ju Hwaran.

Even counting everyone present, only about three people still looked unaffected.

One of them was, of course, me.

“Benefactor, when are the candied sweets coming out?”

Of the other two, one was Cheongpung, who was searching only for candied sweets, to hell with the Taeeul Merciless Sword and everything else.

And the last was…

“Hmm.”

Song Ilseom, the escort with the fierce eyes.

He let out a quiet groan beneath Hwangbo Eom’s aura. When our eyes met, he frowned and turned away.

*I don’t like you either, asshole.*

From the first time I had seen him until now, Song Ilseom had radiated a suspicious stench in more ways than one.

It would not take long to find out whether that impression of mine was mistaken or based on fact.

“Maybe we should have opened a window. The air feels a little stuffy.”

I spoke calmly and raised my internal energy. The hundred years of internal energy coiled within my dantian spread out between the tables like an invisible curtain.

Only then did Ju Hwaran escape the pressure and exhale the breath she had been holding.

“Young Lady Ju, are you all right?”

“Yes, yes.”

Still gasping for breath, Ju Hwaran gripped my sleeve tightly.

“Thank you, Young Hero Jin. But this is…”

“Enough.”

Her voice was cut off by a single word from Hwangbo Eom.

He had transformed from an immortal into a demon before I even realized it, and now he was glaring at me with killing intent.

“The arrogance of a young punk reaches the heavens.”

“I’m pretty good at piercing things. I use a spear.”

“Do you even know what you’re doing right now?”

“Of course.”

I leaned lazily against the hard back of my chair and continued.

“I’m rescuing innocent people who fell into a trap someone dug for them. Of course, I just happened to be passing by.”

“A trap. That someone must be referring to our sect.”

“Well, think of it however you like.”

The fury in Hwangbo Eom’s eyes subsided. What soon appeared at the corners of his mouth was unmistakably a sneer.

“You seem not to understand that every word carries responsibility.”

“Judging by the fact that I came here, I seem to understand that pretty well myself.”

“Boy, you have insulted the Great Zhongnan Sect with baseless nonsense you cannot prove. Do you wish to make an enemy of us?”

“It’s funny to hear orthodox Murim companions talk about friend and foe. Are you perhaps from an unorthodox faction?”

“You insolent whelp!”

“I already heard about the circumstances between the Yongbong Escort Bureau and your sect. That’s why I came here.”

As I spoke, I picked up the snow ginseng rolling across the tabletop.

The thing in my hand was certainly an excellent elixir. Yet the name displayed through Item Appraisal had not changed.

*Hundred-Year-Old Snow Ginseng.*

I already knew that the item Zhongnan Sect had commissioned the Yongbong Escort Bureau to transport was Thousand-Year Snow Ginseng.

It was a peerless elixir said to grant a full jiazi of internal energy instantly upon consumption.

It was such a rare treasure that Murim practitioners would risk their lives to obtain it. They said its value was whatever price someone was willing to name.

*According to the information Gung Gibang had gathered, the Yongbong Escort Bureau had staked its survival on this escort mission.*

Unless Ju Hwaran was a complete fool, she would never have tossed such an important cargo into a cart and left it unattended.

So where had the Thousand-Year Snow Ginseng gone, and why was there Hundred-Year-Old Snow Ginseng here instead—an elixir of a much lower grade?

*It was obvious.*

It could only mean that either the Zhongnan Sect or Hwangbo Eom personally had meddled with it.

On top of that, the Zhongnan Sect had been deeply involved in the Yongbong Escort Bureau’s decline for the past two years.

The Xi’an branch of the Beggars’ Sect, whose information network was said to rival the Lower District Sect’s for the best in the world, had already pieced together most of the circumstances.

*This was meant to be the final blow.*

The Thousand-Year Snow Ginseng was the last strike meant to bring down the Yongbong Escort Bureau, which had been backed into a corner.

They had thrown out a delicious bait that could not be ignored, then dug an inescapable trap beneath it. The result was unfolding right before my eyes.

But…

“After living in this world for a while, I realized that’s how things tend to go. Even when it looks like everything is over, something unexpected suddenly pops out and throws the whole thing into disarray.”

Hwangbo Eom looked at me as if I were ridiculous.

“A brat who still reeks of milk is wagging his tongue. Just because a country bumpkin from Shanxi became the Fire King’s Disciple, do you think no one is above you now?”

“I’m still young, so you don’t have to worry about me. You should be worrying about your old eyes, Great Hero Hwangbo.”

“How should I tear apart that crooked mouth of yours?”

“I don’t know whether my mouth is crooked, but I do know Zhongnan’s special talent. You can’t say a word when you’re standing before someone strong. Was it a year ago? Your Senior Brother gave me an advance lesson.”

I still remembered it clearly. The sight of the Roaring Fury Swordsman pressuring the Jin Family of Taiyuan while invoking the name of the Zhongnan Sect.

Even the way he had been driven out after failing to get a single proper word out when the Fire King, Jeok Cheongang, appeared.

I pressed my lips together and looked at Hyuk Sopyung, who was sitting beside Hwangbo Eom, before continuing.

“And yesterday, I had a review session, too.”

Hwangbo Eom was a perceptive old man.

Once he realized what had happened, he clicked his tongue and muttered.

“…There are worms crawling all over our sect.”

“Still, aren’t harmful pests better than poisonous insects? From my point of view, getting drunk and causing a scene is much more exemplary than ruining a perfectly good escort bureau.”

“A poisonous insect, you say? To this old man? Hah. Hahaha!”

Contrary to my expectations, I could no longer sense even the slightest disturbance from Hwangbo Eom.

He was already looking down on everyone, myself included. He resembled a hawk high in the sky that had finished preparing to swoop down and snatch its prey.

“Boy, do you know what it means to make an enemy of the Great Zhongnan Sect—and of this old man?”

His wrinkled hand pressed down on the table. The spilled tea slowly rose, transformed into the shape of an arrow, and aimed directly between my brows.

“If this old man so much as wishes it, today will be the day of your funeral.”

*That’s what you think.*

I opened my mouth.

“Well, from both my perspective and yours, that doesn’t seem like a particularly good choice for either of us.”

“That is why you are still alive. This old man will personally punish you for what happened today later. If you do not wish to die a dog’s death, withdraw. This is an affair between our sect and the Yongbong Escort Bureau.”

Just as I was about to answer, a hand tugged at my sleeve.

At the same time, a trembling woman’s voice, carried on internal energy, pierced my ears.

*—Young Hero Jin…*

The clear eyes that had sparkled without a single flaw two days ago now swirled with conflicting emotions.

Fear and anger at the current situation. Relief and worry at my appearance.

I could tell exactly what she was thinking and what she wanted to say.

*—I’m grateful that you’re thinking of us, but he’s right. This is an affair between the Yongbong Escort Bureau and the Zhongnan Sect. If you get involved any further, you’ll put yourself in danger as well.*

Looking into Ju Hwaran’s eyes suddenly brought back a memory from a year ago.

The day the Roaring Fury Swordsman had mentioned sealing the gates of the Jin Family of Taiyuan for an absurd reason. What would have happened if Jeok Cheongang had not appeared?

*Orthodox faction? What a load of bullshit.*

What the powerful considered righteous was different from what the weak considered righteous.

I would not say that everyone in orthodox Murim was evil. But neither would I say that everyone was good.

There were surely people with evil hearts even in Shaolin Temple, and I believed that there were good people even in the Demonic Cult, the lair of fiends and monsters.

Orthodox, unorthodox, demonic. Good and evil coexisted in all of them.

*It isn’t a problem with the sect. It’s a problem with the individual.*

In the end, what mattered was the person. And the old man my gaze had landed on was one of the biggest assholes under heaven.

I took a deep breath, then spoke to Ju Hwaran. This time, I used my actual voice rather than Sound Transmission.

“Young Lady Ju.”

“Y-Young Hero Jin?”

“You’re right. This is an affair between the Zhongnan Sect and the Yongbong Escort Bureau. If I stick my nose into it, all I’ll get is a loss. No matter how powerful the Jin Family of Taiyuan is, we’re still nowhere near enough to stand before the name of the Zhongnan Sect.”

Ju Hwaran’s eyelids trembled and lowered in surprise.

I could feel the deep resignation coming from her.

But I was not finished.

“Actually, I kept thinking about it on the way here. Wondering whether this was really right, whether I should just pretend I didn’t know anything and pass by.”

“Young Hero Jin. You can stop. Please, stop.”

“No.”

I shook my head and continued.

“At first, I thought I kept thinking about your face and that was the only reason. But…”

I turned my gaze and saw Hwangbo Eom smiling as though he found this entertaining.

The Zhongnan Sect was one of the Nine Sects and One Gang, and Hwangbo Eom was its elder and most powerful martial artist.

His martial arts were higher and his personality more meticulous, but Hwangbo Eom was still the same kind of person as the Roaring Fury Swordsman.

I looked straight at another Roaring Fury Swordsman and parted my lips.

“It felt like fucking bullshit.”

“……!”

“……!”

Even without seeing it, I could feel the energy in the room stirring.

I continued with a sigh.

“Upright. That’s why you’re called the orthodox faction. But this isn’t orthodox, is it? If you’re going to act like this, you should use the *jeong* from Choco Pie instead, for fuck’s sake. Why use the *jeong* that means ‘upright’?”[^1]

I had never once thought of myself as a good person in all my life.

I became a Hunter for money, and in the Murim, I had even considered abandoning someone in order to survive.

I was dark gray. Nothing more and nothing less.

But now, a thought suddenly occurred to me.

“I guess I was pretty white after all. Why else would I go this far?”

“You insolent little—!”

“Great Hero Hwangbo.”

I smiled at Hwangbo Eom as he tried to roar at me.

“I said this earlier, didn’t I? Even when everything looks finished, something unexpected can suddenly pop out and throw it all into disarray.”

I slowly reached out and tapped the air.

No one else could see it, but I could. Hwangbo Eom’s dominoes were collapsing one after another.

“I’m not even your grandson, Great Hero Hwangbo. So why would I spend this long talking to an eighty-year-old grandfather?”

For an instant, Hwangbo Eom wore a dumbfounded expression. Then his face twisted violently.

He had realized it, too—the presences of several people rapidly approaching the pavilion.

“You bastard. What the hell are you planning?”

“You’re the one who pulled a trick. I…”

I turned my head and finished.

“I made a plan.”

That was the moment the pavilion’s doors opened and about a dozen people came streaming inside.

First came five beggars carrying a mountain of bamboo slips in their arms. They were the Xi’an Branch Leader of the Beggars’ Sect and his subordinates.

And the woman standing at the head of the group on the other side was someone I knew well.

“Congratulations on your promotion. It’s been a while.”

“Oh, our Young Master. A congratulatory greeting after a whole year? How prompt of you.”

Wolhwa, the Branch Leader of the Lower District Sect’s Shaanxi branch, gave her pretty eyebrow a playful arch.

[^1]: This is a pun on *jeong*, the Korean word associated with affection in Choco Pie’s famous slogan, contrasted with the *jeong* in “orthodox,” which means upright or righteous.
## Chapter artifact 322

# Chapter 322

Wolhwa seemed even more beautiful than she had been a year ago.

A dazzling outfit and an alluring smile. She approached me gracefully, like a peacock, and placed a hand on my shoulder.

“Our Young Master Jin. You’ve gotten even more dashing since I last saw you.”

*At least this part of her hadn’t changed.*

I let out a quiet laugh and pushed her hand away.

“You haven’t changed a bit.”

“I’m hurt. After a whole year, is that all you have to say?”

“Hmm. I suppose you’ve gotten a little prettier, too.”

“It feels like I had to fish for that compliment myself, but… fine. This is enough to pass. Coming all the way here after dropping everything I was doing was worth it.”

As Wolhwa gave me one of her characteristic eye-smiles, a young beggar in shabby clothes approached from beside her with a displeased expression.

Three knots were tied together at his waist, symbolizing his position within the Beggars’ Sect.

In other words, he was a three-knot disciple of the Beggars’ Sect.

“I’m the Black Beggar, head of the Beggars’ Sect’s Xi’an branch.”

“Yes, I’m from the Jin Family of Taiyuan—”

“I already know. You’re as handsome as I’d heard. With a face like that, you could easily earn dozens of silver nyang a day if you went begging. Have you ever considered joining the Beggars’ Sect?”

“…”

“Well, forget it if you’re not interested. In any case, it seems someone who should be here is missing.”

Huff, huff.

Heukgeol Beggar looked around, blowing hard through his nose, until he found his target and shouted.

“Gung Gibang! You son of a bitch!”

*When did that bastard get over there?*

Gung Gibang was crouched beneath a table some distance away. He gave us an awkward smile.

“Oh, look. My twenty-year buddy Big Nose is here. What brings you here?”

“I told you not to call me Big Nose! And what brings me here? You miserable bastard! I warned you over and over to make sure this didn’t happen, but you went and did it anyway…!”

Heukgeol Beggar furiously shook the wooden slip in his hand.

Beneath the message telling him to gather the necessary information and come to Tengwang Pavilion, eight yellow hairs had been attached. They had apparently been plucked from a stray dog wandering the neighborhood.

Anyone else would have wondered what the hairs were supposed to mean, but according to Gung Gibang, they were the mark of an eight-knot disciple of the Beggars’ Sect.

In other words, the mark of the Successor Beggar.

“Ahem. I told you, I couldn’t help it.”

“Damn it. If the Law Beggar comes looking for you over this, remember that it’s all your fault.”

“Now, now. You have a lot to say for a mere three-knot disciple. You should be attending to the Successor Beggar instead.”

“You’re no Successor Beggar. You’re a successor mutt.”

Despite the words, Heukgeol Beggar reached out and pulled a chair away so that Gung Gibang could climb out more easily.

Judging from their conversation, the two seemed to have been close friends since they were young beggars.

*That makes things even better. This should go smoothly.*

For someone else, however, it would be very bad news.

I turned my head, and Hwangbo Eom’s twisted face entered my view. The corners of my mouth rose of their own accord.

“If this is your first time meeting, you should at least exchange greetings. Both of them are major figures in Shaanxi Province.”

The Zhongnan Sect could not compare to Huashan, but its position in Shaanxi Province was by no means insignificant.

There was no way Hwangbo Eom did not know the branch leaders of the Beggars’ Sect and the Lower District Sect. I had only added that last part to sour his mood.

“You…”

As I had expected, Hwangbo Eom already knew who they were. He bit his lip. His fingers twitched, and he looked desperate to draw the sword propped beside the table and swing it at someone.

*Go ahead. Draw it.*

But Hwangbo Eom was not nearly as easy to provoke as the Roaring Fury Swordsman.

The eyes of the sly old man slowly turned cold.

“What the hell are you doing?”

The answer came from behind me.

“Indeed. I’m looking forward to whatever our Young Master Jin gets up to next, so my heart is already pounding.”

Hwangbo Eom raised his eyes sharply toward Wolhwa, who had spoken without warning.

“This is not a matter for the Lower District Sect. I do not know why you came here, but… it would be best for you to withdraw at this point.”

“Great Hero Hwangbo, I’m sorry, but I don’t think I can do that.”

Wolhwa continued with a radiant smile.

“I’ve already accepted a commission. Of course, the client is the Young Master Jin standing here. Isn’t that right?”

“Oh, absolutely. Did you receive the silver nyang retainer I sent through the attendant?”

“Of course I did. But one silver nyang is terribly stingy. I’ll make you pay me plenty later, so be prepared.”

I had no idea how much she intended to fleece me for, but that was a problem for later.

Hwangbo Eom silently glared at Wolhwa and me as we chatted amiably. His next target was Heukgeol Beggar.

“And what does the Beggars’ Sect intend to do?”

“Great Hero Hwangbo, this is quite a situation.”

Heukgeol Beggar scratched his lice-ridden head and bowed deeply.

“I’m sorry, but it’s not a matter I can do anything about.”

“Is that the will of the Beggars’ Sect?”

Heukgeol Beggar bent at the waist in alarm.

“What? Oh, heavens, no. How could a mere three-knot disciple like me presume to speak for the Beggars’ Sect?”

“Then withdraw. Unless you wish to make an enemy of our sect.”

“Well, the thing is, we have something called sect rules on our side, too. That might be difficult.”

“You call that an excuse?”

“It isn’t an excuse. It’s the truth. Isn’t that right? No, wouldn’t you say so, Successor Beggar?”

Gung Gibang avoided Hwangbo Eom’s gaze and nodded.

“Well, yeah.”

“This old man went easy on you because you were a young prodigy of the Beggars’ Sect, but you’ve gone too far…”

Hwangbo Eom looked back and forth between the two of them, then shouted like a thunderclap.

“Enough excuses! Beggars’ Sect, will you get the hell out of here already?”

Boom!

With a furious roar, Hwangbo Eom slammed his palm into the center of the table.

A low rumble rolled through the room. The table could not withstand his profound internal energy and burst open, leaving a hole shaped like his palm.

And then…

“Good heavens.”

“Well, this is something.”

At that moment, the atmosphere around the bowing Gung Gibang and Heukgeol Beggar changed.

The two men looked at each other’s grime-covered faces and let out quiet laughs.

“Hey, Gibang. I guess we really are beggars. Even here, people treat us like beggars.”

“Tell me about it. I’m in a lousy mood today, too. Should we just call every beggar in Shaanxi Province?”

“As the branch leader, that’s my job. If we gather only the people in Xi’an, we should have about a thousand.”

“That’s not your call, three-knot. I’m an eight-knot—the one and only eight-knot disciple in the Beggars’ Sect! If the Successor Beggar calls, they’ll come running even from the neighboring province.”

“Shaanxi will become a den of beggars. At that point, wouldn’t it be looting rather than begging?”

“Now, now, what do you mean, looting? I hear there’s a great deal of food on Mount Zhongnan… Let’s wipe out every edible thing while we’re at it.”

It wasn’t Alibaba and the Forty Thieves.

It was Gung Gibang and ten thousand beggars.

I already knew that the Beggars’ Sect was a great sect with a hundred thousand disciples, but hearing them talk about it made me want to piss myself.

*At minimum, it would be a swarm of locusts.*

If ten thousand beggars swept over Mount Zhongnan, it would become a desert within a month. The complete annihilation of the mountain wildlife would be a given, and they would strip away every edible blade of grass and shred of bark.

“Y-you bastards, what kind of nonsense are you spouting…?”

Hwangbo Eom’s wrinkled hand trembled.

“Do you think this old man would stand by and watch such a thing happen? I will personally demand that the Sect Leader punish both of you!”

“Do as you wish. My Master will beat me within an inch of my life, but surely he won’t kill his only Disciple. However…”

Gung Gibang was no longer the man who had been edging his feet backward, trying to escape the situation. His voice had settled low, deeper than a swamp.

“As the Successor Beggar of the Beggars’ Sect, I have issued an order to the Xi’an branch. And there are only two people under heaven who can rescind an order from the Successor Beggar: the Dragon-Head Gang Leader, who leads the hundred thousand disciples, and the Law Beggar, who enforces the sect rules.”

“…”

“My Master, the Dragon-Head Gang Leader, has told me again and again: we may not have homes, but does that mean we have no pride? Great Hero Hwangbo, you have touched the pride of beggars.”

A veteran beggar, all right.

It wasn’t easy to look that cool and that pathetic at the same time, but he pulled it off effortlessly.

*Maybe he’s actually good at begging.*

With a voice brimming with tragic grandeur and words that made him sound utterly pitiable, Gung Gibang dominated the room before turning to Heukgeol Beggar.

“You brought everything I listed in the letter, right?”

“How could I fail to, when it was the Successor Beggar’s order?”

At Heukgeol Beggar’s gesture, the Beggars’ Sect disciples from the Xi’an branch, who had been waiting behind him, began stacking the bamboo slips they had brought.

There were a full one hundred of them.

But that was not all.

“What are you all waiting for? It’s time to get to work.”

When Wolhwa’s alluring voice rang out, the Lower District Sect members standing quietly nearby placed bundles of paper beside the bamboo slips.

Their number was roughly equal to that of the Beggars’ Sect’s documents.

The sight before him made Hwangbo Eom’s complexion turn rigid.

“What—what is all this?”

I gazed fondly at the bamboo slips and sheets of paper.

“Can’t you think of anything? For example… the Yongbong Escort Bureau’s unending run of bad luck over the past two years.”

“…”

“Let’s swim upstream like salmon and retrace the past. And while we’re at it, let’s find out how the Thousand-Year Snow Ginseng that was on its way here without a problem managed to disappear so completely.”

The energy of the two people thrashed with the vigor of salmon fighting upstream.

One was Hwangbo Eom, overwhelmed by confusion.

The other was Ju Hwaran.

Her luminous eyes, frozen cold without a trace of anger or excitement, turned toward Hwangbo Eom.

“So that’s what happened after all.”

“Did you know?”

“I couldn’t not know. I suspected it all along, but I had no choice but to let it happen.”

“Because we were up against one of the Nine Sects and One Gang.”

Her voice drifted away into the empty air.

For the past two years, the Zhongnan Sect had manipulated the Yongbong Escort Bureau’s failures from the shadows. Someone who did not know the circumstances might say that she had brought down the Escort Bureau in a mere two years, but that would be wrong.

The Yongbong Escort Bureau had already been a listing ship, and Ju Hwaran had become its captain at an age when she was not even twenty.

She was the reason the bureau had endured the threat of the enormous monster known as the Zhongnan Sect.

But now… everything would be different.

“You’ve been through a lot.”

At my brief words, Ju Hwaran bit her lips tightly.

And what she chose was not tears, but a smile.

“Thank you, Young Hero Jin. But I’ll hear that after this escort mission is over.”

She was right.

Just as Ju Hwaran had said, the Yongbong Escort Bureau’s escort mission was not over yet.

I gave Heukgeol Beggar and Wolhwa a small nod.

“Let’s begin.”

* * *

Hwangbo Eom suddenly wondered.

*What is happening?*

Everything had been proceeding smoothly. He had taken each step carefully over the past two years, and all that remained was to bring it to a close.

There had been a time when he thought so.

He really had.

“Last summer, the Yongbong Escort Bureau suffered a loss of one thousand silver nyang when its deal with the Geumo Merchant Guild fell through. A man named Hwang Cheolsim secretly intervened in the process. According to what our sect uncovered, he was a lay disciple of Zhongnan, and…”

The voices reaching Hwangbo Eom’s ears felt distant and unfamiliar.

Most of the information uncovered by the Lower District Sect and the Beggars’ Sect was true.

By cross-checking their findings, they had confirmed the facts more thoroughly and uncovered new incidents. The information continued to branch and spread like the stem of a plant.

*This is impossible.*

Hwangbo Eom stood frozen like a statue, repeating the same thought over and over.

Then one person entered his field of vision.

The corners of his mouth were raised. His clear eyes seemed capable of seeing straight through the human heart.

Jin Taekyung was laughing at him.

*It’s all that bastard’s fault. If only he hadn’t been there, if only…!*

People said that Taeeul Merciless Sword Hwangbo Eom was different from his two martial brothers.

But they were wrong.

At this very moment, Hwangbo Eom’s mind was being bleached white by rage.

The cold, poisonous heart that had occupied that space was gone. In its place was something even worse—a murderous intent that filled him to the brim.

“You bastard—!”

Shiiing!

Seizing an Object Through Empty Space.

The scabbard flew into Hwangbo Eom’s grasp, and a silver line burst from it.
## Chapter artifact 323

# Chapter 323

It all happened in an instant.

The qi permeating the air surged, and the sword propped against the table flew toward one man’s waiting hand.

And then…

Shuaaaak!

A dazzling streak of light filled my vision. The strike was impossibly fast and precise.

The blue qi crystallized around the blade and scattered a brilliant radiance. I already knew another name for that light.

*Sword Force.*

A power granted only to those who had stepped into the Supreme Peak realm. Stronger than anything else in the world, it was falling straight toward the crown of my head.

*At this rate, I’ll die. There’s no question about it.*

But…

*This much isn’t nearly enough.*

In a world slowed to a crawl, I moved—and the Sword Force split the air.

Shlick! Kraaash!

Everything was cleaved apart. The table, the chairs, even the floor of the tea house, which must have stood there for countless years.

The gale unleashed by the Sword Force swept through the surroundings. Screams and thunderous crashes swallowed the room whole. Beyond them, I saw the old man’s eyes stretched wide.

“H-how did you…”

I gently pushed Ju Hwaran, whom I had pulled into my arms, to the side and answered.

“How did I dodge? I saw it coming, so I dodged.”

“……”

“People say the Supreme Peak realm—and Sword Force—belong to the realm beyond humanity.”

Unconcealed shock spread across Hwangbo Eom’s wrinkled face.

“Th-then could it be that you…!”

“Who knows?”

I answered with a faint smile.

By now, thunder must have been booming inside Hwangbo Eom’s head.

Of course, I had not gained the enlightenment required to reach the Supreme Peak realm.

To be precise, it would be more accurate to say that my physical abilities themselves had reached a realm beyond humanity—not my martial arts.

*What should I even call this?*

A Supreme Peak master—physically?

There was no doubt that I was a new kind of Supreme Peak master, one without precedent in the history of the Murim.

I shrugged.

“It’s nothing special. I tried it, and it worked.”

Hwangbo Eom shouted, his eyes bloodshot.

“I refuse to believe this! How can a brat like you have reached such a realm?”

“I find it hard to believe, too. Who swings a sword in a place like this? Are you out of your mind?”

“That…”

Hwangbo Eom’s eyes stiffened as they swept across the room.

Fortunately, since his strike had been aimed precisely at me, no one else had been injured. Even so, shock and fury had appeared on everyone’s faces.

“You went on about the orthodox faction and the Great Zhongnan Sect, but the second you lost your temper, you became no better than a demonic fiend. Why not rename yourselves the Zhong-Bastard Sect while you’re at it?”

“You—!”

Hwangbo Eom’s hand trembled around the sword hilt. His eyes darted around in conflict before gradually turning cold.

“Disciples of the Zhongnan Sect, heed my command.”

“Y-yes, Martial Uncle!”

The thirty members of the Taeeul Sword Unit, who had frozen like statues at the sudden turn of events, jolted back to their senses.

They hurriedly cupped their hands, and Hwangbo Eom’s command fell over their heads.

“Seal the entrances immediately. No one is to leave this place.”

“S-Senior Martial Uncle!”

“B-but…”

“What are you waiting for? Do you intend to disobey this old man’s command?”

As Hwangbo Eom’s roar made the Taeeul Sword Unit hesitate, a quiet voice pierced everyone’s ears.

“Yes. I do.”

Hwangbo Eom’s face filled with fury when he recognized the speaker.

“Hyuk Sopyung. How dare you…”

The boy was familiar to me. Hyuk Sopyung, the Zhongnan One Dragon.

He stared at Hwangbo Eom with an indescribably complicated gaze.

“Please stop. This is the first and last time I will beg you.”

“What did you say?”

“The way you’re acting right now, Senior Martial Uncle… Isn’t this beneath a disciple of the Great Zhongnan Sect?”

“Shut your mouth!”

Kraaash!

Another gale swept through the room, and Hyuk Sopyung’s body slid backward.

But his eyes did not waver.

Hwangbo Eom looked back and forth between Hyuk Sopyung and the thirty hesitant members of the Taeeul Sword Unit before biting down hard on his lip.

“You little…”

The next moment, he pulled a small copper tablet from inside his robes and threw it at Hyuk Sopyung’s feet.

“This is our sect’s Sect Leader’s Command Token, entrusted to this old man by your Master. Do you still intend to refuse?”

“……!”

The Sect Leader’s Command Token was a powerful symbol of authority, belonging to the very peak of a sect.

Hyuk Sopyung’s eyelids trembled when he recognized his Master’s copper tablet.

“Senior Martial Uncle, you truly haven’t changed.”

“Choose. Expulsion—or obedience.”

“Expulsion…”

Hyuk Sopyung’s regretful gaze touched me and Ju Hwaran.

Then he gave a bitter smile, bowed deeply toward the copper tablet, and slammed his forehead against the floor.

Thud! Thud! Thud!

“Disciple Hyuk Sopyung obeys the command of the Sect Leader’s token!”

His cry sounded as if he were vomiting blood. Blood streamed down his split forehead.

Hyuk Sopyung rose with an expressionless face, as if he felt no pain at all, and blocked the entrance to the tea house. The thirty members of the Taeeul Sword Unit did the same.

I clicked my tongue as I watched the whole thing unfold.

“At this point, you haven’t just crossed the line—you erased it altogether. Are you sure you can deal with the consequences?”

The major figures of Huashan, the Beggars’ Sect, and the Lower District Sect were all gathered here. No matter how powerful the Zhongnan Sect was, the fallout from today would be fierce.

But Hwangbo Eom’s eyes, already clouded by rage, held nothing but fury.

“They will be safe. Except for you.”

“Ah. So you’ll deal with me first and clean up afterward?”

“Yes. At last, I can tear that mouth of yours apart.”

“Why are you so desperate to tear it apart, old man? The Jin Family of Taiyuan and the Fire Gate Clan aren’t exactly a pair of pushover nobodies.”

“The Fire Gate Clan?”

A sneer formed at the corner of Hwangbo Eom’s mouth.

And then, the next moment, a line of Sound Transmission pierced my ear.

*The young tiger is in danger, yet the great tiger shows no sign of waking.*

“……!”

*Did you think this old man wouldn’t know, you foolish child? I already knew the Fire King’s illness was serious.*

A secret known by only a handful of people had leaked out.

My face stiffened before I could stop it. Hwangbo Eom’s smile deepened when he saw my reaction.

*The Fire King Jeok Cheongang, and you. The two of you have been a damn nuisance. This might be a good opportunity to settle my bad blood with the Fire Gate Clan once and for all.*

Settle his bad blood?

Hwangbo Eom’s words left me momentarily dazed.

*Is what I’m thinking really true?*

My tangled thoughts were wiped clean in an instant. Only one thought remained.

“Sorry, but can I ask everyone for one favor?”

I could feel them, even without seeing them.

Baek Museong and Cheongpung. Gung Gibang and Heukgeol Beggar. Wolhwa and Hyuk Mujin. And finally, Ju Hwaran.

Everyone in the room was looking at me.

Then, a voice so dry that I could hardly believe it belonged to me slipped between my lips.

“Block the entrance. Don’t let anyone get out.”

Hwangbo Eom had been the one to block the entrance first.

But I would be the one to decide whether that door opened or closed.

“Taeeul Merciless Sword Hwangbo Eom.”

I let out a quiet sigh. Extreme Yang qi boiled up from my dantian and flowed out as white steam.

“You said something you never should have.”

He should never have brought up Jeok Cheongang over something as trivial as this.

He truly shouldn’t have.

The price for saying what I should not have said would be paid from this moment onward.

“Bring it, you old fuck.”

In time split into smaller and smaller instants, Hwangbo Eom and I rushed toward each other.

Kraaaaaash!

* * *

Heavenly River Thirty-Six Swords.

The net of Sword Energy covering the heavens and earth was dense and powerful.

The sword forms that came flying without pause were in a completely different league from the Roaring Fury Swordsman I had faced a year ago—or Hyuk Sopyung the day before.

Shishishishishik!

They were dazzlingly fast and destructive. Even a glancing blow would split flesh and bone and bring death.

*This can’t be dodged. It couldn’t be dodged.*

*At least, it would have been true if I were the me from a year ago.*

The saying *wipe your eyes and look again* came to mind.

It referred to an achievement so astonishing that one had to rub one’s eyes and take another look.

Even that saying fell short of describing me.

I had grown stronger through days of harsh, unceasing training.

No.

It would not be wrong to call it evolution.

*Heaven is truly heartless. How can someone like you even exist?*

Jeok Cheongang’s face, filled with helplessness, appeared over the net of Sword Energy.

I gave a quiet laugh and swept my spear, White Flame, upward.

Shraaaak!

The Extreme Yang qi clinging to White Flame’s spearhead tore through the net.

A fish might escape through the gap in a torn net, but I was not a fish.

I was a shark.

The fisherman who had cast the net had clearly overlooked that fact.

The old fisherman’s wrinkled face was filled with shock.

“You—!”

I did not answer.

I bent my knees and lowered my waist. The spear in my hand curved smoothly like a dragon’s tail.

*Fire Dragon’s Single Tail.*

Fwoooosh! Boom!

The blue-burning spear and sword collided.

A deafening crash rang out as immense waves of martial energy erupted.

Had Hwangbo Eom been trying to conserve his strength?

If so, he had made a terrible mistake. No matter how severe the drain on his internal energy, he should have used Sword Force.

“Hup!”

His eyes opened wide.

The old man staggered under my strength, which had entered the realm beyond humanity, and the innate ferocity of my martial art.

“Wh-what kind of martial art is this…?”

The founder of the Fire Gate Clan had been called the greatest martial artist under heaven in his era.

He created the Fire Gate Divine Technique and made it the foundation of the clan. The sixteen Sect Leaders who followed him had each become a different branch growing from that root.

The Fire Dragon Divine Spear was no different.

Created by the fifth Sect Leader, this spear art was extremely destructive and fierce.

It truly resembled the movements of a fire dragon.

And…

*This is only the beginning.*

Whoooosh!

I held nothing back.

I stabbed, slashed, swung, and struck all at once.

Whenever the blue flames ran wild, thunderous crashes that sounded like the sky was splitting apart shook the heavens and earth.

*After the tail come the claws.*

No one under heaven had ever seen a dragon fight.

But while learning the Fire Dragon Divine Spear, I had found myself wondering about it.

*If a fire dragon really swung its claws, wouldn’t it look exactly like this?*

Gooooong.

Extreme Yang qi coiled around the tip of my spear.

The tea that had spilled across the floor during Hwangbo Eom’s earlier rampage had long since evaporated. The jade-colored tea utensils had grown red-hot, just as they must have been when they were being fired in the kiln.

Sensing that something was wrong, Hwangbo Eom shouted like a thunderbolt.

“You bastard!”

He was already nearing eighty.

But for someone who had entered the Supreme Peak realm, age was nothing more than a number.

His formidable internal energy and the Zhongnan Sect’s ultimate techniques, which he had practiced for more than a jiazi, poured down like beams of light.

Swoooosh!

If the Heavenly River Thirty-Six Swords were a net, this was a harpoon meant to sever my breath.

As I watched his sword slash toward my chest at incredible speed, scattering dozens of afterimages, one martial art flashed through my mind.

*Taeeul Light-Dividing Sword.*

One of the Zhongnan Sect’s most celebrated ultimate techniques.

Jeok Cheongang had described the Taeeul Light-Dividing Sword as sword art of extreme speed.

Then he had added one more thing.

*Maybe this old man is senile. Why do I feel like you’ll be faster than the sword?*

If Jeok Cheongang woke up, I wanted to tell him that he had been right.

And that the Fire Gate Clan’s martial arts had broken through the Taeeul Light-Dividing Sword.

*Heavenly Strike.*

The fire dragon swung its claws.

The strike descending from the sky erased the afterimages created by the Taeeul Light-Dividing Sword and fell like a bolt of lightning.

Kraaaaaash!

A pillar of hellfire erupted.
## Chapter artifact 324

# Chapter 324

Kraaaaaash!

The hellfire that had burst forth spread outward, devouring the chill of early spring that had yet to fade.

It erased the wavering afterimages created by the Taeeul Light-Dividing Sword when it split into dozens, then reached the blade as it finally recombined into one.

The Sword Force, the one true essence and concentration of power, collided with the hellfire.

Gooooooong!

A deafening roar rang out as a massive wave of martial energy spiraled around the old man and the young man.

Blue flames coiled around the wind, tore through the tea house’s ceiling, and surged upward like a waterspout.

At the sight, the eyelids of the old man, Hwangbo Eom, trembled.

*The fire dragon…!*

He did not even notice that his once-proud white beard had been scorched black.

All he could feel was his breath catching and his chest tightening as he stared into the burning eyes of the young man glaring at him across their locked weapons.

*It’s hot.*

Hwangbo Eom possessed two jiazi of internal energy and had reached the Supreme Peak realm.

His body, tempered by formidable martial arts, had long since reached the state of being Unaffected by Cold and Heat.

But the young man’s gaze—and the aura radiating from him—was not the kind of thing that could be called mere heat.

Rage and fighting spirit.

And within them, the faintest trace of cold composure.

*How is this possible? Even the word “young” fails to describe him…*

“Cough.”

A dry cough escaped Hwangbo Eom, followed by a mouthful of blood. Then, with trembling eyes, he stared at the spear in the young man’s hand.

Blue-white flames coiled around the transparent silver spearhead.

It was not yet complete, but it was unmistakably Force.

*No. That’s not possible. He hasn’t crossed the wall yet. He’s still at the Peak realm. Then how could this old man…?*

Hwangbo Eom had crossed that wall ten years ago and entered the Supreme Peak realm.

Yet after all those distant years of gaining enlightenment through training and meditation, he was being pushed back by a young brat who had not even left the Peak realm behind.

“How?”

The young man’s answer to his question was short.

“Because I’m stronger.”

“……!”

With that quiet reply, the spearhead locked against Hwangbo Eom’s sword pressed down on him with tremendous force.

Kaga-ga-ga-gak!

“Hup!”

Two jiazi of internal energy poured into the Sword Force?

A martial art of the Supreme Peak realm?

All of it was useless. The strength transmitted through the spearhead was a divine strength no human being should have been able to wield. It brought to mind a myth he had heard as a child.

*Pangu.*

The primordial giant who had created the world by swinging a single ax.

The young man before him had confined the strength of a god within a human body.

And divine strength was not all he possessed.

Shlick!

The senses of a Supreme Peak master were far beyond those of an ordinary martial artist.

Yet even Hwangbo Eom could not evade the sudden silver line that slashed across the air.

Pain he had not felt in decades.

Then blood gushed from his shoulder, and his eyes flew wide.

*When did he…?*

He had not even seen the young man make his move.

Even the Taeeul Light-Dividing Sword, the Zhongnan Sect’s celebrated sword art of extreme speed, could not possibly be like this.

After eighty years of practicing the Zhongnan Sect’s martial arts, Hwangbo Eom shouted.

“This cannot be! How can this be?”

Kraaa-boom!

He summoned every last ounce of strength, and the Force gathered along his blade rose like a wildfire.

At last escaping the pressure, Hwangbo Eom pointed at the young man with trembling fingers.

“Who… Who in the world are you?”

“You know.”

The young man, Jin Taekyung, spat to the side like a common street thug before continuing.

“The Fire Gate Clan’s nineteenth successor.”

Fwoooosh!

The hellfire gathered around the transparent spearhead blazed fiercely.

* * *

Shweeeeeek! Boom!

The spearhead and the sword blade collided.

A series of moments so brief they could be called instants.

The hellfire and Sword Force erased everything in their path as they clashed and separated through dozens of exchanges.

Shishishishik! Bang!

I tilted my head a fraction.

A tremendous wave of martial energy burst from the tip of the sword that stabbed into empty air. A pillar three jang away split like tofu and came crashing down.

I shot myself forward, stepping on the wooden fragments raining from the ceiling.

Light yet heavy.

Soft yet rough.

It was like fire spreading.

*So this is the essence of the Flamefire Path.*

For an instant, a feeling of floating enveloped my entire body.

The world slowed down, and I alone seemed to be pulled forward. My body, light as air, shot ahead like a bullet.

Ding.

> **System**
>
> Enlightenment comes to you in many ways. Through ceaseless training and meditation, and through battles in which you stake your life.
>
> The **Flamefire Path** has risen to seven stars!
>
> You have gained a substantial amount of EXP!

Bang!

Air exploded beneath my toes.

At the same moment the System notification rang out, I found myself directly in front of Hwangbo Eom.

Perhaps because of the unexpected enlightenment and the increase in my speed, I had gotten too close to thrust with my spear.

Instead of retreating, I thrust out a palm strike.

Whoooosh!

My palm advanced, burning through the air.

Hwangbo Eom let out a thunderous roar and thrust out his own palm to meet it.

A dazzling blue light gathered over his wrinkled palm.

It was the Zhongnan Sect’s famed Blue Cloud Heavenly Force Palm.

But he had been given too little time to complete the Force in his palm.

No.

*I was simply faster.*

Whoooooosh! Boom!

The two palms met.

A thunderous crash rang out, followed by a strangled groan.

“Guh!”

Hwangbo Eom’s face had gone pale from his Internal Injury. Gritting his teeth, he raised his other hand and pointed it at me.

Papapap!

Five streams of finger qi cut uselessly through the empty air.

If I had not caught his wrist with the Fire Dragon Claw in that instant, I would have been bleeding.

*How dare you.*

Crack.

Using my thumb, index finger, and middle finger, I twisted the wrist I had seized.

A suppressed scream slipped through his split lips.

Taeeul Merciless Sword Hwangbo Eom.

How long had it been since he had experienced pain like this?

When the curtain falls on a stage, the actors leave.

The curtain had fallen on the war between the orthodox and unorthodox factions half a century ago, and the heroes had scattered in every direction.

The Hwangbo Eom I saw before me now was not a hero.

He was merely a petty old man.

*This is going to hurt.*

I released his limp wrist.

At the same time, I clenched the fingers that had been curled like a dragon’s claws.

Crack.

I had repeated the same stance countless times a day while wearing an iron ball weighing hundreds of geun.

My lower body had to be like roots, my waist like a pillar, and my fist had to be precise and unobstructed.

Not a single part of it deviated from Jeok Cheongang’s teachings.

*At first, I smashed rocks.*

I split waterfalls falling from hundreds of jang above.

*Then I brought down cliffs.*

Like the shell of a turtle, the skin across the back of my hand had burst and split countless times. Blue-white flames spread across it.

The time from taking up the stance to throwing the punch was less than an instant.

*Flame-Extinguishing Divine Fist.*

Gooooong.

The Extreme Yang energy evaporated every trace of moisture within several meters.

Hwangbo Eom’s lips, cracked like a drought-stricken rice paddy, parted.

“You can’t—!”

“I can.”

With that answer, I drove my fist forward.

The Body-Protecting Qi of a Supreme Peak master stood in my way, but only for a moment. The punch shattered the energy surrounding his entire body before slamming into his aged flesh and bones.

Kraaaack!

“Gaaaaaaaaah!”

Hwangbo Eom’s body was hurled backward amid a shriek that seemed to tear the air apart.

Three pillars and part of the wall collapsed, and the remaining ceiling came crashing down.

Just as I began to think of the word *finish*, I saw bloodshot eyes glaring at me through the cloud of dust.

“C-cough!”

“Just lie down. If you want to preserve what little life you have left.”

“You… How could you…”

Shock and confusion.

Rage and humiliation.

Countless emotions churned within Hwangbo Eom’s eyes.

And at last, they all converged into one.

*Hatred.*

His blood-soaked lips slowly opened.

Blood mixed with pieces of his organs poured down, but his eyes continued to burn fiercely.

They were the eyes of a man who had abandoned all thought of what would come afterward.

“This old man is… The First Sword of Zhongnan.”

At that moment, the hot wind swirling around us cooled.

Then a freezing wind began to blow.

It started from one man and rose from one sword.

I felt my overheated blood begin to cool and muttered,

“This is…”

“The Taeeul Formless Sword. Watch closely. This is the sword art that will take your life.”

Shing—

The sword moved, and the wind blew.

The sword was the wind, and the wind was the sword.

Invisible sword strikes were mixed into the wind.

It was the instant I thought I smelled a strong scent of blood.

Shlick!

I took half a step to the side.

That half-step saved my life.

I had no time even to feel the blood flowing from my neck. Every time Hwangbo Eom’s sword vibrated more than ten jang away, invisible sword strikes poured toward me like waves.

Shik, shlick!

My side stung.

The energy carried by the sword strike shook my insides.

Even as I staggered, I raised my arm. The attack that passed within a hair’s breadth of me split a roof beam like tofu.

*What is this?*

Shlick!

I had no time to question it.

This time, my chest was cut open in a long slash. A stream of blood sprayed out and soaked the floor.

*I can’t see it.*

It felt as if I had been swallowed by dense fog.

This was not a matter of strength or speed.

It was martial arts—a sword art of supreme mastery wielded by a martial artist who had attained greater enlightenment than I had and was forcing his internal energy into a rampage.

And yet…

*How have I managed to dodge it until now?*

One question suddenly took over my mind.

Dozens of sword strikes poured down on my rigid body.

I stared at the sight with a dazed expression.

Then I closed my eyes.

In the darkness that came with them, one man’s face appeared.

His sharp, ringing voice echoed faintly.

*In the Murim, live with your eyes wide open. Then you won’t get stabbed and die.*

*But what if I end up in a situation where I’m about to die anyway?*

*Then tear out those useless eyes and see with your heart.*

*My heart? Come on. How is that supposed to work?*

*Have you even tried?*

Yes, I had.

No.

I was trying now.

*So this was what you meant back then.*

A smile spread across my face before I realized it.

I could not see.

But I could feel it.

The sword strikes approaching through the darkness where I could not see even an inch ahead.

The final struggle of Taeeul Merciless Sword Hwangbo Eom.

*Thank you for the lesson, Old Master.*

I twisted my body with my eyes closed.

I finely tuned every limb and every tiny muscle, as precisely as the notes of a piano.

The sword strikes missed my flesh, tearing through my clothes and clawing at the ground.

Kraaa-boom!

Amid the thunderous crash, I slowly opened my eyes.

Hwangbo Eom’s face was filled with astonishment.

An emotion I had never seen before was reflected in his eyes.

*Fear.*

He knew it, too.

He knew the fear he was feeling.

The terror he sensed from me.

“D-don’t come any closer!”

Shweeeek!

I took one step forward and swung my spear.

The sword strike that had been cutting toward my neck collided with the spearhead and vanished.

Then I took another step.

Shishishishing!

I unfolded my spear as naturally as I breathed.

I knocked aside, blocked, and pierced the attacks as though I were dispatching a living enemy.

And all the while, I continued walking forward.

I was not in a hurry.

Hwangbo Eom was desperate.

Ignoring the body that had already reached its limit, he unleashed one final sword strike.

Kraaaaaash!

Sword Force carrying enough power to reduce the entire tea house to dust came rushing toward me.

I watched it approach until it was right in front of my face.

Then I swung my spear like a bolt of lightning.

*Heavenly Strike.*

The fire dragon’s claw seized the Sword Force.

And then—

Crack!

The shattered sword blade tumbled across the ground.

Hwangbo Eom stared blankly at the broken sword he had cherished before lifting his head.

“You… What in the world are you…”

“So why…”

I slowly continued speaking to the greatest martial artist of the Zhongnan Sect, Taeeul Merciless Sword Hwangbo Eom.

“Why the fuck are you insulting someone else’s master? You old bastard who ate your age through your asshole. You trying to get yourself killed? Fuck.”

# Checkpoint Review — 510–514

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

# Chapters 510–514

## Plot

Taekyung nearly exhausts his internal energy practicing **Rising on Duckweed, Crossing Water** behind the ship. When a shark approaches in the Yangtze, he uses the Water God Dragon’s sinew to control five sharks, catches up to the Yangtze River Channel League’s swift ships, and leaves one white sturgeon with a fisherman. A stranger then approaches by walking across the water.

Jeok Cheongang appears, gives Taekyung food, and makes him abandon the shark-assisted shortcut. Taekyung resolves to reach Henan through his own strength while Jeok travels ahead. Jeok explains that the Fire Gate Clan’s violent internal energy requires years of refinement, but Taekyung’s talent and his exceptional teachers give him unusual advantages.

The New Murim Alliance is publicly announced from Mount Song. Shaolin, Huashan, the Nine Sects and One Gang, and the Five Great Families begin moving to join it as Murim debates the threat from Dark Heaven, demonic and heterodox factions, and the Outer Lands.

In Xixia, Henan, the unnamed Young Sect Leader of the Black Dragon Demon Gate, Sama Pyo, acquires a famed sword and provokes Blood Cudgel Do Sangho. Sama Pyo’s enormous subordinate kills Do Sangho with a two-section staff. Twenty Shaolin monks led by Jung Ho arrive and confront Sama Pyo; after learning that Do Sangho had murdered five merchants, Sama Pyo agrees to explain the killing, apologize to bystanders, and pay compensation while assigning blame to his subordinate. A hoarse-voiced figure in a conical hat claims Sama Pyo’s sword belongs to someone else. The arrival of the Jin Family of Taiyuan is then announced.

## Continuity

- Taekyung has abandoned the shark shortcut and is refining his own ability to cross the Yangtze toward Henan.
- A stranger capable of walking across the water has approached Taekyung; the stranger’s identity and motives are unresolved.
- The New Murim Alliance has been publicly announced, with the major orthodox sects and families moving to join.
- Sama Pyo is the unnamed Young Sect Leader of the Black Dragon Demon Gate, an unorthodox faction from Gansu. He owns or claims ownership of the disputed Black Dragon Saber.
- Sama Pyo’s towering subordinate killed Blood Cudgel Do Sangho on the main road near Xixia. Shaolin’s Jung Ho is investigating, though Sama Pyo has agreed to account for the incident.
- The conical-hatted figure traveling with Shaolin has a hoarse voice and claims Sama Pyo’s sword belongs to another person.
- The Jin Family of Taiyuan has arrived or is approaching Xixia.
- The Yangtze River Channel League and Green Forest Alliance may become rear threats to the New Murim Alliance; the North Sea Ice Palace remains isolationist, while the Nanman Beast Palace may support orthodox Murim.
- Mungyeong remains secretly identifiable to Mu Song and five Water Dragon Stronghold subordinates only as an exceptionally powerful Supreme Peak master; his identity as the Slaughter Saint remains concealed.

## Translation Decisions

- Retain **New Murim Alliance**, **Outer Murim**, **Outer Lands**, **North Sea Ice Palace**, **Nanman Beast Palace**, **Small Thunderclap Temple**, **Mad Wind Society**, **Potala Palace**, **Five Poisons Sect**, **Poison Valley**, **Fire Gate Clan**, **Fire Gate Divine Technique**, and **Rising on Duckweed, Crossing Water**.
- Render **흑룡마문** as **Black Dragon Demon Gate**, **소문주** as **Young Sect Leader**, **혈곤** as **Blood Cudgel**, **도상호** as **Do Sangho**, **정호** as **Jung Ho**, **사마표** as **Sama Pyo**, **흑룡도** as **Black Dragon Saber**, and **대초자곤** as **two-section staff**.
- Retain **sa-eo** for 사어, **shark** for 상어, **white sturgeon** for 흰철갑상어, **Shark Water-Ski Team** for 수상스키단, and **swift ship** for 쾌조선.
- Use **Old Master** for 노야, **this old man/I** for 노부, and **Benefactor** for 시주 in direct address.
- Render **천축** as **India**, **갠지스강** as **Ganges River**, **파사국** as **Persia**, **회교도** as **Muslims**, **영웅건** as **hero headband**, **대막** as **great desert**, **귀염권** as **Ghost Flame Fist**, and **장성** as **Great Wall**.

## Durable state

{
  "active_continuity": [
    "Jeok Cheongang's Heart Demon and the dark memories binding him have been expelled; he has entered a new realm and achieved Returned to Youth.",
    "Mungyeong is the Slaughter Saint and former Divine Physician, a Returned to Youth Supreme Peak master and the greatest assassin in history; Mu Song and five Water Dragon Stronghold subordinates know he is exceptionally powerful but not that he is the Slaughter Saint.",
    "Mungyeong is training Taekyung to refine the stability and precision of the violent internal energy produced by the Fire Gate Divine Technique through Rising on Duckweed, Crossing Water.",
    "Zhuge Feng's Demon-Sealing Formation blocks all mana from the exposed Gate by drawing in natural qi, but whether it is permanent and repeatable remains unresolved.",
    "Jang Taebo is the Jin Family of Taiyuan's Master of Ironcraft Hall and is summoning renowned artisans to process the Water God Dragon's remains.",
    "The New Murim Alliance has been publicly announced from Mount Song; Shaolin, Huashan, the Nine Sects and One Gang, and the Five Great Families are moving to join it. Near Xixia, Shaolin has confronted Black Dragon Demon Gate Young Sect Leader Sama Pyo after his subordinate killed Blood Cudgel Do Sangho, and the Jin Family of Taiyuan has been announced nearby.",
    "Taekyung has abandoned the shark shortcut and intends to reach Henan by his own strength.",
    "The Southern Heaven Demon Empress is traveling toward Yunnan and expects to cause further deaths.",
    "Jin Mukyung remains secluded in the training hall after losing to Cheongpung, refusing to emerge until he achieves a great accomplishment.",
    "Mu Song wants to aid the Murim Alliance, but the Seafaring King alone decides the Yangtze River Channel League's major matters; the League and Green Forest Alliance may become rear threats.",
    "The North Sea Ice Palace remains isolationist, while Jeok Cheongang believes the Nanman Beast Palace will probably support orthodox Murim because of its historical goodwill toward the Fire Gate Clan.",
    "A stranger capable of walking across the Yangtze's surface has approached Taekyung."
  ],
  "continuity_sources": [
    514,
    513
  ],
  "open_questions": [
    "Will the Demon-Sealing Formation remain effective permanently, and can equivalent formations be installed repeatedly if more Gates appear?",
    "What is the Lord of Heaven's identity, and how is he connected to the dangerous force Taekyung associates with his original world?",
    "Where is the Southern Heaven Demon Empress ultimately headed, and what does she intend to do in Yunnan?",
    "Will the Nanman Beast Palace, North Sea Ice Palace, Yangtze River Channel League, and Green Forest Alliance support, ignore, or oppose the New Murim Alliance?",
    "Who is the stranger walking across the Yangtze, who is the conical-hatted figure traveling with Shaolin, and whose sword does Sama Pyo possess?"
  ],
  "safe_through": 514,
  "temporary_decisions": [
    "Render 새외무림 as Outer Murim, 새외 as Outer Lands, 북해빙궁 as North Sea Ice Palace, 야수묘왕 as Beast Miao King, and retain Nanman Beast Palace for 남만야수궁.",
    "Render 소뢰음사 as Small Thunderclap Temple, 광풍사 as Mad Wind Society, 포달랍궁 as Potala Palace, 오독문 as Five Poisons Sect, 독곡 as Poison Valley, 천축 as India, and 갠지스강 as Ganges River.",
    "Render 파사국 as Persia, 회교도 as Muslims, 영웅건 as hero headband, 대막 as great desert, 귀염권 as Ghost Flame Fist, and 장성 as Great Wall.",
    "Retain sa-eo for 사어, shark for 상어, Old Master for 노야, this old man/I for 노부, Shark Water-Ski Team for 수상스키단, and swift ship for 쾌조선.",
    "Render 정호 as Jung Ho, 사마표 as Sama Pyo, 흑룡도 as Black Dragon Saber, 대초자곤 as two-section staff, and 시주 as Benefactor in direct address."
  ],
  "version": 1
}

## Reading copies

## Chapter artifact 510

# Chapter 510

Ship-Fire Boy Mu Song had been a sailor from birth.

His parents, whose faces he could no longer remember, had been a famous pair of lovebird river bandits in the area. His maternal and paternal family lines were also full of river bandits and fishermen.

He came from a river-bandit family to the bone.

Maybe that was why Mu Song much preferred spending time aboard a boat to being on land.

Whenever he saw dense forests and open fields, his hands and feet tingled and his breath grew tight, as though he had swallowed deadly poison. But whenever he saw a wide-open river or sea, his vitality returned.

And that wasn’t all. While other stronghold lords who had made fortunes as river bandits bought impressive estates and indulged in wine, women, and gambling at pleasure houses, Mu Song decorated his boat, lay on a bed woven from nets, and watched the Yangtze.

Whenever he did, he always had the same thought.

*I wish the entire world were made of water. Then I could spend my whole life on a boat.*

But now, Mu Song was staring blankly at the Yangtze and muttering,

“Ah, fuck. This boat is fucking slow. I want to get off already…”

“……!”

“……!”

The atmosphere instantly turned icy.

The Water Dragon Stronghold river bandits nearby doubted their own ears.

After rolling their eyes around and exchanging glances, they soon reached a clear conclusion.

*We must have heard wrong!*

*That’s right. All our ears must have malfunctioned at once.*

*Our Stronghold Lord would never say something like that.*

Everyone in the Yangtze River Channel League knew what kind of person Mu Song was, from the most senior Water Dragon Stronghold river bandit to the newest recruit.

The very embodiment of a passionate sailor! A man who loved the Yangtze even more than his Master, the Seafaring King!

There was no way a man like that would curse the swift ship he treasured as much as his own life for being slow and say he wanted to go ashore—

“I should quit this whole damn business. It’s fucking miserable.”

“……!”

“……!”

An invisible shock swept across the deck.

The surroundings fell silent at Mu Song’s sudden declaration of his intention to retire and the threat of the Water Dragon Stronghold being disbanded.

The silence, which seemed as though it might last forever, was broken when a liquor barrel slipped from the shoulder of a dazed river bandit.

Boom! Crash!

The barrel had been filled with liquor, so it was quite heavy. The wooden cask shattered when it hit the deck, sending alcohol splashing in every direction.

Only then did Mu Song snap out of his thoughts and glare.

“What the hell are you doing?”

Mu Song already had a fearsome face. The river bandit who had dropped the barrel went pale and bowed deeply at the waist.

“I-I’m sorry!”

“You bastard. You don’t know the value of liquor? I ought to hang you upside down and… What was it? The Yangtze, the Yangtze… Right. I might just sentence you to the Yangtze’s dip-and-taste punishment.”

“I’ve committed a crime worthy of death. Please, anything but that…”

“Be careful. I’m already in a shitty mood, so don’t make things worse.”

“Yes, sir!”

“Enough. Clean everything up and put things back the way they were. And bring another barrel of liquor to replace it.”

“Pardon? But…”

“Are you insane? How dare you talk back to me? Get moving!”

“Y-yes, sir!”

As the subordinate hurried away, shouting frantic acknowledgments, Mu Song let out a deep sigh.

*Nothing is going right.*

This wasn’t a simple complaint. It was the truth.

Even good fortune would not have been enough to make up for it, yet one bad thing after another kept happening.

He had been forced to leave his home base in Sichuan and come to Hubei. Not long ago, he had also had to say goodbye to Hwang Chung, the Yangtze One Saber, who had been like family to him.

Believing he had to settle what he owed Hwang Chung, he had agreed to take Jin Taekyung’s group as far as Henan. But as expected, the worst possible situation had come to pass.

*I was going to keep pretending not to know until the end.*

An unidentified old master who had clearly achieved Returned to Youth.

That beast wearing the guise of a young medical apprentice had realized that his identity had been exposed.

*What kind of monster is that old man? Who the hell is he?*

Based on Mu Song’s careful observations, only a tiny number of people among the group traveling with them knew the truth. At most, the Fire King, Jeok Cheongang, and Jin Taekyung?

Cheongpung was impossible to predict, but the fact that even he became quiet in front of Mungyeong made it highly likely that he knew too.

*Damn it. If I’d known this would happen, I should have taken the other ship.*

The Water Dragon Stronghold currently had two swift ships heading toward Henan. Jeok Cheongang had insisted that they split up because there were so many people, and Mu Song had not possessed the courage to defy the Fire King.

When Mu Song thought of the deputy Stronghold Lord, who was probably enjoying a comfortable journey aboard the other swift ship more than a thousand feet ahead, his stomach hurt.

*Compared to this, that ship is a flower garden. A goddamn flower garden.*

At least the other ship had people he could communicate with.

Gung Gibang’s smell could be dealt with by holding his breath for a moment, and watching the bizarre snake Cheongpung called Mimi perform its tricks was surprisingly entertaining.

But this ship?

*Blazing Flame Divine Dragon Jin Taekyung. Fire King Jeok Cheongang. And another old monster hiding his identity.*

Calling it a gathering of monsters would not be an exaggeration.

At least Jin Taekyung, who was technically his junior, still used formal speech with Mu Song. And since Mu Song saw Jeok Cheongang so often, the Fire King treated him more or less like a person.

But the last man was the problem.

*Those eyes…*

As he recalled Mungyeong’s cold gaze, Mu Song shuddered involuntarily.

One of the senior river bandits, who had been watching the Stronghold Lord’s strange behavior for some time, approached and cautiously asked,

“Stronghold Lord, are you all right?”

“Do I look all right?”

“Not at all, sir.”

“Then why ask? You already know the whole situation.”

“What a thing to say when I’m worried about you. Anyway, what in the world did that old monster threaten you with to make you look so—”

“Ugh!”

Mu Song’s hand shot out at the speed of light and clamped over his subordinate’s mouth. He looked around with tense eyes.

Only after checking twice, then a third time, that no one had heard did his anger finally boil over.

“Have you lost your mind? Are you dying to die?”

“Ugh—pfft!”

The senior river bandit barely escaped Mu Song’s grip and stammered,

“I-I’m sorry, sir. It just slipped out.”

“I’ve already told you several times, but you and everyone else are not to utter a single word about him. Understood?”

“Yes, sir.”

The senior river bandit was one of the few who had personally witnessed Mungyeong reveal his true power.

Mu Song sighed deeply at the man’s anxious, darting eyes before speaking.

“More importantly, did you make sure everyone thoroughly understood the orders I gave earlier?”

The senior river bandit nodded.

“Yes, sir. Just as you ordered, I firmly told everyone not to go anywhere near the stern.”

“Did anyone get suspicious?”

There were dozens of river bandits aboard. With that many people, there was always at least one idiot with no sense of discretion.

“There was one. Chunsam. Even after I told him it was the Stronghold Lord’s order, he kept asking questions three times. Nearly gave me a heart attack.”

Mu Song ground his teeth.

“I knew it would be that bastard. Where is Chunsam now?”

“We dunked him in the Yangtze and hauled him back out. He’s been tossed down below. He won’t be saying anything like that again.”

“Whew. Good work. Keep the others in line even when I’m away. One slip, and every last one of us could end up drowned at the bottom of the Yangtze along with the swift ship.”

Mu Song’s face was dark.

The monster known as the Fire King, Jeok Cheongang, had not been enough. Now they had an unidentified old monster who had achieved Returned to Youth as well. He almost missed the days when he had known nothing about it.

Seeing their godlike Stronghold Lord show such weakness, the senior river bandit asked anxiously,

“At this rate, are we ever going to make it back to Sichuan? We’ve already been away from the Water Dragon Stronghold for nearly two months. I’m worried it might stay vacant forever.”

“Don’t say such unlucky things. They say that even if you enter a tiger’s den, you can survive as long as you keep your head.”

“That works for a tiger. But against a Returned to Youth Supreme Peak master, I don’t think keeping your head a hundred times would do a thing…”

Come to think of it, he was right.

Mu Song quietly closed his mouth, unable to think of a reply.

That was when a voice came from behind him.

“I brought the liquor barrel. Where should I put it?”

Only one person in this situation would talk about a liquor barrel.

Irritation surged through Mu Song. Without even turning around, he snapped,

“Now that I’ve been letting this slide, that worthless bastard has been—”

“Did you just call me a worthless bastard?”

“……Huh?”

An instant that felt like an eternity.

At the sight of the senior river bandit staring over his shoulder with his mouth hanging open, Mu Song realized that he was thoroughly fucked.

At the same time, he remembered one fact he had forgotten.

*Ah. I left a spare liquor barrel at the stern.*

No wonder that subordinate had started to say something when Mu Song told him to bring another one, then stopped.

Mu Song’s vision blurred.

He had not even felt afraid when he was caught in the whirlpool at Tianling Falls. But now, he was sweating hard enough to wash his neck in it.

“Great Hero Mu Song.”

Mu Song squeezed his eyes shut, then slowly turned around with a forced smile.

The one person he never wanted to meet, even in his dreams, was standing there.

“O-oh, Mungyeong. W-what brings you here?”

“Nothing in particular.”

Mungyeong smiled brightly, like an ordinary boy his age, and answered,

“I was watching the Yangtze from the stern when your subordinate came over. I heard that Great Hero Mu Song had ordered him to bring a liquor barrel…”

“I-I did?”

“Didn’t you?”

“Well, I… I don’t remember giving such an order…”

At that moment, a river bandit appeared from behind Mungyeong with a barrel slung over his shoulder and called out briskly,

“Stronghold Lord! I brought the liquor barrel as ordered!”

Mu Song suppressed the urge to tear that subordinate’s mouth apart and continued,

“I… I do remember giving that order. Right. I did give it. It was obviously a mistake.”

“A mistake. I see.”

Mu Song felt Mungyeong’s gaze moving methodically over various parts of his body.

It had to be his imagination that made him feel as though Mungyeong was looking at his lethal acupoints.

It had to be.

Fortunately, perhaps his desperate wish had reached the heavens. Mungyeong soon withdrew his gaze and spoke.

“The enraged Great Hero Jeok was furious. He said that if something like this happened one more time, you had better be prepared.”

Of course, Jeok Cheongang had not gone berserk, nor had he said any such thing.

But Mu Song was not stupid enough to misunderstand what Mungyeong meant.

“Y-yes, I understand. Tell Great Hero Jeok that I’ll bear it in mind. But there is one thing…”

“Go ahead.”

“What should I do if there is something I absolutely have to take care of? Something needed for ship operations, for instance. Or meals.”

Mungyeong thought for a moment before answering,

“Great Hero Jeok told me to pass along further instructions. In the former case, Great Hero Mu Song is to come alone and take care of whatever needs doing. In the latter, you are to deliver the meals yourself.”

“……You mean I have to do all that alone?”

“Does that displease you?”

“It was my lifelong wish. I couldn’t be happier.”

“I see. Then I’ll be going now. I’ll see you at dinner.”

Mungyeong left Mu Song behind and started walking back toward the stern. Then he suddenly stopped and turned around.

“Oh, and one more thing.”

“What else? Is there still something you need to tell me?”

“Two portions will be enough for meals. All the way until we reach Henan.”

“Hmm?”

“Young Master Jin is going to have no appetite for the time being, so keep that in mind.”

There were still at least ten days until they reached Henan. No matter how poor his appetite was, going ten full days without eating was absurd.

Curiosity got the better of Mu Song, and he summoned his courage to ask,

“Um, did something happen to Junior Jin?”

“Oh.”

A dimple appeared beside Mungyeong’s mouth.

It was such a natural smile that even Mu Song, who considered him a monster, mistook him for an innocent boy for an instant.

“He must be busy right now. Very busy.”

* * *

Sometimes, I get the feeling I’ve become a human smartphone.

Like the warning message that tells you when your battery drops below fifteen percent, a similar System window had appeared in front of my eyes.

Beep.

> **System**
>
> - Most of your **internal energy** has been depleted.
>
> - **Circulate your qi** to replenish your internal energy. If your internal energy is completely depleted, you may suffer a Status abnormality!

But why?

If all my internal energy ran out right now, I would sink into the middle of this vast Yangtze. Yet instead of feeling a sense of crisis, I was more puzzled than alarmed.

And one reason for that was surely the presence of something approaching from far away.

Ssssh.

A large body was drawing closer with extraordinary stealth. The fin jutting above the surface looked oddly familiar.

*No, fuck.*

Why the hell was there a shark in the Yangtze?
## Chapter artifact 511

# Chapter 511

It was the dead of night, with darkness enveloping everything around them. Two vessels sailed swiftly forward with their sails spread wide.

*Sssshhh!*

Any sailor with good night vision would have been startled once by the vessels’ extraordinary speed, then twice by the flag visible beyond their faint torchlight.

The Yangtze River Channel League.

Those five characters, written in blue dye, served as a guaranteed pass allowing one to travel freely and safely across the vast Yangtze.

But the flag was both a pass and a symbol of raiders.

“What the…”

“L-look! The Yangtze River Channel League! They’re river bandits!”

“Eek!”

The pleasure boat’s passengers, who had been holding a feast on the water, fell into a panic. The fishermen hauling in their nets some distance away, however, reacted differently.

“What the hell are they screaming about? They ought to finish guzzling their booze.”

“Don’t worry about it. It’s not like this is the first time. But is that the swift ship the Yangtze River Channel League is so proud of?”

“I’ve seen one of those once before. It sure is damn fast, so it probably is.”

“If I had just one ship like that, I wouldn’t want for anything.”

“How many more fish are you planning to catch?”

“What are you talking about? If I had a swift ship, why would I bother catching fish to chase wealth and glory? I’d switch over to being a river bandit right away.”

There was only a hair’s breadth between a fisherman and a river bandit. When making a living became difficult, a person could take the net and harpoon they had used to catch fish until the day before and transform into a raider.

Perhaps that was why the fishermen did not seem particularly afraid of river bandits.

“Oh, they’re coming this way.”

“Leave them be. It’s not as though they’ll rob us anyway.”

“Damn. We don’t own enough for even river bandits to bother robbing us.”

The fishermen chatted as they watched the situation with keen interest.

Fishermen were sailors second to none when it came to toughness. Even foolish river bandits who knew nothing about the ways of the world avoided messing with them.

They might come looking to extort a few pennies, only to end up skewered on a harpoon.

The Yangtze River Channel League was no different. Robbing fishermen for a few coins simply was not worth the trouble.

So from the fishermen’s perspective, this was like watching another man’s house burn down.

But a little while later, they watched the swift ships pick up speed and disappear into the distance. The fishermen tilted their heads.

“Huh? They’re just leaving?”

“So they are. Do you think some important young master from a powerful family is aboard that pleasure boat—important enough that it wouldn’t be worth messing with them?”

“They didn’t even check anyone’s identity before speeding off.”

“Forget it. What does it matter? Let’s finish hauling in the nets and get home before it gets any later.”

“Yeah, all right.”

Once the two swift ships disappeared without incident, lively music began flowing from the pleasure boat again. The fishermen smacked their lips regretfully, then returned their attention to their own work.

That was how things remained until, just half a shichen later, an unidentified, monstrous cry rang out from somewhere.

“Kkyat-meu!”

At first, the fishermen who heard it did not think much of it.

“Good grief. They ought to show some restraint. They’re making an awful racket over there.”

“Looks like someone knows how to party.”

“I’m already half dead from exhaustion, and now they’re making noises like ‘Kkyat-meu.’ I ought to go punch a hole in the bottom of that boat.”

The half-gray-haired fisherman who had muttered irritably reached for his net again.

That was when another cry rang out.

“I’m going! I’m going! I’m going! I’m going zoom!”

“Yeah, yeah, I’m coming right now, you bastards.”

The fisherman snatched up a harpoon, his eyes rolling back in fury.

“Fuck this. I’ll hurry over, punch a hole in their hull, and come right back, so nobody try to stop me.”

“Wait. Just wait a moment.”

The fishermen finally realized that something was strange and pricked up their ears.

“This… doesn’t sound like it’s coming from the pleasure boat.”

“You’re right. Then what is it?”

“So the sound came from…”

As though they had made a pact, the fishermen all abruptly raised their heads and searched in every direction for the source of the noise.

The music stopped abruptly aboard the pleasure boat as well. Apparently wondering what was going on, men and women dressed in dazzling silk stood at the bow and stared out at the pitch-black Yangtze.

“Did we hear wrong?”

“I definitely heard something strange.”

“Good grief. It’s not as though we’ve been bewitched by a ghost.”

Just as everyone was beginning to doubt their own ears—

*Whoooosh!*

Along with the roar of water being violently split apart, a person appeared.

No, strictly speaking, he was not alone.

“……Oh, my.”

“W-what the hell is that?”

At last, everyone saw the identity of the uninvited guest and opened their eyes wide.

It was astonishing enough that a young man was crossing the Yangtze in the middle of the night with his upper body completely bare. But when they realized what the enormous creature swimming ahead of him was, bound by some unknown rope, they could hardly believe their eyes.

“A s-sa-eo! It’s a sa-eo! Someone’s riding a sa-eo!”[^1]

The shout that burst from someone’s mouth shattered the silence that had settled over the river.

And everyone realized that the bizarre noise they had heard was part of the reality unfolding before their eyes.

*Whoosh, whoosh, whoosh!*

A sa-eo—a monstrous fish with an enormous, hideous body and a naturally vicious temperament, said to devour even human beings.

That very fish was swimming with a person riding behind it.

And what was more—

“T-there’s more than one!”

“One fin, two… five! There are five sa-eo!”

It was truly horrifying. It was unusual enough for sa-eo, which mainly lived in the open sea, to appear in the Yangtze. But five of them had gathered in one place.

If that had been all, the fishermen would not have stood there so dumbfounded.

The reason they had been rendered speechless was simple.

“……Tell me, am I dreaming right now?”

“……I think I’m having the same dream.”

“It looks to me like that young man has put some sort of bridle on the sa-eo and is, well… driving it.”

“I don’t know what that thing is. It’s terrifying…”

Just as the fishermen had said, the five sa-eo had something resembling bridles in their mouths.

A faintly glowing rope had been wrapped tightly around all five snouts, and the young man gripped its other end firmly in his hand.

“Turn left!”

When the young man pulled his wrist along with the shout—

*Whoooosh!*

The sa-eo all moved to the left at once.

“Turn right!”

When he twisted his wrist in the opposite direction—

*Whoosh!*

The sa-eo changed course accordingly.

The five sa-eo had great stamina and tremendous speed. They split the water ahead of them while the young man followed behind, supporting himself on the river with both feet.

They were as fast as the swift ships that had passed earlier—if anything, faster.

“What in the world is that?”

Just as someone muttered in a dazed voice, the young man came rushing right up to the fishermen in the blink of an eye and waved at them.

“Welcome, fishermen.”

“……!”

“Sorry to bother you when we’ve just met, but I’d like to ask for directions. Did two ships pass through here earlier? It would’ve been somewhere between half a shichen and one shichen ago.”

The fisherman who had been planning to attack the pleasure boat lowered his harpoon and answered awkwardly.

“W-we saw ’em. You mean the swift ships, right?”

“That’s right. The Yangtze River Channel League. There was a kid standing at the stern who looked like a nasty little shit.”

“I-I don’t know about that. But if you mean the swift ships, they went over that way. About half a shichen ago.”

“Half a shichen? I’ve almost caught up. Whew, fuck me. I busted my ass getting here.”

“……?”

The fisherman hesitated at the young man’s rich, vivid choice of words, no less colorful than any sailor’s. Just then, the young man casually loosened the strange rope wrapped around his hand.

The fishermen belatedly realized that one of the sa-eo had been released and panicked.

“Urgh!”

“T-the sa-eo’s been released!”

“Back! Back! Row!”

But the situation they feared did not occur.

The sa-eo merely blinked at the young man as docilely as a crucian carp, while the young man opened his mouth with an unconcerned expression.

“Sa-eo? Oh, you mean a shark.”

“What the hell do you think you’re doing?”

“I know what you’re worried about, but my boy doesn’t bite.”

“Your boy?”

“I’ll show you. Here, fin.”

The fishermen’s eyes bulged.

The moment the young man extended his hand, the sa-eo, which had been rolling its eyes around, thrust out its fin.

“See? He listens well, right? I keep telling you, he’s a good boy.”

Not good. More like he had been made good.

The fishermen swallowed the words that had risen to their throats.

The ragged fin and trembling body of the sa-eo were just their imagination. They had to be.

Whether or not he knew that the fishermen were staring at his muscles, the young man continued speaking calmly.

“My boy has anger-management issues, but he’s been controlling himself well ever since I beat the shit out of him. You’ll be fine. You won’t get another chance like this, so why don’t you take one off my hands?”

“Pardon?”

“As thanks. For telling me where the ships went. I have to let them go soon anyway. But do you have anything to eat? I’ve had nothing but sashimi for three meals straight, and it feels like my stomach has turned into an aquarium.”

The fisherman had no idea what was happening, but he instinctively understood what would be best for his own safety.

Trembling like a leaf, he handed over the food he had tucked inside his clothes.

“H-h-here.”

“Ah, yes. Th-thank you.”

The young man accepted the blandly seasoned rice ball and flashed a playful grin.

“Then catch lots of fish.”

*Whoosh, whoosh, whoosh!*

That was the last they saw of him.

The fishermen stared blankly as the sight of one man and four fish vanished into the distant darkness in an instant. Then they looked at the only trace he had left behind.

*Shudder!*

The sa-eo had foolishly picked a fight with the wrong person, been thoroughly beaten, and now feared human beings themselves. The shark—or rather, the white sturgeon—trembled violently.

And the fisherman who had become its new owner realized that his fate had just changed dramatically.

“……I guess I don’t need a swift ship anymore.”

That was the moment a new Morning Star was born in the world of river bandits.

* * *

I can guarantee that no one in either the modern world or Murim has ever experienced water skiing as eco-friendly as mine.

*Sssshhh!*

“Shark number four. Your posture is wavering.”

*Flinch!*

“Yes, you who just flinched. You. Are you an individualist?”

*Swish!*

“Just keep going like that. You’re not going alone. Match fins with your friends and go together.”

Of course, I had used a little violence.

Apparently a few punches hadn’t been enough, because they kept charging at me. So I worked their fins over a little and pulled out a few teeth.

If an environmental group had seen me, they would have called me a nature-destroying criminal who outraged heaven and humanity, as well as an animal abuser who would suffer even in death.

But I hadn’t cared from the beginning.

*It’s not like I’m Shanks or anything.*

The kindhearted hero who offers up one arm because a shark looks hungry only exists in old comic books.

I grabbed one of them, taught it a lesson, called over more of its kind, and founded the Shark Water-Ski Team.

I called it the Catch-’Em Fish Farm.

*Still, I wouldn’t have made it this far without these guys.*

I looked fondly at the water-ski team members who had carried out their mission admirably.

By alternating between resting and moving for half a day, I had replenished some of the internal energy that had once bottomed out. I had also narrowed the distance to the swift ships considerably.

The reward for hard work was freedom.

“All right, everyone. Off you go.”

That was when I untied the ropes around their snouts—or rather, the Water God Dragon’s sinew I had stashed away last time.

“……You really are a lunatic.”

I turned my head at the voice that suddenly slipped into my ear.

Beyond the deep darkness, a person was walking toward me across the surface of the water.

[^1]: *Sa-eo* (鯊魚) and *sang-eo* are both Korean terms for “shark.” *Sa-eo* is the Sino-Korean reading, while *sang-eo* is the ordinary word.
## Chapter artifact 512

# Chapter 512

“…What a lunatic.”

The voice was thick with disbelief, and the red hair stood out even in the deep darkness.

I opened my eyes wide when I came face-to-face with someone I never expected to see.

“Oh? What brings you here?”

“That’s…”

Jeok Cheongang hesitated, his voice trailing off.

“I got seasick and got off for a bit.”

“Ah, seasick. The Old Master got seasick.”

This wasn’t just any Supreme Peak master. This was the Fire King himself.

It would have been more believable for Spider-Man to retire because of acrophobia than for Jeok Cheongang to suffer from seasickness.

“What’s with that smile?”

I forced down the corners of my mouth and answered.

“I naturally have a smiley face.”

“Want me to make it look ready to die?”

“No, thank you.”

“If you have a complaint, say it to my face. Don’t grin at me like a creep.”

“I never said I had a complaint. But what are you hiding behind your back?”

“H-hiding? What are you talking about? What would this old man be hiding?”

“The thing you’re holding in your clasped hands. Whatever could it be that you’re so embarrassed you have to hide it? Are you some kind of Murim high-school girl boss?”

“I said I’m not hiding anything!”

Jeok Cheongang shouted at my sharp observation and awkwardly lowered his clasped hands.

He was fiddling with something wrapped in a large leaf, and the conflict in his movements was obvious.

*It looks like food. And damn, does it smell good.*

The meaty aroma carried on the wind was incredible. My stomach had spent more than half a day digesting nothing but raw fish and grilled fish, so of course it began to churn.

*Grrrrowl.*

“Is it pork?”

“Beef.”

“You didn’t catch it fishing, did you?”

“Of course not. It was loaded in advance. Those river bandits coated it with spices and grilled it. It’s quite good.”

“That sounds delicious.”

“It’s so good that five people could die while two were eating and they wouldn’t even notice.”

“That sounds like deadly poison.”

“It’s that delicious.”

“Then give me some. I’ll have a taste.”

“Hah. You’re not even funny. Did you think I brought it for you?”

“Ah. So you packed it for yourself?”

“Of course.”

“So you got seasick, abandoned the swift ship, and were left in the middle of the river you hate so much while the swift ship sailed away, and yet you still went out of your way to bring food…”

I looked at Jeok Cheongang and slowly nodded.

“That does make a certain amount of sense.”

“…!”

“Give it here.”

Jeok Cheongang answered in a surly voice.

“Here. Stuff your face.”

“Why, thank you.”

“I was originally going to eat it myself, but I lost my appetite, so I’m giving it to you.”

“I know. I know everything. Why do you keep explaining something the whole world already knows?”

“...Damn it.”

I let Jeok Cheongang’s grumbling pass in one ear and devoured the meat.

By the time my short but fiercely fought meal was coming to an end, the four sharks that had been circling nearby while watching me warily had disappeared from sight. So had the swift ship that had been faintly visible in the distance.

“Ah, I missed it.”

“You mean the sa-eo?”

“No. I was planning to let them go soon anyway.”

“Then the swift ship?”

I licked the sauce from my fingers as I answered.

“Yes.”

“You don’t seem particularly disappointed for someone who missed it.”

“I have no reason to be disappointed.”

“What a strange fellow. Didn’t you use the sa-eo to chase the swift ship all the way here so you could catch up?”

He was right. I couldn’t deny it.

But…

“I was starting to regret it.”

“Regret?”

“Yes. Regret.”

“Why?”

“Because doing this… has no meaning.”

I had captured the sharks and come all the way here under the pretext of replenishing my internal energy. But the closer I got to the swift ship, the harder it became to ignore the discomfort in my heart.

And perhaps that was because I had acted against the way I had lived until now.

*I’d let myself grow careless without realizing it.*

I had already gained power I could never have imagined in the past. Enormous wealth, fame, and the attention of the world followed my name like labels attached to it.

Perhaps I had become intoxicated by the rewards that had come with all of that.

*I wouldn’t have acted this way before.*

To obtain something, you had to pay a price equal to its value.

If I had still been the F-rank Hunter who had secured a home for my family in an expensive Safety Sector far beyond our means and thrown myself into raids without rest to pay my mother’s hospital bills, I would never have used some cheap trick involving sharks.

The same went for the version of me who had endured a year of brutal training at Mount Jiuhua without once running away to reality.

“I should’ve just held on to a reef back there.”

Jeok Cheongang frowned at my complaining joke.

“Then you would have fallen even farther behind the swift ship.”

“So what if I fell a little farther behind? I would have learned something equal to the distance I lost.”

“You might never catch up before we reach Henan.”

“I don’t care. Catching up isn’t the goal.”

Jeok Cheongang’s stiff expression slowly relaxed.

“You realized the most important thing in half a day.”

I lowered my head toward him. At that moment, I couldn’t bring myself to meet his eyes.

“It took me half a day. I’m sorry.”

“At first, I waited because I was worried about you. After that, I planned to give you a thorough scolding.”

From Jeok Cheongang’s perspective, it must have been utterly absurd. He had even outsourced my training, only for me to put together a Shark Water-Ski Team and use a cheap trick.

But his voice, flowing between his lips now, was gentle.

“I certainly intended to do that… but this will do. From now on, try to catch up using your own strength.”

Jeok Cheongang finished speaking and stepped forward. The ripples scattering from his toes were so calm they could not even be compared to mine.

Noticing my gaze, he tossed out a single remark.

“Our sect’s martial arts have an especially violent flow. I wasted years calming this storm on my own.”

“Years…”

“You already know it. You know this isn’t something you can learn overnight.”

“I know. I also know that it isn’t overnight. There are still ten days left.”

I shrugged and added,

“But I have two excellent advisors beside me to tell me which way to go. So it should be much easier than the process you went through, Old Master.”

The Fire King and the Slaughter Saint. They were both experts far above me, people who had already traveled far ahead along the path I was taking.

Didn’t that put me in a much better position than Jeok Cheongang, who had been forced to realize everything on his own without anyone’s help?

Jeok Cheongang let out a quiet laugh.

“Look at this sly bastard. You’re proudly announcing that you intend to use another shortcut.”

“I find it hurtful that you call it a shortcut. Most people call something like this a fortuitous encounter.”

“Hah. Your tongue is as smooth as flowing water.”

“But you aren’t denying it.”

“Because you’re right, when I think about it. But that isn’t the only difference between you and this old man.”

“…?”

“Martial talent. With that outrageously excellent body and talent of yours, you should be able to sprout at least one bud before reaching Henan.”

A towering tree and a gorgeous flower both began with a single small bud.

It had taken Jeok Cheongang years to bloom, but I would be different.

After watching me in silence for a while, he suddenly spoke.

“I can’t see the ship anymore. We should hurry and chase those damned bastards.”

“Take care. If you run into a sa-eo on the way, catch one and try riding it.”

“That means you don’t intend to come with me.”

What a mischievous old man. He had clearly already guessed what I intended, yet he was still testing me. I couldn’t help but chuckle.

“I’ll follow in a little while.”

“A little while? That’ll be half a day.”

“It still doesn’t sit right with me. So yes, that’s what I intend to do.”

“Tsk, tsk. There are all sorts of ways to make life difficult for yourself.”

Even as he said that, he couldn’t hide the corners of his mouth lifting into a smile.

Jeok Cheongang stared at me for a moment, then turned and shot toward the deep darkness.

Even after his back had become a dot and disappeared, I stood there for a long while.

At last, the sun rose, and the sunlight began to heat the river.

*Splash.*

I stepped forward through the rough current.

My destination was the swift ship.

No—the destination was Henan.



* * *



The entire Murim world seethed like water in a cauldron.

What had begun as a simple rumor spread in every direction on the lips of gossipmongers. Then one day, dozens—hundreds—of messenger pigeons rose from Mount Song in Henan, each carrying a letter that would turn the rumor into fact.



*To the Murim of the world.*



The letters began with that brief sentence and were delivered across the land. Those who learned their contents realized the truth.

An era of upheaval that no one could escape had arrived.

The New Murim Alliance.

An old martial-world veteran whose entire body was covered in scars remembered the Great Faction War, when corpses had formed mountains and rivers had flowed with blood. Young martial artists born in peaceful times, who had never experienced that horrific past, were swept up in every imaginable emotion.

“The time has come.”

“At last…!”

It was said that troubled times gave birth to heroes.

Some could not hide their excitement at the thought that their chance to make a name for themselves had arrived.

“H-how can this be!”

“So it’s finally come to this.”

Others trembled with fear at the deaths that would soon descend upon them.

But the orthodox Murim of the present era was the victor proven by history.

Had even the mighty Demonic Cult not been defeated and driven back without taking the Central Plains several decades ago?

Although a bloody storm had struck Shaolin and Sichuan, to most martial artists it was a reason to grow angry and fight back—not something that warranted retreating in fear.

“Those with conviction! Any martial artist who carries a weapon, stand beneath the Murim Alliance’s banner!”

The cry rang out across the land.

And there were those who answered it.

“Shaolin of Mount Song requests to join the alliance.”

“Huashan will join the Murim Alliance as well.”

The Nine Sects and One Gang. The Five Great Families.

The fifteen pillars supporting the Murim of the present world began to move.

Shaolin Temple and Huashan were the first to raise the Murim Alliance’s banner, and the other prestigious sects and great factions rushed to request membership as well.

Gossipmongers filling the markets, pleasure houses, and inns were busy talking about it day after day.

“Have you heard? They say the Nine Sects and One Gang and the Five Great Families have all joined the alliance.”

“It’s only been a day since the news became known. Already?”

“Your information is slow. Of course they have. The question is what the other sects will do.”

“I heard the Shandong Yue Family intends to join as well.”

“That’s a bit unexpected. Aren’t they in an awkward position between the Murim and the authorities?”

“What news have you heard from the Hahou Sword Family?”

“I understand the former Family Head died in the Great Faction War. From the current Family Head’s perspective, he’ll probably enter the war if only to avenge his father. There isn’t anyone left who doesn’t know that Dark Heaven is the successor to the Demonic Cult, is there?”

“The Murim Alliance is the symbol of orthodox Murim. The problem is those who practice demonic and heterodox arts—and the Outer Lands.”

Even as the gossipmongers carried on their conversation, movements were taking place all across the Murim world.

And amid the heat spreading like wildfire, ten days passed.
## Chapter artifact 513

# Chapter 513

Xixia in Henan Province, situated along a tributary of the Yangtze, was packed with people again today.

The ferry landing was crowded with boats of every size, while merchants with all kinds of goods piled around them haggled with fire in their eyes.

“Come on! Cheap, cheap! Musk that’s good for your virility, only one silver nyang!”

“I don’t need that crap.”

“Young Lady, you’re looking lovely! Would you like a hand mirror?”

“I’m not buying that crap.”

“…What a pair of fucking assholes.”

The marketplace rang with every kind of noise.

But in the end, the atmosphere of a place was determined by the kind of people who gathered there.

In that sense, the merchant who habitually grabbed hold of a passing young martial artist had chosen the wrong target.

“Sir. Judging by your appearance, you seem to be a martial hero on your way to Mount Song. Perhaps you need a well-honed weapon—gasp!”

The merchant, who had been chatting away with impressive smoothness, swallowed a startled breath.

The handsome face that had first caught his attention had vanished from his thoughts.

The moment he saw the three characters embroidered in black thread across the young martial artist’s dark blue silk uniform, along with the dragon pattern, the merchant let out a cry that sounded almost like a moan.

“B-Black Dragon Demon Gate!”

“……!”

Though the cry had not been particularly loud, the four-character name Black Dragon Demon Gate was enough to plunge the bustling thoroughfare into a pit of silence.

“B-Black Dragon Demon Gate?”

“They’re the unorthodox bastards who’ve been making such a name for themselves in Gansu.”

“I heard they arrived in Henan late yesterday… Could they be here to join the alliance?”

The silence spread in an instant.

The merchants who had been shouting at the tops of their lungs, the commoners wandering nearby, and even the martial artists traveling in groups with weapons at their waists—

Everyone stopped what they were doing and focused their attention on the source of the cry.

Under the gaze of countless people, the young martial artist from the Black Dragon Demon Gate smiled faintly at the merchant.

“You have a decent eye for a merchant. To recognize even our sect’s insignia.”

“Th-that’s…”

“You don’t seem to have much connection to Murim. Are you originally from Gansu? Or perhaps… you picked up a few scraps of knowledge from the Third Rate swordsmen who came here as customers.” 

The young martial artist glanced over the merchant’s shoulder at the various weapons arranged neatly on the stall and clicked his tongue.

“Every last one is so cheap I wouldn’t take it even for free. Bring me the best one.”

“Pardon?”

The young martial artist sighed.

“I forgot you were a merchant. In that case, bring me the most expensive one instead of the best.”

“Y-yes, understood.”

With trembling hands, the merchant pulled out and opened an iron chest hidden deep in the stall.

When the young martial artist saw the lone sword lying inside without even a decent scabbard, he whistled.

“Hm. That doesn’t look like the sort of thing that should be in a place like this.”

The people watching the two of them—especially the martial artists—nodded without realizing it.

Although the sword looked quite old, its blade shone with a dazzling array of colors, and its edge had lost none of its sharpness.

It was a weapon that could easily be called a famed sword.

Sensing greed appearing in the eyes of several martial artists, the merchant hunched his shoulders.

“M-my late father passed it down to me.”

“Was your late father a martial artist?”

“Th-that’s impossible. Somehow, he came to own the sword, but he only told me to keep it secret from others and preserve it as a family heirloom for generations…”

“That makes sense. A sword of this quality would have attracted more than a few greedy eyes.”

Excessive greed led to bloodshed.

Most martial artists would choose to take a famed sword by force rather than pay several hundred silver nyang for it.

After all, thrusting a cheap iron sword at someone was far more effective than gathering enough silver to buy a famed sword.

“Your late father must have been quite wise.”

“Y-yes, yes, he was.”

“But it seems you didn’t inherit his wisdom. Not if you’re displaying something like this so openly.”

“Th-that’s…!”

The merchant could not continue, and the young martial artist let out a quiet laugh.

He had already seen straight through the words the merchant could not bring himself to say and had swallowed instead.

His customer was a martial artist from the Black Dragon Demon Gate, an unorthodox faction.

With a knife at his throat, the merchant had not had time to think things through. Fear had paralyzed his judgment—the fear that if he brought out some other item clumsily, his head might be severed.

It was the first time the merchant had ever experienced such a situation.

For the young martial artist, however, it was familiar.

“I understand. Most people who face me think and act exactly as you did.”

The young martial artist looked the merchant up and down. The merchant sat with his mouth shut, like someone who had swallowed his tongue.

“So I’ll save you.”

Suspicion flickered across the merchant’s eyes.

“Wh-what do you mean?”

“I mean I’ll pay for the sword and take it.”

“Ah!”

The merchant’s face brightened.

His heart had already been burning with anxiety.

He had taken the sword out because he had decided that surviving came first, but more than a few people had seen the famed sword with their own eyes.

Once the young martial artist in front of him left, rootless wandering martial artists and petty thieves would surely smell the opportunity and gather around.

But if this man bought the sword, everything would be solved.

Of course, there would be people who coveted the silver he received in payment, so he would have to leave the area soon. Still, he could preserve his life, secure a comfortable fortune, and enjoy a prosperous life somewhere else.

Having finished his calculations, the merchant immediately bowed deeply.

“G-Great Hero, if you would do that, I could ask for nothing more!”

“You’re not completely empty-headed.”

The young martial artist gave a faint laugh and tossed a money pouch from his robes onto the stall.

Clink.

The merchant opened the pouch after it landed with a heavy sound and blinked.

“G-Great Hero. This is…”

The young martial artist, who had taken the sword from the iron chest and was examining it from every angle, glanced over.

“What is it?”

“Well, I’m afraid you may have miscalculated the amount.”

“Mis-calculated?”

As the young martial artist tilted his head, the merchant swallowed hard.

The famed sword he had inherited was a family heirloom, and merely judging by its value, it was worth at least several hundred silver nyang.

Compared to that, the amount inside the pouch was absurdly small.

“Twenty silver nyang is a little…”

“Well, I see it differently.”

“Pardon?”

“That should be enough. I deducted the price of your life.”

The young martial artist’s voice sank in an instant, and the air around them turned cold.

The commoners watching with expressions mingling curiosity and fear shuddered, while the neighboring merchants who had shared his ups and downs all this time deliberately looked away.

But not everyone there was willing to remain silent.

“The Black Dragon Demon Gate must have quite a reputation if even some wet-behind-the-ears brat is throwing his weight around like this.”

With that rough voice, the crowd split apart. A middle-aged man walked through the opening, grinning at the young martial artist and baring yellow teeth.

“I won’t waste words. Put down the sword in your hand and get the hell out of here.”

The young martial artist blinked.

“Were you speaking to me?”

“Ha! Look at this brat. Who else would I be talking to?”

“Ah, don’t misunderstand. I heard you perfectly well…”

The young martial artist slowly looked the middle-aged man up and down before continuing.

“I simply never imagined that someone like you could say something like that so boldly.”

“…Someone like me? Say something like that?”

For a brief moment, the middle-aged man stared blankly at the young martial artist.

Then he threw back his head and roared with laughter.

“Someone like me? Ha! Hahaha! You’re funnier than you look.”

“That’s strange. No one in Gansu ever told me I had that talent.”

“Boy, what’s your name?”

“I have no particular reason to tell you, and no intention of doing so. Go on your way.”

“You don’t look so good. Are you frightened?”

“It’s not that… It’s just that I find speaking with someone like you rather unpleasant.”

“Heh.”

The middle-aged man laughed aloud, but his eyes gleamed ominously.

His arm, bulging with muscles and covered in scars, was just beginning to move when the young martial artist suddenly spoke.

“That’s enough, Blood Cudgel.”

“……!”

The middle-aged man’s body jerked at the sound of his sobriquet.

Blood Cudgel Do Sangho.

The martial artists watching the confrontation were equally unable to hide their surprise.

There was quite a bit of information circulating about Blood Cudgel, so it was not difficult to guess his identity from the middle-aged man’s appearance and the red cudgel hanging at his waist.

What surprised them most was the young martial artist’s attitude.

A brat dressed in the Black Dragon Demon Gate’s uniform, speaking and acting as if he were looking down on the outstanding Peak master Blood Cudgel from a great height.

Blood Cudgel himself felt something was strange.

“You… knew who I was?”

“I’ve heard of you. I know there’s a man who’ll lick a beggar’s ass as long as he’s paid in silver.”

“……!”

At some point, he had dropped his polite speech and begun hurling insults.

Blood Cudgel’s eyes widened with rage, and the young martial artist continued slowly.

“Now that I’ve met you in person, what I heard seems to be true. How about I make you an offer?”

“An offer?”

“I’ll give you silver. Lick the top of my foot, and I’ll let you live.”

“H-how dare you!”

Blood Cudgel’s body trembled.

He was a Peak master with martial prowess no one could ignore. He wanted to rush forward that instant and smash the brat’s head open.

But the four characters Black Dragon Demon Gate held him back.

The young man was so impossibly young, yet his attitude was so calm. Blood Cudgel hesitated because he had a gut feeling that if this turned into a life-and-death duel, the outcome would not be good for him.

“…Damn it.”

In the end, Blood Cudgel lowered the weapon he had half-raised.

The young martial artist smiled.

“You must really like silver. Is it time to lick my foot now?”

“You bastard, shut your mouth!”

The shout, packed with profound internal energy, lashed out in every direction.

Third Rate martial artists with shallow cultivation groaned and staggered backward, while terrified commoners screamed.

Amid the extreme chaos, Blood Cudgel glared at the young martial artist with bloodshot eyes.

“I don’t know how important you are, but you’ll regret what happened today someday.”

The young martial artist clicked his tongue softly.

“You seem pretty angry. But you should stop there.”

“I, Blood Cudgel Do Sangho! I may forget a favor, but I never forget a grudge. Though I’m retreating like this today, the next time we meet will be the day of your funeral—”

Thud!

Blood sprayed in every direction.

The young martial artist looked at Blood Cudgel’s corpse, its head crushed and its life extinguished, and sighed.

“I tried not to draw blood if I could help it. You should have held back a little longer.”

When had he appeared?

An eight-foot-tall man who had crushed Blood Cudgel’s head with a swing of his massive two-section staff answered in a halting voice.

“Dare… insult Young Sect Leader. This subordinate… will not tolerate it.”

“Well, Blood Cudgel may be acceptable. It’s not as if he could really be called orthodox.”

The young martial artist clicked his tongue softly.

Only then did the people who had belatedly understood what had happened begin scattering in every direction with screams.

“A person’s been killed!”

“Aaaah!”

“What the hell…!”

The martial artists were frozen by the sudden turn of events.

At that exact moment, the young martial artist spotted something beyond the fleeing people and muttered to himself.

“See? I knew there’d be trouble.”

At the end of his gaze, a group of monks wearing yellow kasayas was approaching them.

“So it’s Shaolin Temple…”
## Chapter artifact 514

# Chapter 514

Shaolin Temple, the Mount Tai and Northern Dipper of the Murim.

Whenever turmoil descended upon the Central Plains, Shaolin had always been the first to fight. They had done so a thousand years ago, a hundred years ago, and again during the Great Faction War several decades earlier.

They had shed more blood than any other sect in the Murim as a result, but not a single person in Shaolin Temple regretted it.

It was what they had been meant to do. They had done it for a brighter future—for the greater cause.

And that was the conviction held in the hearts of the group of monks crossing a well-paved road.

Whoosh!

The yellow kasayas draped over the monks fluttered in the fierce wind.

It was a clear spring day without even a breath of wind, but the swift movement techniques carrying the monks forward were more than enough to stir up wind of their own.

“Xixia is in sight.”

There were twenty Shaolin monks. At the words of the martial monk leading them, a middle-aged monk nodded.

“Fortunately, we won’t be late.”

“Yes. The appointed time is around shenshi, so we still have nearly one shichen left.”

Although Xixia covered a broad area, these were martial monks who had reached a considerable realm. Even at their normal pace, a shichen was more than enough time to reach the ferry landing at Xixia.

Having finished his calculations, the middle-aged monk shook the Zen staff in his hand.

Clatter.

The martial monks understood the signal and came to an abrupt stop.

To halt movement techniques that fast in a single instant was proof that their mastery of martial arts had reached a considerable depth.

The middle-aged monk looked over them with satisfaction before slowly turning around.

Someone stood there, wearing a conical hat pulled low over their face.

“We’re about to enter the main road. The commoners may become anxious, so may we slow down from here?”

The middle-aged monk spoke with utmost respect. From beneath the conical hat, tightly closed lips moved.

“Please do.”

The voice was so hoarse that it was impossible to guess the speaker’s age. For a brief instant, grief and pity passed across the faces of everyone present, including the middle-aged monk.

“Thank you for granting permission, Martial… Uncle.”

And with that address, which still had not become familiar to him, the middle-aged monk and the martial monks turned toward Xixia and resumed walking.

That was when—

“Aaaaaah!”

“Murder! Someone’s been killed!”

Faint screams and shouts drifted from far away.

Before the middle-aged monk, whose internal energy was profound, could alert the other disciples, the person wearing the conical hat spoke abruptly.

“It seems we should hurry.”

“……!”

* * *

Whoosh!

Twenty figures flew through the air.

The sight of their fluttering yellow kasayas and the stern faces rapidly drawing closer made the young martial artist of the Black Dragon Demon Gate frown.

“So it’s Shaolin…”

They were an unpleasant group to encounter. Especially at a time like this, with a simple-minded subordinate having killed someone in the middle of a main road.

“What an idiot.”

Thwack!

The towering giant who had been struck in the shin groaned.

“Young Sect Leader. This subordinate hurts.”

“I hit you to make you hurt. I told you to be careful. Why do you always act without thinking?”

“He deserved to die.”

“Whew. There’s really no getting through to you. Fine. The water’s already spilled. What can we do?”

“We should pick it up somehow. No matter what.”

At someone’s curt voice, the giant blinked his large, calf-like eyes.

“Young Sect Leader. This subordinate. No.”

“You don’t need to say it. I already know.”

The young martial artist turned around with a faint smile on his lips. Five steps ahead, he faced the stern middle-aged monk and performed a fist-palm salute.

“It is an honor to meet Shaolin’s eminent monks. I never expected to meet Master Jung Ho so soon.”

The middle-aged monk, Jung Ho, twitched his thick eyebrows.

“You know me. Yet this seems to be our first meeting.”

“It is our first meeting, but I have often heard of your reputation.”

“There is no reputation worth mentioning where this humble monk is concerned. Nor am I worthy of being called a Master.”

“Just as my father told me. You really are a humble man.”

“Your father?”

“He once told me about a truly fiery-tempered monk in Shaolin—ah. I mean, a monk of profound Buddhist faith who follows his principles to the letter.”

The young martial artist’s gaze fell on the Zen staff in Jung Ho’s hand.

“He also told me that you wield a Zen staff like a demon. A staff with prayer beads hanging all over it, no less.”

“……Amitabha. You have a sharp eye.”

“I’m relieved you’re the man I had in mind. It would have been rather embarrassing otherwise.”

Jung Ho regarded the young martial artist with a grave gaze, then spoke abruptly.

“That is fortunate indeed. But as I listen to you, I find that several things seem to fit.”

“I’m listening.”

“Your clothing is unmistakably that of the Black Dragon Demon Gate of Gansu, and the aura and bearing you give off are far from ordinary. You must be the Young Sect Leader of the Black Dragon Demon Gate, whose name I have heard only through rumor. Am I right?”

The young martial artist smiled faintly and lowered his head.

“Allow me to introduce myself again. I am the Young Sect Leader of the Black Dragon Demon Gate, Sama Pyo.”

“I have often heard of the Black Dragon Saber’s reputation. I have also heard that you are a Morning Star in no way inferior to the Ten Dragons and Phoenixes.”

A small stir passed through the monks standing behind Jung Ho.

The sobriquet Black Dragon Saber was that widely known. And as the Young Sect Leader of the Black Dragon Demon Gate, a force counted among the three strongest unorthodox factions, Sama Pyo possessed an impressive background as well.

But none of them saw the sneer that brushed across Sama Pyo’s lips as he lowered his head.

When he raised it again, his face was covered by a broad smile.

“That is excessive praise. To receive such a high opinion from Master Jung Ho despite being an unknown nobody like me, I hardly know where to put myself.”

“I will say it again: I am not worthy of being called a Master. Nor do I intend to overestimate you. I am merely speaking of facts that have already been proven. However…”

Jung Ho looked toward the corpse lying facedown in a pool of blood and continued.

“I am not yet familiar with the facts surrounding this unfortunate man’s death.”

Sama Pyo rubbed his bristly chin.

“Well, it’s a rather long story.”

“There is no need to worry. There is a faster way.”

Clatter.

At Jung Ho’s signal, a martial monk with a slender build stepped forward and examined the corpse.

Before joining Shaolin, he had traveled as a wandering martial artist and accumulated a wealth of experience. It did not take him long to identify the corpse.

“It is Blood Cudgel.”

“Blood Cudgel Do Sangho? Are you certain?”

“Yes. His head was crushed, but I am certain.”

“Blood Cudgel. So it was Blood Cudgel…”

Jung Ho touched the prayer beads hanging from his Zen staff as he muttered, then turned his gaze toward Sama Pyo.

“Did you know?”

“Know what?”

“That Blood Cudgel killed five innocent merchants in Shaanxi two days ago and has been on the run ever since.”

“I was unaware of that.”

“He must have thought himself safe because he committed the crime in a remote mountain area. It seems he grew bold enough to come all the way to Henan.”

“……Good heavens. What a heinous man.”

Sama Pyo deliberately furrowed his brow.

But it was not Blood Cudgel’s crime that troubled him. It was the information network that had identified and relayed the actions of a seasoned wandering martial artist in only two days.

*Is this the power of the Murim Alliance, or Shaolin’s strength?*

Blood Cudgel Do Sangho was a fairly well-known wandering martial artist, but that was because his methods were cruel and he went around boasting about himself.

In a Murim filled with masters far above his level, knowing someone like Blood Cudgel in such detail was proof of an information network as dense as a spiderweb.

*Not exactly welcome news… Though, considering everything that has happened, I suppose it makes sense.*

Sama Pyo kept his thoughts to himself and spoke.

“That is fortunate.”

“What is?”

“The water I spilled turned out to be rotten water. Doesn’t that make it look as though I took care of it before anyone could drink it?”

Jung Ho’s eyes sank deeply.

“You were not unaware of that fact.”

“The outcome is good, so isn’t everything fine?”

“The process is as important as the outcome. No matter what you say, killing someone in the middle of a main road where people were coming and going was not a wise course of action.”

“It was a dangerous situation. He had to be killed before he killed me. Ah, of course, that was not my intention either.”

Sama Pyo raised a hand and pointed at the eight-foot-tall giant standing beside him.

“This fellow is the culprit.”

The giant blinked his enormous, round eyes.

“Young Sect Leader. A person?”

“Facts must be laid bare. Wipe the blood off that vicious two-section staff and make your excuse.”

“That. Correct. Blood Cudgel kill. Me.”

“Please understand him with your generous heart, Master. He is skilled in martial arts, but his head is a little…”

Sama Pyo pressed a finger to his temple and made a slow circling motion.

Jung Ho stared at him in silence before speaking.

“You, or rather, the Black Dragon Demon Gate, will have to explain this matter properly.”

“Of course. This happened because I failed to keep my subordinate in line, so I will cooperate in any way I can.”

“You know this already, but the atmosphere has been far from good lately. The commoners, in particular, are trembling with anxiety.”

The Murim of the present day was like a powder keg on the verge of exploding.

Even an illiterate old villager who could not get through the Thousand Character Classic knew that the Murim Alliance was not merely a social club for martial artists.

During the Great Faction War, it had not been only the martial artists of the Central Plains who were caught up in the war.

“If open murder is committed in broad daylight on a main road at a time like this, people will inevitably look upon us unfavorably.”

“I will bear that in mind.”

“Even if the person who died was Blood Cudgel, a criminal who was fleeing after committing a crime, those above us may still hold you accountable.”

“I will gladly explain myself.”

“You must also apologize to the commoners in the area.”

“You need not worry about that either. I will even pay compensation if they wish.”

Jung Ho’s eyebrow twitched.

Though he was a martial monk, he had spent many years in Shaolin walking the path of a Buddhist.

He was displeased that this had happened, and he was not particularly impressed by the attitude of the Black Dragon Demon Gate’s Young Sect Leader, whose reputation he had already heard.

But what else could he do? Since Sama Pyo was obediently nodding, at least on the surface, Jung Ho had no choice but to turn away.

“Then… that should settle the matter.”

“We have met by fate. Why don’t we move somewhere else for a while?”

“Amitabha. I regret that I must decline. I have a guest to receive.”

Jung Ho answered with an expression that showed no regret whatsoever and was just about to turn away when—

“The sword.”

“Hm?”

“You do not seem to be someone who uses a sword.”

The voice was hoarse, like metal scraping against metal. Someone wearing a conical hat pulled low over their face continued.

“That object appears to have no connection to you. Return it to its rightful owner.”

“Ah, this?”

Sama Pyo smiled faintly as he looked at the sword in his hand.

“It belongs to me.”

“It does not appear so to my eyes.”

“If you do not mind my asking, who are you, Monk?”

“That has nothing to do with this.”

The smile at the corner of Sama Pyo’s mouth faded.

Then, from far away, someone shouted.

“The Jin Family of Taiyuan! It’s the Jin Family of Taiyuan!”

# Checkpoint Review — 865–869

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

# Chapters 865–869

## Plot

Hong Jin warns Jin Taekyung that Baek Yeon led the coup that put the fourth prince on the throne, betraying the late Emperor and Crown Prince and killing 30,000 people in the purge. Hong remains devoted to protecting Prince Shangshan, both to honor the late Emperor’s final wish and for personal reasons. He introduces Ma Sanbao, the East Depot’s second-in-command and his longtime ally. Ma reveals he has stayed in the palace loyal to the late Emperor and asks Hong and Taekyung to help enthrone Shangshan, offering a reward and claiming to know much about Dark Heaven. Taekyung has not agreed.

The Emperor summons Baek Yeon after an assassin reaches Qianqing Palace, conceals poison, and dies by suicide. Baek confronts the Emperor over his opium use and reminds him of their old promise and great undertaking. The Emperor breaks his pipe, plans to meet Shangshan the next day, and warns Baek not to allow another incident.

When Jeong Hogun and the Embroidered Uniform Guard arrive at the pavilion, Taekyung stops them from taking Shangshan and challenges whether they are protecting or surrounding him. Hogun mentions three red lanterns lit from the hour of the Ox to the hour of the Tiger, which he identifies as an East Depot secret signal. Taekyung connects its timing to Ma’s visit, suspects a trap, and denies knowing anything about the East Depot. Hogun escorts Shangshan to meet the Emperor; only Shangshan and Taekyung may attend, not Hong Jin.

## Continuity

- The Emperor has summoned Prince Shangshan and Jin Taekyung for an audience; Hong Jin is barred from accompanying them.
- Ma Sanbao and Hong Jin seek to enthrone Shangshan. Ma remained in the palace loyal to the late Emperor, while Hong left the East Depot to serve the prince. Taekyung has not decided whether to help.
- Ma claims extensive knowledge of Dark Heaven and offers a reward for Taekyung’s help; Taekyung suspects the reward could involve imperial support for the Murim Alliance.
- Taekyung suspects the three-red-lantern signal was a trap timed with Ma’s visit, and denies knowing about the East Depot.
- The Emperor seized the throne as the fourth prince in a bloody coup and purge. He relies on opium, which he calls medicine.
- An assassin reached Qianqing Palace, hid poison beneath a molar, and died by suicide. The assassin’s identity, backer, and intended target remain unknown.
- Baek Yeon and the Emperor share an old promise tied to a great undertaking; its details remain unclear.

## Translation Decisions

- Render 동창 as “East Depot,” 금의위 as “Embroidered Uniform Guard,” 금위군 as “Imperial Guards,” and 창위 as “Changwei.”
- Render 동창 병필태감 as “Brush-Holding Eunuch of the East Depot”; 병필태감 is the East Depot’s second-in-command.
- Render 밀마 as “secret signal” in this context and 천호 as “Thousand Captain.”
- Render 건청궁 as “Qianqing Palace,” 앵속 as “opium,” and 곰방대 as “long-stemmed tobacco pipe.”
- Render 창공 as “Director” for the East Depot’s head and 연판장 as “blood-signed pact.”

## Durable state

{
  "active_continuity": [
    "The Emperor has summoned Prince Shangshan and Jin Taekyung for an audience; Hong Jin is not permitted to accompany them.",
    "Jeong Hogun says three red lanterns lit from the hour of the Ox to the hour of the Tiger match an East Depot secret signal. Taekyung recognizes the timing of Ma Sanbao’s visit, suspects a trap, and denies knowledge of the East Depot.",
    "Prince Shangshan’s party remains under Embroidered Uniform Guard surveillance; Baek Yeon previously promised Taekyung that the guards would cause them no harm.",
    "Ma Sanbao secretly remained in the palace, loyal to the late Emperor and leading a group that seeks to enthrone Prince Shangshan; Hong Jin left the East Depot to serve the prince, while Ma stayed behind.",
    "Ma Sanbao says he knows much about Dark Heaven and offers a reward for helping enthrone Shangshan; Taekyung suspects the reward may be imperial support for the Murim Alliance against Dark Heaven.",
    "Taekyung has not decided whether to join Ma Sanbao’s plan and fears the consequences of failure.",
    "The Emperor is the fourth prince who seized the throne in a bloody coup and purge; Ma Sanbao says tens of thousands died, including many uninvolved in the struggle.",
    "The Emperor relies on opium, which he calls medicine, and broke his pipe to clear his mind."
  ],
  "continuity_sources": [
    868,
    869
  ],
  "open_questions": [
    "Will Taekyung agree to help enthrone Prince Shangshan, and what would the plan require?",
    "What does Ma Sanbao know about Dark Heaven, and what reward is he offering?",
    "What does the Emperor intend for Prince Shangshan and Taekyung?",
    "Who sent the assassin to Qianqing Palace, and what was the intended target?",
    "What happened between Hong Jin and the former East Depot Director?"
  ],
  "safe_through": 869,
  "temporary_decisions": [
    "Render 밀마 as “secret signal” in this chapter’s context.",
    "Render 창공 as “Director” for the East Depot’s head.",
    "Render 연판장 as “blood-signed pact.”"
  ],
  "version": 1
}

## Reading copies

## Chapter artifact 865

# Chapter 865

A person’s body and mind are like a bowstring.

Drawn taut, then released all at once.

Once the tension lets up, exhaustion is bound to catch up with you.

That was true even for me, after weathering countless crises. For a child who was barely twelve or thirteen, it went without saying.

*Click.*

Careful not to wake his young lord, Hong Jin closed the door with the utmost care and whispered to me,

“He must have been exhausted. He fell asleep in no time.”

A soft, even breathing came through the crack in the closed door.

Once I was sure Prince Shangshan was fast asleep, I glanced out the window.

Down below, amid the swaying torchlight, the Embroidered Uniform Guard stood like iron towers, clad in golden armor.

*You bastards. It’s gotten dark enough already. Why don’t you clock out on time for once?*

Of course, my wish wouldn’t come true.

From what I’d seen so far, those guys would risk not just overtime but their lives to carry out an order.

Murim martial artists were all crazy in their own way, but the Embroidered Uniform Guard were hunting dogs, blindly loyal to the Son of Heaven.

“Watching us like that won’t change anything. They won’t leave their posts for even a moment.”

Hong Jin surveyed the torches and guards surrounding the pavilion as if they were laying siege to it, then added,

“That’s how the Changwei operate.”[^1]

“Changwei?”

“Oh, it’s a collective name for the East Depot and the Embroidered Uniform Guard. As I told Young Master Jin, I was once part of one of them.”

I’d heard that Hong Jin used to belong to the East Depot, of course, but there was still plenty I wanted to ask him.

And as if he’d read my mind, Hong Jin spoke first.

“Now that it’s finally just the two of us, shall we talk for a bit?”

I’d be grateful if he did.

I nodded, and Hong Jin and I walked downstairs together.

We’d already sent away the Embroidered Uniform Guard, as well as the palace attendants who were more or less there to keep an eye on us for them.

Even though I could survey everything happening inside the pavilion as easily as looking down at my palm, Hong Jin was still fiercely wary of leaving Prince Shangshan alone.

“Young Master Jin, do you think it’s all right?”

“There’s no need to worry. I’m nearby, and more importantly, I left that rascal Mujin with His Highness as a precaution.”

“Right. That’s why I’m even more uneasy.”

“……”

Thank goodness Hyuk Mujin hadn’t heard that. I stepped into an empty room.

As befitted a pavilion belonging to the imperial palace, it was spacious, and a faint fragrance drifted among the antique furnishings.

*The best part is, there’s no chance of anyone bugging us.*

Back in the modern world, whenever I had an important conversation, I worried that someone might be listening in. Murim was old-fashioned, so I could talk without a care.

“Finally, I can breathe a little. Don’t you think?”

Hong Jin seemed to have had much the same thought. He brought a lit candelabra to the window to brighten the dark room, then sat down and spoke, looking tired.

“I’m sure you have a lot you want to ask me, Young Master Jin, but could I speak first?”

“Go ahead.”

“Don’t provoke him more than necessary. Whatever you do.”

He hadn’t said exactly who he meant, but I immediately knew who Hong Jin was talking about.

“Baek Yeon?”

“That’s right. Baek Yeon, Commander of the Embroidered Uniform Guard. It’s best to keep your distance from him.”

I didn’t ask why.

There was no need.

He was the head of the Embroidered Uniform Guard and an exceptionally skilled Supreme Peak master. On top of that, he was the military officer most trusted by the Son of Heaven.

Any one of those would be reason enough for caution. All three together left nothing to discuss.

But…

“I think that distance has already gotten pretty short.”

Hong Jin sighed at my answer.

“I know. I saw everything with my own two eyes. I’m just saying you should be careful from now on.”

His concern came through in his expression, his voice, even the way he spoke.

The Hong Jin I knew wasn’t lacking in nerve. The East Depot, made up of eunuchs, was a ruthless organization that acted as the Emperor’s human-cleanup crew alongside the Embroidered Uniform Guard.

Judging by the fact that he’d held a fairly high position there, he must have been through all sorts of hell. In fact, when dealing with Jeong Hogun and the other guards, or the East Depot eunuchs, he’d even shown open contempt.

That is, until Baek Yeon appeared.

“Is there another reason I don’t know about?”

The moment I heard Hong Jin’s answer, I understood his concern.

“Thirty thousand. That’s how many people Baek Yeon had arrested and killed in the last coup.”

“……!”

“How did the fourth prince, already sidelined in the struggle for succession, manage to seize the throne of a Great Nation? Just because he was exceptionally capable? No. That wouldn’t have been enough. He needed a cause, and he needed people. No one can become the Son of Heaven by their own strength alone.”

Hong Jin spoke rapidly, then took the long-stemmed tobacco pipe from inside his clothes and put it to his mouth.

Before long, smoke rose with a pungent smell. Hong Jin continued, his face looking especially dark through the haze.

“Baek Yeon was already head of the Embroidered Uniform Guard long before I entered the imperial palace. He had the late Emperor’s full trust from a young age, and at one point he even taught the Crown Prince martial arts.”

“The Crown Prince—you mean the one…?”

“That’s right. So when Baek Yeon helped the fourth prince stage a coup, everyone was stunned. No one thought he’d betray the late Emperor and the Crown Prince—not him.”

*Hoooo.*

Smoke curled up from Hong Jin’s lips. Through it, the past he remembered seemed to drift before us like a pale fog.

“Everything began in an instant and ended just as quickly. The coup was so secretive that even the East Depot couldn’t do a thing. No—maybe it’s more accurate to say we were caught off guard because we never saw it coming.”

The coup began in the dead of night and was over around dawn.

The pounding of hooves echoed across the imperial capital until daybreak, and the screams never stopped.

“The coup was… perfect enough to make your skin crawl. Every civil and military official had gathered to celebrate His Majesty the Emperor’s birthday, along with members of the imperial family from every corner of the land. Security was tighter than ever, in case anything happened. Except for one thing.”

It wasn’t the birthday of some village headman, but of the Emperor, ruler of an entire continent.

I could almost see it all before me: the packed crowds that day, and the dazzling golden armor of the guards who had sealed off the imperial palace.

“……The Embroidered Uniform Guard. They were in charge of the palace defenses.”

Hong Jin gave a bitter smile and nodded.

“Yes. That’s right.”

Everything had been prepared down to the last detail.

Baek Yeon and the guards who followed him took control of the imperial palace in an instant. As everyone looked on in shock, the fourth prince alone rose to his feet and stepped onto the stage prepared for him, his expression calm.

It was the moment the history of the Great Nation changed.

“And then… the purge began.”

The unexpected spectacle was over, but no one left their seats. No—no one could.

The people who had arrived as nothing more than spectators were forced to become actors in the next performance.

“Those who submitted at once survived. Those who resisted were dragged off to the prisons controlled by the Embroidered Uniform Guard. The imperial family had it a little better, at least. At first, they were only confined.”

The Emperor—no, the late Emperor—was already old. He was locked inside his residence. The Crown Prince and his wife, and the rest of the imperial family, were no exception.

They endured day after day under relentless watch, trembling at the screams that rang out day and night beyond the high walls surrounding them.

Waiting for their turn to come.

“Countless people died in the process. More families than anyone could count were destroyed. And…”

Hong Jin let his voice trail off, then added,

“The man who led the purge was the Commander of the Embroidered Uniform Guard. No—the Blood Envoy, Baek Yeon.”

“The Blood Envoy…”

“I’ve always thought that sobriquet suits him rather well. Don’t you?”

Hong Jin curled his lips into a smile, but it was feeble and vanished without a trace almost immediately.

“Young Master Jin. Back then, I couldn’t do anything. I was incompetent as a subject: I failed to detect the treason. And I was powerless: all I could do was watch it happen. But there’s one thing that hasn’t changed, then or now.”

*Tap.*

Hong Jin knocked the ash from his pipe and continued.

He looked up as if trying to see through the ceiling, beyond which the young prince was sleeping peacefully.

“I must protect His Highness Prince Shangshan. It’s the late Emperor’s final wish, and the last act of loyalty from a servant who was both incompetent and powerless.”

His smooth, flowing voice came to a halt.

Turning over what I’d just heard in my mind, I suddenly spoke.

“I’m not sure that’s really loyalty.”

“Hmm?”

“Wanting to protect your lord and wanting to protect a child as a parent are two very different things. And from what I’ve seen of you, Deputy Military Commissioner, I’d say the latter is closer.”

“What are you trying to say?”

“It’s simple. His Highness Prince Shangshan isn’t just a child who needs someone to protect him.”

Hong Jin sighed at my words.

“Young Master Jin, I’m sorry, but he’s still young. He’s only thirteen.”

“That’s right. Only thirteen—and already able to make the Commander of the Embroidered Uniform Guard, a man whose influence could knock birds from the sky, bow his head. Already able to keep his composure while people die right in front of him.”

“……!”

Sometimes. Maybe even fairly often.

People caught up in their personal feelings make the wrong call.

*Even if that person is a eunuch from the East Depot who’s been through hell and back.*

I held Hong Jin’s frozen gaze and continued,

“His Highness Prince Shangshan isn’t a child who needs someone else to protect him. He’s been a king for a long time already. He just hasn’t fully come into his own yet.”

“Young Master Jin, you…”

“If all he wanted was to survive, he could throw himself at the Emperor’s feet as soon as tomorrow and beg for his life. He could plead, ‘I don’t have the faintest idea what crime I’ve committed, but please spare me just this once.’ Assuming, of course, that his desperate plea manages to stir the Emperor’s tender heart.”

“……!”

“But you have something else in mind, don’t you, Deputy Military Commissioner?”

Hong Jin stared at me, his face set, then asked in a dry voice,

“What makes you think that?”

“At a time when you should be bending over backward to please the Emperor, you dared to bring martial-world ruffians into the imperial palace. You dared to taunt the East Depot and the Embroidered Uniform Guard. And…”

I suddenly turned around and continued slowly,

“On this dark night, you brought an uninvited guest all the way here, past the eyes of the Embroidered Uniform Guard.”

At that moment—

*Fwoosh. Whoosh.*

The three candles Hong Jin had lit as soon as he entered the room went out all at once.

I looked back and forth between Hong Jin and the black figure that had appeared out of thin air, then spoke.

“So, when are you going to introduce us?”

[^1]: *Changwei* is a collective term for the imperial court’s East Depot and Embroidered Uniform Guard.
## Chapter artifact 866

# Chapter 866

Having an uninvited guest show up at night is never a welcome situation.

Even less so when he’s a Supreme Peak master skilled in extraordinary concealment techniques.

“Young Master Jin, I know it’s late, but let me introduce you. This is…”

“No need. Since I’ve barged in without permission, the least I can do is introduce myself.”

*Slide.*

The uninvited guest interrupted Hong Jin and lowered his mask, revealing a smooth, clean-shaven face.

His build was so androgynous it was hard to guess his gender, and he looked a good ten years younger than Hong Jin.

On top of that, his personal martial prowess had reached Supreme Peak.

Put all those clues together, and it wasn’t hard to guess who the uninvited guest was.

“The East Depot?”

The guest nodded.

“You’ve got a sharp eye.”

As if barging in uninvited weren’t enough, he was addressing me casually, too.

I didn’t like it, but in a way, it made things easier.

I could just do the same.

“Well, if I couldn’t figure out something this obvious, I’d be better off going out and dying.”

“And you don’t mince words, either.”

“Is it only my mouth that doesn’t mince words?”

“Good. Very good.”

The uninvited guest smiled without making a sound, then clasped his hands in a formal salute.

“Allow me to introduce myself properly. I’m Ma Sanbao, Brush-Holding Eunuch of the East Depot.”

Brush-Holding Eunuch of the East Depot? Ma Sanbao?

Judging by the office, it sounded like a high-ranking position. But his name sounded like something you’d call the kid next door: Dogshit.

At the questioning look in my eyes, Hong Jin spoke up.

“The Brush-Holding Eunuch is the East Depot’s second-in-command. In terms of rank, he comes right after the Chief Eunuch.”

I stared at the uninvited guest—or rather, Ma Sanbao—with wide eyes.

His position was more impressive than I’d imagined, but I was even more curious why a big shot like the East Depot’s second-in-command had come here in secret at this late hour.

Especially after seeing for myself how that old eunuch had treated Hong Jin earlier.

“Hadn’t you already fallen out with the East Depot? Judging by what happened earlier, you two didn’t exactly seem to get along.”

Ma Sanbao laughed again at my question to Hong Jin.

“You’re certainly no ordinary young man. To bring that up so casually right in front of me…”

“I wasn’t asking you.”

“That doesn’t matter. I’m just glad it looked that way. If even our own side was fooled, the Embroidered Uniform Guard certainly won’t suspect a thing.”

Fooled?

I paused at his suggestive remark and looked at Hong Jin.

“……So it was an act? The whole thing?”

“To be precise, I did intend it from the start. But I wouldn’t call it an act. He’s disliked me for a long time.”

Hong Jin answered, and Ma Sanbao nodded.

“Mm. It’s been a long time, all right. If I remember correctly, it’s been over thirty years.”

“You picked a good man, Ma Constable. Or should I call you Eunuch now?”

“My, you’ve gotten even more mischievous since I last saw you. A man like me would never have dared dream of such a position. I was only holding yours for a while.”

“Not at all.”

Hong Jin answered firmly, then continued.

“You’re more than qualified to sit in that position. You were back then, and you still are now.”

“……Good grief. Come to think of it, I forgot to greet you.”

Ma Sanbao shook his head and patted Hong Jin on the shoulder, his face half bitter and half glad to see him.

“Even if the timing couldn’t be worse, I’m glad to see you again, even like this.”

“Likewise.”

Watching two men without balls have an emotional reunion, I felt hot tears begin to run down my face—

No, I didn’t.

An emotional reunion, my ass.

They hadn’t even filled me in on what was going on. Why the hell would I be crying?

Still, even I had to admit that the sight of Ma Sanbao and Hong Jin holding each other by the shoulders was pretty heartwarming.

And that was aside from the sentiment. Ma Sanbao was the East Depot’s second-in-command.

Besides, the meaning behind their conversation so far was definitely not a bad one.

*A secret pact.*

There was no doubt they’d arranged all of this beforehand. I just didn’t know where it had begun, or where it would end.

And my wait for an explanation ended sooner than I expected.

The two men finished their brief reunion and took turns speaking.

“Eunuch Ma and I are from the same cohort. We first set foot in the imperial palace on the same day.”

“And got cut on the same day, too. Do you remember? You were right before me in line.”

“Was I?”

“I remember it clearly. You didn’t let out a single scream. I thought you were one tough bastard.”

I’d been listening to them talk, and now I asked with a queasy look on my face.

My tone was a little more polite than before.

“Um, when you say you were both cut on the same day…”

“What do you think? That.”

“That’s right. That.”

“……Oh.”

I’d suspected as much, but was this for real?

*Ball-cutting buddies.*

Was this what made the imperial palace so amazing?

Childhood friends, coworkers who’d joined on the same day—they didn’t even come close.

And since they’d been cut and entered the palace together, their bond must have been on an entirely different level.

“We joined the East Depot around the same time and rose through the ranks together.”

“That sounds about right. Except you were always one step ahead of me.”

“That was true at times. But the Director always trusted you the most, Eunuch Ma. And when it came to martial arts talent, no one in the East Depot could match you—not just me.”

I didn’t know how much of their conversation was true, but it suddenly struck me that Hong Jin’s assessment of Ma Sanbao’s martial arts was probably not exaggerated in the slightest.

The energy I’d sensed from Ma Sanbao the moment I saw him was in no way inferior to mine or Baek Yeon’s.

*Of course, internal energy isn’t everything.*

I muttered to myself and looked Ma Sanbao over from head to toe.

His overall height and the length of his limbs. Which muscles were especially developed, and what kind of weapon he looked like he might use.

At this point, it was practically a mental disorder—an occupational hazard. But getting a read on the person in front of me was an important habit.

Provided it didn’t needlessly offend them.

“Young man, you’ve got a remarkably keen eye.”

At Ma Sanbao’s sudden remark, I answered, inwardly clicking my tongue.

“I was about to say the same about you.”

“What, surprised I noticed so quickly?”

“Mm. A little.”

“It’s an old habit. I may not be a Murim martial artist like you, but I have to stay alert, wherever I am.”

I’d examined him as discreetly as possible, in a fraction of a second—too quickly for him to have noticed.

And yet Ma Sanbao had caught on while talking with Hong Jin. That meant his Qi Sense was better than that of most Supreme Peak masters.

*So this is the East Depot.*

The East Depot and the Embroidered Uniform Guard.

I’d already heard what these two organizations, collectively known as the Changwei, did.

Assassinations of key figures. Surveillance, intelligence gathering, and so on.

They were intelligence agents trained to the limit, skilled assassins, and soldiers.

And with the Son of Heaven’s dazzling authority behind them, I’d heard they also served as a law enforcement agency.

Their influence and strength must be immense.

*Even the low-ranking Embroidered Uniform Guard and East Depot eunuchs I’ve seen so far were no ordinary people.*

“No ordinary” didn’t even begin to cover it.

Even the weakest were Supreme First Rate, and more than half were Peak masters.

On the way to the imperial palace, I’d seen hundreds of Peak masters with my own eyes.

And if that was only a fraction of their numbers, the strength they hadn’t yet revealed was truly terrifying.

*And if an imperial palace like this were to join hands with Dark Heaven—if, by some chance, it really came to that…*

A cold shiver ran up my spine. My face, reflected in Ma Sanbao’s eyes, had stiffened without me noticing.

“You’re wary of me.”

“Let’s call it a question mark, not wariness. For now.”

“For now?”

“I don’t need you to tell me you two are close. What I want to know is that there still seem to be a lot of facts I haven’t heard.”

“Yes, I suppose so.”

Ma Sanbao dropped into an empty chair and continued.

“How much do I need to tell you to clear up your questions?”

“Everything. From beginning to end.”

“Everything would be difficult. It’s far too long a story to finish here today. But I’ll tell you one thing first.”

“Let’s hear that, then.”

“About a month ago, I sent a secret letter to someone. It contained information that some members of the Embroidered Uniform Guard were heading north while concealing their identities, along with my personal suspicion that their destination was Shanxi Province.”

Hong Jin quietly picked up where Ma Sanbao left off.

“Thanks to the information Eunuch Ma gave me, I had some time to prepare, even if it wasn’t much. Asking Young Master Jin for help was a decision I made after thinking it through carefully.”

“……!”

This was the first I’d heard of it, too.

I’d thought Hong Jin had chosen me simply because he was desperate and had no one else he could turn to.

But that wasn’t it.

Hong Jin had thought it through carefully and asked me for help.

And somewhere along the way, someone had been lending a hand behind the scenes.

No matter how capable Hong Jin was, there was no way he could keep track of everything happening in the imperial capital, over ten thousand *ri* away.

*But the East Depot’s second-in-command could manage it.*

The East Depot had spies planted all over the land, watching for all sorts of developments. And if it was something happening in the imperial capital—practically its own front yard—there was no need to explain further.

That alone didn’t answer all my questions, though.

“I understand that you helped save His Highness Prince Shangshan. But…”

“I think I know what you’re about to say. Yes, you’re right. I’ve already sworn my loyalty to His Majesty.”

Just as I was about to continue, Ma Sanbao spoke first, then added in a low voice,

“Not the traitor sitting on the throne now. The late Emperor.”

“……!”

“Do you know why, and how, I’ve remained in the imperial palace all this time?”

*Tap. Tap.*

Drops of blood fell one by one through the gaps in his whitened fist. The East Depot’s second-in-command continued in a strained voice I’d never heard from him before.

“Because there was something I had to do. Because I had to endure whatever hardships came and wait for my moment……!”

The cry he couldn’t let out at full volume struck the barrier of my internal energy surrounding us and faded away.

Ma Sanbao’s lips quivered as he revealed emotions he’d kept hidden for over a decade.

Then he looked at his longtime friend and spoke in a voice boiling with feeling.

“Hong Jin. Hong Constable. My friend and comrade. The time has finally come. We can’t put it off any longer.”

“Eunuch Ma. Don’t tell me…”

“That’s right.”

*Rumble.*

A thunderous boom suddenly rang out, and the dark sky was flooded with blinding light. With the rain and lightning pouring beyond the window behind him, Ma Sanbao muttered as if spitting the words out.

“Let’s set right, with our own hands, the sky that traitor has thrown into chaos.”
## Chapter artifact 867

# Chapter 867

*Rumble.*

Thunder rolled across the sky. As dazzling lightning flashed and torrential rain came pouring down, the palace attendants hurried about.

Eunuchs and palace maids scurried toward the quarters of the consorts they served, worried that rain might be leaking in somewhere. The Embroidered Uniform Guards stationed throughout the imperial palace stood their ground beneath their broad-brimmed hats.

Everyone who worked in the imperial palace had a role to play.

Do your job well, and you were rewarded. Fail to, and you were punished.

And in the relentless downpour, one man strolled at his leisure. He was one of the few people in this vast imperial palace who needn’t concern himself with rewards or punishments.

No—in fact, it was closer to the opposite.

He wielded such immense authority that he could reward or punish others without the Son of Heaven’s approval.

Yet not one palace attendant dared try to catch his eye or get close to him.

Not even the rain pouring ceaselessly down at that very moment.

*Whoosh.*

Though he walked through the downpour, not a drop of water touched the man.

His half-white hair, tousled as it pleased, was bone-dry. His golden armor, polished with oil-treated cloth, still gleamed brilliantly.

It was a strange, almost unreal sight, but the man was different.

After all, immense authority wasn’t all he possessed.

Raw power.

Martial prowess far beyond the limits of human ability.

He had the strength to make the unreal real. And with an important meeting ahead of him, he simply didn’t want to get wet.

*Vwoom.*

The air trembled before his profound internal energy. The rain struck an invisible barrier and ricocheted away in every direction, unable to touch him.

“It’s been quiet lately, but now it’s really coming down…”

Muttering as he looked up at the sky flashing with lightning, the man resumed his steps. No one dared stand in his way.

They hadn’t in the past. They didn’t now. And they never would.

*Clank. Rumble.*

The mere sight of the man approaching from afar was enough.

The Embroidered Uniform Guards peered out from beneath their deeply lowered hats. Without a moment’s hesitation, they opened the firmly shut gates and kept their heads bowed until he had passed.

The same was true of those quietly performing their duties out of sight.

“Open the way.”

At the man’s sudden command, the vast garden, filled with all manner of rare flowers and plants, shimmered like a heat haze.

*Whoosh.*

Even the foreign trees and flowers that had stood tall against the fierce rain and wind lowered their heads.

Thick leaves and branches stirred aside, revealing a hidden path where only those granted permission could set foot.

Beautiful flowers have thorns.

The imperial palace’s gardens were no different. An unwelcome guest who was fooled by their appearance and stepped inside recklessly would be surrounded by countless mechanisms and formations and riddled like a beehive.

And it wasn’t just the gardens.

The imperial palace itself was a den of countless dangers, a demon-slaying battleground and a mountain of sabers and a forest of swords in the truest sense.

Anyone without permission would die.

Even someone whose martial prowess reached the heavens could never be sure they would survive.

As the man passed through five gates and dozens of pavilions, he was reminded of that once more. At last, he reached his destination and stopped.

Qianqing Palace.

Beneath the signboard, its characters written in a bold, soaring hand, two middle-aged men stood like iron towers. They lowered their heads in greeting.

“You’ve arrived.”

“You’ve arrived.”

Their voices and expressions were as alike as if they were one person.

And their features were so strikingly similar that anyone would know they had been born of the same womb on the same day.

The twins continued, speaking politely to the man.

“Please wait a moment.”

“Please wait a moment.”

The man frowned. It wasn’t because he disliked the twins speaking in unison, despite his countless reminders not to. It was the strong smell of blood coming from them.

“Looks like you had a guest.”

“Yes.”

“Yes.”

“Did you kill him? Who was behind it?”

“He took his own life just before we could capture him.”

“He took his own life just before—”

“Enough. How many times have I told you that once is enough? So you failed to take the intruder alive?”

The twins blinked at him, looking unsure what to do, then mumbled under their breath.

“He had hidden a potent poison beneath one of his molars.”

“He had hidden a potent poison—no, we did everything we could, but we couldn’t stop him. We beg your forgiveness.”

The man clicked his tongue softly.

The fact that the intruder had made it this far was proof of his extraordinary martial prowess.

Failing to capture him and discover who was behind him was a painful mistake, but there was something more important than reprimanding the twins right now.

“Don’t tell me he got inside the palace.”

“Of course not.”

“Of course not.”

At least that was a relief, the man thought to himself, then asked another question.

“Is he inside?”

“He’s waiting.”

“He’s waiting.”

The man nodded, glanced up at the signboard above him, then stepped forward.

Qianqing Palace. Qianqing—“clear sky.” He couldn’t help thinking that those two characters were a poor fit for a day like this.

*Step. Step.*

The palace interior was quiet.

Not a person—or even a rat—could be seen. Only the countless paintings and works of art hanging on the walls glimmered in the faint light.

But there was more than met the eye.

With every step, the man felt eyes following him. Shadows poised to rush in and tear him apart the moment they sensed even the slightest threat, whoever he might be.

At the end of his path, he came to a stop. A vast space had been prepared for one person alone, and its master was waiting.

No—the master of all under heaven.

“I, Baek Yeon, Commander of the Embroidered Uniform Guard, have come at the summons of Your Majesty, the august Emperor.”

At that moment—

*Rustle.*

The colorful silk curtains draped around the room stirred.

Amid the smoke rising here and there, carrying a faint fragrance, the back of a figure dressed in dazzling white showed through the thin curtains.

“You’ve come.”

A quiet voice reverberated through the room. At first, it sounded calm and languid.

The Son of Heaven of the Great Nation continued slowly, as if speaking to himself.

“I had a bad dream. A dream that someone was trying to harm me.”

“……!”

“I fought for a long time, drenched in blood. They kept coming from somewhere, without end, and I kept cutting them down. Only when I finally woke did I realize it hadn’t been some idle dream.”

Baek Yeon raised his head in silence and looked at the pale smoke drifting from between the Son of Heaven’s lips.

“So you’ve turned to opium again.”

“Does this look like opium to you?”

“Forgive me, but that is exactly what it looks like to me.”

“You’re wrong. This isn’t opium. It’s medicine—the only thing that can heal me.”

At that, Baek Yeon’s brow twitched.

“Your Majesty, may I speak with you about something important?”

The Son of Heaven didn’t answer. Instead, he flicked his long, wide sleeve.

*Swish.*

With a faint rustle, the presences surrounding them withdrew like the tide. Baek Yeon straightened from his bow, his voice turning cold.

“Your Majesty, with the great undertaking nearly complete, why would you disgrace yourself like this?”

If anyone else had been there, they would have covered their eyes and ears.

Baek Yeon’s tone was far too sharp for a subject speaking to his ruler. It was more than insolent—it was defiant.

Yet the Son of Heaven didn’t answer this time, either. The ruler of the world gave a low laugh instead. Only after a long while did he suddenly speak.

“The great undertaking. Yes. There was a great undertaking.”

“Please don’t forget the promise from that day.”

“Forget?”

The Son of Heaven muttered with a short, incredulous laugh.

“I haven’t forgotten. I haven’t forgotten for even a moment since that day.”

His voice was as weak as that of a sick man.

But Baek Yeon’s eyes, fixed on the Son of Heaven, didn’t waver. They were sunk deep and steady.

“They’ve already begun to move. Before everything falls apart, remember that you must put things back where they belong.”

After a brief silence, the Son of Heaven nodded quietly.

It was already too late to turn back. He had been no more than the fourth prince, but now he ruled all under heaven. He had become a man who couldn’t help but rely on opium.

Did they say that a horse racing across the wilderness never looked back?

Even the Son of Heaven, who stood above all people, was no exception.

He was a horse. A horse that could no longer stop of its own will, that had to keep running toward its destination even if it collapsed, coughing up blood.

*Crack.*

His hand clenched instinctively, snapping the ornate long-stemmed tobacco pipe. The Son of Heaven stared at the broken pieces in his palm, then closed his fist tightly around them.

*Thump.*

The rough sensation digging into his palm. A pain like a burn. And, little by little, his mind began to clear.

“Ah.”

As if worshiping the heavens, the Son of Heaven tilted his head back toward the ceiling and groaned with his eyes closed.

Baek Yeon watched impassively.

“Shall I call for the imperial physician?”

“No need. Not for an imperial physician.”

The Son of Heaven opened his eyes and continued, his voice clearer now.

“Tomorrow, I’ll meet that child in the audience hall.”

“That child would be…”

“Zhu Bao. I wonder how much my… only younger brother has grown.”

Baek Yeon nodded.

“You can look forward to it. He’s grown even more than Your Majesty expects.”

“Which means he’s become even more dangerous.”

“……”

Baek Yeon pressed his lips together, but the Son of Heaven understood what that meant.

Wherever there’s a delicious meal, all sorts of bugs gather.

Now that Prince Shangshan Zhu Bao had appeared in the imperial capital, his enemies—those who resented him—would surely draw the blades they’d kept hidden beneath their sleeves.

Just like the nameless assassin who had come here before Baek Yeon today.

“Baek Yeon, this must never happen again. Remember that.”

The voice was different now, cold as ice. Baek Yeon hesitated, then answered with a faint smile.

“I will engrave Your Majesty’s words into my bones. Please forgive my disloyalty until now.”

*Flutter.*

In response, the Son of Heaven merely waved his sleeve. Baek Yeon turned and began walking away.

After only a few steps, he stopped.

“And what of that man?”

“If you mean…”

“Zhu Bao. The Murim martial artist who came with him.”

The Blazing Flame Divine Dragon, Jin Taekyung.

Baek Yeon thought carefully about the man who had suddenly come to mind. A long while passed before he spoke.

“I don’t know.”

He had interrogated and killed tens of thousands on the battlefield, and tens of thousands more in the imperial palace.

But that was the best answer Baek Yeon could give.
## Chapter artifact 868

# Chapter 868

The night Ma Sanbao came to see me.

I couldn’t sleep for a long time.

It wasn’t just because of the rain pouring down like the heavens had made up their minds to unleash it, or the lightning striking all around us.

The last conversation I’d had with Ma Sanbao kept replaying in my head. He’d vanished as suddenly as he had appeared.

*I need your help.*

When Ma Sanbao first said those words, I couldn’t give him an answer.

This was an undeniable plot against the throne.

If I agreed, and things went wrong, no one could say what would happen next.

With the imperial family involved, this couldn’t be dismissed as one person’s wrongdoing.

The thought that I wouldn’t pay the price for failure as the Blazing Flame Divine Dragon Jin Taekyung, but as Jin Taekyung of the Jin Family of Taiyuan, weighed heavily on me.

*What happens if this fails?*

*You already know, don’t you?*

*……*

*Fail, and you’re a traitor. Succeed, and you’re the Son of Heaven. If you succeed, unimaginable wealth and glory await you—things no one else in the world could enjoy. But if you fail, you’ll suffer a pain worse than hell.*

I’d fought countless battles and brought down more enemies than I could count.

Some had been so weak I could take them on with one finger. Others had been so terrifying I could barely move a finger against them.

But…… this was different.

The Great Nation was the master of the world, and the Son of Heaven was the master of the Great Nation.

To rebel against that very Son of Heaven meant fighting the world itself.

Me—and everyone around me.

*Think carefully. Of course, since you set foot in the imperial palace to protect His Highness Prince Shangshan, it may already be too late for you.*

*Are you threatening me?*

*No. I’m telling you the truth.*

Ma Sanbao. The East Depot’s second-in-command. The cold, piercing gaze he’d fixed on me was still vivid before my eyes. So was his deep, sunken voice.

*How many people do you think died in the coup? Tens of thousands were executed by poison, died for unknown reasons on the way to exile, were torn limb from limb in the marketplace, or had their heads displayed. That’s only the number the world knows about. How many deaths were never brought to light? And how many of them had nothing to do with it, like you?*

*……!*

*They call it “calling a deer a horse.”[^1] In the end, everything depends on the Emperor’s will. Just as a perfectly ordinary deer can become a horse, you, too, can be made a traitor. Keep that in mind.*

History had proven the fickleness and suspicion of those in power.

And the current Son of Heaven was a tyrant no one in the world could deny. A usurper who had defied the natural order and waded through blood to claim the throne, a ruler wielding absolute power.

So the moment I heard Ma Sanbao’s words, I understood, if only vaguely:

Whether I became a traitor might already be out of my hands.

*Of course, I won’t deny that I helped bring about their deaths. No—I led the way. I had to survive, no matter what it took. I had to remain here, of all places, and wait for the right moment.*

Some had left the imperial palace to serve their young master. Others had remained there to welcome him when he returned one day.

Hong Jin had been the former. Ma Sanbao was the latter.

He became the fourth prince’s—no, the new Emperor’s—hunting dog.

He was one of the cruelest of them, sinking his teeth into his targets’ necks without mercy. He survived that brutal purge and rose to become the East Depot’s second-in-command, its Brush-Holding Eunuch.

And Ma Sanbao wasn’t the only one who survived that way.

*That night, when we all gathered, the Director said that if the East Depot had been a flower blooming in the dark until then, from that point on we had to become weeds.*

Flowers were colorful and beautiful, whether they bloomed in the light or the dark.

Weeds weren’t. No one paid any attention to plain, nameless grass.

And because of that, it survived longer.

The Director, the East Depot’s head and its Seal-Holding Eunuch, had urged his like-minded comrades to survive by becoming weeds like that.

Until he finally fell, unable to overcome the illness that came with his long years.

*Five years ago, after the Director took to his sickbed, I began leading everyone. That was when I started drawing up the blood-signed pact.*

The pact.

Clear proof that the traitors had signed their names in their own blood—and perhaps a record of the names of the meritorious officials who would one day enthrone a new Son of Heaven.

Ma Sanbao mentioned the pact, then left.

And with one last remark that could only keep me up all night.

*Dark Heaven. I know about the people currently throwing Murim into turmoil. Probably far more deeply and thoroughly than you suspect.*

*……!*

*Even if you leave now, I won’t go out of my way to stop you. But if you help us enthrone His Highness Prince Shangshan and set a new order in place…… we’ll have to give you an appropriate reward.*

Ma Sanbao left. Hong Jin returned to the young prince’s side, and I stayed where I was, lost in thought.

Until the first light of dawn reached the window.

Until the rain slowly began to let up and day broke in the distance.

And until this very moment.

“Fuck.”

At my sudden curse, Hyuk Mujin, who’d been nodding off in a corner, jolted awake. He leaped to his feet and fumbled for the sword in his arms, eyes half shut.

“Are we under attack? An attack? You bastards! How dare you—”

“Mujin.”

“Yes?”

“Go to sleep.”

“Yes.”

Hyuk Mujin flopped back down as if nothing had happened and fell asleep again in no time.

The trip all the way to the imperial capital must have been exhausting, but sleeping for four whole *shichen* in that position was a talent in itself.

*Snore.*

“……”

Even so, snoring was crossing the line.

*Whack!*

“Ugh! You bastards! No one lays a finger on the Captain!”

“Mujin.”

“Yes?”

“If my bodyguard sleeps that soundly, they could lay hands on every part of me but a single hair.”

“Gasp! Someone’s already laid a hand on the Captain? No, you don’t even have to tell me. It was Hong Jin, wasn’t it? I knew it. The way he looked at you was lecherous from the start……”

“Mujin. You little shit……!”

I let out a groan that came from the depths of my soul.

Of all people, this idiot was my right-hand man—or rather, my pinky toe.

Things were serious enough as it was, and with him like this, I’d hit a proper moment of clarity. At this point, I was starting to wonder if Dark Heaven had sent him as an ascension-to-immortality hitman to make sure I left this world early.

*No System, and no one I can rely on right now.*

Thinking about it, I’d been pretty lucky until now.

The System had always pointed me toward where I needed to go, even if it did so vaguely through Quests. And whenever I wavered, Jeok Cheongang had been a sturdy pillar I could trust and lean on.

But now I had neither.

Everything that happened from here on would depend solely on the choices I made.

*Fail, and you’re a traitor. Succeed, and you’re the Son of Heaven.*

Ma Sanbao’s words circled in my ears like an echo. His final remark came with them.

*Dark Heaven. I know about the people currently throwing Murim into turmoil. Probably far more deeply and thoroughly than you suspect.*

What exactly did he know, and how had he learned so much? What connection did the information he’d uncovered about Dark Heaven have to the Son of Heaven—and how dangerous was it?

I’d wanted to stop Ma Sanbao, who seemed determined to leave, and press him for more answers. But I held back, imagining the Embroidered Uniform Guard receiving a Buster Call and rushing over the moment I caused a commotion.

No—or maybe I’d let him go because I was weighing the significance of what he’d said next.

*Reward. A reward……*

I quietly turned the word over in my mind.

Ma Sanbao had said it plainly. If I helped them enthrone Prince Shangshan as the new Son of Heaven, they would give me a fitting reward.

And given that he’d mentioned Dark Heaven just before, it wasn’t hard to guess what kind of reward he meant.

*The imperial family—the Great Nation—helps the Murim Alliance wipe out Dark Heaven.*

There was a reason people said the government and Murim must never interfere with one another. The Great Nation had never involved itself deeply in Murim’s affairs.

No, thinking about it now, the reason was obvious.

*There was no reason for them to get involved.*

There was no need to count the forces across the entire world. A million elite troops were stationed near the imperial capital alone, and I’d seen hundreds of Peak masters with my own eyes.

And if you included the forces that hadn’t yet come to light—especially the Supreme Peak masters……

*The imperial capital alone already dwarfs the Murim Alliance in strength.*

Of course, it was undeniable that most of the Great Nation’s forces were concentrated in the imperial capital.

All the wars, including invasions by foreign tribes, had ended long ago. The emperors of the unified dynasty had never given the lords and vassal princes scattered across the land more military power than necessary.

They had simply watched everything from atop these enormous, impregnable walls.

They watched the fierce struggle for power taking place in another enclosure within the Great Nation’s borders—the one people called Murim.

That had been true even during the Great Faction War.

*But if the Great Nation itself took the Murim Alliance’s side……*

The scales of victory would tip in an instant.

Until now, the fight had been between the Central Plains’ Murim and Dark Heaven. If the Great Nation joined in, Dark Heaven would become an external enemy hated by all under heaven.

I still couldn’t gauge how powerful Dark Heaven’s forces were, since so much remained hidden. But the weight carried by the two words “Great Nation” was just as heavy—and undeniable.

Of course, there was one fatal problem……

*What if we failed?*

High risk. High reward.

Fail, and you’re a traitor. Succeed, and you’re the Son of Heaven.

It felt like standing at the edge of a cliff.

I could gain the wings of the Son of Heaven and soar above the clouds. Or the Son of Heaven could break both my legs and send me tumbling off the precipice.

And not just me. Everyone.

*Snore.*

“……”

Right. That included this idiot, too.

“……Mujin. You little shit.”

Hyuk Mujin opened his eyes naturally and spoke.

“I wasn’t asleep.”

“Is that so?”

“Yes.”

“Then why was your snoring so damn loud? The Embroidered Uniform Guard will come up and haul you away soon. The Emperor woke up because of your snoring.”

“I’m serious.”

“How are you going to prove it?”

Hyuk Mujin’s eyes rolled around before he answered.

“I’ll stake Hong Jin’s balls.”

“……”

This idiot was trying to stake something that didn’t exist.

I was at a loss for words when I heard a familiar metallic sound outside the window.

*Clack. Clack.*

Orderly movement. A sharp aura.

The Embroidered Uniform Guard.

Hyuk Mujin stared at the golden-armored guards entering the pavilion and asked, wide-eyed,

“Did the Emperor really wake up because of me?”

“……”

Should I really kill him?

I let out a deep sigh, then said,

“Go bring His Highness Prince Shangshan.”

It looked like the time had come.

[^1]: An idiom meaning to deliberately distort the truth or impose a false label.
## Chapter artifact 869

# Chapter 869

After hurrying Hyuk Mujin upstairs, I blocked the Embroidered Uniform Guards who had come to the pavilion at the crack of dawn.

Then I flashed a broad smile at the familiar face that caught my eye first.

“Oh, fancy seeing you again.”

So much for the old saying that nobody spits in a smiling face. It was a complete lie.

Jeong Hogun didn’t so much as twitch an eyebrow, even when I waved at him like an old friend.

“Where is His Highness Prince Shangshan?”

I shrugged. “He was asleep until just now. Before a bunch of rude bastards barged in at the crack of dawn.”

“It is already the hour of the Rabbit. That is by no means early in the imperial palace.”

The hour of the Rabbit meant five to seven in the morning.

I was itching to explain children’s rights to this man, who was built like a Stone Golem, but when in Rome, you did as the Romans did.

Though, of course, it was the Son of Heaven’s will—above every law in the Great Nation—that had set the Embroidered Uniform Guard in motion so early.

“What brings you here?”

“I have no obligation to tell you.”

“Then let me guess. Is it finally time for a family reunion?”

At that, Jeong Hogun reacted. His eyebrow twitched so sharply I could see it from where I stood.

“His Highness Prince Shangshan is to have an audience with His Majesty the Emperor.”

“Right. Four characters: brothers reunited.”

“You’re a lawless thug from the martial world, so it seems you can’t understand. This is not merely a reunion between brothers. It’s…”

“Oh, I get it.”

I nodded with a solemn expression.

“A somewhat complicated reunion of brothers. Right?”

“……”

“Not quite? Too long? How about a chaotic reunion of brothers? One word shorter, but pretty much the same thing.”

Jeong Hogun took a deep breath, as if trying to calm himself, then spoke in a stiff voice.

“……You’d be wise to watch that insolent mouth of yours before you bring down trouble you can’t handle.”

“Whoa, are you warning me? Didn’t you hear your commander promise our prince yesterday that nothing like that would happen?”

“That was…”

“Judging by your face, you just remembered. If you understand, then let’s do better from now on. Don’t go making trouble for no reason. Okay?”

I smiled and patted Jeong Hogun’s armor. Behind him, the killing intent of the Embroidered Uniform Guards standing like iron towers began to rise in waves.

*Whoosh.*

Now, that was some atmosphere.

Maybe I’d gotten under their skin more than I needed to. But in my experience, people like him only showed even a hint of what they were thinking when you provoked them like this.

Just like now.

“You don’t want to cause trouble either, do you? Especially when you’re this tired. Isn’t that right, Jin Taekyung of the Jin Family of Taiyuan?”

“What?”

“You look rather exhausted. As if you didn’t get much sleep last night.”

Anyone with half a brain could tell that Jeong Hogun hadn’t tossed out that remark on a whim.

I looked into his calmly lowered eyes and the blade hidden in them, thinking to myself:

*Well, look at this guy…*

From the very start, he’d given off the strong impression that he knew something.

But the deeper you thought, the longer you stayed silent—and that only gave your opponent more reason to suspect you.

Knowing that, I furrowed my brow and answered,

“You need to feel comfortable to get any sleep. Could you sleep soundly with a bunch of menacing men surrounding you on every side?”

“They are not surrounding you. They are guarding His Highness Prince Shangshan.”

“Does the imperial palace write ‘guard’ but pronounce it ‘surround’?”

“That isn’t worth answering.”

“Then don’t answer. Oh, while we’re on the subject, let me ask you something else…”

I scratched the back of my head and went on.

“In this imperial palace ruled by His August Majesty the Emperor, what exactly are you guarding His Highness from?”

“……!”

“No, the more I think about it, the stranger it gets. If you’re guarding him, there are already soldiers everywhere. I don’t see why the Embroidered Uniform Guard needs to be on this kind of high alert. And if you’re surrounding him, that makes even less sense.”

Checkmate. A perfect one, too.

Either answer would leave him in an awkward position.

If he said they were guarding the prince, then as I’d said, there was no reason for all this. If he said they were surrounding him, that would be as good as admitting that the Embroidered Uniform Guard was monitoring Prince Shangshan on the Son of Heaven’s orders.

And in this essay question where either answer would lead to a dead end, Jeong Hogun chose silence.

Getting under the skin of someone who’d run out of things to say was my specialty.

“I asked you something, but you’ve gone quiet.”

“……”

“If it were Baek Yeon, I bet he’d give me a straight answer. Are you keeping your mouth shut because you haven’t made the rank yet?”

“……”

“People really have to get ahead in life. When’s your next promotion? Do you get annual leave or sick days? If I cause trouble, does that mess up your performance review?”

“……”

“Honestly, you were surprised when your commander suddenly killed one of his subordinates yesterday, weren’t you? Is he always that reckless? I won’t tell anyone, so just whisper it to me. My earlobes are sensitive, so whispering’s a little awkward. Just use Sound Transmission once.”

Thrilling. Always fresh. Getting under someone’s skin was the best.

I had no idea who’d won this year’s Ballon d’Or, but I wasn’t about to miss out on the Mouth d’Or.

I let my tongue run wild, trying to pry out as much information as I could, and needled Jeong Hogun relentlessly.

I started with gossip about his superior, Baek Yeon, then moved on to promotion woes, a working person’s headache. I asked about the Embroidered Uniform Guard’s average salary and overtime pay, then about what kind of hazing culture they had.

In short, I went after everyone but the Emperor.

And Jeong Hogun held out far longer than I’d expected. He finally opened his mouth after I asked whether the Embroidered Uniform Guard’s chow was any good—and then started digging into his family tree.

“That’s enough… Give it a rest.”

I could feel his superhuman patience in the one breath he took between words. I nodded with a touch of respect, then replied,

“So you’re still an unmarried bachelor, then?”

“……!”

“Don’t get me wrong. I’m not criticizing you for being unmarried at your age. I mean, I’m not your parents. And staying single isn’t so bad—you won’t ruin someone else’s life by accident. So don’t let it get you down. Keep your package—no, your shoulders—up…”

“You son of a bitch!”

To be precise, the shout I heard just then didn’t come from Jeong Hogun.

One of the Embroidered Uniform Guards under him, whose face had been changing colors like a seven-hued rainbow for a while now, had finally lost his temper and charged at me.

Or, more accurately, he took one step forward before someone stopped him.

*Thud.*

“Enough. I won’t say it twice.”

With a voice low and heavy, a calloused palm stopped the guard’s golden armor in its tracks. The guard who recognized the hand as belonging to the very superior I’d just insulted shouted in a voice bubbling with rage.

“Thousand Captain! How can you let that bastard—”

*Whack!*

One punch, delivered with a heavy yet swift movement—brief, precise, and ruthlessly efficient.

Jeong Hogun’s fist caught the Embroidered Uniform Guard squarely on the jaw. The man crumpled without even a groan, and I watched him fall with a quiet sound of admiration.

For another reason entirely than the impressive way Jeong Hogun had moved.

“Wow. You really didn’t say it twice.”

“Obeying those above you—that is the law of the military that sustains the Great Nation, and the rule of the Embroidered Uniform Guard.”

Jeong Hogun handed the subordinate he’d knocked out to the other guards, wiped the blood from his hand, and continued.

“The Commander promised no harm would come to you. For this once, I will follow that order as well.”

“For this once?”

“Any order can be withdrawn depending on the circumstances. There are no exceptions.”

His voice was as blunt as ever, but the gaze he fixed on me was bleak and wild, like the storm that had raged through the night.

It was a side of him I hadn’t seen on the way to the imperial capital or after we’d arrived.

A sign that his composure had slipped—and my guess had been right.

“Well, the situation hasn’t changed yet, so I don’t think that order’s been withdrawn.”

“Is that what you think?”

“Of course.”

At my casual reply, Jeong Hogun closed the distance and leaned in to whisper.

“I’m warning you in all seriousness… If you try anything foolish in this imperial palace, where His Majesty the Emperor resides, you will not escape the consequences.”

“Anyone listening would think I’d already pulled something.”

“From the hour of the Ox to the hour of the Tiger. Three red lanterns were lit.”

“What?”

“From what I’ve heard, that was how the East Depot’s secret signals worked. Probably.”

My heart gave a hard thump.

From the hour of the Ox to the hour of the Tiger. Exactly when Ma Sanbao had come to see me.

*And the signal used red lanterns, too.*

It was lucky that Jeong Hogun wasn’t looking me in the eye while whispering in my ear.

Otherwise, he might have noticed the tiniest flicker of a reaction.

But I’d been through a lot by now. I’d learned how to keep my emotions in check.

I quietly and instantly steadied my breathing and pulse, so no one could notice, then gave a short laugh.

“Hong Jin’s crazy about the color red. You can tell by how he paints his lips that color every day, right?”

“Yeah, I can tell. He used to belong to the East Depot, after all. He must have needed to call in someone who could help, even if it meant using such an outdated secret signal.”

Was it suspicion, or certainty?

After countless thoughts flashed through my mind like streaks of lightning, I reached a single conclusion.

*A trap.*

Neither Hong Jin nor Ma Sanbao was careless.

No—in terms of thoroughness, they were easily in the top five of everyone I’d ever met.

The imperial palace, the East Depot—only people like that could survive in places like these.

And if the secret signal was obvious enough for Jeong Hogun to figure out, there was no way they’d risk meeting while using it.

*I can’t take the bait.*

All those judgments came in an instant—so fast it barely seemed like time had passed.

My next move followed just as quickly.

*Tap.*

I pushed Jeong Hogun away from where he stood right up against me, then curled my lips into a smile as naturally as I could.

“Fuck, you’re writing a whole damn novel.”

“……”

“To hell with the East Depot. I don’t know anything about that. I got tangled up in something complicated and spent a while thinking it over. If you really don’t believe me, go ahead and try to frame me.”

No physical evidence. No witnesses.

It was a trap.

Jeong Hogun stared at my eyes, which didn’t waver in the slightest. His answer was practically decided already.

“The night was unusually noisy. A fierce storm and thunder kept roaring without letup.”

“So?”

“It means nothing. That’s all.”

Was the thing in those black eyes a suspicion he still couldn’t let go of?

Or disappointment because his attempt to sound me out had failed?

For once, I couldn’t tell for sure, and I wasn’t given time to try.

“Have you been waiting long?”

*Step. Step.*

Three people came down the stairs, their footsteps accompanied by a familiar, androgynous voice.

Jeong Hogun and the Embroidered Uniform Guards immediately straightened and saluted the young prince, who had just appeared.

“I, Jeong Hogun, Thousand Captain of the Embroidered Uniform Guard, have come to escort His Highness Prince Shangshan.”

Hong Jin, standing behind Prince Shangshan, who wore a tense expression, gave a wry smile.

“You’re still as impatient as ever. No, perhaps I should say you’ve waited longer than expected, since you did manage to hold out for an entire day.”

“Mind your words, Deputy Military Commissioner.”

“How frightening. Then I’ll…”

“You cannot come with us.”

Jeong Hogun cut Hong Jin off coldly, then added something neither of us had expected.

“His Majesty the Emperor summoned only His Highness Prince Shangshan and Jin Taekyung of the Jin Family of Taiyuan. Those two alone.”

What?

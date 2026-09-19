# Checkpoint Review — 435–439

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

# Chapters 435–439

## Plot

Mungyeong’s Slaughter Saint identity remains hidden beneath his medical-apprentice persona as he continues traveling with Jin Taekyung’s group. He discovers that Taekyung has inexplicably opened his Middle Dantian and pressures him for an explanation. Taekyung blames a dream encounter with a white-haired swordsman, whom Mungyeong identifies as Lü Dongbin, but inconsistencies nearly expose the lie. Jeok Cheongang interrupts their confrontation, begins training Taekyung, and rejects Mungyeong’s suspicion that Taekyung used demonic martial arts. Jeok argues that Taekyung’s rapid advancement is beyond ordinary understanding and orders him to avoid Mungyeong.

The group continues toward Hubei, with Mu Song’s forces escorting them after Jeok objects to the length of the ship journey. Taekyung logs out during the voyage and returns to Korea aboard a private jet. Magic Johnson’s translation-magic ring helps the Skeleton King maintain his Stone-King identity, though his fabricated American background, social-media account, and embarrassing message to Magic Johnson create complications. Korea stages a massive official welcome for Taekyung, including a car parade and a presidential greeting at Incheon Airport. Taekyung resists political involvement despite the tax burden associated with his fifty-trillion bounty, but participates in the public ceremony.

## Continuity

- Mungyeong is the former Divine Physician and secretly the Slaughter Saint; his reason for remaining with Taekyung’s group is still unknown even to himself.
- Taekyung’s Middle Dantian opened within roughly half a day, after previously remaining closed. His claim that a white-haired swordsman opened it during a dream is fabricated and remains unverified.
- Jeok Cheongang has begun supervising Taekyung’s training, believes Taekyung broke through the Supreme Peak wall and opened his Middle Dantian in only two years, and has ordered him to avoid Mungyeong.
- Taekyung and the Sword Saint’s Disciple are regarded by Jeok as divine dragons beyond ordinary martial understanding.
- The group is traveling toward Hubei and will spend more than a week in transit, allowing Taekyung to alternate between Murim and the modern world.
- The Skeleton King’s undead nature remains concealed. He presents himself as Stone-King and wants to be addressed as Mr. King.
- Magic Johnson supplied the Skeleton King with a translation-magic ring and Magic Gem-powered smartphone. The Skeleton King’s social-media account has 5,134 followers.
- Taekyung has returned to Korea as its publicly recognized representative S-rank Hunter. The President has publicly greeted him, and Team Leader Choi manages his media and official arrangements.
- The Arch Lich bounty is worth fifty trillion and may create several trillion in Korean taxes. Taekyung intends to pay the taxes rather than seek political favors, and Choi must consult him before making political commitments.
- Jin Wikyung’s withheld confidential matter and the significance of the mysterious patterns and symbols found in both worlds remain unresolved.

## Translation Decisions

- Preserve **Mungyeong** as the former Divine Physician and **Slaughter Saint**, with a polite medical-apprentice voice contrasted against his terse, threatening true persona.
- Use **Middle Dantian**, **Supreme Peak**, **demonic martial arts**, **Sword Immortal Lü Dongbin**, **Chunyangzi**, **Jang Samfeng**, **Bodhidharma**, **sword-riding sorcery**, and **Life-or-Death Crisis**.
- Render **Stone-King** for 스톤 킹 and use **Mr. King** when others address him.
- Preserve the Skeleton King’s grandiose “this king” diction and “vile human” address, alongside Taekyung’s profane, self-mocking modern humor.
- Retain **translation-magic ring**, **Magic Gem**, **Inventory**, **Arch Lich**, **S-rank Hunter**, **Blue House**, **Peace Guild**, and **Demon Realm**.

## Durable state

{
  "active_continuity": [
    "The Skeleton King's undead identity remains concealed from the public, and he has agreed to exercise restraint.",
    "The Skeleton King uses Stone-King as his claimed identity and wants to be addressed as Mr. King.",
    "Magic Johnson supplied the Skeleton King with a translation-magic ring and a Magic Gem-powered smartphone; his social-media account has 5,134 followers.",
    "Jin Taekyung is Korea's publicly recognized representative S-rank Hunter after returning from China.",
    "Tens of thousands gathered at Incheon Airport, where traffic was halted and a military- and police-controlled car parade was prepared.",
    "The President greeted Taekyung and posed with him at the airport photo line.",
    "The fifty-trillion Arch Lich bounty may produce several trillion in Korean taxes, and Taekyung intends to pay them rather than enter politics for tax relief.",
    "Team Leader Choi manages Taekyung's media and official arrangements but must consult him before making political commitments."
  ],
  "continuity_sources": [
    439
  ],
  "open_questions": [
    "Why does Mungyeong continue accompanying Jin Taekyung's group despite being unable to explain the impulse?",
    "How did Jin Taekyung actually open his Middle Dantian?",
    "What confidential matter is Jin Wikyung withholding?",
    "Are Taekyung's suspicions about the mysterious patterns and symbols found in both worlds correct?",
    "How will Taekyung's public status and the Arch Lich bounty affect his future dealings with Korea's political establishment?"
  ],
  "safe_through": 439,
  "temporary_decisions": [
    "Render 스톤 킹 as “Stone-King” and use “Mr. King” when others address him.",
    "Preserve the Skeleton King's grandiose “this king” voice and Taekyung's profane modern humor.",
    "Keep Arch Lich, S-rank Hunter, Magic Gem, Inventory, Blue House, Peace Guild, and Demon Realm as established terms."
  ],
  "version": 1
}

## Reading copies

## Chapter artifact 435

# Chapter 435

Deep night had swallowed even the sunset. A boy sitting at the bow and staring at the blackened river suddenly opened his mouth.

“What brings you here?”

“I came to gaze at the Yangtze while having a drink. I didn’t realize there was already a passenger here.”

Behind the boy, an old man barely five feet tall appeared like a ghost without making a sound. He shook a gourd and grinned.

“Well? Care to join me?”

“Excessive drinking is harmful to the body. You should avoid it.”

“Don’t be like that. Have a drink with me. The atmosphere is nice.”

“I think it would be better if I were left alone.”

“Listen to the way this little brat talks. You haven’t even looked at me while this old man has been speaking to you.”

At that moment, the boy frowned. Dark clouds gathered over his handsome face, bright enough to call blue skies to mind, and lightning flashed.

Then, instead of his usual clear voice, a low, sunken voice slipped between his lips.

“That’s enough.”

A pale-blue gleam shone from his eyes in the darkness.

There was no trace left of Mungyeong, the bright and cheerful young medical apprentice.

What had taken his place was a peerless martial artist known by the sobriquet Slaughter Saint—a beast baring its sharp claws.

But that wasn’t true of only one person.

“Oh, how frightening.”

The old man curled up the corners of his mouth without a care in the world, standing before an aura powerful enough to freeze even an ordinary Peak master stiff as a statue. Then Fire King Jeok Cheongang tossed him the gourd.

“Drop the little-brat act—it doesn’t suit you—and wet your throat.”

Mungyeong caught the slowly approaching gourd and answered in a dry voice.

“Not interested.”

“What, are you not old enough to drink yet?”

“I quit. A long time ago.”

“Since you started playing medical apprentice?”

“…Don’t you sleep?”

“You get less sleep when you’re old. Like someone I know.”

Mungyeong gave a small shake of his head. For someone who had been taciturn and poor at expressing emotion his entire life, Jeok Cheongang was a difficult person to converse with. If he didn’t want to deal with him, avoiding him was the obvious choice.

“You leaving?”

“That’s none of your business.”

“What about the liquor?”

Mungyeong threw the gourd in his hand into the river. The rolling waves of the Yangtze swallowed it in an instant.

“I finished it.”

“…If you didn’t want to drink it, you could at least have given it back. What a nasty old man.”

As Mungyeong passed Jeok Cheongang, his gaze sharpened.

The Slaughter Saint was already a nonexistent person. The man standing here now was nothing more than an ordinary young medical apprentice one could find anywhere.

“Your tongue is too loose.”

“There aren’t any ears listening, so what does it matter? Besides, after coming all this way, why bother hiding your identity?”

Mungyeong did not answer.

No—he couldn’t answer.

Why had he done it?

Had it been nothing more than a momentary impulse?

It was something even the cold reason that had never wavered through countless killings could not explain.

“So you still haven’t found the answer yourself.”

After falling silent for a moment at Jeok Cheongang’s words, Mungyeong opened his mouth.

“It’s nothing more than traveling together.”

“I understand. This old man was the same at first. But then I met one bizarre bastard, and he completely ruined my later years.”

Mungyeong thought he knew who the “bizarre bastard” was. At the same time, he thought it was probably the most fitting description.

Even from the perspective of someone who had experienced every kind of person and incident in the turbulent martial world, that bastard was a completely unfamiliar type—the first of his kind Mungyeong had ever seen.

“Jin Taekyung.”

“So you do know him. Well, how could you not?”

“He’s a strange one. He’s reached an impressive realm for his age.”

The corner of Jeok Cheongang’s mouth twitched.

“Ahem. Impressive, my ass. He’s just lucky. In terms of pure martial talent, he can’t compare to the Sword Saint’s Disciple. He doesn’t seem to have noticed it yet, but he’s already finished preparing to open his Middle Dantian.”

Mungyeong recalled the young man who had performed tricks with a snake throughout the journey.

He also remembered the sight of that same young man at the Sichuan Tang Clan, scattering dazzling Sword Force despite being barely past the age of twenty.

“That kid was impressive too. No—he did seem impressively insane. In terms of talent alone, he’s definitely one step above Jin Taekyung.”

“What!”

“…?”

“Ah.”

Mungyeong stared at Jeok Cheongang and clicked his tongue.

“You dote on your Disciple.”

“Disciple?”

Jeok Cheongang hesitated briefly before letting out a hollow cough.

“Ahem. Well. He might be my Disciple, or he might not be…”

“What kind of nonsense is that?”

“No, well… There are some complicated circumstances. To explain how this happened…”

Mungyeong suddenly felt a headache coming on.

It had only been a few days since a group of people called Dark Heaven—people no one had ever heard of—had dyed Sichuan red with blood.

His thoughts were already tangled enough. Listening to a story involving this bizarre master and disciple made him feel as though he might develop seasickness despite having none before.

“If you have no business with me, I’ll be leaving. I hope nothing like what happened tonight ever happens again.”

Mungyeong tossed out the words and began walking toward the cabin.

“Thank you. For saving the kid.”

“…”

“I mean it.”

Mungyeong did not answer. He opened the cabin door. He could hear Jeok Cheongang grumbling about what a prickly old man he was, but he ignored him completely and sat down on a hard wooden berth.

On the berth beside his, a passenger who had claimed the spot long ago was deep asleep.

Mungyeong stared at the motionless Jin Taekyung and thought,

*He really is a bizarre one.*

Perhaps that was why he slept so strangely, too. At first, Mungyeong could barely detect his breathing and even wondered if Jin Taekyung had used the Turtle Breath Technique.

And that wasn’t all. He also possessed a Heavenly Martial Physique, a constitution that appeared only once every few hundred years.

Jeok Cheongang had even told him something unbelievable: that Jin Taekyung’s body was becoming more and more perfect.

*That’s impossible.*

Why was a Heavenly Martial Physique called a Heavenly Martial Physique?

Because it was the most perfect body for learning martial arts. That was why it was called a heaven-given martial constitution.

The word “perfect” only applied when there was nothing to add or subtract. Jeok Cheongang had surely judged the matter incorrectly because his foolishly doting eyes were clouded by his affection for his Disciple.

*Still, there’s no denying he’s an impressive bastard. No—are they both impressive bastards?*

On the berth immediately beside Jin Taekyung, Cheongpung was sleeping with drool dribbling from his mouth.

His lips were moving as though he were eating something. When Mungyeong looked more closely, he saw Cheongpung sucking on the head of the snake he always kept tucked beside him, mumbling in his sleep.

“Dumplings, roast duck, and mooncakes too, please…”

“…”

“Lots and lots, please…”

What on earth had happened while he was away?

Mungyeong looked back and forth between Jin Taekyung and Cheongpung with an awkward expression.

*These are the ones who are supposed to illuminate the future of Murim?*

Even to Mungyeong, the two had already gone far beyond the level of rising martial artists.

They were peerless geniuses who had broken through the wall into Supreme Peak despite being barely past twenty.

If either of them opened their Middle Dantian before turning thirty, then…

*This is…*

Mungyeong’s eyes twitched as he studied Jin Taekyung and Cheongpung.

*When? No, how?*

He sprang to his feet like lightning and hurriedly took Jin Taekyung’s pulse.

When he sent internal energy through the Mingmen acupoint, an utterly unbelievable reality unfolded before his eyes. One fact continued to circle through his frozen mind.

*His Middle Dantian… has opened?*

Even the Unshakable Mind he had cultivated over many years was useless.

And just as Mungyeong was staring blankly into the air, someone spoke.

“What are you doing?”

Mungyeong lowered his gaze and saw a pair of eyes looking up at him.

Jin Taekyung glanced in turn at Mungyeong’s two hands, one pressed against the Mingmen acupoint at his lower back and the other against his chest, where his Middle Dantian was located.

Then he opened his mouth.

“What the fuck?”

Mungyeong spoke sincerely.

“It was a misunderstanding.”

“More like, ‘Oh yeah.’”

“Please calm down and listen to me…”

Jin Taekyung answered his sincerity with an equally sincere response.

A shout loud enough to wake everyone aboard the fast ship.

“Old Master!”

*Boom!*

The cabin door exploded into ash and scattered as Fire King Jeok Cheongang appeared.

In the dead of night, the peaceful silence of the Yangtze was shattered.

* * *

Mu Song, known as Ship-Fire Boy, was the Disciple of the Seafaring King—the Alliance Leader of the Yangtze River Channel League—and the Stronghold Lord of Water Dragon Stronghold, which ruled the rivers of Sichuan. He cried out with a face as though the sky had fallen.

“No! My fast ship!”

I quietly looked away, while Mungyeong suddenly announced that he needed to prepare some medicinal herbs and left.

Jeok Cheongang, who had burned one of Mu Song’s fast ships to ashes, patted him on the shoulder.

“It’s fine. You can just build another ship.”

“No! Noooo!”

“Come now, I said it’s fine. Aren’t ships made in a snap as long as you have people and gold?”

“It isn’t that simple! This isn’t an ordinary ship. It’s a special fast ship that only our Yangtze River Channel League can build! To make another one, we’d have to request it from headquarters, bring in craftsmen, and pour a thousand gold pieces into it…”

Mu Song’s furious voice gradually grew quieter.

That was because Jeok Cheongang was looking at him with a sinister smile.

Scorching Yang Qi was already blazing around his fist.

“A thousand gold pieces, and then what?”

Mu Song shut his mouth.

He was clearly weighing whether to pour a thousand gold pieces into rebuilding the fast ship or pour his own blood into the Yangtze.

In the end, it came down to money or his life. The choice wasn’t difficult.

“…I was about to say that even after pouring a thousand gold pieces into it, we’d still have money left over. Great Hero Jeok.”

“Right? Business is good around here, isn’t it?”

Mu Song’s ferocious face twisted. It was a scene that would make ordinary people soil themselves right down to their organs, but despite how he looked, that was his smile. He was a true-blooded river bandit, so his features were simply atrocious.

Despite his size, he rubbed his palms together eagerly.

“Oh, don’t even ask. We’d take more if there were anything left to take.”

“Yes, yes. Good to hear. Since it came to mind, let me say this: don’t rob people too much. It’s none of my business, but they need to make a living too.”

“Yes, yes.”

“I apologize once again for what happened. I made a small mistake while training.”

“Of course. Anyone could make such a mistake. Did you get hurt anywhere?”

“No. But my qi has felt weak lately. It would be nice to have something to chew on…”

“A few good pieces of He Shou Wu came in recently. It looks like they’ve finally found their rightful owner.”

“The owner is you. This old man is merely a customer. Ha ha. Still, if you’re giving it to me, I’ll accept it gratefully.”

After patting Mu Song’s shoulder a few times, Jeok Cheongang turned around and glared at me.

“Damn it. Why did you make such a commotion in the middle of the night?”

I answered calmly.

“Imagine waking up from a nap and finding some man touching your chest and back.”

“I’d burn him down to bone ash.”

“Yes. That’s what happened. How was I supposed to make a judgment in that situation? And then you smashed everything to pieces before I had a chance to stop you.”

The result had been scorching.

Mungyeong had evaded Jeok Cheongang’s attacks with ghostlike movements, true to his sobriquet as the Slaughter Saint, while the Flame Divine Palm packed with superheated force had set the fast ship ablaze.

Jeok Cheongang frowned and muttered,

“I thought that bastard hadn’t kicked his old habits.”

“Well, they say a habit formed at three lasts until eighty.”

“He passed eighty a long time ago, didn’t he?”

“Then let’s say a habit formed at three lasts until a hundred.”

Mungyeong, who had been busily moving around and checking on the people who had fallen into the water, whispered as he passed us.

“If you don’t want to die, shut your mouth.”

Instead of keeping quiet, I shouted loudly enough for everyone to hear.

“Mungyeong, what did you say?”

“Yes, yes?”

“No. Didn’t you just say something to me?”

“That couldn’t… possibly be. You must have misheard me.”

“Right?”

“Yes, yes.”

“Then keep doing your work. Thanks for your hard work.”

“Thank… you.”

This was the fate of someone too committed to his persona.

Anyway, it sure was a spectacle immediately after coming back.

*This is Murim.*

I shook my head as I gazed at the Yangtze stretching endlessly into the distance.
## Chapter artifact 436

# Chapter 436

The Yangtze.

As its name alone suggests, the Yangtze was enormous. In terms of length especially, few rivers on the continent could compare.

It crossed five provinces in all—Sichuan, Chongqing, Hubei, Anhui, and finally Jiangsu. As a vital hub of waterborne transportation, it would occupy a large portion of our journey.

“Our current plan is to follow one of the Yangtze’s tributaries to Hubei, then disembark and continue overland to Henan.”

After finishing his rough explanation, Jin Wikyung slowly looked over the group, including me.

“Does anyone have any questions?”

Whoosh!

The instant he finished speaking, one hand shot into the air.

Judging by the speed with which it went up, its owner looked like an honors student bursting with academic enthusiasm.

In reality, the hand belonged to a Supreme Peak master known throughout Murim as a nationwide thug.

“There’s something this old man has been wondering about for a while.”

“I’m all ears, Great Hero Jeok.”

“So what you’re saying is…”

Jeok Cheongang continued with a deeply sour expression.

“It sounds like you’re telling us to grow old and die on this damn Yangtze. Am I mistaken?”

That was the Fire King for you. He really knew how to bring the heat.

Jin Wikyung swallowed hard at Jeok Cheongang’s way of speaking, which came crashing forward like an eight-ton truck with a broken steering wheel.

“How could that be, Great Hero Jeok? This is simply the itinerary decided upon in our meeting.”

“A meeting? What kind of lunatics came up with this schedule? Even at the fastest pace, it’ll take seven days and nights just to reach Hubei!”

“At the top, we have Great Hero Sword Saint Mae Jonghak, and beneath him, the Nine Sects and One Gang and the Five Great Families…”

“That’s enough. I don’t need to hear any more.”

“Pardon?”

“The Nine Sects and One Gang and the Five Great Families are all idiots with nothing but shit in their heads, so forget about them. I’ll explain things properly to Mae Jonghak myself. Change the itinerary while there’s still time. Staring at water all day is going to give me qi deviation.”

In short, he was telling them to do their worst.

It was the kind of bullying only Jeok Cheongang could get away with. Not a single person here dared object to him.

*Ah. There was one person who could.*

Jeok Cheongang must have had the same thought, because he subtly turned his head.

His gaze met Mungyeong’s in midair.

Mungyeong looked back at him with an expression that clearly said *pathetic*.

Jeok Cheongang stared at him, then tossed out a single remark.

“Hey, what are you looking at me like that for?”

“…”

“You little punk, you’re still wet behind the ears. I ought to poke your eyes out and drain all the ink from them.”

He was openly laying into him now.

Mungyeong’s fist trembled.

As someone who knew his true identity, I found the sight chilling. To everyone else, however, it looked entirely different.

Hyuk Mujin and Gung Gibang, who had been languishing from the aftereffects of sampling the Yangtze, spoke in faint, faltering voices.

“Why are you picking on the boy? Just look at Mungyeong shaking. He’s such a gentle soul…”

“I may eat stray yellow dogs, but Mungyeong couldn’t kill an ant.”

“…”

He probably killed people during the time it took to kill an ant.

I had heard that more than a thousand people had been ‘officially’ declared dead at the hands of the Slaughter Saint.

Even if he went around with antibiotic ointment smeared on his sword, he wasn’t exactly the sort of person one would call gentle.

“You lot… No. Forget it. Just keep living like that.”

Jeok Cheongang had looked ready to say something, but he let out a deep sigh instead. Then, all of a sudden, he turned toward me.

“Why are you saying nothing?”

“About what?”

“What do you think? Do you really want to keep floating around on this miserable water?”

“Oh, that.”

I scratched my chin and thought for a moment before answering.

“I don’t mind it.”

“What!”

“Little Brother!”

Jeok Cheongang and Jin Wikyung’s expressions swung in opposite directions. But I hadn’t said it to help Jin Wikyung. I meant it.

“There must be a reason the people in charge decided on this route. Besides, the scenery is nice.”

This was a world without environmental pollution. Whenever dawn came and a hazy mist covered the river, looking out over the clear water stretching endlessly into the distance made me feel as though my chest were opening up.

When Jeok Cheongang had been unconscious, I hadn’t felt anything at all.

But now…

Regardless, I needed to set aside my impatience for a while and take the time to reflect and collect myself.

*And there are things I need to investigate.*

The mysterious patterns and symbols found in both worlds.

I had to find out whether my suspicions about them were correct. To do that, I had a lot to take care of while going back and forth between Murim and the modern world. If we traveled overland, the time available for that would be drastically reduced.

I tried to gently coax Jeok Cheongang around.

“It’s only a difference of a few days. Old Master—no, Master, you need to think about your health too. It hasn’t been long since you pushed yourself so hard.”

“What do you mean, pushed myself? Do you think this old man is on his deathbed?”

“Then what? Are you sixteen again? Eighteen and in the prime of youth?”

“You little bastard!”

The moment Jeok Cheongang’s eyes lit up, I hurriedly opened my mouth.

“Martial arts! I need instruction in martial arts!”

The hand that had risen as though to smack me stopped in midair.

I didn’t miss the opening and continued.

“I’ve gained some insight recently. If we travel overland, there won’t be enough time for you to teach me.”

“Instruction…”

“There are parts I could never understand on my own, no matter how hard I rack my brain over them—even if I died and came back to life.”

“Is that true?”

“Yes. It’s precious instruction that only one person in all the world can give me—my master.”

Jeok Cheongang narrowed his eyes.

“If we use movement techniques to our fullest overland, we could reach Henan several days earlier.”

“What does that have to do with receiving instruction?”

“It has everything to do with it. Didn’t you say before that you thought Sword Saint Mae Jonghak might be stronger than this old man? By your logic, shouldn’t you reach Henan as quickly as possible and ask the Sword Saint?”

I had tossed that out to tease him, but he remembered it.

I pretended not to know what he was talking about.

“You must have heard me wrong. Was I drunk out of my mind that day?”

“What a load of drunken bullshit.”

“To me, Master, you’re always the best.”

“Is that so?”

Jeok Cheongang glanced sideways at Mungyeong before asking,

“Then how do I compare to the Slaughter Saint?”

“What?”

“I mean the Slaughter Saint. The one among the Three Saints who has no equal when it comes to killing people. How do I compare to him?”

I could feel the people around me waiting with interest for my answer.

And I could also feel someone discreetly leaking killing intent.

*Ah, fuck it. I don’t know.*

I swallowed hard and opened my mouth.

“He’s a total fucking pushover.”

“Hm. Perhaps this boy knows what he’s talking about.”

“I’m something of a martial arts expert myself, you know. I can size someone up at a glance.”

“Ahem. Did you grease your tongue? You’re showering me with flattery you never use normally. Do you think this old man will fall for such a shallow trick?”

“…Then why are you smiling?”

Was he Murim’s Joker?

Jeok Cheongang’s smile stretched all the way to his ears, but he immediately straightened his face. He couldn’t quite hide the corners of his mouth twitching as he struggled not to laugh.

“When did I smile?”

“No, never mind. In any case, let’s just keep going like this.”

Jeok Cheongang already knew that I had opened my Middle Dantian. He considered it for a moment, then smacked his lips.

“Damn it. Even so, I hate water. Looks like this old man will be suffering in his twilight years.”

“…”

Had he been a Fire Pokémon in his previous life?

At this point, perhaps he should change his sobriquet from the Fire King to Charizard.

“What’s with that disrespectful look?”

“Me? When did I do that?”

“Forget it. It isn’t the first or second time, anyway. It was my mistake for expecting manners from an uncouth little brat like you.”

Jeok Cheongang clicked his tongue and turned toward Jin Wikyung.

“You heard everything, didn’t you?”

“Yes. We will see to it that you are kept comfortable.”

“So what are you planning to do after taking this miserable Yangtze to Hubei? There must be a reason worth enduring this much trouble.”

“We have an important matter to attend to.”

“An important matter?”

“Would it be all right if I told you later?”

Jeok Cheongang narrowed his eyes, but that was all.

If Jin Wikyung was speaking that way, it meant the matter was confidential—something better discussed with fewer ears around.

Jeok Cheongang might not care about other people’s reactions, but he wasn’t completely oblivious to them.

“Understood. Then are we finished here?”

Jin Wikyung politely clasped his hands.

“Thank you for your hard work.”

But one person was dissatisfied with the results of this brief meeting.

“W-wait a moment. Are you saying you intend to take our Water Dragon Stronghold’s fast ship all the way to Hubei?”

Just as Jin Wikyung was about to answer Mu Song, the owner of the ship, Jeok Cheongang stepped between them.

“Is there a problem?”

“Great Hero Jeok, Hubei is much too far. Even with a favorable wind, it will take more than seven days…”

“You can’t leave the stronghold empty for that long?”

“Yes, yes! Exactly!”

“A body can’t function with its limbs attached but its head missing. That would be a problem.”

“What does that mean…?”

“Go as far as Sichuan.”

Mu Song’s face brightened.

“Thank you!”

“Leave the ship behind.”

“What?”

“Am I supposed to travel in a skiff? We can find sailors along the way. Leave this fast ship—or whatever it’s called—and go back.”

Mu Song fell silent for a moment before managing to speak.

“Well…”

“What?”

“Now that I think about it, it would be better for me and my subordinates to escort you with every effort.”

“Good heavens, that really isn’t necessary. I already feel bad about burning one of your ships, so I’m not sure whether I should impose on you like this.”

“…Please don’t set anything else on fire.”

“That depends on how you behave.”

Was this the tyranny of a major corporation?

In all my life, this was the first time I had ever felt sorry for a river bandit.

As Mu Song withdrew with a sorrowful expression after clasping his hands, Cheongpung quietly approached him and held out the dumpling in his hand.

Who knew how much he had eaten in the meantime? Both his cheeks were already on the verge of bursting.

“’Ave it.”

“…Are you telling me to eat it? Are you giving it to me?”

“Yeah!”

Feeling the warmth of human kindness for the first time in ages, Mu Song’s eyes grew misty.

“Thank you, Young Hero Cheongpung.”

Then he stuffed the cold dumpling into his mouth in one bite.

After swallowing what he had been chewing, Cheongpung smiled brightly.

“Tasty, right?”

“It truly is. It’s the most delicious dumpling I’ve eaten in a long time. I’ll have to get some from you again sometime.”

“That was the last one.”

“What? You gave me the last dumpling? Young Hero Cheongpung, you…”

“My grandpa told me that when you have something good, you should share it with other people.”

Considering how much he had eaten by himself until now, it sounded like complete bullshit. But Mu Song didn’t know that, and he was deeply moved.

“Thank you, Young Hero Cheongpung. We’ve barely even spoken, yet you’ve gone out of your way to do this for me. I didn’t know that… Sniff.”

Mu Song’s gratitude did not last long.

“My grandpa also told me something else. Whoever eats the last dumpling has to buy the next dumplings!”

“…”

“…”

“If we travel for one more day, we’ll reach a place called Guang’an. The dumplings sold in the market there are really good. When I traveled around the world for a year, I stayed there for a whole month because of those dumplings. Ah, no, that’s not what I meant. Grandpa said we absolutely had to stop there! He said whoever ate the last dumpling had to buy a whole bunch more!”

“…”

“…”

What a terrifying little bastard.

Now he was even using his grandfather to get more dumplings.

Gung Gibang, who had been watching the scene, muttered that Cheongpung would make an excellent Beggars’ Sect disciple.

Mu Song, who looked as though he was about to visit the Guang’an dumpling shop, answered with every ounce of trust in humanity drained from his face.

“Understood.”

“Yay! Grandpa will be happy!”

Was that even human?

I was still horrified by the depths of his character when—

“You don’t look well. May I examine you for a moment?”

Fucking pushover—no, Mungyeong was looking at me with concern.

He had a large acupuncture needle hidden in one hand, pressed right against my waist.

“Uh, no. No, I’m fine. I’m not feeling—”

“You don’t look well. May I examine you for a moment?”

“I’m really fi—”

“You don’t look well. May I examine you for a moment?”

“…”

It was humiliating, but I think I may have wet myself a little.
## Chapter artifact 437

# Chapter 437

As its name suggested, a fast ship was built with speed as its top priority.

If an ordinary warship was a heavyweight in terms of size, then a fast ship was something closer to a welterweight.

As a result, the ship’s hull wasn’t particularly large. Which meant there weren’t many places to hide from everyone else.

“Oh, dear.”

“Great Hero Jin. What brings you here?”

Two river bandits who had been slacking off at the stern under the pretense of standing guard recognized me and bowed deeply.

I nodded gravely and opened my mouth.

“Save me…”

At that moment, something sharp poked me right in the Mingmen acupoint at the small of my back.

“Save—stay alert as you go.”

“What?”

“I said, stay alert as you go. I need to discuss something with this fellow for a moment.”

“Oh, I see.”

*No. Don’t agree. Please be suspicious.*

I continued speaking while shooting an urgent sidelong glance at Mungyeong, who was pressed tightly against my side with his needle at my back.

“Be sure to take care on your way! If anyone asks about me, tell them I’m with Mungyeong!”

“Uh, understood.”

“No, not ‘understood.’ Say, right! My master! If my master comes looking for me…”

“I don’t think that’s likely.”

Mungyeong cut me off with a clear smile.

“Your Master seemed to have something important to discuss with Great Hero Jin Wikyung. In any case, we’ve only come to see a patient for a moment, so please don’t concern yourself with us. Go on and rest in the cabin. I’ll let you know afterward.”

“Then that works for us.”

There was nothing sweeter than legally slacking off in the middle of a boring guard shift.

The river bandits, now free to enjoy the shade, smiled and left. The Sound Transmission I had been preparing to send as my last hope was blocked by a single sentence from Mungyeong.

“You seem to have three or four lives.”

“…”

“You have two choices. Answer every question this old man asks from now on, or quietly keep your mouth shut if you don’t want to.”

I asked, just in case.

“What happens if I choose the second option?”

“You’ll go to Hubei.”

“That doesn’t sound too ba—”

Just as I was about to answer, Mungyeong calmly continued.

“You’ll drift all the way to Hubei while sunk at the bottom of the Yangtze. Quietly.”

“…I thought you said you had given up killing.”

“That depends on this old man’s will. It’s none of your concern.”

*What the fuck? It isn’t like he’s quitting smoking…*

Unable to believe what I was hearing, I challenged him again.

“You’re the Divine Physician. Are you really threatening to kill me?”

“I’m the former Divine Physician. I passed that name on to my Disciple long ago. So? What’s your answer?”

I glared at Mungyeong.

“Do you really think I’ll give in to a threat like this?”

“Of course.”

“You read me perfectly. I’ll answer every question with the utmost sincerity.”

“…”

Mungyeong seemed to have lost his words for a moment. After a long silence, he finally spoke.

“I’ve met all kinds of strange men, but you’re something else.”

“From everyone else’s perspective, I’d say we’re no different. Send a messenger-pigeon survey to all of Murim and ask which one of us is the bigger freak.”

“Freak?”

“My tongue slipped. Sorry.”

The aura Mungyeong let loose made every hair on my body stand on end.

He silently stared at me as I swallowed hard, then tossed out a single word.

“Middle Dantian.”

“Huh?”

“Until a few days ago—no, until half a day ago—your Middle Dantian was closed. What trick did you pull to accomplish such a great feat overnight?”

*So this was why he had called me aside.*

*I knew he had noticed.*

Martial realms were arranged in a perfect vertical structure.

It was like sitting at a high point and looking down at every landscape beneath you.

The Fire King and the Slaughter Saint were extraordinary powerhouses who had climbed to the highest peaks in the rugged mountain range known as Murim.

They had opened their Middle Dantians long before a person named Jin Taekyung had even been born. Naturally, they had noticed my change.

The problem was…

*What am I supposed to tell him?*

It wasn’t as though I had farted in my sleep and somehow opened my Middle Dantian. Other people could only gain that kind of enlightenment through blood-soaked training or extreme situations where they hovered between life and death.

I hesitated for a moment, then spotted the large acupuncture needle in Mungyeong’s hand and answered quickly.

“It just happened.”

“What?”

“It just opened.”

“Are you telling me to believe that?”

*Obviously not.*

So I inserted a cliché commonly found in martial arts novels.

“Actually, I did have a strange dream.”

I lowered my voice and glanced around us. Mungyeong’s brow furrowed.

“A dream?”

“Yes. A white-haired old man who looked incredibly ancient suddenly started swinging a sword at me without warning. At the time, I didn’t even realize it was a dream, so I just focused on dodging.”

It didn’t matter whether it had been a spear, a sword, or a back-scratcher. This was a world where all kinds of superstition ran rampant.

The appearance of a white-haired old man with the air of an immortal was interesting enough to pique anyone’s curiosity.

Sure enough, Mungyeong asked with an expression like a webnovel reader waiting for the next update,

“And then?”

“I summoned every last ounce of strength I had and fought back, but I couldn’t even come close to matching him. No matter what attack I used, he dodged it without a care. And whenever I tried to get away, he would glide up to me like a ghost and slash me with his sword. Swish, slash—ugh! You know the feeling?”

“You didn’t realize it was a dream?”

“I didn’t have time to realize anything. Besides, the pain was incredibly vivid. I was cut hundreds of times in an instant and thought, *So this is how I die.* But not a single drop of blood came out. That was when I realized it was a dream.”

“Continue.”

“But it was driving me insane. I kept getting cut by that sword, and it hurt like hell. Even after I realized it was a dream, I couldn’t wake up.”

“Yes. Exactly.”

Mungyeong flinched as if he had been cut himself.

*This guy has surprisingly good reactions.*

Having confirmed the instinct of the webnovel reader hiding behind the terrifying name of Slaughter Saint, I continued without hesitation.

“I don’t even know how much time passed. Days? Months? I lost all sense of time as I was cut countless times and kept swinging back. Then, all of a sudden, a strange sensation came over me.”

“Explain it in detail. What was it like?”

This part, at least, I could describe in detail and tell him the truth. It was something I had personally experienced in my battle with the Arch Lich.

Mungyeong heard my explanation—one that an ordinary person might have dismissed as some vague, airy description—and muttered quietly.

“Enlightenment. You gained a fortuitous encounter.”

“Wow, I’ve got goose bumps. He said something similar.”

“He left you a message?”

“Yes. He looked at me and smiled for the first time, then said that this fortuitous encounter was a blessing he was giving me and that I should devote myself to my training even more.”

“Was that all?”

“Huh?”

“Did he say anything else?”

“Uh, well…”

*Hold on. I didn’t plan for this.*

I had come up with the story by squeezing my brain dry in a short amount of time. I had already used up everything I’d prepared.

But Mungyeong was demanding another installment, and I had no material left in reserve.

The problem was that Mungyeong wasn’t an ordinary reader.

He was the Slaughter Saint.

*What happens if I end it here?*

What would happen? I’d sink to the bottom of the Yangtze and drift all the way to Hubei.

Under Mungyeong’s narrowing gaze, I hurriedly opened my mouth.

“He did say one more thing.”

“What did he say?”

“Well, that is…”

*Fuck it. I don’t know.*

I swallowed dryly and cautiously spoke.

“You have to suffer to be a Murim man.”

“What?”

“He really said that. He said exactly that, then climbed onto his sword and flew away…”

“I can sense profound wisdom.”

“Huh?”

I let out a stupid sound while keeping a wary eye on the large needle in Mungyeong’s hand.

*What the hell is he talking about now?*

When I raised my head, I saw Mungyeong murmuring under his breath and nodding slightly as though he were groaning.

After muttering something unintelligible, he suddenly spoke.

“It was Lü Yan.”[^1]

“I know about stomach cancer and lung cancer, but… are you sick somewhere?”

[^1]: The Korean reading of Lü Yan’s name, *Yeo-am*, ends in *am*, the Korean word for “cancer”—hence Taekyung’s misunderstanding.

“…You don’t know Lü Yan?”

Mungyeong looked at me as though I were insane, then continued.

“Lü Yan. His courtesy name was Dongbin, and his Taoist name was Chunyangzi. He attained his own Dao and reached the realm of an immortal. People called him the Sword Immortal.”

“Wait. You mean Lü Dongbin?”

“You finally understand.”

I might not have known Lü Yan, but I knew Sword Immortal Lü Dongbin. Along with Jang Samfeng of Wudang and the Shaolin Temple’s Bodhidharma, he was one of the three perennial fixtures of martial arts novels.

Mungyeong continued, his expression deadly serious.

“The old man you saw in your dream must have been Lü Dongbin. He vanished using sword-riding sorcery at the end, so he must have been the Sword Immortal.”

“Uh… I suppose so.”

I had only made it up because it sounded cooler, but somehow it had turned into this.

I knew from novels that there was an immortal named Lü Dongbin, but this was the first time I had heard that he was a master of sword-riding sorcery.

*If you hang it on your nose, it becomes a nose ring; if you hang it on your ear, it becomes an earring.*

That was exactly the situation I was in.

Having decided that the old man in my dream—or rather, the old man in my story—was Lü Dongbin, Mungyeong was fitting everything together with absolute seriousness without even realizing it.

“Did his beard reach down to his chest?”

“Yes.”

“How tall was he?”

“He was short.”

“Boy! I’m asking how short!”

“Oh, he was just short. I was being cut to pieces the whole time. When would I have had the chance to look at something like that?”

Mungyeong nodded and let most of it pass, but there was one dangerously close call.

“What did he carry besides the sword?”

“What was it… His scabbard.”

“Do you want to die? Of course he had that. Was there nothing else?”

“…I think that was all.”

The light in Mungyeong’s eyes sank deep.

“Lü Dongbin did not carry only a sword. He always held a Taoist fly-whisk in his right hand.”

“…”

“Have you been lying to this old man all along?”

It was a life-or-death crisis.

I had no idea why a man known as the Sword Immortal would walk around carrying a fly-whisk, but my top priority was avoiding Mungyeong’s suspicions. Without letting a single change cross my face, I answered.

“Everything I said was true.”

“Then why does your description contradict Lü Dongbin’s usual appearance?”

“He must have left his fly-whisk behind today.”

“What kind of bullshi—”

“No, wait. Have you ever seen Lü Dongbin?”

“…”

“I have.”

*Fuck, I’m the one who saw him. What are you going to do about it?*

Seizing the advantage, I pressed Mungyeong hard while he was momentarily at a loss for words.

“And did I say he was Lü Dongbin? I thought he was just some old man. You were the one who called him Lü Dongbin first.”

“You?”

“That isn’t the point. That’s what happened, isn’t it? Honestly, I don’t care whether he was Lü Dongbin or Kim Dongbin. I met some unidentified old man in a dream and gained a fortuitous encounter. That’s all. But you’re hounding me like I’ve committed some terrible crime, so I really…”

“…”

“Can you see the tears in my eyes? I really don’t want to do this as a man, but I’m so wronged that I’m actually crying.”

The truth was, I was scared.

The self-loathing over having to invent lies while being threatened like this—despite having committed no crime—only made things worse. Before long, another tear rolled down my cheek.

*Is this what life is?*

I had wet myself below earlier, and now I was wetting myself above.

I had started all this as an act, but it had somehow become real. For the first time, bewilderment crossed Mungyeong’s nearly expressionless face.

“You little bastard. What trick are you pulling?”

“Ugh, you’re doing it again. I’m done. I quit. I answered everything, so I’m leaving.”

“You’re leaving?”

“I don’t care. Do whatever you want. Kill me, spare me, use Impure World Reincarnation[^2] on me—whatever.”

[^2]: Impure World Reincarnation is a resurrection technique from *Naruto*.

Just as I was about to take a step, someone appeared while scattering a powerful aura.

“What the hell is this dogshit?”

The gazes of the Fire King and the Slaughter Saint collided in midair.
## Chapter artifact 438

# Chapter 438

Jeok Cheongang’s eyes blazed as he glared at Mungyeong.

“How dare you threaten someone else’s dis, dis… disciple Taekyung while this old man was away?”

“…What the hell is a ‘disciple Taekyung’?”

Utterly dumbfounded, I muttered under my breath, my tears drying up at once. Jeok Cheongang roared.

“Quiet!”

Mungyeong and I answered at the same time.

“You’re louder, Old Master. You’re practically shouting ‘disciple Taekyung’ from the center of the world.”

“Judging by the volume of your voice, you’ll live another ten years.”

*Did he roast and eat a train smokestack in an air fryer?*

It was a good thing Mungyeong had been using his internal energy to maintain a qi barrier and keep any sound from escaping. Otherwise, people would have gathered around us long ago.

Jeok Cheongang’s face had turned bright red. Mungyeong clicked his tongue softly.

“We merely had a brief conversation. What would this old man gain by threatening such a young pup?”

Jeok Cheongang turned toward me.

“You answer me. Is what that old man said true?”

“It’s true that we only talked, but he said I’d sink to the bottom of the Yangtze if he didn’t like my answer.”

At my betrayal, Mungyeong shamelessly added,

“Of course, I did frighten him a little.”

“Would you look at this damned old man! You think you’ll get away with something like this?”

“Calm yourself. I merely had something to ask him about his Middle Dantian.”

Jeok Cheongang had leaned forward as though he were about to charge, but he stopped dead.

“Middle Dantian?”

“Yes. Surely you didn’t fail to notice.”

“…”

“Opening one’s Middle Dantian in such a short time is impossible. Even the phrase ‘heavenly fortune’ cannot explain it.”

Jeok Cheongang looked back and forth between Mungyeong and me, then let out a quiet laugh.

“So it was nothing.”

“…What?”

“So you’re trying to say that the boy learned demonic martial arts or something?”

“That’s…”

“I’ll put it simply. No.”

Mungyeong was left speechless by Jeok Cheongang’s calm, utterly confident response. At that moment, Jeok Cheongang crooked a finger at me.

“What are you waiting for? Come here.”

“Huh?”

“You asked me to watch your training, didn’t you? We’re starting now.”

“Oh. Right.”

The situation had moved on so smoothly that even I was caught off guard. As though he had read my thoughts, Jeok Cheongang asked,

“I am curious, though. How exactly did you open your Middle Dantian?”

“Uh, well. I had a dream, and there was this old man with a sword…”

“Did you meet the Sword Immortal Lü Dongbin?”

“…Well, judging by what that guy over there said, it might have been.”

“You gained a fortuitous encounter. It seems the heavens are helping you. Strange things that no one could ever imagine do happen in this world.”

Jeok Cheongang was looking at me, but his answer was directed at Mungyeong.

After tossing out that single remark as though he wanted Mungyeong to hear it, Jeok Cheongang suddenly swung his wrinkled hand.

*Smack!*

“Ow! Why did you hit me?”

“I felt like hitting you because you were irritating. Got a problem with that?”

“What if I do?”

“Then you can take another hit.”

*Whack!*

“Aaagh!”

“You blockheaded brat. What are you whining about? Stop fooling around and follow me.”

*Can I really just leave like this?*

I glanced at Mungyeong, who stood there with a strange expression that revealed nothing. A thunderous shout immediately crashed down on me.

“And yet this brat!”

“Okay, okay, I get it. Please stop shouting.”

“Dragging your feet like this, do you even intend to train?”

I turned my back on Mungyeong and followed close behind Jeok Cheongang, whispering,

“But aren’t you going to ask anything else?”

Jeok Cheongang answered gruffly without turning around.

“Ask about what?”

“No, I mean… the Middle Dantian…”

“Stop talking nonsense and follow me. From now on, don’t go anywhere near that old man.”

“Yes, sir.”

That was exactly what I wanted. I wasn’t some Mermaid Princess of the Yangtze, and I had absolutely no intention of getting on his bad side and drifting all the way to Hubei with the fish.

“If I catch you looking like this again, I’ll teach you a lesson. Understand?”

“…I’m the victim here. Why are you blaming me?”

“Quiet. I was about to smash everything to pieces earlier, but I held myself back.”

“Come to think of it, you really did show restraint.”

“Would the ship have survived if I hadn’t?”

“True. We should take Senior Mu Song’s circumstances into consideration. Did you see his face when we boarded the fast ship?”

Jeok Cheongang whipped his head around and frowned.

“What kind of nonsense are you talking about? Why should this old man care about the circumstances of those river bandits?”

“Huh?”

“If we lose another ship here, we’ll have to transfer everyone aboard to a different one. The extra weight would slow us down.”

“…Oh.”

“Think before you speak. We need to get off this wretched Yangtze as quickly as possible. It’s damp, it rocks, and it never seems to end.”

*What a lovely personality.*

I watched the Fire Pokémon walk away, shivering from head to toe, when a thought suddenly occurred to me.

*If we burn everything down, couldn’t we travel by land?*

I decided not to say it. Jeok Cheongang was more than capable of actually doing it.

I ignored Mungyeong’s prickling gaze on the back of my head as best I could and followed Jeok Cheongang.

* * *

The fast ship cut through the water without slowing.

Boats that saw the flag of the Yangtze River Channel League flying high above the deck hurriedly cleared a path. Even the government warships connected to the League through their sticky ties of collusion were no exception.

The river bandits knew the lower Yangtze and its waterways like the backs of their hands. Following Mu Song’s orders, they pulled hard on their oars, while the sails billowed wide in the wind blowing from far away.

Like the rough waters of the Yangtze, the hours of that day flowed by quickly.

And…

Just as he had the previous night, Mungyeong sat at the bow, gazing out at the Yangtze shrouded in darkness. When the uninvited guest who had come to see him again arrived, Mungyeong spoke in a low voice.

“You’re later than I expected.”

“It took time to find the liquor that fellow Mu Song—or whatever his name is—had hidden away. He fought to keep it from me until the very end.”

Jeok Cheongang perched himself on the railing and broke the seal on a small jar he had taken out as carefully as though it were a treasured family heirloom.

At the same time, the fragrant scent of liquor spread through the air. A crack appeared in Mungyeong’s usually expressionless face.

“Jiannan Chun?”

“Of course it’s Jiannan Chun when you come to Sichuan. This is what makes the trip worthwhile.”

“That doesn’t seem like ordinary Jiannan Chun.”

“According to that fellow, it was a gift from his Master. A man as eminent as the Seafaring King wouldn’t have given his Disciple ordinary liquor… Thanks to him, this old man’s tongue is enjoying a rare treat.”

Jeok Cheongang lifted the jar to his mouth and gulped down the liquor. Then he smacked his lips.

“Damn, that’s good. Want a drink?”

Mungyeong watched the jar of Jiannan Chun closely, then shook his head.

“…I believe I told you I quit drinking a long time ago.”

“Your answer was too slow. For an old man known as the greatest assassin in history, you make your thoughts awfully easy to read.”

“That still makes me better than an old man who carries on like a reckless brat at his age.”

“What did you say?”

“I’d like to dispense with the nonsense and get to the point. You have something to say to me, don’t you?”

Jeok Cheongang’s visit the previous day had been unexpected. Today was different.

Several shichen earlier, Jeok Cheongang had used Sound Transmission to tell Mungyeong that he would come. Mungyeong had been waiting for him.

“You’re impatient. That isn’t very assassin-like, either.”

“I’m a medical apprentice, not an assassin.”

“Then call yourself a killer of lives.”

“Disciple and Master alike. Your words and actions are exactly the same.”

Jeok Cheongang ignored Mungyeong’s frown, took another drink, and wiped his mouth with his sleeve before answering.

“Our words and actions may resemble each other, but we’re worlds apart. That brat is a monster who has strayed beyond all common sense.”

Mungyeong nodded silently.

He couldn’t disagree with the word *monster*. Reaching the Supreme Peak realm just after passing the age of twenty was astonishing enough, but Jin Taekyung had taken another step before he had even caught his breath.

*When did he reach the Supreme Peak realm?*

Mungyeong searched through memories of the distant past.

He had been younger then—sharper and quieter than he was now. He had devoted his soul and heart entirely to martial arts.

Sometimes covertly and sometimes through direct confrontation, he had accumulated experience through countless real battles. At last, he had set foot in that exalted realm that only the chosen could enter.

*It was sometime in my mid-thirties.*

Even Mungyeong, who had been called the greatest assassin in history and given the name Slaughter Saint, had not reached the Supreme Peak realm until after turning thirty.

And he had opened his Middle Dantian several years later, when he was nearing forty.

Yet Jin Taekyung had left his mark on Murim’s long history just after passing the age of twenty.

In Mungyeong’s estimation, this could only be the work of demonic, heterodox arts—and a legendary demonic martial art at that.

“I have a feeling this conversation will take a while.”

“No, it’ll be over quickly. This old man doesn’t have much to say, either.”

Mungyeong’s gaze sank deeply at Jeok Cheongang’s answer.

“Why not?”

“What can I say about something I’ve never seen or heard? There’s nothing to do but accept it.”

“Surely you don’t believe the nonsense that the Sword Immortal Lü Dongbin appeared in his dream and gave him enlightenment.”

“It may have happened, or it may not have. But even if it’s true, it isn’t all that surprising. Heh heh.”

“Fire King!”

The thunderous cry struck the qi barrier surrounding the two men and reverberated with a deep hum.

But the anger that had flashed across Mungyeong’s face vanished as though it had been washed away by Jeok Cheongang’s next words.

“Two years.”

“…What did you say?”

“It took that brat only two years to break through the wall of the Supreme Peak realm and open his Middle Dantian. If this old man were Lü Dongbin, I would have come to him in person—not in a dream—saying, ‘There’s an incredible fellow in the lower world.’”

Mungyeong first questioned his own ears, then Jeok Cheongang’s state of mind.

But the small old man before him continued speaking with eyes clearer and more transparent than ever.

“Don’t doubt him. When you face that brat, erase everything you’ve seen and heard throughout your life from your mind. Do you understand what I mean?”

“……!”

“Taekyung. That boy and the Sword Saint’s Disciple are, in the truest sense, divine dragons. No one has ever seen one. All anyone can do is guess.”

*Whoosh.*

White foam splashed against the bow. A long time passed before Mungyeong broke the silence.

“I can’t believe it.”

“I didn’t tell you to believe it. I only told you to accept it.”

“That’s impossible. Every part of it.”

“There’s one truth this old man learned while growing older for no reason. You can’t control another person’s heart.”

Jeok Cheongang had learned that only after sending his first Disciple away.

And it was only on the day he sincerely accepted a young man he had met by chance deep into his heart that he suddenly realized something else.

The pain that throbbed whenever he thought of that day had grown fainter.

“You’ll understand if you watch him. Just as I did.”

Mungyeong silently watched Jeok Cheongang’s back as he rose from the railing and shuffled away. Then he suddenly spoke.

“What is that brat doing right now?”

“Taekyung?”

Jeok Cheongang turned his head and laughed heartily beneath the moonlight.

“He’s sleeping like the dead.”

* * *

If training at Fire Gate Cavern had been a marathon, this was a short-distance relay.

During the little over a week it would take to reach Hubei, I decided to go back and forth between the modern world and Murim while maintaining two lives.

> **System**
>
> **Logout** complete!

I opened my eyes to the familiar chime. I was inside the private jet bound for Korea.

I saw people sleeping soundly from all the fatigue they had accumulated, along with one monster staring at me with his eyes wide open.

“What are you looking at, you punk?”

The Skeleton King answered.

“So that was what it was. Hmm. Do all humans sleep like the dead, just like you?”

“I’m special.”

“Not weird?”

*Whack!*

This bastard really went out of his way to get hit.
## Chapter artifact 439

# Chapter 439

*Smack!*

The Skeleton King’s body staggered after taking the blow straight to the forehead.

But only for a moment. He reset his head, which had been knocked upward by the impact, and grinned smugly.

“Heh heh. That barely tickled.”

“Oh, right. It looked so convincing that I got confused for a second.”

Whether it had a soul or not, there was no way an undead monster that was already dead could feel pain. Magic Johnson really had done one hell of a job with his full-body plastic surgery.

As I clicked my tongue softly, the Skeleton King shrugged.

“You must not treat this king as an equal to a weak human.”

“Of course I don’t treat you as an equal. You’re an undead monster.”

“An undead monster? This king is Stone-King, born and raised in Atlanta, Georgia, United States!”

“Hey, hey!”

What the hell was wrong with this lunatic? Why was he suddenly shouting?

I hurriedly raised my internal energy to block the sound, then let out a sigh of relief as I looked at the people sleeping soundly.

“You couldn’t even speak English properly to begin with.”

“I learned several things from the Internet. They said communication would not be a problem as long as I knew only two phrases.”

“Go ahead, then.”

Mr. Stone-King, a proud native of Atlanta, Georgia, United States, opened his mouth.

“How are you. I’m fine, thank you. And you?”

“…You’re Korean, aren’t you, you bastard?”

He had a Hollywood face, but his skill and pronunciation were pure homegrown Korea.

As I shook my head in disbelief, the Skeleton King asked with a shocked expression,

“Is this king’s English truly that terrible?”

“Yeah. So let’s just say you’re Korean mixed-race. It’s not like anyone’s going to be curious about your personal details anyway.”

“Then I was adopted by a family in Atlanta, Georgia…”

“No, for fuck’s sake. Did you hide honey in Atlanta? Is every treasure in the world supposed to be there?”

“But it sounds impressive, does it not? I read on the Internet that white men are popular with women all over the world. Besides, this king is handsome.”

“What good is that when you can’t even get it up?”

“……!”

The Skeleton King, who had been rendered speechless, pointed at me with a trembling finger.

“How could you say something so cruel?”

“I can say worse, so stop talking nonsense. If you don’t want people finding out you’re a monster, wear this around.”

The Skeleton King accepted the object I had summoned from my Inventory and tilted his head, forgetting his anger.

“Vile human, what is this?”

“A gift from Magic Johnson. He said it took a long time because he had to rush it over from the United States.”

“That gracious human? A ring for me?”

The Skeleton King stared at the ring I had given him with a serious expression.

“Is this perhaps what humans call a proposal?”

“What the hell are you talking about, you lunatic? It’s just a ring with translation magic on it.”

“Hmm. I appreciate the gift, but its appearance is rather crude. It does not sparkle like a diamond, either. It is unbefitting of a king’s dignity.”

“Magic Johnson commissioned a grand mage he knows to make it specially, so its performance is top-class. It’s probably worth whatever they ask for it.”

“Now that I look again, I can sense its noble dignity. It should be enough to establish a king’s authority.”

“……”

What an irritating bastard.

There was no doubt about it. He had become far stronger—and far crazier—than he had been as the Skeleton Warlord.

Regardless, he slipped the ring onto his middle finger with a satisfied expression, then pulled a smartphone from the lining of his suit.

That, too, was an expensive, cutting-edge smartphone with a Magic Gem built into it, another gift from Magic Johnson.

“What are you doing?”

“This king must personally express his gratitude to the gracious human.”

“You’ve got better manners than I expected. Are you going to send him a text?”

“Vile human.”

“Huh?”

The Skeleton King looked at me as though I were pathetic and said,

“Who sends texts in this day and age? Naturally, one uses social media.”

“…Uh, sure.”

“I have already followed him, and he has followed me back. I have also learned how to send direct messages.”

I stared at the screen of the Skeleton King’s smartphone, my mouth falling open.

Holy shit. It was real. An undead monster with a social media account. Did this app not even require identity verification?

But something else was even more surprising.

“…You have five thousand followers?”

“State the number accurately. It is 5,134. A record achieved in less than a week.”

“What the hell? Is this fake?”

“Is being handsome not the greatest advantage? I merely used this king’s face as my profile picture, and countless follow-for-follow requests came pouring in from around the world. Heh heh.”

The Skeleton King answered with an arrogant expression and began sending a message to Magic Johnson.

> Good human. I'm fine thank you. and you?

After checking the message, I let out a small sigh.

“Don’t send messages to anyone else.”

“Why not?”

“If I say don’t, then don’t, you bastard.”

So much for Atlanta, Georgia.

Calling himself a native of Atlanta District, Georgia City, Gyeonggi Province, would have sounded more believable.

Apparently, even translation magic could do nothing about English this painfully Korean.

“At this rate, even the Akabutakchi tribe, who have lived in the Amazon rainforest for hundreds of years while preserving their traditions, won’t believe you’re American.”

“Hmm. I do not know exactly what you mean, but the oddly specific nature of it makes me even angrier.”

“Just do as I say. If your identity gets exposed, things won’t end with a little trouble.”

No matter how good my current image was, if the Skeleton King’s identity became known, we would clearly have to brace ourselves for considerable repercussions.

I turned my head and asked,

“Isn’t that right, Team Leader Choi?”

In the seat diagonally beside us, Team Leader Choi had been awake by himself for several minutes. He answered,

“I was already considering the matter of the Skeleton King—”

“Stone-King. Call me Mr. King.”

The Skeleton King cut him off firmly. Team Leader Choi stared at him for a moment, then continued with a sigh.

“In any case, we are considering every possibility regarding Mr. King’s future. For now, it would be best to avoid exposure to the press and other media.”

“I refuse. I will reveal myself to the world with pride.”

“Really? Team Leader Choi, what are the penalties for an illegal immigrant entering the country?”

Team Leader Choi answered immediately.

“Deportation, without question. You would also have to expect a fine or imprisonment.”

“What about an illegal immigrant from the Demon Realm?”

“It has never happened before, but instead of the police, a large-scale raid team would be dispatched.”

“You heard him.”

The Skeleton King’s eyes darted around as he remained silent, but eventually he spoke.

“…It cannot be helped. The world is not yet prepared to accept this king, so I shall exercise restraint for a while.”

“That’s what you should do. Unless you want to spend the rest of your life lying low in my Inventory.”

“A-All right.”

The biggest headache was now dealt with.

Now there was the second headache to deal with… But this one was something I had no choice but to face head-on.

Not because I had no other options, but because it would help with my plans going forward.

*It’s a pain, but it can’t be helped.*

I quietly tapped the armrest, lost in thought, then suddenly spoke.

“What’s the atmosphere like back home right now?”

Team Leader Choi gave me a short, heavy answer.

“It’s insane.”

“…That bad?”

“When someone passes the judicial exam, banners are hung in the neighborhood where they live and at their alma mater, and a short article is printed in the local newspaper. More than 1,500 people pass that exam in a single year. How much more attention would there be for you, Mr. Jin Taekyung?”

Along with that perfectly fitting comparison, Team Leader Choi clicked in midair.

The holographic screen installed in the seat filled with countless online articles.

[At Last, He Has Returned.]

[Who Is Jin Taekyung? Chairman Xiao Yang bows his head on behalf of the Chinese people. The reverent farewell of S-rank Hunters…]

[The Young Hero Who Fought to Rescue Survivors Until the Very End Finally Returns to the Arms of His Homeland.]

It wasn’t just the Korean media. China, the center of the incident, and countries around the world were all flooding the Internet with article after article about my return and what I would do next.

I had known this was coming and expected it, but I couldn’t help gaping when I saw a photograph attached to an online article posted five minutes earlier.

“Wait. Are all those people actually human?”

“They aren’t monsters, so they probably are.”

“Oh, shit…”

The photograph attached to the article showed a crowd packed so tightly around Incheon Airport that there wasn’t a single gap to be seen.

Thousands? No, tens of thousands.

As I stared blankly at the screen, Team Leader Choi’s voice continued.

“Traffic in the surrounding area has come to a standstill, and a car parade is being prepared under military and police control.”

“What? A car parade?”

“Did I not tell you?”

“You mentioned it in passing, so I thought you were joking. No, but… isn’t this a bit much?”

Team Leader Choi shook his head firmly.

“It has to be this much. You are Korea’s new representative S-rank Hunter.”

“Even so, this is excessive. At this rate, the President will show up too.”

“Ah, I really did fail to mention that.”

“What?”

“He is coming. The Blue House contacted us first this morning. I meant to tell you on the plane, but I dozed off and forgot.”

For a moment, my thoughts ground to a halt.

Tens of thousands of people waiting for me at Incheon Airport. Paralyzed roads and a spectacular car parade. And now the President was coming, too.

I remained silent, unable to find the words, then forced out a voice.

“…Really? You’re not joking?”

“Yes. They want to shake your hand once, stand with you at the photo line, and take a picture together.”

“Team Leader Choi, I don’t know anything about politics. If I get dragged into something by mistake and a problem arises, I’ll be completely screwed.”

“I know what you think, Mr. Jin Taekyung. That is why I tried to turn them down politely, but they seemed quite determined as well. It was not easy.”

“You should have turned them down anyway. Even if I am a member of Peace Guild, how could you make that decision on your own?”

No matter how much we trusted each other or how little time there had been, this was something he should have consulted me about.

Team Leader Choi lowered his head apologetically at my stiff expression.

“I’m sorry. They offered several favorable conditions, including tax breaks, so I thought it would benefit you as well.”

“Forget that. Call them right now and tell them it’s off… Wait. Tax breaks?”

“Yes. You know about the bounty that was placed on the Arch Lich. If the Chinese government pays it to you, then under Korean law, it would count as foreign-source income for a Korean resident…”

“Wait. So how much tax would I have to pay in total?”

“I cannot say for certain, but it would be several trillion. The bounty alone is fifty trillion. Even if we simplify things and assume only ten percent is withheld, it would still be an enormous amount. Of course, the amount left over would be much larger.”

“…That’s true.”

“Once again, I apologize for failing to ask for your understanding. I will tell the Blue House that this is no longer happening.”

I nodded with my face set hard.

“Team Leader. This must never happen again.”

Right. I was about to get my hands on tens of trillions. Even if I paid my taxes properly and in full, I would still become incredibly wealthy.

No matter how insignificant the conditions they were offering might be, I couldn’t get involved with politicians just to save a little on taxes. That was something I needed to avoid.

*A few trillion? I can just pay it and be done with it.*

I cast my worries aside and leaned back against the soft seat.

* * *

*Boom! Boom-boom-boom!*

Incheon Airport. Hundreds of cameras flashed at the same time.

At the photo line prepared under strict security, two men from completely different professions were shaking hands with bright smiles.

“Mr. Jin Taekyung. You’ve truly been through a lot.”

“Oh, it was nothing. You’ve been busy too, Mr. President?”

And as the Skeleton King watched the scene, he thought,

*What a vile human.*

It was a brief assessment that included Team Leader Choi, who was smiling contentedly as though everything had gone according to plan.

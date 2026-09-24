# Checkpoint Review — 1000–1004

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

# Chapters 1000–1004

## Plot

Taekyung publicly accepts Song Il and Hwangbo Eom’s apologies, while making clear that trust requires honesty. The two elders set aside their lingering resentment and agree to fight Dark Heaven alongside the Jin Family; Gong Iljung explains that Zhongnan held back its main force to protect the sect. The groups travel west together, reaching Gansu with roughly a thousand people.

Near the Shaanxi–Gansu border, a Lower District Sect member admits he exaggerated rumors of nearby mounted bandits to move civilians out of danger. He reports strange activity among Ningxia’s mounted-bandit groups, which have since disappeared. The group learns that one unidentified master pacified Ningxia nearly ten years ago and is still there; the gangs later disbanded, with many former members becoming merchants, horse caravans, or escorts. The master’s identity remains unknown.

In Tianshui, Sama Pyo returns to his home region after more than a year away. Wolhwa’s sealed bamboo tube is delivered to Taekyung, and the group encounters an unexpected person. They then reach an eerily empty city, where Sima Gong and roughly a thousand Black Dragon Demon Gate disciples welcome them. After Taekyung tries to hide that he knocked Hyuk Mujin off his horse, he has Namho knock Mujin out again with jerky before they enter.

## Continuity

- Taekyung’s party has reached a city in Gansu where Sima Gong and roughly a thousand Black Dragon Demon Gate disciples are gathered. The streets are empty, with no visible battle or blood; Sima Gong says the civilians left of their own accord.
- Sima Gong is Sama Pyo’s father and is personally familiar with Jeok Cheongang; their exchange is openly contentious. Sama Pyo’s eyes sank as his father approached, for an unknown reason.
- Zhongnan’s party joined Taekyung’s group. Song Il and Hwangbo Eom agreed to fight alongside them, though their resentment remains.
- Zhongnan disciples stayed behind to escort villagers toward Shaanxi. The mounted-bandit rumor near the border was deliberately exaggerated to move civilians away from danger.
- Ningxia’s mounted-bandit groups showed strange activity before disappearing. They disbanded long ago, and their former members largely became merchants, horse caravans, or escorts. An unidentified, non-fiend Supreme Peak master who pacified them nearly ten years ago remains in Ningxia.
- Wolhwa sent Taekyung a sealed bamboo tube; its contents are unknown. Ju Hwaran watched it with a somber expression.
- Dark Heaven’s forces are advancing from beyond the desert; their destination and objective remain unknown, and multiple fronts are possible. Their army may rival or exceed the Hundred Thousand Demonic Disciples.
- The Demon-Sealing Formation may neutralize Dark Heaven’s Moving Formations; their number and locations remain unknown.

## Translation Decisions

- Render **마적단** as “mounted bandits.”
- Render **녕하성** as “Ningxia Province.”
- Use “Tianshui” for **천수** and “Land of Ruin” for **멸지**.
- Render **쇄월검진** as “Moon-Shattering Sword Formation.”
- Render Sima Gong’s **노선배** address to Jeok Cheongang as “Senior.”

## Durable state

{
  "active_continuity": [
    "Taekyung’s party has reached an occupied city where Sima Gong and roughly a thousand Black Dragon Demon Gate disciples are gathered; the streets are empty, with no visible battle or blood.",
    "Sima Gong is Sama Pyo’s father and has a familiar, openly contentious relationship with Jeok Cheongang.",
    "Taekyung noticed Sama Pyo’s eyes sink as his father approached."
  ],
  "continuity_sources": [
    1004
  ],
  "open_questions": [
    "Why did Sama Pyo’s eyes sink as his father approached?"
  ],
  "safe_through": 1004,
  "temporary_decisions": [],
  "version": 1
}

## Reading copies

## Chapter artifact 1000

# Chapter 1000

If the Roaring Fury Swordsman and the Taeeul Merciless Sword had shown even a hint of displeasure at that moment—or if they’d been unable to keep their itching hands still and started fiddling with their sword hilts—something serious might have happened.

Me aside, Jeok Cheongang was not the sort of man to stand by and let that happen.

And the Zhongnan Sect Leader, the Wind-and-Cloud Sword Lord Gong Pil—no, Gong Iljung—shared that concern.

—Tell me, Friend Jin. Are you just going to watch?

A low voice slipped into my ear through Sound Transmission.

At the same moment, Jeok Cheongang’s brow twitched as he sensed the sound waves.

“Is there anything we can do to earn your forgiveness?”

Everyone’s eyes widened. Mine included.

Why?

Simple.

Someone we never expected had said something we never expected to hear.

The Roaring Fury Swordsman, Song Il.

The arrogant old Daoist, a man whose pride went beyond mere stubbornness, had opened his tightly sealed lips and spoken the word *forgiveness*.

And the “we” he’d mentioned included another person, too.

“I’ve thought about it countless times over the past few months. About the mistakes I’ve made, and about what came of them.”

The Taeeul Merciless Sword, Hwangbo Eom.

Along with the Roaring Fury Swordsman, he was one of the Wind-and-Cloud Sword Lord’s only two Senior Brothers, and the highest-ranking member of the Zhongnan Sect. He looked at me as he continued.

“It was my fault. There’s no denying it.”

His gaze sank. His voice trembled.

I watched him in silence, then suddenly spoke.

“Did you mean what you just said?”

“You doubt my sincerity?”

“Of course not.”

I drew a deep breath before adding,

“I believe you. At the same time, I’ll put the unpleasant memories of the past behind me. I can’t say I was blameless in the trouble that happened that day, either.”

Everyone’s eyes widened at my calm reply. The people who knew me well were probably the most surprised.

Even I found the voice coming out of my mouth so unfamiliar that it felt like someone else’s.

But another voice slipped out at the same time—and that one was different.

It was the truth I couldn’t say aloud in front of everyone.

— I don’t believe you. No, I won’t believe you.

— …!

— If Great Hero Hwangbo truly regretted what he did, I can’t explain what we saw just a moment ago. I think you both know what I mean.

I sent the Sound Transmission and looked calmly at the Roaring Fury Swordsman and the Taeeul Merciless Sword.

Only moments had passed since they’d clenched their teeth and trembled with their fists balled tight. That wasn’t long enough to forget.

And yet it must have been a long, painful road for them to stand here on their own two feet.

*There’s still resentment. Of course there is.*

I wasn’t telling them to erase it completely.

People don’t change easily.

Not me. Not them.

But this was the moment to set aside the bad blood between us and move forward. Everyone knew that.

— What answer do you want from us?

— The truth. What you genuinely think—not something meant to be shown or said for someone else’s benefit.

— …!

— You don’t have to understand each other. But you have to acknowledge what you feel and accept the distance between you before you can join hands. I think you both know that already.

Silence that lasted too long would invite suspicion.

In the brief hush, the two old Daoists looked at each other, then clasped their hands toward us.

“I, Song Il, bow my head and apologize for the disrespect I showed the Jin Family of Taiyuan.”

“Please forgive me for forgetting my duty as a Daoist and putting the Yongbong Escort Bureau in danger. I promise to apologize again and make amends to the best of my ability.”

The Roaring Fury Swordsman bowed to me. The Taeeul Merciless Sword bowed to Ju Hwaran.

The Zhongnan Sect Disciples who witnessed the astonishing sight reacted in all sorts of ways.

Some bit their lips as if they were angry. Some wore faint smiles. Others couldn’t bear to watch their elders apologize to outsiders, so they closed their eyes as if they hadn’t seen it or turned away.

But most of them probably didn’t notice that the elders’ stiff, unpracticed bows hid the slight movement of their lips.

—Yes, you’re right. Bad blood doesn’t disappear so easily once it’s there. And I know that you, who say so, aren’t much different from us.

—But now is the time to gather our strength and face our great enemy. That is why we, as members of the great Zhongnan Sect and respected masters of the Murim, will fight for the world. Nothing more.

Their Sound Transmissions reached both my ears.

And if those were their genuine feelings, I had no reason to refuse.

Step.

For the first time since we’d come face-to-face with the Zhongnan Sect, I dismounted. Ju Hwaran followed my cue and set her feet on the ground.

Then?

We clasped our hands toward the two old Daoists.

As respectfully as anyone could.

Jeok Cheongang watched me in silence, a curious smile on his face. Then he shrugged at the Wind-and-Cloud Sword Lord.

“Let bygones be bygones. Right, Wind-and-Cloud Sword Lord Gong Iljung?”

The Wind-and-Cloud Sword Lord had looked like he’d just aged ten years. Now, as the situation came to a gentle close, he let out a sigh.

“Piljung. I’ve told you several times already, it’s Gong Piljung…”

“Gong Piljung? Wasn’t it Gong Iljung?”

“…?”

“…?”

“Ah.”

“What’s the problem?”

Only then did the Wind-and-Cloud Sword Lord realize something was off. He shook his head as if he’d seen a ghost.

* * *

The tense atmosphere had lasted only a little while at the start.

Once things had settled in a good direction, the Wind-and-Cloud Sword Lord—briefly thrown into confusion by Jeok Cheongang’s dazzling name-changing skill—was the first to bring up a subject.

“May I ask where you’re headed?”

Jeok Cheongang answered flatly.

“Of course not.”

“Pardon?”

“Ask someone else. I just tagged along as a guest. Someone else is in the presiding chair.”

Who was Jeok Cheongang? The Fire King himself.

He was also the head of the Five Kings Hall, newly established alongside the Murim Alliance. The idea that he was merely a guest was ridiculous.

But the Wind-and-Cloud Sword Lord quietly nodded and came over to me.

If Jeok Cheongang said so, then that was how it was. If he said otherwise, then it wasn’t.

As the leader of a great sect like the Zhongnan Sect, he took Jeok Cheongang’s answer to mean that his Master wanted to give his Disciple the authority to speak.

My thoughts were different, of course.

“Great Hero Jeok cares for you a great deal.”

“You must have bothered him quite a bit.”

“…?”

“He doesn’t like it when people he isn’t close to keep talking to him. Stay some distance away from him for the next half day or so.”

“…!”

“I’m telling you so you don’t misunderstand. I’m not joking.”

The Wind-and-Cloud Sword Lord looked back and forth between me and Jeok Cheongang as if he couldn’t believe what he was hearing, then replied awkwardly,

“Thank you for the kind advice.”

“Don’t mention it.”

“And as Sect Leader, I can’t say this in public, but I’m grateful to you for the other matter, too.”

The other matter.

It was a vague way to put it, but I had no trouble understanding him.

He was clearly thanking me, in his own way, for settling things peacefully with his two Senior Brothers.

“You don’t have to thank me. Honestly… the two of them were the ones who brought it up, and that helped resolve things.”

What would have happened if even the slightest killing intent had slipped from the Roaring Fury Swordsman or the Taeeul Merciless Sword?

Given the situation, it probably wouldn’t have turned into a massive bloodbath. But neither Jeok Cheongang nor I would have stood by and done nothing.

No matter how close Dark Heaven’s blade was to our throats, we couldn’t ignore a dagger coming at us from behind.

“Well, things are more or less settled for now, thanks to them. That’s a relief.”

“Mm. It surprised me, too. Though I doubt my Senior Brothers have entirely let go of their feelings.”

I looked at him in surprise. The Wind-and-Cloud Sword Lord gave a faint, wry laugh.

“What, did you think I wouldn’t know?”

“No. I just…”

“I joined Zhongnan when I was twelve. We served the same Master, and we’ve been together for well over fifty years. I know my Senior Brothers better than anyone. As their Junior Brother and as Sect Leader, I should say no more.”

From the sound of it, he’d cleaned up the mess his Senior Brothers made more than once.

I decided to settle the matter once and for all and spoke up.

“Is that why the reinforcements never really came?”

“…That’s a sharp question.”

“I just want to know what happened. I’m not accusing you.”

The Wind-and-Cloud Sword Lord let out a quiet sigh at my unwavering gaze.

“It wasn’t any one person’s fault. Even I didn’t dare send a large portion of our sect’s main force.”

“Meaning?”

“It was a decision made out of concern for Zhongnan’s safety. If that upset you and the Jin Family of Taiyuan, there was nothing to be done.”

Sometimes a direct, plain answer is the right one.

Like now.

I thought for a moment, then quietly nodded.

“What do you mean?”

“I mean I understand. Completely.”

“Then…”

“Isn’t it ridiculous to tell someone helping you what to do? We had enough reinforcements even without Zhongnan. I was only curious about the reason.”

“I see. Then is that enough?”

“Of course.”

I didn’t bother adding *for now*.

Nor did I bring up the bad blood between the Zhongnan Sect and the Nanman Beast Palace during the Great Faction War.

This was the best we could do at the moment.

Now was the time to look at the forest, not the branches. There was nothing to gain from falling out with the Zhongnan Sect.

*We need Zhongnan’s strength to face Dark Heaven’s army threatening the west.*

There were three Supreme Peak masters here alone.

And the Zhongnan Sect Disciples they led were clearly the elite of the main sect.

That meant they, too, intended to do everything they could in the great battle to come.

It was right to remember the bad blood of the past without constantly dredging it up.

I hoped this decision would lead everyone in a better direction.

That was the only way we could send the Fire Dragon Pavilion members back home in one piece after a short rest—one they were getting up from now, after days of marching without respite.

*Well, two of them are already on their way home.*

I was lost in thought, looking at Sama Pyo and Taishan, when the Wind-and-Cloud Sword Lord spoke.

“So, where are you headed? Qinghai, like the Huashan Sect that passed us earlier? Or…”

“Gansu. We’re going to Gansu.”

I’d been about to ask where the Zhongnan Sect was headed, but realized I didn’t need to.

The Wind-and-Cloud Sword Lord’s face had brightened considerably. That told me they were going the same way we were.
## Chapter artifact 1001

# Chapter 1001

Traveling with the Zhongnan Sect was decided all of a sudden.

Their Sect Leader, the Wind-and-Cloud Sword Lord, had proposed joining forces, and Jeok Cheongang had accepted before I could finish thinking it over.

“Traveling together, huh? That’s not a bad idea.”

“Old—no, Master.”

“What are you standing around for? Get your subordinates ready. And you too, Wind-and-Cloud Sword Lord—start by kicking those lazy disciples of yours in the ass.”

Just like that, all the preparations were finished in the blink of an eye.

Our party had swelled to around a thousand, rounding up a bit, and we set off toward Gansu. Among them were the Roaring Fury Swordsman and the Taeeul Merciless Sword, neither of whom looked particularly pleased.

“Those two have looked like they’re on their deathbeds for a while now. If we’d met them just six months earlier, no more, no less, I’d have cracked them across the jaw first thing.”

Jeok Cheongang smacked his lips as he muttered, and I clicked my tongue softly.

“If you couldn’t stand the sight of them, you shouldn’t have accepted the offer.”

“Is that why your lips are sticking out three inches?”

“Who said my lips were sticking out?”

“Correction. They’re sticking out four inches now.”

I shook my head at Jeok Cheongang’s teasing.

The one small upside was that we’d taken the rear, keeping a good thirty jang between us and the Zhongnan Sect. At least we could have this conversation without everyone hearing.

“Yes, I’m annoyed. Happy now?”

“Honestly, I can’t make heads or tails of you. If that’s how you feel, why bother making up when it was nothing but an empty gesture?”

An empty gesture.

There was no more and no less to it. It was exactly the right way to put it.

I’d already guessed that Jeok Cheongang had heard everything that had passed between us through Sound Transmission, so I answered without much surprise.

“Well, obviously…”

“Because we need to?”

“Right.”

“You make peace because you need to, then cover up old grudges with smiles, at least on the surface… You’ve grown up, haven’t you?”

There was something odd about his tone.

Not sure whether Jeok Cheongang was praising me or scolding me, I stared at him in silence. He gave a quiet laugh.

“Don’t overthink it. I’m just glad to see you’ve grown in one direction or another.”

“Do you think the direction you mentioned might be the wrong one?”

“Who can say? What matters is the outcome, doesn’t it?”

“Isn’t the process usually considered just as important as the outcome? Sometimes more important?”

“The first is what people say when they’re narrow-minded, and the second is bullshit people use when they’ve completely botched the outcome.”

Jeok Cheongang answered with cutting certainty, then went on.

“If I thought you’d done something wrong, I’d have given you a proper scolding. But so far, you haven’t done too badly. Besides, it might be nice to herd those lazy bastards all the way to Gansu like cattle.”

He wasn’t wrong. Even now, the Zhongnan Sect Disciples were running for their lives. It was all because of what Jeok Cheongang had declared before we set out, after unilaterally claiming the rear.

“From this moment until we reach Gansu, if any of you fall behind or try to slack off, this old man will personally have a private talk with you.”

A private lesson with an elder who’d reached a distant realm would be a fortuitous encounter anyone would pray for—unless the teacher was the Fire King. In that case, there was a good chance you’d become a dead man.

Whoosh, whoosh, whoosh!

Have you ever seen a pack of hyenas—or rather, Zhongnan Sect Disciples—race for their lives along a mountainside, desperate to survive?

I have.

Jeok Cheongang watched with satisfaction as the Zhongnan Sect Disciples ran with every last bit of strength they could squeeze out. Then, without warning, he kicked off the ground.

Boom! Whoooosh!

A sharp boom rang out as his figure stretched away in an instant.

Jeok Cheongang’s afterimage seemed to remain behind as he rapidly closed in. The Zhongnan Sect Disciples sucked in their breath, and panicked shouts rang out among them.

“Run!”

“If he catches us, we’re finished!”

“S-Senior Brother, I can’t go on. Don’t worry about this useless Junior Brother—just go on without me…”

“No! Don’t give up! We can survive!”

“……”

My thoughts on the scene were short and clear.

You’re all making a damn spectacle of yourselves.

“Anyone would think Dark Heaven had shown up or someth—huh?”

I clicked my tongue at the Zhongnan Sect Disciples fleeing like locusts from a wildfire. Then I spotted something and narrowed my eyes.

At the same time, I realized the real reason Jeok Cheongang had suddenly sped ahead.

*What’s that?*

We emerged from the narrow mountain path, and a hill opened up the view.

The problem was that, at the same time, a small village appeared in the distance, its hundred or so thatched cottages huddled together—and a crowd of people gathered around it.

At a glance, there had to be several hundred of them.

Hyuk Mujin, who’d spotted the crowd milling around the entrance to the little village a moment later, widened his eyes.

“Captain. Could that be…”

His urgent voice reached my ears.

Guessing what he was about to say, I answered a beat ahead of him.

“Don’t panic already. They don’t look like enemies.”

“Huh? Then…”

“They’re all civilians.”

I gave him a brief answer, thought for a moment, then added,

“At least, from what we can see right now.”

I added that because I wasn’t completely sure myself.

Judging by the route we’d taken, we were now somewhere along the border between Shaanxi and Gansu.

On top of that, Dark Heaven had the dark art known as the Moving Formation. It wouldn’t be all that surprising if we ran into people disguised as civilians here.

Dark Heaven had already disguised its people as government troops in Sichuan once before.

*If something had happened in Gansu, word would’ve reached us by now. So what’s this crowd doing in a tiny mountain village? Are they really preparing an ambush using a Moving Formation?*

Questions chased one another through my mind.

Then, all of a sudden, I heard a chilling sound.

Shing.

I turned and saw Sama Pyo. He’d drawn the Black Dragon Saber, the weapon that shared its name with his sobriquet.

“Whatever they are, there’s no harm in being prepared, is there, Pavilion Master?”

His voice was calm, but his eyes were dark and intent.

The closer we got to Gansu, the heavier the atmosphere around Sama Pyo had become. I quietly nodded and urged my horse on.

Thud, thud, thud, thud!

My grassland horse’s hooves thundered across the ground.

I didn’t know who the crowd waiting ahead of us really was, but one thing was certain.

*Even if Dark Heaven prepared an ambush, all we have to do is trample them and keep going.*

We might be headed into a fierce battle, but my heartbeat was no different from usual.

I’d become far too strong to be stopped in some mountain valley like this.

* * *

In the end, the disaster I’d feared never happened.

No—I should correct that.

It would be much more accurate to say that, at least for our side, it didn’t.

“They’re here! They’ve shown up!”

“Aaaah!”

“E-Everyone, get out of the way!”

It was only natural that urgent shouts and screams erupted all around us.

Nearly a thousand suspicious people came pouring over the steep hill, like water bursting through a broken embankment. Some of them already had gleaming blades in their hands. To the hundreds gathered around the entrance to the little village, it must have looked like a catastrophe.

At their very real reaction, the Wind-and-Cloud Sword Lord, racing at the head of the group alongside Jeok Cheongang, shouted like a thunderclap.

“Enough! Everyone, stop!”

Whoosh!

It was an order from none other than the Sect Leader.

At his shout, reinforced with internal energy, countless Zhongnan Sect Disciples quickly slowed and stopped where they were. But there were always exceptions.

Whoosh.

A faint rush of air, on a completely different trajectory from the rest.

Two figures shot forward like the wind, ignoring the Wind-and-Cloud Sword Lord’s command. I’d been slowing down along with the Zhongnan Sect Disciples, and I clicked my tongue to myself.

*Yeah. Somehow I knew they’d do that.*

They say old habits die hard for a reason.

The Roaring Fury Swordsman and the Taeeul Merciless Sword.

Those two old dogs kept going, disregarding the Wind-and-Cloud Sword Lord’s orders because he was their Junior Brother, Sect Leader or not. I kicked off the ground after them.

Whoosh!

A gale wrapped around me, and I covered dozens of jang in a single instant.

The backs of the two old Daoists, who hadn’t slowed their pace, came closer. So did the civilians’ screams.

And right then, one person’s voice reached the ears of everyone there, including me.

“Stop.”

“……!”

“……!”

It was a low voice, neither shouted with force nor backed by any particular internal energy.

But that one word was enough to stop the Roaring Fury Swordsman and the Taeeul Merciless Sword in their tracks.

More than anything, what mattered wasn’t what the word meant. It was who had said it.

“Are you deaf? You look useless enough already. Want me to rip one of your ears off while I’m at it?”

The Roaring Fury Swordsman had stopped only a few steps away from a civilian who stood frozen with his eyes squeezed shut. His face stiff, he began to speak.

“Senior, I was only trying to make sure…”

“Answer what I asked. Should I take it off or not?”

“……”

“I thought you were just deaf, but now it looks like your mouth’s been sealed shut too. Fine. You answer for your Senior Brother, who can’t manage it himself.”

Fire flickered in Jeok Cheongang’s eyes.

The Taeeul Merciless Sword met his gaze and bowed his head slightly.

“I only wanted to confirm who they were. I had no other intention. If my rash action upset you, Great Hero Jeok…”

“You didn’t upset me. You just made an even bigger mess.”

“I apologize.”

“At least one of you has a working mouth.”

Jeok Cheongang frowned at the Taeeul Merciless Sword, then let out a small sigh.

“Apologize to the people you scared half to death, not me.”

Just as Jeok Cheongang said, several civilians hadn’t managed to run away in time and were still trembling where they stood.

One man, who looked more or less all right, hurriedly waved his hands.

“Oh, it’s fine, sir. It all happened so suddenly that we were startled, but…”

The man trailed off as he looked at the Roaring Fury Swordsman and the Taeeul Merciless Sword, then shifted his gaze to Jeok Cheongang and me.

“Y-You’re… the heroes of the Murim Alliance, aren’t you?”

It was hard to call ourselves heroes after causing such a commotion, but I nodded anyway. The man’s expression—and those of the civilians around him—softened at once.

“Good grief. That took ten years off my life.”

“The Murim Alliance… Isn’t that the place fighting those wicked foreign invaders?”

“That’s right. There seems to have been a little misunderstanding.”

“Damn it. I thought we were done for.”

Just as sighs of relief rose from all sides, the man who’d spoken first brightened and continued.

“To think you’re the heroes of the Murim Alliance we’ve heard so much about. What a relief. We saw a bunch of strange-looking people show up and thought they were the ones… Whoops. There I go, running my mouth again. Calling you strange-looking…”

The man hurriedly clapped a hand over his mouth, but neither Jeok Cheongang nor I cared about that slip of the tongue.

Anyone could see they looked strange. More importantly, he’d said something else.

“Who did you think they were?”

The man answered without hesitation.

“Who else? That vicious gang of mounted bandits.”

What?
## Chapter artifact 1002

# Chapter 1002

“Who else would it be? Those vicious mounted bandits.”

The moment I heard the man’s answer, Jeok Cheongang and I reflexively looked at each other.

And for good reason. They were far too unexpected to show up at a time like this.

Mounted bandits.

Just what the name said: bandits on horseback.

Just as the Yangtze River Channel League had strongholds along every branch of the Yangtze, and the Green Forest Alliance had mountain strongholds on every mountainside with a road, mounted bandits could be found in regions with broad plateaus and plains.

*Pung Yang’s Red Wind Band had been one of them.*

The vast northern Great Steppe wasn’t home to nomads alone.

It was a refuge for all kinds of people who’d crossed the Great Wall—and, at the same time, their only place of rest.

And for those who could never return to the lives they’d left behind, there were two choices.

Eat or be eaten.

Naturally, most of them chose the former.

It was a hundred, a thousand times better to survive as a predator than to become prey.

Pung Yang had probably followed a similar path.

I had no idea how he’d come into possession of a Temporary Strength Pill or learned demonic martial arts worthy of being called a secret technique, but he’d proven himself a formidable predator.

He’d even had the nerve to lead hundreds of subordinates across the Great Wall.

But in the end, Pung Yang and the Red Wind Band had both met their end at the Mount Heng Sword Sect.

No matter how large they grew, they were still just a band of bandits.

Even in Shanxi Province, dismissed as a backwater compared with the Central Plains, there were clear limits to what a mere band of mounted bandits could do.

*And now a bunch of mounted bandits are hanging around here? Right on the border between Gansu and Shaanxi?*

Even the craziest bastards knew to check whether they had somewhere to lie down before stretching out their legs.

With the Kongtong Sect and the Black Dragon Demon Gate standing firm in Gansu, and Huashan and the Zhongnan Sect in Shaanxi, it made no sense for mounted bandits to swagger around here.

*Something’s going on. It has to be.*

Jeok Cheongang must have been thinking the same thing.

He was frowning in thought, so I spoke to the man for him.

“Could you tell us more about them?”

“You mean the mounted bandits?”

“Yes. Their exact location and numbers, if you know them. If not, even a rumor would be useful.”

The man had been blinking at us in silence, apparently picking up on the serious mood. Then he suddenly spoke.

“How much will you pay?”

“What?”

“Four silver nyang. That should be enough.”

“……?”

What was this guy’s deal all of a sudden?

Before I could come up with a reply, the man awkwardly scratched his cheek.

Or rather, he pretended to scratch it as he traced out letters on his cheek.

The name of someone who wasn’t here—but whom I could never forget.

*Wol…hwa. Wait. Wolhwa?*

I finally understood. My mouth fell open as the man—or rather, the Lower District Sect member—winked at me.

“You seem to be in a hurry to get where you’re going. Why don’t we talk on the way?”

“……!”

I’d almost forgotten.

The Lower District Sect’s eyes and ears were everywhere.

I let out a quiet laugh at the man’s shameless act, as though nothing had happened, then called out.

“Mujin.”

Hyuk Mujin came hurrying over and answered at once.

“Yes, Captain. What do you need?”

“Give this gentleman four silver nyang—no, ten. And provide him with a horse.”

I was turning away after delivering the order when Hyuk Mujin’s muttering reached my ears.

“You could at least toss him the money before saying that. And if you give him a horse, what am I supposed to ride?”

“……Ahem.”

“See? You heard me, but you’re pretending you didn’t. I’m so fed up, I ought to just quit—”

“Ahem!”

“Uh, what is it? Did you have another order for me?”

Hyuk Mujin’s eyes went wide and bright as if he’d never said a thing. I gave him a cold look and tossed him the money pouch I’d just taken out of my Inventory.

“Oh my, you really shouldn’t have. You can just deduct whatever you spend from my monthly pay, and if it’s not enough, I can ask my family for more. Or beg for it.”

“I’m… sorry.”

“What do you have to apologize for, Captain? Even if the pillars of the Hyuk Family Textile Shop start shaking, that’s my problem. Right?”

“I get it. Just stop already. That should cover it, right?”

“What about the horse?”

“……!”

“If you give away the horse too, what am I supposed to ride? My ancestors are dead—they’re not going to give me a lift.”

Out of answers, I quietly turned my head and looked at the nearby Zhongnan Sect Disciple.

More specifically, at the fine horse he was riding.

* * *

After the whirlwind shakedown was over, we got an outcome everyone could be satisfied with and set off toward Gansu Province again.

Of course, one Zhongnan Sect Disciple had to climb down from his comfortable saddle and travel on his own two sturdy legs. But that wasn’t my problem.

The only thing that mattered to me was the information the Lower District Sect member had.

“Everyone should stay around here for the time being. No—better yet, don’t come anywhere near. Head toward Shaanxi. Those vicious mounted bandits could attack at any moment.”

The Lower District Sect member repeated his warnings to the villagers who’d stayed behind, then mounted his horse. The Wind-and-Cloud Sword Lord left a dozen or so Disciples behind to help them, just in case danger arose, and lead them safely to Shaanxi.

As soon as we set off, the Lower District Sect member’s first words were enough to leave everyone feeling as if they’d been smacked in the back of the head.

“To be honest, there are no mounted bandits.”

“……?”

“……?”

After a brief silence, Hyuk Mujin fiddled with the sword at his waist and said,

“Ten silver nyang. Spit it back out right now, while I’m still asking nicely.”

“Enough! Hold your tongue! Threatening an ally—how are you any different from those demonic, heterodox villains?”

Jeok Cheongang sternly rebuked Hyuk Mujin, then turned to the Lower District Sect member, who was visibly frightened, and spoke with an unusually kind tone.

“Don’t mind that fool. Go on. Ten silver nyang is a small price to pay for your fare on the road to the afterlife.”

“…….”

God, he’s terrifying.

Just from listening to them, you’d think we were the Demonic Path Alliance, not the Murim Alliance.

The Lower District Sect member, who didn’t seem to have an ounce of internal energy, had gone pale from the pressure. He stammered out his explanation.

“To be precise, there were mounted bandits, but they’ve disappeared.”

“Oh? They were there, and now they’re gone.”

Jeok Cheongang let out an appreciative sound and smiled kindly.

“That makes perfect sense, given the situation. You’ll soon disappear from this world, too.”

“Eek!”

“I’ll take nine silver nyang. Keep one for the trip.”

“Gah!”

“Enough, all of you!”

Only after I stepped in did the people’s anger, which had been boiling like a cauldron over a charcoal fire, finally settle down. The poor Lower District Sect member hurriedly explained the details.

“So what you’re saying is, the mounted bandits in Ningxia Province really have started acting strangely?”

“Y-Yes.”

“Then all those people gathered in the village…”

“I deliberately spread an exaggerated rumor. Trouble is about to break out in the western region, so we wanted to keep the civilians from getting caught up in it as much as possible.”

“Dark Heaven is far away, but the mounted bandits are close?”

“Exactly. Ningxia Province is pretty close, so the mounted bandits there are a greater threat than Dark Heaven beyond the desert. All the more so for someone like me, who hasn’t learned martial arts.”

The Wind-and-Cloud Sword Lord had been riding alongside me. Now he frowned and cut in.

“Wait. Ningxia was once a lawless land ruled by mounted bandits, but weren’t they put down a long time ago?”

What was this now?

Everyone turned toward him at the unexpected information. The Wind-and-Cloud Sword Lord cleared his throat and continued.

“To start from the beginning, Ningxia used to be a longstanding headache for us. Hundreds of mounted-bandit groups, large and small, were spread across the region, to the point that even the government troops couldn’t control them.”

“If even the government troops wouldn’t step in, what happened to the civilians living in Ningxia Province?”

“Would any fish remain in a polluted stream? Most of the civilians either left or became one of them.”

“So it was no different from the steppe.”

“In practice, you could call it another steppe. Ningxia lies between Gansu and Shaanxi, but it was also the final destination for nomads who’d come down from the north and minority peoples who’d been driven out of the Central Plains. And the final touch among them all was…”

“Fugitives. People who came running after committing unforgivable crimes.”

Namho cut in, smoothly picking up where he’d left off.

“That’s why Ningxia had always been a prize the Murim sects of the Central Plains couldn’t quite bring themselves to claim. The land was small and barren, and the people left there were all sorts of vicious bastards. Even if a sect took losses securing the territory, dealing with it afterward would be another problem. Am I right?”

The Wind-and-Cloud Sword Lord clicked his tongue softly and nodded.

“I don’t like admitting it, but I can’t deny it. Before the Great Faction War, we could only watch one another. Afterward, we suffered such heavy losses that we had to focus entirely on recovering.”

I was starting to get the picture.

The Nine Sects and One Gang.

The Five Great Families.

They were symbols of the orthodox faction’s honor, but if you looked at the other side of the coin, they were also an entrenched ruling class that had monopolized power and influence for ages.

Even the Murong Family, which had recently brought about a bloodbath, had started harboring other ambitions partly because it had been treated as a foreign people and excluded during the fierce power struggles before the Great Faction War.

*Though, in the end, that’s nothing but an excuse from a traitor.*

I muttered inwardly, then asked the Wind-and-Cloud Sword Lord, who’d admitted the shameful truth with reddened cheeks, about the most important thing.

“But you said the mounted bandits in Ningxia Province were put down a long time ago. Which sect led that effort?”

The Wind-and-Cloud Sword Lord’s answer was truly unexpected.

“No one stepped forward.”

“What?”

“No, they couldn’t. Ningxia was already lawless, and not only our sect but every martial faction in the surrounding area had only just recovered from the aftermath of the Great Faction War.”

“Then how on earth…”

“I don’t know the details, but I heard that Ningxia Province was able to stabilize because of one person alone. That was nearly ten years ago.”

“……!”

Not a major sect like the Nine Sects and One Gang, but a single individual?

Everyone’s eyes widened at the answer they’d never expected.

Understandable.

From what we’d heard so far, Ningxia Province had once been a lawless land.

It was practically the Wild West of Murim. To have put down hundreds of mounted-bandit groups—

“A master, then. At least someone who’d reached the Supreme Peak realm.”

Jeok Cheongang had been listening in silence. He tossed out the brief remark, which matched my own thoughts exactly.

*A mysterious Supreme Peak master who swept away countless mounted bandits and pacified Ningxia Province ten years ago…*

That wasn’t the only suspicious thing.

The problem was that the mounted bandits in Ningxia Province had started acting strangely after remaining quiet for a whole decade—long enough for the mountains and rivers to change.

*What the hell is going on?*

I was frowning and silently urging my horse onward when a voice broke through the silence.

“Gansu. It’s Gansu!”

Four days had passed since we’d galloped without rest all the way from the Jin Family of Taiyuan.

Beyond the rugged mountain range, a vast plateau spread out before us.

Gansu.

No one could know whether the land before our eyes would become a place of death or a staging ground for another battlefield.

No one.
## Chapter artifact 1003

# Chapter 1003

At last, we realized we’d entered Gansu Province, and a strange tension began to settle over the group.

It was a reminder of why we’d come here.

And of the danger lurking somewhere in this land.

*How many of us will make it out alive?*

I quietly swallowed the thought that had suddenly crossed my mind.

The great battle about to break over us was unavoidable.

It was only a question of exactly when and where. One way or another, countless lives would be lost, and blood would flood the land.

If not Gansu, then Qinghai. If not Qinghai, then Tibet and Sichuan.

*Or it could break out on several fronts at once.*

If the information the Hidden Shadow Pavilion had obtained was true, Dark Heaven’s forces were drawing closer from beyond the desert. Their numbers were comparable to those of the Hundred Thousand Demonic Disciples—or greater.

That was an absolutely staggering army, so large it wouldn’t need to concentrate its forces on just one place.

*As numerous as the Hundred Thousand Demonic Disciples, even more dangerous, and on top of that, they have Moving Formations… This is going in the worst possible direction.*

Of course, with the Great Nation joining us, our own forces were formidable too. But there was no denying that our enemies had more options than we did.

And if even part of my vague suspicion was right, Dark Heaven wasn’t just a group held together by dark arts and fanaticism.

*It can’t be helped. The Murim Alliance leadership knows Dark Heaven’s strength as well as anyone. All I can do is trust them.*

I’d never once failed to give everything I had.

I’d survived one brush with death after another, defeated stronger opponents, and fought tooth and nail to prevent even greater disasters.

But even so, I couldn’t solve everything by myself.

This time was no different.

Just as they’d trusted me, I had to trust them, too.

One person was enough to light the fuse, but it took many people to deal with the aftermath of the explosion.

And so the thoughts that had circled through my mind came to an end, along with the mountain road.

Once we’d crossed the rugged range separating Shaanxi from Gansu, a completely different landscape appeared, as if someone had pulled away a layer of camouflage.

The high elevation and the cold air that came with it.

And beyond that, ocher-colored walls rising in the middle of a vast, open plain.

There was no mistaking the city that emerged through the sand-laden wind. It was Tianshui, on the eastern edge of Gansu Province, bordering Shaanxi.

“...Now that’s one hell of an atmosphere.”

Hyuk Mujin’s dubious remark might have spoken for all of us.

A bleak, desolate mood.

That was the first impression Gansu made on me—and, I suspected, on most of the others.

“Ugh, and what’s with this weather?”

Hyuk Mujin shivered in the chilly, dust-laden wind and pulled his collar closed.

And sure enough, even now, plenty of people were breathing out clouds of white.

There were exceptions, of course.

Those who’d reached the realm of being Unaffected by Cold and Heat through their formidable Supreme Peak martial arts, or Peak masters who couldn’t quite manage that but could use their internal energy to push back the cold.

And then there was…

“Taishan. Nice and cool!”

Right. One of them was from here to begin with.

Actually, make that two.

“It’s been a while, hasn’t it?”

At my sudden question, Sama Pyo, who’d been silently looking around, answered.

“Hard to say. It feels a little strange. I’ve only been gone for a little over a year, but… it feels like ten years have passed.”

A little over a year.

For some, that was a short time. For others, a long one.

And I could understand how Sama Pyo felt.

From the time the Murim Alliance had been reborn to where we were now, the year we’d spent together as members of the Fire Dragon Pavilion was far too short to hold all the moments of crisis we’d been through.

*Yeah. Has it really been that long already…?*

Like Sama Pyo and Taishan, returning to the place where they’d been born and raised, I was overcome with a strange feeling as I watched them.

When I looked back, so much had happened.

So many long, complicated events that we could talk for days without running out of things to say.

And through every one of those fierce moments, those two had always been at our side.

No—they were part of us.

Comrades bound together by the name of the Fire Dragon Pavilion, warriors who could trust each other with their backs.

Maybe that was why. My gaze had grown distant with memories of the past, and Sama Pyo seemed to feel something too. His eyes quivered as he looked at me.

“Pavilion Master. May I say something?”

“Sure. Anything.”

“I have no interest whatsoever in men.”

“...What?”

“I trust you don’t either, Pavilion Master, but one can never be too careful. I hope there’s no misunderstanding. I’ll be going now.”

“...!”

A moving moment, my ass.

I stared blankly after Sama Pyo as he hurriedly rode ahead, then sighed at the knowing look I felt from beside me.

“What? Got something to say?”

At my sharp, sudden question, the Lower District Sect member who’d been keeping pace beside me quickly shook his head.

“No, sir—well, actually, I do, but I’ll say it later.”

“...”

“...”

“Please say it now. Putting it off makes you look even more suspicious.”

“W-Would that be all right?”

“Oh, for the love of—”

The Lower District Sect member flinched at the sight of me scratching the back of my head, then glanced at me nervously and spoke.

“The mission I was assigned ends here.”

“Ends here…?”

“I was to evacuate the nearby residents and travelers, then inform Great Hero Jin of the recent events. Fortunately, we entered Gansu without incident, so I believe it’s time for me to turn back.”

“Turn back where?”

“Our sect and the Beggars’ Sect have disciples watching the western region in case something happens. I plan to deliver this news to our Branch Leader as quickly as possible.”

The Lower District Sect member before me belonged to the Shaanxi branch. Its Branch Leader was someone I knew well.

The proprietor of Honghwaru in Shanxi Province, and the first martial artist I’d met in this world.

“Give Wolhwa my regards—or, I mean, tell the Branch Leader I appreciate her looking out for us.”

“The Branch Leader is looking forward to seeing you again, too. She originally planned to come in person while you were passing through Shaanxi, but circumstances…”

The Lower District Sect member let his voice trail off, then reached into his robe and held something out to me.

“What’s this?”

“The Branch Leader told me to deliver it directly to Great Hero Jin. She kept emphasizing it—‘Make sure you do! You absolutely have to! Don’t forget!’”

The Lower District Sect member offered me a tightly sealed bamboo tube, then gave me a suggestive smile and flashed a thumbs-up.

“I have a great deal of respect for you, personally.”

“...All of a sudden?”

“Doesn’t seem all that sudden to me.”

I followed the Lower District Sect member’s roving gaze and turned my head. For some reason, Ju Hwaran was staring intently this way.

No, more precisely, she was gazing at the bamboo tube in my hand with a somber look in her eyes.

But only for a moment. As soon as our eyes met, Ju Hwaran naturally turned away and started talking to the people beside her.

It had happened so quickly that I almost wondered if I’d really seen it.

*What was that about?*

I blinked, then finally took the bamboo tube. Having completed the last task assigned to him, the Lower District Sect member began to ease his horse’s pace.

“I’ll be going, then. I wish you good fortune in battle.”

He clasped his hands in farewell and turned his horse to leave, when something I hadn’t dealt with yet flashed through my mind.

“Oh, wait. May I ask you one last favor?”

“What favor would that be?”

“I want to know everything happening in Qinghai and Gansu. Even the smallest sign would be useful. The sooner you can get it to us, the better.”

“You don’t need to worry about that. The Murim Alliance’s intelligence network has been active for quite some time. Information should already be reaching every nearby sect under emergency orders.”

I’d only added that out of caution. I wasn’t too worried about it.

The fact that the Hidden Shadow Pavilion had learned what was happening beyond the desert—a place even called the Land of Ruin—was proof enough that our intelligence network was wide-reaching and thorough.

Still, one thing was bothering me.

“Does that network include Ningxia Province?”

“You’re worried about those mounted bandits?”

“From what I’ve heard so far, it seems like I have reason to be.”

Of course I was.

One day, more than ten years ago, peace had suddenly descended upon a lawless land straight out of the American Wild West. And at the center of it all was an unidentified Supreme Peak master.

If there was even the slightest chance he was another hidden weapon Dark Heaven had planted across the world, then I’d have to consider turning my horse around right now.

*It’s bad enough trying to stop the enemy coming at us head-on. A two-front war would be the worst possible outcome.*

But contrary to my concerns, the Lower District Sect member smiled.

“It seems my explanation was lacking. I’ve only made you worry for nothing, Great Hero Jin.”

“What do you mean?”

“Though it’s a frontier region, it’s still part of the world. Our sect and several other intelligence groups have been keeping an eye on Ningxia Province for a long time. We watched even more closely after the trouble there ended at the hands of that unidentified master.”

“Ah.”

I’d let something slip my mind.

Information was money, and that wasn’t a rule limited to the modern world.

If anything, valuable information had to be even more precious in a world like this.

And the Lower District Sect was far less like a martial sect than the Beggars’ Sect, despite the two being regarded as similar. They were, in the truest sense, merchants who dealt exclusively in information.

There was no way they’d ignored the major incident in Ningxia Province.

Sure enough, the Lower District Sect member’s next words were so matter-of-fact that they made my worries seem misplaced.

“The mounted-bandit gangs in Ningxia Province disbanded long ago. Their most notorious leaders were all killed, and the rest didn’t dare resist. We’ve carefully gone over what happened back then and found nothing particularly suspicious.”

“Then what about the mounted bandits said to have appeared nearby?”

“Horse caravans. More precisely, caravans made up of people who used to be mounted bandits.”

Horse caravans.

People who wandered all over the land with their horses and the stars as their companions.

As both merchants and guides, horse caravans were also fixtures of their respective regions.

“So the disbanded mounted bandits became horse caravans.”

The Lower District Sect member nodded.

“They couldn’t remain mounted bandits forever. Some became horse caravans, while others formed merchant companies or Escort Bureaus. They adapted to suit the new age.”

“Then what about the Supreme Peak master who pacified the mounted bandits?”

“That’s the one thing we still can’t explain. We’re told he’s stayed in Ningxia Province ever since, but no one knows who he is, beyond the fact that he isn’t a fiend. Even our best informants have given up.”

If he wasn’t a fiend, then that left a recluse living deep in the mountains.

It wasn’t certain, but for now, his answer was enough to ease my mind.

The Lower District Sect member had just given me the answer I wanted, and he soon set off on his way.

When we reached Tianshui, we came face-to-face with someone we never expected to see.
## Chapter artifact 1004

# Chapter 1004

Everything in the world has its own atmosphere.

A distinctive feeling that clings not only to a person, but even to a place or an object.

Ordinary civilians have considerable trouble judging that atmosphere clearly, but martial artists are different. Years of life-or-death battles and grueling training have heightened their five senses.

Like Jeok Cheongang, who was looking at me right now with a deeply sunken gaze.

*Why?*

But before I could ask, the question that had surfaced in my mind quickly vanished.

The closer we came to the ocher-colored walls standing tall in the middle of the vast plain, the more I began to share Jeok Cheongang’s sense of things.

“Hmm.”

A low hum came from not far away.

I turned my head and met the gaze of the Wind-and-Cloud Sword Lord, who had been staring in our direction.

“You feel it too?”

“Yes.”

I nodded to him, then watched the walls drawing closer as the horses’ hooves thundered beneath us.

“It’s quiet. Too quiet.”

Anything in excess had poison hidden in it.

That was exactly the feeling coming from the small city, now barely a hundred *jang* away.

As in any other place, the Great Nation’s flag fluttered atop the walls, and beneath it stood a firmly shut iron gate.

But even setting aside the unusually desolate mood of the surroundings, something essential was missing.

*People.*

Civilians didn’t live only inside city walls. Some worked fields outside, and travelers passed along the roads.

Yet though the sun had not set, there were few signs of anyone.

No—not a single person was visible.

No people meant no noise, and that only made the place feel more desolate.

The Wind-and-Cloud Sword Lord wasn’t someone who’d fail to notice. His voice emerged between his lips, heavier than before.

“Do you think it could be a trap?”

I fell silent for a moment.

According to the information Wolhwa’s Lower District Sect member had brought us, the Murim Alliance already had a tight surveillance network throughout the western region.

Could the Murim Alliance really have failed to notice a city—not just a small village—being occupied?

Besides…

*It’s bleak, but that’s all.*

There were no visible signs of battle, and the wind slipping into my nostrils carried not a hint of blood.

How much flesh and bone had I cut through by now?

The thick, cloying stench of blood couldn’t disappear in just a day or two.

Even less so when I considered how much blood must have been spilled in taking an entire city.

*It’s not a trap.*

And just as I reached that conclusion after a brief moment’s thought, Sama Pyo rode up beside us and tossed out a single line that turned my guess into certainty.

“There’s no harm in continuing on as we are. Nothing’s going to happen anyway.”

His voice and eyes were completely calm.

At the sight of him, a thought suddenly crossed my mind.

“Could it be?”

“That’s right. It looks like they’ve prepared quite an extravagant welcome.”

Right then—

Rumble.

Several dozen *jang* ahead, the firmly shut iron gate began to slowly open.

As the enormous mass of iron, weighing over a thousand *geun*, parted, a middle-aged man with a cold expression appeared in the widening gap.

He was slender but sturdy, and though he was old enough to be nearing his twilight years, his neatly groomed hair was still jet-black, without a single white strand.

The sight of him called to mind, like a bolt of lightning, the epithet and name I’d heard only in stories.

*The Black Night King, Sima Gong.*

Sect Leader of the Black Dragon Demon Gate, a giant of the unorthodox faction who stood shoulder to shoulder with the Yangtze River Channel League and the Green Forest Alliance. Alongside the Kongtong Sect, he was one of the two powers that divided Gansu Province between them.

But at the same time I realized who he was, I also saw something else.

For some reason, the closer that man—his father—came, the deeper his son’s eyes sank.



* * *



“This lowly martial artist, Sima Gong, pays his respects to you, Senior.”

Sima Gong’s first greeting, offered to Jeok Cheongang, was more than polite. It was almost excessive.

All the more so considering his standing in the Murim and his not-inconsiderable age.

Of course, Jeok Cheongang didn’t care in the slightest.

“Save me the ‘lowly martial artist’ nonsense.”

He snorted so hard I worried a booger might fly out, then continued, looking at Sima Gong.

“Are you so desperate to seem young, or do you want to be young again?”

Sima Gong withdrew his clasped hands and straightened his back before answering.

“That wasn’t what I meant, but if I may speak despite the embarrassment, I suppose the answer is both.”

“Your silver tongue hasn’t changed.”

“Nor have you, Senior. Though your appearance has changed quite a lot.”

“Change the shell and the contents stay the same. And in that regard, your shell has grown quite impressive too.”

Jeok Cheongang paused and slowly surveyed the area.

More precisely, he looked over the streets, where not even a single rat could be seen, and the thousand or so men with swords filling the area around the city gate.

And not one of us could mistake the men in black martial uniforms for anything but disciples of the Black Dragon Demon Gate.

“You brought quite a crowd. Swarming around like a pack of dogs. Quite a sight.”

There was nothing but displeasure in Jeok Cheongang’s eyes and voice.

Ever since its founding over three hundred years ago, the Fire Gate Clan had walked the line between the orthodox and unorthodox factions. But if one had to choose, it leaned a little closer to the orthodox side.

The Black Night King Sima Gong and the Black Dragon Demon Gate he led, by contrast, carried on the orthodox tradition of demonic, heterodox arts.

And judging from the things I’d heard about Sima Gong in the time we’d spent together, Jeok Cheongang’s opinion of him had been poor ever since the Great Faction War.

“Things have been looking rather strange lately, so it came to this.”

“So you emptied your sect and came pouring over here in a crowd because things look strange? Stirring up innocent civilians in the process.”

“You seem to have misunderstood. Even with this many troops away, our sect’s defenses remain secure. The civilians left of their own accord. If they were frightened because of us, then there’s nothing we can do about that… but it isn’t necessarily a bad thing, is it?”

“What?”

As Jeok Cheongang narrowed his eyes, Sima Gong continued, wearing a gentle smile that seemed out of place on his cold face.

“I have no intention of being disrespectful to you, Senior. I only meant that, with this sense of danger hanging over them, the civilians would feel an even greater urgency to protect themselves. That, too, could be a way to save their lives.”

“……!”

By that point, I had to admit one thing.

*This guy can talk.*

He was exceptionally good at dressing up word games and sophistry to sound convincing, and at calming people down with just the right manner and smile.

On top of that, he had martial arts that could rival the two Alliance Leaders of the Yangtze and the Green Forest. That was probably the biggest reason the Black Dragon Demon Gate was what it was today.

*Is that what comes of being father and son? They definitely resemble each other in that regard. Sama Pyo was exactly like that when I first met him.*

Of course, that was in the past.

When I’d first met him, Sama Pyo had spoken and behaved like a slippery eel. But the longer we spent together, the more I realized he wasn’t actually all that talkative.

*Was “keep your outside and inside different” something his father taught him?*

I was thinking that as my gaze moved unconsciously between the father and son.

That was when Sima Gong and I met eyes.

“Well, well. So that’s the young man. The rare genius the Senior took in as a Disciple.”

His voice was directed at Jeok Cheongang, but his eyes, gleaming with interest, were fixed elsewhere.

It was already too late to pretend I hadn’t noticed his gaze and look away.

I glanced at Jeok Cheongang. He was looking at Sima Gong with a frown, but gave a nod.

“My name is Jin Taekyung, of the Jin Family of Taiyuan.”

“I know. How could I not? There’s hardly anyone in Gansu who hasn’t heard of your fame.”

It was the same tired pleasantry people in the Murim always exchanged when they met. But when someone said it with a smile, I was expected to give an answer in kind.

Especially since, aside from the fact that we were on the same side, the man before me was Sama Pyo’s father.

“You’re too kind. I’ve heard a great deal about your reputation too, Great Hero Sima.”

I clasped my hands and answered politely. Sima Gong smiled and looked at Jeok Cheongang.

“This is unexpected. I thought you hadn’t thought much of me for a long time, Senior.”

“Hadn’t thought much of you? Me?”

“Didn’t you?”

“Of course not.”

Well, even Jeok Cheongang couldn’t spit in the face of a smiling man.

I smiled warmly at Sima Gong as if to say, *See?* Just then, Jeok Cheongang continued.

“It’s not that I think poorly of you. I just don’t like you.”

“……”

“So I’ve talked behind your back a little.”

“……”

“Jin Taekyung there is lying through his teeth. ‘Your reputation’ my ass—what kind of bullshit is—”

*Whoosh. Thwack!*

“Gyaaaah!”

The faint sound of something cutting through the air was followed by a sudden scream that swallowed Jeok Cheongang’s voice.

*Clang! Clang! Clang!*

At the same time, dazzling flashes of swordlight sprang up in every direction, and shouts rang out.

“Prepare for battle!”

“The Black Dragon Demon Gate, prepare for an enemy attack!”

“By order of the Sect Leader! Zhongnan Disciples, form the Moon-Shattering Sword Formation at once! …What are you doing?”

The Wind-and-Cloud Sword Lord had been ordering his Disciples to form a sword formation, but his voice trailed off in bafflement. Only then did everyone realize something was strange. Following the Wind-and-Cloud Sword Lord’s gaze, they all looked toward one person.

A homely-looking guy who’d fallen from his saddle with a thunderous scream.

No, Hyuk Mujin.

“Ugh, what the hell was that all of a—”

He groaned and staggered to his feet, then froze like a statue.

At the center of countless gazes pouring down on him like a spotlight, Hyuk Mujin had been blinking silently. Then he belatedly spotted me, and the corners of his eyes twitched.

“Captain. That was you, wasn’t it?”

Everyone’s gaze naturally shifted.

Sima Gong’s eyes in particular were fixed on me. I did my best to keep my expression calm as I opened my mouth.

“Don’t misunderstand. I barely know him.”

Sima Gong asked Hyuk Mujin,

“Who are you? You don’t look like a Disciple of the Zhongnan Sect.”

“I’m Hyuk Mujin, of the Jin Family of Taiyuan.”

“So that’s what he says.”

*That idiot. He’s only ever oblivious at the worst possible times.*

*I should’ve knocked him out in one shot. Since when did that guy get so sturdy?*

I cursed myself inwardly for failing to hit him properly with the Finger Qi, then spoke.

“I know him a little. I didn’t say I didn’t know him at all.”

“So you do know him.”

“Hmm. I suppose I do.”

“Then what do you think caused that young man to suddenly scream and fall over?”

In the suffocating silence, I thought for a moment and came up with the best possible answer.

“He’s always been a bit sick. He has a condition.”

Hyuk Mujin’s mouth fell open. Maybe because the pain had stimulated his salivary glands, a translucent string of drool ran down his chin.

“See? He goes back and forth a few times a day. This sort of thing happens as often as he eats three meals—”

“Wow, you’re really going to do this? You’re seriously going to do this? You want to take it all the way?”

At this critical moment, I sent a discreet Sound Transmission over Hyuk Mujin’s shoulder.

To be precise, I sent it to a quick-witted Hidden Shadow Pavilion agent behind him, whose pupils were shaking in alarm.

*Now!*

Fortunately, Namho was different from Hyuk Mujin.

He moved with a speed and agility that belied his age, and with a stealth that matched, dropping the strip of jerky in his hand onto the crown of Hyuk Mujin’s head.

And that tempting piece of jerky was enough to stir the appetite of someone who’d been hungry for a whole *shichen*.

“Nooo! Jerky!”

*Whack!*

A palm as big as a cast-iron pot slammed down on the crown of his head. Hyuk Mujin promptly collapsed, and a deathly silence followed.

Until I, having barely dealt with the emergency, spoke up.

“Now, don’t mind him. Let’s all go inside.”

“……”

“……”

No, why are you all looking at me like I’m crazy?

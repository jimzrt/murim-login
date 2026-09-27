# Checkpoint Review — 1025–1029

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

# Chapters 1025–1029

## Plot

The Three Elders of Tianshan arrive as envoys for a new Demon Lord, bringing severed heads and offering to return some of their thousand captives if the defenders accept a meeting. Dark Heaven demands that Jin Taekyung attend an unarmed meeting with no more than three people, threatening to kill all the captives if its conditions are broken. Taekyung, Jeok Cheongang, and Sama Pyo go; Sima Gong and the Wind-and-Cloud Sword Lord stay behind.

Their approaching rider is the Blood-Sword Demon Lord, who admits he fears Taekyung might defeat the Lord of Heaven but refuses to explain when Dark Heaven or the Lord of Heaven emerged. When Taekyung and his companions charge, the Blood-Sword Demon Lord signals a strike, and roughly a thousand people are killed.

Taekyung reveals White Flame and immense dark-blue Force, reaching the realm of the Ten Kings as its eleventh giant. He wounds the First Elder; Taekyung kills the Second Elder, and Sama Pyo kills the Third. The First Elder survives, gravely injured. The Blood-Sword Demon Lord admires Taekyung’s cruelty and says he has long admired Jeok Cheongang for burning his attackers alive at Mount Jiuhua. As the armies converge at the Great Snow Mountain, Taekyung recognizes an arriving force of riders as Death Knights.

## Continuity

- The Blood-Sword Demon Lord once served the Heavenly Demon as a favored guard dog and now serves the Lord of Heaven. He killed Goyangcheon, the last survivor of the Goyang Family and former Spear King, and recalls killing the Heaven-Poison Demon Lord and the Hainan Sect Leader.
- The Blood-Sword Demon Lord refuses to say when Dark Heaven or the Lord of Heaven emerged. He says he fears Taekyung might defeat the Lord of Heaven.
- The meeting party was Taekyung, Jeok Cheongang, and Sama Pyo; the rest of their party remained with the defenders. The fate of the meeting party beyond the killings is unresolved.
- Roughly a thousand people were killed at the Blood-Sword Demon Lord’s signal. Who they were and what became of the remaining captives are unknown.
- Taekyung has reached the realm of the Ten Kings and is recognized by Jeok Cheongang as the eleventh giant.
- The First Elder of Tianshan is alive but gravely injured. Taekyung killed the Second Elder; Sama Pyo killed the Third.
- The Blood-Sword Demon Lord admires Jeok Cheongang for burning his attackers alive at Mount Jiuhua.
- A force identified by Taekyung as Death Knights has arrived as the armies converge at the Great Snow Mountain. What the Death Knights are and who commands them remain unknown.
- The Lord of Heaven’s identity and purpose remain unknown. Whether Dark Heaven caused the Great Faction War is also unresolved.

## Translation Decisions

- Render 구양천 as “Goyangcheon,” 구양세가 as “Goyang Family,” 천주 as “Lord of Heaven,” 신교 as “Divine Cult,” and 데스 나이트 as “Death Knights.”
- Retain “Blood-Sword Demon Lord,” “Three Elders of Tianshan,” and “realm of the Ten Kings.”

## Durable state

{
  "active_continuity": [
    "The Blood-Sword Demon Lord once served the Heavenly Demon as a favored guard dog and now serves the Lord of Heaven.",
    "The Blood-Sword Demon Lord killed a thousand people with a gesture and admires Jeok Cheongang for burning his attackers alive at Mount Jiuhua.",
    "Jin Taekyung has reached the realm of the Ten Kings and is recognized as its eleventh giant.",
    "The First Elder of the Three Elders of Tianshan is alive but gravely injured; Jin Taekyung killed the Second Elder, and Sama Pyo killed the Third.",
    "A force of riders identified by Taekyung as Death Knights has arrived as the armies converge at the Great Snow Mountain."
  ],
  "continuity_sources": [
    1028,
    1029
  ],
  "open_questions": [
    "When did Dark Heaven and the Lord of Heaven emerge, and did Dark Heaven cause the Great Faction War?",
    "Who were the thousand people killed by the Blood-Sword Demon Lord, and what became of the rest of the meeting party?",
    "What is the Lord of Heaven’s identity and purpose?",
    "What are the Death Knights, and who commands them?"
  ],
  "safe_through": 1029,
  "temporary_decisions": [],
  "version": 1
}

## Reading copies

## Chapter artifact 1025

# Chapter 1025

There were only a dozen or so of them, yet they stood out even among tens of thousands of enemies. Three things made that possible.

First, the white banner held high, as if to pierce the sky.

Second, the enormous black horse charging fiercely beneath it, its jet-black mane streaming behind it.

And third, the three old men at the head of the group.

*Who are those old men?*

They were too far away for me to make out even with Qi Sense, and yet instinct told me they were no ordinary people.

As I narrowed my eyes in silence, a deep rumble broke out among them. They had reached the foot of the mountain.

“Listen up, you dogs of the Murim Alliance!”

His voice carried across the mountain range, backed by profound internal energy.

At the shout of an old man whose shirt was soaked in blood, Jeok Cheongang looked at me and blinked.

“Well, that’s odd. I think this old man is hearing things.”

“I doubt it.”

“What? Then that lunatic really did tell us to get down and prostrate ourselves? To me, of all people?”

“He didn’t quite single you out, but you are with the Murim Alliance at the moment.”

“True. For now.”

“He called us dogs of the Murim Alliance, so I suppose that includes you. For now.”

“So this old man did hear correctly.”

Jeok Cheongang paused, thinking something over, then continued.

“Then answer me this. When some dog-boned nobodies from who-knows-where insult their Heaven-like Master, what should their one and only Disciple—or, well, someone more or less like one—do?”

“……”

If you’re a Disciple, you’re a Disciple. What’s this “someone more or less like one” business?

Jeok Cheongang was still stubbornly clinging to his act. I clicked my tongue softly and answered.

Not with words, but with action.

Whoosh. Tap.

“H-Huh?”

Leaving the martial artist behind, bewildered now that his hands were empty, I drew back the spear I’d borrowed from him as far as I could.

Though “borrowed” wasn’t quite the right word.

I wasn’t going to be able to return it.

My waist bent like a bow, my muscles tightened, and my joints relaxed in sequence, flowing into one smooth motion.

At the far end of the direction the spearhead pointed, a group stood beneath a white banner, still shouting.

“If you lay down your weapons and surrender right now—”

Whoosh!

The spear finally left my hand, tearing through the air.

It outran even its own fierce whistle, becoming a streak of light. The time it took to reach its target was no more than an instant.

Boom!

Bright red blood burst into the air.

The black horse, its body blown apart before it could even whinny, crumpled like a rotten tree. The old man who’d been energetically spewing that ridiculous bullshit landed nimbly on the ground.

*A Supreme Peak master.*

I’d suspected as much when he demonstrated enough internal energy for his voice to carry across the rugged mountain range. The old man, too, was more than worthy of being called superhuman.

Even at that distance, he’d managed to evade a spear thrown with overwhelming strength and speed without much difficulty.

And he wasn’t the only one among them with that level of skill.

“A rather rough welcome, young one.”

“Attacking first when we’re carrying a white banner? Has the code of the martial world you’re always going on about fallen so far?”

Two low but clear voices rang out.

Between countless bare branches, the other two old men stared straight at me.

“So it’s you. The young brat we’ve heard so much about.”

“Blazing Flame Divine Dragon Jin Taekyung, is that right?”

I answered them, sending my voice out with internal energy.

“No.”

“……?”

“……?”

“I’m kidding. It is.”

“……!”

“……!”

The two old men, who’d spoken as if they knew me, exchanged bewildered looks. So did the first old man—the one who’d just lost his means of transportation to my spear.

There were probably two reasons.

First, the young brat had started spouting nonsense out of nowhere.

Second, the young brat had eaten so much, and so well, that his nonsense carried an incredible amount of internal energy.

I had no intention of explaining to those senile old men exactly how much EXP I’d gobbled up by now.

I was only curious why they were urging us to surrender when they’d already smashed even Dunhuang with a force this powerful.

Of course, first I needed to find out what kind of dog-boned nobodies they were.

“Well, I’ve told you who I am. Since we’re here, shouldn’t we introduce ourselves? It’s that code of the martial world you mentioned.”

The old man in the middle, his face covered in pockmarks, answered without protest.

“A mere brat speaking to his elders like that? Fine. We’re the Three Elders of Tianshan.”

I widened my eyes.

“The Three Elders of Tianshan…!”

The second old man, fat and potbellied, nodded as if he’d expected that reaction.

“So you have heard of us after all.”

“My God. You’re the Three Elders of Tianshan?”

The third old man—the youngest of them, by the look of it, with a crown like a heaping bowl of rice—gave a short laugh.

“You must have heard plenty about us, given that our story has been passed down since before the Great Faction War. Are you finally ready to talk properly?”

I answered, feigning surprise.

“No.”

“You’ll regret it if you don’t listen now—what?”

“I said no. I only heard your title for the first time today. And stop calling yourselves ‘elders.’”

“What?”

“I figured you’d start blabbing on your own if I acted surprised. Oh, have you ever heard of the Three Elders of Tianshan?”

I turned to the living encyclopedia of Murim, Jeok Wiki, and soon got an answer.

“I’ve heard for years that three stray dogs wander around Tianshan.”

“Ah.”

“Maybe they were born dogs. During the Great Faction War, they sided with the Demonic Cult and caused every kind of hell in the Central Plains. This old man was itching to teach them a lesson.”

“And?”

“What do you mean, ‘and’? Why do you think they’re still breathing, even though I was determined to take them on?”

“You never ran into them on the battlefield.”

“Those natural-born bastards had good noses. They were so damn good at running that I never even caught a glimpse of their shadows.”

“Ah.”

I came to a conclusion after that brief exchange, then muttered as if to myself.

Loudly enough for everyone to hear, of course. I sent the words out with internal energy.

“So they were fucking pushovers.”

“……!”

“……!”

“……!”

The air around us quivered.

But unlike the enemies at the foot of the mountain, their anger simmering hot beneath the surface, the allies drawn up along the ridgeline reacted differently.

Who were the Three Elders of Tianshan?

Supreme Peak masters of a bygone era who had left their mark on the Great Faction War—fiends everyone had feared.

And here I was, looking down on them alongside Jeok Cheongang, calling them nothing but dogs. Pushovers.

Those outrageous insults and antics were more than enough to fill our allies with both surprise and relief.

*That was what I was aiming for.*

With a fierce battle about to begin, I’d not only provoked the enemy with a few words, but lifted our allies’ morale as well.

That alone wouldn’t turn the tide against such unfavorable odds, but momentum mattered more than anything.

Of course…

*If the Lord of Heaven is here, momentum won’t mean a damn thing.*

The new Heaven of the Hundred Thousand Demonic Disciples.

An evil so powerful its limits were impossible to fathom.

The corner of my mouth had curled upward for everyone to see, but the thought of that absolute being—someone I’d never even met—left a weight in my chest.

*If the Three Elders of Tianshan serve as nothing more than messengers, then who the hell is leading them?*

As though he’d read the question in my mind, the pockmarked old man, likely the eldest of the three, glared at us with a terrifying light in his eyes and spoke.

“No more need for idle talk. The Demon Lord wishes to see you.”

“……What?”

The Demon Lord?

I frowned and exchanged glances with Jeok Cheongang and the other leaders.

As everyone here knew, all the people who could be called Demon Lords were already dead.

The three who had represented the East, West, and North—and the Southern Heaven Demon Empress, who had finally met her end at the Nanman Beast Palace.

*But there’s another Demon Lord left?*

Were these bastards about to pull some cheap, ridiculous stunt like coming up with an East-and-West Demon Lord or a West-and-North Demon Empress?

Then someone suddenly came to mind.

*Could it be the Blood Lord?*

Had he filled the vacancy left by a coworker who’d been marked dead on the job?

The leaders were about to exchange a low murmur about the identity of the enemy commander when another shout rang out from the foot of the mountain.

“The Demon Lord says your safety will be guaranteed if you accept this offer!”

Dark Heaven, of all people, was guaranteeing our safety.

Naturally, it was complete bullshit.

The leaders and I both let out incredulous laughs at the absurd claim.

Then the Three Elders of Tianshan gestured. One of Dark Heaven’s martial artists following them pulled something from his saddle and handed it over.

Whoosh. Thud.

It soared high and landed halfway up the mountain. Our allies quickly carried it to the leaders.

Before I even opened the large, blood-soaked bundle, I knew what was inside.

So did everyone else.

Thump. Thud.

“Ugh…”

Dozens of severed heads rolled down with a series of heavy thuds. Groans broke out around us. Sima Gong spotted a familiar face among them and muttered under his breath.

“The Kongtong Sword Dragon.”

I’d never seen him, but I knew the title.

A direct Disciple of the Kongtong Sect Leader, and one of the finest young prodigies in the Central Plains, known as a member of the Ten Dragons and Phoenixes.

And… he was the very one said to have escaped Dunhuang alive alongside his Master.

“The two Perfected Ones who were Elders are here, too.”

“The Guardian Court Chief has also met his end. How could this have happened…?”

Not only those already presumed dead, but even those believed to have survived had come back as nothing more than severed heads.

And they had belonged to the core leadership of the Kongtong Sect.

“Then could it be…”

I couldn’t bring myself to finish. Wind-and-Cloud Sword Lord gravely shook his head.

“Fortunately, the Sect Leader seems to have escaped their grasp. Whether we should call that fortunate… I don’t know.”

The battle at Dunhuang hadn’t been the end.

There had been a relentless pursuit, and a horrific slaughter.

And now a new Demon Lord, one I’d never heard of, wanted to see us. For some reason, he’d sent the Three Elders of Tianshan to threaten us as well.

“A shame. If you were a little closer, I could see your faces properly.”

The three old men, who’d been furious only moments ago, chuckled and continued.

“You don’t think this is all we have, do you?”

Jeok Cheongang spoke in a low voice.

“What kind of bullshit is that?”

Perhaps the old fear of him had resurfaced. The Three Elders of Tianshan flinched at Jeok Cheongang’s presence, then answered with even more force in their voices.

“One thousand. There are still another thousand captives.”

“……!”

“If you accept the offer you were given earlier, we’re willing to return some of them.”

My mouth felt dry. Pain twisted through my stomach as I asked,

“And if we refuse?”

The three dogs laughed aloud.

“Want to find out?”

Damn it.

My answer had been all but decided.
## Chapter artifact 1026

# Chapter 1026

Their offer was as follows.

First: They would meet at a midpoint in half an hour, unarmed.

Second: No more than three people could attend.

And third…

*One of those three must be the Blazing Flame Divine Dragon, Jin Taekyung.*

I was recalling the terms I’d just heard, watching the Three Elders of Tianshan ride away, when Jeok Cheongang spoke.

“You’re staying behind.”

His voice was firm. He looked at me, his face set, and continued.

“Not this time.”

I shrugged.

“Well, that was a little different, but it worked.”

“What was?”

“I was about to say the same thing to you. That I think I have to go this time.”

“……!”

There was no other choice.

A thousand people.

They’d wagered a thousand lives without hesitation. This wasn’t some empty bluff to lure us down from the Great Snow Mountain.

Even now, a long line of prisoners, looking battered and miserable, was appearing on the distant hillside, bound together.

They had to be people captured at Dunhuang, or people who’d fled and been run down.

“You see them, right?”

Jeok Cheongang didn’t answer. I continued slowly.

“Not ten. Not a hundred. A thousand. We don’t have a choice.”

Before leaving, those three bastard dogs who’d spent their entire lives as outlaws had issued a stern warning, as if they were judges in a courtroom.

If we broke even one of their conditions, they’d kill every last prisoner.

And I didn’t want those people condemned to die.

“Honestly, I’m pretty damn scared too, but what can you do? I don’t know how much longer I’ll live, but… I don’t want to spend the rest of it losing sleep. So I have to go.”

Half joke, half serious.

When would I stop having nightmares?

I pushed the sudden thought aside, put on a smile, and spoke. Jeok Cheongang had been quiet for a long while. At last, he let out a sigh.

“You foolish brat.”

“Hey, what’s with that all of a sudden? You should be cursing those bastards, not me. Shameless bastards. They won big, and then they even worked hard at chasing everyone down.”

“Don’t pretend to be cheerful. It doesn’t suit you at all.”

“Is it that obvious?”

“You’re more shameless than anyone under heaven, but you’ve never been any good at lying.”

“……I guess not.”

“Even if there were only ten prisoners instead of ten thousand or a thousand, you’d still go. That’s the kind of person you are, as far as this old man knows.”

Would I really?

I didn’t know.

It was hard to be certain about a situation that hadn’t happened.

But… yeah. I probably would have.

And I thought Jeok Cheongang was that kind of person, too.

“You’re going, right? Even if I try to stop you?”

“Were you planning to?”

“No.”

I added, dead serious,

“If things go badly, we could be dead in a flash. You’d better stay by my side, Old Master.”

Only then did Jeok Cheongang let out a quiet laugh.

“So we die together, then?”

“What kind of grim talk is that? I mean we live together.”

“Same thing.”

“It’s not. One word can make all the difference. How can you say that? Keep it up and you’ll hurt my feelings. Don’t you feel my trust, hope, and love for you?”

“Your tongue is a river of eloquence whenever you start running it. But…”

Jeok Cheongang’s laughter faded. His voice dropped low.

“Do you think those men have the same trust you’re talking about?”

Instead of answering, I turned to look where Jeok Cheongang was looking.

A short distance away, the people we’d been discussing—no, the leaders—were approaching after finishing their deliberations.

Squish. Squish.

Dozens of footsteps pressed into the ground, turned to mud by snow and rain.

At their head, at the center of them all, was one man.

The Black Night King, Sima Gong.

“Have you made up your mind?”

For a moment, I stared at Sima Gong as he got straight to the point.

Then I answered.

“I made up my mind a long time ago. And so did the… no, my Master here.”

“You understand how dangerous this could be?”

“Of course.”

“Be careful. If they can draw in a major piece with just a thousand prisoners, it will be the best possible outcome for them.”

Every word was true.

As much as I hated to say it, Jeok Cheongang and I were Dark Heaven’s highest-priority targets for elimination.

After all the damage we’d done, we were enemies they’d like nothing more than to chew up and spit out.

But…

*Just a thousand, huh.*

No matter how you looked at it…

How could you talk so lightly about the immense weight of so many lives?

And how much did the outcome Dark Heaven wanted resemble the picture you were trying to paint? How sincere was that warning to be careful?

I swallowed the words circling the tip of my tongue. Then four characters suddenly came to mind, and I blurted them out.

“A large group is hard to kill.”[^1]

“Right… A large group doesn’t die easily. If you and Senior Jeok are going, you should be able to return safely even if it’s a trap.”

Sima Gong murmured the old Go proverb to himself, then nodded.

“I understand what you and Senior Jeok have decided.”

We’d made our intentions clear. Now it was time to hear theirs.

“Then who will the third person be?”

Three people could attend in all.

Jeok Cheongang and I were settled, but there was still one place open.

What happened next wasn’t far outside the range of what I’d been expecting.

“I’ll go. As Sect Leader of the Black Dragon Demon Gate, I’m willing to…”

“No. I’ll go.”

Two voices rang out almost at once.

Like a couple of middle-aged men arguing over who was going to pay at a bar, Sima Gong and the Wind-and-Cloud Sword Lord tried to stop each other.

“We don’t know what dangers lie ahead. Sect Leader, you should remain here.”

“Then all the more reason I must go. By that logic, I’m more suited to the task than Sect Leader Sima.”

As the Wind-and-Cloud Sword Lord argued, choosing him for the last spot made sense.

Sima Gong wasn’t merely the leader of one sect.

He was the beginning and end of the Black Dragon Demon Gate, and the heart and center of the Gansu Murim world.

If something went wrong and Sima Gong were harmed, the Black Dragon Demon Gate—or rather, the entire Gansu Murim force, which made up more than half of our current army—would be thrown into disarray.

The Wind-and-Cloud Sword Lord, on the other hand, was the Sect Leader of the Zhongnan Sect, but two of his Senior Brothers could fill his place.

The Roaring Fury Swordsman and the Taeeul Merciless Sword were both influential enough within the Zhongnan Sect, regardless of what kind of people they were.

So, in terms of the importance of the position and the danger involved, this was the choice that minimized the risk.

Of course…

*That only applies if you can be certain the people left behind are allies you can trust completely.*

Even if that was the sensible choice, why were we here if the world were governed by common sense?

The world sometimes changed because of a tiny handful of lunatics.

For better or worse.

*And one of those lunatics could take control of the rear while Jeok Cheongang, the Wind-and-Cloud Sword Lord, and I were away.*

But there was no time to argue based on an unease I couldn’t prove. We didn’t have that kind of time to spare.

*There’s no time.*

More than half of the promised half hour had already passed.

I met Jeok Cheongang’s eyes. I could tell we were thinking the same thing.

*If it comes to this, then…*

It would be better for just the two of us to go. Sima Gong wasn’t someone we could fully trust, wherever he was, and that was all the more reason the Wind-and-Cloud Sword Lord needed to stay behind.

I was about to tell everyone that.

No, I was about to.

Until someone no one expected suddenly spoke up.

Step.

“Forgive me for speaking out of turn, but may I respectfully ask you two to let me take the place?”

“……!”

In that moment, I saw it clearly.

As his son stepped forward, his footsteps ringing unusually loud, his father’s eyes sank into a deep, dark gaze.

“Please give me the last place.”

In a clear voice, Sama Pyo repeated himself to everyone.

“I’ll go.”

[^1]: The Korean word for a large group of stones in Go is also the word for cannabis, which sets up the wordplay in the childhood memory that follows.

* * *

Why?

Why had it turned out this way?

I didn’t know the exact reason.

All that mattered was that, at this moment, I was walking alongside Jeok Cheongang and Sama Pyo.

But my patience was just a little too thin to keep the questions building inside me to myself.

“Why’d you do it?”

I deliberately kept my gaze forward. Not long after I tossed out the question, a quiet answer came back.

“I don’t know what you mean.”

“Why’d you suddenly volunteer? Most of it was already decided.”

“If it had been decided, I wouldn’t be here. Would I?”

I furrowed my brow.

“Well…”

“No one wants to walk willingly into a deadly trap when they have no idea what might be waiting for them. Not even the Sect Leader of one of the Nine Sects and One Gang, whose reputation is built on honor.”

Sama Pyo added in a calm voice,

“His disciples would have wanted to prevent that at all costs. They wouldn’t want to send their Sect Leader to his death. Isn’t that right, Pavilion Master?”

I couldn’t argue.

He wasn’t making a guess or a supposition. He was just describing what had happened a few moments ago.

When Sama Pyo stepped forward at just the right time, the Zhongnan disciples had looked relieved and done everything they could to dissuade their Sect Leader. The leaders of the Gansu Murim forces had taken their chance, too, grabbing at Sima Gong’s sleeves.

If everyone left, who would be in command if something happened?

What would happen to all these people?

On top of that, Sama Pyo was both the Young Sect Leader of the Black Dragon Demon Gate and a member of the Fire Dragon Pavilion.

There were plenty of grounds for trying to stop him, but he was also qualified to step forward. Perhaps that was why everyone accepted the young man’s sudden move without much fuss.

Put simply, the situation had been arranged pretty neatly.

While everyone had been trying to read each other’s faces, waiting to see which leader would be left holding the bag, Sama Pyo had scratched exactly the itch they all had.

*Our people, of course, already knew that trying to stop us would be a waste of breath.*

The other Fire Dragon Pavilion members who were staying behind hadn’t tried to dissuade us either. They’d simply told us to come back safely.

Anyway.

Everyone had gotten what they wanted.

Well, almost everyone.

*Sima Gong.*

What was he thinking as he watched his son step forward so suddenly?

Had his eyes grown dark because he’d planned this from the start, or because he’d been caught off guard?

And…

*What the hell was this guy thinking when he volunteered?*

Even now, Sama Pyo hadn’t given me a proper answer to my question.

Instead, he suddenly brought up something that had nothing to do with the situation.

“By the way, I didn’t know you knew anything about Go.”

“What?”

“You said it earlier, Pavilion Master. That a large group is hard to kill.”

Was he changing the subject? Or trying to tell me something?

I couldn’t tell. So I answered calmly.

“I’m no expert. I don’t know much about Go. I just watched and listened from the sidelines when I was a kid.”

“Since you were a kid…”

“My dad liked Go.”

“I see. I’ve heard a little about the Strange Hero of Shanxi, your Family Head.”

“It’s been a long time since I saw him, but I still remember him vividly.”

Sima Gong had no idea.

He had no idea who I was talking about.

In this second life, I’d found brothers who weren’t related to me by blood, new companions and friends, and a Master. But I’d only ever had one father.

The kind of man who, whenever he lost at online Go, convinced himself that those Chinese bastards were using cheat programs, and who went all in on some major Korean electronics company’s stock while insisting it was a daema—a large group, hard to kill.

That was the kind of man he was.

*“Dad, why is the whole computer screen blue?”*

*“Son, what color is the sky?”*

*“Red.”*

*“No, that’s because of the sunset. The sky is blue. My stock’s only blue for a little while, too.”*

*“Really? So it’ll turn red soon?”*

*“Of course. This stock is a daema, you see.”*

*“Daema? Isn’t that bad? The stuff that makes you feel good?”*

*“What on earth are you doing at kindergarten… No, anyway, this isn’t that kind of daema. It means something really big and strong. And something this big and strong doesn’t die easily. In Go, we call it ‘a large group is hard to kill.’”*

*“Oh.”*

*“Once it happens, those lines on the screen will shoot way up. High into the sky, red like the sunset.”*

*“Hmm. I see. But, Dad.”*

*“Yeah?”*

*“Look at Mom’s face. It’s really red!”*

*“……Honey, when did you get here?”*

A quiet laugh escaped me.

Sama Pyo’s eyes widened.

I knew I shouldn’t laugh at a time like this, but I couldn’t hide the smile creeping onto my lips.

“It’s nothing. Just… just remembered something nice from a long time ago.”

“A nice memory with your father.”

Sama Pyo murmured as if to himself, then smiled along with me.

“I see.”

His smile was hazy and bitter, like the cloudy sky.

I felt a strange sense of déjà vu at the sight of him. That was when Jeok Cheongang, who had been silently leading the way, spoke.

“If you two are done laughing and chatting, we should greet our unwelcome guest.”

At that moment—

Clip-clop. Clip-clop.

With the slow sound of approaching hooves, they finally appeared.

No—*he* did.
## Chapter artifact 1027

# Chapter 1027

There are people who stand out.

Like an awl poking through a pocket. Like a reef rising from the middle of the sea. Like a wildflower blooming in the wilderness.

And right now, the man approaching with the leisurely air of someone admiring the scenery was one of them.

Clip-clop. Clip-clop.

Gray hair swayed with the slow rhythm of the horse’s hooves.

The middle-aged man had ordinary features—neither particularly handsome nor ugly—and pupils that were long and vertically slit.

But if there was one thing that made him stand out, it was his gaze: redder than flame, and infinitely more chilling.

“This is the first time we’ve met like this. It’s good to see you, Senior Jeok.”

The respectful address, the smile in his voice.

That was when it happened.

Jeok Cheongang’s pupils widened as he looked at the middle-aged man who had stopped a dozen or so yards away. More precisely, as he looked at those reptilian pupils.

“You can’t be…”

“We were both too busy to meet the last time. What a shame. If you’d been there, Goyangcheon would still be alive and well by now. Don’t you think?”

Goyangcheon.

A name I remembered from something Jeok Cheongang had told me once.

The Family Head of the Goyang Family, which had once wielded power to rival the Five Great Families—or rather, its last survivor.

After the Demonic Cult wiped out his family, Goyangcheon became a vengeful ghost. The world called him the Spear King, and that great martial artist was found one day in an empty field near the end of the Great Faction War.

He’d been cut into dozens of pieces, alongside the spear he’d considered an extension of himself.

Not by a hundred men, or a thousand. By a single person.

A killer who craved blood more than anyone in the Demonic Cult.

“The Blood-Sword Demon Lord…”

A low groan slipped out of me. The middle-aged man—the Blood-Sword Demon Lord—broke into a wide smile.

* * *

The infirmities of old age are a frightening thing.

Like a thief creeping in under cover of night, they steal away your memories one by one.

That was why, when I was staying at Mount Jiuhua, I deliberately pestered Jeok Cheongang with questions about his old memories.

To slow his illness, even if only a little. To delay the curse of time by even a moment.

In the end, it turned out to be a pretty good arrangement for both of us.

The old man, living alone with no one to talk to, recalled forgotten memories through our countless conversations. And the young man who kept him company picked up all kinds of information from the memories of a veteran martial artist who’d lived for more than a hundred years.

Among the things I’d learned was something about the killer who was now looking at me with a smile.

“I’m glad. You know who I am.”

The System I had couldn’t read other people’s minds.

But instinctively, I could feel it.

The Blood-Sword Demon Lord wasn’t merely saying he was glad I knew him. He was genuinely pleased.

There was a childlike innocence to it.

It was far too pure an emotion for a murderer who’d piled up horrific bloodshed. That only made it more unsettling.

“Still, I used to be somebody. These friends here were fairly famous, too, but from the Demonic Cult’s point of view, they were no more than useful guests.”

The Blood-Sword Demon Lord spoke with a beaming smile. The Three Elders of Tianshan, who might have felt insulted by the remark, only nodded stiffly.

“Y-You are right in every way, a hundred times over.”

“How could we ever presume to compare ourselves to the Demon Lord?”

“Though we are utterly lacking, being allowed to serve the Demon Lord is the honor of a lifetime.”

Their skill at kissing the Blood-Sword Demon Lord’s ass on cue was something else. I wanted to ask how many times a day they brushed their teeth if they kept at it like this, but when I thought about it, it was only natural from their perspective.

Might Makes Right. The strong rule.

Those called fiends were the ones who pursued strength more openly than anyone else, and the Blood-Sword Demon Lord was a great fiend beyond comparison to the Three Elders of Tianshan.

Of course, by the world’s standards, the Three Elders of Tianshan were great fiends, too.

Their individual martial prowess and the infamy they’d earned during the Great Faction War were enough to justify the title.

But as Jeok Cheongang had said to their faces half an hour ago, they were born stray dogs.

Just far more vicious, with sharper and stronger teeth than the other dogs.

Still, there was no comparing them to the one mad dog who stood out even among that insane cult of fanatics, a group that had stood shoulder to shoulder with the Murim world for more than a thousand years.

Of course, that mad dog seemed to serve a different master now.

“The Demonic Cult? Shouldn’t you call it the Divine Cult?”

At my sudden question, the Blood-Sword Demon Lord smiled. A moment ago, he’d been talking about the Three Elders as useful guests of the Demonic Cult.

“That was a long time ago. You know that already, so why ask now?”

“So, with a new collar on, do they feed you on time?”

“Goodness.”

The Blood-Sword Demon Lord widened his eyes in mock surprise and turned to Jeok Cheongang.

“Senior Jeok, how did you teach your Disciple? Whatever path we’ve taken, shouldn’t we still treat each other with respect? Like me.”

Jeok Cheongang answered calmly.

“I taught him better than your parents did, so don’t worry.”

The Blood-Sword Demon Lord stared blankly at Jeok Cheongang, then burst into laughter.

“Well, well. Just as the rumors said.”

“You’re worse than the rumors. I regret never catching and killing you when I had the chance.”

“I know your fiery temper well, Senior. Whenever you showed up on a battlefield, useful people died left and right. The Cult Leader was furious more than once.”

“Then you must have had a hard time, too. Weren’t you the Heavenly Demon’s most cherished guard dog, kept close at hand?”

“Sorry to disappoint you, but I didn’t have much trouble. I just killed as many as were dying.”

The Blood-Sword Demon Lord continued, his voice edged with laughter.

“When Heaven-Poison, that foolish old man, died, killing the Sect Leader of Hainan wasn’t enough. I had to bring back the Spear King’s head, too. But what could I do? I did it because I wanted to.”

“Heaven-Poison? You mean the Heaven-Poison Demon Lord?”

“Well, was there another Heaven-Poison?”

I knew the title Heaven-Poison Demon Lord, too.

The second-in-command of the Demonic Cult after the Heavenly Demon, he’d been an insurmountable wall even for Poison King Tang Sadok, the now-deceased Grand Family Head of the Sichuan Tang Clan.

One day, he’d encountered disciples of the Huashan Sect on a battlefield—and met his end that very day.

At the hands of someone who unleashed a brilliant purple Sword Force, bright enough to weigh down the sunset.

“The Sword Saint—though I suppose I should call him the Alliance Leader now? In any case, I was secretly grateful to Mae Jonghak. That old Heaven-Poison always looked at me strangely. Luckily, he died before it was too late, and things worked out well.”

I watched the Blood-Sword Demon Lord chatter away with a gleeful look. Then I frowned at the last thing he’d said.

*Things worked out well, thanks to him?*

The loss of a master meant a gap in one’s forces.

In that sense, the death of the Heaven-Poison Demon Lord must have been a tremendous blow to the Demonic Cult.

And yet he spoke as if…

“So that’s when you changed collars.”

At my blunt remark, the Blood-Sword Demon Lord furrowed his brow.

“‘Changed collars’ is a bit much… But think whatever you like.”

I already knew Dark Heaven had appeared before the Great Faction War was over.

The Head Elder of the Jin Family of Taiyuan, Baeksang of the Nanman Beast Palace, and even the Eastern Heaven Demon Lord, who’d been the Emperor’s closest confidant…

If you traced things back far enough, Dark Heaven had been taking shape from the very beginning of the Great Faction War.

No, perhaps…

*The Great Faction War itself might have begun because of Dark Heaven.*

A chill ran down my spine as I looked at the Blood-Sword Demon Lord and spoke.

“Just when did it begin?”

“When did what begin? I don’t know exactly what you mean.”

“When you all appeared. The Lord of Heaven.”

In that instant—

Whoosh!

The wind whipped up—a violent storm of energy.

The snow covering the ground, the frost, the dirt and sand buried beneath it all flew in every direction, then quickly settled.

Rustle.

As the debris of nature drifted back down, the Blood-Sword Demon Lord stared at me with a cold, sunken gaze.

“You have no manners. That’s for certain.”

The smile had vanished from his lips. His voice rang low.

It might have sounded calm at first, but cold lava flowed beneath it.

“How strange. I can understand you to a point, and yet I simply can’t understand you at all. Why would that person go out of their way to…”

The Blood-Sword Demon Lord let his words trail off, then smiled again with the good-natured expression of a man everyone liked.

“Well, there must be a reason for everything that person does. As always. I only wanted to confirm one thing.”

I didn’t need to ask what.

The Blood-Sword Demon Lord slowly raised a hand and continued.

“Blazing Flame Divine Dragon Jin Taekyung. You’re strong. Strong enough that I wouldn’t want to risk a bloody battle with you. Strong enough that I worry you might commit the blasphemy of defeating that person.”

I could see it. I could hear it.

The Blood-Sword Demon Lord’s eyes and voice, fixed on me.

And I could feel it, too.

The pure admiration in them.

And…

The faint killing intent hidden inside.

“I’m impressed by your limitless potential and your sense of justice. I mean that.”

“……!”

“……!”

“……!”

It all happened in an instant.

Me and Jeok Cheongang—and last, Sama Pyo, who’d been standing quietly in place.

The order and timing of our push off the ground and our charge differed, but the desperation driving us was probably the same.

Crack.

Our toes gouged the earth. Sand crumbled.

Internal energy surged from my dantian into the muscles of my tensed lower body, then exploded.

Boom!

The world slowed. The scenery shifted.

We shot forward, erasing a dozen yards of distance.

In that moment, Jeok Cheongang and I were two fierce streaks of flame, while Sama Pyo was a silent wind.

And in the slowed flow of time, three walls rose up to block the flame and the wind.

“Ha!”

Three voices, one shout.

The Three Elders of Tianshan.

The three fiends of Tianshan unleashed their pent-up fury and energy, wielding a power too great for anyone to dismiss them as mere stray dogs.

A coordinated technique, honed over ages of working together, merged the three walls into one enormous barrier.

Boom!

A single clash shook heaven and earth.

Amid that tremendous roar and the rippling waves of power that filled a time already split into fragments, the Blood-Sword Demon Lord’s hand, raised toward the sky, finally came down.

Like the countless blades on a hill, waiting for just one command.

“Slash!”

Shhk! Thud-thud-thud!

As a thousand or so heads rolled to the ground, my eyes met the Blood-Sword Demon Lord’s. I felt the blood in my entire body turn cold.

He was smiling.
## Chapter artifact 1028

# Chapter 1028

At that moment, the Blood-Sword Demon Lord was smiling.

The crescent curve of his eyes held nothing but pure delight and excitement. His long, vertically slit pupils trembled with anticipation for what was about to happen.

More precisely, with anticipation for one young man.

*Yes. That’s it. That’s exactly the look.*

Watching Jin Taekyung’s eyes widen with shock and fury, the Blood-Sword Demon Lord felt his heart pound.

He’d erased a thousand lives with a single gesture, yet he paid them no mind. All his senses were fixed on Jin Taekyung.

He felt not the slightest guilt for the dead, nor the slightest regret for breaking his promise.

He had been born in the Demonic Cult and raised in the Demonic Cult.

The cruelty he’d possessed since before he was born blossomed when it met the demonic martial arts he’d learned around the time he began to walk. Among the twenty-four great fiends under the Heavenly Demon, no one could compare to him.

Now, Jin Taekyung was the only thing that interested him.

The Divine Dragon of the Central Plains Murim, a rising star whom his master was watching closely.

The Blood-Sword Demon Lord wanted to see everything about that young brat.

He wanted to fully feel the martial prowess unleashed at his fingertips, the emotions pouring out of him, the special quality hidden within.

*Show me. Hurry!*

And just as the Blood-Sword Demon Lord cried out in his heart—

Whooosh!

An immense, unprecedented force surged up around one man.

“Who should I kill first?”

Jin Taekyung.

At the sight of the cold flames pouring from the young man’s eyes, the Blood-Sword Demon Lord’s smile deepened.

* * *

The first emotion the Three Elders of Tianshan felt was suspicion.

A spear was in Jin Taekyung’s hand—a spear that hadn’t been there moments ago.

*How?*

The promise had turned to dust, but one of the terms of their meeting had been to come unarmed. Jin Taekyung’s side had faithfully honored that condition.

So they had all come here empty-handed, which had been a considerable comfort to the Three Elders of Tianshan.

If they could handle the terrifying old monster called the Fire King, two young brats without weapons shouldn’t be much trouble.

Even if one of them was the renowned Blazing Flame Divine Dragon, Jin Taekyung, the three of them were fiends of a bygone age whose infamy had spread from Tianshan to the Central Plains.

From their perspective, it had been a fight they could win.

At least, until Jin Taekyung had a spear in his hand.

And until an immense power, far beyond their expectations, had enveloped that divine weapon, clearly made of Ten-Thousand-Year Cold Iron.

Rumble.

The dazzling white spearhead trembled.

No—the air around it shuddered in tiny ripples.

At the same time, a pure, immense force surged up around the spearhead, far too vast to fit inside the body of a young man who’d only passed his twentieth year a few years ago.

Ssssss.

What martial arts enthusiasts called Force was no longer a dazzling blue-white.

*This is…*

The three old men drew in a breath before they knew it.

What could they call this power?

The Force gathered at the spearhead was dark, like the deepest depths of the sea. Yet it also burned blue, like flames at their most intense, and flashed with the brilliance of a thunderbolt.

*It’s different.*

The Three Elders of Tianshan could feel it instinctively.

That energy was of a different kind, a different order, from the energy they had cultivated all their lives.

But they had no way of knowing what it truly was.

They didn’t know that the strange familiarity they felt in that moment came from the internal energy Jin Taekyung had received from the Heavenly Power Demon.

They didn’t know that the ominous power born of demonic martial arts had finally become one with the Fire Gate Clan’s hellfire and the Hebei Peng Family’s thunder.

And they didn’t know how immense and keen the power in that dark-blue streak of light was.

The only person who knew and understood all of this better than anyone else was standing beside Jin Taekyung.

*Oh.*

The Fire King, Jeok Cheongang, watched Jin Taekyung with a gaze sunk deep in thought.

He’d suspected as much. He simply hadn’t been able to confirm it for himself.

Ascending to the summit of perfection.

The young man who had reached the highest peak, touching the heavens, was no longer someone who could be judged by age or experience.

He was a great martial artist who had forged a path that belonged to him alone, not one followed by someone else before him.

Jeok Cheongang truly wanted to ask him:

Did he know just how remarkable the realm he’d attained was?

And he wanted to tell him:

Those who reached such a realm in all the Central Plains Murim were called this, with the world’s deepest respect.

The Ten Kings.

An endless sky and three stars.

Beneath them stood ten giants.

And today, right here, Jin Taekyung was proving himself.

He was the eleventh giant.

But unlike the heroes of the past, who had fallen to time or collapsed spilling their blood on the cold-blue blades of their enemies, he was a hero of a new age.

On this battlefield, where a thousand lives had faded, an immense blaze was rising.

*Truly, you shine.*

A shiver ran down Jeok Cheongang’s spine.

At the same time, as he looked at the Three Elders of Tianshan staring at Jin Taekyung in a daze, he saw the shadow of death slowly falling over them.

“Old Master.”

A quiet voice.

The call was thick with the pain of failing to stop so many deaths, and the fury born from it. Jeok Cheongang suddenly spoke.

“Do as you’ve decided.”

The Three Elders of Tianshan didn’t know.

They didn’t know those few, cryptic words were the trust and encouragement of a master to his Disciple, who was willing to risk his life.

Nor did they know that the brief exchange had sealed their fate.

Whoosh!

A sharp gust of wind swept through.

A dark-blue flash—impossible to tell whether it was flame, wave, or thunderbolt—distorted space as it came crashing down on them.

It was impossibly fast, and carried tremendous force.

Slash!

The First Elder’s whole body broke out in goose bumps. He had twisted away on instinct, but red blood and horrible pain spread across him.

“Gah!”

The flash flickered, and that was all.

If he hadn’t caught sight of a faint something at the last moment, his ghost would already have been wandering the Nine Springs.

*How—how can this be…!*

The First Elder gritted his teeth, barely holding back the pain and shock. Panic on his face, he clutched his deeply slashed chest and staggered backward.

If he retreated in the face of such speed and power, all that awaited him was death. But fortunately, he had two dependable sworn brothers.

“Elder Brother!”

“No!”

The Second and Third Elders cried out and charged. Each held a saber or sword, and their hands blurred as they swung toward a single target.

Jin Taekyung, who had rushed at them with the ghostlike movement of an assassin.

KWAANG!

One spear against two blades.

The three weapons, carrying several jiazi of internal energy, collided with a terrible roar that shook the surroundings.

The earth flipped. The air burst apart.

Amid a storm of power more violently turbulent than anything they’d ever felt, the two old men saw it clearly.

Jin Taekyung’s eyes, cold flames pouring from them—and his hand, gripping the spear shaft firmly without the slightest tremor, even against two Supreme Peak masters.

And he was holding the spear with only one hand.

“Wa—!”

Before they had the chance—or the time—to get out the two words *watch out*, Jin Taekyung struck the Third Elder in the chest with a palm.

*Ah.*

As his vision blurred, the Third Elder felt a horrible heat smash through his flesh and bones and burrow deep inside him.

Crack.

The sharp sound of breaking came late, seeming to echo from far away. Blood welled up in his mouth. As he crumpled, a familiar shout rang in his ears.

“You bastard!”

“Little Brother!”

No mistake. His elder brothers.

No matter how much the world had called them fiends and bastards, they had cherished him like brothers born of the same mother.

His teeth clacked.

The Third Elder bit his tongue hard and forced his collapsing body upright.

He couldn’t fall here. He hadn’t lived all this time to meet such an empty end.

Besides…

*We have the Demon Lord. We have his power.*

The Third Elder was certain.

By now, the Blood-Sword Demon Lord must have stepped in.

His mind was hazy, and he couldn’t see clearly, but with a single command from the Demon Lord, he could escape this terrible internal injury and pain.

But—

But why?

*Why can’t I feel anything?*

Even with his vision blurred, his senses as a Supreme Peak master remained. Yet as the Third Elder staggered and steadied himself, his Qi Sense told him everything was just as it had been.

Even as his two sworn brothers fought Jin Taekyung with all their might, the Blood-Sword Demon Lord’s presence remained a dozen or so yards away.

“Demon Lord! Demon Lord!”

Crash! Boom!

The roar erupting from the spearhead swallowed the Third Elder’s anguished cry. But the Blood-Sword Demon Lord couldn’t have failed to hear him.

And still, nothing changed.

No—that wasn’t quite true. Something did change.

Compared with the immense energies surging all around them, it was tiny—so tiny it crept in all the more stealthily.

Whoosh—thunk!

“……!”

The Third Elder’s body suddenly locked up.

He realized there was a cold blade through his back, with Saber Force gathered at its tip. He spun around in a flash and swung his arm.

Whoom—boom!

Compressed air exploded, but struck nothing.

As the Third Elder stared dumbly at the empty air he’d struck, someone’s form slowly came into focus.

Black clothes as dark as night, and calm eyes.

The young man looked barely thirty, yet his voice was astonishingly low and composed.

“You should always have watched your back. When you leave an opening like that, I can hardly just stand by.”

“You…!”

Crack.

The Third Elder bit down so hard his lips bled.

It wasn’t the Fire King, Jeok Cheongang. It wasn’t the Blazing Flame Divine Dragon, Jin Taekyung.

From the beginning until now, the young brat he’d paid no attention to had driven a dagger into his back—one he’d somehow kept hidden.

And he’d done it in a single surprise attack.

“And you still call yourself a man of the orthodox faction!”

At the Third Elder’s hollow shout, Sama Pyo shrugged.

“It’s all right. I’m from the unorthodox faction.”

“……!”

“And there’s one more thing I should tell you.”

Sama Pyo paused, then casually flicked his hand.

At the same time, another flash gleamed from the ample sleeve of his martial robe.

“I brought plenty of daggers.”

Whoosh!

A sharp whistle rang out, drowning out the quiet words that followed.

Watching the streak of light shoot straight toward him, the Third Elder couldn’t help sneering inwardly.

At least, until he realized he couldn’t move because of the terrible internal injury Jin Taekyung had dealt him, and the dagger just driven into his back.

*What is this…!*

Thwack!

The dagger pierced the center of his forehead. The Third Elder felt the world grow dark.

As his final memory, he heard Jeok Cheongang’s words, spoken as he watched it all.

“That’s one. No, two.”

The Third Elder, whose breath had already stopped, didn’t see it.

At the very moment his final breath left his body, the spearhead of White Flame, cloaked in dark-blue Force, sliced through the Second Elder’s throat.

Slash!

Beneath the fountain of blood, the First Elder’s eyes widened in horror as his body trembled.
## Chapter artifact 1029

# Chapter 1029

Tap. Patter-patter.

Hot and damp.

Blood that had shot high like a fountain was falling onto my head, soaking my scalp.

For someone already reduced to a headless corpse, it was a sensation they would never feel again.

> **System**
> Defeated Lv. 135 Gungongbo!
>
> Acquired a large amount of Fame.
>
> Acquired a large amount of EXP.

Splatter!

The body, losing its balance a moment later, crumpled onto the pool of blood.

The Second Elder’s head had been severed from his body before he’d had a chance to react. With a bewildered expression, it looked up at his sworn brothers.

Or, more precisely, the only sworn brother still in this world.

“One down. No—two.”

Jeok Cheongang’s timely words announced the Third Elder’s end. I turned to look and saw a silver blade sticking out of the back of the man sprawled like a rotten log.

Pssht.

Blood dripped in little spurts with a deflating hiss.

Sama Pyo was retrieving the dagger lodged between the Third Elder’s brows. When our eyes met, he shrugged.

“Did I do something I shouldn’t have?”

I answered.

“Yeah.”

“If he was yours to deal with, I’m sorry. I thought leaving him alive might cause trouble…”

“That’s not what I mean.”

A question crept into Sama Pyo’s gaze. I exhaled a breath as hot as a ball of fire and continued.

“You shouldn’t have killed him so easily.”

EXP didn’t matter. Neither did whose hand killed him.

He should have suffered more.

He shouldn’t have been allowed to leave this world so comfortably, in a single instant.

Like the Second Elder, whose collarbone had been torn away first, then one arm had been severed, and finally his Eight Extraordinary Meridians had been ripped to shreds before his head was cut off.

“Don’t step in again. Not one step.”

My voice sounded strange and desolate, as if it belonged to someone else.

I didn’t even know what I looked like right now.

But the grim, hardened expressions on Sama Pyo and Jeok Cheongang—and the First Elder, frozen as if face-to-face with a fiend—gave me some idea.

“M-monster…”

His body and voice trembled.

In the eyes of the old fiend who’d lost his two sworn brothers, the companions of his entire life, in the blink of an eye, I saw rage he couldn’t hide—and fear, even deeper and darker.

Splosh.

I took a slow step forward.

Maybe it was because the blood had soaked the ground. The sound of my footfall rang unusually loud, and the First Elder jumped and stumbled backward.

No—he dragged his rear backward, using both arms to brace himself.

With both knees already shattered, it was the only way he could get even a little farther from me.

“D-don’t come any closer! I said don’t!”

With a scream, the First Elder flung out his arms.

Boom!

I turned my head before I even heard the rush of air. The manifested palm force exploded through the space where my head had been a moment earlier.

Though he was already half-crippled, the powerful internal energy flowing deep within his body still burned like an inextinguishable flame.

Of course…

“Do it again.”

To my eyes, his movements were clumsy beyond words, hopelessly slow—and, because of that, full of openings.

“Aaaaaah!”

It was impossible to tell whether his cry was a scream or a battle shout.

Bang! Bang! Boom!

The First Elder, panicking out of his mind, unleashed palm force after palm force, making the compressed air burst.

The force of his frenzied attacks whipped my hair around and tore at my skin along with my collar.

And that was the First Elder’s final struggle.

Grab—crack!

I seized his wrist like lightning and twisted.

This wasn’t a grappling technique steeped in complex principles, or even a move powered by internal energy.

Just raw Strength and Agility.

That power and speed, far beyond the limits of a human being, made short work of frail flesh and bone.

“Ghk…!”

His face contorted with pain. A groan forced its way out.

But I knew.

If the old fiend in front of me were the sort to give up everything at a pain like this, the title of the Three Elders of Tianshan would have been forgotten long ago.

Whoosh! Crash!

Five fingers, curled like hooks, flashed down and struck the ground.

Just one step.

I read his movement and stepped back before he could act. His hand narrowly grazed my collar before plunging deep into the earth. I stomped on its back.

Crack!

The sensation of his bones shattering traveled up through my sole, the full weight of a thousand catties behind it.

His eyes, wide with unimaginable pain and terror, reflected my calm expression.

“Don’t look at me like that.”

Thud.

A precise blow to the jaw turned his head. Yellow teeth flew in every direction with the blood.

“When you look at me…”

Thud.

One more.

“Like that…”

Thud.

Again.

“I feel like killing you right now.”

Crack!

Sticky blood clung to my fist.

Gripping the hair of the First Elder, who no longer moved at all, I slowly straightened up.

“We’re only just getting started, aren’t we?”

I wasn’t talking to the First Elder.

I was speaking to the monster watching this whole scene from more than thirty yards away, his face alight with excitement—the one who’d cut a thousand people’s heads off with a single gesture.

Clap. Clap. Clap.

The Blood-Sword Demon Lord gazed at me with admiration, applauding slowly.

“Magnificent. No—beautiful.”

At his answer, it felt as though the blood in my body were turning cold.

Even now, with extreme rage ruling my mind, the man’s reaction was far beyond anything I could have expected.

“That’s how a Murim warrior should be. You have to crush your opponent, cruelly and completely. That’s what makes a real fight, don’t you think?”

The Blood-Sword Demon Lord was grinning from ear to ear.

Despite two of the Three Elders of Tianshan—important fighters and his own right hands—being dead, and the third crippled, he looked far happier than he had a moment ago.

“Crazy… bastard.”

“Me? Or you?”

“What?”

“Isn’t that right?”

The Blood-Sword Demon Lord blinked at me, then spun around with his arms spread wide.

“Look at me. My clothes are a bit drab, but compared to you, don’t I look positively mild-mannered?”

“……!”

“Ah, don’t misunderstand. I’m certainly not saying you look unpleasant. If anything, I find this rather familiar… It’s a good sight, in more ways than one.”

At the Blood-Sword Demon Lord’s satisfied smile, I suddenly felt short of breath.

He’d called it familiar. He’d called it a good sight.

The Blood-Sword Demon Lord, of all people. The old, vicious fiend.

Me, drenched in blood from head to toe.

Me, a moment ago, consumed not just by revenge but by the desire to inflict even greater pain.

“This… This is, I mean…”

“Enough.”

A voice I knew all too well cut me off, settled low in a way it rarely was.

“That’s enough.”

Jeok Cheongang strode forward. I suddenly wanted to ask him something.

Who was he speaking to?

Me? Or the Blood-Sword Demon Lord?

Or both of us?

But I didn’t ask. No—it was more accurate to say I couldn’t.

For a moment, I was afraid to ask whether I’d looked like a fiend mad with blood and revenge.

And yet, somehow, the one who helped me pull my stiffened body and mind back together was that very fiend.

“To interrupt us at a time like this, Senior—you’re too cruel. We were having a rather meaningful conversation.”

The Blood-Sword Demon Lord shook his head. Jeok Cheongang spat onto the ground.

“Fuck off. This old man never had a junior like you.”

“I know that, but I’ve admired you for a long time, so I can’t help myself. I’ll have to settle for an unrequited love.”

“Do I have to turn you into charcoal while you’re still alive to shut that mouth of yours?”

“Probably. To be honest, I was a little disappointed about that. I thought at least one of those three would end up like that.”

The Blood-Sword Demon Lord gave a showy sigh, then continued.

“You can’t imagine how excited I was when I heard what happened at Mount Jiuhua all those years ago. A descendant of the Fire Gate Clan I’d only ever heard about! When I heard those fools who dared lay a hand on you had all been reduced to ash, I was so delighted.”

“What did you say?”

“Isn’t that right? They burned alive—how much pain they must have felt. What could be a surer, more terrible revenge than that?”

“……!”

“Everyone else shuddered and called you a mad old man, but I didn’t. That was the day I started admiring you.”

At the Blood-Sword Demon Lord, his eyes shining like morning stars, Jeok Cheongang, I, and even Sama Pyo—all of us had been watching the situation calmly—seemed at a loss for words.

A fiend.

More than anyone I’d ever seen, the Blood-Sword Demon Lord was a lunatic worthy of the word.

Now I understood better than ever why the character for “blood” was in his title.

And to the Blood-Sword Demon Lord, the Three Elders of Tianshan were nothing more than livestock he’d kept nearby.

“Those idiots were the same. During the Great Faction War, they couldn’t run away fast enough whenever the battle turned against them. Then today, they stepped up without knowing their place, so they deserved to die… Ah, come to think of it, one of them’s still alive.”

Wheeze, wheeze.

“D-Demon Lord…”

The Blood-Sword Demon Lord glanced at the First Elder, who was still breathing faintly, then turned to me.

“I ask only out of concern, but are you thinking of letting him live?”

“Why do you ask?”

“He’s been bothering me for a while now. He’s neither alive nor dead… Wouldn’t it be best to make things definite?”

“……!”

“If you’re going to kill him, do it quickly. If you want him as a prisoner, have the young fellow beside you take him back. Though he doesn’t know much, so he won’t be of much use.”

The Blood-Sword Demon Lord gestured toward Sama Pyo, then smacked his lips.

“Ah, though I suppose there’s not much time for that now.”

Boom. Boom. Bwoom.

The war drums were drawing closer, growing louder and more resonant with each beat.

The Blood-Sword Demon Lord and us.

Behind each of us, the force of countless troops made the air tremble in every direction.

*Now it begins.*

I could feel it.

The blood-soaked battle for the Great Snow Mountain, the inescapable great war, had finally taken its first step.

And…

*I can end it right here.*

I couldn’t tell exactly how powerful the Blood-Sword Demon Lord was, but Jeok Cheongang and I should be enough.

Now that the Three Elders of Tianshan, a core part of their fighting strength, were gone, the balance of this battle had tipped heavily in our favor.

Surely.

Surely that was how it would go.

*Then why…*

Why had the Blood-Sword Demon Lord only watched?

Why had he treated such important fighters—three Supreme Peak masters—as if they were livestock?

*This is…*

The moment my thoughts reached that point, my eyes widened.

Whoosh!

Dark clouds had gathered at some point. A cold fiercer than the Great Snow Mountain’s own swept toward us, freezing the wind as it came.

And at the center of it all was a company of riders, rushing in like a dark, misty fog.

Sssaaaaa.

As I watched them surge forward with ghostlike movements, not a single thunder of hooves, I remembered.

The otherworldly beings who shouldn’t have appeared here, in the Murim.

“Death Knights…?”

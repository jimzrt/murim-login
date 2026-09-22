# Checkpoint Review — 715–719

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

# Chapters 715–719

## Plot

Jin Taekyung awakens after seven days, physically recovered but burdened by survivor’s guilt over the Inner Palace massacre. Jeok Cheongang urges him to mourn the dead without being consumed by guilt. The Fire Dragon Pavilion reunites around Jin, while Ju Hwaran forcefully keeps the group from disturbing him.

Nanman begins rebuilding its Inner and Outer Palaces. Yohi voluntarily enters the underground prison after repenting for aiding Baeksang, while the Beast Miao King disappears into a ruined shrine, overwhelmed by grief over Baeksang and the Nanman dead. Jin finds him and persuades him to resume his duty as Palace Lord and forest keeper. The Beast Miao King returns to the Inner Palace, where Jin bows before memorial tablets for Baeksang and Baekhwi.

The Beast Miao King later reveals that the sacred stone absorbed the rift’s demonic qi and became a corrupted divine artifact. He can suppress its demonic qi only temporarily. Jin accepts the System quest [Corrupted Divine Artifact] and rejects Jeok Cheongang’s proposal to destroy it, fearing that failure would release another catastrophe. He takes the artifact to Ailao Mountain’s Sacred Land, separate from the Poisonblood Grounds. Placing it there reveals a hidden radiant space and a brilliant pond, leading Jin to believe the artifact may be purified into a new sacred stone.

## Continuity

- Jin Taekyung has fully recovered after seven days and accepted the quest [Corrupted Divine Artifact].
- Jin continues to struggle with guilt over those killed during the Inner Palace disaster, though Jeok Cheongang believes surviving and overcoming that guilt will strengthen him.
- The Fire Dragon Pavilion members are alive and reunited in Nanman; Ju Hwaran is actively protecting Jin’s recovery.
- The System remains concealed from the Fire Dragon Pavilion; the surviving Baekcheon Unit members are expected to maintain secrecy.
- Yohi voluntarily entered the underground prison after siding with Baeksang and later repenting.
- Nanman’s Inner and Outer Palaces are being rebuilt, and Yayul Mok remains occupied with restoration.
- The Beast Miao King resumed leadership after grieving for Baeksang and the Nanman dead.
- Memorial tablets for Baeksang and Baekhwi were placed in the shrine.
- The former sacred stone absorbed the rift’s demonic qi and is now the corrupted divine artifact.
- The Beast Miao King can suppress the artifact’s demonic qi only temporarily.
- The Poisonblood Grounds and the Sacred Land are distinct locations; the Sacred Land is Nanman’s life-giving heart.
- The Sacred Land has revealed a hidden radiant space and brilliant pond around the artifact.
- Whether purification will succeed, produce a new sacred stone, or safely remove the demonic qi remains unresolved.

## Translation Decisions

- Retain **Old Master**, **Old Master Jeok**, **Fire King**, **Blood Monk**, **Flame Divine Palm**, **Force**, **Skill**, **Nanman Party**, and **Pavilion Master**.
- Render **대형** as **Big Brother** when used by the Seven Miao Tigers.
- Render **타락한 신물** as **Corrupted Divine Artifact**, distinct from **신석**, **sacred stone**.
- Render **마석** as **demonic stone** where applicable.
- Render **정화** as **Purification**.
- Preserve the distinction between **독혈지**, **Poisonblood Grounds**, and **성지**, **Sacred Land**.

## Durable state

{
  "active_continuity": [
    "Jin Taekyung has accepted the Quest [Corrupted Divine Artifact].",
    "The corrupted divine artifact is the former sacred stone, now consumed by demonic qi and still being suppressed by the Beast Miao King.",
    "The Beast Miao King cannot suppress the artifact's demonic qi indefinitely.",
    "Jeok Cheongang proposed destroying the artifact, but Jin Taekyung stopped him because a failed destruction could cause another catastrophe.",
    "The guardian spirit's sacrifice to close the rift motivates Jin Taekyung to prevent the artifact from exploding.",
    "The Poisonblood Grounds and the Sacred Land are separate places.",
    "The Sacred Land is Nanman's heart and a land of life.",
    "Placing the corrupted artifact at the Sacred Land revealed a hidden radiant space and a brilliant pond.",
    "Jin Taekyung believes purification may create a new sacred stone."
  ],
  "continuity_sources": [
    719
  ],
  "open_questions": [
    "Will purification at the Sacred Land successfully create a new sacred stone?",
    "What will happen to the corrupted artifact and its demonic qi during purification?"
  ],
  "safe_through": 719,
  "temporary_decisions": [
    "Render 타락한 신물 as Corrupted Divine Artifact and 신석 as sacred stone.",
    "Render 정화 as Purification.",
    "Keep 독혈지 as Poisonblood Grounds and 성지 as Sacred Land."
  ],
  "version": 1
}

## Reading copies

## Chapter artifact 715

# Chapter 715

A room filled with the smell of medicinal herbs.

A middle-aged man stood there, trembling as he held a long acupuncture needle in his hand, while Jeok Cheongang had him by the collar.

*This is going to be good. This is going to be good.*

Even though I had only just woken up, it was easy to understand what was happening. The middle-aged man I assumed was a physician spotted me blinking over Jeok Cheongang’s shoulder and shouted.

“Ah! Ahhh! He’s awake! He’s awake!”

“……”

Even my mother would have been less happy than that if she’d been here.

I guarantee it. That wasn’t the cheer of someone happy that a patient had woken up. It was the cheer of a victim who had spotted the police in front of a serial killer.

Jeok Cheongang let go of the physician’s collar without protest, then turned to look at me.

He said nothing for a long while, even after the physician hurriedly escaped.

Then he suddenly opened his mouth.

“You took your time waking up.”

His voice was gruff, so I shrugged.

I couldn’t exactly tell him that I’d had a fucking nightmare where Old Master had bitten my throat out.

“Did you sleep well?”

“More or less.”

“How do you feel?”

“Light. My head feels clear, too.”

That was the unvarnished truth. My body felt as light as a feather, and the long sleep had washed away the fatigue in my head, leaving me clearer than ever.

*They said I was unconscious for seven days and nights, didn’t they?*

I must have been more exhausted than I realized.

Not to brag, but it was rare for a master who had reached the Supreme Peak realm like me to remain unconscious for an entire week.

Then, without meaning to, I blurted out a single sentence.

“That’s a relief.”

“What is?”

“That this isn’t a dream.”

“……”

“It really is a relief.”

With eyes clouded by emotion, I looked around.

Sunlight streamed through the half-open window, while the chirping of birds tickled my ears. Far off, I could sense people passing by, chatting quietly among themselves.

*I’m alive.*

It was ironic.

Even while breathing through my mouth and nose, even while perceiving reality through my senses, I found it difficult to believe that I was alive.

At the same time, a hollow emptiness seized me.

For an instant, the darkness that had wrapped around the Inner Palace seemed to pass over the sunlight settling on the window. So did the sight of countless corpses collapsed with their faces buried in pools of blood.

*So… it really wasn’t a dream.*

The joy and relief of surviving scattered, replaced by guilt and bitterness.

I stared blankly at the window until a low voice pierced my ears.

“In the end, some survive, and some die.”

Tap.

I felt warmth from the hand resting on my shoulder. Jeok Cheongang continued while gazing into the distance.

“That is the irresistible order of things. That is the Murim.”

“……”

“Be grateful that you survived, and mourn those who died. For now, that is enough.”

Jeok Cheongang walked over to the window and threw it open. Bathed in the sunlight pouring inside, he stood there while I watched him in silence.

Along with the many thoughts flashing through my mind, my lips parted.

“Old Master.”

At my call, Jeok Cheongang gave me a warm smile and shook his head.

“Enough. Say nothing for now.”

“Ah, that’s not what I meant.”

“Enough, I said. There are many things I wish to ask you, but for now, you should first settle your mind—”

“No, it’s just that you’re dazzling me.”

“Hm?”

I cautiously pointed at Jeok Cheongang’s head. His bald head, gleaming in the sunlight, was using Solar Fist as a passive Skill.

“Either close the window or move your head a little.”

“……!”

“By the way, did you use Force? You shaved your head really cleanly. I understand the disguise, but you should’ve left some hair. What if it doesn’t grow back later?”

At that moment, the warm smile around Jeok Cheongang’s mouth vanished.

In an instant, Jeok Cheongang transformed from the kind old man next door into the Blood Monk. He stared at me with a look gone completely cold.

“You goddamn—”

“I was only asking you to do something. Why are you swearing at me? I just woke up.”

“Do you want to go back to sleep? Shall I let you sleep for the next three and a half months?”

Crack.

The bones in his tightly clenched fist shifted with an ominous sound. Realizing that something had gone terribly wrong, I hurriedly opened my mouth.

“I’ve already slept enough.”

“According to this old man’s judgment, you seem to want more.”

“I’m really fine. The work here is almost finished, so we should hurry back to the Central Plains—”

“It’s fine. Once you sleep and wake up this time, you’ll be in Henan at the very least.”

I swallowed hard.

“That sounds… really bad.”

“Why? The journey there will be boring anyway, won’t it?”

“It won’t be boring at all. I like admiring natural scenery.”

“What about returning to nature entirely?”

“……You’re joking, right?”

“Does it sound like a joke?”

“No.”

“What I just said was a joke. Waking up in Henan was not.”

Whoosh.

I saw flames winding around Jeok Cheongang’s fist and instinctively looked around, but naturally, there was no fire extinguisher in sight.

*I’m fucked. Shit.*

Having resigned myself to my fate, I made a polite request.

“Please go easy on me.”

“If you accept it obediently, that won’t be difficult. Which will you take—Flame Divine Palm or Flame-Extinguishing Divine Fist?”

“……Would either of those not hurt if you used them gently?”

“Then shall I hit you hard?”

“……Is there really no option besides Flame Divine Palm and Flame-Extinguishing Divine Fist?”

“There is.”

“Oh? What is it?”

“Dance of the Fire God and Demon.”

I asked in complete sincerity.

“Have you really gone senile?”

Whack!

My vision flashed white.

As I writhed with my mouth hanging open from the blinding pain racing across my forehead, Jeok Cheongang’s thoroughly gruff voice pierced my ears.

“I thought it was about time you woke up, so I stopped by for the first time in a while. And you’re perfectly fine. Stop spouting nonsense and take care of yourself. This old man is leaving.”

Click.

The door slammed shut just as I opened my eyes. Shedding a few tears as I rubbed my forehead, I looked at the empty space Jeok Cheongang had left behind and muttered.

“You could’ve stayed a little longer…”

Before that faint voice could even disperse into the air, I felt a tremor sweeping through the pavilion.

Boom. Boom. Rumble!

Surprisingly, it was someone’s footsteps. Beyond the tremor, which sounded like an elephant charging toward me, several other presences were also drawing closer, moving with uncanny lightness.

They were headed toward the firmly closed door Jeok Cheongang had just passed through.

“Hey, wait—!”

But my desperate shout never reached the end.

Crash!

The wooden door exploded outward, sending a cloud of dust billowing into the air.

As I stood there blankly frozen in the quarters that had become a ruin in an instant, I saw several familiar faces through the dust cloud and let out a helpless laugh.

*Yeah. Well, this isn’t so bad either.*

“How has everyone been?”

That sentence served as the signal. Several figures leaped toward me at once.

No—one enormous figure shot up high enough to reach the ceiling and crashed down on all of us, myself included.

Whoooosh!

“Taishan wanted to see the Pavilion Master!”

“……Ah.”

*You weren’t part of my calculations.*

* * *

Bang!

Hearing the tremendous crash behind him, Jeok Cheongang let out a quiet laugh.

“Well, what a commotion.”

It was obviously the work of that big fellow called Taishan—or was it Geosan?

The physician who had left the quarters first must already have spread the news. The members of the Fire Dragon Pavilion had rushed over faster than anyone else, barely sparing Jeok Cheongang a glance as they headed toward the pavilion. That had happened only moments ago.

*The youngsters want to spend time together, so this old man should step aside.*

There was one old man among them, but from Jeok Cheongang’s perspective, someone who had not yet reached eighty was still in the prime of youth. After all, Jeok Cheongang himself had passed ninety-nine long ago.

It was his firm belief that anyone eighty or younger could chew Ten-Thousand-Year Cold Iron.

*…That may be taking it a little far.*

After muttering inwardly, Jeok Cheongang began to walk slowly.

He looked up at the sky, which had cleared as though nothing had happened, and watched the Nanman people begin gathering in groups of three or five after hearing the news of Jin Taekyung.

Then, as he felt the cool breeze against his skin, he thought.

No. He silently posed a question to someone who was not there to hear it.

*Do you really think so?*

Jin Taekyung had regained consciousness after seven days and nights. He had said he was relieved that none of this was a dream. That it really was a relief.

But the voice and eyes of the person saying those words—and the Jin Taekyung Jeok Cheongang saw—did not seem that way at all.

*He was blaming himself. The self who survived. The self who failed to save them.*

No one knew what had become of the dead.

But Jeok Cheongang had watched countless people survive hell, and he knew that they continued living while carrying the weight of regret and guilt.

The Great Faction War.

Jeok Cheongang had also been there during that eternity of blood and death.

*But once you overcome it, you grow stronger.*

That was why he had chosen his words as sparingly as possible. Even while pretending not to notice Jin Taekyung groaning and thrashing in pain while unconscious, he had forced himself to ask.

*Did you sleep well?*

*More or less.*

It had surely been a terrible nightmare. But Jin Taekyung had lied through his teeth with a perfectly straight face.

*What a cheeky brat.*

Jeok Cheongang was not angry.

He was proud of the way Jin Taekyung was trying to endure it somehow, but at the same time, he felt bitter.

That was all. Nothing more.

So why did something in his chest still ache? Why did Jin Taekyung’s figure keep wavering before his eyes even as he looked at the world around him?

*Damn it. This old man really is getting old.*

And yet, for some reason, he did not dislike himself like this.

He had witnessed that mysterious recovery with his own eyes, but it was Jin Taekyung—not anything else—who filled his heart.

*Well, this isn’t bad either.*

Jeok Cheongang gave a faint laugh and walked toward a quiet place. Sunlight filtering through the leaves shone on his bare, gleaming head.

* * *

“Captain.”

“What?”

“Captain.”

“Ah, what?”

“Captaiiin!”

“Stop calling me, you bastard. I’m not dead yet.”

Despite my shouting, Hyuk Mujin continued to sound as though he was about to cry.

Instead, he clutched my sleeve tightly with both hands and asked with his wet, glistening eyes,

“Then when are you going to pass away?”

“……Are you insane? At this point, you’re practically chanting for me to die.”

“You were unconscious for seven whole days and nights. I really thought you were going to pass away.”

Taishan, who was diligently scrubbing the floor under my direct orders, promptly nodded.

“That’s right. Taishan thought the Pavilion Master would never wake up and was looking forward to it.”

I was just beginning to feel touched when I noticed that something was wrong and blinked.

“Looking forward to it? Why would you look forward to that?”

Namho, who had claimed the only chair under the pretext of his age, muttered,

“Why ask? That son of a bitch was looking forward to the funeral feast.”

“No! Taishan worried whenever he thought about the Pavilion Master, so he drooled!”

“……”

“……”

That bastard really must have been looking forward to it.

Sama Pyo, who was practically Taishan’s mother, met my eyes and lowered his head weakly.

“Pretend you didn’t hear that. I have nothing to say for myself, even if I had ten mouths.”

“Ten mouths? If Taishan had ten mouths, then—!”

“He’d eat ten times more. Please, can someone put a muzzle on that bastard?”

At that moment, Assemblyman Namho of the Nanman Party formally introduced the Taishan Muzzle Bill, and the sound of something cutting through the air came from somewhere.

Whoosh—crash!

The table that had somehow managed to keep its shape in the ruined quarters was crushed in a single blow.

At the same time, a cold voice slipped between someone’s lips.

“What… are you all doing in front of a patient?”

Everyone clamped their mouths shut at Ju Hwaran’s remark, delivered after she had smashed the furniture in front of the patient.
## Chapter artifact 716

# Chapter 716

They say that when someone who is usually quiet gets angry, they become even more frightening.

That was Ju Hwaran right now.

*Crack.*

Wooden fragments spilled from the hands of the Yongbong Escort Bureau’s precious jewel—the human air purifier who had been ventilating this jalapeño pepper party, which not only reeked of old-man funk but had become downright spicy.

Her usually gentle eyes and voice had grown as sharp as thorns.

“Young Hero Taishan.”

Taishan, her first target, flinched.

“Do you have any idea how much the Pavilion Master—Young Master Jin—has gone through for us? How can you say something like that?”

“Taishan was wrong.”

“No matter how strong your appetite is, that’s going too far. If you say anything ominous one more time, I’ll really put a muzzle on you, just like Elder Namho said.”

At Ju Hwaran’s stern warning, Sama Pyo narrowed his brows and opened his mouth.

“Young Lady Ju, Taishan isn’t a beast.”

“Then should I put a muzzle on you instead of Young Hero Taishan?”

“……”

“Well?”

Sama Pyo thought for a moment, then spoke with a serious expression.

“Come to think of it, putting a muzzle on him occasionally for dietary management might not be a bad idea.”

“Be careful from now on. I know you don’t mean any harm, but that was too much.”

“……Understood. I’ll make sure to correct him.”

As the muzzle bill he had proposed narrowly failed to pass, Namho muttered in a sorrowful voice,

“I have to see that bastard muzzled before I die……”

But even Namho couldn’t avoid becoming Ju Hwaran’s target.

“Elder Namho.”

“Huh? What?”

“If you’re an elder, you should act like one. It’s not a good look to curse so harshly in front of a patient who hasn’t even fully recovered yet.”

“What? Patient?”

Namho looked at my face, which gleamed with health after a massive series of level-ups and all that rest, and made a dubious expression.

“No, put that aside for a moment. Where is there a bigger foulmouth than Jin Taekyung? Why are you suddenly coming after me—”

*Tap.*

At that moment, I saw it clearly.

Just as Namho was about to continue in an aggrieved voice, Hyuk Mujin, who was sitting beside him, discreetly jabbed him in the ribs with his elbow.

If I were to reinterpret the meaning behind that small gesture in modern terms, it would be this:

*‘Don’t ruin the mood. Just hit her with a “for real, lol.”’*

Namho had spent decades working as a spy.

His eyes shifted from side to side before he lowered his head in resignation.

“Understood. I’ll be careful.”

“Good. Then, next is Young Hero Hyuk—what are you doing?”

“I’m massaging the Captain’s shoulders to relieve the fatigue from his hard work.”

Right. He wasn’t called Hyukroach for nothing.

Ju Hwaran gave a satisfied smile as she watched Hyuk Mujin massage my body with remarkable awareness, then turned toward the one person who remained.

“Captain Song.”

A tremor ran through Song Ilseom’s pupils. He had remained silent from beginning to end.

“I haven’t said anything.”

“I know. Keep it that way.”

“……Understood.”

After dealing with her final target, Ju Hwaran shifted her gaze toward me.

The moment our eyes met, my lips opened reflexively.

“I’m sorry. I apologize. I was wrong.”

“What?”

“Yes?”

“What are you apologizing for?”

“Ah, no. It’s nothing……”

I just felt like I had to say it. Perhaps it was a survival instinct.

I sent Hyuk Mujin, who was diligently massaging my legs, a look.

*‘What happened? Why is Young Lady Ju acting like this?’*

Hyuk Mujin answered with his eyes as well.

*‘Young Lady Ju was so worried about you that she became like this, so please just let it go.’*

*‘Even so, this is too much. The air is different. The air.’*

*‘If you can’t read the room, at least keep your mo—’*

At that moment, Ju Hwaran abruptly opened her mouth.

“What are you two doing right now?”

“……!”

“……!”

Startled, Hyuk Mujin doubled the speed of his massage.

“What do you mean? I’m just continuing to massage the Captain’s legs. Goodness, the muscles here are really knotted up. Should I press harder?”

Feeling something strange, I carefully stopped his arm.

“That’s enough. Stop.”

“What? Why?”

“Ah, no. It’s fine now.”

“Our Captain is doing it again. You like it because it feels good, don’t you?”

“No. I said it’s fine. You must be tired too, so stop.”

“Don’t be shy. I, Hyuk Mujin, can do anything as the Captain’s right-hand man. Young Lady Ju, you saw that, right? Our Captain takes such good care of his people.”

Then, as Hyuk Mujin laughed heartily at Ju Hwaran, I sent him a Sound Transmission in profound despair.

—That wasn’t my leg just now…

“……!”

—So get your hand off me right now, you bastard. Before I break your wrist.

After a brief silence, Hyuk Mujin slowly withdrew his hand.

I wanted desperately to smack the back of his head as he stared at me with a gaze filled with a mixture of awe and fear, but I barely managed to hold myself back in front of everyone else.

No, perhaps……

*Hmm. No. That would be going too far.*

After muttering inwardly, I took in everyone’s faces one by one.

These were people I had thought I might never see again just a few days ago.

That was how terrible our situation had been. Everything had been shrouded in fog, with no way to see even an inch ahead.

But now that we were all gathered together like this, alive, I was overcome with emotion all over again.

The fact that not one of them had died filled me with joy.

“I’m really glad.”

At my single sentence, which broke the brief silence, everyone’s eyes widened. Then they smiled faintly.

That was enough.

By now, we had grown close enough to understand each other’s feelings.

* * *

It took quite a while to hear the entire story.

We had spent the same amount of time, but they and I had gone through different situations in different places. Their account also included the seven days and nights that had passed while I was unconscious.

“We really thought we were going to die then. The Captain wasn’t there, and we were bound, when that Blood Monk we’d only heard about suddenly stepped off the swift ship. Wow……”

“If we hadn’t recognized Great Hero Jeok, a battle would have broken out. The Nanman warriors who were with us were incredibly aggressive.”

“I truly thought everything was over. We should have been bringing reinforcements to save you, but a great fiend called the Blood Monk appeared.”

It was a more detailed account than the one I had heard from Jeok Cheongang.

When the Blood Monk’s true identity was revealed, the Nanman people were initially skeptical. But the battle ended before it even began when the bandits of the Water Dragon Stronghold, every last one of them sporting bruises around the eyes, stepped forward to confirm that he was the Fire King.

After that, Jeok Cheongang hurried to the Nanman Beast Palace at full speed. By the time the members of the Fire Dragon Pavilion and the Nanman scouts arrived a step behind him, everything was already over.

“When we saw the Captain collapse, we really thought he had died. His entire body was covered in blood, and all around him there was nothing but pools of blood and corpses……”

At that point, I was about to cut Hyuk Mujin off.

If they started talking about the condition of my perfectly healthy body, anyone would have no choice but to become suspicious.

But before I could open my mouth, Ju Hwaran’s voice continued.

“But Great Hero Jeok stepped forward and reassured everyone. He said that you had only collapsed from exhaustion.”

I asked, feeling uneasy.

“……Old Master—no, Master—what exactly did he say?”

“Hmm. I’m not sure. Everyone was in such a panic at the time. But I remember Great Hero Jeok saying that Young Master Jin hadn’t suffered any serious injuries because he arrived in time. Palace Lord Yayul agreed with him, too.”

Namho nodded and joined in.

“It was heavenly luck. Heavenly luck. No matter how powerful that bastard is, how could he have survived that hellscape? Two of the Ten Kings had stepped in. Even the Southern Heaven Demon Empress wouldn’t have been able to do anything.”

It was a story that differed slightly from the truth.

But I silently nodded to show my agreement.

This was unmistakable protection. Jeok Cheongang and the Beast Miao King had taken action to conceal my secret and keep people from becoming suspicious.

*The survivors of the Baekcheon Unit will keep their mouths shut as well. They’re loyal to the Beast Miao King.*

Death meant silence.

The battle that day had taken place mainly in the Inner Palace, and most of the people who had been there had died.

If the survivors didn’t speak, the secret would be kept.

*No matter how close I’ve grown to these people, I can’t tell them.*

In the modern world, phenomena that couldn’t be explained with words were often called Magic or miracles.

But here, in the Murim, they would be called something else.

*Demon.*

Supernatural powers beyond human understanding inevitably inspire fear.

I wanted to keep the System—this ability of mine—as hidden from others as possible.

*Though what was done was done.*

I didn’t know what consequences the choice I had been unable to avoid that day would bring.

But it was fortunate that Jeok Cheongang had been the person who witnessed it from the closest distance. And knowing what kind of person the Beast Miao King was allowed me to feel at ease as well.

“Captain?”

“Huh?”

“What are you thinking about so hard?”

It seemed I had been lost in thought for quite a while.

I waved a hand at Hyuk Mujin, who was watching me suspiciously.

“It’s nothing. Something else just crossed my mind for a moment. Keep going.”

“Ah, yes. But where was I?”

“Did you hit your head?”

“No. Maybe it’s because someone kept hitting the back of it.”

By glancing subtly at me, Hyuk Mujin made the identity of that “someone” perfectly clear before continuing.

“I think I already mentioned that we gathered the dead and cremated them. And you know that all the chieftains who sided with Baeksang and then fled were locked in the underground prison, right?”

“I know the general details.”

“Oh, right. Come to think of it, I heard that Great Chieftain Yohi asked to be punished as well.”

“Yohi did?”

“Yes. Great Hero Yayul seemed willing to forgive her, but she voluntarily entered the underground prison.”

It was surprising that Yohi had gone that far, but at the same time, it felt natural.

Although she had repented late, Yohi had also allied herself with Baeksang to enjoy wealth and power. She must have learned a great deal after passing through the brink of death herself.

*She chose it herself. She must have thought it was the right thing to do.*

After muttering inwardly, I listened to the rest of the story.

More Nanman people than ever were staying in the Nanman Beast Palace to restore the Inner Palace, which had been reduced to ruins, and the Outer Palace, which had suffered considerable damage.

As a result, Young Palace Lord Yayul Mok was so busy that he barely had time to breathe.

“We passed the news along, but I don’t know if he’ll come right away. It’s been hard to even catch a glimpse of him lately.”

“That’s probably true. The Beast Miao King is probably the same.”

“Great Hero Yayul…… You probably won’t see him either—not just us, but anyone else.”

“What?”

“He’s been missing since two days ago. I hear the entire leadership is already in an uproar.”

“……”
## Chapter artifact 717

# Chapter 717

Seven days and nights can be a long time or a short time, depending on the person.

But considering the current situation in the Nanman Beast Palace, it was also nowhere near enough time to repair all the damage they had suffered.

Even though the demonic qi flowing from the rift had disappeared, its aftermath was still painfully clear.

Countless people had died. Some had lost their families and homes. Others were probably living in fear of the disaster that might return at any moment.

*The Beast Miao King disappeared in a situation like this?*

I narrowed my brows, lost in thought, then finally opened my mouth.

“Tell me in more detail.”

Hyuk Mujin scratched the back of his head as he answered.

“Uh, I’m sorry, but I don’t actually know that much. If I had to add anything, it would be what I mentioned earlier—the Nanman leadership is in an uproar, and they were even discussing deploying a net over heaven and earth to search for Great Hero Yayul.”

That was only natural from the Nanman people’s perspective.

The Palace Lord, who should have been their center of gravity more than anyone else in such a difficult situation, had disappeared.

And their concerns probably included the possibility that Dark Heaven had made another move.

*An assassination, for example. Or a kidnapping.*

Maybe I was getting ahead of myself, but it wasn’t impossible.

The Beast Miao King had suffered considerable injuries in his battle with the Southern Heaven Demon Empress.

His personal martial prowess was extraordinary, and Jeok Cheongang had arrived before it was too late to help him. Even so, he couldn’t have simply shaken off his injuries and gotten back on his feet after only a few days.

“So, what were the results of the search?”

At my question, Hyuk Mujin tilted his head.

“What search?”

“……Did you really injure your head? You don’t even remember what you just said?”

“Oh. The net over heaven and earth.”

Hyuk Mujin slapped his forehead and continued.

“I only said it was being discussed.”

“Huh?”

“It fell through.”

What? It fell through? This was a matter of such importance?

I blinked a few times before asking,

“Did the Nanman Beast Palace get swallowed up by Dark Heaven while I was asleep?”

“The leadership? I don’t think so.”

“Ah, then they’re secretly conducting a search because they don’t want to make the tribespeople anxious?”

“I don’t think so either.”

“Then what the hell are they doing, not looking for their Palace Lord?”

“Why are you asking me? He isn’t my Palace Lord.”

*Whack!*

Having finally earned another point toward his back-of-the-head mileage, Hyuk Mujin collapsed with a silent scream.

Watching him writhe on the ground, Namho clicked his tongue softly and turned toward me.

“Under normal circumstances, the leadership would have done something. Whether that meant deploying a net over heaven and earth or secretly sending out warriors to search.”

I lowered my fist and replied,

“But they gave up?”

“More precisely, they had no choice but to give up. Because of someone else.”

“Someone else?”

“What choice did they have? This wasn’t some nobody who’d crawled in off the street. The great Fire King himself told them to drop everything.”

“……!”

“He reportedly told them that if the Palace Lord didn’t appear by midnight two days later, he would step in personally, so they should shut their mouths and focus on calming the people. The Young Palace Lord agonized over it, but in the end, he listened to the Fire King. The other chieftains had no choice either.”

Jeok Cheongang—and Yayul Mok, too?

But my surprise lasted only a moment. After thinking briefly, I nodded calmly.

“If it was midnight two days later, that means tonight, right?”

“That’s right.”

“I see.”

“I see? That’s all you have to say?”

“What else is there to say? If Ol—no, if Master said to drop it, then we should drop it.”

Namho stared at me silently, then smacked his lips.

“Well, the trust between master and disciple is awfully strong.”

“His personality is terrible, but there’s always a reason behind his actions.”

“If I told him you said his personality was terrible, would the bond still be that strong?”

“……It might get heated. Do you want to see me wake up in Henan?”

“Why would you even ask? Of course…”

As an answer came out without the slightest hesitation, Namho glanced at someone’s reaction before continuing in a mournful voice.

“Of course I’ll keep it a secret. Absolutely.”

“……?”

What was that? Had Ju Hwaran just given him an axe-eyed glare?

But when I looked at the way her eyes curved like a half-moon, I decided it had only been my imagination. I probably hadn’t fully woken up yet.

*Smack.*

I patted my cheeks and stretched. With a series of cracks, my stiff bones loosened, and my body felt even lighter.

*My condition is perfect.*

Between leveling up and resting for seven days and nights, I was feeling better than ever.

My mood was a little foul thanks to the nightmare, but that was something that would improve with time.

*Someone else is probably feeling the same way.*

I muttered inwardly, then deliberately put on a sleepy expression for everyone around me.

“Ah, I talked for quite a while after not speaking much for so long. I’m pretty tired. Could everyone give me some space for a moment?”

Being a patient had its advantages. No matter what I said, people accepted it obediently without suspicion.

And once everyone had left, I slipped out of the pavilion through the window.

* * *

It had only been a simple guess.

*If he isn’t there, no big deal. If he is, then great.*

That was all I had expected.

But the moment I entered a remote patch of grass that no one ever visited, my guess became certainty.

“Oh, there you are.”

*Rustle.*

At my casual greeting, the blades of grass trembled faintly. At the same time, a streak of light shot toward me.

*Whoosh—crack!*

The dagger flew straight toward the space between my brows. I caught it without even looking, and the blade began to glow red, unable to withstand the heat of the Scorching Yang Qi in my hand.

*Drip. Hissss.*

Molten metal fell to the ground. Only then did I realize that I was still wearing my mask, so I quickly raised both hands.

“It’s me. Jin Taekyung.”

And then—

*Fwish!*

With several faint sounds of air splitting through the empty sky, multiple figures landed among the dense grass.

*One, two, three…… seven.*

That was the number I had sensed, and I had correctly identified them as well.

“The Seven Miao Tigers, right?”

*Step.*

“Please forgive our rudeness.”

When the figure at the front stepped forward and removed his mask, the face of a good-natured-looking man was revealed.

It was the same face I had seen in the underground prison.

“At last, we can exchange names. Wonhu of the Seven Miao Tigers pays his respects to Great Hero Jin, Nanman’s benefactor.”

“We pay our respects to Great Hero Jin.”

Following Wonhu, the others performed awkward but respectful fist-palm salutes.

I gave a quiet laugh and answered,

“Benefactor? Not at all. I’m the one who should be thanking you. You helped me a great deal that day.”

At the mention of what had happened in the underground prison, Wonhu smiled as well.

“Please, think nothing of it. If not for you, Great Hero Jin, all of us would have been as good as dead. Or…… we would have become monsters who had lost their minds.”

His smile faded along with his bitter words. After letting out a sigh, he suddenly looked troubled.

“But how did you know about this place?”

“I came here once before, to meet Great Hero Yayul.”

Wonhu nodded as if he had guessed the reason.

“That must have been the day. He disappeared without saying a word even to us, his direct guards, so we were very confused.”

“Yes. Yayul Mok—or rather, the Young Palace Lord—guided me here that time.”

“Now that no one comes here anymore, it is perfect for a private conversation.”

“After coming back, I can see that.”

The Outer Palace alone was enormous. It was large enough to be called the capital of a small country, so there was no reason for anyone to seek out a remote patch of grass where even the path had disappeared.

“Then, Great Hero Jin, might you perhaps……”

“Yes. I came to see Great Hero Yayul. I had a feeling he would be here.”

“Hmm.”

Wonhu let out a low hum and stared at me. Then, instead of the answer I had expected, a quiet command slipped from his lips.

“Make way.”

The Seven Miao Tigers standing behind him flinched in unison.

“Big Brother.”

“But our lord ordered us not to let anyone in……”

“I won’t say it twice.”

At Wonhu’s firm voice, the Seven Miao Tigers hesitated for a moment before sighing heavily and splitting apart to either side.

“I trust you already know the exact location. Then, I’ll take my leave.”

Wonhu gave me another awkward fist-palm salute and turned around.

Or he was about to turn around when he suddenly looked back at me.

“I swear by heaven and earth that all the Nanman people, myself included, will remember Great Hero Jin’s help.”

I felt the same way. I would remember the help they had given me until the day I died, and all I could do was be grateful that they were still alive.

I substituted a nod for a farewell to the Seven Miao Tigers, then moved forward through the thick grass.

A few moments later, a dilapidated old shrine finally came into view.

*Step.*

I approached without bothering to conceal my presence. Through the gaps in the door, whose corners had crumbled with age and which was riddled with holes, I could see someone’s back.

“May I come in?”

No answer came, so I entered the old shrine.

*Screeech.*

The moment my foot touched the worn floor, it let out a shriek.

“Whoa. At this point, it could really use some oil.”

As I looked around and continued making small talk, a low voice came from the broad back of the man sitting cross-legged.

“It’s fine. It’s been like that for a long time.”

“True. Great Hero Yayul would know better. You said you always hid here whenever you caused some major incident as a child.”

“……Did I?”

“Have you already forgotten? You told me about it last time.”

“I must have told you all sorts of things.”

He wasn’t saying that because he didn’t remember.

He was saying it because he was suffering over the death of someone who was no longer in this world.

Someone who had always hidden in this old shrine with him.

As I gazed at the Beast Miao King’s back, I suddenly opened my mouth.

“Why did you disappear? You could have at least said something before you left.”

“I simply wanted to.”

“Everyone’s anxious after you left. They keep asking where our Palace Lord went.”

“So you came looking for me yourself?”

“I came on a walk. You should get back before our Palace Lord becomes your Palace Lord.”

“Palace Lord.”

The Beast Miao King let out a quiet, humorless laugh and muttered in an empty voice,

“Do you think…… I have the qualifications to be a Palace Lord?”

“Hmm. I suppose it depends on why you came here.”

“Why?”

“If you’re going to brush it off with the same answer as before and say you simply wanted to, then you should quit being Palace Lord, too. Though, it’s not really my place to say anything when I have no qualifications myself.”

After a brief silence, the Beast Miao King opened his mouth.

“It hurt. More than I could bear.”

“What was it?”

“Because I failed to protect them. The countless tribespeople who followed me, and my one and only sworn brother, who suffered right beside me.”

“……”

“Do you know what hurt me the most of all?”
## Chapter artifact 718

# Chapter 718

“Despite so many people dying, the grief that occupied the greatest place in my heart was for Baeksang alone.”

The low voice pierced my ears. After a brief silence, I opened my mouth.

“So that’s why you left? Because you thought those feelings of yours were wrong?”

“To become the Palace Lord of the Nanman Beast Palace means putting this land and its tribespeople before anything else. But I became trapped by my personal feelings.”

I could see his enormous back, like a thousand-year-old megalith. Yet the back of the giant who had supported Nanman for so many years looked pitifully small at that moment, like a child’s.

“When I faced Baeksang for the last time, do you know what I was thinking?”

I could guess well enough. But I didn’t say it.

The person who knew him better than anyone—and had suffered the most because of him—was standing right in front of me.

“I wanted to save him somehow.”

“……”

“Even in that horrific scene, I wanted to save that bastard Baeksang, who had betrayed everyone in this land, myself included, and help him run far away.”

Though they shared no blood, they were sworn brothers no different from actual family.

The Beast Miao King must have wanted to save Baeksang at any cost.

He must have wanted to absolve the man who had served as Dark Heaven’s hunting dog while his child—the child he had believed dead—was held hostage.

But the one who refused that absolution was Baeksang himself.

“He probably knew, too. That I was hesitating. That must be why he made that choice.”

The Beast Miao King’s muttering faded into the empty air.

The emotion in his voice was grief over being forced to end the life of his sworn younger brother—the man he had cherished more than his own life—with his own hands. It was also self-reproach for abandoning his duty as Palace Lord because of his personal feelings.

“One diseased tree caused the forest to die. Yet the forest keeper is now pacing in front of the diseased tree that has already fallen. Could you call such a person a forest keeper?”

I had been listening quietly to the Beast Miao King’s story. Then I broke the long silence.

“Great Hero Yayul, I’m asking this completely seriously…”

My voice faltered despite myself.

To be honest, I wasn’t even sure whether I should say this now. But somehow, I had to get that mentally shattered forest keeper back on his feet.

Even if it meant crossing the line a little—or perhaps a lot.

“Are you fucking stupid?”

“……!”

Unmistakable agitation came from the Beast Miao King’s back. But since I had already taken the first step, I continued without hesitation.

“What, is the Palace Lord some kind of god of heaven and earth? Don’t you have human emotions?”

“You…”

“Let’s be honest. Someone who spent their entire life with you, someone like family, just died. Who in this world could be fine after that? Are you supposed to be sadder just because other people died, too?”

The Beast Miao King fell silent for a moment beneath the barrage of blunt words before opening his mouth.

“Jin Taekyung, you as well?”

I nodded.

“Isn’t that only natural? What makes a bastard like me so special?”

“……”

“People around me can praise me as a chivalrous hero or a Great Hero, but I’m still a person in the end. Why would a Palace Lord be any different?”

His answer came without the slightest hesitation, and the broad back shifted.

*Rustle.*

His head slowly turned.

It was the first time I had seen the Beast Miao King’s face since entering the old shrine, and he looked utterly haggard.

“They were also Nanman people I had to protect.”

“And you protected them. Even after being branded a traitor, you came back despite the danger. It was thanks to you that countless others could be saved.”

I continued quietly.

“The diseased trees have already fallen, and the forest is still alive. If anything, it needs its forest keeper more than ever.”

Many people had been sacrificed in this incident. But ironically, Nanman would grow even stronger.

Because Baeksang had not been the only diseased tree in the vast forest called Nanman.

*The other chieftains. No—the traitors.*

Baeksang had joined hands with Dark Heaven for his child’s sake. They had followed Baeksang solely for their own safety and power.

They were the trees that should have been cut down long ago. Trees diseased with greed.

More than twenty chieftains had swayed the branches growing from their bodies while drunk on greed. Countless leaves had tumbled across a river of blood as a result, but the forest had not died.

No. Beneath a single banner called the Nanman Beast Palace, it would become more united and flourish more than ever.

And there was only one person who could raise that banner before all the people of Nanman.

“Let’s go back now. Wouldn’t it let that father and son rest easier, too?”

My voice was directed at the Beast Miao King, but my eyes were looking somewhere else.

The Beast Miao King noticed where my gaze had settled and asked quietly,

“You knew?”

“I noticed it as soon as I came in. Everything else in the shrine is covered in dust, but those are completely clean.”

I slowly walked forward.

Between the faded murals and dozens of stone statues whose identities I couldn’t determine, two memorial tablets had been placed—two that hadn’t been there the last time.

Neither tablet had a name carved into it.

But I already knew who they belonged to.

*Baeksang. Baekhwi.*

I murmured those names silently, names that even the person who had made the tablets by hand couldn’t bring himself to carve into them. Then I bowed.

Once.

And again.

When I turned around after completing the two bows, the Beast Miao King’s rigid face was waiting for me.

“Why are you looking at me like that?”

“Because it was unexpected.”

“What? Did you think I was going to knock over the tablets?”

“You could have. Especially considering the crimes committed by Baeksang.”

*Damn it. He wasn’t wrong.*

Given everything that had happened, even if I split Baeksang’s tablet in half and spat on it, it would count as self-defense.

But…

“I just… felt like doing this. That’s all.”

What was this filthy, bitter feeling?

I turned my head to look at the tablets again. And suddenly, I thought I understood what I was feeling.

Maybe it was something that should be called sympathy or empathy.

*I’m too late. I walked down a path I can never turn back from, and I will never stop.*

The voice I had heard in the dark underground prison seemed to ring faintly in my ears.

Looking at the tablet without even a single letter carved into it, I asked a question that would never be heard.

*If I had been you, what path would I have taken?*

No answer came from anywhere.

Not even from the depths of my own heart, rather than from the tablet.

Still, a thought suddenly occurred to me.

*If there really is such a thing as an afterlife, I hope that bastard—someone I could tear to pieces without feeling satisfied—gets to live an ordinary life unlike this one.*

*I hope he can spend a peaceful life without losing anyone or sacrificing anyone, together with the child he missed so terribly.*

*Damn it. How many people died because of him?*

I knew that much. There was no villain in this world without a story.

But the reason I felt so filthy was simple.

Maybe I could have walked the same path as Baeksang.

I could sufficiently imagine how desperately he had struggled within the circumstances he had been given.

That was why this was all I could say.

“Don’t commit any sins over there, you goddamn bastard.”

At that moment, reddish light streamed through the gap in the shrine door and illuminated the two tablets.

As if it meant to serve as an answer in their place.

Then, the next moment, a deep voice pierced my ears.

“The sun is already setting.”

*Cre-eak.*

The old floorboards screamed. At last, the giant unfolded his crossed legs and rose from his seat, staring at me with calm eyes.

“If we head straight to the Inner Palace now, we should still be able to have dinner together.”

“……!”

“Let’s go. We need to get back before it gets any later.”

I looked at the Beast Miao King, let out a quiet laugh, and nodded.

Nanman’s forest keeper had returned.

* * *

Two days passed.

When the Palace Lord, who had disappeared without a word, returned, the leadership—which had been thrown into confusion—quickly regained its stability. After taking a short rest at everyone’s urging, the Beast Miao King summoned me the following day.

No, to be precise, he summoned Jeok Cheongang and me.

Jeok Cheongang arrived at the meeting room hastily thrown together over seven days and nights. The moment he saw the Beast Miao King sitting there, he said,

“Our Miao King has grown up so much. He’s even sitting in the chief seat.”

“……Oh. I’m sorry. I did it out of habit.”

“No, no. I understand completely. So understand this old man’s habit of sending a Flame Divine Palm at any rude punk he sees.”

*Whoosh!*

The Beast Miao King had already experienced that habit during the Great Faction War.

He quickly moved his heavily bandaged body to vacate the chief seat, then politely gestured toward it.

“Please sit, Old Master Jeok.”

“Oh, it’s fine. You’re still injured—there’s no need to go this far.”

“……”

“Enough. Sit down already. I don’t like some wet-behind-the-ears punk ordering me around, but for now, go ahead and spout whatever you want.”

The Beast Miao King seemed confused by the gangster-like way of speaking he hadn’t heard in a long time, so I opened my mouth politely.

“You can just speak. That means he’s willing to listen.”

“……Then, Old Master Jeok, may this junior say something?”

“He really hates being asked questions in return. You’re still not fully recovered, so if you don’t want to suffer something nasty, speak right away.”

“……Understood.”

Unlike the Jeok Cheongang in his memories, the one sitting before him looked much younger. The Beast Miao King glanced at him before carefully opening his mouth.

“I asked you to join us, Old Master Jeok, because I wished to consult you about a grave matter.”

“A grave matter?”

“Yes.”

“From what I’ve heard, the aftermath has been handled smoothly so far. Did you perhaps manage to pick up Dark Heaven’s trail?”

“I wish that were the case, but unfortunately, it isn’t. In another sense, however, it is a problem even more troublesome than that…”

“You’re taking too long to get to the point. Tell me the important part before I shorten your lifespan.”

*This man really hasn’t changed.*

The Beast Miao King looked at Jeok Cheongang with exactly that thought in his eyes, then took something from inside his robes and placed it on the table.

*Thud.*

It was something wrapped in thick cloth. But everyone in the room, myself included, could sense the ominous energy seeping out from within.

As the air suddenly grew heavy, Jeok Cheongang muttered as though groaning.

“……Demonic qi?”

The Beast Miao King nodded with a grim face.

“That’s right. Very pure and powerful demonic qi at that. I couldn’t entrust it to anyone else in Nanman, so I carried it myself.”

Their voices seemed distant, like echoes.

I had a feeling I knew where this demonic qi had come from, as well as what was hidden beneath the cloth.

At the same time, the final roar of an existence that had once echoed through the deep darkness rang in my ears.

“It’s the sacred stone. The one carried by the guardian spirit.”

“As you guessed. Though it is no longer a sacred stone.”

*Rustle.*

The Beast Miao King answered in a troubled voice and peeled back the cloth. Instead of warm, dazzling radiance, a stone filled with murky darkness was revealed.

It had absorbed all the demonic qi flowing from the rift. Now, it was something that ought to be called a demonic stone, and the Beast Miao King’s gaze sank deeply as he looked at it.

“For now, I am suppressing the demonic qi. But I cannot leave it like this forever. That is why I summoned you and Old Master Jeok to discuss what should be done with it.”

At that moment—

*Ding.*

A clear chime, completely at odds with the murky darkness before me, rang out as a holographic window appeared in midair.

> **System**
>
> **Quest:** Corrupted Divine Artifact
>
> Will you accept?
>
> **Y / N**
## Chapter artifact 719

# Chapter 719

> **System**
>
> **Quest:** Corrupted Divine Artifact
>
> Will you accept?
>
> **Y / N**

The holographic window that suddenly appeared before me wasn’t the only one.

I quickly skimmed the information for the newly created Quest.

> **System**
>
> **Quest**
>
> **Corrupted Divine Artifact**
>
> The sacred stone that once protected this land has already lost its original form.
>
> Consumed by demonic qi, it is like the spark of another calamity, and you must dispose of this Corrupted Divine Artifact by some means or another.
>
> **Grade:** Supreme Peak
>
> **Restriction:** Jin Taekyung
>
> **Mission:** Dispose of Corrupted Divine Artifact (Incomplete)
>
> **Reward:** Varies according to how the mission is carried out
>
> **Failure:** Increase in the Corrupted Divine Artifact’s demonic qi

After reading the Quest information window to the end, I muttered quietly to myself.

*Accept.*

> **System**
>
> You have accepted the Quest **Corrupted Divine Artifact**!

Unlike the several Quests I’d been more or less forced to undertake until now, this one offered me an actual choice. But to me, it was no different from an offer I couldn’t refuse.

*I can’t keep suppressing the demonic qi forever.*

The sacred stone—or rather, the Corrupted Divine Artifact consumed by demonic qi—was no different from a bomb that could explode at any moment.

It was fortunate that the person in possession of it was the Beast Miao King. Even an ordinary Peak master wouldn’t have been able to withstand the demonic qi contained within it.

*Just like the Quest information says, we have to deal with it somehow.*

How many sacrifices had it taken to close the rift?

If only for the sake of the guardian spirit that had thrown itself into the breach at the final moment, I had to prevent that bomb from exploding.

And at that very moment, I wasn’t the only one thinking along those lines.

“Demonic qi of this magnitude… This won’t do.”

Jeok Cheongang muttered with a frown, then gestured toward the Beast Miao King and me.

“Stand aside. This old man will take care of it.”

As if he had guessed what Jeok Cheongang meant, the Beast Miao King’s eyes widened.

“Old Master Jeok, surely you don’t mean…”

“You thought it, didn’t you? If there’s even a chance it could become a source of trouble, we need to pull it out by the roots.”

“But this… isn’t something that can be destroyed easily.”

Jeok Cheongang’s answer to the Beast Miao King’s concern was extremely brief and simple.

“That’s true for you.”

“……”

“I can do it.”

That was some fucking macho-man talk.

With a single short sentence, Jeok Cheongang had even silenced the Beast Miao King—the most beastly man in all Nanman—as he slowly stretched out his hand.

*Whoosh.*

Scorching Yang Qi began to gather along his hand, radiating such dreadful heat that the air seemed to distort amid the haze rising from every direction.

But then…

“Old Master.”

The words slipped out after a moment of consideration.

Jeok Cheongang, who had been about to strike, suddenly stopped moving.

“What?”

“I don’t think you should do it. That.”

“Why?”

“I gave it some thought, and I have a feeling things could get ugly if we mess with it carelessly.”

“What?”

At my solemn voice, Jeok Cheongang’s eyes widened.

“You mean you actually thought about something?”

“……”

I was completely at a loss for words.

Jeok Cheongang looked at my thoroughly deflated expression, cleared his throat, and opened his mouth.

“If we leave it like this, it will become a source of trouble sooner or later. We need to deal with it as quickly as possible.”

“I know that.”

“Then why are you stopping me? Because you don’t trust this old man?”

“Oh, come on. Why would you put it that way? Who else would I trust if not you, Old Master?”

That was what I said, but truthfully, about half of me did feel that way.

To be more precise, it wasn’t that I didn’t trust Jeok Cheongang. I was simply worried about what might happen.

*What if he fails to destroy it completely?*

The Corrupted Divine Artifact before me was, for example, like the teacup sitting in front of me.

As long as the cup remained intact, the tea wouldn’t spill. But if the teacup broke, the tea would overflow in every direction.

*If the demonic qi can no longer be contained, then we’ll have another goddamn disaster on our hands.*

No matter how wildly a single mad tiger rampaged, it could simply be beaten down. But if the demonic qi spread, things would become much more troublesome.

No. If that happened, it would be a blessing if trouble was all it amounted to.

That was why I had to stop Jeok Cheongang.

Regardless of how much I trusted him, I couldn’t put someone else’s life on the table as the stake in a gamble like this.

*Even if the odds are only one in a thousand—or one in ten thousand—it’s still not worth it right now.*

We had already spilled too much blood.

Some had died after fighting to the bitter end. Some had died after losing their minds and becoming monsters. Even people who had never held a sword in their lives had died in considerable numbers while escaping that hellscape.

If the guardian spirit hadn’t sacrificed itself to close the rift, the casualties would have multiplied like a snowball by now…

Wait.

*The guardian spirit?*

Along with the sudden sense of déjà vu, that name began circling endlessly through my mind.

The memories from the day I first met it until now brushed past my eyes and ears one after another, racing toward a single thread of enlightenment.

And then, at some point—

“Ah.”

A short exclamation escaped between my lips before I realized it.

Jeok Cheongang and the Beast Miao King looked at me as though wondering what the hell had suddenly happened to me, then spoke in turn.

“Yeah, why the fuck are you suddenly throwing a fit all by yourself again? Let this old man in on it.”

“Have you perhaps thought of some brilliant strategy?”

I wasn’t sure whether it was brilliant enough to deserve that name.

At least, not yet.

But if my current suspicion was true… it was certainly worth trying.

*At least we won’t lose anything by trying.*

I glanced in turn at the Quest window that was still open and the faces of the two men waiting for my answer. Then I shrugged and opened my mouth.

“Why don’t both of you come outside with me for a bit?”

* * *

*Thud-thud-thud-thud!*

The party racing forward as it cut through the wind was a small one. In fact, judging by the head count alone, even calling them a *party* might have been an exaggeration.

Three tigers and three people.

But the picture changed when you looked closely at those three people. The two racing along on either side of me were enough to prove that.

“I wondered how fast a beast could really be, but this isn’t bad at all. The saddle’s comfortable, too.”

Jeok Cheongang was closely examining the tiger racing along beneath him with an intrigued gaze. The Beast Miao King, riding to my left, readily answered.

“He’s one of the bravest and fastest beasts in the Nanman Beast Palace. He’s also descended from a tiger that fought alongside me during the Great Faction War.”

“Oh-ho. That huge one crouching in front of the barracks? I remember him. I thought he looked familiar.”

Yeah. Who needs an Azure Dragon on the left and a White Tiger on the right?

My chest swelled at the thought of this insane lineup—Fire King on the left, Miao King on the right.

A terrifying force capable of devouring even the Southern Heaven Demon Empress if she somehow returned alive.

The feeling of security was more comforting than a bowl of gukbap could have been.[^1] The quiet conversation between the two men reached my ears.

“The more I look at him, the better he seems. Good stamina, fast on his feet, and he looks intelligent at a glance.”

The Beast Miao King smiled proudly.

“I raised him with particular care. He was such a picky eater as a cub that I had quite a time of it. Whenever that happened, I even fed him milk myself.”

“What? You did it yourself?”

“……That’s just how I put it. It isn’t what you’re thinking, Old Master Jeok.”

Jeok Cheongang studied the Beast Miao King’s massive pecs before nodding.

“Well, let’s say that’s what you meant.”

“No, when you put it that way, it sounds even more—”

“Whatever. I’ve decided to take this one with me.”

At that moment, the smile on the Beast Miao King’s lips vanished.

“Excuse me?”

“Why are you asking again? Were you planning to make him run his legs off all the way back to the Central Plains?”

“Th-that obviously wasn’t my intention, but the one you’re riding is a creature this junior raised like a son in his old age…”

“Give him to me.”

“No, wait—”

“Do it.”

“……”

“If you really don’t want to, I’ll take that one instead. He looks like a spiritual creature.”

Jeok Cheongang pointed toward the tiger he had called *that one*. The Beast Miao King hurriedly shook his head.

“Gasp. Anyone but him. I only borrowed him for a while in the first place.”

“What if this old man were to take him?”

“I-I didn’t raise him myself, and as a father, how could I give away someone my son regards as a brother?”

“The sky is awfully clear today. You do have a long tongue.”

After a brief silence, the Beast Miao King answered in a gloomy voice.

“……Understood. I’ll give you the creature you’re riding now.”

“Since you’re insisting so much, I suppose I can’t refuse. I’ll accept your kindness.”

“……”

So much for feeling grand.

Was this really the same senile Fire King? The Fire King truly was a legend…

As I tried to steady my suddenly shrunken chest, the creature carrying me let out a low growl.

*Grrr.*

Judging by the way he even met my eyes, it seemed he also knew that he had only just escaped the clutches of the Fire King—that dogcatcher.

Feeling sorry for him, I gently stroked his trembling white fur.

“It’s okay, buddy. You survived.”

*Whine.*

Muyaho slowed his pace, letting out a mournful cry like a puppy that had lost its mother.

He must have instinctively realized that showing off his abilities in front of Jeok Cheongang would only increase the chances of being dragged all the way to the Central Plains.

Fortunately, Jeok Cheongang’s attention shifted elsewhere moments later.

“What’s that…?”

His voice trailed off.

At the end of the direction Jeok Cheongang was looking stood a bare mountain that had been almost completely burned away.

No, even that pathetic bare mountain had a name.

Ailao Mountain—a name no one living in this land could possibly fail to recognize.

Just as I was about to explain that to him, Jeok Cheongang’s eyes flew open and he shouted,

“What shameless son of a bitch burned down these precious mountains, trees, and grass?”

“……”

“……”

For a brief moment, the Beast Miao King and I exchanged a heated glance. Then I answered in a voice filled with righteous fury.

“Dark Heaven.”

Some truths are beautiful when left unknown.

* * *

Only after finally realizing that the pathetic bare mountain was our destination did Jeok Cheongang immediately frown.

“Did we come all the way here to plant trees?”

“……I’m asking this sincerely because I’m genuinely curious. How crazy do you think I am?”

It was an absurd question.

Today wasn’t Arbor Day, and even if it had been, I wouldn’t have planted any trees. I had come with these two to Ailao Mountain, which had been reduced to a bare mountain, for a purpose that had been decided from the beginning.

“This way.”

It didn’t take long for the Beast Miao King to realize where I was heading.

“The Poisonblood Grounds. No. Should we call it the Sacred Land now?”

It would have been stranger if the Beast Miao King didn’t know. Even if Yohi hadn’t told him the details, she must have given him a rough account of what had happened.

But when I heard him mutter, I shook my head.

“They’re different. The Poisonblood Grounds are the Poisonblood Grounds, and the Sacred Land is the Sacred Land.”

The two spaces were distinctly separate. If the Poisonblood Grounds were a land of death created by humans, the Sacred Land was Nanman’s heart—the land of life.

*Yes. Life itself.*

I set the Corrupted Divine Artifact in my hand down on the ground.

Misty demonic qi began to flow from it, and Muyaho let out a low growl.

But even though darkness had consumed it, its essence remained unchanged.

*Whoosh…*

The land pulsed as though it were a beating heart. With it, another world hidden for countless ages shed a single veil.

At that same moment, I saw it.

Another space filled with warm radiance in every direction.

At its center was a small pond shining more brilliantly than anything else.

“Ah.”

“That’s…”

The exclamations from Jeok Cheongang and the Beast Miao King trailed off before scattering into silence.

But I knew what they had felt.

And I knew what I had to do now.

*Purification.*

Today was the day a new sacred stone would be born.

[^1]: Gukbap is rice served in a hot, hearty soup—a common comfort food in Korea.

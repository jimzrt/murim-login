# Checkpoint Review — 270–274

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

# Chapters 270–274

## Plot

After returning from Murim, Jin Taekyung sleeps for forty-two hours before rejoining modern life. He participates in the Peace Guild’s new-member workshop, effortlessly clears its Stone Golem and Iron Golem raids, and ends the planned six-night, seven-day operation after only three days. Team Leader Choi and Butler Kim accept that Taekyung’s strength can be explained publicly as an unprecedented second awakening, while Choi continues demanding repayment—with interest—for his past assistance.

Taekyung reconnects with his former classmate Park Jihoon, who is secretly influential within Myeongdong Guild. Jihoon learns that the Guild’s higher-ups find Taekyung troublesome and begins arranging an A-Rank raid that appears intended to kill him under cover of a Gate accident. Meanwhile, Peace Guild’s rapid expansion leaves Taekyung training inexperienced recruits through lucrative B-Rank raids. During a Lycanthrope attack, Kim Jinsoo restores the rookies’ formation and earns Taekyung’s approval.

A newspaper reports Hunter Jung Hyunwoo’s death and Myeongdong Guild’s regret. Soon afterward, Choi summons Taekyung to Ilsan Hospital: Im Kkeokjeong was attacked while drinking alone by three unidentified Black Hunters, who severed his arm below the elbow before fleeing. Choi explains that Guilds cultivate trained, unregistered Awakened people as concealed weapons capable of erasing troublesome individuals or rival organizations. Taekyung appoints Jinsoo acting team leader and orders the rookies to delay their next raid while he investigates.

## Continuity

- Taekyung can spend thirty days in the modern world while only three hours pass in Murim; Jeok Cheongang remains unconscious, and Mae Jonghak, Cheongpung, and the unresolved Dark Heaven/Blood Lord threat remain in Murim.
- White Flame is Taekyung’s bound Ten-Thousand-Year Cold Iron spear and the only item that crosses between his Murim and modern-world inventories.
- Peace Guild has recruited twenty B-rank Hunters and thirty C-rank-or-lower Hunters roughly four months after its founding. Butler Kim and Song-i rotate rookie training; Im Kkeokjeong had not yet joined the rotation before his attack.
- Taekyung accepted the Quest **It Was Too Much Money to Say “I’m Not Doing It!”** after Choi offered a 200 percent monthly performance bonus. Several B-Rank Gates were reserved because A-Rank Gates are booked for at least a week.
- Kim Jinsoo graduated first in the B-rank training course, first destroyed a Golem core, and is now acting team leader for two hours while Taekyung is absent.
- Park Jihoon is nominally a Myeongdong Guild Team 1 Hunter, but the nominal leader obeys his orders. Jihoon’s higher-ups and the planned A-Rank raid remain unexplained.
- Jung Hyunwoo’s reported death and Myeongdong Guild’s expression of regret have not been explained.
- Im Kkeokjeong is hospitalized in the Special Treatment Ward after losing his arm below the elbow. The three Korean attackers have no identities among registered Korean Awakened people or Hunters and remain at large.
- Black Hunters are unregistered Awakened people given systematic training comparable to Hunters. Their sponsoring Guild or organization, motive for targeting Kkeokjeong, and connection to Jung Hyunwoo’s death remain unknown.
- Choi’s larger reason for helping Taekyung—and his stated intention to collect Taekyung’s debt with interest—remains unstated.

## Translation Decisions

- Retain **White Flame**, **Black Hunter**, **Special Treatment Ward**, **Stone Golem**, and **Iron Golem**.
- Render **국정원** as **NIS**, **게이트 관리청** as **Gate Management Agency**, and **미등록자** as **unregistered Awakened person**.
- Retain **Haste**, **Strength**, **Healing**, and **Fire Wall** as named spells.
- Render the quest title as **It Was Too Much Money to Say “I’m Not Doing It!”**
- Render Taekyung’s rookie nicknames as **the Pied Pipers** and **the balding rookie**.
- Preserve Taekyung’s profane, gamer-like voice in “Mob farming is fucking sweet,” while keeping Choi’s debt remark as collecting the debt **with interest**.

## Durable state

{
  "active_continuity": [
    "Mae Jonghak is publicly recognized as the Sword Saint despite his Returned to Youth appearance.",
    "Cheongpung can move again and wanted to see Taekyung as soon as he woke; dumplings quieted him.",
    "Jeok Cheongang remains unconscious; the Luoyang Strange Physician examined him but said there was no treatment available for now.",
    "Taekyung considers Jeok both his Master and the equivalent of a close grandfather.",
    "Mae suspects Dark Heaven may seek direct confrontation or may be a smokescreen or subordinate organization of the Demonic Cult.",
    "The Blood Lord, Temporary Strength Pill, and Exploding Blood Demonic Art carry the Demonic Cult’s scent, but the Blood Lord’s sorcery is darker and unfamiliar.",
    "Taekyung has returned to the modern world after more than a year in Murim and can spend thirty modern-world days while only three hours pass in Murim.",
    "White Flame is a bound spear made from Ten-Thousand-Year Cold Iron; only Taekyung can use it, and it alone crosses between his Murim and modern-world inventories.",
    "Team Leader Choi and Butler Kim consider describing Taekyung as an unprecedented second-awakened Hunter sufficient and will not press him about his deeper secret.",
    "Team Leader Choi intends to collect Taekyung’s debt with interest, but his larger motive remains unstated.",
    "Peace Guild has recruited twenty B-rank Hunters and thirty C-rank-or-lower Hunters roughly four months after its founding.",
    "Butler Kim and Song-i agreed to rotate responsibility for training the Peace Guild’s rookie members; Im Kkeokjeong has not yet responded.",
    "All A-rank Gates are booked for at least one week, so Choi has reserved several B-rank Gates for the rookie-training schedule.",
    "Taekyung tacitly accepted the Quest It Was Too Much Money to Say “I’m Not Doing It!” after Choi offered a 200 percent monthly performance bonus.",
    "Three raids were scheduled, and Taekyung temporarily appointed Kim Jinsoo acting team leader with orders not to begin the next raid until Taekyung returned.",
    "Kim Jinsoo graduated first in the training camp’s B-rank course, first destroyed a Golem core during a raid, and restored the rookies’ formation during a Lycanthrope attack.",
    "A newspaper reported the death of Hunter Jung Hyunwoo and Myeongdong Guild’s regret over the incident.",
    "Park Jihoon is nominally a Myeongdong Guild Team 1 Hunter, but the nominal Team 1 Leader treats Jihoon’s position as hollow and follows his orders.",
    "Im Kkeokjeong was attacked by three Black Hunters after drinking alone and is hospitalized with severe injuries, including an arm severed below the elbow; the attackers fled and remain unidentified.",
    "Team Leader Choi states that Guilds cultivate or employ trained unregistered Awakened people as hidden Black Hunters and can erase troublesome people or Guilds."
  ],
  "continuity_sources": [
    274,
    273
  ],
  "open_questions": [
    "Will Jeok Cheongang regain consciousness and recover?",
    "Is the Blood Lord affiliated with the Demonic Cult?",
    "Is Dark Heaven a front or subordinate organization of the Demonic Cult?",
    "Why was the Blood Lord so intent on taking the Green Jade Buddha Staff, and what is the nature and scope of his unfamiliar sorcery?",
    "Who are Jihoon’s higher-ups and the person referred to as “that person,” and what organization or authority do they represent?",
    "Is the planned earliest A-rank raid intended to remove Taekyung as a Gate accident?",
    "What caused the reported death of Jung Hyunwoo, and what does Myeongdong Guild’s regret refer to?",
    "Why did the Black Hunters target Im Kkeokjeong, and which Guild or organization sent or trained them?"
  ],
  "safe_through": 274,
  "temporary_decisions": [
    "Render 낙양괴의 as Luoyang Strange Physician and 술법 as sorcery, distinct from movement techniques and lightness skills.",
    "Retain Morning Star for 신성 and render 염왕채 as Yama’s Debt.",
    "Render 스톤 골렘 and 아이언 골렘 as Stone Golem and Iron Golem.",
    "Retain Haste, Strength, Healing, and Fire Wall for the named spells.",
    "Render 국정원 as NIS, 한국대 and 한국대학교 as Hankuk University, and 게이트 관리청 as Gate Management Agency.",
    "Render the chapter’s rookie nicknames and Quest title as the Pied Pipers, the balding rookie, and It Was Too Much Money to Say “I’m Not Doing It!”",
    "Render 블랙 헌터 as Black Hunter, meaning an unregistered Awakened person with systematic Hunter training.",
    "Render 미등록자 as unregistered Awakened person and 특수 치료 병동 as Special Treatment Ward."
  ],
  "version": 1
}

## Reading copies

## Chapter artifact 270

# Chapter 270

Ding.

> **System**
> 
> - **Logout** complete.

My eyes flew open with the familiar System notification.

The moment my gaze met the two pairs of eyes staring down at me instead of the familiar ceiling—

“Eek!”

“Oh, my God!”

The two of them let out shrieks that could split eardrums and fell backward onto their butts.

I yawned as if I had just woken up and looked at my mother and Hayeon.

“What are you so surprised about?”

“Gasp… Haaah…”

“Huuh… Huuuuu…”

They looked as though they had seen a ghost. Still sitting on the floor and catching their breath, they shouted at the same time.

“You nearly gave me a heart attack!”

“You little bastard! You little bastard!”

Smack! Smack!

Hayeon’s eyes blazed, while Mom charged in and mercilessly pounded my back.

Somehow, the palm of a woman in her fifties hurt more than the fist of an average martial artist.

*Was this some kind of Inner-Family Heavy Hand?*

The Mother’s Palm Strike, remembered by both body and soul.

It was only after I had taken a great many more blows that the palm-storm finally stopped.

Of course, being hit a few times didn’t solve all my problems.

“Son.”

I swallowed hard at the weight in Mom’s voice. As expected, the atmosphere was anything but good.

“Yes, yes, Mother.”

“Do you know you’ve been sleeping for two whole days?”

Hayeon added,

“Forty-two hours, to be exact.”

“That’s right. You wouldn’t wake up, so we almost called an ambulance.”

Forty-two hours.

I’d slept quite a while. I had spent more than a year in Murim, after all, so it made sense that this much time had passed.

To be honest, I hadn’t expected it to take this long, either.

“Do you have narcolepsy or something? How can you sleep that long? You didn’t even react when we shook you.”

Hayeon asked with a thoroughly exasperated expression, and I casually piled lie upon lie.

“What are you talking about? I woke up once or twice in the middle.”

“You didn’t. Every time Mom and I checked, you were sleeping…”

“I woke up around dawn each day. How could you have seen me?”

“Huh?”

“Every time I opened my eyes, it was around dawn. I was tired, so I just kept sleeping.”

“No, but even so, can a person really do that?”

Of course not.

But I had long since mastered the art of dealing with this distrustful little menace of a sister.

“Hey, Jin Hayeon.”

I deliberately hardened my expression as I called her by her full name, and Hayeon flinched.

“Y-Yeah?”

“Don’t you know what I was like in high school?”

“I-I don’t.”

“I slept straight through seven periods without even eating, then slept again during evening self-study.”

“…”

“You think that’s all?”

“There’s more?”

“After sleeping at school, what do you think I did at home?”

“Could it be…”

“That’s right. I went home after school and slept again. That’s the kind of person I am.”

“That’s incredible.”

Hayeon nodded solemnly. Mom, who had been listening quietly, looked utterly crushed as she spoke.

“Son, that’s not something to brag about…”

Sorry, Mom.

But something similar might happen again in the future, so it seemed better to establish that precedent now.

The problem was that I was driving another nail into my mother’s heart.

*I’m building up my unfilial-son score again.*

I quietly avoided Mom’s gaze. It wasn’t as though my poor academic performance was anything new. Thankfully, the whole narcolepsy business disappeared from the conversation.

Before Hayeon could say anything else, I changed the subject.

“Oh, right. The massage chair. Weren’t we going to buy one?”

Hayeon answered with a look of utter contempt.

“We already bought one, you idiot.”

“Oh, really?”

“Yeah. I picked the most expensive one. It was worth every penny. I lay down for a minute and nearly went straight to heaven.”

“You’re taking the express train to hell when you die. Where did you get the money?”

“What do you mean, where? It was all your money. Here. I used the card properly.”

“…Right. Good job.”

When had she taken my card?

But I had my own crimes to answer for, so I couldn’t say anything.

How much did the most expensive one cost, anyway? I should have kept more of the money from selling the raid monster last time.

I was thinking about this and that as I took back the card when—

Ding-dong.

Mom and Hayeon’s ears perked up at the doorbell.

“Could that be them?”

“They’re here!”

What was here?

I asked with a bewildered expression.

“Is someone coming?”

“Of course. The delivery driver.”

Hayeon answered excitedly and dashed out of the room.

But a moment later, the voice that came with the sound of the front door opening did not belong to the delivery driver Hayeon had been waiting for.

“Excuse me. Is Jin Taekyung here?”

“Who…? Are you perhaps a reporter?”

“No.”

A soft yet low voice continued.

“I’m a Team Leader. The Team Leader of the Peace Guild.”

There was only one Peace Guild Team Leader I knew.

When I went into the living room, I saw a man in a black coat over Hayeon’s shoulder.

“Team Leader.”

Team Leader Choi gave a small nod in greeting.

“Have you been resting well?”

“…More or less.”

In truth, the mental exhaustion from struggling in Murim for over a year was no joke.

Even though it had been a while since I’d seen him, unease outweighed happiness. That was because if this man had come all the way to my house, his business was obvious.

“I’m glad to hear you’ve had a good rest.”

“I didn’t say I’d had a good rest—no, but what brings you here? I thought I didn’t have any media schedules for a while.”

“That’s only natural. You aren’t a celebrity, after all.”

“Then?”

“The workshop for our new Guild members is today.”

“A workshop?”

“Yes.”

That was fine. I was curious what the new Guild members were like, and I could go for a little while before coming home and getting some proper rest.

“When does the workshop end?”

“It’s scheduled to last about six nights and seven days.”

“What kind of workshop lasts a whole week? Are we going to Pyeongchang or Gapyeong?[^1]”

[^1]: Pyeongchang and Gapyeong are popular domestic getaway destinations in South Korea, often used for group retreats.

“Think on a larger scale.”

“Then maybe… an overseas resort in Southeast Asia?”

“Hmm.”

“Phuket? It’s Phuket, isn’t it!”

Team Leader Choi smiled brightly.

“We’ve secured an A-rank Gate.”

“Oh.”

“We’ll build team unity while hunting monsters together.”

“…”

A workshop with monsters. Now that was something.

* * *

Grroooan. Boom!

The earth shook every time the five-meter-tall creature took a step.

Its entire body, from head to toe, was made of solid rock. Moss clung to it here and there, and the whole thing looked damp with moisture.

A red light flashed from the rock at the very top, where vines hung down like hair.

The monster’s eyes. Someone muttered like a groan at the gaze of the magical creature, which held not even a speck of vitality.

“Golem…”

A bona fide A-rank monster.

The rookie B-rank Hunters who had just graduated from the training center felt their knees weaken at the mere sight of it.

“How are we supposed to take that down…?”

“I feel like one hit would kill me.”

Just as the roughly twenty new Guild members were watching the Stone Golem loitering in the distance and swallowing dryly, someone spoke.

“There’s no need to be afraid. The Stone Golem coming this way has tremendous destructive power and durability, but it does have one weakness: it’s slow.”

At the young Team Leader’s words—he looked as though he had just stepped out of a fashion magazine—the female Hunters nodded with dreamy expressions.

“They say it’s slow.”

“If Team Leader Choi Minwoo says it’s slow, then it’s slow. He’s right.”

At that moment, the Stone Golem’s head slowly turned toward them.

A brief silence passed. Then its rocky legs accelerated. With every stride, it ate up three meters in an instant.

Boom, boom, boom, boom!

“…It’s really fast, though.”

“Fuck, I should’ve gone with damage dealer instead of tank.”

“Excuse me. Do you think damage dealers are people who sit around and eat for free?”

“Then hold the shield and tank for me.”

“I’d rather not.”

The dark clouds that had settled over the new Guild members’ faces scattered at the clear voice that rang out next.

“Let the wind take root. Haste!”

“Power that can shatter stone. Strength!”

“Breathe life into your weary bodies. Healing!”

Fwoooosh.

The shouts rang out one after another.

Along with a refreshing breeze, halos of light descended over the new Guild members’ heads.

Those who felt their bodies improve beyond comparison turned around with astonished expressions.

*What is this? The difference is incredible.*

*She’s a B-rank healer like me, but her effect is this strong?*

*Wow. So she really is from the Ares Guild.*

At the gazes directed toward her, Song Song furrowed her flawless brow.

“What are you all doing? Do you want to keep standing there glassy-eyed until you have your workshop in heaven?”

Dazed once by the effect of the buff magic—powerful enough to make them mistake her for an A-rank healer—and a second time by her beauty, the new Guild members finally snapped out of it.

Boom, boom, boom, boom!

—Grrrroooar!

The Stone Golem, which had already advanced to within twenty meters, swung its arm.

Whoooosh!

With a tremendous crack of displaced air, a massive tree that had been deeply embedded in the ground only moments before shot toward them like a cannonball.

“S-Shields!”

Clack-clack-clack!

Several tower shields filled with mana rose to block the front amid screams that sounded like cries of terror.

But could they really stop a tree trunk fired at them like a bullet with nothing but this?

Just as everyone gritted their teeth, expecting a violent impact—

“Fire Wall.”

Fwoooosh!

A massive wall of flame surged upward.

The intense heat incinerated the dry branches and leaves. The trunk, blackened all over, crumbled the instant it struck the tower shields.

“Whoa…”

“What is this?”

A deep, mellow voice fit for a coffee commercial rang out above the wide-open mouths of the new Guild members.

“I blocked it once, but there won’t be a second time.”

It was strange. His words and actions were impeccably polite, but the old gentleman’s eyes held the viciousness of the training instructor who had tormented them at the training center until recently.

No, it was even worse.

“Fire Wall.”

With the second incantation, another wall of flame surged upward.

The only difference was that this time, it appeared behind them instead of in front.

“Ah, hot!”

“What the hell is this?”

“Guild Master! Guild Master!”

Kim the Butler blocked off the new Guild members’ rear with a curtain of fire and smiled faintly.

“You cannot grow by receiving nothing but help inside a Gate. Fight as though your lives depend on it.”

“…”

“Mages, find the core with detection magic. Tanks, protect the healers and draw its aggro. Damage dealers… I trust I don’t need to explain any further.”

Swoosh.

Kim the Butler flicked his fingers, and Team Leader Choi and Song Song’s bodies rose into the air.

The abandoned new Guild members were just about to fall into a panic when a shout rang out.

“Tanks, forward!”

Boom!

With a thunderous cry, a massive man in full armor slammed a tower shield into the ground.

Several of the new Guild members frowned when they saw him.

They realized that the first giant to step forward was a middle-aged D-rank Hunter whose only real thing to boast about was twenty years of experience.

“What are you doing? Get your heads in the game!”

But they had no choice. Their bodies, already sensing the threat to their lives, moved toward the front line of their own accord.

“Formation!”

“Formaaation!”

Clack-clack-clack!

With a deafening chorus repeating the command, the tower shields formed a solid wall.

The mages and healers drew up their mana, while the damage dealers prepared the strongest strikes they could unleash.

Im Kkeokjeong, crouched behind the shields, shouted with a grim expression.

“Hold!”

—Grrrroooar!

The Stone Golem charged toward the wall of shields.

Kra-boom!

* * *

“Gasp… Haaah…”

“Ugh…”

Heavy breathing and groans rose from every direction.

The tank with a broken arm and the mages and healers who had exhausted all their mana collapsed onto the ground, while the damage dealers lay sprawled across the Stone Golem’s remains.

“Ugh, I’m dying.”

“Did we really take down this Stone Golem?”

The raid had lasted a full five hours. Despite having more than twenty people, the process had been grueling and taken a long time, but the hearts of the rookie Hunters who had only just graduated from the training center swelled with pride.

“I took down an A-rank monster…”

“Let’s take a group picture later. I’m going to frame it and hang it in my living room.”

“Who takes down a Stone Golem for their first raid?”

“Good work, everyone.”

Just as everyone was looking back on their achievement with moved expressions—

—Grrrroooooar!

—Roooooar!

The new Guild members’ faces went stiff when they spotted golems approaching in the distance with roaring cries.

*What is that?*

There were more than ten of them at a glance, and they looked larger and harder than the Stone Golem. Light flashed every time their massive bodies moved with violent force.

Someone shouted like a scream.

“Iron! Those are Iron Golems!”

“Eeeek!”

The appearance of Iron Golems, among the highest-ranking of all golems, was more than enough to send everyone into a panic.

“W-Why are they here?”

“Aren’t they supposed to be scattered all over the place?”

They had never heard of golems living in tribes.

But the sight of them drawing closer by the second and the ground trembling like an earthquake told them all this was real.

In the end, they had only one lifeline left.

“Please help us! We’ll all die at this rate!”

The cry rose toward the sky. Team Leader Choi, who had been floating in the air and watching the situation from beginning to end, smiled.

“There’s nothing for us to help you with.”

“…What did you say?”

*Has that guy gone insane?*

Just as everyone began to doubt their own ears—

Whoooosh! Slash!

Along with a red flash, the Iron Golem charging toward them split cleanly in half, from the crown of its head to its crotch.

Crash!

A man emerged between the steel masses collapsing to either side.

“Mob farming is fucking sweet.”

The young man, Jin Taekyung, grinned.
## Chapter artifact 271

# Chapter 271

Shhk!

The Iron Golem’s impossibly sturdy body was sliced apart like soft tofu.

Even steel imbued with mana couldn’t withstand Scorching Yang Qi.

Everywhere the spearhead cut and pierced, trails of fire appeared, and molten metal dripped to the ground.

Ding. Ding.

> **System**
>
> - You defeated the **Level 95 Iron Golem**!
> - You gained a considerable amount of EXP!
> - You defeated the **Level 95 Iron Golem**!
> - You gained a considerable amount of EXP…

“Why is it so weak?”

I was bewildered by my own strength.

Iron Golems were difficult monsters. No, they were extremely difficult monsters. They couldn’t be killed unless their cores were destroyed, and their destructive power and durability were both tremendous.

*Regeneration that surpasses a Troll’s, destructive power that rivals an ogre’s.*

They also had inexhaustible Stamina and resistance to magic.

Their only flaw was that they were somewhat slow, but when I considered all their other advantages one by one, could that really even be called a flaw?

There was a reason they were regarded as some of the strongest among A-rank Golems. And yet…

*Why is this so easy?*

Fwoooosh!

The wind pressure tossed my hair around. An Iron Golem’s fist came crashing down toward the crown of my head.

A scream erupted from among the rookie Guild members.

“Look out!”

That rookie needed some training. If a teammate looked like they were in danger, they should have picked up a rock lying nearby and at least tried to distract the enemy. What were they doing?

*Well, he is a rookie.*

I clicked my tongue and clenched my fist.

In the instant that remained after splitting a second in half and then splitting it again, decades of internal energy raced down my arm.

Scorching Yang Qi transformed into blue flames and gathered around my fist.

And then…

Clang!

I thrust my fist forward.

Fist against fist. Iron Fist against the Flame-Extinguishing Divine Fist.

The ground sank with a metallic clang, and compressed air exploded outward. Through the swirling wind, I saw the Iron Golem stagger backward.

Only a few seconds earlier, its sturdy arm had gleamed brightly. Now, it was melting into molten metal and dripping away as though it had been swallowed by a fire dragon.

—Grill?

Iron Golems were magical puppets without emotions.

And yet, at that moment, I thought I could read bewilderment in the creature.

“Yeah. Of course I am.”

I kicked off the ground and shot upward.

The Iron Golem’s steel-colored chest came into view. And then I sensed it.

Deep inside its enormous body, which contained not even a trace of qi, something pulsed as it released mana.

The Golem’s core.

“This Hunter offers free grilling.”

I slapped its chest with my fully spread palm. The cool metal was consumed by the heat of the Flame Divine Palm.

Hisssss!

Molten metal splattered, and a large hole opened in the Golem’s chest. The core supplying its mana cracked apart without resistance.

—Grrrrr…

Rumble!

The enormous body, deprived of its core, lost all its strength. It broke into pieces and collapsed.

Just as a person whose heart had burst could no longer breathe, the same was true of an Iron Golem.

I landed lightly atop the heap of metal that had piled up like a small hill.

“All right. Next.”

—Griiiill!

With a roar like the grinding of machinery, waves of gleaming steel rushed toward me from every direction.

*I wonder if I’ll level up at least once after killing all of these.*

With rising anticipation, I swung my spear.

The Fire Dragon Divine Spear, which had reached the seventh stage, burned through the air and sound as it carved a path of fire.

Fwoooosh!

* * *

Rumble!

The final Iron Golem crumbled with a deafening boom.

It had taken only a few minutes to deal with more than ten A-rank monsters.

When I looked around, everyone was staring at me with astonished expressions.

“This is insane…”

“Did you see that? Did you just see that?”

“Yes. I saw it.”

“Wow, he was playing with an A-rank monster. I couldn’t even see him move.”

“I told you I saw it.”

A voice rang out above the murmuring rookie Guild members.

“Is the raid over already? After combat, clean up the remains and guard the surrounding area. Guild Master and Miss Song, please take charge.”

The words were polite, but the tone was no different from a whip.

Team Leader Choi landed lightly, and the rookies flinched before scattering in a hurry to find something to do.

*He really does have charisma sometimes.*

Was it his unique aura? Something like that had to be innate.

As I was thinking this, Team Leader Choi approached me and spoke with a stern expression.

“Mr. Jin Taekyung. I’ve been thinking about this for a while, but I can’t hold back any longer.”

“Yes.”

“Where did you buy that spear?”

“…”

Right. He had always been this kind of person. I had forgotten for a moment.

Whether or not he knew what I was thinking, Team Leader Choi’s gaze remained fixed on the spear in my hand, White Flame.

“It’s like looking at a work of art. A classical yet beautiful Chinese-style design. Don’t tell me it’s made from Magic Gem?”

*No. It’s made from Ten-Thousand-Year Cold Iron.*

Of course, telling him the truth would only cause trouble, so I gave him a vague answer.

“I couldn’t say. I don’t know much about it myself.”

Team Leader Choi ran his greedy gaze up and down the spear.

“If you don’t mind my asking, would you perhaps consider selling it to me…?”

“No. I’m not selling it.”

Even if I wanted to sell it, I couldn’t. It was a bound item that only I could use. The Item information said so, too.

Perhaps for that reason, it was the only object in my two separate inventories—the ones divided between Murim and the modern world—that could travel between the two worlds.

“Ah…”

Team Leader Choi smacked his lips in disappointment before changing the subject.

“Regardless, I’m truly amazed. You keep getting stronger.”

I answered half-jokingly and half-seriously.

“All it takes is training like hell for a year under a Supreme Peak master with dementia.”

“Dementia? What did you say?”

“A Supreme Peak master.”

“Isn’t that a term from wuxia novels? Peak master, Supreme Peak master.”

“That’s right. I’m thinking of writing a novel as a hobby after I retire. Something like *Login Murim*.”

“That title isn’t very good. It won’t be a hit.”

“I’m not actually planning to write it.”

Team Leader Choi let out a short laugh before speaking.

“I know I say this every time, but whenever I look at you, Mr. Jin Taekyung, I sometimes have a thought.”

“What kind of thought?”

“Whether you and I are really the same kind of person.”

His light brown eyes seemed to grow hot and reddish.

“A perennial F-rank Hunter becoming this powerful in only a few months? If I hadn’t seen you myself, I wouldn’t have believed it.”

It was a reasonable suspicion.

Second-awakened Hunters were uncommon, but there weren’t so few of them that they could be called exceedingly rare.

In my case, however, I had reached a realm far beyond an ordinary second awakening.

And Team Leader Choi had watched my transformation from closer than anyone else.

*Other people might be fooled, but not Team Leader Choi.*

To him, I was no different from a second-, third-, or fourth-awakened Hunter.

I licked my dry lips.

This was a secret I had to keep to myself until the day I died.

If it ever leaked, I might be dragged off by the NIS—or no, NASA—and forced to live as a test subject for the rest of my life.

“Team Leader. I’m sorry, but that’s…”

Team Leader Choi shook his head slightly and cut me off.

“I know. I understand that you have secrets you can’t even tell me. In a way, I’m in a similar position, so I have no intention of pressing you.”

*Similar position?*

Before the question could fully take shape in my mind, he continued.

“A second-awakened Hunter unlike anything ever seen before. That should be enough, shouldn’t it? Butler Kim feels the same way I do.”

Song Song and Im Kkeokjeong had joined later, but Butler Kim had watched my growth from Team Leader Choi’s side.

News articles were already pouring out under headlines like *The F-Rank Hunter’s Rebellion* and *A Miracle*. If the two of them kept their mouths shut, I could probably bring things to an end here.

I dipped my head.

“Thank you. I owe you one.”

“Don’t mention it.”

“But may I ask you one thing?”

“Anything.”

“Why are you going this far for me?”

“Oh, that?”

Team Leader Choi let out an airy laugh.

“You just said it yourself. You owe me.”

“I did.”

“I intend to collect that debt in full—with interest.”

“…?”

“That’s all you need to know. For now.”

Team Leader Choi turned to leave, then stopped.

“That novel you mentioned earlier—if you ever write it, let me read it. I like reading novels more than you might think.”

“Then you won’t be able to read mine.”

“Why not?”

*Because if I ever write it, it won’t be a novel you enjoy. It’ll be an essay based on my experiences.*

Team Leader Choi tilted his head at my silent smile.

* * *

The workshop—or rather, the raid—that had been scheduled to last six nights and seven days came to an end after only three days.

I had gone around by myself and beaten down every monster that caught my eye, leaving nothing else to hunt.

“It was supposed to be a raid for team bonding, but somehow it turned out like this.”

I subtly avoided Song Song’s incredulous gaze.

It wasn’t enough that I had wiped out all the Golems inside the Gate. I had even soloed the boss monster.

*That EXP was so sweet.*

“Ahem.”

“The rookies need to gain raid experience, too. Why are you so desperate to jump in every time you see a monster?”

“Come on, it all worked out. Let it go.”

“Mr. Jin Taekyung.”

“Come on, Miss Song. Let it go.”

“And if I just can’t let it go?”

“I’ll punish you with a confession.”

“…”

Song Song pressed her lips shut and slowly backed away with a frightened expression.

*I achieved my goal, so why do I feel like I might cry?*

*Hah. I loved you…*

I trudged away like the tragic male lead in a romance.

When I exited the dungeon, the reporters who had been camped outside the Gate fired their camera flashes all at once.

Although I had spent an entire year in Murim, only a few days had passed in the modern world.

It would take more time for the interest and fervor surrounding me to die down.

“Please step back, reporters!”

“Only authorized personnel may enter beyond this point!”

Only after the guards rushed in and blocked off the press could I escape the barrage of flashes.

Once the shutter sounds finally stopped, the rookie Guild members, their faces flushed with excitement, shouted loudly.

“Thank you for your hard work!”

Their eyes all shone brightly. They were filled with admiration and respect as they looked at us.

Though, of course, most of that attention was focused on me.

Feeling awkward, I turned my head toward the founding members. That was when I realized someone was missing.

“Where’s Uncle Kkeokjeong?”

“Huh? Now that you mention it, he’s not here.”

Team Leader Choi answered.

“He told me privately on the way here, then slipped away. Apparently something came up.”

“What could be so urgent that he left without even changing out of his gear?”

“It must be urgent if he left like that.”

*What was going on? Had something happened at home?*

A strange unease settled in one corner of my mind.

*Come to think of it, I didn’t get to talk with him much after returning.*

I had spent most of the raid moving alone, so I hadn’t had many conversations with the others.

Looking back, Im Kkeokjeong’s expression had seemed a little dark. At the time, I had thought he was simply nervous, but…

*Did something really serious happen?*

Even after I changed out of my gear and everyone went their separate ways, I couldn’t stop thinking about it.

I debated for a long time whether to call him, but in the end, I sent a quick message to the number saved in my contacts. It simply said that we should grab a drink together soon.

He must have had his own troubles, and prying unnecessarily might be rude.

*That should be enough.*

I was gazing absently at the stubborn number 1 that refused to disappear when—

Bzzzzt.

My smartphone vibrated. A phone icon appeared on the screen, along with the saved name.

It was a name I had saved several months ago and completely forgotten about.

**Garam Middle School Classmate Park Jihoon**

He was someone I had happened to run into the day I went to buy a house, and we hadn’t spoken once since.

*What could he want?*

With mild curiosity, I answered the call.
## Chapter artifact 272

# Chapter 272

“Hello?”

The voice coming through the phone sounded unfamiliar.

The Park Jihoon I remembered from middle school hadn’t even finished going through his voice change, and since then, the only time we had spoken was during a brief, passing conversation a few months ago.

*Is this really him?*

I was hesitating when he spoke again.

“Is this Jin Taekyung’s number?”

“Oh, yeah, it’s me. I thought I might have reached someone else.”

“What the hell? You didn’t save my number last time?”

“I did, but for a moment I thought you might’ve called the wrong number. Your voice didn’t sound familiar.”

“Fair enough. It was the first time we’d seen each other since middle school.”

“Yeah. I didn’t recognize you back then, either.”

“Of course you didn’t. Do you have any idea how much money I poured into this face?”

A low laugh came through the phone. There wasn’t a trace of awkwardness between us; the mood felt warm and familiar.

I laughed along as I climbed into the VIP limousine provided by the Gate Management Agency. The driver met my eyes in the rearview mirror and gave me a polite nod before smoothly pulling away.

“But what’s going on?”

“Nothing much. I called to ask if you wanted to grab a drink.”

“Drinks? Out of the blue?”

“Yeah. I said I’d get in touch when we had our class reunion, but I couldn’t.”

*Had he?*

Thinking back, it seemed like he had. I’d been so busy since then that I’d completely forgotten.

“Something suddenly came up, and I had to go on a business trip overseas. I couldn’t even attend the reunion because of it.”

“An overseas business trip?”

“There was a problem at our European branch. I only got back recently.”

*I went to Murim, and this guy went to Europe.*

I had no idea what he’d done there, but for some reason, I felt cheated.

I spoke with as much envy as I could muster.

“You lucky bastard. Must’ve been nice sightseeing overseas.”

“You’re jealous of me? You?”

Park Jihoon laughed out loud on the other end of the line.

“That sounds really strange coming from you. Were you just rubbing it in?”

“No, that’s not what I meant.”

“I’m kidding. So, are you free tonight?”

I glanced at the time. It was already eight in the evening.

I’d moved out of our family home and into an officetel in Bucheon three days ago, so even if I went home, the only person waiting for me would be Jinho hyung.

I had time. The problem was…

*He doesn’t have some other motive, does he?*

But I only hesitated for a moment.

I’d been a Hunter for seven years. The close friends I’d been inseparable from during my school days had gradually stopped contacting me a long time ago.

The saying that people grew distant when they were separated by distance didn’t apply only to romantic relationships.

And yet here I was, suspecting a friend who had contacted me after all this time without any ulterior motive.

*Have I developed a distrust of humanity?*

The aftermath of the Won Myunghoon incident, along with the harassment I’d endured from certain trash reporters, must have left a lasting mark. I was left with a bitter taste in my mouth.

“You must be pretty busy. I suppose that makes sense. Then maybe next time…”

“No, I’m free now. Where should we meet?”

A little while later, the limousine turned off the road it had been gliding along.

* * *

“You got here faster than I expected.”

Park Jihoon had arrived ahead of me and was waiting outside.

The weather was gradually turning toward winter. Wearing a cashmere coat over a crisp white shirt, he looked completely different from me.

“What’s with the outfit? Why are you dressed up so much?”

“I have something important to take care of today. And let’s get one thing straight. It’s not that I’m dressed up—you’re dressed down.”

“What’s wrong with what I’m wearing? Jeans and a sweatshirt are perfectly fine.”

This was me making an effort, too. Hayeon had kept squawking about how many people were watching me and telling me to stop wearing tracksuits.

“Where did all the money you earned go…? Oh, right. You donated it.”

“Don’t bring that up. It still hurts.”

“That’s why I called you. Alcohol is the best medicine for a sore stomach.”

Park Jihoon gave me a broad grin and jerked his chin toward the entrance. Then he started walking.

We passed a uniformed security guard and countless surveillance cameras installed throughout the grounds before finally making it inside.

The sight that greeted me left me speechless.

*What the hell is this?*

The marble floor glittered in the light, while paintings that looked as though they had come straight out of the seventeenth century hung in frames along the walls.

*I think I saw that one in an art textbook. There’s no way it’s genuine, right? Yeah. It can’t be.*

I followed him, looking around like a country bumpkin.

We stopped in front of five elevators installed side by side.

There weren’t even any buttons, so I had no idea what I was supposed to do. Then Jihoon placed his hand on a black panel, and an elevator descended in the blink of an eye with a mechanical whine.

Bzzzzing.

“What are you doing? Get in.”

“…Wow.”

“What are you so surprised about?”

“Nothing. I just thought you said this was an officetel.”

“It is. An officetel.”[^1]

“…”

The officetel he knew and the one I knew seemed to be two entirely different things. I swallowed the words that were about to come out.

Maybe it was because we were in Cheongdam-dong, but the place practically reeked of wealth from the moment we entered.

“You really made it. You even bought a place like this.”

“There was a property on the market recently, so I bought it. I thought I could drop by sometimes and clear my head.”

Anyone listening to him would think he’d bought a pair of shoes.

While I was shaking my head in disbelief, the elevator stopped and the doors opened. Instead of a cold, dark hallway, a gray-toned living room spread out before me.

I didn’t know the exact square footage, but the living room alone was about the same size as our family home.

“Come in.”

I didn’t know whether he’d really bought the place to clear his head, but one thing was certain: I had never been anywhere like it.

The enormous sitting area and wine cellar installed in the living room made it look as though someone had picked up an upscale bar and moved it inside.

After taking off his coat, Park Jihoon asked me,

“What do you want to drink?”

“What do you have?”

“Château Cheval Blanc, Screaming Eagle Cabernet Sauvignon, Royal de Maria…”

*What the hell is he talking about?*

I blinked at the stream of alien words before asking,

“Chateau Shibal, what?”[^2]

“Château Cheval Blanc.”

I didn’t know whether it was château or shatto, but every single name was impossibly difficult.

After a brief silence, I opened my mouth.

“Don’t you have any somaek?”

Park Jihoon let out a short laugh.

* * *

We piled up a whole crate of soju and another of beer, then drank without pause.

It had been eleven years since we’d lost touch in the third year of middle school, so we had enough things to talk about to fill a mountain.

“Do you remember that guy named No Jaehun from the class next door?”

“Who was No Jaehun?”

“The tall guy who bragged about working out at the gym. Anyway, when he got into a fight with Seon Woongje from our class, you—”

“Wait a second. Who the hell is Seon Woongje?”

“…”

“Are you suffering from amnesia or something?”

We talked about everything from trivial memories of middle school to what we’d been doing since we lost touch.

The only time either of us stopped talking was when we were drinking.

At some point, I realized that the corners of my mouth had been raised for quite a while.

*This is fun.*

What should I call it? Drinking with someone you felt comfortable with was always enjoyable, but sharing the same memories made the experience a little more special.

The atmosphere was so warm and friendly that I felt like an idiot for having suspected him, even for a moment, during our phone call before meeting.

I also learned a few things about him that I hadn’t known before.

“You were born with a silver spoon?”

“What makes you say that? My father just runs a small business.”

“A Hunter-related business that he’s been running for more than thirty years?”

“Yeah.”

“That makes you a silver-spoon kid, you deceitful bastard. The people who talk like you always turn out to be genuinely rich.”

I looked at him.

It wasn’t that he suddenly looked different now that I knew he was rich. I just found it fascinating.

The neighborhood where we’d lived back then had been perfectly ordinary. If it hadn’t been, someone like me—whose grades had been determined by rolling a mechanical pencil to guess the answers—wouldn’t have been able to get in.

By contrast, the Hunter industry was practically a gold mine.

If his family had survived for thirty years amid fierce competition between companies, it wouldn’t have been strange if gold bars were rolling around their house.

“Why are you looking at me like that?”

“It’s strange. Don’t rich kids usually go to Gangnam’s famous School District 8 or somewhere like that?”[^3]

“I guess I’m not a rich kid, then. Besides, I transferred in, remember?”

“You transferred? That’s the first I’ve heard of it.”

“Yeah. In the second year of middle school. There was no particular reason to mention it.”

“Wasn’t there?”

“No.”

I tilted my head and took another drink.

He had a point. What importance could transferring schools in middle school possibly have? It had been more than ten years ago, anyway.

“We only met for the first time in our third year of middle school. We hadn’t crossed paths before then, so it makes sense that I wouldn’t know.”

“But we crossed paths plenty of times.”

“Huh?”

“The day after I’d been at the school for a week, I saw you for the first time in front of the teachers’ office. Then we ran into each other in the hallway. We even crossed paths in the bathroom.”

Fragments of memories from more than ten years ago—already blurred and covered in static—flowed from Park Jihoon’s lips.

“Wow… How do you remember all that?”

His smooth lips curved into a smile.

“I have a better memory than I look like I do. Unlike some people.”

I topped off his empty glass and chuckled.

“Hey, even if my memory is terrible, I remember one thing.”

“What?”

“You never did your homework. Every time we had a test, you guessed your answers, then put your head down and slept.”

“Oh, that.”

“If you had such a good memory, why were your grades in memorization-heavy subjects so terrible? Did you go to college—ah, is that rude to ask?”

“What’s rude about it? I don’t care.”

“Then that’s a relief.”

“And I did go to college. Hankuk University, Business Administration. I awakened suddenly, so I still haven’t graduated.”

“Wait, where? Hankuk University?”

“My parents wanted me to go.”

“…You crazy bastard. Are there parents who don’t want their child to get into Hankuk University?”

Hankuk University was the most prestigious university in the country. Only the brightest students from across Korea could get in.

Park Jihoon laughed lightly at my incredulous stare.

“When I tried, I got in. It wasn’t as hard as I expected.”

“Huh.”

What should I call it? The more I listened to the story of his life, the more I thought of a wide-open highway.

A wealthy family, a sharp mind, admission to the university everyone dreamed of, and then becoming an A-rank Awakened in one shot.

Unlike me, who had been forced to provide for my family, Hunter work had been just one of countless options available to him.

“Why?”

“Huh?”

“You were looking at me strangely.”

“Was it that obvious?”

“Very. Taekyung, are you perhaps…”

Park Jihoon rested his chin on one hand.

His voice continued in a low murmur, thick with alcohol.

“Are you jealous of me?”

Jealous?

It was such an unexpected question that I stared blankly for a moment. Then I burst out laughing.

“Yeah. I guess that’s what it is.”

“…You’re honest.”

“It’s true. Admiration for something I couldn’t have? Envy, I guess. Something like that. Of course, I don’t regret anything. I worked hard enough.”

Park Jihoon stared at me, his eyes widening slightly as though he hadn’t expected that answer.

“You get jealous of people, too.”

“Hey, what am I, some kind of big shot?”

“You are. Look at you now. You’re a Hunter drawing attention from foreign media as well as the domestic press. Before long, you might even join the ranks of Korea’s five S-rank Hunters.”

“That sounds impressive—except I’m also the guy trembling with regret over making a donation.”

I let out a short laugh and emptied my glass. Park Jihoon gazed at me for a while, then his lips began to move as though he were about to say something.

That was when—

Bzzzt.

The smartphone on the table began to vibrate. Park Jihoon stared intently at the screen and licked his lips.

“Who is it?”

“My Guild Team Leader.”

“At this hour? Does the Myeongdong Guild have some kind of twenty-four-hour standby team?”

“Nothing like that. It’s something important.”

“Then…”

“I’m sorry, but I think we’ll have to call it a night.”

“Don’t apologize. It’s not as though we don’t understand each other’s circumstances.”

I set down my glass and stood. Then I gave Park Jihoon, who was looking at me with an apologetic expression, a light tap on the shoulder.

“I had a good time tonight.”

I meant it. Now that I had become a famous person in the modern world, there were very few people with whom I could have a completely selfless conversation like this one.

I stopped him when he tried to accompany me into the elevator.

“I’m heading out. Don’t come out just to see me off. Take care of your problem.”

A faint smile appeared around Park Jihoon’s mouth.

“Okay. Let’s meet again next time. We will.”

With those final words, the elevator doors closed.

* * *

Park Jihoon stood in front of the window and looked down.

A lone figure was leaving the entrance of the officetel amid the darkness that had swallowed the city.

“Hello? Mr. Jihoon? Mr. Jihoon?”

“Go ahead.”

“Ah, we finally connected. You were listening, so why didn’t you say anything…?”

“I think you’ve misunderstood something, Team Leader.”

The other person’s breathing faltered at the dry voice.

Park Jihoon lifted a crystal tumbler to his lips. Instead of the somaek he had been drinking moments ago, amber whiskey rippled inside.

“From now on, wait until I speak. And stop trying to play boss with me.”

Park Jihoon, Hunter of Team 1 in the Myeongdong Guild.

That was the affiliation printed on his business card.

But the Team Leader of Team 1 in the Myeongdong Guild remained silent on the other end of the phone.

They both knew the truth. That title was nothing more than a hollow position.

“You’re not answering.”

“…Understood.”

“So what is it? This important report of yours?”

The Team Leader of Team 1 answered carefully.

“You know Team Leader Jung Hyunwoo, right? The one in charge of Team 8.”

“Of course I do. He’s skilled, but his flexibility doesn’t come close to matching even half of his ability. That’s the problem.”

“It seems he’s caught the scent.”

“Really? He’s more perceptive than I expected.”

“Yes. But what should we do about it…?”

“What are you hesitating over? Arrange a raid for the earliest available date. A-rank.”

“You mean…”

“Team Leader, do you know how many Gate accidents happen in a year? I don’t. No one else does, either. Nobody cares.”

“…”

Park Jihoon clicked his tongue.

“You’re not answering again.”

“Ah, understood.”

“And regarding the Peace Guild—or, more precisely, the Jin Taekyung matter…”

Park Jihoon’s voice trailed off.

The face of the man who had smiled and tapped him on the shoulder came to mind.

*I had a good time tonight.*

It had been a sincere statement.

And that made Park Jihoon even less willing to stop.

“Mr. Jihoon?”

Park Jihoon tossed back the rest of his whiskey.

The crystal tumbler crumpled in his hand like a sheet of paper.

“I finished speaking with the higher-ups today. They find him irritating.”

That was all it took. One passing remark during dinner with *that person*. The matter was as good as settled.

“What? But this isn’t really the right time for something like that…”

The Team Leader’s startled protest was cut off by Park Jihoon’s cold voice.

“Isn’t it only natural for a gardener to pull weeds growing in the lawn? Your Guild Master has probably already heard the news. I’m hanging up.”

Click.

The call ended.

In the quiet that followed, Park Jihoon stared through the spotless window at the scene outside.

Jin Taekyung had disappeared a long time ago.

[^1]: An officetel is a Korean mixed-use unit designed to function as both an office and a residence.

[^2]: “Shibal” is a Korean profanity; here, Taekyung mishears the similar-sounding “Cheval.”

[^3]: Gangnam’s School District 8 refers to one of Seoul’s most prestigious education districts, associated with affluent families and elite schools.
## Chapter artifact 273

# Chapter 273

“Good morning!”

“Good morning!”

I felt like a mob boss. Every time I took a step, rookie Guild members bowed ninety degrees and greeted me from every direction.

They were fresh out of training camp, still green as grass. In terms of years on the job, I was certainly their senior by a wide margin.

*This industry does take seniority and junior status pretty seriously.*

The problem was that some of the rookie Guild members were late-blooming Hunters older than me.

“It’s an honor to meet you!”

A rookie who looked to be well into his mid-thirties bowed with his eyes shining brightly.

Then I saw his crown shining even more brightly than his eyes, and my heart ached.

“Yes. Good luck…”

“Thank you!”

“Thank you!”

Was that an echo or something?

And I wasn’t talking to all of you. You full-haired bastards.

I was looking at the rookies while clicking my tongue inwardly when my gaze suddenly stopped on one young man.

*That one might actually be useful.*

He was the best among the new recruits. The energy I sensed from him was impressive, and every movement he made was restrained like that of a martial artist.

The young man, noticing my gaze, gave me a broad grin.

“Good morning, Senior.”

He was definitely different. Unlike the other rookies, he wasn’t nervous or obsequious.

In my experience, people like him fell into one of two categories.

Either they had absolutely nothing to back up their pride, or they were confident in their own abilities.

The guy standing in front of me belonged to the latter category.

“You there. What’s your name?”

“My name is Kim Jinsoo. I graduated at the top of the B-rank course at the training camp. I was also the first person to destroy a Golem’s core during this raid.”

“Really?”

“Yes. It was my first time in an A-rank Gate, but it wasn’t as difficult as I expected.”

What an interesting guy.

He had no hesitation about gilding his own face. He was the type who would always make sure he got his share wherever he went.

When I stared at him, Kim Jinsoo laughed good-naturedly.

“And you can speak comfortably with me, Senior.”

“We just met. I’ll drop the formal speech once we get more comfortable. The same goes for everyone else, so I’d appreciate it if you skipped the loud greetings from now on.”

“Yes!”

“I’ll keep that in mind, Senior!”

“…”

He wasn’t listening at all.

The deafening noise echoed through the hallway, and the office door at the far end slowly opened.

A stiff white shirt and neatly ironed black slacks. There was only one Hunter in our Guild who came to work dressed like that.

“You’re lively this morning.”

“Too lively, if you ask me.”

Like a scene from a commercial, Team Leader Choi held a coffee cup and jerked his chin toward the office.

“Come in and have some coffee. Let’s calm things down.”

* * *

The office was spacious and comfortable. Perhaps because it had been decorated to suit Team Leader Choi’s tastes, expensive furniture was scattered throughout the room, and a silver nameplate sat on the desk.

**Team Leader Choi Minwoo**

*Even the nameplate looks expensive.*

Moving the Guild House and recruiting all those new Guild members must have cost an enormous amount of money. Apparently, it was true that the Peace Guild had extracted an astronomical settlement from the Star Guild, where Won Myunghoon had been Guild Master.

As I was admiring the nameplate, a cup filled with black coffee suddenly appeared in front of me.

Team Leader Choi followed my gaze and asked,

“Would you like me to have one made for you? A nameplate.”

“I’m fine. I don’t actually have a position or anything.”

“We can always create a position. General Team Leader. Head of Headquarters. Whatever you want.”

“Anything?”

“Yes.”

“Then something modest. Guild Master.”

“…”

“I’m joking. If I became Guild Master, I’d run the Guild into the ground.”

Besides, even if I did become Guild Master, I would obviously just be a figurehead. What would be the point?

I accepted the coffee and sat down on the sofa. More than twenty newspapers were stacked on the glass table.

They ranged from the major domestic daily papers to foreign newspapers filled with writing I couldn’t even begin to understand. Just looking at them made my eyes spin.

“You actually read all of these?”

“I read them to keep track of overseas developments and collect industry information. It’s nothing special. Knowing around five languages is enough to read them.”

“…”

That was extremely special. Five languages? What kind of life had this man led?

Shaking my head in amazement, I glanced at one of the open newspapers.

A vivid color photograph of a man who looked to be in his thirties caught my eye, along with several headlines printed in bold.

- The late Hunter Jung Hyunwoo (photo attached)
- Accidents continue. The Gate—a space of death that even A-rank Hunters cannot escape.
- Myeongdong Guild expresses regret over the deceased’s untimely death…

It looked like there had been another accident.

*The Myeongdong Guild? That’s Jihoon’s Guild.*

Just as I was about to look more closely, Team Leader Choi elegantly tilted his coffee cup and continued.

“The Peace Guild will continue to grow. We’ve already recruited twenty B-rank Hunters and thirty C-rank or lower Hunters. That kind of growth is unprecedented in the domestic market, which has become thoroughly stagnant.”

Just as he said, the Peace Guild’s growth was terrifying.

Only about four months had passed since the Guild was founded, but if we maintained this momentum, it wouldn’t be an exaggeration to call ourselves a mid-sized Guild.

*Of course, compared to other mid-sized Guilds, we’re still seriously lacking in the number of affiliated Hunters.*

That was because we hadn’t recruited more people yet, not because we couldn’t.

The fact that the Guild’s website had gone down due to excessive traffic was proof enough. I’d heard that hundreds of employment-related inquiries came flooding in every day.

“And I played a major role in that. The biggest contributor.”

“That’s true.”

Team Leader Choi continued smoothly.

“It is true, but I’m not giving you a bonus.”

“…You’re quick to catch on.”

I’d tested the waters just in case, but it hadn’t worked at all.

As he watched me silently smack my lips, Team Leader Choi smiled.

“However, I’ll think about it positively if you do me one favor.”

“What favor?”

“I’d like you to take charge of the rookie Guild members for a while.”

“…The rookies?”

“Yes. We carefully selected and recruited them, and they all have talent. But they’re still rather clumsy in many ways.”

“Of course they are. They’re beginners.”

No matter how much training someone went through, the atmosphere of a real battle was different from the air in a training camp.

There was a reason people said that a lower-rank Hunter with ten years of experience was better than a top Hunter who had just finished training camp.

“But why me? There are other people here.”

“I already spoke to Butler Kim and Song-i this morning. I suggested that we all take turns teaching the rookies.”

“What did they say?”

“They agreed. Very willingly, without the slightest hesitation.”

“…What about Uncle Kkeokjeong?”

“I haven’t been able to ask him yet. He’s long past his usual arrival time, and he isn’t answering his phone.”

Team Leader Choi checked the time and continued.

“Wouldn’t it be a good idea? The rookie Guild members are hoping that Mr. Jin Taekyung will teach them, too. Most of them applied to our Guild because of you.”

“Thank you for putting me on a pedestal and all, but…”

I scratched the back of my head.

Dark Heaven had revealed its fangs in Murim, and Jeok Cheongang was still unconscious.

Even if I spent thirty days in the modern world, only three hours would pass in Murim. I had time to spare, but with A-rank Gates to clear, teaching a bunch of greenhorns wasn’t exactly the most rewarding use of it.

If I was going to spend that time on something, being with my family would be a hundred times better.

“Leave me out of it. From the Guild’s perspective, wouldn’t it be more efficient for me to clear another A-rank Gate instead of teaching those guys?”

“More efficient…”

“Yes. Efficiency.”

“Then I suppose it can’t be helped.”

A sinister smile formed around Team Leader Choi’s mouth.

“I’ll be counting on you with our rookie Guild members.”

“What?”

“All the A-rank Gates have been booked solid. You won’t have a chance for at least the next week.”

“Don’t lie to me! You scam artist!”

“If you don’t believe me, you can see for yourself.”

I snatched the paper Team Leader Choi held out. It was densely covered with the reservation schedules for A-rank Gates across the country.

Damn it. He was telling the truth.

“I’ll give you a 200 percent performance bonus this month. You get to go on raids and teach your juniors. How wholesome.”

“…”

“Or you can stay home and do nothing.”

The corners of Team Leader Choi’s mouth rose in an infuriating smile.

I was just about to shout, *I’m not doing it!*, when the System notification rang.

Ding.

> **System**
>
> - The Quest **It Was Too Much Money to Say “I’m Not Doing It!”** has been generated!
>
> Will you accept the Quest?
>
> Y   /   N

“What do you say?”

“…”

“I’ll take that as your acceptance and get the rookies ready. I’ve already reserved a few B-rank Gates.”

Ding.

> **System**
>
> - You have tacitly agreed.
> - You have accepted the Quest!

Goddamn it.

* * *

—Grrrrr.

The rough breathing of monsters closed in from every direction. Twenty pairs of anxious eyes swept across the surroundings.

Huff. Huff.

Their breathing grew ragged, and the hands gripping their shields and weapons turned white.

I was sitting astride a branch high above the ground, watching the scene unfold.

My expression was blank, but my head was filled with a serious dilemma.

*What should I eat for dinner?*

Should I have galbi, or whole boiled duck for the first time in ages?

Both options were too good to give up…

“Hold the line!”

“What are the damage dealers doing? Damage dealers!”

At the sound of those shrill screams, I looked over. It was chaos.

More than a dozen Lycanthropes were charging in and pounding on the shield wall. The pale-faced tanks were being pushed back in a line.

*They’re getting pushed back because they’re trying to fight the monsters with brute strength.*

Of course, it wasn’t entirely the tanks’ fault. The damage dealers were also too flustered to do their jobs.

If they had landed suppressive attacks at the right moments, this situation wouldn’t have happened in the first place.

I had warned them several times before the raid began, but they were still making the same mistakes.

*That’s going to break any second.*

The moment I thought it, the shield wall collapsed amid a chorus of screams.

A gap opened in an instant. One of the most agile-looking Lycanthropes charged through with a characteristic roar.

Its bright yellow predator’s eyes turned toward the healers hiding behind the shield wall.

—Graaaargh!

—Awoooooo!

To me, it sounded no different from a dog barking, but these rookie Hunters, who were only beginning their second raid, were terrified.

“Aaaah!”

“Eeeek!”

The screams of the mage and healer shook the darkened forest.

*It’s already noisy enough. Those screams are going to draw another twenty or so over here.*

I memorized the faces of the two people who had screamed.

*From now on, their nickname is the Pied Pipers.*

“Senior! Senior Jin Taekyung!”

“Please help us, Senior!”

Several round faces looked up at me and cried out desperately.

The front line had already collapsed, and there was nothing behind the rookies except one enormous boulder.

The Lycanthropes closed in, tightening their encirclement with triumphant momentum.

*How did the monsters end up being better at forming ranks than they are?*

I wiped the sleep from the corner of my eye and answered.

“I told you. If I help, your skills won’t improve.”

“Even if they don’t improve, that’s fine!”

“I’m not fine with it. You know what happens if you make a habit of getting help? You make a habit of shitting the bed during raids, too.”

“Even so, I don’t want to die like this!”

“But… nobody wants to die, do they?”

“Please help us!”

“Don’t give up. Fight a little harder. You can do it!”

“Please save us!”

“By the way, which should I have for dinner—galbi or boiled duck?”

“Hey, you fucking bastard!”

It was the balding rookie from that morning. The admiring light that had shone as brightly as his crown was gone, replaced by a gaze full of fury.

“Get down here, you young bastard…”

Thud!

A tank came flying in from somewhere, sending the balding rookie sailing far into the distance with him.

The momentum had effectively shifted to the monsters. I was wondering whether it was time to step in when—

Shhk!

—Kauuugh…

With a flash of light, one of the Lycanthropes let out a groan. Blood gushed from its split-open neck, and it soon collapsed.

The young man who had landed an accurate and powerful strike shouted with all his might.

“Formation Three!”

His booming shout brought the others back to their senses one by one.

Before long, the twenty Hunters had formed ranks and begun advancing slowly.

At the front was the young man, Kim Jinsoo.

“Keep pushing! Archers, get your skills ready!”

*That kid has potential.*

I let out a short laugh and jumped down from the tree. Then I swung my spear at the dozens of Lycanthropes that had been drawn over by the sound of battle.

Whoooosh!

* * *

“You did well.”

“Thank you, Senior!”

Kim Jinsoo grinned and bowed. Behind him, I saw three people with their heads pressed into the ground.

Two of them were the Pied Pipers, and the last was the balding rookie.

I gave the balding rookie the special privilege of holding the push-up position.

He had to protect whatever little hair he had left…

“Keep it up next time, too. You’ll improve quickly.”

“Yes. I won’t disappoint you, Senior.”

“Then go get some rest, Jinsoo. You have another raid in two hours anyway.”

Team Leader Choi was really going all out. He had scheduled three raids in a single day.

I was grinding my teeth inwardly when the phone in my pocket began to vibrate.

**Designer-Brand Junkie**

What was this? Had we developed telepathy?

I answered the call, still baffled, and Team Leader Choi’s urgent voice struck my ear.

“Taekyung. Come to Ilsan Hospital right now!”

Hospital?
## Chapter artifact 274

# Chapter 274

*Hospital? Why so suddenly?*

I was just about to ask what had happened when the call ended amid the sound of hurried footsteps.

I tried calling back two or three times, but it was no use.

—The number you have dialed cannot be reached. After the beep, you will be connected to voicemail…

I hung up when the automated message began repeating. A creeping unease rose from somewhere in my chest.

This was the first time. Team Leader Choi was always calm, but he had sounded so frantic.

*Could it be…?*

No. Don’t jump to conclusions already.

This wasn’t the time to think. It was time to move.

*Ilsan Hospital. He said Ilsan Hospital.*

I grabbed my things and left the changing room. The rookies waiting outside turned their heads when I appeared.

Kim Jinsoo, who had been chatting animatedly in the middle of the group, sprang to his feet.

“Ah, Senior. Are we leaving right away?”

“No. Something urgent has come up.”

As it happened, this worked out perfectly. There were two hours until the next raid, and thankfully, the next Gate was nearby. It wouldn’t take long to get there.

“Mr. Kim Jinsoo.”

“Yes.”

“You’re the acting team leader for the next two hours.”

“What?”

“Take the others to the next Gate. And don’t start the raid under any circumstances until I get there.”

Kim Jinsoo nodded with a dazed expression. I gave him a light tap on the shoulder, then hurried out of the building.

I climbed into the taxi that had been waiting for a passenger, told the driver where to go, and immediately started making calls.

*Pick up. Please pick up.*

Ring. Ring.

The longer the ringing continued, the more anxious I became.

Just as the signal stretched on and I was about to hang up and call again—

Click.

“Hey, son.”

“What? Is that my brother?”

“Be quiet. Don’t touch the phone while you’re eating.”

“Seriously? Is what Mom’s holding a brick instead of a phone?”

“You little brat!”

“Whew.”

Thank God. It wasn’t them.

The tension drained from my body when I heard my family’s voices on the other end of the line.

I gave Mom a vague excuse when she asked what was going on, then hung up.

*Then it must be a problem with the Guild.*

Who was in trouble?

If Team Leader Choi wasn’t answering, the person who would have the clearest understanding of the situation was Butler Kim.

But then someone else’s face flashed through my mind. His noticeably reduced number of words. The heavy expression he had been wearing lately.

*Uncle Kkeokjeong.*

My guess had been right.

When I called the number saved in my phone, I was greeted not by Im Kkeokjeong’s gruff voice but by a cold mechanical message.

—The phone is turned off. After the beep…

* * *

When I arrived at the hospital as though flying, Song Song was waiting for me at the entrance with an anxious expression. She had apparently been contacted in advance.

“You’re here?”

“Tell me while we walk.”

As soon as we passed through the revolving doors, the hospital’s distinctive smell lingered around the tip of my nose.

Civilians, Hunters, hospital employees—people of all kinds crowded the building. We pushed our way through them as we walked.

A few people who recognized me pulled out their phones and started taking pictures.

“Hey, hey. Look over there.”

“That’s Jin Taekyung.”

“Jin Taekyung? Lord Fuck?”

“Wow, he looks incredible in person.”

I forced down the stress that was surging through me.

As the crowd parted like the Red Sea, I whispered to Song Song.

“What happened?”

“I don’t know all the details, either…”

“Tell me what you do know.”

She bit her lip.

“He seemed to have a lot on his mind lately.”

“On his mind?”

“You know how things are. The Guild keeps growing, and talented young rookies keep joining…”

“That’s enough. I know what this is about.”

Im Kkeokjeong had been with the Peace Guild since its earliest days. But he was also the only D-rank Hunter among us.

After the Peace Guild began attracting attention from the media along with me, rumors about him had begun circulating as well.

People called him the Guild’s only weak link. Some even left hateful comments telling him to quit instead of trying to ride our coattails.

Im Kkeokjeong had laughed heartily while stopping us from getting angry over it.

And yet…

“Whew.”

My chest felt tight.

I had promised myself that I would always look after my people, but I had failed to pay enough attention to someone close to me.

“So what happened after yesterday’s raid?”

“Apparently he went out for a drink alone and got into an argument.”

“Go on.”

“I heard he was drunk when the fight started… He was badly injured.”

My heart dropped.

Strangers could say whatever they wanted about him being a low-rank Hunter or anything else, but Im Kkeokjeong was a D-rank Hunter with twenty years of experience.

Even if ten grown men attacked him at once, they wouldn’t be able to bring him down.

“So the other side were Hunters.”

Song Song gave a small nod.

“How badly was he hurt? Is it serious?”

“His treatment is finished for now, but…”

Song Song hesitated, unable to continue, then stopped walking.

A sign reading *Special Treatment Ward* swayed above her head.

This wasn’t a ward staffed by doctors, but by practitioners known as healers.

That alone showed how severe his injuries were.

“You’d better see for yourself.”

With a sigh-like murmur, Song Song opened the hospital-room door.

Creak.

Along with the harsh smell of medicine, I saw three people pacing around the bed.

Team Leader Choi. Butler Kim. And a middle-aged woman who I assumed was Im Kkeokjeong’s wife.

My heart pounding, I approached the bed.

“……Uncle?”

Hhhk. Hhk.

Instead of an answer, I heard a faint, ragged breath. Im Kkeokjeong lay beneath the pure white sheets with an oxygen mask over his face.

And then…

The hairy arm that he habitually used to pull me into a tight hug had been cleanly severed just below the elbow.

* * *

The silence was long.

Even after leaving the hospital room and climbing to the rooftop, I couldn’t figure out what I should say first.

I listened quietly as Team Leader Choi and Butler Kim explained what had happened. At last, I opened my mouth.

“Where are those bastards now?”

Everyone present knew exactly who I was talking about.

Team Leader Choi’s lips moved. Then he silently shook his head.

*No way.*

“You didn’t catch them?”

“No. All three fled the scene.”

“What about the CCTV footage? They were drinking at a store. Their faces should have been recorded.”

“The investigating authorities have already been there. They’ve also reported the results.”

These days, CCTV footage was as clear as anything shot on a proper camera. If the bastards’ faces had been captured clearly, it should only have been a matter of time before they were caught.

There weren’t many Hunters and Awakened people in the country, which made them easier to track down.

“Then that’s fine. We’ll find those bastards right away and—”

“They say their identities are unknown.”

“What?”

Had I heard him wrong?

When I stared at him in bewilderment, Team Leader Choi continued with a sigh.

“Their identities are unknown. Apparently, they aren’t any Awakened or Hunters registered as existing in this country.”

“……Could they be Korean-Chinese? Chinese or Japanese?”

“No. According to the witnesses, the suspects were definitely Korean. They were also the ones who started the argument.”

“Then what the hell is going on…”

Butler Kim, who had been listening silently to my conversation with Team Leader Choi, suddenly spoke.

“They may be Black Hunters.”

Black Hunters?

The term itself sounded filthy. Butler Kim continued in a low voice.

“Not every Awakened person is registered with the Gate Management Agency and the Association.”

I wondered what he meant by a term I had never heard before.

Rubbing my throbbing temple, I asked,

“Isn’t that just an unregistered Awakened person?”

In modern society, Awakened people were both powerful shields that protected the world from Gates and dangerous blades that had to be handled with care.

Even the lowest-rank Hunter possessed strength far beyond that of an average human.

That was why Awakened people were always subject to strict oversight.

Even if they had no intention of becoming Hunters, their names were still included on the list of Awakened people.

The only time someone was removed from the list was after they died.

*Unregistered Awakened* was simply a term for an Awakened person who had failed to register with the Association within the designated period.

Of course, sometimes they were called something else.

*Crazy bastards.*

There was a reason unregistered Awakened people were treated like lunatics.

If they didn’t voluntarily report their Awakening within a month, they stopped being Awakened people and became inmates instead.

Suspended sentences or any other bullshit didn’t matter. They were thrown straight into an Awakened-person prison, and when they were released, they even received an electronic ankle monitor as a free gift.

Who would be crazy enough to gamble their entire life like that?

“Are there still lunatics like that these days?”

“There always have been, and there still are. Isn’t that why crimes continue to occur without end?”

“So the people who attacked Uncle Kkeokjeong were unregistered Awakened people. Then how do we find them…”

Butler Kim cut me off gently.

“They were Black Hunters.”

“Yes. In other words, unregistered Awakened people.”

“They’re different.”

Butler Kim stroked his neatly trimmed beard and continued.

“Hunter Jin Taekyung, what do you think is the greatest difference between an Awakened person and a Hunter?”

It was an unexpected question. I felt as though we were going around in circles.

If the person asking hadn’t been Butler Kim, I might have said something.

Suppressing the anger boiling inside me, I answered.

“Training. Just because someone owns a gun doesn’t make them a hunter.”

“Unregistered Awakened people and Black Hunters are the same way.”

“So what you’re saying is…”

Butler Kim nodded.

“Exactly. An unregistered Awakened person who has received systematic training like a Hunter. That is a Black Hunter.”

I was stunned for a moment.

It was a very simple concept when you thought about it, but I had never considered it before.

And for good reason.

“How is that possible?”

An unregistered Awakened person was a serious criminal. Where would they obtain weapons, and who would provide them with systematic training?

“Are criminal organizations raising Black Hunters? Something like that?”

“Criminal organizations… That’s half right and half wrong.”

“Then what is it?”

The next moment, a short answer burst from Team Leader Choi’s mouth.

“Guilds.”

“……What?”

“Money gathers wherever people gather. And wherever money piles up, disputes are bound to follow. Do you really believe today’s Guilds exist purely to protect the world from the monsters inside Gates?”

I couldn’t answer.

I hadn’t become a Hunter to protect the world, either.

The Great Cataclysm was already a thing of the past. When people thought of Hunters, they no longer imagined noble duty or a spirit of self-sacrifice.

They envied the money and fame Hunters possessed, and the people who grew up watching that became Hunters themselves.

The collection of those Hunters was a Guild.

“Do you know the domestic business rankings? From first to tenth place. On the surface, they are all private companies, but in reality, they are little more than puppets of massive Guilds. Things aren’t much different overseas.”

Team Leader Choi let out a cold laugh.

Only then did I finally begin to emerge from my shock.

“Is… is all of that really true?”

“You once asked me why I left Ares Guild.”

Team Leader Choi didn’t continue, but I understood what he meant.

They were all pieces of shit in the same cesspool.

To them, Black Hunters were daggers hidden up their sleeves. No one knew they existed.

No, they might know and simply pretend not to.

While I was still reeling, another unanswered question came to mind.

“Fine. Let’s say all of that is true.”

I took a deep breath, and my head gradually began to cool.

“But why did those Black Hunters specifically target Uncle Kkeokjeong? Why go this far just to keep a Guild so far beneath them in check?”

“Taekyung.”

Team Leader Choi cut me off and licked his parched lips.

His eyes were strange. He was looking at me as though I were a greenhorn.

It felt as if I had returned to the day I had first become a Hunter.

“You’re naive.”

Before I could answer, he continued.

“This is a place crawling with monsters. A place where one bothersome person—or even one entire Guild—can simply be erased. Discard that half-baked common sense.”

That cold sentence pierced my chest.

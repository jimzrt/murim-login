# Checkpoint Review — 110–114

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

# Chapters 110–114

## Plot

Cheol Mubaek, the Peak-level Tiger of Mount Heng, stops the Mount Heng Sword Sect’s elders from abandoning Lee Cheonbaek’s final wishes and forces them to recognize Lee Seowol as their Sect Leader. Seowol refuses to flee despite the sect’s overwhelming disadvantage, preparing a desperate defense with oil hidden throughout the estate while awaiting Jin Taekyung and Jin Mukyung.

Pung Yang leads more than two hundred Red Wind Band mounted bandits in surrounding Mount Heng. He offers Seowol a choice between total destruction and marriage, intending to preserve the sect’s useful forces under his control. Cheol kills the envoy, prompting the assault. The sect’s defenses initially repel the attackers, and Seowol’s concealed fire attack burns many mounted bandits, but the gate and walls eventually fall. Cheol holds the breached gate alone until Pung Yang confronts him.

Pung Yang swallows an unidentified red pill from a hard wooden case and gains enough power to defeat the mature Peak master Cheol, breaking all four of his limbs and severely injuring him. The surviving defenders retreat to a watchtower, where Seowol continues fighting until exhausted and signals Cheol with a fire arrow. Pung Yang reaches her and renews his demand that she marry him.

Taekyung, Mukyung, Mujin, and Wolhwa arrive at the fortress after a forced ride under Taekyung’s time-limited Peak Quest. Cheol recognizes Taekyung’s Taiyuan Jin Family affiliation, leaving the Jin party as the Mount Heng Sword Sect’s only immediate hope.

## Continuity

- Taekyung, Mukyung, Mujin, and Wolhwa have reached the Mount Heng Sword Sect after racing against the Quest’s irreversible twenty-two-hour deadline.
- Taekyung is Level 55; Mujin is Level 38.
- The Red Wind Band began the assault with more than two hundred mounted bandits, suffered at least one hundred casualties in the fire attack and initial fighting, and still retains more than one hundred fifty when Pung Yang enters personally.
- Pung Yang is an early Peak master whose saber and throwing-knife techniques are highly developed; the red pill temporarily raises his power far beyond Cheol Mubaek’s.
- Pung Yang possesses an unidentified hard wooden case containing the red pill and possibly a weapon or other anti-tiger object.
- Cheol Mubaek is alive but has four broken limbs and severe internal injuries. He refuses to surrender the single-successor Shura Annihilating Fist, though he fears for Lee Seowol’s safety.
- The Mount Heng fortress wall has been overrun. Lee Seowol and the remaining defenders are surrounded at the watchtower, while Pung Yang demands her marriage.
- Lee Seowol remains Sect Leader by choice and has not accepted Pung Yang’s demand.
- The Mount Heng Sword Sect’s survival, Seowol’s response, and Taekyung’s ability to rescue her and Cheol remain unresolved.
- The nature and origin of Pung Yang’s red pill remain unknown.
- The Peak Quest’s required invitation to the Jin Family for the coming Lunar New Year remains the governing objective.

## Translation Decisions

- Retain **Peak**, **early Peak**, **First Rate**, **shichen**, **Red Wind Band**, **mounted bandits**, **Sect Leader**, **Young Lady**, and **Taiyuan Jin Family**.
- Render **수라멸권** as **Shura Annihilating Fist**.
- Render **항산권문** as **Mount Heng Fist Sect**; retain **Mount Heng Sword Sect** where that established sect name is used.
- Render **화시** as **fire arrow**, **쇠뇌** as **crossbow**, **충차** as **battering ram**, and **벽곡단** as **fasting pills**.
- Render **멸문지화** as **total destruction**, **혼인 예물** as **wedding gift**, and **동귀어진** as **perishing together**.

## Durable state

{
  "active_continuity": [
    "Pung Yang personally led the Red Wind Band's assault on the Mount Heng Sword Sect after the envoy's death.",
    "Pung Yang swallowed an unidentified red pill from a hard wooden case and gained overwhelming power.",
    "Pung Yang defeated Cheol Mubaek, breaking all four of his limbs and inflicting severe internal injuries.",
    "Cheol Mubaek would rather die than surrender the single-successor Shura Annihilating Fist's formula to Pung Yang, but worries about Lee Seowol.",
    "The Mount Heng Sword Sect's fortress wall has been overrun; more than one hundred mounted bandits surround Lee Seowol and the surviving defenders at the watchtower.",
    "Lee Seowol continued fighting despite exhaustion and signaled Cheol Mubaek with a fire arrow.",
    "Pung Yang appeared before Lee Seowol and demanded that she marry him.",
    "Jin Taekyung and his companions arrived at the fortress, and Cheol recognized Taekyung's Taiyuan Jin Family affiliation."
  ],
  "continuity_sources": [
    114
  ],
  "open_questions": [
    "What is the nature or origin of the red pill that empowered Pung Yang?",
    "How will Lee Seowol respond to Pung Yang's marriage demand?",
    "Can Jin Taekyung and his companions reach or rescue Lee Seowol and Cheol Mubaek?",
    "Whether the Mount Heng Sword Sect will survive the continuing assault remains unresolved."
  ],
  "safe_through": 114,
  "temporary_decisions": [
    "Render 일류 초입 as early First Rate.",
    "Retain shichen and explain three shichen as six hours in context.",
    "Render 화시 as fire arrow, 쇠뇌 as crossbow, and 충차 as battering ram.",
    "Render 수라멸권 as Shura Annihilating Fist.",
    "Render 항산권문 as Mount Heng Fist Sect.",
    "Render 벽곡단 as fasting pills."
  ],
  "version": 1
}

## Reading copies

## Chapter artifact 110

# Chapter 110

*Bang!*

The person who appeared with the thunderous explosion was a middle-aged man of imposing stature.

Beneath his thick, sharply angled brows, he glared around the room with tiger eyes like an enraged beast.

“Who was the one spouting that nonsense just now?”

Everyone gathered here was a senior figure of the Mount Heng Sword Sect.

Even if they weren’t on their predecessor’s level, they possessed First Rate martial arts and more than enough experience. Yet even they were busy shrinking their necks and avoiding his gaze.

The middle-aged man before them had every right to make them do so.

*Damn it. Of all people, it had to be the Tiger of Mount Heng…*

The storytellers said that two beasts lived on Mount Heng.

The Blood Wolf Sword and the Tiger of Mount Heng. They were close friends, but each was also the wall the other had to overcome.

The middle-aged man, Cheol Mubaek, had been a Peak master known as the tiger of Mount Heng for decades.

“I asked which one of you it was!”

At that roar, the senior figures of the Mount Heng Sword Sect felt every hair on their bodies stand on end.

They said that whenever Cheol Mubaek lost his temper, even his friend Lee Cheonbaek would leave the area. These men were far inferior to him in both martial arts and age, so there was no need to say more.

“We should be united in driving out those mounted bandit bastards, and yet you dare defy Cheonbaek’s final wishes and harbor rebellious intentions?”

Under his gaze, which seemed ready to pour out flames, the senior figures of the Mount Heng Sword Sect flinched as though they had been burned.

“G-Great Hero Cheol. You misunderstand.”

“How could we ever dare harbor rebellious intentions?”

“Then have I grown old enough for my ears to fail me?”

At that moment, everyone inside the main hall felt thirsty. It wasn’t a simple illusion. It was caused by the terrifying Scorching Yang Qi radiating from Cheol Mubaek.

*What the hell?*

*What on earth has he been eating to build up such ridiculous internal energy…?*

Just being near him made it hard to breathe, and sweat poured down their bodies. The Tiger of Mount Heng. This was the moment the true nature of the Peak master who had supposedly trained alone somewhere in the vast mountain range since around the age of twenty revealed itself.

“Haah… Hoo…”

“Great Hero, please calm down… Hah.”

The senior figures of the Mount Heng Sword Sect panted harshly, while the Peak master glared at them without the slightest sign of forgiveness.

The air inside the main hall was about to boil like lava when—

“Uncle Cheol, it’s hot.”

A clear voice like a flowing stream, and slender white fingers tugging at Cheol Mubaek’s sleeve. At the same time, the wrinkles furrowed across his brow in anger smoothed out as though someone had pulled them flat.

“W-Was it very hot?”

“Yes. I can barely breathe.”

“Goodness, I didn’t think of you. How are you now?”

“Much better. Thank you, Uncle Cheol.”

“Don’t say such things. Protecting you, Seowol, is my duty.”

Cheol Mubaek’s powerful Scorching Yang Qi subsided.

Only then did the people throughout the hall finally release the breaths they had been holding. Once they came to their senses, their clothes drenched in sweat, they realized that Cheol Mubaek was not alone.

“Y-Young Lady.”

“We greet Young Lady.”

Cheol Mubaek raised his brows at the senior figures hurriedly standing to show their respect. But the “Young Lady” was faster.

“I’ll tell the two of you one last time, Iron Sword Squad Leader and Master of the Gatekeeper Pavilion.”

The woman who had been hidden behind Cheol Mubaek’s massive frame stepped forward. She was slim and graceful, and the hem of her blue gown rustled whenever it brushed the floor.

“Change how you address me. Not Young Lady. Sect Leader.”

Those who met her frost-cold gaze remembered one fact they had momentarily forgotten.

*Oh. That’s right.*

The Blood Wolf Sword, Lee Cheonbaek.

Lee Seowol was the child in whom his blood ran strongest.

* * *

I knew nothing about horseback riding. After coming to Murim, I had ridden only a few times. In the modern world, horseback riding was practically an aristocratic sport reserved for the rich, so I’d never had the chance to try it.

But perhaps because my physical abilities were so good and I was riding a well-trained horse, I had enough leisure to look at the System Window even during a furious gallop.

*Open Quest Window.*

*Ding.*

> **System**
>
> **Quest**
>
> **Yesterday’s Enemy, Today’s Ally**
>
> Now that all the truth has been revealed, the Mount Heng Sword Sect is not an enemy but an ally you must join hands with. Invite them to the Jin Family of Taiyuan during the upcoming Lunar New Year.
>
> **Grade:** Peak
>
> **Restriction:** Jin Taekyung
>
> **Objective:** Deliver the invitation (Incomplete)
>
> **Reward:** ???
>
> **Failure:** None

Quests were fluid. Sometimes sudden Quests appeared depending on the situation, and sometimes, like now, an existing Quest was updated.

*The Grade was raised.*

The Quest Grade changing from First Rate to Peak meant that the road to the Mount Heng Sword Sect had become anything but easy.

For example, the Red Wind Band. Or the Red Wind Band. Probably the Red Wind Band…

Never mind. Thinking about it any more would only hurt.

*Every day in this place is a walk across thin ice.*

I thought I’d finally received an easy Quest for once, but trouble had struck again.

The reason I wasn’t as anxious as before was partly because of the reliable presence of Jin Mukyung, but also because I myself had grown stronger.

*Open Status Window.*

*Ding.*

> **System**
>
> **Status Window**
>
> **Level:** 55 — Jin Taekyung
>
> **Class:** First Rate martial artist
>
> **Fame:** 1,300 (+150)
>
> **Titles:** 4 (Title effects active)
>
> — Returnee (All stats +10)
>
> — Sleeping Dragon of Shanxi (All stats +10, Fame +100)
>
> — Scion of a Prestigious Family (All stats +5, Fame +50)
>
> — Gambler (Combat-related stats +10% in one-on-one combat)
>
> **Strength:** 196 (+25)  
> **Stamina:** 195 (+25)
>
> **Agility:** 192 (+25)  
> **Intelligence:** 35 (+25)
>
> **Charm:** 35 (+25)  
> **Internal energy:** 15 years
>
> **Toughness:** 155 (+25)
>
> **Remaining Points:** 0

*Ahh, barkeep.*

*Look how well I’ve grown. All by myself.*

Strength, Agility, and Stamina were each nearing 200. Just looking at them made me feel full, and my Toughness, born from getting beaten by Jin Mukyung, was growing nicely too.

*The Title bonuses are hefty, too. This should be enough.*

Until now, I had raised my stats just to survive. Every time I advanced a Quest, one crisis after another came crashing down like three waves at once. There was no way I could afford to invest points in Charm or Intelligence.

*Even if I raised my Intelligence enough to reach an IQ of 180, it’s not like I’d start thrusting a spear scientifically.*

Charm was the same. It wasn’t as though Jopil or the Head Elder would spare me just because I was handsome.

Of course, raising them would help me in some way eventually. But with my life hanging by a thread, I hadn’t had the courage to invest in noncombat stats.

*I can protect this one life of mine to some extent now.*

Once this Quest was over, I planned to pay more attention to my internal energy and noncombat stats.

As it happened, the items I had obtained after defeating Jopil—including the Blazing Flame Divine Pill—were sitting untouched in my Inventory.

*Of course, if I screw up taking it, I could wind up dead.*

At that moment, Wolhwa, who had been riding at the front, spotted a stream and stopped.

“We’ll rest for a little while. The horses are too exhausted.”

How much time had passed?

We had ridden without stopping since leaving the shrine; dawn had broken, and now the sun was high overhead. System messages saying my Strength and Stamina had increased had even appeared twice, so it had definitely been a forced march.

“Whew. My butt hurts like hell. If I’d known this would happen, I should’ve been born the son of a coachman instead of a farmer.”

While the horses rested, Hyuk Mujin dropped heavily to the ground. Since he was the lowest-level member of the group, his exhaustion was obvious.

“Is it hard?”

Hyuk Mujin wiped the sweat from his forehead with his sleeve before answering.

“To be honest, it is… But strangely, it’s much better than last time.”

“Last time?”

“You’ve already forgotten? During the scouting mission.”

“Ah, I remember.”

I had nearly died after encountering Jopil while carrying out a scouting mission for White Tiger Hall. We’d taken horses with us then, too.

*Though we ended up abandoning them when the heavy snow came.*

Remembering the past, I let out a quiet laugh.

“What’s wrong?”

“I was thinking about you. You mouthed off to me without knowing what you were doing and got the crap beaten out of you.”

“……Do you really have to dredge up the past to feel better?”

“You’re the one who asked, punk.”

“Anyway, I’m saying it seems much better than back then.”

“Really?”

“Yes. We’ve ridden much farther than during the scouting mission, but I’m not even that tired. Maybe I’m getting used to riding?”

“Maybe… Ah, wait.”

“Hm?”

Something suddenly occurred to me, so I heightened my Qi Sense.

*Ding.*

Along with a familiar system notification, a Level Window appeared over Hyuk Mujin’s bewildered face.

> **System**
>
> **Level:** 38 — Hyuk Mujin

“……Huh?”

A breathy sound escaped his open mouth. When had Hyuk Mujin’s Level gotten this high?

*Strictly speaking, it wasn’t all that high.*

But considering that he had been only Level 20 when we first met, calling it astonishing progress wasn’t enough. At this point, it was practically like he had been reborn.

*Come to think of it, his Level did seem to keep rising after we first met.*

As I searched my memory, the details came back more clearly.

It had been the same when we reunited as a scouting unit. Whenever I heightened my Qi Sense from time to time, Hyuk Mujin’s Level had risen by one or two.

And now he was Level 38. In terms of time spent in Murim, he had nearly doubled his Level in only about two months.

*Then maybe…?*

With a doubtful heart, I stared intently at Hyuk Mujin.

What if he received stat points like I did? Could I distribute them for him?

*It’s possible.*

Judging by how much stronger I was than a Hunter or martial artist of a similar Level, there seemed to be some kind of System enhancement effect…

*It’s worth trying once.*

“Why are you looking at me like that? Do I have something on my face?”

“No. You’re just ugly.”

“……Seriously.”

I grabbed Hyuk Mujin’s shoulder and shouted inwardly.

*Open Status Window!*

At that very moment—

“What are you doing? My shoulder hurts.”

“Oh. Okay.”

Nothing happened. I thought at least something would appear.

Then again, my main character was still far from reaching the Level cap. Why would my alt character get anything? Still, it was disappointing.

*Should I say it out loud?*

They would definitely treat me like some kind of weirdo, but it was better than moving on with the feeling of not washing my hands after using the bathroom.

I stealthily placed my hand against Hyuk Mujin’s back—lightly, very lightly—and muttered under my breath.

“Open Status Window.”

“Seriously. What is wrong with you today?”

Ignoring him, I sprang to my feet.

The system window had appeared with the notification chime I’d been waiting for.

“Yes! There it is!”

*Ding.*

> **System**
>
> The Quest condition **Time Limit** has been added.
>
> Arrive at the Mount Heng Sword Sect within **22:00:00**. If you are late, there will be no going back.

“Yes…”

My voice faded. My eyes began to tremble.

*A time limit? What kind of time limit is this?*

*Why are you doing this to me?*

As I let out a deep sigh, Wolhwa’s eyes widened and she asked,

“Young Master Jin, are you hurt?”

“No, it’s not that. Do you know around when we’ll arrive?”

“Hmm. At today’s pace, before tomorrow evening?”

“Ah.”

It was a little past noon now. That meant we would have to ride for more than an entire day.

Judging by the Quest Window’s change, it seemed the Red Wind Band bastards would attack the Mount Heng Sword Sect within that time limit…

What was I supposed to do?

“Shall we get going soon?”

“The horses are tired. We need to rest for an hour.”

“Horses, you’re all right, aren’t you? You heard that, right? They said they’re fine.”

“……”

Yeah. I knew you’d look at me like that.
## Chapter artifact 111

# Chapter 111

*Thudthudthudthud!*

Four fine horses raced down the main road. Exhausted from their lack of rest, the horses were already gasping for breath, but there was no way we could loosen the reins.

> **System**
>
> **Time Limit:** 16:25:32

31, 30. The time kept ticking down.

Three *sijin*—six hours—had already passed. We had tried to stop at a small village along the way and find fresh horses, but all they had were small, painfully slow packhorses.

*We really do need to rest.*

We were trapped between a rock and a hard place.

We had been forcing our march as hard as we could, but the time limit was dangerously close. If we kept running like this, the horses wouldn’t hold out.

*Can’t be helped.*

I was just about to suggest to Wolhwa and Jin Mukyung that we rest, even if only briefly, when—

“Hm?”

“Young Master Jin! Ahead!”

Even without Wolhwa’s shout, I had already seen them. Several dozen *jang* ahead, a group of dark figures blocked the main road.

Every one of them wore filthy clothes, with a single curved saber sticking out from his belt. There was no need to say anything more.

*The Red Wind Band.*

The men had surrounded what appeared to be ordinary civilians and were threatening them. At the sound of hoofbeats, they whipped their heads around.

The mounted bandits spotted me riding well out in front and grinned, baring their yellow teeth.

“Well, look at that. Our next customers have already arrived. Stop!”

“Oh, sure.”

They told me to stop, so I had to stop. What else could I do?

*Thud! Thud!*

“Gaaah!”

“Argh!”

The fine horse I was riding didn’t come to a stop until it had trampled the two men blocking the road. The mounted bandits—and even the travelers they had been holding captive—stared at me with their eyes wide.

“You—you bastard!”

I hopped down from the saddle and asked,

“I’m asking just to make sure. You’re the Red Wind Band, right?”

“What the hell are you?”

“Judging by your reaction, I guess I was right. I’m short on time, so let’s finish this quickly.”

Without hesitation, I kicked the leg of the nearest man.

*Crack.*

With a chilling sound, his shinbone snapped, and he collapsed.

It all happened in an instant. The men who had been momentarily stunned quickly thrust curved sabers and spears at me.

“Kill him!”

“A man should always watch his rear.”

“What?”

“Be careful behind you.”

The instant I finished speaking, ten pairs of eyes turned to look behind them.

*Craack! Thud!*

Three fine horses charging at full speed swept the men away.

* * *

The battle was over before it had even begun. The men struck by the horses had been sent flying like bowling pins and lay sprawled out half-dead. The rest were easily subdued.

“P-Please, just spare my life.”

“I won’t kill you. But I’ll have to fix a few things first.”

“Eek!”

While Jin Mukyung methodically broke the limbs of the surviving bandits, Hyuk Mujin brought over the horses tied up beside the road.

“It looks like we can switch to these healthy ones. There must be at least ten of them, so we could take them all and switch whenever they get tired.”

I had been thinking the same thing. Unlike the last group we encountered, these mounted bandits each had their own horses. It was fortunate.

*But still…*

How many of these Red Wind Band bastards were there?

According to the information we obtained at the shrine, more than a hundred remnants had scattered throughout northern Shanxi.

Some were hiding in the foothills, while others were concealed in remote villages or crowded areas, gathering at a designated rendezvous point when ordered.

*These men aren’t stragglers.*

They were ambush forces carrying out an operation. The Red Wind Band Leader was replenishing his forces on the plateau and moving south, while sending the subordinates he had left behind north.

I could easily understand why Wolhwa had described the Red Wind Band Leader as such a terrifying man.

*The judgment to retreat swiftly when the battle turned against him. The meticulousness to prepare his next plan even in the middle of it all. And the drive to carry that plan out.*

On top of that, I had heard that his own martial arts were formidable.

At this point, I almost felt bad for treating him as nothing more than a mounted bandit.

*This has gotten seriously messy.*

Now I understood why the Quest Grade had risen to Peak. And when I thought about it, things seemed to be getting worse by the minute.

It couldn’t be that the Red Wind Band Leader was a Peak master too, could it?

I asked Wolhwa just in case.

She immediately nodded.

“Yes. He is.”

“…Ah.”

“There has to be a reason someone rose to prominence so quickly. He isn’t widely known yet, but according to our sect’s intelligence, the Red Wind Band Leader is indeed a Peak master.”

I was dumbfounded.

“Why would a Peak master become a mounted bandit?”

“There are even Supreme Peak masters among mountain bandits and water bandits. Why couldn’t a mounted bandit be one?”

“Supreme Peak masters? Among mountain bandits and water bandits?”

“When you meet the Green Forest Alliance Leader or the Alliance Leader of the Yangtze River Channel League, ask them yourself. Not that you ever will.”

“…I sincerely hope that’s true.”

A Supreme Peak master? I genuinely hoped I would never meet one.

I shook my head repeatedly and mounted one of the newly taken horses. Jin Mukyung and Hyuk Mujin followed after tying up the Red Wind Band’s mounted bandits and handing them over to the commoners.

> **System**
>
> **Time Limit:** 15:59:13

The time limit continued to tick down even now. Leaving the commoners behind as they bowed deeply in thanks, we kicked the horses in the ribs.

“Giddyap!”

* * *

Deep within the inner grounds of the Mount Heng Sword Sect stood a garden that only a very small number of people were allowed to enter. Cheol Mubaek, the Tiger of Mount Heng, was the only outsider granted that privilege.

“This is my first time here.”

“Because it was a special place. Whenever Father had something weighing on his mind, he would come to the garden.”

Lee Seowol walked through the snow-covered garden, her footsteps crunching softly. Then she suddenly stopped when she spotted a frost-covered flower.

“This was one of Mother’s favorite flowers.”

“Was it?”

“Yes. Whenever she tended the garden, she would always bring me here and tell me the names of the flowers.”

After thinking quietly for a moment, Lee Seowol continued.

“But I can’t remember it now.”

“It was a long time ago. Don’t trouble yourself over it.”

“Uncle Cheol.”

“Yes?”

“I don’t like flowers. I only followed Mother because she liked them. In truth, I never cared about flowers. It’s the same reason Father used to come to the garden.”

Lee Seowol slowly looked around the snow-covered garden. The flowers had withered, and the number of burial mounds in the center of the garden had grown from one to four.

Her gaze sank as she silently stared at the mounds where her family slept.

*Whose fault was it?*

Perhaps it was her own fault for being born the daughter of a Murim martial artist.

That was why she had lost her father and two older brothers one after another, after losing her mother ten years ago.

*I should have kept trying to stop him until the very end…*

A memory from two months ago suddenly resurfaced and blurred her vision.

It had been a conversation between father and daughter, held late one night with no one else present.

*“I’ll have to tie you to the third son of the Jin Family of Taiyuan.”*

*“The third son? Surely you’re not thinking of marrying me to that good-for-nothing?”*

*“No. But it will become an unbearable scandal for you.”*

*“I see.”*

*“Is that all you have to say?”*

*“What can I do? It’s my fault for having a heartless father.”*

*“You’re a child I can never understand. Are you really all right with this?”*

*“If I say I don’t like it, will you change your mind?”*

*“At the very least, I’ll look for another way.”*

*“So the war with the Jin Family of Taiyuan is a foregone conclusion.”*

*“Now that the Strange Hero of Shanxi and the Heaven Shaking Sword are absent, this is the perfect time. This opportunity will never come again.”*

*“The Jin Family of Taiyuan is strong even without the Family Head and the Second Young Master. Please reconsider.”*

*“No. My decision has already been made.”*

*“Then make sure you win. Become strong enough that no one in Shanxi can even open their mouth about a scandal involving me.”*

*“…If you had been a man, I would have made you the Young Sect Leader.”*

*“I’m glad I was born a woman. I have no interest in being this sect’s Young Sect Leader.”*

Her fears soon became reality.

Had even a fortnight passed before Lee Seogeun returned as a cold corpse? Not long after, she lost Lee Cheonbaek, and in the end, even her eldest older brother, Lee Seogwang.

*Now I’m alone.*

And so, the Blood Wolf Sword Lee Cheonbaek’s last surviving blood relative became the new Sect Leader.

A warm palm gently caressed Lee Seowol’s shoulder.

“I’m sorry. I should have come sooner…”

“Uncle Cheol, please don’t say that. If you hadn’t come, our sect wouldn’t have been able to hold out this long.”

Under the Red Wind Band’s fierce assault, the Mount Heng Sword Sect had been helplessly driven back. If not for the Peak master known as the Tiger of Mount Heng, who had rushed over after belatedly learning of Lee Cheonbaek’s calamity, the enemy would never have withdrawn.

“I’ll tear that bastard limb from limb and kill him.”

At the thought of the Red Wind Band Leader, Lee Seowol shook her head.

In a life-and-death duel between Peak masters, Cheol Mubaek had the edge.

They had already clashed once, and Pung Yang had retreated with a minor internal injury.

*But an opportunity like that will never come again.*

The Mount Heng Sword Sect had always gathered information on the mounted bandits of the northern plateau and remained constantly on alert.

There were dozens of mounted-bandit groups on the plateau, but among them, the Red Wind Band led by Pung Yang had grown frighteningly fast.

A man particularly strong and meticulous even among the plateau’s chieftains.

That man was Pung Yang.

*There’s no way someone like that would engage Uncle Cheol in a life-and-death duel. If Uncle Cheol rashly tried to confront him, Pung Yang would turn the tables on him instead.*

Lee Seowol turned toward Cheol Mubaek.

“Uncle Cheol, could you tell me once more about Pung Yang’s martial arts?”

“Early Peak. His saber arts and throwing-knife techniques had reached a high realm. However…”

A deep furrow formed between Cheol Mubaek’s brows.

“Every one of his forms was thoroughly insidious. I suspect he has learned demonic, heterodox martial arts.”

“Demonic, heterodox arts…”

After the Great Faction War, belonging to the evil and heretical paths was tantamount to death in the Central Plains. Unorthodox factions might present themselves as orthodox, but no one openly proclaimed themselves unorthodox.

“For now, it’s only a suspicion. We’ll know if we clash again.”

“I trust you, Uncle Cheol. But don’t underestimate the Red Wind Band Leader. He has any number of subordinates he can sacrifice in his place.”

With enemies bearing down from both directions, their combined force was close to three hundred strong.

Meanwhile, even after gathering every martial artist stationed at its branches, the Mount Heng Sword Sect had less than half that number.

Given the situation, morale was low among both the ordinary martial artists and the newly appointed senior members.

“Seowol. May I say something?”

These were the words of a benefactor who had risked his life out of loyalty to his dead friend. Lee Seowol bowed politely.

“I’ll take your words to heart.”

Cheol Mubaek spoke heavily.

“Leave.”

It was a single word laden with meaning.

But there was not the slightest hesitation in Lee Seowol’s answer.

“I’m sorry.”

“It isn’t too late. You must survive.”

“It isn’t over yet. And I will survive.”

“If you thought Cheonbaek would have wanted this…”

“Uncle.”

At her resolute voice, Cheol Mubaek closed his mouth. Firm determination filled Lee Seowol’s clear eyes.

“This is what I wanted. As the Sect Leader of the Mount Heng Sword Sect.”

“Whew…”

Cheol Mubaek let out a sigh instead of answering.

“I’m already deeply indebted to you, Uncle. Even if you leave now, I won’t resent you.”

“Do you really need to hear my answer before you’ll be satisfied?”

Lee Seowol shook her head. Cheol Mubaek had cherished her like his own child since she was young. In some ways, he had been more of a father to her than her actual father.

“I will never forget this debt. Uncle Cheol, you are the benefactor of both me and the Mount Heng Sword Sect.”

“I’ve watched you since you were little, but… you really are a sly child.”

“I was sly when I was young. Now I’m a ruthless bitch.”

Watching Lee Seowol smile faintly, Cheol Mubaek could only continue to sigh deeply.

“Do we have any chance of winning?”

“If we fought now? Ten percent.”

“What?”

“But if reinforcements arrive, fifty percent. More than that.”

“Reinforcements? From the Jin Family of Taiyuan?”

“A messenger pigeon sent by the Lower District Sect’s Jeongyang Branch arrived four hours ago.”

“How many are there? One hundred? Two hundred?”

“Four. One of them is the Heaven Shaking Sword, Jin Mukyung, and another is…”

Lee Seowol let out a wry laugh, reminded of her ill-fated connection with him.

“The Sleeping Dragon of Shanxi, Jin Taekyung.”
## Chapter artifact 112

# Chapter 112

Mounted bandits openly riding down the main road in broad daylight?

Under normal circumstances, it would be unthinkable. The nearest Murim sect would be the first to act, followed by the soldiers from the local authorities.

But if there were hundreds of mounted bandits—enough to overwhelm even the Murim sect that was supposed to suppress them—the officials could only close their eyes and cover their ears.

Just like now.

“Ar-aren’t those mounted bandits?”

“Don’t call them ‘those guys.’ Do you have three lives or something? They’re the infamous Red Wind Band.”

“The Red Wind Band? Weren’t they defeated by the Mount Heng Sword Sect not long ago?”

“That’s what we thought. But this time seems different. Rumors are already spreading through the marketplace that the Mount Heng Sword Sect won’t escape total destruction.”

“Still, the sect has some ability. Surely they won’t lose to mere mounted bandits…”

“Hey, watch your mouth! The man riding at the front is Pung Yang, the leader of the Red Wind Band. They say he’s a Peak master.”

“What? A Peak master?”

“Yeah. You can’t dismiss them just because they’re mounted bandits. I hear he isn’t merely strong in martial arts—he’s exceptionally clever, too.”

The commoners’ fearful whispers wormed their way into Pung Yang’s ears and those of his mounted bandits.

A subordinate riding on Pung Yang’s right spoke softly.

“Shall I rip those bastards’ mouths apart?”

“Do you want to?”

“If the Leader permits it, I’ll deal with those two first, then turn the entire village into a sea of flames.”

“You’ll kill the old men, capture the young men, and rape the women?”

“Heh heh. Isn’t that what men like us always do? The Mount Heng Sword Sect bastards are probably cowering behind their walls by now, scared out of their wits.”

“They probably are. They’ll be preparing for a final battle by gathering every bit of strength they have.”

“It won’t matter. That’ll just be eggs thrown at a rock. It’s a foregone conclusion that the Leader will wipe out the Mount Heng Sword Sect and take its place.”

“That is why I won’t permit it.”

“What?”

Pung Yang burst into a hearty laugh at his subordinate’s bewildered reaction.

They were all shallow-minded and cruel by nature. That was why they had become mounted bandits—and why Pung Yang kept them close.

*Because they’re easy to handle.*

When his laughter subsided, he spoke.

“Destroying the Datong Branch was part of the war. But if we harm commoners now, all we’ll accomplish is giving the Jin Family of Taiyuan an excuse to intervene.”

“Are they the rulers of Shanxi or something?”

“Not yet. But they will be soon enough. Before that happens, shouldn’t we swallow the Mount Heng Sword Sect and lie flat like dogs?”

“Um, Leader, I’m not doubting your judgment, but… would orthodox factions like the Jin Family of Taiyuan really look favorably on mounted bandits like us?”

“Mounted bandits? Who’s a mounted bandit?”

“What?”

“Last time, I noticed that the Sect Leader of the Mount Heng Sword Sect was quite beautiful.”

Pung Yang’s subordinate blinked several times before finally understanding. The corners of his mouth curled upward.

“She’s of marriageable age, so she’ll need to take a husband.”

“She has two choices: total destruction or marriage.”

“Then what will happen to the Red Wind Band…?”

“We’ll take the heart of it and wear the outer shell. Let’s see… Compared to the others, your face is at least presentable. I’ll make you Master of the Gatekeeper Pavilion.”

“Ha ha ha! I’ll devote my life to serving you!”

As he listened to his subordinate’s laughter, Pung Yang tightened his grip on the reins.

*At last, I’ve made it this far.*

He was a cold and levelheaded man, but his heart pounded at the thought that he had taken another step toward his ambition.

Memories from long ago flickered before his eyes.

*It’s been well over twenty years already.*

Becoming a mounted bandit had been easier and simpler than he had expected. There were only two ways: go looking for them or get caught by them. In Pung Yang’s case, it had been the latter.

When he was young, he had committed a crime and was being taken to the local authorities when a mounted-bandit group attacked. That had been the turning point of his life.

*“Boss, there’s a little one here, too.”*

*“Hm? He’s so skinny that we wouldn’t get more than a few coins for him even if we sold him. Kid, did you get caught pickpocketing?”*

*“No. I killed someone.”*

*“You killed someone? How old are you?”*

*“Thirteen.”*

*“Why did you kill him?”*

*“I hadn’t eaten for three days, and the boss had dumplings…”*

*“Dumplings? Did he take away what you begged for? That would be enough to make anyone snap.”*

*“No. I was hungry, and I didn’t have the strength to beg. He was eating dumplings right in front of me.”*

*“…So you killed him?”*

*“I thought it would be faster to take them and eat them.”*

*“Hey, let this kid go and feed him something. He’s one of us from today.”*

Pung Yang became a mounted bandit that day.

An orphan abandoned by the world, he had wandered from place to place begging for food. He was exceptionally perceptive and quick-witted.

Compared to his past, when he had barely eaten a meal every three days, life as a mounted bandit was lavish.

Robbery? Murder?

To Pung Yang, who had committed murder at the age of thirteen simply because he wanted to eat dumplings, such things were nothing more than what had to be done.

*“Good grief. I’ve been a mounted bandit for more than ten years, but I’ve never seen anyone like you. It’s as if you don’t have a conscience.”*

*“Why? I’m a mounted bandit.”*

*“Kid, that’s not how it works. You gradually get used to it. No one is skilled from the very beginning.”*

*“Were you like that too, Boss? It was easy for me.”*

*“Easy, easy… I’m starting to wonder if I’m raising a tiger cub. How about learning a thing or two about martial arts from me?”*

*“Martial arts?”*

*“Yes, martial arts. You’re still young, so if your bones and martial talent are up to the task, you could become a master.”*

*“Then I’ll call you Master from today onward.”*

*“Master and disciple, my ass. Forget it. Just keep doing what you’re doing now.”*

Not forming a master-disciple relationship had been a wise decision.

A year later, his boss was beheaded and killed by a First Rate master, and Pung Yang found a new nest in another mounted-bandit group.

*“You were under Gwangchil?”*

*“Yes. If you feed me well, I’ll swear my loyalty to you.”*

*“You seem reasonably sharp. I won’t go easy on you because you’re young, so keep up on your own.”*

The plateau was brutal.

There were times when an entire mounted-bandit group was wiped out after attacking the wrong merchant caravan. The struggles for power between mounted-bandit groups never stopped, either.

But Pung Yang survived every time, growing stronger with each passing year.

By the time he turned thirty, his martial arts had entered the First Rate realm, and he managed to seize the position of squad leader in a mounted-bandit group of considerable size.

*But that was as far as I got.*

The law of strength applied everywhere.

The plateau was ultimately just another part of the Murim, where the strong ruled.

Pung Yang possessed grand ambitions and an exceptional mind, but he lacked the martial power befitting a leader.

*The limit of Third Rate martial arts.*

Pung Yang’s martial talent was extraordinary.

If he had entered a prestigious orthodox sect as a child and learned an excellent internal cultivation technique and martial arts, he might have crossed the wall to Peak long ago.

But he had grown up in a beggar’s den and learned Third Rate martial arts from the mounted bandits of the plateau. His limitations were clear.

*If heaven’s fortune hadn’t favored me, I’d probably still be standing in the same place.*

A deep smile settled over Pung Yang’s lips.

Three years ago, on that day, his life had changed completely. He had gone from being a mere squad leader in a mounted-bandit group to the leader of the Red Wind Band, one of the powers moving the plateau—and now it was time to swallow a Murim sect.

“Leader!”

Pung Yang snapped out of his thoughts at his subordinate’s shout.

Far in the distance, stone walls piled high like a fortress had finally come into view.

*The Mount Heng Sword Sect.*

As Pung Yang gazed at his and the Red Wind Band’s new home, one person entered his sight. Even from this distance, he could feel the man’s fiery aura.

*The Tiger of Mount Heng, Cheol Mubaek.*

A wall he would have to overcome in order to take the Mount Heng Sword Sect.

Although he had withdrawn after suffering a slight loss last time…

*Today will be different.*

Pung Yang unconsciously felt inside his robes. After confirming the hard wooden case there, his smile deepened.

“Leader, your orders?”

“Surround them. Don’t let even a single ant escape. Then send an envoy.”

Total destruction or marriage.

The Mount Heng Sword Sect had only two choices.

“I’ll have the Mount Heng Sword Sect in my hands before sunset.”

* * *

“They’ve surrounded our sect without leaving a gap!”

“Their numbers are well over two hundred!”

“Sect Leader, please make a decision!”

Seated in the place of honor, Lee Seowol calmly opened her mouth.

“Are the troops deployed?”

“Of the hundred or so men, half are blocking the sect entrance. The rest have been armed with shields and bows.”

Everyone in the main hall knew that “a hundred or so” was a generous estimate. In truth, they had far fewer than that.

Several of the Mount Heng Sword Sect’s senior figures had fled the previous night, taking their families and the subordinates who followed them.

“Uncle Cheol, what happened with what I asked you to do?”

“It has been arranged as you instructed.”

Lee Seowol’s plan involved oil.

They had spread enough oil to fill ten wagons evenly throughout the estate.

They had covered it with piles of well-dried hay, so it was obvious that the entire area would turn into a sea of flames the moment fire touched it.

*Does she intend for us to perish together with them?*

Cheol Mubaek was worried, but he kept his thoughts to himself. In all the years he had watched Lee Seowol, she had always been calm and clever, even from a very young age.

“We only need to hold out for one day. Exactly one day. Reinforcements from the Jin Family of Taiyuan are on their way, so we have a good chance of winning if we can stall them until then.”

“R-reinforcements from the Jin Family of Taiyuan?”

“I hear the Sleeping Dragon of Shanxi and the Heaven Shaking Sword are coming in person.”

The faces of everyone gathered in the main hall brightened.

The Heaven Shaking Sword, Jin Mukyung, was already renowned throughout the Central Plains as a martial arts genius, while the Sleeping Dragon of Shanxi, Jin Taekyung, was a rising star.

It was uncomfortable that he had earned his fame through a war against the Mount Heng Sword Sect, but knowing that he was now on their side made it feel as though they had gained a thousand troops.

Above all else…

“No matter how bold Pung Yang is, he won’t dare raise his sword against a direct descendant of the Jin Family of Taiyuan.”

“…That’s true.”

Lee Seowol felt bitter inside.

Not long ago, the Mount Heng Sword Sect had stood shoulder to shoulder with the Jin Family of Taiyuan.

Now, a Murim sect that had once commanded northern Shanxi had to focus all its strength on merely holding out against a mounted-bandit group.

*I will never forget what happened today.*

Just then, she bit down hard on her lip.

The doors to the main hall opened, and a martial artist from the Gatekeeper Pavilion came running in, shouting.

“Sect Leader, the enemy has sent an envoy!”

“An envoy?”

“Yes. He says there’s something he wishes to tell you in person…”

Lee Seowol nodded without hesitation.

If they could delay the battle by even a single moment, they had to do everything they could.

“Bring him in.”

Not long after the Gatekeeper Pavilion martial artist withdrew, the Red Wind Band’s envoy was escorted into the main hall.

He exposed his rotten teeth in a crooked grin and bowed deeply in an exaggerated manner.

“I pay my respects to the Sect Leader of the great Mount Heng Sword Sect.”

His attitude was clearly mocking, but the senior figures—and even Cheol Mubaek, whose temper was as fierce as fire—suppressed their anger. Lee Seowol had repeatedly warned them to do so beforehand.

“Why did you send an envoy?”

“Well, shouldn’t you give someone who has come such a long way a bowl of rice wine before asking—gasp.”

The Red Wind Band’s envoy was unable to finish his sentence and began trembling violently.

Cheol Mubaek, unable to contain his anger, had taken one step forward and released an overwhelming aura.

“Do you want rice wine that badly?”

At the deep, heavy voice, the envoy frantically shook his head.

“N-no, sir. I was thirsty, so I said something stu—stupid.”

“Uncle Cheol. That’s enough.”

“…Hmph. Stop talking nonsense and deliver your message.”

Barely freed from Cheol Mubaek’s aura, the envoy stammered.

“T-the Leader says we should stop this pointless war and now cement our friendship.”

“Friendship?”

The senior figures of the Mount Heng Sword Sect doubted their own ears.

Who had betrayed the previous Sect Leader, Lee Cheonbaek, and killed even the Young Sect Leader, Lee Seogwang? And hadn’t they massacred the families and dependents of the Datong Branch only a short while ago?

But Lee Seowol’s reaction was different. Without the slightest hint of surprise, she stared straight at the envoy.

“And if we refuse?”

“He said you won’t escape total destruction.”

“So he means that if we want to save our people, we must offer the Mount Heng Sword Sect in its entirety as a wedding gift.”

“I-I don’t know about anything beyond that…”

At this point, everyone in the main hall understood the meaning of the “friendship” Pung Yang had offered.

All of them were furious, but Cheol Mubaek was the quickest to act.

*Thud!*

In the literal blink of an eye, Cheol Mubaek crossed more than ten *jang* and drove one punch into the envoy’s chest.

The red fist aura carrying horrifying heat shattered his chest bones and burned his blood and flesh.

“Ghuuuh…”

With one final death rattle, the light vanished from the envoy’s eyes.

Cheol Mubaek pulled his fist from the man’s chest and turned toward Lee Seowol.

“He deserved to die a hundred times over.”

“I think so, too. But…”

Lee Seowol slowly rose from her seat and continued.

“We can no longer avoid the fight.”

One hour later, everyone in the Mount Heng Sword Sect heard the sound of horn calls ringing out from all directions.
## Chapter artifact 113

# Chapter 113

Half a shichen after sending an envoy to the Mount Heng Sword Sect, Pung Yang gave the order without hesitation.

“Attack.”

A quick, decisive battle.

The longer it dragged on, the worse it would be for him. Word that the Red Wind Band had surrounded the Mount Heng Sword Sect would spread quickly, and if outside forces—especially the Jin Family of Taiyuan—intervened, things would become troublesome.

*I never expected to enter without bloodshed in the first place.*

She might be a woman, but she carried the blood of the Blood Wolf Sword, Lee Cheonbaek.

If words and gestures couldn’t tame her, he would have to subdue her with violence. It was the same method Pung Yang had always used.

Bwooooooong!

The powerful sound of horns rang out from every direction. At the advance signal used by the mounted-bandit groups of the plateau, the mounted bandits surrounding the Mount Heng Sword Sect simultaneously kicked their horses in the ribs.

“Chaaaarge!”

“Kill every last one of them!”

Thundering hooves shook the ground.

Hundreds of horses raced forward, trampling the snow-covered earth.

The horn calls continued without pause, strong and carrying far into the distance.

* * *

Ding!

> **System**
> 
> **Circulate Qi** was successfully completed.
> 
> A small amount of Fatigue and Stamina has been restored.

The moment I opened my eyes at the sound of the System notification, I looked around.

“Did you guys just hear something?”

Wolhwa and Hyuk Mujin, who had been feeding hay to the horses, looked at me in confusion.

“Young Master Jin, what sound?”

“Sounds are always happening. Listen. The horses chewing hay, the wind…”

“Not that crap, you idiot.”

“Then what?”

“A-a vuvuzela?”

“Vuvu… what?”

“The thing people use to cheer at sporting events… Never mind. It’s something.”

I gave up explaining and stared in the direction the sound had come from—or rather, the direction I thought it had come from.

By coincidence, it was the north, where the Mount Heng Sword Sect lay—the very direction we were heading.

*Did I hear it wrong?*

According to Wolhwa, we still had to ride for another three shichen—six hours—before we could reach the Mount Heng Sword Sect. Whatever had happened, it wasn’t something that should have been audible from this distance.

*Unless it was cannon fire.*

Jin Mukyung, who had just finished circulating his qi, added his opinion.

“I didn’t hear anything.”

“But I could have sworn I heard something.”

“You imagined it.”

“Something might have happened at the Mount Heng Sword Sect.”

“That’s possible. But I didn’t hear anything.”

“But I’m telling you, I think I heard something.”

“So I’m telling you that you imagined it.”

“On what grounds?”

“It’s simple. There’s no way I could fail to hear what you heard.”

“…”

That was incredibly irritating, but he was right, so I couldn’t argue.

Seeing me rendered speechless, Jin Mukyung clicked his tongue.

“If you don’t want to die to a stray blade, focus on mastering your mind and body. You never know what might happen on a battlefield.”

*Look who’s lecturing whom.*

When it came to combat experience, no one here could match me.

I only seemed no different from usual because I had grown so accustomed to it. When it came to preparing for and taking part in battle, I was already thoroughly battle-hardened.

“There are a lot of enemies, so conserve your internal energy as much as possible and minimize your movements. I’ll take the lead. Just follow me, and there won’t be a problem.”

*Was he worried about me because we shared the same blood?*

Come to think of it, Mukyung had made his dislike painfully obvious, yet he had still helped me a great deal.

He had helped with my training, agreed to accompany me to the Mount Heng Sword Sect, and, I’d heard, had even made a considerable effort to reform his lazy little brother when they were children.

Even if Jin Wikyung had asked him to, those weren’t things he could have done if he truly hated me.

*Maybe he’s actually a soft-hearted guy.*

Was this what people called a tsundere?

I looked at Jin Mukyung with a sentimental gaze, feeling as though I might actually be moved.

Our eyes met.

“What are you looking at? Lower your eyes.”

“…”

“If you take even a single wound from those mounted-bandit bastards, I’ll kill you myself.”

“…Yeah, sure.”

*That’s more like it. Tsundere, my ass.*

I had briefly lost my mind and imagined something ridiculous.

Accepting reality, I was about to transfer my saddle to one of the spare horses we had taken earlier when Hyuk Mujin approached and spoke with a deeply worried expression.

“Second Young Master, you aren’t going to kill me too, are you?”

“…Are you saying it’s okay if I die?”

“Ah, no! Why are you putting it that way?”

“I’ll kill you before I die, so shut up and prepare to leave.”

I kicked Hyuk Mujin in the rear while he grumbled under his breath, then mounted my horse.

The Mount Heng Sword Sect was still three shichen away.

From this point onward, we had to ride hard without taking a single break.

> **System**
> 
> **Time Limit:** 6:25:19

* * *

The Mount Heng Sword Sect was like a fortress. The stone walls piled high around it were sturdy enough to be called castle walls, and all kinds of defensive facilities had been installed to hold the fortress.

Built more than thirty years ago under the uncompromising will of the founding Sect Leader, Lee Cheonbaek, those defenses were finally serving their intended purpose.

“Fire!”

Whoosh—whoosh—whoosh!

Dozens of arrows launched at once rained down on the charging cavalry.

But the weapons most commonly found on the plateau were spears, swords, and bows. Accustomed to fighting on the plateau, the mounted bandits of the Red Wind Band raised the shields strapped to one arm before anyone even gave the order.

Thud! Thump!

Only a dozen or so men were knocked from their horses.

The shields, made of bone-dry wood faced with hide from an old horse’s rump, did an excellent job of stopping the arrows.

“Ha ha ha! These punks don’t know their elders when they see them, and they dare—!”

That was when it happened.

Fwoosh—crack!

Something came flying with ferocious force. It pierced through a horse’s neck and buried itself in the squad leader’s chest.

He had only just entered the early stages of First Rate. He stared at the arrow protruding from his chest as though he couldn’t believe it, then toppled over together with his prized horse.

Several of the riders behind him lost formation and fell one after another.

“Crossbows! Watch for the crossbows!”

“Return fire!”

Whoosh—whoosh—whoosh!

If the Mount Heng Sword Sect’s attack had been a passing shower, the Red Wind Band’s arrow barrage was a torrential downpour.

Even while mounted, they drew their bowstrings again and again. Their arrows were fast and accurate.

Thwack! Thwack! Thwack!

“Aaargh!”

“Hide behind your shields! Don’t stick your heads out!”

Taking advantage of the opening, the mounted bandits spurred their horses forward and set grappling hooks and makeshift ladders against the walls, which stood more than ten *jang* high. They began attempting to breach the fortress.

A melee erupted atop the walls.

Screams and blood poured forth.

“Ha ha! Kill them all!”

“Stop them from climbing up!”

Lee Seowol watched the entire scene from the highest watchtower. Her lips trembled, and the color had drained from her face.

*So this is the Murim.*

The screams of those dying.

The desperate struggles of those who wanted to live.

The world of the strong preying on the weak that she had finally encountered was more brutal and frightening than she had imagined.

But…

*I can’t retreat.*

Countless people had already died. Those who were going to leave had left, while those who remained were fighting with their lives on the line.

Lee Seowol was now the Sect Leader who had to lead them. She was bound to share her fate with the Mount Heng Sword Sect.

“Sect Leader! The walls are in danger! We need to send reinforcements!”

“They’re breaking down the gate with a battering ram!”

“Sect Leader! You need to take action!”

“Sect Leader!”

As urgent reports rained down from every direction, Lee Seowol opened her mouth.

“When I give the signal, fire one fire arrow toward the walls and two toward the gate. And, Uncle Cheol.”

Cheol Mubaek, who had been standing beside her, answered.

“Tell me what you need.”

“The gate will be breached soon. Can you buy us a little time?”

“By myself?”

“I’m sorry to ask you to do something so difficult.”

“One against a hundred. I’ve always wanted to try that.”

“The uncle I know is a master who can face ten thousand men. But please be careful.”

“All right. Do you think those bastards can get the better of me?”

Cheol Mubaek laughed heartily, then leaped down.

With the Tiger of Mount Heng—a consummate Peak master—there, no one would be able to get through the gate unless Pung Yang himself stepped forward.

*Just a little longer. A little more.*

Lee Seowol watched the fierce battlefield below, then suddenly let out a thunderous shout.

“Now!”

The two martial artists who had been waiting for her command each drew their bowstrings.

The next moment, the fire arrows soared into the darkening winter sky and shone brightly above everyone’s heads.

* * *

The fire arrows falling like meteors were clearly visible even to Pung Yang, who stood more than a hundred *jang* away.

He thought to himself.

*They had a hidden ace.*

It didn’t take long for his suspicion to become certainty.

A moment later, enormous flames erupted around the walls.

Fwoosh! Fwoooosh!

“Aaargh!”

Burning to death was one of the most painful ways to die.

The mounted bandits of the Red Wind Band, massed beneath the walls like a swarm of ants, writhed and screamed horribly.

The ropes attached to the grappling hooks snapped, and the wooden ladders were engulfed in flames.

“Attack!”

“Kill every last one of those mounted-bandit bastards!”

Those waiting below to climb and those still making their way up burned to death. Those who had already reached the top were stabbed and slashed by weapons converging from every direction.

“So they did make some preparations…”

As Pung Yang stared impassively at the battlefield, one of the mounted bandits came back with parts of his body blackened like charcoal.

“What happened?”

“L-Leader. The casualties are too high!”

The moment he reached Pung Yang, the mounted bandit threw himself flat on the ground and continued in a breathless voice.

“From the first assault until now, at least a hundred men must have died. More importantly, after that fire attack, our brothers’ morale is…”

“The gate?”

“Pardon?”

“What happened to the gate?”

“We broke through, but the Tiger of Mount Heng, Cheol Mubaek, is holding it alone…”

“Alone?”

“Yes. His martial arts are so formidable that no one dares step forward.”

“Then it’s settled.”

At the same time, Pung Yang held out his hand.

The mounted bandit instinctively reached to take it, only for his body to list and collapse.

A dagger was buried deep between his brows.

“How many troops do we have left?”

This sort of scene was familiar to the subordinate who served as Pung Yang’s right hand. After glancing at the corpse, he answered.

“By a rough count, somewhere between a little over a hundred and fifty and just under two hundred. It’s true that our losses are greater.”

“Then imagine theirs. The men on those walls are the Mount Heng Sword Sect’s final bulwark.”

“You mean those few men are all they have left?”

“Yes.”

“I’m not doubting you, Leader, but couldn’t there be another trap like that fire attack?”

“That’s what they’re counting on.”

Pung Yang let out a derisive laugh. He didn’t know whose strategy it had been, but they had played it quite cleverly.

*If I had been less experienced, I would have suspected another trap and pulled our forces back.*

*They’re struggling to buy time. Are they waiting for someone’s support?*

If so, there was even less reason to hesitate.

The few couldn’t stand against the many. Even if the Red Wind Band had suffered considerable losses, wiping out the Mount Heng Sword Sect would be easy.

And besides…

“I’m going myself.”

“You’re going yourself, Leader?”

“Yes. We have to catch the tiger, don’t we?”

Pung Yang burst into a hearty laugh and habitually felt inside his robes.

A hard wooden case rested there.

Inside was something that could bring down a tiger in one go.
## Chapter artifact 114

# Chapter 114

The Tiger of Mount Heng, Cheol Mubaek, stood like an iron tower.

The entrance gaped wide enough for two carriages to pass through side by side, yet not one of the fifty-odd mounted bandits of the Red Wind Band dared set foot inside.

They had seen clearly how the men who went ahead of them had died.

Some had died with their heads blown apart. Others had been pierced through the abdomen or killed when their limbs were broken. No one had properly seen when or how Cheol Mubaek’s fist moved.

More than twenty had died that way.

“Monster…”

A deep voice from behind rescued the mounted bandits, who were paralyzed with fear.

“You’ve done enough. Go on now. I’ll handle this place.”

At the appearance of the voice’s owner, Pung Yang, the Red Wind Band Leader, the mounted bandits retreated like the tide going out. Only then did the two Peak masters face each other.

“Good to see you again, Senior Cheol.”

“I don’t recall ever taking a bandit as a junior.”

“You’re still as prickly as ever. They say even brushing sleeves with someone creates a connection, and you and I have crossed hands, haven’t we?”

“We did. Then you ran away without even looking back.”

“Let’s call it a strategic retreat. I didn’t expect Senior Cheol to show up there, either.”

“Are your internal injuries healed?”

“My insides were burning, so I had a rough few days. But it wasn’t enough to kill me, which is why I’ve come back despite my shame.”

“Today, it won’t end with mere heat.”

“Oh, dear. How about we settle this through conversation? For a man of your age to have such a fiery temper…”

At Pung Yang’s shameless remark, Cheol Mubaek ground his teeth.

“Conversation? If you hadn’t betrayed us, Lee Cheonbaek, my friend, might have lived.”

“I’m not stupid enough to join a fight with no chance of winning.”

“As if that weren’t enough, you killed Lee Seogwang too?”

“I’m not softhearted enough to spare a brat who came at me without knowing his place.”

Pung Yang smiled gently and continued.

“If I’d known that brat would become my brother-in-law, I might have spared him.”

“You bastard!”

A lava-like aura boiled up from every inch of Cheol Mubaek’s body. Under the formidable Scorching Yang Qi of a Peak master, the snow blanketing the ground melted away, and the vegetation turned yellow.

Pung Yang let out an exclamation at the sight.

“Your internal energy really is remarkable. If Senior Cheol had only set his mind to it, the opponent I faced today would have been the Mount Heng Fist Sect.”

“I’ll tear your limbs from your body.”

“Still, you shouldn’t be too confident.”

“Don’t expect the same stroke of luck as last time. Today, you won’t have anyone to use as a shield.”

Pung Yang smiled faintly.

“Why do you think I sent my men away?”

“That…”

Cheol Mubaek hesitated. Pung Yang’s relaxed attitude had been bothering him for some time.

*What is he plotting?*

Last time, Pung Yang had withdrawn after suffering internal injuries in barely a hundred exchanges. The fact that the man who had used his subordinates as shields to escape had sent everyone away and come here of his own accord meant that he was confident enough to do so…

“What kind of dirty trick are you planning?”

“A dirty trick? I simply couldn’t use a chicken-killing knife on a tiger, so I stepped in myself.”

“You? Alone?”

“Is there any reason I can’t?”

“There’s no way. I’m grateful, if anything.”

Cheol Mubaek glared at Pung Yang suspiciously and clenched his fists.

“Thanks to you, this will be over easily.”

Whoooosh!

The instant he finished speaking, a scorching gale rushed straight toward Pung Yang. Pung Yang swallowed a breath and swung his curved saber at the red fist energy flying toward his chest.

Boom! Boom-boom!

The two Peak masters collided. Roaring explosions rang out one after another, and the resulting wind swept across the snow-covered ground.

Beneath a mound of snow that had leaped high into the air, one man staggered backward.

“Ugh.”

Pung Yang swallowed a groan and looked at his torn palm. He had avoided the disgrace of dropping his weapon, but the difference in strength was undeniable.

“You’re still as strong as ever.”

Cheol Mubaek stepped toward him and answered.

“You’ll regret this, but it’s already too late.”

“I feel the same way.”

“I’ll have to tear that mouth of yours apart first.”

Fwoooooosh!

Cheol Mubaek lunged forward with the movements of a tiger.

The fierce forms of the long-lost Shura Annihilating Fist poured down upon Pung Yang.

Kwa-gwa-gwang!

* * *

A fierce bloody battle was raging along the fortress walls. Despite facing a four-to-one disadvantage in numbers, the martial artists of the Mount Heng Sword Sect refused to retreat.

“Retreat, and all that awaits us is death!”

“Are you going to let those mounted-bandit bastards take our home from us?”

“Let’s avenge the martial brothers they killed!”

Slice! Thrust!

“Aaargh!”

“D-don’t push me!”

The mounted bandits of the Red Wind Band had fallen into confusion. The effects of the earlier fire attack and the fear that another trap might be waiting held them back.

In stark contrast, the martial artists of the Mount Heng Sword Sect charged at them wild-eyed. The mounted bandits were helpless against their unstoppable momentum and were cut down one after another.

“Don’t run away!”

“Any bastard who retreats dies by my hand!”

The mounted bandits who served as squad leaders shouted at the top of their lungs, but they were unable to restore order. Instead, they too had to surrender their lives to arrows that seemed to fly out of nowhere.

Thwack!

“Ghk. Gaaah…”

“Squad Leader!”

Lee Seowol stood atop the highest watchtower, drawing her bowstring without pause.

Beside her were the five best archers among the martial artists of the Mount Heng Sword Sect.

Twung! Thud!

Every time a bowstring was drawn, a mounted bandit fell. Squad leaders, or those who appeared to rank even higher, were their highest-priority targets.

*One more. One more.*

But the battle was unfolding more harshly than expected.

The martial artists of the Mount Heng Sword Sect had entered the battle with fewer troops from the very beginning. They grew exhausted at an alarming rate, and before long, one or two at a time began losing their lives to stray blades.

The mounted bandits, meanwhile, were gradually recovering from their confusion.

“Get a grip! There aren’t many of these Mount Heng Sword Sect bastards!”

“If we kill these men, victory is ours!”

The martial artists of the Mount Heng Sword Sect had nothing left to lose. They fought desperately, disregarding their disadvantage.

“Kill them!”

Slice! Slice! Slice!

But every time one mounted bandit was cut down, two more appeared to fill the gap. When two were cut down, three took their place.

“Gasp, gasp!”

A martial artist of the Mount Heng Sword Sect swung his sword frantically, only to be hacked apart by five or six weapons that sprang at him from every direction.

Slice! Thud-thud-thud!

His neck, chest, abdomen… Martial artists were cut and pierced all over, dying without even having time to scream. Their bodies fell in growing numbers.

The mounted bandits of the Red Wind Band, their momentum rising, continued pressing the attack without pause. Before anyone realized it, half the fortress wall was packed with enemies.

“Haa, haa.”

Twung! Twung! Twung!

Lee Seowol summoned every last bit of strength she had and drew her bowstring. Blood ran from her once-delicate fingers and between her clenched teeth, while the dry inside of her mouth reeked of a sickly sweetness.

“There!”

After firing arrows without rest, her position was discovered before long. When about twenty mounted bandits raised their shields and charged toward the watchtower, desperate shouts rang out.

“Sect Leader!”

“You have to get away! They’re coming!”

Three shichen—six hours—had passed since the siege began. Lee Seowol had only practiced archery as a hobby. She was not a martial artist, and her Stamina had reached its limit long ago.

But she did not stop. She forced strength into her thin, trembling arms and searched for her next target.

*Escape? Where would I go?*

She had lived here her entire life. To Lee Seowol, the Mount Heng Sword Sect was both her hometown and something she had to protect until the final moment of her life.

The same was true for the martial artists who continued their last stand.

“Stop them!”

“Never let them reach the Sect Leader!”

Their desperate cries were futile. The fortress walls had already been overrun.

The surviving martial artists of the Mount Heng Sword Sect retreated to the watchtower. But more than a hundred mounted bandits were closing in from every direction.

Eyes gleaming with killing intent and desire shone between the torches held by the advancing enemies.

“You damned bastards dare…”

“I’ll tear every last one of you limb from limb and throw you to the dogs!”

The killing intent of the mounted bandits surrounding the watchtower in a circle stabbed at their skin.

Just as everyone was falling into despair, Lee Seowol suddenly drew her bowstring toward the sky.

Whoooosh.

Trailing a tail of fire, a single fire arrow descended toward the gate, which was shrouded in darkness.

It was a light meant to find one person.

*Uncle Cheol.*

The Tiger of Mount Heng, Cheol Mubaek. He was the Mount Heng Sword Sect’s final hope.

That was when a man walked out beneath the light revealed by the fire arrow.

Clomp. Clomp.

“I suppose it’s a little late to say this now…”

Lee Seowol had heard that voice only once, but she could never forget it, not even in her dreams.

Unable to bring herself to look at him, she closed her eyes.

Pung Yang smiled broadly at her.

“You’ll have to marry me.”

* * *

The hunter Cheol Mubaek became the Tiger of Mount Heng because of a fortuitous encounter.

While tracking wolves along a mountainside in the vast Mount Heng range, he fell between cliffs into a hidden cave. There, he discovered a martial arts manual and an elixir left behind by a reclusive master.

*I’m going back. I’m going back alive, no matter what!*

Cheol Mubaek learned martial arts to survive. When the fasting pills in the hidden cave ran out, he tore up grass growing between the cliffs or caught bats to eat as he trained.

After no less than three years, he climbed the cliff with his bare hands and returned to the village.

What awaited him was his home in ruins—and the deaths of his wife and child.

*Had it been a couple of months since we lost contact? That bastard Hwang, who’d always had his eye on your wife…*

By the time he came to his senses, he had already beaten the village’s leading landowner and all his servants to death.

After avenging his family, Cheol Mubaek returned to the hidden cave and resumed his martial arts training. It was a whip he used against himself, and atonement for his family.

How much time passed like that?

Before he knew it, Cheol Mubaek was being called the Tiger of Mount Heng.

But…

“Hoo. Even a tiger would cry.”

Cheol Mubaek panted harshly. His once-brilliant eyes were clouded like a sky covered in dark clouds, and his beard was drenched in blood.

*I have to hurry. I have to stop that bastard…*

But all he had left was his will. His body, with its limbs broken, had already slipped beyond his control. He had displayed martial arts worthy of the title Tiger of Mount Heng, yet he still could not defeat Pung Yang.

*How in the world did he…?*

The result seemed obvious. Pung Yang had only just entered the Peak realm, barely capable of creating blade qi, while Cheol Mubaek was a Peak master who had reached a mature realm stage.

Pung Yang had been as precarious as a candle in the wind. Then he had suddenly changed after pulling an unidentified hard wooden case from inside his robes.

*The red pill. Yes, that was definitely it.*

Cheol Mubaek had made a mistake by retreating because he thought it might be a hidden weapon. After Pung Yang gulped down the pill, he was no longer the leader of the ordinary mounted-bandit group Cheol Mubaek had known.

*How can a human being become that strong?*

Cheol Mubaek’s eyes trembled as he recalled Pung Yang’s movements.

The gap between them was so vast that it seemed impossible to win, even if they fought ten or a hundred more times. Pung Yang had overturned the battle in an instant, broken all four of Cheol Mubaek’s limbs, inflicted massive internal injuries, and then left.

*I’ll let you live for now. I’ve decided I want your martial arts formula as a wedding gift.*

Cheol Mubaek’s eyes reddened as he recalled Pung Yang’s parting words.

The Shura Annihilating Fist was a martial art passed down to a single successor and never taught to outsiders.

He would choose suicide rather than hand it over to Pung Yang, but Lee Seowol—whom he cherished like a daughter or granddaughter—troubled him.

*What on earth am I supposed to do?*

It was at that moment, as Cheol Mubaek stared at the sky with a heavy heart, that it happened.

Thud-thud-thud-thud!

The sound of approaching hooves grew louder and louder before coming to a sudden stop at his feet.

Beneath the brilliantly shining moon, four pairs of eyes looked down at him.

“Doesn’t the Red Wind Band have a retirement age? Why is an old geezer still out here playing bandit…?”

“Young Master Jin, that’s Great Hero Cheol Mubaek, the Tiger of Mount Heng.”

“Gah! I’m sorry. Hey, Mujin. Hurry up and apologize. What are you waiting for?”

“The squad leader is the one who made the mistake, so why should I…?”

Smack!

“Grandpa—no, Sir. Are you all right?”

Instead of answering, Cheol Mubaek stared intently at the young man’s chest.

One character was embroidered on his navy martial robe.

進.

“Taiyuan… the Jin Family?”

“Oh, you recognize it?”

The young man, Jin Taekyung, grinned.

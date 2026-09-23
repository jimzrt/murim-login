# Checkpoint Review — 795–799

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

# Chapters 795–799

## Plot

Huginn confirms that Muninn killed Siegfried Wassmann, completing Jin Taekyung’s Supreme Peak Quest [An Unknown Death] and rewarding him with the special Item Eyes of Truth. Huginn reveals that “Muninn” is an identity passed among five people; the current one is a white man whom Huginn saw about three years ago. A Muninn from that period supplied Michael Silbert with intelligence about Cheon Taemin, Leviathan, and the plan to lure Leviathan to Tokyo. Jin concludes the Muninns gathered intelligence, eliminated rivals, and moved unrefined Magic Gems. He recalls the search teams, but one convoy is attacked before it can withdraw.

The Prophet massacres the J1 team, leaving Yamamoto Genji as the sole survivor, then escapes before reinforcements arrive. Yamamoto recounts that The Prophet stopped all ten transport vehicles and drained blood and a pale mist from the dead. Magic Johnson rules out human magic; Jin recognizes that The Prophet is a monster. The Prophet leaves a message meant to lure Jin, but its contents are unknown. Jin blames himself for the deaths and treats Yamamoto’s injuries.

Elsewhere, Amir’s concealed group watches a convoy of more than five hundred people approach. Amir orders Hamid and the others to wait for The Prophet and the coming holy war.

## Continuity

- Jin is the World Hunter Federation’s Alliance Leader, pursuing Main Quest [Cataclysm], which requires him to eliminate The Prophet within an unspecified time limit.
- Jin completed Supreme Peak Quest [An Unknown Death] after learning Muninn killed Siegfried Wassmann; he received the special Item Eyes of Truth.
- “Muninn” is a succession of identities. Huginn says the current Prophet is the fifth; his description of the current one is an uncertain personal impression. A Muninn from about three years ago gave Michael Silbert intelligence about Cheon Taemin, Leviathan, and the plan to lure Leviathan to Tokyo.
- Huginn remains captive. Jin ordered further questioning and did not promise to release him.
- The Prophet is a monster. He killed nearly all of J1, draining blood and a pale mist from the victims; the nature of this power is unknown. He escaped, and his location remains unknown.
- Yamamoto Genji is J1’s sole survivor. He is recovering after Jin treated him. Jin suspects he tried to flee during the attack; why The Prophet spared him remains unclear.
- The Prophet left a message intended to draw Jin in; its contents are unknown.
- Amir and Hamid lead a group hidden by an unseen veil near a convoy of more than five hundred people. They intend to await The Prophet and wage a holy war; their location and target are unknown.
- The cause of the desiccated desert deaths found earlier remains unresolved; do not assume they were caused by the same process as the J1 victims.

## Translation Decisions

- Keep **magic**, **mana**, and **magical power** distinct.
- Render **Muninn** as the current identity of The Prophet, while preserving that the name passes between five people.
- Keep the System Quest title **An Unknown Death**, its Grade **Supreme Peak**, and **Eyes of Truth** as the special Item.
- Render **질풍불참** as “Swift No-Show” in the Yamamoto joke.
- Retain “Chōsenjin” as the ethnic slur Yamamoto uses, and “Inshallah” (“God willing”) for **인샬라**.

## Durable state

{
  "active_continuity": [
    "Jin Taekyung is the World Hunter Federation’s Alliance Leader and is pursuing Main Quest [Cataclysm], which requires him to eliminate The Prophet within an unspecified time limit.",
    "The Prophet is a monster who stopped all ten J1 transport vehicles and absorbed blood and a pale mist from the dead; the nature of this power is unknown.",
    "The Prophet left a message intended to lure Jin; its contents are unknown.",
    "Yamamoto is J1’s sole survivor. He says The Prophet left after reinforcements arrived; Jin suspects Yamamoto tried to flee.",
    "Amir and Hamid lead a group concealed by an unseen veil near a convoy of more than five hundred people; Amir orders them to await The Prophet and the coming holy war."
  ],
  "continuity_sources": [
    799
  ],
  "open_questions": [
    "What message did The Prophet leave for Jin, and where is The Prophet now?",
    "Why did The Prophet spare Yamamoto, and what happened when Yamamoto tried to flee?",
    "What was the pale mist absorbed from the J1 victims, and what is the nature of The Prophet’s power?",
    "Where is Amir’s concealed group, and what is its intended target?"
  ],
  "safe_through": 799,
  "temporary_decisions": [
    "Keep magic distinct from mana.",
    "Render 조센징 as “Chōsenjin,” identifying it as an ethnic slur."
  ],
  "version": 1
}

## Reading copies

## Chapter artifact 795

# Chapter 795

> **System**
>
> Quest success conditions met!
>
> **Mission:** Discover the truth behind the death (Complete)
>
> Quest *An Unknown Death* successfully completed!
>
> You have obtained the special Item *Eyes of Truth*!
>
> You have gained a large amount of EXP!

*Ding. Ding. Ding.*

The System messages flowing into my eyes and ears were the final step—the confirmation that everything Huginn had said was true.

But a Quest was just a Quest. I wanted more information than that.

Everything about Muninn—or the person called The Prophet.

“Spill everything you know about him. Don’t leave out a single thing.”

Huginn’s unsteady breath brushed my face as I leaned in close.

“This isn’t what we agreed at the start…”

“An agreement? Of course I have to keep it. Just not now.”

The condition for keeping my promise in the first place was confirming that The Prophet had killed Siegfried Wassmann. But in this relationship, I was the one holding all the cards.

“Talk. Or you’ll rot in prison until the day you die.”

“……!”

“You know what I’m like. If I say I’ll do something, I do it. So quit trying to outthink me and open your mouth. If you’re sure you won’t get caught, go ahead and mix in a lie.”

A person’s eyes held a great deal of information.

And in that sense, the resignation that had just taken over Huginn’s eyes was proof that he’d finally given up on everything.

“……Fuck.”

With a curse that sounded almost like a sigh, Huginn began to speak.

“I don’t know the details, either. Not exactly what the Muninn of today is like.”

At his first words, I’d grabbed a potion bottle. But when Huginn hurriedly added the rest, I frowned.

*The Muninn of today?*

That was too loaded a phrase to brush off.

It sounded as if…

“Like he hasn’t always been the same person.”

“That’s right. He’s changed several times.”

My mind raced. I slowly lowered the potion bottle and fixed Huginn with a steady gaze.

“Tell me more.”

“Since I became an adult and officially began serving the Guild Master, I’ve met three Muninns. Including the ones before then, the person now called The Prophet is the fifth Muninn.”

“What do you mean, before then?”

“When the Great Cataclysm hadn’t ended yet. Everywhere you went, there were war orphans. I was one of them, too. Though I wasn’t a child, of course.”

I didn’t need to hear the details to see the outline of it.

Good people and bad people saw the world in completely different ways.

The good might have pitied the countless orphans left in the wake of the Great Cataclysm. Those on the opposite side would have used them as stepping stones for their ambitions.

*Lee Jungryong acquired Go Jun the same way.*

The good fortune of Awakening came equally to everyone in humanity after their twentieth birthday.

In that sense, orphans with no one to rely on were lottery tickets that hadn’t been scratched yet. Huginn must have been a diamond Michael Silbert had plucked from the mud.

And…

“That’s when you met Muninn.”

“More precisely, the first Muninn. That was the first and last time I saw him.”

“The last? What happened after that?”

“It was after the Great Cataclysm ended. The Guild Master didn’t want my existence to come to light, so he kept me close after I’d completed a certain amount of training in secret. From that day on, I became Huginn, and I was introduced to a man with an unfamiliar face.”

“And he was the new Muninn?”

Huginn nodded.

“What happened to the first Muninn?”

“I don’t know. The Guild Master only told me he’d gone missing during the Great Cataclysm. He probably died in the war.”

“Gone missing? If he was Michael Silbert’s right-hand man, he must have been highly skilled.”

At my sharp look, Huginn gave a bitter smile.

“If you don’t believe me, there’s nothing I can do. But that’s all I know. Back then, I hadn’t even Awakened. I wasn’t Huginn yet.”

“When exactly?”

“Spring of 2021. The Guild Master was already famous by then. After the Great Battle of Paris, he was emerging as one of the heroes who embodied France. No, Europe.”

I studied Huginn’s expression for a moment, but couldn’t find any sign of a lie in his face or eyes.

But the important part started now.

“The Prophet… Who’s the fifth Muninn?”

“Hmm.”

“Think back. Just tell me what you know. Everything you saw and heard.”

Huginn furrowed his brow and thought for a while, but it didn’t take long for him to speak.

“He was a white man. Most of his face was covered, so I couldn’t get a good look at him… But his build didn’t look suited to close combat. That’s just my personal impression, of course.”

You couldn’t judge a Hunter by their build alone—not when you had someone like Jeok Cheongang, with his slight frame, as proof.

But if someone as skilled as Huginn had gotten that impression, it was worth taking seriously.

The problem was… the information he’d given me was nowhere near enough to figure out The Prophet’s identity.

“A white man. Maybe a ranged Hunter. That’s all you know?”

Huginn swallowed dryly at my calm but icy voice, then answered.

“That’s why I said I didn’t know much. I saw him only once, about three years ago. And even then, the Guild Master ordered me to leave right away.”

“Then how do you know he’s The Prophet? That he killed Siegfried Wassmann?”

“The Guild Master told me when the time came. That’s how it’s always been with Muninn.”

“Always?”

“When I stayed by the Guild Master’s side and acted as his hands and feet, they were weapons sent on more dangerous missions. They’d disappear for a year, sometimes several, then suddenly show up one day. I always came into the picture afterward.”

“For example?”

“Information about Sky, Cheon Taemin. And…”

“And what?”

“That…”

*Smack!*

My palm whipped out like a lash and slapped Huginn across the face.

After hesitating for a moment, he spat blood and muttered a few words through his pained expression.

“Tokyo. Leviathan. Magic Gems.”

“……!”

“All of it was information the Muninn from three years ago brought back. That’s everything. Damn it.”

I stared at Huginn, frozen like a statue.

Was it anger?

No. Shock.

*He knew about Leviathan from the start, and used Magic Gems to lure it to Tokyo.*

And the one who gave that information to Michael Silbert was none other than Muninn—the very man now called The Prophet.

The truth finally laid bare sent a chill down my spine, as if someone had poured ice water over me.

*How the hell?*

Even modern humanity, which had brought civilization to greater heights than ever before, still knew little about the deep sea.

And yet… he’d found the catastrophic presence lurking in those dark, distant depths.

Maybe it had all been on Michael Silbert’s orders. But could that really be the whole story?

*Damn it.*

I swallowed the curse rising from deep in my chest.

Now I understood.

Why no one had ever noticed Muninn’s existence.

A hidden blade that secretly visited Michael Silbert once every few years—sometimes after just one.

Unlike Huginn, he hadn’t stayed at Silbert’s side day to day. And since he was sometimes replaced because of his dangerous missions, there’d been no way to notice him.

Even Huginn, who’d handled most of Michael Silbert’s affairs as his right hand, barely knew anything about Muninn.

But one thing was certain…

*He’s dangerous. Far more than I ever imagined.*

He’d taken down Siegfried Wassmann, an outstanding Grand Mage, all on his own. He’d also drawn the outlines of the events behind this terrorist attack and supplied the information to Michael Silbert.

*Michael Silbert hadn’t done it on his own.*

Michael Silbert had reached his current position thanks to the loyal Muninns who’d died for him.

I didn’t know what kind of results the previous Muninns had achieved, but the Prophet I was picturing now was already far more than a mere subordinate.

Another root. Or a second Michael Silbert.

*Where the hell did he find people like that?*

No matter how vast the world was, no matter how many secrets it held, things eventually leaked out somewhere. Just as the great Guilds secretly trained new S-rank Hunters beyond the public eye.

But this was beyond anything I’d expected.

*They must have been handling the dirty work for a long time.*

Five Muninns. And the fifth Muninn.

They were the darkest shadows Michael Silbert had kept hidden.

For a long time, they’d smuggled unrefined Magic Gems out of the Middle East and Africa without pause, and stored them away. They were warehouse keepers, blades that eliminated rivals, and informants, all at once.

At least, until Michael Silbert died.

*But now the Prophet had all of it.*

This wasn’t just a pair of hands and feet like Huginn.

The arm called Muninn, torn from its dead master’s body, had already made itself a new body.

The Prophet.

An heir who commanded countless fanatics from a religion followed by twenty percent of the world’s population—and who’d inherited everything his dead master had hidden away.

That madman now had the knife’s handle in his grasp.

And maybe…

“Fuck.”

No. It couldn’t be that.

I couldn’t make a firm judgment based on information that was still uncertain, not in a situation like this.

I forcibly brushed away the thought that had flashed through my mind and sprang to my feet.

I had to tell everyone about this information as soon as possible and call back the search teams scattered across the Middle East.

The Prophet was powerful enough to kill a Grand Mage on his own.

I’d sent them into the desert to prevent even greater losses, not to throw their lives away.

“W-wait!”

Right. This guy was still here.

At the desperate voice holding me back, I turned around.

Before he could get another word out, I snatched a potion bottle from the box and brought it down on the crown of his head at lightning speed.

*Crash! Thud.*

Huginn lost consciousness in one blow and toppled over along with his chair.

Probably a concussion at the very least, but he’d been drenched in potion, too. He’d be fine.

“Make sure you live a nice, long life, okay?”

I spat phlegm toward him, brushed the glass dust off my hand, and walked outside.

Then I nodded at the torturers pacing in the hallway.

“He told us a fair amount, but there might still be things he hasn’t said.”

“Oh, then…?”

“Get it out of him. Squeeze him for every last drop, even his soul.”

The torturers answered, their faces lighting up.

“Yes, sir.”

“I’ll do my best. There are a lot of methods we haven’t tried yet.”

“Oh, look at this, Michael! Santa left us a whole box of potions!”

“We’ll put them to good use, Boss!”

A promise?

You make those with people. Not trash like Huginn.

“Everyone on the leadership team, to the strategy room. Right now.”

As I listened to Team Leader Choi answer through my smartphone, I walked down the hall. Then I turned my head and looked out the window.

The moon peeking through the clouds looked unusually red tonight.
## Chapter artifact 796

# Chapter 796

That night, someone paused their hurried steps and looked out the window. They thought the moon looked redder than usual.

They weren’t imagining it.

Blood Moon.

It was a phenomenon sometimes seen during a total lunar eclipse or when the atmosphere was unstable. The magical power levels, climbing day by day, were changing not only the state of the atmosphere but the climate itself.

*Whoosh.*

The scattered raindrops grew heavier.

A downpour that seemed out of place in this barren land, where the annual rainfall was less than 250 millimeters, soon blanketed the whole area.

Endless sand, with a few trees scattered across it.

And the head of a being invisible to the naked eye.

*Tap. Patter-patter.*

The rain bounced away without touching any part of his body.

The Prophet, crossing the vast desert behind an invisible barrier, abruptly looked up at the sky.

Dark and noisy.

The ominous storm clouds that had been gathering for days were unleashing rain and thunder with ferocious force.

As if furious at everything that had happened on this land.

But The Prophet paid them no mind. He studied the sky—or, more precisely, opened his senses wide and listened to every sound coming from all around him.

*Rumble. Rrrumble.*

Thunder boomed ceaselessly overhead. The Prophet paused to focus on the sounds around him, then muttered,

“They’re gone.”

He meant it literally.

The sharp cries of eagles, echoing from far away, could no longer be heard.

The persistent flying beasts some pursuer must have sent after him had finally given up and turned back.

*What a nuisance. Good riddance.*

Avoiding satellite surveillance and unmanned reconnaissance aircraft was easy enough.

The magical power mixed into the atmosphere served as a shield against tracking, and concealment spells weren’t made just to boil in a stew.

But those eagles were different. Even the Familiars commanded by the few mages who specialized in mental magic were no more than dirt under their claws by comparison.

They’d followed him for hundreds of kilometers without showing the slightest sign of slowing down.

And their eyes, shining with magical power, looked as if they might even see through his magic.

*They can’t be Familiars… It must be him.*

The Skeleton King. Or perhaps the Stone King.

Thinking of a mere monster that had sided with humanity, The Prophet frowned without realizing it.

The desert was still vast. But the undead army that creature commanded would expand the search area and drastically shorten the time it took to search it.

*This is unexpected.*

Though a lot of things had already gone against his expectations.

He hadn’t thought Michael Silbert would fall so easily, and he hadn’t expected the World Hunter Federation to get its internal chaos under control so quickly and close in right on his heels.

But there was one thing The Prophet knew: every one of these anomalies had started with one man.

*Jin Taekyung.*

Many had shone brightly before, but they’d all been meteors—flashing into view for a brief moment, then vanishing in the blink of an eye.

Jin Taekyung was different. He was a comet.

From the moment he first appeared, he’d been part of the celestial body called the world. Now, he’d become its center.

He was growing so fast that no one could predict where his limits lay. Fast enough to make all of The Prophet’s preparations so far seem pointless.

*Clink.*

A faint metallic sound rang out, following his fingertips as they unconsciously groped for something.

Forcing down the impatience welling up inside him, The Prophet murmured,

“Just a little longer. I can finish it with just a little more time.”

The problem was time.

The necessary components to bring this plan—one that couldn’t afford the slightest error—to perfection had not yet all been gathered, and the enemy’s encirclement was closing in fast.

In these circumstances, The Prophet had only one option left.

*Hunt.*

But time was short. To complete his plan successfully, he had to make it bigger and bolder than before.

For example…

*Vroom.*

The Prophet’s eyes lit up as he spotted transport vehicles moving along a high sand dune, kicking up a thick cloud of dust.

* * *

“Chikushō.”

At the low curse from Yamamoto Genji, Japan’s S-rank Hunter, the Self-Defense Forces Hunters shifted away from him and exchanged glances.

Japan was a long way from being called a Hunter powerhouse, but everyone dispatched to the Middle East was a veteran among veterans. They’d also known each other for a long time, so by now a glance was enough to get the general idea.

*What’s his problem?*

*Isn’t it obvious? Who else could it be?*

*Eeh? Jin-sama?*

*Right. Yamamoto-san got really mad at that transmission from headquarters earlier.*

The whole story was simple. About thirty minutes ago, headquarters had issued an emergency withdrawal order, and Yamamoto Genji had refused.

Then a reply came right back.

Not in the communication officer’s stiff voice, but in the vivid voice of a young man.

> “When Leviathan was wrecking Tokyo Bay, you didn’t come even when we called. You son of a bitch. What? You’re not coming? Give me your coordinates right now. If you won’t come to me, I’ll come to you.”

Who was Jin Taekyung?

The only person who could fill the void left by the unconscious Cheon Taemin, and the Alliance Leader of the World Hunter Federation, who had the support of all humanity.

But before that, no one should forget his temper—the kind that ignored all caution, sometimes, or rather, quite often—and his terrifying skill.

The Self-Defense Forces Hunters, their knees weak at the Supreme One’s reply—practically a murder threat—had desperately tried to talk Yamamoto down. Even after climbing into an evacuation vehicle, Yamamoto Genji still couldn’t contain his anger.

“You bastard! How dare one of those damn Koreans…”

The Self-Defense Forces Hunters pretended not to hear him. Right now, they all had to be deaf and blind.

Honestly, they didn’t much like Yamamoto Genji’s attitude, either. But if word of it reached their superiors, not only would they be cursed out, Japan would get dragged into it, too.

*More of this?*

*No. Absolutely not.*

The Defense Minister, who had played a major role in the Leviathan incident—including preparing a kamikaze operation—was now in a federal prison after his connection to Michael Silbert had come to light. And the kind but stupid Prime Minister couldn’t even go a few days without spewing more shit.

> [Japanese Prime Minister Koizumi: “Yamato people, fight for Jin-sama, the great shogun who defeated Susanoo for us!”]
>
> [Japanese Prime Minister Koizumi, asked by a reporter about the Self-Defense Forces’ strategy for their upcoming deployment to the Middle East: “Combat should be fun, cool, and sexy.”]
>
> [Former U.S. President Joseph Biden: “I understand the Japanese Prime Minister. When my dementia was in its early stages, I didn’t know what I was saying, either.”]
>
> [Chuck Hagel: “I think they’re both just crazy.”]

The Self-Defense Forces Hunters felt sorry for themselves.

The Defense Minister would spend his twilight years in a federal prison, and the Prime Minister was using the media as a loudspeaker to announce, without a hint of restraint, that Japan’s leader was a lunatic.

The mood was so bad that even Korean netizens, who’d been holding back on their comments after picking up on the tension, had said things like this:

> **Top comment:** I don’t really want to bring this up when things are already tense, but… do those guys have something against Japan?
>
> └ The Japanese Prime Minister and Defense Minister are anti-Japan, lmao. Fuck.
>
> └ If you ask me, they must’ve had something going on in a past life.
>
> └ One of them was a turtle ship in a past life, and the other was a lunchbox bomb. Seriously, it’s not easy to spew that much shit.
>
> └ I wonder if this is how the independence fighters felt when they saw Mutaguchi Renya…
>
> └ Shadow independence army. Agreed.
>
> └ Sushi country: “Uh, what are those guys doing?”

In the middle of all this, even Yamamoto Genji, once called the pride of the island nation, had lost face. People had found out that he’d failed to show up twice in a row: first during the Leviathan incident, then at the launch ceremony.

Why had he skipped the launch ceremony?

Even the Self-Defense Forces Hunters didn’t know. If they’d known the real reason, they probably would’ve spat in his face, pride of the island nation or not.

Yamamoto Genji had simply been… embarrassed.

*Damn it. I should’ve just gone.*

At first, he’d been afraid and avoided Leviathan. Then, because he didn’t want to face Jin Taekyung, he’d made up a personal excuse to skip the launch ceremony.

Of course, that might have been why he’d survived this long in one piece. But once everything was over, what awaited him was an insult worse than death.

> Those guys really are something. That S-rank Hunter hasn’t shown his face once, even now, lmao. What was his name again?
>
> └ Genji.
>
> └ Isn’t it Hanzo?
>
> └ That’s Genji’s older brother.
>
> └ Are you guys insane?
>
> └ Why are you talking about a dead game from ages ago, you fossils?
>
> └ It’s true, though? Look it up if you don’t believe me.
>
> └ ?
>
> └ It’s real; he actually has an older brother named Yamamoto Hanzo.
>
> └ How is this real?
>
> └ So can Genji use Swift Strike?
>
> └ He’s great at Swift No-Show.
>
> └ LMAO
>
> └ Goddamn, that really hurts my pride.
>
> └ wwwwwww I was about to get mad, but I laughed without even realizing it?
>
> └ “Don’t laugh at him too much, okay? I thought it was kind of funny, though.” wwwww
>
> └ Even wasabi’s laughing, lmao.
>
> └ Lmao, wasabi showed up, but where’s the black bean sauce?
>
> └ It’s now confirmed that Jin Taekyung is from Shanxi Province, China. After examining old historical records, renowned historians at Peking University discovered the Jin Family of Taiyuan (see more)
>
> └ ;;;; The second they see an opening, these bastards launch straight into their Jin-is-Chinese campaign.
>
> └ Didn’t the Red Guards destroy their old records?
>
> └ (This comment has been hidden.)
>
> └ So did Genji—or was it Hanzo—actually go to the Middle East this time?
>
> └ Yeah. I heard they accepted him since he’s an S-rank Hunter, at least.
>
> └ Isn’t he just going to sit out the fighting? Doesn’t seem like he’d be much help anyway. They should just send him around to entertain the troops.
>
> └ Captain Wasabi.

*How dare they. How dare they insult me like that!*

Remembering the online comments once more, Yamamoto Genji shuddered.

Swift Retreat. Captain Wasabi.

The more he thought about those words, like awls digging into his lungs, the more his anger surged, making his teeth grind.

And on top of that…

*He sent such a rude reply? In front of the Self-Defense Forces, too?*

Jin Taekyung’s warning, which was practically a threat—and the way the Self-Defense Forces Hunters had hurried to hold Yamamoto back instead of getting angry at such rudeness—had stripped away every last bit of Yamamoto Genji’s pride.

*If I go back now, what does that make me?*

By all accounts, he was an S-rank Hunter. But everyone who’d heard the rumors looked down on him. He’d scoured the desert with everything he had, determined to change how they saw him, and it had looked as if he was about to get results.

And now, an emergency withdrawal order.

Yamamoto Genji had been muttering curses under his breath nonstop when suspicion suddenly crept into his mind.

*That Korean bastard… Could it be—no, it has to be. There’s no doubt.*

That was it. All of this was Jin Taekyung’s scheme to stop him from earning credit. The anti-Japanese sentiment that had started long ago had followed him all the way here.

Reaching a conclusion that was practically a delusion, Yamamoto Genji barked,

“Oi, sutoppu!”

At his sudden order to stop, the evacuation vehicle ground to a halt.

Unlike before they’d set out, when they’d strongly objected to disobeying the withdrawal order, the Self-Defense Forces Hunters now meekly followed his command. Yamamoto’s face brightened.

*That’s right. I’m the beacon of the great Yamato people! The one they follow isn’t that Korean—it’s me…!*

But the thought cut off the very next moment.

The Self-Defense Forces Hunters looked confused. And at the same time, one fact flashed through Yamamoto’s mind like a streak of light.

“Wait. Who’s in the driver’s seat right now?”

One of the Self-Defense Forces Hunters blinked and answered,

“No one.”

“Eeh?”

“It’s an unmanned vehicle.”

Silence fell.

They stared blankly at one another, then suddenly realized.

Why the vehicle, which had been moving along just fine, had stopped. Why even the sound of the rain, which had been all around them, had vanished.

“Ambush!”

“We’re under attack!”

And at the same time—

*BOOM!*

A tremendous roar and impact crashed down on them.
## Chapter artifact 797

# Chapter 797

Though the main force’s command had been assembled in only a few days, it had established a well-organized system and amassed tremendous fighting strength.

The World Hunter Federation had taken the lead, with the Great Nations in the G20 among the first to contribute their strength. Even the UN peacekeeping forces, reforged into elite troops through the Great Cataclysm, had joined them.

In that sense, the people gathered in the strategy room at this very moment were the head and limbs that made this massive organism move.

“So…”

Chuck Hagel, who had listened to my explanation in silence for a while, spoke slowly.

“That fucking terrorist was the one who’d been covering Michael Silbert’s ass from the very beginning?”

I nodded without hesitation.

“Yes.”

“Do you believe what he says? Huginn, I mean.”

“Am I crazy? I’m not going to trust a bastard like that.”

“Then what do you believe?”

“The fear he feels.”

Chuck Hagel studied me for a moment, then tapped the ash from his cigar.

“Sounds like it’s true.”

“At least, that’s how it felt to me.”

“You sure?”

“Not a hundred percent. Maybe ninety-five. Even Huginn has no reason to lie in a situation like this.”

“What about the remaining five percent?”

“The people currently keeping him company with knives in hand will fill that in. Maybe it’s already up to ninety-seven by now.”

The first time was the hard part. After that, it got easier. Now that Huginn had started confessing, he’d drag out everything he knew—or had forgotten he knew.

Pain wasn’t what broke a strong person. It was the fear inside them.

*Of course, he’ll still get plenty of torture before that.*

Everyone gathered here probably had a good idea of what was happening, but no one said it out loud.

What mattered most to us right now wasn’t Huginn, who was probably being reduced to a bloody mess. It was what we’d do next.

We had to draw up a new strategy on the assumption that everything he’d confessed was true.

That lunatic fanatic wasn’t just a terrorist. He was skilled enough to take down a Grand Mage by himself.

“Just how strong are we talking?”

At Team Leader Choi’s cautious question, Chuck Hagel smacked his lips.

“Hard to say. We know next to nothing about him.”

“Mr. Hagel. This may be an impolite question, but if you’d been in the same position as The Prophet and targeted Siegfried Wassmann, how would you have fared?”

“I’d met Siegfried, even if we weren’t close, so I could’ve taken him out easily. But for someone he didn’t know, given how reclusive he was? That’d be close to impossible.”

“Then, could it be…”

“It’s one of two things. Either he was so incredibly strong that Siegfried couldn’t even mount a proper defense. Or…” Chuck Hagel paused. “The Prophet was someone Siegfried had met before.”

“……!”

“……!”

Those explosive words froze the strategy room.

What Chuck Hagel had said was that serious—and that shocking.

The first possibility or the second.

We didn’t know which one applied to The Prophet, but either way, he was far beyond anything we’d expected. He was much stronger than we’d imagined.

“In that sense, Jin’s judgment was right. If we stayed scattered, we’d be easy to pick off one by one. Of course, if The Prophet is that strong, even a few hundred people gathered together might be useless.”

He was right. Even among S-rank Hunters, who were practically strategic weapons, there were clear differences in strength.

It was unlikely, but if The Prophet was comparable to Michael Silbert… it would take three average S-rank Hunters attacking at once, with a supporting force backing them up, to bring him down.

*The problem is, where the hell did someone that strong come from?*

No matter how I looked at it, I couldn’t figure it out.

The World Hunter Federation had already cleaned house. We knew the whereabouts and circumstances of every living S-rank Hunter and all the other major Hunters.

*He’s not an insider. So what is he?*

An unknown outsider. And if I put together what Huginn had told me, this outsider had appeared no more than five years ago.

Huginn had first seen The Prophet three years ago, but the last time he’d seen the fourth Muninn was five years ago.

Meanwhile, Siegfried Wassmann was a veteran among veterans, having fought countless battles during the Great Cataclysm. He might have been a scholarly mage, but no one earned the title of Grand Mage through books and research alone.

No matter how talented The Prophet was, there should have been an unbridgeable gap between them.

A kid who’d dropped out of the sky just a few years ago couldn’t overcome a difference like that, no matter what.

Well, there was one exception.

I was living proof that it could be done.

“The System…?”

“Hm?”

“Nothing. Just talking to myself.”

At Chuck Hagel’s raised eyebrow, I smoothly changed the subject, acting like nothing had happened.

“Anyway, how’s the withdrawal going?”

Team Leader Choi answered.

“So far, more than seventy percent of the people who were out searching have returned.”

“Faster than I expected.”

“We mobilized every transport vehicle we had. We also informed Magic Johnson, Faye Chen, and Prince Felix, and gave top priority to withdrawing every search team.”

This was the operations headquarters, but everyone else was leading their own groups according to their respective abilities.

We had to split up to search this vast region thoroughly.

It would’ve been stupid to make all those search teams travel thousands—sometimes tens of thousands—of kilometers just to report back here every time.

“Everyone from Team A1 has returned.”

“Team B2 is still on its way back. We expect them within fifteen minutes and are staying in contact.”

“We’ve temporarily lost contact with Team D4. We suspect interference from magical power, and we’ve dispatched a support team in case of an emergency.”

Reports poured in from all around the room, starting with Team Leader Choi.

Some of the headquarters’ search teams hadn’t returned yet, or we couldn’t reach them. But there was no immediate reason to worry.

As magical power levels rose, it was natural for mana communications and radio signals to grow hazy.

And even if something unpleasant like a Monster Wave happened, *that guy* would be able to handle it without a problem.

Beep.

—Emergency transmission, emergency transmission. This is Team F6. A monster army has appeared ahead. The monsters appear to be undead. Requesting support.

“……”

“……”

Team Leader Choi and I met eyes and sighed at the same time.

“Tell them not to attack.”

“Uh, they’re probably our allies.”

Chuck Hagel had jumped to his feet as soon as the radio crackled. He asked with a face like he’d bitten into something foul.

“Damn it. Is it that guy I’m thinking of?”

“Yes. Judging by Team F6’s current coordinates, it’s definitely him. They must’ve gotten confused.”

“Tell him not to scare the troops. A lot of them haven’t seen him in person yet. We don’t need pointless confusion.”

“The Skeleton King should take that into account while he’s moving, so there’s no need to worry too much…”

Beep-beep!

—Emergency transmission! Emergency transmission! There are way too many monsters! The boss monster, possibly a named one, is laughing like a maniac! This is terrifying! Requesting support!

“……”

After hearing the additional transmission, Chuck Hagel looked at us with a cold stare.

Team Leader Choi subtly looked away and muttered as if to himself.

“No one will get hurt. Probably…”

“That last bit didn’t sound very confident. Am I imagining things?”

“Yes.”

I let out a long sigh.

I’d sent that bastard to bring the troops back, and now he was scaring them instead.

Judging by the looks on the leadership team’s faces as they sat around us, they were probably wondering if we should deal with the Skeleton King before The Prophet.

*You’re dead when you get back.*

Just as I muttered to myself, another urgent transmission rang out.

Beep.

—Engagement in progress! Engagement in progress!

“Again?”

He was really dead.

But as I wondered how I could deal with the Skeleton King in a way that would make the story of his getting his ass kicked spread far and wide, an unexpected follow-up crackled in my ear.

—This is Team J1! Multiple dead! Multiple injured! Send support as fast as you can, aaagh!

Crunch. Splaash!

A chill ran down my spine.

A gruesome sound of flesh being torn and a scream rang out over the radio. At the same time, everyone in the strategy room—including me—leaped to their feet.

“Fuck!”

“Find the transmitter’s coordinates! Now!”

“Sound the alarm! Dispatch the nearest search team to those coordinates immediately!”

“Teams P3 and P4 are moving within thirty-five kilometers!”

“Get the orders out! Hurry! And request support from the Skeleton King, too!”

Wheeeee!

The alarm blared through the speakers, piercing the deep darkness.

I threw myself out the open window and shot high into the air. When I spotted a flash of light far in the distance, I drew up my internal energy.

Bang!

The wind rushing past my whole body seemed to carry the metallic scent of blood.

* * *

Whoosh. Boom!

With a heavy whoosh of displaced air, bone and flesh burst apart.

The headless corpse dropped to its knees, and furious shouts erupted from every direction.

“No! Haruka!”

“You bastard! How dare you!”

Shing, shing, shing!

A blast of blades sliced through the darkness. They sliced through sand thrown up by the force of their swings, certain they could hack apart the enemy who had killed their precious comrade.

Or so they thought.

Until the sand surging up from beneath their feet became enormous spikes that pierced their bodies.

Thud! Crunch!

“Ghk.”

“Guh…!”

With their final gasps, dark red blood soaked the sand.

Hundreds dwindled to a hundred, and a hundred to dozens. It took only a little over ten minutes.

The people who had watched it all with their own eyes trembled with a fear that sank to the marrow. S-rank Hunter Yamamoto Genji was no exception.

*This… This can’t be real.*

He might have been called Swift No-Show or an S-rank janitor, but Yamamoto was still a veteran Hunter who’d fought in his fair share of battles.

Even for him, this was the most horrific and one-sided fight he’d ever seen.

Overwhelming power. Destruction. Terror.

There was a gulf between them that he couldn’t describe with any word he knew.

He was too terrified to run. Too terrified even to swing the sword he’d drawn.

“What are you… What the hell are you?”

Slice!

Instead of answering, an unseen gust of wind cut through another life.

The tank who’d charged with a scream had been split in two along with his massive tower shield. Blood, vivid even in the dark, sprayed through the air.

Splaash. Thud-thud!

The dead of night. The dim light of the moon.

And one figure standing tall amid the blood falling like a sudden downpour.

Swish.

The long hem of a robe brushed over blood-soaked grains of sand as its wearer turned. At that moment, Yamamoto Genji abruptly realized who the enemy was—the one who’d attacked them by surprise.

“The Prophet…!”

Beneath the low-drawn hood, the figure’s lips curled gently upward.

In the next instant, The Prophet’s outstretched hands raked through the air like claws.

Whooosh! Slice!

Had space itself warped? Or had that just been an illusion?

Yamamoto Genji stared blankly around him. Corpses were scattered everywhere: faces gone, holes punched through the centers of chests, limbs cut off.

Before he knew it, he was the only one still alive.

At least, for the moment.

*I’m going to die. There’s no doubt.*

The one thing equal for everyone: the fear of death.

Step.

Yamamoto Genji took a step backward without realizing it. He didn’t even notice the sword hilt slipping in his sweaty grasp.

No. He didn’t care.

If only he could live. If only he could make it back to Japan alive.

But the next moment, someone’s unfamiliar voice pierced his ear.

“Where are you in such a hurry to go, foolish servant?”

“……!”

Just as Yamamoto Genji froze like a statue—

“Over there!”

“Someone’s there!”

“Get into formation!”

Vrooom.

The roar of transport vehicle engines and people’s shouts rang out all around them.
## Chapter artifact 798

# Chapter 798

I knew. No matter how extraordinary your abilities were, you couldn’t prevent every tragedy in the world.

And yet every second felt like an hour because the people who were collapsing in pools of blood at this very moment were suffering because of me.

I was the one who’d called them to this distant desert in a foreign land. I was the one who’d led them to their deaths.

The moment I took on the title of Alliance Leader, I was bound to suffer until this war was over.

I’d been given the fate of fighting harder and leading from the front more than anyone else.

*Whoosh!*

I shot forward, cutting through the fierce wind.

My lightness skill had long since surpassed the realm of Treading Snow Without a Trace. It left no footprints even on fine sand, and each step erased dozens of meters.

*Faster. Faster. Just a little faster.*

I hadn’t looked back for even a second, but I knew I’d come so far that the headquarters, which had stood like a fortress in the desert, was no longer visible.

I was also getting closer and closer to the faint lights I’d spotted when I’d leapt into the sky.

*But why…?*

Why was it so quiet?

At the thought I couldn’t bring myself to finish, my heart sank. I gritted my teeth and stamped down with all my strength.

*Rumble.*

The internal energy flowing through my toes shook the ground. For an instant, my muscles had compressed like a spring; now they recoiled, unleashing explosive force.

*Boom!*

My body shot forward like a cannonball with a heavy boom of displaced air. At the same time, faint sounds reached my ears on the wind.

—…What the hell… that bastard…

—Hans! Hans!

—Fled… survivor… contact headquarters…

The broken-off voices of people, scattered among the sound of vehicle engines.

There were plenty of people nearby, and I could hear plenty of noise as I drew closer. The damage clearly wasn’t too severe.

“Ah.”

Only then did I let out a sigh of relief and pick up the pace.

A moment later, the instant I saw the scene spread out before me, I understood.

All the signs of life and noise I’d sensed earlier belonged to people who had already arrived here ahead of me.

“……!”

I froze like a statue, staring at hundreds of bodies, dried out as tightly as mummies.

The people’s eyes turned toward me. Their murmuring felt as distant as an echo.

Only one word filled my mind.

*The Prophet.*

No doubt about it.

He’d been here.

And maybe…

*He’s still nearby. He has to be.*

I’d have to put off mourning the dead.

If we didn’t catch him here today, we’d have to pay a price tens, even hundreds of times greater.

*Where are you?*

My heart was boiling, but my mind was as cold as ice. My senses were sharper than ever as I spread my Qi Sense.

*Fwoosh.*

As invisible energy swept across the sand, I launched myself forward.

*Whooosh!*

Beyond the sand surging up like a wave, a familiar face flashed into view.

Amid the people who were clearly reinforcements, the Skeleton King was shouting something with an urgent expression. But already, as I streaked across the desert like a beam of light, every one of my senses was fixed on a single presence.

The Prophet.

Today, right here, I had to pull out the last root of a diseased tree.

* * *

If everything in the world had gone the way I wanted, I probably wouldn’t be here now. My father wouldn’t have died, and my mother wouldn’t have gotten sick.

If that had happened, I… I don’t know.

My school grades were a complete disaster, and my only strong point was that I was healthy.

Yeah, fuck.

It was all just a pointless wish and a load of bullshit, something that was never going to happen anyway.

Things in this world had never gone the way I wanted. This time was no different.

“Hell of a morning, isn’t it, Jin?”

I dropped down beside Magic Johnson, who greeted me with an exhausted face.

Neither of us asked the other how it had gone. We already knew that six hours of searching had come to nothing.

Even so, I spoke up, hoping against hope.

“Johnson.”

“I’m sorry.”

“……”

“We searched every inch of a 700-kilometer radius. We practically threatened Syria and Iraq into cooperating, too. But, damn it…”

The Prophet was gone.

No—he’d vanished.

As if he’d never existed in this world to begin with.

No wonder the elite Hunters who’d joined the search right after me all looked as if they’d seen a ghost.

“We were so close. Where the hell did he run off to?”

The reinforcements had moved quickly.

The reinforcements arrived less than fifteen minutes after J1—a team of roughly two hundred Japanese Hunters—reported an engagement.

The problem was that The Prophet, who’d left the battlefield just before they arrived, couldn’t be found anywhere.

“Jin. As far as I know, there’s only one way to explain this.”

Our eyes met. I murmured quietly,

“Magic.”

“Right. The Prophet is a mage. A mage so skilled he’d deserve to be called a Grand Mage.”

Neither Magic Johnson’s magic nor the Skeleton King’s undead army had found a trace of him. And neither had I.

That left only one possibility.

Magic.

When people encountered something they couldn’t understand, they often called it a miracle or something like magic.

In The Prophet’s case, it was definitely the latter.

He couldn’t really be someone chosen by God, like the brainwashed fanatics who believed in him claimed.

*A mage, huh.*

Huginn’s words suddenly came back to me.

His account that The Prophet seemed like a long-range Hunter.

I’d only half believed him, but this time the scales had to tip in that direction.

The Prophet was probably a mage—and a mage skilled enough to disappear without Magic Johnson noticing.

Or…

*One of his subordinates could be a mage at that level.*

If that was true, it’d be the worst of the worst. Fortunately, Magic Johnson immediately shook his head when he heard my thought.

“That’s not it.”

“I hope you’re right, but there’s still a chance…”

“The Prophet was definitely alone.”

“What?”

The certainty in Magic Johnson’s voice went beyond a simple guess. I asked again instinctively, and the next thing he said explained why.

“There’s a survivor, Jin.”

“……!”

“The only survivor from J1. He woke up not long before you arrived.”

The only survivor.

I couldn’t just sit there and listen after hearing those words. I sprang to my feet and asked Magic Johnson,

“Where is he now?”

* * *

The survivor lay in bed, hooked up to all kinds of medical equipment.

Team Leader Choi and the Skeleton King had been talking beside the bed with serious expressions. They opened their mouths as if to say something when they saw me, but then closed them again.

They must’ve been able to tell from my face alone that the search, which had continued until dawn, had come to nothing.

“That him?”

The Skeleton King immediately understood what I meant and nodded.

“Yeah. The only human left alive among those who were there.”

“Then when I first got to the scene…”

“By then, every last one of them was dead. Not a single wounded person left. That human was in critical condition, too, but he got lucky. You came in, didn’t even listen properly, and left again right away.”

Only then did the frantic scene from earlier return to my mind.

The word *survivor* mixed in among the voices of the people as I’d first headed for the scene—and the Skeleton King trying to say something to me as I left.

“You left before I could say a word. I was about to go after you, but I stopped myself. Something else could’ve happened with me away from here, too.”

The Skeleton King had made the right call. Maybe he’d read the situation even more calmly than I had.

Seeing me bite my lip in silence, Team Leader Choi spoke.

“You both made the right decisions. What matters now is that we have a survivor.”

The loss of well over a hundred lives was tragic, but having someone survive was a miracle.

For him, after surviving that horrific scene. And for all of us.

“He woke up a little while ago—six hours after we found him. According to the healer in charge, he’s had enough potions and is entering the final stage of recovery, so he should be fine.”

I stared at the survivor, who was gazing into space with his mouth hanging open.

He didn’t look all that fine for one thing, and his face seemed somehow familiar.

On top of that, there was the fullness of energy inside him, which I could sense without even needing to check his pulse.

*Wait. Could this guy be…?*

When I realized, I turned my head. Team Leader Choi nodded as if he’d read my mind.

Then a quiet Sound Transmission reached only my ears.

—He’s the person you’re thinking of, Mr. Jin Taekyung. The sole survivor of J1 is Japan’s S-rank Hunter, Yamamoto Genji.

—……!

—It was a close call. From what we can piece together, the reinforcements were just about to arrive. The Prophet must have worried he’d get held up, so he couldn’t make sure the job was done.

The five hundred Hunters who’d arrived as reinforcements had been lucky.

If The Prophet had been a little stupider, or more confident in his own strength, they wouldn’t have escaped death either.

But The Prophet was clever and cautious. He knew the longer he stayed in one place, the greater the threat he’d face.

That was bad news for humanity, but good luck for the people who’d survived.

In that sense, the survivor before me—Yamamoto Genji, staring into space with unfocused eyes—had been blessed with exceptional luck.

Of course, having gone through something similar myself, I didn’t think of it that way.

*Damn it.*

I hated Yamamoto Genji.

If I had to define how I felt about him, it went beyond dislike. It was closer to loathing.

Back when so many people were risking their lives to stop Leviathan, he’d shown up late with the most ridiculous excuse.

The only reason I’d gone out of my way to bring someone like him into the World Hunter Federation was simple: he was an S-rank Hunter.

I’d believed that even if he was a useless bastard, he’d manage to pull his weight at least once.

But no matter what I’d thought of him until now, I had no right to curse Yamamoto Genji.

I had no intention of asking him why he was the only one who’d made it back alive when everyone else was dead.

I was the one who’d sent him—and all of them—into a deathtrap.

*Tap.*

I took Yamamoto Genji’s wrist and sent my internal energy into him.

My Scorching Yang Qi, warm to the touch, flowed through his pulse and into his body. His erratic heartbeat steadied, and a flush of warmth spread across his pale face.

“Yamamoto.”

I spoke his name quietly, and he responded. His cracked lips moved.

“……A-ah.”

I watched him quietly, his mouth opening and closing like he’d forgotten how to speak, as I continued to channel internal energy into him.

How much time passed like that? At last, his eyes came back into focus. Yamamoto Genji looked at me and finally spoke.

“Jo…”

“Jo?”

“Chōsenjin?”[^1]

Wait, this fucking bastard.

[^1]: *Chōsenjin* is a Japanese term for Koreans, used here as an ethnic slur.
## Chapter artifact 799

# Chapter 799

If the N-word is the button that sets Black people off, then *Chōsenjin* is the Korean-specific special edition.[^1]

It’s bad enough when Korean weebs who’ve overdosed on Japanophilia start throwing around *Chōsenjin*. But you really see the full horror of it when you hear it straight from a Japanese guy.

Like right now.

“Chōsenjin?”

The moment that magic word pierced my ears—

The will of Hongik Ingan, which had begun with Grandfather Dangun in the distant past, and the vital essence of Korea’s eight provinces surged up from deep within me.

And if you compressed that long-winded sentence into four syllables, you’d get something completely unrelated: Scorching Yang Qi.

Honestly, I was just spouting whatever came to mind because I was pissed off.

*Whoosh!*

“Uh. Uh-oh…”

“Please don’t, Mr. Jin!”

The sudden burst of heat made the Skeleton King swallow saliva he didn’t even have, while Team Leader Choi launched himself at me like a football player and grabbed hold.

“You can’t hit him yet! He’s a patient!”

“Right. Team Leader Choi is right.”

“Yes, yes. So…”

“But so what?”

“Huh?”

“Let go. That bastard’s pissing me off.”

I pried Team Leader Choi’s arms from around my waist and muttered,

“Ahn Jung-geun. Yun Bong-gil. Yu Gwan-sun. Ahn Chang-ho. Kim Won-bong…”

“Gasp.”

“Mutaguchi Renya. Little Boy. Fat Man…”

“Help! I can’t hold him back by myself!”

At Team Leader Choi’s cry for backup, the Skeleton King answered calmly.

“Even the two of us couldn’t stop him.”

“We need to hear his testimony!”

“We do. But who’s going to take responsibility for my beautiful skull if it gets smashed to pieces trying to stop him?”

“Johnson! Mr. Johnson! Help!”

*Bang!*

“Who dares bully my Choi—Oh.”

Magic Johnson burst through the door like a knight in shining armor, then blinked.

“What on earth is going on?”

“Hmm. A wicked human is trying to kill a monkey human.”

“What the fuck? Why?”

“Because the monkey human called the wicked human *Chōsenjin*.”

“Chōsenjin?”

Magic Johnson still looked puzzled, not quite understanding what it meant. The Skeleton King helpfully elaborated.

“As far as I know, it means about the same thing as ‘nigger.’”

“Motherfucking Japs! You goddamn sons of the beach! Jin! Kill that bastard right now!”

Even the hulking Grand Mage, well over two meters tall, had started raging. Team Leader Choi muttered so quietly I could barely hear him,

“Fuck, I really can’t do this anymore…”

“Oh.”

When I’d first met him, I’d thought, *What kind of Young Master is this?* But now, even the occasional swear that slipped out of him sounded native.

Was this how a master felt when he saw his Disciple grow?

I looked at Team Leader Choi with pride.

“You’ve come a long way.”

“Quit screwing around and finish what you were doing.”

“I’m really going to hit him, you know?”

“You were going to do it even if I stopped you, so why ask? Just make it one hit. And go easy.”

“Okay.”

With that settled, I turned around. Yamamoto Genji had become the picture of politeness.

“I’m sorry. I was out of my mind earlier.”

“Yeah. I’m sorry in advance, too.”

“Mr. Jin…”

“No, just call me *Chōsenjin*. That’ll make me feel better.”

“Jin-sama!”

After a three-stage transformation in how he addressed me that would’ve put Frieza to shame, Yamamoto Genji sprang to his feet, dropped to his knees, and pressed his forehead to the floor.

“I sincerely apologize!”

“……Did you go to a dogeza academy or something?”

It was a perfect, textbook dogeza.

At this point, I was starting to wonder whether dogeza was part of the Japanese S-rank Hunter certification test.

I sighed and shook my head, then stared silently at the back of Yamamoto Genji’s head.

Damn it.

Whatever else, he’d come all the way to the Middle East on my orders.

He’d hesitated for a while even after the order to withdraw, and in the end he’d lost every member of his team. But if you looked at it closely, I was more or less responsible for all of it as the one in command.

If Yamamoto Genji was an incompetent defeated general, then I was a pathetic commander who’d entrusted the lives of hundreds of people to a man like that.

“Get up.”

“……”

“I said, get up.”

“Y-yes.”

Yamamoto Genji cautiously sat back on his heels.

His body was completely free of injuries, thanks to the potion shower he’d had. And judging by his wide-open eyes, his mind seemed to be working properly again, too.

“Tell me everything that happened. From beginning to end. Don’t leave anything out.”

Yamamoto Genji hesitated, licked his parched lips, and finally began.

“We were traveling in unmanned transport vehicles when he appeared.”

“The Prophet?”

“……Yes.”

At the word *The Prophet*, Yamamoto Genji shuddered and swallowed.

“At some point, the vehicles suddenly stopped, and an unknown force made my whole body go cold.”

He was a coward and a fool, but he was still an S-rank Hunter. He must’ve instinctively sensed that something was wrong.

But…

“The vehicles stopped? On their own?”

“Y-yes.”

Magic Johnson met my gaze and spoke.

“It was magic. He must have used mana interference to shut down the Magic Gems powering the unmanned transport vehicles.”

“What are the odds it was an artifact?”

“That’s certainly possible. But I understand J1 had ten vehicles assigned to them. Is that right?”

Yamamoto Genji answered.

“That’s right. They all stopped at once.”

“Magic used through an artifact has clear limitations. He’s definitely a mage.”

“R-right. That’s right.”

Yamamoto Genji nodded spasmodically, like someone being chased, and continued.

“I saw it clearly. The flash of light, the blood, people falling at a single gesture… I’d never seen anything like it. Everyone around me died in the blink of an eye. It was definitely magic.”

As if he were reliving the terror of that moment, his hands and feet began to tremble.

I stared at Yamamoto Genji for a while, then suddenly asked,

“What about you?”

“Huh?”

“How did you survive?”

“Th-that…”

His pupils, which had just managed to refocus, wavered.

He reflexively avoided my gaze. There was no grief over the loss of his comrades in him, no anger at himself.

Fear.

The only things Yamamoto Genji felt now were fear of The Prophet and relief at having survived.

“You ran. No—did you try to run and fail?”

“……!”

You son of a bitch.

When he flinched as if I’d hit the mark, something hot surged up inside me.

If someone hadn’t grabbed my shoulder, I would’ve punched that cowardly face of his, testimony or no testimony.

*Damn it.*

I bit down on my lip, trying to swallow the bitterness and anger.

I silently glared at Yamamoto Genji, his head bowed. A long time passed before I spoke again.

“What happened after that?”

The man had his head lowered, his eyes darting around. He cautiously began to speak.

“He heard the reinforcements arriving and left.”

“Was the situation so urgent that he had to leave you behind, an S-rank Hunter? The Prophet must have known you’d be a problem if he let you live.”

“Th-that…”

Yamamoto Genji hesitated for a moment at Team Leader Choi’s sharp question, then answered,

“He must have had another reason.”

“Another reason…?”

“He sucked everything out of my teammates who’d died before me.”

“What?”

Sucked everything out of them?

As the rest of us stared at him, unable to make sense of his words, Yamamoto Genji hurriedly continued.

“I-I swear there isn’t a single lie in what I’m saying. He sucked up the pools of blood all around us, too. He pulled something like a pale mist out of the dead people’s bodies and swallowed it. After that, the corpses dried up like mummies…”

The shock hit me like a blow to the back of the head. The words that followed came through only faintly.

And I wasn’t the only one stunned.

“No. This… That isn’t magic.”

Magic Johnson muttered as if he were groaning and rubbed his forehead. Under the lights, his forehead had grown damp with cold sweat.

“Damn it. What the hell was it? As far as I know, there’s no magic permitted to humans that could do something that horrifying…”

His voice, which had been surging out with his emotions, trembled.

Magic Johnson stopped speaking and stood frozen like a statue. Then he slowly turned his head and looked somewhere.

No—all of us did.

And at the end of our gazes stood one being.

*The Skeleton King.*

My friend. A comrade I could trust with my back.

But the reason we’d instinctively looked at him was that the answer to The Prophet lay in his very existence.

Someone who used magic not permitted to humans.

A powerful being, capable of taking out a Grand Mage single-handedly, whose strength had never once been revealed to the world.

Another secret Michael Silbert had hidden even from Huginn, his right-hand man.

*A monster.*

That was right.

That was what The Prophet really was.

“He left behind a message.”

The monster called The Prophet had been dangling bait in front of me.

* * *

On a tall hill rising like a mound, an old man in a turban watched a hazy cloud of sand billow up not far away.

More precisely, he watched the dozens of vehicles visible through the sand.

“Shall we eliminate them?”

At his subordinate’s voice, which came from empty air, the old man asked calmly,

“How many are there?”

“We estimate more than five hundred.”

“Any S-rank Hunters among them?”

“Not that we’ve been able to determine. Even if there are, I could wipe them all out if I went in.”

The old man stroked his coarse beard. He fell silent in thought, and only after a short while did he speak.

“Leave them be.”

“But the distance…”

“Hamid, did you not hear me?”

After a moment’s silence at the sudden call, the subordinate answered,

“I’m sorry, Amir. I was out of line.”

“Restrain your impatience and wait for the time soon to come. Did The Prophet not say as much? Everything will unfold according to his will.”

The old man reached out and felt around in the air. Something invisible was protecting them from the infidels.

That was why even satellites in orbit couldn’t detect them—and why the infidels couldn’t find them despite drawing within a few kilometers.

No, the infidels wouldn’t find them even if they came right up to them.

Unless they lifted this veil and went out on their own, no one could see or sense them. And if that moment came, it would be the last moment their intruders spent alive.

This mysterious power could only be thought of as divine protection.

Their god had sent The Prophet down to earth in his place, and The Prophet would lead them to the promised land.

They would punish the wicked infidels and set God’s will straight across every land and sea.

“Do not be impatient. As long as The Prophet is with us, we will be victorious in this great holy war.”

“But where is The Prophet now…?”

“He will come of his own accord soon. Do not doubt it. With the net he has laid, he will gather up every last one of those infidels and send them to God.”

“……!”

“Inshallah.”

Feeling his reverence swell, the old man murmured it once more.

Inshallah.

God willing.

[^1]: *Chōsenjin* is a Japanese term for Koreans, used here as an ethnic slur.

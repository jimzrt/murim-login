# Checkpoint Review — 1060–1064

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

# Chapters 1060–1064

## Plot

The unidentified Great Sir reunites with Ma Junggeol and Taekyung. Hyeoncheon explains that the Great Sir sheltered and treated the Kongtong survivors after Dunhuang, then helped them return to Gansu with the Seven Masters of Baekma Bang and thousands of horse-caravan riders. Taekyung’s Qi Sense identifies the Great Sir as Level 119, but his displayed name changes repeatedly—Madman, Gaettong, and others—and his true identity remains unknown. Taekyung concludes he is genuinely insane, not a Dark Heaven spy, and urges accepting him as an ally.

After the Gansu victory, Taekyung completes the Path of Blood Quest and accepts a new chain Quest. News of the victory spreads, with casualty reports exaggerated; the Emperor calls for the government and Murim to unite against Dark Heaven. A bloodied messenger report reveals that Dark Heaven has occupied Kunlun. The Kunlun Sect and its allies have retreated to Qinghai Lake with about a thousand casualties, facing an immense enemy force. Unable to log out while the linked “To Qinghai” Quest remains incomplete, Taekyung and his companions set out for Qinghai, guided by the Great Sir.

Meanwhile, at the Taiqing Hall in Kunlun, the Blood Lord argues with the Grand Mage, boasts of his achievement, and reveals “Kunlun” carved into his throne.

## Continuity

- The Great Sir sheltered the Kongtong survivors after Dunhuang and helped them return to Gansu. He is Level 119, but his identity and changing names remain unexplained; Taekyung believes he is not a Dark Heaven spy.
- The Gansu battle is won. The Path of Blood Quest is complete; Taekyung’s new chain Quest is underway.
- The Emperor has called for the government and Murim to unite against Dark Heaven. Dark Heaven occupies Kunlun; the Kunlun Sect and allied forces retreated to Qinghai Lake with about a thousand casualties. Qinghai and Gansu remain vulnerable.
- Taekyung cannot log out while “To Qinghai” is incomplete. He and his companions are entering Qinghai from the Qilian Mountains with the Great Sir as guide.
- The Blood Lord claims to have retrieved an important item; what it is and the significance of his achievement remain unknown.

## Translation Decisions

- Render 미친놈 as “Madman” when the Great Sir adopts it as a name; retain “Gaettong” for 개똥이.
- Render 말똥 as “Malttong,” glossed as “Horse Poop.”
- Render 태청전 as “Taiqing Hall.”
- Render 황태제 as “Imperial Younger Brother,” the Emperor’s appointed heir apparent.

## Durable state

{
  "active_continuity": [
    "The Emperor has called for the government and Murim to unite against Dark Heaven.",
    "Dark Heaven has occupied Kunlun; the Kunlun Sect and allied forces retreated to Qinghai Lake, with about a thousand killed or wounded.",
    "The messenger report describes Dark Heaven's force as countless, evoking the Hundred Thousand Demonic Disciples.",
    "Qinghai and Gansu remain vulnerable to Dark Heaven.",
    "Jin Taekyung cannot log out while the linked Quest “To Qinghai” is incomplete.",
    "Jin and his companions are entering Qinghai from the Qilian Mountains, guided by Great Sir."
  ],
  "continuity_sources": [
    1063,
    1064
  ],
  "open_questions": [
    "Why does the System prevent Jin from logging out beyond the incomplete linked Quest?"
  ],
  "safe_through": 1064,
  "temporary_decisions": [],
  "version": 1
}

## Reading copies

## Chapter artifact 1060

# Chapter 1060

Great Sir.

An unidentified Supreme Peak master whose name and identity were unknown.

My first impression of the extraordinary man who, about a dozen years ago, subdued Ningxia Province—then little better than a lawless wasteland—in a single stroke, only to defy everyone’s expectations and retire into a life of idleness, was this:

*He looks like a damn beggar.*

That wasn’t just a figure of speech. He really did.

His hair and beard were long enough to cover his face and reach his waist, and so matted they looked like one solid mass.

His clothes were torn and stained in so many places that “rags” would have been the more accurate description. And the stench coming off his grime-caked body was so revolutionary it was practically an evolution of its own.

A beggar among beggars.

A wretch. A king of beggars.

Even Gung Gibang, the Beggars’ Sect’s Successor Beggar and a bona fide minor chief among its hundred thousand beggars, would take one look at this man and cry, “You beg like shit!” I could guarantee he’d cut the rope tied around his waist.

And yet…

“So this really is the beggar everyone’s heard about—or, I mean, the Great Sir?”

“Hard as it is to believe, it’s all true.”

The Bow Saint answered in a nasal voice. She was already standing well away, pinching her nose shut.

That was when—

“Greeeaat Siiiir! Why did you take so long to come?!”

With a plaintive wail, Ma Junggeol, eldest of the Seven Masters of Baekma Bang, came sprinting from far off and threw his arms around the strange man.

Or, more accurately, he tried to hug him, then recoiled as if burned and doubled over like a shrimp.

“Ugh. Blegh.”

“……”

Yeah, I understood.

I’d spent enough time rolling around in Gates to have built up some resistance, which was the only reason I could stand there. Even now, the stench was bad enough to make me wonder if it could really be coming from a human body.

Of course, even I was reaching my limit.

“Wait, just—give me a little space. Why are you doing this when we’ve only just met?”

My initial shock didn’t last long.

I desperately breathed through my mouth to block out as much of the smell as possible, then tried to push the man away. But his legs were planted deep in the ground like thousand-pound boulders. He didn’t budge.

*Looking at that, he really does seem like a Great Sir…*

Even though I’d held back, my strength was so far beyond ordinary limits that even a decent Peak master would have struggled to withstand it.

My head understood. My heart didn’t.

It was like hearing that Kim, the homeless guy who ran the second exit at Seoul Station, had turned out to be the chairman of a major corporation.

*But, seriously, why are you crying so hard?*

As I stood there, unsure what to do and darting my eyes around, the strange man—no, the Great Sir—who’d been wailing in my arms finally spoke in a congested voice.

“Ahem. Ahem. Sorry about that. It was such a moving moment that the tears came before I knew it.”

I looked down at the front of my chest, soaked and sticky, and corrected him.

“I don’t think tears were the only thing that came out.”

“My nose was running, too.”

I could understand tears and a runny nose, but why he had to let them both out while clinging to me was beyond me. Still, I nodded, summoning the bare minimum of patience and respect for my elder.

“Uh, sure. So you’re feeling better now?”

“Thanks to you, I’ve calmed down a little. Do you mind if I blow my nose?”

“You really do everything, don’t you?”

“Hmm? What was that?”

“Nothing. Go ahead.”

“Thank you.”

The Great Sir thanked me in a guileless voice, then blew his nose with a sound that seemed to clear out his entire head.

*Phaaaang!*

On my clothes.

“Whew, that feels much better… Why are you making that face?”

“……”

Ah.

I was really about to snap.

* * *

To sum it up, even with half my sanity gone, I somehow managed not to punch the Great Sir in the head.

Starting a fight in the middle of a battlefield that hadn’t even been fully secured yet would have been unwise. More than that, Perfected Being Hyeoncheon had quickly grasped what was happening and stepped in.

“Here you are, Great Sir.”

It was a sight that would have surprised anyone. No—astonished them.

Who was Perfected Being Hyeoncheon?

The Sect Leader of the Kongtong Sect, one of the Nine Sects and One Gang; a hero of the Great Faction War; and a Supreme Peak master representing Gansu Province.

If we were talking about the Marine Corps, he’d be a legendary first-wave veteran who’d taken part in the Incheon Landing Operation. He had the seniority to stand in the middle of the world and shout, “Everyone below me and above you, fall in!”

And yet this man, whose standing in the Murim and martial prowess both ranked among the highest in the world, was the first to offer a fist-and-palm salute with the utmost respect.

To a strange man who looked worse than even the Beggars’ Sect leader.

It was enough to make Jeok Cheongang, watching from nearby, mutter:

“What the hell does he have on him…?”

For that moment, I had more or less the same thought.

Maybe the filthy-looking fellow had a video file with a title like *Kongtong’s Perfected One H and His Secret Hand Games*.

But there was a reason everyone could understand why Perfected Being Hyeoncheon would show that much respect to a strange man followed by little more than some former mounted bandits.

“This Great Sir was of tremendous help to us.”

To sum up the story, it went like this.

At the time, Perfected Being Hyeoncheon and the Kongtong Sect survivors had been defeated at Dunhuang and had no idea where to go.

They had to flee east to avoid Dark Heaven’s forces gathering like clouds in the west. But now that they felt betrayed by their allies, heading east would have been like walking straight into a tiger’s jaws.

So they chose to go north, toward the grasslands.

“We considered turning south for Qinghai, but we had no idea what Dark Heaven might already have done there. We had no choice but to head for the grasslands, where fewer people lived.”

Though Qinghai lay at the far edge of the Central Plains, it was still watched from every direction.

The grasslands, by contrast, were vast and sparsely populated, which made them better for evading pursuit. If Dark Heaven had reached both places, anyone would have chosen the latter.

“We kept heading north without rest. Even after passing Anxi and entering the grasslands, we couldn’t let our guard down. We considered taking a short break to recover and see what was happening in Gansu, or perhaps crossing the grasslands and going all the way to Shaanxi.”

But for the Kongtong Disciples, already suffering injuries both serious and minor from the fierce battle at Dunhuang, it was an exhausting march.

Even Perfected Being Hyeoncheon, who had to lead them all, had reached his limit from severe internal injuries.

“Still, we couldn’t stop. We had no choice but to keep moving, feeling helpless and miserable. Then, after several days on the road, one night we saw a light flickering in the distance.”

The nights on the grasslands were deep and silent.

For the fugitives crossing that endless expanse, any light in the dark was something to be wary of.

“We crept closer, holding our breath. There was some strange man roasting camel meat. It had been four days since we’d seen food, and we were all half out of our minds.”

Hyuk Mujin had drifted closer at some point and was listening intently. He let out a low, “Ah.”

“Was that the beggar—sorry, the Great Sir?”

Perfected Being Hyeoncheon nodded.

“Indeed. He saw us shivering in the cold and invited us over without hesitation.”

“Now that’s generous. He even offered you food. No wonder you’re grateful, Sect Leader.”

The heartwarming story made the air around us feel a little warmer. Then Perfected Being Hyeoncheon spoke again.

“No, we didn’t get any.”

“What?”

“As soon as he saw us, he devoured all the meat before our eyes and told us we could warm ourselves by the fire for a while, then go our separate ways.”

“……!”

“……!”

What the hell?

Everyone’s eyes turned toward the Great Sir, mine included. He bashfully smoothed his wild, tangled hair.

“I only had enough for myself at the time…”

The air turned cold again. Perfected Being Hyeoncheon continued.

“Regardless, the Great Sir helped us greatly. He gave me and all the Disciples of our sect a place to hide for a while and treated the wounded.”

It was said that a master could recognize a master.

At first, Perfected Being Hyeoncheon had been wary of the unidentified Supreme Peak master, but he hadn’t had any other real options. Before long, he’d come to feel the man’s sincere goodwill.

“While we were there, we also had an unexpected visitor.”

“An unexpected visitor?”

“At first, we thought the enemy had found our hideout and come to attack. But that wasn’t it. It turned out some men called the Seven Masters of White Bones had come to escort the Great Sir.”

“The Seven Masters of Baekma Bang,” Ma Junggeol interjected through gritted teeth.

“Oh, I must have mixed that up. The Black-Horse Seven?”

“I said the Seven Masters of Baekma Bang! Honestly, this is driving me insa—”

*Bap!*

I smacked Ma Junggeol on the back of the head without question or explanation and shut him up. Then I looked around.

Quite a few mounted figures were riding among the battlefield, their horses snorting roughly.

They wore relatively light leather armor and carried weapons like spears and crescent-bladed polearms. Now I could finally be sure who they were.

“Then could those people be…?”

“You’re thinking of the right people. They’re the horse caravans of Ningxia Province.”

Ma Junggeol, grimacing as he rubbed the back of his head, spoke in a tiny voice.

“More precisely, the horse caravans centered around Baekma Bang… Gah!”

He clamped his mouth shut when our eyes met. But this time, instead of hitting him, I patted him on the shoulder.

The Seven Masters of Baekma Bang had promised a few days ago that they would bring the Great Sir back. They’d returned with the horse caravans under their command, and thanks to them, we’d been able to deal a decisive, fatal blow to the enemies who were on the verge of collapse.

*So that’s how this worked out.*

I’d more or less forgotten they existed.

Or perhaps it would be more accurate to say I hadn’t expected much from them.

You always had to prepare for the worst in a battle, and the horse caravans, made up of former mounted bandits, weren’t exactly people you could trust.

But they had kept the promise they made to me, even if they were a little later than they’d planned. And with the Great Sir’s kindness, Perfected Being Hyeoncheon and the Kongtong Disciples had recovered from their injuries and returned to Gansu alongside thousands of horse-caravan riders.

Still, there was one question I couldn’t answer.

*So who the hell is that guy, really?*

I looked at the man they called the Great Sir, my eyes full of questions.

A moment ago, he’d clung to me and sobbed as if we were reuniting with a long-lost family. Now he was yawning widely just because the story had gotten a little long. As expected, he seemed far from sane.

Just as Ma Junggeol and his sworn brothers had told me.

And I quietly, secretly reached out toward the Great Sir.

A hand of detection, invisible and permitted only to me.

*Skill: Activate Qi Sense.*

*Whooooosh.*

The blue circle spread outward from me, at last reaching the Great Sir.
## Chapter artifact 1061

# Chapter 1061

Jin Taekyung’s Qi Sense could be divided into two kinds.

One was the Qi Sense he had honed as a martial artist, a means of survival.

The other was Qi Sense granted by the System as an individual Skill.

The first manifested as naturally as breathing, even in everyday life. The second worked by activating the System with a clear intention and goal.

*Back when I was weak, I had no choice but to rely heavily on the Qi Sense Skill.*

Though he’d used it far less often since his martial arts had reached a certain level, the Qi Sense Skill remained incredibly useful.

Especially when he wanted to get a closer look at someone whose identity was unknown, like right now.

*Skill: Activate Qi Sense.*

The moment Jin Taekyung silently recited the command, the blue circle of [Qi Sense], which had reached nine stars, shot outward.

*Shwaaash.*

The ability he’d been given made no sound and had no visible form.

There was only a faint ripple, perceptible to the tiny handful of masters who had reached the highest realms.

And it offered another way to determine the identity of the strange man called Great Sir.

*If the Skill succeeds, I’ll learn exactly who he is. And even if it fails, I won’t lose anything.*

Of course, the Qi Sense Skill wasn’t all-powerful.

Masters beyond its limits might have their Levels displayed as question marks. Some could even sense the ripple that accompanied its activation and immediately deflect it.

In fact, Jeok Cheongang had once controlled his energy during their first meeting, making his Level appear absurdly low.

But Jin Taekyung was more concerned with how this Supreme Peak master, dressed like a beggar, would react—and what information an already activated Skill would reveal.

*Who the hell are you?*

Jin Taekyung watched the man with a steady gaze.

The wild-haired oddball was scratching his greasy head, acting so unconcerned that Jin Taekyung couldn’t tell whether he knew what was going on or was pretending not to.

He clearly saw the blue circle that would lift the veil of mystery around the man finally reach its target.

At the same time, a familiar alert sounded in his ear.

*Beep-beep!*

A sharp noise announced failure. Jin Taekyung knew what that meant.

*He’s a master. His Level is higher than mine.*

But Jin Taekyung didn’t waver in the slightest.

He’d learned firsthand, more times than he could count, that Level was no absolute measure of strength.

A Level could reliably distinguish the strong from the weak only up to First Rate or, at most, Peak. Masters in realms beyond that were different.

Jin Taekyung, who had once remained at the Peak realm and won one fight after another against enemies dozens of Levels higher, was especially unfazed by Level differences.

But even he was at a loss for words when he saw the next message appear before his eyes.

> **System**
> Skill Qi Sense was half successful!

“……Huh?”

The question slipped from Jin Taekyung’s lips before he knew it.

The message was a little different from the failure alert he’d heard moments ago, and he stared at it, blinking.

A success was a success, and a failure was a failure. What did it mean to be half successful?

*Wait. Now that I think about it, that failure alert did sound kind of strange…*

Before he could finish turning over the question in his mind, the oddball abruptly whipped his head around, as if he’d finally noticed something was off, and spoke to Jin Taekyung.

“Huh? I thought some strange wind just blew over from your side. Did you feel it, too?”

But Jin Taekyung didn’t answer.

No, it was more accurate to say he couldn’t answer.

Ever since he’d gained the ability to use the System, he’d never seen anything as bizarre as what he was staring at now.

> **System**
> **Lv. 119 ???**

Three question marks.

That was all.

Jin Taekyung rubbed his eyes with his sleeve and blinked hard several times. But where the man’s name should have been, there was nothing but question marks.

*……Has this ever happened before?*

He asked himself, but he already knew the answer.

No.

Not once. Ever.

He’d seen plenty of Levels displayed as question marks. But never a name.

A person always had a name, whether it was an alias they used to hide their identity or the real name someone had given them at birth.

But Great Sir—the oddball before him—didn’t.

The strangeness and bewilderment of this situation left Jin Taekyung with no choice but to ask:

“What the hell are you?”

His short question came out abruptly, full of considerable bewilderment and a hint of suspicion. Everyone around them looked at Great Sir at the same time, as if on cue.

Jin Taekyung’s tone had been downright rude. But even Perfected Being Hyeoncheon and the Kongtong Disciples, who owed Great Sir a great debt, forgot to call him out on it.

After spending several days and nights together, none of them had ever learned the identity of their strange benefactor. They all wanted to know at least a little more about him.

The Fire King, the Bow Saint, and the members of the Fire Dragon Pavilion were no different.

A Supreme Peak master who’d been holed up in some remote corner of Ningxia Province for over a decade was intriguing just by virtue of existing.

Under the weight of all those eyes fixed on him, Great Sir calmly asked in return:

“Hm? Were you asking me?”

“Yeah. You.”

“Oh, that’s a very good question.”

Great Sir scratched his grime-streaked neck. His yellowed teeth showed between his long locks as he beamed.

“Come to think of it, we haven’t even introduced ourselves. Let me make a proper introduction. I’m……”

The surroundings had gone deathly quiet.

Hundreds of pairs of eyes fixed on Great Sir’s lips as they slowly parted.

“Cough. My throat’s scratchy from all the dust. Let me start over. I’m……”

His voice slowed again as he cleared his throat. Everyone was about to go mad with curiosity.

Who could he be?

A reclusive master whose name of three syllables had yet to become known?

A master of the previous generation, forgotten by the world long ago?

Or perhaps……a former great fiend who’d once belonged to the Demonic Cult, but had since turned over a new leaf?

As all manner of guesses swelled by the second, Great Sir continued in a solemn voice.

“Uh. So, I’m……”

“You bastard, you’re the biggest piece of shit under heaven!”

Just as Jeok Cheongang, who’d lost half his mind at hearing “I’m” for the third time, rolled his eyes and started forward, Great Sir let out an exclamation like someone who’d had a great realization.

“That’s right. I think that’s exactly it!”

“What kind of dogshit is this? No matter how far the ways of the martial world have fallen, how can you pull something like this…… What?”

Jeok Cheongang stopped in mid-step and asked in confusion. Great Sir clapped his hands and shouted again.

“What you just said—it sounds right! Madman. I think that’s my name!”

“……?”

“……?”

At the same time, a suffocating silence fell.

Without a single exception, they stared at Great Sir, dazed, then looked at one another.

Their eyes exchanged the words no one could say aloud.

*What the hell?*

*Did I hear that wrong?*

*Madman? That’s a person’s name?*

*Does any of this make sense?*

But no amount of exchanging looks could change the reality before them. Jeok Cheongang, seized by an intensity of bewilderment he’d experienced only a handful of times in his long life, turned to the person who’d already put him through it several times.

His one and only Disciple.

“So right now……that damn lunatic just spewed what kind of nonsense?”

But, like his Master, his Disciple was just as incapable of fully understanding or accepting what was happening.

No—if anything, he was even more at a loss.

> **System**
> **Lv. 119 Madman**

“……”

Jin Taekyung stared blankly at the holographic window above Great Sir’s head, which had changed, and thought:

*What the hell is this?*

Well, it had changed. It had definitely changed.

But……

*So what the hell does that mean?*

Could he really say it had changed properly? Or had the System just bugged out?

Just as countless thoughts and regrets streaked through his mind like a meteor shower, someone he’d momentarily forgotten spoke up beside him.

“Good grief, I thought he’d gotten a little better, but here he goes again.”

Everyone turned toward the voice. A middle-aged man with a fearsome face, formerly of the mounted bandits, flinched and spoke.

“Uh, don’t mind him. This is just how he usually is.”

“Usually?”

At Jin Taekyung’s question, Ma Junggeol—the former mounted bandit who’d operated in Ningxia Province, current Chief of Baekma Bang, and eldest of the Seven Masters of Baekma Bang—nodded with a dubious look.

“Well, yes. Didn’t I mention it once before?”

Jin Taekyung vaguely remembered Ma Junggeol saying that Great Sir wasn’t exactly normal.

“No, but still. What the……”

“A few months ago, when I went to the place where Great Sir was staying, do you know what his name was?”

“What?”

“Jeomsuni.”

“……!”

“His name changes every time I visit. He’s even gone by Gaettong—Dog Poop—and Sottong—Cow Poop.”

Just as Jin Taekyung stood frozen, unable to find anything to say, Great Sir suddenly sucked in a sharp breath and shouted.

“Gasp! Gaettong! That’s right! I think it was Gaettong! I’m sure this time! Probably!”

> **System**
> **Lv. 119 Gaettong**

At that moment, Jin Taekyung gave up on thinking.
## Chapter artifact 1062

# Chapter 1062

No matter how smooth a life someone might lead, every person was bound to meet at least one particular kind of madman in their lifetime.

And as someone who’d lived an objectively—no, an extremely—rough and tumultuous life, I didn’t even need to say more.

But I could say this with certainty.

Even I had never met anyone quite so purely insane as that oddball they called Great Sir.

*…At this rate, should I start a whole encyclopedia of madmen?*

I muttered to myself as I watched Great Sir’s back slowly recede into the distance.

Unable to find his true identity even under the name Gaettong, he’d tried Cow Poop and Horse Poop too, completing his trilogy of poop names.

Then he’d immediately tried to change genders and become Jeomsuni, only to receive death threats from Jeok Cheongang and end up dragged away by the horse caravans for containment.

“I swear on everything I have…”

Standing shoulder to shoulder with me, Jeok Cheongang watched Great Sir’s retreating figure, too. His voice was grave as he continued.

“That man is one of two things: either a Dark Heaven spy who’s undergone intense training, or a man who’s completely and utterly insane.”

Anyone who knew the details would have nodded along without thinking. But I answered without the slightest hesitation.

“I doubt he’s a spy.”

“It’s true that he led the horse caravans of Ningxia Province to help our side. But we mustn’t trust him completely. You know that as well as I do, don’t you?”

Of course. I’d been hit in the back enough times to be sick of it.

The Head Elder of the Jin Family of Taiyuan had joined forces with Dark Heaven. Even the Murong Family, one of the Five Great Families, had done the same. It would be stupid to trust some unidentified Supreme Peak master who’d crawled out of who-knows-where.

But…

“There’s no reason we can’t trust him. Not if there’s enough evidence.”

“Evidence?”

At Jeok Cheongang’s question, my lips barely moved.

—System.

A brief Sound Transmission reached his ear. His eyes widened for an instant.

Jeok Cheongang already knew what the unfamiliar word *System* meant in this world, from what I’d told him before. His voice sank low as he spoke.

“So, according to that impressive ability of yours, what did you find?”

“He’s a madman. A complete and utter madman.”

“So he isn’t a spy?”

“Yes. I can’t say that with absolute certainty, though.”

“If you had to put a number on it?”

“Ninety-nine point nine percent. Of course, I mean the odds that that madman—no, Great Sir—isn’t a spy.”

“Don’t call him Great Sir. He’s just a lunatic.”

Jeok Cheongang frowned slightly and clicked his tongue.

“Anyway, you’re not one to trust people easily. If you’re saying this much, then you’re practically certain… So you think he genuinely suffers from madness?”

I hesitated briefly, then nodded.

Even I, who thought I had a pretty good grasp of most of the System, had never encountered anything like this. I couldn’t be a hundred percent sure, but otherwise, there was no explaining why Great Sir’s name kept changing from one moment to the next.

*At least he isn’t lying. No matter what you did, it’d be practically impossible to fool the System.*

So there was only one answer.

Whether he was Gaettong, Sottong, Malttong, or Jeomsuni—

Great Sir firmly believed he was each of those people, and the System reflected that belief without alteration.

Which meant that, in the purest sense of the word, he was insane.

“Great Sir looks so ragged even Myriad-Mile Pursuit, that king of beggars, would weep, but he doesn’t seem old enough to be suffering from infirmities of old age… I can’t even guess where that stray mutt crawled out of.”

Jeok Cheongang had casually demoted the Beggars’ Sect Leader, a man who ruled over the whole world’s Beggars’ Sect, to a mere king of beggars. He frowned, but even he would have found it nearly impossible to work out Great Sir’s identity right then and there.

There were still far too many people hidden away across the vast Nine Provinces and Eight Wastes, the Four Seas and Five Lakes.

Eccentrics living in remote mountain valleys far from the world. Heirs to secret sects who had chosen to let themselves be forgotten.

Or fugitives and killers living quietly, out of sight, somewhere in the world.

Jeok Cheongang himself had shut himself away on Mount Jiuhua until he was nearly sixty, devoting himself solely to martial arts. There was every chance Great Sir belonged to the same sort.

*In fact, ever since the Murim Alliance was newly founded through the Mount Song Resolution, quite a few reclusive masters had joined.*

Of course, unlike Great Sir, they must have gone through proper vetting. The Murim Alliance wasn’t some college club, and this was wartime, with betrayal and intrigue everywhere.

But how should I put it?

A conviction that came to me out of nowhere slipped between my lips as a voice.

“Let’s accept him as one of our own.”

“What?”

“As I said before, Great Sir doesn’t seem to be a spy for Dark Heaven. No—I’m sure he isn’t.”

Jeok Cheongang looked at me with surprise. My voice was firmer than usual.

“Well, now. That’s strange. What makes you trust that suspicious madman so much?”

“That’s…”

Instead of answering, I let the words trail off.

I wasn’t sure, to be honest.

The System didn’t distinguish between friend and foe.

Still, along with my curiosity about Great Sir, I felt a strangely powerful conviction.

The unidentifiable Supreme Peak master wasn’t our enemy. I couldn’t offer a single reason for believing it.

*…Maybe it’s the exhaustion.*

The moment I recognized something I’d briefly forgotten, I suddenly noticed my vision wavering and looked around.

A snowy field covered in countless bodies and blood after half a day of fighting.

People clearing the battlefield, having already forgotten the brief joy of victory. Birds of prey had gathered in a black mass, circling overhead.

The sky, hidden behind dark clouds, was dim. The land beneath it was red all over.

The world caught in my wavering vision felt like a future that would repeat itself forever.

“Did we… really win?”

At my faint, uncertain voice, Jeok Cheongang answered.

“Yes. At least for today.”

But why?

How come?

We’d defeated more enemies than I could count, saved countless lives, and won a great victory that had finally secured Gansu Province.

And yet, even now, with breath still in my lungs—

It didn’t feel like we’d won.

I wasn’t happy at all.

Not even as a clear chime rang in my ears right then.

*Ding, ding, ding.*

> **System**
> Quest conditions have been met.
>
> **Mission:** Eliminate all enemies in the Gansu Province area (**Complete**).
>
> Quest **Path of Blood** successfully completed.
>
> You have acquired a massive amount of EXP and Fame.
>
> A new chain Quest has been created.
>
> Would you like to check the updated information?
>
> Y / N

I suddenly lifted my head.

Beyond the translucent holographic window, the sky remained hidden behind pitch-black clouds. The air that filled my lungs with a deep breath reeked of blood.

When would I finally be free of this sight?

How much more suffering would I have to endure, how many more deaths would I have to witness, before I could escape this horrible cycle?

But as always, I had no choice but to answer.

*Accept.*

It had been a cruel fucking day.

* * *

Crack. Crunch.

Beyond the faintly trembling candlelight, two eyes silently watched a writhing shadow, accompanied by a gruesome sound of flesh tearing.

At first glance, the eyes seemed so deeply sunk that it was impossible to guess what lay behind them. Even so, they held a trace of contempt and disgust—and that look remained even after the tearing sounds stopped.

The shadow’s convulsions slowly subsided. At last, it rose—and immediately showed its displeasure.

“You bitch. What’s with that look?”

It was a rough way to greet someone after such a long time, but the woman paid it little mind.

She had always prided herself on being a rational person, and she knew how difficult it was to expect a mere beast to show the courtesy of a human being.

Of course, that didn’t mean she could speak kindly to it.

“Wipe yourself off. And stop stinking up the place.”

“What? I stink?”

At the woman’s sharp words, the shadow had started to reply—but suddenly let out a quiet laugh.

“Fine. I’ll do as I’m told. You’re in a bad mood as it is. Aren’t you?”

“…What nonsense are you talking about now?”

“Don’t pretend you don’t know when it doesn’t suit you. Don’t. It makes you look pathetic.”

*Swish.*

Cloth slid over smooth muscle and skin.

In the darkness beyond the candlelight, the shadow wiped the blood from its body and tossed out a few words.

“Blazing Flame Divine Dragon Jin Taekyung.”

“……!”

“I heard you nearly failed… So, how was it, you miserable bitch? You mocked me last time, but it wasn’t so easy when you had to face him yourself, was it?”

The Grand Mage silently bit her lip.

She had little room to argue. It was the truth.

When the Grand Mage’s silence showed no sign of ending, the shadow laughed out loud and continued.

“You should’ve been much more careful. I don’t care if you die, but you nearly caused a serious setback to the grand plan.”

The Grand Mage frowned at the continuing taunts and shot back.

“You’re no different.”

“Hardly comparable to what happened then, is it? I caused a bloodbath in the heart of the Central Plains with only a handful of idiots. Even with one eye half-closed, anyone can see this was a different situation.”

*Step.*

The shadow—no, the Blood Lord—chuckled as if to mock her, then stepped into the faint light.

“And on top of that, I had to retrieve an important item.”

After the Shaolin Bloodshed, which had shaken the whole world, he had never appeared again. Now he crossed the spacious room with a jaunty stride.

He sat in the grand chair, which bore the marks of centuries of age and carried an imposing presence of its own. Resting his chin on one hand, he gazed at the Grand Mage.

Like a king on his throne.

“Well. Enough about the past. The important thing is the present and the future. Isn’t that right?”

This time, it was the Grand Mage’s turn to let out a quiet laugh.

She shook her head and stared at the Blood Lord sitting in the grand chair.

“Don’t talk as if you’re somebody. You’re nothing more than a stupid beast—or a monster.”

“A monster, huh? To the people of the Central Plains, aren’t we as bad as each other?”

“No. The only thing we have in common is that we serve that person. None of us can be like you.”

But even at her contemptuous words, the Blood Lord merely shrugged.

“Right. That’s the first thing you’ve said that’s correct.”

“…What?”

The Grand Mage was taken aback by the response, which was nothing like what she’d expected. A smile, deep as blood, spread across the Blood Lord’s lips.

“Of course none of you can be like me. No one, including you, has ever accomplished as much as I have.”

He laughed gleefully and stroked the grand chair.

More precisely, he stroked the two characters carved into part of it in a bold, vigorous hand.

**Kunlun.**

A whirling snowstorm swept past the jagged mountain peaks and crept into the Taiqing Hall, where the two of them faced each other.
## Chapter artifact 1063

# Chapter 1063

People say that a rumor without feet can travel a thousand *li*, while information with wings can reach tens of thousands of *li* away.

And that saying, which the information merchants of Murim held up like a proverb, was no exaggeration.

*Flap!*

On that day, when dark clouds covered the sky and death claimed the land, the sight of dozens of messenger eagles taking flight at the same time was quite a spectacle.

Leaving behind mountains of corpses and pools of blood, the eagles soared high into the sky, beating their great wings as they flew toward their separate destinations.

The snowfield, stained red, dwindled into a tiny drop of blood. The Great Snow Mountain Range, covered in eternal snow, disappeared from view.

The sun and moon traded places, day and night giving way to each other several times. The ocher-colored plateau, seeming to stretch to the ends of the world, vanished beyond the horizon.

And at last, when the dozens of messenger eagles had each completed their journeys, the realm of the Central Plains seethed like lava in a crater.

“Waaaaah!”

“Long live the Great Nation! Long live His Majesty the Emperor!”

“What are you all doing? Come on out! Hurry!”

Though the time and place differed, everyone who heard of the great event in Gansu Province rushed into the streets and cheered.

Some were roused from a sound sleep before dawn by the sudden commotion. Even they, stumbling out past their gates, felt more bewildered than angry.

“Which goddamn fools are making a racket at this hour, when even the hens are fast asleep… Hey, you lot! What the hell are you doing carrying on in front of someone else’s house?”

On an ordinary day, sharp words like those would probably have led to people grabbing each other by the collars first and asking questions later.

But the crowd, cheering and shouting as they chased away the dawn, was too excited to do anything but yell again and again.

“A great victory! A great victory!”

“What are you talking about? That’s not what I asked—wait. A great victory?”

“Good heavens, look at you. You haven’t heard the news yet, have you?”

“You haven’t heard? The rebels from Xinjiang invaded Gansu without knowing their place, and got wiped out to the last man!”

“What? They went after Gansu?”

Only then did those who’d just heard the news widen their eyes. Their shock was the same, no matter their station.

How could it not be?

Just a year ago, Dark Heaven was a name known only to the sharp-eyed and sharp-eared. Now even a country bumpkin in some remote village, living hand to mouth, knew of them.

The rebels of Xinjiang. Fiends from beyond the desert.

Even the Demonic Cult, whose infamy had unleashed a storm of blood half a century ago in what was called the Great Faction War, could not compare to Dark Heaven today.

The Demonic Cult of old had sought to conquer the Murim of the Central Plains. Dark Heaven sought to claim the world itself.

Defying heaven.

The two characters said it all: a band of rebels who would overturn heaven, defy the natural order, and destroy the unified dynasty and peace established after countless turbulent eras.

That was Dark Heaven. And so the people of the Great Nation were still roaming the streets, cheering at that very moment.

“Good heavens, what a joyous occasion. But just how great a victory did you win to get everyone so worked up?”

At someone’s question—one that had chased away the last of his sleep—a proud answer rang out from the crowd.

“Don’t be shocked. From what I hear, tens of thousands of rebels were killed or captured in a single battle.”

“Gasp! Tens of thousands!”

The numbers were staggering—far beyond those of a mere cult—and so was the victory they represented. They had barely caught their breath when voices elsewhere in the crowd rose to contradict the claim.

“What nonsense! A martial artist I know well told me that a hundred thousand were wiped out in half a day.”

“A hundred thousand? Wasn’t it three hundred thousand?”

“What are you all talking about? I heard more than a million rebels were annihilated!”

“Now, that’s enough nonsense. However you look at it, a million is too many, isn’t it?”

“Then let’s split the difference and call it half a million. No—three hundred thousand.”

“Three hundred thousand is still too many. Where did you even hear that?”

“Are you with Dark Heaven? Can’t you read the room?”

“Why are we suddenly talking about—”

“So, are we going with three hundred thousand or not?”

“…Is that something I get to decide?”

“Ah, three hundred thousand! Just so you know, I’m not budging any further!”

“O-okay. Fine. I’ll remember it as three hundred thousand, so please calm down.”

“Now we’re getting somewhere. Come on, repeat after me: Long live the Great Nation!”

“L-long live the Great Nation.”

“Hey! I can barely hear you!”

“L-long live!”

“Much better. Now, long live the Murim Alliance!”

“…When is this going to end?”

“We’re not done yet. Next is the Blazing Flame Divine Dragon—no, long live the Marquis of Shangshan! Prepare yourself.”

A few people looked less than thrilled, but most of the common folk cheered the Murim Alliance without holding back.

And that was a remarkable change in public opinion, even compared to just a few years ago.

The orthodox faction, led by the Nine Sects and One Gang and the Five Great Families, had ruled the Murim of the Central Plains. But a long peace had brought corruption, and power had bred injustice.

Did wearing spotless white make the heart beneath it white, too?

Still waters were bound to grow foul eventually. Perfect good and evil existed nowhere.

But now things were different.

“Long live the Marquis of Shangshan!”

“Long live the Blazing Flame Divine Dragon!”

Whenever people thought about how much had changed because of a single person, they couldn’t help but marvel all over again.

Jin Taekyung.

His path, which had begun about two years ago, was as deep and immense as the footsteps of a giant.

The Jin Family of Taiyuan, which had been crumbling bit by bit, had become a power ruling over Shanxi Province and the northern grasslands. It had even secured a place among the Five Great Families. And that was only one of his many achievements.

Jin Taekyung was the heir of the Fire King, Jeok Cheongang, and the successor to the Fire Gate Clan. He was a young giant who had raised the banner of a new Murim Alliance alongside the most renowned leaders of Murim. And with martial prowess beyond belief for his age, he was a righteous hero who fought against Dark Heaven.

There was no martial artist under heaven who didn’t know Jin Taekyung’s name.

Nor was there anyone who doubted or resented the meaning and weight behind the four characters *Blazing Flame Divine Dragon*.

No. No one would even dare.

Jin Taekyung had proven himself, and countless eyes had watched it all with their own eyes.

And this wasn’t happening only within the iron fence of Murim.


“To all the people under heaven, hear this!”

The Son of Heaven.

The great ruler who governed the realm on heaven’s behalf had proclaimed his mandate to the whole world.

The Emperor revealed all the schemes Dark Heaven had carried out. He named his only surviving younger brother Imperial Younger Brother and heir apparent, declared the fiends beyond the desert traitors, and in a single stroke tore down the sturdy wall that had stood between the government and Murim for ages.

He used none other than Jin Taekyung, the Marquis of Shangshan, as his battering ram.

“By the command of the Son of Heaven, I order you: unite and fight! Protect your land from the rebels who dare defy the natural order and seek to wield supernatural powers!”

And so the name Jin Taekyung resounded beyond Murim, echoing across the Nine Provinces and Eight Wastes, the Four Seas and Five Lakes.

To the martial artists, he was a young giant who would lead a new era. To countless common folk, he was the guardian of the imperial court and the Great General of the realm, who obeyed the Emperor’s solemn command and put down traitors.

A martial artist, and at the same time a marquis personally appointed by the Emperor.

There was no precedent for such a thing in the history of the Great Nation—or anywhere else. And yet it had become reality. The young hero fought with every passing moment to bring an end to this terrible age of chaos.

And once again, he had won.

“Waaaaah!”

“The Great Nation and Murim have finally united to drive out the rebels! Isn’t it all thanks to His Majesty’s wise reign and the Marquis of Shangshan’s efforts?”

“On a day like this, there’s no way I’m not getting drunk. Bring me a jar of wine! No—three jars!”

The story grew as it passed from mouth to mouth, but even without the embellishments, it was a victory no one could deny.

The taverns were packed. Those who spilled out into the streets happily raised their cups to toast the victory in Gansu.

They praised the Emperor as one. They thanked Jin Taekyung and the Murim Alliance for risking their lives to protect the people of the realm, and felt relieved that they and their loved ones were safe because of them.

They were buoyed by a vague hope that the war might soon end without much further loss.

“Come on, drink! Hurry!”

“Down the hatch! That’s it!”

Laughter rang out wherever one went. In the towns where people held great feasts, there wasn’t a trace of fear on anyone’s face.

The martial artists and the common folk alike.

They all laughed loudly and reveled in the joy of victory.

At least, for that one day.

Until a peregrine falcon, having flown from Qinghai on the distant western frontier, completed its weary journey.

* * *

When I was a kid, I used to be really disappointed if I couldn’t remember a dream from the night before.

*It must’ve been a good one, too.*

But at some point, I learned something.

Not remembering a dream meant I could at least avoid shuddering at the lingering feeling of a nightmare.

Of course, that didn’t mean the nightmare itself had never happened.

“Here.”

The first thing I saw when I opened my eyes on the swaying saddle was Hyuk Mujin’s face. He held out a scrap of cloth.

“…What’s this?”

“What does it look like? Take it. It’s not like I can wipe you down myself.”

“Oh.”

Only then did I notice how vividly my clothes clung to my body. What the hell had I been dreaming about to work up that much of a cold sweat?

*I know.*

Since becoming a Hunter, the nightmares I often had had generally fallen into two categories.

People who died because I couldn’t save them.

Or people who died by my hand.

*Actually, there is one more, recently.*

I remembered it suddenly.

A strange, unidentifiable dream.

Memories of the past that Taewon Jin Family’s Jin Taekyung had lived through—memories that couldn’t possibly exist in my head, because I was Jin Taekyung of Korea.

I was mulling over the thought that the dream I’d just had might have been something like that, when—

*Screee!*

A bird’s cry rang out from somewhere overhead, breaking my brief reverie.

As if to tell me to focus on the present, not a dream that was little more than an illusion.

*Right. This isn’t the time.*

I shook my head and drew up the Scorching Yang Qi within me.

*Whoosh. Crackle.*

Steam billowed out, and my damp clothes dried in an instant. Hyuk Mujin’s face flushed from the gentle warmth, and he muttered in a dazed voice:

“…Oh. Right. You could do that.”

“Sure. Unlike you.”

“…Are you bragging right now?”

“Yeah.”

“I mean, if you put it that way, I don’t have anything to say…”

Hyuk Mujin let his words trail off, still not quite satisfied. At that moment—

*Screee!*

The cry rang out again. I looked up at the sky without thinking.

And then my eyes widened.

“……!”

A missive, wet with blood, was tied to the leg of a falcon gliding through the air with its great wings spread wide.
## Chapter artifact 1064

# Chapter 1064

If they’d spotted it even a little later, that messenger eagle would have flown right over everyone’s heads.

Even messenger eagles, bred with far more rigorous training and care than messenger pigeons, were still only trained to fly between set destinations.

But a handful of people, Jin Taekyung among them, noticed the eagle just in time. The Bow Saint was among them.

The Bow Saint was the greatest archer under heaven—perhaps even the greatest in all history.

*Shing. Clack.*

It happened in an instant.

With the metallic sound of steel joints locking together, the two oddly curved swords transformed into a bow. The Bow Saint drew its string without hesitation.

“Now!”

At Jin Taekyung’s shout, the Bow Saint released the taut bowstring.

*Boom!*

The air tore apart.

A streak of light, faster than sound itself, reached the messenger eagle—a distant speck in the sky—in the blink of an eye.

Jin Taekyung had already anticipated all of this, and he shot forward, too.

*Whoooosh!*

His body surged like a gust of wind.

In a single bound, he crossed dozens of *jang*. At his fingertips was the messenger eagle, falling with an arrow through its wing.

*Screee. Screee!*

“Spit on it and it’ll heal in no time, you idiot.”

His words were gruff, but Jin Taekyung gently stroked the beak of the eagle as it cried mournfully. Then he hurriedly checked its leg.

*This is…*

He swallowed a groan as he saw the missive, rolled into a small bundle and fastened tightly around the eagle’s leg.

A sense of foreboding hit him before he’d even read it.

There was no doubt. That reddish substance smeared across the missive was blood—blood that had flowed from someone’s body.

And looking back at everything that had happened, these ominous suspicions never turned out to be wrong.

Kunlun fallen.

The moment Jin Taekyung read the first line of the missive, scrawled in a rough hand, he bit down on his lip without realizing it.

* * *

The Kunlun Mountains.

This immense range, at the western edge of Qinghai, held a distant history and countless legends.

Its ridges stretched for thousands of *jang*, reaching all the way to plateaus and deserts. And its peaks rose so high that calling them the highest summits was no exaggeration.

But the Kunlun Mountains held a particular significance for the martial artists of the realm for another reason.

A reason every bit as decisive as the existence of the Kunlun Sect, birthplace of Daoist martial arts and heir to a long history.

“So the pass we absolutely had to hold has been breached.”

Jeok Cheongang muttered, as if spitting out the words.

The missive, already passed through several hands, was crumpled in his clenched fist.

“If what’s written here is true and they’ve occupied Kunlun, then we’ve effectively lost half of Qinghai.”

At his low words, everyone nodded with grim faces.

Jeok Cheongang was stating a simple fact.

Most of the area around the Kunlun Mountains was made up of basins, vast enough to cover nearly half of Qinghai Province. Losing them meant losing control of the region.

“Must bring back some old memories. Doesn’t it, you old hag?”

At Jeok Cheongang’s sudden question, the Bow Saint frowned.

“That’s not something I want to hear from you. Whether you mean my age or the unpleasant memories of the Great Faction War.”

“So how was it, back at the start of the Great Faction War? When those Demonic Cult bastards crossed Kunlun.”

“It was an unexpected attack. The Demonic Cult’s last invasion before the Great Faction War had been hundreds of years earlier, and even then they’d been soundly defeated before they could cross the Kunlun Mountains. So of course we never expected it.”

But people always fixated on what they couldn’t have.

The Heavenly Demon, who had built the Demonic Cult into a force stronger than ever some fifty years ago, was no exception.

“How many days did the Kunlun Sect hold out back then?”

“Three. They fought for exactly three days and nights before they could hold out no longer and retreated. They suffered losses that came close to annihilation.”

“Three days against a hundred thousand Demonic Cult bastards. They held out a long time.”

He wasn’t mocking them.

The Kunlun Sect had always accepted only a small number of Disciples due to the harsh limits of their terrain and their strict rules. As a result, they had the fewest Disciples among the Nine Sects and One Gang.

But their Disciples were individually formidable, and the Kunlun Mountains were more treacherous than even the Great Snow Mountain. That was how they’d managed to repel the Demonic Cult’s invasions time and again.

Even so, the Kunlun Sect had its limits.

Back during the Great Faction War half a century ago.

And now.

The difference was that this time, unlike in the last Great Faction War, when the Kunlun Sect was dealt a devastating blow by the Demonic Cult at the very start of hostilities, they’d made a wiser choice.

“At least they made the decision to retreat right away, without hesitation. Isn’t that right?”

At Jeok Cheongang’s sudden question, I nodded, having been lost in thought.

“Even I think that was the best choice. Facing them head-on would’ve been insane.”

The Demonic Cult and Dark Heaven were different in kind.

I wasn’t talking about the quality or number of their troops. The darkness within Dark Heaven was far deeper and more boundless than anyone could imagine.

Even I couldn’t begin to guess its true size or depth.

But one thing was certain.

“If they’d decided to fight to the death like they did during the Great Faction War, the Kunlun Sect would already have been erased from the world.”

Maybe the Kunlun Sect had realized this battle was hopeless, too.

That might be why they’d decided to retreat so quickly, despite being joined by Qinghai’s martial artists and government troops—twenty thousand of them.

The missive said that around a thousand had been killed or wounded during the retreat, but that didn’t change the fact that it had been their best choice.

“Fortunately, they retreated as far as Qinghai Lake with most of their forces intact. Qinghai hasn’t been completely taken from us yet.”

Perfected Being Hyeoncheon, the Sect Leader of the Kongtong Sect, had abruptly spoken up. I immediately shook my head.

“You’re not wrong, but at this rate, it’s only a matter of time. The forces still in Qinghai can’t hold them back.”

“That’s…”

“They have magic—or, no, dark arts with a power that’s hard to believe. And the Dark Heaven forces that occupied the Kunlun Mountains are too numerous to count.”

That wasn’t a figure of speech or an exaggeration.

I was only repeating what was written in the missive carried by the messenger eagle I’d just caught.

As the Kunlun Sect decided to retreat swiftly, one of its Elders had sent a missive with these words:

Countless enemies, too many to even number, were filling the mountains and advancing toward them.

And seeing that overwhelming, terrifying sight had made him think of a certain day from decades ago.

“…The Hundred Thousand Demonic Disciples.”

The groan slipped from someone’s lips, and the air grew heavy. It was only natural.

Most of those present had already seen it with their own eyes.

They’d felt it on their skin, in every part of their bodies.

Most of the people here had seen and experienced Dark Heaven wield supernatural powers.

They must have felt despair and defeat as they watched a sight that tore down every assumption they’d ever held.

And now there were a hundred thousand of them.

Even if the Kunlun Sect Elder who’d written the missive had been overcome with fear, an army large enough to bring the Hundred Thousand Demonic Disciples to mind couldn’t have been far off in size.

*And someone I know is probably among them.*

Despite the brief time we’d spent together, the face of one unforgettable person suddenly crossed my mind.

The Grand Mage.

No—the Grand Mage.

I couldn’t be certain, but I already knew it in my gut.

She’d survived, tenacious as ever. If so, she had to be in Qinghai by now.

*If Qinghai falls, things will get out of hand.*

And not just because it was Qinghai.

Gansu, which we’d barely managed to protect, was in much the same situation.

The realm was one enormous dam. All it took to bring it down was a small crack—and the gap that followed.

*We need time. Time to think of something better, to stop them without taking even greater losses.*

A headache pressed in.

But this time, too, time wasn’t on my side.

Or rather, not time. The System.

*Logout.*

I carefully repeated the word in my mind, with a glimmer of hope.

The System’s response came back calm and cold.

*Beep.*

> **System**
>
> **Logout** is unavailable.

“…Damn it.”

Everyone’s attention snapped to me at the curse that escaped on instinct, but I didn’t care.

No, the situation was so fucked that I couldn’t care.

*Why?*

I’d already spent months in Murim and faced death several times over.

But at some point, the System had slammed the door shut and refused to open it.

It had done nothing but block the only way back to the modern world and force new Quests and a brutal reality on me.

Just like a few days ago, when we’d finally finished the long, brutal battle at the Great Snow Mountain.

Even now.

> **System**
>
> The ongoing linked Quest, **To Qinghai**, has not yet been completed!

*Crack.*

I stared at the holographic window floating in the air and swallowed back the curse that was about to slip out.

And, in a stroke of good luck amid all this misfortune, I cursed the System for tossing me a clue like alms in the form of a new Quest title. Then I spoke to a certain lunatic, who was the only one there nodding off like a sick chicken in the middle of this dire situation.

“You said you’d guide us, right?”

“Huh? Yeah?”

Only then did the Great Sir blink blearily awake. Wiping the drool from his mouth, he spoke in a sleepy voice.

“I think I did say that… So, have you decided where you’re going?”

“Yes.”

I straightened up and looked around.

Everyone, myself included, had paused here for a moment. This place was called the Qilian Mountains. At the range’s far end, after several days of travel, a new land awaited us.

A strange and dangerous land called Qinghai.

“Let’s go.”

At my quiet words, everyone’s eyes lit up as they rose to their feet.

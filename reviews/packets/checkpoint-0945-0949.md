# Checkpoint Review — 945–949

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

# Chapters 945–949

## Plot

Taekyung subdues Jang Sam after the bandit chief suddenly gains twenty Levels and attacks him in an apparently irrational state. Jang Il says Jang Sam had recently relocated to Anhui and taken over two small strongholds. A silk pouch given to Jang Sam by an unknown traveler in Hubei likely contained a modified Temporary Strength Pill. Taekyung and his companions suspect Dark Heaven is distributing the pills to give ordinary fighters temporary power, at the cost of dangerous side effects and possible addiction. Taekyung sends guides to alert the Nangong Family and Anhui’s City Lord, investigate the pills, and tighten security.

In Hebei, Peng Cheolhu learns that at least ten thousand grassland troops are gathering and heading toward Shanxi, possibly in alliance with Dark Heaven. In Shanxi, Jin Wikyung weighs evacuating Datong and Saneum and retreating to Henan as the approaching force may grow to thirty thousand. Allied leaders gather, including Lee Seowol with three hundred Mount Heng martial artists; Taekyung’s younger brother also emerges from seclusion. Wikyung walks toward the gathered allies and the coming battle.

## Continuity

- Jang Sam is unconscious and being taken to the Nangong Family. His sudden rise from Level 40 to Level 60, apparent loss of reason, and connection to the modified Temporary Strength Pill remain unexplained.
- The unknown traveler who gave Jang Sam the silk pouch, the pill’s exact effects, and the distribution network remain unknown. Taekyung has ordered an investigation and tighter security in Anhui.
- Grassland forces are approaching Shanxi and may number thirty thousand by arrival. The Peng and Jin Families suspect Dark Heaven is involved, but this is unconfirmed.
- Jin Wikyung ordered evacuations around Datong and Saneum and considered retreating to Henan; after allies gathered, he walked toward them rather than immediately carrying out the retreat.
- Lee Seowol has brought three hundred Mount Heng martial artists, and allied leaders have gathered to fight. Taekyung’s younger brother has emerged from seclusion; his name is not given.
- Taekyung said the Murim Alliance’s Fire Dragon Pavilion and a thousand Embroidered Uniform Guards would reach Anhui within a day or two.

## Translation Decisions

- Render 잠력단 as “Temporary Strength Pill” and 강기 as “Force.”
- Render 선비족 as “Xianbei,” 중양절 as “Double Ninth Festival,” and 이동진 as “Moving Formation.”
- Render 장퀴네스 as “Jangquines,” Taekyung’s teasing nickname for Jang Il.

## Durable state

{
  "active_continuity": [
    "The Emperor was poisoned with Blood Soul Gu, which reached his marrow; the Divine Physician said his vitality was at its limit and could not guarantee survival for another couple of months.",
    "The Divine Physician says the Emperor’s only path to survival requires him to die once; the method is not yet explained.",
    "Taekyung’s System Quest requires him to remove the Blood Soul Gu from the Emperor’s head and successfully treat him; its reward and failure consequence are unknown.",
    "Grassland forces are mobilizing toward Shanxi and are expected to reach thirty thousand; Jin Wikyung ordered evacuations around Datong and Saneum, considered withdrawing to Henan, and then walked toward gathered allies. He suspects Dark Heaven is behind the threat and fears its unrevealed forces.",
    "War against Dark Heaven is imminent; its main force has been targeting Shanxi as a foothold for invading the Central Plains, with the Double Ninth Festival the expected date.",
    "Taekyung was appointed Marquis of Shangshan and Thousand Captain, with a thousand Embroidered Uniform Guards entrusted to him to fight the foreign enemy.",
    "The improved Temporary Strength Pill has circulated for months and may create a dangerous, addictive drive for strength across Murim; its full effects and distribution network remain unknown.",
    "An unconscious bandit chief is being taken to the Nangong Family for possible interrogation; he may hold important information about the pill.",
    "Jang Sam abruptly rose from Level 40 to Level 60, attacked Taekyung while apparently irrational, and is unconscious and being taken to the Nangong Family.",
    "Jang Sam’s silk pouch, received from an unknown traveler in Hubei, likely contained a modified Temporary Strength Pill; its effects and side effects remain unconfirmed.",
    "The Bow Saint once wondered whether Pung Yang might have been the chosen one; the Martial God’s identity and connection to the chosen one and the Bow Saint remain unknown.",
    "The Eastern Heaven Demon Lord’s hidden iron chest contained old bamboo slips, recent papers, and a small silk pouch of unknown significance."
  ],
  "continuity_sources": [
    949,
    948
  ],
  "open_questions": [
    "Who was the traveler who gave Jang Sam the silk pouch, and what are the modified pill’s exact effects and side effects?",
    "How widely has the improved Temporary Strength Pill spread, and who is distributing it?",
    "What is the Martial God’s identity, and what is his connection to the chosen one and the Bow Saint?",
    "How far has Dark Heaven infiltrated the Great Nation, and which officials or commanders are involved?",
    "What do the Eastern Heaven Demon Lord’s papers and silk pouch contain, and what is their significance?"
  ],
  "safe_through": 949,
  "temporary_decisions": [
    "Taekyung intends to keep the pocket watch for half a month before deciding whether to give it to Mujin."
  ],
  "version": 1
}

## Reading copies

## Chapter artifact 945

# Chapter 945

Grrk. Krrk.

What should I call that?

A groan? Or a roar?

Whatever it was, one thing was certain.

That burly man slowly rising to his feet right now was moving one step farther away from the word *ordinary*.

“Who is that…?”

Namgung Ryong looked at the man with a questioning gaze.

It was only natural that he didn’t know who the man was. Before Namgung Ryong arrived, the burly man had run into Jeok Cheongang by chance, picked a fight without knowing any better, and been knocked unconscious with a single punch.

“He’s a bandit.”

“A bandit?”

“Yes. And he’s the head of the bunch.”

I tapped the top of my head, and Namgung Ryong nodded as he immediately understood what I meant.

“I can see why that man was acting like their leader.”

His gaze fixed on the burly man, growing even more intent.

“Though I don’t know if an ordinary bandit chief could look like that.”

Ssshhh.

A breath carrying heat enveloped the area.

I watched the burly man as he exhaled vaporous breaths through his clenched teeth.

More precisely, I was staring at the translucent holographic window that had just appeared above his head.

> **System**
> Lv. 60 Jang Sam

A painfully common name. A face that looked like a bandit at a glance.

But the change that had come over him in such a short time was unmistakable.

It wasn’t just the whites of his eyes showing or the hot breath spilling from his mouth. The number before his name proved it.

*His Level… went up.*

Of course, this wasn’t the first time I’d seen someone’s Level change.

Masters who had reached the realm of Returning to Simplicity, or something close to it, could control their energy freely. Even Qi Sense couldn’t accurately read their Level.

But this bandit chief was different.

He wasn’t a master of Returning to Simplicity, nor had he gained enlightenment and raised his Level that way.

*And people don’t jump twenty Levels all at once.*

A bizarre phenomenon: a backwater bandit chief who’d been only Level 40 suddenly leaping up twenty steps.

How was I supposed to make sense of that?

“I can’t understand this at all, based on what I know. Care to explain?”

The moment I asked—

Whoosh.

A huge fist came down over my head with a heavy whistle.

Crash!

Just one step.

I’d barely shifted to the side when the ground caved in, sending grass and dirt flying in every direction.

That was power he could never have shown before he passed out.

I narrowed my eyes as I looked at the man, who now had a considerable amount of internal energy.

*He’s completely lost it.*

I’d suspected as much from the whites of his eyes, but at this point, he’d practically lost his reason.

No—maybe even waking up from his unconscious state hadn’t been his own doing.

A man in his right mind wouldn’t charge at me in this situation unless he had a death wish.

“Raaaagh!”

“…Well, then.”

There was no helping it now.

As he charged at me like a wild beast again, I slipped into his reach and gently extended my hand.

Tap.

My palm touched his chest.

At the same time, a faint heat—one I’d worked hard to suppress, over and over—burst out through my palm.

Boom!

With a sound like compressed air exploding, his eight-foot frame shot away like a cannonball, cutting through the air before slamming into a tree.

Kraaaash!

Beyond the thick cloud of dust, I grabbed his motionless body with one hand and dragged him back. The bandits’ eyes widened.

“We’re short on time, so I’ll keep this brief.”

As they stared in shock and fear, I continued in a low voice.

“Tell me everything you know. If you want to live.”

* * *

Every man lives with some dream tucked away in a corner of his heart.

It might be a red sports car that costs a fortune, or a study that practically reeks of a successful professional’s life.

I was no different.

When I was a teenager, I dreamed of having a motorcycle. I wanted to take my girlfriend for a ride on the back and really open it up.

Of course, I didn’t know then.

That even ten years later, I’d still have no girlfriend.

And that instead of straddling a sleek motorcycle or a red convertible, I’d be riding a green, four-wheel-drive thoroughbred and saying this to a man:

“Hold my waist tight, you bastard. You want to fall off the saddle?”

“Y-Yes!”

“But don’t grab too hard. If you pinch me, you’ll die.”

“Eek! I’m sorry, I’m sorry!”

Thud-thud-thud!

The thunder of hooves mingled with a tearful voice.

Maybe Namgung Ryong and the authorities had already made arrangements, because nothing got in the way of us as we rode nonstop at full speed.

There was only one thing bothering me: the guy behind me kept sniffling.

“So, Jangquines.”

“…Yes.”

Jang Il answered in a voice that sounded half resigned. He was the bandit who’d posed as a woodcutter who’d lost his carrying frame, only for me to catch him at his real trade.

Jang Il had been a bandit for more than ten years. He was at the very bottom of the pecking order, but there was one unusual thing about him that the other bandits didn’t share.

“You’ve known that guy for ten years?”

“Y-Yes. I’ve known him ever since I first set foot in this line of work. At one time, we were like brothers who’d shared blood.”

“Brothers, my ass. You’re a bandit. What a load of bullshit.”

Jeok Cheongang, who’d been listening as he rode beside us, gave his candid opinion. The Bow Saint frowned and clicked her tongue softly.

“Why don’t you stay out of it and let him finish?”

“What? Am I not allowed to talk to myself anymore?”

“You really haven’t changed. You’ve lost all your hair, but otherwise you’re just like you were back then…”

“Do you have something to say?”

Jeok Cheongang’s gaze turned icy. Lately, his hair had been slowly sprouting like spring shoots, and he’d been tending to it with loving care. He made no attempt to hide his anger.

“That’s enough, you two. You, keep talking.”

Even as the two Supreme Peak masters exchanged cold looks, the horses kept running. Jang Il swallowed hard and continued.

“A-Anyway, I followed the chief from then until now. When he said we were moving the stronghold to Anhui Province, everyone called him crazy and left, but I followed him on nothing but faith and loyalty.”

“You moved the stronghold to Anhui Province?”

“Yes. It was near Hubei originally, but one day the chief suddenly decided that was what we were doing. Everyone was dead set against it.”

Jang Il smacked his lips, as if remembering the day, then went on.

“Truth be told, I didn’t say anything, but I was even thinking about quitting this life and leaving before it was too late.”

“Why? Was moving the stronghold that big a deal?”

“Oh, you don’t know what you’re talking about. Packing up and leaving would’ve been a bit of a hassle, sure, but Anhui has the Nangong Family.”

I frowned. Even at a glance, what Jang Il was saying didn’t quite make sense.

“That’s not a reason. Wudang and the Zhuge Clan were in Hubei, where you were before.”

Jang Il immediately shook his head.

“It’s not about how many great sects there are. You have to look at which great sects are nearby.”

“Oh.”

“Wudang and the Zhuge Clan are relatively mild. Most of the time, they settle things without bloodshed. But the Nangong Family…”

Jang Il trailed off, then shuddered.

“Maybe that’s why the martial artists of Anhui don’t go easy on anyone, either. If things go wrong, you have to be ready to lose your head.”

It was ridiculous—so ridiculous I could hardly believe it.

They were bandits, and they still took things like that into account when deciding where to operate.

But separately from that, there was definitely something strange about the chief’s choice.

He’d built a stronghold right on the border between Zhejiang and Anhui, with the imperial capital close by—and the Nangong Family nearby, too.

“When did you move the stronghold?”

“Probably… three months ago? Around then.”

“What about the other bandits who were with you? From what you’ve said, it sounds like all the ones from your old place ran off.”

“They say you should stick to your own turf, but when we got here, we found these gutsy bastards playing bandit in Anhui without even belonging to the Green Forest Alliance.”

“So your chief brought them under his command?”

“That’s right. One day, he left on his own, leaving only me behind. Then he came back after taking over two small strongholds.”

Jang Il added sadly,

“And here I am, still at the bottom of the pecking order.”

I had no interest in listening to an old man complain about his lot in life. Feeling the wind brush past my hair, I thought to myself,

*Even if they were small, he took over two strongholds all by himself?*

Of course that was bullshit.

Before his Level went up, the man had been no more than a middling Second Rate fighter, relying on some tiny amount of internal energy—who knew how he’d built it up—and his natural strength.

*At best, he was on the threshold of First Rate. That wouldn’t come close.*

You had to be at least Supreme First Rate to even talk about having a chance against dozens of people at once.

And that was assuming your opponents were at least a full level below you.

“So he had something to fall back on after all.”

“Pardon?”

“The man you followed as chief. He wasn’t that strong, was he? What gave him the confidence to move to Anhui and unite two whole strongholds?”

“Well…”

Jang Il hesitated for a moment, then nodded.

“I did find it strange myself. By my standards he was strong, but his martial arts weren’t anything special…”

Anywhere under Heaven, a bandit who stood out in his region eventually had to choose one of two paths.

Either trust in his decent martial arts and swagger around until disciples of a great sect came to wipe him out, or join the Green Forest Alliance.

*In the case of river bandits, there was the Yangtze River Channel League.*

A small business never beats a corporation.

Once you became an officially recognized franchisee of the Green Forest Alliance, you had to pay substantial taxes, but as long as you didn’t openly commit atrocities, you could avoid being hunted down by the great sects.

You went from being a mere bandit to part of a symbiotic system that at least followed a few basic rules.

*But that man fit neither category.*

For the past ten years, he’d never made a name for himself. Then he built a stronghold right next to Zhejiang Province, where the imperial capital stood.

Even if he was trying to cash in on the Double Ninth Festival holiday, there was no way to explain it logically.

Just like the way he’d suddenly grown so much stronger.

*You couldn’t even call this a fortuitous encounter.*

And this whole string of strange events brought back a memory from more than a year ago.

*Pung Yang. Pung Yang, the Red Wind Band Leader.*

The chief of the mounted bandits who’d set his sights on the Mount Heng Sword Sect—no, on Shanxi Province.

And the one item that had given him such grand ambitions.

*The Temporary Strength Pill…!*
## Chapter artifact 946

# Chapter 946

Time is fair.

To the living, the dead, and even things without form.

And in that sense, the name of someone that suddenly crossed my mind at this very moment was already starting to fade.

If not for the fierce battle that day and the item I’d happened to get my hands on after winning, it wouldn’t have been strange if I’d forgotten it in no time.

*The Temporary Strength Pill…!*

Was this what it felt like to be struck by lightning right on the crown of your head?

The shock shook my mind, and I felt my body stiffen before I knew it.

*No way.*

The first emotion that came to mind was denial.

But I knew better than anyone that the reason I wanted to deny the thought that had just crossed my mind was that I didn’t want to believe it.

“What did that bastard—your leader—have?”

“Pardon?”

“Some secret that didn’t sit right. A strange item he didn’t have before. Whatever it was, remember.”

“G-Great Hero, what on earth do you mean…?”

Jang Il, who’d been clinging to my back like a leech, asked in a trembling voice.

Instead of answering, I did everything I could to keep my grip from tightening around the reins.

We couldn’t stop here.

We had to ride even a moment longer.

Even if I reined in the horse right now, nothing would change.

“There must have been something strange. There has to be.”

“P-Please, wait. Please calm down, Great Hero.”

Jang Il looked completely flustered. I was just beginning to regret not bringing the leader, who was still unconscious, when—

“…Huh?”

A dazed voice suddenly reached my ears.

I whipped my head around. Jang Il was staring back at me, eyes wide.

“Come to think of it, at some point he started carrying a silk pouch everywhere.”

“A silk pouch?”

“Yes. I remember it clearly. A few months ago, he got it from a traveler passing our stronghold in Hubei—bad luck for the traveler, I suppose—instead of a toll. After that, he kept it close like it was some kind of sacred relic. I thought it might be precious musk or something.”

A traveler he’d met in Hubei.

A mysterious silk pouch the leader had kept close to his heart.

And the leader’s inexplicable behavior after that.

“Um, was there something wrong with the pouch? I did wonder about it a little, since it didn’t have the distinctive smell of musk.”

I didn’t answer Jang Il’s question.

No—I couldn’t answer.

The moment my ominous suspicion became certainty had arrived.

And I knew there was no more information I could get out of Jang Il.

What had been inside the silk pouch, and who the traveler who’d owned it was—

Even decades from now, he wouldn’t know.

*There’s no doubt. It was the Temporary Strength Pill.*

The Temporary Strength Pill was just what its name suggested: a pill that drew out all the strength latent within the body.

Having experienced its dangers firsthand when I fought Pung Yang, I could only grit my teeth.

Crunch.

“What is it?”

Jang Il wasn’t the only one who’d noticed something was wrong.

I looked at Jeok Cheongang, whose face had gone rigid, and steadied my breathing.

“Do you remember what happened in Shanxi Province?”

“What do you mean by ‘what happened’? When?”

“I mean the mounted bandits who attacked the Mount Heng Sword Sect. I told you about it once before.”

Strictly speaking, Jeok Cheongang had set foot in Shanxi Province just after the Mount Heng Sword Sect affair had ended.

But he was one of the few people who knew everything about Pung Yang and the Temporary Strength Pill.

“…Then could it be?”

His eyes widened as he realized what I was getting at.

“Yes.”

I continued in a low voice.

“It’s likely. No—in light of the circumstances, there’s no doubt.”

“Goddamn it.”

Just as Jeok Cheongang let out the curse like a sigh, the Bow Saint, who’d been listening to us with a grave expression, spoke up.

“This is about that bizarre pill, isn’t it?”

“……!”

“Don’t look so surprised. Even if it was in the past, it was barely a year or two ago. I already knew about the Mount Heng Sword Sect and the Red Wind Band.”

The Bow Saint continued, unfazed by my surprise.

“I know you were careful to keep it quiet, but the truth always leaks out unless you silence the witnesses.”

For a moment, I’d forgotten all about it in the shock of the Temporary Strength Pill.

Why the Bow Saint had chosen to stay by the Emperor’s side.

And just how many eyes and ears of the imperial court were scattered across this vast land.

“If you already know, then there’s no need for me to go into a long explanation.”

The Bow Saint’s lips curved into a faint, inscrutable smile as I quickly regained my composure.

Of course, that faint smile vanished as quickly as it had appeared.

“The events at the Mount Heng Sword Sect gave me reason to wonder, too. Especially after I learned more about a man named Pung Yang, who led the Red Wind Band.”

Setting everything else aside, any martial artist would have had questions.

That day, in front of a fair number of onlookers, Pung Yang had displayed power close to the Supreme Peak realm.

He’d already reached the fully developed Peak realm, making him a formidable fighter in his own right. But the fact that he’d manifested Force, even imperfectly, was beyond all reason.

*Especially when you consider that the Head Elder, who’d reached the very limits of the Peak realm, could only show power like that after drawing on his innate qi.*

Learning martial arts was like climbing an endless flight of stairs.

A beginner just starting out might skip several steps at once. But at the Peak realm, you had to give everything you had just to reach the next one.

Even Cheongpung, born with heaven-sent martial talent and strengthened at a dazzling pace, wouldn’t have skipped the steps laid out before him.

*But the Temporary Strength Pill could make that possible.*

Its effects were tremendous, but the side effects were terrible, and the power didn’t last long. It twisted the natural order itself.

There was no way the Bow Saint could have missed that after learning more about Pung Yang.

“At the time, I even wondered if the man I’d been searching for might have been Pung Yang—who died because of his greed.”

The Bow Saint murmured the words softly.

A question suddenly came to mind.

If Pung Yang, not I, had survived that battle—and if he really had been the chosen one—what choice would she have made?

But I could only quietly suppress that question as it rose within me and swallow it down.

The situation we were facing was far too serious for that.

“It seems… someone is secretly distributing the pill Pung Yang used.”

Naturally, Jeok Cheongang and the Bow Saint already knew who I meant by *someone*.

Dark Heaven.

The ones who had made the Temporary Strength Pill.

I didn’t know exactly how long they’d been setting all this up. But the fact that it had reached the hands of an ordinary bandit was no small matter.

“Are you sure? From what this old man heard, its effects seem far too weak.”

At Jeok Cheongang’s deeply grave question, the Bow Saint shook her head on my behalf.

“The bandit who stood in your way hadn’t even reached First Rate. Considering the changes he showed afterward, there are two possibilities.”

“What two?”

“Either its power varies according to the user’s level. Or…”

The Bow Saint’s voice trailed off as she looked toward me. I spoke up.

“Or they reduced its effects—and the side effects along with them.”

“……!”

A brief silence fell. Jeok Cheongang looked between the Bow Saint and me with a heavy gaze, then muttered in a low voice,

“It must be the latter.”

“We can’t be sure of that yet.”

“No matter what you call it, that’s just wordplay meant to avoid facing reality.”

Jeok Cheongang shook his head at once, then continued in a firm tone.

“Everyone in this world wants power. Wealth, fame, strength—whatever it is, they want to stand above others. But everything comes at a price.”

Great power came at a great price.

And most people, however fiercely they wished for something, couldn’t bring themselves to put in the effort it took to get it.

Because they knew how hard the process was.

Because to obtain what they wanted in the future, they had to sacrifice the happiness and sweetness of the present.

“But what if the price you had to pay for a moment of power was something you could easily bear?”

That was when I understood why Jeok Cheongang was so certain.

And what he was really trying to say.

“They didn’t make it just to bolster their own fighting strength.”

“……!”

“How could Pung Yang, who led a mere band of mounted bandits, and some lowly bandit have gotten his hands on it? No—why would they reach out to people like that in the first place?”

No one would touch a bomb.

It might go off at the slightest jolt. Just getting too close could tear your whole body to pieces with its blast.

But what if it wasn’t a bomb, but a campfire?

On a cold winter day, those wandering through the snow in search of something would reach out to feel its warmth.

Even if they got too close, it would be fine.

They’d get a small burn, that was all. They already knew it wouldn’t kill them.

A campfire anyone could reach toward.

A trivial price to pay for its warmth.

That was probably exactly the picture Dark Heaven wanted to create.

There were madmen scattered all across this vast land, eager to taste power even if they had to pay that small price.

And those called the orthodox faction would be no exception.

*Power anyone can obtain…!*

That was the true danger of the new Temporary Strength Pill.

Its alluring power would tempt people who’d spent ten years, or even decades, stuck in the same place.

It would addict and ruin them in the blink of an eye.

And at the same time, the Lord of Heaven would be able to give greater vitality to the countless followers who served him—or rather, to those who were little more than disposable meat shields.

To the innumerable hordes of Dark Heaven, even now surging like a wave toward Shanxi Province.
## Chapter artifact 947

# Chapter 947

I’d known for quite some time that an uncontrollable danger was drawing near.

I’d watched the enormous blaze called Dark Heaven approach with my own eyes.

But there was one thing I hadn’t known.

That another blaze was approaching from behind.

That heat, which had begun who knows when, was burning through us from deep within, consuming our very organs.

*If the newly improved Temporary Strength Pill spreads throughout Murim…*

It won’t be a simple blaze anymore.

It’ll be a bomb.

A time bomb that’ll suddenly go off with a bang when the moment comes.

Just as modern drug addicts keep reaching for drugs even when they know their bodies and minds will be ruined, martial artists won’t be able to stop either.

No. They’ll be worse.

Martial artists are a bunch of lunatics who’ll do anything to get stronger.

Their desire for martial arts is pure and primal—and that’s exactly why it’s more dangerous than anything else.

All the more so because that desire transcends the values of the orthodox, unorthodox, and demonic paths.

“They’ve… poisoned Murim.”

Jeok Cheongang’s heavy murmur cut straight to the heart of the situation we were in.

Poison.

That was right. This was poison.

A deadly toxin called desire, one that even the Myriad-Poison Ring couldn’t cure.

And among those present, there was only one person who hadn’t yet figured that out: a bumpkin bandit from the countryside.

“P-Poison? What do you mean by that, sir?”

Jang Il’s face was full of confusion.

But no one answered his bewildered question.

“You there. Your ears working?”

At Jeok Cheongang’s abrupt question, the Nangong Family martial artists who’d been acting as our guides stiffened, then replied with serious expressions.

“Of course, Great Hero Jeok.”

“The Family Head told us to treat you as we would him. Give us your orders whenever you like.”

“Orders, you say? That’s good to hear.”

Jeok Cheongang nodded, then gave me a look.

There was a reason I’d spoken about something so important out loud even with Jang Il here.

It was because of them.

*We need to get this information out as soon as possible.*

The unconscious bandit chief, who should be bound and on his way to the Nangong Family by now, was the key to this whole affair.

Of course, since he’d already lost half his mind, there was little chance he’d be sane if he woke up. But if we interrogated him, we might still learn something important.

“Effective immediately, I’m changing part of your assignment.”

There were four guides in all, sent by Nangong Cheon.

I looked at three of them in turn and gave them their new orders.

“One of you will go to the Nangong Family right now. Another will return to Great Hero Nangong and tell him everything immediately. And the last one…”

“To the Anhui provincial government?”

Quick to understand, easy to brief.

I nodded and continued.

“Tell the City Lord directly. Mobilize every force he can and tighten security. Have him investigate every detail related to this matter.”

Dark Heaven’s improved Temporary Strength Pill had begun circulating months ago. No matter how discreetly they’d handled the process, traces would show if we dug deep enough.

And if the City Lord himself, who commanded at least ten thousand troops, got involved, we could search even the remote places the Nangong Family couldn’t reach.

“I’ll relay your orders. But I’m not sure the City Lord will be willing to do that much for us…”

The Nangong Family martial artist let his words trail off. I thought I knew what he was getting at.

Since time immemorial, the government and Murim had stayed out of each other’s affairs.

The Emperor had declared war against Dark Heaven, but this was still only a cooperative arrangement in which he’d thrown his support behind the Murim Alliance.

The City Lord, a servant of the Great Nation to his very bones, wouldn’t be pleased to hear this before he even understood what was really going on.

Especially when it came from martial artists whom officials had long regarded with indifference—and who felt the same way about them—and amounted to an order in all but name.

“That’s true. He might not be.”

The Nangong Family martial artist hesitated at my mutter, then shook his head.

“No. Don’t worry. Even if the City Lord objects, the Family Head can make a strong request in the Nangong Family’s name—”

“Well, there’s no need to go that far.”

“Pardon?”

“Do you have any paper? Oh, never mind. It’s fine.”

Riiip.

Leaving the Nangong Family martial artist blinking in confusion, I spread the strip of cloth I’d just torn off against the horse’s head.

At the same time, I silently spoke a command in my mind.

*Open Inventory. Summon.*

Ding.

Along with a clear chime, a cool sensation reached the hand I’d been feeling around inside my robe with, just to keep up appearances.

“What is that…?”

“Just a moment.”

A question mark appeared in the Nangong Family martial artist’s eyes as he stared at the object in my hand. I ignored him and poured in Scorching Yang Qi.

Rumble.

With a faint tremor, the ornately decorated silver plaque grew red-hot. The characters engraved into it—surely the painstaking work of a renowned imperial artisan—must have heated up as well.

Ssssss.

The heated silver plaque met the dark blue silk.

After breathing in the acrid smell of burning for a few seconds, I lifted my hand. A blackened design and characters had been stamped onto the torn strip of cloth.

*Great Marquis of Shangshan.*

“It’s a little messy, but it should still be legible, right?”

“……!”

“……!”

Silence fell.

The sound of hooves filled the space where no one answered. Before I knew it, everyone except Jeok Cheongang and the Bow Saint was staring at me, eyes wide.

“W-What on earth is this?”

“You didn’t know? It’d take too long to explain, so just take this to the City Lord for now. And be sure to tell him this isn’t a request. It’s an order.”

I spoke to the Nangong Family martial artists, still unable to close their mouths.

“If he still gives you a hard time after seeing this, tell him this. Don’t leave out a single word.”

“W-What should we tell him?”

At someone’s trembling question, I answered without hesitation.

The unchanging rule that held true in Murim, in the modern world, and even in a fantasy world crawling with dragons building nests.

“When I tell you to do it, you do it.”

“……!”

What rank would a City Lord be in the official hierarchy?

The question briefly crossed my mind, but one thing was certain.

He was a few rungs below me, now that I’d formally been made a marquis.

“Oh, one more thing. The reinforcements will arrive within a day or two at the latest.”

The mouths that had hung open moments earlier were now tightly shut.

One of the silent Nangong Family martial artists forced out his voice.

“R-Reinforcements?”

“Members of the Murim Alliance’s Fire Dragon Pavilion. And a thousand Embroidered Uniform Guards.”

“……!”

“Stick close to the City Lord and keep an eye on him. If he seems really suspicious, tell them they can take his head.”

Anhui was close enough to the imperial capital that you could almost get there in a hop, skip, and a jump. The City Lord would have to be insane to harbor any other intentions. But that wasn’t proof Dark Heaven hadn’t gotten its claws into him.

“Is… is that really allowed?”

Someone asked in a dazed voice. I answered calmly.

“It is. I can.”

We were unmistakably at war, and besides holding the exalted rank of marquis, I was a Thousand Captain in the Embroidered Uniform Guard, which answered directly to the imperial household.

Unless he belonged to the imperial family—no, even if he did—I had more than enough authority to punish him.

And all of that authority and prestige came from the Emperor.

*The Son of Heaven put a sword in my hand himself. I’d better swing it without hesitation.*

I hadn’t accepted this sword to enjoy riches and glory or to look impressive.

It was a sword and a title I’d received to cut down any enemy standing in my way and protect my people.

If it took a sword dance to get the job done, I could keep dancing until I dropped from exhaustion.

“Now, let’s split up.”

At my abrupt words, the Nangong Family martial artists, who’d been staring at me blankly from their constantly shifting saddles, finally came to their senses.

“We obey!”

Thud-thud-thud!

With a fervent shout that sounded like they’d forgotten who they worked for, three of them turned their horses and galloped off toward their respective destinations.

We let one guide remain to lead us to the border between Anhui and Henan, along with someone who’d slipped from everyone’s mind for a while.

“I-I obey!”

“……?”

A belated reply rang out behind me.

I turned and met the eyes of the voice’s owner: Jang Il, a bandit with an unnecessarily determined look on his face.

“For the sake of the realm, I’ll do everything in my power to help—”

“Get down. Unless you want to die.”

“Yes, sir.”

* * *

Anyone who’d experienced war even once knew.

The air around them. The wind. The sunlight. The people.

Everything felt different from usual.

An inexplicably heavy, ominous darkness rippled through the world.

Perhaps that was why the old man’s face wouldn’t relax, though he’d woken after a long, deep sleep—the first in a very long time.

“Damn, the weather’s shitty today.”

If someone had heard the old man mutter just now, they’d have scoffed and said the old bastard was senile.

The sky outside the lattice window was blue, and bright sunlight poured down between the few scattered clouds.

But if that someone were a martial artist—or some person living in Hebei—they wouldn’t dare even meet his gaze.

The old man glaring out the window was a giant of a man, and just as renowned across the realm. A living legend.

“Is nobody there?”

A beast’s roar could shake its surroundings even when quiet. The old man’s voice rattled the pavilion, and it took no more than an instant for those nearby to respond.

“Have you woken, sir?”

At the deep voice outside the door, the old man gulped down cold water and wiped his mouth.

“Where’s Cheolyeong, that bastard?”

“The Family Head is in the Inner Hall, attending a meeting.”

“A meeting?”

“Yes. It began two shichen ago.”

“Everyone’s gone mad. And nobody woke me for something like that?”

At the old man’s growl, the person outside the door caught their breath, then answered carefully.

“W-Well…”

“You have an excuse?”

“You said you’d rearrange our five viscera and six bowels if we woke you while you were sleeping soundly.”

“Oh.”

The old man scratched the back of his head.

Now that he thought about it, he had said that.

He hadn’t been sleeping well lately, so he’d been on edge. He’d fallen into a deep sleep for the first time in ages, and forgotten.

“Damn it. I finally got a good long sleep, so I guess something must’ve happened.”

The old man clicked his tongue softly and got up.

He knew what kind of men his eldest son, the current head of the family, and the senior members under him were.

If a bunch of meatheads who had nothing but muscle between their ears had been sitting on their asses for two shichen, the matter had to be serious.

“Go tell them right now. This old man is coming.”

The gaze of the towering old man, Peng Cheolhu, the Thunderbolt Saber King, settled into a deep, unreadable calm.
## Chapter artifact 948

# Chapter 948

Servants and maids hurriedly cleared away the furniture, broken and smashed in every which way.

And amid a scene that looked as if a typhoon had swept through, a group of hulking men glared at one another, breathing hard.

That was what the Thunderbolt Saber King, Peng Cheolhu, saw the moment he entered the Inner Hall’s grand conference room. After grasping the general situation, he looked around and casually said one thing.

“I’ll count to three. No more, no less. If you’re not back in your places by then…”

Whoosh!

Before he’d even finished speaking, dozens of hulking men scattered like the wind, returning to their original places.

All but one.

“You’re here, Father.”

At the greeting from his eldest son, who was already nearing seventy, the Thunderbolt Saber King furrowed his brow.

“You’re awfully late for your morning greeting.”

“I heard you were sleeping soundly…”

“Cut the nonsense. I thought you were finally ready to act like a proper person, so I handed over the Family Head position—and now you’re fighting with your own blood relatives? In this sacred conference room, no less, where we’re discussing matters of vital importance to the family!”

Peng Cheolyeong, the Iron Blood Saber and current Family Head of the Hebei Peng Family, silently endured the booming shout before speaking up.

“It brings back fond memories of when you broke Third Uncle’s left arm. In this sacred conference room, no less, where we were discussing matters of vital importance to the family.”

The Thunderbolt Saber King paused for a moment, then replied in a stern voice.

“That was when I was in my prime.”

“That was last year.”

“…That can’t be right.”

“And that’s not all. The year before, Second Uncle dozed off for a moment during a meeting, so you punched him in the jaw—”

“Now, Family Head!”

Second Uncle cut in sharply, rebuking Peng Cheolyeong for daring to talk back to the Thunderbolt Saber King, his father and Grand Family Head. Then he added,

“It was my shin. I don’t know who got punched in the face, though.”

“I’m sorry. I must have mixed them up. That was probably Fifth Uncle.”

The moment the Thunderbolt Saber King appeared, Fifth Uncle had crumpled into a corner. Now he muttered with sorrowful eyes,

“Right. That was three years ago. I woke up and two days had passed…”

“That’s enough. I get it. Let’s move on.”

Having failed to come out of the exchange with any dignity, the Thunderbolt Saber King shook his head and took the seat of honor.

Fortunately, the sturdy iron chair—provided in keeping with the Hebei Peng Family’s time-honored tradition of throwing punches at the slightest provocation—had survived intact.

“Enough nonsense. Everyone, sit down. First, tell me what was so important you spent two shichen beating each other up and arguing.”

Peng Cheolyeong took the seat beside him and immediately spoke.

“Something’s wrong in the north.”

“The north? Why would the Murong Family suddenly be acting strange?”

It was only natural that the Thunderbolt Saber King brought up the Murong Family.

For the Hebei Peng Family, the north had always meant the Murong Family.

The descendants of the Xianbei, whose ancestors had proclaimed themselves kings of a nation centuries ago, ruled Liaoning Province—the true frontier—and had long since secured their place among the Five Great Families.

“There’s no way anything’s wrong with the Murong Family. You must have heard bad information somewhere.”

The Thunderbolt Saber King waved the idea away as if it weren’t even worth hearing out. But at Peng Cheolyeong’s next words, his expression hardened.

“I wasn’t talking about the Murong Family.”

“What?”

If it wasn’t the Murong Family, there was only one place left.

The real north. A land of outlaws even more lawless than the Murim, where hidden schemes and blades lurked at every turn.

“Don’t tell me… you mean those barbarian bastards from the grasslands?”

“Yes.”

Peng Cheolyeong, considered the mildest of the Hebei Peng Family by blood, continued in a calm voice.

“The rumors we’ve been hearing are troubling.”

“They’re a vicious lot to the bone, but things have been quiet for the past few years, haven’t they?”

What the Thunderbolt Saber King said was true.

More precisely, peace and prosperity had begun to settle over the grasslands about two years ago, after ages of unceasing conflict.

And at the center of it all was the Jin Family of Taiyuan, a rising power in the north.

“I heard there haven’t been any problems since the Jin Family of Taiyuan formed the Seven-Route Army—or whatever they call it—and swept through the place. Am I mistaken?”

“You’re exactly right. They went on a single campaign and pulled out the tooth that had been aching for ages.”

Right after taking control of the Shanxi Murim, the Jin Family of Taiyuan had acted with a speed and boldness that left even the Five Great Families and the Nine Sects and One Gang speechless.

They’d absorbed not only the various sects that had bared their teeth at the Jin Family in the past, but also Escort Bureaus and merchant houses. Then, using that strength, they formed seven military forces and swept across the grasslands.

Neither the mounted bandits who periodically crossed the border to pillage and kill, nor the horse-riding tribes could stand against the Seven-Route Army.

In fact, some of them had even rallied beneath the Jin Family of Taiyuan’s banner and reaped a handsome reward for their victories.

“Temur. Chinggen.”

At the foreign names that slipped from his son’s lips, the Thunderbolt Saber King narrowed his eyes.

Since stepping back from the front lines, he’d devoted himself to martial arts. But he was still, in name and in truth, the Grand Family Head of the Hebei Peng Family.

He remembered the substance of nearly every meeting he occasionally attended, and the names of barbarians whose faces he’d never seen were no exception.

“Those two who joined the Jin Family of Taiyuan and became Great Chieftains. Is that right?”

“Yes. I hear they’re called ‘khans’ on the grasslands.”

“Khan or con, I don’t care. What matters is what those bastards are up to.”

The Thunderbolt Saber King tapped the table with fingers like iron rods, lost in thought.

Temur and Chinggen.

Thanks to their alliance with the Jin Family of Taiyuan, those two had risen to power on the grasslands. If they were acting suspiciously, there were two possible reasons.

They weren’t satisfied with what they had and were showing greater ambition.

Or…

“What are the chances they’ve joined hands with Dark Heaven—those bastards I could tear to pieces and still not feel satisfied?”

“It isn’t certain yet.”

Peng Cheolyeong added quietly,

“But the circumstances suggest they’ve conspired with Dark Heaven.”

The Thunderbolt Saber King let out a low groan to himself.

*Well, those bastards wouldn’t suddenly pull something like this unless they’d lost their minds. Especially when they know full well that Fire King, that crazy old man, is planted right behind the Jin Family of Taiyuan.*

Everyone knew about the relationship between Fire King Jeok Cheongang and the Jin Family of Taiyuan.

There were plenty of rumors that Temur and Chinggen had even betrayed some of their own people to join hands with the Jin Family of Taiyuan and build their current strength, all because they feared the Fire King.

*And now they’re going to stab him in the back like this? It makes no sense.*

Fire King Jeok Cheongang was hellfire itself.

Hellfire that only died down after turning everything to ash.

The Thunderbolt Saber King was prouder than anyone, but the thought of truly becoming Jeok Cheongang’s enemy was enough to make him uneasy.

*They’ve got someone backing them. No doubt about it.*

The Thunderbolt Saber King kept that thought to himself as he stared intently at his eldest son.

“You must have a reason for thinking that. What’s your evidence?”

“About two years ago, we placed trustworthy people on the grasslands.”

“Informants… You put some thought into it.”

“The situation on the grasslands was still unstable then. We took advantage of the new trade routes opening up.”

Opening the trade routes meant opening the way for people, too.

And after the Seven-Route Army’s campaign, led by the Jin Family of Taiyuan, the new trade routes across the grasslands had carried more than refined ceramics and jewelry.

People.

New kinds of people, never before seen on the grasslands, which had long been a lawless region.

Some of those who filled the vacuum there included informants from the Hebei Peng Family.

“Recently, a few of them sent word that the barbarians on the grasslands are gathering.”

“How many?”

“At least ten thousand.”

“…What? Ten thousand?”

“Father.”

Peng Cheolyeong struggled to speak at the sight of the Thunderbolt Saber King staring at him, eyes wide.

“That’s only the number of troops confirmed so far.”

“…”

For a moment, the Thunderbolt Saber King thought he’d misheard.

Ten thousand. A full ten thousand.

And not some rabble, but the forces of a horse-riding people who’d once thundered across the continent.

Men born in the open fields and destined to die in the saddle.

*And if even that isn’t all of them…*

The Thunderbolt Saber King looked down at his fist, clenched so tightly it had turned white.

He could almost see countless riders charging as one, reins in one hand and bows and lances in the other.

And then, the sight was swallowed by the fury that welled up from deep in his chest.

“Enough!”

Whoom! Crash!

A powerful burst of energy and a thunderous boom rang out together.

The Thunderbolt Saber King smashed the huge iron table with a single punch and rose to his feet, glaring at Peng Cheolyeong—or rather, everyone in the conference room.

“Are you all out of your minds? You were going to decide something this important without me present!”

Rumble.

The force of a giant pressed down from all sides.

The Grand Family Head’s anger shook the entire conference room as if a typhoon had swept through. That was when Peng Cheolyeong abruptly spoke.

“I needed to hear everyone’s opinions before telling you.”

“You fool! The fate of the family is at stake!”

Even with his eldest son standing calm and composed—the very son he’d trusted enough to hand over the position of Family Head—the Thunderbolt Saber King’s anger showed no sign of easing.

Ten thousand already confirmed.

If tens of thousands of barbarians swelled into a massive army and entered Hebei within fifteen days—or even just a few days—there’d be no stopping them.

“How dare you…”

Bitter betrayal. Disappointment.

Peng Cheolyeong’s subdued voice cut into the Thunderbolt Saber King’s ears at that very moment.

“Please forgive me. I couldn’t risk Hebei Peng Family blood being spilled over a hasty decision. That’s all.”

“What are you…”

His whole body had been trembling with rage. Now it abruptly went still.

Only then did the Thunderbolt Saber King sense that something was off. He slowly looked around at everyone’s faces.

And he realized why the words he’d just heard had seemed so familiar.

*What they’re after… isn’t our family!*

The realization struck his mind like a bolt of lightning.

That was right.

If the grassland forces were already heading south toward Hebei, no one would be sitting in this conference room.

The family would have mobilized not only its own forces, but the strength of the Hebei Murim as well, and everyone would be preparing for battle as quickly as possible.

*Then… could it be?*

At a thought that flashed through his mind, the Thunderbolt Saber King’s face went rigid.

“Shanxi. It’s Shanxi Province.”

Peng Cheolyeong quietly nodded at the words, spoken almost as if to himself.

“When will those goddamn bastards set foot in Shanxi Province?”

Someone answered in a heavy voice.

“We expect them no later than seven days from now.”

“Do they—the Jin Family of Taiyuan—know about this?”

“Yes.”

Peng Cheolyeong added quietly,

“They’re already preparing for battle.”

The Thunderbolt Saber King groaned and lifted his head. The blue sky outside the window was now filled with dark clouds.

It was a day with fewer than ten days left until the Double Ninth Festival.
## Chapter artifact 949

# Chapter 949

Everything has a warning sign.

When an earthquake is near, the ground trembles and countless birds take to the sky all at once. Before a typhoon strikes, feather-shaped clouds fill the heavens.

If even natural disasters, as terrible as divine punishment, come with warnings, what more need be said of something done by mere humans?

Just a few days ago, some people had sensed something ominous coming from the grasslands.

And they had sensed it with perfect clarity.

*The nomads. No—the entire grasslands are on the move.*

Inside the vast hall, dimness settling over it, a broad-shouldered man silently studied the map before him.

The enormous map, as large as three or four full-grown men, was packed with the terrain and place names of the entire continent. But his gaze was fixed on only one place.

Shanxi.

The hometown where he had been born and raised all his life, and the land his ancestors had protected.

A little over three hundred years ago, near the end of the war that had drenched the world in blood, a man had arrived here.

His family name was Jin, and his given name was Muryang.

He had been an unwelcome outsider, but when he reached Taiyuan, he laid down a foundation stone and raised his banner. That was the beginning of the Jin Family of Taiyuan.

*He probably never knew. That our family would endure for so many years.*

A little over three hundred years.

An unimaginable stretch of time.

Even gorgeous flowers that made onlookers gasp, even towering trees so tall and grand they awed everyone who saw them, had fallen to the passing winters and the relentless march of time.

But the weeds on the frontier—the Jin Family of Taiyuan—still protected this land.

Blooming in profusion, then broken, shattered, and rising again.

“Rise and decline, flourishing and fading…”

Jin Wikyung murmured the words, then slowly continued.

“Our family’s rise was long ago, and we only barely avoided ruin. So I thought surely all that remained was for us to flourish…but…”

Jin Wikyung smiled bitterly.

“I really did get that wrong. Don’t you think so, too?”

It wasn’t a lament to no one, nor was he talking to himself.

Wipeng, who had held his place like a heavy iron tower, calm as a lake, spoke up.

“Looking at you now, my lord, I’m reminded of the past.”

“The past?”

“It wasn’t long enough ago to call it the past, actually. It was only two years ago.”

“The Mount Heng Sword Sect…”

“That’s right. You looked just like this then, too.”

Wipeng continued in a chilly voice befitting his nickname, Ghost Sword.

“The fight hasn’t even started. Are you thinking of laying down your sword before you’ve even drawn it?”

“Is that how it looks?”

“That’s how it looks to me.”

At the firm answer from his most trusted retainer, Jin Wikyung bit his lip.

He was ashamed of himself for being unable to deny it at once.

And the reality that was keeping him from making a decision even out of a moment’s stubbornness felt bleak.

“I’m…the Lesser Family Head of our family. Countless lives depend on a few words or some small action of mine.”

And it wasn’t only the Jin Family of Taiyuan.

All of Shanxi Murim moved according to Jin Wikyung’s will.

The Jin Family of Taiyuan was unquestionably the foremost power in Shanxi Province, and he was, for all intents and purposes, the Family Head.

Even now, a wave of tens of thousands of men and horses was surging toward this land.

“I’ve already sent a letter through the Shanxi Provincial Office, telling them to evacuate the people around Datong and Saneum. We have to prevent as many needless casualties as we can.”

Datong and Saneum were the districts closest to the grasslands.

They would be the first places trampled by the grassland army after it crossed the border.

“The Mount Heng Sword Sect is no different. It’s not too late to retreat. It’s the only way to avoid being wiped out.”

“Do you really think the Sect Leader will accept that proposal?”

“It’s not a proposal. It’s an order.”

Jin Wikyung continued in a subdued voice.

“She has no other choice. By now, she must have accepted reality.”

Over the past two years, the Mount Heng Sword Sect had grown remarkably under the Jin Family of Taiyuan’s banner.

Lee Seowol, who had become its new Sect Leader as a woman, had proven far more capable than anyone had expected.

If the former Sect Leader—her father, Lee Cheonbaek, the Blood Wolf Sword—had built the Mount Heng Sword Sect through fear and force, she had rebuilt the sect with her characteristic intelligence and leadership, rescuing it from the brink of collapse.

So much so that she had drawn the attention of the world.

But no matter how much the sect had grown, there was no question it couldn’t weather the crisis right on its doorstep.

“Thirty thousand.”

Jin Wikyung looked at Wipeng, his gaze heavy.

“By the time they reach Shanxi Province, they’ll have grown to thirty thousand.”

The past few days had passed with merciless speed.

One day, urgent word arrived that nomads scattered across the grasslands were gathering. Then several Escort Bureaus and merchant houses along the grassland trade routes disappeared.

Their fate was obvious. So were the culprits.

“Their goal is clear. And so is who’s behind them.”

Jin Wikyung knew Temur and Chinggen well.

One of the decisive reasons the two had risen so quickly to become powers on the grasslands was the support they’d received from the Jin Family of Taiyuan.

“Temur is strong, but utterly simple. Chinggen is calculating and cautious, but he lacks the stature for this. Neither of them would ever pull something like this. They don’t have the strength for it, either.”

The age when the nomads of the grasslands had thundered across the continent with bows and lances had long since passed.

The empire they built had vanished without a trace, and the nomads, driven out to vast but desolate plains, had fallen into repeated feuds with their own people and continued to decline.

“Their strength has already been proven. But it’s still not enough to threaten the Central Plains.”

Temur and Chinggen, now called khans, were still just two among the many Great Chieftains of the grasslands.

But what of the Central Plains?

Every province had the Great Nation’s soldiers, numbering anywhere from several thousand to over ten thousand, as well as powerful Murim sects.

A divided grasslands.

A united Central Plains.

The gap between them was far too deep and wide.

The day the nomads carried on their ancestors’ great legacy and ruled the world would never come again.

Not unless another enormous power intervened.

“I’m not afraid of thirty thousand nomads.”

Jin Wikyung glared at the enormous map before him.

As if he were waiting for something hidden to spring out from among its dense lines and characters.

“Dark Heaven. I’m afraid of the power they haven’t revealed yet.”

For the past two years, the Jin Family of Taiyuan had gone from strength to strength.

But amid the days of celebration and cheers, Jin Wikyung had writhed each night beneath the same terrible nightmare.

A nightmare of the dead.

“Kill them!”

“Don’t give up an inch!”

Clang! Clang! Clang!

Eight Spring Gorge.

In that blood-soaked gorge where enemies, allies, and traitors had been tangled together, charging at one another like beasts, Jin Wikyung wandered every night.

“Lesser Family Head, are you all right—? Cough!”

He saw a family retainer who had always greeted him with a smile collapse, spraying blood.

“P-Please, spare me. I beg you. I beg you.”

He passed a Mount Heng Sword Sect martial artist who was dying with his eyes wide open, hurrying to face another enemy.

“Do you know what you—you, the Jin Family of Taiyuan—did to us?!”

He came face-to-face with the traitors who had finally drawn the swords they’d hidden away after waiting for decades.

He crossed swords with them without pause, finally brought them down, and came face-to-face with one man.

“Look around you. What do you think as you watch them die so horribly?”

A beard soaked red with blood.

A dry gaze and voice.

The Head Elder, who had surely died long ago, spoke to his own bloodline, his breath cold.

“If you’d been a little more careful. A little wiser…could you have prevented a tragedy like this?”

Those weren’t words he remembered hearing.

Of course not.

They were the questions Jin Wikyung asked himself.

Jin Wikyung knew.

The Head Elder in his nightmare, every word he spoke—it all came from Jin Wikyung himself.

But even knowing that, the nightmare never stopped. It kept repeating.

Even now.

“My lord.”

At Wipeng’s voice, which suddenly pierced his ears, Jin Wikyung slowly blinked as if he’d just woken up.

Only then did he realize his body was drenched in cold sweat.

“…Damn it. Look at me.”

Jin Wikyung let out a short curse, then gave a bitter chuckle.

It was ridiculous.

There he was, trembling like a drowned rat.

And the fate of Shanxi Murim—no, of all Shanxi Province—rested in the hands of this pathetic man, who could barely breathe under the pressure closing in from every direction.

The only small comfort was that someone who had been by his side for so long was still there.

“May I say something, my lord?”

His voice rang out through the brief silence.

Wipeng continued without waiting for Jin Wikyung’s answer.

“The enemy is undoubtedly strong. If the thirty thousand nomads are joined by the forces of Dark Heaven they’ve yet to reveal…then, as you’ve judged, something irreversible may happen.”

“Even if we join forces with the government, we can’t be sure we’ll win. Without reinforcements, we couldn’t handle them even if we threw the full strength of Shanxi Province into the fight.”

Jin Wikyung added bitterly,

“Even if fortune smiles on us and reinforcements arrive in time, their numbers will be woefully inadequate. That’s only natural. If I were in their place, I’d never leave my family unprotected, either.”

A feint to the east, strike in the west.

The vast grasslands bordered not only Shanxi Province, but Liaoning, Hebei, and Shaanxi as well.

The moment the great army heading south for Shanxi Province turned its horses around, the sects and families that had sent reinforcements would become new targets.

And as long as Dark Heaven possessed the strange dark art of the Moving Formation, no one could easily leave their sect or family undefended.

They had things to protect, too.

“I’m thinking of abandoning Shanxi and heading to Henan. As long as our people survive, our family won’t disappear.”

This wasn’t the best choice, or even the second-best.

It was the lesser of two evils, to avoid the worst.

And Wipeng understood Jin Wikyung’s desire to prevent as many people as he could from being sacrificed.

“If that is your command, my lord, I will obey.”

“Wipeng. You…”

“But my lord, do you remember?”

Wipeng continued calmly.

“Two years ago, someone said that once you start retreating, you’ll keep backing away until you trip over a rock and fall.”

“...!”

“I know. I know the enemy is strong. And I know what moved you to make this decision. But…”

After taking a deep breath, Wipeng clasped his hands toward the lord he trusted and followed.

“Our Jin Family of Taiyuan has grown stronger. No—Shanxi Murim has grown stronger.”

Without hesitation, Wipeng turned and opened the tightly shut door.

The door slid open softly.

At that moment, Jin Wikyung saw them.

Beyond the slowly opening door, countless people waited, armed and ready.

At their head stood familiar faces.

“Lee Seowol of the Mount Heng Sword Sect. I’ve come to fight against the foreign enemy.”

Clang! Clang! Clang!

Lee Seowol, dressed in martial attire.

Behind her, three hundred martial artists of the Mount Heng Sword Sect drew their weapons and drove them deep into the ground.

“Sect Leader Lee. What in the world is all this…?”

Jin Wikyung couldn’t finish his sentence.

He had seen the dozens of Sect Leaders and Family Heads who had sworn allegiance beneath the Jin Family of Taiyuan’s banner two years ago.

And among them, all standing with their own weapons and cold eyes, was someone who had just appeared.

“What is there to think so hard about?”

The young man’s voice was rough and awkward, as if he’d forgotten how to speak for a long time.

Wearing clothes like rags, he smiled at Jin Wikyung.

His gaunt cheeks were hollow enough to stand out.

“Hyung.”

“...!”

At the sight of his younger brother, who had finally emerged into the world after a long seclusion, Jin Wikyung closed his eyes, unable to contain the surge of emotion rising within him.

And in the instant of darkness, he recalled the voice of his youngest brother, who wasn’t there, speaking through Wipeng just moments ago.

“Once you start retreating, you’ll keep backing away until you trip over a rock and fall.”

He couldn’t be sure which choice was right or wrong.

But the road ahead was decided.

Step.

Jin Wikyung began to walk.

Toward the people waiting for the Lesser Family Head of the Jin Family of Taiyuan.

Toward the dark future, already thick with the stench of blood.

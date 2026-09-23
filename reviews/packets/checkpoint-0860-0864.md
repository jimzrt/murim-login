# Checkpoint Review — 860–864

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

# Chapters 860–864

## Plot

Hong Jin explains that the Great Nation’s founding emperor ordered Jiangsu’s Murim sects to relocate; the Maoshan Sect and other holdouts were destroyed by the Imperial Guards, leaving the region without sects. As the party reaches Suzhou, Jin Taekyung understands why Hong Jin needs him to protect Prince Shangshan. Jeong Hogun announces that Shangshan is to meet the Emperor that day.

At the imperial palace, Hong Jin reveals his past with the East Depot, and an old eunuch confronts him for bringing outsiders inside. Commander Baek Yeon arrives and promises the prince’s guests will be safe. Shangshan asserts his authority after Taekyung advises him to speak plainly, but Baek announces the Emperor has postponed the audience until the next day.

Baek tests Taekyung’s strength and executes a subordinate who drew his sword before Shangshan. He later orders Jeong Hogun to keep the party under apparent surveillance while leaving openings for someone to approach. Baek says an earlier assignment has not succeeded, then orders that nobody—including Taekyung—leave the palace. Privately, he reflects that Shangshan is the Emperor’s only younger brother and the sole direct imperial relative to survive a brutal power struggle, and sees the grown prince as more dangerous than before.

## Continuity

- Prince Shangshan and his party are inside the imperial palace under Baek Yeon’s escort. Baek has ordered that nobody leave.
- The Emperor postponed Shangshan’s audience until the next day without giving a reason; his intentions toward the prince remain unclear.
- Baek ordered Jeong Hogun to surveil the party while leaving apparent openings for someone to approach.
- Baek’s earlier assignment has not succeeded; its nature and target remain unstated.
- Shangshan will not seek Baek’s punishment because Baek serves the Emperor, not him.
- Hong Jin was formerly part of the East Depot. His history with the old eunuch, including an absence of eleven years and nine days, remains unexplained.

## Translation Decisions

- Render 동창 as “East Depot,” 금의위 as “Embroidered Uniform Guard,” and 금위군 as “Imperial Guards.”
- Render 금의위 지휘사 as “Commander of the Embroidered Uniform Guard.”
- Render 황도 as “imperial capital,” 전음 as “Sound Transmission,” 내성 as “Inner City,” and 호패 as “identity tag.”

## Durable state

{
  "active_continuity": [
    "Prince Shangshan and his party are inside the imperial palace under Baek Yeon’s escort; Baek has ordered that nobody leave.",
    "The Emperor postponed Prince Shangshan’s audience until the next day without giving a reason.",
    "Baek Yeon ordered Jeong Hogun to surveil the party while leaving openings for someone to approach.",
    "Baek Yeon’s earlier assignment has not succeeded; its nature is unstated.",
    "Shangshan will not seek Baek Yeon’s punishment because Baek serves the Emperor, not him."
  ],
  "continuity_sources": [
    863,
    864
  ],
  "open_questions": [
    "Why did the Emperor postpone Prince Shangshan’s audience, and what does he intend for the prince?",
    "What was Baek Yeon’s earlier assignment, and who has so far eluded it?",
    "Who is meant to approach Shangshan’s party through the surveillance gaps?",
    "What happened between Hong Jin and the old eunuch, and why did Hong Jin leave the East Depot?"
  ],
  "safe_through": 864,
  "temporary_decisions": [
    "Render 동창 as “East Depot.”",
    "Render 금의위 as “Embroidered Uniform Guard” and 금위군 as “Imperial Guards.”"
  ],
  "version": 1
}

## Reading copies

## Chapter artifact 860

# Chapter 860

Murim martial artists were like weeds.

They could be found in dark back alleys and on bright main streets, surviving stubbornly in the depths of the mountains and even somewhere along the vast Yangtze.

Perhaps that was why the world they lived in came to be called Murim—the forest of martial arts.

Ruffians who ignored common sense and the law.

But even among the Murim martial artists who had carved out a forest of their own with sharply honed spears and blades, not all of them could grow into towering trees.

In the vast forest that was Murim, only the Nine Sects and One Gang, the Five Great Families, and a few forces that hadn’t reached their heights but had established themselves as the rulers of their respective provinces could be called towering trees.

*The Jin Family of Taiyuan was one of them, too.*

I thought to myself as I looked out the window.

Merchants in the middle of hawking their wares. A woodcutter passing by, sweating buckets under a back-breaking load of firewood. Ordinary commoners and well-dressed dignitaries in silk.

The world outside was full of all sorts of people, the stuff of any society. But one particular sort I’d seen just about everywhere until now was nowhere to be found.

“You can’t find any, can you?”

“Pardon?”

“Murim martial artists. Ones like Young Master Jin.”

Hong Jin had read my thoughts exactly. His face, powdered white, broke into a smile.

“I thought I’d warn you before you waste your energy looking. They’re hard to find in Jiangsu Province. That’s just the kind of place this is.”

“I’ve heard something to that effect… Is it because we’re so close to the imperial capital?”

“That must have something to do with it. They couldn’t let those ruffians run wild near the imperial capital, where the Son of Heaven resides.”

Hong Jin glanced at Hyuk Mujin and me, then added,

“Just so you don’t misunderstand, that’s how the powerful see it. The higher you climb, the more you care about appearances.”

It sounded like he was being polite in case I took offense, but there was no need. I could understand the reasoning to a point.

Well, to be precise, there were plenty of Murim martial artists who went too far.

But that didn’t explain everything just because we were close to the imperial capital.

Hyuk Mujin’s sudden question came from the same line of thought.

“Then what about the Nangong Family, sitting pretty in Anhui? It’s not all that far from the imperial capital, either.”

“Before I answer that, let me ask you the reverse. What’s left among the provinces next to the imperial capital, apart from the Nangong Family in Anhui?”

“Besides the Nangong Family… Well, that would be…”

Hyuk Mujin struggled to find an answer, and Hong Jin let out a quiet chuckle.

“Nothing. Jiangxi, Fujian, Jiangsu, and Anhui. Of the four provinces surrounding Zhejiang, where the imperial capital is located, the Nangong Family is the only famous Murim sect. Though there are exceptions.”

“Exceptions?”

“Yeah. How should I put it? If you judge by history alone, they seem like a real threat. But the imperial court would feel uneasy about going out of its way to provoke them. Martial artist Hyuk, you don’t know of any?”

Hyuk Mujin frowned and thought for a moment before answering.

“If I look into it carefully, I could probably name a few sects. But is there really one like that? Compared to the Nangong Family in Anhui, they’d be worth less than a horse’s balls.”

“Martial artist Hyuk, I don’t have any balls.”

“Ah! I’m sorry.”

“No, you don’t have to apologize that much. It just felt strange hearing it. Anyway, you really can’t think of one?”

“No. Of course not.”

Just then, I smacked Hyuk Mujin on the back of the head, the idiot who’d answered so confidently.

*Whack!*

“The Fire Gate Clan, you asshole! The Fire Gate Clan!”

“Ugh! Ow!”

“Mount Jiuhua in Anhui Province! Three hundred years of history! You saying the Fire Gate Clan’s worth less than a horse’s balls? You think the Fire Gate Clan’s a bunch of fucking pushovers?”

For the record, I was in my second year as a member of the Fire Gate Clan and diligently working my way through the heir-apparent training program.

As I beat Hyuk Mujin with my burning love for the company as fuel, Hong Jin spoke quietly.

“Um, Young Master Jin, sorry, but…”

“Oh, sorry. You don’t have those either.”

“That’s not what I meant. I was worried His Highness would wake up. And not all eunuchs are missing both. I believe I told you that once before.”

“My apologies again. I forgot you were only missing one.”

“……Fine. Please be careful. Keep your voice down so His Highness doesn’t wake.”

With an expression that had given up halfway, Hong Jin looked at Prince Shangshan Zhu Bao, sleeping peacefully, and continued.

“Anyway, Murim martial artists haven’t been able to run rampant in the provinces bordering the imperial capital—not just Zhejiang. Practitioners of the so-called demonic, heterodox arts couldn’t run rampant, of course. Even the Nangong Family—a towering tree of the orthodox faction and one of the Five Great Families—had to call on every connection it had among high-ranking officials.”

“It was that bad?”

“Yes. It happened right after the Great Nation was founded, so it was a long time ago. But things have stayed that way ever since. No matter how rough Murim martial artists were, they probably didn’t want to end up like the Maoshan Sect.”

“The Maoshan Sect?”

The name sounded familiar.

It had come up now and then in the many wuxia novels I’d loved to read back in school.

It wasn’t a major sect like the Nine Sects and One Gang, which appeared in every wuxia novel. It was more of a minor one, but it wasn’t hard to remember a few things about it.

More importantly…

“You mean the Maoshan Sect? The one famous for its sorcery rather than martial arts?”

“Hm? You didn’t know? It was right here in Jiangsu Province.”

It wasn’t as if I were some old master from a previous generation like the Fire King, who’d lived for over a hundred years. How was I supposed to know every little thing that had happened around the time the Great Nation was first established?

Still, what Hong Jin had just said was enough to make me pause.

*It was in Jiangsu Province…*

Past tense, not present.

Then I recalled how Hong Jin had mentioned the Maoshan Sect’s “fate,” and the fact that I’d never once heard its name during all my time in Murim.

The pieces fell into place.

“It disappeared. A long time ago.”

“Correct.”

Hong Jin snapped his fingers cheerfully and continued.

“The Great Nation’s first emperor, the Taizu, chose this place as his capital when he founded the country. Nanjing, in Jiangsu Province, had been the seat of six dynasties in the past. It was the imperial family’s first home.”

“So what happened?”

“With a new unified dynasty on the rise, could they really let the ruffians of the martial world run wild? Once the imperial edict went out, everything moved at lightning speed. Most of the sects in Jiangsu Province moved elsewhere. You’re starting to see where this is going, aren’t you?”

He’d said most of the sects, not all of them.

Guessing what came next, I murmured,

“The Maoshan Sect didn’t.”

“Right. A small number of Murim sects, including the Maoshan Sect, refused the imperial order to leave Jiangsu and held on to their headquarters. They say the Maoshan Sect was big enough to rival the Nine Sects and One Gang back then, so it could afford to be stubborn. But…”

The Great Nation’s first emperor had risen from the dirt and opened a new era—but he hadn’t been as magnanimous as the Maoshan Sect had thought.

“According to the records that remain, a hundred thousand Imperial Guards were dispatched. They killed and burned everything—not a single blade of grass or ant left behind.”

“……!”

“……!”

“That was how the Maoshan Sect was wiped out. And after that, no Murim sect ever established itself in Jiangsu again. Not even after His Imperial Majesty moved the capital to Zhejiang.”

Jiangsu wasn’t just an old imperial capital.

It was a Murim-free zone the Imperial Guards had already swept clean, the imperial family’s front yard, still steeped in the first emperor’s legacy.

And what that meant was perfectly clear.

*We can forget about asking for help.*

Until now, we’d been able to find help just about anywhere. Every province had one or two sects that had put down roots like the local old-timers, and most of them were friendly toward Jeok Cheongang or the Murim Alliance.

Even Nanman, practically the middle of nowhere, and our last journey, when we’d had to keep charging ahead without looking back, had been like that.

The Nanman Beast Palace had old ties with the Fire Gate Clan. And the Lower District Sect and the Beggars’ Sect, both under the Murim Alliance, had left food and fine horses along the route for us, even while we were on our way to Jiangsu.

But not from here on out.

If things were this bad in Jiangsu, the old imperial capital, what would Zhejiang, the current one, be like?

*An absolute Murim-free zone. Maybe they’ve got the odd neighborhood martial arts school.*

If the worst happened to us, what we’d need most of all was force.

But there probably wasn’t a group anywhere nearby with the level of strength I had in mind.

Forget the Nine Sects and One Gang or the Five Great Families. This was more like a neighborhood Taekwondo school.

*No, in this case, a tai chi school.*

Just picturing a mob of people in colorful matching uniforms coming to our aid made my eyes swim.

“We’ve come to help!”

“What sect are you from?”

“Kyunghee Tai Chi!”

“Oh, I see… So, if you don’t mind me asking, what level of martial arts have you reached?”

“I’m a black belt!”

“Ah…”

“We came from the Zhejiang Kendo Association, too!”

“Ahhh…”

I could only hope they weren’t all from the kids’ class.

It was bad enough to fall for that bait-and-switch pitch: sign up for the martial arts school and get three million mesos—no, three taels in iron coins. If those kids wound up facing the Imperial Guards too, how could I ever look their parents in the eye?

“Please, at least the adult class. The adult class in the afternoon…”

“Young Master Jin. Young Master Jin?”

I’d been muttering in a daze, but Hong Jin’s call snapped me back to my senses.

“Ah.”

“Are you all right?”

“Yes, I’m fine.”

“Really? You’re sweating like it’s pouring rain.”

“I just had a bad thought for a moment.”

At my answer, Hong Jin spoke with a shadow over his face.

“I’m starting to feel bad for calling you along. But I couldn’t help it. You were the only person I could think of.”

“No. I understand.”

If all Hong Jin wanted was someone he could trust, the Jin Family of Taiyuan was close enough to provide support.

But, coldly speaking, there was no one in the Jin Family of Taiyuan as strong as me.

No—the right person, someone who could meet every requirement, would be hard to find anywhere under heaven.

What Hong Jin truly wanted was not only someone he trusted, but a powerful martial artist who could save Prince Shangshan Zhu Bao from any threat.

*The Murim Alliance is there, but it would’ve been too risky to move a Supreme Peak master Hong Jin could trust other than me on such short notice.*

Even a rock on a beach left a mark when it moved.

They’d probably already deployed troops all over the land in preparation for a showdown with Dark Heaven. If they pulled away even one force as powerful as a Supreme Peak master, the gap would be enormous.

Given the importance and timing of the matter, there probably wasn’t a more dependable card than Jeok Cheongang and me, fresh from completing our mission in Nanman.

*This could eat away at the very foundations of the nation.*

I let the words I couldn’t bring myself to say drift through my mind. Then a voice that still sounded strange no matter how many times I heard it came from outside the window.

“We’ll reach Suzhou soon.”

His voice was as hard as a rock. The man held the rank of Thousand Captain in the Embroidered Uniform Guard. Jeong Hogun looked at me through the narrow gap in the window and continued.

“Inform His Highness Prince Shangshan. He will pay his respects to His Imperial Majesty sometime today.”
## Chapter artifact 861

# Chapter 861

Jeong Hogun hadn’t been lying when he said they would reach the imperial capital today.

The procession passed through Nanjing, the capital of Jiangsu Province and the former imperial capital, and finally arrived in Suzhou. At the border crossing into Zhejiang Province, they came face-to-face with a force of soldiers.

“We’ve been waiting for you, Commander.”

Gleaming eyes shone between their full suits of iron armor and helmets.

Each man radiated a heavy aura. There were nearly a thousand of them, and on the golden banners fluttering in the wind, the dragon that symbolized the imperial family writhed as if alive.

The Embroidered Uniform Guard.

The Emperor’s loyal hounds—who answered to only one person in this world, the Son of Heaven—saluted their superior, Jeong Hogun, then faced the young prince who carried the noble blood of the imperial family.

“His Highness Prince Shangshan is here. Pay your respects.”

“Long live the prince! Long live the prince! Long, long live the prince!”

Watching the Embroidered Uniform Guard shout in unison without even dismounting, Hong Jin found himself wondering:

How many of them truly meant those words?

No—did even one?

Hong Jin already knew the answer. He swallowed a bitter smile.

*They and I are nothing more than beasts. What matters is the will of the master who raises those beasts.*

That was right. The Son of Heaven was supreme, above all others, and could decide who lived and died.

Nothing could stand in the way of his will.

Not even the blade that had narrowly missed the young prince amid that terrible purge more than a decade ago.

Nor could anything stop this carriage as it headed toward the Son of Heaven’s returning blade.

“Pick up the pace. The imperial capital is just ahead.”

As the sun began to sink, the carriage raced like the wind.

After hiding their identities in worn martial artists’ clothes for thousands of li, Jeong Hogun and the Embroidered Uniform Guard under his command now wore dazzling brocade and armor befitting their name. They advanced like a wave, imperial banners held high.

Like victors returning with an enemy general in chains.

“Make way!”

Nothing could stand in the way of a thousand members of the Embroidered Uniform Guard.

The commoners bowed low, their eyes mixed with fear and awe, as the procession led by the young prince passed through the gates, flung wide open before them.

In just half a day, they had traveled along the great roads and waterways cleared exclusively for them. At last, Hong Jin saw it.

A massive wall he’d thought he would never see again in his lifetime. A wall he had sworn never to return to, if only for the sake of the young prince he served.

*The imperial capital…!*

Hong Jin forced down the sigh that nearly escaped him.

He could see what lay out of sight. He could hear what no longer made a sound.

The dragon’s lair crouched behind those towering walls. The countless screams that had echoed endlessly around a single throne.

They were horrific fragments of the past, lodged deep in Hong Jin’s mind—and the history that had made one man the ruler of the continent.

*“I’ll spare you. Just this once.”*

At the sudden memory of someone’s cold voice ringing in his ears, Hong Jin clenched his teeth without realizing it.

*It won’t go as Your Majesty wishes. Not this time.*

The sunset, beginning far to the west, stained the walls of the imperial capital.

* * *

Hangzhou made a fine first impression.

It had an abundance of goods carried by canal throughout Zhejiang Province, and its scenery was beautiful.

The wide plains we’d passed on the way were covered in every kind of grain, rippling like golden waves. Smiles never left the people’s faces.

*They say it’s the most beautiful city under heaven.*

Something I’d once heard in passing. And it was absolutely true.

Maybe that was why they’d abandoned a great city with Nanjing’s long history and moved the capital to Hangzhou.

There was just one problem: this beautiful city was a lot more threatening than I’d expected.

Clank. Clank.

The cold scrape of weapons.

Whichever way I turned, I saw soldiers. And not the half-trained grunts I was used to—these were elite troops, fully armed.

Even the easygoing Hyuk Mujin had lost his smile and said,

“Captain. This is a bit… much, isn’t it?”

Normally, I’d have shot back at him out of habit. But this time, even I had to agree.

*Why are there so many?*

It wasn’t just a lot. There were a downright disgusting number of them.

There were so many I was starting to wonder if Zhejiang Province’s specialty wasn’t Longjing tea but Imperial Guards.

“Is security always this tight?”

Hyuk Mujin wasn’t the only one who’d lost his smile after we entered Hangzhou.

Hong Jin answered my question in a voice so stiff it hardly sounded like him.

“As the imperial capital, it’s always been well guarded. Of course, it’s never been like this before.”

“Then…”

“They must have received some sort of order. And it’s probably… connected to us somehow.”

Hong Jin licked his red-painted lips and murmured,

“I had my suspicions, but this welcome is more intense than I expected.”

For a moment, I pictured a hundred thousand soldiers pointing their spears and blades at us. Then I shook my head.

*That’s unlikely.*

If they’d wanted to kill him that easily, Prince Shangshan Zhu Bao wouldn’t have made it out of Shanxi Province.

I didn’t know exactly why the Son of Heaven had sent the Embroidered Uniform Guard to bring his young brother here. But one thing was certain: the prince would be dealt with in a way the emperor could publicly justify.

That was the nature of an emperor.

*Besides, the emperor’s public image is already bad.*

Was it for nothing that people said the people’s will was the will of Heaven?

The nomadic people of the steppe, who had ruled the continent before the Great Nation, had fallen alongside the people’s waning support.

The emperor ruled the people, but without the people, there could be no emperor.

In that sense, the public’s view of the current Son of Heaven was quite negative.

*A capable but ruthless emperor.*

I’d heard it now and then in Murim, and learned more about him through quiet conversations with Hong Jin on the way here.

The current emperor had built up an impressive record of military service from a young age, putting down several rebellions and uprisings by foreign peoples. He was also praised as a ruler who left no detail unattended in governing the regions under his charge.

Hong Jin said that if the emperor had been born the late Emperor’s eldest son—or if his eldest brother, the Crown Prince, had been even a little less capable—he would naturally have inherited the throne.

*But things hadn’t worked out that way.*

Before becoming emperor, he’d been nowhere near the line of succession.

He had three older brothers. And his eldest, who had naturally become Crown Prince under the principle of primogeniture, was every bit as outstanding as he was—perhaps even more so, depending on whom you asked.

A fine man who treated people with kindness and integrity regardless of their status, and showed every quality needed to lead the Great Nation.

Hong Jin had described the Crown Prince of that time as:

*A Son of Heaven prepared for the throne.*

The long wars had ended long ago.

The seeds of rebellion scattered across the land and the foreign peoples who had constantly eyed the Great Nation had all been uprooted.

The Great Nation had been established on firm foundations. What it needed now wasn’t conquest, but stability. With his perfect orthodox lineage and all the qualities a ruler could need, the Crown Prince was a successor prepared in every respect.

That was until the Emperor, then the imperial family’s fourth son, had drawn his sword from the shadows—already pushed far from the line of succession.

Clip-clop.

The sound of hooves rang out unusually clearly, snapping me out of my thoughts. I looked around.

*Where are we?*

The answer came quickly.

The carriage had stopped, and beyond the Embroidered Uniform Guard packed tightly around us stood enormous buildings the likes of which I’d never seen in Murim.

They were so tall they reminded me of modern skyscrapers, and so richly and classically decorated that those skyscrapers couldn’t compare. They could only mean one place.

*The imperial palace.*

The dragon’s lair, and the center that kept the enormous gears of the world turning.

I stared silently at the entrance to the palace, so overwhelming that even the sight of it through the narrow gap in the window was enough to make me feel small. Hong Jin leaned close and whispered, barely above a breath.

“Young Master Jin, I’ve held it in until now, but… don’t you think it’s time to tell me?”

The moment he said it, I knew what he was asking.

The others besides Hyuk Mujin and me.

Hong Jin wanted to know where our other helpers were—the ones who still hadn’t shown themselves. I already had my answer.

—Don’t worry. You’ll find out soon enough.

It wasn’t the answer he’d hoped for. Hong Jin furrowed his brow slightly, but didn’t complain.

I’d traveled all this way, without stopping, to help them.

If we couldn’t even trust one another in a situation like this, the anxiety and danger would only grow.

And with that in mind, I couldn’t help asking him something, too.

—How do you know all of this?

It was a question I’d been carrying for quite some time.

Prince Shangshan Zhu Bao might have been a prince in name only, but he was the only direct imperial relative to have survived the horrific struggle over the throne—and a prince who ruled a fief.

I’d long suspected that Hong Jin, the prince’s trusted aide, couldn’t be an ordinary eunuch. But the breadth of his knowledge and the way he faced the Embroidered Uniform Guard, feared wherever they went, without a hint of unease exceeded even my expectations.

I had to ask him directly, even if it meant asking like this.

—Since I’ve risked my life, I deserve an answer to this question. Right now.

Clunk.

At my firm Sound Transmission, Hong Jin stared at me in silence. Then, without warning, he flung open the carriage door.

Looking toward a group of people descending the impossibly high stairs that led down from the imperial palace, he spoke.

“Young Master Jin, I’ve told you why I decided to become a eunuch, haven’t I?”

I nodded.

Back when Hong Jin and I first met in Shanxi Province, he’d briefly told me about his past.

“I hated being poor, and I wanted to save my family. But I didn’t have many options. No—at the time, I only had one.”

Hong Jin continued slowly.

To get what you wanted, you had to sacrifice something else.

So the poor boy, unable to overcome his hunger, became a eunuch and chose a new name for himself.

“Hong Jin. I wanted to reach the great waters. To leave that stinking sewer behind and go somewhere wide and clear, like the sea.”

It hadn’t taken long for that wish to come true.

The young eunuch had escaped poverty and developed ambitions he’d never had before. He also had the ability to fulfill them.

And his usual thoroughness and cool judgment soon caught the eye of the late Emperor.

“One day, the late Emperor summoned me and told me there was a place where my talents could be put to good use.”

Hong Jin continued in a clear voice.

“Young Master Jin. Have you ever heard of the East Depot?[^1]”

“……!”

[^1]: The East Depot was an imperial secret-police agency in Ming China.
## Chapter artifact 862

# Chapter 862

The East Depot.

Anyone who’d read a few martial arts novels knew that name.

If the Nine Sects and One Gang and the Five Great Families showed up like clockwork in those stories, then the imperial court had the East Depot, which stood alongside the Embroidered Uniform Guard as its other great power.

And Hong Jin was a member of that very East Depot.

My mouth fell open before I even realized it.

“The East Depot? The one I’m thinking of?”

“There’s only one East Depot in the world, Young Master Jin.”

“No, I mean, it actually exists?”

“……Is there a fake East Depot, then?”

“Ah. That’s not what I meant.”

I hadn’t known the East Depot really existed.

It hadn’t been that long since I’d learned the Embroidered Uniform Guard was real, either.

The endless incidents and disasters in Murim kept me busy enough. Who would’ve expected to suddenly get tangled up with the imperial court like this?

*Still, if Hong Jin really did come from the East Depot, then some of the things he’s shown me make a lot more sense.*

Newly astonished, I looked at Hong Jin.

I didn’t know the details, but the East Depot’s influence couldn’t be far behind the Embroidered Uniform Guard’s.

At first, I’d thought he was just a eunuch who’d been a bit of a tough guy in his youth. Now that I’d heard his story, I could almost picture him hawking up phlegm in the palace corridors.

Hyuk Mujin must have had a similar thought. He’d been glancing sideways at Hong Jin, and now he whispered in a voice barely above a breath.

“Captain. This is no ordinary eunuch.”

“……Please, just shut your mouth.”

“It’s fine. He can’t hear me.”

“Sorry, but I can hear you just fine.”

At Hong Jin’s sudden reply, I answered quickly.

“I didn’t say anything. That bastard did.”

“Gasp. Captain!”

This was no time to go soft. I shook off Hyuk Mujin’s hand as he grabbed my sleeve and snapped at him.

“Apologize this instant, you bastard. You’ve got nothing but a pair of balls to your name, and you dare say that?”

“I’m sorry. I’m truly sorry.”

“Beta-male behavior: runs his mouth without thinking, then gets dragged off by the East Depot.”

“I’m sorry! I’ve committed a crime worthy of death!”

“Beta-male behavior: commits a crime worthy of death, then actually dies.”

“No! Please spare me, Comrade Hong! I have tiger-like parents and a rabbit-like younger sibling!”

Whoa, that startled me. For a second, I thought we were in North Korea.

Hyuk Mujin was facedown, wailing like a Communist Party member caught in an ideological purge and dragged off to the Aoji coal mines. Hong Comrade—or rather, Hong Jin, Deputy Military Commissioner of Shanxi Province—watched him with a thoroughly unimpressed look and heaved a sigh that seemed to come from the depths of the earth.

“Anyone would think I was the Grim Reaper. Stop making a spectacle of yourself in front of His Highness Prince Shangshan and get up. There are already plenty of eyes on us. At this rate, I’ll die of embarrassment.”

Very sadly, Hong Jin was right.

The Embroidered Uniform Guards were staring at us like they couldn’t believe what a bunch of idiots we were. Prince Shangshan, who’d just woken up and was still groggy, had his eyes wide as he asked me,

“Is that man truly known by the sobriquet Tenfold Man?”

I hesitated for a moment, then answered,

“Something like that.”

It wasn’t wrong.

Tenfold Man and Tenfold Beta Man were only one character apart, after all.

*Though their meanings are complete opposites.*

I held my tongue to protect the young prince’s innocence. Just then, a group of people came down the endless staircase—long enough to make me wonder if it had been built to torture subjects—and stopped in front of us.

Or, more precisely, they knelt before Prince Shangshan Zhu Bao.

“We pay our respects to His Highness Prince Shangshan.”

“A thousand years! A thousand years! A thousand thousand years!”

They wore official robes made of black silk, and their ages varied widely.

Some looked barely twenty, at most; others were old men with deeply wrinkled faces.

But their robes weren’t the only thing they had in common. I realized at once.

*Eunuchs.*

No doubt about it.

Every one of them had a face powdered white and lips painted red. Their voices were neither a woman’s nor a man’s, and their small frames showed even through the loose fit of their robes.

And yet—

*They’re strong.*

Martial power wasn’t decided by the size of your body.

There was more to people than what you could see.

I could feel the immense energy coiled inside their small frames. At the same time, I recalled the name of the organization I’d just heard.

No—I found myself muttering it aloud.

“The East Depot?”

Rustle.

A long hem brushed the ground.

At the head of the eunuchs, an old man who’d bowed deeply to Prince Shangshan raised his head and looked at me.

His strange gaze gave nothing away.

The old eunuch stared at me for a brief moment, as if he could see right through me, then spoke to Hong Jin beside him.

“It’s been a long time, Hong Cheophyeong. Or should I call you Deputy Military Commissioner now?”

Hong Jin answered calmly.

“Call me whatever you like. But you’ve gotten even older since I last saw you.”

Though there was a considerable age difference between them, Hong Jin spoke to him casually and without deference.

That meant Hong Jin’s position back then must have been quite high. The old eunuch’s wrinkles deepened further.

“You’d be wise to watch your words. The landscape isn’t the only thing that’s changed in the last ten years.”

“Things can only change so much. And your brain must have gone stiff with age. It’s been eleven years and nine days, to be precise.”

“You remember that exactly?”

“There are some things you can’t forget, even if you try.”

“And yet you seem to have forgotten rather a lot.”

The old eunuch continued in a chilly voice.

“How dare you bring an outsider into the imperial palace without permission—one of those ruffians from the martial world, no less. Just because you left the imperial court, have you forgotten its rules as well?”

“Times really have changed. Someone like you dares to question something His Highness Prince Shangshan permitted? And…”

Hong Jin continued in a clear voice.

“If everything had gone according to the rules, things wouldn’t have come to this.”

“……!”

“……!”

Hong Jin’s words had a hard edge beneath them, and the air around us froze.

Just as he said, if everything had followed the rules, the current Son of Heaven wouldn’t be sitting on the throne, and Prince Shangshan Zhu Bao’s situation would be very different.

Hong Jin had alluded to that fact, and the reaction of the Embroidered Uniform Guards and the East Depot eunuchs—the Son of Heaven’s own hands and feet—was settled from the start.

Shing.

The cold scrape of a blade reached my ears.

I moved without the slightest hesitation.

Whoosh.

One step.

Space disappeared. The wind fell silent.

In time that seemed to pass slowly, I reached out and pressed down on the hand of someone gripping a sword hilt tightly.

To send the blade, not even halfway drawn, back where it belonged.

Click.

At the soft sound, time—which had slowed for a moment—returned to normal. The wide eyes of an Embroidered Uniform Guard I didn’t know seemed to whisper:

*How?*

But I didn’t bother answering, nor did I knock down my opponent, who’d already gone rigid as a statue.

Then again, even if I had answered, he might not have heard me.

The wind, catching up with my figure after it had moved like a flash of light, whipped in every direction.

Fwoosh!

Clothes billowed in the burst of air.

Dust that had lain in layers between the bluestones, fitted neatly into the ground like a work of art, rose and scattered on the wind.

Like sleet.

In that breathless silence, without a single cough, I spoke calmly.

“Who the hell told you to draw your weapon? With a child—no, with His Highness Prince Shangshan watching, no less.”

“……!”

“……!”

“Let’s not make this any bigger than it has to be. That’s best for everyone, isn’t it?”

I meant every word.

Taking care of the men in front of me wouldn’t be difficult, but doing that at the entrance to the imperial palace could send things spiraling into the worst possible situation.

And my sincere words reached someone I hadn’t expected.

“Your manner is disrespectful, but you’re not wrong.”

“……!”

When had he—

I turned around, feeling as if someone had dumped a bucket of cold water over my head.

About thirty *jang* away, halfway down the endless staircase leading up to the imperial palace, stood a middle-aged man.

*I didn’t sense him at all.*

I’d been constantly honing my Qi Sense so I wouldn’t have to rely on the System as much as possible.

There was no denying the distance between us was considerable, but the fact that I hadn’t sensed him was proof that the middle-aged man’s martial prowess was no less than mine.

*No. It might even be greater.*

I fixed my gaze on the man, feeling my mind grow cold.

Instead of using lightness skill, he came slowly down the stairs with the leisurely gait of a carefree man. He smiled at me and spoke.

“You’re reckless, like the other ruffians of the martial world, but not as ignorant. Jin Taekyung of the Jin Family of Taiyuan.”

It wasn’t especially surprising that the middle-aged man already knew who I was.

I’d expected as much the moment I stepped in front of the Embroidered Uniform Guard.

And just as he knew who I was, I had a vague idea of who he was, too.

Even if he hadn’t been wearing a gleaming golden suit of armor, the shout that rang out the next moment would’ve told me.

“Loyalty!”

“We pay our respects to the Commander!”

Led by Jeong Hogun, the Embroidered Uniform Guards under his command struck their chests and shouted their military salute as one. It was quite a sight.

So was the middle-aged man approaching through a sea of flashing gold.

Step. Step.

His soft footsteps broke the silence that followed the shouts.

He was neither large nor small, but somehow seemed like a giant. He stopped only when he reached the young prince.

“I, Baek Yeon, Commander of the Embroidered Uniform Guard, pay my respects to His Highness Prince Shangshan. I serve only the Emperor with my utmost loyalty, so please forgive me for being unable to kneel, with a heart as vast as the sea.”

His words were respectful, but his voice was light. He didn’t even show the proper deference due to a direct member of the imperial family—a prince.

And then there was that faint smile on his lips.

Still, he held the post of Commander of the Embroidered Uniform Guard for a reason. He was the Son of Heaven’s most trusted military officer, and the head of a force even the highest-ranking officials feared.

“Furthermore, I humbly ask that Your Highness hold me responsible for the crimes of my subordinates, who dared to show disrespect in your presence.”

That wasn’t an apology or a request. It was a notification.

He was telling us to put an end to this here and now.

Even I, who was only watching for the moment, couldn’t help frowning. But Hong Jin, Prince Shangshan’s loyal servant, reacted differently from before.

Crack.

He clenched his fist so tightly that his skin turned white.

The rings on his ten fingers scraped against one another with an unpleasant sound.

But Hong Jin stared at the middle-aged man—or rather, Baek Yeon, the Commander of the Embroidered Uniform Guard—with a deeply restrained gaze, then leaned toward Prince Shangshan and whispered,

“Your Highness.”

It was a quiet call, but the meaning in his suppressed voice was clear.

Hong Jin was worried about confronting Baek Yeon right now.

Whether that was because Baek Yeon held the immense power of the Embroidered Uniform Guard’s command, or for some other reason, I couldn’t say.

And looking at it coldly, I had no place in this decision.

Intervening when an Embroidered Uniform Guard drew his sword was the proper thing to do as a guard in name, but from here on, it was best to follow Hong Jin’s lead.

This was the imperial court, not Murim.

But the next words out of Prince Shangshan’s mouth were something no one there could have anticipated.

“If you were in my place, what would you do?”

Countless eyes turned toward me from every direction.

As I stood there, briefly at a loss for words, Prince Shangshan Zhu Bao spoke again.

To me, and no one else.

“Blazing Flame Divine Dragon Jin Taekyung. I asked what you would do in my place.”

His eyes shone brightly.

The little boy who’d been delighted to get a new autograph was nowhere to be seen. I realized that the child in my memory had grown into a young man.

I knew what answer he wanted now, too.

“Uh, may I speak honestly?”

“That is precisely what I want. This is an order from your prince.”

At the prince’s bold command, I laughed aloud.

Then I looked at everyone and spoke.

“As you said, if I were in your place…”

Let’s not forget.

This was the imperial palace. I had to keep things under control.

“I’d have already beaten the shit out of every last one of them.”

“……!”

“……!”

Okay. So much for keeping it under control.
## Chapter artifact 863

# Chapter 863

Hundreds of members of the Embroidered Uniform Guard and eunuchs from the East Depot gathered in one place would have been quite a sight on its own.

But not as much as the expressions on their faces at that moment.

Shock. Astonishment. Confusion. Anger.

Those emotions swept across the countless faces surrounding us.

Every last one of them stared wide-eyed, gaped in disbelief, wondered if they’d heard right, and then, finally recognizing reality, summoned every muscle in their faces to express their fury.

Except for two people.

“……Young Master Jin?”

Hong Jin looked at me with dazed eyes.

“Ha. Fuck. I’m screwed again……”

Hyuk Mujin dragged a hand down his face with a deep sigh.

Hmm.

Hong Jin was one thing, but Hyuk Mujin had suffered because of me more than once or twice. I did feel a little bad for him.

Still…

*So what?*

He could be squad leader, then.

Besides, this was a royal decree from His Highness Prince Shangshan himself.

As a citizen of Korea—no, of the Great Nation—I had no choice but to follow it with all my heart.

Of course, I’d never even seen an identity tag bearing my name, and had no intention of getting one. But anyway, that was the idea.

In short, this was a legally sanctioned rampage.

“I answered honestly, just as you ordered. I’m not sure whether my answer pleased you, Your Highness.”

At my casual remark, Prince Shangshan Zhu Bao, who’d been staring at me with round eyes, flashed a mischievous grin.

“No. That was exactly the honest answer I wanted. Though I was a little surprised.”

A little? He looked pretty damn surprised.

Even that young prince, who’d shown such unexpected boldness, seemed to have felt the force of my words.

But I didn’t particularly regret them.

Whether this was Murim or the imperial palace, this was a world where showing weakness meant getting devoured.

A rat cornered in an alley and cowering wouldn’t survive long. A cat would bat it around like a toy until it finally stopped breathing.

*If we have to fight back anyway, showing our teeth is the best way to buy ourselves more time.*

I hadn’t charged in without thinking, either.

The Son of Heaven bringing Prince Shangshan all the way to the imperial capital meant he intended to get rid of him only after establishing some kind of pretext.

And that meant the hunting dogs snarling at us from every direction would stay docile until their master gave the order.

Even the pack leader with the sharpest teeth.

“Good grief. I don’t know what to say to that.”

Was Baek Yeon so composed because he commanded so many members of the Embroidered Uniform Guard? Or because he was a master who’d already reached the realm of the superhuman?

Whatever the reason, his reaction was clearly different.

He didn’t show the near-killing-intent fury of the others, nor did he toy with his weapon as though killing me were his life’s ambition.

He merely stroked his beard and said,

“As a word of advice, you’d do well to watch your tongue next time. This is the imperial court of the Great Nation, not Murim.”

I scratched my chin.

“I did what His Highness told me to, and now I’m getting scolded for it. How’s a powerless commoner like me supposed to live with that?”

I shot a sidelong glance at the prince, who caught the signal and spoke up.

“Baek Yeon, Commander of the Embroidered Uniform Guard. This man merely followed my orders. You will say no more about it.”

Baek Yeon didn’t answer. As his inscrutable gaze looked down at the prince, Zhu Bao’s voice grew firmer.

“I asked you a question. Why aren’t you answering?”

Ah.

I couldn’t let that go.

“That’s right! How dare you ignore His Highness? You insolent bastard!”

Good projection. Good timing.

*Fwoooosh.*

And what an atmosphere.

My stern rebuke landed with a satisfying three-quarter beat, and a storm of energy boiled up all around us.

Hong Jin let out a quiet groan. Hyuk Mujin grabbed my sleeve and whispered frantically,

“Captain. Captain. Please, stop.”

“His Highness Prince Shangshan, the younger brother of His Majesty the Emperor, is asking you a question! If you don’t answer, that’s an insult to the imperial family! You’re a traitor!”

“Have you actually lost your mind? Have you been dragging me around all this time just to get me killed in a place like this?”

“Let go of me, you pathetic excuse for a man who can’t even use Sword Energy! Are you on their side, too?”

“No, shit. Please……”

Just as Hyuk Mujin was starting to sound half in tears, Baek Yeon, who’d been staring silently at Prince Shangshan the whole time, suddenly raised one hand.

*Swish.*

The oppressive air scattered in an instant.

The Embroidered Uniform Guard, who’d been furious at the sight of their heaven-high superior being insulted, all withdrew their auras at once. Baek Yeon opened his firmly shut lips.

“Please forgive me, Your Highness. I am slow-witted, and hesitated because I did not know how to answer.”

There wasn’t a single fool here who’d take that at face value.

Even if that person were a young prince who knew nothing of the world.

“I forgive you. But since you took so long to answer, it had better be the right one.”

Watching Zhu Bao respond with such dignity, I realized something anew.

Regardless of his age, he was a member of the imperial family, born to noble blood. He was someone destined to become a dragon if only he could obtain the dragon pearl.

Perhaps even Hong Jin, who’d stood by Prince Shangshan for so many years, had underestimated him. Perhaps even the all-powerful man who remembered him only as a child who had barely survived countless purges and been forced to leave for Shanxi Province with the sole eunuch left at his side had underestimated him.

“I, Baek Yeon, Commander of the Embroidered Uniform Guard, will engrave Your Highness’s command deep in my heart.”

*Clank.*

At the metallic scrape of golden armor, I saw Prince Shangshan’s shoulders twitch.

He had a boldness and dignity beyond his years, but he was still a child. Facing one of the most powerful men in the imperial capital must have taken more courage than I’d imagined.

*In that case…*

A little help wouldn’t hurt.

*Swish.*

I murmured inwardly and, with all due insolence, brushed a hand against Prince Shangshan’s back.

The young prince looked up at me, eyes wide at the sudden warmth flowing into him. Then he gave a faint smile and continued,

“These people are citizens of Shanxi Province, which I govern, and guests whom I personally invited. There must be no neglect or mishap of any kind. Is that understood?”

Baek Yeon glanced at me at the sound of the prince’s newly clear voice, then replied with an odd expression.

“This is the imperial palace, where His Majesty the Emperor resides. Who would dare harm Your Highness’s guests?”

I muttered as if to myself,

“Who knows? I mean, someone’s already drawn a sword in front of His Highness. What wouldn’t they do?”

“……!”

“Good grief. The world’s a frightening place these days, isn’t it, Your Highness?”

At my feigned distress, Prince Shangshan looked at Baek Yeon once more.

“I believe those words are true. What do you think?”

A top tip for dealing with the imperial palace:

Get on good terms with a prince, and even the Emperor’s right-hand man can’t easily touch you—not for now, anyway.

And just as I’d expected, Baek Yeon fell silent for a moment before giving the answer that had practically been decided already.

“I, too, agree with Your Highness’s words.”

“Then I have nothing more to say.”

“……You honor me beyond measure.”

It had been a tense verbal exchange, with no clear victor or loser. But if I had to call the situation, we’d definitely come out ahead.

We’d secured a promise of safety in the Commander’s name, and confirmed that Prince Shangshan Zhu Bao’s authority wasn’t so easy to disregard.

The problem was…

*Who knows how long that safety will last.*

Was this what it felt like to lie on an operating table?

Everyone with me and I were patients. Instead of kind nurses, the place was crawling with members of the Embroidered Uniform Guard and eunuchs armed with blades and spears. And the surgeon would be none other than the Son of Heaven himself.

This was the imperial palace.

With a single word from the Emperor, who still hadn’t shown his face, our fates could change.

*To have your fate decided by someone you’ve never even seen…*

This felt a lot worse than I’d expected.

Of course, even if the Son of Heaven held the power of life and death, I had no intention of going down quietly.

The one saving grace was that they hadn’t made a firm diagnosis yet.

Maybe it would end with a few stitches. Or maybe I’d be put to sleep by terrifying nurses wielding blades and spears instead of anesthetic and surgical instruments. What happened next would depend on what we did.

No. I hoped that was how it would go.

If the surgeon had already declared us terminal, we’d have to fight for our lives with everything we had.

And Baek Yeon—the head nurse who served closest to the surgeon—had come bearing new information about that.

“By His Majesty the Emperor’s command, Your Highness’s audience has been postponed until tomorrow.”

“Postponed? Is that what my elder brother said?”

“Yes, Your Highness.”

Zhu Bao wasn’t the only one whose eyes widened at the unexpected news. Hong Jin’s did, too.

“But before we arrived, I was told…”

“How dare a mere eunuch butt in, Hong Cheophyeong. No—Deputy Military Commissioner now, is it?”

It seemed they’d met before. Baek Yeon cut Hong Jin off firmly and continued,

“You will attend to His Highness until you receive word.”

“……Can’t you at least tell us why?”

“I said it was His Majesty’s command. Do you need another reason?”

Hong Jin had been about to say something, but closed his mouth.

It was the Emperor’s command, after all.

That word left no room for questions or argument. I turned over the meaning of this sudden postponement in my mind.

*Why? Is there a reason?*

An audience that had already been arranged had been postponed. The whims of the powerful weren’t anything to be surprised about, but given the situation, I couldn’t help thinking hard about it.

Of course, with everything shrouded in a thick fog, I couldn’t get very far.

“Thousand Captain Jeong.”

“Your orders?”

“Escort His Highness Prince Shangshan inside. And…”

The moment Baek Yeon’s gray eyes, bearing the marks of many years despite his appearance, turned toward me—

*Rumble.*

I felt Baek Yeon’s aura tighten around my whole body.

That immense force had been aimed at me alone.

As soon as I realized it, I roused the internal energy sleeping deep in my lower dantian.

*Whoosh.*

Two invisible forces met across the empty air. They collided and mingled countless times in the blink of an eye, then finally dispersed like mist.

Along with a voice no one else could hear.

—Not bad, young man.

Half of one’s strength.

No—not even a quarter of it had gone into that contest of auras.

I gained nothing from the brief exchange, so instead of answering, I licked my lips. Baek Yeon gazed at me for a moment, then finished what he’d been saying.

“The others will come as well.”

“Understood!”

Jeong Hogun gave a vigorous military salute, then nodded to his subordinates. A wave of gold surrounded us once more, and we began moving somewhere.

Or rather, we were about to.

“Ah, I nearly forgot something.”

Baek Yeon’s quiet voice stopped everyone in their tracks. He walked up to one of the Embroidered Uniform Guard and spoke.

“You dared to draw your sword in front of His Highness.”

*Shhk.*

In place of an answer, a cold slicing sound rang out, and a head shot into the air.

Baek Yeon had cut down his subordinate with a hand blade faster than a flash of light. Then he turned to Prince Shangshan and smiled warmly.

“A subordinate’s crime is my own fault. Please forgive me, Your Highness.”
## Chapter artifact 864

# Chapter 864

“The crime of my subordinate is my own failing. Please forgive me, Your Highness.”

Baek Yeon smiled warmly as he looked at the young prince before him.

Prince Shangshan’s eyes shone with unusual clarity, reflecting the sight of Baek Yeon with his subordinate’s blood spattered across him.

He looked like a beast facing its prey.

And the response was immediate.

“Baek Yeon, how dare you—!”

Hong Jin sprang in front of his young lord and shouted, his voice boiling with fury, but Baek Yeon paid him no mind.

No—more precisely, he couldn’t afford to.

Someone far more dangerous than any eunuch was staring right at him.

“This guy. I thought we were going to settle this nicely, but you’ve really crossed the line.”

At the young man’s offhand remark, the smile on Baek Yeon’s lips deepened.

“Is there a problem, Jin Taekyung of the Jin Family of Taiyuan?”

“There is. A big one. Are you really allowed to do this?”

Jin Taekyung scratched his chin and pointed at the head lying on the ground.

Blood poured without pause from the cut, so clean it sent a shiver down his spine.

“You commit murder in front of His Highness? Is a Commander of the Embroidered Uniform Guard allowed to run wild like this?”

“Of course.”

“What?”

“I said I’m allowed. No matter how much power a high official wields—even if he’s a member of the imperial family—I and the Embroidered Uniform Guard serve only one person and obey his will.”

Baek Yeon raised one hand toward the darkened sky, then spread both arms toward the vast buildings stretching endlessly behind him.

“The Son of Heaven. Aside from His Majesty the Emperor, who rules this world on Heaven’s behalf, who would dare punish the Embroidered Uniform Guard on a private whim?”

“……!”

“The only reason I—or, rather, the Embroidered Uniform Guard—exists is to serve His Majesty. If anyone tries to challenge or undermine his authority…”

His mouth was still smiling, but his eyes weren’t.

Baek Yeon swept a cold, steady gaze over those around him.

The East Depot eunuchs, their faces stiff. Hong Jin and Hyuk Mujin, tense. And finally, Jin Taekyung, standing between him and Prince Shangshan. After taking them all in, he continued slowly.

“Whoever it is, they won’t escape death.”

Thud.

Baek Yeon kicked the head. It rolled and came to rest at someone’s feet. Jin Taekyung stared at the leather shoe soaking up the blood, then spoke.

“So, are you going to claim we’ve committed treason now?”

“Prince Shangshan committing treason? Ha! That’s a frightening thing to say, my friend.”

Baek Yeon laughed aloud and waved a hand.

“No, no. I merely punished him myself.”

“Punished him?”

“He dared draw his sword in front of His Highness Prince Shangshan. That’s a capital crime. Like someone said earlier, he deserved to be completely fucked up.”

“I appreciate you taking my opinion into account, but it looks like there’s one more person who needs to be fucked up.”

Jin Taekyung laughed along as he continued.

“The man who drew his sword in front of royalty is dead. What happens to the one who spilled his blood?”

“Since I summarily dealt with someone who might have been a traitor, I expect I’ll receive due praise and reward.”

“Who says?”

“You may not know this, but incidents within the Embroidered Uniform Guard are generally resolved quickly. There are only two people with the authority to decide.”

Jin Taekyung let out a dry laugh.

He already had a rough idea from that much.

One of the two decision-makers was the Son of Heaven, the very reason the Embroidered Uniform Guard existed. The other was…

“The Commander of the Embroidered Uniform Guard?”

“Correct. You’re sharper than I expected, Jin Taekyung of the Jin Family of Taiyuan.”

“Damn it.”

“There’s another way, so don’t look so crestfallen just yet. If you want me punished, you can submit a formal petition to His Majesty the Emperor. Every citizen of the Great Nation has that right. Ah, of course…”

Baek Yeon continued as if he’d just remembered something.

“That might be difficult for a martial-world ruffian without even an identity tag.”

“……Hah.”

“There is another way, though. Want to hear it?”

Jin Taekyung thought for a moment, then shook his head.

“That would be difficult.”

“Why?”

“I want to kill you, but I don’t want to die.”

“The former is little more than absurd nonsense, but the latter is a fairly reasonable explanation. And that answer just saved your life.”

Clank. Clank.

An unpleasant scrape rang out with every step Baek Yeon took.

Clad in golden armor that gleamed even in the dark, he stopped in front of Jin Taekyung. He looked up at the young man, who stood a head taller than him, then turned his gaze to the young prince visible beside him.

“Your Highness Prince Shangshan. Do you also believe my conduct was disrespectful?”

“……”

“Your Highness. I am asking you.”

His trembling breath was audible. Yet Baek Yeon’s armor wasn’t the only thing that still shone in the darkness.

“You are… truly arrogant and discourteous.”

Prince Shangshan Zhu Bao trembled, but kept his eyes fixed on Baek Yeon as he continued.

“However, I will not blame you. Nor will I ask My Imperial Elder Brother to punish you.”

Baek Yeon bent at the waist, theatrically.

“I am most grateful to hear that, but may I ask your reason?”

“You are My Imperial Elder Brother’s subject, not mine.”

“……!”

“Both you and I are ultimately His Majesty’s subjects. But if you were my subject, you would not escape death here today. A sovereign must not forgive a disloyal subject.”

At those words, an unreadable emotion passed over Baek Yeon’s face.

But it was gone in an instant. Without answering, he turned and gestured to his subordinates with his chin.

“His Highness appears weary from the long journey. Take him inside at once.”

“Loyalty!”

“Oh, and Thousand Captain Jeong, stay behind a moment.”

The Embroidered Uniform Guard soldiers, who’d paused where they stood, closed in around the party once more.

As the guards moved in a way that made it impossible to tell whether they were escorting the party or surrounding them, Baek Yeon sent a quiet Sound Transmission.

—You’ll regret coming here.

Jin Taekyung’s reply came flying back amid the golden tide flowing toward the Inner City, as though he’d been waiting for it.

—My whole life’s a regret already. Don’t worry about me. Go fuck yourself.

Who else could say something like that to the Commander of the Embroidered Uniform Guard?

Baek Yeon let out a dry laugh at the young ruffian’s reply, which went far beyond all expectations, and walked away, leaving the East Depot eunuchs behind.

Jeong Hogun, who’d stayed at Baek Yeon’s order, naturally followed after him and spoke.

“Is there something you wish to command me?”

“There is. But before you hear an order, thinking for yourself is also a virtue the Embroidered Uniform Guard must possess.”

“I will watch Prince Shangshan and his party without the slightest lapse.”

“That’s close to the answer I wanted, but not quite.”

“Then…”

“Make it look as though you’re watching them without a lapse, but leave gaps all the same. Make sure someone can slip through and approach them.”

“……!”

Clank. Clank.

Baek Yeon climbed the stairs that stretched upward without end. Hundreds, even thousands of them. They symbolized the Son of Heaven’s authority.

No matter how high an official’s rank, whenever they went to court, they had to climb those stairs, sweating profusely.

Leaving behind their power and their gold and silver treasures.

Reminded of the Son of Heaven’s majesty, which reached all the way to Heaven.

“You must watch and find out whom they meet. Who comes to see them. Everything.”

To catch fish in a net, you first had to spread it wide.

Only after that did you close it tightly and haul it in.

Of course, you also had to consider the possibility that something bulky or sharp-toothed might tear through it.

“How is ‘that matter’ I entrusted to you some time ago?”

There was no answer. Jeong Hogun lowered his head in silence, and Baek Yeon clicked his tongue softly.

“Cunning bastards.”

“I have nothing to say. I did my best, but…”

“It doesn’t matter. Not yet. But there must not be a second mistake.”

“Of course. Give me the order, and I will carry it out without fail.”

“Without fail? Whatever the order?”

“Yes.”

Baek Yeon suddenly stopped and turned to look at Jeong Hogun. A silent whisper slipped through his slightly parted lips.

—If I ordered you to assassinate His Highness Prince Shangshan, would you do it?

“……!”

Jeong Hogun’s eyes widened, his pupils wavering. Baek Yeon stared down at his subordinate without a word, then burst out laughing.

“No need to be so shocked. It was only a joke.”

“A joke… you said?”

“Yes. But I really am curious about your answer.”

A bead of cold sweat, he didn’t know when it had formed, ran down Jeong Hogun’s forehead.

But his silence didn’t last long.

“I will follow your orders with my life. If they are the Emperor’s command.”

The smile on Baek Yeon’s lips slowly faded. He studied his subordinate with a curious expression, then smiled faintly again.

“You’re right. That is a truly Embroidered Uniform Guard answer.”

“……I apologize.”

“What are you apologizing for? The Embroidered Uniform Guard lives and dies by the Emperor’s command. Naturally, we move only according to His Majesty’s will.”

Baek Yeon suddenly looked away.

Far in the distance, he could see a procession of torches and golden armor stretching out one after another.

And although he couldn’t see him now, somewhere within that ironclad escort was the bloodline of a dragon.

‘Prince Shangshan Zhu Bao.’

The young prince might not remember, but the old officer remembered clearly.

The Son of Heaven’s only younger brother, and the sole direct member of the imperial family to survive the most brutal power struggle in history.

The child he was seeing again after more than a decade had grown considerably—in body and in mind.

“……Which makes him all the more dangerous.”

Jeong Hogun lifted his head at Baek Yeon’s whispered words.

Baek Yeon waved a hand as if nothing had happened, then spoke again.

His face was stern now, without the slightest trace of a smile.

“Remember one thing.”

“Give me your command.”

“Once someone has set foot in this imperial palace, no one is to be allowed to leave.”

Jeong Hogun immediately understood.

Those words weren’t meant only for Prince Shangshan Zhu Bao.

The Embroidered Uniform Guard had to keep its eyes on more than just the bloodline of the dragon. There was also the martial-world ruffian who had dared to bear the title of Divine Dragon.

‘Blazing Flame Divine Dragon Jin Taekyung.’

The dragon was a mythical creature that symbolized only the Son of Heaven.

But the young prince had brought an uninvited Divine Dragon into the imperial palace where the Son of Heaven resided.

He’d made that ruffian, who ignored the laws of the Great Nation, his guard, defending and sheltering him.

No one could be certain what the result of that choice would be.

Not Jeong Hogun, nor even Baek Yeon, who had anticipated the situation and allowed it to happen.

The Blazing Flame Divine Dragon Jin Taekyung they knew had always been like that.

He always overturned everyone’s expectations, bringing storms and flames that swept in from every direction.

Fwoosh.

In the darkness, a fierce wind blew from somewhere, making the torches flicker.

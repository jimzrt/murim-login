# Checkpoint Review — 855–859

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

# Chapters 855–859

## Plot

Jeok Cheongang’s party pushes east toward Jiangsu after he kills roughly three hundred bandits and river pirates who attacked a caravan. Jin Taekyung rejoins them and, despite his uncertain health and the group’s exhaustion, insists they travel together and reach Jiangsu quickly.

On the road to the imperial capital, Hong Jin travels with Prince Shangshan Zhu Bao and the Embroidered Uniform Guard. The Guard encounters Hyuk Mujin, who had been mistaken for a corpse. Mujin disarms a subordinate and refuses to leave while waiting for the person he serves. Jin arrives and faces off with Commander Jeong, later identified as Jeong Hogun. Zhu Bao intervenes, greets Jin, gives him a secret letter, and asks for his autograph.

Jeong restrains his men, citing the prince’s order to lower their swords, but secretly sends a subordinate to report the interference to the Guard’s Commander-in-Chief. Jin worries that traveling to the capital could leave his party at the Emperor’s mercy. Zhu Bao accepts the Divine Physician’s offer of a checkup and, amused by Mujin’s boast, gives him the joking title “Tenfold Man,” which Mujin inscribes on a bronze token.

## Continuity

- The Divine Physician has the Blood Soul Gu recovered from the deceased City Lord of Sichuan Province. It weakens its host, causes madness, and eventually kills them. Jin suspects Dark Heaven’s covert killing of the City Lord may be part of a scheme targeting the Great Nation or its imperial family.
- Prince Shangshan Zhu Bao is traveling toward the imperial capital with Hong Jin and the Embroidered Uniform Guard. The late Emperor entrusted Hong Jin with Zhu Bao’s care; Zhu Bao trusts his elder brother, while Hong Jin fears the Emperor’s intentions.
- Jin Taekyung’s party is accompanying Zhu Bao toward the capital. Jin is concerned the Emperor could turn the Imperial Guards against them.
- Jeong Hogun leads the Embroidered Uniform Guard escort. He secretly sent a subordinate to report to the Guard’s Commander-in-Chief that uninvited guests had interfered, as predicted.
- Zhu Bao gave Hyuk Mujin the joking title “Tenfold Man,” which Mujin inscribed on a bronze token.
- Zhu Bao handed Jin a secret letter; its contents remain unknown.

## Translation Decisions

- Render 혈혼고 as “Blood Soul Gu,” 대국 as “Great Nation,” and 금의위 as “Embroidered Uniform Guard.”
- Render 금위군 as “Imperial Guards,” 정호군 as “Jeong Hogun,” and 정 천호 as “Commander Jeong.”
- Render 십상남자 as “Tenfold Man.”

## Durable state

{
  "active_continuity": [
    "The Divine Physician secured the Blood Soul Gu found in the deceased City Lord of Sichuan Province; it weakens hosts, causes madness, and eventually kills them.",
    "Jin suspects Dark Heaven’s covert killing of the City Lord may be part of a scheme targeting the Great Nation, possibly its imperial family.",
    "Prince Shangshan Zhu Bao is traveling toward the imperial capital with Hong Jin and the Embroidered Uniform Guard; the late Emperor entrusted Hong Jin with Zhu Bao’s care, and Zhu Bao trusts his elder brother.",
    "Jeong Hogun leads the Embroidered Uniform Guard assigned to escort Zhu Bao discreetly; he sent a subordinate to report to the Guard’s Commander-in-Chief that uninvited guests had interfered, as predicted.",
    "Jin’s party is traveling with Zhu Bao toward the imperial capital, where Jin fears the Emperor could turn the Imperial Guards against them.",
    "Zhu Bao granted Hyuk Mujin the joking title “Tenfold Man,” which Mujin inscribed on a bronze token."
  ],
  "continuity_sources": [
    858,
    859
  ],
  "open_questions": [
    "Why did Dark Heaven secretly kill the City Lord of Sichuan Province, and is it targeting the Emperor or imperial family?",
    "What does the Emperor intend for Prince Shangshan, and what prompted the imperial decree against Hong Jin?",
    "What does the secret letter Zhu Bao handed Jin contain?",
    "Who predicted that uninvited guests would interfere, and what does the Commander-in-Chief or Emperor know about the party?",
    "Who trained the Embroidered Uniform Guard force of highly skilled martial artists, and for what purpose?"
  ],
  "safe_through": 859,
  "temporary_decisions": [
    "Render 혈혼고 as “Blood Soul Gu.”",
    "Render 대국 as “Great Nation.”",
    "Render 금의위 as “Embroidered Uniform Guard.”",
    "Render 금위군 as “Imperial Guards.”",
    "Render 강소 as “Jiangsu.”",
    "Render 정호군 as “Jeong Hogun” and 정 천호 as “Commander Jeong.”",
    "Render 십상남자 as “Tenfold Man.”"
  ],
  "version": 1
}

## Reading copies

## Chapter artifact 855

# Chapter 855

“Which son of a bitch set the fire?”

A voice dropped low.

Hyuk Mujin swept his surroundings with a gaze sharp as a blade, then shuddered with a gasp.

“Damn. Just thinking about that time makes me feel like I’m about to piss myself! As expected of Great Hero Je—”

“Shut your mouth and sit down before I beat you so badly you piss and shit yourself.”

“Yes, sir.”

“That mouth of his never seems to take a break. Was he like that in Nanman, too?”

At Jeok Cheongang’s sighing question, Ju Hwaran, who was standing beside him, answered cautiously.

“Yes. Young Hero Hyuk has always been like that.”

“I wish I had a muzzle for him, but there’s no way to find one around here. It’s enough to drive me mad.”

Jeok Cheongang clicked his tongue and looked around, but that didn’t produce any particular solution. They were traveling along a forest path full of grass and trees.

They did occasionally encounter people, but what kind of lunatic would carry a muzzle meant for a person up a mountain?

“I do have one. Shall I give it to you?”

“……?”

There was such a lunatic.

And he was right nearby.

“Why on earth are you carrying something like that?”

At Jeok Cheongang’s bewildered question, Namho whispered in a small voice.

“Doesn’t everyone have at least one person they’d like to put a muzzle on?”

“……You’re quite something yourself.”

“Anyway, if you need it, just say the word. I won’t give it to you outright, of course. I’ll only lend it to you for a little while. I’ll need it myself as soon as I get the chance.”

Namho glanced meaningfully over his shoulder. Not far away, by a stream, Taishan was staring intently into the water with a troubled look.

“Taishan. I can’t find it at all. I need Namho’s help. He’s old and smart.”

“Hm.”

No matter how much you disliked someone, you couldn’t spit in the face of a smile.

Namho had been about to say something the moment their eyes met, but his tone softened a little as he asked,

“I’m not too sure about that first part, but… fine. What do you need help with?”

“I’m looking for meat, but I can’t see any. Namho’s smart, unlike Taishan.”

“You’ve said nothing but true things today. But what were you sitting there waiting for? Carp? Crucian carp?”

“Neither.”

“Then what?”

“Five-spice pork.”

“Fuck…!”

Namho grabbed a rock and charged at Taishan like a mad bison, but his run was quickly cut short.

At Jeok Cheongang’s glance, Sama Pyo and Song Ilseom appeared like streaks of light from somewhere and grabbed his arms from either side.

“Let go! Let go of me, you brats! You brats are still wet behind the ears!”

“Calm down, Elder Namho.”

“We don’t want to do this either.”

“I’m going to count to three. It would be in your best interest to let go of this old man before something irreversible happens. Now. One, two, two and a half. Two and three-quarters…”

Before he could reach three, Namho was dragged off into the undergrowth. Watching him go, Hyuk Mujin murmured sadly,

“That’s a shame. I’d grown quite attached to him.”

“What are you talking about? Anyone listening would think we were actually going to kill him.”

“Wait, we aren’t? I thought Great Hero Jeok had already given the order.”

“……”

What on earth did this guy think he was?

Flustered by Jeok Cheongang’s burning gaze, Hyuk Mujin started rambling.

“I mean, a few days ago, you cut down every last one of those bandits. All those men…”

“What am I, a butcher? ‘Cut them down’? And it wasn’t just bandits. River pirates were mixed in, too.”

“Isn’t that basically the same thing?”

“They’re distinctly different. Though it doesn’t change the fact that every last one of them deserved to die.”

“Because they set the fire?”

“Of course… No. Because they harmed innocent people.”

Jeok Cheongang hurriedly changed his answer, but watching him only confirmed Hyuk Mujin’s suspicion.

*It was because they set the fire. That’s why he killed them.*

Strangely enough, of all the countless sins in the world, Jeok Cheongang considered arson the worst.

Perhaps that made sense. During the Great Faction War, Sword Saint Mae Jonghak had asked him to join the orthodox faction, but Jeok Cheongang had refused. What finally brought him out into the world was the Demonic Cult’s arson.

The battle three days ago had been for exactly that reason.

*Actually, it’s embarrassing to even call that a battle.*

Hyuk Mujin quietly revised his earlier thought.

It hadn’t been a battle. It had been a massacre.

It was that one-sided—and that brutal.

A full three hundred bandits and river pirates had been wiped out in less than an hour.

Afterward, Hyuk Mujin and the others had left, barely listening to the trading company masters from Hubei thank them.

They’d taken the only merchant ship that had somehow survived the flames as payment for saving their lives.

Of course, they hadn’t asked for the other party’s consent. But anyway, that was what happened.

“Oh, come to think of it, those people must be in Hubei by now, right?”

“Why are you suddenly changing the subject?”

“Those people. The ones we saved.”

“……Is that something a man who barely swung his sword a couple of times should say?”

“But I did swing it.”

What nerve.

Jeok Cheongang glared at Hyuk Mujin in disbelief, then shook his head.

From what he’d seen so far, every last one of those Fire Dragon Pavilion fellows was out of his mind. Thinking too hard about it would only bring back the infirmities of old age he’d barely managed to cure.

*I suppose I should be grateful there’s at least one normal person among them.*

Jeok Cheongang turned his gaze slightly to the side. The one person he could call sane in this band of lunatics, Ju Hwaran, was there.

*The more I see her, the more I like her.*

It had been seven days since they’d left the Sichuan Tang Clan as if something were chasing them.

They’d been traveling day and night, choosing only remote, rugged terrain to avoid drawing attention. Yet Ju Hwaran hadn’t complained once. She’d remained cheerful the whole time.

There must have been any number of hardships, especially as the only woman in the group.

*She’s clearly kept up with her martial arts training, and her character is upright, too. The Escort King has himself one fine granddaughter.*

How many young people mistook recklessness for a virtue?

And that wasn’t limited to street thugs. Even among the disciples of the great sects who were known as young prodigies, there were plenty of fools.

They trusted only in their natural talent, neglected to work hard, and strutted around with their sect’s prestige at their backs.

Jeok Cheongang had seen that sort so often he was sick of them. That was why he couldn’t help finding Ju Hwaran all the more admirable.

Though, of course, he couldn’t say he had no ulterior motives at all.

*Even the ones swaggering around as Elders and Sect Leaders of the Nine Sects and One Gang now were a whole basket of no-good brats when they were young. Compared to them, Hwaran is more than Jin Taekyung deserves… No. What’s he lacking? He’s handsome, well-built, and there’s no need to mention his martial arts.*

A fierce battle was underway in his head.

Jeok Cheongang had already started sipping the broth before the person who’d give him the noodles had even considered it, when a voice suddenly pierced his ears and startled him.

“Great Hero Jeok, are you all right?”

“Hm? What?”

“You looked troubled, so I was wondering…”

“Ah. Ahem.”

Jeok Cheongang had started to answer without thinking, but he hurriedly cleared his throat.

He didn’t want a young girl who was at least young enough to be his great-granddaughter to discover an old man’s foolish preoccupations.

“It’s nothing. I was just thinking about how far we have left to Jiangsu.”

“Oh. At our current pace, we’ll arrive in five days. Even if something comes up and delays us, I expect it’ll take about seven days.”

“How can you be so sure?”

“I came through this area on an escort mission two years ago. I also brought along a map that’s been passed down from my grandfather’s time.”

“Ho. Impressive. Very impressive.”

“Thank you. But I’m not worthy of such high praise from you, Great Hero Jeok.”

They said she’d led the Escort Bureau for several years in place of her father, who had been bedridden until recently. Her answer was every bit as crisp as he’d expect.

Ju Hwaran looked flustered by the sudden praise, and Jeok Cheongang smiled warmly.

“You’ve got everything planned out. You’re so capable, unlike that brat.”

“Pardon? What do you mean…?”

“I was just talking to myself. Still, the more I hear you address me that way, the more stiff it sounds. From now on, you can just call me Grandpa—”

Jeok Cheongang checked Ju Hwaran’s expression and changed his mind mid-sentence.

Grandpa was still far too soon, even by his own reckoning. Every relationship had to start with one step at a time.

If he got ahead of himself and made Ju Hwaran wary, it would surely affect her relationship with his one and only Disciple, too.

“……No. Call me Old Master.”

“Really?”

The only people who called Jeok Cheongang that were those who had known his predecessors, or the heads of the Nine Sects and One Gang and the Five Great Families.

Ju Hwaran’s eyes widened at his unexpected offer. At that moment, Hyuk Mujin, who’d been listening to their conversation, chimed in with a bright smile.

“Thank you, Old Master. I thought the same thing—that the way I address you is too stiff…”

“Would you rather be hit by this old man’s fist, which is harder than a rock? Or keep your mouth shut?”

“……”

“You’re not allowed. Don’t even dream about it.”

Jeok Cheongang made the ruling more firmly than ever and glared at Hyuk Mujin with a fierce expression.

“Good grief. Why are you picking on the poor kid?”

A voice spoke from far away, yet it was as clear as if the speaker were right in front of them.

But Jeok Cheongang knew who it was before he even heard the voice.

A faint footstep and breath—so subtle that even a Peak master with deep internal energy wouldn’t have heard them. That alone was enough.

It wouldn’t have made a difference even if the title Fire King hadn’t come before his name, or if he weren’t a Supreme Peak master.

That was simply what having a one and only Disciple was like for a Master.

“Heh. Look at that slowpoke.”

But Jeok Cheongang instinctively frowned, hiding his delight as much as possible. Unlike when he’d spoken to Ju Hwaran, he didn’t forget to keep his voice gruff.

“What took you so long? Why are you crawling along at a leisurely pace now? I’ve been waiting half a day because of you.”

“Half a day?”

Hyuk Mujin ran toward Jin Taekyung shouting, “Captain!” and Jin Taekyung kicked him hard in the shin. Then he let out a hollow laugh.

“You’re exaggerating. Half a day, my ass. It’s only been half an hour at most. Isn’t that right?”

The Divine Physician, who had followed behind them carrying a bundle stuffed with needles and medicinal herbs, replied calmly.

“I’ll refrain from commenting, Young Hero Jin.”

“Why?”

“Isn’t it obvious? Even if I answer, there’s no point. There’s no reasoning with you anyway…”

“Wow. So you’re not called the Divine Physician just because of your medical skills. You’ve got some insight, too.”

“You’re too kind. It’s simply something anyone would come to understand after experiencing it.”

“…What the fuck is wrong with you two?”

Jeok Cheongang watched them with narrowed eyes, but instead of laying into them, he clicked his tongue.

One way or another, that rude young brat was his one and only Disciple, whom he couldn’t bring himself to hate. And the old man right beside him was a physician who’d agreed to travel a long way to treat that young brat.

What more could he say?

All he could do was pretend nothing was wrong, hide his worry, and ask this:

*How are you feeling?*

Jin Taekyung heard Jeok Cheongang’s Sound Transmission and gave a quiet laugh as he nodded.

Whether he was really all right or only pretending, if what the Divine Physician had told him was true, there should be at least some improvement.

*I’m all right for now. I don’t know when I’ll hit a wall, but… I’ll have to find a way, as best I can.*

Then, noticing Jeok Cheongang had fallen silent, Jin Taekyung gave a faint, bitter smile. He loosened his stiff body and spoke.

“How much farther? Three days? Four?”

Ju Hwaran answered as if she’d been waiting for the question.

“About three days.”

“Three days… We still have time before the first of the month, but it’s going to be close.”

Jin Taekyung looked somewhere to the east and continued,

“Let’s cut the time left down to two days.”
## Chapter artifact 856

# Chapter 856

Seven days and nights passed in the blink of an eye after we left the Sichuan Tang Clan.

The scenery and the people around us changed with every step.

But it was too soon to relax.

Despite my boast that we’d cut the remaining time down to two days, reality was cold. The farther we ventured into the wilderness to avoid drawing attention, the more time we inevitably lost.

“We’ll have to pick up the pace.”

“Even faster than this?”

“Yes. Faster than I thought we’d have to.”

“If we keep up this pace, we can arrive by the first of the month. We’re already pushing ourselves too hard.”

“I know. But do you think the Embroidered Uniform Guard is any different from us?”

“……!”

“We’re not the only ones on the move. We have to push ourselves and get in their way before they reach their destination.”

Jeok Cheongang already knew I was right, so he said nothing.

Information was important. But perfect information didn’t exist.

If we’d picked up some information, then so had our opponents.

That was true even in the modern world, where information could be relayed by the minute or even the second. How much more so in Murim?

Wherever they were headed, they were still within the Great Nation’s territory. Eyes and ears were everywhere, and there had been countless variables from the start. There was only one way to minimize them.

Move as fast as possible. Run ourselves into the ground.

Of course, that meant enduring tremendous hardship.

It was insane to try to cross half the continent in a little over half a month.

“Captain, we’re actually going to die at this rate.”

“Then we should rest.”

“Really?”

“Sure. In Jiangsu.”

“No, I’m not joking. I mean we’re going to die!”

“Mujin. Hyuk Mujin.”

“Yes?”

“If we don’t go, what do you think will happen?”

“……”

“If you want to rest, rest. I’m not being sarcastic or trying to hint at anything. If you think you can’t go on, drop out. It’ll be better for all of us.”

Hyuk Mujin said nothing after that.

No—neither did anyone else.

Instead of complaining, they held their tongues and kept moving.

We crossed rugged mountain ranges and forded winding rivers.

The vast continent’s climate and terrain varied a little from one region to the next.

The midday heat in Hubei was like a blast furnace, while the night wind in Anhui cut like a cold blade.

One day, after a storm swept through, some of the party finally collapsed, unable to overcome their exhaustion.

“Young Hero Jin, I understand how important this matter is, but… we can’t go on any longer.”

At the Divine Physician’s words, spoken after watching the members grow exhausted by the day, I gave him a short reply.

“We’ll set out again after fifteen minutes.”

I carried Hyuk Mujin on my back, and Jeok Cheongang did the same with Ju Hwaran.

Both of them refused at first, but this time I wouldn’t budge. It was obvious at a glance that neither of them was in any condition to be called well, even as a joke.

*Of course they’re exhausted. We’ve been moving until our internal energy and stamina were completely spent.*

And though his title was the Fire King, Jeok Cheongang was a man of cold disposition. For some reason, he felt sorry for Ju Hwaran, who was burning up from head to toe despite the Divine Physician’s treatment.

“Was this really necessary? We could—”

“If you’re about to suggest the two of us travel separately, I’ll refuse right now.”

“Why?”

“Because we have to make it through this together. If we can’t endure even this much, we’ll die before long anyway.”

This wasn’t for my sake. It was for all of us.

The war had already begun, and upheaval lurked all around us.

Catastrophes so terrible and vast that no one had ever experienced anything like them.

To survive the war against Dark Heaven, all of us had to grow stronger—not just me. A blade hammered and tempered countless times won’t break even when it strikes a rock.

And Jeok Cheongang was one of the very few people who understood the meaning of my words better than anyone.

He, too, had been remade through bone-deep effort and hardship. In the end, he’d become a peerless blade that cut through countless rocks blocking his way.

“We have to make it through this together…”

Jeok Cheongang slowly repeated the words he’d heard from me, then gave a dry chuckle.

“You’ve grown up.”

“I’ve always been taller than you, Old Master. Then and now.”

Jeok Cheongang shook his head at my answer.

“You’re still an arrogant brat. Then and now.”

“Isn’t that part of my charm?”

“But no matter how I look at it, this is too much. You heartless little bastard.”

“Miss Ju wanted it. I respected her wishes. If she were in enough pain to actually die, I’d have stopped her myself.”

“Cut the crap. Anyway, your idea might be right, but I can be sure of one thing.”

“Yes? What?”

“This old man guarantees you’ll never find a partner before you die.”

“Hey, why are you suddenly bringing that up?”

“Enough. If you have the energy to flap your gums, take one more step.”

Jeok Cheongang suddenly landed a brutal verbal blow, then darted away like the wind. As I watched his back, I noticed my view gradually growing brighter and raised my head.

*This is…*

I gathered my internal energy and pushed off the ground. Stepping onto the branch of the nearest great tree, I sprang up into its crown. At last, I saw a glow spreading in the distance.

It was the dawn light.

The eleventh dawn I’d seen, one each day since we’d left the Sichuan Tang Clan.

But the reason that light heralding a new morning felt especially welcome today was something coming into view beyond the grass and streams stretching all around us.

“Ah.”

A faint exclamation rang in my ears.

Hyuk Mujin, slung over my back, asked in a voice that sounded half dead,

“C-Captain. Where are we? What’s that?”

I laughed out loud.

Then, loud enough for everyone below the tree to hear, I answered:

“Jiangsu.”

* * *

Empires are majestic and great.

But they can never last forever.

Not so long ago, by the continent’s standards, the empire founded by the nomads of the grasslands had been no different.

Each of them was a fine warrior and herdsman. They worshiped heaven and earth and were close companions to hawks and horses, but they were not good rulers.

A little over a hundred years.

That was all it took for the vast empire founded by the invaders from the grasslands to fall.

There had been a great conqueror who was both hero and devil, destined to remain a legend to the very end. There had also been a wise ruler who strengthened the empire from within and cared for his subjects and people.

But when that age drew to a close, all that remained were horrific famine, corruption, and countless red flags fluttering in the wind.

*“You who hunger, rise up!”*

An age of war began. Figures wearing blood-red flags and headscarves rose like wildfires from every direction and swept across the continent.

The world called them the Red Turban Bandits. They wanted to be called the Red Turban Army, but in truth, the former name suited them better.

They were bandits.

Bandits who stole grain and treasure to fill their empty stomachs.

Bandits who wanted to steal this nation’s mountains and rivers, too.

*“How can the blood of kings, nobles, generals, and ministers be any different from anyone else’s?”*

Even if they were shabby on the outside, did that mean their insides had to be small and shabby, too?

Steal a handful of millet and you’re a bandit. Steal a continent and you become the Son of Heaven.

Just as one hero had done at the end of that long age of war, at last grasping all under heaven.

*“Your Majesty, please ascend the throne!”*

And so a new heaven opened.

Born the son of a poor farmer, he had wandered the land as a mendicant monk. Now he held all under heaven in his hands and occupied the highest position of all, with countless subjects and commoners beneath him.

But even after many years had passed and one of his own children inherited the throne, nothing changed.

At least, not for one boy living in Jiangsu.

*“Hey, you filthy beggar!”*

Filthy beggar.

It was one of the things he’d heard most often in his life. Even now, decades later, the memory was etched clearly into his mind.

So clearly that it appeared without fail whenever he had a nightmare like this one.

“……Ah.”

Hong Jin abruptly woke from his sleep and blinked. Then he respectfully bowed his head to the boy watching him in silence.

“I dared to fall into a dream before Your Highness. Please forgive your unfaithful servant.”

“Forgive you? There’s no need.”

The boy, Prince Shangshan Zhu Bao, replied.

His composure and dignified voice were hard to believe in someone who wasn’t even midway through his teens.

The young prince, taller and more solidly built than most boys his age, continued speaking to his servant.

“If anyone should apologize, it’s me, not you. I’ve put a loyal subject through so much hardship.”

“Hardship? I beg Your Highness to take back those words.”

“No. This is all because of my own shortcomings.”

“Your Highness…”

“But set aside any needless worry. What you’re afraid of will never happen.”

Hong Jin answered by bringing his hands together and bowing deeply.

But as he stared at the floor of the slowly moving carriage, his gaze held both pride in the young prince and a hint of bitterness.

*I earnestly pray it will be so as well, Your Highness… But your elder brother will not see it that way.*

Hong Jin forced down the voice rising deep in his heart.

His master, Prince Shangshan, had been an intelligent, mature boy from a young age. But he was far too young to understand the cruelty of the world.

Even now, as they traveled toward the imperial capital surrounded by the Embroidered Uniform Guard as if he were a prisoner being taken away, he still had unwavering faith in his only blood relative.

But Hong Jin did not.

*You already have all under heaven. What more could you possibly want, Your Majesty?*

With that question, which would reach no one, Hong Jin closed his eyes.

In the pitch-darkness, memories surfaced. Sounds returned.

Those days when the blood never dried. Days of purges when hundreds had their limbs torn off and died, and thousands were beheaded and displayed.

And the late Emperor’s final words.

*“Bao. I entrust that child to you.”*

Thump.

Hong Jin opened his eyes at a small jolt that traveled through the carriage. He turned to look beside him and saw someone’s profile through a narrow gap in the window.

“What’s going on?”

At Hong Jin’s low question, the man beside the carriage, dressed in shabby martial robes ill-suited to the name Embroidered Uniform Guard, replied,

“None of your business.”

His voice was blunt, without even the hint of emotion. But Hong Jin sensed the cold blade lurking beneath it.

A feeling both unfamiliar and familiar.

Just like the Embroidered Uniform Guard now, Hong Jin had once served as the late Emperor’s hands and feet. The sensation brought back something familiar that he hadn’t felt in over a decade.

Along with a hint of puzzlement.

*Why have we stopped?*

This covert procession had already entered Jiangsu, and the Embroidered Uniform Guard had no reason to stop. They were people who would gladly give their lives to carry out the Emperor’s orders.

*Something’s going on.*

Hong Jin quietly sharpened his senses. He might not be skilled enough to have established his own school, but he had still learned martial arts.

Thankfully, the guards seemed to judge that the matter wasn’t serious enough to require Sound Transmission. Their conversation drifted through the gap in the window.

“According to the scouts, there’s an unidentified corpse about three hundred zhang ahead…”

“We didn’t approach in case it was a trap, but there don’t seem to be any obvious wounds…”

“It could be an attempt to split up our forces. We’ll keep moving. Stay close to the carriage.”

The murmuring conversation abruptly stopped. After a brief pause, the carriage started moving again.

Clip-clop. Clip-clop.

As he listened to the quiet sound of hooves, Hong Jin thought,

*An unidentified corpse.*

It wasn’t that strange. The continent was vast, and there were people begging their way across it everywhere. Not even Jiangsu, so close to the imperial capital, was an exception.

But why?

Why did one man’s name suddenly come to mind at this very moment?

And why did an inexplicable hope well up in one corner of his heart?

*Could it be…*

Hong Jin had just lifted his head when—

“Didn’t you say it was a corpse…?”

With one of the Embroidered Uniform Guard’s men murmuring the words, a familiar voice Hong Jin had heard somewhere reached his ears.

“Captain. I swear I wasn’t dozing off. I was just lying down for a second… Huh? Who are you?”

At that moment, Hong Jin burst out laughing, briefly forgetting that the young prince was right in front of him.
## Chapter artifact 857

# Chapter 857

“What? Where’d everyone go? Hey, mister. Have you seen anyone around here?”

His hair was matted into a greasy mess, and grime streaked his face.

At the sight of the young man getting to his feet and babbling, the man he’d called “mister” suddenly spoke.

“What happened? No matter how I look at him, he doesn’t seem to be dead.”

“I-I’m sorry. He was sleeping so still, like he was dead, so I think I mistook him for—”

“That’s enough. We’ll talk about it again after we return to the palace.”

The Embroidered Uniform Guard martial artist who had reported the scouts’ findings earlier went rigid.

He knew very well what kind of man his superior was. He’d served under him for nearly three years.

He also knew how important this matter was to him.

If he was lucky, he’d be demoted. If things went badly, he could lose his position entirely.

*Damn it.*

The martial artist clenched his lips and struggled to suppress the anger welling inside him.

He couldn’t deny that he felt wronged, but a mistake was still a mistake.

He couldn’t gather water that had already spilled across the ground, but he could at least wipe it up.

No—he had to wipe it up.

If only to lessen the punishment that would soon fall on him.

“……I’ll take care of it.”

The martial artist spoke in a subdued voice and stepped toward the young man, who still looked half asleep.

The other guy was some miserable piece of trash who could’ve rolled in from anywhere. If he resisted, the martial artist could simply cut him down in one stroke.

At least, that was what he thought.

“What are you doing?”

Clop.

At the man’s sudden call, the martial artist stopped dead.

Under his superior’s calm but icy gaze, he stammered out a reply.

“I—it can’t be left like this, so I thought I’d handle it myself…”

“Handle it?”

“Y-Yes.”

“How?”

“Pardon?”

“I asked how you intend to handle it.”

“Well… given the situation, wouldn’t it be right to use force if necessary and remove the threat?”

The man was silent for a moment before speaking.

“How many years have you served?”

“I’ve been serving you, Commander Jeong, for almost three years. And…”

The martial artist hesitated, watching his superior’s expression, then added,

“Following my father’s advice, I believe I’ve always done my best to carry out your orders.”

A little unease—and a lot more resentment—colored his voice.

His superior had barely paid him any attention, even after nearly three years as his subordinate. And the way he was treated made it seem as if the man had no respect at all for someone born into a prestigious family.

*How much wealth did my family spend to get me into the Embroidered Uniform Guard?*

There was nowhere beyond the reach of gold, silver, or the influence of power. Not even the Embroidered Uniform Guard, directly under the Emperor, was an exception.

Even if a fortune had only bought him a low-ranking position after a rigorous screening, how many people would have killed to get even that far?

For that reason, the martial artist had no intention of backing down.

He’d mentioned his father as a sort of warning.

A clear attempt to remind his difficult, strict superior that he had powerful connections.

That was why the man’s next words were enough to make him question his own ears.

“Three years. That’s long enough.”

“Pardon?”

“Hand over your badge right now and go where you belong. This will conclude your punishment for the mistake you made earlier.”

“……!”

“What? Do you still have something to say?”

Eyes wide, the martial artist faced a reality he couldn’t believe and shouted,

“What is this! How can you do something so outrageous? Have you forgotten who I am—”

“I remember perfectly. Otherwise, I wouldn’t have kept you as a subordinate for three years.”

The man cut him off, then continued in the same calm voice.

“And the people remember not you, but the prestige of the family behind you. If you don’t want to make the same mistake again, engrave that fact into your heart and mind.”

“Have you said your piece?”

“I haven’t finished, but I don’t think there’s any need to explain the rest. Especially not to someone who can’t even tell what he’s dealing with.”

“What the hell are you—”

The martial artist was about to bellow when a voice reached his ear.

“Excuse me. Sorry to interrupt, but could I get some water first? I’ve been really thirsty for a while.”

“……!”

The voice hadn’t come from far away.

It was right behind him. Close enough that he could smell the sweetness of the man’s breath.

*How did he—?!*

Shock sent the hairs all over his body standing on end. The martial artist spun around like lightning and drew the sword at his waist.

Shing—whoosh!

The treasured sword, passed down through his family for generations, shone in a dazzling array of colors as it cleaved the figure behind him clean in half.

Or so he thought.

Until two hands dripping with grime moved like a flash, just as the sword was about to bite into the crown of his head.

Clang!

A deafening crash rang out as the man brought his palms together. At the same time, a single gasp slipped from the martial artist’s lips.

“Empty-Hand Seizes the Blade…?”

A technique a master would only use against someone at least a step or two beneath them.

Having reached the Supreme First Rate realm with generous support from his family, the martial artist immediately understood what had happened. He stared in shock at the man he’d taken for a mere beggar.

“A Peak master!”

At that horrified cry, the mysterious Peak master answered,

“What are you talking about, asshole? I get shit from everyone all the time for not being able to use Sword Energy.”

“Y-You! Who are you? State your identity!”

“Fuck off. Give me water. Not a sword.”

Whoosh—thud!

It happened in the blink of an eye.

As he redirected the sword he’d caught between his palms, the man drove his hard knee into the martial artist’s face. Then, from the martial artist’s body as it crumpled like a rotten log, he found a small flask and drained it in one go.

Gulp, gulp.

“Ahhh. That’s better.”

He looked like he hadn’t had a drop of water in days.

Commander Jeong watched the young man empty the flask, then shake out the last few drops. He spoke without warning.

“I had my suspicions from the moment I first saw you, but you’re pretty skilled.”

The young man stared at the mouth of the flask, now completely empty, as if expecting wine to come out if he just waited a little longer. Then he asked,

“Do you mean that?”

“Of course. You don’t seem to have reached the level of injuring others with Sword Energy, but the movement you just showed was extremely efficient and impressive.”

“Thanks. Hearing that from someone way more skilled than me almost brings a tear to my eye. Though I could do without you talking down to me.”

“You misunderstand. I wasn’t mocking you.”

“I know. I’m not saying you were. I really do feel like I’m about to cry.”

“……?”

“I’ve been through so much fucking shit. I’ve had every kind of abuse thrown at me. I train my ass off, and all I ever hear is, ‘Why can’t you use Sword Energy?’ and, ‘How can you call yourself a proper person if you can’t even do that?’ And now they’ve gone and left me on the side of the road, too… Ahem. Hic!”

Commander Jeong found himself at a loss for words.

The young man’s complaints had poured out as if he’d been waiting for the chance, and now tears were streaming down his face. He and everyone else there found themselves wondering the same thing.

*What the hell is that guy?*

He looked exactly like a beggar, but turned out to be a lunatic.

There was just one problem: that lunatic was actually pretty damn skilled. A Supreme First Rate martial artist, yet he moved like a Peak master.

But they were in the middle of carrying out an operation.

The Embroidered Uniform Guard martial artists lined up behind Commander Jeong exchanged bewildered looks.

*What are we supposed to do in a situation like this?*

*I don’t know. Captain Hong might know.*

*I don’t know, either.*

*How can you not know, Captain Hong? You’re our Captain.*

*Does a Captain have to be some kind of god? Still, Senior Officer Gal should know. He’s been around much longer than I have.*

*No. I don’t know, either…*

Their gazes wandered, and their mouths grew dry.

When had the famed Embroidered Uniform Guard ever dealt with a situation like this?

At this point, the lunatic had sat down right there on the road and was bawling his eyes out. No one could figure out what to do with him.

Well—not everyone.

Clip-clop. Clip-clop.

Commander Jeong slowly rode forward and looked down at the young man with his usual calm expression.

“Are you done crying?”

The young man answered in a tear-choked voice.

“Not quite.”

“That’s fine. We’re holding up the journey, so move aside.”

“Mm.”

The young man sniffled, then continued.

“That might be a little difficult.”

“Why?”

“Moving out of the way is easy enough, but the person I serve would get furious if I did.”

“I thought you said you’d been abandoned.”

“Sometimes I get left behind when I’m with that person. Anyway, I don’t know why I ended up here, but they’ll be back soon.”

Brush, brush.

The young man stood and dusted off his backside.

“Believe it or not, I’m his right-hand man. Though I might just be his little toe.”

“I see.”

Commander Jeong gave a slight nod and asked,

“Do you have an identity tag?”

“An identity tag? Is that something you boil in soup?”

“So you’re a rogue of the martial world. You treat the strict laws established by the Son of Heaven as nonsense.”

“Something like that. Why are you asking all of a sudden?”

“Just a formality. I can’t harm a citizen of the Great Nation who carries an identity tag based on a rash assumption.”

“Hm. You talk like you belong to the authorities.”

“Something like that, but there’s a slight difference.”

“That’s awfully vague. Maybe an example would help me understand?”

“You don’t need to know.”

“Oh.”

At that calm but icy answer, the young man shrugged and dropped something he’d been holding.

Tap.

A faint sound, and a copper badge flashed as it caught the light. Three characters were engraved on its dirt-streaked surface.

Embroidered Uniform Guard.

“Whoops. Dropped it by accident. I was going to take it as a souvenir.”

His tone and voice were exaggerated. But his eyes, fixed on Commander Jeong, had gone cold.

“I was only looking for the flask, but some weird thing came along with it.”

“You’ve got sticky fingers for a rogue of the martial world.”

“Let’s just call this self-defense. If it’d been the person I serve, you wouldn’t have gotten off this easily.”

Instead of answering, Commander Jeong raised a hand.

The Embroidered Uniform Guard had drawn their weapons. They surrounded the young man like a rising wave of steel.

“Before I kill you, I’ll ask you one thing.”

“If you have time, ask as many as you like. I’d like to live a little longer, if possible.”

Something glinted in Commander Jeong’s eyes as he looked at the young man.

This unexpected situation was as good as over.

When the signal came, the young man would be dead in an instant, and they would continue on their way as if nothing had happened.

And yet…

*He has no intention of backing down.*

He was afraid of death, but he would never retreat.

Commander Jeong saw the bearing of a martial artist in the young man.

“What is your name?”

“Hyuk Mujin.”

Commander Jeong nodded to the young man—Hyuk Mujin—and asked,

“Who’s behind this?”

None of this was a coincidence.

Someone whose identity they didn’t know had been waiting for them from the start. They had surely placed people at every chokepoint the procession had to pass through.

Commander Jeong had to find out who was behind it. But the answer he wanted came from somewhere he never would have expected.

“Calling me the mastermind sounds a little grand, but now that I hear it, I kind of like it. Makes me feel like a Constellation, almost.”

There was no presence. No sound.

Yet the shadow of a young man had appeared among them, stretching down from a tree above.

“We finally meet. How’ve you been?”

“Do you… know me?”

At Commander Jeong’s stiff question, the young man laughed.

“How the fuck would I know you, you son of a bitch?”
## Chapter artifact 858

# Chapter 858

This was when I really felt the System’s absence.

If it weren’t for that damn update, a holographic window would’ve appeared by now, accompanied by its signature clear chime.

*Ding.*

> **System**
>
> Quest **Saving Prince Shangshan** successfully completed!
>
> Quest completion rewards have been granted!
>
> You have gained a large amount of EXP!

Something like that.

But reality was quiet, unlike the scene I’d just imagined. The cold killing intent pouring from dozens of Embroidered Uniform Guard members pricked my entire body like needles.

“That’s enough. Take it down and put it away. Keep this up and you’ll put me in a bad mood.”

I tossed out a few words, then pushed off a branch and dropped toward the ground.

No—I walked down through empty air, stepping on it as if it were a staircase.

“Stepping on Empty Air……!”

Someone’s gasp reached my ears. I could almost feel the Embroidered Uniform Guard’s blade-sharp aura waver.

*It burns through internal energy like crazy, but nothing beats it for this.*

No matter how hostile someone was, after seeing something like that, they wouldn’t dare bare their teeth at me.

Stepping on Empty Air was a technique exclusive to Supreme Peak masters.

*Tap.*

I landed lightly on the ground. Waiting for me there was a beast howling miserably.

“Waaah, C-Captain!”

“Stop. Don’t come over here. Shut up.”

“Where have you been all this time?! I was so scared!”

“……”

I’d gone to all that trouble to set the mood, and this bastard—

I let out a deep sigh and pushed Hyuk Mujin away as he kept trying to hug me.

“Ah, quit whining. I didn’t leave you behind.”

“What?”

“I just took a nap up there. I was tired.”

We’d been on the move for over ten days straight.

Even with three jiazi of internal energy and a body beyond human limits, I couldn’t beat the need for sleep. The fact I’d made it this long without collapsing was practically a miracle.

Scouting and night watch, just in case. Checking on the others and looking after them. And on top of that, the mental strain.

If the Divine Physician hadn’t tried to stop me and Jeok Cheongang hadn’t helped, I might have collapsed before we ever reached Jiangsu.

I wasn’t exactly in good shape, either. I’d been sleeping for half a shichen every three days.

After going through all that hell, it was only natural that sleep had hit me the moment we reached our destination and I was sure we’d arrived ahead of the Embroidered Uniform Guard.

“……So you slept? In a tree?”

“Yeah. If I slept on the road, my mouth would get crooked. And I might get attacked while I was out cold.”

“What about me?”

“You? What about you?”

“I’m asking why you threw me down in the middle of the road while you went somewhere safe to sleep by yourself.”

“Someone had to keep watch on the road. And I didn’t throw you.”

“Then what did you do?”

“I set you down. Carefully.”

I’d actually more or less tossed him down. I was that tired.

Hyuk Mujin’s mouth fell open at my slightly dishonest answer.

“So it doesn’t matter if my mouth goes crooked?”

“You’re the kind of man who speaks the truth even with a crooked mouth. That’s Hyuk Mujin.”

“You said we could be attacked!”

“And I’d wake up when I heard it. Like I did just now.”

“I almost died! If you’d woken up moments later, I’d have been a dead man!”

“But I woke up moments earlier. You’re alive.”

“My God. Captain, are you even human?”

I wasn’t sure what gave the bastard who’d been snoring on my back the right to say that, but I decided to show him a little mercy and let it slide.

We’d been pushing ourselves hard, and besides……

The way he’d looked a little while ago had been pretty impressive.

“Good job.”

At my sudden praise, Hyuk Mujin furrowed his brow.

“What?”

“I said you did a good job. Holding on even in a situation like that.”

“……!”

“But don’t do that again. If you think you can’t win, take a step back and think of another way.”

I patted Hyuk Mujin on the shoulder, then slowly turned around and added,

“Right, Your Excellency from the Embroidered Uniform Guard?”

Our eyes met in midair.

His eyes were impassive, showing no particular emotion. Unlike the others, the man at the head of the procession hadn’t so much as blinked at my appearance. He spoke.

“You know that, and yet you blocked our way. Reckless, to say the least.”

“Mister, watch your mouth. I’ve still got plenty of hair.”

“I don’t know what nonsense you’re talking about, but you are standing against the Embroidered Uniform Guard, who are carrying out the Emperor’s command. Do you understand that?”

“Of course I do.”

“I see. So you admit to treason.”

“Treason?”

Could it really be called that?

After a moment’s thought, I decided I ought to take back what I’d said.

“Uh. Then I retract what I said earlier.”

“……?”

“I was walking along, got tired, and took a nap. And then, by coincidence, you happened to pass by. How’s that?”

Hyuk Mujin, who’d been looking at me as though my earlier praise had touched him a little, answered quickly.

“Sounds fine to me.”

“Right?”

“Yes. It’s convincing. Plenty of people sleep rough while traveling.”

“You know what you’re talking about. What can they do if it was an accident?”

“Exactly. Jiangsu isn’t their land.”

“Wait. Isn’t that true, though? Jiangsu or anywhere else, it all belongs to the Great Nation.”

“Huh. Does it work like that?”

“Doesn’t it? That’s what I understand.”

“Captain, since when do you know things like that?”

“You little shit.”

“Sorry. Anyway, I’ll remember that and ask Old Man Nam later…… Hey, where is everybody?”

Just as I was about to answer, the man spoke first.

“What is the meaning of this?”

“Oh, sorry. We got sidetracked for a second. Anyway, now that you mention it, Jiangsu belongs to you lot too, right?”

“All the mountains and rivers under heaven are ruled by His Imperial Majesty, whose authority is—no, why am I even answering this?”

“It’s nice to help each other out.”

“Enough!”

Our frantic conversation seemed to have rattled him.

I narrowed my eyes at the man, whose aura had grown as cold as frost.

“You there, Your Excellency from the Embroidered Uniform Guard. You said you were Commander Jeong, right? Why are you being so stiff about this? Frankly, neither of us stands to gain anything by fighting here.”

*Shing.*

A cold blade appeared in place of an answer. Commander Jeong drew the enormous saber from his back and spoke in a rigid voice.

“It makes no difference who you are. The Embroidered Uniform Guard obeys His Imperial Majesty. If you oppose his command and stand in our way, you will die.”

*Fwoooooosh.*

An invisible force spread out from him. I licked my dry lips as I felt his aura—pure and overwhelmingly heavy.

*Well, look at that……*

I’d suspected it from the moment I first saw him, but the man called Commander Jeong was a formidable master.

No—by ordinary standards, even “formidable” was an understatement. His skill was enough to shatter a prejudice I’d held deep inside.

*He hasn’t crossed the Supreme Peak threshold yet, but he’s at least at the very top of Peak.*

The authorities and Murim were always close and yet far apart.

Murim was one forest within the Great Nation’s borders, but it was full of beasts like dragons and tigers.

And yet, even among those serving the authorities, I’d rarely seen a proper master.

Common soldiers were Third Rate or Second Rate, while martial officers were First Rate at best. Peak masters were rare among those in the military.

*And most of them had been part of Murim before.*

The former Captain of the Guards to the City Lord of Sichuan Province had been a famous wandering martial artist, practically a personal bodyguard. Li Feng, Assistant Military Commissioner of Shanxi Province, was a former lay disciple of Huashan who’d joined the military after passing the military service examination.

But……

*Where’d a master of his caliber come from?*

My experience might not have been all that broad, but as a Supreme Peak master, I could get a rough measure of someone’s ability at a glance.

And Commander Jeong, as I saw him, bore not the slightest trace of a Murim martial artist. He was the very embodiment of a general, from head to toe.

*Even his internal energy is pure.*

What was more surprising was that the other Embroidered Uniform Guard members were no exception.

From young men who looked to be in their twenties to middle-aged men around forty. They varied in skill, but it wasn’t hard to tell that most of them were Peak masters.

*Dozens of Peak masters……*

Their strength matched that of a mid-sized sect—or more.

Whether they lived up to their reputation as the Son of Heaven’s hands and feet, or had been trained by someone other than the Son of Heaven, was a question for later.

I had no intention of letting this standoff continue when neither side stood to gain anything.

“You’ve got a nice aura, but you’d better put away those ugly weapons before someone gets hurt.”

The instant I stepped forward after warning them—

*Whoosh!*

A shaft of light shot straight at my face with a powerful crack of air. I caught it as gently as if I were cradling it, then sent it flying back in the direction it had come from.

*Thud! Boom!*

Instead of a final scream, a tremor rolled through the ground.

The archer, who’d leapt from the saddle of his fallen steed, stared at me in disbelief. An arrow was lodged in the center of the horse’s forehead.

“I told you to put away what you were holding.”

“……!”

“You’re the reason it died, you animal-abusing bastard.”

Hyuk Mujin, scratching his grime-covered body as if he’d known this was coming, said,

“Why is it his fault? You’re the one who killed it, Captain.”

“If we’re getting technical, sure. But Mujin.”

“Yes?”

“I can kill you too.”

“I’m sorry. I spoke out of turn.”

“Good. I’ll accept that.”

It was a peaceful conversation, as usual. But the tension in the courtyard was already so taut it felt ready to burst.

*Snort. Snort.*

Dozens of horses breathed heavily. The hands gripping their reins with all their strength had gone white, and the aura pouring from them wavered but didn’t subside.

At the head of them all stood Commander Jeong.

“You’re crossing a river that should never be crossed.”

“I haven’t crossed it yet, but that aside, you all seem pretty confident. No matter how good you are, you won’t have a good time fighting me.”

“What I and these men place our faith in is not our personal martial skill. It is our loyalty as officials who serve His Imperial Majesty’s command.”

“What’s your name?”

“Jeong Hogun.”

Commander Jeong—Jeong Hogun—had given me his name much more readily than I expected. Then he asked me in return,

“And yours?”

“Jin Taekyung.”

I wasn’t the one who gave that answer.

Jeong Hogun and I both turned our heads. Then we both dropped to one knee and bowed.

*Step.*

Beneath my lowered gaze, someone’s foot came into view—much larger than it had been in the last glimpse I remembered.

With it came a voice that had grown more mature, too. No longer the voice of a little child.

“It’s been a long time, Jin Taekyung of the Jin Family of Taiyuan.”

Prince Shangshan Zhu Bao.

The bloodline of a dragon, grown so much taller, helped me to my feet.

And before I could even answer, he handed me something he’d been holding.

*This is……*

A secret letter.

The moment that secretive word pierced my mind, Prince Shangshan leaned close to my ear and whispered,

“Please give me your autograph.”

“……”

No, Your Highness. What the fuck.
## Chapter artifact 859

# Chapter 859

“Pardon me, but may I say something?”

Jeong Hogun answered calmly as one of his subordinates rode beside him.

“If you think what you have to say is out of line, then don’t say it in the first place.”

“Commander!”

The subordinate’s gaze was deeply troubled, his expression stiff.

He’d shared hardship with Jeong Hogun for more than ten years. The commander already knew what he was going to say without hearing it.

“I can guess well enough how you feel. You’re unhappy with this situation.”

“Unhappy doesn’t begin to cover it. Are you really going to let those rogues carry on like this, Commander?”

The subordinate glared over his shoulder at the slowly moving carriage.

Laughter and conversation poured incessantly through a window left slightly ajar. The subordinate’s expression hardened, as did those of the Embroidered Uniform Guard around him.

“It’s not too late. If you’ll just give the order…”

The subordinate let his voice trail off, but Jeong Hogun understood exactly what he meant.

“You’re thinking of starting a bloodbath?”

“I understand your concerns, Commander. But we can’t just let a band of traitors who defy the Emperor’s supreme command go free.”

“If we can’t let them go free, are you confident you can bring that man down?”

“Well…”

The subordinate was suddenly at a loss for words.

Though he belonged to the military, he was still a martial artist who had trained in martial arts.

The thought of the man laughing and chatting inside the carriage right now made it hard to answer.

Jin Taekyung of the Jin Family of Taiyuan.

No—Jin Taekyung, the Blazing Flame Divine Dragon.

*I’d heard he was still young, but I never imagined he’d be that strong.*

The Embroidered Uniform Guard received all kinds of reports from across the land.

But the stories about the Blazing Flame Divine Dragon were so famous that he’d heard them countless times, even without relying on the spies they had planted far and wide.

A descendant of a fallen martial family.

The heir to the Fire Gate Clan, passed down through a single successor for more than three hundred years.

The troublemaker nobody in Shanxi had failed to hear of had become a Divine Dragon in barely two years. Now he stood at the heart of the turbulent currents shaking Murim.

But there was only one reason Jin Taekyung had become so exceptional.

*His martial might.*

Everything had its limits, and martial arts were no exception.

But Jin Taekyung had already soared far beyond those limits. It was no wonder he was called one of the Two Dragons alongside Cheongpung, the Huashan Divine Dragon, and hailed as a talent unseen in a thousand years.

Nor was it surprising that, after a long silence, Jeong Hogun’s subordinate answered:

“Much as I hate to admit it… in our current situation, we’d have a hard time facing him.”

“If you know that, then that’s enough.”

Jeong Hogun replied evenly. For the Embroidered Uniform Guard, who served the Emperor’s solemn command, it was a humiliating conclusion. But as a soldier, it was the right one.

You had to be clear-eyed about victory and defeat.

If pride led you to make the wrong call, you could never win that battle.

But there was one attitude the Embroidered Uniform Guard could never abandon: never submit or back down before any opponent, no matter how powerful.

“I know how you feel. All of you.”

Jeong Hogun continued in a low voice.

“But the Emperor’s command was to escort His Highness Prince Shangshan to the imperial capital. As discreetly as possible, without causing the slightest disturbance.”

“……”

“If His Highness Prince Shangshan hadn’t ordered us to lower our swords, I would have fought them myself.”

But Prince Shangshan Zhu Bao’s actions had left every member of the Embroidered Uniform Guard stunned.

This young prince, born of the imperial family’s noble blood, had personally helped a rogue of the martial world to his feet—and then asked him to sign the silver token he carried.

“What’s done is done. This matter isn’t ours to decide. Don’t speak of it again.”

At the firm voice, which allowed not even the slightest objection, the subordinate pressed his lips together.

Commander Jeong was right. Their only duty was to escort Prince Shangshan to the imperial capital. Loyalty to the Son of Heaven and authority were two different things.

Then, turning to the subordinate who was struggling to contain his displeasure, Jeong Hogun continued.

This time, he used Sound Transmission, so only one person could hear him.

—I have something for you to do.

The subordinate stared at Jeong Hogun with wide eyes, then moved his lips.

—Give me your orders.

—Go to the Commander-in-Chief in the imperial capital. You, personally.

—To the Commander-in-Chief?

The Commander-in-Chief was the head of the Embroidered Uniform Guard.

Among the high-ranking officials packed into the imperial capital, where all manner of powerful figures gathered, the Commander-in-Chief of the Embroidered Uniform Guard held exceptional influence and authority. And his immense power came from one person alone.

—You mean…

The subordinate didn’t finish his sentence, but both men knew whose rank his words implied.

The Son of Heaven.

Ruler of this vast continent.

A giant who sat upon the throne and looked down over countless officials and subjects.

The very reason the Embroidered Uniform Guard existed—and the one to whom they gave their absolute loyalty.

So Jeong Hogun’s order to inform the Commander-in-Chief was no different from telling him to report directly to the Son of Heaven.

—Commander, what would you have me do?

—Leave at once. Go straight to the Commander-in-Chief and tell him this.

Jeong Hogun continued his Sound Transmission slowly.

—Just as you predicted, uninvited guests have interfered.

—…!

—Go. I won’t be going far.

The subordinate stared at Jeong Hogun, eyes wide with disbelief. Then a faint smile crossed his lips.

A prediction. He’d definitely called it a prediction.

Those two words were enough. His displeasure with his superior, who had seemed so unlike himself, and the Embroidered Uniform Guard’s wounded pride both vanished completely.

—Loyalty!

Unable to shout it aloud, the subordinate gave a vigorous military salute, then rode off like the wind, moving as one with his horse.

Jeong Hogun watched him disappear and thought to himself:

Everything was in the palm of the Embroidered Uniform Guard—or, more precisely, of His Imperial Majesty, the Son of Heaven.

Just as it always had been.

* * *

Senses were like vision.

Just as looking at what was in front of you didn’t erase the scenery around you, I took in every bit of information from all directions with my keen senses, even as I talked.

The small movements of birds bounding through the thick undergrowth.

The cold air swirling around the Embroidered Uniform Guard surrounding the carriage—as if to escort it, or maybe to hem it in.

And…

The sound of a horse’s hooves rapidly fading into the distance.

“I’ve continued to hear news of you. Every time I hear one of those unbelievable tales of your exploits, I can hardly contain my excitement.”

“If you’re hyperventilating, that’s a little concerning. I happen to know a good physician, so why don’t you get a checkup while you’re at it, Your Highness?”

“I’m glad you’re concerned for me. But entrusting my health to a physician I don’t even know would go against imperial etiquette. Once we reach the imperial capital, there will be an Imperial Physician, so…”

“Then I guess there’s no choice. The Divine Physician is exhausted, too, so that’s probably for the best.”

“Wait. Who did you say?”

“The Divine Physician.”

“I’ll see him! I absolutely will!”

“What about imperial etiquette?”

“Rules are there to be broken.”

No matter how noble a member of the imperial family he was, he was still a child.

I humored Prince Shangshan Zhu Bao as he chattered away, his face flushed, and sent a Sound Transmission to Hong Jin, visible over his shoulder.

—They’ve sent someone somewhere. But I really don’t think he’s a scout.

Hong Jin had learned martial arts, but hadn’t reached the Peak realm. Instead of answering with Sound Transmission, he nodded quietly.

He was clearly mindful of the Embroidered Uniform Guard surrounding the carriage.

—He must’ve gone to deliver a message. Any idea where?

Maybe he’d been reading fan wikis or something; while Zhu Bao rambled on about the Divine Physician, Hong Jin used a finger as a brush and wrote in the air.

The imperial capital.

It wasn’t good news, but I’d expected as much.

The Embroidered Uniform Guard had been created by the Great Nation’s Emperor to serve as his own hands and feet. Anything concerning Prince Shangshan Zhu Bao was certain to reach the Emperor’s ears.

*The imperial capital, huh…*

I liked peaches.

But in Murim, “the imperial capital” meant the very center of the world.

Or rather, that was what the Emperor’s position meant.

The ruler of all the people across this vast land. Wherever the Son of Heaven resided was the center of the world, the dragon’s den.

*Though in this case, it’s a tiger’s den.*

I’d never been to the imperial capital, but I’d heard about it often enough.

Enormous buildings that rose so high they seemed to pierce the sky. Beautiful historic sites that made visitors gasp in awe, and wealth pouring through its canals.

With fertile land and abundant supplies, it was practically a paradise on earth—second to none in the world.

Except for one thing.

*The million Imperial Guards protecting the Son of Heaven and the imperial capital.*

Not ten thousand. Not a hundred thousand.

A million.

Even if I allowed for the usual exaggeration from the people of this continent and cut that figure in half, there’d still be an army of over five hundred thousand stationed around Zhejiang Province, where the imperial capital stood.

*That many… Fuck, I can’t even picture it.*

I unconsciously licked my parched lips.

I really didn’t want to be acting like this, but I couldn’t shake the ominous feeling that had haunted me ever since Sichuan.

*What if my suspicion is right, and the Emperor has some sort of relationship with Dark Heaven?*

I didn’t need to think about the answer.

We’d be fucked. Simple as that.

The moment we entered the imperial capital, surrounded by layers upon layers of a million Imperial Guards, it would all be over.

If the Son of Heaven, who was as good as a living god, gave the order, countless blades would come flying at us from every direction. He wouldn’t even have to say much. He’d just point at us and say one thing:

“They’re dangerous traitors.”

“……”

Just imagining it made my legs go weak.

I’d gone quiet, and Hyuk Mujin, huddled in a corner of the carriage, asked cautiously,

“Why do you look like you’ve got a mouthful of shit?”

“……Mujin.”

“Yes, Captain.”

“You’re always so careful with your tone. Why is the content of what you say so damn bold?”

“Because I’m the manliest of men. Hyuk Mujin, the Tenfold Man—with enough manliness for ten men! That’s me.”

“……”

Is this guy actually insane?

I was silently hurling every insult I could think of at Hyuk Mujin with my eyes when Prince Shangshan Zhu Bao, who had stopped to listen to us, let out a quiet gasp.

“The Tenfold Man? That is an extraordinary title. Just what I’d expect from your subordinate.”

“……?”

“……?”

“It’s fate that we’ve met like this. You said your name is Hyuk Mujin, the Tenfold Man?”

Hyuk Mujin blinked, then hurriedly bowed his head.

“Y-Yes, Your Highness Prince Shangshan. But I’m sorry to say my title isn’t the Tenfold Man…”

“Come here and sign this.”

“Pardon?”

“No need to refuse. Hyuk Mujin, the Tenfold Man. This shall be an honor passed down through your family for generations.”

“……”

“……”

Hyuk Mujin took the bronze token Prince Zhu Bao handed him and inscribed his new title on it.

Watching him, I thought:

What a fucking mess. Seriously.

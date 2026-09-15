# Checkpoint Review — 200–204

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

# Chapters 200–204

## Plot

Jeok Cheongang identifies Jin Taekyung as possessing the rare Heavenly Martial Physique and agrees to oversee his training, despite continuing to deny that they are truly master and Disciple. Taekyung begins calling him Master publicly and Old Master in private.

Jeok tests Taekyung with the Peak-Grade One Step Back Quest, requiring him to force Jeok back one step within thirty minutes. By persuading Jeok to defend without attacking, Taekyung channels all his internal energy into One Annihilation and drives Jeok back five steps, completing the Quest. He collapses from exhaustion; Jeok admits defeat and tends to him, resolving to guide Taekyung toward becoming a Heavenly Dragon.

After Taekyung receives two level-ups and 20 Bonus Points, Jeok immobilizes him, feeds him three Scorching Yang Qi elixirs, and opens hundreds of his acupoints. Taekyung survives the dangerous forced opening of the Conception and Governor Vessels. The System confirms both vessels are open and the related Quest is complete, but Taekyung loses consciousness before the achievement rewards are revealed.

Jeok carries Taekyung away, impressed by his mental strength and believing the Heavenly Martial Physique chose its master well. Meanwhile, Ak Bulgun receives a letter from Heaven’s Gate Temple and asks Jin Wikyung for help after reading it; the letter’s contents remain undisclosed.

## Continuity

- Jeok Cheongang believes Taekyung possesses the Heavenly Martial Physique and has begun personally training him.
- Taekyung addresses Jeok as Master publicly and Old Master privately; Jeok still verbally denies their formal master-Disciple relationship.
- The One Step Back Quest is complete. Taekyung forced Jeok back five steps with One Annihilation after Jeok agreed to defend only.
- Completing the Quest granted Taekyung two level-ups and 20 Bonus Points.
- Taekyung absorbed more than thirty years of energy from three Scorching Yang Qi elixirs and expelled substantial turbid qi.
- Taekyung successfully opened both the Conception Vessel and Governor Vessel, completing the Conception and Governor Vessels Quest. Opening the Conception Vessel greatly improves qi handling and the circulation and accumulation of internal energy.
- The rewards for the Conception Vessel Opening Achievement and the rare achievement from completing the vessel Quest remain unrevealed.
- Jeok believes Taekyung’s mental strength matches his extraordinary physique and hints that an anticipated event may occur sooner than expected; he says he must endure for several more years.
- Jin Mukyung remains secluded and refuses to return to Heaven’s Gate Temple until he achieves complete mastery.
- Heaven’s Gate Temple may expel cadets, including members of the Ten Dragons and Phoenixes, who fail to return by the appointed deadline.
- Ak Bulgun has received an undisclosed letter from Heaven’s Gate Temple and requested Jin Wikyung’s assistance.

## Translation Decisions

- Retain “Heavenly Martial Physique,” “Heavenly Dragon,” and “One Step Back.”
- Render 혈도 타통 as “Acupoint Opening,” 회음혈 as “Huiyin Acupoint,” 임맥 타통 as “Conception Vessel Opening,” and 임독양맥 as “Conception and Governor Vessels.”
- Retain “Scorching Yang Qi,” “turbid qi,” “Fire Spirit Grass,” “Red Flower Grass,” and “Flame Red Grass.”
- Preserve the distinction between Taekyung’s public “Master” and private “Old Master.”
- Preserve the unresolved contents of Heaven’s Gate Temple’s letter and the event Jeok believes may occur sooner than expected.

## Durable state

{
  "active_continuity": [
    "One Step Back grants Taekyung two level-ups and 20 Bonus Points.",
    "Jeok selects three Scorching Yang Qi elixirs to begin Taekyung's Fire Gate Clan training.",
    "Jeok immobilizes Taekyung and performs acupoint opening using the elixirs and his internal energy.",
    "Taekyung's Heavenly Martial Physique rapidly absorbs the elixirs' more-than-thirty years of energy and expels substantial turbid qi.",
    "Jeok successfully opens Taekyung's Conception and Governor Vessels; Taekyung completes the related Quest and loses consciousness.",
    "Opening the Conception Vessel greatly improves qi handling and the circulation and accumulation of internal energy; the achievement rewards remain undisclosed.",
    "Jeok now considers Taekyung's mental strength exceptional and believes the Heavenly Martial Physique chose its master well.",
    "Jin Mukyung remains secluded in the training hall and refuses to return to Heaven's Gate Temple until he achieves complete mastery.",
    "Heaven's Gate Temple may expel cadets who fail to return by the appointed date, including members of the Ten Dragons and Phoenixes.",
    "Ak Bulgun receives an undisclosed Heaven's Gate Temple letter and asks Jin Wikyung for help after reading it."
  ],
  "continuity_sources": [
    204
  ],
  "open_questions": [
    "What are the rewards for the Conception Vessel Opening Achievement and the rare Achievement earned after completing the Conception and Governor Vessels Quest?",
    "What does the Heaven's Gate Temple letter request from Ak Bulgun and Jin Wikyung?",
    "Will Jin Mukyung return to Heaven's Gate Temple before the appointed deadline?",
    "What event does Jeok Cheongang believe may occur sooner than expected, and why must he endure for several more years?"
  ],
  "safe_through": 204,
  "temporary_decisions": [
    "Render 혈도 타통 as “Acupoint Opening.”",
    "Render 회음혈 as “Huiyin Acupoint.”",
    "Render 임맥 타통 as “Conception Vessel Opening.”",
    "Render 화령초 as “Fire Spirit Grass,” 홍화초 as “Red Flower Grass,” and 염적초 as “Flame Red Grass.”",
    "Render 탁기 as “turbid qi.”"
  ],
  "version": 1
}

## Reading copies

## Chapter artifact 200

# Chapter 200

“I asked whether this old man couldn’t be your master.”

“Pardon?”

What the hell was he talking about? Taken out of context, that line could put a romance-drama male lead to shame.

I covered my vital areas and slowly backed away.

“What?”

“N-Nothing. But what do you mean?”

“Forget it. Pretend you never heard me.”

Jeok Cheongang’s expression was strange. He stared at me with a face that mixed inexplicable expectation, irritation, and disappointment, then suddenly opened his mouth.

“You possess the Heavenly Martial Physique.”

“Heavenly Martial what?”

Jeok Cheongang frowned at my reaction.

“You don’t know about the Heavenly Martial Physique? Are you making fun of this old man?”

“I’m hearing it for the first time in my life.”

“…”

*Heaven truly is heartless. How could it give such a thing to someone like this?*

He looked like he genuinely wanted to hit me.

Jeok Cheongang trembled as he clutched his liquor bottle, then let out a sigh.

“Then do you know anything about the Nine Yin Severed Meridians?”

“Oh, the Nine Yin Severed Meridians. I know about that.”

I had seen it plenty of times in the past. Was this the same thing?

I rummaged through my old memories and pulled out a few keywords related to the Nine Yin Severed Meridians.

“An unusual constitution. Painful. Intelligent. Dies young instead.”

“…”

“Am I wrong?”

“You have the gist of it. It is a type of severed-meridian condition in which powerful innate yin energy blocks the meridians and leads to death before long.”

“Then what about the Heavenly Martial Physique?”

A sense of unease began creeping up from somewhere in my chest. The fact that he had used the Nine Yin Severed Meridians as an example made it worse.

*What if it lets me learn martial arts quickly, but I have some problem that makes me die young? That would be a disaster.*

Jeok Cheongang spoke with a solemn expression.

“The Heavenly Martial Physique is a martial constitution bestowed by Heaven, one that appears perhaps once every several hundred years.”

*Bones and muscles bestowed by Heaven?* It sounded incredible just hearing about it.

Which only made me more nervous. The Nine Yin Severed Meridians were practically a double-edged sword that traded genius-level intelligence for a short lifespan.

I stared tensely at Jeok Cheongang’s mouth.

“And?”

“What do you mean, ‘and’?”

“When am I going to die?”

“Why would you die?”

“I think I’ve been having headaches and feeling nauseous lately. My bones and joints ache even now.”

Doctor Choi Tae—no, Jeok Cheongang—gave me a short and concise diagnosis.

“That’s because this old man beat you.”

“Oh.”

“You didn’t seriously think the Heavenly Martial Physique caused you to die young like the Nine Yin Severed Meridians, did you?”

“…”

“Have you lost your mind?”

Jeok Cheongang shook his head in disbelief.

“The Heavenly Martial Physique and a severed-meridian illness like the Nine Yin Severed Meridians are as different as Heaven and Earth. Do you think it’s called something bestowed by Heaven for no reason? You were born with that body in the first place. You were born blessed by heavenly fortune.”

“Me?”

“I heard from the Lesser Family Head that you’ve only been seriously learning martial arts for three months. Do you truly think your achievements so far would have been possible through effort alone?”

“Not really.”

“You are where you are because you possess a constitution that lets you make any martial art your own faster than anyone else.”

Jeok Cheongang was only half right.

The reason I didn’t bother correcting him was that what had been added to my effort wasn’t an innate constitution. It was the System.

*If I really possessed the Heavenly Martial Physique, I wouldn’t have remained Third Rate until I reached twenty.*

A promising tree showed its potential from the very beginning.

If the real Jin Taekyung—the previous owner of this body—had been born with such heavenly fortune, he would surely have distinguished himself long ago.

*This body doesn’t possess the Heavenly Martial Physique.*

I looked down at both my hands. The size and length of my arms and hands, the shape of my muscles, and the strength hidden within them.

Everything was perfectly balanced, without the slightest deviation.

*The System.*

The points I gained from leveling up and training were converted into stats. And the System distributed those stats evenly.

It ensured that every tiny gear inside my body, down to the smallest and most delicate one, meshed together perfectly.

*Since it isn’t innate, it isn’t exactly the Heavenly Martial Physique… But at this level, could I call it an acquired Heavenly Martial Physique?*

Jeok Cheongang had seen my body with his own eyes, so it wasn’t strange that he had mistaken it for one.

And from my perspective, it was better to let him continue making that mistake.

It had taken only three months for a Third Rate wastrel who did nothing but drink to become a Peak master.

Without the Heavenly Martial Physique, people might reasonably suspect me of practicing demonic arts.

*Either way, this worked out nicely.*

The fact that even a Supreme Peak master like Jeok Cheongang could mistake my constitution for the Heavenly Martial Physique proved beyond doubt that my bones and muscles were exceptional.

And since I had none of the side effects associated with the Nine Yin Severed Meridians, it was a complete win.

*Is my path finally paved with flowers?*

When I thought about everything I had suffered until now, tears welled up in my eyes.

I was lost in my emotions when I suddenly felt someone’s gaze and turned my head.

Jeok Cheongang flinched when our eyes met, then abruptly looked up at the sky.

“T-The moon is bright.”

I followed his gaze and mumbled:

“There are thick clouds covering it.”

“…”

“Did you have something to say?”

“Cough. Ahem.”

After clearing his throat several times, Jeok Cheongang cautiously opened his mouth.

“As you know, this old man owes you a debt.”

“So?”

“I’m asking because I want to settle the matter properly before leaving this place. Is there anything you want from this old man?”

Actually, there wasn’t anything in particular.

If I had to name one thing, it would be for him to take back what he had said earlier.

But there was no chance Jeok Cheongang would do that for the sake of his dignity. I had to come up with a request he could reasonably fulfill.

I scratched my head.

“Well, I haven’t really thought about it in detail, so I’m not sure.”

“Then think about it in detail.”

“Oh, I’ll tell you later if I think of something. You’ll have to stay a few more days before you leave anyway.”

But Jeok Cheongang was firm.

“Right now.”

“Pardon?”

“I’m telling you to say it right now. There’s nothing to think about, is there?”

As he urged me, Jeok Cheongang added in a mumbling voice:

“For example, perhaps you want to learn martial arts from this old man. Or maybe you want to learn martial arts from this old man. Or you might want to learn martial arts from this old man. Something like that.”

“…”

“It was only an example. Don’t concern yourself with it.”

“…”

“Ahem. Is there phlegm stuck in my throat? Ahem!”

I watched him quietly before opening my mouth.

“Great Hero Jeok. I’m asking just in case.”

“Ahem! Ahem!”

“Do you want to take me as your Disciple?”

At that moment, Jeok Cheongang’s body froze in the middle of his loud coughing fit. His pupils shook as though an earthquake had struck them.

“W-What are you talking about?”

“You heard me.”

“H-How absurd. You think this old man wants to take you as his Disciple?”

“…”

*Yes. It really looks that way.*

At first, I wondered if I was imagining it, but by this point, anyone who still didn’t get it would have to be a fucking idiot.

When I merely stared at him without saying anything, Jeok Cheongang became flustered instead.

“You little bastard! What is that insolent look in your eyes?”

“I’m just looking at you. Don’t worry about it.”

“You seem to be laboring under some serious misconception, but you’re wrong about everything.”

“Ah. Yes.”

“Do you think I would decide so easily on the successor to our sect’s lineage, which carries a long and venerable history?”

“You decided pretty easily earlier. And you said it in front of all those people, so you can’t take it back.”

“Th-That… I can simply take another Disciple.”

“You said it was a single-successor, no-outside-transmission tradition, didn’t you? Regardless, everyone in the world will think I’m the successor to the Fire Gate Clan.”

Jeok Cheongang had been struck right in the heart of the matter. He shouted:

“There isn’t a single reason for me to take you as my Disciple!”

“I possess the Heavenly Martial Physique.”

“Gasp.”

“It took me about three months to go from Third Rate to Peak. I wonder how long it’ll take me to reach Supreme Peak.”

“Y-You bastard. Do you think it’s that easy? Do you think Supreme Peak is some mutt’s name?”

“It was easy for me.”

“…”

How many times had I crossed the threshold of death?

It had been brutally difficult and painful, but from this point onward, it was going to be easy no matter what.

While Jeok Cheongang struggled to find words, I mumbled as though speaking to myself:

“Actually, Supreme Peak might be difficult.”

“Of course it is.”

“Would around thirty work?”

Jeok Cheongang’s mouth fell open.

“Th-Thirty? Supreme Peak?”

“Ah, did I set the goal too far away? I only said that because it seemed difficult.”

I sighed as I glanced sideways at him.

“Still, you must have been much faster than me, Great Hero Jeok. You’re powerful enough to rank among the Ten Kings, after all. And you had the Fire Gate Clan’s martial arts, too. Wow, I’m jealous. If I learned advanced martial arts like those, I’d become strong in no time.”

“!”

Jeok Cheongang stared at me with trembling eyes. I could easily imagine what sort of scene was unfolding in his mind.

*What would happen if the Heavenly Martial Physique met the Fire Gate Clan’s supreme martial arts?*

I had already displayed unbelievable achievements in only three months. It was possible that an unprecedented monster, unlike anything seen in history, would be born.

*I’m almost there.*

Unable to speak because of his pride, Jeok Cheongang hesitated. I drove in the final nail.

“Actually, this won’t do. I’m thinking of visiting Huashan once this gathering ends.”

“Huashan? Why would you go there?”

“Because of Great Hero Sword Saint Mae Jonghak. I hear the two of you are quite close, so if I explain my circumstances properly, I might be able to become his Disciple without letting the rumor spread…”

“No!”

The shout burst out before Jeok Cheongang could stop it. He flinched and swallowed dryly.

“If you happen to be considering that…”

“Pardon? I can’t hear you. You’re speaking too quietly.”

“Hoo.”

After steadying his breath, Jeok Cheongang spoke again.

“If you’re interested, this old man could personally oversee your martial arts training.”

I widened my eyes as though genuinely surprised.

“Are you serious?”

“Of course. A debt must be repaid, mustn’t it?”

Perhaps he had belatedly decided that he needed to maintain his dignity. His voice was more stern than it had been until now.

*It’s too late for that, old man.*

I barely held back a laugh and answered:

“What you’ve already done is more than enough.”

“It is this old man’s principle to repay a debt tenfold, even twentyfold.”

“I see.”

“Exactly.”

“But aren’t you leaving in a few days anyway? You seem very busy.”

“It can be postponed. I plan to leave once you have achieved a certain level of progress.”

“Ah, so you’re the type who sees things through once you start.”

“It’s simply my nature.”

“What if I fail to achieve the level of progress you want, Great Hero Jeok?”

Jeok Cheongang deliberately hardened his expression.

“Hey, you little bastard! How can you decide in advance that you’ll fail?”

“I’m sorry. I just don’t know how many years it might take.”

“Did you already forget what sort of person I said I was?”

“The type who sees things through once you start?”

“Once a martial artist draws his sword, he should see it through—even if he has to cut down a mountain.”

“Wow, that’s amazing. As expected of you, Great Hero Jeok!”

I gave him a thumbs-up and asked in a suggestive voice:

“But at this point, doesn’t that make us master and Disciple?”

“!”

After a brief silence, Jeok Cheongang vigorously shook his head.

“Master and Disciple? What nonsense! I’m merely repaying a debt.”

“Oh, I see. I misunderstood your intentions, Great Hero Jeok. Please accept my sincere apologies.”

“…”

Jeok Cheongang gave an uncomfortable cough before speaking.

“But I think we need to change the way you address me.”

“The way I address you?”

“Although we are not, well, truly master and Disciple, there are people watching. Shouldn’t we at least make it look right?”

“That’s true.”

*The way I address him? What should I call him?*

After a brief moment of thought, one word slipped from my mouth.

“Then should I call you Master from now on?”

“…”

“Master?”

“H-Huh?”

Jeok Cheongang came to his senses as though he had just woken up and stared at me with a complicated, subtle gaze.

“Yes. That would be good.”

“Yes. Then when it’s just the two of us…”

“Old Master. Call me that.”

“Understood. Old Master.”

I bowed deeply toward him.

The Supreme Peak master whose fame resounded throughout the world, Fire King Jeok Cheongang.

It was the moment my subtle relationship with him began.

* * *

After sending Jin Taekyung back, Jeok Cheongang leaned against an old wall.

The voice he had just heard continued to echo inside his head.

*Master.*

It had been ten years.

Ten years since someone had called him Master.

Jin Taekyung’s build, face, and personality were all different, but Jeok Cheongang was reminded of his dead Disciple when he looked at him.

As Jeok Cheongang quietly sank into thought, a faint smile suddenly appeared at the corner of his wrinkled mouth.

*Not bad.*

He had never imagined things would turn out this way, but he didn’t feel bad about it.

No, he even felt an expectation for the future and an inexplicable sense of cheerfulness.

“Not bad. Truly.”

Jeok Cheongang gave a quiet laugh and looked up at the sky.

At some point, the clouds had cleared, revealing a bright moon.
## Chapter artifact 201

# Chapter 201

“It’s been hard to catch sight of you lately.”

“Tell me about it. These days, I can’t tell whether I’m a bodyguard or a chief steward.”

At Wipeng’s complaint, Jin Wikyung let out a quiet laugh.

“Bear with it for a few more days. More importantly, how did the matters we discussed last time turn out?”

“Everything is proceeding smoothly. The Sect Leaders we brought into the fold are obedient, and the local authorities and merchant world are actively cooperating.”

If the Jin Family of Taiyuan was a ship riding a favorable wind, Jin Wikyung was its seasoned captain.

Beginning with securing the loyalty of the smaller and mid-sized sects on the first day of the gathering, he had handled one major matter after another.

The Fire King was holding down the Murim side of things, while Prince Shangshan, a member of the imperial family, was holding down the authorities. As a result, there had been no trouble at all.

*As for the merchant world, there was never any question.*

Merchants were more sensitive to profit than anyone. Once they smelled money, it was only natural for them to come rushing in.

After quickly organizing his thoughts, Jin Wikyung asked Wipeng:

“What about the budget? How much do you think we’ll have left?”

“We’re short.”

“What?”

At Jin Wikyung’s startled expression, the corners of Wipeng’s mouth rose.

“I mean that we’re short on warehouses to store the wealth.”

“……Phew.”

“Two warehouses were already full two days ago. The wealth that came in after that is being stored in empty pavilions.”

Jin Wikyung released a sigh of relief and gave a quiet laugh.

“What a haul.”

“Great Hero Jeok’s announcement yesterday was decisive. It gave certainty to those who had still been wavering until the end.”

“They’re the real heavyweights.”

“Indeed.”

The wider a person’s connections, the more likely they were to get pricked by thorns.

The Jin Family of Taiyuan was clearly a goose laying golden eggs, but there were also powerful sects and great families—including the Zhongnan Sect—with which it had an uneasy relationship because of the Fire King.

“Seok Family Manor suddenly requesting a private meeting after remaining quiet all this time must be because of that.”

Seok Family Manor was one of the greatest merchant houses in the world.

The fact that they had stepped forward was proof of how certain they were of the Jin Family of Taiyuan’s potential.

“Isn’t weighing the situation their defining trait? Since they were late to the party, they’ll make up for it with a generous gift.”

“They should. Have them come in.”

“Yes, my lord.”

Not long after Wipeng left, a fleshy middle-aged man entered the office.

“Oh, my! Lesser Family Head! How long has it been?”

“It’s been a long time, Chief Ha.”

The middle-aged man was one of Seok Family Manor’s five Outer Stewards. Though he was only one of five, the authority he possessed was immense.

Jin Wikyung smiled gently at the man, who kept wiping away his sweat.

“It’s been three years since we last met. How is your Lord?”

“He’s as hale and hearty as a young man in his prime. As it happens, he heard the happy news this time and wishes to meet you. As you know, Lesser Family Head, he wasn’t feeling well the last time……”

“Yes, I remember. Quite clearly.”

Jin Wikyung remembered that day three years ago as though it had happened yesterday.

He had waited a full fifteen days before being granted a private audience, only to leave Seok Family Manor as though he had been chased out without ever seeing the Lord’s face.

Finding the sedan chair of a high-ranking official in front of Seok Family Manor’s main gate had been a coincidence.

That was what he had chosen to believe.

*That’s how the Murim works.*

But now, their positions had changed.

The past three years had been short but eventful, and the arrogant Outer Steward who had treated him like a beggar had somehow become a humble merchant.

*I didn’t know this man even knew how to use honorifics. That’s a first.*

With a strange sense of amusement, Jin Wikyung listened carefully to Chief Ha.

He readily accepted Seok Family Manor’s proposal to enter the Shanxi merchant world in earnest with the Jin Family of Taiyuan’s cooperation.

Naturally, the details would need to be reviewed, but Seok Family Manor’s offer was extraordinarily generous.

“You’ve made a better offer than I expected. Generous enough to make me wonder whether this is really all right.”

Chief Ha rubbed his hands together and laughed.

“I’m a merchant to the bone. I never conduct business at a loss.”

There were different levels among merchants.

A Third Rate merchant exchanged goods. A Second Rate merchant purchased goods that could leave him a profit. A First Rate merchant bought the future.

Seok Family Manor was one of the greatest merchant houses in the world. They were aiming not for an immediate profit, but for dozens of times that profit in the years to come.

*You won’t make that much off us. Our family will never dance to your tune.*

Unlike his thoughts, Jin Wikyung smiled broadly.

Life in this world was not easy enough to reveal one’s true feelings and say everything one wanted to say. That was even more true with a cunning merchant.

“I’ll arrange a place for you to stay. We can discuss the finer details then.”

“Thank you, Lesser Family Head.”

Chief Ha was about to rise from his seat when he stopped.

“Um……”

“Do you have another matter to discuss?”

“This is a difficult request, but might I be allowed to meet Great Hero Jeok?”

The Outer Steward of Seok Family Manor was a man of considerable authority, but the Fire King was an exception. Since he had begun staying at the Jin Family of Taiyuan, Jeok Cheongang had permitted none of the honored guests to meet him privately.

Chief Ha continued, wiping away his sweat.

“It’s been extraordinarily difficult. I tried going to him myself, and I even sent my subordinates to discreetly request a meeting, but……”

“Oh, dear. Great Hero Jeok probably didn’t take that well.”

“No. My subordinate came back nearly crippled. That’s why I’m shamelessly asking you for a favor, Lesser Family Head.”

Suppressing his laughter, Jin Wikyung answered:

“Well, I can’t say for certain. It might be possible after the gathering ends, but it will be difficult over the next few days.”

“I noticed he hasn’t been seen since yesterday. May I ask why?”

“He must be instructing my youngest brother.”

“Ah, I see. My apologies for intruding.”

As soon as Chief Ha left the office, Jin Wikyung could no longer hold back his laughter.

The fatigue in both his body and mind from hosting the gathering for several days seemed to lift all at once. In a cheerful voice, he called for his most trusted subordinate.

“Wipeng. Who’s next?”

* * *

Before dawn, before the sun had even risen.

The person who woke me was neither Hyuk Mujin nor Cheongpung.

Splaash!

“Gah!”

The first thing I saw after opening my eyes to the cold-water ambush was Jeok Cheongang, glaring at me with his eyes wide open.

“W-What are you doing?”

“You slept like the dead until this hour. Are you out of your mind?”

“I only slept for two shichen.[^1] What do you mean, I slept until this hour?”

Jeok Cheongang started lecturing me as I stared at him in disbelief.

“In four hours, you bastard, this old man could swing a weapon a thousand more times. And where did you learn the disrespect of not even paying your morning respects to your Master?”

“……Master?”

Jeok Cheongang flinched and stammered for a moment.

“W-We need to look that way to other people, don’t we?”

“……”

“To avoid suspicion, we need to act like a real master! Like a real Disciple! That’s the bare minimum!”

“Ah, yes.”

So the pioneer of method acting in the Murim was right here.

At my lukewarm response, Jeok Cheongang’s face grew bright red.

“Regardless, I won’t stand for you loafing around like this. Come with me. Now.”

“Where?”

“There’s a place this old man has picked out.”

I thought he had found a secluded training ground, but the place Jeok Cheongang took me was not inside the Jin Family of Taiyuan. It was a nearby mountain.

Trees with trunks easily several meters around grew thickly in every direction, and the ground was firm.

“This will do.”

Jeok Cheongang stopped in a wide clearing and placed the pack on his back atop a tree stump.

“What’s that?”

“Don’t worry about it. It’s something we’ll use later.”

“Later?”

“Yes. They’re things that will make you writhe with pleasure.”

“……”

Why was I suddenly thinking of whips, candlesticks, and masks?

As I cast anxious sidelong glances at the pack, Jeok Cheongang spoke with a stern expression.

“Stop taking an unnecessary interest in it and take out your spear.”

“Ah, yes.”

I’d had the good sense to bring several spears along, and I planted them in the ground.

The reason Jeok Cheongang had come to find me so early was obvious.

*Training.*

Though he tried hard not to show it, Jeok Cheongang wanted to take me as his Disciple.

The reason he kept stubbornly denying it was that he still wasn’t certain himself.

*He’s already made one painful mistake.*

The emotional wound Jopil had inflicted on Jeok Cheongang had not yet healed.

That was why he would surely continue watching and thinking before deciding whether he could accept someone like me as his Disciple.

*Even if he doesn’t pass down the Fire Gate Clan’s supreme martial arts right away, he’ll still do his best to teach me.*

This was instruction from a Supreme Peak master.

A single word from someone who had gone farther ahead and conquered a longer path than I had was worth more than a thousand pieces of gold.

I lifted one of the well-balanced iron spears and swallowed.

“What do I do now?”

“Attack me.”

“Pardon?”

“I said attack me. With all your strength.”

A smile appeared around Jeok Cheongang’s wrinkled mouth.

“Thirty minutes. If you can make this old man retreat even one step, you win.”

Ding.

> **System**
>
> Quest **One Step Back** has been created.
>
> **Quest**
>
> **One Step Back**
>
> Fire King Jeok Cheongang wants to see your true ability.
>
> Make him retreat within the time limit and imprint your worth upon him!
>
> **Grade:** Peak
>
> **Restriction:** Jin Taekyung
>
> **Mission:** One Step Back (Incomplete)
>
> **Reward:** ???
>
> **Failure:** ???

*Make him retreat one step?*

At first glance, it seemed easy, but there was a reason it was a Peak-Grade Quest.

Especially when the opponent was Fire King Jeok Cheongang.

I took my eyes off the Quest window and saw Jeok Cheongang standing there with a relaxed expression.

“All right. Begin.”

Beep.

> **System**
>
> **29:59**

At the instant the time-limit window appeared in the air, I kicked off the ground and charged toward him.

Whooosh!

* * *

Whoosh!

The spearhead tore through the air. Compressed air burst outward, sending the old man’s white hair flying.

Having dodged the first spear Jin Taekyung thrust at him, Jeok Cheongang thought:

*What is this kid?*

He was fast.

And the spear carried enough force to shatter a boulder.

Even for Jeok Cheongang, who had already examined Jin Taekyung’s body once, the speed and strength were beyond anything he had expected.

Whirl, whoosh! Boom!

Second strike, third, fourth……

He stabbed, slashed, and swept upward.

Every time Jeok Cheongang evaded the shower of spearheads pouring down like torrential rain, his astonishment grew like a snowball.

*He’s seasoned. As if he was born on a battlefield.*

He was only twenty-one. Yet the trajectories and movements traced by his spearhead were no worse than those of any famous master in the martial world.

No—if anything, they were better.

After encountering countless martial artists during the Great Faction War, Jeok Cheongang had learned something well.

*A true martial artist is forged through countless real battles.*

The Nine Sects and One Gang.

The Five Great Families.

They were certainly great powers that held sway over the world, but only a small number of their members had ever experienced surviving at the brink of death.

That was why the Demonic Cult, which had grown through conquest and the principle of Might Makes Right, had been able to swallow half the Central Plains.

How many disciples of prestigious great sects had died at the beginning of the war?

*But this kid is different.*

There was no hollow opening stance or hesitation.

The spearhead that relentlessly targeted the vital points throughout his body and the cold, hardened eyes were marks possessed only by someone who had experienced countless real battles and seen blood.

Shriiiik, whoosh!

The spinning spearhead vibrated.

Humm. Humm. Humm.

The sound was like hundreds of bees beating their wings, and the spearhead shooting toward him was sharper than a poisonous stinger.

*He’s only been practicing martial arts for three months? Someone like this?*

Judging by his movements alone, it seemed not three months but three years.

No—thirty years.

Jeok Cheongang knew nothing of Jin Taekyung’s battle-scarred seven years. All he could do was marvel.

*……What an incredible kid.*

Jeok Cheongang himself had spent his entire life obsessed with martial arts.

Yet even for someone who had achieved a great realm, what Jin Taekyung was displaying now was incomprehensible.

*The greatest martial talent in history, was it?*

Remembering Jin Wikyung’s words, Jeok Cheongang’s body trembled with joy and awe.

*Yes. You were right.*

It was then, as he slowly closed his eyes, savoring the lingering emotion.

Whoosh!

A streak of light shot toward his chest.

Jeok Cheongang’s eyes opened halfway. At the same time, his wrinkled hand seized the spearhead.

Crack!

His hands were already blazing with red flames. They crushed and melted the spearhead.

Molten metal dripped onto the ground, hardened by the cold wind.

“……Wow, shit. Isn’t that cheating?”

Jin Taekyung muttered in disbelief.

Jeok Cheongang grinned at him.

“Now we’re getting started.”

[^1]: A *shichen* is a traditional time unit of approximately two hours.
## Chapter artifact 202

# Chapter 202

Half an hour. A full thirty minutes.

I thought that even if my opponent was the Fire King, if I put everything I had into it, I could make him retreat a little—a very little.

At least, I had thought so until just now.

*How does that make any sense?*

I backed away with a stunned expression.

He had caught a spearhead spinning with internal energy in his bare hand. That made about as much sense as sticking your hand into a grinder.

But if the owner of that hand was Jeok Cheongang, the Fire King, the story changed.

Drip, hiss.

When the molten metal struck the ground, steam rose into the air. Jeok Cheongang clicked his tongue at the sight.

“Maybe it melted so quickly because it was scrap iron. We’ve probably received plenty of wealth this time, so tell them to use better iron.”

“H-How did you do that?”

“You can do it too.”

“Me?”

“Of course. If you possess at least two jiazi’s worth of internal energy[^1] and master our sect’s martial arts to the utmost.”

“……”

“Easy, right?”

As if it were easy.

When I made an incredulous face, Jeok Cheongang opened his mouth and let out a huge yawn.

“You have plenty of time to spare. If I were you, I’d spend it swinging my spear one more time.”

“I was just about to.”

I glanced at the time limit floating in the air and pulled out another spear.

Sixteen minutes remained. Nearly half the time had already passed.

*I only need to make him retreat one step. Just one step…*

But that was easier said than done.

I glared at Jeok Cheongang, who was standing leisurely in the same spot as before, and drew in a deep breath.

“Huuup—”

Whoosh!

At the same time, I kicked off the ground and charged. With one long stride that erased the distance between us, I thrust out my spear.

Screeeech!

The corners of Jeok Cheongang’s mouth rose as he watched me.

“I believe I said we were just getting started.”

Boom!

He stamped his foot just once.

The effect was terrifying.

The ground shook as though an earthquake had struck, and a flock of birds perched on the bare branches took flight.

In the slowed-down world, Jeok Cheongang’s hand blurred for an instant and struck away dozens of stones floating in the air.

Straight toward me.

Shishishishik!

The dozens of stones had been fired with internal energy. Each one was no different from a deadly hidden weapon.

They must have possessed even greater destructive power than the Head Elder’s finger-flicking technique I had faced in the past.

But…

*I’ve grown stronger too.*

Humm. Humm. Humm.

My spear let out a deep hum.

I felt a unity with it on an entirely different level from when I had remained at First Rate.

The Jin Family’s Spear Technique, which had already reached grand mastery, and my footwork technique had achieved perfect unity.

The insight I had gained after crossing the wall of the Peak realm had melted into them, revealing spear paths I could never have imagined before.

And then there were my increased stats.

*I can do this.*

Crack.

The spear shaft buckled under the force of my crushing grip.

And in the next moment—

Whoooosh!

The power compressed like a spring shot forward. Wind burst from the arc of the spearhead as I swung it sideways with all my strength.

It was the release of internal energy—and a storm I had summoned.

Pssshhh.

Fine dust scattered in every direction. They were the last traces of the stones caught in the spear’s path.

“Huh. Look at you.”

The obstacle was gone. Now it was time to strike his body.

I charged at Jeok Cheongang, who looked both dumbfounded and pleased.

Whoosh! Shishishishik!

The spearhead, brimming with internal energy, cut through the air.

Jeok Cheongang bent lightly at the waist and dodged it. At the same time, heat surged from his right hand.

Whoom!

Blazing flames shot out. It was a mass of qi condensed from powerful Scorching Yang Qi.

I gritted my teeth and swung the spear shaft.

Clang! Krrrra-boom!

A deafening roar erupted, and tremendous force and heat washed over my entire body. Jeok Cheongang burst into loud laughter as he looked at me standing there, blackened from head to toe.

“What kind of idiot tries to knock that away?”

“……Hah. I almost had it.”

“Don’t make me laugh. If this old man had used all his strength, you would have died just now.”

I answered bluntly.

“I hit it because I thought I could.”

“And that’s why you look like that?”

“……I didn’t know it would turn out like this.”

“I’ll praise you for not collapsing in such an unsightly fashion. And for managing to block it in the end.”

“But weren’t you only supposed to defend?”

“Who told you that?”

Damn. Come to think of it, he hadn’t.

I tore off my half-charred shirt and threw it aside.

“Well, for someone who calls himself the Fire King, aren’t you using a little too much force against a kid young enough to be your grandson?”

“You’re a kid still wet behind the ears, yet you swing a spear at an old man old enough to be your great-grandfather? And you still call yourself the Sleeping Dragon of Shanxi?”

“You’re a Supreme Peak master, Old Master!”

“You possess the Heavenly Martial Physique.”

“Do you seriously call that *mal*?”

“If it isn’t *mal*—words—then is it a foal?”[^2]

[^2]: *Mal* means “words,” but can also mean “horse,” setting up Jeok’s reply about a foal.

“……”

“What? Why are you looking at me like that?”

Grind.

I tightened my grip on the spear and let out a hot breath.

“Hoo. Now I’m doing this properly.”

Jeok Cheongang scratched inside his ear with his pinky.

“Hm? What did you say? I can’t hear a weakling who got turned into charcoal with one hit.”

“……”

God, I hated this.

When he had been shredding the Roaring Fury Swordsman, his banter had been the most satisfying thing in the world. But now that I was on the receiving end, it was enough to make my stomach turn.

“What are you going to do if I actually make you retreat even one step?”

“It would be faster for the Heavenly Demon to become the Abbot of Shaolin.”

“Grrk.”

“There should only be enough time left for you to drink a glass of cold water. Do you think you can make this old man retreat before then? Not a chance.”

Jeok Cheongang was telling the truth. Only about three minutes remained.

Looking back at the way our fight had gone so far, the Quest’s failure was practically a foregone conclusion.

But I still had one trump card I hadn’t shown him.

I continued the conversation naturally.

“You’ll really regret saying that.”

“What do I have to regret? I was only trying to see how skilled you are in the first place. You do show some promise, though, so if you continue to work hard…”

“That’s a shame.”

“Hm?”

I let out a deliberate sigh at Jeok Cheongang, who looked puzzled. I made myself look like someone who was genuinely at a loss over how unfortunate it was.

“If you didn’t attack at all and only defended, I could succeed easily… But I suppose those weren’t the conditions.”

“If this old man only defends, you can make me retreat?”

A spark flashed in Jeok Cheongang’s eyes. Fighting spirit—or curiosity.

I couldn’t tell exactly what emotion lay in his gaze, but he had certainly taken the bait halfway.

I waved a hand as though I hadn’t noticed.

“No. Forget you heard that. If I succeeded, wouldn’t it damage your reputation?”

That was the clincher.

“……Look at this brat.”

Jeok Cheongang’s cheek twitched as he made a strange face. Finally, he nodded.

“I can see straight through your little scheme, but fine. Go ahead and try.”

“You mean it?”

“Haven’t you heard that the Fire King’s word is worth a thousand pieces of gold? Once this old man says something, he always keeps his word.”

“……Ah. Yes.”

He even changed the first word and plagiarized the proverb.

Regardless, I had achieved what I wanted. I discarded the half-charred spear and took out my third one.

*It’ll probably become disposable.*

But considering it the price of completing a Peak-Grade Quest, it was an absurd bargain.

Jeok Cheongang narrowed his eyes as I adjusted my stance.

“You’re not planning to use poison or some hidden trick, are you?”

“Come on. Of course not.”

I smiled brightly and added:

“A real man settles things with one big shot.”

Gooooong.

The spear shaft, which had swallowed forty-five years of internal energy, trembled.

* * *

Kraaaaaash!

A massive boulder went flying, and a tree as thick as a man was uprooted.

At the center of the clearing, which had been swept by a storm, Jeok Cheongang stood tall.

He had been driven back exactly five steps.

“You—you…”

Jeok Cheongang stared back and forth between me and the devastated surroundings, looking half out of his mind.

The beautiful wilderness that had surrounded us only moments ago had become a grotesque landscape of broken and uprooted trees and scattered boulders.

All of this was the result of a single thrust—One Annihilation.

“W-What in the world did you do?”

“Well, I’m not sure. I didn’t expect it to be this powerful either.”

It was my first time using One Annihilation after reaching the Peak realm.

I had expected its destructive power to be greater, since my internal energy had increased by leaps and bounds, but I hadn’t imagined this.

Jeok Cheongang shouted at my uncertain answer.

“You think that makes any sense?”

“That’s what I’m saying. Wow, this is seriously—”

The world spun before my eyes, and my legs buckled.

It was the result of pouring out every bit of my strength and internal energy without leaving behind even a grain.

A wrinkled hand caught my staggering body. The gaze of the man looking down at me was impossibly complex.

“I’ll hear what happened later. Rest for now.”

At his words, powerful energy flowed into me through my back. It had to be internal energy Jeok Cheongang was channeling into me.

I had expected it to be scorching, like swallowing the sun, but his internal energy was warm and vast.

The comforting warmth brought on an irresistible wave of drowsiness.

“Old Master…”

“Don’t resist. Let your body relax.”

“……I won, right?”

“Hm?”

“I really won, right?”

“……!”

Jeok Cheongang’s eyelids trembled. At last, he answered in a hoarse voice.

“Yes. This old man lost.”

“Heh heh heh.”

A laugh escaped me before I could stop it.

Even though the fight had been subject to countless restrictions, I was filled with joy at having made Jeok Cheongang—a master counted among the greatest under heaven—retreat.

Ding.

> **System**
>
> Quest **One Step Back** was completed successfully!
>
> Quest reward…

The fading sound of the System notification was the last thing I heard before I fell into a deep sleep.

* * *

*That boy. He sure sleeps well.*

Jeok Cheongang stared silently at the dead-asleep Jin Taekyung for a long while.

His cleanly sculpted features made him look like an innocent boy, yet they also gave the impression of a young man who had already experienced the world once.

*What a strange boy. What a strange boy.*

The longer Jeok Cheongang watched him, the more that thought took root.

He had thought he had already peeled away one layer of the boy’s shell, only to find even harder, more dazzling scales hidden beneath it.

*A sleeping dragon.*

This young man, who was sleeping peacefully enough to snore, was a dragon that had yet to obtain its dragon pearl.

That only made Jeok Cheongang more curious. How far would Jin Taekyung go? Would he live long enough to see the boy’s true limits?

*Especially that final strike…*

Jeok Cheongang looked around once more and let out a hollow laugh.

Could this really be a scene created by a young prodigy who had only just passed twenty?

He was certain that even the Sword Saint of years past had not been capable of this much.

*The Martial God. Perhaps he could have done it.*

A martial artist born human and called a god. The one person who had inspired awe in the Fire King, Jeok Cheongang.

What had his youth been like—the man revered not merely as the greatest under heaven, but as the greatest of all time?

As Jeok Cheongang imagined Jin Taekyung as he was now alongside the Martial God in his youth, he suddenly let out a quiet laugh.

*For this old man to think such a thing… That must mean this boy’s talent is comparable to the Martial God’s.*

Jeok Cheongang gazed at Jin Taekyung with profound eyes, then rose to his feet.

By now, a desire had begun to sprout within his heart—a desire to place a dragon pearl in the hands of that young sleeping dragon.

*Fly freely above those clouds. Become a Heavenly Dragon capable of covering the world with rain and wind.*

Grrrrrk.

At the snore that came instead of an answer, Jeok Cheongang burst into hearty laughter.

[^1]: A *jiazi* is a traditional cycle of sixty years.
## Chapter artifact 203

# Chapter 203

I read through the System message floating before my eyes.

It concerned the Quest reward I hadn't had a chance to check because I'd fallen asleep like I'd been knocked unconscious.

> **System**
>
> - Quest **One Step Back** was completed successfully!
>
> - You have acquired a large amount of EXP!
>
> - Level Up!
>
> - Level Up!
>
> - You have acquired 20 Bonus Points!

*That’s pretty damn generous.*

I had leveled up twice and even received bonus points. In other words, completing a single Quest had roughly the effect of gaining four levels.

Maybe the reward was larger than expected because of who my opponent had been.

*Close window.*

Shhk.

The translucent holographic window disappeared, revealing Jeok Cheongang approaching me.

In his hand was the satchel he had prepared in advance.

“Are you awake?”

“Ah, yes. I just woke up.”

“How’s your body?”

“I feel refreshed.”

Jeok Cheongang looked me up and down, then nodded.

“I suppose being young means you recover your strength quickly. We can move on to the next step right away.”

“Ah, the next step. Sounds good.”

“I knew you’d say that. This old man prepared something that suits you perfectly. Let’s see…”

“Old Master.”

“Hm?”

“I mean, that’s all well and good, but…”

I gave Jeok Cheongang an awkward smile and continued.

“Could you release the acupoint sealing before we start?”

I meant it literally.

I didn't know what had happened, but from the moment I first opened my eyes, my entire body had been stiff and rigid.

Jeok Cheongang had pressed my Paralysis Acupoint while I was asleep.

In my current condition, the only thing I could do was speak out loud.

“I’m sure you meant well, but I need to start the next training soon… Heh heh.”

“Ah, yes. Training.”

Jeok Cheongang rummaged through his satchel and added:

“This is the next training.”

“Being subjected to acupoint sealing is training?”

Or was releasing it the training?

Just as I was growing confused, Jeok Cheongang pulled something out of the satchel.

“Here it is. I forgot I’d shoved it all the way to the bottom.”

“…Isn’t that a rope?”

“That’s right.”

With the sturdy rope draped over his shoulder, Jeok Cheongang strode toward me and lifted me up.

“W-Wait. What are you doing?”

“You’ll find out soon enough.”

He carried me toward a massive boulder.

It had been embedded deep in the ground for who knew how long, and it was so large that several grown men couldn’t have wrapped their arms around it.

“Hmm. This should do.”

Jeok Cheongang muttered under his breath, then brought the edge of his hand down on the boulder.

Shhk. Shhk.

The red qi gathered around his hand sliced and split the massive boulder as easily as a cheesecake. After only a few cuts, the boulder had been transformed into a five-star stone bed.

“This is just right.”

“W-Wait a second. You’re not planning to tie me up here, are you?”

“Tie you up? I’m going to secure you.”

“…”

How was that any different from calling shit “feces”?

At any rate, I was beginning to tremble.

Actually, the Paralysis Acupoint alone had been suspicious enough. So had the satchel Jeok Cheongang had been rummaging through for a while.

*He’s not really going to pull out a whip and a mask, is he?*

While my pupils shook like an earthquake, Jeok Cheongang began securing my body to the boulder with the rope.

He wrapped it around various parts of my body and tied it tightly, then smiled in satisfaction.

“This should keep you from falling under ordinary circumstances.”

“Phew.”

“What was that sigh of relief?”

“I’m relieved it isn’t a tortoise-shell knot.”

“A tortoise-shell knot? What is that?”

“…A type of restraint technique.”

“A restraint technique? One used by the military?”

“…”

*Mostly Japanese guys use it.*

*Well, whatever.*

At present, I was tied up with my arms and legs spread wide.

Both wrists and ankles, my chest, stomach, and legs. It really did seem that the goal wasn’t restraint, but securing me in place.

*Then again, he’s already pressed my Paralysis Acupoint. There’s no need to tie me up that tightly.*

But what the hell was he planning to do?

Just as I was rolling my eyes around, Jeok Cheongang finally opened the satchel he had been carrying. And at the same time—

Whooosh!

“Gasp.”

An indescribable fragrance burst out.

A refreshing coolness spread through my entire body through my nose, so strong it felt like it could cure even someone with chronic rhinitis in a single treatment.

I opened my eyes wide and stared at the objects inside the satchel.

“What is this…?”

Three roots of grass lay neatly arranged inside.

Jeok Cheongang picked up the reddish roots and placed them on his palm.

“Elixirs.”

“Whoa. Where did you get something this valuable?”

“I searched the storehouse. It was packed to the brim with useless things, which made it a damn nuisance.”

Silk and gold and silver treasures piled up like mountains were nothing more than utterly useless objects in his eyes.

But Jeok Cheongang was a martial artist to his very bones. Elixirs or martial arts manuals that could improve his martial arts were another matter entirely.

“Well, these elixirs aren’t particularly effective, to be honest. If we’re talking about increasing internal energy, a hundred-year-old He Shou Wu or snow ginseng would be much better.”

“Then why…”

“You’re wondering why I went out of my way to bring these?”

“Yes.”

“Because these are the only things that can provide pure Scorching Yang Qi. You may increase the amount of your internal energy by eating anything just because it’s good, but your power will decrease.”

“Oh.”

I thought I understood what Jeok Cheongang meant.

To put it simply, it was a matter of fuel. No matter how much firewood you piled on, oil was what made a fire explode.

What he held in his hand wasn’t firewood. It was oil that would further strengthen the Scorching Yang Qi already present in my body.

*Still, this is touching.*

I had never expected Jeok Cheongang to go this far for me.

For a man as eccentric as him to endure the nuisance, personally select elixirs containing Scorching Yang Qi, and bring them to me meant he genuinely intended to have me learn the Fire Gate Clan’s martial arts.

*And I’m not even officially his Disciple yet.*

A man warm in both heart and internal energy.

That was the Fire King, Jeok Cheongang.

When he met my heated gaze, he flinched and took a step back.

“W-What’s with that look?”

“Nothing. You just seem like a really good person, Old Master.”

“…”

“You brought those for me to eat, didn’t you?”

Jeok Cheongang hesitated before answering.

“…I only brought them because they caught my eye.”

“I see.”

“The better ones, this old man kept for himself.”

“Yes. Heh heh.”

“Don’t laugh!”

Jeok Cheongang shouted and hurriedly changed the subject.

“Anyway, from now on, this old man will use these elixirs to open your acupoints.”

I had been considering teasing him a little more, but the words that came out of his mouth were anything but ordinary. My ears perked up before I even realized it.

“You’re going to open my acupoints?”

“You heard me. When this old man examined your body before, your muscles and bones were outstanding, just as one would expect from the Heavenly Martial Physique, but you had quite a lot of turbid qi.”

“Oh.”

“I heard you lived immersed in wine and women until recently. Even a fine sword grows dull if it’s left unattended for too long. No matter how extraordinary your constitution is, there’s no helping that.”

It was an undeniable fact.

The Jin Family’s Cultivation Technique was extremely stable, but its power and efficiency when circulating internal energy were lacking.

Although I circulated my qi whenever I had the chance, the traces of twenty years spent slacking off were still there.

“Then…”

“This old man will burn away all the turbid qi in your body with the elixirs and my internal energy. For you, it will be far more effective than cleansing the sinews and washing the marrow.”

“That’s welcome news.”

“I wouldn’t be so sure.”

“What?”

“You’ll find out soon enough.”

Before I had a chance to say anything else, his hand sealed my Mute Acupoint. My tongue stiffened, and a silent scream circled around inside my mouth.

*What the hell is this?*

I was now nothing more than a corpse with its eyes open.

Jeok Cheongang grinned as he looked down at me, frozen like a plaster statue.

“Let’s start by eating the elixirs.”

His wrinkled fingers pried open my jaw and slipped the three roots into my mouth.

The earthy smell that hadn’t been shaken off and the cool freshness filling my mouth lasted only a moment. The hard solids melted as soon as they touched my tongue and flowed down my esophagus into my stomach.

And then—

Ding.

> **System**
>
> - You have consumed **Fire Spirit Grass**!
>
> - You have consumed **Red Flower Grass**!
>
> - You have consumed **Flame Red Grass**!
>
> - Quest **Acupoint Opening** has been created!
>
> - You cannot refuse this Quest. Forced progression will begin!

*Gah!*

Along with the System notifications ringing one after another, tremendous heat swept through my body.

Only then did I understand what Jeok Cheongang had meant.

*It fucking hurts!*

Because my acupoints had been sealed, I couldn’t scream or thrash around. All I could do was open my eyes wide.

Just as I hurriedly tried to draw up my internal energy, Jeok Cheongang rolled up his worn sleeves.

“All right. Shall we begin in earnest?”

“…”

“Bear with it even if it hurts. Pain is temporary, but martial arts last forever.”

Tap. Tap-tap-tap-tap!

His blurred fingers began poking and tapping all over my body.

The impact scattered my internal energy, while the unfamiliar energy of the elixirs coursed through me. I let out a silent scream in the boiling heat.

*AAAAAAAAARGH!*

* * *

Unlike Jin Taekyung’s eyes, bloodshot from unbearable pain, Jeok Cheongang’s gleamed with heat.

*It’s going smoothly. No, it’s explosive.*

Was it because of the Heavenly Martial Physique?

The speed at which the internal energy spread was astonishing. The energy of more than thirty years contained within the elixirs ran wild through every minor meridian in his body.

Jin Taekyung tried to summon his internal energy and suppress the force, but that was not what Jeok Cheongang wanted.

*He can tame it later. For now, I have to let it run wild.*

A tamed fighting bull sometimes forgot how to charge.

The newly infused energy of thirty years had to break through everything in its path without restriction.

It was a dangerous attempt—dangerous enough to cause qi deviation if anything went wrong. Even Jeok Cheongang, a Supreme Peak master, swallowed dryly as he continued moving his fingers.

*Gyeonjeong, Amun, Bongan, Ip-dong…*

Tap. Tap-tap!

Following his guidance, hundreds of acupoints opened and closed over and over. Before long, black sweat poured from Jin Taekyung’s entire body, accompanied by a musty odor.

The stench was so foul that even someone with an iron stomach would have gagged, but the corners of Jeok Cheongang’s mouth twitched with delight.

*It worked!*

This phenomenon was proof that a massive amount of turbid qi was being expelled.

As though to confirm his guess, the sweat gradually grew lighter in color, and the foul odor slowly began to fade.

Before long, the sweat became clear, and a pleasant body scent wafted through the air. Astonishment filled Jeok Cheongang’s eyes.

*Already?*

It was fast. Far too fast.

The process he had expected to last at least three shichen[^1] was nearing its end in less than one.

Even more astonishing was that the elixirs’ energy had barely diminished.

Normally, a considerable amount of energy was lost while removing turbid qi and circulating what remained. Jin Taekyung was different.

*As expected of the Heavenly Martial Physique… It truly lives up to its name.*

At this rate, he could remove all the turbid qi and still gain the full thirty years of internal energy.

But instead of satisfaction, greed and conflict appeared in Jeok Cheongang’s eyes.

*What if we go further?*

The Conception Vessel and the Governor Vessel. He could cross the mountain known collectively as the Conception and Governor Vessels.

It was a realm most martial artists of the Murim could not reach even after devoting their entire lives to training.

It required an enormous amount of internal energy and enlightenment, but perhaps it was possible now.

*The Heavenly Martial Physique. And my help.*

Even so, opening the Conception and Governor Vessels right away was dangerous.

Leaving everything else aside, Jeok Cheongang was worried about whether Jin Taekyung could endure the pain.

*What should I do?*

After agonizing over it again and again, Jeok Cheongang finally spoke.

“I think you can open the Conception and Governor Vessels.”

“…”

Jin Taekyung’s bloodshot eyes trembled as he endured the pain. Jeok Cheongang continued speaking to him when he gave no answer.

“But you’ll have to accept an equal amount of risk. You’ll probably experience pain beyond anything you’ve felt so far. One mistake could result in your death.”

“…”

“You choose. If you trust this old man enough to leave it to me, blink twice.”

The next moment, Jin Taekyung blinked without hesitation.

Twice, with not the slightest trace of doubt.

Feeling the solid trust in his eyes, Jeok Cheongang felt a warmth spread through one corner of his chest.

*Had this brat really trusted me this much?*

Suppressing the swell of emotion, he forced up the corners of his mouth.

“All right. Let’s give it a try.”

At the same time, the immense internal energy flowing from his fingertips poured into Jin Taekyung’s body.

* * *

Ding.

> **System**
>
> - Information about Quest **Acupoint Opening** has changed!
>
> - Quest **Conception and Governor Vessels** has been created! Due to the updated information, the difficulty and rewards have been adjusted!

Listening to the System notification, I thought:

*No, fuck…*

I was sure I’d only blinked once.

[^1]: A *shichen* is a traditional Chinese time unit of approximately two hours.
## Chapter artifact 204

# Chapter 204

Whooosh!

A tremendous amount of internal energy began charging down the path.

To open the Conception Vessel, one had to pass through a path made up of twenty-four acupoints. Its starting point was the Huiyin Acupoint.

The problem was that the Huiyin Acupoint was located in a rather important area.

*No, no!*

*A forced opening?!*

No scream escaped my lips. The internal energy, transformed into a raging bull, slammed into the Huiyin Acupoint.

Boom!

*……!*

It was a sensation only someone who had experienced it could understand. My vision turned white as though I had arrived in heaven, and all my senses drifted away.

The faces of the people precious to me flashed before my eyes one after another.

Mom. Hayeon. Among them was the unfamiliar face of a newborn baby.

*Y-You’re…*

Waaaaah!

A baby’s cry echoed like a hallucination.

Only then did I realize who it was.

*Oh, my baby!*

Jin Taekyung Junior, whom I had yet to meet.

The face of a child I might never meet at all.

The baby’s innocent eyes seemed to ask me:

“Daddy, can’t I come out?”

The next moment, my whitened vision returned, and unimaginable pain shot up from my lower body.

*Kyaaaaaaah!*

As I screamed with my soul, a desperate voice lashed against my ears.

“Get a hold of yourself! If you can’t endure this pain, death is all that awaits you!”

“……!”

*Death? Me? And in such a disgraceful way?*

My mind snapped back as if someone had dumped cold water over my head.

The pain, like a knife stabbing into my lower abdomen, was still there, but I summoned superhuman patience.

*I can’t die like this!*

I was someone who had survived countless bloody battles. Even when my injuries had been severe enough to put my life at risk, I had stubbornly endured.

This was only this much—no, it wasn’t *only* this much, but still, I wasn’t so impatient that I’d let my life end over something like this.

*Hng!*

While I stubbornly endured the pain, the tremendous internal energy broke through the twenty-four acupoints without hesitation.

And finally…

Boom!

It collided with the gate known as the Conception Vessel.

At the same time, pain on a level similar to what I had felt at the Huiyin Acupoint came surging in like a wave.

The difference was that this collision did not end after just one strike.

Boom! Boom! Boom!

Once, twice, three times. Thunderous booms and vibrations rang out inside my body like thunder from the heavens.

Only then did I understand why Jeok Cheongang had pressed my Paralysis Acupoint and Mute Acupoint. And why he had secured me with ropes on top of that.

*Gnnngh!*

Even though my acupoints had been sealed, my entire body trembled. My body was reacting on its own to pain beyond its limits.

Pop.

The tiny blood vessels in my wide-open eyes burst.

Through my vision stained entirely red, I saw Jeok Cheongang roaring.

“Endure it! This is the last one!”

*The last one? Really?*

Whether it was true or not didn’t matter. His words gave me strength.

*Just a little more. More!*

I drew up the internal energy sleeping in my dantian.

Forty-five years of internal energy raced through the wide-open acupoint pathways, where all the turbid qi and obstacles had been removed, and surged upward in one burst.

Then it joined the elixir’s energy, which was already pounding against the Conception Vessel, and Jeok Cheongang’s internal energy.

The battering ram formed from the three energies struck the gate with more force and sharpness than ever.

Bang! Kwoooong!

That was the finale—the end of the long, arduous struggle.

The tightly blocked Conception Vessel collapsed, and the energies poured in like an occupying army.

For an instant, pain sharp enough to make me dizzy swept through me. Then a pleasure and refreshing clarity several times greater than the pain I had felt flooded my entire body.

Ding.

> **System**
>
> - You have successfully opened the **Conception Vessel**!
>
> - The handling of qi has become much freer!
>
> - Your speed of circulating and accumulating internal energy has increased dramatically!
>
> - You have achieved the **Conception Vessel Opening** Achievement!
>
> - As a reward…

*Ah… Ahhh!*

My body trembled now not from pain, but from joy. This was different. Everything I had known until now had been no more than a drop in the ocean.

The difference was as enormous as the gap between First Rate and Peak.

*How can things change this much?*

Although I had to endure tremendous pain, an achievement like this was worth it. No—it was something I had to endure.

Jeok Cheongang beamed at me as I stared in amazement.

“You did very well!”

Seeing how genuinely pleased he was made a corner of my chest grow warm.

To think he had gone all out to help me like this. If my acupoints hadn’t been sealed, I would have performed a formal bow to Jeok Cheongang.

*Jeok Cheongang, you really…*

Just as my eyes began to grow moist, he spoke.

“We can open the Governor Vessel this way, too.”

“…….”

*Oh, fuck.*

*I forgot about that.*

*He wants me to do this one more time?*

*No. I’m not doing it! At least let me rest for a little while first!*

Seeing me blink desperately, Jeok Cheongang chuckled.

“You’re so eager to do it right away. I was going to let you rest a little first, but… Very well. Let’s ride this momentum and open both the Conception and Governor Vessels!”

“……!”

“Here we go!”

And so, the express train to hell departed once more. One shichen later,[^1] I could faintly hear a System notification through my dazed consciousness.

Ding.

> **System**
>
> - You have opened the **Governor Vessel**!
>
> - Quest **Conception and Governor Vessels** was completed successfully!
>
> - You have achieved a rare Achievement! As a reward…

.

.

.

*Whatever, fuck.*

To hell with rare Achievements and whatever else. I couldn’t endure any more.

Having exhausted every last bit of my mental strength, I plunged headfirst into endless darkness.



* * *



The moment Jeok Cheongang loosened the ropes, Jin Taekyung’s collapsing body fell into his careful embrace.

The sweat Taekyung had shed while enduring the pain and the turbid qi he had expelled earlier created a powerful stench, but Jeok Cheongang didn’t care.

Those were the traces left by a martial artist striving to reach a higher realm.

The gaze Jeok Cheongang directed at the unconscious Jin Taekyung was deeper and gentler than ever.

*The more I learn about him, the more remarkable he is.*

At first, Jeok Cheongang had wondered about it.

*Why him, of all people?*

In Jeok Cheongang’s eyes, Jin Taekyung was neither white nor black. He was gray—the sort of gray one could find anywhere in the world.

He wasn’t exactly burning with a sense of justice, but neither was he evil.

*Nor was he particularly devoted to training in martial arts.*

From the moment Jeok Cheongang arrived at the Jin Family of Taiyuan, he had heard so much about Jin Taekyung that the words had been driven into his ears.

Even without asking, the people around him were always talking.

His martial arts were Third Rate, while his drinking, womanizing, and gambling were First Rate. Unlike his two older brothers, who possessed outstanding talent, he had been called a disgrace to the family.

When Jeok Cheongang learned the truth, he had resented the heavens, if only for a moment.

*Why did you give the Heavenly Martial Physique to someone like him?*

A fine sword ought to belong to a swordsman, not a farmer.

Yet the Jin Taekyung of the rumors was no different from a farmer holding a fine sword. He didn’t even possess the farmer’s diligence.

The only thing he applied himself to diligently was drinking, womanizing, and gambling. What more was there to say?

But…

*I was wrong.*

Looking back, Jeok Cheongang realized that everything he had thought was merely an old man’s stubborn prejudice and contradiction.

He wasn’t some immortal sage, so how could he divide someone he had known for such a short time into black and white? And what if Taekyung was gray?

*A human heart. If he holds on to that, it’s enough.*

From everything Jeok Cheongang had seen so far, Jin Taekyung was more than good enough.

Humans were imperfect beings to begin with, so it was absurd to divide them into perfect white and black.

Perhaps gray was simply another name for a good person.

*And on top of that, he possesses remarkable mental strength.*

What good was being born with a fine physique? The process of opening the Conception and Governor Vessels was so difficult and painful that it could be called hellish.

Yet Jin Taekyung had done it. And he had done it splendidly.

It must have been unbearably difficult and painful. Even so, he had held on with nothing but the single-minded determination to become stronger.

Jin Taekyung possessed a mental strength as firm as his physique.

*The Heavenly Martial Physique chose its master well.*

A satisfied smile appeared around Jeok Cheongang’s mouth. After gazing at Jin Taekyung for a long while, he muttered:

“Perhaps… it can happen much sooner than I thought.”

As soon as he finished speaking, Jeok Cheongang’s wrinkled fingers began to tremble.

This had cost even him a considerable amount of internal energy and mental strength. Before his mind could fully process it, his aging body was already informing him of the fact.

“It’s too soon, you bastard. Hold out for just a few more years.”

Jeok Cheongang muttered bitterly and lifted Jin Taekyung’s body.

They had crossed a great mountain. Now it was time to rest.

The young man and the old man alike.



* * *



It was around noon when Ak Bulgun, the spear Instructor at Heaven’s Gate Temple, arrived at Jin Wikyung’s office.

When he opened the door and entered, Jin Wikyung, who had been scribbling something across a bamboo slip, brightened and rose from his seat.

“Sir Ak, welcome. Thank you for accepting my invitation despite how busy you must be.”

“It’s only sensible for the man with more free time to make the trip. Please don’t worry about it.”

The Shandong Yue Family was a prestigious clan of spear techniques, famous throughout the Murim.

Yet despite being a direct scion of such a prestigious family, Ak Bulgun was a straightforward man with no inclination toward empty formalities.

The questions that followed immediately, before he even had time to take a sip of tea, reflected that personality perfectly.

“By the way, why did you summon me? Could it be…”

Jin Wikyung smiled faintly.

“Unfortunately, this isn’t about Mukyung.”

“I see.”

Ak Bulgun nodded and added bluntly:

“Lesser Family Head, please understand that Heaven’s Gate Temple has strict regulations.”

Heaven’s Gate Temple was both a treasure trove of outstanding talent and a gateway to advancement.

As long as they possessed sufficient talent, people could become cadets regardless of their backgrounds. As a result, its members ranged from disciples of small sects in remote regions to disciples and scions of prestigious major sects.

Despite bringing together people from such different backgrounds, Heaven’s Gate Temple had avoided major disturbances because it imposed strict regulations on every cadet.

“If someone fails to return by the appointed date, they can be expelled. Even the Ten Dragons and Phoenixes aren’t exempt.”

“I did go to see him myself, as it happens, but…”

“Did he refuse?”

“Yes.”

Jin Wikyung had gone to see him after much deliberation, but Jin Mukyung hadn’t even shown his face.

According to Childeuk, the martial artist stationed at the training hall, Mukyung hadn’t come outside even once since entering.

He subsisted on fasting pills and refused to let anyone approach him. At least, when he heard that Jin Wikyung had come, he sent back a brief answer:

“I won’t return until I achieve complete mastery.”

Ak Bulgun let out a short laugh after hearing Jin Wikyung’s explanation.

Having taught Jin Mukyung several times before, Ak Bulgun was well acquainted with the young genius’s personality.

“That sounds like him.”

“It’s unfortunate, but I don’t think even I can break my little brother’s stubbornness.”

“The Temple Master will regret it just as much as you do, Lesser Family Head.”

Everyone had their own path to follow. Ak Bulgun nodded matter-of-factly and continued:

“It seems I still haven’t heard why you asked to see me.”

“Oh, I wanted to deliver a letter to you.”

“A letter?”

Instead of answering, Jin Wikyung took a small bamboo tube from inside his robe and handed it over.

Ak Bulgun checked the inscription engraved on the surface of the blue bamboo tube and muttered:

“Heaven’s Gate Temple?”

“It arrived half a shichen ago. I thought it best to bring you here so I could hand it over personally.”

“Please excuse me for a moment.”

After asking permission, Ak Bulgun silently read through the letter.

He checked it twice, then a third time, before raising his head and staring at Jin Wikyung.

“Lesser Family Head.”

“……?”

“I’m going to need your help.”

[^1]: A *shichen* is a traditional Chinese time unit of approximately two hours.

# Checkpoint Review — 530–534

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

# Chapters 530–534

## Plot

Henan remains crowded with Murim Alliance forces preparing for war. Jin Taekyung arrives at Gowolru with Hyuk Mujin and Gung Gibang, only for Hwangbo Ak to be thrown into the street by Taishan, a gigantic martial artist from the demonic, heterodox side. Taekyung stops the fight, protects the civilians, forces both sides to stand down, and charges the inn’s extensive repair costs to the Hwangbo Family.

Taekyung reunites with Ju Hwaran and intimidates Hak Woo into leaving. Hyuk returns with Sama Pyo, the Young Sect Leader of the Black Dragon Demon Gate and wielder of the Black Dragon Saber. Taishan is Sama Pyo’s enormous, food-obsessed subordinate, while Sama Pyo is revealed to have been Hwaran’s former fiancé. Their engagement was a political arrangement Hwaran accepted to support her ailing father, but why it ended remains unclear.

Sama Pyo and Taishan leave under public scrutiny. Sama Pyo recognizes Taekyung as an unusually powerful and principled martial artist, while Taishan considers him strong and kind but remains absolutely loyal to Sama Pyo. Hwaran departs to handle Escort Bureau business. Taekyung is troubled after learning why she accepted the engagement, then returns to the Jin Family lodgings and learns that Alliance Leader Mae Jonghak is looking for him.

## Continuity

- Mae Jonghak is the Alliance Leader of the restored Murim Alliance and is seeking Jin Taekyung; his reason remains unknown.
- Gowolru is the damaged inn where Taekyung reunited with Ju Hwaran and encountered Sama Pyo and Taishan.
- Ju Hwaran and Sama Pyo were formerly engaged in a political marriage arranged for her father’s sake; the cause of their separation is unresolved.
- Sama Pyo is the Black Dragon Demon Gate’s Young Sect Leader and Black Dragon Saber. Song Ilseom considers him stronger and more dangerous than before.
- Taishan is Sama Pyo’s giant subordinate. A childhood head injury left him childlike, wary of strangers, food-obsessed, and absolutely loyal to Sama Pyo, though he regards Taekyung as strong and kind.
- Hak Woo is the Kunlun Sect’s top young prodigy, the Kunlun Cloud Dragon; Taekyung can force him to withdraw through Sound Transmission.
- Song Ilseom remains Hwaran’s direct escort.
- Taekyung’s growing reputation as the Blazing Flame Divine Dragon lets him intimidate major young masters and charge Gowolru’s repairs to the Hwangbo Family.
- The Lord of Heaven, Dark Heaven’s Gate-opening method, the Southern Heaven Demon Empress’s plans in Yunnan, and Jeok Cheongang’s duel with Nangong Cheon remain unresolved.

## Translation Decisions

- Retain **Murim Alliance**, **Alliance Leader**, **Black Dragon Demon Gate**, **Black Dragon Saber**, **Kunlun Cloud Dragon**, **Blazing Flame Divine Dragon**, **Sound Transmission**, and **Gowolru**.
- Render **일기천룡** as **One-Ride Heavenly Dragon** and **태산** as **Taishan**.
- Render **전 정혼자** contextually as **former fiancé** or **former fiancée**, preserving the political-engagement context.
- Preserve Taishan’s clipped, childlike, literal speech; Taekyung’s blunt profanity and intimidation; and the chapters’ embarrassment, financial-therapy, and food-related humor.

## Durable state

{
  "active_continuity": [
    "The Mount Song Resolution formally restored the Murim Alliance; Mae Jonghak is its Alliance Leader, and Song Ho commands the Hidden Shadow Pavilion under his authority.",
    "Jin Taekyung and Cheongpung's prominent role in raising the Murim Alliance flag made them objects of intense attention among Murim factions.",
    "Taekyung believes the Zhongnan Sect resents him, the Jin Family of Taiyuan, and Jeok Cheongang after its repeated humiliations and will obstruct them.",
    "Cheongpung created Mimi Step from Mimi's movements; it is a snake-like footwork technique fast enough that Taekyung could barely track it with his naked eyes, and Cheongpung has recently lost his appetite while refining it.",
    "Mungyeong ended Taekyung's direct training and assigned him a final task of incorporating martial principles into his learned martial arts.",
    "Zhuge Feng's Demon-Sealing Formation still blocks all mana from the exposed Gate, while Jang Taebo is summoning artisans to process the Water God Dragon's remains.",
    "The Southern Heaven Demon Empress is traveling toward Yunnan and expects to cause further deaths.",
    "Unnamed, Hong Dao's practical Disciple, is a scarred Supreme Peak master and Jung Ho's young Martial Uncle after enduring Repentance Cave and receiving Shaolin's Great Restoration Pill.",
    "The Black Dragon Demon Gate remains a major unorthodox power descended from the Demonic Cult's Twelve Branches; Sama Pyo is its Young Sect Leader and Black Dragon Saber, and Taishan is his giant subordinate.",
    "Jin Taekyung remains a Supreme Peak master with Three Flowers Gather at the Crown, advanced qi perception, exceptional resistance to monster Fear, and public S-rank-level recognition despite retaining an A-rank license.",
    "Ju Hwaran is with Taekyung at Gowolru, Song Ilseom remains her direct escort, and her former political engagement to Sama Pyo was accepted for her father's sake.",
    "Sama Pyo and Taishan have left Gowolru under scrutiny; Taishan is absolutely loyal to Sama Pyo but regards Taekyung as strong and kind, and the Alliance Leader is seeking Taekyung."
  ],
  "continuity_sources": [
    534,
    533
  ],
  "open_questions": [
    "What is the Lord of Heaven's identity, how is he connected to the dangerous force Taekyung associates with his original world, and how can Dark Heaven open Gates?",
    "Where is the Southern Heaven Demon Empress ultimately headed, and what does she intend to do in Yunnan?",
    "What is the outcome of the duel between Jeok Cheongang and Nangong Cheon, the Azure Sky Sword King?",
    "Why did Ju Hwaran and Sama Pyo's political engagement end?",
    "Why is the Alliance Leader seeking Jin Taekyung?"
  ],
  "safe_through": 534,
  "temporary_decisions": [
    "Render 고월루 as Gowolru, 곤륜운룡 as Kunlun Cloud Dragon, and 학우 as Hak Woo; render 전 정혼자 contextually as former fiancé or former fiancée.",
    "Render 탈진 as the capitalized system status Exhaustion; retain Ten Dragons and Phoenixes, Blazing Flame Divine Dragon, Dark Heaven, Murim Alliance, and Old Master.",
    "Render 황보세가 as Hwangbo Family, 소가주 as Lesser Family Head, 은비화 as Dagger Hidden Flower, and 전음 as Sound Transmission.",
    "Preserve the chapter's blunt profanity, financial-therapy humor, and monster-comparison humor.",
    "Render 일기천룡 as One-Ride Heavenly Dragon and Taishan's speech as clipped, childlike, and literal."
  ],
  "version": 1
}

## Reading copies

## Chapter artifact 530

# Chapter 530

Henan was a place that truly deserved to be called the Central Plains.

Civilization had begun along the Yellow River, and for thousands of years, the region had remained the center of the world. It had also been the capital of nine dynasties that had risen and fallen like wildfire over the ages.

That was why, even now, with the Murim Alliance officially restored and ominous signs of war beginning to spread, Henan Province had not lost its vitality.

No. If anything, things were moving in the exact opposite direction.

“Is it just me, or are there more people around? And the atmosphere seems pretty good, too.”

Hyuk Mujin was telling the truth. The broad main street was packed with people, and it was hard to find any particular sign of serious worry on their faces.

Every now and then, someone would cast an uneasy glance at a martial artist walking through the streets with weapons strapped to his body, but that was all.

I pulled my bamboo hat lower and muttered,

“Yeah, it does.”

“It’s strange. Until recently, the atmosphere was still pretty grim. Is this what they call the calm before the storm?”

“……You lunatic. Why don’t you go pray for something to happen while you’re at it?”

“Considering the situation, that isn’t entirely wrong.”

He had a point. But Hyuk Mujin was overlooking one important fact as well. I considered smacking him upside the head, then shook my head.

“I think those people have finally realized it.”

“Realized what?”

“That this place—Henan—is the safest place in the world.”

“……Ah.”

From the perspective of commoners, martial artists were like wild beasts that could not be controlled.

But most of the martial artists currently in Henan had gathered under the name of chivalry, the greater good, and the Murim Alliance.

And there weren’t merely dozens or hundreds of them. There were thousands.

From a commoner’s point of view, news that a war had broken out among martial artists must have been frightening. But things were rapidly settling down now.

*If this were the modern world, the atmosphere wouldn’t be this good.*

Imagine a war breaking out between the United States and Russia.

The moment the war began, the citizens of Moscow or Washington, DC, would either be running for their lives or staring up at the sky, trying to guess when an intercontinental ballistic missile or a nuclear weapon might come flying toward them.

*That doesn’t mean Henan is completely safe, though.*

What if Dark Heaven swept away half the world and made it all the way to Henan?

It wasn’t impossible. No matter how many martial artists had gathered beneath a single banner after the Murim Alliance was formed, there was no way to know the outcome of the war.

But an even greater problem was that there were other ways for them to reach us.

*The Moving Formation. No, should I call it a magic teleportation formation?*

It was an unbelievable and unsettling truth that had not yet become known to everyone.

Truths like that could awaken people’s vigilance, but they could also bring tremendous chaos and shock. That was probably why it had not yet been made public.

*When that happens, people won’t be smiling like this anymore.*

I smacked my lips bitterly and glanced around.

There were children staring at the passing martial artists with fascinated expressions. Merchants were excited by the unexpected boom in business. Martial artists moved along the main street with faces full of mingled tension and excitement.

At least none of them knew everything there was to know about Dark Heaven.

Those who knew the deeper secrets were already continuing an endless meeting alongside their new Alliance Leader.

“Captain?”

“What are you thinking about so hard? You’re making people look at us for no reason.”

“……It’s nothing. Let’s go.”

I must have spaced out for a moment. Coming back to myself, I started walking again.

Standing alone in the middle of a main street swarming with people was bound to attract attention.

Sure enough, a few sharp-eyed individuals were already looking our way.

*They’re not ordinary martial artists. They’re masters.*

That didn’t mean they were Dark Heaven’s spies. That would be an overinterpretation.

Every one of them was dressed confidently in martial uniforms with weapons strapped to their bodies, and all of them gave off pure, righteous qi.

“Captain.”

Hyuk Mujin’s low voice came from behind me and slipped into my ears. But I continued walking as though nothing had happened.

“It’s fine. Just keep going.”

“You knew?”

“Of course.”

“I’m still a little nervous.”

I understood Hyuk Mujin’s concern.

Since the Mount Song Resolution, I had become fairly famous.

The Sleeping Dragon of Shanxi and the Blazing Flame Divine Dragon were already epithets firmly imprinted throughout the Murim. But by raising the Murim Alliance’s flag before thousands of martial heroes, I had left an even more definite impression.

I wasn’t as famous as the heads of the Nine Sects and One Gang or the Five Great Families, but my name and face were now better known than those of most Elders from prestigious major factions.

“What’s there to be nervous about? Just pretend you didn’t see them and walk past.”

“No, I’m worried something really serious might happen.”

As Hyuk Mujin continued fretting, Gung Gibang clicked his tongue.

“What a tiny little heart you have. What serious thing is going to happen just because they recognize his face? It’ll only be annoying. This is exactly why he’s wearing that bamboo hat.”

After lightly scolding him, Gung Gibang looked at me and asked,

“What’s wrong with that guy?”

“Leave him alone. It’s kind of endearing. He noticed ahead of time and is worrying about me.”

“……Well. That’s true.”

I smiled inwardly, feeling touched.

Hyuk Mujin usually didn’t show it very well, but he was a tender spot for me.

He was the person I had spent the most time with since coming to Murim, and we had endured all kinds of hardships together, so naturally, I couldn’t help worrying about him……

“This is driving me crazy. What are you talking about?”

“Huh?”

“What?”

Hyuk Mujin continued in a pale voice as he looked at Gung Gibang and me, who had both turned toward him.

“I’ve been about to shit myself for ages, but you two keep saying the strangest things. Seriously.”

“……!”

“……!”

Endearing, my ass.

When he said something serious might happen, he’d meant a real emergency.

Gung Gibang and I were momentarily left speechless. Breaking out in a cold sweat, Hyuk Mujin hurried ahead.

“Where’s the place we’re meeting? Hurry! If this keeps up, it’s going to come out!”

What a terrifying spirit. The desperation on his face was something I had never seen even during battle.

Gung Gibang reflexively raised a finger and pointed at a building.

“It—it’s over there.”

“That one? The three-story inn?”

“Uh? Yeah.”

“Urgh. Then I’m going on ahead. Poooooop!”

Was that final cry an expression of his determination to hold it in?

Or was it a booster burning through his final sphincter and sending him flying?

Even as he staggered, Hyuk Mujin tore through the crowd at incredible speed. Gung Gibang muttered,

“Drunken Eight-Immortals Step……?”

“……Please don’t talk bullshit. He just needs to shit.”

God. Buddha. Why am I surrounded by nothing but idiots?

After lamenting from the depths of my heart, I looked toward the three-story inn Hyuk Mujin was heading for.

It wasn’t far away. Yet the part of my chest that had settled down during the journey suddenly began to churn.

“……A month? No, has it been two months?”

At my unconscious mutter, Gung Gibang narrowed his eyes.

“Oh-ho.”

“What, you bastard?”

“Is it what I think it is?”

“You’re an animal capable of thinking?”

“Am I right?”

“Do you want to be?”

“Come to think of it, the atmosphere back then was a little strange.”

“Want me to pick out a grave for you?”

“You keep dodging so cleverly that it must be true.”

“Do you want to get hit quickly enough that even clever dodging won’t help?”

“Pfft. That bastard Hyuk should’ve seen this.”

“……No. I mean, this is. Hah. Never mind.”

At this point, Gung Gibang would normally have changed the subject just to avoid getting hit. But today was different.

His laughter sounded like air leaking from a punctured sack as he kept glancing at me. My fist clenched, but strangely enough, I didn’t feel like hitting him.

“Pfft-pfft-pfft.”

“…….”

Bam!

Watching him laugh made the urge to hit him come surging back with tremendous force.

I grabbed Gung Gibang by the back of his neck and lifted him off the ground. He hadn’t even been able to scream; he was clutching his solar plexus.

“So. That’s the place, right? The three-story inn.”

“Ow. Y-Yeah, it is.”

“I’m going there to eat. I’m going because I’m hungry.”

“I-I know.”

“I heard that Kunlun Cloud Dragon guy or whatever is there, too. I’m going to see him because it’s been a while. And while I’m there, I’ll build a little rapport with that Hwangbo fellow or whatever his name is.”

“……I’ll remember that.”

“Behave yourself. Unless you want the Ten Dragons and Phoenixes to become the Nine Dragons and Phoenixes.”

That seemed to have driven the lesson home. Once I released him, Gung Gibang rubbed the spot where I had hit him and muttered,

“You vicious bastard.”

“What did you say?”

“N-Nothing.”

His answer wouldn’t fool a fly. Gung Gibang hurriedly changed the subject.

“Still, I’m looking forward to this. The moment they learn that you’ve come, they’ll all welcome you with both hands raised.”

“I don’t care. Whether they welcome me with both hands raised or not.”

I didn’t particularly care about Kunlun Cloud Dragon or that guy who was supposed to be the Lesser Family Head of the Hwangbo Family.

Still…… there was one person I sincerely hoped would be happy to see me.

But Gung Gibang misunderstood my answer and hurriedly continued,

“No! Hwangbo Ak can be a real pain in the ass, but even so, the moment he hears you came all this way, he’ll run out barefoot and—”

Gung Gibang couldn’t finish.

Boom!

A sudden thunderous roar swallowed his voice and all the noise of the bustling main street.

The silence that settled over the street lasted for less than a moment—so brief it could hardly even be called an instant—before it shattered.

“Aaah!”

“Eeeeeek!”

“Gowolru! Gowolru is……!”

Screams erupted as countless people scattered in every direction like a swarm of locusts.

But I stood firmly in place, staring ahead.

*Gowolru.*

I could see it clearly. Part of the three-story inn where today’s meeting was supposed to take place had been blown wide open.

Someone’s body came flying through the rain of building materials and clouds of dust.

Whoosh! Crash!

Not far away, a street stall was smashed to pieces, and the ground was gouged deeply.

A man managed to right himself and rise to his feet.

Thud, thud, thud.

*Who is that?*

His martial uniform was torn to shreds, and his leather shoes had been ripped off. His handsome face was filled with rage and dismay.

“How dare you… You bastard! I’ll tear you apart……!”

That was when it happened.

At the sight of the man spitting out a boiling voice through clenched teeth, Gung Gibang’s mouth fell open.

“Hw-Hwangbo Ak!”

“……?”

“You! What are you doing here?”

What? That guy was Hwangbo Ak?

The sudden call made the man—Hwangbo Ak—pause for a moment. I looked him up and down and muttered,

“He did come running out barefoot.”

Was this some kind of surprise event for me? Or perhaps an impromptu welcome party from the Ten Dragons and Phoenixes?

But judging from the way Hwangbo Ak’s face twisted at my words, it didn’t seem that way.

“What did you just say?”

“Oh. Sorry. That wasn’t what I meant.”

“You damned bastard……”

“You look busy, so let’s talk later. Ah, it’s coming.”

“What?”

My question was answered in an instant.

Hwangbo Ak seemed to have momentarily forgotten something. Then urgency and horror rose across his face.

Whoosh—BOOM!

Something enormous shot through the air and slammed directly into Hwangbo Ak.

Its tremendous power and speed were obvious from the sound of it cutting through the air alone. Even fully alert, he would have been hard-pressed to handle it. After letting himself get distracted, the outcome was obvious.

“Guhk!”

Hwangbo Ak’s body flew backward, spraying blood. At the same time, a massive shadow pursued him.

What should I do?

The deliberation was brief.

*There’s never a quiet day around here.*

Swish.

With a quiet sigh, I stepped forward.

A gigantic man stood before me, blocking out the sun and casting a vast shadow. He looked down at me with eyes as round as bowls.

“You. Move.”

I answered calmly.

“No. I don’t want to.”
## Chapter artifact 531

# Chapter 531

“You. Move.”

“No. I don’t want to.”

“……Huh?”

He clearly hadn’t expected that response.

The giant’s eyes, each as large as a child’s fist, rolled around as he stammered.

“Y-You don’t want to?”

“Yeah. I don’t want to. I’m not moving.”

“That’s s-strange. Everyone moved until now.”

What kind of character was this?

*Did he forget to put any points into intelligence, too?*

For someone with a build so massive that I wondered whether he had a troll among his ancestors, his behavior was nothing short of childish.

I scratched my chin as I watched the giant fidget.

*I’m seeing all kinds of weirdos today.*

I thought I’d developed a decent tolerance after meeting all sorts of people in the Murim, but this guy was a first.

Still, settling down this commotion took priority over my personal curiosity.

“Come on. Back away slowly.”

“Back away?”

“Yeah.”

I had no intention of pretending to be some agent of justice. It wasn’t as though I was overflowing with a sense of duty.

But this was the middle of a main street in Henan. If the fight continued, civilians could end up getting hurt.

“I don’t know what happened, but let’s stop here. All right?”

I spoke gently and glanced at Gung Gibang.

Quick to catch on, Gung Gibang understood what I meant and began evacuating the civilians who had been unable to escape and were still sitting on the ground.

The giant watched him, his huge eyes rolling from side to side.

“That guy. Insulted me.”

The thick finger pointed toward Hwangbo Ak, who was bent over and coughing weakly.

“He insulted you?”

“Rootless practitioner of demonic, heterodox arts. Pig as stupid as they come. What are you going to do if you glare at me?”

“Ah.”

“My lord said to think three times before fighting. So I thought three times and fought. He drew his sword first, too.”

I could more or less figure out what had happened.

The words were short and disjointed, but they were enough to understand the situation.

Hwangbo Ak was the Lesser Family Head of the Hwangbo Family, which held sway over the Shandong region. It wasn’t hard to imagine a Murim golden spoon with enough martial talent to join the Ten Dragons and Phoenixes picking a fight with a martial artist from the demonic, heterodox side.

Besides, Gung Gibang had once called Hwangbo Ak a real pain in the ass.

*So this guy is from the unorthodox faction.*

No wonder the aura he gave off had been so unusual.

Aside from some Third Rate dark-path figures, I had never met a proper martial artist who practiced demonic, heterodox arts. I had to forcibly suppress the curiosity that suddenly rose inside me.

One thought had crossed my mind.

“Did you lay a hand on anyone else?”

“Someone else?”

“Yeah. There must have been…… other people with him.”

My heart gave a small beat. The three syllables of Ju Hwaran’s name, which I had been unable to voice, lingered at the tip of my tongue.

The giant tilted his head and blinked.

“There were. Two men. One was strong, and one was weak. And……”

“And?”

“A pretty woman. A very pretty woman.”

“Damn. At least you have good taste.”

“Huh?”

“Nothing. So, did you fight them, too?”

“No. I only hit that guy. The pretty woman. She was as kind as she was beautiful.”

She was safe.

I let out a sigh of relief inwardly and patted the giant on the shoulder.

“Yeah, yeah. Good job. What a good little boy.”

“Good job? I’m good?”

“Of course you are. So let’s stop fighting and make up now. Got it?”

“Hmm. Hmmmm.”

I had almost won him over.

Since he was from the unorthodox faction, I had wondered whether I should simply knock him down. But gently coaxing him like a kindergartner from the Sunshine Class was enough.

It was at that exact moment, as the giant rolled his eyes full of serious thought, that a furious shout rang out from behind me.

“What do you think you’re doing?”

I turned around. Hwangbo Ak had already straightened up and was glaring in our direction, his eyes blazing.

“Blazing Flame Divine Dragon! Are my ears deceiving me? You’re taking the side of a demonic, heterodox practitioner!”

He was a stranger to me, but apparently I wasn’t to him.

Well, neither of us was in a situation relaxed enough for introductions, so that was convenient.

I calmly gestured toward Hwangbo Ak.

“You’re up. Come over here and make up with him.”

“M-Make up?”

“From what I’ve heard, he had his reasons. Don’t cause any more trouble. Let’s wrap things up here. Be a man, shake hands once, and call it done. Let’s keep things friendly.”

But Hwangbo Ak opened his eyes wide like someone who had locked in Yasuo and then gotten hit with a family insult.

“How can you do this?”

“I can do it just fine. Come over while I’m asking nicely.”

“A fellow orthodox martial artist has been harmed by a practitioner of demonic, heterodox arts. How can you take the side of that vile unorthodox whelp?”

“What does it matter whether he’s from the unorthodox faction or the orthodox faction? We’re all one family in the Murim Alliance. Haven’t you heard that song? We are all friends. That’s right, that’s right.”

“What song are you talking about? And members of the same family? Have you forgotten what those demonic, heterodox bastards did during the Great Faction War?”

“Forgot? I’ve never even experienced it. Did you take part in the Great Faction War? You look younger than I expected.”

“Stop talking nonsense and move! This Young Master must make that bastard kneel and apologize!”

Whoosh.

A warm breeze suddenly blew over my head. It was the giant’s breath.

He was one head taller than me. No, two.

“Kneel? You. Me?”

Hwangbo Ak flinched for the briefest moment, then gritted his teeth.

“Fine. You may have pushed me back earlier because you launched a despicable surprise attack, but I’ll make you regret provoking this Young Master even in death!”

“No. You. I kill.”

The giant’s eyes turned cold.

Fwoosh—whoosh!

A piercing sound tore into my ears.

Hwangbo Ak’s body, shooting forward like a ray of light, twisted violently. His leg lashed out like a whip, wrapped in visible internal energy.

*A kicking technique?*

The Hwangbo Family was a venerable martial family that had produced masters of punches and kicks for generations.

What Hwangbo Ak had unleashed was undoubtedly the Hwangbo Family’s secret martial art—the very technique that had allowed them to reign as the hegemon of Shandong Province.

But……

“You! I kill!”

He had picked the wrong opponent.

From what I could tell, the giant’s martial prowess was in no way inferior to Hwangbo Ak’s. If anything, it would not be an exaggeration to say he was a move or two ahead.

And in the giant’s hands was now a massive two-section staff to match his enormous frame.

Whoosh!

Fast and powerful.

The two-section staff advanced as though crushing the space around it, revealing the giant’s tremendous strength and speed.

At the moment of impact, after watching until the very last instant, I quietly extended both arms.

Boom!

A deafening roar erupted, followed by a massive wave of qi. Materials, dust, and dirt scattered across the ground were blasted beyond a three-zhang radius, and the people nearby sucked in startled breaths.

And in the middle of it all were two pairs of trembling eyes.

How?

The question in the giant’s and Hwangbo Ak’s eyes was unmistakable. Both of them stared in shock at the staff and leg caught in solid grips.

With a single movement, I had stopped every attack and brought the fight to an end.

“This…….”

“Strong! You, strong!”

Meeting their wavering gazes, I slowly opened my mouth.

“Now, let’s make up.”

Ah. I’d forgotten to add one thing.

“If you don’t want me to beat you to death.”

“……!”

“……!”

You could get more done with kind words and a fist than with kind words alone.

The giant stared blankly at me for a moment before stammering,

“I-I will make up. I’m good.”

“Yeah, you’re good. Now, who wants to be a bad little boy?”

My gaze naturally turned toward Hwangbo Ak. His lips pressed into a tight line.

“Blazing Flame Divine Dragon, are you really planning to—”

“Oh! An additional piece of information has arrived! Every bad little boy I’ve met so far has been beaten half to death by me and turned good!”

“……Come to think of it, I suppose I bear some responsibility as well.”

“Good. Then we’re settled.”

Only then did I release the two-section staff and ankle I had been gripping tightly.

The giant kept stealing bewildered glances at me, while Hwangbo Ak trembled with humiliation. But he didn’t dare resume the fight.

He only glared at me with a mixture of anger and fear, his lips moving soundlessly.

“Blazing Flame Divine Dragon, after this, can you still call yourself orthodox?”

“Wow. That’s exactly what I was about to ask you.”

“Very well. I suppose you’re acting this way because you don’t know who this Young Master is……”

“Hwangbo Ak. Twenty-nine years old. Lesser Family Head of the Hwangbo Family. Sobriquet: Shandong Fist Dragon.”

“……!”

“Oh, and he recently had a wet dream.”

“That’s not true!”

“If you say so.”

Hwangbo Ak’s clenched fist trembled.

“You knew who I was, and you still chose to humiliate me like this?”

“A fucking idiot has no gender, age, or allegiance to the orthodox or unorthodox factions. That’s my creed, and it seems to fit you perfectly.”

If I’d let the fight continue, he would’ve had his soul beaten out of him. I had stopped things from getting worse, only to hear all kinds of ridiculous nonsense.

*But why am I not angry?*

After thinking about it for a moment, I realized why.

Because he was even more of an idiot than I’d expected. And because he was so insignificant that he wasn’t worth getting worked up over.

*An insect.*

That was all Hwangbo Ak was to me. An ant that would die if I flicked it with my finger. A mosquito that would be brought to the brink of death by a careless swing of my hand.

After spending so much time alongside giants, I had become a giant myself. It felt as though I had become Gulliver after arriving in Lilliput.

The Hwangbo Ak standing before me was no different.

Perhaps that was why his status as the Lesser Family Head of the Hwangbo Family and a member of the Ten Dragons and Phoenixes failed to impress me.

*Just a Lilliputian who’s a little bigger than the others.*

That was how Gulliver—and I—looked at Hwangbo Ak.

And perhaps some of what I was thinking had been visible in my eyes.

Hwangbo Ak’s face darkened with rage.

“You…….”

“Want some advice?”

“What?”

“Know who you’re dealing with before you pick a fight.”

“You bastard!”

A roar erupted, but I didn’t even blink as I continued.

Hwangbo Ak needed to carve what I was about to say into his bones.

“The Roaring Fury Swordsman. The Taeeul Merciless Sword. You’ve heard those names a lot, haven’t you? Well, maybe not lately. They’re both busy recovering.”

“……!”

“If you don’t want to add the Shandong Fist Dragon to their number, don’t try anything funny. This is your first and last warning.”

Whoosh.

Hwangbo Ak sucked in a startled breath as the aura I focused solely on him pressed down.

He must have heard what had happened to the Sect Leader of the Zhongnan Sect’s two Senior Brothers.

And now, he had realized once again that the Murim of the world operated according to two things:

A just and legitimate cause.

And the law of strength.

Tap.

I patted Hwangbo Ak’s trembling shoulder and smiled.

“You look like you’re having a hard time. I’ll explain things to the others, so go home.”

“B-But—”

“Go.”

There was nothing Hwangbo Ak could do but grit his teeth and leave.

And when his back, looking unusually small, had disappeared into the distance, a familiar voice reached my ears.

“Sir Jin!”

It was a voice I hadn’t heard in a long time—which made it all the more welcome.
## Chapter artifact 532

# Chapter 532

The young man thought long and hard.

*Where did everything go wrong?*

Was it when he had forced down the dumplings someone had bought? Or when he had ignored his mildly aching stomach and accidentally dozed off while standing guard?

He had no idea exactly where or how things had gone wrong. But one thing was certain.

BOOM!

The thunderous roar that had suddenly erupted the moment he entered the privy had ended everything for him.

“Ahhh. So warm…”

His Captain had once told him that giving up made things easier.

He had been right. The pleasure was heavenly, and warmth like a mother’s embrace spread through the young man’s lower body.

So why were tears running down his cheeks?

*Why else? Fuck.*

He had shit himself. He had really shit himself.

And he had done it in the privy of a large inn located on a crowded main street.

The inn was an expensive establishment where only people with money to spare could afford to dine, so the fact that its privies were separated by partitions was a small comfort.

But it didn’t change the fact that he could never leave in this state.

*If anyone finds out what happened, I’m finished.*

His spine prickled and his insides twisted at the mere thought.

A martial artist was nothing but skin once you stripped away his pride and martial arts.

Rather than let anyone discover his current condition and spread the story, he would much rather engage in a life-and-death duel against a cruel fiend.

*What do I do?*

This was the greatest dilemma of his life.

His pants and underwear would obviously have to be thrown away. The leather shoes he had recently bought after working up the nerve to spend the money were already beyond saving.

What if he took everything off, pulled his shirt over his face, and ran across the main street with all his might?

*I’d die.*

In Murim, beating to death a man who was running desperately across the main street with everything dangling freely would practically be legal.

Every passing martial artist would rush out and start swinging their weapons. He might even receive an attack worse than anything a Dark Heaven fiend could unleash.

*Then I have no choice but to ask someone else for help. An inn attendant, maybe.*

That was at least somewhat manageable. If he called over an attendant and slipped him a few silver nyang, the man would bring him a cloth to wipe himself down and some clothes.

If the attendant happened to know his identity, it might cost extra, but that was still better than having to pay for his own funeral.

*What about the others…? No. I absolutely can’t let Captain or Gung Gibang see me like this!*

Hyuk Mujin made a solemn vow.

Unfortunately, his traveling companions were more persistent than poisonous snakes. If they got hold of a weakness like this, they would tease him for at least ten years—possibly even twenty or thirty.

No, they would probably keep going until the very moment Hyuk Mujin was on his deathbed.

*“Mujin…”*

*“Oh, you Hyuk bastard!”*

*“Heh heh. You arrived right on time, Captain. And Great Hero Gung.”*

*“Sob. Of course I had to arrive on time! You were late that day and shit your pants, but I’m not going to be late!”*

*“Hyuk, rest easy now. You can stink up the place behind the folding screen all you want.”*

*“…Please stop.”*

It was a miserable end, even in his imagination.

For a moment, he considered sending an attendant to call Cheongpung, who had remained behind at their lodgings.

But that would be like digging his own grave.

*“Wow! This is the first time I’ve seen someone who shit his pants! At first, I thought you were a snake! You’re a Thousand-Year Dung-Horned Snake that looks just like Mimi!”*

*“Wait. Young Master Cheongpung! Wait!”*

*“Stay here. I’ll go get the others! Excuse me! Daoist from Wudang! Someone I know shit his pants over here…”*

*“You fucking bastard!”*

It would be a hundred times better to hang a sign around his neck that said *The Man Who Shit His Pants* and walk around with it.

Hyuk Mujin was trembling from the chills brought on by the horrifying images filling his mind when it happened.

Rattle.

The door opened, and he sensed someone’s presence.

Hyuk Mujin’s eyes flew open. He cleared his throat.

“Ahem. Cough.”

When there was no response from outside, he coughed even harder.

“Ahem! Ahem! Is anyone there? Cough, cough!”

“Hm?”

At last, he got a response. Hyuk Mujin swallowed dryly and forced out a dignified voice.

“Is that an inn attendant?”

Someone outside answered. The young man’s soft voice naturally carried the casual tone of someone speaking down to him.

“You seem to be looking for an attendant, but unfortunately, I don’t have time to worry about that. You heard it yourself, so you know there’s quite a commotion going on.”

There was no way he could have missed it. That damned roar had been the decisive cause.

It wasn’t as though the building had collapsed, but everyone still seemed busy dealing with the aftermath.

*I should take comfort in the fact that someone is still coming to the privy in the middle of all this.*

That was when Hyuk Mujin heard the man say,

“Then, good luck with that.”

The presence began to recede with those indifferent words.

Hyuk Mujin’s heart plummeted.

“W-Wait! Just a moment!”

“Hm?”

“I’m sorry, but could you help me? I really need help.”

“Well, I’m a busy man myself.”

“A small problem has come up.”

“If it’s a small problem, you should solve it yourself.”

“Wait! Hyung! Father! Benefactor!”

After a brief silence, the voice came again.

“Did you shit yourself?”

Did you shit yourself? Did you shit yourself? Did you shit yourself?

The single question drilled into his ears like an echo. Hyuk Mujin answered in a tear-choked voice.

“Sniff. I did.”

“The big one? The small one?”

“……”

“Good grief. Both?”

“Urgh. Sob…”

The man outside muttered quietly.

“They say taking care of the big job naturally takes care of the small one, too.”

“Please. Please help me.”

“If I see an inn attendant on my way, I’ll let him know.”

“C-Couldn’t you bring me something right now? It might have dried by the time an attendant comes!”

“……That’s disgusting. Anyway, I have someone to meet, so I’ll be going.”

“W-Wait!”

Desperate, Hyuk Mujin squeezed his eyes shut and opened his mouth.

“I-I’m Hyuk Mujin! You appear to be a martial artist as well. If you help me this once and keep quiet about it, I’ll never forget this favor!”

“Hyuk Mujin? As in the Blazing Flame Divine Dragon’s little toe?”

“……That’s right. But I’m his right arm, not his little toe.”

Hyuk Mujin’s vision went dark.

He had guessed that the man outside was a martial artist, but he had never expected the man to identify him so quickly.

At least his attempt to keep the man from leaving had worked.

“I don’t know whether this is coincidence or fate. Interesting.”

“……?”

Flap.

Just as Hyuk Mujin was wondering what he meant, a silk outer robe fluttered down over his head, accompanied by a low chuckle whose meaning he could not understand.

Hyuk Mujin caught the robe by reflex and stammered his thanks.

“T-Thank you.”

“Clean yourself up and come out. I’ll give you a chance to repay the favor.”

“Um. Do you happen to know our Captain…?”

“It’s our first meeting. But the Blazing Flame Divine Dragon isn’t the sort to treat me poorly.”

The soft voice continued.

“Not when I’m the benefactor who helped his little toe—or rather, his right arm.”

“……!”

Hyuk Mujin realized that he had no idea who the man was, but he had clearly gotten tangled up in something serious.

By then, however, it was too late for regret. Hyuk Mujin opened his mouth with a stiff expression.

“Did you throw me this robe for that reason?”

“Why? Have you changed your mind? Then I’ll throw the robe back—”

“If this is how things are going to be, could you find me some clothes to wear, too? I’m far beyond saving with a simple wipe.”

“……”

* * *

Gowolru.

That was the name of the luxurious three-story inn.

Judging by its size, trouble must have broken out there often. The moment we entered, the owner approached us as though he had been waiting, leading more than ten hired martial artists behind him.

He spoke with a fierce expression.

“I don’t know who you are, but no matter how highly regarded you young heroes may be in the martial world, compensation must still be paid—”

I cut him off before he could finish.

“First, my condolences. How much will repairs cost?”

“What?”

“Repairs.”

“……Around two hundred silver nyang, I would say.”

“Then let’s make it three hundred nyang, including compensation for all the other damage.”

“What?”

At worst, part of the third-floor railing and a section of the wall had collapsed.

The owner had gone out on a limb and asked for two hundred nyang, only for me to counter with three hundred. From his perspective, he probably had no idea what kind of person I was.

But I had no hesitation about naming such an enormous sum.

The reason was simple.

*It wasn’t my money anyway.*

“Put it on the Hwangbo Family’s tab. If that Lesser Family Head bastard gives you trouble when you go to collect, tell him Jin Taekyung sent you.”

“How am I supposed to say that…? Wait. Jin Taekyung?”

The owner and the hired blades, who had been studying me suspiciously, opened their eyes wide.

“J-Jin Taekyung? The Jin Taekyung of the Jin Family of Taiyuan?”

“The Blazing Flame Divine Dragon! It’s the Blazing Flame Divine Dragon!”

“I have descended.”

To operate an inn of this size on the main street of Henan, the owner had to be capable.

And the owner of Gowolru was clearly quick-witted.

“It is the honor of a lifetime to receive a visit from Great Hero Jin Taekyung!”

“Better consider it the honor of your entire family. In any case, my throat has been rather scratchy lately…”

“I’ll have a feast laid out so lavishly that it’ll break the table legs! What are you all standing around for?”

As expected, financial therapy was the best way to calm people down.

The owner’s eyes had brightened as though nothing had ever happened. He shouted the order, then led the hired blades away.

A small laugh drifted over from beside me.

I turned toward the owner of that laugh, whose sound made my ears itch just by reaching them.

“What is it?”

Dagger Hidden Flower Ju Hwaran answered with a gaze like forget-me-nots.

“Nothing. I was just reminded of what happened last time.”

“If you mean the last time… Ah.”

“You haven’t forgotten, have you?”

“Of course not.”

The dispute between the Yongbong Escort Bureau and the Zhongnan Sect.

While heading to Sichuan to treat Jeok Cheongang, I had happened to get involved in the matter. After crushing the Taeeul Merciless Sword’s attempt to force the issue through strength, I had even participated in the negotiations.

*I uprooted two or three of Zhongnan Sect’s foundation pillars back then.*

Ju Hwaran was clearly thinking about what had happened. Her eyes glimmered faintly as she looked at me.

“It hasn’t even been that long, but it feels like it’s been ages.”

“It does. Funny, isn’t it?”

The truly strange thing was something else.

Who would have thought that looking into the eyes of the person I was speaking to could be so difficult?

“Why do you keep avoiding my eyes?”

“I’m cross-eyed. I’m looking straight at you right now.”

“Pfft.”

“W-Why are you laughing?”

Had I said something wrong?

Ju Hwaran smiled faintly at my confusion.

“You really haven’t changed at all, Great Hero Jin. Not even a little.”

“You haven’t changed either, Young Lady Ju…”

There was something that almost slipped out, but I barely managed to hold it back.

That was partly because of the several pairs of eyes beside me, watching with narrowed eyes.

Pretending to cough, I secretly sent a Sound Transmission.

*—Gib, why are you staring so hard? Do you want me to punch a hole through your solar plexus?*

*—Ahem. Cough.*

One down.

But there were still three of them left.

Of those three, I looked meaningfully at the one who seemed the least useful.

*—Hey.*

Kunlun Cloud Dragon Hak Woo was the Kunlun Sect’s greatest young prodigy. During the Star-Array Grand Banquet preliminaries, I had stepped on his crown and sent him tumbling down.

For some reason, he had developed a bald spot. He flinched at my gaze and sent a Sound Transmission back.

*—W-What is it, Fellow Daoist Jin?*

*—Nothing much. I was just thinking you probably had somewhere important to be.*

*—Huh?*

*—Tell me honestly. You’re busy right now, aren’t you?*

*—Infinite Life Buddha. I’m not busy.*

*—I don’t think so. I think you’ve just remembered something urgent and need to leave right away.*

*—I have already received permission from my sect regarding today’s appointment. There’s no urgent matter that I need to attend to—*

*—Hey, Hak.*

*—Infinite Life Buddha?*

*—Go. Unless you want me to pluck out every last strand of hair on your head.*

*—……!*

To bald people, hair was as precious as life itself.

Only then did Hak Woo understand what I meant. With a mournful expression, he turned toward Ju Hwaran.

“Um. Young Lady Ju.”

“Yes? What is it?”

“I have just remembered an urgent matter, so I believe I must leave. I’m truly sorry to say this, Young Lady Ju.”

“No, it’s all right. I’m fine, so go ahead.”

“But even so, it’s rude of me to—”

“I can’t walk you out very far. Take care.”

“Wait. At least let me finish what I was saying…”

“I’ll see you next time!”

Come to think of it, Ju Hwaran seemed surprisingly impatient.

Kunlun Cloud Dragon Hak Woo looked back and forth between Ju Hwaran and me with eyes on the verge of tears before disappearing, and my gaze naturally shifted to the two people I had yet to deal with.

“I’ll tell you in advance. I’m not leaving. I’m the Young Bureau Head’s direct escort.”

Song Ilseom, an escort sitting crookedly with a single sword tucked against his chest, spoke flatly.

I shrugged.

“I didn’t ask you to leave. I have no intention of doing so, either.”

“Hm. I’ll take your word for it.”

Song Ilseom’s apparent identity was Ju Hwaran’s escort, but he possessed another hidden identity known only to a very small number of people.

He was the last descendant of the Guangdong Chen Family, an iron-blooded martial family destroyed by the Demonic Cult during the Great Faction War.

He was also an undefeated wandering martial artist who had once gone by the epithet Soul-Chasing Guest.

*Come to think of it, this guy hasn’t changed at all.*

I had been famous back then, too, but my fame was nothing compared to what it was now.

Even so, Song Ilseom was just as calm and prickly as he had been when we first met.

Maybe that was why I liked him even more.

But the last one was…

“Hungry. Food. Too late.”

“……”

What was with that shameless attitude?

Why had this unidentified giant followed us?

I did not know the reason, but I had not stopped him. I was curious about his true identity.

With Qi Sense, I could determine little more than his Level and name. I would have to learn which sect he belonged to and what sort of people he was connected to through conversation.

“You must be very hungry.”

“Correct. I very hungry.”

The giant continued with a serious expression.

“Today. Only ate six meals. Feel like dying.”

“……”

*Six meals? Is that for real?*

I didn’t know which sect he belonged to, but I’d bet Hyuk Mujin’s wrist that this bastard’s food bill had already cost it a few foundation pillars.

*Wait. Hyuk Mujin?*

Come to think of it, he had disappeared saying he was going to shit. Why hadn’t he come back yet?

I had only just noticed Hyuk Mujin’s absence and was looking around when it happened.

“C-Captain!”

The shout was filled with inexplicable anxiety.

But my gaze was not fixed on Hyuk Mujin, who had finally appeared.

Behind him stood an unfamiliar man, smiling faintly in my direction.

Our eyes met.

I muttered quietly,

“Who might that be…?”
## Chapter artifact 533

# Chapter 533

The third floor, where the commotion had broken out earlier, had been completely cleared out long ago.

Not many people were bold enough to calmly sip their drinks in a place where a fight between martial artists had brought down the railings and even parts of the walls.

Besides, martial artists wealthy and important enough to enter Gowolru generally sought out restaurants rather than inns.

So it wasn’t difficult to guess the identity of the uninvited guest who was still smiling despite everything.

*A martial artist.*

There was no need to think about it any further.

The man looked no more than thirty, with open, strikingly handsome features, and a blackish saber scabbard hung from his waist.

And then there was…

*His aura.*

I couldn’t help exclaiming inwardly. The power and aura I felt from him were stronger than those of any member of the Ten Dragons and Phoenixes I had encountered so far.

Even stronger than Jin Mukyung before he entered seclusion.

*Could it be?*

The name of someone I had yet to meet flashed through my mind.

Murong Yeonghwi, the One-Ride Heavenly Dragon. The eldest son of the Murong Family, and one of the foremost among the ten dragons and phoenixes known as the greatest young prodigies in the Murim.

*Should I use Qi Sense to confirm his name?*

Just as I was watching him with that thought in mind, Hyuk Mujin approached with an expression like he was about to shit himself and opened his mouth.

“Um, this is an acquaintance of mine. He said he really wanted to meet you, Captain…”

I stared at the man and spoke.

“Mujin.”

“Yes?”

“I’m asking because I’m genuinely curious. You didn’t actually expect me to believe that, did you?”

“Ghk.”

“Report honestly. Now.”

“……”

“I shit my pants, and he helped me.”

“I figured it was something like that. We’ll talk later. Step aside.”

As Hyuk Mujin backed away with an expression like he wanted to kill himself, the smile at the corners of the man’s mouth deepened.

“Well, this is something. You’re even more perceptive than I expected.”

“It’s not that impressive. It’s more unusual for the son of a textile-shop owner to have a friend like you.”

“Hm. I didn’t know that. Though, to be honest, I didn’t have particularly high expectations.”

“You’re taking your time introducing yourself for someone we’ve just met. Who are you?”

“I’m merely a passing traveler.”

“Your speech is pretty casual, too.”

“If that bothers you, drop the formalities yourself. Relax.”

What a strange guy. He felt different from everyone else I had met until now. I loosely crossed my arms and answered.

“Sure. Let’s keep it casual.”

The man laughed out loud at my response.

“I had only heard about the Blazing Flame Divine Dragon through rumors, but you’re even more interesting than I’d heard.”

“It’s not exactly a fun situation from where I’m standing. Anyway, are you still planning to introduce yourself as a passing traveler?”

“You don’t seem to know who I am. A few people here already look like they recognize me.”

As soon as he finished speaking, his gaze turned toward Ju Hwaran, Gung Gibang, and Song Ilseom.

Ju Hwaran, who had been wearing a faint smile only moments ago, spoke with a stiff expression.

“It’s been a while, Young Sect Leader.”

Young Sect Leader?

A puzzled voice slipped from my lips before I could stop it.

“Young Lady Ju. You know him?”

“We met once. In Gansu.”

“Gansu…”

Along with Qinghai and Sichuan, Gansu had suffered some of the heaviest damage during the Great Faction War. It was also where the Kongtong Sect, one of the Nine Sects and One Gang, was located.

I stared at the man.

“No matter how closely I look, you don’t seem like a Daoist of the Kongtong Sect. If I’m wrong, tell me now.”

“No, you saw correctly. If anything, it’s the opposite.”

The man shrugged and continued.

“If Kongtong found out it had been associated with a demonic, heterodox practitioner like me, it would be displeased. Of course, I feel the same way.”

“A demonic, heterodox practitioner?”

“You may or may not have heard of the Black Dragon Demon Gate.”

Black Dragon Demon Gate. It didn’t take long for me to recall those four words.

“I’ve heard of it.”

At some point, I had heard about the unorthodox sect that dominated Gansu.

Even though the Kongtong Sect was considered one of the weaker members of the Nine Sects and One Gang, I had found it rather surprising that an unorthodox faction rejected by the public could wield that much power.

*Now I understand why this guy isn’t one of the Ten Dragons and Phoenixes.*

His situation was similar to Song Ilseom’s.

No matter how loudly people cried out about the world’s Murim and their fellow martial artists, there was always a league of their own.

People—or rather, orthodox martial artists—had no desire to include wandering martial artists who sold their swords for money and demonic, heterodox practitioners no different from would-be criminals among the Ten Dragons and Phoenixes.

“So, what business does someone as important as the Young Sect Leader of the Black Dragon Demon Gate have here?”

At my question, the man suddenly furrowed his brow.

“Is that all?”

“What else do you need?”

“That…”

“If you want to say more, give me your sobriquet. I might forget it, but I should at least know it.”

“……Black Dragon Saber. Sama Pyo.”

“I didn’t ask for your name. But all right, now I know.”

“……”

“Your name is pretty cool, though. Are you related to Sima Yi?[^1]”

“What?”

“What do you mean, what? Sima Yi. The one from *Romance of the Three Kingdoms*.”

[^1]: “Sama” is the Korean reading and “Sima” the Mandarin reading of the same surname, 司馬.

The man—or rather, Sama Pyo—answered with an awkward expression.

“Our surnames are the only thing we have in common. We have no relation.”

“Really? What a shame. If you were sworn enemies of the Zhuge Clan, I was going to introduce you to someone I know.”

“……That doesn’t mean I have a good relationship with the Zhuge Clan.”

“Yeah, that makes sense. Now tell me why you’re here.”

Sama Pyo studied me with a strange gaze before speaking.

“I came to retrieve my subordinate.”

“Your subordinate?”

“Yes. That bear-like fellow sitting over there.”

Not a single person present could have wondered who he meant. Everyone’s gaze, including mine, turned in the same direction.

The towering giant was crouched down so deeply that his enormous size seemed almost wasted, watching Sama Pyo nervously.

“Taishan. Get up.”

*That guy is from the Black Dragon Demon Gate, too?*

Still, whoever named him had chosen a name that fit him perfectly.

At Sama Pyo’s call, the giant—whose physique truly resembled a mountain—answered in a clumsy voice.

“Lord. I am not Taishan. You mistook person.”

“……”

*He really needs to put some points into intelligence.*

Sama Pyo clicked his tongue.

“You troublemaker. You cause trouble every time I leave you alone. Enough. Get up.”

“Cannot. Food not out yet.”

“What a bear of a man. You’ve eaten that much and you’re still not full?”

“Today. Ate six meals. Barely.”

“What? Six meals?”

Sama Pyo muttered with a rigid expression.

“Only six meals? Have you suffered an Internal Injury?”

“……”

“……”

*For fuck’s sake. I’m speechless.*

While everyone—including me—lost all ability to speak, Sama Pyo thought for a moment and nodded.

“All right. Then we’ll eat before we go.”

“Food! Good! Taishan eat all food here!”

I spoke with complete sincerity.

“Could you please take that guy—Taishan or the entire scenic landscape, or whatever—and get the hell out of here?”

*Why are these lunatics trying to slip into our table?*

Sama Pyo frowned at my firm refusal.

“How stingy.”

“That’s right! Stingy! But Lord, what is stingy?”

“Taishan, it’s short for ‘you fucking bastards.’”

After kindly explaining it to a child from the Sunshine Class, I pointed toward the stairs and continued.

“So go now. You fucking bastards.”

“……!”

A heavy silence pressed down on the room.

Ju Hwaran let out a breath and reached for the flexible sword at her waist, while Song Ilseom, who had been sitting in a relaxed posture, straightened his body.

And their sudden vigilance was directed at only one person.

*Sama Pyo.*

But he didn’t move.

His eyes widened slightly, and he merely stared at me with an unreadable look.

Then his tightly closed lips parted, and a gentle voice flowed out.

“How refreshing. I’ve never had an experience like this in Gansu—or in my entire life.”

“The first time is the hardest. It gets easier from the second time onward. I’ll give you plenty more of it from now on, so don’t worry.”

“Plenty more in the future, too?”

“I have a feeling we’ll be seeing each other often. If not, forget it.”

“You’re certainly different. Very different. Don’t you agree?”

The question he added at the end wasn’t directed at me.

Taishan, who had been rolling his enormous eyes around, nodded.

“Lord. Correct. That person. Different.”

“Yes, so it seems.”

A mysterious smile appeared at the corners of Sama Pyo’s mouth, then vanished.

The next moment, Sama Pyo reached up and grabbed Taishan by the nape of his neck, far above his own head, then hauled him upright.

“It seems difficult to stay somewhere we aren’t welcome. Let’s go, you fool.”

“Taishan disappointed. But Taishan follows Lord. Obeys well.”

“Then we’ll be off. See you next time, Blazing Flame Divine Dragon. And Young Lady Ju.”

That was it.

After the two of them descended the stairs, the sound of the inn’s door closing reached us a short while later. Ju Hwaran’s stiff expression relaxed slightly.

“Whew.”

She let out a quiet sigh. Then Song Ilseom relaxed as well, leaning back against his chair.

“He’s stronger than before. No, perhaps I should say he’s more dangerous.”

Hearing that, the question I had been carrying since earlier grew even deeper.

Judging by everything I had seen, they had clearly experienced something together—more than merely having met once…

*What was it?*

Perhaps someone noticed my expression, because a foot tapped mine beneath the table.

Tap. Tap.

There was no need to look. It was Gung Gibang. His chapped lips moved after sending the signal.

*—Don’t say anything. Don’t ask anything.*

*—Why?*

*—Just don’t, you fucking bastard.*

*What the hell is wrong with this guy? What could possibly be so serious?*

But human nature was simple. Even if I didn’t ask the person involved directly, I still wanted to hear the story from someone who knew about it.

*—What is it?*

*—I don’t want to. I’m not telling you.*

*—Why?*

*—Because you won’t gain anything from hearing it.*

At that moment, Ju Hwaran, who was sitting right beside Gung Gibang and directly across from me, handed me a plate with a smile.

“Please try this, Great Hero Jin.”

“Ah, yes.”

I was supposed to smile, but for some reason, I couldn’t.

I shoved the food Ju Hwaran had given me into my mouth and continued sending Sound Transmissions.

*—Tell me.*

*—I said no.*

*—Tell me.*

*—I said I won’t.*

*This bastard, seriously.*

He could at least have pretended not to know anything. But he refused to budge, stonewalling me so completely that I grew irritated.

And it was at the exact moment I was about to send another Sound Transmission that Ju Hwaran spoke.

“Oh, Great Hero Jin. There’s something I forgot to mention.”

“Tell me what it is while I’m still asking nicely, okay?”

I nearly made a huge mistake.

With my mouth full of food, I raised my head, and Ju Hwaran continued.

“That person. The Young Sect Leader of the Black Dragon Demon Gate.”

“Sama Pyo?”

“Mm. Yes.”

“Um… Did something happen?”

“If you call it something, yes. If you don’t, then no.”

Ju Hwaran stared at me and dropped a single sentence.

No, it wasn’t a sentence.

It was a bomb.

“He used to be my fiancé.”

“Pffft!”

“Aaaaaah!”

“Uaaaaah!”
## Chapter artifact 534

# Chapter 534

Jingle. Clack.

The inn’s door closed with the final ring of the bell, and the stares that had been stabbing relentlessly into the back of Sama Pyo’s head ever since he descended the stairs vanished along with it.

But Sama Pyo already knew.

This wasn’t the end. It was the beginning of something else.

“Those two who just came out of Gowolru…”

“Are you sure?”

“Absolutely. The Black Dragon Saber, Sama Pyo, is the Young Sect Leader of the Black Dragon Demon Gate. And that huge fellow beside him is the monster who crushed Blood Cudgel’s skull seven days ago.”

“I heard he got into a fight with the Hwangbo Family’s Lesser Family Head earlier. Making trouble like that at a time like this… Tsk, tsk.”

“Leave them be. Isn’t that what demonic, heterodox practitioners are like? We’ll have to borrow even their hands to drive out Dark Heaven.”

“I don’t like it one bit. How do we know they won’t stab us in the back?”

“That’s what I’m saying… Shh. The big fellow is looking this way.”

Countless gazes and whispers were focused on them. Even if the people spoke as quietly as possible, they were close enough for him to hear every word if he chose to.

But despite the voices burrowing into his ears, Sama Pyo’s expression remained impassive as he walked.

*There’s nothing strange about it.*

He was already far too familiar with this situation.

Even in Gansu, where the Black Dragon Demon Gate was based and wielded immense influence, things had been the same. The label of demonic, heterodox practitioner that had followed him since birth was an inescapable shackle.

“Whoof.”

A rough snort came from beside him. Sama Pyo glanced at Taishan, who was rolling his enormous eyes around, then moved his lips.

*—Stop.*

Taishan’s hand, which had been sliding toward the two-section staff strapped across his back, halted.

Strength entered the Sound Transmission Sama Pyo sent him.

*—Taishan. You little bastard.*

*—……Understood, Lord. Taishan will endure.*

*—That’s right. Good boy.*

*—Taishan listens well. Taishan likes Lord. Hehehe.*

Taishan flashed a broad grin as though nothing had happened. Sama Pyo let out a quiet laugh.

*—Yes. I like you very much, too.*

*—Taishan got praised a lot today.*

*—Oh? Who was kind enough to praise you?*

*—Mm. Blazing Flame Divine Dragon praised me.*

Sama Pyo’s steps slowed.

*—Blazing Flame Divine Dragon Jin Taekyung?*

*—Correct. Jin Taekyung. He said Taishan was a good boy.*

*—It seems you like him.*

*—Like him. Very strong. Good. Taishan praised him.*

Sama Pyo gazed at Taishan’s profile as the giant strode along excitedly.

Taishan had been born with outstanding martial talent and divine strength, but an unfortunate accident long ago had left him with a head injury. He was no different from a child.

Perhaps it was because of that memory. He was extremely wary around strangers, and aside from Sama Pyo, he rarely opened his heart to anyone.

*It’s rare for someone like him to evaluate anyone besides me so favorably.*

Blazing Flame Divine Dragon Jin Taekyung.

The image of the carefree yet sly young man flashed before Sama Pyo’s eyes. Along with it came the immeasurably powerful aura hidden beneath his calm expression and voice.

*So that’s why they call him the Divine Dragon.*

The world was vast, and there were countless masters. Ordinary people admired the Ten Dragons and Phoenixes, calling them the greatest young prodigies in the Murim.

But Sama Pyo had never acknowledged them.

*They’re nothing more than empty reputations created inside the walls they built for themselves.*

In reality, anyone outside those walls was rejected. Sama Pyo had met more than one or two orthodox martial artists who committed shameless acts while hiding behind irritating words like *justice* and *the orthodox path*.

But…

*He was different. He was definitely different.*

Blazing Flame Divine Dragon Jin Taekyung.

Although their meeting had been brief, Sama Pyo had realized one thing for certain.

Jin Taekyung was special.

His astonishing martial power, which far surpassed that of any young prodigy, was one reason. But what made him feel even more extraordinary was his attitude—the way he differed from everyone else.

The conversation he had shared with Jin Taekyung only moments earlier passed through Sama Pyo’s mind.

*“I don’t know whether you’ve heard of the Black Dragon Demon Gate.”*

*“So what brings someone as important as the Young Sect Leader of the Black Dragon Demon Gate here?”*

*“Is that all?”*

*“What else do you need?”*

*“……!”*

It had been an unexpected question, and Sama Pyo had been rendered speechless for a moment.

That was because it was a question that had never existed anywhere along the path he had walked as Sama Pyo, the Young Sect Leader of the Black Dragon Demon Gate.

*What else do I need? What else…*

The thoughts he muttered inside his heart never escaped his lips.

Sama Pyo silently moved his lips, then turned his head toward Taishan.

*—I have one question.*

*—……?*

*—If you had to fight Blazing Flame Divine Dragon Jin Taekyung, what would you do?*

It happened in the blink of an eye.

Taishan’s smiling face stiffened.

Then a Sound Transmission arrived without the slightest hesitation.

*—Taishan owes Lord a great debt. If Lord commands, Taishan fights anyone.*

*—Didn’t you say you liked Jin Taekyung?*

*—Like Jin Taekyung. But not as much as Lord. Taishan gives life for Lord’s command.*

*—I see.*

Sama Pyo let out a quiet laugh and shook his head.

*—That’s enough. You really are a good fellow.*

*—Taishan good. And good Taishan hungry.*

At the sight of the enormous childlike man glancing at him mournfully, Sama Pyo burst out laughing.

“Come on. Let’s go somewhere. Tonight, I’ll feed you until you’re so full you burst.”

“Hehehe. Lord promised. Taishan believes Lord.”

“Yes, yes.”

“But, Lord.”

“What is it?”

“That woman earlier. Pretty. Very pretty. Who?”

Sama Pyo’s steps abruptly stopped.

Taishan tilted his head when he sensed something strange.

“Lord?”

“No. Was she really that pretty?”

“Yes. Pretty and good.”

“They say you can see ten fathoms into the water, but not one fathom into a person’s heart. How could you know what was hidden inside her after seeing only her face for a moment?”

Taishan vigorously shook his head.

“No! Pretty women are good!”

“……Don’t say it so loudly. People are looking.”

“Admit it! Taishan is right! Pretty means good!”

“Whew. You damned fool. I’m going on ahead.”

“Lord! Lord!”

Sama Pyo walked away, leaving Taishan’s desperate cries behind him. His face was as dry and expressionless as sand.

*Ju Hwaran… I never expected to meet her in a place like this.*

Sama Pyo couldn’t tell whether it was coincidence or fate.

But one thing was certain.

The woman who had been his fiancée, if only for a short time—Dagger Hidden Flower Ju Hwaran—would consider everything connected to him an ill-fated relationship.

*An ill-fated relationship… It wouldn’t be wrong.*

Sama Pyo’s gaze turned cold.

* * *

The meal that day ended without incident.

Under the owner’s lavish hospitality and the flood of attention from the people around us, we left the inn and exchanged farewells.

No. To be precise, it would be more accurate to say that Ju Hwaran said farewell to us.

“I think I should be going. There are some matters related to the Escort Bureau that I need to take care of.”

Jab.

At Gung Gibang’s discreet poke to my side, I stood there blankly for a moment before reflexively opening my mouth.

“Oh, yes. Goodbye.”

“Yes. You too, Great Hero Jin.”

Jab.

Damn it. Apparently, that wasn’t the right thing to say.

“Um, Young Lady Ju.”

“Yes?”

“Would you like me to escort you back to your lodgings?”

“Thank you for the offer, but I’ll be fine. I’ve heard that you barely have enough time to train as it is.”

“Oh. Who told you that? I have been a little busy lately.”

Jab. Jab jab.

*Thanks, you bastard.*

Following the signals from my Gung-vigation system, which was once again informing me that I had veered off course, I gripped the steering wheel tightly.

“Even so, some strange people might approach you, so I think it would be better if I escorted you…”

“Ahaha. No, it’s all right. I’m a martial artist, too.”

“Oh, right. I wasn’t trying to underestimate you, but… well.”

“No, you’re right that I’m lacking compared to Great Hero Jin. Besides, Captain Song is here as well.”

At that, Song Ilseom spoke in his blunt voice.

“If people like that approach, I’ll cut them down in a single stroke. Don’t worry about such trivial matters.”

“You heard him, right?”

“……Yes. I heard him.”

Jab jab. Jabjabjabjab!

*You’re going to put a hole in my side, you bastard.*

But this time, I couldn’t think of anything else to say. My already tangled thoughts twisted together, then scattered.

And that brief silence meant the moment had passed.

“Then I’ll be going now. See you again.”

Ju Hwaran smiled brightly and turned away.

Her silken hair swayed, and a faint fragrance drifted from between the strands and through the air.

I stood there silently, watching the backs of the two people grow more distant.

That was when—

“This guy really is a fucking idiot.”

“Wow. You’re something else, Captain.”

“……”

There was no need to check who they were. I looked at Gung Gibang and Hyuk Mujin with mournful eyes.

“Where did I go wrong, and when?”

The two of them answered simultaneously, as though they had been waiting for the question.

“Since you spat food in Young Lady Ju’s face.”

“Wasn’t the problem Captain himself from the start?”

Their answers were different, but they had two things in common.

First, both of them were infuriating.

Second, both of them were facts I had a hard time arguing against.

“Damn it.”

I kicked the innocent ground.

Honestly, I felt a little aggrieved. How was I supposed to have stayed calm in that situation?

*A fiancé, out of nowhere.*

Even thinking about it again made my head spin.

At this point, it wasn’t a grenade. It was a ballistic missile.

The only thing that comforted me even a little was that the word *former* came before *fiancée*.

“I told you not to ask.”

I answered Gung Gibang with a sigh.

“If I’d known it would be like this, I wouldn’t have asked. Besides, Young Lady Ju brought it up first.”

“You kept making it obvious that you were curious.”

“Great Hero Gung is right. You should have simply assumed there was a reason and left it alone. Why did you…”

“The bastard who shit his pants should shut up.”

“……Yes, sir.”

“I didn’t shit my pants, so I can keep talking.”

“Not for long. In a little while, you’ll be shitting blood.”

“……Calm down. Put your fist down first.”

In truth, I didn’t even have the strength to hit him.

At the customer’s request, I lowered my fist and stared into the empty air.

“I want to turn back time.”

“You can’t.”

“Can’t do that.”

“Still, it wasn’t that obvious afterward, was it? I acted pretty calm.”

Gung Gibang and Hyuk Mujin smiled warmly before answering.

“Of course, of course. It wasn’t obvious at all. Except for the six times you knocked over your water glass.”

“You dropped your chopsticks seven times as well.”

“The best part was when the server told us to add anything else we wanted to the order slip, and you glared at him.”

“Wow. How did you even connect the order slip to Sama Pyo? It took me a long time to understand.”

“You were practically insane.”

“At minimum, you looked like Dark Heaven.”

“……”

*I get it, so stop it, you fucking bastards.*

I wanted nothing more than to beat them half to death, but I didn’t have the strength. All I could do was trudge along.

I didn’t have the energy to care whether my face was visible beneath my crooked bamboo hat, or whether people recognized me.

“Th-That person, could he be…”

“Gasp! It is! It’s Blazing Flame Divine Dragon Jin Taekyung!”

“But why is he walking like that?”

“How would I know?”

“Judging by the way he looks, you’d think some woman had dumped him.”

“Ha ha. What a joke.”

“……”

*Don’t laugh. It isn’t a joke.*

These days, I took damage from all sides even when I did nothing but breathe.

I let out a long sigh and adjusted my bamboo hat.

My mind was still hopelessly complicated.

*An ex-boyfriend. No, an ex-fiancé.*

I had already heard the rough circumstances.

Ju Hwaran had calmly and honestly told me about her past.

*“It was a political marriage. We had never even seen each other’s faces before then.”*

It was a common arrangement.

The Yongbong Escort Bureau had been declining day by day, and the Black Dragon Demon Gate had extended a hand to Ju Hwaran.

Along with an offer she couldn’t refuse.

*“I was the one who made the decision. For my stricken father.”*

That was when Ju Hwaran’s calm voice and expression rose before my eyes.

“My youngest.”

I blinked.

We had arrived at the entrance to our lodgings without my noticing.

The man who spoke to me was large, though not quite as enormous as Taishan.

Jin Wikyung continued.

“Great Hero Mae. No—the Alliance Leader is looking for you.”

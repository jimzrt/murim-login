# Checkpoint Review — 310–314

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

# Chapters 310–314

## Plot

At Black Stone Mountain, Heavenly Axe and five hundred Black Stone Stronghold bandits attack the Yongbong Escort Bureau after revealing their knowledge of its secretly transported Thousand-Year Snow Ginseng. Jin Taekyung arrives, accepts the Crisis of the Yongbong Escort Bureau, defeats and kills Heavenly Axe, and forces the surviving bandits to surrender. He completes the related Quests and levels up. Ju Hwaran, the bureau’s young leader, suspects that one of the senior escorts leaked the ginseng’s existence; Song Ilseom’s hostile behavior leaves his possible betrayal unresolved.

Taekyung continues toward Sichuan with Jeok Cheongang concealed on his pack frame, accompanied by Cheongpung, Gung Gibang, and Hyuk Mujin. In Xi’an, they meet Baek Museong, Huashan’s Lone Crane, who has learned of Shaolin’s blood calamity, Hong Dao’s death, and Mae Jonghak’s possible appointment as Alliance Leader. Baek foresees a coming crisis involving Dark Heaven and intends for Huashan to help prevent it.

Baek is confronting Hyuk Sopyung, the Zhongnan One Dragon, after Hyuk drunkenly destroyed Xi’an Tower’s private annex. Hyuk attacks Taekyung with seven-tenths of the Heavenly River Thirty-Six Swords, but Taekyung breaks through the technique, slaps him three times, and identifies himself publicly as the Sleeping Dragon of Shanxi and a Disciple of the Fire Gate Clan. He ends the dispute by invoking the greater threat posed by Dark Heaven. Cheongpung then apologizes to Baek for defeating him and the Three Plum Blossom Elites while escaping forced escort to Huashan the previous year.

## Continuity

- Jeok Cheongang remains unconscious with progressively blocked qi acupoints. Taekyung is carrying him to Sichuan while pursuing the Divine Physician through the System Quest **Find Mr. Shin in Sichuan**.
- Taekyung’s traveling party consists of Taekyung, Cheongpung, Gung Gibang, and Hyuk Mujin; Jeok is concealed beneath fur on Taekyung’s pack frame.
- Black Stone Stronghold is one of the Green Forest Alliance’s Eighteen Strongholds. Its leader Bangyeol, known as Heavenly Axe, was Level 93 and was killed by Taekyung; the surviving bandits were subdued.
- The Yongbong Escort Bureau has suffered repeated attacks for four months and lost most of its people while transporting the Thousand-Year Snow Ginseng for the Zhongnan Sect.
- Ju Hwaran suspects Seokchil, Noh Piljung, or Song Ilseom of leaking the ginseng information. She asked her uncle Heo Jun to watch Song Ilseom, who is a Level 110 escort captain and has shown hostility toward Taekyung.
- The Jin Family Escort Bureau and Yongbong Escort Bureau are business competitors, with Yongbong still dominant in Shaanxi.
- Baek Museong is Heavenly Sword True Person’s direct Disciple, the first of Huashan’s Three Plum Blossom Elites, and a likely future Huashan Sect Leader. He remains one level above Hyuk Sopyung.
- Hyuk Sopyung is a Peak master and the Zhongnan One Dragon. Taekyung defeated his seven-tenths Heavenly River Thirty-Six Swords and made him withdraw.
- Cheongpung is known as the Huashan Divine Dragon and previously defeated Baek and the Three Plum Blossom Elites while escaping forced escort to Huashan.
- Dark Heaven remains an active threat to the Murim. Shaolin’s blood calamity and Hong Dao’s death have intensified concerns about an impending conflict.
- Mae Jonghak may become Alliance Leader of the revived Murim Alliance; this remains unresolved.

## Translation Decisions

- Use **Black Stone Mountain**, **Black Stone Stronghold**, **Eighteen Strongholds**, **Heavenly Axe**, **Bangyeol**, **Thousand-Year Snow Ginseng**, and **Crisis of the Yongbong Escort Bureau**.
- Use **Defeat Heavenly Axe**, **Subdue Black Stone Stronghold**, and **Find Mr. Shin in Sichuan** for the established Quest titles.
- Use **Huashan Divine Dragon**, **Huashan’s Lone Crane**, **Zhongnan One Dragon**, and **Heavenly River Thirty-Six Swords**.
- Use **Xi’an Tower**, **Huashan–Zhongnan gathering**, and **Fire Gate Clan**.
- Render **일인전승 비인부전** as **one-person transmission and refusal to teach the unworthy**, and **육체파** as **physical school**.

## Durable state

{
  "active_continuity": [
    "The Jin Family Escort Bureau and the Yongbong Escort Bureau are business competitors; the Yongbong Escort Bureau remains dominant in Shaanxi, while the Jin Family Escort Bureau reportedly has more than five branches.",
    "Ju Hwaran suspects an internal Yongbong Escort Bureau betrayal involving the leak of the Thousand-Year Snow Ginseng information and the attacks sustained over four months.",
    "Ju Hwaran told Heo Jun to watch Song Ilseom; Taekyung and Cheongpung also noticed Song Ilseom's hostile attention toward Taekyung.",
    "Song Ilseom is a Level 110 escort captain of the Yongbong Escort Bureau.",
    "Cheongpung is known by the title Huashan Divine Dragon, bestowed after the Star-Array Grand Banquet.",
    "Taekyung, Cheongpung, and Gung Gibang are traveling toward Sichuan to find the Divine Physician and have reached Xi'an after nearly seven days of forced travel.",
    "Baek Museong is the direct Disciple of Heavenly Sword True Person, the first of Huashan's Three Plum Blossom Elites, and widely expected to become Huashan's future Sect Leader.",
    "Hyuk Sopyung is a Peak master of the Zhongnan Sect and the Zhongnan One Dragon; at Xi'an Tower, Taekyung defeated his seven-tenths Heavenly River Thirty-Six Swords and forced him to withdraw.",
    "Cheongpung apologized to Baek Museong for beating Baek and the Three Plum Blossom Elites while escaping forced escort back to Huashan a year earlier."
  ],
  "continuity_sources": [
    313,
    314
  ],
  "open_questions": [
    "Is Song Ilseom involved in the Yongbong Escort Bureau's information leak and the repeated attacks?",
    "Will Mae Jonghak become Alliance Leader of the revived Murim Alliance?"
  ],
  "safe_through": 314,
  "temporary_decisions": [
    "Use Huashan Divine Dragon for 화산신룡.",
    "Use Xi'an Tower for 서안루.",
    "Use Hyuk Sopyung for 혁소평.",
    "Use Zhongnan One Dragon for 종남일룡.",
    "Use Huashan–Zhongnan gathering for 화종지회.",
    "Use one-person transmission and refusal to teach the unworthy for 일인전승 비인부전.",
    "Use physical school for 육체파."
  ],
  "version": 1
}

## Reading copies

## Chapter artifact 310

# Chapter 310

*Rustle, rustle, rustle.*

The number of bandits who emerged behind Heavenly Axe came to five hundred.

But Ju Hwaran’s face had not hardened because of their overwhelming numbers alone.

*Their momentum is different.*

Those trying to cross the mountain and those blocking their way. Escort Bureaus and the Green Forest were inseparable.

The Escort Bureau side could not draw their swords every time, so they paid a set amount as a toll. The Green Forest, in turn, withdrew after taking a reasonable sum, allowing both sides to save face. That had long been the established custom.

But neither Heavenly Axe nor the bandits of Black Stone Stronghold showed any intention of backing down.

“You’re planning to see blood after all…”

At Ju Hwaran’s words, Heavenly Axe curled up the corners of his mouth.

“You’ve got some sense for a little bitch. That’s right. I intend to stain Black Stone Mountain with blood today.”

“Little bitch?”

“What? If you don’t like that, should I call you an old bitch?”

“I am the Young Bureau Head of the Yongbong Escort Bureau. Show me the same courtesy I’m showing you.”

Ju Hwaran’s beautiful eyebrows, as delicate as if they had been drawn with a brush, shot upward.

She was the bureau chief’s only child, but that did not mean she had been raised pampered and sheltered.

From childhood, she had swung a sword until her palms grew callused. She had eaten and slept on the road alongside the escorts, learning from everything she saw.

People fawned over Ju Hwaran as one of the Three Flowers of Jiangbei, but she was no hothouse flower.

“What a brazen little bitch. And what will you do if I refuse?”

“Then…”

Ju Hwaran, the Dagger Hidden Flower—a flower hiding a dagger—continued in a chilly voice.

“You should die. At the hands of a little girl.”

“What? Huh… Hahaha!”

It took a while for Heavenly Axe’s wild laughter to stop.

“You’ve got more backbone than I expected. I like you.”

“I wouldn’t be happy even if some old bandit liked me.”

“You’ve got a sharp tongue. Aren’t you worried about what comes next?”

“Why are you doing this in the first place?”

“Why? A bandit says he intends to kill and rob you. Does he need some special reason?”

At Heavenly Axe’s brazen reply, Ju Hwaran bit down hard on her lip.

“If word of this gets out, the Green Forest Alliance will be put in a difficult position too.”

“Put in a difficult position?”

“Our Yongbong Escort Bureau is also part of the orthodox faction. The orthodox Murim won’t stand by and do nothing.”

“Part of the orthodox faction, is it? Then I suppose it would be a problem.”

Heavenly Axe stroked his shaggy beard and continued.

“So I’ll do my best to make sure it doesn’t get out. Every secret is harmless as long as it doesn’t leak, wouldn’t you agree?”

“…”

*Silencing the witnesses.*

Realizing what Heavenly Axe meant, Ju Hwaran gripped her sword hilt tightly. Chief Escort Heo Jun stepped forward in her place and shouted.

“One hundred silver nyang! Clear the road, and I’ll give you one hundred silver nyang. We’ll consider today’s matter closed, so stop this here!”

“Oh? One hundred nyang? Silver nyang, at that?”

“Of course. Have I ever made an empty promise?”

“No, you haven’t. We’ve met more than once, after all. Brother Heo is trustworthy enough.”

Chief Escort Heo Jun had devoted nearly thirty years to the Yongbong Escort Bureau.

The Yongbong Escort Bureau was a large Escort Bureau based in Shaanxi. He had completed hundreds of escort journeys, large and small, and crossed Black Stone Mountain so often that he had become acquainted with the Green Forest stronghold leaders—including Heavenly Axe, who had become a stronghold leader five years earlier.

“That’s five times the usual toll. Stop this nasty prank and clear the road.”

“A nasty prank? Is that how it looked?”

Heavenly Axe let out a hearty laugh. Then a sudden chill entered his face.

“There’s a limit to treating me like an idiot. Brother Heo, you need to pay the proper price.”

“P-Pay the proper price?”

“Even the dogs we raise in our stronghold know that the goods you’re transporting include a thousand-year snow ginseng. If we sold it as stolen goods right now, we could easily get several thousand silver nyang for it. Isn’t that right?”

“…”

At that moment, the eyelids of several people, including Ju Hwaran and Heo Jun, began to tremble.

A thousand-year snow ginseng was an elixir that could grant a full jiazi of internal energy if completely digested.

The existence of the thousand-year snow ginseng, which had been secretly commissioned by the Zhongnan Sect, was a top-level secret known by only a handful of people within the Yongbong Escort Bureau.

So how had word reached Heavenly Axe?

*It wasn’t a coincidence.*

The past four months of escort journeys flashed through Ju Hwaran’s mind.

Bandits and nameless wandering martial artists who had attacked them as if they had encountered their mortal enemies.

The reason they had endured dozens of battles, large and small, and suffered heavy losses was that information about the thousand-year snow ginseng had leaked.

*Who could it have been?*

She had suspected someone. But she had forced those suspicions down.

The driving force that had allowed her to endure the misfortunes that had piled up over the past two years had been the people around her.

The greatest inheritance her grandfather had passed down to her father, and her father to her.

Even as the Yongbong Escort Bureau lost its former glory and gradually declined, they had not left. They had continued to show her unstinting trust and support despite her repeated failures.

That made her all the more unwilling to suspect them. She did not want to doubt them.

*But now…*

Ju Hwaran swept her surroundings with an empty gaze.

Chief Escort Heo Jun stood frozen, feeling as betrayed as she did. And then she saw the three people who knew about the thousand-year snow ginseng.

They were the three outstanding escort captains who represented the Yongbong Escort Bureau—the men known collectively as the Dragon-Phoenix Three Escorts.

*Seokchil. Noh Piljung.*

Ju Hwaran’s gaze passed over the two middle-aged escorts, both nearing forty, and turned to the last man.

*Song Ilseom.*

Unlike the other two members of the Dragon-Phoenix Three Escorts, Song Ilseom was tall and strikingly handsome.

Barely past thirty, he had entered the Yongbong Escort Bureau as an escort ten years earlier and risen rapidly through the ranks.

He sometimes revealed his rough temper, but his outstanding martial arts had allowed him to lead escort journeys to success. That was why, despite his young age, he had been named one of the Dragon-Phoenix Three Escorts.

But Song Il was followed by a great deal of gossip.

> “They say he used to be a wandering martial artist. A fixer, too.”

> “Apparently, as long as he got paid, there was nothing he wouldn’t do.”

> “Is that all? There are widespread rumors that he’s deeply in love with the Young Lady. Mihyang told me last time—apparently, whenever he gets the chance, he goes into the inner courtyard and wanders around the garden.”

> “I heard he joined the Escort Bureau because of the Young Lady… Though everyone knows the Chief wanted an escort for a son-in-law, right?”

Ju Hwaran knew about the public rumors surrounding Song Il.

She also knew that most of what people said was true.

There had been times when Song Il’s blatant gaze made her uncomfortable. For that reason, she had genuinely agonized over whether to use him on this escort journey.

*But surely Escort Captain Song Ilseom wouldn’t…*

The moment Ju Hwaran’s gaze lingered on Song Il’s face, his thick, fierce-looking eyebrows shot upward.

*Flash—whoosh!*

“Hwaran!”

Three things happened simultaneously.

A dagger shot out from Song Il’s sleeve.

At the same time, Chief Escort Heo Jun hurriedly stepped in front of Ju Hwaran.

And finally—

*Thud!*

“Ghk… Grrrk.”

More than twenty jang away, a Black Stone Stronghold bandit with a dagger lodged in his throat collapsed.

The bandit spewed bloody foam and convulsed before drawing his last breath.

“…”

A cold silence settled over the scene. After a silence that seemed as if it would never end, Song Il broke it with a single shout.

“No more talking! Fight like you’re prepared to die!”

His fierce cry spread into the distance on the night wind, and Ju Hwaran, Heo Jun, and everyone from the Yongbong Escort Bureau realized it.

The negotiations had already fallen through.

They would have to engage in a battle to the death against hundreds of enemies who had been struck by an unexpected opening attack.

“Song Il! What are you doing?”

At Chief Escort Heo Jun’s furious shout, Song Il raised his willow-leaf saber and rested it across his shoulder.

“What do you think I’m doing? It’s too late to ask that now, isn’t it?”

“You bastard…”

“He’s right.”

Ju Hwaran said calmly as she gripped her sword hilt.

Unfortunately, Song Il was telling the truth.

Heavenly Axe was approaching them, radiating a terrifying aura.

He had lost one of his men without having time to do anything. Flames poured from his bulging eyes.

“I’ll slaughter every last one of you.”

*Hissssss!*

Red qi writhed from the lowered blade of his enormous axe.

The Green Forest Alliance contained countless people, but Heavenly Axe was a Peak master ranked among its top twenty.

Fueled by their leader’s aura, the five hundred Green Forest bandits also growled like wild animals.

“Kill them all!”

“This is where you’ll be buried!”

As she listened to their enraged cries, Ju Hwaran looked up at the star-filled night sky.

*This might be my last escort journey.*

Of the more than seventy people who remained, only around forty were escorts, excluding the caravan porters.

Everyone was exhausted from the long escort journey. The conditions were far too harsh for them to face Heavenly Axe and five hundred Green Forest bandits.

*Can I do this?*

*Thud, thud, thud.*

The ground trembled beneath hundreds of footsteps. A battle they could neither avoid nor escape was about to begin.

*All that remains is to fight until the very end.*

She had to send even one person away alive.

Just as Ju Hwaran was about to face forward again, she noticed a star she had never seen before.

Among the countless stars embroidered across the pitch-black sky, one shone unusually brightly. It scattered its radiance for a very brief moment, then vanished.

And then, the next moment, something no one could have expected happened.

“Don’t fight, everyone! No matter how badly you get along, something terrible will happen if you fight!”

At the sudden shout, everyone’s movements stopped dead. Hundreds of heads whipped toward the direction of the voice.

The world was sunk in darkness.

Four figures stood tall on a hill, illuminated by the faint moonlight.

Soon, quiet voices drifted down.

“What are they?”

“They look like bandits. One side looks like people from an Escort Bureau.”

“No, anyone can see they’re bandits. Why are they fighting here in the middle of the night? We’re so busy we could drop dead.”

“They look busier than we do.”

“Mujin, has it been long since you were hit?”

“No. I was hit about half an hour ago.”

*Smack!*

“Gibang, do you know who those people are?”

“Of course.”

“Help me, Speed Beggar.”

“Judging by the flag, they’re from the Yongbong Escort Bureau. The other side is Black Stone Stronghold, led by Heavenly Axe.”

“I’ve never heard of either of them. Strangely, though, Heavenly Axe sounds familiar.”

“The Yongbong Escort Bureau was once counted among the Ten Great Escort Bureaus of the martial world, and Heavenly Axe is a Peak master ranked among the Green Forest Alliance’s top twenty. He wields a single axe like a demon…”

“No, wait. Surely you mean that Heavenly Axe?”

“You know Heavenly Axe?”

“I definitely killed him… Did he take the reincarnation bus or something? Wait here. I’ll go take a look at his face.”

“Benefactor! What’s a reincarnation bus?”

“Try crossing a crosswalk when you’re bored.”

The utterly incomprehensible conversation ended there.

Then a large shadow came trudging down the hill.

Only after it drew closer, one step at a time, could the people make out what the shadow actually was.

*What is that?*

*He’s young as can be. And what’s that pack frame on his back?*

It was a truly bizarre sight.

Hundreds of people facing one another in the darkness, weapons in hand.

And a young man carrying a pack frame, walking beneath the moonlight as if he were out for a stroll.

*Clomp, clomp. Stop.*

“Sorry to bother you while you’re busy.”

At last, the young man stopped and slowly turned his head.

He frowned as he looked at the grimy bandits. When his gaze reached Ju Hwaran, he suddenly squirmed. Finally, he gave Heavenly Axe a quick once-over from head to toe before casually tossing out a single remark.

“This isn’t the bastard.”

“…”

“…”

At the bombshell, hundreds of pairs of eyes widened.

He had called Heavenly Axe—a Peak master counted among the Green Forest Alliance’s foremost experts—a bastard.

Just as everyone began to doubt their own ears, the second bomb dropped.

“Oh, you’re that guy. The real Heavenly Axe. No wonder I thought something was weird. But you don’t look all that impressive either. Not as impressive as the rumors made you sound.”

Heavenly Axe finally came to his senses, and fire shot from his eyes.

“Y-You lunatic!”

The next moment, the axe in his hand crashed down toward the young man’s crown.

*Whooosh—crash!*

Condensed qi collided.

A flexible sword stopped the axe blade, which shimmered with red qi.

Ju Hwaran’s wrist trembled as she desperately blocked the attack.

She, too, was a Peak-level swordswoman. But she was far too lacking to withstand Heavenly Axe, who possessed both natural strength and years of experience.

“Ghk! Young Hero, hurry and run—!”

“You little bitch, how dare you!”

*Clang-clang-clang!*

The two blades locked together, sending sparks flying.

The enormous axe slowly pressed downward.

Just as Heo Jun and Song Il charged forward to help Ju Hwaran, the lips of the young man standing as still as stone parted.

“Say one thing for me.”

“…Yes?”

“Help me. Just those words.”

*Is he out of his mind?*

That was the thought that flashed through Ju Hwaran’s mind.

The young man had not even been able to react to Heavenly Axe’s attack. If she had not blocked it with her flexible sword, he would have been cut in half and killed without a chance.

But despite what she was thinking, her mouth was already speaking.

“Help me!”

And then she saw it.

The faint smile forming at the corner of the young man’s mouth.

A voice so quiet that only she could hear it flowed into her ear.

“Quest accepted.”

*Whoosh!*

A wave of heat suddenly swept over them.

Ju Hwaran felt an endlessly warm sensation.
## Chapter artifact 311

# Chapter 311

“Quest accepted.”

*Ding.*

> **System**
> - You have accepted the Sudden Quest **Crisis of the Yongbong Escort Bureau**!

*You’ve really grown up, Jin Taekyung. Now you can even create Quests on your own.*

I smiled proudly and stretched out my right hand. My palm, heated red by the Flame Divine Palm, struck the side of the axe at a terrifying speed.

*Boom!*

With a deafening crash, Heavenly Axe’s massive body slid backward. After staggering back three jang, his face twisted with confusion and fury.

“W-What is the meaning of this…?”

“What do you think? You picked the wrong person.”

I grinned and looked Heavenly Axe up and down.

This was not the fake Level 10 Heavenly Axe I had encountered long ago. This was the real Heavenly Axe, an actual Level 90.

*Wow. The real thing really is different.*

He was much larger, his face so vicious-looking that it would have been a crime for him not to be a bandit, and his martial arts were on an entirely different level.

Looking at him brought old memories bubbling back to the surface.

*I gained quite a bit of Fame when the false rumor that I’d taken him down spread back then.*

That had been the period when my name began to be reevaluated within the Jin Family of Taiyuan.

Because people had mistaken the fake Heavenly Axe for the real one and spread the rumor, I had gradually managed to shed some of the stigma of being the family’s disgrace.

*Damn, it feels like it was only yesterday.*

Heavenly Axe glared at me warily as I sank into nostalgia.

“Who… the hell are you?”

“Me? The man who’s going to kill you twice.”

“W-What did you say?”

“It’s a long story.”

“Kill me twice? What kind of bullshit is that…? Wait. Could it be…?”

Heavenly Axe’s voice, which had been about to continue, abruptly cut off.

He stared at me with a rigid face. Then a thunderous cry burst from his lips.

“The Sleeping Dragon of Shanxi!”

“Huh? You know me?”

“I heard a rumor like that about a year ago… No, that’s not the point.”

Heavenly Axe opened his mouth with a stammering voice. At some point, even the way he addressed me had naturally changed.

“A-Are you really Young Hero Jin Taekyung of the Jin Family of Taiyuan?”

“I’m not a Young Hero. But I am Jin Taekyung.”

When I nodded readily, startled gasps escaped from all around us.

Bandits and escorts alike stared at me in shock. The gaze I felt from beside me was especially sharp.

> **System**
> **Level 88: Ju Hwaran**

Soon, her smooth lips parted slightly, and a clear voice flowed out.

“You’re… the Sleeping Dragon of Shanxi?”

“Hmm. That’s what people call me.”

The woman who had been looking up at me with her large, wide-open black eyes suddenly performed a formal fist-and-palm salute.

“I am Ju Hwaran, the Young Bureau Head of the Yongbong Escort Bureau. It is an honor to meet Young Hero Jin.”

“Ah, yes. Nice to meet you.”

*I guess I’m more famous than I thought.*

I had never expected to run into hundreds of people who knew me on a mountain road in the dead of night, thousands of li from Shanxi Province.

And I certainly had not expected the most beautiful woman I had ever seen in my twenty-eight years of life to be the one who recognized me first.

*Come to think of it, a person can really look like this?*

There was no way to properly describe Ju Hwaran’s beauty with simple words like *pretty* or *beautiful*.

I was still staring at her, cursing my inadequate vocabulary, when—

“Ahem. Come to think of it, don’t we have repairs to do at the stronghold today?”

“Y-You’re right, Chief. I completely forgot.”

Hundreds of people began cautiously retreating amid awkward coughs.

When I turned my head, I saw Heavenly Axe and the Green Forest bandits of Black Stone Stronghold slowly backing away.

I waved at Heavenly Axe.

“Hey, Axe.”

His body stiffened.

“…Axe?”

“Yeah. Our Axe. Where are you going?”

His expression was a sight to behold. It twisted, then smoothed out, then twisted again.

His face became a ridiculous mixture of rising fury and barely restrained patience. With great difficulty, Heavenly Axe squeezed out a reply.

“I have some business to attend to at the stronghold, so I should be going.”

“Exactly. Why are you leaving without permission?”

“…”

A chilly silence settled over the clearing. The hand gripping Heavenly Axe’s weapon turned white, but that was as far as it went.

There had been only one exchange.

But Heavenly Axe—and everyone else present—must have realized it. I was a master on a higher level than him.

Of course, that was not the only source of the fear that made Heavenly Axe hesitate.

“W-Where is the Fire King?”

*Where is he? Sleeping soundly on the pack frame strapped to my back, of course.*

To prepare for any unforeseen circumstances, I had covered him with layers of fur. No one could imagine that the terrifying Fire King was lying unconscious on the pack frame.

*Besides, no one can find out that Old Master has collapsed.*

If that happened, all kinds of vermin, including Dark Heaven, would come crawling out of the woodwork.

I concealed my thoughts and let out a quiet laugh.

“Why do you ask about my Master?”

“I only asked because I wanted to see him once.”

“Why? Are you close to my Master?”

“Well, he is someone I’ve always respected…”

“If you ever happen to meet him, don’t say that. He’ll be offended if a bandit bastard like you pretends to be close to him. You’ll start by losing three or four ribs.”

“…Your joke is in poor taste.”

“Does it sound like a joke?”

Heavenly Axe bit down hard on his lip and rolled his eyes.

His gaze swept rapidly over me, Ju Hwaran, the other members of the Yongbong Escort Bureau, and finally the faces of the Bermuda Triangle slowly descending the hill. Then his eyes returned to me.

“Then he isn’t here?”

“What if he isn’t?”

“If that’s the case…”

*Swish. Clunk.*

Heavenly Axe raised his axe and rested it on his shoulder.

“Then things will be very different.”

“Like your way of speaking just now?”

“It was difficult humoring a young punk.”

“That’s strange. It doesn’t look like anything would change whether my Master was here or not.”

“That’s because you’re a greenhorn who knows nothing about the ways of the world.”

“In what way?”

“I admit that your martial arts are more impressive than I expected. But it would be a mistake to consider yourself equal to your Master.”

Heavenly Axe raised one hand, a sneer spreading across his face.

At the same time, more than five hundred Green Forest bandits raised their weapons and stepped forward.

The mere fact that the Fire King was not present seemed to have restored their confidence.

“The Fire King, Jeok Cheongang, is undoubtedly a master beyond the human realm. But can you really turn the tide of this battle all by yourself?”

“Hmm.”

I looked around.

There were only a little more than seventy people from the Yongbong Escort Bureau.

Half of them were caravan porters who did not know even a single move of martial arts, and even the escorts who would have to fight looked utterly exhausted.

By contrast, Heavenly Axe commanded nearly five hundred Green Forest bandits.

With more than ten times our numbers, it was certainly a situation in which Heavenly Axe could afford to act confidently.

But…

“I might as well turn it around while I have the chance.”

“Hahaha! Go ahead and try.”

“That’s the plan.”

The smile around Heavenly Axe’s mouth vanished in the next moment.

I had crossed the five-jang distance in a single step and thrown a punch.

*Flame-Extinguishing Divine Fist.*

*Vroooom.*

Compressed air exploded outward. The wind split apart, and a wave of Extreme Yang heat surged forward.

The strike that had once brought down an unnamed cliff on Mount Song shot toward the five hundred Green Forest bandits massed together like an army of ants.

Heavenly Axe stood at the front.

*Baaaaang!*

With a roar that seemed to split the sky, clouds of dust and steam billowed upward.

*Ding. Ding. Ding.*

System notifications continued boring into my ears without pause.

These bandits were at a Level where killing them did not even grant EXP. I had neither the need nor any reason to use my spear.

I simply unleashed my martial arts indiscriminately at the enemies beyond the chaotic fog.

*Baaaaang!*

I tore, struck, and smashed everything in my path.

Blood and screams overflowed across the ground, which heaved as though it had been struck by an artillery barrage.

“Gaaaaah!”

“Kill him!”

“He’s over there!”

*Whoooosh! Thud!*

Dozens of blades arrived belatedly, burying themselves in the innocent ground.

Every one of them moved sluggishly. I could see the exact trajectories their weapons would follow.

*This is easy. Almost bizarrely easy.*

*Crack!*

My movements, by contrast, were precise and carried tremendous destructive power. Every time I continued forward without hesitation, three or four screams rang out.

The panicked bandits could no longer distinguish friend from foe. They simply swung the weapons in their hands like madmen.

*Shhk! Slash!*

“Gaaah! You crazy bastard!”

“W-Wangpal?”

“Yeah, it’s me! It’s me, you bastard!”

“Sorry. I thought you were him…”

I whispered into the flustered bandit’s ear.

“This time, it really is me.”

“…”

*Crunch!*

With exactly as much force and speed as necessary, I seized his neck and twisted.

His body crumpled without even managing to scream.

Before it could touch the ground, I was already moving again.

*Flamefire Path.*

The Fire Gate Clan’s signature cultivation technique.

I kicked off the ground and surged forward. A tail of fire pierced the fog.

For an instant, the surroundings lit up brightly, revealing a giant man eight cheok tall.

Two gazes collided in midair.

“There you are.”

“Jin Taekyung, you bastard…”

*Grind.*

Heavenly Axe ground his teeth as I stepped toward him.

I unleashed the Flame Divine Palm with all my internal energy behind it.

Red qi streamed from the enormous axe Heavenly Axe brought down with the momentum of splitting a person in two.

A roar like a lion’s roar burst from his mouth.

“Die!”

*Whoooosh! Boom!*

An immense wave of energy whirled outward at the moment of impact.

We were so close that I could feel his breath against my cheek. My coldly hardened face was reflected in Heavenly Axe’s bulging eyes.

So was the broken axe—and my hand, which had pierced through the weapon and his chest before protruding from his back.

*Fwoosh!*

“Ghk…!”

Blood did not gush out like a waterfall.

The heat of the Flame Divine Palm in my hand had already vaporized the liquid.

Heavenly Axe’s lips, cracked like a drought-stricken field, moved weakly.

“Y-You… just what…”

“Why? You told me to turn things around.”

*Shhk.*

With those words, I pulled my hand from his chest.

His entire body had been burned and melted after he failed to block the opening strike of the Flame-Extinguishing Divine Fist.

Heavenly Axe looked down at his chest, which had been charred black, and muttered in a halting voice.

“This… is impossible…”

Those unfinished words became Heavenly Axe’s last.

*Thud.*

As his eight-cheok body collapsed, a System notification rang out.

> **System**
> - You have defeated **Level 93 Bangyeol**!
> - You have completed **Defeat Heavenly Axe**!
> - You have gained a substantial amount of EXP!

*Whoooosh.*

Just then, a gust of wind blew from somewhere, swept around Black Stone Mountain, and descended into the clearing.

As the pale fog scattered, the scene beneath it was revealed, and everyone’s eyes widened.

“This can’t be!”

The twentieth-ranked member of the Green Forest Alliance.

The end of Bangyeol, Heavenly Axe—a Peak master counted among the foremost of the countless Green Forest bandits scattered across the continent.

The corpses of more than a hundred bandits who had died in the melee lay scattered throughout the clearing.

The four hundred surviving bandits stared at me with fear-filled eyes.

No. Everyone who had witnessed the scene cried out.

“The Fire King…!”

The Fire King, Jeok Cheongang.

Fifty years ago, in an unnamed wilderness, he had annihilated one thousand Demonic Cultists—a martial artist who could stand against a thousand men alone.

The legend of the Fire Gate Clan had been proven by the Fire King’s myth.

And that spark had now passed to me.

“Choose. Die here, or…”

My entire body was burning hot. Extreme Yang heat flowed between my teeth, sending white steam billowing from my mouth.

I stared at my enemies with flame burning in my eyes.

“Kneel. Every last one of you.”

*Clang.*

Beginning with a single sword someone dropped helplessly, more than four hundred weapons rolled across the ground.

> **System**
> - You have completed **Subdue Black Stone Stronghold**!
> - You have successfully completed the Quest **Crisis of the Yongbong Escort Bureau**!
> - You have gained a substantial amount of EXP!
> - **Level Up!**

The light chime announced the end of the battle.
## Chapter artifact 312

# Chapter 312

After the bandits of Black Stone Stronghold surrendered, the first person to collect herself was Ju Hwaran, the Young Bureau Head.

She looked at me with indescribable emotion in her eyes before performing a deep fist-and-palm salute.

“Thank you for the immense favor you’ve done us.”

“It was nothing. I happened to be passing by, so I took care of it while I was at it.”

I meant it. I had been passing through anyway, and it hadn’t taken much time, so the Levels I gained were more than enough compensation.

From Ju Hwaran’s perspective, though, I must have been a lifeline.

“If not for Young Hero Jin’s help, the Yongbong Escort Bureau would have been buried here. I had heard plenty about the Sleeping Dragon of Shanxi, but it seems the stories about you being a hero who cannot stand by in the face of injustice were true.”

“A hero? Hardly. It’s just a rumor people spread because it sounds good.”

“Pardon?”

“I can ignore injustice sometimes. I only occasionally get rid of people who annoy me. The problem is, the people who annoy me always seem to be scumbags—like that Heavenly Axe bastard.”

I glanced toward Heavenly Axe’s corpse as a caravan porter dragged it away, then continued.

“And my family runs an Escort Bureau too.”

“Ah, the Jin Family Escort Bureau.”

The Seongun Escort Bureau, once run by the Woo family, had changed its sign to the Jin Family Escort Bureau and was thriving. I had heard it already had more than five branches.

Shaanxi and Shanxi shared a border, so the Jin Family Escort Bureau and the Yongbong Escort Bureau would probably cross paths someday.

“You know about the Jin Family Escort Bureau. If you ever run into them, please treat them well. We should help each other out in the spirit of fellow business owners, just like today.”

“The spirit of fellow business owners?”

“Is there a problem?”

“You do know that the Jin Family Escort Bureau and the Yongbong Escort Bureau are competitors, right?”

*Huh? We were competitors?*

I blinked and asked again.

“Is that true?”

“You really didn’t know?”

“No. I barely pay attention to family matters.”

“If you hadn’t saved us today, the Jin Family Escort Bureau might have expanded into Shaanxi Province. It may not look that way right now, but we still dominate Shaanxi.”

“I see.”

“This line of work is more cutthroat than it looks. There are plenty of invisible power struggles, and armed conflicts break out from time to time too.”

“Well, what does it matter if we can’t expand? I’ll tell my eldest brother we should get along.”

Ju Hwaran stared at me with a strange expression before letting out a quiet laugh.

“I’d appreciate that.”

*Wow. I almost let out an actual gasp.*

She had only laughed. So why was it that beautiful?

I swallowed the exclamation that was about to escape when murmuring voices reached me from behind.

“My word. That’s the first woman I’ve seen who’s more beautiful than Young Lady Lee Seowol.”

“Dagger Hidden Flower Ju Hwaran is one of the Three Flowers of Jiangbei. I don’t know who Lee Seowol is, but how dare she compare herself to her?”

“As if she could. Young Hero Gung, go rub yourself against a rock in the stream and wash up. That grime is so filthy it makes me sick.”

“What’s wrong with me?”

“You’re a beggar, aren’t you?”

“Hah. That’s true, I suppose.”

An innocent voice followed.

“That’s not true. Young Lady Lee Seowol is pretty too.”

“What’s gotten into Young Hero Cheongpung? I didn’t know you could say things like that.”

“And Young Hero Gung is pretty too, in my eyes.”

“……Then go down to the stream and wash up with pretty Young Hero Gung. Especially your eyes.”

There was no question about it. They were the Bermuda Triangle.

Normally, I would have at least introduced them, but the level of their conversation was so low that I was embarrassed to say anything myself.

I was forcing out an awkward cough when Ju Hwaran poked her head out over my shoulder.

“Who are those people?”

“I don’t know.”

“You came here together.”

“They’re traveling companions.”

“Really?”

“I swear it on the heavens.”

I had lowered my voice as much as I could, but the Bermuda Triangle had inevitably heard me. Their outrage rose like wildfire.

“Captain! Are you ashamed of us?”

“Am I embarrassing?”

“Benefactor! I’m fine! Please be ashamed of me!”

“……They’re actually my friends.”

“Anyone can see that.”

*Anyone can see that? That was somehow even more devastating.*

Ju Hwaran gave a small laugh at my expression and performed a fist-and-palm salute toward the three of them.

“Ju Hwaran, Young Bureau Head of the Yongbong Escort Bureau, pays her respects to the Benefactors.”

I wasn’t sure what those three had done to deserve being called Benefactors, but the Bermuda Triangle bowed their heads anyway.

“I am Hyuk Mujin, one of the great Jin Family of Taiyuan’s foremost elites, Vice Squad Leader of the Jin Dragon Squad, and the right-hand man of the Sleeping Dragon of Shanxi.”

I calmly corrected him.

“Not the Vice Squad Leader. The acting Vice Squad Leader. And not my right hand. He’s more like the pinky of my left hand.”

Gung Gibang spoke next.

“I am the beggar Gung Gibang.”

“He’s the next-generation beggar boss.”

Finally, it was Cheongpung’s turn.

“Hello! You’re pretty!”

“As you can see, he’s a little unwell. He’s not the sharpest, but he’s a good friend.”

After hearing the storm of introductions and my kind explanations, Ju Hwaran’s lips parted slightly.

Her large black eyes trembled visibly.

“So, let me get this straight…… The pinky of your left hand, the next-generation beggar boss, and the slightly dim but kind friend?”

“Yes, exactly.”

“I’ve never heard an explanation like that before.”

“Would you like me to repeat it?”

“No, thank you.”

She let out a deep sigh, then looked at each of them in turn.

“I’ve heard of the Swift Wind Sword, who rendered distinguished service during the suppression of the mounted bandits in the north.”

“……Huh?”

Hyuk Mujin stared at Ju Hwaran with a bewildered expression.

*Swift Wind Sword?*

I had no idea when he had acquired such a sobriquet, but judging by his reaction, it seemed to be genuine.

Before anyone could say anything, Ju Hwaran continued.

“And the person beside him is Young Hero Gung Gibang, the Successor Beggar and Disciple of Great Hero Myriad-Mile Pursuit, the Beggars’ Sect Leader.”

“P-Pleased to meet you.”

“Lastly, it is an honor to meet Young Hero Cheongpung, the Huashan Divine Dragon. My grandfather and father have always referred to Great Hero Mae Jonghak, the Sword Saint, as a hero of benevolence and righteousness.”

The title Huashan Divine Dragon had been given to Cheongpung after the Star-Array Grand Banquet.

Cheongpung’s eyes opened wide in surprise.

“Wow! How do you know all that?”

Ju Hwaran smiled brightly.

“Because I’m the Young Bureau Head of the Yongbong Escort Bureau.”

It was a short answer, but it carried a great deal of meaning.

We had left Henan only a few days after the Star-Array Grand Banquet ended.

*She gathers information quickly.*

Unlike Cheongpung and Gung Gibang, Hyuk Mujin was merely a newcomer who had operated only in Shanxi Province.

The fact that she knew both his name and his sobriquet so precisely meant that Ju Hwaran was even more meticulous and clever than I had expected.

*Dagger Hidden Flower. A flower hiding a dagger.*

The dagger she concealed was not merely one.

She possessed Peak-level martial arts, a sharp mind, and beautiful features capable of captivating people.

She more than deserved her place among the Ten Dragons and Phoenixes, said to be the greatest young prodigies in the martial world.

*Interesting. At this rate, she must be good at running an Escort Bureau too.*

According to what I had heard from Gung Gibang, the Yongbong Escort Bureau’s past two years had been one hardship after another.

I brushed the question from my mind.

*Eh, what difference does it make if I worry about it?*

Finding the Divine Physician was more urgent right now.

We had already lost nearly a shichen here. If we wanted to reach our destination before dawn, we needed to get moving.

“Young Lady Ju, I think we should be going now.”

Ju Hwaran flinched at my sudden words.

“Now?”

“I have something urgent to take care of.”

“It’s already quite late. Why don’t you stay here for the night and leave in the morning……?”

“That might be difficult…… We need to reach Xi’an by tomorrow.”

“Ah.”

Ju Hwaran hesitated as if she had something to say, then finally opened her mouth.

“Will I be able to see you again?”

“Of course. If fate brings us together.”

I was about to bow and turn away when Ju Hwaran’s voice followed me.

“I will never forget that you saved our lives.”

“I don’t know about that. Even if it hadn’t been me, you would have avoided the worst-case scenario, so you don’t have to be that grateful.”

“What?”

“Of course, you would have suffered some losses.”

*She still doesn’t know?*

Well, it was understandable.

I smiled at the bewildered Ju Hwaran. Then I glanced at the young escort with the fierce eyes before turning away.

> **System**
> **Level 110: Song Ilseom**

*The Murim really is a vast place. Someone with that level of skill is working as an escort?*

He was the owner of the gaze I had felt ever since we arrived.

Thanks to him, the back of my head had prickled the entire time I was speaking with Ju Hwaran.

*But why has that bastard been glaring at me like that? Did I somehow become his sworn enemy?*

Apparently, I wasn’t the only one who had noticed his hostile gaze. Cheongpung followed closely behind me and whispered.

“Benefactor, did you feel it too?”

“Yeah. I don’t know why he’s acting like that, but he’s being incredibly obvious.”

“Right? Maybe he’s interested in Benefactor.”

“……”

*Please stop talking bullshit.*

* * *

The four figures shot away like the wind. As Ju Hwaran watched their backs recede, someone approached her.

“Hwaran.”

“Ah, Uncle Heo.”

Heo Jun had finished binding the bandits and dealing with the aftermath. He followed Ju Hwaran’s gaze and turned his head.

“Jin Taekyung, the Sleeping Dragon of Shanxi. He truly is an extraordinary young man. The others are no different.”

“I know. They say the rumors of the martial world aren’t worth believing…… but in this case, they seem to have understated things.”

Ju Hwaran recalled the martial prowess Jin Taekyung had displayed.

It had been an overwhelming sight. She had thrilled at the spectacle, but at the same time, she had felt bitter.

*If only I had strength like that.*

If she had, the Yongbong Escort Bureau would never have ended up in its current state.

Ju Hwaran swallowed the words hovering at the tip of her tongue and suddenly opened her mouth. The words she sent carried her internal energy in Sound Transmission.

—Uncle Heo. Keep an eye on Escort Captain Song.

Heo Jun was seasoned enough to be the Chief Escort. Without revealing anything on his face, he brought up another subject and replied through Sound Transmission.

—Hwaran. Are you saying that…?

—It’s only a suspicion for now. But there are more than one or two things that bother me.

The leak of confidential information about the Thousand-Year Snow Ginseng. The attacks that had continued without pause for the past four months.

Ju Hwaran intended to cut out the roots of the betrayal that had grown deep within the bureau.

*Especially the last thing Young Hero Jin said.*

He had said that the worst-case scenario would not have occurred even if he had not been there.

That meant there was a master within the Yongbong Escort Bureau capable of easily defeating Heavenly Axe and handling the enemies.

*And…… that look in his eyes.*

It had lasted no more than an instant, but she had seen it clearly.

Jin Taekyung’s gaze had lingered on Song Ilseom as he turned away.

And there had been a faint trace of surprise in his eyes.

*There’s definitely something going on.*

Ju Hwaran suddenly thought back over the past two years—the countless failures she had endured while leading the Escort Bureau before she had even turned twenty.

If those failures had been caused by trusting people too much, if they had been caused by someone’s betrayal, what was she supposed to do?

*Whoosh……*

As the cold wind whipped around her, Ju Hwaran stood there for a long time.

* * *

“Could you provide me with a quiet room?”

The man was dressed in white. He was strikingly handsome, and his speech and conduct were so courteous that no one listening could bring themselves to refuse him.

The sight of him brought to mind a proud, solitary crane, and the head guard standing at the entrance found himself wondering.

*Who is he? I’ve never seen him before.*

Xi’an Tower was, as its name suggested, one of Xi’an’s foremost pleasure houses.

To stay there required not only money, but also a social position to match. As a result, the faces that appeared there regularly were always the same.

*But he’s a young man who came alone, without a carriage or servants……*

Under normal circumstances, he would have been turned away without a second thought.

Yet something about the man bothered him. That was why the head guard had dismissed his subordinates and come out to meet him personally.

“Have you visited our pleasure house before?”

“No. My circumstances aren’t good enough for luxuries.”

The young man gave an embarrassed smile and rubbed his cheek.

The head guard’s eyes widened.

*That’s……!*

Embroidered on the young man’s snow-white sleeve were pale crimson blossoms.

They were unmistakably plum blossoms in full bloom.

A stammering voice slipped between the head guard’s lips.

“M-May I ask your honored name?”

“I’m a Daoist named Baek Museong.”

“H-Huashan’s Lone Crane!”

Baek Museong, the direct Disciple of Huashan Sect Leader Heavenly Sword True Person, smiled faintly.
## Chapter artifact 313

# Chapter 313

Huashan’s Lone Crane, Baek Museong.

There was no one in Shaanxi—or in the entire Murim—who didn’t know that name.

Baek Museong was the direct Disciple of Heavenly Sword True Person, and he had been called Huashan’s future since childhood.

Among the sharp-eared, gossip-loving busybodies, rumors circulated about the Sword Saint’s youngest Disciple. Even they never doubted that Baek Museong would one day become the Sect Leader of Huashan.

“I hear the Huashan Divine Dragon’s martial prowess has already surpassed that of the Elders of the Nine Sects and One Gang. He’s truly a genius who appears once in a century, if that.”

“Even so, no matter what anyone says, the next Sect Leader is obviously Huashan’s Lone Crane. Baek Museong is made of different stuff. He was born with everything a Sect Leader needs.”

“That’s true. Is he lacking in martial arts? Or as a person? If not him, then who could possibly become Sect Leader?”

The people drinking and chatting on the first floor of Xi’an Tower did not know that the subject of their conversation was passing behind them.

“I’ve heard plenty about your renown, Great Hero Baek. It’s an honor to meet you.”

“Great Hero? You flatter me.”

“Not at all. I’m merely calling a Great Hero a Great Hero. What could possibly be excessive about that?”

In response to the head guard’s fervent gaze, Baek Museong merely gave an awkward smile.

The attention people paid him was nothing new.

As Huashan’s standing rose after having faltered following the Sword Saint Mae Jonghak’s withdrawal from the world, so too did the burden on Baek Museong’s shoulders grow heavier.

*The Sect Leader.*

For Baek Museong, who was barely into his thirties, it was a distant and weighty title.

He was inwardly shaking his head at the thought when the head guard stopped walking.

“This is the place.”

“This is…?”

“Even in our Xi’an Tower, which proudly calls itself the finest in Shaanxi, this is the only private annex.”

Baek Museong looked around at the garden decorated with jade and the interior filled with all kinds of luxurious furnishings. His expression grew troubled.

“I’m sorry, but I don’t have enough money on hand to use a private annex. Could you provide me with a quiet room instead?”

“Haha, you’re as frugal as I heard.”

The head guard continued with a hearty laugh.

“Please don’t worry. The owner has repeatedly instructed us that whenever a guest from Huashan arrives, we are to provide the utmost hospitality and charge nothing at all.”

“The owner said that?”

“Yes. There was some sort of trouble with the Zhongnan Sect last autumn, but it was resolved thanks to Huashan’s assistance. The other two members of the Three Plum Blossom Elites—your Junior Brothers—played a major role.”

“Ah, I see. It happened while I was in secluded training, so I didn’t know much about it.”

“Actually, I only heard about it myself. I’ve only been working here for barely a month. Haha.”

Only then did Baek Museong nod as if he understood.

It wasn’t as though he had spent the past year doing nothing.

Meeting Cheongpung, a peerless prodigy, and Jin Taekyung had been a tremendous shock to Baek Museong, as well as a fresh source of stimulation. That was why he had decided to enter secluded training for a year.

*It was a meaningful time.*

The enlightenment he gained during his training had made Baek Museong stronger and more profound than before.

And that wasn’t the only thing that had changed. Huashan’s position was incomparable to what it had been a year ago.

Even the government offices heavily staffed by Zhongnan’s lay disciples had begun seeking Huashan first whenever trouble arose.

*If Master’s letter is true, they have no choice.*

Five days earlier, a messenger eagle sent by his Master, Heavenly Sword True Person, had brought astonishing news.

The blood calamity at Shaolin. The death of Dharma King Hong Dao. And the report that Sword Saint Mae Jonghak was being considered as a candidate for the Alliance Leader of the new Murim Alliance, which was being revived after decades.

“In any case, everyone around me is in an uproar. Even my friends have been asking me about it. They say their children seem to have a talent for martial arts, and they wonder if they might be able to enter Huashan as lay Disciples, at least.”

Baek Museong recognized the meaning concealed in the head guard’s pointed gaze and gave a bitter smile.

The man looked well past forty. He, too, must have been a parent who wanted to send his child into Huashan.

But Baek Museong pretended not to notice and answered.

“Well, if fate brings them together, it may happen. But is there really any need for a child to learn martial arts? At that age, growing up healthy is enough.”

“……I see.”

As the head guard’s face fell, Baek Museong murmured inwardly.

*If you knew about the bloody storm that will soon blow in, you wouldn’t be making that expression.*

Rumors about the blood calamity at Shaolin had already begun to leak out here and there.

But the existence of Dark Heaven remained a top-secret known only to a very small number of people. As one of those few, Baek Museong had a premonition.

A bloody wind would soon sweep through the Murim. Dark clouds would cover the sky, and thousands upon tens of thousands of weapons would tumble across the ground alongside their owners.

The wails of children who had lost their parents and parents who had lost their children would echo from every direction.

*I’ll stop that from happening. I will—and Huashan will.*

Everyone in the Murim must have felt the same way as Baek Museong.

The head guard was tilting his head at the sudden heaviness of Baek Museong’s mood when—

“Where’s the chief manager? Chief Manager!”

“Young Hero, the chief manager has stepped away for a moment. So please calm down—”

“Calm down? After I’ve been treated this poorly, do I look like I’m in any state to calm down?”

“A-as I said, the private annexes are already full. We’ll show you to a special room, so please calm down.”

“Shut up! I absolutely must use a private annex today, so get out of my way!”

“Oh, Young Hero!”

Bang! Crack!

Shouts drew closer amid the clamor. The head guard knitted his brows and spoke.

“I apologize for showing you such an unpleasant scene. It seems my subordinates have failed to handle the matter properly.”

“Please, think nothing of it. I understand completely.”

No matter how carefully Xi’an Tower chose its guests, it was still a pleasure house. Wasn’t it only natural for every kind of bug to swarm a flower garden?

“Still, it’s barely noon, and he seems quite drunk.”

“It happens from time to time. He appears to be the son of some powerful family, but we’ll settle the matter and send him home. Great Hero Baek, you needn’t concern yourself with it.”

Baek Museong let out a hearty laugh and shook his head.

“Haha, I’m not so sure. You’d better stay here.”

“Pardon?”

“He doesn’t seem like an ordinary scion of a powerful family.”

“What does that—”

The head guard faltered. He had sensed the approaching footsteps amid the ceaseless uproar.

*A martial artist!*

As the situation grew more serious by the second, the cries of the guards protecting the inner courtyard rang out alongside hurried footsteps.

“Stop!”

“You can’t pass beyond this point!”

Xi’an Tower was frequented even by high officials and powerful nobles, so the quality of its guards was high as well. But even those First Rate martial artists, rich in practical experience, were no match for the drunkard’s rampage.

“You bottom-of-the-barrel Third Rate trash from wandering martial artist backgrounds dare…”

“Gah!”

Whoosh! Thud-thud-thud!

Short cries of alarm from the guards and the fast, powerful sounds of impacts rang out. In an instant, the area outside the private annex fell silent.

Then rough, unsteady footsteps began to approach, driving the silence away.

*He took down six First Rate martial artists in an instant while that drunk?*

*A master—and not just any master. A Peak master.*

Just as the head guard’s face hardened and his hand moved toward his sword hilt, Baek Museong gave a small shake of his head.

“I think I should handle this.”

“Great Hero Baek, that’s—”

“It’s all right. We know each other from several past encounters. He’ll back down for my sake, if nothing else.”

“What do you mean?”

“Our elders have a connection that has been passed down to us. Ah, of course…”

Baek Museong scratched his cheek and added one more thing.

“It isn’t exactly a harmonious relationship.”

“……!”

At that moment, a thought flashed through the head guard’s mind like lightning.

First came the words *Zhongnan Sect*. Then a man’s name followed.

“C-could it be?”

He had only been the head guard of Xi’an Tower for a little over two weeks. But he had heard so many rumors about that man that his ears ached.

A man whose temperament was as extraordinary as the sect he came from.

The head guard twisted his expression and was just about to say the man’s name when—

Boom!

The private annex’s door, made of sturdy blackwood, exploded. Splinters flew in every direction.

Baek Museong smiled faintly at the young man approaching with a staggering gait and a face flushed red with alcohol.

“It’s been a long time. Have you been well?”

At the same time, the young man snarled.

“Why are you here?”

The face of Hyuk Sopyung, the Zhongnan One Dragon,[^1] twisted like that of an evil spirit.

* * *

“Wow! Wowww!”

“Please stop shouting. Everyone’s staring.”

“Benefactor! Candied fruit over there!”

“That damn candied fruit. Aren’t you sick of it yet?”

“No!”

“Then just open a shop!”

“Can the candied-fruit vendor come with us all the way to Sichuan?”

“No, you lunatic…”

“They sell thin noodles over there! They say the broth is made with beef!”

Cheongpung, you little bastard. You were like a rubber ball that could bounce anywhere without warning.

I quickly grabbed Cheongpung by the back of his neck as he scampered toward a roadside food stall.

“Please, let’s just live like human beings—no more, no less. Like human beings!”

“Candied fruit… thin noodles…”

“Just wait a little longer, and I’ll feed you until your belly bursts!”

“Really?”

“How many times do I have to say it? So please shut your mouth and follow quietly, okay?”

Of course, I wasn’t feeding him with my money. It was Huashan’s money. But either way, same difference.

*We should have passed straight through here, too.*

According to our original schedule, there hadn’t even been any need to stop in Xi’an.

But before we left, the Sect Leader of Huashan, Heavenly Sword True Person, had asked us to stop by Xi’an. Since it was Cheongpung’s hometown, we decided to pass through while we were at it.

We had been pushing ourselves for nearly seven days and nights without eating or washing properly. I also wanted to be hosted properly and rest for at least one day.

*I was told Huashan’s Lone Crane, Baek Museong, would be waiting for us.*

It had already been more than a year since I’d last seen him.

Before leaving for Anhui with Jeok Cheongang, Baek Museong had said this to me.



*“Contact me whenever you come to Shaanxi. I’ll treat you properly. Haha.”*



When he said he would treat me to a full course, I wondered if the guy was from Busan, but apparently it hadn’t been empty talk.

At least, judging by the fact that we were meeting like this today.

“By the way, where’s Xi’an Tower?”

According to a passerby I’d stopped to ask, we just had to follow the main road straight ahead. But why was this street so crowded? I couldn’t see an end to it.

I was looking around when a finger covered in black grime pointed toward a building in the distance.

“That is Xi’an Tower.”

“Where? Oh, you’re right. How did you know?”

Gung Gibang, the future beggar boss, answered with a proud expression.

“It is the finest place to beg. The food they leave behind and throw out is on the level of a sumptuous feast, and because people of high status come and go, they give plenty of alms. No beggar could fail to know this place.”

“……”

So it was a Beggars’ Sect hotspot.

I shook my head and walked toward Xi’an Tower.

When we reached its enormous main entrance, wide enough for ten people to pass through at once, a guard who appeared to belong to Xi’an Tower bowed his head.

“I’m sorry, but we’re closed today.”

“……What? Is it a day off?”

“Not exactly. There was a slight problem during business hours.”

“Oh.”

I hadn’t expected that.

I turned my head slightly and saw Cheongpung looking as though he was about to burst into tears.

Scratching my head, I spoke to the guard.

“Isn’t there any way around it? We had an appointment today. His name is Baek Museong. I was told you’d know him if I gave you his name.”

“Again, I’m sorry, but at the moment— Excuse me? Did you say Great Hero Baek Museong?”

“Yes. Baek Museong, Huashan’s Lone Crane.”

Cheongpung called out in an earnest voice.

“Martial Nephew Baek! Where are you, Martial Nephew Baek? Can you hear my stomach growling?”

The guard looked back and forth between us before flinging open the tightly closed main gate.

“I’ll escort you to the private annex immediately!”

*What the hell?*

*Why the sudden change in attitude?*

*Did Baek Museong stand us up?*

My guess was wrong. Following the guard as he raced ahead almost as if he were flying, we arrived at a nearly devastated private annex.

Baek Museong was waiting for us there, sword drawn.

*Wow. This is really the full course.*

*This kind of shit makes me sick of being a martial artist.*

[^1]: A sobriquet for a leading young martial artist of the Zhongnan Sect.
## Chapter artifact 314

# Chapter 314

I stared blankly at the scene unfolding before me.

The spacious room had been reduced to a wasteland. Amid all the broken debris stood two young men facing each other. No—three, if you counted the middle-aged man whose face had gone deathly pale.

*What kind of picture is this supposed to be?*

The answer came quickly.

What kind of picture? The same one I saw practically every day.

Provocation and fighting. At this point, I was starting to think they were essential virtues of martial artists.

After roughly assessing the situation, I muttered,

“You’ve really laid out a full-course feast.”

Baek Museong quietly lowered his sword and gave me an awkward smile.

“You came.”

“You told me to come, so I did. But now I already want to leave.”

“It’s been a long time. But where are the others…?”

His eyes swept over my back. He couldn’t possibly be looking for Gung Gibang or Hyuk Mujin. He was obviously searching for his hated Martial Uncle.

But Cheongpung and the rest of the Bermuda Triangle had vanished without a trace.

*I thought they were following me quietly.*

*Please, just don’t cause any trouble.*

I rubbed the spot between my eyebrows and answered. Never mind the Bermuda trio—the immediate problem was right in front of me.

“Is that what matters right now? Is causing incidents just a Huashan thing?”

“There was a minor problem.”

“You don’t need to explain. Anyone can see that.”

Suppressing a click of my tongue, I looked at the young bastard facing Baek Museong.

Sharp eyes and a shovel chin. Every young prodigy I’d met around here had been handsome or beautiful, so I’d felt a certain sense of deprivation by comparison. But this guy was on the ugly side, which made me instantly feel more familiar with him.

“Hello.”

They say you can’t spit in a smiling face.

In response to my friendly greeting, the bastard said,

“Get lost. A beggar like you has no place here.”

I turned to Baek Museong.

“Young Hero Baek, who the fuck is this?”

“He is Hyuk Sopyung, the Zhongnan One Dragon.”

“This bastard is a dragon too? Why are there so many dragons?”

“He is known throughout the martial world as Zhongnan Sect’s greatest prodigy and one of the Ten Dragons and Phoenixes.”

“He looks like an earthworm.”

An ugly bastard with an ugly personality. That pissed me off twice as much.

At my mutter, Hyuk Sopyung’s eyebrows shot up.

“Well, look at this dogshit bastard…”

“It’s better than being worse than a dog. And think carefully before you swing that sword. This is the greatest crisis of your life.”

Hyuk Sopyung’s hand twitched. The blade that had been moving ever so slightly toward me was lowered, and he slowly looked me up and down with gleaming eyes.

“You’re no ordinary man.”

“Yep. I’m pretty extraordinary.”

“I thought you were someone who sold hides… But then again, Huashan’s Lone Crane wouldn’t deal with someone like that.”

“Unlike someone like you, Young Hero Baek will deal with anyone. And look at these beautiful muscles. Do you think you can build muscles like this by selling hides?”

My shabby appearance was a fact.

I had charged straight ahead for more than seven days and nights without stopping at an inn even once. The oil in my hair was flowing freely, and the clean martial uniform I’d started with had long since become covered in dust.

And, to put the finishing touch on the whole ensemble, I was carrying a wooden pack frame piled high with hides. The small figure of Jeok Cheongang was hidden inside.

*My clothes are one thing, but I do smell a little.*

It was about time I washed.

Hyuk Sopyung glared at me as I pressed my nose to my uniform and sniffed.

“Stop fooling around and state your sect and name.”

“Every time it’s ‘sect, sect.’ Don’t you ever get tired of it?”

“I’ll guarantee you one thing. If you aren’t from the Nine Sects and One Gang or the Five Great Families, you won’t walk out of here in one piece.”

“Really?”

I deliberately shuddered.

“What should I do? My sect is neither the Nine Sects and One Gang nor the Five Great Families. Could you just let me walk out anyway?”

“You should have watched your mouth. Remember that your paltry three-inch tongue has placed both you and your sect in danger.”

“My sect is actually in a bit of trouble already. There are only two of us in the whole sect, including me.”

“Two?”

“Yep. My Master and me. That’s it.”

Hyuk Sopyung turned toward Baek Museong with a sneer tugging at the corners of his mouth.

“To think you would waste your time dealing with a nobody from a Third Rate sect. You must have far too much time on your hands. Wouldn’t it be better to spend that time practicing your martial arts?”

“Perhaps. But I believe there is a considerable fallacy in what you just said.”

Baek Museong continued with a kind smile.

“First, Young Hero Jin’s sect is not Third Rate, and he is not a nobody. Second, you are a level below me. That has remained true from the day we first met until now.”

“What did you just say?”

“I said you are a level below me. Seeing you run amok while drunk, I suspect that will remain true in the future as well.”

His mouth was smiling, but his eyes were not.

There was something else in Baek Museong’s gaze, something unrelated to whether he possessed martial arts or not.

The aura—or perhaps the dignity—that belonged to him as a person.

That seemed to be part of the reason Hyuk Sopyung, despite grinding his teeth, didn’t dare answer him.

*And people of that type always try to solve things with their fists when they can’t think of a reply.*

Just like now.

The tip of Hyuk Sopyung’s sword trembled. I spoke before he could make a move.

“I believe I already said this. Think carefully before you swing that sword.”

Whoosh.

Hyuk Sopyung turned toward me, his eyes shining with murderous intent.

“You…”

“I’m an egalitarian who doesn’t discriminate between one thing and another, but you should be grateful that you’re a Disciple of the Zhongnan Sect. If you weren’t, you’d already have been carried out of here.”

Dark Heaven was gathering like a storm cloud in the distance.

At a time like this, when the Murim needed to unite just to stand a chance, starting a dispute with the Zhongnan Sect was obviously a terrible idea.

*Though, to be fair, it might already be a little late.*

I already had a bad history with the Zhongnan Sect.

As Three Hands of Zhongnan—and as the Roaring Fury Swordsman.

*Old Master thoroughly beat him down and drove him away a year ago.*

The Roaring Fury Swordsman wasn’t some nameless nobody rolling around in the street. He was an Elder of the Zhongnan Sect—and the martial senior brother of Wind-and-Cloud Sword Lord, the Sect Leader himself. From what I’d heard, the fallout had been considerable.

Later, I heard that the Roaring Fury Swordsman had entered secluded training for some reason, while the Three Hands of Zhongnan had been slapped by their Sect Leader.

*That’s already a perfectly good grudge. No need to take it any further.*

The smell of the oil Jeok Cheongang had poured over the Zhongnan Sect hadn’t even faded yet. Setting fire to it wasn’t something I wanted.

Especially not while Jeok Cheongang was unconscious.

“So put your sword away and go on your way quietly. Okay?”

*Good job. This is how you become an adult.*

It was such a calm response that I wanted to praise myself.

But Zhongnan One Dragon Hyuk Sopyung thought differently.

His teeth ground together, and his eyes flashed.

“Then let’s see if you have the skill to match that mouth of yours.”

Hissssss!

The sword in Hyuk Sopyung’s hand tore through the air at blinding speed.

At the same time, a net of Sword Energy descended upon me.

It was the very same martial art that had been unleashed by Song Il, the Roaring Fury Swordsman, a year ago.

*Heavenly River Thirty-Six Swords.*

The signature technique of the Zhongnan Sect.

Jeok Cheongang had told me that once someone reached the ultimate level of the Heavenly River Thirty-Six Swords, a single swing could fill the heavens and earth in every direction with Sword Energy.

But…

“You know what?”

Whoosh!

Flamefire Path.

The Fire Gate Clan’s signature movement technique, passed down for hundreds of years, transformed into a single streak of flame.

It tore through the net of Sword Energy and reached its target without hesitation. Looking into Hyuk Sopyung’s wide-open eyes, I whispered,

“You and I are on different levels.”

“……!”

Hiss—grab!

Hyuk Sopyung hurriedly changed the path of his sword, but I seized his wrist.

The Extreme Yang qi concentrated in my hand made a sizzling sound as his flesh burned.

“Gaaah!”

A single scream escaped him.

The sword slipped from Hyuk Sopyung’s grasp and rolled across the floor with a metallic clatter.

Before it even hit the ground, my palm had already connected with his cheek.

Smack!

Once more.

Smack!

And once more.

Smack!

Hyuk Sopyung’s body staggered after taking three slaps before he had any chance to resist.

Even without putting any internal energy into the blows, my physical abilities had long since surpassed normal human limits. Hyuk Sopyung’s eyes were already unfocused, his spirit half gone.

“What did you say earlier? You wanted to see if I had the skill to match my mouth?”

“Ghh… Ghhhhh…”

“Listen, you idiot. If you’re from the Zhongnan Sect, then I’m from the physical school. Next time, make sure you know where you’re going to lie down before you stretch out your legs. Okay?”

Tap, tap.

I patted Hyuk Sopyung’s cheek, and only then did his eyes finally regain their focus.

“H-how could you overcome the Heavenly River Thirty-Six Swords at seven-tenths mastery so easily…?”

“You’ve only mastered seven-tenths of it? No wonder it felt so half-assed. Get it to at least nine-tenths before you come at me again. I’ve already faced it once, so the result will probably be the same, but still.”

“You’ve faced the Heavenly River Thirty-Six Swords at n-nine-tenths mastery?”

“I have. I even dodged it.”

“That’s impossible! Fewer than five people in our sect have mastered it to nine-tenths!”

“I’m talking about one of those five. I heard he’s one of the top three masters in Zhongnan.”

I let out a quiet laugh and continued.

“The Roaring Fury Swordsman, Song Il. I wonder how the old man is doing these days. He didn’t look very well when he was publicly humiliated and driven out last year.”

That answer was enough.

Hyuk Sopyung was a Direct Disciple who could be called Zhongnan’s purest blood, and he was known as the sect’s greatest prodigy. There was no way an insider wouldn’t know a rumor that even an outsider had heard.

Hyuk Sopyung’s bloodshot eyes widened, and his body trembled.

“Then are you…?”

“About what I said regarding my sect—every word was true. It isn’t the Nine Sects and One Gang, and there are only two Disciples: my Master and me. I don’t know why our sect’s rules are like that, but with its one-person transmission and refusal to teach the unworthy, it’s damn strict.”

“The Fire Gate Clan…!”

“Disciples! There are two of them!”

“Sleeping Dragon of Shanxi, you’re Jin Taekyung!”

“Jin Taekyung! That’s right!”

I gave his collar a hard yank and shouted. Hyuk Sopyung’s face turned deathly pale.

I watched his expression for a moment, then gave the collar I was holding a few brisk pats.

“You know what our Master is like, right? Let’s end this here without giving each other any reason to be offended. What was it? Right. Let’s agree never to speak of this again.”

“……”

“Strange. No answer. Maybe you’ll be able to hear me after about ten slaps.”

I slowly raised my palm.

Hyuk Sopyung flinched reflexively and clenched his teeth.

“I… understand.”

“Hm? What did you say? I can’t quite hear the voice of a loser who’s only mastered seven-tenths of the Heavenly River Thirty-Six Swords.”

“……I said I understood.”

“Good. Take care on your way. I won’t walk you out.”

Crack.

The bones in Hyuk Sopyung’s fist creaked as he clenched it with all his strength.

After glaring one last time at me, Baek Museong, and the middle-aged martial artist whose identity I didn’t know, he took a long stride toward the door of the private annex.

Just as he was about to leave, Baek Museong spoke.

“I’m reminded of a boy I met at a Huashan–Zhongnan gathering ten years ago.”

“……!”

“Take care, Sopyung.”

At Baek Museong’s calm voice, Hyuk Sopyung stopped for a moment. Then he left the private annex without another word.

Hyuk Sopyung’s presence receded into the distance.

At the same time, someone began creeping toward us.

“Come out.”

At my words, someone sucked in a startled breath.

A moment later, Cheongpung poked his head out, his cheeks puffed up like a squirrel’s.

He gulped down the food in his mouth, glanced around nervously, and bobbed his head to Baek Museong.

“I’m really sorry about last time, Martial Nephew Baek…”

Suddenly, I remembered what had happened a year ago.

While Cheongpung was being forcibly escorted back to Huashan, he had beaten Baek Museong and the Three Plum Blossom Elites before escaping.

*This is a meeting between the perpetrator and the victim.*

*That bastard is guilty, no question.*

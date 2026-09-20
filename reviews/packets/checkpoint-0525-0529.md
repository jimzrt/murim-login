# Checkpoint Review — 525–529

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

# Chapters 525–529

## Plot

Mae Jonghak accepts leadership of the New Murim Alliance and orders its flag raised. At Mount Song, the Alliance is formally inaugurated under a single banner, and Mae declares that war against Dark Heaven has begun. News of the Mount Song Resolution spreads across the Central Plains, drawing factions, wandering martial artists, reclusive masters, and retired legends into the coming conflict. Jin Taekyung and Cheongpung, who helped raise the flag, become known as the Two Dragons above the Ten Dragons and Phoenixes.

The Alliance’s inauguration brings Taekyung a constant stream of visitors seeking connections to him or the Jin Family of Taiyuan. After three exhausting days, he rejects Central Plains Commerce’s approach and expects the resentful Zhongnan Sect to obstruct him. Meanwhile, Cheongpung develops Mimi Step from Mimi’s movements, but his growing focus on the technique coincides with an unusual loss of appetite.

Gung Gibang invites Taekyung and Cheongpung to meet several members of the Ten Dragons and Phoenixes. Cheongpung refuses, while Taekyung attends after learning that Ju Hwaran is waiting for him. At the inn, Hwaran anxiously watches for Taekyung’s arrival. Hwangbo Ak, the Hwangbo Family’s Lesser Family Head and her admirer, resents Taekyung and dismisses his achievements as Jeok Cheongang’s work. After Hwangbo insults Hwaran’s escort and a nearby group as lowborn practitioners of demonic, heterodox arts, someone at the table rises to confront him.

## Continuity

- Mae Jonghak is the Alliance Leader of the formally inaugurated New Murim Alliance; Song Ho remains Chief of the Hidden Shadow Pavilion under his authority.
- The Mount Song Resolution has begun widespread mobilization against Dark Heaven. Mae publicly states that another hundred thousand Demonic Path fighters are approaching the Central Plains.
- Jin Taekyung and Cheongpung are publicly regarded as the Two Dragons, above the Ten Dragons and Phoenixes.
- Taekyung’s role in raising the Alliance flag has made him a target of admiration, resentment, and factional approaches. He reached the system status **Exhaustion** after handling visitors for three days.
- Taekyung expects the Zhongnan Sect to obstruct him because of its repeated humiliations involving him, the Jin Family of Taiyuan, and Jeok Cheongang.
- Cheongpung created **Mimi Step**, a snake-like high-speed footwork technique, and has recently lost his appetite while refining it.
- Ju Hwaran is waiting for Taekyung at the inn. Hwangbo Ak, her admirer and a member of the Ten Dragons and Phoenixes, regards Taekyung as a rival; Baek Woo fears provoking Taekyung after the Star-Array Grand Banquet.
- Gung Gibang opposes the coming war on principle despite the chance for fame.
- Mungyeong has ended Taekyung’s direct training and assigned him to integrate martial principles into his existing techniques; the effect of the custom fire-qi pill remains unresolved.
- Zhuge Feng’s Demon-Sealing Formation still blocks mana from the exposed Gate, while Jang Taebo is arranging for artisans to process the Water God Dragon’s remains.
- The Southern Heaven Demon Empress is traveling toward Yunnan and expects further deaths. The Lord of Heaven’s identity, Dark Heaven’s Gate-opening method, and its connection to Taekyung’s original world remain unknown.
- The Blood Fish’s role in Jang Sam’s transformation and the possibility of further Blood Fish- or Gate-related transformations remain unresolved.
- The outcome of Jeok Cheongang’s duel with Nangong Cheon remains unresolved.

## Translation Decisions

- Retain **New Murim Alliance**, **Murim Alliance**, **Alliance Leader**, **Hidden Shadow Pavilion**, **Dark Heaven**, **Ten Dragons and Phoenixes**, and **Demonic Path**.
- Render **숭산결의** as **Mount Song Resolution** and **미미보** as **Mimi Step**; retain **footwork technique** for **보법**.
- Render **탈진** as the capitalized system status **Exhaustion**.
- Retain **Blazing Flame Divine Dragon**, **Number One Sword Under Heaven**, **Myriad-Poison Asura**, **Thousand-Year Poison Horned Snake**, and **Young Lady Ju**.
- Preserve Taekyung’s blunt profanity, factional insults, Cheongpung’s innocent humor, and the contrast between Hwaran’s sincerity and Hwangbo Ak’s conceit.

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
    "The Black Dragon Demon Gate remains a major unorthodox power descended from the Demonic Cult's Twelve Branches; Wudang's second report identifies Jang Sam as the Killing Ghost and links his transformation to the Blood Fish.",
    "Jin Taekyung remains a Supreme Peak master with Three Flowers Gather at the Crown, advanced qi perception, exceptional resistance to monster Fear, and public S-rank-level recognition despite retaining an A-rank license.",
    "Gung Gibang opposes the war on principle.",
    "Ju Hwaran is eagerly awaiting Taekyung at an inn; Baek Woo and Hwangbo Ak are longtime friends and fellow Ten Dragons and Phoenixes members, and Hwangbo resents Taekyung while Baek fears provoking him."
  ],
  "continuity_sources": [
    529,
    528
  ],
  "open_questions": [
    "What is the Lord of Heaven's identity, how is he connected to the dangerous force Taekyung associates with his original world, and how can Dark Heaven open Gates?",
    "Where is the Southern Heaven Demon Empress ultimately headed, and what does she intend to do in Yunnan?",
    "What is the outcome of the duel between Jeok Cheongang and Nangong Cheon, the Azure Sky Sword King?",
    "Did the Blood Fish cause Jang Sam's transformation, and could similar Blood Fish or Gate-related transformations occur elsewhere?",
    "How will Taekyung incorporate Mungyeong's martial principles, and what effect will the custom pill have on him?"
  ],
  "safe_through": 529,
  "temporary_decisions": [
    "Render 숭산결의 as Mount Song Resolution and 미미보 as Mimi Step; retain footwork technique for 보법.",
    "Render 탈진 as the capitalized system status Exhaustion; retain Ten Dragons and Phoenixes, Blazing Flame Divine Dragon, Dark Heaven, Murim Alliance, and Old Master.",
    "Render 홍적 as Hong Jeok, 모용영휘 as Murong Yeonghwi, and 복마전 as demon-slaying battleground.",
    "Render 새외무림 as Outer Murim, 새외 as Outer Lands, 북해빙궁 as North Sea Ice Palace, 야수묘왕 as Beast Miao King, and retain Nanman Beast Palace for 남만야수궁.",
    "Render 쌀벌레 as Rice Weevil and 만두 벌레 as dumpling grub; retain the chapter's blunt profanity and monster-comparison humor."
  ],
  "version": 1
}

## Reading copies

## Chapter artifact 525

# Chapter 525

The Alliance Leader’s Hall was quiet in every direction. Only one person remained in the hall where countless people had come and gone just one shichen—approximately two hours—earlier.

“How quickly the years pass.”

The young man, Sword Saint Mae Jonghak, murmured the words under his breath.

His gaze was fixed on empty space, reaching back toward some distant point in the past. It was a stale old memory that hardly anyone alive still remembered.

*They all went that way.*

Of the people who shared the same memories as Mae Jonghak, very few had lived out their natural spans.

Most had fallen in nameless wastelands and fields, never to rise again.

The monster known as the Great Faction War had given birth to countless deaths and turned those who survived into heroes.

*But in the end… it’s happening again.*

Enough time had passed for the mountains and rivers to change four times over.

Peace had come to the world. The pain and sorrow endured in the whirlpool of war had faded, and the orthodox Murim had sung of the glory of victory.

Then, beneath a sky that had seemed destined to remain blue forever, a dark cloud called Dark Heaven had appeared.

*Peace is over now.*

The runny-nosed child who had not understood the horrors of war had become middle-aged, while the young man who had drawn his weapon and burned with righteous indignation had grown old.

Those who had not even been born back then had come to Henan in pursuit of glory rather than justice.

Their lives, personalities, and goals were all different.

And Sword Saint Mae Jonghak knew it well. He—and no one else—would have to lead them all into battle once again. He would have to defeat Dark Heaven, which sought to plunge the world into misery.

That was when a low voice slipped between Mae Jonghak’s firmly closed lips.

“Every now and then, I find myself wondering. Wondering whether I can truly do this.”

It was not a soliloquy. Mae Jonghak knew it, as did the person who had been quietly standing guard outside the door for some time.

The sturdy old man, Thousand-Faced Fox Song Ho, stepped forward as he answered.

“You can.”

Clack.

The tip of his prosthetic leg struck the floor, the sound echoing unusually loudly. Beneath his hanging white hair, his shrewd eyes shone with force.

“No—you must.”

“I know.”

Mae Jonghak let out a quiet sigh.

“But I’ve known nothing but the sword my entire life. Thanks to that, I even gained the empty title of Sword Saint.”

“It is precisely because you are the Sword Saint that everyone will trust and follow you.”

“The vessel of a martial artist and the vessel of a leader are different. I couldn’t even become the Sect Leader of a faction.”

“It’s not that you couldn’t. You simply chose not to.”

The Thousand-Faced Fox was speaking the truth.

When the Great Faction War ended and the former Sect Leader passed away, every disciple of Huashan had firmly believed that Sword Saint Mae Jonghak would become their new Sect Leader.

“But you refused. In the end, the Sect Leader’s Command Token went to your Disciple, Heavenly Sword True Person.”

“It was only natural. He was more suited to becoming Huashan’s Sect Leader than I was. And…”

Mae Jonghak ran his fingers over the treasured sword at his waist before continuing.

“I simply liked the sword.”

The Thousand-Faced Fox gazed quietly at Mae Jonghak, then suddenly spoke.

“I don’t know whether I ever told you this.”

“Told me what?”

“That person once struggled with the same concern.”

“If you mean that person… surely you’re talking about the Martial God?”

The Thousand-Faced Fox gave a small nod.

“To the people of the world, that person seemed perfect in every way.”

“I know. The Martial God excelled at everything. No—he was overwhelming.”

“But he was a person too. And in the end, he succeeded. For some reason, these old eyes see the two of you overlapping.”

“……!”

Mae Jonghak’s body abruptly stiffened. After silently regarding the old martial artist standing upright before him for some time, he suddenly spoke.

“Great Hero Song.”

“Yes?”

“It truly is… a fine day.”

“The sky is clear.”

“May I ask the time?”

“It is the wu hour. Everyone is waiting for one person.”

“I’m late.”

“You’re not late. This is only the beginning.”

Sword Saint Mae Jonghak turned his head. Powerful sunlight poured through the wide-open window.

*Yes. It truly is a fine day.*

He repeated the words once more in his heart. After taking in the blue sky, he slowly turned around.

At the same time, the Thousand-Faced Fox realized it.

The young man standing before him was no longer merely a martial artist.

“Chief of the Hidden Shadow Pavilion.”

The quiet voice pierced Song Ho’s ears.

The Hidden Shadow Pavilion was directly subordinate to the Alliance Leader’s Hall, and there was only one person with the authority to command its chief.

Song Ho took a deep breath and clasped his hands.

“Song Ho, Chief of the Hidden Shadow Pavilion. I await the Alliance Leader’s command.”

The next moment, the words that slipped from Mae Jonghak’s lips were the beginning of the New Murim Alliance and the first order of its new Alliance Leader.

“Let’s go raise the flag.”

The old martial artist’s eyelids trembled. Then a powerful cry, as forceful as any young man’s, followed.

“As you command!”

* * *

I raised my head and looked at the sky. The sun, already hanging high in the middle of the blue heavens, poured down fierce sunlight.

Not even a cool breeze stirred in the heat. A thought suddenly flashed through my mind.

*It’s hot.*

It was hot, but not sweltering.

That was not merely because I had reached the state of Unaffected by Cold and Heat after attaining the Supreme Peak realm.

What felt hot at this very moment was not the sunlight, but the heat itself. It would have been just as accurate to call it the aura radiating from countless people.

Sssss.

Below the high platform, the aura released by an immeasurable number of martial artists seemed to have brought even the wind to a halt.

The qi rising like a heat haze burned hotter and fiercer than the sunlight pouring down from the sun.

Then, cutting through that heat, the person everyone had been waiting for finally appeared.

Thud. Thud.

The forceful sound of his footsteps pierced everyone’s ears. That alone was enough to tense their entire bodies and clear their minds.

The wandering martial artist who had been causing a drunken disturbance only yesterday, as well as the orthodox and unorthodox martial artists who had gotten into a full-blown brawl with each other, all swallowed dryly.

Everything was because of the presence radiating from a single person.

*Sword Saint Mae Jonghak.*

The One God, Three Saints, and Ten Kings.

If the Nine Sects and One Gang and the Five Great Families were the fifteen pillars supporting the world, then the people bearing those titles were the heroes who had given the world a new beginning.

Ten kings stood upon the earth. Above them stretched the unreachable sky of the Martial God, and three stars adorned that sky.

And…

*The brightest star of them all.*

Sword Saint Mae Jonghak. Also known as the Number One Sword Under Heaven.

Shhk-shhk-shhk!

The thousands of martial artists split apart all at once.

No cheers or exclamations could be heard.

Some were stunned by Sword Saint Mae Jonghak’s youthful appearance, while others shuddered at the overwhelming aura they could feel against their skin. But not one dared voice a question or say anything aloud.

*No. There’s no room for doubt.*

This was a path meant for one person alone.

And the giant who finally stepped through the ranks of people and climbed onto the high platform swept his calm gaze across the surroundings.

“You’ve all been waiting a long time.”

The platform was a place reserved for the chosen.

The Sect Leaders of factions known as prestigious great sects and the Family Heads of great families. Or, regardless of their origins, heroes and masters who had built up immense fame. They were the people who belonged on this platform.

*Jeok Cheongang and I, as well as the Jin Family of Taiyuan, are no different.*

But if the people on the platform were the pillars of the new Murim Alliance, Sword Saint Mae Jonghak was its foundation and its head.

Without anyone needing to take the lead, everyone including me rose from their seats and clasped their hands toward Mae Jonghak.

Dozens of people spoke at once, but the voices that followed sounded as if they belonged to a single person.

“We greet the Alliance Leader.”

No one held back—not even Jeok Cheongang and Cheongpung, who were seated on either side of me. They all adopted solemn expressions and paid their respects.

Mae Jonghak watched them with a faint smile, nodded, and turned away.

Then, the next moment, the martial artists numbering in the thousands—or perhaps ten thousand—heard it clearly.

The giant’s voice shook heaven and earth.

“Peace is over.”

“……!”

The air surrounding us burst apart.

The towering trees trembled, and the bodies of the heroes gathered below the platform stiffened like statues.

As Mae Jonghak continued speaking with unprecedented internal energy behind his words, there was no trace left of the eccentric figure we had seen until now.

“The war has already begun, and another hundred thousand Demonic Path fighters are approaching the Central Plains.”

There might have been people who had never experienced the Great Faction War, but there was no one who knew nothing of that terrible conflict.

Fear and anger clouded the eyes of the elderly martial artists, while the young martial artists trembled with an inexplicable shiver.

“Dharma King Hong Dao.”

At Mae Jonghak’s next words, the monks of Shaolin softly murmured Buddhist invocations.

“Poison King Tang Taesang and the Heaven-Shaking Venerable Nun of Emei.”

Tang Sadok, the Myriad-Poison Asura, had traveled a long way despite his ailing body, and his green eyes gleamed. The nuns of Emei Sect shed tears.

“The blood that began flowing from Shanxi Province continued into Henan and reached Sichuan and Hubei.”

Countless lives had been lost in little more than a year.

The old martial artists praised by everyone and the young people who were still mere greenhorns alike had fallen before they could ever bloom.

*Eight Spring Gorge.*

The memory still came to me whenever I closed my eyes.

How many people had died in that narrow gorge in Shanxi Province?

Who were the people who had fallen in Henan, Sichuan, and Hubei?

I did not know their names or the dreams they had held in life.

But I knew what they had taken up their swords to protect.

*Something precious.*

Boom!

An unprecedented aura burst from Mae Jonghak’s entire body.

Purple energy rooted in the Zaha Divine Technique rolled over his shoulders like waves.

“Take up your weapons and fight back.”

It was not only his manner of speaking and his aura that had changed.

The Mae Jonghak of this moment was not merely the Sword Saint or the Number One Sword Under Heaven. He was the Alliance Leader guiding everyone.

“For the sake of the families who share our blood. For the sake of the Senior Brothers and fellow disciples, and the sects with which we have shared joy and hardship. And…”

A mighty cry erupted from between Mae Jonghak’s lips.

“To protect this Murim where we live, take up your weapons!”

The giant roared. A shiver rose along my spine.

The martial artists filling every direction exhaled the breaths they had been holding and let out a thunderous cheer.

“Waaaaaah!”

“For the annihilation of the Demonic Path!”

Shhk, chakachachang!

The world was flooded with light. Countless weapons flashed as they caught the sunlight pouring down overhead.

“Waaaaaah!”

“For justice and chivalry!”

Shhk, chakachachang!

The world was flooded with light. Countless weapons flashed as they caught the sunlight pouring down overhead.

As Mae Jonghak stared at the dazzling and magnificent sight, he reached down and grasped the enormous flag lying at his feet.

Murim Alliance.

Those three characters had been written across the flag in a vigorous, flying script. Once he raised it, a new era would begin.

But the next thing Mae Jonghak did was beyond everyone’s expectations.

“Great Hero Jeok. Would you help me?”

“……!”

I could feel the crowd’s agitation against my skin. Jeok Cheongang, who had been silently staring at Mae Jonghak, suddenly spoke.

“Is the flag heavy?”

“It seems to be, for now.”

“That flag feels heavy even to this old man. And the more hands, the better.”

The next moment, I realized what I needed to do.

At Jeok Cheongang’s signal, Cheongpung and I stepped forward and grabbed the flag at the same time.

Then we pulled it upright with all our strength.

The Murim Alliance had been born.
## Chapter artifact 526

# Chapter 526

“Waaaaaaah!”

Boom! Boom! Boom!

A thunderous roar swallowed everything.

The shouts of thousands of heroes, infused with internal energy, and their fierce fighting spirit awakened tranquil Mount Song and echoed without end.

Above the heads of people with different names, personalities, lives, and genders, a flag fluttered high in the sky.

**Murim Alliance.**

Those three words were all that had been written across the pure white cloth.

It was neither as splendid as a flag symbolizing an emperor nor as enormous as the Demonic Cult’s standard, which had once flown above the massive army that invaded the Central Plains.

But that was enough.

Everything was contained within those three words: Murim Alliance.

Now, the martial artists of the Central Plains would become one beneath that flag. In the new era they themselves had ushered in, they would fight a new enemy.

And…

“A new hero will be born.”

The quiet mutter came from somewhere.

Mungyeong had been watching the entire scene from atop an enormous unknown tree that had finally grown thick with leaves. His gaze settled on one person.

*Jin Taekyung.*

Mungyeong could see it clearly. The burning gaze of the young man standing like an iron tower with the flag in his hands.

Together with two giants—the Sword Saint and the Fire King—and another rising star, Huashan Divine Dragon Cheongpung, he accepted the cheers raining down from every direction.

He was already no different from a hero.

“Blazing Flame Divine Dragon!”

“Blazing Flame Divine Dragon Jin Taekyung!”

The heroes loudly chanted the name of the young hero holding the Murim Alliance’s flag.

As Mungyeong watched the scene, a quiet murmur slipped from between his lips.

“It’s finally beginning.”

A new era. A new enemy. And new heroes.

At last, the curtain rose on a stage that had remained closed for a long time.

Some would fall on an unknown plain and never rise again. Others would carve their names into a chapter of the long history of Murim.

Life and death. Humiliation and glory.

Right here, on Mount Song, the prelude to a massive war for the world was beginning.

* * *

The world trembled. No—it was undergoing a tremendous upheaval.

Anything that had not yet happened was fiction, nothing more than a rumor. But once it became reality, its impact was vast and overwhelming.

The Mount Song Resolution.

On a warm spring day, news that the Nine Sects and One Gang, the Five Great Families, and countless other Murim factions had finally gathered beneath a single flag spread far and wide.

That meant a fierce war to decide the master of the world had begun.

“Sect Leader, they say the Murim Alliance has been founded in Henan!”

“Send a messenger pigeon immediately. Our sect will gladly stand beneath the Murim Alliance’s flag.”

“Yes, Sect Leader!”

“Notify the other Sect Leaders in Fujian as well. We need to meet.”

The world was vast, and there were too many sects and families to count.

Those who had been unable to travel all the way to Henan for various reasons declared their intention to join the Murim Alliance one after another. Martial artists without a sect also decided what path they would take.

“Great Hero Jang, let us travel to Henan together. Shouldn’t we join the Murim Alliance?”

“I’m sorry, but I intend to head to Sichuan. You’ll have to go to Henan alone, Great Hero Gwak.”

“Huh. Qingcheng and Emei may still be standing, but if Dark Heaven heads to Sichuan first, just as the Demonic Cult once did, the region may turn into a demon-slaying battleground.”

“That is precisely why I must go to Sichuan. Shouldn’t I lend whatever aid I can?”

Some carried the two words *righteous chivalry* in their hearts.

“Brother, from what you just said, it seems we’re headed the same way. Let us travel together.”

“You’re quite the hero. What is your name?”

“Name? What do I need a name for? I’m nothing more than a wandering martial artist who makes his living by the sword, so put away that embarrassing word ‘hero.’ I don’t know how strong these Dark Heaven bastards are, but if I cut down enough of them, I’ll make a name for myself and earn a decent sum.”

Others took up their weapons while dreaming of competitive pride and making a name for themselves.

Among these people, who belonged to no particular sect and each had their own reasons for taking action, were also unfamiliar faces who had not appeared in Murim for a long time—or had never appeared in it at all.

“What brings you out here, Master?”

“The weather was pleasant, so I came out for some air. But you look troubled. What happened?”

“Well, I was wandering through the mountains looking for snow ginseng to give you, Master, when I met a herb gatherer. He told me that…”

The rumor that the Murim Alliance would be restored in Henan had already spread widely, even before the Mount Song Resolution.

News of the situation in Murim also reached reclusive masters who had withdrawn from the secular world and hidden themselves in remote mountains and deep valleys.

“Hmm. Dark Heaven and the Murim Alliance…”

“They say the foot of the mountain is in an uproar. The Murim Alliance has declared war against Dark Heaven, and the common people are trembling with fear.”

“Hah. After a long peace, calamity has come.”

“Master, what should we do?”

“Countless people will die, just as they did during the Great Faction War. Make preparations immediately, before it is too late. We must go to Henan.”

An old master who had been spending his remaining years in an unknown deep valley set out for the Central Plains with his Disciple.

“Old Master, did you catch a lot today?”

“Ugh. The fish aren’t biting worth a damn today.”

“Haha. I’ve heard you say that for forty years now. I caught a few carp. Take them home and eat them.”

“Of course I should. I was the one who saved your father’s life ten years ago. Give me one of the big, plump ones.”

“Understood. Since this is the last time, I’ll give you all of them.”

“Hmm? What do you mean, ‘the last time’? What strange nonsense are you talking about?”

“Haven’t you heard the news? They say a great calamity has descended upon Murim.”

“A calamity? Tell me more.”

“They say something called the Murim Alliance has been formed in Henan, and that it’s going to fight Dark Heaven, which is said to be the successor to that Demonic Cult. No one knows what might happen, so I was going to take my family and leave for a while… Old Master? What are you doing?”

“Can’t you see? I’m preparing to leave.”

“Where are you going? Wait, are you leaving your fishing rod behind?”

“I don’t think I’ll need it anymore. You use it.”

“Old Master! Old Master!”

“We’ll meet again someday. Stay safe.”

The white-haired old man who had spent his days sitting beside a secluded lake abruptly departed, a spear strapped to his back in place of his fishing rod.

Some of the old martial artists who had once dominated an era—or some of the reclusive masters from remote valleys who had devoted their entire lives to the single character *martial*—stepped back into the secular world and flowed into the wider world.

“Is this the Murim Alliance?”

“That’s right. But if you’ve come to join, we can’t let you in just yet. You’ll need to go to the pavilion over there and provide your sobriquet, name, and something that can prove your identity…”

“Then I’ve come to the right place. Go tell them that Hong Jeok has arrived.”

“Hong Jeok, Red Turban, whatever your name is, you still need to go through the verification process… Wait. What did you just say?”

“Hong Jeok. I said Hong Jeok, a man from Guangxi.”

“Th-the Fist King…!”

Names swept away by the waves of time, sobriquets that had vanished from sight.

And yet, despite everything, titles clearly etched into the memories of ordinary people began appearing everywhere.

Even after the sun set and darkness descended, their existence shone like torches.

Rumors about the newly risen stars also continued to pass from mouth to mouth.

“I’ll stake my life on this: the Ten Dragons and Phoenixes will play a major role in this war.”

At the words of the middle-aged man with the spatula-shaped chin, the narrow-eyed man snorted.

“What a laughable thing to say. They call them the Ten Dragons and Phoenixes, the finest young prodigies in the martial world, but weren’t they ultimately selected from among the disciples and heirs of prestigious sects and families?”

“And? What are you trying to say?”

“They’re all hothouse flowers. How much can people raised in comfort really accomplish on a battlefield?”

Spatula Chin narrowed his eyes.

“Listen to this bastard. Are you with Dark Heaven?”

“What!”

Bird Eyes bristled and shouted.

“They say that even a crooked mouth should speak straight, so don’t say something that’ll get you killed! Why would I be with Dark Heaven?”

“Then why are you putting down the pillars of our orthodox faction?”

“Putting them down? I’m just stating the facts! It’s not like I can shave down your chin!”

“What does my chin have to do with any of this? Why are you insulting my appearance?”

Fire rose in Spatula Chin’s eyes.

“Say one more word about my chin and you’d better be ready. Understood?”

“Spatula Chin! Every time I look at you, my breath catches—chin! Gunggi-chin, ka-thunk-thunk-chin!”

“You fucking bastard!”

Crash! Crack!

The table overturned, and the side dishes and liquor bottles went cascading across the floor.

In the vicious atmosphere, where a sword fight seemed ready to break out at any moment, the goateed man who had been watching Bird Eyes and Spatula Chin’s confrontation opened his mouth in a dignified tone.

“You’re both wrong.”

Bird Eyes and Spatula Chin turned toward the goateed man at the same time.

“What the hell are you saying?”

“I’ll rip out every hair of that beard.”

“……”

The goateed man slowly shook his head and continued.

“I have no particular disagreement with the idea that the Ten Dragons and Phoenixes will distinguish themselves. But compared with the strength Dark Heaven has shown through everything it has done so far, even the Ten Dragons and Phoenixes are ultimately nothing more than young prodigies.”

Color returned to Bird Eyes’ face.

“Then that means I’m right?”

“To some extent, I suppose so.”

“Exactly. You have uncommon insight. Your beard looks especially good today.”

“……”

Spatula Chin ground his teeth and glared at Bird Eyes.

“You bastard, your eyes are smaller than your asshole, and now you’re deaf too. Have you already forgotten that he said both of us were wrong?”

“……That part is fair. But why? I don’t see anything particularly wrong with what I said.”

The goateed man stroked his beard calmly as he answered.

“There are genuine talents everywhere. As you said, the Ten Dragons and Phoenixes grew up in the best possible conditions. But that doesn’t change the fact that they’re the finest young prodigies in the martial world.”

“Hm. And?”

“Not all of them are disciples of prestigious major sects. Jin Mukyung, the Second Young Master of the Jin Family of Taiyuan, is a prime example.”

“Ah, I forgot about the Heaven Shaking Sword.”

Spatula Chin had been waiting for an opening. He cut in with a mocking grin.

“The Heaven Shaking Sword is impressive, but Murong Yeonghwi, a blood relative of the Murong Family, is overwhelming too. Still, what could a nobody like you possibly know?”

“What are you talking about, you bastard whose chin would float even if you drowned…”

The two began growling at each other again. The goateed man let out a deep sigh before speaking.

“Stop fighting and listen. The young prodigies worth paying attention to aren’t the Ten Dragons and Phoenixes. It’s the fact that the Two Dragons stand above them.”

Bird Eyes and Spatula Chin froze.

Even they had to admit that the goateed man’s words were undeniably true. Before the names of the two Divine Dragons—Blazing Flame Divine Dragon Jin Taekyung and Huashan Divine Dragon Cheongpung—even the Ten Dragons and Phoenixes could not compare.

“Certainly…”

“That’s true.”

They nodded despite themselves, then voiced the question that suddenly occurred to them.

“What could those two be doing right now?”

“Who knows? But one thing is certain.”

The goateed man continued with a solemn expression.

“They must be doing something extraordinary.”

* * *

Cheongpung spoke with a stiff expression.

“Ahh, I want dumplings!”

“……”

*Don’t say it so loudly, you idiot.*
## Chapter artifact 527

# Chapter 527

Seven days and nights had passed since the day people called the Mount Song Resolution.

Amid the shouts of countless Murim heroes, the Murim Alliance’s flag had been raised once more. News that the Murim Alliance had officially been restored for the first time in decades spread beyond Henan in an instant, shaking the entire Murim world.

*Things have been moving at a frantic pace.*

At first, I had thought there was no reason for me to be particularly busy. But I realized how naïve that had been less than half a day after the Murim Alliance was formed.

“Captain. I hear there’s a visitor downstairs.”

“Why do you say ‘I hear he’s come to visit’ instead of just ‘he came to visit’?”

“Apparently Young Hero Cheong ran into him while he was out buying dumplings. He says he’s waiting downstairs.”

“I suddenly want dumplings. And I’m not meeting him.”

“I only caught a glimpse of him, but he looked like someone distinguished.”

“What, am I some lowborn bastard? Send our distinguished guest home with all due courtesy.”

“How could I do that? I hear he came after making an appointment.”

“What the hell are you talking about? I never made an appointment after coming here. And how many people do I even know?”

“That’s true. You don’t have any friends, Captain.”

“Really? Because it looks like you’re about to lose your head.”

“Hmm. Maybe they spoke with the Lesser Family Head?”

“This bastard doesn’t even flinch anymore.”

“Spend three years as Hyuk Mujin, and you wind up with about three lives.”

“Enough nonsense. Send him back. Ah, but exactly who is this important person?”

“Oh, wait a moment. I’ll go ask.”

“Go on.”

Hyuk Mujin went downstairs at a leisurely pace, then returned at a speed that could only be described as insane.

“K-K-Kongtong Sect! The Kongtong Sect Leader!”

“Bring him in at once! Bring him innnn!”

*No, seriously—why is hyung there?*

Starting with the Sect Leader of the Kongtong Sect, one of the Nine Sects and One Gang, a steady stream of those known as renowned masters of Murim came to visit.

The Family Head of the Nangong Family, whom I already knew, came in person. Then people from sects and families I had formed connections with while traveling across the Murim world began arriving one after another.

Of course, the vast majority were people coming to establish a new connection with me.

“Captain.”

“……Who is it this time?”

“The Shandong Yue Family. The Family Head came in person.”

“……Receive him with due courtesy.”

“A representative from the Murim world of Guizhou was sent as well……”

“……Bring him in too.”

“Oh, and Captain.”

“……Bring him in.”

I hadn’t realized I was this famous. No, to be precise, I hadn’t realized I was *this* famous.

As I continued meeting people who came rushing to see me, I reached a state of exhaustion after only three days.

*Fuck, I can’t keep doing this.*

I could understand if it were a blind date with a pretty woman.

But dealing with more than ten middle-aged and old men every day made me feel like my soul was leaking out through my ears.

The conversations we had over teacups that made me nauseous just from smelling them were mostly the same.

“Oh! So you’re the very Blazing Flame Divine Dragon I’ve heard so much about!”

*The Jin Taekyung Conversation Guide.*

I wondered if each of them had read a book with that title before coming, because their opening lines were exactly the same.

But even the most obedient child eventually has a moment when he starts acting up.

At first, I had smiled and exchanged meaningless pleasantries. But as time went on, I became more honest.

“I’ve heard many rumors about you.”

“I’ve heard plenty of stories about myself too.”

“A young hero has appeared in Murim. It’s truly wonderful. Ho ho ho.”

“I’m the happiest person of all. Ha ha ha.”

“Incidentally, I have a daughter of marriageable age……”

“I have two marriageable older brothers.”

“Good heavens, man! How dare you spring your daughter on someone out of nowhere like that? Are you in your right mind? Young Hero Jin, don’t take anything that fellow says too seriously.”

“It’s all right. I wasn’t listening closely anyway.”

“Then listen to me instead of him.”

“Wow. So this is how the conversation develops.”

“As a matter of fact, I have a daughter too. I’m sure you’ll like her.”

“I’ll stake Hyuk Mujin’s balls that I won’t.”

“What are you talking about? Balls—no, what man in the world would ever turn down a beauty?”

“If she’s beautiful…… Is your daughter very pretty?”

“Do you even have to ask? Her beauty is already famous throughout Fujian!”

“Oh. Ohhh.”

“There isn’t a single person who doesn’t know her! You could stop anyone passing by and ask them. She’s already pretty enough, but in five years, she’ll surely become the First Beauty of Fujian!”

“Wow, the First Beauty of Fujian…… Wait a moment. Why five years from now?”

“She’s twelve.”

“Get out.”

I could hardly remember how the seven days and nights had passed.

Some of the people who visited me already knew me, while others had come out of simple curiosity. But most of them were trying to form some kind of connection with either me or the Jin Family of Taiyuan.

And, of course, not all of them were martial artists.

“Captain. Someone from a place called Central Plains Commerce is asking to see you.”

“Bring them in—no, wait. Why is a trading company looking for me? Unless they’re after my eldest brother.”

“I’m not sure of the reason. But judging by my own eye for people, they don’t seem like bad people. It might be worth meeting them once.”

“Hey.”

“Yes, yes?”

“You bastard. You took a kickback from Central Plains Commerce, didn’t you?”

“Gasp! H-How did you know?”

“Spit back out every last bit of it and send them away. While I’m still asking nicely.”

Now there were even people slipping bribes to Hyuk Mujin.

Most of the visitors who had come so far had arranged their appointments through Jin Wikyung, and I had met them despite myself because turning them away would have been awkward.

The fact that they knew Jin Wikyung was the only way to meet me and still came directly meant one of two things.

*Either they had already been rejected by Jin Wikyung for some disqualifying reason, or their status was important enough that they could come whenever they pleased.*

The first case was overwhelmingly more common. Those people would try some shallow trick and often leave without even seeing my face.

Why were they going this far?

I already had a pretty good idea why all this sudden attention was being focused on me.

*It’s because of the flag, obviously.*

On the day the Murim Alliance was officially proclaimed, I had raised the Murim Alliance’s flag together with Mae Jonghak, who had taken office as Alliance Leader, Jeok Cheongang, and Cheongpung.

It had been a deeply moving moment for me as well, but I hadn’t attached that much meaning to it. To everyone else who had witnessed it, however, it seemed to have been an enormous culture shock.

*Well, I suppose it makes sense. Two fresh-faced young punks had stolen the spotlight from all the elders.*

At the time, the platform had been packed with people from prestigious great sects, including the Nine Sects and One Gang and the Five Great Families.

Murim had reached such an extreme level of population aging that I could have called the platform a senior center and no one would have objected.

Even the middle-aged men in their forties who had somehow managed to squeeze onto the platform were nothing more than pu'er tea runners. And yet Cheongpung and I, who had only recently passed the age of twenty, had audaciously inserted ourselves into that glorious, historic moment.

That astonishing sight had clearly given everyone a fresh shock.

Some people had nodded, acknowledging the ability and qualifications of those two young punks. Others seemed to have found it extremely irritating.

*The Zhongnan Sect, for example.*

I couldn’t be certain, but by now the Zhongnan Sect’s guts were probably twisted with resentment.

After all, the Jin Family of Taiyuan and I, who had been locked in a bad relationship with them for so long, had begun rising rapidly.

The bad blood had started with the Three Hands of Zhongnan, the three idiots of the Zhongnan Sect. It had worsened when the Roaring Fury Swordsman came to the Jin Family of Taiyuan’s New Year’s Day banquet and caused a scene, only to be beaten by Jeok Cheongang like a dog on the hottest day of summer.

And that wasn’t all. The feud had reached its peak when the Taeeul Merciless Sword, regarded alongside the Sect Leader Wind-and-Cloud Sword Lord as the Zhongnan Sect’s greatest master, was defeated by me.

After suffering such humiliation, they must have ground their teeth at the sight of me receiving attention.

For all I knew, they might be somewhere right now biting, tearing, and chewing on me, the Jin Family of Taiyuan, and Jeok Cheongang.

Given the personalities of the Zhongnan Sect’s people I had seen so far, I could almost believe it if they joined hands with Dark Heaven.

*Hey, Zhongnan Sect.*

*Dark Heaven, come on in.*

*The Murim Alliance was born. Why do you all look so miserable?*

*Jin Taekyung is pissing us off. That fucking brat.*

*Ho ho ho. Want a hit of a Temporary Strength Pill?*

*Sure. Roll me one.*

I could picture it perfectly. I really could.

Still, they belonged to one of the Nine Sects and One Gang and were a venerable orthodox sect. Surely they wouldn’t actually be insane enough to join hands with Dark Heaven.

But they were certain to interfere at every turn in one way or another.

*No, but this is unfair. Why is everyone swarming me?*

At that thought, I looked toward the freeloader—or rather, the dumpling grub—fidgeting in a corner with Mimi-chan.

“Why, Benefactor?”

“Good heavens, the bug talks.”

“Pardon?”

“Nothing. But Young Hero Cheong, why do you look so free? No one comes to see you.”

“I don’t meet people when I’m full. I don’t meet them if they don’t bring delicious food either.”

After thinking for a moment, I asked again.

“You’re always full.”

“Yes. So I don’t meet anyone.”

“……Right.”

*Must be nice to have such an easy life.*

If I had to pick the person in all Murim who gave the fewest fucks and did exactly as he pleased, wouldn’t it be Cheongpung?

Even on the day of the Mount Song Resolution, he had bounced around excitedly because it was his first time raising the Murim Alliance’s flag.

*Is he a genius or a lunatic?*

Probably both. Hmm.

I was muttering that to myself when Cheongpung yawned and opened his mouth.

“And I’m not free. I’m training right now.”

“What fresh bullshit is this?”

“I’m serious. Look.”

Cheongpung took the Thousand-Year Poison Horned Snake, Mimi, off his shoulder and began squirming while still seated.

“……Sorry to interrupt, but are you evolving into a bug?”

“No. It’s martial arts.”

“Martial arts?”

“Yes. I made it after watching Mimi’s movements.”

Then why did it look absolutely nothing like martial arts?

I asked with complete sincerity.

“Is the name of this martial art something like Squirming or Toughening Up?”

“No. It’s a footwork technique.”

“……Then you should stand up and do it, you idiot.”

“Oh, right. I forgot.”

Did I really have to tell him that?

While I was briefly rendered speechless, Cheongpung promptly rose from his seat and took a step.

Or rather, the moment I felt him take a step, his figure disappeared.

Whoosh!

With only the faintest sound, Cheongpung reached the far end of the spacious room. He showed his teeth in a bright grin.

“Ta-da. What do you think?”

“……!”

*What did I just see?*

Goose bumps raced up my back.

It was a ghostlike movement—or rather, the movement of a snake. It was clearly a footwork technique, but it was not like any footwork technique I had ever seen.

Cheongpung hadn’t walked. He had slid.

And he had done it at a speed so fast that even I could barely track him with my naked eyes.

“I mixed Mimi’s movements with bits and pieces of different martial arts. When I move like this, I feel as if I’ve become Mimi too, so it makes me happy!”

“……You mixed them?”

“Yes. The name is Mimi Step! Would you like to learn it too, Benefactor?”

*He really is insane.*

In more ways than one.

I stared at Cheongpung with my mouth hanging open, then shook my head.

“No. I don’t want to.”

“Aww……”

Just as Cheongpung’s shoulders drooped, Hyuk Mujin’s voice came from outside the door.

“Captain. There’s a visitor here.”

*A visitor? Was there anyone else left who could come see me?*
## Chapter artifact 528

# Chapter 528

Creak.

It didn’t take long to realize who the uninvited guest was.

The moment I saw the familiar face open the door and walk in, I spoke without hesitation.

“Hey, Hyuk Mujin. Who told you to let a beggar in?”

“Have you been well—this damn bastard has quite the mouth on him.”

Gung Gibang, who had been grinning brightly despite his grimy face, scowled.

“I went out of my way to make time for you, and this is how you greet me?”

“I called a beggar a beggar. What’s the problem?”

“Don’t you ever think about how the beggar feels hearing that?”

“No. Not for a single second.”

“……You’re worse than a scorpion. One day, you’ll find yourself surrounded by a hundred thousand Beggars’ Sect disciples and beaten half to death.”

I shrugged.

“Not likely. I happen to be a pretty valuable asset to the Murim Alliance.”

“I swear on my begging bowl that when the time comes, you’ll be the first one I beat senseless.”

“That works too. It’ll mean the war is over by then.”

“You mean that?”

“Yeah. Promise.”

Gung Gibang glared at me in silence. Then the tension left his eyes, and a faint smile appeared at the corners of his mouth.

“Damn it. The war has barely begun, and I already want it to be over.”

“What, because you want to beat me up?”

Gung Gibang gave a quiet laugh and shook his head.

“I may be destined to beg for the rest of my life, but I’m not stupid enough to think that way. No matter what, war must never happen.”

“You could distinguish yourself in battle and become a hero.”

“What would a beggar like me do with being a hero?”

“Oh.”

That was a wise answer to a stupid question.

I had asked because I genuinely wanted to know what he thought, but I applauded him sincerely.

Clap, clap, clap.

“What are you doing?”

“Nothing. I was just thinking our Gibang has really grown up. You’re even having thoughts like that now.”

“……How the hell do you see me? And you’re younger than me, yet you’re unbelievably shameless.”

“If simply getting older made people mature, the world would be a much better place. Time passes without anyone having to make an effort.”

In that sense, Gung Gibang’s thinking really was remarkably sound for someone his age in Murim.

This wasn’t the modern world of the twenty-first century. This was Murim, where the primal law of the jungle held sway.

It was best not to entertain the softheaded notion that every martial artist filling Henan had joined the Murim Alliance solely out of a sense of chivalry.

*Especially the younger ones.*

They were at the age when their blood was running hottest, after all.

Actually, even middle-aged martial artists nearing forty weren’t all that different. To them, the Great Faction War was merely a trace of the past that had happened before they were born.

Among generations that had never experienced war, plenty of people dreamed less of chivalry than of distinguishing themselves and becoming heroes.

That included not only wandering martial artists who acted as though they lived only for today, but also disciples of the great sects and great families collectively known as prestigious major factions.

*The era is what it is, and Murim’s social climate doesn’t leave them much choice……*

But no matter how favorably I tried to look at them, they could only appear to me as fucking idiots.

It felt like a godsend that there were more people joining the Murim Alliance out of chivalry than idiots like that.

*Come to think of it, the people around me are pretty normal too. Hmm.*

Just then, Cheongpung’s figure slid forward like a snake and suddenly appeared in front of Gung Gibang.

Ssss—

“Agh! What the fuck?!”

“Hehe. This is the new footwork technique I made, Mimi Step. It really looks like Mimi, doesn’t it?”

“Like Mimi, my ass. It looks like a dog! Like a damn beggar!”

At Gung Gibang’s shriek, Hyuk Mujin spoke with the happiest expression in the world.

“Young Hero Cheongpung, could you do that one more time later?”

“Wow! Of course! Absolutely!”

“Absolutely not! Don’t do it!”

“……”

Normal, my ass.

It wasn’t easy to gather this many people in one place and have them look this fucking stupid.

*Ah, my head hurts.*

Rubbing my throbbing temple, I asked the question I had set aside for a moment.

“Anyway, why are you here?”

Gung Gibang glanced warily at Cheongpung before answering.

“There are a few people who want to meet you and Young Hero Cheongpung. I thought I’d stop by and ask, just in case.”

“Of course there are plenty of people who want to meet me.”

“……You’re obnoxious, but I can’t exactly argue with that.”

“So who are these people who want to meet me?”

Gung Gibang sighed before continuing.

“The Ten Dragons and Phoenixes.”

“If you mean the Ten Dragons and Phoenixes……”

“They’re the Ten Dragons and Phoenixes you know. They’re not all here—about half of them.”

Well, of course they were those Ten Dragons and Phoenixes. Was there another group with the same name?

The moment I heard those three words, I had already made up my mind. I answered without the slightest hesitation.

“No. What am I supposed to do meeting them?”

“Build a relationship. It can’t hurt for young prodigies to maintain a close relationship with one another.”

“It doesn’t seem like it would help much either. And don’t call me a young prodigy. It’d be a mistake to put me in the same class as you people.”

Gung Gibang’s face filled with disbelief.

“……How can you say something so offensive with such confidence?”

“Because it’s something everyone knows.”

“No, that’s true, but…… Damn it. Fine. What about Young Hero Cheongpung?”

Having realized that he had no chance of persuading me, Gung Gibang quickly shifted his target.

Sssssss—

Cheongpung had been closely observing Mimi, the Thousand-Year Poison Horned Snake, who had somehow turned into a giant snake while drawing everyone’s attention. Without even turning around, he answered.

“Hmm. I don’t want to go.”

“They prepared a lavish feast especially for you.”

“I ate dumplings earlier, so I’m full. I don’t think I would’ve gone even if I were hungry.”

“They can pack it up for you. You can eat it when you’re hungry.”

“I don’t know. I haven’t had much of an appetite lately.”

“What—what did you say?”

Gung Gibang stared at him with his eyes bulging, as if he had just been stabbed.

No, Hyuk Mujin and I were just as shocked.

*What the hell? Is he really insane?*

*Captain, did I hear that wrong?*

*No. You heard him correctly. He said he has no appetite.*

*That bastard isn’t Young Hero Cheongpung. He’s definitely a Dark Heaven spy.*

*……That’s disturbingly plausible!*

An inaudible conversation passed between us through our gazes in midair.

That was how shocking Cheongpung’s sudden statement was to everyone.

*Of all people, Cheongpung says he has no appetite?*

It was news as astonishing as the founding of the New Murim Alliance. Yet Cheongpung didn’t so much as flinch beneath the astonished stares of everyone around him.

“Anyway, I’m fine. You go ahead, Benefactor.”

“Huh? Uh, no. I’m not going either.”

“Really? Hehe. Then I’ll finish what I was doing. I think there are a few things I need to improve in Mimi Step.”

I had no idea why he was acting like that, but one thing was certain.

As time passed and the circumstances around him changed, some kind of change had begun in Cheongpung as well.

*That guy……*

I stared at Cheongpung in silence, then turned toward Gung Gibang.

“Anyway, you should get going.”

“Hmm. I suppose I should. We talked so long that I’m late for the time we agreed on.”

Gung Gibang glanced at Cheongpung, still looking stunned, then turned away and muttered.

“They’ll be pretty disappointed. Young Lady Ju in particular seemed terribly excited.”

“Why would she be disappointed? I’ve already met some of the Ten Dragons and Phoenixes at the Star-Array Grand Banquet, and sooner or later we’ll run into the others again while passing by—”

I stopped in the middle of my blunt reply.

The last thing Gung Gibang had said filled my mind.

“Wait. Who?”

“Huh? What are you talking about?”

“No, I thought I heard you say that someone was especially excited.”

“Oh. Young Lady Ju?”

That was right. I hadn’t misheard him.

“Could you mean, by any chance, that Young Lady Ju……?”

“Of course I mean the Young Lady Ju you know. Young Lady Ju Hwaran, the Young Bureau Head of the Yongbong Escort Bureau—the Dagger Hidden Flower.”

“……!”

A single memory suddenly surfaced in my mind.

By Murim reckoning, it had happened only two or three months ago, yet for some reason, it felt impossibly distant.

Ironically, it was also one of the clearest memories left behind by all that time.

*The moon is especially bright tonight.*

Yes. The moon had been unusually bright that night.

Or perhaps it hadn’t been the moon that was truly bright. Perhaps it had been someone’s face.

I hadn’t been looking at the moon then.

*Great Hero Jin.*

*Yes, Young Lady Ju.*

*Do you think I can do it?*

It felt as though one person’s damp, desolate voice, drifting through the flower-filled garden, were echoing in my ears.

What had I said to her back then?

I thought for a moment before muttering blankly,

“……It’s all right even if you can’t.”

“What? What’s all right?”

I suddenly came to my senses.

The soft moonlight, the scent of flowers, and the voice had vanished. Even the face that had been flickering before my eyes dissolved.

When I looked up, the only thing in front of me was Gung Gibang wearing a puzzled expression.

A small sigh escaped me before I realized it.

“Gibang.”

“Hmm?”

“Why are you so ugly?”

“……?”

“I’m sorry, but I mean it. Actually, I don’t think I’m all that sorry. Things were going so well.”

Gung Gibang’s ugly face twisted violently.

“You bastard, you’ve been at it since earlier—”

“Enough.”

I cut him off with a shake of my head.

“Let’s go.”

“What?”

“Stop asking questions and let’s go meet those Ten Dragons and Phoenixes or whatever. Hearing about the feast suddenly made me hungry.”

“Uh, uh-huh?”

Gung Gibang blinked, having forgotten to be angry, then hurriedly nodded.

“Uh-huh. All right, then. They’ll all be happy to see you.”

It didn’t particularly matter who welcomed me.

It was just…… well, how should I put it?

*I just felt like seeing her after all this time.*

That was all. Besides, I had every legitimate reason to go, since I had something to thank her for concerning Jeok Cheongang.

*It’s only natural, if I’m a decent human being. It’s only natural.*

Muttering that to myself, I started walking. Gung Gibang’s shout that he was coming with me rang noisily from behind.

* * *

The three-story inn was large and ornate. Its scale and prices were enough to keep out anyone without a fair bit of money, and in reality, that was exactly how it was.

By the same token, the status of the three men and one woman occupying a window seat on the inn’s top floor was likewise anything but ordinary.

“Young Lady Ju, allow me to pour you a drink.”

“Now, now. Young Lady doesn’t care much for alcohol. Isn’t that right, Young Lady Ju?”

The handsome men, dressed in gleaming silk martial uniforms and hero headbands, had no idea what the woman before them was thinking.

*When is he coming?*

The words being thrown around her no longer reached her ears.

She didn’t know when it had begun, but her body, which had been leaning against the back of her chair, had gradually tilted toward the window. Her eyes kept sweeping restlessly between the half-open window and the stairs.

*Young Hero Gung made such a bold promise. Should I go out and see for myself?*

And just as all those worries and thoughts began chasing one another in endless circles—

Jingle.

The bell above the inn’s door rang as it opened, and Ju Hwaran sprang to her feet.
## Chapter artifact 529

# Chapter 529

Jingle.

“Welcome!”

The inn attendant’s energetic cry came with the ringing of the bell above the opening door.

Ju Hwaran sprang to her feet in hopeful anticipation, but disappointment quickly filled her eyes.

“Ah……”

It wasn’t him. She couldn’t make out the person’s face properly from the angle above, but that alone was enough to tell.

No, if it had really been him, she might have recognized him from his shadow alone.

*It wasn’t him. That person wasn’t here.*

Hwaran let out a quiet sigh and looked down at the first floor once more, her eyes filled with regret.

Nothing would change just because she kept looking, yet for some reason, she couldn’t let go of her disappointment.

The men seated with her cleared their throats at the sight.

“Ahem.”

“Ahem.”

They had been paying close attention to Hwaran’s every movement from the very beginning.

They weren’t stupid enough not to understand what her actions meant.

Three men sat across the table from Hwaran. Among them, two exchanged glances that tangled in midair.

And it wasn’t only their eyes that communicated. Their lips twitched faintly as discreet Sound Transmission passed between them.

—Fellow Daoist Hwangbo. Who do you think Young Lady Ju is waiting for?

The handsome man in spotless white clothes and with clear skin was Baek Woo, the Kunlun Cloud Dragon—a universally acknowledged number-one young prodigy of the Kunlun Sect and one of the Ten Dragons and Phoenixes.

At his Sound Transmission, the beautiful young man with a sharp nose slightly furrowed his brow.

—No idea.

—I can think of only one person. If my guess is correct, then it must be the Blazing Flame Divine Dragon, Jin Tae—

—Drop it.

Hwangbo Ak, the beautiful young man who had coldly cut him off, was the Lesser Family Head of the Hwangbo Family and another member of the Ten Dragons and Phoenixes.

He was in a terrible mood.

*How dare I, Hwangbo Ak, be treated as though I’m inferior to some other bastard.*

It was impossible. And for someone as self-obsessed as Hwangbo Ak, it was a reality he found especially difficult to accept.

Although the Hwangbo Family was not one of the Five Great Families, the name carried considerable influence throughout the Murim.

No one could dispute that it was a deeply rooted martial family and the long-standing hegemon of the Shandong region.

Hwangbo Ak was the Lesser Family Head of that very family.

On top of that, he possessed exceptional martial talent worthy of the name Ten Dragons and Phoenixes, and he was a handsome man who would shine wherever he went.

An excellent family. Immense wealth and prestige. A handsome face as well.

It was only natural that his popularity among women had soared to the heavens.

But the greatest problem was that all the things Hwangbo Ak had enjoyed throughout his life, now approaching thirty, felt meaningless at this very moment.

*The Dagger Hidden Flower, Ju Hwaran.*

The instant he first saw her, Hwangbo Ak realized that all the countless beautiful women he had met until now had been nothing more than fireflies before the sun.

Unlike other women, her face was entirely free of makeup, yet an indescribable beauty radiated from it. And the plain-colored martial uniform she wore seemed more refined than any ornate court dress.

He had fallen in love at first sight.

*Why couldn’t I have met a woman like her sooner?*

Hwangbo Ak stared at Ju Hwaran as though entranced.

His heart fluttered at each of her small movements. Her eyes sparkled like morning stars, and the desire hidden deep inside him stirred.

But then……

“Phew.”

Hwaran’s sigh, heavy with regret, made his brow crease.

He already knew what emotion that sigh contained—and whom it was directed toward.

*The Blazing Flame Divine Dragon, Jin Taekyung.*

He silently repeated the epithet and name in his mind.

His hand, resting beneath the table, clenched on its own.

*What does that nobody have that I don’t?*

Hwangbo Ak had already heard about the connection between Ju Hwaran and Jin Taekyung.

The details of what had happened between the Yongbong Escort Bureau and the Zhongnan Sect two months earlier had not become widely known.

But the shocking news that the Taeeul Merciless Sword, one of the Zhongnan Sect’s three greatest masters, had knelt before a young prodigy who had only just passed twenty had already swept through the Murim.

*It’s impossible.*

It was something that could not and should not have happened. Hwangbo Ak had dismissed it as a ridiculous rumor and clicked his tongue.

But more important than that was his unpleasant suspicion that the incident had caused Hwaran to develop feelings for Jin Taekyung.

—Are you certain?

Baek Woo’s sudden Sound Transmission made him prick up his ears.

—Hm?

—I asked whether what you said earlier was certain. The Blazing Flame Divine Dragon, Jin Taekyung. Is the person Young Lady Ju is waiting for really that bastard?

—Then do you think she’s waiting for the Successor Beggar?

—……

Even Hwangbo Ak had to admit that was unlikely.

No matter how peculiar her tastes were, Ju Hwaran could not possibly like Gung Gibang, who filled the air with the reek of stale dog food just by sitting nearby.

—So you really mean it’s that bastard? Are you saying this Young Master is inferior to a worm that crawled out of some backwater corner of Shanxi Province?

—Not a worm. A Divine Dragon. And Shanxi Province is no longer a backwater corner. It is the hidden residence from which the dragon named Jin Taekyung rose, as well as the center of the trade routes running through northern Gaoyuan.

Baek Woo lightly corrected Hwangbo Ak before continuing.

—Fellow Daoist Hwangbo. The Jin Family of Taiyuan you knew in the past is no more. In fact, now that we’re talking about it, I knew it long ago, from the moment I saw that fellow, the Heaven Shaking Sword.

—The Heaven Shaking Sword? Heaven Shaking Sword Jin Mukyung?

—Do you know another Heaven Shaking Sword?

Hwangbo Ak’s eyebrows trembled.

If Ju Hwaran, who kept sighing across the table, and that young escort who looked like he had crawled in from who knew where had not been watching him, he would have scowled long ago.

—Don’t bring up that name. Do you think I’m asking because I don’t know who that bastard is?

—Ah, now that you mention it, you and the Heaven Shaking Sword were at Heaven’s Gate Temple together—

—Enough. Stop!

—Good heavens. All right. Why are you shouting?

Hwangbo Ak’s tightly clenched fist had turned red.

Jin Mukyung was one of the names Hwangbo Ak would never be able to forget, even until the day he died.

That man had made Hwangbo Ak, who believed he possessed everything, feel an insurmountable wall—and had given him a tremendous humiliation at the same time.

*Damn it.*

And now, after the older brother, the younger brother was blocking Hwangbo Ak’s path too.

Seeing the faint anger showing on Hwangbo Ak’s face, Baek Woo cautiously moved his lips.

—Fellow Daoist Hwangbo. May I offer you one piece of advice?

—What now?

—You remember what you said to me. If the Blazing Flame Divine Dragon comes, don’t ever mention it out loud. No—don’t even move your lips.

—Hmph. Are you worried there might be a fight?

—No, that’s not it. I’m worried I might get dragged into it too.

—……What?

Baek Woo gazed at Hwangbo Ak with deep concern and sympathy.

—If you want to die, die alone.

—……!

—You were in closed-door training at your family’s estate during the Star-Array Grand Banquet, so you probably don’t know. But even now, whenever I think about that man, I feel—ugh. Anyway, keep that in mind. Understood?

What in the world was he talking about? Die alone?

Hwangbo Ak remained silent for a moment, staring at Baek Woo in disbelief. Then he sent another Sound Transmission.

—Are you…… serious?

—Infinite Life Buddha. I swear before the Primordial Heavenly Venerable that I’m completely serious.

—Don’t you have any pride as a martial artist?

—That disappeared during the Star-Array Grand Banquet. Do you know what it feels like to have the top of your head stepped on even after using the Cloud-Dragon Eight Forms?

—That’s going too far!

—No matter how you look at it, it’s impossible. That man is a monster.

—W-What happened to the Kunlun Cloud Dragon who was like one lofty crane? Where did the Baek Woo I knew go?

Baek Woo gazed into the past with a nostalgic look in his eyes.

—Come to think of it, the Successor Beggar said something similar to me back then. Then, in the very next test, he was beaten like a dog by Jin Taekyung. You heard what happened, didn’t you? Gung Gibang fell behind in movement technique, his eyes rolled back, and he tried to grab Jin Taekyung by the hair. He nearly got his head knocked off.

—……!

—Infinite Life Buddha. Let’s be blunt. Do you really think everything the Blazing Flame Divine Dragon showed us was nothing but a rumor?

—Of course!

At Hwangbo Ak’s firm answer, Baek Woo let out a quiet sigh.

—Why?

—How could a person do such things? It’s obvious that his master, the Fire King, solved everything and gave the credit to his Disciple!

—True. If you look at it with common sense, it doesn’t make sense. How could anyone reach Supreme Peak at barely twenty?

At last, Hwangbo Ak heard a normal answer. He nodded with a look of certainty.

—That is exactly what I’m saying. His master, the Fire King Jeok Cheongang, must have stepped in and given the credit to his Disciple.

—I’m saying this again because I’m worried about you: don’t tell the Blazing Flame Divine Dragon that his master handed him the credit. I don’t want to be paired with you as a battle partner and have my face beaten in.

—……What exactly are you trying to do?

—Infinite Life Buddha. It’s simple. Don’t try to reason it out with common sense. Don’t even try to understand it. Just accept it.

For a moment, Hwangbo Ak was speechless at Baek Woo’s almost enlightened tone. Then he changed his approach.

—W-Wait. You have feelings for Young Lady Ju too, don’t you?

—Young Lady Ju? Of course I like her. How could any man not be attracted to her?

—That very Young Lady Ju has feelings for Jin Taekyung. And you still intend to protect your rival?

—My life is more important than Young Lady Ju. My hair is, too.

—What?

Baek Woo glanced around to see whether anyone was watching, then casually lowered his head.

Between his neatly arranged hair, his strangely bare crown stood out.

—Infinite Life Buddha. Do you see it?

—No, what the hell—

Hwangbo Ak could not finish his Sound Transmission. Baek Woo gave him a sorrowful smile.

—My hair stopped growing after my head was stepped on during the Star-Array Grand Banquet……

—……!

—Give up. Giving up makes life easier. But if you absolutely can’t give up, please do it when I’m not around. I’d like to live, too.

What kind of insane nonsense was this?

Hwangbo Ak swallowed dryly.

He was still just as angry, but the chill running down his spine was impossible to ignore. Baek Woo had been his friend for a long time and was a martial artist with a strong sense of pride. If even he was speaking like this, then—

*Is this for real?*

Hwangbo Ak had never once believed that every rumor surrounding the Blazing Flame Divine Dragon was true.

But if, just for argument’s sake, every one of those rumors really was true without a shred of falsehood……

*An inhuman monster.*

Yes. A monster beyond any doubt.

And at the same time, an unbearable humiliation wrapped itself around Hwangbo Ak’s entire body.

*How the hell could this happen?*

His fist tightened. A pained groan slipped through his parted teeth, and Ju Hwaran, sensing the unusual atmosphere, spoke.

“Young Hero Hwangbo. Is something wrong?”

“Ah, no. It’s nothing.”

At Hwangbo Ak’s forced answer, the young escort who had been sitting there doing nothing but taking up space gave a quiet laugh.

“You look very much like something’s wrong.”

“……I said it was nothing.”

“If you say so. In any case, the food here is delicious.”

Hwangbo Ak’s eyes narrowed.

From his behavior to the way he spoke, there was nothing Hwangbo Ak liked about the man. Hwangbo Ak had allowed him to sit with them only because he was Young Lady Ju’s escort, but every little thing about him irritated Hwangbo Ak.

A mutter slipped through his twisted lips.

“This is the problem with lowborn rabble……”

Ju Hwaran was not a fool. A cold chill passed over her beautiful face, which had been filled with troubled thoughts only a moment earlier.

“Young Hero Hwangbo.”

“Ah, I’m only saying this in case Young Lady Ju misunderstands. I wasn’t talking about that fellow.”

Hwangbo Ak put on a fabricated smile and pointed toward a table some distance away.

“I was talking about those bastards who practice demonic, heterodox arts over there.”

And at the moment his voice, neither loud nor soft, rang through the inn—

Scrape.

Someone rose from their seat.

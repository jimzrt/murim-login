# Checkpoint Review — 490–494

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

# Chapters 490–494

## Plot

Mungyeong begins testing Jin Taekyung without warning, using poisoned water, hidden weapons, candy, and concealed attacks. Taekyung survives Potent Paralysis Powder, Potent Soul-Bewitching Powder, Potent Energy-Dispersing Poison, and Potent Seven-Step Soul-Chasing Powder through the Myriad-Poison Ring and Scorching Yang Qi, but the final detoxification permanently reduces his Strength and Agility by five points through Sinews and Meridians damage. Mungyeong reveals that these trials are part of Taekyung’s training and intends to correct his complacency before teaching him secret martial arts, without forming a formal Master-Disciple relationship.

Meanwhile, Jeok Cheongang withdraws from the group and orders them not to search for him until the Water God Dragon’s affairs are complete. Taekyung, Hyeongong, Zhuge Feng, Mungyeong, Gung Gibang, Cheongpung, and others travel to the corpse. They honor the divine creature’s sacrifice, then negotiate over its priceless scales and bones. Taekyung prevents Zhuge Feng from claiming an excessive share and persuades Wudang to help dismantle the body. Cheongpung and Hyeongong cut apart the enormous corpse, while Mungyeong watches Murim’s reverence turn into avarice.

## Continuity

- Mungyeong is the Slaughter Saint, formerly Killing Ghost and later the Divine Physician. He recognizes Taekyung’s innate Heavenly Martial Physique and is testing him through escalating poisons and ambushes.
- Taekyung detoxified Potent Seven-Step Soul-Chasing Powder, but permanent Sinews and Meridians damage reduced Strength and Agility by 5 each. Severe Stomachache was temporary.
- Mungyeong will teach Taekyung secret martial arts without becoming his formal master; the Fake Murim Martial Artist Quest remains accepted and in progress.
- Jeok Cheongang’s innate qi is damaged and steadily diminishing despite treatment. He has disappeared from the expedition and instructed the others not to find him until the Water God Dragon’s matters are finished.
- The Water God Dragon’s spirit has departed, but its enormous corpse is being dismantled and distributed under Taekyung’s direction. Its sacrifice prevented a greater catastrophe in Hubei Province.
- The functionally crippled Gate still leaks faint mana and demonic qi. Its residual mana mutated local life, while the Water God Dragon absorbed the Gate’s mana.
- About one hundred Level 5 Mutated Minnows, locally called Blood Fish, have been captured; the remaining population and the full spread of the mutation are unknown.
- Taekyung believes Dark Heaven’s regeneration, Teleport, and Moving Formation are forms of Magic connected to the Gate. He has told Jeok that he came from another world and that a dangerous force from it is linked to Dark Heaven.
- Honglan, the Southern Heaven Demon Empress, corrupted the Dongting Lake imugi and is traveling toward Yunnan. Her objective remains unknown.
- The severely injured Dongting Fisherman’s exact connection to Dark Heaven and the destruction of the secret refuge remains unresolved.
- Open hooks: the Gate’s destination and lost functions; the Lord of Heaven’s identity; Honglan’s plans in Yunnan; the Dongting Fisherman’s role; and Mungyeong’s remaining trials and martial arts instruction.

## Translation Decisions

- Retain **secret martial arts**, **Master-Disciple relationship**, **Killing Ghost**, **Fake Murim Martial Artist**, and **Agh** in the Quest interface.
- Render **강력한 마비산** as **Potent Paralysis Powder**, **강력한 미혼산** as **Potent Soul-Bewitching Powder**, **산공독** as **Energy-Dispersing Poison**, **강력한 산공독** as **Potent Energy-Dispersing Poison**, **칠보추혼산** as **Seven-Step Soul-Chasing Powder**, **강력한 칠보추혼산** as **Potent Seven-Step Soul-Chasing Powder**, and **심각한 복통** as **Severe Stomachache**.
- Retain **Memory Fragment**, **Gate Conquest**, **Teleport**, **Magic**, **Blood Fish**, **Mutated Minnow**, **Poison Absorption**, and **Detoxification**.
- Retain **Water God Dragon**, **Dark Heaven**, **Gate**, **Force**, **Sword Energy**, **Hellfire**, **Water Breath**, **Old Master**, and **sea of corpses and blood**.
- Render **선천지기** as **innate qi**, **진원진기** as **true-origin qi**, **천기** as **heavenly patterns**, **심마** as **Heart Demon**, **비급** as **martial arts manual**, **반로환동** as **Returned to Youth**, **기막** as **qi curtain**, **무극태을검** as **Martial Extremity Grand Unity Sword**, and **이룡** as **Two Dragons**.
- Preserve **Pine-Pattern Ancient Sword**, **Taiji Wisdom Sword**, **White Flame**, **Dog-Beating Staff**, **Azure Dragon**, **Infinite Life Buddha**, **Ganggangsullae**, **Book of Life and Death**, and **shichen**.
- Preserve Taekyung’s profane contemporary humor, Jeok’s blunt violence, Cheongpung’s literal innocence, Hyeongong’s martial pride, and Mungyeong’s calm coercive authority.

## Durable state

{
  "active_continuity": [
    "The functionally crippled Gate continues leaking faint mana; its residual mana is mutating local life, and the Water God Dragon absorbed all of that mana.",
    "Around one hundred Level 5 Mutated Minnows, locally called Blood Fish, have been captured in the Gate's entrance waterways; the remaining population is unknown, and the fish fight and kill one another.",
    "Taekyung suspects Dark Heaven's regeneration, teleportation, and Moving Formation are manifestations of Magic connected to the Gate.",
    "Taekyung told Jeok that he came from another world, that an evil force from it is linked to Dark Heaven, that the corrupted imugi was their work, and that a fully opened Gate could release monsters.",
    "Honglan corrupted the benevolent Dongting Lake imugi and used it to kill many people; the severely injured Dongting Fisherman may be connected to Dark Heaven and the earlier destruction inside the secret refuge.",
    "The Southern Heaven Demon Empress is traveling toward Yunnan and expects to cause further deaths.",
    "Jin Wikyung and Gung Gibang pledged the Jin Family of Taiyuan and the Beggars' Sect to Taekyung's defense.",
    "Jeok's innate qi is damaged and steadily diminishing despite the Thousand-Year Snow Ginseng and the Divine Physician's treatment, and he has withdrawn from the Water God Dragon expedition.",
    "Mungyeong is the Slaughter Saint, a Returned to Youth Supreme Peak master and the greatest assassin in history; before becoming the Slaughter Saint, he was called Killing Ghost, and he saved countless people as the Divine Physician.",
    "Mungyeong recognizes Taekyung's Heavenly Martial Physique as innate and distinct from Cheongpung's more refined physique.",
    "Mungyeong is testing Taekyung through successive poisoned traps and concealed attacks, intending to teach secret martial arts without a formal Master-Disciple relationship and to correct Taekyung's complacency.",
    "Taekyung detoxified Potent Seven-Step Soul-Chasing Powder, but Sinews and Meridians damage permanently reduced Strength and Agility by 5 each; the Water God Dragon's corpse is being dismantled under Taekyung's direction."
  ],
  "continuity_sources": [
    494,
    493
  ],
  "open_questions": [
    "What lies beyond the exposed Gate, why has it lost most of its functions, and how far has its residual mana's mutation spread?",
    "What is the Lord of Heaven's identity, and how is he connected to the dangerous force Taekyung associates with his original world?",
    "Where is the Southern Heaven Demon Empress ultimately headed, and what does she intend to do in Yunnan?",
    "What is the Dongting Fisherman's exact role within Dark Heaven, and how was he connected to the earlier destruction inside the secret refuge?",
    "What further poison tests will Mungyeong impose on Taekyung, and what secret martial arts will he teach him?"
  ],
  "safe_through": 494,
  "temporary_decisions": [
    "Render 산공독 as Energy-Dispersing Poison, 강력한 산공독 as Potent Energy-Dispersing Poison, 칠보추혼산 as Seven-Step Soul-Chasing Powder, 강력한 칠보추혼산 as Potent Seven-Step Soul-Chasing Powder, 심각한 복통 as Severe Stomachache, 고기 방패 as Meat Shield, 독 장아찌 as Poisoned Pickle, and 독의 as Poison Physician; retain secret martial arts, Master-Disciple relationship, Killing Ghost, and Fake Murim Martial Artist, and preserve 악 as Agh in the Quest interface.",
    "Render 기억의 파편 as Memory Fragment, 게이트 공략 as Gate Conquest, 텔레포트 as Teleport, 마법 as Magic, 혈어 as Blood Fish, and 변이된 송사리 as Mutated Minnow; render 강력한 마비산 as Potent Paralysis Powder, 강력한 미혼산 as Potent Soul-Bewitching Powder, 전신 마비 as Full-Body Paralysis, 독성 흡수 as Poison Absorption, and 해독 as Detoxification.",
    "Render 시산혈해 as sea of corpses and blood and retain Old Master for 노야 with the established rough, profane Taekyung-Jeok banter; render 해시 as hour of the Pig, 한 식경 as half an hour, 타구봉 as Dog-Beating Staff, 창룡 as Azure Dragon, and 무량수불 as Infinite Life Buddha.",
    "Render 선천지기 as innate qi, 진원진기 as true-origin qi, and 천기 as heavenly patterns.",
    "Render 심마 as Heart Demon, 비급 as martial arts manual, 송문고검 as Pine-Pattern Ancient Sword, 반로환동 as Returned to Youth, 강강수월래 as Ganggangsullae, 생사부 as Book of Life and Death, 기막 as qi curtain, 무극태을검 as Martial Extremity Grand Unity Sword, and 이룡 as Two Dragons."
  ],
  "version": 1
}

## Reading copies

## Chapter artifact 490

# Chapter 490

“So, did you finish your conversation?”

The Wudang Daoists returned exactly half an hour later, just as they had said they would.

I still had plenty of questions, and I wanted to move somewhere else and keep talking. Mungyeong, however, had other ideas.

“We’re done. Go back.”

“…What? We’re done? You haven’t even told me what kind of training this is!”

“You’ll naturally find out tomorrow.”

“It’s already the hour of the Pig.[^1] It’ll be midnight soon. Can’t you just tell me and get it over with?”

“It’s late. Don’t forget. We begin tomorrow.”

“No, wait.”

“Wait?”

*Shhk.*

I alternated my gaze between the short sword rising slightly from his sleeve and Mungyeong, then pointed beyond him into the darkness with a stiff expression.

“I mean over there. You can go that way.”

“…”

“Just keep going straight, then turn right.”

“It seems that wasn’t what you were trying to say.”

“I thought you might not know, so I figured I’d better make sure. Hehe.”

“I know. Shut up and get lost.”

“Yes, sir. Have a peaceful night.”

A little while later, after confirming that Mungyeong’s back had completely disappeared from sight, I muttered under my breath.

“Goddammit…”

One mountain after another.

Just when I thought I had finally gotten used to Jeok Cheongang’s methods, now I had to start worrying about the Slaughter Saint’s mood too.

My eyes were already going dark just thinking about the hardships waiting ahead.

*Actually, the Old Master is much better.*

Leaving aside the intensity of his training, Jeok Cheongang at least told me what kind of training I would be doing.

His temper might have been as hot as fire, but he had still prepared something resembling a curriculum.

*But what kind of training is so secret that he won’t even tell me?*

There was a simple reason I was so curious. The Quest I had accepted by accident didn’t contain any information either.

*Quest window, open.*

*Ding.*



> **System**
>
> **Quest**
>
> **Fake Murim Martial Artist**
>
> Mungyeong sensed the war clouds that will soon hang over the world and, after careful consideration, decided to teach you personally.
>
> However, everything requires a period of preparation.
>
> Before passing down his secret martial arts, Mungyeong will test you through various methods.
>
> When this first test ends is up to you.
>
> **Grade:** None
>
> **Restriction:** Jin Taekyung
>
> **Mission:** Earn Mungyeong’s recognition *(Incomplete)*
>
> **Reward:** ???
>
> **Failure:** ???

I looked at the Quest window two or three more times, but it remained unchanged.

Compared to the training Quest at Mount Jiuhua, where the objective had been clearly stated, this was nothing but vague nonsense.

*Earn Mungyeong’s recognition.*

At this point, I would rather run around with iron balls hanging from me. At least then I would have a clear objective and be able to check my progress.

But this was basically the crime of getting on someone’s bad side.

Didn’t it mean I had to keep getting put through the wringer until he decided he liked me?

*This feels like it’ll take a while.*

I didn’t know what Mungyeong’s training methods would be like, but one thing was certain: earning his recognition wouldn’t be easy.

Objectively speaking, it would be strange if it were easy.

*It’s probably going to be brutal, but I’ll have to endure it.*

The man I was dealing with wasn’t some ordinary martial artist. He was the Slaughter Saint, a Supreme Peak master counted among the greatest in the world. Being taught secret martial arts by someone of that caliber was a fortuitous encounter in itself.

And when I thought about it, I had already experienced two such fortuitous encounters.

The first was, without a doubt, the System.

And the second…

*The Old Master.*

There was no way I could leave Jeok Cheongang out of it.

If I hadn’t met him, if I hadn’t learned the Fire Gate Clan’s martial arts—passed down to only one person in each generation—then even with the System, I probably wouldn’t have reached my current strength or position.

Following that train of thought, Jeok Cheongang’s face suddenly flashed through my mind.

*Still, I should go see him.*

Of course, Jeok Cheongang and I were not formally Master and Disciple.

But just because we didn’t call each other Master and Disciple didn’t mean ours was merely a relationship of convenience.

We were the kind of people who understood each other without speaking. Jeok Cheongang and I were the sort who toyed with the words *Master* and *Disciple* in our hearts.

“…”

Or maybe not. I’m suddenly not so sure.

Jeok Cheongang might think differently, but that was how I saw it.

And it was obvious that Jeok Cheongang must be troubled after swallowing his pride and personally asking Mungyeong to teach someone who was practically his Disciple.

*He’s probably off somewhere moping by himself again.*

Other people whispered that Jeok Cheongang was nothing more than a hot-tempered, impossibly eccentric old man. But the Jeok Cheongang I knew was a tenderhearted person.

He might scold and grumble, but deep inside, his feelings for the people he cared about were soaked through with affection.

I glanced up at the bright moon and began to walk.

*I’ll find him soon enough. There are plenty of people around.*

That comfortable thought vanished without a trace less than half an hour later.

“You haven’t seen him?”

“No, sir. I haven’t seen him for a while.”

“If you’re lying to me…”

“Why would I lie to the Captain? If I didn’t want to get beaten to death, I’d make up things that never happened and tell you.”

“What about Young Hero Cheong? You haven’t seen Young Hero Cheong either?”

“No, Benefactor. Why? Is something wrong?”

“It’s… Never mind. It’s nothing. Get back to what you were doing.”

“Oh! If nothing’s wrong, would you like to see Mimi? She ate ten Blood Fish, so her belly is incredibly round!”

“Yeah. Great.”

This place wasn’t even that large. Where on earth had he disappeared to?

I searched here and there for the missing Jeok Cheongang, but no matter whom I stopped and asked, the answers were never helpful.

“Hey, you beggar passing by. Come here.”

“No.”

“You haven’t been beaten enough lately.”

“Damn it. I have a reputation to maintain too. No matter how much of a Supreme Peak master you are, if you treat me, the Successor Beggar, like some stray dog you’re calling over from the street, what will the Sect’s disciples think?”

“Two silver nyang.”

“Are you seriously treating me like a beggar…”

“Ten nyang.”

*Fwoosh!*

“Hm. One cannot ignore a friend’s summons. What is it?”

“Our Old Master—no, our Master. Do you know where he is?”

“Sir Jeok? No idea. I haven’t seen him once since he arrived here.”

“Can you ask the other Beggars’ Sect disciples?”

“Well, we’re all busy with our assigned tasks. Still, you never know. I’ll make a round and let you know if I hear anything.”

“Yeah, thanks.”

“What are friends for?”

“Then get to it.”

“…What about the silver?”

“I’ll pay you later. But if you find my Master’s location, I’ll give you double.”

“T-Twenty nyang! Beggerrr!”

But even Gung Gibang, who had become a slave to capitalism and run off enthusiastically, ultimately failed to find Jeok Cheongang.

I tossed him five silver nyang, then continued visiting various places. The answers I received were always more or less the same.

“Sir Zhuge, have you perhaps seen my Master?”

“Oh, you came at the perfect time. I’m testing our clan’s formation, and I think that with a little more refinement, I can suppress the energy leaking from this gap—”

“That’s great. Good luck.”

“Great Hero Jin! I saw him!”

“Really? Where?”

“About two shichen ago, he was over by the water, beating someone senseless.”

“The person getting beaten was me.”

“…Ah.”

“Great Hero Jin! Great Hero Jin!”

“Yes. You there, with your hand raised. Where did you see him?”

“If you mean Sir Jeok, I haven’t seen him.”

“No, but why are you—”

“Would you sign this martial artist’s uniform for me? My son dreams of becoming a fine martial artist like Great Hero Jin. He says he’ll have no regrets if he can get your autograph…”

“…What’s your son’s name?”

“Zhuge Sopyeong. Please write something telling him to practice his martial arts diligently and not be a picky eater. Especially green onions.”

“Wait. Then may I ask for your autograph too?”

“I got here first. Get in line!”

“What? Why are you suddenly lining up? Move to the back! Don’t line up! Ah, this is driving me crazy.”

About half an hour later, after completing my grand tour, I returned to the temporary private tent that had been set up for me. By then, it was already past midnight.

After signing autographs with inspirational messages for Zhuge Sopyeong, Changwoo, Myoryeong, Jinsu, and the other budding talents, I was completely drained.

“…So where the hell is the Old Master?”

This wasn’t even the Liaodong Plain. How could he simply vanish into thin air?

At this point, he had clearly made up his mind to stay hidden. He had probably predicted that I would come looking for him and deliberately disappeared.

*I’ll be seeing him soon enough anyway. For him to avoid me this much…*

He must have been even more troubled than I had imagined.

I let out a small sigh, picked up the water pitcher from the wooden table in the corner of the tent, and gulped down the water.

I had been walking and talking all day, so my throat was parched. But why did the water taste like this?

*Did they scoop it straight from the river? It’s a little salty.*

Even in the unpolluted Murim, I couldn’t help feeling uneasy.

That was when it happened.

*Beep.*



> **System**
>
> - You have been poisoned by **Potent Paralysis Powder**.
>
> - **Potent Paralysis Powder** is a type of anesthetic that clouds the mind and stiffens the body.
>
> - You feel your consciousness becoming hazy!
>
> - Your **Scorching Yang Qi** resists the poison!
>
> - If you do not take action quickly, the Status condition **Full-Body Paralysis** will activate!



…?

No, fuck. What the hell was this?

I stared blankly at the System window, forgetting even the body that was slowly becoming paralyzed. Then a short memory flashed through my mind like lightning.

*You’ll naturally find out tomorrow.*

*It’s already the hour of the Pig. It’ll be midnight soon. Can’t you just tell me and get it over with?*

*It’s late. Don’t forget. We begin tomorrow.*



“……!”

Mungyeong, you son of a bitch!

A surge of rage made it feel as though my blood were boiling backward.

At the same time, the bloodstream carrying the paralysis powder raced through my body, and my vision began to fade.

I sucked in a startled breath, hurriedly raised my internal energy, and shouted a command in my mind.

*Inventory Open, Summon!*

A ring appeared on my finger at the same moment.

I normally kept the Myriad-Poison Ring in my inventory to avoid other people’s eyes, but now it scattered a strange sheen.

*Ding.*



> **System**
>
> - The usage conditions for the **Myriad-Poison Ring** have been met.
>
> - Special Skill **Poison Absorption** has activated!
>
> - **Potent Paralysis Powder** resists!



*Hissss!*

I could feel it. Deep inside my body, two energies with entirely different purposes collided.

But the Myriad-Poison Ring was a treasured artifact of the Sichuan Tang Clan, one that had even absorbed Jeok Cheongang’s Formless Ultimate Poison.

And with the addition of Scorching Yang Qi, the natural opposite of poison, the paralysis powder had no choice but to collapse helplessly.

*Ding.*



> **System**
>
> - **Detoxification** complete!
>
> - All traces of **Potent Paralysis Powder** have disappeared from your body!
>
> - All Status conditions have been cleared!



“…Phew. You crazy old man.”

I muttered the curse along with the breath I had been holding.

He had set up a trap like this the moment midnight passed. I never imagined that “we begin tomorrow” would mean this.

*Damn it. He really is an assassin.*

At first, I thought it was an ambush by Dark Heaven.

Was this what he meant by turning me into a true Murim martial artist? I was already exhausted, and the sudden attack had sent my heart pounding and made my legs go weak. With a deep sigh, I collapsed onto the bed.

*Phut-phut!*

“…?”

*Beep.*



> **System**
>
> - You have been poisoned by **Potent Soul-Bewitching Powder**!



Slaughter Saint, you fucking bastard.

[^1]: The hour of the Pig corresponds roughly to 9–11 p.m. in traditional East Asian timekeeping.
## Chapter artifact 491

# Chapter 491

“Hey, Captain. You haven’t slept—?”

Hyuk Mujin entered the temporary tent where I was staying at the dim hour before dawn, then clamped his mouth shut with an expression as if he had seen a ghost.

“Why?”

“Uh, well…”

“Say it.”

“No, sir. You just look unusually tired today.”

“…Hoo.”

Tired? Tired. Was that all I could call this?

I glared at the bronze basin filled with wash water. My hair was a mess, and my eyes were bloodshot. When I lifted my head and looked around, the entire tent was a disaster.

Hyuk Mujin belatedly noticed the same thing, and his pupils began quaking.

“What in the world… What on earth happened here?”

“Yeah. Something did happen.”

The voice coming from between my lips sounded unfamiliar, as if it belonged to someone else. I rubbed my haggard face and muttered,

“That fucking assassin bastard…”

It was a quiet mutter, but not quiet enough to be completely inaudible. The word *assassin* made Hyuk Mujin jump.

“Pardon? An assassin?”

“What?”

“No, you definitely just said ‘assassin.’”

“You heard wrong.”

“I heard it perfectly. With my own ears.”

“I said you didn’t.”

Of course, it was true.

Some vicious assassin bastard had installed a dozen or so hidden weapons inside the tent, and I had managed to trigger every single one of them. With a one-hundred-percent success rate, I had been reduced to a bloody rag.

The maddening part was that I couldn’t tell anyone about it.

“C-Captain…”

“Ah, I said you heard wrong!”

“That’s not it. You’re bleeding from your butt.”

“……!”

Fuck. No wonder my ass had felt warm for a while.

As I silently cursed and staunched the wound, Hyuk Mujin gave me an unimpressed look.

“I think it really was an assassin.”

“I was injured during training.”

“Really?”

I weakly nodded.

It was training. I had no idea what country’s training method involved staying awake all night and doing nothing but detoxifying poison, but it was training all the same.

“It really was training. I swear on both your balls.”

“As I’ve told you repeatedly, please don’t swear on my balls. And if an assassin is threatening you right now, blink twice.”

“…Mujin. If you’re going to make me do something like that, shouldn’t you at least ask through Sound Transmission?”

“I still can’t use Sound Transmission.”

“Then you could use written communication.”

“Oh, right.”

“Are you insane?”

Well, what more could I expect from Hyuk Mujin?

I let out a long sigh and looked him up and down. He had even dressed neatly in his martial artist’s uniform this early in the morning, so he clearly had business with me.

“Anyway, what’s going on?”

“Ah, Sir Zhuge is looking for you. Everyone is gathered right now.”

“Everyone? Why?”

“You know.”

Hyuk Mujin glanced around unnecessarily, then opened and closed his mouth a few times. Soon, his voice came in a whisper quiet enough for only me to hear.

“The imugi. The dead imugi.”

“Ah.”

“Only a very small number of people will be going in secret. Perfected Being Hyeongong of the Wudang Sect is waiting as well.”

“Even Perfected Being Hyeongong? Ah, of course he would be.”

Perfected Being Hyeongong was the only Supreme Peak master involved in this incident who had remained in Donghu Stronghold.

On top of that, he was the Wudang Sect Leader’s Junior Brother and a senior figure in the Murim. He had more than enough qualifications to attend as Wudang’s representative.

No matter how strictly confidential the Water God Dragon’s existence was, it wasn’t something we could keep secret from even the Wudang Sect.

*But if this matter is important enough, the Sect Leader himself could have come. Why send Perfected Being Hyeongong?*

The question occurred to me, but it vanished as soon as I thought of one particular person.

“Hey, is anyone going with us—”

I was about to continue, half hoping I was wrong, when a quiet voice came from outside the tent.

“Young Master Jin. Everyone is waiting.”

“……!”

“If you’re ready, please come out.”

The presence outside began moving away as soon as the words ended. Hyuk Mujin tilted his head when he saw me standing rigidly.

“Why are you doing that?”

“Why is he going with us?”

“Who? Oh, Mungyeong? Since he’s actually a disciple of the Divine Physician, he should be able to help a great deal with the imugi’s physical structure and such. But why?”

Why? Because I had no idea what that lunatic might do.

I swallowed the words rising to my throat and started walking. Then I stopped, turned around, and looked at Hyuk Mujin.

“Mujin.”

“Yes?”

“Go first. I’ll follow right behind you.”

“Pardon?”

It felt as if I could hear the System notification ringing in my ears.

*Ding.*



> **System**
>
> - You have acquired **Meat Shield**!

* * *

When I climbed aboard the small vessel prepared for us, I saw several familiar faces.

Perfected Being Hyeongong, dressed in a heavily patched robe with an old Pine-Pattern Ancient Sword at his waist, greeted me with a gentle smile.

“A young fellow Daoist has arrived. It is good to see you again.”

“Greetings, Perfected Being Hyeongong.”

I now made a fairly convincing martial artist’s fist-and-palm salute. Zhuge Feng, sitting beside him, waved his folded fan and cut in.

“But your expression…”

“Nothing happened.”

“You don’t look particularly well for someone to whom nothing happened. Don’t you agree, Perfected Being?”

“I agree with Family Head Zhuge. You look exactly as if you had been tormented by an assassin all night.”

“An assassin? Perfected Being, you do make jokes. Ha ha.”

“Ho ho ho.”

“……”

Don’t laugh. And don’t show me your teeth.

Without the Myriad-Poison Ring, I doubted I would have been able to stand upright by now.

I had been soaked in so much poison that I had seriously considered whether I should change my sobriquet from the Blazing Flame Divine Dragon to something like Poisoned Pickle.

*Look at him, sitting there shamelessly.*

I glared at Mungyeong, who had already claimed a seat on the swift ship.

The boy noticed my piercing gaze and slowly turned his head.

—Lower your eyes.

“……”

If he told me to lower them, I had no choice.

I stealthily turned my gaze away, and Mungyeong’s Sound Transmission continued.

—Judging by your condition, you must have fallen for every trap from the first day. How pathetic. If you hadn’t had the Myriad-Poison Ring and Scorching Yang Qi, you would have been dead by now.

—…How do you know whether I would have died or survived?

—Want me to tell you?

—I misspoke.

He wasn’t entirely wrong. Every hidden weapon Mungyeong had installed was coated with potent poison.

I had once heard that medicine and poison shared the same source. I didn’t know who had said it, but they had been completely right. Somehow, every poison I suffered came with the adjective *potent* attached to it.

Thanks to the Myriad-Poison Ring’s absurd performance and the Scorching Yang Qi I had learned, which was practically the natural opposite of poison, I had gotten away with only a few stab wounds.

If I hadn’t possessed those two things… Just thinking about it made my blood run cold.

*Medical apprentice, my ass. That’s no Divine Physician. He’s a Poison Physician.*

—I know you just insulted me.

“Ghk.”

I accidentally sucked in a startled breath. The kind-hearted Perfected Being Hyeongong looked at me with concern.

“Is something wrong, young friend?”

“Ah, no. It’s just a habit.”

“If so, that is a relief. I was startled, thinking you were actually being threatened by an assassin. Am I wrong, Family Head Zhuge?”

“Ha ha ha! I’m going to split my sides, Perfected Being!”

“Ho ho ho.”

“……”

I should just rip Zhuge Feng’s navel out.

While I glared at his stomach, the vessel carrying its passengers cut smoothly through the calm water.

It was such an obvious departure that I realized it a moment too late and hurriedly opened my mouth.

“Wait. The Old Master—no, my Master isn’t here.”

A question mark seemed to appear over Zhuge Feng’s face at my sudden objection.

“Hm? Didn’t you hear?”

“Hear what?”

“Senior Jeok decided not to attend. He also asked everyone not to look for him for the time being, until everything is finished.”

“…Is that so?”

“You didn’t know? That explains why he didn’t pass the message along through his Disciple.”

This was the first I had heard of it.

Whatever his reason, the fact that he hadn’t told me himself left me a little disappointed. At the same time, I thought I could understand how he felt.

*He must be troubled.*

I had never raised a Disciple, but if I found myself in the same situation someday, I felt I would react similarly.

Wasn’t it like entrusting a beloved pet—one cared for with love and devotion, almost like family—to someone else?

“……”

No, I take that back. If that were the case, I’d basically be Jeok Cheongang’s pet dog.

*His son. Right, let’s call it his son.*

I was still trying to reach that compromise with myself when Cheongpung approached with a bright expression and abruptly held something out to me.

“What’s this?”

“It’s candy, Benefactor.”

“……I know it’s candy, but where does this stuff keep coming from?”

There were only two possibilities.

Either Cheongpung was a System user with ten tons of candy stored in his inventory, or there was a tree nearby that grew candy.

“Either way, thanks.”

I normally wouldn’t have looked twice at it, but with my mind so complicated, candy was an excellent source of sugar.

I bit into the candy he had given me and asked,

“You’re pretty talented to have found candy at a time like this. Ah, did you buy it when you came to the Zhuge Clan last time?”

“No. I already ate all of that.”

“Hm? Then where did this come from?”

“Slaugh—no, Mungyeong gave it to me. He told me to give this one specially to you, Benefactor. He’s a really good person!”

“…Who?”

The answer came from somewhere else.

*Beep.*



> **System**
>
> - You have been poisoned by **Potent Energy-Dispersing Poison**!
>
> - **Energy-Dispersing Poison** temporarily prevents the use of internal energy.
>
> - Your **internal energy** is slowly dissipating! Immediate action is required!



“……”

Fuck. No wonder the candy had tasted unusually sweet.

I quietly took out the Myriad-Poison Ring.

* * *

They say that people leave their names behind when they die, while beasts leave their hides.

The same was true of the spirit creature that had ruled Dongting Lake and the Yangtze for five hundred years.

Although the Water God Dragon’s spirit had already left its body, its body remained where it had last lain down, retaining all the majesty and beauty it had possessed in life.

“…Hoo.”

Even Perfected Being Hyeongong, an old Daoist with profound insight and enlightenment, was speechless. Only a single exclamation escaped his lips.

That was how overwhelming the Water God Dragon’s body was.

Even Gung Gibang, who had already seen the Water God Dragon once, stood with his mouth hanging open, repeatedly exclaiming in awe.

“It’s incredible even the second time around. Don’t you think?”

I answered in a perfectly polite voice.

“It is incredible. So is your breath. Could you get lost? It seems even stronger than the Energy-Dispersing Poison.”

“Hm. That shouldn’t be difficult. However, I have a condition.”

“What?”

“Of the ten silver nyang you promised me yesterday, I still haven’t received five. I knew you were shameless, but I never thought you’d go so far as to prey on a beggar.”

“I’ll pay you, so keep it short. I’m starting to see things in front of me.”

At this point, it was impossible to tell whether his mouth was a mouth or a sewer.

After finally extracting another five silver nyang from me, Gung Gibang grumbled,

“Stop exaggerating. And if you mean hallucinations, I’ve had more than enough of those myself. I’ve been having strange dreams for the past few days.”

“Dreams?”

“Yes. Dreams.”

Gung Gibang gave a quiet laugh and pointed at Mungyeong.

“In the dream, Mungyeong was fighting that imugi. He was sending Sword Force flying through the air and disappearing and reappearing like a ghost. If someone told me he was the Slaughter Saint, the greatest assassin in history, I would have believed them.”

“……”

*He is the Slaughter Saint.*

I continued staring at the Water God Dragon’s body, doing my best to ignore Gung Gibang’s endless chatter.

From head to tail, its enormous body stretched for more than a hundred zhang.[^1]

Its scales, once stained black, now scattered dazzling silver light, while countless wounds were carved across its body.

I stroked one of the gaping scars and apologized silently.

*I’m sorry.*

Of course, I knew. The battle with the Water God Dragon had been unavoidable, and there was no reason for me to feel sorry.

If anything, it had been grateful to us for stopping it, even if we had needed to do so this way.

But I was apologizing because I couldn’t bury its body as it was.

*The corpse.*

The raid was over. It was time to dispose of the corpse.

[^1]: A zhang is a traditional East Asian unit of length, roughly 3.3 meters.
## Chapter artifact 492

# Chapter 492

It went without saying that the reason so many people had gathered in one place was not to pray for the Water God Dragon’s soul.

And one person in particular was showing rather obvious ulterior motives.

“Incredible. Simply incredible.”

Zhuge Feng’s eyes shone with rapture as he stroked the silver scales.

“This strength. This beauty. It’s unbelievable.”

Although it had died without ever becoming a true dragon, the Water God Dragon was still a divine imugi that had lived through five hundred years.

Its body had already proven itself in battle. It was armor and a weapon all on its own.

“This is… a priceless treasure.”

There wasn’t the slightest exaggeration in Zhuge Feng’s words.

The scales were harder than steel and could not be completely severed even by Sword Energy. The bones hidden beneath them were even harder than the scales.

Even in the modern age, where Magic-powered forging techniques had advanced to an incredible degree, material of this quality would sell for whatever price the owner demanded. In Murim, there was no point saying anything more about it.

*It may not be as valuable as Ten-Thousand-Year Cold Iron, but… it’s definitely an incredible treasure.*

The Water God Dragon’s body stretched for more than a hundred zhang,[^1] and every inch of it was made up of treasures like those.

Armor made from those scales would not be pierced even by a crossbow. A weapon made from its bones would be harder and sharper than one made from meteorite iron.

Martial arts manuals, elixirs, and exceptional weapons—the three things every martial artist went crazy for.

It was only natural that greed would appear in the eyes of Zhuge Feng and several others.

“If we made a Dog-Beating Staff out of that…”

Hyuk Mujin immediately objected to Gung Gibang’s muttering.

“Why would you make a Dog-Beating Staff out of the bones? We should make a proper sword. A Bone Sword made from an imugi’s bones… Just imagining it is incredible.”

“Are you looking down on the Beggars’ Sect?”

“No. I’m only looking down on you, Young Hero Gung.”

“Want me to beat you like a dog?”

“Now, now, calm down. There’s enough material to make at least a hundred Dog-Beating Staffs or swords, so why are you fighting over it?”

“That’s true. Then I’ll claim one Dog-Beating Staff for myself first.”

“I’ll reserve one sword too…”

Crack! Crack!

“Ugh!”

“Argh!”

After each receiving a smack to the back of the head, Gung Gibang and Hyuk Mujin turned toward me and shouted.

“Why’d you hit me?”

“Please explain the reason before hitting us!”

These bastards still hadn’t come to their senses.

I frowned and shook a large fist at them threateningly.

“You two useless bastards couldn’t do a damn thing when we were fighting, and now you’re talking about Dog-Beating Staffs? Swords? Reservations?”

“Well, that’s…”

“A martial artist can’t help it…”

“If the Water God Dragon hadn’t been there, Hubei Province would have been destroyed. It wouldn’t have ended with a few fish going berserk.”

There was no question that countless people had died because of the Water God Dragon.

But it had not been of its own free will. And if the Gate had opened completely, Hubei Province would have become a hellscape.

“Of course, the corpse will be useful. But if you’re even remotely human, you should at least be grateful. Got it?”

The two of them flinched at my shout and muttered in voices as tiny as ants.

“Like you are…”

“Honestly, Captain, you don’t have much room to talk either. You turned the Dongting Fisherman into that.”

Crack! Crack!

Two more blows rang out, followed by two more screams.

I glared at Gung Gibang and Hyuk Mujin, who were clutching their heads again.

“Are those two things the same? Are they? Huh?”

I had plenty of grievances of my own.

Of course, I felt bad about wrecking the Dongting Fisherman, but there had been nothing else I could do.

The Dongting Fisherman had been directly exposed to the corrupted Water God Dragon’s Fear. He had harmed people while out of his mind, and every piece of evidence at the time had pointed to him as the culprit.

Even if his limbs had been broken, at least he was still alive. If you looked at it another way, being beaten into a bloody pulp by me had allowed him to escape the Fear.

*A fist beat Fear.*

That was the triumph of humanity…

No, not really. We had both had our own circumstances.

I had even gone to check on him because I felt bad. He had been unconscious, though, so we hadn’t been able to talk.

“Anyway, be grateful. Understand?”

That was when I was shaking my fist threateningly at the two of them.

“Young Friend Jin is right.”

The voice alone carried profound wisdom. Perfected Being Hyeongong of the Wudang Sect stepped forward and spoke with a grave expression.

“I had my doubts when I heard what happened, but seeing it with my own eyes, I understand now. It truly is a divine creature blessed by the heavens.”

Like Perfected Being Hyeongong, Jin Wikyung was seeing the Water God Dragon for the first time that day. He nodded solemnly.

“Your words are completely correct, Perfected Being. It sacrificed itself to prevent even greater bloodshed. This imugi is worthy of being called a divine dragon.”

“It is truly a tragedy. Since we have received such an enormous grace, would it not be proper for everyone to pray for its soul together?”

Perfected Being Hyeongong was exactly what one would expect from an old Daoist who had cultivated profound Daoist mastery at Wudang, the sacred ground of Daoism.

He was fundamentally different from human garbage like Gung Gibang and Hyuk Mujin, who could not feel even the slightest gratitude.

Feeling an overwhelming faith in the Primordial Heavenly Venerable rise within me, I quickly clasped my hands together.

“Amen.”

Perfected Being Hyeongong, who had been reciting Daoist prayers, flinched and turned around.

“Amen?”

“I was mistaken. Amitabha.”

“……Repeat after me. Infinite Life Buddha.”

“Ah, my apologies. Infinite Life Buddha.”

“Excellent. The Primordial Heavenly Venerable will watch over you, Young Friend Jin.”

“Ah. Yes.”

*Does Wudang have missionaries too?*

Perfected Being Hyeongong smiled contentedly, like a Civilization player aiming for a religious victory. After reciting a short prayer, he looked up at the sky.

“You, divine imugi. I pray that you become an Azure Dragon there and soar across the heavens.”

“Ah…”

“As expected of Perfected Being Hyeongong.”

Zhuge Feng and Jin Wikyung, each with his own vested interests, eagerly sang his praises. Perfected Being Hyeongong answered with a benevolent smile.

“Ho ho. I merely did what was proper. That aside…”

“Yes, Perfected Being?”

Everyone, myself included, bowed their heads reverently and listened, wondering what profound words would come from the old Daoist’s mouth.

That was when he said,

“Now, let’s start taking it apart.”

“……?”

“We still have to do what needs to be done, do we not?”

“……!”

I raised my head and saw it.

The greed and longing for weapons blazing in Perfected Being Hyeongong’s eyes. And, carried through his gaze, a silent cry.

*I call dibs on one Pine-Pattern Ancient Sword! One Pine-Pattern Ancient Sword for me!*

He wasn’t a Daoist. He was a lunatic.

As I stared at Perfected Being Hyeongong, whom I had trusted for one brief moment, I realized something once again.

*Every last one of these Murim people is a hopeless bastard.*

* * *

The end of the raid did not mean the end of all the battles.

There was still a process that had to be fought through just as fiercely as the raid itself—sometimes even more fiercely.

*Distribution of the spoils. Final settlement.*

In the end, Hunters did this to make a living.

The top Hunters, who earned tens or even hundreds of billions a year, might be different. But in raid parties made up of lower-tier Hunters, people constantly got into arguments over byproducts worth only a few tens of thousands of won. That was why contracts were essential.

And the Water God Dragon’s corpse was a treasure of immense value in its own right.

Since we had entered the raid without even drawing up a contract, this would have caused an enormous dispute in the modern world.

But this was Murim, not the modern world. And the people gathered here belonged to the physical school, preferring to negotiate with their bodies rather than with words.

And I knew the most appropriate word for people like that.

*Suckers.*

I turned my head and swept my gaze around. Everyone was watching everyone else, waiting to see who would speak first.

Well, two of them were exceptions.

One of them—the Family Head of the Zhuge Clan, which could be called the richest family in Hubei—spoke first.

“Ahem.”

Zhuge Feng cleared his throat and continued casually.

“Regarding this matter, our family will have no choice but to make a concession. The Zhuge Clan will take only ten percent, and the rest can go to everyone else…”

“Stop right there. Are you dealing from the bottom?”

“What!”

I cut him off and gave a quiet laugh.

“Ten percent? What did you do that was worth ten percent? If you try to swallow that much for free, you’ll get a stomachache.”

“You…”

“Am I wrong? I may respect you, Sir Zhuge, but this isn’t right.”

*Ten percent, when he didn’t do a damn thing? How dare he try to sneak in and rob us blind?*

Zhuge Feng flinched under my icy stare, then opened his mouth again.

“Didn’t do anything? If not for the information provided by the Zhuge Clan, you would have been blind even with your eyes open. You certainly would not have made it this far.”

“You have quite a long tongue.”

“Ghk!”

“The conclusion you reached from that information was that the Dongting Fisherman was the culprit. Wasn’t it? You’re telling me that the Dongting Fisherman, lying there injured, suddenly got up, did five somersaults, and then used Stepping on Empty Air to hop all the way here?”

“That, that was…”

Zhuge Feng was momentarily rendered speechless. Then the only other person present who looked completely relaxed smiled gently.

It was the smile of a man whose skill had elevated the Jin Family of Taiyuan to its current position.

“Sir Zhuge, allow me to apologize on behalf of my little brother for his rudeness.”

“C-Cough!”

“It is entirely my fault for teaching my little brother so poorly.”

“His words were rather harsh.”

“I imagine they hurt your feelings. This is really unacceptable of him.”

“It’s all right. At least the Lesser Family Head seems reasonable, so that’s a relief…”

“Not at all. I really must give him a proper scolding. Taekyung, you little rascal! Apologize this instant!”

At Jin Wikyung’s booming shout, I immediately bowed my head.

“I apologize. I spoke too harshly.”

“Even if Sir Zhuge was trying to get something for free, there are still certain lines one must not cross!”

“I apologize once again.”

“No, wait. Hold on. Lesser Family Head Jin?”

Zhuge Feng seemed to sense that something was wrong and opened his mouth, but Jin Wikyung continued shouting.

“Taekyung played the greatest role in defeating the Water God Dragon! He practically saved Sir Zhuge’s life! But you are still the Family Head of a great clan and a respected elder of Murim!”

“Whew. I have committed a crime worthy of death.”

“Wait, Lesser Family Head.”

“Even if you were raised without proper manners, how dare a green youngster like you treat Sir Zhuge, whose reputation resounds throughout Murim, like some shameless bastard! As soon as we return to our family, I will…”

“Lesser Family Head Jiiin!”

Zhuge Feng desperately called out to him and waved his hand with a weary expression.

“All right. I understand. I understand everything, so please take care of me in the settlement.”

“Then you accept our brothers’ apology?”

“I’m sorry, Sir Zhuge!”

“Yes, yes, I understand. Now both of you, stop.”

“Thank you. Even if it isn’t ten percent, we’ll make sure the Zhuge Clan receives a fair share.”

“Even the loser gets a cut. That’s the universal rule.”

“……Whew.”

*Game over. Jackpot.*

Zhuge Feng was reduced to a limp wreck in the blink of an eye. Jin Wikyung and I exchanged satisfied smiles.

No matter how many times I died and came back to life, I could never catch up to Zhuge Feng in sheer intelligence. But this sort of negotiation could not be learned at a desk.

*This is the wisdom of everyday life.*

I had once thrown a fit to get one extra goblin poison dart during a settlement. Jin Wikyung, meanwhile, had spent years mastering the divine art of getting work done in the family’s shit-pile because no one knew whether his father was alive or dead.

If everyone here was a sucker, we were cardsharps.

*And judging by our contributions, I was obviously the top performer.*

Those who fight claim the spoils.

This was a battle from which we could not retreat—and should not retreat.

Only by standing proudly against our opponents, whoever they might be, could we become true Hunters and true martial artists.

—Ten percent. Hand it over. Or hand over your neck.

—We’ll hand it over.

But sometimes there were exceptions.

…Fuck.

[^1]: A zhang is a traditional East Asian unit of length, roughly 3.3 meters.
## Chapter artifact 493

# Chapter 493

Opportunity is not given equally to everyone.

In that sense, Perfected Being Hyeongong, who had become the Wudang Sect Leader’s direct Disciple at the age of ten, was someone who had received far more opportunities than most.

His path had been smooth from the very beginning.

Born with martial talent that ranked among the best of his generation and blessed with an upright character, Hyeongong had always received wholehearted support.

But that also meant he had never experienced a lack of anything in his entire life.

However…

*I want it.*

Perfected Being Hyeongong’s eyes trembled faintly. It was a material desire he had not felt in a very long time.

*I’ve never felt this way before.*

Gold and wealth? Fame and glory? He had never needed any of that.

Whenever he received a Daoist robe, he wore it until it was completely worn out, and he always got by on neat, simple meals.

Elixirs and martial arts manuals had been the same. After reaching the Supreme Peak realm, he had devoted himself to cultivating his mind.

Whenever his Senior Brother, the Sect Leader, offered him an elixir, Hyeongong gave it to his promising grand-disciples instead. And the Wudang techniques he had mastered were more than enough martial arts for one lifetime.

But this—this was different.

“Hoo… Infinite Life Buddha. Infinite Life Buddha.”

Hyeongong roughly stroked his beard and recited the invocation.

Yet despite his efforts to control himself, his gaze kept drifting toward the imugi’s corpse.

*They say those bones are incredibly hard.*

Between the split scales and the wide, gaping wounds, enormous bones radiated a faint glow.

Perhaps because they had belonged to a five-hundred-year-old imugi, the bones had a luster unlike anything else. He had heard they were so hard that even ordinary Sword Energy could not cut through them.

*If I made a sword from those bones, it would be incredible… No, no. What am I thinking? Get a grip, Hyeongong!*

Hyeongong squeezed his eyes shut. He had just witnessed Zhuge Feng being reduced to tatters by the two brothers of the Jin Family of Taiyuan, which only made matters worse.

At least Zhuge Feng had been there when the battle broke out. Hyeongong, on the other hand, had been at the Donghu Stronghold headquarters, hundreds of li away.

He had neither the justification to ask for anything nor the nerve to make a request despite his embarrassment.

*Infinite Life Buddha, Infinite Life Buddha. How can a Daoist allow himself to be distracted by such a base desire? Get a hold of yourself, Hyeongong.*

That was when he was suffering in silence.

“Perfected Being. Are you busy?”

“Hm?”

Hyeongong’s eyes flew open. A familiar young man was looking at him with a knowing gaze.

*Jin Taekyung.*

The young man was one of the driving forces behind the whirlwind shaking Murim alongside the Sword Saint’s Disciple, Cheongpung—the Huashan Divine Dragon.

Among gossip-loving raconteurs, people were already saying that the Ten Kings had the Two Dragons beneath them.

*He’s an incredible young man. Almost unbelievably so.*

But Hyeongong’s opinion of Jin Taekyung was not what mattered to him at that moment.

*Could it be?*

With a sliver of hope and excitement in his heart, the old Daoist looked at Jin Taekyung.

“What is it, Young Friend Jin?”

Jin Taekyung answered with a gentle smile.

“If you’re not busy, I wanted to ask if I could have a word with you.”

“A conversation? What do you need?”

“We have to deal with the corpse now, but there’s a lot more of it than we expected.”

“Th-That’s why?”

“Of all people, you came all the way here in person. Naturally, you ought to have something to take home with you.”

“Oh!”

Hyeongong’s eyes immediately lit up. Jin Taekyung smiled and continued.

“Our Jin Family of Taiyuan has always respected the Daoists of Wudang. As fellow martial artists of Murim, we would be delighted to share even a small portion of this harvest with you.”

“I-Is that really true?”

“Of course. I swear on Hyuk Mujin’s balls. And my eldest brother is fully in favor of it too.”

“Good heavens! Infinite Life Buddha!”

By gently scratching the itch Hyeongong had not had the nerve to ask anyone else to scratch, Jin Taekyung left the old Daoist beside himself with joy.

Hyeongong did not know who Hyuk Mujin was or why Jin Taekyung was swearing on the man’s balls. All that mattered was that he was being given a share.

*How can anyone be this kind?*

He was on an entirely different level from the hypocrites who only knew how to make pretty speeches.

A ray of light shining down on this cold Murim, crawling with shameless masses.

Hyeongong could practically see a halo over Jin Taekyung’s head.

“Thank you so much! May the Primordial Heavenly Venerable protect you and the Jin Family of Taiyuan, Young Friend Jin! Infinite Life Buddha!”

“Amen.”

Something about it seemed strange, but Hyeongong did not care in the slightest.

And as he stood there with a broad smile on his face, Jin Taekyung continued in a gentle voice.

“However, there is one small problem.”

“Hm? What sort of small problem?”

“The corpse is so enormous that I can’t handle it alone. And we can’t exactly move the whole thing.”

“That’s true. Quite true.”

From head to tail, the giant creature stretched for more than a hundred zhang.[^1]

It was questionable whether it could even be moved in one piece. And since doing so would require a great deal of manpower, keeping the matter secret would become even more impossible.

“So I wanted to ask you for a small favor, Perfected Being.”

A glimmer of suspicion passed through Hyeongong’s eyes.

“Wait. Young Friend Jin. This favor of yours wouldn’t happen to mean…”

“Yes. You’ll have to lend us a hand. At this rate, it’ll take several days.”

So that was it! That was why he had shown Hyeongong such kindness!

Hyeongong glared at Jin Taekyung with an expression of betrayal.

“So you’re saying that you want me to use Wudang’s sword techniques to take that imugi’s corpse apart?”

“Think of it simply. It’s just a job.”

“Think of it simply? A job? I did not train my martial arts for this!”

When someone reached the Supreme Peak realm, it meant that they had devoted most of their life—no, their entire life—to martial arts.

Hyeongong was no different. How many years had he spent with one sword as his companion and beloved?

He had even trained in the pitch-black darkness, facing a wall as he honed his martial arts. To him, Jin Taekyung’s request was no different from an insult.

*How outrageous.*

With his face stiff as a board, Hyeongong opened his mouth.

“Infinite Life Buddha. Young Friend Jin. You have insulted not only me but also the sword arts of all Wudang.”

“Insulted you? How could that be? I’m merely asking you to lend us a hand.”

“But I cannot use my sword for something as trivial as—”

At the moment Hyeongong’s voice began to rise, Jin Taekyung casually tossed out a single remark.

“Now that I look at it, your sword is pretty worn.”

“What?”

“It seems like it’s about time you replaced it. What do you think?”

“……”

Hyeongong’s pupils shook as if an earthquake had struck.

Without realizing it, he looked down at the old Pine-Pattern Ancient Sword hanging from his waist. A thought suddenly passed through his mind.

*It is definitely worn… No! What am I thinking?*

It was the sword he had carried ever since he was ten years old. It was also a precious gift from his late master.

Hyeongong hurriedly shook his head, pulled himself together, and glared.

“It is not worn!”

“It is. Take a look for yourself. The hilt alone is completely ragged.”

“It does look a little… No! You saw it wrong!”

“Fine, let’s set that aside. The scabbard is covered in cracks too. Has it been through a drought?”

“Ah! When did this happen…?”

“Whoa, this is in serious condition. Would you draw the sword?”

“Why should I?”

*Shing!*

Hyeongong had shouted before belatedly realizing that he had drawn his sword. He was horrified.

*When did I do that?*

But regardless of that, the devil’s whisper continued.

“The blade doesn’t look to be in very good condition either.”

“It was given to me by my late master!”

Jin Taekyung answered with an utterly calm expression.

“My body was given to me by my parents, but it broke down with use. If I could have replaced it, I would have done so long ago.”

“Well, this old Daoist’s joints ache these days too. I’m practically itching for Bone Transformation… What are you trying to do?”

“I’m just telling you the cold reality. Oh, the edge is still sharp, at least.”

Get a grip. Hyeongong had to get a grip.

Hyeongong steadied his breathing and answered in a voice filled with pride.

“Of course it is. The blade was forged with four nyang of Ten-Thousand-Year Cold Iron mixed into it.”

“Good heavens. You used four nyang of that precious Ten-Thousand-Year Cold Iron?”

“Do you understand now? This sword may look worn, but it is in no way lacking when it comes to being called a treasured sword.”

“Oh. Is that so?”

“Of course! I already possess a sword so fine that anyone would covet it. Why would I need another sword…”

*Clang!*

“Oh, sorry. My hand must have slipped. I dropped my spear. Please continue.”

Jin Taekyung’s sheepish smile did not register in Hyeongong’s eyes.

His eyelids trembled as he stared at the spear radiating a faint glow.

“Y-Young Friend Jin. Is that, by any chance…”

“It’s nothing special. This is made from Ten-Thousand-Year Cold Iron too, but compared to the sword you have, it’s nothing.”

It certainly did not look that way.

Hyeongong swallowed hard and cautiously asked,

“How many nyang?”

“It’s solid. The entire thing, from the blade to the shaft.”

“You’ve got to be kidding me. Infinite Life Buddha.”

“Pardon? What did you say?”

“Ah, nothing. It was nothing.”

A devil. This was the devil’s whisper.

Yet Hyeongong’s eyes remained fixed on Jin Taekyung’s spear, White Flame, as he recited the invocation as if possessed.

“It’s as light as a feather, but how incredibly hard it is. And it’s sharp too. But…”

Then the gentle voice of temptation slipped into the old Daoist’s ear.

“I’ve found myself wanting a weapon made from an imugi’s bones.”

“Infinite Life Buddha. I don’t.”

“Think about it carefully. Not just any weapon, but one containing all the qi of a sacred imugi that lived for no less than five hundred years.”

*Of course it would be incredible. I really want it.*

Hyeongong barely swallowed the words rising to his lips and shook his head frantically.

“Impossible! I can never abandon the sword my master gave me—”

“Who said anything about abandoning such a precious thing? You can have both.”

“What the fuck? That’s an option? Ah, Primordial Heavenly Venerable!”

“Pardon?”

“Stop! That’s enough! Infinite Life Buddhaa!”

“If you help us, we’ll give you a share generous enough that Wudang won’t feel slighted. Do you think I’d settle this with a single sword?”

“I already have a sword made from Ten-Thousand-Year Cold Iron!”

“Yes. And an imugi’s bones.”

“How could I use another sword when I have the one my master gave me?”

“Yes. The more, the better.”

“I did not learn martial arts for this sort of thing!”

As Hyeongong clung to his last shred of pride and lamented, Jin Taekyung suddenly shouted toward somewhere behind the corpse.

“Hey, Young Hero Cheongpung! Is everything going well?”

A bright face popped out from behind the enormous corpse. It was Cheongpung, who had been promised a considerable share as payment for fighting alongside them.

“Yes, Benefactor! I’m working on the waist right now!”

“Really? That part must be especially thick. Isn’t it difficult?”

“No! I’m cutting through it just fine with the Martial Extremity Grand Unity Sword!”

“Good. I’ll be there soon, so keep working.”

“Yes, Benefactor!”

After giving the diligent worker a pleased smile, Jin Taekyung turned back to Hyeongong.

“Ah, sorry, Perfected Being. I took my eyes off the work for a moment.”

“……”

“But what were we talking about? I’ve been forgetting things a lot lately.”

Hyeongong looked back and forth between Cheongpung, who was working diligently, and Jin Taekyung.

And half a shichen later…

*Slash!*

The Taiji Wisdom Sword, Wudang’s finest sword technique, was separating the imugi’s scales from its bones.

“Murim has gone completely mad.”

That was Mungyeong’s brief assessment as he watched the entire situation unfold.

[^1]: A zhang is a traditional East Asian unit of length, roughly 3.3 meters.
## Chapter artifact 494

# Chapter 494

Slash! Shhk-shhk-shhk!

Scales split apart, and huge chunks of flesh were cut into evenly sized pieces.

The enormous bones revealed between the chunks were so clean that it hardly seemed possible.

Thud! Slash!

It was a skill bordering on the supernatural.

As everyone stared at the astonishing sight in a daze, a quiet murmur spread through the crowd.

“Hyuk. I’m asking because I genuinely don’t know, but… Was the Jin Family of Taiyuan originally a family of fishermen?”

“Can I ask the Lesser Family Head that exact question?”

“Of course not, you lunatic. But this really is impossible unless he was born with it. Could he actually be a fisherman…?”

“Lesser Family Head! Do you know what Young Hero Gung just said?”

“Hey, hey!”

“Was one of our ancestors a fisherman? How can the youngest one do that?”

“……Lesser Family Head?”

“If Zhuge Wuhou had seen this, he would have been so shocked that he’d have fallen out of his four-wheeled carriage. Wouldn’t you agree, Perfected Being Hyeongong?”

“Good heavens. Infinite Amen, Avalokiteshvara.”

“……Perfected Being?”

While everyone questioned the roots of the Jin Family of Taiyuan and, at the same time, worked toward religious unification, one person alone was thinking about something entirely different.

*Huh. Look at this guy.*

The movements of Jin Taekyung, cutting and slicing as if possessed, were reflected in Mungyeong’s clear eyes.

*What incredible power. And it’s fast and concise, too.*

A person’s realm could be recognized from even the smallest movement.

In that sense, what Jin Taekyung was showing them was astonishing.

*An incredible achievement. It’s hard to believe he’s barely past twenty.*

Mungyeong had already known that Jin Taekyung was a man who far surpassed common sense.

No, it was not only Mungyeong. Every martial artist in this dusty martial world knew it.

Even the young prodigies of the Nine Sects and One Gang, who received the finest support, struggled to break through the Peak realm at twenty. Jin Taekyung, meanwhile, had reached the Supreme Peak realm and stood shoulder to shoulder with masters of the previous and even earlier generations.

But that was not the only reason Mungyeong admired him.

*He’s as seasoned as an old hand in the martial world. And he can even control his strength in a way no one his age should be able to. There’s no wasted movement.*

Thump! Slash!

Even his smallest movements were efficient. He had every reason to be conscious of the people watching him, yet there was none of the flashy affectation that someone his age might have displayed.

He simply cut, sliced, and separated, like a traveler quietly taking the fastest and easiest road.

*He was the same when he fought the imugi.*

An assassin took in and analyzed everything happening around him. Their profession required them to assassinate their target and find an escape route under any circumstances.

And Mungyeong was the Slaughter Saint, called the greatest assassin of all time.

He had watched Jin Taekyung from Sichuan until now—not as the Divine Physician, but through the eyes of the Slaughter Saint.

*The Heavenly Martial Physique… Was it real after all?*

It had been forty years since Mungyeong left Murim. For all that time—long enough for the mountains and rivers to change four times—he had lived as a medical apprentice.

He had examined and treated thousands upon thousands of patients, accumulating countless experiences.

Yet even for Mungyeong, Jin Taekyung’s body and talent were not easily explained.

*He’s similar to Cheongpung, but subtly different.*

Mungyeong’s gaze turned toward Cheongpung, then quickly moved away.

The only person who could be compared to Jin Taekyung. No—in terms of understanding and applying martial arts, one could even say Cheongpung surpassed Jin Taekyung.

Cheongpung, too, possessed an extraordinary body unlike any Mungyeong had ever seen.

But it was not the same as Jin Taekyung’s.

*Cheongpung was refined. Jin Taekyung was born this way.*

The shape and size of his muscles, his skeleton, his acupoints—everything was perfect.

The Heavenly Martial Physique in every sense.

Mungyeong’s gaze sank into deep thought as he looked at Jin Taekyung.

*What if that boy completely made my secret martial arts his own…?*

The thought flashed through his mind, but Mungyeong quickly pushed it aside.

*Ridiculous.*

Martial arts were like an endless mountain range.

Most martial artists at the foot of the mountain probably believed Mungyeong had reached the summit. But Mungyeong was already facing another mountain.

That was how vast and distant the world of martial arts was.

Even Mungyeong had not seen the end of the secret martial arts he had learned. No matter how exceptional Jin Taekyung’s Heavenly Martial Physique was, it was unreasonable to expect him to show a satisfactory level of achievement in such a short time.

*Especially in a situation like this.*

War was already right on their doorstep.

When he considered the countless battles soon to come, it was only right to teach Taekyung what he needed most. Anything in excess became poison.

The Fire King, Jeok Cheongang, must have known that too. That was why he had entrusted Jin Taekyung to Mungyeong.

*But… What on earth should I teach that bastard?*

Feeling truly at a loss for the first time in a long while, Mungyeong watched the scene unfolding before him.

“Young Hero Cheongpung! Ready?”

“Yes, Benefactor!”

“Lay into it with the Plum Blossom Sword Technique!”

“Ah!”

“Perfected Being! Where are you?”

“Oh. Here I am!”

“Why are you standing over there instead of working? Can’t you see the rest of us working?”

“I-I was just about to take a short break…”

“Perfected Being, you’re such an individualist! How can you have no teamwork at all?”

“I-I’m sorry.”

“Show me how sorry you are. Taiji Wisdom Sword, go!”

“I-Infinite Life Buddha!”

Slash! Slash! Slash!

Following Jin Taekyung’s thunderous directions, the Water God Dragon’s corpse was dismantled in an instant.

While everyone else cried out in admiration, Mungyeong’s heart only grew heavier.

*What am I supposed to teach that bastard?*

At this point, he looked like the kind of person who would grow just fine on his own…

After wrestling with his thoughts, Mungyeong changed his mind.

No. Now that things had come to this, he would see it through to the end.

He also wanted to watch from the side and see just how far this arrogant bastard named Jin Taekyung could go.

*First, I need to fix that absurdly complacent head of his.*

Mungyeong quietly approached Hyuk Mujin, who was watching with his mouth hanging open.

“Martial Warrior Hyuk.”

“Wow, that’s insane. He cut through that in one go—oh, Mungyeong. What is it?”

“I thought Young Master Jin must be exhausted. I was wondering if you could take him some water.”

“Good heavens. You really do think differently from the start. I’ll deliver it right away.”

“Please don’t tell him I gave it to you. It makes me happier when you receive the praise.”

“You really are something…!”

Hyuk Mujin looked at Mungyeong with deeply moved eyes and accepted the leather waterskin.

Of course, along with cool water, it contained a deadly poison called Seven-Step Soul-Chasing Powder—an extreme poison that killed its victim before they could take seven steps.

* * *

“……What is this?”

Immediately after the work was finished, Hyuk Mujin approached me with a leather waterskin. He answered my question with a proud expression.

“It’s water. I thought you might be tired, Captain.”

“There’s no way you could do something this considerate.”

“I really fetched this water myself! Why don’t you trust me?”

Had I been too sensitive lately? Seeing how wronged Hyuk Mujin looked, I felt a little guilty for even suspecting him.

To be honest, after working for so long, my throat was genuinely dry.

“Hm. Really?”

“That’s enough. If you’re going to be like this, don’t drink it! I’ll drink it myself!”

“Hey, hey. Fine. Leave it here and go. I’ll drink it.”

“I said forget it!”

“Just stop there. You’re starting to piss me off.”

“……Yes.”

After sending Hyuk Mujin away, I carefully opened the stopper of the leather waterskin and smelled it.

*Mm. Smell.*

*At least the smell seems normal.*

Even so, I did not let my guard down. I tilted the leather waterskin very carefully.

A drop of water trickled out slowly and plopped onto my tongue.

*Still, just in case, I’ll start with one drop…*

> **System**
> - You have been poisoned by **Potent Seven-Step Soul-Chasing Powder**!
> - **Potent Seven-Step Soul-Chasing Powder** is an extreme poison capable of killing dozens of bulls with a single drop!
> - Severe **Internal Injury** and organ damage are likely. Very, very urgent treatment is required!

“……Hyuk Mujin, you son of a bitch.”

Fuck. This wasn’t the kind of one drop I meant.

*Inventory open. Summon!*

I hurriedly equipped the Myriad-Poison Ring and raised my Scorching Yang Qi, driving out the poison.

An instant later, a System notification announced that Detoxification was complete.

But that was not the end.

> **System**
> - Quick action—but the extreme poison has left aftereffects!
> - Your **Sinews and Meridians** have suffered minor damage!
> - Some abilities have decreased due to the damage to your **Sinews and Meridians**!
> - **Strength** decreased by 5!
> - **Agility** decreased by 5!
> - Status abnormality: **Severe Stomachache**!
> - Status abnormalities will return to normal once you have fully recovered, but decreased abilities cannot be restored!

“What the hell?”

No, fuck. Were these stat losses for real?

And not just one or two points. Ten whole points had vanished from my Strength and Agility combined.

*Ten points is one level-up!*

Damn it. I knew exactly whose work this was.

As the stats I had raised through every kind of hell disappeared pointlessly, hot fury surged up from deep in my gut.

Grrrggg.

……Was that fury?

Or was it feces?

As if the situation were not already bad enough, I had been afflicted with a truly shitty status abnormality.

Feeling my vision turn white from the stomachache, I hurriedly started walking.

“Young Friend Jin, where are you going?”

“Benefactor, where are you going?”

“Move, move. The dismantling is finished anyway, so all we need to do now is sort everything. I just need to take care of something…”

“Benefactor, are you going to poop?”

*Don’t say it so loudly, you lunatic. What if Mungyeong hears you?*

I walked unsteadily with a pale face. Only after I reached a place where no one could see me did I finally feel relieved.

*Whew. Thank goodness.*

The humiliation of shitting myself while standing was one thing, but if Mungyeong had seen me, I definitely would not have gotten off easy.

Fortunately, Mungyeong was nowhere among the others, so he must be somewhere else by now…

*Wait. Somewhere else?*

The question surfaced in my mind at the exact moment my foot came down on the ground.

And then I heard a faint noise.

Step. Tap.

A chill ran down my spine.

I instinctively launched my body into the air.

Shhk-shhk-shhk!

Four sounds of air splitting rang out on the wind.

Four daggers flew in from the front, back, left, and right, piercing the edges of my clothes and skimming dangerously close to my skin.

If I had not dodged, they would have been buried in my chest, back, and limbs.

*What the hell…!*

I righted my body and landed on the ground, then glared furiously at the rock wall more than ten zhang[^1] away.

“Can we take it down a notch? Huh?”

The rock wall rippled like a heat haze.

A moment later, a person emerged and answered in a dry voice.

“I told you clearly. I decide the method of training.”

“You put me in this state and then hid over there? You could at least face me directly—”

“I was not hiding. I was watching.”

“What difference does that make? You got caught.”

“I merely exposed myself enough for you to notice. If you can’t notice even this much, you might as well bite down on a blade and die.”

“You…”

“You?”

Mungyeong.

No—the Slaughter Saint.

The moment I met his deeply sunken gaze, a chill ran over my skin, and hot fury surged up again.

Grrrrrrrk. Frrt.

“……”

“……”

It wasn’t fury.

It was shit, actually.

[^1]: A zhang is a traditional East Asian unit of length, roughly 3.3 meters.

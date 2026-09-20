# Checkpoint Review — 535–539

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

# Chapters 535–539

## Plot

Jin Taekyung and Cheongpung are summoned to the restored Murim Alliance’s Alliance Leader’s Hall, where Mae Jonghak formally recognizes their actions against Dark Heaven as humanity and chivalry. With Tang Sadok’s public support, Mae appoints them as the two pavilion masters of the Alliance Leader’s direct Two Dragons Pavilion, granting them authority to select personnel. Hwangbo Gun objects to Taekyung’s appointment because he protected the Black Dragon Demon Gate, but Mae privately voids the proposed personnel action and retains Taekyung in the post. Taekyung is instead disciplined by being ordered to skip dinner.

The System then assigns Taekyung a Two Dragons Pavilion Quest: recruit at least five companions and name the organization, or receive the Title Loner. Mungyeong refuses Taekyung’s recruitment attempt because he has already accepted Cheongpung’s offer. Mungyeong, formerly the Slaughter Saint and now known as the Divine Physician, treats patients throughout the area and recognizes Cheongpung’s snake-inspired Mimi Step as a genuine martial creation. He judges Cheongpung to have the makings of a Grandmaster and agrees to let him learn through observation. Taekyung orders Hyuk Mujin to write and post public notices seeking other recruits.

## Continuity

- The Mount Song Resolution restored the Murim Alliance. Mae Jonghak is Alliance Leader, and Song Ho commands the Hidden Shadow Pavilion.
- Jin Taekyung and Cheongpung are the two pavilion masters of the Alliance Leader’s direct Two Dragons Pavilion, with regiments and subordinate squads beneath them. They may select personnel and answer directly to the Alliance Leader.
- Tang Sadok and the Sichuan Tang Clan publicly support their appointments and acknowledge an unrepayable debt to them.
- Hwangbo Gun opposes Taekyung’s appointment; Mae Jonghak secretly rescinded the personnel action he appeared to promise Hwangbo.
- Taekyung’s first Two Dragons Pavilion Quest requires at least five companions and an organization name. Failure awards the Title Loner.
- Mungyeong is the former Slaughter Saint who buried his assassin identity after the war and became the Divine Physician. He has accepted Cheongpung’s offer, so Taekyung’s first recruitment attempt failed.
- Cheongpung created Mimi Step from Mimi’s movements. Mungyeong recognizes it as a genuine recreation of martial principles and considers Cheongpung a potential Grandmaster.
- Mimi is a large horned snake who eats dumplings, sweets, and Blood Fish.
- Taekyung is now seeking additional recruits through public notices, with Hyuk Mujin responsible for preparing them.
- The Lord of Heaven, Dark Heaven’s Gate-opening method, the Southern Heaven Demon Empress’s plans in Yunnan, Jeok Cheongang’s duel with Nangong Cheon, and the cause of Ju Hwaran and Sama Pyo’s broken engagement remain unresolved.

## Translation Decisions

- Retain **Murim Alliance**, **Alliance Leader**, **Two Dragons Pavilion**, **Pavilion Master**, **Hidden Shadow Pavilion**, **Dark Heaven**, **Black Dragon Demon Gate**, and **Divine Physician**.
- Render **협** as **chivalry**, **인의** as **humanity**, **협객** as **knight-errant**, **대종사** as **Grandmaster**, **아싸** as **Loner**, and **고잉무림호** as **Going Murim ship**.
- Preserve **Mimi Step**, **Slaughter Saint**, **Blazing Flame Divine Dragon**, **Huashan Divine Dragon**, **Myriad-Poison Asura**, and **Young Hero Gung**.
- Preserve Taekyung’s blunt profanity, dry first-person narration, recruitment and workplace humor, financial-therapy jokes, System-message interruptions, and Cheongpung’s earnest martial enthusiasm.

## Durable state

{
  "active_continuity": [
    "The Mount Song Resolution formally restored the Murim Alliance; Mae Jonghak is its Alliance Leader, and Song Ho commands the Hidden Shadow Pavilion under his authority.",
    "Mae Jonghak formally appointed Jin Taekyung and Cheongpung as the two pavilion masters of the Alliance Leader's direct Two Dragons Pavilion; each pavilion has a regiment and subordinate squads beneath it.",
    "Tang Sadok and the Sichuan Tang Clan publicly support Jin Taekyung and Cheongpung and acknowledge an unrepayable debt to them.",
    "Taekyung believes the Zhongnan Sect resents him, the Jin Family of Taiyuan, and Jeok Cheongang after its repeated humiliations and will obstruct them.",
    "Cheongpung created Mimi Step from Mimi's movements; it is a snake-like footwork technique fast enough that Taekyung could barely track it with his naked eyes, and Mungyeong recognizes Cheongpung as having the makings of a Grandmaster.",
    "Mimi is now a large horned snake under Cheongpung's care, eats dumplings, sweets, and Blood Fish, and has recently had her condition examined by Mungyeong.",
    "Mungyeong ended Taekyung's direct training and assigned him a final task of incorporating martial principles into his learned martial arts.",
    "Zhuge Feng's Demon-Sealing Formation still blocks all mana from the exposed Gate, while Jang Taebo is summoning artisans to process the Water God Dragon's remains.",
    "The Southern Heaven Demon Empress is traveling toward Yunnan and expects to cause further deaths.",
    "The Black Dragon Demon Gate remains a major unorthodox power descended from the Demonic Cult's Twelve Branches; Sama Pyo is its Young Sect Leader and Black Dragon Saber, and Taishan is his giant subordinate.",
    "Jin Taekyung remains a Supreme Peak master with Three Flowers Gather at the Crown, advanced qi perception, exceptional resistance to monster Fear, and public S-rank-level recognition despite retaining an A-rank license.",
    "The System has assigned Taekyung's first Two Dragons Pavilion Quest: recruit at least five companions and name the organization, or receive the Title Loner. Mungyeong has accepted Cheongpung's offer, and Taekyung is now seeking other recruits through public notices."
  ],
  "continuity_sources": [
    539,
    538
  ],
  "open_questions": [
    "What is the Lord of Heaven's identity, how is he connected to the dangerous force Taekyung associates with his original world, and how can Dark Heaven open Gates?",
    "Where is the Southern Heaven Demon Empress ultimately headed, and what does she intend to do in Yunnan?",
    "What is the outcome of the duel between Jeok Cheongang and Nangong Cheon, the Azure Sky Sword King?",
    "Why did Ju Hwaran and Sama Pyo's political engagement end?",
    "Which additional companions will join the Two Dragons Pavilion, what name will it receive, and can Taekyung complete the System Quest?"
  ],
  "safe_through": 539,
  "temporary_decisions": [
    "Render 고월루 as Gowolru, 곤륜운룡 as Kunlun Cloud Dragon, 학우 as Hak Woo, 이룡각 as Two Dragons Pavilion, 협 as chivalry, 인의 as humanity, and 협객 as knight-errant; render 전 정혼자 contextually as former fiancé or former fiancée.",
    "Render 탈진 as the capitalized system status Exhaustion; retain Ten Dragons and Phoenixes, Blazing Flame Divine Dragon, Dark Heaven, Murim Alliance, and Old Master.",
    "Render 황보세가 as Hwangbo Family, 소가주 as Lesser Family Head, 은비화 as Dagger Hidden Flower, and 전음 as Sound Transmission.",
    "Preserve the chapter's blunt profanity, financial-therapy humor, monster-comparison humor, and Mae Jonghak's carefree 'That can happen' refrain; render 고잉무림호 as Going Murim ship, 대종사 as Grandmaster, and 왕희지 as Wang Xizhi.",
    "Render 일기천룡 as One-Ride Heavenly Dragon and Taishan's speech as clipped, childlike, and literal."
  ],
  "version": 1
}

## Reading copies

## Chapter artifact 535

# Chapter 535

“Great Hero Mae. No—the Alliance Leader is looking for you.”

Jin Wikyung’s sudden words made me pause.

“Me?”

“Yes. And Young Hero Cheongpung as well.”

Cheongpung too?

I was about to ask Jin Wikyung why when a familiar face suddenly popped out through the window of the pavilion.

“Grandpa! Are we going to see Grandpa now?”

At Cheongpung’s excited shout, Jin Wikyung smiled faintly and gave a small shake of his head.

“Not your grandfather. The Alliance Leader is looking for you.”

“Yes. So, Grandpa!”

“It’s the same person, but not the same. Regardless, Young Hero Cheongpung, prepare yourself and come down as soon as you can.”

“Wait! I need to pack some dumplings!”

“All right. Pack a variety. And some sweets, too.”

*He’s gotten some experience with this. Look at him not even blinking.*

Jin Wikyung must have seen Cheongpung more than once or twice by now, because he handled him as naturally as flowing water.

When Cheongpung disappeared with a great clatter, Jin Wikyung turned his gaze toward me.

“You aren’t asking why.”

“……I’d say it’s more accurate to say I haven’t had a chance to ask.”

“That’s true.”

“Since it’s come to this, I’ll go and hear it directly. Actually, I already have a bit of a feeling about this.”

“What sort of feeling?”

“Well, I don’t think he called us here just to see his grandson’s face.”

They were looking for Cheongpung and me.

Sword Saint Mae Jonghak—or rather, the Alliance Leader of the Murim Alliance.

They were the same person, but the meaning changed depending on which name one used. That was probably why Jin Wikyung had corrected Cheongpung’s form of address.

*The Alliance Leader.*

That name carried weight. And the fact that a giant who carried the countless martial artists crisscrossing the Nine Provinces, as well as the entire Murim beneath heaven, on both shoulders wanted to see me…

*No matter how I think about it, this feels ominous.*

Had another incident broken out already?

I was thinking that when—

Whoosh!

Along with the sound of rushing wind, Cheongpung appeared. He was carrying a bulging silk bundle in one hand, and his upper body was clad in gleaming silver armor.

Wait.

Armor?

Hiss.

“I’m here now. What the hell.”

“It’s Mimi. She’s gotten so big that I can’t carry her in my arms anymore.”

“……Then how about leaving her behind?”

Cheongpung tilted his head.

“Why?”

“Are you seriously asking because you don’t know?”

“Yes!”

“Oh… Not even a moment’s hesitation. This is driving me insane.”

She was a snake. Not just any snake, but a snake with horns.

She had grown so bulky that Mimi no longer even felt like the right name for her.

Bottom line, I had no idea how many snake enthusiasts there were in the Murim Alliance, but she wasn’t exactly the kind of pet snake they would welcome.

“……What the hell have you been feeding her?”

“Hehe. She’s gotten really big, hasn’t she? Take a guess, Benefactor.”

I answered without hesitation.

“Steroids.”

“Mostly dumplings and sweets. Oh, she definitely seems to have gotten a lot bigger after eating the Blood Fish.”

I stopped just as I was about to demand why he had been feeding a snake dumplings and sweets.

“Blood Fish?”

“Yes.”

The Blood Fish were fish from Dongting Lake that had been contaminated by mana.

In other words, she had eaten something seriously spoiled…

“This won’t do. Mimi stays here.”

“She’s fine.”

“Other people might not be. She could bite them.”

“No, Mimi won’t bite even if someone tells her to. Would you like to see?”

Cheongpung reached toward Mimi with an urgent expression.

“Mimi, bite!”

Swish. Clack!

It happened in the blink of an eye.

Mimi opened her jaws wide and lunged like lightning. Cheongpung’s hand vanished even faster.

Mimi’s teeth snapped together in empty air, and she flicked her tongue as though disappointed.

Hiss.

“See? She didn’t bite.”

“……”

“……”

*Is he insane?*

*No, she simply failed to bite him.*

Just as everyone—including me—lost the ability to speak, Cheongpung muttered with a crestfallen expression.

“The Sl—no, Mungyeong said she was fine…”

“Mungyeong?”

“Yes. I see him often these days. He checked Mimi’s condition then, too.”

Come to think of it, I hadn’t seen Cheongpung and Mungyeong around much lately. I had been busy, but judging by Cheongpung’s words, that wasn’t the only reason.

*The guy who never showed interest in anyone else. What suddenly got into him?*

Cheongpung swallowed a startled breath when he saw my narrowing eyes.

“Gasp.”

“Why?”

“It’s nothing.”

That made him even more suspicious.

Still, I ended the matter with a shrug. Jin Wikyung was visibly beginning to grow anxious.

“My youngest, that…”

“Oh, sorry. Is it urgent?”

“To be honest, there’s no benefit to being late. The others are waiting as well.”

*The others?*

This seemed to be a much bigger affair than I had expected.

Hiding my unease, I jerked my chin toward Cheongpung.

“Let’s go, Young Hero Cheongpung.”

“Yes, Benefactor!”

Gung Gibang and Hyuk Mujin nodded with grim expressions.

“Right. Let’s go.”

“I’ll escort you, Captain. And you as well, Lesser Family Head.”

“You two shut up and stay here to clean up the grime and shit.”

“……”

“……”

* * *

The Murim Alliance resembled a small city.

At its center stood the Alliance Leader’s Hall, and we entered it before stopping in front of a massive door.

“You’ve arrived.”

The guard had a rigid gaze and expression, along with a carefully contained aura.

There was no doubt that he was a Peak master who had reached the level of injuring others with Sword Energy. But the role of this nameless man was nothing more than guarding the door.

He seemed to know Jin Wikyung already. After offering a quiet greeting, he opened the door.

Rattle. Rattle. Rattle.

Scraping sounds rang out one after another. It took five doors opening in succession before the view beyond finally came into sight.

*Good thing I left those idiots behind.*

Gung Gibang and Hyuk Mujin ought to thank me.

If they had followed me, they would probably have been drenched in cold sweat here, unable to open their mouths while filling the room with the stench of dirt and shit.

That was how impressive the people seated around the enormous table were—their faces and auras alike.

“Wow.”

A small gasp escaped from beside me. Jin Wikyung poked Cheongpung in the side as he looked around with wide eyes, then sent a Sound Transmission.

*—This is as far as I go.*

It was easy enough to understand what he meant.

I nodded and stepped over the threshold.

Step.

My footsteps rang out through the quiet.

At the same time, sharp yet impassive gazes filled with awe and curiosity poured toward Cheongpung and me.

“Oh my. So those are the children we’ve heard so much about…”

“Even seeing them again, they’re extraordinary.”

“Hm. They’re not bad.”

“What are you talking about? This is a truly remarkable achievement. It is a blessing for the entire Murim.”

The voices came from both sides, all belonging to elderly men.

Although they had reached supreme realms of martial arts and slowed the aging process, every last hair on their heads was as white as snow. It was enough to give me an idea of how much time they had lived through.

*The leaders of the Nine Sects and One Gang, and the Family Heads of the Five Great Families.*

Fifteen pillars supporting the Murim beneath heaven.

Even during the Star-Array Grand Banquet, which could be called a nationwide Murim event, all of them had never gathered in one place.

The same had been true during the Mount Song Resolution, when the Murim Alliance was declared. Some of them had been unable to arrive in time because of the vast distances involved.

But now, at last…

*They’re all gathered in one place.*

If the Star-Array Grand Banquet had been a celebration of stars that had only just begun to rise, this place was a banquet of giants who had carved their names and footprints into the long history of the Murim.

And even among these giants, several figures radiated an especially immense presence.

Although they were no longer Family Heads, their influence surpassed that of any ordinary family leader. The martial artists of the world called them by names filled with reverence.

One God, Three Saints, and Ten Kings.

Long ago, a hundred-thousand-strong demonic army had surged toward the Central Plains with the blood-red western sky at its back, and heroes had risen to oppose it.

Those heroes had been the swords and spears that cleaved through the enemy, the shields that protected the Central Plains, and, in the end, a vast and radiant legend.

When the sky known as the Martial God disappeared, the three stars that had illuminated it vanished one after another. The ten kings who had stepped down from their thrones gradually died or grew old, but some of them had returned to this place.

*The Azure Sky Sword King, the Thunderbolt Saber King. And…*

There were familiar faces and unfamiliar ones.

But one person among them stood out above all the rest. When he saw me, he raised an eyebrow.

*—How long ago did I call you? And you’re only showing up now? You must be desperate to die.*

Fire King Jeok Cheongang.

His Sound Transmission was gruff, but warmth lay beneath it. A silent laugh escaped me before I could stop it.

*—Look at this bastard. You can laugh at a time like this?*

*What am I supposed to do if it comes out?*

*—Honestly. You were all stiff just now. The Nine Sects and One Gang, the Five Great Families—it doesn’t matter. None of them are anything special. They’re all the same. Our sect is the best.*

Who else could speak so fearlessly?

After that bold and arrogant declaration, another Sound Transmission reached my ears. This one contained a brief hesitation.

*—So straighten your shoulders and open your eyes wide. You… are this old man’s pride.*

Pride.

It was something I had never expected to hear.

Although he hadn’t said it aloud, I had never imagined Jeok Cheongang would say something like that to me.

Unable to hold back, I moved my lips.

*—Old Master.*

Jeok Cheongang, who had been subtly avoiding my gaze, flinched.

*—Ahem.*

*—Old Master.*

*—Wh-Why are you calling me?*

*—It seems like it’s time for you to take your medicine.*

*—You little fucking bastard…*

*—And thank you.*

*—……!*

Jeok Cheongang’s red eyebrows trembled.

I looked away from him and straightened my back.

The muscles throughout my body, which had stiffened from tension, gradually relaxed. My vision cleared.

*I am someone’s pride.*

I still didn’t know what this gathering had been arranged for.

But I knew at least one thing.

The confidence I had briefly lost and then regained had led me to this place.

Step.

Cheongpung and I stopped walking at the same time.

The corridor that had seemed so long and distant had ended. There was nowhere left to go.

The voices of the giants, who had been quietly speaking among themselves while watching us, abruptly fell silent as though they had been waiting for this exact moment.

Silence.

A silence waiting for one person, prepared for one person.

The man seated in the place of honor among the more than twenty giants rose to his feet.

Unlike the others, whose hair had turned completely white, his hair was black, and his eyes were clear.

Rattle.

Three stars had once embroidered the sky spread across the vast world.

Of those three, the Sword Saint Mae Jonghak had become both the brightest and the only remaining star.

He opened his mouth.

No.

*The Murim Alliance’s Alliance Leader, Mae Jonghak.*

That was who stood before us.

And I wasn’t the only one who realized it.

A voice so faint that only I could hear it slipped between Cheongpung’s lips.

“Grandpa…”

A warm smile crossed Mae Jonghak’s lips as he looked at Cheongpung and me.

At the same time, a powerful voice flowed from his mouth.

“The masters of the Two Dragons Pavilion have arrived.”
## Chapter artifact 536

# Chapter 536

Two Dragons Pavilion.

The words reaching my ears were completely unfamiliar—just as unfamiliar as the name itself. And yet, at the same time, I understood.

*The masters of the Two Dragons Pavilion.*

That was referring to Cheongpung and me.

Then, a calm yet powerful voice flowed from between Mae Jonghak’s lips.

“Blazing Flame Divine Dragon Jin Taekyung. Come closer.”

His manner and the atmosphere were completely different.

There was no trace of the man who usually joked around with me and called me his friend.

The person standing before me was no longer Always-Victorious Sword Jongni Chu, nor was he Sword Saint Mae Jonghak.

Step.

After taking a deep breath, I walked forward and respectfully cupped my hands toward the Alliance Leader of the Murim Alliance.

“Jin Taekyung of the Jin Family of Taiyuan greets you, Alliance Leader.”

A light shone in Mae Jonghak’s eyes as he stared at me.

“For generations, the Jin Family of Taiyuan has stood as a symbol of righteous spirit. It fed the hungry, cared for the sick, and whenever the Central Plains was in danger, its members fought without regard for their own lives.”

Three hundred years.

No less than three hundred years.

The Jin Family of Taiyuan had roots deep and sturdy enough to be called an illustrious family. It might have swayed, but it was never uprooted. Its steps might have staggered, but it had never once strayed from the righteous path.

“Two years ago, in winter, you personally cut down Blade of Flowers Jin Baekyang, your own blood relative and the family’s Head Elder. Chief of the Hidden Shadow Pavilion. What was the reason?”

The leader of the Hidden Shadow Pavilion, Thousand-Faced Fox Song Ho, who had been standing silently at attention, opened his mouth with a stiff expression.

“Because he was a traitor. He had been acting in accordance with Dark Heaven’s will for a long time. He was a traitor not only to the Jin Family of Taiyuan, but to the entire Murim.”

“Are you certain?”

“I stake my life on it.”

There was no need to stake his life.

No one present was unaware of the truth.

No. Anyone with even the slightest ear for news from the Murim knew about it.

Then why waste precious time discussing something everyone already knew?

I already had a pretty good idea.

*To remind them once again. And to convince them at the same time.*

Mae Jonghak’s voice, which continued to ring out, was not directed solely at me.

His true targets were the more than twenty giants seated throughout this enormous conference hall.

“One year ago, the Star-Array Grand Banquet was held here in Henan, and Shaolin’s grounds were stained with blood during Dark Heaven’s attack. What did you do?”

I answered Mae Jonghak’s question without hesitation.

“I fought.”

“Why?”

“That was…”

I suddenly closed my mouth.

*Why?*

The question caught me off guard and left me speechless.

Not because I didn’t know.

Because I had never once thought about it.

*Well. Why had I?*

For a long time, I had considered myself a selfish materialist. But that didn’t mean I was a heartless, bloodless bastard. When people were dying right in front of me, where was the time to calculate whether there was anything in it for me?

On the day Shaolin was stained with blood, there had been no question mark in my head. It was filled with exclamation marks. I had run there and fought.

I answered in a relieved voice.

“I’ve never thought about it.”

“Why not?”

“Because it was something any person would naturally have to do.”

“Something any person would naturally have to do…”

Mae Jonghak murmured my answer under his breath, then turned his smiling eyes toward his Disciple and sworn grandson.

“Pung. What about you?”

“Me?”

“Were you not afraid of death?”

Cheongpung stared blankly at Mae Jonghak with clear eyes before answering hesitantly.

“I was afraid. I’d never thought about death even once before.”

“But you went to Shaolin. Why?”

“…Regret.”

“Hmm?”

“I think I would have regretted it for the rest of my life if I’d run away then.”

That was when Cheongpung’s softly murmuring voice grew clear.

“I felt like I would lose something greater than my life.”

That was right. He had said the same thing when we fought the Blood Lord.

Even as he was cut, torn open, and writhing in agony while bleeding an enormous amount of blood, he never retreated. Even knowing he was hopelessly outmatched, he kept charging forward.

*What the hell? Why are you acting like you’re so desperate to die first?*

And when the Blood Lord had asked him that with confusion and anger, Cheongpung had answered with a clear smile.

*If I retreat… I think I’d regret it for the rest of my life.*

That regret.

I knew what it was.

Perhaps I had been more afraid of the years of regret I would have had to endure alone than I was of death itself.

“Regret. So, regret…”

Mae Jonghak muttered quietly, then turned his gaze toward me.

“What about you?”

“Me, sir?”

The answer to that question had never changed—not since the moment I first began working as a Hunter.

I gave a short, quiet laugh and answered.

“Death is always scary. I’m afraid of dying.”

Had I been too honest?

“Ahem. Hm.”

Several of the people who had been silently watching the situation cleared their throats uncomfortably.

But by then, the smile at the corners of Mae Jonghak’s mouth had grown even deeper.

“Overcoming the fear of death and helping someone else in trouble. That is chivalry.”

“……!”

The throat-clearing stopped abruptly. Silence fell over every direction in an instant.

Then a man sitting crookedly in his chair suddenly spoke.

“Something any person should naturally do. But thinking that way and acting on it are worlds apart. And you two acted without hesitation.”

There was warm feeling in his voice. The eyes of Fire King Jeok Cheongang, gazing at me, were unmistakably smiling.

“That is humanity.”

“……!”

Humanity and chivalry.

Chivalry and humanity.

The two words were alike in one sense yet different in another. Brief as they were, their weight pressed down upon everyone in the room.

People say that someone who does not fear death is a true martial artist.

But the world has another name for those who refuse to yield to the fear of death and still act with humanity and chivalry.

“A knight-errant…”

The murmur that slipped between someone’s lips rang out unusually loudly.

That was when a graying middle-aged man with a faint smile opened his mouth.

“A knight-errant. Now that is a word I rather like.”

His hands were strangely large and thick for a man of his relatively modest build.

Only then did I realize who he was.

*Fist King Yan Hwapyeong.*

A distant, dusty past that had long since become old news.

The last descendant of the Jinzhou Yan Family, which had been utterly ruined by power struggles between orthodox factions.

He had turned his back on the world and lived atop an unnamed rugged mountain. But when he heard that a hundred thousand demonic soldiers had invaded the Central Plains, he had joined the Murim Alliance without hesitation.

*“Do you know why the Fist King is such an incredible man?”*

*“How would I know?”*

*“I once asked him whether he had no pride after the orthodox bastards caused his family to fall before he was even born. I asked him how many of the people gathered here even understood human righteousness and chivalry.”*

*“You really have no sense of timing.”*

*“Shut up and listen. What he said next was a masterpiece.”*

*“What did he say?”*

*“He said it didn’t matter.”*

*“What?”*

*“Exactly what I said. Nothing mattered, and he had simply come to help. Then, as soon as the Great Faction War ended, he disappeared like a phantom. No matter how I think about it, that man was the real thing. Ha ha ha.”*

That very Fist King Yan Hwapyeong was looking this way now, smiling.

It was a smile filled with warm feeling.

“Doing what is only natural. Overcoming fear and moving forward. That is what makes someone a knight-errant. Indeed.”

Yan Hwapyeong was not the only one nodding with a satisfied expression.

People throughout the room were looking at Cheongpung and me with gentle gazes.

Several familiar figures in particular were sending us looks that contained unmistakable gratitude.

*Myriad-Poison Asura Tang Sadok.*

Although his complexion was pale, as if he had yet to fully recover, his posture remained straight and the green light in his eyes was clear.

When our gazes met, he slightly tugged at the corner of his wrinkled mouth before suddenly speaking.

“As the Family Head of the Sichuan Tang Clan, I would like to say a few words.”

Everyone’s attention focused on him at his unexpected statement.

Mae Jonghak gave a small nod, and Tang Sadok continued in his hissing voice.

“Being a pavilion master of the Murim Alliance is a position of tremendous weight and responsibility. I believe it requires not only outstanding martial arts, but also the experience to match. It would be unreasonable to entrust it to young people who are not even thirty, let alone forty.”

A small stir spread through the room at his unexpected words. At the same time, several people’s expressions changed slightly.

Feelings such as joy and displeasure passed over various faces.

But…

*The rule about listening to the whole sentence before judging it doesn’t only apply to Korean.*

And Tang Sadok’s next words turned my suspicion into certainty.

“However, Blazing Flame Divine Dragon Jin Taekyung and Huashan Divine Dragon Cheongpung are the exceptions. These two have fought Dark Heaven in Shanxi, Henan, Sichuan, and Hubei, and shown us what humanity and chivalry truly are. This old man and my family have incurred a debt we dare not claim we can repay.”

Voices of agreement rose from various parts of the room.

They belonged to the heads of sects and families who had crossed paths with me personally throughout the Murim, or through Jeok Cheongang or the Jin Family of Taiyuan.

There were also people who nodded as though it were only natural, despite having no connection to me at all.

Encouraged by this response, Myriad-Poison Asura Tang Sadok continued in a clear voice.

“If these two take on important positions within the Murim Alliance, who would dare question their qualifications or object to the Alliance Leader’s command?”

Several people frowned at the unusually forceful emphasis in his words.

The Wind-and-Cloud Sword Lord, the Sect Leader of the Zhongnan Sect, was one of them.

Tang Sadok slowly swept his gaze across the room, his eyes glowing green, then cupped his hands.

“As you can see, there will be no objections whatsoever. Alliance Leader, you need only give the order without concern.”

It was a masterful bit of rhetoric that killed the controversy before anyone could voice a complaint.

Besides, anyone who did object would be taking on the Family Head of the Sichuan Tang Clan—the Murim’s quintessential no-brakes clan.

Although the Sichuan Blood Tragedy had inflicted tremendous damage on the Sichuan Tang Clan, the fact remained that it was one of the Five Great Families and possessed strength no one could afford to disregard.

“Hmm…”

Someone let out a heavy groan.

Then a voice broke the brief silence.

“Blazing Flame Divine Dragon Jin Taekyung. And Huashan Divine Dragon Cheongpung.”

Mae Jonghak continued, gazing at Cheongpung and me with warm eyes.

“I have not yet asked the two of you. Do you wish to join the Two Dragons Pavilion?”

That was when—

Ding.

> **System**
>
> Would you like to join the Murim Alliance?

Neither Cheongpung nor I needed long to think.

We met each other’s gaze and answered as one.

“We will.”

“Then I hereby formally decree this. From this moment onward, the two of you shall belong to the Two Dragons Pavilion, directly under the Alliance Leader’s Office and answerable only to the Alliance Leader’s commands. Each of you shall become a pavilion master, with the authority to select the personnel you require…”

I could no longer make out the words that followed.

No. I couldn’t hear them properly.

Ding. Ding. Ding, ding!

The bells rang without pause, filling my ears.
## Chapter artifact 537

# Chapter 537

“The tea smells wonderful.”

The first to speak was a middle-aged man with graying hair.

Considering that he was actually past sixty, he looked at least ten years younger than his age.

But the face he turned toward the man seated across from him, with a teacup between them, was rigid with inexplicable tension and displeasure.

“Great Hero Mae. No—the Alliance Leader.”

The leisure to enjoy the fragrance of tea was granted only to those who had emptied their minds.

In the end, unable to hold back his impatience, the middle-aged man spoke again. Sword Saint Mae Jonghak smiled faintly.

“I’m listening. What is it?”

“You already know, don’t you? About the Thousand-Faced Fox…”

“He’s the Chief of the Hidden Shadow Pavilion.”

“Yes. That very Chief of the Hidden Shadow Pavilion must have already submitted a report.”

“What report?”

“If you truly haven’t heard, then yes, I’ll tell you myself.”

If the other side intended to pretend ignorance, he had to show his hand first.

Biting down hard on his lip, the middle-aged man—Hwangbo Gun, Family Head of the Hwangbo Family—spoke.

“It concerns my son.”

Mae Jonghak’s eyes widened.

“You had a son?”

“Alliance Leader!”

Hwangbo Gun raised his voice without realizing it, then lowered his head with an expression of regret.

Even if they had shared a connection on the battlefield once, the man before him was now the Alliance Leader of the Murim Alliance.

The Sword Saint Mae Jonghak of the past had been the sort of person who responded to anything with a good-natured smile and let it pass. But committing an offense against the Alliance Leader could narrow the Hwangbo Family’s position considerably.

“I-I apologize. It concerns my son, so I was rude without realizing it.”

Mae Jonghak lifted his teacup with a bright, guileless smile that belied his age.

“Don’t worry about it. These things happen. How many times did we fight together on the battlefield?”

“I’m grateful to hear you say so.”

Some color returned to Hwangbo Gun’s face.

It was an old connection from a distant past, and their positions were now as different as heaven and earth, but Mae Jonghak clearly remembered the bond they had shared back then. Perhaps things might work out after all.

“I’ll get straight to the point. The reason I requested this private audience is…”

The events of only a few hours earlier rushed from between Hwangbo Gun’s lips.

They were exaggerated stories, embellished just enough to differ subtly from the truth. But in Hwangbo Gun’s mind, the matter was clear.

*How dare they do such a thing!*

His only son had been born when he was nearly forty. No matter how much trouble the boy caused, Hwangbo Gun had looked the other way. Even when scandals involving women never seemed to end, he had paid them no mind.

But that precious son had supposedly been subjected to every kind of humiliation in front of countless watching eyes.

To Hwangbo Gun, this was something he could never overlook.

“How can this possibly be acceptable? Even if the principles of the martial world have fallen into the dirt, how could some spawn of the demonic, heterodox arts attack the Lesser Family Head of the Hwangbo Family? And furthermore…”

Hwangbo Gun’s anger-laced voice abruptly dropped.

“An orthodox martial artist who witnessed such injustice and still protected that spawn of the demonic, heterodox arts could no longer be called orthodox, could he? Blazing Flame Divine Dragon Jin Taekyung. I’m speaking of that man.”

“I see. That happened.”

Clink.

Mae Jonghak set down his half-empty teacup and tilted his head.

“But what is it you want, exactly?”

“Pardon?”

“I’ve heard your story, and I understand what happened. So now, tell me what you want.”

Hwangbo Gun stared at Mae Jonghak without speaking, then uttered a single word.

“Punishment. I want appropriate punishment.”

“For example?”

“I had my retainers look into it, and they say the man who attacked my son was a member of the Black Dragon Demon Gate in Gansu.”

“The Black Dragon Demon Gate. I see. Very well.”

Mae Jonghak nodded immediately, and Hwangbo Gun’s expression brightened considerably.

Believing that the Alliance Leader had taken his side, Hwangbo Gun’s voice gained even more force.

“And I believe Blazing Flame Divine Dragon Jin Taekyung should be disciplined as well.”

“Disciplined…”

“As you know from what I’ve told you, didn’t he side with the demonic, heterodox faction even though such an incident happened right before his eyes?”

“That is true as well.”

“That such a man is a pavilion master of the Murim Alliance… It is deeply regrettable, not only to me but to many others.”

He had done his best to soften the matter with the word *regrettable*, but this was precisely the point that had infuriated Hwangbo Gun the most.

*That young punk is a pavilion master?*

Pavilion master was no ordinary position in the Murim Alliance. It was a high-ranking post within the Alliance, placing its holder among roughly the top twenty in the hierarchy. A pavilion master also possessed tremendous authority, with multiple groups and squads under his command.

*He is directly under the Alliance Leader’s Office, so he can’t have subordinate units of his own. But a pavilion master is still a pavilion master. How does that make any sense?*

Even Hwangbo Gun’s son, considered one of the greatest young prodigies in the Murim, was still uncertain to receive the position of Squad Leader.

Yet Jin Taekyung had already risen to a position immeasurably higher.

And when Hwangbo Gun considered how the momentum of the Jin Family of Taiyuan had recently reached even the Shandong region where the Hwangbo Family was based, this was something he had to stop by any means necessary.

“The appointment of the Huashan Divine Dragon as pavilion master is a blessing for the Murim and something we should welcome with both hands. But Jin Taekyung…”

Hwangbo Gun deliberately let his voice trail off as he glanced sideways at Mae Jonghak.

Their conversation had gone smoothly so far. The hopeful look in his eyes said he expected Mae Jonghak to understand exactly what he meant.

The answer that came next far exceeded his expectations.

“Now that I think about it, your words do have plenty of merit. I’ll consider not only disciplinary action against him, but personnel measures as well.”

“Th-Thank you, Alliance Leader!”

Discipline, and personnel measures on top of that?

Hwangbo Gun’s joy was even greater because he had never expected things to go this well.

Mae Jonghak watched him bow repeatedly with a smile, then suddenly murmured,

“The teacup is empty.”

“Pardon? Oh.”

“Time really flies these days.”

Hwangbo Gun paused for a moment. Then he understood what those words meant and rose from his seat.

No matter that he was the Family Head of the Hwangbo Family, how could he continue taking up the Alliance Leader’s valuable time?

By then, the time allotted for their private audience—the time it took to drink a cup of tea—had already passed.

“I suppose I stayed too long. Ha ha.”

“Hm? Are you leaving?”

Those words, at least superficially an attempt to hold him back, warmed Hwangbo Gun’s heart.

He had gained more than he had expected, and he was grateful for Mae Jonghak’s consideration in preserving his dignity. The comradeship they had forged during the Great Faction War felt even stronger now.

“I can’t keep taking up your valuable time. I’ll take my leave, Alliance Leader.”

“Then I suppose it can’t be helped.”

“Yes, then I’ll be going.”

“Take care. Let’s meet again sometime.”

Pat, pat.

Daring to pat the shoulders of the Family Head of the Hwangbo Family.

If anyone else had done it, Hwangbo Gun would have been offended. But this was the Number One Sword Under Heaven and the Alliance Leader of the Murim Alliance.

Instead, Hwangbo Gun withdrew with a broad smile on his face.

It was immediately afterward that—

Clack.

The door opened within moments, and someone entered the office. The prosthetic leg fitted over one of his legs made a dull sound against the floor.

“For the Family Head of the Hwangbo Family to request a private audience over something this trivial… He must have been awfully desperate.”

“That fellow seems to have neglected his martial arts training. His personality has changed a bit, too.”

“Pardon?”

“It’s nothing. Have a seat.”

Mae Jonghak glanced down at the hand that had patted Hwangbo Gun’s shoulder, then gestured for the newcomer to sit.

The Chief of the Hidden Shadow Pavilion, Thousand-Faced Fox Song Ho, cast a brief glance at the teacup Hwangbo Gun had not even half emptied before speaking.

“There are people dissatisfied with the recent appointments.”

“Hmm. Is that so?”

“Before the Family Head of the Hwangbo Family requested this private audience, they held a secret meeting.”

“That can happen.”

“It seems they egged the Family Head of the Hwangbo Family on rather than confronting you directly.”

“Now that I think about it, Hwangbo Gun has always had a tendency to put himself forward. He even stood at the vanguard when the battle broke out in Guizhou.”

“……Hoo.”

At Song Ho’s sigh, Mae Jonghak’s eyes widened.

“Hm? What is it?”

“That isn’t what we’re discussing right now.”

“In the end, it’s all a matter of people, isn’t it? Ha ha.”

Song Ho was about to answer, then stopped.

It wasn’t wrong. In the end, it was a matter of who did what, and how.

From time to time, Mae Jonghak would casually toss out a few words like that, and Song Ho would sense some profound insight hidden within them.

“Regardless, you made a promise to the Family Head of the Hwangbo Family that you cannot keep.”

“A promise?”

“Didn’t you say you would impose disciplinary action and appropriate personnel measures on the Black Dragon Demon Gate and Blazing Flame Divine Dragon?”

“Oh, right. I did. As it happens, I’m thinking about that very thing right now.”

“Alliance Leader, that…”

“Wait. Just wait a moment.”

Mae Jonghak scratched his chin. Only an instant passed before he spoke again.

“All right. I’m done. Then let’s pretend the whole thing never happened.”

“Pardon?”

“I considered it carefully, and I don’t think personnel measures are necessary after all. Discipline should be imposed, but I’ll have to think about that later.”

“……!”

Song Ho stared at Mae Jonghak with trembling eyes, then let out a hollow laugh.

“Of course. You only said you would consider it, Alliance Leader.”

“Even so, he was once a comrade I fought alongside. Shouldn’t I keep my promise?”

“The Family Head of the Hwangbo Family is going to grab the back of his neck.”

“Uh, don’t you think he might understand?”

“Ha ha. Who knows?”

“I meant it sincerely. But if he can’t understand, then it can’t be helped.”

Song Ho forcibly swallowed his laughter.

Mae Jonghak was far more suited to the position of Alliance Leader than he had expected.

He was naturally easygoing and, without needing to think too deeply or act deliberately, simply brushed everything off with *That can happen.* No matter how much pressure came from those around him, it never affected him.

*His principles are upright, and his resolve is firm.*

This was beyond expectations. Song Ho called to Mae Jonghak sincerely.

“Alliance Leader.”

“What is it?”

“I just felt like calling you.”

“Hmm. That can happen.”

“Ha ha ha!”

Mae Jonghak tilted his head at Song Ho’s loud laughter, then spoke.

“Oh, right. How are matters with the Nanman Beast Palace and the North Sea Ice Palace being handled?”

The smile vanished from Song Ho’s lips as he answered.

“We still haven’t received replies from either of them. We sent letters to both earlier than planned, but given the distance…”

“I see.”

“Yes. But as you know, the situation with the Green Forest Alliance and the Yangtze River Channel League is very favorable. Both their leaders have even expressed their intention to come to Henan personally.”

Although they did not belong to the orthodox Murim, the leaders of those two organizations were unquestionably giants of the martial world.

Their forces rivaled those of the great orthodox sects, and they possessed outstanding masters.

“If they join us, they’ll be a great help.”

Mae Jonghak gave a small nod, then suddenly spoke again.

“Oh. About the discipline.”

“The discipline? Ah. Yes.”

“I’ll dictate it now. Write a letter and deliver it to Blazing Flame Divine Dragon—or rather, Chief Jin.”

“As you command.”

Song Ho respectfully cupped his hands.

Jin Taekyung’s role going forward would be extremely important.

Even if the punishment was severe, he had to retain his position as pavilion master.



* * *

I thought my eyes and ears were deceiving me.

“Disciplinary action? Me?”

A martial artist from the Alliance Leader’s Office nodded.

“Yes.”

“Why all of a sudden? And this punishment is too harsh.”

“I delivered the message exactly. Then I’ll be going.”

Whoosh!

*What kind of situation is this supposed to be?*

As I stared blankly at the martial artist’s back as he vanished like the wind, Hyuk Mujin approached and asked cautiously,

“Disciplinary action? What kind of punishment is it?”

With a deep sigh, I answered.

“They said I have to fast.”

“Pardon?”

“They said I have to skip dinner.”

“……?”

“Ugh, I was going to have roast duck tonight.”

I grumbled under my breath, then kicked Hyuk Mujin in the butt.

“Enough. Let’s go.”

“What kind of punishment is that? And where are we going?”

“Recruiting teammates.”

“Whaaat?”
## Chapter artifact 538

# Chapter 538

I asked Hyuk Mujin, whose eyes were wide with surprise.

“What are you so surprised about? Once you become a pavilion master, of course you have to recruit people.”

“No, that’s true, but…”

“But what?”

Hyuk Mujin answered with a face full of disbelief.

“I’m more concerned about the disciplinary action. What is that bizarre order supposed to be? It’s like some children’s prank.”

“I heard our Alliance Leader personally issued that bizarre order that sounds like a children’s prank.”

“Hmm. Come to think of it, there must be some profound meaning behind this disciplinary action. Clothing, food, and shelter are the most important things in life, and among those, being ordered to skip dinner must have some deep significance…”

“……”

Don’t force meaning onto it, you idiot.

They say that once you become famous, people will applaud even when you take a shit. That saying fit the current situation perfectly.

I gave Hyuk Mujin a deep, meaningful look as he instantly changed his tune the moment I mentioned Mae Jonghak’s name.

“You think it’s bullshit too.”

“……Yes.”

“Then shut up and follow me. Don’t worry about the punishment, either.”

Shaking my head, I opened the door and stepped outside. Hyuk Mujin hurried after me, muttering as he went.

“Isn’t it stranger not to be concerned? You were appointed pavilion master less than two shichen ago, and you’re already being disciplined. Did you perhaps take a dump in the Alliance Leader’s room?”

To think I had to hear that from the guy who had singled me out as the one person who had taken a dump in a crowded inn. I clicked my tongue softly and answered.

“That’s a filthy but imaginative thought. You’re close, but wrong.”

“If you’re close but wrong, did you perhaps pee?”

……This bastard.

I held back the urge to punch him and answered.

“Apparently, some people are feeling shitty about me becoming a pavilion master.”

“Oh.”

“Well, isn’t that just how the world works?”

Pavilion Master of the Two Dragons Pavilion.

That was my official title.

At first, I rather liked the unexpectedly cool-sounding name. Then I was surprised to learn that a pavilion master of the Murim Alliance held a much more impressive position than I had imagined.

*I didn’t realize it was this important.*

That was how much prestige the title of pavilion master carried.

Directly beneath a pavilion master was a regiment, and the various squads belonging to it were also included in the organizational structure.

Considering the current size of the Murim Alliance, it was a position of great responsibility, commanding anywhere from several hundred to more than a thousand martial artists.

*Not a position someone my age could even dream of.*

To be honest, until now, the organizational structure of the Murim had been none of my concern.

If I had to name anything resembling a career qualification, it would be the time I served as captain of a reconnaissance unit when war broke out between the Jin Family of Taiyuan and the Mount Heng Sword Sect.

After that…

*I traveled like a madman.*

As if I had a wandering star in my fortune, I had done nothing but move from place to place after descending from Mount Jiuhua following a year of training.

I had traveled so constantly that I sometimes wondered whether my role in the Murim was that of a martial artist or a traveling peddler.

But my long career as a freelancer had come to an end today.

The problem was that several company executives who were unhappy about my conversion to a full-time employee were standing firmly in my way.

“Who do you think they are?”

“Who else could they be?”

“Hmm. There are some names that just came to mind…”

“Then forget it. It’s one of the names you’re thinking of anyway.”

The Hwangbo Family was probably the biggest reason for this punishment, but there was no need to explain every little detail to Hyuk Mujin.

*Well, I expected something like this to happen.*

Even someone kindhearted and friendly to everyone couldn’t escape envious, jealous looks.

If the world could bounce around a round person like a balloon, what would it do to a sixteen-sided polygon like me, with all my sharp edges and corners?

*No. This is better, actually.*

Compared to a balloon that lost its air every time someone poked it with words or weapons, a sixteen-sided polygon that didn’t suffer so much as a scratch when poked was obviously better.

That was how Jin Taekyung had lived until now.

And that was how he would continue to live.

“If they keep poking me, I can just smash them when the time comes.”

“What?”

“Nothing. Let’s go.”

I lightly smacked Hyuk Mujin on the back of the head when he stared at me in confusion at my muttered words, then continued walking.

The news of the Murim Alliance’s new young pavilion master must have already spread, because the gazes of the martial artists walking along the main road were burning with interest.

“Do you see him over there? That’s Blazing Flame Divine Dragon Jin Taekyung…”

“Shh. Don’t call him by name so casually. Haven’t you heard the rumors? He’s an official pavilion master of the great Murim Alliance now.”

“Good grief. Is that really important? Don’t start an argument over something so trivial. He’s barely twenty, young enough to be my son. Just a kid.”

The middle-aged martial artist’s companion clicked his tongue at the dismissive comment.

“A kid? Did practicing martial arts alone harden your brain?”

“What did you say?”

“Isn’t that obvious? You look like you’re also a member of the Murim Alliance, Brother. Then Great Hero Jin is practically your superior. And you may be old, but you don’t even look like you have a son.”

“No, that part is true, but… What does that have to do with anything?”

“I’m worried I’ll get dragged into this too. The Enforcement Hall martial artists belonging to the Alliance are already roaming around Henan with their eyes wide open. I don’t want to be hauled away alongside you for insulting a superior.”

The middle-aged martial artist’s face twisted.

“Are you picking a fight with me?”

“I’m not picking a fight. No, forget it. This is why you still haven’t managed to get married at your age. Watch that blabbering mouth of yours.”

“Fine. Got it, you fucker.”

“What was that? You goddamn son of a bitch…”

Are these people insane? Seriously. How do they even manage to fight like that?

*Are they some kind of battle species?*

Now that I thought about it, perhaps the planet where the Murim existed was actually Planet Vegeta.

With that perfectly reasonable suspicion in mind, I looked around for anyone with yellow hair, and other people’s whispers drifted into my ears.

“What do you think? Should I make an impression on him now?”

“Are you thinking of applying to the Two Dragons Pavilion?”

“Hmm. I’m considering it. Blazing Flame Divine Dragon may be much younger than me, but I’ve heard that as a martial artist, he can already rival the Sect Leaders of the great sects.”

“Could he really be that strong? And even if the Blazing Flame Divine Dragon’s martial arts are as impressive as the rumors say, you should stay away.”

“Why?”

“Think carefully about everything the Blazing Flame Divine Dragon has done until now. Even if he has the worst luck in the world, how does he manage to choose nothing but deadly situations every time he moves? Accomplishing great deeds is all well and good, but if someone at our level joined the Two Dragons Pavilion, whew.”

“Still, shouldn’t we accomplish something?”

“If you want to erect your own tombstone first, go ahead. Besides, the Two Dragons Pavilion has two pavilion masters, not one. The Huashan Divine Dragon might be a better choice. Isn’t he the youngest Disciple whom the Alliance Leader raised like his own grandson? The Alliance will probably take care of him in various ways.”

“You might die even faster if you go there.”

“Hm? Why?”

“I heard the snake the Huashan Divine Dragon keeps with him bites people.”

“……Oh dear.”

Talk about a fast-spreading rumor.

It suddenly occurred to me that if this were modern times, the Murim Alliance would already have an online petition board.



[The Huashan Divine Dragon’s snake bit me between the legs. I demand punishment. Please show your support and interest.]



Thousand-Faced Fox*: Agreed.

Gung Gi*: Agreed.

Jeok Cheon*: LOL, that, snake, bastard, I knew, something like this would happen,,~~!

Cheong*: No, Mimi doesn’t bite people.

Tang Sa*: Ah, Mimi…



The moment the comments piled up and the number of people agreeing to punishment reached ten thousand, Mimi’s fate would be decided. Hmm.

That was when I was spreading my imagination’s wings.

“It’s been about half an hour, hasn’t it? I heard that a commoner passing along the main road earlier saw the snake and was so startled that he fell while backing away. He suffered a minor injury.”

“Oh dear. And then?”

“I heard that some young medical apprentice who was with the Huashan Divine Dragon took him to a medical clinic. Since it happened because he startled himself, it isn’t that serious—ugh.”

The martial artist who had been speaking swallowed a startled breath.

I had already approached to within one step of him.

His gaze trembled violently as he looked at me.

“G-Great Hero Jin?”

“Ah, don’t be startled. It’s nothing serious. I just wanted to ask you something.”

“W-What do you want to ask me?”

“Where is that medical clinic?”

“The clinic? Ah, if you go straight in that direction…”

The martial artist, stiff with surprise at the sudden situation, raised his hand and pointed the way.

I gave him a small nod of thanks and turned in the direction he indicated. Hyuk Mujin asked with a puzzled expression,

“Why are you suddenly going to a medical clinic?”

“I told you. I’m going to find a teammate.”

“What? Then are you looking for Young Hero Cheongpung?”

“……Does that make any sense?”

This wasn’t some Cheongpung team without Cheongpung.

Cheongpung was now an official pavilion master in his own right. There was no way I could drag him under my command.

“Try thinking before you speak. Think.”

“Then who else is there to recruit there besides Young Hero Cheong—”

Hyuk Mujin stopped mid-sentence and opened his eyes wide.

“No way. Right?”

“Who knows?”

I gave him an ambiguous answer, then quietly muttered to myself.

*Open the Quest window.*

Ding.

A translucent holographic window suddenly appeared in midair with a cheerful notification sound.

It was the first Quest generated at the same time I joined the Murim Alliance as Pavilion Master of the Two Dragons Pavilion.



> **System**
>
> **Quest**
>
> **Become My Companion!**
>
> At last, you have become a member of the Murim Alliance and have been appointed Pavilion Master of the Two Dragons Pavilion.
>
> However, an individual cannot become an organization. Therefore, the Murim Alliance has entrusted you with the authority to appoint personnel.
>
> Find new members as quickly as possible, form your organization, give it a name, and become a true pavilion master in every sense of the word!
>
> **Grade:** Peak
>
> **Restriction:** Jin Taekyung
>
> **Mission:**
>
> Secure at least five companions (Incomplete)
>
> Give the organization an appropriate name (Incomplete)
>
> **Reward:** ???
>
> **Failure:** Acquire the Title “Loner”



“……”

Look at that Title. Fuck.

If I failed this Quest, I would become an outsider officially recognized by the System.

I had to succeed. And considering the difficult things that lay ahead, I needed to choose my members with even greater care.

*Exclude anyone who would follow me without needing to be asked. I need someone I can persuade first and pull over to my side. At the same time, it has to be someone who can provide significant help.*

That was what came to mind the instant I checked the Quest. And I didn’t have to think for long.

The first person I needed to recruit had practically been decided from the beginning.

*His personality is pretty damn nasty, but…*

He was someone who could help me in all sorts of ways.

Whatever. I might as well give it a shot.

After taking a deep breath, I headed toward the medical clinic.



* * *



“Tony Tony Cho—no, Mungyeong. Become my companion!”

That lunatic’s condition must have flared up again.

It wasn’t even surprising anymore. It had always been this way.

Jin Taekyung had called Mungyeong out of the blue, saying that the two of them had something to discuss privately, only to start spouting nonsense.

Mungyeong regarded him with a deep, somber gaze.

“No.”

“No, why not?”

The question itself was ridiculous.

Why not? There were countless reasons. But Mungyeong currently had the most appropriate answer.

“Because I’ve already decided to join another place.”

“……What?”

“You’re too late. Isn’t that right?”

“Ah, sorry, Benefactor.”

A voice suddenly rang out, followed by the appearance of another person.

Jin Taekyung’s eyes widened as he looked at Cheongpung.
## Chapter artifact 539

# Chapter 539

The Slaughter Saint.

A man who entered this world as an assassin despised by everyone, then finally became a star that illuminated the heavens.

He tore down the fence that only the chosen were permitted to cross and became living proof of the four-character principle: Might Makes Right.

Yet most people did not know his age, his appearance, or even his name. Assassins were extremely secretive and never revealed themselves.

Even after several decades, the veil hanging over the name Slaughter Saint had not been lifted.

The Slaughter Saint had vanished without a trace immediately after the war ended. He did not show himself even once for a long time, and the words that spilled from the mouths of ordinary people traveled a thousand li, ten thousand li, without needing feet.

The Slaughter Saint is dead!

Half of that was true, and half of it was false.

On the day the Heavenly Demon was defeated by the Martial God and a hundred thousand demon soldiers fell—

An old man wearing a bamboo hat had buried something on an unknown hill before leaving.

It was not only his cherished weapon, stained with blood.

He had buried the name Slaughter Saint as well.

And so the Slaughter Saint died, while Mungyeong entered the world.

The world began calling him by another name.

The Divine Physician.

The tributaries of the Yangtze may divide into many branches, but in the end, their currents all connect to a single river.

In that sense, Mungyeong was a river as well—a river with two names. He was both the greatest assassin in history and the greatest physician under heaven.

To put it simply…

*He’s my number-one recruitment target.*

That was more than enough to qualify him as a passenger aboard my Going Murim ship.

Of course, if I stayed with him, I would probably find myself on the receiving end of assassination attempts from time to time. But in my view, shitting blood a few times was far preferable to dying after running into a monster like the Western Heaven Demon Lord.

Black cat, white cat. It didn’t matter whether the cat was black or white, as long as it caught mice.

It was deeply unfortunate that my first recruitment target was not a cute horned deer but a former assassin who wanted to kill me about three times a day. But this was not a matter of choice.

*Who cares about his personality? He has the strongest damage output and healer abilities, too.*

Right. That was enough. What more did I need?

In this harsh Murim, where I could not even find a single cheap potion, I absolutely needed Mungyeong.

Even if it wasn’t me, Mungyeong might one day save the life of someone traveling with us when they found themselves in grave danger.

The biggest problem was that my confidence had caused me to overlook the existence of one person.

“Hehe.”

“……?”

“Hello, Benefactor.”

“……!”

Hello, my ass. How did this happen?

*No way.*

Staring at Cheongpung with trembling eyes, I somehow managed to force out my voice.

“……Why are you coming out of there?”

“Oh, well. I was passing by earlier.”

“No, I know why you came here. That’s not what I mean.”

This was driving me insane. Seriously.

I was so flustered that I could barely speak. Mungyeong stared impassively at my stammering self and gave me the answer instead.

“I told you. You were one step too late.”

Cheongpung smiled brightly and joined in.

“Hehe. That’s what happened, Benefactor.”

It was the one blow that turned my suspicion into certainty.

After silently looking back and forth between them, I finally managed to part my lips.

“Is this for real?”

Mungyeong nodded.

“It probably isn’t a legend.”

“Then it really happened?”

“Yes. It really happened.”

“Why?”

“There is no reason I need to tell you that.”

“That’s true, but I think I’ll be able to give up cleanly if I hear it directly.”

Mungyeong clicked his tongue softly.

“You are being remarkably filthy.”

“What if I still want to hear it, even if I have to be filthy?”

“Then I should find a cleaner method.”

Shing.

Something glinting silver emerged from the end of his long sleeve.

I rubbed my eyes after confirming that the short sword had popped out like a jack-in-the-box.

“Have I been so tired lately that my eyesight is getting worse? Why is that coming out at this point?”

“Because using this would be clean.”

“That’s true, but wouldn’t the surroundings get messy?”

“It does not matter. I know several methods.”

“……”

He must have learned quite a few useful tricks during his many years as an assassin.

And I had not the slightest intention of personally experiencing any of Mungyeong’s excellent tricks.

“Whew. I’ll be going now.”

“Go. Forever.”

“See you later, Benefactor!”

With the greetings of two people whose temperatures differed dramatically, I turned away and muttered to myself.

*Wow. This is driving me crazy.*

Who would have thought Cheongpung would get ahead of me? I truly had not anticipated this development in the slightest.

The Cheongpung I knew should have been standing there with a meat dumpling in one hand and a vegetable dumpling in the other, wondering which one to eat first.

*Did he put points into Intelligence for me…?*

Now that things had come to this, I had no choice. I would have to recruit the others quickly.

Hyuk Mujin had been loitering near the entrance to the medical clinic. The moment he saw me, he came running.

“Did everything go well—… You don’t look like it went well.”

Hyuk Mujin blinked after hurriedly correcting himself upon seeing my face.

“I don’t see Mungyeong. Then could it be…?”

“Can’t you tell by looking?”

“Good heavens. He refused the Captain’s offer? That fellow knows how to judge his own interests better than he looks— No, I was joking. Please, I beg you, lower your fist.”

“Make one more joke and it will become your last will.”

Hyuk Mujin backed away to secure a safe distance before speaking in a solemn voice.

“There is one method.”

“A method?”

“Yes.”

His attitude was so confident that my ears perked up. I asked him with the feeling of someone clutching a rotten rope.

“What is it?”

“How about I try talking some sense into him? That fellow Mungyeong would do anything I say.”

“……”

Do anything I say, my ass. He’d kill you in the blink of an eye.

If Mungyeong wished, he could turn Hyuk Mujin into a corpse with a single inhale and reduce him to powder with a single exhale.

“Mujin…”

“Don’t worry. We’ve built up a fair amount of affection over the years. If Young Hero Gung and I go and persuade him, he won’t refuse us coldly.”

“That’s not what I mean, you bastard……”

This bastard was actually trying to commit group suicide now.

I looked at Hyuk Mujin with pity.

“You really hate brothels, huh?”

“What?”

“Never mind. Anyway, don’t try to marry him—no, persuade him. Absolutely not.”

“Why not?”

“Just don’t, you bastard.”

Hyuk Mujin did not know Mungyeong’s true identity, so there was no way their conversation could go anywhere.

I let out a deep sigh as I looked at his aggrieved expression, then spoke.

“Can you write?”

“Writing? Wang Xizhi himself would weep and retire.”

“Answer properly before I beat you until you cry.”

“……I’m decent enough. Believe it or not, people called me a prodigy when I was young.”

“Then write a few large notices and put one up.”

“A notice?”

“Yes. Since things have turned out this way, let’s find some proper talent.”

The world was vast, and there were many masters.

And Henan right now was a future king’s court, teeming with countless dragons and tigers.

*What’s so special about holding a public audition?*

If you thought about it, even the imperial examinations were the most traditional audition program in existence. With my fame and eye for talent, it was worth trying.

I imagined the applicants flooding in and muttered to myself.

*Let’s give it a shot. Fuck it.*

* * *

Shik, sssshk!

It was a fast and flexible movement unlike anything anyone had ever seen.

Whenever his hands moved as if dancing, the tip of the large needle flashed, and thread stitched the wound closed.

It took only moments for a swordsman who had been slowly dying from a deep slash across the abdomen to be given a chance at survival.

“How can someone so young possess medical skills of this level…!”

“I have never even heard rumors of a medical apprentice like this.”

“Good heavens. Is this not a skill approaching the divine?”

The physicians gathered in one place ranged from middle-aged men with considerable beards to white-haired elders.

They watched the scene before them with stunned expressions until a voice rang out and brought them back to their senses.

“Finished.”

Tap.

The treatment had ended as quickly as lightning.

Even more astonishing than its speed was the fact that the treatment itself was flawless.

The physicians stood with their mouths hanging open in shock and looked toward the owner of the voice, who was rising from his seat.

“H-How can this be?”

“Hey!”

He was too young to be called a young man, yet he carried an oddly mysterious air that made it difficult to call him a boy.

Mungyeong gathered his belongings and stood.

“Are there still patients remaining?”

The physicians looked at one another, then all shook their heads at once.

“N-No, but…”

“Th-That’s right. It’s all thanks to you.”

This was not the first astonishing sight the young medical apprentice had shown them.

It had been about one shichen earlier. He had brought in a lightly injured patient from somewhere, glanced over the patients lying down, and casually said one thing.

*This will be over quickly.*

He then treated the patients one by one. His speed and treatment had been so swift and perfect that even the physicians who had approached intending to scold him and throw him out could not bring themselves to leave.

*Could medicine like this truly exist under heaven?*

*Who in the world is he?*

They had waited until now to ask about his identity. But when they finally did, the young medical apprentice’s answer was utterly calm.

“Then that settles it. I’ll be going now.”

“W-Wait a moment. I have a mountain of questions to ask you!”

“What is your master’s name? Could it be…!”

As the questions came pouring in, Mungyeong dipped his head slightly.

“If I have time, I will stop by once before I leave and check the patients’ conditions.”

“You may have been free to enter, but you’re not free to leave!”

“Grab him!”

“I’m sorry! But we can’t let you leave like this!”

Whoosh! Crash!

But the hands of the physicians who hurled themselves forward in desperation grasped nothing but empty air.

They failed even to brush against his collar and went tumbling across the floor. Just as they were staring around in bewilderment, Mungyeong’s voice rang out.

“I left a prescription suited to each patient in the place where I was sitting. Examine them and treat the patients accordingly.”

“What? What did you say? Prescriptions?”

“Where are they? Where?”

To physicians, a renowned doctor’s prescriptions were like a peerless master’s martial arts manual.

As the physicians, their eyes half rolled back, engaged in a fierce struggle over dozens of prescriptions, Mungyeong quietly walked outside.

Then he suddenly spoke.

“Come out.”

Swish.

With a faint sound, a figure hiding behind a large pillar emerged.

“Oh! How did you know?”

“Just because.”

“You really are amazing. I thought I could fool you this time. Hehe.”

Mungyeong stared at Cheongpung’s bright, smiling face.

“What martial art is that?”

“Footwork technique.”

“I know that.”

“Oh, I named it Mimi Step.”

“Mimi Step?”

“Yes. I named it after our Mimi. Isn’t it cool?”

The answer to Cheongpung’s sparkling eyes was cold.

“……What an utterly ridiculous name.”

“Oh. Ah…”

Cheongpung’s spirits sank completely.

Mungyeong stared at him with deeply sunken eyes.

*What kind of person is this?*

The name Mimi Step might have been ridiculous, but the profound principles contained in those movements were not.

*He created a martial art based on the movements of a snake.*

Most martial artists spent their entire lives merely trying to fully understand a single school of martial arts and make it their own.

Yet the young brat standing before him had accomplished that difficult feat as if it were nothing.

After making the technique his own, he had completely recreated it.

*This boy… has the makings of a Grandmaster.*

Jin Taekyung was not the only genius. No—in some ways, this was a type of genius that surpassed Jin Taekyung by far.

*Sword Saint, you raised a monster.*

Mungyeong muttered inwardly, then spoke to Cheongpung, who was still looking dejected.

“So why did you offer me your hand?”

“Hmm. Because Benefactor is so amazing.”

“You think Jin Taekyung is amazing?”

“Yes. Before, I wanted Benefactor to catch up with me quickly, but… now I think he’s slowly getting farther away.”

“I see.”

Mungyeong immediately understood what he meant.

A genius no one had ever been able to rival was burning with competitive pride for the first time.

“Do you intend to learn martial arts from me?”

“No. You don’t have to teach me.”

“What?”

“I’ll watch you from the side and learn. That’s enough. Hehe.”

“……!”

Mungyeong froze for a moment, then let out a quiet laugh.

Was this not a completely outrageous boy? He would watch and learn—someone else’s martial arts, of all things. His martial arts.

But he did not dislike it.

“Oh. You smiled.”

“……I did no such thing.”

“You did. You smiled.”

“How dare you, you young brat.”

“Oh. You’re getting angry.”

“……Brat.”

“Would you like some dumplings?”

Mungyeong hesitated over whether to draw his short sword.

In the end, he accepted the dumpling Cheongpung held out and chewed.

The taste was not bad.

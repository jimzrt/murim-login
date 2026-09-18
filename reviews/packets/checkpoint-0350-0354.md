# Checkpoint Review — 350–354

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

# Chapters 350–354

## Plot

Jin Taekyung spends three days trying to feed the imprisoned Heavenly Power Demon and learn what he knows about Dark Heaven, but the old warrior refuses every comfort and remains silent. Meanwhile, the Beggars’ Sect, the Tang Clan’s Green Shadow Squad, and government troops search for the killer of Poison King Tang Taesang and the Heaven-Shaking Venerable Nun. Near Emei, a disguised military group kills a Beggars’ Sect disciple while hunting for others.

After ten days of treatment, Jeok Cheongang’s recovery succeeds ahead of schedule. The Formless Ultimate Poison is gone, his Yin and Yang are balanced, and his vitality has returned, though he remains unconscious and his qi is unstable. The Divine Physician stays to watch him while Mungyeong leaves to check on Venerable Myoryeong.

At the same time, more than three hundred Dark Heaven attackers enter Chengdu disguised as government troops. Tang Sadok mobilizes the entire Sichuan Tang Clan, distributes poison and hidden weapons, and summons the Tang Clan’s Ten Wonders. The disguised messenger is revealed as the one-armed Western Heaven Demon Lord, who claims demonic martial arts and admits he lost his arm fighting Tang Taesang.

Dark Heaven attacks the Tang Clan under the First Fiend, while the Second and Third Fiends move against Qingcheng and Emei. Their poison-neutralizing artifacts and armor defeat the Tang Clan’s principal defenses, killing more than a hundred clansmen and overrunning half the Outer Hall. Retired Supreme Peak Head Elder Tang Jinhu joins the battle and confronts the First Fiend, while the Western Heaven Demon Lord defeats Tang Sadok and most of the Ten Wonders. With Tang Sadok gravely wounded and only three Wonders still alive, Cheongpung arrives before the Demon Lord.

## Continuity

- Dark Heaven’s assault on the Sichuan Tang Clan is ongoing, led by the First Fiend with three hundred attackers; the Second and Third Fiends are attacking Qingcheng and Emei.
- Dark Heaven’s fighters use poison-neutralizing artifacts and armor resistant to ordinary weapons, negating much of the Tang Clan’s arsenal.
- More than a hundred Tang clansmen are dead, and half the Outer Hall has fallen.
- Tang Sadok is gravely wounded. Only three members of the Tang Clan’s Ten Wonders remain alive.
- Tang Jinhu, the retired Supreme Peak Head Elder, is fighting the First Fiend.
- Cheongpung has arrived at the Western Heaven Demon Lord’s confrontation with Tang Sadok.
- The Western Heaven Demon Lord remains vastly stronger than Tang Sadok and the surviving Tang Clan masters. His body-altering demonic martial art remains unexplained.
- Jeok Cheongang’s treatment succeeded: the Formless Ultimate Poison is gone and his vitality has returned, but he remains unconscious with unstable qi. External shock could still be fatal.
- The Divine Physician remains with Jeok. Mungyeong has left to check on Venerable Myoryeong, whose condition is unresolved.
- Taekyung remains underground with Jeok while Cheongpung aids the Tang Clan.
- Taekyung retains the Myriad-Poison Ring with Tang Sadok’s permission.
- The Uninvited Guest Quest has been accepted. Its grade, mission, and reward are unknown; failure means death.
- The Heavenly Power Demon remains imprisoned and refuses to explain his connection to Dark Heaven.
- The Western Heaven Demon Lord commands Dark Heaven’s forces and previously summoned black-robed hunters through a concealed Mystic Gate Formation.
- The purpose and identity of the Lord of Heaven invoked by Dark Heaven remain unresolved.

## Translation Decisions

- Use **First Fiend**, **Second Fiend**, and **Third Fiend** for 일괴, 이괴, and 삼괴; use **Fiend** for 악귀 when descriptive.
- Use **Uninvited Guest** for 초대받지 않은 손님.
- Use **Myriad-Poison Formation**, **Soul-Severing Thread**, **Heaven-Poison Wanderer**, and **poison-warding pearl**.
- Use **Tang Clan’s Ten Wonders** and **Tang Clan’s Three Skills**, retaining the established footnote about the pun.
- Use **Tang War Drum** for 당전고 and **Tang Clan drum** for 당문고.
- Use **Demon Lord** as the shortened title for the Western Heaven Demon Lord.

## Durable state

{
  "active_continuity": [
    "Dark Heaven's three-hundred-man assault on the Sichuan Tang Clan is in progress, with the attackers holding half of the Outer Hall and more than a hundred Tang clansmen dead.",
    "The First Fiend leads the Tang Clan assault, while the Second and Third Fiends attack Qingcheng and Emei.",
    "Dark Heaven's fighters use poison-neutralizing artifacts and armor that defeat the Tang Clan's principal defensive advantages.",
    "Tang Jinhu, the retired Supreme Peak Head Elder, is fighting First Fiend after entering the battlefield with the Council of Elders.",
    "Tang Sadok is gravely wounded, and only three of the Tang Clan's Ten Wonders remain alive.",
    "The Western Heaven Demon Lord remains overwhelmingly stronger than Tang Sadok and the surviving Tang Clan masters.",
    "Cheongpung has arrived at the Western Heaven Demon Lord's confrontation with Tang Sadok.",
    "Jeok Cheongang remains unconscious with unstable qi after treatment.",
    "Taekyung remains with Jeok while Cheongpung aids the Tang Clan and returns.",
    "The Uninvited Guest Quest remains accepted with unknown parameters and death as its failure condition."
  ],
  "continuity_sources": [
    354
  ],
  "open_questions": [
    "Can the Sichuan Tang Clan survive the assault?",
    "Can Cheongpung change the outcome of Tang Sadok's confrontation with the Western Heaven Demon Lord?",
    "What are the limits and nature of the Western Heaven Demon Lord's demonic martial art?",
    "How large is Dark Heaven's force beyond the three hundred attackers identified here?",
    "Will Jeok Cheongang recover before the siege exposes him to external shock?"
  ],
  "safe_through": 354,
  "temporary_decisions": [
    "Render 일괴, 이괴, and 삼괴 as First Fiend, Second Fiend, and Third Fiend.",
    "Render 악귀 as Fiend when used as the First Fiend's descriptive epithet.",
    "Render 만독진 as Myriad-Poison Formation.",
    "Render 초대받지 않은 손님 as Uninvited Guest.",
    "Render 마군 as Demon Lord when used for the Western Heaven Demon Lord's shortened title."
  ],
  "version": 1
}

## Reading copies

## Chapter artifact 350

# Chapter 350

Step. Step.

As always, I walked along carrying the slop bucket.

Time in the underground prison dragged, but it still moved as steadily as the clock at the Ministry of National Defense. I was already entering my sixth day of life in the prison, and the daily routine was gradually becoming familiar.

Clank. Screeech.

I opened the rusted bars and strode into the prison cell, where filth and dirty water had pooled.

An old man bound to a torture rack greeted me with a sly grin.

“You have come?”

He was a killing fiend who had joined the Demonic Cult during the Great Faction War and killed more than a hundred martial artists of the orthodox faction.

Now reduced to a toothless old man, he continued in an indistinct voice.

“I say this for the last time…”

I cut him off while scooping up the slop with a long ladle.

“Didn’t you say it was the last time yesterday?”

“This time, it really is the last.”

“Sure. And after saying that, tomorrow will be the *real* last time.”

It was something I had experienced countless times over the past six days. Nothing about it surprised me anymore.

The old man flinched at my indifferent attitude, then shouted.

“You! Become my Disciple!”

“You! Get hit.”

Whack!

The old man, struck on the crown of his head with the ladle, writhed in pain. The chains binding his limbs swung back and forth with a loud clatter.

“Graaaagh!”

“Keep it down. You’re noisy.”

“Ugh. You little bastard!”

The old man was about to start screaming at the top of his lungs when his eyes suddenly widened and his nose twitched.

He had caught the smell of oil beneath the stench of the prison.

“W-what is that smell?”

“Nothing you need to know about.”

“Roast duck. It’s roast duck! Do you have any liquor too?”

“What liquor?”

“Liar! That aroma is unmistakably Jiannan Chun!”

“…With a sense of smell like that, you’re on the level of a drug-sniffing dog.”

“Hand it over! Hurry!”

Whack!

“Graaagh!”

“It belongs to someone else. Just eat your slop.”

I set down the bucket and headed toward the final cell.

It was unusually deep and dark compared to the others, and a familiar freak was waiting for me there.

Clank.

“I’ve brought your meal.”

“……”

“You must have had a hard time waiting. By the way, why is it so cold in here? Your sleeping arrangements must be terribly uncomfortable. Should I ask the Tang Clan to lay down an animal-hide blanket for you?”

“……”

So he was going to act like this.

Despite my gentle, cat-paw-soft tone, the Heavenly Power Demon remained stubbornly silent.

After what had happened three days ago, the Heavenly Power Demon had closed his eyes and his mouth.

Of course, that wasn’t enough to make me give up.

“Come now, don’t be like that. Try eating this.”

I took out a sheet of grease-stained paper and unfolded it.

A whole roast duck, coated in various spices and cooked to perfection, revealed its plump, appetizing form. Its delicious aroma was strong enough to drive away even the stench in the cell.

“What is this? It’s roast duck made by a former imperial chef. I tried some myself, and the duck is definitely tender. The flavor is very consistent too.”

“……”

“And roast duck calls for liquor. Jiannan Chun, the famous liquor of Sichuan! Liquor and meat suit a Great Hero like the Heavenly Power Demon, don’t they?”

“……”

A chilly silence descended over the prison, where cold air was already circulating.

I stared at the Heavenly Power Demon, who was sitting cross-legged, with a bright smile. In the end, I let out a deep sigh.

“Fuck. This is impossible.”

For three days, I had tried every possible way to please him. I had changed my manner of speaking to soft, polite language, praised him as a Great Hero of benevolence and righteousness, and kissed up to him shamelessly.

But the Heavenly Power Demon had rejected every offer and convenience I extended. No matter what food or clothing I brought him, he didn’t even touch it.

“I think I’ve done more than enough. Are you really going to keep acting like this?”

“……”

“I’m only treating you this politely because I’m a decent person. What do you think will happen if the Sichuan Tang Clan finds out? Hmm?”

At that moment, the Heavenly Power Demon, who had been sitting cross-legged with his eyes closed, opened his mouth. His voice, which I heard for the first time in three full days, was terribly hoarse.

“Do so.”

“What?”

“This old man has suffered enough torture to be sick of it. Even if I leave this world, I will have no regrets.”

The Heavenly Power Demon had spent more than forty years imprisoned in the underground prison. His detached appearance reminded me of an enlightened monk, and I clicked my tongue.

“Good grief. You really don’t make things easy. Is it really so difficult to tell me only what you know about Dark Heaven?”

“This old man has already said everything he has to say. Kill me or torture me. Do as you please.”

“No, what kind of old man is this?”

But the Heavenly Power Demon’s lips had already sealed shut. And they probably wouldn’t open again.

“…What a stubborn old man.”

I let out a sigh deep enough to make the earth sink, placed the liquor and roast duck within reach of his hands, and turned away.

“Fine, I understand for now, but eat that. You haven’t eaten anything for three days.”

Even as I said it, I knew the truth. Whether I came tomorrow, the day after, or three days from now, the food I had given him would be cold and exactly as I had left it.

“Damn it.”

After finishing the food distribution with the Heavenly Power Demon, I collapsed in a corridor far from the prison cells.

*The Heavenly Power Demon.*

That indescribable look in his eyes and his rigid face kept flickering before me. That was unmistakably the agitation the two words *Dark Heaven* had stirred in him.

The problem was, he refused to say a single word about Dark Heaven.

*But it’s certain that he knew about Dark Heaven long ago.*

I hadn’t heard it directly from the Heavenly Power Demon, but it was already as good as established fact.

The question was how much he knew about Dark Heaven, and how he had come to know it.

I slowly began retracing the conversation I had shared with the Heavenly Power Demon three days ago.

After putting the brain that had earned me seventh-tier school grades through its paces, I arrived at only one plausible conclusion.

*Dark Heaven and the Demonic Cult are deeply connected.*

No. They might even be one and the same.

The Heavenly Power Demon had once been an Elder of the Demonic Cult. Even after spending forty years imprisoned and tortured in the underground prison, he had never lost his loyalty to the Cult. His silence was proof enough.

*If Dark Heaven had been an enemy of the Demonic Cult, he would have opened his mouth long ago.*

Then what the hell was Dark Heaven? A kind of splinter faction that had broken away from the Demonic Cult? Or another organization created within the Demonic Cult itself?

*A branch of Shincheonji called Sick Shincheonji. Something like that.*

Whatever the case, they were definitely plague-like bastards.

I had been lost in thought for quite a while when Cheongpung appeared with a sweet smell trailing behind him and a light step in his walk.

“Hey!”

“…Your grandpa lives at Lotus Peak on Huashan, right?”

Cheongpung swallowed what was in his mouth before answering.

“No! He’s in Henan right now!”

“Oh, right.”

What the hell was I supposed to say to him?

Seeing the mountain of food piled in Cheongpung’s arms left me speechless. I almost felt sorry for the former imperial chef whose face I had never even seen.

“You went out for this?”

“Yes! And I also brought a letter from the Beggars’ Sect while I was at it.”

“…Wouldn’t that normally be the other way around?”

“Hehe.”

“Don’t smile. I’ll get attached.”

I answered gruffly and accepted the letter Cheongpung held out to me.

When I unfolded the grimy piece of paper, which had apparently been stored somewhere filthy, three yellow dog hairs slid out.

*A three-knot Disciple. The branch leader sent this.*

As I had expected, the letter had been sent by the Beggars’ Sect’s Chengdu branch leader and addressed to Gung Gibang.

Of course, Gung Gibang was at the Divine Physician’s hidden clinic, so the branch leader had sent it to me for convenience.

A moment later, after I had finished reading, Cheongpung asked, “What does it say?”

“Nothing special. They’re still searching.”

The Beggars’ Sect, which had initially combed through Sichuan with a fine-toothed comb to find the Divine Physician, had changed its objective.

Their new target was the culprit who had murdered the Poison King and the Heaven-Shaking Venerable Nun.

*Well, it’s not like he’d be caught that easily.*

Tang Sadok had said he would solve the matter using only the Sichuan Tang Clan’s strength, but his attitude had changed after lending me the Myriad-Poison Ring.

However, even with the Tang Clan’s active cooperation, the culprit’s trail had vanished like a ghost.

“Do you think they’ll find him?”

“Who knows? We can only hope for a good result. There’s the Beggars’ Sect, of course, and the Tang Clan’s Green Shadow Squad, experts in reconnaissance and pursuit. Surely they’ll find something.”

“What about the government troops?”

“The government troops seem to be doing their part too.”

The influence of Prince Shangshan, Zhu Bao, was tremendous.

Won Gyun, the City Lord of Sichuan Province, had readily accepted my request to find the culprit instead of the Divine Physician.

The individual fighting ability of the government troops was nothing compared to that of Murim warriors, but the sheer number of them—thousands—couldn’t be ignored.

“Wow! Thousands?”

“I don’t know the exact number either, but apparently they’re swarming all over the place. You saw the government troops too, didn’t you, Young Hero Cheong? On the way back to the Sichuan Tang Clan.”

“Oh, but there weren’t that many people when I saw them.”

“…Of course not. Do you think thousands of people would move around all at once?”

It wasn’t difficult to imagine the government troops gathered in groups of three or five according to their assigned formations, stopping and searching people.

> The government troops are gradually expanding their search area and moving toward Qingcheng and Emei.
>
> They appear to be searching for the culprit while also preparing for some kind of incident.

After reading the final line of the letter, I let out a short laugh.

*They’re doing better than I expected.*

Sichuan City Lord Heo Gyun looked exactly like a corrupt official, but it seemed he wasn’t completely incompetent. Either that, or the military official assigned to this mission was highly capable.

*But what am I supposed to do if they still can’t find him after all this?*

I was seriously worried, since I had made quite a show of talking big to Tang Sadok.

Of course, Jeok Cheongang’s safe recovery came first.

I glanced at the treatment room, whose door remained firmly closed, then casually asked Cheongpung, “What food did you bring?”

“Sho mush!”

“…Finish what’s in your mouth. I’ll take care of the rest.”

* * *

Jang Il was a two-knot Disciple of the Beggars’ Sect.

He had become a Beggars’ Sect disciple out of necessity rather than choice. He had heard that if he formally joined the Beggars’ Sect, completed the initiation ceremony, and became an official Disciple, he would receive one dumpling.

What would an eight-year-old beggar brat who had gone hungry for four days have known?

Clutching his starving stomach, he had gone to the Chengdu branch and become a Beggars’ Sect disciple that very day.

“They only gave me half a dumpling, too. Just thinking about it still makes my teeth grind. Goddamn it.”

The beggars listening to Jang Il yawned quietly. They had already heard the story dozens of times.

More than ten years had passed, but Jang Il’s anger had yet to fade.

“I became a vice branch leader after enduring hardship and dedicating myself to the memory of that half dumpling. So you all should…”

As his story showed signs of dragging on, the three one-knot Disciples exchanged glances at the same time.

“Oh! My stomach suddenly hurts!”

“Gasp, mine too!”

“Ugh, the latrine! Where’s the latrine?”

“You little bastards!”

Jang Il shouted, but the three beggars had already fled.

“Those damn brats… Just wait until they come back.”

That was when a group of people entered Jang Il’s field of vision.

Uniform clothing and weapons. Their lack of military discipline was an added bonus. The sight was familiar enough that Jang Il muttered,

“Government troops.”

These days, government troops were more common than neighborhood stray dogs.

They had never been noticeable when they were slacking off as usual, but now that the big shots had gotten involved, they seemed to be hurriedly making at least a show of doing their jobs.

*They said they were expanding the search net. Have they already come this far?*

As he thought this, a middle-aged military official who appeared to be leading the group approached him with a smile.

“Are you, by any chance, a Beggars’ Sect disciple?”

Jang Il nodded without much interest.

“As you can see.”

“I thought so from your knot.”

“Anyone can tell by looking. You’ve made good time, though. To have already come this far.”

“Ah, they say the Beggars’ Sect has the best intelligence network under heaven. I suppose you already knew about this?”

“Our Sect considers this fairly ordinary.”

The military official smiled along with Jang Il’s arrogant grin and asked, “But this place has no village and very few people. Why are you here alone?”

“Don’t ask. The branch leader kept nagging me, so I brought a few men out for some fresh air. Things have been pretty noisy lately with all this talk of a murderer and whatnot.”

“I see.”

“Well then, take care…”

Jang Il never finished speaking.

The military official nodded with a smile, and at that exact moment, something cold pierced into his chest.

Thunk!

*…Huh?*

Cough.

Jang Il stared blankly at the sword buried in his chest, then coughed up blood.

Why? How?

The questions never made it out of his mouth. His knees buckled as he looked at the military official through hazy eyes.

His face slammed into the new shoots just beginning to rise from the earth. A cold voice reached his ears.

“Find the others. They should be nearby.”

“As you command.”

“What a stupid beggar bastard. Why did he have to be here of all places…?”

That was the last thing Jang Il heard.

He was twenty-five years old.

The young beggar died in a secluded forest two days from Emei Sect.
## Chapter artifact 351

# Chapter 351

Waiting was nerve-racking, and time passed slowly.

If I had been one of the countless twenty-somethings living in twenty-first-century Korea, I might have become half a wreck by now.

I would have had to survive ten days in a dark underground prison without a smartphone or Wi-Fi.

But I had something ordinary twenty-somethings didn’t.

Martial arts.

> **System**
>
> - Successfully completed **Circulate Qi**!
> - **Internal energy** rises slightly!

“Phew.”

I slowly drew a deep breath and gathered the qi inside me.

While I was circulating my qi, Cheongpung—standing guard, my ass; he’d been snoring away beside me—blearily opened his eyes.

“Oh, are you finished?”

“Phewww.”

“Benefactor?”

“Phewww.”

“Benefactor, are you hurt?”

“……”

Why did this guy keep ruining my concentration?

He looked ready to keep asking questions until I answered, so I reluctantly replied.

“Don’t talk to me.”

“Why not?”

“I’ll lose qi.”

There was a reason gym rats constantly chanted about losing muscle.

Finishing circulating my qi didn’t mean I could simply get up the moment the process ended. I also needed time to gather the qi, savor the afterglow, and meditate.

“Oh, I’m sorry.”

“Come on. You know all this, don’t you?”

Cheongpung scratched the back of his head.

“I didn’t know there was anything like that…”

“Huh? Then how have you been doing it until now?”

“I just got up and went out to play when I finished.”

“From the very beginning?”

“Yes.”

“……Did Great Hero Mae Jonghak never teach you?”

“Grandpa said that even if you gathered dust, all you’d have in the end was dust. He said it was more important to do what you wanted with that time. Apparently, things like that eventually become the starting point for enlightenment.”

Was this some kind of YOLO cultivation method?

The more I heard stories like this, the more certain I became that Sword Saint Mae Jonghak was definitely an eccentric.

No, wait.

*That guy has more internal energy than I do.*

I currently possessed just over a hundred years of internal energy.

That put me far above my peers; it was the kind of level someone could reach only if a prestigious great sect on the level of the Nine Sects and One Gang committed itself to supporting them.

And I had only managed that because I had gained the Blazing Flame Divine Pill and various other fortuitous encounters while repeatedly surviving life-or-death situations in the Murim.

So how did Cheongpung have more internal energy than me?

“Elixirs! You ate Huashan’s elixirs!”

Cheongpung’s official sponsors were none other than the Sword Saint and Huashan. If he had received their help, it wasn’t impossible.

But Cheongpung’s answer to my reasonable suspicion was simple.

“No, I didn’t. Grandpa doesn’t like people coming to visit him.”

“Oh, right. Then how did you build up that much internal energy?”

Cheongpung thought about it for a while before opening his mouth.

“It just sort of accumulated on its own.”

“……”

“Oh, and when I was little, I often had my sinews cleansed and marrow washed. Hehe.”

What the hell? Why was he talking about cleansing the sinews and washing the marrow as if he were merely washing his face?

I stared blankly at Cheongpung as he smiled awkwardly.

*This guy really was born a protagonist.*

Natural talent and fortuitous encounters. Everything came naturally to him, as if it were all perfectly normal.

I almost felt that the phrase *I just did it and it worked* had been invented specifically for Cheongpung.

“What a rotten world.”

“Benefactor, what is?”

“Nothing. Just something.”

“Yes.”

As if my chest hadn’t already been feeling stifled lately, it now felt like someone had piled a hundred sweet potatoes on top of it.

I had reached the wall that Murim warriors often talked about, and I had been thinking about asking Cheongpung for advice.

*But there’s no point asking him.*

That was when I let out a small sigh.

Grrrrrind.

“……Huh?”

“……Benefactor?”

A heavy scraping sound bored into my ears. Cheongpung stared past my shoulder with his eyes opened wide, and my heart sank as it began to pound.

*No way. No way.*

*It’s only been ten days.*

I slowly turned my head. At the far end of the corridor, an iron door was slowly opening, filling my entire field of vision.

When two people finally appeared, I asked in a trembling voice,

“How…… did it go?”

There was no answer.

But that was enough.

The Divine Physician and Mungyeong—the exhausted master and Disciple—were looking at me with radiant smiles.

They were bright enough to light up the dark underground prison.



* * *



“The treatment was a success. We encountered several difficult moments along the way, but we managed to get through them safely, and we finished the treatment sooner than expected…”

The Divine Physician’s voice continued, but it sounded as though it were coming from far away. Only one sentence kept echoing in my ears.

*The treatment was a success.*

Yes, the treatment had ended successfully. I had heard the words I had wanted to hear more than anything, and that was enough.

*Old Master.*

Without realizing it, I tightened my grip on Jeok Cheongang’s hand.

He still lay there with his eyes closed, perhaps not yet ready to regain consciousness. But I could feel it clearly.

*His vitality has returned.*

That wasn’t all. Jeok Cheongang’s appearance had changed considerably over the past ten days. The age spots had vanished, his wrinkled skin had tightened, and flesh had returned to his body, which had been growing thinner by the day.

Compared to before, he looked a good ten years younger. No, perhaps twenty.

“Could it be…?”

My voice trailed off as I looked at the Divine Physician.

Noticing the question in my eyes, he smiled faintly.

“Unfortunately, it is not Bone Transformation. However, the medicinal ingredients used during the treatment and the energy of the Thousand-Year Snow Ginseng were a great help to Sir Jeok.”

“Oh, I see.”

Disappointment and joy washed over me at the same time.

It would have been wonderful if he had used this treatment as an opportunity to advance to an even higher realm, but perhaps I had expected too much for a moment.

“You seem disappointed.”

“Oh, no.”

I was startled and quickly waved my hands. These two men had successfully completed the difficult treatment without a single complaint. It would have been rude to show such an expression.

“I was only…”

“Heh heh. I did not mean to blame you. How could I not understand Young Master Jin’s feelings for his Master? Is that not right?”

“Of course. Your words are absolutely right, Master.”

Mungyeong answered politely, then continued speaking to me.

“Sir Jeok will regain consciousness within three days at the latest. The treatment has only just ended, so he needs time for his qi to settle properly. You need not worry too much.”

“Three days at the latest.”

“Yes. Of course, even after he awakens, he must avoid exhausting himself for a while. Sir Jeok is famous throughout the Murim, so he should recover quickly.”

“He should. He has an abundance of energy, after all. Then, does that mean everything really is…”

“Yes.”

Mungyeong smiled and nodded.

“The Yin and Yang have regained their balance, and no Formless Ultimate Poison remains. The treatment is over.”

“……Phew.”

I finally let out the breath I had been holding. A feeling of exhaustion washed over me, as if all the energy had drained from my body, followed by the sensation of floating weightlessly.

How long had I waited to hear that answer?

When my legs gave out and I slumped to the floor, the Divine Physician spoke with a mischievous expression.

“It seems this old quack was not very trustworthy to you, Young Master Jin.”

“N-no, it wasn’t that I didn’t trust you, Old Man Dong. It was just, you know, one of those things. Young Hero Cheongpung knows what I mean, right?”

“I don’t know!”

“……Never mind. My mistake for asking you.”

The Divine Physician’s laughter grew louder.

He looked at us with a fond expression, as though he were watching his grandchildren put on a show, then patted me on the shoulder.

“Everything is fine now. This old man will remain here just in case. So if you have any remaining worries, put them away for good.”

“What?”

When he saw my face, the Divine Physician hurriedly waved his hands.

“There is no need to make that expression. I am only staying to watch the patient awaken after treatment.”

“Phew, you scared me. You should have said that from the beginning.”

I had thought there was something else left to worry about.

Mungyeong, who had been grinning at his momentarily flustered Master, spoke up.

“Sorry to interrupt, but I think I should leave now.”

His sudden announcement startled me.

“What? Already?”

“Yes. Venerable Myoryeong should have regained consciousness by now, so I would like to go check on her.”

“You must be tired. Stay and rest for a while.”

“No, it is fine. I did not do very much, anyway. If I still have energy to spare, then I, as the younger one—even if only by a year—should be the one to go. Isn’t that right, Master?”

“You little rascal!”

“Hahaha.”

I was worried about him, but it seemed their decision had already been made.

No sooner had he finished speaking than Mungyeong slung his travel pack over his shoulder. Watching him, I suddenly remembered something I had forgotten.

“Mungyeong.”

“Yes?”

“Thank you. Truly.”

Mungyeong gazed at me for a moment, and a smile formed at the corners of his mouth.

“That is the finest thing a medical apprentice can hear.”



* * *



“Family Head, the Sleeping Dragon of Shanxi requests an audience.”

Ssssss.

At the voice from outside the door, the body of a snow-white snake slipped back into Tang Sadok’s robes.

Tang Sadok frowned when one of the few peaceful moments in his day was interrupted.

“Jin Taekyung, you mean?”

“Yes.”

“For what reason?”

“He says the treatment is over. And…”

The guard’s voice continued, filled with confusion.

“He said he would like to use the item he borrowed for a few more days.”

“The item he borrowed.”

“Yes. Those were his exact words. He also asked to remain in the underground prison for a few more days.”

It was an indirect way of referring to the Myriad-Poison Ring. Tang Sadok let out a short laugh and muttered,

“What a brazen brat…”

“Pardon?”

“I was not speaking to you. Pay it no mind. Tell Jin Taekyung I give him permission, and continue watching him.”

“Yes, Family Head.”

As he sensed the guard’s footsteps fading away, Tang Sadok tapped the table.

He was neither a Great Hero of Benevolence and Righteousness who helped others without seeking anything in return nor a knight who could not tolerate injustice.

He had lent Jin Taekyung the clan’s sacred heirloom through a bargain, but it was only natural for him to continue keeping a close watch on Taekyung.

*I am the Family Head of the great Sichuan Tang Clan. I trust no one.*

One shichen earlier, even the young medical apprentice attempting to leave the clan had been thoroughly searched and questioned.

The only reason they had let him go was that his identity was guaranteed. If he had been a Disciple of some ordinary lesser sect, he would not have been allowed to take even a single step outside.

*In any case, the Fire King’s successful treatment is good news. The Divine Physician really is something.*

Tang Sadok already knew from his late father that Fire King Jeok Cheongang was an exceedingly eccentric old man.

He also knew that Jeok Cheongang’s pride was so strong that he would repay any gratitude or grudge he incurred, no matter what it took.

*You bastard…… your life is almost over.*

A green glint flashed through Tang Sadok’s eyes.

The murderer who had killed his father and the Heaven-Shaking Venerable Nun was definitely said to be one-armed. That was not especially rare in the Murim, but it was not a feature one saw every day, either.

A physical disability stood out anywhere.

*Run. Try running wherever you can. The Sichuan Murim will chase you until the day your breath stops.*

Grind.

Tang Sadok was quietly grinding his teeth when—

“Uncle!”

With an urgent shout, the doors to the pavilion flew open. Tang Sadok’s face twisted at the same time.

It was not the sudden intrusion of the Master of the Gatekeeper Pavilion that caused his expression to change, but the martial artist standing beside him.

The green martial uniform was torn and stained with blood from top to bottom. The two characters meaning **Tang Family** had been embroidered into it with thread.

“You…”

There was no doubt.

It was a member of the Green Shadow Squad.

A member of the Green Shadow Squad who should never have appeared here in such a condition.

Facing Tang Sadok’s rigid expression, the Green Shadow Squad martial artist cried out in a voice choked with blood.

“They’re coming! They’re coming!”
## Chapter artifact 352

# Chapter 352

*They’re coming.*

The Green Shadow Squad martial artist had blurted out a disjointed sentence.

But insight struck Tang Sadok like a flash of lightning. It gave form to the small unease he had harbored in his heart, and it was the conclusion drawn from all the experience he had accumulated over the years.

*The murderer isn’t alone!*

The one-armed man who had killed his father and the Heaven-Shaking Venerable Nun was coming to the Sichuan Tang Clan with his subordinates.

Where the true mastermind was, how many men they had, and how they had been able to move through Sichuan as freely as if it were their own front yard—all of that was irrelevant.

The next moment, a voice like a thunderbolt burst from Tang Sadok’s lips.

“One Origin, Three Divisions, and Five Squads—prepare to meet the enemy!”

Rumble!

The pavilion trembled beneath the enormous shout, laden with powerful internal energy.

The disturbance had occurred in none other than the Family Head’s Hall. The first to react were Tang Sadok’s guards surrounding the pavilion.

“Family Head!”

Bang!

By the time the guards burst inside, smashing through the pavilion doors, the clan members who had heard Tang Sadok’s shout were already spreading his orders throughout the family compound.

Before fifteen minutes had passed, hundreds of Tang Family members, bound together by venomous resolve and resentment, would gather.

And then…

*I’ll show you. I’ll show you what the Tang Family’s revenge looks like.*

Despite the fury boiling in his chest, Tang Sadok’s eyes had grown as cold as the northern wind and bitter snow.

“Family Head, what in the world is—”

“The men who deserve to die are coming. That is all.”

He waved away the bewildered guards, then fixed his gaze on the Green Shadow Squad martial artist.

The martial uniform, torn to shreds and soaked in blood, bore unmistakable traces of battle.

“What happened? Report everything you saw and heard without leaving anything out.”

Only then did the Green Shadow Squad martial artist catch his breath and speak in an exhausted voice.

“It began when we discovered a suspicious group while searching the area around the Golden Hall.”

“A suspicious group?”

“Yes.”

“The Golden Hall is only half a day from the clan at most. The Beggars’ Sect and the government troops already completed all their inspections. How could—”

Tang Sadok suddenly stopped speaking. His gaze sank.

“…The government troops. It was the government troops.”

The Green Shadow Squad martial artist stared at the Family Head with wide eyes, then nodded.

“Y-yes! They were definitely dressed in the uniforms of government troops.”

“A disguise.”

Tap. Tap.

Tang Sadok drummed his bony fingers against the table.

They had been thoroughly caught off guard.

The Beggars’ Sect and the government troops had confirmed Chengdu’s safety several times already, and it had been only two days since they expanded their search area.

The enemy had entered Chengdu through the gap left when the net loosened.

*It couldn’t have been very difficult.*

The elite were always deployed to the front lines. Among the Beggars’ Sect and the government troops, those with experience and sharp eyes had already left Chengdu.

Besides, wasn’t this after several thousand government troops had spent nearly ten days roaming around Chengdu? Anyone wearing their uniforms could have blended in naturally.

“How many were there?”

“Perhaps to avoid suspicion, they were moving in several groups. But from what we were able to determine, there seemed to be at least three hundred of them.”

“Three hundred?”

“Yes. Without a doubt.”

The Master of the Gatekeeper Pavilion had been listening to the report with an anxious expression. Now he spoke in a triumphant tone.

“Three hundred? That’s all? They must be desperate to die. Isn’t that right, Uncle?”

“…”

“More than three hundred martial artists from our family alone can be deployed immediately. And that isn’t all. Isn’t this exactly why we built an impregnable fortress? They won’t even be able to climb the walls before dying to our poison and hidden weapons.”

Tang Sadok’s closed lips parted.

“Shut up.”

“Pardon?”

“I said shut up.”

“U-Uncle, why are you acting like this? It’s only three hundred. With that many, we could wipe them out in the blink of an eye…”

“Only three hundred?”

The fingers that had been drumming against the table stopped abruptly.

Tang Sadok looked at his only nephew with utter contempt.

“You haven’t forgotten the Gyeongwol Year Bloodbath, have you?”

“…How could I forget?”

The Gyeongwol Year Bloodbath was practically a taboo subject within the Tang Clan.

Fifty years ago, it had been the humiliating day when the Sichuan Tang Clan was forced to abandon the home it had occupied for centuries and flee.

That day, Tang Sadok had lost his only older brother, while the Master of the Gatekeeper Pavilion had lost his father before he was even born.

“But things are different now!”

Tang Sadok answered the Master of the Gatekeeper Pavilion’s impassioned shout in a cold voice.

“Yes. Exactly what is so different?”

“The Demonic Cult’s army numbered two thousand, while our family had only three hundred martial artists!”

“So far, you’re more or less correct. Go on.”

“Although we were defeated and forced to retreat, the Demonic Cult suffered enormous losses of more than a third of its forces, while our family suffered only a little over a hundred casualties.”

“That is also true. The damage it suffered delayed the Demonic Cult’s conquest of Sichuan. Our family lost its home, but gained even greater fame in exchange.”

“Then why?”

Bang!

The Master of the Gatekeeper Pavilion slammed his fist down, denting the iron table. He stared at his uncle with blazing eyes and continued.

“Why are you afraid of a mere three hundred enemies? Fifty years ago, even the Demonic Cult’s vicious criminals—several times more numerous than this—had to spill countless rivers of blood just to overcome our family!”

His ringing shout shook the air inside the pavilion.

Tang Sadok’s answer to his furious nephew was short and simple.

“So? Is that all?”

“…What?”

“You pathetic fool.”

As the Master of the Gatekeeper Pavilion’s eyes wavered, Tang Sadok let out a sigh.

“The Gyeongwol Year Bloodbath is a humiliating part of our history that must never be forgotten. But it is also a memory of how our family proved its strength to the world.”

“Y-yes. That is why martial artists throughout the world still praise our family’s martial might and righteous spirit.”

“Ha… hahahaha!”

Ignorance had become a disease at this point. Looking at his nephew, who still failed to understand, Tang Sadok gave a hollow laugh.

“Yes. The entire world knows that fact. Do you think they don’t?”

“……!”

“After the Great Faction War, our family built an impregnable fortress that no one could overcome. We increased the number of our clan members and armed them thoroughly. Is there anyone under heaven who doesn’t know this? I’m asking whether there is anyone who doesn’t know the strength and determination our family displayed during the Gyeongwol Year Bloodbath!”

Under the storm and thunder crashing down on him, the Master of the Gatekeeper Pavilion’s face had turned pale.

Only now did he understand that the three hundred enemies invading the Sichuan Tang Clan were not men anyone could dismiss as *only* three hundred.

By contrast, the old and experienced Family Head’s judgment was swift and decisive.

“Sound the Tang War Drum.”

A stir passed through the guards, who had been frozen like stone at the Family Head’s command.

“Y-you mean the Tang War Drum?”

“Give poison and hidden weapons to everyone, regardless of age or sex. Retired elders, craftsmen who have never learned martial arts, and women are no exception. Our family will commit every last ounce of its strength to this battle.”

“A-as you command!”

The guards’ complexions changed at the blade-sharp command, and they hurried into motion.

A short while later, when the Tang War Drum’s thunder rolled throughout the Sichuan Tang Clan, everyone would know.

Their family stood on the brink of destruction.

And the person who felt the greatest sense of danger among them all was Tang Sadok.

*This is dangerous.*

The experience and instincts he had accumulated while leading the family whispered to him.

Perhaps a mountain of corpses and sea of blood greater than the one on that day in Gyeongwol awaited the Sichuan Tang Clan.

Then, the sound announcing the beginning of everything rang out.

Boom. Boom. Boom!

The majestic sound made anyone who heard it feel their heart pound violently. The Master of the Gatekeeper Pavilion muttered,

“So this is the Tang Clan drum…”

The Tang Clan drum had last sounded before he was born. It was the first time he had ever heard it, and he could not hide his agitation when—

“They’ve taken the first move.”

“U-Uncle?”

The Master of the Gatekeeper Pavilion hurriedly turned his head and saw Tang Sadok’s eyes, sunk into bottomless depths.

At the same time, several gray-flecked figures entered the pavilion with swift movement techniques.

“Family Head!”

“It’s the enemy! They’re coming while beating a war drum!”

“They’re attacking us, yet they’re beating a war drum. What incredible bastards. Truly incredible.”

Tang Sadok let out a hearty laugh.

The ten people staring at him were filled with disbelief.

“This is no time to laugh!”

“Family Head, please give us your orders!”

They varied in appearance. Among them were a young man who looked to be in his thirties, a graying middle-aged man, and an old man around Tang Sadok’s age.

But regardless of age, each of them had proven their martial strength among the hundreds of members of the clan.

That was why Tang Sadok had given them another name.

“The Tang Clan’s Ten Wonders. You arrived right on time. I was just waiting for you.”

“Family Head, what in the world is going on? We should be attacking them immediately—”

“Well, you can ask that friend over there for the details.”

The gazes of the Tang Clan’s Ten Wonders followed Tang Sadok’s.

The Green Shadow Squad martial artist swallowed nervously under the scrutiny of so many powerful figures.

“I-I’ll tell you anything I know!”

“That is welcome news. Then let this old man ask you…”

Tang Sadok continued in a gentle voice.

“Weren’t you one-armed?”

“……!”

“……!”

At that moment, it was as if time had stopped.

The majestic sound of the Tang War Drum, which had finally begun to thunder. The frantic movements and shouts of the clan members.

Unlike the time outside, which continued to flow unchanged, everything inside the pavilion had come to a complete halt.

Amid the silence and shock, only one person moved backward through time.

Crack. Crrrck.

Bones lengthened and shortened. Muscles swelled.

As the blood-soaked uniform tore apart, the two characters meaning **Tang Family**, embroidered across his chest, split in half.

The Green Shadow Squad martial artist slowly rose to his feet.

He was no longer a young man in his twenties. And he was no longer a member of the Green Shadow Squad.

“You have sharp eyes. The Poison King raised his son well.”

The middle-aged man smiled faintly and rubbed his left arm. The color of his skin differed subtly around the elbow, as if the arm had been removed and attached again.

“And to answer your question… I honestly don’t know either. Let’s just conveniently call it demonic martial arts.”

A green light flickered in Tang Sadok’s eyes as he stared at the middle-aged man.

“So it was you. You were the one who harmed my father.”

“Poison King Tang Taesang. He lived up to his reputation. I was honestly impressed. I lost one arm then, too.”

The middle-aged man clenched and opened his left fist, deliberately furrowing his brow.

“The sensation isn’t quite what it used to be. I wonder if I’ll ever be able to return to the way I was…”

“Do not worry. This old man will personally cut off your head and make sure you never have to think about it again.”

“We’ll lend a hand as well.”

Rumble!

The enormous qi pressure flowing from Tang Sadok and the Tang Clan’s Ten Wonders shook the pavilion.

Yet even in the face of deadly poison capable of killing a person with a single breath, the middle-aged man— the Western Heaven Demon Lord—smiled calmly.

“If you can, by all means.”

Roar!
## Chapter artifact 353

# Chapter 353

Boom. Boom. Boom!

Listening to the thunderous drumbeats, an old man muttered,

“It’s been a while since I heard that.”

He was short and stocky, with coarse, unruly features. To ordinary eyes, he was nothing more than an ugly, ill-tempered old man.

But anyone who had faced him even once called him by another name.

*Fiend.*

The old man curled the corners of his mouth upward. Seeing the wet-behind-the-ears pups waiting for him atop the walls surrounding the Sichuan Tang Clan like an impregnable fortress, roughly three hundred yards ahead, put him in an excellent mood.

“It feels as if the stench of blood is already filling the air. I felt this way when we first came down from the Qilian Mountains.”

His had been a difficult birth, and he had been born with ugly features.

How could the other two brothers, born on the same day from the same womb, have been any different? When even their father disappeared, the three brothers, with nowhere left to turn, hid in the Qilian Mountains to escape the people’s contempt.

“We were so young back then. Bastard or bitch, we killed them all, then killed some more…”

The age they had been born into was a time of chaos, and so they became fiends.

When they finally looked around, the people who had despised them for their ugliness and pelted the three brothers with stones all lay submerged in pools of blood.

Then, when they joined the Demonic Cult as it invaded the Central Plains and stained the world red, people came to fear them as the Qilian Three Fiends.

“It’s fun remembering our prime. Don’t you think?”

The old man turned his head with a smile, only to click his tongue when he realized his mistake.

“Good grief. Maybe it’s because I’m getting old, but I keep forgetting things.”

The two younger brothers who had followed him like shadows throughout their entire lives were not here.

The Second Fiend had left to take charge of Qingcheng, while the Third Fiend had gone to take charge of Emei.

Before long, the two famous mountains counted among the greatest in the world would be covered in a sea of corpses and blood.

And then…

Kwahhhhhng!

At last, the signal announcing the beginning of everything rang out.

The First Fiend let out a hearty laugh at the thunderous boom coming from beyond the walls of the Sichuan Tang Clan. The time promised by the Western Heaven Demon Lord had arrived.

“Our lord is calling us. Isn’t he?”

Shing-shing-shing!

Hundreds of weapons were drawn, slicing through the dawn air.

Behind the First Fiend stood three hundred men in black, stretched out in a long line. They had already discarded their government-troop uniforms and were now armed in black leather armor.

“The time has come. Raise the flag!”

The instant the First Fiend’s shout rang out, the Tang Clan martial artists on the walls saw it.

Flap.

Beyond the pale dawn mist, a flag rose high into the air.

Two characters fluttered in the fierce wind.

“Dark Heaven…?”

Someone on the wall muttered the words, but the booming drums swallowed them.

Boom. Boom. Boom!

Matching the increasingly forceful drumbeats, the black-clad men began to advance.

The breath escaping between their lips was hot, but their eyes were cold. Sharp killing intent rolled off their entire bodies.

And at the head of them all stood a single fiend.

“By the command of the Lord of Heaven…”

His blood-red eyes shone with joy.

What a magnificent day this was. The orthodox Murim would remember this day. Everyone would gaze upon the flag of Dark Heaven hanging over the world and tremble with fear.

The First Fiend shouted, quivering with elation.

“Destroy the Sichuan Tang Clan!”

“We obey!”

Boom. Boom-boom. Boom-boom-boom-boom-boom!

The drums grew sharper, accompanied by fierce shouts. Three hundred black-clad men charged toward the walls, while dark clouds rolled across the sky and covered the sunlight that had only just begun to shine.

That was when a powerful shout burst from atop the walls.

“They’re vile criminals who dare invade our family! Don’t leave a single one alive!”

“Everyone, fire!”

Shhhhhhhk! Thud!

An arrowhead shot with tremendous force pierced someone’s body and buried itself in the ground. A mist of blood formed, followed by a scream.

“Gaaaaah!”

But the casualties were extremely few. Most of the black-clad men blocked the arrows with their weapons, while others survived thanks to the armor they wore.

“Wh-what?”

“Even the crossbows can’t pierce them? What in the—”

The crossbows, whose bolts could penetrate even fairly thick iron plates, were useless against the armor.

As the Tang Clan martial artists faltered, a small figure streaked forward faster than anyone else.

Fwoooosh!

“Ha-ha-ha-ha! Excellent! Excellent!”

No one atop the walls knew who the First Fiend was. But everyone who heard his crazed laughter felt the hair on their bodies rise with fear.

“The Myriad-Poison Formation! Activate the Myriad-Poison Formation!”

The order came in a panic. But the First Fiend’s figure had already vanished like a ghost and reached the gate.

With a grin that twisted his face into something fiendish, he threw a single punch. Two jiazi of internal energy surged into it like a whirlwind.

“Let’s see how Tang Family blood tastes.”

Whoom—Kwahhhhhng!

The battle had begun.

* * *

“Hm?”

“What?”

Cheongpung and I looked at each other at the same time. Then we realized that we had both come to the same conclusion.

“Did you hear that?”

“Benefactor, did you hear it?”

The Divine Physician, who was checking Jeok Cheongang’s pulse while he remained unconscious, looked at us with a bewildered expression.

“What are you talking about?”

“Just a moment.”

I raised a hand to stop the Divine Physician from continuing and quietly focused my mind.

My body might have been in the underground prison, but my senses were another matter. Amplified several times over by the power of my internal energy, my hearing escaped the labyrinthine prison corridors and rose upward, higher and higher.

And then…

Boom.

This time, I heard it clearly.

Cheongpung set down the food he had been holding and spoke.

“Benefactor, could this be…”

“That’s right.”

I looked up at the ceiling of the prison and continued,

“It’s a drum.”

Boom. Boom. Boom.

At that exact moment, the drums rang out again, as if agreeing with me.

Ting.

> **System**
>
> - An unexpected Quest has been generated.
>
> - You cannot refuse. The Quest has been automatically accepted!
>
> - Would you like to view the Quest information?

“…”

Without saying a word, I stared at the holographic window filling my vision.

The sudden drumbeats and an unexpected Quest. Neither could possibly be a good sign.

*Damn, look at the goose bumps already rising on my arms.*

“This is driving me crazy.”

But there was no turning back now. The only thing I could do was find out what kind of path lay ahead of me.

*View Quest information.*

Ting.

A new holographic window appeared with the System’s characteristically cheerful notification sound.

Of course, unlike the notification, the content written in the Quest window was anything but cheerful.

> **System**
>
> **Quest**
>
> **Uninvited Guest**
>
> Dark Heaven’s dark clouds have finally spread across Sichuan.
>
> The battle has already begun, and the Sichuan Tang Clan is surrounded.
>
> May fortune favor you in battle.
>
> **Grade:** ???
>
> **Limit:** ???
>
> **Mission:** ???
>
> **Reward:** ???
>
> **Failure:** Death

I read it exactly three times from beginning to end. Then I thought,

*What kind of fucked-up situation is this?*

I was so dumbfounded that I could barely speak.

The contents were absurd from start to finish. Enemies had invaded. We were surrounded and couldn’t escape. It wished us luck and ended there.

*Goddamn, it’s disgustingly simple.*

Grade, limit, mission, reward. Every single one was a question mark.

Well, at least one thing had been made perfectly clear.

If I failed this Quest, I would die.

What a revelation. If we couldn’t stop the enemies who had invaded, I would die. It was such wonderfully useful information that I almost slapped my balls in gratitude.

*Is this a Quest information window or a Quest notification window?*

Boom. Boom. Boom.

My vision swam. Listening to the drumbeats grow clearer and more violent, I soon felt cold sweat gather on my back.

But in contrast, my mind had gone cold as ice.

I dismissed the Quest window, took a deep breath, and spoke.

“Old Man Dong, we have a problem.”

The Divine Physician had learned martial arts, but his realm was far below ours.

Unlike Cheongpung and me, he had not heard the drumbeats. He asked with a puzzled expression,

“A problem? What do you mean?”

“The enemies have invaded.”

“The enemies? Here, at the Sichuan Tang Clan?”

“Yes. There’s no doubt. We’re already surrounded.”

The Divine Physician looked as if he found it difficult to believe. It was a perfectly normal reaction. What kind of lunatics would attack the Sichuan Tang Clan?

But if those lunatics were Dark Heaven, the situation changed completely. They were none other than the perpetrators who had stained Shaolin Temple with blood.

Still, every second mattered. There was no time to give him a detailed explanation.

“We don’t know what’s going to happen, so steel yourself.”

“…I understand.”

The Divine Physician nodded with a grim expression.

Perhaps because he had traveled throughout the world and experienced countless things, he seemed to accept reality more quickly than expected.

I looked at Jeok Cheongang, who was still lying there with his eyes closed.

“How is my Master’s condition?”

“As I said before, his qi has not stabilized yet. If he receives an external shock in this condition…”

The Divine Physician did not finish the sentence, but I had heard enough.

Jeok Cheongang’s condition was still unstable. According to the Quest window, the Sichuan Tang Clan had already been surrounded by Dark Heaven.

*What if we broke through their encirclement and escaped?*

The thought briefly crossed my mind, but I soon shook my head.

Jeok Cheongang’s safety was one concern, but our chances of success were slim as well. Considering the forces Dark Heaven had deployed against Shaolin Temple, escaping might only lead us straight into a deathtrap.

*Especially if that monster called the Blood Lord is there. We have to avoid him at all costs.*

After thinking it over, I arrived at a single answer.

I slowly opened my mouth.

“Young Hero Cheong.”

Cheongpung answered in a subdued voice.

“Yes, Benefactor.”

“Can I ask you for one favor?”

“Anything.”

Cheongpung was endlessly innocent and carefree, but every once in a while, he showed a serious side.

And whenever he did, I found him more dependable than anyone else.

That was why I could ask him for a favor like this.

“Protect Old Master—protect my Master—here. That’s my request.”

“……!”

“As you heard, we can’t get out right now. Someone has to leave and help the Sichuan Tang Clan.”

“Benefactor.”

“So…”

“Benefactor.”

I swallowed the words that were about to follow. Cheongpung was looking at me with clear eyes.

“I’ll stay if you tell me to stay, and I’ll go if you tell me to go. But, Benefactor…”

His quiet voice reached my ears.

“You have someone you need to protect, don’t you?”

“……!”

“I once became too frightened to fight when I had to protect someone. I couldn’t protect the people I cared about. That’s why I’m a fool.”

I had not known. I had never realized Cheongpung thought about things like this.

Even afterward, he had continued living brightly and talking constantly, as if he were the happiest person in the world.

That was how he had always been. It suited him. It was only natural for him.

*But it wasn’t.*

As if recalling what had happened in Henan, Cheongpung turned his gaze toward some distant, dark corner of the underground prison.

A smile formed at the corners of his mouth. It was the same as always, yet different from his usual smile.

Only then did I realize.

The time had come to make a real decision.

*One person stays. One person leaves.*

I slowly shifted my gaze.

Cheongpung, still smiling.

The Divine Physician, wearing a worried expression.

Someone’s screams and shouts, drawing closer by the moment.

And then…

Jeok Cheongang’s face, covered by the shadows of flickering torchlight.

The next moment, my lips began to move before I even realized it.

“Young Hero Cheong. I have one request.”

Cheongpung’s gaze met mine.

I pointed toward the ceiling and flashed him a grin.

“Go give those sons of bitches a good hit and come back.”

“Yes, Benefactor!”

His answer was brighter than ever.
## Chapter artifact 354

# Chapter 354

Clang! Krrr-kang!

“They’re such vile bastards that even chewing them to pieces wouldn’t satisfy me! Don’t hold back!”

“The Lord of Heaven desires it! Destroy the Tang Clan!”

Sword clashed against sword. Harsh breathing mixed with ragged cries. The killing intent and scent of blood given off by several hundred people tangled together flooded the battlefield.

Amid the dawn mist blackened by poison smoke, those who had come to kill raised their weapons and charged at one another.

Pfft!

“Gaaah!”

A scream burst from the mouth of a young man.

Born into a collateral branch of the great Sichuan Tang Clan, he had reached the First Rate realm without much difficulty. His considerable martial talent and composure beyond his years had made him the focus of everyone’s expectations.

But now, the young man’s bright future lost its light alongside the black Sword Energy.

Fwoooosh! Slash!

The Sword Energy carved down diagonally through his upper body, and that was the end.

The black-clad man stared pale-faced at the young man as he collapsed, spilling blood and entrails.

*The kid’s vicious.*

The fight had been decided in only three exchanges.

Yet the unknown Tang Clan martial artist had sacrificed his own life in an attempt to leave them both grievously wounded.

The ox-hair needle that had somehow burrowed beneath the black-clad man’s clavicle was proof of that.

*So this is what it means to be from the Sichuan Tang Clan.*

Clicking his tongue, the black-clad man pulled out the needle.

Its tip was so thin that it could only be seen on close inspection, and it had already turned black. There was no question that it had been coated in poison.

“Ghk!”

His vision blurred for an instant. The poisonous energy that had begun around his clavicle was rapidly spreading throughout his body.

At this rate, even with Peak internal energy, the most he could do was buy himself some time.

And in a chaotic battlefield like this, after being struck by one of the Sichuan Tang Clan’s deadliest poisons, he was as good as dead.

But the black-clad man did not panic.

No—instead, he smiled.

“The Lord of Heaven is… great.”

The words came out muffled between his clenched teeth.

When the black-clad man opened his mouth for the first time, a small bead could be seen inside.

At the same time, an eerie light flowed from the bead, running down the black-clad man’s throat like a river.

Ssssss.

The change was instantaneous. His blurred vision cleared, and the body that had been losing its strength regained its power and vitality.

After every trace of poison had been removed from his body, the black-clad man shuddered.

The Lord of Heaven, the most dignified and greatest of all.

The life force granted by his god filled his entire body.

“The Lord of Heaven has descended upon me!”

The black-clad man cried out in ecstasy and turned his head to search for another victim.

That was when—

“Wrong. The one descending upon you bastards is Yama.”

Crack!

A dagger flying from somewhere buried itself in the black-clad man’s forehead.

The internal energy imbued in the dagger bored through flesh and bone, turning the black-clad man’s brain into mush. He died instantly.

Thud. Crash!

The bead that rolled from the dead man’s mouth was drawn into someone’s hand.

An old man gazed at the bead with wizened gray eyes and muttered,

“These bastards… They’re carrying artifacts.”

An ordinary martial artist would have assumed that the bead was a poison-warding pearl.

But the old man, Tang Jinhu, was a direct descendant of the Sichuan Tang Clan and a veteran of the Great Faction War. He instinctively realized that this bead was something different from a poison-warding pearl.

*What is this?*

Poison-warding pearls normally had a clear color. The greater their transparency, the more effective they were at neutralizing poison, and their value rose accordingly.

But the bead the black-clad man had possessed was an ominous black, as if it held storm clouds inside.

Even so, its power had been great enough to neutralize one of the Tang Clan’s deadliest poisons.

The greater problem was—

*Every single one of them has an artifact of this level. At this rate, neither our family’s poison techniques nor the poison formations we set up in advance will be of any use.*

On top of that, they wore leather armor that even ordinary swords and blades could not pierce.

Tang Jinhu finally understood why the Tang Clan drum had sounded.

At this rate, a bloodbath even more horrific than the one in the Gyeongwol Year would unfold.

“These bastards…”

Crunch.

Tang Jinhu crushed the bead in his hand and extended both arms, his face filled with killing intent.

The silver threads wrapped around his wrists absorbed his internal energy and sprang rigidly upward.

The next instant, a dazzling white flash filled the battlefield.

Screeeech—thud-thud-thud!

“Ghk!”

“Gaaah!”

Only a handful of those struck managed to leave behind even a death cry. Death came equally for First Rate and Peak masters alike.

Raising their weapons to block was useless. The threads Tang Jinhu shot out lived up to the name Soul-Severing Thread, cutting through everything in their path.

Blades, bone and flesh, and even the lives of his enemies.

Tang Jinhu felled over ten black-clad men with a single move and let out an azure dragon’s roar.

“Don’t retreat! Aim for their vital points with hidden weapons and attack together!”

“Head Elder! This old man has come as well!”

“Would you look at these fucking bastards! How dare they invade our family? Can’t you see the Heaven-Poison Wanderer standing before you?”

Tang Jinhu was a Supreme Peak master who had retired more than a decade ago and the head of the Council of Elders.

The sight of veteran masters joining the battlefield one after another at precisely that moment brought color back to the faces of the Tang Clan martial artists who had begun to falter.

“G-Grandfather!”

“The Head Elder is here! The Council of Elders has mobilized!”

But their joy lasted only an instant.

Krrr-kang! Slash!

“Gaaah!”

“Tang Hwi!”

“Hey, brat! Do you have time to look away?”

Pfft-pfft-pfft!

“Help me… Ghk!”

“Lord of Heaven!”

“The great Lord of Heaven is with us. Kill them all!”

The black-clad men were more skilled than the Sichuan Tang Clan martial artists, and the armor and bizarre poison-warding pearls they carried rendered the Tang Clan’s famed poisons and hidden weapons useless.

A dozen Elders, including Tang Jinhu, and dozens of Peak masters whom the Tang Clan had painstakingly trained were fighting desperately.

But their limits were clear.

Screeeech—thud!

Tang Jinhu severed the throats of two black-clad men charging at him with the Soul-Severing Thread and ground his teeth.

“Where did these bastards come from…?”

The sight unfolding before his eyes was utterly tragic.

The black-clad men shouted the Lord of Heaven’s name as if possessed and swung their weapons.

Whenever they blocked swords and hidden weapons with their armor and continued advancing through the poison smoke, blood sprayed and corpses piled up.

In the vacant eyes of a Tang Clan martial artist whose breath had stopped, red flames that had sprung up somewhere flickered. The hot fire and acrid smoke drove away the poison mist and consumed the fallen corpses.

Tang Jinhu roared in a voice that seemed to spit blood.

“No! You bastards! How dare you—how dare you lay hands on my own flesh and blood!”

Even the mighty forces of the Demonic Cult had suffered more than a thousand casualties to overcome the Tang Clan.

How could a mere three hundred enemies create such a horrific scene?

“Ghk! H-Head Elder…”

“Hyung!”

Pfft-pfft-pfft!

Even the Elders who had once roamed the martial world could not escape death.

Although they had not reached the supreme realm of Supreme Peak like Tang Jinhu, every one of them was a veteran master who had reached the very edge of Peak.

But whenever one was cut down, five more charged forward. When those five were cut down, ten more came rushing in.

Among those ten black-clad men who charged forward without regard for their lives, a Peak master was hiding.

Slash. Crash!

After using dozens of his subordinates as sacrifices to behead another Elder, the black-clad man laughed smugly.

“A Tang Clan Elder is nothing special.”

“You bastard!”

Screeeech! Thud!

Despite Tang Jinhu’s furious struggle, the situation did not improve.

More than a hundred clansmen had already lost their lives, and half of the Outer Hall had fallen into the enemy’s hands.

“Huff, huff.”

On top of that, his internal energy and stamina were rapidly running dry.

The battle had already reached a point where it could no longer be turned around by the strength of a single aging Supreme Peak master.

A lament escaped Tang Jinhu’s lips when he realized that.

“What are the Family Head and the Tang Clan’s Ten Wonders doing?!”

If they were here, the situation would have been different. Tang Sadok, the head of the family and its strongest master—and the Tang Clan’s Ten Wonders.

If they joined the battle, they could turn the tide.

But—

“Heh-heh. They’re probably quite busy by now.”

At the voice that suddenly pierced his ear, Tang Jinhu felt his heart drop.

“Who are you?”

“As for who I am… Damn it. I can’t see a thing. Get the hell out of my way.”

Boom!

With a powerful blast of displaced air, three or four black-clad men were hurled away, reduced to bloody mush.

An old man covered in blood stepped into the clear space ahead and flashed Tang Jinhu a wide grin.

“Much better. Now I can see.”

The old man was short, with an ugly face.

Tang Jinhu’s eyes trembled as he stared at him.

“You…”

“Hm? Do you know me?”

“…I never expected the Fiend of Qinghai to still be alive.”

The old man, First Fiend, stared at Tang Jinhu for a moment before his eyes suddenly widened.

“Ah, now I remember. You’re that youngster from the Tang Family. So, have you gotten any better at using the Soul-Severing Thread?”

“Good enough to cut off your head.”

“I thought the Sichuan Tang Clan were fairly practical people for an orthodox faction. But looking at you, I suppose that isn’t entirely true. You’re still lost in such foolish fantasies.”

“…”

“Youngster. You still haven’t figured it out, have you? This old man will tell you personally.”

First Fiend cackled as he continued.

“You, your Family Head, and those idiots called the Tang Clan’s Ten Wonders will all die. Whether they bear the Tang surname or are nothing more than dogs, I’ll kill and burn every last one of them.”

“You—!”

“Don’t be too upset. The Lord of Heaven treats all people equally—he has handed down the same punishment to the Buddhist nuns and those Daoist bastards. Heh-heh-heh.”

Tang Jinhu froze, forgetting even his anger.

Only now did he realize that First Fiend’s two younger brothers, who had always followed him like shadows, were nowhere to be seen.

*…Emei and Qingcheng.*

The carnage of corpses and blood had not been limited to the Tang Clan.

The Sichuan Tang Clan, Emei, and Qingcheng.

He could feel the people’s screams and deaths.

Today, the three factions that ruled Sichuan would fight a battle for their very survival.

Inside the hellscape those men had painted.

“Even after all these years… You truly are a Fiend.”

Tang Jinhu spat the words out through clenched teeth.

First Fiend answered with a smile brighter than ever.

“How kind of you. Could there be greater praise for this old man?”

“I’ll kill you.”

“Your body is old, but your dreams are ambitious.”

First Fiend laughed like a madman and raised the twin axes in his hands.

“Now, shall we taste blood again?”

As if that were the signal, hundreds of black-clad men who had already occupied the Outer Hall poured forward like a wave.

The Tang Clan martial artists who had survived stood in their way with the resolve to fight to the death.

“Go! Kill anything you see!”

“We have to stop them! Never let them into the Inner Hall!”

Those trying to break through and those trying to stop them.

At the very front, two men charged straight toward each other.

Screeeech!

Tang Jinhu threw the Soul-Severing Thread with every ounce of his strength, firm resolve shining in his eyes.

*Family Head, please be safe.*

Kwahhhhhng!

* * *

“Cough!”

Tang Sadok stared at his palm with trembling eyes. Small pieces of internal organs were mixed in with the dark-red blood.

“How… How could this…”

His head slowly rose with his exhausted voice.

At that moment, another life disappeared.

Thud! Crash!

The body of a man whose head had vanished collapsed like a rotten log.

Considering his fame in life, it was a death of unbelievable futility.

“Were they called the Tang Clan’s Ten Wonders? They’re more capable than I expected.”

A few steps from the corpse, a middle-aged man wiped the blood spattered across his face and continued.

“Of course, we’ll have to call them something different now. Let me see… Yes, the Tang Clan’s Three Skills[^1] seems appropriate.”

[^1]: In Korean, the word rendered as “Wonders” and the word meaning “Skills” are pronounced alike; he changes both the number and the written title to belittle them.

“…”

Tang Sadok looked at the middle-aged man through a blurred gaze.

The man had introduced himself as the Western Heaven Demon Lord, and the enemy who had killed Tang Sadok’s father was overwhelmingly strong. Neither Tang Sadok’s poison arts nor the combined assault of the Tang Clan’s Ten Wonders had been of any use.

*Is this really the end?*

Tang Sadok still had enough strength to fight. The other three survivors among the Tang Clan’s Ten Wonders did as well.

But…

*How are we supposed to stand against that monster?*

What made him rise despite the despair weighing him down was the mettle he could display as the Family Head and the Tang blood flowing through his body.

“Not yet. It’s not over yet.”

“Why don’t you just sit down? You must be out of strength.”

“I don’t know why, but I know you have no intention of killing this old man.”

“…Hm. As I said, the Poison King raised his son well.”

“Then kill me.”

“That won’t do. But I do need to wear you down a little first.”

Just as the Western Heaven Demon Lord frowned and reached out toward Tang Sadok—

“Wait, please, wait!”

“…”

A young man came rushing in with a shout and let out a sigh of relief.

“Phew. I’m not too late. Thank you for waiting!”

Looking at the young man, Cheongpung, the Western Heaven Demon Lord thought,

*What kind of lunatic is this?*

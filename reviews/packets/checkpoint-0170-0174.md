# Checkpoint Review — 170–174

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

# Chapters 170–174

## Plot

Jeok Cheongang, the previously unnamed old man, reaches Jang Family Village with Jang-pal and is sheltered by Jang-pal’s family. After learning that tall, handsome swordsmen came looking for him, he prevents Jang-pal from pursuing them and asks where they went. He then arrives at Jang Taebo’s home, identifies himself as a passing traveler, and cryptically directs Taebo toward the worried child nearby. Jeok intends to reach Taiyuan and visit the Lower District Sect while concealing his identity.

Taekyung shows Jang Taebo his huge supply of Ten-Thousand-Year Cold Iron. The *Find the Master Artisan* Quest is completed, and Taebo commits to forging the material into what he calls the greatest divine weapon under heaven. Jeok detects Taekyung’s Qi Sense despite its invisible nature; the System falsely displays him as Lv. 3. After interrogating Taekyung about his identity, sect, and abilities, Jeok releases overwhelming Extreme Yang Qi into his body.

Cheongpung and Hyuk Mujin intervene, but Jeok defeats them effortlessly, recognizing Cheongpung’s Huashan origins and Zaha Divine Technique. Cheongpung’s Plum Blossom Sword Technique prompts Jeok to recall his seven-day, seven-night draw with Mae Jonghak at Mount Jiuhua more than forty years earlier. After Demonic Cultists burned the mountain, Jeok emerged from seclusion and killed all one thousand attackers, becoming known as the Fire King.

Jeok recognizes Cheongpung as Mae Jonghak’s grandson and confirms that he is the Fire King. His internal energy resonates with and strengthens Taekyung’s Scorching Yang Qi. Taekyung conceals his possession of the Flame Divine Palm manual, consumption of the Blazing Flame Divine Pill, and killing of Jopil, but Cheongpung accidentally reveals that Taekyung killed Jin Baekyang, the Blade of Flowers and Taekyung’s great-uncle. Jeok attacks Taekyung with the Flame Divine Palm. Cheongpung briefly slows the strike, but Taekyung’s defense fails, leaving him unconscious with an Internal Injury.

The clash destroys Jang Taebo’s home, leaving only its foundation stones and ending his retirement. Jeok orders Taebo not to seek help and goes ahead to the inn, saying he will decide Taekyung’s fate after hearing the full story. Cheongpung carries the unconscious Taekyung and Mujin away.

## Continuity

- Jeok Cheongang is the nearly one-hundred-year-old Fire King of the Fire Gate Clan, a Supreme Peak master counted among the Ten Kings. Qi Sense’s Lv. 3 reading is false.
- Jeok once fought Mae Jonghak to a draw for seven days and seven nights at Mount Jiuhua. He later killed one thousand Demonic Cultists who burned the mountain.
- Jeok is heading toward Taiyuan and the Lower District Sect in disguise. He seeks an unidentified Peak master skilled mainly in sword and palm techniques.
- Cheongpung is Mae Jonghak’s grandson and disciple. He and Hyuk Mujin defended Taekyung but were defeated without being killed.
- Jin Taekyung is a Level 71 Peak Master with forty-five years of internal energy, Scorching Yang Qi, and seventy unassigned Stat Points. He killed Jin Baekyang and is unconscious with an Internal Injury after Jeok’s Flame Divine Palm.
- Taekyung possesses the Flame Divine Palm manual, consumed the Blazing Flame Divine Pill, and killed Jopil, but Jeok does not yet know these facts.
- Jang Taebo is the retired former Guild Leader of the Ironcraft Guild. He agreed to forge Taekyung’s Ten-Thousand-Year Cold Iron, but his home was destroyed and his retirement has ended.
- The linked Quest generated after *Find the Master Artisan* remains unresolved.
- Jang-pal’s family, including his daughter Hanga, previously sheltered and fed Jeok. Hanga gave the visiting swordsmen information about Jeok.
- Jeok has many questions about Taekyung and has not yet decided whether to kill him.
- The identities and motives of the tall, handsome martial artists seeking Jeok remain unknown.

## Translation Decisions

- Render 적천강 as “Jeok Cheongang,” 화왕 as “Fire King,” 화문 as “Fire Gate Clan,” and 초절정 as “Supreme Peak.”
- Retain “Qi Sense,” “Scorching Yang Qi,” “Flame Divine Palm,” “Blazing Flame Divine Pill,” “Ten-Thousand-Year Cold Iron,” “divine weapon,” “Ironcraft Guild,” and “Lower District Sect.”
- Render 허공섭물 as “Seizing an Object Through Empty Space,” 반박귀진 as “Returning to Simplicity,” 이형환위 as “Shifting Form and Position,” and 백련정강 as “Baekryeon Jeonggang.”
- Render 할부지 as “Grandpa,” 적 할아버지 as “Grandpa Jeok,” and 꼰대/꼰머 as “boomer”/“boomer-brain.”
- Retain “gukbap,” with a footnote explaining it as rice served in hot soup.

## Durable state

{
  "active_continuity": [
    "Jeok Cheongang is the nearly one-hundred-year-old Fire King of the Fire Gate Clan, a Supreme Peak master counted among the Ten Kings; his apparent Level 3 reading is false.",
    "Jeok Cheongang is secretive, cryptic, amused by unusual young martial artists, and quick to threaten violence during interrogation.",
    "Jeok Cheongang plans to reach Taiyuan and visit the Lower District Sect while concealing his identity, and he seeks an unidentified Peak master who mainly uses sword and palm techniques.",
    "Jeok Cheongang once fought Mae Jonghak for seven days and seven nights at Mount Jiuhua and drew; after Demonic Cultists burned Mount Jiuhua, he killed all one thousand attackers.",
    "Jin Taekyung is a Level 71 Peak Master with forty-five years of internal energy, Scorching Yang Qi, and seventy unassigned stat points.",
    "Jin Taekyung killed Jin Baekyang, the Blade of Flowers, and was rendered unconscious with an Internal Injury by Jeok Cheongang's Flame Divine Palm.",
    "Taekyung revealed a huge supply of Ten-Thousand-Year Cold Iron to Jang Taebo, who committed to forging it into a divine weapon; Find the Master Artisan was completed.",
    "Jang Taebo is the retired former Guild Leader of the Ironcraft Guild and a renowned smith over eighty years old who spent a full jiazi at the forge.",
    "Jang Taebo's home was destroyed by the clash between Jeok Cheongang and Taekyung, ending his retirement.",
    "Cheongpung is Mae Jonghak's grandson and disciple, has fought Jeok Cheongang using Huashan arts, and now carries the unconscious Taekyung and Hyuk Mujin to the inn.",
    "Hyuk Mujin is a Level 50 First Rate martial artist, Captain of the Gatekeepers, and Taekyung's subordinate in the reconnaissance squad.",
    "Jang-pal lives in Jang Family Village with his wife and daughter Hanga; they previously fed and sheltered Jeok Cheongang.",
    "The Datong Branches of the Jin Family of Taiyuan and the Lower District Sect tracked the Heavenly Wind Band before finding its annihilated force.",
    "Jin Baekyang, the Jin Family of Taiyuan's Head Elder and Taekyung's great-uncle, died in battle about two months ago and was buried in the family cemetery after Jin Wikyung overrode the family's opposition."
  ],
  "continuity_sources": [
    174
  ],
  "open_questions": [
    "Who is the unidentified Peak master Jeok Cheongang seeks, and where is that person?",
    "Where can Taekyung find the Herb of Eternal Youth?",
    "Who is the unnamed giant leading the Heavenly Wind Band?",
    "What is the linked Quest generated after Find the Master Artisan?",
    "Who are the tall, handsome martial artists who came looking for Jeok Cheongang?",
    "Why does Qi Sense display Jeok Cheongang as Level 3 despite his Supreme Peak martial ability?",
    "Was Jopil a disciple of Jeok Cheongang?",
    "How severe is Taekyung's Internal Injury, and when will he regain consciousness?"
  ],
  "safe_through": 174,
  "temporary_decisions": [
    "Render 삼매진화 as “Samadhi True Fire”; render 정기신 as “essence, qi, and spirit,” 백염 as “white flames,” and 입신지경 as “a transcendent realm.”",
    "Render 어르신 as “elder” and 형님 as “big brother” when used for Jeok Cheongang.",
    "Render 명장 as “Master Artisan,” 장인을 찾아라 as “Find the Master Artisan,” and 가공되지 않은 만년한철 as “Unprocessed Ten-Thousand-Year Cold Iron.”",
    "Render 철기방 as “Ironcraft Guild” and 철기방주 as “Guild Leader of the Ironcraft Guild.”",
    "Render 항아 as “Hanga,” 장팔 as “Jang-pal,” 장가촌 as “Jang Family Village,” and 신령님 as “Mountain Spirit.”",
    "Render 반박귀진 as “Returning to Simplicity,” 이형환위 as “Shifting Form and Position,” 허공섭물 as “Seizing an Object Through Empty Space,” and 백련정강 as “Baekryeon Jeonggang.”",
    "Render 꼰대 as “boomer,” 꼰머 as “boomer-brain,” and 국밥 as “gukbap” with a footnote.",
    "Render 작은 조부님 as “great-uncle” and 전사하셨습니다 as “He fell in battle.”"
  ],
  "version": 1
}

## Reading copies

## Chapter artifact 170

# Chapter 170

*Old and small.*

That was the old man’s first impression of Jang Family Village.

Sitting on the slowly swaying wooden carrying frame and gazing at the houses scattered sparsely across the village, he added in a voice so quiet that no one could make out the words,

“…And peaceful.”

It seemed the years had passed after all. Even an insignificant view like this made his body relax and a corner of his heart itch.

Just like that day, twenty-some years ago.

*It was the same when I took that child in.*

Suddenly, a child he had met long ago flashed before his eyes.

Under normal circumstances, he would have tossed the child a few iron coins or simply ignored them and walked on. But that day had been different.

Perhaps it was because he had just realized that he had developed an illness of old age?

He had looked at the owner of that desperately outstretched hand and, without realizing it, spoken a single sentence.

*Will you come with me?*

“Elder, we’re here.”

The woodcutter’s voice brought the old man back to his senses.

They had stopped in front of a small house. Something small suddenly popped out from behind a loosely woven fence made of bundles of branches.

“Dad!”

“Oh, my daughter!”

The little girl, no more than six or seven years old, came pattering over and clung tightly to her father’s leg.

The old man lightly jumped down from the carrying frame and gazed at the scene.

“Is she your child?”

“Ah, yes. That’s right. Hanga, greet him. This gentleman is…”

Come to think of it, he did not even know the old man’s name.

When Jang-pal trailed off, the old man waved his hand.

“No need for names. It’s nothing.”

Just then, Hanga, who had been gazing up at the old man with sparkling eyes, came toddling over and smacked his bony thigh.

“Grandpa!”

“Hm?”

“What’s your name, Grandpa?”

“I don’t know. I’ve forgotten it too.”

The old man had only said it to avoid the annoyance, but Jang-pal took it differently.

*He’s not sound of mind enough to remember even his own name.*

A simple mountain man, Jang-pal felt terribly sorry for the old man.

He could not leave someone who had apparently been abandoned by his children to wander the streets in clothes barely better than rags.

“Elder, why don’t you at least have a meal first? I’ll prepare a place right away.”

“No need. What I ate earlier was enough.”

“Even so…”

“There’s someone I need to find. I’ve already been delayed for quite some time, so I ask for your understanding.”

After finishing his sentence, the old man stopped.

*Understanding?*

The word that had slipped from his mouth felt unfamiliar.

He had lived his entire life without anything holding him back. Everyone had feared and revered him. Even the renowned masters of Murim had tucked their tails between their legs in his presence.

And yet, with this humble villager he had known for less than half a shichen, such words came easily.

*I’ve grown old. I’m definitely old.*

Someone tugged at the old man’s sleeve as he stood there, bewildered.

When he looked down, he saw chubby baby fat quivering in motion.

“Who are you looking for? Hanga is good at finding people.”

“…Is that so?”

“Uh-huh! Yesterday, I found Grandpa Jang from the house three houses over.”

“You did well.”

“When I found him, he gave me something tasty. I ate until I thought my stomach would burst.”

After saying something incomprehensible, she planted a hand on her waist. Her expression was almost solemn.

“And people have to eat to have strength. At Grandpa’s age, you can chew iron and eat it.”

“H-Hanga!”

“Ha ha ha!”

The old man laughed heartily for the first time in a long while. When was the last time he had laughed like this? It must have been more than ten years ago.

After his laughter faded, he patted Hanga’s round head.

“Yes, you’re right. This old man can chew iron and eat it.”

“Uh-huh. I’m always right.”

With a proud smile, Hanga grabbed his sleeve and led him into the house. The old man followed, pretending he had no choice.

Even if the strongest man under heaven had attacked him, he would not have budged. But today was an exception. More importantly…

*This isn’t so bad.*

He rather liked the situation. It almost felt as though he had become an ordinary old man for once.

As soon as they entered the room, Jang-pal’s wife brought out a meal.

“I’m sorry the side dishes aren’t much.”

Just as she said, the food was simple: a few kinds of namul and mixed-grain rice. The meat soup they had served to make the meal more special was pale and bland.

But everything had been prepared with care. It was obvious at a glance that they were not well-off, yet they welcomed the shabby old man occupying their table as a guest rather than an unwelcome intruder.

*Well, now.*

The old man finished the meal with a strange feeling in his heart. Hanga asked him with sparkling eyes,

“Grandpa, was it tasty?”

“Yes. It was the most delicious thing I’ve eaten lately.”

“Right? My mom cooks the best in the whole village.”

“…Is that so?”

“Uh-huh!”

*It wasn’t that good.*

The old man swallowed the words he wanted to say and nodded.

He had not eaten the meal for its flavor. He had eaten it for the care that went into preparing it.

Hanga, unaware of that, continued chattering excitedly.

“Grandpa Jang from three houses over sometimes comes to our house to eat too. Yesterday I ate at his house, though. Hee hee.”

As Jang-pal watched his daughter fondly, he asked,

“Hanga, you went to the elder’s house again?”

“Uh-huh. Grandpa gave me something tasty yesterday. The other older brothers did too.”

“How many times have I told you not to bother the elder? But what do you mean, older brothers?”

Jang Family Village was a small place. The few young people had either left for other regions or joined Murim sects with dreams of making their fortunes in the martial world.

Those who remained had all started families of their own, so there were hardly any men Hanga could call older brothers. And yet she had mentioned older brothers.

“Were they people you’d never seen before?”

“Uh-huh. They were tall and handsome, and they gave me this much food. So I found Grandpa for them.”

“You found him? Were they looking for the elder?”

“I don’t know. They were just looking for Grandpa. They were cool older brothers with sticks hanging from their waists.”

“Sticks hanging from their waists… Swords?”

They were martial artists. There was no doubt about it.

The faces of Jang-pal and his wife grew serious as they reached the same conclusion.

To ordinary civilians like them, martial artists were objects of fear.

How terrified had they been only a few months ago, during the war between the Jin Family of Taiyuan and the Mount Heng Sword Sect?

And now, unidentified martial artists had come right next door. Worse, their only daughter had become involved with them.

Jang-pal spoke with an anxious expression.

“So what happened?”

“When I took them to Grandpa, he shouted.”

“D-Did you hear who those older brothers were?”

“I heard them, but I forgot!”

Her answer was bright and innocent, but dark clouds gathered over her parents’ hearts. Jang-pal hurriedly rose from his seat.

“I need to go. The elder might have suffered some kind of misfortune.”

“Hanga’s father!”

“You stay here with Hanga. I’ll just sneak over and take a look, so don’t worry.”

Despite his words, he picked up the axe propped in a corner of the room. His horrified wife was about to stop him when—

“Sit down.”

“What?”

“Are your ears clogged? I said sit down.”

The old man, who had been sitting quietly, stood up. His bony knees gave a loud crack.

“I’ve eaten a hearty meal. I’ll take a walk while I’m at it. Consider it payment for the food.”

Jang-pal stared blankly at the old man before giving a hollow laugh.

“Elder, that isn’t a place you can go.”

“It’s the opposite. It’s a place you can’t go.”

“Please stay here. I’ll be back soon.”

“Will you be able to come back?”

The old man stared at Jang-pal with an unreadable expression.

When Jang-pal met those deep, sunken, unfathomable eyes, it felt as though his breath stopped.

“If they’re even a little—just a little—bad, you won’t be able to return. Do you mean to leave your child to grow up without a father?”

The old man’s eyes flashed like a streak of light, then faded.

As though nothing had happened, he patted his lower back and held out a hand toward Jang-pal.

“Give that here.”

That was all.

And yet Jang-pal handed the axe to the old man like someone under a spell.

“You’ve taken good care of it. It’s best to use this only for chopping wood.”

The old man calmly examined the sharp axe blade, then grinned at Hanga. Sensing the atmosphere, the child’s large eyes had already grown wet.

“Why the gloomy face?”

“I think Hanga did something wrong. Hanga was wrong.”

“Yes, this time you were in the wrong.”

Just as a sorrowful cry was about to burst from her, the old man’s voice continued, soft and gentle as a cotton quilt.

“So from now on, pay special attention to make sure something like this doesn’t happen again. Listen to what your parents say. Do you understand?”

“Uh-huh… But, Grandpa.”

“Go on.”

“Will Grandpa come back?”

The old man could not hold back the small laugh that escaped him.

“Of course. I’m old enough to chew iron. What could I possibly be unable to do?”

At that moment, Jang-pal, who had been briefly dazed, suddenly came to his senses.

No matter how you looked at it, he had handed an axe to an old man suffering from an illness of old age. He must have been thoroughly bewitched.

He had to correct this right now.

“Elder, please give me the axe. This, this is ridiculous—”

The next moment, Jang-pal could not finish his sentence. He stood there with his mouth hanging open, because an utterly unbelievable sight had unfolded before his eyes.

Crunch. Crunch.

The axe blade was breaking.

Each time the old man’s yellow teeth moved—teeth that looked incapable of chewing even soft chicken bones—the axe blade Jang-pal had carefully sharpened every day snapped apart piece by piece.

“W-What is this?”

“Your child has a good eye for people. She was exactly right.”

A conversation he had shared with the old man not long ago flashed through Jang-pal’s horrified mind.

*Why are there so many clan villages around here? Less than half a shichen ago, there was something called Hong Family Village or whatever.*

*Hong Family Village? Hong Family Village should be at least three hundred li from here. Are you perhaps confusing it with somewhere else?*

*Do I look like some idiot who can’t even remember something that happened less than half a shichen ago?*

Only then did Jang-pal realize that none of the old man’s words had been lies.

He was not an ordinary old man. Someone who could walk three hundred li in half a shichen and chew iron could not possibly be ordinary.

Only martial artists could perform such extraordinary feats.

“A martial artist…”

The old man asked Jang-pal, whose legs were trembling,

“So where are they?”

* * *

A voice filled with joy escaped between Jang Taebo’s lips.

“I’ll make you the greatest divine weapon under heaven.”

Ding!

> **System**
>
> - Quest objective complete.
> - Quest *Find the Master Artisan* has been successfully completed.
> - A linked Quest has been generated.

“…”

*Shit. If I’d known this would happen, I would’ve shown him sooner.*

Hyuk Mujin looked dumbfounded too. No—looking more closely, he looked horrified.

“Is all of that Ten-Thousand-Year Cold Iron?”

I scratched my chin. What did I know? The System said it was Ten-Thousand-Year Cold Iron, so I simply assumed it was.

“Yeah, probably.”

“No, you can’t just say ‘probably’!”

“I know.”

To be honest, I was flustered too.

When Jang Taebo had shown no reaction after hearing that I possessed Ten-Thousand-Year Cold Iron, I had assumed that people in the upper circles treated Ten-Thousand-Year Cold Iron as basic gear.

But as it turned out…

*Is it like a drink with ten percent apple flavoring added?*

They called it the greatest mineral under heaven, and judging by how people only shaved off tiny pieces to attach to a blade, it really must be incredibly rare.

While everyone else had to use weapons with five or ten percent Ten-Thousand-Year Cold Iron added, I could use one made with one hundred percent.

That was an incredible advantage.

It meant I could rely on my gear to give me a head start.

“With this—with this, I can create the masterpiece of my lifetime.”

Jang Taebo trembled all over, overcome with emotion.

It was hard to believe he was the same old man who had been so indifferent and dismissive only moments ago. Of course, I was happy things had worked out.

“Where on earth did you get such an enormous amount of Ten-Thousand-Year Cold Iron?”

“It’s a secret.”

“H-Have you perhaps discovered a mine where a massive amount of Ten-Thousand-Year Cold Iron was buried?”

Jang Taebo’s eyes flashed like high beams. He had said he no longer needed anything, but now he was—

“Tell me!”

I coldly shook my head. I did not even know where the mine was, and I could not tell him the truth anyway.

“No.”

“Please! I’ll beg you like this!”

“W-Wait, what are you doing?”

Now he was clinging to my trouser leg. The spirit of an artisan who had walked a single path for decades burned in his eyes.

“Come on!”

“Oh, for crying out loud!”

Just as I hurriedly pried Jang Taebo’s hands away—

“Is this the house of Grandpa Jang, who lives three houses over…? Damn it. It’s rubbed off on me already. Anyway, is this Old Man Jang’s place?”

A sharp voice stabbed at my eardrums.
## Chapter artifact 171

# Chapter 171

The owner of that sharp, ringing voice was a short, squat old man.

He was shorter than most elementary schoolchildren these days, and his clothes were grimy. But more than anything else…

*He’s incredibly old.*

I hadn’t lived that long, but in all my years, I had never seen anyone quite that old.

Just as I was thinking that, the old man’s eyes suddenly met mine.

“Hey!”

“Yes?”

“When an elder asks you a question, you’re supposed to answer. Is this Old Man Jang’s place?”

*Is that the vibe that comes with experience?*

The old man looked as though he could drop dead at any moment, yet his eyes were so vivid they practically blazed. Feeling strangely intimidated, I answered,

“It is.”

Jang Taebo, who had been clutching my trouser leg, rose awkwardly to his feet.

I had wondered if the old man might be one of his friends from the senior center, but the wary expression on Jang Taebo’s face suggested otherwise.

“Who are you?”

“Just a traveler passing through. Are you Old Man Jang?”

“That’s right.”

“I see. I stopped by just in case.”

The old man glanced around and added,

“Though I suppose there wasn’t any need for that.”

“…”

“…”

“Then I’ll be going. Once you’re finished here, go visit the little one who lives over there. They’re worried about you.”

With that, the old man turned around.

*What the hell was that old man?*

Everyone was left bewildered by his incomprehensible words and actions. Just then, Cheongpung, who was standing beside me, poked me in the side.

“Smack, smack. Benefactor. Doesn’t that man seem a little strange?”

“…”

“You look stranger to me. And swallow what’s in your mouth before you talk.”

*How long is that guy going to chew those dumplings? Does he have a bottomless spring that keeps producing them?*

At my scolding, Cheongpung gulped down what was in his mouth and muttered,

“No, but there’s something strange about him.”

“Such as?”

“I don’t know. It’s just a feeling.”

“What kind of answer is th—”

Wait.

It was just a feeling?

I froze for a moment. Cheongpung might have been an eccentric, but he was the disciple who had inherited everything from the Sword Saint, as well as a Peak master far above me in skill.

*Could he have sensed something about that old man that I couldn’t?*

*On the surface, he just looks like an ordinary old man…*

There was nothing to lose by checking. In the Murim, where anything could happen, it was best to knock on even a stone bridge before crossing it.

*Activate Qi Sense.*

Ding!

> **System**
>
> - You have used the Skill *Qi Sense*.
> - You can detect targets up to Level 90 within a range of 70 meters.
> - Internal energy is consumed in proportion to range.

Whoosh.

A blue line visible only to me rapidly shot outward.

It passed through Cheongpung, Hyuk Mujin, and Jang Taebo, who were closest to me, before finally reaching the back of the old man as he slowly walked away.

A translucent holographic window suddenly rose above his completely white hair.

> **System**
>
> **Lv. 3 Jeok Cheongang**

*Jeok Cheongang? Now that’s a name fit for a final boss.*

But despite his impressive name, his Level was pitifully low. The old man was unquestionably an ordinary civilian who had never learned martial arts.

“He just seems like a false lead—”

My voice trailed off on its own.

The old man’s leisurely steps had stopped.

His short body slowly turned around. Though he was more than ten jang away, the strange light in his eyes made my skin prickle.

*What?*

My body stiffened. My heart began pounding, and my fingertips twitched.

If the old man’s lips had not opened at that moment, I might have summoned a weapon from my Inventory right then and there.

“Well, this is something…”

The corners of the old man’s wrinkled mouth twitched as he looked at me. His low voice pierced my ears.

“What an interesting fellow.”

* * *

The old man, Jeok Cheongang, encountered a rather interesting situation the moment he arrived at his destination.

*Oh-ho. Well, look at these fellows.*

The Supreme Peak realm was an inhuman domain where one could be called a Martial God without exaggeration. He recognized the young men’s martial prowess at a glance.

One of them was merely so-so, but the other two…

Honestly, they were impressive.

*At that age, they’ve already broken through the wall.*

The one noisily chewing dumplings in front of an elder, especially, had already reached a fully mature Peak realm. It would not be an exaggeration to say so.

*Would only the Elders of the Nine Sects and One Gang whom I crossed paths with briefly in the past be able to compare?*

The other one was tall and broad-shouldered.

*L-Look at the way that bastard’s opening his eyes so rudely. Maybe I should gouge them out.*

The young man had a face like he had seen a walking corpse. Even so, it was obvious that he possessed martial arts far beyond what his age suggested.

*No one his age could stand against him.*

*The rear waves of the Yangtze push the front waves away.*

That was what they said. Jeok Cheongang suddenly realized that the new wave was quite large and fierce.

Large enough to swallow the entire Yangtze.

*I suspected as much when they started making a fuss about Ten-Thousand-Year Cold Iron and all that… But they’re even more interesting than I expected.*

Jeok Cheongang could sense presences dozens of jang away. He had been listening to their conversation ever since he left Jang-pal’s house.

He also knew that the matter Jang had been worried about had not happened.

Far from being coerced, Old Man Jang seemed to be the one clinging to them.

*Given their accomplishments and the fact that they’d even brought Ten-Thousand-Year Cold Iron, could they be from the Nine Sects and One Gang? Well, either way, they clearly belong to a prestigious orthodox faction.*

That was the extent of Jeok Cheongang’s interest.

There was no reason to form a connection with those young men, and he had no desire to reveal his identity.

He had done enough to repay the meal he’d been given, so he intended to leave at once.

“Then I’ll be going. Once you’re finished here, go visit the little one who lives over there. They’re worried about you.”

Jeok Cheongang tossed out his final words and turned away.

He had already wasted quite a bit of time. He planned to reach Taiyuan sometime today and visit the Lower District Sect.

Of course, he had no intention of letting anyone discover his identity.

*A rough mask and a little intimidation should make them spill everything.*

But Jeok Cheongang’s thoughts could go no further.

The next moment, something unknown shot toward him from behind.

Whoosh.

He could neither see nor hear it.

He had only sensed it. A cold, unfamiliar presence pierced toward Jeok Cheongang’s back.

*An ambush?*

No. There was no sticky, unpleasant killing intent.

Instead, it was as natural as a breeze blowing from far away, which made it all the more alien.

The unknown energy vanished the moment it touched Jeok Cheongang’s back.

*What in the world…?*

He had lived for nearly a hundred years, but this was the first time he had experienced anything like it.

Still bewildered, he turned around and immediately realized who was responsible.

“He just seems like a false lead—”

The instant their eyes met, the mouth snapped shut. The young man’s eyes shook, and his fingertips twitched.

Jeok Cheongang’s lips slowly lifted as he looked at the culprit.

“Well, this is something…”

He stroked his chin with an intrigued expression.

“What an interesting fellow.”

At the same time, his foot pushed off the ground.

The distance of more than ten jang between them vanished in the next instant. Jeok Cheongang whispered into Jin Taekyung’s ear.

* * *

*Inventory summon.*

Just six syllables.

All I had to do was picture the spear and shout the words in my mind. But…

“What kind of man are you?”

The breath tickling the back of my neck made every hair on my body stand on end.

*When did he—?*

No, before that…

*How?*

*He was definitely, definitely Level 3.*

It was impossible to believe.

The old man named Jeok Cheongang, who looked as though he could die at any moment, was faster than anyone I had ever seen.

So fast that I did not even dare imagine resisting him.

“Hey, when an elder asks you something, you answer.”

“Y-Yes?”

“Is that your answer?”

A thin, wrinkled finger poked me repeatedly in the solar plexus. There was no force or internal energy behind it, yet it felt as though someone were stabbing me with a sword.

“I’m asking what you are.”

I swallowed hard. My mouth felt as dry as if someone had poured a handful of sand into it.

“I’m Jin Taekyung.”

“Not that crap. Which sect are you a disciple of?”

“Taiyuan—the Jin Family of Taiyuan.”

“The Jin Family of Taiyuan? Does it practice demonic, heterodox arts?”

I nearly nodded without thinking.

The old man’s eyes flashed when he mentioned the demonic, heterodox arts. If I answered yes even by mistake, he looked ready to cut my life short on the spot.

“I’m with an orthodox faction.”

“You are? Then why are you stammering?”

“I’m telling the truth.”

“Taiyuan’s Jin Family… I think I’ve heard of it. Or maybe I haven’t.”

Jeok Cheongang had been lost in thought when he suddenly looked at me strangely.

“The more I look at you, the stranger you are. That thing just now—it was you, wasn’t it?”

*That thing just now?*

His words were vague, but I understood them immediately.

*This old man definitely sensed Qi Sense.*

*How is that possible?*

I had vaguely suspected as much when he reacted immediately, but the sight of it still made my vision go dark.

*Good God. A monster who can sense Qi Sense.*

“Why aren’t you answering?”

I bit down hard on my lower lip and answered,

“No.”

“How do you know what it was?”

“…”

“Hey. It was you, right?”

“No. Anyway, it wasn’t me.”

“Oh, I like that. You seem to have some backbone. Manly.”

Jeok Cheongang laughed heartily and continued,

“Should I break a few bones and ask you again?”

“It was me! Yes, it was me!”

“Good. Fine. Then what did you do to me?”

I hesitated for a moment.

My opponent was an old man whose instincts were as sharp as the years he had lived. If I lied here and got caught, I would not be leaving with my body intact.

I had to stick as closely to the truth as possible while presenting it in a way he would find agreeable.

“You seemed like an extraordinary person, so I just…”

“A little?”

“I checked whether you had learned martial arts.”

“How?”

“Yes?”

“I’m asking how you did it.”

“I just sent a little of my qi toward you and read your qi. Something like that.”

“Ha. Is that so?”

Jeok Cheongang laughed as though he found it amusing, then clenched his fist.

“If you keep lying, I’ll break your legs. Answer me again.”

I hurriedly waved my hands.

“W-Wait a second. Why are you suddenly acting like this?”

“You’ve completely misjudged this old man. Do I look like some fool who can’t distinguish something like that? What I felt just now… was different. Different enough to make me think it was the dark arts.”

“What dark arts? I’m telling you, it’s real!”

*This is driving me insane.*

Qi Sense was certainly a cheat Skill, closer to a System function than martial arts.

Because of that, someone like Jeok Cheongang, who seemed to be a Supreme Peak master, might have sensed a strangeness unlike anything he had encountered before.

*The problem is, how the hell am I supposed to explain that?*

“You bastard! Can’t you tell me the truth?”

*Fuck this. I’m done.*

I decided to be completely frank.

“The truth is, I use something called the System. It’s a bit of a cheat, so it might have felt strange to you. I’m sorry.”

Jeok Cheongang did not speak for a moment.

Then he opened his mouth.

“What kind of bullshit is that?”

“…”

“I told you exactly what happened. I figured you wouldn’t understand.”

“Have you said all you have to say?”

“There’s a lot I haven’t said. I’ve been through so much.”

“You’ve had a turbulent life.”

“You have no idea.”

“Don’t worry. After today, your life won’t have any more twists and turns.”

“Are you planning to make it nothing but downhill from here?”

“Why bother saying it? How about we warm you up a little before we begin?”

It happened in an instant—too fast for anyone present to react.

Jeok Cheongang let out a quiet laugh and poked me in the chest with one finger.

And then…

Whoooosh!

An overwhelming wave of heat swept through my body.
## Chapter artifact 172

# Chapter 172

Jeok Cheongang wore a smug grin.

*Heh heh. Have a taste of something hot, you little punk.*

His fingertips carried Scorching Yang Qi that had reached the pinnacle.

Though he was using only three-tenths of his internal energy, it was still far beyond what a fledgling who looked barely twenty could withstand.

*This ought to snap him back to his senses.*

Jeok Cheongang had no particular hobby of tormenting children, but this one needed to be taught a lesson.

All this time, the boy had been spouting incomprehensible nonsense about some “shisudaem” or whatever. It was hard to listen to.

*I’ve controlled my strength, so if things go well, he might even avoid an Internal Injury.*

If things went well.

Jeok Cheongang added that condition silently as he reached out.

*Tap.*

The instant his bony, wrinkled finger touched the young man’s broad chest, Extreme Yang Qi surged forward like a tidal wave. Jin Taekyung sucked in a startled breath.

“Hk!”

“How is it? Feels like there’s a fire burning inside you, doesn’t it?”

Jeok Cheongang could not help laughing when he saw the boy’s face turn bright red. The saying that a beating was the best medicine truly was an eternal truth.

“Now, stop talking nonsense and tell me the truth—”

*Whooosh! Shhk!*

Jeok Cheongang could not finish his sentence. Two swords had flashed in like lightning and slashed through his waist and arm.

“Did it work? It worked! Young Hero Cheong, you did it!”

Unlike Hyuk Mujin, who was celebrating with a dazed expression, Cheongpung merely scratched the back of his head.

Instead of blood spraying before his eyes, Jeok Cheongang’s figure scattered like mist.

“Uh… Returning to Simplicity and Shifting Form and Position… We seem to have picked the wrong fight.”

Jeok Cheongang was already sitting on a fence some distance away, laughing loudly.

“Your eyes are pretty useful.”

“I’ve seen a lot of things since I was little.”

“You grew up watching?”

Jeok Cheongang was genuinely surprised when he realized what those words implied.

Returning to Simplicity and Shifting Form and Position were both domains permitted only to Supreme Peak masters. That meant Cheongpung had grown up around someone who stood at the same realm stage as him.

“Who is your Master?”

“My grandfather.”

“What an obtuse brat. How would this old man know who your grandfather is?”

“My grandfather used to say that any man who hides behind someone else’s name after being born a man deserves to have his balls cut off.”

“Ha ha ha! What a splendid saying!”

After bursting into laughter, Jeok Cheongang fixed Cheongpung with a long look.

“Can you bear the punishment for daring to point a sword at this old man?”

Cheongpung licked his lips, looking troubled.

“But I didn’t use Sword Energy. Couldn’t you let it slide?”

“Would it have made a difference if you had?”

“Hmm. I don’t think so.”

Jeok Cheongang let out a quiet laugh. He did not know which sect or master the boy belonged to, but he was certainly an interesting one.

“Then why did you step forward?”

Cheongpung pointed at Jin Taekyung, who stood frozen like a monument.

Hot steam rose in wisps from his entire body, which had been heated to a reddish hue.

“I owe that gentleman a little. How could I just stand by while you bully my Benefactor, sir?”

“You must owe him quite a lot. Enough to risk your life, at least.”

Cheongpung’s eyes widened.

“Are you going to kill me?”

Of course, Jeok Cheongang had no intention of killing anyone here. But he deliberately hardened his expression and lowered his voice.

“Of course.”

“Uh-oh. That won’t do. There are still so many things I haven’t tried.”

“This is the Murim. Should this old man take circumstances like that into account?”

Cheongpung thought about it carefully before answering.

“I suppose not.”

Hyuk Mujin, who had been listening to their conversation with growing anxiety, suddenly exploded.

“You can’t just accept that, you idiot!”

“Why not?”

“Because that old man—no, that gentleman—is going to kill us!”

“He isn’t wrong. Hmm, and besides…”

Cheongpung calmly added,

“We won’t know whether we die or live until we try.”

“…Damn it. Fine, let’s do it. If we just sit here, Captain will beat us to death later anyway, so whatever.”

Jeok Cheongang rested his chin on his hand and gazed at the two young men.

They really were interesting.

One was willing to stake his life because he owed someone a debt. The other grumbled while stepping into a battle whose outcome was obvious.

There was something in them that some people called reckless bravado and others called chivalry.

*People like this always die young.*

That had been true forty years ago, and it would probably be true now as well.

That was why Jeok Cheongang had developed a faint fondness for the youngsters. At the very least, they possessed the courage to risk their lives for someone else.

Just as they were doing now.

“Then shall I teach you a thing or two?”

Jeok Cheongang slowly rose to his feet.

At the same time, an aura as vast as a mountain erupted from his short frame and pressed down on everything around him.

Cheongpung and Hyuk Mujin gripped their sword hilts, while Jang Taebo collapsed onto the ground with a deathly white face.

“You stay out of this.”

Jeok Cheongang flicked a finger.

Jang Taebo’s body floated over the fence as though an invisible hand had seized and lifted him.

Cheongpung muttered at the sight,

“Seizing an object through empty space…”

With a single gesture, the old man had lifted Jang Taebo, whose body was larger than that of most full-grown men.

It was proof that the old man before them possessed internal energy no weaker than his grandfather’s.

Hyuk Mujin also muttered with a vacant expression,

“Damn. That’s something you only ever see in novels.”

The difference in their levels was absolute.

At this moment, everything surrounding Jeok Cheongang was both his weapon and his shield. The corner of his wrinkled mouth rose slightly.

“Come.”

That was the signal.

Cheongpung and Hyuk Mujin charged with every ounce of strength they possessed.

The two knew each other’s martial arts intimately after countless duels. Their swords meshed perfectly as they unleashed a coordinated attack.

*Whooosh!*

*Shhk-shhk!*

Just as the two blades were about to pierce Jeok Cheongang’s flank and neck, he stretched out both hands.

His hands were suddenly engulfed in white flames as he caught the blades.

“Do you think that will be enough?”

*Grrrk.*

Hyuk Mujin’s eyes opened wide.

His beloved sword, forged from Baekryeon Jeonggang—the hardest steel imaginable—was bending. Then it turned into molten metal and began dripping away.

“What is this?”

He had put everything he had into that strike, yet he had not even managed to leave a scratch.

As he stared blankly at the blade, already half melted, Jeok Cheongang’s voice reached his ears.

“Your courage was admirable. Get some rest.”

The next moment, Hyuk Mujin’s vision turned white. A palm strike struck him in the chest, and he dropped helplessly to his knees.

“Young Hero Hyuk!”

“Don’t worry. He should have suffered no more than a minor Internal Injury. More importantly…”

Jeok Cheongang glanced at the blade held in his other hand.

It had neither bent nor melted. Instead, it was wrapped in a faint purple Sword Energy.

Jeok Cheongang dredged up a memory from long ago.

“Zaha Divine Technique. Are you a disciple of Huashan?”

Cheongpung answered by throwing a punch.

The Crouching Tiger Fist, a powerful fist technique said to subdue tigers, slammed into Jeok Cheongang’s chest.

*Thud!*

Jeok Cheongang’s white eyebrows curved like a crescent moon.

“Well, look at you.”

That attack would have been enough to shatter a person’s chest, yet that was the entirety of his reaction.

Cheongpung felt as though he were facing his grandfather, the Sword Saint Mae Jonghak.

*He’s strong. Overwhelmingly strong.*

But Cheongpung could not give up like this.

He exhaled slowly and stamped his foot into the ground. The Zaha Divine Technique’s energy rippling through his body flared even more fiercely.

“Go on, then. Let yourself run wild.”

Jeok Cheongang grinned and relaxed his grip on the blade.

Freed from its restraint, the sword unleashed the ultimate techniques of the Plum Blossom Sword Technique.

*Shiiiiing!*

The tip of the sword moved fluidly, drawing plum blossoms in the air.

One became two. Two became five. Five became nine…

At last, twenty-four fully formed plum blossoms transformed into streaks of light and poured down toward Jeok Cheongang.

At this moment, even Jeok Cheongang could not help feeling genuinely impressed.

*Huashan has produced an incredible talent.*

And that brought one person to mind.

A figure who was practically synonymous with Huashan.

No—a figure revered by every swordsman under heaven.

“Mae Jonghak—what is your relationship with that friend of mine?”

The twenty-four plum blossoms wavered dangerously at the word *friend*.

The next moment, the Sword Energy narrowly missed Jeok Cheongang and reduced the surrounding area to ruins.

*Kaboom!*

Cheongpung swallowed a mouthful of thickly rising dust and coughed.

“Cough, cough. Do you know my grandfather, cough?”

Jeok Cheongang laughed with evident pleasure.

“I’ve met him. A very long time ago.”

It had been more than forty years ago.

The Demonic Cult’s hundred thousand followers had devoured half the world. As the tide of war turned against the orthodox faction, the orthodox Murim began searching even for eccentric masters who had withdrawn into remote mountain valleys.

That was when the Sword Saint Mae Jonghak visited Mount Jiuhua.

“Help me.”

Those were his first words.

Jeok Cheongang was surprised by the visit of a master who could be compared to himself, but his answer had already been decided.

“No.”

“The world is in danger.”

“Let’s speak plainly. It’s your orthodox Murim that’s in danger, not the world.”

Even if the master of the Murim changed, the world itself would remain the same. There were villains in the orthodox faction and good people in the Demonic Cult.

And Jeok Cheongang intended to remain on Mount Jiuhua forever.

Mae Jonghak was lost in thought for a long while before suddenly tapping his forehead.

“Oh, now that I think about it, you’re right.”

“…You didn’t come here to persuade me?”

“That’s that, and this is this, isn’t it?”

“What kind of nonsense is that? If you’re going to keep talking rubbish, go home.”

“Then let’s do this. We’ll follow the law of the Murim.”

“Might makes right?”

“If I lose, I’ll leave without complaint. Not only that, I’ll keep your existence hidden from the Murim forever. However…”

“If you win, I have to help the orthodox Murim.”

“Exactly. What do you say?”

“Draw your sword.”

They fought for seven days and seven nights.

It was a battle between Huashan, which had taken root as a great tree of the Murim over hundreds of years, and the Fire Gate Clan, whose martial arts had been passed down according to the principles of one-man succession and secret transmission.

It was a bloody struggle between two Martial Gods.

And the result was a draw, with neither victor nor loser.

“What a pity. With martial arts like yours, why are you holed up in a mountain village like this?”

“Mind your own business. It’s my affair. What does it have to do with you?”

“Oh. Now that I think about it, you’re right.”

“…Listening to you is exhausting. What are you going to do now?”

“Honestly, I’d love to keep going, but… they crossed Gansu and Sichuan fifteen days ago. It’s a shame, but let’s leave it here this time.”

It had been fortunate for Jeok Cheongang.

If their battle had continued for even a few more days, he would have been the one to lose.

Mae Jonghak was ten years younger than him, yet he was already an astonishingly powerful master.

Without his own formidable internal energy, Jeok Cheongang would never have been able to endure.

“They may reach Anhui soon. Take care of yourself.”

“No problem. All I have to do is guard Mount Jiuhua.”

“Oh. That’s true.”

“…Please stop talking and go.”

The Sword Saint Mae Jonghak left just like that, and the Demonic Cult’s army surged forward like a wave and crossed into Anhui.

Fifteen days later, the Demonic Cultists passing through Mount Jiuhua made a grave mistake.

“Set it on fire!”

Mount Jiuhua burned, and Jeok Cheongang emerged into the world.

Not one of the thousand Demonic Cultists survived.

And people began calling him by another name.

“Then my grandfather…?”

Fire King Jeok Cheongang merely smiled faintly instead of answering.
## Chapter artifact 173

# Chapter 173

“Then…?”

At Cheongpung’s astonished expression, the Fire King Jeok Cheongang gave him a faint smile.

“Have you heard of me?”

“My grandfather mentioned you sometimes.”

“Oh-ho. So that friend of mine hasn’t forgotten me. What did he say?”

“He said your martial arts were strong, but your personality was… well, pretty terrible.”

“…”

The truth was, Jeok Cheongang had never been particularly sociable. No, “not sociable” did not begin to cover it. He was downright awful.

He had suffered all kinds of hardships as a child, leaving him with a deep-rooted distrust of people. After that, he had grown up under a Master with an eccentric personality.

So perhaps it was only natural.

“I heard you picked fights almost every day during the Great Faction War. Apparently, you beat up practically every young prodigy from the Nine Sects and One Gang…”

“Ahem. Who says I beat up every one of them? And I was young back then. When you’re young and full of energy…”

“I heard you were sixty at the time.”

“Cough, cough!”

Jeok Cheongang, unable to defend himself, merely cleared his throat. Cheongpung added one more thing.

“But he said that you were a good person once you got to know you, so if I ever met you, I should treat you the way I treat him.”

The corner of Jeok Cheongang’s mouth twitched.

“Hmm. Mae Jonghak really does know me well.”

Jeok Cheongang had fought in the Great Faction War for a little over a year.

It was rare for two Supreme Peak masters to participate in the same battlefield, and he had met Mae Jonghak only about ten times. Even so, they had unquestionably been close enough to call each other kindred spirits.

*He did a fine job raising his grandson.*

Wait a moment. Had Mae Jonghak ever married?

Jeok Cheongang quietly examined Cheongpung’s face.

There was not a single feature that resembled the Mae Jonghak he remembered.

*He doesn’t look like a biological grandson…*

Well, it did not matter.

Whether they shared blood or not, the boy was clearly his successor.

Judging from his behavior and the way he spoke, it would not be an exaggeration to say that they shared a soul rather than blood.

With a pleased smile, Jeok Cheongang spoke to Cheongpung.

“I gained a dependable grandson today. Come, give this old grandfather a formal bow.”

“What?”

Cheongpung tilted his head.

“Why?”

“...What do you mean, why?”

Jeok Cheongang was caught off guard and began to stammer.

“Didn’t Mae Jonghak tell you to treat me the way you treat him?”

“Yes.”

“You little punk, if a grandson meets his grandfather, he should give him a formal bow.”

“My grandfather doesn’t care about things like that. He said only hidebound old men obsess over empty formalities.”

“...!”

Jeok Cheongang’s body trembled after suddenly becoming a hidebound old man.

“What do you call this again? I learned it recently.”

Cheongpung thought hard for a moment, then slapped his forehead.

“Oh, right. A boomer!”

“A boo… what?”

“A boomer. They say ‘boomer-brain’ means something similar.”

A boomer? Boomer-brain? Neither sounded particularly pleasant.

Jeok Cheongang did not know exactly what the words meant, but he understood the context well enough.

*Have I been hiding in the mountains for too long?*

The new waves of the Yangtze were stronger than he had imagined. Even so, he could not beat up the only grandson of his one kindred spirit…

Jeok Cheongang felt his head begin to ache and opened his mouth.

“Is that something young people are saying these days?”

“I don’t know. I only heard it for the first time recently.”

“From whom?”

“My Benefactor.”

Jeok Cheongang followed the direction Cheongpung was pointing and turned his head.

His eyes met those of a young man who was squinting at him.

“Hey, come here.”

* * *

*Did he see me? It felt like our eyes met for a moment…*

*No, he didn’t. Absolutely not. I closed my eyes right away. How could he have seen me?*

I trembled with my eyes shut.

As if I were struggling with all my might to treat an Internal Injury.

Just in case, I even added a groan.

“Uuugh!”

“Hey, I said come here.”

Stay calm.

He was just making a wild guess. If I fell for it immediately, I would be Third Rate.

At times like this, a Peak master had to clench his butt and keep acting his heart out.

“Uuugh!”

“Don’t force it. I’ve seen plenty of people shit themselves doing that.”

He had a point. I relaxed slightly at Jeok Cheongang’s helpful advice.

“Huuugh!”

“Good grief, what a brat. This is the last time I’m asking. Are you coming, or should this old man come to you?”

*The last time.*

I could not fall for a word like that.

I had to hold out until the very last last.

“This old man will go, then. You’re dead today.”

“...I’ll come.”

I opened my eyes with tears in them.

Two eyes blazing with flames were glaring at me.

He truly looked like someone worthy of the title Fire King.

*Fuck. The Fire King.*

*Why is hyung here…*

No matter how many times I thought it over, the situation was utterly unbelievable.

But reality did not change. That short, squat old man was a Supreme Peak master counted among the twenty strongest under heaven—the Fire King.

*I had a feeling from the start.*

I might have been the first person here to realize his true identity.

The moment Jeok Cheongang’s internal energy surged into me, the System had delivered a meaningful message.

Ding.

> **System**
>
> - Your *Scorching Yang Qi* is responding intensely.
> - It is assimilating the internal energy that has entered your body.
> - Your internal energy has risen slightly.

It had happened in the blink of an eye. At first, I thought I was about to be roasted alive. But soon my stomach grew warm, as if I had just eaten a bowl of gukbap,[^1] and my internal energy even increased.

*What the hell is this?*

At first, I was bewildered, but I figured something good was something good. The more I thought about it, though, the less I could afford to be so relaxed.

*Wait. My Scorching Yang Qi came from eating the Blazing Flame Divine Pill.*

How did it make sense that having the same Scorching Yang Qi meant I would not be harmed? It had even absorbed the energy.

I thought intensely for a short while before reaching a conclusion.

It was because they were of the same kind, both born from the same root.

That meant the old man belonged to the Fire Gate Clan, which passed its legacy down to a single successor in each generation. As far as I knew, the current Sect Leader was probably…

*The Fire King… No way. Why would a man who had been off the radar for nearly forty years come here?*

That was what I thought at the time.

They say the first of the five psychological stages cancer patients go through is denial. I was no different.

The only difference was that I entered the final stage—acceptance—in less than five minutes.

*He was close friends with the Sword Saint, lived on Mount Jiuhua during the Great Faction War, and when Demonic Cultists set fire to the mountain, he wiped them all out…*

*Fuck. He really is the Fire King.*

The more I listened to the conversation between Jeok Cheongang and Cheongpung, the more certain his identity became.

He had not explicitly declared, in his own words, that he was the Fire King. But anyone who did not realize it at this point was an idiot.

Once I finally reached the acceptance stage, a chill ran down my spine.

*I’m fucked.*

I pictured Jopil, dead with half his body blown away by my *One Annihilation*. I also thought of the *Nameless Sword* and the *Flame Divine Palm* martial arts manual sitting in my Inventory.

I had already gulped down the Blazing Flame Divine Pill, and it was safely stored in my dantian.

*God, my stomach hurts.*

Whether Jopil was that old man’s disciple or not, I had a problem either way.

With my thoughts in chaos, I slowly began walking like an ox being led to the slaughterhouse. Jeok Cheongang raised a finger.

“I’ll count to three. One.”

Whoosh!

I charged forward with every ounce of strength I possessed. The Fire King looked at me as though I were the craziest bastard he had ever seen and opened his mouth.

“Hey.”

“Yes!”

“You startled me. I’m not deaf, so speak softly!”

Smack!

A crisp impact left the back of my head throbbing. It was the first time I had ever been hit like that in the Murim.

Of course, I had no intention of protesting. My opponent was an irritable Supreme Peak master.

Jeok Cheongang narrowed his eyes as he watched me keep my mouth shut.

“Well, look at you. You’re much quieter than before.”

“No, I’m not.”

“Don’t lie to this old man. You’d have better luck deceiving a ghost. I could tell the moment you opened your eyes.”

Cheongpung approached with a worried expression.

“Benefactor, are you all right?”

*My body is fine. My soul is dying.*

I answered in a half-dead voice.

“Yes. More or less…”

“More or less?”

Without so much as a turn signal, Jeok Cheongang leaned his head toward me and looked me up and down.

“Hmm. Now that I think about it, why are you so fine? You should have been unable to move and forced to circulate your energy for at least half an hour.”

*Why am I fine? Because I absorbed the Blazing Flame Divine Pill.*

But I could not say that. Under his suspicious gaze, my mouth grew dry.

“You’re a strange one, the more I look at you. Which sect are you from?”

“I’m from the Jin Family of Taiyuan.”

“The Jin Family of Taiyuan… I’m sure I’ve heard of it somewhere.”

Jeok Cheongang furrowed his brow for a moment before suddenly exclaiming.

“Oh, was it the Blade of Flowers? That’s right. That fellow Jin Baekyang was from the Jin Family of Taiyuan.”

Blade of Flowers Jin Baekyang.

He was the Head Elder.

I never expected that name to come up here.

Under Jeok Cheongang’s demanding gaze, I licked my lips.

“That’s right.”

“I ran into him a few times while traveling. He was a decent fellow. He had a somewhat gloomy side, but everyone was like that back then. He was also very courteous.”

All that remained of a person was their memories. Especially for an old man like Jeok Cheongang, who did not have many years left.

*But why did it have to be the Head Elder?*

And apparently, he had remembered him fondly.

Then again, no one would have expected the Head Elder to commit such a thing until recently.

During the Great Faction War, he had possessed martial arts strong enough to make him a leading candidate for Family Head, as well as a great deal of respect from others.

“You seem to be of the Jin Family of Taiyuan’s bloodline, judging from your achievements. What is your relationship with the Blade of Flowers?”

“He’s my great-uncle.”

In reality, we had been locked in a relationship of killing or being killed. But I was not technically lying.

At the mention of shared blood, Jeok Cheongang’s eyes softened.

“Oh-ho. Is that so?”

“Yes, sir.”

“How old are you?”

“I’m twenty this year. I’ve reached the age of majority.”

“You seem to have learned Scorching Yang Qi. Did the Blade of Flowers teach you?”

“...Yes.”

He had taught me. At Eight Spring Gorge, about two months ago.

He had been so enthusiastic that I had nearly had my crown split open by Sword Energy.

“Your achievements are remarkable for your age. You’re far more advanced than the Blade of Flowers was in his day.”

Jeok Cheongang was even offering me compliments now.

The atmosphere had become warm and friendly overall.

Then he opened his mouth again.

“So, is he doing well?”

“Uh…”

*Well, he’s doing fine in his grave, I suppose.*

“He must have improved quite a bit by now. Should I stop by and see him while I’m here?”

“About that…”

*You can visit, but you won’t be seeing his face.*

The Head Elder’s grave was in a corner of the Jin Family of Taiyuan’s cemetery—in other words, the family cemetery.

The family elders had vehemently opposed it, but Jin Wikyung had pushed it through. He had felt guilty about the mistake made by his grandfather, the former Family Head.

“I suppose I should have a drink with him. It’s been a long time since I’ve seen him. Surely he won’t turn me away.”

I imagined Jeok Cheongang pouring liquor beside the Head Elder’s grave.

*Damn it. I can’t keep this up.*

I took a deep breath and opened my mouth.

“Um, there’s something I need to tell you.”

“What is it? Go ahead.”

“He passed away.”

“...What?”

“Just a couple of months ago, unfortunately.”

Jeok Cheongang was silent for a moment before muttering,

“Already? He was still in the prime of life.”

“…”

*The prime of life? He was over eighty.*

Of course, he had possessed powerful internal energy. If he had stayed out of trouble, he might have lived another twenty years.

“What happened?”

“He fell in battle.”

“He fell in battle?”

A trace of anger appeared in Jeok Cheongang’s eyes.

“Was it the Demonic Cult bastards?”

“No. The circumstances were complicated and sensitive, so it’s difficult to explain.”

“Do you know who killed him?”

“…”

“Did you avenge him? From the Jin Family of Taiyuan’s perspective, he was the kind of bastard they could grind up and eat, bones and all, and still not be satisfied.”

Listening to him made me feel as though my bones were turning to jelly.

I lowered my head silently with a sorrowful expression. Sensing the subdued atmosphere, Jeok Cheongang stopped speaking.

*Good. Perfect. Hyuk Mujin being unconscious was a stroke of genius.*

If he had been awake, he would have been shooting me sidelong glances and practically shouting, *This is the culprit. He killed him.*

*Enough. Once I get out of here, I’m getting the hell out of here. Maybe I should just use Logout altogether.*

And then, the next moment, I realized something.

“Huh? Blade of Flowers Jin Baekyang—isn’t he the person you killed, Benefactor? Right?”

I had forgotten about that bastard.

[^1]: *Gukbap* is a Korean dish of rice served in hot soup.
## Chapter artifact 174

# Chapter 174

“Wait? Blade of Flowers Jin Baekyang—isn’t he the person you killed, Benefactor? Right?”

I had only one thought.

*I should have muzzled that bastard’s mouth a long time ago.*

Was he even human? He was a beast.

But it was already too late. Cheongpung was rampaging like an unleashed pit bull terrier.

“It’s a famous story. After a fierce struggle, Benefactor drove a spear straight into Blade of Flowers’s chest—bam! Blood sprayed everywhere—splat!”

*Please stop. Enough, you lunatic.*

I had to stop him before it was too late. I was just about to hurriedly open my mouth when—

“I heard you even cursed at Blade of Flowers. ‘Take your hands off me, you son of a bitch!’”

“…”

“Where did you hear that, too?”

“Everyone I met seemed to know about it. When I said I was close to Benefactor, lots of people came over and told me all kinds of things. The cook even packed me a ton of delicious food.”

No wonder he kept disappearing so often.

While staying with the Jin Family of Taiyuan, he must have wandered all over the place, eating and listening to people’s stories.

*Thanks to him, I’m fucked.*

I swallowed hard and slowly turned my head.

Jeok Cheongang stood there with an utterly unreadable expression.

“It’s a misunderstanding.”

Jeok Cheongang’s eyebrow twitched.

“A misunderstanding?”

“Yes. Truly. It really is.”

“A misunderstanding. That can happen. Rumors that circulate through the Murim are always twisted and exaggerated.”

His dry voice continued.

“So you weren’t the one who killed the Blade of Flowers?”

“Uh… I was, actually. But the thing is—”

“Then there’s no need to hear more.”

I could not finish my sentence.

Just a few steps away, I saw Jeok Cheongang’s hands burning red.

*Whooosh.*

I could feel it.

An overwhelming flow of internal energy.

The cold shattered into pieces, and a desert’s hot wind whipped around us. The heat forcing its way between my lips felt as though it would burn my lungs away.

A memory from only a few months ago flashed through my mind.

*The Flame Divine Palm?*

That was right. It was the Flame Divine Palm.

But it was on an entirely different level from Jopil’s.

Several times stronger. Stronger, stronger, and simply stronger.

Jeok Cheongang was no longer an old man who did not have much longer to live.

He was the Fire King incarnate.

“You violated the sacred bonds of kinship and killed the Blade of Flowers. Are you truly human?”

“W-wait a moment! There are some very profound and complicated circumstances behind that…”

That had been a mistake.

Instead of talking about profound circumstances, I should have shouted that the Head Elder had betrayed the Jin Family of Taiyuan.

Profound and complicated circumstances?

*Shit, you have to let me explain before you decide anything.*

For a moment, I forgot who I was dealing with.

The Fire King, Jeok Cheongang.

He was the man who had burned a thousand people to death over the simple matter of trespassing on his home and setting it on fire. Words like *profound* and *complicated* were light-years away from him.

*Whooosh!*

*Damn old man…*

No wonder they called him the Fire King. He was ridiculously straightforward and fiery as hell.

Feeling the heat of the Flame Divine Palm, I opened my eyes wide.

*Is my life flashing before my eyes?*

In the slowed-down world, his palm, engulfed in flames, was moving sluggishly toward my chest.

If Jopil’s Flame Divine Palm had been beef-bone soup, this was spicy fish stew—loaded with hot green chilies.

If I took a direct hit from that, I could not guarantee I would survive.

*I have to block it.*

The problem was that I could not even move a finger.

The reason everything in the world seemed to be moving slowly was simply that my brain had recognized the threat of death. It was not because Jeok Cheongang had slowed down or I had sped up.

*Damn it.*

I desperately tried to raise my hand, but it was already too late.

In the darkness of despair, Jeok Cheongang’s burning red palm filled my vision.

That was when—

*Shiiiiiiik! Boom!*

A streak of Sword Energy shot out of nowhere and struck Jeok Cheongang’s hand.

Clear violet Sword Energy.

It was Cheongpung.

Beyond the thunderous explosion, I heard his cry.

“Benefactor!”

It was a desperate shout.

Even Cheongpung’s Sword Energy could not stop Jeok Cheongang’s Flame Divine Palm. It merely slowed it down for the briefest moment.

But the crossroads between life and death was always decided in that instant.

*Now!*

The forty-five years of internal energy coiled within my dantian stretched awake.

Scorching Yang Qi rose like a wildfire, surging along countless acupoints.

Its destination was both my hands.

I thrust them forward with all my strength toward Jeok Cheongang’s Flame Divine Palm.

*Damn it. I don’t even have time to draw a weapon.*

All I had managed to think of against the Flame Divine Palm was using my bare hands.

It was obviously insane, but it was the best kind of insanity I could manage in this situation.

I let out a roar from the depths of my soul.

“Cheongpung, you son of a biiiiitch!”

At last, my hands met the Flame Divine Palm.

*Gooooong.*

A deafening sound of splitting air erupted.

* * *

The sky seemed to split apart with a thunderous boom.

After a brief silence, the changes began.

*Fssssss.*

They crumbled into ash and scattered through the air.

The stone wall Jang Taebo had carefully built ten years ago. The few trees he had planted in one corner of the yard.

All of it.

Black ash fluttered down over the old man’s white hair.

“W-what in the world…”

The old man, Jang Taebo, could not control his trembling body.

He had spent a long lifetime in the Murim—long enough for the mountains and rivers to have changed six times over, and then some.

He was no more than a blacksmith who had never learned martial arts. But precisely because of that, he had been able to meet countless people.

*“I beg you like this. If you wish, I’ll even give you my head!”*

*“Make me the finest sword under heaven.”*

*“Are you really the Guild Leader of the Ironcraft Guild? I was sent here by the Imperial Son-in-Law.”*

From clueless martial artists to the leaders of renowned sects and great factions. Powerful figures from the imperial court had come as well.

The people who sought out Jang Taebo were all different, but his answer was always the same.

*“If you are worthy, I will make one for you.”*

Jang Taebo believed that every blade had a soul.

For a blunt, rounded lump of metal to take shape, it had to endure thousands, tens of thousands, of hardships. It was bent countless times and beaten again and again. It was heated until it glowed, then cooled until it was cold.

Only after that long process of endurance, once it had finally taken shape, did it gain a soul.

*So choosing a master worthy of a weapon must be part of my duty as well.*

Depending on whose hands held it, a sword could become a killing sword or a life-saving sword.

Jang Taebo knew that better than anyone, and so he never accepted a commission carelessly.

*Someone with a gentle nature. Someone overflowing with ambition. Someone determined to walk only his own path…*

They said no two people were alike. Countless people, each different from the last, had received weapons from him and returned to the Murim.

Some had died. Others had survived.

But they had shared one thing.

*They were strong. Every last one of them.*

They had been masters capable of becoming the overlords of entire regions.

Powerful people who could guard treasures everyone coveted and use them however they pleased.

Some had possessed martial arts that could be compared to those of the leaders of the Nine Sects and One Gang and the Five Great Families.

But…

*This one… this man is different.*

The Fire King, Jeok Cheongang.

The aura and martial arts that had erupted from that short, squat frame were no longer human.

Jang Taebo also realized that Jeok Cheongang would never need a weapon.

*His martial arts have reached the heavens.*

Whether he held something or not no longer mattered.

That was what the Supreme Peak realm he had vaguely imagined must be like.

“Phew.”

Jang Taebo exhaled the breath he had been holding.

As the strength left his body, the object tucked against his chest slipped to the ground.

It was so hard and light that it could hardly be believed to be a mineral, and it gave off a gentle glow even in broad daylight.

“Good grief!”

It was the treasure that would be reborn as his final masterpiece—the greatest work of his entire life.

Jang Taebo hurriedly picked up the Ten-Thousand-Year Cold Iron and pulled it against his chest.

Then he froze.

As his mind returned, he suddenly remembered something he had forgotten.

His client.

“W-wait! Stop! I said stop!”

Jang Taebo got to his feet and rushed forward.

At Jeok Cheongang’s feet, a young man lay sprawled on the ground. His clothes had all burned away, leaving him naked, and he did not move at all.

“I-is he dead?”

Jeok Cheongang did not answer.

He merely stared back and forth between his own hands and the young man, his face hardened into something terrifyingly rigid.

“Say something!”

“…”

“Y-you…!”

Jang Taebo exploded in frustration and was just about to examine the young man—Jin Taekyung’s—condition when a clear voice stopped him.

“He’s not dead. He only lost consciousness for a moment after suffering an Internal Injury.”

The owner of the voice continued,

“Right, Grandpa Jeok?”

“…”

At last, Jeok Cheongang’s voice emerged, hoarse and raspy.

Every word revealed the surprise and complicated emotions he had experienced.

“I never intended to kill him in the first place.”

Just as Cheongpung and Jang Taebo let out relieved sighs, Jeok Cheongang added one brief sentence.

“That was until now.”

“…”

“…”

“Don’t worry. I’ll decide everything after hearing the full story later.”

Jeok Cheongang stared at the fallen Jin Taekyung with a strange look in his eyes.

“I have a lot to ask this boy.”

The words sounded dangerous enough that Jang Taebo stepped forward.

Even after witnessing the Fire King’s martial prowess firsthand, the unyielding will forged by his long years did not waver.

“That sounds like you intend to torture him.”

“I don’t have that hobby. But if necessary…”

“Do you not know who this young man is? Even if you are a master counted among the Ten Kings, it would be a grave mistake to think you could turn all of Shanxi’s Murim against yourself and remain unscathed!”

Jeok Cheongang let out a quiet snort.

“There were once people who swallowed half the world with an army of one hundred thousand. Do you think I was afraid of them?”

“…”

Jang Taebo was left speechless.

That was right. His opponent was the Fire King.

The old monster of Mount Jiuhua who had once fought alone against the Demonic Cult when it sought to rule the world.

Orthodox, unorthodox, or demonic—he belonged to none of them.

He had thrown his own weight onto the scales of war.

The reason was simple.

They had invaded his territory.

Jeok Cheongang stared at Jang Taebo with reddish eyes.

“I have one request. Please, do not ask anyone for help. I don’t want to burn down Shanxi’s Murim at my age.”

He meant it.

And he possessed the power to turn his words into reality.

“Understood?”

“I-I’ll bear it in mind.”

“A wise decision.”

Jeok Cheongang gave him a crooked grin and turned away.

All the strength suddenly left Jang Taebo’s legs. As he began to fall, Cheongpung caught him and asked,

“Where are you going?”

“There’s an inn where you lot were staying, isn’t there? I’ll go ahead. Follow me.”

Cheongpung watched Jeok Cheongang’s back slowly recede and muttered plaintively,

“Whew. Grandfather was right. That man’s personality really is strange.”

He said it so calmly that, if Jin Taekyung had heard him, he would have reached for a muzzle.

Cheongpung turned toward Jang Taebo and bowed deeply at the waist.

“Sorry for causing you so much trouble. We’ll be going now.”

Then he tucked Jin Taekyung and Hyuk Mujin under his arms and scampered away with brisk, purposeful steps.

Jang Taebo stood there for a while as though he had been bewitched by a ghost.

Before long, he realized the crucial fact he had momentarily forgotten.

*The Fire King. What the hell is wrong with that old bastard?*

There had to be limits to such outrageous behavior.

He had burned everything down, leaving nothing but the foundation stones.

Staring blankly at the ash drifting in every direction, Jang Taebo let out a deep sigh.

“Fuck. This place is done for too.”

That was the moment his sweet retirement came to an end.

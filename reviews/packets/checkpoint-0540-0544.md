# Checkpoint Review — 540–544

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

# Chapters 540–544

## Plot

News of Jin Taekyung and Cheongpung’s appointment as masters of the Alliance Leader’s direct pavilion spreads through Henan. Hwangbo Gun’s attempted punishment backfires: Taekyung is ordered to fast, Taishan must pay ten times the damages caused by his actions, and Hwangbo Ak receives temporary disciplinary confinement.

Taekyung launches a recruitment campaign for the Two Dragons Pavilion, seeking upright, passionate martial artists capable of at least Sword Energy. A Honghakru performance turns his slogan into a popular song, drawing an overwhelming crowd. Interviews begin under Hyuk Mujin, but Jeok Cheongang’s violent rejection of Old Man Ilyang—an eighty-five-year-old Supreme Peak master seeking the Fire Gate Clan’s divine technique—drives away many applicants.

Sama Pyo, Young Sect Leader of the Black Dragon Demon Gate, applies with his giant, childlike subordinate Taishan. He admits that he intends to use Taekyung as a useful card, but Taekyung keeps him under consideration while warning that treachery will mean immediate execution. Ju Hwaran and Song Ilseom also apply; Taekyung accepts them after recognizing Hwaran’s need to gain fame and strength for the Yongbong Escort Bureau and Jeok Cheongang’s assessment of Ilseom as a formidable master.

Taekyung decides to build a team capable of containing the widening war against Dark Heaven. Hyuk Mujin commits to staying beside him, prompting Taekyung to ask him not to die. With Ju Hwaran, Song Ilseom, Sama Pyo, Taishan, and Hyuk Mujin accepted, the System confirms the minimum companion requirement and asks Taekyung to name the pavilion. He chooses **Fire Dragon Pavilion**.

## Continuity

- Mae Jonghak is Alliance Leader of the restored Murim Alliance; Song Ho commands the Hidden Shadow Pavilion.
- Jin Taekyung and Cheongpung were appointed masters of the Alliance Leader’s direct pavilion, formerly called the Two Dragons Pavilion and now named the Fire Dragon Pavilion.
- The Fire Dragon Pavilion includes Ju Hwaran, Song Ilseom, Sama Pyo, Taishan, and Hyuk Mujin. Its five-companion System requirement is complete.
- Ju Hwaran seeks the fame and martial strength needed to protect and lead the Yongbong Escort Bureau. Song Ilseom is a highly capable martial master.
- Sama Pyo is Sima Gong’s son, the Young Sect Leader of the Black Dragon Demon Gate, and has disobeyed his father while pursuing a route he believes still serves Sima Gong’s goals. Taishan is his giant, food-obsessed subordinate.
- Old Man Ilyang is Won Cheol, an eighty-five-year-old Supreme Peak master knocked unconscious by Jeok Cheongang after attempting to exploit the pavilion.
- Hyuk Mujin has committed to following Taekyung and remaining at his side.
- The Lord of Heaven’s identity and connection to the dangerous force from Taekyung’s original world remain unknown, as do Dark Heaven’s method for opening Gates, the Southern Heaven Demon Empress’s plans in Yunnan, and the outcome of Jeok Cheongang’s duel with Nangong Cheon.
- The reason Ju Hwaran and Sama Pyo’s political engagement ended remains unresolved. Whether further companions will join the Fire Dragon Pavilion is also open.

## Translation Decisions

- Render **이룡각** as **Two Dragons Pavilion** before its renaming and **화룡각** as **Fire Dragon Pavilion** afterward.
- Retain **Murim Alliance**, **Alliance Leader**, **Dark Heaven**, **Hidden Shadow Pavilion**, **Black Dragon Demon Gate**, **Old Master**, **Grandmaster**, **Ten Dragons and Phoenixes**, and **Blazing Flame Divine Dragon**.
- Render **일양노/열양노** as **Old Man Ilyang**, **원철** as **Won Cheol**, **흑혈도** as **Black Blood Saber**, **노귀산** as **No Guisan**, **원썬** as **One Sun**, **흑야왕** as **Black Night King**, and **녹림투왕** as **Green Forest Battle King**.
- Render **협** as **chivalry**, **인의** as **humanity**, **협객** as **knight-errant**, **대종사** as **Grandmaster**, **탈진** as the capitalized System status **Exhaustion**, and **호거아** as **Tiger Giant Child**.
- Preserve **Honghakru**, **Hongmae**, **Gowolru**, **Kunlun Cloud Dragon**, **Hak Woo**, **Dagger Hidden Flower**, **Sound Transmission**, **Going Murim ship**, **Young Chang piano**, and **One-Ride Heavenly Dragon**.
- Preserve Taishan’s clipped, childlike, literal speech; Sama Pyo’s polite candor; Jeok Cheongang’s blunt violence; Taekyung’s profanity and dry narration; the recruitment-song, audition, financial-therapy, and monster-comparison humor; and Mae Jonghak’s carefree “That can happen” refrain.

## Durable state

{
  "active_continuity": [
    "The Mount Song Resolution formally restored the Murim Alliance; Mae Jonghak is its Alliance Leader, and Song Ho commands the Hidden Shadow Pavilion under his authority.",
    "Mae Jonghak formally appointed Jin Taekyung and Cheongpung as the two pavilion masters of the Alliance Leader's direct pavilion, now named the Fire Dragon Pavilion.",
    "Tang Sadok and the Sichuan Tang Clan publicly support Jin Taekyung and Cheongpung and acknowledge an unrepayable debt to them.",
    "Taekyung believes the Zhongnan Sect resents him, the Jin Family of Taiyuan, and Jeok Cheongang after its repeated humiliations and will obstruct them.",
    "Cheongpung created Mimi Step from Mimi's movements; it is a snake-like footwork technique fast enough that Taekyung could barely track it with his naked eyes, and Mungyeong recognizes Cheongpung as having the makings of a Grandmaster.",
    "Mimi is now a large horned snake under Cheongpung's care, eats dumplings, sweets, and Blood Fish, and has recently had her condition examined by Mungyeong.",
    "Mungyeong ended Taekyung's direct training and assigned him a final task of incorporating martial principles into his learned martial arts; Mungyeong has accepted Cheongpung's offer to accompany him.",
    "Zhuge Feng's Demon-Sealing Formation still blocks all mana from the exposed Gate, while Jang Taebo is summoning artisans to process the Water God Dragon's remains.",
    "The Southern Heaven Demon Empress is traveling toward Yunnan and expects to cause further deaths.",
    "The Black Dragon Demon Gate remains a major unorthodox power descended from the Demonic Cult's Twelve Branches; Sama Pyo is its Young Sect Leader and Black Dragon Saber, Taishan is his giant subordinate, and Sama Pyo has disobeyed Sima Gong while pursuing a path he believes still serves his father's goals.",
    "Jin Taekyung remains a Supreme Peak master with Three Flowers Gather at the Crown, advanced qi perception, exceptional resistance to monster Fear, and public S-rank-level recognition despite retaining an A-rank license.",
    "The Fire Dragon Pavilion now includes Ju Hwaran, Song Ilseom, Sama Pyo, Taishan, and Hyuk Mujin, and its minimum five-member requirement for the companion Quest is complete."
  ],
  "continuity_sources": [
    544,
    543
  ],
  "open_questions": [
    "What is the Lord of Heaven's identity, how is he connected to the dangerous force Taekyung associates with his original world, and how can Dark Heaven open Gates?",
    "Where is the Southern Heaven Demon Empress ultimately headed, and what does she intend to do in Yunnan?",
    "What is the outcome of the duel between Jeok Cheongang and Nangong Cheon, the Azure Sky Sword King?",
    "Why did Ju Hwaran and Sama Pyo's political engagement end?",
    "Whether additional companions will join the Fire Dragon Pavilion."
  ],
  "safe_through": 544,
  "temporary_decisions": [
    "Render 고월루 as Gowolru, 곤륜운룡 as Kunlun Cloud Dragon, 학우 as Hak Woo, 이룡각 as Two Dragons Pavilion before its renaming, 화룡각 as Fire Dragon Pavilion, 협 as chivalry, 인의 as humanity, 협객 as knight-errant, 홍학루 as Honghakru, 홍매 as Hongmae, and 호거아 as Tiger Giant Child; render 전 정혼자 contextually as former fiancé or former fiancée.",
    "Render 탈진 as the capitalized system status Exhaustion; retain Ten Dragons and Phoenixes, Blazing Flame Divine Dragon, Dark Heaven, Murim Alliance, and Old Master.",
    "Render 황보세가 as Hwangbo Family, 소가주 as Lesser Family Head, 은비화 as Dagger Hidden Flower, and 전음 as Sound Transmission.",
    "Preserve the chapter's blunt profanity, financial-therapy humor, monster-comparison humor, and Mae Jonghak's carefree 'That can happen' refrain; render 고잉무림호 as Going Murim ship, 대종사 as Grandmaster, 왕희지 as Wang Xizhi, and 영창 피아노 as Young Chang piano.",
    "Render 일기천룡 as One-Ride Heavenly Dragon and Taishan's speech as clipped, childlike, and literal; render 일양노 and 열양노 as Old Man Ilyang, 원철 as Won Cheol, 흑혈도 as Black Blood Saber, 노귀산 as No Guisan, 원썬 as One Sun, 흑야왕 as Black Night King, and 녹림투왕 as Green Forest Battle King."
  ],
  "version": 1
}

## Reading copies

## Chapter artifact 540

# Chapter 540

They say that words without feet can travel a thousand li.

And these days, Henan Province was boiling like a cauldron over a charcoal fire.

Under countless watchful eyes, news of two exceptionally young Divine Dragons being appointed pavilion masters by the Alliance Leader’s special order spread across Henan before even two days had passed.

“Have you heard the news?”

“I’ve already heard it, so don’t tell me. Even that yellow dog in the back alley probably knows.”

Whenever two or more people gathered, they were busy gossiping about it.

Opinions were divided, but a considerable number of martial artists viewed Jin Taekyung and Cheongpung’s appointments favorably.

“Pavilion masters, huh? Of course. Those two are more than qualified.”

“Still, considering their ages, haven’t they been given responsibilities that are a little too heavy?”

“That’s what makes it so impressive. Who can achieve that level of might and merit at barely twenty?”

“Now that you mention it, you’re right.”

“Damn it. Listening to this is making my stomach hurt.”

“…And who the hell are you, Brother?”

“No, but isn’t it true? Some people are born into good families, meet good masters, learn peerless martial arts, and now they even get to become pavilion masters of the Murim Alliance?”

“By your logic, the young prodigies of the Nine Sects and One Gang and the Five Great Families are all Supreme Peak masters. And why are you taking it out on us?”

“I just got pissed off listening to you and decided to butt in.”

But where there was light, there was bound to be shadow.

Jin Taekyung and Cheongpung were objects of admiration, but they were also objects of envy. That was true not only of wandering martial artists who had lived rough lives, but also of disciples from prestigious sects and families.

“Damn it. How does this make any sense?”

“There’s nothing we can do. It wasn’t just anyone who gave them the appointment—the Alliance Leader himself issued the order. Our Sect Leader firmly told us not to say a word about the matter.”

“And what about you?”

“Whew. What good would it do to say anything? I’m only a third-generation Disciple. Besides, one of my fellow disciples let his mouth run a few shichen ago and got it bad. The enraged Senior Martial Uncle ordered everyone above him and below me to assemble, so…”

“I can imagine.”

“Some madman even called our Master over, so the atmosphere was incredible. He wrung us out down to our souls. He even asked what we were doing when the much younger Blazing Flame Divine Dragon and Huashan Divine Dragon were doing so well.”

“What kind of nonsense is that? Why blame us because those two are monsters?”

“Exactly. When you think about it, they couldn’t do it either.”

“Wait. Don’t tell me…”

“Are you crazy? I didn’t say it. But before anyone could stop him, the madman who’d called our Master over blurted out, ‘Their masters are the Fire King and the Sword Saint.’”

“Good heavens. What am I hearing right now? Look at my arm. I’ve got goose bumps.”

“You think you’re bad? Imagine how I and the other Senior Brothers felt after hearing it directly. Even now, I’ve got goose bumps all the way down to my balls.”

“I’m only saying this in case you’re planning something, but you don’t need to show me.”

“…Even if you begged me to show you, I never would. Anyway, things are insane because of those two. Though perhaps not quite as insane as in the Hwangbo Family.”

By then, everyone had heard the rumor that the Lesser Family Head of the Hwangbo Family and one of the Ten Dragons and Phoenixes, the Shandong Fist Dragon, had suffered a spectacular disgrace.

And after he was appointed Commander of the Murim Alliance’s Outer Hall, the difference between him and Jin Taekyung, a pavilion master directly under the Alliance Leader’s Office, could only be described as the distance between heaven and earth.

“I heard that the Family Head of the Hwangbo Family personally met with the Alliance Leader and demanded punishment…”

“He went around telling everyone himself, so it’s probably true. As for the result, you already know.”

Hwangbo Gun, the Family Head of the Hwangbo Family, had proudly bragged about his private meeting with the Alliance Leader. Before even half a day had passed, however, the disciplinary decision reached him, and he was forced to swallow the humiliation.

I. Jin Taekyung, Pavilion Master of the Two Dragons Pavilion, improperly sided with only one party despite witnessing the dispute firsthand. He is therefore ordered to fast for a limited period.

II. Taishan of the Black Dragon Demon Gate committed two offenses.

His first offense was causing a dispute on a main road and harming innocent civilians. His second offense was disregarding the Alliance’s rules and wielding a weapon first, thereby failing to follow proper procedure.

However, in light of the numerous eyewitnesses and testimonies, some justification for his actions is acknowledged. He is ordered to pay each person who suffered losses because of his actions ten times the amount of their damages.

III. The offense committed by the Shandong Fist Dragon, Hwangbo Ak, is similar to Taishan’s.

However, because he substantially caused the dispute and made remarks liable to cause trouble, he is ordered to remain under disciplinary confinement for a fixed period.

For Hwangbo Gun, it was enough to drive him mad.

The next day, rumors spread that Jin Taekyung had polished off ten bowls of gukbap[^1] in one sitting and patted his stomach, which only made matters worse.

The orthodox purists who supported him also voiced their discontent, but the shadow cast by the giant known as the Sword Saint Mae Jonghak was too deep. They could not defy the Alliance Leader’s authority over something as minor as this, so they had no choice but to swallow their anger.

And amid all the attention of people whose admiration and envy were hopelessly mixed together, Jin Taekyung, newly appointed Pavilion Master of the Two Dragons Pavilion, made another extraordinary move only a day later.

It began with a single notice pasted conspicuously on the wall beside a main road crowded with passersby.

“Have you seen it?”

“If you mean the news about the Two Dragons Pavilion, I’ve heard enough to make my ears bleed. Wait. Seen what? What are you talking about?”

“About half a shichen ago, some fellow named Hyuk—Hyuk something—put up huge notices all over the main roads.”

“Why would I want to hear about that Hyuk-whatsisname?”

“Because that Hyuk-whatsisname is Blazing Flame Divine Dragon Jin Taekyung’s right-hand man. I read the notice, and apparently the Two Dragons Pavilion is recruiting people.”

“What? Is that really true?”

“Without a doubt. But the contents of the notice are… strange. Well, there are other people around, so… Ah, never mind. The whole thing is strange.”

“What are you talking about?”

“It’s, well… Never mind. You should go see and hear it for yourself.”

“…Hear it? What do you mean?”

Every piece of news related to the Two Dragons Pavilion had become a hot topic in Henan.

And now, the youngest pavilion master in Murim history—one who had achieved genius and great accomplishments rarely seen in the long history of the martial world—had caused another incident?

“Ah, I can’t miss this!”

Martial artists who already had affiliations, martial artists who had yet to find a place to belong, and even curious commoners all came rushing over.

And when they gathered in one place, they finally saw it.

★I Was a Nameless Foot Soldier, but in the Two Dragons Pavilion, I’m a Murim Hero?!★

The enormous words, written alongside a bizarre emblem.

The people gathered before it like clouds all widened their eyes and cried out in astonishment.

“Th-That!”

“Good heavens!”

How could a phrase be so easy, simple, and revolutionary? The lines written beneath it were just as easy to take in at a glance.

**Recruitment Requirements**

**First:** Someone with the passion to do whatever they set their mind to.

**Second:** Someone with an upright character.

**Third:** Someone who has reached at least the level of injuring others with Sword Energy.

# Recruiting around the clock # No one below Peak need apply # Gender and sect affiliation don’t matter # Age doesn’t matter # Life begins at eighty # Hey, you can do it too.

Every single part of it was outrageous!

The succession of magnificent lines was enough to make blood surge and hearts pound simply by reading them. A passionate cry erupted from the crowd.

“Yeah! I can do it too!”

“You too? Me too!”

“Aaaah! The Two Dragons Pavilion is calling me!”

“Damn it! The level of injuring others with Sword Energy!”

At that exact moment, the hundreds of people who had read the notice let out their own cheers and groans.

Ting-a-ling.

A clear, lively melody rang out from somewhere.

The people parted as if they had agreed beforehand, and a group that seemed to walk on clouds crossed through the crowd.

“What’s that?”

“Isn’t that the band from Honghakru?[^2]”

[^2]: Honghakru, literally “Red Crane Pavilion,” is a renowned entertainment house in Henan.

“Why would a band show up here?”

The sudden appearance of a famous band ranked among the top ten in all of Henan left everyone bewildered.

Then, before the confused crowd, a breathtakingly beautiful woman appeared and smiled sweetly.

“Hongmae? It’s Hongmae![^3]”

[^3]: Hongmae literally means “Red Plum.”

“Waaaaah!”

Hongmae was Honghakru’s most beautiful singer, a singing courtesan famous for her enchanting voice. She bowed her head with graceful poise, then gave a meaningful glance.

The musicians who understood her signal began to play.

Ting-a-ling. Chaarang!

A song melody as clear and lively as could be.

And the moment they heard the first line of the song flowing from the singer’s lips, the martial artists present were bewitched into understanding the truth.

“Join the Murim Alliance’s Two Dragons Pavilion, and my era of success begins~”

“……”

To succeed in life, they absolutely had to join the Two Dragons Pavilion.

* * *

I had always been that way. There was no particular reason. I simply hadn’t liked songs or children all that much.

But today was an exception.

“Heh heh. You little rascals.”

I smiled contentedly as I listened to the sounds slipping through the gap in the window.

Outside, children who looked to be around elementary school age were running around energetically and singing.

“Join the Murim Alliance’s Two Dragons Pavilion, and my era of success begins~!”

“Join the Murim Alliance’s Two Dragons Pavilion, and now more sects are looking for me~!”

“Join the Murim Alliance’s Two Dragons Pavilion, and my life has changed~!”

“A new era, a new hero!”

“The Murim Alliance’s Two Dragons Pavilion!”

The ending was perfect, too.

I lightly clapped my hands in celebration, then noticed Hyuk Mujin staring at me with an absurd expression.

“What is it, you bastard?”

“…I’m just stunned. I’ve never heard of anything like this.”

“What do you think? Innovative, isn’t it?”

Hyuk Mujin nodded with an awkward expression.

“It seems to be highly effective. I just went around checking the area, and it’s complete chaos. You’d think Dark Heaven had invaded.”

“I knew it would work. Heh heh.”

“Especially that song. It’s causing an uproar everywhere. People are even saying that the Captain has poisoned Murim.”

“What does that mean? What poison?”

“They say it’s more addictive than opium.”

“Oh. Ohoho.”

Ah, how satisfying.

What a rewarding situation this was. I might get sued for plagiarism by some cyber university in Seoul, but this was Murim.

*I’m sorry, and thank you. I’ll use the song well.*

And so, the greatest hit of the era—destined to mercilessly violate the eardrums of the primitive Murim bumpkins—was born.

Even now, remembering the expressions on the bandleader’s and singer’s faces when I first taught them the rough melody I had come up with made me shiver with excitement.

*It was the expression of primitive men who had discovered fire.*

I wondered if this was how Prometheus had felt in Greek mythology.

The difference was that instead of donating my organs to the eagle sent by Zeus, I had to deal with the flood of applicants.

“How is the application process? Are you done?”

Hyuk Mujin looked at me as though I had lost my mind.

“Are you serious?”

“I suppose there are more than you expected.”

“More? It’s insane. Completely insane. There are so many that I’m starting to suspect Dark Heaven may have sent in applications too.”

Hmm. It seemed the song was even more potent than I had imagined.

I had added the requirement of being a Peak master because I was worried something like this might happen, but the world was vast and apparently full of masters.

“Then let’s do this. First…”

I was just about to open my mouth after thinking for a moment when—

Boom!

The door shattered, and someone appeared.

“Join the Murim Alliance’s Two Dragons Pavilion. My era of success begins.”

The most ominous song in the world.

A chilling expression.

I froze completely when I met those glowing red eyes. Fire King Jeok Cheongang continued, spitting out each word.

“Because of this damn song, this old man almost suffered qi deviation.”

“…Welcome.”

[^1]: Gukbap is rice served in a bowl of hot soup, a common Korean meal.
## Chapter artifact 541

# Chapter 541

Henan was a land with a long and storied history.

It was home to sprawling thousand-year-old capitals such as Kaifeng and Luoyang, cities that had served as the seats of numerous dynasties. It also offered breathtaking natural scenery and all sorts of famous landmarks, including four great mountains.

As a result, people never stopped visiting throughout the year. Naturally, there were plenty of inns, pleasure houses, and other places for entertainment and lodging.

But the old innkeeper, whose family had run the same inn for three generations, could confidently say that the street had never once boiled over like this.

*What in the world…?*

The old innkeeper stared around in bewilderment.

What he saw was a truly enormous crowd—so large that it could only be described as a sea of people.

“Hey, wait a minute! Don’t try to cut in line!”

“Good grief, who keeps shoving me?”

“You little pup. You’ve been giving me insolent looks for a while now. Do I have to show you a coffin before you come to your senses?”

“What did you say? I was willing to let it go, but this lowly wandering martial artist is—”

“Heh heh. Everyone’s certainly full of energy. It’s a pleasant sight.”

“Pleasant? It’s been so noisy that I can hardly stand it.”

A wandering martial artist who looked like a wild wolf and a man who appeared to be the scion of a prestigious family glared sharply at each other.

The sight made a middle-aged man with half-white hair burst into hearty laughter, while a beautiful woman whose age was impossible to guess clicked her tongue.

And that was not all. Countless people stood farther away, watching them and whispering among themselves.

*What on earth is going on here?*

In the middle of the chaos, just as the innkeeper felt his soul halfway leaving his body, a voice reached his ears.

“There’s no need to worry so much.”

“Pardon?”

“Not over there. This way.”

The innkeeper turned around in surprise and saw a person sitting at a table, leisurely sipping from a wine cup.

Unlike everyone else, who had been standing in a long line, this old man had claimed a seat and seemed completely at ease.

“They all know better, so there won’t be any serious trouble.”

He was small in stature, with a wild white beard and a face flushed red with drink.

For a moment, the innkeeper wondered if he might be a martial artist. But at first glance, he was nothing more than an utterly ordinary drunken old man.

The innkeeper discreetly looked him over, then whispered in a lowered voice.

“W-What in the world is going on?”

“They’re all people who want to begin their era of success. You must have heard that song, too. ‘Join the Murim Alliance’s Two Dragons Pavilion, and—’”

The old man began humming a lively tune.

The innkeeper’s shoulders instinctively began to sway. Then his eyes widened.

“Ah. Are you talking about that… Two Dragons Pavilion?”

“You got it in one. The young Pavilion Master of that Two Dragons Pavilion is staying right here.”

“Good heavens.”

The innkeeper let out a short gasp.

He had known that the person staying in the detached building was a young knight-errant famous throughout the martial world. But he had never imagined that he was the Pavilion Master of the Two Dragons Pavilion everyone was talking about.

“So that’s why so many martial artists have come here. But even so, I never imagined there would be this many…”

“Heh heh. Isn’t it a fine opportunity? It’s rare to find a place that doesn’t care about your background, gender, or age.”

“That’s true. I heard even an eighty-year-old can apply.”

The old man quietly answered.

“As it happens, that’s exactly what I intend to do.”

“Hahaha! You certainly know how to make a joke.”

“Does that sound like a joke?”

“Pardon?”

“I asked whether that sounded like a joke.”

The laughter stopped at once.

The innkeeper stared at the old man with trembling eyes.

“Th-Then, Old Sir… I mean, Your Excellency is applying as well?”

“Isn’t that obvious?”

The old man wiped his beard, drenched in wine, with his sleeve.

At the same time, his robe shifted slightly, revealing a worn scabbard beneath it.

“I am a martial artist as well. Just like them. And unlike you.”

“Gasp.”

“There’s no need to be so frightened. This old man doesn’t lay a hand on commoners.”

After thinking for a moment, the old man added in a low voice.

“Most of the time, anyway.”

“……!”

Not a trace of drunkenness remained in his gentle voice.

For an instant, his eyes flashed with the ferocity of a wild beast.

The innkeeper felt a chill run through him and unconsciously took a step backward.

That was when he heard someone coming down the stairs.

Thud. Thud.

The sound of approaching footsteps.

The old man’s eyes flashed.

“Is it about to begin?”

The old man was not the only one who had reached that conclusion.

The dozens of Peak masters waiting in the long line and the spectators who seemed to number ten times as many all fell silent.

In the silence that descended in an instant, someone appeared.

“How many people have come— Oh my, that startled me.”

A young man jumped in surprise.

When everyone realized that it was Hyuk Mujin, a trace of disappointment passed over their faces.

But the Peak masters, who had sensed his aura long before he appeared, merely muttered calmly.

“He’s not the Blazing Flame Divine Dragon.”

“He sent a messenger down in his place. Is he already throwing his weight around?”

“He’s quite impressive for a messenger. With that kind of aura at his age, he’s better than most second-generation Disciples from prestigious sects.”

“I agree. And if it’s the Blazing Flame Divine Dragon, I suppose that’s possible.”

Voices drifted in from every direction.

Hyuk Mujin looked sourly at the enormous crowd murmuring around him and cleared his throat.

“Ahem. I was ordered by the Captain—I mean, the Pavilion Master—to begin the interviews. Therefore, I will call each person by name from this point onward. Please follow me one at a time in the designated order.”

Reaching the Peak realm meant being recognized as a master anywhere in Murim.

The Peak masters all took pride in their abilities. They clearly disliked being told they would have to wait again, but none of them complained beyond that.

A thirsty man had to dig his own well. Since they had come here, this was something they had to endure.

“I understand perfectly well, so stop spouting nonsense and call the names already.”

Hyuk Mujin’s eyes widened at the rough-looking middle-aged wandering martial artist’s words.

“Oh. It’s true.”

“What is?”

“Ah, it’s nothing. The Pavilion Master told me to reject anyone who uses informal speech and acts rudely the first time they meet someone, no exceptions. I didn’t expect to find someone so quickly.”

“……What?”

“Let’s see. You’re Great Hero No Guisan, the Black Blood Saber, correct? You may go home now.”

The middle-aged wandering martial artist, the Black Blood Saber, blinked at him in silence.

Then he roared.

“What kind of bullshit rule is that?”

Hyuk Mujin pulled a bamboo slip bearing the Black Blood Saber’s personal details from the purse at his waist and nodded.

“It’s right here. That kind of rule.”

“I waited for an entire shichen!”

“Oh dear. That’s unfortunate.”

“You insolent little bastard! You’re relying on your master and behaving this arrogantly. Do you really think you’ll be safe after this?”

“I think I’ll probably be fine.”

“You little—!”

“If you keep this up, our Pavilion Master will come down himself and say, ‘You bastard!’”

What kind of person was this?

The Black Blood Saber and everyone watching the spectacle stood with their mouths hanging open.

The Black Blood Saber was a renowned powerhouse even among the rough-and-tumble world of wandering martial artists.

People said that if not for his foul temper, he could become the Sect Leader of a school that very day and build it into a mid-level sect.

Yet Hyuk Mujin did not even blink before the aura he released.

“You’re rejected. Off you go.”

But for Hyuk Mujin, who had followed Jin Taekyung around and experienced every kind of hell, this was only natural.

Even the foul-tempered Black Blood Saber was left speechless by Hyuk Mujin’s composure.

That was when—

“Ha! Hahaha!”

Rumble, rumble!

A thunderous laugh erupted from somewhere.

The air seemed to burst, and the ground trembled in tiny, violent shudders.

The Peak masters who sensed the owner of the overwhelming aura pressing down on the surroundings went rigid.

*What incredible internal energy…!*

*One level above me. No—two levels.*

*What in the world…?*

Every horrified gaze turned toward the old man who, only moments earlier, had been leisurely sipping his wine.

He was slowly rising from his seat.

“Don’t make such a commotion. Don’t you feel sorry for the innkeeper?”

The old man smiled gently at the innkeeper, who was lying facedown and trembling.

As everyone stared at him, a cry like a scream burst from somewhere in the crowd.

“T-The Old Man Ilyang!”

Old Man Ilyang.

Those three words were enough.

He was a master between the orthodox and unorthodox paths who had once dominated an entire era. His sobriquet belonged to a monster who had burned countless opponents to death with his mighty Scorching Yang Qi.

The sudden appearance of such a Supreme Peak master froze the entire gathering in an instant.

*Is that truly Old Man Ilyang?*

*Th-That old monster… What is he doing here?*

No one present could compare to Old Man Ilyang.

No—given the difference between Peak and Supreme Peak, it was questionable whether they could bring him down even if they joined forces.

It was only one wall.

But the gap between Peak and Supreme Peak was that vast and distant.

Step. Step.

Old Man Ilyang leisurely walked through the silence, then looked at Hyuk Mujin and smiled.

“Go and tell him that this old man wishes to meet him.”

“……!”

A second quiet shock swept through the surroundings.

It was Old Man Ilyang, of all people.

It was astonishing enough that such an unrestrained Supreme Peak master would seek to join the Two Dragons Pavilion under someone who was barely more than a boy.

Yet he was behaving with such courtesy.

“U-Understood. Please wait a moment.”

Hyuk Mujin turned away with a flustered answer.

He did not see the ominous heat burning in Old Man Ilyang’s eyes.

*The Fire Gate Clan. The Fire Gate Clan, huh? Heh heh. At long last, an opportunity has come even to this old man.*

Blazing Flame Divine Dragon Jin Taekyung?

The truth behind the rumors surrounding him was irrelevant.

He was still nothing more than a young brat barely past twenty. Old Man Ilyang had no intention whatsoever of respectfully serving such a fledgling as his superior at his age.

However…

*The Fire Gate Clan’s divine technique, passed down to only one person in each generation. That alone will become mine, no matter what.*

He had spent his entire life pursuing strength, yet he had never reached the pinnacle of Scorching Yang Qi.

But if he obtained the Fire Gate Clan’s martial arts, it would be possible.

He could even claim the title of the greatest under heaven.

*According to reliable rumors, Fire King Jeok Cheongang has no intention of joining the Two Dragons Pavilion. Then all that remains is his young Disciple and a few other riffraff.*

The moment the Two Dragons Pavilion received a mission and left Henan would be his chance.

Dark Heaven? The Murim Alliance?

What did it matter what became of the martial world’s fate?

The corner of his mouth, covered in age spots, twitched.

“Heh heh. Hahaha.”

Before Old Man Ilyang’s eyes, the five characters meaning *greatest under heaven* were already shimmering.

* * *

Eighty-five years old.

His name was Won Cheol.

His sobriquet was Old Man Ilyang.

His martial arts realm was Supreme Peak.

It was practically a perfect profile. There was not a single thing to criticize.

But the special judge he had suddenly found himself facing had a different opinion.

“Those eyes are exactly the kind that belong to a bastard who’d stab you in the back the second an opportunity arose.”

“Pardon?”

There was no need to ask what he meant.

Jeok Cheongang had already closed the distance and was smashing his fist into Old Man Ilyang’s mouth.

Whoosh!

A surge of Extreme Yang energy that would turn everything in its path to ash.

Old Man Ilyang sucked in a sharp breath and hurriedly crossed both arms in front of himself, but the difference in strength was obvious.

*That’s bad.*

Even Scorching Yang Qi had different levels.

If Old Man Ilyang’s qi was an ordinary flame, the qi possessed by Fire King Jeok Cheongang was lava.

The vast difference in power revealed itself in an instant.

Crunch. Wham!

As the sound of bones being shattered rang out, Old Man Ilyang’s eyes went limp.

Watching the scene, I shouted with genuine concern.

“No! The ace—!”

But once Jeok Cheongang’s fist began spitting fire, it did not stop.

Wham! Wham! Wham-wham-wham!

Arms, legs, stomach, back, face.

As though showing off his regained youth, Jeok Cheongang’s powerful strikes, packed with vigorous qi, pounded every part of Old Man Ilyang’s body.

Each time, tangible Scorching Yang Qi wrapped around them.

*Wow. I get to see a fire pit right here.*

Was this audition genre hip-hop?

One Sun—no, Old Man Ilyang, who had not even received a necklace, lost consciousness without managing a single proper counterattack.

Thud.

Jeok Cheongang stood quietly over Old Man Ilyang, who had collapsed like crumbling ash.

Then he suddenly muttered.

“Now I remember, you bastard. You’re that son of a bitch who said he was after our sect’s martial arts.”

“……It’s a relief that there was at least a reason. I thought you’d gone mad, Old Master.”

“Better late than never. I can’t stand the sight of him, so get him out of here.”

Not long after Old Man Ilyang’s corpse—or rather, his body—was carried away, the area outside grew noisy.

I glanced out the window.

Applicants were fleeing in terror, even using their movement techniques to get away.

“……Oh, for fuck’s sake.”

How much effort had gone into arranging this?

The audition was completely fucked. Seriously.

Jeok Cheongang answered my resentful stare bluntly.

“What do you want me to do?”

“You could’ve gone a little easier on him. Wanting to get his hands on some martial arts isn’t a capital crime. He hadn’t actually done anything yet. You could’ve just rejected him quietly.”

“Tsk, tsk. What an innocent fool. People like that always cause trouble eventually. You have to stamp out a spark before it becomes a fire.”

“……Don’t people usually say you should uproot weeds?”

“Weeds can be left alone, but a spark can burn down a mountain.”

I mean, what was he, the chairman of a forest conservation society?

I was muttering inwardly in disbelief when Jeok Cheongang continued.

“And…”

“What now?”

Jeok Cheongang jerked his chin toward the window.

“When someone leaves, someone else comes.”

“Huh?”
## Chapter artifact 542

# Chapter 542

A person’s walk was one of the important indicators of their personality.

For martial artists in particular, their footsteps revealed far more than most people would expect.

Someone who relied on crude strength when using martial arts would have a heavy, rough gait.

On the other hand, those who had learned graceful martial arts—or specialized in certain fields, such as assassination—could move so stealthily and lightly that their footsteps were barely audible.

In that sense, it would not have been an exaggeration to say that the footsteps of whoever was coming up the stairs were not merely announcing his presence. They were practically screaming it.

Thud. Thud. Thud.

*Now that’s some sound.*

It was the kind of heavy noise that would make an ordinary person’s heart sink just from hearing it.

With every step, the solidly built staircase creaked, and faint vibrations traveled through the floor.

Jeok Cheongang, who had somehow already taken out the gourd hanging at his side and was sipping from it, spoke with a grave expression.

“Dark Heaven. After everything else they’ve done, they’re now turning people into monsters. What kind of trick did they use?”

“Huh?”

For a moment, I had no idea what he was talking about.

Then I understood and waved my hand.

“Sorry to interrupt, but the guy coming up isn’t from Dark Heaven.”

“Hm. Even so, he is not an opponent worth worrying about. Open the door, and the moment he enters, knock him flat. If we throw him to the Murim Alliance, something useful will come out of him.”

“……He’s not from Dark Heaven. And you already smashed the door, Old Master. What door are you talking about?”

“What?”

Jeok Cheongang’s eyes widened like lanterns as he splattered spit while speaking.

“You mean to say that the fellow coming up is a pure-blooded human?”

“Amazingly, he’s all-natural.”

“Hah. Some things really do have to be seen after living a long life. But the aura I sense from him doesn’t seem particularly pure.”

Hyuk Mujin returned after sending the emergency patient downstairs. He wiped his palm, still drenched in Old Man Ilyang’s blood, against his trouser leg before answering.

“Wow, as expected of Great Hero Jeok. You recognized a practitioner of demonic, heterodox arts at a glance.”

“Demonic, heterodox arts?”

“Yes. He’s the Young Sect Leader of the Black Dragon Demon Gate, along with his subordinate.”

The loud footsteps had drowned it out, but there had been two presences from the beginning.

At last, two people appeared beyond the doorway that Jeok Cheongang had blown wide open.

“This junior of Murim, Sama Pyo, pays his respects to Great Hero Jeok Cheongang, the Fire King.”

He was a tall, handsome man. The moment I saw him, my mouth felt gritty, as though I were chewing sand.

That was because three words suddenly flashed through my mind.

*Former fiancé.*

Whether he knew what I was thinking or not, Sama Pyo clasped his hands toward Jeok Cheongang, then poked the lump standing blankly beside him.

“What are you doing? Hurry up and pay your respects.”

Tiger Giant Child Taishan, whose epithet and name suited each other perfectly, bent deeply at the waist.

“Nice to meet. Taishan saw Fire King.”

“……”

What a novel greeting.

I took a quick look at Jeok Cheongang’s expression. He looked like he wanted to show Taishan Yama rather than the Fire King.

Perhaps noticing the mood, Sama Pyo quickly added an explanation.

“As you may have guessed, his vocabulary is limited. This is the best he can do.”

“……In that case, I suppose it can’t be helped.”

Jeok Cheongang muttered with a displeased expression.

“I’ve seen all sorts of strange fellows in my life. Fine. This old man has seen you, too.”

“Heh heh.”

Taishan smiled innocently, then abruptly raised both thumbs.

“Fire King. Strong. Taishan. Likes strong people. Nice to meet you.”

“W-Well, yes. This old man is pleased to meet you as well.”

“But Taishan. Hungry.”

“W-What?”

“Want to eat that. If Fire King allows, Taishan grateful.”

His eyes were already fixed over our shoulders, filled with gluttonous anticipation.

Jeok Cheongang realized there were refreshments laid out on the table and nodded without thinking.

“Th-Then go ahead.”

“Hooray! Refreshments! Taishan will eat well!”

Crash! Crunch!

The innkeeper was going to cry tears of blood.

A massive body that could not possibly belong to an ordinary person charged forward, smashing through what remained of the door.

Taishan swept everything on the table into his arms as though he had been waiting for permission. Jeok Cheongang stared blankly at him and muttered.

“Have I lived too long?”

Even Jeok Cheongang seemed incapable of avoiding surprise.

Then again, until now he had only dealt with people who trembled and groveled whenever they heard the words *Fire King*. His reaction was understandable.

Aside from Cheongpung, this might have been the first genuinely formidable opponent to appear.

*Well, putting that aside.*

I scratched the back of my head and looked Sama Pyo up and down.

“So. What brings you here?”

“I have important business. If possible, I would like to go inside and discuss it.”

“No, that’s exactly why it isn’t possible.”

Sama Pyo shrugged.

“I asked out of courtesy, but you really aren’t ordinary. Do you also harbor ill feelings toward the demonic, heterodox path?”

“Rather than ill feelings……”

Damn it. Now that he had put it that way, I had no answer.

I had only met him once, but my first impression of him had not been particularly bad. Nor was I some hardcore zealot who shouted about eradicating the heterodox path and glorifying the orthodox faction whenever I got the chance.

The same was largely true of Jeok Cheongang.

“What are you two standing there doing? Did you fall for each other?”

With even Jeok Cheongang putting it that way, there was no particular reason to refuse. After finishing my deliberation, I jerked my chin toward Sama Pyo.

“Damn it. Come in, then.”

“Thank you. Thank you, Great Hero Jeok.”

As Sama Pyo entered with a polite greeting, Jeok Cheongang nodded.

“That young brat has decent manners. Or did he inherit that sly bloodline?”

Sama Pyo paused for a moment, then smiled faintly.

“Probably the latter. By the way, you remember my father.”

“I had forgotten him until I saw your face. You look exactly like the Black Night King did in his youth.”

Black Night King Sima Gong.

He was Sama Pyo’s father, a self-made man who had built the Black Dragon Demon Gate into what it was today.

Judging from his epithet, it would have been easy to assume that he was one of the Ten Kings. But according to the information I had learned through Gung Gibang, he had no connection to the Ten Kings whatsoever.

*Just like the Green Forest Battle King, the Green Forest Alliance Leader, and the Escort King of the Yongbong Escort Bureau.*

They, too, were Supreme Peak masters with martial prowess beyond ordinary reach. But it would have been a stretch to recognize them as part of the legend of the Ten Kings.

Black Night King Sima Gong, one of the greatest masters in the unorthodox martial world and the Sect Leader of the Black Dragon Demon Gate, had apparently received the title in much the same way.

“But still……”

Jeok Cheongang stared intently at Sama Pyo, then suddenly furrowed his brow.

“I had no idea the Black Night King had such a young son.”

“I have seven older brothers and nine older sisters. I am the youngest.”

“Hah. The Virility Saber King would cry himself to sleep if he heard that. So you’re the Young Sect Leader.”

Sama Pyo’s eyes widened slightly.

“That is correct, but how did you—”

“Isn’t it obvious?”

Jeok Cheongang snorted and continued.

“Given the Black Night King’s personality, that is exactly what he would do. If your talent was sufficient, he wouldn’t care even if it meant burying all his other children alive as sacrifices.”

“……”

“He doesn’t seem to have changed much from the man I remember. I could never tell what was going on inside his head. He was as sly as a fox and as cunning as a viper.”

*Look at him, casually throwing a parent insult right to his face. My heart almost swelled with awe.*

There was an underlying meaning that acknowledged Sama Pyo’s talent, but a parent insult was still a parent insult. Before the dutiful son could start something over the insult to his father, I cut in.

“So what brings you here?”

“……Hm. Well.”

Sama Pyo’s expression became impossible to read. He reached inside his robe and pulled out something.

It was paper, an expensive commodity in Murim. And the words written at the very top immediately caught my eye.

> ★**I Was a Nameless Foot Soldier, but in the Two Dragons Pavilion, I’m a Murim Hero?!**★

I stared down at the paper on the table and rubbed my chin.

“This looks awfully familiar.”

Sama Pyo gave a quiet laugh.

“It couldn’t be otherwise.”

“I don’t know who came up with it, but it’s genius.”

“And groundbreaking.”

Tap.

Sama Pyo’s long finger pointed to one part of the paper.

It was the recruitment requirements Hyuk Mujin had scribbled down in terrible handwriting.

Among the various items written below, his finger accurately indicated one specific line.

> \# Gender and sect affiliation don’t matter \#

His gentle voice continued.

“I particularly like this part.”

“So?”

“I wish to apply. To the Two Dragons Pavilion.”

I had more or less expected it, but hearing him say it directly still left me with complicated feelings.

After a moment’s thought, I clicked my tongue.

“Why?”

“The moment I heard the song, I had a feeling. This is exactly the place I’ve been looking for.”

“Yeah. Bullshit.”

It was not even funny.

The lyrics about the era of success beginning, more sects seeking you out, and your life changing simply did not apply to Sama Pyo.

The Black Dragon Demon Gate was one of the three strongest sects in the unorthodox martial world.

Even if Sama Pyo had not been the Young Sect Leader, being born into the Black Night King’s family practically guaranteed him a certain level of wealth and prosperity.

*And someone like that wants to join the Two Dragons Pavilion?*

Even if the orthodox faction’s diehards held up picket signs and protested, Sama Pyo was more than capable of securing a position within the Murim Alliance.

I folded my arms and stared at him.

“If you’re joking, it isn’t funny.”

“Fortunately, I’m being entirely serious.”

“Enough bullshit. What’s the real reason?”

“You say I need to provide a reason, but that was not written on the notice.”

“Get lost. I won’t walk you out.”

Sama Pyo shrugged as though he had no choice.

“I thought that if I joined the Two Dragons Pavilion, I might be able to shed the label of belonging to the demonic, heterodox path.”

“You don’t exactly seem eager to shed it.”

“Do I really seem that way?”

“It’s a fact that I don’t trust you.”

“Then I suppose it can’t be helped. In that case, I’ll take this opportunity to speak frankly.”

“Go ahead. Unless you want to get the shit beaten out of you.”

Sama Pyo let out a quiet laugh, then his expression abruptly hardened.

A low voice slipped from between his perfectly smooth lips and pierced my ears.

“I intend to use you for my own benefit. Depending on the circumstances, you will become a useful card to me in one way or another.”

A heavy silence descended.

Even Taishan, who had been chewing noisily without pause, stopped moving. Hyuk Mujin stared back and forth between Sama Pyo and me with eyes as wide as lanterns.

Then a voice broke the silence.

“What an interesting fellow.”

The speaker was Jeok Cheongang.

He stared at Sama Pyo with an expression that made it impossible to tell whether he was laughing or angry, then abruptly asked me a question.

“What do you think?”

I considered it for a moment before slowly parting my lips.

“He’s certainly intense. He doesn’t seem like someone who’s only been through one or two interviews.”

“Will you accept him?”

“Hard to say.”

Sama Pyo, the Black Dragon Saber. It was difficult to judge which of his words were jokes and which were sincere.

But one thing was certain.

*He’s an interesting fellow.*

Tap. Tap.

The only sound echoing through the silence was the tapping of fingers against the table.

After organizing my thoughts for a short while, I looked straight at Sama Pyo.

“Let’s establish one thing before we go any further.”

“By all means.”

“If you try anything funny……”

Before I could finish, Sama Pyo answered.

“Summary execution. Yes, I’ll bear that in mind.”

“Huh. You don’t mince words.”

“It is only natural. Then are we finished here?”

“You haven’t been accepted yet. I’m only keeping you under consideration for now. For today, go.”

“Very well.”

What in the world was this man after?

As my curiosity continued to grow, I watched Sama Pyo and Taishan preparing to leave. Then I realized one important thing I had forgotten.

“And one more thing.”

“……?”

“You’re paying for that guy’s food.”

“……!”
## Chapter artifact 543

# Chapter 543

Thud. Thud.

At the thunderous footsteps that shook the earth beneath them, pedestrians moved aside and cleared a path.

And Black Dragon Saber Sama Pyo knew that the wary looks they were receiving were not because of Taishan walking beside him.

*It seems the rumors about us have spread quite a bit.*

That was only natural. It would have been stranger if they had not spread.

A yellowed, grimy knot protruded from the waist of a beggar dozing against a wall in the alley beside them. The palm of a stallkeeper swatting at flies bore faint calluses.

*The Beggars’ Sect. The Lower District Sect.*

That was only what he could see at a glance.

No matter where they went in Henan, countless eyes were watching them. There was no doubt that today’s movements would be reported to various people before even half a day had passed.

*Not that I intended to hide them.*

Trying to conceal himself would only raise greater suspicion. Sama Pyo had no intention of ruining things through half-baked caution.

*—My lord.*

Taishan’s cautious Sound Transmission pierced his ears. Without revealing anything, Sama Pyo pointed toward a small noodle shop tucked away in one corner.

“Thin noodles sound good today. How about a bowl before we go?”

“Hm?”

“You must have a full belly. If you don’t want any, say so.”

“No! Taishan likes noodles!”

“You should have said so from the beginning. Excuse me. Ten bowls of thin noodles—no, make that twenty.”

The middle-aged woman running the shop looked as though she doubted her ears.

“……How many bowls did you say?”

Sama Pyo had chosen the noodle shop for a simple reason.

Perhaps because it was in an inconvenient location, there were no other customers, allowing them to exchange Sound Transmissions with their backs turned to everyone else.

It also helped that the owner appeared to be an ordinary commoner with no connection to the Murim.

“Twenty bowls. As you can see, I have a hungry ghost with me.”

“Y-Yes!”

It must have been an unexpected windfall for her. While the woman’s eyes lit up and her hands moved busily, Sama Pyo’s lips barely moved.

*—You seemed to have something to say.*

The small chair creaked beneath the massive weight it supported. Taishan, precariously balanced on it, answered.

*—My lord. Taishan. Worried.*

*—About what?*

*—Did not obey Sect Leader’s orders. Taishan. Worried about my lord.*

A bitter smile formed at the corners of Sama Pyo’s mouth.

*—I wondered if that might be the reason. So it was because of that person after all.*

*—Disobeying bad. Sect Leader angry. My lord in danger.*

*—Yes. He is more than capable of that.*

Sama Pyo looked down at the chopsticks neatly arranged on the table.

His father, Black Night King Sima Gong, came to mind. He was a man utterly devoid of paternal affection.

*He probably thinks of his children the way he thinks of these chopsticks.*

*Replace them when they fall to the ground. Set them aside when they no longer please him.*

His seven older brothers and nine older sisters had all been discarded in the same way. Sama Pyo was the final—and best-crafted—chopstick the Sect Leader of the Black Dragon Demon Gate had chosen.

*Though I have no idea when even I might be replaced.*

His father was already well past eighty, yet he still possessed a vigorous appetite and an equally vigorous libido.

Three wives and four concubines had not been enough for him. He had taken more than ten concubines, leaving Sama Pyo with countless blood relatives both older and younger than himself.

And yet—

*—Don’t worry.*

*—Hm?*

Sama Pyo swallowed a mouthful of the lukewarm water the owner had brought him.

*—He is heartless. That is precisely why he cannot easily cast me aside.*

Black Night King Sima Gong was certainly a cruel man. That was why he could discard any notion of parental love and look at reality with such cold clarity.

By the same logic, there was no other successor who could replace Sama Pyo, whose martial talent surpassed even Sima Gong’s in his younger days and whose calculating mind ran deep.

And—

*—There will be no punishment. The route has merely changed; this still leads toward the destination my father wants.*

*—My lord. Taishan does not understand. Taishan is stupid.*

Sama Pyo smiled faintly at Taishan, who only tilted his head in confusion.

*—You don’t need to understand. Just stay by my side. Do you understand?*

*—Taishan listens to my lord. Taishan is good.*

Just then, Taishan nodded vigorously, and the owner began setting bowls piled high with thin noodles on the table.

“Careful, they’re hot. Take it slow—”

“Wow! Taishan! Thank you for the food!”

“Oh my goodness!”

The owner stared in shock as Taishan lifted an entire bowl of steaming noodles and gulped them down.

Sama Pyo let out a quiet laugh at the sight.

Then his face suddenly stiffened.

“Hmm.”

Taishan, who had been working his chopsticks without pause, raised his head.

“My lord. What is it?”

“……”

“My lord?”

Sama Pyo continued staring at something in silence before murmuring under his breath.

“No. It’s nothing. I must have seen wrong.”

But Sama Pyo knew that the person who had passed by in a fleeting glimpse was not a mistake.

And he knew what that meant.

“……Perhaps I should have just obeyed the orders without complaint.”

“Hm? My lord. What did you say?”

Sama Pyo answered with a sigh instead. By then, Taishan was holding the final bowl.

“You shameless glutton. Finish stuffing your face.”

“Wow! Taishan will give his life for my lord!”

* * *

“Here you go.”

The voice was clear and lovely, more beautiful than a Young Chang piano.[^1] Two bamboo slips were held out toward me.

*What is going on?*

Less than half an hour had passed since the two uninvited guests from the Black Dragon Demon Gate had left and Jeok Cheongang had gone to the latrine.

The unexpected guest who had arrived was not merely sudden. She was downright disconcerting.

I blinked at her wordlessly, then barely managed to squeeze out a voice.

“W-What are these?”

“Applications.”

Ju Hwaran answered with an expression that seemed to ask why I was questioning the obvious, then added,

“One for me and one for Captain Song.”

Song Ilseom, standing behind her, muttered under his breath.

“I never agreed to this.”

“I hired you, didn’t I? If you’re my escort, of course you have to come with me.”

“That sort of situation wasn’t included in the contract. It’s a breach of contract. If I join the Murim Alliance, I’ll need hazard pay……”

“I’ll pay you double.”

“Then that’s a different story.”

Perhaps it was because she had wrung so much money out of the Zhongnan Sect, but Ju Hwaran was putting on a brisk young-and-rich flex.

Of course, watching her made me feel as stifled as if I had stepped into a greenhouse in midsummer.

“So. Really?”

“Yes. Really.”

Ju Hwaran nodded without hesitation and stared at me with clear eyes.

“I want to join the Two Dragons Pavilion.”

“……!”

I had more or less expected it, but hearing it directly from Ju Hwaran still left a gritty taste in my mouth. After thinking for a moment, I opened my lips.

“I have no intention of accepting you simply because we have a connection.”

“If I’d planned to rely on our connection from the start, I would’ve come without an application, wouldn’t I?”

A faint smile crossed Ju Hwaran’s face, and I sighed inwardly.

“It will be dangerous. Very dangerous.”

“I know. The Two Dragons Pavilion is directly under the Alliance Leader’s Office, and unlike the other pavilions, it cannot even command its own squads or battalions. It will probably function more like a special operations detachment.”

That was exactly right.

Mae Jonghak wanted to use Cheongpung and me, both considerable assets even within the Murim Alliance, as a small special operations detachment. That was also why most of the Alliance’s leadership had nodded along with the idea.

“Young Lady Ju, if you know that, then why—”

“Great Hero Jin.”

Before I could finish, Ju Hwaran cut in.

“Did you say that to the other applicants as well?”

“What?”

“‘It’s dangerous. Why apply when you know that?’”

Her quiet voice continued.

“That’s strange. You put up a notice because you needed people, yet you’re discouraging them like this.”

“That’s……”

As I hesitated, Ju Hwaran let out a quiet laugh.

“You have nothing to say, do you?”

She had hit the nail on the head. I scratched the back of my head, then nodded reluctantly.

“To be honest, yes. I suppose I don’t.”

“I came here as a martial artist in my own right, so I hope you will look at me as I am.”

“As you are……”

“You may think I’m far from enough for you, Great Hero Jin, but I am also a swordswoman who has reached the Peak realm.”

“Since we’re being honest, if we’re laying it all out, you are indeed lacking. Song Ilseom might be a different story.”

Hyuk Mujin, who had been watching the situation with bated breath, gave me a subtle poke in the ribs.

But that was only unnecessary worry on his part. As proof, Ju Hwaran’s gaze did not waver even at my blunt words.

“Even compared with the other applicants?”

“I can’t guarantee it, but you probably are.”

“What about experience?”

“Experience?”

“I began going out on escort runs with my father when I was twelve. I don’t think I fall short of any old hand in the martial world when it comes to experience or knowledge of the land.”

That was true. Ju Hwaran had once been the successor to the Yongbong Escort Bureau, one of the most renowned escort bureaus in the world.

For the past several years, she had even led the bureau herself in place of her father, who had collapsed from qi deviation.

*The experience she gained from that can’t be dismissed.*

Escort bureaus were groups that roamed every corner of the land. To complete their contracts within the appointed time, they used every means and method available to them. As a result, they possessed knowledge of the roads and information found throughout the world.

Moreover, during the Great Faction War, Ju Hwaran’s grandfather, the Escort King, had successfully completed a journey of ten thousand li while evading the Demonic Cult’s countless eyes.

“Great Hero Jin.”

Her powerful voice pierced my ears.

“I have no intention of becoming a burden. But please think about this coldly as well. Setting aside every connection we’ve had until now, are Captain Song and I truly people the Two Dragons Pavilion has no need for?”

“……!”

“I’m fully prepared for what this entails. Even if you reject me, I’ll accept it.”

I slowly closed my eyes.

Ju Hwaran was right. This was something I had to consider coldly.

The person waiting for my answer was not the woman I had once walked beside at night through a garden where the flowers had only just begun to bloom.

*Dagger Hidden Flower Ju Hwaran.*

She was a martial artist whose abilities were enough to earn recognition as one of the Ten Dragons and Phoenixes, as well as the Young Bureau Head of the Yongbong Escort Bureau.

On top of that, she possessed various abilities that would be needed for the Two Dragons Pavilion’s future missions, which were effectively bound to be those of a special operations detachment.

*So why?*

Why did I hate admitting that fact?

Why did I feel like insisting on stopping her, even if I had to be unreasonable?

“Um, Captain.”

At the voice piercing my ears, I opened my eyes. Hyuk Mujin watched my reaction nervously before continuing.

“I think you’ve forgotten one thing.”

“What?”

“All the other applicants have run away. Every last one of them. It’ll probably be the same tomorrow and the day after.”

“I know, you punk. Old Man Ilyang was carried away half-paralyzed. So what?”

“No, I mean, that’s all I wanted to say.”

Hyuk Mujin flinched and subtly turned his head away.

But the meaning behind his words had come through loud and clear.

“Whew.”

I sighed and looked straight at Ju Hwaran.

“Before I answer, there’s one thing you should know, Young Lady Ju.”

How was I supposed to bring this up? As I hesitated, Ju Hwaran gave me a faint smile.

“It doesn’t matter.”

“What?”

“I saw it on my way here. With someone that large beside you, it would be strange if you didn’t attract attention. From the things people were whispering, I was able to roughly figure out where you were coming from.”

Ju Hwaran continued in a calm voice.

“But why would that be a problem?”

“……!”

“I think I’ve given you plenty of time to think. May I hear your answer now?”

I stared at Ju Hwaran. It felt as though the tangled mess in my head had been neatly sorted out.

No. Perhaps it was not completely sorted out yet.

But at least for now, I knew what answer I had to give.

“Yes. That’s fine.”

A radiant smile spread across Ju Hwaran’s face.

[^1]: Young Chang is a Korean piano manufacturer.
## Chapter artifact 544

# Chapter 544

Ju Hwaran had left.

Beyond the window, her slender yet dignified back grew more distant, with Song Ilseom following behind her like a shadow.

“She’s impressive, Young Lady Ju.”

At Hyuk Mujin’s voice from behind me, I quietly nodded.

*She was like that back then, too.*

I suddenly remembered the day I first met Ju Hwaran.

Even in that desperate situation, surrounded by several hundred enemies, she had refused to retreat. That look in her eyes—

*Perhaps she’s far more of a martial artist than I realized.*

“It’s a shame, too.”

“Yes. She has a lot weighing on her shoulders. Her father still has trouble moving, and…”

“That’s not what I meant.”

“Hm?”

I turned around and saw Hyuk Mujin looking at me with a pitying expression.

“If her goal was to earn merit, she had plenty of other options. Why do you think she came all the way here?”

*The reason, huh?*

After thinking it over, I sucked in a startled breath.

“Wait. No way?”

“Yes. Exactly that no way.”

“Because she thought she could earn even greater merit?”

“……That’s enough. This is too damn filthy to work with.”

As I wondered whether to smack him or not, a voice came to Hyuk Mujin’s rescue.

“Ahh, what a relief.”

Jeok Cheongang appeared after spending half an hour in the latrine.

Apparently celebrating a smooth delivery, he was grinning from ear to ear as he reached for the liquor bottle first. Then he saw Hyuk Mujin’s expression and paused.

“Why do you look like you’ve been chewing shit?”

“Great Hero Jeok. The thing is…”

As though he had been waiting for this, Hyuk Mujin began explaining. Jeok Cheongang listened silently, then his eyes widened.

“The Escort King’s granddaughter came here?”

“Yes.”

“Hm. Two unusual auras passed by while this old man was straining himself. I suppose she was one of them.”

Jeok Cheongang stroked his dark-red beard and continued.

“I heard that something like this happened while I was hovering between life and death, but seeing how it has led to this, it seems to be quite a persistent connection.”

“Then why do you think she came to Captain instead of choosing one of the other options?”

The corner of Jeok Cheongang’s mouth twitched.

“Do you really need this old man to say it aloud?”

“Right? I knew you’d understand, Great Hero Jeok.”

Just as Hyuk Mujin’s face lit up like an LED bulb, Jeok Cheongang continued with a meaningful smile.

“Because she can earn a tremendous amount of merit.”

“……”

*Oh. The bulb went out.*

Hyuk Mujin’s complexion darkened as though night had fallen in an instant, and his voice sank low.

“Are you serious?”

Jeok Cheongang nodded with a confident expression.

“Although she received a considerable fortune from the Zhongnan Sect as compensation, she will need fame and skill in the Murim to protect and lead her Escort Bureau in the future. From what this old man saw, the Escort King’s granddaughter understands how the world works.”

“Great Hero Jeok.”

“What?”

“Forgive me for asking, but have you ever had a sweetheart?”

Jeok Cheongang thought carefully before answering.

“Of course.”

“When was that?”

“I was around ten at the time. That was more than a hundred years ago, I think.”

“……”

“Why are you looking at me like that?”

“N-No, it’s nothing. It seems I was practicing wall-facing meditation.”

“……?”

“A real wall. A wall. The Wailing Wall.”

Jeok Cheongang took his eyes off Hyuk Mujin, who was muttering like an enlightened monk, and turned toward me.

“Anyway, what do you intend to do?”

“Hmm.”

“Judging by your expression, you’ve already made up your mind. That is why I ask.”

I shrugged.

“You’re psychic. I haven’t even told you yet.”

“I heard the details, and it is not a bad choice. You are an absurd monster, of course, but reaching the Peak realm at her age is an impressive accomplishment. And if she has been involved in the Escort Bureau’s affairs since childhood, she should have plenty of experience as well.”

“I was thinking along the same lines. An escort captain named Song Ilseom would be a major asset based on his skill alone.”

Jeok Cheongang had been hovering between life and death at the time, so he had never met either of them in person. But after waking up, he had heard everything that had happened, so he had no trouble following the discussion.

“The last bloodline of the Guangdong Chen Family. From what I sensed in the latrine, he had reached a considerable realm.”

“……That’s a little gross, but I agree.”

Jeok Cheongang was a Supreme Peak master who had reached the Returned to Youth realm. If he considered Song Ilseom’s skill considerable, then no one could dispute the man’s martial prowess.

*Another genius the world has yet to discover.*

He had lost his family at an early age and been cast alone into the world. He had wandered the battlefields as a sword boy for wandering martial artists, and eventually drawn a sword of his own.

Song Ilseom was not a greenhouse flower. He was a weed that had survived harsh storms.

His other name, Soul-Chasing Guest, was legendary even among wandering martial artists.

*He may not be on Cheongpung or Mungyeong’s level, but he’s more than enough to be a useful force.*

It was a shame, but I had no complaints. It was a fact that our lineup had been too spectacular until now.

In truth, it was only natural for things to change from this point onward.

A Supreme Peak master could reverse a losing battle in an instant. With the flames of war spreading in every direction, deploying them where they were needed was only natural.

*Mae Jonghak must have separated Cheongpung and me for the same reason.*

There were fires burning in several places. We could not keep sending the same fire truck to one location.

To win the war against Dark Heaven and prevent even greater sacrifices, this was the natural course of things.

And…

I needed to assemble a team to put out these flames with me.

It was time to make a decision with a cool head and reason.

*I suppose it can’t be helped.*

No matter how I thought about it, this was the best option. No—even if it was not the best, there was no denying that it was the second-best choice.

After organizing my thoughts, I called out one person’s name in a low voice.

“Hyuk Mujin.”

Hyuk Mujin always seemed slow, but he was surprisingly perceptive.

At least whenever I called him by both his given name and family name, he knew that the atmosphere was different from usual.

“Yes, Captain.”

“Let me ask you directly.”

The choice was not mine alone to make. Each person’s choice would come together to form a single will.

But before I could continue, Hyuk Mujin quickly answered.

“I’ll go with you.”

“What?”

“I said I’ll follow you, Captain. That was what you were going to ask, wasn’t it?”

“……Yes.”

“Then that settles it. There’s no need to ask. Naturally, the thread follows wherever the needle goes. Of course, traitors like Young Hero Gung are an exception. This is why outsiders from other sects won’t do. They always have so many complications.”

I stared silently at Hyuk Mujin, who gave me a playful smile, then lifted the corners of my mouth.

“You won’t regret this?”

“Regret?”

“Yes. Regret.”

“Captain. Do you know something?”

Hyuk Mujin continued with a serious look in his eyes.

“Ever since I met you, my life has been one long regret.”

“You son of a bitch.”

“But I decided that a few more regrets wouldn’t be so bad.”

Hyuk Mujin shrugged and continued slowly. His gaze, fixed on the empty air, seemed to be feeling its way through some distant place in the past.

“A few years ago, people called me the son of the Hyuk Family Textile Shop. But at some point, they started calling me the Swift Wind Sword. They even started calling me the Blazing Flame Divine Dragon’s right-hand man. I really like that.”

“Mujin, you…”

“Hehe. Are you touched?”

“No, not that. You’re not my right-hand man. You’re my little toe.”

“Wow, Captain. You really are something else. After all the suffering I’ve endured, I’m still just a little toe?”

At his aggrieved expression, a quiet laugh escaped me. Maybe it was time to promote him a little.

“Then you’re my little finger.”

“……My left little finger?”

“Right hand.”

“Right hand…”

Hyuk Mujin thought for a moment, then cautiously presented a counteroffer.

“Then I’ll take the right hand. How about the thumb?”

“Try again in your next life.”

“I knew you’d say that. Then instead of the thumb, how about the index finger?”

“Not a chance.”

“Damn it. I’ll have to devote my entire life to becoming your right-hand man. Does that make any sense?”

“Yes. It’ll take your whole life, so stay by my side until then. Don’t die.”

“……!”

*Did I say something I shouldn’t have?*

I had not even been out of the bath long, yet for some reason my skin felt itchy. I scratched my innocent chin for no reason, then held out my hand.

“C-Captain.”

Hyuk Mujin looked at me with moist eyes, then firmly clasped the hand I had extended.

*Clasp.*

“Hyuk Mujin, your Captain’s right little finger. I will devote my loyalty to—”

“What are you doing?”

“Huh?”

“Who asked for your hand? Bring me what you received earlier.”

“……Oh.”

Hyuk Mujin clicked his tongue with an expression that said *of course*, then pulled the two bamboo slips I had handed him earlier from inside his robe.

The names of two people were written in tiny letters on the cords binding the slips.

Dagger Hidden Flower Ju Hwaran.

Soul-Chasing Guest Song Ilseom.

But these were not the only bamboo slips I needed to receive.

When I still did not withdraw my outstretched hand, Hyuk Mujin’s complexion turned sour, as though he had guessed what I was thinking.

“Captain. Are you serious?”

“Yes.”

“Hoo. I don’t know if this is the right decision.”

With a sigh, two more bamboo slips were added.

I quietly looked down at the names and epithets written on the cords.

Black Dragon Saber Sama Pyo.

Tiger Giant Child Taishan.

Hyuk Mujin’s words—*I don’t know if this is the right decision*—continued to echo in my ears.

The reason was simple. I also had doubts about whether this was the best choice.

But the voice I heard next gave my hesitation one final push.

“What are you hesitating for? All you have to do is move forward.”

Jeok Cheongang’s words cleared my muddled thoughts.

After taking a small, deep breath, I whispered toward some place deep within my heart.

*Ju Hwaran, Song Ilseom, Sama Pyo, Taishan…*

And last of all, Hyuk Mujin.

After letting the names of all five people pass through my mind at once, I entered the command.

*Approve Two Dragons Pavilion membership.*

A voice answered the words no one else could hear.

*Ding.*

> **System**
>
> - Membership approval procedure initiated.
>
> - Confirmed: **Dagger Hidden Flower Ju Hwaran**, **Soul-Chasing Guest Song Ilseom**, **Black Dragon Saber Sama Pyo**, **Tiger Giant Child Taishan**, and **Swift Wind Sword Hyuk Mujin**.
>
> - Will you accept the five people above as members of the Two Dragons Pavilion?

The answer had already been decided.

I gave a small nod to signify my acceptance, and the translucent holographic window floating in the air changed with a cheerful chime, as though it were turning a page.

*Ding.*

> **System**
>
> - One condition of Quest, **Become My Companion!**, has been completed.
>
> - Secure at least five companions (Complete)
>
> - You have selected the minimum number of members!
>
> - One final procedure remains to become an official Pavilion Master. Choose a new name for the Pavilion assigned to you!

*A name, huh?*

I had never thought about what name to give the newly formed organization.

But no matter how much I thought about it, nothing could possibly be better than the name that had just flashed through my mind.

*Fire Dragon Pavilion.*

*Ding. Ding. Ding.*

Along with the clear bell tones bursting out like celebratory fireworks, powerful System alerts rang in my ears.

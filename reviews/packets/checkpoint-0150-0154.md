# Checkpoint Review — 150–154

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

# Chapters 150–154

## Plot

Four days after losing to Cheongpung, Jin Mukyung isolates himself and trains, realizing that his reputation as the Heaven Shaking Sword and one of the Ten Dragons and Phoenixes had made him a frog in a well. The defeat sharpens his ambition, and his Sword Energy becomes denser and more refined.

Jin Taekyung attempts to force open his Conception and Governor Vessels using his accumulated internal energy and the Scorching Yang Qi from the Blazing Flame Divine Pill. The attempt fails, slightly damages his acupoints, reduces his Sinews and Meridians by one, and leaves him severely injured. Cheongpung explains that Mae Jonghak forbade forcing the vessels open and agrees to train Taekyung after revealing that his own Governor Vessel opened naturally through enlightenment. Taekyung also persuades Hyuk Mujin to join the training.

Cheongpung makes them run to the training hall and climb a sheer cliff using the Wall Lizard Technique, without internal energy or weapons. He throws rocks at them throughout the exercise, rescues Mujin from a fall with the Zaha Divine Technique, and demands ten total ascents. Taekyung and Mujin complete the climbs over three days. Taekyung gains Strength, Agility, and Stamina during the training, acquires Wall Lizard Technique, levels up with 10 Stat Points and 10 Skill Points, and advances from Beginner Trainee to Intermediate Trainee. Cheongpung’s satisfaction generates the linked quest *Sword Saint Training: A Secondhand Experience—2*. Taekyung jokingly claims to have come from another world with a System, but Mujin does not believe him.

Meanwhile, Jang Childeuk begins guarding the Jin Family’s mostly unused training hall. The post is maintained as a symbol because Founder Jin Muryang allegedly trained beneath its cliff and opened the base with One Strike. Taekyung later falls from the cliff, slowing himself with a dagger and surviving through his physique and toughness. Childeuk and the other guard mistake him for a jiangshi until Childeuk recognizes him; Taekyung’s first words after waking mention Taecho Village again.

## Continuity

- Jin Mukyung lost to Cheongpung after roughly three hundred exchanges and has secluded himself to train. His ambition and Sword Energy have strengthened.
- Taekyung failed to force open the Conception and Governor Vessels, suffering slight acupoint damage and a one-point reduction in Sinews and Meridians.
- Cheongpung’s Governor Vessel opened naturally through enlightenment two years earlier; Mae Jonghak warned him never to force either vessel open.
- Cheongpung is training Taekyung and Hyuk Mujin with Mae Jonghak’s cliff-climbing method. The ten climbs are complete.
- Taekyung now has Wall Lizard Technique, 10 additional Stat Points, 10 additional Skill Points, and the Intermediate Trainee rank.
- *Sword Saint Training: A Secondhand Experience—2* has begun or been generated; the number of linked quests in the sequence remains unknown.
- Hyuk Mujin has accepted Taekyung’s training invitation and demonstrated persistence and martial talent. He does not believe Taekyung’s story about another world and a System.
- Jang Childeuk is now a martial artist directly under Jin Wikyung and guards the Jin Family training hall. He remains intensely loyal to the family.
- Taekyung survived his fall at the training hall but again mentioned Taecho Village after regaining consciousness. What Taecho Village is, and why he says “again,” remain unresolved.
- New Year’s Day is ten days away; Prince Shangshan Zhu Bao is expected at the Jin Family’s grand banquet around then.
- Cheongpung still lacks a martial title, which Zhu Bao requires before accepting his autograph.
- Mae Jonghak’s disappearance, Cheongpung’s unexplained origin, and the meaning of the crane that supposedly delivered him remain unresolved.

## Translation Decisions

- Render **임독양맥** as “Conception and Governor Vessels,” **근맥** as “Sinews and Meridians,” **기해** as “qi sea,” and **환골탈태** as “Bone Transformation.”
- Render **벽호공** as “Wall Lizard Technique,” **연무장** as “training ground,” **수련동** as “training hall,” and **청석** as “bluestone.”
- Render **진무량 조사** as “Founder Jin Muryang,” **천응** as “Heavenly Eagle,” **강시** as “jiangshi,” and **태초 마을** as “Taecho Village.”
- Render **초보 수련자** and **중급 수련자** as “Beginner Trainee” and “Intermediate Trainee.”
- Render **검성 수련 간접 체험기** and **검성 수련 간접 체험기-2** as “Sword Saint Training: A Secondhand Experience” and “Sword Saint Training: A Secondhand Experience—2.”
- Retain “His Highness” for formal **전하**, “king” for literal **왕**, “Sword God” for **검신**, “Sword Saint” for **검성**, and “Zaha Divine Technique” for **자하신공**.

## Durable state

{
  "active_continuity": [
    "The City Lord's luncheon requirement has concluded; Prince Shangshan's Token was obtained as the Quest Reward, and Zhu Bao is expected at the Jin Family's grand banquet in roughly fifteen days.",
    "Zhu Bao is ten years old, has trained in martial arts daily for three years, is an exceptionally skilled young swordsman personally named Zhu Bao, and admires Jin Taekyung.",
    "Taekyung remains below the Peak realm and cannot use Sword Energy despite defeating Jopil, Jin Baekyang, and Pung Yang.",
    "Hong Jin and Li Feng are pursuing the Shaanxi–Shanxi trade project through Huashan, with Li Feng acting as intermediary and the Seongun Escort Bureau proposed as the base.",
    "Cheongpung is a twenty-year-old Peak master raised by Mae Jonghak, knows several Huashan martial arts, can use the Zaha Divine Technique, obtained the Royal Guard Armor Set, has no martial title yet, and has begun teaching Taekyung and Hyuk Mujin using Mae's training method.",
    "Mae Jonghak remained in deep seclusion at a hidden Huashan residence and had been there at least ten years before the luncheon; Cheongpung came to Huashan at about age three or four rather than being born there.",
    "Huashan was sealed after Mae Jonghak entered the sleeping Sect Leader's quarters, left a dagger and handwritten letter, and disappeared; the search for his residence remains ongoing.",
    "Baek Museong is a first-generation Huashan disciple known as Huashan's Lone Crane and the first of the Three Plum Blossom Elites; he met Cheongpung ten years ago and is traveling with the other Elites to meet him again.",
    "Chulwoo and Eunhyang are Baek Museong's junior disciples and fellow members of the Three Plum Blossom Elites; both are notorious troublemakers who caused trouble with the Black Serpent Sect while traveling.",
    "Li Feng left Huashan after becoming discouraged by Cheongpung's extraordinary talent, not because of his defeat by Gong Ilhyuk.",
    "The identities of the other two members of the Three Hands of Zhongnan remain unknown.",
    "Hong Jin is a eunuch who formerly served the late Emperor, was ordered to assist Prince Shangshan, has served the prince since infancy, and is the power behind the Shanxi Provincial Office.",
    "Gong Ilhyuk leaves the luncheon humiliated and vows revenge against those who rejected and insulted him.",
    "Jin Mukyung lost to Cheongpung four days before the luncheon, then secluded himself to train; the defeat clarified his ambition and strengthened his Sword Energy.",
    "Jin Wikyung returned to the Jin Family after nearly ten days away, faces a large administrative workload, and prefers practical people with flexible thinking over rigid scholars; Hong Jin gave him one thousand silver nyang, prompting an extravagant pro-imperial welcome and a joking rapport between them.",
    "Taekyung failed to force open the Conception and Governor Vessels, suffering slight acupoint damage and a one-point reduction in Sinews and Meridians.",
    "Taekyung now has a private training ground in a newly rebuilt pavilion at the Jin Family; Hyuk Mujin accepted his invitation to train with him and Cheongpung, and Mujin has demonstrated substantial persistence and martial talent.",
    "Jang Childeuk, formerly a Jin Family servant and now a martial artist directly under Jin Wikyung, has been assigned to guard the largely unused training hall and remains intensely loyal to the family.",
    "The training hall is guarded as a symbol because Founder Jin Muryang allegedly trained beneath its cliff and opened the cliff base with One Strike; Taekyung survived a fall there by slowing himself with a dagger, aided by his physique and toughness stats, and mentioned Taecho Village after waking.",
    "The three-day Wall Lizard Technique training is complete: Taekyung and Mujin climbed the cliff ten times, Taekyung acquired Wall Lizard Technique, gained 10 Stat Points and 10 Skill Points, and had Beginner Trainee upgraded to Intermediate Trainee; Cheongpung's delight generated Sword Saint Training: A Secondhand Experience—2. Taekyung told Mujin, as an unbelievable joke, that he came from another world with a System."
  ],
  "continuity_sources": [
    154,
    153
  ],
  "open_questions": [
    "What did Mae Jonghak mean by saying a crane delivered Cheongpung to him, and why did he remain hidden at Huashan despite the sect eventually finding his residence?",
    "What are the names and individual identities of the other two members of the Three Hands of Zhongnan?",
    "What is the full title of the wuxia novel beginning with 군림…… that Taekyung read through volume thirty-four?",
    "Was the Emperor's reported suspicion of his younger brother the reason Prince Shangshan was sent to Shanxi, and what danger does the imperial succession pose?",
    "What martial title will Cheongpung eventually acquire?",
    "What circumstances led Hong Jin to become a eunuch and come to the frontier in something like exile?",
    "What is Taecho Village, and why does Taekyung say “again” after landing?",
    "How many linked quests are included in Cheongpung's training sequence?"
  ],
  "safe_through": 154,
  "temporary_decisions": [
    "Render 전하 as “His Highness” as the formal royal address and 왕 as “king” when used literally.",
    "Render 초일류 as “advanced First Rate” and 군문 as “military” when describing an affiliation; render 풍운검군 as “Wind-and-Cloud Sword Lord” and 오촌 당숙 as “father's cousin.”",
    "Render 태을미리장 as “Taeeul Miri Palm.”",
    "Render 후배님 and 선배님 as “Junior” and “Senior” in the Gong Ilhyuk exchange.",
    "Render 태사부 as “Grandmaster,” 사숙 as “Martial Uncle,” 자하신공 as “Zaha Divine Technique,” 근위대 as “royal guard,” and 근위대 갑옷 세트 as “Royal Guard Armor Set.”",
    "Render 비무행 as “dueling tour,” 청강검 as “blue-steel sword,” and 광염 as “light-flames.”",
    "Render 검신 as “Sword God,” 검성 as “Sword Saint,” 임독양맥 as “Conception and Governor Vessels,” 기해 as “qi sea,” 근맥 as “Sinews and Meridians,” 사해오호 as “Four Seas and Five Lakes,” and 환골탈태 as “Bone Transformation.”",
    "Render 연무장 as “training ground,” 수련동 as “training hall,” 청석 as “bluestone,” 십팔반병기 as “eighteen traditional weapons,” 찍고 땡 as “touch-and-go method,” 진무량 조사 as “Founder Jin Muryang,” 천응 as “Heavenly Eagle,” 강시 as “jiangshi,” 태초 마을 as “Taecho Village,” 벽호공 as “Wall Lizard Technique,” 낙안봉 as “Falling Goose Peak,” 인피면구 as “human-skin mask,” 초보 수련자 and 중급 수련자 as “Beginner Trainee” and “Intermediate Trainee,” and 검성 수련 간접 체험기 and 검성 수련 간접 체험기-2 as “Sword Saint Training: A Secondhand Experience” and “Sword Saint Training: A Secondhand Experience—2.”"
  ],
  "version": 1
}

## Reading copies

## Chapter artifact 150

# Chapter 150

The training ground was so wide and empty that it looked bleak. Sweat trickled down the forehead of a young man sitting cross-legged.

*What should I have done?*

He closed his eyes and sank into thought. Then he recalled one person.

He remembered Cheongpung’s crude blue-steel sword and clumsy footwork. He remembered the smile that vanished when the young man began to display his martial arts.

At last, from the pitch-black darkness, a figure wrapped in violet light-flames burst forth.

*Cheongpung.*

Grandson and disciple of the Sword God Mae Jonghak. It made no difference what he called him.

What mattered was the fact that four days ago, he had exchanged martial arts with Cheongpung—and lost.

Jin Mukyung had shut himself away in the training ground and his quarters ever since that day. He staved off hunger with fasting pills and chased away sleep through training.

Warm food and honey-sweet rest were of no use to him now.

*I lost. Completely.*

It had taken barely three hundred exchanges. Even taking into account the fact that his condition had not been normal, he had fallen far too easily.

*Who am I?* He was a genius who had reached the Peak realm at barely twenty and caused the Central Plains to tremble.

*Heaven Shaking Sword. Ten Dragons and Phoenixes… How laughable. Was that all I amounted to?*

The grand titles attached to someone as mediocre as himself seemed laughable, nothing more than empty reputations. And yet the way he had secretly held himself in high regard left him feeling hollow.

*Isn’t that the very definition of hypocrisy?*

*Who was it that said the world was vast?*

The Nine Provinces and Eight Wastes. The Four Seas and Five Lakes.

How many masters were hidden across this enormous continent?

Only after meeting Cheongpung did Jin Mukyung understand the true meaning of those words.

*I was a frog in a well.*

Heaven’s Gate Temple was certainly the greatest educational institution in the orthodox Murim, but not every genius under heaven became a student at Heaven’s Gate Temple.

The direct descendants of the Five Great Families and the direct disciples of the Nine Sects and One Gang were too busy inheriting their sects’ secret ultimate techniques.

Cheongpung was one of them. They had been born outside the well and had lived there for a long time.

*Wait for me, Cheongpung. And all the others, too.*

The moment his eyes opened halfway, Jin Mukyung’s body shot upward like lightning, and light burst from his waist.

Whoosh!

Sword Energy. The silver Sword Energy slashed incessantly in every direction. It was denser and clearer than it had been four days ago—no, than it had ever been before.

His duel with Cheongpung had given him insight and fighting spirit. His vague goal of simply becoming stronger had finally gained focus.

Swish, swish, swish, swish!

Jin Mukyung’s sword did not stop after that, either.

Not until he was exhausted, utterly spent, and collapsed…

* * *

In Murim, the dantian is called the qi sea.

The qi sea. The sea of qi. The place where all the internal energy in the body begins and gathers. Whoever coined the term had chosen very well.

Ding!

> **System**
>
> Qi circulation has begun.
>
> Follow the formula of the Jin Family’s Cultivation Technique to circulate your internal energy.

The Jin Family’s Cultivation Technique had reached the eighth stage. Following the path I had already repeated hundreds, even thousands, of times, I sent forty-five years of internal energy flowing through it.

*Hot.*

The Scorching Yang Qi I had gained by taking the Blazing Flame Divine Pill amounted to half a jiazi.

The powerful energy boiling like lava swept through every blood vessel in my body. Seeing its unstoppable momentum, I began to feel a little hopeful.

*Maybe it’s possible now…*

There was always one part that blocked me whenever I circulated my qi. Two acupoints locked as firmly as iron gates, refusing to let internal energy pass through.

I had only recently learned that they were called the Conception and Governor Vessels.

*The Conception and Governor Vessels. I’ve seen them a lot in novels.*

Wasn’t this a stage every protagonist in a martial arts novel passed through at least once?

In martial arts novels, opening the Conception and Governor Vessels was the bare minimum, while Bone Transformation was optional. Of course, I was neither a protagonist nor even a supporting character, so I had been forced to retreat every time.

*That was then. Until now.*

Fifteen years of internal energy had been insufficient. It was like driving a compact car whose airbags did not even work straight into a boulder.

But things were different now. If half a jiazi of Scorching Yang Qi were added to the mix, the compact car would be transformed into a military tank.

*This should be worth a try.*

No. I had to do it.

It was a mountain I absolutely had to cross if I wanted to advance to a higher realm.

I drew up the internal energy that had reached its peak and shot it down two paths, toward the Conception Vessel and the Governor Vessel.

Boom!

The collision between my internal energy and the acupoints sounded like thunder. At the same time, a sharp pain rang through my spine and lower abdomen.

The stronger the collision became, the more vicious the recoil was. But I could not give up here. I clenched my teeth and kept crashing into them.

Boom! Boom! Boom!

*What the hell is this?*

I had put my body through hell in my own way. Being stabbed was nothing unusual, and I had even suffered damage to my internal organs before.

But this was a completely different kind of pain.

*I can accept my lower back hurting, but why does it hurt there?*

A part of a man as important as his life throbbed painfully. It felt as though someone were squeezing it as hard as they could, releasing it, and then repeating the process.

It felt as though I would receive an incredible reward if I opened the Conception and Governor Vessels. It felt as though I would become a Peak master if I could only endure this…

But the more I slammed my internal energy against them, the more the world before my eyes turned yellow.

“Ugh!”

Beep! Beep!

> **System**
>
> Qi circulation failed.
>
> Your internal energy became disordered, causing slight damage to your acupoints.
>
> **Sinews and Meridians** decreased by 1.

My balls were already aching badly enough to make me miserable, and now my Meridians had dropped, too.

I grabbed the still-throbbing area and collapsed face-first onto the bed.

“Ugh! Uuugh!”

As rice bows its head more deeply the riper it becomes, a man bows at the waist more deeply the more his vital points hurt.

I stayed hunched over for a long while as though praying, and the pain gradually subsided.

“Huff, huff.”

I had almost ended up like Hong Jin.

Just as I sprawled out on the bed, drenched in sweat, hurried footsteps approached, and unwelcome guests burst in.

“Captain!”

“Benefactor!”

Hyuk Mujin and Cheongpung rushed through the door, then stopped short when they saw me.

“What happened… Whoa.”

“Benefactor, what are you doing?”

“Huh? What about it?”

I asked the question, then realized it.

I realized what I looked like right now.

“Oh.”

A twenty-something young man in a sealed room, soaked in sweat despite the middle of winter, lying on a bed with one hand clutching that particular spot.

Hmm. There was definitely room for misunderstanding.

I calmly opened my mouth.

“You’ve got it wrong.”

After a brief silence, Hyuk Mujin smiled with his eyes.

“I know. I know everything.”

“No, you don’t.”

“Oh, come on. Why are you acting like this? We’re both professionals.”

“What do you mean, professionals, you lunatic?”

“You’re still pretending not to know. Do I look like such a narrow-minded man to you?”

“I’m telling you, that’s not what it is!”

“Did you enjoy yourself? If you haven’t finished yet, should I step outside?”

“I haven’t even started!”

“Oh, then you were just about to start. Should I come back when you’re done?”

“I’m not doing it! I have no intention of doing it!”

“It’s all right. There’s nothing to be embarrassed about. I do it five times a day when I’m in good shape.”

“Is that actually true…? No, wait. You little—”

Chaos. Destruction. A complete mess.

As the conversation only grew more suspicious with every passing moment, Cheongpung tilted his head.

“What’s the misunderstanding? What does he know?”

“Young Hero Cheongpung, you really don’t know why the Captain is like that?”

“I don’t. Does he need to pee?”

“What? How can this be? I’ll only explain it once, so remember this well. All of this becomes flesh and blood. I’m telling you, it changes your life.”

“Yes!”

“Where is the Captain’s hand right now? Answer me.”

“On his lower half.”

“That’s right. And what’s on the lower half?”

“Underclothes.”

“Underclothes! Good. You’re almost there. And what’s inside the underclothes?”

“Huh? But right now it isn’t on his lower half.”

“What?”

“Benefactor’s hand is coming this way.”

“Gasp.”

Smack!

Thud.

It was a slap aimed precisely at his lower jaw. Hyuk Mujin crumpled with a peaceful expression, and Cheongpung caught him.

“I haven’t heard the whole thing yet.”

“…What are you going to do with the rest of it?”

“You said that hearing it would make it flesh and blood and change my life. Isn’t that a good thing?”

“…”

Come to think of it, that wasn’t entirely wrong.

Cheongpung looked dejectedly at the sex-education teacher who had already passed out.

“But what were you doing while holding your lower half?”

“…”

If anyone else heard this, they would definitely misunderstand.

* * *

“…And that’s what happened.”

By the time I finished an explanation packed full of facts, Hyuk Mujin had woken up and was muttering with a sullen expression.

“Then you should have said that from the beginning.”

“Whew. Do you really want me to beat you to death today?”

“Ah, I’ll pass. My head is still ringing.”

Hyuk Mujin winced and shook his head.

“But why did you suddenly try to open the Conception and Governor Vessels? You’re not a Peak internal-energy master, and you don’t have the guts to risk something like that.”

“…I just tried it once.”

“What?”

“Forget it. You’re noisy, so shut your mouth.”

I waved my hand at Hyuk Mujin, who had opened his eyes wide.

It was too embarrassing to admit that seeing the duel between Jin Mukyung and Cheongpung four days ago had made me want to become much stronger than I was now.

“Anyway, just know that I failed spectacularly. I couldn’t do it properly because it hurt there. Why is this happening?”

“I wouldn’t know. I’m not a physician, and I’m not some Peak master either.”

Hyuk Mujin and I naturally turned our gazes to the side. The aforementioned “Peak master” blinked and opened his mouth.

“Hmm. I’ve heard something about it from my grandfather.”

Hyuk Mujin knew Cheongpung’s identity now, too. We both let out exclamations full of anticipation.

“Ohhh.”

“Ooooooh.”

The Sword Saint Mae Jonghak was one of the most highly regarded masters under heaven. When it came to martial arts, if he had said it, we could believe him even if he told us that red beans could be made into soybean blocks.

“What did he say?”

“He said that if you mess up the Conception Vessel, you might not be able to perform as a man, and that the same goes for the Governor Vessel. And what else did he say? Oh, right!”

Cheongpung, who had been thinking hard, smacked his forehead.

“He said they would open on their own with time, so I should leave them alone. He said touching either of them incorrectly would turn me into a cripple.”

“…”

“…”

*What the hell is he talking about?*

Hyuk Mujin and I exchanged glances almost simultaneously.

“Do the Conception and Governor Vessels normally open with time?”

“I don’t know. That’s the first I’ve heard of it, too.”

“But it couldn’t be nonsense. He’s the Sword Saint, after all.”

“Right. Perhaps it takes a very long time?”

“How long?”

“How would I know? My father is almost sixty. Should I ask him?”

“Oh, ask him whether his Conception and Governor Vessels have opened?”

“Yes.”

“Is he a martial artist?”

“He owns the Hyuk Family Textile Shop.”

“Try not to talk if you can help it. You’ll drive the listener insane.”

“Yes.”

I pitied myself for taking someone like this around as my subordinate.

I let out a deep sigh and spoke to Cheongpung.

“Could you explain in a little more detail? Surely your grandfather didn’t say only that…”

“He said exactly that.”

“…Really? Word for word?”

“I don’t lie to my Benefactor.”

That was true. Cheongpung was not clever enough to lie.

Whether it was in his nature or the result of his upbringing, he was so honest and guileless that, put unkindly, he looked stupid.

Cheongpung added with an indignant expression,

“And my grandfather isn’t someone who lies, either. I waited, too, and mine opened. Not both of them—just the Governor Vessel.”

“The Sword Saint didn’t lie… Wait. What did you just say?”

“Young Hero Cheongpung, what did you say? You opened the Conception and Governor Vessels?”

“Oh, only the Governor Vessel for now. Maybe it’s because I’m still young.”

I asked haltingly,

“How did you open it?”

“Two years ago, I was training when I suddenly felt strange, and then—bang!”

“Bang?”

“That’s how it opened.”

“…”

“…”

“I thought it was strange, so I asked my grandfather about it. He said it was enlightenment. Hehe.”

This was hopeless. We were far too different.

The Sword Saint had been right that the Conception and Governor Vessels would open naturally with time.

The problem was that it only applied to Cheongpung.

The young man smiling brightly in front of me was practically a new species of humanity, fundamentally different from someone like me.

*Genius. Talent bestowed by heaven. That’s what this is.*

Cheongpung and Jin Mukyung. Their innate talent was different from mine from the very beginning. There was no answer for me.

When I remained silent for a while, Cheongpung cautiously watched my expression.

“Benefactor, did I do something wrong?”

“No. You didn’t do anything wrong.”

“Really? That’s a relief.”

As Cheongpung sighed in relief, I licked my dry lips.

“But, um…”

“Yes?”

“Can I ask you for a favor?”

“Tell me whatever it is.”

Damn it. Why was it so hard to say now that the moment had come?

I had thick skin. I had been called shameless, and I had been called without shame.

But why was this one sentence so difficult?

“Benefactor?”

With great difficulty—truly, great difficulty—I forced out the words.

“Could you help me with my training?”

“Of course. Certainly.”

“What?”

“I’ll help you. With your training.”

As I looked into his clear eyes, I finally understood why I had hesitated.

It was competitive pride.

The competitive pride that made me unwilling to accept help from this young man of all people.

It was not because I disliked him. It was because he was an opponent I wanted to bring down solely through my own strength.

I wanted to stand on equal footing with him.

But to do that…

“Then I’ll be counting on you.”

I had to learn. What else could I do?

Turns out I had a thicker hide than I thought.
## Chapter artifact 151

# Chapter 151

The pavilion where I’m staying was newly built only a few days ago.

Apparently, on the first day Jin Mukyung returned to the Jin Family of Taiyuan, he made such a spectacular mess that they tore down the old pavilion and built a new one.

*The important thing is that I have a training ground now.*

There was no way Jin Wikyung, who absolutely melted whenever it came to his younger siblings, would have cut corners.

The inside of the pavilion was decorated far better than before, but more importantly, I now had a private training ground of my own.

“We invited the finest carpenters and stoneworkers from the surrounding area to build it.”

“Really?”

I listened to Hyuk Mujin’s explanation, which sounded like something from a real estate agent, while looking around the training ground.

There was a high wall to keep out prying eyes and a spacious training ground. In one corner, weapons for training—what were commonly called the eighteen traditional weapons—rested on a rack.

“Especially this part. Don’t you think the floor has a bluish tint?”

“It does. It looks like stone.”

“Yes. This is a type of bluestone, but it isn’t just for appearances. Would you like to see?”

Bang! Bang!

“Hey!”

I shouted in surprise when Hyuk Mujin suddenly stomped down with all his strength.

This bastard had completely lost his mind just because it wasn’t his training ground.

But Hyuk Mujin pointed at the floor as though nothing had happened.

“Now, before you get angry, look at the floor. It’s perfectly fine.”

Really?

At Hyuk Mujin’s Level, he was more or less qualified to be called a First Rate martial artist, yet the floor had only suffered a few minor scratches. They must have spent quite a bit of money.

“High-quality bluestone is extremely hard. It doesn’t break easily.”

“Wow.”

“Whoa, they have things like this too? I’ve only ever trained on dirt.”

Cheongpung, who had been tapping the floor in fascination, lightly stamped his foot.

Crack!

“Huh? It broke.”

“…”

“…”

You little bastard. Who told you to put internal energy into your foot?

I stared sadly at the training-ground floor, which had been smashed before I had even gotten to use it properly, then turned toward Hyuk Mujin.

“I didn’t do anything wrong.”

“I didn’t say anything.”

“You just cursed at me with your eyes.”

“Do you want me to do it with my mouth too?”

“…”

“No, thank you. Then I’ll be leaving. I just remembered something important.”

Look at him, casually edging toward the exit.

I grabbed the back of the neck of the man trying to sneak away.

“Why? Why are you doing this?”

“Where do you think you’re going? You have nothing to do.”

“Nothing to do? Do you think I’m some idle wastrel? I told you I have something important to do.”

“Would someone with something important to do spend two days loitering in my pavilion?”

“…”

“I heard you got reward leave. Your eldest brother told me.”

Cheongpung shot his hand into the air and shouted,

“Wow, reward leave! I want to receive some too!”

“...Young Hero Cheongpung, are you making fun of me?”

“You there, clean up the broken pieces of bluestone.”

“Oh, yes!”

What a pointlessly cheerful fellow.

Meanwhile, Hyuk Mujin, who was still trapped in my grip and kicking his feet, let out a deep sigh.

“Whew. Fine. Just hit me once and get it over with.”

“Why would I hit you?”

“Didn’t you grab me because you wanted to hit me?”

“Of course not. Do I look like such a violent person that I’d hit someone without a particular reason?”

“Yes.”

“Some people repay a thousand-nyang debt with a single word, but you earn a thousand blows with your mouth.”

Smack!

“Ugh.”

“Don’t be such a baby.”

Hyuk Mujin rubbed his reddening forehead and said,

“I’ve been hit once, so we’re even, right? I’ll be going now.”

“Going where? Stay here.”

“What would I do by staying here? You’ll obviously just make me run pointless errands.”

When I didn’t answer and only stared at him, Hyuk Mujin grumbled on.

“You may have forgotten, Captain, but I’m a martial artist too. If I want to become the Master of the Gatekeeper Pavilion, I need to train hard.”

“Who told you not to train?”

“Huh?”

I still couldn’t tell whether he was stupid or simply unable to think of the obvious. I clicked my tongue as I looked at Hyuk Mujin, who had yet to catch on.

“I’m saying you should train with us here.”

“...Me? Here?”

He looked back and forth between Cheongpung and me with a bewildered expression before haltingly opening his mouth.

“Is that really all right?”

“No reason it wouldn’t be. Is that okay with you, Young Hero Cheongpung?”

Cheongpung, who had been proudly examining the pieces of bluestone he had somehow managed to fit back together, nodded.

“I don’t mind. But you have to buy me lots of candied hawthorn skewers[^1] later.”

“…Are you possessed by a ghost who died because they couldn’t get any candied hawthorn skewers?”

“A ghost? Benefactor, is there a ghost attached to me right now?”

“No, that’s not what I meant.”

“Wow! A ghost! A ghost!”

“God, this is driving me crazy.”

This guy was completely out of his mind.

I shook my head repeatedly and looked away from Cheongpung. Hyuk Mujin was still standing there in a daze.

“So, what’s your answer? Don’t you want to do it?”

He suddenly came to his senses and shook his head vigorously.

“Of course I want to. I really do... Are you sure I’m allowed to join you?”

“I told you that you are. Did you commit a crime or something?”

“Even so, it’s an unwritten rule of the Murim not to show one’s martial arts to other people...”

It was the same among Hunters, too.

The instinct to avoid showing all of one’s abilities clearly existed among Hunters, even if it was less intense than in the Murim, where people killed one another.

*And the higher a Hunter’s rank, the more true that was.*

As for mediocre lower-level Hunters, they had no money, so they gathered together and trained like people at a neighborhood gym. But once a Hunter reached the middle levels and had some money to spare, getting a private training room became practically standard.

“Captain and Young Hero Cheongpung are masters who inherited the secret arts of your respective sects, but I’m different. I won’t be of much help while the two of you train.”

“Hmm. That’s true.”

“...Yes.”

I continued speaking as Hyuk Mujin lowered his head with a dejected expression.

“That’s why you should learn properly this time and become useful.”

“What?”

“How long are you going to keep getting beaten up? Is becoming the Master of the Gatekeeper Pavilion the goal of your life? If you’re going to advance with me into broader waters, you need to become stronger too.”

“...!”

“Just train hard. Instead of wasting time worrying about whether you’re qualified, keep your mouth shut, be shameless about taking the opportunity, and train even if you have to cut into your sleep.”

That was what I had done. For the past several years, I had struggled desperately to survive even one day longer.

I had attended to senior Hunters and done everything I could to learn even one more thing from them. After bleeding and sweating through the process, I had absorbed what I learned and made it my own.

Because I had experienced that myself, I could understand Hyuk Mujin’s hesitation. But at the same time, it frustrated me.

*He even has considerable talent.*

Martial artists and Hunters were different. Hunters received their abilities overnight, while martial artists built their skills up from the ground, one layer at a time.

In that sense, Hyuk Mujin’s talent was considerable.

*I only have to compare him with the deadwood among the Five Gates of Shanxi to see that.*

Those men had been born into martial families and learned martial arts from an early age.

Hyuk Mujin, on the other hand, began learning martial arts at an age when his bones and muscles had already hardened, yet he reached the First Rate realm in only five years.

Of course, that assessment was based solely on his Level, but even if he fought them in actual combat right now, he could easily overpower men of their caliber.

*Talent wasn’t the only thing he had. He had real grit.*

Five years. That was how long it had taken the son of a textile-shop owner to become a First Rate master. Hyuk Mujin had said that he had not returned to his family home even once during that entire time.

I recalled something he had said a few days earlier.

*“I started learning martial arts a little late. What else could I do if I wanted to catch up with everyone else? I had no choice but to work ten or twenty times harder.”*

It was easy to say, but not something an ordinary person could do.

It meant that he had continued his grueling efforts while sacrificing even his sleep. In that sense, Hyuk Mujin and I clearly had something in common.

*The problem is that our inferiority complexes are similar too.*

That was why he couldn’t easily accept the goodwill Cheongpung and I showed him. He knew it was a good opportunity, but a feeling kept holding him back.

*Can someone as insignificant as me really join them here?*

Those emotions were holding Hyuk Mujin back. I looked straight into his eyes.

“I made the offer. The decision is yours. If you choose to continue as you are, I won’t stop you.”

“...May I ask you one thing?”

I nodded. After a brief silence, Hyuk Mujin parted his lips.

“Why are you being so kind to me?”

“You said you were my right arm, didn’t you? Or was it my heart?”

“Pardon?”

“What do you mean, ‘pardon’? You went around saying that yourself.”

“You told me to stop talking nonsense every time I said it.”

“That was just something I said. If I disliked you, would I have kept you around all this time?”

“Wasn’t it because you were bored? Sometimes you seemed to enjoy hitting me when your hands got restless.”

“…”

Just how much of a piece of trash did this bastard think I was?

When I glared at him, Hyuk Mujin hurriedly pretended nothing had happened.

“Ahem. Ahem, ahem...”

“Listen, if I hadn’t planned to raise you up, I would have gone around alone a long time ago. What would I gain from carrying deadweight like you?”

“Deadweight? How can you change your story so easily? A moment ago, you were calling me your right arm or your heart.”

“Right arm, my ass. At your current level, I’ll let you be my little toe.”

“Wow. That’s harsh. Really.”

He sounded hurt, but he couldn’t hide the corners of his mouth, which kept rising.

Right arm or little toe, they were both important parts of the body. That fact didn’t change.

Feeling strangely embarrassed, I shouted,

“Enough! Are you doing this or not?”

“I’m actually a martial arts genius, you know. I might copy everything you do. Are you sure that’s okay?”

“Bullshit. Copy it if you’re capable.”

“Really?”

“Ask one more time and I’ll beat you until it hurts.”

Hyuk Mujin smiled broadly.

“I’ll do it.”

His voice sounded relieved, as though he had just shed a heavy outer layer.

* * *

Hyuk Mujin and I sat on the floor of the training ground and looked at Cheongpung. Taking a seat was the basic requirement before the real lecture began.

“All right. Let’s begin.”

“I look forward to learning from you, Young Hero Cheongpung.”

“Yes, yes! Hoo, hoo...”

Every time Cheongpung took a heavy breath, white steam puffed from his nose into the cold winter air.

What was wrong with him all of a sudden?

“Are you all right?”

“I’m fine!”

“You startled me. Why are you suddenly acting like this?”

“Oh. Um, well...”

Cheongpung hesitated, then spoke with a face flushed bright red.

“This is my first time teaching anyone, so I’m too excited and worked up... Whew, give me a moment.”

“…”

“…”

I knew this would happen.

Perhaps he was still nervous, because Cheongpung spoke in a trembling voice.

“Th-then I’ll begin.”

“Don’t make it so stiff. Just relax.”

“R-relax?”

“Yes. Relax. Just teach us in whatever way you’re comfortable with, Young Hero Cheongpung.”

“If it’s the way I’m comfortable with...”

“The way your grandfather taught you, Young Hero Cheongpung.”

“Oh. What an easy solution!”

Hyuk Mujin and I looked at Cheongpung with expressions filled with anticipation and curiosity.

This was the teaching method of the Sword Saint himself. How had that great martial artist raised this genius?

*It must be something completely different.*

At that moment, a smile appeared around Cheongpung’s mouth as he became lost in thought. Apparently, merely thinking about the method put him in a good mood.

“Oh, I thought of something. This training will probably help both of you a great deal, too.”

“Oh!”

“Ooh. What is it?”

“Can you see that?”

We turned our heads in the direction Cheongpung was pointing.

Hyuk Mujin spoke first, and I followed up.

“That’s...”

“The training hall.”

It was roughly two hundred jang from the training ground. I had a pretty good idea what kind of training Cheongpung had in mind, and I let out a quiet laugh.

It was the classic touch-and-go method: repeatedly running like hell to touch the destination and come back.

*I expected something different because he was the Sword Saint, but this isn’t anything special.*

It was certainly a classic, but it was an effective exercise for building endurance and strengthening the lower body.

I stood and began stretching leisurely.

“Do we just go there and come back?”

Cheongpung tilted his head.

“Huh? You’ve done it before?”

“I’ve done it until I was sick of it.”

“Oh, I see. That’s a relief.”

Cheongpung smiled brightly and pointed at Hyuk Mujin and me in turn.

“Then I’ll give you half a shichen and one full shichen, respectively.”

“...?”

“...?”

“What?”

I asked in confusion.

“Half a shichen? What does that mean?”

“Didn’t you say you’d done it until you were sick of it? That should be enough time for you.”

“That’s true, but... Ah, I get it. Do we have to make nonstop round trips for half a shichen?”

“No. For now, you only have to do it once. I’ll wait for you at the summit.”

“What? The summit?”

“Yes. There.”

This time, I saw it clearly. Cheongpung’s raised fingertip was pointing at the cliff behind the training hall.

Hyuk Mujin and I both dropped our jaws.

*Holy shit. What the hell is that?*

The height was impossibly vast. Even judging by eye, it was a steep cliff hundreds of jang high. My vision went dark, and my hands and feet began to tremble.

If I was like this, Hyuk Mujin was obviously even worse.

“Are you saying we’re supposed to climb that?”

“Yes! I chose it because it’s about the same height as the place I climbed every day when I was little.”

“…”

“…”

“Oh, it brings back memories. I fell halfway down and nearly died twice. It really hurt back then.”

“...!”

“...!”

He was insane. The Sword Saint was insane, and this bastard was insane too.

[^1]: Candied hawthorn skewers are a traditional snack made by coating fruit on skewers in hardened sugar.
## Chapter artifact 152

# Chapter 152

“Yaaawn.”

A middle-aged martial artist glanced to the side after letting out a long yawn.

Only a few paces away, the new recruit who had been assigned here today was standing stiffly and staring straight ahead.

*What a guy. He’s got one hell of a build.*

Limbs like pestles. Shoulders spread wide.

Judging by his size alone, one might have suspected he came from the Hebei Peng Family, famous for producing martial artists with strong bones and muscles.

*Come to think of it, I don’t even know his name yet.*

The weather was cold, and there were still more than three shichen left in his shift.

On days like this, chatting was the best way to make time pass faster and keep warm. The middle-aged martial artist slowly opened his mouth.

“Hey there.”

“Yes, sir!”

“Good heavens, did you swallow a thunderbolt? Why are you shouting so loudly?”

“I’m sorry!”

“You don’t have to apologize for that. Is it because you’re new? It’s nice to see someone so full of spirit.”

“Ah, thank you.”

“Yeah, yeah. That’s right.”

The middle-aged martial artist smiled, pleased. They had only exchanged a few words, but the kid seemed decent. His manner was straightforward, and unlike young people these days, he was polite too.

For a man who was slowly being treated like an old-timer fit only for the back rooms, he had found himself a pretty good conversational partner.

“Is your surname perhaps Peng?”

“No. It’s Jang.”

“I only asked because I was curious. Your physique is quite impressive. I wondered whether you might be from some distant collateral branch of the Hebei Peng Family.”

The new martial artist scratched the back of his head.

“I was pretty strong even when I was a little kid.”

“I thought so. Your limbs are packed with muscle. You remind me of myself when I was young.”

Of course, that was utter nonsense. But despite his appearance, the new martial artist was perceptive enough to immediately bow deeply.

“Compared to what you were like in your youth, Senior, I’m nothing.”

“Hey, none of this ‘Senior’ business. Call me hyung from now on. Ah, I’m Hong.”

“Yes, hyung!”

“Heh heh. Looks like I’ve got myself a good little brother. So, Jang, when did you join this family?”

“It’s already been several years.”

“Huh? That can’t be right. If a fine candidate for a general like you had joined, I would have heard about it long ago…”

He had been with the Jin Family of Taiyuan for nearly twenty years. He considered himself something of an old hand and knew exactly which martial artists came and went.

“Ah, I haven’t even been a martial artist for a month. Before that, I was a servant who handled odd jobs here and there. I worked in places where I didn’t stand out much, so you might not have noticed me.”

“Ahh, I see.”

The middle-aged martial artist looked at the new recruit with fresh interest.

A servant who became a martial artist. It wasn’t unheard of, but it wasn’t common either.

“You must have a powerful backer.”

“Pardon?”

“Oh, come on. Don’t play dumb. Do you think it’s easy for a new recruit to get assigned to this position?”

The middle-aged martial artist grinned and poked the new recruit in the side.

“Who is it? The Chief Steward is far too strict to be behind it, so did you manage to secure a solid connection somewhere in the leadership?”

“Well, I…”

“Just tell me quietly. I’ll keep it to myself. Is it the Outer Hall Master? Or the Iron Sword Squad Leader?”

*The Lesser Family Head sent me here.*

The new martial artist, Jang Childeuk, swallowed the words that had nearly slipped out.

People’s tongues were terribly light. If he told the truth, the rumor would spread before the sun rose tomorrow.

*I can’t cause trouble for the Lesser Family Head!*

When it came to loyalty toward the Jin Family of Taiyuan, Childeuk was no less devoted than any martyr.

He avoided the middle-aged martial artist’s intensely curious gaze and opened his mouth.

“By the way, was this really such a difficult place to get into?”

The middle-aged martial artist looked disappointed at the change of subject and clicked his tongue. Since Childeuk clearly didn’t want to talk about it, there was no point in pressing him further.

“Tsk. You said you’d been with the family for several years, right?”

“That’s right. Although I was a servant.”

“Then how many times did you come to the training hall during those years?”

“Exactly twice.”

“Right? Now, take a good look around.”

“Right now?”

“Or would you rather do it next year?”

Jang Childeuk looked around as instructed.

Beneath the steep cliffs that enclosed the rear of the Jin Family without a single gap, there was a wide-open cavern.

That was the entrance to the training hall, and other than Childeuk and the middle-aged martial artist, there was no one there.

“What do you think?”

“It’s deserted.”

“Right? How many people do you think come here in a day?”

“How many?”

The middle-aged martial artist answered indifferently.

“No one.”

“Pardon?”

“Other than the people who come to change shifts every four shichen, nobody comes here. Ah, there is a servant who delivers meals.”

“But… this is the training hall, isn’t it?”

“It is. But does anyone train here? No. The Third Young Master came in and out a few times after causing trouble, but that’s about it.”

What an absurd thing to say.

Come to think of it, it was called a training hall, but Childeuk had never seen anyone actually training there.

The training ground, on the other hand, was always crawling with martial artists, no matter the season.

“Then why are we guarding this place?”

“It’s a symbol.”

“A symbol?”

“Long ago, Founder Jin Muryang trained here. According to the story, he suddenly attained enlightenment while training on this cliff and unleashed his martial arts, blasting open the base of the cliff with One Strike.”

Jang Childeuk’s mouth fell open.

He remembered hearing the legend of Founder Jin Muryang. Hadn’t he been one of the most renowned masters in the world three hundred years ago?

But how could such a thing be possible with a human body?

“Is, is that really true?”

“It happened hundreds of years ago. What does it matter whether it’s true or false? There’s another fact that’s actually important.”

“…Yes?”

“If you sit around in front of this training hall for a few shichen a day, your monthly pay comes like clockwork. That’s what matters. The only downside is that time passes unbelievably slowly.”

The middle-aged martial artist grinned and patted Childeuk on the shoulder.

“Congratulations. You’ve been assigned to the finest post the martial artists of this family dream of. They call it a cushy post.”

“…”

Childeuk’s face twisted.

It would be one thing if he were old enough to retire at any moment, but he was still in his prime. He had no intention of wasting his time in the training hall with nothing to do.

The middle-aged martial artist, unaware of his thoughts, pulled out a strip of dried meat and began chewing.

“Want one?”

“I’m fine.”

“Why? It’s salty and pretty good. Looking at the sky while chewing jerky makes time pass quickly.”

The middle-aged martial artist leaned against the entrance to the training hall and tilted his head back to look at the sky.

“Well, would you look at that. The sky is so clear. Just looking at it makes my chest feel wide open.”

Jang Childeuk reluctantly glanced upward.

Just as the middle-aged martial artist had said, the weather was clear. A few wispy clouds drifted slowly across the blue sky, along with several black specks.

“What are those?”

“Birds, probably.”

Childeuk’s gaze, which had been fixed blankly on the sky, shifted toward the cliff towering into the heavens. His eyes narrowed.

“What about that thing clinging to the cliff?”

“The cliff? What’s on the cliff?”

“Yes. It’s pretty big.”

“Dunno. Must be a pretty big bird. Hold on, I brought a bottle of liquor somewhere…”

Without even looking toward the place Childeuk was pointing, the middle-aged martial artist pulled a small porcelain bottle from his robes.

“It seems too big for a bird.”

“It could be a Heavenly Eagle. Those things are as big as people. They aren’t ordinary hawks.”

“Wow. It really is as big as a person.”

“They’re even called spirit creatures. I heard their wingspan alone is more than a jang. I’ve only seen one from a distance, myself.”

“But, hyung.”

“What? Why do you keep calling me?”

“Do Heavenly Eagles fall, too?”

“What the hell are you talking about?”

The middle-aged martial artist, who had been tilting the bottle toward his mouth, hurriedly looked at the cliff.

At that dizzying height, a massive dot was plummeting rapidly.

“Aaaaaaah!”

Childeuk sounded impressed.

“It really is a spirit creature. Its scream sounds exactly like a person.”

“That’s a person, you lunatic!”

“Whaaa!”

“Move! Move!”

The instant the middle-aged martial artist screamed, a person crashed into the ground amid a shower of stones.

*Boom! Rumble, rumble!*

Rocks and dust burst in every direction. The two men swallowed at the same time.

“D-do you think he’s dead?”

“Try falling from that height. Even the Jade Emperor would die.”

What a calamity to interrupt their peaceful daily routine.

The middle-aged martial artist clutched his trembling chest and stared at the body lying facedown.

“What kind of madman falls from a cliff…”

“He looks young.”

“Does it matter whether he’s young or old? The important thing is that he’s dead.”

“That’s true, but…”

“Go turn him over.”

“M-me?”

“Who else is here besides you and me? Hurry!”

At the middle-aged martial artist’s shout, Jang Childeuk hesitantly began approaching the body.

He had only been a martial artist for a month. This was the first time he had ever witnessed someone die right in front of him.

“Huff, huff.”

The closer he got, the more clearly he could see the body.

Its limbs lay limp, and blood streamed from the back of its head as it lay facedown on the ground. Considering the height of the fall, the corpse looked surprisingly intact.

“May you be reborn in paradise.”

He squeezed his eyes shut and reached out to touch the body.

That was when—

The body sprang upright.

*Crack!*

The world flashed before Childeuk’s eyes, followed by a wave of blinding pain.

He landed hard on his backside, mouth hanging open, unaware that blood was pouring from both nostrils.

“Uh… uhhhh.”

“What the hell just… ugh, ughhh!”

The middle-aged martial artist’s legs gave out, and he collapsed.

“The corpse—the corpse is alive!”

“Ugh! It’s a jiangshi! A jiangshi[^1] has appeared!”

The dirt-covered stranger who had suddenly been written off as dead staggered to his feet.

He looked around with his hair in disarray and blood vessels burst in his eyes, then ground his teeth.

“Fuck, Taecho Village[^2] again?”

* * *

Damn, that hurts.

My head, shoulders, knees, feet, knees, feet… There wasn’t a single place that didn’t ache. Luckily, I had slowed my fall by driving a dagger into the cliff. Otherwise, I might have ended up dead.

Of course, the physique and toughness stats I had steadily raised had helped, too.

“Ow, the back of my head is throbbing.”

When I touched the tender spot on the back of my head, blood came away damply on my fingers.

I tore off a strip of my sleeve and was wiping away the blood when—

“Who are you?!”

“Reveal your identity, you scoundrel!”

Oh, right. Those two older guys were here, too.

One of the two men pointing swords at me looked familiar. What was his name again…

“Jang Childeuk?”

Mr. Jang Childeuk, who had been working hard to manipulate public opinion at Honghwa Inn until just a few days ago, recoiled in terror.

“Gasp! How do you know my name?!”

“The jiangshi is talking! It’s bewitching people with its words!”

“…Who are you calling a jiangshi? Can’t you see I’m breathing just fine?”

The middle-aged man with the patchy beard glared at me and shouted.

“You evil creature! You can’t fool my eyes. If you were human, you couldn’t possibly be fine after falling from that height. Who sent you? The Demonic Cult? The Blood Cult? Or perhaps…”

“Taecho Village! Hyung, that jiangshi definitely said ‘Taecho Village.’”

“That’s right! You’re a jiangshi sent by Taecho Village!”

The middle-aged man shouted as if he had finally figured it out, then suddenly stopped and asked Childeuk,

“But where is Taecho Village?”

“I don’t know either.”

“…”

It would have been strange if he did.

I gave up on the conversation and wiped the dirt from my face with my sleeve.

The middle-aged man might not know me, but Childeuk knew my face well. This would be faster.

“Gasp! Third Young Master!”

“Yes. Long time no see.”

“Little brother, the Third Young Master? What in the world are you talking about?”

“The Third Young Master has become a jiangshi!”

“…”

Why was that the conclusion?

[^1]: A jiangshi is a reanimated corpse from Chinese folklore, often depicted as a hopping vampire.

[^2]: *Taecho* means “primordial” or “the beginning.”
## Chapter artifact 153

# Chapter 153

“So…”

Jang Childeuk continued haltingly.

“You were training?”

“Yes.”

“Were you perhaps practicing the Wall Lizard Technique?”

“I’m not entirely sure myself, but I think so.”

The Wall Lizard Technique. I’d seen it plenty of times in wuxia novels.

Apparently, it had been created by observing lizards climbing walls.

It was similar to the real-world sport of climbing, but there were two key differences.

First, unlike climbing, it used internal energy.

Second, there were no safety devices.

*This really is the Murim. No holding back.*

If you fell, you were as good as dead. It was the ultimate macho martial art.

When I nodded, the two men stared at me as though I were a ghost.

“From this height?”

“Is that even possible?”

“It worked.”

When I first heard Cheongpung suggest it, I had wondered what kind of insane nonsense he was talking about, too. But once I tried it, it worked.

It had only seemed unrealistic because I had never attempted it before. My body had already entered the realm of the superhuman—it would not be an exaggeration to say so.

“Oh, my. Third Young Master, what will you do if something serious happens to you?”

The middle-aged guy fussed as he brushed the dust off my clothes.

Only three minutes ago, he had treated me like a jiangshi from Taecho Village. Now he was handling me as carefully as though I were his family’s precious only son, three generations in the making.

“Well, why don’t you stop training for now and return to your quarters?”

“Why?”

“What do you mean, why? You were lucky this time, but if you fall one more time, you could really die.”

I waved a hand dismissively.

“It’s fine. It’s not like this was my first or second time.”

“What?”

“This is already the fifth time. Why are you acting surprised now?”

“The fifth… time?”

“Yes. Five times.”

His trembling eyes moved back and forth between me and the steep cliff.

“H-how are you still alive?”

“It’s fine. There’s someone who’s fallen more than ten times.”

“…”

“…”

“Looks like it’s about time for him to fall again… Oh, there he comes.”

I pointed toward a spot high up on the cliff. A black dot that grew larger by the second was followed by a piercing scream.

“Aaaaaaah! Caaaaaptain!”

The two men’s mouths fell open.

“My goodness. There really was someone else.”

“Who is that?”

“My right arm—no, my little toe.”

“What? What does that mean?”

“No, wait. Shouldn’t we save him right now?”

“Save him? Him?”

I shook my head.

Hyuk Mujin was a healthy adult man. If I tried to catch him as he fell from that height, it would end with more than just a broken bone somewhere.

“Just leave him alone. Don’t get involved and hurt yourselves.”

The two men screamed.

“He’s falling! He’s falling!”

“He’ll die if you leave him like this!”

“He won’t die.”

If he could die from this, he would have died ten times over by now.

But Hyuk Mujin had a lifeline—a sturdy rope that always saved him at the very last moment.

“Aaaaaaah!”

Hyuk Mujin’s scream drew closer by the second. At last, even his horrified expression became clearly visible.

That was when a streak of light flashed above us.

The thing plunging downward at meteor-like speed was glowing with a soft purple light.

“W-what is that…?”

“What is it?”

I answered briefly.

“The Zaha Divine Technique.”

More precisely, it was someone channeling the Zaha Divine Technique.

The two men could not see him, but I could clearly make out Cheongpung, wrapped in the distinctive purple qi of the Zaha Divine Technique.

He was grinning from ear to ear.

“Whoooooa!”

“…”

Look at that bastard having the time of his life.

His personality might have been a little unhinged, but when it came to ability, he was in a league of his own. I could only marvel at what happened next.

*How is that even possible?*

Shot forward like an arrow, Cheongpung snatched Hyuk Mujin by the waist in the blink of an eye.

Then he extended his palm toward the ground rushing up beneath them.

*Bang! Boom-boom!*

Once. Twice. Three times…

With each explosion of compressed air, the ground caved in.

Would this be what happened if an invisible giant pounded the earth with its fists?

Every time Cheongpung struck out with a palm, the frozen ground flipped over. The resulting recoil stopped the falling figure in midair.

A moment later, Cheongpung’s feet landed lightly on the ground.

“Whew, that was fun again. Right?”

Hyuk Mujin, already unconscious, groaned.

“Uhh… uhhh.”

“I knew you’d like it.”

“…”

How exactly did it look like he was enjoying himself?

Cheongpung cheerfully set Hyuk Mujin down, then acknowledged my presence.

“Oh, Benefactor! You’re still here?”

“I fell, remember? Thanks to someone.”

I glared steadily at Cheongpung.

In fact, I had already had several chances to reach the summit. The problem was that Cheongpung was not exactly a man in possession of an ordinary state of mind.

“Hehe. It makes me happy that you say it was thanks to me.”

“Shut up! I would’ve reached the top ages ago if you hadn’t done anything but interfere from up there!”

“Gasp! Please calm down, Benefactor!”

“Calm down? You should have said that before rolling rocks down at me!”

Think about it.

Climbing a cliff more than a hundred jang high with your bare hands was no easy feat to begin with. But every time I thought I had made decent progress, rocks the size of children came tumbling down from above.

Cheongpung’s innocent cries were an added bonus.

*Benefactor, rocks are rolling!*

Only someone who had experienced it could understand. Even if Shakyamuni himself had been in my position, he would have strangled that bastard to death with his prayer beads.

*Now that I think about it, I’m getting pissed off again.*

Should I just go at him?

Just as I clenched my fist, Hyuk Mujin, who had been lying on the ground and twitching only his fingers, suddenly sprang upright with a scream.

“Aaaaaaaah!”

“Hey, hey. Breathe. Take a breath. You’re on the ground.”

“Huff, huff. Am I really alive?”

“Yeah, you idiot. You’re still alive.”

“W-water, please.”

Cheongpung held out the bamboo tube hanging from his waist.

“Here.”

“Thank you…”

Hyuk Mujin absentmindedly accepted the bamboo tube, then froze stiff.

A moment later, a roar burst from him.

“You fucking bastard!”

Cheongpung recoiled in alarm at the sight of Hyuk Mujin running wild with his eyes rolling back.

“W-why are you suddenly acting like this toward me?”

“You’re asking because you don’t know? Captain, catch that bastard!”

“I’m only doing exactly what my grandfather taught me.”

“Get over here right now!”

“See you up there later, Benefactor!”

Cheongpung hurriedly backed away from Hyuk Mujin, then kicked off the ground.

*Boom!*

He shot more than ten meters into the air in a single bound, slapped onto the cliff, and began climbing with the Wall Lizard Technique.

*Papapapapak!*

Now that was a true veteran.

Cheongpung vanished so quickly that he looked as though he had been born walking on all fours. Hyuk Mujin sank to the ground.

“That bastard threw rocks at me. Rocks…”

I answered solemnly.

“I know. I saw you fall earlier. One hit you right in the eye.”

“He’s completely insane. He throws rocks as big as a child’s head.”

“That’s smaller than what he threw at me. He even threw dirt at me.”

“Captain. I’ve made up my mind.”

“About what?”

“I won’t give up until I catch that bastard and beat the shit out of him. I swear it on the name of Hyuk Mujin, a true man.”

Hyuk Mujin’s eyes burned fiercely.

I had never seen him so fired up. No matter what he was like inside, on the surface he had always been cheerful and carefree.

*Could this have been what he was aiming for?*

Was all of this Cheongpung’s way of drawing out Hyuk Mujin’s anger so that he would give it his all?

No. That nature-loving Huashan guy did not have the brains for that.

*Well, as long as it works out.*

I threw a bundle at the huffing Hyuk Mujin.

“Keep it secure inside your clothes.”

“What is this?”

“Fasting pills. I packed them before we started training.”

There was nothing better for replenishing hunger and energy. They were small and light, making them easy to carry, too.

“Eat them if you start running out of strength on the way up.”

“We’re surrounded by cliffs. Where am I supposed to eat fasting pills? I’m going up there right now and cutting that bastard down in one stroke…”

“You’ll be the one who dies in one stroke.”

Apparently, he wanted his newly learned Wall Lizard Technique to take him straight to Mount Beimang. I smacked Hyuk Mujin on the back of the head.

“Ow!”

“And it’s not like the cliff is sheer all the way up. There are ledges here and there, so find a place to stop and eat. Don’t fall because you’re in a hurry. Take it slowly, thinking only about succeeding in one attempt.”

“Hoo.”

“Then let’s go.”

“Yes, Captain!”

Hyuk Mujin and I were standing before the cliff with determined expressions when—

“Um…”

“T-Third Young Master.”

Right. These two were here, too.

Jang Childeuk and the middle-aged guy hesitantly opened their mouths.

“Would it be all right if we reported this to the Lesser Family Head?”

“Considering the circumstances… If you suffer even an injury, Young Master, then we…”

I raised a hand to stop them.

I could easily guess what they were going to say next. I knew the perspective of ordinary employees better than anyone.

“Report it, but…”

“But?”

“After your shift ends. How much time is left?”

“About three shichen.”

“That’s enough.”

It had already been half a day since I started climbing the cliff.

I intended to conquer this maddening cliff within the remaining three shichen.

* * *

This tall, steep, nameless cliff had endured the passage of time. Some sections were uneven, while others were smooth.

In some places, thick roots or rocks jutted out, making them easy to grab. In others, I had to wedge a single finger into a tiny crack and hang on.

*It would be much easier if I could use internal energy or a weapon, at least.*

With internal energy, even solid rock would crumble like tofu.

If I took a weapon from my inventory, I could drive daggers into the cliff like steps and climb that way.

The reason I was going through all this trouble instead of taking the easy route was because this was training…

Well, that was part of it. But every time I tried to use an easier method, Cheongpung would somehow sense it and drop rocks on me.

*Thud-thud-thud.*

A sudden shower of rock dust from above was an ominous sign.

Hyuk Mujin and I hurriedly covered our heads with our arms and shouted.

“We didn’t do anything! Seriously, we didn’t do anything! Don’t roll any rocks!”

“Uuughhh!”

A pale face cautiously poked out from above.

“Really?”

We nodded frantically.

We had not even made it halfway. If we were hit by a stone shower and fell now, all the bold claims we had made before climbing would become a humiliating memory.

“Please believe us!”

“Young Hero Cheongpung! No, Great Hero Cheongpung!”

“My grandfather always said that there must never be any tricks in training. Martial arts are gained through blood and sweat.”

After delivering a full speech, Cheongpung added one more sentence as though he were showing us mercy.

“I’ll let it go just this once.”

“…”

“…”

He was acting like an absolute tyrant.

Suppressing our outrage, Hyuk Mujin and I started climbing the cliff again.

We were in a situation where even the slightest mistake would send us hurtling back down below.

As a result, our senses grew sharper, and we had to pay tremendous attention to every single finger and toe.

*If it weren’t winter, I would have reached the top long ago…*

The higher we climbed, the more treacherous the slope became and the smoother the surface grew.

The cliff was already slippery enough. On top of that, the scattered snow flurries that came almost every day and the wind blowing in from the northern Gaoyuan had turned it into one enormous sheet of ice.

*I’m blocked. I can’t see a path at all.*

As I bit down on my lip, something suddenly caught my eye.

A crack in the rock blocked by a snowball that had not yet frozen.

It was a tiny space, barely wide enough for one finger. It would be difficult, but I had no other choice.

*Hup!*

I launched myself forward with a shout, simultaneously jamming my smallest finger—the little finger—precisely into the crack.

*Thud.*

My prediction had been only half right. I could break through the unfrozen snowball, but the crack was much shallower than I had expected.

It was barely one finger joint deep. And I had to support a body weighing 0.1 tons with my little finger.

“Ungh.”

Even for me, this was a bit much.

To make matters worse, my finger was slowly slipping because of the moisture pooled inside the crack.

*If I waste any more time, I’ll fall.*

There was not much farther to go. I steadied my breathing and calmed the tension in my body. Using my little finger as a support, I lifted my entire body.

Physical ability worthy of being called superhuman.

> **System**
>
> - **Strength** increased by 1.
>
> - **Agility** increased by 1.
>
> - **Stamina** increased by 1.

The stat increase came at exactly the right moment.

Just as I smiled triumphantly and reached toward the next crack—

*Hup!*

“Captain!”

Damn it. My breathing had faltered at the worst possible moment. I steadied my breathing again, but Hyuk Mujin continued shouting.

“Th-this! This!”

“What are you saying? I can’t hear you!”

The fierce snowstorm scattered both sound and visibility.

I was about to open my mouth again when a clear shout struck my ears.

“Above! Above!”

“Above?”

The fact that I could hear Hyuk Mujin’s voice meant the savage wind had paused. Only then did my obstructed vision clear and my ears open.

Following Hyuk Mujin’s gesture, I raised my head and finally saw it.

A massive boulder falling straight toward my face.

*Whoooosh!*

“Ah, shit.”

*Boom!*

* * *

“Wow. I can’t believe you broke such a huge boulder with your bare fist.”

I let Cheongpung’s admiration go in one ear and collapsed onto my back.

Only a moment ago, I had wanted nothing more than to beat that bastard senseless. Now I was completely drained.

*I made it up. It’s over!*

Just as I lay there, unable to move even a hand and cheering inwardly, a bluish, frozen hand reached the summit.

“Huff. Haaah.”

“You succeeded in only one day! You’re both incredible!”

If it weren’t for you, I would have done it in one shichen, you idiot.

I wanted to lay into him, but I was too exhausted to speak. As Hyuk Mujin and I panted from a mixture of accomplishment and fatigue, Cheongpung bowed deeply at the waist.

“You’ve both worked so hard! Now that you’ve succeeded once, you should be able to climb the remaining nine times much faster.”

“…”

“…”

The statement was so shocking that Hyuk Mujin and I stared at Cheongpung without even remembering to breathe.

*What is he talking about?*

Could he possibly mean what I thought he meant?

No, surely not.

As an intellectual of modern society, I opened my mouth with a calm demeanor.

“The remaining nine times? What kind of bullshit is that?”

“My grandfather…”

This guy was either a mountain hermit or a boy detective.

At that moment, Sword Saint be damned—I couldn’t help but see red.

“So you’re telling us to do this nine more times?”

“Yes!”

“You’re going to keep throwing rocks at us from up here?”

“Yes!”

“No.”

“What?”

Hyuk Mujin and I simultaneously collapsed onto the ground.

“I’m not doing it. I don’t even have the strength to go back down. Go ahead and gut me.”

“Gut me too, you vicious bastard!”

“Puhahaha.”

“Are you laughing?”

Cheongpung smiled brightly.

“Sorry. You looked just like me when I first started training, so I couldn’t help it.”

“See? You didn’t want to do it either!”

“No. I thought it was fun and wanted to keep going, but my body wouldn’t keep up.”

Hyuk Mujin muttered in a voice so quiet that only I could hear.

“…Is he insane?”

“So I told my grandfather. I asked whether I could continue the next day because my legs wouldn’t listen to me.”

As he reminisced about his happy past, Cheongpung suddenly drew his sword.

At the same time, purple Sword Energy shot forth.

*Shhk.*

Ice, dirt, rock—Cheongpung cut through all of it without distinction, then continued speaking.

“My grandfather answered that climbing up was difficult, but going down was easy. He said that if I endured it for just a little while, I would be back down in no time.”

*Rumble, rumble, rumble.*

The edge of the cliff ledge where Hyuk Mujin and I were lying—barely ten square meters in size—began to shake.

*Is this for real?*

As we lay there in a daze, Cheongpung waved at us.

“Nine more to go.”

> **System**
>
> - The Quest **Sword Saint Training: A Secondhand Experience** has been generated.
## Chapter artifact 154

# Chapter 154

The middle-aged martial artist and Jang Childeuk were staring at the sky again today—or rather, at the cliff.

“Say, Brother Jang. Have you ever learned the Wall Lizard Technique?”

“The Wall Lizard Technique? Good heavens, someone as timid as me would never even dare try it. What about you, hyung?”

“Once, about five years ago.”

“Why did you quit?”

“Had it been about three months since I started training in it? I misstepped and fell, and broke my ankle.”

“Oof. You must have fallen from somewhere pretty high.”

“Barely five jang or so. I trained for three months without missing a single day, and still broke my ankle.”

“That’s a shame.”

“A shame?”

“Who knows? If you’d kept learning, you might have become a master of the Wall Lizard Technique…”

“A master of the Wall Lizard Technique? Me? I can’t even break out of Second Rate with the sword techniques I’ve practiced all my life.”

The middle-aged martial artist let out a quiet laugh and pointed at the cliff.

“Whatever the martial art, you need talent to be called a master. Don’t you feel anything when you look at those two?”

“That’s certainly true.”

The two men watched the two figures swiftly climbing the cliff.

There was no mistaking them. Jin Taekyung and Hyuk Mujin were dedicating themselves to Wall Lizard Technique training again today.

*Thud-thud-thud-thud!*

Stones and snowballs came tumbling down from far above.

At that very moment, both men were thinking the same thing.

*Are those people or lizards?*

Their hands and feet moved without hesitation as they climbed the nearly vertical cliff.

The difference in speed between them was considerable, but considering how long they had been training, their progress was truly remarkable.

“How many days has it been now?”

“Let’s see. This is our third shift, so… exactly our third day.”

“Only three days. If I had trained for a year instead of three months, could I have learned the Wall Lizard Technique to that extent?”

“…”

The answer to that question was known to both the middle-aged martial artist and Jang Childeuk.

After a brief silence, Childeuk spoke.

“Hyung.”

“Hmm?”

“What can people without martial talent do?”

“We’re useless. Get out the jerky.”

“Yes, sir.”

Jang Childeuk quickly pulled out some jerky and a bottle of liquor from inside his robes. He was adapting rapidly to his post guarding the training hall—the Jin Family of Taiyuan’s cushiest assignment.

* * *

*Whoooosh!*

I pressed myself tightly against the cliff and dodged the boulder plummeting downward at terrifying speed. Far above, I could see Cheongpung looking disappointed as he smacked his lips.

*I knew this would happen, you bastard.*

As if this were the first or second time I’d been subjected to this.

I might have been bad at book learning when I was young, but when it came to learning through my body, I had been unrivaled.

“Haaaargh!”

Hyuk Mujin, on the other hand, was a little slower. Compared to me as I was now, there was a clear difference in level, so perhaps it was only natural.

I shouted toward Hyuk Mujin, who was crawling up from far below.

“Mujin, you okay?”

“No!”

“...Oh. Right.”

What a brutally quick answer.

Of course he wasn’t okay, but most people would say they were fine even as empty courtesy. Hyuk Mujin had no such habit.

“Quit whining and get up here!”

“My entire body is cramping! I barely dodged that one just now!”

For all his complaining, he was keeping up fairly well. This training had confirmed it once again: Hyuk Mujin had a decent amount of persistence and martial talent.

“We’re almost there. Grit your teeth and climb!”

I wedged myself into a hollow in the cliff and took a moment to catch my breath.

*Open the Quest window.*

*Ding.*

> **System**
>
> **Quest**
>
> **Sword Saint Training: A Secondhand Experience**
>
> A master is forged through countless rounds of tempering and hammering.
>
> Cheongpung, who received harsh training from the Sword Saint, will revive his childhood memories and put you through training!
>
> **Grade:** Peak
>
> **Restriction:** Those who have Cheongpung’s permission
>
> **Mission:** Climb the cliff 10 times (9/10)
>
> **Reward:** Acquire **Wall Lizard Technique**
>
> **Cheongpung** is extremely pleased.
>
> **???**
>
> **Failure:** Injury or death
>
> **Cheongpung** is extremely saddened.

Today marked exactly three days since we started climbing this damned cliff.

Only one climb remained before the Quest was complete, but I still couldn’t let my guard down.

Because of this psychopath who looked like he wanted to drop a boulder straight onto my face at any moment.

The first climb had been hard enough, but Cheongpung’s interference had grown more intense with every round.

I curled up as tightly as I could and shouted.

“Benefactor! Where are you? Show me your head!”

“No! Get lost!”

“Oh, there you are! I ran out of things nearby that were good for throwing, so I was delayed while I went to find more!”

“What do you mean, find more? If you ran out of rocks, just don’t throw anything!”

“But… if I don’t do this, you won’t be able to properly learn the Wall Lizard Technique, Benefactor!”

“…”

Was this guy insane?

How many people in the world learned the Wall Lizard Technique while getting pelted with rocks?

Just as I was rendered speechless by the sheer absurdity of it, a battered hand shot up into the hollow where I was hiding.

It wasn’t the hand of some ghost that had died here long ago while learning the Wall Lizard Technique.

Naturally, it was Hyuk Mujin.

“Haaaargh. I’m dying.”

When you were truly exhausted, you couldn’t even speak. You got so out of breath that your head rang, and even breathing made your chest ache.

Even so, Mujin still looked like he had plenty of life left in him. He crawled over beside me, then spread his legs wide.

“Hey, it’s cramped.”

“Am I the only one cramped, Captain? I’m cramped too.”

“Pull your legs in or move over. This is basically a one-person seat.”

“Ah, I’m too tired. You move over, Captain. Aren’t you being a little too harsh on your right-hand man after he worked so hard to get up here?”

“I’m nice to my right arm. But you’re my little toe, so I can afford to be a little harsh.”

“Wow, you’re really going to be like this? This is the only place where we can avoid the rocks. Would it make you feel better if I just jumped out and got one straight to the face?”

I answered with a perfectly serious expression.

“Why would you say that? Of course not.”

“Oh, wow. What’s gotten into you all of a sudden, Captain…”

“I’d feel stifled and guilty for a while. But after a year, I’d be fine. After ten years, I’d have forgotten your face.”

“...You’re awfully realistic.”

“That’s life, punk. Now pull your legs in. Otherwise, you might give me something to feel guilty about.”

“Yes, sir.”

Manspreaders could get their skulls cracked by a rock for all I cared. That was what they got for manspreading.

Hyuk Mujin pulled his legs tightly together, caught his breath, and sighed.

“No matter how I think about it, this is insane.”

“What is?”

“Cheongpung is insane for making us do this, and I’m insane for agreeing to do it.”

“You’re doing pretty well for someone who thinks it’s insane.”

“I’m just fighting like my life depends on it.”

“That’s the answer.”

“What?”

“Going at it like it’s do or die. That’s the answer. Later, when death really is staring you in the face, you’ll regret this moment.”

I tied back my disheveled hair and continued.

“Ah, I should’ve worked harder back then. You know, that kind of regret.”

I prided myself on having worked so hard as a Hunter that I had practically shit blood. But even after doing all that, regret was what remained.

Regret always came too late. It only struck with bone-deep pain after you had lost something precious.

“Your life, your wealth, or someone you care about. If you don’t want to lose something precious, put your life on the line now. Working yourself to death while you’re alive is still better than actually dying, isn’t it?”

“Uh…”

Hyuk Mujin stared at me with round eyes.

“You’re talking like someone who’s been through it.”

“Why? Is that strange?”

“Words feel different depending on whose mouth they come from. The Captain I know is, um…”

“Not exactly someone who should be saying that, having grown up as a young master with nothing to envy?”

“If I had to put it that way, then yes. You look like someone who’s never lost anything precious in his life, but you talk like a battle-hardened veteran who’s been through every possible hardship.”

This guy had pretty good instincts.

Or maybe that was how I looked to everyone else, too.

I simply let out a quiet laugh without answering. Hyuk Mujin studied me suspiciously.

“What’s with that laugh?”

“I was just thinking you’re pretty perceptive.”

“Captain, you’re not a fake, are you?”

“What?”

“It’s a little late to bring this up, but… you’ve changed too much. Your personality, your martial arts—everything. You’re like a completely different person.”

“Haven’t you heard the rumors? I’m a secret weapon secretly raised by the Jin Family of Taiyuan.”

“Rumors are just rumors—unverified ones. Plenty of people saw you carousing and wasting your time, Captain.”

“You were one of them?”

“Yes. At first, I thought you might be wearing a human-skin mask, but that doesn’t seem to be it.”

“A human-skin mask? The kind where you peel the skin off someone’s face and wear it?”

“See? You ask again as if you’re hearing about it for the first time. You also say things that make no sense all the time.”

“Hmm.”

Come to think of it, at some point I had stopped worrying so much about avoiding suspicion. Everyone around me thought I was Jin Taekyung of the Jin Family of Taiyuan. I had also long since accepted my Murim self as part of who I was.

“If I’m right, and you’re some kind of double put forward by a shadowy organization like the ones in wuxia novels, tell me now. I’ll let it slide quietly.”

“What an absurd thing to say. Then you should report me immediately.”

“Well, I like you much better now than I did before. And I owe you my life. Hehe.”

His lips were smiling, but it wasn’t a joke. The subtle movement of his throat as he swallowed and the slight tremor in his eyes were proof.

I thought for a moment, then opened my mouth.

“Want me to tell you honestly?”

“H-honestly?”

“I’ve been itching to tell someone anyway, so this works out. And the location is perfect.”

Hyuk Mujin glanced around anxiously.

The hollow in the cliff was just large enough for two people to plant their backsides. As luck would have it, the lunatic who would drop a rock on us the moment we stuck our faces outside was waiting nearby, too.

It was the perfect place for two people to sit until one of them died without anyone ever knowing.

“You really are stupid, aren’t you?”

Hyuk Mujin swallowed hard.

“C-C-Captain. I don’t care who you are.”

“Too late.”

“Gasp! I won’t say anything! I meant what I said earlier!”

“What if I told you I belonged to the Demonic Cult?”

“The Demonic Cult!”

“I’m only going to say this once. Listen carefully.”

“I’ll pretend I didn’t hear it. No, I won’t listen!”

Hyuk Mujin’s face turned deathly pale as he tried to cover his ears, but my words came a moment faster.

“I’m actually from another world.”

“...?”

“People can talk to each other even when they’re ten thousand li apart, and monsters with horns or wings roam everywhere. If you put it in Murim terms, I suppose you’d call them evil spirits.”

“...What?”

“Anyway, somehow I ended up here from that kind of world. Then strange things started appearing before my eyes, and suddenly—Level Up! Bam! Points! Boom! Ding-ding-ding-ding inside my head!”

“…”

“Anyway, I only entered the world of martial arts two or three months ago. I’ve wiped the floor with dozens of First Rate masters and taken down three Peak masters. So, any questions?”

Hyuk Mujin slowly lowered the hands that had been half-covering his ears.

His expression was complicated, a mixture of irritation and relief.

“Whew. Let’s just say I was wrong. Happy now?”

“Why? It’s the truth. You don’t believe me?”

“Not even a stray dog would believe that. If only my martial arts were stronger…”

*Smack!*

After smacking him on the back of the head, I stood up.

It was a true story, but it didn’t sound true.

Of course, I had expected Hyuk Mujin to react this way. That was precisely why I had told him.

Someone coming from another world? Anyone would think that was ridiculous.

“Nevel-up? Poin-two? Good grief, I should just stop talking. I don’t know what I expected from you, Captain.”

“What did you expect? The Demonic Cult? The Blood Cult?”

“Oh, come on! Just stop!”

I grabbed Hyuk Mujin by the shoulder as he stood up. The next instant, a murderous shriek of displaced air filled the space, and a boulder as tall as a grown man shot past us.

“Watch yourself. We still have a long way to go.”

I patted him on the back and started climbing the cliff again.

We were only halfway to the summit.

* * *

The moment Hyuk Mujin and I finally reached the summit, System notifications burst forth like celebratory cannon fire.

*Ding. Ding. Ding.*

> **System**
>
> - **Cliff climb:** 10 times (10/10)
>
> - Quest successfully completed!
>
> - New martial art, **Wall Lizard Technique**, is now activated!
>
> - Because you achieved outstanding results that exceeded expectations, you will receive an additional reward!
>
> - Level Up!
>
> - You have acquired 10 Stat Points and 10 Skill Points!
>
> - The Title **Beginner Trainee** has been upgraded to **Intermediate Trainee**!
>
> - Open the relevant System window to check and apply the changes.

Cheongpung beamed at us.

“Wow! You really did it!”

“...What’s that supposed to mean?”

“By any chance—”

*This bastard. Don’t tell me…*

At the sharp look the two of us gave him, Cheongpung shook his head.

“It’s nothing. It took me fifteen days, you see. I didn’t expect you to finish so quickly.”

“Fifteen days?”

Hyuk Mujin repeated the number, then stared at me in disbelief.

Who was Cheongpung? The Sword Saint’s successor, a Peak master who had defeated Jin Mukyung. It was only natural that Mujin couldn’t believe we had achieved this faster than he had.

But…

“What are you so happy about, punk? We’re not the same age. Right?”

“I wasn’t even that young! I was already ten years old!”

“...Isn’t ten usually considered young?”

Cheongpung smiled brightly as he reminisced about those days.

“Back then, climbing up Falling Goose Peak and falling back down was part of my daily routine. It was so much fun.”

“Falling Goose Peak?”

“It’s a peak on Huashan. It’s comfortably more than five hundred jang high. Oh, of course, I couldn’t climb all the way to the top until I was eighteen.”

“…”

“…”

Wasn’t he too young even to watch a movie rated fifteen-plus?

At that age, he would’ve only been in third grade—barely old enough to count as a snot-nosed schoolkid.

*When I was that age, I was playing on the jungle gym in the school playground…*

That bastard Cheongpung had been playing on the mountain peaks of Huashan.

As expected of the continent. The scale was completely different.

“Anyway, you both worked incredibly hard. You achieved something amazing!”

Cheongpung clapped excitedly all by himself, then continued.

“So, about that…”

Sensing something ominous, Hyuk Mujin hurriedly cut in.

“No. Hold on. Wait just a second.”

“I know lots of other fun training exercises.”

“Hey! I said wait a second!”

Hyuk Mujin lunged at him with a shout, but it was already too late. Cheongpung effortlessly subdued him with a grappling technique and called out energetically,

“Let’s all give it our best!”

*Ding.*

> **System**
>
> - **Cheongpung** is in extremely high spirits over your outstanding achievement!
>
> - As a special reward, the linked Quest **Sword Saint Training: A Secondhand Experience—2** has been generated!

“You bastard! Let go of my arm right now!”

As I listened to Hyuk Mujin shout, a question suddenly occurred to me.

*How many of these linked Quests are there?*

One thing was certain.

There was no way Cheongpung would stop at a measly two.

*He’s going to work us into the ground.*

I left Hyuk Mujin’s shrill shouting behind and looked up at the sky.

The vast sky was an intense blue. The air was cool, and several hawks floated overhead with their enormous wings spread wide.

New Year’s Day was ten days away.

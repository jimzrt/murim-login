# Checkpoint Review — 130–134

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

# Chapters 130–134

## Plot

Cheongpung, an eccentric young Peak master who recently fled Huashan’s Lotus Peak, travels toward Taiyuan after briefly joining a Seongun Escort Bureau escort run. At Honghwa Inn, he meets Jin Taekyung and Hyuk Mujin and begs for candied hawthorn skewers because he has not eaten all day. Taekyung feeds him, learning that Cheongpung was raised in the mountains by his grandfather and came down to test himself against the Ten Dragons and Phoenixes. Taekyung cannot identify Cheongpung’s Level through Qi Sense; his System Window displays `???`.

Five First Rate heirs of the current Five Gates of Shanxi mock Cheongpung, Taekyung, and Mujin from the inn’s second floor, then refuse to apologize. Their spokesman, Woo Jintae, heir to the Seongun Escort Bureau, is publicly slapped and humiliated by Taekyung, who fabricates the identity Tien Shinhan of the Dodong Sect when challenged about his affiliation. The other heirs—Seongryong, Cheonwoo, Myeonghwa, and Sohye—refuse to fight Taekyung. Mujin warns them that they will be next, secures their apology to Cheongpung, and orders them to prostrate themselves.

Woo Jintae had been using the Seongun Escort Bureau’s wealth, gifts, and hospitality to control the current Five Gates scions before their scheduled luncheon with Shanxi’s ten-year-old Prince City Lord. The luncheon, already locked in as The City Lord’s Invitation Quest, is due to take place the following day.

## Continuity

- Cheongpung is an exceptionally young Peak master with an undetectable Level, an innocent and eccentric personality, and a strong appetite. He was raised by his grandfather in the mountains from age five, and his grandfather repeatedly relocates because people keep finding him.
- Cheongpung recently left Huashan’s Lotus Peak and descended from the mountains to determine whether he or the Ten Dragons and Phoenixes are stronger. His status at Huashan, his grandfather’s identity, and his precise affiliation remain unresolved.
- Hyuk Mujin has returned to Taiyuan after five years. His parents are healthy textile merchants who own the city’s largest textile shop, with branches in Henan and Hebei.
- Woo Jintae is the married, nearly thirty-year-old heir and sole male heir in three generations of the Seongun Escort Bureau. He cultivated the current Five Gates scions through lavish hospitality, gifts, and bribes.
- The current Five Gates of Shanxi are an alliance of more than twenty small and medium-sized sects formed after the former Five Gates—including the Samdo Sect and Gunggui Sect—were annihilated at the Battle of Eight Spring Gorge for serving the Head Elder.
- The five scions are Seongryong, Cheonwoo, Myeonghwa, Sohye, and Woo Jintae. They are pampered First Rate martial artists; Jintae is Level 45 and served as spokesman.
- Taekyung has publicly humiliated Jintae and claimed the fabricated identity Tien Shinhan of the Dodong Sect. The other four scions apologized to Cheongpung and were ordered by Mujin to plant their heads on the floor; whether they obey and what consequences follow remain unresolved.
- The City Lord’s Invitation Quest requires Taekyung’s attendance at the next day’s luncheon with young prodigies. The City Lord is a ten-year-old Zhu Prince and the Emperor’s youngest brother; Woo Jintae and the Five Gates scions are also expected to attend.
- Taekyung still intends to reject Lee Seowol’s marriage proposal because he loves Song Song. The Mount Heng Sword Sect’s reconstruction, the Temporary Strength Pill and Dark Heaven, Pung Yang’s wider consequences, and the Fire King’s status remain unresolved.

## Translation Decisions

- Render 성운표국 as **Seongun Escort Bureau**, 표행 as **escort run**, 쟁자수 as **porter**, 표두 as **Escort Chief**, 은원보 as **silver ingot**, 은자 as **nyang of silver**, 사서삼경 as **the Four Books and Three Classics**, and 연화봉 as **Lotus Peak**.
- Render 빙당호로 as **candied hawthorn skewers**, with an explanatory footnote.
- Render 개방 as **Beggars’ Sect**, 삼도문 as **Samdo Sect**, 궁귀문 as **Gunggui Sect**, 산서오문 as **Five Gates of Shanxi**, and 십봉룡 as **Ten Dragons and Phoenixes**.
- Render 우진태 as **Woo Jintae**, 우 소협 as **Young Hero Woo**, 황 소저 as **Young Lady Hwang**, and 혁 아우 as **Little Brother Hyuk**.
- Render 도동파 as **Dodong Sect** and 천진반 as **Tien Shinhan**, preserving Taekyung’s fabricated identity joke.
- Render 대가리 박으십쇼 as **“bend over and plant your heads on the floor,”** retaining Mujin’s blunt comic coercion.
- Render 촉금 as **Shu brocade**, and retain **First Rate**, **Peak**, **City Lord**, **Prince**, and **The City Lord’s Invitation**.

## Durable state

{
  "active_continuity": [
    "Pung Yang is dead; Jin Taekyung killed him after the Unnamed Sword's Ten-Thousand-Year Cold Iron destroyed his Body-Protecting Qi and pierced his chest.",
    "Taekyung fully absorbed the Blazing Flame Divine Pill and possesses forty-five years of internal energy with the Scorching Yang Qi attribute.",
    "Jin Mukyung survived his fight with Pung Yang and returned to the Jin Family of Taiyuan, but remains incompletely recovered.",
    "Cheol Mubaek remains severely injured and needs extended recuperation; Lee Seowol remains the seventeen-year-old Sect Leader of the Mount Heng Sword Sect and vows to preserve it.",
    "The Lower District Sect sent a relief force after the battle; Wolhwa's real name is Eun Sowol, and she is its Shanxi Branch Leader.",
    "Lee Seowol accepted the Jin Family of Taiyuan's New Year invitation, offered the Mount Heng Sword Sect's territorial rights as an apology, and proposed marriage to Taekyung in exchange for three Peak martial arts; Taekyung plans to reject her because of her age and because he loves Song Song.",
    "Forty-seven mounted bandits survived the battle, but the Lower District Sect can save only about thirty; it is spreading a rumor that the two Jin brothers defeated Pung Yang and rescued Mount Heng.",
    "Cheol Mubaek and Lee Cheonbaek became close friends after first meeting and fighting more than thirty years ago; Cheol is the ninth-generation successor of the Shura Annihilating Fist.",
    "Jopil is dead and left behind the Supreme Peak martial art Flame Divine Palm; the Fire King and the status of the Fire Gate Clan's single successor remain unknown.",
    "The Temporary Strength Pill is in Taekyung's Inventory and has been revealed to Jin Wikyung, Jin Mukyung, and Wipeng; its System description identifies Dark Heaven as its manufacturer and records its unknown Grade, Peak restriction, temporary power increase, +100 combat stats, fifteen years of internal energy, and Body-Protecting Qi effect.",
    "Jin Wikyung and Wipeng traveled to Sakju with fifty elite guards after receiving an emergency report about Pung Yang, the Red Wind Band, the Mount Heng Sword Sect, and the Jin brothers; the Jin Family displayed a large Sakju banner celebrating the safe return of Mukyung, Taekyung, and Hyuk Mujin.",
    "Taekyung, Mukyung, Wikyung, and Wipeng drank through the night for three days; Wipeng is called the God of Drinking and Taekyung is rumored to be the Night King.",
    "Taekyung's Sleeping Dragon of Shanxi Title effect strengthened to all stats +15 and Fame +200; his current Status Window shows Level 61, Fame 2,100 (+250), and 60 remaining points.",
    "Hyuk Mujin accepted The City Lord's Invitation, requiring attendance at the City Lord's luncheon with young prodigies tomorrow.",
    "The City Lord of Shanxi Province is a ten-year-old Prince and the Emperor's youngest brother, appointed at age five; Jin Mukyung met him after being summoned three years earlier and considered the encounter a nightmare.",
    "Cheongpung is an eccentric former porter who recently fled Huashan's Lotus Peak and traveled toward Taiyuan; he is an exceptionally young Peak master whose Level Taekyung cannot determine through Qi Sense, lived with his grandfather in the mountains from age five, and came down to test himself against the Ten Dragons and Phoenixes.",
    "Hyuk Mujin's parents are healthy textile merchants in Taiyuan who own the city's largest textile shop, with branches in Henan and Hebei; Mujin left home to avoid inheriting the business, and a younger sibling later removed that obligation.",
    "Taekyung has begun treating Hyuk Mujin as a valued companion rather than merely a subordinate, acknowledging the hardship Mujin endured while traveling with him.",
    "Woo Jintae is the married, nearly thirty-year-old heir and sole male heir in three generations of the Seongun Escort Bureau; he cultivates the current Five Gates scions through lavish hospitality, gifts, and bribes.",
    "At Honghwa Inn, Taekyung repeatedly slapped Woo Jintae after Jintae refused to apologize; the other Five Gates scions apologized to Cheongpung after Mujin's intervention, and Mujin then ordered them to prostrate themselves."
  ],
  "continuity_sources": [
    134,
    133
  ],
  "open_questions": [
    "How will the Jin Family of Taiyuan respond to Lee Seowol's proposed transaction and territorial transfer?",
    "Can Lee Seowol preserve or rebuild the Mount Heng Sword Sect with so few survivors?",
    "What are the Temporary Strength Pill's exact price and long-term aftereffect, and is it related to the Demonic Cult's Blood-Exploding Pill?",
    "What is Dark Heaven, and why do Jin Wikyung and Wipeng refuse to discuss it?",
    "What consequences will Pung Yang's death have for the Red Wind Band and the wider Murim?",
    "Is the Fire King still alive, and if so, where is he?",
    "Will the Five Gates scions obey Hyuk Mujin's order, and what will happen at the City Lord's luncheon?",
    "What was Cheongpung's status at Huashan's Lotus Peak, who is his grandfather, and what are the individual sect affiliations or family names of the Five Gates scions, including the Wang Family Estate heir and Young Lady Shin?"
  ],
  "safe_through": 134,
  "temporary_decisions": [
    "Render 잠력단 as Temporary Strength Pill and 폭혈단 as Blood-Exploding Pill.",
    "Render 만년한철 as Ten-Thousand-Year Cold Iron and 이름 없는 검 as Unnamed Sword.",
    "Render 열화신단 as Blazing Flame Divine Pill and 반 갑자 as half a jiazi, clarified as thirty years of internal energy.",
    "Render 완전 회복 as Full Recovery and 회광반조 as final rally in this death-and-recovery context.",
    "Render 운칠기삼 as seven parts luck and three parts skill, and 운구기일 as nine parts luck and one part qi, with a footnote explaining the variation.",
    "Render 은공 as Benefactor, 절정 무공 as Peak martial arts, 급식 as school lunch, 고딩 as high schooler, 철컹 as clank, 산서성 as Shanxi Province, 총지부장 as Chief Branch Leader, 원단 as New Year's Day, 갑자 as jiazi, 시진 as shichen, 표행 as escort run, 쟁자수 as porter, 표국 as Escort Bureau, 표두 as Escort Chief, 은원보 as silver ingot, 은자 as nyang of silver, 사서삼경 as the Four Books and Three Classics, and 연화봉 as Lotus Peak.",
    "Render 일인전승 as single successor, 비인부전 as transmission only to the worthy, 구 대 계승자 as ninth-generation successor, 천하십대권법 as the ten greatest fist techniques in the world, 열화문 as Fire Gate Clan, 화왕 as Fire King, 삼성 as Three Saints, 십왕 as Ten Kings, 진무보법 as Jin Family's Manoeuvre Technique, 아이템창 as Item Window, 전서응 as messenger eagle, 고원 as Gaoyuan, 구주 as Nine Provinces, 사술 as dark arts, 마기 as demonic qi, 선천지기 as innate qi, 소음인 as Soeumin, 태양인 as Taeyangin, 암천 as Dark Heaven, 주신 as God of Drinking, 야왕 as Night King, 화주 as fire liquor, 화북 as North China, 현령 as county magistrate, 성주 as City Lord, 장 노인 as Old Man Jang, 적토마 as Red Hare, 여포 as Lü Bu, 성주의 초청 as The City Lord's Invitation, 친왕 as Prince, 주씨 as Zhu, 천자 as Son of Heaven, 황상 and 황제 as Emperor, 태자 as Crown Prince, 구파일방 as Nine Sects and One Gang, 오대세가 as Five Great Families; render 개방 as Beggars' Sect and 십봉룡 as Ten Dragons and Phoenixes.",
    "Render 빙당호로 as candied hawthorn skewers with an explanatory footnote; render 산니백육 as Garlic Pork, 어향육사 as Fish-Fragrant Shredded Pork, 경장육사 as Beijing Sauce Shredded Pork, 규화계 as Beggar's Chicken, 매구 as Maegu, 매채구육 as Maechae Guyuk with a footnote explaining the abbreviation, 촉금 as Shu brocade, 삼도문 as Samdo Sect, and 궁귀문 as Gunggui Sect.",
    "Render 도동파 as Dodong Sect and 천진반 as Tien Shinhan, preserving Taekyung's fabricated identity joke."
  ],
  "version": 1
}

## Reading copies

## Chapter artifact 130

# Chapter 130

Winter in the borderlands was harsh. A middle-aged man shivered violently as the knife-sharp wind cut through his collar.

“Ugh, it’s cold as hell.”

The man, Seokchil, was a porter for the Seongun Escort Bureau in southern Shanxi Province.

He had spent more than a day and a half hauling a cart loaded with over a hundred geun of cargo, soaking his entire body in sweat. Whenever he took a brief rest, as he was now, he had to fight against the brutal cold.

“Hyung, hurry up and leave the cart. Come warm yourself by the fire before you freeze to death.”

A fellow porter, already crouched in front of the campfire, called out. Seokchil answered gruffly as he walked over.

“Brat, I have five mouths to feed. I’ve got a long way to go before I’m ready to die.”

“True. You can’t die when you’ve got a fox of a wife and rabbit-like children waiting for you.”

“What do you mean, fox? She’s a bear. A bear.”

“Was that a deathbed confession? If your wife hears you, she’ll wring your neck.”

“You can curse the king behind his back. What, you didn’t know that?”

Seokchil moved closer to the campfire.

They used horse manure for firewood, so a foul smell spread in every direction. But after nearly twenty years as a porter, Seokchil was as used to it as he was to the smell of cooking rice.

“Ah, now I feel like I can live again.”

“But Hyung, aren’t you being a little stingy?”

“Huh? What kind of nonsense is this?”

His fellow porter grinned and jerked his chin toward something.

“You should bring the rookie over, too. Where’s the sense in rushing over here to save yourself alone?”

Seokchil, who had been warming his frozen hands, turned his head. At the end of his gaze sat a young man on a snow-covered rock, staring blankly into space.

*That kid’s doing it again.*

The young man was a new porter they had picked up in Henan. Escort Chief Song, the person in charge of this escort run, had said that the young man seemed capable enough to earn his keep, so they had taken him on.

*Well, people are always in short supply.*

The problem was that the young man often sat around like this, completely lost in thought, and no one had the slightest idea what was going on inside his head.

As Seokchil clicked his tongue, his fellow porter asked,

“Why? Is he a little strange?”

“He does his work well. He’s surprisingly strong for someone who doesn’t look like much.”

“Then what’s the problem?”

“What do you mean, what’s the problem? It’s frustrating seeing a young fellow sit around like that every day. Back when I was his age…”

“You want to say you had dreams of making your mark on the world and worked hard every day?”

“Of course. A man should know how to set a grand goal and move toward it.”

“I assume that grand goal wasn’t becoming the greatest porter under heaven.”

“You little—”

At Seokchil’s furious reaction, his fellow porter quickly changed the subject.

“By the way, what’s that fellow’s name?”

“Cheongpung.”

“Wow, what a great name. It suits him, too.”

“That’s true.”

Seokchil secretly disliked the young man, Cheongpung, but he had to agree completely.

There was something about the young man’s open, gentle features and clear eyes that made people feel strangely at ease and calmed their anger.

“Hey, rookie!”

At his fellow porter’s shout, Cheongpung turned his head.

“Me?”

“Who else would I be talking to? Come over here and warm yourself by the fire. If you keep sitting there, your butt will get ripped right off.”

“An experience like that wouldn’t be bad.”

“An experience? What experience?”

“The experience of having my butt ripped off. I’ve never had that happen before.”

His fellow porter was silent for a moment before whispering to Seokchil,

“What kind of guy is he?”

“I don’t know. The kid’s a little strange. Maybe he ate something bad.”

Cheongpung tilted his head.

“I ate two dumplings this morning.”

“……You’ve got sharp ears. Fine, just come sit down.”

“Should I?”

Cheongpung trudged over and sat down in front of the fire. The usual questions immediately began flying at him.

“Where are you from?”

“Henan.”

“So you’re from Henan.”

“I was in Hubei a month ago.”

“Hmm. Hubei’s nice, too.”

“Before that…”

The porter turned to Seokchil.

“This guy’s unbelievable.”

“Right? I feel like I’m becoming strange myself whenever I talk to him.”

“How have you lasted over a month with someone like him beside you?”

“That’s why I stopped talking to him lately. Has it been about three days since our last conversation?”

Cheongpung answered with a serious expression.

“Four days and three shichen.”

“……”

“……”

The two men barely managed to suppress their urge to smack Cheongpung over the head.

“So where are you from?”

“I lived in the mountains.”

“That’s not what I meant… No, never mind. Thank you for answering that, at least.”

“You’re welcome.”

Strangely, Cheongpung’s bright smile made their anger subside.

His unpredictable, bizarre remarks were paired with an innocent smile like a child’s. Their curiosity about this strange young man, unlike anyone they had ever seen, continued to grow.

“But you said you lived in the mountains?”

“I mean exactly what I said. I farmed and gathered medicinal herbs in the mountains from the time I was young. I did various other things, too.”

The two men jumped to the conclusion that Cheongpung was from a slash-and-burn farming community.

Most slash-and-burn farmers went into the mountains to escape the cruelty of vicious landlords or to avoid the authorities after committing one crime or another.

“You must have had a hard life.”

“But I had fun.”

“Oh, really?”

Could life as a slash-and-burn farmer really be fun? The thought briefly crossed Seokchil’s mind, but he saw no reason to ask.

“Then what made you come down from the mountain?”

“Life in the mountains got boring. I wanted to see the world, and there were people I wanted to meet.”

“So that’s why you came to Henan.”

“Yes. It turned out to be a wasted trip, but… things aren’t bad now, either. This escort work is pretty interesting, too.”

“You find escort work interesting?”

Cheongpung answered with a broad smile.

“Watching people is interesting. Looking at the land and the sky is interesting, too. Thinking is fun.”

To Seokchil, who had worked as a porter for so many years, these were all sights he was sick to death of seeing.

People worn down by exhaustion and worries about making a living. Damp earth and knife-sharp winds that blew like mad. His mind was filled with only one thought: how much pay he would receive for this escort run.

*Well, he’s still young. That’s the only reason he can say something like that.*

Besides, he had lived in the mountains his entire life and came from a slash-and-burn farming community. It made sense that he would feel this way.

Wouldn’t he learn about the harsh realities of life soon enough and gradually become just like Seokchil as he grew older?

*I used to be like that, too.*

Seokchil looked at Cheongpung with a mixture of envy and pity before opening his mouth.

“Just listen to this as the ramblings of an old man.”

He knew he was meddling where he wasn’t wanted, but he wanted to show this innocent young man the realities of life.

Wasn’t his life too promising to begin and end as a porter?

“Anything seems worthwhile for a while. But after ten or twenty years, you stop seeing much of a future ahead of you. No matter how hard a porter works or how talented he is, he’s still a porter. You should learn even Third Rate martial arts at a local martial arts academy and start working as an escort. You’d be much better off.”

Cheongpung blinked.

“Oh, really?”

“Not ‘oh, really?’ I’m telling you to do it. You’re a little old to start learning martial arts, but who knows? Maybe you have exceptional talent and could become a successful First Rate master.”

“A First Rate master…”

His fellow porter, who had been listening quietly, clicked his tongue.

“Isn’t that giving him too much false hope? A First Rate master isn’t some dog’s name.”

“I’m speaking hypothetically. What kind of sense does it make for someone his age to be satisfied with being a porter?”

“Well, you’re right about that. If I were ten years younger, I wouldn’t be sitting here either.”

“See?”

Seokchil patted Cheongpung on the shoulder.

“You heard him, right? Save carefully for a year or two and enroll in a martial arts academy. It’ll be much better for you. Until then, I’ll teach you everything I know.”

Cheongpung tilted his head.

“A year or two?”

“What? Is that too long? You don’t know how the world works, so I suppose you don’t realize that martial arts academy fees aren’t cheap. Even if you take the lowest estimate, it’ll take a year to…”

“No, because I’m going to quit before then.”

“You’re quitting? When?”

“Now.”

“Huh?”

“What?”

Cheongpung smiled brightly.

“I don’t know the way to Shanxi Province. There happened to be an escort run heading to Shanxi, so I asked them to let me tag along.”

“……And?”

“We’ll reach Taiyuan after one more day, so I was planning to part ways around then.”

Seokchil and his fellow porter looked at each other with expressions that seemed to ask whether this was some kind of joke.

“What the hell? Didn’t Escort Chief Song say he signed a one-year contract?”

“That’s what I heard, too. That’s why they assigned him to the most experienced porter, so he could learn from him.”

With a confused expression, Seokchil asked Cheongpung,

“When you joined us in Henan, you signed something, didn’t you?”

“Oh, yes.”

“If you have it, show it to me.”

Cheongpung pulled a yellowish bamboo slip from inside his clothes and showed it to them.

It was a contract stating that he would work as a porter for the Seongun Escort Bureau for one year and pay a penalty if he left before then.

“You can read, right?”

“I finished studying the Four Books and Three Classics when I was four.[^1]”

“Don’t say stupid things like that. Read this part. Yes, that section. Read it aloud, and make sure I can hear you.”

In a clear voice, Cheongpung read the section Seokchil pointed out.

“Once signed, this contract cannot be revoked. In the event of unauthorized departure, the signer shall pay a penalty of fifty nyang of silver or provide compensation of equivalent value.”

“You know how much fifty nyang of silver is, right? Do you know what ‘compensation of equivalent value’ means?”

Cheongpung thought deeply for a moment, then slapped his forehead.

“Does it mean I’d have to work it off?”

“That’s right, you idiot. Did you think the Escort Bureau was full of nothing but kindhearted saints?”

Seokchil’s blood pressure rose, and the back of his neck began to ache. He wanted to split the top of this kid’s skull open and see what was inside.

*How can someone like this even exist? Is it because he only ever lived in the mountains?*

The dangers of transporting goods across the land were beyond imagination. Mounted bandits, river bandits, mountain bandits, every kind of bandit gang imaginable, not to mention interference from competing Escort Bureaus.

Even if they overcame all those obstacles, one encounter with a natural disaster could bring an escort run to failure.

An Escort Bureau was every bit as thorough and hard-edged as most Murim sects, if not more so.

*And this kid signed the contract, then says what? “I’m leaving around here”?*

The young fool in front of him knew far too little about the world.

Seokchil spoke, determined to keep the boy from throwing his life away.

“I’m telling you this just in case, so give up on running away right now. Work for a year and think of it as earning money. Understand?”

“A year is too long. I think I can work until tomorrow, though.”

“You little bastard!”

“Hyung, Hyung, calm down! If Escort Chief Song happens to see this, we’ll all be in trouble.”

“Let go! I said let go!”

It was just then, as Seokchil was about to snap.

“Uh, wouldn’t this be enough to cover the penalty?”

Clink.

The two men’s eyes widened when they saw what Cheongpung held out.

The object was shaped like a horse’s hoof and gleamed with a silver light whiter than the snow.

“Is that a silver ingot?”

“And there are two of them!”

There were two silver ingots, each worth fifty nyang of silver.

A hundred nyang of silver was an enormous sum that an ordinary porter would struggle to earn even after working himself to the bone for ten years.

And yet such a fortune had come from the clothes of a young man from a slash-and-burn farming community.

“H-how?”

“I was given some traveling money when I left home.”

At Cheongpung’s innocent answer, both men’s mouths fell open.

What kind of family gave their son a hundred nyang of silver as traveling money? And judging from the money pouch hanging limp like a bull’s testicles, this didn’t seem to be all he had.

“At least it looks like the penalty can be settled with this…”

The two men nodded frantically.

“It can. Of course it can.”

“Why did you suddenly start speaking formally?”

“It’s just more comfortable this way.”

“Exactly. It’s the most comfortable thing in the world.”

“Oh. If that’s what you prefer.”

Cheongpung looked at the two men as if they were strange and handed over the two silver ingots.

“I’ll be going, then. Please tell them this is the penalty.”

“A-are you really giving us both?”

“It’s too much…”

“If there’s any left over, you two can split it. I don’t really know how to spend money. Buy yourselves some warm clothes. Something with expensive fur on it.”

“……!”

As Cheongpung slung a bundle over his shoulder and prepared to leave, Seokchil hurriedly spoke.

“C-could I ask your name?”

“Cheongpung. Until half a month ago, I was from Henan. Last month, I lived in Hubei, and before that, I was in Shaanxi.”

After answering, Cheongpung began walking steadily toward Taiyuan.

The sky was blue, and early shoots were already sprouting from the damp earth.

“Maybe spring will come a little early this year.”

He smiled brightly as he thought about it. He hoped the plum blossoms would bloom in profusion again this spring.

Then, without warning, he thought of Lotus Peak on Huashan, from which he had secretly run away not long ago.

[^1]: The Four Books and Three Classics are foundational Confucian texts.
## Chapter artifact 131

# Chapter 131

“Fresh-killed pork, twenty coins per geun! Cheap, cheap!”

“Oh my, what should I do? That ring suits you perfectly. It’s normally one nyang of silver, but you have such pretty fingers, so I’ll give it to you for half a nyang. What do you say?”

“If I may say so, this pill will clear your mind and fill you with strength after just one dose…”

The streets were filled with endless rows of stalls and the booming cries of market merchants.

When I saw the crowded streets of Taiyuan, I clicked my tongue in amazement.

*There are a hell of a lot of people.*

There was quite a variety among them, too. There were not only street vendors, but also quack medicine sellers, people dressed in smooth silk, and beggars whose poverty practically poured off them.

Martial artists wearing swords at their waists were easy enough to spot, but no one paid them any particular attention. Everyone simply continued with whatever they were doing.

*So this is the capital of Shanxi Province.*

Shanxi Province had dozens of counties and towns, but Taiyuan held a particularly important position among them.

Thanks to its many advantages, it had once served as the capital of a dynasty in the distant past.

That dynasty had fallen long ago, of course, but Taiyuan had continued to develop afterward…

At least, that was what Hyuk Mujin had told me.

*That must be why the Jin Family of Taiyuan has managed to survive for three hundred years.*

Abundant supplies and manpower. And economic power.

Come to think of it, even after some worthless son had plundered the family treasury and dumped all of it into a pleasure house, they had still possessed enough strength to go to war with the Mount Heng Sword Sect.

If they had been the Jin Family of Mount Heng instead of the Jin Family of Taiyuan, they would have gone bankrupt and ended up on the streets long ago.

*You can’t pass through Taiyuan without setting foot on the Jin Family of Taiyuan’s land.*

As I recalled something I had heard long ago, Hyuk Mujin asked,

“What are you thinking about so seriously?”

“Land speculation is pretty great. That’s what I was thinking.”

“What?”

“It’s nothing. You…”

“I don’t need to know?”

“You catch on quickly.”

“I’m getting tired of hearing that.”

“Yeah, I’m getting tired of you, too.”

“Then why did you bring me along?”

“Let’s at least get the facts straight. I didn’t bring you. The eldest brother assigned you to me.”

Jin Wikyung had sent me ahead in preparation for tomorrow’s luncheon with Shanxi’s City Lord. I assumed he wanted to accommodate the capricious child as much as possible without causing any trouble.

In any case, that was why Hyuk Mujin was traveling with me. As a native of Taiyuan, he was an ideal attendant in many ways.

“Come to think of it, isn’t this your hometown?”

“My hometown… Yes, it is.”

Hyuk Mujin stared at the streets with complicated emotions in his eyes.

“It’s only been five years, but so much has changed.”

“You must have stopped by a few times in between.”

“No. I haven’t visited even once during that time.”

I was startled by the unexpected answer.

“Not even once in five years?”

“I started learning martial arts rather late. If I wanted to catch up with everyone else, I had no choice but to work ten or twenty times harder.”

“Hmm.”

“I never thought I’d return like this.”

It was the first time in a long while—no, almost the first time ever—that I had seen him look so serious.

Come to think of it, Hyuk Mujin was a First Rate master who had quite a bit of skill, even though he acted foolishly about everything. It was just that he happened to be surrounded by monsters. His realm was by no means low.

He could only have reached that level through tremendous effort. And on top of that…

*He seems to have some talent, too.*

> **System**
>
> **Level:** 48  
> **Name:** Hyuk Mujin

The rapidly rising Level was proof of that.

*Is this guy going to suddenly become a Peak master one of these days?*

Despite my newly appreciative gaze, Hyuk Mujin was too absorbed in the emotions of returning to his hometown after so long.

“Ah, that auntie is still here.”

His voice was happy, yet wistful.

The middle-aged woman he pointed toward had streaks of gray in her hair and was selling various snacks from a small stall.

“Do you like candied hawthorn skewers?”[^1]

Under normal circumstances, I would have told him to stop talking nonsense and keep moving, but the atmosphere was unusual. I answered as kindly as possible.

“I’ve never eaten one in my life.”

“When I was young, I wanted one so badly. Whenever I crouched in front of the stall and sucked on my fingers, that auntie would give me one or two.”

Hyuk Mujin continued with a bitter smile.

“You have no idea how envious I was of the other children. They would come holding tightly to their parents’ hands, buy candied hawthorn and sweets, and walk around the market… I can still see it clearly.”

What was I supposed to do with this atmosphere?

I had assumed there would be some sort of story behind him, but I hadn’t expected it to go in this direction.

*I should have realized something when he said he hadn’t come back for five years.*

There were an unusually large number of orphans in the Murim. Even looking around us, it was easy to find children wandering through the market in filthy rags.

*He must have been in a similar situation.*

If he had no family, he had no reason to return. Coming back would only remind him of the painful memories of standing around the stall as a child, wanting to eat candied hawthorn.

Maybe that was why he had tried to forget his pain through training.

For him, the Jin Family of Taiyuan had been home, and his companions had been his family.

*And without knowing any of that… I’ve been treating him far too harshly.*

Damn it. The tip of my nose was starting to sting for no reason.

Hyuk Mujin immediately noticed the change in me.

“What’s wrong?”

“No, it’s nothing. Maybe the fine dust is especially bad today. My nose feels itchy.”

“Fine dust?”

“Forget that. Why don’t we each get a candied hawthorn skewer?”

“Wouldn’t it be better to find an inn first? If we don’t get a room before the sun goes down, there may not be any left.”

“Hey, how long does it take to eat one of those? They’re not even that expensive. We were given plenty of travel expenses, weren’t we?”

“That’s true.”

“Let’s eat whatever we want and have as much fun as we can before we leave. You can raise that auntie’s sales while paying her back for all the candied hawthorn she gave you when you were young.”

“I’m not sure it’s right to spend the money we were given for things we need on this…”

“Spend it. Spend every bit of it. If anyone complains later, bring them to me.”

“What if the Second Young Master complains?”

“...Bring anyone but him.”

Hyuk Mujin let out a short laugh before speaking in a much brighter voice.

“Then shall we each get a candied hawthorn skewer?”

“Sure. I’ve been looking at them for a while, and they’re making my mouth water.”

I was saying that very deliberately for Hyuk Mujin’s sake. I was almost thirty. What kind of adult salivated over fruit candy?

*As long as it makes him feel better.*

That guy had suffered plenty while following me around. He was constantly berated and beaten, and every time we took on a Quest, we ended up meeting nothing but monsters. He had come close to dying more than once.

My first meeting with Hyuk Mujin had certainly been an ill-fated one, but that was no longer true.

“Hey, Mujin.”

Hyuk Mujin, who had just started walking toward the stall, stopped short.

“Yes? What is it?”

“That…”

The words *I’m counting on you from here on out* hovered at the tip of my tongue. Damn it. That was far too embarrassing for two grown men to say to each other.

After agonizing over it, I ended up blurting out something completely different.

“Let’s each have two. The big ones.”

“Oh. Yes.”

Too embarrassed to look at him, I stared off at a distant mountain. That was when I heard Hyuk Mujin speaking with the middle-aged woman.

“Oh my! Aren’t you Mujin? Hyuk Mujin, right?”

“It’s been a long time, Auntie.”

“My goodness, it is you. It is! I almost didn’t recognize you, child.”

“You haven’t changed at all, Auntie.”

“Ho-ho-ho. That’s kind of you to say. Have you been well, Mujin? I heard you became a martial artist.”

“Yes. I belong to the Jin Family of Taiyuan. I’ll be promoted to Master of the Gatekeeper Pavilion soon.”

“T-Taiyuan Jin Family? Master of the Gatekeeper Pavilion? My goodness, my goodness…”

Whether he would actually be promoted to Master of the Gatekeeper Pavilion remained to be seen, but the conversation brought a pleased smile to my face.

*This sounds like a radio call-in story.*

A kindhearted auntie who used to give candied hawthorn to the orphan child who was always lingering around her stall. After years of backbreaking effort, the child who had endured a difficult childhood finally succeeded and returned as a tall, grown man.

It was a story I had heard somewhere before, but that didn’t make it any less moving.

“Ahem. What is this? Did something get in my eye?”

Was this the yellow dust or the fine dust? Factories couldn’t have been built yet, so it must have been yellow dust.

That was when the rims of my eyes reddened slightly despite myself.

“So, have you gone to see your parents?”

“Not yet. I was thinking of stopping by today or tomorrow.”

“Go see them soon. Didn’t your family move?”

“Move? Where did they go?”

“They moved into a large estate along the main road over there. They even released koi into the pond and raised them.”

“Oh, really?”

“...?”

Parents? Moving? A huge estate with koi?

Wait. Something was wrong here. I asked Hyuk Mujin, who was returning with the candied hawthorn skewers in his hands.

“What were you talking about?”

“Huh? About what?”

“Are your parents still alive?”

Hyuk Mujin stared at me as though I were insane.

“Why would I kill my perfectly healthy parents?”

“No, that’s not what I meant… Then what were you talking about earlier?”

“What did I say?”

“About the candied hawthorn. You said you couldn’t eat it and spent every day sucking your fingers.”

“I couldn’t eat it. My parents wouldn’t let me because they said it would rot my teeth. All the merchants around here knew how overbearing my parents were, so they made a point of refusing to sell any to me specifically. That lady was the only one who would secretly slip me one.”

“…”

“And what about being jealous of the children who walked around holding their parents’ hands?”

“My family’s business was so successful that they never had any free time. I played by myself.”

“Th-then you had family in Taiyuan, and you didn’t visit even once in five years?”

“I left home. I didn’t want to inherit the family business, so I left a single letter behind and ran away. The Master of the Gatekeeper Pavilion in our family is my father’s childhood best friend, so he probably knew everything about how I was doing.”

“…”

“For about two years, they gave me hell over it. Then my youngest sibling was suddenly born, so I no longer needed to inherit the family business. After that, they stopped saying much.”

Hyuk Mujin stretched his neck and looked around before raising a hand to point at something.

“Ah, there it is. Do you see it? That building belongs to my parents… It got even bigger while I was gone.”

I followed Hyuk Mujin’s finger and turned my head.

A huge, towering five-story pavilion and a signboard bearing enormous characters came into view.

**Hyuk Family Textile Shop**

Hyuk Mujin smiled proudly.

“It’s the largest textile shop in Taiyuan. We have branches in Henan and Hebei, too.”

*This bastard is a rich kid, too…*

You had to be pretty damn wealthy to open chain stores in a place this rough.

*What the hell have I been doing?*

A young boy who used to suck on his fingers because he wanted to eat candied hawthorn so badly?

In reality, his successful business-owner parents had forbidden him from eating it because they were worried about their son’s dental health.

*What the fuck is this?*

As I stood there with my mouth hanging open, Hyuk Mujin held out one of the candied hawthorn skewers.

“Here, have one. I specially chose the biggest and shiniest one. The ones that lady sells are the best in this area.”

“You son of a…”

I swallowed the curse that had surged up to my throat and bit down on the candied hawthorn with a loud crunch.

“Let’s hurry up and find a room.”

“Already? We’ve only spent a few copper coins…”

“Hey! Is it your money? It’s travel expenses they gave us to use when necessary. Expenses!”

“Didn’t you just say we should spend it all and have fun?”

“We’ve had enough fun. You said the rooms would fill up after sunset. If we get a bad night’s sleep and end up late to tomorrow’s luncheon, are you going to take responsibility?”

“…”

* * *

Honghwa Inn.

As could be guessed from the name written on its signboard, this was one of the places under the Lower District Sect’s influence.

*Honghwaru at night. Honghwa Inn for lodging.*

Whoever had come up with that arrangement had clearly intended to wring every last penny from drunken customers.

“Let’s go in.”

I was about to lead Hyuk Mujin, who had been pouting since earlier, toward the inn’s entrance when someone spoke.

“Excuse me, I’m sorry to bother you.”

The voice strangely tugged at my nerves. Its owner was a young man with an affable expression and a dreamy, hazy voice as innocent as a child’s.

*This feeling…*

The moment I turned around and met his clear eyes, I found it difficult to breathe.

This was an aura different from Jin Mukyung’s.

> **System**
>
> **Level:** ???  
> **Name:** Cheongpung

Another Peak master had appeared.

Amid the tension, the young man named Cheongpung opened his lips.

“If you don’t mind, may I eat just one candied hawthorn skewer?”

“...?”

*What the hell is this guy?*

[^1]: Candied hawthorn skewers are a traditional snack made by coating skewered fruit in hardened sugar.
## Chapter artifact 132

# Chapter 132

“If it wouldn’t be too much trouble, may I have just one candied hawthorn skewer?[^1]”

[^1]: Candied hawthorn skewers are a traditional Chinese snack made by coating skewered fruit in hardened sugar.

The unexpected comment caused my brain to freeze for a moment.

*What the hell is he talking about?*

It wasn’t one of those *Do you know the Way?* pitches. He was asking if he could have just one candied hawthorn skewer.

I hadn’t planned for a Peak master I’d just met to beg for candied hawthorn in the most polite tone in the world.

*Grrrrrrowl.*

Now he was even tugging at my pity with his stomach clock. Without thinking, I held out the candied hawthorn skewer I was still holding.

“H-here.”

“Thank you, Benefactor.”

Talk about value for money. Ten seconds after meeting him, I had become a Peak master’s Benefactor.

Hyuk Mujin and I stared blankly at Cheongpung as he ferociously bit and sucked on the candy-coated snack children usually ate.

“Captain, do you know him?”

“No.”

Cheongpung devoured the candied hawthorn skewer as though it had vanished in the blink of an eye. Apparently, it hadn’t been enough, because he turned toward Hyuk Mujin with the eyes of a starving beast.

More precisely, he stared at the two candied hawthorn skewers in Mujin’s hands.

“…Mujin.”

“Yes?”

“Give them to him.”

Hyuk Mujin quickly hid his hands behind his back.

“No.”

“You don’t want to?”

“Yes. This is the first time I’ve eaten these in five years. I haven’t even taken a bite yet.”

“I see. Our Mujin wants to die fifty years ahead of schedule.”

“…”

With a deep sigh, he held out the candied hawthorn skewers. Cheongpung’s eyes flashed.

“Thank you, Benefactor!”

The next moment, accompanied by a sharp *whoosh*, the candied hawthorn skewers had transferred into Cheongpung’s hands.

“Gah!”

That was an incredible speed. Hyuk Mujin sucked in a startled breath and whispered to me in a trembling voice.

“He’s not an ordinary beggar, is he?”

What kind of expression would Mujin make if he learned that the filthy young man in front of us was a Peak master?

I studied Cheongpung as he inhaled the candied hawthorn with single-minded focus.

*He looks far too young to be a Peak master.*

I had heard a few rumors by now. I also knew that even famous, powerful sects with every kind of genius training and support only produced a Peak master once in a blue moon.

That was why Jin Mukyung, who had come from Shanxi Province—a remote backwater even by the standards of the Central Plains—had become so famous.

*He reached the Peak realm ten or twenty years ahead of everyone else.*

*But…*

The young man in front of me looked barely my age, yet he was a Peak master whose Level I couldn’t even determine through Qi Sense.

I had never heard of a Peak master this young living in Shanxi Province.

*Where the hell did this guy come from?*

As if on cue, Cheongpung raised his head. Since he had eaten so hurriedly, his mouth was covered in sticky sugar.

“Whew. That was delicious.”

“You must’ve been a little… very hungry.”

“Yes. I haven’t eaten all day.”

“Oh dear. How did that happen?”

“I lost my travel expenses. Still, it was an interesting experience.”

“…”

Could being forced to starve all day because you had no money really count as an interesting experience?

I had felt it from the moment we met, but this guy definitely had a peculiar way of thinking.

Cheongpung smiled brightly and gave us a respectful fist-and-palm salute.

“Ah, I’m late introducing myself. Cheongpung offers his greetings to his Benefactors.”

“My name is Jin Taekyung.”

“I’m this man’s right arm and heart, Hyuk Mujin.”

I completely ignored Hyuk Mujin’s nonsense and kept my eyes on Cheongpung.

I might not look it, but I was fairly famous in Shanxi Province.

Until a few months ago, I had been famous for all the wrong reasons. Now, for the exact opposite reasons, there wasn’t a single person in Shanxi Province who didn’t know my name.

*I wonder if he’ll recognize me.*

Just as I was secretly getting my hopes up, Cheongpung’s face went stiff.

“Excuse me, are you perhaps…”

“Yes, that’s right. I’m the very—”

“Would it be all right if I imposed on you a little longer?”

“What?”

“I’ve been hungry for quite a long time.”

Right on cue, a thunderous sound came from Cheongpung’s stomach.

*Grrrrrrowl.*

“…Then why don’t we have a meal together?”

“Thank you, Benefactor!”

I couldn’t tell whether I was his Benefactor or just a sucker.

* * *

The inside of Honghwa Inn was packed with people who had come for an early dinner.

A quick-footed waiter led us to one of the few remaining empty tables.

“What’ll it be?”

I handed the wooden menu board to Cheongpung.

“Order whatever you want.”

“Oh, no, I couldn’t. I’m not some ungrateful beast who doesn’t know how to repay a kindness. How could I…”

“It’s fine. Order whatever you want.”

“Then I’ll have everything on here.”

“…”

What an ungrateful beast.

The appearance of a colossal sucker kept the kitchen busy. Before long, the dishes we had ordered began pouring out without pause.

“Garlic Pork is here. This dish is made by slicing boiled pork thin and…”

“Oh.”

“Fish-Fragrant Shredded Pork is here. It’s pork served with bamboo shoots, wood ear mushrooms, and…”

“Ohhh.”

“Beijing Sauce Shredded Pork.”

“Ohhhh!”

“Beggar’s Chicken.”

“Ohhhhh!”

Unlike the waiter, whose explanations had grown shorter and shorter, Cheongpung’s reactions were becoming more and more elaborate.

Dish after dish continued filling the table. Just as there was barely any room left, the waiter pushed out another plate with the expression of a man who had reached enlightenment.

“Maegu.”

“Maegu?”

I’d heard of Megumi from the island country next door, but Maegu was a new one to me. Catching my look, the waiter answered as if explaining it was a chore.

“Maechae Guyuk.”[^2]

“…”

Now he was even abbreviating dish names.

While I stared at him in disbelief, Cheongpung rapidly emptied the plates.

[^2]: *Maechae Guyuk* is pork belly with preserved mustard greens. The waiter shortens its Korean name to *Maegu*, which sounds like the beginning of the Japanese name Megumi.

“Nom, nom.”

“Slow down. Eat slowly.”

“Mmph, mmph. Ah hih he ho. Ha hu i heup hi ha.”

“Don’t answer. Just keep eating.”

“Khanks hah!”

Hyuk Mujin whispered with a thoroughly disgusted expression.

“Isn’t he really a beggar?”

“Didn’t you see him snatch the candied hawthorn earlier? He definitely isn’t.”

*Chomp, chomp.*

“…Probably.”

“What if he’s a master of the Beggars’ Sect?”

“The Beggars’ Sect, huh?”

I had seen it countless times in martial arts novels. It also existed openly in the actual Murim as one of the Nine Sects and One Gang.

I had never met one of its members, but any of the beggars loitering near the inn’s entrance could be a Beggars’ Sect disciple.

“Should I take a quick look to see whether he has any knots?”

The masters of the Beggars’ Sect supposedly distinguished their status by the knots around their waists.

I shook my head.

*No. He isn’t with the Beggars’ Sect.*

If he were, he would have reacted somehow when he heard my name. We belonged to the same orthodox faction, so he had no reason to pretend he didn’t recognize me.

*Then what sect is he from?*

There was no way a Peak master this young had simply dropped out of the sky.

He had to come from a famous sect at the very least… The more I thought about it, the more curious I became about this mysterious young man.

“Burp. That was delicious.”

Cheongpung finally finished eating. After patting his tadpole-like belly, he looked at Hyuk Mujin and me, then stopped short.

“It was my first time trying any of these dishes, so I made a spectacle of myself in front of my Benefactors. I hope I didn’t overdo it…”

*You were more than excessive, you idiot.*

Still, it was good that he had at least a little self-awareness.

“It’s fine. I do that sometimes, too.”

“We have something in common. Ha-ha.”

I laughed along with Cheongpung and opened my mouth. It was time to start questioning him.

“You said everything was your first time eating it. You don’t usually eat rich food, do you?”

Cheongpung shook his head gloomily.

“It’s not that I don’t eat it. I couldn’t eat it. If I’d known food this delicious existed, I would have come down from the mountain sooner.”

“Oh, so you lived in the mountains. That must have been difficult.”

“Life in the mountains? It was fun. The scenery was beautiful, and there was plenty to eat here and there. My grandfather has lived alone in the mountains his entire life, too.”

“Your grandfather?”

“Yes. But, um…”

“Go ahead.”

“May I order some alcohol? I’ve never had any before.”

“…Order as much as you like.”

This kid had a lot of things he had never tried.

At least he still had a sliver of conscience left. He ordered the cheapest bottle of fire liquor.

A short while later, Cheongpung downed the fire liquor without hesitation and muttered with a slightly flushed face,

“Ahh, so this is what it means to get drunk. But what were we talking about?”

“That your grandfather had lived alone in the mountains his entire life.”

“Oh, right. Anyway, I lived with my grandfather from a young age. That started when I was five, so it’s already been fifteen years.”

“Really? That’s a long time.”

I did my best not to show my surprise.

*A Peak master at barely twenty.*

That meant he was a genius at least comparable to Jin Mukyung, if not greater. The more I talked with him, the more curious I became about his identity.

“Where was it? If it’s such a nice place to live, maybe I could visit sometime.”

Cheongpung hesitated just as he was about to say something.

“Um, I don’t think I can tell you that.”

“Come on. You can’t even tell me that much?”

“Because my grandfather hates it when people visit. He moves to a different place once or twice a year because of that.”

“He moves?”

“Yes. Strange people keep coming to see him.”

*Strange people? Obnoxious hikers?*

Well, I suppose it would be annoying for someone living in the mountains.

He continued speaking with a nostalgic look in his eyes.

“When I was ten, dozens of people suddenly came rushing over and started causing trouble. I remember my grandfather shouting at them to get lost before he set the mountain on fire.”

“Oh, so that’s why he keeps moving?”

“Yes. Fortunately, the mountains are huge, so he’s been avoiding them successfully for ten years.”

“…”

Ten years? His grandfather was quite a man.

Hyuk Mujin, who had been listening to Cheongpung’s story with great interest, asked,

“Then why did Young Master come down from the mountain?”

Cheongpung, who had been sucking on the mouth of the liquor bottle regretfully, answered,

“Because of the Ten Dragons and Phoenixes.”

“The Ten Dragons and Phoenixes? What’s that supposed to be?”

At my question, Hyuk Mujin looked at me as though I were the strangest person he had ever seen.

“Why don’t you know about the Ten Dragons and Phoenixes, Captain?”

“I’m allowed not to know, damn it.”

“Huh? You made a complete fool of yourself last year after getting plastered at a pleasure house and bragging that you were going to become one of them.”

“That wasn’t me… Never mind. What are the Ten Dragons and Phoenixes?”

“Are you seriously asking because you don’t know?”

“Can’t I just not know?”

“Of course you can’t. The Second Young Master is one of them, after all.”

Wait, really?

As I blinked at him, Hyuk Mujin launched into an impassioned explanation.

“They’re the greatest young prodigies of the orthodox Murim! The dragons and phoenixes who will lead the Murim of the future! How can you not know about the Ten Dragons and Phoenixes?”

“Hey, hey. Keep your voice down. People are staring.”

He wasn’t exaggerating. Hyuk Mujin’s booming voice had drawn glances from the other customers.

“Who cares if they stare? This is too much even for you, Captain! Are you making fun of me?”

“I don’t know about making fun of people, but I’m good at hitting them.”

“I think I got too worked up. I’m sorry.”

Hyuk Mujin regained his composure in an instant. I turned away from him and gave Cheongpung a friendly smile.

“Please continue.”

“It’s nothing important. I just had a childish thought for a moment.”

Cheongpung looked at me through slightly unfocused eyes. Apparently, he had no intention of using his internal energy to dispel the drunkenness, because he was still a little tipsy.

“Who would be stronger, me or them? I wanted to find the answer to that question.”

In the end, it was because of a martial artist’s competitive pride.

The desire to step into a new world. The desire to defeat a strong opponent and prove his martial arts. I could tell that those feelings had led him down the mountain.

*He seems to have the skill to justify thinking that way, too.*

Jin Mukyung had supposedly reached the Peak realm when he was barely twenty and caused an uproar throughout the Central Plains. Now, he was counted as one of the Ten Dragons and Phoenixes, one of the greatest young prodigies of the orthodox faction.

The Cheongpung in front of me possessed martial talent at least comparable to Jin Mukyung’s.

*He has every right to think so.*

I was nodding inwardly when—

“Puhahaha!”

“Pfft, hahahaha. Ah, holding back my laughter was torture.”

I raised my head toward the source of the sound.

On the second floor, five men and women in silk clothes were looking down at us with faces full of mockery.
## Chapter artifact 133

# Chapter 133

Woo Jintae raised a golden wine cup. Five men and women, including him, sat around a table laden with every kind of delicacy and fine liquor.

“Now, to the limitless prosperity of the Five Gates of Shanxi!”

“To prosperity!”

“To prosperity!”

After the wine made its way around once, smiles spread across everyone’s faces.

“As expected of Honghwa Inn. I don’t know who the chef is, but the food is incredible.”

“Right? It practically melts the moment it touches your tongue.”

Woo Jintae let out a hearty laugh.

“Ha-ha! Loosen your belts and eat to your hearts’ content. I’m paying for everyone today, too.”

“Wow, as expected of you, hyung! At this rate, aren’t you going to pull up one of the foundation pillars of the Seongun Escort Bureau?”

“Oh my, can you afford all this?”

Woo Jintae chuckled as he looked at the two men and two women in front of him.

They were the scions of the Five Gates of Shanxi, the representatives of an alliance of twenty small and medium-sized sects. Even so, they had to yield to him.

“Hey, I’m Woo Jintae. Woo Jintae of the Seongun Escort Bureau! I could buy this entire inn and it wouldn’t be a problem, so don’t worry and eat as much as you like.”

There was a little bit of boasting mixed in, but it wasn’t entirely untrue.

The Seongun Escort Bureau dominated the area around Three Questions Gorge and earned an enormous amount of money every year through various businesses, including transportation and security.

Woo Jintae was the heir who would inherit that very Seongun Escort Bureau.

*Money really is the best.*

The Five Gates of Shanxi were nothing more than the scions of a bunch of small and medium-sized sects that were all roughly the same. With the financial power of the Seongun Escort Bureau behind him, there was nothing Woo Jintae had to fear.

“Thanks to everyone here, our Seongun Escort Bureau has climbed another step higher, so it’s only right that I treat you accordingly, isn’t it?”

At Woo Jintae’s words, everyone hurriedly waved their hands.

“Oh, no. How could that be thanks to us? It’s all thanks to the Chief and Young Hero Woo working tirelessly day and night for the growth of the Escort Bureau.”

“That’s right. We could never accept such praise from Young Hero Woo.”

They said that money could make even ghosts do your bidding. Living people were even easier.

*Working tirelessly day and night, huh? Well, that isn’t entirely wrong.*

The Seongun Escort Bureau was neither a prestigious martial family nor a distinct Murim sect. The reason it had been able to join the Five Gates of Shanxi was because it had opened its purse.

The Sect Leaders, senior members, and scions of more than twenty small and medium-sized sects…

Woo Jintae had stuffed all of them with liquor and money day and night, and the results had been undeniable.

*The Five Gates of Shanxi.*

It was a position that could be called the representative of the alliance of small and medium-sized sects in the south.

For an ordinary Murim sect, it would have been nothing more than a hollow honorary position. But for the Seongun Escort Bureau, which generated profits through all kinds of businesses, it was like growing wings.

Woo Jintae lowered his head with an appropriately solemn expression.

“No. The Seongun Escort Bureau of today exists because of all of you. Just a few months ago, those vile old monsters had us living without being able to hold our heads up… Thank you once again.”

“Those old monsters? You mean the traitors?”

“Ugh, don’t even mention them. If this hadn’t happened, all of us would have been helplessly used by them.”

Everyone gathered here was a scion of the Five Gates of Shanxi, but that had not been the case until only a few months ago.

The Samdo Sect, the Gunggui Sect, and three other sects had been the former Five Gates of Shanxi. But during the Battle of Eight Spring Gorge, it was revealed that they were all agents of the Head Elder, and every one of them had been annihilated.

“Now that I think about it, those bastards were especially wary of the Seongun Escort Bureau.”

“They must have been afraid that their identities would be exposed by the keen insight of the Chief and Young Hero Woo.”

Woo Jintae suppressed the laugh that was threatening to escape.

The reason the former Five Gates of Shanxi had been wary of the Seongun Escort Bureau was simple.

*They were worried about exactly this situation.*

The Five Gates of Shanxi had been much stronger back then, and their bonds had been far tighter.

But that was no longer the case. Everyone here had already tasted the money of the Seongun Escort Bureau. Using that as leverage to slowly siphon away all kinds of business interests was only a matter of time.

“Now, let’s raise a toast to our friendship.”

“To friendship!”

The lively drinking continued. From time to time, Woo Jintae also handed out bribes disguised as gifts.

“This is Shu brocade I brought in from Sichuan. I thought it would suit Young Lady Hwang, so I had it set aside separately.”

“Oh my! You mean the Shu brocade I know?”

“Yes. It’s the finest grade, and perhaps that’s why the color is so exceptionally beautiful. I told a servant to load it into the carriage beforehand, so please take it with you.”

“My goodness, Young Hero Woo. Thank you so much.”

“Is there any need to thank me? Just think of it as the feelings I have for you and put it away.”

“Wh-what?”

“Ha-ha, I misspoke. Pretend you didn’t hear that.”

At Woo Jintae’s charming smile, the only daughter of a martial sect with more than a hundred affiliated martial artists blushed.

*Once I make her indebted to me, there will be a day when I can put that debt to use.*

“Hyung, this is unfair. How can you only take care of the young ladies?”

He winked at the scion of a martial family who had become close enough with him to call each other hyung and little brother.

“Did you think I could forget Little Brother Hyuk? Just wait. I’ve prepared an absolutely incredible gift for you.”

“Damn, as expected of you, hyung.”

“Ha-ha, Young Hero Woo, you haven’t forgotten me, have you?”

“What a hurtful thing to say. I only wanted to tell you separately because I have a gift suited to each person.”

It was easy. Expensive silk and jewelry for the women, and peerless beauties and wealth for the men.

There happened to be Honghwaru, supposedly the finest pleasure house in Shanxi Province, nearby. It was perfect.

Woo Jintae smiled as he watched everyone’s delight.

“Now that everyone’s had a chance to unwind, how about we end tonight’s drinking here… What do you all think?”

If they had not received their gifts yet, they might have been disappointed. But things were different now.

The women nodded because they wanted to check the silk and jewelry loaded into the carriage, while the men’s hearts pounded at the certainty that they would be moving to the pleasure house.

“Then let’s have a few final cups before we leave. And don’t forget tomorrow’s luncheon.”

Everyone chuckled at Woo Jintae’s words.

“How could we forget that, no matter how drunk we get?”

“You really underestimate us, Young Hero Woo.”

“I only mentioned it just in case. Ha-ha-ha.”

A luncheon with the City Lord of Shanxi.

That was why the scions of the sects with some clout in Shanxi had gathered in one place. Woo Jintae emptied his wine cup and thought,

*Tomorrow should be interesting.*

The City Lord was only ten years old.

He was already an expert at catering to people’s whims. Woo Jintae had finished making every possible preparation to win the City Lord over.

*I hear he’s quite a mischievous little fellow… He’s a member of the imperial family, so I wonder what he’ll be like.*

Just as Woo Jintae was sinking into thought, a booming shout erupted from downstairs.

“The greatest young prodigies of the Murim’s orthodox faction! The dragons and phoenixes who will lead the Murim of the future! How can you say you don’t know the Ten Dragons and Phoenixes?”

“Hey, hey. Keep your voice down. People are staring.”

At the words *Ten Dragons and Phoenixes*, five pairs of ears perked up.

Who were the Ten Dragons and Phoenixes? They were geniuses already writing the first pages of their legends and the future of the Murim’s orthodox faction.

The Ten Dragons and Phoenixes were objects of admiration for the young martial artists of the martial world, and the people gathered here were no different.

“Who are they? Are they martial artists?”

The person seated closest to the railing craned his neck and looked down at the first floor.

“There are three of them. One is a young master, one looks more or less like a martial artist… and the other one looks like a beggar.”

“What kind of combination is that?”

“Shh. Let’s keep listening.”

At Woo Jintae’s urging, everyone fell silent and pricked up their ears again.

They had all trained in martial arts as befitted scions of martial families, so overhearing the conversation was not difficult.

“Please continue.”

“It’s nothing important. I just had a childish thought for a moment.”

There was a brief silence. Then another statement followed.

“Who would be stronger, me or them? I wanted to find the answer to that question.”

The young prodigies of the Five Gates of Shanxi looked at one another.

“Did you all hear what he just said?”

“Yes. Who said it?”

“That beggar I mentioned earlier. You really do see all kinds of lunatics these days.”

Woo Jintae shook his head.

“He’s a martial artist.”

“A martial artist…?”

“If he’s talking about the Ten Dragons and Phoenixes, he must be. As for how he ended up looking like a beggar, I can more or less guess without even seeing it.”

A mocking laugh escaped Woo Jintae’s lips.

“Isn’t it obvious? He’s the type who picks up a few Third Rate martial arts moves by chance, puts his faith in them, wanders aimlessly through the martial world, and winds up dead.”

“Ah, now that you mention it, you’re right. As expected of Young Hero Woo.”

“The more I think about it, the funnier it gets. How did someone like that dare mention the Ten Dragons and Phoenixes?”

The young prodigies snickered at one another, and their laughter gradually grew louder.

“You can tell what kind of people associate with a lunatic like that. Or maybe they’ll slap him once, call him crazy, and leave?”

“What are the young master and the martial artist sitting with him doing?”

The young prodigy who had glanced down again spoke while trying to hold back his laughter.

“I don’t know what the martial artist is doing, but the young master is nodding to himself.”

“Huh.”

“Really?”

“Wow, you should all see his expression. He genuinely seems to believe that beggar.”

The young prodigies stood up and moved toward the railing. Woo Jintae, who could not resist his curiosity, was among them.

*Let’s see what these people look like.*

The moment he saw the young master’s face, which was nodding with a serious expression, a loud laugh burst from Woo Jintae’s mouth.

“Puhahaha!”

At the same time, the other young prodigies began laughing loudly as well.

“Pfft, ha-ha-ha! I almost died trying to hold that in.”

“Ha-ha-ha! They don’t know the first thing about martial arts, and they’re talking about the Ten Dragons and Phoenixes?”

How long did they laugh?

When they finally managed to stop, what they saw was one person staring quietly up at them.

“Finished laughing?”

At the ‘young master’s’ words, the young prodigies froze.

They had all been raised precious and pampered. How long had it been since anyone had spoken down to them like that?

The chilly silence was broken by Woo Jintae’s dry voice.

“And if we have?”

The ‘young master’ smiled brightly.

“Get down here right now, you fucking sons of bitches. My neck hurts.”

* * *

Hyuk Mujin asked with an expectant look in his eyes,

“Are you going to fight them?”

“Depends on what they do.”

“Once you’ve called them fucking sons of bitches, isn’t that asking for a fight?”

“That would be fine, too. Also, can you see all the spit those bastards sprayed on my face?”

“You’re completely drenched.”

Hyuk Mujin briskly wiped my face with his sleeve.

“What if they don’t apologize?”

“They ought to.”

“Look at their faces. They’re never going to apologize.”

“Then they can get the shit beaten out of them.”

“There are women among them, too…”

“I believe in gender equality.”

“What?”

“I beat everyone equally.”

Cheongpung, who had been watching blankly, looked at me with sparkling eyes.

“Oh. I don’t really understand, but it sounds cool.”

“It’s nothing special… Anyway, thanks.”

Even if I wanted to say more, I was no longer given the time.

The five bastards—or rather, the five sons and daughters of bitches—had jumped down from the second floor.

*Tap.*

They landed lightly, as befitted First Rate masters. One person stepped forward from among the five as they glared at us.

Level 45. He was tall and good-looking. He was also the one who had laughed first.

“I…”

“Are you the head?”

“The head?”

“Are you the boss of the five of you?”

The man gave a short laugh.

“You’d better watch your mouth. If you knew who the people here were, including me…”

I smiled back and scanned through their Level windows.

“Seongryong, Cheonwoo, Myeonghwa, Sohye, and finally, you—Jintae. Want me to tell you your family names, too?”

“…”

“…”

Five pairs of astonished eyes turned toward me. No—along with Hyuk Mujin and Cheongpung, there were seven pairs of eyes fixed on me.

“Oh, and this is a personal request, but please don’t ask how I knew. I’m sick of that line. If you ask, I’ll hit you.”

“How did you…?”

“Did you stick radishes in your ears?”

The next moment, my palm struck the man’s cheek.

*Smack!*
## Chapter artifact 134

# Chapter 134

*Smack!*

Woo Jintae’s head snapped to the side with a satisfyingly solid sound. He blankly stroked his cheek.

*What just happened?*

He was dumbfounded.

Had he just been slapped? By a punk like this?

Woo Jintae was nearing thirty. Thanks to marrying young, he already had a family of his own.

And now he had suffered this humiliation at the hands of some kid who couldn’t have been more than twenty.

“Eek! Young Hero Woo!”

“H-Hyung, are you all right?”

“Isn’t that the Young Bureau Head of the Seongun Escort Bureau?”

“That’s him. My goodness, what kind of reckless bastard would… Wait. Doesn’t that face look familiar?”

The belated reactions of the young prodigies and the stares of the inn’s guests doubled Woo Jintae’s shame.

He glared at the little bastard in front of him with eyes full of killing intent.

“How dare you…”

“That’s not the right way to put it.”

“What?”

“Not *how dare you*. You should be asking *how did you do that?* If you’re a martial artist.”

Woo Jintae froze for a moment.

Since childhood, he had received the full support of the Seongun Escort Bureau, taking in all kinds of elixirs and First Rate martial arts. Even if he hadn’t been born with extraordinary talent, it was only natural that he took pride in being a move and a half ahead of the other young prodigies.

*How did I get beaten so easily?*

He hadn’t even seen when or how the bastard approached him. All he had felt was the humiliation of being utterly disgraced in front of everyone.

Only then did Woo Jintae study his opponent with eyes full of caution.

“Look at those eyes darting around. What, do you want me to tell you my three measurements?”

“Which sect are you from, and who are you?”

“I’m Tien Shinhan of the Dodong Sect, you son of a bitch.”

The only reason Woo Jintae managed to endure the young bastard’s profanity was that his reason had finally returned.

In the Murim, you never knew what might happen. If the other man was a disciple of a great sect, Woo Jintae would have to withdraw cleanly.

*The Dodong Sect? The Dodong Sect’s Tien Shinhan?*

Both the sect and the man’s name were utterly unfamiliar. Woo Jintae glanced back. The other young prodigies wore equally bewildered expressions.

His mind began racing.

*As far as I know, there’s no such sect as the Dodong Sect in Shanxi Province.*

Opening a new sect in Shanxi Province, where all the established sects had already secured their positions, was nearly impossible.

Even without interference from the other sects, word would spread immediately.

*If they raised a young prodigy of this level at that age, they must be a sect with considerable power… Where are they from? Shaanxi? Henan?*

That was when the young martial artist who had been standing idly by as though none of this concerned him suddenly asked,

“What’s the Dodong Sect? Is it a real sect?”

“Would it be? A well-told lie becomes fact before you know it.”

“Ah. I’ll engrave those golden words in my heart.”

“You little punk. You’re speaking nicely for once.”

A young man dressed in rags like a beggar added his own comment.

“A well-told lie becomes fact… Those are wise words. I can sense profound wisdom in them.”

“Ah… yes. Thank you for the compliment, at least.”

Sparks flew from Woo Jintae’s eyes as he listened to the three of them.

“You bastard! Reveal your identity!”

“What, you want to hear who I am and where I’m from, then pick a fight if I seem easy and tuck your tail between your legs and apologize if I turn out to be too high-status?”

“…”

It was a crude statement, but it struck the bull’s-eye. Seeing Woo Jintae unable to answer, the young bastard clicked his tongue.

“Punk, you started with the wrong question. They say the one who farted gets angry. If you wanted an answer from me, you should’ve apologized first.”

Woo Jintae bit down on his lip.

An apology?

Born the sole male heir the Seongun Escort Bureau’s family had produced in three generations, he had been pampered and revered his entire life. He wasn’t flexible enough to bow his head to some nobody whose origins he didn’t even know.

At last, Woo Jintae made up his mind and gave the young prodigies of the Five Gates of Shanxi a subtle signal with his eyes.

*No matter how strong he is, he can’t be that strong.*

There were only three opponents. On their side were five First Rate masters, all among Shanxi Province’s foremost young prodigies.

Seeing the four men and women discreetly gripping their weapons in response to his signal, Woo Jintae felt reassured.

“Do you know who I am—or rather, who we are?”

“I happen to know your names, at least. But is that an apology?”

“An apology? You’ve got some nerve.”

Woo Jintae gave a thin smile.

“We are the heirs of the Five Gates of Shanxi. Surely you can’t claim not to know the Five Gates of Shanxi.”

“I’ll say I know. But are you really not going to apologize? This is your final warning.”

“I’ll give you a warning, too. I don’t know where you came from, but you picked the wrong person to mess with—”

*Smack!*

Woo Jintae’s vision flashed white.

As he instinctively stumbled backward, lightning-fast slaps struck him one after another.

*Smack! Smack! Smack-smack!*

One slap with every step.

After taking five slaps in all, Woo Jintae staggered unsteadily.

Because the blows had relentlessly targeted one side, his cheek had swollen grotesquely. Blood pooled inside his split mouth.

*Even my father never hit me.*

It was the first humiliation of his life—and it had happened in front of everyone.

His eyes rolled wildly.

“You fucking—!”

“I told you, final warning. Do you not know what *final* means, or what *warning* means? Or both?”

“How dare you hit me?”

“I may be the first man ever to treat you so casually, but please don’t fall in love with me. I’m busy enough loving one Song-i.”

“I’ll kill you!”

“I’ll beat you!”

*Smack-smack-smack!*

“Guh!”

Woo Jintae couldn’t regain his senses.

There was no internal energy behind the blows, nor did his opponent seem to be using any mystical manoeuvre technique. And yet Woo Jintae had no way to block the storm of slaps raining down on both his cheeks.

*How is this happening?*

As he was beaten helplessly, a crazed shout rang in his ears.

“Slap with the left hand, slap with the right hand!”

*Smack-smack!*

“One chi, two chi, three chi, four chi—Ppukku cheek! Ppukku cheek!”

*Smack-smack-smack!*

He kept shouting words that made no sense while flinging slap after slap. He looked like a madman born for the sole purpose of smacking people across the face.

Just like right now.

“Raise your left hand and lower your right. Lower your right and lower your left. Lower your left, and don’t raise your right.”

“Hurk!”

“That’s right. Good job. As a reward, your teacher will give little Woo Jintae’s cheeks a thorough beating.”

*Smack-smack-smack-smack!*

How many times had he been struck in the space of less than a moment?

Thirty? Fifty?

He had been hit so frantically that his head rang and tears swam in his eyes.

In the end, all Woo Jintae could do was call for help.

“P-please! Somebody help me!”

* * *

The Young Bureau Head of the Seongun Escort Bureau—the very Seongun Escort Bureau whose wealth alone was said to rival that of the Jin Family of Taiyuan, the richest family in Shanxi—cried out in desperation.

“P-please help me!”

Having thrown away his pride and everything else, Woo Jintae’s desperate plea still failed to make the young prodigies of the Five Gates of Shanxi draw their weapons.

“How are we supposed to beat that…?”

Someone’s groan spoke for everyone.

They were right. There was no need to experience it firsthand.

Just watching from the side was enough to make their knees go weak and their legs tremble. Their opponent was roughly the same age as them, but there was no question that he was a master far beyond their imagination.

“To reach that realm at his age…”

“That thing’s a complete monster.”

*Smack-smack!*

“P-please spare my life!”

Woo Jintae’s voice grew even more desperate. Even his plea for help had subtly changed.

If this continued much longer, he might start begging them to kill him instead.

“We, we should help him, right?”

“At the very least, we should try to stop him… Young Master Wang, do something.”

“Me? Why am I suddenly involved?”

“Why do you think? Every time we got together, you bragged about your family’s martial arts. You said it was sword arts you could display anywhere in the Central Plains without shame.”

The heir of the Wang Family Estate, who had boasted endlessly about the greatness of his family’s martial arts, answered with a stern expression.

“I’m a saber user. I never learned sword arts.”

“What?”

“And why are you trying to dump this on me? If Young Lady Shin wants to stop him so badly, she can step in herself.”

“My goodness. What a ridiculous thing to say.”

That was when the young prodigies of the Five Gates began shoving the responsibility onto one another.

Hyuk Mujin, who had been quietly watching the situation, suddenly cut in.

“You’re all worrying over nothing. If it were me, I’d hurry over and lend a hand, at least.”

“You—no, you. Who are you?”

With such a terrifying scene unfolding before them, they had to speak with even an ordinary martial artist using half-polite language.

Young Lady Hwang, who had received Shu brocade as a gift from Woo Jintae only moments earlier, quickly stepped forward.

“Let me make this clear in advance. We have no ill feelings toward you people. You know that, right?”

“Do you? If that’s how it is, then fine. Let’s say that’s how it is.”

“I’m not saying we should just say that. I’m saying it’s the truth.”

“What good does telling me do?”

Hyuk Mujin smiled thinly and jerked his chin toward Jin Taekyung’s back, where he was enthusiastically beating Woo Jintae.

“Our Captain has quite a temper. Once the gentleman getting beaten over there collapses, who do you think will be next? You, Young Master? Or the Young Lady beside you?”

“…”

“Oh, and just in case you’re wondering, that man hits men and women alike.”

“I-I didn’t laugh!”

“Neither did I!”

“Do I have to say the same thing twice? Telling me won’t do you any good. Though, there is one way that might work.”

“A way?”

The young prodigies’ ears perked up.

They hadn’t trained in martial arts for nothing. They understood that they had no chance against that monstrous young man.

“P-please… somebody save me…”

Woo Jintae’s dying voice happened to drift into their ears, fanning their survival instincts even further.

“W-what exactly is this way?”

Hyuk Mujin stroked his chin with a deliberately serious expression.

“Well, you’re all children of families that can fart with the best of them, so I don’t know whether you’ll be able to do it.”

“I will!”

“I’ll do it! I’ll definitely do it!”

“Good. You know the basics.”

Hyuk Mujin nodded with satisfaction and pointed to Cheongpung, who was watching the one-sided beating with his mouth hanging open.

“First, apologize politely to this gentleman.”

Before he had even finished speaking, the young men and women of the Five Gates bent at the waist.

“We sincerely apologize.”

“We’re truly sorry for judging you rashly based on your appearance.”

Cheongpung scratched the back of his head.

“I’m fine, so everyone can stand up.”

Hyuk Mujin was taken aback by how readily Cheongpung forgave them, especially after they had mocked him in front of so many people.

Even the expression on his face, which should have been flushed with anger, was sunny and bright.

“You’re saying that so easily?”

“Yes. Is there a problem?”

“It’s not that, but… Weren’t you angry earlier? You were insulted so publicly.”

“Why would I be angry? I just thought it was fascinating.”

“What?”

“It was the first time so many people had focused on me like that. It was also the first time someone who had looked down on me apologized. I thought it was fascinating and fun.”

“…”

“Ah. I think coming down from the mountain was a good decision.”

*This guy’s a little nuts, too.*

Hyuk Mujin looked at Cheongpung as though he were some strange creature, then shook his head and turned to the young prodigies.

“You heard him, right? Since the Young Hero here has accepted your apology, we’ll consider the matter settled.”

“Oh!”

“We’re saved!”

But Hyuk Mujin wasn’t finished.

“All right, then. There’s one final thing left—the second.”

“…The second?”

“There’s more?”

“Yes. This is the most important one.”

Then, with a solemn expression, he declared to the four men and women looking at him,

“All of you, bend over and plant your heads on the floor.”

“……!”

“……”

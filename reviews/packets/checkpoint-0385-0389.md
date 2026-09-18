# Checkpoint Review — 385–389

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

# Chapters 385–389

## Plot

At the Mount Qingcheng headquarters, Jin Taekyung clashes with the arrogant S-rank Hunter Wu Heixing, exposing Wu’s scandals and refusing Prince Felix Alexander Louis’s demand that he kiss the prince’s hand. Lee Jungryong and Wei Fenghu arrive before Wu can draw his sword. During the war council, General Liao proposes nuclear strikes across Sichuan, but Wei rejects the plan because of the civilian devastation, while Magic Johnson warns that the Arch Lich could redirect the warheads. The six S-rank Hunters and Chinese forces are divided among six fronts.

Before deployment, Faye Chen invites Jin to drink. Prince Felix leaves when she cannot provide his preferred 1945 Romanée-Conti, while Magic Johnson and Team Leader Choi join her. Jin follows Wu into a forest, discovers Wu’s secret Sound Transmission and martial-arts abilities, and defeats him after Wu attacks. Jin takes Wu’s Top-Grade Potion as compensation, gives him a high-grade potion to heal him, and warns him to keep silent. Lee Jungryong later approaches Wu about an undisclosed private discussion. Jin completes Circulate Your Qi, slightly advances the Fire Gate Divine Technique, and receives the nonrefusable Sudden Quest **The Desperate War Situation**, ordering him to reach the front and defeat the enemies.

China declares martial law as the Sichuan Monster Wave surpasses 100,000 monsters and causes at least 300,000 casualties in its first week. United Nations peacekeeping forces and international S-rank Hunters join the battle. On the fourth day, Faye holds the east-west front while Lee holds the north. Jin, Team Leader Choi, Shao Shen, and approximately one thousand Public Security Armed Forces Department Hunters attack the western front. Jin leads from the front, using Flamefire Path, White Flame, and Extreme Yang Force to cut through the enemy formation.

## Continuity

- Jin is Level 121, has crossed into true mastery, and retains the Undead Hunter Title and the strengthened Skeleton Warlord, mockingly called Bones.
- Jin completed Circulate Your Qi and slightly advanced the Fire Gate Divine Technique.
- Jin is under the nonrefusable Sudden Quest **The Desperate War Situation** and must quickly reach the battlefront and defeat enemies.
- Choi Minwoo has become substantially stronger and more refined; Team Leader Choi remains Jin’s close combat partner.
- The Sichuan Monster Wave exceeds 100,000 monsters and has caused at least 300,000 casualties. The Arch Lich controls most of its undead forces.
- China is under martial law; United Nations peacekeeping forces and international S-rank Hunters are deployed across Sichuan.
- Jin’s western-front assault is advancing into the monster formation; the breach is on the monster side, not a collapse of Jin’s forces.
- Shao Shen is a twenty-one-year-old Chinese military commander who follows Jin’s orders and accepts calling him hyung.
- Faye Chen prevented the east-west front from breaking through, while Lee Jungryong holds the northern front.
- Wu Heixing secretly knows Sound Transmission, internal-energy cultivation, and fist-and-foot martial arts. Jin defeated and healed him, but Wu remains humiliated, resentful, and jealous.
- Lee Jungryong, head of the Ares Guild and one of the world’s three strongest S-rank Hunters, has recognized Jin’s breakthrough and seeks an undisclosed discussion with Wu.
- Lei Fei’s fate remains unknown. The Arch Lich, the Second Fiend assigned to Qingcheng, and Aehyang’s unidentified superior remain unresolved.

## Translation Decisions

- Retain **Blazing Flame Divine Dragon**, **Huashan Divine Dragon**, **Sound Transmission**, **Flamefire Path**, **White Flame**, **Extreme Yang Force**, **Fire Dragon Armor**, **Moving Formation**, **Arch Lich**, **Bones**, **Death Knight**, **death energy**, **Top-Grade Potion**, and **high-grade potion**.
- Use **Faye Chen**, **Wu Heixing**, **Felix Alexander Louis**, **William**, **Lee Jungryong**, **Shao Shen**, and **Wei Fenghu**.
- Use **Public Security Armed Forces Department**, **martial law**, **United Nations Security Council**, **Archmage**, and **War Mage**.
- Preserve **Lord Fuck**, **peninsula bangzi**, **Chairman Comrade**, **Mimi**, **Mimi-chan**, and the chapter’s vulgar historical and cultural jokes.

## Durable state

{
  "active_continuity": [
    "Jin Taekyung is Level 121, has the Undead Hunter Title, and keeps the strengthened Skeleton Warlord in his Inventory under the mocking name Bones.",
    "Jin Taekyung has crossed the wall into true mastery, while Choi Minwoo has become substantially stronger and more refined.",
    "The Arch Lich's three incomplete Liches were destroyed at Chengdu International Airport, and their testimony identified the Arch Lich as responsible for the undead army's actions.",
    "Wei Fenghu is China's Minister of National Defense under the Central Military Commission, a four-star general, and the current Chairman's right-hand man; Lei Fei remains unconfirmed dead or alive after disappearing with his department's Hunters.",
    "Sichuan Province is under martial law amid a Monster Wave exceeding 100,000 monsters, at least 300,000 initial casualties, magical communications interference, and a large undead army controlled by the Arch Lich.",
    "United Nations peacekeeping forces and international S-rank Hunters are engaged on the Sichuan front; Faye Chen prevented an east-west breach from spreading.",
    "Shao Yang is Chairman of China, Chairman of the Chinese Communist Party's Central Military Commission, and General Secretary; he has addressed the United Nations Security Council over the catastrophe.",
    "Faye Chen is an older S-rank Hunter and Great Cataclysm hero with a former film career, a low media profile, and a playful but composed manner toward Jin.",
    "Wu Heixing is an S-rank Hunter hostile toward Jin who secretly uses Sound Transmission and martial arts, including an internal-energy cultivation technique and fist-and-foot martial arts; he remains deeply resentful of Lei Fei and Jin.",
    "Lee Jungryong is the de facto head of the Ares Guild and one of the world's three strongest S-rank Hunters; he has recognized Jin's breakthrough and is now seeking an undisclosed discussion with Wu Heixing.",
    "Jin Taekyung completed Circulate Your Qi and slightly advanced the realm of Fire Gate Divine Technique.",
    "Jin Taekyung is under the nonrefusable Sudden Quest The Desperate War Situation and must reach the front quickly to defeat the enemies."
  ],
  "continuity_sources": [
    389,
    388
  ],
  "open_questions": [
    "Who is the Arch Lich, and what will happen after Jin Taekyung destroys its three servants?",
    "What happened to Lei Fei and the Hunters who disappeared with him?",
    "What happened to the Second Fiend assigned to the Qingcheng attack?",
    "Who is the unidentified person directing Aehyang, and what are they planning?",
    "What important discussion does Lee Jungryong intend to have with Wu Heixing?"
  ],
  "safe_through": 389,
  "temporary_decisions": [
    "Render 열화신룡 as Blazing Flame Divine Dragon, distinct from Huashan Divine Dragon; use Mimi and Mimi-chan for 미미 and 미미쨩, and Third Fiend and Three Fiends for 삼괴.",
    "Render 진인 as Perfected One, 도우 as Fellow Daoist, 신니 as Venerable Nun, 환영진 as illusion formation, and 이동진 as Moving Formation; use Archmage and War Mage for 대마법사 and 워 메이지.",
    "Render 독룡각 as Poison Dragon Pavilion, 가주 대행 as Acting Family Head, 화룡갑 as Fire Dragon Armor, and 공안무력부 as Public Security Armed Forces Department.",
    "Render 사기 as death energy, 의념 as conveyed thoughts, 데스나이트 as Death Knight, 골골 as Bones, 아크 리치 as Arch Lich, 최상급 포션 as Top-Grade Potion, and 상급 포션 as high-grade potion.",
    "Render 시벌좌 as Lord Fuck, 반도의 빵즈 as peninsula bangzi, 짱깨 as chink, 주석 동지 as Chairman Comrade, 전하 as His Highness, and 다급해진 전황 as The Desperate War Situation; preserve Jin's vulgar historical and cultural jokes."
  ],
  "version": 1
}

## Reading copies

## Chapter artifact 385

# Chapter 385

“Isn’t that right, you peninsula bangzi?”[^1]

“What the hell are you talking about, you mainland chink bastard?”

A heavy silence descended.

Foreigners like Magic Johnson were using translation magic, but they were still bewildered because they didn’t understand exactly what *bangzi* and *chink* meant. Team Leader Choi clicked his tongue softly, while one man’s face hardened like stone.

“What?”

“What, you bastard?”

“Say that again, you bangzi.”

“Sure. Chink.”

“You fucking—”

“Good. Let’s clear this up. I’m a dog. You’re a chink.”

“……!”

I watched his face twist violently. Just as he was about to shove back his chair and leap to his feet, the woman sitting beside him raised a hand to stop him.

“Enough.”

She was a beautiful woman in her early twenties, with an atmosphere as clean and refreshing as a soft drink. Her calm voice continued from between her lips.

“I’d appreciate it if you both kept it to a reasonable level.”

*A reasonable level…*

I studied her for a moment before shrugging.

“Well, if you ask.”

Perhaps my unexpected answer had caught her off guard, because one of her eyebrows curved slightly.

“I heard you weren’t an easygoing person, but you accept that rather readily.”

“I have to. It’s your request, after all.”

“So you’ve fallen for the beauty trap? Ah, this is why being beautiful is such a burden.”

She casually swept back her long hair, and I let out a quiet laugh.

“Did you just laugh?”

“You’re more interesting than I expected, Ms. Faye Chen.”

Faye Chen. That was her name.

I couldn’t let myself be fooled by her appearance and atmosphere, which made her look like a university brochure model. She wasn’t married, but she was well over fifty.

At the same time, she was a far older Senior than me—and one of the heroes of the Great Cataclysm.

“So you knew from the start. Hm. I thought young people these days wouldn’t know who I was.”

She wasn’t wrong. Compared to the other S-rank Hunters, Faye Chen had appeared in the media remarkably infrequently.

Behind the scenes, there were even frequent rumors that she had assumed a new identity and started a new life.

But I had known about her since I was very young.

“My mother’s been a fan of yours for years. You starred in that romance movie that came out about twenty years ago, didn’t you?”

“Oh, my. That was ages ago. Still, it’s nice to meet someone who remembers it.”

“Would it be all right if I got your autograph sometime? I think my mother would be happy if I brought her one from you.”

“Of course. And from now on, just call me Chen. Your full name sounds too formal. You can even call me big sister if you want to be more comfortable.”

“What? What are you talking about? I looked you up online. You’re five years older than my mother.”

“……You really aren’t easygoing. Just as I heard.”

But there was someone else who truly wasn’t easygoing.

“You fucking lowlife—!”

The voice boiled over. The man who had briefly been forgotten in our conversation glared at me with rage in his eyes.

“How dare a bangzi from such a weak country look down on me? Do you even know who I am?”

“……Wow. That line is fucking awful.”

Faye Chen rested her chin on her hand as she looked between us with interest.

“Indeed. I’ve been wondering for a while—do you even know who this young man is?”

Faye Chen wasn’t the only person who wanted to hear my answer.

Everyone except Team Leader Choi, who now wore an expression halfway to enlightenment, was staring at my mouth.

The man huffing and puffing like a seven-year-old child who had lost an argument, Magic Johnson, the Archmage from the United States, and even the young man from the United Kingdom. Their attendants were no exception.

Under everyone’s gaze, I nodded.

“I know. Wu Heixing.”

When it came to frequent media appearances, he vied for first or second place even among S-rank Hunters, so there was no way I wouldn’t know him.

At my answer, the man who had been picking a fight with me by throwing around the word *bangzi*—Wu Heixing—opened his eyes wide.

“You knew who I was and still behaved that way?”

“Even a stray dog would know. There’s a human piece of shit among the S-rank Hunters.”

“What, what did you say?”

“Why? You don’t know that your hobby is getting attention and your specialty is committing crimes and then manipulating the media?”

“……!”

“Come to think of it, didn’t you cause an incident around last year? *The only drug my country allows me*—you posted a raid photo on your official social media while acting like that, then got caught using actual drugs a month later. Marijuana, wasn’t it?”

“Mr. Jin Taekyung.”

“Don’t stop me, Team Leader Choi.”

“It wasn’t marijuana.”

“What?”

Team Leader Choi abruptly cut in and calmly corrected the Taekyung Wiki.

“It was cocaine and methamphetamine.”

“Oh, I see. Thank you for letting me know.”

“Think nothing of it. Now that things have gone this far, what is there left that I can’t say?”

*Look at that enlightened expression.*

Leaving Team Leader Choi behind as he prepared to abandon all worldly concerns and ascend to immortality, I flashed Wu Heixing a broad smile and continued.

“Damn, how did you think of laying down foreshadowing like that? This bastard is at least Wu Heishunwon. *Purple Raid.*”

“What, what did you say?”

“Come to think of it, there’s something else. Five years ago, you got caught drugging someone and sexually assaulting them at some club called Burning Moon or whatever. How did you get acquitted? Under Chinese law, it wouldn’t have been strange if you’d been executed two or three times over.”

“……!”

“I heard a rumor that you’re the son of one of the Communist Party’s highest-ranking officials. Did you buy your way out with money and power? Look at this clever bastard.”

“Shut your fucking mouth! How dare a bangzi from the lowest class speak to me like that!”

Wu Heixing’s face turned bright red as he shouted. Someone who had been silently watching the situation finally spoke.

“You’re noisy.”

An arrogant voice flowed as smoothly as water.

“You’re frivolous and vulgar. I hear you are descended from one of China’s noble families. Did the elders of your family fail to teach you proper etiquette?”

Wu Heixing bit his lip when he recognized the owner of the voice.

“Y-You’re……”

“*You’re?*”

Beneath his neatly arranged brown hair, a pair of subtly green eyes slowly swept over Wu Heixing before moving away.

“William.”

At the young man’s summons, the middle-aged man with half-gray hair standing behind him stepped forward.

His shoes were spotless, and his suit had been pressed as sharply as a blade. Standing tall and surveying the room, the middle-aged man spoke in a pleasant, low-pitched voice.

“Everyone, rise and show proper respect to His Highness Prince Felix Alexander Louis, Duke of Cambridge, Earl of Strathearn, Baron Carrickfergus, Knight of the Order of the Garter, and Knight of the Order of the Thistle.”

*Duke of Cambridge, Earl of Strathearn… Fuck, why does he have so many titles?*

In any case, Prince Felix added a solemn remark.

“Everyone may simply call me His Highness Prince Felix.”

“……”

“……”

Look at everyone’s faces. They looked more uncomfortable than anyone else in the world.

Of course, the most impressive expression of all belonged to Wu Heixing, who had just called me a lowborn bastard.

It made sense. When it came to social standing, how could he possibly beat British royalty?

“So, this is……”

“Ah.”

Prince Felix looked at the flustered Wu Heixing and nodded as though he had finally understood.

“I see. Are you a stutterer?”

“A-a stutterer?”

“If not, why can’t you speak properly? Did your family fail to provide you with speech training?”

*Long live His Highness the Prince.*

I didn’t even need to step in myself. It felt as though the third person in line to the British throne had injected carbonated water directly into my veins, making it fizz all the way to my duodenum.

Just as I was grinning so widely that my mouth nearly split open, Prince Felix’s gaze suddenly turned toward me.

“You there.”

“Hm? Are you talking to me?”

At my question, the middle-aged man standing behind Prince Felix opened his mouth.

“When His Highness Prince Felix Alexander Louis, Duke of Cambridge, Earl of Strathearn, Baron Carrickfergus, Knight of the Order of the Garter, and Knight of the Order of the Thistle, addresses you—”

“Enough, William.”

Prince Felix raised a hand and stopped the parrot mid-sentence, then looked at me with a benevolent gaze.

“I have personally set aside my dignity and intervened because I believe in overcoming the differences between social classes.”

“……?”

“What does it matter whether someone is lowborn or noble? We are all merely equal human beings beneath God. So do not take that man’s words too much to heart.”

*What the fuck is this supposed to mean?*

I lost my ability to speak for a moment. Team Leader Choi quietly whispered to me.

“I believe he thinks you are lowborn, Mr. Jin.”

“……!”

*Is that prince bastard insane?*

As I stared at Prince Felix with an incredulous expression, he slowly rose from his seat and extended the back of his hand toward me with an expression that suggested this was only natural.

“Come now.”

“Come now? What is it this time?”

The middle-aged man who might have been a secretary or a parrot smiled with satisfaction and opened his mouth.

“Kiss the back of his hand and express your gratitude for the benevolence His Highness Prince Felix Alexander Louis has shown you.”

“……”

*Are these people completely insane?*

*Did this group of eighteenth-century bastards take a time capsule from the past and come here?*

My head throbbed for a moment. Then a message spell from Team Leader Choi reached my ear.

—No.

I answered through Sound Transmission.

—What do you mean, no?

—Whatever it is, no. Just smile and let it pass. Prince Felix is famous for being an eccentric.

—If I break the back of his hand right now, won’t he become even more famous?

—No. Absolutely not!

—Just the back of his hand. Or maybe only one finger.

—I said no!

I hadn’t known that a message spell could convey this much emotion. Team Leader Choi must have been desperate in his own way.

*Fine. He’s a British prince. I can’t do anything about that.*

I was trying to swallow my anger when—

“Hey, Lord Fuck.”

*What now?*

I looked warily at Magic Johnson, who had approached me out of nowhere.

I had never expected much from Wu Heixing, who was famous for his anti-Korean sentiment and all kinds of trouble. But the joy of seeing S-rank Hunters I had only watched on television in person was gradually running out.

“……No, please. Don’t call me Lord Fuck. Use my name. Would you like it if I called you Dickson instead of Johnson?”

“Hmm. Now that you put it that way, I see your point. Then, Jin?”

“That’s much better. But why?”

“It’s nothing special. I was just wondering—are you really not planning to kiss the prince’s hand?”

“That sounds pretty special to me.”

I was dumbfounded and immediately asked back.

“Of course not. What is this, the Middle Ages? Would you want to do it if you were me, Johnson?”

“I would.”

“What?”

A flash of enlightenment shot through my mind.

I had completely forgotten. Magic Johnson was an American national hero—and a national gay icon.

*Time* magazine’s choice for “the world’s most influential LGBT person” was making a serious suggestion to me.

“So, I was thinking that I’d like to express my gratitude to the prince on your behalf, Jin.”

“……”

*He really knows how to package something.*

But unlike Magic Johnson, Prince Felix quietly withdrew the back of his hand.

“We are all equal human beings beneath God. Such outdated etiquette should disappear. Magic Johnson, I shall accept your kind offer at another time.”

“……”

*Was that really something for the same bastard who had just held out his hand to me to say?*

Faye Chen, who had been listening, muttered as though she found it absurd.

“My, he’s shameless. He may be one step above Wu Heixing, even if he hasn’t actually committed any crimes.”

“He’s still better than Wu Heixing. That guy should have been executed under the law.”

“That’s true.”

The arrival of one heavyweight after another had reduced Wu Heixing to a cowering nobody, but sparks flew from his eyes.

“Y-you, you fucking bangzi!”

“Stop going on about bangzi already. Even the national anthem gets tiring by the second verse. The same goes for me going easy on you.”

“……Giving me consideration? You?”

He sounded as though he genuinely couldn’t understand me, so I nodded.

“Yeah. I just became sure.”

I had a rough idea of what level Wu Heixing was at, but he had no idea who I was.

A fight began with gauging one’s opponent. This fight had ended before it had even begun.

“So stop picking a fight with me and leave while I’m asking nicely. Let’s each focus on doing our jobs.”

“You’re getting carried away because you’re an A-rank Hunter favored by Chairman Comrade, acting as if you don’t know how high the sky is—!”

“Ah.”

So that was why he had started this bullshit with me from the moment we met.

The reason was so predictable and childish that a quiet laugh escaped me.

“Come on. You’re way too fucking old for me to call this cute.”

“……!”

“What are you going to do? You want all of the Chairman’s expectations and attention focused on you, but some Korean guy has pushed you aside.”

“You……”

The moment Wu Heixing realized that I had seen through his true feelings, his face flushed with shame and fury.

Everyone’s attention had gathered on us by then. He must have felt the pathetic looks everyone was giving him down to his bones.

And people like him, when placed in a situation like this…

*Always cross the line.*

My prediction was exactly right.

His fingertips slid almost imperceptibly toward the hilt of his sword.

Broad-minded Chairman Shao Yang had not asked anyone present to disarm as a sign of trust, but that consideration would become poison to Wu Heixing.

*Draw it. Don’t hesitate.*

No matter how reckless I might seem, I still observed a minimum standard of propriety.

Until now, I had only held back because I had come to help China at the Chairman’s request. If Wu Heixing drew a weapon, I would have an excuse to rough him up without going too far.

*That’s right. More. Keep going.*

As though he were being controlled by me, Wu Heixing’s hand reached for the sword hilt.

And just as his fingers were about to seize it—

Step. Step.

The sound of several people’s footsteps echoed through the corridor outside the quiet underground bunker.

Wu Heixing’s hand stopped, and the tightly closed door opened at almost the exact same moment.

The moment I saw the person who entered alongside Minister of National Defense Wei Fenghu, Wu Heixing’s existence vanished completely from my mind.

“I’m late. Have you all been waiting long?”

He had thick, sharply defined features that looked as though they had been drawn with a brush, and a solid build that even his clothes couldn’t conceal.

He looked like a middle-aged man barely into his forties, but what hid beneath that skin was an old tiger and a sly snake.

*Lee Jungryong.*

When Lee Jungryong’s eyes met mine, a deep smile spread across his lips.

[^1]: *Bangzi* is a derogatory Chinese term for Koreans; “peninsula” refers to Korea.
## Chapter artifact 386

# Chapter 386

“I’m late. Have you all been waiting long?”

Lee Jungryong swept his gaze across the gathered people. Some faces were familiar, while others were strangers he was seeing for the first time today.

Magic Johnson and Faye Chen, whom he had encountered several times during the Great Cataclysm. The young British prince. And China’s problem child.

Every time his eyes met someone else’s, the S-rank Hunters gathered in the underground bunker greeted Lee first.

“Long time no see, Lee. You’ve become even more attractive since the last time I saw you. Every time I see you, I feel like confessing my love.”

“Please restrain yourself, Magic Johnson. You’re not my type. Faye Chen here might be, though.”

At Lee’s shameless reply, Faye Chen swept her long hair back.

“Oh my. I had no idea you felt that way about me, Mr. Lee. What a shame. I found out too late.”

“What’s there to regret? You’re still in your prime.”

“Thank you for saying that, but the young people will laugh if they hear you. They’ll ask what the old folks think they’re doing.”

“Is that really how it is?”

Under Lee’s gaze, Wu Heixing hurriedly waved his hands in denial.

“No, no, Mr. Lee. How could that possibly be?”

“I’ve heard a lot about you. You’re exceptionally talented and, hm, a young man who’s honest about everything.”

“Th-thank you.”

Wu Heixing lowered his head, looking deeply humbled by the honor.

He normally had the word *bangzi*—a derogatory term for Koreans—practically glued to his lips, along with his anti-Korean sentiment. But he lacked the nerve to show that side of himself in front of Lee Jungryong.

A bead of cold sweat rolled down the back of Wu Heixing’s neck.

“I’d heard you were coming, but I never expected you to actually show up.”

“Of course I had to come. When a neighbor is in trouble, shouldn’t we help them?”

“It’s an honor to meet you, Mr. Lee.”

Even Magic Johnson and Faye Chen, heroes born during the Great Cataclysm, could not compare to Lee Jungryong.

He was the sworn brother of Cheon Taemin, known as the Jesus of the twenty-first century and the savior of the world. He was also the de facto head of the Ares Guild.

One of the most powerful Guilds in the world. And one of the three strongest people among all the S-rank Hunters.

Lee Jungryong.

Anyone who faced him had to show the proper respect.

Even the overbearing Wu Heixing was no exception. Neither was the prince, despite his noble blood.

“Nice to meet you. A pleasure to meet you, Jungryong Lee.”

“Ah. So you’re that prince.”

“How impudent—”

Prince Felix raised a hand to stop his secretary, then inclined his head with elegant restraint.

“Felix. You may call me Felix. That will do.”

The Korean that came through the translation device was awkward, and his tone was hard to place.

But with those words, Felix Alexander Louis, third in line to the British throne, had made the difference between Lee Jungryong and everyone else perfectly clear.

He had gone so far as to let Lee omit the title *His Highness*.

Of course, Lee Jungryong did not care in the slightest.

*They’re all just brats.*

The only people Lee acknowledged were Magic Johnson and Faye Chen.

No matter their personalities, Wu Heixing and Prince Felix were still called geniuses by the public. But in Lee’s eyes, they were nothing more than chicks that had only just learned to walk.

And the people who truly grated on Lee’s nerves were somewhere else.

*The Peace Guild.*

Lee’s gaze shifted to one side. A deep smile formed at the corners of his mouth as he looked at the two people standing there in silence.

“I seem to be running into you two rather often these days. Have you both been well?”

At Lee’s greeting, Jin Taekyung and Choi Minwoo glanced at each other and shrugged.

“Not really.”

“Not particularly.”

“……?”

What?

Lee Jungryong unconsciously faltered.

It had been less than a month since he had last seen them. Yet something had changed dramatically in the way they treated him.

*Hostility.*

That was it.

The clear hostility and wariness he had sensed from them before were no longer there.

As Lee studied the two people who stood before him with such calm expressions, he soon realized why.

*They’ve grown stronger. So much stronger than before that there’s no comparison.*

There was no doubt about it. Choi Minwoo’s qi was far greater and more refined than before—so much so that Lee found himself wondering how he had managed to grow so much in such a short time.

And the other one, Jin Taekyung—

*……What is this?*

Lee could sense it through his skin and sixth sense: the immense qi contained throughout Jin Taekyung’s body, and the profound stillness in his eyes.

There could only be one meaning.

*He crossed the wall.*

The shock hit Lee like a blow to the back of the head. He had to struggle with all his might to keep his agitation from showing.

*How?*

Jin Taekyung had been a powerful man before, without question. Perhaps he had even stood above the countless A-rank Hunters throughout the world.

He had defeated two Named Monsters on his own. It was only natural that the people and media had been clamoring about the birth of a new S-rank Hunter.

But Lee Jungryong knew that Jin had not yet crossed the wall. He knew that it would take a very long time for the young man to overcome the barrier blocking his path and become a true powerhouse.

And yet—

*How can something this absurd happen?*

This was not something that could be described simply as surprise.

When Lee met Jin Taekyung’s calm gaze, he remembered emotions he had forgotten for a very long time.

Anxiety. Impatience.

It was the first time Lee Jungryong had felt such unease since taking complete control of the Ares Guild.

Only a few months ago, Jin had been nothing more than an amusing and irritating presence. Yet that same man had awakened feelings of anxiety and impatience within him.

*You bastard……*

The smile at the corners of Lee’s mouth vanished as though it had been wiped away. Wei Fenghu looked at his hardened face with puzzlement.

“Mr. Lee? Is something wrong?”

“……It’s nothing.”

“Hmm. Then may we begin the meeting?”

Lee Jungryong nodded without a word, but his gaze remained fixed on one person.

The young man leaning diagonally against the back of his chair, Jin Taekyung, muttered as though speaking to himself.

“Well, it looks like quite a lot is wrong.”

“……!”

“Well, forget it if it’s nothing.”

Without realizing it, Lee Jungryong clenched one fist tight.

* * *

The meeting in the underground bunker continued for a long time.

The Monster Wave had caused at least hundreds of thousands of casualties over the past week. That alone made it an enormous natural disaster and an unmistakable state of war. It was only natural that every decision had to be made with the utmost caution.

“Therefore, we should divide our forces into five armies and gradually pressure the enemy……”

Someone interrupted Wei Fenghu as he continued speaking with a grave expression.

“Minister of National Defense Comrade.”

“Speak, General Liao.”

The middle-aged man called General Liao wore a uniform weighed down with rows of medals. He stroked his beard before opening his mouth.

“After listening to the Minister of National Defense, I found it too stifling to remain silent. At this rate, moving so slowly, when will we ever deal with those monsters?”

*Wow……*

His tone was unbelievably obnoxious.

He was speaking that way to Wei Fenghu, the Chairman’s right-hand man and the highest-ranking man with real power in the military.

As though he had read my thoughts, Team Leader Choi sent me a message spell.

—The Communist Party also has its own factions. General Liao is a pure-blooded member of the Crown Prince Party, the largest faction in the Communist Party since his grandfather’s time. It is a rival faction to the Shanghai Gang, which Chairman Shao and Minister of National Defense Wei Fenghu belong to.

—The Crown Prince Party and Shang…what?

—……If we must rank them, it means the Crown Prince Party is number one and the Shanghai Gang is number two.

—Oh.

Until now, I had assumed that the Communist Party operated under a strictly one-party system. Apparently, they fought among themselves just as enthusiastically.

—But is that really allowed? If Chairman Shao simply pointed at someone and said, “That man is harmful,” wouldn’t they behead him in Tiananmen Square?

—They do it because they’re allowed to.

—……I mean, when you put it that way, I don’t have much to say.

—The factions reached an agreement. During the Great Cataclysm, the Chairman from the Crown Prince Party made so many mistakes that it became awkward for them to keep holding power.

—Ah. Pingping?[^1]

—Yes. Pingping.

[^1]: “Pingping” is a mocking nickname derived from Xi Jinping’s given name.

*That damn Great Cataclysm changed so many things.*

While I was listening to Team Leader Choi’s explanation, General Liao, a pure-blooded product of the Crown Prince Party’s youth ranks, came up with a brilliant proposal.

“Let’s use nuclear weapons.”

“……?”

“……?”

“Let’s formally request it from Chairman Shao and launch dozens of nuclear weapons across Sichuan. Wouldn’t that solve everything nice and cleanly?”

“……”

“……”

*What a fucking nuclear-crazed bastard.*

Everyone, myself included, looked at one another with baffled expressions.

But Wei Fenghu’s expression was the most impressive of all. He looked like he desperately wanted a handgun as he answered.

“Rejected.”

“Why! Are you ignoring me because I’m not part of the Shanghai Gang?”

“Say something that makes sense. Something that makes sense! What about the people who are still alive or haven’t suffered any damage? What are we going to do about the land that will be reduced to a wasteland?”

“Sacrifices for the greater good are unavoidable!”

*I don’t know about the rest, but he sure seems like a total oxhead.*

Magic Johnson, who had been listening quietly, suddenly spoke in his deep voice.

“The damage from a successful nuclear attack would be bad enough, but what are you going to do if someone uses spatial-transference magic to move the warheads? To Beijing, for example.”

“That’s why we have an Archmage like you……”

“Me? Our opponent isn’t an ordinary Lich. If that Arch Lich is more skilled at magic than I am, it could cause a truly irreversible catastrophe. Similar things already happened several times during the early days of the Great Cataclysm, remember?”

“B-but even so…… A sacrifice of this scale……”

“Hey. Motherfucker.”

Bang!

*That startled me.*

Magic Johnson shot to his feet, the muscles of his bronze-colored body rippling.

“Stop it. I like East Asian men, too. I might have to punish you.”

“……!”

“……!”

*That’s the scariest threat I’ve ever heard.*

General Liao’s face turned deathly pale as he looked around for help. But the officials who appeared to belong to his faction avoided his gaze, as did Wu Heixing, his last possible line of defense.

*So this is how it gets resolved.*

His opponent was an American national hero—and a national gay icon.

Everyone seemed desperate not to become one of the East Asian men Magic Johnson liked.

Of course, General Liao’s relentless stream of bullshit had played a major role as well.

“Enough, both of you. Especially you, General Liao. Stop saying things that are completely absurd.”

Under the direction of Wei Fenghu, the Chinese man who had just shut down that chink, the meeting proceeded quickly.

After gathering the opinions that had been raised and settling the arguments, Wei Fenghu secured everyone’s agreement before speaking with a weary expression.

“We will divide the six S-rank Hunters here and deploy them in six directions. According to the official military structure, each direction will receive three Army and Air Force divisions, along with Hunters from the Public Security Armed Forces Department.”

Three Chinese divisions and the Public Security Armed Forces Department.

I didn’t know the exact number of people that meant, but when it came to sheer manpower, it would be enormous.

When it came to the number of Hunters they possessed, wasn’t China always fighting for first or second place?

*Of course, the other side isn’t exactly harmless, either.*

The estimated casualties alone numbered in the hundreds of thousands.

If the Arch Lich had resurrected the dead as undead……

Then an almost unimaginable number of enemies would be waiting for us.

“This concludes the meeting. Please move out as soon as possible.”

Just as everyone rose from their seats after Wei Fenghu said that the exact troop numbers and force organization would be provided in writing, it happened.

“I need a word with you.”

A voice pierced my ear.

It wasn’t a message spell. It was unmistakably Sound Transmission.
## Chapter artifact 387

# Chapter 387

It was already deep into the night by the time we left the underground bunker.

I drew in a deep breath, and cold air seeped into my lungs. As I gazed up at the star-filled night sky, thinking of Sichuan in the Murim somewhere out there, a small hand tapped me on the shoulder.

“Coming with me? I’m thinking of having a light drink.”

“Now?”

“Yeah. Just us.”

It was Faye Chen. Two of the people included in that “us” stood behind her.

One of them spoke in a voice overflowing with dignity.

“Lady of the East, might there be any Romanée-Conti among the wine we shall share?”

“I’m no noblewoman, but of course I have some. Do you like wine, Prince?”

Prince Felix answered with a displeased expression.

“I told you to call me His Highness Felix, not Prince. And I enjoy wine in moderation. Especially the 1945 Romanée-Conti.”

“I don’t have the 1945 vintage.”

“Then I must decline. I shall be leaving.”

Was this guy actually insane?

As Prince Felix disappeared with his attendants, Faye Chen turned toward the one person left behind.

“You’re coming, right, Johnson?”

Magic Johnson grinned, baring his snow-white teeth.

“I’m sorry. Unfortunately, I think I’ll have to put it off until next time.”

“Why?”

“I might be deployed to the front tomorrow, so I’d feel more at ease if I at least prepared my spells with Memorize.”

As expected of an Archmage. Heroes of the Great Cataclysm didn’t become heroes for no reason.

Deeply impressed by Magic Johnson’s attitude, I opened my mouth.

“I don’t think I can go right now either.”

“No.”

“Why not?”

“You’re neither a prince nor an Archmage.”

“……That’s not how this works.”

Unbelievable. Leaving aside the fact that she was throwing around such unreasonable demands, that ajumma was something else for wanting to drink in a situation like this.

“You just cursed me in your head, didn’t you? You called me a clueless ajumma who only thinks about drinking in a situation like this.”

“……How did you know?”

“Oh my, look at how pointlessly honest this boy is.”

Faye Chen poked me on the tip of the nose with one long finger. She looked like a beautiful woman in her early twenties, but in reality, she was older than my mother, which gave me a strange feeling.

“How about you find someone else? Mr. Lee, perhaps……”

“Lee?”

Faye Chen tilted her head slightly. Lee Jungryong had disappeared a long time ago with the Ares Guild members he had brought with him.

“Hmm. He’s a difficult person somehow. He wasn’t like that during the Great Cataclysm, but he’s become such a slippery snake. You can never tell what he’s thinking.”

She had an excellent eye for people.

Faye Chen cast a sidelong glance at another candidate disappearing in the distance before continuing.

“Wu Heixing. He’s far too rude. Drinking with him would ruin the taste.”

I gazed blankly at Wu Heixing’s back as he headed into the secluded forest and answered.

“Nothing we can do, then. You’ll have to drink another time.”

“No. These are exactly the days you drink.”

“……?”

“It might be our last chance.”

“Ah.”

I thought I understood, at least somewhat, why Faye Chen was looking for a drink.

War exhausted people. At the same time, it brought unexpected farewells in the form of death.

This was her own eve-of-battle ritual, after losing countless comrades during the Great Cataclysm.

Once this crisis was over, one of us might have crossed the river from which no one ever returned.

“Well, since things have turned out this way, I have no choice but to change my target. Right, handsome young man?”

“I told you I’m not going.”

Faye Chen stared at me with an incredulous expression.

“Do you have no conscience? I mean the young man over there, not you.”

The handsome young man Faye Chen pointed out—Team Leader Choi—nodded readily, contrary to my expectations.

“If you would invite me, it would be my honor.”

“Uh, Team Leader. You’re really going?”

“Of course. When will I ever have another chance to share a drink with Faye Chen? Besides, there are a lot of things I’m curious about.”

Faye Chen giggled.

“I thought you were only handsome, but you speak sweetly, too. So, what are you so curious about?”

“The Equipment you’re wearing right now. Where did you buy it?”

“……That’s your question?”

“Yes.”

“He’s no pushover either.”

Magic Johnson burst into hearty laughter as he watched Faye Chen sigh deeply.

“Ha ha. Miss Chen, shall we all go have a drink together, then?”

“All together? Johnson, didn’t you say you weren’t coming?”

“I did. I have no interest in drinking alone with a woman. But if an attractive man like Mr. Choi here joins us, that changes things.”

“……”

“I like men. East Asian men in particular.”

“R-right. Let’s go.”

As expected of Time magazine’s choice for the world’s most influential LGBT person.

I sent Sound Transmission to Team Leader Choi, who was dragged away with his body stiff as a board.

“Call me if anything happens.”

Team Leader Choi looked back at me with sad eyes, like a cow being led to the slaughterhouse, then disappeared with the two S-rank Hunters.

I looked around before setting off.

*This was the direction.*

How long had I walked along the dark path, avoiding people’s eyes? I stopped in the pitch-black darkness and opened my mouth.

“Come out.”

After a brief silence, someone’s voice drifted out.

“……Not bad.”

Rustle.

Wu Heixing appeared amid the sound of movement and looked me up and down.

“How did you know?”

What kind of question was that? I answered flatly.

“You might as well ask me what one plus one is. That would be harder.”

“Hmm. So you were more capable than I expected.”

“Don’t pretend to praise me now. It’s obvious you’re trying to pull some cheap trick.”

“……!”

I had hit the nail on the head. Wu Heixing’s face flushed bright red.

In a way, he was remarkably easy to handle. I knew he was well into his thirties, but it was hard to believe anyone could be this simple-minded at that age.

“It wasn’t like that. I sincerely……”

“You sincerely think I’m a bangzi. You were annoyed because some Korean who isn’t even an official S-rank Hunter yet was getting more attention than you. You picked a fight first with your usual one-dimensional behavior, but the reaction wasn’t good, and that bangzi turned out to be less of a pushover than you expected, right?”

I continued firing off words like a machine gun without giving him a chance to answer.

“So now you’re throwing out a few compliments you don’t mean and making friendly gestures, trying to pull some kind of trick…… Wait. Is any part of what I just said wrong?”

“……”

“Yeah, I’ve seen plenty of people like you. After getting hit in the back of the head so many times, even the brain that wouldn’t work started spinning.”

I gave him a contemptuous look, and the red-faced Wu Heixing began to stammer.

“I wasn’t trying to pull some other trick.”

“Then what? If you’re thinking of becoming friends with me, fold that idea up neatly and put it away. If you stand next to shit, the smell gets on me too.”

“……!”

“But what are you doing right now?”

At my quiet question, the hand moving toward his sword hilt stopped abruptly.

“Don’t draw it. You’ll get hurt.”

Wu Heixing looked at me with conflicted eyes before suddenly speaking.

“You already knew everything…… So why did you come along so willingly?”

“Because I had something to ask.”

“What?”

I looked straight into Wu Heixing’s eyes and opened my mouth.

“Sound Transmission. Right?”

“……!”

His stiffened face was answer enough. I had wondered if it was possible, but apparently it was. I scratched the back of my head and muttered.

“I guess it is. Well, this is the mainland, so I suppose various martial arts could have survived here. An internal-energy cultivation technique, for example.”

“W-what are you talking about? That was message magic……”

“Well, look at you.”

A snort escaped me at the sight of him hurriedly making excuses.

Other people who had never encountered martial arts might not be able to tell the difference, but he couldn’t fool me.

*Take a look at me for a moment.*

What had reached my ear near the end of the meeting had unquestionably been Sound Transmission.

I had responded to an invitation I could have ignored because Wu Heixing himself had been the one to send it.

“H-how did you know that?”

“Why? Was it a secret no one else knew?”

I stared at the flustered Wu Heixing and continued.

“I thought it was possible, but it’s still fascinating. Didn’t you wipe out all the martial artists during that whole Cultural Revolution business? Somehow, martial arts survived even through that.”

“Shut your mouth!”

“Oh, right. You said your family was powerful. Did the highest-ranking Communist Party officials quietly smuggle it out by abusing their positions?”

“……”

His expression sank instantly. I must have been right.

As a foreigner, I didn’t know how serious a problem this was, but I understood the value of internal-energy cultivation techniques—in other words, what was called mana cultivation in the modern era.

*If this had been the Murim, there would have been a river of blood.*

He had been caught hiding away a golden calf like that. Naturally, Wu Heixing wasn’t reacting well.

“It would be wise never to speak of what you just said again.”

“I had no particular intention of doing so, but your tone is pretty damn offensive.”

Wu Heixing glared at me with vicious eyes.

“Would you still act like this after learning who my father is?”

“I don’t know who your father is, but he sounds like he might have been a former Red Guard.”

“……!”

“Wasn’t your father the one who went around with a sledgehammer in his youth, smashing Confucius’s tomb?”

“You fucking bangzi bastard!”

Flash!

With a furious shout, his body shot forward.

The Aura Blade surging from the straight sword already drawn from its sheath—no, the Sword Force—flew toward my throat.

Whoosh!

The cool wind scattered my hair. I bent backward until my waist nearly touched the ground and avoided the Sword Force, then sprang up and drove my knee into his chin.

Crack!

Teeth and blood flew into the air. As Wu Heixing staggered, I seized both his arms and whispered into his ear.

“I told you not to draw that sword.”

Sizzle. Crack!

“Aaaaaaargh!”

The powerful Scorching Yang Qi in both hands shattered his armor and burned his flesh.

Wu Heixing’s scream was blocked by the qi barrier I had spread out and failed to travel any farther.

“You bastard!”

Whoosh!

This guy had even learned fist-and-foot martial arts. Unlike his shoddy sword technique, this was fairly sharp.

Of course……

*Compared to the Murim, the quality of the martial arts is far lower.*

I felt a slight sense of disappointment as I reached out.

Boom!

Internal energy collided with internal energy.

His leg, swung like a whip toward my waist, could go no farther.

Wu Heixing’s eyes trembled with shock and disbelief.

“H-how?”

“I’m good.”

I grabbed his ankle and slammed him into the ground with all my strength.

Whoosh! Boom!

Once more.

Whoosh! Boom!

Again. And again. And again.

Boom! Boom! Craaash!

The ground overturned, while rocks and trees were ripped out.

When the living pickaxe work finally stopped, Wu Heixing lay spread-eagled inside a huge crater, looking as though his soul had left his body.

“Still, you’ve got a sturdy body, so you’re not hurt that badly.”

“Urgh…… ugh……”

“Hey, are you crying?”

“Uuuugh……”

He was completely out of it.

Clicking my tongue, I bent over and searched his pockets.

After rummaging through the pouch enchanted with spatial expansion magic for a while, I finally found what I was looking for.

“Ah, here it is. A high-grade potion.”

> **System**
>
> **Acquired:** **Top-Grade Potion**

“……No, wait. A top-grade potion? What the hell, you bastard?”

I stared at the sprawled-out Wu Heixing with startled eyes. Even if he was an S-rank Hunter, carrying something like this around was absurd.

High-grade potions were rare enough, but top-grade potions were items that appeared maybe once or twice a year.

Leaving aside their almost unreal price, they were so scarce that even people with money couldn’t obtain them.

*I’m seeing one here after only ever seeing them online.*

After a moment’s hesitation, I slipped the top-grade potion into my Inventory. Then I searched through his pouch again, found a high-grade potion, and poured it over him.

“I’ve got my settlement payment, so I’ll let you off here. You’ve got plenty to be worried about yourself, so if you go around telling people about what happened today…… You know what’ll happen, right?”

“Ugh…… uuuugh……”

“Okay. We’ve reached a settlement.”

Just as I was wrapping things up neatly, the phone in my pocket began to vibrate.

A short text from Team Leader Choi was waiting for me.

> Team Leader Choi
>
> Team Leader Choi
>
> Mr. Ji nTaekyung, pl ease come quickly.

“……”

*No, Johnson.*
## Chapter artifact 388

# Chapter 388

“Hey. Hey.”

Tap. Tap-tap.

The tip of someone’s foot prodded Wu Heixing in the side. He barely opened his eyes, and a large figure looming over him swam into view.

“Uhhh……”

“I’ve got something urgent to take care of, so I have to get going. If anyone comes by, make up a convincing story for them, will you?”

“Ugh… uuuugh……”

“I poured a potion over you, so quit pretending you’re dying, you bastard. If you keep it up, I might call Magic Johnson and make you produce some real moans. See you!”

Whoosh!

After leaving him with a parting remark that made his butt ache just from hearing it, the person’s presence vanished into the distance in an instant.

It was only ten or so minutes later that Wu Heixing, who had been lying spread-eagled on the ground, finally let out a voice boiling with rage.

“Jin Taekyung……!”

The broken bones and torn flesh had recovered thanks to the high-grade potion, but it couldn’t heal the pain etched deep into his bones or his cracked pride.

*How?*

He couldn’t believe it. No matter how agitated he had been, how could he—a S-rank Hunter—have been so thoroughly toyed with?

The fact that Jin Taekyung had seen through his martial arts was shocking, but Wu Heixing took even greater offense at the defeat itself. He had always been fiercely proud of the power he possessed.

*Me? Me, of all people?*

Wu Heixing had been born with a Hunter’s destiny.

As an infant, he had been recognized for his potential through an extremely expensive mana aptitude test, and his family, part of the highest ranks of the Chinese Communist Party, had spared no expense in supporting him.

Enormous wealth and power accumulated through corruption. Raised in the finest environment with the best possible support, Wu Heixing awakened as an A-rank Hunter at the age of twenty. Ten years later, he achieved the astonishing feat of becoming an S-rank Hunter.

And yet……

*Then why? Why was I defeated by that bastard bangzi from such a tiny country?*

A strange light flashed in Wu Heixing’s eyes as he glared at the pitch-black night sky.

His gaze held anger, jealousy, and even a trace of fear toward the power Jin Taekyung had displayed.

Those were also emotions Wu Heixing had been sickeningly familiar with for more than a decade.

Toward someone who could no longer be found, Wu Heixing shouted.

“Was this your doing? Are you trying to torment me even after you’re dead?!”

The public and media cursed him as an irredeemable delinquent while praising him as a genius born of Zhonghua, but a tiny handful of people, Wu Heixing included, knew the truth.

There was a true genius apart from him. That was why they had kept that person hidden and out of sight.

“Answer me, Lei Fei!”

With not only overwhelming skill but also a noble character, Lei Fei had been an insurmountable wall to Wu Heixing.

How flustered—and delighted—Wu Heixing had been when he first heard that Lei Fei had disappeared.

But within only a week, another wall had appeared.

A wall named Jin Taekyung.

“Gaaaaaaaah!”

It was then that the bushes shuddered at the echoing cry.

“I know that feeling too.”

At the low voice of someone who had approached without making a sound, Wu Heixing sprang upright like lightning.

“Who are you?!”

“That hurts. I thought we knew each other.”

Step.

A man suddenly stepped out of the darkness. Wu Heixing’s eyes widened.

“You’re……?”

Beneath the faint moonlight, Lee Jungryong continued with a smile.

“I believe we have something important to discuss. What do you say?”

“……!”

* * *

Ding.

> **System**
>
> **Circulate Your Qi** completed!
>
> The realm of **Fire Gate Divine Technique** has risen slightly!

By the time I finished gathering my qi and opened my eyes, the world outside was already growing bright.

As though it had been waiting for this exact moment, the Skeleton Warlord immediately opened its mouth.

> “Wicked human. Are you finally awake?”

“I wasn’t asleep, you idiot.”

> “You drank alcohol before a battle. Tsk, tsk.”

“I’m not going to get a hangover, so shut up.”

Drinking too much alcohol caused liquor toxicity to build up, but any decent martial arts master could drive it out with ease.

And with my formidable Scorching Yang Qi, I had even less to worry about.

*Come to think of it, I really did drink a lot. I drank all the alcohol Faye Chen had brought over on her private jet.*

I had definitely gone there to stop Magic Johnson, but I wasn’t entirely sure how things had turned out that way.

> “But human. How long do you intend to remain in this stuffy place?”

“I was planning to leave anyway.”

I checked the time. Five-thirty in the morning. It was about time to get ready.

After packing my things in the hotel room assigned as my temporary lodging, I went down to the lobby and saw Team Leader Choi drinking coffee.

“Oh, Team Leader.”

“……You’ve come out.”

A quick glance revealed dark circles under his eyes. His skin, usually so meticulously cared for that it didn’t have a single blemish, looked rough and dry.

“Did you not sleep?”

“If you were in my position, Mr. Jin, would you have been able to sleep?”

“……”

Fair point.

The sight I had witnessed after racing over in response to the most desperate emergency text in the world the previous night had been nothing short of horrific.

*‘Hey, Choi. It’s just a drinking game. Come on, be cool and do it once. What do you say?’*

*‘Faye Chen! Please help me, Faye Chen!’*

*‘Hmm…… Sorry, but it’s a drinking game. The king’s command is absolute. Isn’t that the rule?’*

*‘Even so, a kiss?! I’ve never even played a drinking game before! You didn’t explain the rules properly!’*

*‘Oh, I don’t know, I don’t know. Number two will kiss number three on the cheek. That’s my command.’*

*‘Choi. Stay still. I don’t want to cast a binding spell on you.’*

*‘This is absurd…… Mr. Jin! Over here, Mr. Jin!’*

*‘Jin. Don’t interfere. I don’t want to cast an offensive spell on you.’*

If I had been even one minute later, a catastrophe would have occurred.

I had been forced to down an enormous amount of alcohol in exchange for rescuing Team Leader Choi, but I didn’t regret it in the slightest. I had been promised fair compensation in return.

“You remember the promise you made yesterday, right? About adjusting my settlement ratio.”

“……I remember. Nine to one.”

Team Leader Choi glared at me coldly.

“How could you do that in such an urgent situation? Are you even human?”

“Then give me a really passionate kiss right now. Number two is coming over, as it happens.”

He might have been number two, but his gayness was second to none in the world.

Team Leader Choi spotted Magic Johnson—a huge Black man who had just entered the lobby—and sprayed coffee all over the place.

“Ptooey! Please, please hide me.”

“I think it’s already too late.”

The moment I finished speaking, Magic Johnson spotted us and waved a hand as big as a cauldron lid.

“Hey, gays!”

Wasn’t it supposed to be *guys*? He must have said it wrong…… right?

Magic Johnson approached us as Team Leader Choi and I stared at him in disbelief, then burst into hearty laughter.

“Don’t look at me like that. I got a little too excited yesterday and played just the tiniest prank.”

“……You were really excited?”

“Ah, that came out wrong.”

“Please watch what you say. You startled me.”

“Haha. Anyway, there were circumstances yesterday.”

“……What kind of circumstances?”

“Huh? No, not *those* circumstances.”

“Please watch your words. You really startled me.”

“Please, both of you, stop. I’m afraid someone will hear you.”

With a look of complete resignation, Team Leader Choi downed the rest of his coffee and turned his head.

A group of people had entered through the hotel’s front doors and was walking toward us.

“It’s time to leave, gentlemen.”

The voice of Wei Fenghu, the Minister of National Defense, who was at the head of the group, was stiff with tension.

At his signal, a military general who looked well into his years handed out folders one by one.

“What are these?”

“Information on the areas where you gentlemen have been assigned and the troops stationed there. Of course, we’ve already provided them with the necessary information and contacted them in advance. From this point on, we will travel by the designated jets.”

I suppose this was one of the conveniences of living in an age where cutting-edge technology had advanced so far.

A short while later, at the temporary airfield we reached by following Wei Fenghu, I saw several familiar faces surrounded by tight security.

“Did you sleep well, young people?”

“……”

“You’re late.”

Faye Chen greeted us while stretching her arms high overhead. Perhaps because of what had happened yesterday, Wu Heixing silently kept his eyes lowered, while Lee Jungryong wore a strange smile.

The Skeleton Warlord, safely stored in my Inventory, spoke in an uncomfortable voice.

> “That human is unpleasant for some reason. This commander does not like him one bit.”

“I agree.”

Faye Chen raised an eyebrow at my quiet mutter.

“Hm? What did you say?”

“Nothing. By the way, where’s Prince Felix?”

“He left just before dawn. Apparently, a battle signal came from the area he was assigned.”

“……I see.”

Another battle, less than twenty-four hours after arriving.

The words *war* suddenly seemed to squeeze a corner of my heart.

Our nationalities and upbringings were different, but knowing that human beings like me were being slaughtered somewhere made my heart heavy.

“Hey, young man.”

“Yes?”

Faye Chen had been staring at me intently. She reached out and gave me a light tap on the shoulder.

“Relax your shoulders. If they’re that heavy, will you even be able to swing your spear properly?”

“……”

“Don’t blame yourself, and don’t be in such a hurry. Don’t try to take responsibility for every death.”

Responsibility.

I thought about it for a moment before answering honestly.

“……I don’t know. I’m not very confident I can do that.”

“Well, you certainly drank yourself senseless yesterday, for someone who feels that way.”

“That was……”

“I know. I’m joking. People like us forget the burden for a little while that way. Our lives might end tomorrow—or even today.”

The content didn’t match her bright voice. The hero who had made her way through the Great Cataclysm with every inch of her body looked up at the sky.

“Ah. Perfect weather for a fight.”

She turned and began walking lightly toward the jet, which had finished preparing for takeoff.

Leaving behind one quiet remark.

“Let’s all…… see each other alive.”

Her back disappeared inside the aircraft.

Magic Johnson gazed up at the sky for a moment with an oddly sentimental look, then suddenly opened his mouth.

“Hey, Choi.”

“Yes?”

“You relax your butt, too.”

“……”

“No, your shoulders. Let’s see each other alive again.”

*That sounded like his true feelings slipping out.*

Magic Johnson laughed heartily at Team Leader Choi’s wary look and boarded the aircraft after Faye Chen.

Wu Heixing followed, walking as though he were trying to escape. Finally, Lee Jungryong, the last one remaining, swept his strange gaze over Team Leader Choi and me.

“Take care of yourselves. We can’t go and die in a place like this, can we? Not at such a young age.”

*What a way for an old man to talk.*

It was an incredibly suggestive remark.

With Team Leader Choi’s face hardening, I smiled and opened my mouth in his place.

“That’s right. Unlike certain people, we’re too young for our deaths to count as a blessing.”

“……!”

“If you do kick the bucket, I’ll make sure to give a generous funeral contribution.”

“I’ll be counting on it.”

After a brief silence, Lee Jungryong tossed out that one remark and led the Ares Guild members away.

Now only Team Leader Choi and I remained.

I stretched as hard as I could, then patted Team Leader Choi on the shoulder.

“Let’s go, Team Leader.”

“Yes. We should.”

“No need to be nervous. Relax your butt.”

“……”

“……That was a joke. I’m sorry.”

*One more joke like that and he looked ready to kill me.*

I was cautiously watching Team Leader Choi’s expression as I boarded the aircraft when it happened.

“Unit—attention!”

A booming shout erupted behind us.

Wei Fenghu stood at attention and saluted us, his half-gray hair fluttering in the wind.

The people filling the airfield followed Wei Fenghu and raised their hands in salute.

It was a gesture of respect for the heroes going to fight for their families and friends.

Their salutes did not end until the jet’s door closed and it disappeared from view as a tiny, distant speck.

*Good grief.*

With this much of a send-off, there was no way my shoulders wouldn’t feel heavy.

I leaned back into my seat, suddenly feeling tired. The next moment—

Crackle. Crrrackle.

“……swer. Respond. This is……”

Along with the static-filled radio transmission suddenly coming from the cockpit, an alert pierced my ears.

Ding.

> **System**
>
> A Sudden Quest, **The Desperate War Situation**, has been generated.
>
> You cannot refuse this Quest. Arrive as quickly as possible and defeat the enemies!

“……”

*Damn it. This is just how my life is.*

I let out a deep sigh, then shouted toward the cockpit.

“Sir, floor it!”

* * *

“Where are they?”

The person who spoke was an old man in his eighties. His face was covered in wrinkles and age spots. His aged body was no longer what it had been in his youth, but his eyes held even greater power than they had back then.

Even through the holographic screen, the old man’s powerful gaze could be felt. Wei Fenghu swallowed hard before answering.

“They have all departed, Chairman Comrade.”

“How is the situation at the front?”

“We cannot easily determine the enemy’s movements because of the communications interference caused by magic and the barriers, but we are doing our best to detect their movement.”

“If the S-rank Hunters arrive……”

“With their strength, they should be more than capable of turning the tide.”

“Don’t jump to conclusions. Do not let your guard down for even a moment. The lives of countless people depend on our decisions.”

“Yes. I will keep that in mind.”

After the brief communication with Wei Fenghu, the Minister of National Defense, Shao Yang, Chairman of China, sat alone in the vast conference room and fell into thought.

*How did things come to this?*

This was an unprecedented catastrophe since the Great Cataclysm. Despite pouring in vast amounts of personnel and money, they had been unable to stop the monster army centered around the Arch Lich.

He had wanted to prevent panic if at all possible, but if they delayed any longer, the opportunity might disappear forever.

That was why Shao Yang had come here today, despite the countless objections within the Communist Party.

“They’re ready.”

“……Connect me immediately.”

At his secretary’s words, Shao Yang opened his eyes.

In the empty seats of the spacious conference room, holographic figures began appearing one after another.

Fourteen people of different races and genders.

No—fifteen, including Shao Yang.

Each of them was the leader of a nation, and they all belonged to a single institution.

*The United Nations Security Council.*

The elderly Chairman announced the start of the emergency meeting in a heavy voice.
## Chapter artifact 389

# Chapter 389

It was a day when the cold snap had finally eased.

The students who had at last been freed from the college entrance exam were busy either preparing to retake it or having fun, while office workers boarded public transportation with dark circles hanging heavily beneath their eyes.

Then, in the midst of that peaceful, ordinary routine, a bombshell no one had seen coming dropped.

> **Urgent Breaking News—Major Announcement from the United Nations Security Council**

The video, just over thirty minutes long, began with Chairman Shao Yang staring into the camera with a grave expression.

“I stand before you as the ninth President of the People’s Republic of China and a member of the United Nations Security Council to speak about the massive Monster Wave that has occurred in Sichuan Province.”

It was a bombshell that drew the attention of the entire world and shook all of Asia.

* * *

One day passed, then two, then three. Even after four days, the situation had not calmed down.

There had been countless incidents and disasters since the Great Cataclysm, but the Monster Wave that had occurred in Sichuan Province was unprecedented in scale.

Chairman Shao Yang of China officially declared martial law, and with the approval of the United Nations Security Council, peacekeeping forces were deployed to the front.

The entire world was watching.

The Asian countries bordering China were especially on edge.

Korea was no exception. Even today, the Hunter Issues section of the country’s largest online forum was boiling like a cauldron over charcoal.

**Here’s a summary of the situation so far.**

**There isn’t anyone here who hasn’t watched the Security Council’s major announcement video, right? If there is, go die somewhere. This is a genuine emergency. The supreme leader up north has probably already watched the whole thing on iTube and is lurking on this board, too.**

**Anyway, so many insect bastards kept asking someone to summarize something their own lives depended on that I finally got fed up and wrote this.**

**1. An unexplained massive Wave occurred in Sichuan Province. Current estimated casualties: at least 300,000.**

**Of course, that was a week ago, so the current figure is probably incomparable. At this point, I doubt it’s even possible to gather accurate statistics.**

**2. The Chinese government stepped in, but the scale was far crazier than anyone expected.**

**A monster army numbering at least tens of thousands has gathered around something called an Arch Lich.**

**The People’s Liberation Army and Air Force got absolutely wrecked, while more than two thousand Hunters from the Public Security Armed Forces Department have gone missing. Communications were cut off by magical interference, and satellite surveillance was neutralized, so they can’t even confirm whether those Hunters are alive.**

**3. The Chinese government secretly contacted several countries and hired a number of S-rank Hunters to suppress the situation as quickly as possible. The United Nations peacekeeping forces were deployed to the front two days ago, and they’re fighting desperately.**

**The Security Council is updating the battle situation, so anyone interested can check it out here.**

*(Link attached.)*

**Everything below this is just my personal opinion, so there’s no problem if you skip it.**

**4. Anyone with a properly functioning brain already knows this, but the current situation isn’t merely serious. Mainland China is practically hell on earth.**

**They’re pulling every useful Hunter they can find and sending them to the front, which means the mana levels of other Gates that are being neglected are unstable, too. Hyperinflation is happening in every area.**

**The truly frightening thing is that if the front collapses and the monster army advances beyond Sichuan…… I’ll leave the rest to your imagination.**

**5. So go to the supermarket and buy emergency food before everyone is completely screwed. Of course, I’m not telling you to hoard supplies and make unfair profits.**

**6. It felt like a shame to end it here, so I’m adding some national pride.**

**Our Lord Fuck and the Ares Guild’s Jung Dragon are active on the front. Keep hyping them up as hard as you have been.**

**The end for real.**

Within only a few hours of being uploaded, the post passed 100,000 views and caught fire beneath the comments of netizens who had been watching the situation closely.

> **Best comment:** The situation really is as serious as the post says, but the author is setting the mood way too hard lol. They say S-rank Hunters are fighting alongside 100,000 ordinary Hunters. What’s there to worry about? Is the military just sitting around?
>
> └ Yeah. They’re sitting around in maintenance depots right now.
>
> └ ……?
>
> └ Didn’t you watch the news? All the Chinese military’s Equipment broke down this time, exposing the largest military procurement corruption scandal ever. They say it’s worth at least tens of trillions of won. Apparently, more than one or two divisions are stuck in place.
>
> └ Huh. This sounds like something I’ve heard a lot before.
>
> └ Please change the canteens already, you motherfuckers. I got out last year, but why did the water in my canteen still taste like it came from Normandy? After one sip, I couldn’t even tell whether my name was Kim Cheol Soo or James.
>
> └ Corporal Kim. Tonight’s dinner is boneless pollock braised in sauce.
>
> └ I’m not eating, fuck.
>
> └ Anyway, the military being stuck because of broken Equipment is a problem, but they’ve got manpower to spare, so they’re probably fine. Hunters are the only ones who can actually inflict meaningful damage on monsters, after all. The real problem is something else.
>
> └ What?
>
> └ The monster population has broken through 100,000.
>
> └ ??
>
> └ ?????
>
> └ What do you mean, 100,000? Don’t talk bullshit.
>
> └ It’s not bullshit. It’s official information announced by the United Nations Security Council. Follow the link in the post and check it yourself. It was posted five minutes ago.
>
> └ Wow…… fuck.
>
> └ Judging by the reaction to the comment above, I guess it’s true. Holy shit.
>
> └ No. That’s just because it’s all in English and I don’t understand what it says. I’m running it through Gargle Translator right now.
>
> └ Is this guy insane?
>
> └ Hey, but if the number of monsters really has broken through 100,000, isn’t that a huge problem? Until now, the largest Monster Wave we’d ever seen hadn’t even reached a thousand monsters, had it?
>
> └ Naturally, this Wave wasn’t anywhere near this large in the beginning. The problem is that there’s an Arch Lich over there. Even an ordinary Lich appearing would be a major incident, but that one is an apex named Monster unknown even to academia. Practically speaking, most of the monsters fighting right now are undead resurrected by the Arch Lich.
>
> └ Arch Lich: “Kaioken, times one hundred.”
>
> └ Then can’t we just kill the Arch Lich? If most of the monsters are undead, killing the controller should end everything, right?
>
> └ ???????
>
> └ Who’s going to kill the Arch Lich, and how, you fucking idiot? The guy who uses an Aura Blade with his keyboard has nothing but a mouth.

A fierce debate raged on.

Some of the commenters watched the situation from a safe distance, as though they were watching a fire across a river, while others took the crisis seriously.

Even as doomsday theories and optimism battled for control, new information continued to pour in.

> **Best comment:** Security Council official report: The front in the east-west sector was breached one hour ago. Fortunately, Faye Chen arrived with reinforcements and stopped the damage from spreading.
>
> └ Holy shit, it’s real.
>
> └ If it’s the east-west front, isn’t that where Wu Heixing is?
>
> └ Yeah. That Chinese junkie.
>
> └ But why did it get breached? He’s an S-rank Hunter.
>
> └ Because he’s a Chinese-made S-rank Hunter.
>
> └ Ah……
>
> └ If Faye Chen hadn’t been there, this could’ve become a real disaster. Maybe it’s because Faye Chen is a well-made Hunter forged by the Great Cataclysm.
>
> └ Faye Chen is Hong Kong-made. Her parents had Hong Kong citizenship.
>
> └ Do you work for the comment quality-control committee? That was fucking clear.
>
> └ While we’re at it, does anyone have news about the Korean Hunters?
>
> └ Jung Dragon has taken charge of the northern front and is gaining the upper hand. I heard Lord Fuck won two or three times on the western front, but there hasn’t been any news since then, so I guess he’s maintaining the current situation.
>
> └ Hmm…… I’m not worried about Lee Jungryong, since everyone knows how skilled he is, but is Lord Fuck safe? He’s still an A-rank Hunter, after all.
>
> └ ??ㅋㅋㅋㅋ
>
> └ ㅋㅋㅋㅋㅋㅋㅋㅋㅋㅋㅋㅋㅋ
>
> └ There’s still an innocent idiot who treats Lord Fuck like an A-rank Hunter lolㅋㅋㅋㅋㅋㅋㅋㅋㅋㅋㅋㅋㅋ As a current A-rank Hunter, all I can do is laugh. That Jin Taekyung guy is just a monster lol.

> Hey, hey, h-hey!! The Se-security Council just announced the w-western front status!
>
> └ Oh, news about Lord Fuck. It’s been a while.
>
> └ You sound incredibly frantic. The western front? What does it say?
>
> └ It says it was breached?
>
> └ Huh?
>
> └ Huh?
>
> └ What are you talking about? Don’t tell me Lord Fuck is dead……?
>
> └ Wait. What is this saying? Everyone, I’m going to watch it again and come back. It’s on the main page, so go check it yourselves.
>
> └ Ah. I’m suddenly freaking the hell out; I’m going in right now.
>
> └ Go go go go go.

The netizens who had been enthusiastically writing comments hurriedly accessed the United Nations Security Council website.

An excessive number of visitors had temporarily flooded the site, causing a traffic overload, so they had to wait for quite some time. At last, when the announcement appeared on the main page, they could do nothing but doubt their own eyes and ears.

“……What is that?”

It was a map showing the standoff with the monster army. The front had formed an oval, but the western front had been gouged inward like a spike.

> I just checked. It really was breached.
>
> └ Is Jin Taekyung dead? How bad are the casualties?
>
> └ No, the monsters’ side was breached.
>
> └ ??
>
> └ ???
>
> └ The breakthrough was so fast that the updates couldn’t keep up.
>
> └ ……Does that even make sense?
>
> └ Shut your mouth and pull down the shutters. Today is the Lady of the House’s memorial day….[^1]

[^1]: Korean netizens traditionally call for a tavern proprietress and drinks when celebrating a surge of national pride; the speaker jokes that the tavern is closed because she is dead.

* * *

The battlefield where a fierce battle would soon erupt was crowded. An endless wasteland stretched before us, filled with more monsters than I could count.

The wind blowing from somewhere carried their thick killing intent and stench with it.

“Damn. They sure gathered in force.”

Team Leader Choi, standing beside me, answered my mutter.

“No matter how many we kill, they never seem to end.”

It was the fourth day since we had been deployed to the western front and the battle had begun in earnest. There was no trace left of Team Leader Choi’s usually immaculate appearance.

Covered in blood and dust, he looked at me with calm, deeply sunken eyes.

“When do we begin?”

“Well, we’ll have to hear what our little commander has to say. Right?”

The last question wasn’t directed at Team Leader Choi.

The twenty-one-year-old ‘little commander’ who had remained at my side the entire time answered.

“I’ll follow Teacher Jin’s orders!”

A snort escaped me at his sparkling eyes.

“You’re still on about calling me Teacher. You were the one who told me to drop the formalities first. I told you to call me hyung instead.”

“Are you really sure that’s all right?”

“I told you it was fine as long as you were okay with it. But is this really all right in front of your men? You said you’re getting promoted to major general now, didn’t you?”

Shao Shen shook his head at lightning speed.

“No problem at all! H-hyung, hyung!”

He was frighteningly calm in battle, so I had no idea why he stammered so much in everyday life.

I looked at the Hunters from the Public Security Armed Forces Department lined up behind him. There were roughly a thousand of them.

Their fever-bright eyes held admiration and awe for the strong.

Of course, Shao Shen stood out above all the rest.

“Give the order, h-hyung.”

“The order, huh?”

I suddenly looked up at the sky.

An eagle with enormous wings spread wide circled overhead.

I had a good feeling about today, too.

“Follow me. Just as you’ve done until now.”

“……!”

“Right now.”

I stepped forward as I answered.

Crack.

The force of ten thousand geun packed into my toes made the ground split like a spiderweb and cave inward.

Then, in the next moment—

Boom!

With a deafening roar, I shot forward like a streak of light.

*Flamefire Path.*

The cold-laden wind heated up and transformed into a blast of hot air.

The ground, wind, and scenery flashed past me in an instant. Then a tremendous roar erupted from behind.

“Charge! Charge!”

“Descendants of Zhonghua! People! Sweep them all away!”

“Waaaaaaah!”

Thud-thud-thud-thud!

Kyaaaauuuuu!

The shouts of humans and the howls of monsters rang across heaven and earth. A tremendous vibration shook the foundations of the world.

At the mouth of that chaos, I swung the White Flame in my hand with all my strength.

Whoosh!

The Extreme Yang Force surging from the spearhead cut through everything in its path.

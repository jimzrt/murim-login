# Checkpoint Review — 500–504

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

# Chapters 500–504

## Plot

Jang Taebo accepts his appointment as Master of Ironcraft Hall and takes charge of processing the Water God Dragon’s remains, recruiting renowned artisans and arranging transport under his and Wipeng’s supervision. Zhuge Feng completes the Demon-Sealing Formation, which blocks the mana leaking from the exposed Gate by drawing on the qi of the natural world. Taekyung warns that Dark Heaven caused the incident deliberately and may repeat it; Jin Wikyung identifies Henan and the New Murim Alliance as the next priorities.

The New Murim Alliance is scheduled to be founded at Mount Song in Henan Province in one month. Jin Wikyung explains that its orthodox-centered coalition must also attract the fractured unorthodox factions before Dark Heaven does. He reveals that he proposed the political arrangement that enabled the government-backed purge of Hubei’s dark-path forces, using Hongcheon, the new Provincial Administration Commissioner and Prince Shangshan’s hidden loyal retainer. Taekyung decides to leave Hubei with those close to him and those he hopes will remain beside him.

Mungyeong finds Jeok Cheongang secluded in a cave after seven days and nights without food or water. Jeok’s leaking innate qi has caused progressive lapses in memory and time, and he fears becoming a burden to Taekyung. He asks Mungyeong to protect Taekyung and become his new Master if Jeok is no longer present. Mungyeong instead tells him of a ninja who abandoned his elderly mother, leading Jeok to recognize that leaving Taekyung would be proud self-denial rather than selfless protection.

Jeok accepts Taekyung’s support and remembers that Master and Disciple have always walked side by side. His Heart Demon and the memories binding him break apart, and he rises into a new realm as powerful qi erupts around him. Mungyeong leaves the cave, Taekyung reunites with Jeok after more than a year, and Jeok is persuaded to travel with Jin Wikyung’s party to the New Murim Alliance. Zhuge Feng also recounts how his grandfather’s gamble redirected the Black Wind Corps through Mount Jiuhua, enabling Jeok to annihilate it and earn the title of Fire King.

## Continuity

- The Demon-Sealing Formation currently blocks all mana from the exposed Gate by drawing on natural qi. Its permanent durability and whether equivalent formations can be installed at future Gates remain unresolved.
- Taekyung believes Dark Heaven deliberately planned the Gate incident and that similar incidents will continue. The Lord of Heaven’s identity and connection to the dangerous force Taekyung associates with his original world remain unknown.
- Jang Taebo is Master of Ironcraft Hall and is recruiting renowned artisans to process the Water God Dragon’s remains.
- The New Murim Alliance will be founded at Mount Song in about one month, primarily under the banner of the orthodox Central Plains Murim. Its leaders intend to draw in the fractured unorthodox factions before Dark Heaven can recruit them.
- Hongcheon, Hubei’s new Provincial Administration Commissioner, secretly serves Prince Shangshan. Jin Wikyung proposed the arrangement behind the Hubei dark-path purge.
- Jeok Cheongang’s infirmities began after he left Sichuan. His leaking innate qi caused worsening memory and time loss, but his Heart Demon and the memories binding him have now been expelled.
- Jeok Cheongang has entered a new realm and is expected to travel with Jin Wikyung’s party after his secluded meditation. The lasting abilities and physical effects of his breakthrough remain unresolved.
- Mungyeong remains the Slaughter Saint and former Divine Physician. He has agreed in principle to protect Taekyung, but the precise nature of his future Master-Disciple relationship with Taekyung is not settled.
- Around one hundred Level 5 Mutated Minnows, locally called Blood Fish, were captured near the Gate; the remaining population is unknown, and the fish kill one another.
- The Southern Heaven Demon Empress is traveling toward Yunnan and expects further deaths. Jin Mukyung remains secluded after losing to Cheongpung.
- Zhuge Gonghu’s historical gamble sent the thousand-man Black Wind Corps through Mount Jiuhua, where Jeok destroyed it and became known as the Fire King.

## Translation Decisions

- Retain **Water God Dragon**, **Gate**, **Origin Essence**, **inner core**, **innate qi**, **acquired qi**, **true-origin qi**, **Demon-Sealing Formation**, **New Murim Alliance**, **Ironcraft Hall**, **Master of Ironcraft Hall**, **Jin Dragon Squad**, **Mutated Minnow**, and **Blood Fish**.
- Render **살천문** as **Salcheonmun**, **심마** as **Heart Demon**, **면벽수련** as **secluded meditation**, **호법** as **stand guard**, **흑풍단** as **Black Wind Corps**, **왜국** as **Wa Kingdom**, **인자** as **ninja**, **은영술** as **concealment techniques**, **표창** as **throwing blades**, and **철구** as **iron balls**.
- Preserve **Returned to Youth**, **Fire King**, **Slaughter Saint**, **Old Master**, **Master-Disciple relationship**, **Fake Murim Martial Artist**, **Memory Fragment**, **Gate Conquest**, **Teleport**, **Magic**, **Poison Resistance**, and **Qi Sense**.
- Retain the established renderings **Energy-Dispersing Poison**, **Seven-Step Soul-Chasing Powder**, **Blindness Powder**, **Potent Paralysis Powder**, **Potent Soul-Bewitching Powder**, **Full-Body Paralysis**, **Poison Absorption**, and **Detoxification**.
- Preserve Taekyung’s profane irreverence, Jeok’s rough Master-Disciple banter, Mungyeong’s calm coercive authority, and the crude humor of the surrounding dialogue.

## Durable state

{
  "active_continuity": [
    "Jeok Cheongang’s infirmities of old age began immediately after he left Sichuan; his leaking innate qi causes progressive memory and time loss, with seven external days experienced as five days by Jeok in this episode.",
    "Mungyeong is the Slaughter Saint and former Divine Physician, a Returned to Youth Supreme Peak master whose assassin instincts remain formidable despite decades spent living as a medical apprentice.",
    "Jeok Cheongang’s Heart Demon and the dark memories binding him have been expelled, and he has entered a new realm after breaking free of those chains.",
    "Zhuge Feng’s Demon-Sealing Formation blocks all mana from the exposed Gate by drawing in natural qi, but whether it is permanent and repeatable remains unresolved.",
    "Jang Taebo is the Jin Family of Taiyuan’s Master of Ironcraft Hall and is summoning renowned artisans to process the Water God Dragon’s remains.",
    "War has begun, and the New Murim Alliance is scheduled to be founded at Mount Song in about one month, with Taekyung believing Dark Heaven deliberately planned the Gate incident.",
    "Jin Wikyung proposed the Hubei political arrangement through Hongcheon, the new Provincial Administration Commissioner and Prince Shangshan’s hidden loyal retainer; the purge of Hubei’s dark-path figures was intended to create an opportunity for rival unorthodox factions while warning them.",
    "Around one hundred Level 5 Mutated Minnows, locally called Blood Fish, were captured in the Gate’s entrance waterways; the remaining population is unknown, and the fish kill one another.",
    "The Southern Heaven Demon Empress is traveling toward Yunnan and expects to cause further deaths.",
    "Jin Mukyung remains secluded in the training hall after losing to Cheongpung, refusing to emerge until he achieves a great accomplishment.",
    "Jeok Cheongang is expected to travel with Jin Wikyung’s party to the New Murim Alliance after seven days and nights of seclusion, apparently persuaded by Taekyung.",
    "Zhuge Gonghu’s historical gamble directed the thousand-man Black Wind Corps through Mount Jiuhua, allowing Jeok Cheongang to annihilate it and gain the title of Fire King."
  ],
  "continuity_sources": [
    504,
    503
  ],
  "open_questions": [
    "Will the Demon-Sealing Formation remain effective permanently, and can equivalent formations be installed repeatedly if more Gates appear?",
    "What is the Lord of Heaven’s identity, and how is he connected to the dangerous force Taekyung associates with his original world?",
    "Where is the Southern Heaven Demon Empress ultimately headed, and what does she intend to do in Yunnan?",
    "Will the fractured unorthodox factions accept the New Murim Alliance’s invitation instead of joining Dark Heaven?",
    "What lasting abilities or changes will follow Jeok Cheongang’s breakthrough after his Heart Demon was expelled?"
  ],
  "safe_through": 504,
  "temporary_decisions": [
    "Render 산공독 as Energy-Dispersing Poison, 강력한 산공독 as Potent Energy-Dispersing Poison, 칠보추혼산 as Seven-Step Soul-Chasing Powder, 강력한 칠보추혼산 as Potent Seven-Step Soul-Chasing Powder, 심각한 복통 as Severe Stomachache, 고기 방패 as Meat Shield, 독 장아찌 as Poisoned Pickle, and 독의 as Poison Physician; retain secret martial arts, Master-Disciple relationship, Killing Ghost, and Fake Murim Martial Artist, and preserve 악 as Agh in the Quest interface; render 실명산 as Blindness Powder, 살천문 as Salcheonmun, and 스승의 날 as Teacher’s Day.",
    "Render 기억의 파편 as Memory Fragment, 게이트 공략 as Gate Conquest, 텔레포트 as Teleport, 마법 as Magic, 흑풍단 as Black Wind Corps, 혈어 as Blood Fish, 변이된 송사리 as Mutated Minnow, 왜국 as Wa Kingdom, 인자 as ninja, and 절강 as Zhejiang; render 강력한 마비산 as Potent Paralysis Powder, 강력한 미혼산 as Potent Soul-Bewitching Powder, 전신 마비 as Full-Body Paralysis, 독성 흡수 as Poison Absorption, and 해독 as Detoxification.",
    "Render 시산혈해 as sea of corpses and blood and retain Old Master for 노야 with the established rough, profane Taekyung-Jeok banter; render 해시 as hour of the Pig, 한 식경 as half an hour, 타구봉 as Dog-Beating Staff, 창룡 as Azure Dragon, and 무량수불 as Infinite Life Buddha; preserve geun as the traditional weight unit with a footnote.",
    "Render 선천지기 as innate qi, 진원진기 as true-origin qi, 천기 as heavenly patterns, and 후천지기 as acquired qi.",
    "Render 심마 as Heart Demon, 비급 as martial arts manual, 송문고검 as Pine-Pattern Ancient Sword, 반로환동 as Returned to Youth, 강강수월래 as Ganggangsullae, 생사부 as Book of Life and Death, 기막 as qi curtain, 무극태을검 as Martial Extremity Grand Unity Sword, 이룡 as Two Dragons, 원정 as Origin Essence, 내단 as inner core, 영험한 기운 as sacred energy, 대호 as great tiger, 취팔선권 as Drunken Eight Immortals Fist, 귀면 as Ghost Face, 요단강 as Jordan River, 진룡 as Jin Dragon, 마봉진 as Demon-Sealing Formation, 철기당 as Ironcraft Hall, 철기당주 as Master of Ironcraft Hall, 신룡 as Divine Dragon, 신(新) 무림맹 as New Murim Alliance, 면벽수련 as secluded meditation, 호법 as stand guard, 한나절 as half a day, 일다경 as the time it takes to drink a cup of tea, 촌각 as moments, 진맥 as take one’s pulse, 은영술 as concealment techniques, 표창 as throwing blades, and 철구 as iron balls."
  ],
  "version": 1
}

## Reading copies

## Chapter artifact 500

# Chapter 500

In the dead of night, before dawn had even begun to break, Jang Taebo had followed us along with a face that looked ready for the grave.

But the moment he saw the Water God Dragon’s remains, he changed completely.

“Ohhh… Ohhhhh…!”

Talk about a complete change of attitude.

Jang Taebo, who had been trembling like a kindergartener who needed to pee, threw himself between the mountains of bones and scales.

“Oh, the strength! The color!”

His eyes were unfocused with rapture, and his trembling voice betrayed his excitement. His hands ran over the scales and gently caressed the bones, unable to hide his joy.

“I’d be happy to be buried here and die! No, I want to die here!”

“Rescue Old Master! The remains are about to collapse!”

“Y-yes, sir!”

The Jin Dragon Squad martial artists had been staring blankly at the remains of a gigantic creature unlike anything they had ever seen. Now they rushed forward and dragged Jang Taebo out.

Only then did the old Master Artisan come to his senses. He looked at me with moist eyes.

“So everything you told me was true.”

“It sounds insane, but every word of it was true.”

“I thought I had handled meteorite iron that fell from the sky and worked Ten-Thousand-Year Cold Iron to my heart’s content…”

Jang Taebo wiped at the corners of his eyes with a deeply moved expression. After sniffing and composing himself, he suddenly grabbed my shoulder.

“Thank you. I can die without regrets now.”

I gazed at Jang Taebo warmly.

“Don’t say things like that. Live a long, healthy life instead. And have something nourishing slow-simmered for yourself, too.”

“You little…”

“You still have plenty of Stamina and life left to grind into the forge. Where are you trying to run off to—the afterlife?”

“You little…!”

The same words. A completely different feeling.

A high-quality slave this difficult to acquire had to be put to proper use. Every now and then, I would give him a little reward and crack the whip.

Of course, I wasn’t the one holding the whip.

“Good heavens. It’s astonishing even after seeing it again. There’s an incredible amount of material here.”

“Welcome, owner of the whip.”

“Hm? What did you say, my youngest?”

“Nothing, eldest brother.”

Jin Wikyung tilted his head, then laughed heartily and patted Jang Taebo on the back.

“How do you find it, Hall Master Jang? It’s a truly spectacular sight, isn’t it?”

“Hall Master… Jang?”

“Heh heh. Of course. You are now the Hall Master of our family’s Ironcraft Hall, so that makes you Hall Master Jang. Come, let us hear your expert opinion.”

Jang Taebo slowly began to understand the reality he had momentarily forgotten. He answered with a dark expression.

“Whew. There’s no need to say anything more. Even at the Ironcraft Guild, where the finest artisans and materials under Heaven were gathered, I never saw anything like this.”

“So, can you do it?”

“I can’t guarantee anything until I try it myself. However…”

Jang Taebo carefully examined the remains piled up like a mountain before continuing.

“The bones are far stronger than meteorite iron, though not quite as strong as Ten-Thousand-Year Cold Iron. They should be workable.”

“What about the hide and scales?”

“As for armor, I made enough of it in my younger days to grow sick of the work. The materials weren’t from an imugi, of course…but I’ll give it a try.”

“Ohh.”

“With this much material, there will be enough to arm every martial artist in the Jin Family of Taiyuan—or rather, in our family—and still have some left over. I should be able to show results soon, so I trust you’ll forgive the first few failures.”

“Of course.”

As a craftsman, Jang Taebo stood at a position equal to or higher than the Three Saints among martial artists.

Jin Wikyung’s face brightened at the measured but well-founded confidence of the high-quality slave.

“I’ve heard that only the finest Master Artisan of the age can become the Guild Leader of the Ironcraft Guild. I’ll be counting on you, Hall Master Jang, so tell me if you need anything.”

“Then please assign some trustworthy artisans to me, Lesser Family Head.”

“Artisans?”

“I know our family has artisans of its own. If I teach them, they may not become the beams supporting the family, but they should at least grow into fairly sturdy pillars. However…”

“It will take no small amount of time. Am I right?”

“That is correct. I have eyes and ears, so I’ve heard plenty about what has been happening throughout the world lately. The artisans I still exchange occasional letters with have told me that orders for weapons and armor have increased sharply.”

The war had already begun.

From the small and mid-sized sects scattered throughout Murim to the Nine Sects and One Gang, everyone wanted weapons and armor to prepare for the war that had drawn so close. The fires of the forges would not go out until the war ended.

In the current state of Murim, it was not only the flames of war that had begun to blaze fiercely.

“Time is short, Lesser Family Head.”

Jin Wikyung silently gazed up at the sky before suddenly speaking.

“Hall Master Jang, how many years have you been doing this work?”

“I began when I was shorter than your sword, Lesser Family Head. I devoted my entire life to it.”

“You spent all those years immersed in one field, so you must have made many friends while working alongside them.”

“Of course. Every one of them is a renowned artisan in their respective field.”

“Send messenger pigeons to every one of them who has just come to mind. I don’t care if it costs a fortune.”

“Everyone has something they value more dearly than wealth. For a craftsman like this old man, the body of an imugi is worth more than a fortune.”

Jang Taebo took one step back and performed a respectful martial salute toward Jin Wikyung.

“Jang Taebo, Master of Ironcraft Hall of the great Jin Family of Taiyuan, obeys the Lesser Family Head’s command.”

Before anyone realized it, the darkness had receded and the sun of a new day had risen.

The light spreading from the east resembled the flames of a forge, while the footsteps of the Jin Dragon Squad martial artists swiftly carrying the Water God Dragon’s remains sounded like the ringing of hammers.

* * *

While fifty Jin Dragon Squad martial artists transported the Water God Dragon’s remains under the meticulous direction of Wipeng and Jang Taebo, Jin Wikyung and I returned to where we were supposed to be and encountered Zhuge Feng, who was brimming with excitement.

“I did it! I’m telling you, I did it!”

He jumped around like a child. There was no sign of the dignity one would expect from the Family Head of a great clan.

However, after checking the result for myself, I had no choice but to nod.

*He completely blocked the mana.*

Unlike before, not even the slightest trace of mana flowed from the enormous rift—or rather, the Gate.

The dogs, pigs, fish, and other creatures that had been left behind as though for an experiment showed some interest in it a few times, then returned to whatever they had been doing.

“You actually managed to do it, Sir Zhuge.”

At Jin Wikyung’s words, a brilliant smile bloomed across Zhuge Feng’s exhausted face.

“I pulled it off because I’m me. Even my ancestor Zhuge Wuhou couldn’t have accomplished something like this. Come to think of it, he had some knowledge of mechanisms and formations, too, but in the end, Wei fucking trounced him…”

“F-Family Head!”

“Ah, why? Isn’t it true? If he really was a chancellor who cared about the people and a true strategist, he should have thrown a resignation letter in that incompetent emperor’s face instead of a campaign memorial and seized the throne…”

“Family Head, you really are insane!”

“Uncle, did I say anything wrong?”

The Zhuge Clan was a real mess.

The current Family Head, having smeared shit all over his ancestor’s reputation, shook off his relatives and continued speaking proudly.

“Well? What do you think after seeing the Demon-Sealing Formation for yourself?”

“The Demon-Sealing Formation?”

Zhuge Feng nodded with satisfaction.

“I named it myself. A formation that seals the power of demons. Doesn’t it suit the purpose?”

The Demon-Sealing Formation. Considering the source of that power, there couldn’t have been a more fitting name.

Of course, what the formation was called didn’t matter as long as it worked.

As I carefully examined the Demon-Sealing Formation, Jin Wikyung whispered to me.

“What do you think?”

“About what?”

“……”

“I’m just looking at it. How would I know?”

Murim formations were essentially the same as modern magic circles.

Even though I had often encountered Magic while living as a Hunter, I was hardly an expert. There was no way I could look at a formation once and judge it.

At most, I had enough aptitude to sense the flow of qi moving through it.

*It seems to be drawing in the qi of the natural world to block the mana…but its operating principle is similar to a magic circle.*

However, compared to modern magic circles, the formations I had seen and heard about in Murim were far more limited in variety and power.

The Murim’s reverence for martial arts itself had probably played a major role in that.

*They did this faster and better than I expected.*

The qi of the natural world flowing through the formation was sufficient to completely block the mana leaking from the Gate. For now, this was the best possible solution.

After examining the Demon-Sealing Formation thoroughly, I turned toward Zhuge Feng.

“How long will this formation remain effective?”

“Do you think the waters of the Yangtze have ever dried up?”

“Ah.”

“The Demon-Sealing Formation will continue drawing in the qi around it and remain active. At least, that’s what my theory says.”

“And what if Sir Zhuge’s theory is wrong?”

“My theory? You might as well say Zhuge Wuhou was a halfwit.”

Clang!

“You bastard, Zhuge Feng!”

“Great-Uncle, no! Put down your sword!”

“Someone shut the Family Head’s mouth!”

The atmosphere had suddenly turned murderous.

Before a bloody storm of familial slaughter could break out, I hurriedly continued speaking to Zhuge Feng as he used a grappling technique against the relatives rushing at him.

“Then can you keep installing this in the future?”

“Huh?”

“What?”

“What do you mean?”

For the sake of the Zhuge Clan members who had frozen in place, I repeated myself with clear enunciation.

“Continuously. I mean dozens or even hundreds of times.”

“……!”

“……!”

The air around us instantly turned cold.

Zhuge Feng, who had been grabbed by the collar by an old man, straightened his clothes. Then his eyes and voice sank as they turned toward me.

“I suddenly find myself curious about the Divine Dragon’s intentions.”

I gave a bitter smack of my lips.

“It’s obvious, isn’t it? You already know, Sir Zhuge.”

“I do. I know that something which has happened once can happen ten times or a hundred times.”

“Then you must think the same way I do.”

“I wasn’t as certain as you. I was merely taking every situation that might arise in the future into account.”

An unreadable light flashed in Zhuge Feng’s eyes.

“Why are you so certain that things like this will continue happening? What grounds do you have for speaking with such confidence?”

I had plenty of grounds. I simply couldn’t tell him about them.

The Zhuge Clan might have been abuzz with joy on the day Zhuge Feng was born, but on the day I was born, all of humanity was abuzz.

The Demon King Asmodeus had fallen, and the long Great Cataclysm had finally come to an end.

It was a difference that could not be explained in words.

After that, as many years passed as I had lived, but Gates still remained in the modern world and continued appearing again and again.

No matter how sturdy a dam was, once it began to crack, the damage would soon become impossible to control.

The current Murim was exactly the same.

*I can’t exactly tell them all of this.*

In the end, the answer I could give had been decided from the beginning.

“I saw and felt it directly in the memories the Water God Dragon passed on to me. This was something Dark Heaven intended from the very beginning, planned, and carried out. And it will continue.”

“You’re more skilled at lying than I expected.”

“You’re more suspicious than I expected.”

“I can’t believe you. No—the honest truth is that I don’t want to believe you.”

“Zhuge Wuhou must have felt the same way. And yet he still served that stupid emperor until the very end. Even if it fucking sucks, you have to accept it.”

“Even if it fucking sucks, you have to accept it…”

Zhuge Feng let out a quiet laugh and turned toward one person.

“What do you think, Lesser Family Head?”

Jin Wikyung answered in a calm voice.

“I think the same as my younger brother.”

“I wonder what the others think.”

“Then why don’t we ask them and hear for ourselves?”

“What does that mean…?”

Zhuge Feng stared at Jin Wikyung, then suddenly muttered,

“Henan.”

“Yes.”

Jin Wikyung looked toward somewhere in the distance and continued.

“The New Murim Alliance.”
## Chapter artifact 501

# Chapter 501

“When is it?”

On the way back after parting with Zhuge Feng, I suddenly tossed out the question. Jin Wikyung answered in a quiet voice.

“In a month. Mount Song, Henan Province.”

“Mount Song…”

The very place where Shaolin Temple—the Mount Tai and Northern Dipper of the Murim—was located.

Only three months ago, the Star-Array Grand Banquet, the greatest gathering of the Murim under Heaven, had begun there. Dark Heaven had unleashed a storm of blood, and now the New Murim Alliance would be born in that same place.

Considering the location of Mount Song and Shaolin Temple’s symbolism, it was the perfect starting line for the Murim Alliance’s resurrection after more than fifty years.

But the fact that only a month remained meant…

“It had already been decided when you came to Sichuan, hadn’t it?”

Contrary to my expectations, Jin Wikyung slowly shook his head.

“It hadn’t?”

“Why do you think Wipeng happened to be in Henan at exactly the right time?”

“Then the reason Great Hero Wipeng came was…”

“The Jin Dragon Squad is our family’s finest elite force. As the Lesser Family Head, I would never allow half of its members to be summoned merely to serve as porters. Even if what they were transporting had been the Son of Heaven’s jade seal.”

“So it was moved forward.”

“Dark Heaven’s movements were harsher and faster than we had expected. The Sichuan Blood Tragedy was decisive.”

To catch an enemy who was ahead, you had to run.

The storm of blood that had swept through Shaolin Temple had spread to Sichuan and now reached Hubei. The leaders of Henan had to make a choice.

“Binding the Murim under Heaven beneath one fence is never easy. But it seems those people have finally made up their minds.”

Muttering quietly, Jin Wikyung pulled a sealed dispatch from inside his robes and held it out to me.

“What’s this?”

“A letter Wipeng brought from Henan.”

“If it came from Henan, is it from the Murim Alliance?”

“You had already guessed.”

“I figured it out when I saw you give one to Sir Zhuge earlier.”

The letter was clearly different from an ordinary one, even in appearance.

But what made it truly special were the three characters written across its surface in a bold, soaring hand:

**Murim Alliance.**

“Read it yourself, youngest.”

“I’m already reading it, so stop talking to me. I can’t concentrate.”

“…Oh. Right.”

Ignoring Jin Wikyung’s downcast expression, I unfolded the letter and quickly skimmed through it.

The letter began with the words, *To the Murim under Heaven,* and its contents were short and powerful. That made it easy to boil down to three lines.



1. Hey, let me tell you about Dark Heaven. These guys are seriously fucking crazy, so listen up.

2. You know the Great Faction War PTSD? Let’s stop this by any means necessary.

3. Any dumbasses who don’t know where Mount Song is? Gather by the specified date. Anyone who doesn’t show is Dark Heaven.

“…”

When I put it into three lines, it sounded pretty pathetic.

Of course, the letter had not actually been written that way.

The calligraphy, written boldly by some unknown master, flowed like clouds. Every sentence and the emotions contained within were solemn and deeply moving.

Personally, I almost wanted to show it to that bastard, the Lord of Heaven.

*If he saw this, even the Lord of Heaven might join the Murim Alliance.*

Everyone could have enjoyed a happy ending if the Lord of Heaven joined the Murim Alliance. It was simply unfortunate that the possibility of that happening was less than the amount of earwax in Hyuk Mujin’s ear.

“In any case, the Murim Alliance will be born soon.”

“In a month, the Murim under Heaven will gather beneath the Murim Alliance’s banner.”

After a moment’s thought, Jin Wikyung added one more thing.

“Not the Murim under Heaven. We should say the orthodox Murim of the Central Plains.”

I already understood what Jin Wikyung meant.

*He’s right. Calling the orthodox faction the Murim under Heaven would be a bit much.*

The dominant force in the Murim under Heaven was unquestionably the orthodox faction, led by the Nine Sects and One Gang and the Five Great Families.

But the orthodox faction had not been the only side to survive and emerge victorious from the Great Faction War.

“The unorthodox faction.”

At my muttered words, Jin Wikyung nodded.

“That’s right. We cannot exclude them.”

The fishbowl called the world did not contain only one color of fish.

Compared to the orthodox faction, the unorthodox faction was weak, but it had built domains of its own. The dark-path figures who ruled the streets at night were part of it as well.

*At first, I wondered why they had left those people alive while shouting about eliminating every demonic and heterodox element.*

Everything happened for a reason.

The unorthodox forces still around today owed their survival to siding with the orthodox faction during the Great Faction War.

The problem was that their choice had not been made out of simple goodwill.

“Do you know why the unorthodox forces currently active in the Central Plains sided with the orthodox Murim?”

“You haven’t forgotten who I’ve spent the past year with, have you?”

“Great Hero Jeok told you.”

“I picked up quite a lot here and there.”

There was an old saying: green goes with green, and crayfish take the crab’s side.

When the Demonic Cult crossed Qinghai and surged toward the Central Plains during the Great Faction War, the unorthodox faction quickly joined them while shouting, “Long live the Cult Leader!”

The Demonic Cult’s momentum had certainly been overwhelming, but the unorthodox faction had also wanted people like themselves—the Demonic Cult—to become the masters of the Murim under Heaven.

However, the unorthodox martial artists living in the Central Plains, the heart of the world, had faced a different situation.



*If they don’t side with the orthodox faction, they’ll be hunted down before they can even leave the Central Plains. Those bastards wouldn’t dare refuse to join this side.*



The words Jeok Cheongang had once spoken with a snort had been an exact description of reality for the unorthodox martial artists of the Central Plains at the time.

“I heard they were basically eating dumplings through their tears.”

“I did not live through that era either, but according to what I have confirmed, that is true.”

“Confirmed?”

“After you left for Sichuan, I remained in Henan and searched through old records. I found countless accounts. The records concerning the unorthodox faction were among them.”

When peace arrived, the Murim Alliance was disbanded, but records preserving the memories of those who had experienced the Great Faction War and the circumstances of that time remained.

It made sense when I thought about it. In the long history of the Murim, fifty years was only half a century.

“What did the records say?”

“What do you think they said?”

“I can make a rough guess. I’ve heard some stories.”

“I do not know exactly what Great Hero Jeok told you, but most of it was probably true.”

“…If that’s true, it’s pretty damn ridiculous.”

From the beginning of the Great Faction War until it had entered its middle and latter stages, the unorthodox martial artists who had joined the orthodox faction betrayed them again and again.

Considering what Jeok Cheongang had said about the Murim Alliance’s leadership even discussing root-and-branch eradication to remove every unorthodox member from within the orthodox faction, the situation must have been serious.

“But I heard they fought hard later on.”

“Because the outcome was no longer certain, unlike at the beginning. There was also the ironclad surveillance of the Hidden Shadow Pavilion, led by Sir Song, the Thousand-Faced Fox. According to the records, once the unorthodox martial artists sensed that the atmosphere among the leadership had become ominous, they cut off their own tails.”

The orthodox faction was not automatically righteous, and the unorthodox faction was not composed solely of the worst kind of villains.

But unlike the orthodox faction, the unorthodox faction possessed the decisiveness and cruelty to cut off its own tail without hesitation.

The instant someone was suspected of being a spy for the Demonic Cult, they slit his throat first and asked questions later.

“In the end, the body whose tail had been cut off survived and became one of the victors by cooperating with the orthodox faction.”

The surviving unorthodox forces were able to maintain their lineage beneath the shade of the great tree known as the orthodox faction. Naturally, however, they could no longer display the same influence as before.

Their reputation had already been filthy, and they had sided with the Demonic Cult countless times.

They were fortunate that the Murim Alliance’s leadership had recognized a certain amount of their contributions and rights. Otherwise, the general consensus was that they would have been dragged out and dismembered by the hardline heroes who screamed for the elimination of every demonic and heterodox element.

The hatred directed toward the unorthodox faction after the war had continued like some ancient tradition.

None of that had been a particularly serious problem.

But from this point onward, things were different.

“We have to take them with us and fight alongside them.”

“Yes. If not with the Murim Alliance, they will side with Dark Heaven.”

“It leaves a bad taste in my mouth to bring them into the fold.”

“They are not people I would want watching my back on a battlefield. There is precedent, and decades of resentment over the postwar allocation of honors and rewards must have accumulated.”

“Then what if we tell them to remain neutral?”

“Let us say the Murim Alliance appears certain to lose. If you were an unorthodox martial artist, youngest, what would you do?”

“…Hmm.”

When he put it that bluntly, I had nothing to say. I smacked my lips, then answered.

“I hate to say it, but I’d side with Dark Heaven.”

“Why?”

“If the Murim Alliance wins, they break even. But as you said, the scales are already tilted, and Dark Heaven is on the verge of becoming the master of the Central Plains Murim.”

“Correct.”

“What kind of people are Dark Heaven? Do you think they’d leave the unorthodox faction alone? Rather than praising them for remaining neutral, they’d be furious that they hadn’t helped when it mattered and kill every last one of them.”

“You are exactly right. That is why the unorthodox faction is a chicken rib.”

A chicken rib. It was a remarkably fitting expression.

It offered little benefit, but it was too wasteful to throw away. Fighting alongside them felt unpleasant, but if we discarded them, Dark Heaven would pick them up and throw them back at us.

No matter how soft a chicken bone was, it was still a bone. Getting hit by one would hurt quite a bit.

If that was the case…

“Henan has already sent them a letter, hasn’t it?”

Jin Wikyung nodded slightly.

“Without a doubt. If we must choose between the two, we need to draw the unorthodox Murim to our side.”

The unorthodox faction had a surprising amount of meat on it for a chicken rib.

Even the dark-path knife-men who wandered the back alleys after sunset belonged to the unorthodox faction. Weren’t we at a point where we would be grateful for a single Third Rate knife-man?

More importantly, it was better to keep them close and hold their leash than let them side with Dark Heaven. That would be far too great a loss…

*Wait a second. The dark path?*

A memory suddenly surfaced, and I frowned.

“What is it?”

“No, I just remembered something I heard recently. Regarding the Water God Dragon incident, didn’t we accuse the dark-path figures of Hubei Province of being the culprits and wipe them all out?”

“We did.”

“…Then the unorthodox faction might be upset. In the end, we accepted the government’s proposal and wiped out their own people.”

It did not look good. This incident might even be enough for the unorthodox faction to reject the Murim Alliance’s offer of membership.

Jin Wikyung, however, looked perfectly calm.

“Two things are wrong with that.”

“What?”

“First. Since the end of the war, the unorthodox Murim has been fractured into countless pieces. They should be considered rivals, not family. We took this opportunity to uproot the dark-path figures in Hubei, whose numbers had become unusually large. Another unorthodox faction will fill the vacant space. It is a new opportunity.”

“…!”

“We gave them enough food, so they will be satisfied. They will also hear what happened in Hubei and realize that it was a warning.”

We had thrown them food, then fastened a leash named fear around their necks.

That was how the Murim Alliance tamed the hunting dog known as the unorthodox Murim.

“And second. The government did not make the proposal and receive our acceptance.”

Jin Wikyung continued in a dry voice.

“We did. No—I made the proposal first.”

“Oh.”

“The government merely accepted it. That distinction is very important.”

“…Would the government really agree that easily?”

“The Provincial Administration Commissioner of Hubei is an important post capable of controlling an entire province. But people know only that the new commissioner previously served as an Assistant Provincial Administrator in Shanxi Province. They do not know that he is Prince Shangshan’s hidden loyal retainer.”

A memory of when we had first arrived in Hubei suddenly flashed through my mind.

The hostile gazes of the people.

And Jin Wikyung questioning the official who had surrounded the ferry landing with government soldiers.



*“By the way, do you happen to know a man surnamed Yi whose given name is Hongcheon?”*

*“H-he was recently appointed as the Provincial Administration Commissioner. May I ask what your relationship with the commissioner is…?”*

*“I have met him a few times and shared a drink or two. I helped him when he needed it.”*



Jin Wikyung’s eyes, fixed directly on me, were gentle. But a cold blade lurked within them.

They were the eyes of a strategist and a politician. Before I could fully register them, they melted away and vanished.

“Do not worry. Everything will work out.”

Tap, tap.

I could feel the strength in the hand patting my shoulder. I gazed silently at Jin Wikyung, then suddenly spoke.

“Family Head… No, what kind of person was Father?”

The faint smile around Jin Wikyung’s mouth vanished as though it had been wiped away.

“No, the mood was so nice. Why bring up that bastard?”

“As you know, I injured my head back then. I don’t remember him very well.”

“You don’t need to remember him! Just erase him from your mind! I’m your father!”

“…”

I already knew he had accumulated quite a bit of resentment, but apparently there was more than one or two things piled up.

Jin Wikyung even trembled his fist, apparently remembering the paperwork hell of those days.

“But why did you ask?”

“Just because. I was thinking how fortunate it was that, after Father disappeared, hyung took charge of the family.”

“…Youngest. Please do not cross the line.”

I shrugged and turned away.

Jin Wikyung asked where I thought I was going when hyung was talking to me, and whether my affection for him had cooled. Without turning around, I answered,

“You said it’s in a month. I’m going to prepare to leave.”

The time had come to leave Hubei behind.

Together with those who were by my side—and whom I wanted by my side in the future.

“I think I’ve given it enough time by now… don’t you?”

The mutter that slipped between my lips vanished without a trace beneath the noise around us.

I scratched my chin as I looked up at the cliff rising into the distant sky.
## Chapter artifact 502

# Chapter 502

“You’re here.”

At the sudden voice from behind him, the brow of the old man sitting cross-legged with his eyes closed twitched.

“I don’t recall inviting anyone.”

“Not my problem. Still, it’s narrower than I expected. Absurdly so.”

“It has to be narrow. I didn’t set aside any room for uninvited guests.”

“Was it around seven days and nights ago? I’m sure I said something similar to someone…”

For some reason, the old man’s small back shuddered the moment he heard those words.

But before the uninvited guest could wonder why, a sharp, cutting voice flew at him.

“Leave. You’re disturbing my meditation.”

“Continue your meditation. I’ll personally stand guard for you.”

The old man—Jeok Cheongang, the Fire King—opened his eyes.

The darkness disappeared, replaced by the damp cave walls mottled with moss.

Then a harsh voice escaped between his tightly pressed lips.

“You want this old man to entrust his protection to none other than the Slaughter Saint? What a ridiculous joke.”

“I thought you could trust me with an old man’s life, if not your precious Disciple’s. Was I mistaken?”

“……!”

At that single remark, Jeok Cheongang’s eyelids trembled. Then, the next moment—

*Shuuk.*

The small figure sitting cross-legged rose into the air, slowly turned around, and landed.

Jeok Cheongang silently stared at the man blocking the narrow cave entrance before suddenly opening his mouth.

“How did you know this old man was here?”

Mungyeong answered in a dry voice.

“When I came up, a great tiger approached and rubbed its head against me. It clearly wasn’t something it had only done once or twice.”

“I left no tracks.”

“That was my profession.”

“So no matter how much you pretend to be a medical apprentice, you’re still an assassin?”

“There are things one cannot forget, no matter how hard one tries. That is all. There are countless eyes watching, and nothing but water all around us. The possible destinations were obvious.”

A sword forged by an exceptional blacksmith did not lose its edge even after the passage of time.

The sharpness of the famous blade called the Slaughter Saint remained undiminished even after more than forty years.

No—his instincts as an assassin might have dulled, but his realm as a martial artist had risen even higher.

“……Perhaps I should have found somewhere more hidden.”

“If you had, it would have taken me a little longer.”

An assassin was a master of assassination and pursuit.

Reading the confidence in Mungyeong’s calm expression, Jeok Cheongang muttered,

“Damn it. What an obnoxious bastard of an assassin.”

“I can hear you.”

“I said it so you would hear.”

“Cursing me out of nowhere. You’re one foul-tempered host.”

“Are you any better, barging in on someone’s secluded meditation without warning?”

“The Fire King, engaged in secluded meditation.”

Mungyeong’s toneless voice echoed through the cave.

His gaze slowly swept across the surroundings. The place was so narrow and damp that calling it a cave seemed generous. Apart from the old man sitting cross-legged, there was nothing there.

And there were things that stood out all the more because they were the only things in sight.

*Jeok Cheongang. This man…*

His cracked lips. The knobby bones protruding beneath his skin.

Mungyeong’s gaze sank as he took in every detail of Jeok Cheongang’s condition.

Judging from his emaciated appearance, it was obvious that he had not put even a drop of water to his lips during the past seven days and nights, let alone eaten anything.

Even for a Supreme Peak master, it was clearly taking a toll on his body.

“You’re doing something foolish.”

Jeok Cheongang was not incapable of understanding what Mungyeong meant. A sharp light flashed from his sunken eyes.

“I’ll return your own words to you. It’s not your problem.”

“What about the fasting pills?”

“I don’t eat them. They taste like shit.”

“……Did you take after him in that, too?”

“What?”

“Nothing. Forget it.”

He had said something pointless. Almost as pointless as Jeok Cheongang’s clumsy excuse that he had refused to eat the fasting pills simply because they tasted bad.

Shaking his head, Mungyeong continued.

“As a medical apprentice, I advise you that this is not a good choice.”

“As this old man, I advise you to mind your own business.”

“You’re more stubborn than I expected.”

“You’re more meddlesome than I expected. Since when have you cared so much about other people’s affairs?”

“That…”

Mungyeong suddenly fell silent. He wanted to argue, but no words came to him.

That was practically an admission that Jeok Cheongang was right.

*Perhaps he isn’t entirely wrong.*

He had not been like this when he first left Sichuan. Yet at some point, he had clearly begun to change, little by little.

When he lived as an innocent young medical apprentice to deceive the eyes watching him, he smiled and talked often. But when he was alone with Jeok Cheongang or Jin Taekyung, there was no need to put on an act that did not suit him.

Then why?

He felt as though he had been talking more than usual today.

No—perhaps it was not limited to today.

*Why?*

Mungyeong remembered himself seven days and nights ago, when he had accepted Jeok Cheongang’s absurd proposal.

He also remembered Jeok Cheongang’s face as the old man continued speaking with an indescribably bitter expression.

That was when Mungyeong’s tightly closed lips finally opened.

“Why don’t you ask?”

“Ask what?”

“About Jin Taekyung.”

“……!”

This time, Jeok Cheongang was rendered speechless.

That was the name he had desperately tried to avoid.

The name he had hoped Mungyeong would tactfully leave unmentioned was enough to send ripples through the emotions he had forcibly suppressed.

“That boy… Is he doing well?”

“He’s keeping up, more or less. Not bad.”

Jeok Cheongang could not hold back a hollow laugh.

“Why are you laughing?”

“Because I know that’s nonsense. ‘More or less’? That’s the funniest thing this old man has heard lately.”

“…….”

“Don’t worry about this old man. Tell me what you really think.”

Mungyeong stared at Jeok Cheongang before opening his mouth.

“His progress is astonishingly fast. Enough to surprise even me.”

“I believe I told you to tell me what you really think.”

“This is what I really think.”

“Only half of what you really think. You left out the part about wanting him.”

“…….”

“Yes. It has always been like that.”

A faint smile touched Jeok Cheongang’s lips.

From the day he had first met Jin Taekyung until now, every day had been one surprise after another.

With his Heaven-given physique and extraordinary martial talent, he was someone any Supreme Peak master who had established their own martial arts would covet as a Disciple.

That applied to Jeok Cheongang himself.

“When I first came to know that boy Taekyung, I suddenly thought of something. If the Fire Gate Clan’s martial arts were passed on to him, perhaps he could see the very limits of martial arts.”

The Fire Gate Clan needed a talent to continue the lineage passed down for hundreds of years, and Jin Taekyung was the only person who fit the requirement better than anyone else.

That was certainly how it had begun.

“At first, I was simply amazed. Then I felt a pang of regret. I didn’t have much time left.”

He had defeated a thousand Demonic Cult martial artists alone and forced countless fiends to their knees.

With the overwhelming power of a single body, he had overturned the tide of battle and led the Great Faction War to victory from the front.

But the true enemy of the Supreme Peak master revered throughout the Murim under Heaven as the Fire King lay elsewhere.

“It happened a long time ago. The Heart Demon came to me.”

The wound left by his first Disciple had been deep, and it soon began to eat away at the body and mind of the Master left behind alone.

Little by little. Slowly.

But without stopping.

“It was strange. Everything else kept moving forward, while this old man alone was walking backward.”

Time passed as quickly as an arrow loosed from a bow. By the time its tip struck the target, more than thirty years had already passed.

Jeok Cheongang had let time flow away into the river without gaining even the slightest enlightenment. Then, one day, he faced a reality too difficult to believe.

“It was a bright blue day. I was enjoying the cool breeze when I suddenly came to my senses surrounded by people. Half a day had passed without this old man even knowing where the time had gone. Heh.”

He had laughed that way on the day the infirmities of old age first came upon him.

Not because he was happy, and not because he was empty inside.

He had simply laughed because he did not know what else to do.

Jeok Cheongang realized what he had to do only after that first half-day had become two full days.

“I left Mount Jiuhua to kill one person.”

And he returned with one person.

“He was my first Disciple. I had to deal with him myself before it was too late.”

But after meeting Jin Taekyung, Jeok Cheongang realized he had been too late in more ways than one.

“Slaughter Saint. May I ask you for one more favor?”

Jeok Cheongang’s gaze and tone toward Mungyeong had changed. They were gentler than ever before.

“If I am not here, become that boy’s dependable shelter. Become his new Master.”

A deep furrow formed on Mungyeong’s smooth, unlined forehead. He narrowed his eyes and stared at Jeok Cheongang.

“Was what you just said sincere?”

“More than anything I have ever said.”

“Why?”

“It’s exactly as I said. I don’t have much time left.”

“What is this…”

Become a new Master out of nowhere? He did not have much time left?

Mungyeong knew what condition Jeok Cheongang was in, but he still could not easily understand.

Jeok Cheongang’s innate qi—the source of all things—had been disrupted, so he would gradually lose his strength. But that should not happen until years had passed.

This was too soon.

“I ask this of you.”

“……!”

Now Jeok Cheongang even lowered his head.

Mungyeong was faced with a sight no one else in the Murim had ever witnessed: the Fire King Jeok Cheongang lowering his head before another person.

He was so bewildered that he could hardly believe what he was seeing.

“What is the reason? Only seven days and nights ago, you were clearly…”

Mungyeong’s voice cut off abruptly. He swallowed the rest of his words and silently stared at the ripples stirring in Jeok Cheongang’s eyes.

Then, amid the suffocating silence that descended in an instant, a thought flashed through Mungyeong’s mind.

*So that was it. That was what happened.*

If his guess was correct, every question had an answer.

Why Jeok Cheongang was worrying so excessively.

Why he had hidden himself from everyone else, including Jin Taekyung.

Why he was reacting so strangely during their conversation.

Mungyeong spoke as though he were sighing.

“It wasn’t seven days and nights ago, was it?”

“No. It was definitely seven days and nights ago.”

Jeok Cheongang smiled bitterly before continuing.

“But those seven days and nights were only five days to this old man.”

Time flowed equally for everyone, but that did not mean everyone experienced it equally.

The first uninvited guest to arrive, one step ahead of Mungyeong—the infirmities of old age—had stolen two days from Jeok Cheongang and fled.

“Since when did it begin?”

“Sichuan.”

“Sichuan? But when I took your pulse, you were clearly…”

“The symptoms appeared immediately after I left Sichuan. After that, I did my best to avoid you.”

Why had he hidden it? Why?

The question Mungyeong was about to ask circled only at the tip of his tongue before disappearing. He already knew the answer.

How pitiful a person became when he realized, at last, that he had grown old.

How much fear he felt when he discovered that his mind had begun to come and go because of the infirmities of old age.

At Mungyeong’s silent, closed-mouth expression, Jeok Cheongang gave a rueful smile.

“Even if I had come to tell you, nothing would have changed. This old man knows his own body well. Even if you are the Divine Physician whose medical skill reaches Heaven, you cannot stop innate qi once it has begun to leak away.”

“…….”

“At first, my memory grew hazy. Then one day, moments had disappeared from this old man’s day. I recognized it because I had already experienced it once before.”

Those moments became the time it took to drink a cup of tea, and that became a full quarter hour.

Now, it had become two days.

Jeok Cheongang grew desperate and did everything he could to find a solution, but it was useless.

“The acquired qi gained through elixirs cannot restore a balance that has already been broken. That left only one choice.”

“……Enlightenment.”

“Yes. Enlightenment.”

“That is why you suddenly began this secluded meditation.”

“I wanted to live as the Fire King Jeok Cheongang. Not as an old man with infirmities who cannot even remember his own name, but as the current Sect Leader of the Fire Gate Clan and someone’s Master.”

His desolate voice echoed through the cave.

The drops of water that gathered on the damp ceiling before falling resembled the tears of an old man.
## Chapter artifact 503

# Chapter 503

A curse bestowed by time.

Infirmities of old age.

Mungyeong quietly rolled the words around on the tip of his tongue.

No sound escaped him, but they were dry and bitter. Jeok Cheongang’s voice that followed was much the same.

“I’m thinking of leaving. I intend to calm my body and mind at Mount Jiuhua.”

“……!”

“You must know the reason, if anyone does. Please, don’t try to stop me.”

Just as Jeok Cheongang said, Mungyeong knew exactly why he wanted to leave.

*He’s afraid of becoming a burden.*

The infirmities of old age would continue to come upon him from time to time.

And if his mind grew hazy at a crucial moment, everyone with Jeok Cheongang would face a grave crisis.

After all, what his enemies feared was the Fire King Jeok Cheongang—not an old man who could not even remember where he lived or what his name was.

*More precisely, he’s worried that his Disciple will be put in danger.*

Everyone had something precious they could not afford to lose.

To a beggar begging in the marketplace, a half-crushed dumpling was his life. To an emperor who commanded all the civil and military officials, the jade seal symbolizing his authority and power was more precious than a thousand or ten thousand subjects.

The young man named Jin Taekyung was such a thing to Jeok Cheongang.

Someone he could trade his own life for. Someone precious he could not lose, no matter what happened.

“You really do cherish your Disciple.”

“My Disciple, you say. My Disciple.”

“If you’re about to spout the same nonsense as last time, forget it.”

At Mungyeong’s stiff voice, Jeok Cheongang smiled bitterly.

“No, you’re right. He is this old man’s one and only Disciple.”

“So you think you’re becoming a burden to him? Is that what you fear enough to leave of your own accord?”

“It is the only choice left. It’s for that boy’s sake.”

“There is another choice. Such as the imugi’s inner core you obtained this time.”

“You know as well as I do that the acquired qi obtained from elixirs cannot cure this. And…”

Jeok Cheongang looked down at his wrinkled hands and muttered,

“This old man has already grown too old. Even if that imugi’s inner core possessed such an effect, I cannot use it on an old man like me while relying on a single slim possibility.”

“……!”

“Even if you patch the bottom of an old boat, water will leak from somewhere in its ancient hull. But that boy—my Disciple—is different.”

Light seeped into the eyes that had sunk so deeply. The name of that light was joy and hope.

Mungyeong could feel the entirety of Jeok Cheongang’s feelings for his Disciple in those two eyes.

“This is a choice I cannot avoid. So please accept this old man’s request. Let me leave with peace of mind.”

“……A choice you cannot avoid. Is that what you’re saying?”

“Could I entrust that boy to you once more?”

Mungyeong, who had been staring at Jeok Cheongang, suddenly opened his mouth.

“If you take a boat east from Zhejiang, you’ll find a small island country.”

“An island country?”

“You must have heard of it. At least the name it is called by—the Wa Kingdom.[^1]”

“……?”

“You haven’t?”

Jeok Cheongang blinked at the sudden question.

“Of course I’ve heard of it. It’s not as if Japanese pirates only started coming to raid us yesterday.”

“Have you ever seen one in person?”

“No, but I hear they’re strange-looking fellows. They carry swords as long as their own bodies, shave half their foreheads back, and walk around wearing rags like undergarments.”

“Whoever told you about them gave you an accurate account.”

“But why are you suddenly talking about this—”

Jeok Cheongang’s words were cut off by Mungyeong’s immediate reply.

“A long time ago, I once fought the finest ninja in that very Wa Kingdom.”

Jeok Cheongang had heard of ninjas as well.

They were said to resemble the assassins of the Central Plains. Their martial arts were not particularly advanced, but they excelled at concealment techniques and were skilled with concealed weapons such as throwing blades.

“There’s no need to ask how it turned out. So are you boasting that you killed the finest ninja in the Wa Kingdom?”

“I didn’t kill him. My objective was to capture him alive.”

Only one of two fates awaited a captured target.

He would either talk after a little pain, or talk after excruciating pain.

No matter which one he chose, death waited at the end. In the end, the difference was only how painfully he died.

“He chose the latter.”

As befitted someone regarded as the greatest ninja in the Wa Kingdom, he held out for quite some time. Unfortunately for him, however, Salcheonmun, the sect Mungyeong belonged to back then, was unquestionably the greatest assassin sect in the Central Plains.

They employed every torture method they knew.

And so, amid pain worse than death, the ninja was forced to spit out every piece of information he possessed.

Not only information, but every memory sleeping in the depths of his mind.

“That was when I heard about a custom in the Wa Kingdom.”

“A custom?”

“Did you know that there are people in the Wa Kingdom who abandon their elderly parents in the mountains?”

“……It’s nothing to be surprised by these days, but they must be utterly inhuman bastards.”

“I heard they do it to reduce the number of mouths to feed. They abandon them without caring whether they starve to death or are mauled to death by wild animals. They’ve grown too old to work anymore.”

To abandon the parents who had raised them in the mountains simply because they had grown old. If it was true, those people were as vicious as they came.

Even during times of extreme disaster, commoners sometimes committed acts that violated the bonds of family. But to say it was a custom was an entirely different matter.

Mungyeong continued in a dry voice.

“The ninja I captured said that he had once abandoned his own mother in the same way. But what do you think his mother said to the child who left her alone deep in the mountains?”

“You fucking bastard.”

“…….”

“You motherless bastard.”

Seeing Mungyeong’s face harden until it was stiffer than Ten-Thousand-Year Cold Iron, Jeok Cheongang continued with a laugh in his voice.

“If it had been that boy Taekyung, he would certainly have answered that way. But that woman was different. Even if a child abandons his mother, a mother’s heart does not disappear so easily. So what did she say in the end?”

“She told him to take his time. That he might fall if it got dark, so he should not hurry and should be careful on the mountain path.”

Jeok Cheongang could understand what that mother had felt. His decision to leave was rooted in something similar.

Though he was not being abandoned like the woman in Mungyeong’s story, the impulse to leave for fear of becoming a burden to someone precious was much the same.

*And if the Slaughter Saint told this story to this old man, that means…*

Jeok Cheongang looked at Mungyeong with a gaze mingling relief and bitterness.

“May I interpret that as your way of saying you’ll accept this old man’s request?”

Mungyeong always called himself a medical apprentice.

Jeok Cheongang thought that Mungyeong had dredged up a painful past he did not even want to remember because he meant to compare the ninja’s mother to himself and tacitly agree to Jeok’s proposal.

At least, that was what he thought until he saw Mungyeong shake his head the next moment.

“What does that mean?”

“I was under the impression that shaking one’s head had the same meaning throughout history and across the world. Is the Fire Gate Clan different?”

“Then why tell me this story…?”

“I forgot to tell you the ending. After that, the ninja’s mother lived out her natural lifespan and was buried in a sunny place. After hearing her last words, the unfilial son belatedly came to his senses and brought his mother home again.”

“……!”

At that moment, Jeok Cheongang’s body abruptly froze.

At last—only now—he understood. He finally understood what Mungyeong had been trying to say, and how foolish the thought that had trapped him had been.

*Even while being abandoned, the ninja’s mother worried about her child. And this old man was trying to leave that boy of his own accord.*

Jeok Cheongang did not want to become a burden to Jin Taekyung, his one and only Disciple. That was all.

But it was not a pure desire to help his Disciple. It was merely the stubbornness and delusion of a proud old man thinking only of himself.

When had it been? He remembered a conversation he had shared with Jin Taekyung one ordinary day at Mount Jiuhua, when they had lain side by side on a broad rock.

*You’re holding out better than I expected. Is your body made of iron?*

*I’m Iron Man.*

*For spouting nonsense, two hundred geun of iron balls added.*

*……Ah.*

*Ha! Just kidding. I’m getting used to your nonsense, so strangely enough, it doesn’t even annoy me anymore.*

*It’s fine. Put the iron balls on me later.*

*You’re making me say it twice. I said I was joking.*

*I’m serious.*

*Hmm?*

*There’ll be plenty of people stronger than me once we leave. I don’t want to be treated like a burden later on for no reason. They say the iron balls weigh less if you put them on early, so just add them.*

*Look at this fellow. If I add two hundred geun, are you confident you won’t become a burden later?*

*No, but I should at least try my hardest. That way, if I collapse later, Old Master will pick me up, won’t you?*

*Now you’re proudly calling yourself a burden. Fine. If this old man does that, what will you do for me?*

*If you ever collapse, Old Master, I’ll carry you on my back.*

*Hah. Do you think this old man is going to collapse?*

*If you get tired, I could at least support you, couldn’t I? So tell me when it gets hard.*

*……I hear you’re an arrogant, impertinent brat. Five hundred geun of iron balls added.*

*Are you insane, human?*[^2]

It had been nothing more than an ordinary conversation on an unremarkable day.

Yet Jeok Cheongang often remembered it afterward.

He remembered turning away after barking at the boy and letting out a quiet laugh, and secretly watching from hiding whenever he added more weight, worried that the boy might get hurt.

Even now, at this very moment, Jin Taekyung’s voice from that day echoed in Jeok Cheongang’s ears like a distant refrain.

*If you ever collapse, Old Master, I’ll carry you on my back.*

He had always thought that he would stand in front of Taekyung, and Taekyung behind him.

That was why he had been even more determined never to collapse.

*If you get tired, I could at least support you, couldn’t I?*

He did not even want to show Taekyung himself staggering. Like every father in the world, he wanted to be invincible—at least in front of him.

It had been the same on the day he had charged forward prepared to face death.

*Dance of the Fire God and Demon… That’s a pretty cool name.*

*Y-you bastard, how did you—*

*You should’ve crushed his head. Just to be sure.*

*Guh!*

*Old Master!*

But he had not been invincible.

He only realized it much later, after waking from a long sleep.

He learned what kind of ordeal his Disciple had overcome while carrying his fallen, useless Master on his back. How many times Taekyung had risked that precious life and fought desperately against impossible odds.

And so he had made a firm decision. He would never collapse again.

He would never become a burden that put his Disciple in danger.

But he had been wrong.

*We were walking side by side. Following the same path, from the beginning until now. Always together.*

One thought filled his mind.

And in that instant, dark, damp memories from the depths of his past surged upward and clouded Jeok Cheongang’s vision.

Fwoosh!

They were countless memories and emotions stretching back to the beggar boy who had struggled to pick up a single dumpling.

Rage and despair. Sorrow and guilt. They crashed over Jeok Cheongang like waves and bound his entire body.

But why?

Unlike usual, he felt no pain at all.

His chest, which had always felt constricted whenever he remembered the past, was calm. He felt none of the splitting headaches.

*What is this?*

Amid a peace he had not felt in a truly long time, Jeok Cheongang suddenly sensed a cool breeze blowing from somewhere.

A voice came drifting along with it.

*Oh, that feels good.*

*Ahem. This is the finest auspicious site on Mount Jiuhua, personally selected by this old man.*

*This rock is practically a long-life stone bed. Five stars.*

*Kh-hehm!*

Warm.

Brilliant light seeped in.

The darkness that had crouched in the depths of Jeok Cheongang’s heart for decades was slowly scattering.

The Heart Demon.

That was the name of the darkness one person carried within himself, and the chains with which he bound himself.

And what drove all of it away was a cool breeze that blew across Mount Jiuhua on a clear day, along with someone’s voice.

Fwoosh!

*Old Master.*

The light swallowed the darkness. It swallowed the Heart Demon.

Though his eyes were clearly closed, the entire world around him shone with blinding brightness.

A faint smile appeared at the corner of Jeok Cheongang’s wrinkled mouth.

*Yes.*

His snow-white hair stirred in a breeze that had blown from somewhere.

And it was neither an illusion nor a delusion.

Rumble!

At last, the giant who had broken his chains and risen to his feet sent a wind sweeping in every direction, centered around the Fire King Jeok Cheongang.

[^1]: **Wa** (倭) was a historical name used in China and Korea for Japan.

[^2]: A **geun** is a traditional East Asian unit of weight; its exact value varied by time and place.
## Chapter artifact 504

# Chapter 504

Enlightenment comes when you least expect it.

It comes when you have forgotten everything around you and entered a state of selflessness, when death is right before your eyes, or when you finally cast off the chains that have bound your body and mind for decades.

That was how enlightenment came.

Fwoooooosh!

A wind of qi flowing from a single person swept in every direction.

The cave interior was dark, deprived of even a ray of light, but it was now brightly illuminated by a halo of light.

The boy who had been silently watching the strange sight spoke in a quiet voice.

“Have you finally escaped your Heart Demon?”

It had not been intentional from the beginning. Mungyeong had only wanted to tell him something.

That Jeok Cheongang was not alone. That he did not need to isolate himself while carrying every worry and burden on his own shoulders.

And the result had been greater than Mungyeong expected.

The Supreme Peak master known as the Fire King had broken the chains that had bound him for so many years and was stepping into a new realm.

“Seems I wasn’t meddling for nothing after all.”

A complicated mixture of emotions swirled in Mungyeong’s eyes as he murmured under his breath.

He did not know why he had sought out Jeok Cheongang or why he had helped a man with whom he had no particular relationship.

No—even if he had known, he would have pretended not to. That was the kind of person he was. That was how he had lived his entire life.

But…

*It doesn’t feel so bad.*

Mungyeong did not realize that, without his knowledge, a faint smile had brushed across his lips.

Nor did he know that something similar had happened once a few days earlier.

It had happened so briefly that Mungyeong had not noticed. Soon afterward, he slowly turned and stepped out of the cramped cave into the world beyond.

Whoosh.

As if on cue, a breeze from outside blew past, stirring his hair and tickling his nose.

Mungyeong silently gazed at the tall grass and flowers growing thickly around the cave—and the wild animals that had gathered there before suddenly speaking.

“I suppose someone will have to stand guard. If those ignorant wild animals go into the cave, all the enlightenment he worked so hard to attain will be wasted.”

Squeak?

A fawn grazing beside its sleeping mother pricked up its ears.

Amid the wary, curious gazes of the animals, Mungyeong raised his head and looked up at the blue sky.

“It’s a beautiful day. I can’t stay cooped up in a cave in weather like this.”

Step.

Mungyeong muttered as though speaking to himself, then began walking at neither a fast nor a slow pace.

As though bidding farewell to him while he disappeared somewhere with the cave at his back, the wind blew once more.

Whoosh.

A clear sky without a single cloud. A refreshing breeze. Wild animals lying among peaceful nature and wildflowers, all enjoying the sunlight together.

And…

Someone who could not bring himself to enter and was lingering outside.

*Master and Disciple alike.*

No matter how he thought about it, those two really were alike.

Two butterflies fluttered down and landed on Mungyeong’s shoulder as he smiled without a sound.

It was truly a beautiful day.



* * *



The fawn had not been alive for very long, and it was curious about everything.

It sometimes chased butterflies with little bounding hops. It also buried its black nose in the tall grass and flowers, sniffing at their scents.

And as always, it soon lost interest and wandered around looking for something else to do.

Squeak?

But this time was different.

The pitch-black entrance to the cave was strangely alluring, as though it were sucking everything inside, while its mother was asleep after being worn out by raising it.

Most importantly, the strange two-legged animal it had never seen before had disappeared into the distance.

Squeak.

*What’s in there? I want to go inside.*

Squeak!

*All right. Let’s go!*

But the fawn’s firm resolve was crushed in less time than it took to pull at the grass a few times.

Step.

Along with the sudden sound of someone approaching, a shadow fell over its round head.

The startled fawn stumbled backward. Reflected in its black eyes was the silhouette of a large figure.

“Not right now. We’ll go in later.”

The figure gently rubbed the frightened fawn’s head and stared at the pitch-black cave.

The stranger’s gaze was so profoundly somber that the fawn, which had instinctively been about to wake its mother, swallowed its cry.

Squeeeeeak.

“That’s right. Good. Now go back to your mother.”

The figure watched the fawn tilt its head and approach its sleeping mother, then straightened from his bent posture.

He walked toward the cave with steady steps, his voice blurred by the wind.

“Now… I suppose I should go, too.”

The path to the cave was long.

A year and several months had passed since the day the old man and the young man first met.

After taking the long way around, they could finally meet again.

Not one before the other or one behind the other, but side by side, shoulder to shoulder.



* * *



“When the hell is Jin Taekyung coming?”

At Gung Gibang’s irritated complaint, Hyuk Mujin clicked his tongue.

“Tsk, tsk. With a temper that impatient, how are you ever going to beg? Try waiting patiently for once.”

“Listen to the way that Hyuk bastard talks. Are beggars not allowed to be impatient?”

“You need patience if you want to receive even a single iron coin in alms.”

“Did you say the Hyuk Family Textile Shop? Should we send a hundred thousand Beggars’ Sect disciples over there to take a shit each?”

“…Let’s leave family out of this.”

“Then watch your mouth. You think my children don’t have money, but don’t have shit?”

Hyuk Mujin looked at Gung Gibang with disgust.

“I’m going insane. I just ate, so why the hell are you talking about shit? We have to board the ship soon, too.”

“That’s why, before the Hyuk Family Textile Shop gets covered in shit—”

“Ah, I said stop! Hearing about food after talking about eating shit is making my stomach turn!”

“……?”

“……?”

While the two men tilted their heads, sensing that something was wrong, Jin Wikyung was asking someone else a question.

“Tell me, are you certain he will be arriving soon?”

Mungyeong, the young medical apprentice known as the Disciple of the Divine Physician, bowed politely.

“Yes. Young Master Jin definitely said so.”

“We will have to set out before sunset…”

Jin Wikyung murmured as he gazed at the sky slowly turning red.

The declaration ceremony for the New Murim Alliance in Henan was only about a month away. They had to leave diligently from this moment onward to arrive on time while allowing for any unforeseen circumstances along the way.

*No. I should consider us fortunate that we get to travel with Great Hero Jeok.*

Many rumors had already spread about Jeok Cheongang, who had secluded himself for seven days and nights.

Some were hopeful stories claiming that he had finally found the beginnings of enlightenment. Others were impious suggestions that perhaps something had gone wrong with his health. Still others insisted that he had simply chosen not to show himself for no particular reason.

Jin Wikyung did not know which of the three was true, but there was no doubt that he had secretly been worried.

*I was afraid he might say he would not participate in the Murim Alliance… It seems the youngest managed to persuade him.*

Most orthodox Murim practitioners had forgotten this fact, but the Fire King Jeok Cheongang was originally a martial artist who belonged to neither the orthodox, unorthodox, nor Demonic factions—a martial artist who stood between the orthodox and unorthodox factions.

That was also the foundation of the Fire Gate Clan, which had maintained its lineage through one-person succession for hundreds of years. Its successive Sect Leaders had defended their position outside every faction through overwhelming martial might.

*Especially since it was Great Hero Jeok.*

Even a child with a runny nose knew that the Fire King Jeok Cheongang had helped the orthodox faction and led it to victory in the Great Faction War.

But few people knew that this Supreme Peak master from two generations ago had been deeply disappointed by the orthodox faction both during and after the war.

“Now that I think about it, I suddenly remember something my grandfather once said about Senior Jeok.”

Zhuge Feng had come out to see them off. Jin Wikyung’s ear twitched at his words.

“About Great Hero Jeok?”

“Yes.”

“I’ve heard that the previous Family Head was a wise man with remarkable insight. May I ask what he said?”

“Well, it was something I heard in the Family Head’s hall when I was thirteen.”

“I see. And what did he say…?”

“I remember it clearly. At the time, my grandfather was talking about what happened during the Great Faction War. Ah, have you heard about how the members of our family played a major role in the great battle that took place in Sichuan?”

Crack.

Zhuge Feng, who had been leisurely fanning himself, suddenly stopped.

He glanced back and forth between Jin Wikyung’s tightly clenched fist and his flushed face, then slowly lowered the fan.

Jin Wikyung’s martial arts were in no way inferior, but even his appearance alone made him little different from a human weapon.

Besides, with the priceless Water God Dragon’s corpse in his hands, was he not the one holding all the cards?

Zhuge Feng discreetly gauged the mood, cleared his throat, and continued.

“Ahem. In any case, I asked him first. I asked when he thought the tide had first begun to turn in favor of the orthodox faction.”

Jin Wikyung asked in a low, level voice,

“Was it because the members of the Zhuge Clan played such an important role in the great battle in Sichuan?”

“No, that wasn’t it! Absolutely not!”

“That is a relief. Please continue.”

Zhuge Feng began speaking while glancing sideways at the clenched fist.

“It was the first and last time I ever saw my grandfather deliberate so deeply. After thinking for quite some time, he finally answered. Can you guess what he said, Lesser Family Head?”

“You just said it was connected to Great Hero Jeok… Then perhaps it was the great battle in Shaanxi. I’ve heard that although the other Seniors also distinguished themselves, Great Hero Jeok’s achievements were truly astounding.”

The battle in Shaanxi that Jin Wikyung had mentioned was one of the particularly brilliant victories among the countless battles of the blood-soaked Great Faction War.

It was an answer Jin Wikyung had reached after giving the matter some thought, but Zhuge Feng gave a quiet laugh and shook his head.

“Wrong.”

“Then what was it?”

“Anhui.”

“Anhui… You mean that?”

“That’s right. No one could have expected the Demonic Cult’s elite Black Wind Corps, a thousand men strong, marching across Anhui, to be annihilated by a single person. Not even my grandfather.”

Jin Wikyung nodded.

On the day Mount Jiuhua was engulfed in flames, an unknown old man living in obscurity became known as the Fire King, while the Demonic Cult lost an elite strike force that had accumulated countless achievements since the beginning of the Great Faction War.

“That makes sense. It was when Great Hero Jeok first entered the world.”

“But if not for my wise and perceptive grandfather’s judgment, not only would the Black Wind Corps not have been annihilated, Senior Jeok would never have gained the title of Fire King.”

“What do you mean…?”

Zhuge Feng looked around, then lowered his voice as much as possible.

“At the time, every road through Anhui was open to the Black Wind Corps. They had no need to pass through Mount Jiuhua.”

“Wait. Then could it be…?”

“My grandfather never forgot anything he had seen once. This was no different. He remembered a record about a one-person sect in our family’s archives, one describing events from more than a hundred years ago.”

“……!”

“Heh heh. It was a bold gamble, but it worked. It was a stratagem that would put even Zhuge Wuhou to shame, wouldn’t you say?”

As Zhuge Feng casually put his own clan’s ancestor to shame, a deep voice reached his ear.

“Is that what happened?”

“…Huh?”

Zhuge Feng turned around in bewilderment.

He saw a middle-aged man approaching from a distance far too great for his voice to have carried.

“Zhuge Clan, assemble.”

And walking beside him, shoulder to shoulder, was a young man.

# Checkpoint Review — 495–499

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

# Chapters 495–499

## Plot

Taekyung secretly stores the Water God Dragon’s finest bones, scales, flesh, and Origin Essence while arranging for the remaining materials to be sent to the Jin Family of Taiyuan. The Origin Essence is an immense, exceptionally pure inner core damaged by mana; Taekyung considers using it to help Jeok Cheongang, whose recovery from the Formless Ultimate Poison remains uncertain. Jeok, meanwhile, has disappeared and is seen taming an old tiger while reflecting on his age.

Hyuk Mujin records the expedition’s aftermath in a profane diary. The Zhuge Clan seals the Gate’s exposed gap with a formation, though the seal may not solve the underlying problem. Mungyeong continues testing Taekyung through concealed, poisoned attacks. After twelve simulated deaths and seven days and nights of training, Taekyung realizes he was failing by imitating Mungyeong instead of fighting in his own way. He survives the final test—Blindness Powder followed by a killing sword stroke—by awakening all his senses. Mungyeong judges that he has acquired the basics and reveals his former connection to the vanished assassin sect Salcheonmun.

Taekyung completes the Fake Murim Martial Artist Quest, gaining EXP, points, greatly increased Poison Resistance, sharper Qi Sense, and a clue to enlightenment. The Fake Murim Martial Artist—Stage 2 Follow-up Quest begins, with its objective dependent on Mungyeong’s future plans. The Jin Family of Taiyuan arrives at Dongting Lake with more than fifty Jin Dragon Squad martial artists, including Wipeng and Jang Taebo. Jin Wikyung reports that Lee Seowol has rebuilt the Mount Heng Sword Sect, while Jin Mukyung remains secluded after losing to Cheongpung.

Jin Wikyung explains that he founded Ironcraft Hall to bring Jang Taebo back into service, but Jang will not return without one of several legendary materials. Taekyung supplies an imugi’s claw, completing the Sudden Quest and making Jang the Master of Ironcraft Hall. Taekyung has still not contacted Lee Seowol since leaving for Mount Jiuhua, despite her recent attempt to reach Jin Wikyung.

## Continuity

- The Zhuge Clan has sealed the exposed Gate gap with a formation, but whether the seal is permanent or fundamental remains unresolved.
- Taekyung retains the Water God Dragon’s finest materials and Origin Essence; most remaining corpse materials are being sent to the Jin Family of Taiyuan.
- The Origin Essence contains immense, exceptionally pure qi and may be dangerous to anyone unable to withstand it. Taekyung may use it to aid Jeok Cheongang, whose lasting recovery from the Formless Ultimate Poison is uncertain.
- Mungyeong is the Slaughter Saint, formerly Killing Ghost and a teacher of assassins from the vanished Salcheonmun. He has completed Taekyung’s initial poisoned training and intends to teach him secret martial arts without a formal Master-Disciple relationship.
- Taekyung completed the Fake Murim Martial Artist Quest, gained a clue to enlightenment, and accepted the Stage 2 Follow-up Quest. He still cannot remember exactly how he evaded Mungyeong’s final sword stroke.
- The Jin Family of Taiyuan has arrived with Wipeng, Jang Taebo, and more than fifty Jin Dragon Squad martial artists, all at least First Rate.
- Ironcraft Hall now exists within the Jin Family of Taiyuan, with Jang Taebo appointed its master after Taekyung provided an imugi’s claw.
- The Mount Heng Sword Sect has been rebuilt and is growing under Lee Seowol, with Cheol Mubaek out of seclusion and helping manage its affairs.
- Jin Mukyung has remained secluded for more than a year after losing to Cheongpung, subsisting on fasting pills and refusing to emerge until he achieves a great accomplishment.
- Taekyung has not contacted Lee Seowol since leaving for Mount Jiuhua, though she recently sought Jin Wikyung.
- Open hooks: the Gate’s true condition and destination; the Lord of Heaven’s identity; Honglan’s plans in Yunnan; the Dongting Fisherman’s connection to Dark Heaven; Jeok’s lasting condition; and Taekyung’s possible use of the Origin Essence.

## Translation Decisions

- Retain **Water God Dragon**, **Gate**, **Origin Essence**, **inner core**, **innate qi**, **true-origin qi**, and the established System labels **Type**, **Grade**, **Restriction**, and **Description**.
- Render **살천문** as **Salcheonmun**, **실명산** as **Blindness Powder**, **돌발 퀘스트** as **Sudden Quest**, **철기당** as **Ironcraft Hall**, and **철기당주** as **Master of Ironcraft Hall**.
- Render **진룡대** as **Jin Dragon Squad** and **진룡** as **Jin Dragon** when referring to the uniform’s embroidered characters.
- Preserve **Fake Murim Martial Artist**, **Fake Murim Martial Artist—Stage 2**, **Master-Disciple relationship**, **Poison Resistance**, **Qi Sense**, **Teacher’s Day**, and **Agh** in the Quest interface.
- Render **장자방** as **Zhang Liang**, **한신** as **Han Xin**, and **소하** as **Xiao He**.
- Preserve Taekyung’s profane, irreverent narration; Hyuk Mujin’s crude diary humor; Mungyeong’s calm coercive authority; Jeok’s rough speech; and the established terminology from earlier chapters.

## Durable state

{
  "active_continuity": [
    "The Zhuge Clan has sealed the exposed Gate gap with a formation, but whether this is a fundamental or permanent solution remains unresolved; the Gate's residual mana previously mutated local life.",
    "Around one hundred Level 5 Mutated Minnows, locally called Blood Fish, were captured in the Gate's entrance waterways; the remaining population is unknown, and the fish kill one another.",
    "Taekyung suspects Dark Heaven's regeneration, teleportation, and Moving Formation are manifestations of Magic connected to the Gate, and he told Jeok that he came from another world whose evil force is linked to Dark Heaven.",
    "Honglan corrupted the benevolent Dongting Lake imugi and used it to kill many people; the severely injured Dongting Fisherman may be connected to Dark Heaven and the earlier destruction inside the secret refuge.",
    "The Southern Heaven Demon Empress is traveling toward Yunnan and expects to cause further deaths.",
    "Jin Wikyung and Gung Gibang pledged the Jin Family of Taiyuan and the Beggars' Sect to Taekyung's defense; Wipeng and the Jin Dragon Squad have joined Jin Wikyung, and Jin Wikyung has established Ironcraft Hall and recruited Jang Taebo as its master.",
    "Jeok's innate qi is damaged and steadily diminishing despite the Thousand-Year Snow Ginseng and the Divine Physician's treatment; Taekyung remains uncertain whether Jeok recovered without lasting aftereffects.",
    "Mungyeong is the Slaughter Saint, a Returned to Youth Supreme Peak master and the greatest assassin in history; before becoming the Slaughter Saint, he was called Killing Ghost, and he saved countless people as the Divine Physician.",
    "Mungyeong recognizes Taekyung's Heavenly Martial Physique as innate and distinct from Cheongpung's more refined physique; after seven days and nights of poisoned tests, he intends to teach Taekyung secret martial arts without a formal Master-Disciple relationship.",
    "Taekyung completed Mungyeong's tests, gained EXP, points, Poison Resistance, sharper Qi Sense, and a clue to enlightenment, while retaining the Water God Dragon's dismantled materials and Origin Essence after permanently losing 5 Strength and 5 Agility from Sinews and Meridians damage.",
    "The Mount Heng Sword Sect has completed its reconstruction and is growing under Lee Seowol, while Cheol Mubaek has ended his seclusion and is helping manage the sect's affairs.",
    "Jin Mukyung has remained secluded in the training hall for more than a year after losing to Cheongpung, subsisting on fasting pills while refusing to emerge until he achieves a great accomplishment."
  ],
  "continuity_sources": [
    499,
    498
  ],
  "open_questions": [
    "Will Zhuge Feng's formation permanently seal the Gate gap, and what lies beyond it if the Gate is reopened?",
    "What is the Lord of Heaven's identity, and how is he connected to the dangerous force Taekyung associates with his original world?",
    "Where is the Southern Heaven Demon Empress ultimately headed, and what does she intend to do in Yunnan?",
    "What is the Dongting Fisherman's exact role within Dark Heaven, and how was he connected to the earlier destruction inside the secret refuge?",
    "Has Jeok fully recovered from the Formless Ultimate Poison, and will Taekyung use the Water God Dragon's Origin Essence to aid him?"
  ],
  "safe_through": 499,
  "temporary_decisions": [
    "Render 산공독 as Energy-Dispersing Poison, 강력한 산공독 as Potent Energy-Dispersing Poison, 칠보추혼산 as Seven-Step Soul-Chasing Powder, 강력한 칠보추혼산 as Potent Seven-Step Soul-Chasing Powder, 심각한 복통 as Severe Stomachache, 고기 방패 as Meat Shield, 독 장아찌 as Poisoned Pickle, and 독의 as Poison Physician; retain secret martial arts, Master-Disciple relationship, Killing Ghost, and Fake Murim Martial Artist, and preserve 악 as Agh in the Quest interface; render 실명산 as Blindness Powder, 살천문 as Salcheonmun, and 스승의 날 as Teacher’s Day.",
    "Render 기억의 파편 as Memory Fragment, 게이트 공략 as Gate Conquest, 텔레포트 as Teleport, 마법 as Magic, 혈어 as Blood Fish, and 변이된 송사리 as Mutated Minnow; render 강력한 마비산 as Potent Paralysis Powder, 강력한 미혼산 as Potent Soul-Bewitching Powder, 전신 마비 as Full-Body Paralysis, 독성 흡수 as Poison Absorption, and 해독 as Detoxification.",
    "Render 시산혈해 as sea of corpses and blood and retain Old Master for 노야 with the established rough, profane Taekyung-Jeok banter; render 해시 as hour of the Pig, 한 식경 as half an hour, 타구봉 as Dog-Beating Staff, 창룡 as Azure Dragon, and 무량수불 as Infinite Life Buddha; preserve geun as the traditional weight unit with a footnote.",
    "Render 선천지기 as innate qi, 진원진기 as true-origin qi, and 천기 as heavenly patterns.",
    "Render 심마 as Heart Demon, 비급 as martial arts manual, 송문고검 as Pine-Pattern Ancient Sword, 반로환동 as Returned to Youth, 강강수월래 as Ganggangsullae, 생사부 as Book of Life and Death, 기막 as qi curtain, 무극태을검 as Martial Extremity Grand Unity Sword, 이룡 as Two Dragons, 원정 as Origin Essence, 내단 as inner core, 영험한 기운 as sacred energy, 대호 as great tiger, 취팔선권 as Drunken Eight Immortals Fist, 귀면 as Ghost Face, 요단강 as Jordan River, and 진룡 as Jin Dragon."
  ],
  "version": 1
}

## Reading copies

## Chapter artifact 495

# Chapter 495

When you’re a newborn, not being able to control your bladder is perfectly normal.

At seven? If you’re kindergarten age, it happens. If you’re in elementary school, it would be a little embarrassing, but it’s not unheard of in the lower grades.

But I was twenty-seven.

The twenty-first-century mass media had competed to proclaim me a new hero, while the martial artists of Murim called me the heir of the Fire King and a rising star destined to change the face of Murim.

And yet…

*Fuck.*

I had taken a huge dump. At twenty-seven. Not just peed myself, either. I had shit myself. In front of Mungyeong, no less.

*Ah, ahh. Anastasia!*

*……Take your time cleaning up and come back.*

After a long silence, Mungyeong left me with only those words.

It was obvious that he was less worried about me than about getting shit on his short sword. What a damn old man.

Every time I thought about what had just happened, I wanted to log out and never return to Murim again. To hell with Dark Heaven and everything else.

*Should I just leave Murim altogether?*

As I sat by the water, seriously contemplating it, someone approached me with a smile on his face.

“Captain. What are you doing all by your—”

The moment I saw the familiar face, I unleashed a heartfelt string of profanity.

“Hyuk Mujin, you son of a bitch.”

“Why are you swearing at me all of a sudden?”

“Stay out of my sight for a while. Please.”

“Even if you’re the Captain, that’s too much. Is that any way to spit in a smiling person’s face?”

“Khack—ptui!”

“Gah!”

Hyuk Mujin barely dodged the glob of phlegm and looked me over as though I were a lunatic.

“What happened to make you act like this?”

“Nothing happened. So shut up and disappear from in front of me.”

“Something about that context seems off.”

“Want me to rearrange your arms and legs?”

Because of the water that bastard had brought me, I had lost stats and my dignity as a human being.

I was barely holding back my fist because I knew Mungyeong was the real culprit.

Hyuk Mujin, unaware of the circumstances, looked bewildered.

“Good grief. Anyone watching would think you’d shit your pants because of me.”

“……!”

“What is that reaction supposed to mean?”

“……Nothing. Why are you here?”

Hyuk Mujin watched me suspiciously, then pointed toward the people standing in the distance.

“We’ve mostly finished sorting things, but apparently there’s something strange.”

“Strange? What?”

“It seems there are fewer bones and scales from the imugi than expected. I think you should come take a look yourself.”

“Really?”

“Yes. He’s furious because the amount recovered is far too little compared to the imugi’s size. He’s searching the area as though he’s hunting lice. He says that if someone stole it, he’ll uncover the culprit in the name of the Primordial Heavenly Venerable’s honor.”

“……”

What was he, Detective Kindaichi?

He must have completely lost his mind after helping with the Taiji Wisdom Sword just to obtain some bones, only to think someone had snatched them away.

The more I listened, the more absurd it seemed, so I asked Hyuk Mujin,

“How could anyone steal it? And it’s not like only a little went missing. It must be well over a thousand geun.[^1] How could anyone hide that without us noticing?”

“Exactly. Besides, only a handful of people even know this place—”

Hyuk Mujin stopped mid-sentence and turned to me.

“But how did you know?”

“Hm?”

“About the amount that disappeared. You said it must be over a thousand geun.”

“I just took a rough guess. They’ve been making an awful racket over there for a while.”

I answered as calmly as I could, but I felt a sudden stab of guilt.

Because…

*He’s sharp. I need to watch what I say.*

The culprit Perfected Being Hyeongong had sworn to find was me.

Every time I thought about all the by-products piled up in my inventory, I felt full.

*Come to think of it, I did take quite a lot.*

It had been easier than lying in bed playing with my smartphone.

The Water God Dragon’s corpse was enormous, and I had personally worked on more of it than anyone else, sweeping all the choice pieces into my inventory.

The sharpest tailbone, the unusually hard scales from its neck, and even some flesh I had taken just in case.

If I piled everything I had smuggled away in one place, it would be large enough to dwarf a decent-sized manor.

“……Why are you smiling so contentedly?”

“Me? When did I?”

“Just now. You looked incredibly shady.”

Apparently, the joy of having pulled off the perfect crime had shown plainly on my face. I answered with a straight face.

“I didn’t do that.”

“…….”

“Anyway, don’t worry about what’s happening over there. Go get things ready.”

“Ready for what?”

“We’re going back. Do you want to live here forever?”

The Water God Dragon’s already sorted corpse would be moved little by little, very discreetly, by people we could trust.

Most of it would become the property of the Jin Family of Taiyuan.

*It’ll be a huge help when the battles ahead begin.*

After organizing my thoughts, I stood up.

Hyuk Mujin had already run off into the distance the moment I finished speaking. Watching his retreating back, I muttered inwardly.

*Inventory open. Summon.*

Shhk.

As soon as I spoke the activation words, the Water God Dragon’s bones, scales, and flesh appeared in my hands. A satisfied smile spread across my face.

*Item appraisal.*

Ding.

> **System**
>
> **Item Window**
>
> **Water God Dragon’s Bones**
>
> **Type:** Material  
> **Grade:** Supreme Peak  
> **Restriction:** Only a Master Artisan can forge it.
>
> **Description:** The bones of the imugi known as the Water God Dragon, who lived for countless years. They possess incredible hardness and contain an unknown sacred energy. If worked by a Master Artisan who has reached the proper realm, their true power can be drawn out.

Although there were slight differences, the System’s description of the scales was similar.

The gist was that they were Supreme Peak materials containing sacred energy and possessing incredible hardness. As for the flesh, it said that consuming it over a long period could increase internal energy and abilities.

*This is like winning the lottery.*

But the real lottery prize was something else entirely.

If the bones and scales were Lotto and the flesh an annuity lottery, this was the American Powerball, with a jackpot on an entirely different scale.

With my heart pounding, I took *it* out of my inventory.

*Item appraisal.*

Ding.

> **System**
>
> **Item Window**
>
> **Water God Dragon’s Origin Essence**
>
> **Type:** None  
> **Grade:** None  
> **Restriction:** None
>
> **Description:** The Origin Essence of the imugi known as the Water God Dragon, who lived for countless years. Though damaged by mana, it is a type of inner core extracted according to the Water God Dragon’s will. It contains qi that is exceptionally pure and immense, and is on an entirely different level from ordinary elixirs. However, if you cannot withstand the qi contained within it… (The rest is omitted.)

*Amazing.*

I carefully stroked the **Water God Dragon’s Origin Essence** in my hand.

The final line was ominous, but this was undoubtedly the greatest reward I had gained from my trip to Hubei.

*“On an entirely different level from ordinary elixirs.” How powerful could it be?*

It had been contaminated by mana, so it was probably inferior to the amount of qi the Water God Dragon had originally possessed. Even so, it was still immense.

The Water God Dragon had lived for more than five hundred years. Even by a simple calculation, that meant it had accumulated at least ten jiazi of qi.

From that perspective, the reduction in the Origin Essence’s power was practically a blessing in disguise.

*When the vessel is small, the water spills over.*

As the final line of the item description suggested, even I would burst like a balloon if I tried to take in that much qi all at once.

*The question is when and where to use it.*

The faces of several people appeared in my mind. One particularly old face kept floating before my eyes.

*Old Master.*

I had not thought of Jeok Cheongang merely because he was old.

The reason, absurdly enough, was Mungyeong’s poison.

After losing ten points of my precious stats to the aftereffects of Seven-Step Soul-Chasing Powder and then shitting myself because of the Severe Stomachache, a thought had crossed my mind.

*If Seven-Step Soul-Chasing Powder did this much… What condition must Old Master be in after being poisoned by the Formless Ultimate Poison?*

Seven-Step Soul-Chasing Powder was certainly an extreme poison, but it was not powerful enough to threaten the life of a Supreme Peak master who had reached a proper realm.

The Formless Ultimate Poison that had infected Jeok Cheongang in Henan, however, contained a level of toxicity that made Seven-Step Soul-Chasing Powder look insignificant.

Even the Luoyang Strange Physician, one of the most renowned physicians in the world, had failed to find an answer and advised us to seek the Divine Physician. And because the poison had already spread so extensively, we had needed to obtain the Myriad-Poison Ring.

*Fortunately, the treatment was completed thanks to the Thousand-Year Snow Ginseng…*

But had he really recovered without any significant aftereffects?

I stared at the **Water God Dragon’s Origin Essence**, my gaze filled with both doubt and worry.

Perhaps this was an item whose purpose had been decided from the very beginning.

“Little Brother!”

*Inventory open. Store.*

I hurriedly put the **Water God Dragon’s Origin Essence** back into my inventory at Jin Wikyung’s shout from behind me, then turned around with an awkward smile.

“Yes, I’m coming!”

Today had been a day of many satisfying gains.

And yet it was also a day when one corner of my heart felt heavy, and when my stomach seemed to twist for some reason.

Grrrggg.

“……Sigh.”

Ah. The status abnormality still hadn’t worn off.

* * *

Settling near water was not a habit unique to humans. Animals in nature did the same.

Birds nesting along the cliffs that lined the broad waters of Dongting Lake, followed by wild boars, foxes, wolves—and even tigers.

If Dongting Lake below the cliffs was territory permitted to humans, then the cliffs above belonged to the animals.

It was a peaceful place where no human foot had ever reached.

That was why the great tiger, the king of this place, was displeased by the sudden arrival of an uninvited guest.

- Grrrrrrr.

The growl spilling between its sharp teeth carried all its irritation.

Its nose flared without pause as it tracked the human scent that had yet to fade.

It did not take long for its sensitive sense of smell to locate its target.

- Grrr.

At the edge of a cliff that dropped away as though it had been carved straight down, the great tiger discovered the uninvited guest and snorted.

What kind of audacious fool had come here? As it turned out, the visitor was even smaller and shabbier than the tiger had expected.

The uninvited guest was an old human who did not even look large enough for one bite.

Ssshhk.

The moment the body weighing several hundred geun moved nimbly toward the old man, the old man spoke.

“So there was a tiger.”

- ……!

The great tiger’s silent approach came to an abrupt halt.

The old man, who had risen to his feet on his short legs, was staring straight at it.

“You’re an old one too.”

- Grrr.

The great tiger bared its teeth, but the old man merely let out a quiet laugh.

“Don’t make such a fuss. Come here and keep this old man company.”

- Raaaargh!

“You striped mutt, do you want to die? I said come here.”

The great tiger flinched.

For some reason, it felt every hair on its body stand on end as it awkwardly approached the old man.

When the wrinkled hand gently scratched its chin, it felt good despite itself.

- Prrrrr.

Watching the great tiger purr, the old man—Fire King Jeok Cheongang—murmured softly.

“Yes. I’ve already grown old.”

The sky spread above the cliffs was clear, but his heart was dark.

[^1]: A geun is a traditional East Asian unit of weight; a Korean geun is roughly 600 grams.
## Chapter artifact 496

# Chapter 496

“Hmm.”

Hyuk Mujin picked up his brush carefully. The small booklet he had spread out on the table was already packed with writing he had begun several days earlier.

X Month X Day. The weather was a damn mess, then cleared up.

I had a nightmare. It was about a monster that looked like a dragon. It was so frightening that I wet myself in my sleep.

As soon as I woke up, I secretly went to the stream to wash my undergarments and trousers, only to find Young Hero Gung already there, washing a pair of shit-stained trousers.

What a filthy bastard. Even a beggar could be more respectable than him.

I have no idea why our Captain insists on dragging around someone who shits his pants.

But why am I in the infirmary?



X Month X Day. Clear skies.

The nightmare was real.

According to Mungyeong, the monster was an imugi, and demonic qi had surged all the way into its marrow, driving it to commit an atrocity that outraged heaven and humanity.

Fortunately, thanks to the Captain stepping in, I was barely affected by the demonic qi. However, I was diagnosed with the need to keep writing in my diary and retracing my memories for the time being.

That aside, I couldn’t believe those ridiculous scenes had all been real.

While listening to Mungyeong, a question suddenly occurred to me. I asked whether that dream—no, whether the sight I had seen of him fighting there had also been real.

Mungyeong answered that it had not. Young Hero Gung joined me in questioning him, but for some reason, I fell asleep on the spot. I must have been tired.

But why do I have a bruise on my forehead?

I don’t know. I should go back to sleep.



X Month X Day.

I went to dispose of the corpse. I shit myself once at the imugi’s enormous size, then a second time at the Captain’s butchering skills.

I asked him to make me a Bone Sword and got beaten until my skull rang.

I heard that the imugi’s corpse, divided into bones, scales, and flesh, would be transported in secret.

Oh, and for some reason, a considerable amount of the sorted remains disappeared.

Perfected Being Hyeongong, enraged, declared that he would find the culprit. But that was ridiculous. It wasn’t a fist-sized amount. Who could steal that much?

After leaving the minor commotion behind and boarding the boat back, I noticed a terrible smell of shit coming from somewhere.

Unable to stand it any longer, I brought it up first. Before I could even finish speaking, the Captain pointed at Young Hero Gung.

He vehemently denied it, but having witnessed him shit himself a few days ago, I couldn’t believe a word he said.

Mungyeong, sitting beside me, wore an odd expression the entire time.

He probably wanted to unload a bucketful of abuse because of the smell, but was holding back out of consideration for Young Hero Gung’s dignity.

What a good kid. He’s so innocent and endearing every time I see him.



X Month X Day.

It has been two days since we disposed of the imugi’s corpse.

I don’t know what happened, but Sir Jeok has disappeared completely, and the Captain grows gaunter by the day.

I joked that he looked like someone being tormented by poison and ambushes day and night, and he glared at me as though he wanted to kill me.

He only makes a fuss at me because I look easy.

Just as I was thinking that, Young Hero Gung said the same thing and I watched him get beaten. I felt better.



X Month X Day.

This is the first time I’ve written in three days. The reason I neglected my diary was that there was nothing worth writing about.

After Sir Jeok, the Captain also became difficult to see, and Mungyeong has been wandering off somewhere or other, so he is rarely around too.

What would a martial artist like me do with his free time? Young Hero Gung and I searched for a decent place and trained.

His breath smells like a sewer, but when he keeps his mouth shut during training, he’s not so bad.

On the other hand, Young Hero Cheongpung’s advice, despite somehow finding us, was useless every time.

Whenever I asked him about martial arts, I got one of two answers.

“It’s really easy.”

“Why can’t you do it?”

You bastard. If it were that easy, would I still be First Rate?

Perhaps because he was frustrated, he demonstrated it for me, but I couldn’t understand a thing.

Every time we trained, that water snake called something like Mimi swallowed Blood Fish beside us. Maybe because of that, he seems to have grown quite a bit. His horns have grown too.

No wonder it seemed as though the Blood Fish had gone extinct. They must have all gone down that bastard’s throat.



X Month X Day.

I’ve become fairly close with several martial artists from the Zhuge Clan and Wudang, and thanks to that, I heard some news.

The Zhuge Clan is testing a formation under the direct command of Sir Zhuge Feng, the Crouching Dragon Guest, apparently one that can completely seal the gap.

I hear that if they can’t block it, strange things like the Blood Fish will continue to appear. I have no idea what bizarre and unfathomable method those Dark Heaven bastards used to create them.

Meanwhile, Wudang is still tracking the Killing Ghost.

Even with the authorities joining the search and turning Hubei Province upside down, they still haven’t found him. He must be an expert at running away.



X Month X Day.

It has been seven days and nights since I came here. The Captain’s complexion was calm when I saw him again after so long.

Before, he had been covered in injuries from whatever training he was doing alone, and his complexion had been pale or even bluish. He seems to have recovered now.

Instead, his temper has grown sharper, and he moves like a ghost.

He gives off so little sign of his presence that he caught Young Hero Gung and me bad-mouthing him and beat us within an inch of our lives.

No, seriously. How did he hear us from that distance?

Come to think of it, Mungyeong had a satisfied expression while I was being beaten…

I must have imagined it.



“Hmm.”

That was as far as the diary recording everything he had seen and experienced over roughly ten days went.

Hyuk Mujin stared down at the small booklet and sank into thought. Just as he was about to draw the first stroke of a new entry, noisy shouts came from outside.

“It worked—it worked!”

“Family Head! We did it!”

“Not you—I did it! As expected, I’m a genius! Zhuge Wuhou!”

Screech! Blot!

His concentration wavered, his hand slipped, and the brush shook.

Hyuk Mujin’s face twisted as he tried to write with the mindset of a great literary master.

“Which bastard was that?”

A familiar voice slipped into his ear as he raged.

“The bastard you’re talking about sounds like Sir Zhuge Feng. Shall I pass along your words?”

“Go ahead. Then Young Hero Gung dies, and I die right after him.”

Hyuk Mujin answered gruffly and put down his brush as Gung Gibang entered the tent without permission.

“But what on earth is going on outside?”

“It looks like the Zhuge Clan succeeded in completely sealing the gap.”

“With a formation?”

“What else? Rocks?”

“Oh, come on. Why couldn’t we block it with rocks?”

“It’s not a fundamental solution. And if it could have been handled that way, they would have sealed it long ago. Think before you speak.”

“Oh, really? Do you shit yourself because you think too much?”

“A dog that pissed itself criticizing a dog that shit itself.”

“Pissing is better than shitting. Besides, Young Hero Gung did it twice. Last time, when we went to dispose of the imugi’s corpse…”

“Ah, this is driving me crazy. I told you, that wasn’t me!”

Hyuk Mujin clicked his tongue as Gung Gibang pounded his chest.

“You should know when to stop denying it.”

“I’m telling you, it’s true!”

“If it wasn’t Young Hero Gung, then who was it? Hmm? Surely you don’t think Perfected Being Hyeongong did it?”

“Jin Taekyung! I swear that bastard reeked of shit—gah!”

Gung Gibang suddenly stopped, his face going pale as he looked around.

Only a few days earlier, he had been beaten half to death after having a similar conversation.

“He’s not here, right?”

Hyuk Mujin swallowed dryly as well.

The Jin Taekyung he knew had a fiery personality. Whoever started the insults, he would happily beat both sides senseless.

“P-probably?”

“You’re sure?”

“How would I know? If you can sense the Captain’s presence, you’re already a Supreme Peak master. Or a ghost.”

The two of them looked around with every sense on high alert, then let out deep sighs of relief.

Suddenly, the absurdity of their situation struck them. They had become afraid after saying only a few words.

“How long are we going to live like this?”

“Until the Captain dies.”

“What if he undergoes Returned to Youth later?”

“Then we bite our tongues and kill ourselves. What else can we do?”

“Damn it. That Jin Taekyung bastard is a real monster. How can anyone be like that?”

Hyuk Mujin nodded vigorously in agreement. He had watched Jin Taekyung since the days when he had been a delinquent, so he couldn’t help but sympathize.

“That’s true. And not just one of them—there are two.”

“Young Hero Cheongpung? Don’t even get me started. After seeing the Drunken Eight Immortals Fist only a few times, he started imitating it pretty closely. If my master found out, he’d try to kill me for leaking our sect’s secret art.”

“Ooh.”

“……I have a fairly good idea what you were just thinking, but keep your mouth shut forever. I’m really going to die.”

“Oooh.”

“You vile bastard.”

Gung Gibang shook his head and suddenly spoke.

“But what is your liege doing? I haven’t seen him at all.”

“I wouldn’t know. He may be training, or he may not. Sometimes he stays in his tent all day.”

“Sir Jin is always busy with one thing or another, and I haven’t seen Sir Jeok in a long time.”

Jeok Cheongang had completely vanished after the first day he arrived.

Many people were curious about his whereabouts, but no one was worried about his safety.

He was the Fire King. Those two words alone were proof enough.

“Who could possibly harm the Fire King?”

“True. Even Dark Heaven wouldn’t dare. If they tried anything, three or four of their pillars would have been ripped out, and the surrounding area would already have been reduced to ashes.”

Gung Gibang nodded in agreement and continued.

“Wait. Come to think of it, I haven’t seen Mungyeong around lately either.”

“Now that you mention it, neither have I. Whenever I see him, he’s with the Captain.”

“Really?”

“Yes. I wonder if it has something to do with the injuries the Captain suffered while training…”

“Hmm.”

“Why?”

“Nothing. Something smells fishy.”

“Did you shit yourself again?”

“Hyuk Mujin, you lunatic. That’s not what I mean. I’m saying there’s something going on between them.”

Gung Gibang narrowed his brow, deep in thought.

“Wait. Could it be?”

“Could what be?”

“You still don’t get it? Why those two have been together so often lately?”

Hyuk Mujin’s expression grew strange.

As he listened to Gung Gibang, something clicked.

“Then perhaps…”

“That’s exactly what you’re thinking.”

“Good heavens. How can this be?”

“If you think about it, it is strange. The Captain punches us whenever he gets bored, but he hasn’t used so much as a single act of violence against Mungyeong.”

“He barely curses at him anymore, either. And he was suspicious the last time we went to dispose of the imugi’s corpse.”

“When Jin Taekyung disappeared, Mungyeong wasn’t there either.”

“Exactly! The Beggars’ Sect’s future Sect Leader never disappoints!”

“Then it’s certain. Mungyeong…”

Gung Gibang’s face stiffened as he spoke.

“He must be learning martial arts from that Jin bastard.”

“Ah, Mungyeong! How did you end up making such a terrible choice?”

Hyuk Mujin was genuinely heartbroken. The thought of ink named Jin Taekyung bleeding into Mungyeong, who was as white and clean as a blank sheet of paper, made his chest ache.

“What sin did that child commit?”

“Alas, what a tragedy. I have no face to show the Divine Physician in Sichuan.”

“Mungyeong, Mungyeong can’t do this! We can’t let him walk the same path as us!”

“The water has already been spilled. Jin Taekyung is a Fiend. Now that Mungyeong has fallen into the hands of such an evil bastard, there’s nothing we can do.”

“Then by now, Mungyeong must be…”

“Whew…”

“Ah…”

The two of them let out sighs filled with simultaneous lament.

Thinking of Mungyeong, who must by now be fighting for his life under Jin Taekyung’s evil clutches, they felt their hearts grow heavy.

*Hang in there, Mungyeong. Please survive.*



* * *

*Please, somebody save me.*

Slash!

A current of wind grazed my neck.

The pain was as cold as ice, then immediately flared hot. A bead of cold sweat ran down my forehead and dropped onto the ground with a soft tap.

Whoosh, tap!

I righted myself in midair and stared straight ahead.

“That was a little dangerous.”

An answering voice came back—or rather, it was Sound Transmission.

—That was the point.

“No, I’m not joking. I really almost died.”

—That is welcome news.

*Where the hell is he?*

No matter how carefully I looked around, I couldn’t see him. There was only the Sound Transmission, impossible to locate.

“Fucking hell.”

—What kind of hell?

I took a deep breath and gripped the shaft of White Flame.

Toward whoever was watching me from somewhere unseen, I muttered as though spitting the words out.

“This is so fucking shitty I can’t keep doing this.”

Whoosh!

In place of an answer, a blinding sword strike flew toward me.
## Chapter artifact 497

# Chapter 497

Half an hour.

That was the longest I could hold out. Feeling the cold edge of a sword against the back of my neck, I muttered under my breath.

“God, this sucks.”

Ssshhk.

A sharp pain stabbed me, and blood slid down the back of my neck. The intent behind the action was so obvious that I couldn’t help sighing.

“I lost. Let’s stop now.”

“Wrong. Again.”

It was a dry voice I hadn’t been able to hear during the fight. And I already knew what its owner wanted me to say.

“…I’m dead. Is that enough?”

The blade slowly digging into my neck came to a sudden stop. When the cold metal vanished, I pressed a hand to the wound to staunch the bleeding, then turned around.

A man was sitting on a rock about thirty feet away.

“Do you know how many times you’ve died?”

“Twelve.”

Five times, my Sinews and Meridians had been severed in all four limbs. Three times, I had died from a Pressure-Point Strike to a lethal acupoint. Three more times, my heart had been pierced. And just now, my throat had been cut.

I hadn’t actually died, but it was practically the same thing. Wiping the sticky blood from my neck with my sleeve, I looked at Mungyeong.

“It’ll be different next time.”

“That is what I’ve heard eleven times already.”

“I mean it this time.”

“That makes twelve.”

“……”

What a memory.

As I stood there speechless, Mungyeong asked me a question.

“Do you know why you died?”

A fight always left behind a result, and results always led to thought.

I silently replayed my fight with Mungyeong in my head before blurting out an answer.

“Because I fought like an assassin?”

“As expected, you know nothing… Hmm.”

Mungyeong had begun speaking almost at the same time as me, then let his voice trail off.

“Was I wrong?”

“Continue.”

“I don’t know exactly when it started, but I found myself imitating you. The movements you showed me and things like that.”

At first, after being beaten so badly I was practically a Poisoned Pickle, I began paying attention to everything around me. After that, I started copying Mungyeong’s movements bit by bit.

As I dueled him two or three times a day, those movements gradually became familiar to my eyes and body.

But…

“That was my mistake.”

“Why?”

“When you wear new shoes, they rub your heels raw. If the shoes are smaller than your feet, even more so.”

“Be more specific.”

“I should have stopped trying to imitate you so clumsily and fought in my own way. Especially against a Slaughter Saint.”

“……”

Mungyeong stared at me in silence for a while before tossing out a single remark.

“You’re not a complete idiot.”

“Oh, was that a compliment?”

“It means you’ve only just reached the basics.”

“Exactly. Thank you for the compliment.”

Mungyeong’s brow furrowed.

“Are your ears plugged?”

“No. They’re perfectly open.”

“……”

“You have a real talent for getting on people’s nerves.”

“Either way, reaching the basics means it was a compliment. Why are you so bad at being honest? Are you going through puberty?”

“I told you I’m not!”

“Why are you suddenly shouting?”

“When did I shout? I’m not!”

“…Now that I think about it, maybe you are.”

*Yeah, right.*

But if I talked back one more time, it looked like my head might really fly off.

Mungyeong had shouted in anger, but he soon returned to his usual calm, dry tone as though nothing had happened.

“The basics are merely the basics. There have been many others like you before.”

*Others like me?*

I cautiously opened my mouth.

“Do you have other Disciples?”

“Of course. Did you not meet one in Sichuan?”

“Other than Old Man Dong. You know exactly what I mean, so why are you changing the subject?”

“……”

Silence was as good as an admission.

The thought that the Slaughter Saint had hidden Disciples made my curiosity rear its head.

“Who? Who are they? Do you still keep in touch? Do you all go out to eat together on Teacher’s Day[^1]?”

“I have no reason to answer you. And what nonsense is Teacher’s Day?”

“You’re awfully difficult.”

“……”

“Your words and conduct grow more insolent by the day. Do you have five lives or something?”

“Judging by the fact that I’ve died and come back twelve times, I’d say I have about thirteen. So are you really not going to tell me?”

Mungyeong stared at me before speaking abruptly.

“I’ll tell you. But there is a condition.”

A condition from the Slaughter Saint.

I put on a confident expression and opened my mouth.

“It’s about time to eat. I’ll be going now.”

“I distinctly remember that you already ate.”

“I eat five times a day.”

“Stay and listen anyway. You seem quite curious.”

“Everyone has their own life and secrets they want to keep hidden. Why would I pry into them? Anyway, I’ll be off.”

“Stop right there if you don’t want your head cut off.”

“……”

*Damn it. I shouldn’t have asked.*

Feeling my guts twist with panic, I turned my half-turned body back around.

Fine. Since things had come to this, I might as well hear the story.

“So, you really had other Disciples?”

“They weren’t Disciples, but I taught several people.”

“That sounds like you’re saying there aren’t any anymore.”

“An exceedingly long time has passed. There’s no way any of them could still be alive.”

“Were they involved in…?”

“They were assassins. They belonged to the Salcheonmun with me.”[^2]

Salcheonmun.

Even the name smelled of blood.

*So this man had a sect, too.*

It made sense when I thought about it. No matter how extraordinary Mungyeong was, he hadn’t been born an assassin.

*But if it was the sect the Slaughter Saint belonged to, it should have been fairly famous.*

Yet no matter how thoroughly I searched my memories, the name Salcheonmun was completely unfamiliar.

Just then, Mungyeong seemed to notice my question before I could ask it.

“It’s pointless. The place disappeared long ago.”

There was only one reason a sect disappeared.

Watching Mungyeong’s expression, I carefully put a single word into my mouth.

“Annihilated?”

“Yes.”

“How did that happen? No, before that—weren’t you the Sect Leader?”

“The wrong path was chosen, and the price was paid. That is all I have to say.”

Mungyeong finished speaking and rose to his feet. A short sword in his hand was already radiating vivid blue sword energy.

“Now. It is time to pay the price.”

“Excuse me?”

“Evade my one sword stroke. That is the condition.”

Most people would probably think, *How am I supposed to evade that?* But from my perspective, it was worth trying.

I had endured half an hour against the Slaughter Saint of all people while clumsily pretending to be an assassin. One sword stroke should be manageable.

“If I evade it, will you tell me more later?”

“Of course.”

“Fine. Why not?”

Mungyeong added one more thing.

“Close your eyes.”

“Fuck. Are you kidding me?”

“Then you will die. Not the thirteenth time, but for the first and last time.”

Before he had even finished speaking, Mungyeong’s sleeve fluttered.

Having grown accustomed to his attacks through experience, I instinctively turned my head. But what flew toward me was not a hidden weapon. It was something else.

*That’s…*

It was powder so fine that I could see it only by pushing my visual acuity to its absolute limit.

The powder rode a wind blowing toward me. The instant it touched the air—

Whoosh!

Darkness swallowed the world.

No. That wasn’t right.

The darkness had not swallowed the world. It had swallowed me.

Beep.



> **System**
>
> You have been poisoned by **Blindness Powder**!
>
> You temporarily lose your eyesight!
>
> Rapid **Detoxification** is required! If Detoxification is delayed too long, permanent damage may occur!

My body hair stood on end as the System’s alert pierced my ears.

Blindness Powder? Poison didn’t matter. I was still wearing the Myriad-Poison Ring.

The problem was that Mungyeong’s sword was approaching through the darkness far faster than the ring could detoxify the Blindness Powder.

Ssshhk.

I couldn’t see anything. But I could feel it clearly.

In a world that seemed to flow in slow motion, as though someone had pressed a pause button, I sensed the killing sword approaching while erasing the wind around it.

*This is…*

A move performed by the greatest assassin in history.

A killing intent unlike anything I had ever felt before—so subtle and terrifying that it made me shudder.

I stared blankly at a world filled with darkness.

And within that suffocating space where nothing was visible, I felt every sense within me awaken.

Slash!



* * *

Wudang, the Zhuge Clan, and the Beggars’ Sect.

Although they had selected only trustworthy elites for the sake of secrecy, the caliber and sheer number of those present were impossible to ignore.

Among the several hundred martial artists from prestigious great sects, the figure of a young medical apprentice was bound to stand out wherever he went.

“Oh, it’s you. Are you just coming out?”

“I’ve just come from seeing Young Master Jin.”

“You seem to be dropping by more often these days.”

“Yes. He’s been training so harshly lately that he keeps getting hurt.”

“Good heavens. I see. Great Hero Jin really is something. He’s younger than my son, if you count their ages, yet he never rests on his current realm and keeps striving…”

“He must be an incredible master. I’m completely ignorant when it comes to the Murim.”

At the young medical apprentice’s innocent remark, the Zhuge martial artist standing guard let out a short laugh.

He had been bored, but now he felt a little guilty for bothering a child whose only training was in medicine.

“He is incredible. No doubt about it. You’ll understand someday, too.”

“Hmm. Is that so?”

“If you’re not involved with the Murim, you might not know. Anyway, has today’s training ended?”

As though he knew nothing, Mungyeong tilted his head and answered.

“No. He told me that no one was to approach for the next two shichen.”

“Understood. This is Great Hero Jin we’re talking about—we can’t interrupt his training. I’ll pass that along to the next guards.”

“Yes. Then take care.”

Mungyeong politely bowed at the waist and was about to leave when the martial artist suddenly spoke.

“My, his training must be rougher than I thought.”

“Excuse me?”

“I mean the blood on your sleeve. Was Great Hero Jin badly injured?”

The guard’s follow-up question never reached Mungyeong’s ears.

Mungyeong silently looked down at his bloodstained sleeve and muttered.

“The basics…?”

“Hmm?”

“Oh, it’s nothing. Young Master Jin is unharmed, so don’t worry.”

“Ah. Right. I understand.”

Leaving the martial artist behind with an uneasy expression, Mungyeong walked away.

Several faces had grown familiar enough to speak to him and acknowledge him as they passed, but the young medical apprentice’s mind held only one person.

*Jin Taekyung. Jin Taekyung…*

He had thought it impossible.

And yet that boy had really managed to evade the final sword stroke.

The results Mungyeong had obtained from the tests over the past several days and today were beyond his expectations.

No. They were beyond his imagination.

*So something like this is possible.*

Everything Mungyeong had told Jin Taekyung had been true.

He had once had people who could properly be called Disciples, and every one of them had possessed the “basics.”

But there was one truth he had not mentioned there: the time it took to acquire them.

*The fastest one to pass had taken a little over a year, I think.*

But Jin Taekyung had done it.

In only seven days and nights.

It was a speed that no one else could match.

Mungyeong did not know whether it was because of his Heavenly Martial Physique or because he was a Supreme Peak master, but Jin Taekyung had something special in his own right.

“Even so… I never thought he would be this good.”

Mungyeong murmured so quietly that no one could hear him, then rolled up his sleeve.

As the skin cut by something sharp and the beads of blood gathered on it came into view, a thought suddenly crossed his mind.

*Now I understand how the Fire King feels.*

But Mungyeong did not realize that a faint smile had formed at the corner of his mouth.

[^1]: Teacher’s Day is a Korean holiday observed on May 15 to honor teachers.

[^2]: *Salcheonmun* is the name of the now-vanished assassin sect; it literally means “Slaughter Heaven Sect.”
## Chapter artifact 498

# Chapter 498

The moment I woke from my long sleep and came to my senses, a thought suddenly flashed through my mind.

*Could I still be poisoned?*

My entire field of vision was pitch-black.

But the faint anxiety quickly faded. After confirming the moon casting a dim light across the ink-black sky, I muttered in a hoarse voice.

“Shit, you could’ve woken me before leaving.”

I had thought it was because of the Blindness Powder, but it was simply dark outside.

A considerable amount of time seemed to have passed while I was unconscious. I had been sprawled out on my back, staring blankly at the sky, before slowly pushing myself upright.

*What the hell happened?*

I had moved almost entirely unconsciously, and since I’d passed out while poisoned by the Blindness Powder, I hadn’t seen what happened at the time. I felt my dirt-covered body all over.

*I must have blocked it somehow. Otherwise, I’d have more injuries.*

I could guess the result, but the process was difficult to imagine. How had I moved? Even when I desperately tried to recall the sensations from that moment, everything remained hazy, like a fog.

Instead, I learned one thing for certain.

Beep.

> **System**
>
> - Mission: Earn Mungyeong’s Recognition (Complete)
>
> - The Sudden Quest, Fake Murim Martial Artist, has been successfully completed!
>
> - The Quest completion Reward has been issued!
>
> - You have gained a considerable amount of EXP!
>
> - You have gained 10 points!
>
> - You have achieved the Outstanding Achievement, Deadly Poison Sommelier!
>
> - You have tasted and detoxified more than ten types of specially manufactured deadly poison. We salute your sturdy body and Detoxification ability!
>
> - Poison Resistance increases significantly!
>
> - You have achieved the Amazing Achievement, Wow, You Survived That!
>
> - At the crossroads between life and death, you grasped a clue to a new enlightenment!
>
> - Qi Sense becomes sharper. Train to advance to an even higher realm!
>
> - The Follow-up Quest, Fake Murim Martial Artist—Stage 2, has been created!
>
> - The objective of the Follow-up Quest will be determined by Mungyeong’s future plans!
>
> - Agh!

“……”

*Like hell.*

As someone who had nearly crossed the Jordan River instead of Dongting Lake, I was furious.

*A Follow-up Quest.*

Even if I had expected something like this, I couldn’t help feeling worried. In Stage 1, I had been told to evade the Slaughter Saint’s sword stroke with my eyes closed. What kind of insane bullshit had they prepared for Stage 2?

The only consolation was that the rewards were pretty generous.

*At least putting my body through hell had been worth something.*

Although I hadn’t leveled up, I had gained a considerable amount of EXP and recovered the points I had lost after being poisoned by Seven-Step Soul-Chasing Powder.

And…

*Which asshole came up with those Achievement titles?*

Deadly Poison Sommelier and Wow, You Survived That.

Despite their deeply unpleasant names, the two Achievements I had earned this time were actually quite valuable.

The Poison Resistance I had gained from the first one was obviously appreciated. The second one might seem a little vague for now, but it was a tremendous gift.

*A clue to enlightenment.*

For someone like me, who had recently begun to feel a wall in front of him, there was no more welcome news.

Of course, if I said that after growing at breakneck speed by learning the Fire Gate Clan’s Supreme Peak martial arts and stuffing my face with elixirs every quarter, I’d be liable to be treated as an enemy of the Murim.

*But a wall is still a wall.*

If you asked a martial artist stuck in the Second Rate or Third Rate realms what they needed, nine out of ten would say martial arts manuals and elixirs.

But the answer given by masters who had reached the Peak realm or higher was different.

*Enlightenment.*

Ten years. Twenty years. Even if they waited longer than that, enlightenment was something that did not come easily.

No matter how outstanding the martial arts they learned or how many elixirs they consumed, there was a limit to how far they could advance.

If stuffing yourself with elixirs could make you a Supreme Peak master and return you to youth, who would bother shedding blood and sweat in training?

They couldn’t overcome the wall because of their clear limitations, so they simply devoted themselves to training as though their lives depended on it.

According to what Gung Gibang had once told me, quite a few martial artists even took opium in an attempt to broaden the realm of their minds and gain enlightenment.

When I asked why anyone would do something so stupid, the answer I got was simple.

*They know, too. They know they’ll become addicted to opium if they keep going like this.*

*Then why do they do it?*

*Because they’re martial artists.*

It was a short answer, but it explained everything.

Martial artists were creatures like that. They were the sort of people who would do anything if it meant becoming stronger. They were more intoxicated by martial arts than by opium, and they had become addicted to power.

And I wasn’t all that different.

*I want to become stronger. Stronger still.*

Even now, when I possessed more than I ever could have imagined in the past, I felt the same way.

There was one decisive difference between me and other martial artists, though.

I wasn’t trying to become stronger so I could obtain something. I wanted to become stronger so I could protect something.

*If I were satisfied with the present, I never would have accepted Mungyeong’s training.*

In that sense, obtaining a clue to enlightenment was an enormous achievement.

There was only one small problem…

*Doctor, I don’t remember anything.*

I didn’t even know exactly what I had done.

Damn it.

No, seriously. How had I done it? I seemed to have barely dodged the attack, but I had no idea what happened afterward.

*Maybe I’ll understand if I keep training.*

I tried to recall the sensations from that moment, but for now, it was only as futile as wandering through a fog.

I let out a long sigh and stood up, brushing the dirt from my clothes.

That was when it happened.

Ssshhk—boom!

Far away, a streak of blue flame shot up into the darkened sky and exploded spectacularly.

*A signal firework?*

Wondering what was going on, I quickly left the training area and encountered the martial artists standing guard.

“What’s going on?”

“Oh, Great Hero Jin. You’re finally out.”

The Beggars’ Sect disciple, clearly belonging to the Hubei branch from his ragged, patched clothes and the two knots hanging from his waist, shrugged and continued.

“Judging by the blue color, it’s a visitor. We’d already heard they were coming, but they’re later than expected.”

“A visitor?”

This wasn’t exactly a tourist attraction.

Since the place was being treated as highly classified, I couldn’t immediately think of anyone who might come here. At most, there were the three sects gathered here and the authorities.

If it were reinforcements, there would be no reason to call them visitors.

“Where are they from? The Zhuge Clan? Or Wudang? Ah, did their Sect Leader finally come?”

“Excuse me?”

The Beggars’ Sect disciple and the other martial artists stared at me as if they had never seen such a strange person before.

“Uh, well. You haven’t heard?”

“Heard what?”

“About the visitor who’s on the way.”

“What does that mean…? Are they people I know?”

The Beggars’ Sect disciple nodded at my question.

“Yes. They’re from the Jin Family of Taiyuan.”

“……Huh?”

From where?

* * *

Splash! Splash-splash!

Disciplined footsteps crossed the moonlit river and left fresh tracks in the sand.

When more than fifty martial artists moved as one and formed lines on either side, a man walking slowly between them spotted me and came to a stop.

“It’s been a long time.”

His eyes were just as sharp as ever, and he had even more scars than before.

I let out a quiet laugh at the familiar face I was seeing for the first time in a year.

“Your face has gotten even more intimidating. At this point, shouldn’t you be called Ghost Face instead of Ghost Sword?”

“There were more than a few bastards who needed dealing with. As our family’s reach has expanded, all sorts of people have crawled out of the woodwork.”

“Just tell me who they are. I’ll take care of them.”

“There’s no need. They’ve already left for a place beyond anyone’s reach. And…”

His narrowed eyes held laughter, while his next words were filled with emotion and joy.

“There’s no need for the Divine Dragon to deal with mere cows and pigs.”

Ghost Sword Wipeng—the right-hand man of Jin Wikyung and the man who had once been assigned to straighten me out—performed a deep martial salute toward me.

“Wipeng, Commander of the Jin Dragon Squad of the great Jin Family of Taiyuan, greets the Third Young Master.”

“Greetings, Third Young Master!”

The tremendous shout shattered the silence of the deep night.

Powerful energy radiated from the bodies of the martial artists standing in lines like iron towers on either side. They were just like the two characters embroidered across every one of their chests: Jin Dragon.

*Wow. When did the Jin Family of Taiyuan get this big?*

It felt like only yesterday that we had been putting our heads together and muttering that we were fucked because we had nowhere near enough First Rate masters for the war against the Mount Heng Sword Sect.

Yet just looking at the Jin Dragon Squad gathered here, the weakest among them was at least a First Rate master.

*I feel high just looking at them. So high.*

The Jin Family of Taiyuan had been slowly declining due to the Family Head’s long absence, a severe shortage of personnel, and a Third Young Master who preferred pleasure houses to his own home, among other problems.

Seeing it rise so dramatically made my chest swell with pride.

*Is this why people build families?*

I was gazing contentedly at Wipeng and the Jin Dragon Squad when a voice from behind him ruined the mood.

“Hey, damn it! You startled me. Why are you all shouting in the middle of the night? What would you do if an old man with a weak heart like me got frightened and dropped dead?”

That didn’t seem very likely.

As I studied the man’s powerful muscles, which were impossible to believe belonged to an old man, I finally succeeded in dredging up an old memory.

“Always do Taebo?”[^1]

[^1]: A Korean internet catchphrase urging people to do Tae Bo; here it puns on Jang Taebo’s name.

The expression of Jang Taebo, former Guild Leader of the Ironcraft Guild, twisted in outrage.

“Look at the manners on this guy. Am I your friend?”

Although I had built up an incredible reputation in the short span of a year, it seemed to mean nothing to Jang Taebo, a master craftsman who never hit the brakes.

Maybe because of that, I felt even more fond of him and happier to see him.

Besides, the White Flame he had forged with everything he had put into it had saved my life several times.

“Elder, what brings you here?”

The answer to my question came from somewhere other than Jang Taebo’s mouth.

“I specifically asked him to come.”

The people who had hurried over after hearing that the Jin Family of Taiyuan had arrived murmured among themselves and parted to either side.

As a man approached through the human curtain, an even louder cry rang out than before.

“Wipeng, Commander of the Jin Dragon Squad of the great Jin Family of Taiyuan, pays his respects to his lord.”

“Loyalty!”

“That’s enough.”

Under different circumstances, I would have grabbed Wipeng’s hand and danced a waltz with him, but countless eyes were watching us.

Jin Wikyung waved a hand with a solemn, dignified expression, then continued in his deep, weighty voice.

“Commander of the Jin Dragon Squad. And Old Master Jang. You’ve both had a difficult journey.”

“Not at all, my lord.”

“This old man is nothing to concern yourself with, Lesser Family Head.”

Wipeng was obviously a trusted retainer, but even Jang Taebo, who called me this brat and that bastard, was unfailingly respectful toward Jin Wikyung.

He had said he retired a long time ago. Had he taken on some subcontracting work for the Jin Family while I was away?

Ignoring my question, Jin Wikyung spoke again.

“The journey must have been tiring. Let’s all move somewhere else first.”

It wasn’t difficult to realize that I was included in that “all.”

It was equally obvious that the man running toward us over there, panting heavily, was not.

“Hyuk Mujin, Vice Commander of the Jin Dragon Squad! I have just completed my guard duty and returned!”

“……”

Some guard duty.

If you’re going to lie, wipe the sleep from your eyes first, you bastard.
## Chapter artifact 499

# Chapter 499

The season was already well into spring, but the night wind blowing along Dongting Lake’s winding waterways was chilly.

The first thing Jang Taebo did after entering Jin Wikyung’s tent, which had been erected with thick cloth, was claim the spot in front of the brazier and sit down to warm himself.

“Whew. I’m finally starting to feel alive.”

Seeing this, Jin Wikyung smiled and handed him a teacup.

“You must have had a difficult journey getting here.”

“I happened to be in Henan, thankfully. If I’d been in Shanxi, I wouldn’t have come even if the Lesser Family Head himself had asked me. How dare you work an old man who’s only waiting for the day he dies this hard?”

I looked at Jang Taebo’s threatening muscles and thought,

*Seems like he’s more than capable of being worked hard…*

Just look at that body. This went beyond staying fit—he was in fantastic shape. While everyone else was shaving years off their lives from overwork, the worst Jang Taebo suffered was muscle loss.

Perhaps thinking the same thing, Wipeng glanced sideways between his own forearm and Jang Taebo’s before speaking.

“I heard all about what happened in Sichuan and Hubei. I came in person, partly to resolve the matter in Henan while I was at it, and partly because I was worried something might happen. It seems I chose the right time.”

Jin Wikyung laughed heartily and patted Wipeng on the shoulder.

“Wipeng. You really are my Zhang Liang!”[^1]

“I’m a martial artist.”

“Oh, then I’ll go with Han Xin.”

“Han Xin was eventually purged.”

“Then Xiao He.”

“Xiao He was a civil official, too.”

“……”

Jin Wikyung stared at Wipeng with an expression that suggested he wanted to purge him immediately, then cleared his throat.

“Ahem. You seem to have been holding a lot in all this time.”

“Yes, I have. You didn’t know?”

“I knew perfectly well, but I didn’t expect you to come all the way here just to say it to my face.”

“I didn’t come here on my own. My lord summoned me. Do you realize you’ve been away from your post for nearly three months? Not long ago, even Sect Leader Lee came looking for you and asked whether something had happened to you.”

“Cough, cough!”

Judging by how Jin Wikyung kept clearing his throat, he clearly had plenty to feel guilty about.

Wait a second. The Sect Leader Wipeng had just mentioned couldn’t possibly be…

“Are you talking about Young Lady Lee—Lee Seowol?”

At my question, Wipeng shook his head.

“Not Young Lady. She is the bona fide Sect Leader of an established sect, Third Young Master.”

“Oh, right. She is.”

The Mount Heng Sword Sect, which had once aimed to become the dominant power in Shanxi Province, had suffered a devastating collapse after a series of incidents.

However, Lee Seowol, the only surviving blood relative of the Blood Wolf Sword, had survived with my help and sworn loyalty to the Jin Family of Taiyuan.

Even if she held the position of a vassal, a Sect Leader was still a Sect Leader.

*When was the last time I saw her…? More than a year ago already?*

It had been around the time I left the Jin Family of Taiyuan with Jeok Cheongang and headed for Mount Jiuhua. Even by the time that had passed in Murim, it had been a year. If I included the time that had passed in the modern world, it was even longer.

I could still clearly recall the day we parted.



*“Excuse me, Sect Leader Lee.”*

*“Young Lady.”*

*“Pardon?”*

*“Please call me Young Lady.”*

*“Ah, yes. Then, Young Lady Lee.”*

*“Go ahead, Young Master Jin.”*

*“May peace prevail throughout your household.”*

*“……”*

*“And may your sect’s affairs flourish in the future. Whatever it is, I hope everything you do goes well.”*



Hmm. I supposed we had parted on a fairly warm note.

The Lee Seowol I remembered was firm and resolute, as befitted the daughter of a martial family. She had not backed down even in front of Pung Yang, who had attacked with the Red Wind Band.

*The ruined Mount Heng Sword Sect must have grown quite a bit by now.*

“So, is Young Lady Lee doing well these days?”

Wipeng thought for a moment before answering.

“She is doing well, if you mean some things. In other respects, perhaps not.”

“Why? Is something going wrong?”

“If you’re asking about the sect, the Mount Heng Sword Sect has already completed its reconstruction. Under Sect Leader Lee’s command, it is growing rapidly, and the number of its disciples is increasing every day.”

“Oh.”

“Great Hero Cheol Mubaek, the Tiger of Mount Heng and a friend of her late father, has also ended his seclusion and is taking an active role in the affairs of the Mount Heng Sword Sect.”

“Ohh.”

Then everything was going well, wasn’t it?

At my puzzled expression, Wipeng’s eyes narrowed.

“Third Young Master. Forgive me for asking, but may I ask you one thing? Have you really not contacted her at all since then?”

“Contacted her? What kind of contact?”

“……Hah. Never mind. Pretend you didn’t hear that.”

Something about the atmosphere felt strange.

Seeing Jang Taebo clicking his tongue beside me, a thought suddenly crossed my mind.

*No way.*

*Come on. It couldn’t be.*

*But what if…?*

*No. That isn’t it.*

Jin Wikyung rescued me from my sudden confusion with a single remark.

“It’s a relief to hear that Sect Leader Lee is doing well. By the way, what is the second doing these days? I haven’t seen him in months.”

Wipeng looked at me as though I were a pill bug before speaking with a sigh.

“He remains the same. He eats only the fasting pills prepared in the training hall and hasn’t taken a single step outside.”

“Mukyung, that idiot. What in the world is he planning…?”

Jin Wikyung’s concern was not unfounded.

Before I left for Mount Jiuhua, Jin Mukyung had lost a duel against Cheongpung. From that day onward, he had shut himself away in the training hall and refused to show himself.

A full year had passed. The Star-Array Grand Banquet had been held, and Dark Heaven’s shadow now hung over the Murim, yet he was still secluded.

*He said he wouldn’t come out until he achieved something great.*

There was a time when all of Murim called Jin Mukyung a genius the ages had rarely seen.

Even the direct disciples of the Nine Sects and One Gang, who were generously supported with excellent martial arts and elixirs, could not compare to him. Jin Mukyung had overcome the limitations of being descended from a fallen borderland martial family and risen to the forefront of the Ten Dragons and Phoenixes through martial arts alone.

*And then he met Cheongpung.*

For Jin Mukyung, Cheongpung’s existence must have been an enormous shock and an equally enormous stimulus.

The fact that he was still continuing his secluded training more than a year later was proof enough.

*He’s definitely the sort of person who will accomplish something. No doubt about it.*

The Jin Mukyung I knew was an undeniable genius.

He had not been given the Sword Saint’s instruction, nor had he received outstanding elixirs and secret martial arts.

Even so, he had reached this point through his own strength. I couldn’t easily imagine what he would look like when he finally broke his seclusion.

*The question is, when is he actually coming out?*

He wasn’t going to emerge when he was nearly sixty, was he?

If he managed to survive on nothing but fasting pills until then, I would genuinely respect him and treat him as my hyung.

The fact that he had continued his secluded training for an entire year while eating that tasteless crap was already impressive enough.

Even Wudang Daoists brought jerky instead of fasting pills when they practiced wall-facing meditation. What did that tell you?

*Even militant vegetarians who flipped over the grill at a barbecue would start looking for pork belly after chewing on a fasting pill once.*

While I was thinking that, the subject of the conversation had shifted to Jang Taebo.

“By the way, Lesser Family Head, will you tell me why you summoned this old man here?”

In response to Jang Taebo’s grumbling question, Jin Wikyung abruptly tossed out a single phrase.

“Ironcraft Hall. What do you think?”

“I’ve never heard of an organization like that within the Jin Family of Taiyuan.”

“You wouldn’t have. It was established only a few days ago.”

Jang Taebo’s brow furrowed.

“It’s a strangely familiar name. It reminds me of the Ironcraft Guild, where this old man once worked.”

“I named it with Old Master Jang in mind. Master of Ironcraft Hall. Doesn’t it sound good?”

“Lesser Family Head.”

Jang Taebo sighed before continuing.

“I left the Ironcraft Guild a long time ago.”

“Then it seems it’s time for you to return.”

“I’m old and tired. I don’t even have the strength to lift a hammer.”

Jin Wikyung stared meaningfully at Jang Taebo’s threatening muscles, then moved his lips.

—Youngest.

At this point, there was no way I could fail to understand why Jin Wikyung had summoned Jang Taebo all the way here.

I had already realized what my eldest brother was planning, so I lightly tapped the White Flame strapped to my back and knocked it loose.

Clang!

“Oh, no! I dropped a masterwork weapon made by a blacksmith who’s too old and tired to lift even a hammer!”

“……”

“Made from Ten-Thousand-Year Cold Iron, too. Supposedly incredibly difficult to work with. I wonder who could have made my spear…”

Jang Taebo glared at me with murderous eyes.

“Enough.”

“Why? I wasn’t talking about you, Elder.”

“Who else made it?”

“What are you talking about? How could someone without the strength to lift a hammer make something like this?”

“……Hoo. That damned brat.”

Jang Taebo sighed as though the ground itself had collapsed, then looked at Jin Wikyung.

“Was this why you gave me all sorts of help over the past few months?”

“Of course not. It was merely an expression of goodwill toward the artisan who made a masterwork weapon for my beloved youngest brother.”

“Then I’ll give you my answer.”

“I’m listening.”

“No. That is the only answer this old man can give you. Even with a knife at my throat, it won’t change.”

I shot my hand into the air.

“What about the spear?”

“Shut up before I take it back and snap it.”

“Ten-Thousand-Year Cold Iron. Special feature: fucking hard.”

“……Why did I make a spear for a bastard like you? What riches and glory was I hoping to gain?”

“You should just become the Master of Ironcraft Hall. I heard you’ve received all sorts of help from our side.”

“I’ll repay you with money. Do you think I’m going to put myself through that kind of hell again at my age?”

“Ah, seriously? You really won’t do it?”

“Then what are you going to do? I said I wouldn’t.”

“Then just tell me your conditions. I’ll meet as many of them as I can.”

“Conditions?”

A triumphant smile suddenly appeared at the corner of Jang Taebo’s mouth.

“Do you remember this time last year? I’ll set the same conditions as I did then.”

“If you mean the conditions you set back then, surely you don’t mean…”

“The Herb of Eternal Youth, gongcheong seokyu, a dragon’s claw, or a dragon pearl. Bring me any one of them.”

Beep.



> **System**
>
> - A Sudden Quest, **No Way You Can Do It Anyway**, has been created!
>
> - Quest Objective: Obtain at least one of the items Jang Taebo named.



Clang! Crash!

I sprang to my feet and shouted.

“Wait, where are you supposed to find things like that? And you’re asking for a dragon, not even an imugi!”

“Whether it’s an imugi or a dragon, bring me one first. Then I’ll bury my bones in the Jin Family of Taiyuan. If you can’t do it, just stay quiet.”

Beep.



> **System**
>
> - Quest details have been changed.
>
> - Quest Objective: Obtain an imugi’s claw.



After checking the changed System window, I nodded.

“Oh, there we go. Here.”

“My mind hasn’t changed, so don’t waste your effort—what are you suddenly giving me?”

“An imugi’s claw.”

“Huh?”

“An imugi’s claw. You told me to bring you one.”

“……What?”

A tremor ran through Jang Taebo’s pupils.

He was a Master Artisan ranked among the three greatest in the world, and he had once served as the Guild Leader of the Ironcraft Guild, the finest blacksmith organization under Heaven.

As Jang Taebo stared at the imugi’s claw, disbelief and horror at an unfamiliar material mingled in his eyes.

“An imugi’s claw? Is it real?”

“Just look at its length. Obviously it isn’t my claw.”

“No, I mean, where in the world did you…”

“I caught it.”

“What?”

“There are bones and scales, too.”

“That’s impossible!”

“Come take a look yourself after sunrise. Great Hero Wipeng has only heard about it through a letter, too, so you can go together.”

Beep.



> **System**
>
> - The Sudden Quest, **No Way You Can Do It Anyway**, has been successfully completed!
>
> - As a Quest Reward, the **Jin Family of Taiyuan** has acquired **Jang Taebo**!
>
> - Achievement unlocked: **Wow, You Found It!**



Along with the cheerful System notification, Jin Wikyung warmly put an arm around Jang Taebo’s shoulder.

“I look forward to working with you from now on, Master of Ironcraft Hall.”

“……!”

Jang Taebo’s eyes were utterly vacant as he was recruited as the Jin Family of Taiyuan’s personal Dobby—no, slave.

[^1]: Zhang Liang, Han Xin, and Xiao He were three of Liu Bang’s founding ministers. Zhang Liang and Xiao He were civil officials and strategists, while Han Xin was a military commander.

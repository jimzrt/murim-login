# Checkpoint Review — 220–224

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

# Chapters 220–224

## Plot

Jin Taekyung remains behind after ordering Won Myunghoon and the Star Guild away from the approaching Black Wyvern. Team Leader Choi, Butler Kim, Im Kkeokjeong, and Song Song stay with him; Butler Kim prepares layered barriers. Song Song rejects Taekyung’s confession but accepts him as a same-age friend and guildmate, agreeing to drink soju with him afterward.

The Black Wyvern arrives as a more-than-fifty-meter Named Monster with one cloudy eye. Taekyung recognizes it as the creature that killed his former teammates at Sangdong Station three years earlier. He channels more than one jiazi of Scorching Yang Qi and manifests blue Spear Energy, piercing the Wyvern’s knee and eye and splitting one wing. The monster reveals that it is Carus, the One-Eyed, who grew stronger by consuming monsters and Magic Gems, then learned magic.

Carus uses Heal, Slow, Dark Binding, Magic Arrow, Binding Magic, and poison spells, but Taekyung’s new Unaffected by a Hundred Poisons nullifies the Paralysis Poison and Nerve Poison. Taekyung spends 100 Bonus Points on Strength and Stamina, survives Carus’s attacks, and kills the Level 115 Named Monster after Carus accepts his death. The System grants the Named Monster Defeated Achievement, records a perfect clear of The Black Wyvern’s Nest, and awards enormous EXP and Fame, including two displayed level-ups. The revenge connected to Sangdong Station is complete.

The exit Gate remains closed because the Gate’s separate boss monster survived and fled into the wilderness. Taekyung and Butler Kim return toward the entrance to recruit outside Hunters to process Carus’s enormous corpse. Butler Kim uses Fire Rain against a wandering Orc group. In the jungle, they find Won Myunghoon leading the Star Guild in an ambush.

Won intends to eliminate the surviving Peace Guild members and conceal the Star Guild’s involvement. He considers the guild members compromised accomplices and orders Kim Jonghun, who knows his secrets and acquired Yeti’s Necklace, bound as bait for the surviving Named Monster. Taekyung and Butler Kim confront the ambush. After Butler Kim heals his injured knee, Taekyung breaks Won’s arm, takes his spear, and punches him when Won declares that the Star Guild came to kill them all.

## Continuity

- Taekyung completed the Manifestation of Qi Achievement, gaining Spear Energy, Unaffected by a Hundred Poisons, two levels, and 100 Bonus Points; he spent the points equally on Strength and Stamina.
- Carus, the one-eyed Black Wyvern, was a speaking Level 115 Named Monster with powerful dragonkin-enhanced magic. Taekyung killed him after piercing his eye.
- The Black Wyvern’s Nest was perfectly cleared as an A-Rank Mutated Gate, but its exit remains closed because the original boss monster escaped and is hiding in the wilderness.
- The Named Monster Defeated Achievement granted an unspecified Reward. The final level and complete rewards from the clear remain undisclosed.
- Carus’s corpse is more than fifty meters long and contains valuable hide, bones, flesh, and scales. Processing it requires outside B-Rank or preferably A-Rank Hunters.
- Taekyung fears using the Inventory to remove Carus’s corpse because reporters are stationed at the Gate entrance and could expose him as a System user.
- Choi Minwoo, Butler Kim, Im Kkeokjeong, and Song Song witnessed Taekyung’s true strength and now understand that his previously observed abilities were only a fraction of it.
- Song Song accepted Taekyung as a same-age friend and guildmate despite rejecting his confession; they plan to drink soju after the crisis.
- Won Myunghoon is a thirty-nine-year-old A-Rank Hunter and Star Guild CEO. He has turned openly hostile toward Taekyung after Taekyung previously ordered him to flee.
- Won’s Star Guild ambushed the returning Peace Guild. Won broke no truce: he explicitly intends to kill the Peace survivors and conceal the Star Guild’s role in the raid.
- Kim Jonghun has succumbed to Fear and is regarded by Won as useless. Won ordered him bound as bait because Jonghun knows Won’s secrets and obtained Yeti’s Necklace.
- Taekyung has broken Won’s arm, disarmed him, and punched him; their confrontation is still unresolved.
- The surviving boss monster’s identity, location, and the conditions for opening the exit Gate remain unknown.
- The Conception Vessel and Governor Vessel rewards, the Gate Suppression Quest, Jin Mukyung’s return, Jeok Cheongang’s warning, the Martial God’s condition, and the Star-Array Grand Banquet remain unresolved.

## Translation Decisions

- Retain “The Black Wyvern’s Nest,” “Black Wyvern,” “Named Monster,” “A-Rank Mutated Gate,” “Carus,” “the One-Eyed,” “Yeti’s Necklace,” “Wind of the Snowfield,” “dragonkin,” and “Fear.”
- Render 기의 발현 as “Manifestation of Qi,” 백독불침 as “Unaffected by a Hundred Poisons,” 오러 as “Aura,” and 마정석 as “Magic Gem.”
- Render 힐 as “Heal,” 슬로우 as “Slow,” 다크 바인딩 as “Dark Binding,” 매직 애로우 as “Magic Arrow,” 속박 마법 as “Binding Magic,” 마비 독 as “Paralysis Poison,” 신경 독 as “Nerve Poison,” and 파이어 레인 as “Fire Rain.”
- Keep “boss monster” distinct from “Named Monster”: the former is the Gate’s original resident, while the latter is an uninvited intruder.
- Retain “hyung” for established fraternal addresses; render Taekyung’s familiar address to Im Kkeokjeong as “Uncle.”
- Render Won’s hostile register as “Mr. Won Myunghoon,” “ill-mannered bastard,” “losers,” “junk,” and “prey” where appropriate.
- Render 개보린 as “Dogvorin,” with a footnote explaining its dog-themed pun on Gevorin, a Korean painkiller.

## Durable state

{
  "active_continuity": [
    "Taekyung completed the Manifestation of Qi Achievement, unlocking Spear Energy and Unaffected by a Hundred Poisons; he later spent the resulting 100 Bonus Points on Strength and Stamina.",
    "Taekyung's Spear Energy and Scorching Yang Qi can penetrate high-level dragonkin defenses.",
    "Carus, the One-Eyed Black Wyvern, could speak and cast magic strengthened by his dragonkin trait; Taekyung killed him at Level 115.",
    "The Black Wyvern's Nest was perfectly cleared as an A-Rank Gate, granting Taekyung enormous EXP and Fame, two displayed level-ups, and the Named Monster Defeated Achievement.",
    "Taekyung remains publicly recognized as Jeok Cheongang's Disciple and heir to the Fire Gate Clan's orthodox lineage.",
    "Jin Mukyung remains secluded in the training hall and has not returned to Heaven's Gate Temple.",
    "The Jin Family received an invitation to the Star-Array Grand Banquet in Henan.",
    "Seong Jinho is staying at Taekyung's new family home after losing his housing deposit to Kim Jong-su.",
    "Taekyung is an A-Rank Hunter and nationally famous as the Tollgate Hero after the tollgate rescue and KPS interview.",
    "The Peace Guild House has extensive magical communication, observation, and alarm systems, and media intrusion exposed Taekyung's family's personal information.",
    "Won Myunghoon is a thirty-nine-year-old A-Rank Hunter, former ranker and celebrity entertainer, and CEO of the Star Guild; Taekyung declined Won's Guild and entertainment proposals.",
    "The joint Peace Guild-Star Guild raid was redirected to The Black Wyvern's Nest; Won killed the Green Wyvern alone, Taekyung received no EXP, and Won lent him Yeti's Necklace.",
    "Taekyung killed forty-seven B-Rank Orc Warriors alone, and Im Kkeokjeong was among survivors he had rescued during an earlier E-Rank Gate attack.",
    "Mutated Gates can contain monsters far above their expected Grade; Song Song rejected Taekyung's confession but accepted friendship and a guildmate relationship.",
    "The Peace Guild witnessed Taekyung kill Carus and now understands that his previously observed abilities represented only a fraction of his strength.",
    "Carus's corpse is more than fifty meters long and difficult to process; Taekyung fears using the Inventory to remove it because reporters are stationed at the Gate entrance.",
    "The exit Gate remains closed because the separate boss monster survived and fled; Taekyung and Butler Kim return toward the entrance to recruit outside personnel.",
    "Won Myunghoon stopped the returning Star Guild and ordered an ambush to kill any surviving Peace Guild members before their involvement could be exposed.",
    "Fear-stricken Kim Jonghun is considered useless as a Hunter by Won, who ordered him bound as bait because Jonghun knows Won's secrets and acquired Yeti's Necklace.",
    "Taekyung confronted Won at the ambush, broke his arm, disarmed him, and punched him after Won declared that the Star Guild had come to kill them all."
  ],
  "continuity_sources": [
    224,
    223
  ],
  "open_questions": [
    "What additional rewards came from the Conception and Governor Vessels Quest, the Conception Vessel Opening, and the Named Monster Defeated Achievement?",
    "Will Jin Mukyung return to Heaven's Gate Temple before the appointed deadline?",
    "What event does Jeok Cheongang believe may occur sooner than expected, and why must he endure for several more years?",
    "What is the true condition of the absent Martial God?",
    "Will Taekyung attend the Star-Array Grand Banquet, and what exactly was the answer that changed the three men's expressions?",
    "What are the Reward and Failure conditions of the Gate Suppression Quest?",
    "What is the identity and location of the surviving boss monster, and when will the exit Gate open?",
    "What will be the outcome of Taekyung's confrontation with Won Myunghoon after Taekyung breaks his arm and punches him?"
  ],
  "safe_through": 224,
  "temporary_decisions": [
    "Render 혈도 타통 as Acupoint Opening, 회음혈 as Huiyin Acupoint, and 임맥 타통 as Conception Vessel Opening.",
    "Render 성라대연 as Star-Array Grand Banquet, 노야 as Old Master when Taekyung addresses Jeok Cheongang privately, and retain hyung for established fraternal addresses.",
    "Render 고시원 as goshiwon, 오피스텔 as officetel, 오우거 as ogre, and 게이트 진압 as Gate Suppression.",
    "Render A급 헌터 as A-Rank Hunter, 아이튜브 as iTube, 태경좌 as Taekyung the Lord, 시벌좌 as Lord Fuck, and 라이칸스로프 as Lycanthrope.",
    "Render 와이번 as Wyvern, 그린 와이번 as Green Wyvern, 오러 as Aura, 만티코어의 밀림 as Manticore's Jungle, 예티의 목걸이 as Yeti's Necklace, and 설원의 바람 as Wind of the Snowfield.",
    "Render 변이 게이트 as Mutated Gate, 네임드 몬스터 as Named Monster, 레어 몬스터 as Rare Monster, 피어 as Fear, 힘껏 찌르기 as Stab with All My Strength, and retain Magic Gem for 마정석.",
    "Render 기의 발현 as Manifestation of Qi, 백독불침 as Unaffected by a Hundred Poisons, 에어 브레스 as Air Breath, 힐 as Heal, 슬로우 as Slow, 다크 바인딩 as Dark Binding, 매직 애로우 as Magic Arrow, 카루스 as Carus, 파이어 레인 as Fire Rain, and retain Taekyung's 아저씨 for Im Kkeokjeong as Uncle.",
    "Render 개보린 as Dogvorin and explain the Gevorin painkiller pun in a footnote."
  ],
  "version": 1
}

## Reading copies

## Chapter artifact 220

# Chapter 220

Won Myunghoon left. The memory of him grinding his teeth at my attitude while still hesitating to attack made a short laugh escape me.

*If he had, I would’ve made him regret it.*

He was a hyena of a man.

When his opponent showed weakness, he bared his teeth. When they showed strength, he hid them.

Looking back over everything he had shown me so far, the incident eight years ago had probably not been unrelated to his nature.

*You should consider yourself lucky.*

No matter how much a hyena leaped or crawled, it was still a beast.

If it knew how to tuck its tail, all you had to do was scare it away.

There was no reason—or desire—to get blood on my hands before it sank its teeth into my shoulder. Especially not before I had to face a real monster rather than some beast.

—Kyaaaaaaaah!

The black dot drew closer.

A roar filled with rage echoed from the edge of the horizon.

Just as I had recognized it, it had recognized me.

*Yes. You remember me too.*

That was enough. I was about to face a half-mad Named Monster, but I felt neither fear nor excitement.

There was only one thing bothering me, like a thorn caught in my throat.

“Why didn’t you leave?”

Team Leader Choi stared at me with his arms loosely folded.

His answer, however, came in the form of another question.

“Who are you asking?”

“Everyone.”

I glanced around. Four people stood against the backdrop of the endless wasteland, with scattered rocks and trees stretching behind them.

Team Leader Choi and Butler Kim. Im Kkeokjeong and Song Song.

Not one of them had left.

“You all know that thing coming this way is a Named Monster, right?”

“We’re all well aware.”

“Then this should be simple. It’s dangerous, so leave while you still can.”

“Where would we retreat to?”

“Where else? The exit we came in through.”

“The Star Guild isn’t exactly a great partner to flee with. Especially if we’ve already fallen out with their Guild Master.”

*I don’t see it that way.*

It wasn’t known yet, but Butler Kim was an A-Rank mage. He had even experienced the unprecedented war known as the Great Cataclysm firsthand.

The Star Guild had more people, but even without me, the Peace Guild wouldn’t be outmatched if they fought Won Myunghoon’s Guild right now.

“That’s a good excuse.”

Team Leader Choi stared at me as I smiled.

“Mr. Jin Taekyung.”

“No.”

I cut him off before he could say anything, but Team Leader Choi was not the sort of person to quietly back down.

“Since I’m trapped with no way to go anywhere because of you, I think I have the right to ask a few questions.”

*Damn. He has a point.*

I answered reluctantly.

“Fine…but keep it short.”

“The monster coming this way—is it connected to what happened three years ago?”

I hesitated before nodding.

“You’re not going to retreat.”

“…”

Silence was as good as an affirmative answer.

Team Leader Choi let out a low sigh.

“Mr. Jin Taekyung, you’re facing a Named Monster.”

“That’s the first I’ve heard of it. All I see is something I need to kill.”

“This is something you need to think about rationally.”

“Do I look that unstable to you right now?”

“That’s…”

Team Leader Choi closed his mouth.

I was calmer now than I had ever been. Unlike my heart, which was pounding like mad, my mind was coming up with countless ways to deal with the creature.

“Team Leader Choi.”

“…?”

“I’ve mentioned my life motto a few times before, haven’t I?”

Im Kkeokjeong, who had been silently watching us, answered in his place.

“Long and thin.”

“You remember that too, Uncle?”

“You were a strange kid. A young man ought to have at least one big dream…but you never did.”

“I’ve never liked a life with too many twists and turns.”

This time, Butler Kim answered with a smile.

“For someone like that, you seem to have come a very long way.”

“That’s why I changed it.”

“Long and broad. Is that right?”

“Yes. It’s too late for me to live a thin life now. Since things have turned out this way, I’m going to live as large and as long as possible.”

“Good. If you wish, perhaps…”

I knew what he was about to say.

I quietly shook my head. Butler Kim was someone who needed to take on a far more important task.

“I’m fine. Protect the others.”

“Understood. Even if you hadn’t said anything, I would have done what I should. I’ll give it my best.”

At Butler Kim’s clear-cut answer, Song Song asked with an incredulous expression,

“You’re telling him to fight a Named Monster alone? Are you all out of your minds? One wrong move and we’ll all die!”

“And why haven’t you left, Miss Song?”

“…That’s true. Why am I still here?”

I watched her sink into deep thought before suddenly opening my mouth.

“Miss Song.”

“No.”

“Absolutely not.”

“Hunter Jin Taekyung, please.”

What was with these reactions?

I had only just gotten the first word out, but after Song Song, Team Leader Choi and Butler Kim had stepped in and cut me off without hesitation.

“Taekyung, go for it.”

At least Kkeokjeong hyung was on my side.

I looked at the other three with an aggrieved expression.

“I haven’t even said anything yet.”

Song Song answered,

“That’s why I’m saying no.”

“How do you even know what I was going to say?”

“Hmm. A confession?”

My head went numb for a moment.

The back of my skull throbbed as if someone had struck it with a hammer.

“Wait. How did you know?”

“Good grief. How could I not know?”

“D-did it show that much?”

“Yes. Very much.”

“Then…”

She shook her head without hesitation.

“I’m sorry. I’m not the sort of person who flips her attitude at the drop of a hat because of money or fame.”

“Oh.”

“To be honest, you’d be quite a catch, Mr. Taekyung. But when I like someone, I’m the type to reel him in right away. I can’t string a bunch of men along.”

After saying everything she wanted without restraint, she blinked.

“Ah, I didn’t say anything too harsh to someone who’s about to fight a Named Monster, did I?”

I had been opening and closing my mouth like a goldfish, but soon I let out a short laugh.

“Why are you laughing?”

“Nothing. I just thought you were refreshingly straightforward.”

At my answer, she narrowed her eyes.

“Hold on. Why are you suddenly speaking casually?”

“You said you’re twenty-seven, right? We’re the same age, so being friends should be fine, shouldn’t it?”

“Hmm. There’s no such thing as friendship between a man and a woman.”

“We’ll think about that if it ever comes to that.”

I added one more thing to the hesitant Song Song.

“We’re guildmates, after all.”

“…When you put it that way, I can’t exactly refuse.”

I grinned at her.

In the end, I had been rejected cleanly, but I didn’t regret it in the slightest. In a way, I felt strangely calm.

If someone saw me like this and asked whether I had really liked Song Song, the answer would be yes. That was an undeniable fact.

But even I couldn’t give a definite answer about what I was feeling now.

I had simply said the words I had kept in my heart for a long time, and regardless of her answer, I felt relieved.

Maybe that was enough for now.

“Let’s have some soju when this is over.”

“My family motto is that boys and girls over seven shouldn’t sit together.”

“All together.”

“…Oh. Yeah.”

I turned around with light steps.

At the same time, I felt an enormous flow of mana behind me. I hadn’t seen it directly, but I could tell that Butler Kim was layering magical barriers one after another.

*I’m counting on you.*

That meant the battle was about to begin. Sure enough, the creature that had been no more than a tiny dot had drawn close enough for even an ordinary person to see it clearly.

“Kid, you’ve grown a lot.”

Its body easily exceeded fifty meters, and its wings were even larger.

Black scales covered its entire body without leaving a gap, flashing in the light of the setting sun.

It had grown at least two or three times larger than when I had last seen it three years ago.

*Was that even possible?*

I had never heard of anything like this.

But there was no mistaking it. Its cloudy eye was proof.

Its other eye, stained red, stared directly at me.

—Kraaaaaaaah!

Whoooosh!

A single roar sent a tremendous wind crashing down upon us. Dirt and pebbles scattered throughout the wasteland rose into the air in thick clouds.

When the curtain of dust settled, I saw a massive shadow standing tall on a hill not far away.

*It’s big.*

And strong.

With my senses fully open, I could feel its rage and power.

A monster that had broken beyond the boundaries of A-Rank.

It possessed the majesty befitting a Named Monster.

“So we finally meet.”

When I finally stood face-to-face with it, my chest trembled. Three years ago, I had lost my comrades, and it had lost one of its eyes.

What a tenacious grudge.

It had to end now.

I gripped the cold spear shaft tightly and began walking slowly toward it.

“Long time no see. Do you remember me?”

A Wyvern was undoubtedly a higher life-form.

It had already been cunning and cruel in the past, so now that it had become a Named Monster, it naturally possessed even greater strength and Intelligence.

—Grrrrr…

“Looks like you remember me. So, how’s your eye?”

A searing red flame rose from its one remaining eye. I let out a short laugh as I watched its scales bristle across its entire body.

“You fucking bastard. Where do you get off hissing at me?”

—Grrrk!

One step.

Then another.

My heart pounded, and my mind spun at full speed. Hundreds of paths through which I could hack apart its body and cut off its breath unfolded before my eyes.

“There were some names I wanted to tell you when I saw you again. Open your ears and listen carefully.”

Step.

Step.

As the distance between us gradually narrowed, something hot surged up from my lower abdomen.

It was like a small sun—both Scorching Yang Qi that had surpassed one jiazi[^1] and rage that had accumulated until it solidified.

[^1]: A *jiazi* is a traditional sixty-year cycle.

“Kim Hyunsu.”

The face of a bespectacled nerd appeared before my eyes.

He had been a Hunter for only four months. He was the first victim. The tail that creature swung had crushed his entire body.

He had been slow on his feet, but full of enthusiasm. Whenever he had a spare moment, he would come find me and ask questions.

*Deputy Team Leader. How do I do this?*

*Deputy Team Leader. I don’t understand this part.*

*Deputy Team Leader…*

Sometimes, I thought about him.

I wondered whether he might have survived if I had explained things more thoroughly back then, if I hadn’t been annoyed by him asking me dozens of questions every day.

But regret was always too late. Kim Hyunsu’s life had stopped at twenty, and the parents who had lost their only son had wailed throughout the funeral.

*Maybe even now, three years later.*

There were nine more people like him.

Every one of them had a family and dreams of their own.

“Lee Hyerim. Song Donghyeok, Park Sangho, Kim Haneung, Park Gwanghyeon…”

With each name came one step, and with each step, memories of that person rose like heat haze.

My vision blurred because of that.

That was what I chose to believe.

After ten steps, only one name remained.

“…And Hong Cheonsu.”

The round face of a man in his thirties flashed before my eyes.

When I first met him, I was a rookie Hunter who had just turned twenty, while he was a ten-year veteran.

After he saved me from being surrounded and nearly killed by goblins, I started calling him hyung.

One ordinary day, I suddenly asked him a question.

*Why are you always so good to me?*

He answered,

*It kept eating at me, seeing a kid like you struggle. My youngest sibling is about your age.*

I learned on the day of his funeral that he had grown up in an orphanage with no relatives at all.

I laughed because the whole thing was absurd. Then I ended up crying.

I remembered the last words he had left behind.

*You cocky bastard. Taekyung, go on ahead.*

He—Cheonsu hyung—died like that.

Leaving behind a wonderful spouse and three children.

And now, at this very moment, I stood before that creature. I opened my mouth while glaring at its enormous red eye.

“Listen carefully, you fucking lizard bastard.”

I had overcome countless crises for the sake of saying those words.

After three years and ninety-two days, I was finally ready to tear off those wings and drive my spear into its heart.

“This time, I’m not going anywhere.”

Internal energy surged from my dantian and spread through every limb and bone in my body.

The Scorching Yang Qi raced forward without restraint, converging on the cold spearhead. The internal energy that linked continuously and tangled together like a skein of thread transformed into a new shape.

Crackle, crackle, crackle!

Aura, Spear Energy.

It didn’t matter what I called it. I leveled the blue-burning spearhead at the creature.

“You’re…dead today.”
## Chapter artifact 221

# Chapter 221

Ding.

> **System**
> 
> You have achieved the Achievement **Manifestation of Qi**!
>
> This is truly an outstanding achievement! An Achievement reward will be granted!
>
> **Spear Energy** is now available!
>
> The effect of **Unaffected by a Hundred Poisons** has taken root in your body!
>
> You have acquired a large amount of EXP!
>
> **Level Up!**
>
> **Level Up!**
>
> You have acquired 100 additional Bonus Points!

The System notifications echoed in my ears like a ringing bell. But my gaze remained fixed solely on the spear.

Ssssss.

Blue flames flickered over the spearhead. A thrilling shiver surged up my spine.

*I did it.*

Today, I had taken one step toward a higher realm and conquered one of the peaks of the perilous mountain known as martial arts.

At the same time, I became certain.

*I can kill it.*

No further thoughts or words were necessary. All that remained was the action that would turn years of waiting into reality.

But I wasn’t the only one waiting for this moving reunion.

The creature with its single eye wide open let out a roar filled with fury.

—Kraaaaaaaah!

No, it was closer to a thunderous boom than a roar.

Gooooooom—

The tremendous air pressure pouring from a maw large enough to swallow a car whole crushed down upon the ground. Compressed air burst around me, and it felt as if a thousand-geun boulder were pressing down on my shoulders.

*Air Breath.*

One branch of a unique ability granted only to dragonkin.

Since a Named Monster was using it, even a capable Hunter would have had their eardrums burst and been forced to their knees.

But not me.

Crack. Grrrk.

I continued forward in silence, enduring the pressure crushing down on my shoulders.

With every step, my ankles sank into the ground, and the pressure grew stronger. But it couldn’t stop my advance.

Even if it was a being that had surpassed the limits of an ordinary monster, I wasn’t afraid.

*Because the same was true of me.*

At least when it came to physical ability, I was already worthy of being called superhuman.

Strength, speed, stamina. In everything that determined the outcome of battle, I stood one step ahead of a Peak master of equivalent level—or an A-Rank Hunter.

“Ahh, that’s refreshing.”

I raised my head with a broad grin.

Above the gigantic torso that rose like a skyscraper, the red eye of the creature spewing Air Breath wavered when it saw my smile.

“What was that just now? Your fan on high?”

—Kraaaaaaaah!

“Turn the fan off. You’re blowing yellow dust everywhere, you bastard!”

At the same time as I shouted, I swung the spear shaft toward the sky with all my strength.

Whoooooosh!

The instant the blue flame of qi carved a semicircle through the air, burning it, the pressure crushing down on my entire body vanished. My body became as light as a feather.

*Now!*

Boom!

With a single stomp, I shot forward like an arrow.

The confused creature twisted its head and unleashed another Air Breath, but it couldn’t keep up with my speed.

Whoosh! Rat-a-tat-tat!

Carrying nothing but light leather armor and a single spear, I crossed the battlefield like lightning and reached the creature’s front before I knew it.

—Grrrrrk?

The startled creature spread its folded wings wide. But by then, I had already leaped with all my strength.

Boom!

With a powerful tremor, I soared into the air. Through my hair streaming in the wind, I saw the creature’s knee beneath its flashing black scales.

The very area people called the cruciate ligament.

“You’re exempt from military service, you bastard!”

With that shout, I drove my spear in with all my strength.

Thrust! Shrrrk!

The Wyvern’s hide and scales, said to withstand ordinary magic and weapons alike, split open in an instant.

A sharp, satisfying jolt traveled through my fingertips, like the feeling of harpooning a fish.

*It went in!*

The blue-burning Spear Energy cut through and shattered everything in its path.

Once the spearhead had opened a gap, the rest was easy. As if hammering in a nail, I used my fist to drive the two-meter spear into the creature’s knee.

Boom! Fwoooosh!

Dark blood erupted like a fountain. The creature, which had just spread its wings and tried to take flight, dropped to its knees with a scream.

—Graaaaaaaah!

But I didn’t stop there. I stepped on the end of the spear shaft lodged in its knee and used its springiness to launch myself upward.

As I shot several more meters into the air, a dagger had appeared in my hand.

*If I don’t have one, I can just take one out.*

My real-world Inventory held countless weapons, not just the ones in the Murim.

I had spent a fortune buying them before, but if it meant killing this creature, I wouldn’t regret spending ten times that amount.

Thrust!

I suddenly remembered practicing the Wall Lizard Technique in the Murim. The cliff I had climbed back then had been even higher, and there had been hardly anything suitable to use as a foothold.

*Whenever I thought I’d climbed far enough, some lunatic would drop rocks on me.*

Compared to that, this was hardly difficult.

I repeatedly drove the dagger into the creature’s enormous body, soaring upward, higher and higher.

Thrust, thrust! Thrust-thrust-thrust!

Before Spear Energy, neither the hide harder than iron armor nor the scales that deflected low-level magic were of any use.

It was easy to imagine a palm-sized something crawling up your body and driving nails into you over and over.

That was exactly what was happening to the creature now.

—Kraaaaaaah!

Unable to endure the pain assailing it without end, the creature writhed with a roar. It was trying to shake me off, but it was too late.

By then, I was already enjoying the sensation of floating in midair.

*Open Inventory. Equip spear.*

The next moment, a solid spear shaft appeared in my empty hand.

The Scorching Yang Qi that had surpassed one jiazi when I opened my Conception and Governor Vessels surged toward the spearhead like an ebb tide.

Whoooooosh. Ssssss!

Blue flames wrapped tightly around the spearhead.

Flickering in the darkness, they were the tail of a meteor.

And I was the meteor itself.

“Where do you think you’re running?”

With that quiet murmur, I became one with the spear and plunged rapidly downward. My target was the creature’s wing, which served as both its foreleg and its arm.

Blinded by pain for a moment, the creature had no way to stop the meteor.

Fwoosh! Shraaaaaak!

Scorching Yang Qi, burning like a small sun, sliced through hide and scales and scorched the flesh beneath. The wing, with a vertical span of more than ten meters, split in two along the spearhead.

—Krrrk…!

It was probably the worst pain the creature had ever experienced. The red eye of the predator that had lived its entire life as a hunter flew wide open.

—Kraaaaaaaaaah!

I landed lightly on the ground and stared at it with a cold, steady gaze.

Within the thick cloud of dust rising around us, the creature’s fifty-meter bulk writhed.

“Does it hurt?”

—Kwak! Kraaaaaah!

“That little?”

Compared to what it had done three years ago, this was nothing.

A single flap of its wings had shattered entire bodies, and heads seized in its claws had vanished without a trace. Not even the corpses of those swallowed by its enormous maw could be found.

That was when I first learned that the human body held so much blood and so many organs.

That a person could die so brutally.

“You bastard. I wouldn’t feel satisfied even if I chewed you to death.”

An eye for an eye. A tooth for a tooth.

This creature would die here today, by my hand. And it had to die horribly—exactly as I had imagined countless times before.

“This is just the beginning. Quit whining and get up.”

Whoooosh.

The wind rising along the spearhead as I swung it drove away the dust.

The creature, covered in blood and dirt, glared at me while breathing heavily.

—Krrrk.

Dozens of blades were embedded throughout its body, and blood poured from its open wounds like waterfalls.

Only one of the wings that symbolized the Wyvern remained.

It was still enormous and imposing, but there was no longer any trace of its dignity as a dragonkin offshoot or a Named Monster.

—Grrrrr…

Its eye, full of resentment and killing intent, glared at me.

The emotions conveyed by that gaze were unlike anything I had ever known from a monster.

“Keep that eye nice and gentle. Otherwise, I’ll pluck it out first.”

I tossed out the words and began walking toward it.

That was when it happened.

—Hu. man.

“……!”

It was a single word that made me doubt my own ears.

My feet froze in place. The corners of my eyes trembled involuntarily.

*What did I just hear?*

But I hadn’t misheard it. The creature’s maw shifted, and a clearer pronunciation emerged.

—Do. you. want. to. kill. me?

A monster was speaking.

That very “monster” was speaking.

A groan-like voice leaked through my parted lips.

“This can’t be happening…”

—It’s. dif.fer.ent. from. be.fore.

The instant it finished speaking, the creature’s red eye turned completely bloodred.

And then…

—Heal.

Sssssss.

Magic began gathering around the creature.

* * *

The One-Eyed Carus.

That was the Black Wyvern’s name.

Before earning that name, he had endured countless crises. He had fought not only monsters, but humans as well.

He had repeated battles hundreds of times—winning meant obtaining prey, while losing meant becoming prey.

That day in the past had been no different.

At least, until a human took one of his eyes.

*How dare he? How dare a human less worthy than a bug do this to me!*

Carus was furious. At the same time, he made a vow.

He would kill the human who had taken his eye. Even if he couldn’t find that human, he would kill other humans again and again.

One day, after repeating battle and slaughter countless times, he suddenly came to his senses and realized that he had become the owner of an enormous body and tremendous strength.

*Why? Did I grow stronger by fighting humans?*

Before long, Carus understood. The reason he had grown stronger wasn’t because of his battles with humans, but because he had eaten other monsters.

And every time he did, something inside his body grew stronger.

*What did the humans call this? Oh, right.*

Magic Gems.

After learning the reason for his growing strength, Carus began hunting Magic Gems.

He devoured other monsters and, rather than human flesh, studied the magic equipment the humans carried.

*So this is how those human bastards use Magic Gems.*

The more Magic Gems he absorbed, the higher his Intelligence rose and the stronger he became.

As a Wyvern—a lesser branch of the dragonkin—Carus had possessed remarkable Intelligence to begin with. At last, he was able to set foot in a new realm.

*Magic, huh? Should I learn it?*

Carus established a new nest in a nameless wasteland. He killed everything that might become an obstacle and delved deeply into magic.

That was when he noticed the humans invading his territory.

*I haven’t even finished digesting the Magic Gems I ate earlier…*

Knowing that he was still incomplete, Carus decided to be patient.

Even when several humans recklessly approached his nest, he tried to ignore them.

*Until he smelled that bastard.*

*My eye! The human who took my eye!*

Carus saw red and immediately raced across the wasteland.

Using one of the humans he had deliberately allowed to escape as a guide, he finally came face-to-face with that bastard.

*I’ll kill him! I’ll chew him up, bones and all!*

But that bastard was strong. Even Carus, who had absorbed hundreds of Magic Gems, was pushed back helplessly.

Yet he still had one last card to play.

—Heal.

Sssssss.

His wounds closed, and the bleeding stopped. He couldn’t completely restore his torn wing, but this was enough.

—I’ll. kill. you. hu.man.

Jin Taekyung, his face filled with shock, clenched his teeth.

Carus had already experienced that speed firsthand, so he cast the spell without hesitation.

—Sloooow!

Some faint trace of dragon blood flowed through Carus’s veins.

Five Slow spells overlapped, surrounding Jin Taekyung’s body.

—Kehahahaha!

Carus burst into laughter as he watched Jin Taekyung move as slowly as possible.

That was when Jin Taekyung spoke.

“One hundred points to Agility.”

—……?

Whoosh.

Carus blinked.

His enormous eye filled with the sight of a spearhead holding blue flames.

“What are you looking at, you fucking bastard?”

Crunch!
## Chapter artifact 222

# Chapter 222

Ssssss.

Blue flames flickered over the spearhead.

They were the concentrated form of immense qi—something that even the Wyvern’s steel-like hide and scales could not stop.

There was no way they couldn’t pierce the eye, the Wyvern’s only real weakness.

“What are you looking at, you fucking bastard?”

Without the slightest hesitation, I drove my spear into its enormous eye.

Crunch! Ssssss!

Hide? Scales?

Nothing could stop the spearhead.

Blood gushed out, and Scorching Yang Qi burned through the retina. The vertically slit pupil expanded, and the creature’s maw opened so wide it looked as if it might tear apart.

—Graaaaaaaah!

It was a howl from the depths of its soul.

An inhuman shriek I had never heard before burst from its mouth, which was stretched wide enough to split.

*That nearly blew out my eardrums.*

Even though I had raised my internal energy to protect my hearing, my ears were still ringing.

After driving in the spear, I landed lightly on the ground and watched the creature writhe.

Boom! Kwooooom!

It thrashed wildly, swinging its one intact wing and tail in every direction. Then, at some point, it suddenly raised its head.

—Grrrrr.

The monster’s house-sized head.

Black blood poured from its eye, which had been crushed almost halfway.

It was a horrifying sight—enough to make even a fairly gutsy person step backward. But as I watched, I felt refreshed, as if someone had opened a hole in my chest.

“You’re one dumb son of a bitch. You still haven’t learned your lesson after what happened three years ago?”

Even if it had lost both eyes, it still had other senses.

The creature’s head, trembling from pain, turned precisely toward me.

—Hu. man.

“Why, Wyvern?”

—How. did. you. even?

At its voice, filled with disbelief, I curled up the corners of my mouth.

It was almost a shame that the creature couldn’t see my smile.

“If you wish hard enough, the entire universe will help you. Something like that.”

—My. ma. gic. was. per. fect!

“Ah, I’ll give you that. It surprised me.”

What kind of monster was a Wyvern?

A body and wings as large as buildings. Hide tough enough to deflect most attacks. The ability to use a breath attack.

I truly had never imagined that a creature capable of displaying such terrifying power with its natural physical abilities could also use magic.

*I also never imagined one measly Slow spell would cut my Agility by fifty.*

According to the System notification I had heard then, the **dragonkin** trait had strengthened its magic several times over.

But I still had one trump card left.

“I’ve saved up quite a few points over the years. Saving is a habit of mine.”

Back when I had been a rookie in the Murim, I had raised my stats with every point I earned.

I had been weak then, and my situation had been so precarious that anything could happen the very next day.

But as I gradually grew stronger, I realized something.

*These could be weapons, too.*

Just as martial artists concealed their ultimate techniques until the very end.

—What. kind. of. orc. shit. is. that?

“What do you think? It means your magic won’t do a damn thing to me.”

I leisurely opened my Inventory and took out a new spear. When I tapped the spearhead with my fingernail, a clear sound rang out.

The blind creature’s body jerked at the sound.

—What. are. you. plan. ning?

“You already know. Why ask?”

Step. Step.

Each time I approached, the creature’s tightly hunched body flinched.

“We need to settle our accounts. Including three years of interest.”

There was no room for compromise. This battle would end only when one of us died.

And the one dying here today would not be me.

“I’m going to kill you.”

—Kraaaaaah!

But the creature wasn’t about to take it lying down.

It had lost one wing and both eyes to me, but it was still unquestionably a Named Monster. It had enough strength left for one final struggle.

—Heal!

Sssssss.

Black magic once again wrapped around its enormous body. The blood stopped flowing at once, and new flesh began to grow. It was far faster than any healing magic I knew.

But the magic didn’t end there.

—Dark. Bin. ding!

Shrrrrrrk!

Thorny vines suddenly shot up from the wasteland covered in dust and dirt, wrapping tightly around my entire body.

At the same time, a System notification rang out.

Beep!



> **System**
>
> **Lv.??? Carus** has used **Binding Magic**!
>
> Due to the **dragonkin** trait, the magic is enhanced!
>
> **Strength** temporarily decreased by 10!
>
> **Stamina** temporarily decreased by 10!
>
> **Agility** temporarily decreased by 10!



The thorny vines slowly crawled up from my ankles to my legs, waist, arms, and finally my neck.

The sawlike thorns jutting from the vines pierced through my thin leather armor and dug into my skin.

Beep.



> **System**
>
> **Paralysis Poison** has entered your body!
>
> **Nerve Poison** has entered your body!
>
> Status abnormality: **Poisoned**!



“……Huh. What the hell is this?”

—Grrrrr.

The creature—or rather, Carus—let out a triumphant laugh. Its horribly shattered eye was already gradually returning to its original form.

—You. let. your. guard. down. hu. man!

“Let my guard down?”

I thought about it for a moment, then nodded.

“Yeah. I did let my guard down.”

—……Why. are. you. so. calm?

“Usually, when someone acts relaxed in a situation like this, it means one of two things. Either they’re bluffing their ass off, or…”

Ding.



> **System**
>
> The effect of **Unaffected by a Hundred Poisons** has been applied!
>
> **Paralysis Poison** has been neutralized!
>
> **Nerve Poison** has been neutralized!
>
> Status abnormality: **Poisoned** has disappeared!



“Or they have a good reason to be.”

As soon as I finished speaking, I took another step.

The thorny vines, each as thick as my thigh, tightened around my entire body, but they couldn’t stop my advance.

“While I’m at it, I’ll splurge on a bonus. Fifty Strength. Fifty Stamina.”

Ding.



> **System**
>
> 100 Bonus Points have been consumed!
>
> The points have been applied to your stats!



Crack. Crrrunch.

I tore and shattered the vines with overwhelming power and Strength.

Carus’s magic had been greatly strengthened by the dragonkin trait, but its actual level was not particularly high.

“Slow magic, binding magic. What’s next?”

Its eye had already almost completely healed.

When Carus saw me emerge from the vines unharmed, its maw fell open.

—You…you!

I casually brushed off the pieces of vine clinging to my arm.

“Don’t you have any other magic? You were so confident that I thought you’d at least know factoring, but you’re actually just a master of addition and subtraction.”

—How. did. you?

“My own magic.”

—Your. own. ma. gic?

“Yeah. Magic.”

I shifted the iron spear in my hand into a reverse grip.

That was the entirety of my preparation. This spear was my magic, and the creature would never be able to stop it.

“Huuup.”

I drew in a deep breath. The muscles throughout my body meshed together like tiny gears, and the world slowed down.

I leaned back and threw my arm forward.

Along with a spell I hadn’t had time to memorize.

“Burst, sesame.”

Whoosh! Fwoooooosh!

Against the red sunset coloring the horizon, a blue flash pierced the creature’s eye, dyed an even deeper shade of blood.

It burned, shattered, and exploded.

Crack!

—Graa…aaaaaaah!

Listening to its scream of agony, I walked toward it. With every step, familiar faces flashed past my eyes.

Faces I would probably never forget for as long as I lived.

Since that day three years ago, shackles had always been fastened around my ankles.

Anger, guilt, the desire for revenge. Emotions that had piled up, layer upon layer.

All of it had been heavy and overwhelming. So heavy I couldn’t take even one step.

*But now…*

At some point, I had grown enough to bear that weight.

I could finally offer belated comfort to the spirits of those who had died before me.

*Yes. Now, finally.*

Just as I murmured those words silently in my heart, mana rippled around the creature writhing in pain.

—Kraaaah! Slow! Dark Binding! Magic Arrow!

Three spells erupted in succession.

I kicked off the ground and sprinted forward. The moment I shot beyond Slow’s area of effect like a streak of light, thorny vines and dozens of mana arrows blocked my path.

Sssshing! Shrrrk!

Everything was sliced apart along the semicircle traced by blue flames. Realizing that its attacks had failed, the creature flapped its one remaining wing.

There was no need to aim at such a huge target. Once again, a flash shot from my hand.

Swoooooosh! Thud!

—Kyaaaaaaah!

Whoooosh!

A sharp scream rang out. Then the creature’s tail, bristling with spikes, came flying at me with a terrifying boom as it split the air.

Boom!

But I had already leaped half a beat ahead of it.

The rocks scattered across the wasteland like reefs rising from the sea shattered into powder.

*Open Inventory. Equip.*

As I descended, I swung my spear.

Shraaaak.

The severed tail rolled through the dust with black blood spilling from it.

—Kraaaaah!

Shrrk. Shrrk. Shrrk.

It was like perfectly meshing gears.

I blocked, dodged, and cut through every attack the creature hurled at me in its desperate struggle.

Then I suddenly realized that no more attacks were coming and stopped my hand.

—Krrk. Grrrk.

Two severed wings. A severed tail. Two eyes that could no longer function.

Ragged breathing, ready to stop at any moment, escaped from the creature’s maw as it lay submerged in a great pool of blood.

I watched it for a while before opening my mouth.

“Do you want to live?”

—……

“Then use your healing magic. I’ll wait.”

—Will. you…save. me?

“No. It just feels like a waste to send you off like this.”

—……!

“Endure ten more times. After that, I’ll kill you.”

The creature’s body trembled. Its gaping eye, pouring dark-red blood like a waterfall, turned toward me.

—You. are. cruel. hu. man.

“Compared to what you did, this is nothing.”

—I. only. did. what. I. had. to. do.

“I know.”

Humans killed monsters, and monsters killed humans.

Their killing of one another was a history and a chain that had continued for decades. And also…

“I’m no different.”

Completing my revenge. That was what I had to do now.

After a short silence, a single word filled with resignation escaped its mouth.

—……Kill. me.

The strength slowly drained from its twitching body.

I aimed my spear at the creature’s blood-caked brow. Then I whispered in a low voice.

“Thank you.”

For staying alive until now. And for dying by my hand.

With that barely audible whisper, I drove the spear forward.

Shnk.

The Scorching Yang Qi flowing from the spearhead as it gently pierced through the center of its brow rampaged like a wild beast, devouring and burning everything in its path.

The skull harder than steel. Flesh. Brain matter. Everything else.

Ding.



> **System**
>
> You have defeated **Lv.115 Carus**!
>
> You have achieved the Achievement **Named Monster Defeated**!
>
> You have achieved a great Achievement. A corresponding Reward will be granted!
>
> You have perfectly cleared the A-Rank Gate, **The Black Wyvern’s Nest**!
>
> Calculating all Rewards…
>
> You have acquired an enormous amount of EXP and Fame!
>
> **Level Up!**
>
> **Level Up!**
>
> …



System notifications washed over me like waves. I released the spear shaft, which had grown hot, and thought,

*I did it. Finally.*

What more was there to say?

The shouts of other people brought me back to myself as I stood there in a daze.

“Mr. Jin Taekyung!”

“Taekyung!”

Team Leader Choi, Butler Kim, Im Kkeokjeong. Song Song.

My guildmates, whom I had met through new connections. My people.

Watching them race toward me, I let out a weary laugh.
## Chapter artifact 223

# Chapter 223

A shiver.

That was what everyone watching the battle felt.

They had known for some time that Jin Taekyung was extraordinarily skilled. They also knew that what they had seen of him so far was not everything he was capable of.

*But who would have thought he was this strong?*

Team Leader Choi—or rather, Choi Minwoo—swallowed dryly.

Though it had only been a few months, he was the person who had watched Jin Taekyung from the closest distance during that time.

Yet in this moment, Choi Minwoo realized that every judgment he had made about Jin Taekyung had been wrong.

*What… exactly is this man?*

Everything he had seen until now had been no more than the tip of the iceberg.

A few months ago, when they had first met at the Hunter manpower office, Taekyung had volunteered to work as a porter for a few hundred thousand won a day.

Now, he had hunted a Named Monster all by himself.

And it had been an overwhelming victory.

Puhk!

A spearhead infused with Aura pierced through the monster’s brow.

It was the moment that an immensely powerful Named Monster had been killed by a single person.

It was also the moment a new legend was born.

“Young Master.”

“……Ah.”

Choi Minwoo had been dazed for a moment, but Butler Kim’s call finally brought him back to his senses.

When he looked around, everyone had a similar expression.

Shock. More shock.

Trembling with an indescribable shiver, they rushed toward Jin Taekyung as if they had planned it together.

“Mr. Jin Taekyung!”

“Taekyung!”

Jin Taekyung smiled at them. It was a relieved smile, as if he had finally cast off even the slightest trace of regret.

Choi Minwoo let out a hollow laugh.

“Are you really in the mood to smile right now?”

“I’m not sure. I don’t really know what else to do.”

“You should shout, at least. It’s not like anyone else is here.”

“Something like, ‘I killed a Named Monster!’?”

“Yes. Now it’s finally starting to feel real.”

Choi Minwoo stared at Jin Taekyung, who was scratching the back of his head, then suddenly extended his hand.

A sentence he had momentarily forgotten had come back to him.

There was something he had wanted to say if—just if—Taekyung won.

“Thank you for all your hard work.”

“…….”

“You’ve truly been through so much all this time.”

For an instant, Jin Taekyung’s eyelids trembled.

An indescribable emotion passed through his clear, deep-black eyes. Then he firmly clasped Choi Minwoo’s hand.

“Thank you. And everyone else, too.”

* * *

For a while, I couldn’t come to my senses amid the barrage of questions and congratulations flying at me from every direction.

“So that was already thirty years ago. The Great Cataclysm was still in full swing at the time…”

“Ah, yes.”

Butler Kim, who rarely showed his emotions, excitedly listed one event after another that had taken place during the Great Cataclysm.

“My goodness. This isn’t a dream, is it? No, it isn’t, right?”

“Uh, no.”

Song Song stared at me, still looking as though she couldn’t tell whether this was a dream or reality.

“Sniff. Taekyung! You bastard! Sniff, sob!”

“……Why are you crying again, Uncle?”

“Because I’m proud of you, you punk. I’m proud. Sniff!”

Im Kkeokjeong burst into tears as if his own child had made it back alive.

In a situation like this, I didn’t have time to check the System messages that had piled up.

In the end, Team Leader Choi was the one who brought order to the chaos.

“All right, everyone, calm down. Let’s start with the cleanup.”

“That’s a good idea, but…”

I cautiously asked the most important question.

“How are we supposed to clean up?”

“……Oh. Well, that is…”

Even Team Leader Choi, who was never at a loss in any situation, looked flustered.

Cleanup after a raid was something we always did, and it was usually similar every time.

Check and treat the casualties, then sort through and collect the byproducts. If there was anything else, it was usually just inspecting the Equipment.

But this time was different.

*This thing’s body alone is over fifty meters long.*

And that was only counting its length. Its enormous girth, wings, tail, and everything else were separate problems.

Just thinking about how to deal with it was giving me a headache.

*But we can’t just leave it behind and go.*

Processing byproducts meant separating the hide, bones, and flesh.

The Carus I had brought down was a Named Monster, so its rarity and the difficulty of processing it were beyond imagination.

*Fuck, what are we going to do with the scales?*

They weren’t fish scales that could be scraped off with a kitchen knife.

Aside from me, someone would have to be at least as capable as Butler Kim or Team Leader Choi to handle the job. Of course, there was one possible solution.

One extremely easy—and simultaneously extremely difficult—method remained.

*Inventory.*

Based on everything I had experienced so far, the Inventory’s capacity was practically infinite. Besides, this was the corpse of a monster, not a living creature.

It was worth trying.

*The problem comes afterward.*

I could already picture everyone’s reaction if I put Carus’s corpse into my Inventory.

Even if I came clean to the guild members, suspicions would arise unless I intended to keep the byproducts forever.

*The reporters are camped out at the Gate entrance. So how exactly did he secretly carry all that out? And so on.*

If that happened, it might not be long before the entire country learned my secret.

The front pages of the daily newspapers and every news headline would be decorated with my name.

> **Breaking News:** A-Rank Hunter Jin Taekyung Revealed to Be a System User.

> **Interview with Jin Taekyung:** “Martial arts were the easiest part.”

> **Hunter Association:** “Jin Taekyung’s Hunter license must be revoked.”

> **Jin Taekyung Denounces the Hunter Association:** “Fuck, if it pisses you off, use the System yourselves.”

> **NASA Official Statement:** “We will capture him at all costs and subject him to experiments.”

“…….”

“Mr. Jin Taekyung? Is something wrong?”

“No. Just thinking about it made me dizzy.”

“Pardon?”

“It’s nothing.”

It was something that absolutely must never happen. Obviously.

In the end, after everyone put their heads together, one opinion was finally chosen.

Team Leader Choi declared it in a solemn voice, like a judge delivering a verdict.

“Let’s bring in outside personnel.”

Gates were not unchanging spaces like evergreen trees.

After a certain amount of time, their destroyed environments and monsters were restored. This phenomenon was called Regen, and the time it took for a Gate to undergo Regen varied according to its Grade.

“As far as I know, A-Rank Gates usually undergo Regen once a week. Today is only the first day, so we have plenty of time.”

The plan was to bring in outside personnel as quickly as possible and speed up the work. For now, it was the most reasonable and feasible option.

There was, however, one small problem with the plan.

“The exit Gate hasn’t opened.”

That was exactly what had happened.

After killing a Named Monster, the exit should have opened as a matter of course. Yet for some reason, even after several dozen minutes had passed, it remained silent.

Im Kkeokjeong also looked around anxiously.

“Come to think of it, why hasn’t it opened? Is the Gate broken?”

“…….”

What a horrible thing to say.

As if Login Murim wasn’t enough, now we had Login Gate? If that was what was happening, I’d rather bite my tongue and die.

Just as I was getting an ominous feeling, Butler Kim spoke.

“It appears that the boss monster is still alive.”

“Alive? The boss monster?”

When I pointed toward Carus’s corpse, which lay with its head buried in a pool of blood, Butler Kim shook his head.

“Named Monsters and boss monsters are different. To explain simply…the former is an uninvited guest, while the latter is the homeowner who was here originally.”

“The homeowner?”

“Yes. It may be easier to understand this way. If an armed intruder broke into Hunter Jin Taekyung’s home, what would you do?”

“I’d beat him until he begged me to kill him.”

“……I forgot. I meant if you were an ordinary person.”

“Oh. Then I’d run. If I thought I was going to die before I could escape, I’d fight back.”

“The boss monster is the same. A powerful being it could never hope to fight appeared, so it fled out of fear.”

The inside of a Gate was ultimately a world ruled by the law of the jungle.

The strong reigned, and the weak were trampled.

Maybe it would have been different with a monster that lived in a tribe, but Wyverns were known to be solitary and ferocious. It probably hadn’t ended with the boss monster merely taking a few knocks to the head and moving out.

From the boss monster’s perspective, it had made a fairly wise decision.

*Unfortunately, that just made things more troublesome for us.*

There was no way the thing had run away to survive, only to stay nearby and trim its claws.

It would have hidden as far away and as secretly as possible. And with only five people, searching this vast wasteland was impossible.

“Then…”

“We need to return to the entrance we used to enter.”

It was the obvious conclusion. And the right person for the job had already been decided.

Without giving it much thought, I shot my hand into the air.

“I’ll go.”

Team Leader Choi asked with concern in his eyes.

“You?”

“That seems like the fastest option. Doesn’t it?”

“That’s true, but you must be exhausted after the battle.”

*I just leveled up, damn it. Just let me go.*

I swallowed the words that had risen to my throat and answered instead.

“I’m still full of energy. If you’re worried, I can receive some healing magic before I leave.”

“As you know, the distance to the entrance is considerable.”

“As you know, I’m pretty fast.”

It had taken quite a while to reach this place the first time, but it was different if I went alone. I wouldn’t need to worry about monsters, and I wouldn’t be traveling in a group.

If I ran at full speed, I could reach the Gate entrance within an hour or two.

“Hmm. In that case, I’ll leave it to you. Mr. Taekyung and Butler Kim can go together.”

“Butler Kim, too?”

Butler Kim stroked his impressively grown beard as he answered.

“We need to bring in outside personnel.”

Processing the byproducts of a Named Monster required at least a B-Rank Hunter, or preferably an A-Rank Hunter.

“I know a few people. If I go personally, they’ll probably drop everything and come running.”

“…….”

That sounded about right.

I still couldn’t forget the sight of the Sangdong Guild Master doing PT exercises while loudly echoing commands.

*It was something I could hardly believe even after seeing it.*

Knowing Butler Kim’s spectacular track record, I could only nod at the decision. We needed him to bring in outside personnel.

“So it’ll just be the two of us, Butler Kim and me?”

“Yes.”

Butler Kim nodded and stepped behind me.

“All right. I’m ready.”

“Pardon?”

“Would you bend your back a little?”

“……Why do you need my back?”

No, what exactly was he ready for? Why did I need to bend my back?

I spoke, a terrible suspicion forming in my mind.

“You don’t mean… soap?”

“Please carry me on your back.”

“Oh. Sure.”

Thank goodness. He wasn’t a centaur.

I let out a sigh of relief and willingly offered my back to Butler Kim.

* * *

Thud-thud-thud-thud-thud!

With Butler Kim on my back, I ran without slowing down.

We encountered a group of Orcs wandering through the wasteland once along the way, but that was all.

“Fire Rain.”

It was the magic of an A-Rank mage.

One-third of the Orcs died beneath the downpour of fire, and the rest scattered in every direction.

I felt like a walking mobile turret.

*This isn’t bad.*

Just as I was thinking about how efficient raids could become if I did them this way, we passed through the barren wasteland and saw a dense jungle ahead.

“You’re astonishingly fast. We’re already at the jungle.”

“I’m going to slow down from here. Given the surroundings, we could get lost.”

“I’ll follow your lead, Hunter Jin Taekyung.”

The jungle, filled entirely with trees and undergrowth, was practically a maze, making it easy to lose one’s way.

We slowed down and continued along the route.

That was when it happened.

“……Huh.”

I suddenly stopped, letting out a hollow laugh.

Butler Kim asked in puzzlement at my abrupt behavior.

“What is it?”

“It’s nothing. Just…”

How was I supposed to explain this?

At last, I found the right word and added gently,

“There are hyenas.”

“Hyenas?”

“Yes.”

Stupid, persistent hyenas that kept baring their teeth even after I had let them go once.

I crooked my finger toward the dense undergrowth in the distance.

“Come out, you fucking bastards.”

Rustle.

The undergrowth shook, and the hyenas began emerging one by one.

But my eyes were fixed on only one person.

> **System**
>
> **Lv. 80 Won Myunghoon**

“What an ill-mannered bastard.”

The leader of the hyenas bared his teeth and growled.
## Chapter artifact 224

# Chapter 224

A few hours earlier, it was Won Myunghoon’s shout that stopped the dozen-plus Star Guild members as they made their way back toward the Gate entrance with all their might.

“Wait. Everyone, halt!”

Every eye turned toward him.

With the tension of a terrifying Named Monster possibly appearing behind them at any moment, Won Myunghoon—who had been lost in thought by himself—finally opened his mouth.

“Scout.”

“Yes, Guild Master.”

The Guild member assigned to scouting answered immediately.

He was fast on his feet and skilled with a bow. Thanks to the good luck of drawing lots, he had barely escaped death, unlike his other comrades.

“Report our current location.”

“According to the coordinates, we’re at 175.37.990.”

“Fuck the coordinates. How far are we from the Gate entrance?”

“Based on our speed so far, it should take approximately seven minutes.”

“Not far, then. There’s only one route to the Gate entrance, right?”

“……Yes. There is, but…”

The scout trailed off with an uneasy expression.

The other Guild members sensed that something was wrong and exchanged glances. Then a single sentence turned their unease into reality.

“We’ll form a cordon here.”

“What?”

“You mean a cordon? In this situation?”

“Guild Master, that’s—”

The Guild members would normally have obeyed without complaint, but Won Myunghoon’s eyes turned cold at their resistance.

“Shut up and follow my orders. I have my reasons.”

“Even so, this isn’t right! We’re talking about a Named Monster—urk!”

Won Myunghoon seized the throat of the Guild member who had raised his voice the loudest and growled.

“You’re disobeying the Guild Master’s orders in a Gate? You suicidal son of a bitch…”

It happened in the blink of an eye.

The atmosphere froze.

Everyone there knew that Won Myunghoon’s words were not aimed at only one person.

They had watched him for years. They knew he was more than capable of following through on his threats.

“I—I’m sorry.”

“This is your last chance. There won’t be a second.”

Thud.

Won Myunghoon turned away from the Guild member, who collapsed to the ground with a white face, and swept his sharp gaze across the area.

“Fucking idiots.”

Even in the face of the unfiltered abuse, a dozen pairs of eyes remained fixed on the ground.

They had already spent several years dealing with Won Myunghoon. This was nothing new to them.

They had to be even more careful around him inside a Gate. He was an A-Rank Hunter—a powerhouse none of them could defeat even if they all attacked him together.

“Do your brains not work? Do I look stupid enough to take on a Named Monster?”

The heads that had been bowed so deeply began to rise, one by one.

“Then…”

“We’ll deal with those losers.”

“You mean the Peace Guild?”

“By now, they should all be dead.”

While fleeing in a panic, they had heard the roar of the monster.

It was pure terror—the kind of roar that made their knees go weak and sent chills down their spines just by hearing it.

They had never managed to see what the creature looked like. That was precisely why they were still alive.

*How could five people possibly fight something like that? They’re all dead by now.*

That was what every one of them believed.

Except for Won Myunghoon.

“What if even one of them survived and escaped?”

“Th—that…”

“No way.”

They had never considered the possibility.

Normally, they might have. But their minds had been paralyzed by fear of the Named Monster and the instinct to survive.

Won Myunghoon spoke to the Guild members as they hesitated.

“If even one of those losers survives and gets out of the Gate, every single one of us is finished.”

“…….”

“An A-Rank Hunter who’s been soaking up the media spotlight is dead. Then one of the only surviving Peace Guild members starts talking about us? You don’t need me to explain what happens after that, do you?”

The attention of the media—or rather, the entire country—would turn toward them.

Investigators would get involved. The news and mass media would treat the matter as a major story and pour out new reports every day.

Even if the survivor couldn’t provide clear testimony or physical evidence, the contempt and condemnation directed at them would not disappear.

They might even have to leave the country. They would be reduced to people who needed a visa just to visit their parents’ graves.

The thought alone was horrifying.

“Sometimes, people’s perception matters more than the truth. You all experienced that eight years ago, didn’t you?”

“Guild Master!”

“That’s—!”

Agitation spread violently among the Star Guild members.

It was an unspoken taboo. Yet Won Myunghoon himself had brought it up.

Wasn’t he the one who had planned everything and recruited them in the first place?

At the Guild members’ hardened gazes, Won Myunghoon let out a quiet laugh.

“Look down, you fucking bastards. Before I pluck all your eyes out.”

“……!”

“You joined because you wanted to. Is there a single bastard here who didn’t take my money? You used that money to buy houses and cars, drink and chase women, then got married and had kids. Now you’re living well while pretending to be good fathers and devoted husbands, aren’t you?”

Won Myunghoon irritably ran a hand through his hair.

Every time his gleaming eyes swept past them, the people around him trembled.

They wanted to deny it, but every word out of his mouth was true.

They had already crossed a river they could never return across, and Won Myunghoon was the one who had ferried them to the other side.

The ferryman had already hidden the boat. Without his permission, they could never return to the far bank.

Not until their dying breaths.

“I won’t waste any more time talking. Hide and form a cordon. When I give the signal, be ready to kill anyone.”

Won Myunghoon’s voice, thick with killing intent, was no different from a written verdict handed down by the Supreme Court.

Realizing that there would be no appeal, the Guild members scattered and began forming the cordon.

“Fucking idiots. It’s been eight years already…”

As Won Myunghoon muttered the words through clenched teeth, one of the Guild members cautiously approached him.

“Guild Master.”

“What?”

“Team Leader One, sir—I mean, what should we do about Team Leader One?”

“Kim Jonghun? Where the hell is that bastard?”

“We moved him over there for now.”

Won Myunghoon turned his head in the direction the Guild member pointed and let out a hollow laugh.

Only a few meters away, Kim Jonghun was pale and clacking his teeth together. He looked like a man possessed.

“Pathetic bastard. I was the idiot for keeping something like that around and calling him an A-Rank Hunter.”

Won Myunghoon clicked his tongue softly and waved a hand.

“Handle it quietly.”

“What? I—I can’t!”

“What the hell does that mean?”

“I mean, I won’t commit murder.”

“What? You lunatic, what the hell are you thinking—wait.”

Won Myunghoon had been about to smack the Guild member when he suddenly stopped.

What he had originally meant was for them to keep Jonghun quiet somehow, with Silence magic or whatever else was necessary.

But was that really necessary?

*Come to think of it, there’s no one who knows more about my secrets than him.*

He had used that man as his right hand for no less than ten years.

Jonghun had some underhanded cleverness of his own, and his skills as a Hunter were excellent.

Even when that incident had occurred eight years ago, Won Myunghoon had believed that Team Leader 1 was the only one who would never betray him.

*If he opened his mouth, he wouldn’t have gotten off unscathed either.*

It wasn’t a matter of trust. It was a matter of mutual interests.

Their greed might have differed in size, but in some ways, the two of them were cut from the same cloth.

But…

*He’s useless now.*

Won Myunghoon had seen plenty of people exposed to the Fear of high-level monsters.

Their symptoms differed, but they all had one thing in common.

*Junk.*

Those whose souls had been branded by fear could never return to the way they had been before.

Some went mad and were locked away in special wards. Even if they barely recovered, their lives as Hunters were over.

*He knows the most about my secrets. And he was the one who personally acquired Yeti’s Necklace.*

On top of that, his credentials as an A-Rank Hunter had become nothing more than a scrap of paper.

Won Myunghoon’s deliberation was brief, and his decision was even faster.

“Bind him. I have a use for him.”

“What?”

“When that Named Monster comes, don’t you think we’ll need at least one piece of prey to throw to it?”

“……!”

“It works out well in more ways than one. Since Jin Taekyung is dead, we need to throw in an A-Rank Hunter from our side to make the story convincing.”

Won Myunghoon patted the frozen Guild member on the shoulder as he passed and hid himself in the nearby undergrowth.

*Come on. Anyone. Come.*

He didn’t have to wait long.

When he saw two people emerge from the undergrowth several dozen meters away, the corners of his mouth lifted.

*That old Guild Master and Jin Taekyung. Is everyone else dead?*

Jin Taekyung was covered in blood from head to toe, with an old mage carried on his back.

No matter how he looked at it, they had the appearance of wounded survivors who had lost a battle.

*This should be easy.*

Especially Jin Taekyung. Won Myunghoon wanted to kill that bastard with his own hands.

He had just finished preparing to signal the Guild members when—

“Come out, you fucking bastards.”

Jin Taekyung crooked a finger directly toward the undergrowth where Won Myunghoon was hiding.

The smile at Won Myunghoon’s lips vanished without a trace.

* * *

“What a rude bastard.”

Seeing Won Myunghoon’s twisted face, I couldn’t help but laugh under my breath.

What could I say? It felt like I had finally seen the absolute bottom of one human being.

“You’re laughing?”

Apparently, my reaction had made him even angrier.

He licked his dry lips and exhaled a hot breath.

“You bastard…don’t you understand what kind of situation you’re in?”

“I understand it perfectly.”

“And someone who understands the situation is grinning?”

“Choose your words carefully. When you say things like that, it makes me want to split your head open.”

“……What?”

“You should’ve stopped when I called you Mr. Won Myunghoon. Won Myunghoon, you fucking bastard.”

The hyenas’ faces went blank.

After being pressed tightly shut for some time, Won Myunghoon’s lips finally managed to open.

“Have you lost your mind?”

“I’m always perfectly sane. Aren’t I, Butler Kim?”

Butler Kim, who was still on my back and watching the situation unfold, answered.

“Entirely normal. Never losing your composure, no matter the situation—that is one of the basic qualities a Hunter should possess.”

“What about that bastard?”

“If this had happened during the Great Cataclysm, we wouldn’t have found even his corpse. Those were somewhat rougher times.”

“That’s what he says.”

Bang!

A single punch smashed apart a tree thick enough to wrap both arms around.

Won Myunghoon’s face flushed bright red as he glared at Butler Kim and me.

“You fucking bastards!”

“What a rude bastard. There’s nothing he won’t say to an elder, is there? Right?”

Butler Kim answered calmly.

“The young fellow is somewhat lacking in manners. But, well, isn’t this a good world? We ought to give him a chance.”

“Is that so?”

“Life is a series of choices. And from what I can see, it appears you have already made up your mind.”

“You’re a ghost.”

“I don’t particularly like that word. I am somewhat advanced in age, after all.”

“I’m sorry. I didn’t mean anything by it.”

“I’ll get down first. One, two, three.”

Crack.

As Butler Kim hopped down from my back, the sound of a bone slipping out of place came from his knee.

“Oh dear, are you all right?”

“My knee is a little troublesome. Heal.”

Once the orb of light disappeared, he tapped his knee a few times and smiled.

“I’m fine now.”

“Wow.”

Magic really was incredibly convenient.

After letting out that exclamation, I turned my head toward the knife-like gazes stabbing in from every direction.

A dozen or so Star Guild members, including Won Myunghoon, were glaring at us as if they wanted to tear us apart and kill us.

“What the fuck are you trying to do?”

“What else? I helped him down. I thought he’d be shaken around quite a bit during the fight.”

“Fight?”

“What, didn’t you come here to fight me?”

“Of course not.”

Won Myunghoon added with a savage laugh,

“We came to kill every last one of you.”

“Oh… You sound exactly like a villain in a web novel.”

I was fairly impressed.

At the same time, the hesitation I had been clinging to until the very end faded away, leaving my mind clear.

*Right. I just had to do it.*

“Thanks for saying that. My headache’s completely gone. Maybe you’re not a son of a bitch after all—maybe you’re Dogvorin.”[^1]

“You bastard!”

“Maybe not. Then let’s go?”

“……What?”

Whoosh!

I suddenly found myself wondering what expression Won Myunghoon was wearing.

But when I thought about it, there was no point.

Whatever expression he had worn until now, the expression he was about to make had already been decided.

“Bear with the pain. No crying now.”

Crack!

As he hurriedly turned and swung his arm, I caught it and twisted it.

The bone broke in an instant. His grip went limp, and the spear slipped from his hand.

His smooth, wrinkle-free face twisted like a demon’s as a scream burst from his throat.

“Gyaaaaaaaaaaah!”

“Didn’t I tell you?”

I continued in a calm voice.

“Never bare your teeth at me again.”

At the same time, I drove my tightly clenched fist into his maw.

Crunch!

[^1]: Gevorin is a Korean painkiller. Taekyung swaps its first syllable for the Korean word for “dog” to make a pun.

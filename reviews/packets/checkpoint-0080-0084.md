# Checkpoint Review — 80–84

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

# Chapters 80–84

## Plot

During a safety-inspection period following a fatal Gate accident, the Peace Guild bribes its way into the B-rank Gate **The Minotaur’s Labyrinth** alongside Sangdong Guild’s fifteen-person raid team. The team includes seven B-rank Hunters; Im Kkeokjeong is registered as an E-rank tank despite the danger, while Butler Kim vouches for his twenty years of experience.

Upon entry, Jin Taekyung receives the restricted **B-rank Gate Clear Quest**, whose first-clear Reward and failure condition remain undisclosed. Team Leader Choi equips the Peace Guild with powerful loaned gear, including Taekyung’s Peak-grade Masterwork Black Drake Leather Set and Masterwork Black Thorn Spear. Kkeokjeong receives Matador’s Full-Body Armor and Matador’s Shield, which provide bonuses against bovine monsters.

Eight Minotaur Warriors emerge from five cavern holes, overwhelming Sangdong’s advance. Im Changsoo, Sangdong’s Level 65 team leader and Guild Master’s son, mocks Taekyung and deliberately misnames him Jang Taekyung. Taekyung answers by calling him Shit Changsoo, escalating their hostility. When Changsoo’s attempts to court Song Song fail, he challenges Taekyung to defeat the eight Minotaurs alone: 500 million won per monster, all byproduct rights, and Song Song’s transfer to Sangdong Guild as the additional stake. Song Song rejects Changsoo’s womanizing, money-flaunting character but accepts the wager, which the Guild Master and Choi also approve.

Taekyung accepts after judging that he can win. He crosses the cavern instantly, beheads one Minotaur, and kills all eight, triggering Bleeding and a Level Up. Changsoo agrees to pay the promised 4 billion won and surrender the byproducts. After Taekyung recalls Changsoo’s behavior toward Song Song, Changsoo draws his sword but is disarmed and subdued. He agrees to apologize to Taekyung and the Peace Guild. Taekyung openly identifies himself as both a Hunter and a Murim martial artist.

## Continuity

- The Peace Guild has entered The Minotaur’s Labyrinth with Sangdong Guild as a fifteen-person raid team.
- The B-rank Gate Clear Quest is active for Taekyung; its Reward and failure condition are unknown.
- Taekyung is using the Masterwork Black Drake Leather Set and Masterwork Black Thorn Spear. The set grants Strength, Stamina, Agility, and Toughness +10; the spear has a 90% chance to inflict Bleeding on hit.
- Im Kkeokjeong is serving as the front-line tank with Matador’s Full-Body Armor and Matador’s Shield.
- Im Changsoo is Sangdong Guild’s Level 65 team leader, the Guild Master’s son, and a notorious womanizer nicknamed Horndog. He treats his subordinates abusively and sponsors the C-rank mage Hye-rin.
- Song Song rejected Changsoo’s romantic advance but agreed to transfer to Sangdong Guild if Taekyung lost the wager.
- Taekyung defeated all eight Minotaurs, received a Level Up, and won the wager. Changsoo owes him 4 billion won and all byproducts and agreed to apologize; whether he fulfills these promises remains unresolved.
- Team Leader Choi has recognized that Taekyung’s abilities and conduct are inconsistent with an ordinary C-rank Hunter.
- Taekyung’s identity as both a Hunter and Murim martial artist is now known to Changsoo and the surrounding raid members.

## Translation Decisions

- Retain **Peace Guild**, **Sangdong Guild**, **Hunter Association**, **The Minotaur’s Labyrinth**, **Minotaur Warrior**, **Black Drake**, **Masterwork Black Drake Leather Set**, **Masterwork Black Thorn Spear**, **Bleeding**, **artifact**, **Peak**, **Matador’s Full-Body Armor**, **Matador’s Shield**, **Taunt**, and **Hallucination**.
- Retain **Shit Changsoo** for the insulting surname pun and **Horndog** for Changsoo’s nickname.
- Use **Top-tier** for 초일류 and **First Rate** for 일류.
- Render 껄떡쇠 as **lech** and retain **oppа** in Changsoo’s coercive, possessive speech.
- Retain the **baram** wind/infidelity pun with a concise footnote, and use **big bills** for 큰 거.
- Render 발설지옥 as **tongue-pulling hell**, with a footnote explaining its Buddhist punishment reference.

## Durable state

{
  "active_continuity": [
    "Taekyung successfully logged out after roughly twenty days in Murim; his watch showed 2:05:35 in the modern world, and ten modern-world days now correspond to one hour in Murim.",
    "Taekyung currently has fifteen years of internal energy, and circulating his qi slightly increases it; Sleep Mode normally keeps his sleep below three hours except when seriously injured.",
    "Team Leader Choi owns the café where Taekyung signed a contract providing a 500 million won signing bonus, a fixed monthly salary of 50 million won, a seventy-percent settlement share, housing, a car, and other benefits.",
    "After ten days of Mukyung’s training, Taekyung mastered the Jin Family’s Spear Technique and Jin Family’s Manoeuvre Technique, and the Training? Trial! Quest succeeded with a Level Up, an Inventory reward, and notice of an additional reward.",
    "Hyuk Mujin remains badly injured after the attack, and the unidentified assassin may be the Head Elder’s hidden disciple.",
    "Jin Mukyung reunited with Jin Wikyung after three years but remains detached and prioritizes sword training; Wikyung plans to summon every Shanxi sect on New Year’s Day and may seek to become Alliance Leader.",
    "Gong Yacheong is recovering and will take charge of the rebuilt Sakju Branch; Socheon and Soyul will accompany him in six months, and five-year-old Soyul does not know her parents are dead.",
    "The Returnee title grants Taekyung All Stats +10 and activates Login and Logout; Taekyung accepted that he was half-finished, asked Mukyung for help, and received a System time limit of 9 days 20 hours 23 minutes.",
    "Childeuk is an injured former meal-delivery servant who became a Level 12 martial artist directly under Jin Wikyung; Wikyung publicly embraced and praised him after acknowledging a minor misunderstanding.",
    "Lee Seowol is the new female Sect Leader of the Mount Heng Sword Sect; Taekyung received the forced Yesterday’s Enemy, Today’s Ally Quest to deliver an invitation for New Year’s Day.",
    "Peace Guild has five members: Taekyung, Team Leader Choi, Butler Kim, Im Kkeokjeong, and Song Song. Butler Kim is Guild Master, Choi leads Team 1, and the other three are team members.",
    "The Peace Guild’s Guild house is Sooni’s Super in Bucheon’s Gate-dense district, on property purchased from the former owner’s surviving family for slightly more than 2 billion won per pyeong.",
    "Im Kkeokjeong is married with two children and joined Peace Guild after Choi recruited him while hospitalized.",
    "Team Leader Choi formerly served in Ares Guild with Song Song; Butler Kim is a retired mage and former Hunter who trained at Nonsan’s 28th Regiment, 1st Battalion, as did Taekyung. Choi is Level 75, Kim Level 80, Song Song Level 64, and Im Hyeokjun Level 24.",
    "A Bucheon Terminal Guild raid against seven B-rank Minotaurs ended with the monsters defeated but two C-rank Hunters dead, making Taekyung judge the Peace Guild’s first raid dangerous.",
    "The Peace Guild joined Sangdong Guild’s party for its first official raid into The Minotaur’s Labyrinth; Sangdong’s team leader is Im Changsoo.",
    "Choi loaned Taekyung a Peak-grade Masterwork Black Drake Leather Set and a Peak-grade Masterwork Black Thorn Spear with a 90% chance to inflict Bleeding on hit.",
    "Sangdong Guild and Peace Guild entered The Minotaur’s Labyrinth as a fifteen-person team with seven B-rank Hunters; Im Kkeokjeong was registered as an E-rank tank, and Taekyung received the restricted B-rank Gate Clear Quest. Taekyung is both a Hunter and a martial artist, and Choi has noticed that his behavior is inconsistent with an ordinary C-rank Hunter.",
    "Im Changsoo is the Sangdong Guild Master’s son, behaves abusively toward his team, maintains a sponsorship relationship with the C-rank mage Hye-rin, and is Level 65. Eight Minotaurs approached, causing his team members to retreat while Im Kkeokjeong remained positioned as the front-line tank.",
    "Taekyung defeated all eight Minotaurs, received a Level Up, and established that Changsoo owes him 4 billion won and all byproducts. Changsoo is the Sangdong Guild Master’s son, is nicknamed Horndog, agreed to pay and apologize after drawing his sword, and learned that Taekyung works as both a Hunter and a Murim martial artist."
  ],
  "continuity_sources": [
    84
  ],
  "open_questions": [
    "The identity and sponsor of the assassin who attacked Taekyung and Hyuk Mujin remain unconfirmed, as does any connection between the attack and Song Sword Sect.",
    "It remains unresolved whether Hyuk Mujin will become the next Master of the Gatekeeper Pavilion.",
    "It remains unresolved whether the Shanxi sects will answer Jin Wikyung’s summons and whether he will become Alliance Leader.",
    "The reason the System displayed the same 2-hour-22-minute Time Limit twice remains unexplained.",
    "The nature of the minor misunderstanding that injured Childeuk remains undisclosed.",
    "Taekyung’s prior relationship with Lee Seowol and the missing details of his memories about her remain unclear.",
    "Butler Kim’s former Hunter rank and background remain unclear, and it is unclear whether Song Song heard Taekyung’s interrupted confession.",
    "Whether Im Changsoo fulfills his promised payment, surrenders the byproducts, and gives the demanded apology and damages remains unresolved."
  ],
  "safe_through": 84,
  "temporary_decisions": [
    "Use gongcheong seokyu for 공청석유 with a footnote explaining the elixir and petroleum pun; use junzi for 군자 and Junzi Sword for 군자검 with a cultural footnote; render 도덕책 as ethics textbook with a footnote explaining the pun.",
    "Retain Hyung-nim for 형 and 형님 in Taekyung’s deferential speech; use Three Questions Gorge for 삼문협, Great Hero for 대협, and Ghost Sword for 귀검.",
    "Use Alliance Leader for 맹주 and summon for 소집; use New Year’s Day for 원단 and close the sect’s gates for 봉문.",
    "Use Sleep Mode for 수면 모드, Medicine King Hall Master for 약왕당주, four-horse carriage for 사두마차, and goshiwon for 고시원 with a footnote.",
    "Use Return for 귀환, Returnee for 귀환자, Ren and Du meridians for 임독양맥, Heart Demon for 심마, Paralysis Acupoint for 마혈, and Mute Acupoint for 아혈.",
    "Render fist-and-kicking technique as 권각술, recognition as 인정, Falling Flow Sword as 낙류검, Twelve Gale Fists as 질풍십이권, Flame Divine Palm as 화염신장, and Tendon-Splitting and Bone-Twisting as 분근착골.",
    "Use Reformation Fist, Toughness, Heavenly Martial Physique, Jang Childeuk, Martial Artist Jang, benevolence/righteousness/propriety/wisdom, killed by a tiger, fifteen minutes, lifelong single, Let’s eat noodles, Squad Leader, Third Young Master, Designer-Brand Junkie, Qi Sense, Peace Guild, Essence of the Himalayas, Sooni’s Super, Song Song, Miss Song, Taurus, Ares Guild, Senior, Young Master, Guild Master, Minotaur, Bucheon Terminal Guild, The Minotaur’s Labyrinth, and Shit Changsoo as established.",
    "Use Sangdong Guild, Hunter Association, Black Drake, Masterwork Black Drake Leather Set, Masterwork Black Thorn Spear, Bleeding, artifact, gear advantage, Hye-rin, Cheongdam-dong, Matador’s Full-Body Armor, Matador’s Shield, Taunt, Hallucination, Minotaur Warrior, Top-tier, tongue-pulling hell, big bills, baram wind/infidelity pun, Horndog, Hoengseong, Gangwon Province, Xyliton, and Hongik Ingan as established terminology or translation choices."
  ],
  "version": 1
}

## Reading copies

## Chapter artifact 80

# Chapter 80

Gate Management Office.

A young man in gleaming armor scowled.

“So why isn’t it allowed?”

The public official in charge of the B-rank Gate *The Minotaur’s Labyrinth* looked troubled.

“I already told you. Because of the fatal accident last week……”

“You think I don’t know that? What I’m saying is, why are you being so uptight with someone you know?”

“It’s a safety-inspection period. If you’re short on personnel, I can’t exactly approve your entry.”

The official was at his wit’s end.

Any Gate where a fatal accident occurred was subjected to a week of safety inspections. In other words, they raised the required number or level of personnel to prevent another accident. But the young man in front of him was being completely unreasonable.

“I put in a little extra this time. Good enough?”

“What is this!”

The official jumped at the white envelope the young man thrust out and glanced around in alarm. A new employee who had joined the office recently was staring at him with wide, round eyes.

“You—you can’t do this.”

“Can’t do what? You’ve been taking it just fine until now.”

“……”

“Being in charge of a Gate is supposed to have perks like this, right?”

At the young man’s blatant remark, the middle-aged official’s face flushed red. It wasn’t as if this was anything new, but what kind of disgrace was this in front of a new employee?

Still, the milk had already been spilled. His conscience grew thinner in proportion to the thickness of the white envelope.

“So……how is your team composed at the moment?”

“Ten, including me.”

“Ten?”

“Five B-ranks and five C-ranks. Why? Is there a problem?”

Of course there was. The Bucheon Terminal Guild, which had been involved in last week’s accident, had sent five B-rank Hunters and ten C-rank Hunters into the Gate. What happened to them had been plastered all over the front page of the local newspaper.

> **The Tragedy Brought on by a Shoddy Raid**
>
> **Bucheon Terminal Guild Master to Cooperate Fully with Hunter Association Investigation**

And now they were talking about ten people. Just as the official was hesitating—

“Hey, mister. Hold on.”

The young man’s menacing face had somehow acquired a smile.

“The numbers have to be roughly right anyway, don’t they?”

“Ah, yes. That works.”

“Then let’s take those guys along. Make it look good.”

The official followed the young man’s finger and turned his head. Five men and women had just entered the management office.

*Two middle-aged men. Two young men. And……*

One stunningly beautiful woman.

Judging by how the young man couldn’t take his eyes off her, his intentions were obvious.

“Good enough now?”

After quickly finishing his calculations, the official picked up the envelope.

“No problem.”

* * *

The middle-aged official kindly explained the situation to us.

It was currently a safety-inspection period, which meant that quite a few Guilds were experiencing delays in entering Gates. He even explained that with our current numbers, we would either have to hire mercenaries or join up with another Guild.

“You’re in luck. The people from Sangdong Guild are waiting, and they’re exactly five people short.”

“If we join them, how long will it take until we can enter the Gate?”

“We can process it immediately once you join.”

*That worked great for us.*

Team Leader Choi, who held the real decision-making power, nodded without objection.

“Then that sounds good.”

Just as Butler Kim, the Guild Master, signed the contract, an unexpected voice cut in.

“Nice to meet you. I’m Im Changsoo, the Team Leader from Sangdong Guild.”

His voice was smooth and easygoing, but his build was quite solid.

Unmistakable confidence radiated from him as he strode over.

*Sangdong Guild was strong enough to justify it.*

Sangdong Guild was one of the five leading mid-sized Guilds in the area around Bucheon, with more than twenty B-rank Hunters alone.

He looked to be in his late twenties at most, yet he was already a Team Leader. That wasn’t a position one could luck into over a game of cards.[^1]

*This guy’s no pushover.*

The Qi Sense I activated soon afterward changed my guess into certainty.

> **System**
>
> **Level 65 — Im Changsoo**

And yet, his name sounded familiar. Where had I heard it before?

While I was tilting my head, Butler Kim greeted him.

“Hello. I’m Kim Hwajong of Peace Guild.”

We called him Butler Kim, Uncle, Kim Hyung, and plenty of other things, and we knew he was only a figurehead Guild Master. But from an outsider’s perspective, it was obvious at a glance that he was the person in charge.

Im Changsoo answered with a bright smile.

“Ah, Peace Guild. I’ve heard the name quite a bit.”

Im Kkeokjeong and Miss Song, who were standing beside him, whispered to each other.

“Miss Song, how long has our Guild been around?”

“Hmm. About two weeks, I think?”

“Raids? Have we done many?”

“What are you talking about? We haven’t even started remodeling the Guild house. This is our first official raid.”

“……”

A B-rank Hunter could hear everything, no matter how quietly someone spoke. Im Changsoo’s head turned toward the two of them.

“And who are these people?”

“They’re Guild members.”

His gaze passed over the two of them—briefly over Im Kkeokjeong, then lingering a little longer on Miss Song.

“I see. I said something unnecessary, haha.”

“Not at all.”

“In any case, it seems fate brought us together. Since we’re on the same team now, I look forward to working with you.”

“All right, then. We’ll go change into our gear and be right back.”

“We’ll wait for you in front of the Gate.”

Team Leader Choi watched Im Changsoo’s back as he walked away, his gleaming chainmail clanking with every step. His face was serious.

“That man……”

“Is there a problem?”

“His equipment is limited edition. That stuff is incredibly hard to get.”

“……”

Oh. Right. It did look expensive.

* * *

Hunters were an enviable profession. Partly because they were guardians who had protected humanity from the Great Cataclysm……but mainly because they made a lot of money.

Even I made over 100 million won a year as a lowest-rank Hunter by working my ass off, so that said it all.

*The problem was that they spent a lot, too.*

The single biggest expense was equipment.

Magic Gems went into equipment as a matter of course, so no matter how carefully you considered cost-effectiveness, you couldn’t help but spend a fortune. On top of that, there were regular maintenance costs and repair fees whenever something broke.

The heartbreak was one thing. Your bank balance got ripped apart.

*There was a reason equipment insurance existed.*

In that regard, Team Leader Choi was the best employer ever.

He loaned us high-end equipment for free.

Rumble, rumble.

Team Leader Choi came into the changing room pulling a suitcase and called us over.

“I picked out decent equipment suited to each of your positions. Take one set each.”

It was a small suitcase, the sort you might use for a short trip. Im Kkeokjeong muttered in disappointment.

“Guess there isn’t one for me.”

The corners of Team Leader Choi’s mouth curled up.

“Of course there is. If you knew what this was, you’d be shocked……”

“Oh, this is a suitcase with a space-expansion spell on it.”

“……”

He had guessed it exactly.

My accurate prediction briefly wiped the smile off Team Leader Choi’s face. But he quickly composed himself and continued.

“That’s right. A space-expansion suitcase made by K Company. Nicholas, known as the greatest craftsman in North America……”

Clatter!

“Wow, it really is! Taekyung, look at this. It’s huge inside!”

“It is.”

“World-renowned designers also participated……”

“Wow, I’ve never seen anything like this before. I could probably sleep in here.”

“Once you close the suitcase, you won’t be able to get out until someone opens it.”

“Really?”

“This product keeps stored items in optimal condition through proper temperature control and ventilation at all times……”

Click, click.

“This is awesome. What do you think? Does it suit me?”

“It fits you perfectly. I thought it was a tailored suit.”

“You look good too. What’s that?”

“It says it’s a Black Drake Leather Set? No, it’s a leather set.”

“Really? If it’s Team Leader Choi’s, it must be good. Hahaha! Thanks, Team Leader Choi!”

“……Don’t mention it.”

Team Leader Choi had completely lost the will to fight by then and changed into his equipment without another word. I checked each piece of equipment I was wearing.

*Item Check.*

Ding.

> **System**
>
> **Item Window**
>
> **Masterwork Black Drake Leather Set**
>
> **Type:** Armor  
> **Grade:** Peak  
> **Description:** An armor set made from the leather of the B-rank monster Black Drake. You can feel the hand of a superb craftsman in it.
>
> **Effect:** Strength, Stamina, Agility, Toughness +10
>
> — Full Set Effect is active.
>
> **Item Window**
>
> **Masterwork Black Thorn Spear**
>
> **Type:** Spear  
> **Grade:** Peak  
> **Description:** A spear made from the spine of the B-rank monster Black Drake. It is extremely hard and sharp. You can feel the hand of a superb craftsman in it.
>
> **Effect:** Upon hitting an enemy, Bleeding activates with a 90% chance.

After checking them, I had exactly one thought.

*This is insane.*

An armor set that gave me forty points simply by wearing it, plus a spear that could kill an enemy from massive blood loss with nearly every stab.

The item information alone made it clear how incredible the effects were.

*So this is what gear advantage feels like.*

When I suddenly remembered my time in Murim, tears clouded my vision.

*Armor, my ass.*

I had fought in soft scraps of cloth and broken dozens of cheap spears. The people of Murim were the very definition of hard-boiled—the real tough guys.

“Maybe it’s because it’s designer gear, but it feels different right away.”

I turned my head and saw Im Kkeokjeong hopping up and down in place, his face flushed with excitement.

“It’s incredibly light, and I feel like my body’s faster too. Is it just my imagination?”

“I doubt it.”

There was no way it was just his imagination. Team Leader Choi had prepared this equipment specifically for Im Kkeokjeong, a D-rank Hunter. Of course it was good.

*Should I take a quick look?*

Just as I was about to place my hand on the full plate armor Im Kkeokjeong was wearing, Team Leader Choi approached us, already fully equipped.

“If you’re ready, let’s head out.”

“What about Butler Kim?”

“Out here, he’s the Guild Master.”

At Team Leader Choi’s pointed correction, Butler Kim chuckled.

“It’s fine. Besides……I’m always wearing my equipment.”

As he spoke, he unbuttoned his suit jacket, revealing bracelets on both wrists and a necklace. They were not ordinary accessories, of course.

The necklace was set with a Magic Gem, and the bracelets were etched with strange yet beautiful patterns.

“An artifact?”

“This is more convenient than a staff.”

Butler Kim answered modestly, but it was rare to see a mage dressed so lightly. Most carried at least some light armor or a staff for self-defense to improve their chances of survival.

*He’s probably not an ordinary mage.*

Everyone deferred to anyone who came out of Ares Guild.

I suddenly found myself curious about Butler Kim’s past, but the question was wiped clean from my mind the next moment.

Knock, knock.

“Hey, guys. Are you still not done?”

“Ah, we’re ready.”

It was Miss Song’s voice from outside the changing room. As soon as Team Leader Choi answered, the door opened a crack.

“Hurry up. People will be waiting.”

“Whoa.”

Her long, straight hair was tied tightly up, and she was wearing light leather armor. I swallowed a startled breath at the sight of her.

*Can a person really be this beautiful?*

It wasn’t just love making me see her through rose-colored glasses. That was simply the truth. I knew that much just from seeing Im Kkeokjeong, who had treated her like a cute niece until now, swallow hard.

Gulp.

“……”

*I’d better keep an eye on this guy.*

If even Im Kkeokjeong was reacting like this, the other guys would be no exception. Any young man who seemed even moderately capable would come crawling out by the truckload to hit on her.

*Take Im Changsoo, for example. Im Changsoo, say. Or maybe Im Changsoo……*

Im Changsoo. The young Team Leader from Sangdong Guild.

His face had been hovering in my mind since earlier.

*I was sure I’d never seen him before.*

And yet……why was he bothering me so much? Was it because that punk seemed interested in Miss Song?

“What are you doing? Aren’t you coming out?”

“Ah, yes.”

My thoughts were cut short. At Im Kkeokjeong’s urging, I hurried out of the changing room.

[^1]: Go-stop is a Korean card game traditionally played with a deck of flower cards.
## Chapter artifact 81

# Chapter 81

In front of the Gate, ten men and women dressed as Hunters were chatting in a friendly atmosphere.

“Oppas, we’re really okay, right?”

At the female Hunter’s question, a B-rank Hunter from Sangdong Guild thumped his breastplate.

“Don’t worry. Don’t you trust us?”

“Of course I do. But I heard someone died here last week.”

“Don’t worry about those idiots. They died mouthing off despite not having the skill to back it up. Who can they blame? Right, Changsoo hyung?”

Im Changsoo, who had been listening quietly, exhaled a cloud of smoke into the air.

“If you’re nervous, go home. Don’t make the mood fucking miserable.”

The atmosphere instantly turned cold. The female Hunter who had spoken first forced the corners of her mouth upward.

“No, oppa, I was just—”

“Shut up. What are you going to do?”

“…Sorry.”

“Then go make yourself scarce in a corner. I’ve got more than enough bitches to bring along even without you.”

Despite his rough words and behavior, not one of them dared to object. They merely tried to lighten the mood with awkward smiles.

This sort of thing was familiar—and perfectly natural—to Im Changsoo.

*Idiots.*

Gates were geese that laid golden eggs called Magic Gems, and Hunters were the laborers who harvested them. Born into a family of estate managers, he had started out on a completely different footing.

“If you’re not heading to a hotel right now, quit clinging to each other. It’ll be a pain if another shitty rumor starts spreading.”

“Hyung, these ones are trustworthy.”

“I don’t trust them, asshole. Didn’t you say those last ones were trustworthy too?”

“Well, that was…”

Sangdong Guild might have been a respectable mid-sized Guild that threw its weight around in the area, but it wasn’t powerful enough to ignore public scrutiny. Im Changsoo had already received warnings from his father, the Guild Master, several times for messing with the wrong women.

“Let’s make sure there aren’t any problems, okay?”

“Yes, sir. We’ll bear it in mind. Loyalty!”

“Tsk. You’re good at answering.”

Im Changsoo flicked away his half-burned cigarette. As if she had been waiting for it, someone beside him called out a spell.

“Wind.”

A magically generated breeze sent the cigarette butt and its smell flying far away. The female mage who had cast the spell gave him a charming smile.

“I did good, right?”

Im Changsoo looked her up and down. She had a sleek figure and was an alluring beauty, and the two of them had a sort of sponsorship arrangement.

Despite her outstanding looks, she was a C-rank Hunter with pathetic skills. But the fact that she was the Guild Master’s son’s lover had been enough to get her into Sangdong Guild.

Her house, her car, and countless designer goods—all of them had come out of Im Changsoo’s pocket. But he had never once thought it was a waste.

*Well, that was true until now.*

But today, his mind had changed. Her figure, her looks, her entire air—all of it seemed tacky and cheap compared to the woman he had met about thirty minutes earlier.

*Was her name Song Song?*

Just thinking about her made his lower abdomen feel heavy.

She was a flower far too precious for some pathetic new Guild. He intended to pull her out without damaging a single root and plant her in his own flowerpot.

“Oppa, did something good happen? Why are you smiling like that?”

Im Changsoo didn’t answer. Instead, he waved toward the five people who had appeared in the distance.

“Ah, over here!”

Of course, he didn’t forget to add a quiet remark to his ex-girlfriend.

“Who the hell are you calling oppa, you fucking bitch?”

* * *

That lech—or rather, Im Changsoo—spoke with a bright smile.

“You’ve arrived. Ah, these are my team members.”

The people who appeared to belong to Sangdong Guild bowed their heads.

Including Im Changsoo, there were exactly five men and five women. Every one of them wore expensive, gleaming equipment, and their outfits clearly prioritized design over practicality.

Especially…

*Oh, wow.*

When it came to the female Hunters, I had no idea where to look. Im Kkeokjeong, a married man with two children, whispered with a stiff expression.

“They’re incredible.”

“……”

I almost nodded before managing to stop myself.

Miss Song was looking at us with a displeased expression.

*Come to think of it…*

Was this a raid or a blind date? Handsome and beautiful men and women pairing up, laughing and chatting as they entered a Gate—it was a perfect recipe for getting themselves killed.

Well, judging by their Levels and equipment, they would probably be fine.

“Is everyone here?”

The middle-aged official in charge of the Gate checked our numbers and Hunter licenses. It was one of the procedures we had to complete before entering.

“Sangdong Guild. Five B-ranks and five C-ranks. Correct?”

Im Changsoo gave him a courteous smile.

“That’s right.”

“Then Peace Guild. Two B-ranks, two C-ranks, and…”

The official’s hand paused as he flipped through the Hunter licenses.

“One E-rank? Where is he?”

Im Kkeokjeong thrust up his heavily furred arm.

“Uh, me.”

“What’s your position?”

“Sir, you’re not very observant. Would I carry around a huge brute of a shield like this if I were a mage? Heh heh.”

“You’re a tank.”

The official furrowed his brow.

A tank was exactly what the name suggested: a human shield who stood on the front line and blocked monster attacks. Because of the danger, tanks were among the best-paid Hunters, along with healers. They also had a high fatality rate.

“Why is an E-rank coming here? And he’s a tank, no less? Good grief.”

“You can make a lot in one go. Who knows? If the Magic Gems come tumbling out, we’ll have hit the jackpot.”

“Oppa, we’re really okay today, right?”

“Don’t worry. This oppa will protect you, Hye-rin.”

Murmurs spread among Im Changsoo’s team members. The official who had to let us enter was no exception.

“An E-rank tank…”

Butler Kim stepped forward at the concern in his voice.

“He is a veteran with twenty years of experience. He is also wearing sufficient equipment to prepare for any danger, so I don’t believe there will be a problem.”

“Veteran is good, of course. But you know what happened last week. Two C-rank tanks died. In a situation like this, letting him…”

That was when an unexpected ally appeared.

“Sir, can’t you make an exception?”

It was Im Changsoo. He continued in a soft voice.

“We’ve already signed the cooperative raid contract, and after meeting such fine people, it would be a shame to render it invalid.”

“Well, I mean…”

“If you could be just a little flexible, we’d really appreciate it… Please.”

What a strange guy. The words coming out of his mouth were all gratitude and requests, but his neck was stiff and his manner was high-handed.

The official flinched for a moment, then sighed.

“All right. But Team Leader, you’ll have to keep them under control.”

“Of course.”

*Keep them under control.* What an unpleasant way to put it.

With Im Changsoo’s help, permission was granted, but an ant seemed to be crawling around in one corner of my chest.

*Well, better to let it go.*

Even Im Kkeokjeong, the person involved, looked completely unfazed. It was ridiculous for me to take offense on his behalf.

“You may enter, then.”

At the official’s words, everyone stepped in front of the Gate. Ten Hunters from Sangdong Guild and five from Peace Guild. Fifteen people in total, including no fewer than seven B-rank Hunters—a highly elite raid team.

“Well, then…”

Im Changsoo, who had naturally taken the lead, winked.

“See you inside the Gate.”

Whoosh!

As Im Changsoo disappeared beyond the field of magic, Miss Song muttered,

“What a creep.”

*I agree.*

* * *

Whoosh.

The damp, sticky energy unique to magic wrapped around my body for a moment. When I opened my eyes, a new space unfolded before me.

It was a cavern so vast that it couldn’t even be compared to an F-rank Gate. Three entrances gaped open like enormous maws. It was the place we had seen in the video on the way here.

*The only difference was…*

Ding.



> **System**
>
> You have entered **The Minotaur’s Labyrinth**.
>
> Quest **B-rank Gate Clear** has been created.

There was a System notification that only I could hear. And, on top of that, a Quest.

“All right, let’s check our numbers and equipment one more time before we go in.”

While everyone checked their belongings, I quietly moved to a corner of the cavern and muttered inwardly.

*Check Quest.*

Ding.



> **System**
>
> **Quest**
>
> **B-rank Gate Clear**
>
> You have entered a B-rank Gate for the first time in your life.
>
> Upon successfully completing the raid, you will receive a corresponding Reward. This applies only once.
>
> **Grade:** First Rate
>
> **Restriction:** Jin Taekyung
>
> **Mission:** Clear the B-rank Gate *(Incomplete)*
>
> **Reward:** ???
>
> **Failure:** ???

What a refreshing start.

I had just closed the Quest window with a warm smile when—

“What are you doing over here by yourself?”

A voice suddenly came from behind me. I turned my head and saw Im Changsoo walking toward me.

“Me?”

I thought he had mistaken me for someone else, but he hadn’t.

“You’re Jang Taekyung from Peace Guild, right?”

“I’m Jin Taekyung.”

“Yes, Jang Taekyung.”

I wasn’t sure whether he was deaf or my tongue was malfunctioning, but I nodded for the moment.

*We’ll probably only see each other once, anyway.*

He had helped out over the matter with Im Kkeokjeong, so I still felt a little grateful toward him.

“Did you need something?”

“Haha, it’s nothing I’d call business. This is fate, so I thought we could at least exchange names. You heard my introduction earlier, so you already know who I am. I look forward to working with you.”

Someone once said you couldn’t spit in a smiling face. It was a little awkward, but I clasped the hand Im Changsoo offered with a broad smile on his face.

“Ah, yes. I look forward to working with you too.”

A Team Leader from another Guild—someone I had never even met before—had offered me a handshake first.

I had participated in cooperative raids several times over the past seven years and had plenty of experience as a day-labor Hunter, but this was the first time something like this had happened.

*Then again, I was an F-rank back then.*

In those days, people had treated me like air. Maybe being a C-rank Hunter meant I was finally being treated like a person. It left me with a strange feeling.

*But why me?*

The question was answered almost immediately.

“That’s a Black Drake Leather Set, right?”

“Ah.”

*This guy’s a Designer-Brand Junkie too.*

Im Changsoo looked over my equipment from head to toe and let out one exclamation after another.

“Wow, I’d only ever seen this in pictures. Where did you buy it? Did you order it from overseas? Or get it in Cheongdam-dong?”

“I rented it.”

“You leased it from a company, then. I heard you’re a C-rank Hunter, but can you really keep something like this maintained? Ah, I’m sorry. I absolutely didn’t mean anything by it. Did I offend you?”

*Of course I’m offended, you moron.*

But I wasn’t stupid enough to let my true feelings show so openly.

What Im Changsoo had said was also a cold reality.

*Still, this guy really has no tact.*

I waved a hand with deliberate composure and added a little self-deprecating humor.

“It’s already breaking my back. Every penny I earn goes toward maintenance. The people around me call me crazy.”

“Haha, but is there anything more important than your life? Right?”

“That’s true.”

“Then I suppose the same goes for the others.”

“Sorry?”

“The others. The Peace Guild members. Their equipment looked pretty good too.”

“Did it? I don’t know much about that sort of thing.”

Im Changsoo laughed as if he had heard an amusing joke.

“Come on. That’s not something someone who spends a fortune leasing equipment gets to say.”

The equipment was leased, but it hadn’t cost me a fortune. Team Leader Choi had loaned it to me free of charge. I briefly considered explaining that, but soon abandoned the thought.

*What’s the point of bringing that up?*

Explaining it would just be a waste of breath.

I was already tired of talking about equipment, so I gave him a vague answer.

“They’re all about the same as mine.”

“I see.”

At that moment, one of Im Changsoo’s team members ran over and told him that preparations were complete.

“Oh, dear. We’ve been chatting for too long. I’d better go. I need to check on my team members one last time, and then we should all move together.”

“Take care.”

“Yes.”

Im Changsoo politely bowed his head and was about to leave when he suddenly asked,

“Oh, right. There’s something I’ve been meaning to ask you.”

“……?”

“Have we met somewhere before?”

I would have been overjoyed if Miss Song had asked me that, but hearing it from a male in heavy armor left me feeling less than pleased.

“This is our first meeting.”

“Really?”

“Yes.”

I only thought his name sounded familiar, but this was definitely our first meeting. At my firm answer, Im Changsoo’s smile deepened.

“All right, then. I’ll be going.”

What was that? His final smile rubbed me the wrong way.

As I watched his back, Team Leader Choi approached without my noticing and asked,

“Do you know him?”

“No. He just said he wanted to be friends.”

“He didn’t make a recruitment offer?”

“Not at all. I think he only came over because he’s a gear enthusiast. He suddenly walked up and asked where I bought my equipment.”

“I bought it in Cheongdam-dong.”

“……”

*I wasn’t asking.*

* * *

“Changsoo hyung, why did you suddenly go talk to that bastard?”

“Nothing. His equipment looked decent, so I sounded him out.”

“Holy crap, seriously? Is that stuff really his?”

“Use your brain, asshole. How could a C-rank wear something like that?”

“Then he leased it? Crazy bastard. The maintenance costs must be insane.”

“Leave him alone. It’s cute, watching him overextend himself trying to make something of himself.”

Im Changsoo let out a quiet laugh.

*As expected, they were nothing special.*

It was true that he had felt a little uneasy when they showed up out of nowhere decked out in expensive equipment. If he messed with the wrong people, things could get out of hand.

But now that he had them figured out, he felt at ease.

*Song Song.*

Money and ability. With only those two things, he believed he could do anything. Getting his hands on one woman would be no trouble at all.

“Let’s get moving. Pass it on.”

“Yes, sir!”
## Chapter artifact 82

# Chapter 82

Fifteen people in total. With nearly half of them being B-rank Hunters, it had turned into a lavish raid team—even taking the Gate’s Grade into account.

“Were B-rank Hunters always this common?”

I agreed with Im Kkeokjeong.

“Exactly.”

Before, even when I went looking for them, I had been lucky to catch a glimpse of their coat tails. They had always lived in a completely different world from people like Im Kkeokjeong and me.

“But you don’t seem all that impressed, Taekyung.”

“Me?”

“Yeah. I saw you talking pretty comfortably with that other team leader earlier.”

“I suppose I can do that. We were just making small talk.”

“You suppose? Not long ago, you would’ve broken your neck just trying to raise your head high enough to talk to one of them.”

*Was it really that bad?*

Come to think of it, he wasn’t wrong. I was simply the one who had changed.

*They say the scenery changes when you change where you stand.*

B-rank Hunters. Mountain ridges that I couldn’t reach even by stretching out my hand were now right in front of me.

But the scenery wasn’t as beautiful as I had imagined.

*They’re around Top-tier? No, maybe First Rate martial artists.*

Their Levels, which I had checked with Qi Sense, and the amount of mana I felt from them were both right around that level. Needless to say, I was a cut above them, armed with the System’s cheat-like advantages. Even compared to martial artists of the same Level, they would probably be a step below.

*That’s the difference between martial artists and Hunters.*

Both sides had their strengths and weaknesses, but if they fought with nothing but their bodies, the Hunter would lose every time.

Martial artists learned cultivation techniques that allowed them to use the qi inside their bodies efficiently, then maximized it through martial arts.

*A Hunter would have a chance only after equipping proper gear and using magic, too.*

The conclusion was simple. Martial artists had the advantage in individual ability, while Hunters were superior in group combat and tactics.

And…

*I’m a total cheat character.*

I was a Hunter and a martial artist, a martial artist and a Hunter. I possessed all the advantages of two different classes that were alike and yet completely different.

The frightening part was that I was still growing at an incredible speed through the System.

*This feels a little like becoming the protagonist of a novel.*

Maybe I should write an autobiography after I got old and retired.

*Login Murim.*

Something like that for the title.

To anyone else, it would sound like a fantasy novel.

“Everyone, assemble! Move according to the formation I call out from now on!”

At the shout, Im Kkeokjeong took a deep breath.

“So it’s starting.”

Im Kkeokjeong’s position was tank. He had to protect the team from the front line.

Maybe it was the pressure of a B-rank Gate. His face, which was always smiling, had hardened.

“Can I do this?”

I patted him on the shoulder.

“You can.”

I wasn’t saying it just to make him feel better. The System window floating before my eyes was proof.



> **System**
>
> **Item Window**
>
> **Matador’s Full-Body Armor**
>
> **Type:** Armor  
> **Grade:** Peak  
> **Description:** Armor of the matador, by the matador, for the matador.  
> **Effect:** Strength, Stamina, Toughness +10  
> Against bovine-type monsters, All Stats +20.



> **System**
>
> **Item Window**
>
> **Matador’s Shield**
>
> **Type:** Shield  
> **Grade:** Peak  
> **Description:** A shield of the matador, by the matador, for the matador. Dyed red with bull’s blood, it is eerie just to look at.  
> **Effect:** Strength, Stamina, Toughness +10  
> Against bovine-type monsters, has a chance to activate **Taunt**.  
> Against bovine-type monsters, has a chance to activate **Hallucination**.

*Honestly, I thought it would be impossible at first.*

But this was enough to put my mind at ease. At least here, in The Minotaur’s Labyrinth, Im Kkeokjeong would be able to perform admirably as a tank.

“Hunter Im.”

The sponsor—or rather, Team Leader Choi—approached quietly and spoke with a serious expression.

“Put it on carefully. It’s part of my prized collection.”

“……”

“……”

*He sure knows how to say something nice.*

* * *

Im Kkeokjeong took the lead as the tank. Once Butler Kim, the mage, and Miss Song, the healer, moved to the rear, only Team Leader Choi remained beside me.

“……Why are you looking at me like that?”

Why else? I wanted him to switch positions with Miss Song.

Wouldn’t it be nice to walk side by side, enjoying a pleasant stroll through the Gate? We could even save each other if monsters showed up.

*The heavens clearly aren’t helping me.*

Even when I tilted my head up in lament, all I could see was the damp ceiling of the cavern. Of course, the ceiling was incomparably higher than in an F-rank Gate.

“It’s definitely huge.”

“It’s a B-rank Gate.”

The higher the Grade of a Gate, the larger its internal space and the stronger the monsters that appeared inside. D-rank was as high as I’d ever gone myself, so this was my first time seeing anything higher. That was what people said, anyway.

“In some cases, you even have to climb a snow-covered mountain. I went once two years ago. It was horrible.”

“Oh, did some kind of accident happen?”

“No. The boots I wore weren’t enchanted with waterproofing.”

“……”

“I have cold hands and feet.”

“……”

“Ah, both of those were jokes.”

Of course they were jokes. How could someone above Level 60 have cold hands and feet? I was staring at Team Leader Choi with an incredulous expression when—

*Drrrk.*

“Hm?”

“Is something wrong?”

“Wait. Just a moment.”

Was I imagining things? No.

There had been a faint vibration beneath the cavern floor. It had lasted only a brief moment, but I had definitely felt it.

*Drrrk.*

The second vibration was clearer and more obvious.

Several people had already noticed it and begun watching the area ahead. Im Changsoo was one of them.

“Prepare for battle!”

His short shout was quick and composed. With half his team being B-rank Hunters and all of them equipped with excellent gear, he had no reason to panic.

There was just one problem.

“Watch the holes!”

This was a labyrinth. There were five wide-open holes right in front of us.

It was difficult to determine exactly where the monsters were coming from based on the vibrations in the ground alone.

“Where are they?”

“……”

*Who is Im Changsoo asking? It’s not like the Minotaurs are going to answer him.*

“—Moooooo!”

“There! The hole on the far left!”

“……Is this for real?”

It was a sight I could hardly believe even while watching it.

I clicked my tongue and gripped my spear. The Masterwork Black Thorn Spear—a vicious weapon with a high chance of inflicting Bleeding on its enemies.

“Doesn’t the grip feel great? I applied the finishing coat very carefully—”

*There’s another vicious thing here.*

If Team Leader Choi died, I had no doubt he would fall straight into the tongue-pulling hell.[^1]

The next moment—

*Boom. Boom. Boom.*

“—Mooooooo!”

They burst out of the darkness.

Their bodies resembled humans, but their physiques were too massive to be human, and their muscles were grotesquely swollen.

Rectangular Level windows floated above two horns stained with dust and someone’s blood.



> **System**
>
> **Level 58 Minotaur Warrior**

“—Moooooo!”

They looked far more vivid and imposing in person than they had in the video, but…

“That’s all?”

“There’s only one?”

There really was just one.

*Could that Minotaur have gotten lost in the labyrinth, too?*

“At that level, we should be able to deal with it without ranged support, shouldn’t we?”

“Hye-rin, I’ll be right back.”

The Sangdong Guild members confidently stepped forward. Two tanks and two damage dealers. All of them were B-rank Hunters.

Their intention to show off in front of the women was painfully obvious.

*Oh, you morons.*

Guys like that always fooled around and ended up dead. Of course, that probably wouldn’t happen because of a single Minotaur.

“If you’re going to do it, finish it quickly.”

With Im Changsoo’s permission, the four men drew their weapons and started toward the monster.

That was when—

*Boom. Boom.*

“Hm?”

“—Moo.”

A Minotaur popped out of the second of the five holes.

“Oh, now there are two.”

“That one’s a little smaller. It looks weaker, so you take it.”

“What the hell are you saying? Says the weakest bastard here.”

*Boom. Boom.*

“—Moo.”

The third hole.

“Oh, three. At this rate, this might actually be a pretty fun fight.”

“Anyone who takes even one wound buys drinks tonight. How about it?”

“I’m in.”

“I’m in. The guy who suggests these things always ends up paying.”

*Boom. Boom.*

“—Moo.”

“Ah, shit. What is this?”

“Four might be a bit much.”

“We should probably form up and take them out one at a time.”

“Me too.”

Team Leader Choi, who had been watching the situation, scratched his neck.

“Maybe we should wait a little longer and come up with a strategy.”

“Huh?”

“The holes. Don’t you get the feeling more might come out?”

“No way. It’s not like they’re introducing Olympic athletes.”

*Boom-boom-boom-boom!*

*He was right.*

Lane five—no, the fifth hole—had news for us, too.

The only unexpected part was that this time, it wasn’t alone.

“—Moooooo!”

Maybe it had a lot of friends. Four Minotaurs came stampeding out together.

Including the ones that had appeared earlier, there were eight in total.

Four B-rank Hunters had no chance against that number. Team Leader Choi spoke.

“What do you think?”

“It might be difficult.”

*Difficult, my ass. If you don’t want to die, stay behind the tank.*

I had toned it down for the benefit of the ears around us.

“What about you, Mr. Taekyung?”

“Me?”

“Yes. You, Mr. Taekyung.”

“Hmm.”

The Minotaur, a B-rank monster, was in the mid-to-late fifties in Level.

For a martial artist, that would be close to Top-tier. But if I fought them, I would have to account for all sorts of variables.

Simply put, I would have to fight them to know.

“I’m not sure.”

“You’re not sure…… Do you know something?”

Team Leader Choi stared at me with a strange look in his eyes.

“Most C-rank Hunters don’t answer like that. They wouldn’t take time to think about a question like that, much less take it seriously.”

I felt a sudden twinge of unease.

I had no reason to hide my strength, but I also had no desire to brag about it to the whole neighborhood.

For now, I wanted to avoid attention and keep it as my own secret. A Hunter who was just a little more capable than everyone else. That was all.

“I’ve known this for a while, but you really are an interesting person, Jin Taekyung.”

“No, wait, Team Leader. I think there may be some misunderstanding here.”

I had just begun to speak when—

“Haha, I see. Listening to you, even I’m getting interested.”

Im Changsoo suddenly cut in, his gaze sweeping over Team Leader Choi and me.

“You were having such an interesting conversation that I couldn’t help overhearing some of it. You don’t mind, do you?”

*If we minded, what exactly would you do about it?*

“For a C-rank with fuck-all to his name, you sure had a lot to say about Minotaurs and whatnot. You were practically writing a novel.”

*Ah. So I wasn’t imagining it.*

I looked at Im Changsoo with fresh eyes.

*It suits him.*

Everyone had clothes that suited them. The same went for smiles and attitudes.

That was Im Changsoo in front of me. The mockery gathered in the corners of his raised mouth suited him perfectly. It was practically made for him.

“I didn’t mean to offend you.”

At Team Leader Choi’s characteristically impassive expression and tone, Im Changsoo let out a short laugh.

“Why would I be offended? It’s the truth. These guys are fucking lousy. They only look impressive because people keep calling them B-rank, but among B-ranks, they’re complete bottom-of-the-barrel trash. But……”

Im Changsoo jerked his chin toward me.

“They’re still better than a C-rank. Isn’t that right, Mr. Jang Taekyung?”

I finally said what I had been holding back since earlier.

“It’s Jin Taekyung.”

“Whether you’re Jin Taekyung or Jang Taekyung, I don’t care what your surname is.”

“Then should I call you Shit Changsoo?”

“What?”

“Im Changsoo or Shit Changsoo. I don’t care what your surname is, either.”

The smile disappeared from Im Changsoo’s face.

[^1]: The tongue-pulling hell is a Buddhist hell where liars and slanderers are punished by having their tongues pulled out.
## Chapter artifact 83

# Chapter 83

Im Changsoo’s attention had been fixed entirely on Song Song for some time.

*Damn, she sure knows how to play hard to get.*

He had deliberately kept circling near her and tried striking up conversations in passing several times, but Song Song’s responses had been utterly matter-of-fact.

“Oh, okay.”

“Thank you.”

“I understand.”

For all his effort, the results were pathetic.

*What a difficult bitch.*

They said that when women looked at men, they cared about their faces when they were young, but their bodies and abilities once they got older. Im Changsoo possessed all three, and he had never failed at picking up a woman.

There had been women who became disgusted with his shallow relationships and left first, or ones he had grown tired of and dumped before they could leave.

But he had never encountered indifference like this.

*She sure knows she’s hot shit.*

Even when he grew irritated, the anger slowly melted away whenever he looked at Song Song’s sleek figure and dreamlike face. Her fragrant natural scent, completely different from the smell of other women’s cosmetics, helped, too.

*Don’t get impatient. She’ll fall for me eventually.*

There was still plenty of time. The Minotaur’s Labyrinth was a labyrinth in the truest sense of the word. Raid times could stretch to twice as long as those of other Gates.

That was more than enough time to pick up one woman.

There was only one problem…

*One guy keeps getting on my nerves.*

Choi Minwoo, was it? He looked more suited to a fashion magazine than a Gate. His polished face, his long limbs—even his characteristically impassive expression irritated Im Changsoo.

*The rest are just fucking idiots.*

The old geezer who did nothing but chuckle and the bandit-like middle-aged man were out of the running from the start.

There was one more young guy named Jang Taekyung, but he didn’t even qualify as competition.

*He’s weirdly irritating, though.*

A run-of-the-mill C-rank Hunter. He wasn’t even part of a major Guild, just a small-timer scraping by with high-end equipment he’d leased despite it being above his station. Yet his attitude and way of speaking were strangely confident.

In fact, at the end of their conversation a moment ago, Taekyung had seemed almost annoyed with him.

*Trying to save face, are we?*

With the two irritating bastards, Jang Taekyung and Choi Minwoo, standing together, it was only natural for Im Changsoo to keep his eyes and ears trained on them.

—Mooooo!

It was when the Minotaurs began appearing one after another.

“What do you think?”

“It would probably be difficult, wouldn’t it?”

*Well, look at these bastards.*

Im Changsoo, who had just been about to call his men back, closed his mouth and listened.

“What about you, Mr. Taekyung?”

“Me?”

That was already absurd enough, but the answer that came a moment later was even more ridiculous.

“I’m not sure.”

A C-rank Hunter facing eight Minotaurs, and what? He wasn’t sure?

The bastard would be a corpse within a minute even in a one-on-one fight, but all he had going for him was his mouth.

*Crazy bastards. Go ahead and write a novel.*

Im Changsoo let out a short laugh, then suddenly paused.

An idea had flashed through his mind: this was a chance to humiliate the two men he disliked in front of Song Song.

That was why he abruptly stepped between them.

“You were having such an interesting conversation that I couldn’t help overhearing some of it. You don’t mind, do you?”

He planned to get an apology, laugh at them, and make it unmistakably clear who held the upper hand.

But then…

“Then should I call you Shit Changsoo?”

“What?”

“Im Changsoo or Shit Changsoo. I don’t care what your surname is.”

Shit Changsoo.

Im Changsoo’s brain froze at an insult unlike anything he had ever heard in his life.



* * *

Silence fell all around us.

Sangdong Guild. Peace Guild.

Even the Minotaurs seemed to stop mooing.

In that suffocating silence, the man’s tightly closed mouth finally opened.

“…You little shit.”

At this point, using polite speech would have been ridiculous.

I gave him an equally breezy answer.

“What, you little shit?”

“You really… Are you insane?”

“Everyone on Earth is already spinning. Don’t you know geocentrism, you ignorant bastard?”

“That’s heliocentrism. Geocentrism is the cosmological view that the Earth is fixed at the center of the universe, unmoving, while the Moon, Sun, and planets orbit around it, each traveling along its own celestial sphere…”

*Smack.*

Im Kkeokjeong’s enormous, cauldron-lid-sized hand had approached so quietly that no one noticed it until it clamped over Team Leader Choi’s mouth.

“Mmph. What are you doing? Mmph, mmph.”

…

I wished he would just drop dead right there.

There was a limit to having no sense of the situation. I almost wondered whether Sangdong Guild had paid him.

“I can’t believe I’m talking to people like you.”

Im Changsoo looked at Team Leader Choi and me as if we were unbelievable.

“How did airheaded bastards like you even become Hunters?”

“What, do they recruit based on school transcripts? Get a TOEIC score of 900 and you’re B-rank, and if you can speak Chinese, you’re A-rank?”

“You’d better shut that mouth if you want to live a long time.”

“Wow, threats now? I’m so scared I won’t even be able to piss in Sangdong Guild’s direction.”

Im Changsoo ground his teeth, sparks flying from his eyes.

“You seem to have forgotten… This is a Gate.”

“I know, asshole. I also know that eight Minotaurs are coming toward us from over there.”

They say even a tiger comes when you talk about it.

Right on cue, the bellow of a bull echoed through the cavern.

—Moooooo!

“They’re coming!”

“What do we do?”

“What do you think? Get back! Hurry!”

*Boom. Boom. Boom.*

The cavern floor shook every time the herd of Minotaurs moved.

Watching his team members run back with their tails between their legs, Im Changsoo spat out a wad of phlegm.

“You should consider yourself lucky.”

“I tend to be pretty lucky.”

Thanks to the System, it wouldn’t be an exaggeration to say that I was living a second life. I had gone through enough hardships to die from, but I had always been blessed with incredible luck.

“We’ll see each other after I deal with those bastards.”

“That works, too.”

“I hope you’re prepared to take responsibility for what you said.”

“I think I can handle that.”

I looked at the Level window floating above his head.



> **System**
>
> **Level 65 Im Changsoo**

Level 65. High.

Compared to his other team members, he was nearly ten Levels higher, which meant he was probably quite capable even among B-rank Hunters.

Of course, he still wasn’t as good as me.

*Well, character and ability aren’t proportional.*

Hunters weren’t selected based on TOEIC scores, school grades, or personality tests.

I shook my head and turned away.

“How about now?”

“…?”

“The Minotaurs. Didn’t you say you were confident you could handle them alone?”

Ah. I had a rough idea of what he was getting at.

His intentions were obvious from his tone and expression, and a short laugh escaped me.

“I don’t remember saying anything like that.”

“You should take responsibility for what you said.”

“You’re too childish. I can’t indulge you. If you have a problem, settle it one-on-one after the raid.”

Butler Kim and Miss Song, who had been watching the situation with calm expressions, spoke up as well.

“It would be better if both of you calmed down.”

“Excuse me, but don’t you think this is a bad time?”

*Boom-boom-boom.*

Even now, the Minotaur herd was drawing closer by the second.

It was fortunate that they were approaching cautiously. If they had really wanted to, the battle could have begun long ago.

“You heard them, right? Don’t put innocent people in danger. We’ll deal with this later…”

“Five bills.”

“Huh?”

Im Changsoo spread all five fingers wide.

*That wasn’t five stars… it was five bills.*

Was he talking about the thing I thought he was?

“The Minotaur herd over there. If you handle them alone, I’ll give you five big bills per head.”

“Big bills?”

“Yeah. Big bills.”

That meant fifty million won per Minotaur, or four hundred million for all eight.

Even for me, a C-rank Hunter, that was a considerable sum.

*But…*

I didn’t want to look weak in front of everyone, especially Song Song, by showing how easily money swayed me.

This was a matter of pride!

*Miss Song. Can you hear my heart?*

I gazed deeply into her eyes and answered.

“I refuse.”

Im Changsoo’s eyebrow twitched.

“Even if I give you all rights to the byproducts?”

“No.”

“Magic Gems might come out of them.”

“Still no.”

My answer was as firm as a juvenile court judge’s. Im Changsoo bit his lip.

“What a pointlessly proud bastard. I’m offering four billion won and all rights to the byproducts, and you’re refusing?”

“Get lost… Wait. What did you just say?”

Had I heard him wrong?

All kinds of thoughts raced through my mind. Only after sorting them out could I finally part my lips.

“How much? Four billion won?”

“Didn’t I say? Five big bills.”

…

“Then… five hundred million per Minotaur?”

*You should’ve said five fucking huge bills.*

Four billion won.

The mind-boggling sum left not only me, but Song Song and Im Kkeokjeong, gaping.

*What the hell, is this guy made of money?*

He was the team leader of a mid-sized Guild and a B-rank Hunter, so he probably earned a lot.

But casually offering billions of won like this was absurd.

“You’re just giving me four billion?”

“Just? That won’t do. This is a bet.”

“What kind of bet?”

“I need something to gain, too.”

The corners of Im Changsoo’s lips curled.

“If you die or run away, all the rewards promised so far are void. On top of that…”

His head slowly turned.

His gaze stopped on one person.

“Me?”

“Yes. I’d like to invite Miss Song to join our Guild.”

Im Changsoo bowed politely.

The sudden change in attitude was so different from how he had acted until now that it was downright creepy.

“Ugh, that’s giving me goose bumps. Just act the way you were. It looks much better than putting on a fake act.”

…

…

Song Song had an honest personality.

She shuddered, as if she really had gotten goose bumps, and folded her arms.

“Shit Changsoo—no, Im Changsoo, right?”

“…Yes.”

“Okay. I’ll be blunt. You’re not my type.”

Her blunt declaration came in like a 160-kilometer-per-hour fastball, tight and inside. Im Changsoo’s gaze wavered.

“You’re tall and handsome, but you look exactly like you’d cheat. I hate wind, you see.[^1] I finally got my hair looking nice, and if it gets mussed up… Ah, no, that’s not what I mean, is it?”

“Y-yes? Yes?”

“Anyway, you’re not my type. I absolutely can’t stand womanizers who flaunt their money.”

I had never seen Im Changsoo look so dumbfounded.

To anyone else, I probably had the same expression right now.

“Oh, that look you just had was kind of okay. But I’ve been watching you for a while, and your personality is kind of… You can tell that yourself, can’t you?”

Im Changsoo barely managed to compose his expression before answering.

“We can work those things out one by one.”

“Do you really have to taste something to know whether it’s shit or soybean paste? You don’t seem interested in anything but bumping bellies with me. Am I right?”

“……!”

“……!”

Everyone, myself included, was left gaping.

As if bashful, she toyed with her hair while delivering one line after another, each blow landing like a nuclear bomb.

“It’s not like I particularly dislike Sangdong Guild.”

Im Changsoo, who had been taking hit after hit without a break, brightened and asked:

“Really?”

“Yes. I can always switch again anyway.”

…

*Miss Song, are you a genius?*

After delivering a massive fuck-you with an innocent expression, Song Song continued.

“But I’d need to ask permission before switching Guilds. Right, Guild Master?”

“Ah, of course.”

Butler Kim had been watching with an interested look in his eyes. Song Song turned toward him.

“Team Leader, what do you think?”

“What do you mean? About Song Song switching Guilds?”

“If we lose this bet, that’s what will happen, right?”

Team Leader Choi calmly nodded.

“Go ahead.”

“Isn’t that a little too easy an answer?”

“I answered easily because it was an easy question.”

For just a moment, I thought I saw hurt in Song Song’s eyes.

*No, surely not.*

The emotion had passed too quickly for me to be certain.

Returning to her frank, easygoing self, Song Song turned to Im Changsoo and said:

“Then I’m in on the bet. What about you, Mr. Taekyung?”

“I…”

My deliberation wasn’t short.

From the moment I first heard Team Leader Choi’s question, a strange certainty had already taken root deep in my heart.

The certainty that I was stronger than those bastards.

“I’ll take the bet.”

A smile spread across Team Leader Choi’s lips.

“I’ll join in, too. A bet is more fun when the stakes are high, isn’t it?”

“Wow, look at you, a proper gambler. How much?”

“Four billion won. Of course, I’m betting that Jin Taekyung will take down all eight.”

“What?”

Im Changsoo stared at Team Leader Choi for a moment, then let out a short laugh.

“You’re an interesting bunch. One of you is desperate to get himself killed, and the other is dying to throw away his money.”

“So what’s your answer?”

“Obviously, yes.”

“Should we write up a contract?”

“A contract? What do you take me for? I keep my word once I’ve given it. You don’t have to keep yours. I’ll make you keep it. Everyone, move back!”

The enormous, damp cavern transformed into a Colosseum.

An arena with an absurd amount of money at stake.

I was the gladiator who had to fight the Minotaur herd.

“Team Leader Choi. What will you do if I lose?”

“You will win.”

Where did this confidence come from?

Faith in himself? Or in what he’d seen of me so far?

It didn’t matter.

I would simply do my best to achieve my goal.

*Boom-boom-boom-boom-boom!*

—Moooooo!

Twenty meters ahead, I could see each of them clearly.

Hot breath steaming from their nostrils. Heat. Muscles. Weapons held high.

*This is my first time fighting a cow.*

It should be an interesting experience.

I gripped my spear and charged at the herd like a matador.

[^1]: The Korean word *baram* can mean either “wind” or an affair, making her next line a deliberate pun.
## Chapter artifact 84

# Chapter 84

Im Kkeokjeong thought.

*This is insane.*

Jin Taekyung was a C-rank Hunter. A Minotaur, on the other hand, was a B-rank monster.

And there wasn’t just one of them. There were eight. To Im Kkeokjeong, the situation looked like more than recklessness. It looked hopeless.

*What the hell does money matter?*

Four billion won was certainly enough to change a person’s life, but it wasn’t worth throwing away one’s life for. Im Changsoo had blinded Jin Taekyung with money, and Taekyung had lost his ability to think clearly.

*I have to stop him. I have to.*

Those vicious bastards from Sangdong Guild, Butler Kim for not stopping him, even Team Leader Choi—they were all insane. He had to prevent his cherished little brother from throwing his life away like a stray dog.

“Taekyung!”

It was at that very moment, when Im Kkeokjeong reached out toward Jin Taekyung, who had just gripped his spear at the ready.

Whoosh—

“…Huh?”

Along with the sound of wind, Jin Taekyung vanished. Jin Taekyung began sprinting at a speed that Im Kkeokjeong, an E-rank Hunter, could neither match nor properly see.

It had all happened in the blink of an eye. Im Kkeokjeong let out a dazed sound.

“Uh, uh-oh.”

What was this? What was happening? Had Taekyung always been this strong? No, wait. Could a C-rank Hunter really move that fast?

Whoooooosh!

A black bolt of lightning shot across the cavern.

One step. Two steps. Three steps.

The distance of several dozen meters vanished in an instant, and the spearhead flashed.

Swoooosh! Slice!

The Minotaur—the over-three-meter-tall monster’s enormous body tilted to one side.

The thick neck that should have been above its shoulders was already gone.

For one moment, it seemed as if the half-human, half-beast creature with a human body and a bull’s head were nothing more than an ordinary person.

Thump.

The head that had been severed in an instant dropped to the cavern floor.

Crash.

The headless monster collapsed. Blood burst from the cleanly severed cross-section of its neck.

“What the…!”

Someone’s voice spoke for everyone’s thoughts.

Amid the invisible shock and stunned disbelief, one person grinned.

“This is doable.”

That one remark delivered the final blow.

Im Kkeokjeong’s legs gave out, and Im Changsoo muttered without realizing it.

“Fuck… my four billion.”

* * *

Minotaurs had bodies specialized for close-quarters combat.

Like any mid-sized monster, they were huge, packed with incredibly dense muscles, and armed with heavy weapons such as maces and axes.

Boom!

But what good was that? If they couldn’t hit anything, it was all for nothing.

No matter how hard they swung, all they could do was smash the innocent cavern floor.

*I’ll give them one thing—their strength is impressive.*

But fights weren’t won with strength alone. I slipped inside one monster’s guard and stabbed it in the lower abdomen.

Squish.

> **System**
>
> **Precise Attack!**
>
> **Status Effect: Bleeding activated!**

—Mooooo.

The Minotaur’s cry was pitiful. It had already lost too much blood to charge in as ferociously as before. The attack it had launched moments ago had probably squeezed out the last of its strength.

—Moo. Mooooo.

I approached the creature as it staggered backward.

Looking into its calf-like eyes almost made me feel sorry for it…

*Like hell.*

All I could see was a stack of five hundred million won.

“In your next life, please be born in Hoengseong, Gangwon Province.”

—Mooooo!

Slice.

The Minotaur’s breathing stopped.

A moment later, there were eight enormous pools of blood.

And eight monster corpses.

Ding.

> **System**
>
> **Level Up!**

The cheerful System notification was the movie’s background music. The real highlight of the movie was something else entirely.

I turned around with a wide smile.

“Now, for the fun part—the settlement.”

Among the people engulfed in shock and silence, one person stood out in particular.

I began settling the accounts loudly enough for the half-frozen Im Changsoo to hear.

“Let’s see. Five hundred million per head to start with…”

He flinched.

“One, two, three, four… Eight of them. Four billion in total. Wow, a few of them even dropped Magic Gems. You said all the byproducts were mine, too, right?”

He flinched again. And again.

“Changsoo. Why aren’t you answering? Don’t tell me you lied to me.”

Im Changsoo forced an awkward smile.

“Of course not.”

“Watch your tone.”

“How could that possibly be the case? I was just…”

“Just what?”

“Mr. Taekyung. If you could just listen to me for a moment…”

“Mr. Taekyung? I’ve been meaning to ask you this for a while. How old is our Changsoo?”

“…I’m twenty-five.”

“Oh, my. What a cheeky little shit. You’re only twenty-five, and you’ve been acting so disrespectfully toward your elders?”

“…”

“What happened to your tongue? You kept spitting out casual speech, so I thought you were ninety-five. Why does your face look so weathered? You didn’t just register your birth late, did you?”

As I kept going, Im Changsoo’s face grew bright red with anger.

“Keep that expression under control. If you turn into a Hongik Ingan one more time, I’ll make you genuinely red.”[^1]

“I’m… sorry.”

After barely managing to compose his expression, he cautiously opened his mouth.

“Um, may I ask you one thing?”

“Ask.”

“Are you really a C-rank Hunter…?”

“Yeah. I am.”

Im Changsoo looked at me and the sprawled-out Minotaur corpses in turn, his eyes filled with disbelief.

“What? Why?”

“If you’d rather not reveal it, you don’t have to tell me.”

“Just think whatever you want.”

“Oh, no. That’s not what I meant.”

He said it wasn’t, but there was no doubt he was letting his imagination run wild.

He had thought I was an ordinary C-rank Hunter, yet I had just beaten eight B-rank monsters in a head-on fight.

*That’s right. Imagine away.*

There was nothing to gain from antagonizing Sangdong Guild for no reason. Since they were bowing their heads on their own, I was simply grateful.

“So, perhaps you’re laundering your identity—no, you aren’t. You wouldn’t be. Right.”

Im Changsoo had been about to spout some nonsense, but he glanced sideways at my spear and immediately changed the subject.

This guy’s reactions were kind of fun.

“So?”

“Pardon?”

“Don’t ‘pardon’ me. You have to pay me. Four billion.”

To be honest, I was a little worried that he might tell me to go to hell.

Four billion won wasn’t some random dog’s name. It was a huge sum of money that ordinary people could hardly hope to lay their hands on even after working their entire lives.

But Im Changsoo was different.

“Ah, of course I’ll pay you.”

“…Are you sure?”

“Yes. I keep my promises.”

His answer was so straightforward that it was almost suspicious.

No matter how much money a B-rank Hunter made, there was such a thing as an average income. Yet Im Changsoo talked about billions of won as casually as if it were a thousand-won bill in his pocket.

“You’re not going to disappear after saying that, are you? If you act like none of this matters because there’s no contract, I’ll be very disappointed.”

I casually stroked my spear, and he flinched violently.

“Absolutely not. Absolutely not. I can easily afford that.”

“Hmm. You must make pretty good money. Sangdong Guild treats you well?”

“No. There’s nothing particularly different about my treatment.”

“Of course there isn’t. It’s not like you’re the Guild Master’s son or something. Why would they treat you especially well?”

“…”

“…?”

“…”

Something about the atmosphere felt strange.

I thought about it carefully before asking:

“What’s your father’s name?”

“Im Chunsu.”

“What’s the Sangdong Guild Master’s name?”

“Im Chunsu.”

What a strange coincidence. Im Changsoo’s father and the Sangdong Guild Master had the same name.

Then again, the world was a big place, and there were plenty of people with the same name.

“Hey, I’m only asking just in case, so forgive me for prying…but what does your father do for a living?”

“He’s a Hunter.”

“Just a Hunter?”

“He runs a Guild.”

“Oh, I see.”

This bastard was the Sangdong Guild Master’s son.

A brief silence passed, and in that short interval, I realized what had seemed so familiar about Im Changsoo.

“Are you that guy?”

“A dog?”

“No, I’ve heard about you before.”

It was a story I had heard around this time the year before last and let pass in one ear and out the other.

The Sangdong Guild Master’s only late-born son had awakened as a B-rank Hunter and secured a position in his father’s Guild. But he was such a womanizer that he was apparently a constant headache.

And the nickname he had earned was…

“Horndog. Right?”

Im Changsoo answered by lowering his head.

It was an embarrassing nickname to hear in front of other people, to be sure.

But since I had to collect four billion won, I comforted him in a warm voice.

“It’s okay, man. Guys can be like that sometimes. I used to dream of living like you, too.”

But reality was cold, and that dream seeped into a 100-terabyte USB drive.

Jinho hyung, a renowned authority in the world of adult videos, once borrowed my USB. When he returned, he had a hollow-eyed expression and left me with a one-line review.

*This should be designated a UNESCO World Heritage Site.*

Anyway.

Im Changsoo lifted his head at my warm consolation.

“Really?”

*Of course not.*

Did I look like the kind of guy who hit on just any woman? I was the sunflower of this era, gazing at only one person in the entire world—Miss Song…

*Wait a second.*

This bastard had hit on Miss Song earlier.

“You little shit.”

“Gasp!”

Im Changsoo, frightened before I had even done anything, reflexively placed his hand on his sword hilt.

Shing. Clack.

But the blade had barely made it halfway out before it was forced back into its sheath.

I had moved like lightning, pressing down on his sword hilt while kicking his legs out from under him.

Crash!

When I pressed down on the neck of the man who had lost his balance and fallen, his face went white.

“Ghk! Cough!”

“You little bastard. Where do you get off pulling that thing on me?”

Getting beaten by Jin Mukyung had certainly paid off.

In the past, I wouldn’t have been able to subdue a B-rank Hunter with such a simple, fluid movement. Im Changsoo was probably surprised, but I was even more surprised.

“This is a Gate, you idiot. You already said that yourself. Did you forget so soon?”

“I’m sorry! I’m sorry!”

I wanted to beat him senseless, but since it had only been an attempt, I decided to let him off.

*It absolutely wasn’t because I hadn’t received the four billion yet.*

“Damages.”

“Ghk. What?”

“You drew your sword. Don’t you know that’s attempted murder? And you owe me and Miss Song—no, all our Guild members—a sincere apology.”

“What are you talking about?”

Im Changsoo looked around at the others with an aggrieved expression, but no one came to his aid.

His team members only shrank back whenever my eyes landed on them. Meanwhile, our Guild members, who had been watching the spectacle, took it one step further.

“Drawing a sword on a member of an allied Guild. Well, I never.”

Butler Kim clicked his tongue as if he felt sorry for him.

“You’re only doing this because you don’t want to pay, aren’t you? My goodness, Changsoo, that’s so low. Isn’t it, Uncle?”

“Hmm? Uh-huh. What a nasty young man!”

That was Miss Song and Im Kkeokjeong’s lowlife-and-nasty-man combo.

And then Team Leader Choi delivered the final blow.

“Now, would everyone take a look at my helmet? This product is a custom-made helmet produced by Xyliton, a famous Finnish equipment manufacturer. It has all sorts of functions, but most importantly, it has been enchanted with a video-recording spell…”

Im Changsoo stared at everyone with his mouth hanging open, betrayed and utterly dumbfounded. Then he let out a long sigh.

“I’ll do it.”

“What did you say?”

“I said I’ll do everything you tell me to!”

That was the answer I had been waiting for.

I happily helped him back to his feet.

“Good choice, kid. We can discuss the damages slowly.”

“…This is driving me crazy. If my old man finds out, I’m dead.”

“Would you rather die here?”

“You don’t want the four billion?”

“You’ve got some nerve.”

Im Changsoo let out another deep sigh before opening his mouth.

“May I ask one question?”

“One hundred million per question.”

“…”

“I’m kidding. Go ahead.”

“What do you really do?”

Was he really that curious?

I let out a quiet laugh and answered him.

“Someone with two jobs.”

A Hunter and a Murim martial artist.

The only two-job combination in the world.

[^1]: *Hongik Ingan*, meaning “to broadly benefit humanity,” is a Korean national founding ideal. Taekyung twists the phrase into a joke about Im Changsoo’s reddening face.

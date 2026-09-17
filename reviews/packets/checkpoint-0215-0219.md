# Checkpoint Review — 215–219

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

# Chapters 215–219

## Plot

A Star Guild scheduling mistake redirects the joint Peace–Star Guild raid from Manticore’s Jungle to The Black Wyvern’s Nest, an A-Rank Gate. Despite Taekyung’s trauma from the previous Black Wyvern encounter, the raid proceeds. Won Myunghoon lends Taekyung a Yeti’s Necklace, which Taekyung later equips after Item Appraisal reveals that it attracts dragonkin monsters.

Taekyung kills forty-seven B-Rank Orc Warriors alone, alarming the Star Guild. Won kills a Lv. 97 Green Wyvern, while privately arranging for a stronger monster to appear. After the party crosses the jungle and enters a wasteland, seven scouts encounter a Wyvern identified as a Named Monster. Only Team Leader 1 returns, having abandoned the others under the monster’s Fear. The Gate is confirmed to be an A-Rank Mutated Gate.

Taekyung recognizes the approaching Named Monster as the Black Wyvern that slaughtered his former teammates three years earlier at the Sangdong Station Mutated Gate. The spear wound he inflicted then damaged one of its eyes. Taekyung orders Won and the Star Guild to flee while he keeps the necklace and confronts the monster. He also withdraws his familiar “hyung” address and warns Won not to bare his teeth again, sharply straining their relationship.

## Continuity

- The Peace and Star Guild raid was accidentally redirected to The Black Wyvern’s Nest.
- The raid party is inside an A-Rank Mutated Gate, where monsters can greatly exceed the expected Gate Grade.
- Won killed the Lv. 97 Green Wyvern; Taekyung received no EXP because he did not contribute.
- Taekyung killed forty-seven B-Rank Orc Warriors using an ordinary iron spear.
- Won gave Taekyung Yeti’s Necklace as a personal gift; its Wind of the Snowfield effect attracts dragonkin monsters and marks its possessor as a target.
- A Named Monster Wyvern killed six scouts. Team Leader 1 survived by abandoning them after succumbing to Fear.
- The Named Monster is the same Black Wyvern that killed Taekyung’s former teammates three years earlier; one eye bears Taekyung’s old spear wound.
- Taekyung has ordered Won and the Star Guild to escape and remains alone to face the approaching Black Wyvern.
- Taekyung and Won’s previously friendly hyung-and-younger-brother relationship is now openly hostile or severely strained.
- The immediate unresolved crisis is whether Taekyung can survive the Named Monster and why the Black Wyvern became one.
- The Conception Vessel and Governor Vessel Achievement rewards, Gate Suppression Quest conditions, Star-Array Grand Banquet, Jin Mukyung’s return, Jeok Cheongang’s warning, and the Martial God’s condition remain unresolved.

## Translation Decisions

- Retain “The Black Wyvern’s Nest,” “Black Wyvern,” “Named Monster,” “A-Rank Mutated Gate,” “Yeti’s Necklace,” “Wind of the Snowfield,” “dragonkin,” and “Fear.”
- Render 와이번 as “Wyvern,” 그린 와이번 as “Green Wyvern,” 오크 as “Orc,” 오크 워리어 as “Orc Warrior,” and 트롤 as “Troll.”
- Render 변이 게이트 as “Mutated Gate,” 네임드 몬스터 as “Named Monster,” 레어 몬스터 as “Rare Monster,” and 피어 as “Fear.”
- Retain “hyung” for Taekyung’s address to Won; render the correction from “Myunghoon hyung” to “Mr. Won Myunghoon.”
- Render 힘껏 찌르기 as “Stab with All My Strength.”

## Durable state

{
  "active_continuity": [
    "One Step Back granted Taekyung two level-ups and 20 Bonus Points.",
    "Taekyung opened his Conception and Governor Vessels after consuming three Scorching Yang Qi elixirs.",
    "Taekyung is publicly recognized as Jeok Cheongang’s Disciple and heir to the Fire Gate Clan’s orthodox lineage.",
    "Jin Mukyung remains secluded in the training hall and has not returned to Heaven’s Gate Temple.",
    "The Jin Family received an invitation to the Star-Array Grand Banquet in Henan.",
    "Seong Jinho is staying at Taekyung’s new family home after losing his housing deposit to Kim Jong-su.",
    "Taekyung is an A-Rank Hunter and nationally famous as the Tollgate Hero after the tollgate rescue and KPS interview.",
    "The Peace Guild House has extensive magical communication, observation, and alarm systems, and its website has begun recruiting members.",
    "The media frenzy exposed Taekyung’s family’s personal information, leaving him burdened by the hero label.",
    "Won Myunghoon is a thirty-nine-year-old A-rank Hunter, former ranker and celebrity entertainer, and CEO of the Star Guild in Incheon.",
    "Taekyung and Team Leader Choi cleared The Lycanthrope’s Black Forest after Taekyung killed its Silver-Mane Lycanthrope boss.",
    "A false report claimed Taekyung would transfer to the Star Guild; Won and the outlet issued corrections.",
    "The joint Peace Guild-Star Guild raid was redirected from Manticore’s Jungle to The Black Wyvern’s Nest.",
    "Won killed the Lv. 97 Green Wyvern alone, so Taekyung received no EXP; Won lent him Yeti’s Necklace to attract a stronger monster.",
    "Taekyung killed forty-seven B-Rank Orc Warriors alone, and Im Kkeokjeong was among the survivors he had rescued during an earlier E-Rank Gate attack.",
    "Won gave Yeti’s Necklace to Taekyung, and a Named Monster Wyvern killed six scouts inside the A-Rank Mutated Gate.",
    "Mutated Gates can contain monsters far above the Gate’s expected Grade, and Named Monsters are true monstrosities beyond the A-Rank boundary.",
    "Team Leader 1 was afflicted by Fear, abandoned his team, and returned alone from the Named Monster encounter.",
    "The Named Monster is the same Black Wyvern Taekyung fought three years earlier at the Sangdong Station Mutated Gate, with one eye damaged by Taekyung’s spear.",
    "Taekyung ordered Won and the Star Guild to leave, warned Won not to bare his teeth again, and remained with Yeti’s Necklace as the Named Monster approached."
  ],
  "continuity_sources": [
    219,
    218
  ],
  "open_questions": [
    "What are the rewards for the Conception Vessel Opening Achievement and the rare Achievement earned after completing the Conception and Governor Vessels Quest?",
    "Will Jin Mukyung return to Heaven’s Gate Temple before the appointed deadline?",
    "What event does Jeok Cheongang believe may occur sooner than expected, and why must he endure for several more years?",
    "What is the true condition of the absent Martial God?",
    "Will Taekyung attend the Star-Array Grand Banquet, and what exactly was the answer that changed the three men’s expressions?",
    "What are the Reward and Failure conditions of the Gate Suppression Quest?",
    "How will the Gate near Hwang Cheol Soo’s tollgate ultimately be contained, and what further monsters may emerge?",
    "How will Taekyung and the remaining raid members survive the Named Monster, and what caused the Black Wyvern to become one?"
  ],
  "safe_through": 219,
  "temporary_decisions": [
    "Render 혈도 타통 as “Acupoint Opening,” 회음혈 as “Huiyin Acupoint,” and 임맥 타통 as “Conception Vessel Opening.”",
    "Render 성라대연 as “Star-Array Grand Banquet.”",
    "Render 노야 as “Old Master” when Taekyung addresses Jeok Cheongang privately.",
    "Render 고시원 as “goshiwon,” 오피스텔 as “officetel,” 오우거 as “ogre,” and 게이트 진압 as “Gate Suppression.”",
    "Render 기레기 as “hack reporter.”",
    "Render 원명훈 as “Won Myunghoon,” 스타 길드 as “Star Guild,” 주간 헌터즈 as “Weekly Hunters,” and retain “hyung” for Taekyung’s address to Won.",
    "Render A급 헌터 as “A-Rank Hunter,” 아이튜브 as “iTube,” 태경좌 as “Taekyung the Lord,” 시벌좌 as “Lord Fuck,” and 라이칸스로프 as “Lycanthrope.”",
    "Render 와이번 as “Wyvern,” 그린 와이번 as “Green Wyvern,” 오러 as “Aura,” 만티코어의 밀림 as “Manticore’s Jungle,” 예티의 목걸이 as “Yeti’s Necklace,” 설원의 바람 as “Wind of the Snowfield,” 한서불침 as “Unaffected by Cold and Heat,” 오크 as “Orc,” 오크 워리어 as “Orc Warrior,” 트롤 as “Troll,” 변이 게이트 as “Mutated Gate,” 네임드 몬스터 as “Named Monster,” 디스패스 as “Dispass,” 북한 as “North Korea,” 수령님 as “Supreme Leader,” 마에스트로 as “maestro,” 레어 몬스터 as “Rare Monster,” 피어 as “Fear,” and 힘껏 찌르기 as “Stab with All My Strength.”"
  ],
  "version": 1
}

## Reading copies

## Chapter artifact 215

# Chapter 215

Wyvern.

One of the high-tier monsters classified as dragonkin, along with drakes.

Its body was larger than an airplane’s, its hide was tough, and its intelligence was high enough for it to use magic.

It possessed enough power to be called a small dragon without exaggeration.

The creature I had encountered three years ago was something that could not—and should not—have emerged from an E-Rank Gate.

*“Kyaaaaaaar!”*

I opened my eyes at the monster’s roar, echoing in the distance.

Instead of a dark, humid cave, I saw a clear sky and the familiar faces of the Guild members around me.

“Mr. Jin Taekyung, are you all right?”

“Taekyung.”

At the worried voices, I relaxed my stiff expression.

“Yes. My stomach felt a little queasy. I guess I got motion sickness.”

“Motion sickness? You?”

Motion sickness in a Peak master—or rather, an A-Rank Hunter. Even I knew it was a pathetic excuse.

Even Song-i, who had been keeping a little distance from me lately, asked with concern,

“Would you like me to cast a healing spell?”

“No, I’m fine.”

I gave her a weak smile like the protagonist of *The Last Leaf* and added,

“Just having you next to me is healing enough, Song-i.”

“…Ah. Yes.”

Im Kkeokjeong leaned close to my ear and whispered,

“You bastard. How the hell did you come up with a line like that?”

“Was it bad?”

“No, it was insane. The moment I heard it, electricity shot through my whole body.”

Was it really that effective?

My head had been completely blank, so I had just blurted out the first thing that came to mind.

But judging by Song-i, who had frozen rigidly like someone struck by lightning, it seemed to have worked.

*Why does it feel like I landed a critical hit?*

In the meantime, the throbbing in my temples and the nausea in my stomach both subsided.

Just as I was taking a deep breath, the door of the limousine bus we had been riding in opened, and someone appeared.

“Everyone’s arrived. But…”

Won Myunghoon, whose voice trailed off at the unusual atmosphere inside the bus, asked Team Leader Choi,

“Did something happen?”

“Yes. It’s serious enough that we need to talk.”

Team Leader Choi answered firmly, then turned toward me.

“Mr. Jin Taekyung, you as well.”

* * *

“The Star Guild got here ages ago. Why can’t we see the Peace Guild?”

“Wait. Isn’t that Jin Taekyung?”

“It is. And Won Myunghoon is next to him, so it’s definitely him.”

“Take pictures quickly. Get ready to interview him in a little while.”

Team Leader Choi, Won Myunghoon, and I moved toward a secluded corner.

The gazes of the reporters and Hunters who had rushed over after hearing the news made my face sting.

Finally, once the eyes that had been clinging to us relentlessly fell away, Team Leader Choi spoke with a grim expression.

“What’s the reason for the sudden change of location?”

“Change? What do you mean?”

“Wasn’t Manticore’s Jungle supposed to be today’s raid location?”

“What? That can’t be right. Do you happen to have the contract with you?”

“Here. It’s stated clearly.”

Won Myunghoon hurriedly examined the contract Team Leader Choi handed him. His face twisted violently.

“That bastard, the leader of Team One.”

Judging by his reaction, there seemed to have been a mistake somewhere along the way.

After muttering several curses—unusually for him—Won Myunghoon spoke awkwardly.

“I’m sorry. One of our employees made a serious mistake. I don’t know what to say.”

“A mistake. I see.”

Team Leader Choi’s dry voice continued.

“I think it would be best to call off today’s raid.”

“What?”

“This isn’t just any Gate. It’s an A-Rank Gate. Entering without perfect preparation could lead to an accident. And…”

For a brief moment, Team Leader Choi’s voice trailed off as his gaze brushed over me.

He had already investigated my past.

He knew that I was the sole survivor of the Sangdong Station Mutated Gate incident three years ago, and that I still suffered from its aftereffects.

“Wyverns are still too much for our Guild members. We appreciate the offer, but I think it would be best for both sides if we withdrew here.”

“Team Leader!”

Despite Won Myunghoon’s flustered cry, Team Leader Choi’s attitude remained as sharp as a blade.

“No wyvern. At least not now.”

“…”

That was when I abruptly spoke up, having quietly watched the situation unfold.

“Let’s do it. The raid.”

“Mr. Jin Taekyung.”

“Enough articles have already been posted online, and the reporters have gathered here. If we call it off now, won’t people start talking?”

I stared past Team Leader Choi and Won Myunghoon, standing side by side.

Reporters with cameras hanging around their necks were already edging closer, watching our reactions.

*They have an incredible nose for a story.*

They had clearly sensed the unusual atmosphere and come over to investigate.

So before Team Leader Choi could say anything, I quickly cut him off.

“It’s not that I particularly care about the articles. It’s just that I’m all right now.”

“Are you sure?”

“Yes.”

Half of that was true. The other half was a lie.

I still wasn’t all right. For the past three years, I had relived the same nightmare over and over, remembering the creature’s roar and my teammates’ screams.

Then I would wake drenched in cold sweat, pretend nothing had happened, and repeat the same day as always.

But not anymore.

“I can do this. I’m not the same person I was back then.”

I was no longer the utterly powerless F-Rank Hunter I had been. I was a Peak master and an A-Rank Hunter, someone who could confidently call himself strong wherever he went.

“So it’s fine. No, I want to do it.”

Team Leader Choi stared at me for a long moment before letting out a deep sigh.

“All right. Let’s do it.”

A short while later, we stood before a door of ominously rippling mana.

Cameras recorded the Guild members from both sides as they began the joint raid, while flashes went off without pause.

“Phew.”

I took a deep breath and stepped forward.

Familiar System notifications appeared as sticky mana coiled around my body.

Ding.

> **System**
> - You have entered **A-Rank Gate, The Black Wyvern’s Nest**.
> - A Reward commensurate with your performance will be granted upon clearing it.

Ssshhh.

When I opened my eyes again, everything around me had changed.

* * *

“Huff. Huuuff.”

Im Kkeokjeong, clad in thick, solid plate armor, panted raggedly.

An hour had passed since we entered the Gate, and sweat was already pouring down his forehead like rain.

But he wasn’t the only one. Most of the more than twenty people from the Star Guild and Peace Guild were walking with sweat streaming down their faces.

*It was understandable.*

I clicked my tongue and looked around.

Under the blazing sun, a jungle formed from trees dozens of meters tall and bizarre-looking plants stretched endlessly into the distance.

The sight alone was enough to make it hard to breathe, and the air—hotter and more humid than a steam sauna—completed the picture.

*A primeval forest.*

It looked exactly like something from a dinosaur documentary.

Setting aside the weather, the scenery itself was spectacular.

“Wow.”

Just as I let out an involuntary exclamation, someone approached and tapped me on the shoulder.

“You look relaxed.”

“Oh, Myunghoon hyung. Weren’t you at the front?”

Our formation had Won Myunghoon at the front, me in the middle, and Team Leader Choi and Butler Kim at the rear.

At my question, Won Myunghoon flashed his white teeth in a grin.

“You have to check behind you sometimes. Everyone’s struggling, and I saw some carefree guy sightseeing by himself, so I came over.”

“What if a wyvern suddenly jumps out?”

“We’re still in the jungle zone, so only minor monsters will appear. Wyvern nests are on cliffs or peaks, so we’re still a long way from one.”

“Seriously?”

“It’ll take at least half a day to encounter a wyvern, or a full day if we’re unlucky. Enjoy the scenery while you can.”

I had known that higher-level Gates were larger, but I hadn’t expected this. I shook my head in disbelief.

“This is incredible. No wonder they give people raid access for a full week.”

“That’s how long it takes. If you visit a few A-Rank Gates like this, you’ll get sick of them.”

“I don’t know.”

I probably wouldn’t.

To me, a Gate had long since stopped being a tiring, tedious workplace. It was a place where I could grow even stronger.

“I’m having fun.”

“…Well, I suppose that’s possible.”

Won Myunghoon looked at me strangely before handing me something.

“Here. Keep this.”

“What is it?”

It was a necklace set with a blue jewel. Before I could inspect the Item, Won Myunghoon continued,

“It has a cold spell on it, so wear it. You’re an A-Rank, so you’ll be fine for now, but the heat will drain your Stamina later. You’re a key combat asset, so you need to conserve your strength.”

“You don’t have to give me something like this, hyung.”

“I’m not giving it to you. I’m lending it to you. Take good care of it and return it later.”

It looked incredibly expensive at a glance.

I hesitated, but at Won Myunghoon’s urging, I had no choice but to put it on.

Ding.

> **System**
> - You have equipped **Yeti’s Necklace**.
> - A wind from the snowy plains flows from the necklace.

At the same time as the System notification, a chill cold enough to send shivers down my spine wrapped around my entire body.

“It works well.”

“It suits you. Keep wearing it from now on. I’m going to deploy the scouting team.”

Won Myunghoon smiled with satisfaction and strode away. The moment his back disappeared from view, I took off the necklace.

*I told him I’m really fine.*

Maybe Won Myunghoon had taken my words as modesty, but I had only been stating a fact.

In the Murim, I had opened my Conception and Governor Vessels and obtained something far better than the *Yeti’s Necklace*.

*Unaffected by cold and heat.*

That was why I hadn’t broken a sweat so far. In fact, it wouldn’t matter if one hour turned into ten.

This level of heat couldn’t affect me at all.

It would be much better to give it to someone who needed it more than I did.

“Uncle.”

“Huff, huff. What?”

Im Kkeokjeong, who had been walking a few steps ahead, turned around. Sweat poured down him as if someone had installed a sprinkler on the top of his head.

“Why are you sweating so much? Are you all right?”

“…Do I look all right?”

“No.”

“Don’t talk to me. I’m dying here.”

“You should’ve worn something cooler. Team Leader Choi has plenty of magical Equipment.”

“I thought we were going to fight a manticore, so I prepared for maximum defense. At this rate, I’m going to end up attending my own funeral.”

“That won’t do. You have a wife and children.”

I gave a quiet laugh and put the necklace around his neck myself. Im Kkeokjeong’s eyes widened as he felt the cool wind from the snowy plains.

“Huh? What’s this?”

“A present. Of course, I’m not giving it to you. I’m only lending it to you while we travel.”

“Whew. I don’t know what it is, but I can finally breathe.”

His exhausted face suddenly came alive. Just as Im Kkeokjeong beamed at me, it happened.

—Peeeeep!

A sharp cry rang out from somewhere.

The birds hiding in the dense forest burst into flight, and branches and leaves came crashing down over everyone’s heads like a torrential downpour.

But no one, including me, paid them any attention.

—Kyaaaaaaak!

Along with a cry that raised goose bumps, a massive shadow enveloped the roughly twenty people.

I looked up and spotted a shadow circling high above, so high it was almost impossible to see.

“Wyvern…”

Won Myunghoon had been wrong.

Not half a day. Not a full day.

In only one hour—

It had appeared.
## Chapter artifact 216

# Chapter 216

The moment I saw the Wyvern circling through the air, only one thought came to mind.

*It’s small.*

From head to tail, it was more than twenty meters long, with a massive body and wings, but it didn’t intimidate me in the slightest.

Maybe it was because of that thing three years ago.

*Did I get stronger? No. That thing was much bigger and stronger.*

That one had been pitch-black all over. By contrast, the Wyvern circling overhead now had a bright green body.

Won Myunghoon, leading the group, announced its identity in a powerful voice.

“It’s a Green Wyvern! It’s a relatively weak specimen, so everyone stay calm!”

A man in his early thirties drove a tower shield into the ground and shouted,

“Formation!”

At the command of Star Guild’s second A-Rank Hunter and Team Leader 1, the tanks rushed forward and formed a wall of shields.

“Taekyung, watch yourself!”

After hurriedly throwing out a word of warning, Im Kkeokjeong joined the tanks’ wall with a spirited yell.

Boom! Boom-boom-boom!

The first row, then the second. Large, beautiful tower shields overlapped layer by layer, forming a curved defensive barrier.

The waiting mages and healers began chanting their spells.

“Wind imbues you. Haste!”

“Power that shatters stone. Strength!”

“Restore life to the weary body. Healing!”

Bright motes of light spread outward like dandelion seeds.

At the same time, a System notification rang out.

Ding.

> **System**
> - Your physical abilities have temporarily increased due to the effects of magic.
> - **Agility** has increased by 10!
> - **Strength** has increased by 10!
> - Fatigue has been recovered!

There was a reason people called mages and healers “iron rice bowls.”[^1]

The so-called three-drug combo of buff spells was far more effective than I had expected.

*Is it because they’re all B-Rank?*

The Hunters gathered here were all assets who would be welcomed wherever they went.

But the Green Wyvern flying overhead and watching for an opening was no easy opponent either.

It was an A-Rank monster, after all.

“Kyaaaaaaak!”

With a shriek that tore through the air, it opened its enormous jaws.

The next moment, green slime that stood out even from a distance came pouring down like a torrential rain.

“It’s poison!”

“Scatter!”

Some people took cover behind the tanks’ shield wall, while others threw themselves toward nearby cover.

I was one of the latter. The moment I hid behind a boulder as large as a house, green rain blanketed a radius of more than thirty meters.

Thut-thut-thut. Ssssss!

Poison. Acidic poison, at that.

The moment it touched the surface of the rock, holes began appearing everywhere, and an indescribably foul stench stabbed at my nose.

*So this is what a Wyvern is like.*

Even a tiger cub is still a tiger.

The Green Wyvern was supposedly a relatively weak specimen among its kind, but the speed at which it spewed its poison was frightening, and its acidity was tremendous. If they had been mediocre mid- or low-level Hunters, they would have melted along with their Equipment.

“Team Leader 1. Casualty report.”

“None.”

Most of the people gathered here were B-Rank Hunters.

Even Im Kkeokjeong, the only weak link, was a veteran with twenty years of experience.

His deficient physical abilities were made up for by Team Leader Choi’s top-tier Equipment, so no one had suffered any damage.

“As expected.”

Won Myunghoon nodded with satisfaction, but the Green Wyvern was furious.

“Kyaaak! Kyaaaaaaak!”

The Green Wyvern glared at us through vertically slit pupils before suddenly folding its wings.

Its massive body, which had been leisurely ruling the sky, tilted toward the ground and began a steep dive.

Whoosh!

The sight of the Wyvern plunging down from several hundred meters in the air brought a plane crash to mind.

We could at least block the acidic poison with shields, but if that thing collided with us, we would be done for.

Terrified by a situation he had never encountered before, Im Kkeokjeong screamed,

“Honey! Jinwoo! Sowon!”

At this rate, he would start calling out his father’s cousin next.

Unlike Kkeokjeong, however, the Star Guild members remained calm.

Won Myunghoon even flashed me a broad grin.

“Taekyung, want hyung to show you something cool?”

“…Now?”

“Yeah.”

Wouldn’t it be better to order everyone to scatter?

There were still several dozen seconds before impact, but how could he be this relaxed?

“Watch carefully. It’ll help you.”

After tossing out that remark, Won Myunghoon adjusted his grip on his spear, holding it in reverse.

“Hup.”

Veins bulged over his dense muscles, and an immense amount of mana surged into his spear like a rising tide.

At the same time, a faint line of light appeared along the spearhead.

Ssssss.

It was Spear Energy—a powerful concentration of mana known as Aura in the modern world.

“Kyaaaaaau!”

Perhaps sensing that power, the Green Wyvern twisted its body with a roar.

It turned precisely toward the direction where Won Myunghoon and I were standing.

And then—

Thud! Boom!

Won Myunghoon kicked off the ground and charged forward. One step, two steps, and finally, three.

The Green Wyvern, which had been no more than a black speck moments ago, was now only a few meters above us. Its enormous green eyes, each as large as a basketball, flashed, and its jaws opened wide beneath its rough scales.

Just as its sharp teeth were about to descend upon its small prey—

“Hah!”

With a powerful shout, light shot from Won Myunghoon’s grasp.

Whoosh! Crash!

A spear wreathed in Aura pierced through the Green Wyvern’s neck. Red blood and green acidic poison burst out like a fountain.

Sssss!

As the sound of flesh burning filled the air, its pupils contracted and its body, stretching dozens of meters, writhed.

“Kiiiik! Kiiiiiik!”

Boom! Crash-crash!

Rocks and trees alike shattered and went flying.

The Green Wyvern’s wings trembled as it writhed in pain.

Only a few seconds later, its tail, which had been held rigidly upright, dropped limply to the ground.

“Kiiiuuu…”

With its dying cry, the light vanished from its savage eyes.

Then, as if to prove its death, a System notification rang out.

Ding.

> **System**
> - You have defeated **Lv. 97 Green Wyvern**!
> - No EXP has been awarded because you made no contribution!

Of course. This was the achievement of one person alone.

I dismissed the holographic window in front of me and saw Won Myunghoon pulling his spear from the Green Wyvern’s corpse.

“As expected of our Guild Master!”

“A ranker really is on another level. That Aura was something else!”

“What ranker? That was a long time ago.”

Won Myunghoon grinned at the cheers ringing out from every direction and approached me.

“Did you watch carefully?”

“Yes.”

“Was that your first time seeing Aura in person?”

“Um… yes.”

“Haha. You must’ve been surprised, if you’re even stammering.”

A gravelly voice suddenly cut in.

“Who wouldn’t be?”

It was Team Leader 1, Star Guild’s second-in-command and the main tank of today’s raid team.

He looked like a weasel. Tapping me lightly on the arm, he continued with a shameless grin.

“When I first saw it, I thought, ‘What the hell is that?’ There’s a reason people say you have to know how to use Aura to be a true A-Rank Hunter.”

Won Myunghoon deliberately furrowed his brow.

“Quit buttering me up, punk. You’re embarrassing me.”

“Aw, what flattery? It’s the truth. Am I exaggerating just because you’re skilled? Hunter Jin Taekyung, don’t you agree?”

“Uh… yes.”

“There you have it. I’m not the only one who thinks so.”

I licked my dry lips, not knowing what to say. Fortunately, before the atmosphere could become awkward, Won Myunghoon spoke.

“You’d be perfect if you weren’t such a flatterer. Once you’re done buttering me up, have the guys handle the cleanup. Check the Equipment again, too.”

“Understood, Guild Master. Loyalty!”

After giving an exaggerated salute, Team Leader 1 turned away.

“That guy’s always like that. He’s flighty and careless enough to even send the wrong contract…”

Won Myunghoon’s voice trailed off as he watched Team Leader 1 walk away.

“But, Taekyung.”

“Yes?”

“Are you all right? Why have you looked like that this whole time?”

“…It’s nothing. I was just a little surprised.”

“Is it because of the Wyvern? Well, this is your first A-Rank Gate, so it’s understandable. You’ll get used to it.”

“…”

I swallowed the words that had risen to my throat. I finally understood how the barber who saw the king’s donkey ears must have felt.

*That wasn’t what surprised me.*

Trying not to reveal how confused and frustrated I felt, I looked at Won Myunghoon.

He was tall and lanky, with a youthful face that made it hard to believe he was nearly forty.

But the real reason I had admired him wasn’t his handsome appearance or his catchy hit songs.

*An A-Rank Hunter, master of the spear. And a ranker.*

For a very long time, the idol in my heart hadn’t been Star Won Myunghoon, but Hunter Won Myunghoon.

That was why I had chosen a spear when I began working as a Hunter, and I had read and reread the spear manual Won Myunghoon had written during his ranker days until it was worn to pieces.

But…

*Why is he so weak?*

The reason I had remained still from beginning to end was simple.

I wanted to see Won Myunghoon’s combat with my own eyes.

But it was beyond anything I could have imagined—in an entirely different way.

*His movements are slow as hell, he’s all swagger and no substance, and it’s not like he even knows how to use Aura properly.*

Watching him had nearly given me a stroke.

Had Won Myunghoon always been this weak? Or had he regressed?

There were questions everywhere, but if I had to summarize my thoughts in one line, it was this:

*What the fuck is this?*

It was unfair. There was no particular reason for me to feel wronged, but somehow I felt spectacularly cheated!

It was like reserving a seven-star hotel course meal and being served braised boneless pollock and beef bibim sauce.

*This isn’t what I had in mind. It really isn’t.*

Won Myunghoon, unaware of my feelings, still wore a relaxed, confident smile.

“By the way, where’s the necklace? I don’t see it.”

Was the necklace really the issue right now?

Overcome by an inexplicable sense of emptiness, I answered carelessly.

“…I put it in my pants pocket.”

“Why?”

“Just because. It was getting in the way. Why?”

“No, it doesn’t matter. Just make sure you keep it safe.”

Won Myunghoon’s gaze flicked toward my lower body. After confirming that the pocket of my tight leather pants was bulging, he added,

“Don’t lose it. Got it?”

“Yes.”

There was no way I could lose it. No—if I did lose it, there would be no reason for me to keep living.

*My stuff is precious.*

It was a good thing my body in the Murim and my body in reality were the same.

When I thought of the black anaconda coiled inside my pants, my gloomy mood improved a little.

* * *

While the Hunters dismantled the Green Wyvern and cleaned up the area, Won Myunghoon and Team Leader 1 moved to a secluded spot.

“That necklace works well.”

Team Leader 1 grinned.

“It was difficult to get. Even magical scans don’t detect it.”

“Yes, you did well, but…”

Won Myunghoon suddenly furrowed his brow and continued.

“It’s more effective than I expected. We haven’t even left the jungle yet, and a Wyvern has already appeared.”

“Couldn’t it just be a coincidence? It’s not that rare.”

“It was a coincidence eight years ago, too.”

“…What choice do we have? A Gate is a place where you can’t predict even an inch ahead.”

“That’s why I hate Gates. With people, you can more or less figure out what the bastard is thinking. But you can’t do that with this fucked-up space.”

Won Myunghoon answered in a low voice and looked around.

Everywhere he looked was filled with grass, trees, and strange insects. He wanted to return to the forest of buildings as soon as possible.

“Let’s get started soon. Something bigger and stronger than a Green Wyvern needs to show up.”

“So the surviving witnesses can testify?”

“You’re a smart bastard. Tell you one thing, and you know ten.”

A smile formed at the corners of Won Myunghoon’s mouth.

[^1]: “Iron rice bowl” is a Korean expression for a secure, dependable job.
## Chapter artifact 217

# Chapter 217

Bean sprout soup might not look like much, but more ingredients went into it than people expected.

In that sense, *The Black Wyvern’s Nest* was like bean sprout soup.

This expansive A-Rank Gate contained more than just Wyverns. There were several different species of monsters, just like the ingredients in bean sprout soup.

—Kweeeek!

At the faint sound of a pig squealing in the distance, I muttered,

“…Does bean sprout soup have pork in it?”

Won Myunghoon, who was walking beside me, turned and asked,

“Hm? Where did pork come from all of a sudden?”

“Nothing. I thought there might be a monster nearby.”

“A monster?”

Won Myunghoon stopped and listened for a moment before speaking.

“I don’t hear anything.”

“Uh, well…”

How was I supposed to explain this? While I was thinking, Won Myunghoon smiled and opened his mouth.

“Haha, you seem tense. Don’t get scared just because this is an A-Rank Gate. Relax.”

“I definitely heard it…”

“You must have imagined it. If there had been a sound like that, I would’ve noticed it first.”

Faced with his confident tone and smile, I closed my mouth.

Won Myunghoon was a famous star, but his reputation as a Hunter was considerable as well.

Being a ranker meant being among the top one hundred out of the tens of thousands of Hunters in Korea.

Compared to him, I was still nothing more than a rookie who had only just begun to stand out.

*On the surface, that is.*

There probably wasn’t anyone in the entire world with as many secrets as I had.

But people only saw what was visible and heard what they wanted to hear.

I swallowed the words that had risen to my throat and nodded.

“I guess I imagined it.”

“That happens. Being cautious is good, but don’t worry too much. We’re using detection magic as we move, anyway.”

“…”

I stared blankly at Won Myunghoon as he lightly patted my shoulder, as if he knew everything.

Ever since I had started watching him, I had felt… how should I put it? A complicated feeling in one corner of my heart.

*Was this all there was to him?*

A few hours earlier, while watching Won Myunghoon face the Green Wyvern, I had realized two things.

First, Wyverns weren’t as strong as I had expected. And second—

*Hyung isn’t either.*

He was strong. There was no doubt about that. He could use Aura, and he had once been skilled enough to rank among the top one hundred.

By Murim standards, it wouldn’t have been unreasonable to call him a Peak master.

But that was all. No—if what Won Myunghoon had shown was everything he could do, he was actually inferior to a Peak master of the Murim.

*He doesn’t know how to wield his strength properly.*

Was it because the environments were different?

Unlike the modern world, the Murim was a brutal place where people had to survive with nothing but a single weapon.

It was a world where swords were closer than laws, so martial arts had inevitably developed to an extreme degree.

*Modern Hunters, on the other hand, focus on raids, and magic exists.*

Martial artists who constantly honed themselves within the vast framework of martial arts, and Hunters who divided up their roles and pursued maximum efficiency within them.

It wasn’t a question of right or wrong, but one thing was certain.

*If you compared individual martial strength, Hunters couldn’t stand against martial artists.*

If everything he had shown so far was all he could do, Won Myunghoon was no exception.

Even if he could use Aura, it made no difference.

*I really have grown stronger.*

Only a few months had passed.

I had grown enough to assess an A-Rank Hunter who had been my idol for years.

*It made me happy, but it also left a bitter taste.*

That was when I was immersed in these strange thoughts about Won Myunghoon.

—Kweeeek!

—Kweeh!

The second monster cry was louder and clearer than the first.

Won Myunghoon finally noticed it too. He turned and began searching for the source of the sound.

“Where in the world did that just come from…?”

I pulled the spear shaft from my back and answered,

“Five o’clock. About thirty jang away—or rather, a hundred meters.”

“Huh?”

“There are quite a few of them. You should start preparing for the raid.”

“P-Preparing?”

“Yes. It sounds like about forty or fifty.”

“What are you—”

Won Myunghoon couldn’t finish.

We had spotted a group of more than forty Orcs approaching through the dense undergrowth.

“There are forty-seven. Should I just take care of them?”

“…”

“Hyung?”

At my call, Won Myunghoon jolted as if waking from sleep.

“Uh, huh?”

“Should I take care of them?”

“…By yourself?”

“Yes. I haven’t warmed up yet.”

“R-right. Do whatever you want.”

“If any of them try to run, please take care of them.”

I finished speaking, swung the spear shaft around a few times, and walked toward them.

It was an ordinary iron spear, the kind that could be found anywhere, with no magic cast on it.

*If I use enchanted Equipment for no reason, I’ll have trouble adapting in the Murim.*

Magic was an astonishingly convenient and useful ability.

But while it might be a positive factor for now, it would become a negative one in the long term.

I needed to build up my fundamental abilities rather than rely on Equipment if I wanted to deal with any crisis.

*If I take down all of them, maybe I’ll level up once.*

With that happy thought, I kicked off the ground. The splitting wind shook my hair.

Whoooooosh!

* * *

Whoosh! Sslice! Boom-boom-boom!

The spearhead cleanly sliced through an Orc’s throat.

Before the Orc’s knees even touched the ground, the head of another Orc beside it exploded.

Then another, and another two, followed by three…

Every time the silver line traced an arc, blood and death poured forth.

He tore through their ranks unhindered.

“…Wow.”

Team Leader 1 unconsciously let out a gasp of admiration before hurriedly closing his mouth. Won Myunghoon was glaring at him with a murderous look.

“Uh, CEO. That’s not what I—”

“You bastard. Is this the time to stand there and enjoy the show?”

“I’m sorry. It just slipped out.”

Team Leader 1 glanced around cautiously before speaking again.

“No, but he really is good, isn’t he?”

“…What do you mean, good?”

“His movements are on a different level. He isn’t an ordinary A-Rank rookie.”

“…”

“From the looks of it, he isn’t wearing a single piece of magical Equipment, either. You have to give him credit just for having the guts to charge into fifty Orcs alone. If someone told me to do that… honestly, I’m not sure I could.”

Won Myunghoon licked his lips with an irritated expression.

He couldn’t deny anything Team Leader 1 had said. No, every word had been completely accurate.

The longer Won watched Jin Taekyung, the more his bewilderment grew.

*What the hell is that guy?*

Orcs might be treated like punching bags in fantasy novels, but they were by no means easy monsters.

There were many different Orc species, and dozens of confirmed tribes. Judging by the crude armor they were wearing, the Orcs before them were Orc Warriors belonging to the B-Rank.

And yet Jin Taekyung was overwhelming them.

*He’s fighting fifty Orc Warriors alone? A brat who only just awakened as an A-Rank?*

Won had already investigated him thoroughly.

Jin Taekyung had been a bottom-tier Hunter branded as defective, someone who had started as an F-Rank and was certain to die as an F-Rank.

How could someone who had only fought goblins in tiny F-Rank Gates do this?

“Guild Master. Guild Master?”

Won Myunghoon came to his senses and answered in a dry voice.

“What?”

“Didn’t you hear me? I’ve been asking you for a while whether you noticed anything suspicious, since you’ve been standing beside him the whole time.”

“Suspicious?”

“Yes. It’s strange. That Jin Taekyung bastard definitely has something going on.”

“…”

After a brief silence, Won Myunghoon gave Team Leader 1 a short explanation of what had just happened.

“He knew the Orcs were coming?”

“Lower your voice. We aren’t the only ones here.”

Team Leader 1 glanced behind him. After checking the Peace Guild members watching the battle with peaceful expressions, as if they had come out for a picnic, he whispered in a voice barely louder than an ant.

“My God. How did that bastard know? Can you think of anything?”

“It must have been detection magic. It has to be detection magic.”

“What if it wasn’t detection magic?”

“What?”

Team Leader 1 swallowed nervously.

“Guild Master, what if—this is really just a one-in-a-million possibility, but…”

“Shut your mouth. I’m not listening to your nonsense.”

“W-we can’t rule it out.”

A strange light flashed in Won Myunghoon’s eyes.

“Fuck… Are you saying that bastard Jin Taekyung is stronger than me? Is that what you’re trying to say?”

Overwhelmed by his murderous momentum, Team Leader 1 hurriedly lowered his head.

But Won’s low, growling voice continued to bore into his ears.

“You think I learned Aura by playing Go-Stop? I took in that bastard when he had nothing and raised him, and now he thinks I’m a joke? Does the title of ranker look like a fucking joke to you?”

“N-no, sir.”

*You should at least get your facts straight. When we first met, you and I were about the same. And your ranker status was only the result of the recognition you built in the entertainment industry and an enormous amount of lobbying.*

Team Leader 1 swallowed down the words rising in his throat.

They had been together for well over ten years. There were too many things they had gone through together to turn back now.

Sensing that, Won Myunghoon glared at him with the eyes of a venomous snake.

“Our Jonghun’s all grown up.”

Being called by his name instead of his position carried another meaning.

Several Star Guild members sensed the dangerous atmosphere and moved around the two of them with practiced ease, blocking them from outsiders’ view.

“Hey, Kim Jonghun.”

Tap, tap.

Won Myunghoon lightly patted Team Leader 1’s cheek and muttered in a voice drier than sand,

“Get a grip. If you make a mistake here, we’re all fucked.”

“…Yes, sir.”

“Send a few agile guys to find the boss monster. If that doesn’t work, drag over a few Wyverns that look strong enough.”

“Understood.”

The moment Team Leader 1 answered with a cowed expression, cheers erupted from somewhere.

A middle-aged man with a bandit’s beard was leaping up and down like a live fish.

“Taekyung! You bastard! You magnificent bastard!”

The battle was finally over.

It had taken only about fifteen minutes to wipe out around fifty B-Rank monsters—the Orc Warriors.

Amid the dozens of corpses strewn across the area, a young man with sharp, well-defined features was grinning.

“Ah, I’m finally warmed up. Myunghoon hyung, I did well, right?”

“……!”

Won Myunghoon hurriedly turned his head to hide his face, which had become horribly twisted before he knew it.

*Goddammit…!*

Every time he looked at Jin Taekyung, his head grew hot and his stomach churned.

A guy who had only attracted media attention because of sheer luck. A guy who had received that kind of fortune but didn’t know how to use his fame properly—or even intend to.

In Won Myunghoon’s eyes, all of it was an act, and the source of his disgust.

*That bastard is going to spend his whole life running Gates until he drops dead, and he has the nerve to reject my offer without even knowing his place?*

If Jin Taekyung had wanted to become a star Hunter under some other major entertainment agency, Won wouldn’t have been this angry.

But Taekyung had rejected him without the slightest hesitation. He had chosen the Peace Guild, which was little more than a mom-and-pop shop.

*What a fucking idiot.*

He’ll regret it.

Won Myunghoon muttered those words inwardly and signaled Team Leader 1 with his eyes.

* * *

“Great job! Great job, you bastard!”

Thump! Thump!

Im Kkeokjeong snorted through his nose as he patted my shoulder.

“Wow! Fifty Orc Warriors! You’re seriously the greatest Hunter!”

“Calm down.”

“Your movements, spear technique, soul… Just as expected of an A-Rank Hunter. You turned the Gate upside down!”

“…”

Why was “soul” in there? And what did he mean, I had turned it upside down?

Unlike me, who was dumbfounded, Im Kkeokjeong’s excitement showed no sign of fading.

“I knew you’d become like this, ahem.”

“…You aren’t crying, are you?”

Unable to continue, Im Kkeokjeong’s lips trembled as he turned his head away.

“Who’s crying? I just, well, I remembered the old days.”

“Uncle.”

“Do you remember that time? Two years ago, when we were attacked in an E-Rank Gate.”

“When… Oh, I remember.”

“Yeah. That bastard who called himself the Team Leader ran away first, and I thought we were all going to die. But you stayed in the rear until the end and protected the injured.”

“Was Uncle one of them?”

Im Kkeokjeong nodded with an emotional expression.

As far as I remembered, I had saved about seven people that day. I only found out today that Im Kkeokjeong had been among them.

*Was that why he recommended me to Team Leader Choi?*

“You still remember that?”

“I may forget what people do to me, but I never forget a debt until the day I die.”

“Forget it. It was a long time ago.”

“Anyway, I’m really happy that you’re doing well, Taekyung. No matter how hard I try, I’m still only a D-Rank Hunter… but I want you to know that I’m always cheering for you.”

I knew that. Not only Im Kkeokjeong, but the other Guild members always cared about me and thought of me.

*I guess I’m lucky when it comes to people.*

I looked at the Guild members with warm eyes.

First was Team Leader Choi, our practical source of funding.

“Mr. Jin Taekyung.”

“Yes, Team Leader.”

“You truly are remarkable.”

“It was nothing special.”

“Your eye for things is remarkable.”

“…?”

“The look in your eyes just now must mean that you recognized this ‘Frozen Eye’ hanging around my neck.”

Team Leader Choi smiled proudly and pulled off his necklace.

*When had he even started wearing that? I’d never seen it before today.*

“Russia’s greatest jewelry maker, Vladimir Stalin, designed it…”

“…”

*Fuck, give me back my touching moment.*

I was sighing at his maddening consistency when—

“Hm?”

Team Leader Choi suddenly paused and pointed at Im Kkeokjeong’s neck.

“Is that perhaps Yeti’s Necklace?”

Im Kkeokjeong was startled by his greedy gaze and nodded.

“Huh? Uh-huh.”

“That’s an item that rarely even appears on secondhand markets… Where did you get it?”

“T-this?”

He looked ready to tear the necklace off along with Im Kkeokjeong’s neck.

Sensing the threat to his life, the middle-aged man hurriedly took off the necklace and handed it to me.

“It’s not mine. Taekyung lent it to me.”

“Mr. Jin Taekyung did?”

I nodded.

“I lent it to him. I borrowed it from Myunghoon hyung, though.”

“I see. If you don’t mind, may I take a look at it?”

“I suppose there’s no harm in looking.”

Just as I was about to hand him *Yeti’s Necklace*, I suddenly became curious.

*Was this item really that expensive?*

*Come to think of it, I haven’t even had it appraised yet.*

It wasn’t particularly useful to me, but there was no harm in finding out exactly what it did.

Without giving it much thought, I muttered inwardly.

*Item Appraisal.*

Ding.
## Chapter artifact 218

# Chapter 218

“This is…”

After spending a long while examining *Yeti’s Necklace* once it was handed to him, Team Leader Choi’s eyelids began to tremble.

“I’m angry.”

He was normally not this blatant with his emotions.

Im Kkeokjeong, who had been squatting quietly, asked with intense curiosity,

“Team Leader Choi, what’s wrong? Is there a problem?”

“There is. A very serious problem.”

Team Leader Choi bit down hard on his lip and continued.

“The fact that there is such a limited supply of this beautiful product. That is the greatest problem in the world—one that deserves condemnation from everyone on Earth.”

“…Ah.”

“Look at it. The artistic shape that expresses an icicle! The magical function that preserves the chill of a snowy field!”

Like a North Korean TV announcer passionately praising the Supreme Leader—no, the necklace—Team Leader Choi suddenly whipped his head toward me.

“What do you think, Mr. Jin Taekyung?”

“Me?”

Where should I start? How should I explain it? And what was I even supposed to say?

My hesitation was brief. A calm, gentle voice came from my mouth—so calm that even I was surprised.

“I’m angry too.”

“…”

“What’s wrong?”

“No, it’s nothing.”

Team Leader Choi stared at me with a strange look before continuing.

“It’s just that you feel a little unfamiliar somehow.”

“Do I?”

I rubbed my chin. The stubble that had begun to show was rough against my fingers. The sensation felt unfamiliar, almost like someone else’s skin.

“Is it because I haven’t shaved?”

“Mr. Jin Taekyung, perhaps…”

Just as Team Leader Choi was about to say something, Won Myunghoon approached with a pleasant smile.

“Wow, that was incredible. Taekyung, you really can fight.”

“…You think so?”

“Your spear technique was completely different from the one in the manual I wrote. Did you learn it at the training center?”

“No. I just picked up a few things here and there.”

“Here and there? That wasn’t a level you could reach from just picking things up. At this rate, I’m worried you’ll catch up to me in a few years. Haha.”

I silently pulled up the corners of my mouth.

When nobody laughed along, his laughter gradually faded. It should have been awkward, but Won Myunghoon smoothly changed the subject.

Everything about him was polished, without a single unnecessary movement—as if I were watching a scene from a television drama.

“So, what were you doing?”

His mouth was asking the question, but his eyes were already busy figuring out what was going on. His gaze briefly passed over *Yeti’s Necklace* in Team Leader Choi’s hand.

“We were looking at the necklace you lent me. Team Leader Choi is very interested in things like this.”

“Team Leader Choi? I suppose that makes sense. He did seem like the type.”

If Won Myunghoon wrapped himself from head to toe in flashy luxury brands, Team Leader Choi was the exact opposite.

His clothes were still expensive, but how should I put it? They were refined and clean. In any case, anyone who saw what he normally wore would realize that he was very interested in fashion.

But Won Myunghoon’s interest lay elsewhere.

“So, what did you think after looking at it?”

Team Leader Choi answered,

“It’s much better in person. If you ever decide to sell it, please contact me.”

“I’m afraid that won’t happen. It’s something I personally treasure.”

*Something he personally treasured…*

I mulled over his words before speaking without thinking.

“It must be important.”

“Of course. Very important.”

“I see.”

I held *Yeti’s Necklace* out toward Won Myunghoon.

“I’ll return it now.”

“Hm?”

“You said it was important to you, hyung. And from what Team Leader Choi said, it sounds like it’s extremely expensive.”

“…”

“Are you not going to take it?”

The necklace swayed in my hand with a light metallic clatter.

A very brief silence passed. Won Myunghoon stared at me, and a faint smile formed around his mouth.

“Taekyung.”

“Yes.”

“Your hyung values the bonds between people more than material things.”

“The bonds between people.”

“Right. The Guild members who came with us today are the same. They’re people who stayed by my side during the hardest time of my life.”

“You mean eight years ago?”

“…Well, yes. Anyway, what I’m trying to say is, don’t worry about it too much. What’s so precious about a necklace like that? Right?”

Won Myunghoon patted my shoulder with his broad palm. Unlike mine, his palm was soft, and his fingernails were long.

A strange thought suddenly crossed my mind.

*Maybe this person standing in front of me isn’t the person I knew.*

“Actually, the necklace is a gift.”

“A gift?”

“Yeah. A gift from your hyung to you.”

Every time Won Myunghoon leaned closer to me, the strong scent of his cologne wafted over.

“So don’t give it to anyone else. Understand?”

“…”

“Taekyung?”

I put the necklace around my neck as I answered.

“Yes. I won’t let anyone else touch it.”

Ding.

> **System**
> - You have equipped **Yeti’s Necklace**.
> - The wind of the snowfield flows from the necklace.

As I felt the wind of the snowfield wrap around my entire body, I recalled the Item Window I had seen just five minutes earlier.

> **System**
> **Item Window**
>
> **Yeti’s Necklace**
>
> **Type:** Accessory  
> **Grade:** Peak  
> **Restriction:** None  
>
> **Description:** A necklace that only an exceptionally skilled warrior Yeti can possess. In truth, however, it is a shackle marking a yeti as a former slave and food animal of the dragonkin. Anyone who possesses this item becomes a target of dragonkin monsters, regardless of the possessor’s species.
>
> **Effect:** **Wind of the Snowfield** effect activated.

*So I’m a target.*

It was hardly a pleasant word.

In many ways.

* * *

Time passed slowly inside the Gate.

After traveling for half a day, we left the jungle and entered the wasteland. But the only monsters we had encountered so far were the Green Wyvern that had appeared at the beginning, the Orcs I had dealt with, and the Troll the others were fighting now.

—Gwoooor!

The Troll was about a head taller than an adult man, with an abnormally large head.

Trolls were monsters with extraordinary regenerative abilities. That was also why they were used as the main ingredient in healing potions, like an indispensable ingredient in every dish.

Even if you cut off their arms and legs, they could regenerate them in just a few seconds. Naturally, they were difficult opponents.

But the Star Guild members were all veterans who were nothing to scoff at.

“The head! Aim for the head!”

“Fire magic!”

Sshhk! Fwoooosh!

At the beginning of the Great Cataclysm, Trolls had earned a notorious reputation as immortal monsters, but their weakness had been discovered soon enough.

*The head and the heart. And magic, on top of that.*

Unless it was an undead monster, death after the cessation of breathing was only natural.

Trolls possessed enough terrifying regenerative power to restore even their heads and hearts, but that didn’t make them immortal monsters.

If you froze them with ice or seared them with flames before they could regenerate, there was little they could do.

“DPS, get in there and cut it down!”

“Mages, stand by!”

Sshh-shh-shhk! Thwack!

—Graaaar!

The Troll’s body toppled backward after losing one arm and one leg.

A moment later, the sharp axe blade of a halberd cleaved through its neck, which was packed with fat and muscle.

Thud! Sshhk!

The Troll’s body flailed, now empty above the shoulders. Soon, new flesh began to writhe and swell across the cut surface.

In a little over a minute, it would have a new neck.

Of course, the Star Guild members had no intention of waiting that long.

“Burn it!”

Fwoooosh! Ssssss!

Cold that froze to the bone and flames that scorched the skin.

The Troll’s body, which had failed to regenerate, shuddered violently once before becoming motionless again.

“Unit Three cleared!”

“Help over here! This one’s regenerating!”

With three people assigned to each Troll, the situation ended quickly.

Amid the stench of burning flesh and fat, Won Myunghoon, who had been watching the battle from about a dozen meters away, muttered.

His voice was so quiet that nobody could make it out over the noise of battle, but to me, it sounded as clear as if he were speaking right beside me.

“These idiots had to make it smell. I told them to freeze them whenever possible.”

“Hah.”

I barely managed to suppress the hollow laugh trying to escape.

Someone had once said that life was a tragedy up close and a comedy from far away.

But a battle against monsters was a tragedy no matter where you watched it from.

When you could lose your life in an instant, the smell of burning Troll flesh was nothing.

*It’s a hundred times better than being the one behind a folding screen, smelling funeral incense burn.*

But to Won Myunghoon, it was someone else’s problem.

He frowned and cursed under his breath before suddenly sensing my gaze and turning toward me.

“Oh, Taekyung.”

His voice was warm, and his forehead had smoothed out as if nothing had happened.

Everything about him was natural.

That was why it felt even more abnormal.

“What is it? Do you have something to say?”

For some reason, it sounded to me like he was asking, *Did you hear everything I said?*

I answered calmly without letting anything show.

“Yes.”

“Really? What is it?”

“I feel a little nauseous. I was fine at first, but… I started feeling strange after we came in here. I even tried healing magic, but it hasn’t helped much.”

“Ah. That.”

Won Myunghoon gave a quiet laugh.

“It’s because this is your first A-Rank Gate. The amount of mana distributed inside a Gate is on an entirely different level.”

“Oh, I see.”

“Beginners are all like that. I’m used to it by now.”

I let out an exclamation as if I were hearing this for the first time, even though I already knew everything.

“So I’ll get used to it next time too, right?”

“Next time?”

The corners of Won Myunghoon’s mouth twitched before he nodded.

“That’s right. You’ll be much more used to it next time.”

“I hope I can come with you again then, hyung.”

“Well, I don’t know when I’ll have time again. I have so many other schedules.”

“You don’t even have time to go on raids?”

“You may not know this yet, Taekyung, but Guild Masters like me are all busy. We have to coordinate the Guild as a whole.”

“Ah.”

“It’s the difference between a musician and a conductor. You know what a maestro is, right?”

As Won Myunghoon pretended to wave a conductor’s baton, I suddenly asked,

“Then did you go to the department store for a Guild-related meeting?”

“Hm?”

“I saw an article about it on the Internet. What was the headline again? Ah, I remember.”

Won Myunghoon suddenly lost his words. Watching him, I continued clearly,

“Something like *Rising Star Hunter Won Myunghoon Goes on a Luxury Shopping Spree.*”

“…”

“Was there an article like that?”

“It was on a Hunter community site, but only for a very short time. It was deleted after five minutes.”

“R-really? Are you sure you didn’t see it wrong?”

“Yes. There’s a Rice Weevil who doesn’t study these days and does nothing but dig through the Internet. Whenever an article comes out, he tells me immediately.”

A deep dimple appeared in Won Myunghoon’s handsome face. But it wasn’t the bright smile I had seen on television in the past.

“That can’t be right.”

“Isn’t it?”

“Of course not. I do like shopping, but I’m not that bad. At most, I might go once a month.”

“I heard pictures were uploaded too.”

“…”

“You know Dispass, right? The site that specializes in digging into celebrities. They even interviewed someone from the department store. Apparently, you’re a VVIP who visits five times a week.”

“…”

Won Myunghoon licked his dry lips. The dimple that had appeared a moment ago had vanished without a trace.

“Taekyung. You don’t actually believe that, do you?”

“Come on, it must be a rumor sheet. You’re busy coordinating the Guild schedule, hyung. Maestro.”

“…Yes, Maestro.”

Won Myunghoon was staring at me with dry eyes as I enthusiastically mimed swinging a conductor’s baton when—

“Hyung! No, CEO!”

The shout rang across the endless wasteland of dirt, sand, and winding rocky hills. Its owner was Star Guild’s Team Leader 1.

He had gone out to scout for the Wyvern that had been nowhere to be seen since earlier, and had now returned.

But unlike his relaxed departure, his face was deathly pale as he came sprinting toward us like a madman.

“What happened? Where are the others?”

At Won Myunghoon’s question, Team Leader 1 stammered.

“Th-that, th-that…”

I didn’t need to hear the rest.

Seven people had left, but only one had returned. The drops of blood splashed across his face and armor turned my guess into certainty.

“You bastard. Speak clearly!”

Team Leader 1 flinched at the thunderous roar.

“We found the Wyvern. We found it.”

“The Wyvern? How many?”

“O-one.”

“What? One?”

An A-Rank Hunter and six B-Rank Hunters made a formation more than capable of dealing with a single Wyvern.

And yet six people had died, while one had fled back alone.

“Is that supposed to be an explanation? Are you messing with me?”

“They’re all dead. We approached while using concealment magic, but… it noticed us.”

“What kind of bullshit is that? How could a Wyvern see through concealment magic?”

Click. Clack-clack.

His teeth chattering from fear, Team Leader 1 finally forced out a single word.

“A-A Named Monster.”

“…”

“It’s definitely a Named Monster. This place… it’s a Mutated Gate.”

An A-Rank Mutated Gate. And a Named Monster.

There was no one among us who didn’t understand what those two words meant.

Amid the suffocating silence, someone muttered in a voice barely loud enough to hear.

“Fuck…”
## Chapter artifact 219

# Chapter 219

From the early days of the Great Cataclysm to the present, humanity had classified monsters and established a hierarchy based on its countless experiences with death and destruction.

Accordingly, the Grade of each Gate was determined by the Grade of the monsters inhabiting it.

However…

*There are exceptions to everything.*

Mutated Gates were one such exception. Having broken free from the boundaries established by humanity, they were, in every sense of the word, mutations.

Another variable had intruded into the space known as Gates—spaces that humanity still regarded as an enigma.

*The worst kind.*

A D-Rank monster could appear in an F-Rank Gate, and a B-Rank monster could appear in a D-Rank Gate.

That alone was a horrifying nightmare, but there was one even greater problem.

*Rare Monsters.*

As if running into an unexpected higher-level monster wasn’t bad enough, every one of those creatures possessed strength that surpassed that of other monsters of the same Grade.

The term Rare Monster was coined for the first time then.

And not long afterward, someone raised another question.

*Then what about the Rare Monsters that appear in A-Rank Mutated Gates? Aren’t they too strong to be considered the same Grade?*

For Hunters, A-Rank represented the highest realm that could be reached through a single awakening.

Among them, those recognized as especially strong were given the honorable Title of ranker.

The same issue applied to monsters. After countless arguments and debates in the relevant academic circles, a new term was born.

*Named Monster.*

True monstrosities that had broken beyond the boundaries of A-Rank.

Team Leader 1, the only one to return alive, had said that such a Named Monster was here.

In the very space where we stood—in the Wyvern’s Nest.

“Bullshit!”

Won Myunghoon shouted roughly as he seized Team Leader 1 by the collar.

“There’s no such thing as a Named Monster here.”

“I-I’m telling the truth. I saw it clearly with my own eyes.”

Team Leader 1 continued in a trembling voice.

“It was several times larger than an ordinary Wyvern. It was so huge that I couldn’t believe what I was seeing, even with my own eyes.”

“Shut up!”

But the terror Team Leader 1 had received from the Named Monster was beyond imagination.

Despite being an A-Rank Hunter, he was so frightened that he looked like a seven-year-old child.

“That thing is on an entirely different level from the Wyverns we’ve fought so far. We need to run right now.”

“Kim Jonghun, you son of a—”

Grind.

Won Myunghoon ground his teeth, but that was all he did.

Although he had fallen short of expectations in every respect, he had once risen to the rank of ranker. As an A-Rank Hunter, he couldn’t possibly be unaware of what everyone here already knew.

Won Myunghoon was bullying Team Leader 1 only as a defense mechanism to conceal his own fear.

*There must have been signs of a Mutated Gate already.*

I knew that well, having experienced it myself three years ago.

The strangely low number of monsters that appeared. And the unusually generous amount of Magic Gems compared to the number of monsters defeated.

I hadn’t known about the latter. Handling the byproducts was the Star Guild’s responsibility, and even though this was a joint raid, Won Myunghoon was the commander who made every decision.

*And that commander just took a giant shit.*

This wasn’t a minor error in judgment.

The thing stalking us somewhere in that wasteland wasn’t an ordinary Wyvern, but a Named Monster.

“Goddammit…”

As Won Myunghoon spat out a harsh curse, Team Leader Choi spoke.

“Let’s calm down. In the current situation, our immediate withdrawal has to come first.”

“Calm down? Do I look like I can calm down in a situation like this?”

“I’m telling you to settle your mind and face reality.”

Team Leader Choi’s calm voice continued.

“Fortunately, we aren’t too late. If we turn around and retrace our path as quickly as possible, we can reach the jungle within an hour. But if we run into that thing in this wasteland…”

“Who doesn’t know that? Stop meddling.”

The cheerful and well-mannered gentleman was gone. At Won Myunghoon’s irritable response, Team Leader Choi’s eyes grew cold.

“That’s unfortunate. I didn’t expect you to take it that way.”

“Unfortunate? Just because we’re cooperating, you seem to think we’re really equals or something… Fuck, there’s no point in talking. Anyway, stop telling me what to do. I’m already in a shitty mood.”

They say that you can learn a person’s true nature when they are in a crisis.

In that sense, Won Myunghoon was exactly this kind of person. The only thing that left a bitter taste in my mouth was the fact that I had once considered someone like him an idol.

Won Myunghoon spoke to the Guild members with an anxious expression.

“Take only the Magic Gems. We’re returning to the Gate entrance as quickly as possible.”

There were two doors through which one could leave a Gate: the entrance used to enter it and the exit that opened after the boss monster was killed.

For now, choosing the former was obviously the right decision.

“Yes, sir.”

The preparations were finished quickly. The only problem was Team Leader 1, who remained deathly pale.

“What’s with that guy?”

At my mutter, Butler Kim answered. He had been keeping quiet a single step behind me the entire time.

“He’s been exposed to a monster’s Fear.”

“An A-Rank Hunter?”

“The opponent is a Named Monster.”

“Oh.”

“And a Grade is merely a measure of strength. It has nothing to do with how strong someone’s mental fortitude is.”

Even so, an A-Rank Hunter had been afflicted by Fear.

There were two possibilities. Either Team Leader 1 normally had a weak mentality, or the Named Monster was truly that powerful.

*Personally, I’d prefer the former.*

With that thought in mind, I approached Team Leader 1. I only meant to help him to his feet, but he flinched as if he had been burned.

“It’s okay. I’m not trying to hurt you. You know me, right?”

“J-Jin Taekyung.”

“You’re still coherent, at least. Now pull yourself together and get up. Otherwise, you can keep sitting there and become prey.”

“Gah!”

Sometimes, stoking fear worked better than inspiring courage.

At the word prey, Team Leader 1 shot to his feet and looked around anxiously.

“T-the thing…?”

“It’s not here. More importantly, how did you survive?”

It was something I had wanted to ask for a while. But from the moment the words Named Monster had come out, nobody had been curious about anything else.

Team Leader 1 bit his lip.

“I had no choice.”

“…I see.”

He had run away. He had abandoned his team members.

But I didn’t condemn him. Not because I understood him, but because I didn’t think I had the right to.

*Someone might have the right to curse him out, but not me.*

Whether he knew what I was thinking or not, Team Leader 1 began rambling incoherently.

“We were approaching carefully, but it saw us. Then it spread its wings—its black wings—wide…”

“Black wings?”

“Y-yes. It was completely black from head to tail.”

A memory suddenly surfaced. The screams filling the cave, and those enormous wings.

The Wyvern I had encountered back then had also been black from head to toe.

“A Black Wyvern.”

“No, it was different. It was several times larger and stronger than the Black Wyverns we’ve seen so far. That thing… it’s a real monster.”

Then it couldn’t have been the same creature I had encountered three years ago.

After the Sangdong Station Mutated Gate incident, I had been subjected to countless investigations. The investigative team dispatched to determine the truth of the incident had concluded that the creature wasn’t significantly different from an ordinary Black Wyvern.

*Then where would that thing be now?*

Monsters inside Gates respawn at regular intervals. By the time the investigators arrived, it had already disappeared.

Whenever I drank, I sometimes found myself thinking about it.

*Where is it now? Did it die at the hands of another Hunter? If it’s still alive, will I ever have the chance to get revenge?*

*Now it’s possible.*

As long as we were both alive, the day would come when we met again.

Me to it, and it to me. We had each left the other with an indelible memory.

But apparently, today wasn’t that day.

“Mr. Jin Taekyung.”

“Taekyung!”

The Guild members had finished preparing and were waiting for me. I had just started walking to rejoin the formation when—

“One eye.”

The single word that suddenly came from Team Leader 1’s mouth made my body freeze.

I slowly turned around. Team Leader 1 was pointing at one of his own eyes with a trembling hand.

“What did you just say?”

“Right. One of its eyes was damaged. As if something had stabbed it…”

“…”

A current ran down my spine. My mind went blank, and my fist clenched on its own.

Three years ago, I had charged at that thing prepared to die.

I had gathered every ounce of strength I possessed and unleashed One Annihilation—no, *Stab with All My Strength*—and the spearhead had pierced straight into its eye.

That had been my final act of defiance, and the only mark I had left on it.

*It’s him.*

I didn’t wonder how an ordinary Black Wyvern had become a Named Monster.

My skin, with every last hair standing on end, was the witness, and my pounding heart was both prosecutor and judge.

Everything that made me who I was shouted as one.

The unidentified Named Monster Team Leader 1 had described was the very creature that had given me an unforgettable nightmare three years ago.

*We finally meet again.*

I didn’t know what to call this feeling.

Fear? Joy?

My entire body trembled with an emotion I couldn’t identify.

And then, just as my senses—sharper and more taut than ever—began to mingle with the thick scent of blood—

—Kyaaaaaaaah!

I raised my head at the roar echoing from the distance.

On the horizon of the wasteland beneath the setting sun, wings dyed entirely black were flying toward us.

* * *

*Goddammit. Goddammit. Goddammit!*

The same curses kept replaying endlessly in Won Myunghoon’s mind.

The plan was as good as ruined. Now they were in a situation where they had to worry about their very lives.

*A Named Monster.*

The situation was as serious as it had been eight years ago—no, it was even worse.

Won Myunghoon had driven the Guild members to finish their preparations as quickly as possible and was just about to order them to set out when—

“It’s coming.”

The quiet voice that pierced his ears made his heart drop.

It was even worse because the voice belonged to Jin Taekyung.

“W-what does that mean?”

“Prepare for battle. Or run for your life.”

“What are you talking about?”

“What else would I mean?”

There was something unfamiliar about Jin Taekyung’s steady gaze.

The person standing before Won Myunghoon was neither his biggest fan nor the foolish twenty-something who had grinned stupidly.

*What is this feeling?*

As Won Myunghoon flinched, a dry voice slipped between Jin Taekyung’s lips.

“Take everyone with you. I still have the necklace.”

“…What?”

What the hell was this bastard talking about?

As Won Myunghoon fell into confusion, Jin Taekyung curled up the corner of his mouth.

“Why are you so surprised? Did you think I wouldn’t know?”

“You little—”

“Myunghoon hyung. No, Mr. Won Myunghoon.”

Won Myunghoon stopped dead. It wasn’t because of humiliation, but because of the oppressive weight.

A pressure he had never felt before was radiating from Jin Taekyung.

“Whatever you did or were planning to do, I’ll let everything up to now slide. But…”

A glint appeared in the eyes that had darkened beneath his wildly tousled hair.

“Don’t bare your teeth at me again.”

“…”

“I’m done talking. Get lost.”

Won Myunghoon’s lips moved, but no words came out.

He stared at Jin Taekyung with an indescribable look in his eyes before roughly turning away.

He could feel the gazes of the Peace Guild members stabbing into the back of his head. They had only just realized that something had happened.

*Those fucking idiots. How dare they…*

But it didn’t matter.

Jin Taekyung and those ragtag Guild members would be dead soon anyway.

A short while later, as Won Myunghoon and the Star Guild members ran with all their might, a roar echoed from far away.

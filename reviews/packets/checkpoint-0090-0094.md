# Checkpoint Review — 90–94

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

# Chapters 90–94

## Plot

During a week of paid vacation, Jin Taekyung begins arranging to buy and remodel his family’s former home. He reunites with former classmate Park Jihwang, now Park Jihoon, a Hunter in Myeongdong Guild whose strength appears comparable to or greater than Im Changsoo’s.

Sangdong Guild investigates Taekyung after Im Chunsoo receives reports of his impossible recent feats. Chunsoo orders expanded surveillance while Sangdong’s Team 1 Leader remains skeptical. Hong Woojin, a B-rank mage and information broker, monitors Taekyung through tiny Familiars. Taekyung detects and drives away the Familiars around his home, concludes the controllers must have been nearby, and decides to catch them himself.

Taekyung purchases and stores 350 million won worth of low-rank weapons at the Ilsan Store. On returning home, he learns that Hayeon has found an abandoned kitten and received permission to foster it. Taekyung identifies the kitten through the System as a level-two Cat—Familiar, raising the possibility that it is connected to the surveillance.

## Continuity

- Peace Guild’s Guild house will finish remodeling in one week; Taekyung is on paid vacation until then.
- Choi Minwoo and Butler Kim suspect Taekyung may be a third-awakening Hunter, but this remains unconfirmed.
- Taekyung agreed to buy his former family home for 3.38 billion won, paid the ten-percent deposit, and plans to remodel it and move after Hayeon’s college entrance examination.
- Park Jihwang changed his name to Park Jihoon and works in Team 1 of Myeongdong Guild.
- Im Chunsoo ordered Sangdong Guild’s Audit Team to expand surveillance of Taekyung. Sangdong’s Team 1 Leader, Chunsoo’s loyal right hand and the Guild’s only other A-rank Hunter, doubts the reports of Taekyung’s feats.
- Peace Guild’s Guild Master and Team Leader remain protected by an unexplained security Lock that hides their personal and account information.
- Hong Woojin is investigating Taekyung with Familiar magic. He severed the Link to his rice-weevil Familiar and intends to continue with more conspicuous surveillance.
- Taekyung’s Qi Sense reaches seventy meters and detected the Familiars in his home, but tiny Familiars generally evade ordinary detection magic.
- A B-rank mage’s Familiar connection reaches up to 500 meters, with approximately 300 meters considered a safe operating distance. Forced Link severance causes physical distress and may cause mana backflow.
- Taekyung spent 350 million won at the Ilsan Store and stored the weapons in his Inventory.
- Hayeon is temporarily fostering an abandoned level-two Cat Familiar with Kim Jeonghee’s permission. Its owner and connection to the surveillance are unknown.
- Retaliation by Im Chunsoo or Sangdong Guild, Woojin’s motive, Hayeon’s schooling, and the existence of third-awakening Hunters remain unresolved.

## Translation Decisions

- Use **third-awakening Hunter**, **third awakening**, **Frozen**, **Qi Sense**, **Familiar**, **Link**, and **Lock** as established.
- Render **Park Jihwang** and **Park Jihoon** for the former and current names.
- Use **Myeongdong Guild**, **Team 1 Leader**, **Audit Team**, **Ilsan Store**, **Assistant Manager**, and **Cat—Familiar**.
- Retain **jeonse** with its explanatory gloss, **goshiwon** with its established footnote, and **samgyetang** with its explanatory footnote.
- Preserve the established explanatory footnote for **백조** and the forum author’s exaggerated comic voice.

## Durable state

{
  "active_continuity": [
    "The party sells The Minotaur's Labyrinth byproducts and Magic Gems to the Administration.",
    "Im Kkeokjeong warns that Sangdong Guild is a powerful local Guild capable of threatening Peace Guild; Im Chunsoo, its A-rank Guild Master and founder known as Frozen, ordered expanded surveillance of Taekyung through Sangdong's Audit Team.",
    "Im Changsoo transferred the promised four billion won to Jin Taekyung after Im Chunsoo learned about his transfers and beat him.",
    "Kim Jeonghee is Taekyung and Hayeon's mother; Taekyung's father died when a Gate opened downtown during the Great Cataclysm.",
    "Kim Minsu is the restaurant owner's son, a D-rank Hunter in Sangdong Guild, and is not known personally by Im Changsoo.",
    "Taekyung is a C-rank Hunter who reawakened from F-rank, defeated B-rank Minotaurs, and can use the Jin Family's Cultivation Technique to perform Circulate Qi for Healing on others.",
    "Hayeon and Kim Jeonghee recovered substantially after receiving Circulate Qi for Healing from Taekyung; Hayeon also asked whether she could drop out of school after learning about his raid earnings.",
    "Taekyung's reality and Murim Inventories are separate.",
    "Peace Guild's Guild house remodeling is scheduled to finish in one week, and Taekyung is on paid vacation until then.",
    "Choi Minwoo and Butler Kim suspect that Taekyung may be a third-awakening Hunter; the possibility remains unconfirmed.",
    "Taekyung agreed to buy a meaningful former family home for 3.38 billion won, paid a ten-percent deposit, and plans to remodel it and move after Hayeon's college entrance examination.",
    "Park Jihwang changed his name to Park Jihoon and is now a Hunter in Team 1 of Myeongdong Guild; Taekyung judged Jihoon's strength comparable to or greater than Im Changsoo's.",
    "Hong Woojin is a B-rank mage and information broker investigating Taekyung through Familiars; he severed his rice-weevil Familiar's Link and plans more direct surveillance.",
    "Sangdong Guild's Team 1 Leader is the Guild's only A-rank Hunter besides Im Chunsoo and doubts the report of Taekyung's feats, while withholding Woojin's warning from Chunsoo.",
    "Peace Guild's Guild Master and Team Leader have personal and account information protected by a security Lock reportedly imposed by an upper agency.",
    "Taekyung's Qi Sense reaches seventy meters and detected the fly Familiars in his home; after Woojin severed the rice-weevil Link, Taekyung confirmed that no Familiar remained.",
    "Taekyung spent 350 million won at the Ilsan Store and stored the purchases in his Inventory.",
    "For a B-rank mage, Familiar connections reach up to 500 meters, with about 300 meters considered safe; forced Link severance causes physical distress and may cause mana backflow.",
    "Tiny Familiars evade most detection magic, leading Taekyung to conclude that the people who controlled the Familiars near his home yesterday were nearby and to decide he has another reason to catch them himself.",
    "Hayeon found an abandoned level-two Cat Familiar and received Kim Jeonghee's permission to foster it temporarily; Taekyung recognized it through the System."
  ],
  "continuity_sources": [
    94
  ],
  "open_questions": [
    "Whether Im Chunsoo or Sangdong Guild will retaliate against Peace Guild remains unresolved.",
    "What will happen to Kim Jeonghee after leaving the restaurant remains unresolved.",
    "Whether Hayeon will actually drop out of school remains unresolved.",
    "Whether third-awakening Hunters exist and whether Taekyung is one remains unresolved.",
    "Why Hong Woojin is investigating Taekyung and what information he seeks remains unresolved.",
    "Whether Sangdong Guild sent the Familiars observing Taekyung remains unresolved.",
    "Who controls the Cat Familiar and whether it is connected to the surveillance remains unresolved."
  ],
  "safe_through": 94,
  "temporary_decisions": [
    "Use Frozen for 프로즌, preserve the tiger-father/dog-son wordplay in 호부견자, and use ajumma for 아줌마.",
    "Use goshiwon for 고시원 with an explanatory footnote; use Hope Goshiwon for 희망 고시원.",
    "Use Minsu for 민수; render 운기요상 as Circulate Qi for Healing, 하급 포션 as Lesser Potion, and 상급 포션 as Superior Potion.",
    "Render 3차 각성자 as third-awakening Hunter, 3차 각성 as third awakening, 피의 일주일 as Bloody Week, and 전세 as jeonse lease.",
    "Render 사장님 as Boss in the real-estate context, including young Boss.",
    "Render 박지황/박지훈 as Park Jihwang/Park Jihoon, and 삼계탕 as samgyetang with an explanatory footnote.",
    "Render 1팀장 as Team 1 Leader, 기감 as Qi Sense, and 락 as Lock when referring to security restrictions.",
    "Render 집파리, 검정파리, 금파리, and 패밀리어 as Housefly, Black Blow Fly, Green Bottle Fly, and Familiar; use Rice Weevil for 쌀벌레, Link for 링크, Store for 스토어, Assistant Manager for 대리, Kim Seonhee for 김선희 and the source variant 김희선, Ilsan for 일산, and Lafesta for 라페스타."
  ],
  "version": 1
}

## Reading copies

## Chapter artifact 90

# Chapter 90

“A week off?”

“Yes. Exactly as you heard.”

Team Leader Choi’s call that evening had been unexpected.

A whole week off? Had something happened to the Guild?

When my thoughts reached that point, I suddenly remembered something.

“Uh, you didn’t have a problem with Sangdong Guild, did you?”

“Sangdong Guild?”

“I mean, because of the Im Changsoo situation…”

“Ah, you don’t need to worry about that. The Guild house remodeling is supposed to be finished in a week.”

It was a relief to hear that nothing had happened. But did people really stop raiding because of Guild house remodeling?

*It’s nice to hear I’m getting a whole week off.*

For the past seven years, I had lived with my eyes fixed straight ahead, running without rest. Lately, I had been going back and forth between the Murim and reality, spending my days without a moment to breathe.

Honestly, I wanted to re—no. This was precisely when I needed to work harder. I spoke in a voice filled with determination.

“Team Leader. I want to work.”

“Ah, but you’ll still receive your full salary during your vacation.”

“Then I’ll see you in a week.”

“……”

“I’m hanging up. I need to eat dinner.”

“…Yes.”

As soon as I ended the call, Hayeon came hurrying over and bowed politely.

“Oppa. The evening meal has been prepared.”

“……Could you stop speaking like that? It’s giving me goose bumps.”

“Switching to casual mode requires a paid purchase.”

“You make asking for allowance sound so complicated.”

When I held out two 50,000-won bills, Hayeon flashed a wide grin.

“Mom says dinner’s ready.”

“Oh, what’s on the menu?”

“Beef bulgogi. And bean sprout soup that I made.”

“Beef bulgogi sounds good.”

“Mom says my bean sprout soup is good. She praised me.”

“Mom’s homemade beef bulgogi never lets you down. It’s always fresh, the best, thrilling.”

“……”

My younger sister was thoroughly pissed off, and the table was covered with Mom’s cooking.

What was so special about vacation? I would eat and sleep to my heart’s content at home.

* * *

Tap.

Choi Minwoo set down his smartphone after ending the call. Butler Kim, seated across the table from him, asked,

“What did he say?”

“He was worried too. About Sangdong Guild.”

“The more I see of him, the more interesting that young man becomes. He seems to act without thinking, yet he’s quick to grasp the situation.”

Choi Minwoo tapped the table with his long fingers.

Even after some time had passed, the sudden appearance of Jin Taekyung remained a mystery.

When they had first met, Taekyung had seemed like nothing more or less than a diligent F-rank Hunter. Yet yesterday, he had single-handedly swept through a B-rank Gate.

*He’s getting stronger.*

As of yesterday, his suspicions had turned into certainty.

Jin Taekyung was getting stronger. And he was doing so incredibly fast.

“Is there no additional information about Jin Taekyung?”

“No. I’ve repeatedly reconfirmed everything, but nothing has turned up.”

Butler Kim was a man who handled his work thoroughly. But this time was different. Choi Minwoo carefully opened his mouth.

“Butler Kim.”

“Yes, Young Master.”

“Could you perhaps look for cases of Hunters who awakened a third time?”

“What?”

Butler Kim’s eyebrows twitched.

A third awakening? It was a term he had never heard or seen in his entire life. If a Hunter like that had existed, no one would have used the word *reawakening*.

A reawakening was called a reawakening because there was nothing after it.

“Young Master, that…”

Just as Butler Kim was about to express his difficulty, a name flashed through his mind.

*Jin Taekyung. If it’s that young man, who knows?*

Butler Kim was a living witness who had experienced the Great Cataclysm firsthand. He had accomplished brilliant feats and participated in countless battles.

Yet even to his eyes, Jin Taekyung was special.

*Those movements… They were truly remarkable.*

Sometimes forceful, sometimes fluid. His transitions between offense and defense were efficient, and he possessed an innate combat sense that told him when to advance and when to retreat.

When Butler Kim watched Jin Taekyung fight, the only word that came to mind was *overwhelming*.

*A third awakening, huh.*

It would take time, but it was worth investigating.

Butler Kim lowered his head.

“I’ll look into it.”

“Thank you. Ah, what are Sangdong Guild’s movements like?”

“They’ve deployed surveillance agents. They’ll probably obtain most of the information within a few days.”

It had not even been half a day since word came that Im Changsoo had been summoned to the Guild Master’s office and beaten like a dog, yet Sangdong Guild’s watchers had already latched on. They were moving faster than expected.

“The target is Jin Taekyung, then.”

“They must have marked him as a major figure. For now, they’ll analyze the entire Guild, though.”

“What about the other Guild members?”

“I’ve warned them in case someone follows them. But…”

Butler Kim hesitated before adding,

“Shouldn’t we tell Jin Taekyung as well?”

“It’s fine. In fact, I hope Sangdong Guild’s intelligence network is far better than ours.”

The person who was hardest to understand—and the person about whom the most had already been revealed.

It was like looking into a clear spring and still being unable to see what lay inside.

Choi Minwoo wanted to use Sangdong Guild’s power, if necessary, to get closer to Jin Taekyung’s true identity.

“More importantly, it seems Sangdong Guild’s Master is extremely angry.”

“He does seem much more cautious than before. If this were the past, he would have barged in and caused a scene by now.”

“Ah. Could it be?”

At Choi Minwoo’s reaction, Butler Kim smiled and nodded.

“I’m acquainted with Sangdong Guild’s Master.”

“An ill-fated relationship?”

“Who knows?”

Butler Kim’s smile deepened.

* * *

“What can I do for you?”

I answered the real estate agent, a man whose forehead shone brightly.

“I’d like to look at some houses.”

“Are you looking for a monthly rental? A jeonse lease? Or perhaps…”

“A house to buy.”

“Well, well. So you’re a young Boss. Sorry, but wait just a moment. Let me take care of this and I’ll be right back. It’s so urgent I can barely hold it.”

I wondered what he needed to take care of, then noticed the toilet paper in his hand.

If that was what he needed to take care of, he should hurry. When I nodded, the real estate agent dashed into the bathroom.

“Have something to eat while you wait on the sofa. There’s some mocha bread on the table. Gnnngh…”

Pfft. Pffft.

“……”

I wouldn’t be able to eat mocha bread ever again.

I lamented inwardly and leaned back against the sofa. On the television, which had already been turned on, a documentary about the Great Cataclysm was playing.

> “Aaaah!”
>
> “Crash! Boom!”
>
> “This is an emergency bulletin. Mysterious phenomena are currently occurring across the country. In response, the government has declared martial law effective immediately…”

People scattered while screaming, buildings collapsed, and flames shot into the sky. News reports announcing the beginning of the Great Cataclysm flashed by one after another, until the exhausted face of the American president filled the screen.

> “We have yet to determine their identity, but one thing is certain. They are our enemies. Not merely the enemies of the United States, but the enemies of the entire world and all of humanity. Even now, countless monsters are passing through Gates and invading Earth.”

Gate.

A Gate meant a door, quite literally. The Demon King Asmodeus had opened that door from beyond another dimension and descended upon Earth with an innumerable army of monsters.

*After that, it went exactly as written in the textbooks.*

Humanity had been helpless. Downtown areas, rural villages, mountains and seas, jungles… Gates appeared regardless of time or place, and the monsters pouring through them committed murder and destruction.

When the hellish period known as the Bloody Week ended after the Gates first opened, the casualties numbered in the tens of millions, while the property damage was so immense that it could not even be calculated accurately.

> The Great Cataclysm: The Ten Most Horrific Years in Human History.

By the time the documentary reached its midpoint alongside the caption, the bathroom door flew open.

“Whew. I feel alive again.”

The real estate agent plopped down after wiping his sweat-slick forehead.

“Sorry to keep you waiting. You said you were looking to buy, right?”

“Yes.”

“Did you happen to visit somewhere else before coming here? There must’ve been plenty of real estate offices on the way.”

“No, this is my first stop.”

“Really?”

Judging by the way his eyes rolled around, he seemed to be deciding whether or not to take me for a fool. I pretended not to notice and held out the note I had prepared.

It had the address written on it.

“I’d prefer to see the property at this address, if possible.”

“With this address… that’s a safe zone.”

“Yes.”

“You really said you wanted to buy, right? Did I hear you wrong because I had to take a dump so badly?”

When I nodded, the man’s eyes traveled subtly up and down.

Jeans and a white T-shirt. A pair of 20,000-won sneakers bought at a market or online. No matter how you looked at it, I was not dressed like someone wealthy.

“What do you do for a living?”

“I run Gates.”

“Oh, a Hunter? I thought so. You’re young and already successful.”

A bright smile blossomed across the man’s face. Hunters were one of the most prominent high-income professions. It was hardly unusual for young, successful Hunters to buy expensive houses and cars.

He asked in a much friendlier tone,

“Have you checked the market prices?”

“I searched online on the way here.”

“Then you’re in luck. There actually happen to be a few listings available. Let’s see…”

Perhaps he was excited by the prospect of a sale, because the man began making calls to one person after another.

He hung up and called again, repeating the process. About five minutes later, he put away his smartphone and turned toward me.

“I found a listing that’s perfect for you, Boss. If you’re not busy, would you like to go take a look right now?”

“Sure. Why not?”

Since I was on vacation, I had no reason to refuse. When I stood up, the man broke into a huge smile.

* * *

Vroom.

I sat in the passenger seat of the sedan and watched the scenery pass by. Detached houses stood in rows, shops dotted the streets here and there, and playgrounds and schools appeared along the way.

“It’s changed a lot…”

The man glanced at me.

“Did you used to live around here?”

“When I was young.”

I had been in my third year of middle school—sixteen years old—so it had been exactly eleven years since then. I had been born and raised here, so in a way, this was my hometown.

“This area was redeveloped about ten years ago, so it must look pretty different. It used to be an old apartment complex, but when they heard an Association branch was going to be built within thirty minutes of here, they tore the whole thing down.”

“I see.”

I already knew that. As soon as news of the redevelopment spread, housing prices skyrocketed. We could not afford the jeonse deposit, which had risen by hundreds of millions of won, so we decided to move.

*It was not long after my father died.*

On the night before we moved, I saw Mom crying silently.

It was several years later that I learned the place had been my parents’ newlywed home.

“We’re here.”

The man’s voice brought me back to myself. When I opened the door and stepped outside, I saw a detached house with a yard.

“This is the address you gave me, Boss. The owner happens to be out, so let’s take a quick look around and get going.”

“Ah, just a moment.”

Maybe it was because of the memories. The old apartment complex had already been demolished, but the area still felt strangely familiar.

*Still… I’m glad it hasn’t changed completely.*

Some traces of the old scenery remained even after the redevelopment. The real estate agent smacked his lips as he watched me look around, lost in nostalgia.

“You must be happy to be back after all this time. Why don’t you take a lap around the neighborhood while you’re at it?”

“Is that okay?”

“You’re going to sign the contract, right?”

“No. I mean, yes.”

This house was something I had to buy, no matter what.

The man let out a quiet laugh and took out a cigarette.

“Then I should accommodate you. It won’t take long to walk around the neighborhood. I’ll stay here and smoke while I wait, so don’t worry about me.”

After offering him a brief word of thanks, I began walking slowly.

*Is this the right way?*

I passed through an alley and found the supermarket I had often visited as a child.

“When I was a kid, this place was my hangout. Back when I smoked like crazy in middle school, the old lady here was so old that…”

A gleaming foreign car was parked in front of the supermarket. A man and woman who had been talking together stopped when they saw me.

No—the man was the one who stopped.

He tilted his head, then approached me and asked,

“Do you know me?”
## Chapter artifact 91

# Chapter 91

“Do you know me?”

I asked the approaching man a question in return.

“Who are you?”

*At least introduce yourself before asking something like that, shouldn’t you?*

Maybe my bewilderment had shown clearly on my face, because the man slid his dark sunglasses down. A handsome face with a lightly tanned complexion appeared beneath them.

“Park Jihoon.”

Park Jihoon? Well, it wasn’t as if I had only met one or two people over the years.

More importantly, I didn’t recognize him at all.

“I’m sorry, but I think you have me confused with someone else.”

“I don’t. It’s definitely you. Didn’t you attend Garam Middle School?”

“Huh?”

That was the name of the school I had attended. I had moved away before graduating and lost touch with everyone there, but my memories of it were still vivid.

“Right? Garam Middle School. You’re twenty-seven this year.”

“Yes, that’s true, but…”

“Then it is you! Jin Taekyung from Class 6, Third Year!”

He even remembered my name, grade, and class—details I barely remembered myself.

At that point, I couldn’t deny it. I asked the sunglasses-wearing man, who was grinning from ear to ear,

“…Do you really know me?”

“I’m Jihoon. Park Jihoon! We played soccer together all the time in middle school! We were always getting called to the homeroom teacher’s office because we were bad at studying, and then the two of us would get smacked around. You don’t remember?”

Soccer? Getting beaten by our homeroom teacher?

I opened my mouth, wondering if it could really be him.

“Park Jihwang?”

“That’s right, you punk. I’m Park Jihwang! Ah, right. You wouldn’t know that I changed my name.”

“Of course I wouldn’t.”

I didn’t know Park Jihoon, but I knew Park Jihwang.

I never expected to meet one of my middle school classmates here. A smile naturally spread across my face.

“Wow, meeting you here. Some guy I’d never seen before came up and acted like he knew me, so I was wondering what was going on.”

“Shouldn’t you have recognized me anyway? It’s not like we were in kindergarten together. It was only ten years ago.”

“Even if it had only been five years, I wouldn’t have recognized you. Your face has changed too much.”

“Has it? Ha-ha.”

It was an undeniable fact. The scrawny kid with the dark complexion had turned into someone who could probably be called handsome wherever he went.

“You didn’t just get better-looking. You got a better body, too?”

“Oh, you have a good eye.”

“It’s basic observation.”

As far as I remembered, he had been about a head shorter than me. Now, our eye levels were roughly the same.

“Damn, you really made it big.”

An unrecognizably changed face, a solid build, a pretty girlfriend, and a foreign car that looked like it would easily cost a hundred million won.

Jihwang—or Jihoon—had changed a great deal in the ten years since we had last met. And I knew why.

*This guy is a Hunter, too.*

Now that my Qi Sense had reached a higher realm, I could assess people even without using the System.

*Is it that I can feel his qi?*

There was no doubt about it. He was a Hunter. He seemed about as strong as Im Changsoo—or perhaps even stronger.

*A friend I haven’t seen in ten years turns out to be a Hunter. How strange.*

I could even use Qi Sense to read his Level, but I didn’t feel like going that far.

I had met an old friend in a place filled with memories. Right now, I was neither a Hunter nor a martial artist.

I was just an ordinary Jin Taekyung.

“Anyway, it’s really good to see you. You know I was really upset when we lost touch right after you transferred, right?”

“Was I? Things were so chaotic back then.”

I had been sixteen at the time. I was right in the middle of adolescence, and my head had been a mess because my father had just died.

After entering high school, I focused entirely on training with the goal of attending a college of physical education. I naturally lost touch with the friends I had known before.

“Ah, right. Things were like that back then. I’m sorry.”

Maybe he thought he had made a mistake, because Jihwang’s—or Jihoon’s—smile turned awkward.

“What are you apologizing for? It was my fault for not getting in touch sooner. But do you still live around here?”

“My whole family lives in Seoul now. I stopped by because I remembered this place while returning from a trip with my girlfriend.”

“Wow. What a triumphant return.”

“Don’t make it sound so embarrassing. I still have a long way to go before I can call myself successful.”

“You’ve already succeeded plenty. What more could you want?”

We continued talking with smiles on our faces. Most of what we discussed were memories from middle school, but that alone was enough to make the time enjoyable.

A considerable amount of time passed before Jihoon’s girlfriend subtly hinted that her legs were hurting.

“Oppa, my legs hurt.”

“Hm? Then do you want to wait in the car? I’ll talk a little longer and be right there.”

“…Is that really something you should say?”

I had no intention whatsoever of interfering with my friend’s love life, so I took the hint and waved my hand.

“No, let’s talk about the rest next time.”

“Next time? Didn’t you say something like that ten years ago, too? You said you’d contact me next time, then left and never contacted me once.”

I had nothing to say to that. As I stood there smacking my lips, Jihoon held out a business card.

“Forget it. Call this number right now.”

> Myeongdong Guild, Team 1  
> Hunter Park Jihoon

Myeongdong Guild might not have been one of Korea’s top ten Guilds, but it was easily one of the top twenty—a major Guild.

And being part of Team 1 meant he was an elite recognized even within Myeongdong Guild. He could probably transfer to any respectable mid-sized Guild and become a Team Leader without breaking a sweat.

*I expected him to be doing well, but this is more than I imagined.*

I hid my surprise and called the number on the card.

Bzzzz.

Jihoon checked his smartphone and grinned.

“I’ll call you. We have to grab a drink sometime.”

“We’ll see. If I’m busy, I won’t be able to make it. If I have time, I’ll go.”

“What kind of answer is that? Your name came up at the last class reunion. People were asking what you were doing these days.”

“My name came up?”

“Why do you sound so surprised? You were popular with the other kids.”

“Was I? I spent all day on the field, so I guess I was friendly with the boys, at least.”

“You were popular with the girls, too. There were a few girls who had crushes on you back then. You never noticed?”

“…Really?”

“Everyone in the class knew. Why were you the only one who didn’t?”

*Damn. They should’ve told me sooner…*

No, that didn’t matter now that I had Ms. Songi. I was devoted. Now that I had met my destined partner, none of that mattered.

“We’re planning to get together soon, so come if I call you. You can meet your fan club, too. Okay?”

“O-Okay.”

*Yeah, I’m only going to see their faces. They’re just old classmates.*

Jihoon gave me a quiet laugh, then opened the driver’s-side door before suddenly stopping.

“It was good seeing you.”

“Huh? Oh, yeah.”

“See you again.”

Vroom.

As I watched the car disappear with the roar of its large engine, a thought suddenly occurred to me.

“Were we really that close?”

* * *

“They really seemed like childhood best friends.”

“Who? Oh, Taekyung?”

“Who else would I be talking about?”

“Why are you talking like that? Did you not like him?”

“Yeah. I didn’t want to say it because he’s your friend, Oppa, but honestly, he was kind of off.”

“That’s strange. He was really popular when he was young.”

“Why?”

“There were plenty of reasons. He was tall, had a good build, and was great at sports. He wasn’t exactly bad-looking, either. His only problem was that he was completely oblivious when it came to romance.”

“Hmm. I didn’t care for him. Doesn’t he look too much like a complete unemployed bum? What does he do for a living?”

“Hmm. I forgot to ask. He dreamed of becoming a physical education teacher when he was young, so maybe he went into that field.”

“He’s twenty-seven, though, and a man… Is he still in college? Studying for some exam?”

“I don’t know. Neither do I.”

“Maybe it’s because I’m with you, but other men don’t catch my eye. You’re handsome, kind, and incredibly capable.”

“Even if it’s just lip service, that’s nice to hear.”

“I’m not saying it just to flatter you. You’re a hundred times better than that friend of yours who only looks presentable.”

“Don’t say that. He’s a good guy.”

“You said it was the first time you’d met in ten years. He was even the one who stopped contacting you first. Were you really that close that you still speak well of him?”

Park Jihoon smiled gently.

“No. Not at all.”

* * *

“What do you think?”

The real estate agent asked in a phlegmy voice. He had chain-smoked for an hour while waiting for me, and his complexion looked terrible.

“It’s nice.”

I wasn’t just being polite. The two-story detached house with a broad lawn was better than any house I had seen so far.

*Four bedrooms and two bathrooms. The living room is spacious, too.*

It looked like something out of a fairy tale. I toured the house while listening to the real estate agent explain every detail, then stepped out through the front gate.

“Listings like this are hard to find. The current owner has several buildings, but he’s putting this one up as a quick sale because he’s planning to put up another building in Incheon.”

“So what’s the market price?”

“Exactly what you saw online. 3.38 billion won.”

It was still an amount that made me want to swear, but the house was worth every bit of it.

For my family’s safety, and because this place held special meaning for us.

“Please contact me.”

“Then…?”

“I’ll buy it.”

“Oh, you’ve made a wonderful decision, Boss!”

I firmly shook the hand the man held out.

“Since we’re on the subject, would it be all right if I took another look around the neighborhood?”

“…”

“I’m joking.”

Just because I had said one thing, look at how tightly his hand clenched.

* * *

“Have a safe trip home.”

“Yes. Take care.”

I left the real estate office after putting down the ten-percent deposit. I had agreed with the owner to set a date soon and proceed with the formal purchase. Since he needed cash quickly, the negotiations had moved along fast.

*I’ll have to put off moving for a while.*

The house was about an hour away from where my family lived now. Even though I had purchased it, moving immediately would be difficult.

More importantly, Hayeon had her college entrance exam this year.

I would surprise them with the news immediately afterward.

*I’ll have to remodel it, too.*

I intended to make it as similar as possible to our old home. It had happened a very long time ago, but perhaps because we had lived there for sixteen years, I remembered the layout perfectly.

*I’ll sign the formal contract and find an interior contractor… What else is there?*

I knew how to wield a spear in a Gate, but I was a complete novice when it came to this sort of thing. I had no idea where to start.

I was turning into a dark alley while thinking about this and that when—

*Hm?*

The back of my neck began to tingle. The fine hairs on my body stood up, and it felt as if the air had shifted.

I sensed someone secretly watching me from behind.

*Open Inventory. Summon.*

I spun around like lightning, a dagger already in my hand. But then…

Meow.

“What the hell? A cat?”

Meow.

A mottled cat jumped down from the wall.

It glanced at me, then slowly wandered away.

*Was I overreacting?*

As my senses improved, I had become more sensitive. I was supposed to gradually grow accustomed to it alongside my growth, but my growth had been too fast for any adjustment period to have meaning.

*No. It felt strange this time.*

I belatedly raised my Qi Sense, but there was nothing in the deserted alley.

Beep.

> **System**
>
> There are no targets for **Qi Sense** to detect.

If the System said that was the case, then it must be true. I must have been especially tired lately.

“Ah, now I suddenly have a craving for samgyetang.[^1]”

Since I had thought of it, should I go out to eat with my family?

Thinking about tender meat and hot broth made my steps feel lighter.

[^1]: Samgyetang is Korean ginseng chicken soup, traditionally served hot.

* * *

In a dark little room, a young man who had been meditating suddenly opened his eyes.

“Gasp!”

His hair stuck out in every direction, soaked with sweat, and his breathing was ragged. He hurriedly drank bottled water, then let out a relieved sigh.

“Fuck, that scared the hell out of me.”

Everything had gone smoothly. No, it had been boring enough to be tedious.

The investigation target happened to be on vacation, and his movements were predictable. Home, convenience store, home. Today, he had traveled as far as an hour away, but tracking him had still been no trouble.

But then…

“What the fuck was that? Why did that bastard suddenly turn around and start pulling that shit?”

The moment he saw that sharp gaze, his heart had dropped. If he had not hurriedly severed the Link with the cat, he might really have been discovered.

“He didn’t know, did he?”

The target was only a C-rank Hunter. Compared to the people he had investigated until now, he was far below them.

*There’s no way. Who do you think I am?*

Hong Woojin, a B-rank mage and information broker, shook his head.

He was a master of tracking and surveillance magic. He could not use flashy attack magic, but when it came to this field, he took pride in being the best.

“That’s right. There’s no way. It was just a coincidence. A coincidence.”

Hong Woojin muttered the words like a mantra. Anxiety lingered in his voice.
## Chapter artifact 92

# Chapter 92

> **Target Report**
>
> **Name:** Jin Taekyung
>
> **Age:** 27
>
> **Residence:** Address xxx-xxx, Hope Goshiwon[^1]. Living separately from his family.
>
> **Family:** Eldest son in a family of one son and one daughter. Father died in an accident eleven years ago. Information on his mother and younger sister attached separately.

This was the report Im Chunsoo received three days after ordering the investigation. After reading through the densely packed information filling five pages, he opened his mouth.

“Hey, Team 1 Leader.”

“Yes, Guild Master.”

The Team 1 Leader seated across from him answered. Apart from Guild Master Im Chunsoo, he was the only A-rank Hunter in Sangdong Guild, as well as Im Chunsoo’s loyal right hand.

“Did you read this report?”

“Not yet.”

“Why not?”

“Because it was your order, Guild Master. You told us to report any information that came in without filtering it along the way.”

“Then read it now.”

The Team 1 Leader politely accepted the report Im Chunsoo held out to him. His eyes moved rapidly across the pages. About ten minutes later, he raised his head and muttered,

“This is a little…”

“What do you think of the report?”

“I can only follow your judgment, Guild Master.”

“No. Speak frankly.”

After a brief hesitation, the Team 1 Leader answered.

“I think the information is incorrect.”

“Which part, exactly?”

“The subject of the report, Jin Taekyung, was an F-rank Hunter until only half a month ago. However, he succeeded in reawakening as a C-rank Hunter. That much is rare, but not impossible.”

“Go on.”

“But according to the testimony of Team Leader Im Changsoo—no, Hunter Im Changsoo—and the others who participated in that raid, Jin Taekyung single-handedly defeated a group of B-rank monsters, the Minotaurs.”

“Minimum five. Maximum ten, if I remember correctly?”

“Yes. They even said he brought down the boss monster with a single strike.”

“Right. A mere C-rank Hunter taking down a Minotaur Warrior with one blow. Does that make any sense?”

“I don’t think it does.”

“Then what is it?”

He was not asking because he genuinely did not know. He only wanted to confirm once again whether the Team 1 Leader was thinking the same thing he was.

“There are three things that concern me.”

“List them.”

“First, the report may be wrong.”

“Who wrote this report? Hong… What was it? Definitely not Hong Gil-dong.”

“Hong Woojin. He’s still young and doesn’t have much experience, but his ability is well known.”

“Right, that Hong Woojin—or Hong Gil-dong, or whatever the hell his name is. Check with that bastard again. Put some pressure on him, too. Anyway, what’s the second?”

“Second, Hunter Im Changsoo and the others may have coordinated their stories and lied.”

“Changsoo’s an idiot who can’t think straight, but he’s never lied to me in his life. Continue.”

“The last possibility is that Jin Taekyung is an A-rank Hunter whose strength has not yet been confirmed, or perhaps…”

A troubled look crossed the otherwise calm Team 1 Leader’s face. After a moment, he hesitantly opened his mouth.

“Could he be a third-awakening Hunter?”

“Third awakening?”

“…Yes.”

“Team 1 Leader. Doesn’t it sound absurd even to you? A third-awakening Hunter? Does that make any sense?”

The Team 1 Leader answered by lowering his head.

Im Chunsoo clicked his tongue at the sight and picked up the report. Extreme cold began to flow from his fingertips.

Crackle. Crash!

“Rewrite the report. Finish it by the end of this week and put it on my desk when you come in on Monday. Make it nice and clean.”

“Yes, sir.”

“And what about the information on the other people from that Peace Guild—or was it Love Guild?”

“……I was just about to report on that.”

“What? You haven’t found out anything?”

“We’ve finished identifying everyone except for three people.”

Im Chunsoo frowned.

“Three? One of them must be Jin Taekyung. Who are the other two?”

“The Guild Master and Team Leader of Peace Guild.”

He had heard about them from his son. The young Team Leader was an insolent brat, while the middle-aged Guild Master was a clueless man who had done nothing but chuckle throughout the entire raid.

“Why those two?”

“There was a Lock on them.”

“What?”

“Exactly as I said. Not only their personal information, but even their account details are all under security restrictions. The Audit Team is at a loss as well.”

“Did you skimp on the money?”

“Not at all. I already gave them plenty…”

“And yet?”

“They seem very reluctant on their end as well. They said an upper agency had placed the security lock, making it difficult for them to touch.”

Im Chunsoo was dumbfounded.

A Guild that had not even existed for a month. A small Guild whose entire membership could not even make up one raid team. No, at that point, calling it a Guild was strange. It would not have been odd to call it a social club instead.

And yet, who the hell were those bastards to have a Lock placed on them?

“Huh. Look at these bastards.”

“What should we do?”

“Don’t dig any deeper into that part for now. Leave it alone. And make absolutely sure the people we paid this time keep their mouths shut.”

During the Great Cataclysm, Im Chunsoo had been famous for his fiery temper. But after running a Guild, he had learned one important thing.

To achieve a goal—and to gain results beyond that goal—one had to remain calm and cautious.

“So everything else is completely investigated?”

“Yes. Completely.”

That was the answer of the Team 1 Leader, who had earned Im Chunsoo’s trust through his meticulous nature. Im Chunsoo nodded.

“Deal with those two locked targets as I said. For now, focus only on Jin Taekyung. Mobilize a few people from the Guild Audit Team and increase the surveillance separately.”

“Separately…?”

“Yes. Looking at the state of this report, it’s no good. When you think about it, our Guild Audit Team isn’t exactly outclassed, is it?”

“That’s true, but…”

The Team 1 Leader suddenly hesitated. He remembered what Hong Woojin had repeatedly stressed when he went to commission Woojin for the job.

> “The moment I accept this assignment, it becomes my job. Got it? Within a week, I’ll find out the color of this bastard’s underwear on the day in question, so leave it to me. If you cause trouble on your end and the surveillance target catches on, you’ll ruin my job.”

Hong Woojin had little experience, but word had spread that he was good at his work. Despite Woojin’s arrogant way of speaking, his professionalism had inspired trust, and the Team 1 Leader had personally given him his word.

*I should probably tell him.*

But the objection the Team 1 Leader was about to raise went straight back down his throat at Im Chunsoo’s next words.

“Why? Is there something else you want to say?”

“Oh, no, sir. I’ll relay it exactly as you said.”

“Good. You can go.”

Im Chunsoo had been in a bad mood lately. It was the Team 1 Leader’s job to keep him appeased as much as possible and guide him in a favorable direction.

*It’ll be fine, right? It will be.*

Even after leaving the Guild Master’s office, the Team 1 Leader could not shake his uneasy feeling.

* * *

Home. Vacation.

Just thinking about those two words made me happy. And in reality, it was just as wonderful. But…

Bzzzz. Bzzzzzz.

“Ah, this is driving me crazy.”

I swatted at a fly with lightning-fast speed. It was not an ordinary palm strike, either—my palm was charged with internal energy. After killing the fly instantly, I tossed it into the trash and returned to the sofa.

“Why the hell are there so many flies?”

Hayeon, who had briefly come out into the living room to get a drink of water, let out a deep sigh.

“It’s summer, you idiot, Oppa.”

“It’s not just that.”

“What’s the big deal? How many could there be? There was only one just now.”

“That’s the problem. They keep coming in one at a time. Every time I catch one, another one keeps coming in from somewhere.”

“How many have you caught?”

“I swear to heaven, I’ve caught at least a hundred since this morning.”

“Look at you exaggerating. This is why men are…”

“I’m serious!”

“Okay, okay.”

Damn, this was driving me crazy. I tore at my hair and swatted down another fly. A hundred? I was not exaggerating at all. What had happened to this neighborhood that so many flies could swarm into one house?

*Did someone smear honey on the windows?*

At first, they had only been annoying. Just like Hayeon had said, I thought it was a normal phenomenon because it was summer.

But the more time passed, the more I realized that something was strange.

*It was after I’d killed about thirty of them.*

These damn things kept coming in without a break! I would kill one, then another would come in. I would kill that one, and a different fly would take its place.

Even after closing every window in the house and searching with my Qi Sense, the nightmare of the fly army continued.

Bzzzzzz.

“See? Another one came in before we could even turn around. Where the hell are these things coming from?”

I carefully searched for some tiny gap I had failed to notice, but I could not figure it out. They seemed to be coming through spaces barely large enough for a single ant to pass through.

“Don’t swat them. Just leave them alone. Then they’ll quiet down.”

“What kind of creative bullshit is that? You think they’ll stay still just because you leave them alone? We won’t be able to sleep with all that buzzing.”

“The flies in my room stay still.”

“What?”

“There are about three in my room, too. They bothered me at first, so I thought about killing them, but when I left them alone, they stopped flying around and just sat on my desk.”

“That’s only temporary. They must fly around like crazy when you’re not looking.”

“I think they’re just lazy flies. They haven’t moved even once.”

“Say something that makes sense.”

“I’m serious. Want to bet a hundred thousand won?”

“You even have a hundred thousand won? You’re an examinee.”

“Of course I do. It’s from the money you gave me last time.”

“You’re going to bet against me with the allowance I gave you?”

“If you’re scared, you can just die.”

“……Deal.”

Shit. So this was how money went around in circles.

We went straight to Hayeon’s room. She pointed at a fly sitting quietly in place and grinned triumphantly.

“See? I was right, wasn’t I? Hand over the hundred thousand won.”

“Hand over what? We need to run an experiment first.”

I brought my palm down over the fly. I struck at an ordinary person’s speed, slow enough for the fly to dodge easily. But then…

Flinch. Scramble.

The fly startled violently and scurried away, moving its legs as fast as it could.

I could not hide my bewilderment. Hayeon wore a similar expression.

“Sis.”

“Y-Yeah?”

“Are all flies these days like that?”

“Th-They could be, couldn’t they? Anyway, give me the hundred thousand won.”

“I’ll give it to you. I will. But isn’t that fly strange?”

“A fly is a fly. It’s just a weird one.”

“What kind of fly acts like that? I’ve seen goblins and Minotaurs in my life, but I’ve never seen a fly that flies around so little.”

The instant I finished speaking—

Bzzzzzz—

“……”

“……”

Suspicious. Extremely suspicious.

The timing was questionable enough, but the way its wings moved—as if it were trying hard to look ordinary—was even stranger. Even its flight was awkward and unsteady.

*Forget that. It gives me the creeps. This feeling is weirdly familiar.*

Where had I felt something similar?

Oh, right. That alley I had walked through on the way home two days ago, after looking at a house.

That déjà vu of someone secretly watching me.

*Am I really just being oversensitive?*

I glared at the fly and raised my Qi Sense. Its activation range now extended to a radius of seventy meters, spreading into every corner of the house.

And then something no one could have expected happened.

Ding. Ding. Ding.

> **System**
>
> Lv. 1 Housefly—Familiar
>
> Lv. 1 Black Blow Fly—Familiar
>
> Lv. 1 Green Bottle Fly—Familiar

“……?”

*What the hell is this?*

[^1]: A goshiwon is a very small, inexpensive room-for-rent housing arrangement.
## Chapter artifact 93

# Chapter 93

*What a bunch of amateurs.*

Hong Woojin was furious enough to burst. If he had entered the cat’s body like last time, he would have puffed up its fur and hissed.

But right now, he was a rice weevil smaller than a fingernail. The most he could do to express his anger was hide in the gap beneath the refrigerator and wriggle.

Bzzzzzz.

*That bastard’s coming in again.*

The target of his anger was the fly that kept entering the house.

Woojin did not know who was behind them, but whoever it was seemed to think they were being careful by sneaking the flies in one at a time. Instead, they were only putting Jin Taekyung further on guard.

“Ugh, these damn flies.”

Whoosh. Smack!

A predictable end. Hong Woojin grew anxious, worried that Jin Taekyung might notice him.

*Bastards like that have no professional courtesy, and they’re stupid on top of it.*

Most Hunters would never have noticed, but he recognized it immediately.

That fly was a Familiar being controlled by a mage. The proof was the incredibly faint mana that only another mage could sense.

*Who hired the bastard? Sangdong Guild, after all?*

If that was the case, he would have to quit this assignment right away. He was a professional with immense pride in his abilities.

He could not tolerate an intruder interfering with his sacred workspace.

*I told them over and over…*

No matter how well you handled a job, there were times when a single loach released by an impatient client muddied the water. Just like now.

“Are all flies like that these days?”

“Th-They could be, couldn’t they? Anyway, give me the hundred thousand won.”

“I will. I’ll give it to you, but… don’t you think that fly’s a little strange?”

Damn it. He knew this would happen.

Swallowing his curses, Hong Woojin hurriedly moved his body. He was wriggling deeper into a place no human eyes could reach when—

A jolt.

*…Huh?*

He was seized by a strange sensation, as if his body had suddenly floated into the air. It had never happened once since he began using Familiar magic.

*Is it because this Familiar is too small?*

The sensation lasted only an instant, but Hong Woojin could not shake off his unease. For a moment, he wondered whether it had been some kind of detection spell, but he soon shook his head.

*It definitely wasn’t magic.*

That was not merely because Jin Taekyung was a non-mage Hunter. After all, this was a world where anyone could obtain magical equipment if they had enough money.

But mages recognized their own kind. As a B-rank mage, there was no way he could fail to distinguish a detection spell.

*The connection must have weakened for a moment. Yes. That has to be it.*

The decisive reason he convinced himself it had been a simple illusion was Jin Taekyung’s reaction.

“Maybe its wing’s injured. This fly’s looking pretty weak.”

Smack!

With a crisp sound, Jin Taekyung returned to the living room and sprawled out on the sofa. He chuckled at a variety show for a while, but soon the house was filled with loud snoring instead of laughter.

Grrrrr. Grrrrr.

Only then did Hong Woojin relax.

*Of course. What could a C-rank Hunter who was an F-rank until recently possibly know? What happened two days ago must have been a complete coincidence, too.*

The incident from two days ago still lingered in the back of his mind. He had been watching Jin Taekyung through a cat Familiar and had been startled by what happened. For some reason, it had continued to bother him ever since. Now, at last, he felt he could breathe a little easier.

*If he can’t even recognize a shoddy Familiar like this, then that says it all.*

There was only one problem: the lazy bastard had no intention of moving at all…

*I’ll have to monitor him a little more boldly from now on.*

Hong Woojin had chosen a rice weevil from among all the living creatures in the world because he had retained a sliver of caution toward Jin Taekyung.

But now, it seemed safe to leave the body of this tiny, painfully slow insect.

*Let’s meet in a different form tomorrow, Jin Taekyung.*

Pop.

Hong Woojin severed the Link. The creature hiding beneath the refrigerator was no longer a Familiar. It was nothing more than a small, fragile rice weevil.

And then—

Grrrrr…

Jin Taekyung’s snoring gradually faded before stopping altogether.

* * *

A faint presence disappeared. I could sense the change only because I was using every one of my senses.

*Did he leave?*

I opened my eyes while pretending to stretch. The first place I looked was the gap beneath the refrigerator.

> **System**
>
> Lv. 1 Rice Weevil

Only ten minutes ago, its Level window had carried the tag “Familiar.” Not anymore—not with the Link severed.

“Yaaawn. Is there anything to eat…?”

I got up from the sofa and casually walked around the house. Only then could I be certain.

*There aren’t any Familiars left.*

The only things caught by my Qi Sense were a few ordinary flying insects. There was no Familiar anywhere.

The buzzing of wings that had continued without pause had stopped, too.

They had probably gotten spooked by what just happened, so at least they would not show their faces for the rest of the day.

*Damn it. A Familiar?*

Familiar magic.

It was a kind of mental magic used by mages. The caster formed a mental connection with the creature chosen as a Familiar and, depending on the caster’s skill, could even control it at will.

*That was my first time experiencing it firsthand.*

A melee Hunter was not automatically a master of every weapon, and mages were the same. Mental magic, in particular, was said to be among the more difficult branches.

*Why would people like that come after me?*

The reason I thought of them as “people” rather than “someone” was that there had been two Familiars. The two could have been working together, or they might not have been.

Still, I had a rough idea of who had sent them.

*Who else could it be but Sangdong Guild?*

The only place I had formed some kind of grudge against in the real world was Sangdong Guild. More precisely, Im Changsoo.

*When you mess with someone’s child, the father comes running.*

Im Chunsoo, the A-rank Hunter known for being cold-blooded and foul-tempered.

If what happened today was his order, this would not end easily.

But…

*I can’t just sit back and take it.*

I could let the fact that they had followed me two days ago go. I could tolerate that.

But I could not tolerate what happened today. This was my home, the place where my beloved family lived. They had touched my one inviolable boundary.

*How should I screw these bastards over…?*

I was thinking about it when Hayeon’s bedroom door flew open.

Her face was stiff. Had they used a Familiar to pull something behind my back? My thoughts grew frantic.

“Oppa.”

“What is it? What happened? Is there something strange in your room?”

“No, it’s not that.”

“Then what is it?”

“Why haven’t you given me the hundred thousand won?”

“…”

Right. I had been underestimating you far too much.

* * *

The next morning, I left the house as soon as dawn broke.

My eyes felt gritty from staying alert all night in preparation for another Familiar’s intrusion with Qi Sense, but I shook off the fatigue by circulating my qi.

“Where should I take you?”

“Ilsan Lafesta, please.”

The taxi sped along the wide-open roads without a hitch, reaching the destination much faster than I had expected.

*Is this my first time coming to the Store since I visited once a few years ago?*

The Store, located in the center of Ilsan, stood out clearly even from a distance. For one thing, it was overwhelmingly larger and more splendid than the shops around it.

There was another thing that set it apart from ordinary stores. At the entrance, guards in suits were screening the customers.

“Sir, we’re adults, I’m telling you!”

“No.”

“We’re adults, so why aren’t we allowed inside?”

“Because the fingerprint scanner says you’re not adults.”

“Isn’t it defective?”

“No.”

“Ah, shit, just let us in!”

“‘Shit’?”

Five or six teenagers who looked obviously young flinched and took a step back.

“…What?”

“Is that any way to treat customers?”

“Customers? Ha. You little shits, seriously.”

The guard rubbed the corners of his eyes with a weary expression. He was not an ordinary adult man but a hired guard Hunter. Even if a whole crowd of professional fighters came instead of five or six minors, they would not be able to force their way in.

“Customers to me are Hunters or civilian adults who’ve been issued membership cards. Not high school punks like you.”

“…”

“Are you leaving while I’m asking nicely, or should I call the police?”

People like that existed everywhere. Especially in a Store filled with all kinds of goods ordinary people could never access.

“…Hey, hey. Let’s go.”

Only after the kids loitering in front had left did the guard notice me. He addressed me politely.

“What brings you here?”

“I’d like to purchase something.”

“Please present your membership card or Hunter certification.”

“Here.”

“I’ll need to complete the verification process.”

Only after my certification had been checked and my fingerprints scanned was I given an admission pass.

“As a C-rank Hunter, you may access up to the third floor.”

The items stocked on each floor of the Store were different. I had visited once when I was an F-rank Hunter, but the second floor had been the highest I could access at the time. I had never even gotten to look around above it.

“Have a pleasant time.”

“Thank you. Have a good one.”

Once I passed through the doors, I saw endless rows of glass display cases.

The space was incomparably larger than an ordinary shop. Yet there were only a handful of customers in sight.

*Well, it would be strange if this place were crowded.*

The people who could use this place were an extremely small minority: Hunters, who made up only 0.1 percent of Korea’s total population, and civilians with enough social influence to be issued membership cards.

They were the Store’s main customers.

“This item was manufactured by domestic S Company and has a built-in alarm spell, making it useful for security…”

“This brooch was made by overseas M Company. With its beautiful, tasteful design and built-in shield spell, it’s perfect for your wife’s personal protection…”

The employees were busy explaining their products to customers.

That was right. The Store was a kind of luxury department store where people could buy expensive magical goods that were difficult to obtain through ordinary channels.

“Then I’ll take that one and this one. Bring me that, too.”

“Don’t you have anything with better performance? Don’t worry about the price. Bring me some options.”

There might not have been many customers, but their purchasing power was unmatched.

I was staring blankly at people buying goods that cost at least several million won when a pretty female employee approached and bowed.

“Hello. I’m Assistant Manager Kim Seonhee from the Ilsan Store. I’ll be assisting you today.”

“Ah, yes.”

She had treated me politely the last time I visited, too, but not to this extent.

Now that I was a C-rank Hunter, the customer service was considerably more lavish.

“Is there a particular product you’re looking for?”

“I’d like to buy some raid equipment.”

The employee’s expression brightened. The Store carried countless magical goods, but Hunter equipment was among the most expensive of them all.

And I was a C-rank Hunter. Even a mid-level Hunter could spend hundreds of millions of won on a single piece of equipment.

Naturally, a sales employee would be delighted at the thought of adding that kind of sale to her record.

“I’ll show you to the third floor.”

As she turned toward the escalators, I spoke.

“No, please take me to the second floor.”

“Pardon? But to purchase C-rank Hunter equipment, you’ll need to go to the third floor…”

“It’s fine. I’m looking for weapons for low-rank Hunters.”

I pretended not to notice her expression darkening and stepped onto the escalator first.

*I wonder if they have anything useful for killing rats.*

The time had come to fill my Inventory.

* * *

“It’s fine. I’m looking for weapons for low-rank Hunters.”

Assistant Manager Kim Seonhee secretly sighed at the customer’s words. As someone who was unusually concerned with her sales numbers, this was far from welcome news.

*I need a good sales record this month if I want to get promoted.*

The colleague who had joined the company at the same time as her, but worked at the Seoul branch, was already a Team Leader. Whether it was because of luck or business savvy, every customer she encountered was apparently a big spender.

Compared to her…

“This one looks good.”

“Ah, yes. This product was manufactured using an F-rank Magic Gem…”

Kim Seonhee quickly pulled herself together and began her explanation. The customer had picked up a dagger with a black-painted blade.

Compared to the other weapons, it was nothing special. It did not even have magic embedded in it. It was just an ordinary consumable.

“How much is it?”

“It’s currently on sale as part of our summer promotion, so we’re offering it at the reasonable price of 520,000 won.”

“Hmm. That’s expensive.”

“…”

What was the annual salary of a C-rank Hunter again? Didn’t their basic allowances alone amount to several hundred million won? Kim Seonhee found it ridiculous, but silently waited for the customer to make his choice.

“Ah, well, I guess it can’t be helped. I’ll buy it. Give me one.”

“…Yes.”

The look on his face, as if parting with the money were killing him, was utterly obnoxious. Kim Seonhee was silently cursing him to herself as she picked up the dagger when—

“No. Not that one.”

“Excuse me?”

“The one next to it.”

Her gaze shifted to the side. One hundred daggers were neatly arranged inside a storage box.

“They’re the same product, sir.”

“I know. Give me one of those.”

“…Are you referring to that storage box?”

“Yes. Give me one box of those. And one box of that, too. And that one…”

That was the moment Assistant Manager Kim Seonhee’s worries about her sales numbers disappeared.
## Chapter artifact 94

# Chapter 94

“Three hundred fifty million won.”

The employee’s voice trembled as she ran the payment, and so did my hand as I handed over the card.

*Good lord. Three hundred fifty million won?* I had just spent three years’ worth of salary from back when I worked like a dog in barely an hour.

*No. Let’s look on the bright side.*

This was money spent to protect my family from the people watching us.

I could keep earning money from now on, anyway, and I could use the things I bought today for a long time.

Beep.

- Approval complete.

“Your payment has gone through.”

Thanks to me, this young lady was the only one who had hit the lottery. I took my card back from Assistant Manager Kim Seonhee, whose smile stretched from ear to ear.

“So that’s everything, right?”

“Ah, if you give us your address, we can have everything delivered.”

“That’s all right. I have somewhere to go right now.”

Delivery, my ass. The moment I got out of everyone’s sight, I could just store everything in my Inventory.

*The System sure is convenient at times like this.*

Thinking that, I accepted the shopping bags until both my hands were full. Of course, they weren’t ordinary paper bags. They were tough, sturdy leather shopping bags supposedly made from ogre hide. They had been free gifts, but instead of feeling happy, they just made my stomach hurt.

“Take care.”

“Please come back next time! We look forward to seeing you again.”

“…Ah, yes.”

I accepted the business card she held out while she bent at the waist at a perfect right angle.

*One obsessed with sales figures. Their name: salesperson.*

* * *

I stopped by a nearby restroom and stored the things I had bought at the Store in my Inventory before hailing a taxi. These days, I regretted never getting my driver’s license.

“Please take me to Apartment A in Ilsan.”

The moment I sat in the passenger seat, I pulled out my smartphone and started searching for information.

The search term was…

*Familiar.*

The moment I pressed the search button, related information came streaming onto the screen.

There was quite a bit of information that ordinary people couldn’t see and that required Hunter certification to access. One title in particular caught my eye.



No Joke: Don’t Use Familiar Magic. It Made My Hair Fall Out.



It was a title that resonated with my soul. There was no way I could not click it.

*Ah, so this was where it was posted.*

The post was on a famous domestic Hunter community site.

It had been selected as a monthly best post, with over one hundred thousand views and more than two thousand comments.

*Let’s see what it says.*

Click!



No Joke: Don’t Use Familiar Magic. It Made My Hair Fall Out.



I’m a currently active B-rank mage.

I’ve been in the business for a while and make decent money as a freelance Hunter. Please understand that I can’t reveal my exact specifications.

Anyway, the reason I’m writing this post is exactly what the title says.

I got hit by a hair-loss beam because of Familiar magic…

I’m still in my twenties, but the top of my head is classmates with a two-thousand-year-old mummy. Goddamn it.

Before anyone starts nitpicking, let me say this in advance: My family has always been blessed with thick hair. I even saw a photograph of my great-grandfather taken during the Japanese occupation, and he looked like Rapunzel of Joseon.

Anyway, back to Familiar magic. This stuff is a real double-edged sword.

Any of you guys who are mages will know this, but mental magic isn’t exactly common. Even civilians can make a living once they learn a skill.

For a mage, mental magic is exactly like that. If you have this one thing, you can live well no matter what.

But fuck, your hair starts falling out. It keeps falling out.

Anyone here ever tried washing their hair with a Superior Potion? I have.

You crazy bastards, I spent tens of millions of won washing my hair just once. I tried every kind of crazy shit imaginable, but even that only worked for a little while.

When none of it worked, I went to a regular doctor, and the bastard let out a long sigh and said:

“You’re a mental-magic mage, aren’t you?”

He said it exactly like that, without getting a single word wrong. I was shocked and asked how he knew, and then he told me something genuinely horrifying.

More than ninety percent of mental-magic mages suffer from hair loss, and the rate is one hundred percent among those who use the more difficult Familiar magic.

Apparently, because we overwork our brains like crazy, even people with thick hair turn into bald people at some point.

At first, I thought, *What the hell is he talking about?* But I looked into it, and it turned out to be true.

I hurriedly joined a mental-magic mage café and searched for people like me, only to find that ninety-eight of its one hundred members suffered from hair loss.

After hearing about my situation, they told me it was already too late. Potions only restore cells temporarily, so using them too often just ends up killing your hair-follicle cells.

I ignored the café’s promise to upgrade my membership if I wrote a review of my medical consultation, quit, and am searching for my own treatment method…

Three-line summary.

1. Mental-magic mage is great. But you lose your hair instead.

2. Potions are useless. Use hair-loss-prevention shampoo and go to a regular hospital instead. Hair must be treated with heart and desperation, not magic.

3. I will not give up.

That’s all.



“…”

After reading the entire thing, my vision grew blurry. So even the mages I had always envied, the people who seemed to have everything, had their own hardships.

“Are you all right, sir?”

“I’m fine… Hngh.”

“What’s wrong?”

“Ah, it’s nothing. I’m fine.”

Of all things, the taxi driver happened to be bald, too. Feeling like a sinner, I lowered my head toward my smartphone.

Below the post, I found more than two thousand comments.



Anonymous#232: Give us the one-line summary.

└ Author: [Comment hidden due to severe profanity.]



Anonymous#112: Is the person who made the first comment even human? I cried. I’ll be rooting for you. Hang in there.

└ Author: Thanks…



Anonymous#1512: I don’t know about the rest, but the second commenter seems to be suffering from hair loss, too. But after reading the whole thing, it sounds like you make a lot of money. Can’t you live without some hair? Just wear a good wig.

└ Author: [Comment hidden due to severe profanity.]



Anonymous#4885: Wow, I’m seeing a Familiar mage here. You guys don’t know this, but the author is a real aristocrat. Even among B-ranks, your income is incomparable. So is the way you’re treated.

└ Author: What good is having money when you don’t have any hair?

└ Anonymous#4885: Now that you mention it, you’re right.

└ Author: If you’re going to comfort me, see it through, you son of a bitch.

.

.

.



Moderator: Congratulations! You’ve been selected as a popular post!

└ Anonymous#5252: LMAOOOOOOOOOO

└ Anonymous#8984: LMAOOOOOOOOOOOOOOOOOOOOOOOOOO

└ Author: Am I supposed to laugh at this or not?

└ Anonymous#2652: You don’t have any hair and you still feel like laughing?

└ Author: [Comment hidden due to severe profanity.]



Author: Thanks for the overwhelming support. Looks like I’m about to make the monthly best list and enter the Hall of Fame. If you have any questions, leave them below. I’m working right now, but I’ll drop in and answer them whenever I get a chance.

└ Anonymous#9665: You said you’re a freelancer. What kind of work do you mainly do?

└ Author: Freelancer is a nice way of putting it. What I do is similar to running a private detective agency. I’ve tracked high-level criminals—Hunters, of course—and I’ve also taken on an affair case at a nouveau riche family’s house.

└ Anonymous#915: Oh… You must make a lot. How much do you earn?

└ Author: That depends on the job, obviously. Still, after working for a few years, I put up a building in Seoul. The house I live in now is also under my name.

└ Anonymous#5252: Show us proof of your house.

└ Author: I’m outside working right now. I’ll properly verify it later, so wait until then.

└ Anonymous#9882: What does working have to do with it? Familiars are remote-controlled anyway, aren’t they?

└ Author: Even remote control has a range limit, you idiot. Do you use the Wi-Fi at your house while traveling in the United States?

└ Anonymous#9882: Sorry.

└ Author: The maximum distance for a Familiar connection is five hundred meters. I’m increasing the distance little by little, but it’s difficult. If the Link is forcibly severed, my stomach starts churning and I feel like I’m going to throw up. There’s also a risk of mana backflow.

└ Anonymous#9882: So you always have to stay within five hundred meters.

└ Author: Yeah. To work safely, maybe three hundred meters? You have to prepare for anything that might happen. Most people probably do the same.



I was scrolling through the comments when I suddenly stopped.

It seemed I had unintentionally discovered some important information.

*The connection with a Familiar is severed if it goes beyond five hundred meters?*

The maximum distance was that much, and the safe working distance was three hundred meters.

In other words, if the author’s comments were true, then the people who had controlled the Familiars yesterday had been somewhere not far from my house.

*And they’d be going bald, too. Maybe completely bald.*

There was a strong possibility they were wearing wigs, but knowing that couldn’t hurt.

I continued searching for information about Familiar magic and was able to organize a few facts.

*For a B-rank mage, the maximum Familiar connection distance is five hundred meters. The safe distance is three hundred meters. If a Familiar dies, the Link is forcibly severed, and the caster also takes a slight hit.*

And I realized one more thing: why they had gone out of their way to use an expensive Familiar mage to watch me.

*What? Tiny Familiars don’t get caught by most detection magic?*

It was like this: detection magic was a net, while tiny Familiars like flies and rice weevils were too small to get caught in it.

Of course, there were products with built-in top-of-the-line detection magic capable of detecting even those, but when I looked them up, they cost five hundred fifty million won as part of a summer special.

“…”

I had no idea which part of that was supposed to be a summer special. I already had plenty of places where money would be going from now on. Five hundred million won, my ass.

*That’s one more reason I have to catch them myself.*

My thoughts suddenly turned to the other Guild members, too. Had Familiars been attached only to my family?

I still didn’t know the exact identity of the person who had commissioned this. Sangdong Guild was only the prime suspect.

“That’ll be 8,400 won.”

“Ah, yes. Here you go.”

I paid the taxi fare and got out. The entrance to the apartment complex, which had always looked exactly the same, seemed a little unfamiliar today.

The presence of the watcher bothered me like a thorn lodged in my throat.

*Should I contact Team Leader Choi?*

I was looking at his number saved on my smartphone when—

“Oppa!”

A familiar “swan”[^1] in a green tracksuit and round glasses, her greasy hair tied tightly back, waved at me.

[^1]: In Korean slang, a “swan” is an unemployed woman.

“Oh, y-yeah.”

“What’s with that reaction?”

“I guess I’d rather not acknowledge knowing you in public. You could say I’m embarrassed…”

“Are you embarrassed by your one and only little sister? Huh?”

“Go buy some clothes. What are you doing wearing a tracksuit again when you left the clothes you bought at the department store last time at home?”

“You should worry about yourself. You’re one to talk, when you go around wearing the same kinds of clothes every day.”

Hayeon’s pointed remark left me speechless for a moment. I had paid three hundred million won only an hour or two ago, but I was still wearing nothing but jeans and a T-shirt. Apparently, the old grime of being an ordinary little citizen, caked on over twenty-seven years, had not yet completely washed off.

“W-Well, anyway. Where are you headed?”

“Where am I going? The convenience store!”

Hayeon, who had been sulking until just now, began grinning foolishly.

*What’s gotten into her?*

I asked in a bemused voice.

“Why are you so excited? Is your heart already pounding at the thought of raiding the convenience store?”

“Who’s raiding anything? I’m going to buy canned tuna.”

“Canned tuna? Are we having tuna kimchi stew for lunch today?”

“No! We’re not!”

“…What’s with you today, seriously? Did you drink?”

“You’ll be like this, too, when you see this little one.”

Despite my reaction, Hayeon only continued to grin strangely, unlike her usual self. Then she lowered the zipper of her tracksuit and pulled something out from inside her clothes.

A tiny ball of white and yellow fur wriggled in her palm.

“Meeoow.”

“…Is that a kitten?”

“Cute, right? I went out to sort the recycling earlier, and someone had abandoned it in a box. It had been left there for anyone who wanted to raise it.”

“…”

“I don’t know what kind of bastard abandoned her, but she’s pitiful, isn’t she? What did it ever do to deserve that? Right, Oppa?”

“…Yeah. Animals haven’t done anything wrong.”

“I got Mom’s permission to foster it, even if it’s only for a little while. You’re okay with it, too, right?”

“Me?”

“Yeah. Our Mom melts for her eldest son, you know. She told me to get your permission, too, so put in a good word for me when we go inside later.”

“We’ll see.”

“What? You liked animals when you were little.”

I did. I still did, in fact. But this little thing sitting quietly in Hayeon’s palm was…

> **System**
>
> Lv. 2 Cat—Familiar

A little different.

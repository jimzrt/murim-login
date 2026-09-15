# Checkpoint Review — 210–214

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

# Chapters 210–214

## Plot

Jin Taekyung becomes nationally famous as the Tollgate Hero, but invasive media expose his family’s private information. Jinho reminds him that he does not need to save everyone and should focus on becoming strong enough to protect his family and precious people.

Taekyung meets Won Myunghoon, an A-Rank Hunter, former celebrity ranker, and CEO of the Star Guild. Taekyung’s admiration leads to a friendly hyung-and-younger-brother relationship, but he declines Won’s offers to join the Star Guild or an entertainment agency. At a live ceremony, Taekyung receives his A-Rank Hunter card and achieves the A-Rank Hunter Achievement. His accidental profanity becomes a viral iTube sensation, earning him the nicknames Taekyung the Lord and Lord Fuck.

Taekyung and Team Leader Choi perfectly clear the B-Rank Gate The Lycanthrope’s Black Forest. Won’s history is revealed: he survived the Myeongdong Station Mutated Gate Catastrophe, where Do Minsu and around thirty others died, then endured a trial before retiring from entertainment. After apologizing for the false transfer report, Won arranges a joint raid between the Peace and Star Guilds, guaranteeing the Peace Guild the Gate’s drops.

The combined party enters The Black Wyvern’s Nest, an A-Rank Gate. Taekyung recognizes it as the site of a traumatic encounter three years earlier, when a Black Wyvern slaughtered his teammates.

## Continuity

- Taekyung is publicly known as the Tollgate Hero and an A-Rank Hunter.
- Taekyung achieved the A-Rank Hunter Achievement, gained a level and 20 Bonus Points, and received a major Fame increase.
- Taekyung declined Won Myunghoon’s Star Guild and entertainment-agency offers.
- Taekyung and Won have a friendly hyung-and-younger-brother relationship.
- Won is a thirty-nine-year-old A-Rank Hunter, former ranker and entertainer, and CEO of the Star Guild.
- Won survived the Myeongdong Station Mutated Gate Catastrophe, where Do Minsu and around thirty others died.
- The Peace and Star Guilds are conducting a joint raid on an A-Rank Gate; the Peace Guild has rights to the drops.
- Im Kkeokjeong participates despite his nervousness as a D-Rank Hunter.
- The raid party is inside The Black Wyvern’s Nest, which Taekyung remembers as the site of his teammates’ deaths.
- The rewards for the Conception Vessel Opening Achievement and rare vessel-related Achievement remain unknown.
- The Gate Suppression Quest’s Reward and Failure conditions remain unknown.
- The Star-Array Grand Banquet, the Martial God’s condition, Jin Mukyung’s return, and Jeok Cheongang’s anticipated event remain unresolved.
- It is unresolved why the joint raid led to The Black Wyvern’s Nest and what will happen inside.

## Translation Decisions

- Retain “Tollgate Hero,” “A-Rank Hunter,” “Star Guild,” “hyung,” “iTube,” “Taekyung the Lord,” and “Lord Fuck.”
- Render 라이칸스로프의 검은 숲 as “The Lycanthrope’s Black Forest.”
- Render 은빛 갈기 라이칸스로프 as “Silver-Mane Lycanthrope.”
- Render 도민수 as “Do Minsu.”
- Render 명동역 변이 게이트 대참사 as “Myeongdong Station Mutated Gate Catastrophe.”
- Render 블랙 와이번의 둥지 as “The Black Wyvern’s Nest.”
- Render 기레기 as “hack reporter” and 찌라시 as “rumor sheets.”

## Durable state

{
  "active_continuity": [
    "One Step Back granted Taekyung two level-ups and 20 Bonus Points.",
    "Jeok Cheongang selected three Scorching Yang Qi elixirs for Taekyung's Fire Gate Clan training and successfully opened Taekyung's Conception and Governor Vessels.",
    "Taekyung is publicly recognized as Jeok Cheongang's Disciple and heir to the Fire Gate Clan's orthodox lineage.",
    "Jin Mukyung remains secluded in the training hall and has not returned to Heaven's Gate Temple.",
    "The Jin Family received an invitation to the Star-Array Grand Banquet in Henan.",
    "Seong Jinho is staying at Taekyung's new family home after losing his housing deposit to Kim Jong-su.",
    "Taekyung has achieved the A-Rank Hunter Achievement, leveled up, gained 20 Bonus Points, and received a major increase in Fame.",
    "The tollgate Gate released ten B-rank ogres; Taekyung defeated them, blocked the arriving military team from taking the remaining monsters, and collected their valuable parts; the incident exposed concealed Gate casualties.",
    "The Peace Guild House has extensive magical communication, observation, and alarm systems; its website has begun recruiting Guild members, and Team Leader Choi serves as its spokesperson.",
    "Taekyung's identity and Hunter status are public, and his tollgate rescue made him nationally famous after his KPS Nine O'Clock News appearance.",
    "The media frenzy exposed Taekyung's family's personal information, and online backlash against intrusive media reportedly shut down Hailey News and prompted a national petition seeking legal changes.",
    "Taekyung feels burdened and guilty about the hero label; Jinho tells him not to try to save everyone and to enjoy the recognition as a reward.",
    "Won Myunghoon is a thirty-nine-year-old A-rank Hunter, former ranker and celebrity entertainer, and current CEO of the Star Guild in Incheon.",
    "Won Myunghoon's eight-year absence followed the Myeongdong Station Mutated Gate Catastrophe, where Do Minsu and around thirty others died; Won survived, was tried and cleared, and later retired from entertainment.",
    "Taekyung and Won Myunghoon have adopted a friendly hyung-and-younger-brother relationship.",
    "Taekyung declined Won Myunghoon's Star Guild and entertainment-agency proposals, and Taekyung's accidental live profanity became a viral broadcast hit.",
    "Taekyung and Team Leader Choi perfectly cleared the B-Rank Gate The Lycanthrope's Black Forest after Taekyung defeated its Lv. 83 Silver-Mane Lycanthrope boss.",
    "A speculative report falsely claimed that Taekyung would transfer to the Star Guild; Won and the media outlet quickly issued corrective statements, settling the matter.",
    "Won arranged a joint Peace Guild–Star Guild raid on an A-Rank Gate for which the Star Guild has permission, guaranteeing the Peace Guild rights to the Gate's drops; the raid is scheduled for 2 p.m. with one selected Star Guild team and four A-Rank Hunters across both Guilds.",
    "The raid party arrived at The Black Wyvern's Nest, an A-Rank Gate Taekyung recognizes from a traumatic encounter three years earlier."
  ],
  "continuity_sources": [
    214,
    213
  ],
  "open_questions": [
    "What are the rewards for the Conception Vessel Opening Achievement and the rare Achievement earned after completing the Conception and Governor Vessels Quest?",
    "Will Jin Mukyung return to Heaven's Gate Temple before the appointed deadline?",
    "What event does Jeok Cheongang believe may occur sooner than expected, and why must he endure for several more years?",
    "What is the true condition of the absent Martial God?",
    "Will Taekyung attend the Star-Array Grand Banquet, and what exactly was the answer that changed the three men's expressions?",
    "What are the Reward and Failure conditions of the Gate Suppression Quest?",
    "How will the Gate near Hwang Cheol Soo's tollgate ultimately be contained, and what further monsters may emerge?",
    "Why did the joint raid lead the party to The Black Wyvern's Nest, and what will happen there?"
  ],
  "safe_through": 214,
  "temporary_decisions": [
    "Render 혈도 타통 as “Acupoint Opening,” 회음혈 as “Huiyin Acupoint,” and 임맥 타통 as “Conception Vessel Opening.”",
    "Render 성라대연 as “Star-Array Grand Banquet.”",
    "Render 노야 as “Old Master” when Taekyung addresses Jeok Cheongang privately.",
    "Render 고시원 as “goshiwon,” 오피스텔 as “officetel,” 오우거 as “ogre,” and 게이트 진압 as “Gate Suppression.”",
    "Render 기레기 as “hack reporter.”",
    "Render 원명훈 as “Won Myunghoon,” 스타 길드 as “Star Guild,” 주간 헌터즈 as “Weekly Hunters,” and retain “hyung” for Taekyung's address to Won.",
    "Render A급 헌터 as “A-Rank Hunter,” 아이튜브 as “iTube,” 태경좌 as “Taekyung the Lord,” and 시벌좌 as “Lord Fuck.”",
    "Render 라이칸스로프 as “Lycanthrope,” 은빛 갈기 라이칸스로프 as “Silver-Mane Lycanthrope,” 도민수 as “Do Minsu,” 소나무 위키 as “Sonamu Wiki,” and 블랙 와이번의 둥지 as “The Black Wyvern’s Nest.”"
  ],
  "version": 1
}

## Reading copies

## Chapter artifact 210

# Chapter 210

Sometimes, a spark casually flicked away can create a massive blaze.

After a day, two days, three… about a week, the tiny spark had spread into a forest fire—and I was standing at its center.

**[Korea Daily] The Rise of an F-Rank Hunter. “I trained exactly according to the manual.”**

**[Goryeo Daily] The Birth of a New Hero. “S-Rank Hunters, watch out!”**

**[Happy Thoughts] A Man in His Twenties Who Prevented a Major Disaster. “I only did what anyone should have done.”**

**[Current Hot Topic] Two Gates Open in a Single Day… An Unprecedented Crisis, and a Fierce Clash Between the Ruling and Opposition Parties Over National Defense and Security**

**[Parliament’s Words of the Day] Freedom Patriot Party Chairman’s Outrageous Remark Becomes a Hot Topic: “Jin Taekyung’s Arms are Thick, so He’s Obviously Conservative. Conservatives Saved the Country.”**

Daily newspapers, weekly magazines, current-affairs publications, lifestyle magazines, and more.

If all the newspapers and magazines piled high on the table had one thing in common, it was that my face and name were plastered across them.

Even looking at them was enough to make me feel overwhelmed by the sheer volume.

*Why are there so many?*

How many interviews had I done over the past week?

All kinds of media outlets, starving for an exclusive, had flooded the world with articles as though they had been waiting for this moment.

Reporters had staked out the Guild House and my home, while my personal information, past activities, and photographs circulated across the internet.

*Wow. These people are fucking insane.*

I had thought I was somewhat used to being famous after enjoying a fair amount of recognition in the Murim, but compared to this, that had been nothing.

Korea had been an internet powerhouse for a long time, and the respectable, gray-haired people in their fifties had actually been keyboard warriors in their younger days.

The saying that you could meet the entire nation just by browsing a few major online communities was not baseless nonsense.

“Why is everyone so interested in other people’s business?”

At my mutter, Hyung Jinho shrugged while eating bibimbap from a large metal bowl.

“It’s a good thing. You’re famous for doing something good.”

“I don’t know about that. There are all kinds of lunatics out there.”

“Ah, right. What happened with your family…”

Hyung Jinho quietly shut his mouth when he saw my expression. I had not looked in a mirror, but I was sure my face looked pretty frightening.

*They had nobody else to mess with, so they went after my family?*

The world really was a big place, and there were a lot of lunatics in it.

After I appeared on the KPS Nine O’Clock News, the public reaction exploded, and reporters hungry for a fresh scoop combed through everything connected to me with a fine-tooth comb.

The problem was that my family’s personal information had been exposed in the process.

“You know Hayeon called a few days ago, right? She ordered delivery because reporters kept following her whenever she went outside—and the delivery person turned out to be a reporter in disguise.”

“Ah, that guy really was a hack reporter. I’d only ever heard stories about people like that, but I never imagined they’d really go that far.”

“There were even people who hired Familiar mages.”

Sometimes I wondered if this was what hack reporters and paparazzi were supposed to be.

When I first heard about it, I saw red. But before I could personally go after the reporter and the media outlet, netizens rose up like wildfire.

Several massive online communities, each claiming more than a million registered members, were still blazing away, using hack reporters as firewood.

**Top Comment:** LOL, these fucking hack reporters are crossing the line again. A few people are alive because of Taekyung, and they’re pulling this shit? I’m embarrassed for them.

└ They would’ve done the same thing if their own families had been there. They’re just fucking crazy.

└ What company is it? Post the article link.

└ Hailey News. Reporter B.H.Y. The original’s been deleted, but it’s already too late, LOL.

└ Let’s turn it into Hell News.

└ It already is. The site’s been shut down.

**Top Comment:** I heard there was another media outlet that hired a wiretapping mage and a Familiar mage. What happened to them?

└ The people involved are having a reunion in the holding cells. Their lives are probably over.

└ The person above doesn’t know Hell Joseon.[^1] The ones who gave the orders will get suspended sentences at worst, LOL.

└ Nope. A national petition went up about it, and it passed three million yesterday. The Blue House is supposedly preparing legislation. Looks like they’re going to overhaul the whole system this time.

└ We’ll have to wait for the results, but I really hope they do.

└ They’re probably going to clean house while they’re at it. Blinded by their hunger for an exclusive, they messed with someone they never should have touched.

└ I’m a man in my twenties. Everyone my age. Loves Jin Taekyung.

[^1]: “Hell Joseon” is an online term criticizing the harshness and unfairness of life in Korea.

The reactions of people like that left me more bewildered than anything else. I was happy, but at the same time, I felt burdened.

*I really only did what anyone should have done.*

It had been an accident that nobody could have predicted.

The news kept calling me a hero who had prevented a major disaster, but every now and then, I found myself wondering whether, if I had been just a little faster, there might have been even one fewer casualty.

“What’s with that expression?”

“Huh? Nothing.”

“Someone with nothing wrong isn’t supposed to pick at his food like that.”

“I’ve already eaten three bowls.”

“You normally eat at least five.”

“…That’s true.”

“Hey, Taekyung. I’m not really qualified to give you advice, but let me say one thing.”

It was the first time in a while that I had heard such a serious tone from him.

Hyung Jinho set down his spoon covered in red pepper paste and continued slowly.

“Don’t try to become a hero.”

“…”

“You’re not a god. How can you save everyone? Even gods can’t do that.”

He was right.

I wasn’t denying the existence or power of a god, but that didn’t mean I could reconcile myself to it, either.

The only things I knew for certain were the hundreds of millions of people who had died during the Great Cataclysm, my father’s death in an accident, and the poor, fiercely difficult life my family had endured.

“What was your dream again?”

“To make sure my family could live without envying anyone else. To protect the people precious to me.”

“Sum it up in one word.”

A quiet laugh slipped out of me.

Instead of the word *landlord*, which I had parroted day after day, an unexpected word came to mind.

*The greatest under heaven… no, the greatest of all time?*

I was briefly lost in my own thoughts, but when I saw Hyung Jinho looking puzzled, I hurriedly answered.

“Hmm. A strong Hunter landlord?”

“Exactly. That’s enough. You’ve practically achieved your dream already, so don’t drive yourself into the ground with pointless greed and guilt.”

“Pointless greed…”

“Let me ask you one thing. Taekyung, did you fight those monsters because you wanted this?”

“Absolutely not.”

“Then that’s enough.”

Hyung Jinho grinned and picked up his spoon again.

“Just enjoy it. Wouldn’t you feel more at ease if you thought of it as a reward for all the hardship you endured and the good you did?”

A reward.

I had already received plenty of rewards through the System, but the reward Hyung Jinho was talking about meant something completely different.

Not a material reward or power, but a reward for the mind.

In other words, he was telling me to find contentment and breathing room.

*Contentment and breathing room.*

The words felt unfamiliar as I repeated them silently.

When I had been an F-rank Hunter, I fought monsters for money. Now, I worked even harder to become stronger.

Thinking about it carefully, I realized what a greedy bastard I really was.

“Hyung.”

“Yeah? What is it?”

“Nothing. Just… thanks.”

Hyung Jinho, who had been scooping up a spoonful of bibimbap, froze.

“Really?”

“I mean it.”

“Then lend me one hundred thousand won.”

“Don’t start talking about money just because things got awkward.”

“I mean it, too.”

“…”

What the hell was this guy?

Just as I was staring at him in disbelief, the phone resting on the table began vibrating violently, and a text message arrived.

> **Team Leader Choi**
>
> **Team Leader Choi**
>
> I’ve arrived. Come down to the underground parking garage right away.

* * *

Just as the message said, Team Leader Choi was waiting for me in the underground parking garage.

The problem was that he was not alone.

“Oh my God News! Could you give us just one word about the current situation?”

“Mr. Jin Taekyung, I’m Reporter Hong from Housewives’ Daily. You were chosen as the number-one ideal man by married women in their forties this week, and…”

“This is *Vivid Current-Affairs Talk*! What do you think about the remark made in Parliament about the size of your arms?”

“Where are you headed right now? What did you have for lunch?”

More than twenty people were thrusting cameras and microphones at me. It was absolute chaos.

Unlike me, who let out a deep sigh, Team Leader Choi remained calm as he pushed back the enemy forces.

“Please step aside.”

“Just a moment. It’ll only take a second.”

“Mr. Jin Taekyung is a member of the Peace Guild. Please leave interview inquiries through the Guild’s official website.”

When had they even made an official website?

Not long ago, they had posted a massive recruitment notice for new Guild members as well. It seemed they intended to row this boat as hard as they could while they had the chance.

But despite Team Leader Choi’s efforts to stop them, the reporters clung to us stubbornly. Apparently, not getting a single interview over the past few days had eaten away at them.

“You’re the Team Leader of the Peace Guild, right? We weren’t asking you, so step aside!”

“Yeah! Move! Your website is a piece of garbage, too. How long are we supposed to wait before we can send an inquiry and get an interview?”

“It’s just one word. Why are you acting so precious?”

“Are you looking down on us because we’re a tiny second-rate media outlet?”

“Mr. Jin Taekyung is my team member, and I am currently the Guild’s spokesperson, so I have every right to intervene. The website is functioning normally, I have never played hard to get, and the reason I ignored you is that you failed to follow the proper procedure.”

Team Leader Choi answered without even blinking as he smoothly pushed the reporters and cameramen aside.

He looked slender, but an incredible amount of strength was hidden inside that body. He was using only one arm, yet the people blocking our path were pushed back in a line.

“Whoa!”

“Hey, he’s using force now?”

“A Hunter! The Hunter is beating people up!”

*Go on, make a whole fucking scene…*

I swallowed the words that had risen to my throat.

Just by looking at them, I could tell the reporters in front of us were low quality.

Team Leader Choi had arranged dozens of interviews over the past week as the Guild’s spokesperson. The fact that he was filtering these people out was enough to tell me they were shit, not soybean paste.

*Why are their questions such garbage in the first place?*

They were questions not worth answering. Even if I responded, they would obviously twist my words maliciously before publishing them.

“We’re passing through.”

That was when Team Leader Choi began forcing his way forward without paying them any attention.

“Whoops!”

Crack!

A camera that had slipped from someone’s hand struck the parking-garage floor and shattered.

The problem was that the entire sequence of events felt deliberately staged.

“My camera! Oh, no!”

His voice sounded heartbroken, but his eyes flashed with the look of someone who had finally caught his prey.

Team Leader Choi stared at the cameraman’s terrible acting. Then he bent down and reached for the broken device.

The cameraman angrily slapped his arm away.

“Don’t touch it! I recorded everything you did, so you’d better prepare yourself—”

Smack! Crack.

Everyone’s eyes dropped to the floor.

The wristwatch that had fallen from Team Leader Choi’s wrist was rolling across the parking-garage floor.

More than ten watch hands. Jewels set densely across its surface. And a face cracked like a spiderweb.

“…”

“…”

Gulp.

The cameraman’s swallow echoed through the parking garage.

Then Team Leader Choi’s quiet voice pierced everyone’s ears.

“The Universe-302, the final masterpiece personally crafted late in the life of Peter Philip, Switzerland’s greatest watchmaker. The pinnacle of automatic mechanical watches, this beautiful timepiece survived even the Great Cataclysm, only to be damaged so pointlessly.”

“…”

With sad eyes, Team Leader Choi picked up the watch—Universe, School Bus, or whatever it was—and delivered the final blow.

“I’m suing you.”

At Choi Moses’s miracle, the crowd parted in two.

* * *

Vroom.

A luxury sedan glided smoothly across the asphalt.

Team Leader Choi glanced at the rearview mirror and spoke.

“They aren’t following us anymore.”

“…I wouldn’t follow us, either. How much is that watch?”

“It’s worth more than you imagine. Of course, that’s assuming it’s genuine.”

“Oh, it’s an imitation? No wonder. I thought it was strange that you would throw away such a valuable luxury item so easily.”

“You noticed?”

“If a wristwatch came loose that easily, that would be even stranger.”

“I only scared them a little. I wore it in case something like this happened. It was a good choice.”

Wasn’t this basically Zhuge Liang?

I was admiring Team Leader Choi’s clever trick when something suddenly sprang out in front of the sedan, which was just leaving the entrance to the officetel neighborhood.

“Team Leader Choi!”

Screeeeeech!

Team Leader Choi hit the brakes half a beat ahead of my shout. He stared at the person visible through the windshield and muttered,

“He doesn’t look like a reporter.”

I thought so, too.

An ordinary person could not wear such a relaxed smile in a situation like this.

*And…*

Even without activating Qi Sense, I could feel the considerable energy coiled inside the man smiling at us.

*A Hunter. And a pretty high-level one at that.*

The uninvited guest, a man in his early thirties wearing a suit, tapped on the window and spoke.

“Let’s talk.”
## Chapter artifact 211

# Chapter 211

I stared silently at the man who had suddenly blocked the car.

*He’s definitely a Hunter, but…*

The reason I found myself thinking that despite sensing his extraordinary energy was his flashy appearance.

Starting with the semi-formal suit covered in complicated patterns, he was wrapped head to toe in all kinds of luxury brands.

On top of that, he had smooth, taut, blemish-free skin and teeth so white they seemed almost unnatural.

No matter how I looked at him, he seemed more like a celebrity than a Hunter.

Maybe that was why he seemed strangely familiar.

*He’s even more over the top than Team Leader Choi.*

They both liked luxury brands, but the man in front of us took it a little too far.

That included the enormous sunglasses he was wearing on such a gloomy day.

“Can’t you hear me? Is this thing under a noise spell or something?”

At the man’s mutter, Team Leader Choi lowered the window.

“What can I do for you?”

“Oh, you can hear me. Then why didn’t you answer?”

“We’re short on time. If you have nothing else to say, please step aside.”

“You must be pretty busy.”

“Yes. Very.”

The man studied Team Leader Choi’s calm response with a strange look before turning toward me.

“You’re Jin Taekyung, right? You’re even better-looking in person than on-screen. No wonder the female-dominated online communities went wild.”

“Whoa, really…? Wait, who are you?”

“As you’ve probably noticed, I’m not a reporter trying to get an interview. I run a Guild in Incheon.”

“Oh.”

I could more or less guess what he wanted without asking.

*Another recruitment offer, probably.*

I was used to it by now.

Ever since I started becoming famous, more than one or two Guilds had approached me.

I had proven my ability by taking down a group of ogres single-handedly, and since I had appeared in all kinds of media, I had plenty of buzz as well.

To them, I was a tempting “product” in more ways than one.

“Here. This is my business card.”

I had become a master at turning people down.

Taking the card, I put on the most natural smile I could manage.

“I’m sorry, but I’m not thinking about changing Guilds yet.”

“Really?”

“Yes. I’m quite satisfied with my current Guild. They were also the first to reach out to me.”

At my immediate answer, a faint smile passed over Team Leader Choi’s lips in the rearview mirror.

The man looked back and forth between Team Leader Choi and me, then rubbed his chin.

“That’s a shame.”

“I’ll contact you another time.”

“Still, there’s no harm in having a cup of coffee together, right? I’m a fan.”

“Pardon?”

“Thirty minutes. No, fifteen should be enough. I’m a busy man myself, so I can’t come around often.”

What the hell was this guy talking about?

Making a recruitment offer in front of Team Leader Choi was already incredibly rude, but now he was acting entirely on his own terms.

*He’s crossing the line.*

That was the look I was giving the man as I wondered how to deal with him when—

“Strange. Did I read the interview wrong?”

“...?”

“You said that in Weekly Hunters. You said your favorite Hunter was me.”

I blinked. Only then did I realize who the man was.

And why he had seemed familiar.

“C-could you be…?”

The man grinned at my reaction.

“That hurts. I went to the trouble of giving you my business card, and you didn’t even look at it properly.”

I hurriedly lowered my gaze to the card.

The metal business card gleamed gold, as though it had been plated, and clear letters were engraved across it.

> **Star Guild CEO Won Myunghoon**

“W-whoa!”

Seeing me splutter like Mute Samryong,[^1] the man—no, the A-rank Hunter Won Myunghoon—reached through the half-open window and offered me his hand.

[^1]: Mute Samryong is the title character of a well-known Korean short story.

“Nice to meet you, Taekyung.”

* * *

Won Myunghoon.

He was thirty-nine years old, and his birthday was April 1. He stood 185 centimeters tall, weighed eighty kilograms, and had a well-balanced physique.

While preparing for college entrance exams in physical education, he awakened as an A-rank Hunter on his twentieth birthday. With his exceptional ability and good looks, he earned a reputation as a man who had it all.

“Do you think that’s all? He has an amazing personality, too. He donates often, and there are countless heartwarming stories about him. He even runs a scholarship foundation…”

Team Leader Choi, who had been listening to my endless stream of information, asked with an incredulous expression,

“How do you know all that? Why have you memorized his physical stats and even his birthday?”

“I told you. He’s my favorite Hunter.”

It was something I said at least once in every interview.

The people I respected most were my parents. My favorite Hunter was Won Myunghoon.

“...Even so. At this point, isn’t it practically love?”

“What a horrifying thing to say. He’s more of a role model. The Won Myunghoon Syndrome. Haven’t you heard of it?”

“I haven’t.”

“Oh, dear…”

“What’s with that pitying look?”

*Because I feel sorry for you for not knowing how cool Won Myunghoon is.*

Things were very different now, but even when I was in school, Won Myunghoon’s influence had been tremendous.

Being an A-rank Hunter was impressive enough, but he also had enormous star power. Whenever you turned on the television, his face was there.

At the time, he was an all-around entertainer in every sense of the word.

“Movies, dramas, commercials. He could sing, too, so he even released albums.”

“You mean he was a singer as well? A Hunter?”

“Team Leader, you’d recognize them if you heard them. *Go*, *Coward*, *I Don’t Know Hunters*, *Escape*… He has tons of great songs. He even crushed Japan’s Unicorn chart.”

He was the role model of countless aspiring Hunters and one of the few male singers welcomed at military morale-boosting performances.

I hummed a few lines as a demonstration, and Team Leader Choi showed a flicker of recognition.

“Oh, I think I’ve heard *I Don’t Know Hunters* before.”

“Right? It’s still on the popular karaoke charts. Anyway, that’s how famous Myunghoon hyung is. There’s even a saying that any Korean man who doesn’t know Won Myunghoon is either a spy or a monster.”

“Is living abroad for a long time really enough to call me a monster?”

“Who called you a monster? You’re overreacting.”

“Hoo.”

Team Leader Choi shook his head, then suddenly looked puzzled.

“But even taking all that into account, the name Won Myunghoon feels strangely unfamiliar.”

“When did you return to Korea, Team Leader?”

“Three years ago.”

“Ah, then you might not know about that incident. It was pretty shocking, so everyone in the media has been keeping quiet about it.”

“An incident?”

“Yes. Though I suppose it’s already been eight years. What happened was…”

Just then, Won Myunghoon, who had briefly left to use the restroom, came walking back from a distance, waving his hand.

“Team Leader, Myunghoon hyung is calling me. I’ll get going.”

“...Go ahead. I have about thirty minutes to spare anyway, so I’ll look at some clothes in the department store nearby.”

“Yes, yes.”

I answered vaguely and ran toward Won Myunghoon.

He let out a quiet laugh at the sight of me. He looked so young that it was hard to believe he would turn forty in just a few months.

“What about Team Leader?”

“He went to take care of something. More importantly, hyung, you can speak casually with me.”

“Hyung? The age gap between us is too large for that.”

“Oh, come on. In this day and age, twelve years means we’re practically the same age.”

“Should I, then?”

“Yes.”

“Haha. It feels good to have a good younger brother like you, Taekyung.”

“...!”

I trembled with emotion.

Good heavens. I had become hyung and dongsaeng with Won Myunghoon himself.

If Jinho hyung, who had even once been the manager of Won Myunghoon’s fan café, found out about this, he would grab me by the trouser leg and refuse to let go. He would insist that the three of us swear a Peach Garden Oath together.

*Not a chance.*

A pleased smile came naturally to my face.

Drunk on happiness, I followed Won Myunghoon into a nearby café. A male part-time worker in his early twenties was looking at a book behind the counter. He looked up with a mechanical customer-service smile.

“Welcome. May I take your or—”

A brief silence followed.

Then a breathy gasp escaped from the employee’s mouth.

*Of course.*

He was a hardcore Won Myunghoon fanboy, too. I nudged Won Myunghoon in the side with my elbow and whispered,

“As expected of you, Myunghoon hyung. You’re still incredibly popular.”

“Haha, this is embarrassing. It’s been a while since I gave an autograph.”

Won Myunghoon laughed awkwardly.

I felt proud for no reason and puffed out my chest.

That was when—

“Jin Taekyung? You’re Jin Taekyung, right?”

“...Huh?”

“From the Outer Ring Road a little while ago! The B-rank Gate!”

“I-I am, yes.”

“Wow. That’s fucking awesome.”

The employee muttered his admiration, then hurriedly pulled out a piece of paper and a pen and held them out to me.

“Could you give me your autograph?”

What on earth was going on?

*Not Myunghoon hyung… me?*

I turned around in bewilderment, and Won Myunghoon’s face came into view.

His eyes were dry, and his expression was stiff.

I had never seen that unfamiliar look on his face anywhere before. The next moment, however, it vanished like a mirage beneath his warm voice.

“What are you waiting for? You should give him your autograph.”

“Pardon? Oh, yes.”

*The café lights must have been too bright. I must have seen wrong.*

With a strange sense of déjà vu, I took the pen.

“What should I write?”

The employee answered in an excited voice.

“Please write, ‘Hye-gyeong, wishing you and Jinwoo a beautiful life together.’”

“…”

Goddammit.

* * *

The initial awkwardness soon faded, and the moment I sat down, I spent more than twenty minutes enthusiastically showing off my fanboy devotion.

“As you know, hyung, there aren’t that many A-rank Hunters who use spears.”

“Hmm. That’s true. Quite a few people started with spears and switched to swords later.”

Although spears looked easy to use, they were actually very tricky weapons.

Having an advantage in range was useful, but you couldn’t always maintain that advantage.

Spears were highly effective in low- and mid-level Gates, but high-level Gates were filled with dangers you couldn’t anticipate.

There had even been a time when I considered using a one-handed sword with a shield.

“But you stuck with it. You even made your own manual.”

“That was a long time ago. It must have been… ten years by now.”

“Yes. Exactly ten years ago. I was in my first year of high school, and you were already a ranker.”

Just as there were differences in ability among Peak masters, there were differences among A-rank Hunters as well.

Among the roughly one hundred thousand Hunters in Korea, the term *ranker* referred to the one hundred most skilled.

“I used that manual a lot later, when I was at the training center.”

“Really? I’m not sure if it was actually helpful.”

“It was incredibly helpful, of course.”

“If that’s true, then I’m glad.”

Of course, the manual had only been useful up to low-level Gates.

That went without saying in the Murim, where martial arts had advanced to a level that could not even be compared with the modern world.

*But it was a huge help back then.*

The easiest way to explain it was that the manual had been written at the level of a novice.

You couldn’t teach an ant how a tiger moved.

After I finished praising him from every possible angle, Won Myunghoon tilted his lukewarm coffee cup.

“That’s all in the past.”

“You’re still in your prime and actively working, though.”

“No. It’s been a long time since I lost my ranker status, and people have mostly forgotten about me.”

“...Hmm.”

Was it because of that incident?

It was unfortunate, but I couldn’t deny it completely. Over the past eight years, countless star Hunters had emerged who could match or surpass Won Myunghoon, and the public had cheered for brighter lights.

“It wasn’t until last year that I finally thought about starting again. As it happened, I also took over a Guild from an acquaintance who was about to retire.”

“The Star Guild?”

I had discreetly searched it earlier.

The Star Guild was the new name Won Myunghoon had given it after taking it over. Before that, it had been a sizable, established Guild that ranked among the top three in Incheon.

“Yeah. A few lines about it appeared in the news, but that was the end of it. Did you know about it?”

“Last year… I’m sorry. I was a little busy back then.”

It wasn’t only then that I had been busy. For the past several years, I had repeated the same day over and over.

Raids, goshiwon, raids.

When the day ended, I went home to sleep and eat, then went back out to fight monsters.

Even if I had heard about it, I would have forgotten it soon enough. Won Myunghoon was already a good memory to me, not someone who belonged to the present.

“There’s no reason to apologize.”

Won Myunghoon smiled bitterly and continued.

“It’s not like I’m the only flash-in-the-pan star around. I suppose this was simply the extent of my limits.”

*A flash-in-the-pan star.*

It might have been true because his active career had been so short, but in another sense, it was wrong.

*A star?*

Even if he had appeared in a few movies, dramas, and commercials and released albums, Won Myunghoon’s true nature was that of a Hunter.

He had been lucky enough to awaken despite the incredibly low odds, and thanks to that, he had seized enormous wealth and fame.

Even though he had gone through an unfortunate incident…

*Maybe this is him returning to his original self.*

Despite the uneasiness I felt inside, I nodded.

It wasn’t that my thought was wrong. It was simply different. I had no desire to bring it up and make the atmosphere uncomfortable.

“I see.”

“Then I heard about you. You were incredible. It felt like I was looking at my old self.”

“M-me?”

“Yeah. I searched for and read your interviews. I was happy and grateful to hear that you were such an enthusiastic fan of mine. Thanks to you, I even received offers to appear on television from several places.”

“Oh.”

Had my interview actually helped Won Myunghoon?

I was scratching my chin with an awkward smile when—

A hand clamped around mine.

“Taekyung. Can I make you an offer?”

“...Hyung?”

Won Myunghoon gripped my hand tightly and spoke with a serious expression.

“Transfer to our Guild. I’ll take responsibility for you, Taekyung. I’ll turn you into a star Hunter.”
## Chapter artifact 212

# Chapter 212

“Transfer to our Guild. I’ll take responsibility for you, Taekyung. I’ll turn you into a star Hunter.”

I blinked.

“A star… Hunter?”

“Yeah. A star Hunter.”

Won Myunghoon continued in a confident tone.

“Times have changed. People are obsessed with Hunters and envy the abilities we have that they don’t. You know that too, don’t you, Taekyung?”

“That’s true.”

“When I was in elementary school, do you know what the kids around me wanted to be? The president. An astronaut. But these days? Children and adults alike all want to be Hunters.”

Wealth and fame.

Most people understand the Hunter profession through those two words.

Even now, decades after the Great Cataclysm ended, they don’t want to think about the fact that hundreds of Hunters still die in Gates every year.

“You have everything the public wants. Good looks, buzz, and a fresh character unlike anything they’ve seen before.”

Won Myunghoon’s face flushed with excitement. His heated voice continued.

“But how long will that last? The public heats up quickly, and they cool down even faster.”

“Hyung.”

“If you let this opportunity pass, you won’t even become a flash-in-the-pan star, Taekyung. Fortunately, it isn’t too late yet. If you start getting professional management now, appear on television, and work on your image…”

“Wait, wait. Hyung.”

“Huh? Oh. Right.”

Won Myunghoon closed his mouth for a moment, and I scratched my chin.

I hadn’t expected the conversation to go in this direction, but it would be better to make things clear while I had the chance.

“You said you weren’t going to make me a recruitment offer. You told Team Leader Choi that, too.”

“I did. But Taekyung, this is a really good opportunity.”

“Uh, I’m sorry, but I have no intention of changing Guilds.”

Won Myunghoon opened and closed his mouth as if he was about to say something, then nodded.

“Right. That’s understandable at your age. Then let’s forget about changing Guilds. How about an entertainment agency, instead? It’s pretty common these days.”

“An entertainment agency?”

“Yeah. I happen to own a major stake in one.”

Dual contracts with Guilds were illegal, but other social activities weren’t a problem.

As he said, it was no longer unusual for high-ranking Hunters to sign with entertainment agencies or management companies.

But I answered without hesitation.

“No, I don’t need an agency either.”

“What?”

“I’m satisfied with what I have now.”

“…You’re satisfied?”

“Yes.”

Won Myunghoon frowned.

“Taekyung. You don’t seem to understand what I’m saying.”

“You said that if I let this opportunity pass, I wouldn’t become a star? That’s fine. I didn’t do any of this hoping for that.”

“I know. I know, but think it over one more time. Just a regular television program and a few major commercials could bring in tens—or even hundreds—of billions of won. Can’t you tell by looking at me?”

Won Myunghoon spread both arms wide. From head to toe, he was dressed in luxury brands whose names and prices I couldn’t even begin to guess.

I suddenly remembered an Internet article I had seen in the past.

> **A-Rank Hunter Won Myunghoon Purchases Building Worth Tens of Billions in Cheongdam-dong**

The subject of the article I had admired and envied endlessly was standing right in front of me.

“I saw your interview. You’ve been pretty busy. Isn’t it time you enjoyed life a little? I heard your dream was to own a building.”

“That’s true.”

It had changed a little, but it was still one of the goals I wanted to achieve.

Won Myunghoon flashed a grin at me as I nodded readily.

“Then joining an entertainment agency would be faster than Guild work. You won’t have to fight monsters in dangerous Gates, either. You’ll just have to work for a few hours in a cool studio. Ah, full makeup might feel a little stifling. Ha-ha.”

“Oh, really?”

“Of course. You just need to get used to smiling brightly and delivering your lines in front of a camera.”

“Then Gates would probably be better. I’m the type who likes using my body, so I don’t like feeling stifled.”

“…What?”

“I also swear a lot in everyday life. It wouldn’t pass broadcast standards. Even if I attracted attention for no reason, my family would just suffer like they are now.”

“T-Taekyung.”

I continued speaking as I watched his obvious bewilderment.

“And as for owning a building, I can become a building owner without doing television or commercials. It’ll take some time, but still.”

“What are you talking about? It’s true that A-rank Hunters make a lot of money, but do you have any idea how expensive land in Gangnam is?”

“Gangnam?”

“Yeah. Do you even know what the current price per pyeong is there—?”

I blinked blankly, then let out a quiet laugh.

“Why Gangnam? I can just buy one near my house.”

“Huh?”

“A three-story neighborhood shopping building would still make me a building owner. I haven’t even thought about Gangnam.”

“…A neighborhood shopping building?”

“Yes. It’d be close, so it would be easy to visit, and the rent would come in like clockwork. If Mom says she’s bored after quitting her job, I could set her up with a little snack bar or something.”

“A snack bar?”

The more I spoke, the more Won Myunghoon’s face twisted. Had I said something wrong?

“Hyung?”

“…”

“Myunghoon hyung. Are you all right?”

Won Myunghoon’s lips moved soundlessly before he let out a trembling breath.

“Taekyung.”

“Yes, hyung.”

“Can you—can you really be satisfied with that?”

“You saw my interview. Until a few months ago, I was an F-rank Hunter. I’m making dozens of times more now without having to work myself to death like I did back then. What’s the problem?”

I had no debts, and I had gotten my house back.

As for people’s attention and fame, I felt that I had already had more than enough of both in the Murim and the modern world.

I had especially learned how exhausting and unpleasant the spotlight could be in real life.

I also knew what kind of life would make me and my family happier.

“So this is enough for me. Team Leader Choi already showed me a whole pile of commercial offers, but there were too many, so I’m planning to choose a few, film them, and focus on the Guild again.”

I could earn plenty of money without getting involved in the entertainment industry.

Even after I finished speaking, Won Myunghoon remained silent for a long time. Finally, he parted his lips.

“I see. I understand.”

“You’re not offended because I turned you down, are you?”

“…Of course not.”

Just then, the phone resting on the table vibrated. There was no need to check the caller. It was Team Leader Choi.

When I checked the time, we had already gone well past the thirty minutes we’d agreed on.

“Hyung, I think I should get going.”

“Already? You must be busy.”

“The Association contacted me and asked me to get my rank reassessed today. I got your number today, so I’ll contact you again soon.”

“Then I’ll see you next time. It was nice meeting you.”

“Next time, let’s go to a coin karaoke room together. I’ll practice your song before then.”

“A coin karaoke room? Sounds good.”

Just thinking about hearing the original live version of *Coward*, my signature song, already made my heart race. Should I ask Jinho hyung to come along, too?

“Then I’ll be going. Don’t forget your promise.”

I left the café with Won Myunghoon nodding behind me, a faint smile on his face.

The black sedan parked by the roadside honked.

* * *

“Sir. Shall I clear your cup?”

Won Myunghoon did not answer the part-time worker’s question. He stared silently down at the empty coffee cup before suddenly opening his mouth.

“Do you perhaps not know who I am?”

“Pardon?”

“Won Myunghoon. Haven’t you heard of me?”

“I know who you are. You released a few famous songs, didn’t you?”

The part-time worker gave an awkward smile and continued.

“Actually, I just looked you up. You’re much more famous than I expected. I only saw you a few times on television when I was young, so I didn’t remember you very well…”

“You looked me up.”

The smile lingering around the part-time worker’s mouth slowly faded at the dry, sandy tone of his voice.

After the worker nervously returned to the counter, Won Myunghoon sat there for some time. Eventually, a familiar melody rang through the café, and the corner of his mouth twisted.

It was his own song, released ten years ago.

Everything he had made had become a relic of the past.

“That bastard thinks he can make fun of me…”

His quiet voice was drowned out by the music, and Won Myunghoon rose from his seat.

His mind was filled with one person.

Jin Taekyung, a dayfly Hunter who had been eking out a living in F-rank Gates only a few months ago.

But now he was someone who received the public’s attention and affection.

“A coin karaoke room, for fuck’s sake… Some lucky bastard gets one flash of fame and doesn’t even know his place.”

Muttering under his breath, Won Myunghoon put on his sunglasses.

People passing by turned to stare at his expensive, flashy clothes, but no one recognized him.

* * *

“Congratulations, Mr. Jin Taekyung.”

The Bucheon Hunter Association president, a middle-aged man with hair more than half gray, handed me a card with a genial smile.

The card, about half the size of my palm, gleamed entirely silver.

Platinum. In other words, the card was made of platinum—a possession everyone dreamed of owning.

*It means I’ve gained that much wealth and fame.*

But perhaps because I had expected this to happen, I remained calm even as I accepted the card the Association president held out to me amid the barrage of flashes from countless cameras.

*I’m a Peak master. An A-rank Hunter is no big deal.*

Still, I felt pretty good.

I grinned and waved at the cameras, and the Association president asked in a robotic tone,

“So, Mr. Jin Taekyung. How do you feel right now?”

*Obviously, I feel fantastic.*

I was just about to answer when—

Ding.

> **System**
> - You have earned the **A-Rank Hunter** achievement.
> - Achievement Reward granted.
> - Level Up!
> - You have gained 20 Bonus Points!
> - Fame increases greatly!

“Oh, fuck.”

“…!”

“…!”

“…Ah.”

*Right. There are cameras here.*

I looked at the Association president, who had frozen with a stunned expression, and at the broadcasting staff, who seemed to doubt their own ears. Then I saw Team Leader Choi lowering his head with the hollow look of a man experiencing post-nut clarity.

*I’m fucked.*

This was probably the greatest broadcast disaster in history.

Feeling my throat grow painfully dry, I whispered to the Association president,

“They’ll edit that out, right? You have to make sure they do.”

“Edit it out? Mr. Jin Taekyung, are you out of your mind?”

The Association president muttered in a heavy, sunken voice. He looked like he wanted to grab me by the collar right then and there.

“Edit my ass. This is live. What’s it called? An iTube live stream.”

“What?”

“Can’t you see the monitors in front of us? More than fifty thousand people are watching right now.”

“…”

*For fuck’s sake. He’s right.*

There had been so many people and machines around that I hadn’t noticed. But now I could see that five or six monitors set up below the podium were displaying the Association president and me.

The chat window beside the video was about to explode from the sheer volume of messages.

“What do we do?”

“What do you mean, what do we do? Apologize immediately!”

The Association president snapped at me with a face flushed bright red. That was when the camera director at the very front mouthed something.

—The reaction is good?

“Huh?”

“What?”

*What is that supposed to mean?*

I looked at the chaotic chat window. Dozens—no, hundreds—of messages had scrolled past in only a few seconds, but my extraordinary dynamic vision caught every little detail.

ㅋㅋㅋㅋㅋ

ㅋㅋㅋTaekyung the Lord, are you insane?ㅋㅋㅋㅋ

No, not Taekyung the Lord. He’s Lord Fuckㅋㅋㅋㅋㅋ

That was the greatest acceptance speech everㅋㅋㅋㅋㅋ Usually, they start with religion or family and end with something like, “Minsik, Changsu, Hyerim, thank you,” right?ㅋㅋㅋㅋㅋ

Lord Fuck doesn’t do any of that. I knew what he was like from the moment he beat down an ogre on his way to work, dragging his slippersㅋㅋ

??? : Oh, fuck.

Look at the Association president’s faceㅋㅋㅋㅋㅋㅋ The old man’s soul left his body.

Taekyung, nobody cares, so just do whatever you wantㅋㅋㅋㅋ I’d probably laugh it off even if you insulted my parents.

└ May your parents live long and healthy lives.

? What the fuck is this guy?

It was a complete mess, but I learned one thing.

The broadcast disaster I had caused by accident had become a huge hit.
## Chapter artifact 213

# Chapter 213

“Netizens have some serious firepower. Everyone’s going crazy over the press conference.”

Team Leader Choi’s relaxed voice came from behind me.

Ssshhhwing!

At the same time, a sharp beast’s claw slashed through the air like a blade. I simply leaned my head back to dodge it and muttered,

“Tell me about it. I thought I’d caused a broadcast disaster, but things worked out like this.”

“On top of that, everyone’s praising you for going straight to a Gate as soon as the press conference ended.”

“Isn’t it normal for a Hunter to go on a raid?”

“That’s why image is so important. You know the saying, don’t you? Take a shit, and you’ll become famous.”

“……I don’t think that’s quite it.”

Shhhk! Crack!

I knocked away and crushed every claw that came flying toward my head, shoulders, and chest.

The creature staggered backward with a painful howl. Just as I was about to approach it, Team Leader Choi asked,

“Would you like to take one next time?”

“Take what?”

“A shit.”

“I’ll pass.”

I answered firmly and swung my spear shaft.

Wham!

With the sound of something being crushed, the creature that had rushed in from the side slammed straight into the ground.

It was two meters tall—a massive, gray-furred, bipedal wolf with nothing left above its shoulders. I had blown its head off through sheer strength alone.

A System notification rang out at the same time.

Ding.

> **System**
> - You have defeated **Lv. 73 Lycanthrope**!
> - You have gained EXP!

The lycanthropes that had watched their fellow die let out howls.

- Grrrrr.

- Awooooo.

Their long, vertically slit yellow pupils trembled.

Seeing them hesitate, Team Leader Choi remarked as if he had just realized something,

“This is the first time I’ve seen lycanthropes look so docile.”

“They’re good at controlling their anger. Maybe being half-human means they picked up things like this, too.”

Whenever I saw hotheads who claimed to have anger-management issues, the pattern was always the same.

They acted like Lü Bu without hesitation in front of the weak, but the moment they faced a muscular older brother, they became the most polite people in the world.

*And once they lose the momentum, it’s over.*

Slash!

I flicked the sticky blood off my spearhead and beckoned to the creatures with one finger.

“Come on, you sons of bitches.”

- Whiiine.

Their ears had folded halfway back, and their tails had curled between their legs.

The moment a wolf became a dog, the fight was as good as over.

“You little bastards are cute.”

As I walked toward them with a grin, Team Leader Choi said,

“If possible, please handle them cleanly.”

“Why?”

“So we can take some proof shots. We’re going to upload them to the Peace Guild’s official social-media account.”

“……”

“Too much pixelation would be a shame. People like it uncensored.”

Ah. He had a point.

* * *

- Awooooooooo!

As expected, the boss was different from the rest.

Its roar was packed with ferocity and killing intent. Its body was much larger than the other lycanthropes’, and silver fur covered it from head to toe.

It had the kind of presence that showed with every inch of its body that it was a boss monster.

“Wow. You’re impressive.”

As I admired it, I made a decision.

I would give this one special treatment.

“One Annihilation.”

Krrrunch. Thud.

The monster’s huge body, a gaping hole torn through its chest, collapsed like a rotting tree.

Ding.

> **System**
> - You have defeated **Lv. 83 Silver-Mane Lycanthrope**!
> - You have perfectly cleared the **B-Rank Gate, The Lycanthrope’s Black Forest**!
> - You have gained a substantial amount of EXP!
> - The exit has opened because you defeated the boss monster.

Kiiiiing.

Once the conditions were met, a Gate exit appeared in the center of the clearing. But I still had something left to do.

“All right. Time for the fun part—cleanup.”

Looking at the corpses scattered everywhere filled me with a deep sense of happiness.

I was approaching the bodies with the heart of a farmer harvesting grain when Team Leader Choi spoke.

“About Won Myunghoon.”

“Yes?”

I turned at the sudden sound of his voice behind me.

He was sitting on a flat rock with his entire body covered in a shield spell, staring at a specially made phone.

But his expression looked strange.

“Myunghoon hyung?”

“Yes. What happened to Mr. Won Myunghoon eight years ago?”

I had no idea why he was suddenly curious about that.

I had been a student back then, and I was such a huge fan that I knew everything by heart. But explaining it all would make my mouth hurt.

“Look it up. Everything comes up if you search Sonamu Wiki.[^1]”

“People say you should stay off Sonamu Wiki.”

[^1]: *Sonamu* means “pine tree” in Korean.

“……They have a point.”

“Just give me a simple explanation. Of all the people around me, I believe Jin Taekyung knows the most about Mr. Won Myunghoon.”

“Well, if you put it that way…”

I started talking as I skinned the lycanthrope with a dagger.

“Eight years ago, Myunghoon hyung was on a downward slide. He bombed every movie, drama, and album, and then allegations of tax evasion were piled on top of that.”

“That isn’t particularly unusual.”

“No. There are so many incidents in that industry.”

“I skimmed through the articles. It seems the tax-evasion charges were dropped.”

“Yes. It ended without any significant problems.”

But that wasn’t the end of it.

Once mud had been splashed onto his clean image, all kinds of speculative articles and rumor sheets about Won Myunghoon began circulating online.

In the end, Won Myunghoon, who had already passed his prime and was going through a difficult period, decided to take some time away from the public eye.

“He said he’d spent too much time looking elsewhere and would devote himself to his duties as a Hunter for a while.”

“And then that incident happened?”

“Oh, you read that article?”

“I just did.”

Team Leader Choi held out his phone. The screen, about the size of an adult’s palm, displayed a headline from eight years ago in bold type.

> **Myeongdong Station Mutated Gate Catastrophe, Around 30 Dead Including A-Rank Hunter Do Minsu… Surviving Won Myunghoon: “Minsu, I’m Sorry.”**

It had been a massive incident, sensational enough to make the front pages of every newspaper at the time.

“Who is Do Minsu?”

“An A-rank star Hunter who was extremely close to Myunghoon hyung. He was rapidly gaining popularity, but he died while on a joint raid with Myunghoon hyung for a get-together.”

No one had expected anything like that to happen when they set off for a B-rank Gate in such a lighthearted mood, as if they were going on a picnic.

And it had been a catastrophe that occurred despite two A-rank Hunters taking part.

The domestic media boiled over like a cauldron on charcoal, then quickly went cold.

“It took several years for him to stand trial over that incident and be cleared of the charges.”

After a long legal battle, all that remained was an image covered in filth and the indifference of the public.

He appeared on television a few times after that, but that was all. Unable to make a comeback, he quietly retired from the entertainment industry.

*Though I don’t think he’s given up yet.*

If he had abandoned all his lingering attachments, he wouldn’t have offered to recruit me and turn me into a star Hunter.

In any case, after listening to everything I had to say, Team Leader Choi gave a small nod.

“I see.”

“But why are you suddenly asking about that?”

“Won Myunghoon’s name is number one in the real-time search rankings. There are already dozens of related articles.”

“Oh, really?”

“And Jin Taekyung is tied for first place with him.”

“What?”

What was going on? Had there been a tie for first place in the real-time search rankings?

As I tilted my head, Team Leader Choi held out his phone again.

A fresh article, posted ten minutes earlier, was displayed on the screen.

> **Jin Taekyung & Won Myunghoon. Successful Fanboy Transferring to Star Guild?**
>
> **A New Star Hunter Is About to Be Born.**

A brief silence passed.

After I pulled my eyes away from the phone screen, Team Leader Choi asked,

“Are you transferring?”

No, what the hell was he talking about?

* * *

*Hyung, I’ll see you again soon.*

I hadn’t expected those words, spoken only a few hours ago when I parted ways with Won Myunghoon, to come true so quickly.

Of course, the place where we met again wasn’t a coin karaoke room but the Peace Guild House.

“I’m sorry.”

Won Myunghoon had read the article while handling some business and rushed over immediately. He bowed politely to every Guild member, including me, then explained in a flustered voice,

“I was surprised, too. Someone must have seen us meeting and spread a speculative article, but I’ve already lodged a complaint with the media outlet and arranged for an immediate statement to be released.”

Team Leader Choi, who had been staring at Won Myunghoon, spoke.

“I saw the article saying it was baseless a few minutes ago. You work quickly.”

“False information needs to be corrected as soon as possible.”

“False information?”

Team Leader Choi’s long fingers tapped against the phone screen.

“But it isn’t exactly baseless, is it? I heard from Jin Taekyung that you offered to recruit him. And you did it in a café with other people around.”

“That…”

“Team Leader Choi, let me explain it again.”

I stepped in for the hesitant Won Myunghoon.

Considering the situation, I had no choice but to reveal the conversation we’d had at the café, and I was already feeling a little guilty about it.

“What happened exactly was…”

But before I could continue, Won Myunghoon’s firm voice cut me off.

“It’s true. I offered to recruit him, and Taekyung turned me down. It all happened because of my own selfishness, so I sincerely apologize.”

“Hmm.”

Who was Won Myunghoon, anyway?

His career as a Hunter aside, he had once been a celebrity who enjoyed immense popularity at the very top.

When someone like that admitted his mistake cleanly, bowed politely, and took responsibility, there wasn’t much anyone could say.

*It wasn’t as though he had violated professional courtesy in any serious way.*

Hunters were professionals, plain and simple. As long as they stayed within the boundaries allowed by the regulations, they could transfer to or leave a Guild whenever they wanted.

The dozens of recruitment offers I had received before Won Myunghoon’s had been the same.

The only difference was that I had arranged a separate meeting with him because I was a fan.

*And the later articles about me transferring had already been proven baseless.*

Thanks to the swift action taken by both sides, the situation was already dying down.

Team Leader Choi, who had been deep in thought, finally spoke.

“All right. Let’s put this matter to rest here.”

Won Myunghoon’s face brightened.

“I’m relieved you see it that way. Thank you.”

“Not at all. I have no intention of turning a minor incident into something bigger than it is. Besides, our side shares some of the blame.”

Im Kkeokjeong, who had been watching the situation carefully, cut in with a good-natured grin.

“Yeah, yeah. You two look good together. That’s how people live—understanding each other.”

Butler Kim and Song Song nodded as if they agreed.

The atmosphere inside the Guild House, which had been strangely uncomfortable only ten minutes earlier, had turned warm and friendly.

*It’s a relief that things worked out better than expected.*

Won Myunghoon was soon being served coffee as well. With a genial smile, he brought up one topic after another.

“Taekyung is incredibly devoted to the Peace Guild. I wanted him so badly that I tried to entice him, but he didn’t budge.”

“Haha! This guy’s always been unbeatable when it comes to loyalty.”

“You’re all such wonderful people that I suppose he didn’t want to leave. After meeting you in person today, I understand why Taekyung turned me down so decisively.”

“Wow. Mr. Won, you really know how to say things people like hearing. When I watched you on television, I thought it was all scripted.”

“I got called an obnoxious bastard because of that.”

In the middle of the friendly conversation, Won Myunghoon naturally made another proposal.

“What are your schedules like tomorrow? I was wondering if we could go on a raid together.”

“Tomorrow?”

“A raid?”

Everyone reacted differently, but their eyes all turned toward one person.

Team Leader Choi.

On the surface, Butler Kim was the Guild Master. But Won Myunghoon had realized that Team Leader Choi was the real power behind the Guild, too.

“What do you think, Team Leader? This would be a good opportunity to clear up the suspicions raised by the rumor sheets, and it could also be a valuable experience for the Guild members.”

“I’m not sure.”

Maybe it was because I’d gotten used to Team Leader Choi by now.

There was something subtly uneasy about his expression.

But his hesitation vanished at Won Myunghoon’s next words.

“It’s an A-rank Gate. Fortunately, our Guild obtained permission to raid it this week. It seems like a shame to let the opportunity go to waste.”

“An A-rank Gate?”

“Yes. We’ll also guarantee you the rights to whatever comes out of the Gate.”

Gate qualification reviews were strict.

As a Guild that had only just begun recruiting members, the Peace Guild would need a considerable amount of time before it could enter an A-rank Gate.

“An A-rank Gate…”

Team Leader Choi murmured under his breath, then finally nodded.
## Chapter artifact 214

# Chapter 214

Once the details of the joint raid had been finalized, Won Myunghoon rose from his seat.

“Then I’ll be going.”

“Hyung, you’re leaving already?”

“It would’ve been nice to have a drink together.”

At Jin Taekyung and Im Kkeokjeong’s regretful tones, Won Myunghoon gave them a genial smile.

“I still have work to do. I’m technically the Guild Master—I can’t cause a mess and then be the only one having fun.”

“Ah, right.”

After he put it that way, no one could stop him.

Telling the others not to see him out too far, Won Myunghoon left the Peace Guild House. He walked along leisurely as he pulled out his phone.

After a few rings, someone answered.

“Yes, CEO.”

“I finished the arrangements. We’re doing the joint raid tomorrow at two in the afternoon.”

“That was quick.”

“The bait is good. When would people like them ever get the chance to enter an A-Rank Gate?”

“Haha. That’s true.”

“We’re only bringing one team from our Guild. You’ve told the guys to keep their mouths shut, right?”

“Do you not trust me? I handpicked only the ones who know how to follow orders.”

“That’s why you’re Team Leader 1. I’ll be back right away, so choose the list of people participating tomorrow and have it ready.”

“Yes, sir. What about the Peace Guild?”

“Here?”

Won Myunghoon gave a short laugh and continued.

“I came just in case, but it’s a complete mess—a hodgepodge. They’re a bunch of nobodies without even a proper hierarchy. What could a Guild with only five members possibly accomplish?”

“Even excluding Jin Taekyung, they have three B-Rank Hunters.”

“Still, that’s all they have. The old man sitting there as Guild Master looks like a figurehead. The Team Leader and the woman are former Ares Guild members, but they aren’t worth worrying about. The other one is even D-Rank.”

“D-Rank? Tomorrow’s work should be easy, then.”

“Easy?”

The amusement in Won Myunghoon’s voice vanished, leaving it cold.

The sudden change in atmosphere seemed to make the person on the other end flinch. He hurriedly added,

“CEO, that’s not what I meant.”

“Team Leader 1—no, Jonghun.”

“…Yes.”

“Let’s stay sharp. Why do you think I’m personally running Gates at my age? Am I wrong?”

“I’m sorry.”

“All right. If you understand, do better from now on. Watch what you say.”

“Understood, CEO.”

“All right. See you later.”

After ending the call, Won Myunghoon took out his lip gloss and applied it to his lips.

He was at an age when he would be entering his forties in only a few months.

He spent hundreds of millions of won every year maintaining his appearance, but there was no deceiving time.

“I’m going to be back in the media for the first time in a while. Maybe I should stop by the salon today.”

Muttering in a voice too quiet for anyone to hear, he climbed into the sports car parked by the roadside.

The thought of facing those disgusting monsters again after so long put him in a foul mood. But when he imagined the smooth road that would open up before him afterward, he began humming to himself.

* * *

The next morning, Jinho hyung sat across from me at the table, unable to take his eyes off his phone screen.

“You haven’t even eaten. What are you looking at so intently?”

“Your articles.”

“Again?”

“What do you mean, again? I never get tired of looking at stuff like this.”

Anyone watching him would have thought the articles were about Jinho hyung, not me.

These days, checking the public reaction and reporting it to me had become part of his daily routine. He was practically my manager.

“People like you. There are tons of articles about Won Myunghoon, too.”

“Of course there are.”

“You two look good together. So heartwarming… I wish Lord Fuck would swear at me, and so on.”

“……”

“There’s even a guy asking to be tied up and beaten.”

The world really was a big place, full of crazy people.

I was so dumbfounded that I searched for myself directly. Articles about me were overflowing across the Internet, along with all kinds of nicknames and edited images on countless online communities.

There was even a post summarizing my exploits sitting prominently on the best-posts board.

**A Summary of Lord Fuck’s Exploits So Far.txt**

> Hi. I’m an unemployed guy in my thirties.
>
> I was thinking hard about what useless thing to do today when I became curious about Lord Fuck. Most people who know anything about him probably already know all this, but I figured there might be some people who don’t, so I wrote it up.
>
> I couldn’t be bothered to move my fingers much, so here’s the short version.
>
> 1. Awakened as F-Rank at twenty. Spent seven years getting run even harder than a brand-new private, then reawakened.
>
> 2. But the Hunter Association played its trap card, so he was measured as C-Rank at the time. The accepted scholarly consensus is that the Hunter Association is full of idiots.
>
> 3. The bewildered Lord Fuck was snared by an unknown Guild called the Peace Guild.
>
> 4. A B-Rank Gate erupted while he was going to work in a tracksuit, dragging along slippers. He chewed through the ogres by himself and saved hundreds of people.
>
> 5. His life turned around. On the day he received his A-Rank Hunter ID, he made *that remark* in front of fifty thousand people. Acquired the title “Lord Fuck.”
>
> That’s about it. I didn’t write anything about his family because I might get sued.
>
> A few media outlets have already been taken down. An unemployed thirtysomething like me would be nothing by comparison. If a complaint lands, I’ll get a Mom’s Touch across the back, so cut me some slack.[^1]
>
> I ate doenjang jjigae for breakfast, scratched my balls, and scribbled this together.

[^1]: “Mom’s Touch” is a Korean fast-food chain; here it is being used as a pun for getting smacked across the back by one’s mother.

My first thought after reading it was simple.

*It’s way too short.*

If I listed everything I had experienced while traveling between the modern world and the Murim, even a hundred pages wouldn’t be enough.

*Well, they’re ordinary people who don’t know anything, so I suppose this is a natural reaction.*

I scrolled down through the densely packed comments.

Of course, I couldn’t read all several hundred of them, so I looked at only a few of the best comments.

> **(Best comment) Fuck. I love him.**
>
> └ I saw Lord Fuck live, and he really swore more colorfully than my grandma. Did he attend some kind of swearing academy?
>
> └ But it feels natural. You can’t hate him.
>
> └ There have been some pretty innocent and nice people who appeared on TV as A-Rank Hunters, but none of them were this down-to-earth. Lol.
>
> └ Yeah, that’s why people like him. Looking at the stories he told in the interview about when he was an F-Rank Hunter, he seems to have suffered like crazy. Maybe that’s why.
>
> └ Personally, I liked that he went on a raid right after leaving the Association. It felt like he was focused on a Hunter’s real duty instead of money.
>
> └ Agreed.

> **(Best comment) So what happened to him transferring to the Star Guild? I’d rather he just transferred.**
>
> └ Completely untrue. He kept sucking up to Won Myunghoon in every interview, so he went to see him once, and the story got distorted.
>
> └ Suck… up?
>
> └ That’s today’s joke.
>
> └ This Lord Fuck does it for free.
>
> └ There are so many crazy bastards.

> **(Best comment) Lord Fuck already has a permanent get-out-of-criticism pass, and Won Myunghoon is suddenly getting hard-carried by the collar.**
>
> └ Seriously. I’d even forgotten Won Myunghoon’s name. I vaguely remember seeing an article a few years ago saying he was cleared in that case.
>
> └ Wasn’t he popular? Why did he get buried?
>
> └ He was. He was at his peak while he was active, but the problem was that it was too short. By today’s standards, his persona was too predictable, and his acting wasn’t anything special… He only got famous because one of his songs became a hit, and he had tons of fans who were only into his face. There are still plenty of people sucking up to Won Myunghoon. Jin Taekyung’s the same.
>
> └ Suck… up?
>
> └ This guy is that guy from the comment above. Anyway, apparently the Peace Guild and Star Guild are doing a joint raid today. I’m looking forward to it.

The netizens’ overall reaction was favorable.

Apparently, appearing on the news once or twice and doing a few magazine interviews had made an extremely good impression.

*The public reaction to Myunghoon hyung isn’t too bad, either.*

Was it nostalgia?

Although he had gradually been forgotten because of an unpleasant incident, there were still plenty of people who remembered Won Myunghoon.

Jinho hyung sitting across from me was one of them.

“Don’t forget to get Won Myunghoon’s autograph, okay?”

“Got it. I’m going to get a callus in my ear.”

I gave a halfhearted answer to Jinho hyung, who was fluttering like a teenage girl, then stood up.

Since we’d eaten breakfast late, it was already past ten in the morning. We had to leave soon if we wanted to finish the final checks before the raid.

“Damn it. If I were a Hunter, I’d be going on a raid with Won Myunghoon, too.”

Jinho hyung muttered sadly, his face full of envy.

To be honest, I was a little nervous myself.

*An A-Rank Gate with Myunghoon hyung.*

It would be my first time challenging an A-Rank Gate, but I was also excited at the thought of raiding alongside an old idol of mine.

*I never thought I’d live to see a day like this.*

I left the house with my heart fluttering.

* * *

If mid- and low-level Gates were grains of sand, an A-Rank Gate was a massive boulder.

Even in Korea, a country famous for having many Gates despite its small territory, there were few A-Rank Gates. As a result, competition for raids was fierce.

For the Peace Guild, which still had only five official Guild members, this was unquestionably an opportunity that would be extremely difficult to obtain.

And yet…

*Why is everyone so relaxed?*

Even I, who considered myself the strongest person here, had to swallow nervously. But Team Leader Choi, Butler Kim, and Song-i looked as calm as if they were going to the neighborhood supermarket.

“Did they change this to a B-Rank Gate without telling me?”

Team Leader Choi answered in his usual calm voice.

“It is an A-Rank Gate.”

“Then why are you all so composed? Did everyone secretly take Cheongsimhwan?”[^2]

[^2]: Cheongsimhwan is a traditional herbal medicine taken to calm the mind and body.

“Song-i and I have been to plenty of them. Back when we were with the Ares Guild.”

“Ah. Right.”

Ares was the greatest Guild in Korea—no, in Asia—and a major Guild recognized throughout the world.

Its strength was one thing, but it was also made up entirely of elites. There was no reason they couldn’t handle an A-Rank Gate.

“And as for Butler Kim…”

At Team Leader Choi’s words, Butler Kim smiled broadly.

“I saw more than enough of them during the Great Cataclysm.”

“……”

“Back when I was active, monster armies used to pass along the highways, and packs of drakes flew through the sky. Things like that.”

What the hell? That was terrifying.

As expected of someone from the Great Cataclysm generation. His level of experience was on an entirely different scale.

Butler Kim was publicly known as a B-Rank Hunter, but he was actually powerful enough to make Im Chunsoo—an A-Rank Hunter and the Guild Master of Sangdong Guild—do physical-training exercises.

*What on earth is someone like him doing here?*

Team Leader Choi and Butler Kim’s true identities and relationship remained a mystery.

They knew I was curious, yet still refused to tell me. They must have their reasons.

*That aside…*

I turned my gaze toward the last remaining Guild member.

The one person I had been most worried about. Contrary to my expectations, Im Kkeokjeong was leaning back against the car seat with a calm expression.

“Are you all right?”

“Of course I’m all right—urrrgh!”

“……”

*Fine, my ass. You’re nervous as hell.*

Perhaps he knew it himself, because he quickly pulled out the black plastic bag he had brought in advance and buried his face in it.

After finishing a bout of retching, Im Kkeokjeong muttered with a deathly pale face,

“I’m fine. Really.”

Kkeokjeong hyung might have been fine, but I wasn’t. The very act of letting a D-Rank Hunter enter an A-Rank Gate was a dangerously reckless decision.

“Uh, I’m only saying this just in case…”

As soon as I cautiously began speaking, Im Kkeokjeong shook his head.

“No. The Guild Master and Team Leader gave me permission, too. I can’t keep imposing on everyone forever. I need to gain some experience.”

“Hmm.”

“Taekyung, I have a wife and children. I’m already past the age where I can make decisions based on pride or childish impulses. Even if something happens…”

“Ah, I understand. That’s enough.”

I hurriedly cut him off before he could keep saying ominous things.

He must have been worrying a lot lately because his rank was so much lower than those of the other Guild members, but he had taken it far too far.

“We’ll go in safely and come out safely. The Star Guild is sending two A-Rank Hunters, too. And Myunghoon hyung used to be a ranker.”

Between the two Guilds, there were four A-Rank Hunters and over ten B-Rank Hunters. They had more than enough strength to compensate for Kkeokjeong.

Team Leader Choi nodded as well.

“Nothing will happen.”

He was a cautious man. If he had decided to let Im Kkeokjeong participate, it was because he had the confidence that it would be safe.

“Yeah. It will.”

A faint smile appeared around Im Kkeokjeong’s mouth.

That was when the tall buildings outside the car window began to come into view.

It looked like an entire village—or even a small city.

The residents and guards there were soldiers carrying firearms and Hunters decked out in expensive equipment.

“Wow.”

Unlike me, who let out an exclamation, Team Leader Choi frowned.

“This place…”

After looking around at the view outside, Team Leader Choi turned toward the driver.

He was driving the limousine bus Won Myunghoon had sent especially for us.

“I think you may have come to the wrong place.”

“What? That can’t be.”

The driver opened his eyes wide, as if he had no idea what Team Leader Choi meant.

“The A-Rank Gate, The Black Wyvern’s Nest. This is the right place. I entered it into the GPS and came straight here.”

“The Black Wyvern’s Nest? There must have been some mistake. Won Myunghoon said…”

“Who’s Won Myunghoon? I work for the bus company, so I don’t know him. I came exactly where I was told to go.”

The voices of Team Leader Choi and the driver buzzed in my ears.

Suddenly, my stomach began to churn, and a sharp pain throbbed through my head.

Amid the confusion, a roar I had heard three years ago shook my mind.

*“Kyaaaaaaar!”*

Blackened eyes and a tongue sharp as a blade.

The wingbeats of the creature that had brought down the cave and the claws that had torn my teammates to pieces rose vividly in my mind, blurring my vision.

*The Black Wyvern.*

*To think we’d meet again like this.*

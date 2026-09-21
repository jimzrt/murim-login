# Checkpoint Review — 600–604

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

# Chapters 600–604

## Plot

Jin Taekyung tells Team Leader Choi about the second secret area in Area A, and Choi reveals that it hides Cheon Taemin, who has been unconscious for more than twenty years. To stop the investigation and secure Taemin, Choi begins reclaiming Ares Guild as Cheon’s only maternal grandson. He pressures the remaining executives, publicly announces his lineage, and gains their support with Jin’s help. Park Daewon backs his return and prepares the formal board process.

Baek Hanseong then negotiates an alliance with Choi, agreeing to settle the Guild Association dispute and halt the investigation at Ares headquarters. Choi is unanimously elected Guild Master of the Peace Guild and Vice Guild Master of Ares Guild. Jin, Choi, and the Skeleton King search Area A, where Jin’s Middle Dantian partially activates at 10% and expands his Qi Sense enough to locate the concealed subspace. He tears through its magical barrier with Force.

The subspace is Lee Jungryong’s private vault and prison, containing vast wealth, rare treasures, and Cheon Taemin alive inside a wired mechanical capsule. Choi recognizes Taemin as his maternal grandfather and keeps his survival secret with Jin and the Skeleton King. Since Taemin cannot remain there, they seek a trusted person capable of teleporting him; the unnamed contact agrees to come to Korea after hearing Choi’s request.

## Continuity

- Cheon Taemin is alive but unconscious after more than twenty years, confined in a wired mechanical capsule inside Lee Jungryong’s hidden vault.
- Cheon Taemin is Choi Minwoo’s maternal grandfather and only living blood descendant.
- Jin, Choi, and the Skeleton King know Taemin’s location and are concealing his survival from the authorities and Ares Guild.
- Jin opened the concealed Area A subspace using expanded Qi Sense and Force.
- The subspace contains approximately five hundred Magic Gems, five S-grade Magic Gems, gold, diamonds, bonds, and priceless artwork.
- Jin’s Middle Dantian is partially activated at 10%, improving the efficiency of his martial arts and internal energy.
- Choi Minwoo is Guild Master of the Peace Guild and Vice Guild Master of Ares Guild.
- Baek Hanseong and Choi have formed a cooperative relationship; the Guild Association dispute and Area A field investigation are being halted.
- Lee Jungryong and Song Cheonwoo concealed Taemin’s condition, but the cause of his prolonged unconsciousness remains unknown.
- Taemin must be moved covertly through teleportation magic. A trusted but unidentified helper has agreed to come to Korea.
- Go Se-won’s promised repayment to Jin remains unexplained, and the authorities’ final resolution of Jin’s charges remains pending.

## Translation Decisions

- Use **Area A**, **Middle Dantian**, **Qi Sense**, **Force**, **Magic Gems**, **Guild Association**, **Guild Master**, **Vice Guild Master**, and **maternal grandfather**.
- Use **Team Leader Choi**, **Skeleton King**, **Ares Guild**, and **Peace Guild** consistently.
- Render **외할아버지** as **Grandfather** when Choi addresses Cheon Taemin.
- Use **Salvator Mundi** and preserve the regional wordplay involving Gyeongsang-do.
- Retain **Magic Johnson** for 매직 존슨 and **Mr. President** for direct presidential address.

## Durable state

{
  "active_continuity": [
    "Cheon Taemin has been unconscious for more than twenty years and is hidden alive inside a wired mechanical capsule in a secret subspace within Ares Guild's Area A; Team Leader Choi has confirmed that Taemin is his maternal grandfather.",
    "Jin Taekyung discovered and opened the concealed Area A subspace using expanded Qi Sense and Force.",
    "The subspace is Lee Jungryong's private vault and prison, containing approximately five hundred Magic Gems, five S-grade Magic Gems, gold, diamonds, bonds, and priceless artwork.",
    "Lee Jungryong and Song Cheonwoo concealed Cheon Taemin's condition, and Choi Minwoo now controls the Guild power needed to investigate and relocate him.",
    "Choi Minwoo has publicly identified himself as Cheon Taemin's maternal grandson and only living blood descendant.",
    "Choi Minwoo is Guild Master of the Peace Guild and Vice Guild Master of Ares Guild.",
    "Baek Hanseong and Choi Minwoo have established a cooperative relationship concerning the two Guilds and the government's response.",
    "Go Se-won remains the person closest to the surviving secrets of Ares Guild and has not explained what debt he intends to repay to Jin Taekyung.",
    "Jin, Choi, and the Skeleton King are keeping Cheon Taemin's survival and location secret.",
    "Cheon Taemin must be moved covertly by teleportation magic with help from a trusted person who has been contacted but not identified."
  ],
  "continuity_sources": [
    603,
    604
  ],
  "open_questions": [
    "What caused Cheon Taemin to lose consciousness and remain in a vegetative state for more than twenty years?",
    "Who can provide the teleportation magic needed to move Cheon Taemin safely and covertly, and where can he be taken?",
    "What debt does Go Se-won mean to repay to Jin Taekyung?",
    "How will the authorities ultimately resolve the charges against Jin Taekyung?"
  ],
  "safe_through": 604,
  "temporary_decisions": [
    "Use Team Leader Choi for 최 팀장.",
    "Use Butler Kim for 김 집사.",
    "Use President's Security Service for 청와대 경호실.",
    "Use Grandfather for 외할아버지.",
    "Use Guild Association for 길드 협회."
  ],
  "version": 1
}

## Reading copies

## Chapter artifact 600

# Chapter 600

The sorrow of losing something precious never disappears completely. With the passage of time, it only wears down little by little and grows hazy.

And in that sense, the week that had passed was exactly the time Team Leader Choi needed to pull himself together.

“He’ll rest peacefully. Butler Kim will. But we’ll be even busier from now on, won’t we?”

From those quietly spoken words, I could tell that he was ready.

Ready to rise while keeping the person who had left us in his heart. Ready to start walking forward again.

Which meant I could finally say it.

“I met Go Se-won a week ago.”

Team Leader Choi reacted to my abrupt remark.

“Go Se-won… You mean Ares Guild’s Head of Security?”

“Yes. The very man who was Go Jun’s closest aide.”

At the mention of Go Jun, Team Leader Choi’s straight eyebrows twitched.

But only for a moment. He quickly composed his crumbling expression and answered in a calm voice.

“Please continue.”

“He was the one who requested the meeting. He said he had a debt to repay to me.”

“A debt to repay. Given his actions, I doubt it was simply a matter of expressing his gratitude.”

Team Leader Choi had never met Go Se-won in person, but his guess was sharp—and accurate.

I nodded in confirmation and slowly told him everything I remembered from that day.

The private meeting held inside the special detention center. And the existence of another secret area, something only I had heard about.

“He said he didn’t know its exact location or what the space was for. Only that Lee Jungryong and Go Jun were the only ones allowed to enter.”

After hearing the entire story, Team Leader Choi muttered quietly.

“I had my suspicions… So it was all true.”

“Excuse me?”

His reaction was completely different from what I had expected. When I stared at him with wide eyes, Team Leader Choi asked me a question.

“Other than you, Mr. Jin, does anyone else know about this?”

“Uh, I think Go Se-won and I are the only ones. We temporarily blocked the sound, and we covered our mouths while speaking.”

“You said the President’s Security Service accompanied you.”

“They seemed suspicious, but they haven’t asked any questions or shown any particular reaction. They might have reported it to President Baek Hanseong, though.”

“I see.”

I had answered his questions honestly, so now it was my turn. I looked at Team Leader Choi, my own question in my eyes.

“Did you already know about this, Team Leader Choi? Your reaction makes it seem that way.”

Team Leader Choi nodded without offering any particular denial.

“I heard it from someone else as well.”

“…So there weren’t two people who knew. There were four. At this point, doesn’t President Baek Hanseong know too?”

“I doubt it. Ares Guild’s security is extremely thorough, and information concerning Area A was restricted to a very small number of people. Besides…”

Team Leader Choi added in an even tone.

“There are three people. Not four.”

“Excuse me?”

“The person who told me about it died recently. Of course, he too was once as close to Ares Guild’s dark secrets as Go Se-won was.”

As far as I knew, there couldn’t have been many people like that. In fact, there had been so few since Ares Guild’s founding that they could be counted on one hand.

*And if he died recently…*

One name flashed through my mind.

When I finally realized who he was, I muttered in a low voice.

“Song Cheonwoo.”

Team Leader Choi nodded and continued.

“When we last met inside a Gate, he told me about several secrets he had hidden until then. I don’t know whether it was his final pang of conscience or whether he simply wanted to put his own mind at ease.”

The reason didn’t matter. The water had already been spilled, and there was no way to put it back.

But we still had to search the spilled water for traces.

“Did Song Cheonwoo know the location or purpose of the other secret area? That old man seems like the sort who would.”

“He didn’t know the location either, but he knew what it was for.”

“What is it?”

The purpose of the other secret area. That was what I had been most curious about all this time. If Area A was the shell, then the secret area inside it was the core.

Lee Jungryong and Go Jun. What secret had those two master and disciple shared?

What had been hidden inside a place that remained unknown even now, while Area A was being investigated down to the last detail?

*An astronomical amount of cash? S-rank Magic Gems smuggled away in secret? Or maybe… a human experimentation lab?*

Keywords from all kinds of conspiracy theories and movies flashed through my mind.

But the next words Team Leader Choi spoke left my cluttered thoughts completely blank.

“It is my maternal grandfather.”

“Excuse me?”

“The purpose of the other secret area is to hide my maternal grandfather’s existence from the world.”

“…!”

* * *

How much time had passed?

Even as the wind blew and clouds drifted slowly overhead, I couldn’t move for a long while.

*This is insane.*

I never would have thought of this.

Cheon Taemin. That Cheon Taemin was inside the secret area.

It felt like A-Gwi of Gyeongsang Province had smashed the back of my head with a sledgehammer.

I had stood frozen like a stone statue, but somehow I managed to force out a voice.

“Um… You don’t happen to have two maternal grandfathers, do you?”

“…”

“No, this is something we need to be absolutely certain about.”

Team Leader Choi looked at me as though he were wondering if I was an idiot, then answered.

“As far as I know, no.”

“…Huh.”

*Holy shit. I guess it really is him.*

And as I stood there, temporarily speechless, Team Leader Choi sent another home run flying straight at me.

“I heard he lost consciousness more than twenty years ago. Lee Jungryong and Song Cheonwoo concealed that fact and kept it secret all this time.”

“…He lost consciousness? Cheon Taemin? I mean… *the* Cheon Taemin?”

The immortal hero born from humanity. The Slayer.

Cheon Taemin, who had even defeated the Demon King Asmodeus, was in a vegetative state.

That was harder to believe than Jin-ho hyung passing the civil service exam or Hyuk Mujin becoming the Murim Alliance Leader.

*How could that be possible?*

Cheon Taemin stood in a position comparable to the Martial God of the Murim.

More than twenty years had passed since he went into seclusion, but no one had even come close to reaching his level.

A flawless warrior who possessed absolute power.

The reason he had gained his current authority and come to be called an immortal hero was because he truly possessed power of that magnitude.

And yet someone like Cheon Taemin had supposedly remained in a vegetative state for decades—even in the modern world, where cutting-edge medicine and magical treatments existed.

*Something stinks.*

It seemed that thought had shown plainly on my face. Before I could say anything, Team Leader Choi shook his head.

“I don’t think Lee Jungryong or Song Cheonwoo were the ones who did that to him.”

“What makes you think that?”

“Everyone becomes honest in the face of death. Even more so when their families are being held hostage.”

“…Phew. That makes sense.”

“The important thing is that my maternal grandfather is hidden in another secret area within Area A. And no one except those three knows about it. Not even the government, despite its thorough investigation of Area A.”

I thought of President Baek Hanseong, who had been beside me throughout the national funeral, and asked. If there was one profession better than any other at hiding what they truly thought, it was politicians.

“Are you sure?”

“This isn’t a simple guess. It’s a certainty based on information. Several key insiders within the government investigation team sent to the site have already joined forces with us.”

“…!”

“So at least for now, you can rest easy.”

As I watched Team Leader Choi explain everything in a calm tone, a thought suddenly occurred to me.

Perhaps the past week had done more than help him rise from his grief. Perhaps it had made him run.

*This man… had already begun.*

Team Leader Choi had endured a life-or-death crisis in Sichuan and indescribable grief in Pyeongchang. Somewhere along the way, he had grown tremendously.

And I had a fair idea where his next step would lead as he ran forward in long strides.

“The investigation is expected to take at least a month. What would you do, Mr. Jin?”

“We’d have to stop the government’s investigation first. To secure that person while avoiding suspicion.”

“Then what would be the fastest way to stop the investigation?”

“We need to put this situation to rest and become the lawful owners of Area A as soon as possible.”

And becoming the lawful owner of Area A meant only one thing.

Team Leader Choi reached out and ran his hand over the memorial stele.

“I once made a promise to Butler Kim.”

The impregnable fortress surrounding the royal castle had collapsed miserably, and the prince who had been stripped of his right to inherit the throne and sent into exile had finally returned after a long passage of time.

To reclaim the crown stolen from him long ago.

“I promised him I would make Ares Guild mine. No matter what.”

His deeply sunken eyes gleamed.

Team Leader Choi stared at the name of the late Kim Hwajong, carved highest of all, then turned toward me.

“Will you help me?”

It was a question he didn’t need to ask.

From the day I signed the contract he had first offered me, my answer had already been decided.

“The contract still has a long time left on it, so I’ll help. But we’re not going to have to kill anyone else, right?”

At my shameless counterquestion, Team Leader Choi let out a quiet laugh.

It was the first time he had smiled since waking up.

He pulled out his smartphone and answered.

“No. This time, all you have to do is be the stick.”

“The stick?”

“Yes. A little carrot and stick for the people who are hesitating.”

Beep. Beep. Beep.

Click.

After the third ring, someone answered the phone. Team Leader Choi addressed the unidentified person on the other end in a voice without any rise or fall.

“Hello, Vice President Park Daewon. This is Choi Minwoo.”

The moment I heard that name, which had appeared so often in the news lately, I realized who he was speaking with.

*The most senior executive currently remaining in Ares Guild.*

With Vice Guild Master Go Jun dead and most of the executives who held real power dragged in for questioning by the prosecutors’ office after Go Se-won’s revelations, he was the man who had inadvertently become Ares Guild’s acting head.

“Yes. I’m listening. Team Leader Choi Minwoo—no, Mr. Choi Minwoo.”

The dark voice coming through the phone was met by Team Leader Choi’s gentle reply.

“You still seem unable to make up your mind. Judging from how you left without saying much even after the national funeral.”

“I, well… It’s just that…”

“Six o’clock this evening.”

“Excuse me?”

“I’ll come to the headquarters myself. When I open the conference room door and walk in, I want all the executives—including you, Vice President Park—to be there.”

“W-wait a moment, please. I still need time…”

“Six o’clock this evening. You still have three hours, so that should be plenty of time. Goodbye.”

Click.

*What in the world was going on?*

I stared dumbfounded at Team Leader Choi as he hung up without hesitation. He spoke as though nothing unusual had happened.

“I assume you have a rough idea of the situation since you heard the conversation. Let’s go.”

“Right now? Leaving everything else aside, you said there are still three hours.”

“I’m going to hold a press conference as well.”

“…Excuse me?”

“It’s going to be a busy day. We’ve waited a long time. Once you draw your sword, you have to swing it like lightning.”
## Chapter artifact 601

# Chapter 601

Ares Guild headquarters was still being repaired.

The atmosphere inside the conference room was heavy.

Around a massive round table, some thirty men and women sat with somber expressions, all watching one person’s mouth.

“…And that is why I called this emergency meeting.”

The moment Vice President Park Daewon finished speaking, several reactions erupted from every corner of the room.

“Well, well. They certainly looked down on us. And by a brat who isn’t even thirty, at that.”

“His intentions are laughably obvious. Isn’t he simply planning to swallow all of Ares whole?”

“No, hyung. Why would you call an emergency meeting at the request of an outsider who has no authority? Even if you are the Vice President, this is going too far.”

As voices of condemnation rushed at him from all sides, Vice President Park rubbed his half-bald forehead with a handkerchief.

Now nearing sixty, he found the entire situation bewildering.

*Phew. How had things come to this?*

He had distinguished himself on the battlefield, but had never possessed much talent for political infighting.

Fortunately, his personality—one that avoided making enemies—had allowed him to hold on to the largely ceremonial position of Vice President until now.

But just ten days earlier, while on vacation before his retirement, he had heard unbelievable news.

Ares Guild headquarters had been crushed by a single person, and Go Jun, the Vice Guild Master, had been murdered.

*That couldn’t be true.*

That was what he had thought. For at least the first ten minutes.

But every bit of it had been true. The impregnable fortress they had spent some thirty years building had fallen, and its newly appointed City Lord had lost his head before he had even settled into office.

And the retainers who had barely escaped the prosecutors’ handcuffs were now voicing their complaints in unison.

“This is absurd! There’s no need to listen to such nonsense.”

“We created the name Ares, and we were the ones who protected it. What right does some outsider—some bloody brat who still doesn’t know how the world works—have to interfere?”

“Vice President Park, this really isn’t right!”

“……”

Park Daewon silently took a long drink from his glass of water.

Everyone gathered here had spent at least ten years, and as many as thirty, working for Ares Guild.

Even if most of the people who held real power within the Guild had been summoned by the prosecutors’ office, these men and women were far from powerless.

*……But that doesn’t mean we can ignore him.*

Park Daewon knew all about Choi Minwoo.

No, he couldn’t not know. Cheon Taemin’s private life and family relationships had been protected with the utmost care, but things were different for the few people classified as his close associates.

Park Daewon, one of the founding members, was one of them.

*The first time I saw him was at his first-birthday ceremony, and the last was at the funeral…wasn’t it?*

The child who had been slowly fading from his memories had grown up and returned. He had come to reclaim what he himself had lost long ago.

Park Daewon, who had spent his entire life simply going along with every situation, couldn’t shake the discomfort in his chest.

It was a shallow sense of guilt born from the fact that he had turned away from Choi Minwoo when the boy had been completely excluded from the Guild.

*What should I do?*

While Park Daewon was lost in thought, a short, powerful voice rang through the noisy conference room.

“I was going to watch and see how far this went, but it gets more appalling by the minute. I can’t listen to any more of this.”

“……!”

“……!”

A chill fell over the conference room.

Several pairs of widened eyes focused on one person.

“Managing Director Kim, what kind of outrageous statement was that?”

“Managing Director, my ass. Hey, Kim Gwangpil! What the hell are you talking about?”

After the brief silence came a harsh outburst, and Managing Director Kim shrugged his broad shoulders.

“Was anything I said wrong? I only called it appalling because it is. And Executive Director Baek, watch your language. Even if I am your junior, those words are unpleasant to hear.”

“Just you wait, you traitorous bastard……”

Managing Director Kim’s thick eyebrows twitched.

“What? Traitorous bastard?”

“Yes, you bastard! If there hadn’t been traitors like you, we wouldn’t be in this goddamn situation!”

“Wasn’t it the people on Executive Director Baek’s side who acted like animals? We can figure that out simply by seeing who’s in the detention center right now.”

“What?”

“You seemed awfully bothered that a few executives and I joined Jin Taekyung. But in the end, what kind of shit was the Vice Guild Master—no, what was that man Go Jun—up to? Or did you have a hand in it too, Executive Director Baek?”

“You, you bastard……!”

“Hey, Managing Director Kim! Watch your mouth!”

“You’re the ones who should be watching your mouths!”

“Exactly!”

“How dare these bastards!”

The conference room split into two factions, with furious shouts flying back and forth.

That was when Vice President Park Daewon, who had remained silent by himself, suddenly spoke.

“Strictly speaking, he isn’t an outsider.”

At those words, the executives who had been shouting at one another stopped short.

“What?”

“Vice President Park. What did you just say……”

“I’m talking about Choi Minwoo.”

Park Daewon slowly looked over the thirty-some executives before continuing.

“Isn’t he Guild Master Cheon Taemin’s only maternal grandson?”

“……!”

“……!”

His single statement struck directly at the room’s blind spot, and silence descended over the conference room.

For an instant, bright light appeared on the faces of Managing Director Kim and his faction, while the executives who had been loudly voicing their complaints turned pale.

“But—but that’s just a rumor, isn’t it?”

“Th-that’s right, hyung. It’s an unconfirmed rumor.”

Ever since the Small Cataclysm, rumors about Choi Minwoo’s identity had been quietly spreading.

So their behavior was less a matter of not knowing than of pretending not to know.

But at least Park Daewon wasn’t pretending.

“No, I’m certain. As I remember it, he is definitely that person’s maternal grandson. And……”

Before anyone could force out another rebuttal, Park Daewon placed the smartphone in his hand on the table and continued.

“It seems he has decided to reveal it himself now.”

“What do you mean……”

“Fight among yourselves if you like, but you should at least have checked what was happening outside, especially with the secretaries you brought barred from entering. Isn’t that right?”

At those words, several people realized something and hurriedly pulled out their smartphones.

Before even a minute had passed, startled gasps rang out throughout the room.

A reporter’s urgent voice played from dozens of smartphones.

> “M-Mr. Choi Minwoo! Could you state your maternal grandfather’s honored name once more, clearly?”

And then another person’s voice rang through the conference room.

> “The Cheon character, the Tae character, and the Min character. Cheon Taemin. He is my maternal grandfather.”

> “……!”

> “……!”

The ceaseless camera flashes and the surrounding murmur vanished in an instant.

The same silence had fallen not only over the place where the official press conference was taking place, but also over the conference room.

Everyone had carried the same suspicion in their hearts. But when that suspicion became fact and was announced to the world, its impact was far greater than anyone could imagine.

All the more so when it concerned the only blood relative of Cheon Taemin, a man about whom everything was shrouded in mystery.

At the same time, everyone in the conference room realized the same thing.

*He has finally drawn his sword.*

More than twenty years of life that had been little different from exile.

At last, the royal grandson had drawn the sharpest sword at the most opportune moment. He had come to reclaim what he had lost through his own strength.

But the most important question was where that blade would be swung—and whom it would be aimed at.

Gulp.

No one could bring themselves to speak easily. As time passed in an atmosphere where an invisible thread of tension had been pulled taut, the room filled with faint whispers.

Then—

Beep.

Everyone’s head moved at once with the tiny electronic sound.

The source was the clock mounted on the broad wall of the conference room.

The current time glowed on its red LED display, as though warning them of danger.



**PM 06:00**



Six o’clock in the evening.

The time they had gathered here—and the time that signaled someone’s arrival.

Step. Step.

Everyone heard shoes crossing the hallway outside the door, and without realizing it, they reflexively rose from their seats.

And then……

Click.

Two people appeared beyond the smoothly opening door.

“You gathered early.”

“Oh, they fixed this place pretty quickly. I think I was the one who broke it last time.”

It was the arrival of an invading force—polite and rude at the same time, but impossible to avoid.



* * *



When I was young, my father used to say this like it was a proverb.

*Son, once a man draws his sword, he has to cut at least a radish.*

From that perspective, Team Leader Choi was a man among men. He had come here not to cut a radish, but to cut down Ares Guild.

“……”

Come to think of it, I had already cut it down once myself.

But still.

“Nice to meet you. I’m Choi Minwoo.”

With a polite greeting, Team Leader Choi bowed his head.

The Ares Guild executives who had been standing around the large round table awkwardly returned his greeting.

Some wore such dark expressions that one might think the world would end in three seconds. Others were familiar faces with smiles spread wide across their lips.

They were the executives from Song Cheonwoo’s faction—the ones who had sided with me during the assault on headquarters.

But one person’s attitude was difficult to judge.

The elderly middle-aged man seated at the head of the table.

Vice President Park Daewon.

“Welcome, Team Leader Choi Minwoo.”

Team Leader Choi studied Park Daewon’s conflicted expression for a moment, then nodded.

“I hope I’m not late. The press conference went longer than expected, so I ended up being discourteous despite myself.”

I had expected this, but judging by everyone’s expressions, they had watched the main broadcast live without missing a second.

Of course, about half of them didn’t seem to be enjoying the value of their license fees, judging by the atmosphere.

“Of course not. Then, before we begin, please take a seat……”

“That won’t be necessary.”

Team Leader Choi stopped Vice President Park as he gestured toward a seat, then continued in a gentle voice.

“We’ll be finished soon enough. Since everyone here still considers me an outsider, wouldn’t it make things uncomfortable if I let the conversation drag on?”

“……Ahem.”

His words had a barb in them, and awkward coughs erupted from several places.

Team Leader Choi looked around without the slightest concern for their reactions, then suddenly spoke.

“Now that I look around, five seats are empty. The three advisers. And where are the directors of the United States and French branches?”

A middle-aged man with a prickly appearance answered with an uncomfortable expression.

“You seem very interested in our people.”

“My memory is quite good, Executive Director Baek.”

“……”

Executive Director Baek closed his mouth.

Then one of the executives who had joined my side ten days earlier answered quickly.

“They didn’t come.”

“It seems they had unavoidable circumstances. Is that right?”

“I understand that the three advisers were absent because of illness, while the two branch directors refused to attend.”

“I specifically told them to attend. It seems my wishes weren’t conveyed properly.”

Team Leader Choi muttered this calmly, and Executive Director Baek spoke again.

“This isn’t an official meeting. It’s a gathering held at the request of an outsider. There’s no reason we had to attend. Even if that outsider is……”

After hesitating for a moment, he continued in a distinctly quieter voice.

“That person’s maternal grandson.”

“You’re right.”

Team Leader Choi nodded in agreement, then took a small note from inside his clothes and handed it over.

“What is this?”

“A prescription for the advisers who are suffering from illness. Ah, as for the two other branch directors, something else will be sent in place of a prescription.”

The people who had used illness as an excuse to skip the meeting would probably recover from every ailment the moment they saw that note.

They contained a detailed record of crimes that had not yet been revealed.

Executive Director Baek swallowed hard after reading the note.

“T-this……”

“Executive Director Baek, you don’t look well either. Should I give you a prescription as well?”

“N-no. What are you talking about? I-I’m fine!”

I stood with my arms crossed, watching the situation, and muttered.

“Wasn’t that ‘I’m fine’ a little too casual?”

“I—I am quite well.”

“One Hundred and One Ways to Kill Without a Sound, by Jin Taekyung.”

“I—I’m perfectly fine, sir.”

Hmm. He definitely seemed capable of understanding what people were saying.

I glanced at him as he stood there swallowing nervously, then spoke to Team Leader Choi.

“Can’t we sit down and talk? My legs hurt.”

“Well, there isn’t really a suitable seat…”

As he let his sentence trail off, I helpfully pointed toward the head of the table.

“There. The seat’s empty.”

“Oh, I see. But would it be all right for me to sit there?”

“Let’s vote. By majority rule. Anyone opposed, raise your hand?”

“……”

No one raised a hand.
## Chapter artifact 602

# Chapter 602

Whipping someone is an effective way to force them to do something, but it can also breed resentment. In that sense, Team Leader Choi was a man who knew exactly how to use the whip in his hand.

“Director Hong.”

At Team Leader Choi’s call, made naturally from the seat of honor, one of the youngest executives answered with a nervous expression.

“Yes, yes.”

“I’ve heard plenty about you, Director Hong. That you’re exceptionally capable.”

“Oh, no. I’ve simply been lucky…”

“A position as an Ares Guild executive isn’t something you can reach through luck alone. Especially at your age. Wouldn’t you agree?”

“……”

Team Leader Choi’s tone and voice were gentle, but an unmistakable anxiety appeared on Director Hong’s face. And there was bound to be a reason why Team Leader Choi had singled out one person from among dozens of executives.

“When I was young, I grew up abroad, so adapting was difficult. But I suppose it was still a place where people lived, because I gradually made a few friends.”

Even if he had been exiled, he was still a royal grandson in the end. Team Leader Choi had lived a life on an entirely different level from that of a small-time citizen like me, and his connections were beyond anything I could imagine.

“Those friends occasionally pass along various bits of news. I heard some interesting things about you as well, Director Hong.”

“……Did you?”

“Yes. They had nothing but praise for you. Of course, the same goes for everyone else here.”

Whenever Team Leader Choi’s calm gaze shifted, the executives who met his eyes flinched as though they had been burned. Unless they were idiots, none of them could possibly take his words at face value.

*Stagnant water eventually rots.*

Ares Guild was one of the largest organizations in the world, and an executive position in a place like that allowed a person to seize astronomical wealth and honor.

How many of the executives gathered here were as clean as fresh water? The reason they had avoided being summoned by the prosecutors’ office until now wasn’t that they were pure and honest. It was because they were only about third-grade water.

The ones with wastewater or filth floating around them were already holding a reunion in the detention center.

“Are you feeling unwell? You’re breaking out in a cold sweat.”

At Team Leader Choi’s question, Director Hong wiped the sweat from his forehead and answered.

“Oh, no. It’s just a little hot.”

“There must be a problem with the temperature-control Magic. You should have it fixed quickly.”

The conference room was being maintained at a comfortable temperature through Magic, but half the executives were breathing heavily as if they had stepped into a steam room. Everyone had seen the whip concealed in Team Leader Choi’s sleeve. Rather than actually swinging it, he was pressuring the executives by letting them glimpse it.

But there were exceptions to everything.

“This is too unpleasant to listen to.”

The person who spoke was a middle-aged man with sharp, irritable eyes. His white beard was sparse, and he tapped the round table with thick knuckles as he continued.

“Are you seriously threatening us?”

“You’re Director Kim, in charge of the Asian region.”

At the blatant question, Team Leader Choi rubbed his chin and asked in return.

“Did it feel that way?”

“What if it did?”

“Then I won’t deny it. Because it’s true.”

“What did you say?”

“I said it was true. I am threatening all of you, and I intend to make Ares Guild mine.”

Team Leader Choi added one more thing in a gentle voice.

“Of course, I intend to do so legally, with everyone’s consent.”

“A lizard is saying it’ll swallow a dinosaur.”

Director Kim snorted as he looked back and forth between Team Leader Choi and me.

“You’re young, so you still have a lot to learn. Do you really think Ares Guild is that easy to laugh at?”

I nodded as though I found this interesting.

“Hmm. Somewhat?”

“……”

Perhaps he had nothing to say now that I had responded like that. After a brief silence, he continued.

“Just because headquarters fell, don’t make the mistake of thinking the entire Ares Guild is helpless. No matter how strong you are, do you really think you could take on all of us?”

It wasn’t entirely unreasonable. Ares Guild had a massive presence, with countless branches throughout the world, and the forces at headquarters were only a fraction of the whole. Even I couldn’t defeat every one of them by myself.

But still…

“So what?”

At my question, bewilderment flashed across Director Kim’s face.

“What?”

“I said, so what, asshole.”

“Asshole?”

“You fucking bastard. I’ll—”

“……Huh?”

*What the hell is this guy doing?*

That was exactly the expression on his face.

When I raised my fist, Director Kim instinctively dragged his chair backward and blinked.

“What……what kind of situation is this?”

“What do you think? I’m going to beat the shit out of you.”

“You’re going to use force? Now? Here?”

“Then should I use my brains? It’s already depressing enough that my intelligence is pathetic.”

“No……if you do that, it’ll be illegal.”

“Was killing Go Jun ten days ago legal?”

“……!”

“We’ll figure something out. I’ve already sent a few people to the grave, so who’s going to complain if I add one more? Right?”

At my question, Team Leader Choi smacked his lips.

“This is a somewhat different matter. Someone might actually complain.”

“The atmosphere’s pretty good these days, but even I can’t avoid prison, can I?”

“That’s right. But given how favorable the public image and public opinion surrounding Mr. Jin Taekyung are at present, if things go well, you might be able to settle for a few years.”

“Right. What if I was drunk?”

“Are you a genius? Then the sentence would be reduced considerably.”

“Come to think of it, I’ve been through so much lately that I might qualify for diminished mental capacity.”

“Oh, you might even be able to aim for a suspended sentence.”

What a wonderful country. If you got drunk and claimed diminished mental capacity, they even generously threw in sentence reductions.

But the face of the person listening to our hopeful conversation had turned ashen.

“You, you crazy bastards.”

“I thought you already knew. You didn’t? That I’m a crazy bastard?”

“……!”

“Watch your behavior. I’m trying to handle this amicably, so why are you the only one going off the rails?”

Of course, I was only saying that.

What mattered was how my words and actions came across to the other person. A madman who had smashed Ares Guild headquarters with his eyes rolled back and committed murder without caring about the consequences.

That was me.

In a situation like this, even a joke would sound serious.

*If the whip doesn’t work, you need one hell of a strong whip.*

It was just when even the closest thing to a dissenter had firmly shut his mouth that Vice President Park Daewon, who had been quietly observing the situation, suddenly spoke.

“I understand what the two of you want. In particular, regarding Team Leader Choi Minwoo’s return to Ares Guild……I support it in my capacity as Vice President.”

“V-Vice President.”

“Why? Is there a problem?”

“Well, that’s……”

Confused voices rose from several places at his sudden declaration of intent. But the tide had already turned, and Team Leader Choi threw the carrot he had prepared at them.

“If the rest of you accept Vice President Park Daewon’s opinion, Ares Guild will stabilize quickly. The vacancies created by this incident will soon be filled as well.”

“……What do you mean?”

“Separate from everything that has happened until now, I have no intention of denying your abilities. Once things settle down, there will be sweeping personnel changes.”

I could see the rabbits’ ears perking up as they realized what the carrot was.

If Ares Guild changed hands, the people in the most precarious positions would be its existing executives. But if that concern disappeared and they were even promised promotions as a reward, the situation changed.

*There’s no reason to refuse.*

On top of that, Team Leader Choi had no real disqualifying flaws. If anything, he was more than qualified. That was why he could continue speaking so calmly and confidently.

“I’ll put everything that has happened until now behind me. I’ll quickly stabilize the Guild, restore its tarnished image, and use this incident as a stepping stone to make it grow even larger.”

No one raised any more objections.

It wasn’t only because of the carrot being offered to them. They were also well aware of Team Leader Choi’s abilities.

In barely more than half a year, he had raised Peace Guild to its current position. There was no denying that my presence had played a key role, but without Team Leader Choi’s eye for people, his ability as a manager, and his political skill, the Peace Guild as it existed now would never have come into being.

And besides……

*He’s Cheon Taemin’s only blood descendant.*

Dynasties had disappeared from this country long ago, but the name Cheon Taemin belonged to the realm of divinity.

The bloodline of the savior who had saved humanity was noble and powerful in its own right. Neither the chaebol groups that had seized enormous wealth nor any dynasty that had ever existed could dare stand above Team Leader Choi.

And a title like that was bound to carry tremendous influence, especially within Ares Guild.

“Hmm.”

Low groans rose from various parts of the conference room. They knew it too. Lee Jungryong and Go Jun had been nothing more than usurpers, while Team Leader Choi—with undeniable legitimacy and ability—was the one suited to become the new City Lord.

Scrape.

More than ten executives rose from their seats, accompanied by the sound of friction breaking the quiet silence. They had effectively boarded the same ship ten days earlier, and they bowed politely toward Team Leader Choi without hesitation, as though they had been waiting for this moment alone.

“……!”

The tide had already turned.

They had seen both the whip and the carrot. Now it was time to choose.

The executives who had been watching the scene with wavering eyes began to rise one after another.

Scrape. Scrape.

Amid the sounds of chairs scraping across the floor, I sent a Sound Transmission to the two people holding out until the very end.

“Ah, fuck, seriously…”

“……!”

“……!”

The two men shuddered as though they had been electrocuted. Executive Director Baek and Director Kim rose from their seats on trembling legs and bowed.

Now, only one of the executives in the conference room remained seated.

*Vice President Park Daewon.*

Under the gazes of Team Leader Choi and me, he finally rose quietly from his seat. An aged voice slipped through his dry lips.

“Do you know that I’ll be retiring soon?”

Team Leader Choi calmly nodded, and Vice President Park Daewon muttered softly.

“Then this will be my final task.”

“If you wish, I can arrange for you to remain here longer.”

“No. I’m sorry I couldn’t look after you until now……and thank you. For coming back like this.”

Being the person among them who had belonged to Ares Guild the longest also meant he was the one who had turned away from Team Leader Choi for the longest time.

Vice President Park Daewon looked at Team Leader Choi with a complicated expression, as though a thousand emotions were crossing through him, then bowed politely.

Along with the words that announced everything was over, he said:

“I’ll convene an official board meeting, Young Master.”

“……!”

A glint flashed in Team Leader Choi’s eyes.

Surrounded by more than thirty retainers, he was already no different from the City Lord.
## Chapter artifact 603

# Chapter 603

*It’s over.*

Thud.

Baek Hanseong, the occupant of the Phoenix Chair, gave a bitter smile as he set down the report.

The report, submitted personally by the director of the NIS, contained a complete account of Choi Minwoo’s movements from the day before.

The press conference held immediately after the national funeral.

The atmosphere inside Ares Guild, where an emergency meeting had taken place.

*He moved this quickly?*

The secret of Choi Minwoo’s birth was something Baek Hanseong had already known.

But he had never expected it to be revealed in front of everyone at such a perfect moment.

No. More accurately, he had never expected Ares Guild’s executives to accept a new City Lord so easily.

*It must mean that much. The significance of Cheon Taemin’s bloodline.*

Cheon Taemin was a hero who symbolized humanity itself.

No matter how much filth had been smeared across Ares Guild by the series of incidents that had taken place, the symbolic power of the name Cheon Taemin remained unchanged.

No media outlet or celebrity would dare touch him, for he stood in a realm beyond reproach.

But that was not the only reason Choi Minwoo had created the Peace Guild of today and secured the support of Ares Guild’s executives.

*Jin Taekyung.*

A young hero who was fearless, approachable, and devoted.

As long as Jin Taekyung—who was steadily drawing closer to Cheon Taemin’s unrivaled reputation—stood beside Choi Minwoo, nothing could stand in their way.

The same would be true even if every powerful politician, chaebol corporation, and major Guild in the country joined forces.

“Mr. President.”

At the chief secretary’s call, Baek Hanseong looked up.

“What is it?”

“The Guild Association is asking to see you.”

The words he wanted to hear least had finally come.

The Guild Association, which represented the ten largest Guilds in the country, had been watching Ares Guild like a pack of wolves ever since the Go Jun incident.

They had cooperated so actively with the government not for the sake of social purification or justice, but because they wanted to strip away the treasures and remains of the fallen castle at last.

*That’s how it would have gone, if not for Choi Minwoo.*

Choi Minwoo was young, capable, and possessed legitimacy.

If he rose to the position of Vice Guild Master, Ares Guild would be rebuilt. With the positive images of Choi Minwoo and Jin Taekyung, it could even wash away the filth that covered it.

The Guild Association’s opposition had been expected.

The problem was that the person they were demanding rewards and reciprocal favors from was none other than Baek Hanseong himself.

The President muttered bitterly.

“…Well, speak of the devils.”

“Excuse me?”

“Nothing. As for the matter concerning the Guild Association, put it on hold for now.”

“Mr. President, I’m sorry to bring this up, but the requests have been coming in without pause…”

“I said put it on hold.”

The chief secretary flinched at the quiet voice, bowed his head, and turned away.

Once the door closed, Baek Hanseong rubbed his stiff, tired eyes.

The successive problems had exhausted him, both physically and mentally.

He even found himself desperately thinking about cigarettes—the habit he had quit immediately after being elected.

But what he truly needed now was not nicotine or tar.

It was a solution.

A way to untangle the problems knotted together like the Gordian knot of myth.

And the place most likely to provide the fastest and surest solution was not the Blue House.

*In the end, is this the only way?*

With a heavy heart, Baek Hanseong pressed the button attached beneath his chair.

A little over ten seconds later, the security officers waiting in the next room hurried in and bowed their heads.

“I was thinking of getting some fresh air. Would that be all right?”

The head of the Presidential Security Service answered with a calm expression.

“Of course, Mr. President. Do you have a destination in mind?”

A destination.

Baek Hanseong looked toward somewhere beyond the window and spoke.

“The Peace Guild. Let’s go to the Peace Guild.”

* * *

I had been wondering why the Guild was so quiet today.

There was a good reason.

At Team Leader Choi’s summons, I left the training room and entered the room. I understood immediately.

“You’ve arrived, Hunter Jin Taekyung.”

“…Why are you here again?”

At my genuinely heartfelt question, Baek Hanseong gave me a weary smile.

“I was wondering the same thing. Still, it’s good to see you again after so long.”

“Sure.”

I wasn’t sure whether seeing someone again after only fifteen days could be called a long time, but I pulled out a chair and sat down.

Baek Hanseong was holding a cigarette and turning it over in his fingers. I didn’t forget to add one more thing.

“This is a no-smoking area.”

“I know. I quit smoking a year ago.”

Baek Hanseong rubbed the dark circles beneath his eyes and continued.

“But lately… I’ve been wondering whether I should start again.”

He must have been through a lot. He looked ten years older than when I had last seen him.

I watched him sympathetically, then patted him on the shoulder in consolation.

“I get that, but I’m telling you, this is a no-smoking area.”

“…”

“So what brings you here?”

My question was merely a formality.

The middle-aged man in front of me was the President of a country. The head of state wasn’t some neighborhood bakery owner, and there were very few reasons he would come here in person.

Especially under circumstances like these.

As expected, Baek Hanseong gave a short, humorless laugh before answering.

“I believe the two of you have already guessed.”

Team Leader Choi spoke in a calm voice.

“It seems the Guild Association’s opposition is severe.”

“To be precise, it isn’t only the Guild Association. The political and business communities have chosen to step back for now.”

“They’ll move according to whichever way the scales tip.”

“Exactly. In the end, the Guild industry is the one most affected by this matter.”

Baek Hanseong sighed and continued.

“As you already know, they’re afraid of another Ares Guild appearing.”

Ares Guild was a predator in both name and reality. Especially in this country, it had wielded overwhelming influence since its founding. It would not have been an exaggeration to say that it possessed more power than the Blue House.

“The Guild Association won’t back down easily. This is an opportunity that may never come again. They want to use this incident to weaken Ares Guild and receive a portion of its interests as compensation.”

“…”

“But Team Leader Choi held a press conference and made contact with Ares Guild’s leadership…”

“That must be quite a burden.”

“To be honest, yes. They’ve been hounding me relentlessly.”

I had been listening silently to their conversation when I suddenly spoke.

“You can be more honest than that.”

“What do you mean?”

“You’re worried too, aren’t you, Mr. President? About a second Ares Guild. No, about a second Lee Jungryong.”

“…”

“Our Peace Guild is growing at a terrifying pace even as we speak. And now Ares Guild is going to bow before Team Leader Choi as well? If that happens, the game is completely over.”

The strength of a corporation came from its size and capital. The strength of a Guild came from the Hunters themselves.

In that sense, the Peace Guild of today possessed a reputation and military strength that far surpassed the ten largest Guilds in the country.

Because it had me, with my overwhelming power, and Team Leader Choi, Cheon Taemin’s only blood descendant.

*And what if Ares Guild joined us as well?*

Team Leader Choi would gain truly formidable power.

He would go from being the only contender capable of bringing down Ares Guild to becoming an unbeatable favorite whom no one could touch.

“Hmm.”

As Baek Hanseong groaned softly, I snapped my fingers.

Tap. Fwoosh.

A flame created with Samadhi True Fire flickered in the air.

Baek Hanseong stared at it in surprise. When I nodded, he understood my intention and placed the cigarette between his lips.

Sizzle. Hoo.

White smoke poured out with his breath. Perhaps because it had been so long since he had smoked, he leaned back against the sofa and closed his eyes before suddenly removing the cigarette from his lips.

“Hunter Jin Taekyung is right. I’m more worried about a second Lee Jungryong than a second Ares Guild.”

Team Leader Choi waved away the cigarette smoke with one hand.

“That’s unfortunate. I didn’t realize you thought of me that way, Mr. President.”

“Everyone changes. That’s something I learned after entering politics.”

“But you came here in person today. You even postponed your meeting with the Guild Association.”

“…”

“Why?”

Silence lingered for a moment before Baek Hanseong finally spoke with difficulty.

“I wanted to believe. I wanted to believe that the two of you sitting here were different.”

He looked at Team Leader Choi and me with subdued eyes before continuing.

“Isn’t what matters most not the strength or sharpness of a weapon, but the person holding it?”

He was right.

Even a cheap box cutter from a stationery store became a weapon in a criminal’s hand. And even a magnificent sword made of Ten-Thousand-Year Cold Iron became a kitchen knife in the hands of a master chef.

And the Team Leader Choi I knew was…

Capable and wise. The kind of person who would never swing the weapon in his hand carelessly.

“Then I suppose I can put your worries to rest.”

At Team Leader Choi’s quiet words, Baek Hanseong’s eyes lit up.

“What do you mean?”

“Trust me. I will use the influence and power I possess fairly and properly, and I will hand over enough interests to quiet the Guild Association. If you wish, I can even put it in writing.”

“!”

“But since I’ve given you the answer you wanted, I would like you to promise me one thing as well.”

Baek Hanseong blinked at the startling promise, then asked urgently.

“What is it?”

“I don’t want any more noise surrounding my actions from now on. Resolve the problem with the Guild Association, and stop the ongoing field investigation at Ares Guild headquarters.”

This was both an alliance based on trust and a transaction.

Baek Hanseong was a seasoned politician. Without much hesitation, he nodded.

“If you keep the promises you just made, that won’t be difficult.”

“Then it’s settled. Cleanly.”

As though they had planned it in advance, the two men rose from their seats at the same time and extended their hands.

Just as they were about to shake hands firmly, Baek Hanseong looked at me and suddenly spoke.

“Hunter Jin Taekyung. May I ask you one last question?”

“To me? Sure. I don’t see why not.”

“Your request that we stop the field investigation at Ares Guild… Is it related to the visit you made to the special detention center recently?”

“Ah.”

I had suspected that a report would reach him eventually.

Apparently, I had been right.

Our eyes met for a moment. I read the answer in the affirmative light shining in Team Leader Choi’s eyes, then shrugged.

“Yes. It is.”

“Huh. It seems there was something the investigation team failed to uncover.”

“Why? Do you want to search again, even now?”

“I am curious what Go Se-won was hiding, but… if I were that stupid, I would never have made it this far.”

Baek Hanseong answered like a politician, then smiled as he grasped Team Leader Choi’s hand.

“I hope we can maintain a good relationship from now on.”

“I look forward to working with you as well, Mr. President.”

It was the moment when the newly born super-Guild and the government established a firm cooperative relationship.

And it meant that the final obstacle standing between us and Ares Guild had disappeared.

* * *

“Could you say that again?”

“Cheon. Tae-min. My maternal grandfather’s name is Cheon Taemin.”

On the day of the joint national funeral for the victims, the reporters who had finished their coverage and were preparing to return were unable to process the bomb that had dropped on their heads.

No. Aside from the tiny number of people who had obtained the information beforehand, everyone was the same.

Cheon Taemin.

The immortal hero whose every detail had been shrouded in mystery for more than twenty years.

His only blood descendant, who had remained out of sight even amid the waves crashing over Ares Guild, had finally appeared before the cameras.

It was only natural that the media, both domestic and international, opened fire all at once.

[Peace Guild Team Leader Choi Minwoo: “My Maternal Grandfather Is Cheon Taemin.”]

[Press Conference Thrown into Shock. Ten Seconds of Silence.]

[Foreign Media in Uproar. Descendant of a Living Legend. Who Is Choi?]

[Lie or Truth? Debate Erupts over Choi Minwoo’s Shocking Statement.]

[Peace Guild Spokesperson: “Choi Minwoo Confirmed as the Peace Guild’s New Guild Master.”]

[Ares Guild Official: “Official Board Meeting to Be Convened Regarding Choi Minwoo. Likely to Take Office as New Vice Guild Master.”]

[The Peace Guild’s New Captain—and Ares Guild Comes Calling?]

[KakaoPage Web-Novel Reader Ttol*seu Comments on Chapter 599 of Some Novel: “Choi Minwoo is a diehard Baek fan. I’ll just watch the fun Gigant Rider instead.” Author’s Response: “?”]

The matter concerning Choi Minwoo received extensive coverage not only from the country’s four major daily newspapers, but also from foreign media.

The fact that nonsense was even spreading across web-fiction platforms showed just how great the shockwave had been.

A brief dispute over the truth did break out, but it quickly died down.

That was because Go Se-won, who knew Ares Guild’s internal affairs better than anyone, and Magic Johnson finally spoke.

[Former Head of Security Go Se-won: “Choi Minwoo’s Statement Is True. After Losing His Parents as a Child, He Was Shut Out from Ares Guild for More Than Twenty Years.”]

[American Grand Mage Magic Johnson: “He Is Certainly Cheon Taemin’s Maternal Grandson, and an Extremely Capable and Charming Man Who Has Grown the Peace Guild to Its Present State. By the Way, Where Is Kanghee Lee Now? Is He in the Shower?”]

[Former U.S. President Joseph Biden: “I Think That’s How It Was, If I Remember Correctly. No, Actually, I’m Not Sure.”]

[Prince Felix of the United Kingdom, After Hearing the News: “What The Fu*k…” Royal Household Directly Requests That the Interview Be Suspended.]

The final touch was the Blue House’s announcement and declaration of support confirming Choi Minwoo’s identity, followed by the results of Ares Guild’s official board meeting convened the next day.

[Ares Guild Elects Choi Minwoo, Current Peace Guild Master, as New Vice Guild Master. “The Board Vote Was Unanimous.”]

[The Young Power Broker Who Now Holds Both Major Guilds. Choi Minwoo.]

[Contrary to Expert Predictions That the Guild Association Would Resist: “Our Sincere Congratulations.”]

[And Yet the Immortal Hero Has Never Revealed Himself.]

[Overseas Reaction: “Where Is Slayer?”]

…

“Mr. Jin Taekyung?”

At the voice that pierced my ear, I lifted my gaze from the smartphone I had been staring at.

The face that appeared countless times in the articles was standing right in front of me.

Amid thunderous applause and enthusiastic support, he had become Ares Guild’s new captain. Now he asked with a calm expression:

“What are you looking at so intently?”

“Articles about Team Leader Choi. No, should I call you Guild Master now? Or Vice Guild Master? You’ve got one foot in each Guild, so it’s confusing.”

“Call me whatever you prefer.”

“Hmm. Should I? Minwoo?”

“Ah… Please just call me Guild Master Choi Minwoo.”

“That feels awkward. I’ll just keep calling you Team Leader.”

Considering the people’s gazes and the position he held, Guild Master would have been the proper title.

But Team Leader Choi couldn’t refuse my proposal.

It was a hundred times better than being called Minwoo.

“…Understood.”

Team Leader Choi answered with an uneasy expression and swept his gaze across the surroundings.

This was a vast, devastated area that had deliberately been left unrepaired so that the investigation could proceed properly.

The hidden Area A inside Ares Guild headquarters.

*Though I suppose I should call it the area that used to be hidden now.*

I crossed the familiar hallway while muttering inwardly.

This was where I had fought a fierce battle against the mutated Go Jun. As a result, every direction I looked and every path I followed was filled with wreckage.

*Damn, it’s huge.*

It wasn’t an orchard, but judging by eye, the place had to cover well over a thousand pyeong—more than 35,000 square feet.

The problem was that Team Leader Choi and I had to search the entire place with a fine-toothed comb.

No. Strictly speaking, there were three of us.

It was just that the other member wasn’t human.

“Come out, you bastard.”

Swoosh.

A human-shaped creature that was not human emerged from my inventory and muttered.

“Am I remembering this wrong? I’m pretty sure you said you were taking me to a club. You even promised drinking games with beautiful women.”

I answered the Skeleton King’s aggrieved expression with complete confidence.

“We’re going to play treasure hunt here.”

“…”

“If you find it quickly, I’ll really take you to a club. I swear on Hyuk Mujin’s balls.”

“…”

“You despicable human. I’ll trust you one last time. But who in the world is this Hyuk Mujin you keep wagering his balls?”

I casually ignored the Skeleton King’s question and gestured toward Team Leader Choi.

“You take that side. I’ll take this one. Bones, you handle over there.”

“Isn’t the area you assigned me rather large?”

“Team Leader, you’re hurting my feelings. If you don’t like it, quit. Is he our grandfather? He’s your grandfather.”

“That is immediately convincing. Understood.”

Once we finished dividing the work, we moved quickly.

Three hours later, we gathered in one place and muttered with grim expressions.

“Fuuuck… I can’t do this shit.”

“For some reason, the mana detector isn’t working. This is a genuine luxury item I bought at a Sotheby’s auction.”

“Human. Treasure hunt game is boring as hell.”

I had expected it to be difficult to find the secret area, considering Lee Jungryong’s meticulous personality.

But I had never imagined it would be this difficult.

There was a reason the government investigation team had returned empty-handed.

*There isn’t even a reaction in the office. Could the information have been wrong?*

But Go Se-won was the person closest to Ares Guild’s secrets.

Now that Lee Jungryong, Song Cheonwoo, and even Go Jun were dead, trusting his word was the only…

“Huh?”

A thought suddenly flashed through my mind, and my eyes widened without my realizing it.

Team Leader Choi, who had been pounding the mana detector with his fist, and the Skeleton King both asked:

“What is it?”

“Oh. Did you think of a club with a great crowd?”

“No, wait. I think I know where to look.”

I quickly retraced my memories of Area A.

The battle against Go Jun.

The first victory.

And then…

*When I came back.*

*He was running away.*

At the time, Go Jun had been fleeing in that horrible form—a creature made from a mixture of human and monster.

But the important question was where he had been heading.

*That’s it. There’s something there that I failed to find.*

Tap—whoosh!

Without another thought, I launched myself forward.

Team Leader Choi and the Skeleton King hurried after me as I shot ahead like the wind.

It was a place we had already searched several times.

But this time, something was different.

Swoosh.

There was a dead-end hallway and several rooms.

I slowed down and pressed myself against the wall, heightening my Qi Sense.

With a chime from the System, a blue circle spread outward from me.

But even after searching every corner of the hallway and rooms, no notification appeared to tell me that I had found anything.

Fwoooooosh.

The range of [Qi Sense] was determined by the System, and I could perceive only as far as that range allowed.

But was that truly all there was?

*Farther. Wider.*

I calmly regulated my breathing.

The sounds around me receded, and the internal energy rising from my dantian lent strength to my Qi Sense.

And then…

At the moment my Middle Dantian finally responded—

Fwoooooosh!

The blue circle that had stopped expanded outward.

Beyond the visible space, toward another space hidden in secret.

At the very edge of its reach was the notification I had been waiting for.

*Ding.*
## Chapter artifact 604

# Chapter 604

*Ding.*

> **System**
>
> - You have gained enlightenment regarding **Middle Dantian**!
> - **Middle Dantian** is partially activated!
> - **Middle Dantian** activation: 10%
> - The efficiency of all martial arts and internal energy has increased slightly, and you may occasionally exert strength beyond your limits!
> - You have achieved the rare Achievement **Waaah, I’m a Baby Middle Dantian**!
> - You have gained a large amount of EXP as an Achievement reward!
> - Level Up!

*Activated?*

I hadn’t expected this.

It had been more than a month since I opened my Middle Dantian, but I never imagined it would come with benefits like these.

And then, following the System notification announcing an unexpected reward, the news I had been waiting for arrived.

*Ding.*

> **System**
>
> - The range of **Qi Sense** is expanding!
> - The target cannot be identified precisely!
> - An unidentified, strange power is being sensed!

I had failed to identify the target, but this wasn’t a failure. It was a success.

Certain that something existed beyond this wall, I punched it without hesitation.

Boom!

As the solid wall exploded, empty space was revealed.

The hidden Area A on the top floor of Ares Guild headquarters was maintained by various barriers, invisibility magic, and gravity magic.

Naturally, the government investigation team must have known this as well.

The problem was that they had missed the most important thing.

*No. They couldn’t have helped missing it.*

I reached through the collapsed wall and stroked the empty air. It was literally empty—nothing could be felt. The mana detector in Team Leader Choi’s hand remained silent.

But I was certain. Something had to exist beyond this point.

Fwoosh.

Three jiazi of Scorching Yang Qi transformed into flame. I silently looked down at my hands, bluish-white flames flickering over them, then closed my eyes and reached out.

*What you see isn’t everything.*

This was a matter of perception. I had to see and feel with my instincts, my senses, and my heart—not my eyes.

I focused with all my might and poured out my internal energy without restraint. My faintly opened Middle Dantian responded.

The flickering flames gradually settled, completely enveloping my entire hand.

Compression. True Form.

And then…

Crack.

I gripped the flow of qi in my grasp and tore it apart with all my strength.

Shraaak!

The empty air split apart alongside the bluish-white flames.

All kinds of magic beyond my understanding were dispelled by Force, and a gap leading into a new space appeared.

The Skeleton King and Team Leader Choi stared blankly at the scene unfolding before them and muttered.

“He tore it.”

“No, how in the world did you…”

“When your body is bad, your head has to work harder. Let’s go.”

“…Isn’t it usually the other way around?”

“Usually, yes.”

*But I’m not ordinary.*

At my casual answer, Team Leader Choi threw the mana detector in his hand behind him.

Hmm. Having a good body really was the best.

* * *

It was a good thing we had cleared out the top floor in preparation for any unexpected situations.

Otherwise, we might have ended up live-streaming our entry into an unidentified subspace.

Swoosh.

When I stepped into the long vertical gap, a completely different world unfolded before me.

*What the hell is this?*

It was vast in every direction, with a high ceiling. It was also filled with a blend of unfamiliar elegance and extravagance.

Team Leader Choi and the Skeleton King entered behind me and immediately became too busy looking around to speak.

“That’s…”

Team Leader Choi’s eyes trembled faintly as he walked across the soft carpet covering the floor.

He slowly examined the paintings hanging along the vast corridor before muttering.

“Salvator Mundi.”

I asked in an offended voice.

“Did you just call me Mundi?”

“No. That’s the title of the painting. Salvator Mundi. It’s a masterpiece by Leonardo da Vinci. Have you really never heard of it?”

“I’ve heard that from my mom sometimes. Her hometown is in Gyeongsang-do.”[^1]

“…”

“What’s with that expression? Are you looking down on Gyeongsang-do right now? Team Leader Choi, are you one of those people with regional prejudice?”

“What? Regional prejudice?”

Team Leader Choi hadn’t said that. The Skeleton King, who had been looking around, suddenly butted in with an offended expression.

“Regional prejudice must be eliminated. In that spirit, this body, who hails from the Demon Realm, also agrees with the treacherous human’s opinion.”

“Look at this undead bastard trying to bone in on the conversation. Stay out of it.”

“No, this is pissing me off. Why are you cursing me when I’m helping you?”

“If we’re talking about the Demon Realm, that’s dimensional prejudice, you bastard. The way you talk, someone would think the Demon Realm was right next to Mount Jiri.”

“The Gate where I was active was in Bucheon. Of course, I’m from Atlanta, Georgia, in the United States.”

“Are you seriously insane?”

While I was arguing with the Skeleton King across dimensions and borders, Team Leader Choi—who had given up on our conversation early on—suddenly spoke up as he moved around the corridor, opening one closed door after another.

“Both of you, stop arguing and come over here.”

The Skeleton King answered with the stiff posture of a scholar.

“This body is the lord of the undead. I do not listen to the words of a human steeped in regional prejudice.”

“Follow me if you don’t want to get your ass kicked.”

I grabbed the collar of the idiot spouting nonsense and dragged him along.

The moment I followed Team Leader Choi’s gesture and looked inside the wide-open door, I understood why he had called me over.

“What is this…”

Even though not a single light was on, the room was as bright as day. The reason was the Magic Gems neatly arranged on the display shelves.

Even the lowest grade among them was A, and a rough visual estimate put their number at around five hundred.

*How much would all of this be worth in money?*

The value was astronomical—so high I couldn’t even begin to guess.

On top of that, the five S-grade Magic Gems emitting the brightest light from the top row were treasures that would be nearly impossible to obtain even for someone with money.

“So this is all…?”

As my voice trailed off, Team Leader Choi gave a small nod.

“Lee Jungryong definitely stole them. From what I’ve seen so far, the other rooms are the same.”

“This is fucking insane…”

“Not only Magic Gems, but also gold bars, diamonds, bonds, and other valuable assets. There are even countless works of art believed to have disappeared after the Great Cataclysm.”

Team Leader Choi was telling the truth. Every time we threw open one of the doors lining either side of the long corridor, treasures of immense value—or treasures too precious to put a price on—were revealed.

The calculator in my head had long since been smashed to pieces by the scale of it all.

*I had expected something like this to an extent… but he really took a hell of a lot.*

After the Great Cataclysm, the existence of Gates and Magic Gems had become the second Oil Money.[^2] No, they had become something even greater than that, giving the major Guilds enough wealth and influence to crush even powerful corporations.

Under those circumstances, everyone—including me—had assumed Lee Jungryong’s wealth would be enormous. But no one could have known there would be this much hidden wealth beyond what had already been uncovered.

*Vault.*

The word flashed through my mind.

Right. This was the private vault Lee Jungryong had built and passed down to Go Jun.

But there was one thing we couldn’t forget.

This place was both a vault concealing immense wealth and a prison.

*A prison meant to hide one person from the world.*

But the only two guards had already met their deaths, and the new owner of this space was walking toward the final door beside me.

Step. Step.

At the end of the long corridor, Team Leader Choi walked toward the tightly closed door. There was an unmistakable tremor in his steps.

“Hoo.”

He took a small, deep breath to calm himself, but I stepped forward without hesitation in his place.

I swung a hand blade down at the door, which radiated an enormous flow of mana. A streak of flame cut through the air.

Slice! Boom!

The various spells were dispelled, and the alloy door split apart to either side.

At the same time, darkness and bitter cold that had been crouching beyond it swept over us.

Whoooosh.

An inexplicable chill seized my entire body.

Even I, who had already reached the realm of Unaffected by Cold and Heat, shuddered. Even the Skeleton King, an existence born from death and cold, trembled.

But one person was the exception.

Step.

In the darkness, the sound of footsteps rang out unusually loudly.

There was no longer any tremor or hesitation in Team Leader Choi’s back as he walked forward without a word.

More than twenty years.

The child had become a boy, and the boy had become a young man.

The child who had lost his parents early had been separated from his maternal grandfather without understanding why. At last, he had returned to his rightful place and stood here.

To meet his only blood relative.

To confirm the truth.

“I missed you. I always have.”

Step.

His footsteps continued forward until, at some point, they suddenly stopped.

A large oval-shaped mechanical capsule, connected to countless wires, lay before him.

The machine looked like something out of a science-fiction movie. It appeared to be designed for hibernation—a coffin prepared for a living person.

Hoo.

In the chilly air, Team Leader Choi’s breath fogged the dust-covered glass.

His long fingers trembled faintly as they brushed the glass clean.

“I wanted to see you.”

As the dust was wiped away, a person’s face finally emerged. Unlike the photographs circulating online, the face looked old and exhausted.

But the old man looked so much like Team Leader Choi that it proved they shared the same blood.

In a quiet voice, Team Leader Choi continued speaking to him.

“Grandfather.”

* * *

Team Leader Choi kept everything top secret.

At least for the time being, no one besides the Skeleton King and me could know about this secret, and I wholeheartedly agreed with him.

Of course, there was one minor complication.

“Keeping a secret won’t be difficult. But I have two conditions.”

The Skeleton King recited his conditions with the determined expression of an independence activist.

“First, take me to a club. Second, give me one of the S-grade Magic Gems in there.”

Team Leader Choi readily accepted the first proposal, but the second was another matter.

As he considered it seriously, I offered a clear alternative.

“There is a better way.”

“What is it?”

“How many S-grade Magic Gems are there right now?”

“There are still five.”

“Then let’s beat that bastard up and make it six. We can keep the secret and secure an additional S-grade Magic Gem.”

“…!”

“…!”

The Skeleton King, who had demanded his terms with the spirit of an independence activist, became a pro-Japanese collaborator and cooperated, and we reached a dramatic compromise by agreeing to take him to a club.

But there was one crucial matter concerning Cheon Taemin’s future that we couldn’t solve on our own.

“We can’t keep my maternal grandfather here forever. We need to move him somewhere else.”

“The problem is that we have to move him without attracting anyone’s attention…”

That was something even a pocket enhanced with spatial expansion magic—or my inventory—couldn’t accomplish.

The Immortal Hero, Cheon Taemin, was most certainly still alive.

After much deliberation, only one answer remained.

“We have to move him using teleportation magic.”

The key was who that person would be.

Someone we could trust more than anyone else. Someone who wouldn’t reveal the secret even after learning it.

Someone sympathetic to both the unconscious Cheon Taemin and us, and able to keep helping us…

“One person comes to mind.”

“I believe I’m thinking of the same person as you, Mr. Jin.”

For that reason, I called someone.

“Can you come to Korea for a little while?”

—Hey, Jin. I’m busy too. There’s a mutated Gate right now—

“Team Leader Choi wants to see you. Kissing is absolutely on the table.”

—I'll come right now.

[^1]: “Mundi” sounds like *mundi*, a Gyeongsang dialect insult, which is why Taekyung misinterprets the painting’s title as a comment about him.

[^2]: “Oil money” refers to the immense wealth and influence generated by petroleum resources. Here, Taekyung is comparing the economic power of Gates and Magic Gems to—and beyond—that of oil-rich nations.

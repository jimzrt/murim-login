# Checkpoint Review — 275–279

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

# Chapters 275–279

## Plot

After Im Kkeokjeong’s attack, Jin Taekyung discovers a coordinated campaign linking the Black Hunters, a media smear operation blaming him for Won Myunghoon’s death, and apparent interference with the investigation. Butler Kim traces the attackers’ “tail” to Im Yeongjun, a Level 95 A-rank Hunter hiding a Black Hunter training base in the countryside.

Taekyung attacks the mansion alone. He kills many of the twenty-eight assembled Black Hunters, defeats Im Yeongjun, destroys the mansion’s defenses, and tortures Yeongjun for information. Yeongjun identifies Myeongdong Guild as his only significant connection. Taekyung spares ten surviving Black Hunters, who are removed before Butler Kim burns and conceals the site.

Myeongdong Guild Guild Master Park Tae Seop confronts Park Jihoon over Jihoon’s unauthorized killing of Team Leader Jung Hyunwoo and his involvement in the operation targeting Taekyung. Tae Seop reveals that the Guild secretly operates Team 11, roughly thirty trained Black Hunters. After Team 11 reports an intruder at its remote base and then loses contact, Taekyung visits Myeongdong Guild headquarters when Jihoon stops answering his calls. He forces his way inside, hears Jihoon receive a report that twenty-eight people were wiped out, and seizes the unnamed Team 1 Leader while confronting Jihoon through the phone.

## Continuity

- Im Kkeokjeong lost both arms below the elbows. Healing magic and advanced potions completed his treatment, but his return as a Hunter remains uncertain.
- The Black Hunter attack, media campaign, and investigation interference are part of an organized operation intended to isolate Taekyung and the Peace Guild.
- Im Yeongjun was a Level 95 A-rank Hunter who concealed a Black Hunter base in his countryside mansion. He survived Taekyung’s assault and was removed with nine other surviving Black Hunters.
- Taekyung learned from Im Yeongjun that Myeongdong Guild was his significant organizational connection. The mansion and remaining evidence were destroyed and concealed.
- Yeongjun confirmed that the attack on Kkeokjeong was ordered by an unnamed authority above him.
- Park Jihoon is a Myeongdong Guild Team 1 Hunter and covert enforcer. He killed Team Leader Jung Hyunwoo after detecting wrongdoing, without Tae Seop’s permission.
- Park Tae Seop is Myeongdong Guild’s Guild Master, a Great Cataclysm hero, and one of Korea’s top rankers. He accepted a proposal from an unidentified person who had personally contacted him.
- Myeongdong Guild publicly has ten teams but secretly operates Team 11, containing roughly thirty Black Hunters, including three A-rank and twenty-five B-rank Hunters.
- Team 11 reported “Intruder detected” from a remote unsafe-zone location, then lost contact. Taekyung is the apparent intruder and reported killer of twenty-eight members.
- Taekyung entered Myeongdong Guild headquarters after failing to reach Jihoon, overpowered two C-rank Security Team Hunters, and bluffed entry by proposing a cooperative raid.
- Myeongdong Guild’s twenty-story headquarters houses Team 1 on the nineteenth floor and the Guild Master and board on the twentieth.
- Kim Cheol Soo is a newly hired, regulation-bound C-rank Security Team Hunter.
- Taekyung has seized the unnamed Team 1 Leader and is speaking to Jihoon through the leader’s phone.
- Unresolved: the identity of the person directing the operation; the exact roles of Myeongdong Guild and Jihoon; what wrongdoing Jung Hyunwoo uncovered; who authorized the attack on Peace Guild’s D-rank Hunter; and whether Jihoon is acting against Taekyung or pursuing a separate objective.

## Translation Decisions

- Retain **Black Hunter**, **Myeongdong Guild**, **Team 11**, **Guild Master**, **Great Cataclysm**, and **unsafe zone**.
- Render **임영준** as **Im Yeongjun**, **박태섭** as **Park Tae Seop**, **박지훈** as **Park Jihoon**, **정현우** as **Jung Hyunwoo**, and **김철수** as **Kim Cheol Soo**.
- Render **꼬리** as the investigation’s **“tail”** designation.
- Render **침입자 발생** as **“Intruder detected.”**
- Render **유도리** as **yutori**, with the sense of leeway or flexibility.
- Render **세 얼간이** as **the Three Idiots**.
- Render **도사견** as **Tosa dogs** and **보신탕** as **dog-meat soup**.
- Preserve Taekyung’s graphic, dryly mocking voice and the distinction between the **Flame-Extinguishing Divine Fist** and **Heaven-Destroying Divine Fist**.

## Durable state

{
  "active_continuity": [
    "Taekyung defeated the Black Hunters at Im Yeongjun's countryside mansion and spared ten survivors.",
    "Im Yeongjun identified Myeongdong Guild as the significant connection behind the Black Hunter operation.",
    "Park Jihoon is a Team 1 Hunter and covert enforcer for Myeongdong Guild.",
    "Park Jihoon killed Team Leader Jung Hyunwoo after detecting wrongdoing without Park Tae Seop's permission.",
    "Park Tae Seop is the Guild Master of Myeongdong Guild and a top Korean ranker.",
    "Taekyung contacted the phone number saved for his former classmate Park Jihoon.",
    "Myeongdong Guild publicly has ten teams and secretly operates Team 11, composed of Black Hunters.",
    "Team 11 comprises roughly thirty Black Hunters, including three A-rank and twenty-five B-rank Hunters.",
    "Team 11 sent the message 'Intruder detected' from a remote unsafe-zone location and then lost contact.",
    "Park Jihoon said an unidentified person had personally contacted Park Tae Seop about the proposal that Tae Seop accepted.",
    "Taekyung went to Myeongdong Guild headquarters after failing to reach Jihoon by phone or find him at home.",
    "Taekyung gained entry by overpowering two C-rank Security Team Hunters and fabricating a cooperative-raid opportunity.",
    "Kim Cheol Soo is a newly hired C-rank Myeongdong Guild Security Team Hunter who is rigidly loyal to Guild regulations and company duty.",
    "Myeongdong Guild's twenty-story headquarters houses Team 1 on the nineteenth floor and the Guild Master and board on the twentieth.",
    "Taekyung recognized Jihoon's voice reporting that twenty-eight people had been wiped out and seized the unnamed Team 1 Leader while speaking to Jihoon through the phone."
  ],
  "continuity_sources": [
    279
  ],
  "open_questions": [
    "Who is the unidentified person directing the proposal and the Black Hunter operation?",
    "What happened to Team 11 after it reported the intruder, and who was the intruder?",
    "What exact role did Myeongdong Guild and Park Jihoon play in the operation targeting Taekyung and the Peace Guild?",
    "Is Park Jihoon acting as Taekyung's enemy or pursuing a separate objective?",
    "What wrongdoing did Jung Hyunwoo uncover before Park Jihoon killed him?",
    "Who authorized the Black Hunters to target the Peace Guild's D-rank Hunter?"
  ],
  "safe_through": 279,
  "temporary_decisions": [
    "Render 임영준 as Im Yeongjun.",
    "Render 블랙 헌터 as Black Hunter.",
    "Render 명동 길드 as Myeongdong Guild.",
    "Render 박태섭 as Park Tae Seop.",
    "Render 정현우 as Jung Hyunwoo.",
    "Render 한남동 as Hannam-dong.",
    "Render 11팀 as Team 11.",
    "Render 침입자 발생 as Intruder detected."
  ],
  "version": 1
}

## Reading copies

## Chapter artifact 275

# Chapter 275

*You’re naive.*

That one sentence I’d heard the day before wouldn’t leave my mind.

I sat in the caregiver’s chair beside the bed, staring blankly at the humidifier spraying mist. Then a thought suddenly occurred to me, and I said it aloud.

“No. It wasn’t naivety.”

Murim was a world that lived up to the phrase *a mountain of blades and a forest of swords*.

Bloodshed was commonplace, and death was part of daily life. Might made right, and the survivors were the winners.

Whenever I witnessed the cruel side of Murim, I thought of the modern world.

An organized welfare system and laws. People’s sense of ethics. A civilization incomparably more advanced than Murim.

But I had been wrong.

“It wasn’t that I was naive. I was just stupid.”

Murim people wore swords at their waists, but modern people hid daggers up their sleeves.

Monsters weren’t confined to Gates. They existed outside them, too.

People who wrapped themselves in expensive clothes and wholesome images before ruling over the concrete jungle. The moment those bastards began drawing the daggers hidden in their sleeves, they became the monsters outside the Gates.

*Like Won Myunghoon.*

I had been thinking too softly about things. Even though I knew the world was unfair and fucked-up, I hadn’t been able to let go of my complacency.

*This is the modern world. A democratic society in the twenty-first century.*

There might be a vicious struggle to prove one’s abilities, but I had believed something like today’s incident couldn’t happen.

*And this is what that got me.*

I stared at Im Kkeokjeong sleeping on the bed. Both arms, severed below the elbows, had been treated with recovery magic from a high-ranking healer and advanced potions.

He probably wouldn’t have much trouble with daily life, but I couldn’t guarantee his return as a Hunter. Potions weren’t a cure-all.

*Which bastard was behind this?*

Various thoughts swam through my cold mind.

Who had sent the Black Hunters, and why? What was their purpose?

Cutting off Im Kkeokjeong’s arms could have been a warning to stop here. Or it could have been the signal announcing the beginning.

*I’ll find out what they meant soon enough.*

Until then, I had no intention of sitting around and waiting.

Neither did Team Leader Choi.

“Get some rest, Uncle.”

I had just pulled the disordered blanket over Im Kkeokjeong when—

Bzzzz.

Along with the vibration, a smartphone lit up the darkness.

It was a short text message from Team Leader Choi.

> **Team Leader Choi:** To the Guild House.

* * *

I left the hospital as soon as I read the message. It was deep into the night, and two people were waiting for me at the Guild House, where everyone else had already gone home.

“Ah, Mr. Jin Taekyung.”

“Welcome.”

Team Leader Choi and Song Song.

Butler Kim, whom I had naturally expected to be there, was nowhere to be seen.

Team Leader Choi noticed my gaze and spoke first.

“He’s stepped away for a moment.”

“Really?”

It was unusual to see Butler Kim absent from Team Leader Choi’s side, where he had always stood like a shadow. But that wasn’t important right now.

I skipped straight to the point.

“What happened?”

“I should offer you a cup of coffee before I explain, but… Take a look at this first.”

Instead of a coffee cup, Team Leader Choi held out his smartphone. The screen displayed the country’s largest online portal.

His long finger tapped an internet article, and a stream of articles divided into different categories appeared.

Among them, I skimmed the article at the very top.



> [The Judiciary Bows Before the Fame the Public Has Created. Where Is the Fairness?]
>
> [United Party Supreme Council Member Assemblywoman Yoon Seoyoon: “A Death Brought About by One Individual’s Rash Actions. Won Myunghoon Should Have Faced the Judgment of the Law.” Strong Condemnation…]
>
> [Self-Defense or Murder?]

Articles filling the politics and society sections. They didn’t include my name, but it was obvious who they were talking about.

“When was this posted?”

“An hour ago. And it already has over a hundred thousand views and more than five thousand comments.”

“An hour ago? That would’ve been around four in the morning.”

“Apparently, netizens are more diligent than we thought. Or should I say the paid commenters?”

“Interesting.”

Team Leader Choi took a sip of coffee that had gone as cold as the smile on my lips.

“There’s an even more interesting article.”

“More interesting than this?”

“Scroll down a little. It’ll be more than you expected, Taekyung.”

He was right. My finger stopped moving before I realized it.

I stared silently at the headline in bold.



> [Exclusive Interview with Former Colleague K to Be Released Early: “Famous Hunter J Is an Ugly Human Being.”]

When I tapped the article, a preview video of an interview lasting just over three minutes appeared. After a fifteen-second advertisement for a luxury cosmetics brand, the screen filled with the image of a potbellied man in a carefully tailored suit.

There was a small amount of mosaic blurring over his face, but I recognized him at a glance.

“Ha.”

When I realized the identity of the middle-aged man—or rather, “former colleague K”—a hollow laugh escaped me.

It was an all-too-familiar face. Someone I had thought I would never see again was right there on the screen.

“I didn’t expect to see him again like this.”

Song Song, who had been looking at the phone over my shoulder, asked,

“You really know him?”

“Of course. How could I not?”

“If things were bad enough for him to give this shitty interview, you obviously didn’t get along.”

“No.”

“Then were you close?”

“It’s not that…”

What word could describe the relationship between that man and me? I thought about it carefully before opening my mouth.

“It was fucking awful.”

“Oh.”

No matter how I thought about it, those words fit perfectly.

Our relationship had been that terrible. Considering everything we had been through together, it was almost strange that we had never crossed blades.

I stared at the face that had somehow grown even fatter since the last time I’d seen him.

*Mr. Common Sense. Long time no see.*

Kim Sangshik, Team Leader of the Sopung Guild.

When I had been an F-rank Hunter, he had been the one who goaded the Guild Master into firing me.

The last time I’d seen him was when I ran into him at the Association while going through a Grade reassessment. And now, I was seeing him again like this.

*I heard he was fired from the Guild afterward.*

Kim Sangshik was a man with no ability and endless greed. Despite his name, he lacked common sense, too, and had been fired after committing every kind of idiotic blunder imaginable.

He was practically the very definition of a petty little man, so it was obvious that he had been grinding his teeth at me ever since.

That was probably why he had even filmed an interview like this.

*Let’s hear what kind of bullshit he’s spouting.*

As it happened, the reporter’s questions began playing on the video.

“‘I hear you have something to say about the recently famous Hunter J. First of all, is it true that you were his former colleague?’”

Kim Sangshik nodded with an unusually serious expression.

“‘That is absolutely true. I was Jin Tae… No, J’s immediate supervisor.’”

“‘More precisely?’”

“‘He was a member of my team. I became team leader after the Gate accident two years ago. I was also the one who notified J of his dismissal this summer.’”

“‘Oh dear. Was there a reason?’”

“‘There wasn’t just one reason.’”

After that, Kim Sangshik launched into an indignant tirade about why he had fired me.

Every single excuse was a gem of bullshit, but his final exchange with the reporter was the crowning touch.

“‘I was falsely accused of employment corruption and driven out of the Guild where I had worked for more than twenty years. But I did not fire J for any personal gain.’”

“‘Are you saying there was another reason?’”

“‘Yes.’”

There had been a reason they had released only a three-minute preview. Kim Sangshik ended it with the solemn expression of a martyr for the nation.

“‘During the mutated Gate accident two years ago, J threw his teammates to the monsters as prey and fled. He is the kind of man who won’t hesitate to do any ugly and dirty thing to survive…’”

I couldn’t properly hear what came after that.

Even after the video ended with a caption promising that the full interview would be released soon, I continued staring at the screen in silence.

As if Kim Sangshik might leap out of it if I kept watching long enough.

Team Leader Choi broke the heavy silence.

“How did you find it?”

Ah, how did I find it?

Well. The back of my head felt numb, and part of me wanted to laugh. At the same time, my lower stomach was boiling.

“It’s very interesting. Just like you said, Team Leader.”

“I laughed when I first saw it, too. I know roughly what kind of person the K in the interview is—or rather, the man named Kim Sangshik. The problem is…”

“The public won’t find it very funny.”

“Exactly.”

The comments section was already on the verge of exploding.

There were more than ten thousand comments now, and I didn’t need to read them all. One of the most upvoted comments caught my eye.

> **(Best comment)** I knew this was coming. I heard it across the bridge[^1] and thought, *No way,* but I had a feeling it would blow up someday.
>
> [^1]: A Korean expression meaning the information was heard indirectly.

*What bridge? And what the hell is supposed to blow up?*

I didn’t know what kind of asshole had written it, but it was a relief he wasn’t standing in front of me.

If he had been, I would have made sure that at the very least, he heard the next rumor from the overpass to the Yellow Springs.

“Well, I don’t think there’s any need to read more.”

I closed the comments with a hollow laugh.

Team Leader Choi took back his smartphone, folded his arms loosely, and spoke.

“This is organized. It’s clear now that sending the Black Hunters was part of the plan from the beginning.”

“And they’re the ones creating the hostile public opinion, too.”

“That’s how people are. Once someone really starts muddying the waters, it’s hard for people to keep their bearings.”

“And I doubt there will be even a single line in the news about Uncle Kkeokjeong being attacked in the middle of all this.”

“You understand the situation well.”

“If I didn’t, I’d be a fucking idiot. Did the investigation team handling the case say anything?”

Team Leader Choi slowly shook his head.

“Don’t tell me they’re in on it, too.”

“There seems to be outside pressure. The CCTV footage is in the other side’s hands, too.”

“Didn’t you say there were witnesses?”

“We’ve lost contact with all three.”

“That’s just fantastic.”

A sound like bones shifting out of place came from my clenched fist, which had tightened without me realizing it.

“They’re really coming at us with a plan.”

“They seem intent on isolating you completely. The interview with Mr. Kim Sangshik is part of that.”

We weren’t dealing with some Third Rate media company that sold gossip.

This was one of the country’s ten largest major media outlets.

They would wrap even the most ludicrous bullshit in attractive packaging and broadcast it convincingly. Along the way, they would use money and power to bolster its credibility.

For example… testimony from people who knew me well.

“We’ll get to see the faces of my old coworkers again. Though I guess it’ll be hard to recognize them if they’re shown with their faces mosaicked.”

I asked Team Leader Choi, who was looking at me with an unreadable expression,

“Why are you looking at me like that?”

“As I recall, Jin Taekyung had a good reputation within the Sopung Guild.”

“I got along with everyone. It was such a dinky little Guild.”

“Then why did you think that?”

“Because there’s one thing that works on everyone. This. And this.”

I brought my thumb and index finger together and wiggled them.

In the end, it came down to money. Money was everything.

For Hunters who were willing to risk their lives to make money, the temptation would be even stronger.

“Maybe it’s because I’ve been blindsided so many times in a row, but… These were people I’d spent seven years laughing and joking around with. And I still can’t trust them.”

If this had happened a few days ago, I might have naively believed in my old coworkers.

But not now. The world where dreams, friendship, and common sense meant anything had already vanished from my mind.

“Looking at how the article made it into the politics and society section, it seems like they greased some lawmaker’s palm, too. You think they couldn’t buy off a few low-rank Hunters who are struggling to make ends meet?”

“…”

“It’s obvious. I’ll become the worst bastard alive, get carved up all over the internet, and be torn apart. The image I’ve built up until now will come crashing down, and our Guild will come crashing down with it.”

Team Leader Choi, who had been wearing a strange expression the entire time, let out a quiet laugh.

“You’ve improved a little. You can think like a jaded adult now.”

“Are you taking back what you said yesterday about me being naive?”

“I’ll decide after I see what you do from this point on.”

“What?”

“We can’t just stand there and let them do this to us.”

As he spoke, his finger pressed the screen of his smartphone. A ringing tone sounded, and someone answered.

“I found it. The tail.”

Butler Kim’s low, smooth voice flowed through the speaker.
## Chapter artifact 276

# Chapter 276

The middle-aged man was an ordinary neighborhood uncle, the kind you could see anywhere.

A bluish stubble shadow ran from his sideburns to his chin. His hiking clothes, chosen with practicality in mind, bulged around his belly.

At the crack of dawn, he finished stretching with sleepiness dripping from his eyes, then began jogging slowly along the path between the rice paddies.

“One-two, one-two,” he went, adding the hearty rhythmic sounds unique to middle-aged uncles.

He was the “tail” Butler Kim had found.

“Is this the man?”

Inside an utterly ordinary minivan, Song Song muttered doubtfully as she watched the footage Butler Kim had recorded with magic.

“He looks ordinary.”

“Wouldn’t it be stranger if he looked extraordinary? A Black Hunter doesn’t exactly look like a ninth-grade civil servant.[^1]”

“Even so, that uncle looks too ordinary. Is there something only combat Hunters can recognize?”

“There is.”

I stared intently at the middle-aged man as he finished his jog and entered the mansion.

All I was looking at was a recording, so I couldn’t sense his internal energy. But no matter how talented an actor was, they were bound to reveal themselves through some minute movement.

And I had the insight to see through an act.

“A Peak master…”

“Hm?”

Song Song wasn’t the only one to react to my mutter.

Team Leader Choi and Butler Kim looked at me as if asking what I meant, so I continued.

“…I mean, an A-rank Hunter.”

“You seemed to say something else. Did you say ‘Peak master’?”

“Nope. You must have misheard.”

When something like this happened, the only answer was to build an impenetrable wall. If I said I hadn’t said it, what could they do?

Their doubtful looks lasted only a moment before Team Leader Choi and Butler Kim nodded as though they agreed with my assessment.

“I agree that he is an A-rank Hunter.”

“From what I observed, he is a fairly high-level expert even among A-rank Hunters. I had no choice but to keep my distance because I thought he might detect the surveillance magic.”

I could understand Butler Kim’s assessment. He was a battle-hardened veteran of the Great Cataclysm and had watched the man himself.

But Team Leader Choi’s insight was far sharper than I’d expected.

This wasn’t something just anyone could recognize.

*Well, that isn’t important right now.*

I asked about the thing I was most curious about.

“But how did you find him? I heard the investigation team had collected all the nearby CCTV footage.”

“We went and retrieved it again.”

No, I mean how did you do that?

Before I could ask, Team Leader Choi pressed his thumb and index finger together, forming a circle.

“You said this worked on all kinds of things, Taekyung.”

“Ah…”

“It is an immutable truth. I’ve used the method myself for a long time.”

So he had slipped a bribe to someone on the investigation team.

Considering Team Leader Choi’s generosity, whoever it was must have made quite a haul.

“Didn’t you say there was outside pressure?”

“When there is outside pressure, you give them enough money to withstand it.”

That was impressive.

But from what he said next, even money had its limits.

“It appears that someone fairly powerful has gotten involved. Normally, they should have started talking readily enough, but perhaps out of fear, they refused to open their mouths no matter how much money we fed them. The CCTV footage was our best option.”

“And that man was caught on it?”

“Yes. There were slight discrepancies, possibly because he used an artifact enchanted with Illusion magic, but there is no doubt.”

I had expected something like this to a certain extent, but it seemed the people pulling the strings held considerable power.

They had greased the palm of a supreme council member from a political party and manipulated public opinion online as easily as breathing. Even the police and prosecutors—corrupt enough to accept bribes—were afraid to make a move.

*It has to be one of the major Guilds.*

A major Guild ranked among the top twenty could do this. They were no different from corporate giants standing tall under the name of a Guild.

They had even cultivated an illegal private army of Black Hunters. They had clearly crossed every line.

“So what does that bastard do?”

“He’s an urbanite who fulfilled his dream of moving to the countryside and farming.”

Butler Kim added a smooth comment as he handed me a tablet.

“On the surface.”

The tablet contained everything about the “tail.”

He was now in his mid-forties. He had accumulated a considerable fortune through stocks more than a decade ago, but after repeatedly collapsing because of a chronic illness, he had decided to move to the countryside.

“A chronic illness?”

“There are hospital records, too.”

What kind of chronic illness could an A-rank Hunter have?

I gave a short laugh as I flipped through the medical records.

“I’ll bet my left wrist that all of this is bullshit.”

Team Leader Choi nodded as though it were obvious.

“Then I’ll bet Jin Taekyung’s right wrist.”

“…”

Was this guy insane? Why was he betting my wrists?

Team Leader Choi casually ignored my incredulous stare and continued.

“In any case, on the surface, he is a perfect ordinary citizen. Apparently, he was sociable from the day he first settled there. He held a village feast once every two weeks, so the villagers stopped treating him like an outsider a long time ago.”

“No one is suspicious of him in a remote mountain village?”

“He’s a rich, good-natured man.”

“It’s the perfect place to hide and do things. For example, train Black Hunters.”

I examined the final image closely.

A picturesque two-story detached house. The house itself looked relatively small compared to the spacious yard.

A luxury SUV and a sedan were parked beside the gray stone wall.

*How many people are inside?*

The men who attacked Im Kkeokjeong numbered three. There was no reason for them to scatter one by one like the Dragon Balls, so I had to assume they were inside that house.

Ah, wait. Hold on.

“You said earlier that he held a village feast once every two weeks.”

“Yes. He orders large quantities of food from outside every time, but… Ah!”

The village feasts were probably a cover for procuring food and supplies.

*There might be quite a few more of them than I thought.*

Did he keep the rest crammed into a basement for training?

Or were they somewhere in the dense forest surrounding the house?

It was a personal preference, but I hoped they were all huddled together in the basement.

It would make things easier.

“Approaching carelessly could backfire. So let’s call it a day for—”

“Yes. Let’s slowly get started.”

I pulled my hood low and opened the car door.

“I’ll be back.”

“Pardon?”

“The three of you come in twenty minutes. It should be mostly over by then.”

All three of them shot me bewildered looks.

Butler Kim, the most experienced among them, spoke first.

“Hunter Jin Taekyung. There is nothing more frightening than an enemy whose capabilities you have not assessed.”

“Yes. I know.”

“I understand that your skills are exceptional, but…”

Butler Kim continued in a grave voice.

“I mean that dozens of A-rank Hunters like the one I observed could be waiting for you.”

“It’s fine. If anything, the Three Idiots looked stronger than that guy.”

“…”

“Don’t worry about it. He just reminded me of some people I know.”

Song Song asked in disbelief,

“You’re thinking about acquaintances at a time like this?”

“No. I’m always thinking about you.”

“Eek.”

“Be quiet before I punish you with a confession.”

“Aah!”

*Whew. I’m fucking cool. No wonder women run screaming.*

I was about to step out of the minivan after chalking up another easy win when Team Leader Choi spoke.

“I want to stop you, but I can’t.”

His expression was too strange to describe.

“Every crazy thing you’ve done has always succeeded.”

“You really know me. Then move exactly as I said. It’ll all be over within an hour at most.”

“Black Hunters… Those men have been trained to hunt humans, not monsters. Be careful.”

I couldn’t hold back a short laugh.

“Good. That happens to be my specialty, too.”

“Pardon?”

I left the wide-eyed Team Leader Choi behind and stepped outside.

Under the rural night sky, scattered with countless stars, I drew the cool wind deep into my lungs and stretched.

As I walked toward the Black Hunters’ base, shrouded in darkness in the distance, I was no longer Hunter Jin Taekyung.

I had become Jin Taekyung, a man of Murim.

* * *

Grrrrr.

A beast’s eyes flashed in the pitch-black darkness.

I sent killing intent toward the two Tosa dogs baring their teeth at me from behind the iron bars.

“If I hear you bark, you’re becoming dog-meat soup.”

Unless the dogs attended a Korean language academy, there was no way they could understand me.

But killing intent was another matter.

Refined through countless battles and encounters with death, killing intent awakened a primitive fear.

Even a person with exceptional nerve could wet themselves from it. Dogs, which were even more sensitive to such things, were no exception.

Whine. Whimper.

The Tosa dogs sensed my killing intent, hid their teeth, tucked their tails beneath their bellies, and flattened themselves against the ground. Their eyes shook anxiously, unable to look in my direction.

“That’s right. Good dogs.”

Slice.

The moment I sliced through the iron bars with qi condensed around my hand and stepped into the yard, a blaring siren rang out as I felt as though I’d passed through a soft membrane.

Wheeeeeeeeng!

Ding.

> **System**
>
> **Alarm Magic** has activated!
>
> **Sound-Blocking Magic** has activated! No noise will leak outside the mansion!
>
> **Vision-Blocking Magic** has activated! The scene inside cannot be seen from outside!

They had taken some precautions.

Even better.

The instant the magic activated, the lights inside the mansion blazed to life.

I sensed dozens of people moving hurriedly inside. Then the iron front door burst outward as though it had exploded.

Bang!

Five men emerged first. The “tail” stood at the center of them.

The eyes of the ordinary-looking middle-aged man had changed into those of a killer.

> **System**
>
> **Lv. 95 Im Yeongjun**

“You…”

His face twisted, and his eyes shook. There was no doubt he had recognized me.

I gave him a broad smile.

“I’m with the village youth association.”

“Jin Taekyung!”

“Nope. This is Patrick.”

“How did you find this place?”

“We have a rich young master in our Guild. He’s good at pulling strings.”

Im Yeongjun sharply swept his gaze around.

“Don’t tell me you came alone?”

“If I did?”

“Looks like you did.”

The corners of his mouth twisted.

“Fucking idiot. Even if you don’t know how the world works, there should be a limit.”

“That’s what I wanted to say to you. You should’ve picked your target more carefully.”

“That D-rank pipsqueak who doesn’t even look like a Hunter? Did they put his arms back on?”

“They did, but… Apparently, he has some lingering aftereffects. So I came to collect a little compensation.”

“I was going to kill him, but I held back. Be grateful that it ended there. If you don’t want to suffer something worse, lie flat and quiet as a dead mouse.”

“I’ve already seen something worse, and lying flat like a dead mouse isn’t my style. I’m not particularly grateful, either, so isn’t that why I came here?”

Im Yeongjun gave a short laugh.

“Kid, I know you’re excited because people around you treat you like a big shot, but don’t make the mistake of thinking we’re ordinary Hunters.”

Just as he said, the aura and killing intent emanating from the Black Hunters were far denser and stronger than those of ordinary Hunters.

I slowly swept my gaze across the mansion.

I could feel them—the presences hiding inside and waiting for orders.

“One, five, ten… Twenty-eight in all. You rounded up quite a crowd.”

“…”

“How?”

“I’m not an ordinary Hunter, either.”

I looked at his face as it hardened and continued.

“Three. Hand over the three who took part in the attack two days ago, including you. Disarm the rest and tell me everything you know. Then I’ll spare your lives.”

“You crazy bastard.”

“Good. I was worried you might accept.”

That had been my first and last offer.

There would be no next time.

*Open Inventory. Equip White Flame.*

The moment the cool spear shaft filled my grasp, Im Yeongjun shouted, his voice rising almost to a scream.

“Kill him!”

Those words were the signal.

Dozens of Black Hunters, who had been holding their breath while waiting for orders, smashed through the walls and windows and surged toward me.

Crash! Shhhhk!

An endless rain of blades and arrowheads poured in from every direction.

My eyes had already gone cold as I watched them.

“You picked the wrong person to mess with.”

Fwoooosh!

[^1]: In South Korea, grade 9 is the entry-level rank for civil servants.
## Chapter artifact 277

# Chapter 277

An endless rain of blades and arrowheads poured in from every direction.

I didn’t need to think about how to move. A picture formed naturally in my mind, and my hands moved at the same time as my thoughts.

Fwoosh!

Blue flames wrapped around the spearhead and traced a semicircle.

KRAAASH!

The arrows and weapons caught in its path split apart like tofu.

Ten-Thousand-Year Cold Iron was hard and sharp enough to destroy Body-Protecting Qi on its own. Once Spear Energy was added to the mix, the result was obvious.

Though perhaps not to them.

“Gasp!”

The Black Hunter closest to me let out a hollow gasp as he stared at his sword, which had melted under the Fire Gate Divine Technique’s flames.

He was my first target.

Crack!

My grip could crush stone and rebar. When I tightened my fingers around his forearm, his flesh was mangled and his bone burst through.

“Gyaaaaaah!”

I had memorized the descriptions of the men who had attacked Im Kkeokjeong. I stared intently at the Black Hunter’s face as he screamed in agony.

“You’re not one of them.”

“Die!”

A dagger shot up beneath my chin with a venomous cry. Even in the middle of his pain, he didn’t hesitate in the slightest.

This wasn’t the movement of someone in a raid.

It was the movement of a skilled killer.

*I tried to reason with people like these.*

I reflected on it once again.

*I really was a fucking idiot.*

I let out a hollow laugh and dodged the dagger. At the same time, I seized his other arm and pulled with all my strength.

No, I tore it off.

Crack-crack-crack!

“Urrrrgh…!”

His mouth stretched wide, but the pain was so great that he couldn’t even scream.

I kicked the man in the back as his limbs trembled violently. Along with his breath, which came in gasps that sounded ready to break, blood gushed from the torn stumps.

I tossed the two arms separated from their owner’s body onto the lawn.

“One down.”

“……!”

“……!”

A heavy silence descended over the area.

The Black Hunters hesitated after watching one of their companions, someone around their level, get taken down in an instant. Im Yeongjun, who had been watching everything from behind them, twitched his eyebrows.

“So you had something to rely on.”

“Yeah. That’s why I came. But it doesn’t look like you have anything.”

“You fucking bastard, Jin Taekyung…”

“You should’ve listened while I was asking nicely. Because of you and the other two, this guy can’t even jerk off by himself anymore.”

I swept my gaze around in a dry voice. Every time my eyes passed over someone, a wave of emotions rippled through them—anger mixed with confusion.

Im Yeongjun read the atmosphere and shouted furiously.

“What are you waiting for, you bastards?! I’ll save every one of you, even if I have to shower you in potions! Don’t be scared—beat him to death!”

I blinked. For a moment, I wondered if I had heard him correctly.

Ah, right. Potions.

“If someone loses both arms, you’d need high-grade potions at the very least. You must have a lot of money.”

“If you think of it as the cost of removing a major obstacle, it isn’t wasteful. We should have eliminated you from the beginning, but… I didn’t like the order from the moment I received it.”

“Isn’t it a bad idea to blab so openly about having someone powerful behind you? Won’t they kill you to silence you?”

“Kill me to silence me?”

A sneer formed at the corners of Im Yeongjun’s mouth.

“We’re the ones who kill people to silence them. And either way, you’re going to die here.”

“Sure, let’s put that aside for now. There’s something I’ve been wondering about.”

I asked sincerely,

“That potion you use—can it bring dead people back to life, too? Or do you carry three or four extra lives around with you?”

“What?”

Slice!

The spear answered in his place. The Black Hunter groaning at my feet lost his head.

I casually kicked the head separated from his body and sent it rolling toward the others.

“Try saving him.”

“……!”

“Right. If someone’s heart bursts or their head comes off, even a potion can’t bring them back.”

Shhk!

Without hesitation, I flicked my hand.

The two daggers shot out at a terrifying speed and became flashes of light.

Thwack!

Two Black Hunters staggered, then collapsed.

Unable to withstand the internal energy carried by the daggers, half of each corpse’s head had been blown away.

“Ah. I was trying to plant them neatly between their eyebrows, but I couldn’t control my strength.”

“……!”

The air around us seemed to vibrate.

The sneer had vanished completely from Im Yeongjun’s lips. A tempest now raged in the eyes of the Black Hunters, whose number had been reduced to twenty-five.

“H-How?”

“Goddamn it…”

Suppressed groans rose from here and there. It was something they had never experienced before.

Hunters hunted monsters.

Black Hunters had been created to hunt those Hunters.

Murder, kidnapping, blackmail, and every other filthy task—they had served as the enforcers of a major Guild.

But they had clearly never imagined being hunted themselves.

They certainly hadn’t imagined being hunted so one-sidedly.

I spat phlegm onto the headless corpse.

“You bastards are like dark-path knife fighters.”

No. In terms of their mindset, dark-path knife fighters were actually better.

At least those men were prepared for the possibility that they might someday be stabbed to death in a back alley.

“What… exactly are you?”

His voice was dry, as though all the moisture had been sucked out of it.

I grinned at Im Yeongjun as he stared at me.

“You already know, so why ask?”

His gaze sank coldly.

“You deceived everyone perfectly. You’ve never killed just once or twice in your life.”

“Killing beasts doesn’t count as murder. People usually call it slaughter.”

Step. Step.

Every time I advanced slowly, the Black Hunters surrounding me in a semicircle took a step backward.

Even the dullest among them must have realized by now that I wasn’t simply an A-rank Hunter.

They could feel the qualitatively different killing intent and the thick scent of blood clinging to me.

“Jin Taekyung.”

Im Yeongjun spoke with a stiff face.

“Taking out that D-rank Hunter was a warning. It was an order from above.”

“I didn’t like the way you delivered that warning. Not one bit.”

“I understand what you mean. Stop here.”

“And if I don’t?”

“The next one could be worse.”

“Worse?”

“Are you not worried about your mother and younger sibling?”

“……!”

For a moment, I couldn’t speak.

My steady approach finally stopped, and Im Yeongjun’s voice gained strength.

“I can negotiate with the people above us. I’ll serve as the stepping stone.”

“A stepping stone…”

“You only have to give up one thing. Don’t live as A-rank Hunter Jin Taekyung. Live as a civilian named Jin Taekyung. Of course, you’ll be compensated generously for it.”

I gazed silently into Im Yeongjun’s eyes.

There was wariness of me in them. At the same time, they were the eyes of a wolf constantly watching for an opening.

After a brief silence, a dry voice escaped my lips.

“A stepping stone. That sounds good.”

The corners of Im Yeongjun’s mouth began to rise slightly. I continued smoothly.

“Since you’re a stepping stone, I can just step lightly on you and pass over. I’ll find out who’s on the other side of the stream when I get there.”

“……!”

There would be no compromise.

They had crossed the line and had already become my enemies.

I placed the modern way and the way of Murim on opposite sides of a scale and agonized over the choice until the very end.

But today, I would choose the latter.

“And you, asshole. When you make an offer like that, you should at least say it with eyes that look trustworthy.”

“Jin Taekyung!”

I heard his shout as I kicked off the ground.

The Black Hunters charged toward me with gritted teeth, and I brought my spear down at them.

Slice!

* * *

Boom!

A single punch infused with three-tenths of my internal energy.

The enhancement magic shattered, and the Tower Shield broke apart.

The tank hiding behind it stared at me in shock.

Thrust!

White Flame’s spearhead pierced through his chest and burst out the other side.

The mage behind the sturdy shield hurriedly stepped backward.

Thwack!

I flicked my hand, and a dagger buried itself in the back of his head.

But it wasn’t over yet.

“Die!”

Shhhhhk!

Neck, chest, shoulder.

Three blades rushed toward me with a fierce sound of splitting air. The faint Sword Energy gathering around them made it clear that they were A-rank Hunters.

Slice!

I pulled the spear from the dead tank’s chest and swung it.

At that lightning-fast speed, all three swords shattered, and one of the men collapsed while clutching his throat.

As blood sprayed around me like a fountain, I released the spear.

I thrust both palms toward the two men trying to cut me down with their broken swords.

Crack—BOOM!

Compressed air exploded outward.

The men struck in the chest by the Flame Divine Palm knelt as blood poured from their seven openings.

Their melted magical armor clung to their upper bodies and burned their flesh, but they were already dead before they had time to feel the pain.

“Goodbye.”

I had just wiped the blood from my face with my sleeve when—

Shhk! Shhhhhk!

I tilted my head slightly.

An iron arrow thick and heavy enough to be called a small spear flew past me and embedded itself in the stone wall behind me.

Boom!

A cloud of dirt shot into the air as the arrow drove deep into the solid rock.

It had tremendous power.

*They’ve been irritating me for a while.*

These men also had the same basic positions as ordinary Hunters.

They had tanks and mages, as well as melee damage dealers. Naturally, they couldn’t leave out ranged damage dealers.

Three archers had never left the mansion. They had been constantly drawing their bows from the second-floor windows.

Shhk-shhk-shhk!

I clicked my tongue and was about to knock the arrow away with the shaft when the air wavered.

A black silhouette suddenly sprang out of it and tried to split my crown in two.

Shrrrkk!

Fast and precise.

He was clearly a melee damage dealer with an excellent stealth-type Skill.

How many people had he killed with this tactic?

I didn’t know, but one thing was certain.

*Today, he picked the wrong person.*

Bang-bang-bang!

I deftly twisted the spearhead.

The iron arrows, which should have been swept aside like fallen leaves, changed course and pierced the Black Hunter who had been trying to bury a dagger in my crown.

Thwack-thwack-thwack!

“Urgh!”

Struck by arrows out of nowhere in midair, the Black Hunter fell with a heavy thud.

I pulled the iron arrows from his upper body. His body shuddered, then went still. At the same time, I flung the arrows hard in the direction they had come from.

Shhhhhk! Thwack!

The iron arrows infused with internal energy did their job perfectly.

They flew back toward their original owners twice as fast and twice as powerfully as when they had first been fired.

The three archers, who had been nocking their next arrows, met death almost simultaneously.

“This is fucking insane…”

The men who had been about to charge stopped when they saw the scene. I could see their hands trembling around their weapons.

They had just watched more than ten of their comrades die before they could even blink.

But I had no intention of stopping.

Shrrrkk! Slice!

I charged straight at them, cutting, stabbing, and smashing.

A mist of blood formed, and someone’s arms, legs, or head flew in every direction.

“Gyaaaaaah!”

“Argh!”

Screams erupted from all around.

Amid the terrified enemies, a knuckle wrapped in Fist Energy shot out and smashed into my spear shaft.

Boom!

“Retreat into the mansion!”

I let out a short laugh at Im Yeongjun’s shout. He had bought them a brief moment.

“Did you set up some magic circles as traps?”

“Shut up!”

Whoosh!

He was their leader for a reason. As expected, he was the best of them.

No, at this level, he could even be called a Peak master in Murim.

*He knows how to use qi.*

One reason I considered Hunters so far inferior to martial artists was their method of handling qi.

But Im Yeongjun and the other Black Hunters moved far more efficiently than ordinary Hunters.

*Even so, they’re only this good.*

No matter how high someone flew or how low they crawled, there were walls they could never cross.

I punched toward the knuckle.

Im Yeongjun gritted his teeth and met my fist head-on.

Boom!

One Strike.

The knuckle broke.

Boom!

Two Strike.

Im Yeongjun’s fist was crushed.

KRA-BOOM!

Three Strike.

A move from the Flame-Extinguishing Divine Fist slammed into his shoulder.

His flesh melted and his bones were pulverized.

It was as though a fire dragon had devoured his entire shoulder.

Im Yeongjun spat blood and was sent flying into the distance.

“Team Leader!”

But he still had subordinates left.

The Black Hunters who had waited until the last moment quickly hoisted Im Yeongjun onto their backs and rushed into the mansion.

Thud.

The door had barely closed when layer upon layer of transparent barriers wrapped around the mansion.

*A defensive spell?*

It had to be an extremely powerful one. It even felt sturdier than the defensive magic Butler Kim had shown me before.

But I didn’t stop walking.

I reached the door in a single step and punched the dozens of defensive barriers.

*Four Strike.*

The Heaven-Destroying Divine Fist, unleashed with all my strength, hammered into the barriers.

Just as it had shattered some nameless cliff on Mount Song, the Heaven-Destroying Divine Fist broke and crushed everything blocking its path.

KRAAAAAASH!

With a roar that sounded as though the sky itself were splitting apart, the defensive barriers were torn to shreds.

The roof flew away, and the walls crumbled into ash.

Through the melted front door, I saw the frozen enemies.

Im Yeongjun stood at the center of them.

His jaw trembled. A single word, sounding almost like a groan, escaped between his lips soaked in blood.

“What… what the hell are you?”

I gladly answered him.

“A monster. Same as you.”

Team Leader Choi had said it before.

This world was teeming with monsters.

So I had decided that, every once in a while, I would become a monster myself.

Just like today.

“Have you ever heard of Tendon-Splitting and Bone-Twisting?”

It didn’t take long for Im Yeongjun to open his mouth.
## Chapter artifact 278

# Chapter 278

The beautiful two-story house had been transformed into a haunted ruin.

If the dozens of layers of defensive barriers hadn’t absorbed part of the Flame-Extinguishing Divine Fist’s impact, the entire place would have been reduced to ash.

Just then, I sensed someone approaching from behind, and a quiet voice sounded in my ear.

“Mr. Jin Taekyung.”

I had been sitting on a half-charred sofa. Turning my head, I answered,

“Yes.”

Team Leader Choi, Butler Kim, and Song Song stood there.

Their expressions were complicated as they looked at me. Considering they had seen the bodies strewn miserably across the garden, it was only natural.

My appearance—completely drenched in blood—probably wasn’t particularly pleasant to look at, either.

Song Song carefully asked,

“Did you… kill all of them?”

“Yeah.”

“……!”

“I’m kidding. I spared the ones who surrendered.”

I added one gentle word.

“For now.”

I had answered Song Song, but my words were also directed at Team Leader Choi and Butler Kim.

Team Leader Choi asked with concern,

“Are you hurt anywhere?”

“As you can see, I’m fine.”

“What about the survivors?”

“I gathered them in one place.”

“Without taking any other measures?”

“Of course I did. For the next few hours, they’ll be no different from corpses that can still breathe, so don’t worry.”

The personal measure I had taken was a Pressure-Point Strike.

After striking their Mute Acupoints, Paralysis Acupoints, and Sleep Acupoints, I had stacked the Black Hunters neatly inside the only room left standing.

I had used force to subdue them, but I wasn’t some blood-crazed murderer who intended to kill even those who surrendered.

More importantly, they might prove useful later.

“You did well. But…”

Team Leader Choi’s gaze shifted toward someone collapsed at my feet.

“Who is that?”

“The owner of this house.”

I turned the man over with my foot, revealing a man in his forties.

The homeowner and leader of the Black Hunters: Im Yeongjun.

His entire body was so covered in blood that he could easily have been mistaken for a corpse, but he was definitely alive. What was more, he didn’t have a single wound left on him.

Butler Kim examined him and muttered as though he already knew the answer.

“You used potions. Repeatedly, too.”

“Yes.”

“Did you torture him?”

“You have sharp eyes.”

“It was common during the Great Cataclysm. There were plenty of people worse than Black Hunters.”

Song Song’s expression darkened at the word *torture*. But soon, she let out a faint sigh and placed a hand on my shoulder.

“You worked hard.”

Feeling repulsed was only natural. Even I, who was accustomed to the ways of Murim, didn’t feel comfortable about it.

But Im Yeongjun had been far more tight-lipped than I had expected. Ordinary threats would never have been enough to make him talk.

“They aren’t ordinary opponents. Someone had to do it.”

“If you hadn’t done it, Hunter Jin Taekyung, I would have. Don’t take it too much to heart.”

Team Leader Choi and Butler Kim each added a word.

They were right. Just as they had said, it was something someone had to do. My hands were already stained with blood. There was no reason to hesitate over torture now.

I shook my head to clear away my troubled thoughts, then opened my mouth.

“There’s no physical evidence. Apparently, the moment I broke in and the alarm magic went off, they deleted all the relevant information.”

“All of it?”

“Yes. There weren’t even any computers in the house. Only two people, including Im Yeongjun, had cell phones. Even those were burner phones with no identifiable source.”

I showed them the remains of the cell phone I had collected beforehand.

Even someone as hopeless with this sort of thing as me could tell that recovery was impossible. Every component had been crushed, and they had burned the SD card, too.

Team Leader Choi clicked his tongue when he saw the wreckage.

“Thorough. At this point, there’s no way any documents would have been left behind.”

“Exactly.”

“What about the other Black Hunters?”

“Ten survived, but not one of them knows anything. The one who seemed to be their deputy was killed by me. Im Yeongjun recruited and trained every person who was here.”

From what I had gathered, they operated as a thoroughly compartmentalized organization.

Everything involving the Black Hunters, from laundering their identities to paying them, had been handled through Im Yeongjun.

“At least Im Yeongjun survived. What did he say?”

“That…”

I suddenly stopped speaking.

The one sentence he had screamed like a howl after experiencing Tendon-Splitting and Bone-Twisting three times still echoed in my ears.



“M-Myeongdong Guild! I said Myeongdong Guild!”



A major Guild that might not rank among the top ten in the country, but could easily be counted among the top twenty. And…

*Jihoon.*

It was also the Guild where an old friend I had met again recently belonged.

After thinking it over, I opened my mouth again.

“Could you give me a little time?”

“……?”

“There’s something I need to check personally.”

Team Leader Choi stared at me for a moment, then nodded.

“We’ll clean up the scene first. Check it and let us know.”

“Yes.”

“Let’s get started right away.”

At Team Leader Choi’s words, Butler Kim swung the staff he had been using like a cane.

The tightly closed door opened, and the ten Black Hunters whose acupoints had been struck floated into the air one after another before leaving the house.

Im Yeongjun was among them, of course.

“Everyone, stand back.”

After giving the warning in a low voice, Butler Kim began reciting an incantation.

As mana surged, enormous flames swallowed the two-story house that had barely managed to keep its shape.

The fire swept through the garden and would not stop until it erased everything.

Fwoooosh!

A cloud of acrid smoke rose along with the flames.

Yet the peace of the quiet rural village where the mansion stood remained undisturbed.

The mansion’s magic blocked all sight and sound. It would only be discovered much later.

“Will this do?”

“This is more than enough. Even if we didn’t, they would step in and erase this place themselves.”

People had disappeared overnight, and a house had burned down. But that was all.

The villagers would talk about it for a while, but nothing would happen.

That was how monsters with power and authority operated.

But there was only one thing I wanted to know.



**Garam Middle School Classmate Park Jihoon**



Which side did the owner of the number saved in my phone actually belong to?

* * *

It was still dawn, with the darkness not yet fully gone, when Park Jihoon got dressed and left his house.

A limousine driver in formal uniform was waiting at the entrance.

“You’re here, sir.”

“What’s going on? Why are you picking me up all of a sudden at this hour?”

“I’m not sure, sir. The Guild Master merely instructed me to come to your home and pick you up.”

Fair enough. What would a mere driver know?

Park Jihoon clicked his tongue softly and got into the car. Perhaps because it was still so early, the roads were empty.

After some time, the smoothly moving limousine stopped somewhere in Hannam-dong, where luxury apartments and villas stood in rows.

A massive mansion.

One of the guards stationed along the stone wall ran over and bowed to Park Jihoon.

“He’s waiting inside.”

Park Jihoon passed through the iron gates that reminded him of a European nobleman’s estate, then crossed a garden wider than an athletic field before finally meeting the person who had summoned him.

“Have you eaten breakfast?”

He was a man in his fifties with half-gray hair. Despite his age, he had an imposing build, and well-developed chest muscles were visible beneath his white robe.

Park Jihoon bowed his head and answered,

“Not yet.”

“Then come and eat. The beef-and-radish soup turned out very well today.”

It was only six in the morning. There was no reason to welcome a meal at this hour, especially after being woken from sleep.

Nevertheless, Park Jihoon picked up his spoon without complaint after offering his thanks.

“Won’t you eat, Guild Master?”

“I’ve already eaten. Don’t mind me and finish your meal.”

The man answered casually and unfolded a newspaper.

It was today’s morning edition.

On the front page was a photograph of a middle-aged man in a suit, bowing his head with a solemn expression.



**Park Tae Seop, Guild Master of Myeongdong Guild, visits the wake of the late Hunter Jung Hyunwoo. “I can only feel grief. I bow my head and apologize to the bereaved family.”**



Only then did Park Jihoon understand why he had been summoned.

*The old geezer’s pissed.*

The man who looked exactly like the middle-aged man in the photograph asked without taking his eyes off the newspaper,

“How’s the picture? Did I come out well?”

“Yes. You’re naturally handsome.”

“That’s your problem. No matter what you say, it always sounds like lip service.”

“I’m sincere.”

At the unhesitating answer, the middle-aged man—Park Tae Seop, Guild Master of Myeongdong Guild—raised his eyebrows.

It was a sign that his patience had run out.

“Jung Hyunwoo. Why did you kill him?”

Here it came.

Park Jihoon quietly set down his spoon and answered,

“I caught a whiff.”

“Then you should have stopped at covering your nose.”

“That was Myeongdong Guild’s role. Mine is twisting the necks of people who catch a whiff of something rotten before they start blabbing about it somewhere.”

“Without my permission?”

“Do I need permission, too?”

Bang!

Park Tae Seop slammed his fist into the dining table. With a splintering crack, the table broke apart, sending glass and food flying in every direction.

“Guild Master!”

The guards who came running were met by a furious shout.

“All of you, get the hell out! Don’t take a single step inside until I give you permission!”

“……!”

The guards froze for a moment, then bowed and withdrew.

Park Jihoon calmly pulled out a handkerchief and wiped the soup splashed across his face.

“What a shame. It was delicious.”

“How dare a brat who still smells of his mother’s milk…”

“We both stink of something rotten anyway. A little milk on top won’t make any difference.”

“I built this Guild with my own blood. And some little shit like you kills a Guild member without even saying a word?”

“Come on, Guild Master.”

Park Jihoon’s smooth brow, still free of wrinkles, furrowed.

The handkerchief in his hand dropped onto the shattered remains of the table.

“What else was I supposed to do?”

“What did you say?”

“Don’t you know how troublesome it gets if the people who catch a whiff of something start opening their mouths? One spark, and the whole house goes up in flames. If it were only your own house burning, I wouldn’t have anything to say. But the fire spreads to our side too, so I stepped in.”

“Even so, you—!”

“And I’d appreciate it if you would state things accurately. A war hero who fought and bled during the Great Cataclysm? I’ll give you that. But insisting that Myeongdong Guild is your personal Guild is a bit…”

Park Jihoon let out a short laugh and rose from his seat.

“Thank you for breakfast. Though I barely got a few spoonfuls.”

Park Tae Seop trembled as he watched him, then opened his mouth.

“Sit down.”

“If you have anything else to say, call me. If you keep this up, I’m going to lose my respect for a great senior like you.”

“I said sit down.”

The air around them began to churn violently.

Park Tae Seop, the Guild Master of Myeongdong Guild, was a hero born from the Great Cataclysm and one of the top rankers in the country.

But Park Jihoon knew that he couldn’t lay a hand on him.

“I’ll see you next time.”

He bowed politely and turned away.

That was when Park Tae Seop spoke again.

“Because of the sparks you caused, the whole house is about to burn down. You didn’t know that?”

“What are you talking about? I handled Team Leader Jung’s matter so thoroughly that there wouldn’t be any loose talk.”

“Those Black Hunters. I heard they recently messed with a D-rank Hunter from the Peace Guild?”

Park Jihoon’s face hardened.

He instinctively realized that a serious problem had arisen.

“……What is it? What happened?”

At that moment, the phone in Park Jihoon’s coat pocket began to vibrate.

As though possessed, he pulled it out and stared at the name filling the screen, his eyes darkening.



**Jin Taekyung**
## Chapter artifact 279

# Chapter 279

Jin Taekyung.

The three-syllable name appeared clearly on the screen.

A thunderous shout stopped Park Jihoon just as he was about to press the call icon.

“I’m not finished talking. Put that damn phone away and sit down right now!”

“……”

“Are you deaf?”

“……No, sir. Go ahead.”

Park Jihoon turned off the phone screen and dropped heavily into a chair. Park Tae Seop glared at him with blazing eyes.

“Was killing a Team Leader-level Hunter without permission not enough?”

“I was under the impression that matter had already been discussed. ‘That person’ said they had personally contacted you to ask for your understanding.”

“Understanding? Not a threat?”

“They’d be hurt if they heard you say that.”

“What the hell do you have against Jin Taekyung and the Peace Guild that you went as far as sending Black Hunters…?”

“Let’s stop there.”

Park Jihoon cut him off in a rigid voice.

“You don’t need to know facts you really ought not know.”

“……!”

“Isn’t it important that the Guild Master accepted the proposal? One way or another, the result matters more than the process.”

“Yeah. So is that why you turned that important result into this mess?”

Park Jihoon’s brow furrowed. Park Tae Seop’s complaints were nothing new, but this was the first time he had been so blatant about them.

*What the hell happened?*

“It would be best if we stopped bickering here. What problem has arisen?”

Park Tae Seop, breathing hard with anger, tossed out a single sentence.

“Two hours ago, Team 11 sent an emergency message.”

To the outside world, Myeongdong Guild had ten teams.

But that was merely its *public* face. The Team 11 Park Tae Seop had mentioned was a team that officially did not exist—in other words, a team made up of Black Hunters.

“Did you say an emergency message?”

“If you have eyes, check it yourself.”

Park Tae Seop pulled something from his robe pocket and tossed it over. When Park Jihoon caught it, he saw an old-fashioned cell phone so outdated that he couldn’t even guess when it had been made.

The call history had been wiped clean. In the message inbox, there was only one text, sitting there by itself. It had arrived two hours ago.

> Intruder detected.

A short, single line.

But its contents were anything but ordinary.

Park Jihoon closed the phone and asked,

“Where was it?”

“Far away. A backwater hole in the middle of nowhere, beside an unnamed mountain. It’s outside a safe zone, and there aren’t any Gates nearby, so there’s no reason for anyone to go there.”

“Any word after that?”

“If there had been, would I be bringing this up?”

“So they’re out of contact.”

“I sent people to check, but… I have a bad feeling about this.”

Park Jihoon shared his concern.

Seven years ago, as soon as he had been assigned to Myeongdong Guild, his first task had involved Team 11.

Park Tae Seop, the Guild Master of Myeongdong Guild, had strongly objected to hiding and training criminals. But he had been unable to defy the orders of *that person*.

That was how they had gathered roughly thirty Black Hunters.

*Three A-rank Hunters. And twenty-five B-rank Hunters.*

They were a force powerful enough to rival—or even surpass—Team 1, Myeongdong Guild’s elite.

And now they had lost contact after an intruder appeared.

Just then, anxiety began to crawl up from a corner of Park Jihoon’s heart.

Brrrrr.

The phone in his inner coat pocket began to vibrate again. The longer it continued, the more his anxiety swelled.

* * *

Ring. Ring…

The call went unanswered and ended in voicemail, just as it had every time before.

This was already the tenth call. I had sent a text a long time ago, too, but no reply had come back.

*He should be at work by now.*

The entrance of the high-rise building towering over the center of Seoul was crowded with people. I was watching the scene blankly when someone spoke to me.

“Excuse me.”

The man addressing me was dressed in a suit.

His face was angular, and his eyes were sharp. I could sense his solid build and the energy coiled inside his body. The man standing beside him, his colleague, was much the same.

I put away my phone and answered,

“Yes, excuse me.”

The suited man hesitated, then opened his mouth. The name tag on his chest clearly displayed both his name and his affiliation: Myeongdong Guild.

“We’re from the Security Team. We received a report about you.”

“I’m not a sir. What kind of report?”

“We checked the CCTV footage and saw you loitering in front of our building for quite a while… Is there something you need?”

The looks they gave me were full of suspicion and wariness.

A guy in casual track pants and a hoodie, with a cap pulled low over his face and sunglasses on top of that, peering into the building was bound to attract a report.

“Sir, would you mind moving somewhere else for a moment?”

“No, I’d rather not. And I told you, I’m not a sir.”

“It’ll only take a moment.”

Despite his fairly polite tone, his actions were the exact opposite.

Whoosh!

With two short bursts of wind, both men thrust their arms toward me at the same time.

And in the next instant, question marks appeared on their confident faces.

Tap. Grab.

“Huh?”

“Hmm?”

I caught both of their wrists without the slightest effort and put on a stern expression.

“Y-You rude punks. How dare you lay hands on this gentleman?”

“W-Wait a second.”

“Who the hell are you? Let go of this!”

The two C-rank Hunters from the Security Team were visibly flustered. No matter how hard they strained, their arms did not move even an inch, and their mouths fell open.

*Should I break them?*

I considered it for a moment, but the time wasn’t right yet. Before the commotion grew any larger, I released their wrists.

“Let’s not lay our hands on other people so carelessly.”

The two men rubbed their reddened wrists and cautiously asked,

“Were you… a Hunter?”

“Excuse me, but what are your affiliation and name?”

“I’m Jin Taekyung of the Peace Guild.”

“Excuse me?”

“Could you be the Lord Fuck I’ve heard about?”

“……You must have seen that internet broadcast.”

*I’d rather be the Sleeping Dragon of Shanxi. What the hell is Lord Fuck supposed to mean?*

I sighed and lowered my sunglasses slightly. The two men let out startled exclamations and immediately bowed deeply.

“It’s an honor to meet you.”

“You’re much more handsome in person.”

Their eyes sparkled like high school students who had just seen their favorite idol. Judging from their attitude, they clearly didn’t know anything about the deeper circumstances.

*Of course. Anything related to the Black Hunters would be top secret. If an ordinary Security Team Hunter knew about it, the secret would have leaked long ago.*

“But what brings you to our Guild…?”

“I came to see someone I know.”

“Someone you know?”

I took a thin piece of paper from my wallet and held it out. It was Park Jihoon’s business card, which I had received a while ago and kept there.

“Hunter Park Jihoon of Team 1?”

The Security Team Hunter tilted his head as he looked at the card, then asked his colleague,

“Senior, do you know who this is?”

“Who?”

“He says he’s Hunter Park Jihoon from Team 1. I know all the Hunters in Team 1, but I can’t quite remember this person…”

“Park Jihoon, Park Jihoon… Oh, him. You know, the one…”

He jabbed his colleague in the side with an elbow, and only then did the other man let out an “Oh!”

The two of them looked back and forth between me and the business card with fascinated expressions.

*What is this reaction?*

My eyes narrowed on their own. The Security Team Hunter, unable to see my reaction hidden behind my sunglasses, asked,

“Are you close with Hunter Park Jihoon?”

“We went to middle school together.”

“Ohhh, so you’re friends.”

I answered with a gentle smile.

“Well, we are for now.”

“Huh?”

“I’m joking.”

*I might not be.*

Without knowing what I was thinking, the Security Team Hunters laughed and continued their questions.

“So you came to see Hunter Park Jihoon?”

“Yes. He wasn’t answering his phone, and he wasn’t at home, either. I thought I might be able to see him if I came to his workplace.”

“I’m sorry about this. We didn’t know.”

“You were just doing your job, so don’t worry about it. More importantly, is Jihoon inside?”

The senior Security Team Hunter answered,

“He probably won’t come in today, either.”

“Today, too?”

“Yes. He doesn’t come to work often. If you count the number of times, maybe once a month? I’ve been here almost a year and have only run into him a few times, and this guy’s been here barely a month…”

“Sounds like the Hunters of Myeongdong Guild don’t come to work very often.”

“Would that make sense? I don’t know why, but everyone just accepts it.”

*He’s right. Why is that?*

I had never heard of a Guild Hunter who showed up for work once a month.

The question that had taken root in one corner of my mind grew deeper.

Without showing it, I opened my mouth.

“Could you try contacting Jihoon for me? I understand there’s a separate phone for Guild summons.”

“Uh, that’s…”

The two men hesitated, so I made them an offer they couldn’t refuse.

“I came to discuss a cooperative raid. If I put in a word, I think I could add one or two more people…”

“Gasp.”

“Are you serious?”

*Of course not.*

It was all a lie, from beginning to end. But I kept a perfectly straight face and continued.

“You’re both C-rank, right?”

“Yes, yes.”

“How did you know?”

“It’s obvious at a glance. But you seem too good to waste away in the Security Team.”

Strictly speaking, a Guild’s Security Team was little more than a non-mainstream department.

If a Hunter were truly skilled, why would the Guild let him waste away as a security guard? From the Guild’s perspective, sending him on raids would be far more profitable.

There was no way the two Security Team members didn’t know that. Their eyes began to shine.

“I’ll contact him right away!”

“I’d appreciate that.”

“Is there anything else you need?”

“Would it be all right if I looked around the Guild for a bit? I can wait for Jihoon inside.”

“Yes. Yes, of course.”

Unlike the senior, who kept bowing obsequiously, the junior Hunter’s face had gone stiff.

He had only been with the company for a month. It was probably the time when a sense of duty and loyalty to the company burned brightest.

“Senior, I don’t think that’s right.”

“What? You little punk?”

“I really respect Hunter Jin Taekyung, too, but doesn’t this violate the Guild’s internal regulations?”

“Hey, you idiot!”

He seemed to realize he had made a mistake after shouting, because he glanced at me before lowering his voice to a whisper.

“Are you crazy? It’s an A-Rank Gate. Even if you rot in the Security Team for three years, you’ll never get an opportunity like this.”

“Then we should report it to the Team Leader first…”

“God, you’re so rigid. Why would we need to report it just because he wants to look around for a moment? It’s not like he’s just anybody. He’s Hunter Jin Taekyung.”

“No, even so…”

“Please. Let’s live with a little yutori, okay?”[^1]

“Yutori?”

The junior Hunter’s expression suddenly turned grave.

“Please refrain from using such a thoughtless word in times like these. It makes me uncomfortable.”

“You’re out of your mind. Do you want to make your life at the Guild difficult from now on?”

This was a complete circus.

Clicking my tongue, I stepped forward. The junior Hunter flinched, then stuck out his chest.

“D-Do you have something to say?”

“No. I just found it inspiring listening to you.”

“Huh?”

“You’re a true patriot, and your loyalty to the company goes without saying. I’ll be sure to mention it when I meet the Guild Master of Myeongdong Guild later.”

“T-The Guild Master?”

“Yes. Jihoon said he would tell the Guild Master, too. I should make sure to mention that there’s an excellent talent here.”

I glanced at the name tag on the junior Hunter’s chest and added,

“Hunter Kim Cheol Soo.”

“……!”

The eyes of Kim Cheol Soo, so devoted to his company, trembled with emotion.

With the friendliest smile I could manage, I asked,

“Can I go in now?”

Kim Cheol Soo shouted at the top of his lungs,

“Irasshaimase!”

“……Ah, yes. Arigato.”

[^1]: *Yutori* is a Korean colloquialism borrowed from Japanese, meaning leeway or flexibility. Cheol Soo objects to the Japanese-derived word as inappropriate in the current climate.

* * *

The twenty-story luxury building belonged to Myeongdong Guild.

The senior Hunter, who had ditched his junior by pulling rank and followed me, continued chattering.

“The first through ninth floors house the civilian departments—tax, accounting, corporate affairs, and so on. From the tenth through the nineteenth floors, each floor belongs to a raid team.”

“What about the twentieth floor?”

“The Guild Master and the board of directors, obviously.”

“I see.”

“Team 1 is the Guild’s elite team, so they’re on the nineteenth floor.”

Ding.

The elevator arrived as he finished speaking. I pressed the button for the nineteenth floor and was waiting for the doors to close when—

“Hey, hey! Wait!”

The senior Hunter hurriedly pressed the open button.

The doors slid open, and a middle-aged man with a receding hairline stepped inside.

He gave us a sidelong glance, then covered the receiver slightly as he answered the call.

“Yes, yes. No, it’s nothing. It’s because of the elevator. Yes.”

The energy coming from him as he continued his important conversation was formidable.

*An A-rank Hunter?*

The senior Hunter had gone rigid at the man’s appearance. I gave him a questioning glance, asking who it was, and he slowly raised one finger while mouthing the words.

*Team 1 Leader.*

No wonder he hadn’t pressed a floor.

As Team 1 Leader, going to the nineteenth floor was only natural. I focused on his conversation.

And in the very next moment, a familiar voice pierced my ears.

—Are you saying twenty-eight people were wiped out? Hurry up and—

“……!”

My body trembled as though I had been electrocuted.

A familiar voice.

And, on top of that, the number twenty-eight.

*So it was you.*

My hand moved at the same time as the thought.

Grab!

“Ghk! Who the hell are you…?”

I seized the Team 1 Leader’s throat like a shackle and whispered into the receiver,

“Park Jihoon. You fucking bastard.”

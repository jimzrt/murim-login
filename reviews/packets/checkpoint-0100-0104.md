# Checkpoint Review — 100–104

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

# Chapters 100–104

## Plot

Im Chunsoo learns that Sangdong Guild’s investigation of the Peace Guild failed, Hong Woojin disappeared, and the Security Team was defeated by Jin Taekyung. Taekyung interrogates the captured Hunters, confirms that Woojin was hired by Team Leader 1 and that Im Chunsoo directed the operation, then faces Chunsoo in person. Chunsoo tests him with ice spikes, but Taekyung counters with Fire Wall before Level 80 mage Kim Hwajong arrives. Hwajong’s former-instructor relationship with Chunsoo is revealed, along with Chunsoo’s deep fear and obedience toward him. Team Leader 1 conceals the encounter and formally warns the Security Team over its unauthorized escalation.

Taekyung buys a two-story house in Goyang for his family and plans to live there alone until Hayeon finishes her entrance exam. After moving out of Hope Goshiwon and logging into Murim, he discovers Seong Jinho emerging from the capsule inside the new house.

In Murim, Taekyung, Jin Mukyung, and Hyuk Mujin travel through a blizzard to Honju. They stay at the Phoenix Inn, where Mujin’s travel funds rapidly dwindle under Taekyung’s appetite. When martial artists ruin Taekyung’s chicken-and-corn soup and provoke him, he punches the first aggressor. The inn’s proprietress hears that the Sleeping Dragon of Shanxi subdued six men, recognizes the name, and goes to meet him.

## Continuity

- Im Chunsoo is Sangdong Guild’s Level 75 A-rank ice-mage Guild Master; the failed Security Team operation against Taekyung was conducted under his special order.
- The Security Team’s six Hunters were defeated and captured, then released by Team Leader 1. Choi Byungil’s team faces formal discipline; the final punishment remains unknown.
- Team Leader 1 assesses Taekyung as a top-tier B-rank or possibly A-rank Hunter.
- Hong Woojin is a B-rank Familiar mage hired by Team Leader 1. The relationship between Woojin’s investigation and Sangdong’s operation remains unresolved.
- Kim Hwajong is a Level 80 mage, former Hunter Training Center instructor, and the trainer who traumatized Class 25 trainee Im Chunsoo. Why he arrived at the confrontation—and why he now works as a butler—remains unknown.
- Taekyung owns a two-story detached house in Goyang and intends it as his family’s home. Logout remains active, so he no longer needs the capsule for travel between worlds.
- Seong Jinho unexpectedly emerged from Taekyung’s capsule inside the new house. How and why he entered remains unknown.
- Taekyung’s current Quest requires him to deliver the Jin Family of Taiyuan’s Lunar New Year invitation to the Mount Heng Sword Sect, now led by Lee Seowol, his former accuser.
- Taekyung, Mukyung, and Hyuk Mujin are staying at the Phoenix Inn’s private residence in Honju. Wikyung gave Mujin fifty silver nyang for the journey; Mujin has five silver nyang left after paying half the lodging fee.
- Mukyung is a Peak master who uses a superficially learned heat-yang technique to warm Hyuk Mujin and considers enduring hunger martial training.
- The unnamed Phoenix Inn proprietress knows the name Sleeping Dragon of Shanxi and has gone to meet Taekyung after hearing about the fight.
- The three possible surveillance properties near Taekyung’s former home remain unidentified, as do the black Familiar’s immediate instructions and the final consequences of the Phoenix Inn fight.

## Translation Decisions

- Retain **Familiar**, **Logout**, **Inventory**, **Qi Sense**, and **Fire Wall**.
- Render **아가리 봉인술** as **mouth-sealing technique**.
- Render **교관님** as **Instructor**, **1번 훈련생** as **Trainee Number One**, and **춘수** as **Chunsoo** when used familiarly by Hwajong.
- Render Im Chunsoo’s **자네** as **you** while preserving his blunt senior voice.
- Render **열양공** as **heat-yang technique** and related **화기** as **fire qi**.
- Render **원단** as **Lunar New Year**.
- Render **항산검문주** as **Sect Leader of the Mount Heng Sword Sect**.
- Render **별채** as **private residence**, **냥** as **nyang**, and **봉황객잔** as **Phoenix Inn**.
- Render **계용옥미갱/계용옥미앵** as **chicken-and-corn soup**, preserving the latter as a spelling variant.
- Render **형장** as **Brother** in the martial artists’ address to Taekyung.

## Durable state

{
  "active_continuity": [
    "Sangdong Guild's Security Team was assigned to surveil Jin Taekyung; the property being used as its surveillance base remains unidentified.",
    "Choi Byungil led the failed operation against Taekyung and was defeated with the other field Hunters; the Security Team faces written discipline, a pay cut, and possible dismissal.",
    "Kim Junsu is the Security Team's sole Familiar mage, and Hong Woojin is an outside B-rank Familiar mage hired by Team Leader 1.",
    "Seong Jinho is Taekyung's thirty-year-old civilian goshiwon manager and sworn-brother-like friend in Bucheon.",
    "Im Chunsoo is a Level 75 A-rank ice mage and Guild Master of Sangdong Guild.",
    "Kim Hwajong is a Level 80 mage and former Hunter Training Center instructor; he trained Im Chunsoo, who was a Class 25 trainee assigned to the 28th Regiment, First Battalion, Second Company.",
    "The reason Kim Hwajong arrived at the confrontation remains unknown, as does why he now works as a butler.",
    "Team Leader 1 assesses Taekyung as a top-tier B-rank or A-rank Hunter.",
    "Taekyung owns a two-story detached house in Goyang intended as his family's home and will live there alone until Hayeon finishes her college entrance exam.",
    "Logout is active, so Taekyung no longer needs the capsule to travel between the modern world and Murim.",
    "Seong Jinho unexpectedly emerged from Taekyung's capsule inside the new house after Taekyung logged into Murim; how and why he entered remains unknown.",
    "Taekyung, Mukyung, and Hyuk Mujin have reached Honju and are staying at the Phoenix Inn's private residence.",
    "Mukyung is a Peak master and uses a superficially learned heat-yang technique to warm Hyuk Mujin.",
    "Taekyung must deliver the Jin Family of Taiyuan's Lunar New Year invitation to the weakened Mount Heng Sword Sect, now led by Lee Seowol, his uncomfortable former accuser.",
    "Hyuk Mujin is a First Rate martial artist from a tenant-farmer family, Captain of the Jin Family's Gatekeepers, deputy squad leader of White Tiger Hall's reconnaissance squad, and a candidate to become the next Master of the Gatekeeper Pavilion.",
    "Jin Wikyung gave Mujin fifty silver nyang for the journey and ordered the travelers to use good lodging and meals because they had no attendants.",
    "Mukyung considers enduring hunger a form of training, while Taekyung's appetite causes Mujin severe financial anxiety.",
    "A group of martial artists at the Phoenix Inn ruined Taekyung's soup and provoked him; Taekyung punched the first aggressor.",
    "The unnamed Phoenix Inn proprietress was told that the Sleeping Dragon of Shanxi subdued six martial artists and went to see him."
  ],
  "continuity_sources": [
    104
  ],
  "open_questions": [
    "Which of the three recently traded properties is being used by the surveillance personnel?",
    "Whether the black Familiar and Kim Gwondong are operating under the same immediate instructions remains unresolved.",
    "Why Kim Hwajong arrived at the confrontation remains unknown.",
    "Why Kim Hwajong, despite his former instructor status and exceptional ability, now works as a butler remains unexplained.",
    "What final disciplinary action will be taken against the Security Team remains unknown.",
    "How and why Seong Jinho entered the capsule and emerged inside Taekyung's new house remains unknown.",
    "How Lee Seowol will react to the invitation remains unknown.",
    "What will result from the Phoenix Inn fight, and why the unnamed proprietress recognizes the Sleeping Dragon of Shanxi, remain unknown."
  ],
  "safe_through": 104,
  "temporary_decisions": [
    "Use mouth-sealing technique for 아가리 봉인술.",
    "Keep Fire Wall as the spell name.",
    "Render Im Chunsoo's 자네 as you while preserving his blunt senior voice.",
    "Render 김화종's 춘수 as Chunsoo and 교관님 as Instructor.",
    "Render 1번 훈련생 as Trainee Number One.",
    "Render 열양공 as heat-yang technique.",
    "Render 원단 as Lunar New Year.",
    "Render 봉황객잔 as Phoenix Inn and 계용옥미갱/계용옥미앵 as chicken-and-corn soup."
  ],
  "version": 1
}

## Reading copies

## Chapter artifact 100

# Chapter 100

Everyone had at least one hobby. Im Chunsoo was no different.

The first thing Team Leader 1 saw when he entered the Guild Master’s office was a golf ball rolling toward the door.

Roll, roll. Thunk.

The ball had rolled far wide of the hole and only stopped after striking Team Leader 1’s shoe. As he bent down to pick it up, Im Chunsoo waved him off.

“Forget it. Come over here and have some tea.”

“Yes, sir.”

A brief silence passed between them. After savoring his tea, Im Chunsoo suddenly spoke.

“Smells good, doesn’t it?”

“Ah, yes. I suppose it must be good tea.”

“This is Longjing tea. I received it as a gift, but to be honest, I don’t really know what it is. It’s just filthy expensive.”

“What?”

“Why are you so surprised?”

“I thought you liked tea.”

“Not at all. I only pretend to savor it because I want to look sophisticated. At home, I drink instant coffee.”

Team Leader 1 let out a quiet laugh. Im Chunsoo’s love of tea was famous among the Guild executives. They had even begun competing to see who could give the Guild Master the better tea.

“A few people are going to be surprised.”

“For example?”

“Team Leader 3. He’s been bragging that he’ll bring back some famous tea from his upcoming business trip to China.”

“Fire that bastard. He’s lost his mind thinking about gathering weeds instead of doing his job.”

“You’re serious?”

“Of course I’m joking. Am I not allowed to joke?”

Light laughter passed between them. Im Chunsoo gulped down the remaining tea as if it were cold water, then smacked his lips.

“So, when are you going to tell me?”

“Tell you what?”

“You have some new information. I went out of my way to tell you a secret because you were having trouble speaking up…”

“Was it that obvious?”

“Look in a mirror before you come in next time. With a long face like that, anyone could tell.”

It wasn’t long before Team Leader 1 finally managed to speak.

“The investigation into the Peace Guild that you ordered previously… has failed.”

“Both of them?”

“Yes. I’m sorry.”

“Explain in more detail.”

“They approached carefully, but they say it would be better not to provoke the Peace Guild Master or Team Leader.”

“I expected as much. I should have made the request personally. In the end, I didn’t step in because of my useless pride, so some of the blame is mine.”

“No, it was because I was inadequate.”

“That’s true, too. Even if those locked-down bastards were out of reach, this C-rank Hunter named Jin Taekyung should have been a success.”

Im Chunsoo shot him a cold glare.

“Why exactly did you fail? I gave you a Familiar mage hired from outside and even assigned the Guild’s Security Team to him.”

“Well, that…”

Team Leader 1 hesitated, then finally forced out the words he had been unable to say.

“We lost contact.”

“Hm? That bastard Hong Woojin?”

“Hong Woojin disappeared after leaving a single text message. The ones we lost contact with were the Security Team.”

“Why the Security Team? Don’t they report the situation regularly?”

“Yes. Reports come in every two hours, but… the last one was four hours ago.”

“Are you saying the entire Security Team walked out on us?”

“No. Judging by the circumstances, it’s highly likely Jin Taekyung got to them.”

“What?”

What was that supposed to mean?

As Im Chunsoo stared at him in disbelief, Team Leader 1 handed him the pages he had printed out.

“Today’s report.”

The fact that only certain sections had been highlighted in red showed that this was an emergency report, not a regular one.

Im Chunsoo’s eyes raced across the words.

The target had spoken on the phone with someone whose identity was unknown, and both the contents of the conversation and the target’s actions were suspicious. After reading the report from beginning to end, Im Chunsoo let out a sigh.

“Hah. He’s more interesting than I expected. What happened next?”

“The Security Team Leader contacted me directly. He said they needed to pursue the target immediately, so he would take action first and report afterward.”

“And then they lost contact…”

Im Chunsoo fell deep into thought as he tapped the table.

Tap. Tap. Tap.

When he raised his head, the high-quality wooden table had frozen solid.

“Who did Jin Taekyung call? You found out at least the person’s full name, or you wouldn’t have shown me this.”

“Seong Jinho. A thirty-year-old exam candidate living in Bucheon.”

“……Team Leader 1. Did I hear you wrong? An exam candidate, not a Hunter?”

“I checked again myself, but there’s no mistake. He’s the manager of the goshiwon where Jin Taekyung lives. They’re supposedly like sworn brothers.”

“Hah. Today keeps surprising me.”

Im Chunsoo had expected him to be at least an A-rank Hunter. But what was this? A civilian exam candidate?

Shaking his head, Im Chunsoo rose from his seat.

“Ugh, we really got played. How does a Guild with only five people have so much to hide?”

“What should we do?”

“What do you mean, what should we do? It’s almost dinnertime. We should go have a meal.”

“……What?”

Im Chunsoo clicked his tongue at the bewildered Team Leader 1.

“Stop talking and follow me.”

He was thinking of having dinner in Ilsan that evening.

* * *

The six-on-one fight ended in an instant.

To begin with, Choi Byungil was the only one who could exchange blows with me. Even he didn’t last long before dropping to his knees.

*Obviously.*

But it seemed to have been a tremendous shock to someone.

With both ankles broken, Choi Byungil continued talking to me with a face as white as a sheet.

“An A-rank Hunter? Were you hiding your identity?”

“No. I never hid my identity.”

“Tell me your real affiliation! Is Ares Guild making a move against our Sangdong Guild…?”

“I’m with the Peace Guild. And Ares Guild wouldn’t be interested in your Guild. You’re in completely different weight classes.”

“Then who was the person you called?”

“How many times do I have to tell you? He’s my goshiwon manager hyung. Would you know him if I said his name was Seong Jinho?”

“This can’t be. This can’t be happening.”

In the end, there was nothing for it but to use the mouth-sealing technique. I tore his clothes into strips and gagged him, then treated all the remaining wounded, including him.

Of course, I didn’t use the potions I had bought from the Store.

“Wow, Sangdong Guild gives you guys some serious support.”

Even after looting only what they had brought with them, the quality and quantity of their Equipment and consumables were nothing to sneeze at. I used some of them for treatment, and the rest…

“I’m confiscating this for now. Anyone have a problem with that?”

Naturally, no one raised a hand.

They must have been so intimidated by my overwhelming strength that, even after their injuries had been healed, they didn’t dare attack me again. They were fairly smart men.

“Now, who wants to tell me all about your mission?”

Once again, nobody raised a hand, so I had to choose someone myself.

The choice was easy.

“You.”

“M-me?”

“Yeah, you.”

The Familiar mage, Kim Junsu, flinched. Then he declared with a resolute expression,

“I’m with the Security Team. I cannot carelessly disclose the Guild’s confidential information to an outsider.”

“Oh.”

I was impressed. At the same time, I grabbed him by the hair and yanked.

A small sound like tape being ripped came from somewhere, and his wig came clean off. The gleaming bald crown hidden beneath it was exposed.

“What is this?!”

“From now on, if you lie or keep claiming ignorance in response to my questions, I’ll pluck your hair out by the handful.”

“……!”

After that, everything proceeded smoothly. All kinds of information poured from the mouth of a balding man desperate to protect his hair by any means necessary.

“Hong Woojin?”

“Yes. He’s a B-rank mage hired from outside by Team Leader 1. Like me, his specialty is Familiar magic.”

“Really?”

What a waste. I should have caught that bastard and beaten the information out of him, too.

*I’ll run into him someday. If it takes too long, I can always track him down myself.*

Smacking my lips, I continued extracting information. Whenever Kim Junsu seemed to hesitate, I encouraged him by fiddling with his remaining hair.

“That’s everything. I really mean it, that’s all. Even though I’m in the Security Team, I truly don’t know anything else. So please, just leave my hair alone…”

His tone was full of both resentment and sincerity. The final words in particular struck a chord with me.

*This should be more or less everything.*

The mastermind behind it was the Sangdong Guild—or, more precisely, Im Chunsoo.

After seeing that his spendthrift son had been shaken down for a hundred million won in income, he had started digging into our Guild.

Well, in the end, I was the one who robbed him instead.

“The Guild Master won’t let this go.”

“Is that some line reserved for weaklings? Forget invoking the Guild Master and clean up the shit you made yourself.”

“……Tch.”

At my sharp retort, Choi Byungil lowered his head in frustration. But the man wasn’t entirely wrong.

*The Sangdong Guild Master is going to be pretty pissed when he finds out.*

He had sent his subordinates to watch me, only for them to get robbed and captured instead. For the Guild Master—and the Guild as a whole—this was about as fucking humiliating as it got.

Given the seriousness of the matter, I could only hope they would quietly bury it and move on.

*Should I call Team Leader Choi?*

That was when it happened.

010-xxxx-xxxx

A call from a number I didn’t recognize.

What was this?

A strange tension rose within me for no apparent reason as I answered.

“Hello?”

“Come downstairs. I’m waiting below.”

“Huh? I think you have the wrong number.”

“Jin Taekyung. That’s right, isn’t it?”

“Well, yes, but… who are you?”

“My name is Im Chunsoo. I heard you have a few of my people with you.”

“……”

“Are you listening?”

I was listening. I just couldn’t speak.

The Guild Master of a mid-sized Guild had come all the way here himself to meet me. And it was Im Chunsoo, of all people—the man with the terrible temper.

“Come down. We can clear up any misunderstandings over a meal.”

There was no misunderstanding that needed clearing up, but I had no idea what would happen if I said, *No.*

Hadn’t the man already found out my location?

In the end, I had only one option.

“I’ll be down shortly.”

* * *

Im Chunsoo’s first impression was intense. He was younger than I expected, and although his eyes seemed gentle, they burned with heat.

*Fiery.*

Ironically, that was my first thought upon meeting a master of ice magic.

“Hello. My name is Jin Taekyung.”

“I’m Im Chunsoo.”

His voice was cold, unlike his burning gaze. At last, he seemed like someone who deserved the nickname Frozen.

“It’s interesting to see in person the face I’d only seen in report photos.”

There were actually people who could admit so bluntly and without embarrassment that they had dug into my background.

“What about my people?”

“They’re upstairs.”

“Are there any fatalities?”

“Of course not. I have no desire to become a criminal.”

“I appreciate that.”

Im Chunsoo gave me a slight nod.

“My people got impatient and made a mistake. Can you let it slide?”

“If there’s reasonable compensation.”

Im Chunsoo let out a quiet laugh, and the man beside him, who looked like a Team Leader, frowned.

“Young man, you’re rude.”

“I am, somewhat… but hearing that from someone who even put me under surveillance feels a little strange.”

“Even so—”

The man couldn’t continue. Im Changsoo raised a hand to stop him.

“Team Leader 1, go upstairs and release my people.”

“……Yes, Guild Master.”

If Kim Butler possessed a gentle charisma, this man possessed a rough one. Maybe it was because they were both mages. Somehow, the two men overlapped in my mind.

“Come take a walk with me.”

Im Changsoo went ahead, and I followed behind him.

“Do you know something?”

After walking briskly for a while, Im Chunsoo suddenly spoke.

“Once I have a grudge against someone, I have to see it through to the end. I don’t know about you, but that’s the kind of person I am.”

*Very Murim of him.*

The strong devour the weak. Survival of the fittest. It seemed the blood of a Murim tough guy flowed through this man’s veins, too.

“That’s how I built the Sangdong Guild. I climbed higher by stepping on what I had brought down and salvaging whatever I could.”

“I see.”

“What about the Peace Guild?”

“……What do you mean?”

“The past decade has been dull. We’re allies with every nearby Guild, and we haven’t had a rival for a long time. Then you people appeared.”

As I looked into his eyes, where curiosity and passion seemed to be boiling, I had only one thought.

*This is dangerous.*

Whether I cared or not, Im Chunsoo continued speaking.

“Your Guild Master and Team Leader are people whose information I can’t easily access myself… But more than anything, your existence has stirred me up.”

We were climbing a hill now. Despite his considerable age, Im Chunsoo didn’t seem short of breath.

“Do you know why I came all the way here?”

“To see me.”

“You’re only half right.”

Im Chunsoo’s footsteps stopped. Slowly turning around, he released a frigid chill from his entire body.

> **System**
>
> Level 75 Im Chunsoo

“At my age, time is money. I’m not so indulgent that I’d come all the way here just to see your face.”

Frozen. The seasoned A-rank mage who had fought his way through the Great Cataclysm himself.

The moment he extended his hand toward me—

Hissssss.

Around a dozen ice spikes formed in the empty air above my head. The midsummer air froze, and frost settled over the scorching dirt path.

*I’d been well and truly caught.*

I had thought he was an old man with some sense of propriety. I never imagined he would launch straight into something like this.

“Do you really have to go this far?”

“I’m going this far because it’s you.”

“I’m only a C-rank.”

“Exactly. I want to see what that C-rank Hunter can do.”

The moment he finished speaking, Im Chunsoo clenched his fist. The ice spikes, streaming with biting cold, shot toward me.

Whoosh!

But they couldn’t even touch the hem of my clothes.

“Rise up. Fire Wall.”

At the sound of a clear voice, the mana permeating the air began to churn. The ground, which had been frosted over by Im Chunsoo’s magic, melted as flames surged upward.

Fwoosh! Fwoosh!

It was exactly what its name suggested: a wall of fire. Blue flames swallowed the ice spikes and split the space between Im Chunsoo and me.

Beyond the wavering flames, Im Chunsoo cried out in shock.

“What is this…!”

But I wasn’t looking at Im Chunsoo.

Behind him, a man standing at the entrance to the hiking trail greeted me in a gentle voice.

“I’m glad I’m not late. Chunsoo, you’re here too.”

> **System**
>
> Level 80 Kim Hwajong

Kim Hwajong.

Kim Butler had arrived.
## Chapter artifact 101

# Chapter 101

*What the hell is this?*

I was dumbfounded. Butler Kim’s appearance was unexpected, but that was nothing compared to the words he had directed at Im Chunsoo.

*Chunsoo? You?*

*Were the two of them acquainted?*

Come to think of it, Butler Kim and Im Chunsoo had a lot in common. They were around the same age, and both had been Hunters for a long time.

*Come to think of it, Butler Kim was active as a Hunter during the Great Cataclysm, too.*

I had never heard it directly from him, but I had suspected as much. Looking back and forth between the two men, I carefully asked,

“Are you two close?”

Im Chunsoo’s pupils trembled.

* * *

When Im Chunsoo first received the report on the Peace Guild, he had doubted his own eyes.

The face in the photograph was one that remained in his hazy memories—a face he had been certain he would never see again.

*Who did you say this man was?*

*Peace Guild Master Kim Hwajong. He’s fifty-five years old and a B-rank Hunter.*

*Kim Hwajong? A B-rank Hunter?*

*Yes. Is there some problem?*

*No, no. He resembles someone I used to know, so I mistook him for that person.*

That figures. Im Chunsoo let out a sigh of relief.

The face did resemble him a little, but that was all. More importantly, hadn’t that man died over thirty years ago?

No matter how bizarre the world had become, the dead could not come back to life.

*Even if that bastard had come back to life, he wouldn’t be rotting away in a place like this. I simply mistook him for an old B-rank Hunter.*

That day, Im Chunsoo drank a glass of soju for the first time in a long while and tried to shake off his uneasy feelings. It was an attempt to cast off the terrible memories that had clung to his ankles even after he turned fifty.

*Damn. I’m this old, and I’m still like this.*

Later, when he heard that Kim Hwajong’s information was protected by airtight security, he had even felt a chill run down his spine.

*Could it be? No. There’s no way.*

But then… why did ominous premonitions never turn out to be wrong?

“Rise up. Fire Wall.”

A quiet voice chanting a spell rang out, and a wall of fire surged upward.

*Fwoosh! Fwoosh!*

Blue flames burning at an extreme temperature vaporized the ice spikes, which were harder than steel, without leaving a trace.

And then—

“I’m glad I’m not too late. You too, Chunsoo.”

The moment he heard the voice he could never forget, not even in his dreams, Im Chunsoo remembered.

The terror of being controlled by that man.

The humiliation of rolling around on the ground to survive.

*Fuck… I’m screwed.*

As he stood frozen like a stone, Jin Taekyung asked him,

“Are you two close?”

What? Close?

Im Chunsoo swallowed the stream of curses rising from the depths of his lungs and turned around.

A man he had believed had died long ago was standing there.

“I-Instructor.”

Butler Kim smiled gently. It was the smile of a demon still deeply engraved in Im Chunsoo’s mind, even after all these years.

“Twenty-eighth Regiment, First Battalion, Second Company. Im Chunsoo. Yes, I knew the moment I saw you.”

It was the resonance of the soul.

Im Chunsoo’s hunched back straightened. His feet snapped together at a forty-five-degree angle, and his gaze turned fifteen degrees upward toward the front.

After a series of movements as fast as lightning, a thunderous shout burst from his throat.

“Trainee Number One! Im! Chun! Soo!”

The mountain shook as he bellowed out his military identification for the first time in thirty years.

* * *

What Team Leader 1 found after climbing up the mountain was grass splattered with blood in several places and the Security Team bound tightly with magical ropes.

*What a sight.*

Clicking his tongue inwardly, he drew his sword and cut through the ropes.

Everyone had lost some blood, but none of them appeared to have suffered serious injuries. Jin Taekyung seemed to have shown them at least the bare minimum of consideration.

*At this level, he’s either a top-tier B-rank… or an A-rank Hunter.*

That was how strong Jin Taekyung appeared to Team Leader 1.

For one person, the walk back down the mountain was a hellish experience.

“Why did you do that? We might have been able to overlook the surveillance, but what happened today could amount to attempted murder. Did you start this after thinking about what would happen afterward?”

“I’m… sorry.”

At Team Leader 1’s words, the Security Team Leader hung his head.

They had gone so far as to use force, only to be thoroughly trounced by Jin Taekyung. Even if he had ten mouths, he would have had nothing to say.

“The Guild Master is deeply disappointed.”

“Th-then?”

“A written report and a pay cut are a given. Prepare yourself for anything beyond that, too.”

“Are you talking about resignation?”

“That depends on the Guild Master.”

“Team Leader, perhaps…”

“Let me tell you up front: don’t ask me for any favors. I don’t have any interest in taking the side of someone who smeared the name of the company I work for. And I have no intention of going against the Guild Master’s wishes.”

“…”

“Whew.”

It was then that Team Leader 1 let out an irritated sigh.

A booming shout echoed from far away.

—Trainee Number One! Im! Chun! Soo!

“……”

“……”

What was that? Were they hearing things?

Team Leader 1 and even the Security Team members, who had all looked ready to die, jumped in surprise. The first to recover his composure was the Security Team Leader.

“Team Leader 1, I’m sorry to bring this up in this kind of atmosphere, but I think I just heard the Guild Master’s voice.”

Team Leader 1, who had been cleaning out his ears, opened his eyes wide.

“Did you hear it too?”

“We heard it, too.”

“But we couldn’t really tell whether it was the Guild Master’s voice… We think we heard a name, though.”

“That was a person’s name? I thought it was just someone screaming.”

“Really? I thought it sounded like someone giving their name and rank.”

Team Leader 1’s face hardened as he listened to the Security Team whispering among themselves.

“Who just said that? What was that about giving a name and rank?”

To him, Im Chunsoo was a respected senior and superior.

Im Chunsoo was an unrivaled Hunter who had been active since the Great Cataclysm and a war hero—and they were saying he had suddenly given his name and rank?

Team Leader 1 had never imagined such a thing. He couldn’t even imagine it.

“Do you still have the leisure to spout this kind of nonsense? Do you think this is something people in their right minds would say?”

“S-sorry.”

“We must have heard it wrong.”

“Everyone, get a hold of yourselves. Understood?”

After issuing his warning, Team Leader 1 started walking again.

That was when it happened.

—No, sirrrrr!

“……”

—I’ll correct it, sirrrr!

“……”

Those were the shouts of a private second class filled with the very essence of his soul.

It took a while before Team Leader 1’s tightly sealed mouth finally opened.

“From now on, we’re running at full speed. Move.”

“M-Move!”

Everyone gathered there was at least a C-rank Hunter. They were superhuman beings who had already far surpassed the limits of ordinary people.

They raced forward like runaway locomotives and reached the entrance to the hiking trail in less than five minutes.

“You’re slow as hell. Took you long enough?”

“Guild Master!”

“Keep your voice down. You’ll burst my eardrums.”

Seeing Im Chunsoo looking the same as always, Team Leader 1 let out a sigh of relief.

“I was worried something might have happened…”

“Something happened? Was there anything strange?”

“N-no, sir. But where did that Jin Taekyung bastard go?”

“I gave him a talking-to and sent him on his way. After speaking with him, I found out he was a better fellow than I expected. Why?”

“I was wondering if he had caused some kind of disturbance.”

“Ah, are you talking about the man shouting earlier?”

“Yes, that’s right. But his voice sounded just like…”

He couldn’t bring himself to finish the sentence.

Just like the Guild Master’s.

Im Chunsoo glared at him.

“Just like what?”

“Oh, it was nothing.”

“What a bland bunch. Some greenhorns were playing army down there, so I chased them away. Do colleges still have hazing culture these days?”

“Ah, I see.”

“What was it? I made them do some PT exercises for a while, and they looked ready to die.”

Team Leader 1 felt the suspicions he had been harboring vanish completely.

*I must have been out of my mind. How dare I even think such a thing?*

While he was deeply repenting to himself, Im Chunsoo was tearing into the Security Team.

“Security Team Leader.”

“Y-yes, sir!”

“Oh, you can answer properly. After causing this mess, are you still a Team Leader just because you’re technically still a Team Leader?”

“I’m sorry, Guild Master!”

“Are the others keeping their mouths shut because they did such a good job? Do I need to make my sword dance today?”

“We’re sorry, Guild Master!”

Team Leader 1 watched the scene with a pleased smile.

Every so often, there were people who spread the rumor that Im Chunsoo had a godawful personality. But after watching him up close, Team Leader 1 knew better. He was a charismatic superior and an outstanding senior in life.

*Guild Master. I’ll follow you forever.*

As Team Leader 1 gazed at Im Chunsoo’s back with boundless respect, he suddenly tilted his head.

*…But why is there dirt on the Guild Master’s back?*

He must have scolded those kids rather intensely.

* * *

“We’ve arrived.”

At Butler Kim’s words, I came to my senses with a start and looked around. Through the window, I could see the entrance to an apartment complex.

*When did we get here?*

“Th-thank you.”

“Don’t mention it.”

A smile appeared on his handsomely lined face. He looked like a middle-aged actor who had once ruled an entire era.

*No, this man really did rule an era, too.*

Until now, I had thought of him as nothing more than a senior Hunter from a distant generation. But that meant I hadn’t understood Butler Kim at all.

*He made an A-rank mage—and Im Chunsoo, no less—run around like a dog.*

He had made a former war hero do a hundred sets of PT Exercise No. 8, then later kicked him in the shin with his dress shoe. Even now, the way he had calmly berated Im Chunsoo in that gentle voice sent chills down my spine.

*Trainee, who uses mana during PT exercises?*

*Whack!*

*Trainee Number One Im Chunsoo. S-sorry, sir.*

*Does it hurt? Now that you’ve gotten older, has your voice gotten quieter, too?*

*No, sirrrrr!*

*Attention. At ease. Attention. At ease.*

*Snap-snap-snap-snap!*

*On your backs. On your fronts. On your backs. On your backs.*

*Gasp.*

*Trainee, didn’t you hear me say on your backs? Get your head straight.*

*I’ll correct it, sirrrr!*

*And why are you bullying an innocent junior? Haven’t I repeatedly emphasized that seniors and juniors should help each other?*

*S-sorry, sir.*

*Repeat after me. Sitting down, cherish your junior; standing up, cherish him. One. Two.*

*Cherish my junior!*

*Trainee, I remember you’re Class 25. Am I right?*

*Trainee Number One Im Chunsoo. Yes, sir.*

*I’m Class 3. If what happened today gets out or happens again, Classes 4 through 24 will assemble without exception.*

*…*

*Why aren’t you answering? Prepare for squat jumps.*

*P-prepare, sir…*

He kept working him over, then working him over some more.

It was the kind of sight you couldn’t see even if you paid for it. If the Sangdong Guild members had witnessed it, the Guild might have had to close its doors that very day.

*What on earth is Butler Kim’s real identity?*

If someone was Class 3 at the Hunter Training Center, they could line up every Guild Master in the country on a parade ground and beat every last one of them with a bat.

And he had been an instructor, no less.

It would not be an exaggeration to say that every mage from the early days of the Great Cataclysm had passed through his hands.

*His ability as a mage is at least A-rank, too.*

I could tell just by watching Im Chunsoo take his punishment without daring to make a peep. Butler Kim surpassed him in both seniority and skill.

There was probably also an elemental advantage between ice and fire. You could say Butler Kim was the one who taught Im Chunsoo and raised him to his current position.

*But…*

Why was someone that accomplished working as a butler?

I was sneaking a sidelong glance at Butler Kim when our eyes met.

“You seem to have a lot you want to ask.”

“To be honest, I do.”

I was too curious to stand it any longer.

Seeing my thoughts written plainly across my face, Butler Kim curled up the corners of his mouth.

“It’s a long story.”

“That’s fine. I’m on vacation, so I have plenty of time.”

“Ah, then this is a good opportunity to hear your story as well, Mr. Jin. I already have more than one or two questions myself.”

“Now that I think about it, it’s already dinnertime. Tomorrow is the last day of my vacation, so I have to sign a real-estate contract, too. Hahaha.”

“……”
## Chapter artifact 102

# Chapter 102

Everyone has their own area of expertise.

I knew the formations used at Gates, what to do when a crisis struck, and the weaknesses of various monsters like the back of my hand. My being clueless about legal matters was simply another example of everyone having their own specialty.

“Thank you for your hard work.”

“You too.”

The man in the angular horn-rimmed glasses was the legal scrivener I had hired to handle the real-estate transaction. Across from me, the homeowner and the licensed realtor were exchanging farewells and getting to their feet.

“Congratulations on the contract. A young man making it big.”

“Ah, yes. Thank you.”

As I shook hands with the homeowner, I realized something for the first time.

*This is my house now.*

And it was my family’s house.

A home we had reclaimed after no less than eleven years.



* * *



I looked around the cramped room.

The bed, whose springs had broken long ago. A small wardrobe that could barely hold a few outfits. A desk with its paint peeling off in places. A small TV sitting on top of it.

After packing up my clothes and assorted belongings, excluding the things I had to leave behind, I filled one cardboard box.

*Just one box.*

The past seven years were contained inside it. I was staring around the room with a strange tightness in my chest when a voice came from behind me.

“You leaving?”

I knew who it was without turning around.

He was someone I couldn’t leave out of my seven years.

“Yeah.”

“What about the house?”

“I found one, so I’m moving out.”

“Bastard, that was fast. Has your family already moved into the new place?”

“No. It’s still a secret. I’m planning to move in first and tell them after my sister finishes her college entrance exam.”

“Fair enough. She’s at an important stage.”

“Yeah. I need to remodel the place first, too.”

A brief silence followed. We were comfortable enough not to need conversation, the kind of people who could read each other’s thoughts from a look alone. But right now, neither of us seemed to know what to say.

“Hyung.”

“Hey, hey. Don’t set the mood.”

Jinho hyung slapped me hard on the back.

“It’s not like you’re an elementary school kid transferring schools. Just because you’re moving, you’re not going to stop seeing me, are you?”

“Of course I’ll see you. I definitely will.”

“Then it’s fine. Besides, I’m moving my stuff out by the end of today, too.”

“You are?”

“I told you last time. Don’t you remember?”

“Oh, right. You did.”

I had felt bad about leaving Jinho hyung alone in the goshiwon after all the years we had spent living together. Now I finally felt a little more at ease.

“Where are you moving?”

“Well, I ended up crashing at someone I know’s place. Where did you say the house you bought was?”

“Goyang. It’s only thirty minutes from here, so it’s not that far.”

“Goyang?”

Jinho hyung’s eyes widened.

“I’m in that area too, you punk!”

“Huh? Really?”

I was secretly pleased by the unexpected news. By now, his was a face I felt lonely not seeing for even a single day. If we lived close by, we could keep meeting often.

“Hyung, then where exactly is your address—”

Just as I was about to ask, the smartphone in my pocket rang. When I answered, a gravelly voice came from the other end.

—Hello, is this Mr. Jin Taekyung? I’m in front of the goshiwon right now.

“Ah, yes. Driver.”

It was the private moving-truck driver I had called in advance. I glanced out the window and saw a blue light truck waiting in front of the goshiwon.

—Do you have a lot of luggage? If anything’s heavy, I can help you carry it.

“No, it’s fine. I’ll carry it myself.”

I only had two things to move.

A cardboard box filled with small belongings, and…

*The capsule.*

Now that the Logout function had been activated, I no longer needed to use the capsule to travel between the Murim and modern worlds.

It had become nothing more than a bulky nuisance, but it held a more special meaning for me than anything else. That was the entire reason I had called a moving truck despite having so little luggage.

*What would have happened if I hadn’t had this capsule?*

I slowly ran my hand over its surface. The coldness of the metal and its rough texture traveled through my fingers.

This one old capsule had completely changed my life.

*Oh, right. There was also someone who played a major role in that.*

“Jinho hyung.”

“Yeah?”

I couldn’t help letting out a quiet laugh at his puzzled expression.

If Jinho hyung hadn’t gotten dead drunk that day, I never would have had a reason to enter the capsule.

“Never mind. It’s nothing.”

“You’re no fun. Anyway, shouldn’t you get going? There’s a truck waiting outside.”

“Yeah. Since you’re here, carry that box down for me. I have to carry the capsule, so I’m short on hands.”

“Uh, what?”

“What’s with that reaction? Can’t you carry one box for your little brother who’s moving away?”

“That’s not it… Ah, now that I think about it, I need to pack my own stuff too. Even if it’s a hassle, just make one trip back and forth. Well, good luck!”

“……”

Look at him slither away like a loach.

I watched Jinho hyung’s back as it slowly disappeared into the distance, then eventually picked up the box myself.

The moving driver, tired of waiting, honked the truck’s horn. The sound struck my ears.

Honk, honk!

“Yes, I’m coming down!”



* * *



“Are you a Hunter?”

The moving driver, who had been sneaking glances at me, finally spoke. The light truck, carrying the box and capsule, was heading toward my new home according to the navigation.

“How did you know?”

“You can tell at a glance. I used to be a Hunter, too. F-rank.”

“Oh, really?”

“I’m probably your Senior by training-center class. Ah, I’m not trying to pull rank. It would be ridiculous for a guy who quit after exactly one month and handed back his license to act like some old-timer.”

The driver continued, sounding as though he were simply airing a long-held grievance.

“Being a Hunter at the training center was manageable. Even though I was only F-rank, I took pride in becoming a Hunter. But the moment I joined a Guild after graduating, an accident happened.”

An accident at a Gate was synonymous with death.

Even if someone lost an arm or a leg, they could recover as long as they had enough money. Hunters didn’t call something that minor an accident.

“He was one of my training-center classmates, and he joined the Guild at the same time as me… Before I knew what was happening, he was dragged away and died just like that. I should have chased after him and saved him, no matter what it took, but I just couldn’t make myself move. After his funeral, I applied for retirement. Someone like me shouldn’t be going on raids.”

He tried to sound calm, but he couldn’t hide the tremor in his voice.

“I said something awfully ominous in front of a Hunter customer. It’s not exactly a pleasant story. Sorry about that.”

“Don’t worry about it.”

I understood how he felt.

I had experienced something similar. If I hadn’t felt responsible for my family, and if Jinho hyung hadn’t been there to comfort me, I might have retired two years ago.

*Then my life would have turned out completely differently.*

Being a Hunter was a brutal profession. The media praised them as humanity’s guardians and shields, but they lived with death always at their side.

—Turn right in fifty meters.

The driver flinched at the navigation’s voice, then muttered,

“Oh, come to think of it, this is a safe zone.”

“That’s right. Just keep going.”

“Ah, yes.”

The light truck arrived at its destination soon afterward.

It was a two-story detached house with a blue roof. A low stone wall surrounded a yard covered in grass. The house felt different from when I had first seen it a few days ago.

*It must be because it’s ours now.*

Our house.

The more I repeated those words in my head, the better they sounded. Of course, the fact that the house itself was beautiful probably helped.

“Wow… It’s a nice house.”

The driver climbed out of the cab and clicked his tongue in admiration. Praise sounded sweeter coming from someone else. No matter how hard I tried to suppress it, the corners of my mouth kept rising.

“You must be a successful Hunter. My dream was to live in a house like this.”

“Mine too.”

“Your wish came true. You must be happy.”

*Of course I was ecstatic.*

The driver continued exclaiming over the place, touching the stone wall and looking over the lawn, before asking,

“Would it be all right if I took a quick look inside? I can help move the capsule while I’m at it.”

“Sure. Go ahead.”

The moving driver became the new house’s first guest by accident as he climbed into the truck’s cargo bed.

He was going to move the capsule.

“That thing must weigh quite a bit.”

“It’s fine. I’ve moved plenty of them, so I know. Game capsules are all roughly the same weight.”

“No, it’s seriously heavy.”

I knew because I had lifted it myself earlier. It had been moderately heavy even for me, with my Strength stat in the triple digits. For the driver, it would be a different story entirely.

“Boss, I’ll move it myself.”

The driver hugged the capsule and grinned.

“Come on. You’re underestimating me. I may be an ex-Hunter, but something like this shouldn’t—nnngh!”

“Oh, wow.”

As expected of a former Hunter, he did manage to lift it in one go.

The only thing that had changed was that the smile had disappeared from his face.

“Go ahead and open the doors. Quickly!”

His voice suddenly urgent, I hurried over and threw open the front gate and the house’s entrance door. I had no idea why this had me feeling tense, too.

“I can carry it—”

“Move!”

“Ah, yes.”

He charged into the living room with the urgency of an alarm and shouted like he was screaming for his life.

“Which room?!”

“I was going to put the capsule upstairs…”

“What?!”

“…but just leave it in the nearest room.”

Fortunately, the door to one of the rooms was already open. With a heavy thud, the driver set down the capsule and began panting.

“Why… why is this… huff… so heavy?”

“……”

Hadn’t I told him it was heavy?



* * *



As soon as the moving driver left, I dropped onto the living room sofa.

It was one of the pieces of furniture the previous owner had transferred to me on the condition that I pay the remaining balance all at once.

*I’ll have to live alone for a few months.*

I had told my family that I was going back to Bucheon.

Until Hayeon finished her college entrance exam, I planned to eat and sleep here and commute to work.

*I need to remodel the house and buy a car, too. Ah, the Guild said they’d provide the car anyway, so I need to get my license first.*

There was a mountain of other things to do. But instead of feeling tired, I felt energized. These were all things I hadn’t been able to do before, no matter how much I wanted to.

It had only been a few months since I had done nothing but suffer while going back and forth between Gates and the goshiwon, yet so much had changed.

*You’ve come a long way, Jin Taekyung.*

One person suddenly came to mind.

A man who had always smiled like a boy despite his age. A man who had done his best for his wife and children and approached them like a friend.

*Dad, I bought a house. The place we used to live in was already gone. But I did well enough, right?*

I wanted to brag about it like a child, but the person who would have praised me had passed away long ago. All I could do was repeat, in my heart, words that could no longer reach him.

How much time passed like that?

When I came to my senses, it was already eight in the evening. The summer sun was slowly sinking.

*So this is how my last day of vacation ends.*

An entire week of vacation. It had been hectic because of everything involving the Sangdong Guild, but it was still the best rest I had enjoyed since becoming a Hunter.

Now it was time to return to my daily life.

*Precisely twelve hours from now.*

I lay flat on the sofa where I had been sitting. I briefly considered entering the capsule, but soon dismissed the thought.

After eleven years, I finally had a home of my own again. Just this once, I wanted to wake up in our living room instead of inside the stuffy capsule.

*Login.*

The System responded to my call.

Ding.

> **System**
>
> Would you like to connect to Murim?
>
> Y / N

Of course, my answer was yes.



* * *



A long time after Jin Taekyung lost consciousness, something no one could have expected was taking place in the room beside the front door.

Hissssss.

The door of the metal object that looked like a gigantic egg—the capsule—slowly began to open.

The first thing to emerge was a pair of feet.

Red letters were printed across a pair of long athletic socks that reached up to the calves.

**Hope Goshiwon Early-Morning Soccer Club**

Next came sweatpants rolled up halfway to the knees, followed by a pair of pale, skinny hands. The cover of the book he clutched tightly, as though it were scripture, gleamed in the sunset pouring through the window.

**Complete Mastery of the Civil Service Exam**

And finally, his face emerged.

After enduring several long hours of agony, he looked as haggard as Crown Prince Sado[^1] yet as relieved as Park Hyeokgeose emerging from an egg.[^2]

A parched voice slipped between his bone-dry lips.

“Is this my new nest…?”

As Seong Jinho gazed around the spacious room, a satisfied smile spread across his lips.

[^1]: Crown Prince Sado was an eighteenth-century Joseon royal who died after being confined in a wooden rice chest.

[^2]: Park Hyeokgeose is the legendary founder of the ancient Korean kingdom of Silla, said to have been born from an egg.
## Chapter artifact 103

# Chapter 103

Clatter, clatter.

The carriage lurched dangerously under the hands of an inexperienced coachman.

Though it was a fairly well-maintained makeshift road, the blizzard that had continued for several days had frozen the whip into an icicle, and it kept jabbing the horses in the rump.

And then, at last, trouble struck.

Thud!

Neigh!

The four fine horses, which had been moving their hooves surprisingly quickly despite the slippery snow, suddenly stopped.

“Gah!”

The coachman nearly pitched forward but somehow managed to regain his balance. Yet more than the relief of avoiding a fall, he was consumed by fear of what was about to happen.

*Please, Jade Emperor, Primordial Heavenly Venerable.*[^1]

Had his desperate prayer been answered? He cautiously peeked into the carriage, but the two young men were sitting there as though nothing had happened.

*Well, technically, one of them is sleeping.*

One young man was buried in fur until only his forehead showed. Perhaps someone had pressed a sleep-inducing pressure point, because he showed no sign of waking. The other sat cross-legged, utterly absorbed in circulating his qi.

Sssssip. Hooooo.

If anyone had witnessed the scene, they would have been surprised twice.

Once by the young man’s handsome features, and once again by the formless qi of a Peak master pouring from his body.

Hyuk Mujin, the coachman, thought he had grown somewhat accustomed to him by now. But he was no different.

*What kind of bullshit is this?*

His envy had gone beyond envy and reached the point of anger.

A handsome face and genius-level martial talent. If he possessed even one of those things, he would have no other wish in the world. But that young man, Jin Mukyung, had both.

*And there’s even another one.*

The same went for the other young man, Jin Taekyung, who had said he would circulate his qi only to fall into a deathlike sleep.

No, he might even be a greater monster than his older brother, Jin Mukyung.

After all, only a few months ago, he had been a Third Rate wastrel who did nothing but visit pleasure houses. Now, he was the Sleeping Dragon of Shanxi.

*How can two brothers be this alike?*

Their handsome features had been inherited in full from their mother, who had once been known as Shanxi’s foremost beauty. Their talent was so extraordinary it inspired jealousy.

And lastly…

*They were both assholes.*

Hyuk Mujin glared at the two brothers in turn.

One had taken all the fur for himself to keep warm, whether his subordinate froze to death on the driver’s bench or not. The other had given him hell for a full two hours because he couldn’t even drive a carriage properly, and now he was comfortably circulating his qi.

*They’re perfectly matched.*

They should have been difficult to rank because of their excellence, but these brothers were the opposite.

Hyuk Mujin was carefully considering which brother had the worse personality when it happened.

“Hey.”

A chilly voice. Formless qi poured from the eyes of the man who had just finished circulating his qi, binding Hyuk Mujin in place.

“What are you doing? Why aren’t you driving?”

“A problem, ahem, came up for a moment.”

“What problem?”

“Well…”

What would happen if he told him that the horses had gotten angry because the frozen whip kept stabbing them in the rump? Hyuk Mujin made the wise choice.

“My body is frozen, so I can’t drive.”

He also wanted to take a break. Didn’t the backside that had been suffering on the driver’s bench deserve some rest?

But Jin Mukyung’s response was simple.

“Hand.”

“Pardon?”

“Give me your hand.”

Hyuk Mujin reflexively held out his hand like a mutt. Jin Mukyung grabbed it and casually said,

“Bear with the heat.”

Before Hyuk Mujin could understand what he meant, an enormous surge of qi traveled through his fingertips. The fire qi was so intense that his entire body seemed to catch fire, and his breath caught in his throat.

*Gah!*

The shock was too great for a scream to come out. It lasted no more than an instant, but Hyuk Mujin stood there with his mouth hanging open, his body trembling violently. He did not even realize that Jin Mukyung had already let go of his hand.

“How is it? Better?”

Only then did Hyuk Mujin come to his senses. He barely managed to open his mouth.

“What, what was that just now?”

“A simple type of heat-yang technique.”

“That didn’t look simple… I thought I was going to burn to death.”

“Really? I suppose I’m still unskilled at it, since I only learned it superficially.”

Jin Mukyung’s offhand tone left Hyuk Mujin dumbfounded.

*Why would you use something you only learned superficially on me…?*

Hard to tell the brothers apart? The older brother won the contest by a mile.

Jin Taekyung had beaten him up before, but he had never tried to burn him to death with heat-yang qi.

“Now go drive the carriage. We still have a long way to go.”

“…”

He hadn’t merely warmed up. He had been roasted. But the effect was undeniable.

“Then I’ll get us moving again.”

When Hyuk Mujin returned to the driver’s bench with his body blazing hot, Jin Mukyung turned his gaze forward.

Jin Taekyung was buried in fur so thoroughly that it was difficult to tell whether he was a bear or a person.

*He said he was going to circulate his qi, but he’s sleeping like a log.*

Mukyung had thought he was talking nonsense, but he hadn’t expected him to sleep so openly. A martial artist was supposed to constantly ponder martial arts and train without rest.

Jin Mukyung shouted with a stern expression.

“You rascal! Will you not get up this instant?”

His voice reverberated so loudly that Hyuk Mujin on the driver’s bench and even the horses flinched. Yet Jin Taekyung himself did not stir.

Snnn. Snnn.

“You rascal!”

Jin Mukyung sprang to his feet and struck his younger brother’s forehead with his palm. With a sharp smack, the skin turned bright red.

*Let’s see if this wakes you up.*

Smack, smack, smack.

Snnn. Snnn.

“…”

His forehead had turned red enough for a lump to rise and look ready to burst, yet he did not twitch.

Jin Mukyung was overwhelmed by shock. Even a commoner without a shred of internal energy should have screamed awake from this. Yet this guy, supposedly a top-tier First Rate martial artist and the Sleeping Dragon of Shanxi, did not move an inch.

Jin Mukyung had never seen anyone so defenseless in all his life.

*And that guy is my younger brother.*

Just as the training he had put Taekyung through over the past several days was beginning to feel like a complete waste of time—

“Hmm.”

The eyes that had seemed destined to remain closed forever slowly opened.



* * *



Before I even opened my eyes, I realized that I had returned to Murim.

The cool air against my cheek. The rattling interior of the carriage.

And pain.

“…”

Wait. Why was I in pain?

When I opened my eyes, a fairly familiar face was looking down at me.

*Jin Mukyung.*

I ignored his expression, which seemed to say *What kind of person is this?*, and straightened my slumped body. Only then did I identify the source of the pain.

“Ow.”

My forehead. When I carefully touched it, I felt a lump and the heat radiating from the surrounding skin.

*What the hell?*

How had I gotten a lump on my forehead?

For a moment, I wondered if I had slammed my head against the wall. But with the bones, muscles, and toughness I had steadily built up, that wouldn’t even leave a scratch.

*This was a deliberate hit, plain and simple.*

Fortunately, there were two suspects right in front of me.

Jin Mukyung and Hyuk Mujin. Even a three-year-old could tell who the culprit was.

“What did you do while I was asleep?”

“While you were sleeping? Didn’t you say you were circulating your qi before that?”

“…”

*I did?*

It had happened long enough ago that I couldn’t even remember it. But that wasn’t important right now.

“You hit someone while they were sleeping?”

“You looked so pathetic that I did. A martial artist like you was sleeping away instead of training.”

“You call yourself a martial artist and attack someone who’s defenseless?”

“Then shall we get off right now and have a bout? Like true martial artists?”

We both sprang to our feet and glared at each other without waiting for the other to move first. Jin Mukyung spoke in an ominous tone.

“Hyung Mujin.”

“It’s Hyuk Mujin. Second Young Master, please.”

“Stop the carriage.”

“…”

“Yes, sir.”

The carriage slowly began to decelerate. Now it was my turn. I met his gaze and opened my mouth.

“Hyuk Mujin.”

“Ah, why me this time, Squad Leader?”

“Keep going.”

“Haah, this is driving me crazy.”

The carriage began to speed up again. As I slowly sat back down, Jin Mukyung asked with an incredulous expression,

“Didn’t you just suggest that we have a bout like martial artists?”

“What a joke. The mission comes first, and fighting comes after. And…”

“And?”

“I never said we should fight. I only said you were underhanded.”

“…”

I had said it as confidently as possible, but there was no hiding how lame it looked.

I snuck a look at Jin Mukyung’s Level window.



> **System**
>
> **Lv. ??? Jin Mukyung**

*Right. Come on, fighting him the moment I got back would be a bit much.*



* * *



*Check the Quest window.*

Ding.



> **System**
>
> **Quest**
>
> **Yesterday’s Enemy, Today’s Ally**
>
> Now that all the truth has been revealed, the Mount Heng Sword Sect is no longer an enemy but an ally you must join forces with. Invite them to the Jin Family of Taiyuan for the upcoming Lunar New Year.
>
> **Grade:** First Rate
>
> **Restriction:** Jin Taekyung
>
> **Mission:** Deliver the invitation (Incomplete)
>
> **Reward:** ???
>
> **Failure:** None

I took one more look at the last Quest I had received.

It was an easy mission. The Quest’s Grade wasn’t particularly high, and there was no penalty for failure. I simply had to deliver the invitation to the Mount Heng Sword Sect.

*The Mount Heng Sword Sect…*

The current Mount Heng Sword Sect had been reduced to its bare bones. Once Lee Seogeun was poisoned and the pillar known as Lee Cheonbaek fell, its collapse had been swift.

*The battle at Eight Spring Gorge had been the fatal blow.*

They say words without feet can travel a thousand li.

That day’s battle, watched by countless eyes and ears, spread rapidly through messenger pigeons and word of mouth. With nearly all its main forces gone, the Mount Heng Sword Sect became easy prey for someone.

*Wandering martial artists. And mounted bandits.*

They said as many as two hundred attackers had suddenly raided the Mount Heng Sword Sect. After two days and nights of fighting, the attackers were driven off. Lee Seogwang, who had remained at the sect after being placed under disciplinary confinement, ultimately fell in battle.

The Mount Heng Sword Sect needed a new rallying point, and one person emerged.

*Lee Seowol.*

Lee Cheonbaek’s last surviving descendant, and the current Sect Leader of the Mount Heng Sword Sect.

We had to deliver this invitation to her.

The problem was…

*We had a thoroughly uncomfortable relationship.*

Actually, “uncomfortable” was a softened description from my perspective.

In a way, the two of us had been at the very starting point of all this.

*I think it was right after I came out of the training cave.*

I remembered Wipeng’s words exactly, down to the last syllable.

“Is it true that you tried to force yourself on the daughter of the Mount Heng Sword Sect?”

These days, no one was unaware of my innocence. But back then, I had been treated like the worst bastard under heaven.

Lee Seogeun, who had come to pressure the Jin Family of Taiyuan with fabricated evidence, was poisoned on his way home, and that was the beginning of everything.

*Only a month or two has passed.*

The Third Rate wastrel despised by his own family had become the Sleeping Dragon of Shanxi, while the woman whose name I hadn’t even known was now the new Sect Leader of the Mount Heng Sword Sect.

We had both gone through so many changes in the meantime that, in a sense, we had something in common.

*Our positions, however, were very different.*

The Jin Family of Taiyuan was now, by everyone’s admission, the foremost family in Shanxi.

The Mount Heng Sword Sect, on the other hand, was nothing more than an empty shell. This invitation was, in truth, almost a proposal that they surrender and come under the Jin Family of Taiyuan.

I would have to experience it firsthand to know how Lee Seowol would react.

*I just hope she doesn’t suddenly stab me.*

Just as I closed the Quest window, sunlight streamed in and the sound of a boisterous crowd drew closer. Hyuk Mujin looked at me, his face flushed with excitement.

“We’re at Honju.”

We were now only two days away from her.

[^1]: The Jade Emperor and Primordial Heavenly Venerable are major figures in Daoist cosmology.
## Chapter artifact 104

# Chapter 104

A city that never sleeps.

That was my first impression of Honju. Even though it was a dark night, the streets lined with countless pavilions were bright with lanterns, and the sound of people laughing and talking never stopped.

*More than I expected.*

It wasn’t quite as lively as a modern city at night, but it was still a well-developed commercial district.

How should I put it? Maybe it had a unique charm born from the culture of this era.

*Oh, that looks pretty cool.*

Unlike me, who was gazing out the window with interest, Jin Mukyung looked unimpressed.

“It’s noisy. We would be better off camping outdoors.”

“Come on, we’re only passing through. Why are you complaining?”

Hyuk Mujin’s cheeky reply made Jin Mukyung’s eyebrow twitch.

“If you had driven the carriage properly, we would have passed through a long time ago.”

“If the Second Young Master hadn’t chased away the coachman in the first place…”

“What?”

“Nothing. I’m the one who deserves to die.”

Stung by the sharp glare, Hyuk Mujin began rambling out excuses.

“Still, we’re representing the family. Shouldn’t we eat something good at a good place? And let the horses rest, too.”

“Food need only satisfy hunger. Besides, who told you to do any of that?”

“The Lesser Family Head.”

“……Brother?”

“Yes. He repeatedly told me that since we were traveling without any attendants, we should at least take care of our meals and lodging somewhere decent.”

*I should’ve been that bastard’s older brother.*

Jin Mukyung had a terrible personality and never listened to anyone, but he was completely helpless in front of his only older brother. After hesitating for a moment, he sighed.

“Fine. Just hurry up and go.”

“Yes, sir.”

Hyuk Mujin had finally won one battle. With the corner of his mouth twitching, he began driving the carriage.



* * *



The carriage stopped in front of a massive wooden building that stood four stories high.

The Phoenix Inn. The signboard, written in elegant calligraphy, was striking.

“This place looks incredibly expensive.”

“Of course it is. This is where the Young Masters of the Jin Family of Taiyuan will be staying. The Lesser Family Head told me repeatedly—he said we had to choose the absolute best!”

“……”

*He’s awfully excited when it’s someone else’s money.*

I shook my head and climbed down from the carriage. A shopkeeper who looked about middle-school age came running over and bowed at the waist.

“Welcome!”

For someone so young, he had quite a bit of service spirit. Hyuk Mujin stepped forward and asked in a weighty voice,

“Do you have any rooms available?”

“Of course, sir. What kind of room would you like?”

“Give us the largest one.”

“Ah, do you mean the private residence?”

The shopkeeper looked over our group. All three of us were dressed in martial artist’s robes, so he chose his next words carefully.

“I’m sorry, but half the fee for the private residence must be paid in advance.”

“Ha! What a shrewd little bastard.”

Hyuk Mujin deliberately hardened his expression and pulled a heavy money pouch from inside his robes. It seemed to be the money Jin Wikyung had given him for expenses.

“Fine. How much?”

“It’s fifty nyang for one day, sir.”

*How much was fifty nyang?*

I had never used money here and didn’t know how the currency worked, so I could only leave it to Hyuk Mujin.

*Well, he’ll handle it somehow.*

I glanced to the side. Jin Mukyung seemed to be thinking the same thing as me.

Then again, he was a martial arts fanatic and the young master of a wealthy family. His background had nothing to do with understanding money.

The reaction of Hyuk Mujin, however, was different.

“What? How much?”

“Fifty nyang, sir.”

“……Iron coins?”

“Excuse me?”

The shopkeeper looked Hyuk Mujin up and down, then let out a quiet laugh.

“Would you like me to change your room?”

“……!”

It was an unmistakable laugh of mockery. Hyuk Mujin’s lips trembled, but soon he burst into hearty laughter.

“Ha ha ha! That’s some impressive business sense for a little brat. Change it? Don’t be ridiculous. Hurry up and show us to the private residence.”

“But you’ll have to give me twenty-five nyang first.”

“You little—!”

“Whoa!”

The shopkeeper flinched at Hyuk Mujin’s show of defiance.

That guy only got bullied when he was with us. Despite appearances, he was a First Rate martial artist and a candidate to become the next Master of the Gatekeeper Pavilion of the Jin Family of Taiyuan.

A commoner who knew nothing about martial arts—and a child barely into his teens at that—could only be frightened.

“I-I’ll show you the way right away!”

We followed the thoroughly tense shopkeeper to the private residence. Along the way, we saw a garden that was, with a little exaggeration, the size of a soccer field, as well as a pond where carp swam.

The private residence was divided into three large rooms and decorated with objects that looked expensive even at a glance.

“Wow, this room is nice.”

Jin Mukyung nodded as well.

“Not bad. At this size, there will be no problem training here.”

“……”

*Is martial arts the only thing in that guy’s head?*

While I was walking around the private residence and looking around, Hyuk Mujin returned after paying for our stay.

“Are you two not going to eat?”

“I’m fine. Enduring hunger is a form of training, too.”

Jin Mukyung answered firmly, then left the private residence and disappeared into the garden.

“What about the Squad Leader?”

“Do I look like that lunatic to you? I’m starving to death. Let’s hurry up and order everything they have.”

*Was it my imagination, or did Hyuk Mujin’s face suddenly darken?*



* * *



The Phoenix Inn was one of Shanxi’s most famous establishments. There were three reasons for that.

First, it was large enough to accommodate hundreds of people. Second, its dishes were prepared by a former imperial-court chef. And third was the beauty of its female proprietor.

As a result, customers never stopped coming to the Phoenix Inn, despite its high prices.

Of course, Hyuk Mujin, who had been born into a family of tenant farmers, had never even dreamed of visiting a place like this.

*If someone like me doesn’t come here at a time like this, when will I ever get the chance?*

Just an hour ago, Hyuk Mujin’s mood had reached its peak. A fine room, delicious food, and even the beauty of the proprietress, whom people said could only be seen on lucky days.

*And I get to enjoy all of this with someone else’s money!*

*Is this a dream or reality?*

Then he heard the price of one night in the private residence and thought about it again.

*Is this a dream or reality?*

The same words. A completely different feeling.

He would have preferred it to be a dream, but by the time he came to his senses, it was already too late. He had fallen completely for the shopkeeper’s mockery and even paid the advance fee. It was all over.

*All I was given for expenses was fifty nyang.*

Fifty silver nyang.

Considering that a family of four generally lived on only a little more than ten silver nyang a year, it was an enormous amount of money.

The problem was that the Phoenix Inn’s prices were on an entirely different level from ordinary prices.

*I gave them twenty-five nyang in advance, so I have exactly half left.*

Even that money would be gone once the sun rose. Hyuk Mujin was about to spend all the expense money Jin Wikyung had given him on a single night’s lodging, and sweat dampened the small of his back.

*If that damned shopkeeper hadn’t laughed at me…*

Regret always comes too late.

Hyuk Mujin quickly began calculating on the abacus in his head.

*The expense money is gone. But I brought some emergency savings just in case, so maybe I can somehow manage.*

Five silver nyang. It was everything he had saved up until now. He had brought it in case something happened, but he had never expected to actually use it.

*If I don’t indulge too much, I should be able to hold out until we return.*

But there was one thing Hyuk Mujin had failed to consider.

Jin Taekyung’s appetite.

Slurp. Gulp. Munch, munch.

“Wow, this really melts in your mouth.”

“……”

Osmanthus chicken, fish-fragrant shredded pork, pork with preserved mustard greens, scallion tofu, Kung Pao chicken… Each time one of those dishes—or one of the more than ten others—arrived at the table, Jin Taekyung’s hand moved like lightning.

“Wow, this is really good. The meat is so juicy.”

“……”

“You’re not eating? Then I’ll eat the rest, too.”

“……”

“Wow, this broth is incredible.”

“……Please, eat as much as you like.”

At some point, a single tear rolled down Hyuk Mujin’s cheek.

*The dishes that have come out so far have already cost five silver nyang.*

His last hope was finished. Judging by the way things were going, that pig would eat another twenty plates.

Hyuk Mujin wanted to smash the pig-like bastard over the head with a plate, but he held himself back. He didn’t want to lose his life after losing his entire fortune.

*Jade Emperor, Primordial Heavenly Venerable. Please, stop that bastard.*

It was just as he was cursing the heavens.

Crash!



* * *



If the most difficult things about living in Murim were ranked, survival would come first and food would come second. For some reason, every dish was spicy, salty, and greasy, leaving me craving soup at every meal.

In that sense, the dish that had just been placed on the table held a special meaning.

*Chicken-and-corn soup.*

It was a kind of corn soup with egg beaten into it until it was silky smooth.

I lowered my head slightly and smelled it. The distinctive savory scent of corn lingered at the tip of my nose.

*Yes, this is it.*

A smile spread across my face on its own. My stomach had already begun to feel greasy. If I settled it with the chicken-and-corn soup, I could probably clear another ten plates.

*All right, then, now…*

Just as I grasped the hot ceramic bowl with pleasant anticipation—

Crash! Clatter, clatter!

“……Huh?”

It happened in an instant. The liquor bottle that had shattered in the middle of the table broke into hundreds of ceramic shards that flew in every direction.

And along with them came the small amount of liquor remaining inside the bottle.

Pitter-patter.

I was drenched by the sudden shower and lost all ability to speak.

*How could this happen?*

The chicken-and-corn soup I had been eagerly awaiting—the warm, savory broth that would gently soothe my stomach—was no longer there.

What now filled the ceramic bowl was nothing more than food waste mixed with liquor and pieces of pottery.

Sitting across from me, Hyuk Mujin stared with his mouth hanging open.

“Oh, Jade Emperor. Primordial Heavenly Venerable.”

I ignored his nonsense and slowly turned my head toward the direction from which the bottle had flown.

Five men were looking this way and snickering.

“Oh, Brother. Sorry about that.”

“Who can you blame when a hand slips? We can just order you another one.”

“Hey, don’t talk crazy. Didn’t you see how much that guy’s been eating?”

I watched them chuckle among themselves, then crooked a finger.

The one who had apologized first—he was the bastard who had ruined my soup.

“What, you want me to come over?”

The man let out a quiet laugh, then stood and strode toward us.

His martial artist’s robes were stained with the smell of sweat and blood, and a curved saber hung at his left hip. That was where his confidence came from.

*All right. Let’s deal with this rationally.*

I calmly opened my mouth.

“The ancient sages said that even a dog shouldn’t be disturbed while it’s eating. Apologize properly and order the food again. Starting with the chicken-and-corn thoup.”

“Well, listen to the little brat lisp.”

“What about the apology?”

“Come on, stick out your tongue. I’ll pull it out for you.”

When he grinned, I saw teeth that had rotted black.

The horrific stench of his breath wiped away my appetite. I supposed I would have to eat the thoup later.

“Open your mouth. My fist is going in.”

At the same time as I spoke, I drove my fist into his face.

Crack!



* * *



There were three reasons the Phoenix Inn was famous.

But the third reason was why people—and men in particular—came here in such great numbers.

The beautiful proprietress, whom one could only meet on a lucky day.

And today was that day.

“It’s noisy.”

The proprietress’s clear yet languid voice was not a soliloquy. The disappearance of the presence outside the door was proof of that.

A moment later, a quiet voice came from beyond the door.

“A fight has broken out between martial artists.”

The proprietress clicked her tongue softly before speaking.

“Did anyone die?”

“One man subdued all six of the others.”

“Who was he, and where was he from?”

“He’s the Sleeping Dragon of Shanxi.”

The proprietress laughed without making a sound.

“What a welcome name. I should go see his face after all this time.”

She had been lying at an angle, but now she sat up. Moonlight filtering through the window illuminated a long-stemmed tobacco pipe.

# Checkpoint Review — 885–889

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

# Chapters 885–889

## Plot

Taekyung discovers that laborers carrying banquet supplies are assassins working with Eunuch Ma. Told to return and wait, he instead encounters So Gyo in an abandoned forbidden ground where the late Emperor and his relatives were once confined. So Gyo reveals that she is searching for someone and can read the instability in Taekyung’s internal energy. When he refuses to yield, she attacks; Taekyung withstands her pressure and strikes her, but appears badly weakened as a streak of light approaches.

Baek Yeon arrives with So Gyo. Taekyung stops fighting when So Gyo says Prince Shangshan is still under the Emperor’s control and that she has a mission to keep Taekyung alive. He infers that the Lord of Heaven wants him alive, returns Baek Yeon’s weapon, and withdraws. Afterward, So Gyo tells Baek Yeon that Taekyung may be the person she seeks—the one foretold by “that person”—but that she must confirm it. She retrieves two curved sabers from a flower garden and says the coming battle may surpass the one fought more than a decade ago. With the banquet three days away and Shangshan in enemy hands, Taekyung slips into the rain to find Jeok Cheongang, but Jeong Hogun blocks his way at the Outer Palace.

## Continuity

- The imperial banquet is three days away. So Gyo expects the coming battle to be fiercer than the one over a decade ago.
- Assassins disguised as laborers are inside the palace, working with Eunuch Ma; their mission is unknown.
- So Gyo is searching for someone and suspects Taekyung may be that person. The identity of the person and the foreteller she calls “that person” remain unknown.
- So Gyo says only she and the Emperor know the secret she withheld from Baek Yeon. She suggests Jeok Cheongang joining Taekyung’s side might be preferable, but does not explain why.
- So Gyo’s identity and allegiance remain unconfirmed. Taekyung suspects a connection to Dark Heaven; her mission to keep him alive and his inference that the Lord of Heaven wants him alive do not establish who she serves.
- So Gyo recovered two matching curved saber-like objects buried in a flower garden and wears one at each hip; their purpose is unknown.
- Prince Shangshan remains in the Emperor’s control. Taekyung believes the confrontation is unavoidable and is trying to reach Jeok Cheongang.
- Taekyung encounters Jeong Hogun while trying to pass the Outer Palace guards. His condition is poor after the fight with So Gyo.

## Translation Decisions

- Retain “that person” for 그분; the foreteller is not identified.
- Render 곡도 descriptively as “curved saber,” not as a proper name.
- Retain “Golden Dragon” for Baek Yeon’s weapon and “Ten-Thousand-Year Cold Iron” for 만년한철.
- Continue to use “Hongmen Banquet” for 홍문연.

## Durable state

{
  "active_continuity": [
    "The imperial banquet is three days away; So Gyo says the coming battle may be fiercer than the one over a decade ago.",
    "So Gyo believes Jin Taekyung may be the person she seeks and the person foretold by “that person,” but has not confirmed it. She says only she and the Emperor know the secret she withheld from Baek Yeon.",
    "So Gyo recovered two matching, curved saber-like objects buried in the flower garden and wears one at each hip.",
    "Prince Shangshan remains in the enemy’s grasp; Taekyung believes the confrontation cannot be avoided and slips toward the Outer Palace to reach Jeok Cheongang.",
    "Taekyung encounters Jeong Hogun while attempting to pass the guards at the Outer Palace."
  ],
  "continuity_sources": [
    889
  ],
  "open_questions": [
    "Who is the person So Gyo seeks, and who foretold them?",
    "What secret do So Gyo and the Emperor share, and why would Jeok Cheongang joining Taekyung’s side be preferable to So Gyo?",
    "What will happen at the imperial banquet, and can Taekyung reach Jeok Cheongang?",
    "Who is So Gyo, and whom does she serve?",
    "What is the purpose of the two curved saber-like objects So Gyo recovered?"
  ],
  "safe_through": 889,
  "temporary_decisions": [
    "Render 곡도 descriptively as “curved saber”; do not treat it as a proper name.",
    "Retain “that person” for 그분; the foreteller is not identified in this chapter."
  ],
  "version": 1
}

## Reading copies

## Chapter artifact 885

# Chapter 885

Naturally, there was no moving reunion beyond that.

We’d only been apart for a few days, and it wasn’t exactly a situation where we could openly acknowledge each other.

*There’ll be a chance soon enough.*

I crossed the sprawling grounds of the imperial palace, vast enough to deserve the word, and looked around at everything.

The layout and locations of the buildings. The number of Imperial Guards visible everywhere. Even the outsiders who’d come in to prepare for the banquet.

And in the process, I noticed something I hadn’t expected.

*What’s that?*

My steps stopped as the question crossed my mind.

I narrowed my eyes and watched a group carrying boxes just ten paces ahead.

“Hold on. Take that this way.”

“One, two. Hup!”

“Those are offerings from Grandee Guanglu. They’re worth more than all your lives put together, so handle them carefully.”

“Yes, of course. We’ll be careful.”

Their clothes were clean, but old, with patches here and there. The wrinkles on their faces were etched with the hardships of life.

Even as sweat poured down their faces, they bowed and smiled at a man who looked like a low-ranking official, then kept hauling the piles of goods without pause.

Just like any other laborers, living from one day’s wages to the next.

But…

*They’re different.*

I could feel it.

A faint sense of something off about them.

It was an instinct honed through countless real battles and brushes with death—so subtle that I wouldn’t have noticed it if I hadn’t reached my current realm.

*They’re not ordinary laborers.*

There was only one reason I’d think so when I couldn’t sense any internal energy from them.

*The stench of blood.*

A brand that wouldn’t come off, no matter how many times they washed.

The stench of blood seeped from their bodies, not entirely masked by the sour smell of sweat or the mustiness of their old clothes.

*Martial artists?*

The question crossed my mind, but I wasn’t sure yet.

Were they martial artists who’d voluntarily taken Energy-Dispersing Poison to hide their internal energy? Or was it just my imagination, brought on by the fact that I had to be sensitive to everything happening around me right now?

*I’ll know if I check.*

I moved closer to get a better look at them. Or rather, I was about to.

Until a cart, unable to bear its own weight, began to tip toward me.

Crack. Crash!

Wooden splinters flew everywhere with a heavy crash. The official clutched his head as silver yuanbao and all kinds of ornaments spilled out of the boxes.

“What the hell do you think you’re doing!”

“I-I’m sorry. This old servant loaded the cargo incorrectly, and…”

“You stupid old fool! Forget apologizing and hurry up and pick everything up! If even one item is damaged, you’ll pay for it!”

“Yes, yes. Understood.”

The one who bowed so low he looked ready to snap toward the official as he stormed off was an old man with graying hair.

He was small and emaciated, like a tree that had lost its vitality. He limped over and looked at me with frightened eyes.

“Are you all right, sir? Did this old man’s mistake hurt you at all…?”

A mistake. A mistake, huh?

I thought to myself, then answered calmly.

“I’m fine. I’m not hurt.”

“Phew. What a relief.”

“Indeed. That cart looked perfectly fine, then suddenly toppled over. It startled me, too.”

At the smile on my lips, the old man looked flustered and bowed again.

“This old servant apologizes once more.”

“Don’t mention it. Anyway, want me to help? Looks like there’s a lot to pick up.”

“Oh, how could I let you do that? It’s already more than I deserve that someone of your standing would speak so politely to me…”

“I’m not someone of high standing. I’m sure you already know that.”

For the briefest moment.

A strange current passed among the laborers who’d come over to deal with the mess. Then, in a silence so short no one else would have noticed it, the old man slowly spoke.

“If you’d help us, we’d be very grateful.”

“Then that’s settled.”

I nodded, squatted down, and began picking up the things that had spilled.

Quietly, without saying anything, as if that had been my only reason for coming over. But I kept my eyes fixed on the old man.

In the end, he was the one who broke the silence, not me.

“How did you know?”

At his admission, I let out a short laugh.

“You’re quick to admit it.”

“I can’t stand wasting time. Especially not for an old man like me, who doesn’t have much time left.”

“Are you a martial artist? Who do you belong to?”

“It’s rude to answer a question with a question. Remember that.”

“What are you—oh.”

“How did you know? I was certain no one could tell.”

The old man’s eyes gleamed fiercely, as if he’d never played the humble laborer. I gave him a brief answer.

“The stench of blood.”

The old man wasn’t surprised. He frowned, sniffed at different parts of his body, then smacked his lips and said,

“My nose must be going bad with age. All I smell is old-man stink.”

“That’s there, too. Since we’re on the subject, let’s put a little more distance between us. It’s hard to breathe.”

“I thought you were just skilled in martial arts, but you’ve got a hell of a nose, too.”

“Do you know me?”

“I do. Information is essential for this sort of thing. But even if I hadn’t heard anything about you beforehand, I’d have figured it out right away.”

“How?”

“The stench of blood.”

For a moment, I was at a loss for words. Then the old man continued.

“Didn’t you know? You reek of blood, too. Enough that it wouldn’t be strange to call you a Killing Ghost instead of a Divine Dragon.”

“……!”

“Ah, there’s no need to look at me like that. It’s a compliment, as far as I’m concerned. You know what they say.”

The old man grinned. A terrible stench poured out from between his blackened, yellow teeth.

“Kill a hundred and you’re a Killing Ghost. Kill a thousand and they call you a hero. Kill ten thousand and you become… a king.”

My mouth felt gritty, like I’d been chewing sand. I stared at the old man, whose breath stank right in my face.

*What the hell is this?*

Something felt wrong. Just standing in front of him sent a chill down my spine.

Even in Murim, where every sort of person crossed paths, you didn’t run into people like this often.

“Who are you—or rather, who are all of you?”

“You call a Senior of Murim ‘you’? Does your master know his Disciple is so rude?”

“Someone I met recently told me that answering a question with a question is rude.”

The old man stared at me with wide eyes, then burst out laughing.

“Well, you got me good.”

“Now that you’ve had your laugh, answer me.”

“You know already, so why ask? Those children and I are martial artists, just like you.”

“I think you’re very different, personally. Am I just imagining things?”

“No need to worry. We may not belong to the Murim Alliance, but we’re comrades in the same boat.”

“What does that—”

As my voice trailed off, an idea suddenly struck me.

“No way…”

“Eunuch Ma. Is this enough of an answer?”

“……!”

“Everyone has a place and a role. You should go back and wait for your moment. If you draw any more attention, it’ll become a nuisance.”

With that, the old man rose to his feet and bowed to me.

“We’ll take care of the rest, so you can stop now, sir. We’ll handle everything from here.”

It was an unmistakable dismissal, as well as a performance for any watchers keeping an eye on us from somewhere.

No, calling this a simple performance would be an insult.

The old man was a laborer through and through, every movement perfectly in character.

“Please get back safely, sir. Then this old servant will be off…”

Step. Step.

As I watched the old man limp away with a box, I finally felt I understood who these people disguised as laborers were.

Even in this vast Murim, where countless different sorts of people roamed, there were only a few groups who could move around while hiding themselves so perfectly.

And then there was that overwhelming stench of blood.

At that moment, only one word came to mind.

Assassins.

* * *

Even among martial artists, with their hordes of lunatics and people who had no sense of self-preservation, there were certain sorts they’d always avoid. A few members were fixtures on that list.

Killing Ghosts. Fiends. Suspicious old men and beautiful women wearing veils, and so on.

Like Japan’s legendary first-string team, they were never easy to find. But martial artists with even a shred of common sense, and any hope of living long enough to retire in a village for the elderly, knew to steer clear of them.

Why? Simple.

Even messing with them—and sometimes just being near them—made a sense of doom creep over you.

And among them, right after Killing Ghosts and fiends, one of the top three most avoided professions was the assassin.

To put it bluntly, they were the three kings of utter bastards.

No one disputed it or questioned it.

In fact, quite a few people put assassins at the top of that list. And there was someone around me who’d given me similar advice.

It was a little ironic that the kindly advisor’s sobriquet was none other than the Slaughter Saint.

*Actually, “ironic” doesn’t even begin to cover it. It was practically black comedy.*

I muttered to myself and kept walking.

It suddenly occurred to me that I didn’t know where this road led. But that thought was quickly buried by the conversation with the Slaughter Saint that came to mind.

*“A Killing Ghost or a fiend would be better. But no matter what the circumstances, stay away from assassins.”*

*“Why? Aren’t they all the same kind of lunatic?”*

*“Your head’s as solid as a rock, so I’ll give you a simple example. Say you’re eating in an inn and a Killing Ghost or fiend suddenly walks in. What would you do?”*

*“That’d be fucking awful. I’m trying to eat.”*

*“Well… you’re not wrong, but think a little more deeply before you answer.”*

*“You called me a blockhead. I don’t want to think, so could you just tell me?”*

*“In case you’ve forgotten, I can break rocks with my fist. A head made of stone is no exception.”*

*“I see I was too quick to answer. Could you give me a moment?”*

*“You’ve gotten a little smarter.”*

*“Thank you. Hmm. First, I’d watch the Killing Ghost or fiend, then carefully…”*

*“Right. The first priority is to carefully get out of there.”*

*“No. I’d hit them first.”*

*“……What the hell did the Fire King teach you?”*

The Slaughter Saint had looked up at the sky and sighed, then hit me on the head a couple of times with his rock-breaking fist before saying,

*“To put it more simply, Killing Ghosts and fiends are no different from madmen who don’t think about the consequences.”*

*“Ow, my head. Doesn’t that make them even more dangerous? Like you said, if I ran into one in an inn, the whole place could turn into a sea of blood.”*

*“But you’d still have a decent chance of surviving.”*

*“Well, sure, if your martial skill is high enough…”*

*“It has nothing to do with skill. You can never predict people like that. They kill or spare people on a whim.”*

*“They really are crazy.”*

*“But what do you think an assassin would do?”*

*“An assassin… Oh.”*

*“Looks like you’re finally getting it. Exactly. They’re not just ordinary lunatics. They’ll do anything to assassinate their target. That’s why an assassin can kill an expert a level or two above them.”*

*“They’ll do anything to assassinate their target…”*

*“That’s why you need to be most careful around assassins and keep your distance. Understand?”*

*“Yes. I understand.”*

*“You don’t see many of them anymore, since they’ve lost their place in the world. But still… what are you doing?”*

*“Packing my things.”*

*“Why?”*

*“You told me to stay away from assassins.”*

*“……!”*

*“Oh, does that rule not apply to former assassins?”*

Man. I got beaten up a lot that day.

But that’s why I remember it so clearly.

The problem I was facing now was that I’d run into those very assassins in the middle of the imperial palace.

*If Ma Sanbao was going to bring in martial artists, why bring assassins into the imperial palace?*

Just as a question I couldn’t answer right away rose in my mind—

“Stop.”

A clear, bright voice pierced my ears.
## Chapter artifact 886

# Chapter 886

“Stop.”

The moment I heard that clear, bright voice—the last thing I’d expected—instinct surged ahead of thought and took over my whole body.

Whoosh.

My figure blurred. I closed the distance of three zhang in an instant, thrusting out my hand as instinct commanded.

Toward the owner of that voice.

Toward that snow-white neck.

Whoom.

The wind, unable to keep up with my speed, arrived a beat late. With a heavy whoosh, her hair fluttered.

At the last moment, I pushed back against instinct and stopped my hand in midair. Then I stared at the familiar face before me.

And asked,

“What is it?”

“That’s what I’d like to ask you.”

The woman who answered calmly—So Gyo—glanced at my hand, halted just in front of her throat.

“To strike so suddenly, without warning. You’re as rash as you look.”

“I think you meant ‘more rash than I look.’”

“In this case, I think I said it right. More importantly, when are you planning to move that threatening hand?”

“When I’m sure.”

“Sure?”

Instead of answering, I sent the internal energy I’d drawn up spreading in every direction.

The System update had sealed my Skills, but that didn’t mean I’d lost the Qi Sense that was part of me as a martial artist.

Whoooosh.

The air rippled like water. I swept the area within a radius of thirty or so zhang in an instant and, finding no other presence, slowly lowered my hand.

Only then did I feel my heartbeat begin to settle.

*If this had been a trap…*

Shit.

I’d let my guard down too much.

I’d been so lost in thought that I hadn’t even realized someone was nearby. Even if I’d walked right into a trap, I’d have had no excuse.

*More importantly… why is she here?*

As far as I knew, So Gyo was one of the Emperor’s people and stayed in Qianqing Palace.

For a moment, I wondered if I’d somehow wandered deep into the Inner Palace without realizing it. But I quickly shook my head.

That made no sense.

The boundary between the Outer Palace and Inner Palace was like the difference between heaven and earth.

No matter how much wider my freedom of movement had become, there was no way I could get into the Inner Palace unless the Embroidered Uniform Guard protecting it had all taken a group nap like a pack of golden retrievers at doggy daycare.

And no matter how deep in thought I was, I couldn’t have passed by that many people in the Inner Palace without noticing them.

*Then I’m still in the Outer Palace. Was there a place like this inside the imperial palace?*

I slowly looked around.

Strange flowers and rare plants crowded the grounds in every direction. A moss-covered pond lay nearby, and at the center stood a huge pavilion, rising like a mountain.

The vast space was desolate. There wasn’t another soul in sight besides So Gyo.

“Where are we?”

To be honest, I hadn’t expected an answer when I asked. But So Gyo’s next words proved me very wrong.

“A forbidden ground.”

“A forbidden ground?”

“A place in the imperial household that no one wants to enter, and everyone avoids talking about.”

“But two people have already entered.”

“Do you perhaps not know the difference between ‘won’t’ and ‘can’t’?”

“Oh.”

“This place was abandoned a long time ago. No one tries to come near it, so no one guards it.”

“Even outsiders like me?”

“Only people who have been thoroughly vetted can enter the imperial palace. Even an outsider who doesn’t know this place is forbidden wouldn’t go beyond a certain point if they had the slightest bit of common sense.”

“So you’re saying I’m an idiot with no common sense?”

“Thanks for saying it yourself.”

She got me there.

But thanks to what she’d said earlier, I thought I could guess where I’d wandered by chance.

“Is the reason people don’t come here connected to what happened more than ten years ago?”

“……!”

“Your expression tells me I got it right.”

So Gyo’s face, calm until now, changed ever so slightly. She looked at me in surprise, then gave a small nod.

“You’re more perceptive than you look.”

“This time, I think you meant ‘as perceptive as I look.’”

“I said it right. Just like a moment ago.”

At So Gyo’s firm reply, I resisted the urge to snap back and looked once more at the desolate scene before me.

*So this is the place.*

Something had seemed off from the moment I first saw it.

There was no one around, and it had been left to decay to an unreasonable degree.

But now I understood, at least somewhat.

If this was the place where the late Emperor and the direct imperial bloodline had been confined after the rebellion more than ten years ago, then no one in the imperial palace would dare come near it.

But…

“Why are you here?”

I couldn’t make sense of it.

Why had So Gyo, one of the Emperor’s trusted followers, come to a place that might as well have been the Emperor’s greatest sore spot?

And why had she answered my questions so readily, when I was practically her enemy?

“Could it be…?”

“I didn’t come after you. I thought we’d meet again soon, but I didn’t expect to run into you here of all places.”

“Then what is it?”

“Why should I tell you?”

“Well…”

I was at a loss for words and could only smack my lips. Then So Gyo, who had been watching me with composed eyes, suddenly spoke.

“If you answer one question honestly, I might tell you why I’m here.”

“What?”

“I promise.”

What the hell was this woman?

I thought it over for a moment, but I didn’t hesitate long. There was something I really wanted to know.

“In exchange, can I ask you something else?”

“Of course.”

I couldn’t make out the intent behind that calm expression of hers. I watched So Gyo with my brows drawn together, then let out a small sigh.

“Fine. Let’s hear it. What do you want to know?”

“It’s simple.”

And with So Gyo’s next words, I was even more confused than before.

“How long have you been studying martial arts?”

“What…?”

“I mean exactly what I said. I asked when you started learning martial arts.”

I blinked, momentarily at a loss for words.

So Gyo’s question had gone far beyond anything I’d expected.

I’d been keeping my expression in check, expecting a question like, *How deep are you in with Ma Sanbao?* Instead, all the tension drained out of me—and I was left wondering.

“No, why would you suddenly ask that…?”

“Have you already forgotten our conversation a moment ago? You only need to answer honestly.”

She was right.

All I had to do was answer honestly. Whatever her reason for asking, there was no reason my answer would harm me or my allies.

The problem was…

*Who’d believe it?*

I’d spent all this time going back and forth between Murim and the modern world, but add the time in both together and it came to barely two years.

Who’d believe I’d reached my current realm in just two years?

Even the handful of people who knew the truth hadn’t fully believed it. They’d simply let it pass, thinking there must be some circumstances behind it.

Even Jeok Cheongang, who’d watched me from closer than anyone else for the longest time.

*He didn’t fully accept it until he learned about the System and the modern world.*

The idea that a Third Rate punk steeped in pleasure had become a Supreme Peak master who shook the Central Plains in only two years was simply beyond the bounds of what anyone could accept.

That was why rumors so far from the truth had become accepted as fact.

—Jin Taekyung is a secret weapon the Jin Family of Taiyuan raised at the cost of the family’s survival.

—They had him pretend to be a layabout early on, so he wouldn’t catch the eye of the Mount Heng Sword Sect or the Head Elder.

—They funneled money to him under the pretense of paying a pleasure house. God knows how many elixirs they bought him with it. Jin Taekyung has three legs, they say.

That last one was a little strange, but anyway.

Rumors like those didn’t come out of nowhere.

Becoming a Supreme Peak master in two years was impossible even if the heavens split in two. So the lies had quickly become accepted as fact—and that worked in my favor.

If I told the truth outright, I could be branded an irredeemable practitioner of demonic, heterodox arts—or worse, an enemy of all Murim who’d mastered terrifying demonic martial arts.

*So even if I tell the truth, there’s no way So Gyo will believe me.*

As far as I could tell, So Gyo was also a First Rate martial artist.

Sometimes, what matters more than the complete truth is what looks like the truth.

Like right now.

“Fifteen years.”

I spoke up and looked at So Gyo without changing my expression.

“The story going around is that I caught a tiger with a pinecone when I was one, and learned the art of shrinking space when I was two… but that’s a load of bullshit only idiots believe. Going by the memories I still have, it’s been about fifteen years.”

So Gyo had been listening without a word. She murmured,

“Fifteen years.”

“You might not know this, but I have an older hyung just a few years above me. I worked hard, taking beatings from him left and right. And I had talent, too.”

“Like Cheongpung, the Huashan Divine Dragon?”

“Right. Cheongpung—wait. You know him? Even his title?”

“I know far more than you think. I’ve continued to hear news from Murim.”

“No, I mean, why would you need to?”

“There’s someone I need to find. Someone I absolutely must find.”

So Gyo answered calmly and turned away.

Or, more precisely, she was about to turn away when I thrust out my arm as fast as lightning.

“I answered, so you have to keep your promise…”

And then—

Swish. Rustle.

A breeze blew past.

“Huh?”

I stood frozen like a statue, staring dumbly at the hem of her robe as it brushed past my fingertips.

*What was that?*

I hadn’t used my full strength, of course, but it had still been more than fast enough to catch a First Rate martial artist.

Yet So Gyo had slipped past my hand with a movement technique so smooth she seemed to glide. As though it were only natural.

*Was that just my imagination? Or…*

A thought took shape in my mind, and the blood in my body seemed to turn cold. I glared at So Gyo, my eyes sinking deep.

“I didn’t know you had a trick like that.”

So Gyo replied calmly,

“I have quite a few tricks. Just as you can see.”

“Your movement technique is definitely beyond First Rate… Are you good at lying, getting under people’s skin, and running off, too?”

“Lying? I don’t think you’re in a position to say that.”

“What?”

“That claim that you’ve been practicing martial arts for fifteen years. It’s all a lie.”

“……!”

“Don’t underestimate the imperial family’s intelligence network. That’s why I’m staying here, too.”

A chill ran down my spine.

Her calm eyes, fixed on me right now, seemed to pierce my heart like arrows.

And I had a feeling the woman named So Gyo wasn’t merely one of the Emperor’s trusted followers.

“You… what are you, exactly?”

Ssshhh.

Three jiazi of Scorching Yang Qi heated the air around me.
## Chapter artifact 887

# Chapter 887

Sssshhh.

Heat like molten lava coursed through me, scorching countless acupoints.

I glared at So Gyo with burning eyes. The voice that escaped with my breath was dry as ash.

“You… what the hell are you?”

“That’s quite a reaction. You should calm down and settle your internal energy before you overdo it.”

So Gyo—or rather… the woman whose identity I no longer knew—answered.

As always, she was calm and composed.

But she’d shed the polite speech and courteous manner she’d used to keep up appearances until now.

Then, the next moment, one sentence slipped from her lips and surged over me like a raging tide.

“Especially considering the state you’re in right now. Don’t you think?”

“……!”

Maybe this was what it felt like to be struck by lightning right through the crown of your head.

A trembling voice slipped out before I knew it.

“H-How?”

“Your internal energy is flowing unevenly.”

So Gyo’s answer was short and simple—and, above all, impossible to refute.

But that wasn’t why I’d momentarily lost my words.

For such an obvious answer, one thing had to be true.

*Qi Sense.*

And not just any Qi Sense. It had to be exceptionally keen, sharp as a blade.

Every fight began with gauging your opponent.

A master could see through the amount and condition of a lesser martial artist’s internal energy, but a lesser martial artist couldn’t accurately gauge a master’s level.

And right now, I was unmistakably the latter.

*A master!*

There was no doubt.

The woman in front of me, So Gyo, was an incredible master.

A Supreme Peak master who’d reached the realm of Returning to Simplicity—able to hide herself so perfectly that even I couldn’t see through her.

*So that movement I saw earlier wasn’t a fluke.*

I suppressed the sigh threatening to escape and quietly clenched my fists.

I was unarmed, without a single decent weapon, and my body was in rough shape.

No matter how optimistically I looked at it, this wasn’t a good situation for facing a master a level above me. Still, I lowered my stance at an angle and drew up my internal energy again.

“Who are you?”

So Gyo replied in a calm voice.

“I have no obligation to answer that. You were the one who broke your promise and lied first, Blazing Flame Divine Dragon Jin Taekyung.”

“Shut your mouth and answer me. Whose orders are you following, exactly? The Emperor’s? Or…”

I glared at So Gyo and spat out the two words.

“Lord of Heaven?”

“Who knows.”

A brief silence.

So Gyo gazed at me, her expression too vague to read her intentions. Then she suddenly spoke.

“If you knew who I was, what would that change?”

“It would change things. This is a matter of life and death.”

“Life and death…”

“Yeah. Depending on your answer, someone here is definitely going to die.”

“If that happens, the person who dies has already been decided. Don’t you think?”

At that moment—

Sssshhh.

The air trembled.

The force that became wind and shook the grass and flowers was like the north wind, and her cold gaze and voice wrapped around me like winter’s chill.

But I didn’t waver.

I’d already lived through too many bloodbaths to feel afraid just because my opponent was strong.

As a Hunter and as a martial artist of Murim.

“Yeah, maybe it has been decided to some extent. But is there a rule that only one of us can die?”

“What?”

“I’ll kill you. No matter what.”

“……!”

“I swear on everything I have. No—I guarantee it.”

Even I was surprised by how calm my voice sounded.

But this wasn’t some desperate bluff from a weaker fighter backed into a corner. My conviction reached So Gyo intact.

“You… you’re serious?”

“Of course.”

“So you’re ready to take me down with you. Heh.”

So Gyo let out a faint laugh and looked me up and down like some strange animal.

“So the reports were true after all. I suppose you must have had some hidden trick up your sleeve to survive this long.”

“The Blood Lord, the Western Heaven Demon Lord, and most recently, even the Southern Heaven Demon Empress. Of course, the Sword Saint and the Fire King helped you through your crises, but surviving encounters with all of them is all but impossible.”

“……!”

I stared at So Gyo with a cold, steady gaze.

I had a feeling I didn’t need to hear the answer to my earlier question.

*This woman knows about the Western Heaven Demon Lord and the Southern Heaven Demon Empress.*

Not just their names. She spoke as if she knew what kind of people they’d been and how powerful they were.

As though she’d known them personally.

At last, the identity of the woman hiding behind the name and status of So Gyo came into focus.

*…Dark Heaven.*

Yeah. It could only be that.

Hadn’t she practically admitted it herself?

She’d said one of the main reasons she stayed in the imperial palace was its vast intelligence network.

That meant she wasn’t a loyal servant of the Emperor, and that she had another purpose of her own.

*She meant to seize the imperial palace—or rather, the Emperor—and pull the strings.*

The scattered pieces of the puzzle fell into place.

The Fourth Prince’s sudden rebellion. The deaths of the late Emperor and the direct imperial family, and everything that had happened since.

But in the end, it had only been a partial success.

Even though the Emperor had been replaced overnight and countless people had vanished like dew on the execution grounds, they’d failed to completely root out the opposition and take control of the entire Great Nation.

*Then could it be…*

Just as the puzzle in my head was almost complete, So Gyo, who’d been watching me silently, suddenly spoke.

“Let me ask you one thing. Why are you going this far?”

“Why?”

“Yeah. Why insist on fighting me with that body of yours in such poor shape, when you’re even prepared to die taking me down?”

I fell silent for a moment.

Not because I needed time to think about the reason, but because it was so obvious to me.

“Because if I do, fewer of my people will die.”

“What?”

“Even if we both die here, that’d still be a lot better than letting a bitch like you live.”

“What if I told you I had no intention of harming you?”

“Sure. That’d obviously be bullshit, but fine.”

“Why?”

“Because a viper like you only causes more harm the longer she lives.”

How many people had died by now?

Every time Dark Heaven made a move, hundreds died. Then thousands. In the end, tens of thousands vanished as lonely ghosts.

So if I could put an end to it with just my life, I’d count myself lucky.

Of course, the best possible outcome would be that I survived and So Gyo died…

“But it doesn’t matter. I don’t think I’ll feel at ease until I pull out those damn fangs and strip the skin right off you.”

This time, So Gyo chose silence.

She kept her lips tightly shut for a long while, then tossed out a single remark.

“You’re much crazier than I expected.”

“What the hell are you talking about, you crazy bitch?”

“And I think I understand a little why Prince Shangshan, that child, looks up to you so much. Yes. I really do.”

“Are you threatening me now because you’ve got a kid hostage?”

“Who knows?”

“What the hell do you think? Now I’ve got one more reason to kill you, no matter what it takes.”

“I like the enthusiasm. But things don’t always go the way you want.”

So Gyo gave a small shake of her head.

“To have reached this level at such a young age… Your talent and achievement are so extraordinary they seem like a trick of heaven. No one can deny that. But…”

She continued slowly.

“Everything has its time. Being born with heavenly patterns won’t let you escape death.”

Swish.

A faint sound brushed against her collar.

At the same moment, the belt wrapped around So Gyo’s slender waist—no, a flexible sword—filled with powerful internal energy and pointed at me.

Beyond its supple blade, her eyes were cold.

“Shall we put it to the test? See whether heaven saves you, or leaves you to die right here?”

Whoooom.

At that very moment, a low but clear sword hum rang out.

Fwoosh.

I felt it unmistakably.

A truly horrifying, enormous aura spread out from So Gyo—a power I’d never felt before.

It squeezed and pressed down on my whole body, leaving no opening.

Hah.

I drew in a breath without meaning to.

The air had grown heavy in an instant, constricting my throat.

Under the pressure of her overwhelming aura, every hair on my body stood on end, and cold sweat beaded on my skin.

But—

“Fuck. Off.”

With those words spat from between my teeth, I pushed back against the chains of internal energy I couldn’t see.

I endured as they bound my arms and legs tight and forced myself toward So Gyo.

Crack. Thud.

One step.

It was only one step, yet the solid bluestone beneath my foot shattered at once, and the layers of earth beneath it caved in.

Was it because my body was that heavy? Or because this place, abandoned for so long, had grown that decrepit?

Neither.

It was because I’d taken that step while bearing the full pressure of internal energy weighing thousands upon thousands of geun.

And because I’d endured it through physical ability that had long since surpassed human limits—not by neutralizing her internal energy with my own.

Crack. Craaack.

I put more strength into my next step. My foot crushed the soil and flowers beneath it. I could feel the bluestone fragments that had already shattered crumbling into dozens, then hundreds of pieces.

With every step I took closer, the pressure grew stronger.

But…

*I can take it.*

A well-honed blade was a fine weapon all on its own. The same was true of the physical abilities I’d built by crossing the line between life and death countless times.

Strength. Stamina. Agility.

I was superior in every way. I’d gone beyond my limits.

One of the main reasons I’d survived against enemies a level—or even two levels—above me was this body, which could wield superhuman strength without internal energy.

The body that could tear steel apart with bare hands, run for two days and nights without collapsing, and surge forward like the wind by pushing off the ground.

So even if internal energy equivalent to several jiazi pressed down on me, I could endure it.

No—I could break through.

“Hah!”

With a short shout, I threw both arms out with all my strength.

Boom!

With so much power and speed behind it, the compressed air burst apart. I felt the internal energy that had surrounded and pressed down on me from every direction scatter.

*Now!*

The moment my heavy body felt as light as a dandelion seed, I seized the instant opening and launched myself forward.

One person, staring at me with eyes now wide open.

Toward So Gyo.

Fwoosh—Boom!

Flamefire Path.

One step was all it took.

Scorching Yang Qi surged up from deep within my dantian and exploded from my foot. Along with the blazing heat, I crossed the distance of five jang in an instant and drove my fist forward like a cannonball.

*BANG!*

The world shook.

Beyond the surging blue-white flames, a thin figure shot backward at tremendous speed, accompanied by a roar that seemed to split the sky—then spun gracefully through the air.

Tap.

Her toes touched the blossom of a nameless flower, opened wide beneath the year’s strongest sunlight.

So Gyo landed on the flower as lightly as a passing breeze. I nearly let out an involuntary gasp.

*Ah.*

Ethereal, yet graceful.

It was an extraordinary movement technique.

So much so that I forgot for an instant she was my enemy. So much so that I briefly set aside the thought that I had to keep pressing my advantage.

So Gyo stared at me, her eyes flashing with an inexplicable light.

“I couldn’t feel any internal energy from you at all… How did you do that?”

I should be the one asking.

How had she blocked the Flame-Extinguishing Divine Fist I’d thrown with all my strength so easily?

How could she meet that flash of speed and destructive force head-on without even looking strained?

*You damn bitch. Have some conscience and at least pretend you’re struggling.*

I grumbled to myself and gave a wry smile.

Why was I smiling in a situation like this?

I didn’t know.

Maybe I really had gone crazy. Maybe it was because I’d already prepared myself to die before this fight.

Yeah. That was it.

I’d prepared myself.

A long time ago.

“You die, I live.”

I laughed like a man half out of his mind and took a step forward.

My condition?

Of course it wasn’t fine.

The dantian that had unleashed an enormous amount of power all at once was already lurching like an overworked engine, and my internal energy no longer moved as freely as my hands and feet.

But this wasn’t a sport in a ring.

There was no referee to stop the match, no second ready to throw in the towel on behalf of a fighter in danger.

That was what a life-and-death duel was.

Just as I’d always known.

*I’d already made my choice.*

Unlike my body, my resolve didn’t waver.

With that single-minded determination, I charged So Gyo once more.

Fwoosh!

The world slowed.

The scenery around me shifted.

And at the moment I surrendered my whole body to the heat, the wind, and the fighting spirit bubbling like lava—

Screeeech!

With a violent whistle, a streak of light hurtled toward me like lightning.
## Chapter artifact 888

# Chapter 888

It all began and ended in the blink of an eye.

Whoosh!

A streak of light came hurtling in faster than the sound of it tearing through the air. And then…

KABOOM!

A deafening blast, followed by a tremendous shock wave that shoved my whole body backward.

“Hngh!”

Crack. I swallowed a breath and dug my feet in. The ground flipped up beneath them.

The gale whipped up by the impact sent the pond water surging high into the air and swept through the rare flowers and plants blanketing the grounds.

Whooosh.

If anyone had seen the scene, they might have been overwhelmed for a moment and gasped in awe.

Countless petals swirling on the wind really were a spectacular sight.

But even the most carefree, clueless person would have groaned instead of gasping if they’d seen what had caused it.

Just like I was doing now.

“This is…”

My voice trailed off as I stared at *it*.

Amid the pond water and petals raining down like a sudden shower, *it* stood embedded deep in the ground, radiating a chilling edge. It was a weapon in a shape I knew well.

“A crescent blade?”

The words slipped out before I could stop them. Then a low, resonant voice pierced my ear.

“Calling it just a crescent blade is a bit of an insult.”

I turned toward the voice. There was the face I’d half expected—and had very much hoped not to see here.

Baek Yeon, Commander of the Embroidered Uniform Guard.

I calmly addressed the man people called the Blood Envoy in fear.

“Then what is it?”

“Golden Dragon. That’s its name. It’s been my trusted weapon for over thirty years.”

“Golden Dragon, Goldie—doesn’t really matter to me either way, but I’m surprised.”

“Surprised by what?”

“Nothing. It just seems like if it’s your trusted weapon, Blood Dragon would suit it better than Golden Dragon.”

Baek Yeon had been approaching without hesitation, but at my pointed question, he came to an abrupt stop.

“Seems you’ve heard a few things about me.”

“Plenty. Sounds like Goldie had quite a feast about ten years ago. You killed a lot of people with it.”

“It’s Golden Dragon, not Goldie. And it was necessary.”

“Sure. I’m sure it was necessary.”

I glanced between So Gyo and Baek Yeon, speaking sarcastically.

“In more ways than the rest of us were told.”

“Perhaps. I won’t bother defending myself, but even if only half of what you know or suspect is true, shouldn’t you be more careful about what you say and do?”

“Careful about what I say and do?”

I let out a hollow laugh.

“In a fucked-up situation like this, I’d cuss out the Emperor himself—or his grandpa. Don’t you think?”

I forced up the corners of my mouth, but I couldn’t do anything about the tightness in my chest.

I’d already been preparing to face So Gyo alone, ready to fight to the death. And now Baek Yeon had shown up, too.

*I didn’t expect him to get here this fast. Was killing me already part of the plan?*

Even calling this the worst possible situation didn’t do it justice. Heavy-hearted, I stepped forward and gripped the crescent blade lying a few paces away.

Shing.

It slid free, cutting through the solid ground as easily as a knife through tofu. The blade gleamed with a clear, almost transparent silver sheen.

It felt unfamiliar because it belonged to someone else, yet that familiar cutting edge made the anger that had briefly settled in me surge back up.

“Ten-Thousand-Year Cold Iron. Guess the Commander of the Embroidered Uniform Guard gets a hell of a weapon. I’m borrowing Goldie.”

Baek Yeon stroked his chin beard as he replied.

“That’s a troubling offer.”

“Why?”

“Because you’ll try to cut me and her down with it.”

“Then you shouldn’t have thrown it over.”

“I was in a hurry. What else could I do?”

Baek Yeon shrugged and continued.

“It also has a deeper meaning to me. The late Emperor personally bestowed it on me the day I was appointed Commander of the Embroidered Uniform Guard.”

“Then all the more reason I don’t care. The late Emperor would rather I used it anyway. If I said I was going to beat the traitorous bastards with it, he’d jump out of that pond and throw me Silverie, too.”

“……!”

“And this isn’t an offer. It’s a statement.”

At that moment, I saw it.

Baek Yeon’s thick eyebrow twitched, just for a moment.

After a brief silence settled between us, his voice slipped through his lips, low and subdued.

“Must you really make such a fuss?”

“Will it end with just a fuss?”

I quietly went over the plan I’d revised while we talked.

*If I fight them here, I’ll just die for nothing. Somehow, I need to draw as many eyes as possible over here.*

What would happen if I had to fight two masters who were both above me?

I didn’t need to think hard about it. I’d lose. No question.

*I do have One Annihilation as a last resort, but I can’t even be sure that would work.*

One Annihilation wasn’t invincible, and my body was already at its limit.

Even with the recovery I got from Level Ups, my body had ended up like this. What would happen now, without the System?

*It’d be the final move in the truest sense.*

The problem was, even if I burned my life away to use it, I might not take a single person with me. It could turn into a suicide mission that got me killed after missing my target.

*That’s a little too far over the line.*

I had no interest in becoming some dumbass who died of exhaustion after whiffing—or an SSS-rank suicide Hunter.

Now that things had come to this, I had no choice but to turn it into an all-out battle.

They had their own plans, and so did the anti-Emperor faction led by Ma Sanbao. But none of that mattered to me now.

No—the more accurate way to put it was that I didn’t have the luxury of thinking about any of that with those two monsters in front of me.

*Since we’re here, I’ll pull every damn stunt I can.*

Luckily, I had allies inside the imperial palace.

I didn’t know all the details, but there were Murim assassins Ma Sanbao had brought in. And above all, the Fire King, Jeok Cheongang, was right there.

*And, of course, the existing forces plotting against the Emperor.*

We had a decent chance of winning this fight.

Now that I’d worked it out, there was no point hesitating. I angled the crescent blade in my hand, ready to leave at once.

Whooom.

They said a weapon that spent a long time with one owner could take on a soul of its own. Seeing the blade tremble as if it rejected its unfamiliar owner and strange energy, I suddenly remembered something Jang Taebo, the former Guild Leader of the Ironcraft Guild and now a retainer of the Jin Family of Taiyuan, had once said.

But…

*Stay bent out of shape.*

Fwoosh.

Its brief resistance vanished as blue-white flames flared up, and I launched myself forward with all my strength.

Or I would have.

If So Gyo’s sudden words hadn’t pierced my ear just as the flames of Flamefire Path were about to burst from my feet.

“You’d better stop before you regret it.”

“What?”

“Prince Shangshan. Zhu Bao.”

“……!”

Just five words, but they were enough to stop me in my tracks.

In all the confusion, I’d overlooked one thing.

Right.

They still had that child.

As long as Prince Shangshan was in Qianqing Palace, the Emperor held his life in his hands.

Qianqing Palace was a demon-slaying battleground. Just from what I’d seen with my own eyes, there were no fewer than four Supreme Peak masters there, including the Emperor.

It wouldn’t matter if it were me or the Fire King. Even if the Martial God himself returned, he couldn’t do anything about the blade at the young prince’s throat.

“Choose which path to take. And think about what awaits you at the end of it.”

Her tone was calm, but in the cold air surrounding us, I had to force my voice through clenched teeth.

“What the hell are you trying to get out of this?”

“You don’t need to know. What matters is that you’ll survive here today.”

*Survive? Me?*

The lackeys of Dark Heaven would just let me go, now that they had leverage over me?

Stunned by her completely unexpected words, I could only blink. Then So Gyo added,

“And I want you to survive, too.”

“You do?”

“Yes.”

“……Why?”

“Because there’s a reason I still need you alive. It’s also the mission I was given.”

My eyes flew open before I knew it.

I’d heard something like that only a few months ago.

From none other than the Southern Heaven Demon Empress.

That was why I couldn’t help seeing the Southern Heaven Demon Empress as she’d been then, overlaid with the So Gyo standing before me now.

*The Southern Heaven Demon Empress had held back from killing me as much as she could, even right up until she was about to turn into a monster. Just like So Gyo is now.*

If so, the meaning could only be one thing.

Just like the Southern Heaven Demon Empress, So Gyo—or rather, the Lord of Heaven—still wanted me.

Not my cold corpse, my soul already gone.

Me.

Jin Taekyung, the Blazing Flame Divine Dragon.

*Why?*

None of it made any sense. I’d thwarted Dark Heaven’s plans at every turn, even cutting off two of their limbs in the process: the Western Heaven Demon Lord and the Southern Heaven Demon Empress.

From the Lord of Heaven’s perspective, after starting a war with the Murim of the Central Plains, I was one of the obstacles he ought to chew to pieces.

*So why?*

A memory from the past flashed through my mind.

The underground prison beneath the Sichuan Tang Clan. The whispers of that deep darkness I’d encountered briefly when it borrowed the body of the Western Heaven Demon Lord, who had unmistakably died.



*“How interesting. How very interesting.”*



And the eerie laughter that had seeped through that darkness.



*“We’ll meet again.”*



“……!”

Had it started then?

Was that one remark where it all began?

Crack.

Without my noticing, the veins stood out on my fist, now gone white. My body hair rose as I tried to settle the shock. So Gyo watched me calmly.

“So, what’s your answer?”

I closed my eyes, forgetting for a moment that I had an enemy right in front of me.

Then, the next instant—

Swish.

I reversed my grip on the crescent blade and shot it away like a beam of light.

Whoosh! Kaboom!

The blade tore through the air, followed by a thunderous boom.

Baek Yeon recovered his weapon from where it had buried itself deep in the ground a step ahead of him and clicked his tongue.

“You have quite a dramatic way of returning it.”

If this had happened just fifteen minutes ago, I’d have fired back with a sarcastic quip. But not now.

I gritted my teeth and spoke to the two of them.

“Don’t… touch Prince Shangshan.”

“Rest assured. Nothing like what you’re worried about will happen.”

I had no way of knowing whether that answer was true or false.

All I could do was look for another way.

*Still, I got one thing out of this. As long as the Lord of Heaven wants me alive, they can’t just move against me.*

Suppressing the killing intent I felt toward So Gyo and Baek Yeon, I started walking. To borrow a saying from Murim, from this moment on, every fifteen minutes would feel like three autumns.

The grand banquet would soon be held in the imperial palace.

That festival would be the battlefield where our fates were decided.

*The Hongmen Banquet. So who’s Xiang Yu, and who’s Liu Bang?*

I turned and walked away without hesitation. Before I’d completely disappeared from their sight, with my back to them, So Gyo’s voice suddenly reached me.

“Why did you give up fighting? Blazing Flame Divine Dragon Jin Taekyung. Do you want Prince Shangshan to become Emperor, too?”

A laugh escaped me.

It wasn’t a question worth answering.

Still, I kept walking without turning around and replied,

“Yeah. Since we’re going this far, of course I want him to become Emperor. But that’s not the only reason.”

“Then what is?”

“He’s a kid.”

I kept walking in a direction I didn’t even know, muttering under my breath.

“He’s still a kid, you crazy bastards.”
## Chapter artifact 889

# Chapter 889

Those who were going to leave left. Those who were going to stay stayed.

So Gyo watched Jin Taekyung’s back until it vanished in the distance, turning over the faint words she’d heard moments ago, carried to her on the wind.

*“He’s still a kid, you crazy bastards.”*

So Gyo suddenly wondered what expression Jin Taekyung had worn when he said it. How much sincerity had been in the back of him as he left, with anger and bitterness hanging over him?

But there was no way for her to know.

*You can plumb ten fathoms of water, but never one fathom of a person’s heart.*

As So Gyo repeated the saying to herself, Baek Yeon abruptly spoke.

“How much of this did you intend?”

“Intend?”

“Jin Taekyung coming here. Was that what you intended?”

So Gyo shook her head slightly.

“Not particularly. What happened just now was only a coincidence.”

“A coincidence. Then the reason you asked His Majesty to let him move about freely…”

“I needed to keep a closer eye on him. You already know some of the reasons I’ve been staying in the imperial palace, don’t you?”

“Could it be…?”

So Gyo answered Baek Yeon, whose eyes had suddenly widened, in an even voice.

“I can’t be certain yet…but I think he’s the one. The person I’ve been looking for. And the person that person foretold.”

There was not a trace of formality in the words the beautiful woman in her thirties spoke to the half-white-haired veteran, but Baek Yeon paid it no mind.

The woman calling herself So Gyo had the standing and the strength to speak that way. And her answer just now was more astonishing than he’d expected.

“So that’s why you made him stay in the imperial palace?”

“I had to see for myself. Whether the rumors surrounding the Blazing Flame Divine Dragon, Jin Taekyung, were true. Whether he really was the one that person spoke of. And…”

So Gyo turned her head. Her gaze swept over the place where someone had been moments ago, though that person was already gone. For an instant, her eyes gleamed sharply.

“What kind of person he is.”

Fortunately, the outcome of this chance encounter had been excellent. Perhaps not for Jin Taekyung, who had left with anger in his heart, but So Gyo had gained a measure of certainty and sorted out her thoughts.

*The Huashan Divine Dragon, Cheongpung. The Blazing Flame Divine Dragon, Jin Taekyung.*

So Gyo placed the names of the two rising martial artists she had been watching for some time on the scales in her mind.

And unlike when she’d first heard of them, she could see the scales tipping toward one of them.

*The Blazing Flame Divine Dragon, Jin Taekyung.*

As she’d told Baek Yeon, it was too soon to be certain. But given Jin Taekyung’s past actions and what she’d seen and sensed herself, there was every chance he was the person she was looking for.

*That must be why that person entrusted this task to me.*

Thinking this to herself, So Gyo slowly crossed the flower garden.

The place had been left in shambles by their brief clash, as if a storm had swept through it. At its center, something hidden beneath the flowers and grass poked up through the dirt.

“It’s been a long time.”

How deep beneath the ground had it been buried, and for how long?

So Gyo greeted the familiar-looking object as if speaking to herself, then reached out.

Whoooom—THUNK!

As an enormous, unseen surge of qi shook the air, two objects buried deep in the ground shot up into So Gyo’s hands.

They were exactly alike in length and width, as if measured with a ruler. Each also curved gently toward its tip.

They looked much like curved sabers. So Gyo hung one at each hip, then spoke to Baek Yeon, who had been watching her.

“It’ll be a fierce battle. Maybe fiercer than the one over a decade ago.”

Baek Yeon nodded.

“I’m prepared.”

“To the point of staking your life?”

“Do you know something?”

Baek Yeon followed the question with a calm reply.

“I’ve always staked my life to get what I wanted. That’s how I made it this far.”

“I hope you do the same this time.”

“I must. I will.”

Baek Yeon’s eyes sank as heavily as his voice.

“May I ask you one thing?”

So Gyo nodded.

“Anything, within what I can answer.”

“Why are you leaving the Blazing Flame Divine Dragon, Jin Taekyung, alone?”

“Why?”

“That’s right.”

“You must have guessed already.”

“Of course I have. But before we wipe them all out in one place, we should go after Jin Taekyung right now—”

“Impossible.”

So Gyo cut Baek Yeon off firmly, then spoke.

“There are still things we need to confirm. Until then, it’s better to let things proceed as they are.”

“What if he becomes an obstacle to the great undertaking?”

“An obstacle. For example?”

“As you know, Jin Taekyung’s master is the Fire King, Jeok Cheongang. And, by coincidence, he vanished without a trace after reaching the imperial capital. The other Murim martial artists following Jin Taekyung won’t make much difference to the larger situation, but…if they draw the Fire King in as well, things could become complicated.”

Baek Yeon was genuinely worried.

The Fire King, Jeok Cheongang.

Though the government and Murim were meant to stay out of each other’s affairs, there wasn’t a soul in the land who hadn’t heard of the man’s fame after more than a hundred years of life.

And Baek Yeon, who had led the Embroidered Uniform Guard since the late Emperor’s reign, was among those who knew better than anyone whether the countless rumors surrounding the Fire King were true.

A hero born of the Great Faction War. A demon awakened by the Demonic Cult.

A martial prowess that towered above even those powerful enough to be called kings.

He could not reach someone born in a human body and called a god, but he stood shoulder to shoulder with the Three Stars. If he took the other side, they would have to be prepared for tremendous losses.

Even with So Gyo, himself, the Emperor, and several other Supreme Peak masters on their side.

“Their forces are already formidable enough. And that’s only what we’ve managed to learn so far. If the Fire King joins them after Jin Taekyung…”

“The Fire King? That wouldn’t be bad.”

For a moment, Baek Yeon doubted his ears.

Then, seeing So Gyo continue with a faint smile on her lips, he realized she’d meant what she said.

“No, actually, that might be better.”

“……!”

Leaving Baek Yeon frozen like a statue, unable to understand her at all, So Gyo turned away with a quiet laugh.

The words she hadn’t told him drifted through her mind.

*Wait. You’ll know soon enough.*

Baek Yeon thought he knew everything, but he was wrong.

The story So Gyo had kept from him was something only she and the Emperor knew. Secrets were better off unknown.

At least until the banquet that both allies and enemies were eagerly awaiting.

“Only three days left until then.”

So Gyo looked up at the sky, now dark with night, and murmured. As if sensing the calm before the storm that had already begun, cold raindrops started to fall.

* * *

Shaaah.

The heavy rain hammered everything around us.

It was so loud that it swallowed even the shouts of the palace attendants running here and there in bamboo rain hats and rain cloaks.

Even after spending a good while in Murim, this was the fiercest downpour I’d ever experienced. The unexpected rain and thunder were more than enough to block the watchers’ view.

“You’re really going?”

Hyuk Mujin asked, his face tense. I answered,

“I have to.”

“What if they catch you…”

“They won’t. Not in this situation. You were there and heard it too, so you know.”

“I do. I know it’s urgent. But even so…”

“It’ll be all right. If it’s Young Master Jin.”

Hong Jin suddenly spoke, his voice subdued.

“Even if they catch him, there’s a good chance they’ll pretend they didn’t see him.”

“Huh? What do you mean?”

“If what Young Master Jin told us is true, what they want is to wipe us all out at once. They intend to uproot us in one fell swoop. We have no choice.”

I nodded silently.

Would So Gyo and Baek Yeon have let me go without a thought?

Even knowing full well that this story would reach their enemies?

*No way.*

This was a warning, and a declaration. A declaration that we weren’t to avoid this all-or-nothing battle. And we couldn’t refuse it.

*With Prince Shangshan in their grasp, there’s no way to avoid it, no matter what we do.*

The fact that our enemies had engineered the situation meant they were confident of victory. But no matter how thorough their preparations or how many traps they’d set, we couldn’t back down.

*We have to fight. Right now, before we worry about winning or losing, we have to make a decision.*

The stage was set. So were the actors.

The enemy had arranged the stage, and they intended to star in it. But sometimes, against everyone’s expectations, the supporting actor outshines the lead.

That was my job.

To change the lead of the coming performance—and the ending of this story.

And fortunately, there was one important surprise in the imperial palace that the enemy didn’t know about.

*Old Master.*

I stared out the window at the sheets of rain.

The downpour obscured my view, and the sky was already pitch-black. Below the pavilion, Embroidered Uniform Guard soldiers stood watch in shifts.

There were about twenty of them, all Peak masters.

But even if they were Supreme Peak masters, they couldn’t predict a sudden lightning strike.

FLASH! KABOOM!

*Now.*

At the instant white light flashed and a thunderous boom rang out, I pushed off the railing and sprang into the air.

Whoosh!

The Ghost Illusory Slaughter Step, a signature martial art created by the greatest assassin of all time, unfolded from my feet.

I hadn’t formally learned it; I’d only managed to work a little of it in. But that was enough to slip past the watchers during the brief confusion.

Tap. Swish!

I landed on the roof of a pavilion I didn’t know by name, said to house the palace attendants, and shot forward—quietly, but swiftly.

With the layout of the imperial palace already etched deep in my mind, I didn’t hesitate for even a moment.

*From here, along the east-west axis.*

The grounds were vast—vast enough to be boundless—with pavilions lined up here and there between them.

The black clothes I wore blended into the darkness, and the guards posted throughout the grounds failed to catch my movements.

“Damn, it’s really coming down.”

“The grand banquet’s right around the corner, and now the weather’s like this…”

The imperial guards grumbled as they gazed up at the sky from beneath the eaves. They had no idea that an uninvited guest had just passed within two steps behind them and entered the Outer Palace.

But not everything went smoothly.

“What are you doing here?”

“Y-Yes, sir!”

“If I remember the regulations correctly, your assigned post isn’t beneath the eaves.”

The only ones startled by that rock-hard voice weren’t the soldiers. I was just about to move on when I saw the familiar face that had suddenly appeared and swallowed a groan.

*Fuck, what’s that bastard doing here?*

Jeong Hogun.

A high-ranking Thousand Captain in the Embroidered Uniform Guard, he was walking toward the soldiers.

And at the same time, he was heading toward me, concealed not far away in the darkness.

# Checkpoint Review — 625–629

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

# Chapters 625–629

## Plot

The Nanman Beast Palace’s ruler, Yayul Cheok, welcomes Jin Taekyung after recognizing him as Jeok Cheongang’s disciple. Cheok explains that he cannot decide whether Nanman will join the Murim Alliance without the thirty-two tribes and four great tribal groups. His sworn younger brother, Baeksang, the Bai people’s great chieftain, arrives and firmly declares that Nanman will never join.

The Fire Dragon Pavilion is later subjected to deliberate mistreatment by palace staff resentful over Nanman’s losses in the Great Faction War and the recent massacre of more than two hundred Miao civilians. Yayul Mok apologizes and explains that Nanman lost most of the roughly ten thousand warriors it sent to the war, including his three older siblings. He rejects the alliance proposal, but Taekyung says he came to contain a spreading crisis rather than demand Nanman’s support.

The first tribal council opposed joining the Murim Alliance. A second council involving all thirty-two tribes will take place in three days, with Baeksang and two other great chieftains already opposed and Yayul Cheok the main remaining holdout. While returning to the pavilion’s lodging, Taekyung gets lost, disguises himself with a crudely made tiger mask, and enters the Outer Hall’s market. He sees the Yi and Yao great chieftains return from a beast-subjugation campaign. Yohi, the Yao great chieftain, notices him and reacts with sudden interest.

## Continuity

- Yayul Cheok is the Beast Miao King, ruler of the Nanman Beast Palace, a Supreme Peak master, and great chieftain representing the Miao people.
- Nanman consists of thirty-two tribes, including the four great tribes: Miao, Bai, Yi, and Yao.
- The Nanman Beast Palace has not formally rejected the Murim Alliance, but the first tribal council opposed joining.
- The second council will gather all thirty-two tribes in three days. Baeksang and two other great chieftains oppose joining; Yayul Cheok has not accepted their position.
- Baeksang is the Bai people’s great chieftain, Yayul Cheok’s sworn younger brother and childhood companion, and Yayul Mok’s sworn uncle. He has refused Cheok’s fruit wine for decades and remains estranged from him.
- Nanman’s opposition is fueled by the recent Heavenly Demon Escort Bureau massacre of more than two hundred Miao civilians and by its catastrophic losses in the Great Faction War.
- Yayul Cheok lost two sons and a daughter in the Great Faction War. Yayul Mok’s three older siblings died there, leaving Mok Cheok’s only surviving son.
- Jin Taekyung came to Nanman primarily to contain the crisis, though he will attempt to persuade the tribes without demanding anything in return.
- The Fire Dragon Pavilion is staying in temporary lodging inside the Nanman Beast Palace.
- Taekyung is currently separated from the pavilion and moving through the Outer Hall market while wearing a crudely made tiger mask to conceal his Han Chinese identity.
- The Yi and Yao great chieftains returned with roughly five hundred warriors after hunting man-eating beasts; local reports say the Yi achieved no notable result.
- Yohi is the intelligent and exceptionally beautiful female great chieftain of the Yao people. She noticed Taekyung in the crowd and reacted strongly.

## Translation Decisions

- Use **Yayul Cheok**, **Yayul Mok**, **Baeksang**, and **Yohi** consistently.
- Render **야수묘왕** as **Beast Miao King**, **소궁주** as **Young Palace Lord**, and **대족장** as **great chieftain**.
- Use **Miao people**, **Bai people**, **Yi people**, and **Yao people** for the four great tribes.
- Use **sworn younger brother** for the relationship between Yayul Cheok and Baeksang; do not treat **White Elephant** as Baeksang’s alias.
- Retain **Murim Alliance**, **Heavenly Demon Escort Bureau**, **Nanman Beast Palace**, **Outer Hall**, and **Crudely Made Tiger Mask**.
- Preserve Taekyung’s casual profanity, teasing, and clipped exchanges with Taishan.

## Durable state

{
  "active_continuity": [
    "The Fire Dragon Pavilion is staying in temporary lodging within the Nanman Beast Palace after being welcomed by Yayul Cheok.",
    "Nanman's first tribal council opposed joining the Murim Alliance; all thirty-two tribes will meet in three days for a second council.",
    "Baeksang is the great chieftain of the Bai people and Yayul Cheok's sworn younger brother, but he opposes Nanman joining the Murim Alliance.",
    "Jin Taekyung came to Nanman to contain a spreading crisis rather than as a diplomat, but he will attempt to persuade Nanman if possible.",
    "Jin Taekyung is currently in the Nanman Beast Palace's Outer Hall after getting lost on the way back to the Fire Dragon Pavilion's lodging.",
    "Jin Taekyung is concealing his identity with a crudely made tiger mask while moving through the crowded Outer Hall market.",
    "The Miao, Bai, Yi, and Yao peoples are Nanman's four great tribes; the Miao are strongest, followed by the Bai.",
    "The Yi and Yao great chieftains returned with roughly five hundred warriors after a campaign against man-eating beasts, and the Yi achieved no notable result according to local reports.",
    "Yohi is the female great chieftain of the Yao people, renowned for her intelligence and extraordinary beauty.",
    "Yohi has noticed Jin Taekyung in the crowd and her eyes lit up when she recognized him."
  ],
  "continuity_sources": [
    629,
    628
  ],
  "open_questions": [
    "Why does Baeksang oppose joining the Murim Alliance despite his lifelong bond with Yayul Cheok and their shared service in the Great Faction War?",
    "What is the meaning of Baeksang's cold scrutiny of Jin Taekyung?",
    "Will Yayul Cheok overcome the other great chieftains' opposition and bring the Nanman Beast Palace into the Murim Alliance?",
    "Will the remaining tribes follow Baeksang and the other opposing great chieftains at the council in three days?",
    "Why did Yohi react so strongly after noticing Jin Taekyung?"
  ],
  "safe_through": 629,
  "temporary_decisions": [
    "Use Baeksang for 백상 and do not treat White Elephant as a separate alias.",
    "Use sworn younger brother for 불알 동생 in the relationship between Yayul Cheok and Baeksang.",
    "Use Jiang Taigong for 강태공 and Jindro for 진드로.",
    "Render 황개 as Hwang Gae and 똥개 as Ddong Gae.",
    "Render 입맹 as joining the alliance."
  ],
  "version": 1
}

## Reading copies

## Chapter artifact 625

# Chapter 625

People possess something called an aura.

Some people’s auras are so faint and hazy that they can barely be felt, while others possess auras so powerful and rough as waves that they overwhelm anyone who stands before them.

The Beast Miao King, Yayul Cheok, was the latter.

*Whoosh.*

Yayul Cheok slowly rose to his feet, looking as though a massive mountain had begun to move.

Despite being well over eighty years old, the muscles covering his entire body were as solid as armor. His steps were firm and unhesitating, and his half-gray beard streamed like a lion’s mane.

*Thud. Thud.*

Everyone could now see him as he approached, trampling down the vine-covered stairs with his bare feet.

Yayul Mok and his guards immediately dismounted and dropped to one knee. It was their own form of etiquette for showing respect to the lord of the Nanman Beast Palace.

“Greetings, Palace Lord.”

The Beast Miao King stared intently at Yayul Mok.

“You ran off again without saying a word.”

“There was a fire in the northeastern pasture. I happened to be nearby…”

“Did you put it out?”

“Yes.”

“And the culprit?”

The question was clearly directed at Yayul Mok, but the Beast Miao King’s gaze was fixed on me.

I stared straight into his tiger-like eyes, which radiated a fierce light, and stepped forward.

“‘Culprit’ would be putting it a bit strongly. There was a little mistake.”

“It’s been a long time since I’ve seen Han Chinese. Are you the culprit who started the fire?”

Before I could answer, his voice continued with a growl.

“Think carefully before you answer. Nanman’s laws are far from merciful.”

After thinking for a moment, I asked,

“How are people punished in a case like this?”

“It depends on the severity of the damage, but in serious cases, they become food for wild beasts. Or they are thrown into a pit filled with venomous beasts.”

“What about minor cases?”

“They are hanged from a vine.”

“That’s considered minor?”

“Of course. At least the body can be kept intact.”

“Ah.”

I nodded, then casually stepped to the side and introduced someone.

“Ta-da. Actually, this is the culprit.”

An ordinary person might have panicked, but a Hidden Shadow Pavilion agent with fifty years of experience was clearly different. Namho calmly opened his mouth.

“Are you fucking insane?”

“No, I’m not exactly wrong.”

“You fucking bastard…”

Namho was just about to unleash a proper stream of abuse when the Beast Miao King abruptly spoke in a rough voice.

“So you intend to abandon your companion and save your own life.”

“Hmm. There seems to be a misunderstanding. I never said I was abandoning him.”

“A misunderstanding?”

“I’m just pointing out the facts. No, not facts. The truth. We haven’t known each other for very long, but he’s still a good person. And there’s the Murim Alliance’s reputation to consider.”

I had deliberately brought up the Murim Alliance, so the Beast Miao King might have let the matter drop at that point. But the fierce light in his eyes, once kindled, did not fade in the slightest.

“Now that you have entered Nanman, you must follow Nanman’s laws. If one of you must take responsibility, then what?”

“If you insist…”

I scratched the back of my head and continued.

“Wouldn’t we have to stop that somehow?”

And then, in that very moment—

*Whoom!*

The air around us vanished.

Before the short, heavy sound of air splitting could even be heard, a single punch shot toward me. It carried enough force to resemble a battering ram, and I crossed both arms in front of myself.

*Boom!*

A deafening roar rang out as though the sky itself had split open, and the shock wave from the collision swept in every direction.

The tremendous force drove me back a full ten feet. I let out a sigh.

“Is that enough?”

The Beast Miao King asked, his eyes emitting a glacial light.

“What are you talking about?”

“Our first greeting.”

“What?”

“Before coming to Nanman, someone told me something. The Beast Miao King may look ignorant and reckless, but he’s actually warmhearted and loves playing pranks. So take him in stride and get along with him.”

“……!”

“……!”

The Fire Dragon Pavilion members’ reaction—standing there with their mouths hanging open—was nothing compared to what came next.

Yayul Mok, the Young Palace Lord, and his guards stared at me in shock before reaching for their weapons at lightning speed.

But before they could act, the Beast Miao King, whose lips had been twitching at my words, burst into laughter.

“Ha ha ha ha! Old Master Jeok hasn’t changed a bit.”

I rubbed my stinging forearms and answered,

“Well, he’s still remarkably healthy.”

“I heard he had taken a disciple, but I never expected to meet you so soon.”

The Beast Miao King looked at me with renewed interest and continued with a broad grin.

“Good to meet you. This old man is called Yayul Cheok.”

It might have been different with someone else, but before he was the lord of the Nanman Beast Palace, the man before me was an acquaintance of Jeok Cheongang.

I respectfully clasped my hands toward Yayul Cheok, the Beast Miao King.

“Jin Taekyung, nineteenth successor of the Fire Gate Clan, pays his respects to Great Hero Yayul Cheok, the Beast Miao King.”

“Good. Ha ha ha ha!”

The Beast Miao King let out a rough but refreshing laugh and continued in a voice full of goodwill.

“We have much to discuss. Follow me.”

Everyone watched his retreating back with bewildered expressions before turning their eyes toward me.

Their looks seemed to ask what had just happened, so I shrugged and answered,

“He’s kind of close with my master.”

As expected, life was all about school ties, regional ties, and blood ties.

* * *

The Beast Miao King looked happy.

No, he was definitely happy.

I already knew from Jeok Cheongang that he was normally a fairly cheerful person. But as he sat in the main hall inside the Nanman Beast Palace and brought up old stories, he looked like a huge child.

“I remember the day I first met Old Master Jeok. The moment he saw me, he immediately sent a Flame Divine Palm flying.”

“……According to the Old Master—no, according to my master—he didn’t actually let it fly. He said he only almost did.”

“No. It definitely hit me. It knocked the breath out of me and scared the shit out of me.”

The Sect Leaders and Family Heads of the prestigious factions I had met so far generally maintained a certain degree of dignity.

But the Beast Miao King, who walked around wearing nothing but a pair of tiger-skin pants, did not care about dignity or anything else.

As proof, he showed me the mark of the Flame Divine Palm stamped into his side and added casually,

“It was quite a first meeting. I shit blood twice, then went back to see him, and he poured me a drink, telling me to disinfect the wound. What a bighearted man.”

“……Ah. Yes.”

I wondered whether he and I understood the meaning of “forthright” in the same way, but the person who had been hit said he was fine, so what could I say?

Besides, the person in question was Jeok Cheongang. Criticizing him would only be like spitting in my own face.

“I was disappointed that I couldn’t see Old Master Jeok after the Great Faction War ended, but meeting his Disciple like this is truly a pleasure. Do you like alcohol?”

“I do, of course, but I don’t think I can drink right now.”

“Why not?”

“There’s something more urgent than drinking.”

If the world had been at peace, I would gladly have held a drinking party with him.

I would have toasted the Beast Miao King, shouted, “Yayul Cheok’s favorite—random games!” and gotten all the people of other ethnicities completely wasted on drinking games.

But at a time like this, that was impossible.

“This time, I didn’t come as my master’s Disciple. I came as the Pavilion Master of the Murim Alliance.”

At my quiet words, the smile around the Beast Miao King’s lips faded slightly.

“Is it because of Dark Heaven?”

“So you already know.”

“I received a messenger eagle concerning it. Since we’re tens of thousands of li from the Central Plains, the message arrived late. But it’s not as though I know nothing about the situation in the Central Plains.”

“If you don’t mind me asking, when did you receive it?”

“Let me think. It seems to have been over a month ago.”

Considering the distance between Henan and Nanman, as well as the timing, the letter must have been sent before the formation of the Murim Alliance, an event called the Mount Song Resolution.

As many sects as possible had needed to attend the Mount Song Resolution, and Chief of the Hidden Shadow Pavilion Thousand-Faced Fox was not the kind of person who would send a letter without taking even that into account.

And that meant…

“You refused to join the alliance. The Nanman Beast Palace did.”

There had been enough time to send a reply and to lead some of the people of other ethnicities to Mount Song.

But the fact that the Nanman Beast Palace had sent no response to the Murim Alliance could only be interpreted as a polite refusal.

The Beast Miao King remained silent for a moment before abruptly opening his mouth.

“It was not an outright refusal. We simply haven’t reached a conclusion.”

“If it’s a conclusion, then, Palace Lord…”

My words were cut off by a gesture from the Beast Miao King.

He stroked his beard, which resembled a wild beast’s mane, and spoke again.

“Disciple of Old Master Jeok. No, you said your name was Jin Taekyung.”

“Yes.”

“I have a question for those you brought with you. Do you know who I am?”

The hesitant atmosphere lasted only a moment.

Hyuk Mujin was the first to meet the Beast Miao King’s gaze. He swallowed dryly before answering.

“You are Great Hero Yayul Cheok, the Beast Miao King. You are also a Supreme Peak master among the Ten Kings.”

“That is correct. The woman beside him. Yes, you.”

Ju Hwaran answered without hesitation.

“As everyone knows, you are the Palace Lord of the Nanman Beast Palace.”

“That is also correct. But it is not the answer I want. This time, you beside her—tell me.”

Before anyone could stop him, Taishan blinked his enormous eyes and answered.

“Taishan. Hungry.”

*You bastard, Taishan. You answering-machine bastard. You fucking bastard…*

The answer went so far beyond what I had expected that the Beast Miao King wore a distinctly awkward expression.

“Who is that fellow?”

After thinking for a moment, I answered honestly.

“I’m not really sure anymore, either.”

“What a strange fellow. Then let the old man beside him answer.”

Namho, who had been firing a rapid stream of profanity at Taishan in a low voice, opened his mouth.

“You are the great chieftain who leads the Miao people.”

“That is correct.”

The Beast Miao King nodded and continued.

“I am the great chieftain who represents countless Miao people. I gathered them under one banner and became the Palace Lord of the Nanman Beast Palace with the support of the other tribal chiefs. Mok, do you know how many tribes exist in our land?”

Yayul Mok, who had been standing silently at attention, answered.

“If we include all of Nanman, there are thirty-two tribes, including four great tribes such as the Miao people.”

“Yes. That is the Nanman Beast Palace.”

I realized what the Beast Miao King was trying to say.

No, I was not the only one. Everyone here had realized it as well.

Except Taishan, of course.

“Does that mean…”

“Before I am the Palace Lord, I am the great chieftain of the Miao people. And the lord of the Nanman Beast Palace is not a king.”

He meant that the Beast Miao King could not make every decision by himself.

The Nanman Beast Palace was certainly like a separate kingdom, cut off from the Central Plains. But that kingdom was made up of an alliance of large and small tribes.

Then why was he being so honest about all this?

*Are the other tribes opposed, while the Beast Miao King himself is considering agreeing to join the alliance?*

Just as I was about to voice the question that had suddenly occurred to me, a quiet voice came from beyond the firmly closed doors of the main hall.

“Palace Lord, may I speak with you for a moment?”
## Chapter artifact 626

# Chapter 626

“Palace Lord, may I speak with you for a moment?”

A low, rigid voice drifted through the crack between the closed doors.

Everyone instinctively turned toward the door behind us, but I didn’t miss the change that occurred in that brief instant.

*The Beast Miao King. And Yayul Mok.*

We outsiders were nothing more than stones that had happened to roll in from elsewhere. But those two were embedded so deeply in Nanman that they were like an indispensable inner core.

I didn’t know who the owner of that voice was, but the fact that both of their gazes had instantly darkened was answer enough.

*They’re not exactly on smiling terms.*

Just as I reached that conclusion inwardly, the Beast Miao King happened to meet my gaze and let out a quiet laugh.

“What an interesting fellow.”

“Pardon?”

“It’s nothing. Just something that slipped out.”

As if it were nothing. Anyone could see it was something.

But the Beast Miao King gave a small wave of his thick hand, as if telling me not to ask any further, then addressed everyone—including me.

“I’m sorry, but another guest has arrived. Could you give us some privacy? There is still time, so I would like to discuss things in greater detail after you’ve rested from your journey.”

There was a slight contradiction in the Beast Miao King’s words about there still being time. As long as Dark Heaven existed, no one knew what might happen.

Still, I agreed with his suggestion that we rest for a while before talking.

*At least, it doesn’t seem like anything unusual has happened in Nanman yet.*

As I nodded, the Beast Miao King’s gaze shifted to Yayul Mok, who was standing at attention on his right.

“Mok.”

It was only a single word, but that was enough. Yayul Mok respectfully performed the proper etiquette, then gestured toward us.

It meant we should follow him.

“We’ll take our leave.”

“Go. I’ll prepare a grand welcome.”

*Forget the grand welcome. I just hope the discussions about joining the alliance and Dark Heaven go well.*

After we took our leave of the Beast Miao King and reached the door, the stone door carved from solid rock began to move.

*Rumble.*

Beyond the slowly opening gap, accompanied by a heavy grinding sound, two muscular strongmen wearing bear hides could be seen pulling on chains connected to the door.

And then…

“It’s been a long time.”

The owner of the rigid voice we had heard earlier was there as well.

At his sudden greeting, Yayul Mok lowered his head.

“Yayul Mok of the Miao people pays his respects to Uncle Baeksang.”

The middle-aged man of another ethnicity was dressed entirely in white, from head to toe, including his clothing and accessories. The man Yayul Mok had called Uncle Baeksang opened his mouth.

“I heard you had returned. I also heard there was quite a large fire in the northeastern pasture.”

“It was a minor problem. It was put out quickly.”

“A minor problem.”

The cold gaze that accompanied his rigid voice swept over us. Baeksang examined Yayul Mok and everyone standing behind him.

More precisely, he examined me in particular.

At the same time, his low, unhurried voice continued.

“I hope so.”

“……”

“Where is the Palace Lord?”

“He is waiting inside.”

That was all.

Baeksang glanced at Yayul Mok, who was still bowing his head, then passed by us without another word.

*Rumble.*

When the stone door closed once more with another heavy grinding sound, Yayul Mok finally raised his head.

He stared at the firmly closed stone door with his lips pressed tightly together. I asked him,

“Who was that?”

“None of your business.”

“You don’t want to tell me. Fine, then. Elder Namho?”

Namho, the Hidden Shadow Pavilion’s walking encyclopedia of Nanman, answered without hesitation.

“He is the great chieftain of the Bai people, one of the four most powerful great tribes in Nanman.”

“Oh. No wonder he was dressed entirely in white. I saw a few people like that near the entrance to Nanman. You mean those whiteys, right?”

Namho answered with a reluctant tone.

“White guys… Well, that isn’t exactly wrong. The tribe itself venerates the color white.”

More than thirty tribes coexisted throughout Nanman. They formed villages in various places and preserved their own customs.

Yeongin was practically a gathering place even in Nanman, so several tribes lived there by making various compromises. The Bai people were among them.

*I didn’t know they were that powerful.*

In any case, the great chieftain of one of the great tribes dividing this vast land of Nanman into four…

I had suspected as much from the moment Yayul Mok called him Uncle, but Baeksang was an even bigger figure than I had imagined.

After learning the basic information, I quickly caught up with Yayul Mok, who had moved well ahead of us.

“But you two didn’t seem very close. Is he really your actual uncle?”

“……”

“Hey. Hey, can’t you hear me?”

“……”

“If someone calls you, you’re supposed to answer. Do you want to see the burning pasture? Huh? Want me to start a nice fucking fire on the way back?”

“……”

“Oh, this bastard is ignoring me to the very end. Fine, I get it. You have to see fire, not a coffin, before you’ll cry.”

Judging by my record as a mouth-fighting champion, my win rate was one hundred percent.

This time was no different.

“……Please stop spouting incomprehensible bullshit.”

“Oh, then behave yourself. If you answered promptly, none of this would happen.”

Yayul Mok glared at me for a moment before letting out a sigh.

“Think before you ask. If he were my actual uncle, would he belong to a different tribe?”

“True. But why are you calling him Uncle?”

“He and my father are sworn brothers. They formed a deep friendship when they were young, and I heard they always fought together during the Great Faction War.”

My eyes widened in surprise.

“What? Is that true?”

“I heard you Han bastards were suspicious by nature, and it seems that was true. What? You don’t believe me?”

“It’s not that, but… I was a little surprised.”

“Is it really so surprising that the two of them are sworn brothers?”

“No, not that.”

“……?”

“Great Hero Yayul Cheok was your father? Not your grandfather or great-grandfather?”

“……!”

Yayul Mok’s gaze turned icy, but surprising was surprising.

Good grief. A fellow who looked no older than his mid-twenties was the son of the Beast Miao King, who was well over eighty.

Even if martial artists generally married late, that was impressive in an entirely different way.

“Um, Pavilion Master?”

At Ju Hwaran’s cautious call, I waved my hand.

“Just a moment. I only have one last question. Are you the eldest son? No, right?”

*Tap tap tap.*

Yayul Mok’s footsteps suddenly quickened. He answered through clenched teeth.

“I am the only son for three generations.”

“Wow. Yayul Only-Son. An omniscient Nanman point of view is totally possible.”

“What does that mean? Are you actually insane?”

“I do sometimes say things people can’t understand. Anyway, that Baeksang fellow seems to be on the side opposing Nanman Beast Palace joining the alliance, right? Whatever happened in the past, you two aren’t exactly on good terms now?”

“That is no concern of an outsider like you—!”

This was why the flow of a conversation was important.

Yayul Mok had been answering with his face flushed from anger, but he faltered and let his sentence trail off. However, the water had already been spilled, and the fire had already spread.

Having baited him perfectly, I smiled warmly and patted his shoulder.

“You bastard. Why did you stop talking? So my guess was right, then?”

“……You.”

“This is enough for now. I’ll ask again later if I need to. Thanks, by the way. Oh, and this is our lodging, right? Thanks for showing us the way.”

I turned away from Yayul Mok, who was glaring at me as if he wanted to kill me.

Namho was staring at me with the expression of a primitive man who had just discovered fire.

“Have you ever considered joining the Hidden Shadow Pavilion?”

“The Hidden Shadow Pavilion? Forget it. Anyway, you heard all that, didn’t you?”

“Of course. The way you lured him in and hooked him was at least Jiang Taigong’s level.”[^1]

I answered in a solemn tone.

“A fisherman who catches people. Please call me Jindro.”

“Jindro…!”

Ju Hwaran and Hyuk Mujin also clenched their fists, excitement written across their faces.

“Pavilion Master. You’re truly, truly amazing. At first, I really thought you had lost your mind.”

“Young Lady Ju is right. I was so frustrated that I wanted to tear Captain’s mouth open and kill him.”

It felt a little strange, but I had still accomplished something. I smiled with satisfaction and opened my mouth.

“Thank you for the compliment, Young Lady Ju. Mujin, put your head down.”

“Yes, sir.”

*Thud.*

Hyuk Mujin planted his head on the ground as naturally as breathing. I sat astride his back.

Song Ilseom and Sama Pyo had been watching the situation with dumbfounded expressions. They asked,

“That was outrageous, but… regardless, we learned some important information.”

“Pavilion Master, what do you intend to do now?”

I shrugged without a word.

We had gained new information, but the fact that the great chieftain of the Bai people opposed the Nanman Beast Palace joining the Murim Alliance was hardly good news.

What concerned me even more was the reason.

*Why? Why?*

Why would a man who had fought in the Great Faction War—the Beast Miao King’s childhood best friend and sworn younger brother—oppose joining the alliance?

And what did the coldness I had sensed from Baeksang during our brief encounter mean? What did it mean that he had been studying me so carefully?

That was what bothered me.

*Grrrrrrk.*

“Taishan. Hungry.”

“……”

*That fucking bastard.*

* * *

A high-backed chair covered in leopard and tiger hides.

The Beast Miao King sat in it with his chin resting on one hand, then picked up the wine bottle placed before him.

*Glug-glug.*

As the rough stone bottle he had carved himself tilted, cloudy liquor filled a large wooden bowl.

Of the two cups he filled, the Beast Miao King offered one to his new guest.

“It’s the fruit wine you like. Don’t hold back, Baeksang.”

Baeksang. The name meant white elephant.

Yet the middle-aged man who caught the slowly drifting cup looked nothing like an elephant.

His gaze was as cold as ice, and the corners of his mouth were stiff. With a lean build completely unlike the Beast Miao King’s, he answered in a rigid voice.

“I’m fine. I’ll pass today.”

*Clack.*

Baeksang deliberately set the cup down with a noise. The Beast Miao King smiled bitterly.

“……I see. That’s fine.”

Despite what he said, his heart ached.

Somewhere in the old memories that had grown hazy with time, his one and only sworn brother had once spent days and nights laughing, talking, and constantly raising their cups with him.

For decades, that brother had been giving him the same answer.

*I’ll pass today.*

It wasn’t just today. It had been the same the day before yesterday and yesterday. Tomorrow and the day after would be no different.

The Beast Miao King was already familiar with it, which was why he could predict it. And knowing that his prediction would come true pained him.

“So, what brings you to seek out this older brother today?”

Baeksang answered in an unwavering voice.

“You know why.”

“It’s because of them.”

“I heard they came from the Murim Alliance.”

“That’s right. They were sent by Sword Saint Mae Jonghak, who has taken office as the new Alliance Leader.”

The Beast Miao King readily admitted it. There was no reason to hide it, and even if he did, Baeksang would inevitably hear about it in the end.

There were already countless Bai people among those belonging to the Nanman Beast Palace’s Inner Hall.

*He may even know their exact identities.*

The Baeksang he knew had always been meticulous, and this time would be no different.

Baeksang’s cold gaze settled on the Beast Miao King as he silently tipped his cup.

“You haven’t forgotten the result of the last tribal council, have you?”

*Of course not.*

As the Beast Miao King answered inwardly, Baeksang’s rigid voice pierced his ears.

“We—the Nanman Beast Palace… will never join the alliance.”

[^1]: Jiang Taigong is a legendary Chinese fisherman famed for luring people through patience and skill; his name is also used for someone who expertly hooks others.
## Chapter artifact 627

# Chapter 627

The temporary lodging we’d been assigned was decent enough. It wasn’t as lavish or high-class as anything in the Central Plains, but it was clean and more than adequate for me and the Fire Dragon Pavilion members to stay in for the time being.

Of course, that didn’t mean we’d received an unconditional welcome.

“Hmm. Does anyone know what’s stuck to my chopsticks right now?”

At the surprise quiz I posed during the meal, Hyuk Mujin shot his hand into the air.

“Oh, right. Mujin. Answer it.”

“The correct answer is… a bug!”

“Correct. More precisely, it’s a centipede. But why would something like this be in our food?”

“Hmm. Perhaps it’s a custom of the non-Han people of Nanman?”

Namho, an eighty-year veteran of being one of Nanman’s non-Han people, muttered as he picked out something resembling a pine caterpillar.

“This is the first I’ve ever heard of such a custom…”

I could have understood it to some extent if they’d simply roasted locusts and served them to us. But this was on the level of dumping live insects into the food. There was no way even I could defend it.

Sama Pyo let out a sigh as he stared pointedly at Taishan, who was still trying his hardest to bury his face in his plate.

“So it seems we really aren’t welcome.”

There was no way this could be called a meal. Song Ilseom set down his chopsticks and replied calmly.

“It’s probably because of the Heavenly Demon Escort Bureau incident.”

I agreed. But that didn’t mean I thought Yayul Mok had personally ordered this.

Someone important enough to be the Young Palace Lord wouldn’t use such petty methods.

*So this was the work of other non-Han people within the Nanman Beast Palace.*

We’d been hated consistently from the moment we entered Nanman until now. I was just thinking that even the ugly duckling hadn’t been treated this badly when Ju Hwaran quietly appeared.

She had gone upstairs before the meal, saying she was going to wash up.

“Huh? You’re already done?”

How long had it been since she went upstairs? Not even Recruit Number 54 at the Nonsan training center could wash that quickly.

At my questioning tone, Ju Hwaran answered with an ambiguous smile.

“Ah, yes.”

“……”

I had a distinctly bad feeling about this. When I continued staring at her without saying anything, Ju Hwaran hesitated for a moment before speaking.

“Actually, the thing is…”

After hearing the whole story, I couldn’t help letting out a dry laugh.

“They gave you water hot enough to boil in this weather? And they mixed something resembling filth into it?”

Ju Hwaran nodded awkwardly.

“I wasn’t going to tell you. It could have been a simple mistake, but I was worried this might cause trouble…”

“It wasn’t a simple mistake. And don’t worry about it. Even without that, we already have another problem.”

Only then did Ju Hwaran realize what was happening with the meal and gave her brief assessment.

“Ugh.”

“I’m only asking to be sure, but you’re not going to eat that, are you?”

“No. Of course not.”

I had never seen Ju Hwaran answer so decisively before. Clicking my tongue softly, I rose from my seat.

“Captain, where are you going?”

“To make a scene.”

The way of the world was simple: stay still, and people took you for a mat; keep letting them get away with things, and they took you for something to wrap up.

Since we had come here to persuade the Nanman Beast Palace, I would maintain a certain degree of restraint. But I needed to make a proper fuss at least once if I wanted to ensure they never tried this again.

I was about to fling open the door when I suddenly remembered something I’d forgotten and stopped.

“Oh. And one more thing.”

“Yes?”

“Make him stop eating.”

No one asked who I meant by “him.”

There was only one person among us wolfing down his third bowl of colorful insect fried rice. Sama Pyo gazed at Taishan with sorrowful eyes.

“Taishan. Stop…”

Yes. Please stop.

* * *

It was the largest tree I had ever seen.

Its trunk was so massive that dozens of strong men would have needed to stretch out their arms to encircle it, and its lofty height reached at least several dozen jang.

I couldn’t help letting out an inward exclamation when I saw it, but I hadn’t come here to admire the tree. I had come to meet someone.

“Hey. Get down.”

*Rustle.*

The dense leaves shook. Soon, accompanied by the low growl of a beast, Yayul Mok’s displeased voice reached my ears.

“It’s you again. How did you find out about this place?”

“I asked, and someone told me. They said you come here often.”

“Who?”

“The guy who manages the pavilion.”

“Hwang Gae?”

“Maybe it was Hwang Gae or Ddong Gae. Something like that.”

“He isn’t the sort of person who would tell a Han Chinese that.”

“Maybe not a Han Chinese, but he was pretty forthcoming with my fist.”

“……”

“Come down. My neck hurts.”

I didn’t think he would come down simply because I said my neck hurt, so I kindly added one more thing.

“Before I break the tree.”

“This tree was planted by my ancestors’ ancestors. It took root in this land a full thousand years ago.”

“Then, sometime far in the future, your descendants will say, ‘There used to be a thousand-year-old tree here, but some Han Chinese bastard came and ripped it out by the roots.’ And when the child asks, ‘Why, Mom?’ she’ll say, ‘Because our ancestor wouldn’t come down from the tree when asked nicely.’”

“……”

“So get down before I damage the environment.”

I wondered whether I would really have to pull the tree out if he refused again, but Yayul Mok loved nature even more than I’d expected.

*Swish. Tap.*

*Grrrr.*

A white tiger landed smoothly after stepping on branch after branch. It let out a low growl in my direction.

Yayul Mok lightly stroked the white tiger’s neck, then glared at me.

“You’re insane.”

“Come on. Why are you acting surprised?”

I scratched the back of my head bashfully. Yayul Mok’s face flushed red with anger, and he snarled like a wild beast.

“What happened to Hwang Gae?”

“Ah, that guy? All four limbs are intact. He was a little frightened, though.”

“You’re out of your mind. You came here asking for help, yet you’re oppressing the people of Nanman.”

“You seem to have misunderstood. I really didn’t lay a finger on him. I did grab him by the collar, though.”

I wasn’t some neighborhood thug. I had never gone that far even in the Central Plains.

I always started by speaking gently and only used my fists when that failed. And this time, I had more than enough reason.

“Insect fried rice. Bathwater mixed with filth.”

“What?”

“If that isn’t a traditional custom, then the Nanman Beast Palace’s treatment of its guests is pretty terrible. Don’t you think?”

Yayul Mok furrowed his brow and thought for a moment before muttering as if sighing.

“I think I have a general idea of what happened.”

“If you had a general idea, you should have warned them beforehand.”

“I never expected them to show such blatant hostility…”

Yayul Mok was about to continue when he suddenly closed his mouth. Then he dipped his head toward me.

“I’m sorry. I sincerely apologize.”

“……”

“Oh.”

“What’s with that reaction?”

“It’s nothing.”

I was honestly a little surprised. We hadn’t known each other long, but I hadn’t expected someone as proud and rough as Yayul Mok to bow his head so obediently.

*Is he the type who admits his mistakes immediately and doesn’t hold grudges?*

Making a mistake was easy. Admitting it and offering a sincere apology was much harder.

In that sense, the young Young Palace Lord of the Nanman Beast Palace had a better personality than I’d expected.

“I’ll replace the people responsible as soon as I return. Hwang Gae, of course, as well as everyone else involved. Nothing like this will happen again.”

“Well, if you’ll do that…”

“It was my mistake. I apologize once again, so I hope this doesn’t reach my father’s ears.”

“Why? Does he beat you when you make mistakes?”

Yayul Mok answered with an indignant expression.

“What kind of nonsense are you talking about?”

“If not, never mind. You went so far as to ask me not to tell him, so I thought you might get beaten for three days and three nights.”

“My father has never laid a hand on me even once.”

If his father was the Beast Miao King, I supposed it was possible to raise a son without ever touching him.

With that size and that level of martial power, he could probably give not only his son but also his grandson—and perhaps even his great-grandson—a free pass through puberty.

While I was thinking this, Yayul Mok hesitated, then added in a small voice,

“I may be fine, but the others are a different matter. If my father finds out about this, he’ll come down on them like thunder.”

“Ah.”

“He welcomed you as guests. It’s only natural for you Han Chinese to protest after being treated so poorly. But even so, I have no intention of punishing Hwang Gae or the others.”

“Because they were pissed off over that fucking Dick Demon Escort Bureau?”

“……”

“The name seems a little off, but that is one of the reasons.”

“One of the reasons? That makes it sound like there are others.”

Yayul Mok stared at me silently for a while. Then, as he stroked the chin of the now-quiet white tiger, he opened his mouth.

“The Great Faction War.”

“Hmm?”

“We shed far too much blood in the Central Plains. Under my father’s leadership, all of Nanman’s tribes joined forces, and as many as ten thousand warriors went to the battlefield. But the number of those who returned home alive was less than a quarter of that.”

*Grrr.*

The white tiger quietly accepted the hand stroking it, then looked at its master with worried eyes.

Yayul Mok’s voice continued, heavy with complicated emotions.

“Someone’s parents. Someone’s children. Friends and relatives who had grown up together since childhood. Most of them left for the battlefield with smiles on their faces and never returned. Even I, who was born long afterward, wasn’t exempt.”

“You, too?”

“If things had gone as they should have, I wouldn’t have been able to become the Young Palace Lord. That is the real answer to the question you asked earlier.”

Recalling the conversation I’d had with Yayul Mok immediately after he parted from the Beast Miao King, I suddenly realized.

“You had older siblings.”

“Three. One of them was my elder sister. She was young, and she was a woman, but I heard she was as brave as any warrior. If she hadn’t participated in the Great Faction War, she would have married the man she loved. My father and Uncle Baeksang would have become in-laws as well as sworn brothers.”

“Wait. Then…”

“You’re thinking correctly. In the war between the Han Chinese that they named the Great Faction War, my father lost two sons and a daughter, while Uncle Baeksang had to send off a son he cherished like his own life.”

Yayul Mok gave a bitter smile and added,

“Don’t blame Hwang Gae too much. He lost his parents and every last one of his relatives.”

I had nothing to say, so I simply closed my mouth.

I had heard so much about the Great Faction War from one place and another that my ears were practically ringing with it. But I hadn’t known Nanman had suffered losses on this scale.

No. To be more honest, I hadn’t thought I particularly needed to know.

Nanman lay in the Outer Lands, tens of thousands of li from the Central Plains, and I had thought it was a completely separate land with nothing to do with Murim.

The others who talked about the Great Faction War even now were probably the same.

The only people who had even told me that Nanman had suffered heavy losses were Jeok Cheongang and a tiny handful of others.

*So they must have all been carrying old resentment. The Heavenly Demon Escort Bureau incident from recently must have been the flashpoint.*

Whatever compensation they had received right after the war ended, the wound was still there. And just as that wound was beginning to heal and had barely formed a scab, this had happened.

“Only a few decades ago, we united and risked our lives fighting for the Han Chinese. And now, you killed some of us.”

Yayul Mok’s voice, coldly boiling over, pierced my ears.
## Chapter artifact 628

# Chapter 628

“Only a few decades ago, we united and risked our lives fighting for the Han Chinese. But now, you’ve turned your swords on us.”

At that moment, Yayul Mok was genuinely furious.

More than two hundred people had been massacred in the recent tragedy. Most of the victims had been powerless old men, women, and children.

They had also been members of the Miao people—the same group Yayul Mok belonged to. And after doing something like that, they still had the nerve to ask for help.

“We’ve already shed enough blood. Not for ourselves, but for you Han Chinese.”

Yayul Mok continued in a voice that boiled with anger.

“Nanman will never shed blood in vain again. So stop causing trouble and go back.”

His words were as sharp and decisive as a blade. After finally saying everything he had been holding back, Yayul Mok looked at the Han Chinese man before him with a lighter heart.

*He said his name was Jin Taekyung.*

Until half a day ago, Yayul Mok hadn’t known much about him. Aside from hearing in passing that he was a renowned young prodigy from the Central Plains, he had known nothing.

But if the absurd rumor that Jin Taekyung was a Supreme Peak master was true, he might be one of the three greatest warriors in Nanman—the land where Yayul Mok had been born and raised.

*He blocked Father’s punch, of all things. Maybe the rumor is true.*

Yayul Mok knew better than anyone how formidable his father, Yayul Cheok, was.

Before he had even reached forty, Yayul Cheok had become the greatest warrior in Nanman. He had made the Miao people the strongest tribe, and after earning everyone’s recognition, he had become the lord of the Nanman Beast Palace.

And that wasn’t all. Through his astonishing martial power, he had even made the Han Chinese of the Central Plains—who treated the people of Nanman as barbarians—admire him.

Yayul Mok had heard that his father had earned the sobriquet Beast Miao King around that time.

*I thought Uncle Baeksang was the only person capable of exchanging blows with Father.*

But according to what he had witnessed with his own eyes, Jin Taekyung’s martial arts were astonishing, despite him being at most around Yayul Mok’s age.

He had blocked Yayul Cheok’s punch without much difficulty—a punch Yayul Mok himself couldn’t properly see, much less stop.

Of course, Jin Taekyung had been unable to withstand its force and had retreated nearly one jang, but that was no reason to underestimate him.

*And besides…*

He was big.

He was a head or two taller than an ordinary grown man, with broad shoulders and a muscular build that even his clothes couldn’t conceal.

Standing still and facing him from such a short distance, Yayul Mok felt as if he were looking at a beast that had risen onto two legs.

Perhaps that was why. Or perhaps it was because the eyes and the corners of his mouth—which had always seemed to be smiling foolishly—were now completely rigid.

Without realizing it, Yayul Mok swallowed dryly.

That was when it happened.

“Hey.”

“……!”

“Why are you so startled? I just called you.”

Yayul Mok flinched at the low voice that suddenly cut in, then answered.

“……Wh-why did you call me?”

“Why are you stuttering?”

*Because you’re standing there with that terrifying look on your face, you bastard.*

Until now, Jin Taekyung had always seemed lighter than a feather. But with the smile wiped from his face, it was as if a massive boulder weighing ten thousand jin stood before Yayul Mok.

—Grrr…

The owner’s feelings had even reached the white tiger beside him.

Yayul Mok pretended to remain calm as he stroked the neck of his beloved tiger, which had shrunk back along with him.

“I-I wasn’t stuttering.”

“……”

“Why did you call me, then? If you called me, say what you want.”

“Hmm. It’s nothing important.”

Jin Taekyung looked at Yayul Mok with an odd expression, scratched the back of his head, and continued.

“Thanks for telling me.”

“Huh?”

“I mean, thanks for telling me everything honestly. There were still some things I didn’t know, but thanks to you, I learned quite a few things. I understand the situation around here a little better now, too.”

*What was he talking about?*

This was a completely different reaction from what Yayul Mok had expected.

After staring at Jin Taekyung in silence, he suddenly opened his mouth.

“So what you’re saying is… you’re just going to go back?”

“Hm?”

Jin Taekyung tilted his head.

“Does it work that way?”

“No, but you said you understood.”

“Yeah. Of course I understand. It’s not as if I have some kind of empathy disorder.”

“Then?”

“That’s separate from this.”

“What?”

“This’ll take too long if I explain everything, and my mouth hurts. So let’s cut to the chase and ask one thing.”

Jin Taekyung naturally leaned his back against a tree and continued in a low voice.

“Do you sincerely believe the Great Faction War was a war fought only for the Han Chinese?”

“……!”

“And since we’re on the subject, do you think the Nanman people who died in that war died like dogs for no reason?”

“That’s…”

“That’s what?”

Yayul Mok suddenly found himself unable to speak.

For some reason, no easy answer came to mind.

As he searched through his confused thoughts for something to say, Jin Taekyung’s quiet voice pierced his ears.

“There are two reasons you can’t answer easily, right? First, you know in your heart that what I’m saying is true, but you don’t want to admit it. And second…”

Jin Taekyung held up two straight fingers and tossed out the words.

“Because you’re still a brainless brat.”

“What the hell does that—”

“Don’t ask me. Think it over carefully yourself. Why did the Nanman Beast Palace bring so many warriors and travel tens of thousands of li to help the Central Plains? Was it simply because the ancestor of the Fire Gate Clan put Nanman, which was in chaos, in order a long time ago? If that were true, the white tiger next to you would laugh.”

“……!”

“Most of you Nanman people probably oppose joining the alliance for the first reason. Because you think you only shed blood for nothing. Because you don’t want to repeat that history.”

Jin Taekyung continued with a sigh.

“If you look at it that way, it isn’t entirely wrong. Who the fuck wants war? So what if you fight like hell and gain land, gold, and silver treasures? People are dying like ants in every direction. And some of those ants might be my friends, my family, or my lover. They could even be me—or you. By the way, do you have a girlfriend?”

At the unexpected question, Yayul Mok shook his head without thinking.

“An ex-girlfriend?”

“What exactly is this ‘girlfriend’ you’re talking about?”

“A lover. Or a romantic partner. A being with a physical structure different from a man’s who dates you while harboring tender feelings for you.”

“Uh, no.”

“Oh. You did have one?”

“No.”

“So you did have one?”

“……I’ve never had one. Not even once.”

“How old are you?”

“Twenty-six.”

“What a guy. A promising candidate for the virgin-boy technique. If you hold out like this for fifty years, you might even become a Martial God. Fine, let’s take lovers off the list of victims.”

For some reason, Jin Taekyung smiled with satisfaction.

Yayul Mok’s mood soured, and all the strength drained from him.

The man was impossible to understand, and he was having an impossible-to-understand conversation.

“What the hell are you trying to say? Why did you suddenly go off on a tangent about lovers?”

“Who knows? I’m not entirely sure myself, but one thing is certain.”

Jin Taekyung’s faint smile disappeared as he continued calmly.

“The sacrifice of the Nanman people who left their homeland long ago and fell in the Central Plains wasn’t a pointless death. And if the same thing happens again, it won’t be pointless this time, either.”

“……”

“I’m sincerely sorry about what happened with the Heavenly Demon Escort Bureau. But if there were people crazy enough to do something like that… I would have killed them myself.”

“Even though they were Han Chinese like you?”

“What does that have to do with anything?”

Perhaps it was his imagination. But for some reason, Yayul Mok felt as if he had been unable to respond several times today.

With his mouth pressed tightly shut, he stared at Jin Taekyung and tossed out one final remark.

“No matter how pleasant your words sound, Nanman will not help the Central Plains.”

“It’ll probably be difficult, but we still have to try persuading you.”

“It’s pointless.”

“What?”

“The matter is as good as decided. The conclusion was reached at the first tribal council held fifteen days ago.”

“That makes it sound as if there’s going to be a second one.”

“Nanman is vast, and it takes considerable time for thirty-two tribes to gather in one place. That is why the four great chieftains, including my father, review matters first.”

“And the result was opposition to joining the alliance? Go on.”

“In three days, all the tribes of this land will gather in one place for a council. But the great chieftains other than my father have already made up their minds, so little will change.”

Yayul Mok’s words were true.

The Nanman Beast Palace was a symbol of harmony, but that did not mean the tribes were equal.

If three great chieftains, led by Baeksang, the great chieftain of the Bai people, united their opinions, then even the Beast Miao King—the greatest warrior in Nanman and lord of the palace—could not decide to join the alliance as he pleased.

*Because those were the rules here.*

Yayul Mok muttered the words inwardly as he watched Jin Taekyung carefully.

How would that young and powerful Han Chinese from the Central Plains react?

Now that Nanman’s joining the alliance was practically impossible, he was curious about what Jin Taekyung would do.

*He’ll probably be disappointed. If not, he’ll surely exhaust himself trying to persuade us somehow…*

“First, I’ll do whatever I can. If it doesn’t work, then it can’t be helped.”

“Huh?”

Yayul Mok was confused without realizing it.

Jin Taekyung’s reaction was so calm and unconcerned that it was completely outside his expectations.

“B-but the result is already decided, isn’t it?”

“Yeah. But you said it isn’t over yet.”

“That’s true, but…”

*What is this?*

Yayul Mok asked in bewilderment.

“Shouldn’t you try to persuade us no matter what?”

“That’s why I said I’d try first. If it doesn’t work, then I’ll go back. Of course, I’ll take care of something more important first.”

“Something more important?”

“You seem to be misunderstanding something.”

Jin Taekyung scratched his chin and continued.

“I didn’t come here as a diplomat. If I had to put it another way, I came here as a firefighter.”

“A firefighter? What is that?”

“Someone who puts out fires.”

“Didn’t you set fire to the pasture as soon as you arrived?”

At Yayul Mok’s genuinely curious question, Jin Taekyung was silent for a moment before answering.

“Well, that was just a metaphor. To put it bluntly, I’m not particularly talented at persuading people.”

“That much seems to be true.”

“…You fucking bastard. Now I’m getting annoyed for no reason. Anyway, it’d be a shame if Nanman didn’t join us, but if trying doesn’t work, there’s nothing we can do.”

“But you’re Han Chinese. And aren’t you also a member of the Murim Alliance?”

“So?”

“I don’t know the exact circumstances, but I know well enough that the Central Plains is in danger. At a time like this, when you should be begging us for help no matter what, you came to help us?”

At Yayul Mok’s gaze, which seemed to be examining some strange creature, Jin Taekyung let out a quiet laugh.

“What are you going to do if the pasture catches fire again like last time?”

“Put it out immediately.”

“Why?”

“If we don’t put it out, the flames will spread in every direction.”

“Good. There’s your answer.”

“……!”

“Don’t overthink it. There’s a fire, so I’m trying to put it out. Just like the Nanman people of this land who left their homeland and headed for the Central Plains decades ago.”

After a brief silence, Yayul Mok spoke with a complicated expression.

“Then are you saying you came here simply to help us… without asking for anything in return?”

“What if I did?”

“I don’t believe you.”

“Believe whatever you want. Ah, but before that…”

Jin Taekyung naturally turned around and began walking. Then he continued with a suddenly hardened expression.

“At least feed me properly, asshole.”
## Chapter artifact 629

# Chapter 629

After parting ways with Yayul Mok, I turned my steps toward the temporary lodging where the Fire Dragon Pavilion members were waiting.

Even if my martial prowess meant there was no danger of anyone trying to harm me, there was nothing to be gained from wandering around alone in an atmosphere like this.

And as I walked, I somehow found myself in the Outer Hall of the Nanman Beast Palace.

“Good grief. When did I get here?”

Muttering to myself, I looked around.

Perhaps because it was hidden among the thick, overgrown grass, I couldn’t see a single rat anywhere…

Well, that wasn’t quite true.

Two or three monkeys—mascots of Nanman much like Gukkeoni is for the Ministry of National Defense—were milling around.

—Screech?

*Why has that Han Chinese bastard crawled all the way out here instead of quietly hiding in his lodging?*

The monkey’s curious eyes seemed to be asking that, but I had nothing to be ashamed of before the heavens.

*What do you want me to do? I got lost.*

Of course, following the teachings I had received from the greatest assassin of all time, who wore the guise of the Divine Physician, I had concealed my breathing and moved stealthily so that no one else would notice me.

But one thing was certain.

I had gotten lost.

The temporary lodging was less than fifteen minutes away, and there were only two possible roads, but that was beside the point. If I had gotten lost, then I had gotten lost.

*Still, I came here representing the Murim Alliance. I should at least be able to figure this out on my own.*

A fellow recruit had said something like that back when we were at the Hunter training center.

*A perfect lie is a true story.*

In the end, all that mattered was not getting caught. Of course, given the circumstances, I still had to make an effort not to get caught.

*Rustle.*

After steadying my breathing, I slipped out of the grass and blended into the people gathered nearby.

I erased my presence and reined in my aura. At the same time, I bent forward slightly to lower my height and melted into the crowd.

Exactly as Mungyeong had once taught me.

*Do you know who the most frightening assassin in this world is?*

*I do. The person standing right in front of me.*

*……*

*I’m sorry. I’m sorry. I’ve committed a crime worthy of death. Please put away the dagger in your sleeve and teach this foolish disciple.*

Mungyeong had glared at me with an expression that seemed to ask whether he should kill me or not, then answered.

*An ordinary person.*

*Ordinary?*

*Someone more ordinary than anyone else, someone who blends naturally into any place. That is the most frightening assassin.*

What Mungyeong had taught me back then didn’t apply only to assassins.

He had mentioned it in passing, saying it was nothing more than a simple miscellaneous skill that couldn’t even be called martial arts. But I hadn’t forgotten his teaching, and I had found plenty of opportunities to put it to good use.

Just like now.

*This really is different from the Central Plains. Completely different.*

I turned my head as naturally as possible and surveyed the various parts of the Outer Hall.

The Nanman Beast Palace was a truly distinctive place, even after seeing it again.

It was less like a sect than a small city, and all kinds of different peoples lived together within that city.

Compared to the Central Plains, where the Han Chinese made up the majority, Nanman was practically a melting pot of races.

A Miao woman draped in colorful jewelry strode through the market, enjoying the attention of the people around her, while a Bai merchant in white traditional clothing tried to conduct a trade with a monkey perched on his shoulder.

And then there was an old man limping straight toward me.

*No, sir. Why are you coming this way?*

“Excuse me. I’m trying to buy some cloth at the market. Which shop would you recommend? If I were ten years younger, I could have found it with my eyes closed, but perhaps it’s because I’m old that I can’t remember anything these days.”

“Uh…”

Had I blended in too naturally? I hadn’t expected this.

The non-Han old man had blocked my path with his cane and asked me the question. I hesitated for a moment, then answered as shamelessly as possible.

“Go straight ahead, then turn into the alley on the right.”

“The alley on the right? Was there a cloth shop there?”

*I have no idea either, sir.*

But contrary to my thoughts, I nodded.

“Yes. There are plenty. More than the hairs on your head. They’re springing up everywhere.”

“Really? What’s the name of the shop?”

*Why do you need me to tell you the name, too?*

But if I hesitated now, he would become suspicious. I blurted out the first shop name that came to mind.

“Hyuk Family Cloth Shop. Their quality is pretty good.”

“Hyuk Family Cloth Shop? I don’t think I’ve heard of it before…”

I had underestimated the old man’s local experience.

It was clearly an unreasonable answer, but in situations like this, the shameless person won. With an expression utterly free of shame, I spoke firmly.

“It’s been around for more than ten years.”

“Really? How strange. As far as I remember, it was definitely…”

“Isn’t that why you asked me? Because your memory is getting hazy?”

“That’s true, but…”

“Sir, if you don’t mind my asking, how old are you this year?”

“Me? I’m eighty-two.”

“I’m twenty-two. I still vividly remember moving from my father’s side to my mother’s side.”

“You remember that…?”

“I’m only twenty-two, so I remember everything. So please trust me.”

“Ah, all right. In any case, thank you.”

The old man, defeated in the battle of sheer confidence, was about to leave when I suddenly remembered something and hurriedly opened my mouth.

“Excuse me. Sir?”

“Yes? What is it?”

“Where is the place with the biggest crowd right now? I was supposed to meet someone, but that bastard isn’t showing up anywhere, so I’m going to look for him myself.”

“If that’s the case, go over there. I caught a glimpse of it on my way here, and I don’t know what exactly was happening, but it was terribly noisy. Perhaps it’s because of the festival that will be held in a few days.”

Just then, the old man, who had pointed in a direction with his cane, seemed to pause. Then he stared closely at my face with his cloudy eyes.

“By the way, which tribe are you from?”

“What?”

“Judging by your appearance, you don’t seem to be from the Yao people like me. It’s quite strange that you speak our language so fluently…”

“Oh, I can see it over there. Please be careful on your way.”

“Hey. Wait.”

I left the non-Han old man behind and hurried away.

No matter how naturally I blended in, if I gave someone enough time to study my face, they were bound to notice something.

The difference wasn’t large enough to make me stand out immediately, but there were still certain distinctions between the appearances of Nanman’s non-Han peoples and the Han Chinese.

But that didn’t mean there was no solution.

Fortunately, my hands were very fast. And as luck would have it, the market was packed with non-Han people, while the merchant selling traditional animal masks was too busy dealing with customers pouring in from every direction to pay attention to anything else.

To put it simply, there was no problem with slipping a mask into my possession.

*Open Inventory. Store.*

*Ding.*

> **System**
>
> You have acquired **Crudely Made Tiger Mask**!

What was faster than the eye wasn’t the hand.

It was the System.

After putting the mask into my inventory and naturally passing two or three people, a tiger mask painted with crude dye had been placed over my face.

*This should be enough. I won’t stand out much in this neighborhood.*

Was it because of the festival the old man had mentioned? If there were ten people in sight, two or three of them were wearing masks similar to mine.

I walked in the direction the old man had shown me, listening to the voices drifting over from various places.

“Have you heard the news? The great chieftains of the Yi and Yao peoples have returned.”

“Really? I thought they left about fifteen days ago to subdue the man-eating beasts.”

“They mobilized around five hundred warriors, so they must have finished quickly. Unlike the Yao people, it seems the great chieftain of the Yi people didn’t achieve any noteworthy results, though.”

“It’s exactly what I expected. Not that I was expecting much.”

I didn’t miss the familiar information exchanged in their conversation.

*The Yi people. And the Yao people.*

Together with the Miao and Bai peoples—led respectively by the Beast Miao King, lord of the Nanman Beast Palace, and Baeksang, whom I had briefly encountered earlier—the Yi and Yao peoples made up Nanman’s four most powerful tribes.

I recalled the information Namho had told me on the way to the Nanman Beast Palace.

*The four great tribes of Nanman are the Miao, Bai, Yi, and Yao peoples. The Miao people are the strongest, followed by the Bai people.*

*Then what about the Yi and Yao peoples?*

*If you were talking about twenty or thirty years ago, the Yi people would have been ahead.*

*That sounds like you’re saying they aren’t anymore.*

*That much time has passed. People say the great chieftain of the Yi people, who inherited his position from his late father, isn’t very strong-willed. The Yao people, on the other hand, have grown considerably. They gained an outstanding leader. No man could have accomplished as much, no matter whom they put in that position.*

*Could it be…?*

*Your guess is correct. The great chieftain of the Yao people is a woman. Extremely intelligent, and extraordinarily beautiful.*

At that moment, the thoughts continuing in my head abruptly came to a stop.

Not by my own choice, but because of an outside force.

The thing that interrupted my thoughts was the clear sound of a musical instrument reaching me faintly from far away.

*Fwoooosh.*

A gentle melody carried on Nanman’s hot, humid wind crossed the wide space and reached my ears.

The noisy market fell silent in an instant, and a short exclamation escaped someone’s lips.

“Ah…”

That exclamation was impossible to suppress—truly involuntary.

The melody reaching my ears was that pure, and the procession that emerged as people retreated in a flurry was both splendid and beautiful.

*Thump. Thump. Thump.*

Hundreds of men and women continued forward in the procession to the accompaniment of low drums.

The Yi men wore black tops edged with floral cloth and wide, pleated trousers.

The Yao women wore conical hats and moved slowly forward in two separate groups.

“Wow.”

“The Yi and Yao people have arrived!”

Cheers burst out from every direction.

But while everyone around me marveled at their beauty and striking appearance, I was looking at the weapons strapped around their waists and shoulders.

*Every single one of them is a warrior.*

A warrior of Nanman was equivalent to a Murim practitioner in the Central Plains. Since these people belonged to their respective tribes, it would be more accurate to call them members of a martial sect.

*And from what I just heard, the great chieftains of the Yi and Yao peoples returned after finishing their campaign…*

This wasn’t merely a procession. It was a kind of victory parade, and a victory parade like this was never complete without the general who had led the battle to victory.

And the generals in question were the great chieftains of those two great tribes I had just heard about.

“Oh!”

“Th-there…!”

A short cry of alarm reached me just as I was thinking that.

In the next moment, countless gazes and voices focused in one direction. Then, without anyone taking precedence over anyone else, a tremendous cheer erupted.

“Waaaaaaaaah!”

Amid the roar that seemed capable of shaking all of Nanman beyond the Outer Hall, two people finally appeared at the center of the procession and waved their hands.

One was a man riding a huge black bear, presumably the great chieftain of the Yi people.

And the other was…

“Yohi! Great Chieftain Yohi!”

A woman who smiled brightly amid an outpouring of attention and affection that surpassed the man’s by comparison.

Even if I hadn’t heard the people shouting her name, I would have quickly realized that she was the great chieftain of the Yao people.

*The great chieftain of the Yao people is a woman. Extremely intelligent, and extraordinarily beautiful.*

Namho’s words had been true.

Yohi was beautiful. Almost bewitchingly so.

Whenever her deep gaze swept across the surroundings, people let out exclamations of admiration.

That was probably why.

Amid the cheers and wonder surrounding her, I stood there like a block of wood, making me unusually conspicuous.

“……!”

Yohi’s eyes lit up when they found me.

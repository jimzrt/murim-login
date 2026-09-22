# Checkpoint Review — 630–634

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

# Chapters 630–634

## Plot

Yohi identifies Jin Taekyung beneath his tiger mask and reveals that the four great chieftains generally oppose Nanman joining the Murim Alliance. She seeks to place the Yao people at the center of Nanman’s power structure, while Heugung, the Yi great chieftain, remains under her and Baeksang’s influence. Baeksang recognizes Jin as well and confronts him, arguing that Nanman has already sacrificed enough for the Central Plains. His anger at Jin’s mention of someone’s son leads Jin to suspect a connection to Head Elder Jin Baekyang.

After two days of fruitless investigation for Dark Heaven traces, Yayul Cheok secretly summons Jin and Namho. Their discussion of Baeksang’s loyalty is interrupted by an urgent warning from Ailao Mountain and the System quest **Unknown Omen**. Cheok mobilizes the Nanman Beast Palace, while Yayul Mok organizes the Miao warriors and palace defenses. Jin and Cheok race to Ailao Mountain, the former headquarters of the destroyed Five Poisons Sect and a forbidden land filled with proliferating poisons and beasts.

At the mountain, they find a poisoned sentry and more than a hundred elite Nanman guards massacred. The victims suffered poison, crushing force, and dismemberment, while nearly all their accompanying beasts have vanished. A colossal Black Tiger then emerges, identified by the System as **Ailao Mountain’s Wraith**.

## Continuity

- The second Nanman tribal council is scheduled for the following day, though the Ailao Mountain crisis may disrupt it.
- Yohi wants Yao influence to dominate Nanman. She and Baeksang control Heugung, making him a possible but unreliable persuasion target.
- Baeksang remains firmly opposed to joining the Murim Alliance. He is Yayul Cheok’s lifelong friend and sworn younger brother, but Jin and Namho question whether he can still be trusted.
- Baeksang bears a burn scar from Jeok Cheongang. His reaction to Jin’s mention of someone’s son may connect him to Head Elder Jin Baekyang, but this remains unconfirmed.
- The Fire Dragon Pavilion found no Dark Heaven traces around the Nanman Beast Palace, but betrayal has not been ruled out.
- Yayul Cheok and Jin Taekyung are investigating Ailao Mountain under **Unknown Omen**, a time-limited quest with five hours remaining when accepted.
- Yayul Mok has taken the Seven Miao Tigers to mobilize the Miao warriors and prepare the palace’s defenses. Namho returned to warn the Fire Dragon Pavilion. White Tiger is temporarily carrying Jin.
- Ailao Mountain has been forbidden for over a century. Three hundred elite Nanman warriors rotate through its guard posts, and the four great chieftains conduct annual extermination campaigns there.
- More than a hundred guards have been killed, while most of their beasts are missing. The Black Tiger appearing at the site is identified as Ailao Mountain’s Wraith.
- Unresolved: whether Dark Heaven caused the massacre, whether the mountain’s beasts acted independently, whether they are being controlled, and why the beasts disappeared.

## Translation Decisions

- Use **Heugung** for 흑웅; do not translate it as “Black Bear.”
- Use **Black Tiger** for 흑호 and **Ailao Mountain’s Wraith** for 애뇌산의 망령.
- Use **Transcendent** for 초일류.
- Render **Fire King hand pie** and **Wind Style: Mouth Dragon** as Jin’s established jokes.
- Render **Insi** as the shichen from three to five in the morning.
- Retain **Muyaho** as White Tiger’s personal name and preserve the explanatory sense of *seori* as stealing produce from a field.
- Continue using **Beast Miao King**, **Young Palace Lord**, **great chieftain**, **Miao people**, **Bai people**, **Yi people**, and **Yao people**.

## Durable state

{
  "active_continuity": [
    "Ailao Mountain has been a forbidden zone for more than a century, guarded by three hundred rotating elite Nanman warriors and subject to annual small-scale exterminations led by the four great chieftains.",
    "More than a hundred elite warriors stationed at Ailao Mountain have been massacred by varied physical attacks and deadly poison, while most of their accompanying beasts are unaccounted for.",
    "Jin Taekyung and the Beast Miao King are investigating the Ailao Mountain crisis under the active time-limited quest.",
    "A giant Black Tiger has appeared at the massacre site, and the system identifies it as Ailao Mountain's Wraith."
  ],
  "continuity_sources": [
    634,
    633
  ],
  "open_questions": [
    "Did Dark Heaven cause the Ailao Mountain massacre, did the mountain's venomous beasts act independently, or are the beasts being controlled by Dark Heaven?",
    "Why are nearly all of the warriors' accompanying beasts missing from the massacre site?",
    "What is the relationship between the giant Black Tiger and Ailao Mountain's Wraith?",
    "Can Jin Taekyung and the Beast Miao King identify the attacker before the investigation timer expires?"
  ],
  "safe_through": 634,
  "temporary_decisions": [
    "Use Black Tiger for 흑호.",
    "Use Ailao Mountain's Wraith for 애뇌산의 망령.",
    "Use Transcendent for 초일류."
  ],
  "version": 1
}

## Reading copies

## Chapter artifact 630

# Chapter 630

The moment I covered my face with the mask, I let my guard down. That was my mistake.

Should I have stamped my feet and clapped like everyone else?

The thought only occurred to me now, but it was already too late. Even at this very moment, Yohi’s gaze was fixed directly on me.

Still, it shouldn’t become a problem. The only thing that made me stand out was the fact that I had been standing there awkwardly without joining in.

The chances of the Yao people’s great chieftain—the star of this splendid victory parade—showing any further interest in me were close to zero.

“You there.”

“……”

I said close to zero. I never said zero.

*Damn it. So she really is calling me.*

Yohi was looking straight at me, so I cautiously turned around, just in case.

“Yes. You who just turned around.”

Fortunately, I wasn’t the only person who had just looked back.

At Yohi’s sudden and unexpected action, the people gathered in the marketplace began murmuring and turning their heads in every direction like meerkats.

“The person wearing the tiger mask.”

I swiftly scanned my surroundings. There were about a dozen people wearing cool-looking tiger masks, including me. Those were reassuring odds.

Buying a tiger mask had been the right choice. Of course, I hadn’t paid for it.

“The seven-foot-tall man wearing a tiger mask who just made eye contact with me. That’s enough. Come forward.”

The tiger-mask lottery’s value plummeted with the sudden addition of gender and height requirements. Now that my odds of being the winner had shot up, I could almost feel sweat beading on my forehead.

I hurriedly lowered my head to avoid Yohi’s gaze, then discreetly crossed my legs.

After hiding my Black Anaconda perfectly between my legs, I raised my head—and met Yohi’s gaze, which had gone completely cold.

“……”

“……”

The procession, which had continued amid the cheers, had come to a stop some time ago.

Under the suffocating silence that had settled over the marketplace and the gazes of Yohi and countless others, I uncrossed my tightly clenched legs and opened my mouth in a solemn voice.

“Um, did you call for me?”

“……”

“……”

They only looked back and forth between my masked face and my lower body. No one answered.

*Shit. I should’ve just stepped forward when she first called me.*

* * *

A leader needed many virtues. Among them, a keen eye was essential.

“I had a strange feeling the moment I saw you.”

After the celebratory procession for the subjugation of the man-eating beasts ended, Yohi had sent an attendant to summon me privately. Now she continued in her languid voice.

“Somehow, you were the only one who seemed out of place among all those people.”

Beside her, the great chieftain of the Yi people, who had been popping fruit into his mouth nonstop, grinned broadly and chimed in.

“She’s right. You were standing there like a block of wood all by yourself. You really stood out.”

The middle-aged man had a plump build that didn’t suit a warrior. He waved his hand, still damp with fruit juice, in greeting.

“You’re quite a rude fellow, keeping your mask on even now. I don’t know who you are yet, but you already know who I am, don’t you? I’m Heugung, and I lead the Yi people.”

Heugung. The name meant Black Bear.

So that was why he had been riding a bear during the procession. Apparently, people around here routinely kept fierce animals named after themselves as pets.

*What am I supposed to say to that?*

In truth, now that things had turned out this way, I had been planning to take off my mask and reveal my identity. That was why I hadn’t slipped away beforehand.

But Yohi was far more perceptive than I had expected.

“You can leave the mask on. Jin Taekyung of the Jin Family of Taiyuan.”

“Hmm?”

“Oh?”

I was a little surprised. First, because Yohi had only just arrived, yet already knew my identity. And second, because Heugung—the other great chieftain—was even more shocked than I was.

At the sight of Heugung and me both freezing for a moment, Yohi let out a quiet laugh.

“Why are you so surprised? I already heard that the Palace Lord brought the Han Chinese group sent by the Murim Alliance into the Inner Palace.”

Heugung tilted his head with a bewildered expression.

“Han Chinese from the Murim Alliance? Really? I hadn’t heard anything about that.”

“That’s because you’re as slow as a foolish bear. Though that side of you is charming.”

Even the Skeleton King would have realized that her added compliment was nothing more than lip service, but Heugung only grinned happily.

“Are you being sincere?”

“Of course. Don’t forget that I’ve always been in love with you.”

Her voice and gaze were alluring. When her pale, flawless fingers—so white and unblemished that it was hard to believe she was from Nanman—stroked his pockmarked cheek, rapture spread across Heugung’s face.

“Ahh. My dear.”

If someone asked me to describe this scene in three words, I would have answered without hesitation.

*Ugh. Fucking hell…*

A middle-aged man in his fifties with a bulging belly was melting like butter beneath the touch of a woman in her twenties.

People said that love knew no age or borders, but at this point, they would have to invent new ones.

*Not that it was real love anyway.*

Now I understood why the Yi people’s power had been dropping day by day like a stock awaiting delisting. I also understood why the Yao people had been able to grow so strong.

*Still… different as they are, there are some similarities.*

Just as I was thinking of someone else, Yohi glanced at me and stroked Heugung’s shoulder.

“But, big brother.”

“B-big brother?”

It was a line I had heard a few times in the daily dramas my mother liked to watch.

*Don’t call me Manager. Call me Oppa.*[^1]

Yohi had struck precisely the sort of nerve that could drive a pathetic middle-aged man insane. Her gentle voice continued as Heugung looked ready to die from happiness.

“Would you mind stepping outside for a moment? There’s something important I want to ask this Han Chinese man.”

“Hmm? Of course. I should. If that’s what you want, I’ll do anything!”

“Thank you, big brother. See you later.”

“Ooh. Oooooh!”

Heugung left the tent with an excited face, forcefully exhaling through his nose. Yohi let out a quiet laugh, leaned against the silk bedding, and muttered.

“Fucking moron.”

I had roughly expected something like this, but it was worse than I’d imagined. As I scratched my chin, Yohi raised the corners of her mouth.

“What? Was I too obvious?”

When someone came at you this directly, it was actually easier.

I thought for a moment, then answered honestly.

“Well, you’re not wrong.”

“You weren’t particularly surprised, so I suppose you had already figured it out. I thought you were only good at martial arts, but you’re more perceptive than I expected.”

“It’s not a personality that’s completely unheard of. The Central Plains has more than a few people who are different on the inside from what they show on the outside.”

“Really? I suppose the Central Plains must be very large. A bitch like me is rare in Nanman. Oh, is that girl who came with you the same sort? I think I heard her name was… Ju Hwaran?”

I stared at Yohi instead of answering. The smile at the corners of her mouth grew even broader.

“Fine. I take it back. Judging by your expression, I must have said something I shouldn’t have.”

I didn’t know what expression I had made at that moment. But it probably wasn’t a particularly kind one.

That was just how it felt.

With a strange feeling in my chest, I forced myself to speak calmly.

“Watch what you say next time. She’s a member of the Fire Dragon Pavilion who trusted me enough to follow me all the way to Nanman.”

“Oh? Just a subordinate you care about?”

“I don’t really distinguish between people based on whether they’re superiors or subordinates… but think whatever you want.”

“I appreciate you putting it that way. I happen to have quite a vivid imagination.”

Yohi let out an enigmatic laugh, apparently imagining something, then continued.

“You were staring at me so intently earlier that I got the wrong idea. I wondered if you had fallen in love at first sight.”

“As if. I’m not the kind of guy who just likes anyone.”

“Then why were you looking at me like that? Did Heugung, that fucking moron, look pathetic to you?”

“No. You reminded me of someone I’d seen before.”

Interest appeared in Yohi’s eyes.

“Who? A woman?”

“A woman, yes. You wouldn’t know who she was even if I told you now.”

In truth, she was closer to a monster than a woman. The person Yohi had reminded me of was the Southern Heaven Demon Empress.

The people belonging to Dark Heaven were monsters to whom distinctions between men and women meant nothing. They were fanatics who worshipped the Lord of Heaven.

“Hmm. A woman… Does she resemble me that much?”

“A little. But fundamentally, you’re different.”

“How can you be so sure? I could be that woman, you know?”

Yohi made a mischievous face, but I had already checked with Qi Sense just in case. There wasn’t even room for confusion.

*Like I said, the two of them were fundamentally different.*

If Yohi’s appearance and air were bewitching, the Southern Heaven Demon Empress possessed a magic all her own that could ensnare people.

And that wasn’t limited to her looks.

*Her atmosphere.*

The Southern Heaven Demon Empress had a distinctive air that was both beautiful and natural—and because it was so natural, impossible to suspect.

Even I had only realized how dangerous her beauty and atmosphere were after she completely deceived me in Hubei Province.

“Either way, you’re different.”

“Hmm. How boring. Whoever she is, she must be important, then?”

“She is. More than that, she’s dangerous.”

“Dark Heaven. It’s Dark Heaven, isn’t it?”

Yohi was perceptive indeed. She already knew why I had come to Nanman, tens of thousands of li away from the Central Plains, and what I had come here to do.

“I’m sorry to tell you this, but none of the great chieftains of the four great tribes want to join the alliance. Not a single one—except the Palace Lord.”

“What about you?”

“Me? I don’t particularly care either way. No matter what losses the Nanman Beast Palace suffers, I want our Yao people to unite the four great tribes under us.”

“That’s just your opinion. The other tribal chiefs…”

“Of course, there are chiefs who don’t think that way. But one thing is certain. Most of them share the desire for their tribes to grow stronger. And if they shed blood for nothing in the Central Plains, their power within Nanman will naturally diminish.”

I suddenly remembered what the Beast Miao King had told me earlier in the Inner Palace.

He was the lord of the Nanman Beast Palace and one of the Ten Kings recognized even in the Central Plains, but ultimately, he was still the great chieftain of the Miao people.

If the chiefs who controlled every large and small part of Nanman thought the same way as Yohi, then, just as Yayul Mok had said, it was effectively impossible for the Nanman Beast Palace to join the Murim Alliance.

*God, the negotiation difficulty here is fucking ridiculous.*

I hadn’t come to Nanman as a diplomat, but this situation was still as good as a failure before it had even begun.

Yohi looked amused by my bewilderment.

“I’m sorry, but that’s reality. Ah, of course, there’s at least one person you might have a chance of persuading. He leads a tribe large enough to rank among the four great tribes, and he’s so stupid that it’s hard to believe.”

I already knew who she meant from that description alone. I spoke with a sigh.

“Heugung?”

Yohi burst into loud laughter.

“Yes, that fucking moron. He can’t do a thing with me and that old man Baeksang keeping him firmly under our thumbs anyway.”

“……”

Even so, he was the great chieftain of a huge tribe that raised quite a few bears in Nanman. Was this treatment for real?

Just thinking about Heugung made my heart shrink.

*And if I really had any chance of persuading Heugung, she wouldn’t have kindly told me about it.*

Heugung was nothing more than a puppet, grinning idiotically without even realizing that he was being manipulated by Baeksang and Yohi.

*Was she messing with me or what?*

Just as I was frowning at Yohi, the area outside the tent suddenly grew busy, and a voice reached us.

“Yohi. Are you in there?”

It was a cold, dry voice.

Baeksang.

[^1]: *Oppa* is a Korean form of address used by a woman for an older brother or older man, often with romantic overtones.
## Chapter artifact 631

# Chapter 631

There are times when you get that kind of feeling.

The feeling that someone dislikes you even though all you’ve done is meet their eyes. The feeling that no matter how hard you try, you could never become friends.

My second meeting with Baeksang, the great chieftain of the Bai people, was like that.

“You…”

Even with my face concealed behind a mask, Baeksang knew exactly who I was. Then again, considering his martial prowess, it wasn’t all that surprising.

*At least the early stage of Supreme Peak.*

That was my estimate of Baeksang’s level.

A Supreme Peak master was someone whose level couldn’t easily be found even in the Central Plains. It would have been stranger if he failed to recognize me just because I had covered my face with a crude tiger mask.

Martial artists who had reached a certain realm could identify their opponents by their aura.

But the important thing wasn’t that Baeksang had recognized me at a glance. It was that he showed no pleasure at seeing me.

“So we have an unwelcome guest.”

Not a welcome guest, but an unwelcome one.

If he had said that during our first meeting, it would have scratched my tender heart. But after hearing all sorts of information beforehand, I remained relatively calm.

I scratched the back of my head and answered.

“As they say, even if your mouth is crooked, you should still speak plainly. To state the facts exactly as they are, I’m not an unwelcome guest. I was invited here.”

“Invited?”

His gaze shifted naturally.

Yohi, whose eyes had met Baeksang’s, smiled sweetly and opened her mouth.

“It’s true. I called him here.”

A beautiful woman’s smile was usually highly effective, but Baeksang was clearly not that sort of man.

“Are you planning to collude with the Han Chinese?”

At his even colder tone, Yohi gave an exaggerated shrug.

“Collude? I was merely a little curious. It’s not as though we met alone from the beginning.”

“But only the two of you—and the heavens—know what you discussed after sending Heugung away.”

“Please put your needless concerns aside. I haven’t forgotten the promise we made that day.”

I didn’t know what promise they had made that day, but even hearing about it gave off a distinctly suspicious odor.

Baeksang’s gaze sank even deeper.

“You’re saying pointless things in front of a Han Chinese man, Yohi.”

*Fwoosh!*

An invisible wave of aura flowed from Baeksang’s entire body and swept through the tent.

The air grew heavy in an instant. As the pressure of a Supreme Peak master bore down from every direction, the smile on Yohi’s lips finally began to fade.

That was when I abruptly opened my mouth.

“Come on. There’s a Han Chinese guy standing right in front of you, hearing all this, so let’s stop calling me ‘bastard’ over and over.”

*Whoosh.*

The air, which had been growing heavier by the moment, suddenly lost its force.

Baeksang’s eyebrows twitched as my words simultaneously disrupted the aura surrounding us.

“You bastard.”

“Jin Young Hero, Pavilion Head Jin, Blazing Flame Divine Dragon, or you. Pick whichever title you like and use it. At this point, I’m getting confused about whether I’m from the Jin Family of Taiyuan or the Bastard Family of Taiyuan.”

“……!”

“I do speak well, don’t I? I know. Of course, I trust you understand that I didn’t become a Pavilion Head of the Murim Alliance just by running my mouth. If I had, my sobriquet wouldn’t be Blazing Flame Divine Dragon. It would have been something like Wind Style: Mouth Dragon.”

From my behavior and words, Baeksang must have realized two things for certain.

First, my martial prowess was by no means inferior to his.

Second, I wasn’t merely some green young Han Chinese. I held a high-ranking position as a Pavilion Head in the Murim Alliance, which had been formed from the martial world of the Central Plains.

Even if only one of those facts were true, I was not someone who could be casually dismissed.

Baeksang stared at me in silence for a while before abruptly opening his mouth.

“Now that I see you again, there’s no doubt that you’re the successor of the Fire Gate Clan. Your words and actions, which disregard all consequences, are truly worthy of the Fire King’s Disciple.”

“Old Master—no. Have you met my Master before?”

“The Palace Lord and I were always together. That was true even on the day I first met the Fire King I had only heard about.”

I asked on a sudden hunch.

“Oh. Then, could it be…?”

“Before we had time to do anything, the Palace Lord fell in an instant. Then I was next. It was because I called him a crazy old man.”

Baeksang slightly lifted the white robe he was wearing, revealing the burn scar remaining along his side.

“……”

What was this? It wasn’t as though someone had graded a piece of beef.

*At this point, it’s practically a certification mark.*

Baeksang showed me the traces of the piping-hot Fire King hand pie he had eaten decades ago, then continued in a cold voice.

“It happened a long time ago. But whenever I look at the scar, I remember that day.”

Jeok Cheongang had once told me to be careful of gratitude and grudges in the Murim.

And now, the gratitude and grudges Jeok Cheongang had accumulated in the past were coming back to me like a boomerang.

*Is this that Murim-style gratitude-and-grudges payback thing?*

I was momentarily at a loss for words. Baeksang stared at me with deeply sunken eyes.

“I don’t care whether you’re the Fire King’s Disciple or a Pavilion Head of the Murim Alliance. Nanman has already shed enough blood for the Central Plains, and the Palace Lord’s judgment was wrong.”

“……”

“That is all I have to say to you. So disappear from my sight at once. Before I take matters into my own hands.”

Baeksang’s mood was extremely menacing, and instead of arguing, I rose from my seat.

Not because I was afraid of him, but because there was more to lose than to gain. This was a time to think calmly.

*Step.*

I was about to leave the tent when I suddenly stopped.

I had thought of something I wanted to say to Baeksang, whom I might not see again for some time.

“The blood wasn’t shed for the Central Plains.”

“What?”

“The blood you shed wasn’t for the Central Plains. It was shed for the world.”

I calmly added one more thing.

“It was the same for someone’s son.”

*Whoosh!*

A fierce and mighty aura swept through the tent like a raging gale.

Yohi’s face, which had been watching our conversation in silence, instantly turned pale. The entire massive tent swayed like a leaf caught in a typhoon.

And at the center of it all stood one man, trembling with rage.

“You…!”

His eyes blazed with fire, and his voice seemed to boil.

I didn’t avoid Baeksang’s gaze.

In the face of the violent emotions pouring toward me, I merely remembered someone who had been hiding in a distant corner of my memory.

*This…*

I didn’t know.

I didn’t know whether this suspicion was true or whether it would end as nothing more than a guess.

But before that, I had to show the proper respect for the reverse scale I had touched.[^1]

I inclined my head slightly toward Baeksang, then left the tent.

All the way to my quarters, I thought of someone who was clearly different from Baeksang, yet resembled him in some way.

*……Head Elder.*

The Blade of Flowers, Jin Baekyang.

One of the heroes of the Great Faction War born in Shanxi Province, and a man who, despite being the second son, had nearly become the Family Head of the Jin Family of Taiyuan.

And a traitor who had lived for decades beneath the shadow of Dark Heaven.

I didn’t know why I had thought of him at that exact moment.

But perhaps, perhaps…

*Damn it. I don’t know.*

Just as I let out a deep sigh, I saw Hyuk Mujin roasting an entire wild boar in front of my temporarily assigned quarters in the Inner Palace.

I didn’t know where he had gotten it.

*Look at this thoughtful little punk.*

I often berated him when I was bored, but he was someone who had shared every kind of hardship with me since our days in the Jin Family of Taiyuan.

More importantly, as a former gate guard of the family, he was the person among the Fire Dragon Pavilion members accompanying me who knew the most about the Head Elder.

*He might be able to give me some decent advice.*

Just as I was about to wave at him happily, Hyuk Mujin spotted me approaching and abruptly raised one hand.

He was holding a reddish-hot iron skewer.

“Who goes there?”

“……”

Advice, my ass.

I took off the tiger mask and answered.

“Put your head to the ground.”

“Uh. Ha ha. I was joking.”

“Good. I wasn’t, so put your head to the ground.”

“……”

*Clank.*

The iron skewer slipped from Hyuk Mujin’s limp hand.

* * *

Two days passed in the blink of an eye.

The Beast Miao King, who had told us at our first meeting to wait because he would summon us soon, had yet to summon us. Instead, Yayul Mok’s visits became more frequent than expected.

*Thump.*

White Tiger tossed the wild boar he had been carrying in his mouth onto the ground, then proudly thrust out his chest.

I asked Yayul Mok, who was stroking White Tiger’s neck.

“Where did you catch it this time?”

“In the western grass.”

Yayul Mok answered without thinking, then hurriedly continued with a look of sudden realization.

“……No. I found it on the way here.”

“Why did you bring something you found here?”

“Hmm. I felt bad throwing it away?”

“But for something you found, the bite marks on its neck look exactly like a tiger’s.”

“My child is well trained, so he doesn’t bite just anything. Whether it’s a beast or a person.”

“……”

What kind of bullshit was this?

Was this one of those ideas that there were no bad tigers in the world?

I carefully examined White Tiger’s teeth, which were caked with blood and scraps of flesh, and muttered.

“He looks like he’d bite and chew up anything in one bite, whether it was a beast or a person. Are you saying he doesn’t discriminate when it comes to food?”

“Anyway, that isn’t true. It must have been another tiger.”

“If that’s the case, why are there only one set of bite marks?”

“I don’t know. I simply found it dead on the roadside and brought it here.”

“Oh, I see. A wild boar that had been living hale and healthy somehow died of natural causes on the roadside? Then White Tiger just went *chomp* and brought it here?”

“Exactly.”

“……”

When someone’s shamelessness went beyond all limits, I no longer had the energy to answer.

I stared at Yayul Mok with an incredulous look, then sighed as I gazed at the wild boar, which was large enough to form a mountain.

“By the way, another wild boar?”

“It’s a wild boar. Is there a problem?”

“Another wild boar?”

“……”

“Do Han Chinese people have no conscience? At least shut up and eat it, considering the effort I went through to catch and bring it here.”

“I thought you said you found it?”

“Ah. My mistake. I found it.”

This guy was something else, too.

I only learned later that the meat Hyuk Mujin had been roasting two days ago had been brought by Yayul Mok.

Of course, no one had seen him at the time, and Yayul Mok had stubbornly insisted that it wasn’t him.

“Even wild boar gets old after a day or two. I’ve been eating nothing but this for days, and I’m sick of it. Sick of it.”

“Then take it back.”

“Mujin. Take care of the meat.”

“Yes, sir.”

Yayul Mok and White Tiger looked at me with flat, thoroughly chilled eyes, but I had been wearing a thick skin for so long that my face didn’t even sting at this level.

Yayul Mok clicked his tongue softly as he watched Hyuk Mujin hurry about preparing the meat, then turned his gaze toward me.

“Is the work you’re doing going well?”

Instead of answering, I shook my head.

“So that means you haven’t achieved anything.”

“At least not yet.”

It wasn’t as though I had spent the past two days doing nothing. The Fire Dragon Pavilion members and I had been investigating both inside and outside the Nanman Beast Palace.

I had Ju Hwaran and Hyuk Mujin investigate what was happening in the Inner Palace, while I led the remaining members in scouting the surrounding area.

*We might find a trace of Dark Heaven.*

But as I had just said, despite our efforts, we had achieved no notable results.

The absence of any trace of Dark Heaven near the Nanman Beast Palace was a good thing. But if the traces weren’t absent and we simply hadn’t found them, then it was a different story.

“For now, I plan to keep going. At least until the tribal council.”

The tribal council where all the tribes of Nanman would gather in one place was tomorrow.

Yayul Mok nodded at my words, then opened his mouth in a voice lowered as far as it could go.

“It would be better to postpone it today.”

“Postpone it? Why?”

“The Inner Palace has summoned you.”

[^1]: In East Asian lore, a dragon’s “reverse scale” is a uniquely dangerous vulnerable spot; touching it is said to provoke the dragon’s rage.
## Chapter artifact 632

# Chapter 632

The Inner Palace.

Our current quarters were also part of the Inner Palace, but it didn’t take me long to realize that wasn’t what Yayul Mok meant.

“Great Hero Yayul is summoning us?”

“That’s right. More precisely, he ordered me to bring only you and that old man.”

That was good news. It meant the Beast Miao King, who had remained silent all this time, had finally agreed to my request for a private audience.

But why summon only Namho and me instead of the entire Fire Dragon Pavilion?

A thought flashed through my mind along with the question, and I suddenly opened my mouth.

“Do we need to avoid other people’s eyes?”

Yayul Mok stared at me with an expression of surprise, then gave a small nod.

“You’re quicker on the uptake than I expected. We should move without attracting attention if possible.”

“Because the tribal council is tomorrow?”

“No. Because most of the tribal chiefs hate all of you.”

“……”

“It’s a fact.”

*Was he a guillotine in his previous life? Look at him chopping off even the words that were about to come next.*

Still, it was an undeniable fact, so I clicked my tongue bitterly.

“I more or less understand the situation. Great Hero Yayul is under pressure from all sides too, isn’t he?”

Yayul Mok’s lips parted as though he was about to say something, but he soon closed his mouth with a hardened expression.

Just as I couldn’t deny what I had heard earlier, neither could he.

But there were some things one had to acknowledge.

Nanman was not the barbaric land the people of the Central Plains imagined it to be, and the Beast Miao King was not their king, but merely one of the great chieftains representing them.

*There’s no way this guy doesn’t know something I already do.*

Yayul Mok was a decent enough young man in his own way, but he was still a youth who hadn’t completely shed his immaturity.

And then, with his lips tightly pressed together in a wounded expression of pride, Yayul Mok muttered,

“You’re right. No matter how capable my father is, it’s impossible for him to handle all of them alone.”

“……?”

“What’s with that look?”

“Nothing. I’m just surprised. I didn’t expect you to admit it so honestly. You’ve matured a little in the meantime, huh?”

*Had he realized something after our conversation two days ago?*

Come to think of it, even though he still snapped at me like a middle-schooler going through puberty, Yayul Mok had become much friendlier than he was at first. He even brought us wild boar himself on a regular basis.

*That’s a good thing. The problem is that in this enormous land, our side is no bigger than a grain of millet.*

I opened my mouth a moment before Yayul Mok could glare at me.

“When and where?”

“Insi. I’ll come to get you then.”

“Good. Oh, and while you’re coming…”

“While I’m coming? What?”

“Bring us some venison or roe deer. Anything but wild boar.”

“……!”

* * *

A day in the Murim was divided into twelve shichen, and each shichen meant two hours. Insi referred to the period from three to five in the morning.

And Yayul Mok kept his promise.

In the dead of night, while everyone was deep asleep, a White Tiger covered from head to toe in pure white fur tore through the darkness and landed in front of our quarters.

*Thump.*

A familiar-looking beast lay dead beside him.

“Fuck, it’s another wild boar. Are you doing this on purpose?”

“I found it on the way here.”

“You keep finding them. What, do you have a wild-boar farm somewhere? Do you water them, let them grow nice and big, then sneak over and steal them?”

Namho asked with a bewildered expression.

“What is *seori*? I’ve never heard that word before.”

“It’s a thing. And for you, Old Man Namho, this will be the first and last time you ever hear it in this lifetime.”

“So that’s how you Han Chinese talk…”

“Please stop hating the Han Chinese.”

After politely requesting that Namho stop grumbling in displeasure, I received a gesture from Yayul Mok toward the space behind him.

“Get on.”

“On this tiger?”

“……Do I need to carry you on my shoulders, then?”

“He looks like he has a nasty temper.”

“That’s prejudice. I’ve been with him since he was a cub, so he’s as gentle as can be. If you don’t believe me, test him.”

“Oh. Really?”

I reached out to stroke the White Tiger’s chin, then yanked my hand back like lightning.

*Clack!*

Its large, sharp teeth snapped shut through empty air.

At the demanding look in my eyes, Yayul Mok clicked his tongue softly.

“What a shame.”

“You bastard.”

“I told you to test him if you didn’t believe me. I never said he wouldn’t bite.”

After spouting nonsense that even a dog wouldn’t believe, Yayul Mok gently scratched the White Tiger between the eyes.

“Yaho. Yaho, my boy. Don’t be angry.”

At first, I thought he was cosplaying a North Korean mountain hiker. But then, a thought suddenly occurred to me.

“Don’t tell me that’s his name.”

Yayul Mok proudly nodded.

“Muyaho (武野虎).[^1] It means ‘tiger of the mighty wilds.’”

[^1]: “Muyaho” echoes a Korean meme catchphrase and also resembles *yaho*, a shout traditionally made in the mountains.

“……”

“It’s a truly magnificent name, isn’t it?”

*Grrrrr. Prrrrr.*

The White Tiger purred as though it, too, was proud to be part of the feline family. Yayul Mok looked ready to die of cuteness and continued proudly.

“That means he’s in a very good mood. You may get on now.”

“……Ah. Yeah.”

“Why do you look like that? Is something wrong?”

*There is. A small problem that only I know about. But I can’t say anything here.*

I swallowed the words that had risen to my throat, silently climbed onto the White Tiger’s back, and Namho followed with a slightly flushed face.

“To think I’d ride a tiger at my age, an animal supposedly reserved for warriors. And a sacred White Tiger at that!”

Nothing in this world makes you happier than hearing someone praise your child. Yaho-mom Yayul Mok nodded proudly.

“You know what you’re talking about, old man. Do you like White Tigers?”

“Of course. I’ve always been very fond of them.”[^2]

[^2]: In Korean slang, “White Tiger” can also refer to a woman with little or no pubic hair, giving Namho’s answer an unintended sexual double meaning.

“……”

*No. Stop. Don’t take it any further. That would be a terrible move.*

Just as I waited for the next line with equal parts anticipation and dread, the White Tiger stretched leisurely, seemingly unaffected by carrying three people, then kicked off the ground and raced away.

*Papat!*

Beneath the bright moonlight, the three people riding one tiger crossed the dark jungle like a streak of light.

They stopped in front of an old shrine that was slowly collapsing.

* * *

The air inside the shrine was as hot and humid as a steam sauna.

Dust covered the floor, insects had eaten through the pillars, and an oil lamp swayed as though it might go out at any moment, casting a faint light over the interior.

And at the center of it all stood one person waiting for us.

“When I came back after all this time, the place was a complete mess. Then again, it wasn’t in particularly good shape back then either.”

Unlike when I had first met him, the expression on the Beast Miao King Yayul Cheok’s face as he turned around with a low mutter was as indistinct as the oil lamp’s light. In it, I could see unmistakable fatigue.

Perhaps for that reason, no one, myself included, asked why he had chosen to meet us in this old shrine instead of the Inner Palace’s main hall.

Instead, I chose to respond to his disjointed words.

“When are you talking about?”

“When I was young. No, I was even younger than that. Whenever we caused some huge disaster we couldn’t possibly clean up, we would hide here to avoid the adults.”

“When you say ‘we’…”

“You’ve already met him. Though I’m sure you’ve already guessed.”

“Baeksang. The great chieftain of the Bai people.”

The Beast Miao King nodded.

“That’s right. Exactly him.”

“I know the two of you have been together for a long time.”

“Even ‘a long time’ isn’t enough to describe it. We spent our entire lives together. In the grasslands, the swamps, the mountains and fields, and even on the battlefield—we were always together.”

As though remembering those days, the Beast Miao King silently stared at the swaying oil lamp for a moment, then gave a small nod.

“Yes. That’s right.”

“I heard the two of you were inseparable childhood friends and sworn brothers.”

At my sudden words, the Beast Miao King’s gaze shifted to me. I met his eyes directly and continued.

“But are you still like that now?”

“Hmm.”

“……Jin Taekyung. Watch your mouth.”

“Grrrr.”

The White Tiger, which had been crouching nearby, let out a low growl.

The Beast Miao King made a small waving gesture toward his son, who had stepped forward with a quiet warning, then stared at me.

“Do you think we aren’t?”

“I just had a thought. I thought Great Chieftain Baeksang might have a different opinion from you, Palace Lord.”

“……”

“I don’t know how much detail you’ve heard, but all sorts of things are happening in the Central Plains right now. And the first of them began in Shanxi Province, where my Jin Family of Taiyuan is located.”

I still remembered it vividly.

The Shaolin Bloodshed and the Sichuan Blood Tragedy had overshadowed it, but the first time the name Dark Heaven appeared in the Central Plains was in Shanxi Province.

They manipulated the Mount Heng Sword Sect and its Head Elder into starting a war, and no fewer than a thousand people had to lose their lives.

*If he received information from the Hidden Shadow Pavilion, there’s no way he wouldn’t know.*

As though he had read my thoughts, the Beast Miao King nodded.

“I’ve already heard about it. I had even met Blade of Flowers Jin Baekyang before.”

“No one could have predicted it. If he had been an outsider with no ties to the family, perhaps. But the Head Elder was blood kin and the senior elder of the Jin Family of Taiyuan.”

That was why Jin Wikyung had continued to trust the Head Elder to the end even while remaining wary of him, and the Beast Miao King was not dull enough to miss the meaning behind my words.

“Baeksang… No. It can’t be. He’s different from the Blade of Flowers.”

“No one can know that.”

After my firm answer, Namho, who had been silently watching the situation, suddenly spoke.

“I once had a subordinate I cherished like blood kin. He was the sole descendant of a fallen martial family, and his parents had been killed by the Demonic Cult. Later, when the hundred-thousand-strong Demonic Path rose like wildfire in the west, he joined the Murim Alliance. He never feared death when carrying out missions, and the information he brought us led to more than ten minor victories.”

It was the story of a Hidden Shadow Pavilion agent unknown to the world—someone whose existence even I had never heard about.

But just like Namho’s dark expression, the words that followed were no brighter.

“Even after it happened, I couldn’t believe it. I couldn’t believe he was a traitor. One day, the information he brought back at the cost of one arm drove more than five thousand Alliance members to their deaths.”

“……!”

“When everything was revealed, he fled. And several days later, I saw the head of a man brought back by the assassination squad. He was grinning from ear to ear, as though something had made him terribly happy.”

Silence settled over the place where his voice had faded. Namho let out a deep sigh, then spoke again.

“I am not saying that the great chieftain of the Bai people is a minion of Dark Heaven. But this is the Murim, a place where you cannot see even an inch ahead. Baeksang, Yohi, Heugung—or even one of the thirty-two tribal chiefs gathering here tomorrow—none of it would surprise me if one of them turned out to be a traitor.”

The Beast Miao King did not answer.

For a very long time.

He merely stared at the oil lamp as it swayed and righted itself again and again, then suddenly turned his head toward me.

“Are you certain?”

I answered.

“At least one thing.”

“What is that?”

“The Southern Heaven Demon Empress. That fucking bitch won’t leave Nanman alone.”

The Beast Miao King let out a low groan before opening his mouth.

“Nanman is not an easy target.”

“Then were the Sichuan Tang Clan, Shaolin Temple, Emei Sect, and Qingcheng Sect attacked because they were easy fucking pushovers?”

“……!”

“Oh, sorry. I went too far.”

The Beast Miao King let out a hollow laugh at my sudden outburst before answering.

“You really are Old Master Jeok’s Disciple.”

“He’d be offended if he heard that.”

“He’d secretly love it.”

“……Oh.”

*Okay, he really knows Old Man Jeok.*

Just as I was silently giving the Beast Miao King a thumbs-up, a rough disturbance came from outside the shrine.

*Whoosh, hiss!*

Then a voice, held as low as possible, reached us.

“P-Palace Lord!”

At the same time, a red warning light flashed in my mind.

Along with a System alert.

> **System**
>
> *Ding.*
## Chapter artifact 633

# Chapter 633

The voice from outside was hushed as much as possible, but neither its urgency nor the presence behind it could be concealed.

“P-Palace Lord!”

At the call, presumably from one of his guards, the Beast Miao King and Yayul Mok sharply raised their heads.

“Something has happened at Ailao Mountain…!”

*Boom!*

A powerful wave of qi suddenly shot out and swept through the shrine.

The Beast Miao King shattered the decrepit door and shouted at one of his men with wide, blazing eyes.

“Something happened at Ailao Mountain? What do you mean?”

And at that very moment, a low ringing tone pierced my ears before the voice could reach me.

*Ding.*

> **System**
>
> - A sudden quest, **Unknown Omen**, has been generated!
>
> **Quest**
>
> **Unknown Omen**
>
> Nanman’s forbidden land, Ailao Mountain, is screaming.
>
> Across its countless high and treacherous peaks, bodies torn to pieces hang in the open air. Blood from something unknown flows along the thousand-foot cliffs between them. The endless howls rising from that place, shrouded in black clouds and mist, have filled everyone with fear.
>
> And now, a new path has appeared before you.
>
> **Grade:** Sudden Quest
>
> **Restriction:** Jin Taekyung
>
> **Mission:** Investigate Ailao Mountain within the time limit (Incomplete)
>
> **Reward:** ???
>
> **Failure:** ???
>
> - Would you like to accept the quest?

*An unknown omen, huh?*

I muttered inwardly, then suddenly thought the quest title needed to be changed.

Not *Unknown Omen*, but *Fucking Obvious Omen*.

Of course, putting that aside, I already knew what answer I had to give in this situation.

*Accept quest.*

*Ding.*

> **System**
>
> - You have accepted the sudden quest, **Unknown Omen**!
>
> - A time limit has been created!
>
> **Time Remaining:** 4 hours 59 minutes 59 seconds

Time, which had been frozen, began to flow again. Before even a moment had passed, we set out for Ailao Mountain, racing through the predawn darkness.

* * *

They said that the warriors of the Nanman Beast Palace grew up alongside fierce beasts.

They grew up together from childhood, forming bonds along the way. After completing their coming-of-age ceremony and being recognized as full-fledged warriors, they officially became the beasts’ owners and companions.

However, even this venerable tradition, with its history of several hundred years, had exceptions, as everything did.

*Whoosh! Rustle!*

The Beast Miao King Yayul Cheok was someone who had no need for the help of a beast.

He had probably been that way since childhood, and he was the same even now.

He was the greatest warrior Nanman had ever produced—and a beast himself.

Leading the way through a jungle filled with darkness and tangled grass, the Beast Miao King let out a mighty roar.

*Gwaaaar!*

It was quite literally the roar of a beast. Rougher, more savage, and far more primal than the lion’s roar, the supreme technique of Shaolin Temple imbued with the power to subdue demons.

The Beast Miao King’s roar tore through the deep darkness and spread farther and faster, announcing a warning.

Looking down at the hundreds of torches rising in various places beneath a distant mountain ridge, the Beast Miao King shouted at the guards running around him.

“Gisan. Dogok. Go to the Outer Palace. Find the tribal chiefs staying there, reassure the people, and mobilize the warriors to prepare for a possible foreign invasion!”

“Yes, sir!”

“Wonhu. Manjeok. You’re going to the Inner Palace. Mobilize the Miao warriors and protect the inside of the palace!”

“At your command!”

“The remaining three of you, find the other great chieftains and inform them of the situation. Tell each of them to mobilize one hundred elite warriors and head for Ailao Mountain!”

The Beast Miao King gave a series of precise orders to the Seven Miao Tigers, his personal guard made up of the finest warriors among the Miao people.

Then his gaze slid toward his late-born son, who was running hard behind him.

“Mok.”

“……Yes, Father.”

Yayul Mok’s grim expression had nothing to do with the darkness settling around us.

As though he had already anticipated what his father was about to say, he answered in a dull voice. The Beast Miao King continued in a firm tone.

“Go with them. Gather the warriors under the Miao people and raise a force in case something happens.”

“But…”

“Have you forgotten? You’re the Young Chieftain of the Miao people and the Young Palace Lord of the Nanman Beast Palace.”

This was when I realized once again why the Beast Miao King was the lord of the Nanman Beast Palace.

When I had first met him, he had seemed relaxed, like a well-fed male lion. But now, he was a beast with its prey right in front of it.

And Yayul Mok wasn’t immature enough to disobey his father’s unyielding orders in a situation like this.

“……I obey, Palace Lord.”

But contrary to his answer, Yayul Mok did not immediately leave the formation.

Instead, he moved right beside me as I ran alongside the Beast Miao King and made an unexpected proposal.

“Take this one with you.”

“Huh?”

*Grrr?*

The one Yayul Mok was talking about was none other than White Tiger, which made the offer all the more surprising.

The warriors of Nanman considered the beasts who fought alongside them their most precious comrades—and their family.

*Whoosh!*

I dodged a branch that shot right into my face and asked carefully.

“Are you giving him away? Like, to a new family?”

“What nonsense!”

*Grrrr!*

“Whoa. Why are you getting so angry? If it’s not, just say no.”

“No! If you conserve even a little of your strength, you can be of greater help to Father!”

*Gwaaaar!*

It wasn’t for nothing that they said hearts could communicate without words. Man and beast were both being fucking ridiculous as a pair.

*Anyway…*

*It would definitely be much better to ride him.*

The amount of internal energy I possessed was a level that could not easily be found even in the Central Plains. But it wasn’t as though it sprang up endlessly from some bottomless reservoir.

If I ended up facing Dark Heaven under the command of the Southern Heaven Demon Empress at Ailao Mountain, then, as Yayul Mok had said, it would be best to conserve as much strength as possible.

*What a good kid.*

I hadn’t been in Nanman for very long, but I understood what it meant for someone here to lend me their beast.

I looked at Yayul Mok with an approving gaze and decided to give him a present in return.

“Here. Don’t refuse just because you feel burdened. If something comes in, something should go out.”

*Rustle!*

Silence flowed between the passing wind and swaying branches.

Namho, who was being held in both my arms like a piece of luggage, spoke with a grim expression.

“Am I an object?”

“If you were an object, we could throw you and use you to attack. Old Man Namho can’t even do that.”

“Have you ever seen such a lawless thug with no respect for his elders? How dare you attack an old man…”

“Quit complaining and go. Your retirement plans are looking bright, so don’t get dragged into this for no reason. And our kids can’t just sit around doing nothing either.”

This wasn’t me ignoring him. It was consideration.

No matter how much hardship Namho, an agent of the Hidden Shadow Pavilion, had endured, he was still an old man who had never learned even a single move of martial arts.

And Namho knew that better than anyone else. He let out a deep sigh, his face filled with worry.

“I’ll make sure to tell the Fire Dragon Pavilion. That the Pavilion Master is looking for you.”

“That should be enough. I trust you’ll tell them what they need to be wary of, too.”

At last, the fuse attached to the Nanman powder keg had been lit.

The important question was whether the one who had lit it was an outside enemy or an enemy within.

Unlike his aging body, Namho’s mind had not grown old in the slightest. He gave a small nod.

“Pavilion Master, there’s one last thing I want to say.”

“Yes?”

“Don’t get hurt.”

“Ah.”

“Of course, you absolutely mustn’t die, either.”

I answered his concern with a faint smile instead of words.

Yayul Mok took Namho from me, then, with a glance, kicked off White Tiger’s back and sprang away.

*Tap. Whoosh!*

A shadow swept beneath the hazy moonlight.

As Yayul Mok and the Seven Miao Tigers disappeared into the darkness, the Beast Miao King, who had been charging on all fours like a gigantic brown bear, increased his speed.

*Crack-crack-crack! Smash!*

Thick branches snapped, and dense grass was trampled beneath us.

I climbed onto White Tiger’s back, which Yayul Mok had left behind, and heard the Beast Miao King’s voice through the wind rushing violently past my ears.

“Do you think this was Dark Heaven’s doing?”

“We’ll have to get there to know for sure, but the possibility is high. At the very least, it’ll be connected somehow.”

I spoke again to the Beast Miao King, whose face had hardened.

“But what exactly is Ailao Mountain?”

“It is a forbidden land. No one may enter unless they have permission.”

I already knew that Ailao Mountain was a forbidden land. Namho had told me on the way here, and the System had confirmed it moments ago.

That was why the Beast Miao King’s answer didn’t feel particularly clear.

“But isn’t the Nanman Beast Palace the same? No, now that I think about it, most of Nanman seems to be like that.”

“It’s different. Completely different. The most outstanding warriors from each tribe enter that place and stand guard.”

“Why on earth…?”

“It happened more than three hundred years ago. Back when my ancestor’s ancestor—and his ancestor before him—were living in Nanman. At that time, more than a hundred tribes had been waging wars of life and death across this land for generations. Dozens of tribes vanished in the process, and the descendants who barely survived established a sect of their own in the deepest reaches of Nanman. Then they began handling something more dangerous than any sharp weapon or beast.”

At that moment, a conversation I had shared with Jeok Cheongang in Henan several months ago flashed through my mind.

It had been about the history of the Nanman Beast Palace, which was connected to the deeds of the former Sect Leaders of the Fire Gate Clan.

That history was also one of the reasons the Nanman Beast Palace had taken part in the Great Faction War.

*If that’s the case…*

There was only one answer.

I muttered softly.

“Poison. It was poison.”

“That’s right. That was the beginning of the Five Poisons Sect, which terrorized Nanman for the next hundred years.”

We crossed towering peaks, leaped over hills, and raced through the dense forest, stepping on the tops of trees.

The Beast Miao King curled his hands like claws, struck a thick tree, and sent it flying before continuing.

“They say an enormous number of people died. The riverbanks were littered with dead fish, and the beasts that unwittingly ate the fish washed downstream died as well. Poison spread through the wells, and an unknown epidemic broke out. When thousands upon tens of thousands had died, the tribes that had once been divided finally gathered beneath a single banner and began a new war.”

That was the birth of the Nanman Beast Palace.

But death bred death, and revenge returned as revenge.

And just as the Nanman Beast Palace and the Five Poisons Sect were waging a fierce war, trapped in an endlessly turning cycle of vengeance, an outsider arrived from the distant Central Plains.

“He claimed to be the Sect Leader of the Fire Gate Clan. It was an unfamiliar name, one my ancestors had probably never heard in their lives, but that likely didn’t matter to them. The moment he entered Nanman, he burned to death the one hundred warriors of the Five Poisons Sect who had ambushed him.”

The Fire Gate Clan’s Sect Leader of that era had not appreciated the Five Poisons Sect’s unexpectedly grand welcome.

Like most martial artists, he also hated poison.

He planted his ass on the scales of power and crushed the balance between them, then led the Nanman Beast Palace and reduced the Five Poisons Sect to ashes.

“The problem came after he left.”

The disciples of the Five Poisons Sect had turned to white bones, but the venomous beasts and fierce beasts they released in their final moments continued multiplying deep in the mountains where the sect had once made its headquarters.

Slowly.

Secretly.

And that former headquarters of the Five Poisons Sect was none other than…

“That place right there. Ailao Mountain.”

I followed the Beast Miao King’s fingertip and raised my head.

Far in the distance, a black mountain filled with peaks shrouded in clouds and mist came into view.
## Chapter artifact 634

# Chapter 634

*Papat!*

Neither the Beast Miao King nor White Tiger slowed their pace. I narrowed my eyes against the chilly wind brushing past my entire body.

*That must be Ailao Mountain.*

Its rugged terrain and deep valleys were unmistakable even from a distance. Countless peaks shrouded in mist rose so high they seemed to pierce the heavens.

Perhaps it was because the predawn darkness had not yet lifted. Or perhaps it was because this had once been the old headquarters of the Five Poisons Sect, which had plunged Nanman into terror long ago.

Whatever the reason, Ailao Mountain’s rapidly approaching landscape felt dark and ominous.

That was probably why the Beast Miao King’s voice, which reached me soon after, had sunk so low.

“The Five Poisons Sect was destroyed by the Palace, but that did not mean everything disappeared.”

If objects remained where people had vanished, you could simply burn them away. But things were different if those objects had legs.

“No one knew at the time that the unknown things left behind by the Five Poisons Sect were still living in the deepest reaches of Ailao Mountain.”

For more than a hundred years.

The Five Poisons Sect’s dark legacy had seeped deep into Ailao Mountain and continued to live there. In a territory of their own that no one could invade, they devoured one another while breeding and slowly growing in number.

“But eventually, our ancestors found out. In a way no one had wanted.”

Three hundred elite warriors of Nanman melted into a handful of bloody water, and two great chieftains and around a dozen tribal chiefs were torn limb from limb.

That was what happened during the tribal council held at Ailao Mountain in the exact year that marked one hundred years since the Nanman Beast Palace had destroyed the Five Poisons Sect.

“According to the records, what attacked the Palace were venomous beasts and strange ferocious beasts rarely seen in Nanman—or even anywhere in the world.”

Deadly poison for which no antidote was known, along with hundreds of beasts possessing claws and teeth harder than steel.

The Nanman Beast Palace suffered enormous losses in the unexpected attack and was horrified. They trembled when they discovered the shadow of the Five Poisons Sect, which they had believed had disappeared long ago.

“Once again, all of Nanman gathered its strength. We mobilized every warrior from every tribe, surrounded Ailao Mountain, and tried to kill them all.”

But the Nanman Beast Palace’s attempt ended in only half a success.

They killed hundreds of beasts and burned the venomous creatures, but the losses they suffered were simply too great. And in the process, invisible cracks began to appear.

*When you think about it, it couldn’t have gone any other way.*

Even if you ordered a single pizza and shared it, someone would inevitably eat one extra topping while someone else got less.

The Nanman Beast Palace’s campaign to subdue Ailao Mountain had followed a similar pattern.

The venomous beasts and ferocious beasts, sensing danger, appeared and attacked from all directions as though possessed by Hong Gil-dong.[^1] The tribal chiefs leading the warriors feared the losses their own people would suffer.

[^1]: Hong Gil-dong is a legendary Korean outlaw hero proverbially said to appear here, there, and everywhere.

To put it bluntly, they couldn’t exactly say, “Since things have come to this, let’s have only a few people die from each tribe and split the bill evenly.”

“The tribes grew more divided with each passing day. As a last resort, we chose to use fire, but the flames spread outward and caused even more damage. They still weren’t enough to burn down all of Ailao Mountain.”

And so, the Nanman Beast Palace had to withdraw from Ailao Mountain. Of course, that did not mean they left with nothing to show for it.

“The Palace had suffered immense losses, but the threat had been reduced by just as much. We had hunted countless venomous beasts and ferocious beasts and burned at least part of Ailao Mountain. In that sense, perhaps the result was inevitable.”

“What happened after that?”

“Ailao Mountain grew quiet, as though nothing had ever happened, but no one let down their guard this time. We designated the entire mountain as a forbidden zone, permanently stationed three hundred elite warriors drawn from the various tribes there, and had the four great chieftains take turns leading small-scale exterminations every year. We maintained peace that way for more than a hundred years.”

It was a reasonably wise compromise for the tribal chiefs belonging to the Nanman Beast Palace—one that allowed them to guard against the threat of Ailao Mountain without suffering enormous losses.

But the problem was…

“I guess that peace is coming to an end today.”

I spoke in a heavily subdued voice and pointed ahead.

Ahead lay a dark, rugged valley like the entrance to Hell, with a lone figure sitting against a tree.

*Whoosh!*

The Beast Miao King’s body shot upward like a beam of light, crossed the air, and landed at the mouth of the valley.

When I arrived close behind him and climbed down from White Tiger’s back, the Beast Miao King stood tall before the figure. His face was stiff as stone.

“…We’re too late. He’s already dead.”

I quietly nodded. Even if I hadn’t heard him say it, I probably would have known. Before we had even come within a few steps, an indescribable stench had stabbed into my nose.

And there was only one cause of death capable of producing a smell this horrible.

*Poison. It’s poison.*

And an incredibly potent one at that. The figure leaning against the tree—no, the corpse—had released a stench and bloody runoff so strong that the ground and grass soaked in it had turned black and died.

Unless a martial artist had cultivated Scorching Yang Qi, which was rooted in fire qi and naturally opposed poison, even a master in the early stage of Peak would probably have difficulty resisting the poisonous qi within three zhang.

*Grrr.*

I soothed White Tiger, who was frowning fiercely, then opened my mouth.

“Do you recognize him?”

“Somehow, he looks familiar. He must be one of the warriors stationed at Ailao Mountain.”

“Do you normally post guards at the entrance?”

“Of course not. When preparing for an emergency at Ailao Mountain, we need every warrior we can get. The mountain covers such a vast area that there are three or four villages nearby, but even they know the situation well.”

In other words, the area had been strictly controlled for a long time, so there was no need for another sentry.

And if that was the case…

*He came down from the mountain. He was running away from something.*

I raised my head and surveyed the surroundings.

Beyond the thick darkness, faint but unmistakable footprints remained. They were clearly human footprints at a glance. There was no trace of a beast or any venomous creature.

And one more thing.

“There’s a wound. Look at the corpse’s side.”

Just as the Beast Miao King had said, the clothing along the corpse’s side had been torn as though something had clawed it, and the skin beneath had been stained completely black.

“It wasn’t a weapon, at least. It looks as though he was simply grazed by something rough and powerful, but…”

“That is why poison is frightening. Even a slight wound can bring death in an instant.”

It was only a shallow scratch, and yet this had happened.

*Could it be something like the Formless Ultimate Poison Jeok Cheongang once suffered from?*

I took my eyes off the corpse and stared into the valley drowned in darkness. I had not witnessed it myself, but a scene seemed to flash through my mind.

Until just moments ago, the unknown dead man had probably been running through this rugged valley. Poisoned, stumbling and staggering, he had fled in a panic before meeting his death beneath that tree.

It was tragic, but the identity of whatever had killed him was more important to me right now.

*Was it Dark Heaven, or one of Ailao Mountain’s venomous beasts? Or else…*

One of Ailao Mountain’s venomous beasts being controlled by Dark Heaven.

With the question still unanswered, I looked at the Beast Miao King.

“In the end, it seems there’s only one answer.”

“That’s right.”

The Beast Miao King continued in a growling voice like an enraged beast.

“We’ll have to see with our own eyes exactly which bastard did this.”

*Ding.*

> **System**
>
> **Investigate Ailao Mountain Within the Time Limit (Incomplete)**
>
> **Time Remaining:** 01:24:32

* * *

Even though it should have been the dim hour of dawn by now, Ailao Mountain remained shrouded in thick darkness.

No. Darkness was not the only thing that existed here.

*The scent of blood.*

The smell of blood, which had become familiar at some point, was an invisible guide. Following the footprints left behind by the dead man, the Beast Miao King and I raced through the mountain before turning without hesitation toward the scent of blood carried on the damp wind.

And at last, we found it.

Countless corpses collapsed across the mountain ridges, along with the distinctive stench of deadly poison that even overwhelmed the heavy scent of blood.

“……!”

“……!”

How many were there? A hundred? Or more?

The ominous prediction I had made when we first encountered the corpse in the valley had become reality.

At the horrific sight spread before him, flames rose in the Beast Miao King’s eyes.

“Which bastard dared…? I’ll tear him limb from limb!”

It was a natural reaction from the ruler of the Nanman Beast Palace. But instead of joining him in his anger, I calmly drew up my internal energy, formed a qi curtain to block any sounds that might escape, and examined the corpses.

*Fractures. Blunt-force trauma. Dismemberment. Poisoning.*

Unlike the first corpse, the deaths here had varied causes besides poisoning. Some had died with their limbs crushed, while many others had parts of their bodies—their necks and elsewhere—torn away by some unknown, overwhelming force.

*If they were elite enough to be stationed at Ailao Mountain, they must have possessed considerable skill.*

And yet they had been slaughtered this horribly.

From what I had learned so far, only a very small number of Nanman’s warriors—including the Beast Miao King and Baeksang—were exceptional. Most of Nanman’s warriors were inferior to those of the Central Plains.

But even taking that into account, elite warriors would have been First Rate at minimum, reaching Transcendent or, in rare cases, Peak masters.

*Besides, Nanman’s warriors don’t fight alone. If you consider the ferocious beasts fighting alongside them, their combined strength should rival that of the major sects of the Central Plains…*

I was continuing that thought when I suddenly stopped at the strange feeling creeping over me. The moment I saw White Tiger keeping watch over the surroundings with a low growl, I realized what had caused it.

*The beasts. Where did the beasts go?*

The beasts that were always attached to their warriors as though they were one body were nowhere to be seen.

I hurriedly looked around, but it was the same everywhere. Among the more than a hundred corpses visible at a glance, there were only three or four beast carcasses.

“Why on earth?”

The instant I voiced the question that had taken root in my mind—

*Hsssss.*

“……!”

A chilling energy came riding the wind, piercing into me like an awl.

I had been confused, while the Beast Miao King had been barely suppressing his boiling rage. But both of us turned our heads like lightning.

At the same time, we saw it. We heard it.

*Rustle.*

Far away, grass trembled faintly. Darkness undulated as though it were alive. And then—

*Grrr.*

A low growl, deep as an abyss, came from some creature crouched among the grass where darkness had settled.

*Step.*

In a world that seemed to have slowed, the darkness moved, trampling the grass.

Wrapped in darkness from head to toe, it came toward us. It was larger than any beast I had ever seen, and its blue-white eyes held unmistakable anger and dignity.

*Black Tiger.*

The word flashed through my mind like lightning. At that exact moment, White Tiger’s body began to tremble.

*Gwaaaaaaaaaang!*

As a roar tore through the darkness and made heaven and earth tremble, a familiar ringing tone pierced my ears.

*Ding.*

> **System**
>
> - **Ailao Mountain’s Wraith** has appeared!

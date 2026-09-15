# Checkpoint Review — 135–139

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

# Chapters 135–139

## Plot

At Honghwa Inn, Jin Taekyung finishes humiliating Woo Jintae and beats the remaining four heirs of the Five Gates of Shanxi with sword-case blows. The inn’s guests recognize Taekyung as the Sleeping Dragon of Shanxi and side with the Jin Family of Taiyuan. Cheongpung, curious about violence, asks to strike the final heir himself. The injured heirs later discuss the collapse of the Mount Heng Sword Sect, the Jin Family’s growing influence, and their need to attend the City Lord’s luncheon. They also resolve to investigate Cheongpung.

Taekyung, Hyuk Mujin, and Cheongpung move to Honghwa Inn’s private annex and discover its hot springs. Cheongpung, who has never experienced one, decides to stay. Mujin’s warnings about hidden Murim grudges are based largely on wuxia novels, prompting Taekyung to punch him.

Prince Shangshan’s royal command summons the young prodigies to a noon luncheon. Because Mujin’s face is bruised and Woo Jintae remains unconscious, Taekyung substitutes Cheongpung as the delegation’s most impressive member. They travel in a six-horse carriage; Cheongpung’s complete lack of worldly and royal etiquette nearly causes repeated crises, including detaching a golden dragon ornament and calling the resident prince a king.

At the Shanxi Provincial Office, Assistant Military Commissioner Li Feng confronts Eunuch Hong, who has invited the Three Hands of Zhongnan to entertain the prince. Gong Ilhyuk taunts Li Feng over a defeat at Huashan ten years earlier. When Taekyung’s group arrives, the tense gathering includes Li Feng, Hong Jin, and three young martial artists from the Zhongnan Sect. Taekyung identifies himself as Jin Taekyung of the Jin Family, easing the hostility, then recognizes Zhongnan from a novel he once read before stopping himself from revealing too much.

## Continuity

- Woo Jintae is unconscious and severely swollen after Taekyung’s beating; the other four Five Gates heirs are injured but attend the luncheon.
- Jang Childeuk is present at Honghwa Inn as a Level 15 supporter of the Jin Family.
- Cheongpung is an undetectable-Level Peak master, was raised in the mountains, lacks worldly etiquette, and has now become interested in hot springs and firsthand martial experiences.
- The City Lord is Prince Shangshan, a ten-year-old member of the imperial family. His luncheon is held at the Shanxi Provincial Office, a heavily fortified palace-like complex with highly trained soldiers and long-term wartime stores.
- Hyuk Mujin remains at Honghwa Inn because Taekyung bruised his face; Taekyung continues to conceal the real reason for Woo Jintae’s absence.
- The unnamed martial official is Li Feng, Shanxi’s Level 68 Assistant Military Commissioner, a former Huashan lay disciple who left roughly ten years ago and has nearly mastered the Seven Plum Sword.
- Eunuch Hong is Shanxi’s powerful Deputy Military Commissioner and Li Feng’s political rival.
- Gong Ilhyuk is the third of the Three Hands of Zhongnan; Huashan and the Zhongnan Sect have been rivals in Shaanxi for about a century.
- Hong Jin is Level 22, delicate in appearance and voice, and welcomes Taekyung at the luncheon.
- The three Zhongnan martial artists’ names and individual identities remain unresolved. The earlier dispute involving Li Feng, Huashan, and an insult also remains unresolved.
- Taekyung nearly exposed that he knows Zhongnan from a novel, raising an unresolved question about what he intended to say and whether anyone noticed.

## Translation Decisions

- Render 칠매검 as **Seven Plum Sword**, 상산왕 as **Prince Shangshan**, 도지휘첨사 as **Assistant Military Commissioner**, 도지휘동지 as **Deputy Military Commissioner**, and 종남삼수 as **Three Hands of Zhongnan**.
- Render 육두마차 as **six-horse carriage**, 속가제자 as **lay disciple**, and 초일류 as **advanced First Rate**.
- Use **His Highness** for the formal royal address 전하; retain **king** when Cheongpung uses 왕 literally.
- Render 군문 as **military** when describing an affiliation.
- Render Cheongpung’s first-experience villain phrasing and his etiquette mistakes in a comic but politically dangerous tone.

## Durable state

{
  "active_continuity": [
    "The Jin Family procession reaches the Shanxi Provincial Office for the City Lord's luncheon.",
    "The Shanxi Provincial Office is a palace-like fortified complex that can accommodate several thousand people and holds enough grain to endure ten years of wartime defense.",
    "The soldiers stationed at the Shanxi Provincial Office are highly trained: most guards are around Level 20, commanders exceed First Rate, and units practice synchronized spear formations.",
    "Cheongpung does not understand the etiquette surrounding royalty and must be told to address the resident prince as His Highness rather than king.",
    "The official escorting the young prodigies is deeply afraid that Cheongpung will make an inappropriate remark and repeatedly asks Taekyung to keep him quiet.",
    "A tense discussion is already underway at the luncheon before Taekyung's group enters; fragments mention the Assistant Military Commissioner, Huashan, and an insult.",
    "Hong Jin is a Level 22 man with a delicate appearance and voice who interrupts the tense exchange and flatters Taekyung while greeting him.",
    "Li Feng is a Level 68 man in black martial robes whose appearance and bearing suggest affiliation with the military.",
    "Three additional young martial artists at the luncheon identify themselves as members of the Zhongnan Sect of Shaanxi and treat Taekyung as a junior.",
    "Taekyung identifies himself as Jin Taekyung of the Jin Family of Taiyuan, causing the hostile atmosphere around the other four men to ease somewhat.",
    "Taekyung recognizes the Zhongnan Sect from reading about it in what he thought was a novel, then stops himself before completing the reference."
  ],
  "continuity_sources": [
    139
  ],
  "open_questions": [
    "What conflict involving the Assistant Military Commissioner, Huashan, and an insult preceded Taekyung's arrival at the luncheon?",
    "What are the names and individual identities of the three Zhongnan Sect martial artists?",
    "What was Taekyung about to say after recognizing the Zhongnan Sect from the novel?"
  ],
  "safe_through": 139,
  "temporary_decisions": [
    "Render 전하 as “His Highness” when used as the formal royal address.",
    "Render 왕 as “king” when Cheongpung uses it literally, while preserving the official correction to “His Highness.”",
    "Render 초일류 as “advanced First Rate.”",
    "Render 군문 as “military” when describing an affiliation."
  ],
  "version": 1
}

## Reading copies

## Chapter artifact 135

# Chapter 135

*Smack!*

“P-please, help me!”

“No one’s coming to help you.”

*Smack-smack!*

“P-please, spare me!”

“No. Not happening. Go back.”

*Smack-smack-smack!*

“Th-then just kill me…”

“No, you’re still fine. Words are still coming out of your mouth.”

*Smack-smack-smack-smack!*

“Hhk… Hhrrgh…”

“Yes. That’s the reaction I was looking for.”

Only then did I finally stop my hand.

The young master’s face, which had been reasonably presentable until now, had puffed up like a steamed bun. Instead of a healthy flush, both cheeks were covered in dark blue bruises.

“Our Jintae. Did you do something wrong or not?”

“Hhrrgh.”

Seeing him sob with his face in such a mess, I suddenly felt a little sorry for him.

*Right. He’s someone else’s precious son, too…*

“You did something wrong, didn’t you?”

“Hhk! Hhrrgh!”

“Then why did you ignore what I was saying? You should’ve apologized the moment I told you to. Wouldn’t that have been better? Don’t you think?”

“Hhrrr.”

“Let’s live properly from now on. Understand?”

“Hhrrgh.”

I quietly watched Woo Jintae nod furiously before opening my mouth.

“But you…”

“Hh?”

“Why have you been answering like that this whole time? Can’t you speak like a normal person?”

His sobbing stopped dead.

“I-I’m sorry.”

“You could do it? You could speak, but you chose not to? Why were you crying? Were you trying to show everyone how much pain and hardship you were in?”

“No!”

“Your voice is getting louder, too. You’ve got some volume. Have you been practicing diaphragmatic breathing? Were you planning to blow out my eardrums and escape this crisis?”

“No. Absolutely not. Please, stop now. Hh-hhng…”

“Oh? You’re crying again? You can still cry? What have you done to deserve tears? Is your life over because you’re crying? And ‘please stop’? Anyone watching would think I was the one attacking you.”

“I’m sorry. I won’t cry.”

“Wow, look at him stop crying right away. You’re a creepy one, aren’t you? If I were you, I’d feel so guilty for picking on an innocent person that I’d cry until I passed out from exhaustion. Are you really sorry?”

“P-please, just listen to me for a moment…”

“Listen to what? Do you even have the right to speak? Is this some kind of entertainment awards ceremony? Am I supposed to sit quietly while you talk, then smile warmly and applaud when you’re finished?”

“…”

“Now you’re not even answering. You must feel full even without eating. Right? If you keep crunching through other people’s words like that, it must feel good…”

Just as I was about to continue, Woo Jintae slammed the back of his head into the floor with lightning speed.

*Thud! Plop.*

What a shame. I could have kept chewing him out for at least another shichen.[^1]

[^1]: A shichen is a traditional time unit equal to approximately two hours.

As I turned away from the unconscious Woo Jintae, countless gazes came flying toward me and stuck fast.

“The Young Bureau Head of the Seongun Escort Bureau went down that easily…”

“Who the hell is that young man?”

“His hands are vicious enough, but his tongue is a venomous snake all on its own.”

A murmur mixed with shock and fear spread through the room like a wave.

There were more than a hundred guests on the first floor alone. It was hardly surprising that some of them recognized my face.

“It’s the Sleeping Dragon of Shanxi!”

“What? The one from the Jin Family of Taiyuan?”

“Do you think there are two Sleeping Dragons of Shanxi? I knew his face looked familiar.”

*My reputation as the Sleeping Dragon of Shanxi really does reach the heavens.*

I was just about to give the crowd a pleased smile and wave when someone spoke up.

“Are you sure? I saw the Sleeping Dragon of Shanxi at Honghwaru around this time last year, but he looks a little…”

“You don’t remember that the two of us were there together?”

“Oh. Were we?”

“Yes. His build and overall impression have changed quite a bit, but it’s definitely him. I can still see him causing a scene because he wanted to bring a courtesan back to the Jin Family.”

“…”

*Damn. Why do people remember such useless things?*

As I awkwardly lowered my hand, several of the guests who had been whispering among themselves suddenly raised their hands.

“I was there, too!”

“You were, Brother?”

“I remember it clearly. That guy—no, that gentleman—fell down the stairs, grabbed the thing between my legs, and gave it a long yank… Whew. Just thinking about it still makes me dizzy.”

“My goodness, how indecent. Are you all right now?”

“Fortunately, I’m perfectly fine. Not only that, I think it’s gotten a little longer since then.”

“…”

*Can that happen?*

I barely managed to suppress my urge to ask the man who had just spoken exactly how much longer it had gotten. There was still the trash from the so-called Five Gates of Shanxi to deal with.

But then…

“Huh?”

What came into view were four young prodigies with their heads planted on the floor in a row—and Hyuk Mujin standing there with his head held oddly high.

“We’re ready.”

“Did you order them to do this?”

“They say that even a village-school dog can recite poetry after three years. Now, if you give me a hint, I know exactly what to do.”

“You little…”

I was seized by an indescribable emotion.

At first, I had thought he was an idiot, but he seemed to be getting smarter by the day.

I was almost suspicious that he was putting points into Intelligence for me.

“You’ve grown. I’m very proud of you.”

“You’re too kind. More importantly, what should we do with them?”

“Give me the sword case.”

“At your command.”

It was straight out of a historical drama. I took the sword case Hyuk Mujin held out and brought it down against my palm.

The grip was good, and the impact felt good, too.

“Everyone, get up.”

The four young prodigies sprang to their feet the moment I spoke.

Ignoring their terrified gazes, I scanned their Level Windows again. Just as I thought, they were barely First Rate, if that.

“You already know what you did wrong… You’re the heirs of the Five Gates of Shanxi?”

“Y-yes, sir!”

“The third son, the youngest daughter, that sort of thing?”

“No!”

“Are you sure?”

“Yes, we are!”

Their voices, filled with proper martial spirit, rang through the inn. I tapped the sword case against my palm and muttered,

“Really? Then the Five Gates of Shanxi aren’t anything special, are they?”

“…”

“…”

Every one of their faces flushed with shame, but none of them dared to answer.

They knew who I was now.

Their difference in martial power was only the second issue. Even putting that aside, people from the Five Gates of Shanxi couldn’t hold their heads high in front of the Jin Family of Taiyuan.

“You’ve had it good all this time, haven’t you?”

“…No.”

“What do you mean, no? You never had to worry about money, and you had powerful backing. You relied on that and lived large all this time, didn’t you? Picking fights wherever you went.”

“…”

“But then a war broke out between the Jin Family of Taiyuan and the Mount Heng Sword Sect. The Jin Family was the one that had always treated you well, but you were afraid of the retaliation that would come if Mount Heng won, so you kept watching the situation and ended up here. Right?”

“Th-that’s… We…”

“You’re the heirs, aren’t you? A Young Sect Leader, a Lesser Family Head—something like that, right? Ah, that fellow over there was the Young Bureau Head.”

The four people I pointed toward reflexively glanced in that direction and shuddered.

Unable to endure the merciless barrage of slaps and trash talk, Woo Jintae had chosen to pass out. He lay on the floor as though he were dead.

“Anyway, given the situation, you should’ve kept your heads down. What did you come all the way here for, acting so high and mighty? Do you think the Jin Family of Taiyuan is a joke? Do I need to tattoo ‘Sleeping Dragon of Shanxi’ on my forehead and walk around with it?”

“I-I’m sorry.”

“Does apologizing make everything go away? Should I beat you into a bloody mess and then apologize to you?”

“Eek!”

Just look at those terrified eyes. I felt like a walking disaster.

This was a situation that no longer required words. I raised the sword case.

“Historically, this has always been an effective remedy. Everyone, get down.”

Then I asked the four trembling young prodigies who lay face down in a chilling voice,

“How many blows will it take for you to reflect? Each of you, give me a number.”

“W-what?”

“Give me a number. I beat that Woo Jintae so badly because he was acting too high and mighty. Since you paid up voluntarily, I’ll take that into consideration.”

A heavy silence descended.

The four of them exchanged hurried glances before shouting as one.

“J-just one!”

“One? Will that really be enough?”

“Yes, sir!”

“If you take one hit, will you swear never to do anything like this again?”

“We swear it before Heaven and Earth and all the divine spirits!”

I gripped the sword case tightly.

“Good. Then ten each.”

“……!”

“……!”

“I just asked Heaven and Earth, and they said one wouldn’t come close to being enough for you. So ten it is.”

I never thought I’d find myself in a situation like this.

Back in school, I felt like one of those physical-education entrance-exam teachers who swung a bat whenever he got the chance.

Wallowing in a strange sense of nostalgia, I swung the bat—or rather, the sword case.

*Whack! Whack! Whack! Crack!*

“Guh!”

“Don’t move. You’ll hurt your bones. All right, again.”

*Whack! Whack! Whack!*

It must have been a rare sight for everyone filling Honghwa Inn. The heirs of the Five Gates of Shanxi were crawling across the floor like grubs.

There were even two women among them.

The whispers of the people surrounding us cut into my ears.

“Is that really okay?”

“I know, right? Even if they are the Five Gates of Shanxi… Couldn’t this turn into one of those big fights over Murim gratitude and grudges?”

“Don’t be so clueless. Are you really that out of touch with what’s happening these days? Maybe things would be different if the Mount Heng Sword Sect were still standing, but to stop the Jin Family of Taiyuan now, every small and medium-sized sect in Shanxi would have to join forces—and even then, they might not manage it.”

“It’s that bad?”

“They might have the numbers if they gathered everyone, but the caliber is completely different. You only have to look at the Sleeping Dragon of Shanxi over there to know that.”

“That’s true. Those Five Gates heirs swaggered around acting so important, but they’re completely worthless in front of the Sleeping Dragon of Shanxi.”

“If you think about it, they were the ones who picked the fight first.”

“That’s true, too.”

“And since we’re on the subject, there’s something rotten about all those people who call themselves the Five Gates of Shanxi these days.”

“Rotten?”

“They call themselves an orthodox faction, but they’re really just sucking the marrow out of ordinary people without anyone noticing. Just look at the Seongun Escort Bureau. How many complaints have merchants made about them?”

“Were all those rumors true?”

“What about the Jin Family of Taiyuan? When there was a famine ten years ago, they released relief grain. Long before that, they even held off the Demonic Cult. Those bastards were vicious murderers who went around killing ordinary people like us. If not for the Jin Family of Taiyuan…”

“Ugh. I don’t even want to think about it.”

“That’s right. I also heard it was the Jin Family of Taiyuan that drove off the mounted bandits who came over from Gaoyuan this time.”

“Is there anyone who hasn’t heard that rumor yet? They say the Heaven Shaking Sword and the Sleeping Dragon of Shanxi slaughtered every last one of them.”

“My goodness.”

“So even if another war breaks out, what’s there to worry about? I swear, if the Five Gates of Shanxi try to make an issue of this, I’ll join the Jin Family of Taiyuan and fight alongside them!”

“Oh!”

“That’s some impressive chivalrous spirit for such a young man. Now that I’ve heard you out, I think you’re right. Here, have a drink on me!”

*Whack! Whack! Whack!*

I had turned three of the four young prodigies into grubs when I turned my head toward the voices.

They were defending the Jin Family of Taiyuan with such passion that, by the time I finished listening, I almost wanted to buy them a drink.

*In terms of mindset, he’s already one of our Jin Family.*

If his Level were high enough, he’d be my first pick for recruitment. Smiling with satisfaction, I checked the Level Window of the great orator.

> **System**
>
> **Level 15: Jang Childeuk**

“…What the fuck?”

*Jang Childeuk? The Jang Childeuk I know?*

Looking again, I realized that I definitely knew the face.

He was the servant who had brought us meals every day while I was receiving one-on-one intensive training from Jin Mukyung.

That Jang Childeuk was the great orator’s true identity.

*Holy shit. Goose bumps.*

No wonder he had been taking the Jin Family’s side so aggressively.

He hadn’t said anything incorrect, of course, but manipulating public opinion like this…

Just as I trembled at the feeling that I had uncovered some enormous conspiracy in the political world, someone spoke up.

“Um…”

It was Cheongpung, the one person I had momentarily forgotten. He opened his mouth with his clear eyes shining.

“There’s still one person left.”

“Ah.”

The last man lying face down flinched. Cheongpung seemed innocent in his own way, but he was also strangely frightening.

Not that I had any intention of going easy on him just because he was last.

“I was just about to hit him.”

I was about to swing the sword case when Cheongpung spoke again.

“Excuse me. May I ask you one difficult favor?”

“We’re out of candied hawthorn skewers[^2] now.”

[^2]: Candied hawthorn skewers are a traditional snack of fruit skewers coated in hardened sugar.

“That’s not it. I, uh…”

Cheongpung hesitated, then quietly pointed at the sword case.

“I’d like to try hitting the last gentleman once.”

“What?”

“I’ve never done anything like this before…”

“…”

I had seen every kind of nutcase in my life, but this was my first time seeing a first-experience villain.
## Chapter artifact 136

# Chapter 136

“Ugh.”

“Gnnngh.”

The two men’s eyes met as they groaned. Seeing each other lying face down with their bare buttocks exposed was embarrassing, but it also gave them a strange sense of solidarity.

“Ahem. Young Hero Jeong, how are your wounds?”

“Ahem. More or less. How about you, Young Hero Gal?”

“I feel like I’m going to die, hngh!”

“Actually, same here, ngh!”

The pain returned as they spoke. Both men blinked back tears and muttered,

“There’s bad luck, and then there’s this. Out of all the people in the world, we had to run into the Sleeping Dragon of Shanxi.”

“I know. I never thought I’d suffer this kind of humiliation in my lifetime.”

The mood was gloomy.

In the Central Plains, where countless prestigious sects stood shoulder to shoulder, things might have been different. But out in borderland Shanxi Province, both men were heirs to sects big enough to swagger around spitting and farting as they pleased.

They had never once had to ask anyone for a favor or lower themselves in their entire lives. Now they were lying on a bed, groaning after being thoroughly beaten.

“Even when the Mount Heng Sword Sect was still standing, the Five Gates of Shanxi weren’t like this…”

“Those were the days.”

A few months ago, the Five Gates of Shanxi and the alliance of small and medium-sized sects could still have made their voices heard. Now, they couldn’t even squeak. The balance of Shanxi Murim had been shattered.

With the fall of the Mount Heng Sword Sect, the balance of power in Shanxi Murim was bound to tilt toward the Jin Family of Taiyuan.

“My father will kill me if he finds out.”

“Same here. He warned me so many times. If he finds out this happened… Ugh. I don’t even want to think about it.”

They had been publicly humiliated in front of more than a hundred people. By around New Year’s Day, the rumor would certainly have spread throughout all of Shanxi.

“If I had my way, I’d run far away.”

“To hell with running away. I don’t even know if I’ll be able to walk tomorrow. But I can’t refuse the City Lord’s summons, either…”

“Even if our legs are broken, we have to go. What else can we do? He isn’t just some ordinary City Lord. He’s a member of the imperial family.”

“That’s true. At least our faces are fine.”

“They are.”

Their eyes naturally shifted to the side.

Woo Jintae lay there as though dead, his face swollen like he had been stung by a swarm of wasps. If not for the occasional labored breath, they would have thought he was already dead.

“Still, how could anyone beat a person like that?”

“I never knew the Sleeping Dragon of Shanxi was this vicious.”

“Thank goodness we planted our heads on the floor beforehand. We almost ended up just like Brother Woo.”

“He absolutely would have done it. Isn’t he the bastard who beats women without mercy, too?”

There were two women among their group. A man might be expected to go soft in front of young, beautiful women, but that bastard Jin Taekyung’s reaction had gone far beyond anyone’s expectations.

“Age.”

“Y-yes?”

“Age. How old are you?”

“I-I’m seventeen.”

“And you?”

“I-I’m eighteen.”

Seventeen. Eighteen. They were both at the flower of their youth. They were also old enough for talk of marriage arrangements to begin circulating.

Just as everyone was wondering whether Jin Taekyung might be interested in the women, it happened.

“Lift your butt higher. You’ll break a bone.”

*Whack! Whack!*

“You kids are still wet behind the ears! And you’re already drinking!”

*Whack! Whack!*

“If you want to drink, hide somewhere and do it quietly! Don’t pick a fight with someone who was minding his own business!”

*Whack! Whack!*

“You haven’t learned how to behave! People like you are exactly why corporal punishment is necessary! Do you understand or not?”

*Whack! Whack!*

“Improve teacher authority! A certain amount of corporal punishment is absolutely necessary!”

*Whack! Whack! Whack!*

The two men trembled as they recalled what had just happened.

One had fainted, while the other had cried until tears and snot streamed down his face in front of everyone.

After having their buttocks thoroughly beaten by a man outside their families in front of so many people, it was only a matter of time before their marriage prospects were ruined.

“What in the world does ‘improve teacher authority’ mean? Is it something from Mencius?”

“I don’t know, either. He even hit me one extra time.”

“What a vicious bastard…”

“Even so, I envy the others.”

“What kind of outrageous thing is that to say? Can’t you see that your butt is covered in bruises?”

“At least the others were beaten by the Sleeping Dragon of Shanxi. I was beaten by some beggar-looking bastard… Sob!”

“Oh, that’s awful.”

“If I had been beaten by the Sleeping Dragon of Shanxi, I could have made excuses. But some mangy bastard whose origins I don’t even know beat my butt… What was he doing, borrowing a beating instead of money?”

His chin trembled with humiliation. He was thinking of the beggar-looking man who had taken the sword case from Jin Taekyung and gleefully thrashed him.

“Wow, this is fun! You have some good bounce in that butt!”

*Whack! Whack! Whack!*

“Does it hurt? How much does it hurt? If you don’t mind, can I hit you harder? This is my first time doing something like this, so please understand if I’m not very good at controlling my strength!”

*Whack! Whack! Whack!*

It was a moment of humiliation he would never forget—not until the day he died, and perhaps not even after death. If he could, he would have chewed that bastard from head to toe and swallowed him piece by piece, and it still wouldn’t have been enough.

“I will never forgive that bastard!”

“Don’t worry. I’ll help you however much I can, Young Hero Jeong!”

Who were they? They were the heirs of the Five Gates of Shanxi. Apart from Jin Taekyung of the Jin Family of Taiyuan, they had enough power to deal with a young beggar.

“Um, about that…”

“Yes?”

“Are you sure he really is a beggar? I’m not saying this because I’m afraid, but considering what happened with the Sleeping Dragon of Shanxi, I suddenly think there’s nothing to lose by preparing for the worst.”

“…Should we look into him a little more?”

“Y-yes. Let’s do that.”

The pampered rich kids had taken a group beating and finally learned to be cautious.

* * *

Once the lesson was over, we decided to move to a private room.

It was hard not to notice the eyes of the surrounding guests while we remained on the first floor.

Enjoying attention was fun for a moment or two, but if I tried to eat under these circumstances, I’d probably get confused about whether the food was going into my mouth or my nose.

“I’m Seok, the man responsible for Honghwa Inn. Please feel free to call me Chief Steward Seok.”

The Sleeping Dragon of Shanxi’s reputation really was something. The man in charge, who hadn’t shown even a trace of himself until now, had come to bow his head to me.

*This man must be part of the Lower District Sect, too, right?*

Honghwaru was Wolhwa’s base as the Chief Branch Leader of the Lower District Sect’s Shanxi branch, and Honghwa Inn was practically one of its subordinate organizations, as anyone could tell from the name.

He might even have known about my existence before I set foot inside Honghwa Inn.

*I can’t say that makes me feel particularly good.*

Was it overreacting to think that unseen gazes were monitoring my every move?

Still, I wasn’t exactly offended.

It was more like a little caution. We had certainly maintained a friendly relationship until now, but no one knew what might happen in the future.

“I’ve prepared a quiet place for you separately.”

“Oh, that sounds good.”

They were offering it as a courtesy, so there was no reason to refuse. I was just about to follow the chief steward when—

“Thank you for everything, Benefactor.”

I turned toward the voice and saw Cheongpung, wearing an innocent smile.

“What do you mean? Surely you aren’t planning to leave just like this?”

“Yes. It’s already late, so I was thinking of heading out.”

*Where does he think he’s going? We hadn’t even gotten to talk properly because those random bastards barged in.* I hurriedly waved him off. “Hey now, if it’s late, you should stay the night. You said you don’t have any travel money, right?”

“It’s all right. I’m used to sleeping rough.”

“You shouldn’t be used to that. Besides, this would be a new experience! Have you ever slept at an inn?”

“I stayed at an inn a few times before I lost my travel money. And I’ve already imposed enough on the two of you.”

Hyuk Mujin, who had been standing beside me, muttered,

“That’s true. With my candied hawthorn skewers[^1]—”

[^1]: Traditional fruit skewers coated in hardened sugar.

“You be quiet. So, are you really leaving?”

“Yes. Fortunately, I still have business left in Shanxi Province, so if we happen to get the chance, we’ll meet again.”

At this point, I had nothing left to say. If a Peak master was determined to leave of his own accord, I couldn’t exactly hold him back by claiming the roads were dangerous at night.

Even so, I was still intensely curious about the identity of this oddball who had suddenly appeared out of nowhere.

“If you have nowhere to go, come to the Jin Family of Taiyuan. If you give them my name, they’ll let you through.”

“Oh, now that you mention it, you’re a Young Master of the Jin Family of Taiyuan, aren’t you? The Sleeping Dragon of Shanxi, Jin Taekyung… I’ll remember the name of my Benefactor.”

He had known who I was for a while, yet he hadn’t reacted at all. His response amounted to, *Oh, I see,* and nothing more.

Hyuk Mujin subtly signaled me and cut in.

“The Jin Family of Taiyuan. You don’t know it?”

“Well, I think I’ve heard of it somewhere. It does sound familiar, but I don’t really know much about it.”

After tilting his head for a moment, Cheongpung bowed to us.

“If fate brings us together, we’ll meet again. Then I’ll be off.”

I replied with deep regret.

“Take care. And don’t forget the Jin Family of Taiyuan.”

“Haha, of course I won’t.”

He turned away with a hearty laugh. Thinking the conversation had come to an end, the chief steward spoke up.

“Then I’ll escort you to the annex.”

“Ah, yes. Mujin, let’s go.”

“Oh! We’re going to sleep in the annex of the famous Honghwa Inn?”

“We stayed in the annex at Phoenix Inn, too. Why are you acting like this is something new?”

“What are you talking about? If Phoenix Inn is a young prodigy, then Honghwa Inn is already a famous Peak master. Its hot springs, in particular, are such a renowned attraction that even high officials and nobles visit them.”

“Hot springs?”

“I’ve only heard about them from rumors, but they say there’s no paradise like it.”

The chief steward added in a calm voice,

“My father is turning eighty this year. He came here once and nearly departed for paradise.”

“…Isn’t that dangerous?”

“It only means the hot springs are that good. He’s still hale and hearty.”

“Ah, I see. I hope he lives a long life.”

Hot springs…

I had gone to saunas plenty of times, but I had never visited a hot spring. Just thinking about sinking into pleasantly hot water already had me excited.

“Ahem. Shall we go?”

“I’ll escort you.”

I was just about to follow the chief steward when a firm hand suddenly seized my shoulder.

“Um. Did you just say hot springs?”

“…You haven’t left yet?”

Looking at Cheongpung’s sheepish grin, I was certain of one thing.

I’d stake both my balls on the fact that this bastard had never been to a hot spring before.

* * *

In the early dawn, while darkness still blanketed the training ground of the estate, a man was swinging a sword.

He looked to be about thirty. His strong, rugged features were striking.

*Swish, swish, swish!*

He thrust, slashed, and swung without a moment’s hesitation. Each form flowed smoothly into the next, as softly as flower petals fluttering on the wind.

The Seven Plum Sword, in which he had reached eight-tenths mastery, cut through the cold dawn air when a messenger opened the main gate and entered.

“What is it? I forbade anyone from entering while I’m training.”

“I beg your pardon. His Highness Prince Shangshan ordered me to deliver a message…”

“His Highness?”

“Yes. It is the Prince’s command that you attend the luncheon at noon today.”

“The luncheon… You mean the gathering where the young prodigies of Murim are coming?”

“Yes, sir.”

The man let out a deep sigh. He was a Third-Rank Assistant Military Commissioner, an official who could easily be counted among the five highest-ranking figures in Shanxi Province.

*I can’t refuse an order from His Highness. What a nuisance.*

The position of Assistant Military Commissioner was by no means an idle one. It was a weighty office responsible for training the soldiers.

But the order had come from Prince Shangshan, the City Lord and a man of royal blood. The man had no choice but to nod.

“Tell him I accept the royal command.”

“Yes, sir!”

After the messenger left, the man picked up his sword again.

As he began the Seven Plum Sword once more, it seemed as though the plum blossoms of Huashan, which he had left behind long ago, were blooming from his blade.
## Chapter artifact 137

# Chapter 137

“Are you awake?”

A familiar face abruptly opened the annex door and barged in.

I had just finished circulating my qi, so I unfolded my legs from the lotus position and spoke.

“You came in without even waiting for an answer?”

“Come on, Captain. You and I aren’t that distant.”

“What kind of relationship do you and I have?”

“Not related by blood, but comrades who can fight back-to-back? A lord-and-vassal relationship tightly bound by affection and trust?”

“Affection? Hmm. You’ve made up your mind to get beaten half to death first thing in the morning.”

“One hit, then. Surely I won’t die.”

He was getting more shameless by the day. I let out a quiet laugh and shook my head.

“Enough. What brings you here so early?”

“Obviously… Wait, what’s with that guy? Did he sleep here?”

Hyuk Mujin stared incredulously at Cheongpung, who was sprawled out in the corner.

“Why would he sleep here when the annex has several rooms?”

“Leave him. These things happen. I found him asleep when I got back from the privy.”

To cut to the conclusion, I had failed completely at figuring out Cheongpung’s identity.

The moment he got out of the hot spring, he had fallen asleep from exhaustion. I couldn’t bring myself to wake him, so I slept, too.

“Even so, Captain. How could you let a strange man you met yesterday sleep in your room?”

“…That sounded a little strange.”

“That’s not what I meant. I’m saying you should be more careful.”

“Careful? Anyone listening to you would think he was an assassin.”

“Can you say for certain that he isn’t?”

“What?”

“You’re a good man in many ways, Captain, but I think you take the Murim too lightly. This is a place tangled up in complicated gratitude and grudges. If you let your guard down, you really could end up dead.”

“What an unlucky thing to say. Want me to send you there?”

“Seriously! I’m not joking.”

Mujin thumped his chest in frustration, then watched the sleeping Cheongpung with wary eyes.

“Isn’t he a little strange? He seems remarkably skilled for someone so young, yet he wanders around dressed like a beggar. And he isn’t even a Disciple of the Beggars’ Sect.”

“Maybe that’s just the way he’s wired.”

“What if all of that is just a disguise meant to lower people’s guard? If he were a trained assassin, it would be entirely possible.”

“An assassin? Who would even want to target me?”

“Why wouldn’t anyone?”

“You know I’m not such a bastard that I make people hold grudges against me everywhere I go.”

“…Just counting yesterday, I think at least five people now have a grudge against you.”

Come to think of it, he had a point.

But suspecting Cheongpung of being an assassin was an overreaction.

I spoke to Mujin, who was still shooting Cheongpung suspicious glances.

“This guy isn’t one. If he were an assassin, would I still be alive?”

“Well, that’s true.”

“And what assassin? Aside from those Five Gates of Shanxi bastards, who could possibly have a reason to hold a grudge against me?”

“Did the Head Elder try to kill you because of some personal grudge? What about the martial artists of our family who died in the last war?”

“That… is true.”

Mujin shook his head from side to side.

“I’m only telling you to be careful. The gratitude and grudges of the Murim run deep and stay hidden, so no one knows when or where something might happen.”

“Hmm.”

“Flies swarm around appetizing food. The more famous the name Sleeping Dragon of Shanxi becomes, the more trouble you’ll have to deal with. There are even people who show up out of nowhere and challenge you to a life-and-death duel.”

The world was a big place, and there were plenty of lunatics in it. I was surprised to hear something I had never imagined, but I was also impressed by Mujin.

*This guy is saying something genuinely useful for once.*

“You know quite a lot. What a good boy.”

“Ahem. It’s nothing worth making a fuss over. I’ve just seen a lot of things.”

As expected of a local. People in the Murim around my age had apparently seen assassins killing people and all kinds of other things.

“Does that sort of thing happen every day in the Murim? You know, you go out to the market and see martial artists getting into arguments and fighting each other?”

“What?”

Mujin blinked.

“What are you talking about? This is Taiyuan. The public order is excellent.”

“Oh. So not often, but sometimes?”

“Sometimes? I lived in Taiyuan for nearly twenty years before entering the Jin Family of Taiyuan, and I never once saw martial artists fighting each other.”

“…What?”

“The Shanxi Provincial Office, where the City Lord resides, is half a shichen west of here, and the Jin Family of Taiyuan is one shichen east. Starting a sword fight for no reason would only make your life miserable. Even the lowest wandering martial artists pretend to be Great Heroes of honor and justice in Taiyuan. You didn’t know that?”

What the hell was this guy talking about?

After a brief silence, I spoke.

“You said you’d seen a lot of things, didn’t you?”

“What? Oh, that?”

“Yes, that.”

“Of course I read about that in books.”

“…Books?”

“Yes. There was a bookstore run by an old man in front of my house. For one nyang in iron coins, you could read books for half a shichen. That’s where I nurtured my dreams.”

Mujin gazed out the window with a nostalgic look in his eyes.

*The Shop Assistant Becomes a Sword God, You Must Hurt to Become a Martial Artist, The Son of Murim Walks Three and a Half Rounds Around the Nine Provinces and Eight Wastes,* and so on. They were really interesting.

“Oh, so you decided to become a martial artist after reading those books.”

“Of course. I even bought and kept a few of them when the bookstore went under. Would you like to borrow them?”

“No, I’m good. Anyway, Mujin.”

“Yes?”

“Do you really want to get beaten to death?”

I was an idiot for being impressed.

This wuxia-novel otaku bastard was confusing fiction with reality. I grabbed Mujin by the lapels.

“Do you think novels and reality are the same? Huh? Didn’t any of the novels you read have someone getting beaten to death for running his mouth?”

“W-wait! Wait! I’ve never personally witnessed anything like that, but the Murim is more than capable of—”

“Right, next otaku.”

*Smack!*

* * *

Honghwa Inn stood in the center of Taiyuan. Even in Taiyuan, which was known as Shanxi’s prime real estate, it was famous for its excellent location.

It was only natural for the area in front of Honghwa Inn to be crowded with people, but today the crowd was unusually large.

“Oh dear, what’s all this?”

“There’s a carriage and soldiers… Hey, Mr. Yang, have you heard anything? Is there a war breaking out?”

“I haven’t heard nothin’.”

Amid the murmuring, a luxurious, enormous carriage drawn by six fine horses came to a stop.

Then at least a hundred soldiers stood in neat ranks at the entrance to Honghwa Inn. An official dressed in his robes shouted loudly,

“Receive the royal command of His Highness Prince Shangshan!”

“Receive the royal command!”

The short phrase royal command carried tremendous weight. On top of that, the thunderous cry of a hundred elite soldiers caused hushed voices to spill out from every direction.

“Did you hear that?”

“Do you think my ears are decorations? I heard them say royal command.”

“Any idea what this is about?”

“I heard the Sleeping Dragon of Shanxi is staying at Honghwa Inn. Isn’t it probably because of him? Everyone knows the young Prince likes martial arts.”

“I know that much, but I’m saying this because he’s never made such a commotion before.”

“Well, the Sleeping Dragon of Shanxi has become awfully famous lately. He even wiped out those Red Wind Band bastards in place of the government troops not long ago, so he’s certainly done the Prince a great service.”

“Do you think His Highness plans to grant him an official post… Ah, they’re coming. They’re coming!”

At someone’s shout, countless eyes turned toward the entrance of the inn.

The doors stood wide open. As the people summoned by the Prince appeared beneath the glaring sunlight, a wave of excitement spread through the onlookers.

“Oh! Is that the Sleeping Dragon of Shanxi?”

“There’s more than one of them.”

“They’re wearing swords, so I suppose the others are young prodigies, too.”

“Then which one is the Sleeping Dragon of Shanxi?”

“Can’t you tell at a glance? The tallest and most handsome one in the middle. That’s Young Hero Jin Taekyung, the Sleeping Dragon of Shanxi.”

“My, my. They’re all handsome men and beautiful women, aren’t they?”

As the people whispered, five figures emerged, each one worthy of being called a dragon or phoenix.

Among them, Jin Taekyung’s presence was head and shoulders above the rest. At the very moment admiring gazes poured toward him as he stood tall in the center—

“Ugh!”

*Thud!*

“…?”

“…?”

One of the young prodigies suddenly crumpled to the ground.

Not only the onlookers but even the soldiers standing at attention stared at the fallen prodigy as though they had no idea what was going on.

“Ahem. Ahem!”

When the official cleared his throat, the fallen man’s face turned bright red.

The young prodigy who had fallen flat on his face got back up on legs trembling like a newborn calf. The official unfurled a red silk scroll.

“Ahem. The young prodigies of Murim shall receive the royal command! I, the younger brother of the holy Son of Heaven…”

“Eek!”

*Thud!*

This time, the one who collapsed was a woman.

The unexpected accident made the official’s breathing turn ragged for a moment. But he was the bearer of a royal command. He couldn’t let something so trivial throw him off.

The official composed himself and took another breath.

“I, I…”

“Gasp!”

*Thud!*

“The command I issue to you…”

“Eek!”

*Thud!*

This time, even the official couldn’t escape the disaster. Perhaps he had bitten his tongue, because a cracking sound came from his mouth, followed by blood streaming down his lips.

The crowd fell silent, though for a different reason than before.

As the official stood there in despair, one person approached him with a confident stride and whispered,

“Do we really have to do this outside? Why not just do it inside?”

The official considered Taekyung’s words for a moment before answering.

“Let’sh do that.”

“…Just nod. You’ll get blood on your clothes.”

* * *

The official spoke with a grave expression.

“How on earth did this happen?”

Everyone was watching me for a response. In the end, I had no choice but to explain the situation as briefly and clearly as possible.

“The kids aren’t feeling well.”

“Not feeling well? What do you mean?”

“They’re the fresh young pillars of Murim, aren’t they? They trained so hard to become stronger that they wore themselves down and keep collapsing.”

“Is that really what happened?”

“…”

“…”

It was quiet enough to hear a mouse breathe. I turned slightly and asked,

“He’s asking whether that’s true. Did you not hear him?”

The four young prodigies of the Five Gates of Shanxi jolted as though they had seen a ghost.

“O-oh, no. We heard him. We were just thinking of an answer…”

“Th-that’s right. I was waiting for someone else to answer…”

“What was there to think about? Just tell him the truth. Isn’t that right? Hahaha.”

Of course, if they told the truth, they would get some private one-on-one time with me. The law was far away, and fists were close at hand.

The four of them, who had no choice but to stay on the good side of the Jin Family of Taiyuan if they wanted to live in peace in Shanxi Murim, forced smiles onto their faces.

“Well, that’s what happened.”

The official looked suspicious and asked another question.

“But why is one person missing? As I understand it, there should be six people, including Young Hero Jin.”

“Ah, you mean the Young Bureau Head of the Seongun Escort Bureau.”

“That must be him. His name was…”

“Jintae. Woo Jintae.”

“That’s right. Why hasn’t he come out?”

*Because that one is in no condition to be seen as a human being.*

If I had known from the start that the Five Gates of Shanxi’s young prodigies had been invited to this luncheon with me, I wouldn’t have beaten him quite so badly.

*Well, what’s done is done.*

All I could do was clean up the mess as best I could.

I shook my head with the most sympathetic expression I could manage.

“Last night, he got injured after a minor disagreement and still hasn’t regained consciousness.”

“A disagreement? Are you saying he got into a fistfight?”

“Something like that. In any case, his face is in such a state that he simply can’t appear in front of people.”

“Good heavens. What kind of fiend would do that to a guest invited by His Highness?”

“…”

This felt really strange. With the culprit standing right in front of him, the official muttered something about treason, then lamented.

“This is a serious matter. Whatever the reason, the fact remains that he can’t attend the invitation. How furious will His Highness be when he learns of this?”

“Could I perhaps explain things to him properly?”

“Young Master, you don’t understand. Once His Highness takes offense, no one can stop him. The surrounding area will be turned into a wasteland for the time being.”

“Turned into a wasteland? What do you mean by that?”

“What else could I mean? First, they’ll arrest and severely punish the man who injured the Young Bureau Head of the Seongun Escort Bureau. Then, citing the terrible state of public order, dozens of officials will be forced to resign. I’ll probably be one of them.”

“…”

Why would they take it that far?

The official, who looked like he was about to be laid off in the prime of his life, added the finishing touch with a tragic expression.

“I have more than ten family members to feed… Sigh. I can only blame the heavens.”

*He has a big family, too.*

Just when I was unable to sit still and desperately racking my brain, it happened.

“Yaaawn.”

A carefree yawn completely out of place in the atmosphere.

My eyes lit up when I saw someone coming downstairs with a long stretch.

“Hey, how about we do this?”

“Hm? What do you mean?”

“If we bring along an even more impressive young prodigy, there won’t be a problem. Right?”

“I can’t be certain, but that’s probably true. His Highness wouldn’t complain if you found someone even more outstanding.”

Perfect.

With a triumphant smile, I waved at Cheongpung.

He was a young prodigy who was no less than a Peak master.

“Have you ever seen a member of the imperial family?”
## Chapter artifact 138

# Chapter 138

The luxurious six-horse carriage raced onward without slowing.

Soldiers who looked like elite troops cleared the road ahead, while the people who had been swarming around like ants split neatly to either side and watched the carriage dash past like the wind.

“So this is how Moses felt.”

Cheongpung reacted to my mutter.

“Moses? Who is that?”

“Someone.”

“Oh, I see.”

If it had been Hyuk Mujin, he would have complained for ages about me saying something strange, but Cheongpung was different.

He had the excited expression of a child at an amusement park as he pressed and tapped every part of the carriage.

“This is my first time riding in a six-horse carriage!”

“…What about a four-horse carriage?”

“I’ve never ridden in one of those, either!”

“What about an ordinary carriage…?”

“I’d like to ride in one of those, too!”

“…”

If I put him on a subway, he would probably faint.

At this point, it would be much faster to count the things he had done than the things he had never done.

I stared at Cheongpung, who had entered a state of total excitement.

*What the hell is this guy?*

Was he innocent or stupid?

Then again, he had said he had lived his entire life in the mountains. Maybe this was only natural.

*At least he’s easy to handle.*

I still couldn’t forget the expression he had just made. His eyes had lit up like high beams at the mere mention of the imperial family.

*“Have you ever seen a member of the imperial family?”*

*“I want to! I’ll see one! Please let me see one!”*

What filled his eyes wasn’t the sort of admiration ordinary commoners felt toward the imperial family. If I had to compare it to something, it was more like the excitement of going to see an elephant at the zoo.

*He really is a strange one.*

Apparently, I wasn’t the only one who thought so.

The young prodigies of the Five Gates of Shanxi, excluding the severely injured Woo Jintae, were staring at Cheongpung as if they were looking at something bizarre.

“Is he really all right…?”

“Can we really go like this?”

“If he says something inappropriate in front of His Highness, we might get dragged into it, too.”

“It’ll be lucky if it ends with him saying something inappropriate. If he gets excited about seeing an imperial family member for the first time and pulls on his ear, we’re finished. Completely finished.”

…That was a surprisingly plausible prediction.

Hearing the young prodigies whispering, the official riding in the carriage with us leaned over and spoke in an anxious voice.

“Um, Young Master Jin.”

“Yes?”

“That person… Is he really all right?”

“Believe me. He’s a master I can vouch for.”

“To hell with whether he’s a master. I’m asking whether he’s right in the head.”

“Oh.”

“Wouldn’t it be better to bring along the martial artist who was with you instead?”

“Who? Ah, Hyuk Mujin?”

“I believe that was his name. I hear he’s also quite skilled in martial arts.”

If Mujin had heard that, he would have jumped for joy.

The problem was that he had a dark blue bruise on his face from getting beaten by me that morning, so there was no way he could come along.

*And Hyuk Mujin wouldn’t be enough.*

To avoid offending the young prince, I needed to bring a more impressive gift.

I firmly shook my head at the worried official.

“Don’t worry. I’ll take responsibility for making sure nothing happens.”

Who was I? A direct descendant of the prestigious Jin Family of Taiyuan, a rising star, and Shanxi Murim’s newest sensation.

My bold assurance brightened the official’s expression a little.

“Then I’ll trust Young Master Jin—”

*Crack.*

“…?”

“…?”

Wait a second. What was that sound?

As though we had made a pact, we all turned our heads at the same time.

There was Cheongpung, clutching something in his hands.

“Huh? Why did this fall off?”

The official stared at me in silence for a long moment as Cheongpung grinned foolishly while holding an exquisitely crafted golden dragon.

“Young Master Jin.”

“Yes?”

“Is he really all right?”

After thinking it over, I opened my mouth.

“Probably.”

* * *

The space was so vast that it could have been called a castle rather than a residence. A man strode through it without hesitation.

Everyone who saw his tightly pressed lips and resolute gaze respectfully paid their respects.

“Greetings, Assistant Military Commissioner.”

He acknowledged them with a nod and quickened his pace.

After passing through a corridor lined with endless pillars, how long had he been walking? The man finally stopped when a massive iron gate engraved with a dragon appeared before him.

“Announce me.”

“Yes, sir.”

A commander from the palace guard saluted him and called out in a powerful voice.

“His Excellency Li Feng, Assistant Military Commissioner of Shanxi Province, entering!”

Before long, a voice answered from within.

“Let him enter.”

“…”

The voice was neither as high and childish as a little boy’s nor as deep as a grown man’s.

At the moment the man—Li Feng—seemed to realize something and his eyebrows shot up, the iron gate opened with a heavy groan.

*Grrrnnng.*

Beyond it was an extravagantly decorated grand hall. Gold and silver treasures glittered in every direction, and a table large enough for dozens of people was covered with every delicacy from land and sea.

It was a sight that would have left anyone else gaping. But Li Feng’s gaze remained fixed on a single point.

*How is he here?*

At the end of Li Feng’s gaze, a man seated at the head of the table smiled faintly.

Wrapped in dazzling red silk, the man spoke in a coy, lilting voice.

“Well, well. If it isn’t our Assistant Commissioner Li.”

*Our Assistant Commissioner Li?*

Li Feng bit down on his lips and performed a military salute.

“…Greetings, Deputy Military Commissioner.”

The Deputy Military Commissioner was a second-rank official, with only two such posts in each province.

Aside from the Military Commissioner, who was the commander-in-chief, and the City Lord, Prince Shangshan, it was the highest position there was. As the deputy commander, he also wielded tremendous authority.

That was what people knew publicly. In truth, the man before him possessed even greater power.

*That bastard deserves to be beaten to death.*

A sycophant and corrupt official who used his glib tongue and petty tricks to blind the young prince’s eyes and ears while lining his own pockets. That was Li Feng’s assessment of him.

But even beneath Li Feng’s openly hostile gaze, the man continued smiling.

“Assistant Commissioner Li, it’s been a while. Isn’t the atmosphere a little too tense? Did I perhaps do something to offend you?”

“…Of course not. I was merely surprised to find you in a place like this, Deputy Military Commissioner.”

“A place like this?”

“It is a gathering of martial artists from the martial world. They are rather rough people, so I was concerned that you might be uncomfortable, Deputy Military Commissioner.”

His words sounded considerate, but their true meaning was different. Neither man was unaware of that.

“What’s the problem? I like places like this. Besides, you’ve been so stiff with your title since a while ago. Just call me whatever you like. We’re close enough, aren’t we?”

“Close enough for what, exactly?”

“We’re the kind of people who would split a bean between us. True loyal subjects who serve His Highness with all our hearts.”

*Split a bean between us? True loyal subjects?*

Li Feng asked bluntly,

“Then may I call you Eunuch Hong?”

The smile on Eunuch Hong’s face stiffened for a moment.

With a single word, Li Feng had touched his sore spot.

“That’s… a little too familiar, don’t you think?”

“I only followed your instructions.”

“Well, this is something. I didn’t realize Assistant Commissioner Li considered me that close.”

“I’m overwhelmed that you understand my feelings at last.”

“Assistant Commissioner Li.”

“Did you call, Eunuch Hong? Or should I go back to calling you Deputy Military Commissioner?”

A heavy silence settled over the hall.

It was a long while before Eunuch Hong opened his mouth again.

“Our Assistant Commissioner Li has improved quite a bit, hasn’t he?”

“Have I?”

“Yes. Compared to a few years ago, you’ve made remarkable progress.”

“I’ve learned many things thanks to you.”

“I thought you were only good with a sword, but now I see you’re good with your tongue, too. I’ll have to look at you differently.”

“I’m still nowhere near as skilled as someone else.”

Their gazes collided in midair. Within the tightly stretched silence, Eunuch Hong smiled gently.

“Well, we can talk about that later… May I ask you one thing?”

His opponent was no pushover, but he had taken a step back. If he kept biting at him, he would only end up at a disadvantage. Li Feng silently nodded.

“Ask.”

“You said you used to belong to Huashan, didn’t you?”

Li Feng paused. Huashan was a place he both missed and remembered with pain.

It had been nearly ten years since he had left Mount Hua, but the memories of that time still remained deep in his body and heart.

“Yes. I was a lay disciple.”

“And Huashan is in Shaanxi?”

He and Eunuch Hong were what one might call political enemies. For that very reason, they knew one another inside and out.

Eunuch Hong was neither careless nor stupid enough to ask about such a basic fact without a reason.

If anything, he was a crafty man with a hundred snakes writhing inside him.

That was why Li Feng was even more puzzled.

“That’s right. But why are you suddenly asking?”

“I’ve come to know a few people recently, and I wondered if you might know them, too.”

“Are they martial artists?”

“Yes. And they’re from Shaanxi.”

“Don’t tell me they’re from Huashan…?”

“Oh, come on. If they were, I would have told you already.”

Li Feng let out a sigh of relief.

In the end, he had left of his own accord, but Huashan was still the sect he would be proud of for the rest of his life. It was a tremendous relief that he had not been entangled with a sycophant like Eunuch Hong.

“There are more than one or two sects in Shaanxi. And I didn’t go outside while training at the main sect, so even if I heard their names, I might not recognize them.”

“Is that so? Then perhaps you would recognize them if you saw their faces?”

“…?”

Seeing Li Feng’s expression, Eunuch Hong picked up the chopsticks lying on the table.

“You asked earlier why I was here, didn’t you?”

The beautifully crafted silver chopsticks tapped against a wine cup.

*Ping.*

The clear sound spread through the hall.

Eunuch Hong gave the bewildered Li Feng a knowing smile.

“I invited a few acquaintances. Famous and powerful martial artists whom His Highness would enjoy meeting.”

At that moment, a powerful shout rang out from beyond the iron gate.

“The Three Hands of Zhongnan request an audience!”

“The Three Hands of Zhongnan… The Zhongnan Sect!”

Li Feng’s complexion changed drastically.

Huashan and the Zhongnan Sect had been bitter rivals fighting for supremacy in Shaanxi for a full hundred years.

Eunuch Hong’s intentions were every bit as clear as the smile on his face.

“They’re from Shaanxi, so I thought I’d arrange a gathering. Isn’t that nice?”

Just as Li Feng clenched his fists, the massive iron gate opened and three imposing men strode into the hall.

One of them had a familiar face.

“Well, well. If it isn’t Li Feng of Huashan?”

Li Feng’s body trembled. The moment he saw that man’s face, the humiliating memory from ten years ago came rushing back.

“How did you get here?”

The sharp-eyed man answered casually.

“How did I get here? When the Deputy Military Commissioner of Shanxi Province invites you, you have to come running even if it’s a thousand li away. Isn’t that right?”

“There’s no need to thank me. I’m the one grateful that you accepted the invitation.”

*Grind.*

Gong Ilhyuk, the third of the Three Hands of Zhongnan, grinned at Li Feng as he ground his teeth.

“Anyway, you’ve done well for yourself. Assistant Military Commissioner, someone like you… Huashan must have spread around quite a bit of silver for you. Hmm?”

“How dare you insult Huashan?”

“Insult Huashan? You’re the one who insulted it. Ten years ago, who was it that knelt after a little over a hundred exchanges against that magnificent Huashan martial arts?”

“You bastard!”

A thunderous shout burst from Li Feng’s mouth.

At the moment he glared at Gong Ilhyuk with eyes that seemed to pour out streams of flame, a third shout rang out from beyond the iron gate.

“The young prodigies of Shanxi Murim request an audience!”
## Chapter artifact 139

# Chapter 139

The six-horse carriage carrying Jin Taekyung and his group had been on the road for less than a shichen when the streets of Taiyuan heated up once again.

This time, it was because of the fifty mounted soldiers surrounding the four-horse carriage, as well as the martial artists radiating sharp, piercing gazes.

“That’s…”

“It’s the Jin Family of Taiyuan!”

“Woooooah!”

“First the Sleeping Dragon of Shanxi, and now the Jin Family of Taiyuan? My eyes are getting spoiled today.”

Inside the carriage, Jin Wikyung’s ears pricked up at the cheers pouring in from every direction.

“Mukyung, did you hear that just now?”

Jin Mukyung yawned and nodded.

“Yes. I heard it.”

“Wipeng, you too?”

Wipeng answered with an exasperated expression.

“You don’t care whether I heard it or not. Just say what you wanted to say.”

“Why do you always speak like that? Does it make you feel better?”

“Feel better? I’m about to give myself an ulcer as it is. So what did you want to say?”

“People were saying that Taekyung…”

“Wow. This is driving me insane.”

Jin Wikyung pretended not to hear Wipeng’s muttering and continued.

“It seems he’s on his way to attend a luncheon with the City Lord. He might even have arrived by now.”

“He probably has. It’s close enough to touch if you fall over.”

“I hope nothing happens.”

“The Third Young Master isn’t some little child you’ve left beside a pond. He’s probably being treated to such an extravagant meal that the table legs are breaking. Stop worrying.”

“I don’t know. He’s such a free-spirited child.”

Wipeng’s eyes went round as though he were asking what the hell that was supposed to mean.

“Free-spirited? Isn’t this more a case of him being reckless and out of control?”

“Ahem.”

“You could just say you’re worried he’ll cause trouble. Why do you have to dress it up like that…?”

“Shut your mouth.”

“Yes, my lord. Then I won’t say anything. If you’re really that worried, ask the Second Young Master over there.”

At Wipeng’s indifferent reply, Jin Wikyung’s gaze shifted slightly to the side.

In truth, Wipeng’s advice was appropriate. Jin Mukyung was the only person among them who had ever met Shanxi’s current City Lord, even once.

*The problem is that he won’t tell us anything else.*

Jin Mukyung had dismissed his luncheon with the Shanxi City Lord with a single phrase—*It was fucking awful*—and had firmly kept his mouth shut ever since.

“Mukyung, by any chance…”

Before he could finish, an answer came flying back.

“There shouldn’t be any problems.”

Jin Wikyung let out a relieved sigh at the decisive answer, but Jin Mukyung added one more thing.

“If his stomach can handle it.”

“…His stomach? What are you talking about all of a sudden?”

It was a meal hosted by royalty and the City Lord. Was he saying they might serve food crawling with maggots at such a grand banquet?

As confusion filled Jin Wikyung’s gaze, he saw Jin Mukyung’s face slowly twist.

“There’s someone here as disgusting as a bug.”

* * *

The Shanxi Provincial Office, where the City Lord resided, had long since outgrown the shape of an ordinary estate.

The Jin Family of Taiyuan and the Mount Heng Sword Sect, which I had visited not long ago, were both enormous, but compared to this place, they seemed laughably small.

*What should I call this? A fortress? No, a castle?*

I had known for a long time that the continent operated on a massive scale, but this was beyond anything I had imagined.

Cheongpung and the other young prodigies gaped as they looked around. The official gave a small smile.

“What do you think?”

“It’s big. Extremely big.”

“It can easily accommodate several thousand people, so it has to be. If we had to defend it during wartime, we even have enough grain to last ten years.”

The official pointed to several enormous warehouses one after another. He added that they were filled with food.

“All of those?”

“Of course.”

The official continued with a proud smile, like a resident of a Gangnam apartment showing off his building.

“Provincial offices are generally built large and sturdy in preparation for wartime, but they aren’t normally this large.”

“Then…?”

“Have you already forgotten who lives here?”

“Oh.”

Right. He wasn’t merely the City Lord. He was a member of the imperial family. On top of that, he possessed an official royal title—a proper prince in his own right.

“Then is this the royal palace?”

“In a manner of speaking.”

We continued moving, looking around like country bumpkins.

Everywhere we looked, servants and maidservants hurried about their business, while elite soldiers with razor-sharp discipline stood guard or sparred in the training grounds.

*They’re pretty good.*

The most surprising thing was the remarkably high quality of the soldiers.

Most of the soldiers standing guard were around Level 20, while the commanders wearing fairly impressive armor were comfortably above First Rate.

*Well, it’s not as if there’s any reason they shouldn’t learn martial arts when they’re readily available.*

If anything, it would make the army stronger. It was something that ought to be encouraged.

I kept walking while glancing toward the training grounds.

*Boom! Boom! Boom!*

“Thrust!”

“Argh!”

It was noon, with the sun already high overhead.

Hundreds of spearheads flashed in time with the drums, and the soldiers gathered and scattered in perfect unison, moving as one body.

Watching them train in formations, tactics, and battle strategies, one word suddenly came to mind.

*Raid team.*

Uniform weapons. Coordination drilled into them through systematic training. In a large-scale battle, that kind of teamwork would display terrifying power.

*Their individual skills might be inferior to those of Murim martial artists.*

A battle of dozens against dozens might be another story, but if hundreds fought hundreds, or thousands fought thousands, even an ordinary Peak master couldn’t turn the tide by himself.

That was the terrifying strength of a trained group.

*Make up for inferior quality with numbers and training. Is that it?*

It was just as one would expect from a unified empire that had ruled a vast territory for hundreds of years.

Wasn’t that part of the reason those proud Murim martial artists acknowledged that they were subjects of a great nation?

And yet…

*What the hell are they keeping all this for? To trade it in for candy?*

There were already more than several hundred soldiers in sight. If even a portion of them had been sent to northern Shanxi, the Red Wind Band would have made a run for it long ago.

*Fuck. Some of us nearly died going through all that trouble.*

Seeing the true face of incompetent public authority suddenly plunged me into a spell of hollow enlightenment.

What good was owning the finest sword under heaven? If you didn’t draw it from its scabbard, it was no different from a club.

Just as I was cursing them inwardly, the official spoke.

“Well, we’re almost there.”

He was right. At the end of a long corridor lined with dozens of pillars, a massive iron gate came into view, and anxious sighs escaped from both sides.

“Phew…”

“Whew. What do I do, Young Hero Jeong? I’m so nervous.”

“Don’t worry. You have me.”

“…What a fucking load of bullshit.”

They say people destined to succeed will succeed, but I had no idea how those two had managed to hit it off in the middle of all this.

*Maybe getting beaten together made them fall for each other?*

*What kind of country is this?*

Unable to hide my discomfort as a two-star general of the Singles Brigade, I heard Cheongpung ask brightly as he walked along with a light step.

“Is the king inside?”

King.

At that single word, the young prodigies of the Five Gates of Shanxi gaped, while the official leading us leaped as though he had been stung by a bee.

“A king? How impudent!”

“Huh? Isn’t he a king?”

“Of course he’s a king!”

“Then wasn’t I right?”

“No, that’s not what I mean…!”

At this rate, one of two things would happen. The official would collapse from high blood pressure, or he would invoke treason and immediately summon the hundreds of soldiers training in the grounds.

I wanted neither, so I stepped in to mediate.

“First, calm down. And, Young Master Cheongpung.”

“Yes, Benefactor.”

“You can’t call him a king. You have to say ‘His Highness.’ Right?”

The final question was directed at the official. He glared at Cheongpung and nodded furiously.

“Absolutely! You must!”

“Oh, really?”

“Phew. Yes.”

Cheongpung blinked his clear eyes.

“Why?”

“…Young Master Jin. Do we really have to take this fellow—or rather, this person—with us?”

“I don’t mind leaving him out. But are you sure you’ll be all right?”

The official fell silent for a moment.

If he took five people without Cheongpung, he would be reprimanded by his superiors and lose his job. But if Cheongpung let his tongue slip just once, he might lose his head.

A moment later, when he spoke again, his face looked ten years older.

“…Let’s just go.”

Cheongpung beamed.

“Thank you. If we have time, I’ll put in a good word with the king—or rather, His Highness.”

“Please, just keep that gentleman’s mouth shut.”

The official proceeded to list every precaution we needed to take, along with his earnest pleas, and we finally reached the iron gate.

The gate was so enormous and thick that it was almost absurd. From behind it came the sound of quiet voices.

*Assistant Military Commissioner, Huashan, insult?*

Those fragmentary words alone gave me no clue what kind of conversation was taking place. Still…

*The atmosphere doesn’t seem very good.*

I had a feeling this wasn’t the best place for people to sit across from one another over a meal.

At that moment, a man standing at attention before the gate shouted loudly,

“The young prodigies of Shanxi Murim request an audience!”

*Groooan.*

The iron gate began to open at the same time.

The official gave me one final warning with a worried expression, stealing a sidelong glance at Cheongpung.

“Please just keep that man’s mouth shut.”

“…Ah. Yes.”

He must have been extremely worried.

* * *

The moment we entered, it felt as though my eyes had brightened.

The lavishly decorated grand hall was filled with a long table like the ones I had only seen in movies set in magic schools, along with every kind of dish imaginable.

And the moment I saw the five people who had arrived ahead of us, only one thought crossed my mind.

*We’re screwed.*

When it came to reading the room, I was second to none. After spending so long scraping by as an F-rank Hunter, always watching everyone’s mood, I could read the room in 0.1 seconds.

Just like now.

*What a wonderful atmosphere.*

The air around the five people was pulled taut.

I had sensed that something was wrong from outside, but the reality was worse than I had expected.

It was fortunate that everyone had come empty-handed because of the occasion. If anyone had been carrying so much as a weapon at their waist, someone would have drawn steel on the spot.

“Well… Since we have guests, shall we end this reunion here?”

The tense atmosphere was dispersed by a man’s delicate voice.

Though was he really a man? His slender build was delicate enough to make him seem like a woman. His face was pale, and his lips were red as though they had been painted with dye.

> **System**
>
> Level 22: Hong Jin

He smiled at me.

“You’re a strikingly handsome young prodigy, just as one would expect from the martial world. I heard a young hero from the Jin Family of Taiyuan was coming today. Might that be you…?”

Now was the time for introductions. I performed a fist-and-palm salute toward the five men.

“My name is Jin Taekyung of the Jin Family of Taiyuan.”

The unpleasant atmosphere immediately eased somewhat. Surprise painted over the traces of displeasure and ridicule lingering on the other four faces.

“If you’re Jin Taekyung of the Jin Family of Taiyuan…”

A huge man dressed in black martial robes muttered.

From the moment I first saw him, he had radiated tough-guy energy. His name was Li Feng, and the number 68 hovered above his head.

*Is he affiliated with the military?*

I couldn’t judge everything from a first meeting, but that was the impression he gave. A proud and upright soldier. That was my first impression of him.

*Li Feng, Li Feng… At Level 68, he’s probably an advanced First Rate?*

Just as I was engraving his name and Level into my mind, the other three men reacted.

“Hm. That’s the Sleeping Dragon of Shanxi?”

“He’s young. No, he’s a child.”

“He doesn’t look particularly as incredible as the rumors claim…”

The gazes fixed on me with apparent curiosity contained surprise, a hint of jealousy, and a subtle sense of superiority.

In situations like this, there was usually no need to ask about the other person’s identity. They were the sort of people desperate to show off.

“Apologies for the late introduction, Junior.”

A sharp-eyed man grinned as he spoke to me. The other two had their arms folded as they looked at me like a cute little chick.

*This is weirdly irritating.*

What kind of people acted like my Seniors right off the bat?

My question was answered soon enough.

“Oh, you don’t know yet, do you? We came from Shaanxi. The Zhongnan Sect of Shaanxi—have you heard of it?”

My mouth fell open before I knew it.

“The Zhongnan Sect? *That* Zhongnan Sect?”

The three men’s faces blossomed with smiles.

“Haha! Look how surprised he is.”

“Exactly.”

“Perhaps you know our sect well?”

I shouted, suddenly brimming with excitement.

“I do! I know it very well! I had so much fun reading about it!”

“We’re glad to hear you know us… Wait. What do you mean, ‘reading about it’?”

“What else? Obviously, *The Reign…*”

I stopped halfway through my answer.

*Ah. This wasn’t a novel.*

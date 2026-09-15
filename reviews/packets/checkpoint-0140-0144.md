# Checkpoint Review — 140–144

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

# Chapters 140–144

## Plot

At the City Lord’s luncheon, Jin Taekyung humiliates Gong Ilhyuk by exposing his tenuous relationship with Zhongnan Sect Leader Gong Iljung. When Ilhyuk attacks Cheongpung, Cheongpung effortlessly destroys his arm with the Taeeul Miri Palm. Revealing that Mae Jonghak, the Sword Saint, taught him the technique, Cheongpung prompts Li Feng to recognize him as his Martial Uncle. Cheongpung then demonstrates the Zaha Divine Technique, confirming his inheritance of Mae Jonghak’s legacy and further humiliating Zhongnan.

Hong Jin dismisses the Zhongnan delegation and abandons their expected partnership, choosing to pursue the Shaanxi–Shanxi trade route through Huashan instead. Li Feng agrees to contact Huashan and act as intermediary. Gong Ilhyuk leaves vowing revenge.

Hong Jin and Li Feng escort Taekyung and Cheongpung through the Provincial Office to meet ten-year-old Prince Shangshan, Zhu Bao. Zhu Bao recognizes Taekyung as the Sleeping Dragon of Shanxi, requests his autograph, and eagerly questions Cheongpung after learning he is Mae Jonghak’s disciple. Taekyung carves an encouraging signature for Zhu Bao, who plans to display it publicly.

The luncheon attendance condition is fulfilled, with the associated quest reward deferred until the luncheon ends. Hong Jin and Li Feng ask the Jin Family of Taiyuan to support an Escort Bureau expanding from Shaanxi toward the Central Plains, offering half the funding and official assistance. Taekyung agrees only to relay the proposal to Jin Wikyung and suggests using the Seongun Escort Bureau as the base.

## Continuity

- Cheongpung is Mae Jonghak’s twenty-year-old grandson and martial heir, a Peak master raised in seclusion. Li Feng formally recognizes him as his Martial Uncle.
- Mae Jonghak remained hidden at a Huashan residence protected by ten formations. Li Feng saw Cheongpung there as a child and left Huashan after being overwhelmed by his talent, not because of his defeat by Gong Ilhyuk.
- Cheongpung knows the Taeeul Miri Palm, Zaha Divine Technique, and several other Huashan techniques. His Extreme Yang internal energy and martial ability vastly exceed his apparent age.
- Cheongpung’s exact parentage and the meaning of Mae Jonghak’s claim that a crane delivered him remain unresolved.
- Hong Jin is Shanxi’s eunuch Deputy Military Commissioner and has served Prince Shangshan since infancy. Li Feng is the Assistant Military Commissioner and commands the Provincial Office’s soldiers.
- The trade and Escort Bureau project has shifted from Zhongnan to Huashan, with Li Feng serving as Hong Jin’s intermediary. Taekyung has not endorsed the proposal; he will present it to Jin Wikyung.
- Gong Ilhyuk leaves humiliated and vengeful. The names and identities of the other two members of the Three Hands of Zhongnan remain unknown.
- Zhu Bao is an exceptionally skilled ten-year-old swordsman who has trained daily for three years. He admires Taekyung and wants to emulate him.
- Taekyung remains below the Peak realm and cannot use Sword Energy, despite defeating the Peak masters Jopil, Jin Baekyang, and Pung Yang.
- Cheongpung wants royal-guard armor because he admires its black appearance and has agreed to call Li Feng Martial Nephew in exchange for royal-guard equipment.
- The full title of the wuxia novel beginning with “The Reign…” remains unknown. The Emperor’s reported suspicion of his younger brother and the political danger surrounding Zhu Bao also remain unresolved.

## Translation Decisions

- Render **태을미리장** as **Taeeul Miri Palm**, **자하신공** as **Zaha Divine Technique**, **태사부** as **Grandmaster**, and **사숙** as **Martial Uncle**.
- Render **풍운검군** as **Wind-and-Cloud Sword Lord** and **오촌 당숙** as **father’s cousin**.
- Render **근위대** as **royal guard** and **근위대 갑옷 세트** as **Royal Guard Armor Set**.
- Use **His Highness** for formal royal address and **king** when Cheongpung uses the literal term.
- Render **주표** as **Zhu Bao**, Prince Shangshan’s personal name.

## Durable state

{
  "active_continuity": [
    "The City Lord's luncheon has concluded its attendance requirement; the associated Quest Reward is pending until the luncheon ends.",
    "Zhu Bao is an earnest young prince and enthusiastic admirer of Jin Taekyung who wants to emulate him and display his autograph at the Shanxi Provincial Office.",
    "Taekyung remains below the Peak realm and cannot use Sword Energy despite defeating Jopil, Jin Baekyang, and Pung Yang.",
    "Hong Jin and Li Feng seek the Jin Family of Taiyuan's support for an Escort Bureau expanding from Shaanxi into the Central Plains, offering half the funding and maximum convenience.",
    "The project shifted from the Zhongnan Sect to Huashan after Hong Jin learned that Mae Jonghak had remained there and raised successors.",
    "Taekyung will relay the proposal to Jin Wikyung without making the decision himself and has suggested using the Seongun Escort Bureau as the base.",
    "Cheongpung is a twenty-year-old Peak master raised by Mae Jonghak, the Sword Saint, and recognized by Li Feng as his Martial Uncle.",
    "Mae Jonghak remained in deep seclusion at a hidden Huashan residence and had been there at least ten years before the luncheon.",
    "Li Feng left Huashan after becoming discouraged by Cheongpung's extraordinary talent, not because of his defeat by Gong Ilhyuk.",
    "Cheongpung knows several Huashan martial arts and can use the Zaha Divine Technique with potent Extreme Yang internal energy.",
    "Cheongpung's exact parentage and the truth behind his claim that a crane delivered him to Mae Jonghak remain unclear.",
    "The identities of the other two members of the Three Hands of Zhongnan remain unknown.",
    "Hong Jin is a eunuch who has served Prince Shangshan since infancy and is the power behind the Shanxi Provincial Office as Deputy Military Commissioner.",
    "Gong Ilhyuk leaves the luncheon humiliated and vows revenge against those who rejected and insulted him.",
    "Taekyung encouraged Cheongpung to insult the Zhongnan disciples, and Cheongpung swore for the first time.",
    "Hong Jin and Li Feng are pursuing the Shaanxi–Shanxi trade project through Huashan, with Li Feng acting as intermediary.",
    "Li Feng commands the military's respect, while Hong Jin holds influence over civil officials and servants through fear.",
    "Cheongpung wants to join the royal guard because he admires its black armor and accepted Li Feng's Martial Nephew address in exchange for royal-guard equipment.",
    "Zhu Bao is ten years old, has trained in martial arts daily for three years, and is an exceptionally skilled young swordsman personally named Zhu Bao."
  ],
  "continuity_sources": [
    143,
    144
  ],
  "open_questions": [
    "What is Cheongpung's exact parentage, and what did Mae Jonghak mean by saying a crane delivered him?",
    "Why did Mae Jonghak remain hidden at Huashan despite the sect eventually finding his residence?",
    "What are the names and individual identities of the other two members of the Three Hands of Zhongnan?",
    "What is the full title of the wuxia novel beginning with 군림…… that Taekyung read through volume thirty-four?",
    "Was the Emperor's reported suspicion of his younger brother the reason Prince Shangshan was sent to Shanxi, and what danger does the imperial succession pose?"
  ],
  "safe_through": 144,
  "temporary_decisions": [
    "Render 전하 as “His Highness” as the formal royal address and 왕 as “king” when used literally.",
    "Render 초일류 as “advanced First Rate” and 군문 as “military” when describing an affiliation.",
    "Render 풍운검군 as “Wind-and-Cloud Sword Lord” and 오촌 당숙 as “father's cousin.”",
    "Render 태을미리장 as “Taeeul Miri Palm.”",
    "Render 후배님 and 선배님 as “Junior” and “Senior” in the Gong Ilhyuk exchange.",
    "Render 태사부 as “Grandmaster” and 사숙 as “Martial Uncle” in the Huashan context.",
    "Render 자하신공 as “Zaha Divine Technique.”",
    "Render 근위대 as “royal guard,” 근위대 갑옷 세트 as “Royal Guard Armor Set,” and 주표 as “Zhu Bao.”"
  ],
  "version": 1
}

## Reading copies

## Chapter artifact 140

# Chapter 140

Gong Ilhyuk of the Three Hands of Zhongnan stared at the young man in front of him with a dubious expression.

*What is this guy?*

Jin Taekyung, the Sleeping Dragon of Shanxi. He was the driving force behind a whirlwind that had quietly spread his name as far as Shaanxi in the span of only a few months.

Gong Ilhyuk mulled over what Jin Taekyung had said.

*“The Reign…” What was it?*

It definitely seemed as though he had been about to say something before stopping himself.

Unlike his enthusiastic reaction when he first heard the name of the Zhongnan Sect, he now looked completely deflated and let out one deep sigh after another.

“Whew.”

“…What’s with the sighing?”

“It’s nothing. Really.”

“What do you mean, nothing? Go on and finish what you were saying.”

Gong Ilhyuk was beginning to feel irritated. What kind of sect was his? It was none other than the famous Zhongnan Sect.

It was one of the great pillars of Murim, a sect that had proudly earned its place among the Nine Sects and One Gang on the strength of centuries of history and deeply rooted martial traditions.

And yet…

*Can’t he at least be grateful that I acknowledged him? Why is he sighing?*

No matter how successful the Jin Family of Taiyuan was, it was still merely a family from the frontier.

Compared to the Zhongnan Sect, one of the Nine Sects and One Gang, it was like a firefly before the sun. In terms of both background and personal fame, Jin Taekyung was a hopelessly insignificant greenhorn.

*What an arrogant bastard.*

Gong Ilhyuk had lived his entire life with pride in being a disciple of the Zhongnan Sect. It was only natural that he felt offended.

The other two men known alongside him as the Three Hands of Zhongnan were also looking at Jin Taekyung with displeasure.

“Ahem.”

“Young friend, you have a habit of stopping halfway when you speak.”

As the atmosphere grew increasingly unpleasant, Jin Taekyung waved his hand.

“No, it’s not like that. I just misunderstood something on my own.”

Gong Ilhyuk opened his mouth, deliberately adopting a generous tone.

“What did you misunderstand? Tell me. I’ll answer everything.”

“It’s really nothing…”

“Ah, just tell me!”

“Why are you shouting?”

Gong Ilhyuk took a deep breath.

He was almost forty years old. Yet here he was, getting worked up over a brat barely twenty.

For some reason, looking at that handsome face made his blood boil.

“It’s not that… Whew. Anyway, tell me.”

“Hmm.”

Jin Taekyung finally opened his mouth, as though he had no choice.

“Then may I ask you one thing?”

“Anything.”

“What is the name of the current chairman of the Zhongnan Sect—or rather, the Sect Leader?”

“Hm? You mean the Sect Leader’s name?”

“Yes.”

What kind of question was that? Gong Ilhyuk answered with a puzzled look.

“Gong Iljung.”

“Ah. Yes.”

Jin Taekyung’s response was so indifferent that it was as though he had no idea who that was.

The veins on the foreheads of all three men began to bulge.

“Have you never heard the Sect Leader’s name?”

Jin Taekyung scratched the back of his head.

“I think I have. Or maybe not…”

“…Then what about the title Wind-and-Cloud Sword Lord?”

“Wind-and-Cloud Sword Lord Gong Iljung. Wind-and-Cloud Sword Lord Gong Iljung… Hmm. I’m not sure.”

It was beyond absurd.

The Sect Leaders and Family Heads of the Nine Sects and One Gang and the Five Great Families were all renowned masters whose names were known throughout the world. No martial artist could possibly be unaware of them.

And yet this fellow, who was supposedly a member of the Jin Family of Taiyuan—not some half-baked martial artist—didn’t know the Sect Leader of the Zhongnan Sect.

He even called him by his given name, as though they were friends.

*Is this bastard making a mockery of the Zhongnan Sect?*

Gong Ilhyuk’s head was spinning from the shock when Jin Taekyung suddenly looked up at him.

“Oh? Now that I think about it, your names are similar. Gong Iljung, Gong Ilhyuk.”

At least he had some basic social awareness. Gong Ilhyuk’s irritation eased slightly.

“He’s a family elder.”

“Oh, a family elder! Then are you two…?”

“He’s my father’s cousin.”

“Your father’s cousin!”

Seeing Jin Taekyung’s eyes widen, Gong Ilhyuk straightened his shoulders.

It wasn’t just anyone. He was the Wind-and-Cloud Sword Lord. Being related to the Sect Leader of the Zhongnan Sect was an immense honor.

“Ahem. Don’t spread it around too much. If this became widely known, people’s attitudes toward me would change.”

In reality, Gong Ilhyuk wanted this fact to become known more than anyone.

He had enjoyed all kinds of benefits by putting the Wind-and-Cloud Sword Lord’s name out front: superior martial arts, elixirs, and even the title of Three Hands of Zhongnan.

If he continued advancing at this rate, it was only a matter of time before he seized an important position within the Zhongnan Sect.

“You understand what I mean, right? If you absolutely have to tell someone, just tell a few close friends…”

Jin Taekyung waved his hand.

“No way. I’d never tell anyone. It would obviously hurt Great Hero Gong’s reputation. People would say, ‘He’s a guy who climbed this high by relying on connections.’ Oops. Sorry. Anyway, that kind of rumor would be troublesome, wouldn’t it?”

Gong Ilhyuk gave a dry cough. Even he had to admit that the boy wasn’t entirely wrong.

“Ahem. It’s not as though it would hurt me that much. I only meant that there might be people who are curious about me…”

“People curious about you? I don’t have a single friend, so there’s no one I could tell.”

“…Your eldest brother, the Lesser Family Head of the Jin Family, might be curious. Or Young Hero Heaven Shaking Sword.”

“Oh, you don’t know much about my family situation. My eldest brother is incredibly busy right now. My second brother isn’t interested in much besides martial arts.”

“…Really?”

“Yes.”

There was nothing more to say after that.

As Gong Ilhyuk continued giving irritated coughs, Jin Taekyung smiled brightly.

“And what good would it do to tell anyone? If he’s only your father’s cousin, you’re practically strangers. I thought you two were father and son or something.”

“……!”

* * *

There was nothing more exhilarating than screwing someone over while smiling.

Especially when it was someone who acted arrogant. If I managed to get one over on them properly, the rush doubled.

*Ah. I think I could get addicted to this.*

Were they called the Three Hands of Zhongnan?

I hadn’t liked them from the moment I met them. Not their gazes, which seemed to look down on everyone, nor their swaggering attitude as members of a great sect.

*So it really is different from the novel.*

When I was in high school, becoming a disciple of the Zhongnan Sect had been one of my dreams.

As expected, reality was a cesspool.

I held back my laughter as I watched Gong Ilhyuk trembling with rage.

*What a cute bastard. He’s so much fun to tease.*

I wanted to keep going, but this was probably enough. If the Jin Family of Taiyuan was a local player, these people were national-level.

There was nothing to gain from picking a fight with them.

Fortunately, a voice suddenly cut in and lightened the atmosphere.

“Aren’t you gentlemen monopolizing the conversation a little? The other guests must be lonely. You haven’t even finished introducing yourselves.”

I got goose bumps once at the nasal, lilting voice.

Then I got them a second time when the pretty middle-aged man looked at me and winked.

“I haven’t introduced myself yet, have I? I’m Hong Jin, the Deputy Military Commissioner of Shanxi Province.”

“Deputy Military Commissioner… what?”

“The Deputy Military Commissioner. Ah, you’re a martial artist, so I suppose this is your first time hearing of the office?”

“Yes.”

*I’d heard of “Comrade Chairman,” but “Comrade Deputy Military Commissioner” was a new one.*

Hong Jin giggled as he looked at me blinking.

Good heavens. A middle-aged man was giggling.

“Why that expression? Did something bad happen?”

“…No. I’m just so happy.”

“Happy? Ho ho ho, you’re adorable. Don’t you agree, Assistant Commissioner Li?”

*He called me cute. Fuck, that bastard called me cute.*

I was barely holding back my nausea when the man I had seen only briefly earlier greeted me in a blunt voice.

“I am Li Feng, Assistant Military Commissioner of Shanxi Province. I oversee the training of the soldiers under the Shanxi Provincial Office.”

“And he’s my direct subordinate. Isn’t that right, Assistant Commissioner Li?”

Li Feng’s thick eyebrow twitched.

We had known each other for less than five minutes, but I already knew one thing.

Li Feng hated Hong Jin.

That alone made him someone worth treating with courtesy. I performed a fist-and-palm salute.

“My name is Jin Taekyung of the Jin Family of Taiyuan.”

“I have heard your reputation. A great new star has risen over the Shanxi martial world.”

“A new star? You flatter me.”

Li Feng shook his head with a serious expression.

“No. Rumors are often exaggerated, but after seeing Young Hero Jin today, I can tell they were all true.”

Kind words deserved kind words in return.

I brought up the soldiers I had seen on the way here.

“I was surprised by how skilled the soldiers were. I wondered who had trained them, but I suppose it was only natural that it would be you.”

I gave him a firm thumbs-up, and a smile flickered across Li Feng’s lips.

It had been so long since I’d had a normal, pleasant conversation that I was almost moved.

“If it isn’t discourteous, could you introduce the other guests as well?”

“Of course. This is…”

“Greetings! To the respected Seniors of Murim and those who toil day and night for the sake of the nation…”

“……”

What was this, an interview at a conglomerate?

The young prodigies of the Five Gates of Shanxi, who had been waiting for an opportunity, rushed to give exaggerated introductions and shower everyone with flattery.

That left only one person.

“All right. Junior, where are you from, and who are you?”

At Gong Ilhyuk’s question, delivered with all the smugness of someone high on his seniority, Cheongpung blinked.

“Me?”

“Who else would I mean?”

“One, two, three, four… There are lots of people besides me.”

The veins on Gong Ilhyuk’s forehead bulged.

“Not that! You’re the only one who hasn’t introduced himself!”

“Oh, I see. You called me a junior, so I didn’t think you meant me.”

“Good heavens! In Murim, we’re all fellow practitioners! We’re all seniors and juniors to one another. How do you not know that?”

If it were me, I would have responded with heavy sarcasm.

But Cheongpung was Cheongpung.

He was in a different class from ordinary people.

“Wow, this is my first time being a junior! I look forward to working with you!”

“…What kind of person is this?”

Sometimes, a pure child was much harder to deal with than an adult who had been properly tainted by the world.

Cheongpung spoke with a bright smile.

“My name is Cheongpung, and I live in Shanxi.”

Gong Ilhyuk had been left speechless, but he finally came to his senses and stammered out a question.

“Ahem. Then you must also be one of the young prodigies of the Five Gates of Shanxi.”

“Hm? No.”

“You’re not?”

“No. I came from Henan.”

“You just said you were from Shanxi.”

“I live in Shanxi, so I’m from Shanxi. Hehe.”

“Then… whew.”

A furrow appeared in Gong Ilhyuk’s forehead.

He clearly wanted to throw a punch right then and there, but the occasion forced him to hold himself back.

“All right, then. Which sect in Henan are you from? The Iron Blood Sect? The Five Tigers Sword Sect?”

“Where are those?”

“You’re from Henan, but you don’t know the Iron Blood Sect or the Five Tigers Sword Sect? Does that make any sense? Hm? Then are you from Shaolin?”

“Oh, I stayed in Henan for about half a month before moving to Shanxi, so I don’t know much about it.”

“You said you were from Henan?”

“It’s true that I came from Henan, but before that I was in Shaanxi…”

“You little bastard! Then just say the whole world is your hometown!”

At last, Gong Ilhyuk exploded. He shouted as he grabbed Cheongpung by the collar—or tried to.

Snag.

His wrist was caught with absurd ease.

Gong Ilhyuk let out a hollow laugh.

“Well, look at you. You know at least one trick, huh?”

“Ah, I just reacted on instinct. I’m sorry, Senior.”

“On instinct? And you’re apologizing?”

Seeing Cheongpung apologize with a miserable expression, Gong Ilhyuk gave a short laugh.

“Never mind. You don’t have to let go. There’s no need to apologize, either.”

“Really?”

“Yes. But you’ll pay dearly for your reckless bravado.”

“What? What does that mean?”

“You’ll find out soon enough.”

I stepped in at that exact moment.

I threw myself in front of Cheongpung, and Gong Ilhyuk looked at me with dry eyes.

“Move aside, Junior.”

“Pardon me, Senior.”

“Pardon you… Should I take this to mean the Jin Family of Taiyuan intends to oppose the actions of our sect?”

I answered calmly.

“Not at all. I only want to prevent this from becoming a bigger problem.”

“A problem? What problem?”

“His Highness will be arriving soon, won’t he? And there are plenty of eyes on us.”

“Plenty of eyes. Deputy Military Commissioner, what do you think?”

I could see Hong Jin smiling behind Gong Ilhyuk.

His delicate voice followed.

“Well, I don’t think it will be much of a problem.”

Li Feng immediately objected.

“This is the grand hall. We cannot tolerate even a minor disturbance.”

“Assistant Commissioner Li, I find the word ‘tolerate’ unpleasant. Anyone listening might think you were my superior.”

“Deputy Military Commissioner!”

“Why, Assistant Military Commissioner?”

The instant Hong Jin finished speaking, the other two members of the Three Hands of Zhongnan quietly stepped in front of Li Feng.

As befitted members of the Zhongnan Sect, both were at least advanced First Rate masters.

Li Feng bit down hard on his lip, then muttered to me,

“I’m sorry.”

Gong Ilhyuk smiled triumphantly.

“Well? What are you going to do now?”

What was I supposed to do?

I shrugged once and stepped back. Gong Ilhyuk’s smile deepened.

“A wise choice.”

“I only wanted to prevent the problem from getting bigger. You understand, right?”

“Of course. Everyone here will remember it clearly.”

“I hope so.”

Cheongpung stared blankly at me.

“Benefactor, did I do something wrong?”

Gong Ilhyuk was faster than I was with his response.

“What? Wrong?”

His gaze turned murderous as he glared at Cheongpung.

“Are you insulting me and the Zhongnan Sect right now?”

“That’s not it. I was just…”

“Can’t you shut that mouth of yours?”

A complicated, subtle expression appeared on Cheongpung’s face.

Then he said the one thing more than enough to make Gong Ilhyuk lose his reason.

“Wow, this is the first time anyone’s ever sworn at me. How fascinating.”

“You goddamn bastard…!”

Whoosh!

A heavy sound split the air.

Gong Ilhyuk’s fist shot toward Cheongpung’s ribs at blinding speed.

Then—

Crack. Crunch.

“……!”

“……!”

Amid the silent shock, one man opened his mouth wide in pain.

His fist had been crushed. Bone jutted through the torn flesh of his forearm, and blood covered Gong Ilhyuk as he asked in a trembling voice,

“Wh-what is this? What kind of fist technique…?”

If he hadn’t asked, I would have asked the same thing.

I had expected this result, but not to this extent.

With a single counter, Cheongpung had rendered Gong Ilhyuk, a Level 70-plus master, completely helpless.

And then…

“It wasn’t a fist technique.”

At my mutter, Cheongpung answered with a face that looked ready to vomit.

“Benefactor is right. It wasn’t a fist technique. It was a palm technique called the Taeeul Miri Palm. But Senior, you’re bleeding too much. The smell of blood is making my stomach churn. Urk!”

What a lunatic.

I gave a hollow laugh as Cheongpung flung Gong Ilhyuk aside and began dry heaving.

That was when—

“Ta-Taeeul Miri Palm!”

Li Feng asked with his eyes wide.

“Did you just say Taeeul Miri Palm? Are you certain?”

“Urk, yes. My grandfather taught me.”

“M-May I ask his name?”

“Mae Jonghak, urk—urgh!”

Splash!

I was shocked that Cheongpung had vomited in the very place where the king was about to arrive, but Li Feng seemed unfazed.

He trembled as though he had been struck by lightning, then squeezed out a single word.

“Sword Saint…”
## Chapter artifact 141

# Chapter 141

I recalled something Jin Mukyung had told me a few days ago.

*One God, Three Saints, Ten Kings.*

Great martial artists who had already become legends.

Going by that order, Sword Saint Mae Jonghak had to be one of the top five Supreme Peak masters in the world.

*Now even the Sword Saint is showing up.*

Jin Mukyung had told me that the Fire King earned his place among the Ten Kings by hunting down and killing a thousand members of the Demonic Cult over four days and nights.

If that was what it took to earn a place among the Ten Kings, just how formidable was the Sword Saint, whose name ranked ahead of his?

*Why do nothing but monsters keep popping up?*

I was dumbfounded, but then I looked at Cheongpung and found myself nodding.

Beans grow where beans are planted. A monster had raised a monster.

*There’s no way a gifted freak like that could appear out of nowhere.*

Cheongpung was unquestionably a Peak master.

He was only twenty years old. If he had grown up under the guidance of a phenomenal master like the Sword Saint, it made perfect sense.

“Urk, uweeek!”

…Actually, it was starting to make less sense. How had someone like that become a Peak master?

I asked Cheongpung, who continued retching.

“Are you all right?”

“I’m all right, urk!”

“You’re clearly not all right.”

“More importantly, Senior looks badly hurt, ugh!”

“Don’t call me Senior. I’m fine. A little spit and this much will heal right up.”

“Really?”

Of course not.

I patted Cheongpung on the back and glanced around. Everyone except Hong Jin was staring at us with wide eyes.

“S-Sword Saint Mae Jonghak? The Sword Saint I know?”

“That idiot is the Sword Saint’s grandson?”

“What on earth is going on…?”

Gong Ilhyuk’s reaction stood out more than anyone else’s. He had apparently forgotten his pain and was staring blankly at Cheongpung before suddenly shouting.

“Nonsense! The Sword Saint has been in seclusion for more than thirty years! How dare a piece of trash like you claim to be the Sword Saint’s heir?”

“Excuse me for interrupting.”

I scratched my chin and continued.

“Why don’t you stop the bleeding first? You’re losing a lot of blood.”

“……”

Gong Ilhyuk’s face turned bright red. He had to be embarrassed. His arm had been shattered with a single blow, yet he was still calling someone else a piece of trash.

“Tch. If only I hadn’t let my guard down…”

“Then shall we arrange a rematch once you’ve recovered? I can lend you my family’s training hall.”

Even if they fought a hundred times, Gong Ilhyuk would lose all hundred. The difference between the two of them was that obvious.

The proof was that, now that I had actually offered him the chance, Gong Ilhyuk went silent as though he had swallowed honey.

“Stop the bleeding first. Stop the bleeding.”

“……You bastard.”

Gong Ilhyuk glared at me with murderous eyes.

It seemed he had finally realized that I disliked him, but I didn’t feel particularly threatened.

*You should’ve stopped when I told you to.*

If word of what happened today got out, they were the ones who would suffer. They had gotten entangled with the Sword Saint’s grandson, and even the Sect Leader of the Zhongnan Sect—Gong Ilhyuk’s father’s cousin—wouldn’t be happy about that.

Meanwhile, I wasn’t even directly involved. I had also gained an unexpected golden connection.

*Listen here, I gave the Sword Saint’s grandson candied hawthorn skewers[^1], took him to the hot springs, and did it all, okay? You bastard.*

So this was how the candied-hawthorn stock took off.

I was smiling inwardly when Gong Ilhyuk finished stopping the bleeding and sneered.

“Come to think of it, this is ridiculous. As far as I know, the Sword Saint had no children. How could he possibly have a grown grandson?”

Cheongpung, who had just stopped retching, tilted his head.

“That’s not true. I really am his grandson.”

“The entire world knows that the Sword Saint devoted his entire life to martial arts! You’re obviously lying!”

“No, I’m really not.”

Cheongpung continued with a miserable expression.

“I really am my grandfather’s grandson. A crane brought me to him twenty years ago.”

“……?”

“……?”

*What the fuck was that supposed to mean now?*

As everyone’s attention turned toward him, Cheongpung looked back at me with a confused expression.

“Benefactor, am I mistaken?”

“What exactly do you know?”

“About cranes bringing babies. Grandfather told me that babies are chosen by Heaven, and when the time comes, a crane delivers them.”

“Who told you that?”

“My grandfather.”

“Oh.”

The story practically wrote itself. Their surnames were different, so the Sword Saint had obviously adopted him from somewhere…

Cheongpung had grown up alone with his grandfather in the mountains from an age he couldn’t even remember.

Whatever his grandfather told him, he must have simply accepted it.

“Cranes don’t bring babies? Then am I not my grandfather’s grandson?”

“Well, that’s…”

I continued with a heavy heart. Cheongpung was twenty years old, and now that he had come down from the mountains, it was time for him to learn about the world one thing at a time.

“There are three stages involved in having a child: ovulation, fertilization, and implantation. Try it.”

“With Benefactor?”

“Why would you do it with me? Are you insane? I said to repeat the words out loud.”

“Yes. Ovulation, fertilization, implantation…”

However, the sex education I had begun so ambitiously had to end the moment it started.

“You bloody little bastards! How dare you behave like this in front of a great Senior of Murim!”

The owner of that growling voice was, of course, Gong Ilhyuk.

With help from the other two men officially known as the Three Hands of Zhongnan—but more accurately described as his lackeys—he had even had a splint attached. Now he glared at us.

“A frontier bumpkin and a fool who acts tough because he trusts only his strength dare look down on a disciple of the great Zhongnan Sect?”

Cheongpung’s eyes went round.

“Am I the fool?”

“Probably.”

“Then Benefactor is the frontier bumpkin?”

“Thank you very much for telling me.”

I let out a deep sigh. This man was old enough to know better, yet he still seemed unable to understand the situation. Was his background as a member of the Zhongnan Sect, and his faith in his father’s cousin, simply too strong?

“Well, our Senior sure has a loose mouth.”

“What did you say?”

“Never mind me. What are you going to do if what this friend said is true?”

“If it were true, there’s no way Li Feng wouldn’t have recognized him.”

Li Feng? Why was Li Feng being mentioned here?

I looked at Li Feng, puzzled. He had gone rigid as though he had seen a ghost, but now he finally parted his lips.

“I am a lay disciple of Huashan. Until ten years ago, I was at the main sect.”

Gong Ilhyuk added with a mocking grin,

“That fellow was quite prominent among the lay disciples. At least, until he lost to me during a friendly duel with our sect. Isn’t that right?”

“That’s correct. I stayed at the Zhongnan Sect for two days for the duel, but I ate something bad and became seriously ill.”

“That story again. Don’t you ever get tired of it?”

“Isn’t it a strange coincidence, no matter how often I think about it? Everyone who was scheduled to duel with you, myself included, suffered the same fate.”

“……So you still can’t accept your defeat?”

“No. I accepted it a long time ago. In fact, thanks to you, I learned what Murim was like. As tuition, it was a cheap lesson.”

Gong Ilhyuk’s eyebrow twitched at Li Feng’s calm tone.

“Enough pretending to be magnanimous. Answer me honestly. Have you ever seen that fool at Huashan?”

“Before that, let me ask you one thing. Do you still think I left Huashan because of you?”

“Of course. You ran out of Huashan less than two months after our duel. What excuse are you going to make now?”

“It’s true that I was discouraged for a while… but you’re wrong.”

Li Feng shook his head and continued slowly.

“It had been about a month since that day. My Master suddenly told me that there was somewhere we had to go. When we arrived, all the leaders of our sect, including the Sect Leader, were gathered there.”

“Did they hold a consolation banquet for a lay disciple? Huashan is more generous than I thought.”

“It is a generous sect. After all, they let a failure like me join them on an important visit to see our Grandmaster.”

Gong Ilhyuk’s eyes narrowed.

“Your Grandmaster? Could it be…?”

“There is only one Grandmaster in our sect. Sword Saint Mae Jonghak. The one everyone knows.”

Gasps rose from several places around the hall. Meanwhile, growing unease spread across Gong Ilhyuk’s face.

“That’s impossible. I heard the Sword Saint hadn’t shown himself in a long time…”

“It’s true. However, he was still living at Huashan. He had simply gone into such deep seclusion that we hadn’t been able to find him.”

“Th-Then what happened?”

“We combed through Huashan from top to bottom. We had to break through ten formations before we could reach his residence. Can you guess what I saw there?”

Everyone present could guess. Li Feng’s gaze was fixed on Cheongpung’s face.

“A cute little boy. He was much smaller than the other children his age, but he was diligently swinging a sword… No one could laugh. Who could laugh after seeing a monster perform the Plum Blossom Sword Technique at the age of ten?”

“……!”

“……!”

Silent shock spread through the crowd. Gong Ilhyuk stammered.

“That—that’s impossible. As far as I know, one must be at least First Rate to perform the Plum Blossom Sword Technique…”

“Unimaginable things sometimes happen in Murim. Compared to that, pulling dirty tricks in a friendly duel is nothing.”

Li Feng gave a self-deprecating laugh.

“After more than a month of facing the wall in training, I came to a realization. I had no reason to remain there. That was why I left Huashan. What do you think? Isn’t it interesting?”

The story Li Feng told had a powerful impact. Everyone, myself included, stared silently at Cheongpung.

Suddenly, I remembered the conversation I had shared with him at Honghwa Inn the night before.

*“I was ten years old. One day, dozens of people came barging in and made a scene. I remember my grandfather shouting at them to get the hell out before he set fire to the mountain.”*

*“Ah. So that’s why he keeps changing where he lives…?”*

*“Yes. Fortunately, the mountain is so large that he’s managed to avoid them for ten years.”*

Until then, I hadn’t known that the people who had come to cause trouble ten years ago were the leaders of Huashan, or that the Sword Saint Mae Jonghak was Cheongpung’s grandfather.

And the part about them making a scene was only how it had appeared from young Cheongpung’s perspective. The reality had probably been very different.

*Who would cause trouble with the Sword Saint? That’s a perfect way to get yourself killed.*

The Sword Saint who had threatened to set fire to his own sect wasn’t exactly ordinary, either.

In any case, on the day Huashan had nearly become a real volcano, Li Feng had met Cheongpung as a child and clearly despaired after witnessing his talent.

*Fair enough. First Rate at the age of ten.*

There were countless people who couldn’t reach First Rate even after turning twenty.

Two of the rising martial artists from the Five Gates of Shanxi present here still weren’t quite good enough to be called First Rate masters.

And yet Cheongpung had reached that realm at the age of ten.

*Could Jin Mukyung have done the same?*

The moment that question occurred to me, Gong Ilhyuk shouted as though suffering a fit.

“Proof! What proof is there that he’s that child?”

The rising martial artists of the Five Gates of Shanxi who had been trying desperately to curry favor, Hong Jin, who had been watching with great interest, and even the other two members of the Three Hands of Zhongnan all frowned as though they had planned it together.

“There’s no proof. All I have is my memory.”

“Exactly. Mountains and rivers change in ten years. Should I really trust your paltry memory?”

“No. To be honest, I’m not certain either. I don’t know how that child grew up.”

Li Feng answered calmly, then suddenly drew his sword.

*Shing.*

He studied the blade, which radiated a cold chill, and asked Cheongpung,

“Young Hero. How much do you know about Huashan’s martial arts?”

Cheongpung answered with a bewildered expression.

“Uh, I’m not from Huashan.”

“You’re not from Huashan…”

“Yes. My grandfather just taught me various things, saying they would be good to learn.”

“Then allow me to ask you something. Of the Six Harmonies Sword, Plum Blossom Sword Technique, Supreme Clarity Sword, Taeeul Miri Palm, Falling Flower Chasing Shadow Palm, and Scattering Flowers Shadowless Hand… how many do you know?”

“All of them.”

“Heh. All of them. Every one.”

Li Feng gave a hollow laugh and handed the sword he was holding to Cheongpung.

“Could you perform the Plum Blossom Sword Technique?”

“My grandfather told me not to show my martial arts to anyone.”

“One form—or rather, a single sword stroke—will be enough.”

After hesitating for a moment, Cheongpung took hold of the hilt.

“Then I’ll show you briefly.”

The instant he finished speaking, something changed.

*Sssssss.*

*Sword Energy? No.*

From Cheongpung’s head to his toes, tangible strands of purple qi flowed from his entire body.

It was Extreme Yang internal energy so potent that merely being near it scorched the breath in one’s lungs.

“Zaha Divine Technique[^2]…!”

Li Feng let out a cry of delight.

At that moment—

*Whoosh!*

The tip of Cheongpung’s sword traced a beautiful arc.

Like plum blossoms falling at the end of the season, a single streak of Sword Energy cleaved the enormous table in half.

The food, the dishes, even the sturdy table.

“Ah…”

A gasp escaped me before I knew it.

Breaking things was easy. But Cheongpung’s Sword Energy was so sharp and clean that, if the table hadn’t collapsed a moment later, no one would have noticed it had been cut.

*Boom! Crash!*

As the table split in two and collapsed, Li Feng clasped his fist and palm in an exceedingly respectful salute.

“Li Feng, lay disciple of Huashan, pays his respects to Martial Uncle Cheongpung.”

[^1]: Candied hawthorn skewers are fruit skewers coated in hardened sugar.

[^2]: A Huashan internal-energy technique.
## Chapter artifact 142

# Chapter 142

“Li Feng, lay disciple of Huashan, pays his respects to Martial Uncle Cheongpung.”

Zaha Divine Technique. Plum Blossom Sword Technique. And finally, the last word to come from Li Feng’s mouth:

*Martial Uncle.*

Gong Ilhyuk’s face darkened at this unbelievable turn of events.

*Then is that bastard really…?*

Even if Cheongpung wasn’t the Sword Saint’s biological grandson, one thing was certain.

That idiot who kept bowing at the waist with a bewildered expression had inherited everything from Mae Jonghak, the Sword Saint.

“This, this can’t be. It’s impossible. This makes no sense…”

As Gong Ilhyuk stammered and denied reality, a lilting voice reached his ears.

“Great Hero Gong.”

“Ah, Deputy Military Commissioner.”

Gong Ilhyuk’s expression brightened when he spotted Hong Jin.

The Zhongnan Sect had been pursuing various ventures through its connections with the government, and Hong Jin was one of the powerful men of Shanxi Province whom they had come to know in the process.

He was also the only person who could possibly extend a hand of salvation to Gong Ilhyuk in this predicament.

“What happened?”

Hong Jin’s gentle voice put Gong Ilhyuk at ease.

“I must have been mistaken for a moment.”

“Mistaken? About what?”

“I merely thought he was some fraud going around trading on the Sword Saint’s name…”

“Well, I’m no expert in martial arts, but he doesn’t look like a fraud to me.”

“There, there was only a slight misunderstanding.”

“A misunderstanding…”

Hong Jin murmured the word quietly, then stared directly at Gong Ilhyuk.

“Great Hero Gong.”

“Yes, Deputy Military Commissioner.”

“Do you know why I invited you and the others from the Zhongnan Sect here?”

“Yes. Of course I do.”

There were two reasons.

First, to become acquainted with Prince Shangshan, the City Lord of Shanxi and a member of the imperial family, and receive his approval for their new business venture.

Second, to put Hong Jin’s political rival, Li Feng, firmly in his place.

“But as you know, I’ve been rather busy lately. I was so distracted that I forgot to tell His Highness that some other guests would be arriving.”

“I see.”

The nasal quality had vanished from Hong Jin’s voice, leaving it completely dry. Gong Ilhyuk asked anxiously,

“But why are you suddenly bringing that up…?”

“I’d like you to leave for today.”

“What?”

“Wouldn’t the presence of uninvited guests make His Highness uncomfortable?”

It was an unmistakable order to leave. And on top of that, Hong Jin had called them uninvited guests.

Gong Ilhyuk protested.

“Uninvited guests? Deputy Military Commissioner, what exactly do you mean?”

“Oh my, do I have to say it twice? I mean exactly what I said before. I failed to mention your arrival to His Highness.”

Hong Jin was a eunuch. He had remained at Prince Shangshan’s side since the prince was an infant, and thanks to that, he had risen to the post of Deputy Military Commissioner, becoming the power behind the Shanxi Provincial Office and the second-ranking figure in the military.

The young prince favored him above all others. And yet he was sending guests away simply because he had failed to inform His Highness in advance?

“I, I’m not sure I understand what you’re saying, Deputy Military Commissioner…”

Hong Jin smiled sweetly at the flustered Gong Ilhyuk.

“Great Hero Gong.”

“Yes?”

“I didn’t think you were like this, but you’re a little slow, aren’t you?”

“…What?”

“Or are you just bad at reading the room?”

The sudden verbal abuse plunged the hall into silence.

Gong Ilhyuk and the other two members of the Three Hands of Zhongnan trembled as they clenched their fists.

“Your words are excessive.”

“Oh my, if that’s how you feel, then you’ve understood my intentions perfectly. I’ll admit I deliberately went a little too far.”

“Deputy Military Commissioner!”

“Lower your voice. This is the grand hall.”

“Why are you suddenly acting like this? Are you disappointed in me because of what just happened?”

“I said lower your voice. And I’m not disappointed in you, Great Hero Gong. We aren’t friends, after all. We’re not close enough to expect anything from each other or feel disappointed.”

“How could you say that? Have you forgotten your agreement with our Zhongnan Sect?”

“Agreement? Oh, you mean the one about opening a route into Shanxi Province?”

Hong Jin gave a quiet laugh and continued.

“That’s how business works. Until a deal is finalized, it can fall apart at any moment. Surely you didn’t think a few words meant everything was settled when His Highness hasn’t even given his approval yet?”

Gong Ilhyuk barely managed to suppress his rising anger.

He had already boasted to his sect as though the deal were complete.

If the venture succeeded, he would receive a suitable reward. But if it failed, he would be unable to escape a harsh reprimand. For now, he had no choice but to coax the eunuch standing before him.

“If this deal succeeds, wouldn’t it benefit you as well, Deputy Military Commissioner? The Zhongnan Sect never forgets gratitude or grudges.”

The mention of grudges alongside gratitude was an indirect threat.

It was a warning that Hong Jin risked making an enemy of one of the Nine Sects and One Gang.

Hong Jin had spent his childhood and youth as an inner palace official, watching every kind of political struggle. There was no way he could fail to understand the hidden meaning in Gong Ilhyuk’s words.

*Hmph. This is why martial artists are so hopeless.*

Hong Jin clicked his tongue inwardly.

Every one of Gong Ilhyuk’s words and actions was clumsy and blatant.

Compared to a half-polished man like Gong Ilhyuk, Li Feng—quiet, stubborn, and martial artist to the bone—was a far more troublesome opponent.

*He doesn’t even realize who holds the upper hand right now.*

If he had a goal he wanted to achieve, he should have been crawling on the ground to get it. And yet he had added a threat on top of everything else.

That helped Hong Jin make up his mind.

“Great Hero Gong. I’m a delicate person, you see. Hearing words like that frightens me too much to continue working together.”

“Ah, if there was any room for misunderstanding…”

Gong Ilhyuk was about to apologize as though he had no idea what Hong Jin meant when Jin Taekyung, who had been watching the two men with a bored expression, casually tossed out a remark.

“Room for misunderstanding, my ass. A dog passing by wouldn’t believe that.”

“You, you…!”

“Hey, Seniors from the Zhongnan Sect. I don’t know what kind of incredible business you’re running, but couldn’t you discuss it somewhere else later? I’m already miserable enough seeing the entire meal overturned.”

Hong Jin let out a quiet laugh at the sight of Taekyung licking his lips while looking at the food scattered across the floor.

“Don’t worry. Once these gentlemen leave, I’ll have new food brought in. Isn’t that right?”

The situation had now progressed to Hong Jin practically pushing them out the door.

Gong Ilhyuk gritted his teeth.

“Deputy Military Commissioner. I admit my judgment is terrible. But please think carefully about what you will gain and lose from what happened today.”

“You seem to be mistaken. I made this decision after thoroughly weighing the practical benefits.”

“What does that mean?”

“We’ll continue with the project. We’ll build a dedicated trade route and trading post connecting Shaanxi and Shanxi, and we’ll expand the scale as well.”

“Then all the more reason you should join hands with our sect!”

Hong Jin’s eyes widened at the desperate shout.

“Is the Zhongnan Sect the only sect in Shaanxi? As far as I know, there’s a place far older than the Zhongnan Sect—and one with a much better reputation among the public.”

“……Are you talking about Huashan?”

Gong Ilhyuk’s face twisted.

Huashan and the Zhongnan Sect had been bitter rivals, constantly at odds, for the past several hundred years.

If this project went to Huashan instead of some other sect, Gong Ilhyuk knew he would face far more than a light reprimand.

“How could you do this to me?”

“Of course I can. There’s a better option right in front of me.”

“Our sect is by no means inferior to Huashan. In fact, in the current generation, I can proudly say that we’ve surpassed Huashan.”

“‘I can proudly say.’ It’s good to see such loyalty to one’s sect. But from my perspective, wouldn’t the phrase ‘acknowledged by all’ sound better?”

Hong Jin continued without hesitation.

“Great Hero Gong, let me ask you directly. Does the Zhongnan Sect have a master like the Sword Saint?”

“……That is…”

“Then what about a young prodigy as outstanding as that young hero over there?”

“……”

None of the Three Hands of Zhongnan, Gong Ilhyuk included, could easily answer.

The Sword Saint?

The Zhongnan Sect’s Sect Leader, the Wind-and-Cloud Sword Lord, was occasionally compared to the Ten Kings, but that was as far as it went.

As for a monster like Cheongpung, no one had ever heard or seen anything like him.

Gong Ilhyuk, who had been the one to attack first and still ended up on his knees in a single exchange, flushed red.

“B-but the number of Peak masters belonging to our sect is by no means inferior to Huashan’s.”

“I’ve heard that the strength of a Murim sect doesn’t depend on how many masters it has, but on what kind of masters it possesses.”

Hong Jin’s single remark struck the bull’s-eye, and Gong Ilhyuk was momentarily rendered speechless.

But no matter what it took, he had to prevent the position from being handed to Huashan.

“Also, everything we’ve done in cooperation with the government has been completed successfully. Huashan, on the other hand, has never attempted anything like this. They’re inexperienced. Mistakes are inevitable.”

“Oh my, is that so?”

Hong Jin smiled and turned toward someone.

“Assistant Commissioner Li, what do you think?”

Li Feng, who had been silently observing everything, answered.

“That is true. Huashan does tend to draw a firm line between the government and Murim.”

Hong Jin frowned, and color returned to Gong Ilhyuk’s face.

But Li Feng’s heavy voice continued.

“However, doesn’t everyone have a first time?”

“Li Feng, you bastard!”

Hong Jin burst into laughter.

“Our Assistant Commissioner Li has improved so much.”

“Thanks to you.”

The two men had exchanged almost exactly the same words only a quarter of an hour earlier, but the atmosphere was now the exact opposite.

They continued their conversation in a warm and friendly atmosphere.

“I’d like you to act as our intermediary, Assistant Commissioner Li. What do you think?”

“Of course. I’ll send a messenger pigeon to my Master. The Sect Leader will be pleased to hear this news as well.”

“Ah, and you should also tell him that we have a precious guest here.”

Li Feng followed Hong Jin’s meaningful glance and smiled faintly.

“That is news our Grandmaster will be pleased to hear.”

“It’s a good start.”

“I think so too.”

Gong Ilhyuk, who had been completely excluded from the conversation, trembled from head to toe.

The situation had gone too far to turn back now.

He swept his furious, betrayed gaze across the room.

“How dare you ignore the mighty Zhongnan Sect.”

“Hey, there’s something I’ve been meaning to say.”

The voice belonged to Jin Taekyung, who had suddenly cut into the conversation. He gave a quiet laugh and continued.

“It’s not the Zhongnan Sect we ignored. It’s you. You might not know this, but I really like the Zhongnan Sect. *The Reign…* Anyway, I kept up with it all the way through volume thirty-four.”

“What kind of bullshit are you talking about? The Jin Family of Taiyuan is a family without even a proper pedigree! This is no place for the likes of you to butt in!”

Taekyung put on a wounded expression and poked Cheongpung in the side.

“Young Master Cheongpung. That old man says our family doesn’t even have a family tree.”

“What? He said that to my Benefactor?”

“Yeah. I know he’s a Senior, but isn’t that going too far? I’m too scared of the Nine Sects and One Gang to answer him myself. Could you say something for me?”

“M-me? I’m not very good at things like that.”

“Am I not your Benefactor? Was I only a Benefactor in name?”

“No, of course not.”

“Then say what I tell you.”

After Taekyung whispered something to him, Cheongpung opened his mouth hesitantly.

“G-get, get…”

“Young Master Cheongpung, louder! You can do it!”

Encouraged by Taekyung, Cheongpung squeezed his eyes shut and shouted,

“Get lost, you boomer bastards!”

“……!”

“……!”

*Boomer?* They didn’t know exactly what it meant, but that wasn’t important. It had been followed by the word *bastards*.

“You goddamn bastards…!”

All three men, Gong Ilhyuk included, glared with their eyes wide open.

Who were they?

They were main disciples of the Zhongnan Sect’s headquarters. They were accustomed to the admiring gazes of others, and this was an insult they could never wash away.

But…

Gong Ilhyuk ground his teeth. “Let’s go!”

Gong Ilhyuk turned away, swallowing his outrage.

This was neither the right place nor the right opponent for him to repay this humiliation.

*I’ll make them pay for this someday. I swear it!*

Blood dripped from the fist he clenched so tightly that his knuckles creaked.

He stormed out of the grand hall, his footsteps heavy and violent.

Behind him came the voices of Jin Taekyung and Cheongpung.

“Wow, you’re good at swearing. Was that your first time too?”

“Yes! It was my first time ever!”

“For a first attempt, you’ve got some real talent. You should learn a lot from me from now on. As you go through life, there are plenty of times you’ll need to use them even if you don’t want to.”

“Yes!”
## Chapter artifact 143

# Chapter 143

After the Three Hands of Zhongnan left in disgrace, their footsteps echoing heavily, Hong Jin pulled a small bell from inside his robes and shook it.

“Well, now that the uninvited guests are gone, I suppose we should clean up.”

*Ding. Ding. Ding.*

Exactly three times. Before the sound had even faded, the iron doors opened and dozens of servants entered, bowing at the waist.

“Clean the grand hall and bring out a fresh meal.”

“We’ll carry out your orders.”

After bowing once more, they moved with perfect coordination.

They began clearing away the broken tables and scattered food without batting an eye—not even at Cheongpung’s vomit.

*They’re professionals. Absolute professionals.*

They put most cleaning companies to shame.

Unlike me, Cheongpung had been groaning with an expression like he needed to use the bathroom. He cautiously approached the servants.

“I-I’m sorry. Let me help.”

One of the servants shook his head.

“No, sir. This is our duty.”

“But I made the mess, so at least let me…”

No matter how sturdy the servants were, they were facing a Peak master. They had no choice but to follow Cheongpung’s wishes.

However, the moment Cheongpung forcibly took the cleaning tools from them and began wiping up the vomit, his movements abruptly stopped.

“Urk, uweeek!”

“……”

*Please stay still. Stop making more work for them.*

As Cheongpung emptied his stomach once again, Hong Jin looked at Li Feng with a doubtful expression.

“Assistant Commissioner Li, is that young man really Sword Saint Mae Jonghak’s Disciple?”

“Certainly.”

“Then why is he like that?”

“Ahem.”

Li Feng cleared his throat, his face reddening.

To him, Cheongpung was both Sword Saint Mae Jonghak’s Disciple and an elder of his sect. But it was also impossible to deny that he was a slightly strange young man.

“I suppose he’s like this because he’s spent his life completely removed from the secular world.”

“No, but even so. Are you saying Great Hero Mae didn’t teach him the basics?”

“Well… from what I’ve seen and heard, my Grandmaster is not an ordinary person himself.”

*Not an ordinary person.*

It was an impressive effort at putting things politely, but what I heard was, *They’re two of a kind.*

Hong Jin must have gotten a similar impression, because he remained silent for a moment.

“Would it really be all right to leave this matter to Huashan?”

“……”

“Yes.”

Li Feng’s answer came half a beat late. Hong Jin shook his head in disbelief.

“We can discuss that later. Shall we get going?”

His words made me suspicious, so I asked,

“Where? His Highness hasn’t even arrived yet.”

“That’s exactly who I’m going to fetch.”

“What?”

“If we stay here, we’ll be waiting until sunset. I have a rough idea where His Highness is.”

I watched Hong Jin turn away with a wink.

*He’d be a decent guy if he just stopped doing that.*

I was grateful that he had taken our side, but that was that, and this was this.

*My backside is precious.*

* * *

Hong Jin and Li Feng walked side by side at the front.

As I followed them, I gradually began to understand what positions they held here and how much influence they possessed.

“Loyalty!”

People’s emotions show in their eyes, their posture, and their voices.

The soldiers snapped off energetic military salutes toward Li Feng, and I could read boundless respect in their faces.

*It’s understandable.*

Li Feng, a lay disciple of Huashan, was an advanced First Rate master. Respecting strength was a male instinct, and he radiated an unmistakably masculine presence. From what I had observed, he was steadfast and taciturn.

*But he isn’t completely inflexible, either.*

I could tell from the fact that he had accepted Hong Jin’s proposal. Their relationship had clearly been hostile, but Li Feng knew when to join hands and when to let go.

No one disliked a superior who was reasonably flexible.

*Then what about Hong Jin?*

I shifted my gaze to the side.

Not a single soldier showed Hong Jin any respect as he walked along, frivolously wiggling his backside. If anything, some of them even cast contemptuous looks his way.

However…

“I-I pay my respects to Deputy Military Commissioner Hong.”

“Mm. Yes. Good work.”

“Yes, sir!”

Several officials and servants we passed on the way practically groveled before him.

Their trembling voices and cautious footsteps made their emotions obvious.

They were afraid.

*Respect and fear.*

They were opposing emotions, but they were the same in one respect.

Both came from the art of handling people. Li Feng and Hong Jin each held the support of their subordinates through respect and fear.

*So one of them controls the military, while the other controls civil affairs?*

Shanxi Province was called a frontier region, but its size couldn’t be ignored.

It was a respectable autonomous territory with a vast area and a population of several million registered in its household records.

Where there was land, people gathered. And where people gathered, power and wealth flowed. Even within the Shanxi Provincial Office, an invisible and fierce struggle for power was still underway.

*From what I’ve heard, Hong Jin seems to be ahead. But that’s not my problem.*

I was too busy trying to make a living to get involved in someone else’s power struggle.

After walking for some time while lost in thought, we passed through nine gates and came upon a group of people.

“Deputy Military Commissioner, and Assistant Military Commissioner, have you arrived?”

The tenth gate was particularly large and tall. I couldn’t tell whether it had genuinely been built that way or only seemed so because a hundred soldiers surrounded it without leaving even a gap.

*Wow. Talk about tight security.*

Would a Peak master, and one capable of using Sword Energy at that, be needed to try anything here? Every one of the guards was heavily armed with armor, spears, swords, bows, and more. Sharp eyes gleamed from beneath their helmets.

Cheongpung, who had been looking around and exclaiming in wonder this entire time, lowered his voice and whispered to me.

“Wow. What do these people do?”

“I’m not sure. Perhaps they’re the royal guard protecting Prince Shangshan?”

“The royal guard? They’re amazing…”

Cheongpung muttered with a vacant expression, then clenched his fists.

“Benefactor, I’ve made up my mind.”

“About what?”

*Why do I get nervous every time he opens his mouth?*

Of course, my premonition proved correct again.

“I want to join the royal guard too!”

“……I don’t think that’s such a good idea.”

This was news the Sword Saint probably wouldn’t like.

I rubbed my throbbing forehead.

“Um, shouldn’t you get your grandfather’s permission first?”

“It’s all right. Grandfather said life is short, so whenever I want to do something, I should try it.”

“So that’s why you want to join the royal guard?”

“Yes.”

Cheongpung stared intently at the royal guards standing in perfect rows, his eyes shining.

More precisely, he was staring at their gleaming black armor.

*No way. Is this guy…?*

“……It’s not because the armor looks cool, is it?”

“Gasp.”

That was it.

What kind of lunatic joined the royal guard because he wanted their merchandise?

Li Feng, who had overheard our conversation, approached us with a face that looked ten years older.

“Martial Uncle Cheongpung, I may be nothing more than a lowly lay disciple, but you are Huashan’s direct Disciple, someone who will bear the future of the sect on your shoulders. To abandon the sect and devote yourself to the military… Please be careful with what you say and do…”

Cheongpung stood there with an expression that had clearly been hit right in the bull’s-eye, then frantically waved his hands.

“N-No, that’s not it. Really.”

“Is that so?”

“Yes, yes!”

“Then I’ll take your word for it. I was considering bringing you a suit of armor on the way out, if you needed one, but…”

Cheongpung took the bait immediately.

“Thank you. I’ll accept it gratefully, Great Hero Li.”

“……”

“……”

*Is this guy serious?*

Cheongpung, oblivious to the sudden chill in the air around us, grinned.

“Great Hero Li is a good person.”

“I’m not Great Hero. I’m your Martial Nephew, Martial Uncle Cheongpung.”

“Martial Uncle, Martial Nephew. Those words feel awkward…”

Cheongpung tilted his head.

“Can’t we just call each other whatever feels comfortable?”

“No. Our sect’s hierarchy is strict. Call me Martial Nephew from now on. Then I’ll give you the armor.”

“Hmm. Even so…”

Li Feng delivered his final blow to the hesitating Cheongpung.

“If you call me Martial Nephew from now on, I’ll give you the weapons used by the royal guard as well.”

“Gasp…!”

The game was over.

The finishing touch for merchandise was a complete set. Cheongpung, now on the verge of obtaining the Royal Guard Armor Set, spread both arms with a face full of joy.

“Martial Nephew Li Feng!”

Li Feng answered awkwardly.

“M-Martial Uncle Cheongpung.”

“I like Martial Nephew Li Feng best in the world!”

“……Thank you, Martial Uncle.”

I felt sorry for the Sword Saint, who had raised that guy as his grandson for twenty years.

While even the royal guards were distracted by this unexpected farce, Hong Jin let out a deep sigh and spoke.

“What are you doing? Why haven’t you opened the gate?”

* * *

The young prince barely came up to my chest, if that. Prince Shangshan, Zhu Bao,[^1] was much smaller than I had expected—and much stronger.

*Ssshhk, ssshhk, ssshhk!*

That was not a sound a mere ten-year-old child should have been able to make with a sword.

His sword paths were sharp, and his footwork technique carried him busily across the training ground.

Even I, who wasn’t particularly well versed in sword techniques, could tell that his skill was more than enough to make me nod in approval.

*So there was a reason he invited us.*

When I first received Prince Shangshan’s invitation, I had one thought.

*I’ll go and tell him a few of the heroic tales he wants to hear. That was about all I had expected.*

That was all I had expected.

But that child was different. I might have to teach him about martial arts instead of telling him stories about my exploits.

“What do you think of His Highness?”

Hong Jin had waved away all the attendants waiting outside the training ground with a single gesture before asking me.

Even then, the young prince, absorbed in his martial arts, didn’t notice who had arrived or who had left.

“What kind of opinion are you asking for?”

“Well, for starters, his martial arts?”

I answered honestly.

“He’s beyond my expectations. No, he’s outstanding. When did he begin learning?”

“He began showing an interest in martial arts three years ago.”

“Three years…”

“Yes. Ever since the day he first held a sword, he has trained in martial arts every single day unless something unusual happened.”

Li Feng smiled proudly and added,

“He is not like an ordinary child in many ways. He possesses astonishing determination. Much like Young Hero Jin.”

“Me?”

“That’s right. I heard Young Hero Jin worked himself to the bone from a young age. You’ve been making quite a name for yourself, just as one would expect from a master the Jin Family of Taiyuan secretly raised with such painstaking care.”

“Uh… yes, I suppose.”

That was a bogus rumor the Jin Family of Taiyuan had spread for public consumption.

In reality, I didn’t even remember what I had been doing at the age of ten.

*I must have been attending elementary school or something.*

Li Feng continued.

“You have no idea how delighted His Highness was when he heard the story of the Sleeping Dragon of Shanxi. He must have been eagerly awaiting the chance to meet Young Hero Jin today.”

“……For someone who was looking forward to it, didn’t he make us wait rather a long time?”

I felt as though we had been waiting for almost an hour. Was it because he was a prince? The little brat already had no basic manners.

Li Feng smiled faintly at my timid complaint.

“His Highness has a habit of immersing himself in martial arts whenever he is nervous. If he has offended you, please accept my apologies.”

There was no need to apologize over something like that. I was waving my hands dismissively when Hong Jin cupped both hands around his mouth and shouted,

“His Hiiiighness—!”

The little figure who had been practicing his sword technique stopped abruptly at the shrill call. A moment later, he noticed us and crooked a finger.

“What is that supposed to be?”

“What do you mean? His Highness is calling us.”

“No, I mean, are we neighborhood mutts?”

“Wow, this is my first time being a neighborhood mutt!”

“……Please shut your mouth. No one here has ever been a neighborhood mutt.”

Suppressing my frustration, I walked toward the training ground.

Prince Shangshan Zhu Bao. His face came closer with every step.

*The rude ones always seem to be handsome.*

Even at such a young age, his already fully formed features were sharp and distinct. His black eyes stared directly at me.

When I reached him, a voice that was still unmistakably childish drifted out.

“Do you know who I am?”

I had at least learned the basics of etiquette by now. I lowered myself onto one knee so that our eyes were level.

“Yes. His Highness, Prince Shangshan.”

“I do not yet know your name.”

“My name is Jin Taekyung of the Jin Family of Taiyuan.”

A faint trace of surprise appeared in his previously dignified eyes.

“T-The Sleeping Dragon of Shanxi, Jin Taekyung?”

“That’s right.”

I wondered what his reaction would be.

The young prince remained silent for a long moment. Then he suddenly pulled something from inside his robes.

A wooden tablet about the size of an adult’s palm, and a dagger.

“This…”

“……?”

He had handed them to me, so I accepted them. But what was I supposed to do with them?

As I stood there in bewilderment, Zhu Bao delivered a single dignified word.

“I would like your signature.”

“……”

*Oh. He wants an autograph?*

[^1]: Zhu Bao (朱豹) is Prince Shangshan’s personal name.
## Chapter artifact 144

# Chapter 144

He was asking me for an autograph. A king, no less.

*What the hell is this?*

I never saw this scenario coming.

As I struggled to continue speaking in my bewilderment, a pair of large eyes stared at me quietly.

“Have I asked too much of you?”

“No, it’s not that… What are you planning to do with my signature?”

“Hmm. If you don’t want to, you don’t have to.”

Hidden beneath his archaic, historical-drama way of speaking was a desperate eagerness he was trying to conceal.

The tips of his feet scraped at the training ground floor like a puppy, and both his hands kept fidgeting restlessly. Those were proof enough.

*The little guy is cute, though.*

He was still a child. No matter how much of a king he was, he couldn’t hide his age.

His expression was dignified, but his body language was honest. I let out a quiet laugh.

“Why are you laughing?”

“It’s nothing. So I just carve my name into this wooden tablet?”

The young king’s lips twitched.

“If possible, include your alias as well.”

Why was he answering so seriously over something like this? I held back my laughter and picked up the dagger.

Scritch, scritch, scritch.

Sleeping Dragon of Shanxi, Jin Taekyung. I rested the wooden tablet on my knee and carefully carved the seven characters into it.

That was when Zhu Bao suddenly asked,

“Wouldn’t it be easier if you used Sword Energy?”

“It would.”

“Then why aren’t you using it?”

“It’s not that I’m choosing not to. I can’t.”

“You can’t use Sword Energy?”

“I mean exactly what I said. I can’t use Sword Energy because I’m not a Peak master yet.”

“You’re… not a Peak master?”

I raised my head slightly. Zhu Bao was staring at me with a shocked expression.

“Aren’t you the Sleeping Dragon of Shanxi?”

“Yes, that’s me.”

“And yet you can’t use Sword Energy? You’re not a Peak master?”

“…That can happen.”

“No, it can’t!”

Wow. He almost sounded hurt.

I had already been feeling a sense of relative deprivation because Sword Energy had been appearing so often lately. Now a little kid I had never seen before was twisting the knife.

*Is being unable to use Sword Energy a crime?*

I was hurt in my own way, and the young prince’s fandom had taken a hit too.

I was wiping my nose in wounded frustration when he suddenly exclaimed,

“How can you be so strong if you aren’t even a Peak master?”

“What?”

“One Question, One Kill Jopil, Blade of Flowers Jin Baekyang, and finally Pung Yang, the Red Wind Band Leader, not long ago. Weren’t all the enemies you’ve defeated powerful Peak masters?”

Jopil was the only one I could honestly say I had defeated entirely with my own strength, but I nodded for the time being.

“That’s right.”

“How was such a thing possible?”

“Well…”

*The Inventory is unbelievably useful. And no one can beat a group attack.*

*When things seem impossible, try rummaging through your Inventory. You might find an elixir worth half a jiazi or a weapon made of Ten-Thousand-Year Cold Iron.*

*…I can’t exactly answer that way.*

An image was something you built for yourself.

I opened my mouth with a gentle smile.

“Isn’t it because I was stronger?”

“Wow!”

“There’s a saying in Murim. The strong do not survive. Those who survive are strong.”

“Wow!”

“I’ve fought three Peak masters so far. I’ve even been attacked by dozens of First Rate masters.”

“How could that be!”

Zhu Bao clenched his tiny fists and let out an admiring gasp.

He gave such great reactions that it made me want to keep talking. I continued, recalling the moments of crisis I had fought my way through.

“But every time, I fought with everything I had and survived. Peak masters? Sword Energy? Those things aren’t important.”

“Sword Energy isn’t important? Do you mean that?”

“Of course.”

*It’s fucking important.*

Every person I met kept drawing out Sword Energy like endless strings of rice cake, and I was the only one who couldn’t use it.

Every fight left me wondering whether I had a human life or a fly’s.

*Make sure you eat plenty of elixirs. Without Sword Energy, your body will suffer.*

I shamelessly placed a hand on the young king’s shoulder and whispered,

“The desire to win. The unbreakable will to never give up until the very end. That is what made the Sleeping Dragon of Shanxi who he is today.”

“An unbreakable will…!”

Zhu Bao’s small body trembled. Then, after letting out a heated sigh, he opened his mouth.

“Can I become like you?”

“You can. From what I just saw of your training, you look like you’ll become a master in no time.”

“D-Do you really mean that?”

*Without the System, it would be difficult.*

*But you have to water a growing sprout.*

I nodded at those enormous, sparkling eyes. Then I added a few more characters to the completed wooden tablet and handed it over.

“Look at this whenever things get difficult, and let it give you strength.”

“What is this…?”

The young king examined the tablet and broke into a radiant smile.

“Thank you very much. I shall have this tablet enlarged and hang it on the signboard of the Shanxi Provincial Office.”

“…That?”

“Of course. Everyone who enters and leaves this place will read your famous words.”

I looked at Zhu Bao, who was gazing fondly at the wooden tablet, and thought,

*He’s going to hang that on the signboard of the Shanxi Provincial Office?*

*Dreams☆come true.*

—Sleeping Dragon of Shanxi, Jin Taekyung—

*…That?*

* * *

When we returned to the grand hall, it had been restored to pristine condition as though nothing had ever happened.

Once the servants filled the newly placed tables with all kinds of delicacies, Prince Shangshan Zhu Bao, seated at the head of the table, spoke.

“I thank you all for willingly answering my summons. Now, please eat your fill.”

*Ding.*

> **System**
>
> Quest condition, **Attend the luncheon hosted by the City Lord**, has been fulfilled!
>
> The Quest Reward will be issued after the luncheon ends.

The atmosphere that followed was warm and cheerful. With the young king, the host and master of the gathering, grinning from ear to ear, it could hardly have been otherwise.

“I have heard that One Question, One Kill Jopil was an exceptionally vicious man. Could you tell me what he was like?”

“Oh, that bastard was absolutely brutal. Well, you see…”

“I’ve heard that Blade of Flowers Jin Baekyang was a Peak master whose name was known even in the Central Plains. How strong was he?”

“He was insanely strong. Completely crazy.”

“Young Hero Jin, His Highness is listening. Please be more mindful of your language.”

“Ah, sorry. Anyway, to tell you about what happened then…”

After telling stories for quite some time, I was exhausted. I handed Cheongpung over to Zhu Bao, who continued asking me questions, and quietly withdrew.

“Sleeping Dragon of Shanxi, where are you going?”

“You know the Sword Saint, Mae Jonghak, right? This guy is his disciple.”

“The Sword Saint!”

“And he’s a Peak master, too. Ask him to teach you Sword Energy.”

I left Zhu Bao behind, happy as a child who had met Santa Claus, and slipped away to the side.

I saw the young prodigies of the Five Gates of Shanxi forcing food down without managing to say a word, as well as two people engaged in a fairly serious conversation.

Neither the former nor the latter made for company I particularly wanted to join.

*I’ll just eat.*

But before I could take more than a few pieces of meat, a syrupy voice wormed into my ears.

“Young Hero Jiiin.”

“…What?”

The moment I heard that voice, my appetite vanished.

“What are you doing all by yourself over there? Come over and talk with us.”

“No, thank you. I’m hungry.”

“It’s about the Jin Family of Taiyuan.”

“I don’t get involved in family affairs. Talk to my eldest brother instead.”

“That’s unfortunate. In that case, I suppose we’ll have no choice but to entrust it to the Seongun Escort Bureau.”

Seongun Escort Bureau? The name sounded familiar. Then I remembered—it was the family of the man I had thoroughly beaten at Honghwa Inn yesterday.

That guy had been the Young Bureau Head of the Seongun Escort Bureau, hadn’t he?

“Why the Seongun Escort Bureau?”

Hong Jin curled up the corners of his mouth.

“Oh, nothing. Please eat your meal. They say even a dog is left alone while it’s eating, so how could I bother the Sleeping Dragon of Shanxi?”

“…”

“Hee-hee. I was joking. Don’t look so serious. Come over and sit down.”

Hong Jin pulled out the chair beside him. I sat down as though I had no choice.

Beside Li Feng, of course.

As I’ve said before, my backside is precious.

“Let’s hear what this is about. I’m not very knowledgeable in this area, so I may not be much help.”

Hong Jin, who had been pretending to sulk with his lips stuck out, spoke.

“It doesn’t matter if Young Hero Jin doesn’t make a decision here. You only need to pass the matter along to the Lesser Family Head. Now, Assistant Commissioner Li?”

Li Feng took over.

“We would like to borrow the strength of the Jin Family of Taiyuan for this matter.”

“This matter being…?”

“I believe you’re aware of our plan to establish a primary connection between Shaanxi and Shanxi.”

“The thing you originally intended to do with the Zhongnan Sect?”

Hong Jin, who had been watching us, nodded.

“To be honest, the Zhongnan Sect isn’t a bad partner. It’s a massive sect belonging to the Nine Sects and One Gang, and its leadership, including the Sect Leader, the Wind-and-Cloud Sword Lord, has a practical nature. They’re different from the other, relatively closed-off Murim sects.”

“Then was there really any need to change partners? If you weren’t going to work with Huashan from the beginning, it might have been better to leave things as they were.”

“It was a decision I reached after giving it a great deal of thought. Although we overturned it today.”

Hong Jin continued with a faint smile.

“I’m not a martial artist, but I know very well what position the Sword Saint occupies in Murim.”

“…”

“But it has been more than thirty years since the Sword Saint disappeared. If we had known from the beginning that he had remained in Huashan and was raising successors, we wouldn’t have chosen the Zhongnan Sect.”

When he finished speaking, Hong Jin shot Li Feng a reproachful look.

Apparently, Li Feng had known about the Sword Saint and Cheongpung for the past ten years and hadn’t said a word.

“Deputy Military Commissioner, I’ll say it again: that was classified information belonging to our sect. There was simply no longer any reason to conceal it once Martial Uncle Cheongpung descended the mountain.”

Li Feng answered calmly, then turned toward me.

“I’ll get straight to the point. We need an Escort Bureau capable of expanding into the Central Plains, beginning with Shaanxi.”

“Ah.”

I had a rough idea of what was going on.

They were asking the Jin Family of Taiyuan to provide material or human resources.

“Are you planning to create an Escort Bureau?”

“Something similar. However, we would like to borrow the name of the Jin Family of Taiyuan. In return, we’ll provide half the funding and every possible convenience.”

They were practically offering to back us outright. Wouldn’t it be better for them to create their own Escort Bureau at this point?

As I wondered about that, I suddenly remembered what Jin Mukyung had told me several days ago.

*He said that the current Emperor also assassinated his older brother, the Crown Prince, and ascended the throne. I’m sure of it.*

It was only an unconfirmed rumor, but judging by how cautiously these two were acting, it didn’t seem entirely baseless.

Could the Emperor’s wariness have been the reason he sent his only younger brother to Shanxi Province, a place regarded as a frontier region?

*Hmm. This feels suspicious too.*

As I wondered whether I had gotten myself entangled in something dangerous, the two men spoke to me.

“We’ll arrange a meeting soon regarding this matter, so please speak well of it to the Lesser Family Head.”

“Young Master Jin, you know this is a good offer, right?”

“I know. I do, but…”

In a way, this was someone else’s family feud. If they were ordinary brothers, they might fight over who got to eat one more ice cream, end up with a bloody nose, and leave it at that.

But this wasn’t ice cream. It was the imperial throne.

That meant it wouldn’t end with a bloody nose.

“I’ll make sure to pass it along to my eldest brother.”

I deliberately kept my answer vague. Jin Wikyung would be the one making the decision anyway, so there was no reason for me to worry about it. Unless he asked for my opinion first, that was.

“That’s enough. He won’t ignore what Young Master Jin says. We’ve heard plenty about how much the Lesser Family Head cares for his younger brothers.”

*So everyone in the neighborhood has heard about it.*

I drained my cup of liquor with an embarrassed expression, and my eyes met the four of them sitting at the far end of a table some distance away, all looking as though they were about to get indigestion.

Oh, right. I almost forgot something.

“Hey. Comrade Chairman—no, Deputy Military Commissioner.”

“Yes?”

“That Escort Bureau business. Wouldn’t it be enough to simply change the sign?”

Unlike the bewildered Li Feng, Hong Jin grinned.

“You have a place in mind?”

“The one the two of you were talking about earlier.”

“The Seongun Escort Bureau? Don’t take them too lightly. It’s the most prestigious Escort Bureau in Shanxi, after all. They’ll be difficult to swallow in one bite.”

“That’s why we have to chew thoroughly.”

I could tell exactly what we were dealing with from the Young Bureau Head. If Hong Jin and Li Feng helped the Jin Family of Taiyuan as it stood now, we could chew through the whole thing—bones and all—and still digest it.

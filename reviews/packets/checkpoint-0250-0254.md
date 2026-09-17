# Checkpoint Review — 250–254

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

# Chapters 250–254

## Plot

The Star-Array Grand Banquet’s main event reduces more than five hundred finalists to roughly ten. Jin Taekyung wins every duel, defeating Black Water Dart, the Hebei Peng Family’s Hunyun Saber, the Lesser Family Head, and Gung Gibang to reach the final. Gung reveals that he has mastered only five stages each of the Eighteen Dragon-Subduing Palms and Dog-Beating Staff Technique.

The Invincible Divine Sword is revealed as Cheongpung, who has been traveling under the false name Kang Pung. He defeats Zhuge Gyun and Wudang’s Willow-Cloud Divine Dragon, reproducing the Taiji Wisdom Sword and shattering the Divine Dragon’s Pine-Pattern Ancient Sword with the Thirty-Six Plum Blossom Swords. Cheongpung and Taekyung expect to meet in the final, but Cheongpung must first face Jongni Chu in the semifinal.

Jongni Chu’s unfamiliar martial arts and unexplained identity alarm the Hidden Shadow Pavilion, which is unable to verify his background. Agents surveil him, Taekyung, and Cheongpung; Shadow Killer’s contact was lost after pursuing Jongni. Song Ho disguises himself as a beggar and follows Jongni, suspecting they have met before. His recurring leg pain recalls the Demonic Cult’s final battle decades earlier, when he lost the leg and heard an unknown man threaten to tear it off.

After observing Taekyung’s effortless counters, bare-fist destruction of an internal-energy-infused staff, and endurance against the Eighteen Dragon-Subduing Palms, Jongni suspects that Taekyung possesses the Heavenly Martial Physique and identifies him as the Fire King’s Disciple. Before the final, Hyuk Mujin tells Taekyung that rumors identify Cheongpung as Invincible Divine Sword Kang Pung. Jongni and Cheongpung begin their semifinal; Jongni refuses Cheongpung’s offer of a better sword, leaving the result unresolved.

## Continuity

- Jin Taekyung has reached the Star-Array Grand Banquet final after defeating Gung Gibang in exactly fifteen minutes.
- Cheongpung is the Invincible Divine Sword and is competing under the false name Kang Pung.
- Cheongpung defeated the Willow-Cloud Divine Dragon and advanced to the semifinal against Jongni Chu.
- Jongni Chu is a young Peak martial artist from Yunnan, known as the Life-Sustaining Sword and Always-Victorious Sword. His identity, affiliation, and martial-arts origin remain unknown.
- Jongni Chu has befriended Cheongpung but carries a heavily rusted sword and refuses to borrow another.
- Jongni Chu may be connected to Dark Heaven, the Demonic Cult, the Demonic Path, or another unknown power; no conclusion has been reached.
- The Hidden Shadow Pavilion is surveilling Jongni Chu, Taekyung, and Cheongpung. Shadow Killer’s fate remains unknown after contact was lost.
- Song Ho is the former Chief of the Hidden Shadow Pavilion, a master of disguise, and a former Peak master who lost one leg during the final battle against the Demonic Cult.
- Song Ho suspects he has encountered Jongni Chu before.
- Taekyung believes Cheongpung will win the semifinal and is preparing for their possible final duel.
- Hong Dao still intends to retire after the banquet and believes he has roughly one year left to live.
- The Gold-Faced Young Master, concealed finalists, Hong Dao’s interim successor, and the significance of Song Ho’s prior encounter with Jongni remain unresolved.

## Translation Decisions

- Use **Pine-Pattern Ancient Sword** for 송문고검, **Great Clarity Sword Technique** for 태청검법, **Taiji Wisdom Sword** for 태극혜검, and **Thirty-Six Plum Blossom Swords** for 매화삼십육검.
- Use **Hunyun Saber** for 혼원도 and **Willow-Cloud Divine Dragon** for 유운신룡.
- Use **Dog-Beating Staff Technique** for 타구봉법 and retain **Eighteen Dragon-Subduing Palms** for 항룡십팔장.
- Keep **Demonic Path** distinct from **Demonic Cult**.
- Use **Kang Pung** for Cheongpung’s false name, **Shadow Killer** for 암중살, and **Taiyuan Park Family** for 태원박가.
- Retain **Life-Sustaining Sword**, **Always-Victorious Sword**, **Invincible Divine Sword**, and **Hidden Shadow Pavilion**.
- Render Jongni’s address to Taekyung’s master as **Fire King’s Disciple** and preserve the abrupt tonal shift in his line: “I’ve never had a friend like you.”

## Durable state

{
  "active_continuity": [
    "The Star-Array Grand Banquet has reached its finals after Jin Taekyung defeated Gung Gibang in the semifinals.",
    "Jongni Chu is a young Peak martial artist from Yunnan whose identity and martial-arts origin remain unexplained.",
    "Jongni Chu is known as the Life-Sustaining Sword and Always-Victorious Sword and has befriended disguised Cheongpung.",
    "Jongni Chu's unfamiliar martial arts and unexplained identity have drawn Song Ho's suspicion and the Hidden Shadow Pavilion's surveillance.",
    "Jin Taekyung is Jeok Cheongang's Disciple and has reached the finals.",
    "Cheongpung is the Invincible Divine Sword, using the false name Kang Pung, and is now fighting Jongni Chu in the semifinals.",
    "Song Ho is the former Chief of the Hidden Shadow Pavilion, an intelligence operative, and a master of disguise.",
    "Song Ho lost one leg during the final battle against the Demonic Cult decades ago and suffers recurring pain from the old injury.",
    "Song Ho suspects he has encountered Jongni Chu before but does not know when or where.",
    "The Hidden Shadow Pavilion has assigned agents to follow Jongni Chu from a distance and to monitor Jin Taekyung and Cheongpung.",
    "Hyuk Mujin came to keep Jin Taekyung company because the final is scheduled for the following day.",
    "Hyuk Mujin knows the rumors identifying Cheongpung as the Invincible Divine Sword Kang Pung and expects him to win the semifinal.",
    "Jin Taekyung believes Cheongpung will win but is observing the semifinal to prepare for their possible final duel.",
    "Jongni Chu entered the semifinal carrying a heavily rusted, poorly maintained sword and refused Cheongpung's offer to lend him a weapon."
  ],
  "continuity_sources": [
    254
  ],
  "open_questions": [
    "How will Cheongpung's semifinal against Jongni Chu conclude, and will the eventual Taekyung-Cheongpung final occur and how will it conclude?",
    "What is Jongni Chu's identity, affiliation, and martial-arts origin?",
    "Is Jongni Chu connected to Dark Heaven, the Demonic Cult, the Demonic Path, or something else?",
    "Why was Shadow Killer pursuing Jongni Chu, what did the Hidden Shadow Pavilion seek, and what became of Shadow Killer after contact was lost?",
    "Who is the Gold-Faced Young Master who bet on Taekyung?",
    "Which powerful martial artists concealed their abilities during the preliminaries?",
    "Who has Hong Dao chosen to serve as Abbot until Unnamed returns from Arhat Cave?",
    "Why does Song Ho attend the main-event duels daily before leaving during the third day, and what is the significance of his prior encounter with Jongni Chu?"
  ],
  "safe_through": 254,
  "temporary_decisions": [
    "Use Wave King for 낭왕 and Arhat Cave for 나한동.",
    "Use Benefactor Jeok for 적 시주, Fellow Daoist for 도우, and the three idiots for 세 얼간이.",
    "Use Eighteen Dragon-Subduing Palms for 항룡십팔장, Dog-Beating Staff Technique for 타구봉법, and Three Visits to the Thatched Cottage for 삼고초려.",
    "Use Life-Sustaining Sword for 연명검, Hidden Shadow Pavilion for 은영각, Black Water Dart for 흑수표, and Invincible Divine Sword for 무적신검.",
    "Use Kang Pung for 강풍, Shadow Killer for 암중살, and Taiyuan Park Family for 태원박가.",
    "Use Demonic Path for 마도 and keep it distinct from Demonic Cult.",
    "Use Hunyun Saber for 혼원도.",
    "Use Willow-Cloud Divine Dragon for 유운신룡; use Pine-Pattern Ancient Sword for 송문고검, Great Clarity Sword Technique for 태청검법, Taiji Wisdom Sword for 태극혜검, and Thirty-Six Plum Blossom Swords for 매화삼십육검."
  ],
  "version": 1
}

## Reading copies

## Chapter artifact 250

# Chapter 250

The Demonic Cult.

If they had not existed—if the people who called themselves the Heavenly Demon Divine Cult had never appeared—the Murim under heaven would never have united as one.

But when Qinghai, Gansu, and Sichuan fell into the Demonic Cult’s hands in a mere four months, everything changed.

The leaders of countless orthodox factions, including the Nine Sects and One Gang and the Five Great Families, gathered in one place. Even the major figures of the unorthodox and dark-path forces, such as the Yangtze River Channel League and the Green Forest Alliance, lent their strength.

And at the center of it all stood the Martial God.

An unparalleled master known as the greatest beneath heaven. An invincible man who belonged to no faction.

*“Let’s raise one flag. That is the only way.”*

Thus, after years of repeatedly joining together and splitting apart, the orthodox factions, dark-path forces, and unorthodox factions united beneath a single flag.

The Murim Alliance was born.

Not long after the fierce ten-year Great War ended, the Murim Alliance was dissolved along with the Martial God’s disappearance. But the site where the heroes of old had once gathered remained, carrying on in a new form with new people.

“Good grief, it’s packed.”

A middle-aged man stared at the long line stretching out in front of the Murim Alliance with a weary expression.

They had not even entered yet, and it was already this crowded. Just imagining how chaotic it must be inside made his vision go dark.

To make matters worse, he was still suffering from yesterday’s hangover.

“Honey, let’s just take a lap around the market and go, huh?”

At the middle-aged man’s desperate whisper, his wife firmly shook her head.

“No. Do you have any idea how excited he is? He’s been begging us for three whole days, ever since the first day of the main event.”

“No, no. It’ll be fine. We can take a lap around the market and put some candy in his mouth. That’ll keep him quiet. To hell with the Star-Array Grand Banquet and all that. What’s so impressive about watching Murim people fight anyway… Huh?”

The middle-aged man swallowed a startled breath.

His son, who had been carried on his wife’s back, had woken up and was staring at him.

The boy’s large eyes were moist, as if he might burst into tears at any moment.

“Dad. Aren’t we going to see the Star-Array Grand Banquet?”

“No, son. That’s not what I—”

“Sniff, sob…”

“W-Wait a second. Just listen to me.”

“Waaaaaaah!”

“…My boy sure has a powerful set of lungs.”

A short while later, the child held some candy and a wooden doll about the size of an adult’s palm in his hands.

The middle-aged man grumbled at the unexpected expense.

“Damn thieves. What kind of piece of wood costs that much?”

But he was a parent too. When he saw his child’s beaming face, his irritation eased a little.

“You like it that much?”

“Yes! Jin Taekyung is so cool! The Sleeping Dragon of Shanxi is the best!”

“Jin Taekyung? The Sleeping Dragon of Shanxi? Is that wooden doll’s name Jin Taekyung?”

“Dad, you don’t know Jin Taekyung?”

“Of course I do.”

“Really?”

“Of course. There’s nothing your dad doesn’t know.”

He could not afford to lose his dignity as a parent over some wooden doll.

Having barely escaped the crisis, the middle-aged man waited until his son was looking away before quietly asking his wife,

“Honey. Who’s Jin Taekyung, the Sleeping Dragon of Shanxi? You don’t know either, do you?”

“Why wouldn’t I?”

His wife looked at him as if he were hopeless.

“We came here to watch his duel today.”

“…”

“The Sleeping Dragon of Shanxi, Jin Taekyung. Our Hyeok has told you several times that he’s on a three-win streak in the main event… How can you be so uninterested in your own child?”

As his wife’s lecture continued, the middle-aged man thought:

*I hope this Sleeping Dragon or whatever gets his ass kicked today.*

* * *

Whoosh!

I calmly watched the sword being swung at me.

It was as fast as an arrow and as agile as a snake.

After a bewildering series of forms, red Sword Energy shot toward me.

Shhk-shhk-shhk-shhk!

I flipped my body.

The Sword Energy passed within half a span of me, and I thrust out my fist.

A single punch wreathed in blue flame—the first form of the Flame-Extinguishing Divine Fist.

Boom!

A powerful collision.

Sword Energy and Fist Energy slammed together, sending a thunderous boom across the arena. Dust from the stones piled on the dueling platform whirled into the air and blocked my vision.

I stepped forward.

Again. One more time.

Boom! Kraa-boom!

The shock wave bursting from my fist split the air. The flames of the Flame-Extinguishing Divine Fist devoured the cloud of dust.

A man stood at the other end.

Blood trickled from the corner of his mouth, and his face was pale. He gripped a broken sword and stared at me with wide eyes.

“H-How?”

“Well.”

At the same time, I kicked off the ground.

Crack.

The instant my foot left the ground, spiderweb-like cracks spread across the hard bluestone.

I pushed through the fierce wind and threw a third punch at him.

“I surrender!”

The cry burst out like a scream.

My fist stopped right in front of the man’s nose. The wind pressure created by its tremendous power and speed sent his hair flying.

The hero’s headband slipped from his forehead, fluttered out of the arena, and landed with a thud.

“S-Sleeping Dragon of Shanxi, victory!”

Waaaaah!

At the referee’s shout, the cheers that had been held back exploded from every direction.

Hundreds, even thousands, of people rose from the stands, throwing flowers and all sorts of objects.

“Yeah! Sleeping Dragon of Shanxi!”

“Dad! I can’t see! Give me a shoulder ride!”

“You’re the best, kid! I even bought your wooden doll!”

The stands were not filled only with martial artists. A considerable number of commoners from Henan—and even people who had come from far away to watch the Star-Array Grand Banquet—were there as well.

I waved to the especially noisy father and son before turning away.

> **System**
>
> - You won the duel against Black Water Dart!
> - An overwhelming victory! Everyone who watched the duel offers unreserved praise!
> - Your **Fame** increased by 500!
> - Your **Fame** increased by 430!
> - Your **Fame** increased by…

I listened to the familiar notifications as I stepped down from the dueling platform.

At the same time, someone landed in front of me with an elegant movement technique.

Tap!

“Good heavens, what are all these specks of dust on your precious body? This poor Daoist will wipe them away for you.”

*Damn, this guy’s back again.*

No matter how many times I tell him not to come, he just won’t fucking listen. He’s hopeless.

I snatched the towel from his hand.

“If you’re going to come, at least come normally. Don’t use that Cloud-Dragon Eight Forms or Oh Tae-sik or whatever.”

Baek Woo, the Kunlun Cloud Dragon, answered with a dejected expression.

“It is the Cloud-Dragon Eight Forms. Even so, it is one of the Kunlun Sect’s secret arts. You could at least remember its name…”

“Right. How heartbroken do you think your Master would be if he saw you using that secret art to deliver towels? He’s probably watching from the VIP seats even now.”

“My Master told me to get along with Fellow Daoist.”

“…”

“I heard that Great Hero Jeok Cheongang, the Fire King, once saved my Master’s life…”

No wonder Baek Woo had been unusually friendly since the day after we arrived.

He must have scampered over to his Master to tattle on me, only to have it blow up in his face.

On top of that, after watching the previous three duels—or four including the one just now—he must have realized it clearly.

My skills were far above his own.

And the other two idiots were no different.

“Our sect’s Eighteen Dragon-Subduing Palms is one of the five greatest palm arts beneath heaven.”

“Sure. But you’ve only mastered it to the fifth level, right?”

“That is correct.”

“Is that why you brought that?”

“Yes.”

Gung Gibang approached with a basin of water for washing my face in his hands.

“…”

I found the situation absurd, but I thanked him anyway, washed my face, and dried myself with the towel Baek Woo had brought.

The Beggars’ Sect’s Successor Beggar had brought me water, and the Kunlun Cloud Dragon, one of the Ten Dragons and Phoenixes, had brought me a towel.

To everyone else, this must have looked like a very strange sight.

Wait.

Come to think of it, someone was missing.

“Where’s Gyun?”

The fellow who would have rushed over long ago and started talking about his ancestor, Zhuge Wuhou, had been nowhere to be seen.

Baek Woo answered my question.

“Young Master Zhuge went to duel.”

“No wonder I haven’t seen him.”

There were no fewer than five hundred finalists. As a result, the duels were being held sequentially at several different locations.

Today was the third day. Once all the scheduled duels were over, only around thirty people would remain.

*There are more injured people than I expected.*

Every participant was a master with at least one exceptional skill.

Some degree of injury was unavoidable. There were even cases where someone won a razor-close duel, only to withdraw afterward.

*I’m the unusual one.*

Including the victory I had just secured, I had won four times in total, but not one of my duels had lasted a full fifteen minutes.

The longest had been a fight of a little over two hundred exchanges, and that was only because I wanted to experience my opponent’s unusual martial art.

*I’m glad I decided to participate in the Star-Array Grand Banquet.*

From what I had seen, some of the participants understood certain martial arts more deeply than I did.

I was simply superior to them in several other areas, and I was gaining experience by facing unfamiliar martial arts I had never encountered before.

*If I had stayed in Fire Gate Cavern, I never would have gotten this kind of experience.*

My gaze naturally turned toward the VIP seats.

I saw Jeok Cheongang doing his best to keep his expression under control and Jin Wikyung looking so pleased he could barely contain himself.

And beside them…

“That man’s here again today.”

“Who?”

“Who?”

“The Thousand-Faced Fox, Song Ho. He comes every day without missing one.”

Baek Woo and Gung Gibang, who had been about to turn their heads at my words, both stopped.

“Why? Is he someone important?”

“Sir Song?”

“You mean the Thousand-Faced Fox?”

The two of them asked at the same time, then lowered their voices.

“He’s certainly an impressive man. No—perhaps I should say frightening.”

“The Murim Alliance’s Hidden Shadow Pavilion once possessed an information network that could rival the Beggars’ Sect—or even surpass it.”

“The Hidden Shadow Pavilion?”

Gung Gibang nodded.

“I heard it performed truly astonishing feats during the Great Faction War. Of course, the Thousand-Faced Fox, who was its head, deserves much of the credit for the Hidden Shadow Pavilion’s existence.”

*If I had to compare it to the modern world, would he be like the director of the FBI?*

If even the Beggars’ Sect’s Successor Beggar spoke of it that way, the Hidden Shadow Pavilion’s intelligence network must have been extraordinary.

Judging from the past tense, it seemed to have followed the same path and naturally disappeared after the Murim Alliance was dissolved.

*The former head of a retired intelligence organization…*

Just as I was watching him closely, Song Ho rose from his seat and disappeared somewhere.

I kept my eyes on his back until the last moment.

Then the roar of the crowd rang in my ears.

“Waaaaah!”

“The Life-Sustaining Sword won again!”

I turned toward the cheers and saw Jongni Chu coming down from the dueling platform in clothes that looked like rags.

His entire body glistened with sweat, and he was breathing heavily.

The two idiots muttered as they watched him.

“Life-Sustaining Sword? Whoever came up with that epithet had quite a knack for naming people.”

“He does keep winning by a hair. In that sense, he really is the Always-Victorious Sword.”

The nickname Life-Sustaining Sword had been given to Jongni Chu because he won every match by barely surviving.

I had not expected him to make it to four wins, but it seemed he was unexpectedly well suited to actual combat.

*If he made it this far, he must have some skill.*

Just how did he fight to earn the name Life-Sustaining Sword?

A quiet laugh escaped me as I watched Jongni Chu hurriedly gulp down cold water.

*Maybe I’ll run into him on the dueling platform later.*

I had not had much contact with Jongni Chu since three days ago. When we happened to cross paths, we merely acknowledged each other.

If our next meeting took place on the dueling platform, I might feel a little sorry for him.

“Anyway, thanks for the towel and the water. While you’re at it, clean this up too.”

Baek Woo and Gung Gibang each took the towel and basin before asking,

“Where are you headed?”

“Our sect’s Eighteen Dragon-Subduing Palms is one of the most renowned martial arts beneath heaven… Where are you going?”

“To watch Gyun’s duel.”

I had heard that Zhuge Gyun had learned a fan technique that used a folding fan.

I decided to watch his duel and broaden my knowledge of martial arts while I was at it.

I was about to head toward another dueling platform when I suddenly stopped.

“Oh, right. Who was his opponent again?”

* * *

*The Invincible Divine Sword.*

Zhuge Gyun was breathing heavily.

When he first heard his opponent’s epithet, he had inwardly laughed. He had thought it far too grand for an unknown nobody with no reputation to use.

But…

*How has someone like this remained unknown until now?*

The hand gripping his fan trembled.

His legs had already lost half their strength, and merely remaining upright was difficult. His eyes, opened wide as he tried to follow sword strikes too fast to see clearly, were beginning to ache.

The internal energy in his dantian had been exhausted long ago.

Yet even though Zhuge Gyun, one of the Ten Dragons and Phoenixes, was in this state, the Invincible Divine Sword remained completely calm.

No—he even seemed excited.

“Wow! You’re the first person I’ve ever seen use a fan technique! Do you have another one? Another one?”

“…”

At the innocent voice drifting from beneath the deeply lowered bamboo hat, Zhuge Gyun threw away his fan.
## Chapter artifact 251

# Chapter 251

My prediction that Zhuge Gyun would win was spectacularly wrong.

When we found the place where several duels, including his, were being held, what awaited us was the roar of the crowd chanting for the Invincible Divine Sword—and Zhuge Gyun sitting there blankly.

“What happened? You lost?”

At my question, Zhuge Gyun bitterly nodded.

“I was completely toyed with. I couldn’t touch so much as a hair on his head.”

Zhuge Gyun was a direct descendant of the Zhuge Clan, one of the Five Great Families.

As his epithet, the Divine Marvel Dragon, suggested, his true weapon was his brilliant mind. But having learned his family’s secret arts, he also possessed outstanding martial arts.

The name Ten Dragons and Phoenixes was not something one could earn through intelligence alone.

*That guy was toyed with?*

Then his opponent was clearly a master one or two levels above him.

A sudden curiosity welled up inside me, and I asked Zhuge Gyun,

“Where is he?”

“He probably left immediately after the duel… Huh? There he is.”

I followed the direction Zhuge Gyun pointed and narrowed my eyes.

“That guy? The one stuffing his face with dumplings?”

“Yes.”

“……Hmm.”

“What’s wrong?”

“Nothing. He just feels strangely familiar.”

The man wore a loose-fitting robe and a bamboo hat pulled down low over his face. I couldn’t make out his features or even his build clearly, but the side profile of the way he kept shoving dumplings into his mouth looked somehow familiar.

*Where have I seen him before?*

The answer in situations like this was to take the direct approach. I walked toward the Invincible Divine Sword.

The closer I got, the blurrier my memories became, but that was all. Instead, I did learn one thing.

*He’s strong.*

His posture and attitude were as careless as they could be, and he seemed so relaxed that he did not appear to be on guard at all.

Yet the energy I sensed from the Invincible Divine Sword was by no means inferior to my own.

*Had someone like this been around all along?*

After some thought, I opened my mouth.

“Excuse me.”

*Chomp, chomp.*

The Invincible Divine Sword’s mouth, which had been chewing and swallowing dumplings as if possessed, abruptly stopped.

“You’re the Invincible Divine Sword, correct?”

“……”

“I apologize for approaching you out of the blue. I have a few things I’d like to ask.”

“……”

“Excuse me?”

What was wrong with this guy? Why wasn’t he answering when someone was calling him?

As I stared at him, the Invincible Divine Sword’s Adam’s apple bobbed visibly beneath his bamboo hat.

*Gulp.*

“Ahem. Ahem.”

“……?”

“Erhem. J-Just a moment.”

After clearing his throat several times, a low, resonant voice emerged from between the Invincible Divine Sword’s lips.

But *what can I say?* It was painfully obvious that the voice was being forced.

“Why? No—I mean, what is it?”

“I have a few things I’d like to ask.”

“Go ahead. No, speak.”

“……”

What was this guy doing?

I looked at the Invincible Divine Sword through half-lidded eyes. Perhaps he noticed my suspicion, because he pulled his bamboo hat even lower.

*I’m getting a feeling about this.*

I casually threw out some bait.

“Oh, I’m sorry for introducing myself so late. I’m Park Taekyung of the Taiyuan Park Family.”

“Huh? Since when did you change your surname?”

“……”

“……!”

An icy silence fell.

Realizing his mistake, the Invincible Divine Sword frantically waved his hands. Instead of the forced baritone, a clear and crystalline voice like a young boy’s spilled out in a rush.

“No, that’s not what I meant. The Sleeping Dragon of Shanxi is so famous that I knew who you were.”

“Oh. I see.”

“Yes. Yes.”

“May I ask your name?”

“The Invincible Divine Sword.”

“Your name, not your epithet.”

“K-Kang Pung.”

*What kind of Pung?*

What a naming sense.

I let out a quiet laugh, unable to believe it.

This was not even something I needed to confirm with the Qi Sense Skill. At this point, it would have been stranger not to know.

“It’s been a while. Let’s talk somewhere quiet.”

“……Why, why? This is the first time I’ve met you.”

“Really? Should I send a messenger pigeon to Huashan?”

“……!”

The Invincible Divine Sword slowly lifted his bamboo hat.

A young man with an innocent expression looked at me with eyes filled with both resignation and delight.

“Hello, Benefactor.”

A familiar face I had not seen in a year.

I laughed and lightly tapped Cheongpung’s bamboo hat.



* * *



The Murim Alliance was almost a city in itself. It had residential areas where people could live, along with all kinds of facilities for daily life.

So it was not particularly surprising that it also had an entertainment district.

We settled down at an inn in the most remote alley we could find.

There were no other customers in the place besides the proprietor, who was so old that he could barely hear.

“I heard what happened. You ran away on the way back to Huashan?”

“Yes. Right after Benefactor left with Grandpa Jeok.”

“Why? Huashan is practically your home.”

“I didn’t want to go back. Grandpa wasn’t there anymore, and I hadn’t seen much of the world.”

“Still, you managed to escape.”

“My Martial Nephews tried to stop me, so I used a little force. They probably wouldn’t have woken up for three days. I ran away while they were out. Hehe.”

“……”

How much force had he used, exactly?

In any case, it was the sort of thing only someone like Cheongpung could have managed.

Baek Museong might have been known as Huashan’s Lone Crane and one of the Three Plum Blossom Elites, but Cheongpung was already a true genius on an entirely different level.

Even a Third Rate sword technique like the Three-Talent Sword Technique became a Peak martial art when performed by him.

From what I had seen, the depth of his understanding of martial arts and the speed at which he learned them were incomparable.

*If there were another genius like him, it would probably be Jin Mukyung.*

I listened to Cheongpung’s excited account of his travels through the martial world while thinking about this and that.

I had expected as much, and sure enough, he hadn’t done a damn bit of martial arts training. His stories were all about roaming around, goofing off, and eating to his heart’s content.

“I ate dumplings in Sichuan, but they were spicy!”

“Ah, yes. That sounds very surprising.”

“Dumplings in Guangdong and Hainan have seafood in them!”

“That makes sense. They’re close to the sea.”

“Zhejiang Province’s dumplings are…”

Had this guy done nothing but eat dumplings all year?

In the end, while listening to him talk about Hunan Province’s dumplings, I couldn’t take it anymore and cut him off.

“So what are you going to do from here?”

“Do what?”

“The Invincible Divine Sword. Are you going to keep that up?”

“Yes. Martial Nephew Baek Museong knows that I’m participating in the Star-Array Grand Banquet. If I hide like this, no one will recognize me!”

“……”

“Hehe. Everyone’s been completely fooled.”

I would bet my right hand and my entire fortune that he had already been found out. I was even willing to double down on it.

*No wonder there were so many Huashan disciples near the dueling platform earlier.*

Since the Star-Array Grand Banquet was open to martial artists from across the world, there were no particular restrictions even if someone deliberately concealed their identity.

But Huashan was one of the Nine Sects and One Gang. There was no doubt they had noticed Cheongpung’s presence long ago.

And yet they were merely watching him from a distance.

*At this point, this is basically a group hidden-camera prank.*

A movie titled *The Cheongpung Show* would not even seem strange.

I watched Cheongpung enjoying himself while inwardly clicking my tongue, then opened my mouth as a thought suddenly occurred to me.

“Then I guess we’ll meet later?”

The smile spread across Cheongpung’s face grew wider.

“I hope so.”

“You hope so?”

“I was curious how strong Benefactor had become. I’ve wanted to spar with you at least once.”

I felt the same way.

One of the reasons I had decided to participate in the Star-Array Grand Banquet was the existence of Cheongpung and Jin Mukyung.

“What do you think now that you’ve seen me again?”

“Hmm…”

“Be honest.”

I leaned back against the old chair.

Amid the creaking sounds, Cheongpung was silent for a moment. Then he suddenly tapped the scabbard hanging from his waist.

“Grandpa used to say that a martial artist should speak with their weapon.”

“He was right.”

The Sword Saint’s word, straight from the source. I let out a quiet laugh and stood up.

“Where are you going, Benefactor?”

“To prepare for the finals. We’ll finish our conversation there. With our respective martial arts, of course.”

“The finals…”

Cheongpung slowly repeated the word, then nodded with an unusually serious expression.

“Good. I’ll win anyway.”

“Big dreams for someone who spent the entire year eating dumplings.”

“I trained sometimes, too.”

“Sure you did.”

I ignored Cheongpung’s disgruntled muttering, paid the bill, and left the inn.

The moment we escaped the narrow, dark alley, we ran into a familiar face.

“Jongni Chu?”

Jongni Chu smiled and waved.

“Oh, we meet here again. We must be fated to cross paths.”

“What fate? It’s probably just a coincidence. What brings you here?”

“I came to grab a bite.”

“Here?”

The remote alley contained only a few shops lined up beside each other. Even those were so old they looked ready to collapse at any moment.

To anyone, it looked like a terrible place to find a meal.

But Jongni Chu calmly nodded.

“I ate some thin noodles at a nearby street stall, and the vendor told me the dumplings at that shop were supposed to be delicious.”

The sign he pointed to belonged, by pure coincidence, to the very shop Cheongpung and I had just left.

“Really?”

“Of course. Apparently, it’s a hidden gem known only to those in the know. Have you tried it?”

Cheongpung, who had already pulled his bamboo hat low over his face, abruptly joined in with an awkwardly altered voice.

“They’re incredibly delicious. No, I mean, delicious they are.”

Jongni Chu’s gaze shifted to Cheongpung.

“I don’t believe we’ve met before. Would it be rude to ask who you are?”

“The Invincible Divine Sword, Kang Pung.”

“That is quite an impressive epithet. I’m Jongni Chu, the Always-Victorious Sword. I look forward to getting along with you, friend.”

“F-Friend?”

Cheongpung slightly lifted his bamboo hat and looked at Jongni Chu before vigorously nodding.

“Great! No—I mean, good! I’m delighted! You’re the first person who’s ever asked me to be friends!”

“……Enough. That’s more than enough.”

Why didn’t he just walk around with a sign on his forehead saying *Cheongpung of Huashan*?

Jongni Chu smiled gently as he watched Cheongpung jumping for joy while I tried to calm him down.

“Looks like you already have a good friend by your side. In any case, I’ll see you next time, friends.”

“Yeah, let’s just happen to run into each other once in a while. Not too often.”

“Goodbye! Goodbye, my friend!”

“I’ll keep that in mind.”

He dipped his head and disappeared into the dark alley.

When we reached the bright street where the sunlight was shining down, Cheongpung grinned and said,

“He seems like a good person. That’s how he feels.”

I gave him some serious advice.

“Not everyone who likes dumplings is a good person.”

“Oh, I should have told him to dip them in only a little soy sauce.”

“……”

He really didn’t listen to a word I said.



* * *



Cheongpung’s concern had been pointless.

Jongni Chu did not enter the shop.

Even after passing it, he did not stop walking.

How long had he walked through the dark alleys tangled together like a maze? At last, in a place containing nothing but a few rats and filth, Jongni Chu stopped.

A quiet voice slipped from his lips.

“The Invincible Divine Sword. The more I think about it, the better that epithet sounds. What do you think?”

The moment he finished speaking, something changed in the alley that had been filled with nothing but silence.

*Whoosh! Crack!*

Three streaks of light flew toward Jongni Chu’s vital points.

At the same time, a small masked figure shot into the air. His steps as he ran along the wall were swift and stealthy as the wind.

He possessed outstanding movement techniques—and a concealment technique that surpassed even them. Just as the masked man gathered his strength to leap away—

*Thud.*

“Where are you in such a hurry to go?”

“……!”

“Come down and talk.”

An immense force weighing down on both shoulders. Breath brushing against the back of his neck.

The masked man’s falling body trembled like it had been struck by lightning.

*How can this be?!*

He had carried out hundreds of missions, but never had anything like this happened.

Overwhelming. Inescapable.

The words had never felt so real. He realized there was only one path left to him.

*Pavilion Master, it seems this is as far as I go.*

The face of his superior, whom he had served loyally for decades, the Thousand-Faced Fox, flashed before his eyes.

Just as Shadow Killer—the Hidden Shadow Pavilion’s finest agent, whose name had since been forgotten—was about to bite down on the poison pellet hidden in his tooth—

“As expected of the Hidden Shadow Pavilion. No hesitation at all. But…”

*Tap, tap.*

Lightning-fast fingers struck Shadow Killer’s entire body. A low voice burrowed into his ears as his body stiffened.

“You should have known who you were pursuing.”

Along with a feeling of utter despair, Shadow Killer’s consciousness was dragged into the abyss.
## Chapter artifact 252

# Chapter 252

One day, two days, three days.

As time passed, the tournament bracket grew smaller. The more than five hundred participants who had filled the first day of the main event had dwindled to barely ten.

And along with the crowd’s rising excitement, one man’s mood was soaring higher and higher.

“This old man was thinking it over…”

The Fire King, Jeok Cheongang, continued in a solemn voice.

“I’m beginning to think our sect’s martial arts really are the greatest under heaven. What does everyone think?”

“……”

The people seated at the head table had to struggle to keep their expressions from crumpling.

It was hardly the first time he had said something like that. They had fully expected it, but that did not make it sting any less.

What was even more infuriating was that they could not refute him.

That they could not risk offending the Fire King was one thing. The performance of his disciple, the Sleeping Dragon of Shanxi, had been nothing short of astonishing.

He had caused a tremendous stir from the preliminaries onward, then continued advancing triumphantly while displaying overwhelming skill against one renowned master after another.

Yesterday, he had even beaten the Hebei Peng Family’s Hunyuan Saber as mercilessly as a dog marked for slaughter.

*Damn old man. He couldn’t even wait before bragging again.*

*The greatest martial arts under heaven, my ass. All he did was raise one talented brat well.*

*Still, the kid’s the real deal. Where did he find such a monster?*

Their thoughts were written plainly across their faces. Under normal circumstances, Jeok Cheongang would have threatened them for failing to control their expressions.

But right now, he was the very image of a benevolent Buddha.

He smiled contentedly as he looked around, then his gaze stopped on one man.

“Hey, Virility Saber King.”

“……”

The enormous old man, the Thunderbolt Saber King, pretended not to hear and stared at a distant mountain. His face had turned bright red.

“When someone calls you, you should answer. I’m three years older than you, too. Don’t you agree?”

“……Shut your mouth while I’m asking nicely.”

“Oh, come now. Why are you so angry?”

Jeok Cheongang responded slyly, widening his eyes in feigned surprise.

“Is it because that eldest grandson of yours—the one you praised until your mouth went dry, calling him the greatest prodigy in Hebei or whatever—was beaten for fifteen minutes by my disciple?”

“……!”

“Good grief. Haven’t you heard the saying that victory and defeat are simply part of war? Why get so worked up over it?”

Only then did the Thunderbolt Saber King, who had been snorting furiously, slowly turn his gaze toward Jeok Cheongang.

“Th-That’s right. There are times you win and times you lose.”

“Exactly. That’s how it is at that age.”

“You’re finally saying something sensible. Since we’re on the subject, my grandson was exhausted from traveling such a long distance. That’s why he couldn’t display his full strength.”

Jeok Cheongang smiled kindly and nodded.

“I understand. When someone’s martial arts are lacking, they need an excuse.”

“……What did you say?”

“Come to think of it, you aren’t even the same age. Your eldest grandson is over thirty, isn’t he? Our Taekyung is only twenty-two. Heh heh, it can happen. It can.”

“Y-You old bastard!”

“Hm? What was that? I can’t hear you very well. You’re the Grand Family Head of the Hebei Peng Family who was eliminated in the quarterfinals, after all. Hahahaha!”

The Thunderbolt Saber King’s eyes rolled back as he started to surge to his feet.

A hand holding a string of prayer beads blocked him.

The Dharma King, Hong Dao, sighed as he looked at the two men.

“Amitabha. The two of you should act your age. Have you forgotten where you are?”

This was the dueling arena of the Star-Array Grand Banquet, with thousands upon thousands of spectators watching.

Only then did the Thunderbolt Saber King notice the curious gazes pouring toward the head table. He lowered himself back into his seat.

“Urgh.”

“Benefactor Jeok, what about you?”

Jeok Cheongang stared at Hong Dao for a moment, then gave a small nod.

“……Fine. I understand.”

“Good. All of you should get along. What will you do when I’m not around?”

“What will I do? I’ll break that old man’s nose.”

Despite the Thunderbolt Saber King’s taunt, Jeok Cheongang did not react.

After giving Hong Dao a sidelong glance, he merely looked toward the dueling arena with a heavy expression.

One thing Hong Dao had said before continued to echo in his mind.



*“I intend to step down after this Star-Array Grand Banquet.”*



His old friend was preparing for death.

Had he said he had, at most, another year to live? Hong Dao could no longer read the heavenly patterns as clearly as before, but if the Dharma King said it was so, then it was so.

*You bald-headed bastard. You should live another ten years at least.*

Even when Jin Taekyung’s victories lifted his spirits, thinking about Hong Dao quickly weighed them down again.

Just as they were now.

Sensing the change in Jeok Cheongang’s mood, Hong Dao suddenly spoke.

“In any case, there have been unusually many upsets at this Star-Array Grand Banquet. Wouldn’t you agree?”

“The Abbot is right.”

“None of us expected these results.”

The Sect Leaders seated at the head table nodded.

“The Sleeping Dragon of Shanxi goes without saying…”

At the mention of Jin Taekyung, the muscles in Jin Wikyung’s face twitched from his seat at the lower end of the table.

He had remained silent only because his age and standing in the martial world were still insufficient. If he had been given the chance, he would have stood up long ago and performed a happy dance.

The Sect Leaders looked at him with undisguised envy and continued.

“But the most unexpected upsets were the Life-Sustaining Sword—or rather, the Always-Victorious Sword—and the Invincible Divine Sword.”

“Ah, yes. Those two surprised me the most as well.”

What kind of place was the Star-Array Grand Banquet?

It was a gathering attended by countless young and renowned martial artists from every corner of the world.

Yet the Always-Victorious Sword and the Invincible Divine Sword were not disciples of any famous major sect, nor had either of them ever made a name for themselves.

The fact that they had remained in the bracket until now was even more surprising than Jin Taekyung’s advancement. After all, Taekyung was both the Fire King’s disciple and a member of the Jin Family of Taiyuan.

“The Invincible Divine Sword is particularly impressive. He seems capable of standing against even an Elder of our sect.”

At the words of one of the Sect Leaders from a mid-sized sect, Jeok Cheongang, who had been quietly listening, suddenly spoke.

“Keep your mouth shut. At least then you might pass for average.”

“……Excuse me?”

“I don’t know what sect you belong to or who you are, but that child is already far beyond the level of a young prodigy. Are you truly unable to guess, or are you pretending not to know even though you do?”

Hong Dao and the Thunderbolt Saber King also chuckled in agreement.

“Benefactor Jeok’s words are harsh, but he is right.”

“I hate agreeing with that old man, but he’s right. It may only be natural. The Sword… Ahem. Anyway, the kid is incredible.”

The Thunderbolt Saber King trailed off and glanced sidelong at someone.

It was a middle-aged man with a gentle smile—the Sect Leader of Huashan, the Heavenly Sword True Person.

“Hahaha. It seems even I cannot deceive the eyes of my Senior predecessors.”

At the Heavenly Sword True Person’s ringing laughter, the others asked in voices filled with suspicion,

“Could it be?”

“That’s right. The Invincible Divine Sword is a disciple of our sect.”

“Ah, I knew it!”

“You have an outstanding disciple, True Person.”

A few of the stronger martial artists nodded silently, as though they had already guessed the truth. Others exclaimed in astonishment.

But an even more shocking statement soon passed the Heavenly Sword True Person’s lips.

“Not a disciple. He is my junior brother.”

“Th-Then you mean…”

“Through a twist of fate, we came to serve the same master. The last time I saw him was more than ten years ago…but it pleases me to see how wonderfully he has grown.”

The same master.

No one properly heard what followed. Not a single person present was unaware that the Heavenly Sword True Person’s master was the Sword Saint, Mae Jonghak.

*The Invincible Divine Sword is the Sword Saint’s disciple?*

As the people around him were swept up in shock, the Heavenly Sword True Person merely smiled in silence.

The sight made him resemble a Daoist who had attained enlightenment.

His thoughts, however, were very different.

*I finally caught you, you little punk!*

After his master, the Sword Saint, even his youngest junior brother had run away.

A year ago, he had thought he had finally caught up with him, only for the boy to beat down his disciples and flee again.

Every time the Invincible Divine Sword stepped onto the dueling platform, the Heavenly Sword True Person had to suppress the urge to grab him by the collar and drag him back to Huashan.

“Heh heh heh. He is a treasure of our Huashan.”

The Heavenly Sword True Person concealed his true feelings and smiled like an immortal. Congratulations poured toward him.

“What a tremendous occasion. The Sword Saint’s name will remain in Huashan even in the next generation.”

“Congratulations, True Person.”

“Congratulations!”

“A duel between the Sleeping Dragon of Shanxi and the Invincible Divine Sword. The finals will be even more exciting now. Hahaha!”

Amid the warm atmosphere, a wrinkle formed between Jeok Cheongang’s brows.

At the same time, a strand of Sound Transmission reached Hong Dao’s ear.

—Everyone is forgetting one person.

Hong Dao quietly rolled his prayer beads.

—You mean Jongni Chu, the Always-Victorious Sword?

—That’s right. Him.

The Star-Array Grand Banquet was a gathering of the martial world where anyone could participate regardless of background or affiliation. As a result, participants did not have to undergo a particularly detailed verification process before applying.

But that was only how it appeared from the outside. The reality was different.

—I mobilized the Hidden Shadow Pavilion to investigate the identities of every participant who advanced to the main event.

A year ago, when Hong Dao first sensed the existence of Dark Heaven, the first person he sought out was the Thousand-Faced Fox, Song Ho.

After hearing the circumstances, Song Ho summoned his former subordinates without hesitation. The Hidden Shadow Pavilion, which had been reduced to nothing but a name, was reborn.

—And the result?

—The result was the same no matter how many times we checked. Everyone’s identity checked out except for one person. We could find no trace of the Always-Victorious Sword, Jongni Chu, anywhere.

—Are you certain? If he had concealed himself thoroughly for some reason…

—It was only a suspicion. At least, it was until contact with Shadow Killer was lost three days ago.

—Shadow Killer? You mean someone got to him?

Shadow Killer was an extraordinary figure, impressive enough that even Jeok Cheongang knew of him.

He was the Hidden Shadow Pavilion’s finest intelligence agent, and as an assassin, he had reached the Supreme Peak.

The fact that contact with him had been lost meant—

It was not difficult to imagine Shadow Killer as a cold corpse by now.

—What do you think? Can you identify his martial arts?

Hong Dao’s Sound Transmission caused Jeok Cheongang’s gaze to deepen.

—I don’t know either. That is the greatest mystery.

He had seen countless martial arts throughout his life.

He had watched them with his own eyes and even fought against and overcome them personally.

But the martial arts Jongni Chu displayed were utterly unfamiliar to Jeok Cheongang.

—His martial arts don’t even seem particularly powerful…and yet he has somehow won every time and made it this far. His martial arts are unlike anything I’ve ever seen.

—Then are you saying his martial arts defy common principles?

—Defy common principles?

Jeok Cheongang’s face hardened.

Decades ago, saying that something defied common principles meant only one thing.

*The Demonic Path!*

At the same time, the same word crossed both men’s minds.

Hong Dao and Jeok Cheongang had lived through an age of war. They understood its meaning better than anyone.

—Then are you saying he is a descendant of the Demonic Cult?

—I don’t know. Whether he belongs to Dark Heaven, the Demonic Cult, or something else entirely.

Just as the two men finished their Sound Transmission with grim expressions, a shout filled with internal energy shook the dueling arena.

* * *

“Martial artists of the world, allow me to introduce the rising young master, the Invincible Divine Sword—and Wudang’s Willow-Cloud Divine Dragon!”

The Invincible Divine Sword—or rather, Cheongpung—looked especially excited as he climbed onto the dueling platform.

He hopped up and down in place, waving his hands at the thunderous cheers directed toward him.

“Wow! Woooow! Hello! This is my first time reaching the quarterfinals at the Star-Array Grand Banquet!”

His opponent, the Willow-Cloud Divine Dragon, was warming up with a stiff expression.

He was one of the Ten Dragons and Phoenixes, considered one of the leading young prodigies of orthodox Murim. Along with Jin Mukyung, he was said to rank at the very top.

*He’s definitely strong.*

Not only was he over thirty, he was also the direct disciple of the Wudang Sect Leader.

According to Zhuge Gyun, he had long since accumulated considerable real-combat experience on a journey of duels.

But still.

*Well, you never know how a duel will turn out.*

I leaned back comfortably in the spectator stands.

Only yesterday, I had crushed the Lesser Family Head of the Hebei Peng Family as Jeok Cheongang had wished and advanced to the semifinals.

Unless there was a major upset, I would make it to the finals without much trouble.

And my opponent there would likely be Cheongpung.

*Let’s see what you can do.*

At the same moment my eyes began to shine, the flag signaling the start of the duel rose.
## Chapter artifact 253

# Chapter 253

Whoosh!

There was no opening stance or anything of the sort. The instant the flag signaling the start of the duel rose, the two combatants charged at each other.

And the moment the distance of more than ten zhang vanished in an instant, a dazzling beam of light surged up from the Willow-Cloud Divine Dragon’s waist.

*Sword Energy from the very start?*

Everything had its advantages and disadvantages.

Sword Energy wielded tremendous power, but it consumed an extreme amount of internal energy.

The Willow-Cloud Divine Dragon had chosen to finish this duel quickly rather than fight a battle of attrition.

Whoosh!

Blue energy spilled from his Pine-Pattern Ancient Sword and slashed down toward Cheongpung’s shoulder.

It was a clean strike without any unnecessary movement. It was probably a trajectory he had swung countless times since the day he first picked up a sword.

But…

*If I can see it, then Cheongpung can see it too.*

Boom!

Cheongpung had dodged it by exactly half a step. The Pine-Pattern Ancient Sword, wrapped in blue Sword Energy, crashed into the dueling platform.

But the Willow-Cloud Divine Dragon was a Peak master with extensive experience. As though he had anticipated this, he twisted his sword and swept it toward Cheongpung’s ankle.

“Oops!”

Whoosh! Whoosh-whoosh-whoosh!

With a playful cry, Cheongpung evaded the sword and twisted his body.

The Sword Energy raked and split the air in every direction like the claws of a wild beast. The loose hem of his robe caught in its path was shredded into tatters and scattered through the air.

Screams and gasps rose from the crowd.

“Eek!”

“Gasp!”

But I could see it clearly. Cheongpung’s body had not suffered so much as a scratch, and a smile hung around his lips.

He was enjoying himself. Moving lightly as though dancing, Cheongpung escaped the sword strikes, then broke into a wide grin and clapped.

“Wow! That was the Great Clarity Sword Technique, right?”

“Y-Yes.”

The Willow-Cloud Divine Dragon answered reflexively, his face blank with bewilderment.

And who could blame him? Anyone would have reacted the same way. *What was that? How did that bastard dodge just now?* His head was surely filled with thoughts like that.

“The sword path is really interesting. Have you perhaps not learned the Taiji Wisdom Sword?”

“Why would you ask that…?”

“I’ve always wanted to see the Taiji Wisdom Sword. My grandfa—no, someone I know praised it a few times. He said it was an excellent martial art.”

The Taiji Wisdom Sword was Wudang’s greatest secret art, famous enough that even I had heard of it a few times.

Cheongpung had spoken with pure intentions, but to anyone unfamiliar with his personality, his words were unbearably rude.

The Willow-Cloud Divine Dragon standing before him was no exception.

“Our sect’s martial arts do not exist to be evaluated, nor do they exist to entertain you.”

The Willow-Cloud Divine Dragon spoke with a stiff expression and raised his Pine-Pattern Ancient Sword to point it at Cheongpung.

“But if you desire it so badly, I will show it to you. Then you will understand how fearsome this martial art is.”

A gentle yet powerful aura rose and pressed down on everything around them. At the same time, the tip of his sword moved slowly, drawing a circle.

Taiji—the essence of Wudang’s martial arts—was about to unfold through his hands.

“The Taiji Wisdom Sword! It’s the Taiji Wisdom Sword!”

“Give it everything you have. Otherwise, you will regret it.”

Whoosh!

As soon as he finished speaking, the Willow-Cloud Divine Dragon’s figure vanished like an illusion.

The next moment, blue Sword Energy rippled through the air and aimed at Cheongpung’s upper body.

That was when Cheongpung’s sword, which had not been drawn even once since the duel began, finally appeared.

Screeeeeech—boom!

Sword Energy collided with Sword Energy. It was only a single clash, but who held the advantage was obvious.

The Willow-Cloud Divine Dragon slid back a full zhang and opened his eyes wide. Blood flowed from his torn palm.

“W-What is this?”

“Can I go this time?”

With those words, Cheongpung’s figure scattered like an illusion.

The Dark Fragrance Drift of Huashan. It was the exact movement I had grown sick of watching during my duels with him in the past.

A year had passed, and his Dark Fragrance Drift had become even more secretive and faster.

Whoosh!

A faint violet aura clung to the tip of the sword as it swept toward the crown of the Willow-Cloud Divine Dragon’s head.

He avoided attacks as much as possible, and only used Sword Energy at the exact moment of striking.

It was proof that he was reducing unnecessary expenditure of internal energy while controlling his own power perfectly.

“Gah!”

The Willow-Cloud Divine Dragon, startled, hurriedly knocked his sword upward. But this time, things were different from before. The Pine-Pattern Ancient Sword slid along Cheongpung’s blade and changed direction.

Softness overcoming hardness.

That was the foundation of Wudang’s martial arts and the principle contained within the Taiji Wisdom Sword.

But…

“Oh, I know how to do something similar, too.”

Sshk.

As he spoke innocently, Cheongpung’s wrist rotated fluidly.

The Pine-Pattern Ancient Sword had clung stubbornly to Cheongpung’s blade, pressing down on it. But it was knocked away helplessly in a single motion.

For an instant, the Pine-Pattern Ancient Sword wavered in midair, and Cheongpung’s sword ensnared it.

“Got it. This is how you do it, right?”

“……!”

“Or not? Wait, I think it’ll work better if I do this. Ah, this is it.”

Cheongpung suddenly withdrew his sword and fell into deep thought. Then he smiled brightly.

In contrast, the Willow-Cloud Divine Dragon stared at him in utter shock.

The martial artists watching the duel were no different.

“Gah!”

“H-He used the Taiji Wisdom Sword!”

Strength was overcome by greater strength. Softness was overcome by even greater softness.

The shock was immense. Cheongpung had defeated the Taiji Wisdom Sword—the greatest supreme technique of Wudang, whose martial arts were founded on the principle of softness overcoming hardness—with that very same principle.

*Cheongpung is one move ahead of the Willow-Cloud Divine Dragon. No, at least two moves ahead.*

There was no way the Willow-Cloud Divine Dragon, who was facing him directly, had failed to realize that.

“H-How did you do that?”

“Hmm. You just have to think of embracing your opponent. Then your body reacts on its own, and you know where and how to move. It’s easy, right?”

“……”

*Easy, my ass. You crazy bastard.*

No, more importantly, could someone really do that?

*This is the guy who supposedly spent a whole year eating nothing but dumplings.*

As I stared at Cheongpung in disbelief, the Willow-Cloud Divine Dragon’s eyelids trembled from the shock.

Then he suddenly charged at Cheongpung.

Tzzzz!

Blue Sword Energy blazed more brightly than ever before. There was no doubt he had gathered all his internal energy into that one strike.

The blade approached as though it would split Cheongpung’s chest open at any moment. Just as the spectators began screaming at the sight of Cheongpung standing there blankly—

Whoosh-whoosh-whoosh-whoosh!

Vivid violet light-flames filled the dueling arena. The sword in Cheongpung’s hand drew a beautiful arc.

From that single movement, I knew exactly what martial art Cheongpung was using.

*The Thirty-Six Plum Blossom Swords.*

It was impossibly fast and smooth.

For a moment, it seemed as though the scent of plum blossoms brushed the tip of my nose. The violet Sword Energy of the Zaha Divine Technique burst like flower buds and bloomed into thirty-six plum blossoms.

And then, the Willow-Cloud Divine Dragon’s Pine-Pattern Ancient Sword stopped dead in front of Cheongpung’s chest.

Crack.

The Sword Energy that had poured forth in torrents only moments ago was nowhere to be seen. Hairline cracks spread across the straight, snow-white blade like a spiderweb.

A powerless voice escaped the Willow-Cloud Divine Dragon’s lips as he stared at his beloved sword.

“Plum blossoms… I see. You are a disciple of Huashan.”

Cheongpung jumped in surprise and stammered.

“Ah, I’m not.”

“Well, I suppose that hardly matters.”

Resignation, followed by understanding.

The Willow-Cloud Divine Dragon’s arm slowly lowered toward the ground. The Pine-Pattern Ancient Sword shattered into hundreds of fragments and tumbled across the dueling platform.

“I concede.”

Only then did the silence finally break.

The judge came to his senses and lowered the flag. Like a dam bursting after being blocked, the tremendous roar of the crowd swept through the arena from every direction.

* * *

“How was I? I did well, right?”

I came back to myself at the sound of the innocent voice. Cheongpung had thrust his face right in front of mine, his eyes sparkling like a child’s.

“Whoa, you scared me. Let’s try to stop doing things like that.”

“Benefactor, I asked how I did.”

Was this really the same person who had just fought?

The Invincible Divine Sword had crushed the Willow-Cloud Divine Dragon—one of the Ten Dragons and Phoenixes and the future of Wudang—in the most literal sense.

And watching this duel had made me realize once again that Cheongpung had long since surpassed the realm of young prodigies.

*Was he always this strong?*

Once you climbed to a high vantage point, you could see more of the landscape. The same was true of the mountain called Cheongpung. This was a view I had been unable to see a year ago.

*He’s incredible. It’s hard to believe all of that comes purely from natural talent.*

His martial prowess was astonishing, but his talent was even more so.

Watching him, one could almost suspect that Cheongpung was a System user.

“Benefactor. Why aren’t you answering?”

“Are you a child? Do I have to praise you for even something like that?”

Cheongpung muttered with a slightly downcast expression.

“Grandfather always told me I did well…”

“That’s your problem.”

It was then that I deliberately answered him curtly.

“Hey, I watched your duel. Great job, friend!”

At the sudden voice that seemed to leap out of nowhere, Cheongpung turned around with a brightened expression.

“Jongni Chu!”

“Oh! You remember me, friend!”

“Of course I remember you. Of course I do—uh, yeah, of course!”

“……”

*What a pair of idiots.*

I quietly watched Jongni Chu and Cheongpung embrace and laugh together. Then a thought suddenly occurred to me, and I opened my mouth.

“Wait. You two.”

“Hm? What is it?”

“Why?”

“Aren’t you two each other’s next opponents?”

The two of them stared blankly at each other, then both gasped.

“T-That’s right!”

“I-I see. You’re my next opponent, Kang Pung.”

I could already hear the sound of their friendship cracking.

I clicked my tongue as the two of them awkwardly pulled away from one another.

*Well, the result is more or less obvious anyway.*

As with everything else, luck played a part in the Star-Array Grand Banquet. In that regard, Jongni Chu was a man born under an extraordinarily lucky star.

For some reason, he had kept facing middling opponents and climbed all the way to the semifinals.

Of course, the opponents he had defeated so far only seemed middling to me. They were comparable to Jongni Chu, or even stronger.

*And apparently, he even received a bye yesterday.*

From what I had heard, Jongni Chu’s quarterfinal opponent had suffered a severe injury and withdrawn.

If nothing else, the bastard had luck to spare.

*Still, making it to the semifinals is no small feat.*

Cheongpung was not an opponent anyone could defeat through luck. Perhaps they knew that themselves, because they exchanged a few words with troubled expressions.

“Sorry. I’ll go easy on you. No, wait—sorry, pal. I’ll go easy on you.”

“If you would do that, I would be grateful. I truly ask it of you.”

One of them openly promised to go easy, while the other thanked him without even a shred of pride. Neither of them was in his right mind.

I shook my head at the sight of them and spoke.

“You two childhood friends can resolve that matter yourselves. I’m leaving now. I have a prior engagement.”

“A prior engagement? But Benefactor, you don’t have any friends.”

“What? Did you have any friends besides me?”

“……”

It was sadder that I could not deny it.

Just as I was at a loss for words, the judge’s shout, amplified by internal energy, rang throughout the arena.

“Sleeping Dragon of Shanxi, Jin Taekyung! Come up to the dueling platform!”

“Yes. I’m coming.”

Cheongpung and I each had one more step to climb before we could face each other in the finals.

I stepped onto the dueling platform with light footsteps and looked at my opponent.

“You’re lucky too. I never expected you to make it this far.”

My opponent in the semifinal muttered in a gloomy voice.

“Our sect’s Eighteen Dragon-Subduing Palms is one of the five greatest palm techniques under heaven.”

“But you’ve only learned five stages.”

“That is correct.”

“Then you can concede.”

“If I did, my Master would beat me like a dog on the hottest day of summer.”

“Then?”

“There’s only one path left.”

Gung Gibang, the Successor Beggar of the Beggars’ Sect, spat out a thick wad of phlegm. He pointed a well-worn bamboo staff at me and continued.

“Our sect’s Dog-Beating Staff Technique is the greatest under heaven. I’ll beat you senseless like a dog in a back alley.”

“Sure. Go ahead.”

And exactly fifteen minutes later, Gung Gibang, his eyes swollen and puffy, clung to my calf and shouted,

“I’ve only learned five stages of the Dog-Beating Staff Technique!”

“……”

*This bastard has stopped at five stages in everything.*

As I tossed away the bamboo staff split in two, the judge lowered the flag.

“Sleeping Dragon of Shanxi, Jin Taekyung advances to the finals!”
## Chapter artifact 254

# Chapter 254

“Sleeping Dragon of Shanxi, Jin Taekyung, wins!”

At the judge’s shout, tens of thousands of spectators rose to their feet as one.

As Jin Taekyung came down from the dueling platform beneath a storm of cheers and applause, the eyes of the man watching him were sunk deep in thought.

*What a strange fellow.*

The Dog-Beating Staff Technique was the Beggars’ Sect’s greatest secret art, one that could only be taught to someone who had become the Successor Beggar.

Despite its comical name, its power and the subtlety of its forms ranked among the top ten martial arts in the world.

And yet Jin Taekyung had countered it far too easily without using any particularly notable martial art.

He had smashed apart a bamboo staff infused with internal energy using his bare fist, and even after taking the Eighteen Dragon-Subduing Palms head-on, all he did was frown.

He had even seemed to deliberately take attacks he could have avoided. No, that had undoubtedly been his intention.

*Why?*

At first, Jongni Chu wondered if Taekyung was some kind of oddball who enjoyed pain, but judging by the agonized faces he made every time, apparently not.

Besides, what kind of lunatic would take the Dog-Beating Staff Technique head-on just to raise his Toughness?

*Regardless, he’s interesting.*

Jongni Chu still could not forget the surprise he had felt when he first saw Jin Taekyung.

His Muscles and Bones were seemingly bestowed by heaven itself. If there was such a thing as the Heavenly Martial Physique, surely this was it.

*A Disciple of the Fire King… I’ll have to keep a close eye on him.*

With that final thought, Jongni Chu, the Always-Victorious Sword, turned away and blended into the cheering crowd.

And there were eyes following his back.

A merchant with a generous belly, a hunched old man, a Third Rate martial artist and a wandering martial artist dressed in cheap martial-arts uniforms…

They all had ordinary faces one could see anywhere.

Yet whenever their lips moved, Sound Transmission passed between them—a technique only Peak masters could use.

—Pavilion Master, your orders.

—Two and Three will follow him. Keep watch from a hundred zhang away.

—We might lose track of him.

—I know. But this is the best option.

—…Understood.

—Four and Five, keep an eye on Jin Taekyung and Cheongpung. If he approaches again, report it immediately.

—Yes, sir.

—Then I wish you all good martial fortune.

The brief conversation ended, and no answer came back. The ordinary-looking faces continued walking casually until they disappeared into the crowd.

Meanwhile, a middle-aged beggar who had been sitting on the street begging for alms continued bowing low as people tossed him small change. After a while, he got to his feet.

The transformation began in a deserted alley.

Crack. Sssrk.

His hunched shoulders straightened, and his twisted spine became perfectly erect. Then his facial muscles began to quiver as if kneaded by invisible hands.

Before he had walked ten steps, the middle-aged beggar had become a genial-looking old man.

Tap. Tap.

A wooden prosthetic leg made of ebony, hard as steel, struck the stone pavement.

*Jongni Chu, the Always-Victorious Sword.*

The old man, Song Ho, the Thousand-Faced Fox, repeated the name in his mind.

Before he was the Pavilion Master of the Hidden Shadow Pavilion, he was also an intelligence operative and a master of disguise.

He never forgot a face he had seen even once, and he could identify a person by the smallest habits or the structure of their bones. Even if someone used disguise arts, they could not escape his eyes.

But there was one exception: Jongni Chu.

*I’ve definitely crossed paths with that bastard before.*

But when? And where?

Song Ho had been sunk deep in thought as he recalled Jongni Chu’s face when pain shot through his leg and brought him to a halt.

*It’s starting again. It’s been getting worse lately.*

It was a truly old injury.

Decades ago, in his youth, he had taken part in the final battle against the Demonic Cult and lost one of his legs.

He had barely survived after countless twists and turns, but the memory of that day was etched deep in his mind like a brand.

So was the voice of one man, deep and dark as a bottomless abyss.

*Thousand-Faced Fox Song Ho. You’re quite a large fox, aren’t you? Shall I start by tearing off a leg?*

Song Ho shuddered all over, endured the pain, and started walking again.

It was a past that no longer left even a trace. He needed to focus on the present, whose substance was far more tangible.

*Jongni Chu… who are you? And what are you plotting?*

He had already finished making every possible preparation. Even so, the unease lingering in his chest kept shaking him.

*Am I getting old? Or has peace lasted too long?*

A quiet sigh escaped the old man’s lips.

* * *

I closed my eyes.

In the darkness, I pictured one person: a boyish face that always wore a bright smile and an ordinary frame.

But the moment he drew his sword, everything changed.

Whoosh!

Even if it could not be seen, I could see it. Even if it could not be heard, I could hear it.

Violet Sword Energy shot out, flawlessly covering all thirty-six directions.

It was as fast as a ray of light and as soft as drifting flower petals. As I watched that beautiful sight, I thought,

*The Flame-Extinguishing Divine Fist, the Flame Divine Palm, or…*

Several other martial arts flashed into my mind before disappearing again.

Cheongpung was an opponent I had to face with everything I had. In the end, there was only one answer. It was just as I gripped the cool shaft of my spear after a brief moment of thought.

Creak.

“Captain. Captain.”

The voice boring into my ear shattered my thoughts. Cheongpung and the illusory Sword Energy he had conjured vanished as if washed away.

When I lifted my eyelids, I saw Hyuk Mujin poking his head through the crack in the door.

“Hehe. I’m here.”

I stared at him for a moment before speaking.

“What are you doing here?”

“I came to keep you company in case you were lonely.”

“Company?”

“Yes. Isn’t that thoughtful of me?”

“Thoughtful?”

With a deep sigh, I pulled off one of the chair legs.

“Get down on your stomach, you despicable bastard.”

“W-Why are you doing this?”

“Did Cheongpung send you to interfere with my training?”

“Gasp! You were training?”

“Then do you see people sitting cross-legged and falling asleep?”

Mujin glanced around nervously before speaking hesitantly.

“I heard that when you were young, you tried to practice Horse Stance while sitting in a chair.”

“That wasn’t me… Wait. Are you talking back to me?”

“What? Am I not even allowed to talk back?”

What the hell? Had this guy gone crazy?

I stared at Hyuk Mujin in bewilderment. In the past, he would have quickly covered his head, but after flinching for an instant, he thrust out his chest.

“What are you doing?”

“Since we’re on the subject, I believe I’ve made no small contribution while serving you, Captain.”

“So?”

“Treat me accordingly.”

“What kind of treatment? The four mandatory insurances? Workers’ comp if you get hurt from now on?”[^1]

“I don’t really know what the four mandatory insurances or workers’ comp are. But if you keep doing this, I’m just going to quit everything and take over the textile shop.”

After thinking it over, I nodded.

“Go ahead, then.”

“Pardon?”

“Good work. No—thank you for your hard work, Mr. Mujin. May your textile shop prosper from here on out.”

“Wait, wait a moment.”

“Oh, right. I don’t know about the other locations, but prepare to close the main branch in Shanxi Province.”

Grab!

Hyuk Mujin wrapped his arms around my calf and spoke with an imploring look in his eyes.

“I misspoke.”

“Did you?”

“Yes. Please hit me once on the back of the head.”

“Didn’t you ask me to treat you accordingly?”

“No. I’ve become a man who can’t live even a day without your blows.”

“…”

Had he gone insane?

I shook my head and lightly tapped him on the forehead.

“Enough nonsense. Get to the point. Why are you here?”

“The thing is, I really did come to keep you company.”

“What?”

When I fixed him with a hard stare, Mujin’s voice shrank even further.

“I thought you might be feeling pressured since the final is tomorrow…”

“The opponent hasn’t even been decided yet. Don’t you know today is the last day of the semifinals?”

The sun was beginning to set, so Jongni Chu and Cheongpung’s duel would start soon.

The winner would be my opponent in the final, and barring some massive upset, Cheongpung’s victory was certain.

Mujin shrugged at my words.

“I know. I just stopped by.”

“What a silly guy. Use this time to train, you idiot.”

That was what I said, but a corner of my heart felt strangely warm. Come to think of it, that Mujin had gone through a lot while following me around.

Maybe his occasional deranged behavior was because my repeated smashes to the back of his head had destroyed too many of his brain cells.

*Now that I think about it, I feel bad.*

I was resolving to treat him better from then on when Mujin asked,

“Young Hero Cheongpung will win, right?”

“Of course he will… Wait. How do you know that?”

“Even if no one else does, I need to know. With that ridiculous epithet, Invincible Divine Sword, his name being Kang Pung, and the fact that he used the Zaha Divine Technique in his last duel, how could I not?”

“You’re smarter than I thought.”

“Rumors have been spreading here and there. Cheongpung isn’t well known, so most people only know him as a disciple of Huashan, though.”

He had a point. The Zaha Divine Technique was distinctive enough that anyone could make that much of an educated guess.

“So Young Hero Cheongpung is definitely going to win, right?”

“Isn’t that obvious?”

“It has to be certain. Absolutely!”

What was with that greedy look in his eyes?

The moment I nodded uneasily—

“Waaaaah!”

A roar echoed from not far away.

I picked up the spear resting beside me, White Flame, and got to my feet.

*Cheongpung is the one who’ll be advancing anyway. That fact won’t change.*

This was an obvious battle between an egg and a rock.

But watching how the egg collided with the rock, and how the rock shattered the egg, would be a great help in the final duel.

“What are you doing? Aren’t you getting up?”

“Yes, sir.”

* * *

“Life-Sustaining Sword!”

“I bet one silver nyang on you! Turn this around!”

“Hahaha! You bet on the Life-Sustaining Sword instead of the Invincible Divine Sword? There’s no bigger sucker!”

Amid the blazing torches and the boisterous laughter, Jongni Chu was climbing onto the dueling platform when he suddenly stopped.

It was because of the gazes looking down at him from the seats of honor.

There were no fewer than three Supreme Peak masters known as the Ten Kings. He could also see the heads of the Nine Sects and One Gang and the Five Great Families, as well as Song Ho, the Thousand-Faced Fox, quietly watching from the very back with a glint in his eyes.

“Jongni Chu, the Always-Victorious Sword. Stand in the designated position.”

His pause had lasted only a moment. At the judge’s words, Jongni Chu climbed onto the dueling platform with dragging footsteps and drew his sword without hesitation.

Ssshing!

The sudden action made the surrounding crowd fall silent for an instant, but quiet snickers soon broke out.

The hilt was so clogged with dirt that its design could not even be made out, and the blade was covered in reddish rust.

A martial artist normally cherished their weapon like their own life, but Jongni Chu’s sword looked as though it had never received so much as a cleaning since the day it had been made.

“What the hell is that?”

“I thought something serious was happening. Gave me quite a start.”

“That’s why they call him the Life-Sustaining Sword. What did you expect?”

Ignoring the laughter behind him, Jongni Chu scrutinized the rusty blade and clicked his tongue.

“I can’t use this for now.”

Just then, Cheongpung, who had been excitedly waving at the crowd, held out his own sword.

“Want to borrow mine? No, would you like to use it?”

“No. You should use that.”

“I’m fine, though…”

“You’re fine? Then what will you use?”

“It doesn’t matter. We’re friends.”

When Cheongpung nodded vigorously, Jongni Chu let out a genial laugh.

“I appreciate the thought. Mine is good enough.”

“But we’re friends…”

“Listen.”

Sssrk.

The rust-red blade pointed at Cheongpung.

The torchlight flickering in Jongni Chu’s eyes had replaced the playfulness that had been there only moments before.

“I’ve never had a friend like you.”

[^1]: Korea’s four mandatory social-insurance programs cover national health insurance, national pension, employment insurance, and industrial accident compensation insurance.

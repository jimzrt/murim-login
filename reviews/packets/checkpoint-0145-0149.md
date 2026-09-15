# Checkpoint Review — 145–149

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

# Chapters 145–149

## Plot

Jin Taekyung pressures the four heirs of the Five Gates of Shanxi other than the Seongun Escort Bureau to support the Jin Family of Taiyuan, Huashan, and the government, threatening to absorb Gopyeong Sect as a Jin Family branch if necessary. He invites ten-year-old Prince Shangshan Zhu Bao to the Jin Family’s grand banquet in fifteen days and promises to obtain Jin Mukyung’s autograph, though Zhu Bao refuses Cheongpung’s autograph until Cheongpung earns a martial title.

At the luncheon’s conclusion, Zhu Bao gives Taekyung Prince Shangshan’s Token as the Quest Reward. Hong Jin then joins Taekyung’s journey to the Jin Family, sending Jin Wikyung a thousand silver nyang and arranging a large escort and delegation. Cheongpung receives the Royal Guard Armor Set and decides to stay with the Jin Family temporarily. The Five Gates’ young prodigies remain at Honghwa Inn until New Year’s Day to support the Seongun Escort Bureau. During the journey, Cheongpung reveals that he came to Huashan at age three or four and was not born there; Hong Jin discloses that he is a eunuch, formerly served the late Emperor, was assigned to Prince Shangshan, and reached the frontier in something like exile.

Wikyung prepares an extravagant, bribe-influenced welcome for Hong Jin. He and Hong Jin immediately establish a playful rapport, while Cheongpung reveals that Mae Jonghak is his grandfather and that he secretly left Huashan to defeat all the Ten Dragons and Phoenixes. He chooses Jin Mukyung as his first opponent. Cheongpung activates the Zaha Divine Technique, and his light-flames collide with Mukyung’s Sword Energy as their duel begins; the outcome is unresolved.

Meanwhile, Huashan’s Lone Crane, Baek Museong, travels with fellow Three Plum Blossom Elites Chulwoo and Eunhyang toward the Jin Family. After Chulwoo and Eunhyang cause trouble with the Black Serpent Sect in Xi’an, Baek makes them return the stolen money and jade hairpin and apologizes to the innkeeper. Huashan has been sealed since Mae Jonghak entered the sleeping Sect Leader’s quarters, left a dagger and handwritten note, and disappeared. A messenger from Shanxi prompted Huashan to dispatch the Three Elites, and Baek looks forward to seeing how Cheongpung has grown since their meeting ten years earlier.

## Continuity

- Prince Shangshan’s Token has been obtained as the completed luncheon Quest Reward; Zhu Bao is expected at the Jin Family’s grand banquet in roughly fifteen days, around New Year’s Day.
- Zhu Bao is ten years old, an exceptionally skilled young swordsman, and an admirer of Jin Taekyung. Jin Mukyung refused Zhu Bao’s autograph three years earlier; Taekyung has promised to obtain it.
- Cheongpung is a twenty-year-old Peak master, grandson and disciple of Sword Saint Mae Jonghak. He secretly left Huashan without Mae Jonghak’s knowledge and is undertaking a dueling tour against the Ten Dragons and Phoenixes.
- Cheongpung’s duel with Jin Mukyung has begun, but its outcome is unknown. Cheongpung still lacks a martial title, which Zhu Bao requires before accepting his autograph.
- Cheongpung came to Huashan at about age three or four rather than being born there. His parentage and Mae Jonghak’s statement that a crane delivered him remain unexplained.
- Mae Jonghak disappeared after entering the sleeping Huashan Sect Leader’s quarters, leaving a dagger and handwritten note. Huashan is sealed, and the search for Mae Jonghak’s hidden residence remains unresolved.
- Baek Museong is Huashan’s Lone Crane and the first of the Three Plum Blossom Elites. Chulwoo and Eunhyang are his junior disciples and fellow Elites; both are notorious troublemakers.
- Hong Jin is a eunuch who formerly served the late Emperor and has served Prince Shangshan since infancy. His circumstances of castration, exile-like transfer to the frontier, and political role remain unclear.
- Hong Jin and Jin Wikyung have formed a joking rapport. Hong Jin bribed Wikyung with one thousand silver nyang, prompting the Jin Family’s extravagant pro-imperial welcome.
- Hong Jin and Li Feng continue pursuing the Shaanxi–Shanxi trade project through Huashan, with the Seongun Escort Bureau as the proposed base. Taekyung is to relay the proposal to Jin Wikyung.
- The four non-Seongun heirs of the Five Gates will remain at Honghwa Inn until New Year’s Day while supporting Taekyung’s side.
- Gong Ilhyuk remains humiliated and vengeful; the identities of the other two members of the Three Hands of Zhongnan are unknown.
- Taekyung remains below the Peak realm and cannot use Sword Energy despite his victories over Peak masters.

## Translation Decisions

- Render **주표** as “Zhu Bao,” **상산왕** as “Prince Shangshan,” and **상산왕의 패** as “Prince Shangshan’s Token.”
- Render **고평문** as “Gopyeong Sect” and **고평지부** as “Gopyeong Branch of the Jin Family of Taiyuan.”
- Render **비무행** as “dueling tour,” **청강검** as “blue-steel sword,” and **광염** as “light-flames.”
- Render **화산일학** as “Huashan’s Lone Crane,” **매화삼절** as “Three Plum Blossom Elites,” and **매화검수** as “Plum Blossom Swordsmen.”
- Use “Senior Brother” for **대사형** and “Big Brother” for **큰 오라버니** when Eunhyang deliberately uses the familiar alternative.
- Preserve the crude eunuch misunderstanding and Cheongpung’s innocent “ball friend” joke.
- Render **금성전장** as “Golden Star Exchange,” **전표** as “bank draft,” **은자** as “silver nyang,” **철전** as “iron coins,” **은원보** as “silver yuanbao,” and **사서삼경** as “Four Books and Three Classics.”
- Continue rendering **전하** as “His Highness” formally and **왕** as “king” when used literally.

## Durable state

{
  "active_continuity": [
    "The City Lord’s luncheon attendance requirement has concluded; Prince Shangshan’s Token was obtained as the Quest Reward, and Zhu Bao is expected at the Jin Family’s grand banquet in roughly fifteen days.",
    "Zhu Bao is ten years old, has trained in martial arts daily for three years, is an exceptionally skilled young swordsman personally named Zhu Bao, and admires Jin Taekyung.",
    "Taekyung remains below the Peak realm and cannot use Sword Energy despite defeating Jopil, Jin Baekyang, and Pung Yang.",
    "Hong Jin and Li Feng are pursuing the Shaanxi–Shanxi trade project through Huashan, with Li Feng acting as intermediary and the Seongun Escort Bureau proposed as the base.",
    "Cheongpung is a twenty-year-old Peak master raised by Mae Jonghak, knows several Huashan martial arts, can use the Zaha Divine Technique, obtained the Royal Guard Armor Set, has no martial title yet, and began a duel with Jin Mukyung whose outcome is unknown.",
    "Mae Jonghak remained in deep seclusion at a hidden Huashan residence and had been there at least ten years before the luncheon; Cheongpung came to Huashan at about age three or four rather than being born there.",
    "Huashan was sealed after Mae Jonghak entered the sleeping Sect Leader’s quarters, left a dagger and handwritten letter, and disappeared; the search for his residence remains ongoing.",
    "Baek Museong is a first-generation Huashan disciple known as Huashan’s Lone Crane and the first of the Three Plum Blossom Elites; he met Cheongpung ten years ago and is traveling with the other Elites to meet him again.",
    "Chulwoo and Eunhyang are Baek Museong’s junior disciples and fellow members of the Three Plum Blossom Elites; both are notorious troublemakers who caused trouble with the Black Serpent Sect while traveling.",
    "Li Feng left Huashan after becoming discouraged by Cheongpung’s extraordinary talent, not because of his defeat by Gong Ilhyuk.",
    "The identities of the other two members of the Three Hands of Zhongnan remain unknown.",
    "Hong Jin is a eunuch who formerly served the late Emperor, was ordered to assist Prince Shangshan, has served the prince since infancy, and is the power behind the Shanxi Provincial Office.",
    "Gong Ilhyuk leaves the luncheon humiliated and vows revenge against those who rejected and insulted him.",
    "The four heirs of the Five Gates of Shanxi excluding the Seongun Escort Bureau are frightened of the Jin Family, Huashan, and the government and are being pressured to support Taekyung’s side; they will remain at Honghwa Inn until New Year’s Day.",
    "Taekyung threatened to absorb Gopyeong Sect as the Gopyeong Branch of the Jin Family of Taiyuan if its young sect leader refused to cooperate.",
    "Jin Mukyung flatly refused Zhu Bao’s autograph request three years earlier; Taekyung now promises to obtain Mukyung’s autograph for Zhu Bao at the upcoming banquet.",
    "The current Military Commissioner is incompetent, fond of bribes, and directly appointed and dismissed by the Emperor.",
    "Jin Wikyung returned to the Jin Family after nearly ten days away, faces a large administrative workload, and prefers practical people with flexible thinking over rigid scholars; Hong Jin gave him one thousand silver nyang, prompting an extravagant pro-imperial welcome and a joking rapport between them."
  ],
  "continuity_sources": [
    149
  ],
  "open_questions": [
    "What did Mae Jonghak mean by saying a crane delivered Cheongpung to him?",
    "Why did Mae Jonghak remain hidden at Huashan despite the sect eventually finding his residence?",
    "What are the names and individual identities of the other two members of the Three Hands of Zhongnan?",
    "What is the full title of the wuxia novel beginning with 군림…… that Taekyung read through volume thirty-four?",
    "Was the Emperor’s reported suspicion of his younger brother the reason Prince Shangshan was sent to Shanxi, and what danger does the imperial succession pose?",
    "What martial title will Cheongpung eventually acquire?",
    "What circumstances led Hong Jin to become a eunuch and come to the frontier in something like exile?",
    "What is the outcome of Cheongpung’s duel with Jin Mukyung?"
  ],
  "safe_through": 149,
  "temporary_decisions": [
    "Render 전하 as “His Highness” as the formal royal address and 왕 as “king” when used literally.",
    "Render 초일류 as “advanced First Rate” and 군문 as “military” when describing an affiliation.",
    "Render 풍운검군 as “Wind-and-Cloud Sword Lord” and 오촌 당숙 as “father’s cousin.”",
    "Render 태을미리장 as “Taeeul Miri Palm.”",
    "Render 후배님 and 선배님 as “Junior” and “Senior” in the Gong Ilhyuk exchange.",
    "Render 태사부 as “Grandmaster,” 사숙 as “Martial Uncle,” 자하신공 as “Zaha Divine Technique,” 근위대 as “royal guard,” and 근위대 갑옷 세트 as “Royal Guard Armor Set.”",
    "Render 비무행 as “dueling tour,” 청강검 as “blue-steel sword,” and 광염 as “light-flames.”",
    "Render 서안 as “Xi’an,” 서악 as “Western Peak,” 흑사파 as “Black Serpent Sect,” 화산일학 as “Huashan’s Lone Crane,” 매화삼절 as “Three Plum Blossom Elites,” and 매화검수 as “Plum Blossom Swordsmen.”"
  ],
  "version": 1
}

## Reading copies

## Chapter artifact 145

# Chapter 145

Hong Jin let out a quiet laugh and tilted his cup.

“Our Young Master Jin, you’re greedier than I thought.”

“I’m about as greedy as anyone else. And I have a favor to ask. Could you just call me Young Master Jin?”

“Oh my, pretending you don’t like it when you do.”

“Fucking hell…”

“Hm? What did you say just now?”

“Ah, I said it’s nice. It feels like family.”

“Family, huh? That’s nice to hear. I’m already looking forward to meeting the Lesser Family Head Jin.”

Right. No matter how much I talked in this room, the final decision would be made by Jin Wikyung and Hong Jin.

Both of them were practically professionals in this area, so it was only proper for an amateur to step aside.

“By the way, what grudge do you have against the Seongun Escort Bureau?”

“It’s not quite a grudge… I’m just giving an extra slap to someone I dislike. And it doesn’t hurt that I can pick up a few crumbs along the way.”

“Ah. Is this related to the Young Bureau Head of the Seongun Escort Bureau who was originally supposed to come?”

This man’s instincts were anything but ordinary.

Since he had already figured it out, there seemed to be no need to explain every little detail. I simply shrugged.

“Something like that. How did you know?”

“Young Master Jin, I’ve lived in the imperial palace for more than twenty years.”

“Excuse me?”

“I survived on my ability to read the room. Reading the expressions of children is easy enough.”

Hong Jin gestured with his chin toward the young prodigies of the Five Gates of Shanxi.

At the far end of a distant table, the young men and women had been sneaking glances our way with frozen expressions. They flinched and shrank back when they realized they had been noticed.

“They’ve been like that since they first came in. Carefully watching Young Master Jin’s every move.”

“Really?”

“Yes. I almost felt sorry for them just watching. What on earth did you do?”

“They had something similar happen with the people who left earlier.”

“The Three Hands of Zhongnan? Tsk, tsk. They failed to recognize who they were dealing with, didn’t they?”

As expected, Hong Jin understood everything with the slightest hint. He clicked his tongue sympathetically, while Li Feng abruptly turned his head and stared at the young prodigies.

His eyes seemed to say he would remember exactly who had provoked Martial Uncle Cheongpung.

“Gasp.”

“Assistant Military Commissioner! No, Great Hero Li! It’s not like that…”

Li Feng was not only a powerful figure in the Shanxi Province military but also a lay disciple of Huashan.

Even though the government and Murim were supposed to remain separate, getting entangled with him in the wrong way would make the future of the Five Gates of Shanxi very unpleasant.

Ignoring the young men as they hurriedly offered excuses, Li Feng asked me,

“Could you tell me more about what happened?”

“It’s all over now. The person involved even beat them himself. What more is there to say?”

“Beat them himself?”

“Ah, I mean he beat them up. Of course, they apologized before that.”

“Martial Uncle did it himself? Hmm.”

Strictly speaking, Cheongpung had only dealt with one of them, but he had beaten him all the same.

Li Feng looked at the young prodigies with a much gentler gaze.

“Do you understand what you did wrong?”

“Yes, sir!”

“We feel it in our bones!”

Their booming replies erupted immediately. It wasn’t only Li Feng’s position that had them sweating bullets. They now knew Cheongpung’s identity as well.

Putting aside the fact that he was a Peak master, he was the Disciple of the Sword Saint and Huashan’s direct Disciple.

*They’re completely screwed.*

The Five Gates of Shanxi were ultimately nothing more than a collection of minor sects. If Huashan, one of the Nine Sects and One Gang, got angry, even their extended families might get beaten with a bat.

No, they would be lucky if it ended there.

“The conversations and events that took place here today…”

Li Feng’s heavy voice had barely begun when the answers came flying out.

“We’ll keep silent!”

“We’ll take it to our graves!”

“I’ve already forgotten everything!”

“Where are we? Who am I?”

*They’re really putting on a fucking show.*

As I watched an epidemic of amnesia break out before my eyes, I added one more thing.

“Is that enough?”

“Ex-Excuse me?”

“What do you mean?”

“What do I mean? If you want to become part of the family, you need to put your spoon in too. You there. What does ‘family’ mean?”

The young prodigy I had pointed at stammered out an answer.

“People who eat together… Unless that’s not it, in which case, I’m sorry.”

“That’s right. Now, how do you become family?”

“Ah!”

The young prodigy slapped his forehead with a cry of realization.

At least that one had some sense.

“Then I’ll arrange a fine place for our next meeting. How about Honghwaru?”

“……”

What a complete idiot.

With heirs like these, the state of the Five Gates of Shanxi was obvious without even looking. I let out a deep sigh and explained it simply.

“Forget Honghwaru. I’m telling you to do whatever our side tells you to do. For example, anything involving the Seongun Escort Bureau. Understand?”

“Ohhh.”

The Jin Family of Taiyuan had certainly become the greatest power in Shanxi, but if the minor sects united and resisted, it would inevitably become a nuisance.

We belonged to the orthodox faction, after all. If we seized whatever we wanted and held people accountable like a band of mounted bandits, everyone would point fingers at us.

Wasn’t legitimacy just as important as martial arts in Murim?

*But if there’s no one left to point fingers, it won’t be a problem.*

I slowly took in the four men and women before me—the heirs of the four sects among the Five Gates of Shanxi, excluding the Seongun Escort Bureau.

If they stepped forward and sided with the Jin Family of Taiyuan, things would become much easier.

“When you’re eating, pay close attention to where you sit. That way, you can at least get a bite or two.”

The Seongun Escort Bureau was supposedly one of the most prominent powers in the province, despite being located in a frontier region. It was more than enough of a feast to share around.

At my words, the quick-witted one’s eyes quietly gleamed, while the clueless one cautiously opened his mouth.

“Even so, that might be a little…”

I cut off the dense-looking young man before he could finish.

“What sect are you from?”

“M-Me?”

“Yes, you.”

After a long hesitation, the name Gopyeong Sect finally came out.

It was a name I vaguely recognized—a minor sect so obscure that I could barely remember hearing it. That was about the extent of Gopyeong Sect’s standing.

No, that was true of all the sects in the new Five Gates of Shanxi.

“Gopyeong Sect. Gopyeong Sect… It doesn’t have a very pleasant ring to it. Should I recommend a new name?”

“Excuse me?”

I stared into his eyes as he continued to fail to understand.

“Starting next month, let’s begin again under a new name. The Gopyeong Branch of the Jin Family of Taiyuan. How does that sound?”

“……!”

“……!”

“You don’t seem to like it. I was only saying it for fun, you idiot.”

Of course, I hadn’t been saying it for fun.

I patted the deathly pale Young Sect Leader of Gopyeong Sect on the shoulder and swept my gaze across the room.

“Is anyone here sworn brothers or sisters with Woo Jintae?”

“N-No, sir.”

“Or perhaps you’ve been close friends since childhood, watching each other for more than ten years? Maybe you were betrothed before birth? There are plenty of possibilities.”

“Absolutely not! Absolutely not. We’ve only spent time together a few times.”

“I-I only received a few bolts of silk and a little jewelry…”

“Then that settles it.”

Clap!

The sharp sound of my hands coming together made the four men and women flinch.

“Choose. Are you going to make enemies of the Jin Family of Taiyuan, Huashan, and the government, or…”

I grinned and enunciated the final words clearly.

“Are you going to abandon someone you aren’t even close to and share the feast with us?”

Clap, clap, clap, clap.

This time, it wasn’t me. Hong Jin was laughing loudly and applauding.

“Our Young Master Jin, I like you more and more every time I see you.”

“……”

*Brother, please refrain from making dangerous remarks.*

* * *

“Are you leaving already?”

His tone was still arrogant, but his voice and eyes were filled with regret.

*The more I see him, the cuter he gets.*

I was about to pat the head of my little fanboy—no, Prince Shangshan Zhu Bao—when I lowered my hand under Li Feng’s gaze.

*Oh, right. He was a king. And a member of the imperial family, at that.*

“Ahem. I have some urgent business to attend to.”

“Can you not put it off until later?”

“I’m sorry, but it’s a matter where every moment counts.”

“I see…”

Looking at the dejected kid’s face made me feel a little guilty—like hell it did. I wanted to hurry back home to my family and get some proper rest.

Right then, Hong Jin cut in with his delicate voice.

“His Highness, I’m here, so please let Young Master Jin go now. All right?”

But Zhu Bao only stared at me stubbornly.

“Then when shall I be able to see you again?”

“Hmm, I don’t know. After a thousand nights?”

“A thousand nights!”

Zhu Bao cried out with a shocked expression.

That was approximately three years. For a child who was only ten years old, it must have seemed like an enormous amount of time.

“Are you truly that busy?”

“There are such things as adult matters, Your Highness.”

“Good heavens. Even my late father was never that busy…”

He seemed deeply disheartened. Zhu Bao’s head drooped, but Li Feng’s next words made him straighten up again.

“Your Highness, what do you think of this?”

“What do you mean?”

“I hear the Jin Family of Taiyuan will be holding a grand banquet in fifteen days. Why don’t you pay the Jin Family of Taiyuan a personal visit?”

“The Jin Family of Taiyuan?”

“Yes. All the masters who are famous throughout Shanxi will be gathered there, so I’m sure you’ll be pleased.”

Zhu Bao’s eyes began to sparkle.

“Of course! Why didn’t I think of that?”

“Yes, Your Highness.”

“……”

What the hell were these two talking about?

They hadn’t even been invited, yet they were spreading their wings and soaring through the realm of imagination. But if I told him not to come, it felt as though something would explode, so all I could do was nod.

“Great Hero Li is right. Come visit us then.”

“Would that really be all right?”

He was asking rather late.

I answered with a professional smile.

“Of course. My brothers will be happy to see you too.”

“Is that really true?”

“You know who my brothers are, don’t you? You should already be acquainted with my second brother.”

“Heaven Shaking Sword?”

A dark cloud suddenly fell over Zhu Bao’s bright, innocent face.

“Your second brother dislikes me. Three years ago, he only ate and left without saying a word. He was even rude.”

“He didn’t say a single word?”

“I do not wish to speak of that day anymore.”

Hong Jin whispered in a tiny voice,

“His Highness asked him for an autograph, but he flatly refused.”

Jin Mukyung had said he was invited three years ago, so…

Zhu Bao must have been seven at the time.

Good grief. How could anyone flatly refuse when a seven-year-old child—an actual king, no less—asked for his autograph?

*That man really is something.*

In a way, it was very much like Jin Mukyung.

Recalling how his fanboy enthusiasm had been so brutally crushed, Zhu Bao silently fidgeted with his fingers.

Watching him, I felt a pang of sympathy.

“If you come this time, I’ll ask him to give you his autograph.”

“Really?”

“Pinky promise. Seal it.”

I even hooked pinkies with the bewildered boy and sealed our promise.

“What is this?”

“It means I swear before the gods of heaven and earth.”

“Oh!”

Everyone around us was making a fuss because he was royalty, because he was a king, and so on. But a child was still a child.

Seeing Zhu Bao so happy that he didn’t know what to do, everyone smiled fondly.

“It’s been a long time since I’ve seen His Highness this happy.”

“I know. After dealing with that boring Assistant Military Commissioner every day, he’s smiling brightly for the first time in ages.”

“I’ve only been doing my best.”

“Doing your best doesn’t always produce the best result. It happens.”

“Deputy Military Commissioner!”

“What is it, Assistant Military Commissioner?”

Hong Jin and Li Feng.

I could never tell whether the two of them got along or hated each other as they bickered back and forth.

Meanwhile, Cheongpung approached Zhu Bao with an expectant expression.

“Can I sign something for you too?”

“……”

“You’ve never signed your name before, have you?”

“Gasp. How did you know? I’ve left my hand mark as a luggage porter before, but this is my first autograph.”

“Wouldn’t it be strange if I didn’t know?”

Just look at that eager expression. He looked desperate to give someone his very first autograph.

“C-Can I not sign one?”

“No. Do whatever you want. His Highness will be happy if you give him your autograph.”

But Zhu Bao’s reaction was unexpected.

“An autograph? Yours?”

“Yes! I really want to give you my autograph!”

“No.”

“W-Why not? They say my grandfather is a very famous man. Haven’t you heard of the Sword Saint?”

“I know. Of course I know. But…”

Zhu Bao put on a deliberately stern expression and shook his head.

“You don’t have a martial title yet, do you?”

“Excuse me?”

“Come back after you’ve acquired a cool martial title. Then I shall certainly get your autograph.”

“……”

“……”

*So this was something only named characters could do.*
## Chapter artifact 146

# Chapter 146

Every meeting must eventually end in a parting.

As the familiar six-horse carriage drew near, Zhu Bao held out something about the size of my palm.

“What is this?”

“My reward for today’s meeting.”

“Oh, you really didn’t have to…”

When I accepted it and examined it closely, I saw that it was a kind of golden medallion.

Clouds and a dragon had been delicately engraved into its surface, which flashed brilliantly in the sunlight.

*Ding.*

> **System**
>
> - The Quest target is extremely pleased with today’s meeting!
>
> - As a Quest Reward, obtained **Prince Shangshan’s Token**!

“It is my token. If there is anything else you desire or a wish you would like granted, bring this token and come find me. I shall fulfill it to the best of my ability.”

“Oh.”

A coupon for an exchange.

At a Chinese restaurant, twenty coupons would get you a large serving of sweet-and-sour pork. Since this was a coupon from Prince Shangshan, I might be able to exchange it for all kinds of elixirs or treasures.

*I do need a weapon, too.*

Thanks to absorbing the Blazing Flame Divine Pill, I had more than enough internal energy.

It was just a shame that I didn’t have a decent spear to use. As for the other weapons, I had used and discarded them from the start like disposable chopsticks.

*Should I just trade it in right now?*

I considered it for a moment, then shook my head.

The greatest dangers had already passed. Exchanging the prince’s token for a single weapon when there was no immediate need would be a waste.

“Thank you. I really wanted something like this.”

When I bowed deeply from the waist, Zhu Bao rose onto his tiptoes and gently ruffled my hair.

“I am happy that you like it.”

“……”

This felt really strange. I’d let it slide because he was cute.

In the meantime, the carriage that would take us home came to a stop. As I was about to climb aboard, Zhu Bao waved at me.

“Take care! Come again!”

*Next time, you should come to me, you little punk.*

There were only a little over two weeks left until New Year’s Day. I would probably be able to see the young prince again around then.

“Then, I shall take my leave.”

“I’ll return, Your Highness.”

The carriage was so large that its entrance was wide as well. Hong Jin and I climbed aboard side by side.

“……Hm?”

Wait a minute. That had been so natural that I’d almost let it pass.

I stared at Hong Jin in disbelief.

“What is it?”

“Hm? Why?”

“This carriage is going to the Jin Family of Taiyuan.”

“I know. That’s why I got on.”

“What?”

“You know what they say—strike while the iron is hot. Shouldn’t I take this opportunity to have a conversation with the Lesser Family Head Jin?”

Hong Jin smiled pleasantly and snapped his fingers. An official came running over like the wind.

“Deputy Military Commissioner. Do you have an order for me?”

“We’re visiting without an appointment, so we should bring plenty of gifts. Don’t forget to send a messenger ahead to offer them our respects.”

“I shall carry out your orders!”

Li Feng also issued an order to one of the officers under his command.

“He is an honored guest. Escort him to the Jin Family of Taiyuan.”

“Yes, sir!”

At the two men’s commands, nearly a hundred soldiers and a hastily assembled delegation began moving in perfect order.

Cheongpung, who had been about to climb aboard after us, gave a small round of applause at the sight.

“Wow.”

Having obtained the royal guard gear set he had longed for so desperately, he decided to stay at the Jin Family of Taiyuan for the time being.

Li Feng dipped his head toward me.

“I entrust Martial Uncle to you.”

“Of course.”

Even without hearing him say that, Cheongpung was someone I wanted to become friends with first.

If I used him as a bridge to strengthen the Jin Family of Taiyuan’s relationship with Huashan, our family’s future would surely be bright.

*He’s an interesting guy, too.*

Cheongpung waved with a sunny smile.

“Martial Nephew Li Feng, don’t worry about me! Interesting things keep happening whenever I’m with Young Master Jin!”

“Just in case, I’ll say this now. Don’t cause any trouble.”

“Yes!”

At least he was good at answering.

I turned toward the people who remained behind.

“What have you decided to do?”

The young prodigies of the Five Gates of Shanxi answered hesitantly.

“We plan to stay at Honghwa Inn until New Year’s Day.”

“It would be difficult to visit our families. There isn’t much time…”

“To be honest, we don’t even dare go back.”

“If I return now, my father might kill me.”

Their answers were as gloomy as could be.

Then again, rumors about what had happened the day before had probably already spread like wildfire, so their fear was understandable.

I clicked my tongue as I looked at them.

“Behave yourselves until New Year’s Day. I’ll smooth things over with the Sect Leaders later.”

“Are you really going to do that?”

“But in return, each of you needs to do your part. You know what I mean, right?”

“The Seongun Escort Bureau… Yes, sir. We understand.”

The tide could no longer be turned. By now, both these young men and the Sect Leaders of the Five Gates of Shanxi would know that.

All that remained was to grow as large as possible under the Jin Family of Taiyuan.

“All right, then. Do your best, and I’ll see you at New Year’s.”

“What?”

“Why? What is it?”

“W-we’re going the same way.”

“Where? To Honghwa Inn?”

“Yes.”

I tossed one final remark at the bewildered young men.

“This is an express carriage to the Jin Family of Taiyuan.”

*Bang!*

The carriage began moving almost as soon as the door slammed shut.

* * *

The inside had been spacious even with six people seated in it. Cheongpung, Hong Jin, and I each claimed several seats and leaned back against the soft cushions.

“I think I could live here.”

Cheongpung continued with a blissful smile.

“When I lived with Grandfather, I slept on grass or rocks. I don’t think I could live like that anymore.”

*He’s a primitive man discovering civilization.*

At his words, Hong Jin asked with curious eyes,

“Then have you always lived on Huashan, Young Master?”

“Yes. Ever since I was very young. But apparently I wasn’t born on Huashan. I asked Grandfather about it once, and he said I came to Huashan when I was three or four years old.”

That figured. No matter how great a master the Sword Saint was, even he had limits when it came to raising a child.

Reaching the Supreme Peak realm wouldn’t make milk come out of a man’s chest, after all.

“……”

*Actually, a Supreme Peak master might be able to do it.*

They were monsters who could use Sword Energy and Sword Force. Producing a little milk couldn’t be beyond them.

I imagined a white-haired old man nursing a newborn baby.

“Ugh.”

“Benefactor, are you all right?”

“Young Master Jin, are you all right?”

“I’m fine. I just felt a little nauseated.”

“Oh my, that won’t do. Here, lie down on my lap.”

“……”

*Maybe I should just smash his knee.*

When I hurled a silent double curse at him with my eyes, Hong Jin covered his mouth and laughed.

“Hoho. As expected, Young Master Jin is so much fun to tease.”

If a beautiful woman had said that, I would have laughed along with her. But Hong Jin was unmistakably a man. No amount of white powder on his face or lipstick on his lips could change that fact.

*He said he used to be a palace attendant.*

Didn’t that make him a eunuch?

I had heard once that not every eunuch was necessarily castrated. But there was no way to tell whether Hong Jin was equipped or not.

“Young Master Jin.”

“Yes, yes?”

“What are you looking at right now?”

“Ah, I thought there was something stuck there.”

*Damn it. He caught me.*

He wasn’t a Murim martial artist, but his ability to read the situation was on the level of a Supreme Peak master. I quickly pulled my gaze away from Hong Jin’s lower body and changed the subject.

“By the way, how did Great Hero Li Feng end up joining the military?”

“Assistant Military Commissioner Li? He passed the military examination, of course. After that, it was smooth sailing all the way.”

“As expected of a Huashan lay disciple.”

“I can’t say that had no influence, but it wasn’t only because of that. Becoming a Third-Rank Assistant Military Commissioner in only ten years is extremely difficult.”

“Third-Rank means…?”

“What is Third-Rank? Is it something you eat?”

I vaguely understood that it was a high position, but that was about it.

Seeing that Cheongpung and I had no idea what he was talking about, Hong Jin explained patiently.

“It’s a high office. There are only four such positions in each province, and in terms of rank, Assistant Military Commissioner Li is one of the top three in the military.”

Hong Jin counted them off on his fingers.

“The Military Commissioner, who is the commander in chief. Then me, directly beneath him. And third is Assistant Military Commissioner Li. Of course, His Highness Prince Shangshan stands above all of us.”

“The Military Commissioner?”

“He’s about to retire. He was born the son of a Grand General, accomplished a little, and has a tremendous fondness for bribes.”

*A corrupt military official. The kind whose petty corruption had become a way of life.*

With the commander in chief being that kind of person, it was easy to understand why security in Shanxi Province had been such a mess lately.

“The current Military Commissioner is incompetent. You only need to look at the mounted bandits roaming freely the moment the Mount Heng Sword Sect collapsed.”

“If he’s that incompetent, then why not just…”

I swallowed the rest of the sentence before it left my mouth.

*Why should I meddle in someone else’s workplace? Especially when they’re all high-ranking government officials.*

Seeing my reaction, Hong Jin kindly added an explanation.

“The Military Commissioner is appointed directly by the Emperor. His dismissal works the same way.”

“Oh.”

“Well, at least he has no ambitions beyond that. I like bribes too, so I’m hardly in a position to criticize him.”

*What kind of person was this?*

I had seen plenty of politicians on television who claimed to be innocent of all charges of accepting bribes, but Hong Jin was the first person I had met who admitted to liking them so openly.

“Why? Did I look that upright?”

“No. You did look like someone who would enjoy bribes, but…”

“But you didn’t expect me to say it so openly?”

“Something like that. To be honest, I’m a little flustered.”

“Young Master Jin. Do you know what?”

Hong Jin continued with a serious expression.

“I don’t have a thing.”

“What?”

“I’ve been castrated.”

“……”

*What the hell was I supposed to say to that?*

I had suspected as much, but I hadn’t expected him to suddenly drop a bomb like that.

Cheongpung, who had been looking out the window, abruptly joined in with a curious expression.

“What does ‘castrated’ mean?”

“……Please, please shut your mouth.”

*He said he doesn’t have his thing—his thing!*

Every second dragged by. Sweating coldly, I forced myself to speak.

“I’m sorry to hear that.”

“There’s no need to be sorry. Some people live without it, and some people live with it. Right?”

“Th—that’s right.”

His admirable attitude made me solemn for no reason.

Meanwhile, the mountain-dwelling primitive who didn’t know what a eunuch was kept chattering without the slightest sense of danger.

“Benefactor, could you please tell me what a eunuch is?”

*Even if I die, I’m not telling him. Never.*

Even if I explained it, there was a 99.99 percent chance he would say something like, *Wow, I’ve never met anyone without one before!*

But Hong Jin remained composed.

“It means a man doesn’t have his thing.”

“Wow, I’ve never met anyone who didn’t have—”

“Oh, shut up already!”

Cheongpung sucked in a startled breath.

“B-Benefactor.”

“Calm down, Young Master Jin. If he grew up in the mountains, it’s understandable. And besides, it’s not as if I’ve only been living as a eunuch for a day or two.”

“Still, that was too harsh.”

“Was I in the wrong? My sincerest apologies.”

“It’s fine. Chin up. It’s still attached.”

*Decades of experience as a eunuch hadn’t gone anywhere.*

Hong Jin waved his hand as if telling us to calm down, then continued as though nothing important had happened.

“I have never regretted the decision I made. When your own family is starving to death, what wouldn’t you do? Am I wrong?”

“Of course not.”

“I—I would have done the same!”

Whatever Hong Jin said now, we had to agree with him. Cheongpung and I could only nod, feeling like condemned criminals.

“I’m not an upright man, but I’m not cowardly enough to betray my loyalty. If I were, I wouldn’t have continued serving His Highness all this time.”

Hong Jin gazed out the window with hazy eyes.

“I served the late Emperor at his side long ago. He ordered me to assist His Highness Prince Shangshan.”

“The late Emperor?”

If the previous Emperor had entrusted Hong Jin with such a request, it meant he must have held a considerably high position among the palace eunuchs even back then.

Hong Jin nodded and continued.

“I came to the frontier in something like exile, but… I’m satisfied with things as they are now. More than satisfied.”

Despite his words, an unmistakable light shone in his eyes.

Ambition? Hope?

Before I could understand what that light meant, it disappeared, and the coachman’s quiet voice reached my ears.

“We can see the Jin Family of Taiyuan.”
## Chapter artifact 147

# Chapter 147

Jin Wikyung let out a deep sigh.

“I have to start working the moment I return to the family.”

“Were you not away for several days?”

“That was due to circumstances beyond my control!”

“Getting angry like this won’t make the work disappear.”

“Wipeng, save me. At this rate, I’m really going to die of overwork.”

Despite his desperate, pitiful plea, Wipeng answered coldly.

“Finish your work before you die. I’ll give you a grand funeral.”

“……You’re a demon. Are you really human?”

What awaited Jin Wikyung, who had returned to the Jin Family of Taiyuan half a day earlier, was a mountain of work.

Because he had been away for nearly ten days, hundreds of bamboo slips were scattered across not only the writing desk but also the floor.

“How am I supposed to do all this alone?”

“You can do it. You’ve done fine until now, so why are you making such a fuss?”

“Does our family really have so few people? No—are there really so few capable people in all of Shanxi Province?”

“Have you ever considered lowering your standards when it comes to people?”

“Are you saying this is my fault?”

“More than ten people have come and gone already. They all looked like decent scholars to me, but you made the mistake of choosing only two.”

“Decent scholars? Please. Do you have no eye for people?”

They couldn’t simply accept anyone who had studied.

The Jin Family of Taiyuan was, after all, a Murim sect. How much of the Four Books and Three Classics someone had memorized, or what they had learned from which great scholar, wasn’t important.

The kind of talent Jin Wikyung wanted was a practical-minded person with flexible thinking—not a rigid scholar who went around constantly quoting Confucius and Mencius.

“Those two were the only ones among them who were worth using.”

He still didn’t regret that choice. At his firm answer, Wipeng picked at his ear.

“Oh, really? And where are those two now? What are they doing?”

“……Well, that’s…”

When Jin Wikyung was momentarily at a loss for words, Wipeng continued in his place.

“They worked through four straight nights and then ran away.”

“W-who ran away? What are you talking about? One of them had a mother who was gravely ill…”

“I looked into it after that fellow disappeared. His mother died ten years ago.”

“……Really?”

“The other one said he was going to the latrine, then slipped away and never came back. Am I wrong?”

“Cough. Cough-cough!”

“My lord, you’ve trained in martial arts, so you can stay up for several nights and remain perfectly fine. But those men are different. They’re commoners who have never read a single line of a cultivation technique formula in their entire lives.”

“Ah, I know that. That’s why I’m paying them generously.”

“If they had stayed another fifteen days, that silver would have gone to their survivors.”

“……”

“Do you have anything else to say?”

“……No.”

“If you have nothing else to say, start working. From now on, accept any scholars who seem useful when they come looking for work.”

Jin Wikyung nodded gloomily and reached for a bamboo slip.

That was when one of the martial artists from the guard detail waiting outside the office cautiously entered and delivered an unexpected report.

“Who did you say?”

In response to Jin Wikyung’s question, Wipeng answered.

“A messenger sent by the Deputy Military Commissioner of Shanxi Province.”

“I heard that much. But the Deputy Military Commissioner is… that man who’s supposedly Prince Shangshan’s closest aide and the real power behind him?”

“Yes. There used to be plenty of talk about how a palace attendant had managed to secure a high-ranking military post.”

“Right. I remember hearing that.”

Jin Wikyung had heard the rumors about the palace attendant who sat at the top of the military hierarchy and single-handedly kept the young prince under his thumb.

“We’ve never even met him. What could he want all of a sudden?”

“What do you think?”

“Could it be because of the Third Young Master?”

“Given the circumstances, that’s highly likely. Bring the messenger inside first.”

“Yes.”

“Ah, and just in case, call Mukyung as well.”

“Understood.”

Not long after Wipeng nodded to one of his subordinates, a man entered the office.

He moved with measured precision and wore light armor.

Anyone could tell at a glance that he belonged to the military. He was the messenger Hong Jin had sent.

“Are you the Lesser Family Head of the Jin Family of Taiyuan?”

Jin Wikyung nodded.

“I am Jin Wikyung. Let’s skip the tedious formalities between us. What brings you here?”

“I have come to convey the Deputy Military Commissioner’s words.”

“Is this related to my younger brother?”

“Yes. He is on his way here now, together with the Deputy Military Commissioner.”

“Together?”

“Yes. They should arrive in half a shichen.”

Jin Wikyung silently stroked his chin as he listened.

Hong Jin was effectively the second-most powerful man in Shanxi Province. He wasn’t the sort of person who moved without a reason.

It would have been surprising enough if someone who had never had any connection with them sent nothing but a letter. The fact that he was coming in person made the situation all the more bewildering.

“I don’t recall making an appointment.”

Wipeng added a remark with a face dripping with frost.

“No matter how high-ranking an official the Deputy Military Commissioner is, this is clearly an insult to our family. Are you aware of that?”

“Th-that…”

Sweat gathered on the messenger’s forehead.

He had trained in military martial arts, however slightly. When faced with the gaze of the Peak master known as the Ghost Sword, his heart couldn’t help but sink.

“What business does he have here?”

“I-I was only ordered to deliver his message…”

“He certainly knows how to pull rank.”

The messenger, who had become so nervous he could hardly sit still, was rescued by Jin Wikyung.

“Wipeng, that’s enough. So what exactly did the Deputy Military Commissioner say?”

“He told me to convey his apologies in advance for his sudden rudeness. And…”

The messenger pulled a small cylinder from inside his robes and handed it to Jin Wikyung. Inside the cylinder, which was about the size of an adult’s palm, was a rolled-up sheet of white paper.

“What is this?”

“I haven’t heard anything myself. He merely said that you would understand once it was delivered.”

“Hmm.”

Jin Wikyung deliberately furrowed his brow and unfolded the paper.

At that moment, the office door opened, and a second guest entered.

“Did you call for me?”

“……”

“Older brother?”

Jin Wikyung stared silently at the paper in his hand for a while before raising his head.

“You’re here.”

“Yes. I heard you were looking for me while I was training… What did you call me for?”

“We have an honored guest coming. We need to prepare to go out and greet him.”

“An honored guest?”

“My lord, what do you mean, an honored guest? Do we really need to go out and greet him?”

Wipeng frowned and objected.

“He’s coming without even giving us notice. What kind of honored guest is that? He’s an uninvited guest.”

He showed no restraint despite the messenger standing right in front of him. Considering the position the Jin Family of Taiyuan currently held in Shanxi, it wasn’t an entirely wrong thing to say.

Jin Wikyung quietly handed him the paper.

“Look at this, then we’ll talk again.”

“What is it?”

“Seeing is believing.”

“You could simply tell me instead of making such a fuss…”

Wipeng’s voice gradually grew quieter before cutting off completely. His eyes trembled as they darted back and forth.

A moment later, his lips parted.

“An honored guest is coming.”

“Right?”

“Yes. Exactly.”

The two men turned their gazes toward Jin Mukyung, who was still standing there with no idea what was going on.

“Mukyung.”

“Second Young Master.”

“Yes?”

“You said you came straight from training, right?”

“You smell like sweat.”

“It’s only natural to sweat when you train.”

“Go wash.”

“Wash immediately.”

Unable to understand the reason for their reactions, Jin Mukyung asked with a frustrated expression,

“Who on earth is coming to make you act like this?”

Jin Wikyung and Wipeng answered at the same time.

“A big spender.”

“And an extremely big one at that.”

Wipeng waved the paper in his hand. It was a thousand-nyang bank draft issued by the Golden Star Exchange, valid anywhere under heaven.

“This isn’t just a thousand nyang. It’s a thousand nyang of silver.”

A thousand silver nyang was worth one hundred thousand nyang in iron coins. To the Jin Family of Taiyuan, which was already pouring money out in every direction, it was a fortune like rain after a drought.

For the first time in a long while, Jin Wikyung gave his younger brother a stern look.

“Mukyung, let’s go wash up.”

“……”

* * *

The moment I got out of the carriage, a word slipped out on its own.

“Wow, fuck…”

There was no way I could stop myself from swearing. Atop the towering wall, a fluttering cloth banner displayed enormous letters that read:



**The Day the Deputy Military Commissioner Came to the Jin Family of Taiyuan**

*This isn’t even Buddha’s Birthday. What the hell is this?*

I was too embarrassed to lift my head when Hong Jin climbed down behind me and burst out laughing, clutching his stomach.

“Wow. This is beyond what I expected.”

“Are you perhaps childhood friends with my eldest brother? How else could he give you such an enthusiastic welcome…?”

“Young Master Jin, I don’t have balls.”

“Ah—oh. I’m sorry. I’m really sorry.”

That was a tremendous blunder. Without a stick, there was no way any fertilized eggs would be left behind.

As I writhed under the weight of my guilt, Cheongpung approached and comforted me.

“Benefactor, my grandfather used to say that people who don’t know how to read the room have no friends around them. But don’t worry. I’ll be your ball friend.”

“……”

*I don’t need one, you bastard.*

As I desperately swallowed my curses, Hong Jin spoke to me.

“Young Master Jin, do you know what makes relationships between people strong? Wealth. They say gold and silver can make even ghosts work for you. Living people should be even easier, don’t you think?”

“And?”

“I told you I’d give him a present. It’s basically a bribe.”

*Money can make even ghosts work for you.*

I agreed with that to some extent, but I didn’t like the fact that the person in question was Jin Wikyung.

I already thought of him as my older brother deep down. I didn’t appreciate Hong Jin making him out to be some materialistic opportunist who could be bought with a bribe.

Perhaps that displeasure showed on my face, because Hong Jin smiled and said,

“Was that too harsh? But it’s only natural. Who doesn’t like wealth?”

“He’s still my eldest brother. Don’t think you’ve won over the Lesser Family Head of the Jin Family of Taiyuan with a measly few silver nyang.”

“Young Master Jin…”

Hong Jin’s eyes widened at my low voice.

“A few silver nyang? I gave him a thousand nyang.”

“Just a few silver… How much?”

“A thousand silver nyang. That’s one hundred thousand nyang in iron coins.”

I had finally gotten a rough sense of prices and currency in the Murim.

The private suite at the Phoenix Inn, which could be considered a luxury hotel, cost fifty silver nyang per night. That was said to be close to twice the annual living expenses of a family of four commoners.

*In modern currency, that would be tens of millions of won.*

A thousand silver nyang was twenty times that. In other words, Hong Jin had casually tossed around several hundred million won in one go.

“That’s… a lot, isn’t it?”

“A lot, yes. I put in some effort this time.”

“Still, that’s far too much.”

“It’s for the sake of our future relationship. And right now, the Jin Family of Taiyuan is probably losing money faster than it’s bringing money in. Winning a war and occupying the enemy’s territory isn’t the end of it.”

“Ah, yes.”

“The assistance you give at times like this feels much greater. I learned that after giving and receiving so many bribes myself. Ah, of course…”

Hong Jin continued with a wink.

“I did spend a little extra because I took a particular liking to Young Master Jin. You understand my feelings, right?”

The moment he finished speaking, I felt a hard foreign object against my butt.

The sensation poking me repeatedly snapped me fully awake.

*No way. Is this bastard seriously…?*

I swear, in my entire life, this was the most spine-chilling moment I had ever experienced.

*Fine, if you’re going down, I’m going down too. Let’s have another war!*

I spun around at lightning speed.

What met my eyes was a silver lump about half the size of my palm. What did they call those again? A silver yuanbao?

“Here. Pocket money from me.”

*Oh, right. He was a eunuch.*

I calmed my pounding heart and answered.

“Th-thank you.”

“Sure. Go buy some candied hawthorn skewers.[^1]”

“Benefactor, could you take me with you when you go buy them?”

Cheongpung joined in, smacking his lips.

Just then, a familiar voice rang out from behind us.

“Heh heh. I’ll tell the cooks separately, so order as much as you like. Right, Wipeng?”

“We’ll build a mountain of candied hawthorn skewers.”

“Who is that fellow? Candied hawthorn skewers? He isn’t even a child, so what’s this about?”

I didn’t need to look to know who it was.

I turned around with a happy smile, only to find a scene that left me speechless.

*Flutter. Flutter.*

Jin Wikyung was smiling broadly. So was Wipeng. Jin Mukyung’s face was bright red.

In the hands of all three men, tiny scraps of cloth fluttered in the wind. I had no idea when they had made them.



> **Long live the Great Nation! Long live His Imperial Majesty the Emperor!**
>
> **His Highness Prince Shangshan, may you become a sage king!**

“……”

“……”

*What had I said to Hong Jin earlier?*

*Had I told him not to think he’d won over the Lesser Family Head of the mighty Jin Family of Taiyuan with a mere few silver nyang?*

*Fuck, “won him over” my ass.*

At this point, he was burned—burned to a crisp.

[^1]: Candied hawthorn skewers are a traditional snack of fruit coated in hardened sugar.
## Chapter artifact 148

# Chapter 148

In the atmosphere warmed by the enormous sum of a hundred thousand nyang, Jin Wikyung and Hong Jin exchanged greetings.

“I am Jin Wikyung of the Jin Family of Taiyuan. It is an immense pleasure to meet the Deputy Military Commissioner I’ve heard so much about.”

“Being so warmly welcomed by the Lesser Family Head of the great Jin Family of Taiyuan leaves me at a loss. From now on, please just call me Comrade Hong.”

“Even so, how could I address an official that casually?”

“Come now, you’re being too stiff. I said to call me casually.”

“Ha-ha. Then shall I, Comrade Hong?”

What was with the sudden communist atmosphere?

As I wondered whether I was in Pyongyang or the Murim, Jin Wikyung finished exchanging introductions and turned his gaze toward me.

“Hmm. Taekyung, you’re here?”

“Yes.”

His voice was heavier than usual, so I answered politely and read the room.

Apparently, he understood that acting as he normally did in front of outsiders would not only damage his personal dignity but also humiliate the entire family.

“So, did you greet His Highness properly?”

*Properly? I didn’t just greet him. I even held a private autograph session.*

Hong Jin smiled and patted my shoulder.

“His Highness was delighted. He’d always wanted to meet Young Master Jin here.”

“Oh, is that so?”

“Yes. He was so happy that he had no intention of letting him go.”

“Uhehehe. It seems our youngest—no. It seems His Highness has taken quite a liking to my younger brother.”

“I can see why. He’s handsome, tall, and well-built. He’s strong in martial arts, and he has such an easygoing personality. Who could dislike him?”

“Ehem. It feels strange to say this myself, but Taekyung really is an extraordinary talent. If he had been born somewhere like the Five Great Families instead of our family, it wouldn’t be strange if he became the greatest under heaven.”

Hong Jin’s expression hardened as Jin Wikyung got carried away, chattering excitedly and forgetting all about maintaining his dignity.

“The greatest under heaven? Lesser Family Head Jin, that’s too much of a joke.”

“Pardon? What do you mean?”

“You’re saying Young Master Jin has what it takes to become the greatest under heaven? Even if I have no connection to the Murim, surely you aren’t making light of me.”

“……Ahem.”

As the atmosphere instantly turned cold, Jin Wikyung gave an uncomfortable cough. Hong Jin immediately continued.

“Someone like Young Master Jin could become the greatest of all time.”

“……!”

“Allow me to congratulate you in advance, Lesser Family Head. For the greatest of all time to come from the Jin Family of Taiyuan—what a blessing for Shanxi Province.”

Jin Wikyung cried out with a deeply moved expression.

“Comrade Hong!”

“Lesser Family Head Jin!”

“……”

They say Hong Jin lived in the imperial palace for twenty years. His skill with his tongue certainly wasn’t ordinary.

I clicked my tongue as I watched Jin Wikyung rejoice as though he had found his soulmate.

“This won’t do. There’s no point staying here. I’ve already arranged a place, so why don’t we have a drink?”

“What should I do? I’m not very good with alcohol.”

“Ah, what a shame.”

“The only time I can’t drink is when there’s none to be had.”

“Comrade Hong!”

“Lesser Family Head Jin!”

“……”

“……”

Look at how perfectly they clicked together.

When the two men disappeared, laughing loudly with their arms around each other’s shoulders, Wipeng stared at me with an utterly dumbfounded expression.

“Is that man really the Deputy Military Commissioner?”

“Unfortunately, yes.”

“I heard he was a former palace attendant, but I didn’t know he’d be so frivolous.”

Well, then what did that make Jin Wikyung, a martial artist who had played along with every bit of it?

Jin Mukyung, who had been wearing a sour expression for some time, finally spoke.

“That’s just the kind of man he is. Last time, he subtly stroked my shoulder. I barely stopped myself from breaking his arm.”

He ripped the cloth in his hands into strips and threw them onto the ground, then spoke with a much more relieved expression.

“Then I have important business, so I’ll be leaving.”

“What business? Training again, I assume.”

“Is there anything more important to a martial artist than training?”

“……No.”

That left me with nothing to say.

As I stood there at a loss, merely smacking my lips, a clear, ringing voice rang out.

“Wow, that’s exactly what my grandfather always says.”

Wipeng and Jin Mukyung’s gazes pierced Cheongpung like awls.

To ordinary people, Cheongpung was merely a young man with a slightly unusual air about him. To masters, however, he was something else entirely.

When both men’s eyebrows shot upward, Cheongpung turned to me with a flustered expression.

“Uh, Benefactor. Did I do something wrong?”

“What do you mean, wrong? They just found it interesting. Right, gentlemen?”

Neither man took his eyes off Cheongpung. They merely nodded.

An extraordinarily young Peak master. It was only natural that they would be curious about the identity of this Cheongpung who had suddenly appeared out of nowhere.

“Since we’re here, why don’t you introduce yourselves? This is Cheongpung.”

Before I had even finished speaking, Cheongpung gave a deep bow.

“Hello, I’m Cheongpung! I’ve only been in Shanxi for a few days. Before that, I was in Henan, and before that…”

*Where did this guy crawl out of?*

The question was written plainly across both men’s faces.

Just as I expected. I explained Cheongpung’s identity simply and clearly.

“He’s the Sword Saint’s disciple.”

“……!”

“……!”

The name of Sword Saint Mae Jonghak was practically an instant cheat code among martial artists.

When the two men stared at Cheongpung in shock, mouths hanging open and unable to speak, he asked cautiously,

“Um, which of you is the Heaven Shaking Sword?”

Jin Mukyung, who still hadn’t recovered from the shock, stammered out a reply.

“I-I’m the Heaven Shaking Sword. But are you really the Sword Saint Mae Jonghak’s…?”

“Yes. He’s my grandfather.”

“Gasp!”

He looked several times more shocked than when he had seen the Flame Divine Palm martial arts manual.

A young man claiming to be the disciple—and grandson—of a Supreme Peak master who was known to have gone into seclusion decades ago had suddenly appeared before them. Their reaction was understandable.

“This can’t be…”

“He’s the Sword Saint’s successor…”

Cheongpung looked back and forth between the two astonished men, then smiled brightly.

“I didn’t know either until I came down the mountain.”

“Y-Young Hero. Did Great Hero Mae also descend the mountain…?”

His voice was filled with expectation and excitement.

Both men had trained in swordsmanship their entire lives. To them, Mae Jonghak was practically a god—a man who had reached such a level in the Way of the Sword that he had earned the martial title of Sword Saint.

But Cheongpung’s answer shattered their expectations.

“No. I just snuck out by myself. There were people I wanted to meet.”

“Ah…”

“How unfortunate…”

“But putting that aside…”

Cheongpung looked at the two crestfallen men before speaking again.

His bright eyes had been fixed on Jin Mukyung for some time.

“Are you really Young Hero Jin Mukyung, the one from the Ten Dragons and Phoenixes?”

“That’s right. I’m Jin Mukyung.”

“Wow, I finally found you!”

“……Hmm?”

“I searched everywhere for you. From Heaven’s Gate Temple in Henan all the way here.”

*What? The person that guy had been looking for was Jin Mukyung?*

Wipeng, as well as Jin Mukyung himself, asked with bewildered expressions,

“You were looking for me?”

“Yes. Since you were nearby, I thought you’d be a decent place to start.”

“A first? What does that mean?”

“A dueling tour.”

Cheongpung smiled softly. It was completely different from the bright, innocent smile I had seen from him until now.

“I decided it while coming down the mountain. I won’t return until I’ve defeated all the Ten Dragons and Phoenixes.”

“……!”

“My grandfather told me this: A martial artist has no need for conversation. We settle things through martial arts alone.”

Sssss.

At that moment, I felt a wave of heat. Violet light-flames had risen around Cheongpung’s entire body, surging upward.

I had already seen this once before.

*The Zaha Divine Technique.*

The Extreme Yang qi burned the cold away. The earth melted, and the soil scorched. Cheongpung opened his mouth with all traces of his smile gone.

“Shall we move somewhere else?”

“Is there any need?”

Jin Mukyung continued,

“Draw your sword.”

* * *

Jin Mukyung let out a long breath. His rapidly beating heart slowly began to settle. Breathing was important in battle. Only now was he finally ready to draw his sword.

As he placed a hand on the hilt, he thought of one man’s name.

*Sword Saint Mae Jonghak.*

Not once had he forgotten that name since the day he first held a sword.

A legendary swordsman who was said to have reached the ultimate realm of the sword—or perhaps a realm beyond it.

Everyone revered the Sword Saint, but Jin Mukyung was different.

*Someday, I’ll defeat him.*

If anyone had heard him say that, they would have snorted. They would have pointed at him and called him crazy.

No matter how talented Jin Mukyung was, he could never touch the Sword Saint’s level. Ever since Mae Jonghak had begun to be called the Sword Saint, no one had surpassed him.

Sword Saint Mae Jonghak had written a new chapter in the history of the orthodox Murim decades ago and become the protagonist of a legend.

*It doesn’t matter. This is my goal.*

It wasn’t reckless arrogance. It was a goal.

A goal he had etched into his bones and heart every day as he trained with his sword.

And at this very moment, someone who had inherited everything from Sword Saint Mae Jonghak stood before him.

“My grandfather used to tell me this. ‘Compared to the Ten Dragons and Phoenixes, you are nothing. Don’t become arrogant.’”

Cheongpung slowly stepped forward. A single blue-steel sword dangled from his waist, tied on haphazardly, and his footsteps were as light as though he had come out for a stroll.

But…

*There are no openings.*

He looked utterly careless, yet Jin Mukyung couldn’t figure out when or how he was supposed to attack him.

Jin Mukyung licked his parched lips.

“I’ve never even met him… He praised me too highly.”

“No, honestly, you surprised me a little. I mean that.”

Jin Mukyung knew that everything Cheongpung was saying was sincere. That only made it feel stranger.

*Just a little?*

More than twenty years had passed since he began training with the sword. He had reached this point through talent and effort.

People had called him a genius, given him the martial title Heaven Shaking Sword, and counted him among the Ten Dragons and Phoenixes.

He had believed that he had never once been intoxicated by such hollow fame, but…

*I still have a long way to go.*

At some point, he must have grown accustomed to the gazes of people who looked up to him.

The wound Pung Yang had inflicted on him not long ago seemed to throb again.

“Do you know something?”

“What?”

“That you’re strong.”

“Until recently, I wasn’t certain. But now I know.”

“Because you met me?”

“Yes. Because I met Young Hero Jin. Now I know what the Ten Dragons and Phoenixes are capable of.”

“Is that so?”

Jin Mukyung let out a quiet laugh.

What an interesting guy. He possessed martial arts that rivaled—or even surpassed—those of an Elder of the Nine Sects and One Gang, yet he remained untainted by the world. He was pure. Honest.

He was a martial artist, but he didn’t fit in the Murim.

*He’s the exact opposite of someone I know.*

One person suddenly came to mind.

A guy who seemed like he could somehow survive no matter where he was thrown in the Murim, and who fought in the least martial-artist-like way imaginable.

“How old are you?”

“I’m twenty this year.”

“We’re the same age. Is it coincidence? Or fate?”

“What?”

Jin Mukyung shook his head instead of answering.

In truth, he already knew the outcome of this duel. The qi of the Zaha Divine Technique surging through Cheongpung’s entire body was that overwhelming.

It was merely regrettable that he couldn’t display all his abilities against an opponent of this caliber.

*How would that troublemaker handle a situation like this?*

Jin Mukyung glanced at his troublesome younger brother. With a grin like a little devil’s, Taekyung was mouthing something.

*You. Are. Fucked.*

*What a goddamn bastard.*

Laughing hollowly, Jin Mukyung placed a hand on his sword hilt. The internal energy boiling up from his dantian coursed through every part of his body.

Cheongpung looked at Jin Mukyung’s sword and spoke.

“My grandfather told me something else, too. A duel doesn’t need an opening stance or anything like that.”

“I agree.”

The next moment—

With a tremendous boom, violet light-flames and silver Sword Energy collided.
## Chapter artifact 149

# Chapter 149

Xi’an’s history ran deep. Until the dynasties changed, it had been called the center of all under heaven for hundreds of years.

Its enormous population. Its abundant resources, produced by the plains and mines. And the famous scenic and historic sites left behind by three unified dynasties swept away by the passage of time. Those were still the reasons so many people visited Xi’an.

In one of Xi’an’s bustling inns, two Confucian scholars dressed in thick fur coats were among those visitors.

“Come on, hurry up. If we want to get back to the inn before sunset, we’re running out of time.”

Unlike his enthusiastic friend, the other scholar shook his head with a thoroughly fed-up expression.

“Again?”

“What do you mean, again?”

“Can’t we just rest for today? We’ve been walking around for days, and my legs feel like they’re about to break.”

“Don’t be such a baby. We walked a thousand li to get here—how can we just turn around and go back? Do you really think we’ll have another chance to come to Xi’an at our age?”

“Good grief. I came to sightsee in Xi’an, and now it looks like I’m going to end up sightseeing Mount Beimang.[^1] Leave me alone.”

[^1]: Mount Beimang is traditionally associated with burial grounds and death.

“Come now. I don’t know about the other places, but we absolutely have to visit Western Peak. You’ll regret it until the day you die if you miss such a magnificent sight.”

“Western Peak…”

The five most famous mountains in all under heaven were called the Five Great Mountains.

Western Peak referred to Huashan, which lay near Xi’an.

“Imagine how it would feel to climb Huashan and look down upon all under heaven. Doesn’t your lofty spirit surge just thinking about it?”

“Well… I suppose it does.”

Unable to resist his friend’s fervent persuasion, the scholar reluctantly nodded.

He was well aware that Huashan was famous not only for its ruggedness but also for its beautiful scenery.

“Do you think a famous mountain became famous for no reason? We need to soak up plenty of its spiritually efficacious energy this time if we want good news at the next civil service examination. How many times have you already failed?”

“Why are you bringing that up all of a sudden?”

“Don’t get angry. Anyway, we’ll go to Huashan, receive some lofty spirit, receive some spiritual energy, and that’ll be that.”

When the scholar still looked hesitant, his friend added in a coaxing voice,

“I won’t ask you to visit anywhere else. We’ll just stop at Lotus Peak and come straight back down.”

At that, even the scholar who had been stubbornly resisting began to waver. Who knew? Perhaps he really would pass the civil service examination with flying colors next year.

But one rumor still bothered him.

“I heard Huashan is crawling with martial artists…”

“If you mean Huashan’s Daoists, there’s nothing to worry about. An acquaintance of mine went there years ago and said nothing happened to him.”

“Ahem. Then shall we give it a try?”

The scholar made a show of giving in as he rose, but suddenly lost his balance and staggered. The strength drained completely from his legs, which had been trembling for some time.

He was about to crack the back of his head against one of the many table corners scattered around him.

“Huh? Wh-whoa!”

Just as he was about to fall with a short scream, a rough, sturdy hand braced the scholar’s back.

“Ugh. I barely survived that.”

After barely righting himself, the scholar looked at the owner of the hand with a relieved sigh.

The young man looked to be around thirty. He wore a white robe and had an ordinary appearance, but he offered the scholar a gentle smile.

“Are you all right?”

“Th-thank you, Young Master.”

“It was nothing.”

Having narrowly escaped disaster, the scholar looked at the young man with curiosity.

*He looks ordinary.*

He was of middling height and had a slender build. Yet he had supported the scholar’s body, which outweighed the young man’s by several dozen pounds, with one hand.

The scholar glanced at his waist, wondering if he might be a martial artist, but it was empty. Apparently not.

*He’s much stronger than he looks.*

Regardless, the young man had saved his life. The sages of old had said that repaying kindness was a person’s duty.

“Thank you again. Thanks to you, Young Master, I avoided a terrible mishap.”

“I only did what anyone should have done. There’s no need to worry about it.”

“You helped me greatly. How could I end things with a few words? Why don’t you join us? Dinner will be on me.”

His fellow scholar cut in with an incredulous look.

“What are you talking about? What about Huashan? What about Lotus Peak?”

“Didn’t you just see me nearly go to the grave? This is a sign that I should rest at the inn. And since the Young Master here saved me, I ought to repay him. Isn’t that right?”

The young man smiled and waved his hand.

“I’m really fine. I’m waiting for my companions.”

“Companions? You’ve been sitting here alone for more than a shichen.”

“Ha-ha. It seems something came up and they’re running late. I have no choice but to wait.”

He had already been there for more than a shichen, and he still intended to keep waiting? He was as good-natured on the inside as he looked.

Still, with the young man saying he had companions, the scholar could hardly insist that he join them. He clicked his tongue regretfully.

“Then it can’t be helped. May peace prevail throughout your household for as long as you live, and may you enjoy good health and a long life.”

“Huashan! Lotus Peak!”

“I’m going, so shut that obnoxious trap of yours.”

“I knew I could count on you.”

“I might just throw you off the summit of Lotus Peak.”

The scholar glared at his companion and was just about to take a step when—

Bang!

A deafening boom that made everyone’s hair stand on end rang out. The inn’s door was smashed apart, and a man and a woman appeared amid a thunderous shout.

“We’re here!”

“Eunhyang’s here too!”

Every customer inside the inn stared at them with their mouths hanging open.

They were shocked by the man’s enormous physique and the beautiful girl’s appearance.

*What kind of combination is that?*

*In all my life, I’ve never seen anyone that huge.*

In the silence that fell over the inn, only one person showed no surprise. It was the young man who had helped the scholar moments before.

“You’re late.”

The man, who was several heads taller than anyone else, vigorously scratched his head.

“I’m sorry. We got caught up in a little dispute on the way.”

“What happened that made you more than a shichen late?”

“Well, the thing is…”

When the man began to mumble, the girl who had introduced herself as Eunhyang cut in with a bright grin.

“Big Brother, have you ever heard of the Black Serpent Sect?”

“The Black Serpent Sect? I can’t say I have. Going by the name alone, they don’t sound like they do much good.”

“That’s right. They’re a dark-path gang that runs a gambling den just up ahead. Their boss took one look at Brother Chulwoo and asked if he wanted to work with them… Mmph! Mmph-mmph!”

“No, he didn’t! I swear! I look so innocent!”

The man named Chulwoo covered Eunhyang’s mouth and protested, but no one in the inn believed him.

*Look at that face. With a face like that, he’s already one of the dark-path figures.*

*Even if I were the Black Serpent Sect’s boss, I’d have tried to recruit him.*

*He’d be their number-one pick. Number one.*

Everyone only muttered those words inwardly because Chulwoo had widened his eyes and was glaring around the room. Faced with the gaze of an enraged beast, the people could only swallow nervously.

Of course, one person was an exception again.

“So, what happened?”

At the young man’s question, Chulwoo quickly answered,

“I just told them I wasn’t interested and sent them away.”

“Is that true?”

Chulwoo subtly averted his gaze.

“Y-yes, it’s true.”

“There’s blood on your fist.”

“Gasp! Really? I definitely wiped it off!”

“…”

“…”

“Mmph. Mmph!”

The young man let out a deep sigh.

“Let go of Eunhyang first.”

“...Yes, Senior Brother.”

“Mmph—phew!”

Eunhyang was finally released. She scrunched up her face and spat repeatedly.

“Ugh, that’s salty. When was the last time you washed your hands, Brother?”

“Yesterday.”

“What? I could swear I’ve seen you visit the privy at least five times between yesterday and today. Then…”

“Ahh!”

“It’s all right. I smell wonderful even if I only bathe once every fifteen days.”

“Are you insane? No wonder women hate you.”

“What did you say?”

As the two began growling at each other, the young man rubbed the corners of his eyes tiredly.

These two were notorious troublemakers even within their sect. He had known that something like this would happen someday, but he had never expected them to cause trouble before they had even left Xi’an.

*I couldn’t refuse when it was the Sect Leader’s order.*

What could he do? He had no choice but to consider this his karma.

Already half drained of energy, he spoke.

“Do you both want to go back? Should I tell the Sect Leader to put you through wall-facing meditation before you come to your senses?”

“Gasp! No, Senior Brother.”

“I’m fine too, Big Brother.”

The young man deliberately hardened his expression.

“Come now. I’m not Big Brother. I’m your Senior Brother.”

“Yes, Big Brother.”

“Eunhyang, you… Phew. Never mind.”

“Hehe.”

How powerful was a beauty’s smile?

When Eunhyang smiled sweetly, the chilly atmosphere in the inn warmed at once.

That was when the innkeeper, who had been watching them nervously, approached.

“Um, sirs…”

The young man recognized the innkeeper and spoke with an apologetic expression.

“Ah, I’m sorry for causing such a commotion. We’ll leave right away.”

“No, that’s not it…”

The innkeeper glanced at Chulwoo with terrified eyes before continuing with difficulty.

“Compensation, please.”

“Ah.”

Only then did the smashed door come into view.

As the young man sighed again, Chulwoo swiftly pulled a silver nyang from a heavy pouch.

“This should be enough.”

“Where did you get this silver nyang?”

Eunhyang answered with a bright smile.

“The Black Serpent Sect.”

Chulwoo cried out in horror.

“Hey!”

“What? I didn’t do anything wrong.”

“You took a jade hairpin, too!”

“Oops. How did you know?”

“…”

Not only had they smashed the Black Serpent Sect, they seemed to have stripped it of every last possession as well. The young man’s forehead began to throb.

“Return it immediately.”

“Senior Brother, even if those men kept this wealth, they’d only use it for evil deeds.”

“That’s right. Since it’s already happened, we could eat something delicious while we travel to our destination…”

The young man cut them off in a stern voice.

“Since when was running a gambling den an evil deed? Or have you seen them commit any evil with your own eyes?”

“We don’t need to see it. It’s obvious. They’re dark-path figures.”

“How can everything in this vast Murim be only one color? And if the Black Serpent Sect were truly a group of villains, the main sect would have taken action long ago.”

“But…”

“Enough. We’re in a hurry, so we’ll leave the money here. Is that all right, Innkeeper?”

By now, everyone in the inn knew that these people were martial artists and that they had made enemies with one of Xi’an’s dark-path factions.

The innkeeper, who desperately wanted to avoid entanglement with martial artists, wore an expression like he had stepped in filth.

“G-Great Hero, forgive me, but an old man like me can’t handle something like this.”

Chulwoo, who was about to lose the reward for his hard work, spoke bluntly.

“Don’t worry. Nothing will happen.”

“Nothing may happen right now, but once you leave, I’ll be in serious trouble.”

“Come now, I said that won’t happen. Even after we leave, they won’t be able to lay a finger on you.”

“No, that’s not something you can say so easily…”

*Is his brain made of muscle too? He’s damn short-sighted.*

The innkeeper couldn’t bring himself to say that aloud and could only suffer in silence. At that moment, the young man smiled calmly.

“When they come, just tell them one thing along with this pouch.”

“Great Heroes, I don’t think you understand what I’m saying…”

The innkeeper’s words were cut short by the young man’s voice.

“Tell them that Baek Museong, a first-generation disciple of Huashan, apologizes for his junior disciples’ mistake.”

The inn fell silent.

The name *Huashan* was intimidating enough, but the young man’s name also sounded familiar, as though they had heard it somewhere before.

“Baek Museong of Huashan?”

“Baek Museong… Baek Museong… Wait. Could it be?”

Xi’an was practically Huashan’s front yard. It didn’t take long for a few martial arts aficionados to realize the young man’s identity.

“Baek Museong, Huashan’s Lone Crane!”

The title had been given to him because of his lofty bearing, like that of a solitary crane.

He had been known as an outstanding prodigy since the day he entered Huashan, and he possessed another title as well.

“If he’s Huashan’s Lone Crane, isn’t he the first of the Three Plum Blossom Elites?”

The current Sect Leader of Huashan had three disciples, all of whom had grown into outstanding masters.

It was only natural that they had been appointed Plum Blossom Swordsmen, the pride of Huashan, and they soon began to distinguish themselves.

“I heard one of them was a woman… Then are those two—?”

“Why even ask? Didn’t you hear her call Huashan’s Lone Crane Senior Brother?”

“Good heavens. I never thought I’d live to see the Three Plum Blossom Elites in a place like this.”

Ignoring the exclamations erupting throughout the inn, Baek Museong spoke.

“Would it really be impossible?”

The innkeeper answered with a solemn expression.

“I’ll return this property to the Black Serpent Sect at the risk of my life. At your command!”

“…”

* * *

“Ah, that’s right.”

At Baek Museong’s mutter, his two junior disciples turned toward him.

“What is it, Senior Brother?”

“Did you leave something behind?”

Baek Museong shook his head.

“I forgot to tell him that Huashan had been sealed off.”

“Who?”

“I don’t know his name. That man is going to drag his aching legs all the way there only to make the trip for nothing.”

Eunhyang clicked her tongue sympathetically.

“How sad. It’ll be months before he can go.”

“Indeed.”

They recalled the incident that had thrown all of Huashan into an uproar several days earlier.

While the Sect Leader—in other words, their Master—was asleep, an intruder had entered and left without anyone noticing.

The intruder had committed the audacious act of leaving a dagger and a handwritten letter beside the Sect Leader’s head.

> “I’m going out to get some air. Don’t slack off just because you’ve become Sect Leader. Train your martial arts when you should be sleeping.”

Under ordinary circumstances, they would have immediately cast a dragnet across the entire mountain. But if the intruder’s identity was Sword Saint Mae Jonghak, the matter was different.

The Sect Leader had immediately ordered Huashan sealed tight and instructed them to search for the Sword Saint’s place of seclusion. The search had continued ever since.

“Grandmaster really is something. He’s an amazing person.”

“I’d only heard about him. I didn’t know he was this extraordinary.”

“If that messenger pigeon hadn’t arrived, we would have been stuck searching Huashan too.”

In the midst of all that, the messenger pigeon that flew in from Shanxi Province had been a light of salvation.

After much deliberation, Huashan’s leaders had decided to dispatch the exceptional talents known as the Three Plum Blossom Elites.

“But what about that person named Cheongpung? Have you ever met him, Senior Brother?”

“Yes. Once, ten years ago.”

A disciple whom Sword Saint Mae Jonghak had raised like a son—like a grandson.

Baek Museong had been there that day ten years ago as well. The eyes of Huashan’s Lone Crane, Baek Museong, gleamed.

“I’m looking forward to it. I wonder how much he’s grown.”

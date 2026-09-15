# Checkpoint Review — 185–189

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

# Chapters 185–189

## Plot

Cheongpung is recognized as Mae Jonghak’s Disciple and Baek Museong’s Martial Uncle, but because he never underwent Huashan’s initiation ceremony, he is technically outside the sect. He refuses the Heavenly Sword True Person’s order to return to Huashan and chooses to remain with Jin Taekyung.

Taekyung reveals that the Fire King entrusted him with the Flame Divine Palm manual and the Unnamed Sword forged from Ten-Thousand-Year Cold Iron. Jin Wikyung orders Taekyung, Hyuk Mujin, and Cheongpung to keep the items and their connection to the Fire King secret. He also halts the interrogation of three surviving Dark Heaven remnants, preserving them as evidence while suspecting Shanxi was only the beginning of Dark Heaven’s plans.

At the Jin Family’s grand New Year’s banquet, Jin Wikyung publicly reaffirms the family’s place in Shanxi and accepts the Mount Heng Sword Sect as a vassal after Lee Seowol and First Elder Cheol Mubaek swear loyalty. He also wins support and gifts from former neutrals. Chulwoo falls intensely in love with Seowol and challenges Taekyung after seeing them interact. Chulwoo defeats numerous challengers, but Taekyung accepts the System Quest *There Is a Man Who Loved You So Much* and faces him.

Chulwoo’s incomplete Fist Qi cuts Taekyung’s spear down to a short rod. Taekyung spends his remaining stat points—twenty on Strength and fifty on Agility—and gains the advantage, ending the block by stabbing the back of Chulwoo’s neck while perched on his shoulder. The duel’s outcome remains unresolved.

## Continuity

- Jeok Cheongang, the Fire King, entrusted Taekyung with the Flame Divine Palm manual and the Unnamed Sword forged from Ten-Thousand-Year Cold Iron.
- Taekyung, Hyuk Mujin, and Cheongpung must keep the Fire King’s items and related information completely secret.
- Three Dark Heaven remnants remain alive under Wipeng’s custody; their restrictions prevented useful interrogation. Jin Wikyung suspects Dark Heaven’s Shanxi attack was only an opening move.
- Lee Seowol is eighteen and remains Sect Leader of the Mount Heng Sword Sect, now a vassal of the Jin Family. Cheol Mubaek is its First Elder.
- Chulwoo is twenty-five, Level 95, in love with Seowol, and capable of manifesting incomplete Fist Qi through his gauntlets.
- Choo Dohwan of the Iron Blood Sect is Level 65 and known as the Iron Fist; Chulwoo defeated him and at least fourteen other challengers.
- Taekyung accepted the quest *There Is a Man Who Loved You So Much*; refusing it would grant the System Title “Weak Male.”
- Taekyung has unlocked Sound Transmission but cannot yet use it reliably without practice.
- The identities of the figures behind the split human curtain at the Grand Training Ground remain unknown.
- Open hooks include Dark Heaven’s objective, the three remnants’ identities, Jeok Cheongang’s intentions toward Taekyung, completion of Taekyung’s commissioned weapon, the Treasured Jade’s whereabouts, consequences of Woo Hwangtae’s conflict, and the final result of the Taekyung–Chulwoo duel.

## Translation Decisions

- Render 화왕 as “Fire King,” 화염신장 as “Flame Divine Palm,” 만년한철 as “Ten-Thousand-Year Cold Iron,” and 이름 없는 검 as “Unnamed Sword.”
- Render 암천 as “Dark Heaven,” 전음 as “Sound Transmission,” 대연무장 as “Grand Training Ground,” and 권기 as “Fist Qi.”
- Render 입문식 as “initiation ceremony,” 본산 제자 as “main-sect Disciple,” 속가 제자 as “lay Disciple,” and 문적 as “sect registry.”
- Render 일장로 as “First Elder,” 가신 as “vassal,” and 철권 as “Iron Fist.”
- Retain “Martial Uncle,” “Martial Nephew,” and “Young Lady” for the established Huashan and Mount Heng relationships.
- Render 한 남자가 있어, 널 너무 사랑한 as “There Is a Man Who Loved You So Much” and 나약한 수컷 as the System Title “Weak Male.”

## Durable state

{
  "active_continuity": [
    "Jeok Cheongang entrusted Jin Taekyung with the Flame Divine Palm manual and the Unnamed Sword forged from Ten-Thousand-Year Cold Iron.",
    "Jin Wikyung ordered Taekyung, Hyuk Mujin, and Cheongpung to keep the Fire King's entrusted items and all related information secret; he described them as dangerous objects that awaken Greed and can drive people mad.",
    "Three Dark Heaven remnants survived interrogation under powerful restrictions; Wipeng was ordered to keep them alive as the Jin Family's only physical evidence.",
    "Jin Wikyung suspects Dark Heaven's attack on Shanxi Province was only the beginning and considers the Jin Family's victory suspiciously easy.",
    "Gong Yacheong, Socheon, and Soyul visited Taekyung at the Jin Family and were visibly healthier than before.",
    "Hyuk Mujin is on duty for the grand banquet and sent Socheon to deliver the banquet notice to Taekyung.",
    "Jin Wikyung admitted people beyond the invited guests to the grand banquet, and Taekyung was escorted to an honored seat with Baek Museong, Eunhyang, Chulwoo, and Cheongpung.",
    "Eunhyang's displayed Level is 75.",
    "More than three hundred Jin martial artists surrounded the Grand Training Ground and split a human curtain with a coordinated weapon display; the people behind it remain unidentified.",
    "Jin Wikyung publicly vowed that the Jin Family of Taiyuan would remain established in Shanxi three hundred years in the future as it had three hundred years in the past.",
    "Lee Seowol and the Mount Heng Sword Sect swore loyalty to the Jin Family of Taiyuan on New Year's Day, and the Jin Family accepted the sect as its vassal.",
    "Lee Seowol is eighteen and remains the current Sect Leader of the Mount Heng Sword Sect; Cheol Mubaek presented himself as its First Elder.",
    "Chulwoo is twenty-five, has fallen intensely in love with Lee Seowol, previously made a similar romantic declaration to another pretty third-generation disciple, and challenged Taekyung after seeing him interact with Seowol.",
    "Jin Wikyung is using the grand banquet to draw loyalty and gifts from former neutrals.",
    "Level 65 Choo Dohwan of the Iron Blood Sect, known as the Iron Fist, challenged Chulwoo and was defeated in roughly fifty exchanges.",
    "Chulwoo defeated at least fifteen duel challengers, including Level 25 Hwang Jinsu, before selecting Taekyung as his next opponent.",
    "Taekyung has unlocked access to Sound Transmission through reaching the Peak realm but has not yet learned to use it without practice.",
    "Taekyung accepted the Quest There Is a Man Who Loved You So Much and entered the duel with Chulwoo.",
    "Chulwoo's incomplete Fist Qi cut Taekyung's spear down to a short metal rod; Taekyung then allocated twenty stat points to Strength and fifty to Agility.",
    "The duel remains unresolved after Taekyung stabbed the back of Chulwoo's neck while sitting on his shoulder."
  ],
  "continuity_sources": [
    189
  ],
  "open_questions": [
    "What is Dark Heaven ultimately seeking, and why was Shanxi Province targeted?",
    "Who are the three surviving Dark Heaven remnants, and what can be learned from them?",
    "Who or what is revealed when the human curtain at the Grand Training Ground splits apart?",
    "Does Jeok Cheongang intend to take Jin Taekyung as his Disciple?",
    "When will Jang Taebo complete Taekyung's commissioned weapon?",
    "Who has the Treasured Jade, or was it lost by Jopil?",
    "What consequences will follow Woo Hwangtae's conflict with Chulwoo and the Jin Family?",
    "What is the final outcome of the duel between Jin Taekyung and Chulwoo?"
  ],
  "safe_through": 189,
  "temporary_decisions": [
    "Render 화왕 as “Fire King” and 화염신장 as “Flame Divine Palm.”",
    "Render 만년한철 as “Ten-Thousand-Year Cold Iron” and 이름 없는 검 as “Unnamed Sword.”",
    "Render 암천 as “Dark Heaven.”",
    "Render 전음 as “Sound Transmission.”",
    "Render 대연무장 as “Grand Training Ground.”",
    "Render 주모 as “Lady of the House.”",
    "Render 권기 as “Fist Qi.”"
  ],
  "version": 1
}

## Reading copies

## Chapter artifact 185

# Chapter 185

“Baek Museong, First-generation Disciple of Huashan, pays his respects to his Martial Uncle.”

“Who are you?”

For a moment, I thought the world had stopped.

Jin Wikyung and Wolhwa, who had been walking behind Baek Museong, stopped in their tracks. Even the pretty young woman following them came to a halt.

Of course, Chulwoo had the best reaction of all.

“Senior Brother, what are you talking about? Why is our Martial Uncle here?”

“Can’t you tell just by looking?”

“Which Martial Uncle?”

“Martial Uncle Cheongpung. The one standing to your right.”

Chulwoo glanced at Cheongpung, then burst out laughing as though he had just heard the funniest joke in the world.

“Ha ha ha! Senior Brother, you must be mistaken.”

“Second.”

“Enough. Wait, is this some kind of setup to mess with me?”

“It’s the truth.”

“Senior Brother, I’m not that gullible. Now that I think about it, the people of the Jin Family of Taiyuan are pretty playful too. Did all of you really conspire together just to fool me? Ha ha ha!”

“……”

What was this, some kind of Korean-Chinese co-produced drama?

There was no way Huashan and the Jin Family of Taiyuan had teamed up to plan the most hilarious hidden-camera prank ever just to fool this one guy.

“Ha ha ha.”

When no one—not even me—reacted, Chulwoo’s laughter gradually faded before cutting off completely.

“……You’re serious?”

Baek Museong rubbed his temple as he answered.

“Yes.”

“Not a single word of it is a lie?”

“As I said.”

Chulwoo whipped his head toward Cheongpung.

“Excuse me, Young Hero. What’s your name?”

“Cheongpung.”

A tremor ran through Chulwoo’s pupils. He had clearly remembered what he had said to Cheongpung just a few moments earlier.

“D-Dumpling.”

“Dumpling?”

“N-Nothing. Then is this really Martial Uncle Cheongpung?”

“Without a doubt.”

I almost wished I had some popcorn.

Leaving Chulwoo behind as he slapped his own cheeks over and over, apparently wondering whether he was dreaming, Baek Museong spoke.

“I apologize, Martial Uncle Cheongpung.”

Cheongpung answered with an innocent expression.

“No, it’s fine.”

“You failed to recognize an elder of our sect and committed a grave discourtesy. It is only right that you apologize a hundred times. Is that not so?”

“Please forgive me, Martial Uncle.”

Chulwoo lowered his head gloomily. Judging by his expression, he would need some time before he could accept that dumpling ghost as his Martial Uncle.

Of course, Cheongpung didn’t care in the slightest.

If anything, he was more curious about his relationship with these new faces.

“Who is everyone?”

“We are all Disciples of Huashan, just like Martial Uncle Cheongpung.”

“Oh. I’m just my grandpa’s grandson, though.”

The Sword Saint had not merely passed his martial arts on to Cheongpung as a Disciple. He had raised him as his grandson. That was why Cheongpung had only the vaguest understanding of sects and martial artists.

Yet Baek Museong did not lose his gentle smile at Cheongpung’s response.

“My Master goes by the title of the Heavenly Sword True Person. In terms of seniority, he is your eldest Senior Brother.”

“My eldest Senior Brother?”

“Yes. Your Master—or rather, your grandfather—the Sword Saint had three Disciples before you. Have you ever heard about this?”

Cheongpung murmured in a thoroughly uncertain voice.

“I don’t really know. I think I heard something about it from Grandpa once, but…”

“He even came to visit you with several others ten years ago.”

Cheongpung thought hard, then suddenly cried out.

“Ah! That scary-looking old man!”

The Sect Leader of Huashan, and Cheongpung called him a scary-looking old man.

Regardless of everyone’s shock, Cheongpung was delighted that the mystery had been solved.

“Is he my Senior Brother?”

“Precisely.”

“Ohhh. I see. I thought he was a bad person. It looked like he was trying to kick me and Grandpa out.”

“Martial Uncle may be unfamiliar with the circumstances of our sect. You can learn about those things little by little.”

What admirable patience.

Even if Baek Museong had slapped Cheongpung across the ear in the middle of the conversation, he probably would have been acquitted at the first trial. Yet he never lost his smile.

*No wonder there’s a crane in his epithet.*

As I was thinking that, Cheongpung turned to me with a bright smile.

“Benefactor, they say they’re my Martial Nephews!”

“Ah, yes. Congratulations.”

“Do you want to be my Martial Nephew too, Benefactor?”

“……Me?”

“Why? If you don’t want to be my Martial Nephew, I can make you my Martial Uncle.”

This crazy bastard was saying crazy things.

Not only was that not something Cheongpung could decide on his own, but being Cheongpung’s Martial Uncle would mean becoming a junior fellow Disciple of the Sword Saint, Mae Jonghak.

For all I knew, I could even order the Sect Leader of Huashan to run cigarette errands for me.

“……”

That actually sounded pretty good.

I was just about to nod as if under a spell when—

“Ha ha, Young Hero Cheongpung really, really knows how to joke.”

Wipeng’s mouth was smiling, but his eyes were saying something entirely different.

His glare looked like he wanted to tear me apart. I instantly came to my senses.

“No, it’s fine. I’m all right.”

“Really? What a shame.”

Unlike the other two members of the Three Plum Blossom Elites, who stood there with their mouths hanging open in bewilderment, Baek Museong only smiled.

“You may not be able to formally enter the sect, but we can certainly welcome you as an honored guest.”

I blinked.

“Was that a formal invitation?”

“Of course. A talented young martial artist like Young Hero Jin would always be welcome. And…”

His gentle voice continued.

“You could also serve as good company for Martial Uncle Cheongpung on his journey back to our sect.”

Cheongpung had been swaying excitedly, but his movements stopped abruptly.

“Huh? Return?”

“Yes, Martial Uncle Cheongpung.”

Baek Museong made a deep fist-and-palm salute. When he spoke again, his voice was stern and solemn.

“It is the Sect Leader’s order. Please return to Huashan.”

* * *

As Cheongpung disappeared into the main hall of the Jin Family of Taiyuan, Chulwoo clicked his tongue.

“What kind of guy—or Martial Uncle—is that?”

Eunhyang, who bickered with Chulwoo at every opportunity, nodded this time.

“Exactly. I didn’t know there was anyone who could refuse our Master’s order.”

“There is one person.”

“Who?”

“Grandmaster.”

“Senior Brother Chul, he doesn’t count.”

Chulwoo scratched the back of his head awkwardly.

“Well, that’s true.”

The Sect Leader’s authority was absolute. Even if someone ranked higher than him in terms of sect seniority, they could not openly refuse his orders.

Challenging the Sect Leader’s authority was no different from tarnishing the name of the sect.

That hierarchy was even more rigid in a major sect.

“But to reject it in one clean stroke… Whew. I knew he was unusual, but he’s even more extreme than I expected.”

“You’ve only seen the tip of the iceberg. Earlier, I even called him Dumpling—no.”

Chulwoo shook his head, then cautiously asked,

“What are you planning to do now, Senior Brother?”

“I don’t know.”

Baek Museong, who had been lost in quiet thought, finally spoke.

“I didn’t expect Martial Uncle Cheongpung to refuse so stubbornly.”

“At this point, shouldn’t the Disciplinary Hall step in instead of us?”

“Why do you think that?”

“He disobeyed our Master’s order.”

Even the slightest violation of Huashan’s rules resulted in a summons from the Disciplinary Hall. If that body, which dealt with even the smallest matters with ruthless precision, judged the case, Cheongpung would be no different from a serious criminal.

At the sight of his Junior Brother snorting through his nose, Baek Museong gave a quiet laugh.

“Martial Uncle did not violate the rules.”

“Pardon?”

“What do you mean?”

“The rules apply only to the Disciples of our sect. If a Disciple of Qingcheng Sect violated Shaolin’s rules, would he be punished?”

“Does that make any sense?”

“Of course it does. But Martial Uncle Cheongpung is… our Martial Uncle. He’s Grandmaster’s Disciple.”

“If only that were the case.”

Baek Museong added with a sigh,

“Strictly speaking, Martial Uncle Cheongpung is no different from an outsider. This happened because he never underwent the initiation ceremony.”

Every Disciple, whether a main-sect Disciple or a lay Disciple, underwent an initiation ceremony. Only then did they become Disciples of Huashan and have their names entered into the sect registry.

But Cheongpung was different.

“Who could have known Grandmaster would do something like that?”

Baek Museong remembered what had happened ten years ago with perfect clarity.

After the Sword Saint had lived in seclusion for many years, his Master, the Heavenly Sword True Person, had led several people in searching Huashan himself. At last, they discovered a residence where a ten-year-old boy was swinging a sword.

“It was utterly unbelievable.”

No one knew when the boy had arrived, where he had come from, or how he had been raised. Yet he had already learned Huashan’s treasured signature arts.

And the boy’s astonishing accomplishments were soon buried beneath the Sword Saint’s even more shocking declaration.

*You want me to initiate him?*

*Yes, Master. I intend to conduct the initiation ceremony and accept him as a main-sect Disciple. The order may be backward, but we can’t ignore a genius of the ages like that—*

*Ignore him.*

*Pardon?*

*I said to continue ignoring him. When the time comes, I’ll send him over myself.*

*M-Master!*

*And don’t come looking for him again. Not unless you want me to set the whole place on fire.*

*Set fire to Huashan? Are you saying we should all die together?*

*Oh. Now that you mention it, I suppose we would. Anyway, take it that way. I’ll take responsibility for Cheongpung, that child.*

Chulwoo and Eunhyang both gaped at him.

“D-Did he really say that?”

“Are you sure you’re not exaggerating?”

“I wish I were exaggerating… but don’t you know what happened afterward?”

Cheongpung, whom the Sword Saint had said he would send over when the time was right, had slipped out into the world without anyone noticing, and the Sword Saint had vanished without a trace.

“The truth is, our Master isn’t worried about Grandmaster. He’s worried about Martial Uncle Cheongpung.”

Cheongpung had already demonstrated unbelievable accomplishments ten years ago. But the world—and Murim in particular—was overflowing with all kinds of sinister schemes.

It was far too dangerous for someone who wasn’t a Disciple of Huashan to wander the world while possessing Huashan’s secret arts.

“We must bring Martial Uncle Cheongpung back. For his sake, and for the sake of our sect. Do you understand?”

The two nodded at his resolute voice, then suddenly spoke up.

“But, Senior Brother…”

“How are we supposed to bring him back? By force?”

“That…”

Baek Museong hesitated before letting out a deep sigh.

“First, we need to bring the Sleeping Dragon of Shanxi over to our side.”

All three of them remembered Cheongpung’s final words at the same time.

*I’m staying with my Benefactor!*

The Sleeping Dragon of Shanxi, Jin Taekyung.

Faced with this unexpected obstacle, Baek Museong felt a throbbing pain in his head.

*What kind of help did he receive for Cheongpung to call him his Benefactor? Could he have saved his life?*

A bond that had begun with a few candied hawthorn skewers[^1] was proving more tenacious than expected.

* * *

The moment we entered the main hall, Wipeng abruptly asked,

“What on earth did you do?”

“What do you mean?”

“I’m talking about Young Hero Cheong.”

Everyone’s eyes naturally turned toward Cheongpung.

He was stuffing the refreshments from the table into his mouth until his cheeks bulged.

“I didn’t really do anything.”

“Young Hero Cheong defied the Sect Leader’s order. He said he would stay with the Third Young Master.”

“So?”

“What do you mean, ‘so’? Don’t you understand that if you make some needless mistake, it could sour the relationship between our family and Huashan?”

*Is this like when a top student’s grades fall and his parents start hating his friend?*

I shrugged.

“I’ll persuade him somehow.”

“You must. You absolutely must persuade him.”

Wipeng’s voice was filled with firm resolve. He whipped his head toward Jin Wikyung, who was seated in the place of honor.

“My lord, please say something as well.”

“Very well.”

Jin Wikyung put on a solemn expression and parted his lips.

“Youngest. Your face has gotten so haggard in just a few days. Was the journey uncomfortable? Do you know how worried I was…?”

“Stop. I was an idiot for trusting you, my lord.”

“Don’t be so hard on him. The youngest will handle things properly on his own.”

“This is driving me insane. As of today, I’m leaving the Jin Family of Taiyuan.”

“Ha ha ha. This friend knows how to tell a joke.”

“Did that sound like a joke?”

“Yes. It was very funny.”

“I’m not amused. I haven’t been amused since yesterday noon, when the Third Young Master was late despite promising to return by then.”

Jin Wikyung’s eyes widened.

“Oh, that reminds me, youngest.”

“As you promised last time, please scold him thoroughly this time.”

“What’s that sword strapped to your back? It looks like you had it made while you were away. Let me take a look.”

Unable to contain his anger, Wipeng shot to his feet.

“I’m really leaving. It was filthy being with you, so let’s never see each other again.”

“Ha ha ha. What’s gotten into that friend today? Why is he making me laugh so much?”

“Damn it. Draw your sword.”

“Taekyung, Wipeng seems eager to see your new sword. Would you draw it for him?”

“Aaaaaah!”

With his eyes rolling back, Wipeng let out a shriek and placed his hand on the sword hilt.

But the next words I spoke made his body freeze.

“Since it’s something the Fire King gave me, I think it would be best not to touch it if possible.”

“……?”

“……?”

Jin Wikyung and Wipeng blinked silently before finally managing to speak.

“F-Fire what?”

“Third Young Master, what kind of nonsense are you talking about?”

“The Fire King. Fire King. He entrusted a sword to me. Oh, and a martial arts manual too.”

*Thunk. Clang.*

In the suffocating silence, the sound of Wipeng dropping his sword rang out like thunder.

[^1]: Candied hawthorn skewers are a traditional snack made by coating hawthorn fruit on skewers in hardened sugar.
## Chapter artifact 186

# Chapter 186

Jin Wikyung and Wipeng.

As the conversation continued, the emotions of the two men became increasingly obvious.

Shock. Disbelief. And then shock all over again.

“Th-That’s really true?”

I had talked for so long that I felt completely drained. Tired, I answered,

“It’s a hundred percent pure truth, so believe me.”

Wipeng, who had been staring blankly into space, suddenly lunged at me.

“Third Young Master. If all of this is a lie, then I’m really going to die—and so are you.”

“I said it’s a hundred percent. A hundred percent!”

“No, but still…”

“Ah, I mean a hundred percent truth with not a speck of lies mixed in. What the hell!”

“……”

Wipeng paused with an expression that seemed to say, *Why do I suddenly feel so disgusted?*

I waved the sword and martial arts manual at him.

Now more than ever, I couldn’t give him time to mull it over.

“If you’re really suspicious, inspect them yourself. The Flame Divine Palm manual, and a sword made of Ten-Thousand-Year Cold Iron!”

“Gasp! Put them away. Quickly!”

Even if someone shoved a cross in a vampire’s face, they probably wouldn’t react this strongly.

“What’s wrong?”

Wipeng answered with a horrified expression.

“You’re telling me to inspect the Flame Divine Palm manual? Have you decided to destroy our entire family?”

“Oh, right. That’s how it was.”

Anyone who stole a look at the Fire King’s signature martial art would get a taste of the heat—enough heat to burn their whole body.

“Regardless, everything is true. We have witnesses here, too. Right?”

Hyuk Mujin, who had been sitting in the corner like a corpse, cautiously raised his hand.

“Pardon me for interrupting, but everything is true.”

Cheongpung, who had been stuffing his mouth with snacks of unknown variety, spoke with a serious expression.

“Uh-oh-wa-uh-oh!”

“……”

That testimony probably wouldn’t carry much weight. More importantly, how long was that guy planning to keep eating those snacks? Was he some kind of inexhaustible jar?

“Wipeng, I believe Taekyung’s story really is true.”

At Jin Wikyung’s words, Wipeng nodded with a complicated expression.

“Yes. It’s a truth that’s nearly impossible to believe, but there’s no choice except to believe it.”

“The Fire King. The Fire King himself.”

Jin Wikyung let out a long breath. After hesitating, he reached for the Unnamed Sword resting on the table.

*Shing.*

The pure-white blade emerged from its rough scabbard.

As Jin Wikyung gazed at the sword, which radiated a frost-like sharpness, he murmured,

“It smells of blood.”

I had momentarily forgotten.

Before he was the Lesser Family Head of the Jin Family of Taiyuan, Jin Wikyung was a swordsman.

Unlike me, he didn’t need to look at an Item description window to accurately read the weapon’s condition. He slid the sword back into its scabbard.

“Taekyung.”

“Yes.”

I straightened my posture.

The fact that Jin Wikyung had called me by my name instead of *youngest* meant that he was about to say something serious.

“Do you know what these things are?”

“A precious treasure, aren’t they? The kind that would be difficult to obtain even if you spent a thousand nyang of gold.”

A Supreme Peak martial art that could let its wielder look down on the entire world, and a peerless sword forged from Ten-Thousand-Year Cold Iron.

The Murim martial artists I knew would risk their lives to obtain these things.

Jin Wikyung shook his head.

“Wrong.”

“Pardon?”

“These are ghostly objects. They take away a person’s soul and drive them mad.”

“Oh.”

“Do you know the name of that ghost?”

I muttered softly,

“Greed.”

“That’s right. Greed. A tenacious and dangerous creature dwelling in everyone’s heart.”

I knew.

I had experienced it firsthand, so there was no way I couldn’t.

On that day several years ago, greed had taken root in my heart, and because of it, I had lost people close to me.

“I don’t know what intentions the Fire King had when he entrusted these dangerous objects to you, but… everything related to this must be kept completely secret. Do you understand?”

His gaze and posture were directed solely at me, but his words were meant for everyone in the room.

Me, Hyuk Mujin, and finally Cheongpung.

As though we had made a promise, we answered at the same time.

“Yes.”

“I’ll keep it in mind, Lesser Family Head.”

“Ah-uh-ah-hae-ho, ma-ah-hae-oh.”

……

That damn mouth of his. I ought to just…

* * *

Jin Wikyung lifted the thick curtain. Through the latticework window, he could see Jin Taekyung’s back growing more distant.

Sunlight struck the rough scabbard strapped to Taekyung’s back and shattered into fragments.

“The weather is fucking beautiful.”

“Didn’t you say it was fantastic earlier?”

“That was then. It’s basically the same thing.”

“This feels a little different.”

“Don’t nitpick when you already know what I mean. Come to think of it, why is the person who said he was leaving still here?”

Wipeng answered in a weary voice.

“You’re the one nitpicking, my lord. My head is already complicated enough.”

That applied to both of them.

Jin Wikyung murmured with a face that looked ten years older.

“What on earth is happening?”

“I’m curious about that myself.”

When he looked back over everything that had happened to the Jin Family of Taiyuan over the past year—or rather, the past six months or so—it was enough to make him wonder whether some demon had gotten involved.

“Now even the Fire King has appeared.”

“I’ve heard he has an exceptionally eccentric temperament. I’m worried he might bring calamity down on our family.”

“We have to turn this crisis into an opportunity.”

Jin Wikyung gently caressed his teacup. To anyone else, he might have appeared lost in thought, but his lips were moving almost imperceptibly.

*How is that matter progressing?*

Wipeng understood the meaning of the Sound Transmission and acted naturally.

“The tea has gone cold. Shall I have them bring out a fresh cup?”

*We haven’t learned anything yet.*

“It’s fine. It’s still drinkable.”

*What about the surviving remnants?*

“You’ll ruin your health if you keep doing that.”

*Most of them died during the interrogation.*

“You’re the only one who worries about my health.”

*So, how many are left?*

“Shouldn’t I at least look after you, with the Lady of the House not here?”

*Three.*

Jin Wikyung’s fingers stopped dead.

The news was so unexpected that, for a moment, he even forgot that he was supposed to continue speaking.

*Only three?*

Wipeng sighed and nodded.

*They had a far more powerful restriction placed on them than expected. I’m sorry to say this, but… my abilities aren’t enough.*

*It isn’t your fault. Our family’s capabilities are lacking.*

*Give me your orders.*

Jin Wikyung felt his throat grow dry.

*Stop the interrogation. Keep them clinging to life by whatever means necessary. Right now, those men are our only physical evidence.*

*Understood.*

He closed his hand around the cold teacup.

On the trembling surface of the tea, a distorted face with no discernible features was reflected.

Just like those men.

*Dark Heaven…*

He didn’t know where, how, or why they had done such a thing.

He was flailing at empty air without learning a single thing.

Yet one suspicion in Jin Wikyung’s mind was gradually hardening into certainty.

*They’re extremely dangerous. Targeting Shanxi Province was only the beginning.*

The Head Elder had endured for many years while waiting for his moment. But for a decades-long grand design, the results were far too shabby.

Jin Wikyung realized that only after the joy of victory had faded.

*This was… too easy.*

It had been a perfect opportunity to seize an entire province.

Yet Dark Heaven had never revealed themselves. It was as if this much had been enough for them.

*What on earth are they after?*

For now, he had no idea.

He could only hope that he had overestimated them.

“My lord?”

“Ah.”

“You’ve been away from your seat too long. The guests are waiting.”

“……Is that so?”

At Wipeng’s call, Jin Wikyung drained his teacup in one gulp and rose.

“Let us go.”

This was a gathering for the Jin Family.

For now, it was all right to savor the joy of victory to his heart’s content.

* * *

Winter days were short.

I had only just returned to the Jin Family of Taiyuan, but the sun was already beginning to set.

*Come to think of it, aside from circulating my qi, I haven’t had a proper training session in days.*

It was around then, while I was training in the ground attached to my pavilion to loosen up my body, that some unexpected guests came to see me.

“Benefactor!”

“Benefactor!”

“……?”

Was that an echo or something?

I turned my head toward the direction of the voices.

“I’m here!”

Cheongpung was smiling brightly, his mouth covered in a thick layer of some mysterious sauce. And then there was…

“Benefactor! It’s Socheon!”

“It’s been a while, Young Hero Jin.”

“Huh?”

They were the survivors of the Sakju Branch, Gong Yacheong and Socheon.

Seeing their familiar faces after so long, I felt a sudden rush of happiness.

*But it feels like someone’s missing.*

Just as I was tilting my head in confusion, a whining voice came from beneath the stone wall blocking my view of them.

“Me too! Soyul wants to see Uncle too!”

“Wait a moment.”

Gong Yacheong reached down, scooped something up, and hoisted it onto his shoulders.

The small girl, Soyul, smiled brightly and waved her hand.

“Uncle!”

“Oh, you’ve grown a lot.”

“You’ve grown a lot too, Uncle!”

“Thanks for that. But I’m not an uncle.”

“Anyone can see you’re an uncle!”

“……Sure.”

What did it matter whether I was an uncle or not?

I let out a quiet laugh and walked toward them.

“Has everyone been well?”

Gong Yacheong answered with a faint smile.

“Of course.”

He still looked somewhat gaunt, but his complexion was healthy. He was clearly much better than when he had been poisoned and hovering on the verge of death.

*The kids seem to be doing well, too.*

Socheon was in the middle of his growth period, and in the time since I had last seen him, he had grown another half a handspan taller. Soyul’s cheeks were plump.

And Cheongpung’s stomach had puffed up as though he had been eating well.

“……”

Right. Eat well and grow well.

Twenty was still a good age for growing.

“But what brings everyone here?”

Socheon spoke as though he had been waiting for me to ask.

“Martial Artist Hyuk asked us to come. The banquet is about to begin, but he has to go stand watch, so he asked us to deliver a message to you in his place.”

“Oh, the banquet.”

I vaguely remembered hearing something about it earlier. There was supposed to be a grand banquet in the evening.

Cheongpung, who had been licking the sauce from around his mouth, suddenly looked shocked.

“Gasp! Really?”

“……What? Didn’t you come here knowing that?”

“Yes. If I’d known, I would have eaten less!”

Soyul also opened her eyes wide in shock. The candied treat in her hand slipped to the ground.

“No! Soyul’s full too!”

“……”

Judging from their reactions, I could roughly guess where the two of them had met.

“Well, when does it start?”

“Less than half an hour remains, Benefactor.”

“Benefactor, hurry! This is my first banquet!”

“Where is it?”

“In front of the new Grand Training Ground, Benefactor.”

“They said it’s in front of the Grand Training Ground, Benefactor!”

“Ah, there.”

I set down the training spear I was holding and tightly secured the bundle I had laid out beside me to my back.

Of course, the item inside the bundle was the sword entrusted to me by the Fire King.

“Let’s all go.”

I was about to set off when I stopped.

I had thought of something I had wanted to say for a while.

“Oh, and one more thing…”

“Please speak, Benefactor.”

“What is it, Benefactor?”

I let out a deep sigh before continuing.

“Only one of you should call me Benefactor. It’s confusing.”

They were exactly like two parrots.

The two Benefactor parrots nodded as though they didn’t need to think about it.

“I’ll keep that in mind, Benefactor.”

“Okay, Benefactor.”

“……”

No, think before you answer.

* * *

The Grand Training Ground.

As its name suggested, it was the largest training ground in the family, and it was packed with people.

“What the hell? Why are there so many people?”

Weren’t only invited guests allowed inside?

Cheongpung was the one who answered my question.

“I heard it from the cook earlier. He said the Lesser Family Head told them that everyone should be together on a day this wonderful, and ordered them to let in all the people outside, too.”

“All of them?”

“Yes. So the cook got really angry. He said the Lesser Family Head had no common sense and shouldn’t run his mouth when he wasn’t going to help with the cooking.”

Soyul, who had been sucking happily on a candied treat, chimed in.

“That’s right! He even gave Soyul a candied treat and told her not to tell anyone!”

“……Then why are you telling us?”

“Gasp!”

I shook my head and continued walking.

I had only taken a few steps when a martial artist from the Jin Family approached us.

“We’ll escort the two Young Masters to their designated seats.”

“I don’t mind watching from anywhere. I’m guessing that won’t be allowed, right?”

“No, Young Master. It is the Lesser Family Head’s order.”

Given the circumstances, there was nothing I could do.

I exchanged a light farewell with Gong Yacheong and the others before moving to the seat prepared for me.

My seat was one of the places of honor reserved for the very small number of distinguished guests.

Of course, that meant…

“Martial Uncle Cheongpung, Young Master Jin. We meet again so soon.”

The Three Plum Blossom Elites were among them.

Baek Museong had his junior disciples seated on either side of him. He greeted us with a fairly friendly expression.

“We didn’t get to properly introduce ourselves earlier, did we? I’m Eunhyang.”

> **System**
> **Level:** 75  
> Eunhyang

She was probably around the same age as my younger sister, Hayeon.

The moment I finished greeting her, a sullen voice burst out.

“Damn it. You’re sitting next to me?”

Chulwoo was a massive man, large enough to make the seat look cramped.

“Why? You don’t like it?”

“Would you?”

“I don’t like it either. That’s why I said it. Guess we agree on something.”

“Don’t say disgusting things!”

“Then switch seats.”

“With whom?”

“Lots of people besides you would love to sit there. Switch with anyone standing down below.”

“You son of a bitch!”

“Did you just insult my parents? Are you trying to pull a Jin-rula in the Jin Family of Taiyuan?”

Chulwoo’s body trembled as Baek Museong scolded him.

“You! What kind of outrageous nonsense is this?”

“No, Senior Brother. It’s just…”

“Quiet. Young Hero Jin, I apologize in place of my Junior Brother. I also apologize to Martial Uncle Cheongpung.”

Cheongpung, who had been hiding behind me, cautiously peeked his head out.

“I’m fine, Martial Nephew.”

I also smiled gently.

“I’m fine too. Aren’t you at the age when your blood is running hot? We have to be understanding.”

“You’re five years younger than me, you little punk. What did you just say?”

“Young Hero Baek, if you don’t mind, could you switch seats with me? I’m a little afraid to sit next to him…”

“Second!”

“Whoo. Whoo-hoo.”

I dropped into the seat beside the snorting Chulwoo.

Chulwoo on my right, Cheongpung on my left.

What a spectacular arrangement.

*Where is Jin Wikyung?*

No matter how much I looked around, I couldn’t see Jin Wikyung or Wipeng.

Then—

*Boom!*

The martial artists of the Jin Family surrounding the Grand Training Ground began striking their weapons.

There were more than three hundred of them, and from their ranks surged an aura sharp as a blade and a spirit as powerful as a wave.

*Boom! Boom! Boom!*

The sound resembled the drums of a battlefield. It grew louder and louder until it swallowed every other noise.

And then…

*BOOM!*

With a thunderous crash louder than any before it, the human curtain split apart.
## Chapter artifact 187

# Chapter 187

Hundreds of martial artists stood there, radiating an aura as sharp as frost. And along the path they had created, one man came walking.

*Clomp. Clomp.*

The commoners who had come to watch, the nameless martial artists dressed in worn uniforms, and finally the powerful figures who moved Shanxi Province—

Everyone held their breath and watched one man.

Jin Wikyung.

*This feels like a scene from a movie.*

Wearing a martial uniform embroidered with a silver wyvern, Jin Wikyung walked without hesitation. His dignified bearing and the authority that naturally radiated from him overwhelmed everyone present.

The silence Jin Wikyung had created was broken by his voice.

“Our family has put down roots in Taiyuan for three hundred years.”

His shout, infused with profound internal energy, spread far and wide.

“Our beginnings were undeniably humble.”

It had been a time of chaos. Natural disasters had continued one after another, and the empire that had seemed eternal had lost its strength. Countless heroes raised their banners across the land and claimed to be kings, and war broke out.

Blood soaked the parched earth in place of water, while grain that should have been harvested was trampled beneath horses’ hooves.

At the end of that long war, a man who had wandered the world stopped walking in the ruined capital of an old dynasty.

That was the beginning of the Jin Family of Taiyuan.

“Our ancestor, Grand Patriarch Jin Muryang, accepted orphans and cared for widows and the elderly. Though he raised martial arts as our banner, he never forgot humanity.”

The small seed quickly sprouted. Those who gathered beneath the banner of the Jin Family of Taiyuan became its branches and trunk, and eventually its strong, deep roots.

The family that had begun so humbly grew into a towering tree that encompassed all of Shanxi Province.

“However, our family could not escape the rise and fall of fortune.”

Everything had slowly changed with the passage of time. After enduring one event after another, both great and small, the towering tree began to wither.

The wrong choices of the leadership, invasions by foreign enemies, betrayal by allies, natural disasters beyond human power to prevent…

Before long, its many branches had broken, and its lush leaves had fallen.

“But!”

A thunderous shout burst forth. His voice boiled like lava.

“We survived.”

Even when the branches broke and the leaves fell, the roots remained whole.

“Though we were shaken, we were never uprooted.”

As long as the roots remained, the tree would grow again. It would regain its vitality and sprout abundant leaves as though nothing had ever happened.

Just as it was doing now.

“As the Lesser Family Head of the Jin Family of Taiyuan, I swear this.”

*Boom!*

Hundreds of weapons struck the ground. Invisible heat rose from the martial artists of the Jin Family of Taiyuan, all of whom had dropped to one knee.

“We! The Jin Family of Taiyuan!”

It was a vow to the countless members of the Jin Family, to everyone gathered here, and to the enemies who had yet to bare their fangs.

“Three hundred years ago and three hundred years from now, we will remain here unchanged!”

*Boom! Boom!*

“I ask all of you!”

His blazing eyes swept across the crowd. Jin Wikyung took in the faces filled with a mixture of excitement and anticipation, fear and guilt, then shouted.

“Are you ready to lay a new foundation stone together with our family?”

A tremendous roar erupted from the crowd, centered on the martial artists of the Jin Family of Taiyuan.

“Loyalty!”

*Boom, boom-boom-boom-boom-boom!*

Just then, a clear voice rang out from somewhere.

“May we join the path the Jin Family of Taiyuan wishes to walk?”

The voice had come neither from the seat of honor where I sat nor from the honored guests’ seats below.

As the enormous crowd surrounding the Grand Training Ground opened a path, the owner of the voice appeared.

*That person is…*

Instead of a flowing gown, she wore a comfortable martial uniform. Her mature features seemed beyond her years as she respectfully saluted Jin Wikyung with clasped fists.

“I am Lee Seowol of the Mount Heng Sword Sect. I have arrived in response to the Lesser Family Head’s summons.”

The middle-aged man who had been standing beside her like an iron tower revealed his identity in a rough voice.

“I am First Elder Cheol Mubaek. I pay my respects to the Lesser Family Head of the Jin Family of Taiyuan.”

The martial artists of the Mount Heng Sword Sect standing behind the two of them shouted in unison.

“We pay our respects to the Lesser Family Head!”

A stir spread through the crowd.

The appearance of the Mount Heng Sword Sect, which stood on the verge of destruction.

The new Sect Leader was the only daughter of the late Blood Wolf Sword, while the man who called himself the First Elder at her side was the Tiger of Mount Heng, Cheol Mubaek.

And yet, amid everyone’s astonishment, Jin Wikyung’s expression remained calm.

Of course it did. He was the one who had sent me to deliver the New Year’s Day invitation.

“This is the first time I’ve met you in person, Young Lady. Did you receive the formal invitation I sent last time?”

“Yes. In addition…”

Lee Seowol answered calmly before raising her head and looking this way.

“I have also received a debt of gratitude I could never hope to repay.”

Her gaze flew toward me, making my face prickle.

Naturally. There probably wasn’t a single person in Shanxi Province who didn’t know that Jin Mukyung and I had saved the Mount Heng Sword Sect.

After giving me a faint smile, she looked back at Jin Wikyung.

“I would like to hear your answer to the question I asked earlier.”

Lee Seowol took a deep breath. Her eyelids trembled.

“May we… join the Jin Family of Taiyuan as well?”

Jin Wikyung’s answer contained not a shred of hesitation.

“Of course.”

“……!”

“This time, I’ll ask you. Are you ready to walk alongside our family?”

*Thump.*

Instead of answering, Lee Seowol dropped to one knee. Cheol Mubaek and the martial artists under his command did the same.

“I, Lee Seowol, the second Sect Leader of the Mount Heng Sword Sect, swear before Heaven and Earth.”

The Mount Heng Sword Sect had once commanded all of Shanxi Murim. Its new Sect Leader, inheritor of its true line, had knelt before Jin Wikyung.

No. She had knelt before the Jin Family of Taiyuan.

“Our sect will dedicate its loyalty to the Jin Family of Taiyuan.”

“Loyalty!”

Their numbers were small, but their shout was thunderous. Jin Wikyung grasped Lee Seowol’s shoulder and helped her to her feet.

His manner of speech had naturally changed as well.

“I grant you permission.”

It was New Year’s Day.

The moment the Jin Family of Taiyuan accepted the Mount Heng Sword Sect as its vassal.

* * *

“Waaaaaaah!”

“Jin Family of Taiyuan! Jin Family of Taiyuan!”

Cheers, followed by more cheers.

The crowd of more than a thousand people enthusiastically chanted the name of the Jin Family of Taiyuan.

*It really was that impressive.*

A speech that made the blood of everyone listening boil, followed by the Mount Heng Sword Sect’s oath of loyalty.

*What an ending.*

The actual banquet hadn’t even begun, but everyone here must have realized it.

The Jin Family of Taiyuan was the hegemon of Shanxi Province, combining overwhelming strength with mercy.

Chulwoo, seated beside me, was no exception.

“……Huh.”

The guy who had seemed simpleminded and proud to a fault wore an expression of genuine admiration.

*The kid knows a thing or two.*

It was childish, but I couldn’t help puffing out my chest a little. I was a member of the Jin Family of Taiyuan, after all, and I had contributed quite a bit to making this day possible.

“Ahem, ahem. Looks like you were moved.”

“It was truly amazing. My heart pounded the entire time I watched.”

Chulwoo continued in a voice brimming with excitement.

“How can someone be so beautiful!”

“Not to brag, but the Jin Family of Taiyuan is doing this well in Shanxi—what did you say?”

What had I just heard?

After some hesitation, I asked in an uneasy voice,

“You’re not talking about my eldest brother, are you?”

“What?”

“You know, that sort of thing. *I covet that man’s muscles. I want to do bench presses with him and strip each other’s Under Armour.* Something like that…”

“What the hell are you talking about?”

Chulwoo frowned. Judging by his expression, that wasn’t what he meant.

“Good. That’s a relief. I thought you were gay.”

“Gay? What’s that?”

“Well, to use an analogy, I suppose it’s the process by which a pair of Diglett meet and become Dugtrio.”

“I can’t understand a word you’re saying. Explain it simply.”

I thought of the simplest word.

“Male homosexuality.”

“You little bastard…!”

Chulwoo was about to raise his fist when he stopped short. Baek Museong, his Senior Brother, was sitting right beside him.

*The Huashan’s Lone Crane buff was damn useful.*

I grinned and asked,

“So what exactly is beautiful?”

“The woman! That woman who came from the Mount Heng Sword Sect!”

“Oh, Young Lady Lee Seowol?”

Strictly speaking, she was the Sect Leader, but calling her Young Lady still felt more comfortable.

At my rather familiar tone, Chulwoo’s eyes lit up.

“Y-You know her?”

“We have a little history.”

“What kind of history?”

A history that began with a sexual harassment scandal and ended with a proposal, maybe.

“It’s a pain to explain. It’s a long and eventful story. But are you perhaps…”

I let my words trail off and looked at Chulwoo.

“Interested in this Young Lady?”

“Interested?”

Chulwoo sprang to his feet, and I felt slightly reassured.

“Right? I thought you were talking about your heart pounding and all that, so I thought you were really interested…”

“It isn’t interest! This is love.”

“……”

“Three children would be about right. Two boys and one girl.”

“……Sure. Go on, then.”

“I’ll raise a yellow dog, too. I heard that raising children alongside a dog from a young age is good for their emotional development. We’ll have a happy family.”

I was about to call him an idiot when I suddenly stopped.

*I feel like I’ve seen this scene somewhere before.*

Where had it been?

For some reason, I felt a strange pang.

Why was I suddenly thinking of Song-i and Uncle Kkeokjeong, who should have been in the real world?

*That’s strange.*

I pushed the question aside and opened my mouth.

“Are you done?”

“I’m not done yet.”

“Then let’s consider it done and you listen to me. This is important.”

At my serious tone, Chulwoo paused.

“Important?”

“Yeah. How old are you?”

“Twenty-five.”

“Do you know how old Young Lady Lee is?”

“I don’t.”

“She’s seventeen. Ah, the year has turned, so she’s eighteen now.”

“So?”

“What do you mean, so, you atrocious bastard! Never mind the seven-year age gap—school lunches and late-night self-study! Huh? She’s at the age when she has to choose between the humanities and sciences! What about her school grades?”

Chulwoo looked baffled by my anger.

“What are you talking about? She’s at the perfect age to get married.”

“Ah, sorry. I got too worked up.”

As the older brother of a younger sister who was still in school, I couldn’t help empathizing. I kept forgetting that this was the Murim.

“Anyway, think it over carefully. Don’t let a fleeting emotion sway you.”

“No.”

Chulwoo answered firmly, his expression growing dreamy.

“I knew the moment I first saw her. My heart, which had been stopped my entire life, began to beat.”

“……So was it dead for twenty-five years?”

“Dead? Yes, you’re right. Before meeting her, I was no different from a corpse.”

“Can you really not die? Please die.”

“I can’t. I’ve become a man who can neither die nor live without her permission.”

“……Wow. What a load of bullshit.”

Baek Museong and Eunhyang, who had been listening to our conversation, shook their heads.

“Here we go again.”

“Big Brother, didn’t you say something similar to one of the pretty third-generation disciples last year?”

*He’s even a repeat offender?*

*What are you, some serial confession demon?*

Just as Chulwoo was about to explode at Eunhyang’s revelation of his embarrassing past—

“Young Master Jin.”

A pleasant, beautiful voice reached my ears. I turned my head and saw a woman climbing the stairs.

No. A girl.

*Lee Seowol.*

It was her.
## Chapter artifact 188

# Chapter 188

Dressed in a martial uniform, she looked more mature and beautiful than the last time I had seen her.

The closer she came, one step at a time, the more a faint fragrance reached me.

*Honestly, I can see why Chulwoo fell for her.*

Not just Chulwoo—half the men gathered at the Jin Family of Taiyuan might be sizing up their chances of confessing to her.

*And a girl like that proposed to me.*

She was still just a kid, and the proposal had been little different from an offer of a political marriage, but I couldn’t help feeling strangely about it.

At last, she reached me and greeted me.

“It’s nice to see you again. Have you been well?”

“Yes. What about you, Young Lady Lee?”

The words were barely out of my mouth before I realized my mistake. Her family had been killed, and her sect had nearly been annihilated. There was no way she could have been well.

“Uh…”

As I stood there flustered, Lee Seowol answered.

“I’ve been well. Thanks to Young Master Jin.”

With a light smile, she added,

“And I will continue to be.”

There was a steely resolve in her voice. It felt as though she had grown another step through the crisis that threatened to destroy her sect and the difficult decision to swear loyalty.

I answered her sincerely.

“I hope so.”

Lee Seowol gave a faint smile and nodded. That was when—

“H-Hey, Taekyung!”

“…What are you doing?”

I stared at Chulwoo with disbelief. He had thrown an arm around my shoulders with an expression and tone so awkward they were painful to witness.

“You’re in the way. Move your arm.”

“H-Hahahaha! What’s gotten into you? We’re childhood friends. What’s wrong with this much?”

“Weren’t we sworn enemies?”

“M-My friend, your jokes have improved tremendously! Hwa-ha, hahahaha!”

“Does that sound like a joke to you?”

“Ha! By the way, who is this beautiful lady?”

“…So that was your purpose.”

The fabric of space-time cringed. After putting on a spectacularly bad performance, Chulwoo bowed ninety degrees toward Lee Seowol.

“Hello! It is an honor to meet you!”

“Ah… yes. It’s an honor for me as well.”

“If I may introduce myself, I am this man’s friend of ten years—”

To help the flustered Lee Seowol, I added,

“I met him for the first time today.”

“Although we only met today, we have built a friendship deep enough to call ourselves friends of ten years—”

“We’re not close at all.”

“S-Since this is fate, perhaps you would sit beside me—”

“He’s making a pass at you because he thinks you’re pretty. Don’t fall for it.”

Chulwoo ground his teeth, while Lee Seowol opened her eyes wide.

“Oh, really?”

“Yes. Can’t you tell just by looking at him?”

There was such a thing as being too oblivious. If she couldn’t even notice something this obvious, it was a problem.

As I sighed, Lee Seowol stepped closer.

“No. I meant something else.”

“Pardon?”

“Do you think I’m pretty, too, Young Master Jin?”

“Wait. Hold on.”

Her voice was alluring, and her eyes sparkled.

*What’s with her? Why is she acting like this?*

As I stood there with Lee Seowol, Chulwoo’s gaze sank into gloomy despair.

* * *

“Waaaaah!”

“Drink! Drink!”

The atmosphere at the Grand Training Ground was incredible, to put it mildly. The dance troupe—or rather, the dancers—brought in from Honghwaru captivated everyone’s attention with their dazzling movements, while the crowd ate, drank, and enjoyed themselves.

Even the honored guests, who had looked uncomfortable at first, soon began to relax.

*Those bastards should be down on their knees with their heads to the floor, and even that wouldn’t be enough.*

Many of the honored guests owed the Jin Family of Taiyuan a debt, yet they had remained neutral during the recent war.

Neutral was a generous way to put it. They had simply withdrawn because they were afraid of retaliation from the Mount Heng Sword Sect.

*They must feel safe now that the Jin Family has accepted the Mount Heng Sword Sect.*

In front of those very people, Jin Wikyung had embraced the Mount Heng Sword Sect, the Jin Family’s greatest enemy, and seated Lee Seowol in a place of honor.

It meant that the Jin Family would no longer hold them accountable for what had happened.

Naturally, a warm current flowed through the honored guests. Their swift oaths of loyalty were followed by a barrage of gifts.

“Lesser Family Head, the Sangdo Sect and I wish to place ourselves under the Jin Family of Taiyuan.”

“Oh, how kind of you.”

“This is a small gift I prepared as a token of my sincerity.”

“Thank you, Sect Leader Hwang.”

“Great Hero Jin, I am the one leading the merchant guild…”

“It is a humble offering, but please accept it…”

It didn’t take long for luxury goods, gold, and silver treasures to pile up like a mountain. I doubted Jin Wikyung would ever have to worry about the family budget again after today.

Once things had settled down to a certain extent, Jin Wikyung approached me.

“How was it?”

I gave him a thumbs-up.

“It was impressive. But is it really all right for you to come over already? There still seem to be people who haven’t even had a chance to speak with you.”

“That is why they will be growing anxious.”

“What?”

“How do you think those who were unable to speak with me today feel?”

“I don’t know. Maybe they feel like they’ve fallen far behind everyone else?”

“Correct.”

Jin Wikyung took a sip of his drink and gave me a wink.

“The more desperate they become, the more they will offer. It is only the first day. I am looking forward to the final day even more.”

“Damn.”

He was going to bleed them dry.

The Sect Leaders of the Five Gates of Shanxi, who were staring this way as if someone had lit a fire under their asses, would surely be the highlight of the final day.

“But, youngest.”

Jin Wikyung lowered his voice.

“Why is the Defeated Flower Fist acting like that?”

Chulwoo had moved to the far end of the honored seats without me noticing. He kept glancing this way with a gloomy expression.

He glared at me with blazing eyes, then let out a deep sigh every time Lee Seowol and I exchanged a few words.

“Uh, well…”

How was I supposed to explain this? Lee Seowol was sitting not far away, so I had to be careful.

*If I’d known this would happen, I would’ve practiced Sound Transmission beforehand.*

Reaching the Peak realm had made Sound Transmission available for me to learn through practice; it hadn’t granted me the skill on the spot.

“He doesn’t look well. Is he hurt somewhere?”

He was probably hurting, all right. In his heart.

“I guess he’s just in a bad mood.”

I mumbled out a vague answer, and then the music filling the Grand Training Ground abruptly stopped. The people began to murmur.

*Who’s that now?*

A young man walked confidently through the flustered dancers. After looking around, he gave a respectful fist-and-palm salute toward the honored seats.

More precisely, toward Jin Wikyung.

“My name is Choo Dohwan of the Iron Blood Sect of Henan.”

Jin Wikyung’s eyes widened.

“Could you be Choo Dohwan, the Iron Fist?”

“It is merely an undeserved reputation.”

“I have heard many rumors about you. But what brings a Disciple of the Iron Blood Sect here without prior notice?”

Even I had heard of the Iron Blood Sect of Henan a couple of times. It was a well-known sect.

*Judging by his sect alone, he must be one of the top three among the honored guests.*

Under the concentrated attention, Choo Dohwan revealed why he had stepped forward.

“I have come to request a duel.”

“A duel? Right now?”

“Yes. I apologize, but I must ask this of you.”

Of course he ought to apologize. What kind of place did he think this was?

Surprisingly, however, very few people frowned. They had already had a few drinks, and most seemed to regard this as an exciting surprise event.

“Hmm.”

“If you do not accept, I will sincerely apologize and withdraw.”

At least he understood etiquette. Baek Museong, who had been observing the situation, added a word.

“I have heard the name Choo Dohwan, the Iron Fist. As befits a Disciple of the Iron Blood Sect, he is skilled in fist-and-foot techniques and has an upright character.”

“You could choose Young Hero Baek as your opponent.”

Baek Museong smiled faintly.

“My junior brothers and I would be happy to accept.”

“Are you sure?”

“Of course. On such a fine day, I am simply grateful for the opportunity to help enliven the festivities as a guest.”

His answer carried the ease and courtesy of a powerful man. Jin Wikyung rose from his seat and spoke.

“I accept Young Hero Choo’s request.”

“Thank you.”

But Jin Wikyung didn’t stop there.

“Furthermore, anyone who wishes to participate in the duels may step forward! The final victor will receive one hundred silver nyang and a fine weapon worthy of the prize!”

“Waaaaah!”

Cheers erupted at his generous gesture, rowing while the tide was coming in. After all, there was nothing more entertaining in the world than watching a fight.

The eyes of the young martial artists, still brimming with youthful vigor, lit up at the thought of testing themselves.

“Then, Young Hero Choo!”

Jin Wikyung drew everyone’s attention with his booming voice before asking Choo Dohwan,

“Name your first opponent.”

“The opponent I wish to face is…”

A Disciple of the Iron Blood Sect, famous for his fist-and-foot techniques. His nickname was the Iron Fist, for heaven’s sake.

*It was obvious.*

Just as I expected, Choo Dohwan named a particular person.

“Young Hero Chulwoo, the Defeated Flower Fist!”

“…Me?”

Chulwoo, who had been sitting there blankly, rose to his feet. His eyes, steeped in gloom, turned toward Choo Dohwan.

“That sounds good.”

“Let us determine which of us is stronger!”

I looked at the Level window floating above Choo Dohwan’s head and thought,

*He’s going to get beaten to death.*

> **System**
>
> - **Level 65 Choo Dohwan**

And my prediction soon became reality.

* * *

*Wham! Wham! Wham!*

There were no forms or techniques at all. The difference between the Peak realm and First Rate was the difference between heaven and earth, and Choo Dohwan had nothing that could bridge it.

*Thud!*

“Guh! H-How can it be this easy?”

“Are you really the Iron Fist? Why are you so soft?”

Chulwoo, on the other hand, rampaged like a monster. He was ahead in martial arts, and he had been born with strength, size, and toughness. In only fifty exchanges, he had knocked his opponent senseless.

In fact, it looked as though he had been holding back quite a bit.

“You know how to throw a punch, but it won’t work on me anyway. Give up here.”

Choo Dohwan gritted his teeth.

“No! It isn’t over until it’s over!”

“What a stubborn bastard.”

*Whoosh! Crack! Thump!*

Well, now it really was over.

When Choo Dohwan passed out, martial artists from the Jin Family of Taiyuan, who had been waiting nearby, carried him away on a stretcher.

“Whaaaat?”

“As expected of the Defeated Flower Fist!”

“The Iron Fist Choo Dohwan is a fairly well-known master, but he’s no match for one of Huashan’s Three Plum Blossom Elites.”

According to the simple rules they had established, the winner had to continue accepting challenges. Once there were no challengers left, the winner could name an opponent.

Lee Seowol, who had somehow taken the seat beside me, whispered,

“Do you think someone else will challenge him?”

I snorted quietly.

“The Iron Fist ended up like that. Do you really think anyone will come forward? I’ll bet my wrist that nobody will.”

Just then, a man wearing a heroic headband suddenly stepped forward and shouted,

“I am Hwang Jinsu of Hwang Family Manor! I challenge the Defeated Flower Fist!”

“…”

“…”

*Damn it. I should’ve just kept my mouth shut.*

While I was regretting it, Hwang Jinsu of Hwang Family Manor fell to the ground, spraying teeth everywhere.

It was the obvious result when a Level 25 stepped forward.

“What about now?”

“Didn’t you just see what happened? He got it even worse than the Iron Fist. Bones can be set, but teeth are finished. Completely finished.”

“And your wrist…”

“Fine, I’ll bet it. I bet both of them. It was my left wrist before, and this time it’s my right. Look. Now nobody will come forward. For real.”

A wandering martial artist wearing a bamboo hat stepped forward.

“I am Gal Mo. I may be a nameless wandering martial artist, but would you care to exchange a few moves?”

“Do you even need to ask? Come on up.”

*Did that bastard put honey on his fists or something? The challengers just keep coming.*

After knocking down fifteen-odd people in about the time it took to eat a meal, Chulwoo let out a roar.

“Is there no one who can stand against me?”

Despite having fought so many duels in such a short time, he was still full of energy. The gap in ability was so enormous that the other martial artists now looked thoroughly daunted.

Thinking this was my chance, I spoke up.

“Now nobody’s coming out. Really, nobody. I’ll bet my wrist.”

Lee Seowol answered helpfully,

“You already bet that earlier. Both of them.”

“Then my left ankle.”

“You bet that in the fifth match.”

“Oh, then what about my right ankle?”

“You already bet that in the sixth match.”

“My neck…”

“The eighth match…”

*Damn it. So this was what a corpse with its eyes open looked like.*

As I sat there in a daze, Lee Seowol let out a small laugh.

“It’s all right. I won’t take it.”

“…Were you planning to?”

“If you do me one favor.”

“What favor?”

Just as Lee Seowol was about to open her mouth—

“Shan! Xi! Sleeping! Dragon!”

An enormous shout shook the Grand Training Ground. Having defeated every challenger, Chulwoo crooked a finger at me.

“Jin Taekyung, come out.”

At the same time, a System alert rang out.

*Ding.*

> **System**
>
> - **Level 95 Chulwoo** has chosen you as his duel opponent!
> - **Quest:** **There Is a Man Who Loved You So Much** has been created.
> - Would you like to accept the **Quest**?
> - Refusing will incur a massive penalty!

“…”

I could say this with absolute certainty: that was the most fucked-up quest title I had ever received.
## Chapter artifact 189

# Chapter 189

> **System**
>
> **Quest**
>
> **There Is a Man Who Loved You So Much**
>
> A man's burning feelings for a woman have manifested as jealousy and rage.
>
> He seeks to win her love by knocking you down.
>
> **Grade:** Peak
>
> **Restriction:** Jin Taekyung
>
> **Task:** Win the duel (Incomplete)
>
> **Reward:** EXP and Fame
>
> **Failure:** Acquire the Title **Weak Male**
>
> —Would you like to accept the **Quest**?
>
> —If you refuse the **Quest**, the Title **Weak Male** will be granted.

*Wow. That sucks.*

Of course, the penalty for refusing would suck twice as much.

*No choice.*

As I clicked my tongue and rose from my seat, everyone's attention turned toward me.

“Young Master Jin!”

“Young Master Jin.”

“Young Hero Jin, you don't need to go out there.”

“That's right. Has Senior Brother Chul gone crazy? Why is he suddenly acting like that?”

Wolhwa, Lee Seowol, Baek Museong, and even Eunhyang, whom I had barely exchanged a few words with, all looked at me with concern.

I was the only one who didn't think much of it.

“It's fine. Let's have a good, clean match.”

Wolhwa sighed.

“Young Master Jin, do you know who your opponent is?”

“I do. Chulwoo, the Defeated Flower Fist.”

“I don't think you do. The Defeated Flower Fist is a prodigy recognized even within Huashan. Think carefully about why he's called one of the Three Plum Blossom Elites.”

“He probably got the name because he's good at fighting.”

“No, that's not what I meant… Whew. Fine, I give up. Do whatever you want.”

Wolhwa was out.

Baek Museong and Eunhyang stepped forward next.

“I'm not underestimating Young Hero Jin in any way, but my Second Junior Brother is, how should I put it? He’s…”

“He's a mad bull. When Senior Brother Chul loses his temper, it’s going to be really painful.”

“Eunhyang!”

“What? It's not wrong.”

In short, they were saying that someone like me couldn't go toe-to-toe with Chulwoo.

*That's what you think.*

I thought differently. I still wasn't sure whether it was arrogance or confidence. I simply…

*I don't think I'll lose.*

I had that certainty. The certainty that I could defeat that man shouting at me.

“Come! Out! Right! Now!”

“I'm coming, you bastard.”

Under the eyes of more than a thousand people gathered around the Grand Training Ground, I walked toward Chulwoo.

* * *

“We have to stop the duel.”

At Baek Museong's words, Jin Wikyung shook his head.

“My younger brother has already accepted the Defeated Flower Fist's challenge. The duel will end after that.”

“Great Hero Jin.”

“I don't know what happened between them, but it seems there is some bad blood between the two. Wouldn't it be good for them to clear it up while they have the chance?”

Baek Museong inwardly sighed at Jin Wikyung's carefree words.

*Does he not understand the situation?*

To Baek Museong, Chulwoo looked absolutely furious. He seemed ready to break several of Jin Taekyung's limbs before he stopped.

*This is bad.*

They had to stop it here. Baek Museong had heard more than enough rumors about the Sleeping Dragon of Shanxi on the way here, but none of them compared to his Second Junior Brother.

The names Defeated Flower Fist and Three Plum Blossom Elites had not been earned through his Master's reputation alone.

“He could be seriously injured. Shouldn't we stop this before something happens?”

“Who?”

“…Pardon?”

“The duel hasn't even begun yet. Neither has its outcome.”

Baek Museong realized that his understanding had been wrong all along. Jin Wikyung understood the situation better than anyone.

Their assumptions were simply different.

“Great Hero Jin. Could it be…”

“That is correct.”

Jin Wikyung gave a low laugh. His gaze remained fixed on the back of his younger brother as he walked toward the dueling platform.

“That boy will win. Just as he always has.”

“…”

Baek Museong was left speechless. The Sleeping Dragon of Shanxi was undeniably an incredible prodigy, but he could not match Chulwoo in experience, martial arts, or internal energy.

Baek Museong had watched Chulwoo since he was a child. He could state it with certainty.

*The Lesser Family Head is wrong. The Sleeping Dragon of Shanxi can't stand against my Second Junior Brother.*

Baek Museong shook his head, but the water had already been spilled. Backing out now would surely drag the prestige of both sects through the dirt.

*I'll have to step in at the right moment.*

As he watched the dueling platform with sunken eyes, he missed one fact.

Munch, munch. Smack, smack.

Cheongpung—the man who called Jin Taekyung his Benefactor—was silently watching the situation unfold.

* * *

“Waaaaah!”

“Sleeping Dragon of Shanxi! Sleeping Dragon of Shanxi!”

“Defeated Flower Fist! Defeated Flower Fist!”

The moment I stepped onto the dueling platform, cheers erupted from every direction. The response was on an entirely different level from when the other challengers had appeared.

“Oh, so everyone knows the Sleeping Dragon of Shanxi. For the record, he’s scary strong.”

“Waaaaah!”

I waved enthusiastically at the crowd, and Chulwoo glared at me.

“Wave your hand a little, too. There are no stars without fans. Don't you know that?”

“Wave all you want. For the next three months, you'll be staring at the ceiling of a medical clinic.”

“Let me ask you one thing. Why the fuck are you giving me shit?”

“You're asking because you don't know?”

I shrugged.

“Did you get rejected before you could confess?”

“Who got rejected!”

Chulwoo shouted with a flushed face.

“If you hadn't interfered, I would already have three children and be living happily!”

“…Isn't that a little too fast?”

There were limits to speeding things up. We hadn't even known each other for half a shichen. How was he supposed to get married and have three children already?

*What is he, a Command Center? He'll hit a population of two hundred in no time.*

As Cheongpung had said, even if a goose delivered them by rocket delivery, it would take half a day. And in this case, there were three children, so it was a bundle delivery.

“It's fine to spread your imagination's wings, but leave me out of it. I don't have anything to do with this Young Lady, so this is unfair.”

“Nonsense! I saw the look in her eyes when she looked at you!”

“The look in her eyes? What was it like?”

“That… That…”

Unable to continue, Chulwoo groaned and widened his eyes.

“I swear. You won't leave this place on your own two feet.”

“I'm a nice guy, so I'll let you crawl out on all fours.”

“I'll smash that insolent mouth of yours!”

With a roar, Chulwoo charged.

I swung my spear shaft at the punch flying toward me with a fierce aura.

Whoosh! Boom!

The intense impact sent my body sliding backward. The force was unbelievable for a collision between flesh and steel.

By then, a pair of dull-black gauntlets covered his hands.

“Those Items look pretty good. Mind if I take a look for a moment?”

“You bastard!”

Whoosh!

He was a mad bull in every sense of the word.

The only difference was that he had fists instead of horns, and those fists didn't simply attack.

“Hup!”

I held my breath and swung my spear. The gauntlets and spearhead met in their arcs, spitting sparks.

Clang-clang-clang!

I pressured him with the spear's advantage in reach, while Chulwoo pressured me with his natural reflexes and strength.

Whoosh!

A steel-like leg lashed toward my waist like a whip.

His movements were fast and flexible despite his size. I retreated while thrusting my spear toward his neck.

Bang! Krrrck!

His toes cut through empty air, while the spearhead was stopped by his gauntlet. Chulwoo seized the spearhead and grinned.

“Got you.”

Krrrck!

At the same time, an immense force pulled the spear toward him. He had probably been aiming for this from the beginning.

A spearman without his spear was no different from a scarecrow with its eyes open.

Of course…

*I expected this much.*

I relaxed my grip and charged toward Chulwoo. The look of triumph on his face turned to shock.

His own strength had sent both hands flying overhead, the spear still clutched in them as though he were cheering.

“You…!”

“Give me my spear.”

Crack!

“Guh!”

Something broke. Chulwoo staggered after taking a knee to the face. Next came his solar plexus.

Thud!

“Ghn!”

After being struck in a vital spot, he dropped the spear and stumbled backward. I calmly retrieved it in the meantime.

“You bastard!”

The moment I saw Chulwoo finally straighten his back after escaping the pain, I let out a quiet laugh.

“Y-You’re laughing?”

“You have a nosebleed.”

“You’re really dead—what? A nosebleed?”

He hurriedly wiped the bridge of his nose with the back of his hand, and his face twisted in outrage.

“How dare you injure my face?”

“It's fine. You're so ugly that no one can tell.”

“That makes it worse! Won't I become even uglier now?”

“…”

What the hell? Surprisingly, he had an accurate grasp of himself.

“Gaaaaah!”

Chulwoo let out a furious roar, and his eyes flashed.

“I was going to finish this at an appropriate level out of consideration for my Senior Brother, but… Never mind.”

“Do it properly. That's why I came out here.”

“Fine. I'll face you seriously.”

As if to prove his words, a faint light shimmered around Chulwoo's gauntlets.

“Fist qi?”

It was still incomplete, but it was unmistakably fist qi. A vicious smile spread across his lips.

“It's too late to regret it now.”

Whoosh! Slice!

Sparks flew as the spearhead was cleanly severed. Chulwoo's fist, drawing up all the internal energy in his body, blurred.

Swish! Swish-swish-swish!

A sharp whirlwind surged around us. Every time I swung my spear at the wind raised by his fists, the spear grew shorter by a handspan.

Though incomplete, the cutting power of his manifested qi was tremendous.

Slice! Slice! Slice!

In less than the blink of an eye, the steel spear in my hands had been reduced to a sharp metal rod no longer than my forearm.

“Damn. I thought I was finally getting used to it.”

At this point, it wasn't a spear anymore. It was a short flute. A short flute.

Grumbling, I swung the steel flute through the air.

“Oh, it's suddenly so light that I can't adjust.”

Perhaps my appearance looked funny to him, because Chulwoo burst into laughter.

“Ha-ha-ha! Pathetic bastard. What are you planning to do with that?”

“Mind your own business.”

“Are you already admitting defeat?”

“What do you mean, admitting defeat? Who's lost?”

“What kind of confidence does a man who has lost even his weapon have? If you think your Senior Brother or your elder brother will save you, you're mistaken.”

I let out a quiet laugh.

“You'd better not regret this. If you suggested a draw right now, I might even consider it.”

“What? A draw?”

“Yeah. On the condition that you stop hitting on this Young Lady.”

“You're crazy.”

“Then negotiations are over.”

I walked steadily toward him, casually brandishing the steel flute that could no longer be called a spear.

“Come here. Let's fight.”

A spearman was fearlessly approaching a master of fist-and-foot techniques. And he was doing it without even a proper weapon in his hands.

The crowd surrounding the Grand Training Ground began to murmur at the sight.

Chulwoo frowned as if he were looking at some strange creature.

“What the hell are you?”

“Jin Taekyung, the Sleeping Dragon of Shanxi. You know that.”

“Are you acting cocky because you trust in some hidden move?”

“Who knows?”

“You aren't planning to use some underhanded trick, are you?”

An underhanded trick. In a way, it might have been similar.

It was a technique permitted only to me—one no one else could see.

*Status Window Open.*

The distance between Chulwoo and me was only thirty paces. The System responded.

Ding.

> **System**
>
> **Status Window**
>
> **Level 71 Jin Taekyung**
>
> **Class:** Peak Master
>
> **Fame:** 2,500 (+250)
>
> **Titles:** 5 (Title effects active)
>
> - **Returnee** (All stats +10)
>
> - **Sleeping Dragon of Shanxi** (All stats +15, Fame +200)
>
> - **Scion of a Prestigious Family** (All stats +5, Fame +50)
>
> - **Gambler** (Combat-related stats +10% in one-on-one combat)
>
> - **Intermediate Trainee** (Training speed +20%)
>
> **Strength:** 255 (+55)  
> **Stamina:** 207 (+50)
>
> **Agility:** 250 (+55)  
> **Intelligence:** 40 (+30)
>
> **Charm:** 40 (+30)  
> **Internal Energy:** 45 years
>
> **Toughness:** 200 (+50)
>
> **Remaining Points:** 70
>
> - Certain stats have been temporarily increased by the **Gambler** effect.
>
> - Assign the remaining points.

The Gambler effect. And the seventy points I had gained by breaking through the wall of the Peak realm.

I stepped forward without hesitation. Twenty paces away, I could see the bewildered look on his face.

“Crazy bastard.”

“I've heard that a lot.”

Fifteen paces.

I muttered inwardly.

*Assign twenty points to Strength.*

Whoosh.

Along with an invisible wind, new strength seeped into me. My Strength, temporarily exceeding 300, churned like an active volcano.

*Fifty points to Agility.*

A second wind blew. At the same time, the step I took felt unfamiliar, as though it belonged to someone else.

*Was I always this light?*

It felt like I had entered an entirely new world.

I took a deep breath. It was Chulwoo, not me, who first closed the remaining ten paces.

“Damn it, I told you to surrender! Now that it's come to this, don't blame me!”

Whoosh!

I knew this martial art. It was called Crouching Tiger Fist because it was said to subdue tigers.

Just as the fierce first strike of the Crouching Tiger Fist was about to slam into my chest—

Whoosh.

A third wind blew.

It began at my toes and ended at my fingertips.

“Hey, Level 95.”

Swish.

I stabbed the back of Chulwoo's neck with the pointed steel flute.

By then, I was already sitting on his shoulder.

“Looks like I've gotten a lot stronger.”

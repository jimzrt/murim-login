# Checkpoint Review — 375–379

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

# Chapters 375–379

## Plot

Tang Sadok awakens and confesses that he revealed the Myriad-Poison Ring’s location to the Western Heaven Demon Lord to spare the Tang Clan. Jin Taekyung forgives him, completing **Atonement and Forgiveness**, earning the Tang Clan’s Benefactor title, and receiving EXP, Fame, and a level-up. Tang Sadok transfers the Myriad-Poison Ring to Taekyung and temporarily entrusts Mimi to Cheongpung.

Mungyeong and his Disciple Dong Feng revisit their past and confirm Mungyeong’s identities as the Divine Physician and former Slaughter Saint. Dong Feng urges him to help prevent the coming war, but Mungyeong refuses to return to Murim and limits himself to treating the wounded. Taekyung’s party leaves Chengdu aboard Water Dragon Stronghold ships, while an unidentified boy asks for passage.

The Sichuan City Lord conceals the government’s role in the Three-Gate Bloodbath after being manipulated by his concubine Aehyang, whose eyes reveal an ominous red light. At sea, Taekyung binds a fragment of the Western Heaven Demon Lord’s Black Dragon Armor, transforms it with the Fire Gate Divine Technique, and names it Fire Dragon Armor. The armor can repair itself by consuming his internal energy.

After logging out, Taekyung returns to the modern world aboard a private jet bound for Chengdu. Chengdu International Airport is under attack by a massive monster army. He kills the lead Wyvern, Black Star, and two others, but the defenders are soon overwhelmed by Wyverns, Griffons, Gargoyles, and undead raised through black magic. Shao Shen rallies the Chinese forces, only to face the reanimated Dullahan Yao Wei and mounting casualties. A gigantic burning aircraft sweeps across the battlefield, leaving its identity and impact unresolved.

## Continuity

- Jin Taekyung is Level 120, at the Supreme Peak realm, and publicly known as the Blazing Flame Divine Dragon. He has manifested Force.
- Taekyung’s bound Items include White Flame, the Myriad-Poison Ring, and the Fire Dragon Armor. The Fire Dragon Armor repairs damage by consuming his internal energy.
- Tang Sadok survived but remains gravely wounded. The Tang Clan is rebuilding, and Mimi is temporarily under Cheongpung’s care.
- Mungyeong is the Divine Physician and former Slaughter Saint. He has sworn never to kill again and intends to remain a physician; Dong Feng is his Disciple.
- Taekyung’s party departed Chengdu aboard three Water Dragon Stronghold ships. The unidentified boy seeking passage remains unexplained.
- Aehyang is manipulating the Sichuan City Lord on behalf of an unidentified superior.
- Chengdu International Airport is being defended by the Chinese People’s Liberation Army and the Public Security Armed Forces Department Hunters, but losses are approaching half their strength.
- Shao Shen is a young Hunter fighting with a spear imbued with aura. Yao Wei, formerly an A-rank Hunter, has been raised as a Dullahan.
- The gigantic burning aircraft has entered the airport battlefield; its identity and the consequences of its attack are unresolved.
- The Lord of Heaven escaped after possessing the Western Heaven Demon Lord’s body. Their nature and the Demon Lord’s fate remain unknown.
- The Second Fiend, Dark Heaven’s response, the Moving Formation’s origin and purpose, and the coming war remain unresolved.

## Translation Decisions

- Use **Atonement and Forgiveness**, **Tang Clan’s Benefactor**, **Myriad-Poison Ring**, **Fire Dragon Armor**, and **Black Dragon Armor**.
- Render **신의** as **Divine Physician**, **살성** as **Slaughter Saint**, and **동봉** as **Dong Feng**.
- Use **Dullahan**, **Griffon**, **Gargoyle**, **Wyvern**, **Poison Breath**, and **Public Security Armed Forces Department**.
- Use **Force** for 강기 and **aura** for 오러; render 강기(劍罡) as **Aura Blade** when explicitly distinguished in the modern world.
- Preserve **Mimi**, **Mimi-chan**, **Cheongpung**, **Shao Shen**, **Yao Wei**, and **Aehyang**.

## Durable state

{
  "active_continuity": [
    "Chengdu International Airport is under attack by an unexpectedly large monster army that includes ground monsters and flying monsters.",
    "The Chinese People’s Liberation Army and Public Security Armed Forces Department Hunters are defending the airport, but the defenders have suffered losses approaching half their strength while the monster army continues to grow.",
    "Shao Shen is a young Hunter of the Public Security Armed Forces Department who rallied the defenders and fights with a spear imbued with aura.",
    "Black necromantic magic has raised the battlefield dead as chained undead, including the former A-rank Hunter Yao Wei as a Dullahan.",
    "A gigantic burning aircraft has entered the airport battlefield and swept across it; its identity and the consequences remain unresolved.",
    "Jin Taekyung is Level 120 at the Supreme Peak realm, has manifested Force, and is publicly known as the Blazing Flame Divine Dragon.",
    "Jin Taekyung remains aboard a private jet approaching Chengdu International Airport as the battle unfolds.",
    "The Myriad-Poison Ring is bound to Jin Taekyung alongside White Flame and the Fire Dragon Armor.",
    "Mungyeong is the Divine Physician and former Slaughter Saint, has sworn never to kill again, and intends to live as a physician; Dong Feng is his Disciple.",
    "Cheongpung remains a Supreme Peak master with Mimi and is Mimi’s temporary guardian.",
    "The Lord of Heaven temporarily possessed the Western Heaven Demon Lord’s body and escaped after One Annihilation; their nature and ultimate fate remain unresolved.",
    "Aehyang is manipulating the Sichuan City Lord under the direction of an unidentified person."
  ],
  "continuity_sources": [
    379
  ],
  "open_questions": [
    "What happened to the Second Fiend assigned to the Qingcheng attack?",
    "What is the true nature and purpose of the Lord of Heaven, and what became of the Western Heaven Demon Lord?",
    "What was the origin and purpose of the Moving Formation, and why did it lose its power?",
    "Who is the unidentified person directing Aehyang, and what are they planning?",
    "Will Mungyeong remain outside the coming war, or will the crisis force him to intervene?"
  ],
  "safe_through": 379,
  "temporary_decisions": [
    "Render 열화신룡 as Blazing Flame Divine Dragon, distinct from Huashan Divine Dragon.",
    "Use Mimi for 미미 and Mimi-chan for 미미쨩; render 삼괴 as Third Fiend in singular references and Three Fiends in collective references.",
    "Render 진인 as Perfected One, 도우 as Fellow Daoist, 신니 as Venerable Nun, 환영진 as illusion formation, and 이동진 as Moving Formation.",
    "Render 독룡각 as Poison Dragon Pavilion, 가주 대행 as Acting Family Head, and 화룡갑 as Fire Dragon Armor.",
    "Render 듀라한 as Dullahan, 공안 무력부 as Public Security Armed Forces Department, 중화 as Zhonghua, and 포이즌 브레스 as Poison Breath."
  ],
  "version": 1
}

## Reading copies

## Chapter artifact 375

# Chapter 375

Even paying a visit to the sick has an order to it.

When word spread that Tang Sadok—the Family Head and senior patriarch of the clan—had awakened, the members of the Tang Clan dropped everything and came running.

However, not all of the more than one hundred people could see Tang Sadok.

“Benefactor, when can we go see Grandpa Tang?”

“Hard to say. The people who went in ahead of us have been there for quite a while, so they should be coming out soon.”

“Oh, I see.”

Cheongpung nodded at my answer.

Wait. Cheongpung?

“What are you doing here? When did you get here?”

“Just now.”

He had slipped into the conversation so naturally that I hadn’t even realized he was there. But why had he come here?

As if he had read my question, Cheongpung pointed to his chest and answered,

“Mimi said she wanted to see him.”

“...?”

What had I just heard?

*Now he could even communicate with a snake.*

Was this guy actually from Slytherin instead of Huashan?

At my suspicious stare, Cheongpung tilted his head.

“Why are you suddenly looking at my forehead? Is there something on it?”

“I was just checking whether you had a lightning-shaped scar on your forehead.”

“What?”

“There is such a thing.”

The instant I finished speaking—

Clunk.

The tightly closed door of the medical room opened, and about a dozen people emerged.

They were among the few remaining direct members of the Sichuan Tang Clan. Tang Horyong, whom I had met before, was among them.

“Whew...”

His eyes bloodshot, he looked up at the sky before walking toward us.

“The Family Head wishes to see you.”

“We’ve been waiting.”

Jin Wikyung nodded and led the way. Cheongpung and I followed him into the medical room.

After walking for some time with the smell of herbal decoctions vibrating through the air around us, we entered the treatment room guided by a physician whose nose and mouth were covered by a white cloth.

At last, we came face-to-face with several familiar people.

“Cough... You came.”

Tang Sadok’s condition was obviously serious. His limbs were broken, and the qi in his body was unstable from his internal injuries.

The Divine Physician, who exchanged a brief glance with us, stopped Tang Sadok as he tried to sit up.

“Family Head, didn’t I tell you not to move?”

“This old man is a sinner. I committed a crime deserving of death, so it is only right that I ask for punishment.”

Tang Sadok shook his pale face and continued, staring directly at me.

“I will not make any pitiful excuses. The reason the Western Heaven Demon Lord headed for the underground prison was because I told him about it.”

I folded my arms at an angle.

“Ah. No wonder.”

“...?”

“Why?”

Tang Sadok asked with a flustered expression.

“Ah, you knew?”

“Of course I didn’t know at first. Things were too hectic back then. But when I thought about it later, I started wondering how the hell that bastard had learned the location of the Myriad-Poison Ring.”

Only a tiny number of people knew where the Myriad-Poison Ring was.

Cheongpung might have looked as light as a flower petal on the outside, but he was as solid as a tree root. Tang Sadok was the only person who could have let it slip.

“Why did you do it?”

“He said that if I told him where the Myriad-Poison Ring was, he would preserve our family’s bloodline.”

“And you believed him?”

“This old man was foolish. My judgment was clouded for a moment, and I committed an act I should never have committed.”

“At least you realize that much.”

Tang Sadok’s eyes trembled as he looked at me.

“The reason this old man was able to keep his life must have been Heaven’s will. I was spared so that I could apologize to you and receive my punishment.”

“Then what punishment do you want, Family Head?”

The cold voice belonged to Jin Wikyung, who had been silently listening to our conversation.

“Are you the Lesser Family Head of the Jin Family of Taiyuan?”

“Yes. I am also the elder brother who raised my two younger brothers as if they were my own sons.”

Unmistakable anger clung thickly to Jin Wikyung’s deeply settled eyes.

“It was something no one who walks the righteous path should have done.”

“I know. No—I know, Young Hero Jin. That is why I am asking for punishment.”

“What will you do if I tell you to kill yourself?”

“...!”

Everyone, myself included, stared at Jin Wikyung in shock.

Everyone except Tang Sadok.

He opened his mouth with an utterly calm expression.

“I betrayed the principles of the Way, but thanks to you all risking your lives and fighting for us, my family will be able to continue its bloodline. If I can use this insignificant old man’s life to atone, I will gladly do so.”

After a brief silence, Jin Wikyung let out a sigh.

“Whew...”

He looked at Tang Sadok with complicated emotions before turning toward me.

“What will you do?”

“...Do about what? Kill him?”

“Anything.”

Having the hilt of a sword suddenly placed in my hand made my heart clench.

Even more so when I realized that the life of the Family Head of the Sichuan Tang Clan was hanging from that hilt.

*Look how icy the mood suddenly got.*

Of course, this was not something I could simply laugh off. I wasn’t some perfectly fair-minded, broad-hearted Great Hero of Benevolence and Righteousness. When I understood the full truth of what had happened, anger had quietly surged up inside me.

At the time, everyone’s lives had been on the line—not just mine.

But...

“Enough. I don’t want to take it that far.”

That was right. On the other hand, I understood Tang Sadok’s position.

If I had to place a blood relative whom I was duty-bound to protect as the Family Head on one side of a scale, and an outsider whose face I had seen only a few times on the other, I felt like I might have made the same choice.

*Besides, I already owed him one.*

Tang Sadok’s help had played a major role in allowing Jeok Cheongang to awaken.

Even if there had been a certain deal involved, Tang Sadok had still been the one who lent us a sacred treasure without telling even his own blood relatives.

“So let’s call it square. No, that’s going too far. Let’s just say the Sichuan Tang Clan owes us a huge debt because of what happened this time.”

When I finished speaking, Cheongpung and the Divine Physician spoke up.

“It was definitely Grandpa Tang’s fault that Benefactor was put in danger... but I’ll follow Benefactor’s wishes, too.”

“I have already forgotten about it. If I have one wish as a physician, it is for the Family Head to recover as soon as possible. There are still clan members who survived, aren’t there?”

The last person to speak was Jin Wikyung. Unlike before, there was no longer any anger in his voice.

No—perhaps he had known my answer from the beginning.

“So that is what they say. What do you think, Family Head?”

“...!”

Tang Sadok’s eyes trembled violently as he looked at us.

After a brief silence, a hoarse voice slipped between his lips.

“This old man... The Sichuan Tang Clan has received an enormous kindness from you.”

It was at that moment, just as Tang Sadok sincerely bowed his head, that—

Ding. Ding. Ding.

> **System**
>
> Confessing one’s sins is difficult, but there is something that requires even greater courage than that.
>
> Forgiveness.
>
> **Hidden Quest, “Atonement and Forgiveness,” successfully completed!**
>
> **Level 115 Tang Sadok** expresses his deep gratitude for your goodwill. He and the **Sichuan Tang Clan** will never forget the goodwill and assistance you showed them today, and the people of the **Sichuan Tang Clan** will remember you as their Benefactor!
>
> You acquired the **Title: Tang Clan’s Benefactor**!
>
> You received a massive amount of **EXP** and **Fame** as a reward for completing the Hidden Quest!
>
> **Level Up!**

What the hell? A Hidden Quest all of a sudden?

While I was still dazed by the unexpected System notification, something cold brushed between my legs and slipped past.

Sssrikk, sssriririk.

“Mimi, you little rascal.”

Seeing Mimi and Tang Sadok reunited after so long reminded me of something I had momentarily forgotten.

“Oh, right. Speaking of the Myriad-Poison Ring... Luckily, I’ve kept it safe all this time—”

“Is that so?”

Before I could finish, Tang Sadok cut in.

“Then continue keeping it.”

“Yes, then I’ll continue keeping it... Wait, what?”

“I will entrust our family’s sacred treasure to you. It is a token of our gratitude toward our Benefactor, so please do not refuse.”

Ding.

> **System**
>
> At the owner’s request, **Myriad-Poison Ring** has been transferred to you!
>
> A new Item is now bound to you!
>
> **Bound Items currently in your possession:** White Flame, Myriad-Poison Ring, ???
>
> You have a bound Item whose name has not yet been determined. Please give it a new name.

What was with today?

I was starting to feel uneasy, wondering what kind of shitty things were about to happen for me to be showered with rewards like this.

Seeing me gape soundlessly like a goldfish, Tang Sadok smiled faintly.

“If there is anything you want, tell me. As far as our family’s abilities allow, I will grant you anything.”

The Divine Physician smiled along with him and answered,

“If there is something I want, I simply hope that the patients recover as soon as possible.”

“Oh?”

That was an answer worthy of the Divine Physician. Or should I call him Dong Feng now?

But one thing was certain: he was another true Divine Physician.

“What do you want?”

Cheongpung jumped at the sudden question.

“M-Me?”

Tang Sadok nodded, and Cheongpung twisted his hands and feet as he answered.

“I... Well. Hmm. I don’t have anything.”

“Are you sure?”

“Yes. I don’t think I have anything.”

“...”

“...”

*Hey, you little bastard. Take your eyes off Mimi-chan and talk.*

I wanted to bring him a mirror and show him what he looked like. His eyes were filled with aching longing and desire for Mimi-chan.

*At this rate, he’s going to bore a hole through her scales.*

Just then, Tang Sadok spoke.

“This fellow is my old friend. For the past several decades, Mimi was the only one with whom I could share all the joy, anger, sorrow, and pleasure I could never show anyone else.”

Cheongpung looked at Tang Sadok with pity.

“Grandpa Tang doesn’t have any other friends.”

“I did not make any. Being the Family Head of the Tang Clan was that kind of position.”

“So you don’t have any friends.”

“It is not that I had none. I could have made some, but...”

“You didn’t have a single friend. How sad.”

“...”

The Divine Physician hurriedly grabbed Tang Sadok by the shoulder.

“Family Head, please calm down. Your breathing is much too rapid!”

“Huff... Hoo, huff...”

“Take deep, slow breaths. Now, follow me. One, two...”

“Whoooosh...”

A short while later, Tang Sadok had barely escaped a bout of high blood pressure. He looked at Cheongpung and spoke.

“But I could give you Mimi...”

Cheongpung covered his mouth with both hands.

“No, Grandpa Tang. I can’t take your only friend away from you.”

“...I have not yet said that I would entrust her to you.”

“Oh. Oh, no.”

Tang Sadok let out a deep sigh. For a moment, he had undoubtedly wondered whether it was really safe to entrust Mimi-chan to someone like that.

“Yes, just as you guessed. We do not know what path our family will take from here, so I wish to entrust Mimi to you. Temporarily, of course.”

“Yaaay!”

“Did you hear what I said at the end? Temporarily.”

“Yaaay!”

*I’ll bet Hyuk Mujin’s right wrist that he didn’t hear that.*

Cheongpung, now Mimi’s temporary guardian, did not know what to do with his happiness.

“Don’t worry. I’ll take good care of her!”

“From what I saw last time, Mimi does seem to follow you well. However, she is naturally quite fussy and very wary of strangers, so...”

“Mimi. Whirlwind, then spin around and around and say hello!”

Sssriririk!

“Oh, shit.”

And Mimi busts out a new move right here.

Jin Wikyung, who had been half out of his mind at the sight, muttered in a dazed voice,

“It seems you have nothing to worry about, Family Head.”

An earthquake struck Tang Sadok’s eyes.

Tang Sadok asked Jin Wikyung to stay behind for a private conversation, while Cheongpung and I left the room first.

No—one more person had just been added.

“Young Hero Jin, could you spare this old man a moment?”

“Me?”

The Divine Physician nodded with a gentle smile.

“There is something I must ask of you before you leave.”
## Chapter artifact 376

# Chapter 376

A sea of people.

That was the only way to describe the scene.

After hearing that the Sleeping Dragon of Shanxi—no, the Blazing Flame Divine Dragon Jin Taekyung—and the Huashan Divine Dragon Cheongpung were leaving, people had gathered like clouds.

Not only martial artists, but also fearless ordinary citizens had come to see them off. The crowd stretched endlessly, one person after another, until it was impossible to count them.

“Safe travels, Blazing Flame Divine Dragon!”

“Sichuan Murim will never forget you!”

“It has horns! The Huashan Divine Dragon has a horned snake!”

“Whoa, the snake just did a flip in midair!”

“Fire King! The Fire King is grabbing the snake and trying to roast it!”

The murmuring noise gradually faded into the distance as the procession moved away.

On a deserted hill, a boy sat on a tree stump watching the entire scene. Then he suddenly spoke.

“We’ve come a long way.”

“Indeed. I’m getting tired.”

At the sight of his old Disciple dropping heavily onto the grass with ragged breaths, Mungyeong muttered,

“…We really have come a long way.”

He wasn’t talking about distance. Mungyeong was speaking of the years they had traversed.

“Do you remember when we first met?”

“How could I forget?”

The old Disciple wiped the sweat from his brow, as though the scorching sunlight from that day were still beating down on him.

“The first year of Hongwu.[^1] That particularly hot summer.”

It was the year the civil war over the imperial throne ended and a new Son of Heaven ascended.

The young, ambitious emperor changed the era name and sought to introduce reforms, but the people, exhausted by the long civil war, were far too weary to heed the Son of Heaven’s will and take part in them.

“Rebellions broke out across the land, and bandits ran rampant.”

“There was a drought, and swarms of locusts swept across the plains. The corpses of government soldiers and rebels filled every corner, and epidemics raged.”

“Yes. It was truly a time of turmoil.”

Death begot more death, and before long, it swallowed the continent whole.

A young carpenter surnamed Dong could not escape the dark shadow that had fallen over the land.

“Even now, I sometimes think about those days.”

The decades had changed more than just the mountains and rivers. The young carpenter who had lost his beloved wife and two children to the epidemic had eventually become an old physician.

“I sometimes wonder whether I could have saved my family if I had been a little faster, if I had found you sooner.”

“Do you regret it?”

“Yes.”

Sitting on a hill close to the heavens and gazing at the drifting scraps of cloud, the old physician’s eyes had returned to those of the young carpenter.

“For the rest of my life, as long as I draw breath.”

It had been a difference of only one day.

By the time the carpenter dragged his plague-stricken body to bring back the unnamed old physician who had been staying in a slash-and-burn settlement, everything was already too late.

He had cried for an entire day, dug a pit to bury his family, and then made one request of the physician he had brought.

“Please bury me with them. That was what I asked.”

Mungyeong replied in his blunt voice.

“That was why I slapped you across the face.”

“It hurt. So much that I wanted to die.”

It had hurt—not because of any pain that could decide life or death, but because he could no longer see his beloved wife and children.

“You were the one who helped me stand again.”

Mungyeong shook his head.

“I only held out my hand. You were the one who grasped it and got back up.”

“I had to live. I had something I needed to do.”

Under normal circumstances, the carpenter should have died from the epidemic as well.

But the physician cured him with medical arts unlike anything he had ever seen, and for the first time, the carpenter realized that even a mere human being could alter the cycle of birth, aging, sickness, and death ordained by Heaven.

“I can still see it clearly. You kneeling before me and begging me to accept you as my Disciple.”

“That is different from what this Disciple remembers. I remember you beckoning for me to follow you.”

The young carpenter who had lost his family found a new goal, while the old physician who roamed the land tending to poor and helpless patients gained a new Disciple.

It was only after many years had passed that the carpenter, now a physician—Dong Feng—learned his Master’s true identity.

“The Slaughter Saint… It is a truly terrifying sobriquet. That was when you first seemed like a stranger to me, Master.”

Mungyeong gazed into the distance with an impassive expression.

What he was about to ask was something he had never once asked his Disciple.

“Why did you not leave?”

“Did you think I would leave you, Master?”

“I have harmed countless lives. I was nothing more than an ugly killing fiend hiding his past. I would have understood if you had left.”

“Perhaps I really would have. But I knew all too well what kind of person you were, Master.”

The next words came in a low voice.

“You are the Divine Physician. My Master is known as the Divine Physician. You are not someone who would kill without reason.”

“...!”

Mungyeong’s eyes trembled.

It was something he had never told anyone, and something no one had ever wanted to acknowledge.

He had lived as an assassin and personally taken countless lives, whether they belonged to the orthodox faction, the unorthodox faction, or the Demonic Cult. Every one of them had been someone with a reason to die.

A Great Hero of the orthodox faction, renowned for his fairness and integrity, had a habit of raping and murdering women. A master of an unorthodox faction had wiped out an entire village for fun.

If the Demonic Cult’s army invading the Central Plains had not killed and destroyed indiscriminately, if the greatest assassin under Heaven had not stepped forward when he could no longer stand by and killed the notorious fiends, he could never have been called the Slaughter Saint.

“If I had not fought the Demonic Cult, the entire world would have pointed fingers at me. Just as it always had.”

The sobriquet Slaughter Saint had been both the absolution bestowed upon him by the orthodox faction that ruled Murim and praise for a powerful man.

Though Mungyeong had always been Mungyeong, people neither knew nor tried to learn the truth hidden behind him.

“Why did you never tell anyone?”

“It is all in the past. I wanted to leave Murim, and I became a physician as I had intended. I will continue to do so.”

Mungyeong slowly rose to his feet. By then, the long procession that had left the Sichuan Tang Clan had already disappeared into the distance.

“Let us go down. There are patients waiting for us.”

The instant he started walking, his Disciple spoke.

“A great war will break out soon.”

Mungyeong’s footsteps stopped abruptly. Behind him, the old Disciple’s voice continued.

“The same thing that happened back then will happen again. Countless people will die and be wounded. There will be countless people who have lost their parents and children, and the screams and deaths will never cease.”

“…We will be very busy. I should make preparations.”

“You know what I am trying to say, Master.”

“I do not want to know.”

“Master.”

“I am a physician. Though I broke the promise I made to myself and was forced to kill, I will not make the same mistake again.”

Mungyeong continued slowly.

“Fighting is their responsibility, and treating the sick is ours. My heart left Murim long ago.”

“Then why did you never give up martial arts?”

“...!”

Mungyeong was left speechless.

It was a question he had carried inside himself for a long time. If he had wanted to leave Murim because he hated killing, then it would have made sense to abandon martial arts as the means of killing as well.

Yet his martial arts had instead advanced another step. It was proof that he had been unable to let go of his attachment to them.

*Why is that?*

The voice of his old Disciple broke through his brief thoughts.

“You can treat hundreds, even thousands of patients, Master. At the same time, you are someone capable of saving tens of thousands of lives.”

“…”

“Please prevent the war as the Divine Physician, not the Slaughter Saint. This Disciple will care for the patients here.”

Mungyeong suddenly raised his head and looked at the sky.

It was clear and blue. Seven days earlier, when the Sichuan Tang Clan had been stained with blood, the sky had been filled with dark clouds.

“The sky is clear.”

With his blunt voice, Mungyeong’s halted footsteps began moving forward again.

“I should go tend to the patients. Come down slowly.”

From behind him, Dong Feng’s voice scattered into the air.

“The Hour of the Dog.[^2] They said the ship would depart from Chengdu’s western harbor.”

“Pointless. The place I should be is not Murim.”

Yet a faint smile formed at the corner of the old Disciple’s mouth as he watched his Master’s back slowly recede.

“Please… stay well.”

Whoooosh.

A wind that had come from somewhere swept between the two of them.

* * *

“What are you looking at so intently?”

At Hyuk Mujin’s question, I turned away from the crowd surrounding the harbor.

“It’s nothing. I was just checking something.”

“Checking what?”

“You little pest, why are you prying into every little thing? If I say it’s nothing, then take it as nothing.”

Hyuk Mujin gave me a meaningful smile.

“I actually know why you are doing that, Captain.”

“…?”

I froze for a moment. How the hell did he know? Even Cheongpung hadn’t heard the conversation between the Divine Physician and me.

*Was this guy always this perceptive?*

Just as I was wondering, he whispered,

“Weren’t you looking at the Young Lady standing fourth from the right in the front row?”

“…”

“She is definitely pretty. She looks like the daughter of a fairly wealthy family, too. If you permit it, Captain, I could go over there as your right-hand man and arrange for the two of you to meet privately…”

“Mujin.”

“Yes? Ah, do you prefer natural meetings? If so…”

“Do you want to sink to the bottom of the Yangtze?”

“...!”

“Stop spouting bullshit and keep lying there. And don’t go vomiting later because you get seasick.”

“…Yes, sir.”

As Hyuk Mujin quietly crumpled into silence, Gung Gibang snickered.

“You idiot. It wasn’t the fourth from the right. It was the third woman from the left. Anyone can see she is much prettier. Your eyes are screwed up.”

“Want me to screw up your eyes for you?”

“…Sorry.”

“Let’s try to live like decent human beings. Decent human beings.”

With a sigh, I shook my head and gave the cloud-like crowd one final sweep.

Both of them were definitely pretty, but the third woman from the left was more my type…

No. That wasn’t it.

*Damn it. Those bastards kept going on about it, so now I keep looking at her.*

As I was thinking that, a huge man with a copper-colored complexion approached me and spoke.

“Hey, Junior. No, not Junior. Young Hero Jin. No, Great Hero.”

*What is this, buffering?*

The man cycling through forms of address at lightning speed was Ship-Fire Boy Mu Song. I offered him a solution.

“Just call me Junior.”

“Ahem. Would that really be all right?”

“Why wouldn’t it be? You did just fine before.”

“Still, you have accomplished something so great.”

That was true. I had gone from being a regional young prodigy known as the Sleeping Dragon of Shanxi to a nationally famous figure.

“And Great Hero Jeok seems not to like me very much, either…”

“It’s fine. He was never very fond of water in the first place.”

Where Mu Song was glancing stood Jeok Cheongang, his face thoroughly incensed.

Right beside him, Jin Wikyung was examining a bamboo slip whose purpose I couldn’t identify, while Cheongpung was teaching Mimi a new technique.

“Mimi, ride the waves!”

Sssrik, shaaaash!

*Was that a water snake?*

Mu Song had briefly been distracted by the rare sight—one that was difficult to see anywhere else—before opening his mouth with an awkward expression.

“Anyway, we have finished preparing for departure. When should we leave?”

“What time is it now?”

“The Hour of the Dog you mentioned has passed. It would be best to leave before it gets any darker.”

“…Hmm.”

“Are we waiting for anyone else?”

I thought about Mu Song’s question for a moment before shaking my head.

“No. No one else.”

“Then we can depart.”

“Let’s do that.”

“Understood.”

When Mu Song raised his hand high, the river pirates who had already finished preparing moved in perfect unison.

It was at that exact moment, as the people gathered to see us off waved in our direction, that—

“Wait! Wait just a moment!”

“Stop! Stop!”

The bow of the fast ship pulling away from the harbor shook.

Far off in the distance, I spotted a boy forcing his way through the crowd. I let out a short laugh.

“Let’s take one more person aboard before we go.”

[^1]: Hongwu was the reign name of Zhu Yuanzhang, the founding emperor of China’s Ming dynasty.

[^2]: The traditional Hour of the Dog lasted roughly from 7 to 9 p.m.
## Chapter artifact 377

# Chapter 377

“Have they left?”

The Captain of the Guards answered the tense question from the plump, middle-aged City Lord of Sichuan Province.

“Yes. The fast ship of the Yangtze River Channel League carrying them departed half an hour ago.”

“Whew.”

The City Lord let out such a deep sigh of relief that his belly jiggled, then waved a hand.

“All right, you may withdraw. If you hear any news related to the martial artists, report it immediately.”

“Understood. But what about the troops stationed near Chengdu…?”

The City Lord frowned.

“Listen, Captain of the Guards.”

“Yes?”

“Do I need to worry about such trivial details? Handle that kind of cleanup among yourselves. Consult the Military Commissioner, that stubborn bastard, if you have to. Hmm?”

“…”

The Captain of the Guards was speechless.

*Were those words or a fart?*

The City Lord’s incompetence and habit of dumping work on his subordinates were nothing new, but this was too much, even for him.

*He wasn’t always this bad. Was he?*

Several years ago, he had taken a favorite concubine, and ever since then, he had been lost in women, putting his official duties aside.

The Captain of the Guards sighed inwardly and gave a dispirited military salute.

“…I will carry out Your Excellency’s orders.”

“Of course you will. Then get to work. I have an important matter to attend to.”

Only then did the City Lord nod in satisfaction and rise from his seat.

The Captain of the Guards watched his retreating back as he huffed and puffed beneath his excessive weight, then muttered in a voice barely louder than an ant’s.

“Important matter, my ass. He’s probably going to embrace his favorite concubine again.”

The Captain of the Guards’ prediction was correct. The first place the City Lord visited after leaving the great hall was a lavishly decorated bedchamber.

“Aehyang! Aehyang!”

A beauty lying half-naked on a silk bed larger than most rooms sat up.

“My lord. Why did you take so long? Aehyang has been waiting for you.”

“Y-You have?”

The City Lord was dazed once by her coy eyes and twice by the pure white skin that flashed between the sheets. His mouth fell open in a foolish grin.

“I’m sorry. The Captain of the Guards kept bothering me.”

“That man again? My lord is already so busy. Why does he keep harassing you?”

“I know, right?”

“This is why incompetent underlings are such a problem. Without my lord, none of them could do anything.”

“You’re the only one who truly understands me, Aehyang!”

It was the sort of conversation that would have made the Captain of the Guards roll his eyes if he had heard it.

As the City Lord’s cheeks trembled with emotion, his favorite concubine opened both arms toward him.

“Come here, my lord. You’ve had such a hard time. Let Aehyang hold you.”

“Aehyang…”

At the seductive, lingering smile in his beloved concubine’s eyes, the City Lord’s gaze grew hazy.

“Could there possibly be a woman in all the world as beautiful as you?”

The City Lord had been born into a powerful family that had produced members of the Three Excellencies[^1] and had walked a smooth path throughout his life.

Backed by inexhaustible wealth, he had visited pleasure quarters countless times and held every kind of beauty in his arms.

He had taken several women as concubines whenever they caught his fancy. But because he had met so many women, his interest never lasted a year before fading.

*But this girl is different!*

He swore he had never seen a woman like her. Her voice, her gaze, even the slightest movement of her fingertips—everything about Aehyang was enchanting and lovable in the City Lord’s eyes.

He had been looking at her for several years already, yet he could not grow tired of her. No—if anything, he was sinking into her more deeply, almost frighteningly so.

“I love you. I love you, Aehyang!”

The City Lord, who was just entering his fifties, cried out with the passion of a young man in love.

As though bewitched, he approached and settled into his favorite concubine’s embrace. As he always did, he began telling her about everything that had happened that day. To the City Lord, she was the only person to whom he could confide even his most secret thoughts.

“…And so, those troublesome ruffians finally left.”

“You mean those people, don’t you? The martial artists who came here last time.”

“That’s right. The ones who brought His Highness Prince Shangshan’s Token.”

“Hmm.”

“What is it?”

“Nothing. I was just thinking that you must have had a difficult time because of this. I heard the martial artists got into a fight and many people were killed or injured.”

The City Lord shook his head with a disgusted expression.

“Don’t remind me. They dared to steal government uniforms from who knows where, put them on, and disrupt the order of the Great Nation.”

“Oh my. Is that true?”

“You may find it hard to believe, but it is. Regardless of everything else, I will certainly submit a report to the imperial court about this…”

“How gallant of you. But, my lord…”

With a sweet smile, Aehyang stroked the City Lord’s head where it rested on her lap.

“Wouldn’t things become serious if the imperial court found out?”

“H-Hmm?”

“Think about it. One day, my lord will rise to the position of one of the Three Excellencies, command all the civil and military officials, and assist the Emperor… I’m worried that the people who envy you might use this incident against you.”

“Heh heh. You truly are the only one who thinks of me this much, Aehyang.”

The City Lord gazed at his favorite concubine with overflowing affection.

But he was not a complete fool.

Though the government and Murim occupied mutually noninterfering spheres and generally ignored each other, well over a thousand people had died throughout Sichuan over the past seven days and nights.

He could leave the trivial cleanup to his subordinates, but this was something he needed to handle personally.

“Your concern is admirable, but the bigger the matter, the more trouble it causes if you try to hide it.”

“My lord, do you really think I don’t know that?”

“Hmm? Then what do you suggest?”

“Hide what must be hidden, and exaggerate your accomplishments.”

Her coquettish voice tickled the City Lord’s ear.

“Say that there was a major conflict among the martial artists, and that my lord mobilized the government troops under your command to calm the situation.”

“Hmm.”

“You will become a benevolent City Lord who restored the Great Nation’s order after it was disrupted by ruffians and cared for the common people. Of course, it would be best to leave out the part about the government weapons and uniforms. They might cause misunderstandings.”

“It would be nice if things went exactly as you say, Aehyang. But even so, submitting a false report to the court…”

“My lord, look at me.”

The hesitant City Lord let out a short exclamation when he saw her eyes, beautiful and gleaming like polished obsidian.

“Ah.”

“Do you not understand how I feel about you, my lord? How much I adore you?”

“I… That is…”

The City Lord could not finish his sentence.

The moment his eyes met his concubine’s, his mind had already gone blank.

His heart trembled at her alluring figure, and the flowerlike fragrance of her body made his senses swim.

An immense trust and affection that had risen from somewhere, along with unbearable desire, seized control of him.

“Aehyang, Aehyang!”

His voice was desperate. But the concubine caught the City Lord’s hand as it reached over to grope her body.

“My lord, what is your answer?”

“Of course I’ll do as you say. I’ll do anything for you!”

The smile at the corner of his concubine’s mouth deepened.

“Well done. Just keep doing as you have until now. Do you understand?”

“Yes, yes!”

Overcome by intense desire, the City Lord failed to notice.

He could not see the ominous sight of an eerie red light seeping into the eyes of the concubine he loved so deeply.

“Oh, what a good boy. Our City Lord listens so well.”

His favorite concubine laughed aloud.

Everything was proceeding in the direction she wanted—or rather, that person wanted.

* * *

“Hmm?”

“What is it?”

“Nothing. I thought I heard some crazy bitch laughing just now.”

“A crazy woman? Here?”

“Yeah. It gave me a bad feeling.”

Hyuk Mujin and I looked around. Three fast ships flying the flags of the Water Dragon Stronghold were moving smoothly along a broad tributary of the Yangtze, and naturally, there was not a woman aboard any of them.

“Did I hear wrong? That’s strange.”

*After everything I’ve been through lately, am I hallucinating now?*

As I was pondering this, Hyuk Mujin spoke with a serious expression.

“Could it be that…”

“That what?”

“You have been unable to forget the Young Lady standing fourth from the right in the front row?”

Gung Gibang shook his head.

“Bullshit. It was the third from the left. A beauty like that would be hard to forget.”

“Oh, so that’s what this was about?”

I smiled benevolently as I looked at the two of them.

“I think today is going to be a day neither of you forgets.”

With a bright smile, I beckoned. Several burly river pirates came running over and bowed repeatedly.

“Did you call for us, Great Hero Jin?”

“Is there something you need this humble one to do?”

“Grab those two bastards and give them a little dip in the Yangtze.”

The river pirates looked at each other in confusion.

“Uh, did you say dip?”

“We’re ignorant men, I’m afraid. What exactly does ‘dip’ mean?”

“Dipping is the proper culture… No, I mean just keep dunking their heads in and pulling them out until I tell you to stop.”

“Ohhh, understood.”

“That sounds easy enough.”

“W-Wait a minute!”

“Captain!”

Hyuk Mujin and Gung Gibang tried to resist, but it was hopeless.

One of them had only one good leg, while the other was wrapped in bandages from head to toe.

As several large, martial-arts-trained river pirates swarmed over, grabbed their arms and legs, and began the dunking show, I looked at the System Window I had already left floating in the air.

> **System**
>
> There is a bound Item whose name has not yet been decided. Would you like to check it?

*Obviously, yes.*

Ding.

> **System**
>
> **Item Window**
>
> **???**
>
> **Type:** Armor  
> **Grade:** Divine Weapon  
> **Restriction:** Jin Taekyung  
> **Description:** An armor containing the spirit of an unknown ancient master smith. It possesses truly formidable defensive power. Since its former owner has died, ownership has been bound to a new owner. Once given a name, it can be freely used anywhere.

*Its ownership was bound to me because its former owner died?*

I had wondered if that was the case, and it seemed that the item was exactly what I thought it was.

After turning my inventory upside down, I found the new bound Item. A flat, deflated sound escaped me.

“…What?”

The thing resting on my palm was nothing more than a tiny fragment. It had originally been called the Black Dragon Armor.

*I definitely blasted it away along with that bastard, the Western Heaven Demon Lord, in the final One Annihilation. Did it automatically enter my inventory because it was a bound Item?*

I could still vividly see the Black Dragon Armor shattering into pieces.

But I had no idea what I was supposed to do with a fragment this small.

*It would certainly make me feel safe if I put it in the front of my underwear.*

Ah. Was that why it was classified as armor?

I had just tugged at the front of my pants to check the most suitable position when—

“What are you doing—”

“…Ah.”

A chilly silence descended over the scene.

The boy’s face stiffened when he saw my loosened waistband and my hand shoved inside it.

After making sure no one else was nearby, the Slaughter Saint—no, Mungyeong—spoke.

“Of all places, here?”

“No, wait. I think there’s been a misunderstanding.”

I was about to hurriedly explain when Mungyeong’s gaze turned cold.

“I told you before we departed. In front of anyone other than the Fire King and Cheongpung, you are to treat me as Mungyeong.”

I answered with an aggrieved expression.

“You’re speaking informally too, asshole.”

“…!”

“Ah. Sorry.”

Mungyeong wore an expression of mixed emotions, then clicked his tongue as he glanced at the river pirates who had approached.

The transformation from a terrifying killing fiend into the Divine Physician’s Disciple and a bright young medical apprentice happened in an instant.

“What were you doing?”

“What business is it of yours?”

“…!”

This was surprisingly fun. But I couldn’t do it three times.

I quickly held out my hand toward the speechless Mungyeong.

“This got into the waistband of my pants.”

That was not entirely true, of course, but Mungyeong did not care about any of that. More precisely, his gaze had locked onto the fragment of the Black Dragon Armor.

“This is…”

“Do you happen to know this item? No, do you recognize it?”

“Where did you get it?”

“From that guy.”

Mungyeong understood that I meant the Western Heaven Demon Lord and nodded.

“You acquired a Divine Weapon. I do not know how only a fragment remains, though.”

“He called it the Black Dragon Armor.”

“The Black Dragon Armor?”

“What? Is that different from the name you knew?”

“I read about it in an old secret history. It was said to be a mysterious armor without a fixed name, one whose form and properties changed according to its owner.”

“Its form and properties change? How?”

Mungyeong answered with a look that suggested I was an idiot.

Only then did I realize what I needed to do.

*Internal energy.*

Internal energy was the very form and nature of its owner.

Ssshhh.

Following the formula of the eighth-stage Fire Gate Divine Technique, I sent lava-like energy flowing toward the fragment of the Black Dragon Armor.

The ink-black energy swirling over the fragment’s surface disappeared, and bluish-white Scorching Yang Qi filled its place.

With a pattern that looked as though flames were blazing across it, the object could no longer be called the Black Dragon Armor.

*Fire Dragon Armor.*

It was simple, but there could be no more fitting name.

At the same moment that I smiled in satisfaction, a cheerful chime rang out.

> **System**
>
> You have given the bound Item ??? a new name!
>
> You can now freely use Fire Dragon Armor anywhere!
>
> Fire Dragon Armor is resonating with your energy! It wants its owner’s strength in order to repair its damaged sections on its own!

Whoosh.

I could feel the vast amount of internal energy leaving my body and rushing toward the Fire Dragon Armor.

I pretended to tuck the energy-draining object into my arms before storing it in my inventory.

*Automatic repair? That’s incredible.*

I had definitely acquired something useful.

Thank goodness the last gift I received on this journey was the Fire Dragon Armor.

Mungyeong stared at me with wide eyes as I turned away.

“Where are you go—where are you headed?”

“What business is it of yours?”

“…”

I was starting to think I might get addicted to this.

I waved at Mungyeong, who was probably repeating the character for patience in his head.

“I’m going to take a nap. Don’t wake me.”

“…?”

Yes. Now it was time to awaken from a long sleep.

But…

*Why do I feel so uneasy? Did I forget something?*

Frowning, I found a place in the fast ship’s cabin and lay down. I closed my eyes, took a deep breath, and spoke the command.

*Logout.*

Ding.

> **System**
>
> Logging out in ten seconds. Ten, nine, eight, seven…

With the final count, the sound of splashing water and someone’s distant cries seeped faintly into my ears.

Splash! Gasp! Captain, save—gasp!

[^1]: The Three Excellencies were the highest-ranking offices in the imperial government.
## Chapter artifact 378

# Chapter 378

Ding.

> **System**
>
> **Logout** completed successfully.

Along with the cheerful System notification, the sensations that had briefly fallen away began to return.

The softness of the bed against my back. The warm air inside the private jet.

And the hands gripping and shaking both my shoulders, along with someone's shouting.

“Mr. Jin Taekyung! Wake up! Mr. Jin Taekyung!”

—Wake up, you wicked human!

At the urgent voices drilling into my ears—two voices, no, one monster and one human—I blinked.

As my vision cleared, a familiar face came into view.

“Uh, Team Leader Choi…”

Smack!

“Wake up!”

—Well done, you slightly less wicked human!

“…”

What the hell?

After taking a completely unexpected slap, I answered in a dazed voice.

“I’m awake…”

“What is wrong with you?! We’ve been trying to wake you up! Why are you only getting up now?!”

—Just die! Go ahead and die!

“S-Sorry…”

Talk about forceful. This was the first time I had ever seen Team Leader Choi this furious.

Lightning was practically shooting from the eyes of the man who usually remained calm no matter what happened and spent his time showing off designer goods.

*But what’s wrong with him? We’re still on the plane, aren’t we?*

I had apologized reflexively, but I was still bewildered. Was this really enough to earn a slap?

Then—

“This is no time for this! Hurry—”

“Aaaah!”

The rest of Team Leader Choi’s words were drowned out by the flight attendants’ screams. Shouts from men I presumed were the pilots followed.

“Mayday! Mayday! Mayday!”

“Control tower! Control toweeer!”

“…What the hell?”

What on earth was happening?

As I frantically looked around, Team Leader Choi threw out an unbelievable statement.

“We’re under attack by monsters!”

“Monsters? An attack?”

What kind of bullshit was this? We were flying at an altitude of twenty-five thousand feet in a private jet sent by China’s Central Committee.

By now, it shouldn’t have been strange to see our destination, Chengdu International Airport in Sichuan Province—

“Huh?”

I absentmindedly turned my head to look out the window, then stared with my mouth hanging open.

Far below, a vast airport spread out beneath us. Flames surged upward, and countless large and small dots moved across the grounds.

It was a battle. A savage fight to the death between humans and monsters was taking place.

And that was not all.

—Kyaoo-o-o-o!

A gigantic monster’s body rapidly approached the private jet I was riding in.

“That’s…”

There was no mistaking it. Even after rubbing my eyes and looking again, it was a Wyvern.

An A-rank monster classified as dragonkin alongside the Drake.

They were bastards I would hate to encounter even on the ground, but I especially did not want to meet them at twenty-five thousand feet.

And there were more than ten of them!

*…What the hell kind of situation is this?*

A fierce battle was raging around Chengdu International Airport below, while a group of Wyverns pursued the private jet I was riding in at twenty-five thousand feet.

It did not take my temporarily frozen brain long to reach a conclusion.

“Lich!”

The name burst from my mouth like lightning.

A week ago, by modern-world time, the highest-tier undead monster had appeared alongside an unprecedented monster wave. It had undoubtedly extended its sinister reach all the way here.

“The control tower isn’t responding!”

“The Wyverns, the Wyverns…”

“Kyaaaah!”

—I knew this would happen! We’re all dead!

Even in my panic, I corrected the Skeleton Warlord.

“That’s true, but weren’t you already dead?”

—Shut up, you wicked human! This is all your fault! Ahhh, my legion! Forgive your commander!

Human or monster, screams and shouts erupted from every direction as everyone fell into a panic.

Only one person among them had retained any semblance of sanity.

“Everyone, calm down! Nothing you’re worried about is going to happen!”

As expected of Team Leader Choi. Reliable as ever. He must have thought of a way to overcome this crisis.

After calming everyone down in a steady voice, Team Leader Choi pointed at me.

“Mr. Jin Taekyung will solve this!”

“…”

“Mr. Jin Taekyung, what should we do?”

“Wait, why are you asking me…?”

“I believe in you, Mr. Jin Taekyung!”

“…”

That was exactly the problem. Why did he believe in me? In a situation like this, believing in God, Buddha, or Allah would probably be more useful.

For a moment, I lost my ability to speak. Then the gazes of everyone around me flew toward me and pierced into my body.

“N-Now that you mention it, I’ve heard about that Hunter. They say he’s so capable that even Comrade Chairman Xiao Yang made a special request for him.”

“I’ve heard the rumors too. They say he might be a new S-rank Hunter. Apparently, he defeated two Named Monsters all by himself.”

“Ooh! Ooooooh!”

“We’re saved! We’re going to live!”

—You, wicked human! I knew you were strong, but this is beyond my imagination! Rejoice, my legion. Your commander lives!

“…I already told you, you’re dead.”

This was driving me insane. None of them were in their right minds anymore.

I stared at Team Leader Choi with utter disbelief.

“What exactly are you basing this on?”

Team Leader Choi answered without hesitation.

“I already told you. I believe in you.”

“Which means, where does that baseless faith—”

“It is not baseless.”

“Excuse me?”

“The way you are acting in a situation like this. Your tone of voice. Your expression. All of it is the basis for my belief.”

“…”

Only then did I finally realize it.

I had been caught off guard by the unexpected situation, but I was not afraid. I did not feel even the slightest bit of fear or dread.

The answer was closer than I had thought.

*Because I’m strong.*

I was strong. Stronger than before. Strong enough to avoid any danger.

That was why I was not afraid of the monsters sweeping across the ground like a wave, or the pack of Wyverns closing in right behind us.

“So that’s how it is…”

I muttered quietly to myself, then opened my mouth.

“Who’s the captain?”

A hand suddenly rose from the cockpit ahead.

It was trembling violently. With his other hand, the captain was probably gripping the controls for dear life and desperately trying to evade the Wyverns charging at us.

“I-I am.”

“Can I open the door for a moment?”

“What?”

“I’m asking if it’s okay for me to open the plane door.”

The captain must have been so shocked that he poked his head out and stared at me as if I were insane.

“Of course not! Not only is it impossible to open because of the pressure-sealing system, but the aircraft will be damaged because it can’t withstand the pressure difference! You won’t even be able to breathe properly!”

Team Leader Choi fiddled with the ring on his finger and cut in.

“I think I can block the pressure. I don’t know what you have in mind, but go ahead and try.”

“Okay.”

“Don’t! You *bangzi* bastards! Are you trying to kill us all?!”

“…What, *bangzi*?”[^1]

[^1]: *Bangzi* is a derogatory Chinese term for Koreans.

I could not believe he had insulted Koreans in front of a proud Korean Kimchi Man.

The captain’s face went pale when he realized his verbal slip.

“No, that’s not what I meant.”

“You chink bastard. Damn it.”

“…”

“Hey, Captain!”

“Yes, yes?”

“Should I open it?”

“Ah! Aah!”

Before the captain had time to stop me, I opened the door.

No—I cut it open.

Slice!

Force—the phenomenon called an Aura Blade in modern times—cut through the sturdy alloy and created a small opening.

It was the kind of overwhelming power that only an S-rank Hunter could display here, just as a Supreme Peak master could in the Murim.

Team Leader Choi’s eyes widened in shock.

“Mr. Jin Taekyung, this is…”

“Team Leader!”

Whoooosh!

This was no time to be surprised. The tremendous wind and pressure had sent the aircraft swaying, turning the cabin into a complete mess.

Team Leader Choi came to his senses at the people’s screams and my shout, then rubbed his ring.

“A flawless barrier surrounds us. Barrier!”

“Oh.”

Along with the incantation, a transparent mana barrier blocked the new opening without leaving so much as a gap.

So there was a way to do that.

With a brief exclamation of admiration, I stuck my upper body outside the cabin.

Team Leader Choi’s barrier spell recognized me as an ally and let me pass through without resistance.

Rumble, rumble, rumble!

The wind pressure slammed into my upper body as if it wanted to crush me. I grinned.

*This is no joke.*

But it was not unbearable.

No, it would have been strange if I could not withstand it. Compared to the energy waves emitted by the Western Heaven Demon Lord, this was no more than a gentle spring breeze.

—Kyaoo-o-o-o!

The monster’s sharp cry blended into that spring breeze.

The pack of Wyverns had already approached within a short distance, and I estimated the gap between us.

*About a hundred meters. I’ve never tried this before…but at this distance, it should be enough.*

*Inventory, open. Equip.*

Sssshk.

A spear purchased at a discount from the Hunter Market slid into my hand.

Like a javelin thrower, I pulled my shoulder as far back as I could. From my waist to my wrist, every muscle and tendon I needed drew taut like bowstrings.

—Kyaoo!

The leader Wyvern at the front noticed that something was wrong and threw its head back with a shriek.

I could see a mass of pure-white air being sucked toward its snout.

*That’s…*

—Breath! It’s using Breath! Dodge it, wicked human!

The Skeleton Warlord’s shout was correct.

Among countless monsters, Breath was a power granted only to the dragonkin. I could clearly see it taking shape inside the Wyvern’s wide-open maw.

Gooooom.

A gigantic sphere of wind. An Air Breath capable of shredding metal like paper had taken complete shape.

“Hey, Wyvern!”

—Kyaoo?

“I’m putting it in!”

I shouted like a thunderbolt and whipped my pulled-back shoulder forward.

Fwoosh! Sssshaaa!

The Force of flame wrapped around the spearhead, scorching the air and slicing through the wind.

The Wyvern’s bright-yellow eyes widened at the blue-white streak of light shooting straight toward it.

—Kiiiiik!

Whoooosh!

Compressed air burst from the tip of the spear. A cloud of pure white formed, and then—

Crunch! Boom-boom!

A gigantic body fell toward the ground like a kite whose string had been cut.

* * *

—Kyaoo?

—Kiiit?

More than ten pairs of bright-yellow eyes looked at one another.

Wyverns were ferocious creatures from the moment they were born, but even they were utterly bewildered at that moment, unable to figure out what to do.

—Kikik?

—Kiiik…

*What? Is the boss dead?*

*I think so…*

After exchanging words among themselves, the Wyverns were dumbfounded.

Their leader was an exceptionally powerful creature, strong enough to be called the “Black Star” among its kind.

And now, the Black Star had become a black dot as it fell toward the distant ground below.

—Kiririk?

—Grrrrk.

What was more, none of them had properly seen how it died.

They could only guess that the tiny human had thrown a spear and hit it.

But that was ridiculous.

How could a mere human dare to attack a descendant of the great dragon—

“Hey, Green Wyvern!”

—Kik?

“I’m putting it in!”

Crunch!

This time, they saw it clearly.

Their comrade’s head burst apart in the streak of light.

—Kik!

—Kyaoo-o-o!

After their leader, another of their bloodline had died!

The enraged Wyverns swore revenge on that accursed human.

—Kiiit!

Of course, not today.

They would take revenge later. A little later.

“Hey, Blue Wyvern!”

Crunch!

…Could they actually get their revenge?

More than ten pairs of wings began beating for dear life.
## Chapter artifact 379

# Chapter 379

Rumble, rumble, rumble!

A tremendous roar and vibrations transmitted through the ground.

The twenty-year-old man staring toward the horizon, Shao Shen, could not believe what was happening.

*They’re supposed to be thousands of kilometers away. How are the monsters…?*

This was not a question Shao Shen alone had asked himself.

More than a thousand Hunters from the Public Security Armed Forces Department and five thousand members of the Chinese People’s Liberation Army dispatched to maintain public order were stationed at Chengdu International Airport. Every one of them had wondered the same thing, and all of them were stunned by the reality bearing down on them.

—Screeech!

—Graaaar!

From low-level monsters such as goblins and Orcs to higher-tier monsters like Trolls, ogres, and Lycanthropes…

An army of monsters filled the horizon, charging forward with hideous shrieks.

As the distance of one kilometer rapidly closed by the second, cries like screams broke out.

“Form up by platoon! Assemble! Assemble—!”

“Fire! Fire!”

Rat-a-tat-tat! Boom!

The People’s Liberation Army hurriedly formed ranks and unleashed their firepower at their commanders’ orders, but the effect was utterly negligible.

An unexpected army of monsters had attacked.

The soldiers, ordinary people without any abilities, were paralyzed with fear. The weapons they fired were effective only against low-level monsters at best.

“There are too many monsters! There are too many!”

“Pilots!”

“Get the fighter jets into the air! Bomb them from above—!”

The frantic shouts of the commanders were drowned out the next moment by a vicious roar that echoed through the sky.

—Kyaaaao-o-o!

“W-What is that?”

“Wyvern! It’s a Wyvern!”

A gigantic body flew in with the setting sun behind it.

A Wyvern, known as the terror of the skies, led the way, followed by dozens of Griffons and Gargoyles.

The A-rank monsters angled their several-meter-long wings and dove upon the fighter jets that had not yet managed to take off.

Crunch! Boom!

The tons of metal lurched beneath their powerful wingbeats, while the aircraft hulls were torn apart like sheets of paper by claws imbued with mana.

Metal fragments blasted away with tremendous force alongside the explosions, crashing into the pilots who were running frantically toward their planes.

Boom! Crunch!

They died instantly, without even leaving behind a scream.

The firearms roared at the commanders’ orders once they regained their senses, but the monsters’ skin and hides, saturated with powerful mana, could do no more than suffer scratches beneath hundreds or thousands of bullets.

—Kikikik.

At the monsters’ laughter mocking the helpless humans, everyone felt a shock of terror that made the hair on their entire bodies stand on end.

“H-How can this be?”

An army of monsters filled both the ground and the sky. The creatures were monsters in every sense of the word, and even firearms barely affected them.

“M-Monsters…”

“I-I have to live. I don’t want to die like a dog in a place like this!”

The fear of death spread faster than any epidemic.

And while the members of the People’s Liberation Army were slowly backing away, one person was instead advancing toward the front.

“Don’t retreat!”

Shao Shen, a young man who had not yet lost all traces of his youth, shouted with blazing eyes.

The Five-Starred Red Flag, the national flag of the People’s Republic of China, was embroidered across the chest of his armor.

“Who are we?”

At the young man’s question, those who had been trying to flee stopped in their tracks.

Shao Shen glared at the army of monsters charging from several hundred meters away. His voice thundered out once more from beneath his tightly pulled-down helmet.

“Who are we?”

His shout made their blood boil.

With every eye upon him, Shao Shen raised the tip of his spear.

“We are the descendants of Zhonghua, and we are brothers in the People’s Liberation Army and the Public Security Armed Forces Department!”

An aura resembling the light of the setting sun rose from the spearhead, which had been thrust high enough to pierce the heavens.

Hissss!

“Let’s go! Let’s wipe out every last one of those monsters!”

“Waaaaaaah!”

A tremendous roar that numbed the ears shook the earth.

Led by Shao Shen, the Hunters of the Public Security Armed Forces Department gripped their weapons and charged toward the army of monsters like ravenous tigers.

“Don’t retreat! Show them the strength of Zhonghua!”

“Uaaaaah!”

—Graaaar!

—Awooooo!

Human cries filled with the resolve to face death mingled with the monsters’ shrieks. The two groups collided and became entangled in one mass.

Kwagwagwagwang!

A clash that shook the sky and earth. Death rained down from every direction.

“Gyaaaah!”

—Kweeeek!

Squish! Crack!

Screams and thunderous noises rang out from every part of the battlefield.

An A-rank Hunter’s aura-coated blade sliced through a Lycanthrope’s neck, while the iron club swung by an ogre turned three or four Hunters into bloody pulp and sent them flying.

Two Hunters combined their strength to bring down a monster, then raised their weapons toward the next enemy. A gigantic shadow fell over their heads.

—Kiiiiiit!

Slice!

The claws of a Griffon diving straight down tore the Hunters’ bodies apart along with their armor.

A large ball of fire flew toward the Griffon as it searched for its next prey.

“Fire Ball!”

Boom!

The Griffon’s body, gliding through the sky, lurched amid the acrid smoke. The ranged units on the ground, waiting for the perfect opportunity, did not let the opening pass.

“Now!”

Bang! Boom-boom-boom!

All manner of spells and arrows brimming with mana pierced the Griffon.

As the Griffon plummeted with a dying shriek, the flying monsters let loose ferocious cries.

—Kyaaaao-o-o!

Modern weapons made of lead and iron blocked the flying monsters as they plunged toward the ranged units.

“Concentrated fire, commence!”

Rat-a-tat-tat-tat! Boom!

Countless rifles and heavy weapons, along with dozens of tanks, belched fire all at once.

Though modern weapons could not compare to mana—the natural counter to the monsters’ magical power—concentrating their firepower all at once forced even the flying monsters to hesitate.

—Kiiit!

“It works!”

“It’s useless anywhere else! Aim for their eyes!”

The flesh of monsters, which had been saturated with mana since birth, easily ignored most physical force. But there was one exception: their eyes.

Their eyeballs, covered by a thin membrane, could be damaged sufficiently if heavy weapons were brought to bear.

At the sight of the monsters hesitating, the divisional commander, who had been watching the entire scene, excitedly waved his command baton.

“More! Pour it on! Don’t let those monsters move—”

Rooooar!

His voice never continued.

The Poison Breath fired by a Green Wyvern blanketed an area over a hundred meters in radius, and the divisional commander and his command staff were drenched in the powerful acidic poison and melted away.

“C-Commander!”

“The command staff…!”

The People’s Liberation Army lost hundreds of soldiers and high-ranking officers in the blink of an eye and fell into a state of panic.

Officers, noncommissioned officers, and soldiers alike stared at the horrific scene unfolding before their eyes, crying out in shock.

“This can’t be happening…”

“N-No. This isn’t right. It can’t be! This isn’t my mission!”

Someone’s scream spoke for everyone’s feelings.

They had brought their forces in preparation for an emergency, but their primary mission was to join and escort the foreign Hunters who would soon arrive at Chengdu International Airport, then act according to their superiors’ orders.

They had never heard a single word about an army of monsters that was supposed to be thousands of kilometers away invading them.

“What the hell is this…?”

“We’re going to die. We’re all going to die.”

The fear they had briefly forgotten settled over the heads of the People’s Liberation Army.

They were not the Hunters from the Public Security Armed Forces Department fighting at the front of the battlefield. They were nothing more than ordinary people carrying modern firearms.

And their ominous suspicion soon became reality.

A nightmare worse than anything they had imagined.

—Om. Neu. Ha. So. Yu.

A voice broken into disconnected syllables. An eerie noise resembling the static of a radio with an unstable signal echoed across the battlefield.

Black fog that had gathered from somewhere spread over the people’s heads.

—Yen. Wi. Ga. Ji. Ke!

That was when the horrific change occurred.

Swoosh!

Dark mana, black as storm clouds, spread like a web through the blood and corpses.

It breathed new power and souls into the corpses growing cold, binding them in chains and subjugating them.

Thud. Thud-thud-thud.

An army of skeletons gained new life and slowly rose from pools of death.

*Those beings* had woven countless dead together with invisible chains and made them their slaves. They laughed with satisfaction.

—Kik, kikikik.

—Grrk. Kihihih.

* * *

—Grrrrrk.

With a bubbling sound, a man rose to his feet.

He wore armor emblazoned with the Five-Starred Red Flag and carried a massive ax. He looked exactly like the A-rank Hunter Shao Shen remembered.

*…Mr. Yao Wei.*

But Shao Shen could not call the man’s name aloud. He could not bring himself to.

Because he knew that the person standing before him was no longer the man he had known.

*Ah… ahhh.*

If he had not witnessed the man’s head being severed only ten minutes earlier—if he had not seen him rise at this very moment with his own severed head tucked beneath his arm—Shao Shen would have thought of him as a colleague and friend.

But Yao Wei no longer existed.

A new name slipped between Shao Shen’s lips.

“Dullahan…”

A headless knight. A Dullahan.

Shao Shen bit his lip at the sight of his former colleague transformed into a high-level undead monster. Something hot ran down his cheek.

“I’m sorry. I truly am.”

—Graaaar!

As the Dullahan charged with a shriek, Shao Shen shot forward like the wind.

In the past, the two of them had often sparred like this. What began as simple competitive pride continued every day, and whenever the sparring ended, Shao Shen had to put up with Yao Wei’s complaints.

*You little punk, where are your manners? Would it kill you to let me win once?*

*Ha-ha. Let’s go get something to eat. The loser was supposed to pay, so I guess you’re buying again today, Mr. Yao Wei.*

*You’ve got plenty of money at home, and you’re still so greedy. One day, I’ll make you buy me a meal.*

But that had never happened before, and it never would.

Shao Shen had always been the winner.

*Goodbye. Thank you for everything.*

Whoosh! Slice!

The ax swung through empty air, while the aura surging from Shao Shen’s spearhead cleaved through the Dullahan’s upper body.

A line was drawn from the waist upward. The headless knight’s body slowly collapsed.

Thud. Crash.

Shao Shen stared blankly down at the face of the fallen Dullahan—or rather, Yao Wei—and his eyes burned.

“How dare you… How dare you do this…”

Only half a day ago, his friends and colleagues had been laughing and chatting alongside him. Now they had become undead monsters.

The Hunters of the Public Security Armed Forces Department were famous for their strict discipline, but they were not cold-blooded people without a drop of blood in their veins.

The Hunters who had entered battle prepared to die now faced a new kind of fear for the first time: their attachment to one another.

“Get a grip! It’s me, Liu Yinqin! Liu Yinqin!”

“Hyung…!”

—Grrrrrk!

Crack! Boom!

Screams and death rained down from every direction. Unlike the Public Security Armed Forces Department, which had suffered losses approaching half its strength, the army of monsters had actually increased its numbers and continued pouring forward without end.

*Am I going to die here, like this?*

For the first time in his life, Shao Shen thought of death. The situation was desperate enough to make even someone as bright and cheerful as him think that way.

*We never received a warning signal, so communications are probably down. There won’t be any reinforcements either… This really is the end.*

Slice!

After cutting down one undead monster after another as they charged him, Shao Shen laughed hollowly and looked up at the sky.

The sunset was quite beautiful. Once the sun went down and darkness arrived, he would never see a sight like this again.

*At least the last sky I see is pretty decent…*

Huh?

Shao Shen blinked, unable to continue his thought.

Something enormous was approaching the battlefield at tremendous speed high above.

*An airplane?*

Roooooar!

A gigantic aircraft wreathed in flames. And someone’s shout echoing across the vast sky.

“Hey! Monsters!”

“…”

—…?

*Am I hearing things?*

Everyone on the battlefield, not only Shao Shen, looked up at the sky.

Someone’s voice, carrying an almost palpable madness, rang out like thunder.

“I’m going to ram it!”

Ram what?

Shao Shen soon understood what those words meant.

Rumble, rumble, rumble!

The airplane’s enormous fuselage swept straight across the battlefield.

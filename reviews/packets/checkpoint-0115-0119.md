# Checkpoint Review — 115–119

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

# Chapters 115–119

## Plot

Jin Taekyung and Jin Mukyung enter the Mount Heng fortress after finding Cheol Mubaek critically wounded by Pung Yang’s Temporary Strength Pill. Wolhwa and Hyuk Mujin remain behind to protect Cheol while the Jin brothers attack the Red Wind Band. Although Mukyung initially dominates, Pung Yang consumes another pill, gains enough power to produce imperfect Sword Force and Body-Protecting Qi, and reverses the fight. He reveals that he obtained the Crimson Blood Twelve Swords, the Crimson Blood Cultivation Technique, and five Temporary Strength Pills from a hidden plateau tomb, killing his companions to keep the legacy.

Mukyung appears to break Pung Yang’s defensive qi, but concealed throwing knives leave him unconscious. Taekyung consumes Jopil’s Blazing Flame Divine Pill, gaining thirty years of Scorching Yang Qi and temporarily raising his internal energy to forty-five years. He outmaneuvers Pung Yang and wounds him with a dagger before his Body-Protecting Qi fully forms, but the divine pill’s energy runs wild and severely damages Taekyung. As Pung Yang’s Temporary Strength Pill begins to wear off, Lee Seowol and nine surviving Mount Heng martial artists make a last stand so Taekyung can escape with Mukyung.

Taekyung refuses to flee and attacks with One Annihilation, but Pung Yang destroys it, severely injures him, and captures him. When Pung Yang attempts to mutilate him, Taekyung summons the Unnamed Sword. Its Ten-Thousand-Year Cold Iron destroys Pung Yang’s Body-Protecting Qi, leaving the confrontation unresolved.

## Continuity

- Cheol Mubaek is alive but critically injured, with broken limbs and severe internal injuries; Wolhwa’s medicine provides only temporary support.
- Jin Mukyung is unconscious after Pung Yang’s five concealed throwing knives; his recovery is unresolved.
- Pung Yang reached the Peak realm through the Crimson Blood martial arts and heterodox cultivation in two years.
- Pung Yang has approximately seventy percent mastery of the Crimson Blood Twelve Sabers and can temporarily manifest imperfect Sword Force and powerful Body-Protecting Qi with a Temporary Strength Pill.
- Pung Yang’s Temporary Strength Pill began losing effect after roughly half a shichen. He retained one final pill but refused to take it because using three consecutively could endanger his life.
- Pung Yang still intends to capture both Jin brothers and obtain the Taiyuan Jin Family’s martial arts formulas.
- Taekyung consumed the Blazing Flame Divine Pill and gained the Scorching Yang Qi attribute, but its uncontrolled energy caused severe internal injury and a major drop in his stats. The Divine Pill Absorption Quest remains active, and his survival is uncertain.
- Taekyung’s iron spear was cut to less than half its length; he learned Pung Yang’s attack pattern before the final exchange.
- Lee Seowol and nine other surviving Mount Heng Sword Sect martial artists began a sacrificial last stand to protect Taekyung and Mukyung; their fate is unresolved.
- Taekyung’s Unnamed Sword destroyed Pung Yang’s Body-Protecting Qi at the endpoint. Taekyung’s and Pung Yang’s final conditions, and whether either survives, remain unresolved.
- The Peak Quest’s Lunar New Year invitation to the Jin Family remains the governing objective.

## Translation Decisions

- Retain **Peak**, **early Peak**, **First Rate**, **Red Wind Band**, **Sect Leader**, **Taiyuan Jin Family**, **Scorching Yang Qi**, and **Body-Protecting Qi**.
- Render **잠력단** as **Temporary Strength Pill**.
- Render **적혈십이도** as **Crimson Blood Twelve Sabers**, distinct from **Crimson Blood Twelve Swords**.
- Render **열화신단** as **Blazing Flame Divine Pill** and **영단 흡수** as **Divine Pill Absorption**.
- Render **만년한철** as **Ten-Thousand-Year Cold Iron** and **이름 없는 검** as **Unnamed Sword**.
- Render **내상** as **Internal Injury** and **중상** as **Severe Injury** in System notifications.
- Render **일 식경** as **one meal’s time** in this passage.
- Retain **Narye tagon** with a footnote explaining its lazy-donkey imagery; render **격산타우** as **Striking the Ox Across the Mountain** with a footnote explaining force through an obstacle.

## Durable state

{
  "active_continuity": [
    "Cheol Mubaek was critically injured after Pung Yang defeated him using a Temporary Strength Pill.",
    "Pung Yang possesses the Crimson Blood martial arts and has reached the Peak realm through them and the Temporary Strength Pill.",
    "Pung Yang can temporarily manifest imperfect Sword Force and can maintain powerful Body-Protecting Qi after taking the pill.",
    "Pung Yang has reached approximately seventy percent mastery of the Crimson Blood Twelve Sabers.",
    "Jin Mukyung is a young Peak-level swordsman known as the Heaven Shaking Sword.",
    "Jin Taekyung is a First Rate martial artist who uses One Annihilation with his iron spear.",
    "Jin Mukyung's visible duel with Pung Yang ended in Mukyung's favor, but Pung Yang's concealed throwing knives left Mukyung unconscious.",
    "Pung Yang killed more than ten Mount Heng Sword Sect martial artists after incapacitating Mukyung.",
    "Pung Yang plans to take both Jin brothers and obtain the Jin Family of Taiyuan's martial arts formulas.",
    "Jin Taekyung has taken the Blazing Flame Divine Pill, temporarily gaining Scorching Yang Qi and raising his internal energy from fifteen to forty-five years.",
    "The Blazing Flame Divine Pill's energy may kill Taekyung if he cannot control it, and the System has created the Divine Pill Absorption Quest.",
    "The pill's temporary energy increase lets Taekyung read and evade Pung Yang's attacks more effectively.",
    "Pung Yang knows the Temporary Strength Pill is a secret legacy of demonic, heterodox arts and has taken it several times.",
    "Pung Yang cut Taekyung's iron spear to less than half its length, but Taekyung learned his attack pattern.",
    "Taekyung's dagger inflicted a serious internal injury on Pung Yang by striking before his Body-Protecting Qi fully formed.",
    "Taekyung's thirty years of Scorching Yang Qi is running wild and has caused severe internal injury and a major drop in all stats.",
    "Pung Yang's Temporary Strength Pill began losing its effect after approximately half a shichen; he will not use his last pill because taking three consecutively could endanger his life.",
    "Lee Seowol and nine other surviving Mount Heng Sword Sect martial artists made a last stand to buy Taekyung time to escape with Jin Mukyung and asked him to avenge them.",
    "Taekyung's One Annihilation was defeated, after which Pung Yang severely injured and seized him.",
    "The Unnamed Sword's Ten-Thousand-Year Cold Iron destroyed Pung Yang's Body-Protecting Qi at the chapter's endpoint; neither man's final fate is established."
  ],
  "continuity_sources": [
    119
  ],
  "open_questions": [
    "Can Taekyung survive his severe injuries and the runaway Scorching Yang Qi?",
    "Can Taekyung defeat Pung Yang now that the Unnamed Sword has destroyed his Body-Protecting Qi?",
    "Can Pung Yang survive his internal injury and the loss of his Body-Protecting Qi?",
    "Will Lee Seowol and the nine other surviving Mount Heng martial artists survive their last stand?",
    "Will Jin Mukyung recover from the five concealed throwing knives?",
    "Will Pung Yang obtain the Jin Family's martial arts formulas?",
    "What is the origin and full long-term effect of the Temporary Strength Pill?",
    "What lasting consequences will the Blazing Flame Divine Pill have if Taekyung survives?"
  ],
  "safe_through": 119,
  "temporary_decisions": [
    "Render 일류 초입 and 절정 초입 as early First Rate and early Peak.",
    "Render 잠력단 as Temporary Strength Pill and 호신강기 as Body-Protecting Qi.",
    "Render 격산타우 as Striking the Ox Across the Mountain and 북망산 as Mount Beimang, with a burial-ground footnote.",
    "Render 열화신단 as Blazing Flame Divine Pill and 반 갑자 as half a jiazi, clarified as thirty years.",
    "Retain Narye tagon for 나려타곤 with a footnote explaining the idiom.",
    "Render 만년한철 as Ten-Thousand-Year Cold Iron.",
    "Render 이름 없는 검 as Unnamed Sword.",
    "Render one 식경 as one meal's time in this passage."
  ],
  "version": 1
}

## Reading copies

## Chapter artifact 115

# Chapter 115

Cheol Mubaek, the Tiger of Mount Heng.

I had heard that name several times already. Wolhwa had said that without him, the Mount Heng Sword Sect would have been wiped out by the Red Wind Band long ago.

*“He’s considered a Peak master comparable to or even stronger than the Blood Wolf Sword, Lee Cheonbaek.”*

She had definitely said that.

*Then why has that incredible Peak master ended up like this?*

His limbs were twisted at unnatural angles, and the black blood soaking his shirt was proof of severe internal injuries. Cheol Mubaek looked at us through hazy eyes.

“Taiyuan… Jin Family?”

“Oh, you recognize us?”

I forced the corners of my mouth upward. I wanted to reassure Cheol Mubaek, who was in critical condition, even if only a little.

The man before me was no longer the renowned Peak master known throughout the Murim. He was nothing more than an old man who had found his last hope.

“Red Wind Band… inside… Seowol’s in danger…”

Even without hearing Cheol Mubaek’s halting words, everyone here understood how serious the situation was. Everywhere we looked, there were corpses and pools of blood.

*But it’s not too late yet.*

> **System**  
> **Time Limit:** 00:05:12

We had made it just in time. The problem was that the bastard who had reduced the Tiger of Mount Heng to this state was still inside.

Wolhwa seemed to have reached the same conclusion. She calmed Cheol Mubaek and asked,

“Sir Cheol, did Pung Yang attack you together with another master?”

Cheol Mubaek gave a faint shake of his head.

“You’re saying Pung Yang defeated Sir Cheol by himself?”

“R-red pill. Be careful of that bastard…”

A red pill?

I wanted to ask more, but that was the limit of Cheol Mubaek’s strength. His lips moved soundlessly, then his head drooped. Hyuk Mujin sucked in a startled breath.

“H-he’s dead.”

“…He’s still alive.”

“Oh. So he is. His breathing was just so faint…”

Hyuk Mujin, you bastard. What kind of person kills even the living?

Still, he wasn’t entirely wrong. Cheol Mubaek’s thin breath was so precarious that it could stop at any moment.

That was when Wolhwa pulled a small porcelain bottle from inside her robes.

“Could you lift his head a little?”

She tilted the bottle into the unconscious Cheol Mubaek’s mouth.

As an unidentified green liquid trickled down his throat, color gradually returned to his pale face. It seemed to be a remarkably effective medicine.

“This will help him catch his breath, but it’s only a temporary measure. In his current condition, even a child would be too much for him to handle. You understand, right?”

In short, someone had to stay behind to protect Cheol Mubaek in case something happened. I nodded without hesitation.

“Then Mujin can—”

“Two people stay behind.”

“Huh? Two people?”

What was he talking about? Jin Mukyung met my gaze and looked back at me as if he couldn’t understand what the problem was.

“Why?”

“No, you mean the two of us should go?”

“Is there a problem?”

…

Of course there was.

*Pung Yang had turned a formidable Peak master like Cheol Mubaek into a half-dead man, and he still had all those mounted-bandit bastards under his command.*

We were at the point where we needed every hand we could get, and he was suggesting this?

I didn’t know about Hyuk Mujin, whose abilities were still questionable, but Wolhwa absolutely had to come with us.

“Can the two of you manage?” Wolhwa asked.

I hurriedly opened my mouth.

“Obviously, that’s—”

“We can.”

Just as I was about to say it was impossible, Jin Mukyung’s deep, dark eyes fixed on me.

“I said we can. Trust me.”

His calm yet confident words left me speechless.

For a moment, I wondered if this was merely the reckless bravado of an immature young man. But then I realized I was shaking my head inwardly.

*The Heaven Shaking Sword. A martial arts genius.*

The guy standing before me was a monster born from the combination of effort and talent. From everything I had seen, he wasn’t foolish enough to throw his life away for nothing.

And then…

> **System**  
> **Time Limit:** 00:02:21

Damn it. There was no time left to hesitate.

I let out a deep sigh and asked Jin Mukyung,

“Are you confident?”

“This is the best option. Someone of middling skill would only become a burden.”

Wolhwa let out a quiet laugh.

“My, you’re awfully honest.”

“…I apologize for that.”

“Well, that’s all right. You’re not wrong.”

That was the first time I had ever seen him apologize to anyone.

Hyuk Mujin interrupted this rare spectacle.

“Second Young Master, I’m a martial artist too!”

“Then follow us. But staying alive is your responsibility.”

“On my own…?”

“I guarantee that once the fighting begins, the enemy will target you first. There’s nothing wrong with fighting bravely as a martial artist and dying.”

After a brief silence, Hyuk Mujin answered with a resolute expression.

“As a martial artist, I will safely protect Sir Cheol, who walks the same path of martial arts as I do.”

…

Sometimes, I wondered if that guy was even human.

*If I had the time, I’d beat the hell out of him.*

But even now, time continued to pass.

> **System**  
> **Time Limit:** 00:01:09

“Whew.”

I gripped the spear I had already taken out and spoke to Jin Mukyung.

“I’ll handle the small fry.”

“Usually, at a time like this, shouldn’t you say that you’ll take the leader?”

“Yeah. Throw away that stereotype.”

“You’re ridiculous.”

“Let’s just say I know my place.”

“Fighting spirit and competitive pride help a martial artist grow.”

“And hasten his death. I’ve learned to choose my opponents carefully, so deal with Pung Yang using all that overflowing fighting spirit and competitive pride.”

“You certainly have a way with words.”

“Oh, and when we get inside, approach as quietly as possible. Then ambush them when I give the signal. Got it?”

“Ambush?”

“Use the essence of an ambush to inflict as much damage as possible at the beginning. While the enemies are thrown into confusion, we’ll get to the Sect Leader of the Mount Heng Sword Sect…”

“I see.”

“Good. It’s nice to be understood for once.”

That took care of every preparation. Forty seconds. Thirty-nine. Thirty-eight.

I watched the numbers fall and was just about to walk toward the door when—

Clomp.

There wasn’t even time to stop him.

Jin Mukyung strode inside and let out a shout infused with internal energy.

“Pung Yang!”

> **System**  
> **Time Limit** has disappeared.

…

Jin Mukyung, you fucking asshole.

* * *

“Marriage? I’d choose death instead.”

Pung Yang clicked his tongue as he watched Lee Seowol draw a silver dagger and hold it to her own throat.

“You’re making this awfully difficult. You really are the Blood Wolf Sword’s daughter.”

Though Pung Yang was a master of throwing knives, he couldn’t fully display his specialty in his current condition.

*Damn old man… He actually forced me to use the Temporary Strength Pill.[^1]*

Even Pung Yang possessed only three of these precious pills. Using one had allowed him to defeat Cheol Mubaek, but the aftereffects were considerable.

He hid his hands, trembling like aspen leaves, beneath his sleeves and said,

“Bring everyone who’s still breathing.”

“Yes, Leader.”

Not long after the order was given, martial artists from the Mount Heng Sword Sect were dragged over, bound hand and foot. Darkness settled over Lee Seowol’s face.

“What are you planning to do?”

Pung Yang smiled.

“You can probably guess. First, I’ll cut off their limbs one by one in front of you. Arms, legs, this and that. It won’t be a pleasant sight, so I recommend closing your eyes.”

“If you do that…”

“If you’re going to kill yourself, I won’t stop you. But your loyal subordinates will be slaughtered for it.”

Lee Seowol clenched her teeth.

“That isn’t what you want, is it?”

“If my bride-to-be says she’s going to die, what else can I do? Still, the Blood Wolf Sword’s secret martial art and the Tiger of Mount Heng’s martial arts formula would be enough. Ah, I should take that old man Cheol with me on the way back, too.”

“…Uncle Cheol is still alive?”

“Of course. How could I kill a Benefactor who is going to hand over such a precious martial arts formula?”

“…”

“I’ll stake my life on this promise. It’s not too late even now, so marry me. If you do, I’ll let everyone live. I’ll stop at destroying their dantians.”

That was the decisive blow.

Lee Seowol’s eyelashes trembled for a while before she slowly lowered her hand.

“Keep your promise.”

“A wise choice.”

A triumphant smile spread across Pung Yang’s face.

From this day forward, he would begin his third life.

He had gone from a beggar boy to a mounted bandit. Now, he would finally don the mask of an orthodox faction and become the true master of the Mount Heng Sword Sect.

Though there had been heavy losses, it didn’t matter. New wine belonged in new wineskins. Under the name of the Mount Heng Sword Sect, he would recruit martial artists and expand his power.

*If the Blood Wolf Sword could do the same thing over thirty years ago, why couldn’t I?*

Just as the corners of his mouth lifted with overflowing delight—

“Pung Yang!”

A shout infused with internal energy shook the heavens and earth.

Lee Seowol, Pung Yang, and every surviving person turned their heads as if they had made a pact.

A young man dressed in black as dark as night was walking toward them from some fifty jang away.[^2]

*A master.*

A chill ran through some corner of Pung Yang’s chest beneath the young man’s needle-sharp gaze.

He was a master. And not merely a master—he was a Peak master who was in no way inferior to Pung Yang himself. Pung Yang could tell just from the way the young man’s hand moved as it gripped his sword hilt.

*There are only two Peak masters this young in Shanxi. And if one of them is a swordsman…*

The answer came immediately.

Jin Mukyung, the Heaven Shaking Sword. A genius who had reached the Peak realm while still in his early twenties.

More importantly, behind him stood the Jin Family of Taiyuan, which had risen to become the foremost family in Shanxi.

*At least he came alone.*

But the next moment, another person cautiously stuck his head out through the fortress gate Jin Mukyung had entered.

The young man wore a navy martial robe. His clothing, the dark iron spear in his hand, and above all, his nearly identical face told Pung Yang who he was.

“The Sleeping Dragon of Shanxi?”

At the nickname that escaped someone’s mouth, Jin Taekyung flinched and muttered,

“Fuck. I knew this would happen.”

Jin Taekyung came sauntering forward, cursing crudely in a manner unbecoming a scion of a prestigious family, while Jin Mukyung followed at an easy pace.

The two brothers were heading straight toward Pung Yang.

*The Taiyuan Jin Family, at a time like this… This is very bad.*

The family’s reputation, built over many years, and the fame it had gained through the battle at Eight Spring Gorge had made the Jin Family’s current standing unrivaled.

Because of that, countless young people across Shanxi who dreamed of becoming martial artists were flocking to the Jin Family.

That was why, even if Pung Yang swallowed the Mount Heng Sword Sect right now, he would still have to bow flat and hide his claws.

*Once I get past this hurdle, my opportunity will come.*

The Mount Heng Sword Sect had already collapsed. The Murim was a world where the strong preyed on the weak, and Pung Yang was a new power in that world. Even if his opponent was the Taiyuan Jin Family, he believed he had earned the right to be treated with respect.

Clomp. Clomp. Clomp.

Each time Jin Mukyung and Jin Taekyung took a step, the mounted bandits of the Red Wind Band retreated in confusion.

By the time the two men reached him, Pung Yang raised his hands in a formal salute.

“I am Pung Yang, Red Wind Band Leader.”

If Pung Yang had not been a seasoned martial artist who never lowered his guard, or if the effects of the Temporary Strength Pill had not still lingered faintly, he would never have avoided that strike.

Shiiiiing!

He hurriedly twisted his body.

A dazzling streak of Sword Energy skimmed past his neck and sliced through three mounted bandits behind him.

“Is this the will of the Taiyuan Jin Family?”

Jin Taekyung, who had already felled the mounted bandits nearby, muttered,

“I’d rather talk it out.”

“You fucking bast—”

Before Pung Yang could finish speaking, another streak of Sword Energy flew in and grazed his back.

The pain felt like being burned by fire.

He barely avoided the continuing attack, and his assessment of Jin Mukyung had to change.

*He’s stronger than me.*

At this level, Jin Mukyung’s movements were comparable to Cheol Mubaek’s. On top of that, Jin Taekyung was slaughtering Pung Yang’s subordinates.

Pung Yang realized that he had only one option left.

*The Temporary Strength Pill.*

While his subordinates died one after another trying to stop Jin Mukyung, Pung Yang pulled the wooden case hidden inside his robes and tipped the pill into his mouth.

Shiiiiing!

Jin Mukyung’s blue Sword Energy was reflected in Pung Yang’s eyes, which had turned blood-red.

Slice!

[^1]: The pill’s name literally means “Temporary Strength Pill.”

[^2]: A jang is a traditional unit of distance, roughly three meters.
## Chapter artifact 116

# Chapter 116

The moment Jin Mukyung’s Sword Energy split Pung Yang’s back, I thought,

*This fight is won.*

It was hard to predict the outcome of a life-and-death duel between Peak masters.

But even to me, someone who had yet to reach the Peak realm, the difference between Jin Mukyung and Pung Yang was obvious.

*Is Jin Mukyung really that strong, or was Pung Yang weaker than I thought?*

Had he exhausted all his strength in his earlier fight with Cheol Mubaek, the Tiger of Mount Heng?

What mattered was the fact that Jin Mukyung held an overwhelming advantage.

Slice! Shraaak!

“Gaaaaah!”

Pung Yang retreated, using his subordinates as shields, while Jin Mukyung pursued him without hesitation, cutting his way through them. As the mounted bandits of the Red Wind Band scattered in all directions to avoid the blue Sword Energy, Pung Yang was revealed standing alone.

*It’s over.*

That was when I clenched my fist in triumph.

Then I saw the red pill in his hand.

*Wait. A red pill?*

It was the very thing Cheol Mubaek had mentioned. At the same moment the warning bells began ringing in my head, Pung Yang tossed the pill into his mouth.

Jin Mukyung didn’t miss the opening. His blue Sword Energy plunged toward the crown of Pung Yang’s head.

Shiiiiing! Slice!

Blood sprayed through the air. One shoulder was cut deeply.

The person staggering backward was none other than Jin Mukyung.

I blinked.

*What the hell just…*

What had happened?

The System answered my question.

> **System**
>
> A sudden Quest has been generated.
>
> **Quest**
>
> **Temporary Strength Pill**
>
> Red Wind Band Leader Pung Yang has taken a Temporary Strength Pill (暫力丹) and is currently empowered by abnormal strength. Defeat him and save the Mount Heng Sword Sect.
>
> *The Quest will fail if Lee Seowol dies!*
>
> **Grade:** Supreme Peak
>
> **Restriction:** Jin Taekyung
>
> **Task:** Stop or defeat **Lv.??? Pung Yang** (Incomplete)
>
> **Reward:** ???
>
> **Failure:** ???

A Quest with a Grade of Supreme Peak.

I skimmed through the details and immediately understood why that bastard had grown so strong.

“Temporary Strength Pill? Don’t tell me…”

I gaped at Pung Yang.

He looked completely different from before. His eyes had turned completely bloodred. Veins bulged beneath the skin exposed below his sleeves, and his muscles looked ready to burst. On top of that, the sheer force radiating from him made it frightening to even approach.

*There’s no mistaking it.*

No, fuck…

A fucking Peak master, cheating by doping?

* * *

“Heh-heh-heh.”

Pung Yang let out a low laugh.

Power and vitality surged throughout his body. His head burned hotter than ever, and everything in his field of vision seemed weak and insignificant.

The internal energy boiling in his dantian only added to the sensation.

*So this is the power of the Temporary Strength Pill.*

It was an unknown red pill capable of drawing out twice the strength a person currently possessed—no, even more than that—for a limited time. Pung Yang himself didn’t know who had made it or how.

It was, quite literally, a fortuitous encounter bestowed by the heavens.

*The Crimson Blood Twelve Swords. The Crimson Blood Cultivation Technique. And a wooden case containing five Temporary Strength Pills.*

Among the countless tombs hidden on the vast plateau, Pung Yang had discovered a Peak-level martial arts manual and the Temporary Strength Pills in one of them. The moment he found the Peak-level manual and Temporary Strength Pills left behind by an unknown person, he realized he had encountered a great opportunity.

He also realized that such treasures could not be shared with anyone.

*Even if I went back to that time ten times, I would have made the same choice.*

Pung Yang killed his subordinates and kept the fortuitous encounter for himself, then began training in a hidden refuge that no one ever visited. In only two years, he reached the Peak realm.

The absurd speed of his growth and the killing intent that surged from him at unpredictable moments made him realize he had learned demonic, heterodox arts.

But it didn’t matter to him.

*This is the Murim!*

In a world where strength was the law, arguing over whether something was orthodox, heterodox, or demonic was laughable. After returning to the plateau, Pung Yang quickly began to distinguish himself.

His intelligence was far beyond that of the other mounted bandits, and his martial arts were exceptional.

By using violence and rewards in just the right measure, he quickly bent his subordinates to his will. Of course, he had faced crises as well.

But Pung Yang possessed a wondrous treasure he had never shown to anyone.

*That was when I first learned what the Temporary Strength Pill could do.*

One against a hundred? It was far beyond that.

After taking a Temporary Strength Pill, he became an invincible master whom no one on the plateau could withstand.

Two major mounted-bandit groups that had tried to eliminate their new competitor were wiped out overnight. It was only natural that the Red Wind Band, led by Pung Yang, would take their place.

*But that was as far as I could go.*

Demonic, heterodox arts could be learned quickly through shortcuts, but they lacked depth. Just as Pung Yang was trying to make up for that weakness with orthodox martial arts, two places caught his eye: the Jin Family of Taiyuan and the Mount Heng Sword Sect.

A battle between a dragon and a tiger.

Pung Yang didn’t care which one fell.

At first, Lee Cheonbaek had hired him with the Jin Family of Taiyuan’s martial arts promised as payment…

But things had become complicated, leading him to this point.

*I should have used a Temporary Strength Pill when I first attacked the Mount Heng Sword Sect.*

He could attack the Mount Heng Sword Sect again and force it to submit whenever he wanted.

But he could never obtain another Temporary Strength Pill.

If he had taken one back then, he might already have become the master of the Mount Heng Sword Sect.

“Well, this isn’t bad either. I’ll obtain the martial arts of both the Jin Family of Taiyuan and the Mount Heng Sword Sect.”

Jin Mukyung, who had pressed an acupoint on his shoulder to staunch the bleeding, spoke.

“Was that your goal from the beginning? I thought some mounted-bandit bastard was desperate to play at being a Great Hero of the orthodox faction.”

“A Great Hero? If I kill the Heaven Shaking Sword and the Sleeping Dragon of Shanxi today, I might at least become a demon lord. Wahaha!”

“You? A demon lord? Don’t make me laugh. And you don’t have to worry about that happening.”

“I broke all four of Cheol Mubaek’s limbs. Your way of speaking is beyond saving, so I’ll have to cut off two of yours.”

“Oh, really? This is something my younger brother says often…”

Jin Mukyung spat out a wad of phlegm.

“Go fuck yourself.”

Whoosh!

The blue-steel sword was missing so many pieces from its edge that it looked pathetic. But once blue Sword Energy coated it, it transformed into the finest sword in the world.

Shraaaaak! Shishishiiing!

Sword Energy rained down, cutting through everything around them. Horrible screams erupted from all directions, but Jin Mukyung did not stop swinging his sword.

They were merely the screams of mounted bandits who had been caught in the attack after failing to evade it. The person whose voice Jin Mukyung actually wanted to hear was easily avoiding his sword.

“As expected of the Heaven Shaking Sword. The edge of your sword is fairly sharp.”

Jin Mukyung moved with lightning speed and slashed toward Pung Yang’s waist.

Clang!

When Jin Mukyung’s Sword Energy-wreathed blade collided with Pung Yang’s curved saber, a thunderous boom rang out.

“It’s disgusting hearing that from someone who grew stronger through sorcery.”

“The important thing is that I grew stronger. How many moves do you think that supposedly incredible Tiger of Mount Heng lasted against me?”

“I don’t know.”

Whoosh!

This time, the attack came for his face. Sword strikes poured toward his arms, chest, stomach, side, and legs before suddenly shooting straight upward.

Pung Yang hurriedly pulled his head back. The blade skimmed past his cheek by the narrowest margin.

Sizzle.

But he couldn’t avoid even the sharp pressure of the wind. Blood dripped from the cheek the wind had raked.

Pung Yang retreated without a word, checked the wound, and ground his teeth.

“…You little brat.”

Despite the murderous voice, Jin Mukyung calmly opened his mouth.

“So?”

“What?”

“So how many seconds did Sir Cheol last against you?”

Pung Yang glared at Jin Mukyung for a long moment before answering.

“A hundred moves.”

“What about me?”

“Two hundred moves. I’ll finish you before then.”

“Do you have what it takes?”

“Before cutting off your limbs, I should pull out your tongue first. Listening to you has been pissing me off for a while now.”

“Be grateful you didn’t have to fight my younger brother. If he were your opponent, you’d have already plugged your ears and killed yourself. He’s an expert at making fun of people.”

“The Sleeping Dragon of Shanxi? Then I suppose I should pull his tongue out too.”

“…That actually sounds kind of appealing.”

“Enough nonsense. Raise your sword. That way, you can struggle for even a moment longer before you die.”

The moment Pung Yang’s red eyes gleamed with an eerie light, immense internal energy surged from his lowered saber.

Fwoooosh!

When internal energy was infused into a medium and given tangible form, it was called Sword Energy.

But after taking the Temporary Strength Pill, Pung Yang had now surpassed that realm.

“Sword Force…”

A Supreme Peak master.

It was the symbol of those known as Martial Gods.

Though his enlightenment was insufficient for it to be called true Sword Force, there was no doubt that he had reached the absolute pinnacle of the Peak realm.

“Well, damn.”

Jin Mukyung let out a hollow laugh.

How many years would Pung Yang have needed to reach that realm through training alone? Ten years? Twenty?

But a tiny red pill had allowed him to leap over all those years—the contemplation of martial principles, the endless training, the blood and sweat.

It had let him surpass all of it.

“What kind of son of a bitch made something like that…”

Tsssss.

Sword Energy rose from Jin Mukyung’s sword as well. Pung Yang spoke with open contempt.

“Last two hundred moves, and I’ll let you live.”

“Yeah, go fuck yourself.”

Fwoooosh!

As he watched the Sword Force plunge down as though it meant to split heaven and earth, Jin Mukyung suddenly thought that he was beginning to resemble his insolent youngest brother.

*But what is that guy doing, taking so long to get here?*

KABOOOOM!

* * *

Rumble, rumble, rumble.

The ground shook as though an earthquake had struck.

I had no idea what kind of battle was taking place thirty jang away, but I knew one thing.

*I can’t go over there.*

I wasn’t joking. If I got caught up in that fight, I felt like I would die.

I had no desire to personally experience what happened when a First Rate got its back broken between Peak masters. And more importantly…

Whoosh! Slice!

“Gueeegh.”

This side was hard enough already.

At this point, I might not be a match for a hundred men, but I had to be good for at least seventy.

I swung my weapon like a madman, drenched in the blood pouring down around me.

Shwaaak!

I caught the cavalry spear thrusting toward my side and pulled it toward me. I drove it into the stomach of the man who had been bringing his saber down behind me, then chopped the shaft with the edge of my hand.

Crack!

“Gasp!”

“Use an iron spear next time. Something heavy and sturdy. You can even do squats with it. How great is that?”

Along with the friendly advice, I slammed my fist into the mounted bandit’s jaw. His body went limp as his jawbone shattered.

Shraaaaak!

*Throat, side, leg.*

I could read the daggers thrusting toward me from three directions without even looking at them.

How could every one of them be so slow and predictable?

I was also genuinely amazed by myself. In that brief moment, I could think of a response and put it into action.

Tap. Crack!

I put my weapon into my Inventory, freeing one hand. As I simultaneously caught the wrists of the men stabbing toward my throat and side and broke them, I kicked backward with my leg fully extended.

Their short screams and the dull impact were proof that I had struck them exactly where I intended.

*More. More. More.*

My hands gradually grew faster, and the sounds around me grew more distant.

Every time I brushed against the bodies of the enemies surrounding me, weapons summoned from my Inventory appeared and vanished.

Stabbed, slashed, swung.

Broke.

How many had I brought down?

At some point, the noise that had been pushed far away came rushing back all at once.

Thud.

“Ggh…”

“Urgh.”

The dead lay motionless with their faces buried in the cold dirt. The survivors rolled around, groaning. The twenty or so mounted bandits who had escaped death and injury took several steps backward to get away from me.

“T-the Sleeping Dragon of Shanxi…”

One step. Two steps.

Terrified, they retreated as I advanced, forgetting that furious enemies were still behind them.

Shraaaaak! Thud!

“Kill them! Kill every last mounted bandit!”

“You fucking bastards!”

They were martial artists of the Mount Heng Sword Sect who had survived and fought to the bitter end.

Caught by the bloodshot-eyed men’s surprise attack, the mounted bandits fell like dominoes.

“Kyaaaagh!”

“P-please, spare me…!”

Everywhere I looked, the ground overflowed with corpses, blood, and groans.

How many mounted bandits had died here today? Two hundred? Three hundred?

I didn’t know.

What I did know was that this battle would not end until one person died.

*Pung Yang.*

It was time to deal with that cheating, pill-popping bastard.

“…”

*I can do this, right? I should be able to. Probably…*
## Chapter artifact 117

# Chapter 117

Jin Mukyung had learned countless martial arts over the years. Among them were everything from Peak-level arts that had once defined an era to Third Rate martial arts easily found even on a street stall in some backwater village.

But at this very moment, he realized something.

*It’s strong. Stronger than any martial art I’ve learned until now.*

Fwoooosh.

A curved saber descended with the force of a single slash cleaving something in two.

It wasn’t a Supreme Peak art like the Nangong Family’s Emperor Sword Form or Huashan’s Plum Blossom Sword Technique. This was the first move of the Three Calamities Sword Technique, Mount Tai Presses Down on the Crown—the move even a Third Rate street thug would know.

*Pressing down Mount Tai. I think I know what that feels like.*

The red saber qi rippling over the blade seemed capable of doing more than merely pressing down Mount Tai. It looked like it could split the mountain apart.

*I can’t block it.*

In the briefest instant, Jin Mukyung threw himself aside without hesitation.

Shraaaaak!

The saber qi grazed Jin Mukyung’s clothes by a hair before striking the ground. The sight of the earth splitting wide open without a single boom or tremor sent a shiver through him.

“You dodged that?”

But Pung Yang was dissatisfied with the result.

That had been an all-out attack. Even after drawing out 120 percent of the Temporary Strength Pill’s effects, he hadn’t managed to leave so much as a small wound on Jin Mukyung.

*The Tiger of Mount Heng could barely parry that.*

Even Cheol Mubaek, a fully mature Peak master, had suffered internal injuries and been forced to retreat in exchange for blocking it. So how had a brat not even thirty years old managed this?

“So you do live up to the name Heaven Shaking Sword?”

Jin Mukyung adjusted his stance and replied flatly.

“This much should be dodged.”

“It’s not as though you couldn’t block it, is it?”

A sneer appeared at the corner of Pung Yang’s mouth.

“Of course, a young master of the mighty Jin Family of Taiyuan would have been desperate enough to flee by rolling across the ground like a lazy donkey.”[^1]

Narye tagon. It was a phrase comparing someone to a lazy donkey rolling on the ground. To martial artists from prestigious orthodox factions who valued their dignity, it was practically the ultimate humiliation.

But not to Jin Mukyung.

“Donkey or mule, I don’t care. Does dignity put food on the table?”

“What?”

“Compared to the price of my life, it was cheap. Besides…”

The face that had remained impassive the entire time cracked into a quiet laugh.

“Why are you laughing?”

“Just thinking that if there are people who pelt Peak masters with rocks, rolling across the ground isn’t such a big deal.”

Pung Yang involuntarily asked in response to the nonsensical joke, unable to understand what he meant.

“Throwing rocks at a Peak master? Are they insane?”

“When I first heard about it, I thought the same thing. But after thinking it over, I realized he was exactly the kind of bastard who would do something like that.”

“I’d like to see the face of this lunatic.”

“You’ll see him soon.”

“What does that mean?”

That was when Pung Yang felt a faint sense of puzzlement.

Shiiiiing!

A sharp aura came from behind him.

He turned around, and the face of a handsome young man was reflected in his red eyes.

*The Sleeping Dragon of Shanxi.*

Within the slow flow of time, Jin Taekyung grinned. The iron spear in his hands was already hurtling toward Pung Yang’s chest.

KABOOM!

One Annihilation.

A vortex erupted from the spearhead and swallowed Pung Yang whole.

* * *

My condition was perfect. Leveling up while dealing with the minions had completely restored my fatigue and Stamina.

The timing was pretty good, too. Pung Yang’s broad, defenseless back looked like it was begging to be stabbed with a spear.

As the finishing touch to this beautiful picture, I chose One Annihilation. I hadn’t seen anyone remain fine after taking this attack.

But then…

“You should’ve picked your opponent more carefully before charging in.”

A low voice like the growl of a beast.

Pung Yang was surrounded by a curtain of qi as red as his eyes. It had completely blocked the vortex unleashed by One Annihilation, and now writhed like living armor.

*What did wuxia novels call something like this again?*

Oh, right. I remembered. I barely managed to move my lips.

“Body-Protecting Qi?”

“At least you’re not blind.”

“No, for fuck’s sake…”

Sword Energy and Sword Force weren’t enough, and now he had Body-Protecting Qi too?

As I stood there dumbfounded, the sight before my eyes going dark, Pung Yang curled up the corner of his mouth.

“It’s too late for regret.”

Whoosh!

A strand of saber qi shot up from his curved saber and sliced off a clump of my hair. I had bent at the waist just in time. If I had been even slightly slower, it would have been my head that was cut off.

*Fuck.*

I swallowed the curse trying to burst out and leaped away. No sooner had I done so than savage saber strikes shredded the place where I had been standing.

Shh-shh-shh-shhk!

The problem was that every strand of saber qi was unbelievably powerful. Seeing the frozen ground split apart like soft tofu sent a chill down my spine.

*If I make one wrong move, I’m really going to die.*

Even an A-rank magic armor wouldn’t have been enough here, yet I was fighting while wearing nothing but a scrap of cloth. It was like walking across a sheet of thin ice.

More than anything else…

*Doesn’t that bastard ever get tired?*

Maintaining Body-Protecting Qi alone had to consume a massive amount of internal energy, but Pung Yang seemed like a spring that would never run dry.

“I heard you two were brothers, but the way you run away like rats is exactly the same.”

That was when a voice came from behind him.

“It’s not exactly a pleasant thing to hear.”

Jin Mukyung appeared out of nowhere and scattered a flurry of sword strikes. A long blue flash shot toward Pung Yang’s neck.

Clang!

But even Jin Mukyung’s Sword Energy, which seemed capable of cutting through anything, couldn’t pierce the Body-Protecting Qi. Pung Yang leisurely rubbed the neck struck by the Sword Energy.

“It’s a little stiff. Is that all?”

“Of course not.”

Shiiiiing!

As Jin Mukyung charged in without hesitation, the curved saber in Pung Yang’s hand moved at the same time. The aura was so powerful that I could feel the flow of the air change.

This wasn’t a fight I could join.

Whoosh!

At last, the moment Jin Mukyung’s blue Sword Energy met Pung Yang’s red saber qi, a tremendous wave of force erupted along with a boom loud enough to make my ears ring.

KABOOM!

Most of the people standing firmly on both feet lost their balance and staggered.

But I widened my eyes and watched the result of this incredible clash.

*Which one?*

Through the dust swirling from the impact, I saw two people facing each other.

A sword and saber reduced to nothing but their hilts. Tightly pressed lips.

Pung Yang was the first to break the brief silence.

The man kneeling on the ground spat out dark red blood.

“Urgh—bleeeargh!”

A small cheer rose through the battlefield. Jin Mukyung stood proudly while Pung Yang knelt on the ground. The winner of this fierce battle had been decided.

*We won.*

I hadn’t been able to see the entire exchange, but there was no doubt that Pung Yang had suffered internal injuries first.

The proof was the distinct palm print stamped across his chest—something that hadn’t been there before. That must have been the decisive blow.

“Cough, cough.”

Pung Yang wiped the blood from the corner of his mouth and staggered to his feet.

“Striking the Ox Across the Mountain.[^2] Even so, I never expected my Body-Protecting Qi to break so easily… Was my enlightenment lacking?”

When Jin Mukyung gave him no answer, Pung Yang clicked his tongue.

“Damn it. Even after using the Temporary Strength Pill, I’ve ended up like this. I suppose I should hole up in some remote mountain valley and train my martial arts for a while.”

“A remote mountain valley? Training?”

I was genuinely curious.

“Where are you going?”

“Wait, and you’ll find out soon enough. I plan to take you brothers with me, too.”

This was pretty awkward.

Since we’d been invited to a housewarming, should I at least bring a box of tissues?

“Uh, us?”

“Yes. I need the martial arts formulas you know from the Jin Family of Taiyuan. They should be a great help in supplementing the violent qi circulation of the Crimson Blood Cultivation Technique.”

After hearing that much, the words that had been lingering on the tip of my tongue came out on their own.

“Are you, by any chance, a lunatic?”

I hadn’t checked, but everyone probably wore the same expression I did.

The battle had already clearly decided its winner, and yet—what?

“Forget your remote mountain valley training. I’ll send you on a filial-piety tour of Mount Beimang. You can train there.”[^3]

“Mount Beimang? You think you can send me there?”

“Even if it isn’t me personally, there are plenty of people behind you who can send you to Mount Beimang.”

I jerked my chin toward the people behind him.

The martial artists of the Mount Heng Sword Sect were already approaching slowly, weapons drawn.

The beautiful woman among them, glaring at him with especially venomous hatred, had to be the Mount Heng Sword Sect’s new Sect Leader, Lee Seowol.

*This man isn’t going to get an easy death.*

It was time for him to pay for the karma of his past misdeeds. I flicked my spear toward Pung Yang.

“Are you still going to keep spouting nonsense?”

The bastard stared at us for a moment before opening his mouth.

“Perhaps you’re under a serious misconception.”

The laugh in his voice was impossible to hide.

“Is there anyone among you capable of defeating me?”

“What the fuck does that even—”

“If you find that hard to believe, it would be faster to ask the Heaven Shaking Sword standing before me. Well, what do you think of what I’ve said?”

Jin Mukyung didn’t answer Pung Yang’s question, and only then did I realize it.

Why he hadn’t said a word for some time. Why he had done nothing but stand in place like a stone statue.

Tap.

Pung Yang’s hand touched Jin Mukyung’s chest. At what point had it happened? His body had already lost consciousness, and now it crumpled limply.

Only then did I see the five throwing knives embedded in his upper body in a neat row.

Thud.

The red eyes sweeping across the silent crowd curved like crescent moons.

“Well, shall we finish things up?”

* * *

The “finishing” began quickly.

It started with the more than ten throwing knives that shot from Pung Yang’s sleeve as he approached us at an easy pace.

Whoosh! Thunk-thunk-thunk!

It might have been a close-range attack, but it was a throwing-knife technique that even Jin Mukyung hadn’t been able to evade. Pung Yang’s knives pierced their targets with perfect accuracy, and screams rang out without fail.

“Urgh.”

“Guhk!”

The martial artists of the Mount Heng Sword Sect were already at the limit of their endurance, and their individual martial prowess wasn’t particularly high, making them easy prey.

By the time I finally stepped in front of Pung Yang, more than ten of them had already lost their lives.

“Stop.”

He shook his head.

“No, that’s not how it works. An order is a right reserved for the strong.”

“…I’ll kill you.”

“I could see it if you were the Heaven Shaking Sword, but a wet-behind-the-ears fledgling like you dares?”

I closed my mouth at Pung Yang’s sneer. He wasn’t wrong. My decision to block him had been half courage and half foolhardiness.

*But how do I take him down?*

My mind felt like it was burning itself blank. Amid all the tangled thoughts, two faces surfaced.

The first was the Head Elder. He had been the most powerful and despair-inducing opponent I had ever faced. But back then, I’d had Jin Wikyung and the martial artists of the Jin Family to help me.

*What about now?*

No one. I had no one.

After taking the Temporary Strength Pill, Pung Yang had to be a master comparable to, or even stronger than, the Head Elder. And the only person left to face him was me.

That naturally brought the second person to mind.

*Jopil, One Question, One Kill.*

Perhaps Jopil was the person who had forced me to face a genuine crisis. For the first time, I’d lost one of the subordinates I’d gained in the Murim, and I’d nearly died. Only after that had I managed to defeat the bastard.

But the Pung Yang standing before me was on an entirely different level from Jopil.

*This goddamn Temporary Strength Pill…*

The more I thought about it, the more curses came out. I wanted to see the face of whatever son of a bitch had made it.

“Once you’ve learned your place, curl up quietly.”

Watching Pung Yang act like the greatest master under heaven simply because he trusted that pill twisted my gut. If he’d only been around Jopil’s level, I might have found a way to deal with him…

*…Wait.*

A forgotten fact suddenly flashed through my mind.

There had been something nasty among the things Jopil possessed. What was it again?

*The Blazing Flame Divine Pill.*[^4]

A peerless divine elixir that granted half a jiazi of internal energy when consumed—but was also a double-edged sword that could kill its user through the fire qi contained within it.[^5]

*The Blazing Flame Divine Pill. The Blazing Flame Divine Pill…*

The next moment, I abruptly opened my mouth.

“Hey.”

Pung Yang, who had already passed me, stopped and turned around.

“Hey? Were you talking to me?”

“Yeah, you pill-popping bastard.”

“Hah. What did this little brat just say…?”

“Did you enjoy being the only one popping pills?”

“…What?”

I looked straight at his face, mottled with bewilderment and fury, and enunciated each word.

“I asked if you enjoyed taking pills all by yourself.”

An eye for an eye. Doping for doping.

Now I was going to pop a pill and fight, too.

You bastard.

[^1]: *Narye tagon* literally compares someone to a lazy donkey rolling on the ground. For martial artists from prestigious orthodox factions, it implies humiliatingly abandoning dignity to survive.

[^2]: A martial-arts term describing force that passes through one object to strike another behind it.

[^3]: Mount Beimang is traditionally associated with burial grounds and the dead; sending someone there is a euphemism for killing them.

[^4]: The name literally combines “blazing flame” with “divine pill,” emphasizing the elixir’s dangerous fire qi.

[^5]: A *jiazi* is a sixty-year cycle; half a jiazi is thirty years.
## Chapter artifact 118

# Chapter 118

“Was it fun being the only one shoving pills down your throat?”

“What?”

“I asked if it was fun shoving pills down your throat all by yourself.”

Pung Yang let out a hollow laugh.

*For a mere brat barely twenty, his speech was far too disrespectful. Had being born the youngest young master of the Jin Family of Taiyuan and being called the Sleeping Dragon made him think he could get away with anything?*

“What a brat. Heh.”

The empty laughter soon died away, and murderous eyes took its place.

“Must you see the coffin before you shed tears?”

Jin Taekyung’s eyes widened.

“Wow, hearing that line in real life makes it sound really weird. Try it again.”

“You’re a brat who can’t be reasoned with.”

As he approached at a leisurely pace, Pung Yang wondered how he could make that young brat beg for his life.

His usual method was to pull out the tongue and slowly break all four limbs. But he couldn’t treat a valuable body that knew the Jin Family of Taiyuan’s martial arts so carelessly.

A reasonable compromise was necessary.

*If I sever the meridians in his legs, he’ll quiet down.*

He had already crossed an irreversible river with the Jin Family of Taiyuan. Once this fight was over, Pung Yang planned to retreat into some remote mountain valley untouched by human feet, refine his martial arts, and then return to the Murim.

The Red Wind Band had been annihilated, but he could gather a force again whenever he wanted. The Murim was a place ruled by the strong, after all.

“Everything that happened was brought on by you, so don’t blame me.”

Pung Yang was just tightening his grip on the curved saber when—

“Ah, wait a second.”

Jin Taekyung held up a hand, then casually tossed something into his mouth.

The action was so natural that Pung Yang couldn’t help stopping.

*What is he doing?*

His question was answered a moment later.

After Jin Taekyung’s body shuddered once, tremendous heat began to rise from every inch of him.

* * *

I had only one option left.

To make one last gamble with the Blazing Flame Divine Pill.

It was a dangerous choice, but it was a hundred times better than dying after being forced to spit out the Jin Family’s martial arts formulas for Pung Yang.

Gulp.

True to its name, the divine elixir melted the moment it touched my tongue and slid down my throat. The problem began after that.

*Ding.*

> **System**
> - You have taken the **Blazing Flame Divine Pill**.
> - **Circulate your qi** to control your energy.

It was hot. The thirty years of internal energy contained within the Blazing Flame Divine Pill spread through every part of my body like wildfire.

> **System**
> - You have temporarily gained the **Scorching Yang Qi** attribute.
> - Your **internal energy** has temporarily increased to 45 years.
> - If you cannot control your energy, you may die!
> - Quest, **Divine Pill Absorption**, has been created.

I had no time to check the System notifications that continued ringing in my ears. Controlling the Blazing Flame Divine Pill’s energy rampaging through my body was already more than enough.

“Hoo. Hooooo.”

I felt like a human pressure cooker. It was as though a real fire had broken out inside me, and wisps of smoke rose from my entire body.

The snow covering the ground beneath my feet melted, and the damp earth softened until it flowed like water.

*I expected something this bad, but this is…*

It was far beyond my imagination. I couldn’t even scream. I could only tremble as Pung Yang’s voice pierced my ears.

“What have you done?”

Seeing the bewilderment on his face actually made the heat subside a little.

I forced the corners of my mouth upward and answered.

“What else? I’m going all in.”

“You brat!”

Had he sensed something ominous in my answer? Pung Yang’s curved saber flew toward me at a blinding speed. A red strand of saber qi extended from the blade and aimed for my chest.

*Swish!*

Death passed me by at a distance of exactly half a step. The curved saber missed its target and drew another chaotic arc.

*Shh-shh-shh-shhk!*

But once again, the blade only cut through empty air. Pung Yang’s face twisted as he stared at me, already backed away.

“You…!”

“What, asshole?”

I answered as casually as I could, but the person most surprised was me. When we had crossed hands earlier, I hadn’t been able to dodge so easily.

This was on an entirely different level from before, when Pung Yang’s overwhelming aura and saber qi had forced me to do nothing but evade.

*Since when has my body felt this light?*

The instant I thought I needed to avoid an attack, my body moved faster than ever before. And that wasn’t the only thing that had changed.

*I can see everything clearly.*

I could see and read each of Pung Yang’s movements. If I could see the attacks, there was no reason I couldn’t evade them. I felt like I could dodge even saber force, not just saber qi.

At last, I understood why.

*It’s because of my internal energy.*

My original fifteen years of internal energy had merged with the thirty years from the Blazing Flame Divine Pill. I couldn’t control it perfectly, but that didn’t mean the power of thirty years of internal energy had simply disappeared.

Like an overinflated balloon, the Blazing Flame Divine Pill’s energy filled my entire body.

*The problem is that I have no idea when this balloon will burst.*

So I had to take down Pung Yang before that happened.

Feeling the heat bubbling up inside me, I adjusted my grip on the iron spear.

“Come at me.”

Pung Yang bit his lip.

“Young brat, you’re already getting cocky. Someone like you is nowhere near strong enough.”

“You look pretty tense for someone saying that.”

“A wild beast gives its all even when catching a rabbit.”

“But a wild beast doesn’t take a Temporary Strength Pill to catch a rabbit.”

“...!”

Shock flashed across Pung Yang’s face. He stared at me with his mouth hanging open, then stammered.

“Y-You mean the Temporary Strength Pill?”

“Yeah. The Temporary Strength Pill.”

“How do you know that name?”

“Corporate secret, asshole.”

“Did you take one too?”

“Well, I did eat something similar.”

I wondered whether he would recognize the name if I called it the Blazing Flame Divine Pill.

Compared to the Temporary Strength Pill, its stability was complete garbage. I intended to find out exactly how powerful its effects were starting now.

“You’re fucking dead.”

With those final words, I kicked off the ground.

*Shweeeeeek!*

* * *

Pung Yang was deeply troubled.

*How does that brat know about the Temporary Strength Pill?*

The existence of the Temporary Strength Pill was a secret he had to take to his grave.

It was a hidden trump card that might save his life someday. But if its existence became known, it would be a wondrous object capable of bringing a bloodbath to the entire world.

Just the fact that it could draw out two or three times the power of the person who took it would be enough to make martial artists throughout the land salivate and come running.

But there was an even greater problem.

*It’s a legacy of demonic, heterodox arts.*

After the Great Faction War, the Murim had fallen into the hands of the orthodox factions.

If even a rumor spread that Pung Yang had inherited the legacy of demonic, heterodox arts, it wouldn’t be only the Jin Family of Taiyuan pursuing him. The entire Murim would come after him.

*Jin Taekyung, the Sleeping Dragon of Shanxi… I must kill him and eliminate the trouble he’ll cause later.*

Pung Yang gritted his teeth and unleashed his martial arts.

After only a few years of training, he had already mastered seventy percent of the Crimson Blood Twelve Sabers. That was more than enough to kill a brat hopelessly beneath him in both age and martial arts.

“Die!”

*Shiiing!*

The Crimson Blood Twelve Sabers was a domineering martial art. Red saber qi shot from the curved saber and slashed wildly in every direction. The fierce momentum split open the surface of the earth and burst the air apart.

Yet the target he needed to cut was no longer there.

Jin Taekyung dodged the attack by exactly half a step and thrust his spear.

*Shweeeeeek!*

The spearhead drove toward Pung Yang’s throat. Pung Yang hastily twisted his head aside to evade it, and a chill settled in his chest.

*Fast.*

Fast and accurate. He had yet to reach the stage where Sword Energy could injure a person—the hallmark of a Peak master—but his movements had already caught up to Pung Yang’s.

*Could this brat have taken the Temporary Strength Pill too? No. It’s completely different from mine.*

Pung Yang had already taken the Temporary Strength Pill several times.

From Jin Taekyung’s body, which had turned bright red with heat, Pung Yang could tell that what he had swallowed earlier was not the Temporary Strength Pill.

*Then what did he… Wait!*

Pung Yang couldn’t continue thinking. Jin Taekyung had finally seized the initiative and begun to unleash the Jin Family’s Spear Technique in earnest.

*Shh-shh-shh-shh-shhk!*

Dozens of spear shadows poured down like a rain shower. It was a suffocating sight.

No, it wasn’t just an illusion. It really was suffocating.

A bead of sweat rolled down Pung Yang’s forehead.

*This is…*

Scorching Yang Qi.

And not just any Scorching Yang Qi—it was powerful enough to affect even Pung Yang, a Peak master himself. The Tiger of Mount Heng, Cheol Mubaek, had also possessed Scorching Yang Qi, but it couldn’t compare to what Jin Taekyung was emitting now.

*He ate a divine elixir—a Scorching Yang-type divine elixir!*

*Whooooom!*

Recognizing it changed nothing. The heat was dizzying, and the attacks were sharp. Pung Yang bit down hard on his lip as he repeatedly retreated, barely managing to evade the spearhead.

*Against a brat this young!*

He had lived his entire life fiercely. Now, even after taking the Temporary Strength Pill, he felt humiliated to be driven back by a young brat who had only just begun making a name for himself.

That anger flowed straight into his curved saber. The saber qi rising over the blade burned redder than ever.

*Hiss!*

The Jin Family’s Spear Technique and the Crimson Blood Twelve Sabers differed in their weapons and forms, but they shared one thing in common: both were domineering martial arts.

In the blink of an eye, Jin Mukyung’s iron spear and Pung Yang’s curved saber finally parted after more than ten fierce exchanges.

“Hmm.”

Jin Taekyung was the first to retreat. Blood flowed from his torn palm, and the heavy, sturdy iron spear had been cut by the sharp saber qi until less than half of it remained.

“You fool.”

Pung Yang smiled triumphantly. A martial artist losing their weapon meant defeat.

Even the Tiger of Mount Heng, Cheol Mubaek, who had built his reputation entirely with his fists and feet, had knelt before Pung Yang. Jin Taekyung hadn’t even crossed the wall into the Peak realm yet. The moment he lost his weapon, he was as good as dead.

“Did you think you could defeat me in a head-on fight?”

Jin Taekyung rubbed the blood from his palm and answered.

“No. But I did learn some valuable information.”

“...Valuable information?”

“Yeah. I learned your attack pattern.”

“Pat—what?”

“Your attack pattern is strong, strong, strong, strong, strong.”

*What kind of bullshit is this?*

Pung Yang understood that the brat was talking about his martial arts, but he had never heard of this “pattern-whatever” before. And what did he mean by strong, strong, strong, strong, strong?

Pung Yang glared at Jin Taekyung with murderous eyes.

“I’ll sever the meridians in all four of your limbs as payment for talking nonsense.”

Jin Taekyung opened his mouth with a bored expression.

“You really like cutting off and pulling out people’s limbs. Are you a limb fetishist?”

“You little brat…”

“You old bastard…”

Pung Yang drew a deep breath. He was a Peak master who had spent his entire life possessing a cool, rational mind. But he couldn’t stop his voice from breaking into pieces with anger.

“You. Will. Die. By. My. Hand.”

“I. Sometimes. Cut off limbs. Sometimes, I don’t like this version of myself.”

He felt his patience snap. He could swear that he had never been this furious in nearly ten years.

“Graaaargh!”

Pung Yang charged like a madman, emitting a howl that could have been either a scream or a roar.

Without using a single form or martial art, he brought the curved saber down over the crown of Jin Taekyung’s head with all his strength.

“Die!”

That was when Jin Taekyung’s calm expression was reflected in Pung Yang’s bloodshot eyes gleaming with killing intent.

In an instant, his mind snapped clear as though someone had dumped cold water over him.

*Something’s wrong.*

Pung Yang drew up his internal energy with all his might.

As his Body-Protecting Qi rose, a dagger flashed in Jin Taekyung’s previously empty hand.

*Shnk!*
## Chapter artifact 119

# Chapter 119

*Thud!*

A tingling tremor ran through my fingertips. It was a familiar sensation, one I had felt thousands, tens of thousands of times before.

*It went in.*

At the same time as that certainty struck me, I twisted the dagger buried in Pung Yang’s side. A scream burst from his mouth.

“Graaaargh!”

The dagger itself must have caused excruciating pain, but that blow had also inflicted a serious internal injury. The Body-Protecting Qi that had failed to fully form before scattering like smoke was proof enough.

*That was close.*

Pung Yang’s instincts were extraordinary. If the dagger hadn’t pierced him in that fleeting moment, just before his Body-Protecting Qi was completed, I would have been the one in trouble.

“Guh!”

Pung Yang spat out dark blood and reached out with one arm. In that instant, a flash of light burst from inside his pitch-black sleeve.

*Shweeeeeek!*

I instinctively took a step back and tilted my head. A dagger shot from Pung Yang’s sleeve and narrowly grazed the bridge of my nose.

*That was dangerous.*

If I hadn’t stepped back, it would have struck my throat instead of my nose.

I was only able to evade it because I had seen Pung Yang use throwing knives earlier. I stuck out my tongue and licked up the blood running down the bridge of my nose.

“Thanks. I was thirsty anyway.”

“You little rat bastard…!”

Pung Yang widened the distance between us and ground his teeth.

“Was this what you were aiming for from the beginning?”

“Yeah. Does it hurt?”

“Wait. I’ll pay you back a hundredfold.”

“There’s no need to go that far between friends. You don’t have to pay me back.”

“Grrrrrgh!”

Teasing him was surprisingly satisfying. It would be nice if he died of rage, but there was no chance of that happening.

*It was a good opportunity.*

I had succeeded in drawing Pung Yang in by taunting him, but I had failed to finish him off completely. Even after taking the Blazing Flame Divine Pill, the gap between Pung Yang and me was still enormous.

And more importantly—

*This is getting difficult.*

My entire body was hot as a furnace. The thirty years of Scorching Yang Qi that I hadn’t been able to control from the beginning was now running wild of its own accord.

It would have been touch and go even if I’d tried to suppress it with my existing internal energy, but I’d fought Pung Yang at close quarters with the reins completely off, and my condition was steadily worsening.

*Damn it. I wish this had been a Temporary Strength Pill instead of the Blazing Flame Divine Pill.*

The Blazing Flame Divine Pill and the Temporary Strength Pill had been created for entirely different purposes.

Was the Temporary Strength Pill a stimulant that temporarily awakened latent power and raised it to its limit? To put it simply, the difference was like that between traditional herbal medicine and a stimulant.

*Does that bastard not have any side effects? He’s annoyingly full of energy.*

I was looking at Pung Yang with a trace of envy when—

“Cough.”

Oh? What was this?

For an instant, the whites of Pung Yang’s eyes showed through during his short cough.

His eyes had been completely blood-red the entire time. No matter how I thought about it, there could only be one reason for this change.

*The Temporary Strength Pill is losing its effect.*

* * *

Pung Yang was flustered. He immediately recognized the abnormal signs appearing in his body.

*Already?*

The Temporary Strength Pill’s effect lasted a little over one shichen. Yet now, after barely half a shichen had passed, the power that had been surging through his entire body was gradually fading.

Fatigue he hadn’t felt before pressed heavily down on his shoulders, and pain that had seemed distant began to prick at his nerves.

“Cough.”

On top of that, he had suffered a considerable internal injury.

Pung Yang bit his lip as dark-red blood came out with his cough.

*I’ve expended too much strength.*

The Temporary Strength Pill was a wondrous object that could draw out twice, or even more than twice, the strength a person possessed—but it demanded an equal price.

In exchange for temporarily granting tremendous power, it weakened the body’s physical abilities. If the user’s body could not support it, the effect would disappear.

*Taking the Temporary Strength Pills one after another was the problem.*

First the Tiger of Mount Heng, Cheol Mubaek, and then the young brats from the Jin Family of Taiyuan. If he hadn’t taken the pills, he would have died long ago, but Pung Yang knew the price he would have to pay and feared the aftermath.

*At this rate, the Temporary Strength Pill’s effect will last only one meal’s time longer at most…*

He had to settle the battle within that time.

He must not use the last Temporary Strength Pill. Taking three in succession could put his life at risk.

“One meal’s time…”

Pung Yang muttered under his breath and glared at the remaining prey.

“That’s more than enough.”

The whites of his eyes disappeared again, filled once more with blood-red light.

* * *

Had I been mistaken?

When Pung Yang raised his head again, his eyes were red, and an overwhelming aura poured from his entire body.

“I’ll kill you with a single stroke.”

I watched his curved saber and opened my mouth.

“I thought you needed the martial arts formulas.”

“It doesn’t have to be you. Why do you think I went to the trouble of keeping Jin Mukyung alive?”

“Because you love him.”

“I swear by the gods of heaven and earth… I will cut out your tongue.”

The next moment, Pung Yang raised his curved saber.

*Shweeeeeek! Clang!*

Pung Yang caught an iron arrow flying toward him with tremendous force and frowned.

“There are plenty of bastards who want to die. Or is it a bitch this time?”

The owner of the arrow slowly walked over and stood beside me. Her footsteps were light as down, and her height barely reached my shoulder. Even in this desperate situation, her beauty was enough to steal my gaze for an instant.

The Sect Leader of the Mount Heng Sword Sect, Lee Seowol, whispered to me in a low voice.

“We’ll buy you some time.”

*We* meant the surviving martial artists of the Mount Heng Sword Sect, including Lee Seowol. There were only ten of them. As befitted those who had survived until the end of such a brutal battle, every one of them was a First Rate master, but against Pung Yang, the outcome was obvious.

*They’ll all be wiped out.*

How much time could they buy even if they stepped forward? They were more likely to get in my way. It was coldhearted, but that was reality.

I shook my head.

“That won’t change anything.”

“We’re not saying we’ll fight alongside you.”

“Then?”

“Take your brother and run.”

The distance between Pung Yang and us was only a little over ten zhang—about thirty meters. No matter how quietly she spoke, there was no way a Peak master like him hadn’t heard her.

“What, run? Hahahaha!”

Despite Pung Yang’s booming laughter, Lee Seowol continued speaking without flinching.

“It may only be for a fleeting moment, but we’ll buy you time. Run as far away as you can.”

I turned my gaze toward the fortress gate. It was about one hundred zhang—three hundred meters—from here. Wolhwa, Hyuk Mujin, and the horses waiting to carry us were not far beyond it.

*It’s worth trying.*

I was already suffering internal injuries from the Blazing Flame Divine Pill, but I could still endure them to some extent. If I squeezed out every last bit of strength I had, I might be able to escape even while carrying Jin Mukyung on my back.

But…

*They’ll die.*

Every last one of them. Not a single exception.

Lee Seowol herself was included in the *we* she had mentioned. She had stepped forward prepared to die as well.

*Why?*

The Mount Heng Sword Sect and the Jin Family of Taiyuan were bitter enemies. Even if they had been manipulated by the Head Elder’s schemes, they had killed one another, and both sides had shed a great deal of blood.

And yet Lee Seowol was trying to save me.

She was willing to sacrifice her own life—and the lives of her subordinates—to do it.

“You don’t need to look at us like that. I reached this conclusion after careful consideration. In return, may I ask you for one thing?”

I asked her,

“What is it?”

“Aveng​e us in our place.”

Lee Seowol stared at Pung Yang with icy eyes.

“Kill that man. As cruelly as possible.”

Ten people were throwing away their lives for one person’s death.

I could feel the hatred Lee Seowol held in every word she spoke. Just as I was rendered speechless, Pung Yang, who had been watching us with a mocking smile, opened his mouth.

“That’s a bold idea, but it won’t happen. You’ll all bury your bones here.”

One of the Mount Heng martial artists shouted.

“Shut up, you vicious bastard!”

*Thwack!*

The next moment, the martial artist’s head jerked back. The iron arrow Pung Yang had been holding was embedded in his forehead.

“Senior Brother!”

As the belated scream rang out, Pung Yang smiled.

“I was just about out of throwing knives, too… Thank you, Sect Leader.”

Lee Seowol bit her lip.

“Go! Hurry!”

I took a deep breath. I had already drawn out every step in my mind.

Jin Mukyung had fallen only about twenty zhang—sixty meters—from here. If I drew out as much internal energy as possible, ran while carrying him on my back, and endured the internal injuries, I could reach the fortress gate quickly.

Pung Yang would probably catch up to me by then, but if these people bought me just a little more time, I could survive.

*I can go back.*

I could return to the Jin Family of Taiyuan, where Jin Wikyung was, and to the home where my mother and Hayeon were waiting. If I lived to fight another day, I was confident I could return much stronger—strong enough to make Pung Yang seem insignificant by comparison.

*That’s enough.*

After taking another deep breath, I turned toward Lee Seowol.

“I’ll avenge you. I swear.”

For the briefest instant, did Lee Seowol smile?

It was so fleeting that I might have imagined it. When I looked again, only firm resolve remained on her face.

“Go. Hurry.”

Her words were the starting signal. The Mount Heng martial artists charged with furious shouts, Lee Seowol at the front.

*Yes. I have to go.*

I drew up every last bit of internal energy in my body. Sharp pain tore through me as the internal injuries left by the Scorching Yang Qi sent dark-red blood flowing from my nose, but I endured it.

It only had to last a moment. A very brief moment.

*Inventory open, equip spear.*

The cool shaft of the spear settled into my grip.

Then I pushed off once.

*Boom.*

I shot forward like an arrow—no, faster than an arrow.

Not toward Jin Mukyung, but toward Pung Yang. I could see his broad smile.

“That’s more like it!”

“Shut up, you son of a bitch.”

“Ha-ha-ha-ha!”

Pung Yang’s curved saber was larger than ever before. Brimming with red saber qi, it swung toward me.

*Whoooosh!*

The wind exploded, and even the air seemed to vanish.

I gripped the iron spear until it felt as though it might crumble in my hands.

*Please. Just this once.*

I poured all fifteen years of my internal energy into the spear. Drawing back my shoulder and waist as far as I could, I sent everything I had flying forward.

*One Annihilation.*

*Rumble-rumble-rumble!*

A gigantic mass of saber qi collided with the vortex.

A thunderous roar filled the world, as though the sky itself were splitting apart. Through the raging wind, I saw it clearly.

*Kaboom!*

The white vortex shattered into pieces before the red saber qi. The massive concentration of qi completely pulverized One Annihilation.

Pung Yang whispered with an ecstatic expression,

“This is as far as you go.”

The next moment, Pung Yang’s internal energy surged along the spear and hammered into me.

*Boom!*

Blinding pain and ringing ears rolled over me like waves.

*Ding.*

> **System**
> - You have suffered **Internal Injury**! Your condition is extremely serious!
> - **Scorching Yang Qi** is running wild!
> - You have suffered a **Severe Injury**! All stats have dropped significantly!

System notifications rang out one after another, mixed with the shouts of the Mount Heng martial artists, Lee Seowol’s scream, and Pung Yang’s laughter.

*It’s over.*

The instant my legs gave out despite my will, a powerful hand clamped around my throat.

“Guh. Guhh.”

“That was fairly impressive. If I’d been only a moment slower, you might have won.”

Pung Yang bared his teeth in a grin. The red light in his eyes was slowly fading.

*Damn it. I was so damn close.*

I wanted to say it aloud, but my mouth was full of blood, making even that difficult.

“I swore by the gods of heaven and earth, didn’t I? I swore I’d pull out your tongue.”

Had he said that? By now, even who I was had become hazy.

Pung Yang pried open my mouth with his other hand. I felt his rough fingers tugging on my blood-soaked tongue.

“Ghh…”

“When you were flapping that mouth, didn’t you know this would happen? Huh?”

“Ghaa… hahahaa.”

“Hahaha! What the hell are you mumbling? Shall I let you leave some last words?”

Pung Yang laughed heartily and released my tongue. Only then could I speak. I swallowed the blood in my mouth and said,

“Salty.”

“What?”

“It’s insanely salty.”

“What kind of bullshit is that?”

*What do you think?*

*I’m saying the taste of your fingers brought me back to my senses a little.*

I muttered through my fading consciousness.

*Inventory open, summon anything.*

*Ding.*

> **System**
> - No item named **Anything** can be found. The oldest item stored in your inventory will be summoned first.
> - The **Unnamed Sword** has been summoned.

*The Unnamed Sword? What was that again?*

*Whatever.*

I gathered up the last of my strength and thrust the sword in my hand toward Pung Yang’s chest, which was shrouded in Body-Protecting Qi.

It was a futile last-ditch attack with an obvious conclusion.

*Damn Body-Protecting Qi.*

But this was enough. I had no regrets left.

It was at that moment, as my head slowly drooped—

*Thud!*

*Ding.*

> **System**
> - The **Unnamed Sword** satisfies a specific condition.
> - **Ten-Thousand-Year Cold Iron** has destroyed **Body-Protecting Qi**.

…Huh?

# Checkpoint Review — 455–459

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

# Chapters 455–459

## Plot

Taekyung interrogates the captured Three Fiends at the Zhuge Clan but learns only that the former-generation great fiend and his brothers followed the Demon Lord’s orders and supposedly know nothing about Dark Heaven’s headquarters or wider operations. He keeps the prisoner alive for transport to Henan. Beggars’ Sect intelligence fails to locate the Hubei attackers, but Lower District Sect records place the missing Dongting Fisherman somewhere in the province.

Taekyung and Zhuge Gyun suspect the destruction of the Sea Serpent Society and three Yangtze River Channel League strongholds was a diversion for a larger attack on a sacred treasure or major orthodox power. Zhuge Gyun coordinates the Zhuge Clan’s intelligence with the Beggars’ Sect and Lower District Sect, while Taekyung warns Wudang and Donghu Stronghold. Taekyung then leaves for Dongting Lake with Cheongpung, Hyuk Mujin, Gung Gibang, and the chained Three Fiends.

Upon reaching Wuhan, Taekyung’s party finds Dongting Lake engulfed in flames and littered with wreckage and corpses. The unavoidable Peak-grade Quest *The Tragedy of Dongting Lake* requires him to rescue survivors before time expires. He uses destroyed ferries and his Inventory to cross the lake, eventually rescuing Honglan and Ju Wongong. They are the only survivors found, and Taekyung earns the Water Rescue Worker Title. Grieving with the mourners, he vows revenge against those responsible.

After regaining consciousness, Honglan confirms that a single unseen water-arts master sank the escort ships and pleasure boat with Force before escaping across the lake. His ability to match the Seafaring King identifies him as the Dongting Fisherman, a previous-generation Supreme Peak master with hidden refuges throughout Dongting Lake. Taekyung concludes that the Dongting Fisherman is Dark Heaven’s operative and prepares to search the refuges with Honglan.

## Continuity

- The unavoidable Peak-grade Quest *The Tragedy of Dongting Lake* is complete; Taekyung rescued two people and earned the Water Rescue Worker Title.
- Honglan is the sole surviving eyewitness to the Dongting Lake attack. She is a First Rate martial artist and knows several possible locations of the Dongting Fisherman’s hidden refuges.
- Ju Wongong also survived and remains unconscious under heavy guard after passing the most dangerous stage of his injuries.
- The Dongting Fisherman is a previous-generation Supreme Peak water-arts master comparable to the Seafaring King, remains in Hubei Province, and is suspected of being Dark Heaven’s tail and the perpetrator of the lake attack.
- Taekyung is transporting the captured Three Fiends alive, with his acupoints sealed, to investigate possible Dark Heaven codes or markings.
- Zhuge Clan, Beggars’ Sect, and Lower District Sect intelligence networks are searching for the perpetrators of the Hubei massacres.
- Taekyung suspects the Hubei massacres were a diversion for a larger Dark Heaven operation. The shared symbols between the Arch Lich’s magic circle and Dark Heaven’s formations, the other attackers’ identities, and the Wudang killer demon’s connection to Dark Heaven remain unresolved.
- Jin Wikyung is cooperating with Taekyung’s investigation as an inspector for the new Murim Alliance. The Skeleton King’s undead identity remains concealed, and Go Jun is searching for Lee Jungryong’s holographic recorder.

## Translation Decisions

- Use “Dongting Lake,” “Dongting Fisherman,” “Water Rescue Worker,” “Wuling Peach Blossom Spring,” “Yiyang Tower,” “water arts,” and “Force.”
- Render 삼괴 as “Three Fiends,” 대마두 as “great fiend,” 마군 as “Demon Lord,” 살귀 as “killer demon,” and 일급 낭인 as “First Rate wandering martial artist.”
- Preserve “Hwang Cheol,” “Do Ripgun,” “Mad Water Saber Demon,” “Wave Fox,” “Sichuan Blood Tragedy,” “Ju Wongong,” and “Honglan.”
- Retain “sibu-leol,” “Lord Fuck,” and “Lord Sibu-leol,” along with Taekyung’s dry profane humor, Cheongpung’s deferential Benefactor address, Honglan’s humble formal voice, and the Skeleton King’s grandiose voice.
- Preserve established renderings including “Daejuksan Escort Bureau,” “Hyungmun Sword Family,” “Eungseong Merchant Association,” “Celestial Dragon,” “four-person sedan chair,” “singing courtesan,” and “the nine branches of kin.”

## Durable state

{
  "active_continuity": [
    "Taekyung completed the unavoidable Peak-grade Quest The Tragedy of Dongting Lake, rescued two people who were the only survivors found, and earned the Water Rescue Worker Title.",
    "Honglan survived the Dongting Lake disaster and regained consciousness; Ju Wongong also survived but remains unconscious under guard after passing the most dangerous stage of his injuries.",
    "Jin Wikyung is acting as an inspector for the new Murim Alliance and is cooperating with Taekyung's investigation.",
    "The shared symbols between the Arch Lich's magic circle and Dark Heaven's formations remain unexplained.",
    "The Sea Serpent Society and three Yangtze River Channel League strongholds, including Donghu Stronghold, were destroyed, with more than a thousand casualties, while the perpetrators' wider plans remain unknown.",
    "The Dongting Fisherman is a previous-generation Supreme Peak water-arts master comparable to the Seafaring King, remains in Hubei Province, and is suspected of being Dark Heaven's operative and the perpetrator of the Dongting Lake attack.",
    "Wudang is responding to an unidentified killer demon responsible for more than thirty deaths, including twenty pilgrims on Mount Wudang.",
    "The Skeleton King's undead identity remains concealed, and Taekyung has ordered him to join Peace Guild under a prepared contract.",
    "Go Jun is expected to succeed Lee Jungryong as Ares Guild's captain and is searching China for Lee's holographic recorder.",
    "The captured Three Fiends is a former-generation great fiend and Supreme Peak Dark Heaven subordinate whom Taekyung is transporting alive to investigate possible codes or markings.",
    "Qingxia Hall is an influential Hubei social club formed by powerful families' children, and Ju Wongong is its exiled young master who defers to Prince Shangshan while Honglan conceals her real name.",
    "Beggars' Sect, Lower District Sect, and Zhuge Clan intelligence are searching for the people responsible for the Hubei massacres."
  ],
  "continuity_sources": [
    459,
    458
  ],
  "open_questions": [
    "What are the origin and purpose of the symbols shared by the Arch Lich's magic circle and Dark Heaven's formations?",
    "Who destroyed Donghu Stronghold and the related Yangtze River Channel League strongholds, why was no Moving Formation trace left, and was the destruction a diversion?",
    "What is the Dongting Fisherman's exact role in Dark Heaven and the Hubei atrocities, and what do his hidden refuges contain?",
    "Is the killer demon attacking Wudang connected to Dark Heaven?",
    "What evidence is contained in Lee Jungryong's holographic recorder, and what are the terms of the Peace Guild–Wizard Guild agreement?"
  ],
  "safe_through": 459,
  "temporary_decisions": [
    "Render 익양루 as Yiyang Tower.",
    "Render 황철 as Hwang Cheol, 도립군 as Do Ripgun, 광수도귀 as Mad Water Saber Demon, 파랑호 as Wave Fox, 동정호 as Dongting Lake, and 사천혈사 as Sichuan Blood Tragedy.",
    "Render 살귀 as killer demon, 일급 낭인 as First Rate wandering martial artist, 삼괴 as Three Fiends, 대마두 as great fiend, and 마군 as Demon Lord.",
    "Render 시부럴 as “sibu-leol,” 시벌좌 as “Lord Fuck,” and 시부럴좌 as “Lord Sibu-leol.”",
    "Preserve the Skeleton King's grandiose, mock-offended voice and Taekyung's dry, profane humor; render 주원공 as Ju Wongong, 대죽산표국 as Daejuksan Escort Bureau, 형문검가 as Hyungmun Sword Family, 응성상회 as Eungseong Merchant Association, 천룡인 as Celestial Dragon, 사인교 as four-person sedan chair, 홍란 as Honglan, 가기 as singing courtesan, 구족 as the nine branches of kin, 수상 구조대원 as Water Rescue Worker, and 수공 as water arts."
  ],
  "version": 1
}

## Reading copies

## Chapter artifact 455

# Chapter 455

“Cough, cough.”

Hunched over like a shrimp, the old man coughed with difficulty.

Whenever he moved, the cold rising from the prison’s stone floor seeped into his bones.

Yet no illness could ever take root in the old man’s body.

The several jiazi[^1] of internal energy accumulated in his dantian over the years no longer obeyed their master’s control, but they were more than enough to protect his aged body.

And that fact only made the old man angrier.

*Damn it…!*

The ugly old man’s features twisted like those of an evil spirit.

He had once crossed the continent and unleashed countless storms of blood. Now, he was being treated like livestock that could be slaughtered at any moment.

“Then kill me! If you’re going to subject me to this humiliation, just kill me already!”

As the old man writhed and let out a tearing scream, the chains binding his body tightly grated against one another.

Yet just like the internal energy sealed within his dantian, the dozen or so iron balls connected to the chains did not move an inch.

“You bastaaaardsss!”

Although his martial arts had been sealed and he could no longer display the same martial might as before, his innate viciousness remained unchanged.

The old man glared through the thick iron bars with bloodshot eyes. Faces that must have been laughing at him somewhere flashed before his eyes like hallucinations.

“You bastards…!”

A grudge etched into his bones and soul.

They had taken the lives of his two brothers, who had been born on the same day and hour and spent their entire lives together. The old man himself had been captured and forced to endure every kind of humiliation.

They had even crushed his testicles as though castrating livestock. Calling them enemies who could never coexist was not enough to describe it.

“Fine, then. I’ll survive somehow.”

Flames poured from the old man’s eyes.

“I’ll escape this place no matter what, then tear you bastards to pieces and kill you while you’re still alive!”

It was at that exact moment that his shout, brimming with killing intent, rang through the underground prison.

“I heard your escape pledge. Quite moving.”

“……!”

When had he—

The old man blinked. One of the faces that had flashed before his eyes moments ago was now staring at him from beyond the prison bars.

A chill ran through one corner of his chest at the smile hanging from the young man’s lips.

“You—you’re…”

“How’s the busted part? Must hurt every time you take a piss.”

The old man almost nodded without realizing it.

But the young man was one of the names written side by side at the very top of his kill list. He was someone the old man had to kill by any means necessary.

The old man glared at the young man through the bars with gleaming eyes.

“If you’re curious, lift the seal on my martial arts right now. I’ll show you myself.”

“I’m not particularly curious about that…”

The smile on the young man’s lips—Jin Taekyung’s lips—vanished as if wiped away.

“You’ll have to tell me everything else you know, Three Fiends.”

* * *

In the modern world, torturing prisoners was classified as an illegal act. If such a fact became known, even a Great Nation would be condemned by the international community.

But this was the Murim. The authority of the law was vague, and the boundary between people and beasts was blurred.

And in my eyes, the Three Fiends were closer to beasts wearing human faces.

*There’s no reason to hesitate.*

He had harmed countless people over the course of many years.

He was a fiend who had taken hundreds, even thousands, of lives simply to satisfy his own killing urge.

There was no room for shallow morality in the bloody path he had walked or in this damp, dark underground prison.

I stared at the Three Fiends with cold eyes.

“Guhk, hnggg…”

His body hung limply, bound to an iron chair.

Bloodstained saliva dripped from his open mouth, and his limbs, torn and broken all over, spasmed with pain.

“How is he?”

At my question, the old man who had been closely examining the Three Fiends beside him scratched his head with a bloodstained iron skewer.

“He’s already reached his limit. At this point, we must assume he has confessed everything he knows.”

If torture skill were divided into realm stages, I was barely First Rate. The old man before me was a Supreme Peak master.

He had handled prisoners so effectively and cruelly that Zhuge Gonghu, the Fan-Wisdom King, had taken notice of his torture techniques during the Great Faction War and invited him to the Zhuge Clan after the war ended.

“If we continue torturing him…”

“He will certainly die. And this old man’s opinion is that beating him any further will not produce anything else.”

The old man’s voice was full of certainty.

The appearance of the Three Fiends, who had become half a corpse, and his aura, which seemed ready to go out at any moment, lent even greater weight to those words.

But it was not enough. I stared at the Three Fiends, who was trembling as though half his soul had already left his body.

*Is this really everything?*

It was not as though the Three Fiends had known nothing.

He had held out through sheer spite for the first few shichen,[^2] but once the torture reached its final stages, he had talked enough to fill five bamboo slips with closely packed writing.

Yet most of it was useless or concerned events from the past, and the information I needed most had never come out.

*The series of incidents happening in Hubei Province right now.*

The Sea Serpent Society had fallen, and Donghu Stronghold had been massacred.

The casualties had already far exceeded a thousand, including innocent commoners who did not know even a single martial move or half a stance.

As far as I knew, there was only one group with the ruthlessness and power to commit such madness.

*Dark Heaven.*

The problem was that I could not get hold of their trail.

Where and how had they attacked the Sea Serpent Society and Donghu Stronghold? Where had they hidden the Moving Formation?

And finally, where were the people who had committed this atrocity now, and what were they doing?

“This won’t do.”

With a quiet mutter, I seized the unconscious Three Fiends by the wrist. The old man, who had been standing there with a bored expression, hurriedly tried to stop me.

“Great Hero. If you do that—!”

“It’s fine. I’m not trying to kill him.”

I sent internal energy through the Three Fiends’ wrist. As the warm heat of Scorching Yang Qi seeped along his acupoints, color returned to the man’s pale cheeks and his eyelids lifted.

My face was reflected in his gray eyes, which trembled without being able to focus.

“You—you’re…”

“You need to wake up. It’s still too soon.”

“J-just kill me.”

“If you tell me everything you know, you can have what you want. But if you keep pretending to be a loyal subject…”

I increased the strength of the internal energy I had been sending through him. The Three Fiends’ eyes flew open with a sharp gasp.

His body was already ruined inside and out. It could not withstand the heat of Scorching Yang Qi.

“Ghk, gack.”

His painful, gasping breaths carried the smell of meat being cooked. But I continued staring at the Three Fiends without wavering.

“That’s not the answer I want.”

“This old man—I’ve already told you everything.”

“Not that, either.”

“Ghk. P-please.”

“Judging by how well you’re holding out, you’re still a long way from dying. Just like the information I haven’t heard yet.”

“What else in the world are you asking me to say…?”

“I’ve already told you several times. Everything about Dark Heaven. The events happening in Hubei Province, and the Dongting Fisherman.”

“I told you I don’t know—kuweeegh!”

The more we exchanged words, the stronger the Scorching Yang Qi became.

The Three Fiends trembled violently with his eyes rolled white, then a scream burst through his lips.

“Kill me! Kill me already! Even as a vengeful ghost, I’ll chew through your bones and flesh…!”

Damn it. This was as far as I could go.

I roughly withdrew the internal energy I had been sending through him. At the same time, the Three Fiends, who had been convulsing, went limp like a puppet with its strings cut.

I changed the flow of energy and gently stabilized his insides. The old man, who had been waiting nearby, quickly checked his pulse and examined his condition.

“He’s a hard one to kill. He stopped right at death’s door.”

I knew. I had controlled my strength as much as possible to avoid killing him.

*This man can’t die here.*

The Three Fiends was a great fiend from the previous generation and a Supreme Peak master belonging to Dark Heaven.

If we kept him alive and escorted him to Henan, there might be a way to learn even more information.

Of course, I could not rule out the possibility that the writing on those bamboo slips contained everything the Three Fiends knew.

No. That possibility was probably quite high.

*Even after all this, he still refused to talk… That could mean his claim that this is everything was true.*

The mental strength and endurance of a Supreme Peak master were beyond imagination.

Even after the Three Fiends had reached the point of begging someone practically no different from his mortal enemy to stop and screaming for death, he had clung to his story until the very end.

*I—I and my brothers only followed orders under the Demon Lord! I don’t know anything about Dark Heaven’s headquarters or what happened elsewhere, I tell you!*

Remembering the Three Fiends’ cries during the torture, I called out one man’s name.

“Gung Gibang. Any news?”

Gung Gibang, who had been leaning against the iron bars, shook his head.

“Nothing. Our Hubei branch still hasn’t found them.”

“Three Supreme Peak masters. Or hundreds of people and ships must have been mobilized. They couldn’t have avoided attracting attention, so if we focus on outsiders, there should be a chance…”

“We’re already doing that, but it isn’t easy. More than several hundred large ships travel along the Yangtze in Hubei every day, and there are too many people moving by land to count. If it happened a good ten days ago… there’s an even greater chance they escaped Hubei by some means.”

“Damn it.”

Unlike Shanxi Province, which was treated as a borderland, Hubei Province was one of the regions called the Central Plains, and various industries were well developed there.

With merchants and travelers constantly passing through such a vast land, even the Beggars’ Sect could not help but struggle.

Gung Gibang, who had been watching my expression, cautiously opened his mouth.

“Cheongpung and Hyuk Mujin went to the Lower District Sect, so we have no choice but to hope they found something. It probably won’t be much different from our Hubei branch’s findings, but we should hold on to hope.”

Gung Gibang was right. Half a shichen later, Cheongpung and Hyuk Mujin returned to the Zhuge Clan with a large bamboo slip in their hands.

And written on the cord binding the slip was one man’s sobriquet.

Dongting Fisherman.

“This…”

Hyuk Mujin swallowed dryly before speaking.

“It seems the Lower District Sect had some kind of friction with the Dongting Fisherman. They said they had been keeping a close eye on him for several years on the Sect Leader’s orders… It would probably be best if you looked through it yourself.”

I quickly skimmed the contents of the bamboo slip.

The records on the Dongting Fisherman began no fewer than three years ago, and the slip in my hands contained only a portion of them.

And the records from one month ago until today revealed a single fact.

*The Dongting Fisherman is still in Hubei Province.*

That meant…

Rattle!

I shoved the bamboo slip into my robe and went without hesitation to find one man.

Zhuge Gyun, the Divine Marvel Dragon—the Zhuge Clan’s Lesser Family Head, who had been issuing orders in place of the Family Head, Zhuge Feng—opened his eyes wide at my noisy arrival.

“What happened all of a sudden? My ancestor Zhuge Wuhou said that a junzi[^3] should always maintain proper bearing and remain tranquil…”

“Shut up. Are the people ready?”

“The people my fath—no, the Family Head mentioned are already prepared to leave. Do you intend to depart immediately?”

“Yeah. But I think I need to stop somewhere else first.”

“Pardon? Where…?”

“Dongting Lake.”

[^1]: A **jiazi** is a traditional sixty-year cycle.

[^2]: A **shichen** is a traditional time unit of roughly two hours.

[^3]: A **junzi** is the Confucian ideal of a morally upright gentleman.
## Chapter artifact 456

# Chapter 456

“Dongting Lake, out of nowhere? What do you mean?”

Zhuge Gyun’s puzzlement lasted only a moment. Though he occasionally behaved like an eccentric, his mind was as sharp as befitted a scion of the Zhuge Clan.

The epithet Divine Marvel Dragon had not been bestowed on him simply because he was deeply versed in mechanisms and formations.

“Are you trying to find the Dongting Fisherman?”

Several shichen[^1] earlier, Zhuge Gyun had heard the full circumstances of the case from me when I had just arrived at the Zhuge Clan. He also knew that the Dongting Fisherman had been identified as one of the culprits.

“Yeah.”

“You are acting rather suddenly… The source of this information must be the Beggars’ Sect and the Lower District Sect.”

“More precisely, the Lower District Sect. They’ve been watching the Dongting Fisherman for three years.”

“Not watching. Monitoring. Our family had also noticed that something had happened between the Dongting Fisherman and the Lower District Sect Leader.”

“Either way, this works in our favor. Read it.”

Zhuge Gyun took the bamboo slip from me, and his eyes moved rapidly across it.

He read every bit of its contents in the space of a few breaths, then rubbed his temple and muttered,

“The Dongting Fisherman is still in Hubei Province?”

“That’s what the Lower District Sect’s intelligence says.”

“This is insufficient. According to what is written on this bamboo slip, the Lower District Sect has not determined the Dongting Fisherman’s exact whereabouts. They merely failed to detect him leaving Hubei Province.”

“I’ve considered that, too. But what if the information is accurate?”

“If that is the case…”

The Dongting Fisherman, whom everyone believed to be dead, was alive and well somewhere in Hubei Province?

That could mean only one thing.

“If the Dongting Fisherman really is a Dark Heaven underling and one of the culprits who massacred Donghu Stronghold, then it would certainly be possible. No—in fact, it would make it even more certain that he is a culprit.”

Zhuge Gyun nodded heavily.

“That is true. If he were not affiliated with Dark Heaven, he would already have revealed the tragedy at Donghu Stronghold to the world and requested assistance from the Zhuge Clan and Wudang.”

After the Sea Serpent Society, three strongholds of the Yangtze River Channel League, including Donghu Stronghold, had been annihilated.

If we had not arrived when we did—and if it had not been for Ship-Fire Boy Mu Song and the fast boats under his command—the tragedy at Donghu Stronghold beyond Tianling Falls would have remained unknown for much longer.

“But a question remains. This is not the kind of thing that can be concealed. It might take time, but the truth would eventually come to light. If Dark Heaven had deliberately intended to hide it, they would have handled the matter more quietly, without attracting the attention of the common people. They could have framed the Yangtze River Channel League for what happened to the Sea Serpent Society.”

He was right. The reason the Zhuge Clan and Wudang had been unable to cross Tianling Falls was that they lacked vessels sturdy enough for the journey and skilled boatmen to pilot them.

Even without Mu Song and the river bandits of Water Dragon Stronghold, they would soon have been able to find people from another region.

Zhuge Gyun stared pensively at the bamboo slip before raising his head to look at me.

“Then why go this far?”

I tilted the cup on the table and moistened my throat.

“In ordinary circumstances, it would be to buy time.”

“Exactly. Dark Heaven would have needed time to escape. But the fact that the Dongting Fisherman is still in Hubei Province is strange.”

“Yeah. It’s strange. So strange that it doesn’t fit together.”

When I answered without hesitation, Zhuge Gyun’s eyebrows rose slightly.

“You have another thought in mind.”

“I told you. In ordinary circumstances.”

“Then…”

“Dark Heaven isn’t made up of ordinary people. You experienced them in Henan, so you should know that.”

“……!”

“They’re the kind of people who throw a pebble first to draw everyone’s attention, then prepare a boulder. The Sea Serpent Society and three strongholds won’t be the end of it. They’re definitely aiming for something bigger.”

Dark Heaven’s power and audacity lay beyond common sense.

Two Supreme Peak masters from the previous generation belonging to the Ten Kings had already died, and thousands of lives had fallen in rivers of blood.

And the two blood tragedies Dark Heaven had caused shared one unmistakable objective.

“Sacred treasures…”

At Zhuge Gyun’s low murmur, I quietly nodded.

In Henan, Dark Heaven had stolen the Shaolin Temple’s sacred treasure, the Green Jade Buddha Staff. When they attacked Sichuan, they had attempted to seize the Myriad-Poison Ring.

Fortunately, their operation in Sichuan had failed. But what they were after was obvious.

*Sacred treasures—or the destruction of the prestigious great sects known as the Nine Sects and One Gang and the Five Great Families.*

It was difficult to believe that people like that had gone to such lengths merely to eliminate the Sea Serpent Society and three strongholds whose members made their living on the water.

It would have been more understandable if they had been aiming for the headquarters of the Yangtze River Channel League, where the Seafaring King was based.

Zhuge Gyun spoke with a stiff expression.

“Then there is sufficient reason for the culprits, including the Dongting Fisherman, to remain in Hubei Province.”

“It’s still only speculation, but for now, we have to assume they drew attention elsewhere in preparation for something bigger. The delay was merely a curtain meant to make us believe they had already left Hubei Province.”

“Unable to see what is right beneath one’s nose… Could they have already disappeared through that bizarre formation known as the Moving Formation?”

“You might as well say Cheongpung walked past a dumpling shop.”

“Oh. Now that you put it that way, I understand completely.”

I glared into empty space and spoke.

“What happened to the Sea Serpent Society and Donghu Stronghold was the pebble. The boulder comes next.”

The pond called Hubei Province was vast. Even if a pebble fell into it, the ripples would not travel far before subsiding.

But if a boulder fell, a great splash would rise, and the fish inside the pond would not escape unharmed.

We had to stop the boulder from falling before the pond was dyed with blood.

“I will inform the local authorities and Wudang in preparation for the worst, then further strengthen our defenses inside and out.”

“Be wary of the government troops. You’ve heard what happened in Sichuan, haven’t you?”

The forces of Dark Heaven led by the Western Heaven Demon Lord had disguised themselves as government troops and swept through the Tang Clan, Emei, and Qingcheng.

It was already common knowledge, so there was no way Zhuge Gyun, the Zhuge Clan’s Lesser Family Head, was unaware of it.

“I am already taking precautions. Though I doubt they will use the same method twice.”

“Inform Donghu Stronghold, too. The fast boats from Water Dragon Stronghold should be waiting at the Zaoyang ferry, so you can entrust the letter to our household retainers.”

Messenger pigeons would have been faster and more convenient, but there was a risk that someone might intercept them. Besides, the Zhuge Clan had no messenger pigeons trained to travel to and from Donghu Stronghold.

*The other two strongholds that had been able to communicate with Donghu Stronghold had already been wiped out, too.*

The horrific sight of the mountain of corpses and sea of blood flashed before my eyes, and my fist tightened before I realized it.

From Shanxi to Henan, then Sichuan, and finally the monster wave that struck Sichuan Province in the modern world—I had already crossed between two worlds and witnessed far too many deaths.

Scrape.

As I rose from my seat, Zhuge Gyun asked,

“Are you leaving right now?”

“The sooner, the better. I don’t know where the Dongting Fisherman is now, but we should go to Dongting Lake first and search for traces.”

“That will not be easy. The Dongting Fisherman spent his entire life around Dongting Lake, so he likely knows several hidden places unknown to the rest of the world.”

I clenched my fist and spoke.

“Hey, are you Dark Heaven?”

“Pardon?”

“I asked if you’re Dark Heaven.”

“Ah, no.”

“Then stop saying ominous things and cheer me on, you bastard.”

Zhuge Gyun glanced at my fist and hurriedly answered,

“Yes, sir. For now, I will mobilize all of our family’s intelligence resources and cooperate with the Beggars’ Sect and the Lower District Sect to search every region outside Dongting Lake.”

“Do a good job. I’m leaving.”

I was about to turn around when I realized I had forgotten one important question.

“Wait. Does the Zhuge Clan have a sacred treasure, too?”

“Of course. There is the four-wheeled cart our ancestor Zhuge Wuhou rode during his lifetime, the Twenty-Four Chapters on the Art of War, in which he compiled his insights, and the White Feather Fan.”

“……That’s quite a lot.”

I had no idea how impressive a cart, a book, and a fan could be as sacred treasures, but I had to check, just in case.

I turned to Zhuge Gyun.

“Let me take a look. I just need to confirm something.”

“We had them, but now we don’t.”

“……?”

“The Twenty-Four Chapters on the Art of War were lost during a war, and the White Feather Fan crumbled with age. As for the four-wheeled cart, I heard that one of our former Family Heads rode it and broke it around two hundred years ago. I cannot remember his name.”

“…….”

What the fuck.

Was this some grand strategy in which they destroyed the treasures themselves before Dark Heaven could steal them?

Judging by the sacred treasures themselves, they seemed to have been meaningful only because they were objects left behind by Zhuge Wuhou. But it was still just as absurd.

“The four-wheeled cart is still here in its broken state, though. Would you like me to show it to you?”

“No, forget it.”

I answered firmly and left the pavilion. Outside, three people who had finished making all their preparations were waiting for me beneath the night sky, which had darkened once more.

Or was it four people?

“He’s still breathing, right?”

“Yes, Benefactor.”

Cheongpung nodded, carrying a wooden pack frame on his back just as I had in Sichuan. The Three Fiends lay on it, all his acupoints sealed and his body bound in chains.

“He is quite weak, but I think he will be fine if I use internal energy from time to time to restore his vitality.”

“That’s enough.”

There was a simple reason for bringing the Three Fiends along. I wanted to find out whether there were any codes or markings that only members of Dark Heaven could recognize.

That was the only reason he was worth keeping alive.

“Let’s go to Dongting Lake.”

We left the Zhuge Clan and raced along the straight highway like comets.

The wind brushing against my entire body seemed to carry the smell of blood with it.

* * *

Whoooosh!

We sprinted without sparing our strength.

Hyuk Mujin’s internal energy and movement technique were inferior to mine, Cheongpung’s, and Gung Gibang’s, so he kept falling behind. But it did not become much of a problem.

“Get on my back.”

Hyuk Mujin, his entire body drenched in sweat, shook his head with difficulty.

“Huff, huff. No, sir. I can run farther!”

“I know you’re having a hard time, so get on.”

“Huff, I am truly fine. I am the Vice Squad Leader of the Jin Dragon Squad of the great Jin Family of Taiyuan! I cannot cause trouble for my family or Captain—”

“Did a guy like you run around trying to pick up silver nyang?”

“…….”

“If you don’t want to die, get on. Otherwise, I’ll leave you behind.”

“Yes, sir.”

Hyuk Mujin was a man of considerable size, but I possessed an exceptional Strength stat. Carrying a person while running was not much of a burden for me.

*I feel like the Red Hare for some reason.*

I wondered at the strange feeling as we continued running.

By the time we had gone some distance, the sky that had been slightly dim when we left the Zhuge Clan had sunk into complete darkness. The people traveling along the highway had vanished as well.

After more than two shichen had passed, Gung Gibang, who had been exerting his movement technique at full strength, opened his mouth.

His words, carrying the smells of filth and sweetness, pierced my ears.

“Wuhan.”

Wuhan was the capital of Hubei Province, a city close to Dongting Lake.

But perhaps because of the series of ominous incidents that had recently occurred, the streets that normally bustled through the night were silent. Not even a rat showed its face.

*Of course. From the common people’s perspective, who would want to wander around at night and die like a stray dog?*

That was what I was thinking as we crossed Wuhan’s complicated streets when it happened.

“Dongting Lake! A boat has sunk in Dongting Lake!”

“……!”

Someone’s scream erupted in the distance, shattering the deep, dark silence.

[^1]: A **shichen** is a traditional time unit of roughly two hours.
## Chapter artifact 457

# Chapter 457

“Dongting Lake! A boat has sunk in Dongting Lake!”

“P-please, help us! People have fallen into the water!”

*Clang, clang—!*

Along with the scream-like shouts rising in the distance, the sharp sound of an alarm bell rang out from beyond the darkness.

But another sound had reached my ears a moment earlier.

*Ding.*

*This is…*

A familiar notification.

A chill of foreboding ran down my spine. I stared at the translucent System window floating before my eyes.

> **System**
>
> - An unexpected Quest, **The Tragedy of Dongting Lake**, has been generated!
> - You cannot refuse the Quest!
>
> **Quest**
>
> **The Tragedy of Dongting Lake**
>
> Dongting Lake is one of the most scenic places under heaven.
>
> Poets and men of letters climb Yiyang Tower to enjoy the beautiful scenery and compose verses about nature, while those blessed with power and wealth set large, splendid pleasure boats afloat and spend days and nights enjoying themselves.
>
> But today, this clear, blue-green lake is filled with the wreckage of shattered boats and corpses.
>
> If someone does not step forward, those who are still alive will meet the same fate!
>
> **Grade:** Peak
>
> **Restriction:** Jin Taekyung
>
> **Mission:** Rescue people (Incomplete)
>
> **Reward:** ???
>
> **Failure:** The deaths of the people
>
> *A considerable amount of time has already passed. You must rescue the people before it is too late!*

When I finished reading the final line of the Quest window, a small holographic window appeared in the air.

> **System**
>
> **Time Limit:** 45 minutes 36 seconds

Damn it. Less than an hour.

*If we waste even a little time… everyone will die.*

There was not even time to wonder how such a catastrophe had happened. A single life might depend on every minute—or even every second.

I drew as much internal energy as possible from my dantian and opened my mouth.

“Run to Dongting Lake with everything you have from this moment on. We save the people first.”

*Whoosh!*

No one answered. There were only rigid faces and an even faster pace.

Using the cries and alarm bells rolling in from the distance as our compass, we ran and ran.

And when the first digit of the time limit changed from four to two, we were finally able to see it.

*Fwoom, kwoooosh!*

Dozens of large and small vessels burned across the broad waters, engulfed in flames, while countless shouts rang out from every direction.

“Bring boats! Even a ferry will do, so hurry!”

“We don’t have enough boatmen!”

“More! Bring more people! How can the warships still be nowhere to be seen when things have come to this?”

“Ahhh! Ahhh!”

With every step closer, the scene before us came into sharper focus.

More than a hundred people ran nonstop along the shore of Dongting Lake, while several small ferries moved slowly across the water.

*That won’t be enough.*

They were making a desperate effort, but it was woefully inadequate for the number of people who needed rescuing.

Even I, whose martial arts were more than worthy of being called superhuman, felt my breath catch the moment I saw the scene.

*How are we supposed to rescue them?*

I had heard many times that Dongting Lake was enormous, but seeing it with my own eyes, its size far exceeded my expectations.

There was no way the vessels would be packed close together on such a vast lake. Judging from the distances between them, every ship must have been out enjoying itself at least several hundred zhang from the others.[^1]

And this was only what I could see immediately. How many more boats and people were submerged beyond my sight?

*Damn it.*

I bit down hard on my lip and increased my speed.

The murmurs of the people who noticed us racing toward them like the wind grew louder.

One military officer, who appeared to belong to the authorities, shouted urgently,

“A-are you martial artists? Please, help—”

“No time for explanations. We’re borrowing some boats.”

“Pardon?”

I left the dumbfounded officer behind and shouted like thunder.

“Gung Gibang, Hyuk Mujin! Smash the ferries!”

*Whoosh!*

There was no hesitation or doubt in either man’s movements.

Gung Gibang and Hyuk Mujin shot past my sides, shouting as they sent palm force and sword strokes flying.

*Slash, boom!*

The two ferries being hurriedly moved by the people were transformed into hundreds of pieces of wood in an instant.

The military officer, momentarily stunned by what had happened before he could even say anything, screamed,

“What in the world are you doing!”

Shocked cries erupted from every direction.

“T-the ferries…!”

“Those bastards are the villains who caused this disaster! They must be trying to keep us from rescuing the people!”

Shock and anger spread rapidly. All manner of curses poured in from every side, along with gazes brimming with killing intent.

But I did not care.

No—saying I had no time to care would have been more accurate.

> **System**
>
> **Time Limit:** 28 minutes 52 seconds

There were barely thirty minutes left.

Even if I explained why I had done what I did, it would only lead to more casualties.

And fortunately, three martial artists were present who could understand my intentions and put them into action.

“Cheongpung, Gung Gibang!”

“Got it!”

“Yes, Benefactor!”

Gung Gibang and Cheongpung understood what my shout meant. They picked up the ferry fragments and hurled them with all their strength toward Dongting Lake, which lay shrouded in darkness.

*Whoosh, splash!*

Dozens of pieces of wood flew through the darkness and fell across the lake.

“W-what!”

“Could this be…?”

Several people finally realized my intentions and widened their eyes, but that number of fragments was not enough.

They might sink before we could even reach them.

In that case…

*We have no choice but to make a path ourselves.*

The moment I made the decision, I stamped down hard.

*Boom!*

The sand and dust piled along the shore surged into the air all at once, making the unprepared people cough.

Taking advantage of the moment when everyone’s vision was obscured, I reached out.

Along with the damp, hard feel of the wood, I called out the command only I could use.

*Inventory: Store.*

*Ding. Ding. Ding.*

> **System**
>
> - **Ferry Fragment** has been stored in your Inventory!
> - **Ferry Fragment** has been stored in your Inventory…

The notifications pierced my ears as the pieces of wood vanished into the air as if dissolving into it.

I left behind only enough fragments to avoid arousing suspicion, then shouted forcefully,

“Cheongpung and Gung Gibang, come with me. Hyuk Mujin, stay here and gather boats and people!”

“Y-yes, sir!”

Just as Hyuk Mujin, who had been gasping for breath since earlier, squeezed the words out, the figures of Cheongpung, Gung Gibang, and me had already shot toward the darkened Dongting Lake.

*Whoosh!*

Hot energy surged from my lower abdomen and flowed down toward my legs.

Powerful internal energy filled a body with such perfect muscles and elasticity that it could have been mistaken for a Heavenly Martial Physique.

*Now!*

*Boom!*

A massive shock wave burst from my toes, pressed down against the ground, and shoved back the rippling water. Sand and gravel scattered as dust, while a cool wind swept across my entire body.

If I reached out, I felt as though I could pluck the stars scattered across the night sky from the heavens.

But that lasted only a moment.

Every leap was followed by a fall.

*Whoooosh!*

The black water, surging violently, rushed toward us.

And my vision, keen as a wild animal’s, had no trouble spotting the pieces of wood half-submerged in the water.

*Tap. Thump!*

My landing was light, but the second leap that followed was heavy.

Cheongpung, Gung Gibang, and I launched ourselves forward again.

We used the ferry fragments we had scattered in advance as stepping stones—once, then twice, three times…

Only after repeating the process several more times did the vessel that had seemed so far away finally draw close enough to distinguish clearly with the naked eye.

But as the distance closed, the foreboding in my heart grew as well.

*I can’t feel any life force.*

There were no screams or movements from survivors—nothing that should have been there if they were alive.

And it did not take long for the foreboding I felt to become reality.

*Tap.*

On the vessel, most of whose hull was already submerged, Gung Gibang and Cheongpung landed on the bow and muttered like men groaning in pain.

“This is…”

“…Benefactor.”

Their voices sounded faint, as though they were coming from hundreds of zhang away.

In that suffocating silence, I looked around blankly.

Everywhere my gaze fell, countless corpses floated on the water alongside the wreckage of shattered ships.

They were dead.

Everyone was dead.

A potbellied man who appeared to be a merchant, dressed in splendid silk. A gaunt, shabby-looking boatman. Musicians and courtesans who seemed to have been hired to liven up the festivities.

Even the number immediately visible to me was easily in the hundreds.

There was no lively music or laughter on the black water.

All that remained was destruction and death—and the fear plainly etched across the faces of the dead.

*How could this have happened?*

For a moment, my mind seemed to go completely blank.

As if possessed, I walked across the water by stepping on the fragments. I used Qi Sense without holding anything back, searching for even one more survivor.

But…

*Beep.*

> **System**
>
> - **Qi Sense** has failed.
> - The qi of the desired target could not be detected within range.

The System was more merciless than ever.

The translucent holographic window and grating failure notification told me that there was not a single survivor nearby.

“What in the world…”

I muttered in despair when a thought suddenly flashed through my mind like lightning.

*Wait. The System?*

I hurriedly raised my head and stared into the air.

The translucent holographic window was still there.

> **System**
>
> **Time Limit:** 9 minutes 43 seconds

“……!”

It felt as though someone had struck me hard in the back of the head.

If there truly were no survivors, the Quest should have been canceled or a failure notification should have appeared. The System was faster and more direct than anything.

But the Quest was still in progress, and the System window displaying the time limit had not disappeared.

There could be only one meaning.

As I stood there, frozen stiff, Gung Gibang spoke to me in a cautious voice.

“Unfortunately, it seems pointless to keep searching for survivors…”

“There are survivors.”

“What?”

“We just can’t see them. There are survivors somewhere much farther away than this. I know it.”

Gung Gibang had been about to say something, but his expression hardened when he saw the certainty on my face.

Cheongpung spoke as well, his voice more serious than usual.

“If what Benefactor says is true…”

“Then we find them and save them. No matter what it takes.”

Gung Gibang stared at me for a moment, then nodded.

“We’ll have to split up. If we tear apart the sunken boats around here and use them, we might be able to keep going for another half a shichen.[^2]”

“You have fifteen minutes from now. Both of you search as far as you can within that time. If you don’t find any survivors, come back.”

The time limit meant the amount of time remaining for the survivors. Searching beyond that point would be meaningless.

The unusual firmness of my tone made the two of them look puzzled, but they soon nodded without another word.

“We’ll do that.”

“Fifteen minutes. I’ll remember, Benefactor.”

“Then split up in your respective directions now. See you shortly.”

*Thump, whoosh!*

When I finished speaking, I kicked off from the bow and leaped.

As I watched the time limit shrink by the second, I pushed all my internal energy and senses to their peak and ran and ran across Dongting Lake, vast as an open sea.

> **System**
>
> **Time Limit:** 1 minute 12 seconds

*Am I too late?*

And just as I was about to give up on everything—

“P-please, save me…”

A tiny, faint voice reached my ears.

[^1]: A **zhang** is a traditional Chinese unit of distance, roughly 3.3 meters.

[^2]: A **shichen** is a traditional time unit of roughly two hours.
## Chapter artifact 458

# Chapter 458

*P-please, save me…*

Like a dying ember, the voice was tiny and faint.

But that alone was enough. My heart, weighed down by the helplessness of having failed to save anyone, began pounding fiercely, and strength surged through my limp body.

I launched myself in the direction of the voice.

*Inventory: Open. Summon!*

*Thud!*

A remaining fragment of the ferry skimmed across the moon’s reflection on the water.

I leaped through the air like a bird, drew up the last of my internal energy, and focused it in my eyes.

My drastically enhanced vision took in the scene below with perfect clarity.

*That’s…*

Shipwreckage and corpses.

Though the vessel had been smashed into pieces beyond recognition, there was no doubt that it had been the largest and most splendid ship I had seen on Dongting Lake.

*There’s a survivor somewhere among them.*

The problem was that there were far too many corpses and fragments visible at once.

But there was no time to hesitate.

> **System**
>
> **Time Limit:** 59 seconds

Fifty-nine seconds. The survivor’s life depended on the brief span of less than a minute.

I closed my eyes and steadied my breathing. Then I drew up every last bit of my internal energy, which was already nearly depleted.

*Fwoooooosh!*

Qi Sense.

The Scorching Yang Qi extending from my entire body raced across the rippling water.

It swept through the more than one hundred corpses whose souls had already departed, as well as the countless fragments of ships, searching every inch.

And finally—

“……!”

I saw it.

No—I felt it.

Dozens of zhang away,[^1] a faint qi that was even now sinking beneath the surface by the second.

I opened my eyes halfway.

> **System**
>
> **Time Limit:** 32 seconds

The Scorching Yang Qi circulating through my body rushed toward my lower half.

When I stepped on empty air with the tips of my toes, the compressed air exploded outward, and a cold wind swept across my entire body.

*Boom! Fwoooooosh!*

I shot forward like a meteor. The wind split apart, and space seemed to vanish.

The scenery on either side flashed past, but my gaze remained fixed on a single point.

The rough, surging black water.

There was a survivor in there.

*Damn it. I can’t even swim.*

The thought had barely crossed my mind when Dongting Lake slammed into my entire body.

*Splash! Gurgle!*

The impact was enough to make my breath catch.

If I had not learned martial arts, my bones would have broken and my internal organs would have been shaken to pieces.

I sank beneath the surface, exhaling a cloud of bubbles.

A school of fish scattered in alarm at the sudden arrival of an unwelcome visitor, revealing two figures slowly sinking into the depths.

> **System**
>
> **Time Limit:** 20 seconds

*More. More. More…*

I summoned every last bit of strength I had and pushed forward. I seized the wrists of the two unconscious, limp figures and surged upward with all my might.

Ten seconds. Nine, eight…

The faint moonlight reflected on the surface drew closer.

My arms and legs felt as heavy as if iron balls had been tied to them, while the two people in my hands weighed like thousand-catty boulders.

And then—

*Splash!*

“Puaaah!”

I expelled the breath I had been holding.

Air cold enough to sting flowed deep into my lungs.

But pulling the survivors out of the water did not mean everything was over.

> **System**
>
> **Time Limit:** 3 seconds

In that moment, I instinctively realized what I had to do.

*Save them.*

That single thought moved my body, which had briefly come to a stop.

I thrust both palms, infused with what little internal energy I had left, toward the two people.

*Boom!*

Their bodies jerked, and water splashed.

But instead of any response from the unresponsive survivors, the number on the System window floating in the air changed.

> **System**
>
> **Time Limit:** 2 seconds

*One more time…*

*Boom!*

> **System**
>
> **Time Limit:** 1 second

Everything slowed down.

That paltry digit of 1 grew larger and heavier than ever, pressing down on me.

I was staring blankly at the System window, my eyes wide, when—

“Puh.”

“Cough, cough.”

At the same moment the survivors’ breathing finally returned, the System window, which had been about to change to its final digit, stopped.

Then a bell rang out like a victory cannon.

*Ding.*

> **System**
>
> - You succeeded in **Rescuing Lives**!
> - You completed the unexpected Quest **The Tragedy of Dongting Lake**!
> - You have successfully completed the Quest. An appropriate Reward will be granted!
> - You acquired a considerable amount of EXP and Fame!
> - You acquired the Title **Water Rescue Worker**!

I listened to the notification drilling into my ears and muttered,

“Sibu-leol.”

The joy and relief of having finally succeeded came second to the crushing heaviness of my exhausted body. I had been worn down by the forced march that began at the Zhuge Clan.

Maybe it was because the tension I had maintained by a thread had suddenly snapped.

*…Damn it. It’ll take forever to get back to land.*

At this rate, would I end up needing to be rescued too?

That was when I found myself floating with the two survivors, using my body’s buoyancy.

*Whoooooosh!*

Something cut rapidly through the water in the distance like a jet ski before stopping right in front of me.

A pure-white body and scales, along with two horns.

“A water snake…? No, a Thousand-Year Poison Horned Snake?”

*Hiss. Hiss. Hiss-hiss!*

“Hey, don’t go anywhere!”

I hurriedly shouted at the creature as it flicked its tongue and turned away.

“Hey! Hey! Water snake! Thousand-Year Poison Horned Snake!”

*Hiss!*

“You little bastard, did you just spit at me—wait.”

Could this be its way of expressing that it was sulking?

One thought suddenly came to mind, and I opened my mouth in an earnest yet cautious voice.

“Mimi… Mimi-chan?”

*Hiss-rik! Hiss-ririk!*

Only then did the Thousand-Year Poison Horned Snake—or Mimi-chan—nod in satisfaction and extend its tail toward me as if telling me to hold on.

Right on cue, someone shouted from far away.

“Mimi! Rescue Benefactor!”

*Hiss-rik!*

“…….”

Yeah, fuck it. Who cared what the technique was called? Just get me out of here.

* * *

I sat on a damp rock and stared at the rippling water.

Two people. Only two.

Of all the countless people who had buried their bones in Dongting Lake today, the two I had saved were the only survivors.

*…Only two out of all those people.*

I had suspected it from the moment the Quest was completed, but reality was even more brutal and merciless than I had imagined.

And the countless deaths left behind by today’s tragedy had given rise to even greater sorrow.

“Ugh…”

“Sniff, sob!”

“Oh, poor Chil-Sam’s father!”

“What inhuman bastard could have done such a thing!”

By then, the number of people gathered along the shore of Dongting Lake had grown to more than a thousand, and they poured out every emotion imaginable.

A Confucian scholar lamented, unable to continue speaking. Behind a government soldier clutching a fallen comrade’s corpse and weeping came the wails of a woman with an infant strapped to her back. An old man, the veins standing out on his neck, even swung his long-stemmed tobacco pipe at some unseen culprit.

There was no longer any laughter or singing to be found at Dongting Lake, one of the most famous scenic sites under heaven.

Only the sorrow and lamentation of those left behind remained, along with the anger infused in all those emotions.

But nothing changed.

The waters of Dongting Lake had grown calm, as if nothing had happened, while the faint dawn mist spreading across the lake created a beautiful scene.

*Is this what the Wuling Peach Blossom Spring where immortals are said to live looks like?*[^2]

I stared silently at the scene before me, then spoke without warning.

“This feels like… something, doesn’t it?”

I was not talking to myself.

Cheongpung, who had not left my side for more than fifteen minutes, answered,

“Yes. Like fucking shit.”

Under normal circumstances, I would have snorted with laughter despite myself. But now, I felt nothing but empty.

I fidgeted with a pebble and asked,

“I only said ‘something.’ I didn’t know Young Hero Cheongpung knew how to swear.”

“I didn’t at first, but I know a little now. I learned by watching someone.”

“You’d better keep that a secret from Great Hero Mae Jonghak.”

“Why, Benefactor?”

“Why do you think? How would you feel if Mimi suddenly called you a fucking bastard one day?”

“Hmm. I don’t think I’d like it.”

“……Wouldn’t most people be surprised that a snake was talking before getting angry? Either way, you’d be surprised and angry. Great Hero Mae Jonghak would be the same.”

“Oh. I see.”

“Yeah. That’s how it is.”

“What should I do if I accidentally swear in front of Grandfather?”

“Say Gung Gibang taught you. Or Hyuk Mujin.”

“Okay.”

Silence descended.

That conversation had been nothing more than nonsense dragged out as it came to me. I had felt that I needed to say something—anything. I wondered if doing so might make things a little better.

Both Cheongpung and I knew the truth.

We also knew that doing this would not make our current feelings any better.

“Fuck…”

I muttered the curse like a lament.

I did not know whether today was simply an unusual day, or whether those creatures also understood the circumstances and were grieving.

There was no birdsong.

Only the wails and sobs of the people filled the air around us.

I listened quietly to those stifling, unbearable sounds, then clenched the pebble resting in my palm as hard as I could.

*Crack. Crunch.*

A handful of powder spilled from my fist.

No—it was carried by a breeze that had blown in from somewhere and settled lightly on the surface of the water.

As if they were mortal remains imbued with someone’s spirit.

Cheongpung watched the scene in silence before suddenly speaking.

“Benefactor.”

“What?”

“What should I do at times like this?”

“…….”

“So many people have died. In Henan, in Sichuan, at Donghu Stronghold, and today, here.”

His voice trembled faintly as he continued.

“I keep thinking about the dead. And I get angry. I hate the people who keep killing others, and I feel pathetic for being unable to do anything.”

“……I was like that too. No, I still am.”

“What did Benefactor do whenever you felt this way?”

“Me?”

I turned my head and finally met Cheongpung’s gaze.

His eyes, usually clear without a single blemish, were swirling with a mixture of emotions.

Within that confusion, I saw my past self—and the present me staring at Cheongpung now.

*Was I like this?*

The current version of myself, viewed through Cheongpung’s eyes, was simply impassive.

I was not exhausted like Gung Gibang or Hyuk Mujin, nor was my body trembling with anger and sorrow like those who had lost their families and companions.

No, it was not that I could no longer feel emotions.

I had merely learned to contain them.

The rock that had collided with something again and again over many years, worn and ground down until it had finally grown accustomed to it, stood there before me.

“Who knows? What did I do back then?”

After thinking for a moment, I slowly continued.

“I wasn’t any different from you, Young Hero Cheongpung. I swore nonstop at those bastards who deserved to die, blamed myself for my helplessness, and then made a vow.”

“A vow?”

“Yeah. A vow.”

I raised a finger and pointed at the grieving people and the corpses laid out along the shore.

“I vowed to kill every last bastard who did this. That was my vow.”

“……!”

“I’m no saint. I won’t be satisfied until I pay them back at least in equal measure. This time is no different.”

That was when a dry, cold voice that felt unfamiliar, almost as if it belonged to someone else, slipped through my lips.

“Captain.”

Hyuk Mujin approached us, exhaustion plainly visible on his face.

“The survivors have regained consciousness.”

“That’s good. Both of them?”

“No, sir. Only one of them, for now.”

It was unfortunate, but I had suspected as much. The treatment I had performed after rescuing them had only been an emergency measure.

“Then let’s go.”

“Yes, sir. This way.”

Cheongpung and I followed Hyuk Mujin.

At last, we came face-to-face with one of the survivors who had regained consciousness.

“We’ve met again rather quickly, haven’t we?”

At my greeting, Honglan, the singing courtesan of dazzling beauty, bowed with the utmost respect.

“It is an honor to see you, Benefactor.”

[^1]: A **zhang** is a traditional Chinese unit of distance, roughly 3.3 meters.

[^2]: Wuling Peach Blossom Spring is a classical Chinese image of an idyllic, isolated utopia.
## Chapter artifact 459

# Chapter 459

A flower does not lose its natural beauty simply because it has been drenched by water.

The same was true of Honglan. She looked haggard after everything she had been through, but even that appearance was as lovely as a hydrangea blossom.

“It is an honor to see you, Benefactor.”

At that moment, I thought I finally understood what people meant when they described a voice as sounding like jade beads rolling across one another.

Her face, entirely free of makeup, was dazzlingly pale, and beneath her long lashes were two eyes like morning stars.

“Good heavens.”

“How can anyone be this beautiful…?”

Exclamations rose from every direction.

Those who had been admiring Honglan’s beauty hurriedly shut their mouths and left when they noticed my gaze.

Perhaps they were ashamed of behaving that way while hundreds of people had been drowned.

On the other hand, it could also mean that Honglan’s beauty was extraordinary enough to make them forget such a fact.

*If this weren’t the situation we were in, I wouldn’t have been any different from them.*

After composing myself, I spoke.

“I’m glad you’ve regained consciousness. How are you feeling?”

Honglan lowered her head slightly before answering.

“Although I cannot compare to my Benefactor, this lowly woman has also trained in martial arts. I do not seem to have much trouble moving.”

The martial arts I had sensed from her were barely at the First Rate realm.

She might not have been quite skilled enough to be called a fully matured First Rate master, but the vitality of a martial artist who had built up their body and accumulated internal energy was incomparable to that of ordinary civilians.

*Thank heavens.*

The fact that Honglan was a martial artist had been a blessing both for her and for the other person rescued alongside her.

I asked the military officer who was still standing nearby,

“Where is Ju Wongong?”

Ju Wongong. A carefree distant imperial relative who had taken a pleasure boat out on Dongting Lake despite the troubled atmosphere of the times.

He was the other survivor.

“If you mean Young Master Ju, we assigned him an ironclad escort and moved him somewhere safe. According to the physician, he has passed the most dangerous point for now, but they cannot say when he will regain consciousness.”

He was the same military officer who had directed everyone when we first arrived at Dongting Lake.

Responsible for the security and defense of Dongting Lake, one of the major areas of Hubei Province, he continued in his stiff voice,

“When we reported what happened, the City Lord was furious as well. Although they failed, attempting to assassinate a member of the imperial family is the gravest of crimes. We will immediately mobilize the entire fleet and all forces in the city and make an example of these insolent rebels—”

“The murder of an imperial family member was not their objective.”

“What?”

I stared at the confused officer and continued.

“They’re called Dark Heaven. You may have heard of them.”

“Dark Heaven…? Aren’t they a gang of thugs that has been causing trouble in the martial world recently?”

“A gang of thugs?”

A scoff escaped me at his choice of words.

The name Dark Heaven had begun to spread among ordinary people after the Shaolin Bloodshed, but the officer before me had no idea how powerful or terrifying they truly were.

Gung Gibang, who had been standing beside me, also spoke with an incredulous expression.

“Hey, Officer. Do you know that gang of thugs killed Master Hong Dao, the Abbot of Shaolin Temple and the Dharma King?”

“Th-that…”

“The Poison King, Tang Sadok, the Grand Family Head of the Sichuan Tang Clan, was killed too. So was the Heaven-Shaking Venerable Nun of Emei Sect. Three Supreme Peak masters from the previous generation who once shook the martial world, along with more than two thousand martial artists, are dead. And you call them a gang of thugs?”

“I-I have heard those rumors, but I did not know exactly how powerful they were. Then, are you saying that Dark Heaven was responsible for this?”

“There’s a limit to how ignorant a person can be. Good grief. Even a stray dog passing by would laugh.”

“That’s enough.”

I raised a hand to stop Gung Gibang. Then I continued speaking to the officer, whose face had turned red with embarrassment.

“Regardless, what I’m saying is that their objective was not Ju Wongong.”

“Th-then what grounds do you have for thinking that?”

“If Dark Heaven had wanted Ju Wongong dead, he would already be gone from this world.”

“……!”

“If they wanted to kill him, they could have done so by any means. He wouldn’t have been able to stop them even if they ambushed him in broad daylight. Why would they wait until he set a pleasure boat afloat on Dongting Lake, then destroy it along with all the other vessels? And why would they do so without even confirming whether their target was dead or alive?”

To Dark Heaven, Ju Wongong’s life was like an object inside a cloth bundle. If they made up their minds, they could put him in or take him out whenever they wanted.

Besides, there was no obvious reason for them to target a distant imperial relative who had committed a crime and been banished.

If they wanted to cause chaos, the Emperor or Prince Shangshan Zhu Bao would have been far more attractive targets.

I spoke in a firm voice.

“Their objective was not the murder of an imperial family member. He was simply one of the fish that happened to get caught in the net they cast.”

“Then what in the world were they after…?”

“We’ll naturally find out once we catch the culprit.”

“What?”

“I’m talking about the culprit who carried this out directly. The fact that Dark Heaven is behind everything is already certain.”

The officer, who had been staring blankly with his mouth open, hurriedly asked,

“G-Great Hero, are you saying that you know who the culprit is?”

“There is someone I suspect, but the testimony of the person who saw them directly would be more accurate.”

I turned my head and looked at Honglan.

With Ju Wongong hovering between life and death, she was the only witness who held the key to unraveling everything.

“Did you see them?”

It was a short question, but it was enough. With everyone’s eyes fixed on her, Honglan’s red lips slowly parted.

“Yes.”

“……!”

“……!”

Shock and agitation spread through the room in an instant. Amid the commotion, I clenched my fist tightly.

*Finally.*

The series of incidents that had begun with the Sea Serpent Society. The bastard—or bastards—who had remained hidden without revealing even a hair had finally begun to show themselves.

I couldn’t let go of this tail now that I had finally found it. I had to seize it with all my strength, drag it out until I reached the body, and deal with them.

Remembering the countless corpses left behind so far, I asked again.

“Tell us exactly what you saw.”

“It was…”

A shallow furrow appeared on Honglan’s smooth, unlined brow.

She seemed to be recalling what had happened. After hesitating for a moment and steadying her breathing, she began to speak.

“Everything happened in an instant. The festivities were in full swing when the two military ships nearby sank one after another, only moments apart. That was how it began.”

I listened closely to Honglan’s story.

Ju Wongong might have been a distant relative, but he was still a member of the imperial family. The two military ships assigned to escort him had been overwhelmed by a sudden ambush, and the pleasure boat, where the festivities had been reaching their peak, had fallen into chaos as well.

“But no one could stop it. Nothing was visible, yet the ship suddenly tilted with a tremendous roar. Then a single streak of Force flew from somewhere and swept through the vessel. That was all it took.”

“Force…!”

“I am certain. Most of the Peak masters guarding Young Master Ju and the martial artists of Qingxia Hall died from that single attack.”

The scene seemed to unfold before my eyes.

Force was one of the most destructive manifestations of martial energy. Even someone who had never seen it before would understand what that dazzling light was the moment they faced it.

Honglan was no different. It must have been an attack that Ju Wongong’s guards and the bumbling martial artists of Qingxia Hall had been powerless to stop.

Perhaps because she had recalled such a horrifying memory, Honglan’s voice began to tremble faintly.

“But in the final moment, the guards risked their lives to push Young Master Ju away, and I embraced him before throwing myself into the river.”

Honglan’s quick thinking had saved both herself and Ju Wongong.

Those whose bodies had seized up with terror were mostly slaughtered soon afterward, while those who were still breathing could not endure the cold of the deep night or the injuries they had suffered in the fall for long.

And then…

Honglan said that, amid the darkened waters of Dongting Lake, she had seen something rapidly moving away.

“It was a person. Just one.”

“……!”

The moment the tail revealed itself, I bit down hard on my lips and asked again.

“Are you certain?”

“How could I lie to my Benefactor? It was only for the briefest moment, but I saw it clearly with these two eyes.”

Honglan was the sole witness, and she was also a martial artist who had reached the First Rate realm. If she was certain, then it was highly likely to be true.

*That’s right. It was him.*

Just as thoughts of someone flashed through my mind, the military officer, who had been listening to us with a dazed expression, suddenly spoke.

“A-are you all out of your minds? No matter how powerful martial artists are, this is not land. This is Dongting Lake! Dongting Lake is as deep and vast as the open sea!”

“Does anyone here not know that?”

Gung Gibang muttered it like a sigh, while Hyuk Mujin clicked his tongue.

“And?”

“What do you mean, ‘and’! I have heard plenty about the miraculous abilities of martial artists like you, but this is absurd. Even the water bandits of the Yangtze River Channel League whom I have encountered were never capable of such feats. How could anyone swim so quickly across such a vast body of water, much less sink dozens of vessels single-handedly, including the Great Nation’s warships?”

“He could. If he is the man I’m thinking of.”

A clear voice rang out. Under everyone’s gaze, Honglan slowly opened her lips.

“He can breathe like a fish, swim faster than one, and easily sink dozens of vessels by himself. I do not know how formidable the water bandits you know are, but at least here in Dongting Lake, even the Seafaring King himself would be unable to stand against him.”

Honglan’s gaze turned toward the blue-green waters beyond the camp.

Dongting Lake. A scenic site known throughout the land for its long history and beautiful landscapes.

And one old fisherman who had guarded Dongting Lake all his life.

No. A Supreme Peak master of the previous generation, and a master of water arts who stood shoulder to shoulder with the Seafaring King.

I quietly murmured his alias.

“The Dongting Fisherman.”

“……!”

The Lower District Sect’s information had been correct. The Dongting Fisherman had not yet left Hubei Province.

He had faked his death and remained here in Dongting Lake, a place that could be called directly beneath a bright lamp, evading everyone’s suspicions and attention.

And at last, I had found Dark Heaven’s tail—the Dongting Fisherman.

*I’ve finally made it this far. You damn old bastard.*

We had already paid far too high a price in lives. Before any more time passed, I had to capture the Dongting Fisherman and uncover every detail of Dark Heaven’s movements and plans.

It was the only way to prevent an even greater tragedy.

That was why Honglan’s next words felt like a torch lighting the way forward.

“Do you happen to know, Benefactor, that the Dongting Fisherman has hidden secret places where he stays throughout Dongting Lake?”

“You’re saying that you might know where they are?”

“I do not know their exact locations, but I know several places where they might be. Once you have finished preparing, please tell me. This humble woman can guide you there herself.”

“……!”

I clenched my fist tightly. Then I immediately sprang to my feet.

“Let’s go there. Right now.”

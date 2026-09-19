# Checkpoint Review — 460–464

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

# Chapters 460–464

## Plot

Taekyung travels across Dongting Lake with Cheongpung, Hyuk Mujin, Gung Gibang, Honglan, and a skilled boatman to investigate the Dongting Fisherman’s hidden refuges. After searching four sites unsuccessfully, they reach the deepest location despite worsening weather. The Water Rescue Worker Title lets Taekyung breathe and move underwater, where he discovers a cave and enters the Fisherman’s secret refuge. He confirms the Fisherman is inside and attacks from solid ground, but a snow-white streak interrupts his spear thrust.

At Donghu Stronghold, Zhuge Clan and Wudang forces find no land-based Dark Heaven traces or Moving Formation remnants. Mungyeong searches the deep river and later reveals to Jeok Cheongang that he is the Slaughter Saint and has reached Returned to Youth. Warning that Taekyung and possibly everyone else are in danger, he prompts Jeok to launch the boat immediately.

Jeok Cheongang reaches Five Qi Returning to Origin and Furnace Fire Pure Blue but cannot advance further, recognizing that his desire for Returned to Youth is greed rooted in unresolved inner demons. The danger Mungyeong sensed, the identity of the white streak’s attacker, and the Dongting Fisherman’s exact role remain unresolved.

## Continuity

- Taekyung is inside the Dongting Fisherman’s underwater secret refuge. The Dongting Fisherman is present, and a white streak has just interrupted Taekyung’s surprise attack.
- Deliberate, substantial damage marks the refuge’s passage; its cause and connection to the Fisherman remain unknown.
- Four of five suspected refuges were empty. The final refuge lies beneath Dongting Lake.
- Taekyung’s Water Rescue Worker Title grants underwater breathing, movement, and vision for twenty-four hours; it cannot be reused for one week, and his Fire Gate Clan martial arts are twenty percent weaker underwater.
- Honglan survived the Dongting Lake disaster and is recovering. Ju Wongong remains unconscious under guard.
- Mungyeong is the Slaughter Saint and has reached Returned to Youth. He warned Jeok Cheongang that Taekyung and possibly everyone else are in danger.
- Jeok Cheongang has achieved Five Qi Returning to Origin and Furnace Fire Pure Blue but remains unable to cross the next barrier.
- Donghu Stronghold’s land search found no Dark Heaven evidence or Moving Formation remnants; Mungyeong searched the remaining river area.
- The shared symbols between the Arch Lich’s magic circle and Dark Heaven’s formations, the Hubei massacres, the Wudang killer demon, and Dark Heaven’s wider plan remain unexplained.
- The captured Three Fiends remains alive and is being transported for investigation. Jin Wikyung is cooperating with Taekyung; the Skeleton King’s undead identity remains concealed; Go Jun is searching for Lee Jungryong’s holographic recorder.

## Translation Decisions

- Use “Dongting Lake,” “Dongting Fisherman,” “Water Rescue Worker,” “Water Rescue Worker’s Webbing,” “Water Rescue Worker’s Gills,” “Hidden Shadow Ghost,” “secret refuge,” “Wall Lizard Technique,” “reef,” and “Yiyang Tower.”
- Render 오기조원 as “Five Qi Returning to Origin,” 노화순청 as “Furnace Fire Pure Blue,” 반로환동 as “Returned to Youth,” and 살성 as “Slaughter Saint.”
- Preserve “Eight Extraordinary Meridians,” “Tianling Falls,” “Hwang Cheol,” “Do Ripgun,” “Mad Water Saber Demon,” “Wave Fox,” “Sichuan Blood Tragedy,” “Ju Wongong,” and “Honglan.”
- Retain “Three Fiends,” “great fiend,” “Demon Lord,” “killer demon,” “First Rate wandering martial artist,” “sibu-leol,” “Lord Fuck,” and “Lord Sibu-leol.”
- Preserve Taekyung’s dry, profane humor, Cheongpung’s deferential Benefactor address and innocent voice, Honglan’s humble formal speech, Jeok Cheongang’s gruff profanity, and the Skeleton King’s grandiose voice.

## Durable state

{
  "active_continuity": [
    "Taekyung has entered the Dongting Fisherman’s underwater secret refuge and confirmed that the Dongting Fisherman is inside; a white streak of light has just struck Taekyung’s attacking spearhead, so the confrontation’s outcome is unresolved.",
    "Fresh damage throughout the refuge’s passage bears the traces of one person’s deliberate force, but its cause and connection to the Dongting Fisherman remain unknown.",
    "Taekyung completed the unavoidable Peak-grade Quest The Tragedy of Dongting Lake, rescued the only two survivors found, and earned the Water Rescue Worker Title.",
    "Honglan survived the Dongting Lake disaster and is recovering; Ju Wongong remains unconscious under guard after passing the most dangerous stage of his injuries.",
    "Jin Wikyung is acting as an inspector for the new Murim Alliance and is cooperating with Taekyung’s investigation.",
    "The shared symbols between the Arch Lich’s magic circle and Dark Heaven’s formations remain unexplained.",
    "The Sea Serpent Society and three Yangtze River Channel League strongholds, including Donghu Stronghold, were destroyed with more than a thousand casualties, while the perpetrators’ wider plans remain unknown.",
    "Mungyeong is searching Donghu Stronghold for Dark Heaven traces with Zhuge Clan and Wudang; Mungyeong found no land evidence or Moving Formation remnants and entered the river to search the remaining area.",
    "Wudang is responding to an unidentified killer demon responsible for more than thirty deaths, including twenty pilgrims on Mount Wudang.",
    "The Skeleton King’s undead identity remains concealed, and Taekyung has ordered him to join Peace Guild under a prepared contract.",
    "Go Jun is expected to succeed Lee Jungryong as Ares Guild’s captain and is searching China for Lee’s holographic recorder.",
    "The captured Three Fiends is a former-generation great fiend and Supreme Peak Dark Heaven subordinate whom Taekyung is transporting alive to investigate possible codes or markings."
  ],
  "continuity_sources": [
    464,
    463
  ],
  "open_questions": [
    "What is the Dongting Fisherman’s exact role in Dark Heaven, and who launched the white streak that interrupted Taekyung’s attack?",
    "What caused the single person’s deliberate destruction inside the refuge, and is it connected to the Dongting Fisherman or another intruder?",
    "What are the origin and purpose of the symbols shared by the Arch Lich’s magic circle and Dark Heaven’s formations?",
    "Who destroyed Donghu Stronghold and the related Yangtze River Channel League strongholds, why was no Moving Formation trace left, and was the destruction a diversion?",
    "What danger did Mungyeong detect, and are the Wudang killer demon and that danger connected to Taekyung, Jeok Cheongang, or Dark Heaven?"
  ],
  "safe_through": 464,
  "temporary_decisions": [
    "Render 오기조원 as Five Qi Returning to Origin, 노화순청 as Furnace Fire Pure Blue, 반로환동 as Returned to Youth, and 복자 as diviner.",
    "Render 살귀 as killer demon, 은영귀 as Hidden Shadow Ghost, 일급 낭인 as First Rate wandering martial artist, 삼괴 as Three Fiends, 대마두 as great fiend, and 마군 as Demon Lord.",
    "Render 시부럴 as “sibu-leol,” 시벌좌 as “Lord Fuck,” and 시부럴좌 as “Lord Sibu-leol.”",
    "Preserve the Skeleton King’s grandiose, mock-offended voice and Taekyung’s dry, profane humor; render 주원공 as Ju Wongong, 대죽산표국 as Daejuksan Escort Bureau, 형문검가 as Hyungmun Sword Family, 응성상회 as Eungseong Merchant Association, 천룡인 as Celestial Dragon, 사인교 as four-person sedan chair, 홍란 as Honglan, 가기 as singing courtesan, 구족 as the nine branches of kin, 수상 구조대원 as Water Rescue Worker, and 수공 as water arts.",
    "Render 익양루 as Yiyang Tower, 황철 as Hwang Cheol, 도립군 as Do Ripgun, 광수도귀 as Mad Water Saber Demon, 파랑호 as Wave Fox, 동정호 as Dongting Lake, 사천혈사 as Sichuan Blood Tragedy, 천령폭 as Tianling Falls, and 기경팔맥 as Eight Extraordinary Meridians."
  ],
  "version": 1
}

## Reading copies

## Chapter artifact 460

# Chapter 460

It was bad weather in more ways than one.

The waters of Dongting Lake, which had swallowed dozens of vessels and claimed lives overnight, were rough, and the wind blowing in from the distance was violent.

Even the old boatman who knew Dongting Lake like the back of his hand seemed to think that setting out in such weather was a terrible idea.

“I—I can’t do it, sirs.”

Those were the first words from the boatman, who had clearly been dragged here against his will from the beginning. He continued anxiously,

“The places you wish to visit are unusually narrow and turbulent even for Dongting Lake… In weather like this, it would be even more impossible.”

“That is why we are asking for your help. Merchant ships and warships cannot enter those places, but a sturdy ferryboat guided by the most skilled boatman on Dongting Lake might be able to.”

“No matter how you put it…”

“Boatman?”

“Y-yes?”

“Please.”

A man remained a man, no matter how old he got.

The old boatman, dazed by Honglan’s gentle voice and dazzling beauty, only came to his senses after climbing aboard the ferryboat.

“What was I thinking? I must have gone mad. I knew what happened last night, yet I still set out on the water. What will I do if I run into a Hidden Shadow Ghost…?”[^1]

A Hidden Shadow Ghost?

The unfamiliar word mixed into his grumbling pricked my ears. When I turned around, my eyes met the terrified boatman’s.

He swallowed hard before answering.

“Just as the name says, it’s a ghostly creature. Plenty of boatmen have fallen victim to it lately. One of them was an old friend of mine. He went out at night hoping to earn a few extra coins, and then…”

The old boatman stared at the rippling waters of Dongting Lake with eyes steeped in fear.

“In any case, they call it a Hidden Shadow Ghost because people die without ever seeing even a shadow of it. This is only the humble opinion of an old man, but those recent incidents are clearly its doing. Every one of them was the work of that evil spirit.”

Gung Gibang clicked his tongue and cut in.

“Evil spirit, my ass. Listen, boatman. Do you think that’s the first story like this I’ve heard? If every one of those stories were true, half the fish in the world would have human faces, and the mountains would be crawling with thousand-year-old white tigers and dragons.”

“This is the absolute truth. With all these abominable things happening, the spirit of Dongting Lake must have grown furious.”

“An evil spirit wasn’t enough, so now we have a lake spirit too? Enough. Let’s not talk about it.”

“No, but every boatman in Hubei Province has heard this story…”

“Do I look like a boatman to you?”

“N-no, sir. Anyone can see that you’re a beggar among beggars.”

“Ah, that’s true, but now I’m suddenly pissed off.”

“P-please calm down, honored sir. This old man is guilty of nothing more than reporting what he heard.”

The old boatman’s voice was thick with grievance.

He had spent his entire life as a boatman in the Murim, where all sorts of legends and superstitions were treated as fact.

Perhaps because of that, he seemed to firmly believe that the recent string of gruesome incidents had been caused by the evil spirit known as the Hidden Shadow Ghost.

*When you think about it, it might not be complete nonsense.*

Judging by Honglan and Cheongpung’s expressions, they had reached the same conclusion.

The moment our gazes met, they both spoke at once.

“Benefactor, could it be…”

“Benefactor, is the Hidden Shadow Ghost the boatman mentioned…”

“Wait. I know what both of you are trying to say, so you don’t have to. And if you absolutely insist on calling me Benefactor, take turns. You’re confusing me.”

A single Benefactor parrot had already been enough. Now there were more of them.

Sometimes, things like this made me feel as though I had become someone important.

Then again, Honglan had good reason after I saved her life. But was that man Cheongpung really planning to treat me as his Benefactor for the rest of his life just because I had given him a few sweets when he was hungry?

I sighed and continued.

“Anyway, the Hidden Shadow Ghost is probably the Dongting Fisherman. Or it could be people taking advantage of the confusion to commit robbery.”

“That’s exactly what I was going to say, Benefactor.”

Not to be outdone by Cheongpung, Honglan nodded as well.

“I think so as well, Benefactor.”

“I said one person at a time.”

Regardless, the odds of this being a simple natural accident were slim.

From what we had heard so far, more than one boatman had died. The old boatman’s next words made the situation seem even more suspicious.

“Come to think of it, all the dead boatmen disappeared in roughly the same area. Hm? Wait a moment. The place you honored guests are heading toward is nearby too…”

The old boatman suddenly froze and slowly raised his head.

He looked us over one by one without a word, then quietly lowered the oar he had been holding to set off and stood up.

“Where are you going?”

At my question, the old boatman gave an awkward smile.

“Well, I seem to have forgotten to relieve myself.”

“Mujin.”

“Yes, Captain.”

“The boatman needs to pee.”

“Does he?”

By now, Hyuk Mujin and I understood each other perfectly.

When Mujin, who was practically a giant compared to the old boatman, blocked his way, the boatman’s eyes grew moist like those of a calf being led to the slaughterhouse.

“Do you still need to go?”

At Hyuk Mujin’s low voice, the boatman shook his head.

“…Come to think of it, I don’t.”

“Good. We’ll let you go before what you’re worried about happens, so don’t worry too much.”

I felt sorry for bullying an old boatman, but we needed an experienced guide to reach the Dongting Fisherman’s refuge.

Our destination was a narrow passage through which only a few ferryboats could pass.

Even if the government mobilized a hundred ships and tens of thousands of soldiers, they would not be able to enter. They would only become a burden.

*If we end up fighting the Dongting Fisherman, bringing more people will only increase the casualties.*

The government would seal off every route connecting Dongting Lake to the Yangtze in case he tried to flee. Then a small elite force, including Cheongpung and me, would pursue him and capture or kill him.

But just as important as dealing with the Dongting Fisherman was preventing any more pointless sacrifices.

Having finished thinking it through, I abruptly spoke.

“Hyuk Mujin, Gung Gibang, Young Lady Hong. You three…”

“No.”

“Where’s that dog barking?”

“I’ll contribute what little strength I have.”

The answers came before I could finish speaking, leaving me momentarily speechless. Hyuk Mujin and Gung Gibang clicked their tongues at my expression.

“It’s obvious. Completely obvious.”

“I can see exactly what you’re about to say.”

“We came all this way. How could we turn back now? What kind of man would that make me?”

“I feel the same. The Successor Beggar of the mighty Beggars’ Sect can’t be scared off by something like this.”

“Captain, you always tell us to stay out of anything that looks even a little dangerous. That’s your defining trait. Captain’s special.”

“You’re surprisingly timid.”

“But why have you been repeating everything I say since earlier, Young Hero Gung? It’s getting seriously annoying.”

“You damned bastard. Why pick a fight when things were going so well? Have you lost your mind?”

“Beggars’ Sect special. Not content with eating discarded food at inns, you pick up other people’s words too.”

“…I’ve never seen such a bastard who’s worse than a dog.”

“Regardless, I’m going with you no matter what you say, Captain. When I was young, a gifted fortune-teller read my fate and told me I would live in wealth and glory, eating well and living comfortably until I was over a hundred. There’s no way I’m dying today.”

Gung Gibang stared at Hyuk Mujin’s boast with an incredulous expression, then shook his head.

“Fine. I shouldn’t say anything. And I agree with that idiot, so don’t even think about leaving me behind. I’ve inherited the Beggars’ Sect’s finest arts. Even if I’m not as strong as you or Young Hero Cheongpung, I have no trouble protecting this one life of mine.”

“…”

I opened and closed my mouth without managing to say anything.

In truth, neither of them was weak enough to be dismissed.

Hyuk Mujin had begun learning martial arts relatively late, yet he had grown explosively while passing through countless crises alongside me. Gung Gibang was talented enough to become the Successor Beggar, as well as a Peak master who had entered a mature realm.

*But I’m afraid.*

I was afraid of losing people close to me. Afraid that what happened that day would repeat itself.

As I hesitated, Cheongpung suddenly spoke.

“Benefactor. If you go, I can follow you to the very depths of hell.”

“Young Hero Cheongpung.”

“Please don’t say no. I am a proper man and a martial artist too.”

“Young Hero Cheongpung.”

Cheongpung gave a small smile and shook his head.

“Benefactor, please don’t say anything. You trust us as much as I trust you. That’s all we need.”

“No, that isn’t what I meant. You’re obviously coming with us, so why did you step forward and…”

“Oh. Ah…”

“Don’t say anything pointless. Sit down and don’t ruin the mood.”

“…Yes, Benefactor.”

A quiet laugh escaped me at his crestfallen expression. I nodded toward Hyuk Mujin and Gung Gibang.

“Keep one thing in mind. In every situation, follow my judgment. Even if that means obeying an order to abandon me and run.”

“Captain, that…”

Gung Gibang discreetly jabbed Hyuk Mujin in the side.

“Of course we will. Hyuk will do the same, won’t he?”

“Hm? Ah, yes.”

It was obvious what was going on, but I pretended not to notice.

I would do everything in my power to prevent that situation from arising. I was confident I could separate them before they fell into danger.

But the last person was a problem.

“You already know what I’m going to say, don’t you?”

Honglan’s red lips slowly parted.

“You will need someone who knows the exact route.”

“It’s fine. According to you, Young Lady Hong, the finest boatman on Dongting Lake is already with us.”

“What if something unexpected happens?”

“I’ll deal with it.”

“Although I am insignificant compared to you and the others, I have also reached the First Rate realm…”

“I know. And I also know that this First Rate master spent several shichen submerged in the river while holding on to a strong man, and has only been conscious for half a shichen.”

“…”

Honglan bit down softly on her lip, struck where it hurt.

She knew better than anyone.

Being able to move around as she did now was entirely different from fighting a fierce battle.

“Once again, I suppose all I can do is watch.”

“Once again?”

“Yes. Back then, long ago. Last night. And now.”

Honglan read the question in my eyes and smiled. It was more bitter than any smile I had seen from her before.

“A great many things happened before a little girl who lost her clan and her parents overnight could become the woman she is today…”

“Ah.”

“Please excuse me for a moment.”

She looked up at me with shining eyes and quietly reached out a hand.

Her pale, slender fingers brushed through my tangled hair and along my neck. My body shuddered before I could stop it.

“Young Lady Hong, what are you…”

“All done. Ah, much better. Would you like to take a look?”

I followed Honglan’s fingers with my gaze and looked down at the clear waters of Dongting Lake.

Someone’s reflection floated on the surface.

My hair was neatly arranged, held in place by a single beautiful silver hairpin.

When I raised my head, Honglan was smiling brightly.

“Benefactor—no, Great Hero Jin.”

Her hair, which had come loose at some point, swayed softly in the wind. It billowed, shimmered, and gradually seemed to grow radiant.

“I wish you good fortune in battle.”

Her quiet voice slowly faded from my ears.

With Honglan’s departing figure behind me, the boatman’s oar struck the water with all his strength.

[^1]: “Hidden Shadow Ghost” is a literal rendering of a local name for a killer said to strike without being seen.
## Chapter artifact 461

# Chapter 461

In terms of speed, a ferryboat was inferior not only to the Yangtze River Channel League’s swift ships but even to ordinary vessels. Especially in weather as foul as today’s.

*Hoooooosh, splash!*

The ferryboat rocked in the fierce wind and churning current.

A smaller hull meant less resistance to external conditions. Veins bulged on the arms of the old boatman gripping the oars.

As befitted an experienced boatman, he had guided the ferryboat skillfully despite the bad weather. But the closer we came to our destination, the more violent the current grew, and he was nearing his limit.

*This is probably too much for him from here on.*

It would have been insane to come this far relying on nothing but a single ferryboat and an old boatman.

I rolled my neck from side to side, then stepped forward.

“Shall we begin?”

At my single sentence, three people opened their eyes. They had been circulating their qi without moving an inch despite the rocking hull.

“I’m ready, Benefactor.”

“To use one of the Beggars’ Sect’s finest arts for something like this… Master would certainly have a thing or two to say if he saw me.”

“Captain. What should I do?”

Once Cheongpung, Gung Gibang, and Hyuk Mujin had replenished their qi by circulating it, I quickly gave them their orders.

“Young Hero Cheongpung, follow me to the stern. Gung Gibang, take the front. Mujin, you protect the boatman. I’ll call for you when I need you, so move the moment I do.”

As the three men moved according to my instructions, the old boatman, who had been struggling to row, blinked.

“E-excuse me, what exactly are you saying…?”

But before he could finish, the fierce palm force shot from Cheongpung’s hands slammed into the water.

*Boom! Fwoooooosh!*

“Waaaaaagh!”

The so-called palm-force booster.

Far smaller and lighter even than the sleek-hulled swift ships, the ferryboat shot into the air.

The boatman’s scream mingled with the wind that tore past us.

Using that scream as my signal, I stepped forward.

*Now.*

*Whoooosh!*

Just as the ferryboat that had risen into the air was about to settle back onto the surface, I drew up the internal energy filling my dantian and sent it toward my palms.

*Boom! Booooom!*

With my mastery of the Flame Divine Palm now at eighty percent, its heat made the surrounding air scorching hot. The ferryboat, which had seemed about to descend, sprang upward like a flying fish.

The boatman’s eyes widened. With trembling fingers, he pointed ahead.

“Reefs! There are reeeefs ahead!”

Did anyone really think the Dongting Fisherman would establish one of his secret refuges somewhere easy to reach?

The route we were taking was too narrow for ordinary vessels to enter. The current was also unusually strong, making it difficult for a light boat like a ferryboat to escape once it was caught in the flow.

Once the current swept a boat away, it would be easy for it to crash against one of the reefs scattered throughout the passage.

“You fucking bastards! I told you I wasn’t coming!”

At the exact moment the old boatman let out a heartfelt scream, I shouted a name.

“Gung Gibang!”

“Got it!”

Gung Gibang answered energetically and flung his sleeves, which were little more than rags.

The Eighteen Dragon-Subduing Palms, said to be passed down only to two people in the Beggars’ Sect of a hundred thousand disciples—the Beggars’ Sect Leader and the Successor Beggar—burst through the air.

*Kwoooooo-boooom!*

Under the barrage of palm force pouring down like a rain shower, the reef standing like an iron wall shattered into countless fragments.

The second and third reefs that appeared soon afterward could not withstand the might of the Eighteen Dragon-Subduing Palms either.

*Kraaaaaash!*

The ferryboat broke through the scattered fragments of reef and landed on the surface.

Spray surged up on both sides of the hull, and several fish that had leaped from somewhere slapped the old boatman across the cheeks.

“Gah… Uhhh…”

He was completely out of it.

I shook the shoulder of the drooling boatman, whose eyes had gone half vacant.

“Wake up. Stay with us.”

“Ugh… Uhhh. You fucking…”

“This isn’t going to work. Mujin.”

“By your command.”

Hyuk Mujin rolled up both sleeves and delivered a solid slap.

*Smack!*

The boatman’s eyes refocused.

“Gah! What was that for?”

*Smack!*

“…But I was already awake.”

“Stop.”

“Yes, sir.”

Nothing brought someone to their senses like a good slap across the face.

I asked the boatman, who was rubbing his reddened cheeks,

“About where are we?”

“No matter how honored you are, how can you treat a person like this…?”

“Mujin.”

“By your command.”

“I’ll check right away, sir.”

The boatman sprang to his feet and looked around.

The river was narrow enough that only two or three ferryboats could barely pass through at once.

Sheer cliffs rose on both sides, while violent currents swirled across the surface. Thick fog hung over everything.

The old boatman narrowed his eyes and examined the area carefully before nodding.

“Yes. This is the first of the places you mentioned.”

According to the Lower District Sect’s information, which Honglan had passed on to us, there were five locations considered likely to be the Dongting Fisherman’s refuge.

The place we had reached was the closest of them.

It was certainly good news, but it was too early to celebrate.

“Coming here quickly is great and all, but… how are we supposed to find it now?”

At Gung Gibang’s question, I scanned our surroundings and answered,

“I don’t know. The information Young Lady Hong gave us wasn’t exact, either. We’ll have to search the area thoroughly.”

“Ugh. This is going to take forever.”

“Don’t say such unlucky things. At least be grateful that Young Lady Hong’s information got us this far.”

A secret refuge wasn’t called a secret refuge for nothing.

Honglan’s information had not given us its exact location, but merely narrowing down the Dongting Fisherman’s unknown hideout to this area was already a major gain.

Even if we came up empty-handed at the first location, we would eventually catch something if we kept narrowing the net.

*Or it might jump out on its own before we catch it.*

As I kept a close eye on our surroundings, I suddenly felt a prickling sensation on my face.

I turned my head slightly. The four pairs of eyes staring at me with strange expressions immediately darted away.

“What?”

“W-what are you talking about? I was just… I thought it was nice that you were thinking about Young Lady Hong even in the middle of all this.”

“Ahem. Captain, you have my support.”

“Ah, youth is a fine thing. I was popular with the ladies myself until about thirty years ago. They once called me the Dongting Lake Heart-String Fisherman. Hahaha.”

“…”

I knew perfectly well what they were thinking.

I was inwardly clicking my tongue when my eyes happened to meet Cheongpung’s. He flinched like a bird that had been shot and waved both hands.

“No! No, Benefactor! I wasn’t thinking about anything!”

“What on earth were you thinking about? I haven’t even said anything yet.”

“Really, I wasn’t! I swear I wasn’t imagining Young Lady Hong and Benefactor falling madly in love, getting married, having two children, and living happily ever after! I wasn’t imagining myself living next door to Benefactor and visiting you often, either!”

“…”

“Gasp!”

Only then did Cheongpung realize his mistake. He clapped both hands over his mouth, but it was already too late.

*He imagined all that in the space of a few seconds?*

At that level, he could quit being a martial artist and become a novelist.

His pen name would be Huashan Divine Dragon. If he published it under the Huashan Sect’s name and got Sword Saint Mae Jonghak to write a blurb, it would sell like hotcakes.

Of course, if he made me the protagonist, he would get the shit beaten out of him just as quickly.

“Good grief. What is wrong with you people…? Never mind. Forget it.”

There was no point in talking. My mouth would only hurt.

I sighed and quickly issued new orders—not because my face had felt inexplicably hot for some time, and not because the faint scent clinging to Honglan’s silver hairpin kept brushing against the tip of my nose.

*…Really.*

“Young Hero Cheongpung and Gung Gibang, use the Wall Lizard Technique to search the cliffs. Mujin, circle around in the boat and search below. We don’t know what might appear or when, so don’t let your guard down for even a moment.”

At my serious voice, the faint smiles at the corners of everyone’s mouths vanished as though they had been washed away.

If the Dongting Fisherman really was here, a battle would be unavoidable.

I did not know exactly how powerful he was, but if a Supreme Peak master of the Dongting Fisherman’s caliber launched a surprise attack, Cheongpung and I were probably the only ones who could properly meet it.

“Keep this in mind. If you let your guard down, you die.”

Of course, we would do everything in our power to prevent that from happening. But in the world of martial artists, life and death could be decided in an instant.

I turned away from the people nodding heavily, but Hyuk Mujin suddenly spoke.

“What are you doing?”

“We’re searching together. Did you think I was going to sit around and have fun by myself?”

“No, that’s not what I meant. Weren’t you planning to stay on the ferryboat?”

“Cheongpung and Gung Gibang are covering the cliffs, and you’ll be down below, so I have to search somewhere else.”

“Somewhere else? What else is left…?”

Hyuk Mujin stopped mid-sentence.

“Could it be?”

“That’s right.”

I looked down at the churning river and said,

“We have to search underwater too. If it were anyone else, I might not consider it, but this is the Dongting Fisherman’s refuge. It’s a perfectly reasonable possibility.”

“But you’ve never learned water arts, have you?”

“Hmm. I don’t think so.”

At my confident answer, Cheongpung and Gung Gibang, who had been about to climb the cliffs with the Wall Lizard Technique, added their own comments. Even the old boatman, who had raised his oar as if it were a weapon, joined in.

“Benefactor, my grandfather told me that one must absolutely avoid fighting a master of water arts underwater.”

“I agree. You haven’t learned water arts, so you can’t search this entire stretch. And if your opponent is the Dongting Fisherman, you should avoid it all the more.”

“I know that you’re a skilled martial artist, honored sir, but the water is deep here and the current is strong. If you make even one mistake, you could truly be in grave danger.”

There wasn’t a single flaw in any of their arguments.

Battles between Supreme Peak masters could be decided by one tiny detail.

And the difference between fighting on land and fighting underwater was like the difference between heaven and earth.

*The martial arts I’ve learned are especially vulnerable underwater, too.*

Most of the Fire Gate Clan’s martial arts were based on Scorching Yang Qi—in other words, fire qi.

By their very nature, those martial arts could not help but lose power underwater compared to their performance on land.

That was also why Jeok Cheongang hated the Yangtze so much. He knew that if a life-and-death duel took place there, it would be a battlefield disadvantageous to him.

“…”

Hmm. I take that back. Thinking about it again, he probably just hated water itself.

Regardless, it would not have been particularly surprising if the Dongting Fisherman had established a secret refuge underwater, away from other people’s eyes and footsteps.

He was a master of water arts who could breathe like a fish and move even faster than one.

But I had not stepped forward without a plan.

My entire swimming career consisted of the children’s swimming class I had attended when I was seven. There was another reason I had decided to enter those deep, raging waters.

*I haven’t used it even once yet, but if the explanation is accurate, it should be more than possible.*

I let out a short breath and removed my shirt and shoes.

Before Hyuk Mujin could stop me, startled by my sudden action, I jumped straight into the river.

*Splash! Whoooooosh!*

The water was as cold as ice, and crystal clear at the same time.

Schools of brightly colored fish swam together. Far below, unidentifiable aquatic plants swayed in the depths.

And then… at last, the sound I had been waiting for rang out.

*Ding. Ding. Ding.*

> **System**
>
> - The **Water Rescue Worker** Title’s effect has activated!
>
> - The special Skill embedded in the Title has been applied!
>
> - **Water Rescue Worker’s Webbing** has been generated!
>
> - **Water Rescue Worker’s Gills** have been generated!
>
> - The special Skill will last for 24 hours and cannot be used again for the next week!
>
> - The martial arts you have learned are incompatible with the surrounding environment. When using **Fire Gate Clan** martial arts underwater, their power is reduced by 20 percent!

At the same time as the System notification, changes began around me.

*Shhhhhhh.*

A faint light visible only to me swept across my entire body. Transparent webbing formed between my fingers and toes.

*What is this…?*

Even though I was underwater, my movements felt as light as they did on land.

My vision grew even clearer. When I exhaled the breath I had been holding, the cold water turned into air and rushed into my lungs.

*The effect is even better than I expected.*

I had never imagined that the Title I had earned after completing the sudden Quest *The Tragedy of Dongting Lake*—**Water Rescue Worker**—would become useful so quickly.

*This is more than enough.*

Grinning, I began to swim smoothly.

I cut through the fierce current with my transparent webbed feet and moved toward somewhere in the distance at a speed faster than a fish.
## Chapter artifact 462

# Chapter 462

The old boatman could not believe the reality unfolding before him.

*What in the world is going on?*

He had worked as a boatman for nearly forty years, ever since he had been around twenty. In all that time, he had never experienced anything as bizarre as today.

*Tap-tap-tap-tap!*

Two figures raced across the sheer cliff above him. It was not the first time he had seen them today, but the sight still amazed him every time.

The boatman stared upward with his mouth hanging open.

*Are those apes or people?*

He had encountered countless martial artists during his years as a boatman, but this was the first time he had ever witnessed martial arts of such astonishing caliber firsthand.

Most martial artists who used his ferryboat were wandering martial artists with mediocre skills and shallow pockets, or disciples of small and middling sects.

*I had my suspicions when the government troops suddenly showed up and ordered me to follow them…*

He had seen it clearly: Officer Gwak, who was in charge of Dongting Lake, had been visibly flustered as he addressed these people with honorifics.

Considering how arrogant the man usually was, there was no doubt that today’s passengers were important figures who carried considerable weight even in the Murim.

*If things go well, I might be able to make a tidy sum.*

He had been considering retirement lately. Whenever he heard about the nonstop tragedies of the past month, unease had settled in one corner of his heart, and his old bones had begun aching more than usual.

He had nearly made up his mind after hearing that hundreds of people had been slaughtered en masse on Dongting Lake the previous night.

*The spirit of Dongting Lake must have grown enraged. The heavenly patterns are ominous, so evil spirits like the Hidden Shadow Ghost are running wild.*

Boatmen were famous for believing in all sorts of superstitions, and old men were prone to retelling legends as though they were facts.

It was only natural that a man who had spent his entire life as a boatman—and had grown old doing it—would decide to retire.

But if important people were calling for him, what choice did he have? When they had dragged him away like a criminal and ordered him to launch the ferryboat, he had been prepared to die.

*Tap-tap-tap-tap!*

But seeing those figures filled him with hope.

Hope that he could survive, of course, but also hope that he might make enough money to retire in comfort.

*They must possess incredible martial arts!*

They said martial masters of the highest realms could fold the earth beneath their feet and walk through the air.

What those people were doing was not much different from the rumors the old boatman had heard secondhand.

Even the young man who appeared to be their leader was charging through the rough water as though he were a fish.

*No, that’s not right. This is already the fourth location. He isn’t fish-like—he’s an actual fish.*

What kind of human being had webbed feet and gills? Every time that young man went underwater, he stayed there for at least one full shichen.

He had already repeated that impossible feat three times. If anyone deserved to be called a martial master, it was him.

*Masters like these could deal with some miscellaneous Fiend like the Hidden Shadow Ghost in an instant.*

If he could only make it out alive, retiring with a fortune would be easy.

Just as the old boatman was brimming with hope, a shout rang out from the cliff above.

“Young Hero Cheongpung! Did you find anything?”

“I’ll tell you when I see something!”

“If you discover anything, tell us immediately!”

“Yes, I certainly will… Ah!”

“Gasp! What is it? What happened?”

A heavy tension abruptly settled over the area.

Hyuk Mujin, who was scanning the surroundings from the slowly moving ferryboat, swallowed hard. So did Gung Gibang, who was watching the opposite cliff with sharply gleaming eyes.

Then, under everyone’s gaze, Cheongpung shouted,

“Wow, it’s a swallow’s nest! I’ve never seen one this big before!”

“…”

“…”

“…”

The air froze solid.

The boatman suddenly thought,

*…Spirit of Dongting Lake, please protect this old man.*

Seeing the people above, he was about to lose what little faith he had left.

That was when it happened.

*Whooosh! Splash!*

A shadow shot out of the water amid a spray of droplets and landed lightly on the ferryboat.

The figure had a build large enough to be called massive, with flexible yet seemingly steel-hard muscles. A beautiful silver hairpin that suited him strangely well held his disheveled hair in place.

“Welcome back.”

At Hyuk Mujin’s greeting, Jin Taekyung silently nodded.

His brow was furrowed. The old boatman cautiously asked,

“Nothing this time either?”

It was a pointless question. If he had discovered something, his expression would not have been so dark.

Jin Taekyung remained deep in thought, his brows drawn together, before opening his mouth.

“This is the fourth location, right?”

“Yes, that it is.”

The old boatman answered, but he could not help watching Taekyung’s mood.

These incredible passengers had already come up empty-handed three times. Including this place, they had failed to find anything four times in total.

Riding in the same boat as martial masters who were clearly in a foul mood was hardly pleasant.

The one thing that was both fortunate and unfortunate was that one final location remained.

*Fwoosh. Hissss!*

Jin Taekyung lightly circulated his internal energy, evaporating the water clinging to him, and asked,

“How long do you think it will take to reach the final location?”

“If we continue at the pace we’ve kept so far, about half an hour should be enough. But…”

The old boatman swallowed before continuing.

“The wind and current are growing stronger the farther we go. It’ll be starting to get dark by the time we arrive, so perhaps it would be better to try the next day.”

“No. It has to be today.”

“But, surely…”

“We have to go. Right now.”

His tone was as decisive as a blade slicing through something. The old boatman closed his mouth.

For some reason, the weather today was ominously foul. The sky, which should have been clear, was filled with dark clouds, while the fierce wind and current showed no sign of settling down.

*I’ve got a bad feeling about this.*

The foreboding he had felt only in the past, when floods or storms were bearing down on them, pricked at every inch of the veteran boatman’s body.

But he forced himself to ignore the unease seeping into his chest.

*Have I grown timid with age? That can’t be it.*

A sudden flood or storm? It made no sense.

Boatmen like him were more sensitive to changes in the river than anyone.

The current had certainly grown unusually rough over the past month, but it was not the rainy season. A disaster of that scale was impossible.

The boatman was still considering it when he realized that a large hand had settled on his shoulder.

“Boatman. Aren’t you going?”

“…I’m going.”

At Hyuk Mujin’s weighty voice, the boatman slowly began adjusting the ferryboat’s course.

Of course, he did not forget to curse inwardly at the rude fellow who looked like the weakest of the group.

“Boatman. Were you cursing me just now?”

“……!”

The boatman’s oar slipped, and the ferryboat rocked.

The rapids had grown even rougher than when they first set out, dragging at the small hull. Jin Taekyung stepped forward and swept both palms outward.

*Boom!*

The ferryboat regained its balance and surged ahead.

As Taekyung gazed at the sky slowly darkening above them, his eyes sank deep.

*Did we get the wrong place?*

The information Honglan had passed on from the Lower District Sect pointed to five locations in total.

But even after searching thoroughly both in and out of the water, they had found no trace that could be called the Dongting Fisherman’s secret refuge.

After coming up empty-handed one place after another, it was only natural to wonder whether the information had been wrong from the beginning.

Taekyung thought for a moment, then shook his head.

*No. It’s too early to decide that.*

One final place remained. Of the five locations suspected to contain the Dongting Fisherman’s secret refuge, it was the deepest and most treacherous.

It might even have been more important than the other four combined.

If it really was the Dongting Fisherman’s refuge—and if they encountered him there…

*It’ll be a life-and-death duel. We’ll have to fight with our lives on the line.*

Against a Supreme Peak master, giving one’s all was only natural. But Taekyung had to capture him without killing him if at all possible.

The true reason he was searching for the Dongting Fisherman was to reach the larger body behind him.

Dark Heaven was practically a three-headed, six-armed monster. Killing the Dongting Fisherman would be like cutting off one of its arms. Capturing him would let them strike at its body.

“The body. The body, huh…”

His quiet mutter scattered into the wind.

Without realizing it, Taekyung touched the silver hairpin holding back his hair and suddenly thought of one person.

He also remembered the hundreds of corpses that had filled the clear waters of Dongting Lake, and the wails of those left behind.

“I’ll catch you. Every last one of you bastards.”

A faint fragrance drifted from the silver hairpin and lingered at the tip of his nose. At the same time, the bow of the ferryboat forcefully split the river, which had begun turning black.

* * *

Donghu Stronghold.

The largest water stronghold in Hubei, which had once wielded tremendous influence under the command of the outstanding Supreme Peak master Hwang Chung, the Yangtze One Saber, had been crowded with unfamiliar visitors since two days ago.

“Pull when I count to three. One, two. Heave!”

Some people were tying logs together to make a makeshift path across the river. Elsewhere, middle-aged men dressed in neat scholar’s robes were writing something on bamboo slips.

A young Daoist wearing a robe approached one of them and asked,

“Excuse me, sir. Has the search of the left cliff already been completed?”

“About half of it. I can stake our family name on the fact that we haven’t found any trace of a Formation so far. How is Wudang doing?”

“It is progressing smoothly. We are also maintaining a strict watch in case anything unexpected happens, so you need not worry.”

They were the Zhuge Clan’s disciples, known collectively as Divine Mechanism Zhuge. The others were Daoists from Wudang who had accompanied Perfected Being Hyeongong to Donghu Stronghold.

These unfamiliar visitors, who had been nowhere to be seen two days ago, had formed groups and were searching the cliffs, devoting all their efforts to finding traces of Dark Heaven.

But even with countless eyes and ears spread throughout the area, and bright torches burning everywhere, they failed to notice one person.

*Swish.*

His movements made no sound and left no trace.

The small, lithe figure quietly and stealthily headed toward the cliff. He passed dozens of people at the very least, yet not one of them noticed who he was.

The same was true of the Ghost Illusory Slaughter Step, performed by the greatest assassin in history.

*What a nuisance.*

Mungyeong muttered inwardly as he stepped forward.

He stepped on empty air and leaped like a bird, his figure quickly sweeping across the cliff.

The stealthy search conducted by the young medical apprentice whom no one paid attention to ended soon afterward.

*Nothing. I’m certain.*

The area where Donghu Stronghold’s headquarters had been established was vast.

It was an island capable of comfortably housing more than a thousand people. High cliffs surrounded it on every side, and narrow, undeveloped paths ran along their upper reaches.

But that was all.

He could not sense a trace of human presence anywhere, nor any remnants of a Formation known as a Moving Formation.

That was the conclusion reached by a Supreme Peak master who had surpassed Returning to Simplicity and reached the realm of Returned to Youth after two days of searching.

Mungyeong trusted his judgment. At the same time, he realized that there was still one place they had not searched.

*That’s right. One place remains.*

The river visible from the cliff was unusually wide and deep.

Deep enough that even he had no desire to enter it.

*…I suppose I have no choice.*

It was a way to prevent an even greater sacrifice.

The face of the old disciple he had parted from on an unknown hill overlooking the Sichuan Tang Clan flashed before his eyes.

*All right, you rascal.*

Mungyeong quietly threw himself into the air.

His figure plunged deep into the river as though melting into it, then slid smoothly toward the depths.
## Chapter artifact 463

# Chapter 463

Deep within a dark cave where a faint light seeped in, a small old man sat cross-legged, contemplating himself.

An energy like the sun raced through hundreds of acupoints and into the Eight Extraordinary Meridians. Tangible energy rose and enveloped the old man’s entire body.

Then, the changes began.

*Whoooooosh.*

Three flower buds bloomed above the old man’s snow-white hair before soon disappearing.

As the buds formed, the scattered energy created a new shape: five rings radiating a dazzling spectrum of colors.

It was a phenomenon that could only be displayed by one of the chosen few among Supreme Peak masters who had reached the realm of Five Qi Returning to Origin.

But the changes surrounding the old man did not end there.

*Fwoosh. Hissssss!*

The five rings symbolizing Five Qi Returning to Origin turned red. Tremendous flames erupted from the rings of internal energy filled with Scorching Yang Qi, wrapping around the old man before soon taking on a blue hue.

Furnace Fire Pure Blue.

When the fire in a furnace grew hot enough, it turned blue. The realm of martial arts the old man had achieved was the same.

It would not have been an exaggeration to say that the internal energy and insight he had accumulated over more than a hundred years had already reached the ultimate.

And yet…

*Is this as far as I go?*

The old man, Fire King Jeok Cheongang, withdrew his internal energy. The figure that had been floating cross-legged in the air descended until his body touched the ground, and the strange phenomenon surrounding him vanished as though it had been washed away.

The only thing left in the quiet space was Jeok Cheongang’s hollow chuckle.

“Heh heh.”

Why could he not break through the wall before him and advance any farther?

Because he knew that fact better than anyone, Jeok Cheongang nodded, yet the unmoving wall still seemed bitterly unfortunate. At times, he even resented the heavens.

But instead of furrowing his brow, Jeok Cheongang soothed his bitterness with a laugh.

*What is there to resent? This old man brought it upon himself.*

Martial arts grew stronger through ceaseless training, while insight only came when one emptied the heart.

But Jeok Cheongang had been unable to clear away the filth that had accumulated in his heart over the past several decades.

Anything that piled up and stagnated would eventually rot. With his rotting heart filled with afflictions, an inner demon had come for him, and once the inner demon arrived, he could no longer prevent the infirmities of old age.

“If I hadn’t met that brat… I’d probably be smearing shit all over the walls by now. Heh heh.”

Jeok Cheongang let out a hearty laugh.

With one realization—just one small realization—he might be able to reach the realm of Returned to Youth.

But he knew that this, too, was greed. It was proof that he had not completely emptied his heart.

When he suddenly looked up, he saw the sky through a small opening. Jeok Cheongang spoke to someone invisible beyond it.

“Does this mean I should be satisfied with this? Is that right?”

No answer came back.

No… Perhaps he had already received his answer.

He had taken a killer demon by nature as his disciple and allowed innocents to die. But thanks to his second disciple, he had at least been able to preserve his sanity. The answer was that he should no longer cling to anything.

There was no one to give him that answer, yet Jeok Cheongang heard it coming from within his own heart.

“What a fucking joke. After all the fiends this old man has dealt with, this is the shabby treatment I get?”

Jeok Cheongang sighed in complaint and lowered his head before continuing.

“Don’t you think so?”

One person stood at the end of Jeok Cheongang’s gaze. Crouching Dragon Guest Zhuge Feng answered while waving his folding fan.

“Once, when I was nine, my grandfather sat me beside him and said something similar. ‘I don’t know what kind of bastard is up there, but he must have a truly god-awful temper.’ Senior, you’re saying the same thing now.”

Jeok Cheongang nodded.

“Zhuge Gonghu did occasionally say something right.”

“He was a wise man.”

“He was smarter than you, of course. At least he didn’t wave his fan insolently in front of someone old enough to be his grandfather. Fold that thing before I break it.”

“It is not an object that breaks easily. I put two nyang of Ten-Thousand-Year Cold Iron into it.”

“Is your skull made of Ten-Thousand-Year Cold Iron too?”

“Ah, I see. Thank you for the instruction.”

Zhuge Feng promptly folded his fan, then looked around the cave and spoke.

“But what brings you here? The search has already ended, and no one comes here anymore.”

“That is precisely why I came. I’m no expert when it comes to mechanisms and formations, so I need to make preparations in my own way.”

At the word *preparations*, Zhuge Feng’s brow rose slightly.

“You think a battle will break out.”

“A martial artist should always prepare for a fight. Besides, those bastards from Dark Heaven are cruel, lawless, and persistent. This will not end here.”

Jeok Cheongang’s voice was heavy.

Dark Heaven had taken the life of his close friend, Dharma King Hong Dao.

The countless deaths caused by the bloodshed in Henan and Sichuan were more than enough to remind him of the Great Faction War.

“I assume you know that the Heavenly Power Demon was imprisoned in the underground prison beneath the Sichuan Tang Clan.”

“Of course. I also know that, through Young Hero Jin, he called Dark Heaven the successor of the Demonic Cult before meeting his death.”

The Great Faction War, fought over supremacy in the world, had ended with victory for the orthodox factions. But it had not been a sweeping victory. It had been a victory marked only by wounds.

If the orthodox factions of that era had retained enough strength, they would have pursued the retreating armies of the Demonic Cult and torn out every last one of its roots.

But the Heavenly Demon Divine Cult and the orthodox factions—the two great powers, like a dragon and a tiger—had lost most of their strength as soon as the war ended. And the long gap of more than fifty years had been enough time for the defeated side that escaped to rise again.

Under a new name.

Dark Heaven.

“Time has passed like this before we even realized it. The wheel has turned, and troubled times have come again.”

At Jeok Cheongang’s quiet voice, Zhuge Feng suddenly looked up.

The sky visible through the gaps in the cave ceiling was dark and chaotic. Even if the black clouds vanished tomorrow and the sky cleared to blue, the heavenly patterns had already been thrown into such disorder that no diviner in the world would be able to read them.

*Troubled times.*

The age of turmoil had finally returned after completing its long circle, and the era of calamity had already reached their doorstep.

Blood would form rivers, and corpses would pile up like mountains.

Death and destruction would be carried out everywhere. Orphans who had lost their parents would wander the world, while epidemics and famine would spread because there would be no one to dispose of the rotting corpses.

*What is happening now is only a small part of it.*

Zhuge Feng realized that fact once more and felt a chill run over his skin.

But Dark Heaven’s existence was not the only reason.

“I see you already had a guest.”

A voice pierced his ears.

Zhuge Feng froze on the spot as though someone had poured ice water over him.

*How?*

Although he had not reached the Supreme Peak realm, Zhuge Feng was still a master at the very edge of Peak.

Yet he had sensed no presence. He had heard no sound.

Even though he had left three guards who followed him like shadows at the entrance to the cave, he had noticed no sign of anything.

That meant the owner of the voice was at least a Supreme Peak master.

*If he is that kind of master…*

Aside from Jeok Cheongang, the only possibility was Perfected Being Hyeongong of Wudang.

But the voice he heard was far too young and clear.

It sounded almost like a boy’s voice.

*Ah.*

With a flash of insight, Zhuge Feng turned around.

The instant he saw the young medical apprentice he had encountered several times in passing, the fog filling his mind scattered, and a sobriquet slipped from between his lips.

“The Slaughter Saint.”

The young medical apprentice, Mungyeong, twitched an eyebrow.

“You already knew?”

“I did not. Not until just now.”

Zhuge Feng continued in an excited voice.

“But I have always wondered why the greatest assassin in history disappeared. I also wondered why the exceptional physician known as the Divine Physician only appeared after the Great Faction War ended.”

“Not bad.”

“I once watched you closely, but I never imagined that you had reached the realm of Returned to Youth.”

The Slaughter Saint was an unknown figure about whom almost nothing was known.

Zhuge Feng stared at Mungyeong with gleaming eyes before suddenly hesitating.

“But why would you deliberately reveal yourself to me… Unless?”

“You’re quick to notice things. You really are a member of the Zhuge Clan.”

“You can’t fool blood, after all. He may be a little strange, but he’s a clever boy. Zhuge Gonghu raised his grandson well. Now, putting that aside…”

Jeok Cheongang shrugged and continued while staring at Mungyeong.

“What brings you here? Why has an old man who had been pretending to be a child, despite it not suiting him at all, come here in such a hurry?”

“I’ll keep it short. You must leave this place immediately.”

“What?”

As Mungyeong had said, his words were extremely brief.

And to Jeok Cheongang, they were nowhere near enough reason to cross that godforsaken Tianling Falls.

“What kind of bullshit is—”

“I should make it even shorter.”

Mungyeong continued in a deeply sunken voice.

“Your disciple is in danger. No. Perhaps everyone is.”

“……!”

The moment he heard those words, Jeok Cheongang realized that he needed no further reason.

He turned his head toward Zhuge Feng. Blue flames had already kindled in his aged eyes.

“Launch the boat. Right now.”

* * *

By the time we reached the final location, the waters of Dongting Lake had turned purple.

I looked at the sunset shining through the gaps between the cliffs and strange, jagged rocks before speaking.

“Don’t move recklessly from now on. Tie the ferryboat somewhere safe, then move overland and prepare for anything.”

Dongting Lake was a lake, but it was so vast that calling it a lake hardly seemed adequate.

It wasn’t all water in every direction; small islands and flat stretches of ground formed from mud and sand carried in by tributaries of the Yangtze were easy enough to find.

*If a battle starts, it will be much more advantageous to fight on land.*

Not one of us had mastered water arts.

I could at least move freely underwater thanks to the Water Rescue Worker Title’s effect, but I could not avoid the debuff that reduced my martial arts’ power by twenty percent.

*If the situation turns bad… I need to be able to respond from land, at the very least.*

The others understood my thinking perfectly well.

Gung Gibang spoke with a determined expression.

“I’ll go with you.”

“Can you swim?”

“I can dog-paddle a little.”

“Go to land before you get beaten like a dog.”

“Hmm. That probably is better.”

Gung Gibang stepped back, and Hyuk Mujin came forward.

“Captain.”

“You stay on land too. Hide and keep out of trouble. You won’t be any help if you charge in for no reason.”

“I know. I only called out to encourage you.”

“……”

What a sibu-leol bastard. I felt like even the little strength I had left was draining away.

I let out a small sigh, then gave Cheongpung one last earnest warning.

“The Dongting Fisherman may or may not be inside. But if I find him and drag him outside…”

Cheongpung nodded.

“I won’t miss the opportunity.”

“Good. That’s all I need.”

I did not know how formidable the Dongting Fisherman was, but with Cheongpung’s help, things would be much easier.

*Of course, he might not be here either.*

But how should I put it? This time felt different.

It was not a matter of reason. It was instinct.

I looked at each person in turn, then leaped without hesitation into the purple water.

*Splash!*

Along with the familiar sensation, a System notification rang out.

In accordance with the Title’s effect, transparent webbing formed between my ordinary fingers and toes, and breathing became effortless.

*Deeper. Further in.*

I continued forward without stopping.

I swam rapidly through the cold water and past countless fish.

Then, just as I was moving through the depths, something appeared in the distance.

*What’s that…?*

Far ahead, a pitch-black cave came into view.
## Chapter artifact 464

# Chapter 464

Dongting Lake was unquestionably a lake, but its total area alone stretched for a thousand *li*, and even its shallowest points easily exceeded a dozen *zhang* in depth.

The place I was swimming through now was one of the deepest parts of Dongting Lake. Naturally, the water was much deeper here, and the current raged like waves.

Finding a small underwater cave under these circumstances was practically an act of heaven’s grace.

*That’s…*

Amid countless fish swimming in schools, I spotted a gap barely wide enough for a full-grown man to squeeze through.

At the same time, a thrill ran down my spine.

*I found it.*

Cliffs rooted deep in a riverbed naturally split apart over the years through sedimentation and erosion. I had seen it several times at the four places we had already visited.

But this time was different.

My reason and instinct, which usually went their separate ways, were whispering the same thing.

*The Dongting Fisherman’s secret refuge.*

Everything left traces.

Though the difference was extremely subtle and well hidden, my accumulated experience and keen eyes told me that human hands had touched the entrance of the cave slowly drawing closer.

*The edges of the entrance are smooth. Someone definitely worked on them.*

There was no need to ask who that someone was.

I heightened every one of my senses to their limit and cut through the current.

Slowly. Carefully.

It would be stupid to announce my presence to an enemy with whom I would soon be locked in a life-and-death duel.

If he prepared himself, the situation would become even more unfavorable.

*Fortunately, there’s still plenty of time left on the Title’s effect. No need to rush.*

I had seen plenty of people hurry to arrive ten minutes earlier, only to arrive fifty years early.

Whether a person lived or died depended on their will and perseverance. I did not hurry. I let the current carry me along.

*Swish.*

The brilliantly colored fish that noticed me seemed to hesitate, then cautiously brushed past me.

Since I was barely moving, they must not have sensed me as something that posed a threat.

*Good.*

If a fish this close could be fooled so easily, it was enough. I suppressed my presence even further and approached the cave.

I took a small breath in front of the entrance, which was just large enough for one adult man to squeeze through, then pushed my body inside.

Another underwater passage hidden beyond it came into view.

*No presence so far.*

The passage, no wider than the entrance, was deeper and longer than I had expected.

I sharpened my senses more than ever and searched the passage for any human presence. Only after I was certain there was none did I begin moving again.

I passed several strange-looking fish and aquatic plants. How far had I gone?

A faint light was approaching from far ahead.

*Wait. Light?*

This was underwater in Dongting Lake, but it was also a passage inside a cliff. How could there suddenly be light?

The passage did angle upward, but its structure left no way for light to leak in.

*Then…*

I swam gently toward the light, searched my surroundings once more, and finally shot upward toward a small hole in the ceiling of the passage.

*Splash!*

I sucked in a breath.

Damp air seeped deep into my lungs.

At the same time, I felt the transparent gills that had formed around my throat disappear.

The next moment, I emerged from the water and finally saw the source of the faint light. My eyes widened.

*Night-shining pearls.*

It was a cave.

The path stretched into the distance, narrow and dark. Large and small night-shining pearls were embedded at regular intervals across the ceiling, which was only high enough for me to barely straighten my back.

*A submerged passage and a cave carved inside a cliff. Night-shining pearls, too… At this point, you’d have to be an idiot not to know.*

The Lower District Sect’s information had been correct. This was unquestionably the Dongting Fisherman’s secret refuge.

My heart pounded with the thrill of finally finding him and the tension of the battle that would soon begin.

No. It was not just those emotions.

*That.*

I turned my head, following a strange smell that worked its way into my nose, and saw them.

A piece of wood lying facedown on the waterlogged floor of the cave, and oil floating on the surface of the water.

*A torch? Well, it’s not like he has an unlimited supply of night-shining pearls.*

The night-shining pearls embedded in the ceiling were obviously low quality, but that did not mean they were cheap.

I had never heard that the Dongting Fisherman was a tycoon, so torches must have been essential for lighting this long cave.

And that half-burned torch told me something important.

*It hasn’t been out for long.*

A faint warmth remained in the piece of wood. It was not difficult to infer that the torch had fallen for some reason only one or two *shichen* ago.

There was also one fact this situation pointed to.

*The Dongting Fisherman is definitely here!*

In the end, the person I wanted to find was not a place but a man. Even if I found his secret refuge, it would be useless if the Dongting Fisherman was not there.

But through the torch, the Dongting Fisherman had revealed his presence.

Even if I were in his position, I would never have expected an intruder to enter a secret refuge hidden this well.

*That’s your mistake.*

I rose to my feet and began walking slowly along the path stretching out before me.

I had plenty of high-performance equipment, including White Flame, which could be called my favored weapon, Fire Dragon Armor, and the Myriad-Poison Ring. But now was not the time to bring them out.

It would be better to make my opponent lower his guard by showing him that my hands were empty, then take advantage of the benefits my Inventory offered.

*Drip. Drip-drop.*

Listening to the irregular sound of water dripping from the ceiling, I walked on and on with my presence suppressed as much as possible.

The path, straight at first, began to twist. Inclines and declines appeared as well, but I never let down my guard.

*But… What are these traces?*

It did not take long for me to sense that something was strange.

My sharp eye was part of it, but the state of the passage was that abnormal.

Sections of the walls had been smashed and broken here and there, with rocks jutting out abruptly. Unlike the other places, which were covered in green moss, the freshly broken sections stood out unmistakably.

*Thud-thud.*

When I touched it, part of the wall immediately crumbled and fell away.

*This would be impossible without applying force deliberately.*

The entire cave consisted of solid rock that had accumulated over at least several hundred years.

To damage it, someone would have to strike with a considerable amount of internal energy. But was there any reason for the Dongting Fisherman to destroy his precious refuge himself?

*Could there have been a battle here…? No. No, this is definitely the trace of a single person.*

I was still far from having the insight to discern the nature and roots of martial arts, but having reached the Supreme Peak realm, I had little trouble inferring what had happened from the traces left throughout the passage.

I furrowed my brow and thought deeply for a moment before shaking my head.

*I need to focus on the Dongting Fisherman first. Careless complacency and excessive tension are both forbidden.*

I kept repeating that to myself as I continued walking.

Then it happened.

*Splash! Whoosh!*

“……!”

The sudden sound snapped me to attention like a person doused with cold water.

The senses spread wide across my entire body analyzed the sound, then sent new information flowing toward my brain.

*Fifty-odd zhang ahead. Closer than I expected.*

On top of that, the sound echoed unusually deeply and loudly. That meant there was a larger space ahead, not merely this narrow cave passage I was walking through.

*Swish.*

One step. Then another.

I focused every nerve in my toes as they touched the damp cave floor.

It was a blessing that I had used my Scorching Yang Qi beforehand to dry the water that had soaked me through. If water dripping from my body had struck the floor and made a sound, the Dongting Fisherman would have discovered me.

*I have to finish this in the cave. Fighting underwater would make things much harder.*

My opponent was a Supreme Peak master of water arts, one of the best in the world.

I had confidence in my own martial prowess, but if I fought the Dongting Fisherman underwater, I would have to bear the full twenty percent reduction in power the System had warned me about.

But this was solid ground—firm land—and that meant there was no debuff.

*I can’t let this opportunity slip away.*

The fifty-odd zhang between us rapidly narrowed.

*Tap. Whoooosh.*

The incomprehensible sound continued to reach me, serving as an excellent landmark that revealed the distance and direction in real time. As I came to a bend in the cave passage, I relaxed every muscle in my body.

I was ready.

Dozens of images flashed before my eyes, showing how I would move and how I would finish him.

If the Dongting Fisherman proved too formidable, I would kill him with everything I had. If not, I would capture him and use him to draw out the bigger player behind him.

*I’ll end it in one stroke, like a bolt of lightning.*

With a short breath, I awakened the fire dragon sleeping deep within my dantian.

The three *jiazi* of Scorching Yang Qi I had continually replenished through circulation flowed into every limb and bone of my body.

I infused hundreds of acupoints and the Eight Extraordinary Meridians with searing heat, maximizing every physical ability.

And then…

*Pop!*

One step was enough.

I gently stepped onto the slanted wall and shot forward.

A space roughly thirty *zhang* in radius, presumably the center of the cave.

Toward a white-haired old man crouching with his back turned to me.

*The Dongting Fisherman!*

A silent cry rang out within me.

It was hard to believe that this small, shabby old man had harmed so many people. The anger I had buried for a while surged up as a cold flame.

*Inventory open. Summon!*

As the world slowed, the unknown power of the System covered my entire body as I charged toward the Dongting Fisherman.

*Swish. Clack.*

Red armor wrapped around my bare upper body: Fire Dragon Armor.

Then, as a cluster of light visible only to me brushed against my fingers, it transformed into the divine treasure known as the Myriad-Poison Ring. At the same time, a spear with a transparent blade appeared in my hand.

The next moment, three *jiazi* of Scorching Yang Qi seeped into all of it.

*Whoooooosh!*

The damp air vanished. The river water pooled on the floor vanished. Even the droplets falling from above vanished.

No—they evaporated.

Blue-white Force rose from White Flame’s transparent spearhead like a wildfire, burning through everything in its path.

There was one person in the direction toward which that hot and destructive concentration of energy was headed.

*Die.*

The arrow had been fired, and the bird that had been resting in its nest would not be able to escape.

To me, the Dongting Fisherman was no different from that bird.

A bird that had believed its nest was safe.

Even if it realized the truth too late, it could not stop an arrow that had already been fired.

Even if the bird hurriedly spread its wings, it could not avoid being killed or injured.

Just like the Dongting Fisherman, who was turning his body very slowly right now.

*It’s already too late.*

But the next moment, I realized something.

I should never have been so quick to assume.

*Boom!*

A snow-white streak of light flew in from somewhere and struck White Flame’s spearhead.

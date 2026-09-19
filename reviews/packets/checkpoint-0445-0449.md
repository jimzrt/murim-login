# Checkpoint Review — 445–449

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

# Chapters 445–449

## Plot

Taekyung’s group reaches the Zhuge Clan, where Zhuge Feng reveals that the Sea Serpent Society was annihilated at Red Cliffs and that the Dongting Fisherman disappeared after condemning the Yangtze River Channel League. Dangyang and Honghu Strongholds have also vanished, while Donghu Stronghold is cut off beyond Tianling Falls. Taekyung accepts the quest *Another Chaos* and joins Jin Wikyung’s investigation.

Mu Song leads Taekyung’s group, elite Zhuge and Wudang disciples, and four fast ships through the dangerously violent Tianling Falls. They reach Donghu Stronghold but find no response. Wang Pil, the Little Tide Demon and Hwang Chung’s right-hand man, is recovered dead, and the stronghold itself has been destroyed: its ships, settlement, martial artists, civilians, and children were all killed. Hwang Chung is also dead. Taekyung and Jeok Cheongang suspect Dark Heaven may have bypassed the falls using a concealed Moving Formation, but the perpetrator, motive, and connection to the Yangtze River Channel League remain unknown.

## Continuity

- Taekyung accepted *Another Chaos* to uncover the truth behind the Hubei incidents and is cooperating with Jin Wikyung, an inspector for the new Murim Alliance.
- The Sea Serpent Society was destroyed at Red Cliffs; the Dongting Fisherman disappeared after condemning the Yangtze River Channel League.
- Dangyang and Honghu Strongholds vanished after taking over Sea Serpent Society territory. Donghu Stronghold was later found completely destroyed.
- Hwang Chung, the Yangtze One Saber and Lord of Donghu Stronghold, and Wang Pil were found dead.
- The Dongting Fisherman’s broken Black Bamboo Fishing Rod remains evidence in Zhuge Feng’s possession.
- Dark Heaven’s possible use of a hidden Moving Formation is only a suspicion. The shared symbols between Dark Heaven’s formations and the Arch Lich’s magic circle remain unexplained.
- Mungyeong continues traveling with the group while concealing his former identities as the Divine Physician and Slaughter Saint.
- The Skeleton King’s undead identity remains hidden; he is being placed in Peace Guild as Stone-King, while Peace Guild negotiates with Magic Johnson’s Wizard Guild.
- Go Jun is expected to succeed Lee Jungryong as Ares Guild captain and continues searching for Lee’s holographic recorder.

## Translation Decisions

- Use “Sea Serpent Society,” “Red Cliffs,” “Dongting Fisherman,” “Yangtze River Channel League,” “Donghu Stronghold,” “Dangyang Stronghold,” and “Honghu Stronghold.”
- Render 황충 as “Hwang Chung,” 장강일도 as “Yangtze One Saber,” 소조귀 as “Little Tide Demon,” 황 숙부 as “Uncle Hwang,” 천령폭 as “Tianling Falls,” 흑죽조간 as “Black Bamboo Fishing Rod,” and 이동진 as “Moving Formation.”
- Render 현공진인 as “Perfected Being Hyeongong” and 대천성신장 as “Great Heavenly Star Divine Palm.”
- Preserve Taekyung’s dry, profane humor; Jeok Cheongang’s irreverence; Zhuge Feng’s composed directness; and the Skeleton King’s grandiose “this king” diction.
- Retain established forms of address and terminology, including “Team Leader Choi,” “Mr. Jin Taekyung,” “my youngest,” “Old Master,” “Senior,” “Peace Guild,” “Wizard Guild,” “black magic,” and “poison human.”
- Render 시부럴 as “sibu-leol,” 시벌좌 as “Lord Fuck,” and 시부럴좌 as “Lord Sibu-leol.”

## Durable state

{
  "active_continuity": [
    "Taekyung accepted the Quest Another Chaos to uncover the truth behind the Hubei incidents and find the culprit.",
    "Jin Wikyung is acting as an inspector for the new Murim Alliance, and Taekyung is cooperating with his investigation.",
    "The shared symbols between the Arch Lich's magic circle and Dark Heaven's formations remain unexplained and may relate to black magic.",
    "The Sea Serpent Society was destroyed at Red Cliffs, the Dongting Fisherman disappeared after condemning the Yangtze River Channel League, and the League is implicated only by circumstantial evidence.",
    "Dangyang Stronghold and Honghu Stronghold vanished after taking control of Sea Serpent Society territory.",
    "Hwang Chung, the Yangtze One Saber, was Mu Song's mentor-like senior and Donghu Stronghold's Lord; he was found dead after the stronghold's destruction.",
    "The Dongting Fisherman's broken Black Bamboo Fishing Rod was found, and Zhuge Feng ordered Mu Song to guide the group to Donghu Stronghold.",
    "Mungyeong remains with Taekyung's group while concealing his former Divine Physician and Slaughter Saint identity from most companions.",
    "The Skeleton King's undead identity remains concealed from the public, and Taekyung has ordered him to join Peace Guild under a prepared contract.",
    "Go Jun is expected to succeed Lee Jungryong as Ares Guild's captain and is searching China for Lee's holographic recorder.",
    "Taekyung's group survived the unusually violent Tianling Falls aboard four fast ships and reached Donghu Stronghold.",
    "Donghu Stronghold was destroyed along with its civilian population; Wang Pil and Hwang Chung were found dead, and Dark Heaven's possible use of a Moving Formation remains only a suspicion."
  ],
  "continuity_sources": [
    449,
    448
  ],
  "open_questions": [
    "What are the origin and purpose of the symbols shared by the Arch Lich's magic circle and Dark Heaven's formations, and are they connected to black magic?",
    "Why does Mungyeong continue accompanying Taekyung's group despite being unable to explain the impulse?",
    "What confidential matter is Jin Wikyung withholding?",
    "What are the terms of the Peace Guild–Wizard Guild agreement, and what evidence is contained in Lee Jungryong's holographic recorder?",
    "Who destroyed Donghu Stronghold and caused the related disappearances, whether Dark Heaven used a Moving Formation, and why the Yangtze River Channel League was targeted?"
  ],
  "safe_through": 449,
  "temporary_decisions": [
    "Render 황충 as Hwang Chung, 장강일도 as Yangtze One Saber, 천령폭 as Tianling Falls, 흑죽조간 as Black Bamboo Fishing Rod, 소조귀 as Little Tide Demon, and 황 숙부 as Uncle Hwang.",
    "Render 시부럴 as “sibu-leol,” 시벌좌 as “Lord Fuck,” and 시부럴좌 as “Lord Sibu-leol.”",
    "Preserve the Skeleton King's grandiose, mock-offended voice and Taekyung's dry, profane humor.",
    "Render 최 팀장님 as “Team Leader Choi,” 진태경 씨 as “Mr. Jin Taekyung,” 막내야 as “my youngest,” 노야 as “Old Master,” and 노 선배님 as “Senior.”",
    "Keep Peace Guild, guild house, Inventory, Magic Johnson, established martial-arts terminology, black magic, poison human, World Hunter Association, Wizard Guild, Sea Serpent Society, Red Cliffs, and Dongting Fisherman unchanged; render 현공진인 as “Perfected Being Hyeongong” and 화왕질리언 as “Fire King Zilean.”"
  ],
  "version": 1
}

## Reading copies

## Chapter artifact 445

# Chapter 445

Clack.

“Ah.”

Someone let out a small gasp.

The grandeur of the enormous library that unfolded before us when the doors opened was astonishing enough, but the doors themselves had opened without any human hand or movement of internal energy.

And as someone who had spent his entire modern life passing through automatic doors tens of thousands of times, I still found it a remarkably fresh experience.

*Some kind of machine?*

No, this was Murim. Should I call it a mechanism?

The doors that had just opened contained components made of iron and wood, all intricately interwoven into an elaborate structure.

And that wasn’t all. As I slowly turned my head and looked around the library, I saw unmistakable traces of mechanisms like the one installed in the doors everywhere.

Of course, compared to the cutting edge of modern civilization, they were crude. But there was no question that this was a sight I had never encountered in any of the other prestigious great families and sects I had visited.

*That aside…*

Why is nobody here?

There wasn’t even a servant or guard in sight, let alone the Family Head himself.

Zhuge Gyun shouted loudly while everyone, myself included, stared around.

“Family Head!”

His shout, infused with internal energy, echoed through the library.

The space was not merely large. Vast was the more appropriate word. It was larger than a modern soccer stadium.

Zhuge Gyun’s voice burrowed between the endless rows of bookshelves, but no answer came back.

“What the hell? Is he not here?”

“He seems to be inside, but… Ah, this is driving me crazy.”

As if he had known this would happen, Zhuge Gyun let out a deep sigh and continued.

“He often gets like this when he becomes absorbed in something. I’m sorry, but if you could wait here for a moment, I’ll find the Family Head and—”

Jeok Cheongang, who had been looking around the library, interrupted him.

“Enough. Is that really necessary?”

“Pardon? Even so, with Great Hero Jeok visiting…”

“He’ll come out when the time is right. Everyone has their own circumstances.”

For a moment, I wondered if I had heard him correctly. Of all people, I never expected those words to come from Jeok Cheongang.

Cheongpung even dropped the candied fruit he had been bringing to his mouth.

*Am I dreaming?*

I was still seriously considering the question when Jeok Cheongang continued with a warm smile.

“Come to think of it, this old man has never seen a library so large and magnificent in his entire life. Would it be all right if I looked around for a while?”

Zhuge Gyun answered with a dazed expression.

“Of course.”

“Even if I burn it down?”

“…Pardon?”

“It was a joke, you little punk. Ho-ho. Even so, how could I burn everything down indiscriminately when I’m here as a guest?”

Jeok Cheongang laughed heartily before continuing.

“Unless I accidentally knock over a bookshelf.”

And in the next moment, Jeok Cheongang’s body shot upward like a streak of light.

At the same time, his palm strike, carrying the tremendous force of ten thousand geun, slammed into the nearest bookshelf.

Boom!

It happened before anyone had time to stop him. I stared at the scene unfolding before me with my mouth hanging open.

*Oh, fuck.*

Rumble…

The bookshelf, which looked to be at least three zhang tall, began to tilt.

And there were hundreds of them.

The countless bookshelves packed together at regular intervals transformed into one enormous domino in the blink of an eye.

“W-wait, wait, wait, wait!”

Crash! Rumble-rumble-rumble!

An earth-shaking roar swallowed Zhuge Gyun’s scream.

As every bookshelf collapsed, dust that had accumulated over many years burst into the air all at once and filled the library in a dense cloud.

No, I wasn’t even sure it could still be called a library. A graveyard of books. Something like that would have been more appropriate.

It might even have become one person’s grave.

“Fatherrrr!”

Jeok Cheongang patted Zhuge Gyun on the shoulder as he wailed.

“You’re the new Family Head of the Zhuge Clan now.”

“Nooo!”

Whack!

After smacking Zhuge Gyun on the back of the head, Jeok Cheongang opened his mouth with an incredulous expression.

“You really don’t understand jokes, do you? Can’t you see your father over there, alive and well?”

Jeok Cheongang was telling the truth.

After a couple of coughs came from within the thick cloud of dust, a slender figure emerged, waving one hand as he walked forward.

“Well, now. Cough. I’m sorry I couldn’t come out to greet you in advance. There have been an unusual number of matters requiring my attention lately. Cough.”

“At least you know. What an ill-mannered brat.”

Jeok Cheongang answered curtly and flicked his sleeve.

Whoosh!

With the sound of compressed air bursting outward, the dust cloud scattered. At last, the figure of a man became fully visible.

“Ha. Seeing you like this, I realize how much time has passed. Do you remember this old man?”

A clear voice answered.

“Of course. That day was the fifth Mid-Autumn Festival I celebrated after being born. Senior ate two plates of roast duck and five jars of Yeoahong, then fought a duel with Great Hero Peng as the gathering was ending and ended up with a bloody nose.”

“What? That Thunderbolt Saber King bastard was there too? We even fought?”

“Yes. Great Hero Peng laughed loudly and struck the table, spilling wine onto Senior’s knee. It was a minor disagreement.”

“A major incident in which it wouldn’t have been strange for someone to die.”

Jeok Cheongang let out a quiet laugh before continuing.

“Quite a few years have passed, but that incredible head of yours is still as sharp as ever. All right, enough nonsense. Come here. You have guests waiting for you.”

“I was planning to greet them regardless.”

The middle-aged man had been covered in dust, but it couldn’t conceal his refined appearance.

He was the youngest Sect Leader of any prestigious great family or sect I had met so far. His eyes, unusually clear and radiant, turned toward us.

“I apologize for keeping such honored guests waiting. I am Zhuge Feng.”

It was a remarkably plain greeting for the Family Head of the Zhuge Clan, the foremost great family in Hubei Province and one of the central pillars of the orthodox faction.

And the moment I heard what Zhuge Feng said next, before anyone had a chance to respond, I suddenly understood why his sobriquet was Crouching Dragon Guest.

“Time is as valuable as gold, and I have no intention of taking anyone else’s precious gold. Those who wish to remain here may do so. Oh, and it has long been my personal belief that conversations should be held comfortably, so please do not misunderstand.”

I wondered what he meant until I saw Zhuge Feng lie down flat on his side right there, paying no attention to the dust piled across the floor. I let out a quiet laugh.

“Sure, why not? This is comfortable.”

As I spoke, I lay down at an angle and propped my chin on one hand. The corners of his eyes curved like crescent moons.

* * *

Although they were dumbfounded, everyone gradually sat down and listened to Zhuge Feng.

Mu Song tried to leave, saying that he had to go to a Yangtze River Channel League stronghold in Hubei, but he had no choice but to stop after Zhuge Feng said one thing.

“I won’t stop you if you wish to leave, but what I am about to say is deeply connected to you as well, Ship-Fire Boy Mu Song.”

“……!”

Mu Song hesitated before remaining behind. Mungyeong, who had seemed the most likely to leave first, unexpectedly stayed quietly in his place.

Then again, in a situation where everyone else was staying, perhaps leaving alone would have drawn even more attention.

Through the Zhuge Clan’s own intelligence network, Zhuge Feng already knew that this young medical apprentice was the Disciple of the Divine Physician. He looked at Mungyeong once with a strange expression, then turned his gaze away and opened his mouth.

“It was exactly one month ago. I was in the library, reading the *Records of the Grand Historian* for the eighty-fifth time, when I heard the news.”

The Nine Sects and One Gang and the Five Great Families were the leading powers representing each province.

Since their roots stretched back anywhere from a hundred years to several centuries, each possessed a dense intelligence network that let them know their territory as well as the palm of their hand.

The Zhuge Clan was no exception.

“The news was that the Sea Serpent Society had disappeared.”

“The Sea Serpent Society? What’s that, Benefactor?”

“I don’t know either.”

Unlike the bewildered Cheongpung and me, everyone else opened their eyes wide.

Mu Song’s reaction in particular stood out more than anyone else’s.

“Th-the Sea Serpent Society?”

“Yes, the very one you know. The association formed by the countless fishermen and boatmen living in Hubei Province.”

Ah. Now I understood.

I had never heard of the Sea Serpent Society, but I could guess what kind of organization it was.

To put it simply and dispense with all the old-fashioned explanations, it was a sort of professional association.

Just as each region had a Hunter Association, Hubei Province had—or rather, used to have—an association of fishermen called the Sea Serpent Society.

And this news was unquestionably good news, at least for Mu Song. The faint smile that appeared at the corners of his mouth was proof enough.

“I cannot say what the Zhuge Clan’s position on this is, but as someone devoted to the League, I find it welcome news. The Sea Serpent Society caused my Master no end of trouble.”

“I thought you would feel that way. At least in Hubei Province, it was the only organization capable of standing against the Yangtze River Channel League.”

Tributaries of the Yangtze ran throughout Hubei Province like a spiderweb.

No matter how powerful the Yangtze River Channel League was, the number of people engaged in fishing must have been overwhelming.

Although the matter did not concern Sichuan, which was under his responsibility, Mu Song laughed heartily at the news that one powerful rival had disappeared.

“But how did they end up disbanding? Did they happen to smuggle salt or something…?”

Zhuge Feng shook his head.

“Of course not. Even if they had, the Sea Serpent Society would not have handled the matter so carelessly. If they had been caught, the fleet acting under the Son of Heaven’s command would already have filled the Yangtze in Hubei.”

“Then was it an internal conflict?”

“I get the feeling you have not properly understood what I said.”

A pair of clear, transparent eyes fixed on Mu Song.

As he faced Mu Song’s confusion, Zhuge Feng continued slowly.

“The Sea Serpent Society disappeared. I mean that someone thoroughly crushed it.”

“……!”

“The night before I received that report, a banquet was held to celebrate the Society Head’s eightieth birthday. Forty-five shipowners who had sworn loyalty to him and roughly a thousand members of the Sea Serpent Society attended. They drank until past midnight and launched dozens of pleasure boats onto the waters of Red Cliffs. And that was the last of it.”

The next morning, an old boatman who rose at dawn saw countless corpses filling the waters of Red Cliffs and the wreckage of brutally shattered boats.

The Society Head—the head and body of the Sea Serpent Society—along with dozens of ship owners and the organization’s core members had all met their deaths at Red Cliffs.

Nothing can move without a head and a body.

The Sea Serpent Society, which had wielded power in Hubei Province alongside the Yangtze River Channel League for decades, disappeared just like that.

“H-how could such a thing happen…?”

“It is strange that you, of all people, did not know about it.”

Zhuge Feng stared silently at Mu Song, who could not continue.

“Do you know who moved first after the incident at Red Cliffs became known? The authorities? The Sea Serpent Society members who were lucky enough to survive? No. It was the Yangtze River Channel League. They invaded the Sea Serpent Society’s territory and took control of the Yangtze with astonishing speed.”

“……Great Hero Zhuge.”

Mu Song’s face hardened.

Like the rest of us, he seemed to have finally realized why he had needed to remain there.

“Are you saying you suspect me? The League?”

“Of course I didn’t. The Great Hero Hwang of Donghu Stronghold whom I know is not such a foolish man. He is different from the other foolish and violent Stronghold Lords.”

Zhuge Feng brushed the dust from his shoulder and smiled faintly at Mu Song.

“That was certainly what I thought. Until the Dongting Fisherman, who had publicly condemned the Yangtze River Channel League, disappeared three days ago.”

“……!”

At that moment, unrest spread through the group, and a familiar notification rang in my ears.

Ding.
## Chapter artifact 446

# Chapter 446

Ding.

> **System**
>
> A Quest has been generated.

A familiar System notification.

And immediately afterward, a translucent holographic window that only I could see appeared in midair.

> **System**
>
> **Quest**
>
> **Another Chaos**
>
> An ominous air hangs over the once-peaceful Hubei Province.
>
> The clear waters of the Yangtze have been dyed red with blood, the once-mighty Sea Serpent Society has fallen amid countless deaths, and the Dongting Fisherman, who publicly condemned the Yangtze River Channel League, has disappeared.
>
> If someone reveals the truth behind these events and finds the culprit, the chaos will subside.
>
> **Grade:** Peak
>
> **Restriction:** Jin Taekyung
>
> **Mission:** Uncover the truth behind the incident *(Incomplete)*
>
> **Reward:** ???
>
> **Failure:** Worsening chaos in Hubei Province and a succession of additional incidents
>
> Will you accept the Quest?
>
> Y / N

*A Quest…*

I slowly looked around.

Mu Song sat with his lips pressed tightly together, while Crouching Dragon Guest Zhuge Feng stared at him with a cold smile.

Jeok Cheongang was frowning as he watched the two of them, and Mungyeong sat expressionlessly.

And finally… Jin Wikyung calmly observed the entire situation.

*So he did know.*

According to what Zhuge Feng had said, the Sea Serpent Society Head and a thousand of his men had been buried beneath the waters of Red Cliffs a fortnight ago. Jin Wikyung must have heard about it while he was on his way to Sichuan.

*And adding Hubei to the itinerary for the return journey meant that the leadership in Henan had approved it as well.*

Now that Dark Heaven’s existence had spread throughout the world because of the bloody incidents in Shaolin and Sichuan, the series of events taking place in Hubei could not be taken lightly.

If this was Dark Heaven’s scheme, we had to stop it.

And if the Yangtze River Channel League had plotted this conspiracy while taking advantage of the chaos caused by Dark Heaven, then they had to be punished as an example to all.

Jin Wikyung had not come here as the Lesser Family Head or acting Family Head of the Jin Family of Taiyuan.

He had come as an inspector for the new Murim Alliance that would soon be formed.

And the meaning of that was simple.

*I’m supposed to stand with Jin Wikyung, too.*

In any case, this was a Quest without a penalty. Asking whether I would accept it was pointless when I was already in the same boat as Jin Wikyung.

I muttered inwardly.

*Yes.*

Ding.

> **System**
>
> - Quest accepted!
> - Quest **Another Chaos** has been registered in the Quest window! Quest information may be updated depending on the situation.

I wasn’t sure what else could be updated here.

Judging from Zhuge Feng’s words and the atmosphere I had sensed on the way to the Zhuge Clan, it was clear that Hubei Province as a whole had already branded the Yangtze River Channel League as the culprit and was pointing fingers at it.

But…

“Are you certain the Yangtze River Channel League is the culprit?”

At least for now, my personal judgment was that we couldn’t jump to conclusions.

And as my one question broke the heavy silence, Crouching Dragon Guest Zhuge Feng smiled faintly and opened his mouth.

“Blazing Flame Divine Dragon Jin Taekyung. You seem to have many questions about this matter.”

“I can’t say I don’t.”

“Go ahead. So long as we do not waste each other’s precious time.”

“First, I would like to ask whether there is any evidence.”

“Evidence?”

“Yes. All we have are circumstances, aren’t they? At the very least, shouldn’t there be a witness who saw the Yangtze River Channel League attacking the Sea Serpent Society on the night of the incident at Red Cliffs?”

“A witness. And what else?”

“The whereabouts of the Dongting Fisherman, who publicly condemned the Yangtze River Channel League, have not been uncovered, either.”

“Continue.”

I glanced at Jeok Cheongang before going on.

“According to what I once heard from the old—no, from my Master, the Dongting Fisherman was a Supreme Peak master who belonged to neither the orthodox nor unorthodox factions.”

“You know the facts precisely. The Dongting Fisherman spent his entire life near Dongting Lake, building friendships with famous figures from every walk of life.”

The Dongting Fisherman was an especially well-known figure even in Murim, where strange and extraordinary people were common.

It was unusual enough that he had never belonged to either the orthodox or unorthodox factions and had never left the area around Dongting Lake in his entire life.

But the profound martial arts he wielded with the single fishing rod he always carried were famous throughout Murim as well.

“I couldn’t understand how a Supreme Peak master like the Dongting Fisherman could disappear without anyone knowing.”

“What part of it do you find difficult to understand?”

“If the Dongting Fisherman was killed by someone, that means his opponent was also a master of equal or greater ability. When Supreme Peak masters really fight, it causes a massive commotion. There’s no way no one would have noticed.”

“You certainly speak plainly. Continue.”

“And this is going to sound disrespectful to Senior Mu Song.”

Mu Song, who had regained a little of his composure after I stepped in, nodded.

“Go ahead. I’m fine.”

“Really?”

“Of course.”

“Well, if you say so.”

I carefully opened my mouth.

“Honestly, does the Yangtze River Channel League have a master of that caliber? From what I’ve experienced, it didn’t seem that way.”

“……!”

“……!”

You said you were fine. You told me to go ahead.

Mu Song’s expression looked even less fine than before, so I quietly amended what I had said.

“Ah, of course, I’m only talking about Hubei. I respect Great Hero Seafaring King. I even enjoyed the drama—no, anyway, I like him a lot.”

“……”

“Actually, when I was young, my dream was to become a river bandit. The Grand Line! The great Yangtze!”

“……”

All right. I was in the wrong.

Why did I feel guilty even though I was technically trying to help?

Zhuge Feng rescued me from the crisis with a single sentence.

“There is such a master.”

“What? There is? You’re not lying? Seriously?”

“……”

Mu Song grew dejected again, and Zhuge Feng continued slowly.

“Yangtze One Saber Hwang Chung.[^1]”

[^1]: Hwang Chung is the Korean reading of Huang Zhong, a general from *Romance of the Three Kingdoms*.

“Yangtze One Saber. Yangtze One Saber…”

The title sounded vaguely familiar, but the name itself was unfamiliar. Surely he wasn’t the Hwang Chung from *Romance of the Three Kingdoms*.

*He does seem to be the Uncle Hwang Mu Song mentioned when we first arrived in Hubei.*

As I tilted my head at the name I was hearing for the first time, Jeok Cheongang cut in with his sharp voice.

“Yangtze One Saber? That bastard who is the Seafaring King’s sworn brother?”

“Yes. I imagine Senior knows him as well.”

“I saw him once during the Great Faction War. He was calm and clever for a river bandit. I remember thinking that despite being young, he had a decent personality and considerable martial talent… It seems he finally crossed the wall.”

“If he had not helped the Seafaring King, the Yangtze River Channel League as it exists today would not be here.”

“You call that something worth saying? Without someone to keep him in check, how could the Seafaring King, that foul-tempered bastard, have ruled the Yangtze?”

Wow. That was practically spitting in his face.

Mu Song, who had just heard his Master being insulted right before him, moved his lips as if he had something to say. But Jeok Cheongang silenced him with nothing more than a fierce glare.

I took advantage of the opening and quickly spoke up.

“Then are you saying that Yangtze One Saber killed the Dongting Fisherman?”

Zhuge Feng thought for a moment before nodding.

“Most likely.”

“Most likely?”

“Nothing has been proven. We have no certainty, only suspicions and circumstantial evidence. But there are many witnesses who can testify about where the Dongting Fisherman went before he disappeared.”

“Where was that?”

Zhuge Feng looked at Mu Song and continued in a slow voice.

“Donghu Stronghold. He headed for its headquarters, where the Yangtze One Saber, Great Hero Hwang Chung, serves as Stronghold Lord. And he never appeared again.”

“That’s impossible!”

Those words had not come from me.

Mu Song shot to his feet, the veins standing out on his neck as he shouted.

“Uncle Hwang isn’t that kind of person!”

He was also one of the disciples who had inherited the Seafaring King’s ultimate technique.

The qi pressure radiating from Mu Song, who stood at the far edge of Peak, stirred the dust that had settled around us.

Covering his mouth with his sleeve, Zhuge Feng gave a small cough and answered calmly.

“Why do you say that?”

“You know as well as I do, Family Head! Uncle Hwang was the one who persuaded my Master to support the orthodox faction during the Great Faction War. He also belongs to the moderate faction within our League! For someone like him to deal with the Sea Serpent Society this way and kill the Dongting Fisherman… That is something he could never do!”

“‘Something he could never do’? What an empty and meaningless statement. Circumstances and people change every time. A wise man like me infers the outcome from the circumstances of a matter.”

Zhuge Feng was so calm that Mu Song’s anger seemed almost meaningless.

“I can say this much with certainty: I am not convinced that the Yangtze River Channel League is behind this. But all the circumstantial evidence points to your League.”

“Why? Because once the Sea Serpent Society, which had opposed our League for so many years, disappeared, our brothers moved in to occupy the empty space? Or because the Dongting Fisherman simply disappeared while on his way to visit Uncle Hwang?”

“Both.”

“Did you even ask our brothers about it?”

“Not yet.”

“Then why—!”

Just as Mu Song was about to shout, Zhuge Feng’s quiet voice pierced the ears of everyone in the room, including me.

“If no one from the Yangtze River Channel League has shown themselves, whom could I ask?”

“……!”

“……!”

“A full month has passed. Do you think our family, Wudang, and the authorities have done nothing and are simply suspecting the innocent Yangtze River Channel League for no reason?”

Only silence filled the room.

Everyone stared silently at Zhuge Feng and Mu Song.

Unlike Mu Song, who had frozen like a statue, Zhuge Feng continued smoothly.

“Two days after the incident at Red Cliffs, Dangyang Stronghold and Honghu Stronghold, which had moved quickly to seize the Sea Serpent Society’s territory, vanished without a trace. Every single person.”

“……Then what about Donghu Stronghold?”

“Someone once told me that Donghu Stronghold was a natural fortress built on the water. I tried to see for myself, and they were right. Now that even the Sea Serpent Society’s core boatmen have all been drowned, we could not enter Donghu Stronghold by crossing the waters of Tianling Falls.”

Mysterious and magnificent nature sometimes refused to allow human intrusion.

The Tianling Falls Zhuge Feng mentioned were clearly the passage to Donghu Stronghold, one that only a tiny number of boatmen could navigate.

A boatman with some of the finest skills even in the Yangtze River Channel League and the Sea Serpent Society—or someone who had spent his entire life on the Yangtze in Hubei…

The Dongting Fisherman must have been one of them.

“The Dongting Fisherman and the late Sea Serpent Society Head were close friends. Enraged by his friend’s death, he publicly condemned your League, launched a boat, and crossed Tianling Falls—the very same Tianling Falls where we sank dozens of ships over the past month or so.”

Zhuge Feng suddenly rose and began to walk leisurely.

He clicked his tongue softly at the fallen bookshelves, then continued speaking as he rummaged through the piles of books stacked high around him.

“But did you know this? Although we failed to cross Tianling Falls, the Yangtze, after accepting dozens of ships as tribute, tossed us a gift as if out of generosity.”

Scrape. Crash!

The precariously stacked pile of books collapsed, sending dust billowing into the air.

Zhuge Feng, covered in pale dust, adjusted his cap and straightened his back.

Something dark and battered was in his hand.

“That’s…”

“Your guess is correct, Successor Beggar.”

At Gung Gibang’s mutter, Zhuge Feng nodded.

“The Black Bamboo Fishing Rod. The Dongting Fisherman’s signature weapon—the only one of its kind in all Murim.”

“……!”

“Well then, Ship-Fire Boy Mu Song.”

Zhuge Feng slowly raised the broken Black Bamboo Fishing Rod.

Then he pointed it toward the wide-eyed Mu Song as if he meant to stab him and continued.

“You will lead the way and guide us to Donghu Stronghold beyond Tianling Falls. I need to see with my own two eyes exactly what happened there.”
## Chapter artifact 447

# Chapter 447

Whoosh.

Silence hung over the fast ship as it cut rapidly through the current.

The river bandits of Water Dragon Stronghold rowed like machines with their mouths pressed tightly shut, while Mu Song did nothing but stare ahead with a stiff, frozen expression.

*What a wonderful atmosphere.*

I clicked my tongue inwardly and looked around.

There were four fast ships heading toward Donghu Stronghold.

But the atmosphere aboard them was worlds apart from when we had been heading toward Hubei.

The reason was the unfamiliar faces that had not been there before.

*The Zhuge Clan. And Wudang.*

Disciples from the two prestigious great factions that divided Hubei Province filled the four fast ships.

It was obvious at a glance that they were elites carefully selected in preparation for any unforeseen bloodshed. Every one of them was an outstanding martial artist.

And at the center of them stood two people.

“The wind seems unusually strong today, Family Head Zhuge.”

At the old Daoist’s words, Zhuge Feng answered in an untroubled voice.

“You need not worry. If the wind is blowing like this, things will actually be easier for us.”

“Why is that? I understand that dozens of ships have already sunk in winds weaker than this.”

“The boatmen’s skill is one thing, but the fast ships that serve as the symbol of the Yangtze River Channel League are qualitatively different from ordinary vessels. Rather than being swept away by strong winds, they can catch the force and move forward with even greater vigor.”

“I have heard some talk about fast ships as well… but I do not know the details, as my experience is limited. I have spent my entire life in Murim, yet it feels as though I have wasted it.”

“Since you have remained at Wudang’s headquarters all this time, it is understandable that you would not know. But… may I ask what became of the matter you mentioned last time?”

“Our Sect Leader is personally working on it together with the disciples of our main sect. As for me, I was sent here instead, since all I was doing was sitting around and consuming the sect’s grain.”

“Consuming grain? With Perfected Being Hyeongong joining us, this junior feels as though he has gained a thousand troops and ten thousand horses.”

Zhuge Feng’s words were not mere courtesy. They were true.

Perfected Being Hyeongong.

That was the Daoist title of the old man wearing a patched Daoist robe and carrying a single Pine-Pattern Ancient Sword at his waist.

His position within Wudang and his generational seniority in Murim were in no way inferior to Zhuge Feng’s.

No, one could even say that he stood shoulder to shoulder with Zhuge Feng—or above him.

Unlike Zhuge Feng, who had not yet reached sixty, Perfected Being Hyeongong was a master of the previous generation who had distinguished himself during the Great Faction War. He was also the current Wudang Sect Leader’s Junior Brother.

*On top of that, he’s one of Wudang’s famed Supreme Peak masters.*

Perfected Being Hyeongong was the swordsman said to have reached the ultimate stage of Wudang’s greatest technique, the Taiji Wisdom Sword.

The fact that Zhuge Feng, Family Head of the Zhuge Clan, spoke so respectfully even in front of others was itself a sign of his respect for Hyeongong.

Ah, of course, there was one exception to all of this.

“That guy’s grown a lot.”

At the words of Jeok Cheongang—Murim’s own Bodhidharma and the ultimate old-timer—I muttered in disbelief.

“Sure has. He’s grown so much that his beard has turned white.”

“How old was that fellow the last time I saw him? Thirty?”

“……”

“Ha. Time really flies. Those young pups with soft fuzz on their faces are all Sect Leaders and Elders now.”

“Soft fuzz? If he was thirty, wouldn’t he have had a full bush down there?”

Jeok Cheongang glared at me with blazing eyes.

“Judging by the way you keep nitpicking my words, it seems you want every hair below your waist plucked out.”

“No, why would you say something like that?”

I had not the slightest desire to undergo Fire King Zilean waxing on the deck of a fast ship.

I waved my hands at lightning speed, then glanced sidelong at Jeok Cheongang.

“Since we’re on the subject, may I ask your venerable age?”

“My venerable age?”

Even under ordinary circumstances, Jeok Cheongang treated being called old as synonymous with asking him to kill you. I awkwardly tried another term.

“…Then, how many years have you lived, sir?”

“How many years?”

No, seriously. He was over a hundred years old. What more did he want from me?

I asked, thoroughly exasperated.

“Cheongang, how old are you?”

Whack!

Right. I knew this would happen.

After striking the back of my head like a bolt of lightning, Jeok Cheongang answered in a bored tone.

“I stopped counting after I passed one hundred.”

“So when was the last time you counted?”

“Five thousand years ago. Satisfied?”

Cheongpung, who had been dangling from the nearby bow, opened his mouth wide.

“Wow, five thousand years old!”

“…Does that fellow not know what suspicion is?”

“…He’s always been like that. Anyway, you look incredibly young for your age.”

Jeok Cheongang stared at me.

“Do you want to know more?”

“Of course not.”

I honestly did want to know, but judging by his expression, I probably shouldn’t.

He was sensitive about his age under ordinary circumstances. On top of that, the reality of riding a fast ship that was racing forward over rougher waves and stronger winds than ever before seemed to be placing an enormous amount of stress on him.

“When the hell is this goddamned piece of wood going to stop?”

Right then.

As if it had heard Jeok Cheongang’s complaint, the goddamned piece of wood picked up even more speed.

Whoooosh!

A column of water surged high into the air, and the previously stable hull rocked from side to side.

At the sudden rough movement, Cheongpung let out a cheer like a child visiting an amusement park on Children’s Day.

Hyuk Mujin and Gung Gibang, who still had not recovered from the aftereffects of the Yangtze taste-test incident, released ear-splitting screams. Mungyeong, who had been calmly keeping his balance by himself, tactfully grabbed the railing after noticing everyone’s eyes on him.

And Jeok Cheongang…

“Uhh! Uhhhhh!”

He was panicking, making a noise so undignified that it rendered the title Fire King meaningless.

Good heavens, look at those bulging eyes. He could be used in a Gangnam plastic surgeon’s subway advertisement as a successful double-eyelid surgery case.

I dodged the water splashing into my face and shouted toward Mu Song.

“Senior! Could you slow down a little—”

“That will be difficult.”

Mu Song cut me off with a voice as sharp as a blade.

Like a man born and raised on the Yangtze, he stood perfectly upright as if he were on level ground. He raised one hand and pointed ahead.

“Can you see it?”

See what?

I narrowed my eyes and stared in the direction of his finger.

I drew up my internal energy and concentrated it in my eyes. My eyesight, enhanced by leaps and bounds, pierced through the thick fog covering the rippling river.

*That’s…*

I could see it.

A narrow passage barely wide enough for two fast ships—the most streamlined kind of vessel—to pass through.

And directly in front of it, a violent whirlpool twisting like a blade.

Whoooosh! Crack!

A massive log, swept in from who knew where and caught in the whirlpool, which measured more than a hundred zhang in radius, broke apart after failing to withstand the pressure of the water.

Some of the splintered pieces were flung away and smashed into a huge rock standing behind the whirlpool like a gatekeeper, shattering into fragments.

*A whirlpool like that in a river, not the sea?*

It was a mysterious sight, but one that sent a chill down my spine.

And every single person aboard the fast ships knew the identity of that terrifying whirlpool.

“Tianling Falls!”

Someone shouted the words like a scream.

That was right. This was Tianling Falls.

A work of nature that had transformed Donghu Stronghold of the Yangtze River Channel League into a natural fortress—and a monster that had swallowed countless lives and ships over the centuries.

Jeok Cheongang declared with a face that looked as though he might suffocate at any moment.

“Turn the ship around. I would rather fight the Great Faction War one more time than cross that.”

Gung Gibang and Hyuk Mujin spoke next, their faces already looking as if they had suffocated.

“Senior Mu Song. Please save us. I would rather beg in a beggars’ den.”

“Captain. Thank you for everything. I’m quitting Murim now. I want to go home and sell silk.”

“…It looks like your soul will be sold before the silk.”

I was afraid, too.

As I watched the enormous whirlpool rushing closer, I felt as though I had become an ant trapped in an antlion’s pit.

*Fuck. First we’ll get smashed to bits against that rock, then we’ll be sucked in like a toilet flushing.*

In the face of the terror offered by Mother Nature, even the System and Supreme Peak martial arts felt utterly useless.

If someone dropped me in the middle of the Yangtze, I was confident I could somehow swim to shore. But if I were swept into a monstrous whirlpool like that…

That would truly be the end.

“Whew. Whew.”

A thick hand settled on my shoulder as I took deep breaths.

“My youngest.”

Even I, who was fairly tall, had to lift my head to look up at the giant. Jin Wikyung opened his mouth with a calm expression.

“Do not worry about a thing.”

His composure was enough to make me call him Big Brother without thinking.

Putting aside Jeok Cheongang, who had a pathological hatred of water, even I had reached the Supreme Peak realm and was still feeling my blood run cold. Yet Jin Wikyung, whose martial arts were far below ours, did not waver in the slightest.

*So this is why he’s the eldest brother and the Lesser Family Head.*

“Big Brother…”

“Yes.”

Jin Wikyung smiled faintly and nodded.

“Even in death, the bond between our brothers will last forever.”

“What?”

“I can see our deceased parents hovering before my eyes. It is as though they are beckoning to us from Tianling Falls.”

“…Isn’t Father still alive?”

“We lost contact with him again a long time ago. Let us consider him dead.”

*Big brother, my ass. He’s just a big bastard.*

And while he was at it, he had declared our perfectly alive father dead just because the man had dumped the family responsibilities on him and run away.

*Shit…*

I looked around. Most of the people were already half out of their minds, letting their bodies move to the beat of Mother Nature.

I looked at Mu Song with the last of my hope.

“Senior Mu Song.”

“I’m sorry, but it’s too late to stop.”

Whoooosh! Crack!

“Oh, fuck. He’s right.”

Mu Song nodded with a hardened expression.

“Hold on tight. My men and I will do our best as well.”

“What? What do you mean, do your best?”

“Do you think Tianling Falls is some common feature that can be found in every province? I have only crossed it three or four times, when I came to Hubei to see Uncle Hwang. We have no choice but to trust the League’s fast ships and the skills we have honed over the years.”

“W-wait. So you’re saying… you’re a Tianling Falls newbie?”

“I do not know why Liu Bei suddenly came up, but naturally I would be unfamiliar with it. I spent all my time in Sichuan after leaving headquarters and becoming Stronghold Lord.”

He had a point.

A fucking punchable one.

Half out of my mind, I barely squeezed out my voice.

“You’ve got to be kidding me. Why are you only telling us something this important now?”

“Great Hero Zhuge told me not to tell anyone else.”

What?

I turned my head at lightning speed and saw the disciples of both sects, their bodies rigid with tension, and the man standing at their center.

Zhuge Feng met my gaze and laughed heartily as he was pelted by the rising spray.

“A wise man leads his allies, while a strategist deceives even his allies. Since we have all climbed onto the tiger’s back, let us see this through to the bitter end!”

“……!”

“……!”

Was this for real?

Everyone, myself included, was left speechless, while Jeok Cheongang lost his reason.

“That fucking son of a bitch…!”

It was one of the greatest fits of rage I had ever witnessed.

But just as Jeok Cheongang rolled his eyes back until only the whites showed and prepared to charge—

“Everyone, hold on tight!”

With Mu Song’s urgent shout, the whirlpool of Tianling Falls opened its maw wide and slammed into the fast ship.

KRA-KOOOOM!
## Chapter artifact 448

# Chapter 448

A Supreme Peak master was a being capable of feats straight out of an old folktale—erasing several zhang of distance in a single step, leaping through the air as though stepping on empty space, and bringing down a cliff with one punch.

But…

“Hold on tight—aaahhh!”

KRA-KOOOOM!

This place was the middle of the Yangtze, vast as an endless ocean rather than solid land.

In front of a massive whirlpool hundreds of zhang across, the fast ship carrying me was no more than a tiny leaf.

Boom!

“Whoa, whoa, whoaaaa!”

“Aaaaargh!”

When the tremendous pressure of the water slammed into the side of the fast ship, the hull that had been moving swiftly and roughly lifted into the air and tilted sideways.

As the world slowly turned upside down, Jin Wikyung clung tightly to my upper body as if I were a life jacket and screamed.

“Mother! I’m coming!”

“Where do you think you’re going? Let go!”

“Father! If you’re watching, tell me the answer!”

*Fuck, there isn’t even an answer.*

But the bigger problem was that it wasn’t just Jin Wikyung. Gung Gibang, Hyuk Mujin, and even the disciples of the Zhuge Clan and Wudang had all been driven half out of their minds.

The only ones who had managed to keep their composure were the Supreme Peak masters, myself included.

“Uhh! Uhhhhh! Water! Wateeer!”

“…”

Correction. There was one exception.

I grabbed Jeok Cheongang, who was screaming at the top of his lungs with his eyes squeezed shut, and thrust my free hand into the air with all my strength.

*Flame Divine Palm!*

Boom!

Compressed air burst outward in a wave of powerful internal energy.

Part of the whirlpool that had been raging like a blade dispersed, and the hull that had been plunging upside down toward the surface barely managed to regain its balance.

But it was far too soon to feel relieved.

A second and then a third whirlpool were approaching the falling fast ship.

*I’m not enough on my own. In a situation like this…*

With a thought flashing through my mind like lightning, I shouted one person’s name.

“Cheongpung!”

“Yes!”

Cheongpung nodded as if he understood everything and raised both arms.

“Kiya-hoo!”

“No, not ‘kiya-hoo,’ you lunatic! Do what I did!”

“Ah. Yes, Benefactor!”

Cheongpung had been enjoying the Wolmido Disco Pang Pang[^1] all by himself, but now he shook both sleeves.

The Taeeul Miri Palm, one of Huashan’s proudest techniques, transformed into dozens of flower petals that lashed out through the air.

Boom-boom-boom!

It could not match the destructive power of the Flame Divine Palm, but in a situation like this, the Taeeul Miri Palm was perfect, thanks to its much wider range.

When Tianling Falls, which had been raging like a blade, faltered, it seemed that the disciples of the Zhuge Clan and Wudang also regained the senses that had briefly departed them.

“Ha-ha-ha! The tiger is rampaging! Disciples of our family, unleash the Great Heavenly Star Divine Palm!”

Crouching Dragon Guest Zhuge Feng, who had issued the order, waved the feather fan in his hand.

Although he had not yet crossed the wall, he was said to stand shoulder to shoulder with Supreme Peak masters when it came to fan techniques alone.

Whoooosh!

The breeze that began along the fan’s ribs transformed into a powerful wind and blocked the whirlpool.

And at the moment when a wall of water rose high like a triangular wave, seemingly ready to swallow the fast ship, only to be stopped by the wind—

Whoosh!

A streak of light shot up from the waist of Perfected Being Hyeongong and swept through the air.

Taiji Wisdom Sword.

The streak of light passed through everything in its path, cleaving space and slicing through the wind. The wall of water raised by Tianling Falls seemed to be severed in an instant before collapsing into pieces.

SPLAAASH!

Spray scattered in every direction.

Jeok Cheongang, who had been drenched by an enormous amount of cold water, opened his eyes wide like a man waking from sleep.

Then he glared at the whirlpool with eyes that poured flames and shouted.

“You wet, smelly, filthy things!”

“…”

It wasn’t entirely wrong, but why did he sound so pathetic?

Contrary to my thoughts, however, the internal energy erupting from Jeok Cheongang’s sleeves was anything but pathetic.

“Get the hell out of here!”

Fwoosh—KRA-KOOOOM!

Several jiazi’s worth of Scorching Yang Qi burst out all at once.

The moisture filling the air evaporated, and the fast ship shot forward like an arrow under the tremendous recoil.

“Kiya-hoo!”

“Cheongpung, you lunatic!”

“Oh. Sorry, Benefactor!”

Boom-boom-boom!

Palm forces erupted without pause to protect the ship, while Tianling Falls tried to sink the unwelcome guests who had entered its territory without permission.

Mu Song gritted his teeth so hard that blood began to seep from his gums, the veins standing out on his neck.

“Hard to port! Turn at the same time!”

“Aaaaargh!”

Bang!

In the middle of this chaotic situation, only three people knew the secret of how the young medical apprentice had quietly fired a palm force while screaming strategically among the others: Jeok Cheongang, Cheongpung, and me.

“One, two!”

“Now! Row with every bit of strength you have!”

SPLAAASH!

Hard work never betrayed its results.

And so, the four fast ships carrying hundreds of passengers pushed onward through the whirlpool, farther and farther ahead.

* * *

The moment they passed through Tianling Falls, the exhausted passengers collapsed wherever they stood, no longer bothering with appearances.

But there was an exception to everything.

Jeok Cheongang gazed at the Yangtze, which had become unbelievably calm, his eyes red around the edges. Then he suddenly opened his mouth.

“As the current Sect Leader of the Fire Gate Clan, I hereby declare that, as of this time tomorrow, the Zhuge Clan shall be our public enemy.”

“…”

“Every bastard bearing the Zhuge name should be seized and thrown into that godforsaken Tianling Falls. Any objections?”

“What if there are?”

“I’ll throw you in with them.”

“Then I’ll have no objection.”

“Good. Seize that goddamn bastard and bring him before me at once.”

At the end of Jeok Cheongang’s burning gaze was a fast ship following several dozen zhang behind us, with Zhuge Feng sitting at its bow and waving his feather fan.

“Ha-ha, Senior! Please set aside your anger!”

“…”

“Are you laughing?”

Even I wanted to kill him.

It was easier to bring down a cliff than to escape after being sucked into a whirlpool in the middle of the vast Yangtze, where there was nowhere to run.

People tossed around names like Stepping on Empty Air and Rising on Duckweed, Crossing Water as if they were simple tricks, but those techniques consumed tremendous amounts of internal energy. Rescuing several hundred people was beyond the realm of possibility.

*What the hell is something like that doing in a river, not even the sea?*

There was a reason it had been given the name Tianling Falls.

Then again, if it were merely a somewhat fierce current, the Zhuge Clan and Wudang would have stormed into Donghu Stronghold long ago.

And while I was thinking about this, Jeok Cheongang’s anger continued racing toward its conclusion.

“Turn the ship around at once. Whether he calls himself Zhuge Feng or Crouching Dragon Guest, this old man will break that bastard’s legs and make him lie down for the rest of his life!”

“Please calm down. Calm down.”

“Do I look like I can calm down right now? I already hate water, and now I’ve suffered through this because we came to some godforsaken place! And the man who claims to have crossed it several times is groaning because he can’t even find the correct waterway! At this point, are you a river bandit or a ferryman on the road to the underworld?”

At the sight of Jeok Cheongang raging like a madman, Mu Song, who had been lying spread-eagled on the deck, flinched and forced himself upright.

“P-please calm yourself, Great Hero. I never dreamed Tianling Falls would be this bad, either.”

“You’ve been here several times and didn’t know? If you don’t know, does your life as a river bandit end here? Should I end your life here, too?”

“That’s not it. The current at Tianling Falls has grown abnormally strong compared to before…”

“Grown stronger? What kind of bullshit is that? It barely rained this year, and you’re trying to deceive this old man with sweet talk that’ll be exposed immediately?”

“I-I’m telling the truth! How could I dare lie to the Fire King?”

*Hmm.*

Mu Song had a point. Who would dare lie to Fire King Jeok Cheongang?

The day you were caught lying to him, losing a hand would be the least of your worries. Your entire body would be roasted medium-rare.

*By the way, can the current really become that strong when there hasn’t been much rain?*

Never mind. I wasn’t a meteorologist or an ecosystem researcher. Thinking about it wouldn’t produce an answer.

I clicked my tongue softly and spoke to Jeok Cheongang, who had not stopped berating Mu Song.

“Old Master.”

“When we return, do your job properly. If you make this old man suffer through what we just experienced one more time, I’ll storm the headquarters of the Yangtze River Channel League, set every ship on fire, and throw that Seafaring King bastard into Tianling Falls along with the Zhuge Clan bastards…”

“What is it? Tell me later.”

“That’s not it. I think we’ve arrived.”

“What!”

Tap-tap-tap-tap!

He moved with the speed of lightning itself.

Jeok Cheongang tossed Mu Song aside and crossed the fast ship in a single step, then stared ahead with his eyes wide open.

Soon, an emotional exclamation spilled from his lips.

“Oh. Ohhh!”

Anyone watching him might have thought he had discovered a treasure island, but what appeared beyond the thick fog was simply an island.

It was not small like the islands scattered along Korea’s Han River, nor was it an uninhabited island with no sign of human presence.

“That thing over there… Could it be…”

At Hyuk Mujin’s mutter, Gung Gibang, standing beside him, nodded.

“It’s a ferry landing. Looks like we came to the right place.”

The existence of a ferry landing where ships could dock meant, in other words, that people lived there—or that the island was frequently used as a stopover.

And everyone present already knew the identity of those who had established a settlement in a place that could only be reached after crossing that insane Tianling Falls.

“Whoa, Donghu Stronghold!”

Cheongpung’s shout shattered the silence of the Yangtze and spread into the distance.

Jin Wikyung opened his mouth, his face stiff.

“By now, Donghu Stronghold must know that we have arrived. It would be wise to prepare for any unforeseen situation.”

“…”

No one needed to ask what that unforeseen situation meant.

If Donghu Stronghold really was responsible for the two incidents that had occurred over the past fifteen days, just as the circumstances revealed so far suggested… then a clash of martial force might take place, in accordance with the laws of Murim.

“Stronghold Lord. We did not come here to spill blood. I trust you understand what I mean.”

Mu Song, who had remained silent with his mouth shut, stared at Jin Wikyung as he answered.

“The reason my subordinates and I came here at the head of the group was to prove that the brothers of our League are innocent. If you persecute us without even hearing the full circumstances…”

“I can state categorically that such a thing will not happen. Wudang and the Zhuge Clan have already vouched for this, and everyone present, myself included, will serve as witnesses.”

Mu Song hesitated before giving a small nod.

“…I’ll believe you.”

Perhaps Mu Song was the person here who most wanted to prevent bloodshed.

No matter how outstanding the river bandits of Donghu Stronghold were, and no matter how powerful Yangtze One Saber Hwang Chung—the man who led them—might be as a Supreme Peak master, they could not withstand our current strength.

Even if some utterly incomprehensible disaster—a true one-in-ten-thousand chance—caused everyone here to sink into the Yangtze, the Yangtze River Channel League would then have to face all of Murim.

If the Nine Sects and One Gang joined forces with the Five Great Families, the Yangtze River Channel League would disappear without a trace.

“Raise the flag high and let them know we are here.”

The river bandits of Water Dragon Stronghold immediately carried out their lord’s order.

Soon, the Yangtze River Channel League’s flag fluttered above the four fast ships, and seven low drumbeats echoed beyond the fog.

And then…

Nothing happened.

The Yangtze, the fog, and the quietly flowing river remained unchanged.

The only things that changed were the puzzled expression on Jin Wikyung’s face and Mu Song’s wavering eyes.

“Stronghold Lord. What is happening?”

“I’m not sure, either. We definitely sent the signal, so a reply should have come…”

At that very moment—

“I’m afraid that will be difficult.”

At the sudden voice, everyone turned their heads.

Countless gazes fell on the young medical apprentice whom no one had paid attention to until now.

In a clear, composed voice, he continued.

“It seems something has happened.”

“What do you mean…!”

Mu Song’s shout never finished.

The young medical apprentice, Mungyeong, raised a finger and pointed.

There, something previously hidden by the fog and aquatic plants had floated into view.

It was someone’s corpse.

[^1]: Wolmido Disco Pang Pang is a Korean amusement-park ride in which riders sit on a rotating platform while the operator jolts and spins it.
## Chapter artifact 449

# Chapter 449

From the moment they crossed the unnaturally powerful current of Tianling Falls and entered the territory of Donghu Stronghold, Ship-Fire Boy Mu Song’s heart had been beating faster and faster.

*Uncle Hwang. I’ve come.*

Hwang Chung, the Yangtze One Saber and Lord of Donghu Stronghold, was like a master to Mu Song. No—perhaps he was even more than that.

Mu Song’s true Master, the Seafaring King, was not a warm man, and their relationship was as dry and barren as sand.

When Mu Song was young, it was Hwang Chung’s warm advice and consideration that allowed him to endure the harsh scolding and training.

*I believe in you, Uncle. You’re not the kind of man who would do such a thing.*

Hwang Chung was the most serious and thoughtful person in the Yangtze River Channel League.

There was no way a man like him would have made the worst possible move by eliminating the Sea Serpent Society and the Dongting Fisherman in such a manner.

Because of his unshakable faith in Hwang Chung, Mu Song had chosen to come here in person.

But regardless of that faith, his unease continued to grow with every passing moment.

*Why is it so quiet?*

The Hwang Chung he knew, the Yangtze One Saber, was thorough and cautious in everything he did. He would never neglect the stronghold’s defenses just because he trusted in Tianling Falls.

Donghu Stronghold was a natural fortress built on the Yangtze.

If unauthorized intruders crossed Tianling Falls, they would soon see a gorge several hundred zhang long, along with countless arrowheads waiting to greet them from above.

But…

*We’re already right in front of it. Why hasn’t there been any reply?*

Even after they raised the Yangtze River Channel League’s flag high and beat the drums to send a signal, the surroundings remained as quiet as before.

Mu Song’s heart pounded violently as he stared at the island shrouded in thick fog.

*Something has gone wrong.*

That single thought flashed through his mind. Before long, the vague unease he had felt revealed its true form.

“It seems something has happened.”

“What do you mean…!”

At the words of the young medical apprentice Mungyeong, Mu Song turned his head—then could not finish his sentence. He swallowed hard.

A moment later, unrest spread like wildfire among the people aboard the ships.

“Th-that’s…”

“A corpse! It’s a corpse!”

Everyone present was a martial artist accustomed to blood and death. They had seen enough corpses to grow sick of them, but this time was different.

This was Donghu Stronghold. At a time when the Sea Serpent Society’s key figures had been wiped out and the Dongting Fisherman was all but confirmed dead, there should have been no one in Hubei Province capable of crossing the even more violent Tianling Falls to reach this place.

And yet a corpse had appeared out of nowhere.

Amid the agitation, Mu Song, who had remained silent, forced his voice out.

“...Pull it aboard at once. We need to identify it.”

“Y-yes, sir!”

Before the river bandits of Water Dragon Stronghold could move, someone strode forward.

“Stand back.”

Fire King Jeok Cheongang had been raging only moments ago. Now, he spoke in a low, settled voice as he stretched out one hand.

Powerful internal energy shot across the distance and seized the corpse submerged in the water.

Whoosh—bang!

With a heavy thud, the body landed on the deck of the fast ship.

Half of its upper body was gone, and its face was bloated. Mu Song’s eyes widened when he saw it.

“This man…”

“Do you know him?”

Jin Taekyung strode over to him, and Mu Song nodded dazedly at the question.

“Little Tide Demon Wang Pil. Uncle Hwang’s right-hand man and the Deputy Stronghold Lord of Donghu Stronghold.”

Donghu Stronghold ruled the Yangtze in Hubei Province. Naturally, the name and sobriquet of its Deputy Stronghold Lord—and the right-hand man of the Yangtze One Saber Hwang Chung—were widely known.

Ignoring the sighs that escaped at the name Little Tide Demon, Jin Taekyung stared at Mu Song with a stiff expression.

“Deputy Stronghold Lord? Are you certain?”

“Without a doubt. The corpse is badly damaged, but not so badly that I can’t recognize his face.”

“...Damn it.”

Jin Taekyung’s face hardened. It was the same for everyone who understood what this meant.

Even if it had been an ordinary river bandit, the event would have been ominous. But this was the Deputy Stronghold Lord of Donghu Stronghold—and a Supreme Peak master of the Yangtze River Channel League, whose name was renowned throughout Hubei Murim.

The meaning of this chain of events was obvious.

*Something has happened at Donghu Stronghold.*

Jin Taekyung was the first to turn the thought that had flashed through everyone’s minds into action.

Whoosh!

He crossed the deck at blinding speed and reached the stern of the fast ship, then thrust both arms forward with all his strength.

Boom! Booooom!

The Scorching Yang Qi carried by the Flame Divine Palm evaporated the river water and propelled the fast ship forward.

Only then did the others recover from their shock and begin moving after him.

“Boatmen, get back to your positions and take hold of the oars! Every second counts!”

“Tell the other ships! Send them a signal at once!”

Boom, boom, boooom!

Urgent shouts and drumbeats shattered the silence.

Amid the confusion, Mu Song raised his head, feeling his own heart pounding louder and more violently than the drums echoing around him.

And then—

“...!”

He saw it.

No—all of them saw it.

Beyond the fog slowly dispersing along the bow of the fast ship were a shattered ferry landing and countless corpses filling the river.

* * *

“What the fucking hell…!”

The curse burst from my mouth at full volume before I could stop it. But no one gave me a disapproving look or blamed me.

Maybe they were too distracted to care. Or maybe I had simply said what they all wanted to say.

That was how horrific the scene before us was.

“This is nothing short of hell.”

“...How could this happen?”

Jeok Cheongang muttered in a deeply subdued voice, while Cheongpung, who was usually so cheerful, looked around with trembling eyes.

Everywhere he looked, there were collapsed houses and corpses.

The bodies we had seen around the ferry landing were only a fraction of the countless deaths that had descended upon the island.

“C-Captain. Over there…”

“I know.”

I forced myself to ignore Hyuk Mujin, who was calling to me in a trembling voice.

I already knew what was in the direction he was pointing. My teeth clenched before I even realized it.

*Children and commoners who never learned martial arts.*

Donghu Stronghold was not inhabited solely by river bandits.

The stronghold’s people had brought their families and blood relatives to this safe, natural fortress, and the people gathered there had formed a village of their own.

And…

*They’re all dead.*

Children who had only just been weaned. Frail old people and women. Even the hundreds of river bandits who should have risked their lives to protect them.

Every single one of them had died.

That was the result after my companions and I, along with the martial artists of Wudang and the Zhuge Clan and the river bandits of Water Dragon Stronghold under Mu Song, had searched every corner of the island for more than half a day.

And among those countless dead was one particular person.

“Uncle Hwang!”

Mu Song’s beastlike roar echoed from far away. Gung Gibang muttered in a heavy voice.

“Looks like he finally found him.”

Some people said that no human life was more valuable than another.

But that was not true. There was certainly a difference in weight. The weight of a person’s death changed depending on who they had been in life and what relationship they had shared with you.

For Mu Song, at least, the Yangtze One Saber Hwang Chung must have been such a person.

“The Family Head ordered me to escort you to him at once.”

At the words of the Zhuge Clan martial artist who came running up to us, Jin Wikyung nodded.

“This concerns Great Hero Hwang, I presume.”

“Yes. Great Hero Hwang’s corpse was just found. However…”

“Let’s go. We’ll hear the rest directly from the Family Head.”

Without another word, we began walking.

Not to mourn his death, but because the dead Yangtze One Saber Hwang Chung was important enough to warrant it.

The reason Jeok Cheongang, the only person among us who had known him, wore such a hard expression was not grief, either.

—What do you think?

At the Sound Transmission that suddenly slipped into my ear, I slowed my steps and answered.

—The same as you, Old Master.

—You know what this old man is thinking?

—The same thing I am.

—I’m getting an urge to use the Flame Divine Palm.

—I’ve needed to piss since earlier, too, but I’ve been holding it in. You should hold it in as well, Old Master. I’m organizing what I want to say.

I calmly laid out the thoughts I had been considering over the past half day.

—Donghu Stronghold is a natural fortress that can only be reached by crossing Tianling Falls. I don’t know the details of the situation here, but defeating the Supreme Peak master Hwang Chung and the river bandits under him would be impossible for any ordinary force.

—Even a mongrel gets the upper hand on its own doorstep. To face men who have spent their entire lives on the Yangtze, you would need overwhelming strength.

Jeok Cheongang’s Sound Transmission continued.

—The Yangtze One Saber in particular is like a ghost of the water. During the Great Faction War, he achieved overwhelming victories against the Demonic Cult in every naval battle. To wipe out Donghu Stronghold, the attacker would have needed at least twice its forces.

Twice the forces of Donghu Stronghold…

I had only realized it after coming here, but Donghu Stronghold was on a scale utterly incomparable to the other water strongholds.

The number of corpses discovered so far had already surpassed a thousand. In terms of size alone, it would not have been an exaggeration to call it a faction.

*Mu Song said something like that before, too. Donghu Stronghold is the second most powerful water stronghold in the Yangtze River Channel League, after its headquarters.*

I only had to look around to understand.

Everything had been shattered and destroyed, but this one water stronghold had once assembled a fleet of more than fifty ships and built a settlement of homes that would not have looked out of place in a bustling city.

It might not have reached the level of a prestigious great faction such as the Nine Sects and One Gang or the Five Great Families, but the river bandits under the command of the Yangtze One Saber had undoubtedly been highly elite as well.

And there were very few groups capable of deploying twice that force against Donghu Stronghold.

No—only a handful.

—If there is a place capable of mobilizing that many men and ships…

—As far as this old man knows, there are only four such places in Hubei Province. One of them is already practically gone.

—Wudang, the Zhuge Clan, the government, and the Sea Serpent Society. Correct?

—Correct. But most of the Sea Serpent Society are fishermen and boatmen who gathered for their livelihood, so they have far too few masters. Wudang and the Zhuge Clan possess the strength, but neither has any reason or justification to attack Donghu Stronghold.

—The government is the same.

—Of course. Even a child knows that Murim and the authorities maintain a relationship of mutual noninterference. Even if the Son of Heaven had issued an imperial edict to subjugate the stronghold, they could not have carried it out secretly in a way that deceived the eyes of the entire world.

Murim was a tree rooted deep within the forest that was the world.

It had grown too tall to prune its branches, and anyone who tried to chop it down carelessly would risk damaging the blade of their own ax.

That was one of the reasons Murim had survived even though the master of the forest had changed many times.

A massive tree that even the Son of Heaven, the woodcutter, could not easily raise his ax against.

That was Murim. The countless branches and leaves that had grown from that great tree had flourished by joining forces—and, at times, by breaking one another.

The Yangtze River Channel League was one of the thicker branches.

If the water strongholds scattered throughout the world were gathered in one place, they would be more than worthy of being called a great faction, and their number of masters was not far behind that of the Nine Sects and One Gang or the Five Great Families.

And now that very branch of the Yangtze River Channel League had been broken.

By someone whose identity was unknown.

—Do you think the culprit is one of those four places: Wudang, the Zhuge Clan, the authorities, or the Sea Serpent Society?

—This is a waterway crossed by hundreds of ships every day. Avoiding all those eyes while mobilizing enough force to cross Tianling Falls would be… extremely difficult.

—It might have been extremely easy.

I finally let out the words that had been circling the tip of my tongue.

—If it was Dark Heaven.

—...!

—They had no need to load hundreds or thousands of soldiers onto ships and cross Tianling Falls. If a warp—no, if the formation they call a Moving Formation were hidden somewhere around here, that would explain everything.

Dark Heaven had already proved it in Shaolin and Sichuan.

If my guess was correct, it would also fully explain how they had gone unnoticed by the countless eyes traveling along the Yangtze.

Jeok Cheongang remained silent for a while before letting out a low groan.

—So this old man is not the only one who thinks so.

—In a situation like this, excluding Dark Heaven… the smell is far too damn foul.

—But why the Yangtze River Channel League?

—I don’t know.

I continued speaking as I looked toward the familiar faces slowly approaching from the distance.

—We’ll have to find that out now.

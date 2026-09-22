# Checkpoint Review — 615–619

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

# Chapters 615–619

## Plot

The Fire Dragon Pavilion’s Nanman expedition travels from Mount Daebyeol through Hubei and Sichuan using secret horse-caravan routes preserved in Ju Hwaran’s map and the Escort King’s records. Water Dragon Stronghold ships then carry the party down the Yangtze toward Yunnan. Along the way, Jin Taekyung restrains Song Ilseom and Sama Pyo’s hostility, while Song warns him that Hwaran has suffered greatly and must not be hurt or abandoned.

After entering Nanman, Taekyung completes the Journey to Nanman Quest and receives its rewards, including the achievement **Thousands of Li in Search of Nanman**. The resulting Peak-grade Chain Quest, **Seeds Planted in Nanman**, directs the expedition to contact a Hidden Shadow Pavilion agent in Yeongin before proceeding against the Nanman Beast Palace.

Yeongin’s inhabitants react violently to the Han Chinese because a Heavenly Demon Escort Bureau group from Sichuan allegedly massacred about two hundred villagers. The group’s nearly thirty men and one woman were later found dead from deadly venom. At Poison Flower Pavilion, the elderly innkeeper reveals himself as the Hidden Shadow Pavilion agent and identifies Taekyung as the Blazing Flame Divine Dragon. The woman may have been the Southern Heaven Demon Empress, but her identity remains uncertain.

## Continuity

- The Fire Dragon Pavilion is staying at Poison Flower Pavilion in Yeongin, Nanman.
- Jin Taekyung, Ju Hwaran, Hyuk Mujin, Song Ilseom, Sama Pyo, and Taishan are part of the expedition.
- The Nanman Beast Palace remains the expedition’s primary objective.
- The Chain Quest **Seeds Planted in Nanman** has reached its contact stage with the Hidden Shadow Pavilion agent.
- The Poison Flower Pavilion owner is the elderly Hidden Shadow Pavilion agent planted in Yeongin. He speaks both the local language and Chinese and knows Taekyung’s identity.
- Water Dragon Stronghold provided the expedition’s ships. Its Deputy Stronghold Lord promised to leave one or two ships nearby until the party returns, while Mu Song remains away under Seafaring King Pa Ryun’s summons.
- Ju Hwaran’s inherited horse-caravan map and the Escort King’s records enabled the rapid overland journey through Hubei and Sichuan.
- Song Ilseom remains hostile toward the unorthodox faction but recognizes Hwaran’s suffering and is concerned for her safety.
- Yeongin’s hostility toward Han Chinese outsiders stems from the alleged Heavenly Demon Escort Bureau massacre.
- The Heavenly Demon Escort Bureau group came from Sichuan, consisted of one woman and nearly thirty men, and all members later died from deadly venom.
- The woman may have been the Southern Heaven Demon Empress, possibly disguised, but the agent’s account does not confirm her likeness.
- The identity of the poisoner, the reason for the massacre, and the fate or purpose of the suspected Southern Heaven Demon Empress remain unresolved.
- The Lord of Heaven has awakened, empowered Dark Heaven’s servants, and declared that the Great War has begun.

## Translation Decisions

- Use **Nanman**, **Nanman Beast Palace**, **Yeongin**, and **Poison Flower Pavilion** consistently.
- Render **天魔镖局** as **Heavenly Demon Escort Bureau**.
- Render **蛮族** as **Man people**.
- Use **Southern Heaven Demon Empress** for the suspected woman; retain **South Heaven** for the faction previously established as a major power.
- Continue using **Fire Dragon Pavilion**, **Water Dragon Stronghold**, **Hidden Shadow Pavilion**, **Blazing Flame Divine Dragon**, **Peak**, and **Chain Quest**.
- Preserve Taishan’s clipped, childlike speech and the established forms **Pavilion Master**, **Young Lady Ju**, and **Great Hero Jin**.

## Durable state

{
  "active_continuity": [
    "The Fire Dragon Pavilion has reached Yeongin and is staying at Poison Flower Pavilion.",
    "The elderly Poison Flower Pavilion owner is the Hidden Shadow Pavilion agent planted in Yeongin and has identified Jin Taekyung.",
    "Yeongin’s inhabitants are hostile toward Han Chinese because a Heavenly Demon Escort Bureau group allegedly massacred approximately two hundred nearby villagers.",
    "The Heavenly Demon Escort Bureau group came from Sichuan, included one woman and nearly thirty men, and all of them later died from deadly venom.",
    "The woman in the Heavenly Demon Escort Bureau group may have been the Southern Heaven Demon Empress, but the innkeeper did not recognize her likeness and she may have used a disguise technique.",
    "The Nanman Beast Palace remains the Fire Dragon Pavilion’s primary mission objective.",
    "The Peak-grade Chain Quest requiring contact with a Hidden Shadow Pavilion agent in Nanman has reached its contact stage in Yeongin."
  ],
  "continuity_sources": [
    619
  ],
  "open_questions": [
    "Was the woman in the Heavenly Demon Escort Bureau group the Southern Heaven Demon Empress?",
    "Who poisoned and killed the Heavenly Demon Escort Bureau group, and why?",
    "What information or assistance will the Hidden Shadow Pavilion agent provide?",
    "What dangers and plans await the Fire Dragon Pavilion at the Nanman Beast Palace?"
  ],
  "safe_through": 619,
  "temporary_decisions": [
    "Render 天魔镖局 as Heavenly Demon Escort Bureau.",
    "Render 蛮族 as Man people.",
    "Continue rendering 永仁 as Yeongin and 毒华楼 as Poison Flower Pavilion."
  ],
  "version": 1
}

## Reading copies

## Chapter artifact 615

# Chapter 615

The road to Yunnan Province—the region officially known by that name, though people in the Central Plains commonly called it Nanman—was long and arduous.

*Prrrff. Prrf.*

The horse’s breathing was ragged.

We had been riding without a break for a full four shichen since leaving Mount Daebyeol.

After entering Hubei on the fine horses Ju Hwaran had procured, we finally loosened the reins for a moment in an unfamiliar ravine.

“If we travel only like this, it will take a considerable amount of time. You’ve been to Sichuan before, Pavilion Master, so you know that, don’t you?”

“Me?”

Of course I knew. Just thinking about it made my calves cramp even now.

I unconsciously nodded at Ju Hwaran as she asked me with her clear, sparkling eyes.

“Of course. It was really fucki—”

“Pardon?”

“It was a little… difficult. A little.”

I barely stopped myself from saying that something almost fell off back then.

I, Jin Taekyung, was endlessly cold-blooded toward men, but a gentleman—warm and considerate—toward women.

Of course, despite having lived this long, I had never once been in a relationship.

“Even using a movement technique, it took nearly half a month.”

“Just getting as far as Sichuan is a distance of well over three thousand li. And considering that you must have traveled without any shortcuts, that’s remarkable.”

I felt good about being praised, but she probably hadn’t started this conversation just to compliment me.

At my meaningful glance, Ju Hwaran smiled and pulled an old leather scroll from inside her robes.

*What’s that?*

Just as I began to wonder, Song Ilseom, who was sitting in the saddle and inspecting the edge of his willow-leaf saber, spoke with an unexpected look on his face.

“It’s made of horsehide. Is it perhaps something belonging to the horse caravans?”

Ju Hwaran nodded.

“You recognize it. You’re right. More precisely, it’s a map they used.”

“I’ve heard that a map of the horse caravans is a treasure that cannot be obtained even for ten thousand gold pieces.”

“As the Young Bureau Head of the Yongbong Escort Bureau, I can tell you that there is nothing in this world that cannot be obtained with wealth. But my grandfather gained a friendship more precious than gold. He received this map as a token of it.”

Hmm. I see.

*…Actually, I didn’t understand a damn thing.*

Aside from the fact that Ju Hwaran’s grandfather, Escort King Ju Gongsan, had received an amazing map from someone belonging to a place called the horse caravans.

After patiently listening to the two of them, I opened my mouth.

“Um, Young Lady Ju. Sorry, but what exactly are the horse caravans?”

“They are descendants of the northern mounted tribes.”

“They traveled along the ancient trade routes for hundreds of years, carrying goods from the Outer Lands and the Central Plains back and forth. Their numbers have dwindled considerably over the years, though.”

“……”

Well, all right. I understood what the horse caravans were now.

But I was pretty sure I had asked Ju Hwaran. Why were the answers coming from two dark-clad men?

Song Ilseom and Sama Pyo had spoken almost simultaneously, and now they looked at each other.

“You’re more knowledgeable than you look.”

“Than I look? Have you forgotten where the Black Dragon Demon Gate is located? Horse caravans are still active in Gansu, where our sect is based.”

“Active? You mean being squeezed dry?”

Song Ilseom gave a short laugh and continued.

“I’ve heard the rumors. The Black Dragon Demon Gate has seized control of the trade routes and collects enormous tolls.”

“I heard you were a wandering martial artist. Do you have some bad blood with our sect?”

“Not particularly. I just want to kill any demonic, heterodox practitioner I see.”

“We agree on that point. I can’t stand meeting people who draw their weapons before anything else. So, are you finished tending to your weapon?”

“Not yet. But we’ll be getting blood on it soon enough, so there’s no harm in doing it later.”

“Then let’s move somewhere else for a while.”

What the hell was happening to the conversation?

I stared blankly at the two men as they amicably turned their horses around, then opened my mouth.

“Move somewhere else for what, you lunatics?”

Song Ilseom and Sama Pyo answered at the same time.

“It is a personal matter. Do not interfere.”

“We need to let the horses rest anyway, so have some tea while we’re gone. We’ll be back shortly.”

“……”

One was an individualist, and the other was Guan Yu.

When the Nanman expedition, which had set out with such high hopes, began showing signs of cracking right from the start, I had no choice but to intervene as the Fire Dragon Pavilion Master.

*Whish!*

Two sharp blasts of air rang out.

Song Ilseom and Sama Pyo landed on the ground after avoiding the Finger Qi I had fired at them. Just as they reflexively began to draw their weapons, I warned them in a calm voice.

“You’ll regret drawing those.”

“……!”

“……!”

It wasn’t merely a verbal warning. The two men froze when they felt the immense qi pressing in from every direction.

Unmistakable astonishment appeared in their trembling eyes.

*He’s strong.*

That was what their gazes said.

And it was an undeniable fact.

Sama Pyo, the Black Dragon Saber, was the Young Sect Leader of the Black Dragon Demon Gate, Gansu’s dominant power, and the foremost young prodigy of the unorthodox faction. Song Ilseom, the Soul-Chasing Guest, had become a legend after cutting down countless enemies on fierce battlefields and in life-and-death duels. Both of them must have understood it clearly.

No, they could understand it all the better precisely because they were not mediocre Peak masters.

A person standing at a higher place could see farther and grasp the whole picture.

*I was already two moves above them before, but the pressure they’re feeling now must be much greater.*

As always, I had grown stronger after waking up than I had been before falling asleep.

That was because I had gained a small insight while developing and systematizing a mass-produced martial art for modern Hunters.

Of course, I hadn’t created some earth-shattering martial art, so it wasn’t enough to call it a great advance…

But even moving forward a quarter of a step was a major achievement.

It was merely unfortunate that the first people to experience that achievement were allies rather than Dark Heaven.

“There are several thousand li left to travel. But if you still want to fight, then fight right now until one of you dies. If not…”

“Pavilion Master.”

I certainly had goodwill toward Ju Hwaran, but now was not the time to listen to her.

I shook my head slightly at Ju Hwaran, whose expression had gone rigid, and continued.

“If not, the two of you can join forces and come at me. You won’t get another chance, now or ever.”

“……”

“……”

Song Ilseom and Sama Pyo kept their mouths tightly shut as they stared at each other. It did not take long for them to reach a decision.

*Shrrrk. Click.*

With a cold scraping sound, the two blades that had been faintly exposed disappeared from view.

Ju Hwaran watched the two men climb back into their saddles as if nothing had happened, then let out a small sigh.

“Whew… I had hoped nothing like this would happen.”

So did I. But it was also something I had thought long and hard about before accepting those two into the Fire Dragon Pavilion.

*Their feelings toward each other probably aren’t very good. Especially from Song Ilseom’s perspective.*

Everything had begun with a feud that went back several decades, to the time when the orthodox and demonic factions had divided the world between them and fought a decisive battle.

A young and bold escort bearing the surname Zhu accepted a commission from a certain woman and created a new legend known as the Ten-Thousand-Mile Escorts. The child that woman bore grew up strong, then left behind a son and passed away.

That son was Song Ilseom—the last descendant of the Guangdong Chen Family, which had been wiped out by demonic, heterodox arts.

Unless he was Buddha or Jesus, it was only natural that he would harbor hatred toward the unorthodox faction.

*I just didn’t expect it to blow up this soon.*

Shit, we’d only been on the road for a few shichen. Were there already signs that this whole thing was falling apart? I was beginning to understand why college students hated group projects so much.

And that was true even if I excluded the two men who had become archenemies faster than anyone in Murim history.

“Captain, maybe it’s because I got hit in the stomach earlier, but I really need to take a shit.”

“My lord. Do not fight. Taishan worry when my lord in danger. Taishan hungry.”

“……”

Look at this lineup.

*For fuck’s sake.*

Watching Hyuk Mujin, whose stomach was more active than his body, and Taishan, the Tiger Giant Child, who seemed to have an inventory instead of a stomach, made my vision go dark.

But even in this bleak situation, there was one ray of light.

“Young Lady Ju.”

“Yes?”

“Thank you. I’m really glad you’re here.”

I meant it. Setting aside whether she was beautiful, wasn’t she the most normal person here?

It was true that her martial arts were slightly weaker than those of the other members, but she had extensive knowledge of Murim and was excellent at finding her way.

The fact that she had found a shortcut known only among the horse caravans proved it.

But why wasn’t she answering?

“Young Lady Ju?”

“……”

“Um, Young Lady Ju?”

Even when I called her again, no answer came.

Still holding the reins in silence, Ju Hwaran turned her head away and stammered.

“I-I think we should take this road.”

“What? No, you certainly did a great job. I mean…”

“I’ll go ahead and look for the horse caravans’ markers. Hyah!”

“Whoa. Whoa, whoa?”

I had no time to say anything else.

I could only stare blankly at Ju Hwaran’s back as she hurriedly rode away, her body moving as one with her horse. Then I felt an irritating prickling at the back of my head and turned around.

*Why are these guys acting like this now?*

Song Ilseom. Sama Pyo. Hyuk Mujin. Even Taishan.

Exactly four pairs of eyes were fixed in place, staring holes through me.

Their mysterious gazes were impossible to interpret. I flinched instinctively and asked,

“What? Why is everyone staring at me like that?”

“Hmm. It is nothing.”

“Let us go ahead, Pavilion Master.”

Song Ilseom and Sama Pyo slowly urged their horses forward, their expressions complicated. Hyuk Mujin and Taishan answered with dubious looks.

“Uh, I was just looking. Because I need to take a dump.”

“If you need to take a dump, why are you looking at me?”

“When I look at you, whatever was about to come out goes right back in.”

“Taishan. Taishan was just looking because hungry. Nothing else.”

“Why the hell would your hunger have anything to do with me?”

“No. Just… just. Hmm. Taishan understand now. Taishan know a little more.”

What kind of bullshit was that supposed to be?

I could understand Hyuk Mujin, but having that giant glutton look at me with such pity was deeply unsettling.

Before I could press him for an explanation, Taishan slapped the rump of the half-dead thoroughbred and charged off.

“Taishan! Go! Horse go too!”

The thoroughbred, already half-dead, staggered into motion. Hyuk Mujin hurriedly followed after him.

“Hey, wait! Let’s go together!”

“No! Do not follow! Taishan only look ahead and run!”

“I have jerky.”

“Taishan! Found friend! We together forever!”

Those lunatics…

But why did I feel like I was the one being ignored by those lunatics?

I grabbed the reins with an expression like I had bitten into something foul.

“Hey. Let’s go, too.”

*Prrrff.*

“……”

Now even the horse was making an annoyed face.

I smacked the horse on the head as it snorted, then squeezed its sides hard.

With a small whinny, the fine horse raced through the ravine.
## Chapter artifact 616

# Chapter 616

To become a successful merchant in Murim meant surviving fierce competition.

In that sense, the map said to have been made by the horse caravans as they traveled between the Outer Lands and the Central Plains was more than enough proof of how they had managed to accumulate such immense wealth.

“This is the right place. It’s faint, but there’s no mistaking it—it’s a horse caravan marker.”

“Huh. I never knew there was a road through a place like this.”

Secret shortcuts hidden throughout the Central Plains, swift and accurate despite their concealment.

Some had vanished completely over the years, while others were so treacherous precisely because they were hidden, but neither posed much of a problem for us.

“Captain, isn’t the slope too steep here?”

“It is. And the road’s narrow, too. But we have to go, so what else can we do?”

“Then I’m afraid we’ll have no choice but to abandon the horses.”

“Abandon what? We can carry them.”

“Pardon?”

Correction. It wasn’t *us* who had no problem with it. It was *me*.

Everyone who heard my words opened their eyes wide.

“What did you say?”

“They aren’t even big warhorses. They were brought in from the grasslands, so they shouldn’t be that heavy, right?”

“……Even if they’re light, they’re still horses. Can you really do that?”

As it turned out, I could. And far more easily than I had expected.

I was already the possessor of physical strength that had far surpassed human limits, so I slung two horses over my shoulders and strode up the mountain. Taishan, who was not as strong as I was but was a natural strongman with a massive build, could manage as many as three.

“Pavilion Master. Taishan heavy. Cannot help it. One horse eat here. No, leave it here.”

“……Swallow your saliva and say that again.”

In truth, that guy’s appetite was a bigger problem than the horses’ weight.

And in proportion to the time and distance we had saved, even greater obstacles were waiting for us.

“According to the map, there should definitely have been a road ahead. But…”

“The road has vanished. More precisely, it appears to have been blocked.”

“Escort Song is right. I heard there was a landslide in the area a month or two ago. It seems the road was blocked then.”

“This time, I’m afraid we have no choice but to turn back. According to the map, we would have to travel at least ten li along this road. Unless it were a distance of a few dozen *jang*, clearing a road buried like this would be absurd…… Pavilion Master, what are you doing?”

“Preparing to clear the road.”

“What?”

“We aren’t exactly going to dig through the entire mountain. If we clear away some dirt and move the rocks and boulders, it looks like we can pass through. You said it happened only a few months ago, right?”

“No, that’s true, but…”

“As they say, when the body is weak, the head has to suffer.”

“……That sounds strange. Isn’t it usually the other way around?”

“Usually, yes.”

For several days, we carried horses up mountains, dug through buried roads, and alternated between walking and running.

At an insane speed, we crossed Hubei and reached Sichuan.

All of it was thanks to Ju Hwaran, who knew the shortcuts shared only among a handful of old horse caravans and remembered all the information left behind by her maternal grandfather, the Escort King.

*I can’t believe we got here this quickly.*

Even without using the waterways, we had traveled at an astonishing speed.

Of course, I had played no small part in making the impossible possible, but Ju Hwaran had fulfilled her role exactly as she had claimed she would before joining the Fire Dragon Pavilion.

No, given the results, she had exceeded my expectations.

*Martial arts really aren’t everything.*

No matter how much of a Supreme Peak master I became, I couldn’t do anything like this. I gave Ju Hwaran a heartfelt exclamation of admiration.

“You’re incredible. There’s no one like you, Young Lady Ju.”

“I’m going to feed the horses some hay.”

“What? Why? They aren’t Taishan. How long has it even been since they ate hay…… Young Lady Ju? Young Lady Ju?”

What the hell was this?

At this point, I couldn’t tell whether she couldn’t hear me or had simply decided not to.

As I watched Ju Hwaran hurry away using a movement technique, I turned my head at the gaze I felt from beside me.

*Swish!*

The movement had been as swift as lightning, but it couldn’t escape my sharp eyes. I stared suspiciously at the culprit.

“Hey.”

The man flinched.

“I saw everything. Don’t pretend you don’t know what I mean.”

At my certain accusation, Song Ilseom, who had been sitting by the water, awkwardly looked around.

“Hmm. Were you perhaps speaking to me?”

“Sorry, but you’re the only one nearby. And you do realize your expression is incredibly awkward, right?”

“……I have no idea what you’re talking about.”

“If you were watching, then you were watching. Why are you trying so hard to hide it? And do you sharpen that willow-leaf saber whenever you get the chance? By the time we reach Nanman, it’ll have turned into a needle.”

*Splash.*

Song Ilseom poured water over the blade, which gleamed like a mirror after being polished with extraordinary care. He deliberately hardened his expression before answering.

“Watch your mouth. This weapon has a special meaning to me.”

He had never been particularly expressive, but seeing him turn so sternly made it seem as though there really was a story behind it.

*Then again, that guy has quite a history.*

Hurting someone else’s feelings was a terrible thing to do.

I had paused, thinking that I might have made an inconsiderate mistake, then carefully opened my mouth with an apologetic expression.

“Hmm. Is it a treasured blade passed down through your family or something?”

“Impossible. I heard that my family could not bring out even a single martial arts manual. My grandmother never learned martial arts in her entire life. It was a miracle that she survived that war at all.”

“Well, it did look pretty worn for a treasured blade. Then is it a keepsake from your father?”

“That isn’t it either.”

As if reminiscing about happier days, Song Ilseom raised a wistful smile to his lips. He ran his hand along the blade as he continued.

“I received this willow-leaf saber when I was young, while serving as a sword boy for a Third Rate wandering martial artist. I cut a person with it for the first time in my life. I was probably twelve.”

“……Oh. I see.”

*Emotional scars, my ass.*

The guilt that had cautiously begun to rise within me melted away like snow in spring.

He had been born a martial artist from the start. Song Ilseom, who cherished the memory of his first killing, looked completely insane.

*Yeah. This guy isn’t right in the head either.*

There were all kinds of people in Murim, but most of them were, by and large, lunatics.

Perhaps that was because Murim was a place no one could survive without being insane.

You could die while eating. You could die while fighting. Even if you somehow survived all the hardship, your wounds could worsen and kill you.

Even after becoming a master through years of suffering, you could die from qi deviation while training.

*What was the title again? In that martial-arts novel I read before, there was even a scene where someone retired peacefully through golden-basin handwashing.[^1]*

Only after coming to Murim did I realize that novels really were nothing more than novels.

When I once asked Jeok Cheongang about golden-basin handwashing, he had answered me like this.

“Golden-basin handwashing? Easy.”

“Oh. It’s easy?”

“Of course. First, buy a basin made of gold. Then invite a whole crowd of close acquaintances.”

“It already reeks of social butterflies and capitalism, but all right. What comes next?”

“Wash your hands in peace. Of course, the moment you take your hands off your weapon, an assassin hiding among your acquaintances will throw a hidden weapon at you.”

“Ah….”

“And one more thing. The person you thought was an acquaintance might be an assassin, too. What do you think? Isn’t it easy?”

Just as my dear Fire-Rice Grandpa’s famous words suggested, this was how fucking Murim was.

Forget golden-basin handwashing or any other bullshit. Most martial artists ought to be grateful simply for waking up in the morning and washing their faces with ice water.

After all, the next day they might have to bathe and purify themselves in the waters of the Sanzu River instead of ice water.[^2]

Of course, if things went that far, it was similar to golden-basin handwashing in the sense that it meant retiring.

The only difference was whether you were still breathing.

*This isn’t Murim Escape Number One.*

It was an old program that had already been canceled, but if it came to Murim, it would be an instant smash hit.

Assuming television had been introduced, it might even reach a 107 percent viewership rating—like the turnout in a Russian presidential election.

A master of demonic, heterodox arts hired as an experiment expert would give everyone a friendly smile and conduct the experiment himself.

“All right, fellow martial artists. What do you think will happen if you dodge like this in this form?”

*Stab.*

“See? Dead. Heh heh.”

The experimenters wouldn’t survive for long……

It was all just my imagination, but Murim was the kind of place where it could become reality the moment television arrived.

In this insane world, I had to drag around a bunch of lunatics and fight other lunatics.

“……Hoo.”

Feeling sorry for myself, I silently stared at the river. That was when Song Ilseom suddenly spoke.

“I really was watching.”

“Hm? Watching what?”

“What happened a moment ago. I realized I never answered you.”

I had wondered what the hell he was talking about. I shrugged and answered.

“I knew you were watching. Why were you staring?”

“Because I heard a sound, so I looked.”

“Be more honest.”

“Your words and actions looked so stupid that I couldn’t help staring.”

“……Oh. That’s very honest.”

“But it’s the truth. Isn’t that why Young Lady Ju keeps leaving whenever you say things like that?”

For some reason, I felt wronged.

“What did I even do? I was just sincerely admiring her and complimenting her.”

“That is something not even a passing dog would believe.”

“But it’s true.”

“Stop. It isn’t funny.”

“I haven’t found it funny from the start.”

“Fine. Let’s say that’s so.”

Song Ilseom gave a quiet laugh as though he had just heard a joke. Then he looked at my expression and asked in a dubious voice,

“Is it true?”

“I’m telling you, it’s true.”

“You’re saying that, without a single lie, you have no idea what your words and actions mean? You truly don’t know why Young Lady Ju keeps leaving whenever you do that?”

“I swear to heaven, I’ll stake my balls.”

“Huh. You’re staking your own balls instead of Hyuk Mujin’s…… It must be the absolute truth.”

The verification process seemed a little strange, but since I had managed to get my sincerity across, I decided to let it go.

Now that Song Ilseom fully believed me, he stared at me as if he had seen a unicorn.

“How can a person be like this?”

“What?”

“You said your old sobriquet was the Night King, didn’t you? Then common sense dictates that you should at least know the basics.”

“……”

How long was I going to have to clean up the shit left behind by that promiscuous predecessor?

If it had been the Porn King, I could have admitted to it in good conscience to some extent. But the Night King?

“……It’s a long story.”

At my sighing answer, Song Ilseom nodded.

“Of course it is. You must have spent many long nights.”

“You son of a bitch. Draw your sword. You’re fucking dead today.”

“Unfortunately, we’ll have to put that off until later. Thanks to you, I have to find an employer who still hasn’t appeared even after fifteen minutes.”

“You seem to have forgotten, but I’m the Fire Dragon Pavilion Master. Your direct superior.”

“But the person who gives me silver nyang is my employer. And my mission is to protect that very employer.”

Song Ilseom secured the well-polished willow-leaf saber at his waist and rose from the water’s edge.

Step. Step.

Without even saying goodbye, he turned and walked away over the sand and gravel. Then, all at once, his figure came to a stop.

“If you don’t know why Young Lady Ju acts that way, think about it carefully with that nonexistent sense of tact you have. You have to find the answer yourself.”

“What?”

“She may look strong, but she’s a woman who has suffered a great deal. I hope she never has to be hurt or meet a pointless death.”

Those were his final words.

As I watched Song Ilseom’s back, he resumed walking as though nothing had happened. A thought suddenly occurred to me.

*Is that guy really staying by Ju Hwaran’s side because of silver nyang?*

Before I could find the answer to that question, a resonant sound filled the surging Yangtze in Sichuan.

*Boom. Boom-boom. Boom!*

Powerful drums. The prows of ships cutting strongly and swiftly through the current.

By then, a dozen or so swift ships had emerged through the fog, with the flags of the Water Dragon Stronghold fluttering above them.

I muttered,

“Our taxi’s here.”

[^1]: A ceremonial retirement ritual in which a martial artist washes their hands in a golden basin, symbolizing that they are giving up martial pursuits.

[^2]: The Sanzu River is a Buddhist river associated with the boundary between life and death.
## Chapter artifact 617

# Chapter 617

*Splash!*

A dozen or so swift ships rapidly approaching the riverside were visible to anyone who wasn’t blind.

For a martial artist who had reached a realm stage, it went without saying.

“Water Dragon Stronghold…”

Sama Pyo had used his movement technique to rush over in an instant. He muttered while narrowing his eyes at the flags on the swift ships, then shifted his gaze toward me.

“You told me to wait a moment. Was this why?”

“Yep.”

“Sichuan is a land filled with treacherous terrain, so if we travel down the Yangtze, we can certainly move faster than we are now. Still, I’m somewhat concerned that our counterparts are the Yangtze River Channel League.”

There was a good reason for the distrust faintly visible in Sama Pyo’s expression.

The Yangtze River Channel League was, at its core, a group of water bandits whose livelihood was plunder.

Moreover, the prevailing opinion was that the Seafaring King, Pa Ryun, was a deeply sinister man, quite apart from his personal martial prowess.

*He didn’t attend the formation of the Murim Alliance, either, for some reason.*

I didn’t know whether it was because of illness or the distance.

All he had done was send an envoy to convey his intention to join the Alliance and make an official announcement. Of course, the same was true of the Green Forest Alliance.

These two forces were closer to the unorthodox faction than the orthodox faction. More accurately, they were plunderers who had established powerful domains of their own.

“I hear Pa Ryun is a man whose true intentions are impossible to read. Rumors about him have even been circulating quietly in Henan.”

“You mean the kind of man who’ll sell out to Dark Heaven when the time comes?”

“Sounds like you’ve heard them.”

“Are my ears just decoration? And since we’re on the subject…”

I looked at Sama Pyo and continued in a low voice.

“If the public opinion you mentioned is accurate, then the Yangtze River Channel League and the Black Dragon Demon Gate are two of a kind.”

“……”

“Am I wrong?”

After a brief silence, Sama Pyo replied with a bitter expression.

“Now that I think about it, it seems you’re right.”

“Not ‘it seems.’ I’m right, you bastard. If you look closely, the Black Dragon Demon Gate is actually worse. At least those guys rob people without discriminating between the orthodox and unorthodox factions. You people are unambiguously unorthodox.”

“……I understand perfectly well. Stop now. Listening to you is making me dizzy.”

Taishan, who had been circling Sama Pyo like a large dog, joined the conversation.

“Lord. Taishan hungry too. Head dizzy.”

“……”

*Watching this is making my head dizzy, too.*

I rubbed my throbbing temple and opened my mouth.

“And one more thing. You don’t need to worry. Those water bandits can be trusted.”

“Trustworthy water bandits. That sounds like a martial artist who hasn’t learned martial arts.”

“It’s a long story. Anyway, we have a pretty strong bond.”

I didn’t know what kind of person the Seafaring King Pa Ryun was.

But even if the public opinion about him was true, my opinion of Ship-Fire Boy Mu Song wouldn’t change.

At least the Mu Song I had seen and known was trustworthy and held to his principles.

It wasn’t as though a Disciple was required to resemble his master.

*I can tell from the fact that they came rushing over the moment we sent word after reaching Sichuan.*

While I was thinking that, the swift ships reached the riverbank, and a dozen or so men poured off them.

*Splash!*

The river water sprayed in every direction at their rough momentum and movements, befitting water bandits who had made their bones on the Yangtze.

Their bronze-colored muscles showed through their loose robes as they ran toward us with flying steps and clasped their hands in salute.

“Great Hero Jin!”

“We came running as soon as we received your message.”

These were Mu Song’s trusted hands within the Water Dragon Stronghold, all at least squad-captain level.

I had seen their faces several times a day the last time I came to Sichuan, but the face I was most familiar with was nowhere to be found.

“All familiar faces. But I don’t see Senior Mu Song.”

The Deputy Stronghold Lord immediately answered my question.

“I’m sorry to say this, but he left for the League’s headquarters two days ago.”

“The headquarters… You mean the headquarters of the Yangtze River Channel League?”

“Yes, sir. It was on the League Leader’s orders, so he couldn’t delay even a moment.”

“I see.”

Within the Yangtze River Channel League, the Seafaring King’s orders were absolute. His direct Disciple, Ship-Fire Boy Mu Song, had no choice but to answer a summons.

I looked at the water bandits with a mixture of regret and gratitude.

“Even so, you managed to come right away. And Senior Mu Song isn’t even here.”

The Deputy Stronghold Lord was startled and waved his hands.

“Oh, please don’t say that. The Stronghold Lord must have had the foresight to anticipate this. Before he left, he gave us very specific instructions regarding Great Hero Jin.”

“Regarding me?”

“Yes. He said that if a person had received help, they absolutely had to repay it. There’s also the matter concerning the late Yangtze One Saber, Great Hero Hwang. So if the Jin Family of Taiyuan or Great Hero Jin ever needed help, he told us to do everything within our power.”

“Oh. Senior Mu Song truly understands honor. He’s a real hero.”

*See that, you bastard?*

I smiled with satisfaction and glanced at Sama Pyo.

Just then, one of the larger water bandits standing nearby whispered to the Deputy Stronghold Lord with a bewildered expression.

“Deputy Stronghold Lord.”

“Yes?”

“Didn’t the Stronghold Lord also say that since Great Hero Jin was obviously going to raise hell if we didn’t help, we should just give him whatever he wanted instead of letting him wreck perfectly good swift ships?”

“Ah. Right. Jang Pil, you little—!”

“……”

“……”

Silence descended in an instant.

Never mind the water bandits. The gazes of the proud members of our Fire Dragon Pavilion were painfully sharp.

As the entire area fell silent, Ju Hwaran muttered in a voice so quiet it was almost inaudible.

“What on earth have you been doing to make even water bandits…”

Her words had struck deep. I felt my chest grow heavy as I looked out over the endless Yangtze.

I wanted to offer some kind of excuse, but it was true that I had thrown tantrums here and there and used them like a taxi. I had nothing to say.

“In some ways, you’re worse than the unorthodox faction.”

I did my best to ignore Sama Pyo’s final remark and looked at the Deputy Stronghold Lord with mournful eyes.

“Let’s just set off.”

“Yes, sir.”

“And Deputy Stronghold Lord, come with me later. Bring that Jang Pil fellow, too.”

“……”

The Deputy Stronghold Lord stared at me in terror for a moment before shouting in a choked voice,

“Raise the anchor! Raise the anchor!”

I must have imagined the tearful note in his voice.

* * *

*Whoosh!*

The bow of the ship swiftly and powerfully cut through the river water.

Spring had arrived, and the wind was blowing in our favor. The water bandits’ rowing, honed through years of plunder, had reached a level no one else could match.

Of course, even though these were fairly decent water bandits who had been reformed by Mu Song, their innate instincts remained.

“Five ships spotted to the southeast!”

“Oh, Deputy Stronghold Lord. They’re sizable merchant ships!”

“Merchant ships? Then let’s rob them!”

*What the hell are you robbing them for in the middle of this, you lunatics?*

As everyone, myself included, watched the situation with dumbfounded expressions, the Deputy Stronghold Lord’s face twisted.

“You idiots! We have honored guests aboard! What do you think you’re doing? Do you people have no basic manners?”

“S-sorry.”

For a water bandit, he sounded exactly like Judge Bao.[^1]

After sternly rebuking his subordinates, the Deputy Stronghold Lord approached us and bowed politely.

“We’re sorry for showing you such an unbecoming side of ourselves.”

“Heh heh. It’s nothing.”

I smiled amiably and continued.

“I understand. This is your line of work, after all. I can see how it happened.”

“Thank you for understanding. In that case, we’ll rob them quickly and set off again.”

“Huh?”

“It’ll take half a shichen at most. We’ll do a quick job and send them on their way…”

“Get down.”

There had been a slight incident, but after I made the Deputy Stronghold Lord drop and hold the push-up position a few times, even that impulse disappeared.

The swift ship continued onward with the wind at its back.

One day, two days. Three days…

As time passed quickly, the Fire Dragon Pavilion members, who were now confined to the ship, focused on their respective tasks.

*Swish! Whoosh!*

Sama Pyo and Song Ilseom devoted themselves to their own martial arts training after the first day without a single clash between them.

“Taishan likes sashimi. But no fish caught. Give Taishan one.”

“This guy has no shame. I went through all that trouble to catch a few fish, and now he wants them? Captain, this fellow keeps pestering me. Can you get him away from me?”

“Hand over all the fish you’ve caught so far. Obviously, slice them into sashimi, too.”

“Taishan impressed. Is Pavilion Master a genius?”

“……”

Hyuk Mujin and Taishan spent most of their time fishing at the bow.

Of course, there were plenty of days when they caught nothing, and even when Hyuk Mujin did catch something, someone else would often take it away from him. Still, he didn’t complain much.

And I knew the reason wasn’t that he had given up.

Fishing itself wasn’t even about catching fish.

*That’s why he doesn’t say anything.*

Hyuk Mujin was fishing so he could empty his mind, even if only in that way.

Even when the bobber trembled right in front of him, he didn’t bother yanking on the fishing rod. Every night, he locked himself in the cabin to practice martial arts or devote himself to circulating his qi.

As each day passed and we drew closer to Yunnan, everyone prepared for a possible battle in their own way.

I was no different.

*Open the Quest window.*

*Ding.*

> **System**
>
> **Quest**
>
> **Journey to Nanman**
>
> Murim Alliance Leader Mae Jonghak has assigned the Fire Dragon Pavilion its first mission.
>
> You must now head to Nanman and actively respond to any situation that may arise.
>
> There is no way to know what lies ahead for you and the Fire Dragon Pavilion.
>
> Always remain vigilant and act with a flexible mindset.
>
> **Grade:** Peak
>
> **Restriction:** Jin Taekyung and Fire Dragon Pavilion members
>
> **Mission:** Enter Nanman (Incomplete)
>
> **Reward:** Chain Quest
>
> ???
>
> **Failure:** Obtain Title: Can’t Go to Nanman
>
> Fame and trust greatly reduced

In terms of time spent in Murim, I had received this Quest about half a month ago.

Counting the time in the modern world, it had been more than a month.

I was carefully examining the Quest window again to see if I had missed anything when a faint floral scent mingled with the breeze.

“Why are you staring so intently at empty space?”

It was Ju Hwaran.

I closed the holographic window and gazed seriously at the night sky, thick with stars.

“I was reading the heavenly patterns.”

“Oh. Really?”

“Yes. Really.”

“That’s impressive.”

Ju Hwaran let out a quiet laugh and asked,

“So what did the heavens tell you?”

“They said the weather would be nice today.”

“Really?”

“Yes. Young Lady Ju, you see the Big Dipper over there?”

Ju Hwaran looked up at the sky along my pointing finger and blinked.

“Oh. Um.”

“What is it?”

“Pavilion Master, I’m sorry, but that isn’t the Big Dipper.”

“……That can’t be right. Did its shape change in the meantime?”

“What?”

*What kind of nonsense was that?*

The words were already out before I realized how ridiculous they sounded. When I scratched my chin in embarrassment, Ju Hwaran burst out laughing.

“You read the heavenly patterns in an interesting way.”

“To be honest, I don’t know much about heavenly patterns. I just deal with things as they come and act according to the situation.”

“I know. Still, it makes me want to hear more. As it happens, there’s something I’ve been curious about personally. May I ask you about it?”

I smacked my lips before answering.

“I already told you, but I don’t know how to read the heavenly patterns.”

“I already told you that I know. And this isn’t something I want to ask the heavens about. I want to ask you.”

“If that’s the case, then there’s no problem. I’ll answer anything I can.”

*Tap.*

Ju Hwaran lightly jumped onto the bow and looked out at the pitch-black river before opening her mouth.

“What do you think will happen from here on? To us?”

With Nanman so close, Ju Hwaran was undoubtedly anxious.

*How can I reassure her?*

After thinking for a moment, I opened my mouth.

“I don’t know. There’s a strong possibility that Dark Heaven is plotting something, but it’s also possible that nothing will happen.”

Nanman was a remote region, so far away that it was classified as the Outer Lands.

It was also a vast territory home to the Nanman Beast Palace, the dominant power in Nanman, as well as numerous ethnic groups, including the Miao people.

If my ominous suspicion was entirely correct and Dark Heaven was plotting something in Nanman, countless dangers would be waiting for me and the Fire Dragon Pavilion.

But…

“Nothing will happen. Whatever happens, we’ll be able to return home safely. I promise you that much.”

Ju Hwaran didn’t answer.

Instead, she looked at me with an unreadable expression for a moment—or rather, for a very long time.

“Young Lady Ju?”

“……I see.”

A short voice finally emerged from the silence.

With a faint smile on her lips, Ju Hwaran gently shook her head.

Her glossy hair, which even the human-skin mask couldn’t conceal, rippled like the river.

“I’ll trust you, Pavilion Master.”

“……?”

Something felt off.

I was wondering whether I had given the wrong answer when the Deputy Stronghold Lord appeared with a torch, his face flushed with excitement.

“Great Hero Jin. We’ve arrived.”

“……!”

[^1]: Judge Bao, or Bao Qingtian, is a legendary incorruptible magistrate celebrated in Chinese folklore and popular fiction.
## Chapter artifact 618

# Chapter 618

Before anyone knew it, the air had turned hot and muggy. In the distance, high mountains and deep valleys came into view.

The Deputy Stronghold Lord of the Water Dragon Stronghold pointed toward the rapidly approaching shore.

“This is as far as we can take you, Great Hero Jin. Once you disembark and walk ten li straight ahead, you’ll be in Yunnan. You should arrive in no time.”

The Yangtze’s tributaries covered an incredibly vast area across this continent, but they did not extend all the way into the interior of Yunnan Province.

No—that wasn’t strictly true. They didn’t simply cut off all at once.

The problem was that if we continued along the waterways to the plateau in northern Yunnan, it would actually take much longer to reach our destination.

*Our highest priority is the Nanman Beast Palace, after all.*

The Quest I had received required me to reach Nanman, but the Fire Dragon Pavilion’s mission required us to head for the Nanman Beast Palace.

With that thought in mind, I gave the Deputy Stronghold Lord a small bow.

“Thank you very much. You must be busy raiding merchant ships, yet you still brought us all the way here.”

“Oh, please, don’t say that. You’re no ordinary person. If Great Hero Jin calls for us, we should drop everything and come running at any time. I’m almost sorry to part ways with you, heh heh heh.”

He looked far too happy for someone who was supposedly sorry.

Then again, he’d had to bang his head against the ground and hold a push-up position in front of his men at the drop of a hat. He probably really was happy to say goodbye today.

I laughed along with him and asked,

“Ha ha. Really?”

“Of course. Heh heh.”

“Then it would be perfect if you stayed nearby, wouldn’t it?”

“Heh heh heh. What?”

“We came all this way, but I was worried about having to think about getting back later. But since you just said you’d be sorry to part ways, this works out perfectly.”

“……!”

“So wait nearby.”

The smile vanished completely from the Deputy Stronghold Lord’s face. He stammered,

“Ah, no. That might be a little difficult. We have things to do as well…”

“I understand. I do. So you can send the rest of the ships back and leave one or two behind.”

“G-Great Hero Jin, please don’t do this. Why don’t you send word after you’re finished with your business in Yunnan instead…”

“Hmm. But then I’d have to wait way too long.”

“……”

The happiness that had filled the Deputy Stronghold Lord’s face was nowhere to be found now.

I gently patted his shoulder as he lowered his head in dejection.

“I know it’s an unreasonable request, but let’s impose on you a little.”

“No, even so…”

“Come on. Let’s impose on you a little.”

“……”

“Ah, fuck. Answer me already. You need to conduct yourself properly if you want to survive long in the Murim.”

“Gasp.”

The Deputy Stronghold Lord’s face darkened. His answer might as well have already been decided.

A short while later, I finally extracted a promise that they would remain anchored nearby until we returned. After I disembarked, the gazes directed at me were far from ordinary.

“I felt like I was looking at a Third Rate wandering martial artist.”

“I’m asking this without any ill intent, but is the Jin Family of Taiyuan perhaps rooted in the unorthodox faction?”

“As expected of our Captain. You never disappoint.”

“Taishan thought Pavilion Master was a water bandit.”

“I think the Pavilion Master made the right decision. If something happens in Nanman, we’ll be able to receive their help. Isn’t that right?”

That last answer was the only correct one.

*As expected, Ju Hwaran is the only person who understands me.*

I looked at her with a deeply moved expression.

“That’s right. You’ve expressed my thoughts exactly, without getting a single word wrong.”

“Oh, did you really think so?”

“Huh?”

“I only took your side because everyone else was criticizing you. I thought someone should support the Pavilion Master…”

“……”

*Is my image really okay as it is?*

While I was pondering that question, we continued walking along a crude road that was nothing like the roads of the Central Plains.

Then a familiar sound pierced my ears.

*Ding.*

> **System**
>
> Entered **Nanman**.
>
> Mission, **Enter Nanman**, completed.
>
> Quest, **Journey to Nanman**, successfully completed!
>
> Quest completion rewards acquired!
>
> A small amount of EXP acquired!
>
> A small amount of Fame acquired!
>
> Achievement, **Thousands of Li in Search of Nanman**, achieved!
>
> Nanman is a perilous land with erratic weather, filled with all manner of wild beasts and venomous creatures. Outsiders must always beware of endemic diseases and poison.
>
> Acquired: **Advanced Antidote** ×10, **Intermediate Antidote** ×20, **Basic Antidote** ×30!
>
> A new Chain Quest has been created.
>
> Would you like to check the Quest window?
>
> Y / N

The System notifications rang out one after another, and holographic windows filled the air around me.

The Deputy Stronghold Lord had been telling the truth. We hadn’t seen a single person nearby, but after walking for a short while, we had apparently stepped into Nanman territory.

I muttered inwardly while pretending nothing had happened.

*Confirm.*

*Ding.*

> **System**
>
> **Quest**
>
> **Seeds Planted in Nanman**
>
> You have arrived in Nanman after traveling thousands of li, but Nanman is a sparsely populated land where outsiders are not welcomed.
>
> With the limited knowledge and information you currently possess, you cannot act recklessly. Make contact with the Hidden Shadow Pavilion agent planted in Nanman by the Murim Alliance in the past and obtain detailed information.
>
> **Grade:** Peak
>
> **Restriction:** Jin Taekyung and Fire Dragon Pavilion members
>
> **Mission:** Make contact with the Hidden Shadow Pavilion agent (Incomplete)
>
> **Reward:** Chain Quest
>
> ???
>
> **Failure:** Stats decreased

*Hmm.*

Make contact with a Hidden Shadow Pavilion agent.

After reading through the new Chain Quest several times, I recalled the conversation I’d had with Song Ho, the Chief of the Hidden Shadow Pavilion, before leaving Henan.



*“After the Great Faction War ended and the first Alliance Leader, the Martial God, disappeared, the Hidden Shadow Pavilion was naturally disbanded as well. But even now, after several decades have passed, the minimum personnel needed to maintain the intelligence network still remain.”*

*“You mean…”*

*“Didn’t I tell you? The eyes and ears of the Hidden Shadow Pavilion are everywhere.”*



After the Great War that had shaken the world came to an end, people gradually grew accustomed to peace.

But there were others who did not.

The Thousand-Faced Fox Song Ho and the Hidden Shadow Pavilion were like that.



*“Only great righteousness and spirit. They are people who have remained in their places for all these years with those two things engraved in their hearts. Once you arrive in Nanman, look for him first. You’ll be able to receive plenty of help from him, not to mention information.”*

*“How am I supposed to find him? You’re not just going to give me the man’s name and address, are you?”*

*“There is a secret code known only to Hidden Shadow Pavilion agents. I’ll tell you the specific place where the code can be checked. If you go there, you should be able to meet him.”*



It was astonishing when I thought about it again.

Nearly fifty years had passed since the end of the Great Faction War, yet the Hidden Shadow Pavilion’s intelligence network was still alive.

*And in a remote place like Nanman, where they would have been even less inclined to stay.*

But thanks to the sacrifices of people like them, the Fire Dragon Pavilion’s mission would become much easier.

After sorting out my thoughts, I spoke to the Fire Dragon Pavilion members as they moved forward while keeping watch over their surroundings.

“We’re going to Yeongin.[^1]”

[^1]: Yeongin (永仁) is a county seat in Yunnan.

“Yeongin?”

Hyuk Mujin tilted his head and asked,

“I’ve never even heard of that place. Where is it?”

“It’s a county seat about two hundred li from our current location. Of course, it’s far more underdeveloped than any county seat in the Central Plains.”

Ju Hwaran answered in my place and continued,

“It’s also a place where several different ethnic groups live together. That doesn’t mean there are no conflicts, though.”

I sensed something in her effortless answer and tone, so I asked,

“Have you been there before?”

Ju Hwaran smiled gently and nodded.

“Didn’t I tell you? Three years ago, I managed to persuade my father to let me go on an escort journey to Nanman.”

“Ah, so that was Yeongin.”

“Yes. It was a short visit, but I still remember it vividly. Captain Song was with me as well.”

When everyone’s gazes turned toward him, Song Ilseom raised an eyebrow and casually added,

“I never want to come to Nanman again. It was a horrible place. But Yeongin was relatively tolerable. The ethnic groups there were comparatively mild-tempered.”

Considering Song Ilseom’s usual cynical attitude, that was quite a generous assessment.

Then again, that must have been why he had been able to escort a shipment across this rough and dangerous land of Nanman.

“But why are we going to Yeongin?”

At Ju Hwaran’s question, everyone looked at me this time. They had probably all wanted to ask from the beginning but had been holding back.

There was no reason to hide it, so I answered honestly.

“We’re going to meet one of the Murim Alliance’s informants in Yeongin.”

“Then we definitely have to go. News from Nanman doesn’t easily reach the outside world.”

Nanman was the most remote of remote lands.

The dozens of ethnic groups living in the dense jungles were extremely wary of the Han Chinese from the Central Plains. They had also fought countless wars among themselves to defend their respective territories.

That was why even most major Escort Bureaus and merchant organizations were reluctant to travel to Nanman.

If they succeeded, they could acquire rare gems along with various spices and medicinal herbs. But the many dangers lurking in the jungle could also claim their lives.

Even without an ethnic group suffering from anger-management issues, countless poisonous creatures, wild beasts, and highly lethal endemic diseases were serious obstacles.

“But Yeongin should be fine.”

Ju Hwaran smiled brightly and continued,

“Our Yongbong Escort Bureau has had ties with the people there since the time of its former leaders, and the ethnic groups living there are relatively friendly toward the Han Chinese.”

“Oh. Is that so?”

“Yes. You’ll see when you meet them, but they’re all good people.”

* * *

“Caw, spit.”

A thick strand of phlegm landed at our feet.

Living up to the name Bai, or “White,” a tribesman dressed in white glared menacingly at us before disappearing from sight.

I watched him silently, then cautiously spoke to Ju Hwaran.

“Um, I’m asking just in case, but does someone like that count as one of the nicer ones among the ethnic groups?”

“……”

“Young Lady Ju?”

After a brief silence, Ju Hwaran answered,

“Hmm. That man seems to have a rough personality. Most people aren’t like that.”

“Right?”

“Yes, yes. Of course. I know because I’ve been here myself.”

The moment Ju Hwaran finished speaking, a middle-aged ethnic woman dressed in clothes as colorful as a peacock covered a child’s eyes and muttered,

“Oh, my. Those Han bastards dared to come all the way here. Let’s go inside. You’ll ruin your eyes.”

“Mom. Mom. I can’t see.”

“It’s okay, sweetheart. Let’s hurry away from those vicious men. Honey! Come out quickly! Han bastards have entered the village!”

“What? Wait there. I’ll grab a plow and smash the heads of these Han sons of bitches!”

“……”

“……”

I saw it clearly.

For an instant, Ju Hwaran’s pupils shook violently.

With one last shred of hope, I asked her,

“Those people are also just a little rough compared to the average, right?”

“……That’s probably the case. I think.”

But Ju Hwaran’s hopes were brutally ignored.

Before long, the ethnic tribesmen filling the roadside began openly displaying their hostility toward us.

“So they really are Han Chinese.”

“They’ve got some nerve. Contact the chief immediately.”

“I’ve already sent someone.”

“Take the women and children into their homes, and gather the men to keep an eye on those Han bastards.”

I felt like I was a criminal.

No. To them, we were already criminals who deserved to be torn apart and killed.

The other members, who could neither use the System’s translation nor speak the ethnic language like Ju Hwaran, could feel it well enough.

“Captain.”

“What?”

“I think we’re fucked.”

Hyuk Mujin swallowed hard and continued in a whisper.

“I don’t know what they’re saying, but the atmosphere is extremely hostile. Wouldn’t it be better to get out of here?”

“Hmm.”

One of a leader’s duties was to eliminate his subordinates’ anxiety. I answered in a solemn voice.

“It’s not like that.”

“It isn’t?”

“No. They’re just staring because Han Chinese are unusual to them.”

“Then why are they carrying axes?”

“They probably came over after chopping firewood.”

“They’re carrying swords too.”

“They probably came over after slaughtering something.”

“……”

*Don’t look at me like that. You’re making me feel guilty.*

I did my best to ignore Hyuk Mujin’s distrustful gaze and crossed through the ethnic tribesmen radiating a menacing aura.

We stopped in front of a wooden building.

**Poison Flower Pavilion**

The sign was so old that it looked as though it might crumble at any moment.

It was the meeting place the Thousand-Faced Fox had told me about.
## Chapter artifact 619

# Chapter 619

Poison Flower Pavilion…

It was a name that suited Nanman, a land crawling with all kinds of venomous beasts. The catch was that it looked more like a crumbling mansion than an inn or pleasure house.

*If the Thousand-Faced Fox’s directions were right, this should be the place.*

As I stared suspiciously at the wooden building that looked old enough to crumble at any moment, the atmosphere surrounding the outsiders grew more hostile by the second.

“You fucking Han bastards!”

“Go back to your own land!”

Whoosh! Crack!

Sama Pyo dodged the rock flying toward the back of his head and muttered with a sigh,

“Pavilion Master, we’d better just go inside. Unless we plan to fight them right now.”

“Fighting them is out of the question.”

At least this time, he was completely right.

We couldn’t turn every native in Nanman into an enemy the moment we arrived.

I glanced at the group of non-Han locals radiating a murderous aura, then opened the door to the Poison Flower Pavilion.

Creeeeak.

The ancient wooden door let out a weak scraping sound.

Inside the inn, everything was steeped in dim light and a gloomy atmosphere. The patrons sitting at crude tables scattered around the room like weeds turned their heads toward us.

“Faces I’ve never seen before… Han Chinese?”

“Caw, spit.”

Is this a Hydra?

The people around here used phlegm like a passive Skill.

The ethnic patrons spat onto the dusty floor and rose from their seats, their faces flushed red.

“Those Han bastards dare come here of all places. Are they desperate to die?”

“I’ve lost my appetite for liquor. Let’s leave. Nothing good can come from staying here with those bastards.”

Bang!

When the door slammed shut behind them, Ju Hwaran spoke with a troubled expression.

“Something must have gone badly wrong. It definitely wasn’t this bad the last time I came here.”

Song Ilseom nodded in agreement.

“I think so too. It’s true that the ethnic groups of Nanman are wary, but Yeongin, which is closest to the Central Plains, was different.”

“That’s right. It wasn’t common, but merchants and Escort Bureaus from the Central Plains used to travel through here. But why…”

Ju Hwaran let her voice trail off when an elderly voice suddenly interrupted from somewhere.

“Why? Because of that Escort Bureau. Those Han bastards just like you.”

We weren’t the only ones left in the Poison Flower Pavilion.

The old man, who had been sleeping off his liquor until a moment ago, continued while rubbing his bent back.

“You’ve all been cursed with bad luck. You lot, for crawling all the way into Nanman without knowing what you were getting into. And some old man whose business is about to be ruined because of fearless Han bastards like those.”

I realized who the old man was and asked,

“Are you the owner?”

The old man looked at me in surprise when he heard the fluent language of the locals flowing from my lips.

“You can speak our language. Are you perhaps one of the Miao people?”

“No.”

“Then you don’t look like the Bai or Man people either. Judging by your face, you’re definitely Han Chinese… but you speak remarkably well. I’d believe you were born and raised here.”

As expected of the *Integrated Language Pack*. It certainly did its job.

Even Ju Hwaran looked surprised by my fluent pronunciation.

“When did you learn the language of the ethnic groups?”

“Hmm. Well, that…”

Since I couldn’t exactly explain everything, I let my voice trail off and answered casually.

“I just happened to pick up the skill. It’s nothing more than a miscellaneous trick.”

Hyuk Mujin, sitting beside me, muttered under his breath,

“The only things our Captain used to know were drinking, women, and gambling…”

“You little shit.”

Bam!

“Urgh!”

The old man clicked his tongue as Hyuk Mujin collapsed, clutching his solar plexus.

“That one sure picks only things worth getting hit for.”

“He’s always like that, so don’t worry about him… Wait. Can you speak Chinese?”

“To a degree. When I was young, I served as an interpreter for the Han Chinese several times.”

The old man answered as though it were nothing important, then pointed at Song Ilseom with a finger reduced to little more than bone.

“That dark-looking fellow seems familiar. Did you perhaps come here around three years ago?”

Strictly speaking, Ju Hwaran should have been the most eye-catching person there. But perhaps because she was wearing a human-skin mask, the old man recognized Song Ilseom first.

Song Ilseom silently nodded, and the old man slapped his knee.

“I knew it. Your name was probably Dragon King…”

“It was the Yongbong Escort Bureau. Not Dragon King.”

“Right. The Yongbong Escort Bureau. Unlike the other merchant groups and Escort Bureaus from the Central Plains, you Han Chinese came here two or three times a year, so I remember you clearly.”

For someone who remembered it so clearly, he got the name wrong right from the start.

I held back the words itching to leave my mouth and asked the question I had wanted to pose to the old man for a while.

“But what did you mean earlier?”

“Hm? What about?”

“You said things had become like this because of an Escort Bureau. To quote you exactly, you said it was because of Han bastards like us.”

The old man asked back with a blank expression.

“I did? When?”

“What? You clearly said…”

“I don’t remember a thing.”

As if hell he didn’t. Realizing something from the old man’s attitude, I spoke with a sigh.

“Food. Can you prepare it right now?”

“Ah, of course I can. I can make anything as long as you pay, so don’t worry.”

At the mention of food, Taishan sprang up from where he had been lying facedown on the table with a dying expression.

“Taishan wants five-spice pork!”

“So there’s one fellow here who’s absurdly full of energy. Then I’ll prepare chicken.”

“Why chicken? Taishan hates chicken! Five-spice pork!”

I had no idea why his request for five-spice pork had somehow been changed to chicken, but for now, we needed to keep the old man in as good a mood as possible.

I immediately called out the name of the one person who could stop Taishan from throwing a fit.

“Ma Pyo. What are you doing?”

“It’s Sama Pyo.”

“Right, Sa-pyo.”

“…”

Sama Pyo glared at me with an unpleasant expression, then turned to Taishan.

“Taishan. Enough. Sit down.”

While he calmed Taishan, the old man casually held out his hand.

“What is it?”

“Payment in advance.”

“Ah.”

“Let’s see. One chicken per person is the minimum, so we’ll need five chickens. And at one silver nyang per chicken… That comes to ten silver nyang.”

“…Ten silver nyang? Even if it’s one nyang per chicken, that should be five silver nyang.”

“Is that so? Then let’s make it two nyang per chicken.”

“What?”

The old man answered boldly,

“Ah. I said let’s make it two nyang per chicken.”

“…”

“If you don’t like it, spit on the floor and leave. For your information, there isn’t another village within a hundred li.”

Talk about shameless price gouging. If he’d been born in Yongsan[^1] some fifty years ago, he would have become a landlord.

[^1]: A central Seoul district where decades of development drove real-estate values sharply upward.

*I wondered why we hadn’t run into bandits on the way here. Turns out they were in the inn, not the mountains.*

The price was no different from highway robbery, but this wasn’t the time to save money.

I took ten silver nyang from the well-filled pouch of expenses I had received from the Murim Alliance and handed them to the old man.

“Here. Ten silver nyang.”

“For a Han, you’re surprisingly reasonable.”

Rustle.

The old man swept up the gleaming silver with a grin.

“That aside. What about liquor?”

“No, thank you.”

“Drink.”

“…”

“I said drink.”

I no longer had the strength to answer.

With a gloomy expression, I opened my pouch again.

* * *

Our first meal in Nanman was impressive in an entirely different sense.

There was a chicken dish so thin and scrawny it looked malnourished. And there was strong liquor that clearly looked like someone had already drunk from it and left the rest behind.

It was astonishing that the old man charged us dozens of silver nyang for this, but even that paled beside the fact that a considerable portion of it had gone into his mouth.

“Burp. That hit the spot.”

“…”

Why were you the one who ate well instead of us?

The question rose all the way to the back of my throat, but I barely managed to swallow it down. We had obtained information in exchange for offering him money and a meal.

“The Heavenly Demon Escort Bureau?”

“That’s right. As I recall, they definitely said they came from Sichuan. There was one woman, and with the other men, there were nearly thirty of them.”

The old man nodded and continued with his face flushed from the liquor.

“At first, everyone thought nothing of it. Han Chinese had come to Yeongin more than once or twice, and their group wasn’t particularly large.”

But that had been a miscalculation.

His eyes red from drink, the old man slowly recalled what had happened that day.

“Something no one could have expected happened. The people from a nearby village held a feast for them and treated them as guests, but every last one of them was slaughtered overnight.”

“…”

“Fortunately, our village avoided the disaster. But when we checked later, we found that some two hundred people had died that very night. Men, women, children, even the elderly. Not a single person survived. Needless to say, those Han bastards were responsible.”

“Damn.”

It was a shocking and horrific story. Only now did I fully understand the hostile looks and oppressive atmosphere that had been directed at us.

Two words came to mind.

*Dark Heaven. And the Southern Heaven Demon Empress.*

It was hardly an overreaction to be troubled by one woman who had been part of the Heavenly Demon Escort Bureau.

I exchanged glances with the Fire Dragon Pavilion members, who had been listening with grim expressions, then took a sheet of paper from my inventory.

“Sorry to interrupt, but could you take a look at this?”

“What is it?”

The paper I had taken out contained a drawing.

More precisely, it was a likeness of Honglan—or rather, the Southern Heaven Demon Empress—created from the testimony and memories of several people, including me.

I showed it to him just in case, but the old man’s reaction was lukewarm.

“That artist is remarkably skilled. But who is this woman?”

“Hmm, no. I was just wondering if you recognized her.”

“I’ve never seen the woman in that drawing. If a woman were this beautiful, I would have remembered her somehow. I may be old, but I’m still a man.”

It wasn’t the response I had been hoping for, but I wasn’t terribly disappointed.

Whatever her character might have been, the Southern Heaven Demon Empress possessed a striking appearance. Just as Ju Hwaran had hidden her face with the human-skin mask Song Ilseom made for her, she could have used any number of methods.

*It wouldn’t be strange at all for the Southern Heaven Demon Empress to have mastered an extraordinary disguise technique.*

I muttered inwardly, then asked the old man again,

“Where are the Central Plains people who claimed to have come from the Heavenly Demon Escort Bureau now?”

The Quest required us to make contact with an agent of the Hidden Shadow Pavilion, but if those people were still nearby, that changed things.

As if he had read my thoughts, the old man asked,

“Why? Are you thinking of chasing after them even now?”

“If we can.”

“Well, it’s an admirable thought, but it’ll be difficult. More than fifteen days have already passed.”

“Even so, if you know which direction they went or have a destination in mind, it should be worth trying.”

Every Fire Dragon Pavilion member present was highly skilled, myself included.

Even Hyuk Mujin, the least skilled among us, was a First Rate master who had endured countless real battles and brushes with death.

Yet despite my attitude, the old man merely let out a short laugh.

“It’s impossible.”

“Old man. I don’t think you understand yet…”

“I’m not the one who fails to understand. You are. Every one of those Central Plains people is dead.”

I paused for a moment, then asked,

“What?”

“I mean exactly what I said. There were countless tribal warriors among those who suffered that calamity. Do you think people like that would have stood by and let themselves be slaughtered? The Central Plains people all died too. We found their bodies after they were poisoned with deadly venom and collapsed before they could get very far.”

“…”

“No matter how skilled you are, there’s no way to chase them into the afterlife. And the same goes for…”

His voice trailed off. A moment later, the old man continued with a sigh.

“The Hidden Shadow Pavilion agent, who’s already old as dirt.”

Gulp. Gulp.

The old man drained the strong liquor to the last drop, then smiled at me.

“Good to meet you, Blazing Flame Divine Dragon Jin Taekyung.”

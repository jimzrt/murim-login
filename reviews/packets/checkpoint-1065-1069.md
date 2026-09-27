# Checkpoint Review — 1065–1069

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

# Chapters 1065–1069

## Plot

After the victory at Great Snow Mountain, Jin Taekyung’s allied force leaves Gansu for Qinghai, growing to nearly two thousand as Kongtong, Zhongnan, Black Dragon Demon Gate, and Embroidered Uniform Guard fighters join. Sama Pyo exposes traitors among Gansu’s faction leaders and leaves Taekyung his late father’s blank book. Guided by Great Sir, the force reaches northwestern Qinghai at least two days ahead of schedule.

The allies win their first battle in Qinghai, killing over a thousand enemies with about thirty wounded and no deaths. They discover a reanimated Kunlun Disciple resembling a victim of Wei Zhong’s Corpse Art. Taekyung and Jeong Hogun suspect Ma Sanbao may be with Dark Heaven, but this remains unconfirmed. Rotting, bloodred-eyed birds watch the force; Great Sir first detects Ma Sanbao’s covert surveillance.

Pursued by tireless undead, the exhausted force keeps retreating toward Qinghai Lake, estimated to be two days away at full effort. Taekyung orders the Embroidered Uniform Guard to remove its distinctive armor, and Jeong Hogun agrees after Taekyung invokes the Emperor’s order prioritizing the Marquis of Shangshan’s commands. Before they can carry out the order, a rumble stronger than any previous pursuer’s begins.

Meanwhile, Ma Sanbao reports to the Blood Lord that Jin’s force detected his surveillance. The Grand Mage suspects Hyeoncheon and the surviving Kongtong Disciples went to Great Sir, but does not know his identity.

## Continuity

- Jin’s allied force is retreating toward Qinghai Lake while repeatedly pursued by tireless undead. Reaching the lake is estimated to take two days at full effort; safety there depends on Qinghai’s forces having assembled and the enemy not committing fully to the pursuit.
- A powerful rumble has begun in the distance. Its cause and what is approaching remain unknown.
- Jeong Hogun agreed to remove the Embroidered Uniform Guard’s armor, but Jin told him to keep his helmet on when the rumble began; the order had not yet been carried out.
- Ma Sanbao serves the Blood Lord and covertly watched Jin’s force. Great Sir first detected the surveillance in Ningxia.
- The East Depot’s information network had shared its view with Dark Heaven through the Eastern Heaven Demon Lord.
- The allies found a reanimated Kunlun Disciple resembling a victim of Wei Zhong’s Corpse Art. Whether Ma Sanbao joined Dark Heaven or spread the Corpse Art remains unconfirmed.
- Great Sir’s identity and connection to Hyeoncheon and the Kongtong survivors remain unknown. Jin’s sword struck at a watching crow, but its fate was not shown.

## Translation Decisions

- Render 青海省 as “Qinghai Province” and 青海湖 as “Qinghai Lake.”
- Render 강시공 as “Corpse Art.”
- Use “Great Sir” for 대인, the address/name for the mysterious figure.

## Durable state

{
  "active_continuity": [
    "Jin’s allied force is retreating toward Qinghai Lake while repeatedly pursued by tireless undead; reaching the lake is estimated to take two days at full effort.",
    "A rumble stronger than any previous pursuer’s has begun in the distance as Jin’s group retreats.",
    "Jeong Hogun agreed to Jin’s order to remove the Embroidered Uniform Guard’s armor, but Jin told him to keep his helmet on when the new rumble began.",
    "Ma Sanbao serves the Blood Lord and was covertly watching Jin’s force; Great Sir first detected the surveillance in Ningxia.",
    "The East Depot’s network had shared its view with Dark Heaven through the Eastern Heaven Demon Lord.",
    "The Grand Mage suspects Hyeoncheon and the Kongtong survivors went to Great Sir."
  ],
  "continuity_sources": [
    1068,
    1069
  ],
  "open_questions": [
    "Who is Great Sir, and what is his connection to Hyeoncheon and the surviving Kongtong Disciples?",
    "Did Jin’s sword strike kill or otherwise affect the watching crow?",
    "Are Dark Heaven’s forces broadly composed of reanimated corpses, and has Ma Sanbao spread the Corpse Art to others?",
    "What caused the new rumble, and what is approaching the retreating group?",
    "What is the Lord of Heaven seeking through Jin, and when will he appear?"
  ],
  "safe_through": 1069,
  "temporary_decisions": [],
  "version": 1
}

## Reading copies

## Chapter artifact 1065

# Chapter 1065

Losing a battle meant the end.

That was especially true in a large-scale engagement, where tens of thousands of men clashed head-on.

The defeated survivors had only two possible fates:

Become prisoners, or run to the ends of the earth.

They had no say in which fate awaited them, and no way to refuse it.

But the victors were different.

So, three days ago, just after the bloody battle around the Great Snow Mountain ended in a crushing victory for our side, we were given a new choice.

Would we stay to protect Gansu Province after dealing with the aftermath of the battle?

Or would we move out to stop the Dark Heaven forces advancing somewhere else?

We chose the latter.

No—more accurately, everyone respected my wishes.

“I’ll be leaving now. There’s something I have to do.”

The snowfield was covered in flames and smoke that day.

The fire, consuming tens of thousands of corpses, burned as if it would never go out. And my sudden announcement must have felt unbearably cruel to those watching the scene, their tears falling without end.

Even though they’d been robbed of any chance to grieve in peace, they didn’t blame me.

Not a single person.

Only Perfected Being Hyeoncheon, the Sect Leader of the Kongtong Sect, stepped forward to ask a brief question.

“Where do you intend to go?”

I’d known my answer from the start.

The System had already pointed the way to our next destination with a Quest as clear as a compass.

“Qinghai. Qinghai.”

“Which means…”

“Yes. They’re coming.”

Even though I spoke with a certainty that made no sense, Perfected Being Hyeoncheon didn’t ask why.

He only nodded, his face heavy.

“The world will be stained with blood once more.”

“It will. Without a doubt.”

“If we win a great victory against them there as well, do you think we can bring this accursed war to an end?”

“We’ll be one step closer. And the step we take this time will be bigger and deeper than any before it.”

“Big enough to reach the Lord of Heaven?”

“I believe so.”

“Then the Kongtong Sect will stand with you.”

“……!”

“We won’t stop until we reach the end. If only for the sake of the souls who, by now, must be under the care of the Primordial Heavenly Venerable beyond those clouds.”

If Perfected Being Hyeoncheon had been leaking the same killing intent he’d shown while slaughtering the Dark Heaven followers who’d survived, I would have refused his offer.

But the eyes of the old Daoist, who had already lost so much, were clear. The same was true of the Kongtong Disciples, who had let out all their anger and grief.

“Good.”

And so, Perfected Being Hyeoncheon and about a hundred Kongtong Disciples joined us. But that was only the beginning.

“I, Hyuk Sopyung, an unworthy martial artist, humbly ask to answer for my sect’s sins.”

Hyuk Sopyung, the Zhongnan One Dragon.

Along with him, more than three hundred Zhongnan Sect Disciples who had barely survived the bloody battle set down their weapons and knelt.

The Roaring Fury Swordsman, Song Il, and the Taeeul Merciless Sword, Hwangbo Eom.

The faces of those Disciples who had learned of the sins committed by the two elders of their sect—now both dead—were full of shame and grief. Blood trickled between their clenched teeth.

If the Wind-and-Cloud Sword Lord, the Zhongnan Sect Leader, hadn’t been unconscious with severe injuries, he would have knelt with his Disciples and asked to answer for their sins, too.

Perfected Being Hyeoncheon watched the Zhongnan Disciples in silence for a long while, then spoke.

“A father’s sins do not belong to his children. A master’s sins do not belong to his Disciples. So why do Zhongnan’s Disciples ask me to punish them?”

“……!”

“Still, if you wish to accept your punishment, so be it. Follow Great Hero Jin here and walk a straight and righteous path. That will be the new way of the Zhongnan Sect.”

At the wise, kind old Daoist’s words, Hyuk Sopyung and the Zhongnan Disciples bowed deeply, then saluted me with the utmost respect.

“We wish to walk the righteous path without the slightest deviation. We ask to join you, Great Hero Jin.”

This was the first time I’d come face-to-face with Hyuk Sopyung since the incident at the Yongbong Escort Bureau.

He had once been the Zhongnan Sect’s most promising young prodigy, one of the Ten Dragons and Phoenixes. The gap between us had grown even wider than before.

So, while I spent several days with the Zhongnan Sect in Gansu, I could only pass him at a distance.

Maybe that was why I only then realized how much more serious and profound his aura and gaze had become compared with the last time I’d seen him.

“I gladly accept your offer.”

I accepted the Zhongnan Sect’s offer with a rare show of courtesy. As I watched our numbers swell to more than five hundred with the two sects’ arrival, someone came over.

“This still won’t be enough. Don’t you think?”

“Who knows? It’s a lot better than padding the numbers with any old riffraff.”

“Why do my ears itch? Must be my imagination.”

“Maybe not.”

The new Sect Leader of the Black Dragon Demon Gate chuckled at my deliberate air of innocence, then pointed to his new followers, lined up in perfect ranks.

“Five hundred. We were short on time, but I thoroughly vetted the volunteers. They may not measure up to the Nine Sects and One Gang’s Disciples, but I can guarantee their loyalty and fighting spirit.”

“So you’re putting them under my command?”

“No. I’d be grateful if you’d let them come with you.”

“What?”

“I, Sama Pyo, Sect Leader of the Black Dragon Demon Gate, and five hundred men ask to join the Fire Dragon Pavilion Master. Please let us fight for the world and make up, even a little, for the mistakes of our past.”

“……!”

For a moment, I was at a loss for words.

If a big guy hadn’t then shouted while dangling a small old man from his neck, I might not have been able to hold back the emotion welling up inside me.

“Taishan’s going! Taishan’s going, too! Taishan will go with the Pavilion Master to the end!”

“Goddamn it! Stop bouncing around so hard! Please!”

Everyone burst out laughing at once, as if they’d planned it.

Me, Sama Pyo, the Fire Dragon Pavilion members, and the survivors of the Nine Sects and One Gang.

Even Jeong Hogun, Thousand Captain of the Embroidered Uniform Guard, whose expression had always been utterly dry, whether he was happy or sad.

“What an amusing bunch you martial artists are.”

“Really? Since we’re on the subject, want to hear something even more amusing?”

“Something even more amusing?”

“Yeah. It’s about a certain Thousand Captain of the Embroidered Uniform Guard who kept talking back to a Marquis like he was his equal and is now on the verge of being forcibly discharged. The funny thing is, he has the same surname as you. What a coincidence, huh?”

“……Is that the way you’re going to play it?”

“Then do your best. So I don’t have to.”

As if he couldn’t win against me, Jeong Hogun shook his head, then stood as straight as an iron tower and saluted me.

“Then, please give your orders.”

“Qinghai. We’re going to Qinghai. At full speed.”

“I, Jeong Hogun, Thousand Captain of the Embroidered Uniform Guard, accept the solemn order of the Most Honorable Marquis of Shangshan.”

And so, two days ago, the final piece of our force—the Embroidered Uniform Guard—joined us. Our numbers had grown to nearly two thousand. After a brief rest, we headed straight for Qinghai Province.

A few people did argue that Dark Heaven might target Gansu again, but the Bow Saint ended all their concerns with a brief remark.

“The North is on the move.”

Of course, he didn’t mean northern Gansu.

He meant the North of the entire world, divided by the Great Wall—and the two powers that ruled that vast land.

The fierce tiger of Hebei, the Hebei Peng Family.

And the Azure Dragon of Shanxi Province, the Jin Family of Taiyuan, who had now claimed even the skies of the green grasslands.

“Each arrow may fly at a different speed, but as long as it doesn’t stray from its course, it will reach its target in the end.”

The Bow Saint and the Embroidered Uniform Guard were the first arrows shot, for example.

It was a metaphor worthy of the Bow Saint. After that, no one dared argue.

Not merely because the Bow Saint had said it.

Everyone knew that with the Azure Dragon and the fierce tiger of the North spreading their wings and baring their claws, Gansu’s safety was more or less guaranteed.

And the brief purge just before we left Gansu was enough to wipe out any possible future threat.

“Anything you want to say before you die? Spare me the excuses. I’ll hear your last words.”

“I—I never colluded with Dark Heaven. There must have been some misunderstanding!”

“Young Sect Leader—no, Sect Leader! Why are you doing this? You know your late father and I were practically sworn brothers!”

“Yeah, I know. Close enough to betray us together. You were so close that my father wrote it all down in detail… Did you know that?”

“……!”

The critical meeting that would decide the future of Gansu’s Murim had turned into a trial, with traitors being called to account. The room froze in an instant.

Wide eyes. Trembling lips.

Sama Pyo gave a small sigh at the sight of them and pulled a battered old book from inside his robe, setting it on the table.

“Looks like you really didn’t know. You might at least have suspected.”

Even I found it surprising that the meticulous Black Night King, Sima Gong, had left such clear evidence behind. So imagine how those men must have felt, having known him in life for decades.

But Sama Pyo went on without a second thought.

His voice held a trace of bitterness toward his father, and his eyes looked at them as though they were insects.

“So, any last words?”

That was the finishing blow.

“You—you little brat, with the blood barely dry on your head! You dare kill me, your uncle in all but name?!”

“Heh. Heh heh. So this is how it ends.”

A cornered rat had only two choices.

Charge with its adorable little front teeth as its only weapon—or give up on everything and accept its fate.

And the fools who chose the first option were met by…

“Story’s over, Taishan.”

“Yaaawn. Taishan almost fell asleep listening.”

The designated hitter for the Gansu Province Black Dragon Dragons, boasting a career batting average of .999: Tiger Giant Child Taishan.

*Wham! Wham!*

I’d been there in case anything happened, but there was no need for me to step in.

Taishan’s two-section staff was enthusiastically spewing fire—no, blood.

One of the Black Dragon Demon Gate’s senior members had shouted that Sama Pyo was a little brat with the blood barely dry on his head, then charged at him. His head was gone before he could spill any blood into it. Several Sect Leaders and Family Heads tried to flee with all their might, but they were surrounded the moment they left the pavilion.

By the warriors of the Black Dragon Demon Gate, who had pledged their loyalty to their new lord.

And by their own followers and Disciples.

“G-Gangpyeong! How could you do this to me?!”

“And how could you do this, Sect Leader?”

“Guard the way! Quickly! No, wait. I’m the Sect Leader! Stop those men right—”

“Shut your filthy mouth.”

“What?”

“Because of you, my Master, my Junior Sister, and my Martial Nephew died! That makes you guilty of deceiving your master and betraying your ancestors. Disciples of the Gorang Sword Sect, execute the Sect Leader on the spot, as the sect rules demand!”

“What are the members of the Lanzhou Hyuk Family doing?!”

“Please don’t hold it against us, Family Head. You were the one who betrayed us first.”

“Y-you bastards…!”

*Slice! Thud-thud-thud!*

Under the storm of spears and blades from every direction, around a dozen Sect Leaders and Family Heads died with their eyes wide open, unable even to leave proper last words.

It was a pitiful end for men who had led Gansu’s Murim, each the head of a faction with a substantial number of followers.

But the young Sect Leader of the Black Dragon Demon Gate didn’t so much as blink as he killed or captured twenty renowned masters in all.

He watched the whole scene with calm, cool eyes, then idly touched his teacup, which had gone cold, and suddenly spoke.

“Should I have them bring us fresh tea?”

“No. It tastes bad. We don’t have time, either. Besides, that scatterbrained guy will be joining us soon, so it’ll only upset my stomach.”

“Benefactor, does he really know the fastest route to Qinghai Province?”

“More precisely, Ma Junggeol told me. I don’t know what the guy used to do in his youth, but he knows geography inside out.”

“I see. Then, since we’ve finished our business here, I’ll come with the Pavilion Master.”

Sama Pyo nodded and stood.

The table had been filled with more than twenty faces only fifteen minutes earlier. Now it was empty, with nothing but toppled teacups and a battered old book left on it.

“Aren’t you taking it?”

“It’s useless to me now.”

With that, Sama Pyo left. I hesitated for a moment, then picked up the book.

It might have outlived its purpose and been thrown away, but this battered old book was still one of the traces left behind by his dead father.

And the moment I turned its first page without thinking, absently tasting the bitterness in my mouth, I understood the real meaning of what Sama Pyo had said.

“…Huh.”

I let out a laugh and set the book down.

No.

It was a bundle of yellowed pages, not a single character written on them, clearly left to gather dust somewhere for years without ever serving its purpose.

“Guess blood really does tell. In a good way.”

Muttering under my breath, I walked on, breathing in the stench of blood flowing from the traitors’ bodies.

Two days passed. Then, as we traveled across mountain slopes so rough they made me want to curse, another three days went by.

“Hey, young man. What’s your name?”

“Jin Taekyung. You know this is the twenty-fourth time you’ve asked, right?”

“Ah, yes. Jang Sam.”

“Why the hell would Jin Taekyung be Jang Sam… Hah. Never mind. What is it?”

“Well, it’s not all that important, really.”

“Then tell me anyway. While I’m still using polite speech with you.”

“It’s nothing much. I was just wondering where we are.”

“Pardon? What?”

“I asked where we are.”

“Son of a bitch.”

A powerful urge to kill that lunatic guide, who kept spouting insane nonsense with a straight face, took hold of me.

It was a fierce, deep-seated urge, strong enough to snap my last thread of self-control.

*Step.*

But just as I approached the Great Sir, unable to hold back any longer and ready to let our bodies do the talking—

*Ding!*

The clear chime that momentarily glued my fraying self-control back together rang in my ears.

> **System**
>
> Entered **Qinghai Province**.
## Chapter artifact 1066

# Chapter 1066

*Ding!*

> **System**
>
> Entered **Qinghai Province**.

At the timely chime of the System notification, I stopped in my tracks. I’d been clenching my fist and walking toward the Great Sir.

“You made the right call. There’s nothing to gain by hitting someone who’s already in rough shape… Are you listening to me?”

“Shh.”

Hyuk Mujin had let out a sigh of relief, thinking I’d changed my mind. I gestured for him to be quiet and looked around.

Dense forest lay under the cover of darkness, and insects chirped here and there.

The landscape around us hadn’t changed in the slightest, but there was no doubt that all of us—including me—had just crossed an invisible boundary.

The System was always accurate. It never lied.

And the Great Sir, who had somehow managed to fulfill the task assigned to him, wore the same baffled expression as the question marks that had floated above his head. He asked me,

“What is it, Jang Sam?”

“…I’m Jin Taekyung, not Jang Sam.”

To be honest, I’d doubted him right up to the end.

Following someone who couldn’t even remember his own name was, by anyone’s standards, a terrible idea.

What’s more, he kept changing direction along the way. Even people like Sama Pyo, who’d been born and raised in Gansu Province, had questioned him several times.

Still.

*The results speak for themselves.*

We’d cut at least two days off our journey compared to what I’d expected. And though we’d traveled through rough mountain country, we’d gained time to rest and recover our Stamina.

*The question is, how does this guy know a route like this?*

The obvious question surfaced again. But when I saw the Great Sir yawn so wide his jaw might split, my head shook before I knew it.

What good would it do to keep wondering?

He’d been out of his mind for ages, and now the System had officially certified him a Madman. There was no room left for doubt.

What mattered was that the Great Sir was, at the very least, on our side—and thanks to his help, we’d all reached Qinghai Province.

More precisely, the area near Qinghai Province’s northwest border.

*And this place is…*

Right.

Enemy territory, now under Dark Heaven’s control and filled with countless dangers.



* * *



Three thousand men.

Not a small number by any means.

In the modern world, a force of that many Hunters would be considered a major Guild. Even the other Nine Sects and One Gang, with the exception of the Beggars’ Sect, would have to call in even their lay Disciples outside the main sect to reach those numbers.

But everything was relative.

Considering that the Dark Heaven forces invading Qinghai were a great army comparable to the Hundred Thousand Demonic Disciples of old, three thousand men were no more than fireflies before the sun.

*This is urgent, but if we rush straight in with everyone this exhausted, we’ll be the ones getting slaughtered.*

So I proposed a day of rest in the mountain range where we’d paused our march. No one objected.

Not even Perfected Being Hyeoncheon, who could be considered my toughest opponent.

If anything, he went out of his way to show me more respect than necessary, which only left me flustered.

“A truly sound decision. Very well. What are your orders after we rest?”

“Sorry? My orders?”

“Is something wrong? I don’t mind if you call them commands instead.”

“…Just curse me out instead. Why are you doing this to me?”

Was this how a family heir felt when his grandfather’s generation bowed deeply to him during a holiday gathering?

At my thoroughly disconcerted reaction, Perfected Being Hyeoncheon gave a quiet laugh and said something I hadn’t expected.

“Why not take a look around you now and then?”

“What do you mean…?”

“Look at how many people are around you, and how they look at you. That is where you stand now.”

“……!”

Only then did I finally understand.

All those eyes fixed on me in that moment.

The deep admiration and goodwill in their gazes were so vivid I could almost reach out and touch them. Their faint smiles held a gratitude they couldn’t hide.

Then Perfected Being Hyeoncheon’s warm voice drifted into my ears.

“Whether it’s a request, an order, or a command, it makes no difference. We all owe you a great debt.”

“A debt…”

“Gratitude and grudges must always be repaid. That is the way of Murim. I forgave my grudge, and now I intend to repay the kindness. I imagine they feel the same.”

I thought for a moment about how they must feel.

They’d lost comrades they’d shared years of hardship with, family, Senior and Junior Brothers. Before they’d even begun to recover from the fear and sorrow they’d felt on the battlefield, they’d chosen of their own accord to follow me into another deadly place.

They had come to repay a debt, but they were also driven by a desire for revenge that would bring darkness to this land.

And that desire was, in itself, a light that would illuminate the darkness.

“Ah.”

It was a strange feeling, one I could never get used to.

I didn’t even know what to say.

But the old Daoist, whose wisdom matched his long life, didn’t demand a reply. He simply patted my shoulder a few times and walked away.

The attention of those who remained was fixed on me.

The Disciples of the Kongtong and Zhongnan Sects.

The martial artists of the Embroidered Uniform Guard and the Black Dragon Demon Gate.

Even Jeok Cheongang and Bow Saint, who stood among the Fire Dragon Pavilion members, silently nodded at me.

As though they’d follow me to the end, even if I were headed straight for hell.

“I… No, I…”

Under the gaze of all three thousand men, I slowly parted my lips.

And at the very moment the suffocating silence broke, a thought suddenly struck me.

*How can it possibly be this quiet?*

Only then did I realize that the loud chirping of insects hidden throughout the thick forest had stopped at some point.

The birds that had perched on the high branches were gone, too.

“……!”

A chill ran down my spine.

*Rumble. Rumble.*

A faint tremor finally reached us from far away. With it came the eerie cry of something unknown, carried to my ears on the desolate wind.

*Grrrk.*

“…Shit.”

The curse slipped out on reflex.

I tightened my grip on the shaft of White Flame.

I stared into the darkness at the enemies who had come out early to greet their unexpected visitors, then gave my first command in Qinghai.

“Prepare for battle.”

*Shing! Shing! Shing!*

Countless waves of steel rose all at once, their cold gleam lighting up the darkness.

And the enemies who had been approaching under its cover.

“……A-ah…”

At the low groan that slipped from someone’s lips, the enemy crawling up the ridge at the very front tilted his head.

*Plop. Plop.*

The drops falling from the head that had already lost nearly half its mass were as pale as his skin.

Brain matter.



* * *



From time immemorial, long before anything had been committed to the written record, people had called a vast mountain range at the far western edge of the world:

“The land closest to the heavens, the highest peaks touching the clouds…”

The Blood Lord murmured as if to himself, then looked around and nodded.

The mountain range stretched on in endless, overlapping ridges, its many peaks rising here and there. It was majestic and beautiful enough to make anyone gasp.

“Quite a sight. I can see why people of the Central Plains consider this place sacred. And why those worthless Daoists of the Kunlun Sect fought so stubbornly to protect it. Don’t you agree?”

At the Blood Lord’s sudden question, the Grand Mage, seated on a large rock and making strange gestures with her hands, answered,

“Seems like you’re quite taken with the scenery.”

“Well, whatever else you can say about Tianshan, it’s bleak.”

“Then why not formally apply to join the Kunlun Sect? Who knows? You might become its Sect Leader someday.”

Her words were openly mocking, but the Blood Lord showed little reaction to her intent.

He only stared at her with a strange, inscrutable look, then shrugged.

“That offer doesn’t tempt me much. Got anything better?”

The Blood Lord’s casual retort made the Grand Mage furrow her brow before she knew it.

“What’s gotten into you?”

“What do you mean?”

“You weren’t like this before.”

“Wasn’t I?”

His smooth reply was nothing like the man in her last memory of him.

As she watched the Blood Lord, a strong sense of displeasure gradually welled up inside her.

*Putting on airs, like he’s got all the time in the world. And he’s a deranged monster.*

The Blood-Sword Demon Lord had been a bloodthirsty killer, but the Blood Lord was even more unbearable.

Stupid, vicious, and without the slightest sense of shame.

Those three failings alone were more than enough reason to dislike him, but there was something else more important.

*Why does that person keep someone like this so close?*

She couldn’t understand it.

The Blood Lord she’d known wasn’t particularly skilled in martial arts, nor was he a deep thinker—unlike the four Demon Lords and the Demon Empress who had died before him.

But there was no denying that, unlike the Blood-Sword Demon Lord, a mere piece on the board, the Blood Lord had his master’s trust. And the fact that he stood on equal footing with her only made her more uncomfortable.

There was also the person sitting just a few *jang* away, who gave off a horrific stench without pause.

*Jingle. Jangle.*

The Grand Mage frowned as she looked at the man in black, sitting cross-legged and muttering something incessantly.

The foul odor drifting over on the wind was bad enough, but the dull, grating jingling of his bells every time he moved was even worse. The more she heard it, the more it grated on her.

As if an awl were scraping at her ears and stirring up her mind.

“Who’s that?”

At the Grand Mage’s question, the Blood Lord answered readily.

“My subordinate.”

“Did you have someone like him working for you? There’s something about him that feels oddly familiar, and unpleasant.”

“Probably because he’s a sorcerer.”

“What?”

“Oh, don’t get the wrong idea. He’s a different kind of sorcerer from a certain sharp-tongued bitch. He only joined my ranks recently, actually.”

For a moment, the Grand Mage’s eyes widened as she guessed what he meant.

“Then…”

“That’s right. Until a few months ago, he served another Demon Lord. Well, more precisely…”

The Blood Lord curled his lips into a smile and added,

“I should say he was his Disciple, rather than his subordinate.”

At that very moment—

*Clatter.*

Along with another dull bell sound, deeper and louder than before, the man in black raised his head.

Pale skin. Eyes tinged blue.

And a dry voice, without a hint of emotion.

“I found it.”

Not long ago.

At Ma Sanbao’s report—once the East Depot’s Brush-Holding Eunuch, and a man who’d held the imperial court in his grasp—the Blood Lord smiled with satisfaction.

“That’s very good news.”
## Chapter artifact 1067

# Chapter 1067

Half a shichen.

That was how long the first battle in Qinghai had taken—from its beginning to its end.

“So this is where you were.”

The forest now reeked of blood.

I sat on the body of an enemy I didn’t recognize, catching my breath. Then I turned toward the voice.

*Squish.*

Footsteps squelched through blood and mud as someone strode closer.

A familiar face came into view, clad in armor stained red and stripped of its original golden luster.

“Shouldn’t you say, ‘So this is where you were, sir’?”

Jeong Hogun, the Embroidered Uniform Guard Thousand Captain, let out a small sigh before answering.

“So this is where you were, sir. Happy now?”

“Not even close. You suddenly dropped half your tongue for the second part.”

“...Cut it out. We’ve both been through enough.”

“I was about to. How are our casualties?”

“Calling them casualties feels like an insult. We have only around thirty wounded, and not a single one of them died.”

Jeong Hogun glanced around at the heaps of bodies and added,

“A miraculous result, considering we wiped out more than a thousand enemies.”

Three thousand against one thousand.

Even though we’d started with the advantage in numbers, winning without a single fatality was an absurdly decisive victory.

Even more so when you considered we’d achieved all this in the space of half a shichen.

But my answer to Jeong Hogun was matter-of-fact.

“It wasn’t a miracle. It was only natural.”

“I can’t argue with that. The difference in strength was simply overwhelming.”

Our troops had all been chosen for their skill, each faction bringing its own elite. But more than anything, the Supreme Peak masters had made an enormous difference.

Bow Saint. Jeok Cheongang. Perfected Being Hyeoncheon. Me.

And last of all, even the Great Sir—though he hadn’t been much help.

With a difference in strength like that, losing would have been harder than winning.

There was only one problem…

“How’s everyone doing?”

“What do they look like?”

At Jeong Hogun’s immediate question in return, I clicked my tongue.

Honestly, there was no need to ask.

I could look around and see nothing but rigid faces.

Despite our overwhelming victory and almost nonexistent losses, every one of our allies looked deathly pale. A faint fear lingered in their eyes.

As if they’d witnessed something horrible they were never meant to see.

And that was exactly what had happened.

The unknown enemy writhing beneath my ass right now was undeniably a monster.

*Grrk. Grrrk.*

A hoarse cry seeped through its torn throat.

Only then did Jeong Hogun notice the monster and furrow his brow.

“It’s still alive?”

“Maybe. If you can call this being alive.”

I gazed down at the cursed monster.

Its limbs had been brutally severed, and its body was rotting.

It had clearly died days ago, yet it hadn’t crossed the Sanzu River[^1] and passed on to the next world. It remained here, writhing stubbornly.

It couldn’t even remember who it had been in life.

But two characters embroidered with thread on its torn and ragged robe still remembered their owner.

“Kunlun…”

At Jeong Hogun’s low murmur, I quietly nodded.

That was right.

This monster was none other than a Disciple of the Kunlun Sect.

No—it *had been* one.

“I heard there were casualties during the retreat from Kunlun Mountain. I suppose this was one of them.”

“Probably.”

“Did you know him?”

I shook my head at Jeong Hogun’s cautious question.

“No. Not at all.”

I’d crossed paths with Hak Woo—the Kunlun Cloud Dragon, the Kunlun Sect’s greatest young prodigy and a member of the Ten Dragons and Phoenixes—during the Star-Array Grand Banquet. But I didn’t recognize the face of this Daoist, now turned into a monster.

Still, I had a rough idea who might have made him this way.

“What do you think? Look familiar?”

“Yes.”

Jeong Hogun’s eyes darkened.

“Cang Gong. This is astonishingly similar to the dark arts he used.”

Wei Zhong.

The East Depot’s Seal-Holding Eunuch, known as Cang Gong, had two deep secrets.

The first was that he was the Eastern Heaven Demon Lord, one of the Lord of Heaven’s most loyal servants.

The second was that he was a descendant of the Maoshan Sect, which had been wiped out by the imperial family long ago.

But even after Wei Zhong met his end at my hands, the Maoshan Sect’s legacy hadn’t been completely extinguished.

“Ma Sanbao. It has to be him.”

The Disciple who’d inherited everything from Wei Zhong.

Like his Master, he’d worn a mask while working in secret as an East Depot eunuch. His body had never been found, and that could only mean one thing.

“So that’s where he went. He must’ve clung to life and joined Dark Heaven after all.”

Of course, it might not be Ma Sanbao.

According to Jeok Cheongang, the Corpse Art Wei Zhong had shown him had far surpassed its former limits. That meant it had been improved with the Lord of Heaven’s help.

But even if Dark Heaven had trained others to use the Corpse Art, none could match Ma Sanbao, who’d learned directly from Wei Zhong himself.

Besides…

*Qinghai is an important battlefield for them and for us. They’ll be committing more troops than ever.*

Dark Heaven’s army of a hundred thousand had already swallowed half of Qinghai Province.

I couldn’t begin to guess why the Lord of Heaven had intended for them to lose in Gansu, but this time, he’d surely commit everything he had.

Even Dark Heaven, with strength that far surpassed the Demonic Cult of the past, wouldn’t throw a hundred thousand troops away as mere bait.

*Ma Sanbao is another piece they need to win. They wouldn’t leave him out.*

A thought flashed through my mind, and I swallowed the groan that threatened to escape.

If all a hundred thousand enemies had been turned into jiangshi, it would be an unstoppable disaster.

And on top of that…

*The Lord of Heaven could show up on the battlefield himself.*

I’d never even faced him properly, but the thought of those two words made my heart sink.

How could I forget?

The Lord of Heaven had appeared only once, and I remembered every moment of it clearly.



*“Interesting. Very interesting.”*



That day, the one who’d watched Jeok Cheongang and me with a smile hadn’t been the Western Heaven Demon Lord.

He’d been a demon borrowing a human body. The darkness of the abyss itself. An absolute being who seemed beyond the reach of anyone.



*“Until next time.”*



But after that day, the Lord of Heaven never appeared before me again.

He simply crouched in the deepest darkness, watching everything.

Even as his loyal servants, including the Western Heaven Demon Lord, met their ends one by one. Even as the plans he’d spent considerable effort and years preparing were systematically dismantled.

The Lord of Heaven never appeared.

But he was watching everything all the same.

Waiting for a moment that no one in the world could guess—the moment only he knew.

And deep in my heart, I sensed that the moment he wanted wasn’t far off.

I also sensed that it was connected to me, deeply and unmistakably.

*What is he trying to get from me?*

The moment I repeated that unanswerable question in my head—

*Whoosh! Thwack!*

A sharp whistle cut through the air. Snapping out of my thoughts, I heard a shout from not far away.

“Oh, I got it! I got it!”

“Wow! Sir! That was amazing! Taishan is truly impressed!”

“*Ahem.* Did you see that? When I put my mind to it, something like this is easy.”

Curious, I looked over. The Great Sir was proudly holding a bird in his hands.

Its head was smashed to a pulp. It looked like it had died from being hit by a stone.

And Taishan was staring at the Great Sir—or, more precisely, at the bird—with drool in his mouth.

“Tasty—no, impressive! Taishan will start a fire, so let’s hurry and cook it!”

Starting a campfire in the middle of enemy territory was bullshit that set everyone’s blood boiling, mine included. But one lunatic didn’t seem to mind.

“Young friend, you do know how to show proper courtesy. As a reward for your hard work, I’ll let you have some of my meat. Which part do you prefer?”

“The legs! Definitely the legs!”

“You know your way around a chicken. Fine, I’ll give you one.”

“Both! All of them!”

“...Don’t push your luck.”

The Great Sir suddenly sobered up. Taishan drooped his head in disappointment, and that was when—

“You’re all acting like a bunch of damn fools. It reeks like something crawled out of who knows where, and you want to eat it? Like hell.”

At Namho’s words, delivered from his comfortable perch on Taishan’s shoulder, a thought suddenly struck me.

*Wait. Could it be?*

The suspicion became certainty the moment Jeong Hogun examined the bird.

“It’s rotting. The bone’s showing.”

“Which means…”

“Looks like the monsters aren’t only on the ground.”

It had been strange enough that any birds were still around after a group of strangers invaded their territory.

When the others finally realized what was happening and turned to look, the Great Sir blinked in confusion.

“Is something wrong? That fellow was staring right at me from a branch, so…”

“It was staring at you?”

The Great Sir nodded.

“Definitely. Its eyes were bloodred, too. It creeped me out, so I just went ahead and threw a stone at it.”

“...A Familiar?”

“Hm? What was that?”

“Nothing. Just talking to myself.”

I waved the Great Sir off and stared silently into the air.

The light of dawn was beginning to spread from the east. Between the lofty branches, I could make out shapes here and there.

Monsters that had hidden in the dark—and been brought back to life by its power.

*They’ve been watching us this whole time.*

I felt my mind turn cold as I slowly rose to my feet.

Then I spoke to the Great Sir, who still looked confused.

“If you see any more birds like that, kill every last one.”

“Every one?”

“Yes. Every one.”

“I don’t know about that. Even so, isn’t life precious?”

I thought about how to answer for a moment, then said,

“They’re dangerous birds.”

“Oh. Then I’ll kill them.”

“Please do.”

I patted the Great Sir’s shoulder and started to leave, but then remembered something and stopped.

Quietly murmuring, I reached out.

“Infinite Life Buddha.”

*Stab.*

The monster had stopped moving completely. I left it—and the Kunlun Sect Disciple—behind and walked away.

Every second counted now.

Eyes were already watching us, and pursuers would soon be on our heels.

[^1]: The Sanzu River is a Buddhist river associated with the boundary between life and death.
## Chapter artifact 1068

# Chapter 1068

If anyone asked me how to shake off enemy pursuers, I’d answer without a moment’s hesitation.

There were only two things that mattered:

Speed and stamina.

But knowing what to do and doing it were two different things.

Even though every one of us knew that—including me—the wall of reality standing in our way was high and solid.

Unlike our three thousand allies, who hadn’t had a proper rest, the pursuers closing in by the moment were monsters who didn’t even feel fatigue.

“Northwest! About two thousand feet out!”

We’d been coming down the mountain without a break for barely two hours when—

“There! The bastards are here!”

The people who spotted the distant cloud of dust cried out. I immediately turned and sized up the hazy yellow cloud.

*Three hundred at least. Maybe five hundred.*

The F-rank Hunter who used to scrape by in narrow, pitch-dark Gates was gone.

No—even if some part of that old me still remained, I’d changed in many ways.

I’d learned how to fight multiple enemies and how to make snap decisions in all kinds of situations.

“Old Master.”

We’d reached the point where we understood each other from a glance.

Jeok Cheongang read the meaning in my brief call and immediately poured internal energy into his voice.

“You slowpokes! What are you waiting for? Run like your feet are on fire!”

That wasn’t just a scolding from a cranky old man.

Jeok Cheongang’s mighty Azure Dragon’s Roar shattered the fear lodged in our allies’ hearts and drove their hesitant feet forward, if only for a moment.

And the great martial artist who’d come to be known as the Bow Saint after countless battles knew her abilities and her role precisely.

“Go. I’ll send it at the right time.”

I nodded, kicked off the ground, and charged toward the dust cloud.

*Whoosh!*

The wind split.

The ground-covering dust billowed up behind my advancing feet, forming another cloud—one larger and denser than the cloud surrounding the several hundred enemies.

*I see them.*

Beyond the swirling sand and dust, the monsters who were neither dead nor alive came into sharp focus.

I tilted up the spear clenched in my hands just as a dazzling streak of light reached the enemy a step ahead of me.

*Boom!*

An arrow of Force exploded.

Shot from the Bow Saint’s fingertips, it swallowed up dozens of monsters charging at the front and vaporized them in an instant.

I plunged into the gap it left behind, not about to waste that perfect opening.

*Whoosh!*

The hair on my arms stood on end at the faint, spine-chilling whistle.

Breath, speed, strength.

As if to prove my skill advanced with every passing day, everything aligned in an attack without a hair’s breadth of error. It only grazed the enemies—but that was enough.

*Slice! Splatter!*

One cutting sound, but dozens of deaths within it.

A single diagonal sweep split and burst their rotting bodies, spilling blood.

Along with a clear chime, wholly at odds with the horrific sight.

*Ding. Ding. Ding-ding-ding!*



> **System**
>
> You have slain a Lv. 56 Corrupted Lower-Rank Fanatic!
>
> You have slain a Lv. 75 Corrupted Mid-Rank Fanatic!
>
> You have slain a Lv. 52 Corrupted Martial Artist!
>
> …
>
> …
>
> …
>
> EXP and Fame are calculated based on the level difference between you and your opponents!
>
> You have gained a small amount of EXP!
>
> You have gained a small amount of Fame!



I swung my spear as if entranced, listening to the System notifications ringing one over another.

Monsters and enemies surrounded me on all sides.

Each time my spear traced an arc, a dozen or even dozens of them crumpled like rotten logs, never to move again.

Freed from the chains that had bound them to this world, they returned to the order of things as it was meant to be.

*Ding.*

At the last chime, I confirmed that nothing else was moving and lifted my head.

Beneath a cloud that half-obscured the sun, a black-winged crow drifted through the air.

Its eyes glowed bloodred.

“Come down. Let’s talk.”

Naturally, I got no answer. I picked up a sword from the one submerged in a pool of foul-smelling blood and added,

“If you don’t like that, come yourself.”

*Whoosh!*

The sword shot upward, tearing through the air. In an instant, its blade covered the crow’s red eyes.

*Thrust!*



* * *



“Hmm.”

The man opened his eyes with a low groan and rubbed the space between them.

The pain that had come with the flash of light at the last moment still lingered in his mind, as if an awl were burrowing into his head.

*What a monster. He’s gotten even stronger.*

Ma Sanbao couldn’t help but be surprised.

Jin Taekyung’s martial skill, which he’d watched through another being’s senses, had advanced even further than when Ma had seen him at the imperial palace.

*Was that even possible? In less than three months?*

Ma Sanbao asked himself the question, then shook his head.

It was a stupid question.

The time to wonder whether it was possible had passed long ago.

What mattered was that Jin Taekyung had made it real—and that was precisely what made that young man, not even thirty yet, so exceptional.

Ma Sanbao already knew something else, too.

Unlike Jin Taekyung, his own role was already set. He would never be the star of this stage.

And the most important task currently before him was nothing more than keeping a thorough watch and reporting back.

“My Lord.”

Ma Sanbao went to find the superior he’d only recently begun serving and reported everything in detail. The Blood Lord listened, then furrowed his brow.

“Wait. They even found out you were watching them?”

“Yes. I’m ashamed to say that’s what happened—”

*Boom!*

A palm strike flew at him before he could finish.

Even an ordinary Peak master would have died on the spot if struck by that blow. Ma Sanbao was swept away by the force, yet despite the tremendous impact, he immediately prostrated himself.

“Huh. Look at how sturdy this body of yours is.”

“Please kill me.”

“Don’t rush me. I was just considering whether to beat you to death right here.”

“...My Lord.”

“What, are you finally scared? I suppose you have reason to be. Your Master died the same way, after all.”

Ma Sanbao lowered himself even further.

Unlike his Master, the Eastern Heaven Demon Lord, Ma hadn’t achieved Great Completion in the White Illusion Jiangshi Art. So his fear of death could only be greater.

“Please show mercy…”

“Shut your mouth. If you want to live even fifteen minutes longer.”

The Blood Lord glared down at Ma Sanbao with irritation, but that was the extent of the punishment he could give.

Ma Sanbao was a useful expendable in many ways, and the Blood Lord had never intended to kill one of the few subordinates worth keeping.

Besides, the reason the Blood Lord had threatened Ma so harshly was that he wanted to show off his authority and control in front of someone he disliked.

Of course, that someone paid no attention to the Blood Lord’s display and remained focused on another matter.

“They found out? This soon?”

The Blood Lord answered the Grand Mage’s question, which sounded almost like she’d asked herself.

“No need to make a fuss. It’s sooner than expected, but not all that surprising.”

“Looking at the result, sure. That’s about as far as your thinking goes.”

“What?”

“The Bow Saint, the Fire King, Jin Taekyung. And while he’s not on their level, even that old Daoist from the Kongtong Sect. They could’ve noticed. But that’s not what I want to know.”

The Grand Mage fixed the Blood Lord with a mocking look, then turned to Ma Sanbao.

“Come now. Don’t worry about your foolish superior. Tell me honestly: who was the first to notice your covert surveillance?”

“That was…”

“Once you’ve said something, you can’t take it back. I find it hard to believe the Eastern Heaven Demon Lord would take in a Disciple foolish enough to lie under these circumstances.”

Ma Sanbao hesitated for a moment. But when he met the Grand Mage’s deeply penetrating gaze, he realized—

She already saw through everything.

She had guessed what he’d been too afraid to say, worried that his violent superior would scold him even more.

“It was someone I’d encountered only vaguely, through brief rumors and bits of information, more than a decade ago.”

At last Ma Sanbao answered cautiously. The Blood Lord let killing intent seep from him, while the Grand Mage wore a faint smile, as if she’d expected as much.

“I thought so. The East Depot wouldn’t be what it is otherwise.”

The world belonged within the bounds of the Great Nation, and the Great Nation’s imperial family had built a watchtower to observe what lay inside and beyond those bounds.

The East Depot—the imperial watchtower.

And that peerless watchtower, overlooking the world, shared its sights with Dark Heaven through the Eastern Heaven Demon Lord.

“Though his influence has waned in his conflict with the current Emperor, information still flowed in from all across the realm through the eyes and ears he’d planted everywhere.”

“And among them was the man who noticed the surveillance today?”

“Yes. In Ningxia Province, he is called Great Sir.”

“Great Sir. An odd nickname for a martial artist.”

“It isn’t a particularly well-known name, either. He’s a madman, and his past is shrouded in mystery.”

“Even the East Depot couldn’t find out who he was?”

“I can’t say for certain, but at the time, the Emperor was using the Embroidered Uniform Guard to keep the East Depot in check. That clearly limited what we could find out.”

Caught up in the coinciding currents of the times, Great Sir’s existence had gradually been forgotten.

Until today, when Ma Sanbao dug through his old memories.

Listening to the story of this mysterious man, the Grand Mage suddenly found an answer to a question she’d forgotten.

*The Kongtong Sect. I wondered where Perfected Being Hyeoncheon and the Kongtong Disciples who survived Dunhuang had disappeared to along the way…*

A suspicion close to certainty. At the same time, another question surfaced, and her gaze grew distant.

*Who in the world is he?*
## Chapter artifact 1069

# Chapter 1069

When someone suddenly changes, the people around them can’t help feeling uneasy.

Especially when it happens in the middle of a chase.

“Hh…”

At Great Sir’s sudden groan, the silence shattered—and the air around us froze.

It hadn’t even been fifteen minutes since we’d shaken off the third group of pursuers.

Our allies had been moving quickly and quietly, keeping low among the shallow hills and reeds. Now they reflexively tightened their grips on their weapons. Jeok Cheongang was among them.

“What is it?”

At Jeok Cheongang’s low, grave question, everyone—including me—turned toward Great Sir.

His face had gone rigid without anyone noticing. His pupils, usually a little unfocused, had suddenly dilated, as if reflecting his state of mind. A bead of cold sweat rolled down his forehead.

“I have a bad feeling. A really bad one.”

If we’d been in Gansu, I might’ve just wondered what crazy thing he was going to say this time and let it pass.

But no matter how unhinged he was, Great Sir was an undisputed Supreme Peak master. We were in enemy territory, with threats lurking everywhere. And though it might’ve been a coincidence, he was the first to notice the enemy using birds to spy on us. His words weren’t something we could simply brush aside.

A person’s innate sixth sense had nothing to do with how advanced their martial arts were.

“A bad feeling?”

Jeok Cheongang asked gravely. Great Sir nodded.

“That’s right.”

“Explain in more detail. And be polite if you don’t want to get beaten to death.”

“Understood.”

Jeok Cheongang chuckled at Great Sir’s answer, then turned to me.

“Would it be all right if this old man taught that lunatic a lesson?”

“Would it?”

“Probably not.”

“Then why ask?”

“I thought I’d check. Anyway, so it really isn’t all right?”

“You can read his palm, but you can’t lay a hand on him.”

“Damn it. The code of the martial world has fallen to the ground.”

Jeok Cheongang sighed up at the sky, then looked at Great Sir with a half-resigned expression.

“Fine. I understand. Now keep talking. What exactly does this feeling feel like?”

“How should I put it? Like an invisible hand is squeezing my insides.”

“And?”

“My stomach keeps churning, and I’m breaking out in a cold sweat.”

“Any idea what’s causing it?”

“I don’t know. Somehow, it feels familiar…”

“Ulp!”

Before he could finish, Great Sir groaned again.

His face went pale. He moved before anyone had a chance to stop him.

*Whoosh!*

His figure shot away so quickly it left a blur behind. Great Sir vanished among the dense reeds in an instant. Jeok Cheongang, the other Supreme Peak masters, and I hurried after him.

Or, more precisely, we were about to.

Until a certain sound rang out clearly from the reeds.

*Flap, flap-flap-flap!*

“…?”

What the hell was that?

Just as we all began to dread the answer, Great Sir’s voice confirmed our suspicions.

“Ahhh, that’s better…”

“……!”

“……!”

A deathly silence settled over the area. Jeok Cheongang stared at me in disbelief, then finally parted his tightly shut lips.

“Are you sure it’s not all right?”

“……”

“I won’t kill him. I’ll just break one thing. His arm or something, not his leg.”

At Jeok Cheongang’s earnest plea, Bow Saint muttered through her pinched nose.

“An arm might be all right…”

I’ll admit, I was tempted.

But I resisted the urge through superhuman self-control and shook my head.

*Sixth sense, my ass.*

If he could just refrain from acting like a complete idiot for once, that’d be a miracle. What had I expected from someone who didn’t even know his own name?

*Still, he more than pulls his weight.*

I swallowed a sigh. Great Sir—who’d just finished taking care of business with a racket that was anything but discreet—emerged looking completely at ease.

“Whew. I feel great.”

“……A minute ago, you said you felt really bad.”

“Me? I don’t believe I did. You must’ve misunderstood.”

“You’re pissing me off.”

“Hm? What was that?”

“Nothing. Just talking to myself.”

“Hm. That’s a bad habit. It doesn’t bother me, but you should break it soon. If you talk to yourself too often, people might think you’ve lost your mind.”

“……”

I must’ve lost my grip on reason for a moment.

My vision blurred, and when it cleared, a fierce-looking face was blocking my view.

“Whoa! Take it easy, take it easy!”

“Let go! Let go! That ugly face of yours is already bad enough. Want me to make it even worse?”

Ma Junggeol—the chief of the mounted bandits who’d somehow ended up following us this far, and now the head of a horse-caravan business—looked at me sadly.

“……That was a bit harsh.”

“Ah, sorry. I got carried away.”

My apology eased some of the sadness from Ma Junggeol’s face.

“Calm down. You know Great Sir didn’t mean anything by it.”

Of course I knew.

Maybe that was why his innocence made me even angrier.

He’d been a complete nuisance at a critical moment, and all that fuss had been over a satisfying bowel movement.

Even Shakyamuni himself would have shouted, “Amitabha, fuck this! Guanyin, drop dead!” and cracked Great Sir’s skull with a wooden fish.

*But I can’t exactly leave him behind somewhere.*

If pure evil existed, maybe Great Sir was it.

I sighed deeply and raised a hand for everyone to get moving.

Every moment mattered, and we’d already wasted nearly fifteen minutes for nothing. We needed to pick up the pace.

*At this rate, it could take us several more days just to reach our destination.*

The first attack had come before we’d even made it all the way down from the mountain range. By now, the enemy had caught up with us three times.

Each time, the Supreme Peak masters, including me, had led the charge and wiped out the pursuers. But the important thing was how quickly and relentlessly the enemy caught up to us.

*They have eyes to keep watch on us—and monsters that can chase us without resting for even a moment.*

Monsters that had forgotten death, pain, and fatigue.

That was what made the undead truly terrifying.

They’d been reborn from death with their emotions stripped away. They hadn’t died, yet they were already as good as dead. They’d forgotten sensation, and for the same reason, they couldn’t even feel fatigue.

*We haven’t been down from the mountains for long. But if they keep slowing us down like this…*

The words *surrounded* and *wiped out* rose in my mind. I quietly swallowed them.

Anyone who thought about defeat from the start was bound to lose in the end.

Thousands, or tens of thousands.

Even if a hundred thousand undead came to close their hands around our throats, I had to lead everyone through this dense net and keep moving.

Toward our destination far to the east, where our allies in Qinghai—including the Kunlun Sect—should be waiting.

As if she’d sensed what I was thinking, Ju Hwaran broke away from the people moving out and came over.

“If we can make it as far as Qinghai Lake, they won’t be able to pursue us so easily.”

Song Ilseom, who—as always—stayed close beside Ju Hwaran like a shadow, spoke up unexpectedly.

“You’re not wrong. But that’s only if all of Qinghai’s forces have gathered there, and those monsters aren’t pursuing us with everything they have.”

“……Captain Song.”

“No, Young Lady Ju. He’s right.”

In a way, it was a discouraging thing to say, but Song Ilseom’s judgment was cold and accurate.

You could keep hope in a corner of your heart, but your mind had to question everything.

Build for the worst, then strive for the best.

That was the most important thing when it came to survival and victory.

“How far is it to Qinghai Lake?”

“If we push ourselves to the limit, two days. I’ve gone over the map in detail, and there’s no route that would get us there any faster.”

The old map in Ju Hwaran’s hands was anything but ordinary.

She’d inherited it from her grandfather, who’d even been called the Escort King. It contained detailed notes on secret roads hidden throughout the land and the features of each region.

But this was Qinghai Province.

Especially in the northwest, with its endless open plains and basins, only sparse vegetation and reed beds grew. The terrain was full of obstacles for us.

*But perfect for them.*

Ju Hwaran had said that even if we pushed ourselves to the limit, it would take two days to reach Qinghai Lake.

If the pursuers kept catching up, that could mean three days, four days, or even more than a fortnight.

*They’re pursuing us harder than I expected. Stealth or speed—we’ll have to give up one of them.*

That left me with only one choice.

And the first thing I needed to do was obvious.

“Take it off.”

I abruptly picked up the pace and tossed out the order.

Jeong Hogun, who was hunched low at the rear of the Embroidered Uniform Guard, reflexively asked, “What?”

“Say that again.”

“……What did you say?”

“I said take it off right now.”

At the sight of Jeong Hogun’s eyes practically shaking, I added an explanation to head off any misunderstanding.

“Don’t get any dirty ideas. I’m talking about that damn armor.”

I pointed at the armor, which had been thoroughly smeared with mud to hide its distinctive shine. Jeong Hogun frowned.

“I can’t. His Majesty personally bestowed this on every member of the Embroidered Uniform Guard.”

“You don’t want to?”

“That’s right. No matter what orders the Marquis of Shangshan gives, this armor carries the authority and honor of the imperial family.”

“So you’d rather die protecting that authority and honor?”

“That’s…”

“Fine. Keep wearing it, then. When you fall behind, we can just leave you behind.”

After a brief silence, Jeong Hogun answered.

“On second thought, I believe His Majesty did tell us to put the Marquis of Shangshan’s orders first.”

“That’s a pretty ugly excuse.”

“Damn it.”

“I’ll take that as agreement. Don’t waste time—give the order to your men right now…”

I trailed off and stared into the hazy darkness that had settled around us.

Then I sighed and spoke to Jeong Hogun, who’d just taken off his helmet.

“Don’t take it off yet.”

At that moment—

*Rumble.*

A tremor unlike anything the previous pursuers had caused began to churn in the distance.

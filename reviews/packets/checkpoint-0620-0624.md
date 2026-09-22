# Checkpoint Review — 620–624

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

# Chapters 620–624

## Plot

The Fire Dragon Pavilion confirms that the Poison Flower Pavilion owner is Namho, a Hidden Shadow Pavilion agent who has spent over fifty years surveying Nanman. Namho stages the destruction of his inn to conceal the contact, gives the group a wooden map of Nanman, and joins them after receiving the Pavilion Master’s warning about the rift. He guides them toward the Nanman Beast Palace, activating and advancing the related Chain Quest.

After a dangerous journey through Nanman, including repeated poisonings, lethal fungi, and hostile terrain, the party reaches the Beast Palace’s vast directly administered territory. Taishan’s attempt to eat a protected calf causes a confrontation, while Namho’s emergency signal accidentally starts a pasture fire. Jin Taekyung extinguishes it, and the Beast Palace’s Young Palace Lord, Yayul Mok, arrives on a white tiger and escorts the group inside.

The Nanman Beast Palace’s Outer Hall is effectively a city populated by Miao people and beasts. Its residents distrust the Han Chinese because the Heavenly Demon Escort Bureau massacred a Miao village about a month earlier. Sama Pyo suspects the massacre was timed as part of a larger scheme. Taekyung recognizes the powerful aura of Yayul Mok’s father, Yayul Cheok—the Beast Miao King—who is waiting in the Outer Hall.

## Continuity

- Namho is the Hidden Shadow Pavilion agent formerly posing as the Poison Flower Pavilion owner. He is an eighty-year-old Miao elder who has lived in Nanman for over fifty years.
- Namho gave the Fire Dragon Pavilion a wooden map recording Nanman’s terrain and tribal locations and is guiding the party through the Beast Palace’s territory.
- The Nanman Beast Palace Chain Quest is active; the party has arrived at the palace and reached its Outer Hall.
- Yayul Mok is the Nanman Beast Palace’s Young Palace Lord. He rides a long-bonded white tiger, understands spoken Han Chinese, and ordered the Fire Dragon Pavilion to follow him.
- Yayul Cheok is the Beast Miao King, ruler of the Nanman Beast Palace, leader of the Miao people, and the lowest-ranked of the Ten Kings. Taekyung has identified him by his aura, but their conversation has not begun.
- The Fire Dragon Pavilion trespassed into protected Beast Palace territory and caused a serious pasture fire, though Taekyung ultimately extinguished it.
- Taishan remains a powerful but unpredictable asset whose appetite creates immediate diplomatic and operational problems.
- Nanman residents distrust Han Chinese because the Heavenly Demon Escort Bureau recently massacred a Miao village.
- Sama Pyo suspects the massacre’s timing is connected to a larger scheme, while Song Ilseom remains hostile toward him and avoids discussing it.
- The identity of the woman traveling with the earlier Heavenly Demon Escort Bureau group, the reason for that massacre, and the poisoner who killed the group remain unresolved.
- Dark Heaven is targeting Nanman, and the approaching disaster associated with the rift remains an active concern.

## Translation Decisions

- Use **Namho**, **Nanman**, **Nanman Beast Palace**, **Outer Hall**, **Yayul Mok**, and **Yayul Cheok** consistently.
- Render **소궁주** as **Young Palace Lord** and **야수묘왕** as **Beast Miao King**.
- Render **天魔镖局** as **Heavenly Demon Escort Bureau** and **蛮族** as **Man people** where applicable.
- Preserve **Hidden Shadow Pavilion**, **Fire Dragon Pavilion**, **Blazing Flame Divine Dragon**, **Pavilion Master**, and **Chain Quest**.
- Render **一山有四季, 十里不同天** as “One mountain holds four seasons, and ten li bring a different sky.”
- Preserve Taishan’s clipped, childlike speech and the established forms **Young Lady Ju** and **Great Hero Jin**.

## Durable state

{
  "active_continuity": [
    "The Fire Dragon Pavilion is inside the Nanman Beast Palace's territory and has now reached its massive Outer Hall under Yayul Mok's escort.",
    "Yayul Mok is the non-Han Young Palace Lord of the Nanman Beast Palace, rides a long-bonded white tiger, and understands Han Chinese well enough to follow Taekyung's remarks.",
    "Yayul Cheok is the Beast Miao King, lord of the Nanman Beast Palace and leader of the Miao people.",
    "Taishan is a major Fire Dragon Pavilion asset but his childlike appetite creates immediate operational problems, including attacking animals for food.",
    "Nanman residents distrust Han Chinese because the Heavenly Demon Escort Bureau recently massacred a Miao village.",
    "Sama Pyo suspects the massacre's timing may be connected to a larger scheme, while Song Ilseom remains openly hostile toward him.",
    "Taekyung has sensed the Beast Miao King's powerful aura and identified him before their conversation begins."
  ],
  "continuity_sources": [
    624
  ],
  "open_questions": [
    "How will the Beast Miao King respond to the Fire Dragon Pavilion's arrival and the recent massacre's effect on Nanman's view of Han Chinese?",
    "Was the timing of the Heavenly Demon Escort Bureau massacre connected to Dark Heaven's scheme?"
  ],
  "safe_through": 624,
  "temporary_decisions": [
    "Use Yayul Mok for 야율목 and Yayul Cheok for 야율척.",
    "Use Young Palace Lord for 소궁주 and Beast Miao King for 야수묘왕.",
    "Render 一山有四季, 十里不同天 as “One mountain holds four seasons, and ten li bring a different sky.”"
  ],
  "version": 1
}

## Reading copies

## Chapter artifact 620

# Chapter 620

“Nice to meet you. Blazing Flame Divine Dragon Jin Taekyung.”

“……!”

A low voice burrowed into my ears, and a ripple of agitation spread through the room. But instead of being startled, I stared quietly at the old man.

While speaking with him, I had already suspected to some degree that he might be an agent of the Hidden Shadow Pavilion.

*He certainly had the right conditions.*

The old man before me was the owner of the meeting place Thousand-Faced Fox had told us about. And unlike the other non-Han locals, he hadn’t shown us any particular hostility.

Still, if you didn’t want to misstep, you had to knock on even a stone bridge before crossing it.

The System had warned me through the *Journey to Nanman* Quest, too. To stay alert at all times and act flexibly.

At least this time, I intended to follow that advice faithfully.

Ssshhh.

Invisible internal energy spread around the inside of the inn. In a space where all sound from outside had been cut off, I quietly opened my mouth.

“Are you affiliated with the Hidden Shadow Pavilion?”

That was probably the question everyone wanted to ask.

As all eyes turned toward him, the old man stroked a filthy liquor cup and answered,

“It has already become a distant past—the time when I received a second name, Namho.”

Namho. Literally, it meant “amber from the south.”

The Hidden Shadow Pavilion was an intelligence organization, so it gave its agents codenames to conceal their identities. The name Namho matched the information Thousand-Faced Fox had given us exactly.

“One fox said a fierce wind was blowing in Nanman.”

“Even if a typhoon rages, the Poison Flower rooted deep in the ground will not be shaken.”

After confirming even the secret signal Thousand-Faced Fox had given me, I was finally certain.

I refilled the liquor cup sitting in front of the old man—no, Namho—and spoke.

“To be honest, I never let go of my suspicions until the very end… But you really are affiliated with the Hidden Shadow Pavilion.”

Namho drained his cup in one gulp and asked,

“Why? Did you never imagine that an agent of the Murim Alliance’s Hidden Shadow Pavilion might be one of the non-Han peoples?”

Just as Namho said, he was indeed not Han Chinese.

His dark, sun-browned skin from Nanman’s blazing heat and his distinctive features were far removed from those of the Han Chinese—so much so that anyone with even a little observational skill could tell at once.

I gave a small nod and answered,

“To be honest, I can’t say I didn’t think that. It’s just that you’re so far from the Central Plains that it was hard to believe you were with the Murim Alliance’s Hidden Shadow Pavilion. And from what I could sense, you didn’t seem to have learned martial arts, either.”

“Everyone has their own circumstances. What matters is that most people think as you did.”

“Because everyone accepted you that way, you were able to avoid suspicion?”

“Who would suspect an old non-Han man who hasn’t learned even a single martial arts move? It would be absurd.”

After emptying the last remaining bottle of liquor, Namho suddenly opened his mouth as if he had just remembered something.

“Oh. Did you block the sound with your internal energy?”

“Of course. We can’t let this conversation leak outside.”

“Then lower it for a moment. There’s something I absolutely must do.”

Something he absolutely had to do?

What was it?

I wanted to ask in more detail, but Namho’s expression was utterly serious.

And the moment I withdrew the internal energy that had sealed off every direction, Namho suddenly turned toward Hyuk Mujin.

“You there. Who’s standing behind you?”

“Huh?”

Crash!

“Get the hell out of here, you rude Han bastards!”

It happened in the blink of an eye.

A liquor bottle struck Hyuk Mujin squarely in the back of the head, cracking him over the skull. The cheap bottle shattered, sending fragments flying in every direction.

And Namho, the obvious culprit behind it all, began shouting at the top of his lungs.

“You bastards! Even tearing you apart wouldn’t satisfy me! How dare you cause trouble here!”

“……!”

“……!”

Everyone, myself included, stared with our mouths hanging open at the sudden turn of events.

Of course, no one was more shocked than Hyuk Mujin. Clutching the back of his head, he stared blankly at Namho before shouting,

“Has this old man gone insane?”

“Yeah, I’m insane! You motherless, fatherless Han bastard!”

“Whoa. That’s crossing a line. You’re crossing a line!”

“You Han bastards crossed the line! As if murdering people in Nanman weren’t enough, now you’re eating without paying!”

“No, fuck! What did you do with the silver coin I gave you earlier? Boil soup with it?”

“You didn’t give me a single penny, so what kind of bullshit are you spouting? I took pity on you and gave you a meal after agonizing over it, and now get the hell out of my sight!”

Whoosh! Crash!

Liquor bottles and bowls flew in every direction. Within only a few seconds, the inside of the inn had turned into a complete mess.

Namho hurled every object he could get his hands on while screaming every insult under the sun. Then his lips moved ever so slightly as he looked toward me.

*Half a shichen[^1] from now. Meet me by the lakeside ten li away.*

[^1]: A shichen is approximately two hours, while ten li is approximately five kilometers.

Only then did I understand the meaning behind his actions. I signaled to the members of the Fire Dragon Pavilion.

Ju Hwaran, Song Ilseom, and Sama Pyo, all quick to catch on, sprang to their feet, overturned tables, and smashed everything in sight.

Of course, they didn’t forget to shout a line each.

“Food!”

“Dog!”

“Tastes like shit!”

Crash-crash-crash!

Crack! Rumble!

When one unfortunate pillar was smashed to pieces, the ceiling tilted.

The Poison Flower Pavilion had already been on the verge of collapse. At this rate, it really was time to change its name to Crumble Mansion.

I grabbed Hyuk Mujin, who was still shouting at Namho at the top of his lungs, and Taishan, who was shoveling the remaining food into his mouth, by the backs of their necks and ran.

“You crazy old man! You ate your age through your asshole—cough!”

“No! Taishan’s chicken leg! He was saving it!”

“Quit your bullshit and get out! All of you!”

Crunch!

Screams and clouds of dust mingled together in the middle of the chaos.

The Fire Dragon Pavilion members rushed out of the Poison Flower Pavilion with me at the front. Waiting outside was a crowd that had grown to a hundred people.

“The Han bastards are out!”

“They dared attack Elder Chao!”

“Kill them!”

“No! Throw them alive into the snake pit!”

Of course, there wasn’t a single sane person among them who wanted to be thrown alive into a snake pit.

Sss! Thud!

As I dodged a pickaxe with a sigh, a delayed System notification pierced my ears.

Ding.

> **System**
>
> - Mission **Contact with a Hidden Shadow Pavilion Agent** completed!
> - Quest **Seeds Planted in Nanman** completed successfully!
> - Quest completion Reward acquired!
> - A small amount of EXP acquired!
> - A small amount of Fame acquired!
> - A new linked Quest has been generated!

*So where exactly is this lakeside?*

* * *

Just as he had said, Namho appeared exactly half a shichen later.

He had a bundle in one hand, while the other was wrapped tightly in bandages.

“The pillar. Who broke it?”

“…….”

“…….”

“The inn I operated for forty years collapsed. I nearly died without even getting the chance to leave a will.”

I cautiously tried to comfort him.

“We didn’t know that would happen. Everything will be all right.”

“Is that something to say? Does saying it’s all right make everything all right?”

“We’ll compensate you properly later.”

“That makes it a little better.”

As expected, nothing worked in this world like financial therapy. Namho’s condition improved in an instant as he looked at us and spoke.

“Understand what happened at the inn. I had no choice if I wanted to avoid the villagers’ suspicions. The atmosphere is so dangerous these days that if I had protected you, I would have drawn attention too.”

Hyuk Mujin answered sourly,

“So you killed off my parents when they’re both alive and well?”

“I apologize for saying you had no mother or father. It couldn’t be helped.”

“How would you feel if someone said the same thing to you?”

“I grew up alone from a young age. My parents died early, so I don’t even remember their faces.”

“Ah.”

As expected, years of experience as a Hidden Shadow Pavilion agent were no joke.

With only a brief exchange, Namho had silenced Hyuk Mujin. He took something out of the bundle in his hand and held it out to us.

“What is this?”

“A wooden map. For more than fifty years, whenever I had the time, I traveled all over Nanman and recorded the terrain and the locations of the tribes in detail.”

A long time had passed since the Great Faction War ended, but that didn’t mean everyone had been basking in peace.

Namho, too, had continued his work without forgetting his duty.

“Nanman is full of treacherous terrain, predators, and venomous beasts. It couldn’t have been easy… You must have gone through a great deal.”

Namho’s expression turned bitter at Ju Hwaran’s exclamation.

“আমি did nothing more than what needed to be done. In fact, while making this map, I hoped it would never be needed.”

But contrary to Namho’s wishes, peace had ended.

Dark Heaven had shed the shell of the Demonic Cult and run rampant. Blood had stained every corner of the Central Plains, and that dark shadow was now stretching beyond the Central Plains into Nanman.

“I already know what happened before and after. The Pavilion Master is deeply concerned. Do you feel the same way?”

“Yes.”

I nodded without hesitation.

Considering the chain of events centered around the Water God Dragon in Hubei, Nanman was nothing less than a powder keg on the verge of exploding.

It was a place crawling with countless spiritual creatures, venomous beasts, and wild animals beyond anything the Central Plains could compare with.

“I assume you’ve already heard about the rift.”

“Nanman is a remote place. Rumors about it haven’t reached the people here yet, but I received the news through a messenger eagle. If the Pavilion Master had not sent the letter, it would have been a story I couldn’t have believed.”

Anyone else would have felt the same, even if they weren’t Namho.

The Central Plains people who had heard about the Water God Dragon were treating it as a ridiculous rumor, after all.

But it wouldn’t be long before these impossible events became reality.

Just as they had during the period modern people called the Great Cataclysm.

“Dark Heaven is definitely targeting Nanman. Even if nothing has surfaced yet, something will happen before long.”

Namho stared at me with sunken eyes as I spoke with complete certainty.

“Long ago, I left Nanman of my own accord by entrusting myself to a Central Plains merchant caravan. And for the past fifty-odd years, I haven’t left this land even once. But aside from that incident a little while ago, nothing happened.”

“Do you mean the incident where the Central Plains people claiming to have come from the Heavenly Demon Escort Bureau attacked a nearby village?”

“Yes. The non-Han locals grew furious, and the atmosphere became dangerous, but that was all. It wasn’t common, but it wasn’t something that had never happened before, either.”

“I don’t know what connection that incident might have had with Dark Heaven, but…”

I continued in a low voice.

“From now on, a tragedy will occur that makes that look insignificant.”

“……!”

Namho’s eyes trembled.

This was his homeland, the land where he had lived all his life. After a short silence, an aged voice slipped between his lips.

“Even while packing my belongings and leaving my home, I didn’t want to believe it. But now that things have come to this, I have no choice.”

Namho slung the bundle over his shoulder and took a step forward.

“Let’s go. Wherever your destination is, I’ll guide you.”
## Chapter artifact 621

# Chapter 621

“Let’s go. Wherever your destination is, I’ll lead the way.”

I looked at Namho, the elderly Hidden Shadow Pavilion agent, with admiration. Despite his advanced age, he was showing an iron will.

“You’re saying you’ll lead us even if our destination is the afterlife. I don’t know what to say in response to the sense of honor you’ve shown us, Elder Namho.”

“No, I never said I’d follow you to the afterlife…”

“Your joints must ache these days, and you probably find yourself forgetting things more often, too. Thank you for stepping forward like this. It’ll be a great help to us.”

“……How very kind of you. Listening to you, I feel as if strength and motivation are welling up throughout this old body of mine.”

“You’re welcome. There’s no need to thank me.”

Namho stared at me with a sour expression before suddenly opening his mouth.

“But where are we going? I may have a different idea, but I’d like to hear your desired destination first.”

Destination, huh?

Instead of answering, I glanced up at the empty air.

The space above us was, quite literally, an empty void where there was nothing at all.

But just as it had happened countless times before, I could read information in that empty space—information that no one else here could see.



> **System**
>
> **Quest**
>
> **Nanman Beast Palace**
>
> The Nanman Beast Palace is one of the representative great powers classified as part of the Outer Lands, and it is located in the deepest, most secluded part of Nanman—a land that is already extremely closed off.
>
> However, the Murim of the Central Plains now needs their help for the Great War that is soon to come. The time has come to awaken the beast of the jungle that has slept for so long.
>
> Or perhaps… to save the beast from a crisis that has yet to reveal itself.
>
> **Grade:** Supreme Peak
>
> **Restriction:** Jin Taekyung and Fire Dragon Pavilion members
>
> **Mission:** Arrive at the Nanman Beast Palace (Incomplete)
>
> **Reward:** Chain Quest
>
> ???
>
> **Failure:** ???



It was the Chain Quest that had been newly updated right after meeting Namho, and it was also a signpost that matched my own thoughts.

“The Nanman Beast Palace. We’re heading to the Nanman Beast Palace.”

At my belated answer, Namho nodded with deeply sunken eyes.

* * *

Nanman was an expansive land, but it was also unbelievably rugged.

In terms of land area, it was smaller than Sichuan, but the effort required to travel through it was incomparable to anything in the Central Plains.

“The Pavilion Master once said this: ten li in Nanman is the same as a hundred li in the Central Plains.”

Anyone who couldn’t understand Namho’s words had never set foot in Nanman.

Because in only half a day, the Fire Dragon Pavilion members and I had learned exactly what a damnable place Nanman was.

Bzzzzzt. Smack!

“Mujin, what was that sound just now?”

“It was nothing. Just a mosquito. My nape suddenly stung, so I wondered what it was.”

“Oh, really? Still, be careful. You never know. Should I call Elder Namho and ask him about it?”

“Come on, Captain. What do you take me for, a child? Hyuk Mujin, a battle-hardened warrior who has fought countless fierce battles at the right hand of the Blazing Flame Divine Dragon! That’s me.”

Exactly one shichen[^1] later, the battle-hardened warrior Hyuk Mujin collapsed while vomiting.

“Bleeaaagh!”

“Gasp, Mujin!”

“What happened?”

“Elder Namho! Mujin has collapsed!”

“Even if I am old, I can clearly see when someone has collapsed. Was he bitten by a mosquito?”

“Cough, yes. About one shichen ago, by one with blue stripes…”

“Blue stripes? And it was one shichen ago? An antidote. Hurry and bring me an antidote!”

Fortunately, getting the battle-hardened warrior back on his feet wasn’t particularly difficult.

I had the Myriad-Poison Ring, a treasured item of the Sichuan Tang Clan, as well as fifty antidotes I had received as Quest rewards.

But that didn’t mean we could let our guard down.

“They normally swarm together in groups of dozens and even hunt predators. If we’d been one shichen later, he wouldn’t be among the living anymore.”

With Namho’s stern warning ringing in our ears, we resumed moving deeper into the secluded land, avoiding the eyes of the non-Han peoples who charged at Han Chinese the moment they saw them.

And that meant we were heading into an even more dangerous place.

“Taishan! Taishan’s stomach hurts too much! It feels like it’s being torn apart!”

“Elder Namho!”

“What did you eat this time?”

“Taishan was hungry, so Taishan picked and ate the red mushrooms growing on a tree.”

“What kind of dog and pig bastard are you? After all the warnings I gave you, you ate blood-feeding fungus that even a tiger couldn’t withstand just because you were hungry? Antidotes won’t work on this!”

Namho personally unleashed a fit of absolute fury, but his anger soon turned into bewilderment.

Taishan had eaten whatever this blood-feeding fungus was—the kind that even a tiger supposedly couldn’t survive—and then gone into the brush to do his business. Afterward, he came back looking perfectly fine.

“Taishan. Feels better after shitting it all out. Taishan is fine now.”

“……Is that thing even human?”

After a moment of thought, Sama Pyo answered in an uncertain voice.

“Probably.”

“Taishan is hungry again now that Taishan’s stomach is empty.”

“I swear by heaven and earth, if you ever eat another mushroom, you’d better be prepared never to feel hunger again.”

“Oh. Taishan. Tempting.”

“……I regret everything. If I had learned martial arts, I would have killed that bastard with a single palm strike by now.”

We continued on our way, leaving the old Hidden Shadow Pavilion agent to lament behind us.

Dense jungle and humid, sweltering heat awaited us at every step, while the eyes of predators lurking throughout the overgrown brush and swamplands glowed a vivid yellow.

*Did we come to Nanman, or did we somehow end up in the Amazon?*

What a goddamn shithole.

What kind of place was this? Tigers were more common than stray cats in a university neighborhood full of studio apartments, and crocodiles teemed like tadpoles in Cheonggyecheon.

Of course, even that was child’s play compared to the strange poisonous flowers and plants that could knock you out from their scent alone, or the bees that flew around with stingers larger than their own bodies.

At least the predators were large enough to be seen.

There was a reason Hyuk Mujin had started groaning only a day or two after leaving Yeongin.

“To hell with the Nanman Beast Palace. I think I’ll be dead by the day after tomorrow.”

Even if it wasn’t by the day after tomorrow, he did look as if his life would be in danger four days from now. He had been poisoned about four times on the first day alone, and over the past two days he had become skin and bones.

Shanxi Province was considered a borderland from the Central Plains’ perspective, but Nanman had gone far beyond anything we had expected.

“Can’t we take another route? It might be a little run-down and rough, but compared to this place, it’d practically be a flower-lined path.”

It wasn’t as if there were no paths in Nanman at all.

Though it was severely underdeveloped compared to the Central Plains, I had heard that the dozens or even hundreds of non-Han peoples who had settled in Nanman each claimed their own territories, and that it wasn’t particularly unusual for them to travel back and forth so long as they didn’t cause disputes.

But despite Hyuk Mujin’s desperate plea, Namho’s answer was firm.

“Impossible. You know the reason, don’t you?”

“If it’s because of the non-Han peoples who are dying to kill us, I’d rather just face them head-on. If we can settle things through conversation, then all the better.”

“Conversation?”

Namho blinked at Hyuk Mujin’s answer, which was full of dreams and hope.

“Are you serious?”

“Of course.”

“An entire village disappeared. More than two hundred people who had welcomed Han Chinese with goodwill were slaughtered, regardless of age or sex. Do you think conversation will work?”

“……No. Actually, I wasn’t serious.”

“You’re finally being honest. Fine, then shut up and keep moving.”

“Yes, sir.”

*Look at Captain Hyuk’s lightning-fast change of attitude.*

But this time, Namho was completely right.

Saying that we would fight the non-Han people who attacked us was the same as declaring war on all of Nanman.

They normally snarled at one another, but one of Nanman’s defining traits was that they would unite as if nothing had happened whenever an external enemy appeared.

*That must be why even the Demonic Cult couldn’t completely conquer Nanman during the Great Faction War.*

The hundred thousand demonic soldiers of the Demonic Cult, who had once swallowed half the world, had only been able to plant their flags around Nanman’s outskirts before withdrawing.

They knew that if they went any deeper into this jungle, with its brutal endemic diseases, treacherous terrain, and countless predators and venomous beasts, the losses would outweigh the gains.

*But it’s not as if we can go around revealing our identities, either.*

It was questionable whether the non-Han peoples, whose hatred of Han Chinese ran so deep, would lower their hostility that easily. But more important was the presence of Dark Heaven, which was surely lurking somewhere in Nanman.

*They’re definitely targeting Nanman. It’s only a matter of time before something happens.*

This was an assumption bordering on certainty. There was a reason we had traveled secretly, like nighttime thieves, all the way from Henan, where the Murim Alliance headquarters was located.

We had been forced to reveal our identities to the bandits of the Water Dragon Stronghold on the way to Nanman, but we had also made certain that they kept their mouths shut.

That was why we hadn’t sent word to the Emei Sect, the Qingcheng Sect, or the Sichuan Tang Clan, despite the ties we had formed during our previous journey to Sichuan.

But if we revealed our identities to the non-Han peoples, all our efforts would be wasted.

Dark Heaven would realize that the unseen dagger was right under its nose and accelerate its plans even further. Then the door to disaster would open along with the rift.

*We can’t reveal our identities until at least after we arrive at the Nanman Beast Palace.*

The Beast Miao King, lord of the Nanman Beast Palace, had participated in the Great Faction War, and I had heard that he held goodwill toward Jeok Cheongang and the Fire Gate Clan.

Considering both the importance of our business and the position he occupied in Nanman, he was far more likely to listen than the other non-Han peoples with their eyes turned red.

*Still, we’re getting shit splattered on us because of those Heavenly Demon Escort Bureau bastards or whatever they are.*

They say the squid is the one that shames the fish market. We had been lumped together with them as part of the same Han Chinese package, and the image of both me and the Fire Dragon Pavilion members had been completely ruined.

I wasn’t even Han Chinese.

*……Is this what they call being a fake Han Chinese?*

It was incredibly unfair, but there was nothing I could do.

Even if I went up to the non-Han peoples of Nanman and pulled some shit like, “Actually, I’m not Han Chinese. I’m Korean. South, not North,” there was no way they’d understand.

Besides, when I had gotten homesick during our training at Mount Jiuhua and drawn the Korean flag, Jeok Cheongang had said only one thing.



*“Wudang?”*

*“No.”*

*“Anyone can see it’s taiji. What kind of bullshit are you spouting? If it’s taiji, it’s Wudang.”*

*“If it’s taiji, it’s Korea.”*

*“What’s Korea?”*

*“That’s… Never mind. You don’t need to know, Old Master.”*

*“An extra two hundred geun of iron balls.”*

*“……Two hundred geun? Why?”*

*“You don’t need to know.”*



Even remembering it brought tears to my eyes.

It felt like only yesterday that I had been suffering in this distant land of another dimension, yet the fact that the suffering was still ongoing was enough to make me despair.

“Whew.”

At the sight of me sighing, Namho glared fiercely.

“What? Do you also want to go down there and settle things through conversation right now? Or would you rather throw down with the non-Han peoples?”

“……Why are you suddenly revving up like that? I have absolutely no desire to do either.”

“That’s a relief.”

There had already been plenty of chances to throw down with someone, and there would be plenty more in the future. Even now, several predators were wandering around us, letting out their cries.

After surveying the densely packed jungle and swamplands, I asked Namho,

“How much farther?”

“Three days if we’re quick. Six days at most.”

“That’s much farther than I expected.”

“Considering that we have to travel while avoiding prying eyes, even that is a short estimate.”

Namho, whose face had aged noticeably, patted his lower back before starting to walk again.

“From now on, don’t slow your pace for even a moment. If we cross Ailao Mountain today, we’ll be able to reach the Nanman Beast Palace in four days at the latest.”

Namho’s words proved true.

Exactly four days later, as we passed over a high mountain peak, we spotted a massive structure in the distance, shrouded in deep clouds and mist.

“The Nanman Beast Palace…”

The voice that slipped from someone’s lips spread on a wind that had blown in from somewhere.

[^1]: A shichen is approximately two hours, while a li is approximately half a kilometer. A geun is a traditional unit of weight roughly equal to 600 grams.
## Chapter artifact 622

# Chapter 622

Even counting only the time I had spent in the Murim, well over a year had already passed.

After getting tangled up in one incident after another, I had left Shanxi Province and spent my days traveling from place to place. Along the way, I had met all kinds of people and visited the sects they belonged to.

But I could say this with certainty: no matter how large or powerful a sect was, none of them could even compare to the sight unfolding before my eyes.

“Whew.”

“You’ve got to be kidding me…”

Exclamations erupted from all around us.

I had known it covered an enormous area even when I saw it from the mountain peak, but I hadn’t expected anything like this.

As the clouds and mist faded and we drew closer to our destination, my jaw dropped wider and wider.

*No, seriously. This is a sect?*

It was astonishing in two different ways.

The first, as I had already mentioned, was the sheer vastness of the place. The second was…



**Nanman Beast Palace**



The fence surrounding the vast grounds, and the wooden sign someone had scrawled in an atrocious hand.

It wasn’t a high, sturdy fortress wall or an iron gate.

It was literally a fence.

A fence.

*…No, seriously. This is a sect?*

The thought was the same. The meaning was different.

The fence wasn’t even in good condition.

I stared at the half-collapsed fence for a moment before turning to Namho.

“Elder Namho, surely this isn’t really…”

“You’re asking if this is truly the Nanman Beast Palace?”

“Ah, yes.”

When I nodded, Namho calmly opened his mouth.

“Can you read?”

“Of course.”

“Then read that sign over there. No, I suppose it would be better if I read it for you.”

Namho pointed at the sign covered in clumsy writing and continued.

“Nan. Man. Beast. Palace.”

“……”

“It says exactly what it says. The Nanman Beast Palace begins here.”

I knew that.

That was the problem.

It was so far beyond the image I had imagined in my head that I didn’t know what to make of it.

When I had seen the place from above, I had assumed there must be some enormous structure here. But now that we had emerged from the mist and come close enough to see it clearly, this was practically an empty field.

“Captain, shouldn’t this be called the Nanman Ranch instead of the Nanman Beast Palace? There are nothing but fences all around us.”

Ju Hwaran, who had been looking around, nodded at Hyuk Mujin’s dubious comment.

“This is my first time at the Nanman Beast Palace, so I can’t say I know much about it, but… it does fall short of deserving the name palace.”

Song Ilseom and Sama Pyo, who had been silently observing the situation, each added a comment.

“There is certainly something strange about this.”

“As Hyuk Mujin said, it bothers me that we haven’t seen a single person. There aren’t any other pavilions or buildings, either. Am I wrong, Taishan?”

“My lord. Taishan is hungry. Can Taishan eat that mushroom?”

Sama Pyo immediately shook his head.

“No.”

“Then what about the cow? That cow walking over there looks delicious.”

“You said you were the Young Sect Leader of the Black Dragon Demon Gate, didn’t you? This is a favor, but please shut the mouth of that beast worse than an animal. If I hear one more word, I think my chest will burst and kill me.”

“……I understand.”

“One more thing. Every blade of grass and every animal you can see belongs to the Nanman Beast Palace. Please don’t forget that—or that my insides are about to burst.”

After issuing Sama Pyo a stern warning with a face that had suddenly aged, Namho pointed toward the vast land and continued.

“I understand your thinking perfectly well, but I never said this place was the Nanman Beast Palace.”

“What? You definitely said that a moment ago.”

“I did not.”

“Ah. Have you perhaps lost your mind with age?”

“……”

Namho’s expression darkened so rapidly that there could be no doubt.

I looked at him with sympathy.

“Oh dear. Still, I’m sure you’ll be fine. Someone close to me also suffered from infirmities of old age, but they’ve almost completely recovered now.”

“I would like to say three things first. One, I do not suffer from infirmities of old age. Two. This came to mind while listening to you, so I’m a little curious. How did this acquaintance of yours overcome infirmities of old age?”

“Returned to Youth.”

“……That is a very good method. Except for the fact that I’m an eighty-year-old man who has never learned martial arts.”

“Isn’t that when life begins?”

“I’d like to end your life here, but I’ll let it go since I don’t have the strength.”

After suppressing his surging anger, Namho continued.

“Third, what I said before remains unchanged. I never said this place was the Nanman Beast Palace. I said the Nanman Beast Palace began here.”

“Oh.”

The words were similar, but their meanings were clearly different.

Now that I finally understood what Namho had meant, I asked again.

“Then?”

“That’s right. This is one of the lands under the rule of the Nanman Beast Palace. Unlike the other regions of Nanman, it is directly administered by the Palace Lord. That may make it easier to understand.”

“So it’s similar to how the Emperor appoints vassal kings or City Lords throughout the realm. This place is like the capital of a country.”

“Exactly. Of course, there are differences. The Palace Lord’s authority does not reach the Son of Heaven’s, while the authority of the various tribal chiefs throughout Nanman exceeds that of City Lords.”

Ju Hwaran, who had been listening to Namho, let out a quiet exclamation before speaking.

“Now that I think about it, I once read something similar in a record my grandfather left behind. It said that Nanman was a single kingdom, and that the Nanman Beast Palace was like a gigantic ranch encompassing five counties.”

“You truly are the Escort King’s granddaughter. But even that Great Hero Ju Gongsan never made it beyond these fences. Anyone who isn’t a member of the local ethnic groups is forbidden to enter.”

“It’s really that strict?”

“It is.”

If Namho was telling the truth, then even the Sichuan Tang Clan, a sect whose isolation was second to none in the world, would have to yield to the Nanman Beast Palace.

I clicked my tongue and stared beyond the endless line of fences and grasslands.

“But we have to get inside.”

“That’s right.”

“Is there another way? Since you’re one of the local ethnic groups, perhaps you can enter…”

“I said outsiders cannot enter. I don’t recall saying that entry was easy simply because I’m one of the local ethnic groups.”

“Oh.”

“Here, I’m nothing more than a powerless, ordinary old man of the Miao people. If Dark Heaven hadn’t extended its claws into the world, and if you people hadn’t come looking for me, I would have quietly ended my life… you bastard!”

I flinched at Namho’s sudden bellow and opened my eyes wide.

“Elder Namho, why are you blaming yourself? Why would quietly ending your life make you a son of a bitch?”

“Not me! That bastard! That fucking son of a bitch—catch him!”

At Namho’s shout, which sounded as if he were about to choke to death, we turned our heads.

A huge backside was crawling over the fence.

And in front of it, a single yellow calf was peacefully grazing.

“Oh. Oh, no?”

“That guy, surely not…”

“When did that bastard get over there?”

“Young Hero Tae!”

“Taishan!”

At the voices of the others, followed at last by Sama Pyo’s desperate cry, Taishan flinched.

*Moo?*

The calf realized something was wrong and raised its head sharply.

Taishan had somehow already drawn close. An exclamation mark seemed to pop into the calf’s large, clear eyes, and at the same time, its still-growing hooves struck the grass.

*Pat-pat-pat!*

It made a split-second judgment and tried to flee.

But Taishan was one step faster than the calf.

“Beef! Stop right there!”

With a shout filled with iron determination, Taishan’s enormous body soared through the air.

It wasn’t a tiger or leopard, but how could a half-grown calf evade a Peak master who had set his mind on catching it?

With a heavy *thud*, the calf pinned beneath him let out a scream.

*Moooooo!*

It was such a plaintive cry that merely hearing it made my eyes sting.

But to Taishan, whose stomach had turned inside out from the consecutive forced marches and strictly rationed meals, it was enough to make his mouth water.

“Taishan! Beef!”

“Grab that bastard right now!”

Before Namho had even finished shouting, I had already vaulted over the fence and dashed right up to Taishan.

*Grab.*

“Let go! Beef tartare!”

“Stop it, you heartless, bloodthirsty lunatic. You haven’t even seen *The Sound of the Bell*?”[^1]

“I haven’t!”

“……Ah.”

That made sense.

I understood for a moment, but that was that and this was this. I grabbed Taishan by the back of the neck and pulled him away with an appropriate amount of force.

When his mountain-sized body toppled backward, the beef—or rather, the calf—finally escaped with its life. It sprang to its feet and started running.

*Thundering thud-thud-thud!*

Grass flipped wildly into the air, followed by clouds of dust.

As Taishan watched the calf’s rump disappear from the pasture at full speed, he muttered mournfully.

“No. Taishan’s rump meat…”

*Was this guy born in Majang-dong or something?*[^2]

I was beginning to question his origins when Namho suddenly started raging, shouting like a volcano erupting.

“You bastard!”

“Elder Namho, calm down. Please, calm down.”

“How am I supposed to calm down right now? I repeatedly warned you not to touch anything in the Nanman Beast Palace’s territory! And this hulking glutton of a bastard ignored every word an elder said and went and caused trouble?”

Sama Pyo hurried over and stepped between Namho and Taishan.

“I’m sorry, Elder Namho. I only looked away for a moment, and then… Taishan, you wretch, apologize at once.”

Taishan looked Namho straight in the eye and answered.

“Taishan hungry.”

“That fucking bastard. Let go of this hand right now. Let go! You won’t? Do you think I spent more than fifty years waiting in Nanman, getting bitten by mosquitoes, just to see this?”

Life really did begin at eighty.

I only had to look at Namho, who had never learned martial arts yet was giving off an aura fierce enough to make even Jeok Cheongang yield to him for once, to know it.

The old Hidden Shadow Pavilion agent, who had been raging like a live volcano, finally calmed down after fifteen minutes.

“Whew. I’m fine now, so let go of my hand.”

“Are you really all right?”

“My internal organs turned over once in the meantime, but I’m not about to die.”

If they had turned 180 degrees, that would have been a problem.

But 360 degrees? That was acceptable.

At my nod, Hyuk Mujin released Namho’s hand. Namho sighed with the face of a man on the verge of death.

“Yes, at least nothing actually happened. If someone from the Nanman Beast Palace had witnessed that, things would have gone wrong from the very beginning.”

If this had been another sect in the Central Plains, someone might have thought, *It’s only one cow.*

But in the end, this was a difference in culture and people.

Just as grassland nomads treasured their horses like their own lives, livestock was a valuable asset here, where the divisions and boundaries between tribes were so clear.

*The place is called the Nanman Beast Palace, after all.*

Even the name gave off an unmistakably animal-friendly feeling.

There was a reason Namho had warned us from the start not to touch anything.

“Then what do we do now? We can’t just wait here until someone appears.”

“If we trespass into the Nanman Beast Palace’s territory without permission, it will cause a disturbance. In that case, we must naturally find another way.”

Answering Hyuk Mujin’s question, Namho pulled something out of his bundle.

“What is that?”

“A signal firework for emergencies. If this explodes, someone will at least come out to see what’s happening.”

With a confident smile, Namho struck a spark with a fire striker.

*Crackle.*

The fuse burned rapidly toward the end.

At the same time, the firework shot into the sky with a tremendous bang.

*Fwoooosh—boom!*

The problem was that the firework’s burst came down on the pasture instead of exploding in the air.

“……Huh?”

“……Huh?”

*Whoooosh—roar!*

The pasture was engulfed in flames alongside the stunned voices of the others.

I stared blankly at the livestock fleeing in every direction and muttered.

“……Someone will definitely come out now.”

“……This isn’t how it was supposed to go.”

Not how it was supposed to go, my ass.

We were fucked.

And just as I stared at the burning pasture with a devastated heart—

*Kraaaar!*

Along with the harsh roar of a wild beast, a figure appeared beyond the hill of the burning pasture.

[^1]: *The Sound of the Bell* is a Korean documentary film about an elderly farmer and his ox.

[^2]: Majang-dong in Seoul is famous for its livestock and meat markets.
## Chapter artifact 623

# Chapter 623

With his handsome brown skin darkened by the sun and fine muscles settled attractively across his lean frame, the non-Han young man possessed an unusual appearance that marked him as different from the Han Chinese of the Central Plains.

As he gazed at the scene below the hill, he thought,

*…What is going on?*

His confusion was only natural. A vast pasture was blazing before his eyes.

Even now, the rapidly spreading flames were belching endless clouds of black smoke, while cows, sheep, horses, and other livestock fled frantically through the chaos.

*Grrrr.*

A low growl and tremor suddenly reached him from below. The young man gently stroked the snow-white mane of the white tiger beneath him.

“It’s all right. It’s okay.”

*Grrk.*

“You’re really angry, aren’t you?”

Feelings were not conveyed through words alone.

Though human and beast belonged to different species, they had spent so many years together that they could understand each other through the slightest gesture or the rise and fall of a growl.

The non-Han young man met the white tiger’s blue gaze and nodded.

“That’s right. We’ll put out the fire first. Punishing the intruders comes afterward.”

If they left it alone, the flames would grow beyond control and turn the entire pasture into ashes.

The land could be restored, of course, but they still had to save the livestock that would otherwise be swallowed by the flames and die.

And then came the next matter…

*How dare they do something like this?*

As if trespassing into the Nanman Beast Palace’s territory without permission were not enough, those insolent bastards had even set it on fire. They had to be punished.

The non-Han young man glared at the mysterious intruders barely visible through the distant, acrid smoke and stroked the white tiger’s mane.

The white beast understood his intention and shot forward like the wind.

*Kraaaar!*

A thunderous roar rang out through the flames.

* * *

It happened in the blink of an eye.

A white tiger and a non-Han young man had suddenly appeared on the hill, then began rushing about in every direction as though they had become one body.

*Whoosh—roar!*

*I think I saw something like this in an educational comic when I was little.*

Was this what they called fighting fire with fire?

One fire collided with another. They devoured each other until one disappeared. The young man’s skillfully raised backfire was remarkably effective.

As the flames quickly died down as if nothing had happened, I stepped forward to lend a hand out of sheer conscience.

*Boom!*

I struck out with a short, sharply cut-off punch. The flames wavered like a candle in the wind…

…and then grew even larger.

*ROOOOAR!*

“Good grief.”

What the hell was this?

As I stood there in confusion, Namho shouted at me like he was screaming in agony.

“This is insane! What the hell did you do?”

“…Is that really something for Old Man Nam to say? It’s like the one who farted getting angry. The person who set the fire is complaining.”

“I didn’t know it would turn out like this!”

“Neither did I.”

“Is that what matters right now? Put out the fire first… Oh, oh, oh! Behind you! Behind you!”

*ROOOOAR!*

“Don’t be so dramatic. It’s still fine.”

The flames had not become overwhelmingly powerful, but we did need to deal with them as quickly as possible.

Pressed for time, I sent a series of palm strikes toward the flames that had suddenly swollen in size without giving it any further thought.

And then I realized.

*Oh, right.*

The name of the palm technique I had just used was the Flame Divine Palm.

*Fwoooooosh!*

The flames had not been this strong a moment ago, but now I could say it with confidence.

They had become enormously powerful.

In one sense, it was almost a miraculous sight. Flames that had been nearly extinguished were now roaring several times higher than before.

Of course, to the livestock fleeing madly in every direction, it was probably a scene straight out of hell.

“…Huh.”

I silently shifted my gaze between the near-inferno around us and my palms. Beyond the raging flames, I met the eyes of two pairs of furious eyes glaring at me.

They belonged to the white tiger that had appeared on the hill and the non-Han young man.

Their eye colors and species were different, but they had one thing in common.

They were both absolutely pissed off.

“You bastard! What do you think you’re doing?”

*Kraaaar!*

The kid looked young, yet he was speaking casually to me on our first meeting.

Clearly, he had crossed a line—but I was the one who had burned that line down. As a civilized man of the twenty-first century, I reassured them with a polite and composed attitude.

“I don’t know who you are, but don’t worry. I’ll handle this.”

Of course, there was no guarantee that the other party would feel reassured just because I had reassured them.

As demonstrated by the immediate response.

“No! You can’t!”

*Kraaaar!*

I gently admonished the one man and one tiger shouting in perfect unison.

“It’s okay. I can do this. More importantly, could you quiet the tiger down a little?”

“No! You cur!”

*Kraaaar!*

“Don’t?”

“Don’t!”

*KRAAAAR!*

Hmm. They were putting up as much resistance as the flames.

But I shook my head.

“No. I’m going to do it. I trust myself.”

“You crazy Han Chinese bas—!”

*Kraaaar…!*

Before the white tiger and the young man could finish shouting, I struck with both palms at lightning speed.

*Whoooosh—boom!*

Two streams of mighty palm force shot through the air, splitting apart and bursting through the rolling waves of fire.

But if I stopped there, the flames would only grow more intense. That would simply mean repeating the mistakes I had already made.

Without hesitation, I fired off one palm force after another.

*Boom! Boom!*

The reason people had difficulty putting out fires was simple.

Either they lacked enough water to extinguish the flames, or they lacked wind strong enough to snuff them out like a candle.

In the end, all they needed was more water or stronger wind.

And in this case, the latter would do.

*Boom!*

The final palm force I sent out was especially powerful.

A wind like a typhoon swept across the pasture. The livestock that had been fleeing in panic were briefly lifted from the ground, while every blade of grass and every tree was flattened.

And then…

*Whoosh.*

The flames spreading in every direction died down in an instant.

All that remained were small embers burning like a campfire and patches of pasture reduced to black ash.

And standing there, dumbfounded by the sight, were a non-Han young man and a single snow-white tiger.

“What… What is this?”

*Grrrr?*

Two pairs of eyes stared at me as if they could not believe what they were seeing.

I walked over to the last ember nearby, ground it out beneath my foot, and shrugged.

“I told you. I can do it.”

“……!”

*……!*

The non-Han young man stared at me with eyes filled with pure astonishment. Then he pointed the spear in his hand at me and asked,

“I am Yayul Mok of the Nanman Beast Palace. And you?”

As expected, he was a member of the Nanman Beast Palace.

I nodded and was just about to answer when an elderly voice suddenly rang out from behind me.

“He is Jin Taekyung of the Jin Family of Taiyuan.”

I turned around. The members of the Fire Dragon Pavilion had approached without me noticing, with Namho at the front.

“In the Central Plains, he is known as the Blazing Flame Divine Dragon, the foremost young prodigy of his generation. He is also the Pavilion Master of the Fire Dragon Pavilion, which belongs to the Murim Alliance.”

I did not know whether my name and sobriquet had reached Nanman.

But at the very least, the non-Han young man in front of me—Yayul Mok—seemed to understand the words Namho had added perfectly.

“The Murim Alliance…”

Yayul Mok murmured in a low voice and stroked the white tiger’s mane.

He quietly watched as the growling beast gradually calmed down. Then he lowered the spear pointed at me and turned around.

“Follow me. Since the Murim Alliance has been mentioned, I will let this go for now. But don’t do anything as foolish as that again.”

Namho shrugged.

“It was an accident. But I’ll keep it in mind.”

“You had better. Unless you want to die a sudden death.”

I watched Yayul Mok’s back as he rode ahead on the white tiger, then said to Namho with a sour expression,

“That kid is rude. Setting the fire was wrong, but still.”

“Hey, Han Chinese. I can hear you.”

*Grrrr.*

“I said it so you could hear me, punk.”

“What?”

“What kind of way is that to speak to an elder? Don’t you have a grandfather?”

Anger flashed across Yayul Mok’s face for a moment, but that was all.

After glaring at me once, Yayul Mok turned away again. Walking behind me, Namho gave me a flat, unimpressed look and said,

“Watch your tongue.”

“I was taking your side, Old Man Nam. Does it make any sense to tell someone who could drop dead any day that he’ll ‘die a sudden death’?”

“Since when could I drop dead any day…? Forget it. I should never have expected anything from you. Do you have some illness that’ll kill you on the spot if you go even one day without stirring up trouble?”

“Do you have some illness that makes you senile if you don’t set fire to a pasture owned by the Nanman Beast Palace?”

“……”

“Take a good look at yourself before I confiscate your walking stick for three months.”

Namho had taken a devastating loss in the exchange of insults, and he let out a sigh.

“All right. I admit it. This was clearly my mistake. It was something I had kept for more than fifty years, so I should have been more careful handling it.”

“It’s nice to see you admit it so cleanly. The pasture is still burning hot, though.”

“Every time I hear you speak, my bones start aching. But be a little careful when dealing with that young man.”

“Why?”

“Why else? Didn’t he say it himself? His name is Yayul Mok.”

“Whether he’s Yayul Mok or Yayul Mosquito, what do you want me to do about it…?”

I trailed off as I spoke.

Something forgotten in my memories felt as if it were about to come back to me.

*Yayul Mok. Yayul Mok…*

After thinking it over carefully, I turned to Ju Hwaran and asked,

“Excuse me, Young Lady Ju.”

“Yes?”

“What was the name of the Lord of the Nanman Beast Palace again?”

“Are you asking about the Beast Miao King?”

“Yes.”

The Beast Miao King, lord of the Nanman Beast Palace, was the leader of the Miao people, one of the most powerful tribes in Nanman. Regardless of his non-Han origins, he was also one of the Ten Kings, occupying the lowest position among them.

Ju Hwaran gave me a slight smile and answered in a kind voice.

“Yayul Cheok.”

“Ah. I see.”

“Yes. Yayul is his family name. It’s a rare surname that you don’t often encounter even in Nanman.”

“Then that rude little friend must be a Ya, I suppose. His name is Yulmok.”

“I’m sorry, but are you hoping that’s true?”

“Hmm. What if I am?”

Ju Hwaran had just opened her mouth to answer when the forest blocking Yayul Mok’s path far ahead of us began to shake.

*Rustle. Crackle!*

I could swear that this was the first time I had seen so many different animals gathered in one place since visiting the zoo at the age of seven.

Jaguars and tigers covered in black fur, along with leopards and even elephants.

The non-Han men and women riding various beasts spotted Yayul Mok. They hurriedly dismounted and prostrated themselves before him.

“Young Palace Lord!”

“Are you unharmed?”

“We received an urgent report that a fire had broken out. If Young Palace Lord continues acting so recklessly, the Palace Lord will be terribly worried… But who are these people?”

Dozens of pairs of eyes—human and beast alike—turned toward us.

I silently mulled over the title they had just called him, as well as my earlier question about whether he had a grandfather.

Then I slowly approached Yayul Mok, slipped an arm around his shoulders, and said,

“We’re friends. Right, Mok?”

“……”

“Hey, smile.”
## Chapter artifact 624

# Chapter 624

Ju Hwaran told me that her grandfather, the Escort King Ju Gongsan, had left these words about the Nanman Beast Palace:

> “Nanman is practically a kingdom, and the Nanman Beast Palace is a vast ranch encompassing five counties.”

The Escort King, who had once traveled throughout the Four Seas and Five Lakes and the Nine Provinces and Eight Wastes, had been right.

The territory directly ruled by the Nanman Beast Palace was truly vast, stretching across five counties. In terms of sheer area, even the Nine Sects and One Gang or the Five Great Families of the Central Plains could not compare to the Nanman Beast Palace.

*Is it a matter of direct rule versus indirect rule?*

The ruler of the Central Plains was the Son of Heaven, but in Nanman, the Nanman Beast Palace held supreme authority.

Under such circumstances, the palace might not have been able to surpass the great orthodox factions of the Central Plains in martial power, but its influence was inevitably far greater.

However, if there was one part of the Escort King’s words that was wrong…

*It isn’t a ranch. It’s a safari.*

I had never seen a place with such a chaotic mix of animals, plants, temperatures, and terrain.

Following Yayul Mok and his subordinates, we passed through grasslands and jungles, crossing mountains and rivers. Before long, I could only shake my head in disbelief.

“What the hell is wrong with this weather?”

Ju Hwaran, who was riding on my right, answered my mutter.

“One mountain holds four seasons, and ten li bring a different sky.[^1] It’s a saying that describes Nanman’s unpredictable nature quite well.”

“After experiencing it firsthand, I can’t exactly disagree. Young Lady Ju, how did you ever think of accepting an escort job to a place like this?”

“I didn’t know it would be this extreme, either. I have accompanied my father on escort journeys before, but this is my first time going so deep into Nanman.”

Ju Hwaran smiled faintly, a thick fur pelt draped over her shoulders. White breath spilled from between her lips.

Most people associated Nanman with jungles. I had thought the same, just like any other person from the Central Plains.

But this damned land had somehow crammed frigid, temperate, subtropical, and tropical climates together as neatly as apartments lined up along a hallway.

“At this point, it’s practically cursed land.”

“……Watch your mouth.”

If Ju Hwaran occupied my right, then Namho had taken the left.

The elderly Hidden Shadow Pavilion agent was sharing a black panther with one of Yayul Mok’s subordinates. Even while hunching down to avoid branches, he glared at me fiercely.

“I’m sure they’d love to hear you say that. Don’t you think?”

“So what? It’s true. And I’m speaking in Han Chinese, so they can’t understand me anyway.”

At that moment, Yayul Mok, who was riding a few dozen feet ahead of us, suddenly spoke.

“I’d prefer it if you kept that mouth of yours shut.”

“……That’s Han Chinese.”

“……Han Chinese?”

*How the hell did he pull that off?*

I felt like a cardsharp caught dealing from the bottom of the deck during a card game.

Yayul Mok spoke Han Chinese haltingly, but clearly. I exchanged a meaningful glance with Namho before asking,

“Did you study Han Chinese?”

“A little. I lost interest and quit soon afterward.”

“Oh, really? A little? And even that you quit right away?”

At my expectant question, Yayul Mok answered with a stiff expression.

“I know enough to understand it without difficulty. For example, words like ‘cursed land.’”

“…….”

“We will soon arrive, and then you can leave this cursed land. Until that time, I would appreciate it if you remained quiet.”

He had made his point so thoroughly that I had nothing to say.

As I quietly shut my mouth, Namho smiled like a sage and spoke to me.

“Well done. Very well done. Thanks to your efforts, the Nanman Beast Palace and the Murim Alliance should be able to join hands with ease.”

“You’re slipping that in so subtly. Still, you did hear some good news.”

“It’s good news for Dark Heaven. The Murim Alliance’s foremost young prodigy came here to propose an alliance, asked the Young Palace Lord of the Nanman Beast Palace whether he had a grandfather, and called Nanman a cursed land. Come to think of it, are you perhaps a member of Dark Heaven?”

“Do I look like a member of Dark Heaven?”

“No. But I have to admit, I’m beginning to have my doubts. Enough nonsense. Tell me about this good news I supposedly don’t know.”

I answered confidently.

“They say we’ll be arriving at the Nanman Beast Palace soon.”

“God damn it…”

“Hey, don’t swear.”

“Do I look like I can help swearing right now? That A-Gwi bastard they call Taishan—or Geumsugangsan or whatever his name is—is one problem, but in my opinion, you’re no less troublesome, Pavilion Master. You’re already acting like this before we arrive. What are you going to do if your particular brand of insanity flares up when you actually come face-to-face with the Beast Miao King?”

“‘Insanity’ is a bit harsh. I may look like I act without thinking, but I know where to put my feet before I stretch out my legs. And Taishan may be lacking in certain areas, but he’s a major asset. When the time comes, he’ll pull his weight. You don’t need to worry so much.”

At that moment, a mournful animal cry and a frantic shout rang out from behind us.

“Grrrrrrr!”

“Y-Young Palace Lord! This huge Han bastard is biting my bear’s ear off!”

“Taishan! Bear meat!”

“Captain!”

“Taishan! Stop! Stop eating!”

“Seize that Han bastard immediately!”

I briefly turned my head to check what was happening behind us as we rode, then added one more comment to Namho.

“Of course, his appetite is a problem.”

“For fuck’s sake. There’s appetite, and then there’s appetite. Is that thing a beast or a person?”

I could not deny it.

Lately, I had begun to wonder whether Taishan was some unknown creature hovering somewhere between human and beast.

*Fire Dragon Pavilion. Are we really going to be all right like this?*

Taishan was munching contentedly on the ear of the bear he had been riding, while Sama Pyo tried to stop his subordinate’s animal abuse.

The bear, meanwhile, howled in pain and expressed its refusal to carry passengers with every inch of its body.

As I watched the scene, Yayul Mok spoke with a sigh.

“We’re here. For the love of all that’s holy, stop it and get down this instant.”

He was telling the truth.

The chill that had lingered in the air had vanished without a trace. In its place was humid, oppressive heat, along with a dense tropical rainforest waiting for us.

And beyond it…

*Rumble, rumble.*

An iron gate covered in vines and tree trunks opened, revealing countless pavilions and houses.

This was one glimpse of the Nanman Beast Palace, which had built a kingdom of its own in Nanman, tens of thousands of li from the Central Plains—and in the deepest, most secluded part of that land.

* * *

Any family or sect of a certain size, including the Jin Family of Taiyuan, generally divided its organization into an Outer Hall and an Inner Hall.

They built an organizational structure both inside and outside their main grounds, creating their own lines of defense in preparation for an attack by their enemies.

However, the Outer Hall of the Nanman Beast Palace now before my eyes far exceeded the scale of any ordinary sect.

*This is practically a city.*

The Escort King had not called it practically a kingdom for no reason.

Unusual houses and countless buildings unlike anything commonly seen in the Central Plains caught my attention.

A market appeared to be in full swing on one side, with people haggling energetically. Nearby, children who looked to be six or seven years old laughed and ran around with young beasts.

There were countless people and buildings, along with all kinds of commerce and manufacturing.

The scene looked like the capital of a small nation, and Hyuk Mujin’s mouth hung open in amazement.

“Wow. I thought I had seen and experienced quite a lot, but this place is truly beyond my imagination. Captain, do you see that? It’s amazing.”

“It is. But there’s something even more amazing. Want to know what it is?”

Hyuk Mujin, who had been looking around frantically, asked,

“What’s the most amazing thing?”

“Us.”

“Ah.”

“Now that you’ve gotten the idea, shut your mouth and stop gawking. We’re already attracting enough attention.”

Judging by the settlement immediately visible before us and its sheer size, the Outer Hall alone probably contained several thousand households.

Moreover, the Nanman Beast Palace was located in the deepest part of Nanman, and outsiders were strictly forbidden from entering. Naturally, we stood out like a handful of pebbles among them.

There were probably quite a few people seeing Han Chinese for the first time.

Making a fuss under these circumstances would not do us any good. Especially not in an atmosphere like this.

“Are those Han Chinese? They look similar to us, but kind of strange.”

“Shh. Don’t even make eye contact. Didn’t you hear what happened in the northern lands recently? Apparently, a bunch of Han Chinese slaughtered an entire Miao village. Those men might be part of the same group.”

“Of course I heard about it. But what could those bastards possibly do here? They look like the Young Palace Lord captured them.”

“I don’t think they look like prisoners… Either way, what could possibly have brought Han Chinese all the way here?”

Their languages varied just as much as their appearances and clothing.

Ju Hwaran, Namho, and I were able to understand what they were saying, so we spoke quietly among ourselves.

“Looks like the rumors have already spread.”

“I can understand only the Miao and Bai languages, but even so, the atmosphere here seems tense.”

“It happened only a few days ago. Conflicts between tribes occur dozens of times a year, but an incident caused by outsiders might happen once in a decade, if that. Of course the rumors spread quickly.”

If we had built up a good reputation, we might have been welcomed wherever we went. But the massacre of the Miao village about a month earlier had produced the exact opposite result.

Hyuk Mujin hunched down tactfully and grumbled.

“Those lunatics. The Heavenly Demon Escort Bureau, or whatever they were called. Why did they have to commit such an atrocious crime in Nanman of all places…?”

“I wonder. Why did they?”

Sama Pyo suddenly spoke, continuing in an amused tone.

“We need to think harder about why something like that happened now, of all times. I imagine that fellow has been thinking along the same lines as I have. Isn’t that right?”

Song Ilseom answered calmly.

“Yes, but no.”

“……What does ‘yes, but no’ mean?”

“It means that regardless of what I think, I don’t want to exchange words with you. So don’t talk to me.”

“You’re more petty than you look. Well, if that’s how it is.”

Sama Pyo raised one eyebrow slightly after my warning gaze met his, then took a step back first.

But regardless of the feud between those two, the question Sama Pyo had raised was one I had also been carrying with me throughout the journey.

*The Heavenly Demon Escort Bureau.*

Whether by coincidence or design, the timing of the tragedy was extremely suspicious.

It was still too early to jump to conclusions about the answer.

*Still, does this mean we’ve managed to avoid the worst-case scenario?*

To be honest, I had been somewhat worried before meeting Yayul Mok.

No. I had been very worried.

I had feared that Dark Heaven’s scheme had already begun and that Nanman Beast Palace had become a living hell.

Of course, our image as Han Chinese had plummeted to the level of a pro-Japanese corporation, but the mere fact that nothing had happened yet was more than enough.

*Even if we have to take some abuse, this is much better.*

I was muttering inwardly when I suddenly raised my head.

A strange sense of déjà vu had come over me.

*This is…*

Others might not have noticed it, but I could feel it.

The flow of the air had grown heavy so naturally that no one could detect the change.

Beyond the countless noises and signs of people nearby, someone’s aura was pouring out roughly.

My gaze followed that aura, eventually reaching an old man seated on the vine-covered steps.

His upper body was completely bare, revealing a massive, muscular frame.

I realized who he was before he even opened his mouth.

*The Beast Miao King.*

It was him.

[^1]: A traditional saying describing Nanman’s rapid shifts in climate and weather.

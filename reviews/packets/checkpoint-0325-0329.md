# Checkpoint Review — 325–329

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

# Chapters 325–329

## Plot

Jin Taekyung defeats and severely injures Hwangbo Eom after Hwangbo attacks first. Hyuk Sopyung restrains the Taeeul Sword Unit, acknowledges Zhongnan’s manipulation of the Yongbong Escort Bureau, apologizes, and asks Taekyung to spare Hwangbo. Under pressure, Hwangbo agrees that Zhongnan will void its contracts with the bureau and pay four hundred thousand silver nyang.

Ju Hwaran and Taekyung identify Chief Escort Heo Jun as the traitor behind the bureau’s two-year failures. Heo Jun accepted bribes from Zhongnan, drugged the escorts, stole and replaced the Thousand-Year Snow Ginseng, and fabricated mistakes to conceal the sabotage. Hwaran kills him after rejecting his claim that betrayal was merely a mistake.

Song Ilseom reveals that he is Song Pyosan’s son and that his grandmother was the surviving child of the Guangdong Chen Family rescued by Ju Gongsan. He became the Soul-Chasing Guest after surviving as a sword boy and won 102 life-and-death duels. The family’s martial arts were lost when the Guangdong Chen Family was destroyed.

Taekyung’s party departs for Sichuan after receiving a Hundred-Year-Old Snow Ginseng from Hwaran. Taekyung comforts Hwaran over her fear of failing as Young Bureau Head, then reveals that he already possesses the Thousand-Year Snow Ginseng. The party continues toward the Divine Physician with Jeok Cheongang unconscious on a pack frame.

## Continuity

- Hwangbo Eom survived but is critically injured and requires at least a year of recuperation. His sword was destroyed, and he signed the compensation agreement under duress.
- Zhongnan has accepted responsibility for the Yongbong Escort Bureau’s manipulated failures, voided its contracts with the bureau except for the compensation payment, and has not yet identified all conspirators or explained the broader scheme.
- Heo Jun is dead. He was the bureau’s two-year traitor and was responsible for the mind-clouding drug, the Thousand-Year Snow Ginseng substitution, and related sabotage.
- Hyuk Sopyung publicly apologized on Zhongnan’s behalf and is expected to report the incident to the Sect Leader and Elders.
- Song Ilseom is Song Pyosan’s son, the former Soul-Chasing Guest, and a descendant of the Guangdong Chen Family through his grandmother. His faded jade hairpin preserves the family connection.
- Ju Hwaran remains the Yongbong Escort Bureau’s Young Bureau Head and gave Taekyung a Hundred-Year-Old Snow Ginseng.
- Taekyung possesses the Thousand-Year Snow Ginseng and remains publicly identified as the Fire Gate Clan’s nineteenth successor, with the Flamefire Path at seven stars.
- Taekyung’s party has left the Yongbong Escort Bureau for Sichuan. Jeok Cheongang remains unconscious in a suspended-animation-like state beneath leather on the pack frame.
- The party must locate the Divine Physician and obtain treatment for Jeok Cheongang within his remaining six-to-eight-month treatment window.
- Unresolved hooks include the identity of the people seeking the Guangdong Chen Family’s Peak martial arts, the fate of the other Chen Family members, Song Ilseom’s impact on the Murim, Zhongnan’s internal response, and the consequences of Hwangbo’s defeat and Heo Jun’s betrayal.

## Translation Decisions

- Use **Taeeul Sword Unit**, **Taeeul Merciless Sword**, **Taeeul Light-Dividing Sword**, **Taeeul Formless Sword**, **Tengwang Pavilion**, **Flamefire Path**, **Heavenly Strike**, and **Fire Gate Clan**.
- Use **Senior Martial Uncle** for 황천’s 사백님 and **Martial Grandmaster** for the Taeeul Sword Unit’s 사조님.
- Use **Dagger Hidden Flower** for 은비화, **Junzi Sword** for 군자검, **mind-clouding drug** for 몽혼제, and **a needle in a bag** for 낭중지추.
- Use **Soul-Chasing Guest** for 추혼객, **sword boy** for 검동, **Rain of Ten Thousand Flowers** for 만천화우, and **Ten-Thousand-Mile Escorts** for 만리표.
- Use **Captain Song**, **Young Bureau Head**, **Great Hero Jin**, and **Young Hero Song** for the established forms of address.
- Use **Lady** in Taekyung’s joking sobriquet for Kim Jeonghee.

## Durable state

{
  "active_continuity": [
    "Song Ilseom is Song Pyosan’s son and was known ten years earlier as the Soul-Chasing Guest; he has won 102 life-and-death duels.",
    "Song Ilseom’s grandmother was the surviving child of the Guangdong Chen Family rescued by Ju Gongsan; she fled with infant Song Pyosan, gave Song Ilseom the jade hairpin and family history, and died when he was ten.",
    "The Guangdong Chen Family’s martial arts were lost when the family was burned, and Song Ilseom developed his ability through battlefield experience after working as a sword boy.",
    "Ju Hwaran remains the Yongbong Escort Bureau’s Young Bureau Head and is still burdened by responsibility for its losses and future.",
    "Ju Hwaran gave Taekyung a Hundred-Year-Old Snow Ginseng, which he accepted.",
    "Taekyung’s party has departed the Yongbong Escort Bureau for Sichuan with Jeok Cheongang unconscious on a pack frame.",
    "Taekyung possesses the Thousand-Year Snow Ginseng and had forgotten to place it in his inventory.",
    "Taekyung must find the Divine Physician in Sichuan within Jeok Cheongang’s remaining treatment window.",
    "The Zhongnan Sect’s other conspirators and the organizers behind the broader scheme remain unidentified."
  ],
  "continuity_sources": [
    329
  ],
  "open_questions": [
    "Who sought the Guangdong Chen Family’s Peak martial arts, and what happened to the other members of the family?",
    "How will Song Ilseom’s Guangdong Chen lineage affect the Yongbong Escort Bureau and the wider Murim?",
    "How will the Zhongnan Sect’s Sect Leader and Elders respond to the exposed scheme and settlement?",
    "What consequences will Hwangbo Eom’s defeat, Heo Jun’s betrayal, and Zhongnan’s coercion cause within the Murim?",
    "Where is the Divine Physician in Sichuan, and can Jeok Cheongang be treated within the remaining window?"
  ],
  "safe_through": 329,
  "temporary_decisions": [
    "Use Captain Song for 송 표두.",
    "Use Great Hero Jin for 진 대협 when Ju Hwaran addresses Taekyung.",
    "Use Lady for 여사 in Taekyung’s joking sobriquet for Kim Jeonghee.",
    "Render 추혼객 as Soul-Chasing Guest and 검동 as sword boy.",
    "Render 만천화우 as Rain of Ten Thousand Flowers and 만리표 as Ten-Thousand-Mile Escorts."
  ],
  "version": 1
}

## Reading copies

## Chapter artifact 325

# Chapter 325

A shudder.

That was the emotion everyone present shared.

Huashan, the Beggars’ Sect, the Zhongnan Sect, the Lower District Sect, and even the Yongbong Escort Bureau. Dozens of trembling pairs of eyes stared dumbfoundedly at the scene unfolding before them.

“So.”

Thwack!

“While I was still asking nicely.”

Thwack!

“You should’ve stopped.”

Thwack!

“And where do you get off throwing the first punch—the first sword, even?”

Craack!

The final blow was especially loud. With a wet, choking rattle of blood in his throat, the old man’s body crumpled to the ground.

His face was covered in blood. The sharp bridge of his nose, which had once made countless women’s hearts flutter, had long since been flattened, and the even teeth that had belied his eighty years of age had been reduced to a single front tooth.

“You talk shit about someone else’s Master like you’re insulting their fucking dad, you piece of shit.”

Craack!

The last remaining front tooth went flying through the air and landed in a corner of the tea house.

As they stared at the scene in stunned disbelief, one thought flashed through everyone’s mind.

*What the hell am I looking at?*

Something no one had thought would happen—something that should never have happened—was happening right before their eyes.

Who would believe that a young man barely twenty years old, only just beginning to make a name for himself in the martial world, was brutally beating the Zhongnan Sect’s greatest master and the Sect Leader’s senior brother?

And yet everyone present had witnessed it with their own eyes.

The exchange between two men whose movements had been too fast to follow. And at the end of that exchange, the fallen old man and the young man standing alone.

“The fire dragon…”

Someone muttered those two words like a groan, and they sank deep into the hearts of all who heard them.

The Sleeping Dragon of Shanxi. That was the martial name by which the young man Jin Taekyung had been known in the Murim.

But that was wrong. The Hidden Dragon had finally risen, and he would soar through the skies of the entire world—not merely those of Shanxi.

As a fire dragon.

“The only subject I ever got a perfect score in was ethics. But today, I’m making an exception and attacking an old man properly. Get up.”

No. Not a fire dragon.

Was he a Mad Dragon instead?

The sight of Jin Taekyung gripping Hwangbo Eom’s beard, which was a filthy mess of soot and blood, as though it were a fistful of hair jolted the thirty members of the Taeeul Sword Unit out of their stupor.

Who was that old man?

He was Taeeul Merciless Sword Hwangbo Eom, a senior of their sect and the Sect Leader’s senior martial brother.

“W-wait!”

“Martial Grandmaster!”

The voices erupted all at once, as if they had been rehearsed.

Among them was one particularly loud shout, filled with force.

“You bastard! Release Senior Martial Uncle this instant!”

Hwangcheon[^1], the Commander of the Taeeul Sword Unit and a second-generation disciple of the Zhongnan Sect, hurriedly drew his sword and stepped forward.

[^1]: Hwangcheon (黃泉) literally means “Yellow Springs,” a traditional term for the underworld.

Shing. Clack.

“……!”

Hwangcheon’s eyes widened like saucers.

It had happened in the blink of an eye.

A cold blade had stopped at his throat. A yellow bamboo staff was pressed against his chest, while the blade he had drawn halfway from its scabbard had been caught on someone else’s sword and could not be drawn any farther.

The three martial artists who had subdued Hwangcheon, a Peak master of the Zhongnan Sect, in an instant spoke in turn.

“You’d better not draw that sword.”

“If you want a fight, the Yongbong Escort Bureau and I will be your opponents.”

“It’ll hurt quite a bit if you get hit by the Dog-Beating Staff Technique. I’ve only mastered it to five stars, though.”

Huashan’s Lone Crane Baek Museong, Dagger Hidden Flower Ju Hwaran, and the Beggars’ Sect’s Successor Beggar, Gung Gibang.

And that was not all.

“Protect the Young Bureau Head!”

“This is troublesome. We’re almost done here, so it would be a problem if things ended like this.”

Chief Escort Heo Jun and the cold-faced Song Ilseom, who had been muttering something incomprehensible, led the Yongbong Escort Bureau’s escorts in confronting the Zhongnan disciples.

“The branch leader commands you filthy Beggars’ Sect bastards! Show those dogs who are beneath even a yellow dog what a beggar’s cudgel feels like!”

“We’re both beggars. Why are you calling us bastards?”

“Good grief. It’s been ages since I got to really cut loose.”

“If any of you get hurt, it’s the branch leader’s responsibility. Don’t hassle us just because we can’t beg for a while.”

Heukgeol Beggar and the Beggars’ Sect disciples drew the cudgels hanging from their waists with considerable enthusiasm.

“You lot, don’t get involved and hurt yourselves for no reason. Write down every detail of what happens. We’ll be able to sell it for a high price later.”

“Um, are you planning to make an enemy of the Zhongnan Sect?”

“Hm? Why would I make an enemy of an important customer? I’m going to sell this to the Zhongnan Sect. Even if I jack up the price sky-high, they’ll have no choice but to buy it.”

“Ah! Of course!”

“Draw pictures, too. Make them vivid enough to leap off the page.”

“Yes, ma’am!”

Wolhwa and the Lower District Sect members, who were hoping to make a fortune, began recording the scene before them in words and pictures without missing a single detail.

“Wow! This is the first time I’ve seen anything like this in my life!”

“You bastards! Hyuk Mujin is here too—the Vice Squad Leader of the Jin Dragon Squad and the Captain’s right-hand man!”

Finally, even Cheongpung and Hyuk Mujin, who had been standing a step away and watching the fire from across the river, joined in.

As events took an unexpected turn, Hwangcheon’s face flushed with confusion and rage.

“W-what is the meaning of this? Everyone, stop this at once!”

The answer came from somewhere else.

“What if we don’t want to stop?”

“……!”

Hwangcheon sucked in a breath.

Over the shoulders of the people blocking the Zhongnan Sect’s path, a pair of eyes filled with cold flames stared directly at him.

“I asked you. What are you going to do if I don’t want to stop?”

White steam escaped from Jin Taekyung’s lips as he sneered.

Was it because he had witnessed that unbelievable display of power? Merely meeting Jin Taekyung’s gaze and hearing his low voice bore into his ears was enough to make Hwangcheon’s breath catch.

His aura was truly overwhelming.

*H-How can someone so young…?*

Hwangcheon realized it once again.

To the young man who had defeated the greatest master of the Zhongnan Sect, age was nothing more than a number.

*He’s a monster. That man is a monster.*

And that monster was looking directly at him.

How could the martial arts he had once been so proud of feel this insignificant?

Hwangcheon swallowed dryly again and again as Jin Taekyung’s aura pressed down on him.

That was when—

“Junior Brother, withdraw. Everyone else, sheathe your swords.”

A calm voice accompanied the back of a man who stepped in front of them.

Hwangcheon’s eyes widened at the familiar figure.

“Senior Brother Hyuk…!”

Zhongnan One Dragon Hyuk Sopyung.

He had been called the future of the Zhongnan Sect, and even now, despite his indulgence in wine and women, he had not lost his reputation as the sect’s greatest young prodigy.

Standing before Hwangcheon, he stared at Jin Taekyung with firm eyes.

Though dozens of weapons were pointed at him, his voice did not waver in the slightest.

“Please stop this meaningless fight.”

“Meaningless? Stop it?”

A short, breathy laugh escaped through Jin Taekyung’s lips.

“Even if you started it, I’m the one who decides how it ends.”

“I know. That is why I’m asking.”

“You’re asking? Just because you have a mouth doesn’t mean you can say whatever you want. You might end up with that mouth actually being pierced.”

“The victor is already clear. I’m asking you to show the magnanimity of the stronger party.”

The Zhongnan disciples’ eyes widened—not at his surprisingly courteous manner or voice, but at the meaning of his words.

Hwangcheon, who had remained silent behind Hyuk Sopyung, raised his head and shouted.

“Senior Brother! The magnanimity of the stronger party? That would damage Senior Martial Uncle’s and the Great Zhongnan Sect’s reputation—”

“Junior Brother.”

“Y-yes?”

Hyuk Sopyung cut him off in a gentle voice.

But his next words were as sharp as a drawn blade.

“Will you shut that mouth of yours?”

“……Senior Brother?”

Not only Hwangcheon, but all thirty members of the Taeeul Sword Unit stared at Hyuk Sopyung with blank expressions.

Receiving all of his junior disciples’ stunned gazes, Hyuk Sopyung slowly opened his mouth.

“Anyone who wasn’t blind would have seen it. Anyone who wasn’t deaf would have heard it—how all of this began.”

“…….”

“We plotted in the shadows to swallow the Yongbong Escort Bureau whole. That is not the conduct of a great orthodox sect. Therefore, our sect has already lost its dignity.”

His voice was low, and his expression was twisted with pain. But Hyuk Sopyung did not stop.

“Worse, even in the face of such clear evidence, we refused to admit our wrongdoing, harbored murderous intent, and swung our swords. That severed the last shred of trust our sect still possessed. And yet which one of us dares speak of reputation? Me, who forgot my duty and floundered in wine and women? Or you, who refuse to admit your mistakes and cling only to your pride?”

Hwangcheon lowered his head.

He was not the only one. All thirty Zhongnan disciples fell silent, gripping the scabbards at their waists so tightly that their knuckles turned white.

They were ashamed because everything Hyuk Sopyung had said was true. And as the pride they had held in their sect crumbled, they felt hollow and humiliated.

No one spoke, but the emotions they felt were vividly conveyed to everyone around them.

“At least today… we were not the Great Zhongnan Sect.”

With those final words, Hyuk Sopyung looked at his junior disciples with eyes filled with regret, then turned around.

He took a deep martial salute toward the one man who had silently waited for him to finish speaking.

“This Zhongnan disciple, Hyuk Sopyung, humbly asks this of you. We deeply regret and apologize for the wrongs our sect has committed. Please show mercy just this once and spare him.”

His manner was exceedingly respectful, as though he were addressing a legendary master of the martial world.

And yet the person receiving his salute was a barely grown young man.

After staring silently at the bowed Hyuk Sopyung for a moment, Jin Taekyung opened his mouth.

“It leaves a bad taste in my mouth to keep an old bastard like this alive… but fine. I’ll let him off this once.”

Before Hyuk Sopyung could even raise his head, Jin Taekyung continued brightly.

“After I hit him one more time.”

Craack!

* * *

The inside of Tengwang Pavilion was beyond ruined.

The roof had collapsed completely, and all the furnishings had been reduced to splinters by the battle between Hwangbo Eom and me. Cold wind and the murmuring of onlookers drifted in through the collapsed walls.

“My heavens, Tengwang Pavilion…”

“What on earth happened? Does anyone know?”

“I don’t know the details either. But from what I’ve heard, about one shichen ago, Taeeul Merciless Sword of the Zhongnan Sect led his disciples…”

Xi’an was the center of Shaanxi Province. No matter how far from the main streets Tengwang Pavilion had been, it could not escape the people’s attention.

And the commoners who had gathered out of equal parts curiosity and concern were forced to face dozens of sharp martial artists’ gazes.

“That’s far enough.”

“This is a matter of the martial world. Don’t get involved. Go back!”

Dozens of armed martial artists formed a wall of people to block their approach. The commoners hesitated, then slowly backed away.

I clicked my tongue as I watched the Zhongnan disciples struggling desperately to keep the scene inside from being exposed.

“You’re really trying. Really.”

The Great Zhongnan Sect’s reputation had already been destroyed, yet they were still struggling to preserve even a shred of it.

It was both pitiful and idiotic.

I dropped into a wooden chair with a broken back and opened my mouth.

“Well, unpleasant things happened, but we still have to finish what needs finishing. Let’s find some common ground through dialogue instead of barbaric violence.”

“…….”

“…….”

Oof. Those stares were sharp.

I ignored the gazes raining down on me from every direction and smiled at one person.

“So, Great Hero Hwangbo, what do you think?”

Hwangbo Eom answered immediately.

Or rather, he groaned.

“Hrrgh… hrrrgh…”

Both of his arms were broken, and one leg was fractured. On top of that, he had suffered an Internal Injury that would require at least a year of recovery, while his nose and teeth had been smashed to pieces.

A sobbing groan escaped from his slightly open mouth, accompanied by the wet rattle of blood and phlegm.

“Hrrrgh…”

I grabbed Hwangbo Eom by the wrist.

Resisting the urge to break it, I sent a small amount of internal energy into him. The pallor of his face improved slightly.

“Patient, patient, wake up. It’s time for your injection—no, your negotiation.”

“Hrrgh… Jin Taekyung. You…”

“That catchphrase went out of fashion fifty years ago.”

“You bastard. Do you think our sect will let you get away with this…?”

“Hm.”

*What do I do? He still doesn’t seem to have come to his senses.*

I scratched the back of my head, then whipped my hand out like lightning.

Smack!

“Guh!”

Hwangbo Eom’s eyes rolled back after the slap.

As he trembled all over and began to slide out of the chair, Hyuk Sopyung caught him and sighed.

“Whew.”

“It’s not my fault. He keeps earning these beatings. He’s practically begging me to kill him. What else am I supposed to do?”

“Even so, restrain yourself. Any more than this could endanger his life.”

“You’ve had a rough time, too. Judging by his personality, I can’t imagine he treated you particularly well either. Am I wrong?”

“……What kind of person he was to me is irrelevant. He is my Master’s senior martial brother, and a disciple of our sect.”

The complicated expression on Hyuk Sopyung’s face suggested that there was some story between them.

*He seems surprisingly decent, considering. Was that why he used to drink and cause disturbances?*

The question crossed my mind for an instant, but I had no intention of asking.

I was not particularly curious, either.

There was something more important to deal with now.

“All right, then. Let’s negotiate. Young Lady Ju, are you ready?”

“Pardon? Y-yes, yes.”

“You may state your demands.”

*What on earth happened here? Is this a dream?*

Still looking as though she could not quite believe what was happening, Ju Hwaran rubbed her flushed cheek and began to speak.

“As compensation for this incident, the Yongbong Escort Bureau demands that the Zhongnan Sect void the contract and pay the contractual penalty—”

Hwangbo Eom’s hoarse voice cut her off.

“We refuse. Our sect will not pay any compensation.”

I knew it.

I gestured toward Ju Hwaran, who had gone rigid.

“Young Lady Ju, wait a moment.”

“Yes?”

“It’ll only take a second.”

Without hesitation, I slapped Hwangbo Eom across the face.

Smack!

“Guh!”

“Senior Martial Uncle!”

“I’ll ask again. Are you paying compensation or not?”

Hwangbo Eom glared at me with burning eyes.

“Our sect will… not pay any compen—”

Smack!

“Guh! No compensation whatsoever.”

Smack!

“Guhhh! Our sect will pay any compensation!”

“Okay, compensation! Okay! Thank you!”

Negotiation sure was easy.
## Chapter artifact 326

# Chapter 326

The negotiations went smoothly.

“To begin with, looking only at the year before last, the Yongbong Escort Bureau suffered losses amounting to twenty-five thousand silver nyang because of the Zhongnan Sect’s schemes. Do you acknowledge that?”

“Twenty-five thousand silver nyang? What nonsense! This old man absolutely does not acknow—”

“Ha. This old bastard’s starting again.”

Smack!

“Guh! I acknowledge it! I acknowledge it!”

Of course, there were times when things did not go smoothly. But all that mattered was making them go smoothly.

The Beggars’ Sect organized the mountain of information they had gathered, and the Lower District Sect used it to calculate the losses on their abacuses.

“Let’s see. The contract cancellation with the Nakcheon Merchant Guild on the seventeenth day of the first month last year. The Zhongnan Sect was involved in this one, too.”

“How much were the damages?”

“Six hundred and thirty-two silver nyang.”

I had been quietly listening to the Beggars’ Sect disciple and Lower District Sect member talk when I suddenly spoke up.

“Seven hundred nyang.”

“Pardon?”

“Seven hundred nyang.”

“……Yes.”

The middle-aged Lower District Sect member, clearly seasoned in financial dealings, hastily crossed out the character for six and changed it to seven.

As I watched them work, I suddenly picked up one of the bamboo slips that had been set aside.

“What’s this?”

“Ah, that was something that happened on the sixth day of the fifth month last year…”

“Skip the date. How much were the damages?”

“Nine hundred and twenty-six silver nyang.”

“Nine hundred and what?”

The Lower District Sect member quickly corrected himself when he saw my expression.

“One thousand nyang.”

“One thousand nyang? They really bled us dry. There isn’t a single place they didn’t stick their noses into.”

Two silver nyang was enough to cover a family of four’s living expenses for a month. Income inequality might have been severe, but one thousand silver nyang was enough for an ordinary commoner’s family to live in luxury for three generations.

As I marveled at the sum, the Lower District Sect member spoke up.

“Um, Young Hero Jin. That incident was not caused by the Zhongnan Sect.”

“It wasn’t? Then why is it here?”

“Well, you see, Young Master Jin…”

A long, slender finger poked my forearm. It belonged to Wolhwa, who had been standing behind me this entire time, giving off a strange fragrance.

“We brought every piece of information that seemed even slightly suspicious. When we compared everyone’s records, quite a few turned out not to have been Zhongnan’s doing. Young Lady Ju, the Young Bureau Head, would know that well.”

“Oh, really?”

Ju Hwaran was already examining the bamboo slip. After quickly scanning its contents, she nodded.

“That’s right. I remember this one clearly because the loss was so great. This escort mission failed because of a mistake on our side. Isn’t that right, Uncle Heo?”

Under everyone’s gaze, Chief Escort Heo Jun cleared his throat before answering.

“That’s correct. I personally took charge of the escort, and Chief Escort Song here accompanied me. Unfortunately, several misfortunes happened at once, and we failed to meet the deadline. In the end, we had to pay a contractual penalty of one thousand silver nyang.”

His face was filled with shame.

But I did not miss the suspicious look Heo Jun shot at Song Ilseom when he discreetly turned his head.

Nor did I miss Song Ilseom, standing far away with his back against the wall as though he had nothing whatsoever to do with the matter.

“Hmm.”

“What is it, Young Master Jin? Is something wrong?”

“No. Let’s move on.”

“All right, then. We’ll set this one aside separately.”

At that moment, someone’s hand blocked Wolhwa’s pale, slender fingers as they reached for the bamboo slip.

It was not a woman’s hand, but the rough hand of a martial artist.

Its owner was Ju Hwaran.

“Wait a moment.”

“Yes, Young Lady?”

“I’ve thought it over carefully, and I think this was probably the Zhongnan Sect’s doing after all.”

“……What?”

“……Huh?”

While everyone stared at her in confusion, Ju Hwaran paid them no attention. She picked up the bamboo slip and smoothly handed it to the Lower District Sect member who was calculating the damages.

“Add this one, too.”

“Y-Young Lady Ju.”

*I feel like I’ve seen this scene somewhere before.*

The Lower District Sect member glanced between Wolhwa and me, squeezed his eyes shut, and moved his brush.

With just a few strokes, Ju Hwaran added the hefty sum of one thousand silver nyang. Then she picked up another bamboo slip.

“All right, shall we take another look at the others?”

“……”

“……”

“This one, too. And that one. Oh, hand me the one over in the corner. Yes, that one.”

Ju Hwaran examined the bamboo slips and checked the amounts with lightning speed. Every time she did, the damages multiplied like a litter of rabbits.

The calculations taking place in her head were precise, and her fraud was audacious.

“This part seems suspicious, too.”

“Um, that was determined to have been a mistake by Chief Escort Heo Jun.”

“No. It was the Zhongnan Sect’s doing. Add it.”

“Th-then we’ll add another one hundred and fifty silver nyang…”

I let out a quiet laugh and spoke up.

“Two hundred silver nyang.”

“Pardon?”

“Let’s make it two hundred nyang.”

Ju Hwaran shook her head.

“Three hundred nyang.”

“……”

“……”

*She called it and doubled the amount. Talk about bold.*

Hwangbo Eom, who had already given up halfway, cried out in a blood-choked voice.

“I-I’ve never seen a pair of highway robbers like you!”

*A pair of highway robbers?*

Hwangbo Eom seemed intent on eating food set out for the dead starting tonight.

I was just about to start preparing the funeral rites when—

“Did you just call us highway robbers?”

Ju Hwaran stared at Hwangbo Eom with an icy expression I had never seen on her before.

“Our Yongbong Escort Bureau is demanding what we are rightfully owed. If you refuse even that… then I will let the whole world know who the real highway robber is.”

“How dare you…”

“If every one of these facts is revealed in full, will the disciples of the Zhongnan Sect still be able to show their faces in public?”

Ju Hwaran had been forced to lead the Yongbong Escort Bureau at an age barely shy of twenty, after her father collapsed from qi deviation.

She had lost so much because of the Zhongnan Sect’s schemes, and the grief of those she had been forced to send off had sunk deep into her heart.

“Escort Captain Seok Domin, escorts Gil Wangjun, Hong Seokjeong, and Noh Dusam, and caravan porter Seok Sam…”

She recited the names of people whose identities I did not know in a trembling voice, then glared at Hwangbo Eom with tear-filled eyes.

“Thirty-three in total. These are the people who lost their lives on this escort mission. Every one of them was family to the Yongbong Escort Bureau. Even when the bureau’s finances deteriorated so badly that we could no longer pay them properly, they stayed with us until the very end.”

They had not shared blood, but they had been like family.

Just as I had lost my former teammates, Ju Hwaran had lost people precious to her—people who had believed in her and followed her.

“Do not expect us to make any concessions. And neither I nor anyone else in the Yongbong Escort Bureau will ever forget this.”

“……!”

“Do you have anything else to say, Great Hero Hwangbo of the Great Zhongnan Sect?”

His tightly clenched fist trembled. Hwangbo Eom closed his eyes instead of answering.

Hyuk Sopyung stepped forward and gave Ju Hwaran a martial salute on his behalf.

“On behalf of our sect, I offer you our apologies, Young Lady Ju.”

“Please call me Young Bureau Head. And I will not accept an apology that consists only of words.”

At her blade-sharp reply, Hyuk Sopyung sighed.

“Of course not. I will immediately report this to my Master and the other Elders, who are still unaware of what happened.”

“I sincerely hope they were unaware.”

I did not know what sort of person the Zhongnan Sect Leader, Wind-and-Cloud Sword Lord, was.

But the former Sect Leader, whom Jeok Cheongang had described as “quite the Daoist,” had personally named him as his successor. I could only hope that meant he was someone who could be reasoned with.

*The Yongbong Escort Bureau’s situation is one thing, and my own situation is another.*

As the old saying goes, a crayfish sides with a crab, and an arm bends inward.[^1]

I had killed too many enemies to count, but Hwangbo Eom was not merely one martial artist.

The name Taeeul Merciless Sword represented the Zhongnan Sect, and on a personal level, he was also the Sect Leader’s Senior Brother.

*I could eliminate him if I wanted to… but what comes after that is the problem.*

The Zhongnan Sect was powerful enough to belong to the Nine Sects and One Gang.

If I had cut off Hwangbo Eom’s head, would they have simply stood by and watched?

Hyuk Sopyung, who had tried to stop me, and everyone else here must have guessed the same thing deep down: that I would not kill Hwangbo Eom.

*Should I be satisfied with leaving him half-crippled?*

It left a bitter taste in my mouth, but there was nothing I could do.

Hwangbo Eom would need at least a year of recuperation to recover from the injuries he had suffered today.

The important thing was that he was still alive—and by the time he recovered, I would be even stronger.

*Since they were kind enough to shit all over themselves first, things became much easier.*

Hwangbo Eom had made two critical mistakes. The first was drawing his sword. The second was ordering the Taeeul Sword Unit to seal off the pavilion.

Drawing his sword was one thing, but the second mistake had been fatal.

*Because it dragged not only the Beggars’ Sect and the Lower District Sect into this, but Huashan as well.*

The Zhongnan Sect’s position would become even more precarious because of this incident—not only in the Murim, but financially as well.

The final number written on the bamboo slip after all the calculations were complete proved it.

“For the material and human losses suffered by our bureau, along with the enormous contractual penalty we would have owed your sect if this escort mission had failed… the total comes to four hundred thousand silver nyang. The Zhongnan Sect’s finances should be able to handle that much, shouldn’t they?”

Ju Hwaran’s voice was calm, but the same could not be said of the people listening to her.

Gung Gibang dropped the bamboo staff he had been holding in shock, while Wolhwa clicked her tongue and whispered to me.

“Young Lady Ju—no, the Young Bureau Head of the Yongbong Escort Bureau—is something else, isn’t she?”

“How large an amount is four hundred thousand silver nyang?”

“Well, if I told you that the annual budget of a prestigious major sect belonging to the Nine Sects and One Gang was just under one hundred thousand silver nyang, would that give you a rough idea?”

“……Huh.”

“Young Master, you just don’t know enough about it. If they paid that much all at once, half the Zhongnan Sect’s foundations would have to be torn out.”

In modern terms, would that be several trillion won? Thinking of it that way made the sum feel more tangible.

I was briefly rendered speechless by the astronomical amount when a gentle voice slipped into my ear.

“Not bad. She’s beautiful enough to topple kingdoms, she’s intelligent, and she has backbone. Our Young Master is going to have his work cut out for him.”

“Pardon?”

“Hmm? What is it?”

“No, I’m sure you just said…”

“Did I? When?”

*What was that? I feel like I just heard something awfully strange.*

It was just as I was giving Wolhwa a suspicious look that Ju Hwaran’s powerful voice rang out.

“Great Hero Hwangbo, please stamp your handprint yourself as proof.”

We had already reached the final stage.

Hwangbo Eom was visibly furious, but he had no options left.

As though he intended to curse every person in the room until the day he died, he took each of them in one by one with his eyes. Then he pressed his bloodied palm to the bamboo slip as a seal.

“Is that enough now?”

“That is sufficient. From this moment on, no contract exists between the Yongbong Escort Bureau and the Zhongnan Sect aside from the compensation payment.”

Ju Hwaran then gave a deep martial salute.

“I will not see you out. Return safely to your main compound. I hope we never have cause to meet again.”

“You…!”

Hwangbo Eom tried to shake off the hands of the Zhongnan disciples supporting him, but even that was no longer easy.

After coughing several times, each cough wet with blood, the last person he glared at was me.

“I have one question.”

“You can ask, but think before you open your mouth. Otherwise, you’ll be buried right there.”

Hwangbo Eom shuddered once before speaking.

“Did you truly… truly cross the wall?”

“Oh, so that’s what you were so curious about.”

“What I saw was that your Force was not yet complete. Then how…”

“My Master once told me that people see only as much as they can see, and believe only what they want to believe.”

“What does that…”

“Is it because you’re so old? You can’t seem to grasp the point. Think whatever you want about my realm. But…”

I could understand why he had his doubts.

But what could I do? In both reality and the Murim, I was the kind of existence that could be summed up in three words: beyond common sense.

That was the System, and that was who I was.

I gazed steadily at Hwangbo Eom and continued.

“Let’s remember two things. You’re weaker than me, and I’m stronger than you. And this place is… the Murim.”

Might Makes Right. The strong devour the weak.

The ground beneath my feet was the Murim, and I was a martial artist standing upon it. Hwangbo Eom, who had lived as a martial artist for eighty years, understood the meaning of my words better than anyone.

“The Murim. You said the Murim.”

His mutter sounded almost like a sigh. After a brief, hollow laugh, his face became utterly cold.

“We’ll meet again. We will!”

“I’ll come pay my respects at your funeral next time. I promise!”

Half a shichen ago, he might have ground his teeth at me, but he had no teeth left for that now.

Hwangbo Eom turned away, radiating cold fury, and shook off the disciples’ hands as he shouted.

“Let go! I’ll walk on my own!”

Though staggering from his serious injuries, Hwangbo Eom forced himself to walk away. Hyuk Sopyung bowed his head heavily before departing, while the Zhongnan disciples hurried after him.

As I watched their backs, one word suddenly came to mind.

*Gratitude and grudges.*[^2]

One of the great gears that drove the Murim.

I did not know what consequences today’s events would bring in the future. But I did not regret it. I was already at odds with the Zhongnan Sect, and ignoring an obvious scheme would have left a bad taste in my mouth.

*Pests have to be exterminated before they grow any bigger.*

Pest control. That was all.

Just as I reached that conclusion with a lightened heart, another thought suddenly crossed my mind.

*Oh, right.*

There was still one left. A pest I absolutely had to catch.

A remarkable pest, too—the kind that had swapped Thousand-Year Snow Ginseng for Hundred-Year-Old Snow Ginseng.

And I had not been the one who drew the sword to exterminate it.

Shing.

A supple flexible sword slid into view. Dagger Hidden Flower Ju Hwaran’s deep-red lips parted, and a toneless voice flowed from them.

“Now there is only one last matter left. Isn’t that right?”

One person was reflected in her dark, gleaming eyes.

[^1]: A Korean proverb meaning that people naturally favor their own kind or those close to them.

[^2]: In the Murim, gratitude and grudges are moral debts that must eventually be repaid.
## Chapter artifact 327

# Chapter 327

“We still have the most important matter left to discuss. Don’t you agree?”

Ju Hwaran was beautiful with her sword hanging loosely at her side. She was also cold.

An aura as sharp as frost rose around her and focused on one person.

“Captain Song.”

Following Ju Hwaran’s gaze, everyone turned their heads. He stood at the end of it.

He was a man who looked to be in his early thirties. His features were fairly handsome, but his fiercely arched eyebrows were a flaw.

As Song Ilseom’s lips twisted, a chilly voice slipped out.

“Are you calling me?”

The people still inside the pavilion fell into exactly two groups.

The outsiders, who were confused because they did not know who Song Ilseom was, and the escorts of the Yongbong Escort Bureau, whose faces had gone rigid.

Chief Escort Heo Jun was the first to step forward. A faint trace of anger showed on his face.

“You’re standing before the Young Bureau Head. Can’t you show proper respect?”

“I’ve shown enough respect. But you people have been saying the same thing for ten years.”

“How dare you…!”

“Then let me ask you something. Why is the Chief Escort who insists that I show proper respect calling the Young Bureau Head by her name in front of everyone?”

“Th-that’s…”

“You don’t need to answer. I don’t care what you call the Young Bureau Head. Just don’t demand that I show you respect.”

His tone and behavior were obnoxious, but Song Ilseom did not seem to be wrong.

As I stared at Heo Jun, who had been rendered speechless, Wolhwa whispered to me.

“Young Master Jin, do you know that man well?”

“Who? Heo Jun? Or…”

“The young and handsome one, obviously. I already know who Chief Escort Heo is.”

“Then why are you asking me? You’re the Shaanxi Branch Leader of the Lower District Sect, of all people.”

“It’s nice that you think so highly of me, but what could a Branch Leader who has been in her post for less than half a year possibly know? If he were a disciple of a famous major sect, maybe. But knowing every ordinary escort captain is beyond even me.”

“An ordinary escort captain… Do you know who he is?”

“Hmm. I know that one of the Dragon-Phoenix Three Escorts is a young escort captain with a nasty temper. That’s about it.”

Song Ilseom. His position was escort captain. That was about all I knew of him, too.

But I knew one thing Wolhwa did not.

Song Ilseom’s strength.

*He’s a considerable master. Stronger than the Ten Dragons and Phoenixes.*

If there was one thing I had learned from moving between the Murim and the modern world, it was that Level was not an absolute measure.

Some people were useless despite having high Levels, while others were much stronger than those above them despite having lower Levels.

Song Ilseom was the real thing. I could tell just by watching his stride and the minute movements of his hands. He was a swordsman with extensive real-combat experience and exceptional martial arts.

*How many people his age are that strong?*

Even if he was not a disciple of a famous major sect, someone of his ability should have become known throughout the Murim long ago.

A needle in a bag was bound to poke through eventually.

*Yet no one knew the needle was there. Not for ten whole years.*

There was only one possible answer.

The needle had deliberately hidden itself, so thoroughly that even the people of the Yongbong Escort Bureau who had spent years with him had no idea how strong he truly was.

*Well, well…*

A thought suddenly crossed my mind. I could not be certain yet, but he was clearly someone I needed to watch carefully.

*I’d like to step in right now.*

But this was a knot Ju Hwaran had to untangle herself.

While I finished making all the preparations necessary to act at any moment, Heo Jun—who had hesitated for a brief instant—began pressing Song Ilseom even more fiercely.

“Captain Song. No, Song Ilseom! Stop spouting nonsense and confess everything already!”

“I don’t know what you’re talking about.”

“Fine. I’ll ask you directly. Where did you hide the Thousand-Year Snow Ginseng?”

“I know nothing about it.”

“It’s not too late. If you admit your crimes and tell us where the Thousand-Year Snow Ginseng is, even now…”

“I said I don’t know.”

At Song Ilseom’s answer, Heo Jun stared at him with eyes that had gone flat and cold.

“Are you really going to play it this way?”

“I could say the same to you.”

“I was giving you one last chance for old times’ sake… but I suppose it can’t be helped.”

As Heo Jun raised his hand, more than twenty escorts spread out around Song Ilseom, blocking his escape in every direction.

The two middle-aged escort captains presumed to be the other members of the Dragon-Phoenix Three Escorts surrounded Song Ilseom together with Heo Jun, forming a triangle.

The atmosphere was stretched taut as a bowstring.

That was when Ju Hwaran, who had remained silent until then, suddenly spoke.

“All of you, step back.”

“Hwaran, he’s not going to confess willingly. We should subdue him first and then—”

“Wait, Uncle Heo. I have something to ask him.”

Whoosh!

Her wrist turned, and the flat of her snake-curved flexible sword struck one of the bamboo slips piled on the table, sending it flying toward Song Ilseom.

“What is this?”

“There are quite a few interesting records here.”

After checking what was written on the bamboo slip, Song Ilseom muttered.

“This is…”

“That’s right. They’re records of the escort missions you were responsible for over the past two years.”

“You’ve gathered only the failures.”

“Why do you think the Lower District Sect and the Beggars’ Sect collected this information?”

“You must have thought they were connected to the Zhongnan Sect.”

“Captain Song was responsible for fifteen escort missions over the past two years. Ten of them failed, and each time, our Yongbong Escort Bureau had to pay a substantial contractual penalty.”

Ten failures out of fifteen. His success rate was less than half.

At that point, even his parents would have suspected him—not just the Beggars’ Sect or the Lower District Sect.

Ju Hwaran continued in a calm voice.

“That’s not all. Looking at the escort missions in which you participated as an assistant escort captain, there are many things that seem suspicious.”

“I did my best every time, but I failed. That is the only answer I can give the Young Bureau Head.”

“That isn’t enough.”

Whoosh! Clatter!

Once again, her flexible sword swung. More than twenty bamboo slips swept up in the sword wind, cut through the air, and fell at Song Ilseom’s feet.

“Are these all records connected to me? There certainly are a lot.”

He clicked his tongue, leaned his sword beside him, and began picking up the bamboo slips to read them.

“That bastard…”

Chief Escort Heo Jun looked ready to charge at the traitor then and there, but at a glance from Ju Hwaran, he had no choice but to let his sword droop.

The wait was not a long one.

“So that’s how it was.”

After muttering those words and setting down the final bamboo slip, Song Ilseom raised his fierce-looking eyebrows.

“How did you figure it out?”

“You did it cleverly. Cleverly enough that someone could close their eyes and dismiss it as a mistake.”

“You figured it out from this alone? You’re sharper than I expected. I thought you were merely a child, but… I underestimated you.”

“That’s a shame.”

“What is?”

“Though not a single drop of blood passes between us, I thought of you as family.”

“Family. What soft talk. Time changes even mountains and rivers, so how much more does it change people?”

At some point, Song Ilseom had gone from formal politeness to openly talking down to her. Yet somehow, every change had come as naturally as flowing water.

He asked in a carefree voice, like a man who had just taken off a constricting set of clothes.

“So what are you going to do now?”

“Punish the criminal.”

“Children resemble their parents. Can you really do it, as Junzi Sword’s bloodline?”

Ju Hwaran answered coldly.

“It is something I have to do, and I will do it.”

Hissssss!

Her flexible sword, charged with internal energy, rose stiffly into the air. Ju Hwaran’s hardened face was reflected in the transparent blade.

A low voice slipped between her lips.

“No matter who I am facing.”

Whoosh!

She moved without warning, faster than anyone else in the Yongbong Escort Bureau.

Though she had only just entered the Peak realm, Ju Hwaran was still a Peak master. The subtlety of speed was woven into both her sword arts and her movement technique.

Thrust!

The flexible sword shot forward like a ray of light and pierced its target exactly.

A wet sound rang out as it pierced flesh. Blood spurted into the air, followed by a scream from a single man.

“Gaaah!”

Ju Hwaran’s eyelids trembled as she watched the man kneel, spraying blood.

The voice that followed was a question aimed at one person.

A condemnation directed at the man she had never once doubted.

“Why did you make that choice, Uncle Heo?”

“H-Hwaran.”

The man raised his head.

The pale, bloodless face of Chief Escort Heo Jun was revealed.

* * *

Whoosh!

Heo Jun’s hair stood on end, and a chill ran down his spine. But by the time he registered the faint sound of something cutting through the air, it was already too late.

Thud!

The blade that pierced through flesh was cold as ice. The pain that followed was hot as fire.

Chief Escort Heo Jun dropped to his knees with a scream.

Even then, only one thought continued to circle through his bleached-white mind.

*Things have gone wrong.*

Although the situation had been overturned by the unexpected arrival of Jin Taekyung, it had not been a bad turn of events for him.

Over the past two years, he had secretly skimmed off wealth worth several thousand silver nyang, sometimes by pretending to make small mistakes and sometimes by making bolder ones.

He had already amassed a tremendous fortune. If the Yongbong Escort Bureau prospered because of this incident, his authority as Chief Escort would rise even higher.

On top of that, he could avoid the guilt of betraying the people he trusted.

It would have been the best of both worlds.

But then…

*Why now, of all times?!*

If he cut Song Ilseom’s throat, everything would be over.

The man would die as a traitor who had betrayed the Yongbong Escort Bureau and colluded with the Zhongnan Sect, and the matter could be quietly wrapped up without any further trouble.

*I even hid my identity so thoroughly from the Zhongnan Sect, just in case. How did they figure it out?*

Pain.

And then, a shock greater than the pain itself hardened Heo Jun in place.

A low voice pierced his ears.

“Why did you make that choice, Uncle Heo?”

Heo Jun’s bowed body trembled.

He knew the owner of that voice. He could not have failed to recognize it.

It belonged to the girl he had watched over since she was a baby.

She had been his sworn brother’s treasured jewel, the one and only niece he had once regarded as more his own child than his biological children.

And…

She was also the person who had driven a sword through his shoulder.

“H-Hwaran.”

Heo Jun slowly raised his head and met the eyes of Ju Hwaran looking down at him.

Her voice had been calm, but her eyes trembled with emotion. Seeing that, an emotion he had temporarily forgotten rose to the surface.

Hope.

*I can live.*

Heo Jun immediately recognized the turmoil in Ju Hwaran’s eyes.

She was caught between affection and betrayal. That was the only avenue of escape he had left.

“I was wrong. It was all my fault!”

“Uncle.”

“Please spare me. I’m begging you!”

Heo Jun cried out desperately. He did not care about the horrified looks of the escorts or anyone else watching their trusted superior betray them.

His dignity? The contempt of others?

The dead could not feel any of it.

He would do anything if it meant surviving this place and seeing tomorrow’s sun.

“Urgh. Hwaran…”

Heo Jun groaned in pain. Ju Hwaran’s flexible sword had pierced straight through his right shoulder, and the hand gripping the hilt was trembling slightly.

“Then make an excuse. Tell me why you did it. Tell me why you had no choice.”

If making excuses could have increased his chances of survival by even a little, Heo Jun would have already begun listing every excuse he could think of.

But he knew Ju Hwaran’s personality well. The fact that she had swung her sword meant she was already certain. A halfhearted excuse would only hasten his death.

He had to beg unconditionally and work his way into her heart.

“It was all the fault of this foolish uncle. I have nothing else to say.”

Heo Jun lowered his head and reddened his eyes.

The effect was immediate. He felt the strength in the sword weaken and continued speaking.

“It’s shameful, but I once accepted a bribe. Then, after Hyung suddenly collapsed, the Zhongnan Sect approached me using that as leverage, and I… I was afraid I would be cast out. I didn’t want to leave the Escort Bureau I had devoted my entire life to, and I believed the Zhongnan Sect’s promise that they wouldn’t hurt you.”

“…”

“I intended to agree only once—just once—but by then I had already stepped into a swamp I could never escape.”

“Is all of that true?”

“How could I lie to you?”

Contrary to his words, there was only one truth in Heo Jun’s entire speech.

He had accepted a bribe.

He had been the one who approached the Zhongnan Sect while concealing his identity immediately after Junzi Sword collapsed, and that secret relationship had continued for two years.

*I just have to get through this moment. Just this moment!*

Tears streamed down his face. They contained no remorse—only his fear of death and his desperate wish to survive.

“Please forgive me…!”

At his desperate plea, the people watching shook their heads from side to side. More than a few escorts turned away, unable to bear the sight.

But Ju Hwaran was different.

She stared at Heo Jun with her lips pressed tightly together before suddenly speaking.

“How did you steal the Thousand-Year Snow Ginseng? I never let it out of my sight, not even for a moment.”

“Th-that…”

“Tell me the truth.”

“…I mixed a mind-clouding drug into the food. Everyone was exhausted, so a small amount was enough.”

The drug was a narcotic that clouded the mind and induced sleep, and its effects were reliable.

Even Ju Hwaran, a Peak master, had fallen into a deep sleep, believing it was merely the result of the journey’s exhaustion.

“So that was why you were outside my room that night.”

“I had to be careful not to make a sound even when leaving. That man—no, Captain Song—was still awake until dawn even after taking the drug.”

Song Ilseom, who had been standing against the wall with his arms crossed, muttered expressionlessly.

“So that was a mind-clouding drug. No wonder I felt so tired that day. Next time, use something better. Though I don’t know whether you’ll have a next time.”

*What a goddamn bastard.*

Heo Jun barely managed to swallow the curse that rose to his lips and looked at Ju Hwaran.

“Hwangbo Eom, that old man, threatened me. He said that if I didn’t switch the Thousand-Year Snow Ginseng, he would kill me and my family and wipe out the Yongbong Escort Bureau. I only wanted to protect everyone!”

“Then you made the wrong choice.”

“You’re right. I once went to Hyung’s sickbed, crying as I confessed everything. But… but I couldn’t undo the mistake.”

“Your mistake?”

At the mention of her father, Ju Hwaran’s eyes trembled—but only for an instant.

She soon shook her head slightly.

“No. You’re wrong. It wasn’t a mistake. It was a choice, Uncle.”

“Hwaran…!”

“My father used to tell me that every choice comes with responsibility. Although he failed to make the family business he inherited prosper, he never once regretted his choices.”

Heo Jun suddenly realized that the conflict and wavering he had seen in Ju Hwaran’s eyes were gradually disappearing.

*Could it be?*

No. It could not be.

This could not be happening!

Tears and cold sweat streamed down Heo Jun’s cheeks.

He desperately raised his voice.

“Give me one chance! Just one last chance! I’m your father’s one and only sworn younger brother, and your uncle, aren’t I? Hwaran, for the sake of the bond we’ve shared, please!”

“The bond we’ve shared, you say?”

“Yes. I shared both good and bad with Hyung for thirty years. If your father were here—if it were him—he wouldn’t take my life this easily!”

“Uncle Heo. No, Chief Escort Heo Jun.”

Heo Jun, who had been repeatedly smashing his head against the floor, lifted his head in a daze.

The eyes of his niece were there.

They were eyes he had never seen before—cold eyes with not a trace of hesitation left in them.

“You’re right. If my father were here, he would have forgiven you. But…”

A low voice continued toward the frozen Heo Jun.

“I am not Junzi Sword Ju Hogun. I am Dagger Hidden Flower Ju Hwaran.”

And in the next moment, silver sword light filled Heo Jun’s vision.

Swish! Rip!
## Chapter artifact 328

# Chapter 328

“Guh… ghk.”

Blood bubbled up from Heo Jun’s slashed throat.

He thrashed and clutched at his neck, but it was already too late.

Ju Hwaran’s single sword strike had been fast and precise. It had accomplished its purpose without a single mistake.

“Grrk…”

It was the dying gasp of a man on the verge of death.

What had he wanted to say? *It’s unfair? Spare me? Or perhaps, I’ll curse you even in death?*

Heo Jun’s lips, which had been opening and closing as blood rattled in his throat, suddenly froze.

The strength drained from his struggling limbs, and the light went out of his eyes as they stared at Ju Hwaran, stained with countless emotions.

Haaa…

The last breath he exhaled in this world scattered into the air.

Heo Jun, the sworn brother of Junzi Sword Ju Hogun and the Chief Escort who had spent thirty years with the Yongbong Escort Bureau, died just like that.

At the hands of the niece who had once looked up to him as family.

“…Uncle Heo.”

Ju Hwaran’s quiet voice drifted through the air. Her back looked strangely desolate.

After gazing down at Heo Jun’s lifeless body for a moment, she slowly turned around.

Her obsidian-like eyes swept past the escorts of the Yongbong Escort Bureau and turned toward the outsiders.

One person at a time. Then, at last, she looked at me and saluted everyone with clasped hands.

“I, Ju Hwaran, Young Bureau Head of the Yongbong Escort Bureau, have been discourteous before my seniors in the martial world.”

Pain sometimes made people mature. I hoped she had grown another step through this ordeal.

*It’s a relief that she seems calmer than I expected, but…*

Something about the atmosphere felt awkward.

Just as I was thinking that, something pressed down hard on my foot.

I looked down and saw a flashy women’s shoe.

As far as I knew, there was only one person here who might wear something like that.

When I looked at her questioningly, Wolhwa gestured to either side with her eyes.

Only then did I notice everyone staring at me.

The people around me had parted neatly to either side, all of them looking straight at me.

And at the end of that line stood Ju Hwaran, still holding her salute.

*…What is this?*

Was there something on my face?

As I stood there flustered, Wolhwa whispered so softly that I could barely hear her.

“Young Master Jin, say something.”

“Pardon?”

“Young Lady Ju greeted you. You need to respond on everyone’s behalf.”

“Why do I have to do it?”

“Hurry. Young Lady Ju will grow old waiting.”

“…”

Well, she had aged about ten seconds in the meantime.

I wasn’t sure why I had to speak when we had Huashan’s leading candidate for Sect Leader, the Beggar Prince, and the Lower District Sect’s Shaanxi Branch Leader standing right there, but I gave an awkward bow anyway.

“There’s no need to call it discourteous. And I’m not a senior in the martial world, so you can treat me casually.”

“How could I do that?”

Ju Hwaran raised her head and spoke calmly.

“Great Hero Jin and the other seniors are Benefactors of the Yongbong Escort Bureau. Without your help, we would have suffered a terrible calamity… and we would never have been able to punish the traitor.”

A trace of bitterness crossed her face as she added the final words.

Perhaps she felt it herself, because her voice grew firmer.

“I will repay the debt we owe you today without fail.”

It wasn’t as if we had done anything extraordinary—but the help I and the other sects had provided had certainly been substantial. From Ju Hwaran and the Yongbong Escort Bureau’s perspective, even bowing a hundred times would not be enough.

*Being called Great Hero is still a little much.*

Even Young Hero made me cringe. This was a whole new level.

I suddenly felt as if I should grow a beard, so I changed the subject.

“Repay the debt to the other people here, not me. More importantly, what are you going to do now?”

“We’ll recover the bodies first and return to the bureau. There’s a lot to take care of.”

“You must be extremely busy.”

Ju Hwaran was managing the bureau in place of her unconscious father.

The day would fly by just dealing with the aftermath of the long escort mission, and with one crazy incident after another on top of that, even ten bodies wouldn’t be enough.

Ju Hwaran nodded at my words and opened her mouth.

“Even so, we have enough time to host Great Hero Jin and his companions.”

“You have enough time? That’s a relief… Huh?”

“You and your companions are Benefactors who saved me and my family. I can’t send you away without offering you proper hospitality.”

“Um, Young Lady Ju, the thing is…”

“Are you perhaps very busy?”

I was busy. Extremely busy.

Jeok Cheongang had a treatment window of at least six months and at most eight.

Within that time, I had to search the vast land of Sichuan for the mysterious person known as the Divine Physician.

*It took us a week to get from Henan to Shaanxi. Reaching Sichuan will take another week at the very least.*

And that was assuming I used my movement technique to the fullest.

Everything about the Divine Physician was shrouded in mystery. No one could predict how long it would take to find him.

That was why I had already begun feeling anxious after spending only a day in Xi’an.

*And I’m already late today.*

The sun had been high in the sky for quite some time. Our entanglement with the Zhongnan Sect had cost us a considerable amount of time, so I needed to start running myself ragged from this moment on.

And yet…

“No, I’m not busy.”

The words escaped my mouth before I could stop them.

What had just happened? That was the exact opposite of what I had intended to say.

While I stood there in a daze, Ju Hwaran cautiously asked,

“Great Hero Jin, are you really all right? If you have something urgent to attend to, we can postpone it until later.”

*Thank you. Thank you so much for saying that first.*

That was just like her—sharp and perceptive. Her words scratched exactly where I was itching, and I answered without hesitation.

“No matter how urgent it is, can’t I share one meal with you?”

“Yes.”

“I was hungry after exerting myself so much anyway. That works out perfectly. Let’s go.”

*Am I a fucking idiot? Seriously?*

I needed to go to Sichuan. Why was I going to the Yongbong Escort Bureau?

But by the time I came to my senses, I was already carrying a wooden A-frame carrier on my back.

Just as I let out a deep sigh inwardly, one person who had seemed completely detached from the entire situation caught my eye.

As I stared at him, he spoke first.

“What? Do you have something to say?”

This was the first time someone’s casual speech had sounded so natural upon first meeting.

In any case, since he had dropped the formalities first, I felt more comfortable too.

“I was just wondering if you weren’t coming.”

“I have no reason to.”

“Then come up with one.”

“…”

“Since I know you have time to spare, let’s have a conversation.”

“A conversation?”

“Yeah. A conversation.”

Song Ilseom raised his eyebrows as he looked at me, then straightened from the slanted position in which he had been leaning.

* * *

It was early spring. The bright sun disappeared behind the western mountains less than two shichen after we arrived at the Yongbong Escort Bureau.

Oil lamps lit the guest hall, where a magnificent feast had been laid out on the table. Cheongpung and Gung Gibang stared wide-eyed as they shoved food into their mouths.

“Mmph. Benefactor. This is delicious. Mmph-mmph-mmph.”

“…Eat as much as you want. Preferably don’t talk.”

The food did look delicious.

At least until Cheongpung deliberately showed me what was in his mouth.

“Gobble, gobble. This Escort Bureau sure knows how to cook. Young Bureau Head, could you distribute the leftovers to the members of our sect as well?”

Gung Gibang really was a beggar to the bone.

As he continued his meat-centered massacre, Ju Hwaran nodded.

“Of course. Tell them to come by whenever they’re hungry.”

“Oh, whenever they’re hungry?”

“…Not quite that much.”

If every Beggars’ Sect disciple in Shaanxi Province descended on this place, the four hundred thousand silver nyang we were supposed to receive as compensation would disappear into food costs.

Gung Gibang grinned, exposing his yellow teeth.

“Don’t worry. I’ll make sure there’s nothing to worry about.”

Hyuk Mujin, who was at least eating normally, whispered,

“That makes me even more worried.”

“You said it.”

At this rate, would the Yongbong Escort Bureau go under because of the Beggars’ Sect instead of the Zhongnan Sect?

I was inwardly determined to warn him when Ju Hwaran spoke to me.

“It’s a shame the others didn’t come.”

“Yeah. The food is good, too.”

The others in our group—in other words, Baek Museong, Heukgeol Beggar, and Wolhwa—had all declined the invitation.

I wasn’t sure why, but they seemed to change their tune after Wolhwa fixed the two of them with a long, hard glare.

In any case…

“You aren’t eating very much, considering that.”

“No, it’s delicious. Look. I’ve already finished two bowls of rice.”

“That’s strange. Why does it look like you’ve eaten so little?”

“It’s all relative. Look at them. They’re waging the Great Faction War against the food.”

*Schlurp, schlurp!*

*Gobble, gobble!*

*Chomp, chomp, chomp!*

Ju Hwaran nodded as if she had gained enlightenment.

“Ah.”

“Mujin and I are the normal ones. The one who’s actually eating little is over there.”

Song Ilseom answered in his blunt voice.

“I’ve been saying this for ten years, but the food here is too salty. Spicy and salty food is too stimulating and makes the body feel heavy.”

“Someone suddenly comes to mind. If she were here, she would have beaten you to death with a ladle.”

“Who are you talking about?”

“There’s someone like that. If she hits you once, you’ll scream without meaning to. I’ve been beaten by her plenty of times myself. Strangely, I could never dodge even once.”

“Great Hero Jin, is that true?”

“You mean you?”

Ju Hwaran asked back in surprise, and Song Ilseom’s eyes flashed.

“Even if the person who defeated the Taeeul Merciless Sword says that, she must be an extraordinary master indeed… Can you tell me her name and sobriquet?”

“Kim Jeonghee. Her sobriquet is Lady.”

“Hmm. I’ve never heard of her.”

Of course he hadn’t. She was my mother.

Without showing anything on my face, I continued in a solemn tone.

“In any case, she always said that you had to eat all kinds of food without being picky if you wanted to grow big—or rather, become strong.”

“Hmm.”

“So stop whining about the side dishes and fucking eat.”

Song Ilseom pondered this with a serious expression, then picked up his chopsticks and began eating the side dishes.

The more I watched him, the stranger his personality seemed.

*He’s strange, but he doesn’t seem dangerous.*

A few shichen earlier, I had briefly suspected Song Ilseom of being dangerous in the worst possible way.

It had been a fairly reasonable suspicion. An exceptional Peak master who had hidden his strength for ten years. I had already encountered a similar case in Shanxi Province.

*Dark Heaven.*

The Head Elder and the Five Gates of Shanxi, who had been lying low for decades. Somehow, Song Ilseom’s behavior had overlapped with theirs.

But the longer I spoke with him, the suspicion faded and only curiosity remained.

*What the hell is this guy?*

His blunt manner of speaking and behavior. He seemed rough to the point of being crude, yet there was a peculiar air of refinement in his appearance and various other aspects of him.

Perhaps that was why his casual speech sounded so natural.

*Well, this is something.*

I stared at Song Ilseom.

He was chewing his side dishes thoroughly with an exaggerated grimace. After swallowing, he spoke.

“That look again. What is it?”

“I was just thinking about your identity.”

“Are you that curious?”

“Yes. Very.”

Talking with this guy was like driving down a wide-open highway. That was why it felt comfortable.

Before long, everyone else—including Ju Hwaran—had perked up their ears and was watching Song Ilseom’s mouth.

He seemed displeased by the attention and raised his eyebrows.

“There’s nothing special about it. I only stayed at the Yongbong Escort Bureau because I had ties to the previous generation.”

“You had ties to the previous generation?”

“To be precise, my father received a great favor from them.”

Huh? Wait a second. That sounded familiar, but I couldn’t quite place it.

I turned my head and saw Ju Hwaran staring at Song Ilseom with her eyes wide.

It was clearly the first time she had heard this story in ten years.

“May I ask your father’s name?”

“Song Pyosan.”

“Song Pyosan… I’ve never heard of him.”

“That’s hardly surprising. It happened almost fifty years ago.”

Almost fifty years ago? Was he talking about the Great Faction War?

Before we could ask, Song Ilseom continued as if it were nothing important.

“The Guangdong Chen Family was a clan forgotten long ago. My mother was saved with the help of Escort King Ju Gongsan, but she feared the greedy martial artists and had her child carry on her surname. It was a wise decision.”

It felt as if I had been struck in the back of the head. Ju Hwaran stared at Song Ilseom with trembling eyes.

“Then could it be that you…?”

Instead of answering, Song Ilseom pulled a faded jade hairpin from his robes and held it out.

It was the only escort fee a young escort surnamed Ju had ever received from a woman in the final stages of pregnancy more than fifty years ago.
## Chapter artifact 329

# Chapter 329

When Song Ilseom’s identity was revealed, everyone was left utterly astonished.

Hyuk Mujin had admired the Murim even before becoming part of the Taiyuan Jin Family, so of course he knew the stories about him. Even Cheongpung pretended to know him, claiming that the Sword Saint had told him about Song Ilseom.

“Mmph-mmph. Grandpa said the Escort King was a good man. Gulp. He said so.”

“…I know. Swallow everything before you talk. Please.”

“Yes! Mmph-mmph.”

If even Cheongpung knew about him, the other two went without saying.

Ju Hwaran, the Escort King’s granddaughter, was staring at the jade hairpin with trembling eyes, while Gung Gibang was so excited that he sprayed the contents of his mouth in every direction.

“Th-the Guangdong Chen Family!”

Tududududuk!

Song Ilseom knocked away a dozen or so grains of rice with his chopsticks and replied,

“As I said, the Guangdong Chen Family ceased to exist long ago. By the way, can you do something about all that flying out of your mouth?”

“My Master also told me about the Escort King’s Ten-Thousand-Mile Escorts. But to think the child in that story was you!”

“Did you listen with your nose? That child was my father. And stop spitting everywhere. It’s disgusting.”

Swish! Tududududuk!

Wow. He knocked all of those away.

Song Ilseom once again whipped his chopsticks through the air like lightning, then asked me,

“Is this beggar really the Successor Beggar of the Beggars’ Sect?”

“He is, even if he doesn’t look like it. Why?”

“A Rain of Ten Thousand Flowers keeps pouring from his mouth. I wondered if he might be a disciple of the Sichuan Tang Clan.”

“Hmm. Probably not.”

While we were having that conversation, Ju Hwaran, who had been staring blankly at the jade hairpin, finally spoke.

“I heard it from my father. He said my grandfather remained curious about what had become of the Guangdong Chen Family until the very end. But he was never able to find them…”

“My grandmother carried that regret as well. She had to flee with my father, who was still a baby, without leaving behind even a single letter.”

“Why did they suddenly disappear?”

“Because it was dangerous. The Guangdong Chen Family’s martial arts were all lost when the family was burned to the ground, but apparently people refused to believe that.”

“But if they were within the territory of the orthodox factions…”

“Greed does not discriminate between members of orthodox factions and practitioners of demonic, heterodox arts. Some of those seeking the Guangdong Chen Family’s Peak martial arts were people even the Escort King’s name couldn’t deter.”

*A time of chaos.*

When I thought of those words, I felt as if I could understand what the mother and child must have gone through back then.

In turbulent times, the rules between people crumble. Everyone follows their instincts, and morality inevitably grows faint.

The mother had fled to protect her child from the greed of others. Without telling anyone.

“My grandmother was a woman who couldn’t stand against even a Third Rate swordsman, but she was wiser than ten Peak masters combined.”

After a brief silence, Song Ilseom added,

“Of course, she couldn’t escape birth, aging, sickness, and death.”

“Then…”

“She died of an illness when I was ten. As she gave me this jade hairpin, she told me everything that had happened. It was an astonishing story—the first I had ever heard of it.”

Despite his blunt appearance, Song Ilseom was rather talented at telling a story.

The one thing I had been curious about was his parents. But after hearing that he had wandered the streets following his grandmother’s death, there was no need to ask.

Unfortunately, it was clear that both of them had died young.

And as soon as one question disappeared, another took its place.

“Then how did you develop that level of skill? Didn’t you say the Guangdong Chen Family’s martial arts were lost as well?”

Song Ilseom’s answer was simple.

“On the battlefield.”

“Did you live as a wandering martial artist?”

“I had no talent for begging. More people beat me because they found my face and expression unpleasant than those who tossed me an iron coin.”

Gung Gibang, who had been listening quietly, nodded emphatically as if he could relate.

“There’s a proper way to beg. The most important things for a beggar are a face and expression that inspire pity, but when you’re as handsome as Young Hero Song or me, even earning a few coins is difficult. I went hungry plenty of days because of that.”

Song Ilseom’s face hardened.

“Successor Beggar, that remark is deeply offensive. I would appreciate it if you didn’t insult me.”

“Why? Did you ever see my face when I was young? I’m telling you, without exaggeration, Song Yu would have wept at the sight of me.”[^1]

“Song Yu would cry?”

Song Ilseom stared intently at Gung Gibang’s face, which looked like something out of a Picasso masterpiece.

“With that face, he might. If you run into me at night, stay far away. If I suddenly came face-to-face with you, I might cut you by mistake.”

Song Ilseom looked as if he were seriously considering whether to cut him down on the spot, then continued his story.

“In any case, I was hopeless at begging, and I had no decent work either. After going hungry for more than three days, the sky began to look yellow. I decided that becoming a sword boy would be better than starving to death.”

“A sword boy? The kind who carries someone’s sword?”

“That’s right.”

“Isn’t that something people with money hire? They don’t want to bother carrying their own swords, so they make someone else do it.”

“Do you think people with money would hire some beggar brat whose origins they didn’t even know?”

“Fair point.”

“Surprisingly, wandering martial artists hire the most sword boys. Normally, they make them handle all kinds of odd jobs. When things get dangerous, they use them as meat shields.”

*I thought that sounded like a sweet part-time job. Turns out it was a job on the Hell Continent.*

“It wasn’t a particularly comfortable or pleasant experience.”

Song Ilseom calmly listed the events of his past.

Normally, he had to serve wandering martial artists while enduring all kinds of abuse and violence. When arrows rained down, he had to collect the weapons left on the battlefield.

When the wandering martial artist abandoned him and fled because he was too busy saving his own life, Song Ilseom experienced nothing short of hell.

“I hid among piles of corpses for four days. When I barely made it out alive and went looking for the wandering martial artist, the first thing he did was search for the sword he had entrusted to me.”

“Wow. What a crazy bastard.”

“Fortunately, the two swords I was carrying were safe. Even while fleeing, I held on to them desperately.”

“…Wow. You really are a crazy bastard.”

“I wasn’t as crazy as he was. He started spouting nonsense about how he had originally entrusted me with three swords, then told me to get the hell out of there if I didn’t want to die like a dog. Of course, he didn’t give me a single coin for the year I had worked for him.”

Song Ilseom brushed back his fallen bangs and muttered,

“I was pissed.”

Naturally, instead of filing a complaint with the labor authorities, he chose a faster solution.

“There happened to be two swords. I picked one up. It was heavy.”

“You won.”

“I killed him.”

Song Ilseom lightly corrected me and spun his chopsticks around.

“It wasn’t very difficult. I had always watched his martial arts, and they were predictable. I dodged ten times and stabbed him once, like following a prearranged exchange. He fell.”

Gulp.

Hyuk Mujin swallowed nervously and asked,

“How old were you then?”

“Twelve? Thirteen? I don’t remember clearly, but somewhere around that age.”

“Th-then your opponent…”

“He was a lousy Third Rate wandering martial artist. If he’d been First Rate, do you think I’d have been crazy enough to take him on?”

*No, the fact that a kid who hadn’t even graduated elementary school attacked a martial artist in the first place seems insane.*

*What was I doing at that age?*

I didn’t know. I was probably playing while picking my nose or something.

*This guy’s a gifted bastard too.*

There were countless martial sects and families throughout the world.

If the Nine Sects and One Gang and the Five Great Families were the first tier, there had to be a second tier as well.

According to what Jeok Cheongang had casually told me, the Guangdong Chen Family had been one of those.

*Is this what they mean when they say the blood of a martial family can’t be hidden?*

To reach that level without the family’s secret martial arts…

Just as I was marveling at the thought that Song Ilseom really was something special, Gung Gibang, who had been silent for a while, suddenly stared at him in shock.

“Could you be the Soul-Chasing Guest?”

“That’s what they called me ten years ago. By the way, is your mouth a bottomless jar? How the hell are you still spitting out rice after all this time?”

“Hah. I never imagined that famous Soul-Chasing Guest would be a young man around my age.”

The Soul-Chasing Guest. That seemed to be Song Ilseom’s sobriquet.

He must have been rather famous, because Ju Hwaran’s eyes also grew round.

“You’re the Soul-Chasing Guest who won a hundred life-and-death duels?”

“Exactly one hundred and two. It’s all hollow fame, so there’s no need to make a fuss. There are already two people here who are younger and more impressive than me.”

Cheongpung, who had somehow finished off most of the food, answered with a cheerful grin.

“No, you’re amazing too, Young Hero Song.”

I nodded as well.

“He’s strong. Just weaker than me.”

“…Are you two making fun of me?”

Cheongpung slurped down something that looked like cinnamon punch and said,

“No teasin’ you!”

“He says he isn’t teasing you.”

Song Ilseom’s gaze shifted toward me after my kind translation.

“What about you?”

“I am teasing you.”

“…Is there no alcohol? I feel like having a drink after all this time.”

* * *

The meal, which had begun in the early evening, ended only when midnight was drawing near.

Song Ilseom had left the fine liquor untouched and repeatedly emptied cups of strong liquor instead. He was now resting his head on the table, while Ju Hwaran, who had been sipping hers, had bright red cheeks.

And then…

*It’s really time to leave now.*

When I stood up, Gung Gibang used his internal energy to drive away his drunkenness, while Hyuk Mujin hoisted Cheongpung onto his back. Cheongpung was already completely drunk and snoring softly.

“We’ve imposed on you, Young Lady Ju.”

“You’re leaving already?”

“I’d like to stay longer, but I don’t think I can this time.”

“Is that so?”

Her intoxicated eyes curved like half-moons.

Her steps were light, almost as if she were dancing. Clear dimples appeared in her cheeks. It seemed that her drunken habit was laughter.

“Would you like to take a walk?”

“Pardon?”

“Let’s walk. The flowers in the garden have just bloomed.”

“Oh. Congratulations. They must be pretty.”

A burst of laughter escaped her.

Before I could ask why she was laughing, Ju Hwaran giggled and stepped outside.

I followed behind her without thinking, then suddenly stopped and turned around.

“You two aren’t coming?”

“…Is he human?”

“Worse than a beggar. A beggar of a man. Worse than a beggar.”

“What the hell? Why are you looking at me like that?”

“It’s how I feel.”

“That’s how I feel.”

“Let’s go. Young Lady Ju said the flowers have bloomed in the garden. We can look around together and leave right afterward. The timing will be perfect—”

My words were cut off by the sighs of Gung Gibang and Hyuk Mujin.

The two men shook their heads with expressions of utter horror and spoke in turn.

“I need to take a dump. Where’s the latrine?”

“Me too. We’ll take turns going back and forth, so take your time looking around.”

“…Uh. Sure.”

*What’s wrong with those two? Is their stomachache really that bad? Their expressions are practically demonic today.*

*I must have imagined the contempt and fury in their eyes.*

I hurried outside and began walking through the garden beside Ju Hwaran, who had been waiting for me.

“Great Hero Jin is, how should I put it, a really interesting person.”

“Am I?”

“Yes. You can be a little exasperating sometimes, but… well, in a way, that’s a strength too.”

“…?”

*What is this? Is she insulting me indirectly?*

At my bewildered expression, the smile around Ju Hwaran’s lips deepened.

“I don’t know how long it’s been since I last laughed out loud. It feels like it’s been more than half a year.”

“Hmm? Didn’t you laugh last time too? When we passed Black Stone Mountain?”

“Oh. Did I?”

“Maybe you just don’t remember. That makes twice in three days.”

“I wonder. Did that really happen?”

Ju Hwaran mumbled in a slightly airy voice, then suddenly pointed toward the sky.

“Great Hero Jin, can you see that?”

“Of course. It’s a full moon.”

“The moon is especially bright tonight.”

“Did you know why the moon is bright, Young Lady Ju? It’s because it reflects light from the sun.”

“Pardon?”

“No, I’m serious. It’s not some ridiculous story. It’s a famous result of scientific research… No, I heard it from a scholar. Where was it? That’s right, somewhere around the imperial palace.”

Another little laugh slipped from her lips.

“No, it really is true…”

“All right. I’ll believe you. By the way, Great Hero Jin.”

“Yes?”

“This.”

To me, still feeling wronged, Ju Hwaran suddenly held something out.

It was a solid, elongated wooden case, one I had already seen at the teahouse.

“Could this be…”

“That’s right. It’s Hundred-Year-Old Snow Ginseng.”

“…”

“It’s a small gift compared to what you did for us, but would you accept it? So that my heart can be a little more at ease.”

I silently looked back and forth between Ju Hwaran and the wooden case.

*Should I refuse? Should I accept it? Should I refuse…*

After several rounds of internal conflict, I finally nodded.

“I’ll accept it gratefully. Thank you.”

Ju Hwaran smiled brightly.

Her smile was brighter than the moon hanging in the sky.

We walked for about fifteen minutes, chatting about trivial things, until the flowers lining both sides of the path gradually began to thin.

Ju Hwaran’s steps slowed as well.

“Great Hero Jin.”

“Yes, Young Lady Ju?”

“Do you think I can do well?”

Her sudden voice was damp and desolate.

Perhaps this was why she had drunk.

But there were times like this. Days when nothing could suppress your emotions. Moments when feelings you had desperately held back surged over the brim.

“Do you really think I can do well?”

I suddenly opened my mouth.

“It’s okay if you can’t.”

“…”

*It’s okay. I understand how you feel right now. Hang in there.*

There were times when every word of comfort sounded hollow. Of course she wasn’t okay, and someone standing a step away could never understand everything the other person was going through. Hearing someone tell you to stay strong didn’t suddenly fill you with strength.

I didn’t offer Ju Hwaran some clumsy consolation today because she was already suffering enough.

“Young Lady Ju, you’re only human too. It’s okay if you don’t do well, and it’s okay not to force yourself to stay strong.”

She only had to continue forward as she had been, following the current as it flowed.

One step at a time, matching her own steps instead of someone else’s.

“Wouldn’t that be enough?”

Ju Hwaran’s tear-filled eyes looked up at me.

Then they curved like half-moons.

* * *

Thump!

I kicked off the ground.

The scenery fell away, and the earth blurred past beneath me.

The voices of Ju Hwaran and the people of the Yongbong Escort Bureau gradually faded, then abruptly disappeared.

Only then did the two guys who had been watching my reaction speak.

“Young Lady Ju’s eyes looked swollen earlier…”

“Do you think she cried? No, no way. She couldn’t have.”

*They noticed that carefully even in the dark.*

When I didn’t answer, Hyuk Mujin pointed at the bulge across my chest and asked,

“But what is that?”

“Oh, this?”

*I forgot to put it in my inventory.*

I gave a quiet laugh, remembering someone’s lie.

“Thousand-Year Snow Ginseng.”

“Whaaat?”

“Huh?”

[^1]: Song Yu was a famous ancient Chinese poet traditionally celebrated as a paragon of male beauty.

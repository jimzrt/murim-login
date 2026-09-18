# Checkpoint Review — 370–374

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

# Chapters 370–374

## Plot

Seven days after the Three-Gate Bloodbath, the Sichuan Tang Clan begins rebuilding with aid from Emei, Qingcheng, the Beggars’ Sect, and other allies, while Emei conducts funerals for the dead. Jin Taekyung awakens, is publicly honored as the Blazing Flame Divine Dragon, and is recognized by Jeok Cheongang as a new Great Hero after reaching the Supreme Peak realm.

Cheongpung the Ancient Sword and Extinction Divine Nun, now Emei’s Sect Leader, lead Taekyung and Jeok to a hidden cavern near Chengdu. There they discover Dark Heaven’s inactive Moving Formation, once capable of transporting hundreds of people across hundreds of li. The Slaughter Saint identifies Dark Heaven as the successor to the Demonic Cult. Mungyeong then renounces his former identity and vows to live only as a medical apprentice; Taekyung agrees to keep his secret.

Taekyung’s System confirms his advancement to Level 120, the Supreme Peak realm, and the eighth stage of the Fire Gate Divine Technique. He also discovers a second bound Item beside White Flame, but its identity remains unknown. Before he can investigate further, an investigation team from Henan arrives.

Jin Wikyung offers the devastated Tang Clan orthodox protection and possible relocation, warning that a war greater than the Great Faction War is approaching. He must escort the captured Third Fiend to Henan, so Taekyung prepares to accompany him. Their departure is delayed when Tang Sadok awakens, with Tang Horyong still serving as Acting Family Head.

## Continuity

- Jin Taekyung is awake, Level 120, at the Supreme Peak realm, and has manifested Force. He is publicly known as the Blazing Flame Divine Dragon.
- Taekyung’s Fire Gate Divine Technique and Fire Dragon Divine Spear are at the eighth stage. White Flame and an unnamed second bound Item are in his possession; the Myriad-Poison Ring remains unappraisable.
- Jeok Cheongang is alive but still recovering from the battle and prison escape.
- Mungyeong is secretly the Slaughter Saint and intends to live as a medical apprentice. Taekyung, Jeok, Cheongpung, and the two Sect Leaders have agreed to protect his identity.
- Dong Feng’s dantian and martial arts were destroyed while shielding Jeok; he remains Mungyeong’s Master.
- The Third Fiend is captured and is to be escorted to Henan by Jin Wikyung and Taekyung. The Second Fiend’s fate remains unknown.
- The Sichuan Tang Clan suffered catastrophic losses and is rebuilding. Tang Sadok has awakened; Tang Horyong remains Acting Family Head, and relocation has been proposed but not decided.
- The hidden cavern near Chengdu contains Dark Heaven’s inactive Moving Formation. Its origin, purpose, and loss of power remain unexplained.
- Dark Heaven is identified as the successor to the Demonic Cult, and its response to the failed Three-Gate Bloodbath is unknown.
- The Lord of Heaven escaped after possessing the Western Heaven Demon Lord’s body; both the entity’s nature and the Demon Lord’s fate remain unresolved.

## Translation Decisions

- Render 열화신룡 as **Blazing Flame Divine Dragon**, distinct from **Huashan Divine Dragon**.
- Render 삼괴 as **Third Fiend** for the individual and **Three Fiends** for the collective.
- Use **Supreme Peak**, **Force**, **Fire Gate Divine Technique**, **Fire Dragon Divine Spear**, **White Flame**, and **Moving Formation**.
- Render 환영진 as **illusion formation**, 독룡각 as **Poison Dragon Pavilion**, and 가주 대행 as **Acting Family Head**.
- Render 진인 as **Perfected One**, 도우 as **Fellow Daoist**, and 신니 as **Venerable Nun** when used as forms of address.
- Use **Mimi** and **Mimi-chan** for 미미 and 미미쨩.
- Preserve the contrast between Mungyeong’s cheerful medical-apprentice persona and the Slaughter Saint’s restrained authority.

## Durable state

{
  "active_continuity": [
    "The Sichuan Tang Clan is rebuilding seven days after the Three-Gate Bloodbath, which caused catastrophic casualties and ongoing funerals.",
    "Most Dark Heaven attackers involved in the Sichuan assault are dead or captured; Mungyeong captured the Third Fiend in the hidden cavern, while the Second Fiend's fate is unknown.",
    "Jin Taekyung is awake, has reached Level 120 and the Supreme Peak realm, manifested Force, and is publicly known as the Blazing Flame Divine Dragon.",
    "Jeok Cheongang is alive but remains weakened and is recovering his strength.",
    "Dong Feng's dantian and martial arts were destroyed while shielding Jeok Cheongang; the Divine Physician is Mungyeong's Master.",
    "Mungyeong is the Slaughter Saint and Dong Feng's Disciple; he has sworn never to kill again and intends to live as a medical apprentice.",
    "Hyuk Mujin and Gung Gibang remain badly wounded after fighting the Third Fiend.",
    "Cheongpung remains a Supreme Peak master at the Sichuan Tang Clan with Mimi.",
    "The Lord of Heaven temporarily possessed the Western Heaven Demon Lord's body and escaped after One Annihilation.",
    "The Myriad-Poison Ring remains in Jin Taekyung's possession and cannot be appraised by the System.",
    "A hidden cavern near Chengdu contains the inactive Moving Formation used by Dark Heaven; the Slaughter Saint identifies Dark Heaven as the successor to the Demonic Cult.",
    "Tang Sadok has awakened after prolonged unconsciousness; Jin Taekyung is preparing to leave with Jin Wikyung to escort the Third Fiend to Henan, while the Tang Clan weighs relocating its headquarters."
  ],
  "continuity_sources": [
    374
  ],
  "open_questions": [
    "What happened to the Second Fiend assigned to the Qingcheng attack?",
    "Why did Mungyeong tell the companions that Jin Taekyung ordered the rescue of Emei?",
    "What is the true nature and purpose of the Lord of Heaven, and what became of the Western Heaven Demon Lord?",
    "What was the origin and purpose of the Moving Formation, and why did it lose its power?",
    "How will Dark Heaven respond to the failed Three-Gate Bloodbath?"
  ],
  "safe_through": 374,
  "temporary_decisions": [
    "Render 열화신룡 as Blazing Flame Divine Dragon, distinct from Huashan Divine Dragon.",
    "Use Mimi for 미미 and Mimi-chan for 미미쨩; render 삼괴 as Third Fiend in singular references and Three Fiends in collective references.",
    "Render 진인 as Perfected One, 도우 as Fellow Daoist, and 신니 as Venerable Nun in forms of address.",
    "Render 환영진 as illusion formation and 이동진 as Moving Formation.",
    "Render 독룡각 as Poison Dragon Pavilion and 가주 대행 as Acting Family Head."
  ],
  "version": 1
}

## Reading copies

## Chapter artifact 370

# Chapter 370

The Sichuan Tang Clan had long been famous for its reclusive nature.

Even prominent figures could not easily come and go. And because the clan feared that a daughter who married out might leak its martial arts and secrets, they brought in a son-in-law to carry on the Tang surname.

The gates of the Sichuan Tang Clan, which had endured for hundreds of years in this manner, had been thrown wide open only seven days ago.

“Over there! Set that pillar straight!”

“Pull when I count to three. Ready. One, two—!”

Strongly built laborers pulled on ropes and carried stones and lumber.

Across the spacious grounds, buildings were slowly taking shape atop foundation stones still stained dark red with blood.

Far away, dozens of Buddhist nuns had gathered and were chanting prayers.

“May I have no other thought at the end of this life, with Amitabha alone beside me, my heart forever bound to the light from the white curl between his brows…”

The monks, their heads shaved close and their eyes filled with spiritual energy, were nuns of Emei Sect.

In front of them, countless wooden coffins burned within the flames.

“May you be reborn in the Pure Land. We will never forget your loyalty and your spirits.”

Several days and nights had passed, but the fires still had not gone out.

That was how many victims had died in the Three-Gate Bloodbath. The Sichuan Tang Clan, in particular, had suffered catastrophic losses.

“Whew…”

“Venerable Myoryeong, you look exhausted. You should rest, even if only for a little while…”

“No, Daoist Myeongjin. I am only doing what must be done, so please do not concern yourself. Let us continue.”

The Daoist gazed at the middle-aged nun’s pale complexion, then slowly nodded.

A short while later, martial artists with swords at their waists came walking in a line, carrying several dozen wooden coffins.

Among them were Daoists of Qingcheng Sect, disciples from small and mid-sized sects, and beggars with grime running down their bodies.

A group of physicians came running along behind them.

“The patient suddenly started vomiting blood? Weren’t they stable?”

“If I knew that, would I be here right now? The patient clearly suffered serious internal injuries, but I can’t make sense of these symptoms…”

“Spread out and bring the Divine Physician! Quickly!”

Emei nuns, Qingcheng Daoists, Beggars’ Sect beggars, and martial artists dispatched from sects both great and small. Along with them were ordinary people—carpenters, stonemasons, physicians, and more.

Countless people moved through the grounds of the Sichuan Tang Clan, each faithfully performing their own role.

From a tall pavilion, a young beggar watched the scene through an open window and muttered in a weary voice.

“I never thought I’d live to see something like this. And in the Sichuan Tang Clan, no less.”

Hyuk Mujin, lying on a bed, answered him.

“Stop watching and go help. Don’t slack off just because you’re the Successor Beggar.”

“Slack off?”

Gung Gibang opened his eyes wide and pointed at himself.

His upper body was tightly wrapped in spotless white bandages. One leg had been fitted with a temporary splint.

They were glorious wounds, earned while fighting the Third Fiend.

“Are you seriously saying that after looking at me? This is slacking off? Huh?”

“Are you the only one who got hurt?”

Hyuk Mujin snorted, then deliberately wriggled his body like an earthworm.

Unlike Gung Gibang, he was wrapped in bandages from head to toe, making him look like a mummy.

“You have to get hurt this badly before people say, ‘Ah, this kid must have had a rough time.’ You understand?”

“……!”

Gung Gibang shuddered.

The fact that he had not been seriously injured clearly proved that his martial arts were superior. Yet somehow, he felt as though he had lost.

“I changed my bandages five times!”

“I’m lucky to be alive. And that’s only because your body was so filthy. I heard a physician tried to scrub you clean, then passed out from exhaustion. Is that true?”

“……”

“Forget it. There’s no point talking to you anymore; all I get is bad breath. Since we’re on the subject, ask them to brush your teeth next time, too. Every time I talk to you, it feels like I’m speaking into the ass of a street mutt.”

What a vicious tongue.

Gung Gibang was speechless for a moment, then gazed up at the ceiling and lamented.

“The Third Fiend should have killed that bastard.”

“Hey. That’s crossing a line.”

“I still don’t understand how someone like you survived that battle.”

“If you’re really that curious, stick with our Captain for two years.”

“……I’ll pass.”

If there was one thing Gung Gibang and Hyuk Mujin, who were always bickering, agreed on, it was Jin Taekyung.

A man who seemed to embody every upheaval in the world.

A tenacious vitality and stubborn determination that somehow allowed him to survive any crisis.

And now, Jin Taekyung had reached such distant heights in martial prowess that they could hardly believe he was human like them.

*There is one more person like that.*

*Yeah. That guy.*

The two men thought the same thing, and their heads turned in unison toward one direction.

“Mimi, Whirlwind!”

Sssrrk!

“Good job, Mimi! This time, fly through the air!”

Sssrrk?

“Oh. You can’t do that. Then this time…”

Hyuk Mujin and Gung Gibang wondered whether the bizarre young man telling a snake to fly really was the Huashan Divine Dragon—the successor of the Sword Saint who had defeated First Fiend, the strongest of the Qilian Three Fiends, all by himself.

“Say, Young Hero Gung.”

“What?”

“Do you have to be a little unhinged to become a Supreme Peak master?”

“……I don’t know. I really don’t know anymore.”

Gung Gibang dodged the question.

His own master was rather eccentric, but not to the extent of Jin Taekyung or Cheongpung.

Then again, looking at the Sword Saint and the Fire King, perhaps disciples really did resemble their masters.

“But what exactly is that snake?”

“A snake with horns that big? Other than an imugi, there’s only one possibility. A Thousand-Year Poison Horned Snake.”

“When I was young, I read an encyclopedia of spirit creatures that described it as an extremely venomous creature that was black all over.”

Cheongpung shouted.

“Mimi! Lie down!”

Sssrrk!

“Looking at it now, it doesn’t seem poisonous. It just looks like an animal.”

“That’s what I’m saying.”

“But why is Young Hero Cheongpung here? He barely got hurt.”

“Didn’t you hear that loud crash outside earlier? They say Young Hero Cheongpung went out to help and ended up destroying a pavilion.”

“……Oh.”

The two men lost their words at the same time. They lay side by side on their beds and stared at the ceiling.

The pavilion had somehow retained its shape even after nine-tenths of the building was damaged. It was now being used as a temporary clinic for the most important patients.

Hyuk Mujin caught the scent of medicinal decoctions drifting in from somewhere and suddenly muttered,

“It feels like a dream.”

“Tell me about it.”

Seven days had passed since the Three-Gate Bloodbath.

The black-clad men of Dark Heaven who had stained every corner of Sichuan with blood had mostly been killed or captured by the net over heaven and earth formed by the united forces of Sichuan’s Murim. Even the Third Fiend, who had vanished without a trace, had been captured by a mysterious figure.

And with that, the brief war had come to an end.

But…

“I don’t think this is over. What do you think, Young Hero Gung?”

“Do you even have to ask? If this is really the end, I’ll brand my palm.”

It was a sense of crisis shared by everyone, not only the two of them.

In barely two months, Henan and Sichuan had been stained with blood.

Once news of the Three-Gate Bloodbath spread to the farthest reaches of the continent, the people of the world would realize it.

The dark cloud called Dark Heaven had already reached their doorstep.

It was the undeniable beginning of an age of turmoil, and heroes were born in such times.

Hyuk Mujin’s gaze naturally turned toward the closed door.

“When do you think our Captain will wake up?”

“Who knows? Do I look like I have an answer? According to Mungyeong, there’s nothing wrong with him, so all we can do is wait.”

“Since we’re talking about it, Mungyeong may be skilled for his age, but isn’t he a little young for us to entrust Captain to him?”

“The Divine Physician is busy, I suppose. Great Hero Jeok is still recovering his strength, and there are so many critical patients, including Great Hero Tang Sadok. There’s no helping it.”

“I understand. I do. But even if he is the Divine Physician’s Disciple, Mungyeong is a little… What could that child possibly know?”

At Hyuk Mujin’s worried words, Cheongpung abruptly lifted his head.

“Uh-oh. Don’t. You’ll die.”

“Young Hero Cheongpung?”

“What you just said—don’t say it in front of Grandpa Mun. I mean, especially not in front of Mungyeong.”

“What? Why are you suddenly saying that?”

“No. Really, don’t.”

“……?”

Hyuk Mujin and Gung Gibang exchanged bewildered looks.

Then Cheongpung suddenly sucked in a breath.

“Mimi! Where did you go, Mimi?”

At that moment, Cheongpung began desperately searching for the Thousand-Year Poison Horned Snake that had vanished during the brief moment he looked away.

From beyond the tightly closed door came a strangled shout.

“Ghk! You damn snake!”

The three men’s gazes collided in midair.

At the same time, several voices calling one person’s name rang out all the way outside the pavilion.

“Benefactor!”

“Captain!”

“Jin Taekyung!”

The people working outside caused an uproar as well.

“Did you hear that?”

“Could he have woken up?”

“Tell the Sect Leader! Quickly!”

* * *

I had a nightmare.

In an abyss of pitch-black darkness where I could not see an inch ahead, a snake slowly tightening around my neck.

I couldn’t breathe, and my vision turned white.

Then, in the next instant, I opened my eyes and exhaled the breath I had been holding.

“Ghk!”

Sssrrk.

“……?”

*Sssrrk? What the fuck?*

My brain stopped working for three seconds.

At last, I realized what my nightmare had been. I grabbed the horn of the snake tightly wrapped around my neck.

“You damn snake!”

Whether it was a Thousand-Year Poison Horned Snake or Mimi-chan, I didn’t care what its name had been. Starting today, this bastard’s name was Snake Liquor.

“You’re living on dew from now on. Chamisul.”[^1]

I was about to swing it around and slam it forcefully onto the floor when the tightly closed door exploded inward and someone came rushing through.

“Benefactor!”

Cheongpung’s thunderous shout made my skull ring.

Behind him, I saw Hyuk Mujin wriggling like an earthworm and Gung Gibang hopping along on one leg.

“Captain!”

“Jin Taekyung!”

“……Why do you two look like that?”

Hyuk Mujin bounced his body energetically and answered.

“The Third Fiend. That crazy old monster did this to me.”

Gung Gibang helpfully added an explanation.

“Surviving was a miracle. That lunatic Hyuk Mujin threw dirt mixed with stones at the Third Fiend. If the Seven Fairies hadn’t stepped in and blocked the attack, he would have been torn limb from limb.”

“……?”

Who the hell were the Three Fiends, and who were the Seven Fairies? Kim Seonja was the name of my high school student-affairs teacher…

*These lunatics.*

My relief at surviving the underground prison lasted only a moment before I pressed a hand to my forehead, feeling a headache coming on.

I had clearly told them to stay put at the Divine Physician’s residence, but they apparently could not resist crawling out and fighting to the death.

Thank goodness they had survived. What would have happened if they had died?

“Were you two desperate to die? What kind of trouble did you cause this time?”

“……?”

“……?”

“What? Why are you looking at me like that?”

The three of us, excluding Cheongpung, exchanged bewildered looks.

“Is there a problem?”

“Of course there is.”

“You told us to go save Emei Sect, Captain.”

The first answer came from Gung Gibang. The second came from Hyuk Mujin.

They were both talking nonsense, so I deliberately frowned.

“What are you talking about? I did?”

“Yes. That’s what Mungyeong told us. Did you hit your head?”

That couldn’t be it.

The moment I opened my eyes, I could feel it. Powerful qi surged throughout my entire body.

Everything before my eyes and the natural qi surrounding me felt clear and vivid.

*So this is Supreme Peak…*

I wanted to test this power immediately. And the System messages that must have piled up like a mountain by now.

But before I could keep listening to this nonsense, there was one thing I needed to ask.

“Is everyone all right?”

They knew who I meant by *everyone*.

Instead of answering, Cheongpung threw open the enormous window.

“You can see for yourself, Benefactor.”

As if in a trance, I slowly walked toward the window.

A warm spring breeze brushed across my face. An oddly quiet atmosphere greeted me as I leaned my head out beyond the window.

“Ah.”

I looked down and lost my words.

There were people below.

There were nuns, Daoists, and craftsmen who appeared to be carpenters. There were also physicians wearing spotless white robes. The emotion held in the countless gazes turned toward me was one thing.

*Awe.*

The next moment, they paid their respects as though they had made an agreement beforehand.

Some formed a fist-and-palm salute. Some bowed their heads slightly. Others prostrated themselves and bowed deeply.

A vast voice rose as one.

“We pay our respects to the Blazing Flame Divine Dragon!”

At that moment, a single shiver pierced down from the crown of my head to the tips of my toes.

Ding.

> **System**
>
> Your accomplishments and Fame will resound throughout the Central Plains.
>
> You have acquired a new sobriquet!

Along with the System alert that pierced my ears, I spotted someone in the distance.

“Well done.”

I smiled back at Jeok Cheongang.

[^1]: Chamisul is a Korean soju brand whose name literally means “true dew.”
## Chapter artifact 371

# Chapter 371

“I pay my respects to Great Hero Jin Taekyung, the Blazing Flame Divine Dragon!”

At the moment that awe-filled cry rang throughout the grounds of the Sichuan Tang Clan, Jin Taekyung was not the only one who felt a shiver run through him.

The old master watching everything from a distance had to struggle to hide his swelling emotions.

*You rascal…*

Jeok Cheongang remembered the day he had first met Jin Taekyung as clearly as if it had happened yesterday.

The Third Young Master of a frontier martial family. The young man who had only just begun making a name for himself in Shanxi had become a Hidden Dragon, and at last, he had spread his wings wide and soared into the blue sky.

*Yes. You are the Divine Dragon, and the Great Hero.*

Their eyes met, and Jeok saw Jin Taekyung grin. Leaning his upper body out the window, he waved both hands wildly.

“What’s my name?”

“Jin Taekyung!”

“And my sobriquet?”

“Blazing Flame Divine Dragon!”

“Louder—!”

“Waaaaaaaah!”

The solemn gathering flipped over all at once and became a cauldron of madness.

Jeok Cheongang burst into the laughter he had been holding back.

“Ha! Ha-ha-ha!”

His refreshing laughter mixed with the cheers. The breeze was cool, and the sky was clear.

It was the beginning of an age of turmoil, but the day a new hero was born was warm with spring.

* * *

Jeok Cheongang appeared just after the cauldron of madness had settled down.

“So many people crammed into a room as small as a grain of millet.”

“Huh? It’s not cramped at all.”

“Great Hero Jeok, there’s an empty seat over there.”

Unlike Cheongpung and Hyuk Mujin, who would have to die and come back to life before they learned to read the room, Gung Gibang was a pure-blooded beggar to the bone and moved immediately.

“Oh my, now that you mention it, it does look cramped enough to burst. I’ll step outside.”

Cheongpung and Hyuk Mujin waved at him.

“Goodbye, Young Hero Gung.”

“That fellow is finally leaving. Captain, haven’t you noticed the smell of a stray dog’s backside around here?”

I carefully nodded.

“Yeah. It was a little strong…”

“Stop talking crap and both of you get out!”

“No, I’m telling you, it really did smell…”

“Fine, fine. Don’t get so angry, Young Hero Gung.”

At Gung Gibang’s furious outburst, Cheongpung lowered his head with a dejected expression.

“Mimi. Say hello while doing a whirlwind.”

Sssrrk. Sssrrrkk!

“…What the fuck.”

Looks like Mimi had picked up some new tricks in the meantime. After putting on that flashy performance, Cheongpung was the last to leave the room.

Jeok Cheongang finally spoke.

“You reckless little brat. You certainly made quite a ruckus.”

His face was stern, and his voice was low and calm.

He really hadn’t changed at all. Seeing Jeok Cheongang act just like his usual self made me want to laugh for some reason.

“You laughing?”

“Of course I’m laughing. What else should I do, cry?”

“Hah, look at this brat. You made a spectacle of yourself in front of everyone and dragged our sect’s reputation through the mud, yet you still have the nerve to say that?”

“You were laughing pretty loudly for someone who thought that.”

“…!”

“I saw everything.”

The stern expression he had been struggling to maintain collapsed all at once. Jeok Cheongang’s head slowly turned toward the window.

“Ahem. What exactly do you claim to have seen?”

“About fifty people besides me probably saw it too. For a moment, I thought your smile had split your mouth open and you were bleeding from the corners.”

It was practically the Chinese Joker.

My finishing shot left him no room to escape. Jeok Cheongang hesitated for a long while, unable to continue, before finally muttering one word.

“…Did.”

“Huh?”

“I said you did well!”

Jeok Cheongang shouted with his face bright red, then grumbled under his breath.

The sight made the smile at my lips deepen.

Yes. That one sentence was enough.

“Thank you. It was all thanks to you, Old Master.”

“…”

What was this? His expression seemed strangely off.

His eyes even looked almost hurt. I asked, baffled,

“What’s wrong this time?”

“Nothing. It’s nothing.”

“Your expression doesn’t really look like nothing…”

“I said it was nothing!”

“Why are you shouting? The mood was finally warm and pleasant for once.”

“If I say it’s nothing, then take it as nothing! You keep prying and asking questions, so this is happening!”

“Uh-oh. It’s getting worse?”

What was wrong with this man all of a sudden? Had I made some kind of mistake?

It was just as I tilted my head in confusion.

Ssssh.

Two presences were coming up the stairs.

Their footsteps were so light and graceful that I might not have noticed them if my senses had not grown even keener after crossing the threshold.

*They’re both incredible masters.*

Two Supreme Peak masters, just like that?

After everything I had been through lately, my body moved on its own.

But when I clenched my fists, Jeok Cheongang stopped me with a glance and waved his hand.

A thin stream of hot air gently pushed open the closed door.

“You people are impatient. Couldn’t you wait fifteen minutes before coming swarming in?”

An old Buddhist nun and a Daoist answered Jeok Cheongang’s gruff voice in turn.

“Impatient? Hearing that from a lay devotee gives this poor nun a rather strange feeling.”

“This junior was discourteous. However, given the circumstances…”

The old nun had a face covered in fine wrinkles, and I had never met her before. But I immediately recognized the Daoist.

I cupped my hands toward him.

“Greetings, Perfected One.”

“It’s good to see you again, Fellow Daoist Jin.”

The old Daoist was Cheongpung the Ancient Sword, the Sect Leader of the Qingcheng Sect whom I had once visited to ask for help in finding the Divine Physician.

*Then this nun must be the Sect Leader of Emei Sect… Who is she?*

I knew a fair amount about famous masters by now, but I wasn’t familiar enough with the internal affairs of every sect to know them in detail.

Especially not a Sect Leader who had only recently taken office after the death of the Heaven-Shaking Venerable Nun.

As though he had read my thoughts, Jeok Cheongang sent me a quiet message through Sound Transmission.

*That old hag is the Extinction Divine Nun of Emei Sect. She looks kind enough, but the moment she loses her temper, she’s a rakshasa incarnate. Watch what you say. And don’t even open your mouth about her age.*

I replied cautiously through Sound Transmission.

*Just how advanced in years is she?*

*Older than this old man. She was also the Heaven-Shaking Venerable Nun’s Senior Aunt.*

*Oh.*

I didn’t know Jeok Cheongang’s exact age, but I did know he was over a hundred years old. Add in the force suggested by her sobriquet…

I bowed deeply to the old woman who looked like the owner of a bossam restaurant.[^1]

“Greetings! My name is Jin Taekyung!”

“Good to meet you, Benefactor Jin.”

The Extinction Divine Nun studied me with a strange look in her eyes, then nodded.

“So the rumors were true. No—in fact, you’re even more than they said.”

Cheongpung the Ancient Sword smiled faintly and continued,

“Isn’t it truly astonishing?”

“The waves behind push the waves ahead on the Yangtze. It seems the younger generation intends to push even old people like us aside. To cross the threshold at such a young age…”

“It isn’t only him, Venerable Nun. There is also a young man named Cheongpung.”

“Ah, you mean the Sword Saint’s successor?”

“Yes. This poor Daoist lacks the ability to judge which of the two is superior, but both young men are unquestionably heaven-sent. They are a great blessing to the Murim.”

“Oh…”

Interest and surprise flickered across the two faces marked by fatigue.

Feeling awkward, I rolled my eyes around. That was when Jeok Cheongang stepped in front of me.

It didn’t make much difference, considering the enormous difference in our heights.

“You’re going to wear out the boy’s face. Say what you came to say and hurry up.”

The two Sect Leaders looked embarrassed by his blunt words and finally got to the point.

“A problem has arisen. Could the two of you accompany us for a while?”

“It won’t take long. You have my word.”

“Accompany you? Right now?”

Jeok Cheongang asked in a displeased voice as he turned toward me.

“What will you do?”

“…”

Two Sect Leaders from the Nine Sects and One Gang were asking for my help. What exactly was I supposed to do?

“I’ll go.”

I felt light enough on my feet, and accompanying them would let me hear what had happened so far. I had no particular reason to refuse.

At my ready agreement, the two Sect Leaders took the lead and started walking.

Then Jeok Cheongang suddenly spoke.

“But why isn’t one of them here?”

“He’s waiting below.”

“He said he didn’t want to attract the attention of the other people.”

One of them? If he was important enough to be part of this group, was it Tang Sadok, the Family Head of the Tang Clan?

*Well, whoever it is, I’ll see him soon enough.*

But my curiosity vanished without a trace the moment we left the pavilion and ran into one person.

The familiar face immediately drew a delighted shout from me.

“Hey, you bastard! Mungyeong!”

Mungyeong looked exactly as he had before leaving the Sichuan Tang Clan.

Dark Heaven had invaded not long after he left, so I had been worried. Yet, perhaps our paths had simply missed each other, because he had somehow escaped without a scratch.

“When did you get here? You look taller than before. Are you going through a growth spurt?”

“…”

“Why are you so quiet? Are you in a bad mood? Maybe…”

I ruffled Mungyeong’s hair, then leaned in and whispered,

“Did you have a wet dream this morning?”

“…”

“You did. You totally did.”

The little brat. Look at him saying nothing because he’s embarrassed.

I smiled with satisfaction.

It was something that happened from time to time at that age. This would be a good chance to spread some proper sex education through this dusty old Murim.

“Your hyung here is going to show you a whole new world. From now on, call me Teacher Jin Seong-ae.”[^2]

Teacher Gu Seong-ae, are you watching? Your knowledge is crossing space and time to reach the next generation.

I was patting Mungyeong’s shoulder with a proud smile when—

“Uh…”

“Um…”

“Oh dear… We forgot to tell him that.”

Forgot to tell me what?

Three deep sighs came from behind me. At the same time, a flat voice emerged from between Mungyeong’s lips.

“Take your hand off.”

“…Huh?”

“And wet dreams ended a long time ago.”

“That’s a little problematic, because your secondary sexual development hasn’t completely finished ye—no, that’s not what I mean.”

I swallowed hard.

A terrifying possibility had suddenly flashed through my mind.

“Who… are you?”

Mom, I’m scared.

* * *

“And that is how things came to this.”

“It truly is a bizarre matter.”

Even while the two Sect Leaders used their movement techniques at tremendous speed, their voices did not waver.

They looked to me for an answer, and I forced my lips apart.

“Oh, right. So there’s some weird formation at the place we’re going?”

“According to the Third Fiend, whom we captured and interrogated, that appears to be the case. But the formation itself is so strange…”

Jeok Cheongang replied in a gruff voice.

“This old man and this brat are both hopeless at formations. We wouldn’t understand anything even if we looked at it.”

I agreed. The Fire Gate Cavern on Mount Jiuhua had a formidable Mystic Gate Formation installed inside it, but that didn’t mean we were experts in formations.

*We should call in someone like the Zhuge Clan instead.*

But it would take a considerable amount of time for the Zhuge Clan to arrive.

For some reason, the two Sect Leaders seemed to have high expectations of us.

Especially me.

“Fellow Daoist Jin, did you notice anything else strange about that man? Anything he said or did?”

“I’ve told you everything. And from what I could tell… I don’t think he could get any stranger than that.”

Dark Heaven was strange by nature. They were fanatics who worshiped the Lord of Heaven as almost—no, simply—as a god.

The powers and bizarre abilities shown by the Blood Lord and the Western Heaven Demon Lord were no different.

*Regenerating like a human Troll, taking an arm off and sticking it back on as if it had double-sided tape on it—and finally, even possession.*

The more I thought about it, the more miraculous it seemed.

The fact that we had fought those people and won.

“Before you woke up, we heard the general situation from Benefactor Jeok. Once the messenger eagle we sent to Henan returns with a reply, we should have a better idea of how to proceed.”

“If you notice anything strange when you inspect the formation, be sure to tell us.”

“Yes.”

As I answered, I glanced toward the figure moving far ahead of us.

Mungyeong.

No—the man known by the sobriquet Slaughter Saint.

*Fuck. Why is the Slaughter Saint here?*

To be honest, I almost pissed myself.

*Even if I spent half a day swimming in the Sanzu River valley, grilled meat, and came back, it wouldn’t be this bad.*[^3]

*Mungyeong was the Slaughter Saint. And I asked the Slaughter Saint if he’d had a wet dream!*

Teacher Gu Seong-ae, I nearly died because of you.

I was secretly letting out a sigh of relief when the dense undergrowth around us began to disappear, revealing towering cliffs ahead.

[^1]: Bossam is boiled pork commonly wrapped in salted napa cabbage and served with condiments; a bossam restaurant owner is a familiar image of a hearty Korean neighborhood eatery.

[^2]: Gu Seong-ae is a Korean sex educator. Taekyung is parodying her name by replacing Gu with Jin.

[^3]: In Buddhist tradition, the Sanzu River is associated with the boundary between life and death.
## Chapter artifact 372

# Chapter 372

“This is the place.”

“It’s a cliff, isn’t it? A pretty ordinary one.”

I stopped in front of the steep cliff with the others and looked around.

The cliff was over a hundred zhang high and made entirely of solid rock, but there was nothing particularly special about it.

*There’s supposed to be a formation here?*

However, it didn’t take long for my question to be answered.

Following the strange sense of déjà vu I suddenly felt, I walked slowly until I stopped in front of a yellowish-brown rock wall.

“This is…”

Everything has a flow and a grain. Even something as invisible and untouchable as qi cannot escape that principle.

And the senses I had honed after reaching the Supreme Peak realm were more than enough to detect the unnatural flow of qi.

“A formation?”

A voice answered my mutter.

“More precisely, an illusion formation.”

Mungyeong—or rather, the Slaughter Saint—stepped forward and extended a hand after scanning my face with dry eyes.

Along with the tremendous movement of qi, the solid rock wall vanished like mist, revealing the entrance to a dark cavern.

“You’re not completely blind, at least.”

“Uh, what?”

“Don’t ask again.”

The Slaughter Saint tossed out that one remark and walked toward the cavern without even giving me time to respond.

*Was that an insult or a compliment?*

It left a strangely unpleasant feeling.

But even so, getting angry would have been awkward. There was no hostility toward me in the Slaughter Saint’s words or actions. They were merely as dry and stiff as the way he treated everyone else.

So instead of making the listener angry, his words could only leave them feeling awkward.

“…”

Of course, the identity of the person saying it had something to do with my willingness to let it slide.

What else was I supposed to do if that was just how the Slaughter Saint was? Even if it bothered me a little, I had to put up with it.

Considering that I was still standing after bringing up wet dreams, I should be grateful.

*I nearly turned the Slaughter Saint into the Rice Saint, so this is practically getting off easy.*[^1]

I was thinking that when I heard a low chuckle from beside me. I turned my head and saw Jeok Cheongang twitching the corners of his mouth.

“Why are you laughing all of a sudden?”

“Nothing. I was just thinking that the Slaughter Saint is remarkably incapable of being honest.”

“What?”

“Don’t ask again.”

“…”

What was this? Was it some new catchphrase?

After saying that, Jeok Cheongang strode away. The two Sect Leaders and I followed him into the dark cavern.

*Come to think of it…*

I couldn’t believe a place like this had been hidden here.

It was even close enough to reach from Chengdu, the heart of Sichuan, in half a day. That was at an ordinary commoner’s walking pace, so people who knew martial arts could get here much faster.

I walked through the seemingly endless cavern, looking around.

*The entrance alone is huge. It’s several times larger than the underground prison beneath the Sichuan Tang Clan.*

I had heard a brief explanation on the way here. The murderous criminals of Dark Heaven had stayed in this very cavern.

So this was where they had been hiding and waiting for the right moment. That explained where so many of them had appeared from.

*But how did they get in here in the first place?*

There had been over three hundred enemies who attacked the Tang Clan under the Western Heaven Demon Lord’s command.

If the ones who went to Qingcheng and Emei were added to that number, it became a force that couldn’t be ignored.

*Was security in Sichuan Province really that terrible? No, even so, wouldn’t the Beggars’ Sect and the Lower District Sect have noticed them?*

I had been walking with that question in mind for who knew how long when the passage—wide enough for ten grown men to walk abreast—finally ended, revealing a new space.

Without meaning to, I muttered,

“…Huh. Look at this.”

The area was large enough to accommodate well over a thousand people. Dozens of night-shining pearls embedded in the ceiling cast a soft glow, while jars and containers full of dry rations and fasting pills, along with weapons, were stacked in one corner.

But that wasn’t what surprised me most.

*What is that?*

Strange patterns covered the entire floor of the cavern.

Carved in regular arrangements like intricate gears, they looked like the ruins of an ancient kingdom forgotten long ago.

“Is that perhaps the thing you mentioned earlier…?”

At my question, Cheongpung the Ancient Sword, the Sect Leader of the Qingcheng Sect, nodded gravely.

“That is correct. That is the strange formation I mentioned.”

I had wondered if that was really what they were talking about, but it was actually a formation.

I had experienced various mechanisms and formations at the Star-Array Grand Banquet, but I had never seen anything so large or strange.

*This has gone beyond strange and become downright malformed.*

Perhaps it was because of the patterns, which looked mysterious yet dangerous.

Jeok Cheongang seemed to have the same thought and spoke up.

“But what in the world are those bizarre patterns?”

“We have not yet been able to determine that either.”

Extinction Divine Nun added to Cheongpung the Ancient Sword’s words.

“We cannot make a hasty judgment at this point. We copied part of the formation and showed it to several learned scholars and famous figures, but none of them recognized it. We also cannot completely rule out the possibility that it is writing from the Western Regions, unknown to anyone here.”

But then, before I knew it, a sentence slipped out between my lips.

“Uh, that isn’t writing.”

“…”

“…”

“…”

Everyone’s eyes turned toward me. The Slaughter Saint, who had remained silent ever since we entered the cavern, suddenly spoke.

“What is your basis?”

“My… basis?”

“If you claim that so confidently, there must be a sound reason. Answer me without asking another question.”

Of course I had a reason. A solid reason that neither a renowned scholar who had accumulated knowledge by reading tens of thousands of books nor a famous martial artist who had traveled throughout the Murim all his life could refute.

*The Integrated Language Pack.*

The *Integrated Language Pack* translated every language automatically through the power of the System.

With it, communication wasn’t the only thing I could manage. I could also read and write.

It was thanks to the *Integrated Language Pack* that I had been able to speak with the Skeleton Warlord in the modern world.

Yet even though its interpretation function was always active like a passive Skill, the patterns forming the formation had remained exactly as they were.

That was definitive proof that those patterns were not writing.

The problem was…

*How am I supposed to explain that?*

I shouldn’t have said anything. I should have just kept my mouth shut.

But it was already too late. As the Slaughter Saint’s gaze grew more intense, I stammered,

“Bo… bo.”

“Boobs?”

The Rice Saint’s eyebrow twitched. It was the first emotion he had shown. He had clearly remembered the wet-dream incident.

“Ah, no, not boobs.”

“Then breasts?”

“…”

Please. Don’t say things like that with a face that didn’t show a single trace of emotion.

“No, that’s not what I meant.”

I was waving my hands frantically when Jeok Cheongang suddenly interrupted.

“Are you threatening my Disciple? How dare you threaten the heir of the Fire King and the Young Sect Leader of the Fire Gate Clan?”

“Threatening him? It isn’t necessary, but it isn’t beyond me either.”

“I was trying to let it pass out of gratitude for the favor of saving my life, but if you, Mun, are going to act like this, then this old man cannot remain still either.”

As the atmosphere grew increasingly hostile, I squeezed my eyes shut and shouted,

“I guessed!”

“…”

“…”

“…”

“I think I saw something like it in a book before… and it just felt like it wasn’t writing, so I guessed.”

A heavy silence settled over the cavern.

The Slaughter Saint let out a barely audible sigh before asking Jeok Cheongang,

“So that fellow is the heir of the Fire King and the Young Sect Leader of the Fire Gate Clan?”

Jeok Cheongang was silent for a moment before answering.

“Now that I think about it, he never went through the formal initiation ceremony.”

“…”

“So strictly speaking, he isn’t an official Disciple of our sect. In other words, he should still be considered a member of the Jin Family of Taiyuan…”

Jeok Cheongang’s eyes met mine, and he quietly looked away.

“That will be all.”

“…”

What did he mean, that would be all? He had already said everything there was to say.

Extinction Divine Nun and Cheongpung the Ancient Sword had just witnessed the complete destruction of trust between Master and Disciple. With awkward expressions, they changed the subject.

“Ahem. In any case, it seems we will have to continue investigating this strange formation.”

“F-Fellow Daoist Jin and Senior Jeok’s insights were a great help.”

Heaven and earth knew that they hadn’t helped at all. Everyone here knew it, too.

Even a stray dog in a back alley wouldn’t believe that.

After bringing the situation to an end with that unbelievable statement, Cheongpung the Ancient Sword spoke to Extinction Divine Nun with a troubled expression.

“More importantly, this is truly unbelievable. To summon such a large number of people with nothing but a formation. Honestly…”

“Indeed. If such a thing is possible, does that not mean they could appear anywhere throughout the land?”

Wait. What did they just say?

I had been staring at the ground, frustrated by my inability to explain myself and still suffering from the aftermath of the boob incident. I abruptly raised my head.

“What is the matter, Benefactor Jin?”

“No, it’s just… I think this is the first time I’ve heard the two of you mention something about the formation.”

“Hmm? You mean the Moving Formation?”

“…The Moving Formation?”

“That is correct. According to the Third Fiend, that strange formation is called a Moving Formation. We cannot know how much of their absurd story to believe, but they say Dark Heaven used that formation to leap across hundreds of li.”

A Moving Formation. They said it was a Moving Formation.

Even if a critic wearing angular horn-rimmed glasses had suddenly walked out and announced, “This formation gets four and a half stars,” I wouldn’t have been any more bewildered than I was now.

*This sounds familiar.*

A formation that could move hundreds of people across hundreds of li.

The more I thought about it, the harder my heart pounded and the drier my lips became.

What if this formation called a Moving Formation was *that thing* I was thinking of?

*No, that can’t be.*

But despite my desperate denial, my Adam’s apple bobbed heavily.

“Is this formation still operational?”

I had asked the two Sect Leaders, but it was the Slaughter Saint who answered.

“The Third Fiend. I caught him here myself.”

“…He tried to escape through the Moving Formation.”

“That was his intention. But that was all it was.”

“What do you mean?”

“According to what he later confessed, he tried to activate the formation, but nothing happened.”

“Oh.”

“One thing is certain. No flow of qi can be felt from that formation. It has completely lost its power and is now nothing more than an empty shell.”

After explaining in his flat voice, the Slaughter Saint added one more thing.

“Judging from the circumstances that have come to light, Dark Heaven is without a doubt the successor to the Demonic Cult. The Demonic Cult possesses countless monstrous martial arts and supreme techniques, so it would not be strange if they had any number of bizarre arts.”

I had heard what sort of place the Demonic Cult was so many times that it had practically been beaten into my head.

A powerful religious organization that could be called demonic, heterodox arts incarnate.

Although it had ultimately lost the Great Faction War, the reason it had been able to overwhelm the Murim of the entire land for so long was because of the monstrous martial arts and supreme techniques it possessed.

*So this formation is one of the countless bizarre techniques passed down from the Demonic Cult?*

No matter how much I thought about it, I couldn’t figure it out. Maybe it was because this was a trope I’d seen so often in the fusion-fantasy novels I had read before. Somehow, that only made it more confusing.

*They got away with it just fine in* Mukhyung. *Ugh. I shouldn’t have read a novel that never even got an ending.*

Even so, just in case, I decided to memorize the formation’s arrangement and patterns.

I was staring intently at the Moving Formation and carving it into my mind when the Slaughter Saint suddenly spoke.

“Judging by your attitude, you seem to know something. Does it remind you of anything?”

“…”

What excuse was I supposed to make?

[^1]: In Korean, *sal* means “slaughter,” while *ssal* can mean “rice” and also evokes *ssada*, slang for ejaculating—tying the wordplay to the wet-dream incident.
## Chapter artifact 373

# Chapter 373

The trip back was short.

On the way there, we had at least slowed down to exchange information. But if you put it in game terms, this was a deluxe party with no fewer than five Supreme Peak masters traveling together.

The distance that would have taken an ordinary person half a day had been reduced to almost nothing.

“You’ve worked hard, Benefactor Jin.”

“And you must still be tired. Thank you for coming with us.”

When the two Sect Leaders spoke to me as we neared the Sichuan Tang Clan, I shrugged.

“It’s nothing. I didn’t really help much, anyway.”

“That’s true.”

“He didn’t.”

“…”

It was true that I hadn’t been much help, but wasn’t that a little harsh?

Cheongpung the Ancient Sword gave me a faint smile before clasping his hands toward the Slaughter Saint and Jeok Cheongang.

“I’m grateful to both of you Seniors as well. I’m sorry for making you come all this way for nothing.”

The Slaughter Saint and Jeok Cheongang answered at the same time.

“It was a pointless trip.”

“Next time, don’t do anything you’ll need to apologize for. Understood?”

“…Ah. Yes.”

That was exactly how I felt.

The Slaughter Saint continued, addressing the visibly uncomfortable Cheongpung the Ancient Sword.

“And… I hope you won’t come looking for me in the future.”

He wasn’t telling us to call on him sparingly because it was bothersome. After briefly returning as the Slaughter Saint, he was trying to go back to being the young medical apprentice, Mungyeong.

Everyone here understood what he meant.

The two Sect Leaders were the most flustered of all.

“S-Senior, you mean…”

“Benefactor, might you reconsider?”

But instead of answering, the Slaughter Saint gave them a dry look.

After a moment of silence, Cheongpung the Ancient Sword and Extinction Divine Nun nodded with small sighs.

“…We will do so.”

“I shall respect your wishes. For now.”

For now.

Those last words carried unusual emphasis. A quiet voice slipped from between the Slaughter Saint’s lips.

“My decision has not changed. Coming this time was nothing more than a passing whim.”

It was a firm answer that left not even the slightest room for argument. The Slaughter Saint’s gaze shifted toward Jeok Cheongang and me.

“I trust you two understand that as well.”

Jeok Cheongang suddenly spoke.

“Are you planning to pretend to be a medical apprentice again, despite how ill-fitting it is?”

“It isn’t an act. The Slaughter Saint no longer exists. Only a medical apprentice remains.”

“Even if a tiger wraps itself in goatskin, can you call it a goat?”

“If it hides its teeth and claws, even a tiger can become a goat.”

“But you revealed your claws in the end. Didn’t you?”

A shallow crease formed between the Slaughter Saint’s brows.

“You’ve grown more talkative with age. You owe me a debt, after all.”

“…Damn. I can’t argue when you aren’t wrong.”

“I’ll take that as an answer.”

After dismissing Jeok Cheongang’s remark, the Slaughter Saint glanced at me.

“And you?”

“Me?”

“Who else is left?”

“No, that’s not what I meant. Do I get a choice?”

“Of course. There are two choices.”

The Slaughter Saint spoke with an impassive expression.

“First, you can loudly announce that the young medical apprentice named Mungyeong is actually the Slaughter Saint, then be found dead without a soul knowing how. Second, you can keep your mouth shut so no one notices, treat me as you did before, and leave quietly.”

“…”

“Which will you choose?”

Wow. The choices were so difficult that I was speechless for a moment.

After swallowing hard, I opened my mouth.

“The second one.”

“Good thinking.”

“Yeah.”

The Slaughter Saint had been about to nod at my prompt answer when he suddenly stopped.

“What did you just say?”

“Why?”

“What?”

“No, I mean, why are you acting like that? You told me to treat you as I did before.”

“…”

“…”

The two Sect Leaders stood there with their mouths hanging open. The Slaughter Saint was silent for a moment before asking Jeok Cheongang, who had begun chuckling.

“Is this guy insane?”

“He’s always been like that. Gives you a headache, doesn’t he?”

“I want to smash his skull in.”

I quickly bowed before he could make good on that threat.

“Ah, I made a mistake for a moment. I apologize.”

“Not even a dog would believe that, but I’ll let it slide this once.”

Had it been too obvious that I was trying to mess with him while pretending it was a mistake? The Slaughter Saint glared at me with narrowed eyes before speaking.

“In any case, be careful from now on. Aside from the people here, no one knows the truth about me. Ah, that boy Cheongpung is an exception. My Disciple is an exception as well, of course.”

“Young Hero Cheongpung knew too?”

“Yes. Everyone who saw me that day is dead, except for him.”

Now that was some clean-up.

I finally understood why there hadn’t been a single prisoner at the Sichuan Tang Clan.

The masked Slaughter Saint. Once the mask came off, every panelist and audience member alike dropped dead.

*Come to think of it, this feels stranger the more I think about it. Mungyeong was the Slaughter Saint all along.*

Memories from the first time I met him on the Yangtze until now flashed through my mind.

Which of the sides he had shown me was real, and which was a lie?

The innocent young medical apprentice I had known no longer existed. There was only the greatest assassin under heaven, with a pair of dry, emotionless eyes.

Before I knew it, a question escaped my lips.

“Why do you try so hard to hide yourself?”

The Slaughter Saint, who had been walking toward the Sichuan Tang Clan now visible in the distance, came to an abrupt stop.

After a short silence, an unexpectedly calm answer reached me.

“Because I’m sick to death of the Murim.”

“That’s why you left?”

“Yes. I swore to the heavens that I would never take another life.”

In this place—the Murim—assassins were despised.

They weren’t welcome among the orthodox factions, or even among practitioners of the demonic, heterodox arts.

They were considered people born solely to kill, rather than martial artists pursuing higher realms of martial arts.

How much blood had an assassin spilled and been stained by before earning the sobriquet Slaughter Saint?

I thought I understood his feelings to some extent.

But…

“On the other hand, I’m a little curious.”

“What?”

“Why you returned to the Murim you hate so much.”

“…What nonsense are you talking about, saying I returned?”

The Slaughter Saint’s eyes sank deeper.

“It was a choice I had no way around. An unavoidable one.”

“I don’t know. If that’s how you put it, I have nothing to say. But it seems like you made at least a few choices yourself. For example…”

I scratched the back of my head and continued.

“You asked to travel with some martial artists you met on the Yangtze because you were headed in the same direction. A few days later, you happened to run into them again and casually revealed your identity. Or you borrowed my name to order the Successor Beggar of the Beggars’ Sect to rescue Emei Sect, while you went to Qingcheng…”

“Enough.”

“Yes. I was about to stop anyway. Now that I’ve listed them one by one, there are quite a few.”

“What is it you want to hear? That I should have stood by and watched countless people—including you and your Master—die?”

“Of course not. I’m truly grateful, Great Hero.”

I wasn’t being sarcastic. I was one hundred percent sincere.

If he hadn’t stepped in at the right moment, countless people would have died or been injured.

Jeok Cheongang and I would certainly have been among them.

But the Slaughter Saint’s response to my words was as dry as desert sand.

“Don’t call me Great Hero.”

“Then what should I call you?”

The Slaughter Saint stared at me without speaking, then turned away.

As he took a step toward the Sichuan Tang Clan, which looked like a large dot in the distance, he glided forward like a ghost.

The boy’s voice scattered through the wind.

“Mungyeong. That is enough.”

Was it really enough?

Only he knew the answer.

I shrugged and replied,

“Yeah, got it, Mungyeong.”

“…!”

At that moment, the figure walking ahead of us stumbled.

* * *

When I returned to the pavilion, two leeches latched onto me.

One was Hyuk Mujin, whom I could never decide was my right arm or my pinky. The other was a beggar whose skin had gotten a little whiter, as if he had started scrubbing off some dirt lately.

“Why is Mungyeong like that? He somehow seems a little gloomier.”

“That’s understandable. His Master, the Divine Physician, was injured, and there are so many patients waiting for treatment.”

“Oh, I see. But, Captain, where did you go with Mungyeong?”

“Isn’t it obvious he took the kid out for some fresh air because he looked down? Why are you so stupid?”

“Huh. In all my life, I never thought I’d hear that from a beggar. I may look like this, but I’ve read several hundred books. I’ve never been called stupid before.”

As far as I could tell, both of them were just stupid.

I swallowed the words *Slaughter Saint* that were circling the tip of my tongue. Those two probably wouldn’t realize Mungyeong’s true identity even if they died and came back to life.

*Then again, with acting skills like that, anyone would be fooled.*

The instant people’s attention turned toward him, the Slaughter Saint returned to being Mungyeong.

No one suspected his identity just because the cheerful young medical apprentice seemed a little gloomier than usual.

No one could even have guessed.

“I’d give you credit if you’d read the Four Books and Three Classics, but all you’ve done is read martial arts novels nonstop. What books are you talking about?”

“I’ve read romance novels too. Don’t you know Gwiyeommi?”[^1]

“Wait. Gwiyeommi? Are you talking about the writer who wrote *The Temptation of a Young Prodigy*, *That Bastard Was Strong*, and so on?”

“Oh, you know him.”

“Of course I do. When I was a one-knot Disciple, I used the money I’d begged for to rent one of those and got beaten black and blue by the gang boss. If I ran into that bastard now, I’d lay into him with the Dog-Beating Staff Technique. I’d—”

*Whack!*

“Gah!”

“Aagh!”

I kicked both their asses—the two idiots happily sharing their memories—and sent them out before slamming the door shut.

I didn’t know why those bastards had come here to make a racket when I already had more than enough to think about.

*Finally, some peace and quiet.*

Cheongpung was probably running around all over the place by now, and Jeok Cheongang had told me to get a full day of rest. No one would come looking for me for a while.

I lay down on the soft bed and decided to take care of something I had been putting off.

*Check unread messages.*

Ding. Ding. Ding-ding!

System windows filled the air amid the endless chimes.

This had happened a few times before, but this had to be a new record.

Speechless for a moment, I began checking the important messages one by one.

> **System**
>
> You have reached the **Supreme Peak** realm!
>
> You defeated **Lv. 170 No Gunbaek**!
>
> Quest **Uninvited Guest** successfully completed!
>
> You have acquired a tremendous amount of **EXP** and **Fame**!
>
> System messages have exceeded the limit. Acquired EXP and Fame are being totaled.
>
> You have reached **Lv. 120**!
>
> Your Fame has surpassed the threshold. You acquire a new sobriquet!
>
> Through battles that brought you to the brink of life and death, you gained enlightenment on your own. The realms of all martial arts have risen greatly, and you can now use new martial arts!
>
> **Fire Gate Divine Technique** has reached the eighth stage!
>
> **Flame Divine Palm** has reached…
>
> **Fire Dragon Divine Spear**…

An endless stream of handshaking requests—no, messages.

My eyes started spinning just from skimming through them.

“…Holy shit.”

What was all this?

I was almost stunned to discover that half of the unread messages still remained.

Just as I scrolled down to see how many were left, something unusual caught my eye.

> **System**
>
> A new Item becomes bound to you.
>
> Currently bound Items: **White Flame**, **???**
>
> This Item has not yet been given a name. If you give it a new name, it will become completely bound to you and can be summoned through your Inventory from anywhere.

“This pops up here…”

The Modern World and Murim inventories were separate. However, bound Items like White Flame weren’t restricted by space and could be pulled out and used anywhere.

White Flame alone had been leaving me wanting more, so this was quite a stroke of luck.

*If they’re giving it to me, I’ll gladly take it.*

I was just about to check my Inventory, brimming with anticipation, when—

Knock, knock, knock.

A knock sounded on the door, and someone poked their head inside.

“Captain. It’s me, Mujin…”

“Get lost.”

“No, that’s not what I meant.”

“Hyung’s busy. Go read some Gwiyeommi novels.”

“Oh, Captain, you read them too?”

“…You little bastard, seriously.”

This wouldn’t do.

Before cracking open the Item, I’d have to crack that bastard open first.

I shot up from the bed, and Hyuk Mujin hurriedly shouted,

“Henan! It’s Henan!”

“What?”

“An investigation team has come from Henan! They’re looking for you, Captain.”

“…An investigation team?”

I frowned at Hyuk Mujin’s completely contextless explanation.

Ding.

A familiar alert reached my ears.

[^1]: *Gwiyeommi* (貴艶美) is a literary pen name meaning “precious, bewitching beauty.”
## Chapter artifact 374

# Chapter 374

Tang Horyong, the Master of Poison Dragon Pavilion, rose from his seat to greet his guest.

An imposing man had just opened the door and entered, and an indescribable pressure radiated from him.

“You’ve worked hard coming all this way.”

“Compared to what the Sichuan Tang Clan has endured, it was nothing. Let me once again express my deepest condolences.”

Despite his rough features, the man’s voice was low and gentle. At the same time, it possessed a force that compelled listeners to pay attention.

*The aura possessed only by a leader who commands others, perhaps?*

The man’s eyes were gentle yet deeply settled, and they suddenly reminded Tang Horyong of someone.

*This feels like facing another older cousin…*

That realization left Tang Horyong more than a little flustered.

He had heard that the man before him was still young—not yet forty.

His older cousin, on the other hand, was an extraordinary figure not only in age but also in his standing within the Murim.

He was also an iron-willed Family Head who had accomplished countless military feats during the Great Faction War and rebuilt his fallen family stronger than ever.

Tang Sadok, the Myriad-Poison Asura.

Tang Horyong, the Acting Family Head of the Sichuan Tang Clan, inwardly sighed as he thought of his older cousin, who still had not regained consciousness.

*Please wake up soon and lead us, Family Head.*

Tang Horyong had been born a martial artist.

He prided himself on having mastered the use of poison and hidden weapons, but leading a family was an entirely different matter.

Especially lately, countless problems had been pouring in from every direction, leaving him no time even to think about the grief and anger caused by the loss of his blood relatives.

*It would have been nice if someone like this had been in my position instead.*

In that sense, Tang Horyong couldn’t help envying the man before him.

He wasn’t judging him solely by his first impression. He had already heard plenty of rumors about the man.

Even if only a quarter of those rumors were true, the man clearly possessed the ability to lead a family.

“Sir Tang, is there something on my face?”

“Ah, no. I was so distracted that I committed a discourtesy. My apologies.”

At Tang Horyong’s hurried apology, the man nodded with a solemn expression.

“Not at all. It’s understandable. You’ve suffered something so devastating.”

In truth, even the word *devastating* was insufficient to describe the damage suffered by the Sichuan Tang Clan.

Nearly ninety percent of the clan’s people had died, and most of the Tang Clan’s grounds had been destroyed.

The fact that the family line had survived was their only consolation. It would take an extraordinarily long time to restore the clan to its former glory.

“The fellow martial artists of Sichuan have been stepping forward to help us, but… I’m worried about what comes next.”

If Tang Sadok, the Family Head, had been in his position, he would never have shown weakness under any circumstances.

Tang Horyong was different.

At his honest words, the man gently ran his long fingers over his teacup.

“I believe you know why I came here, Sir Tang.”

“I understand that you came to investigate the Three-Gate Bloodbath.”

“To be precise, when I first left Henan, my purpose was to find the culprit who murdered the late Poison King Tang Sadok and the Heaven-Shaking Venerable Nun. However, the situation changed drastically on the way here.”

“That’s right. Dark Heaven, those bastards beyond the pale, finally revealed their fangs.”

“Although there was a precedent in Henan, the fact that they so boldly attacked three famous and powerful clans and sects known throughout the land all at once is proof that war has reached our doorstep.”

Small disturbances give birth to greater disturbances.

But Dark Heaven’s existence could no longer be concealed, nor was there any reason to hide it.

Seven days and seven nights had passed since the horrific day of the Three-Gate Bloodbath.

By now, word of mouth would be racing a thousand miles, and countless messenger pigeons would be flying to every corner of the realm.

And war, rather than mere chaos, had brought people together.

“I heard that the orthodox Murim of Henan is rallying in the aftermath of the Shaolin Bloodshed. In that case, perhaps…”

“For now, it is only in the preparation stages. But it is a foregone conclusion.”

The man continued in a weighty voice.

“That is why I ask: would you consider going to Henan?”

“Henan.”

“Yes. The thing you’re thinking of is going to happen soon.”

After a brief silence, Tang Horyong spoke.

“I’m grateful that you invited us to such an honorable occasion, but I cannot leave at present. As you know, as the Acting Family Head, the members of our family…”

“Sir Tang.”

“Please, go on.”

“As you just said, you are the Acting Family Head. Naturally, you cannot leave the members of the Tang Clan behind.”

“…”

Only then did Tang Horyong understand the meaning behind the man’s proposal. His mouth fell open.

It was something he had never dared even consider.

“So you’re saying that we should move our family headquarters?”

“Well…”

The man’s clear eyes, as if they could see straight through a person, turned toward Tang Horyong.

“Great Hero Mae Jonghak told me something. He said that a war even greater than the Great Faction War would soon break out.”

“The Sword Saint…”

Tang Horyong swallowed a groan.

That could not be the opinion of the Sword Saint alone.

The Shaolin Bloodshed had awakened the anger and vigilance of countless orthodox martial artists, and the new Murim Alliance had already finished preparing to emerge.

The entirety of the orthodox Murim was preparing for the war that would soon arrive.

*Can our family survive in a situation like this?*

The question flashed through his mind, and his heart sank.

The Sichuan Tang Clan had already suffered the greatest blow in its history.

Moreover, the Qingcheng Sect and Emei Sect had also lost considerable strength.

If the enemy invaded once more, they would have little hope of stopping them.

“Good heavens.”

As Tang Horyong sighed with a dazed expression, a quiet voice reached his ears.

“Sir Tang, why do you think the Sichuan Tang Clan has survived for the past several hundred years?”

“That is because…”

“Because it was the Tang Clan. Even if you strip away the name “Sichuan,” that fact does not change.”

“…”

“If you make up your mind, the orthodox Murim will help the Tang Clan.”

Tang Horyong trembled and struggled to open his mouth.

“We have made countless enemies over the years. Even among the Nine Sects and One Gang and the Five Great Families, there are those who harbor ill feelings toward our family. Will there truly be no problems?”

“Everything will be handled fairly and openly. Rest assured and build a new nest. Henan, Shaanxi, or…”

A gentle smile formed at the corners of the man’s mouth.

“Shanxi would be good as well.”

“Shanxi?”

“Just say the word. I have plenty of land to spare.”

Tang Horyong suddenly remembered one fact he had forgotten.

The man standing before him was the Alliance Leader who had unified Shanxi Murim, as well as Shanxi Province’s greatest landowner and wealthiest magnate.

“Thank you. Truly, thank you, Great Hero Jin!”

“It was nothing.”

At that moment, the man—Jin Wikyung, the Lesser Family Head of the Jin Family of Taiyuan—responded to the Acting Family Head of the Sichuan Tang Clan’s clasped-fist salute with a courteous yet dignified bearing.

Clunk.

“Um, I heard you called for me.”

Jin Wikyung spotted a young man poking his head through the gap in the pavilion door and let out a lion’s roar.

“My youngest!”

Thud-thud-thud-thud—crash!

His charge resembled that of an enraged bull.

As Tang Horyong watched the reunion of the two brothers, which was impossible to distinguish from either an embrace or a collision, one of the rumors he had heard about Jin Wikyung came to mind.

*They say he’s completely helpless when it comes to his younger brothers.*

The Alliance Leader who had unified Shanxi Murim and the greatest landowner in Shanxi Province was nowhere to be seen.

In his place stood nothing but a hopelessly doting fool.

*He’s still young, so he lacks experience. He can’t compare to my older cousin, who remains so clearheaded at all times and in all places. Yes, that’s right.*

Tang Horyong had no idea that Mimi-chan existed.

* * *

“My youngest!”

Jin Wikyung charged toward me, scattering tears from his damp eyes, and grabbed me in a fierce embrace.

I had been in the Murim for two years now. I had suffered through this kind of thing more times than I could count, so I had expected a reaction like this.

Crack!

…But I hadn’t expected that.

No, what was this supposed to be? Why did I hear bones shifting?

I sighed as he squeezed my entire body like an anaconda in the Amazon jungle.

Still, since he was happy to see me, I let him hug me without resisting.

But his reaction was more violent than ever before.

“Wait, Hyung-nim. Let’s talk after you let go. Let go.”

“Hyung-nim? Why are you using such a stiff form of address? Didn’t I tell you to call me hyung comfortably? You’ve changed. You’ve really changed!”

“Ah, all right, I get it, so let me go now.”

“You used to speak informally when you were little. Why are you using honorifics now? You’ve changed. You’ve really changed!”

“Let go, goddammit.”

“Gasp! You never swore, even when you were at your most rebellious! You’ve changed…”

“Wow, your running commentary is driving me crazy.”

Was his main job really being a martial artist, with being a Dementor as his side job?

Feeling as though my soul were being sucked out, I shuddered and stretched out my hand.

Whoosh—crash!

Jin Wikyung’s huge body was driven headfirst into the ground, and a heavy thud rang out.

A middle-aged man from the Sichuan Tang Clan, who had been watching us, let out a startled groan.

“It’s all right. It’s fine. We’re just playing around.”

“N-No, but…”

“Look. He’s getting right back up.”

Just as I had said, Jin Wikyung sprang to his feet as if nothing had happened, tears of emotion welling in his eyes.

“You’ve grown even stronger in the meantime. That’s my youngest.”

At his unchanged behavior, I let out a quiet laugh.

“You really haven’t changed.”

“Haven’t changed? Do you know how worried I’ve been these past two months? I couldn’t sleep at night, and I lost my appetite so badly that I became skin and bones.”

I looked over his enormous, muscular frame and muttered,

“Your skin and bones look awfully well-padded.”

Come to think of it, two months.

So much time had already passed.

I belatedly realized that it was almost time for me to return.

If ten days in one world amounted to roughly an hour passing in the other…

*About six hours must have passed. The plane might be landing soon.*

The timing couldn’t have been better. I had accumulated quite a bit of fatigue after getting over the mountain that was the Western Heaven Demon Lord.

Without bothering to say anything more, I got straight to the point.

“When are we leaving?”

“My youngest, you must have suffered so much… Hm?”

Jin Wikyung, who had been anxiously looking me over, stopped.

“What did you just say?”

“You came to take me with you, didn’t you? Ah, and the Third Fiend, too.”

Jin Wikyung’s eyes widened.

“How did you know that?”

The middle-aged man, who appeared to be an important figure in the Sichuan Tang Clan, also spoke with a surprised expression.

“Great Hero Jin, didn’t you come to investigate the whole matter?”

“I did, but some of us, myself included, will be returning to Henan. Just before we arrived in Sichuan, we received an assignment to escort the Third Fiend, one of the principal culprits behind the Three-Gate Bloodbath.”

“Then what about the matter concerning our family?”

“That offer remains valid, of course. But the Tang Clan will have difficulty moving right away.”

“That is true. The Family Head still cannot travel any great distance. We also need to obtain the consent of the other family members.”

“Yes. And…”

After quietly discussing something with the middle-aged man, Jin Wikyung sent me a covert Sound Transmission.

*How did you know?*

*You say it, I get it. The circumstances made it seem likely.*

*Ah, my youngest. What kind of ordeal did you go through to make you smarter as well?*

*…*

Something about that rubbed me the wrong way.

I hadn’t figured it out from the circumstances. I knew because a Quest concerning the Third Fiend’s escort had appeared.

“So when are we leaving?”

Jin Wikyung had just finished his conversation and answered my question.

“If you already knew, this will be easier. The sooner, the better. Are you ready?”

“The only things I brought with me were my two balls. I just need to leave with my body.”

Plus two bundles wrapped tightly in bandages.

Jin Wikyung nodded and turned to the middle-aged man.

“Sir Tang, where is the Third Fiend?”

The middle-aged man addressed as Sir Tang answered.

“We have him bound hand and foot and confined under close watch. Ever since his testicles were crushed, he’s been trying to kill himself whenever he gets the chance, so you’ll need to be careful.”

“…How awful.”

Even I would want to die after that.

In any case, we were ready to move quickly.

Jin Wikyung thought for a moment before answering decisively.

“Then half a shichen.[^1] We’ll leave within half a shichen. Is that acceptable?”

“No problem.”

The instant I answered without hesitation, a frantic commotion arose outside the pavilion, followed by someone shouting.

“The Family Head! The Family Head has awakened!”

Jin Wikyung amended his words in a lukewarm voice.

“One shichen. Let’s make it one shichen.”

“…Yes. That sounds better.”

What a shame. I could’ve taken the Myriad-Poison Ring and run.

[^1]: A shichen is a traditional Chinese time unit of roughly two hours.

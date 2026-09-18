# Checkpoint Review — 340–344

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

# Chapters 340–344

## Plot

Venerable Myoryeong reveals that the Heaven-Shaking Venerable Nun, the Emei Sect Leader, and three Elders were murdered by a one-armed middle-aged man—the likely killer of Tang Taesang. Mungyeong treats Myoryeong’s Black Hand Seal and reveals that he is the Divine Physician’s Disciple. He leads Jin Taekyung’s party to the hidden clinic of Dong Feng, the Divine Physician, who begins treating Myoryeong and examines the unconscious Jeok Cheongang.

Dong Feng explains that Jeok’s disrupted Yin and Yang require a Yin-Cold elixir containing at least one jiazi of energy. Taekyung provides Ju Hwaran’s Thousand-Year Snow Ginseng, then accompanies Dong Feng and his companions into Cold-Ice Land to gather the herbs needed for the Life-Restoring Great Technique. After five days, they collect the required one hundred roots of each of twenty-four varieties.

During preparation, Dong Feng discovers that Jeok also contains Formless Ultimate Poison. His Scorching Yang Qi is suppressing it, but the Life-Restoring Great Technique cannot detoxify the poison. Mungyeong suggests the Sichuan Tang Clan’s legendary Myriad-Poison Ring, causing a mandatory Peak-grade Chain Quest. Taekyung leaves Hyuk Mujin and Gung Gibang at the clinic to guard Myoryeong and travels with Cheongpung, Dong Feng, and Mungyeong to the Sichuan Tang Clan.

Tang Sadok has returned after learning of the Emei massacre, deployed the Green Shadow Squad, and strengthened the Gate Guard Pavilion. He admits Taekyung’s group after learning that Dong Feng may be the Divine Physician. Taekyung immediately asks to borrow the Myriad-Poison Ring.

## Continuity

- Jeok Cheongang remains unconscious and critically ill with Formless Ultimate Poison. His Scorching Yang Qi is containing the poison, but treatment cannot safely proceed without an antidote.
- The mandatory Myriad-Poison Ring Quest requires Taekyung to obtain the Tang Clan treasure or Jeok will die.
- Taekyung, Cheongpung, Dong Feng, and Mungyeong are inside or entering the Sichuan Tang Clan seeking the ring.
- Hyuk Mujin and Gung Gibang remain at Dong Feng’s hidden clinic, guarding Venerable Myoryeong.
- Myoryeong is under treatment for the Black Hand Seal and requires rest; her full recovery remains unresolved.
- Dong Feng is the Divine Physician, and Mungyeong is his Disciple. Dong Feng is preparing the Life-Restoring Great Technique after the required herbs were collected.
- Tang Sadok believes the one-armed middle-aged killer murdered both Tang Taesang and the Emei leaders. The killer’s identity and motives remain unknown.
- Tang Sadok has deployed the Green Shadow Squad and increased security around the Gate Guard Pavilion.

## Translation Decisions

- Use **Divine Physician**, **Dong Feng**, **Divine Physician’s Disciple**, **Black Hand Seal**, **Life-Restoring Great Technique**, **Formless Ultimate Poison**, and **Myriad-Poison Ring**.
- Use **Cold-Ice Land**, **Mystic Gate Formation**, **Emei Sect**, **Heaven-Shaking Venerable Nun**, and **Sichuan Tang Clan**.
- Render **녹영대** as **Green Shadow Squad**.
- Render **익산** as **Yishan** and **삼합** as **Sanhe**.
- Preserve Taekyung’s modern comedic phrasing as **no-brakes macho-man talk/approach**.

## Durable state

{
  "active_continuity": [
    "The mandatory Myriad-Poison Ring Quest requires Jin Taekyung to obtain the legendary Tang Clan treasure or Jeok Cheongang will die.",
    "Jeok Cheongang remains unconscious and critically ill with Formless Ultimate Poison while Dong Feng's treatment is being prepared.",
    "Taekyung, Cheongpung, Dong Feng, and Mungyeong are entering the Sichuan Tang Clan to seek the Myriad-Poison Ring.",
    "Hyuk Mujin and Gung Gibang remain at Dong Feng's hidden clinic to guard Venerable Myoryeong.",
    "Venerable Myoryeong remains under treatment for the Black Hand Seal and is expected to have no immediate problems if she rests.",
    "Tang Sadok has returned to the Sichuan Tang Clan after receiving Qingcheng's report about the murders on Mount Emei.",
    "The one-armed middle-aged killer murdered the Heaven-Shaking Venerable Nun and three Emei Elders in a direct confrontation.",
    "Tang Sadok has deployed the Green Shadow Squad to investigate the killer and strengthened security around the Gate Guard Pavilion."
  ],
  "continuity_sources": [
    344
  ],
  "open_questions": [
    "Does the Sichuan Tang Clan possess the Myriad-Poison Ring, and will Tang Sadok lend it to Taekyung?",
    "Can Taekyung obtain a viable antidote and save Jeok Cheongang before his treatment deadline?",
    "Who is the one-armed middle-aged killer, and is he responsible for both the Mount Emei massacre and Tang Taesang's murder?",
    "Will Venerable Myoryeong fully recover from the Black Hand Seal?"
  ],
  "safe_through": 344,
  "temporary_decisions": [
    "Render 활신대법 as Life-Restoring Great Technique.",
    "Render 무형지독 as Formless Ultimate Poison.",
    "Render 만독지환 as Myriad-Poison Ring.",
    "Render 녹영대 as Green Shadow Squad."
  ],
  "version": 1
}

## Reading copies

## Chapter artifact 340

# Chapter 340

The middle-aged nun, Venerable Myoryeong, struggled to speak, her face pallid.

“The Venerable Nun… has passed into nirvana.”

The moment I heard those words, my fist clenched on its own, and something deep in my chest sank with a heavy thud.

The two Elders of the Qingcheng Sect, who had rushed over after sensing the ominous atmosphere, widened their eyes and shouted,

“Venerable Myoryeong, what do you mean? The Venerable Nun has passed into nirvana?”

“That’s impossible! It can’t be!”

I already knew whom the Venerable Nun referred to.

She, too, had been one of the former-generation masters whose image was etched clearly into Jeok Cheongang’s memories.



*She had a very forthright personality. She stopped at nothing against her enemies, and her martial arts were outstanding. There were even times when she was better than Hong Dao, that lazy bald monk.*



During the Great Faction War, the Demonic Cult had feared her and called her the Blood Rakshasa, while the Murim of the Central Plains had given her the sobriquet Heaven-Shaking Venerable Nun.

Even after time passed and the heroes of the past gradually disappeared, she remained on Mount Emei and held her place.

The Emei Sect’s sole Supreme Peak master and its respected Sect Leader.

And now, the Heaven-Shaking Venerable Nun was dead.

*After the Poison King, now the Heaven-Shaking Venerable Nun too.*

What a damned mess.

I finally spoke the words that had been circling inside my mouth.

“Who was behind it?”

“……!”

“……!”

Venerable Myoryeong, Gung Gibang, Hyuk Mujin, and the two Elders of the Qingcheng Sect.

Five pairs of eyes turned toward me at once. The emotion in all of them was surprise, but the reason for it differed.

“The culprit?”

“D-Do you mean the Heaven-Shaking Venerable Nun was…?”

The two Elders of the Qingcheng Sect could not continue and fell silent. They had only belatedly realized what they had failed to notice in their shock at the news: Venerable Myoryeong’s current condition.

Her clothes were stiff with dried, dark-red blood, and her complexion was bluish and deathly pale.

She had been staring at me with wide eyes, but now she lowered her head.

“As expected, Young Hero Jin already knew.”

*As expected?*

At my questioning gaze, Gung Gibang gave a heavy nod.

“We couldn’t help it. The culprit who murdered the Heaven-Shaking Venerable Nun…”

“He’s the same person as the culprit behind what happened at the Sichuan Tang Clan, or at least connected to him. I think so too.”

The Elders, realizing there was something they did not know, asked in urgent voices,

“You knew about the culprit? Has something happened at the Sichuan Tang Clan?”

“Tell us everything. Quickly!”

There was no way to hide it anymore.

Perhaps this had been inevitable ever since the Poison King was murdered.

I took a deep breath before parting my lips.

“A few days ago, Great Hero Tang Taesang, the Poison King, passed away. To be more precise, I should say that someone murdered him.”

“……!”

“The Family Head, Great Hero Tang Sadok—the Myriad-Poison Asura—declared that he would have his revenge. By now, he should be pursuing the culprit with the members of his household.”

But the Poison King was not the only victim.

I left the stunned Elders behind and looked straight at Venerable Myoryeong.

“What happened?”

“It was a middle-aged man. He was missing one arm.”

“One-armed?”

“Yes. He was…”

A trembling voice escaped between Venerable Myoryeong’s lips.

“He was a demon incarnate.”

* * *

Whoosh-whoosh-whoosh!

The fierce wind howled, and the scenery around us flashed past with every step.

The nun in my arms was astonishingly light, and the qi I felt through the contact between our bodies was perilously faint.

*In this condition, she still made it all the way here…*

Venerable Myoryeong had not even finished telling us what happened before she vomited a basinful of blood and lost consciousness.

Gung Gibang, who was following close behind, spoke with a grim expression.

“How bad are her injuries?”

“Serious. I poured internal energy into her to bolster her vitality in an emergency, but… it won’t be enough.”

Gung Gibang let out a quiet groan.

“She wasn’t in this condition when she first set out. Venerable Myoryeong herself insisted that she could endure it.”

“You should’ve stopped her anyway, you bastard.”

“……I couldn’t. I’m sorry.”

My lips moved, but I soon pressed them tightly shut.

I knew. Even if I had gone myself instead of Gung Gibang and Hyuk Mujin, I wouldn’t have been able to stop Venerable Myoryeong.

Even as she vomited blood, the voice she had forced out still rang vividly in my ears.



“The Sect Leader and even the three Elders… They all died by that demon’s hand. I—we couldn’t chase him as he walked away smiling.”



She said the demon had descended upon Mount Emei, the holy mountain of Buddhism, only three days ago.

The demon had climbed the mountain like any other pilgrim and sought out the residence where the Heaven-Shaking Venerable Nun lived. Three Elders happened to be there at the time.

Then a battle that shook heaven and earth had erupted. A mountain peak collapsed, and Mount Emei itself trembled.

What Venerable Myoryeong had witnessed after recognizing the disaster and rushing there from the nearest location was four dead nuns and a single demon.



“Don’t look so shocked. My killing arts were simply stronger than Emei’s Buddhist teachings.”

“H-How could you do such a thing? Are you truly not afraid of Heaven?”

“How laughable. The Buddha and Heaven you speak of are all lies and illusions. I will show you that I have another Heaven.”



That was the last thing he said.

The culprit struck Venerable Myoryeong with a palm and disappeared. While the Emei Sect was consumed by grief and rage, two young men arrived.

After hearing from Gung Gibang and Hyuk Mujin that the Qingcheng Sect was nearby, she ignored everyone who tried to stop her and descended Mount Emei.



“Please help us. Please! No matter what, we must stop that demon… Cough!”

Recalling Venerable Myoryeong crying out until the final moment before she lost consciousness, I clenched my teeth.

*What kind of bastard was he…?*

A one-armed middle-aged man. A master whose martial prowess was terrifying enough for him to single-handedly kill the Heaven-Shaking Venerable Nun, a Supreme Peak master of the former generation, and three Elders.

What purpose could he have had? Why had he done something like this? And was he the same culprit who had murdered Tang Taesang, the Poison King?

*What if he wasn’t?*

The moment my thoughts reached that point, a chill ran down my spine, and my heart began pounding violently.

If the culprits behind the two incidents were different people… it would only be a matter of time before Sichuan became a land of death.

Just as my previously effortless steps began to grow heavy, the two Elders of the Qingcheng Sect spoke.

“I think we should part ways here.”

“I’m sorry, but our circumstances don’t allow us to do otherwise.”

It was the obvious choice for men worried about their sect.

The Sichuan Tang Clan had been attacked, and now the Emei Sect had suffered the same fate. Anyone with a brain could guess that the Qingcheng Sect would be next.

“There’s no need to apologize. I would have done the same.”

“Thank you for understanding.”

“Are you going straight to Mount Qingcheng?”

The older of the two Elders shook his head.

“I will lead some of our Disciples to help the Emei Sect. My Junior Brother will return to the main sect with the remaining Disciples. And you?”

“Venerable Myoryeong’s injuries are more serious than I expected. I’m going to find a physician, then contact the Sichuan Tang Clan.”

With a substantial portion of their members away, the Sichuan Tang Clan and the Qingcheng Sect had both been left virtually undefended. We had to warn them in case something happened.

The Elder, whose sect was in the same position, understood that as well.

“For now, focus on treating Venerable Myoryeong. We will send someone to the Sichuan Tang Clan.”

“Thank you.”

“Not at all. May fortune favor your martial path.”

“And yours.”

We clasped our hands in a martial salute and split into three groups.

The two Elders each led their Disciples away to the north and east. That left only four people, including me.

*Ah. Jeok Cheongang and Venerable Myoryeong were here too.*

We had come all the way to Sichuan to heal a patient, but instead of finding the Divine Physician, we had gained another patient.

*What is this? A hidden-camera prank?*

Fuck, as if.

I let out a deep sigh inwardly and was about to start walking again when—

Step. Step.

Light footsteps came up the dirt path, accompanied by a cheerful humming sound. A boy climbing along the mountain trail finally spotted us and opened his eyes wide.

“Huh? Wha—?”

It was a familiar face. The boy’s name was Mungyeong.

I was glad to see him again after only a few days, but before that feeling could fully surface, another thought crossed my mind.

“Mungyeong.”

“What brings everyone here…? Huh?”

“You’re a medical apprentice, right?”

I still remembered him treating patients on the deck of the Swift Tide.

I did not know exactly what kind of treatment he had provided, but according to the river bandits, he was quite skilled.

“Yeees. I am, but…”

Mungyeong answered with a bewildered expression, then turned his gaze toward Venerable Myoryeong in my arms. No further explanation was necessary.

He took a wooden case containing acupuncture and moxibustion tools from the travel bag he had been carrying and strode toward us.

“First… let me examine the patient.”

* * *

Swish.

The time it took Mungyeong to feel her pulse and place the needles was no more than an instant.

But even though he handled the entire process as smoothly as flowing water, a shadow remained over his face.

“…How is she?”

I did not need to ask to know that the result would not be good.

As expected, Mungyeong quietly shook his head.

“It’s not good. Really.”

“At least you were able to provide some treatment, right?”

“Yes.”

I let out a sigh of relief.

It might have sounded unkind, but I had never expected much from Mungyeong to begin with. He was still young, and he had only been practicing medicine for a short time.

All I wanted was that minimum treatment.

“You’ve done enough. That’s sufficient for now. If we get to Chengdu as quickly as possible and find a way…”

“Will that really be enough?”

“What?”

“After a month, her flesh will begin to rot. After four months, her bones will melt away.”

“Hold on. What the hell are you talking about…?”

But Mungyeong’s quiet voice continued without stopping.

“If she spends half a year in terrible pain, she’ll start to look like a walking corpse. A year at most. Once her organs begin to rot, she’ll finally stop breathing.”

“…What?”

“Even if you go to Chengdu, there won’t be any suitable treatment. The physicians available among ordinary people can only treat women’s ailments, the sort suffered by high officials and nobles. And the Sichuan Tang Clan…”

I was surprised twice.

First, by the fact that Venerable Myoryeong’s injuries were that serious.

Second, by the unfamiliar sight of Mungyeong calmly continuing to speak such terrifying words.

“I heard rumors throughout the marketplaces that the Tang Clan’s martial artists headed west. It will take several days at least for them to return. By then, it will be too late. How long has it been since she was injured?”

Hyuk Mujin answered haltingly.

“Th-Three days. A little over three days, I think.”

“Three days…”

Mungyeong let out a quiet groan and continued in a heavy voice.

“The Black Hand Seal is a terrifying evil technique. Once seven days and nights have passed, there will be no turning back.”

Grab!

That was as far as he got.

My patience had run out, and I could not hold back any longer. I seized him by the collar.

“You… How the hell do you know that?”

A teenage medical apprentice had just named an evil technique that no one here had ever heard of.

If this was the Mungyeong I knew, such a thing was impossible.

“Tell me. Now.”

Mungyeong swallowed hard at my chilling aura before answering,

“My Master… My Master told me everything.”

“Your Master?”

“Y-Yes. Yes… Cough!”

A sudden flash of insight passed through my mind.

The strength ebbed from the hand gripping his collar.

A murmur like a groan slipped between my lips.

“The Divine Physician…?”
## Chapter artifact 341

# Chapter 341

A conversation I’d had with Mungyeong several days ago flashed through my mind.

*Thank you for everything.*

*Forget the thanks. Just focus on becoming a great physician.*

*Like the Divine Physician?*

*Yes, like the Divine Physician.*



And there had been one last thing he had said almost in passing.

*It’s a shame we can’t go together this time. I have to return to my Master.*



How had I not realized it?

Thinking back, Mungyeong had been unusual from the very beginning. The incredible resourcefulness he had displayed when river bandits threatened his life, the composure far beyond his years, and his remarkable medical skills.

*That’s not all.*

The boy who had nearly sunk to the bottom of the Yangtze because of the river bandits had brazenly hitched a ride aboard the Swift Tide, then gone to the Sichuan Tang Clan—infamous throughout the Murim for their vicious tempers—just to get a prescription.

Mungyeong had done things that even Murim artists with Botox injected into their livers might have shied away from, and he had done them without batting an eye.

*And on top of that, the things he just said and did…*

I had no idea what kind of martial art the Black Hand Seal was or how powerful it might be.

But I knew one thing for certain.

“The Divine Physician. You’re the Divine Physician’s Disciple.”

“……!”

“……!”

The others stared wide-eyed at Mungyeong after hearing the joy and deflation mingled in my words.

Mungyeong shrank back in the suffocating silence that descended over us.

“I-I’m sorry. But I couldn’t tell you.”

“Why not?”

I regretted asking the moment the words left my mouth. The Divine Physician had spent his entire life hiding his identity. Of course his Disciple had kept silent.

If Venerable Myoryeong’s life had not been hanging by a thread, Mungyeong almost certainly would never have revealed his Master’s identity.

“Where is the Divine Physician—or rather, where is your Master?”

Mungyeong hesitated, then bit his lip tightly.

“But before that, could you promise me one thing?”

“I’ll keep the secret. Absolutely.”

With that firm answer, I pulled something from inside my robe and held it out.

It was something I had been taking out of my Inventory to examine whenever I had a spare moment lately.



> The finest Chinese gallnuts come from Sichuan.



Mungyeong’s eyes widened when he saw the faint writing on the jade-colored porcelain shard.

“This is…”

“Do you recognize it?”

“Yes. It’s unquestionably my Master’s handwriting.”

Mungyeong examined the Divine Physician’s Token from every angle, apparently fascinated, then let out a small exclamation.

“Come to think of it, my Master once told me that a very long time ago, he left a token with a famous physician and told him to come to Sichuan. But how did you, Young Master, come to possess this…?”

“The famous physician gave it to me directly. There’s a patient whom no one but the Divine Physician can treat.”

I continued emphatically.

“There’s someone I have to save.”

“I don’t know who that person is, but… you hold them very dear, Young Master.”

Someone I hold dear.

Yes. I suppose that was true. Jeok Cheongang was someone precious to me. He had given me everything he had, and now it was my turn to protect him.

“Yes. That’s right.”

Mungyeong smiled faintly and nodded.

“Come with me. I’ll guide you to my Master.”



* * *

Crunch. Crunch.

The snow collapsed beneath our feet with every step.

I looked around. Frost-covered, bare branches. White snow piled thickly everywhere I looked.

*It’s amazing no matter how many times I see it.*

Outside, early spring had arrived, and new shoots were beginning to emerge. But the place we were walking through looked like a winter day buried beneath falling snow.

*So this is a Mystic Gate Formation…*

Mungyeong had led us to the very same mountain we had searched with the Qingcheng Sect. But after we reached a certain point, he strained to move several rocks, and an entirely new path and landscape unfolded before us.

*All of us, myself included, had been left speechless at the sight we had never seen before.*

Mungyeong had told us that the person who installed this place was the Master of Strange Illusions.

According to Gung Gibang, who had explained it with spittle flying, the Master of Strange Illusions had been called the greatest formation master under heaven in the distant past.

I had no idea what sort of connection he had shared with the Divine Physician, but he had installed something like this. We had nearly wandered around for ages despite being right in front of the place.

*No wonder nobody could find him.*

What good was it to deploy top-tier Murim artists and countless government troops?

If they had searched every mountain one by one using ordinary methods, even half a century would not have been enough, let alone six months.

“Wow! Woooow!”

Cheongpung, who had been running several steps ahead of us like a puppy let loose in a snowy field, cried out in delight. I was about to scold him when the scenery changed completely the very next moment, and my mouth fell open too.

“……Whoa. What the hell is this?”

The world had changed again after only a few steps.

The snow-white midwinter landscape had given way to spring in full bloom.

Everything around us was green, and nameless flowers were in full bloom. Hyuk Mujin approached with a dazed expression and asked,

“Captain. Am I seeing things?”

“I don’t know, Mujin.”

Even Gung Gibang, the most experienced Murim veteran among us, could only stand there with his mouth hanging open.

“Good heavens… Hk! Ptooey, ptooey! What is this?”

“Are those butterflies?”

Oh, they really were butterflies. And not just one or two.

Every color imaginable.

Hundreds of butterflies that had been resting throughout the flower field took flight at the same time. It was a spectacular sight.

Whoooosh.

Where had the wind suddenly come from? And where was the bright sunlight pouring in from?

Every single thing I saw felt like one of the Seven Wonders of the World.

*The pyramids have nothing on this.*

There was a place where the seasons changed after only a few steps, so what were the pyramids compared to that? Some Egyptian logistics officer probably just ran his workers ragged building them.

All the pharaoh had to do was put on a solemn face and say, “This pharaoh is disappointed in you,” a few times, and they would be hauling stones while getting whipped.

But this place…

This was an entirely different league.

“Young Master Jin?”

“Huh? Oh, yeah.”

“We’re almost there. We only have to cross that hill.”

We hurriedly came to our senses and followed Mungyeong once more.

When we crossed the low hill covered in green grass, a small thatched hut standing alone on a flat stretch of land came into view.

And…

He was there.

“Master!”

At Mungyeong’s shout, an old man who had been planting something in the vegetable garden before the hut straightened his bent back. His beard was as white as the snow we had seen on the way there. Deep wrinkles framed his clear eyes.

When he noticed us, the corners of his eyes curved gently.

“Some honored guests have arrived.”

We had finally found him.

The Divine Physician.



* * *

It was a long while before we properly spoke with the Divine Physician.

After examining Venerable Myoryeong’s condition, the Divine Physician had Mungyeong carry her into the hut. The two of them did not emerge again until a shichen later.

“It has been a long time since anyone came to visit.”

The Divine Physician’s sudden voice resembled a cool spring breeze. I had been pacing around the hut and hurriedly bowed at the waist.

“Jin Taekyung of the Jin Family of Taiyuan pays his respects to the Divine Physician.”

“Dong Feng.”

“Pardon?”

“That is my name. The title Divine Physician is too grand for me, so please call me Old Man Dong.”

I wasn’t about to call the greatest physician under heaven Old Man Dong like some old man Kim at a neighborhood real estate office.

*And he was old enough to be my grandfather.*

But when I met the Divine Physician’s benevolent gaze, I had no choice but to quietly comply.

“Yes. I will, Old Man Dong.”

“Thank you, Young Master Jin.”

After giving me a gentle smile, the Divine Physician exchanged greetings with everyone else, one by one.

He maintained his manners even with us, who were far younger than him, and he never once seemed rushed.

“Hello! I’m Cheongpung!”

He did not even lose his smile in front of the local lunatic.

“Heh heh. You’re a very energetic person. My name is Dong Feng. You may call me Old Man Dong, just like the others.”

“But my grandfather told me that I have to show respect to my elders.”

“Your grandfather gave you an excellent lesson. But if our hearts are at ease with each other, what harm is there? Just think of me as a friend who happens to be a little older than you.”

“A friend?”

“That’s right. A friend.”

Cheongpung smiled brightly.

“Then I look forward to getting along with you, Old Man Dong!”

“Heh heh. Heh heh heh!”

He’s laughing?

Was he some kind of Murim joker? The type who laughed when angry and laughed when bewildered.

“Old Man Dong, have you ever eaten candy?”

“I like sweets. I used to enjoy candied hawthorn skewers,[^1] too.”

“Hey, me too!”

The setting looked like a healing movie, but the conversation itself was pure horror thriller. In the end, Gung Gibang, his face gone deathly pale, clamped both hands over Cheongpung’s mouth and slowly backed away.

The Divine Physician laughed heartily at the sight, then turned toward Mungyeong.

“You have brought some interesting people.”

Mungyeong bowed deeply.

“I’m sorry, Master. I brought them without your permission.”

“No, no. Fate is tied by Heaven. This must be the natural order as well. Don’t you agree?”

His last question was directed at me. I nodded and held out the Divine Physician’s Token I had prepared in advance.

“This is a token you left behind long ago, Divine Physician—or rather, Old Man Dong. The Luoyang Strange Physician gave it to me and told me to come find you.”

“I did?”

“Pardon?”

No way. Had he forgotten about it?

The Divine Physician tilted his head for a moment. It was only after Mungyeong reminded him again that he let out a small exclamation.

“Ah, yes. I remember now. It was so long ago that I had temporarily forgotten.”

“Whew. I thought you had forgotten completely.”

“Now that I think about it, the fact that you possess this token means that something has happened for which you absolutely need this old man.”

“Yes, that’s right.”

“Is it about the nun you brought here? If so, there is no need to worry too much. She has already made it past the immediate crisis.”

The Divine Physician looked toward the hut where Venerable Myoryeong was lying and continued.

“It will not be an easy road, but… if she receives sufficient rest after the remaining treatment is complete, she should make a full recovery.”

It was the best news I had heard in a while. Not only had Venerable Myoryeong escaped the brink of death, but the Divine Physician truly possessed medical skills worthy of his reputation.

I took a deep breath before speaking.

“There’s another patient.”

“Another patient?”

“The person who gave me the token said that there was only one person under heaven who could treat him. You.”

“Only I can treat him…”

The Divine Physician repeated the words quietly before speaking again.

“Birth, aging, sickness, and death are not things a mere human can decide. But if there is even the slightest possibility, I will do my best as a physician.”

“That’s enough… That’s all I need.”

There had been a time when my mother was sick.

Those were the same words the doctor in charge of her surgery had spoken.

*I’ll do my best.*

For Hayeon and me, those words had been our only hope, and the surgery had ended successfully.

Just as I had done with that doctor in the past, I tightly gripped the Divine Physician’s wrinkled hand.

“Please. Old Man Dong.”

The Divine Physician smiled benevolently, as if he understood everything.

“Let us see the patient first.”

After that, there was nothing but waiting and anxiety.

Once Jeok Cheongang, who had been lying on the pack frame, was carried into the hut, I walked back and forth, waiting for the Divine Physician and Mungyeong to emerge.

I saw butterflies and honeybees flitting through the flower field and trees sprouting fresh green leaves, but I felt nothing.

*It went well, right? It must have gone well.*

I could not even bring myself to approach the hut, afraid that I might hear something negative.

I walked for a long time, endlessly repeating that one thought.

Only after the sunlight disappeared and faint darkness settled over the land did I return to the hut.

And there, despite looking exhausted, the Divine Physician and Mungyeong were waiting for me with faint smiles.

“I believe I can treat him.”

The instant I heard those words, all the strength drained from my legs, and a familiar alert pierced my ears.

Ding.

> **System**
>
> - Quest condition, **Get examined by the Divine Physician**, completed!
>
> - Quest, **Find Mr. Shin in Sichuan**, successfully completed!

[^1]: Candied hawthorn skewers are a traditional snack made by coating fruit in hardened sugar.
## Chapter artifact 342

# Chapter 342

*Finding Mr. Shin in Sichuan* had been a Supreme Peak Grade Quest. And with difficulty that vicious, its rewards were bound to be substantial.

Ding. Ding. Ding.

A massive EXP payout and the resulting Level Up. Even an achievement.

I dismissed the incessant System notifications and the holographic windows blocking my view. It was hard to feel nothing but happy when the Divine Physician’s expression looked so grim.

“What’s wrong? You’re not having second thoughts, are you? You’re not about to tell me you can’t treat him after all, right?”

“That is not the case. I may be an old quack, but if I give it my all, there is still plenty of hope.”

“Then why do you look like that…?”

He hesitated for a moment before letting out a shallow sigh. The faint smile that had lingered around his lips had already changed into wrinkles filled with anguish.

“There are too many things we must prepare for the treatment.”

“Oh, if this is about the cost, you don’t need to worry.”

I might not look it, but I was the youngest son of the Jin Family of Taiyuan. It was already common knowledge that the Jin Family of Taiyuan had amassed a fortune through the northern trade routes over the past few years.

“If it’s really urgent, I can borrow some money from his family. Hey, there are Hyuk Family textile shops in Sichuan too, aren’t there?”

Hyuk Mujin nodded with a troubled expression.

“There are. It would be strange if there weren’t, considering Sichuan is famous for its silk.”

“Then let’s borrow some emergency cash. We can sell the shop if things get desperate, right?”

“Of course not.”

“I’ll pay you plenty of interest.”

“And if I refuse?”

“Then I’ll give you plenty of travel money for the road to the next world.”

“……”

“Just take it all. Go ahead and pull up the very foundations of my family while you’re at it.”

Okay, problem solved.

But for some reason, the Divine Physician’s expression remained dark.

Since his Master could not easily bring himself to speak, Mungyeong opened his mouth in his place.

“Um, Young Master Jin.”

“Yes?”

“That isn’t the biggest problem. Of course, the treatment will require an enormous amount of money, but there are materials that would be difficult to obtain no matter how much gold and silver we had.”

“Materials that are difficult to obtain…? Are you talking about an elixir?”

“Yes. An elixir meeting certain conditions is needed to treat Great Hero Jeok. It is extremely valuable and rare, so if we start looking for one now, we may have to wait several years before finding it.”

Several years?

That was far too long. Jeok Cheongang’s lifespan would run out in only a few months.

Just as I found myself unable to speak, the Divine Physician continued in a subdued voice.

“I believe a detailed explanation is necessary. The reason the patient has not regained consciousness is that his balance has been disrupted.”

“His balance?”

“All things in the world contain the energies of the Five Elements and exist in a proper balance. The human body is no different. But the patient attempted to wield an enormous force and ended up destroying that balance.”

An enormous force?

The Divine Physician’s words suddenly brought something to mind.

*Dance of the Fire God and Demon.* The Fire Gate Clan’s final secret technique, which drew out and amplified every ounce of power possessed by its user.

*So that was the cause.*

In the distant past, Jeok Cheongang had earned the name Fire King by using the Dance of the Fire God and Demon against a thousand members of the Demonic Cult. But as the years passed, his old and diseased body could no longer endure that power. It had shattered.

“When a vessel breaks, whatever it held inside will inevitably leak out. Fortunately, there is a way to reverse the damage, but it requires an elixir rarely seen in this world.”

“An elixir rarely seen in this world…”

“And even among those, it must meet certain conditions.”

“Tell me. I’ll obtain it no matter what it takes.”

The Divine Physician sighed and nodded.

“It will be extremely difficult, but what choice do we have? We must place our hopes in you, Young Master. Now listen carefully to what I am about to say.”

“Yes.”

In a grave voice, the Divine Physician explained in detail Jeok Cheongang’s current condition, the method of treatment, and the requirements for the necessary elixir.

“Will you remember all of it?”

“……”

“Young Master?”

“Oh, yes.”

“I asked whether you remember all of it.”

“Yes. I remember everything. But this is… Whew.”

“……”

“Could you check whether I heard this correctly? I mean, confirm it for me?”

“I was planning to do so anyway. Go ahead.”

I carefully began to speak.

“So, his balance was disrupted by excessive expenditure of power, and in particular, the harmony between Yin and Yang was destroyed?”

“That is correct.”

“And the cause was an enormous amount of Scorching Yang Qi that had gone out of control.”

“Continue.”

“To restore this broken balance and bring it back into harmony, we need an elixir—an incredibly powerful elixir at that—but to do so…”

Mungyeong quickly cut in.

“Among elixirs, it must possess the nature of Yin-Cold Qi. In addition, it must contain at least one jiazi’s worth of energy.”

“Four months. If we cannot find it within four months, everything will be pointless.”

The Divine Physician’s heavy voice brought the conversation to an end.

Ding.

> **System**
>
> - A Chain Quest, **Thirty Thousand Li in Search of an Elixir**, has been generated.
>
> - This is something you must accomplish. You cannot refuse!
>
> - Find an elixir containing at least one jiazi of energy and possessing the nature of Yin-Cold Qi!

I stared blankly at the holographic window before finally coming to my senses.

“Will that do?”

“Many other materials are necessary, but this is the most important one—the core ingredient. So you must depart immediately and find an elixir…”

“Ah, yes.”

And so I departed.

Two steps forward toward the Divine Physician. Then I pulled something from inside my robe and held it out.

“Here.”

“……?”

“……?”

“Take it.”

Master and Disciple alike stared blankly at me, then reached out at the same time to take the object I held out.

“What is this?”

“Master, why don’t you open it first?”

“W-Well, shall I?”

Click.

The Divine Physician swallowed nervously and carefully opened the wooden box. Along with a pure, clear fragrance that seemed capable of purifying even the coronavirus, *it* revealed itself.

“Gasp!”

“Good heavens!”

“It’s a Thousand-Year Snow Ginseng. It contains at least one jiazi’s worth of energy and possesses the nature of Yin-Cold Qi. Is this enough?”

The Divine Physician’s eyes widened as he looked back and forth between me and the Thousand-Year Snow Ginseng. Then he nodded vigorously.

“It is enough!”

Ding.

> **System**
>
> - Quest conditions fulfilled!
>
> - Chain Quest, **Thirty Thousand Li in Search of an Elixir**, successfully completed!
>
> - Achievement, **Mountain Herb Gatherer**, acquired!
>
> - A substantial amount of EXP acquired!
>
> - Level Up!

As the System notifications rang out, I suddenly thought of Ju Hwaran.

*Thank you, Young Lady Ju.*

I let out a wry chuckle as I thought of how she had given it to me while passing the Thousand-Year Snow Ginseng off as Hundred-Year-Old Snow Ginseng, worried I might feel burdened and refuse it otherwise.

*Now I have a reason to stop by Shaanxi on the way back.*

And when I did… I hoped I would be with a healthy Jeok Cheongang.

I turned toward the still-dazed Divine Physician.

“All right, then. What do we do next?”

The Divine Physician carefully tucked the wooden box into his robes and began walking.

“Follow me. Gyeong, you stay here and look after the patients.”

“Yes, Master.”

Leaving Mungyeong behind as he answered respectfully, we followed the Divine Physician.



* * *



Swish!

A small figure sped along right beside me. Every time he extended one foot, a zhang of distance vanished and the wind swept past.

What was astonishing was that his feet never touched the ground even once.

With a faint tap, the grass beneath his toes bent gently before springing back into its original shape.

I narrowed my eyes at the sight.

*Flying Over Grass?*

Flying Over Grass was a realm in which one ran as though flying while stepping across blades of grass.

Martial artists who had mastered their movement techniques to the Peak realm could perform feats like this. Treading Snow Without a Trace, which left no footprints even while running across snow, and Rising on Duckweed, Crossing Water, which allowed one to walk across water as though it were solid ground, were similar techniques.

Stepping on Empty Air was a realm attainable only by Supreme Peak masters with internal energy to spare.

*Of course, Flying Over Grass isn’t beyond me either if I put my mind to it.*

Even so, it felt astonishing because the person currently using it in front of me was the Divine Physician.

*I knew he had learned martial arts, but his movement technique is especially impressive.*

I had realized that the Divine Physician knew martial arts when we first met.

Although he was small in stature, he possessed vitality and sturdiness comparable to those of a young martial artist. The energy contained in his dantian was considerable as well.

*His martial arts are First Rate, and his internal energy is probably around Peak.*

Just as I was quietly assessing him, the Divine Physician sensed my gaze, turned his head, and smiled.

“Why are you looking at me like that?”

I answered honestly.

“Your movement technique is remarkable.”

“Heh heh. No matter how hard this old man tries, how could I compare with you, Young Master? I merely happened to learn it.”

“Honestly, before I met the Divine Physician—or rather, Old Man Dong—I never imagined you had learned martial arts.”

“You must have been surprised. The others are the same.”

I glanced behind me. Everyone except Cheongpung wore an expression of desperate curiosity.

There was no reason to be vague now that things had come this far. It would be better to ask him plainly.

“This may be presumptuous, but may I ask how you came to learn martial arts?”

Martial arts and a physician. It was understandable if the subject made him uncomfortable, but the Divine Physician did not avoid answering.

“When I was around twenty, just after becoming a medical apprentice, my Master personally instructed me.”

“Then was your Master perhaps…?”

“That is correct. My Master was a martial artist.”

The Divine Physician’s Master had been a martial artist. It was an identity I had never expected.

Seeing my expression, he let out a hearty laugh.

“Heh heh. There is no need to be surprised. By the time he accepted me as his Disciple, he had already left the Murim.”

“Oh, I see.”

“My Master had reached the highest realm both as a martial artist and as a physician. He said that he became a physician to wipe away the killing karma he had accumulated.”

For some reason, I felt I understood that feeling.

I had accumulated killing karma too. At first, I swung my spear while thinking only of getting home and believing that this was merely a fictional world created by a game.

*But everything was real. They were all living people.*

By the time I realized that, it was already too late.

I could not stop, and I did not stop. I killed to survive, and I killed them because they were my enemies.

In the Murim and in the modern world.

At some point, the scent of blood had seeped deep into my body. It was a stench that no amount of washing could remove.

“……I see.”

At my delayed answer, the Divine Physician gave me a gentle smile.

“It was simply each person’s choice. My Master chose the path he believed was right, and I did the same. However, so many people came looking for this old man that I had no choice but to learn martial arts for my own protection. I was naturally a dullard, so I was scolded quite often, heh heh.”

Everyone has memories.

Perhaps remembering the days he had spent with his Master, the Divine Physician suddenly stopped walking in the middle of his laughter.

“Well, we have arrived.”

Crack.

A frozen leaf crumbled beneath someone’s foot.

This was an especially cold valley within the Mystic Gate Formation spread around the Divine Physician’s residence.

“Where exactly are we?”

“I call this place the Cold-Ice Land.”

Cold-Ice Land. It was a fitting name.

Though perhaps Yanggu in Gangwon Province or Moscow would have been better.

I glanced at Hyuk Mujin, who had already begun to shiver violently, then asked the most important question.

“What do we do now?”

“You will have quite a difficult time. We must find and dig up various things, including the medicinal herbs needed for the initial stage of the treatment.”

“That sounds simpler than I expected.”

“Let me see… A hundred roots of each should be enough.”

“Ah, yes. A hundred roots.”

“I said a hundred roots of each.”

“Yes. That’s what you said. A hundred roots.”

I nodded, then froze.

Wait. What had I just heard?

“A hundred roots *each*? Not a hundred in total?”

“That is correct.”

The Divine Physician continued with a hearty laugh.

“A hundred roots each of twenty-four kinds.”

“……!”

Ding.

> **System**
>
> - A Chain Quest, **Herb Slave of Cold-Ice Land**, has been generated.
>
> - This is something you must accomplish. You cannot refuse!
## Chapter artifact 343

# Chapter 343

Whoooooosh.

“What the hell is with this wind? Fucking hell.”

I shuddered as the bitter cold pierced straight through my leather clothes. *Unaffected by Cold and Heat*, my ass. More like *Very Much Affected by Cold and Heat*.

“Pfooh-chew!”

I turned around, wondering what bizarre sound that had been, and found Hyuk Mujin rubbing his blue-tinted nose.

When our eyes met, his narrowed into hooks.

“What?”

“……”

“What are you looking at?”

“No, I was just wondering about the sound of your sneeze…”

“Seriously? You find even that fascinating? If you have that much time to spare, dig up another herb.”

“……All right. My bad.”

I quietly looked away and scanned the area for another herb.

It had already been five days since I had taken a job as a herb slave in Cold-Ice Land. The hierarchy between us had reversed a long time ago.

“Ah, what are you doing? There’s one right over there. There!”

“Oh. So there is.”

“Get a grip!”

Ugh. I couldn’t even punch him.

If he had followed a friend to Gangnam, at least the land prices would have gone up. Instead, Hyuk Mujin had followed me to Cold-Ice Land and was suffering through the worst ordeal of his life.

He had been dragged into all kinds of fights before and always stopped after grumbling a few times, so the fact that he was now glaring at me with murder in his eyes said everything.

“I’ll dig for herbs beyond that hill. Don’t stop working. I’ll come check on you from time to time.”

“……Got it, you punk.”

I repeated the character for patience to myself, gently dug through the snow, and pulled up an herb.

As soon as I placed it in the basket the evil employer—or rather, the Divine Physician—had issued to each of the herb slaves, the System notification rang out.

Ding.

> **System**
>
> - You gathered **Cold-Ice Herb**.
>
> - Remaining quantity: **100 / 100**.
>
> - Gathering **Cold-Ice Herb** is complete!

“Whew. Finally finished another one.”

The fact that I could slowly see the end was at least some consolation.

As I checked the Quest window to see how many remained, Gung Gibang approached me, shivering violently.

“Hey, how many are left?”

“About two hundred roots. If things go well, we might finish today.”

“Two hundred roots are left?”

“Only two hundred. Hang in there a little longer.”

“No. Two hundred roots is way too many. By then, I’ll be a frozen corpse buried somewhere under this snow.”

“……”

What a load of crap.

Still trembling, Gung Gibang pulled a fire striker from inside his clothes and lit it.

He brought his face close to the tiny flame and murmured in a wistful voice, “I miss my Master. I miss the days when I begged in the alley outside a warm inn…”

Was he the Little Match Girl?

I muttered, dumbfounded by his behavior.

“You were still a beggar back then.”

“At least I was a warm beggar back then. That’s a hundred times better than being a cold one.”

“……You have a point.”

“I want to go back to those days. A lazy noon, sunlight pouring down. A delicious-looking yellow dog walking by…”

What the hell did he mean, a plump yellow dog?

Gung Gibang’s eyelids slowly drooped as he said something that would make animal-protection groups scream.

This bastard couldn’t possibly be—

“Hey! Hey!”

I hurriedly sent Scorching Yang Qi into his body.

He had to come to his senses somehow—

“It’s warm…”

“I said wake up, you lunatic!”

Smack! Smack!

It was no use. No matter how hard I slapped his cheeks, his eyes showed no sign of opening again.

I continued sending Scorching Yang Qi into him and shouted, “Is anyone there? Somebody, come here, quick!”

In response to my desperate cry, someone came sprinting over from far away.

“Benefactor! Benefactor!”

“Nice, Cheongpung! Quickly, take this guy outside—”

Cheongpung ran over like the wind, beaming as he held something out to me.

“Benefactor, look! It’s the first snowman I’ve ever made!”

“You son of a bitch!”

* * *

The Divine Physician checked all the herbs in the baskets and nodded.

“This should be enough.”

Ding.

> **System**
>
> - Chain Quest, **Herb Slave of Cold-Ice Land**, successfully completed!
>
> - Achievement, **Mountain Herb Gatherer Who Returned Alive from Hell**, acquired!
>
> - You acquired 10 bonus points for earning an achievement!

Look at that achievement title.

I didn’t even have the strength to get angry anymore.

The Divine Physician’s gaze, which had been resting on our utterly exhausted forms, suddenly stopped on one person.

“Why is Young Master Cheongpung so dejected?”

That was because I had smashed the first snowman Cheongpung had ever made with my Flame Divine Palm.

I glared murderously at the still-sullen Cheongpung and asked the Divine Physician, “So, are all the preparations complete now?”

“They are. With this quantity, we will be prepared for whatever may happen later.”

“Prepared?”

The Divine Physician nodded heavily.

“We do not know what may happen.”

I suddenly realized something I had forgotten for a moment.

The Divine Physician had never once been certain.

He had only seen a possibility and said that he would do his best.

*It isn’t over until it’s over.*

The words I whispered to myself whenever I faced a crisis now became a dagger stabbing into my chest.

In the end, there was only one thing I could say.

“Please… do everything you can. Do everything you can.”

“This old man will do everything within his power. I promise.”

Mungyeong, who had been standing beside the Divine Physician, spoke with resolve.

“I will also do everything I can to assist my Master.”

“Thank you.”

“There’s no need. It is only natural for a medical apprentice to do so.”

“Then when will the actual treatment begin?”

The Divine Physician remained silent for a moment, thinking.

“Probably in seven days. Until then, Mungyeong and I will combine and refine the twenty-four types of herbs you brought us and prepare them as ingredients for the Life-Restoring Great Technique.”

“All of them?”

“This is only a portion of what we need. Fortunately, I already possess the remaining ingredients required for the Life-Restoring Great Technique, which allowed us to shorten the preparation time.”

“What exactly is this Life-Restoring Great Technique…?”

The Divine Physician stroked his snow-white beard and answered.

“As I mentioned before, my Master was once a martial artist. He primarily practiced medicine among the common people, but he was also deeply learned in the proper management of qi.”

Hearing that, I had a rough idea of where this was going.

Hyuk Mujin suddenly cut in with a gasp.

“A martial artist! So the Life-Restoring Great Technique was created to treat martial artists!”

“That is correct. Master of Strange Illusions was one of them. He recovered from severe qi deviation thanks to the Life-Restoring Great Technique, then installed a Mystic Gate Formation before departing.”

For martial artists, qi deviation was practically a death sentence. Their internal energy reversed course, their qi and blood became tangled, and all their acupoints and dantian were damaged.

The easiest way to understand it was to imagine a small bomb exploding inside a person.

*But he cured qi deviation.*

If Master of Strange Illusions had been in a condition serious enough for the Divine Physician to describe it that way, he must have been little more than a walking corpse at the time.

Even just hearing about it gave me some idea of how effective the Life-Restoring Great Technique was.

*Then Old Master will definitely—*

I quickly brushed the thought aside.

There was no reason to be certain now, and no reason to worry.

“Please take good care of him.”

“Until preparations for the technique are complete, no one may approach the place where the patient is being kept. Do you understand?”

“Yes.”

“By then, the preparation of the Life-Restoring Great Technique will be finished, and we will have a clearer understanding of the patient’s condition. Wait patiently until then.”

“I will keep that in mind.”

“Remember. Seven days.”

But the Divine Physician’s words did not come true.

He reappeared with Mungyeong after only three days, and the moment I saw their expressions, I knew something had happened.

“……What is it?”

After a long silence, it was Mungyeong—not the Divine Physician—who finally spoke.

“Formless Ultimate Poison.”

“What?”

“There is an unidentified, extremely deadly poison inside the patient’s body. That was the real cause.”

“W-Wait.”

My thoughts became tangled and chaotic.

Formless Ultimate Poison? Out of nowhere?

I looked at the Divine Physician in confusion.

“What does this mean?”

“It means exactly what you heard.”

Looking incomparably more haggard than he had three days earlier, the Divine Physician continued.

“While preparing the technique and examining the patient’s condition, I discovered something strange. The Scorching Yang Qi, which should have been growing more rampant, was gradually subsiding.”

“Then isn’t that a good thing? Suddenly bringing up poison—what does that have to do with anything…?”

“The technique has not even been performed yet. How could the Scorching Yang Qi be decreasing on its own?”

“That’s…”

“Did you not notice anything strange?”

At that moment, a thought suddenly flashed through my mind.

On the journey from Henan to Sichuan, I had periodically stabilized Jeok Cheongang’s qi with True Qi Guidance. Yet contrary to what I had been doing, Jeok Cheongang’s Scorching Yang Qi had continued to diminish.

*I thought he was simply growing weaker.*

The Divine Physician sighed when he saw my expression harden.

“When one type of energy gains the upper hand, the energy opposite it naturally grows weaker. But the patient was different. His Yin-Cold Qi remained unchanged, while his Scorching Yang Qi was gradually dwindling.”

“Are you saying that was because of the poison?”

“I do not know how it happened, but a Formless Ultimate Poison was hidden inside the patient’s body—one that even I would not dare touch. Whether it was a blessing or a misfortune, if the Scorching Yang Qi had not happened to wrap around the poison while it was running wild and played the role of using poison to control poison, he would have melted into a handful of blood long ago.”

“……!”

I did not know when or how the poison the Divine Physician called Formless Ultimate Poison had entered Jeok Cheongang’s body.

But I understood one thing clearly: the Scorching Yang Qi was acting as a breakwater and preventing the poison from spreading.

“Then… then does that mean even the technique cannot cure him?”

“The Life-Restoring Great Technique can regulate his qi and untangle his disrupted qi and blood, but it is not enough to detoxify a poison like that. If we perform the technique as things stand… the Scorching Yang Qi will be calmed, but we will have no way to stop the poison.”

I shouted urgently, “I’ll find an antidote! The Sichuan Tang Clan is here, isn’t it?”

“……Young Master.”

The Divine Physician shook his head, his expression dark.

“I know very well that the Sichuan Tang Clan is the greatest authority in the world when it comes to poison. But this poison…”

His voice trailed off, and my heart seemed to drop into my stomach.

*Even the Sichuan Tang Clan isn’t enough?*

Damn it. This was a truly fucking awful situation.

At that moment, Jeok Cheongang’s body was like a cage containing two savage wolves that were keeping each other in check.

If either one disappeared, the other would be free to run wild.

And now there was no way to detoxify the poison.

*What the fuck…!*

Tap. Drip.

Blood fell from my tightly clenched fist. My throat burned as if I had swallowed a fireball.

Just as I was holding back the curses that were about to burst out, someone’s voice pierced my ears.

“There is a way.”

I opened my closed eyes and saw the boy’s face. Mungyeong continued with an expression more serious than I had ever seen before.

“Let us go to the Sichuan Tang Clan.”

The Divine Physician looked at his Disciple with a dark expression.

“Mungyeong. As you know, this Formless Ultimate Poison…”

“I know, Master. I clearly remember you saying that the Tang Clan’s poison arts focus on killing, and that their detoxification techniques are lacking. But…”

Mungyeong looked straight at me with clear eyes.

“If the Sichuan Tang Clan possesses a legendary treasure—a sacred artifact said to detoxify any poison under heaven—then it is possible.”

Ding.

> **System**
>
> - Quest, **Myriad-Poison Ring**, has been generated!
## Chapter artifact 344

# Chapter 344

Ding.

> **System**
>
> - Chain Quest, **Myriad-Poison Ring**, has been generated!
>
> - There is something you must accomplish. You cannot refuse!

I stared at the holographic window that filled my vision along with the System notification.

> **System**
>
> **Quest**
>
> **Myriad-Poison Ring**
>
> The Myriad-Poison Ring, said to absorb any poison under heaven, is a sacred artifact of the Sichuan Tang Clan and one of the legends passed down through the Murim.
>
> Its owner and even its existence are uncertain, but for now, it is the only possible solution!
>
> **Grade:** Peak
>
> **Restriction:** Jin Taekyung
>
> **Mission:** Acquire the **Myriad-Poison Ring** — Incomplete
>
> **Reward:** A large amount of EXP
>
> **Failure:** Jeok Cheongang's death

“A sacred artifact said to absorb any poison.”

Mungyeong nodded at my mutter.

“That is the Myriad-Poison Ring’s ability. However, there is one problem…”

“Its owner and even its existence are uncertain.”

“Yes. The Sichuan Tang Clan has even denied the existence of the Myriad-Poison Ring several times.”

The Divine Physician added in a heavy voice, “That is why it is a legend. It is so old that it has been passed down only through people’s mouths.”

After thinking for a moment, I suddenly opened my mouth.

“No. It exists.”

“Hmm?”

“The Myriad-Poison Ring definitely exists. It’s just being kept hidden.”

“How can you be so certain?”

Both the Divine Physician and Mungyeong, who had first brought up the Myriad-Poison Ring, stared at me with wide eyes.

“Obviously because…”

Because of the System.

This was a Chain Quest to treat Jeok Cheongang.

If the Myriad-Poison Ring truly did not exist, a Quest like this would never have been generated.

Of course, if I said that out loud, they would definitely think I was insane.

I naturally continued, “If such a sacred artifact existed, would people really leave it alone? The Sichuan Tang Clan is famous throughout the Murim for being stubbornly reclusive. Naturally, they would want to avoid any unnecessary trouble.”

This was a world where people killed one another over a single coin or a dumpling. If the treasure in question were something like the Myriad-Poison Ring, just imagine how many flies would swarm around it.

It was a hastily improvised explanation, but it was convincing enough that everyone nodded.

“That makes sense. In fact, after conducting an extensive investigation into whether the Myriad-Poison Ring truly exists, even our sect—”

I looked at Gung Gibang, who had opened his mouth as if he had been waiting for this moment.

“Forget it. Stay here and tell Mujin the rest.”

“Huh? Stay? You want me to stay here with Hyuk Mujin?”

“Captain, what do you mean?”

“What do you think I mean? Exactly what you heard.”

I pointed at the two bewildered men in turn.

“Hyuk Mujin and Gung Gibang are staying here.”

“Why? Why me?”

“I want to go with you too! Please, don’t leave this vicious beggar and me behind!”

“What? You worthless bastard!”

Smack! Smack!

Sometimes, a good beating was the best medicine. I shook my fists at the two men, who were clutching the tops of their heads.

“Stop talking nonsense and stay here to guard Venerable Myoryeong. If anything happens, Gung Gibang, you contact me immediately.”

“Contact you? Is there a messenger pigeon here that can fly to the Sichuan Tang Clan?”

“What kind of beggar’s-foot-rag nonsense is that? If something happens, you need to come running after us so fast your feet catch fire.”

“What do you mean?”

“If you don’t like that, tame one. There were plenty of butterflies in the flower garden.”

It was a conclusion I had reached after a cold analysis, brief though it had been.

Hyuk Mujin’s martial arts were the weakest among us, especially his movement technique, so I would leave him behind and keep Gung Gibang with him as a precaution against any unexpected situation.

Gung Gibang was a reasonably capable Peak master, and his feet were as quick as his wits. He would be able to handle any unforeseen crisis.

“Anyone dissatisfied with my decision or curious about something, raise your hand immediately.”

“Put that fist down before you ask.”

“I’ll just stay here.”

At that moment, one person’s arm shot into the air. Cheongpung asked with an innocent expression, “What about me, Benefactor?”

“You’re coming with me to the Sichuan Tang Clan, Young Hero Cheongpung.”

“Why?”

“Who knows what kind of trouble you’ll cause if I leave you behind? Don’t leave my sight even for a moment. Got it?”

“Yeees…”

At Cheongpung’s dejected reply, the Divine Physician spoke with pity in his eyes.

“Do not scold him too harshly. He seems like an innocent young man.”

“He is innocent. Innocent enough to start a forest fire and burn this whole place to the ground.”

“Hoho, surely he would not go that far.”

“Within a few days, he’ll burn this whole place down and leave Old Man Dong homeless—and I’ll bet Mujin’s left wrist the old man ends up joining the Beggars’ Sect.”

“……!”

The Divine Physician studied Cheongpung with a wary expression before answering.

“It would be best if he came with us.”

“A wise choice.”

“Gyeong, what will you do?”

Mungyeong thought deeply for a moment, then nodded as if he had made his decision.

“I will follow my Master as well. The Emei nun should have no trouble as long as she gets some rest.”

“I would appreciate that.”

The person I needed most right now was actually the Divine Physician. But having Mungyeong with us would be even better. He was always at his Master’s side, serving as a capable assistant.

Besides, he was the one who had first brought up the Myriad-Poison Ring.

*The only thing left is figuring out how to obtain it.*

Myriad-Poison Asura Tang Sadok. If I met him, the head of the Sichuan Tang Clan, I would know for certain.

Once I had finished thinking, I turned to Cheongpung.

“Young Hero Cheongpung, grab two A-frame carriers and two ropes. Make them big and sturdy.”

“Benefactor, why do we need the carriers and ropes?”

“We need to get there as fast as possible. It’d be a disaster if we dropped you along the way, so we’ll tie you both down tight with the ropes.”

The Divine Physician’s and Mungyeong’s faces turned deathly pale.

* * *

The dark main hall was silent. Even after the middle-aged man entered, it was a long while before the old man finally opened his mouth.

“Some fifty years ago, before you were even born, our family suffered a great humiliation. Do you know about it?”

At the Myriad-Poison Asura Tang Sadok’s words, the middle-aged man lowered his head.

“How could I not?”

“This old man was barely twenty at the time, and I witnessed it all with my own eyes. Our people died all around us, the armory burned, and the pavilions collapsed. We were defeated and forced to withdraw from Sichuan.”

The great war that lasted ten long years ended with the orthodox faction’s victory. The Tang Clan returned to Sichuan and rebuilt its family, but the scars from that time had been carved deeply into everyone’s hearts.

“And yet—how? How could we suffer such humiliation again?”

The instant green light flashed in Tang Sadok’s eyes, the middle-aged man held his breath as poisonous energy poured from Tang Sadok’s entire body.

“Hngh.”

“How dare they make us suffer this kind of humiliation again!”

Sssssss!

Tang Sadok’s wrinkled hand pressed down on the table—or rather, melted it.

Not only the wood but even the iron fittings along the corners liquefied into black poison and flowed across the floor. The middle-aged man immediately prostrated himself.

“Please calm yourself, Family Head!”

Despite the middle-aged man’s pleas, Tang Sadok’s anger did not easily subside.

His fury was only natural. Instead of finding the culprit who had harmed his father, Poison King Tang Taesang, he had returned after chasing false leads and receiving an urgent message from the Qingcheng Sect.

“How dare they…!”

The message sent by the Qingcheng Sect had been brief. It had also been as shocking as the Poison King’s death.

*He killed Heaven-Shaking Venerable Nun and three Emei Elders all by himself.*

And it had not been an assassination targeting a single person. It was said to have been a head-on fight.

Heaven-Shaking Venerable Nun was a Supreme Peak master who could have aimed for even the lowest position among the Ten Kings. The three Elders who had been with her were also experienced Peak masters.

The killer had single-handedly brought down the leadership of an entire sect, then vanished like a ghost.

*There can’t be two masters of that level. It must have been the same bastard who harmed Father.*

As his anger slowly subsided, wariness took its place.

He had decided to return not as a son but as the Family Head of the Sichuan Tang Clan. At the same time, he had not forgotten to pursue the culprit.

“What became of the Green Shadow Squad?”

“They divided into ten groups of five and scattered from Chengdu toward Qingcheng, Emei, Yishan, and Sanhe to carry out their missions.”

Even within the Sichuan Tang Clan, the Green Shadow Squad were specialists in intelligence gathering and assassinating key targets.

They had been chiefly responsible for eliminating countless demon heads immediately after the Great Faction War, but Tang Sadok felt an inexplicable sense of foreboding.

“Do not let your guard down. Strengthen the defenses of the Gate Guard Pavilion, and do not allow anyone to enter.”

“Yes.”

“You may leave.”

As Tang Sadok watched the middle-aged man turn away cautiously, he suddenly spoke.

“Once this matter is over… hand the position of Master of the Gatekeeper Pavilion to someone else and move to the Inner Hall.”

“F-Family Head?”

“I’m saying this as your uncle, not as the Family Head. You’re nearly fifty. How long did you think I would leave my only nephew in the Gate Guard Pavilion?”

“Th-Thank you, Uncle.”

Tang Sadok answered by flicking his sleeve.

His nephew was not exceptional, but neither was there anything particularly lacking in him.

Tang Sadok had grown numb with time and lived for many years without thinking about it. Yet recently, he had begun remembering his elder brother, who had lost his life during the Great Faction War.

“I suppose I’m growing old too, Father.”

At Tang Sadok’s quiet monologue, spoken after he was left alone, his chest rose and fell. Then something slowly poked its head out.

Hiss. Hiss.

It had a body as white as snow, blue eyes, and a triangular head with two horns. It was a snake.

A spiritual creature known throughout the Murim as the Thousand-Year Poison Horned Snake, it was notorious for its ferocity. It stuck out its long tongue and licked Tang Sadok’s cheek.

“You little rascal…”

Tang Sadok’s stiff expression slowly softened.

He had a prickly personality and disliked meeting people, but he made an exception for this Thousand-Year Poison Horned Snake.

It was the first and last gift he had ever received from his father, the Poison King. Since Tang Sadok had no children of his own, the snake was more precious to him than anything.

“Hey, that tickles. You little thing.”

He was watching the snake play with a faint smile when the sound of someone’s approaching footsteps grew closer.

The white body hurriedly slipped inside Tang Sadok’s robes.

“What is it?”

“Family Head, it’s me.”

At the voice of his nephew, who had left only moments earlier, Tang Sadok deliberately furrowed his brow.

“Why have you come back?”

“Well, those people have come again.”

“Those people?”

“Sleeping Dragon of Shanxi Jin Taekyung and Huashan Divine Dragon Cheongpung.”

“I believe I explicitly ordered that no one be allowed inside. Denied.”

“But… one of them may be the Divine Physician.”

“What? The Divine Physician?”

For once, even Tang Sadok could not hide his surprise.

*Who was the Divine Physician? A man who had reached the realm of the divine through his medical arts. An unknown figure who had not shown himself for many long years.*

*Why had that very Divine Physician come to our family?*

His hesitation did not last long. A hoarse voice escaped between Tang Sadok’s lips.

“Let them in.”

* * *

“Are you the Divine Physician?”

Now that was some no-brakes macho-man talk.

Tang Sadok had asked the question out of nowhere without even pretending to look at us, and the Divine Physician let out a hearty laugh.

“This old man’s name is Dong Feng.”

“Then you are not the Divine Physician?”

“People have given this old man an undeserved name.”

“Seems they were right.”

“You believe me rather easily.”

“Unless someone has a death wish, no one tells lies in front of this old man.”

“……”

That was pretty damn convincing.

Tang Sadok slowly looked us over, his eyes filled with their usual green light.

“The Divine Physician… You, whom the whole world has searched for without catching even a glimpse of you, have come looking for me. And you have brought young prodigies of the Murim with you. Why?”

“May I answer that?”

I stepped forward, and Tang Sadok’s gaze collided with mine in midair.

“Go ahead. If you say something nonsensical, be prepared to become a handful of blood…”

“Please lend me the Myriad-Poison Ring.”

At my no-brakes macho-man approach, Tang Sadok’s pupils trembled.

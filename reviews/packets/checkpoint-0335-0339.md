# Checkpoint Review — 335–339

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

# Chapters 335–339

## Plot

Jin Taekyung’s party enters the fortified Sichuan Tang Clan, where Tang Sadok reveals that his father, Poison King Tang Taesang, was tortured and murdered. The clan refuses direct aid in finding the Divine Physician while independently pursuing the unidentified killer, who survived severe poison exposure by amputating his own left forearm.

After leaving the Tang Clan, Taekyung divides his forces. Mungyeong returns to his Master with medicinal prescriptions and herbs; Gung Gibang and Hyuk Mujin seek help from the Emei Sect; and Taekyung and Cheongpung recruit the Qingcheng Sect and the Sichuan authorities. Qingcheng’s leader mobilizes hundreds of disciples, two Elders, and the sect’s lay network. Using Prince Shangshan’s one-use Token, Taekyung secures the cooperation of Sichuan’s City Lord, Won Gyun, who deploys several thousand troops, local constables, official notices, and a thousand silver nyang reward.

Government and Murim conduct a joint search across Sichuan for three days, but the Divine Physician remains unfound. Gung Gibang and Hyuk Mujin return from Emei with only one reinforcement: Venerable Myoryeong, a severely injured nun coughing blood from an internal wound. Taekyung demands an explanation for her condition.

## Continuity

- Jin Taekyung and Cheongpung remain in Sichuan seeking the Divine Physician; Hyuk Mujin and Gung Gibang support the search.
- Jeok Cheongang remains unconscious and steadily weakening, with at most roughly half a year left without treatment. Taekyung still possesses the Thousand-Year Snow Ginseng.
- The Divine Physician’s Token points to Sichuan through its Chinese-gallnut clue, but the Divine Physician’s location remains unknown.
- The Qingcheng Sect has committed hundreds of disciples, two Elders, and its lay-disciple network to the search.
- The Sichuan government has committed several thousand troops, local constables, official notices, and a thousand silver nyang reward. Prince Shangshan’s Token has been used and cannot be used again.
- Won Gyun is the corrupt City Lord of Sichuan Province but is currently cooperating with the search.
- Venerable Myoryeong is the Emei Sect’s sole reinforcement and has arrived with a severe, unexplained internal injury.
- Tang Taesang, the former Family Head and Poison King of the Sichuan Tang Clan, was tortured and murdered. Tang Sadok is pursuing the unidentified killer independently and has promised the Tang Clan’s full assistance after its revenge is complete.
- The killer survived poison exposure by amputating his left forearm; his identity and unfinished objective remain unresolved.
- Mungyeong has returned to his Master after obtaining prescriptions and medicinal herbs from the Tang Clan.
- Ju Hwaran continues investigating traitors within the Yongbong Escort Bureau. Song Ilseom will remain for roughly one month before seeking Ju Hogun’s elixir in Xianyang.

## Translation Decisions

- Use **Sichuan Tang Clan**, **Tang Sadok**, **Tang Taesang**, **Poison King**, **Divine Physician**, **Divine Physician’s Token**, **Qingcheng Sect**, **Emei Sect**, and **Venerable Myoryeong**.
- Render **Cheongpung the Ancient Sword** for the Qingcheng Sect leader and keep him distinct from the companion **Cheongpung**.
- Use **Mount Qingcheng**, **Mount Emei**, **Shangqing Palace**, and **Qingcheng Seventy-Two Swordsmen**.
- Render **Won Gyun** for 원균 and preserve his role as Sichuan’s City Lord.
- Continue rendering **Chinese gallnut** for 오배자, **Young Master** for 공자님, **Old Master** for 노야, and **Ship-Fire Boy** for 선화아.

## Durable state

{
  "active_continuity": [
    "Jin Taekyung and Cheongpung remain in Sichuan seeking the Divine Physician, with Hyuk Mujin and Gung Gibang supporting the search.",
    "The government and Murim are conducting a joint search throughout Sichuan after Taekyung secured Won Gyun's cooperation with Prince Shangshan's Token.",
    "The Qingcheng Sect's two Elders and hundreds of disciples are participating in the search.",
    "The Divine Physician remains unidentified and unfound somewhere in Sichuan.",
    "The Emei Sect's sole reinforcement, Venerable Myoryeong, arrived severely injured with an internal injury, and the cause is unknown.",
    "Jeok Cheongang remains unconscious and steadily weakening, with at most roughly half a year remaining without treatment.",
    "Tang Sadok continues leading the Sichuan Tang Clan's pursuit of Tang Taesang's killers and has promised assistance after the clan's revenge is complete.",
    "Tang Taesang's murderer and the killer's unfinished objective remain unresolved.",
    "Mungyeong has returned to his Master after obtaining medicinal prescriptions and herbs from the Sichuan Tang Clan.",
    "Taekyung possesses the Thousand-Year Snow Ginseng, and the Divine Physician's Token still points to Sichuan's Chinese gallnuts.",
    "Ju Hwaran remains the Yongbong Escort Bureau's Young Bureau Head while investigating its traitors; Song Ilseom remains for one month to help her before seeking Ju Hogun's elixir in Xianyang."
  ],
  "continuity_sources": [
    339,
    338
  ],
  "open_questions": [
    "What caused Venerable Myoryeong's severe injury, and can the Emei Sect provide useful assistance?",
    "Can the Divine Physician be found and treat Jeok Cheongang before his remaining time expires?",
    "Who was the middle-aged man who killed Tang Taesang, and what unfinished objective was he pursuing?",
    "Can the Sichuan Tang Clan identify and destroy the culprits behind Tang Taesang's murder?",
    "Which other Yongbong Escort Bureau members collaborated with Heo Jun, and how will the Zhongnan Sect's leaders and wider organizers respond?"
  ],
  "safe_through": 339,
  "temporary_decisions": [
    "Render 선화아 as Ship-Fire Boy and retain Mu Song for 무송.",
    "Render 사천당문 as Sichuan Tang Clan and 당가 as Tang Family when the source distinguishes the forms.",
    "Render 공자님 as Young Master, 화타 as Hua Tuo, and 노야 as Old Master in their established contexts.",
    "Render 미산 as Meishan, 월영살곡 as Moonshadow Assassination Valley, 곡주 as Valley Master, and 신의의 증표 as Divine Physician's Token.",
    "Render 청풍고검 as Cheongpung the Ancient Sword and keep it distinct from 청풍, Cheongpung."
  ],
  "version": 1
}

## Reading copies

## Chapter artifact 335

# Chapter 335

Like Sichuan Province in the real world, Sichuan in this world boasted a vast territory.

Shanxi, Henan, and Shaanxi. You had to combine all three provinces for their total area to rival Sichuan’s. That was how enormous it was.

*The continent really is something.*

With land this vast, it wasn’t all that strange for three tigers to coexist in a single province.

*The Emei Sect and Qingcheng Sect, both counted among the Nine Sects and One Gang. And…*

Finally, the Sichuan Tang Clan. Or the Tang Family.

One of the three tigers crouching in Sichuan, it was also the closest to Chengdu, making it the perfect first destination.

*If we can get the cooperation of all three factions and bring the Beggars’ Sect into the picture, things should go much more smoothly.*

As I was thinking this, Gung Gibang, who had been following one step behind me, pointed ahead.

“We’re almost there. The Sichuan Tang Clan.”

He was right. A wide basin stretched out before us. Rising high above it was a stone wall.

We were still too far away to judge its exact height, but it looked like it easily exceeded ten meters.

“What the hell? Why did they build a fortress?”

“They learned from history.”

“History?”

“They suffered terribly during the Great Faction War. When the Demonic Cult occupied Sichuan, many members of the Tang Family were killed, and even Tang Family Hill, the clan’s main base, was burned down.”

“Their home base got completely wrecked.”

“Not entirely. As they retreated, they released all kinds of deadly poisons, so the Demonic Cult bastards who charged in without knowing what they were doing died in droves, too. Do you know what the Sichuan Tang Clan’s motto is?”

“Uh… ‘The North Remembers’?”

“……What the hell are you talking about?”

“You know nothing, Gung Snow.”

Gung Gibang looked at me as though he were staring at a madman before opening his mouth.

“Repay kindness twofold. Repay grudges ten thousandfold.”

“Damn, that’s intense.”

“It was. The demonic, heterodox bastards who sided with the Demonic Cult during the occupation of Sichuan died while shitting and pissing through all seven apertures.”

“Poisoning?”

“Poisoning, assassination, and even sending out pursuit squads to hunt them down independently. They died in all sorts of ways. A few may have survived through sheer luck, but they probably weren’t really living even if they were alive.”

I could understand why.

The people approaching us from the other side might be assassins sent by the Tang Clan. Maybe one of them had poisoned the teacup. Trapped in a prison created by psychological pressure, their nerves would have been shot for the rest of their lives.

They probably trembled in the corner of a room with a sword in one hand and a silver spoon in the other.

“When it comes to poison and hidden weapons, the Sichuan Tang Clan is number one under heaven. No one can match them in being closed-off and relentless. Did you see anyone from the Sichuan Tang Clan at the Star-Array Grand Banquet?”

Thinking back, I didn’t think I had seen a single one.

Even factions that hadn’t sent their young prodigies to participate in the Star-Array Grand Banquet, such as the Nangong Family, had sent important figures. But I hadn’t heard that anyone from the Sichuan Tang Clan had come.

“I don’t think so.”

“Right? There wasn’t anyone?”

“No. There really wasn’t.”

“That’s the Sichuan Tang Clan.”

*They did whatever the fuck they wanted. No backing down.*

I could feel it. The more I listened, the more uneasy I became.

*What if they turn us down flat?*

I had even brought a letter from the Sword Saint Mae Jonghak to request their cooperation, but the uneasiness refused to go away.

I was suppressing those thoughts and using my movement technique when Gung Gibang suddenly spoke.

“We should walk from here.”

“Do we really have to?”

“They probably won’t like it if we suddenly approach at high speed.”

“They might like it.”

Gung Gibang pointed at a massive boulder a few paces ahead.

Written across it in blood-red letters were the following words:

> Anyone who approaches without permission will pay a blood debt.

“Let’s walk. I’ve wanted to walk for a while now.”

“……”

“Hey, sometimes you need to look around at the scenery and gaze up at the sky. That’s what living like a normal person is about.”

Gung Gibang, Hyuk Mujin, and I stopped using our movement techniques.

But one person did not.

With a fierce gust of wind, a figure shot straight toward the front gate.

*Whoooosh!*

“Hellooo!”

“Cheongpung, you crazy bastard!”

“I’m Cheongpung!”

A boy of similar build was riding on his back as Cheongpung shot forward, waving energetically.

Cheongpung spoke to Mungyeong, who was swaying pitifully in every direction.

“Medical apprentice, say hello!”

“H-Hello!”

*Please don’t.*

*Don’t make him do anything weird. And don’t do it just because he tells you to.*

I lunged forward to grab Cheongpung by the scruff of his neck, but the Sichuan Tang Clan’s answer came faster.

*Whoooosh! Boom!*

A massive spear as tall as a grown man hurtled down from atop the stone wall. It buried itself directly in front of Cheongpung’s foot, its shaft quivering.

Then, in the next instant—

“Who are you people?”

*Clatter-clatter-clatter!*

Along with the shout, which carried powerful internal energy, dozens of crossbows appeared above the stone wall.

Between the countless arrowheads glittering in the sunlight, a middle-aged man with his eyes wide open shouted at us again.

“Outsiders, identify yourselves!”

Cheongpung answered.

“Hello! I’m Cheongpung!”

“I-I am Mungyeong. P-please show mercy and lower your weapons, and I shall repay this grace even if this body dies and dies, then dies a hundred times over, until—”

“Mmph! Mmph!”

*Stop it, you trolls!*

I hurriedly clamped both hands over Cheongpung and Mungyeong’s mouths before bowing repeatedly toward the stone wall.

“I’m sorry. I’m sorry. The kids are still immature. My name is Jin Taekyung of the Jin Family of Taiyuan.”

“Jin Taekyung of the Jin Family of Taiyuan?”

The middle-aged man’s eyes widened slightly as he thought.

“Jin Taekyung, the Sleeping Dragon of Shanxi—the Disciple of Great Hero Jeok Cheongang, the Fire King?”

“Yes. That’s me.”

I jerked my chin toward Gung Gibang, who had arrived a beat later, and continued.

“This is the Oseong-and-Haneum villain—no, the Beggars’ Sect Successor Beggar, Gung Gibang.”[^1]

“The Disciple of Great Hero Jeok Cheongang and the Beggars’ Sect’s Successor Beggar…”

His tone and expression remained suspicious, but the middle-aged man’s wariness had eased considerably.

When he crooked a finger, the crossbows aimed at us lowered toward the ground.

“What brings you to our family?”

“I’d like to meet the Family Head.”

“The Family Head?”

“Yes. It’s important.”

The middle-aged man frowned, apparently displeased with my answer, but this was not something we could announce to the neighborhood.

The Sword Saint Mae Jonghak was no fool. There was a reason he had written a handwritten letter and sent it by hand instead of using a messenger pigeon.

“His Excellency the Family Head has many matters to handle right now. Our family is not accepting any outsiders whatsoever, so withdraw and come another time.”

“You only need to deliver a message.”

“Impossible. The person who gave me this order was the Family Head himself. And if it was really that important, you should have contacted us in advance.”

*Why is he being so damn firm? I didn’t plan for this.*

Gung Gibang seemed to be thinking the same thing. He whispered in a voice as small as an ant.

“Something’s strange. Even for a closed-off place like the Sichuan Tang Clan, this is too much…”

I agreed. Pointing crossbows at us right away and maintaining such intense vigilance from the beginning were things one would expect only in wartime.

*What a warm welcome.*

Still, we had come to ask for their cooperation. I couldn’t simply complain. If we wanted to meet the Family Head, it seemed we would have to show him at least half our cards, even if we didn’t reveal everything.

*Can’t be helped.*

After hesitating for a moment, I stared straight at the middle-aged man and opened my mouth.

“I brought a letter from Great Hero Mae Jonghak, the Sword Saint.”

“……!”

“Please let me meet the Family Head.”

The effect was immediate. The Sword Saint Mae Jonghak was an idol to martial artists and a giant among giants who might become the Alliance Leader of the New Murim Alliance.

He was in a completely different league from greenhorns like us, who had only made names for ourselves within the past year or two.

“……Hmm. Wait here a moment.”

The middle-aged man let out a groan and disappeared from the top of the stone wall. He returned a short while later.

And his first words were practically a foregone conclusion.

“The Family Head has granted permission.”

The moment he finished speaking—

*Grrrrrrr.*

The enormous iron gate slowly opened its jaws with a grinding groan.

* * *

Not long after passing through the iron gate, I realized that my earlier suspicion had been correct.

*Something happened. There’s no doubt about it.*

The people who appeared to be members of the Sichuan Tang Clan were proof enough. Their guarded movements, tense eyes, and overall atmosphere said it all.

The sense of incongruity grew even stronger after we left the Outer Hall and entered the Inner Hall.

*Clang! Clang! Clang!*

Craftsmen hammered away at something without pause. Martial artists dressed in uniforms walked around in pairs, while crates loaded with weapons and hidden weapons were carried from place to place.

Gung Gibang and I exchanged Sound Transmission.

*“Hey, am I the only one getting a bad feeling?”*

*“That’s what I was thinking. It looks like they’re preparing for battle.”*

*“Could they have discovered some demonic fiend? Maybe one of the men who set fire to the Sichuan Tang Clan during the Great Faction War.”*

*“I don’t know. For now, we should keep our mouths shut and pretend we don’t know anything.”*

I had already been planning to do that. If they had intended to tell us, they would have done so already.

But the real problem was that the Sound Transmission had only reached me.

“Wow! I’ve never seen anything like this before! Are you preparing for a war or something?”

“……!”

“……!”

For a moment, I thought the world had stopped.

The craftsmen and martial artists around us stopped whatever they were doing and silently stared at us.

Hundreds of gazes pierced my entire body like hidden weapons.

*What sin did I commit in my past life to get tangled up with a bastard like Cheongpung?*

One second. Two seconds. Three seconds.

*Is this the Hyperbolic Time Chamber?*

By the time my mouth had dried out like the sand around the Sphinx’s front paws, the middle-aged man guiding us spoke to the others.

“What are you doing? Why aren’t you continuing your work?”

Only then did the world begin moving again.

The middle-aged man glanced at the people who had gone back to their tasks before casually tossing a remark at us.

“You all look tight-lipped. I like that.”

It sounded like a compliment on the surface.

But why did it sound like he was telling us to keep our mouths shut if we wanted to live long, healthy lives?

*Why? Because that’s exactly what he meant, damn it.*

Maybe it was because of the Tang Clan’s association with poison and hidden weapons.

The middle-aged man, along with the other members of the Tang Family, was clearly one level below me in skill, but they all gave off an unmistakably dangerous scent.

“Hold your breath. That’s poison mist. It smells awful.”

“……Oh. Yes.”

*So that was the dangerous smell?*

I glared at the blue-haired bastard, who was still looking around with a bright expression, and continued walking behind the middle-aged man.

I had no idea how long we walked.

During that time, we passed through five gates and finally stopped in front of the sixth.

“You cannot bring weapons into the Family Head’s Hall.”

Following the middle-aged man’s instructions, we handed over all our weapons. After that, the martial artists guarding the hall searched us as well.

*They’re incredibly strict.*

At that moment, one of the guards patting me down in search of hidden weapons suddenly flinched and shouted.

“There’s a hidden weapon here!”

“That’s not a hidden weapon. It’s my thing.”

“Pardon?”

“It’s mine. You know… that.”

“……!”

*What kind of humiliation play is this?*

I would rather pull out a poisoned hidden weapon than take that out in the Family Head’s Hall. It would be a much easier way to die.

After I reluctantly gave him permission to inspect the real thing, the middle-aged man’s eyes widened.

“You’re quite something.”

“……Could you just let me through without saying anything?”

“I understand. But you really are quite something.”

“Oh, please.”

Reading the sincerity mixed into my plea, he was about to order the guards to let us pass when he suddenly frowned.

“I nearly forgot. You there, stay behind.”

*Oh, right. He was here.*

The “you” the middle-aged man was referring to was Mungyeong.

“I hear you’re a medical apprentice who came to our family to obtain a prescription.”

Dragged along this far before he even knew what was happening, Mungyeong answered in a trembling voice.

“Y-Yes.”

“Under normal circumstances, it would be out of the question… but you were lucky enough to meet the right group. I’ll assign someone to you, so go take care of your business.”

“Th-Thank you.”

Mungyeong bowed deeply before disappearing with one of the martial artists. The middle-aged man took the lead and beckoned to us.

“Let us go inside.”

Twenty steps made of blue stone.

And a single door at the top.

“Uncle, it’s me.”

An elderly voice answered the middle-aged man.

“Come in.”

[^1]: Oseong and Haneum were famous Joseon-era friends whose names are commonly paired.
## Chapter artifact 336

# Chapter 336

An old tree.

That was the first thing that came to mind when I saw the old man.

Inside a dark pavilion blocked off by cloth on all four sides, the old man stood alone, his back to us. He looked just like an old tree that had lost all its vitality.

If he hadn’t slowly turned around the next moment, I might have thought he had already put down roots into the floor.

“Yeah…”

His two eyes glowed with a swirling green light.

The old man, Tang Sadok, the Myriad-Poison Asura, continued speaking in a voice that hissed like a snake.

“You brought a letter?”

The middle-aged man answered.

“Yes, Uncle. It was sent by Great Hero Mae Jonghak…”

“Did I ask you?”

“……”

“You have no place in this conversation. Leave.”

Realizing his mistake, the middle-aged man bowed and exited the pavilion.

After coldly driving his own nephew out with a few words, Tang Sadok reclined in a leather chair.

*Look at the old man’s presence.*

The problem was that it was the presence of a villain.

From his first impression alone, I could have believed he was from the Demonic Cult rather than the orthodox faction.

I stepped forward under Tang Sadok’s gaze.

“I’m Jin Taekyung of the Jin Family of Taiyuan. It is an honor to meet you, Great Hero Tang Sadok.”

Tang Sadok answered with an unreadable expression.

“I have heard that Senior Jeok took on a Disciple in his later years. I also know that he has ties to the Jin Family of Taiyuan.”

“Oh, really?”

That was a good sign.

Tang Sadok stroked his chin and seemed to think for a moment before suddenly speaking.

“His name was… Yes, the Blade of Flowers, Jin Baekyang. I remember now.”

*Good sign, my ass. That name keeps popping up whenever I’ve almost forgotten it.*

The Head Elder really must have been something in his day.

Then again, it made sense. He had been a Peak master who had distinguished himself during the Great Faction War. It wasn’t strange that he had formed friendships with other masters during that time.

*He even said he’d met the Fire King once or twice.*

Thanks to that, when I first met Jeok Cheongang, I got nailed with a Flame Divine Palm before I could explain the situation.

Tang Sadok stared at me and asked,

“How has Jin Baekyang been these days?”

“Well, you see…”

Before answering, I looked around.

It was so I could dodge quickly if a poisonous snake suddenly sprang out from somewhere or a hidden weapon came flying at me.

“He passed away.”

“What?”

*Yeah, I knew this was coming.*

I hurriedly continued speaking to Tang Sadok, whose eyes had widened.

“It was an unfortunate accident. There are circumstances behind it, of course. If you’d just give me a little time, I’ll explain everything without any misunderstanding—”

“No need.”

“Excuse me?”

“He was an obnoxious bastard. Every time people praised him as some Great Hero or chivalrous knight, it soured my mood.”

“……”

“There is no such thing as a death without reason for a martial artist. Dead is dead.”

Things were going smoothly, which was a relief, but the old man’s personality was almost poisonous enough to kill.

Wasn’t he basically saying that it was good that an unpleasant bastard had died?

*His personality is practically on Dark Heaven’s level.*

Whether he knew about the suspicion growing in my heart or not, Tang Sadok waved his hand as though I were a nuisance.

“Enough about the dead. Let us get to the point. Great Hero Mae Jonghak sent me a letter?”

“Yes. It would be faster if you read it yourself.”

I pretended to search inside my robes and summoned the Sword Saint’s handwritten letter from my inventory.

Tang Sadok accepted the letter and began reading. The furrows between his brows deepened, and at last, a roar filled with fury burst from his throat.

“What kind of sons of bitches are these?!”

*Whoooom!*

The pavilion trembled from the shout, which carried profound internal energy.

Tang Sadok’s green robes fluttered as he vented his anger. Then he asked in a voice that sounded as though he were chewing and spitting out every word.

“Is everything written in this letter true?”

“Yes. It is exactly as written.”

The Sword Saint’s letter laid out the events in Henan in an orderly fashion. It also asked Tang Sadok to actively cooperate in finding the Divine Physician so that Jeok Cheongang could be treated.

“To think Senior Jeok’s condition is so critical…”

“Actually, there’s something I’d like to ask before we go looking for the Divine Physician.”

The Sichuan Tang Clan was known throughout the martial world for poison and hidden weapons, but each and every member of the family was also a skilled physician.

And among them stood one person at the very peak.

I looked straight at Tang Sadok and asked,

“Could I meet the Grand Family Head?”

Poison King Tang Taesang.

A Supreme Peak master who had been called the greatest in the world when it came to poison and hidden weapons, even before the Great Faction War.

He had dominated an entire era. Twenty years ago, he handed the position of Family Head of the Sichuan Tang Clan to his only child and disappeared.

That child was the old man standing right in front of me—Tang Sadok.

“It may take several days or even longer to find the Divine Physician. Before then, if the Poison King could examine my Master’s condition…”

“Enough.”

Tang Sadok cut me off. His face had hardened as he spoke.

“Impossible. That is this old man’s answer.”

“……”

My chest dropped with a thud at the unexpected response.

Even though Poison King Tang Taesang had not shown himself for many years, Tang Sadok clearly knew where he was.

Impossible. He knew, yet he was saying that he would not help.

A trembling voice slipped between my lips.

“W-Why?”

“I cannot say.”

“You cannot say?”

“Instead, I will assign several people to guide you. If you go to Qingcheng and Emei, they will gladly help you.”

*What did I just hear?*

This shock was several times greater than the first.

Tang Sadok’s words meant that the Sichuan Tang Clan would not help us with this matter.

It wasn’t that they would provide no assistance at all.

*A few guides to lead us to the Qingcheng Sect and Emei Sect.*

That was it.

That was all the help we could receive from the Sichuan Tang Clan.

The back of my head felt numb, as though I had been struck with an iron club. Something hot abruptly surged up from the corner of my chest.

“Is that all?”

“What more help did you expect?”

“We need to find the Divine Physician!”

“That is your problem, not mine or our family’s. It makes no difference that you brought a letter from Great Hero Mae Jonghak. It was a request, and this old man refused. That is all.”

The words caught in my throat.

Everything Tang Sadok had said was correct. To him, and to the Sichuan Tang Clan, all of this was a choice—not an obligation.

*Right. That was how it was.*

When I finally accepted the truth I had been desperately hoping wasn’t true, disappointment and anger surged up inside me.

Just as I stood there at a loss for words, someone stepped forward amid the sweet scent of snacks.

“I am Cheongpung of Huashan. It is a pleasure to meet you.”

I had never seen that side of him before.

Cheongpung clasped his hands with an expression and tone I had never seen him use before, then continued.

“I do not know why the Family Head refuses, but if you help us, I will never forget this kindness.”

“I know that you are Great Hero Mae Jonghak’s Disciple. One must be careful when forming debts of gratitude and grudges in the martial world. Do not poke your nose into matters that do not concern you. Withdraw.”

“I’m not poking my nose into anything.”

“Then what are you doing?”

Cheongpung answered with a clear, unwavering gaze.

“My grandfather called it human compassion.”

“……”

Tang Sadok stared at Cheongpung with a complicated expression before shaking his head.

“Even if Great Hero Mae Jonghak came to me personally and asked, this old man’s answer would not change.”

“But…”

Just as Cheongpung, Gung Gibang, and Hyuk Mujin all began to speak at once, I cut in with a single question.

“What is the reason?”

“The reason?”

“Even a stray dog passing by knows how much power the Sichuan Tang Clan possesses. So why in the world are you refusing?”

“What will you do if I do not wish to tell you the reason?”

“What will I do?”

I stared into Tang Sadok’s green eyes and answered,

“Then the gratitude and grudges you mentioned will be established between me and the Sichuan Tang Clan. I should warn you that they will not be the pleasant kind.”

“……”

“Hah. What a fearless brat.”

“Normally, I check where I’m lying before I stretch out my legs, but in this case, I’m in a bit—well, a lot—of a hurry.”

At most, Jeok Cheongang had about half a year left.

The Divine Physician was someone even the most renowned martial sects under heaven and the Imperial Court had failed to find.

If Jeok Cheongang died because he could not receive treatment in time… If it happened because the Sichuan Tang Clan had refused to help…

“Then I don’t know what I’ll do.”

When I finished speaking, suffocating silence filled the pavilion.

Tang Sadok stared at me for a long time with deep, unfathomable eyes. Then he finally parted his lips.

“It is unfortunate that Senior Jeok ended up in such a state.”

“If you feel sorry for him, why not help us?”

“This old man would like to. But what can I do? Our family does not have that kind of room to spare right now.”

No room to spare?

The moment I heard those words, the scenes I had witnessed on the way here flashed through my mind.

An atmosphere so grim it was practically murderous. Artisans constantly making something without pause. Weapons being carried somewhere every few moments.

“What in the world is going on?”

“Going on?”

*Step.*

Tang Sadok took a step toward me.

Perhaps because of the poison arts he had cultivated, the green in his eyes gleamed more eerily than ever. And within that green light were anger and sorrow.

“The matter has already happened. Now all that remains is to mobilize every ounce of our family’s strength and slaughter every culprit involved.”

That was it.

That was why the Sichuan Tang Clan could not help us right now.

That was why Tang Sadok had not been able to easily say anything even after a green young brat like me challenged him to his face.

That was why this matter took priority over finding the Divine Physician and saving the Fire King’s life—and why he had flatly refused to let me meet Poison King Tang Taesang.

“Surely…”

Perhaps he noticed that I had realized the truth.

Tang Sadok looked at me as I stared back wide-eyed, then spoke in a voice filled with killing intent.

“When we received the news, everything was already too late. Not one of his limbs was left intact.”

Those words turned my suspicion into certainty.

Poison King Tang Taesang was dead.

* * *

“Hmm.”

The middle-aged man was of average height and had a round face. He possessed the sort of ordinary appearance one could see anywhere.

Leaning against the wall of a pitch-black cave, he carefully examined his forearm and muttered,

“This won’t do. The poison is vicious.”

The middle-aged man clicked his tongue softly.

He had done everything he could, but the most he had managed was to drive the poison into one arm.

“Poison King… He was fierce. More than I expected.”

Poison King Tang Taesang.

The expression on Tang Taesang’s face as his breath finally left him was still vivid in the middle-aged man’s mind.

But it had been a terrible result for him.

He had succeeded in eliminating a Supreme Peak master known as the Poison King, but he had failed to accomplish something more important.

*I never thought it would be easy, anyway.*

After muttering inwardly, the middle-aged man suddenly brought the edge of his hand down on his left forearm.

A blinding flash erupted.

At the same time, the severed forearm fell to the floor.

*Schhk! Ssssss!*

Blood thick with poison splattered and melted everything around it. Acrid toxic smoke rose from the wound.

Small creatures watching the middle-aged man from unseen places were exposed to the smoke and died without even knowing what had happened.

*Eek… Eeeek…*

Listening to the bats’ dying shrieks, the middle-aged man walked out of the cave.

When he saw the sunlight pouring down, he grinned.

It was a smile no one would have believed belonged to someone who had just cut off his own arm.
## Chapter artifact 337

# Chapter 337

Inside the broad, chilly pavilion, a draft forced its way through the gaps around the windows, making the oil lamp beside one of them flicker. An old man’s face slowly appeared superimposed over the wavering flame.

Eyes suffused with green light and a body as dry as an ancient tree.

The old man’s name was Tang Sadok. His alias was the Myriad-Poison Asura.

He was the Family Head of the Sichuan Tang Clan, one of the Five Great Families under heaven—and a son who had recently lost his father.

Whoooosh.

The cold wind beating against the closed window seemed to carry the voice I had heard several shichen ago.



*When I heard the news, everything was already too late. Not one of his limbs was left intact.*



The One God, the Three Saints, and the Ten Kings.

The heroes who had once saved the world from the hundred thousand forces of the Demonic Path had long since become white-haired old men.

Some had grown old or sick and died. Some had vanished after seeking peace. Others had handed their successors the responsibility and stepped down.

Poison King Tang Taesang had also left to find his own path.



*There’s a place called Meishan two days away. My father used to speak from time to time about the beautiful mountains of Meishan.*



More than twenty years ago, it had only been natural for the Poison King, who had stepped down as Family Head, to head for Meishan.

It must have been the final resting place chosen by an old martial artist who had spent his entire life battling the turbulent currents of Murim.



*He didn’t like people coming to visit. We had no choice but to send someone to check on him once in a while.*



And that had become a scar that would never fade.

Several days ago, unbelievable urgent news had arrived.

What Tang Sadok had witnessed when he rushed there in a panic was the aftermath of a battle that had shaken heaven and earth—and the Poison King’s corpse.



*My father’s body had been… severely mutilated. There was no doubt about it. They were unmistakable signs of torture.*



I did not know why the culprit had tortured the Poison King.

But Poison King Tang Taesang, a Supreme Peak master who had dominated an entire era, had died that way. At the hands of an unknown figure whose name and face were both a mystery.

Tang Sadok had been so furious that he personally led his family members in combing the surrounding area, but it had already been too late.



*I will find that bastard and kill him. I’ll tear his limbs apart and scatter them across the Nine Provinces, then let the blood flowing from his body run into the Four Seas and Five Lakes.*



What could anyone say to Tang Sadok as he raged, spilling suffocating killing intent? I understood his anger and determination well enough.

He and the Sichuan Tang Clan would never stop until they found the culprit and killed him. Naturally, they could not help us find the Divine Physician.

“Poison King Tang Taesang is dead. The Poison King himself…”

A massive tectonic shift was taking place. And it was happening right beside us.

Just as I muttered quietly while staring at the oil lamp, an urgent voice came from behind me.

“Watch your mouth. Do you have any idea what’ll happen if you say something like that in the middle of the Sichuan Tang Clan?”

It was not difficult to tell who the voice belonged to. I had sensed the presence of the three people approaching long ago.

Without turning my head, I answered,

“You’re back.”

“Not ‘you’re back.’ I said watch your mouth. Your mouth!”

“It’s fine. There’s no one nearby.”

“I’m saying we should be careful. Every time I’m around you, you scare the life out of me.”

Gung Gibang sighed and dropped into a chair. Cheongpung and Hyuk Mujin entered behind him and each claimed a seat.

“Where did you go?”

Gung Gibang answered curtly.

“The Chengdu branch of the Beggars’ Sect.”

“Mungyeong went with you?”

“Of course not. He’s holed up in the pavilion the Tang Clan provided separately. When I saw him earlier, he was so absorbed in a medicinal prescription that he didn’t even notice someone had entered. He’ll probably stay the night and leave with us tomorrow.”

“So? Did you find anything out?”

“No. It was a waste of time. I casually probed the branch leader about the Sichuan Tang Clan, but he didn’t know much either.”

That was understandable. From what I had heard, the Poison King’s residence had been prepared in a remote mountain valley that no one visited. Only a member of Tang Sadok’s household would secretly stop by from time to time.

*Besides, the Sichuan Tang Clan deliberately hid everything…*

Tang Sadok wanted revenge using only the power of his family.

Considering the power possessed by the Sichuan Tang Clan, a great Murim family, and the character they had displayed, their independent course of action was not strange at all.

“He did find it a little suspicious. Apparently, the Sichuan Tang Clan recently sent people to demand some information.”

“They’ve already caught the scent. Did you tell him?”

Gung Gibang hesitated for a moment before speaking.

“Although Great Hero Tang Sadok ordered everyone to keep silent… I’m the Successor Beggar of the Beggars’ Sect. I told the branch leader the truth and instructed him to keep an eye on anyone suspicious.”

“What about Young Hero Cheongpung?”

In the midst of the serious atmosphere, Cheongpung, who had been struggling to hold back a yawn, answered,

“I sent a messenger eagle to my grandfather, just as my Benefactor instructed.”

Gung Gibang nodded and added,

“The message will reach him within seven days at the latest.”

“Good. Well done.”

I thought we had taken the minimum necessary precautions.

Tang Sadok would be furious if he found out, but this was something I had to do.

“Um, Captain.”

“Hmm?”

Hyuk Mujin glanced around cautiously before speaking.

“May I ask you something?”

“If I say no, will you refrain from asking?”

“No. You know I can’t stand being curious about something.”

“……”

I was already so troubled that I could die from it, and this idiot was unbelievable.

I briefly considered giving him a good, satisfying smack for the first time in a while, but held myself back.

“What is it?”

“Why are you clenching your fist? That’s scary.”

“Stop stalling and just ask, you bastard.”

Hyuk Mujin stared warily at my fist and whispered,

“Who is the culprit?”

“The culprit?”

“Yes. The culprit who killed and even tortured Great Hero Tang Taesang, the Poison King.”

“Well, well. The culprit.”

Smack!

“Argh! Why did you hit me?”

“If I, knew, would I, be standing, here, like this? Huh?”

Smack! Smack! Smack! Smack!

I gave the back of his head several more blows without holding back. It felt wonderfully cathartic.

“Ugh… If you didn’t know, you could’ve just said so. Why…”

“You’re saying things that don’t even make sense. You’re pissing me off.”

“Th-that’s…”

Gung Gibang looked at Hyuk Mujin with contempt as he thrashed around, clutching his head.

“Tsk, tsk. What a man more foolish than a stray yellow dog. How would anyone know where that heinous bastard came from or who he was?”

Hyuk Mujin wiped away a tear that had trickled out and muttered,

“You spread out a mat beside that stray yellow dog and beg on the street.”

“What did you say?!”

“Why? Was I wrong?”

“How dare you insult our Sect!”

“They say you should call a spade a spade, so don’t misunderstand. I only look down on you, Young Hero Gung.”

Cheongpung burst out laughing and clapped.

“Wow! Benefactor! Young Hero Hyuk said he looks down on Young Hero Gung!”

“Don’t laugh! Stop him, you lunatic Cheongpung!”

Hyuk Mujin had gotten much better with his words.

I blocked Gung Gibang, whose eyes had nearly turned inside out after being struck by the facts, and said,

“Both of you, calm down.”

That did not seem sufficient, so I added one more thing.

“Unless you want me to beat you to death.”

“……”

“……”

That was better.

I let out a deep sigh as I watched them both huffing at each other.

“Who could know what kind of bastard the culprit is? If we knew, the Sichuan Tang Clan would have caught and killed him already.”

Hyuk Mujin still had not relaxed his eyes as he spoke.

“I know that. I mean, do you have no idea who it might be?”

“Think before you ask. Think, you foolish bastard.”

“But when did we ever become close enough for you to keep speaking informally? Is it acceptable to look down on the Vice Squad Leader of the great Jin Family of Taiyuan just because you’re the Beggars’ Sect’s Successor Beggar? Don’t you agree, Captain?”

…Actually, with that much of a difference between them, it did seem acceptable to look down on him.

When I did not answer, Hyuk Mujin’s eyes narrowed.

I subtly changed the subject.

“Well, the Murim is crawling with suspicious people. There are the Dark Heaven and Demonic Cult bastards, for starters.”

“Hmph! Do you think they’re the only possibilities?”

Gung Gibang snorted harshly and picked up the thread.

“The Sichuan Tang Clan has devoted all its strength to eliminating demonic, heterodox arts. It could have been someone with a personal grudge.”

I looked with disgust at the booger stuck to the bridge of Gung Gibang’s nose and asked,

“Weren’t all the demonic, heterodox practitioners wiped out already?”

“No matter how thoroughly you sweep a courtyard, sand remains. The world is vast. Do you really think there wasn’t anywhere for them to hide? Some people survived to the bitter end despite relentless pursuit.”

That was a valid point.

And if they had survived the pursuit of the orthodox Murim faction that ruled the world, every one of them had to be an incredible master.

*Like the Yin-Yang Twin Freaks I fought at Shaolin.*

Who could have imagined that two Supreme Peak demonic fiends believed to be dead would appear at Shaolin?

Murim was a place where countless chains of gratitude and grudges became tangled together. No matter what happened or where, nothing would be strange.

*And there was the torture.*

There were two reasons someone would torture another person.

Either they held enough of a grudge to want to inflict pain before killing him, or there was something they wanted to hear from his mouth.

I did not know the culprit’s purpose, but one thing was certain.

*…A filthy dangerous bastard has appeared.*

He was also someone I did not want to encounter, even by chance.

My current realm was at the very edge of Peak. I had not yet gained enlightenment, but with the power I had obtained through the System, I could face someone at the early stages of Supreme Peak.

*Hwangbo Eom, the Taeeul Merciless Sword, was a good example.*

But an opponent beyond that level would be difficult. In fact, if I had not gained a small insight during my battle with Hwangbo Eom, I might have been forced to kneel before his Taeeul Formless Sword.

And if the opponent was powerful enough to kill the Poison King, who had ranked among the top five of the Ten Kings…

*For now, I would lose without fail.*

As painful as it was, I had no choice but to acknowledge that reality.

While I was quietly lost in thought, Gung Gibang suddenly opened his mouth as though he had just remembered something.

“Come to think of it, the culprit could be an assassin.”

“A killer? An assassin?”

“Are there other kinds of assassins?”

I frowned.

“You think those bastards are that skilled?”

“You don’t know what you’re talking about. According to what I heard from my Master, the master of Moonshadow Assassination Valley has killed no fewer than three Supreme Peak masters.”

“…An assassin killed three Supreme Peak masters?”

“Without a doubt. I heard it threw the entire Murim into an uproar.”

“Then is that valley master or whatever the greatest assassin under heaven?”

Gung Gibang looked at me as though he had just spotted the most insane person alive.

“What are you talking about? The greatest assassin under heaven has never changed.”

“Oh.”

I had momentarily forgotten.

The Sword Saint. The Bow Saint. And finally, the man known as the Slaughter Saint.

*When I first heard it, I thought he was called the Slaughter Saint because he had killed a lot of people.*

As it turned out, being an assassin was his actual profession.

According to what I had heard from Jeok Cheongang, he had killed more people than anyone could count. He had slaughtered people from the orthodox, demonic, and heterodox factions alike, killing them all so fairly and evenly that he had even been branded an enemy of all Murim.

*That was, until the Great Faction War.*

He had killed so many demonic fiends that the people had no choice but to issue an amnesty decree for a man who had once been an enemy of all Murim—and give him the alias Slaughter Saint.

“Of course, it couldn’t have been the Slaughter Saint who killed Great Hero Tang Taesang, but the Sichuan Tang Clan will be keeping that possibility in mind.”

“It’s unfortunate, but they’ll deal with it themselves.”

Whoever the culprit was, I had only one goal: find the Divine Physician and save Jeok Cheongang.

It was unfortunate that we could not receive help from the Sichuan Tang Clan, but Qingcheng and Emei still remained.

That meant…

“Gung, did you pull that booger out in advance so you could eat it as a late-night snack?”

“What did you say?!”

“Wahahaha! Benefactor! Young Hero Gung is going to eat his booger as a late-night snack!”

…No. Seriously, what the hell was wrong with these bastards?

Unable to hold myself back any longer, I overturned the table.

“Get the hell out! We have to leave early tomorrow, so go get some sleep!”

I let out a lion’s roar and chased the Bermuda Triangle away before dropping back into my chair.

I stared absently at the flickering oil lamp, then muttered quietly,

“Inventory open. Summon.”

Tap.

A small jade-colored shard appeared in the palm of my hand.

When I turned over the **Divine Physician’s Token**, faint writing appeared.



> “The finest Chinese gallnuts come from Sichuan.”



“Chinese gallnut, my ass. They should’ve written down the damn home address.”
## Chapter artifact 338

# Chapter 338

That night, my mind was so full of worries and thoughts that I ended up staying awake until dawn.

*My body isn’t tired, but my mind is.*

Looking back, I had been through every kind of upheaval over the past few months.

If I hadn’t steadily cleared my body and mind by circulating my qi, I might have developed stress-induced hair loss.

I had even considered crossing over to reality for a while to rest, but a crazy skeleton mage was running wild over there.

*Come to think of it, that place is in Sichuan too.*

Was some kind of curse following me?

No wonder Shu was the first to fall in *Romance of the Three Kingdoms*.

Feeling vaguely uneasy, I left the pavilion with the pack frame on my back. The Bermuda Triangle was already outside waiting for me.

“Oh? The booger’s gone. Did you really eat it as a late-night snack?”

“Stop! I said stop!”

“Benefactor! Benefactor! They say Young Hero Gung ate that booger yesterday!”

“I didn’t!”

“……”

Ugh. I wanted to beat every last one of them to death.

If this were a novel and I were the author, I would find some way to kill those bastards.

But when did anything in this world ever go the way I wanted? It was just as I was slowly shaking my head—

“*Huff, huff.* I’m sorry I’m late!”

Right. There was that guy, too.

Mungyeong came running up, panting heavily.

“Huff… I, uh, stayed up late going over medicinal prescriptions and…”

I didn’t even have to look. I could see the whole thing in virtual reality: he had clearly pushed himself too hard in his burning enthusiasm for learning, then overslept.

I waved off Mungyeong, who was watching my expression.

“It’s fine. I just came out too. By the way, your luggage got a lot bigger overnight.”

“Oh, this?”

Mungyeong smiled brightly and patted his stuffed travel bag.

“They gave me copies of some precious medicinal prescriptions and plenty of medicinal herbs, and, and… Anyway, they gave me a lot!”

“Good. Congratulations.”

“Hehe.”

That kid was absolutely thrilled.

Then again, to a novice medical apprentice like Mungyeong, all of this was practically a fortuitous encounter.

The Sichuan Tang Clan wasn’t the kind of place that opened its doors just because someone knocked and readily handed over medicinal prescriptions.

It was a great Murim family as well as a renowned medical family, so everything Mungyeong had gained here would become a tremendous asset for his future.

“Good. You should be able to take something away from this, at least.”

“Huh?”

“It’s just something like that.”

“Did things not go well for you?”

“Yeah. There’s someone who absolutely has to be treated, but… circumstances are making it difficult.”

We were in the middle of talking when the middle-aged man we had met the day before approached with several subordinates.

“Everyone’s here. Follow me.”

We followed him. The atmosphere and behavior of the people we passed seemed even more tense than yesterday, but there were far fewer martial artists around.

*It’s begun.*

Large numbers of martial artists must have left to hunt down the culprit.

No, it had probably begun before we even arrived. Tang Sadok had lost his father. There was no way he would have remained dazed for several days.

After walking while lost in thought, we soon reached the iron gate.

As the gate slowly opened, the middle-aged man suddenly spoke.

“Uncle—no, the Family Head asked me to deliver a message.”

“What kind of message?”

“Once his revenge is over, our family will help you with all its strength.”

Mungyeong looked confused, but everyone else, myself included, clasped our hands in a martial salute.

“May you achieve what you seek.”

“And you as well.”

A faint smile crossed the middle-aged man’s cold face.

We hadn’t received any practical assistance, but this was a decent enough farewell.

Now it was time to say goodbye to one more person.

“It’s been fun.”

Mungyeong nodded as though he understood.

“You’re leaving again.”

“Yeah. We have a lot of places to stop by.”

“If I may ask, where are you going…?”

“Qingcheng. And then Emei.”

Mungyeong’s eyes went wide.

“Oh! Mount Qingcheng and Mount Emei, two of the most famous mountains in the world! You mean the places sacred to Daoism and Buddhism, where all kinds of exotic flowers and mystical herbs are said to be hidden?”

“……Uh, I think so.”

“This is unbelievable! You’re going to such wonderful places!”

What was this? Déjà vu?

I had been seeing scenes like this a lot lately. Just as a strange sense of foreboding sent a chill down my spine, Mungyeong let out a soft sigh.

“It’s unfortunate, but I can’t go with you this time. I have to return to my master.”

“Nice one, Master!”

“……?”

“I mean, that’s too bad.”

“Riiight.”

“I mean it, you punk.”

Mungyeong looked at me suspiciously before bowing deeply at the waist.

“Thank you for everything. Thanks to you Young Masters, I was able to survive and have many wonderful experiences.”

“There’s no need to thank me. Stay healthy, study hard, and focus on becoming a great physician.”

Mungyeong’s eyes sparkled.

“Like the Divine Physician?”

“Exactly. Like the Divine Physician.”

“Yes, Young Master! I’ll engrave your words on my heart and never forget them!”

A quiet laugh escaped me at Mungyeong’s spirited answer.

“Then take care.”

“Goodbye! We have to meet again someday!”

If our paths crossed, we would see each other somehow.

After waving to Mungyeong, I turned decisively toward the west.

“Come on. Let’s go to Qingcheng.”

I was just about to take my first determined step when—

“Young Hero Jin Taekyung?”

“Hm?”

I turned around and saw the Bermuda Triangle standing there blankly, along with two unfamiliar men.

They were the people the Sichuan Tang Clan had assigned to guide us.

“What is it?”

“Um. It’s just that…”

“……?”

“That’s not the right direction. The road is blocked if you go that way.”

“……!”

* * *

The guides Tang Sadok had assigned us were like a stroke of genius.

Unusually for members of the Tang Clan, they specialized in gathering and cultivating medicinal and poisonous herbs rather than martial arts. Perhaps because of that, they knew the land of Sichuan as well as the backs of their own hands.

“We go this way from here, right?”

“No. That way is faster.”

“But according to the map, this seems to be the right way.”

“What’s written on a map isn’t always the answer. That’s especially true of old maps.”

“The Sichuan Tang Clan gave me this one.”

“I made that map twenty years ago.”

“……”

“Let’s go.”

Well, if the mapmaker said it wasn’t the right way, then it wasn’t.

After that, I simply went wherever they told me to go and stopped wherever they told me to stop. Of course, I wasn’t just sitting around doing nothing.

“Wait. Can’t we just jump across here?”

“Huh? This is a cliff.”

“If I jump straight across to the cliff on the other side, we’ll get there quickly.”

“You’ll die quickly, too. The gap is nearly twenty zhang wide. How could you possibly—”

“Come on, let’s give it a try.”

*Boom! Whoooosh! Tat-tat!*

“See? It works.”

“……It actually works.”

“Come on, everyone. Cross one at a time!”

“……Are you talking to us?”

“Oh.”

“Could you jump back over and carry us across?”

“Possible. Totally possible.”

I was willing to do anything if it would save time.

With the Made-in-Sichuan navigation and my monstrous physical abilities, which far exceeded the limits of the human body, wherever I went became a road.

“My goodness… This is impossible. It took only half a day to get from Chengdu to Mount Qingcheng. That distance normally takes three days.”

“Impossible is nothing.”

I threw out a famous line I had picked up from television and entered Mount Qingcheng.

After revealing our identities to the disciples of the Qingcheng Sect, we were escorted to Shangqing Palace, where the sect made decisions on all matters great and small. There, we met another Supreme Peak master and the Sect Leader of the Qingcheng Sect, Cheongpung the Ancient Sword.

“I’m Jin Taekyung of the Jin Family of Taiyuan.”

“Wow, hello! I’m Cheongpung! It’s so nice to meet someone with a name so similar to mine!”

“Please shut up… And Cheongpung the Ancient Sword isn’t his name. It’s his alias.”

The Elders of the Qingcheng Sect looked at us as if wondering what kind of lunatics had just walked in, but their Sect Leader, Cheongpung the Ancient Sword, was even more straightforward than I had expected.

After reading the letter I handed him, he laughed heartily like an old man from the neighborhood and spoke.

“We should help one another. Great Hero Mae Jonghak specifically asked me to do this.”

That evening, the residents living at the foot of Mount Qingcheng were thrown into an uproar.

Daoists from the Qingcheng Sect, whom they rarely saw even a few times a year, came streaming down the mountain in a line.

There were hundreds of them. Among them were the Qingcheng Seventy-Two Swordsmen, all First Rate masters, as well as two Elders.

“Our Sect Leader Senior Brother has ordered us to do our utmost to help Young Hero Jin find the Divine Physician.”

“Junior Brother and I have been put out to pasture for years, but for something like this, we’ll gladly step forward. Ho ho.”

*Thank you. Overwhelming thanks…*

Honestly, I couldn’t help getting a little choked up.

No matter how we were all members of the orthodox faction, an entire sect had rolled up its sleeves to save Jeok Cheongang.

“I will repay the Qingcheng Sect for the help you’ve given us.”

“I’ll hear you say that again after we find the Divine Physician.”

“This isn’t all. We’ve also sent messenger pigeons to our lay disciples, so we should be receiving good news soon.”

Although the Qingcheng Sect did not possess the same standing as Huashan or Shaolin, it was still a massive, prestigious sect—large enough to be called one of the Nine Sects and One Gang.

The web of connections they had formed through their lay disciples would be an enormous help.

“Thank you. Truly, thank you.”

“A man’s back shouldn’t bend so easily. We’re merely doing what we ought to do, so don’t let it trouble you.”

“Yes. Excessive gratitude is unbecoming. Enough with the formalities. Tell us where we should begin looking.”

I rubbed my reddened eyes and answered.

“All of it.”

“Huh?”

“What?”

“All of Sichuan…”

“……!”

“……!”

After a brief silence, a quiet mutter slipped between the lips of the two old Daoists who looked like immortals.

“Goddamn it…”

“How are we supposed to find him…?”

I left the two Daoists behind as they began to grow jaded with the secular world less than fifteen minutes after descending the mountain, and set off toward our next destination.

“Benefactor! Are we going to Mount Emei now?”

“No. Gung and Mujin will handle the Emei Sect.”

We had two guides, and there were already plenty of people in our group. There was no need for everyone to move around in a huge crowd.

There was no telling where Cheongpung might run off to, so I would keep him with me. By now, Gung Gibang and Hyuk Mujin were probably running as hard as they could toward the Emei Sect.

Just then, one of the guides asked curiously,

“Then where are you going?”

“To the authorities.”

“The authorities? You mean you’re going to a government office?”

“Yes.”

“Young Hero Jin, I don’t know what ties you have to the authorities, but this isn’t something that can be handled by mobilizing a few constables.”

“Right.”

“Then why…?”

I spoke to the guide, who shook his head as though he could not understand me at all.

“But wouldn’t it be a different story with hundreds or thousands of people?”

“H-Hundreds or thousands? Are you perhaps acquainted with the Sichuan City Lord?”

“No.”

I grinned and continued.

“I’m friends with a king.”

“Pardon?”

Prince Shangshan, Zhu Bao.

He was the one and only younger brother of the emperor of the Great Nation that ruled the world, a noble imperial Prince—and a huge fan of mine.
## Chapter artifact 339

# Chapter 339

Early morning.

The City Lord of Sichuan Province, who had been nestled in his favorite concubine’s arms, asked in a sleep-heavy voice,

“Who is it? Who came to see me?”

The Captain of the Guards, suddenly confronted with his superior’s naked body first thing in the morning, hurriedly lowered his gaze and answered,

“Jin Taekyung of the Jin Family of Taiyuan, along with someone named Cheongpung of Huashan, requests an audience.”

“Huashan?”

It was a name he had heard often enough.

Born into a powerful aristocratic family and raised in a life with no connection to Murim, even the City Lord of Sichuan had heard of Huashan more than once.

“Huashan… Isn’t that one of those Ten Great Sects or whatever they’re called?”

“More precisely, it is called the Nine Sects and One Gang. Huashan is also a prestigious great sect with an extremely famous name in Murim.”

“They’re still nothing but ruffians. Calling men who swing swords in broad daylight without even carrying official identity plaques a prestigious great sect… Tsk, tsk.”

The Captain of the Guards had once roamed the martial world himself. He had plenty to say, but antagonizing the City Lord was not a wise choice.

As the City Lord clicked his tongue at the silent captain, he suddenly spoke.

“Wait. The name Jin Family of Taiyuan sounds rather familiar too.”

“It is an emerging sect that unified the Murim of Shanxi two years ago and has now made its name known throughout the Central Plains. Of course, if we are speaking only of the family’s history, it is old enough to rival the Nine Sects and One Gang…”

“No, that’s not what I mean. I’ve definitely heard it many times… Ah!”

After frowning in thought for a moment, the City Lord slapped his knee with a cry of realization.

“That’s right. The Jin Family Escort Bureau!”

“The Jin Family Escort Bureau…”

Only then did the Captain of the Guards recall the memory he had momentarily forgotten.

Come to think of it, it had not been all that long ago. Perhaps three or four months at most. The sight of wagons loaded with wealth rolling in one after another had brought a smile to the City Lord of Sichuan’s face.

“But weren’t they the Jin Family Trading Company?”

“The Jin Family Escort Bureau and the Jin Family Trading Company. Both belonged to the Jin Family of Taiyuan, if I remember correctly. I remember now.”

The Jin Family of Taiyuan had entered the world of commerce in earnest by opening new trade routes through the northern tribes. Before long, its name had begun spreading here and there throughout the Central Plains.

“So, what have they brought this time?”

At the City Lord of Sichuan’s expectant gaze, the Captain of the Guards hesitated before answering,

“Well, they appear to have come empty-handed.”

“What?”

“However, the young man named Jin Taekyung is a direct descendant of the Jin Family of Taiyuan and a young prodigy who has built an impressive reputation in Murim…”

“Stop with that martial-world nonsense.”

The City Lord’s face had already twisted into a scowl.

He had been born into an aristocratic family, and aristocratic pride was embedded in his bones.

If the Jin Family Trading Company had come bearing bribes, he would have welcomed them with open arms. But a young brat from a frontier martial family asking for a private audience early in the morning was another matter entirely.

*No need to hear him out. He’s obviously here to ask for some filthy favor. This is why you shouldn’t accept things from lowborn people too easily.*

Having already decided that they were unwelcome guests, the City Lord pulled the blanket up to his chin.

“Damn. I finally got a good night’s sleep, and now my mood is ruined.”

At that moment, his favorite concubine, who had just woken up, asked in a seductive voice,

“My lord, what has you so upset?”

“Some young brat showed up at the crack of dawn. You know, Aehyang? That Jin Family Trading Company that came by a few months ago.”

“Oh my. Yes, yes. Of course I remember.”

“He says he’s a direct descendant of the Jin Family of Taiyuan, a pack of martial-world ruffians from Shanxi.”

“And?”

“What do you mean, ‘and’? He obviously came to ask for some dirty favor, so I should throw him out immediately. How dare he…”

“My lord.”

“What is it?”

“Why don’t you meet him just once?”

“W-What?”

“He might have brought another nice gift. Like this pretty necklace I’m wearing right now.”

At the concubine’s coy smile, the City Lord’s heart softened and melted.

Just as she said, many of the items the Jin Family Trading Company had brought last time had been rare treasures.

The various pieces of jewelry and ornaments said to have been made by the northern tribes were mysterious yet exquisitely crafted. His concubine wore them constantly and never took them off.

“It’s my request. Won’t you grant it? Please?”

*Favorite concubine: launch three seconds of pleading gaze at target!*

*It was super effective!*

The City Lord of Sichuan frantically waved toward the Captain of the Guards.

“Bring them in. Quickly!”

“Yes. Shall I escort them to the reception room?”

“What reception room? I’ll only look at their faces for a moment. Bring them here.”

“……”

“What are you waiting for? Hurry up and bring those martial-world ruffians in.”

The Captain of the Guards bowed with a displeased expression and left the room. The City Lord of Sichuan thrust his protruding belly proudly forward and put on airs for his concubine.

“I’m only agreeing to meet them as a special favor because you asked.”

“Thank you, my lord. But I heard those martial-world ruffians are terribly rough… Aehyang is scared.”

“What? Scared?”

The City Lord of Sichuan burst into hearty laughter before shouting in a deliberately stern voice,

“Ho! I govern an entire city by the command of His Imperial Majesty himself. Are you saying you fear a few common street ruffians?”

“Oh, my. My lord, you’re so wonderful!”

The City Lord of Sichuan embraced his concubine as she nestled into his arms and smiled contentedly.

“Don’t worry about a thing. The moment those bastards enter, I’ll make them kneel and keep them from even looking at you.”

* * *

“W-What is that?”

Rat-a-tat-tat—thud!

The City Lord of Sichuan rushed from the bed in his naked body, threw himself flat on the floor, and cried out,

“I-I behold the token of His Highness Prince Shangshan!”

Good grief. Did he cook a locomotive smokestack rare and eat it?

His reaction was so violent that even I was momentarily taken aback.

All I had done was take *that* out and show it to him.

*Was it really that powerful?*

I looked down at the gold plaque in my hand.

It had been about a year ago, if I remembered correctly. I had even held a private autograph session for Prince Shangshan, Zhu Bao, and received this Item as a Quest completion Reward.



> **System**
> **Item Window**
>
> **Prince Shangshan’s Token**
>
> **Type:** Treasure  
> **Grade:** None  
> **Restriction:** Jin Taekyung  
> **Description:** A token imbued with the authority of Prince Shangshan, Zhu Bao, the emperor’s only younger brother and an imperial Prince. The clouds and dragon engraved into its surface symbolize the imperial family, and it is also of immense artistic value.  
> **Special Note:** Can be used only once.

I never expected to use something I had shoved into my Inventory and forgotten about like this.

I had known that the authority of the imperial family was powerful in this world, but the City Lord’s reaction exceeded even my expectations.

*It’s a shame I can only use it once.*

Still, I couldn’t complain.

I decided to provide Prince Shangshan with even more impressive fan service.

*Next time I see him, I’ll give him a rare collectible and even throw in a free hug.*

When I remained silent, the City Lord slowly raised his upper body.

At first, he had looked at Cheongpung and me as though we were street thugs. Now his eyes shook as if struck by an earthquake.

Wobble, wobble.

“……”

No matter how you looked at it, that part did not need to be shaking too.

At my disgusted glare, the City Lord of Sichuan hurriedly covered his lower body.

“T-There’s a reason for this…”

There probably was.

Spring flowers were blooming one by one outside, but in here the smell of chestnut blossoms was overpowering.

I picked up a blanket lying nearby and tossed it to him.

“T-Thank you.”

“Don’t mention it.”

I was the one who should be thanking him. Looking at a naked middle-aged man with a belly that made him look about thirty-five weeks pregnant was torture in itself.

Beside me, Cheongpung stared at the City Lord’s bulging belly with keen interest and whispered,

“Benefactor. Do you think it’s a boy or a girl?”

“Men can’t give birth.”

“Gasp!”

Still, he had come a long way. Just a year ago, he had firmly believed in the theory that cranes delivered babies through rocket express.

I addressed the City Lord, who was hiding his lower body beneath the blanket and watching me nervously.

“There’s nothing to gain from dragging this conversation out, so I’ll get straight to the point. We came to ask you for a favor.”

“T-The messenger of His Highness Prince Shangshan need only speak. I will help to the fullest extent of my power.”

“I’m looking for someone. First, how many people can you mobilize?”

The City Lord of Sichuan hesitated before answering in an uncertain voice,

“Well, I’m not sure. If we exclude the forces needed to defend against invasions by the border tribes, I suppose we could mobilize several thousand.”

Several thousand government troops alone. If we included the constables from the local offices, the number would be even higher. That was excellent news.

I smiled broadly, grabbed the City Lord by the shoulder, and pulled him to his feet.

“Then let’s search everywhere around Chengdu first. The first condition is that the person must be a physician.”

“A physician? The person you’re looking for is a physician?”

“Yes. People call him the Divine Physician.”

“Gasp! The Divine Physician? You mean that Divine Physician?”

“What’s the matter? Are you losing your nerve? If you do a good job, I can put in a good word for you with His Highness Prince Shangshan.”

After thinking for a moment, the City Lord of Sichuan cried out in a trembling voice,

“I shall complete this mission with all my heart and soul!”

Wobble, wobble.

“……”

No, everything else was fine, but he really needed to stop that from shaking too.

* * *

The reputation I had heard about the City Lord of Sichuan was the worst imaginable.

He was known as an incompetent official who had claimed his current position by riding on his family’s prestige. His hobby was gobbling up bribes wherever he could get them, and his specialty was wine, women, and gambling—or so everyone said.

*But he’s the City Lord.*

That was what mattered most. Just as I had borrowed Prince Shangshan, Zhu Bao’s authority, he possessed the authority and power of the highest-ranking official in Sichuan.

“The City Lord of Sichuan, Won Gyun,[^1] commands this! Let the officials of Sichuan carry out my orders without fail!”

Hearing his name had made me trust him considerably less, but a City Lord was still a City Lord.

[^1]: Won Gyun shares his name with a Korean admiral infamous for disastrous incompetence.

Courier horses carrying official documents raced to every corner of Sichuan, and notices seeking the Divine Physician were posted throughout the marketplaces. Naturally, a massive reward was offered to anyone who provided information.

“A thousand silver nyang! As expected of an acquaintance of His Highness Prince Shangshan, you are truly generous!”

Won Gyun’s admiring gaze did not last long.

“What are you talking about? You’re paying for all of it.”

“……What?”

“Do I look like someone who carries around a thousand silver nyang?”

“N-No, but even so, that’s an enormous amount.”

“Then put it on credit. I’ll mention it to His Highness Prince Shangshan later and ask him to pay you back.”

“No! I’ll pay it myself!”

“By squeezing the lifeblood out of the common people? Or by squeezing the fat out of your own belly?”

“Even if I have to spend my personal fortune, I will pay it myself!”

“Wow. Our City Lord is so cool!”

A massive reward capable of changing a person’s life several times over, along with a huge number of people mobilized for the search.

But even that was not enough.

*If the Divine Physician could be found with this much, the imperial court wouldn’t have given up.*

Who was the Divine Physician?

He was an unknown figure whom the imperial court had failed to find even after spreading a proclamation throughout the world in the emperor’s name.

People like that generally had a tendency to avoid being noticed.

“Let the government troops handle the marketplaces and busy districts. We’ll search every place with beautiful mountains and clear water.”

“I agree.”

“I should’ve just stayed at Qingcheng…”

The hundreds of Disciples who had descended the mountain alongside the two Elders of the Qingcheng Sect were exactly the right people for the task.

Three days after the government and Murim had joined hands and begun an unprecedented full-scale search, they finally arrived.

* * *

“Captain…”

The moment I saw Hyuk Mujin, whose exhaustion was plain to see, and Gung Gibang, who stood silently with a grim expression, I realized what had happened.

*Things had gone wrong.*

I could not rejoice even though the people I had been waiting for had finally arrived. They had not brought the news we had been waiting for.

I walked forward without a word. Passing Hyuk Mujin and Gung Gibang, I stopped in front of one person.

“I’m Jin Taekyung of the Jin Family of Taiyuan.”

She was a middle-aged nun. Her closely shaven head and pallid complexion immediately caught my eye.

The Emei Sect’s reinforcements consisted of her alone.

No, she looked more like a survivor of a routed army.

“I-I am a nun using the Dharma name Myoryeong… Cough.”

Drops of blood trickled down her chin.

An internal injury.

I caught her as she staggered. Looking into the eyes of Venerable Myoryeong, which seemed ready to fade away at any moment, I asked forcefully,

“What on earth… happened?”

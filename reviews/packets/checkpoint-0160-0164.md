# Checkpoint Review — 160–164

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

# Chapters 160–164

## Plot

Jin Taekyung recognizes that entering the Peak realm is only the beginning. Cheongpung ends their nearly ten-day training rather than continue their unfinished duel, allowing Taekyung to digest his breakthrough. Completing *Beyond the Wall* changes Taekyung’s class to Peak Master, raises him to Level 71, improves his cultivation and Qi Sense, unlocks trainable Sound Transmission, and awards him Unprocessed Ten-Thousand-Year Cold Iron. The resulting *Find the Master Artisan* Quest requires him to have the material forged into a weapon.

Meanwhile, Black Sand reveals that the five-hundred-member Heavenly Wind Band is subordinate to his one-hundred-member Black Sand Band. He forms an alliance with Temur and Chinggen to exploit the Mount Heng Sword Sect’s collapse: on New Year’s Day, their forces will attack the Jin Family through Hequ while Shanxi’s sect leaders gather in Taiyuan. The Human Butcher claims Wipeng as his target, but an apparently senile old man interrupts the gathering. The old man, secretly a Supreme Peak master, effortlessly defeats and kills the Human Butcher, then kills Black Sand after overhearing his attempt to exploit the old man’s declining mind. He forces the surviving chieftains and their followers to serve him while searching for a Peak master who uses sword and palm techniques, then leaves for Datong and promises to return in about a month.

Jin Wikyung and Hyuk Mujin celebrate Taekyung’s breakthrough. Taekyung asks Wikyung to investigate both the Master Artisan and the Fire King. The Jin Family has reportedly discovered a reclusive artisan nearby whose skill ranks among the world’s top ten. Taekyung also reveals that he obtained the Flame Divine Palm manual after the Eight Spring Gorge operation and had previously offered it to Mujin; he will decide whether to learn it only after confirming whether the Fire King is alive and consulting Wikyung.

## Continuity

- Taekyung is a Level 71 Peak Master with forty-five years of internal energy and seventy unassigned Stat Points.
- Cheongpung canceled *Sword Saint Training: A Secondhand Experience—2* without penalty; their full-strength duel remains unfinished.
- Taekyung possesses Unprocessed Ten-Thousand-Year Cold Iron and the *Find the Master Artisan* Quest, which requires commissioning a Master Artisan to forge it into a weapon.
- The Jin Family has heard of a nearby reclusive Master Artisan reputed to rank among the world’s top ten; Wikyung will verify the information and report back.
- The Human Butcher and Black Sand are dead. Temur and Chinggen survived, and the planned New Year’s Day attack on the Jin Family may have been disrupted but has not been explicitly resolved.
- An unnamed Supreme Peak master nearing one hundred years old is suffering increasingly prolonged periods of unconsciousness. He uses Samadhi True Fire and Scorching Yang Qi and is searching for an unidentified Peak master skilled mainly in sword and palm techniques.
- The old man left for Datong on the Shanxi–Gaoyuan border and said he would return to the Northern Gaoyuan in about a month.
- Taekyung has the Flame Divine Palm manual but has not decided whether to learn it. The Fire King’s survival and location remain unknown; Wikyung is to investigate.
- Hyuk Mujin knows Taekyung obtained the Flame Divine Palm manual after the Eight Spring Gorge battle and once refused it.

## Translation Decisions

- Render **초절정 고수** as “Supreme Peak master,” **삼매진화** as “Samadhi True Fire,” **정기신** as “essence, qi, and spirit,” **백염** as “white flames,” and **입신지경** as “a transcendent realm.”
- Render **명장** as “Master Artisan,” **장인을 찾아라** as “Find the Master Artisan,” and **가공되지 않은 만년한철** as “Unprocessed Ten-Thousand-Year Cold Iron.”
- Render **어르신** as “elder” and **형님** as “big brother,” preserving the old man’s abrasive rejection of both forms of address.
- Preserve established renderings including “Peak Master,” “Peak realm,” “Sound Transmission,” “Flame Divine Palm,” “Black Sand,” “Black Sand Band,” “Heavenly Wind Band,” and “Hequ.”

## Durable state

{
  "active_continuity": [
    "The unnamed old man is a Supreme Peak master nearing one hundred years old whose old age causes increasingly long periods of unconsciousness; he delayed its effects for roughly twenty years with two jiazi of internal energy.",
    "The old man can use Samadhi True Fire and possesses overwhelmingly potent Scorching Yang Qi, along with extraordinary physical strength.",
    "The old man is searching for an unidentified Peak master who mainly uses a sword and palm techniques; he carries a portrait and sought information from the Northern Gaoyuan's local powers.",
    "Black Sand attempted to manipulate the old man's senility through a plan to locate the sought-after master and obtain the old man's martial arts.",
    "The old man killed Black Sand with a single palm after overhearing the plan; Chinggen and Temur survived.",
    "The old man left the Northern Gaoyuan for Datong on the Shanxi–Gaoyuan border and said he would return in about a month.",
    "Jin Taekyung is now a Level 71 Peak Master with forty-five years of internal energy and seventy unassigned stat points.",
    "Taekyung received the Find the Master Artisan Quest to commission a Master Artisan to forge his Ten-Thousand-Year Cold Iron into a weapon.",
    "The Jin Family recently learned of a reclusive master artisan living nearby, whose skill is said to rank among the world's top ten; Jin Wikyung will verify the information and send word.",
    "Taekyung seeks information about the Fire King and will consult Jin Wikyung before deciding whether to learn the Flame Divine Palm.",
    "Hyuk Mujin knows that Taekyung obtained the Flame Divine Palm martial arts manual after the Eight Spring Gorge battle and once offered it to him."
  ],
  "continuity_sources": [
    164
  ],
  "open_questions": [
    "Who is the unnamed Supreme Peak master, and what is his relationship to the Peak master he seeks?",
    "Who is the unidentified Peak master being sought, and where is that person?",
    "Who is the reclusive Master Artisan capable of forging Ten-Thousand-Year Cold Iron?",
    "Is the Fire King alive or dead, and where can he be found?"
  ],
  "safe_through": 164,
  "temporary_decisions": [
    "Render 삼매진화 as “Samadhi True Fire.”",
    "Render 정기신 as “essence, qi, and spirit,” 백염 as “white flames,” and 입신지경 as “a transcendent realm.”",
    "Render 어르신 as “elder” and 형님 as “big brother” when Black Sand addresses the old man, preserving the old man's rejection of both forms.",
    "Render 명장 as “Master Artisan,” 장인을 찾아라 as “Find the Master Artisan,” and 가공되지 않은 만년한철 as “Unprocessed Ten-Thousand-Year Cold Iron.”"
  ],
  "version": 1
}

## Reading copies

## Chapter artifact 160

# Chapter 160

“Was Grandfather right?”

“No. Not at all.”

There was a simple reason I was flatly denying the words of Mae Jonghak, the great martial artist known as the Sword Saint.

*Look at the Sword Saint trying to fool me.*

*Nothing special, my ass.*

He had said that changing one’s position changed the view one could see. Behind the Peak wall I had barely crossed, a rugged mountain range was waiting.

*I still have a long way to go.*

They said learning had no end. Martial arts were no different.

I was nothing more than a beginner who had barely gained enlightenment from a casual remark tossed out by the max-level Sword Saint.

Still…

“Thank you.”

When I bowed with those heartfelt words, Cheongpung panicked.

“Benefactor, why are you suddenly doing this?”

“Because I’m grateful. That’s all.”

I knew there were countless martial artists, as numerous as grains of sand on a white-sand beach. I also knew that only a tiny fraction of them reached the Peak realm.

I also knew that even with advanced First Rate martial arts and internal energy, anyone without the enlightenment to match would spend their entire life stuck in place.

*If not for Cheongpung, I would have been lost for a long time.*

But I had been lucky. Cheongpung had devoted nearly ten days to helping me train, and he had even passed on the Sword Saint’s teachings.

That was far too generous a return for a few candied hawthorn skewers.[^1]

“Please don’t do this. I didn’t really do anything.”

“Didn’t do anything? I may be shameless, but I’m not an ungrateful bastard.”

“Huh? Really?”

“…”

How had this guy been looking at me all this time?

As my eyes narrowed, Cheongpung hurriedly waved his hands.

“No, that’s not what you’re thinking.”

“What am I thinking?”

“I mean, it’s just…”

Cheongpung looked around with lost eyes, then spotted Hyuk Mujin snoring in the corner of the training ground and shouted.

“Young Hero Hyuk! Wake up! This isn’t the time to be sleeping.”

“…”

This was genuinely pathetic.

Hyuk Mujin’s eyes suddenly flew open at Cheongpung’s shout. When he saw me, he spoke as though nothing had happened.

“As expected. I believed in you.”

“…”

This bastard was taking it even further.

“This Hyuk Mujin stood guard with the noble single-minded goal of protecting his Captain.”

“…”

“Enlightenment comes with difficulty and breaks easily. So I stood guard right here! With my eyes wide open! Making sure not a single rat could get inside!”

*I don’t know about the rat, but you sure seem like a fucking bastard…*

I stared at him, saliva stains covering the area around his mouth, and quietly spoke.

“Mujin.”

“Yes, sir!”

“I’ve become a Peak Master, you know?”

“Congratulations!”

“Yeah. And now my body is overflowing with strength. My fists are itching, too.”

“…”

“Guard duty? Rats? If your snoring had been even a little louder, I might have suffered qi deviation, you bastard.”

“…You heard me?”

“Did you think I wouldn’t?”

You had to wonder how loudly he had been snoring if even my mother in Ilsan could have heard him.

As he scratched the back of his head and grinned sheepishly, I spread my fingers wide.

“This is your last chance. I’m counting to ten, so disappear from in front of me. One, two, three…”

*Rat-a-tat-tat-tat!*

Cheongpung watched Hyuk Mujin flee at tremendous speed and exclaimed in admiration.

“Wow, training really does work! You’re incredibly fast!”

So that was how he interpreted it.

I said to Cheongpung, who was clapping like a seal and looking proud of himself.

“Then let’s start again.”

“Huh?”

“The duel. It isn’t over yet.”

“I’m fine with that, but… Aren’t you tired?”

“Not at all.”

It was a lie. My body, having entered a new realm, was overflowing with vitality, but my mind was exhausted beyond belief. It felt like the weakness that came after an all-out sprint.

But I wanted to continue sparring with Cheongpung even more.

*Because I want to test it.*

Gaining enlightenment was utterly different from raising my stats with points.

Right now, I felt as though I could unleash an entirely new martial art—not merely something faster or stronger.

“I’m perfectly fine.”

I said it again, but Cheongpung shook his head.

“My grandfather said that rest is also training.”

“Not even once?”

“No. Benefactor, you need to rest now. And…”

“And?”

Cheongpung giggled as he continued.

“I’m going to win anyway. So what’s the point?”

“…”

“You know that now too, don’t you?”

“That… is true.”

I didn’t want to admit it, but it was a fact.

People saw only as much as they knew. After reaching the Peak realm, I realized once again just how much of a monster Cheongpung was.

I also realized that, as I was now, I could never defeat Cheongpung if he fought at full strength.

*Unless he went easy on me.*

But that was not what I wanted. Winning a duel against an opponent who was not giving his all would only leave a bitter taste.

“Don’t be impatient. For the time being, you’ll be busy just digesting the enlightenment you gained today.”

“Then…”

“Let’s postpone our duel until next time. What a shame. I was having fun too.”

*Ding.*

> **System**
>
> - Quest *Sword Saint Training: A Secondhand Experience—2* has been canceled.
>
> - Since the Quest proposer made the decision themselves, you will not receive any penalty.

“Get plenty of rest today!”

I watched Cheongpung’s back recede for a long time before returning to the pavilion.

The System notifications reminded me of the things I had been putting off.

*Check messages.*

*Ding. Ding. Ding.*

Along with the endless System notifications, the messages I had not yet checked unfolded before my eyes.

I stared at the translucent System window with my mouth hanging open.

*How many of these are there?*

It looked like I would have to wait quite a while before I could rest.

* * *

The large wooden bathtub sloshed with hot water.

I had gone several days without washing properly and desperately needed a bath. As soon as I sank into the steaming tub, a moan escaped me.

“Ahhh. This feels great.”

Now I finally felt alive again. After closing my eyes and enjoying the sensation for a while, I opened the System window.

“Check messages.”

*Ding. Ding. Ding.*

System messages poured out like water bursting through a broken dam. I read them one by one.

> **System**
>
> - You have successfully completed Quest *Beyond the Wall*!
>
> - Your class has changed to **Peak Master**!
>
> - You have acquired a massive amount of EXP!
>
> - Level up!
>
> - Level up!
>
> - Level up!
>
> - Level up!
>
> - Level up!

*Oh. I went up five Levels at once?*

Someone might think that was stingy, but not me.

The Murim was another reality, but I was practically a game character here.

Back when I was a beginner, killing a single bandit could raise my Level. Things were different now. The amount of EXP required kept increasing, and my rate of leveling had been slowing down.

*This is more than enough.*

But the rewards did not end there.

> **System**
>
> - The realm of *Jin Family’s Cultivation Technique* has risen to the ninth stage.
>
> - You can now acquire more internal energy with greater stability.
>
> - The realm of *Qi Sense* has risen to the seventh stage.
>
> - You can detect targets at Level 90 or below within 70 meters.
>
> - You have acquired EXP due to the dramatic increase in your martial arts.
>
> - Level up!
>
> - Level up!

I was already satisfied that the realms of Jin Family’s Cultivation Technique and Qi Sense, which had stagnated for so long, had risen. Gaining two more Levels on top of that was an entirely separate stroke of luck.

Just from the messages I had seen so far, I had already leveled up seven times.

*Now that’s a proper reward.*

I smiled contentedly and continued reading the other messages.

> **System**
>
> - A Peak Master is a powerhouse capable of leading an entire school. You can create your own martial art and establish a new sect.
>
> - You have gained insight into the manipulation of internal energy that you had not known before. Through training, you can use the new Skill *Sound Transmission*.

Creating a sect and inventing martial arts.

The System was treating me like a Peak Master indeed. The treatment was worlds apart from what I had received as a First Rate martial artist.

*Well, I am a Peak Master now.*

Shanxi was crawling with thousands of martial artists. Even so, there were fewer than twenty Peak masters.

I didn’t know what things were like in the Central Plains, but at least in Shanxi Province, that was the kind of existence a Peak master was.

*But none of that is very useful to me.*

I didn’t know anything about inventing martial arts yet, and I had no intention of founding a new sect. Why would I leave the dependable Jin Family of Taiyuan?

More importantly…

*Sound Transmission is good. Very good.*

Sound Transmission. A technique for secretly transmitting sound by using internal energy.

The first two options were difficult to imagine using right away, but Sound Transmission had considerable practical value.

Training would be necessary, but that was manageable.

*Are there only three left now?*

All the countless message windows had disappeared. Exactly three remained.

With half relief and half regret, I checked the remaining messages.

*Ding.*

> **System**
>
> - *Ten-Thousand-Year Cold Iron* has been added to your Inventory.
>
> - A martial artist and their weapon are one body. Finding a weapon capable of drawing out all of one’s strength is also a martial artist’s duty.
>
> - Quest *Find the Craftsman* has been created.

“…Huh?”

* * *

Northern Gaoyuan.

The place where a great ruler had founded a powerful nomadic empire long ago had changed with the passage of time.

The vast pastures covered in green grass were gradually disappearing, and wooden buildings from the Central Plains were beginning to replace the gers, the nomads’ homes.[^2]

The customs of the nomads still remained, but the clothing and culture of the Central Plains were slowly infiltrating the plateau.

The man wearing a sheepskin cloak did not like it.

“Han Chinese bastards swarming the sacred grasslands.”

“Temur, bear with it. It’s not as if this started today or yesterday.”

“Chinggen. We are descendants of the khans. We must not forget that.”

“I haven’t forgotten. I’m simply telling you not to forget what kind of gathering this is.”

“Damn it. An inn instead of a perfectly good ger.”

Temur and Chinggen, two chieftains who each commanded a hundred tribespeople, entered the inn.

Built by Han Chinese who called themselves mounted bandits, it was the only establishment of its kind in Northern Gaoyuan—and it was enormous to match.

The moment the two men stepped inside, they saw mounted bandits packed all the way to the upper floor, along with two men seated at the center of the crowd.

“Ha-ha-ha! The chieftains of the Great Steppe have arrived! Sit here. I’ve warmed some mare’s-milk wine for you.”[^3]

Unlike the middle-aged man who welcomed them with both arms spread wide, the other man did not even dip his head. He merely gestured.

“Sit.”

“…”

“…”

The veins on Temur and Chinggen’s foreheads bulged.

Who were they? They were descendants of the Great Khan who had once crossed the steppe and ruled the Central Plains.

It had happened centuries ago, but their pride had never died.

“You Han Chinese bastard, lower than a dog!”

Temur had always been hot-tempered and reckless. Before Chinggen had time to stop him, his hand seized the curved saber at his waist.

“I’ll offer your head to the Tengger God—”[^4]

And that was when it happened.

“Sit down.”

The voice was cold, and the eyes were like an abyss. Even Temur, who led a tribe across the harsh steppe, found himself unable to draw his saber.

Taking advantage of the moment, Chinggen hurriedly grabbed Temur by the shoulder. He did not forget to whisper in a voice barely loud enough to hear.

“Temur, don’t act rashly. You know who he is, don’t you?”

Temur swallowed.

Four people had gathered here today. They had never met before, but each was a powerhouse who held up one of the major forces of Northern Gaoyuan.

But if there was a master capable of intimidating him this badly…

There was only one person.

*The Human Butcher.*

No one knew his surname. No one knew his name.

No one knew where he came from or what he had done.

He was Han Chinese, and he had ridden across the steppe with only fifty subordinates. He had earned the nickname Human Butcher because he killed people as though slaughtering livestock.

In other words, he was a butcher of human beings.

“You’re a slow one, friend.”

[^1]: Candied hawthorn skewers are fruit coated in hardened sugar.

[^2]: A *ger* is a traditional round felt dwelling used by nomadic peoples of the Central Asian steppe.

[^3]: Mare’s-milk wine is a traditional alcoholic drink made by fermenting mare’s milk.

[^4]: Tengger is a sky deity in traditional steppe belief.
## Chapter artifact 161

# Chapter 161

“You’re a slow one, friend.”

The Human Butcher’s words sent a chill through Temur. He could feel the killing intent lurking in the man’s calm voice like a dagger.

*They call him the Human Butcher, but what the hell kind of killing intent is that…?*

But he could not back down here.

The tribespeople he had brought for this gathering, along with the Han Chinese mounted bandits, were watching his every move.

*Damn it.*

The honor he carried as a chieftain clashed with the last shred of reason in his mind.

Should he draw his saber or not? As Temur wavered, a burst of laughter came to his rescue.

“Ha-ha-ha! As expected of the heroes of the world. A timid little man like me is too frightened to get involved.”

Temur looked toward the source of the laughter.

“Who are you?”

“Me?”

The middle-aged man, whose hair was half gray, smiled warmly.

If not for the eyepatch covering one eye, he would have looked as gentle as a kindhearted merchant.

“I have two names. I abandoned one when I left my homeland, while the other was given to me by friends I met on the steppe. Which one are you curious about?”

Temur did not need to answer. The Human Butcher revealed the man’s identity for him.

“Black Sand. Enough with the pointless drivel.”

“Oh, come on. What kind of person exposes someone like that? I was just getting to the fun part.”

“It wasn’t fun at all.”

“That’s why people call you the Butcher. Tsk, tsk.”

Temur and Chinggen realized who the middle-aged man was and opened their eyes wide.

“Black Sand? The Black Sand Band?”

“You’re that man?”

The eyepatched middle-aged man, Black Sand, nodded without hesitation.

“That’s right. I’m Black Sand.”

“…”

“…”

The Black Sand Band. Composed exclusively of Han Chinese, they were counted among the strongest powers on the harsh steppe.

There were only a hundred of them, but every single one was said to be a master of mounted combat and a martial artist of exceptional skill.

To think the leader of the Black Sand Band was such a frivolous man.

Chinggen was astounded.

*So that’s why that vicious Human Butcher didn’t react when he was called a butcher.*

It was only possible because the man was Black Sand. If anyone else had said it, the Human Butcher would have pulled out his tongue and cut off his head long ago.

But…

“Why are you here?”

Once his surprise had subsided, Temur also looked at Black Sand suspiciously.

“I’d like to ask you the same thing.”

Black Sand smiled faintly at their open wariness.

“Didn’t you receive a letter?”

Temur and Chinggen both flinched.

“A letter?”

“How did you know about that?”

“Because I’m the one who sent it.”

“That’s impossible. The letter clearly bore the seal of the Heavenly Wind Band Leader.”

Unlike Temur, who was bewildered, Chinggen seemed to have figured out the situation to some extent. He regarded Black Sand with a grave, thoughtful gaze.

“What is your relationship with the Heavenly Wind Band Leader? Where is he now?”

“So you’re Chinggen. I’ve heard you’re calm and sharp for a young chieftain.”

“That isn’t the answer I want.”

“You have a frightening look in your eyes. How am I supposed to say anything with you staring at me like that? Still, now that you’re here, there’s no secret worth hiding. I’ll tell you.”

After joking around, Black Sand continued.

“The Heavenly Wind Band Leader has been wandering around near Datong under my orders, drawing attention.”

*Under his orders.*

The meaning was obvious.

*We’ve been completely fooled all this time.*

The Heavenly Wind Band Leader was clearly Black Sand’s subordinate. That meant the Heavenly Wind Band, which numbered a full five hundred, was nothing more than a subsidiary organization of the Black Sand Band.

Temur and Chinggen exchanged silent glances.

*The Black Sand Band is already strong enough. And if you add the Heavenly Wind Band…?*

*It would be more than enough to change the balance of power on the steppe.*

A deep smile spread across Black Sand’s lips as he watched them.

“You seem to have a lot on your minds.”

“To be honest, this is rather bewildering.”

“What exactly are you scheming?”

“Scheming? I’m simply proposing a deal that benefits us all. You would know if you read the letter.”

Temur and Chinggen recalled the contents of the letter they had received fifteen days earlier.

The letter, tied to an arrow and shot to them, contained one short line.



*If you want to become a khan, come.*



A khan! The ruler of the steppe, a great king commanding countless warriors.

The very word made their blood boil. It was even more powerful to two young and strong chieftains who dreamed of restoring their clans to glory.

“The steppe is fractured into pieces these days. It’s hard to believe when you think of the glorious great empire founded by your ancestors.”

Black Sand swirled his mare’s-milk wine as he continued.

“If you help me, I’ll help you in return. Weapons, horses, wealth. If necessary, I’ll even send you some of my subordinates. Unite the fragmented steppe. Bring your enemies to their knees and force them to swear absolute obedience. I guarantee that you can become the khan of the Great Steppe within ten years.”

“Easy for you to say.”

Unlike the sarcastic Temur, Chinggen remained calm.

“Why us?”

“Because you’re young, capable, and ambitious. Your legitimacy as descendants of the khans also helps. In any case, my proposal is simple.”

Black Sand pushed a hard, dried lump of horse dung into the fire, which was gradually dying down. The flames suddenly leaped up and flickered in his eyes.

“Would you care to seize a city with me?”



* * *

“A stronghold? You mean Shanxi?”

“Where else would I mean?”

Only then did the two chieftains roughly grasp his intentions. He intended to force his way into the power vacuum left by the collapse of the Mount Heng Sword Sect.

The problem was that, for all his grand talk of khans and support, his proposal offered them little that was actually attractive.

“None of you look very pleased.”

Chinggen answered with an unconvinced expression.

“If you’re thinking of raiding the north now that it’s become ownerless, wouldn’t that be difficult?”

“Why?”

“Because the Jin Family of Taiyuan is moving quickly. I’ve heard they’re establishing branches throughout the north, while the government is also getting involved.”

Even they had a line they could not cross.

Attacking a merchant caravan made them mounted bandits, but invading a city and plundering civilians would make them rebels.

If an army of tens of thousands were dispatched to suppress the rebellion, they would have no way to oppose it.

“I don’t want to be driven out of my homeland, either. And I have no desire to die a dog’s death like Pung Yang.”

Temur nodded at Chinggen’s words. He was hot-tempered, but he had to acknowledge reality.

“That bastard Pung Yang didn’t even touch the government. He was killed by the young brats from the Jin Family of Taiyuan.”

“Pung Yang had nearly four hundred subordinates. Less than one in ten of them made it back alive.”

The Human Butcher, who had been listening silently, suddenly spoke.

“Pung Yang was a man who fled from the steppe. The people under him were nothing more than a bunch of ragtag strays he hastily gathered.”

“You’ve met Pung Yang?”

“Once or twice. He was nothing special. I can say this with certainty: no one here is weaker than him. Ah, that includes that idiot, of course.”

“You bastard!”

“Lower your voice before I cut out your Adam’s apple.”

“The Han Chinese bastard has a big mouth. You think you can do it?”

“Of course. Right now, if you want.”

*Schriing.*

Just as the blades at both men’s waists slid from their sheaths—

“Honestly. Keep it under control.”

There was no one here who could disregard Black Sand, whether because of his age or his power.

After the two men exchanged a tense battle of wills and sheathed their weapons at the same time, Black Sand laughed as though he found it amusing and spoke to Chinggen.

“You don’t need to worry about the government. This will end as a matter between the Jin Family of Taiyuan and us.”

“What do you mean?”

“If we finish the job like a bolt of lightning before anyone can react, what could they do?”

“Do you think that’s possible? Shanxi Province is practically already in the hands of the Jin Family of Taiyuan. Even if we break through Datong, the family’s main force and countless small and medium-sized sects will be waiting by then.”

“What if we strike before they gather? And target only their heads?”

“…”

“What?”

“In three days, on the coming New Year’s Day, the heads of every sect in Shanxi Province will gather at the Jin Family of Taiyuan. We’ll enter through Hequ instead of Datong, then charge straight toward Taiyuan.”

“…”

“If we keep our weapons to a minimum and secure hardy steppe horses with excellent endurance, we can easily cover five hundred li in a day.[^1] We can strike the enemy in as little as two days, or three at the most.”

Crossing half of Shanxi Province to strike directly at the enemy’s head.

It was such a bold and reckless plan that Chinggen’s voice trembled.

“W-Wait. What if they realize what we’re doing in advance and prepare?”

“Prepare? What exactly do you mean?”

“As I said, branches of the Jin Family of Taiyuan are being established throughout the north. If we advance while fighting our way through each one, we’ll lose our mobility. If we ignore them and pass by, they’ll hear about us before we even arrive.”

“Don’t worry about that. We only need to smash the Hequ branch.”

“Then what about the other branches?”

“By then, they’ll be fighting for their lives in Datong.”

“Datong… Ah. Could it be?”

“The Heavenly Wind Band Leader will do his part. I told him to run wild without restraint on that day.”

The Heavenly Wind Band was a northern plateau power everyone knew.

Their numbers and the individual skill of their members were at least equal to those of the Red Wind Band, if not greater.

“In half a day, the Jin Family of Taiyuan’s branches throughout the north will be empty. With a fire burning in front of them, do you think they’ll have time to look behind them?”

Black Sand’s words were exactly right. The branches would scrape together every martial artist they had and send them to Datong to stop the Heavenly Wind Band. Taking advantage of that opening, the real main force would cross Hequ and advance south.

Trampling everything in their way beneath their horses’ hooves…

“Also, the Jin Family of Taiyuan is currently devoting all its strength to stabilizing the north. From what I’ve learned, there might not even be a hundred martial artists in the main family.”

Black Sand’s voice continued.

“This is a gathering attended by every sect in Shanxi Province. No matter how large the Jin Family of Taiyuan is, it can’t feed and house all of them. Even if you add every martial artist remaining at the main family, there may be only two hundred.”

Chinggen’s throat went dry. The forces under the people gathered here alone totaled three hundred without difficulty.

No, if they scraped together every last person, they could double that number.

*We won’t be outmatched even in a battle between masters.*

Black Sand. The Human Butcher. Temur and Chinggen.

All four of the people gathered here were exceptional Peak masters.

According to the Human Butcher, who had personally met the dead Pung Yang, no one here had inferior martial arts to him.

*But the Heaven Shaking Sword and the Sleeping Dragon of Shanxi from the Jin Family of Taiyuan only barely defeated Pung Yang after joining forces.*

That had already been confirmed as fact.

Pung Yang had even defeated the Tiger of Mount Heng, a veteran of the martial world. As a result, rumors had spread that the mounted bandits of the northern plateau were stronger than most First Rate martial artists.

*Could this actually be…?*

Black Sand watched Chinggen, who had fallen silent in thought, with amusement in his eyes.

“What do you think?”

Temur, who had been listening while repeatedly swallowing, shouted.

“Damn it! How can you tell me about such a fantastic plan and then ask what I think? I’m in, no matter what!”

“I’ll accept as well.”

Chinggen finally finished thinking and agreed. The Human Butcher cut in with a vicious smile.

“I don’t need anything else. Just leave Ghost Sword Wipeng to me.”

“Of course. You have my word.”

Black Sand, his face filled with a broad smile, looked around at the three men.

Now that they had accepted his proposal, he was effectively their presiding leader.

“Everything we gain from this will be divided into four equal shares. If anyone breaks that agreement, I’ll chase them to the ends of the world and cut off their head. Any objections?”

“None.”

“Me neither.”

“Keep the promise written in the letter.”

“Of course.”

Black Sand answered readily and filled an empty bowl with mare’s-milk wine before passing it around.

“Now that we’ve sealed our resolve, let’s get thoroughly drunk today!”

“Waaaaah!”

“Let’s drink! Bring more alcohol!”

Cheerful shouts erupted from every corner of the inn.

And just as they were raising their bowls in an atmosphere as heated as the mare’s-milk wine itself—

*Creeeeak.*

Amid the uproar, the inn’s door opened, and someone stepped inside.

[^1]: A *li* is a traditional Chinese unit of distance.
## Chapter artifact 162

# Chapter 162

There are moments when the boisterous, perfectly interlocking din of a place suddenly disappears.

This was one of them.

*Creeeeak.*

The inn fell silent at the sound of its old door opening.

The gazes of the four leaders and more than two hundred mounted bandits and nomads, who had been raising their cups in celebration of their plan to turn Shanxi Province upside down, all converged on the entrance.

*Step. Step. Step.*

*What the…?*

Black Sand’s eyes narrowed as he identified the uninvited guest slowly walking toward them.

*What’s with this old man?*

The uninvited guest was an old man. Literally an old man.

But Black Sand had never seen anyone older than the man approaching them now.

*He’s practically a corpse.*

His unsteady gait made him look as though he could collapse at any moment. His wrinkled skin was ice-cold, and the breath escaping his lips was thin and faint.

Temur, Chinggen, and the Human Butcher watched the old man in silence for a while before exchanging a few words.

“That’s the oldest person I’ve ever seen. He’s older than our tribe’s shaman.”

“But what’s an old man doing here? And why is he dressed like that?”

“He must have run into some mounted bandits.”

As they said, the old man’s appearance was utterly miserable. His clothes were tattered, as though he had suffered some misfortune somewhere, and his body was so emaciated that only skin seemed to remain.

“What an unlucky old man. After barely surviving, he ends up here in a mounted-bandit den.”

The Human Butcher clicked his tongue.

“I don’t even feel like killing someone that old. Get rid of him.”

“Yes, sir.”

His subordinate was about to step forward when—

“Wait.”

The one who stopped him with an upraised hand was Black Sand. His brow furrowed as he stared at the old man.

*Something’s strange.*

The inn where they were staying had been built by mounted bandits. Its owner, cook, and servers were all either mounted bandits or former mounted bandits.

It was the only neutral ground in the Northern Gaoyuan, which was why it sometimes served as a place for gatherings and reconciliations like today’s.

*But he came crawling here on his own? And he’s that old?*

Anyone who set foot in the Northern Gaoyuan naturally knew the inn existed.

They also knew that an ordinary commoner who entered it would be as good as dead.

“What is it?”

“Shh. Wait a moment. Something about this doesn’t feel right.”

Black Sand’s reaction caused the others to sense the oddity as well.

“Come to think of it, how did he get here?”

“He looks like an outsider…”

“He’s not an outsider. There’s no way an old man like that could have reached this place with his body intact.”

Hundreds of mounted-bandit groups and nomadic tribes were scattered throughout the Northern Gaoyuan. Unless someone was exceptionally daring, they would never even consider crossing the plateau alone.

The four men, including Black Sand, fell into thought.

*Could he be…?*

*If he’s a martial artist, it’s possible.*

*A martial artist? That old man?*

*He’s bothering me. We should kill him.*

To the Human Butcher in particular, murder was no different from breathing. As he fearlessly reached for his sword sheath, Black Sand glared at him.

Then Sound Transmission slipped into the Human Butcher’s ear.

— I told you to wait. It won’t be too late to act after we observe him a little longer. Haven’t you ever heard that, in the Murim, you should be wary of women, children, and old men?

— You’re worrying over nothing. That sickly old man?

— Don’t act rashly. You never know what might happen in the Murim.

The old man looked as though he would die if someone merely poked him.

But the Human Butcher could not simply ignore Black Sand’s warning.

With an irritated sigh, he took his hand off his sword sheath.

— Good choice.

By then, the mysterious old man had reached the four men with trembling steps.

A strange tension hung in the air. The old man looked around with hazy eyes, then opened his mouth.

“W-Water…”

His voice was dry and parched as he searched for water. The people around him shook their heads with expressions that seemed to say, *Of course.*

But Black Sand was different. Careful and calculating by nature, he did not lower his guard until the very end.

“The elder seems thirsty. Bring him some cool water.”

“Yes, sir.”

After a mounted bandit handed him a cup, the old man gulped down the water as though his life depended on it. He drank so desperately that it seemed he might collapse.

Only after downing five or six cups in succession did the old man raise his head.

“Whew.”

“Feeling better now?”

A broad smile spread across the old man’s wrinkled face.

“Yes!”

“…”

“Thank you, mister!”

*Mister?*

Startled, Black Sand shot to his feet and grabbed the old man’s wrist.

There was no resistance. No strength at all. The thin bones looked as though they would snap if he applied even a little force.

“Elder?”

“Yes? Why?”

The old man’s smile and tone were like those of a child. Black Sand stared at him blankly, then his face twisted.

“Damn it. He’s senile.”

The tension drained out of him. He had definitely sensed something strange, but it seemed it had all been in his head.

With an important undertaking ahead of them, perhaps his nerves had simply been on edge.

Black Sand shook his head from side to side, and the Human Butcher laughed at him.

“They say you never know what will happen in the Murim. I suppose they were right. An old man suffering from age-related infirmities? Ha-ha-ha!”

“Shut your mouth.”

Black Sand answered curtly and began to release the old man’s wrist.

That was when—

“Where the hell is this?”

The voice was sharp and clear, completely different from before. The old man’s eyes had become focused as he looked around, then he let out a deep sigh.

“Damn it. You should die once you get old.”

It seemed he had finally returned to his senses. Laughter leaked out from various corners of the inn at his grumbling.

Black Sand had completely relaxed as well. He gave a quiet laugh and asked,

“Elder, are you feeling better now?”

The old man answered.

“Who told a little bastard like you that he could use *hao*-style speech with me? Are you from the Lower District Sect or something?”[^1]

[^1]: *Hao*-style speech is a semi-formal Korean speech level; its name sets up the pun on the Lower District Sect’s Korean name, *Haomun*.

“…”

“What are you holding my wrist for? You trying to get fresh with me?”

“W-Wait a moment.”

“Are you letting go or not? I’ll count to three. One, two, three.”

*Whoosh.*

Black Sand let go of the old man’s wrist before he even realized what he was doing. His mind was completely scrambled by the sudden turn of events.

*What the hell is this old man?*

The thick curses and rapid-fire words had made his body move on its own.

The old man was clearly nothing more than a deranged elderly man who did not know a single martial art, yet Black Sand felt as though he had been bewitched.

“Ha-ha-ha-ha! You got played beautifully!”

The Human Butcher burst into raucous laughter. He had already disliked Black Sand acting as leader when Black Sand was clearly a step below him in martial arts.

Seeing Black Sand humiliated by a senile old man made him feel thoroughly refreshed.

“That old man has quite a mouth on him. He made me laugh, so I suppose I’ll let him live.”

But the satisfied smile at the corner of the Human Butcher’s mouth did not last long.

A single sentence from the old man made it disappear.

“You worthless bastard… Don’t you have a mother and father?”

“…”

The inn fell into icy silence.

Who were Black Sand and the Human Butcher?

They were major figures who dominated the Northern Gaoyuan. Their forces were formidable, but each of them was also a Peak master capable of crushing an average mounted-bandit group with ease.

Yet the old man had carved the two men apart with only a few words.

“One’s a sodomite from the Lower District Sect, one grew up without parents and has only half a tongue, and the other two…”

The old man glanced at Temur and Chinggen, who wore their hair in queues, then sighed.

“Young men, and your foreheads are already completely bare. What a pity.”

No one had the energy to be surprised anymore. In the midst of the atmosphere thick with shock and horror, the old man clicked his tongue and noticed the food laid out in front of the four men.

“Well, damn, you’ve laid out one hell of a feast. I was hungry, too. What a stroke of luck.”

No one had time to stop him.

The old man grabbed a well-roasted duck by one leg and ripped into it.

“Wow, look how tender this meat is. It just melts on the tongue.”

*Crunch, crunch.*

After devouring both legs in the blink of an eye, the old man thrust a piece of meat toward the Human Butcher, who was trembling with rage and shock.

“You’re still young, so why are you trembling so much? Don’t waste away from weakness. Eat this. I hate dry breast meat—no, I can’t eat it. My teeth aren’t very good.”

*Crack.*

Everyone in the inn heard the same sound.

It was the sound of the last thread of the Human Butcher’s reason snapping—and the death knell of a man.

“You goddamn old bastard!”

The next moment, the Human Butcher, beside himself with rage, shot upward like lightning. At the same time, crimson Sword Energy poured from the horse-chopping sword in his hand and swept across everything in front of him.

“What the hell!”

“Get out of the way!”

*Kaboom!*

Temur and Chinggen had barely thrown themselves aside when a thunderous explosion rang out.

Hundreds, even thousands, of wooden fragments flew in every direction as a cloud of dust billowed through the air.

“Die! Die! Die!”

The people watching the scene felt the hair rise on the backs of their necks. Judging by the madness radiating from the Human Butcher, there was no doubt the old man had died without leaving behind even a single scrap of flesh.

“How dare a senile old man—! Aaaaargh!”

*Boom! Boom! Boom!*

A relentless storm of Sword Energy continued to pour forth. The Human Butcher finally withdrew his horse-chopping sword after roughly a quarter of an hour.

“Huff… huff…”

Breathing heavily, he swung his sword through the air. The resulting sword pressure scattered the dust cloud, revealing a half-pulverized ruin.

As everyone had expected, the old man was nowhere to be seen.

“He was the bravest person I’ve ever seen.”

“Farewell, elder.”

“Why did he have to provoke the Human Butcher…?”

“As expected of those Han Chinese. They’re unbelievably savage.”

The more than two hundred mounted bandits and nomads were whispering among themselves when—

*Crunch, crunch. Gulp. Guh-hup!*

“…”

“…”

“…”

At first, they were simply dumbfounded.

In an atmosphere like this, what kind of clueless idiot was eating food and drinking liquor?

But it took no more than an instant for their confusion to become astonishment, and their astonishment to become horror.

“T-The old man! The old man is alive!”

“What? Where?”

“Behind us! I heard him behind us!”

Someone shouted.

Then a sharp, clear voice followed, making everyone doubt their own ears.

“Young people these days are a real problem. So rude. Is my name *old man*? Am I your friend?”

“W-Whoa!”

“That does it. I’ll teach you lot some manners today.”

*Thud-thud-thud! Whoosh!*

The mounted bandits and nomads filling the inn went flying through the air one after another.

Their limbs were mangled and their faces smashed as they were flung away. The sight made the leaders break into cold sweats.

*W-What is this?*

*How is he over there?*

*I didn’t even see him move.*

A master.

A master capable of deceiving the eyes of even Peak masters like themselves.

Black Sand, Temur, and Chinggen had gone rigid when, as the only exception, one man charged straight toward the old man.

“You goddamn old bastard!”

The Human Butcher was already beyond reason and had no reservations left.

The old man saw him rushing forward and frowned.

“You…”

“That’s right, it’s me! This time, I’ll definitely kill you!”

“So you’re the one without parents.”

“Graaaargh!”

*Whoooosh!*

*Mount Tai Presses Down on the Crown.*

At that moment, the horse-chopping blade, its crimson Sword Energy blazing, was about to split the crown of the old man’s head.

The old man swung something.

*Slice! Thud!*

It felt as though time had stopped.

In the silence, not even a breath could be heard. Everyone doubted their own eyes.

The horse-chopping sword had been cut in half.

And in the old man’s hand was a tiny object.

“T-That’s…”

For the first time, the Human Butcher’s eyes regained their composure. He stared at the old man in fear and astonishment.

“…A chicken bone?”

“There’s no part of a chicken that goes to waste. The meat is delicious, the bones make a fine broth when simmered down, and sometimes they’re even good for wielding Sword Energy.”

He had used a chicken bone to wield Sword Energy.

The Human Butcher had never seen or heard of anything so bizarre.

He understood instinctively.

*A master. A Supreme Peak master. Someone I could never oppose.*

The old man looked at the Human Butcher, who had fallen into shock, and muttered,

“Come to think of it… You’re a vicious one. The smell of blood is coming off your entire body.”

Every word sent a chill through him. He had lived his entire life as a predator, yet now he was no more than a rat before a tiger.

“You can’t just leave someone like this alive…”

The Human Butcher suddenly felt a chill. The deadly aura flowing from the old man’s entire body made his teeth chatter.

“P-Please.”

“Hm?”

“Please spare me. Please…”

Tears ran down his cheeks. His trousers grew damp, and the horse-chopping sword slipped from his limp hand.

The plea of a butcher who had spent his entire life taking other people’s lives was an unbelievable sight.

The old man looked at him for a moment before speaking.

“Don’t be afraid.”

*I’m safe. I’m alive! I escaped death!*

The Human Butcher let out a relieved sigh without realizing it.

That was when—

*Thump.*

A hand with protruding knuckles pressed against his chest. The old man’s hand was rough and wrinkled.

And that was the end.

“…Huh?”

The world turned upside down along with his faint question. Blood poured from the seven orifices of his fallen body and soaked the floor.

*He said he would spare me. Why?*

Beyond his fading vision and the sounds receding into the distance, he heard the old man’s voice.

“Don’t be afraid. I’ll send you off without pain.”

The old man was telling the truth.

There was no pain.

* * *

The Human Butcher.

A Peak master whose evil reputation had spread all the way to the Central Plains had died from a single move.

“Well, then…”

The old man addressed the people who had frozen in place.

“Where is this place?”
## Chapter artifact 163

# Chapter 163

“What? The Northern Gaoyuan? There are only three days left until New Year’s Day?”

“Yes.”

“Well, now.”

The old man fell silent. In front of him, the three leaders and more than two hundred underlings knelt respectfully, watching his lips.

“Is that really true?”

“W-We’re certain.”

“How could we possibly dare lie in your presence?”

“…I see.”

The old man’s expression darkened at their desperate excuses.

He knew what they were saying was true. He had only wanted to deny it, if only a little—the fact that he was growing old.

*So I was out of it for seven days and nights. Seven days and nights… It’s getting longer.*

It was because of his old age.

He had first sensed something strange more than twenty years ago. During cultivation, he had realized that his essence, qi, and spirit were falling out of alignment. That was when he knew the years had finally caught up with him.

He was already nearing a hundred. He was not afraid of death, but he did not want to be remembered as a senile old man.

*Even after all that effort…*

He had reached his limit. The curse of time could not be held back even by his two jiazi of internal energy, or by the manifested qi of a Supreme Peak master.

He had managed to delay the effects of old age for no less than twenty years. That alone should be enough to satisfy him. The old man forcibly shook off his bitterness.

“Pour me a drink.”

“Um, the wine has gone cold, so we’re preparing a fresh batch.”

At Black Sand’s cautious reply, the old man clicked his tongue.

“When will that be? Never mind. Bring me the cold wine.”

“Yes.”

Who would dare object to an order from him? At Black Sand’s gesture, two mounted bandits who looked strong enough hauled over a wine jar, groaning with effort.

The enormous jar, tall enough to reach a person’s chest, sloshed with half-cooled mare’s-milk wine.

“Tsk, tsk. Young men these days are so weak. Don’t you feed the people under you?”

“H-How could we not?”

“Then why can’t you even lift this properly? Good grief. Watching you is making me frustrated.”

The old man shot to his feet and snatched the jar away. The jar, which weighed at least several hundred catties, rose effortlessly in one hand.

It was almost impossible to understand how such strength could come from a body that had been reduced to little more than bones. Black Sand wanted to gouge out his own eyes.

*I must be crazy. I thought a monster like that was nothing more than a senile old man.*

At least he had been careful with his words. Hadn’t the Human Butcher died horribly after waving his sword around and calling the man an old geezer?

Black Sand had no desire to die with blood pouring from his seven orifices.

“Elder! I’ll do it!”

“Don’t call me elder. Sit down and stop talking nonsense.”

“No, no. Mare’s-milk wine is best when it’s piping hot. I’ll heat it myself…”

“Piping hot, what?”

Black Sand was at a loss for words.

The next moment, tremendous heat burst from the wine jar.

The source of that heat was the old man’s hand gripping the jar.

White flames, enough to make the mere sight of them suffocating and raise goose bumps, instantly heated the wine jar and warmed the mare’s-milk wine.

“T-That’s…”

“S-Samadhi True Fire?”

Temur, Chinggen, and the more than two hundred underlings were stunned by the sight before them.

The shock suffered by the leaders was especially immense.

*What the hell?*

*He’s using Samadhi True Fire on a wine jar that size?*

*That’s an unbelievable amount of internal energy. Who is this old man?*

Samadhi True Fire was a flame created by burning internal energy. A Peak master with deep internal energy could use it without much difficulty.

However, its firepower was pitiful compared to the enormous amount of internal energy it consumed, making it hopelessly inefficient in actual combat.

“Bring me a bowl. A big one.”

But what about this old man?

The heat they had felt, though momentary, had been tremendous. If he wished, he seemed capable not only of harming people but of melting steel.

*His martial arts and internal energy have already reached a transcendent realm.*

*It’s not only the Samadhi True Fire. His internal energy itself is overwhelmingly Scorching Yang Qi.*

*Don’t say anything. If I put one foot wrong, he’ll kill me.*

The three men swallowed dryly and moved as quickly as waiters receiving an honored guest.

“I’ll pour you a drink, sir.”

“Bring meat! Meat!”

“Just bring the legs!”

Black Sand, the Squad Leader of the Black Sand Band—known across the steppe as a harbinger of death—poured the mare’s-milk wine. The two tribal chieftains, descendants of the Great Khan and commanders of hundreds of mounted warriors, circled the table, tearing off only the tender leg meat and presenting it to the old man.

It was a sight difficult to witness even if one paid for it.

“Mm. This is why rude bastards need to be beaten. They only learn manners after someone teaches them a lesson.”

“You’re absolutely right, elder.”

The old man, who had been eating carefully stripped meat with his mare’s-milk wine, paused.

“Elder?”

“Y-Yes. Did I make some kind of mistake?”

“You’re making me sound old. Like some old man who’s about to die any moment.”

*Yes. You really do look like you’re about to drop dead.*

Black Sand barely managed to swallow the words that nearly escaped him. His opponent was a peerless master whose realm was impossible to gauge. He had to placate the old man somehow.

“Then, big brother…”

“Do I look like a pushover?”

“I-I’m sorry!”

*Bam!*

Black Sand slammed his forehead into the floor without a word. He felt like he was dying. The old man hated being called an elder because it made him sound old, but calling him big brother apparently made him look easy to deal with. What was Black Sand supposed to do?

The old man lightly kicked Black Sand while he was still prostrated.

“Get up.”

“Yes, sir!”

“And you two with the scraped foreheads.”

*Whoosh!*

Temur and Chinggen, who had been diligently stripping meat from the bones, rushed over at the speed of light and knelt.

Only after draining a long gulp of mare’s-milk wine did the old man finally speak.

“So, what kind of people are you?”

Mounted bandits. And nomads who were no different from mounted bandits.

They had no idea what would happen if they told the truth to an old man who clearly looked like a senior of the orthodox faction.

Just as the three men were desperately exchanging glances—

*Smack! Smack! Smack!*

“Ghk!”

“Gasp!”

“Argh!”

The old man struck each of them on the head with a knuckle at a speed too fast to see, then glared.

“You goddamn bastards. An adult asks you a question, and all you do is roll your eyes at each other?”

“I-I’m sorry, elder.”

“I told you not to call me elder. Are you holding some kind of ritual to pray for my death? Huh?”

*Smack!*

Black Sand answered and got hit again for his trouble. He felt tears welling up. He was over fifty, and all his subordinates were watching him…

“Let the oldest one answer first.”

Black Sand opened his mouth while gazing at the old man with moist eyes.

“I, that is, I roam the steppe with my close brothers and horses for company…”

“You’re a worthless mounted bandit. You spend every chance you get looting, murdering, and setting fires.”

“…”

The old man stared at Black Sand with utter contempt before turning away. Temur and Chinggen flinched and lowered their heads.

“You two call yourselves nomads, but you’re no different. Am I wrong?”

“N-No, sir.”

“You speak the absolute truth.”

“The one way you’re better than mounted bandits is that, even though you loot and kill, you aren’t arsonists who set fire to everything in sight. People who burn down other people’s homes deserve to be beaten to death!”

“…”

“…”

“…”

Wasn’t murder normally considered the gravest crime?

The three men tilted their heads at the strange feeling, only to be struck by another storm of blows.

*Smack, smack, smack!*

“Anyway, I have a general idea what sort of places you crawled out of. What I want to know is how much influence you have around here.”

“Ow… What do you mean by influence?”

“Exactly what I said. Do you have any clout?”

The three men rubbed their crowns and answered carefully.

“If we join forces, there aren’t many who could stand against us.”

“Most of us are divided into branch clans, so we are scattered rather widely. But if all our relatives gathered, we could easily fill dozens of tribes and still have people left over.”

“We exchange all the news that occurs throughout the steppe without missing anything.”

The old man’s eyes flashed at Chinggen’s final answer.

“Oh? That’s useful.”

Quick to read the situation, Chinggen realized the old man wanted information and immediately answered.

“If you need information, we’ll tell you anything you wish to know.”

“I’m looking for someone. I don’t know exactly where he is, but… he probably isn’t too far away. Can you do it?”

“Yes. If you could tell us his appearance or any distinguishing features, it would be even easier.”

“Wait here.”

The old man pulled a crumpled sheet of xuan paper from his robes. A skilled artist seemed to have drawn it; the face of the person being sought was clearly depicted.

“Will this do?”

Chinggen nodded without hesitation.

“Of course. With a portrait sketch as well, we should be able to start asking around immediately.”

If they sent messengers in all directions and dispatched messenger eagles, they could learn the answer within fifteen days at the longest.

The steppe was vast, but no one could escape the eyes of the nomads.

*Besides, all news about outsiders reaches my ears.*

But Chinggen’s confidence faltered at the old man’s next words.

“He’s a Peak master. He mainly uses a sword and palm techniques.”

“…Did you say he’s a Peak master?”

“Why? Wouldn’t that make it easier? He’ll stand out wherever he goes, so you should be able to find him quickly.”

Chinggen struggled to speak.

“I-I’m sorry, but if he’s a master of that level, my brothers would have noticed him long ago.”

“Hm. What do you think?”

“I control a fairly wide area myself, but I’ve never heard that a master like that has appeared.”

“If Chinggen can’t do it, I have no way either.”

The old man asked the same question of Black Sand and Temur, who had been sitting quietly with their shoulders hunched, and received similar answers. His brow furrowed.

“Damn that bastard. Making an old man go through all this trouble.”

The three men’s ears perked up at the bitterness in his mutter.

What kind of circumstances could have driven an unidentified Supreme Peak master to search for someone personally? And in a body suffering from old age, no less.

*His son? Or his Disciple?*

Judging by his attitude, it had to be a blood relative or a Disciple…

Black Sand felt his heart pounding. An old man standing at the end of his life was searching for someone while struggling to hold on to a mind that came and went.

Someone he had to meet before he died. He must have had at least one lingering regret that he absolutely had to resolve, even if he had to do it this way.

*Could this be…?*

Black Sand’s thoughts raced. Perhaps he could turn the life-or-death crisis he had faced today into an opportunity.

His lips parted slightly, and Sound Transmission slipped out.

— Chinggen.

Despite the sudden Sound Transmission, Chinggen showed no reaction. As expected, he was a shrewd one.

— Are you listening? Answer me.

— Accept the old man’s offer. Quickly!

— Impossible. I can’t find the person he wants. If we succeed, we may receive a great favor, but if we raise his hopes for nothing and fail, all we’ll gain is his resentment. I have no intention of dealing with that. Nor do I want to become more entangled with that old man.

— Find him.

— What?

— If you find him, you can obtain the old man’s martial arts. Martial arts powerful enough to look down on the entire world!

At that moment, Black Sand was filled with certainty. Whether the person was a Disciple or a son, they had to find him. If they succeeded…

*We could steal not just a single city, but the entire world!*

Black Sand’s plan was an attempt to blackmail a Supreme Peak master. Chinggen’s lips trembled as he grasped what Black Sand meant.

— Are you insane? Greed has blinded you!

— No, it’s entirely possible. You’re too afraid of that old man to think it through.

— Don’t be ridiculous. Do you think he’ll fall for a threat like that? He’ll tear us apart before that happens!

— He’s already an old man whose mind comes and goes because of his age. First, we search the surrounding area thoroughly and find the bastard, then we drag things out. Until the old man’s mind completely goes.

Even Black Sand thought it was a perfect plan. When the old man’s mind was not clear, he was no different from a child.

They would wait for that moment, then subdue him. Through persuasion and threats, they would steal every bit of that powerful martial arts knowledge.

— What are you hesitating over? Accept already!

That was when a reply came.

“Yes, go on and accept. What are you waiting for?”

Black Sand froze.

The old man was staring at him with reddish, glowing eyes. Flames no one could possibly resist streamed from his dark, sunken pupils.

“Are you finished?”

“E-Elder.”

“You’re not particularly bright, are you? You’ve already made me say the same thing three times.”

*Thud.*

At the same time, the old man’s palm pierced Black Sand’s abdomen. Scorching Yang Qi at its utmost burned his organs and seared his blood vessels.

“Didn’t I tell you not to call me elder?”

*Thump.*

Black Sand collapsed as a charred lump. Chinggen closed his eyes. A voice drier than desert sand drilled into his ears.

“I’ll be back in about a month.”

When Chinggen opened his eyes again, the old man was nowhere to be seen.

* * *

The old man clicked his tongue.

“Nothing has changed. Absolutely nothing has changed.”

The world he had returned to after so long was still the same. Evil people, righteous people, and grays who belonged to neither were all mixed together.

No matter who lived or died, the empty place was always filled. The same went for those mounted bandits. They had simply been unlucky.

“Speaking of which, the Northern Gaoyuan…”

He had come a long way. The old man muttered to himself and looked around.

The horizon stretched to the ends of the world. Here, where blue grassland and parched earth existed side by side, the old man already knew where his steps would take him.

*I’ll leave this area to that nomad bastard and search Shanxi Province myself.*

The old man began to walk. With every step, the landscape flashed past and the grasses bowed low.

His stride was leisurely, yet he moved as quickly as a loosed arrow. The arrow’s destination was Datong, on the border between Shanxi and the Gaoyuan.
## Chapter artifact 164

# Chapter 164

> **System**
>
> **Status Window**
>
> Lv. 71 Jin Taekyung
>
> **Class:** Peak Master
>
> **Fame:** 2,400 (+250)
>
> **Titles:** 5 (Title effects active)
>
> - Returnee (All stats +10)
>
> - Sleeping Dragon of Shanxi (All stats +15, Fame +200)
>
> - Scion of a Prestigious Family (All stats +5, Fame +50)
>
> - Gambler (Combat-related stats +10% in one-on-one combat)
>
> - Intermediate Trainee (Training speed +20%)
>
> **Strength:** 255 (+30)  
> **Stamina:** 207 (+30)
>
> **Agility:** 250 (+30)  
> **Intelligence:** 40 (+30)
>
> **Charm:** 40 (+30)  
> **Internal Energy:** 45 years
>
> **Toughness:** 200 (+30)
>
> **Remaining Points:** 70
>
> - Distribute your remaining points.

It was a Status Window I looked at more than ten times a day, but my mouth still split into a grin every time I saw it.

Who knew the four characters meaning “Peak Master” could make me this happy?

*The System calls me a master. A Peak Master.*

Only a few hours ago, the Class field had read [First Rate Martial Artist]. But now I was a Peak Master. Not a martial artist, but a master.

I had become a genuine master, recognized even by the System.

*I’m already Level 71, too.*

The rewards had been incredible.

Seven level-ups, a one-stage increase in both the Jin Family’s Cultivation Technique and Qi Sense, and…

*I even got something you couldn’t buy with money.*

Open Inventory.

As soon as I entered the command in my mind, a familiar System notification chimed, and a translucent holographic window appeared.

My Inventory was packed with all kinds of junk I had collected in the Murim, but my eyes fixed squarely on one item.

*Summon Ten-Thousand-Year Cold Iron.*

Whoosh.

A heavy sphere suddenly popped into existence in midair. It was about the size of a bowling ball, its unpolished surface uneven and jagged, bulging out in every direction.

At first glance, it looked like a useless lump of metal or a rock. But with even a little attention, one could recognize its true value.

*Inspect Item.*

Ding.



> **System**
>
> **Item Window**
>
> **Unprocessed Ten-Thousand-Year Cold Iron**
>
> **Type:** Material
>
> **Grade:** Supreme Peak
>
> **Restriction:** Master Artisan
>
> **Description:** Ten-thousand-year-old cold iron is harder, sharper, and rarer than any mineral currently existing in the world. Only a craftsman who has reached the ranks of a master artisan will be able to handle this precious material.

“Now, this is the real deal.”

Personally, I was happier about obtaining the Ten-Thousand-Year Cold Iron than I was about leveling up. I was a Hunter, and I was a martial artist. Anyone in this line of work had dreams about their equipment.

I simply hadn’t had the means to turn those dreams into reality.

*I had no money in the real world, and in the Murim, I didn’t have a decent spear.*

The Jin Family of Taiyuan’s roots lay in sword techniques, not spear techniques.

Supply followed demand. From the lowest-ranking martial artists to the heads of the family, most of them were sword users. As a result, both their martial arts and the quality of the weapons in the armory were far superior for swords than for spears.

If Jin Wikyung hadn’t looked out for me, I might have had to fight with a cheap wooden spear or bamboo spear.

How many times had my guts twisted whenever I swung an iron spear while leaving the [Unnamed Sword], made from Ten-Thousand-Year Cold Iron, at my side?

*But that humiliation is over now.*

I had obtained the finest mineral in the world. I could have a beloved weapon of my own made.

Of course, there was one prerequisite.

The Quest I had received this time was related to it.

*Inspect Quest.*

Ding.



> **System**
>
> **Quest**
>
> **Find the Master Artisan**
>
> Forging Ten-Thousand-Year Cold Iron requires tremendous experience and skill. Only an exceptionally skilled artisan will be able to draw out all the power of this precious material.
>
> **Grade:** Peak
>
> **Restriction:** Jin Taekyung
>
> **Mission:** Commission a Master Artisan to make a weapon (Incomplete)
>
> **Reward:** ???
>
> **Failure:** ???

I smiled contentedly and closed the Quest Window.

*Of course. I can’t entrust something as valuable as Ten-Thousand-Year Cold Iron to just anyone.*

Even without the Quest, I would have looked into it myself.

Just as a famed sword only truly revealed its brilliance in the hands of a master, precious materials like Ten-Thousand-Year Cold Iron were no different.

Although the Quest was graded Peak, the mission itself didn’t seem particularly difficult.

*Finding someone shouldn’t take long.*

Surely there had to be at least one master artisan in this enormous land.

The Jin Family of Taiyuan had branches spread throughout Shanxi. If I asked Jin Wikyung to send out word, we would soon know where to find one.

*And if that doesn’t work, I can ask the Lower District Sect.*

I even had a powerful connection in Wolhwa. With eyes and ears planted throughout Shanxi Province, something like this would be a piece of cake for her.

*Whatever it takes, I’m completing this Quest before I leave.*

A month in the Murim was only three hours in the modern world.

I still had plenty of time.

“Hehehe. A spear made from Ten-Thousand-Year Cold Iron. A spear made from Ten-Thousand-Year Cold Iron…”

Just as I was grinning from ear to ear—

Bang!

The door burst apart with a deafening roar. A person rushed in like lightning and threw both arms wide toward me.

“Youngest!”

Yep. I knew it would be you.

I let out a deep sigh and asked Jin Wikyung,

“What’s going on?”

“What do you mean, what’s going on? I heard the wonderful news that you broke through the wall and rushed here at once!”

“…How did you hear about that?”

It had only happened an hour or two ago, but the speed of the information network was no joke. Had this guy attached a Familiar to me or something?

As I stared at him in bewilderment, I suddenly noticed Hyuk Mujin standing in front of the blown-open doorway, smiling proudly. He casually rubbed beneath his nose and said,

“Shouldn’t such wonderful news be delivered first by the closest aide?”

“…”

Not a Familiar. It was a Hyuk-miliar.

That bastard had definitely used my name to score some points with Jin Wikyung.

“Our youngest broke through the wall! He reached the Peak realm!”

As expected, Hyuk Mujin quickly cut in.

“Lesser Family Head, I served as his guard!”

“Thank you. Truly, thank you. Your contribution was enormous!”

“Not at all. As your right arm, I merely did what I was supposed to do. I had not a shred of selfish intent. However, I noticed that the position of Master of the Gatekeeper Pavilion is still vacant…”

“It’s yours without question! No, you’ll be the next Family Head of the Jin Family of Taiyuan!”

“W-Whaaaat? Is that really true?”

“…”

Of course it wasn’t, you dumbass.

Did it make any sense to appoint someone Family Head just because he had stood guard? And all that bastard had actually done was snore.

But the two men, blinded by joy and power, were already out of their minds.

“Hyuk Mujin. You said your name was Hyuk Mujin, right?”

“Yes, Lesser Family Head!”

“Our Mujin can do whatever he wants! Become Family Head! Smash the Nine Sects and One Gang! Smash the world!”

“Smash!”

“…What are you smashing, you lunatics?”

The future of the Jin Family of Taiyuan looked bleak.



* * *

After the commotion finally passed, Jin Wikyung managed to calm himself and looked at me with moist eyes.

“Your brother is proud of you.”

“I’m proud of you too, Captain. But if I hadn’t served as your guard…”

“Mujin, let’s keep quiet unless you want your pot cracked. And by ‘pot,’ I mean your head.”

“Yes, sir.”

Hyuk Mujin, now sporting a lump on his forehead, answered at once. As expected, he only listened after getting hit.

“Your useless older brother couldn’t even look after you properly, and yet you grew up this well all on your own. Sniff.”

“…”

Look at the sensitivity on this human weapon.

Whenever Jin Wikyung acted like this, I was grateful that this world had no social media. If it did, a post tagging every member of the Jin Family of Taiyuan would have gone up on Outstagram.

A teary-eyed selfie and hashtags would have been included for free.



#JinFamilyofTaiyuan #UselessOlderBrother #OurYoungestIsAPeakMaster #KeepYourChinUpToday



Wolhwa: Oh my! Young Master Jin? Congratulations!

Cheongpung: Wow, this is my first time pressing Like!

Wipeng: Don’t lie.

Hyuk Mujin: I served as his guard.

Jin Mukyung: Is this a country?

Zhu Bao: An autograph, please.



The thought of countless Shanxi Province celebrities reacting like that made my vision swim.

I hurriedly pushed the horrifying image from my mind and comforted Jin Wikyung.

“Please stop crying. How old are you?”

“Sniff. How did that immature little youngest grow up to be such a fine man?”

Jin Wikyung gazed at me with a mixture of emotion and pride, then wiped the corners of his eyes with his sleeve.

“No, this won’t do. I need to go right now and…”

“You’re not planning to write ‘Jin Taekyung has become a Peak Master’ on a gigantic banner like last time, are you?”

“Huh.”

“…”

I knew it. Judging by everything Jin Wikyung had done until now, there was no way he would let this opportunity pass. I had to make myself perfectly clear.

“Don’t do anything like that. It’s cringe.”

“Cringe? What does that mean?”

“It means embarrassing.”

Jin Wikyung asked with a shocked expression,

“Are you saying you’re embarrassed by me? By your own brother?”

“No, that’s not what I…”

This was driving me insane.

Before I could answer, Hyuk Mujin, who had been sitting there quietly with his shoulders hunched, suddenly cut in with a baffled expression.

“Huh? Captain, you usually like getting attention.”

“When have I ever?”

“You don’t? If I remember correctly, you seemed to like it a lot. When we returned from the Mount Heng Sword Sect, you waved your hand like crazy from the very front.”

“…Ahem.”

If he had been making that up, I would have punched him. But it was true, so I had nothing to say.

I quietly avoided Hyuk Mujin’s gaze and replied,

“That was different. I had my reasons.”

“What reasons?”

“There were reasons. You don’t need to know.”

“Wow, there he goes again.”

I ignored Hyuk Mujin’s muttering and turned my gaze back to Jin Wikyung.

“Anyway, we’re not doing anything like that. The attention I’m getting now is more than enough.”

“Hm. If that’s truly what you want…”

Jin Wikyung couldn’t hide his disappointment, but I was so firm that he reluctantly nodded. That let me breathe a sigh of relief.

*What’s the point of advertising that I became a Peak Master? I’ll only attract a whole swarm of flies.*

There had been a time when I was willing to risk my life for Fame, but not anymore.

No, if anything, it felt ominous.

*Why does it feel like the higher my Fame gets, the stronger the people it attracts become?*

My life motto was to live thin and long. Of course, living thick and long would be even better, but people who lived that way rarely had peaceful lives.

And after constantly fighting battles where my life hung in the balance, I was exhausted in both body and mind.

*I need to make at least the bare minimum of preparations.*

I planned to make one hell of a spear from the Ten-Thousand-Year Cold Iron and hone my martial arts. To do that, I absolutely needed Jin Wikyung’s help.

“Could you do me one favor?”

Jin Wikyung was not the sort of person to refuse. He confidently nodded.

“Say the word.”

“I need information.”

“Information? About what, exactly?”

“Two things. First, the whereabouts of a master artisan skilled enough to work with Ten-Thousand-Year Cold Iron. Second, news about the Fire King.”

“The first is understandable, but the Fire King… Surely you aren’t thinking of learning *that*?”

*That* referred to the Flame Divine Palm.

I had never told Jin Wikyung directly, but he already knew everything.

It made sense. The Flame Divine Palm was the Fire King’s signature martial art, and touching it carelessly was no different from holding a bomb that could put the entire family at risk. I had already guessed that Jin Mukyung would have told his Lesser Family Head brother about it long ago.

“Taekyung.”

At the concern in his voice, I waved my hand.

“I’m not planning to learn it right away. I just want to confirm whether the Fire King is alive or dead before I decide.”

“Hmm.”

After a brief silence, Jin Wikyung spoke.

“Will you promise me one thing? Before you do that, you’ll consult with me first.”

“Yes.”

“Then that’s settled.”

Jin Wikyung nodded decisively and rose from his seat.

“Information about the Fire King may take some time, but I can tell you about the first matter right now.”

Already? That was the Jin Family of Taiyuan for you. They seemed to have a handle on almost everything.

The progress was much faster than I had expected. My butt practically itched with impatience to go find the man immediately.

“He must be someone nearby?”

“Yes. He has apparently been living in seclusion without anyone knowing. Even our family only learned of his existence recently.”

“Could you tell me about his skill?”

“I guarantee that even if you searched the entire world from top to bottom, he would be among the top ten.”

If Jin Wikyung could speak that confidently, then the man’s skill was beyond question.

A master artisan capable of handling Ten-Thousand-Year Cold Iron. I had found him much faster than expected.

“I’ll go back and confirm it once more, then send word. Now, get some rest. Ho ho, you broke through the wall. A Peak Master at twenty!”

Jin Wikyung disappeared with a broad grin. Hyuk Mujin opened his mouth, looking as though his curiosity might kill him.

“What is it?”

“Hm? What is what?”

“What on earth is that ‘thing’ related to the Fire King?”

“Oh, that? The Flame Divine Palm.”

“The Flame Divine Palm?”

He looked utterly bewildered. Of course. He wasn’t a martial arts expert like Jin Mukyung, so it was only natural that he didn’t know.

“Yeah. The Flame Divine Palm. It’s the Fire King’s signature martial art.”

“…What?”

“Why are you so surprised?”

“H-How did you get it? No, before that, is it really all right to tell me something this important?”

I answered him kindly despite the expression of shock and confusion on his face.

“Yeah. You even saw it yourself.”

“…What?”

“What do you mean, ‘what’? You’ve seen the Flame Divine Palm martial arts manual before. No, you didn’t just see it—you almost ended up owning it.”

“I did?”

“Yeah. Don’t you remember? Before the battle at Eight Spring Gorge, we stayed behind as the rear party. With those Samdo Sect guys—Gwak Jun or whatever his name was, and the others.”

Hyuk Mujin sank into thought, and his mouth slowly fell open.

“Don’t tell me it was that thing back then…”

“That’s the one. The thing you refused when I told you to take it.”

“…”

“Whew. Good thing I didn’t give it to you back then.”

Hyuk Mujin’s face twisted miserably.

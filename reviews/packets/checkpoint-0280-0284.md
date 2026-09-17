# Checkpoint Review — 280–284

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

# Chapters 280–284

## Plot

Jin Taekyung stormed Myeongdong Guild headquarters after Park Jihoon’s role in the Black Hunter operation became clear. He defeated Team 1 and roughly fifty additional Hunters, occupied Jihoon’s office, and rejected Jihoon’s offers of money, land, buildings, Gate rights, and silence. Taekyung demanded a sincere apology and compensation for the injured D-rank Hunter, as well as an apology from the unidentified “that person” who had ordered Jihoon.

Jihoon revealed hidden strength and fought Taekyung alongside Guild Master Park Tae Seop, but Taekyung overwhelmed both men, breaking Jihoon’s knee and disarming them with Mae Jonghak’s Flow principle. Lee Jungryong then arrived, identifying himself as Ares Guild’s Vice Guild Master, one of Korea’s two S-rank Hunters, and a Supreme Peak master. He claimed only an acquaintance with Tae Seop and no connection to Jihoon, but Jihoon’s cry of “Master” exposed their relationship.

Lee attacked Taekyung with a powerful palm technique and injured him, though Taekyung’s Flame Divine Palm also withstood Lee’s strike. While restraining Lee with a dagger at Jihoon’s throat, Taekyung severed both of Jihoon’s arms and badly injured his leg and shoulder. He left Jihoon alive but warned that Jihoon’s Hunter career might be over, and threatened to collapse the building and expose the confrontation publicly.

## Continuity

- Taekyung defeated Myeongdong Guild Team 1 and approximately fifty additional Hunters, then occupied Jihoon’s office.
- Park Tae Seop is Myeongdong Guild’s Guild Master, a Great Cataclysm hero, and one of Korea’s top rankers. He fought Taekyung under pressure from “that person.”
- Park Jihoon secretly possesses considerable strength, uses a fingerprint- and iris-protected phone, and can recover with potions. Taekyung broke his knee and severed both arms, while also seriously injuring his leg and shoulder; Jihoon survived.
- Lee Jungryong is Ares Guild’s Vice Guild Master, one of Korea’s two S-rank Hunters, and a Supreme Peak martial artist. He has known Tae Seop since the Great Cataclysm.
- Lee Jungryong is Jihoon’s master, and Jihoon is his disciple. Lee gave Jihoon his initial orders, but the story has not confirmed that Lee is the unidentified “that person” directing the broader operation.
- Lee’s qi control and palm technique are comparable to those of the Yin-Yang Twin Devils. His attack injured Taekyung, but Taekyung remained capable of controlling the confrontation.
- Taekyung demanded an apology, compensation, and one person’s life, specifically connecting Jihoon’s punishment to the injuries suffered by Im Kkeokjeong.
- Taekyung threatened to bring down Myeongdong Guild’s headquarters and reveal the incident across Korea.
- The Black Hunter operation, the blockade of high-level Gates around the Peace Guild, and the order targeting its D-rank Hunter remain only partially explained.
- Choi Minwoo led an evidence-gathering ambush after the Black Hunters’ secret house was burned and captured Myeongdong personnel.
- Team 11’s fate after losing contact remains unknown.
- The exact wrongdoing Jung Hyunwoo uncovered before Jihoon killed him remains unknown.
- The proposed apology and compensation for the injured Hunter and his family have not yet been delivered or enforced.

## Translation Decisions

- Retain **Black Hunter**, **Myeongdong Guild**, **Peace Guild**, **Team 11**, **Ares Guild**, **Vice Guild Master**, **S-rank Hunter**, **Supreme Peak**, and **Great Cataclysm**.
- Render **그분** as **“that person”**, preserving the unknown commander’s ambiguity.
- Render **이정룡** as **Lee Jungryong**, **박태섭** as **Park Tae Seop**, and **박지훈** as **Park Jihoon**.
- Retain **Master** and **Disciple** for Lee Jungryong and Park Jihoon’s martial relationship.
- Render **흐름** as **Flow** when naming Taekyung’s application of Mae Jonghak’s movement principle.
- Retain **Flame Divine Palm** and the established distinction from the other divine-fist techniques.

## Durable state

{
  "active_continuity": [
    "Taekyung defeated Myeongdong Guild Team 1, occupied Jihoon's office, and currently holds Park Tae Seop and Park Jihoon at knifepoint.",
    "Park Tae Seop is Myeongdong Guild's Guild Master, a Great Cataclysm hero, and one of Korea's top rankers; he fought Taekyung alongside Jihoon under coercive pressure associated with 'that person.'",
    "Lee Jungryong is Ares Guild's Vice Guild Master and one of Korea's two S-rank Hunters.",
    "Lee Jungryong is a Supreme Peak master with qi control and palm technique comparable to the Yin-Yang Twin Devils.",
    "Lee Jungryong has known Park Tae Seop since the Great Cataclysm and is Park Jihoon's master.",
    "Lee Jungryong gave Jihoon his initial orders and offered to resolve the matter while denying or obscuring his connection to the Black Hunters.",
    "Taekyung demanded an apology, compensation, and one person's life from Lee Jungryong.",
    "Lee Jungryong's attack injured Taekyung, while Taekyung's Flame Divine Palm met Lee's palm without dislodging him.",
    "Taekyung severed Jihoon's arms and inflicted severe injuries to his leg and shoulder, but left him alive; Jihoon called Lee Jungryong Master.",
    "Taekyung threatened to collapse the building and expose the confrontation across Korea.",
    "Jihoon previously used a secret fingerprint- and iris-protected phone and a potion to recover from Taekyung's assault.",
    "Jihoon previously threatened to end Taekyung and the Peace Guild if Taekyung advanced farther.",
    "Jihoon and Myeongdong Guild sent Black Hunters against the Peace Guild and coordinated a blockade of high-level Gates around it.",
    "Jihoon acted under orders from an unidentified 'that person,' whose identity and broader role remain unconfirmed.",
    "Choi Minwoo led an evidence-gathering ambush after the secret house burned and captured Myeongdong Guild personnel.",
    "Team 11 remains an officially nonexistent Myeongdong Guild team whose fate after contact was lost is unknown.",
    "The exact wrongdoing Jung Hyunwoo uncovered before Park Jihoon killed him remains unknown.",
    "The identity of the authority that authorized the Black Hunters to target the Peace Guild's D-rank Hunter remains unresolved."
  ],
  "continuity_sources": [
    284
  ],
  "open_questions": [
    "Is Lee Jungryong the unidentified 'that person,' and is Ares Guild directly behind the broader Black Hunter operation?",
    "What exact authority and role did Lee Jungryong and Park Tae Seop hold in the Black Hunter operation and the blockade of Gates?",
    "What happened to Team 11 after contact was lost?",
    "What exact wrongdoing did Jung Hyunwoo uncover before Park Jihoon killed him?",
    "Who authorized the Black Hunters to target the Peace Guild's D-rank Hunter?",
    "What consequences will follow from Jihoon's mutilation and loss of both arms?",
    "Will Lee Jungryong retaliate against Taekyung or attempt to contain the incident?",
    "Will the proposed apology and compensation for the injured Hunter and his family be delivered or enforced?"
  ],
  "safe_through": 284,
  "temporary_decisions": [
    "Render 이정룡 as Lee Jungryong and 스승님/제자 as Master/Disciple.",
    "Render 임영준 as Im Yeongjun and 블랙 헌터 as Black Hunter.",
    "Render 명동 길드 as Myeongdong Guild and 평화 길드 as Peace Guild.",
    "Render 11팀 as Team 11.",
    "Render 그분 as 'that person' and 어른폰 as AdultPhone, retaining the child/adult pun footnote.",
    "Render 행신동 불닭볶음손 as Haengsin-dong Fire-Chicken Stir-Fried Hand, retaining the buldak-bokkeum-myeon/son pun.",
    "Render 흐름 as Flow when naming Taekyung's application of Mae Jonghak's movement principle.",
    "Use the established renderings Ares Guild, Vice Guild Master, S-rank Hunter, Supreme Peak, and Flame Divine Palm."
  ],
  "version": 1
}

## Reading copies

## Chapter artifact 280

# Chapter 280

“Park Jihoon, you fucking bastard.”

— ……

The voice that had been about to continue on the other end of the phone abruptly cut off.

I couldn’t see him, but his confusion and agitation at that moment came through clearly enough.

“What’s the matter? If someone calls you, you should answer.”

Not long afterward, a reply came.

— Is that you?

“Yeah, it’s me, you bastard.”

An agitated voice spilled from between my lips. Blood raced through my body, and my heart hammered in my chest.

But my head was as cold as if someone had poured ice water over it.

Maybe some part of me had already anticipated a situation like this.

*I kept thinking, surely not. Surely not.*

The number twenty-eight that had slipped from his mouth was enough to turn a faint suspicion into certainty.

What I wanted to know was whose orders they were acting on—and how deeply he was involved.

“Did you send those bastards?”

A low, smooth baritone answered.

— Who knows? If that’s what happened, then I suppose I did.

“……”

— What? Did you think I’d deny it?

Well, look at this guy.

His attitude, as if he had not a trace of shame before heaven, drew a hollow laugh from me.

— Who told you? Im Yeongjun? Of course. He’s the only one it could be. I thought he was the one guy who knew how to keep his mouth shut…but I misjudged him.

Park Jihoon clicked his tongue and continued.

— What a fucking idiot. I shouldn’t have left it to him.

“What did the shit do wrong? The asshole who dropped his pants and strained in public is the one at fault. But you…”

Crack.

The Team 1 Leader, who had been struggling with his neck caught in my grip, turned pale.

“Did you think about how you were going to clean up after making this mess?”

— It’s unexpected that things turned out this way…but do you really think I’d have done my business without considering the cleanup?

“Yeah. I’m saying that because it looks like you did.”

— What?

“Do you think you can handle me?”

Silence descended.

One second. Two seconds. Three.

And at the end of that short silence came a cold, razor-sharp voice unlike anything I had heard from him before.

— If you take even one more step from there, you and the Peace Guild are finished.

“So?”

— It’s not too late. Don’t make this any bigger than it already is. Come out. Let’s finish this here.

Hearing that, I suddenly thought that the way the world worked wasn’t all that different from a battle.

The one who seized the advantage pressed forward without mercy, while the one who felt fear took a step back first.

And I knew exactly what Park Jihoon was afraid of.

*Black Hunters.*

The existence of Black Hunters—the illegal private armies of major Guilds.

The thought that they were holding Park Jihoon back made the corners of my mouth rise.

“Finish this?”

— Yes.

“Who decided that?”

— …!

“You were the ones who started it. I’ll decide where it ends.”

On the other end of the phone, Park Jihoon’s breathing grew ragged.

— Well, well. I knew you were stupid, but you’re even worse than I thought.

“The result will be more than you expect, too. You can fucking look forward to it, sir, you son of a bitch.”

That was when it happened.

Ding.

— Nineteenth floor.

With the mechanical announcement, the tightly closed elevator doors slowly slid open.

A high ceiling and a broad hallway came into view, with dozens of people moving through it.

Several of them naturally turned their eyes in this direction. Then their mouths fell open.

“T-Team Leader?”

“You there! Who the hell are you…?”

Instead of answering, I threw the Team 1 Leader. A Hunter who had been approaching while pointing at me slammed into the wall together with him.

At the same time, an employee sitting at the desk screamed and pressed the emergency button.

WEEEEEE!

“Emergency! Emergency!”

“It’s an intruder! Team 1, arm yourselves!”

Amid the shrill noise, Park Jihoon’s final words pierced my ears.

— Go ahead, then. Let’s see you try.

Beep. Beep. Beep……

I shoved the Team 1 Leader’s phone, now disconnected, into my inner pocket.

When I pulled my hand out again, there were two daggers in it instead of a phone.

*“Let’s see you try?”*

I was already planning to.

“Who are you?!”

“Drop your weapons! If you don’t want to die, do it now!”

Myeongdong Guild’s elite Hunters armed themselves at incredible speed and surrounded me in a half-circle.

Behind me was the elevator. The only other person there stood frozen like a plaster statue, muttering to himself.

“This is a dream. It has to be a dream.”

I glanced at him, half out of his mind, and asked,

“What phone do you use?”

“Huh?”

“Your phone. What kind?”

“I-I use an AdultPhone 25.”

“Ah. The apple you bit into and spat out.”

“Y-Yes, yes. That’s right.”

“Take it out and record a video.”

“Yes, sir!”

He answered loudly, then stopped halfway through pulling out his phone.

“Y-Yes, sir? I’m sorry, but what did you just say?”

“You said you use an AdultPhone 25. The image quality is much better than mine, so I thought it would be better to film with that one.”

“W-What do you want me to film?”

“Everything.”

Just then, the fallen Team 1 Leader sprang to his feet and shouted,

“What are you waiting for, you bastards? Beat the hell out of that bastard right now!”

“Team Leader, isn’t that Hunter Jin Taekyung? What is going on all of a sudden…?”

“I’ll take responsibility.”

No matter the Guild, Team 1 was its symbol and elite force.

And Team 1 of Myeongdong Guild, which was consistently ranked among the top ten in Korea, was a team of professionals among professionals. They were no different from living combat machines.

“This is an order from above. Don’t think of him as a person. Think of him as a monster and fight.”

The moment their Team Leader gave them a firm order, dozens of gazes sank into cold focus.

Five tower shields at the front slammed into the marble floor simultaneously, without a single inch of error.

Boom!

“Formation—!”

In the middle of their peaceful daily lives, the downtown building became a battlefield.

* * *

*What am I looking at?*

Lee Minsu, a C-rank Hunter belonging to Myeongdong Guild’s Security Team, blinked.

The scene unfolding before his eyes was simply that unreal.

Krrr-crack! Boom!

A tower shield as sturdy as an armored vehicle shattered, and a massive tank flew far away as if it had been struck by a giant’s hammer.

A gap barely wide enough for one person opened for the briefest moment.

A pale figure slipped through it.

And then—

Shriiiik! Slash! Slash!

“Gaaah!”

“Gasp!”

With a flash of light, the shield wall collapsed.

The tanks toppled forward in an undignified heap, their calf tendons cleanly severed.

*How did he…?*

The attacks were too fast to see properly.

Blink once, and two people fell. Blink twice, and three or four fell.

Every time the young man in the gray hoodie, Jin Taekyung, took a step, blood spurted and screams overflowed.

“Stop him! Stop him!”

“Damage dealer!”

The front line where the tanks had been holding had already collapsed the moment the battle began. Five blades swung powerfully toward Jin Taekyung as he advanced one step at a time.

Whoosh-whoosh-whoosh-whoosh!

Both shoulders and the chest. Both legs as well.

Three targeted his upper body, while two targeted his lower body. They were attacks he could not avoid without retreating.

“We got him!”

At the instant someone cried out in delight, the daggers in Jin Taekyung’s hands blurred like mist.

Clang-clang-clang-clang-clang!

The five blades everyone had been certain would hit shot into the air.

The Hunters holding their hilts stared at Jin Taekyung in disbelief. Their hands had burst open from the force of the deflection, dripping with blood.

“W-What is this…?”

“That’s impossible!”

Jin Taekyung answered their scream of disbelief in a flat voice.

“It seems possible to me.”

Slash!

A single line swept horizontally across the air.

An attack that could neither be seen nor avoided.

Five Hunters who had just attempted to attack stood directly in its path.

Fwoosh!

As the Hunters fell, spraying fountains of blood from their chests, a streak of light pierced between them.

Whooosh! Thunk!

The arrowhead stopped just short of Jin Taekyung’s chest.

It was an arrow shot with perfect accuracy by an A-rank Hunter, mana coursing through it.

But what stopped it was neither a shield coated in various magics nor a sharp weapon.

Crack.

Jin Taekyung broke the arrow shaft between two fingers and flicked his hand.

With a terrifying whistle, the arrow shot back along its original path, shattered three defensive spells, and buried itself in its owner’s shoulders.

Thud!

“Ghk!”

“If you fire one more arrow, I’ll make sure you have an odd number of balls.”

“……!”

“And the rest of you, step back if you don’t want to end up with lopsided balls. Adjusting my strength is annoying.”

He had been holding back?

The Hunters of Team 1 felt as if they had been possessed by ghosts. It was hard enough to believe that he had rendered more than a dozen people unable to fight in the time it took to drink a glass of cold water.

And he had been holding back while doing it?

For a moment, the same thought occurred to all of them.

*What kind of monster is this?*

Who were they?

They were Myeongdong Guild’s elite—the battle-hardened veterans of its Hunter force. The least experienced had eight years under their belts, while the most senior had been Hunters for more than twenty.

They had reached this position because they possessed exceptional skills compared to other Hunters of the same rank, and they took great pride in that fact.

At least, they had—until they faced Jin Taekyung here today.

“Please move aside while I’m still speaking politely, Seniors. I’d really like to smash every one of your faces in, but you don’t seem to be directly involved, so this is all I’m doing.”

He was dressed casually, in loose track pants and a gray hoodie, as if he had stopped by a café near his home. But not a single person ignored his words.

He had already shown them his strength and carved it into their minds.

“So clear a path.”

Even veterans who had fought countless fierce battles in Gates found it hard to breathe beneath the aura pressing down on the room.

It was a primal fear unlike anything they had ever felt from a monster.

*Monster. That guy is a real monster.*

Step. Step.

The monster walked straight toward them.

The Hunters moved their feet without realizing it and made way.

That was when—

“Burning Hands!”

Whoosh!

A hand wreathed in flame came crashing down on Jin Taekyung amid fierce heat.

It was a fire spell capable of melting even ordinary rock, but the huge hand made of mana vanished without a trace the moment it collided with Jin Taekyung’s palm.

“M-Magic?”

“It’s called the Flame Divine Palm. Pretty useful, right?”

The Team 1 Leader’s eyes widened at the sight of the palm wrapped in blue flame.

Jin Taekyung stared at him and licked his dry lips.

He looked like a predator that had just discovered prey it had forgotten about.

“Ah. You’re the exception to what I said earlier.”

“Gasp.”

Whoosh!

Jin Taekyung’s form scattered like a ghost.

But the Team 1 Leader was an outstanding battle mage in his own right, having led Myeongdong Guild’s elite team. Even in his panic, he reacted quickly.

“Blink!”

It was a teleportation spell that allowed him to move anywhere within ten meters, as long as the destination was within his field of vision.

*If I move behind him and unleash my attack spells all at once, even someone as skilled as him…*

The Team 1 Leader used Blink to move behind Jin Taekyung, but for an instant, he was overcome by the sensation that the world had stopped.

Jin Taekyung’s clear, deep black eyes were right in front of his face.

Thud. A palm still radiating heat pressed down on his shoulder.

“Why are you so surprised?”

“……!”

“You were rolling those eyes around so conspicuously.”

Had he predicted the direction from the movement of his eyes?

No. That wasn’t all.

The Team 1 Leader’s body trembled as if struck by lightning.

*This guy’s movements are faster than my Blink spell.*

What kind of monster was he?

And what kind of monster had Park Jihoon—and Myeongdong Guild—provoked?

With a trembling voice, the Team 1 Leader recited the final spell he had prepared.

“P-Poison.”

Whoosh.

A green poisonous fog poured out and coiled around Jin Taekyung’s face.

But just as the Team 1 Leader had ominously sensed, the monster proved once again that he was, in fact, a monster.

“Ugh. Smells like a fart.”

Jin Taekyung’s handsome brow furrowed.

That was the entirety of his reaction to the Poison spell.

Having reached Peak and attained the realm of Unaffected by a Hundred Poisons, Jin Taekyung blew on the frozen Team 1 Leader.

“Hoo.”

“Gasp.”

The Team 1 Leader inhaled the poisonous fog, and his face turned blue.

Jin Taekyung grabbed the Team 1 Leader—whose entire body had gone rigid from the paralyzing poison—by the nape, looked around, and asked,

“Where is that bastard Park Jihoon’s office?”

Ten fingers pointed toward a single door.
## Chapter artifact 281

# Chapter 281

The limousine raced down the road without a single jolt.

Park Jihoon took a bottle of water from the refrigerator installed inside and offered it to the middle-aged man sitting across from him.

“Would you like some?”

“In this situation? And where did you learn the habit of offering someone else’s things as if they were yours?”

“Then I suppose it’s all right if I drink only half. I have at least that much of a stake in bringing Myeongdong Guild to where it is today.”

“……”

The middle-aged man, Myeongdong Guild Master Park Tae Seop, glared silently at Park Jihoon as he tipped back the bottle.

“You’re awfully calm.”

After emptying exactly half the bottle, Park Jihoon leaned back against the soft seat and answered,

“Is there some reason I should be worried?”

“This whole mess has happened, and you’re acting as if nothing’s wrong?”

“It’s nothing more than a minor incident.”

“A sand tower can collapse from a single drop of water.”

“Because it’s a sand tower.”

“You’re saying Myeongdong Guild is different?”

“Five hundred Hunters under its banner. Twenty of them are A-rank Hunters. At this point, calling it an iron tower instead of a sand tower wouldn’t be inaccurate. And…”

The corners of Park Jihoon’s mouth curved gently upward.

“Myeongdong Guild should be excluded from the comparison. We have ‘that person,’ after all.”

“……”

“That’s true.”

Park Tae Seop nodded reluctantly, though his expression remained displeased. Seeing him like that, Park Jihoon asked,

“What is it? What has you so anxious that you can’t sit still?”

After a brief silence, Park Tae Seop spoke.

“A feeling.”

“What?”

“When you reach my age, you develop a certain instinct. Something you can’t explain.”

Ha.

Park Jihoon could not suppress a quiet laugh inwardly. He had wondered what the man was going to say, but in the end, it was nothing more than an old man past sixty throwing a fit.

*Just a feeling? What a ridiculous thing to say.*

Those thoughts appeared plainly on his face. And Park Tae Seop had lived too long not to notice.

“You may think it’s nonsense. I understand. It’s an area greenhorns like you can’t comprehend.”

“Ah, I’m sorry if that’s how you feel.”

“That tone, which doesn’t sound sincere in the slightest, is also something only a greenhorn could manage.”

“I simply can’t understand it. What exactly is bothering you so much?”

After a short silence, one person’s name slipped out.

“Jin Taekyung.”

He exhaled the name like a sigh. It was the name that had occupied his thoughts ever since contact with Team 11 had been lost.

For a brief moment, he had thought it was merely a trace of anxiety over things going wrong.

But it wasn’t.

His intuition, which had even endured the Great Cataclysm, had given him the answer to what troubled him.

“He’s a siege cannon. Not just a sand tower—even an iron tower could crack under his fire.”

Without waiting for a reply, Park Tae Seop reached out. He picked up the bottle of water Park Jihoon had left behind and drained it in large gulps.

His throat had grown so dry after speaking that he could hardly stand it.

Meanwhile, Park Jihoon’s brow furrowed deeply as he watched.

*Has the old man lost his mind?*

He admitted that the process of handling things had not gone entirely smoothly. There had been some unexpected snags, especially involving the Black Hunters and Team 11.

But even taking those into account, Park Tae Seop’s reaction was far too extreme.

It was only natural that Park Jihoon, who absolutely worshiped “that person,” should feel displeased.

“I didn’t know you rated Jin Taekyung that highly.”

“Because he’s shown us results.”

“Jin Taekyung only came into prominence recently.”

“And it’s also true that he’s shown us a great deal in that short time.”

“Shown us?”

A mocking smile touched Park Jihoon’s lips as he continued.

“That Won Myunghoon was trash. The bottom of the rankers. Even when the Korean Wave was at its height, the only reason he was put on the list once was as an act of charity. You know that too, Guild Master.”

“I heard he was stupid and greedy, and that his fame made him look more skilled than he really was.”

“And the Named Monster? It was called a Named Monster, but that Black Drake was the weakest of all the Named Monsters to appear in nearly twenty years. The Magic Gem recovered from its corpse wasn’t much different from one taken from an A-rank monster.”

“Then can you kill that weak Named Monster by yourself?”

“It wouldn’t be impossible.”

Park Jihoon answered without hesitation.

He took pride in his own abilities.

He possessed extraordinary talent, which was why he had received the honor of being chosen by “that person.” It was also why, despite not yet being thirty, he could sit across from the Guild Master of Myeongdong Guild and meet his eyes as they spoke.

But the next question stopped him short.

“Then what if you fought Jin Taekyung? Could you still be certain of victory against him?”

“……Of course.”

This answer came half a beat late. As Park Tae Seop watched him realize it and bite down slowly on his lip, he spoke.

“That hesitation just now seems to say something about what kind of person Jin Taekyung is.”

Park Jihoon replied coldly,

“I simply remembered something from the past.”

“Ah. You said you were friends, didn’t you?”

“I don’t want to talk about that. What I’m saying is that this incident isn’t as serious as you think, Guild Master.”

“We don’t even know whether Team 11 is alive or dead, and the public figure currently drawing more attention than anyone else in the country has barged into Myeongdong Guild headquarters. You’re saying that isn’t serious?”

“He’s an idiot. That’s why he lost control of his temper and recklessly broke into Myeongdong Guild headquarters.”

About ten minutes earlier, while Park Jihoon had been speaking with the Team 1 Leader on the phone, he had been startled by the sudden sound of Jin Taekyung’s voice.

At the same time, he had felt relieved.

*This will be easy to resolve.*

Myeongdong Guild had more than five hundred Hunters. Even if half of them had gone out on raids, an enormous number still remained at headquarters.

Of course, that number included Team 1, the Guild’s elite force.

“Jin Taekyung walked straight into a tiger’s den. Once we hold him there and sort things out, it’ll be over.”

There was no need to worry even if reporters who caught the scent of the story got involved.

He had—no, “that person” had—the power to render cameras and microphones useless.

“I’ll wrap everything up cleanly today.”

Park Tae Seop muttered with a face that suddenly looked much older.

“This isn’t normal. Maybe it’s because I’m getting old, but I’m starting to feel worn out.”

“It’s only a passing breeze. It would be a problem if the legs of someone who endured even the Great Cataclysm were trembling.”

Park Tae Seop recognized that the words contained criticism rather than encouragement and closed his mouth.

Just then, a monotonous cell-phone notification rang from somewhere.

“That isn’t my phone.”

“It’s mine.”

“Who is it?”

“Manager Kim, the one in charge of my security. I told him to find out what happened to Team 11. It seems he’s just arrived.”

“That’s good. Tell him to erase every trace related to Team 11 first.”

“Are you giving me orders now?”

Park Tae Seop frowned and answered the phone.

“It’s me. What happened? Hm? Ah, I see.”

His brow furrowed, then smoothed. His pupils repeatedly expanded and contracted.

As his expression grew stranger and stranger, Park Tae Seop pulled the phone away from his ear.

“What happened?”

“Take it.”

Park Tae Seop held out his phone to him. A vein stood out sharply on his forehead.

“Hello?”

“Hurry!”

Park Jihoon accepted the phone with a bewildered expression and pressed it to his ear.

A voice as soft as a cat’s paw slipped into his ear.

— Hunter Park Jihoon of Myeongdong Guild Team 1?

The instant he heard it, Park Jihoon realized.

The caller was not Manager Kim, whom he had crossed paths with several times.

The voice was young and polite, yet carried an air that made him difficult to approach.

“That’s me. Who is this?”

Something felt wrong.

The unfamiliar voice answered Park Jihoon’s question, which carried an instinctive sense of unease.

— My name is Choi Minwoo.

“Who?”

— Ah, I’m with the Peace Guild. I’m a Team Leader.

“……The Peace Guild?”

— Yes.

*Fuck.*

Park Jihoon’s lips twitched.

A few words were enough to figure out what had happened. Myeongdong Guild’s people had fallen neatly into a trap laid by the Peace Guild.

There was no need to see what had happened to Manager Kim, the phone’s owner. He was obviously either bound tightly and unconscious or helplessly watching someone else use his phone.

*Myeongdong Guild, you fucking idiots.*

The voice of Team Leader Choi coming through the receiver was as relaxed as a victor’s.

— I called because I’d like to have a conversation.

“Well, you see…”

Park Jihoon clenched his teeth, his mind racing furiously.

That was when a vibration traveled up from his chest.

It was not Park Tae Seop’s phone in his hand.

— Hunter Park Jihoon?

“Wait. Just a moment.”

With his free hand, Park Jihoon pulled his own phone from the inner pocket of his suit and checked it.

He had received a text message. The sender was…



**[Team 1 Leader]**



*Got him.*

Relief spread across Park Jihoon’s lips in a smile. Jin Taekyung, who had entered the tiger’s den known as Myeongdong Guild, had finally been forced to his knees.

The scales, which had been tipping in the other direction, had finally balanced.

But then—

“……Huh?”

The smile disappeared from Park Jihoon’s lips as he checked the message.

Filling the six-inch screen was not a report from the Team 1 Leader saying that he had captured Jin Taekyung, but an image file.

*What is this?*

The faces were familiar.

A young man was grinning broadly in the photograph, his face spattered with blood. A middle-aged man was held against him, his complexion blue and sickly, like that of a drug addict.

*Jin Taekyung…and the Team 1 Leader?*

That wasn’t all.

A familiar background appeared behind them.

The nameplate reading *Hunter Park Jihoon, Myeongdong Guild Team 1* provided a decisive clue as to where they were.

And there was something else.

*No way…… Did no one stop him? That one Jin Taekyung?*

It was a reality he did not want to believe.

That was when Park Jihoon’s wandering eyes began to shake.

Bzzz.

Another text message arrived with a vibration. Its contents were short, but devastating.

With just five words, it crushed Park Jihoon’s mind.



> **Team 1 Leader**
>
> Bring Melona when you come.[^1]

“This—this fucking…!”

Crack.

The phone in Park Jihoon’s hand crumpled like a sheet of paper.

Watching him, Myeongdong Guild Master Park Tae Seop muttered quietly,

“We’re fucked.”

* * *

> **Team Leader Choi**
>
> We’ve captured the people dispatched by Myeongdong Guild.

It was a text message from Team Leader Choi.

A few hours earlier, after burning down the secret house used by the Black Hunters, we had split into two groups.

An ambush team to secure definite evidence.

And me, who had insisted on acting alone.

It was because Team Leader Choi had argued that we absolutely had to capture something that could serve as evidence or a witness.

*He was right.*

They had been managed so meticulously that every Black Hunter, including Im Yeongjun, had already undergone identity laundering. There was no connection between them and Myeongdong Guild—not even the slightest link.

Team Leader Choi had identified that problem exactly.

*He’s always calm and composed.*

Looking back, he had never lost sight of the right direction.

Butler Kim’s role as an excellent mage and wise adviser probably helped, but at this point, I had to assume Choi was simply born that way.

*With this, we’ve secured one solid weakness.*

On top of the captured Black Hunters, we now had official employees of Myeongdong Guild as well.

That should make an excellent shield.

*And we could use it as a dagger, too.*

I sent a message saying good work, along with the photograph I had taken earlier.

Maybe it was because it was an AdultPhone,[^2] but even a picture taken with a foot came out great.

[^2]: “AdultPhone” is a Korean pun on iPhone: *ai* can mean “child,” while *eoreun* means “adult.”

“Should I take this opportunity to change my phone, too?”

Someone flinched at my mutter. It was a Security Team Hunter I had hired as my personal cameraman for the day.

Of course, I wasn’t paying him.

“Why?”

“N-No, sir!”

“Make yourself comfortable. Don’t just stand there. Sit on the sofa or something.”

“I’m comfortable like this!”

“You look uncomfortable to me.”

“I’m fiiiine!”

Was it my imagination, or did his shout sound like it contained a sob?

As an ordinary Security Team Hunter, he had just watched me completely destroy Team 1, a group whose elite members he would not have dared to meet eye-to-eye properly. His reaction was understandable.

*The ones who came later were similar.*

The other Myeongdong Guild Hunters who arrived later didn’t dare attack me after seeing the scene before them.

Of course, quite a few of them were armed with fierce devotion to their Guild.

Unfortunately, they lacked the skill to match. Every one of the men who charged at me was beaten to a pulp and carried away.

After I had knocked down around fifty of them, no one else tried to attack me. Park Jihoon’s office became forbidden territory that no one could enter.

I sank into the chair Park Jihoon had been using and thought,

*He must be racing here like a madman by now.*

Just thinking about him made my heart feel cold.

A middle-school classmate I had happened to run into on the street after a full ten years.

*How much of Park Jihoon was the real him?*

*Come quickly. Before I get any angrier.*

Crack.

That was when the armrest of the chair broke beneath the strength of my grip.

“H-He’s here!”

“Guild Master!”

Murmurs spread beyond the office door like a wildfire.

At the same time, I felt two massive presences approaching this way without hesitation.

*He’s here.*

And in the next moment, the door blew apart with a thunderous roar.

BOOM!

[^1]: Melona is a popular Korean melon-flavored ice cream bar.
## Chapter artifact 282

# Chapter 282

BOOM!

Two people appeared amid a thunderous roar.

I waved at the familiar face among them.

“Well, the fucking bastard’s here.”

“……You.”

I had been about to punch him in the mouth the moment I saw him, but when I saw his face twist in rage, all I could do was snort.

Looking at Park Jihoon’s tightly clenched fist, I asked with exaggerated disappointment,

“You didn’t bring it?”

“What?”

“Melona.”[^1]

“You little—”

A large palm seized the shoulder of the man whose face had flushed red.

“There are still too many eyes on us.”

Biting his lip, Park Jihoon took a step back.

As I watched him with amusement, the middle-aged man who had sent everyone nearby away spoke to me.

“Do you know who I am?”

I nodded. There was no way I could not recognize that face.

His name carried weight, and he appeared often enough in newspapers, magazines, and other media.

*Park Tae Seop, Guild Master of Myeongdong Guild.*

A war hero who had distinguished himself during the Great Cataclysm, and one of Korea’s top rankers.

After surviving every kind of brutal struggle and becoming the master of a major Guild, he was the dream of Hunters and a respected elder.

*I used to respect him, too.*

But not anymore.

My good memories of Park Tae Seop had expired two days ago.

Thoughts showed themselves in one’s attitude. Sensing the undisguised hostility in my gaze, Park Tae Seop opened his mouth.

“You…… consider me an enemy.”

“I can’t exactly consider you a friend. We both know each other’s circumstances.”

“Don’t be so quick to make assumptions. As you live, you come to realize that there are no eternal friends or enemies.”

“I don’t know about there being no eternal enemies.”

I continued while looking at Park Jihoon beside him.

“But there being no eternal friends certainly has some truth to it.”

Park Jihoon answered in a cold voice.

“Your premise is wrong from the start. We weren’t friends.”

“We weren’t friends.”

I sank deeply into the chair and repeated his words under my breath.

One thing I still couldn’t understand was Park Jihoon’s sudden change in attitude.

But……

“Then again, what does that matter at this point? It was already over the moment you sent the Black Hunters.”

At the mention of the sensitive term, Black Hunters, Park Tae Seop waved a hand.

At his Guild Master’s command, the hundred or so Hunters who had filled the hallway flowed away like the tide going out.

Listening to their footsteps recede, I curled up the corners of my mouth.

“You’re not exactly being open about it.”

“It’s a disgrace.”

“You’re honest enough to be irritating.”

“I’m ashamed of it myself.”

“For someone who considers himself ashamed, you gave a pretty damn despicable order.”

“……”

“What was the reason?”

An uncomfortable look crossed Park Tae Seop’s face. But it was not directed at me.

For the briefest moment, his eyes touched Park Jihoon standing beside him, then moved away.

*Well, well……*

What Park Tae Seop had just done was not intentional.

If that action had emerged unconsciously, then there was definitely something he was trying to hide.

I recalled the things that had never quite made sense and thought,

*Something stinks to high heaven. It reeks.*

While I was muttering inwardly, Park Jihoon suddenly spoke.

“To keep you and the Peace Guild in check.”

“To keep us in check?”

“The appearance of a new powerhouse means someone else’s slice of the pie gets smaller. Other Guilds probably feel the same way, not just us.”

At first glance, it was a reasonable explanation.

The Korean Guild market was already oversaturated. The ranks had been divided, and the pecking order established. The old powers did not want a new competitor to appear.

“The Peace Guild is dangerous. For now, you’re limited to Bucheon, but soon you’ll grow at a frightening pace and expand your influence.”

“So you sent the Black Hunters?”

“We did send them. But didn’t I tell you? It was only a warning.”

“I believe I told you, too. Because of that ridiculous warning, one person ended up crippled.”

“Crippled? His two severed arms were attached properly, weren’t they? He won’t have any trouble with his daily life. Do people call that crippled these days?”

“It’s as good as crippling him. One Hunter’s career is over.”

“It’s better than the Guild being finished.”

“What?”

Park Jihoon snorted.

“This is only the beginning. All the high-level Gates worth visiting have already been blocked off for your Guild. With the surrounding Guilds shutting you out, you’ll slowly wither away and die.”

I suddenly remembered something from a few days ago: Team Leader Choi telling me that the other Guilds had claimed every A-rank Gate.

Because of that, I had been forced to lead the rookies from one C-rank or B-rank Gate to another, unable to gain any meaningful experience.

“Don’t tell me that was—”

“You’re slow. Did you think it was a coincidence?”

The corners of Park Jihoon’s mouth rose. He had not only fully regained his composure, but was even relaxed enough to lean back against the sofa.

“I heard you recruited a lot of Guild members recently. What are you going to do? At this rate, you’ll have to let them all go within a year. You’ll be lucky if they don’t sue you for failing to pay their allowances.”

“……”

I slowly relaxed my folded arms.

“You’ve got some skill. No wonder you’re a major Guild.”

“Well, I suppose we are.”

“But…… we’re holding a pretty decent card on our side, too. I think it would be interesting if the things Myeongdong Guild did behind the scenes by scraping together a bunch of criminal bastards came to light. What do you think?”

Without waiting for Park Jihoon to respond, I continued.

“Looking at how things work around here, you’d just snatch them away if we handed them over to the police. So I figured it might be better to play a little truth game through a live iTube stream.”

“……iTube? A live stream?”

“Oh, right. You don’t know we opened a Guild channel, do you? Subscribe and hit Like, too. Don’t forget to turn on notifications.”

“……”

“Wow, we’re already at three hundred thousand subscribers. If this blows up, we could break ten million. Probably half the people in Korea will watch.”

The smile around Park Jihoon’s mouth vanished as if it had been wiped away.

“It would be better not to start something you can’t handle.”

“I can handle it.”

“Do you want to make every major Guild your enemy?”

“If I raise hell here, can you clean it up?”

“……”

Park Jihoon’s mouth pressed shut as if someone had glued it together.

After glaring at me with burning eyes for a while, he tossed out a single sentence.

“Tell me what you want.”

“What I want?”

“I’ll accommodate whatever you demand as much as possible. Don’t make this any bigger. Let’s negotiate here.”

“Negotiate.”

“If we take this all the way, we’ll both come out wounded. You know that, too.”

He was right. If this had been something I could take responsibility for alone, I would have gone all the way.

But the lives of so many people connected to the Peace Guild were at stake here.

Someone’s friend, lover, family……

Their futures, too.

I quietly licked my dry lips.

“What can you give me?”

“Money and power. And all kinds of benefits that will help the Peace Guild grow.”

“Didn’t you say the Peace Guild’s growth bothered you enough to send the Black Hunters?”

“Which is why we need to set a limit.”

“Don’t step outside the fence we assign you?”

“That’s right.”

The more I listened to Park Jihoon’s proposal, the more a rough picture formed in my mind.

The terms we could obtain in exchange for handing over the prisoners currently held by the Peace Guild and keeping silent about this incident were substantial.

No, they were enormous.

Buildings and land. The transfer of exclusive rights to high-level Gates controlled by Myeongdong Guild. And an enormous sum of cash.

The overall picture looked good.

But……

“The most important thing is missing.”

“Those conditions are more than sufficient—what?”

Park Jihoon furrowed his brow.

“What did you just say?”

“I said the most important thing is missing.”

“You’re crazy. You’re demanding even more here?”

“To be honest, explaining it to me won’t do much good. I only know that the value is high. Our Guild Master or Team Leader Choi are the experts when it comes to what’s beneficial and what’s harmful.”

“Then what exactly is missing?”

I stared at Park Jihoon.

“An apology.”

“……What?”

“If you did something wrong, you should apologize. But the most important thing—an apology—is missing.”

His proposal contained plenty of extravagant conditions, but no apology.

The thing that should have come before everything else had disappeared.

“Ha.”

Park Jihoon let out a hollow laugh. Absurdity and anger showed in the way he looked me up and down.

“Fine. I’m sorry. Happy now?”

“That’s not how you apologize.”

Crack.

A bone-shifting sound came from Park Jihoon’s tightly clenched fist.

But only for a moment. After taking a deep breath, he looked into my eyes and spoke each word clearly.

“I’m sorry.”

“That’s better.”

“Are you satisfied now?”

I gave a small nod.

“But next time you do it in person, try putting a little more sincerity into it. Bow your head politely, too.”

“……What the hell are you talking about now?”

“What good does your apology do me? You need to apologize to the victim and his family.”

Park Jihoon’s eyelids trembled.

“You want me to apologize to that D-rank Hunter?”

“What, can’t you?”

“I believe I already said I’d pay compensation. It’s an amount most Hunters could never even touch in their entire lives.”

“That works out nicely, then. A heartfelt apology will be even more effective if it comes with a massive compensation payment as an expression of remorse.”

“You…….”

I added one gentle remark to Park Jihoon, who was glaring at me with vicious eyes.

“If it hurts your pride, bring one more person along and apologize together.”

Myeongdong Guild Master Park Tae Seop, who had been listening to us in silence, finally spoke.

“I’ll go in person and apologize. With all sincerity.”

“At least you’ve got the basics down, Guild Master. I suppose you could call yourself a somewhat cleaner piece of shit.”

Cleaner shit. At this point, I could not think of a more appropriate—and more paradoxical—expression.

But Park Tae Seop was not the other suspect I had in mind.

I lifted my back from the chair and looked into Park Jihoon’s eyes.

“Bring along the person who gave you your orders. Make that person apologize, too.”

“……!”

An uncontrollable wave churned through his eyes.

It lasted only the briefest instant, but the violent agitation was more than enough to turn my suspicion into certainty.

“Fine. Guild Master Park Tae Seop just agreed, anyway.”

Park Jihoon continued in a voice as calm as he could manage.

“We’ll go together and apologize.”

“Cut the bullshit. Bring that person here.”

“I don’t know what you’re talking about.”

I rose with a silent laugh and walked toward the reception sofa where Park Jihoon sat.

“No matter how much I thought about it, I just couldn’t understand.”

I dropped into the seat across from him.

Beyond the large solid-wood table, I slowly examined him as he pretended to remain calm.

His solid build. The muscles visible beneath his shirt.

And I sensed the mana lying dormant inside him.

It was immense and powerful.

Even without checking his Level, I could tell the gap between him and the Team 1 Leader.

“You say you don’t understand. What does that mean?”

“How someone strong enough to chew up that Team Leader lying over there with one hand isn’t even a deputy team leader, but merely an ordinary Hunter.”

“……!”

“And he shows up for work so rarely that he might come in once a month. From the conversation I overheard between you and the Team 1 Leader, you were practically his superior.”

There were more than one or two things that seemed suspicious.

And as I spoke with them today, my suspicions gradually became certainty.

“Amazing conditions are being exchanged, yet the highest person in charge stays silent while the one doing all the talking is an ordinary team member with no position at all…… How am I supposed to take that, Guild Master Park Tae Seop?”

Myeongdong Guild Master Park Tae Seop met my gaze and slowly closed his eyes.

That was a fine enough answer.

I let out a quiet laugh and looked at Park Jihoon.

“So bring that person here. I don’t know who it is, but bring them here and make them apologize first.”

Park Jihoon’s tightly sealed lips parted.

“And if I refuse?”

“Then we go all the way.”

“You crazy bastard. Do you even know who that person is?”

“No. I don’t particularly want to know, either. But I do want to see that bastard come here, slam his head down, and apologize. Then I’ll be satisfied.”

Swish!

At the same time, I thrust out my hand at blinding speed.

Park Jihoon cried out in alarm.

“You little bastard!”

Pap-pap-pap!

In an instant, his hand collided with mine and became entangled.

Five exchanges passed in the blink of an eye.

Crunch.

His wrist broke, and his eyes widened.

I grabbed his hair, meticulously styled with wax, and slammed his head down toward the table.

Bang!

“Like this.”

[^1]: Melona is a popular Korean melon-flavored ice cream bar.
## Chapter artifact 283

# Chapter 283

BANG!

The air in the office rang with a sharp vibration.

Park Jihoon’s forehead smashed through the table and slammed into the floor. With a sharp crack, spiderweb-like fractures spread across the ground.

“Guh.”

I pressed my knee into his back, using the principles of the Thousand-Catty Drop.

My eyes, fixed on the back of his head, were filled with surprise.

*Huh. Look at this bastard.*

Modern Hunters had no concept of martial arts.

Even among close-combat types, it was extremely rare to find someone like Im Yeongjun, a Black Hunter who focused primarily on hand-to-hand combat. Most concentrated on weapons.

*Because that was the better way to improve their survival rate.*

But Park Jihoon was different. Even though it had lasted only a moment, the movement he had shown was comparable to that of a Peak master from the Murim.

*It was a little clumsy, but it was almost like a grappling technique wielded by someone who had reached a higher realm.*

I had underestimated him and been caught off guard. The fight had ended almost immediately, but the fact that he had exchanged moves with me five times already put his ability far beyond what I had expected.

*Has this level of hand-to-hand combat survived into the modern era? Why hasn’t anyone heard of it?*

I asked aloud, unable to suppress my curiosity.

“You. Where did you learn that just now?”

Park Jihoon answered in a strained voice.

“Let go right now, before you regret it.”

“I see. Still full of energy, are you?”

BANG! BANG! BANG!

Once. Twice. Three times.

Every time I grabbed his hair and slammed his head down, a muffled groan escaped him. Blood spattered across the office floor, which had been spotless only moments ago.

As his body went limp, Park Tae Seop, who had been observing the situation, suddenly spoke.

“That’s enough.”

“Is this bastard the Guild Master’s son?”

“Would he be my son?”

“Then is he your daughter?”

“Obviously not that, either.”

“Then this isn’t a matter for the Guild Master to interfere in. If you cross the line here, I can’t guarantee what I’ll do, either.”

Park Tae Seop’s eyebrow twitched.

“You’ve got quite a spicy tongue.”

“My hands are even spicier. My old nickname was the Haengsin-dong Fire-Chicken Stir-Fried Hand.[^1]… Want a taste?”

“I have a reputation to uphold. I have no intention of fighting a young man as green as you.”

Park Tae Seop uncrossed his arms and continued.

“But if that fellow is seriously injured, it will put me in a difficult position. He’s an important business partner.”

“He’s a manager sent by your business partner, right? No, seeing how you’re being pushed around, it’s embarrassing to even call him a business partner. You’re practically a figurehead. Does he have something on you?”

I must have struck a nerve, because he deliberately furrowed his brow.

“You’re more perceptive than I expected. Though I heard you weren’t very bright.”

I didn’t need to ask which bastard had said that.

I grabbed Park Jihoon’s wax-stiffened hair even more roughly and answered.

“I’m a slow learner. But once I learn something, I don’t forget it.”

“He learned his lesson properly this time, so let him go now.”

“I was planning to do that anyway.”

As I lifted Park Jihoon by the hair, Park Tae Seop gave a small nod.

“Good thinking.…”

I drove the fistful of hair back down with all my strength.

BANG!

*One more time.*

CRACK!

The floor shattered beneath the deafening impact. I drove my toe into the solar plexus of the man flopping around like a raw fish.

With a thud, Park Jihoon flew backward and slid all the way to the door.

“Ghk!”

The impact jolted him awake. He trembled violently and spat out a mouthful of blood.

“……”

Park Tae Seop was unable to continue speaking, so I addressed him.

“I let him go. There. Happy?”

“You…… You’re quite something.”

“Am I really as bad as the bastard who cuts people’s arms off and calls it a warning?”

“I don’t particularly like that fellow myself, but you would’ve been better off taking my advice.”

His expression and voice had turned rigid.

He was sincere.

Rather than feeling afraid, I became curious. Who was this person that even Park Tae Seop—a war hero of the Great Cataclysm and one of Korea’s top rankers—was wary of?

I asked with a questioning look.

“Who is it? That bastard only called him ‘that person.’”

“I can’t tell you. Even if I did, you’d only resent me later.”

“Why make such a big deal out of it? Is that person Asmodeus or something?”

“If you made him your enemy, it would be better if he were the Demon King. At least the whole world would fight alongside you.… But what are you doing right now?”

Park Tae Seop stared at me with his eyes wide.

Or, to be precise, he was staring at the phone in my hand.

“I’m looking at this phone.”

“Suddenly?”

“Yes.”

He had the exact expression of a man wondering what kind of lunatic he was dealing with.

Park Tae Seop asked, unable to understand me at all.

“What are you doing with that?”

“What do you think? Since you won’t tell me, I’m trying to find the number myself.”

“The number?”

“Yes. That person’s number.”

“Wait. Is that…?”

“That’s right. I took it from that bastard’s pocket earlier.”

Park Tae Seop’s eyes widened. Park Jihoon, who had been coughing up blood, shouted as though he had forgotten his pain.

“Give it back right now!”

“Yeah, I can’t give it back.”

I toyed with the mysterious phone, whose make I couldn’t identify.

It looked completely different from the phone I had seen when I visited his officetel last time. There was no way he had changed it in the past few days, so it was probably a separate phone he kept for secret communications.

It wasn’t strange. Even people who secretly cheated on their partners carried two or three phones.

*He has so many secrets, after all.*

When I touched the screen, two messages appeared alongside a lock icon. They were asking for fingerprint and iris recognition.

I could understand the fingerprint part, but what the hell was with the iris scan?

I gestured toward Park Jihoon, who was staggering to his feet.

“Hey. Come here. Put your fingerprint and iris against it.”

“Jin Taekyung, you crazy bastard. Do you even know what you’re doing?”

“Yeah, I know. So get over here and press an eye and a finger against it before I rip them out.”

“Don’t rush me. I was planning to do that even without you telling me.”

Park Jihoon ground his teeth with a crunch and wiped at the corner of his mouth.

But unlike before, when he had been gasping for breath, he now seemed overflowing with strength.

Aside from the blood covering him here and there, his cracked forehead and broken nose had already healed completely. His stamina was as good as new.

Only then did I notice a small reinforced-glass vial rolling around by his feet.

“A potion?”

“When there’s an enemy in front of you, never let your attention wander until the very end. Didn’t they teach you that at the training center?”

He must have taken out the hidden potion and gulped it down during the brief moment I was looking at my phone. I shrugged.

“That only applies when the two sides are evenly matched. That’s not the case here, is it?”

“What?”

“I don’t know where or from whom you learned whatever you learned.…”

As I circulated my qi according to the formula of the Fire Gate Divine Technique, the fire dragon coiled within my dantian awakened.

I fixed Park Jihoon with reddish, glowing eyes.

“You and I are in different classes, you fucking scrub.”

The next moment, the fire dragon formed from a jiazi’s worth of Scorching Yang Qi scattered into hundreds of streams. As they dispersed, they awakened my acupoints and raced forward without restraint.

The internal energy converged again at a single destination and merged into one.

*Disperse, compress. And…*

*Release.*

WHOOSH!

The weather had already turned toward early winter. Yet the once-cold office transformed into the sweltering heat of midsummer beneath a blazing sun. An enormous burst of fiery qi erupted in an instant and surged through the room.

“Hah.”

I exhaled a breath of scorching air.

Beyond the wavering heat haze, I saw a man whose face was filled with shock. His expression had gone rigid, and turbulent waves churned in his eyes.

“You, you……”

A groan-like voice slipped between Park Jihoon’s lips.

“How?”

“I told you. We’re different.”

As though someone had thrown ice water over him, he trembled and bit down on his lip. He bit so hard that the flesh split at once, and blood began to flow.

“This, this is impossible. How could you.…?”

The man muttered with a twisted expression, then abruptly opened his mouth.

“I’m going to need your help, Guild Master.”

There was no question who he was speaking to.

Park Tae Seop, Guild Master of Myeongdong Guild, had been watching me with astonishment. He answered in a heavy voice.

“Is there even a way to refuse that proposal?”

“No.”

“And if I refuse anyway?”

“Definite rewards and punishments according to your choice. You must know how ‘that person’ operates, Guild Master.”

“……I’m sick to death of this.”

Park Tae Seop sighed and pulled a sixty-centimeter-long rod from his waist. When he stroked the Magic Gem attached to its end, a snow-white blade surged upward.

Hssssss!

“Don’t blame me.”

With that bitter remark, he pointed the tip of the sword at me, the blade engulfed in a blue aura.

My opponent was a hero of the Great Cataclysm and one of Korea’s top ten rankers. A massive aura rose from his body and confronted my Scorching Yang Qi.

With a powerful ally at his side, Park Jihoon smiled coldly.

“You’re finished.”

“Finished?”

I laughed aloud.

Since I had heard he went to Hankuk University, I had assumed he was at least somewhat smart. But it seemed he had completely forgotten what I told him last time.

“I’m the one who decides whether this ends, you fucking idiot.”

Park Jihoon had forced me onto the starting line and pulled the trigger to signal the beginning of the race. But he had failed to anticipate the most important thing.

That this race had no finish line.

And that wherever I stopped was the finish line.

*Open Inventory.*

Summon White Flame.

FWOOSH!

I stepped forward amid the flames.

Blue fire streamed along the spearhead, scorching everything around it as it surged toward the enemy.

* * *

“Haah!”

With a powerful battle cry, a massive greatsword came flying at me. The blue aura gathered at its tip was denser and longer than anything I had ever seen in reality.

*As expected of one of Korea’s top rankers.*

Internal energy and mana.

Their names were different, but their essence was the same. In that sense, the energy Park Tae Seop possessed exceeded mine.

But.…

*That’s all.*

I sprang upward.

My hair narrowly grazed the ceiling, while the blade sweeping across my waist cut through empty air.

WHOOM! CLANG-CLANG-CLANG!

The massive pressure wave swept everything away. The reinforced glass covering one side of the office shattered and fell toward the ground.

Before the screams from below could reach me, I brought the spearhead down toward the crown of Park Tae Seop’s head.

WHOOSH! BANG!

With a deafening roar, Park Tae Seop’s knee struck the floor.

His eyes widened in shock as he hurriedly blocked the attack with the shield in his other hand.

“What is this?”

By now, he must have been feeling the crushing pressure of a boulder weighing ten thousand geun.

It was the difference in our physical abilities, as well as the gap created by the way we used our energy.

*Hunters really aren’t very efficient.*

In contrast, Murim cultivation techniques explosively increased the efficiency of internal energy. That was why renowned great powers like the Nine Sects and One Gang and the Five Great Families were so strong.

The various martial arts built around excellent cultivation techniques—

when those small gears meshed together with precision, they could finally be called a divine technique.

*Disperse, compress, release.*

Internal energy was like a scarce resource. You had to draw it out when absolutely necessary and find the best possible use for it.… Even Park Tae Seop, one of Korea’s top rankers, had not completely escaped those limitations.

BANG! BANG! BOOM!

After blocking a total of four attacks, Park Tae Seop’s shield split in half. At that moment, a flash shot toward my side.

“Die!”

The owner of the thin, sharp rapier was obviously Park Jihoon.

Just as I thought I had avoided it, the aura clinging to the tip of the blade surged out even farther and grazed my side.

SIZZLE!

Disappointment flashed across Park Jihoon’s face.

His aura had only cut through my clothes and passed by.

I checked my uninjured side and licked my lips.

“……This is pretty interesting.”

“Interesting? You’re not afraid?”

“Did the guy you call ‘that person’ or whatever teach you?”

“Shut your mouth. You’re not worthy of even speaking of that person.”

“Huh. So I was right. This isn’t some kind of cult, is it?”

“You son of a—!”

WHOOM! SHH-SHH-SHHK!

Park Tae Seop’s greatsword came from the right, while Park Jihoon’s rapier flew in from the left.

As I watched the two men tear through the space between us, I thrust out both arms.

BANG! BOOM!

I blocked Park Tae Seop’s greatsword with White Flame and Park Jihoon’s rapier with the dagger I had just summoned, then smoothly rotated my wrists.

KRRRANG!

The four blades locked together and tangled around one another.

I remembered my duel with Sword Saint Mae Jonghak.

His sword that let everything flow past.

His movements.

And I put them into practice.

*Flow.*

Sliiide.

The spearhead and dagger slipped like snakes. Neither the massive greatsword nor the slender rapier could block their path.

Before long, the two keen-edged weapons touched the men’s throats.

Swish.

“Drop your weapons.”

“……!”

“……!”

Two shocked gazes turned toward me.

Park Jihoon spoke in a voice filled with rage and despair.

“How could you……?”

“You didn’t hear me, did you?”

CRACK!

There was no hesitation.

I raised my foot and drove it down onto his knee. The cartilage shattered, and a scream burst from him.

“Aaaaargh!”

“We’re down two arms on our side. One leg doesn’t balance the books.”

I was about to crush his one remaining knee when—

“I think that should be enough.”

An unfamiliar voice bored into my ears.

The voice was impossibly deep and low. A chill ran down my spine, and the fine hairs on my body stood on end.

This was……

*A Supreme Peak master?*

[^1]: Buldak-bokkeum-myeon literally means “fire-chicken stir-fried noodles”; the nickname replaces myeon (“noodles”) with son (“hand”).
## Chapter artifact 284

# Chapter 284

“I think that’s enough.”

It was completely unexpected.

The voice from behind me sent a chill through my mind, as though someone had dumped ice water over my head.

*When did he get there?*

I hadn’t sensed his presence. Even taking into account the fact that I had been in the middle of a fight, that should have been impossible.

If he had managed to evade my senses, which were at the very edge of Peak, then there was only one answer.

*A Supreme Peak master.*

I turned around slowly. Amid the rubble of the wall that had collapsed in the aftermath of the battle, a man was staring at me.

“Nice to meet you.”

He was a middle-aged man who looked to be in his early forties. He had bold features that looked as though they had been painted with a brush, and a solid build that even his clothes couldn’t conceal.

And…

*He’s strong.*

The moment I sensed the qi coiled within his body, my heart sank. At the same time, all the experience I had accumulated and my keenly honed senses whispered to me.

The middle-aged man before me was a Supreme Peak master I could not possibly handle in my current state.

“Young man, you’ve got good instincts. Better than I expected.”

The middle-aged man looked me over with interest, then suddenly tilted his head.

“Or is it because you know my face?”

“Both.”

The shock brought on by the middle-aged man’s appearance was immense.

I tried my best to look calm, but I couldn’t hide my cracking voice or trembling eyes.

“Well, it’s not as if my face has only been plastered around once or twice.”

The middle-aged man nodded as though it were nothing important, then strode forward.

He crossed the wrecked office and extended a hand for a handshake.

“Nice to meet you. I’m Lee Jungryong.”

A short, simple introduction.

But the meaning and influence carried by the three syllables of Lee Jungryong’s name were neither short nor simple.

He was the kind of person who could use his face and name as identification anywhere in the world, not just in Korea.

*The second-in-command of Ares Guild. And one of the two S-rank Hunters Korea possesses.*

That was Lee Jungryong.

A powerful man who wielded absolute authority over Ares Guild in place of its Guild Master, the other S-rank Hunter.

Ares Guild was said to rank among the top five Guilds in the entire world. Their influence over Hunters was tremendous, to say nothing of politics and the economy.

People even said that Korea had two Blue Houses.

Why had such a major figure appeared here of all places, right now?

*Fuck. It’s obvious.*

Suddenly, the conversation I’d had with Park Tae Seop flashed through my mind.

*Who is he? That bastard earlier only called him “that person.”*

*I can’t tell you. Even if I did, you’d only resent me later.*

*Why make such a big deal out of it? Is that person Asmodeus or something?*

*If you made him your enemy, it would be better if he were the Demon King. At least the whole world would fight alongside you.*

The answer had already emerged in my mind.

If the “that person” Park Jihoon had mentioned was Lee Jungryong, and Ares Guild was behind this whole affair, then everything fit together perfectly.

*This is turning into a real goddamn mess.*

The unexpected appearance of such a major figure chilled my blood.

Unlike me, who had gone rigid, Lee Jungryong smiled gently and spoke.

“I’ve heard a great deal about you. You look much better in person than you do on television.”

“Thank you.”

“You don’t look happy to see me at all.”

“How could that be? You’re an S-rank Hunter recognized throughout the world.”

“It’s only a false reputation. I’m nowhere near the Guild Master. Anyway…”

With his characteristic smile, Lee Jungryong opened and closed his empty hand in the air.

“When are you planning to accept my handshake? I’m starting to feel embarrassed.”

As I listened to his good-natured smile and his soft words delivered like a joke, I thought:

*This man has at least a hundred snakes in his stomach.*

And I hated snakes.

“I’m sorry, but I don’t have a hand free right now.”

“Is that really a problem? Just put down whatever you’re holding and it’ll be easily resolved.”

“I can’t let go of an issue that needs to be resolved just to shake hands.”

I tightened my grip on the weapons in each of my hands.

Swish.

With a faint sound, thin lines of blood appeared across the throats of Park Tae Seop and Park Jihoon.

The two men had closed their eyes and pressed their lips tightly together the moment Lee Jungryong appeared. Even so, I could sense something like resolve from them.

“I understand the two of you are quite close. Why don’t you at least say hello?”

“Close? Me?”

Lee Jungryong let out a hearty laugh.

“I’ve known Guild Master Park since the Great Cataclysm, so we’re at least acquainted. Isn’t that right?”

Park Tae Seop, Guild Master of Myeongdong Guild, bit his lip and answered.

“It’s been a long time, Vice Guild Master Lee Jungryong.”

“Yes. It has. But what happened here?”

“There was an unpleasant incident… I’m sorry you had to see me in such a sorry state.”

“I don’t know what sort of misunderstanding there is, but these things can be settled through conversation. And who is that young man beside you?”

“He’s a member of my Guild. He’s been with us ever since he completed his training center course.”

Park Jihoon spoke in a trembling voice.

“Nice to meet you. I’m Park Jihoon from Team 1 of Myeongdong Guild.”

“……!”

I wasn’t surprised by the way Lee Jungryong spoke down to Park Tae Seop despite looking at least ten years younger than him.

I was surprised by their shamelessness.

Everyone here knew that Lee Jungryong was the one who had given Park Jihoon his initial orders.

Yet the conversation between those three men meant only one thing.

*The lizard’s tail.*

An old lizard who had already prepared to cut off its tail smiled gently as he looked at me.

“See? That young man is a complete stranger to me. And I only exchange occasional greetings with Guild Master Park.”

I let out a hollow laugh and asked,

“By ‘exchanging greetings,’ do you mean secretly sending Black Hunters to cut off the arm of some innocent person?”

“Black Hunters? Stop it. Your delusions are getting out of hand. Anyway, regarding the matter involving Guild Master Park…”

He shook his head and continued.

“I think I may be able to offer a little help with that problem.”

“Help?”

“Yes, help. We have to resolve the problem, don’t we?”

My earlier thought had been only half right. The lizard wasn’t planning to cut off its tail yet. He wanted to clean up the mess.

Lee Jungryong and I stared at each other across the room. A bead of cold sweat that had formed at some point trickled down my neck.

This was both an offer and a warning: let these men go.

But…

“It’s a personal matter, so I don’t think that’ll be possible.”

Whether I stopped here or kept going was up to me.

I had already made my decision.

“Hmm? Ha ha.”

Lee Jungryong laughed aloud and looked at me with amusement.

“Young man, you’ve got quite a bit of grit. And plenty of spirit.”

“I do hear that fairly often.”

“What about being called arrogant?”

“I hear that even more.”

“Young men full of spirit are often misunderstood.”

“I think so too.”

“Yes. I’m glad to hear that, but…”

An unreadable light flashed in Lee Jungryong’s eyes.

“Don’t you think it’s time for you to change as well?”

“What do you mean?”

“You’re a famous person known throughout the world, and you’re approaching thirty. I’m saying it would be better to avoid those sorts of misunderstandings.”

“Thank you for the advice, but I’m not planning to do that yet.”

“Why not?”

“Because the people who say things like that to me are always fucking idiots who’ve done nothing but pile on years. If a few neighborhood mutts are blocking the road, there’s no reason to run away.”

“It wouldn’t be pleasant to get bitten by a vicious dog.”

“No matter how vicious a dog is, it’s still a dog. No offense, but I consider myself at least a wolf.”

“A wolf… Then what would you do if it wasn’t a dog blocking the road, but a tiger?”

The corners of Lee Jungryong’s mouth curved gently upward.

He was the tiger.

A tiger blocking my path. A beast with teeth and claws capable of killing a wolf.

“I’d run. A wolf can’t beat a tiger.”

“That’s right.”

“But if I added a few details to the setup, I might be able to take it on.”

“Details?”

“Yes. For example…”

I continued slowly as I looked at Lee Jungryong.

“If that tiger were the one who seriously injured my friend. Something like that.”

He stared at me with a peculiar expression.

“It seems the wolf’s friend was badly hurt.”

“Both his legs were cut off. How could he not be? And he has young children.”

“That’s an awfully detailed setup.”

“I came up with it while thinking of a plausible setup. It’s just a setup, so don’t worry about it.”

“If that’s all it is.”

Lee Jungryong shrugged.

“Still, a wolf taking on a tiger for his friend… That’s quite loyal of him.”

“You’d know if you watched a documentary about wolves. They take loyalty very seriously.”

“But it would be reckless.”

“Why is that?”

“Because if you challenged a tiger, you’d die.”

I answered with a quiet laugh.

“You never know. Maybe a young, strong wolf could beat an old tiger.”

“……A tiger losing to a wolf? From the sound of it, that doesn’t seem like a very well-made documentary.”

“I enjoyed it. The part where every animal in the mountains came rushing over to feast on the tiger’s corpse after the wolf won was especially memorable.”

“……”

For the first time, the smile disappeared from Lee Jungryong’s face.

It was only natural. He had understood the meaning hidden in my words.

When I saw his face stiffen, I felt as though the formula I’d been fed as a baby had finally started to go down.

“You’re irritating. More than I expected.”

After a brief silence, he spoke again.

Lee Jungryong slowly withdrew the hand he had kept extended until then.

“What do you want?”

I answered without hesitation.

“An apology and compensation. And one person’s life.”

“His life?”

“Yes. I want one person’s life.”

Park Jihoon’s neck twitched.

A tremor traveled through the dagger pressed against his throat. Since Lee Jungryong’s appearance, he hadn’t made a single sound, but now he was trembling with fear of death.

“That’s not possible. I can’t allow it.”

“You’re not allowing anything. I’m making a demand.”

“Learn to distinguish courage from recklessness. I’m a patient man, but I’m also quite fickle.”

“I’m a man lacking in basic decency, so I can’t rest until I repay at least what I received.”

“Your demand is excessive. Haven’t you already received more than enough compensation?”

“Who only collects the principal? I’m taking the interest too—and the compound interest.”

“And if I refuse?”

“Do you remember that documentary I mentioned earlier?”

“……!”

“Tiger hide or not, do you really think a wolf’s teeth won’t sink into it?”

Lee Jungryong’s gaze sank heavily as he looked at me.

In the strangely tranquil silence, his mouth slowly opened.

“You really don’t know how frightening a tiger can be.”

Whoosh!

Before he had even finished speaking, a palm wrapped in a red aura shot toward my chest.

Only five steps separated us. I made my decision in an instant.

*White Flame. Unequip.*

As White Flame was stored in my Inventory, I thrust out my freed right hand.

Disperse, compress, release.

The fire dragon that had been waiting impatiently to awaken transformed into blue flames and took shelter in my palm.

Flame Divine Palm with everything I had.

And then we collided.

BOOOOOOM!

The entire building shook as though an earthquake had struck, accompanied by a deafening roar that left my ears ringing.

I was the one who felt the impact most severely.

I staggered back three steps as if dancing, then spat out a mouthful of blood that surged up from deep within my lungs.

“Cough!”

Through the pale dust falling from the ceiling, I saw Lee Jungryong standing firmly in place.

“You…”

His eyes were filled with surprise. But I was just as surprised.

I had felt a method of manipulating qi that was impossible to experience in the modern world.

*He’s different. He’s not an ordinary Hunter.*

It had been only a single exchange.

But I knew.

Lee Jungryong’s strike had been close to the palm technique of a Supreme Peak master. He didn’t merely know how to wield his qi properly—he was capable of far more than that.

*So this is an S-rank Hunter.*

The power I had felt for that brief moment was comparable to that of the great demon, the Yin-Yang Twin Devils, whom I had encountered at Shaolin.

*What kind of monster is this?*

I hadn’t expected to have an experience like this in the modern world.

Lee Jungryong’s eyes were wide as he looked at me, swallowing blood while holding Park Jihoon in one hand and a dagger in the other.

“How could someone as young as you know that method…?”

*That method?*

He was probably referring to an internal energy cultivation technique in those terms.

I was about to answer, but instead I grinned, baring my bloodstained teeth.

“I’m taking what I demanded.”

At the same time, I drove the dagger into Park Jihoon’s chest.

Thud. Thud-thud-thud!

A scream burst from his mouth along with a spray of blood.

“Aaaaargh! Master!”

I’d wondered how this bastard knew about it. Now I saw—they were master and Disciple.

“Stop!”

Even as he shouted, Lee Jungryong couldn’t easily take a step forward.

That was because every time he did, I pressed the dagger right against Park Jihoon’s throat.

“Now, now. If you want to save your adorable Disciple, you’d better stay right there.”

“……!”

Thud. Squelch!

Without hesitation, I brought the dagger down again and again. I hacked at his upper body indiscriminately, avoiding his heart, then tore through the muscle of his thigh.

Slash!

I cut down along his calf and severed the tendons in his ankle. Then I straightened my back, which I had briefly bent, and slashed diagonally upward through his shoulder.

Slash, shraaak!

“Aaaaaaargh!”

It was a horrible scream.

Uncle Kkeokjeong must have screamed like this, too. He must have fainted and woken up several times from the unbearable pain, screaming each time.

And that wasn’t all. The wife who saw her husband return without both arms had her heart butchered as well.

“Save your screams. There’s still one more left.”

“……!”

Slash! Thud!

Park Jihoon’s body, now missing both arms, trembled violently.

“Ghk, guh…”

He must have screamed so much that his throat had gone completely hoarse. Strange sounds slipped from it.

I grabbed him by the hair. His neatly waxed hair was drenched in blood.

“P-please… save me…”

My blood was boiling more fiercely than ever, but the voice that escaped between my lips was colder than ice.

“Jihoon.”

“Please. I’m sorry…”

“I couldn’t say this back then because I had to move in a hurry.”

I looked into his bloodshot eyes and delivered a congratulatory message ten years past its expiration date.

“Congratulations on graduating, you fucking bastard.”

I threw him down with all my strength.

Thud.

Lee Jungryong picked up the sprawled man in his arms. His eyes burned fiercely.

“You bastard!”

“I left him alive. I can’t promise anything about his life as a Hunter, though.”

“Do you really want to die?”

“How about we take this a little further? Bring the whole building down and let half the people in Korea hear about what happened here. That doesn’t sound so bad to me.”

Lee Jungryong’s face twisted into a ghastly expression.

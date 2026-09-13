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

## Chapter 374 Expedition

- This branch intentionally starts at Chapter 374. Chapters 65–370 have no accepted local English translation here; Chapters 371–373 are source-only bridge summaries.
- Treat `docs/EXPEDITION_SEED.md` and `summaries/0369-0373.md` as bounded orientation, not as a substitute for missing translations.
- When the current Korean source conflicts with bridge context, the current source wins. Preserve uncertainty instead of inventing skipped-range backstory.
- From Chapter 374 onward, the ordinary workflow update, names ledger, profiles, summaries, QA, hashes, and mastering artifacts are authoritative for this branch.

## Checkpoint summary

# Chapters 370–374

## Plot

Chapter 370 is intentionally skipped; no accepted English translation or plot details are asserted.

In Chapter 371, Taekyung is celebrated as the Flame Divine Dragon after reaching the Supreme Peak realm. The Qingcheng and Emei Sect Leaders ask him and Jeok Cheongang to investigate a strange Dark Heaven-related formation identified by Samgoe. Taekyung encounters Mungyeong and learns that the physician is secretly the Slaughter Saint.

The group enters a cave hidden by a phantom formation in Chapter 372. It contains supplies, weapons, and a huge inactive transport formation apparently capable of moving people over great distances. Its patterns are not writing, and its origin and purpose remain unclear. Slaughter Saint suggests Dark Heaven succeeded the Demonic Cult, while Taekyung senses something familiar about the formation.

Slaughter Saint decides to resume living as Mungyeong. Back at the Sichuan Tang Clan, Taekyung processes accumulated System messages, reaches Level 120, and discovers that the previously unnamed Inventory item is bound to him and summonable in either world. An investigative party from Henan arrives.

In Chapter 374, Jin Wikyung urges acting Family Head Tang Horyong to relocate the devastated Sichuan Tang Clan to Henan, Shaanxi, or Shanxi, promising orthodox Murim support as a larger war approaches. Horyong does not decide. Wikyung prepares to escort Samgoe to Henan, but Tang Sadok awakens after his long coma, delaying their departure. Taekyung identifies the bound item as the Myriad Poison Ring and expects to return to his original world soon.

## Continuity

- Chapter 370 remains a source-only gap; later references across it must be checked against the current Korean source.
- Taekyung is at the Supreme Peak realm and Level 120. His exact Fame, titles, martial-art stages, and unassigned points after the skipped range are not established here.
- Slaughter Saint is secretly living as Mungyeong and intends to leave Murim after intervening in the crisis.
- The inactive Dark Heaven-associated transport formation remains unexplained. Its origin, destination, mechanism, and connection to Dark Heaven are unresolved.
- Dark Heaven’s agents, larger purpose, and connection to the Demonic Cult remain unresolved.
- The Sichuan Tang Clan, Qingcheng Sect, and Emei Sect were devastated by Dark Heaven. Tang Horyong remains acting Family Head; Tang Sadok, the Poison King, has awakened.
- Jin Wikyung is the Lesser Family Head of the Jin Family of Taiyuan, leader of unified Shanxi Murim, and the assigned escort for Samgoe. He has offered the Tang Clan relocation and orthodox support.
- Orthodox Murim is preparing a new Murim Alliance after Mae Jonghak’s warning of a war greater than the Great Faction War.
- Samgoe remains under guard and is being taken toward Henan; the escort’s outcome and timing are unresolved.
- The Sichuan Tang Clan’s relocation decision and destination are unresolved.
- Taekyung’s return to his original world is imminent; roughly six hours have passed there while about two months passed in Murim.
- The previously unnamed bound Inventory item is the Myriad Poison Ring.
- The outcome of Taekyung’s spar with Jin Mukyung remains unresolved in the accepted earlier anchor.

## Translation Decisions

- Preserve **Flame Divine Dragon**, **Supreme Peak**, **Dark Heaven**, **Slaughter Saint**, **Mungyeong**, **Myriad Poison Ring**, **Sichuan Tang Clan**, **Qingcheng Sect**, **Emei Sect**, **Henan**, **Shaanxi**, and **Shanxi**.
- Preserve uncertainty around the transport formation; do not treat its patterns as writing or assert an origin, destination, or confirmed mechanism beyond its apparent transport function.
- Render **반 시진** and **한 시진** as **half a shichen** and **one shichen**, with a footnote explaining that a shichen is a traditional two-hour period.
- Render **종형** as **older cousin** in the Tang family context.
- Treat Chapters 371–373 as source-only bridge summaries, not complete accepted English translations.

## Durable state

{
  "active_continuity": [
    "By the end of the source-only bridge, Jin Taekyung has reached the Supreme Peak realm and Level 120; exact current Fame, titles, martial-art stages, and unassigned points must be taken from the current Korean source rather than inferred across the skipped range.",
    "Jin Mukyung is Taekyung's second older brother, twenty-three, the Heaven Shaking Sword, a Peak-level martial genius, and substantially stronger than Taekyung.",
    "Dark Heaven rescued the former conspirators from the Demonic Cult, implanted gu in them, and its larger purpose and reason for sparing Taekyung remain unresolved.",
    "The Sichuan Tang Clan, Qingcheng Sect, and Emei Sect were devastated by the recent Dark Heaven attacks; Tang Sadok has awakened, and Tang Horyong remains acting Family Head.",
    "Slaughter Saint is concealing his identity as the young physician Mungyeong and intends to leave Murim after intervening in the recent crisis.",
    "A hidden, currently inactive transport formation associated with Dark Heaven was found near Sichuan; its origin and function remain unresolved.",
    "Jin Wikyung has proposed relocating the Sichuan Tang Clan and has been assigned to escort Samgoe toward Henan.",
    "Taekyung's return to his original world is imminent, with roughly six hours having passed there.",
    "The previously unnamed Inventory-bound item is the Myriad Poison Ring."
  ],
  "continuity_sources": [
    374
  ],
  "open_questions": [
    "The outcome of Taekyung's spar with Jin Mukyung remains unresolved in the accepted local anchor.",
    "Dark Heaven's agents, purpose, and connection to the transport formation remain unresolved.",
    "The Sichuan Tang Clan's relocation decision and destination remain unresolved.",
    "The outcome and timing of the planned Samgoe escort to Henan remain unresolved."
  ],
  "safe_through": 374,
  "temporary_decisions": [
    "This expedition deliberately skips accepted translation of Chapters 65–370.",
    "Chapters 371–373 are source-only bridge summaries and must not be treated as complete English continuity.",
    "When bridge context conflicts with the current Korean source, preserve the current source and record the uncertainty.",
    "Use Reformation Fist for 갱생권, grappling technique for 금나수, and retain hyung for 형 where the accepted anchor requires them.",
    "Render 반 시진 and 한 시진 as half a shichen and one shichen, with a footnote explaining that a shichen is a traditional two-hour period.",
    "Render 종형 as older cousin in this chapter's family context."
  ],
  "version": 1
}

## Reading copies

## Source-only bridge artifact 370

# Chapter 370

## Plot

Chapter 370 is intentionally skipped in this expedition and has no accepted
local English translation. No plot details are asserted here.

## Continuity

- This source-only boundary must not be treated as an English translation or
  as evidence for facts not established by the bounded bridge dossier.
- The current Korean source remains authoritative when later chapters refer
  back across the skipped range.

## Translation Decisions

- Source-only gap marker; do not invent a translation, terminology, or plot
  summary for this chapter.
## Source-only bridge artifact 371

# Chapter 371

## Plot

Taekyung is publicly hailed as the Flame Divine Dragon after reaching the Supreme Peak realm. Jeok Cheongang privately celebrates his growth. The Qingcheng and Emei Sect Leaders ask Taekyung and Jeok Cheongang to investigate a strange Dark Heaven-related formation revealed by Samgoe. Taekyung encounters Mungyeong on the way and discovers that the physician is actually Slaughter Saint.

## Continuity

- Slaughter Saint is Mungyeong's hidden identity.
- A Dark Heaven-related formation is under investigation.

## Translation Decisions

- Source-only bridge summary; do not treat as an accepted English translation.
## Source-only bridge artifact 372

# Chapter 372

## Plot

The group enters a hidden cave concealed by a phantom formation. The cave contains supplies, weapons, and a huge inactive formation that Samgoe identified as a transport formation capable of moving people across great distances. The patterns are not interpreted as writing. Slaughter Saint says Dark Heaven is likely a successor of the Demonic Cult, while Taekyung suspects he recognizes something about the formation.

## Continuity

- The transport formation is inactive and its origin and purpose remain unresolved.
- Dark Heaven's connection to the Demonic Cult remains an active explanation, not a fully resolved history.

## Translation Decisions

- Source-only bridge summary; preserve uncertainty around the formation's mechanism.
## Source-only bridge artifact 373

# Chapter 373

## Plot

Slaughter Saint says he will return to living as Mungyeong, the young physician, after intervening in the crisis. Taekyung returns to the Sichuan Tang Clan, checks a backlog of System messages, reaches Level 120, and learns that a new unnamed item has become bound to him and can be summoned through his Inventory in either world. Hyuk Mujin announces that an investigative party from Henan has arrived.

## Continuity

- Mungyeong's Slaughter Saint identity is known only to the people present at the recent confrontation.
- Taekyung has an unnamed newly bound Inventory item.
- An investigative party from Henan is seeking Taekyung at the Chapter 374 opening.

## Translation Decisions

- Source-only bridge summary; do not infer skipped-range terminology or plot details.
## Chapter artifact 374

# Chapter 374

Tang Horyong, the Pavilion Master of the Poison Dragon Pavilion, rose from his seat to greet his guest.

An imposing man had just opened the door and entered, and an indescribable aura poured from him.

“You’ve gone to a great deal of trouble coming such a long way.”

“Compared to what the Sichuan Tang Clan has endured, it was nothing. Once again, please accept my deepest condolences.”

Despite his rough features, the man’s voice was low and gentle. At the same time, it possessed a force that made anyone who heard it pay close attention.

*Could it be the aura possessed only by a leader who commands others?*

At the man’s gentle yet deeply composed gaze, Tang Horyong suddenly thought of someone.

*This feels like meeting another older cousin.*

The realization left Tang Horyong more than a little bewildered.

He had heard that the man standing before him was still a young man who had yet to reach forty.

His older cousin, on the other hand, was considerably older and held an eminent position in Murim.

He had achieved countless military feats during the Great Faction War and was also an iron-blooded Family Head who had rebuilt his ruined family on an even stronger foundation.

The Myriad-Poison Asura, Tang Sadok.

Tang Horyong, acting Family Head of the Sichuan Tang Clan, let out a silent sigh as he thought of his older cousin, who still had not regained consciousness.

*Please wake up soon and lead us, Family Head.*

Tang Horyong had been born a martial artist.

He prided himself on having made himself an authority in poisons and hidden weapons, but leading a family was an entirely different matter.

Especially lately, so many issues had been pouring in from every direction that he had not even had time to dwell on the grief and anger of losing his family members.

*If only someone like this man were in my position.*

In that sense, Tang Horyong could not help but envy the man before him.

He was not judging him solely by his first impression. He had already heard plenty of rumors about the man.

Even if only a quarter of those rumors were true, the man clearly possessed the ability to lead a family.

“Sir Tang, is there something on my face?”

“Ah, no. I was distracted by everything going on and acted rudely. My apologies.”

At Tang Horyong’s hurried apology, the man nodded with a serious expression.

“Not at all. It’s understandable. You’ve suffered something truly devastating.”

In truth, even the word *devastating* was insufficient to describe the damage the Sichuan Tang Clan had suffered.

Nearly nine-tenths of its household members had died, and most of the Tang Clan’s grounds had been destroyed.

The fact that the family line had survived was their one consolation, but it would take an extremely long time to restore the glory they had once enjoyed.

“The fellow martial artists of Sichuan have stepped forward to help, but… I’m worried about what lies ahead.”

If the Family Head, Tang Sadok, had been in his place, he would never have shown weakness in any situation.

Tang Horyong was different.

At his frank words, the man gently stroked his teacup with his long fingers.

“I believe you know very well why I came here, Sir Tang.”

“I understand that you came to investigate the Three-Sect Bloodbath.”

“To be precise, when I first left Henan, my purpose was to find the murderers who killed the late Poison King Tang Sadok and the Heaven-Shaking Divine Nun. But the situation changed considerably along the way.”

“That’s right. Dark Heaven—that bunch of inhuman bastards—has finally revealed its claws.”

“Although there was a precedent in Henan, attacking three prestigious great sects renowned throughout the land so boldly and all at once is proof that the war has reached our doorstep.”

Small unrest begets greater unrest.

But Dark Heaven’s existence was no longer something that could be concealed, nor was there any reason to conceal it.

Seven days and nights had already passed since the horrific day of the Three-Sect Bloodbath.

By now, word of it would have traveled a thousand li, and countless carrier pigeons would be flying to every corner of the land.

And unlike mere chaos, war brought people together.

“I heard that the orthodox Murim is rallying in Henan in the immediate aftermath of the Shaolin Bloodbath. Then, perhaps…”

“It is still only in the preparation stage. But it is a foregone conclusion.”

The man continued in a heavy voice.

“That is why I’m making this suggestion. Why don’t you go to Henan?”

“Henan.”

“Yes. The thing you’re thinking of will happen soon.”

After a brief silence, Tang Horyong spoke.

“Thank you for inviting me to such an honored occasion, but I cannot leave right now. As you know, as the acting Family Head, I must remain here for the members of my family…”

“Sir Tang.”

“Please, speak.”

“As you just said, Sir Tang, you are the acting Family Head. Naturally, you cannot leave the members of the Tang Clan behind and go.”

“...!”

Only then did Tang Horyong understand what lay behind the man’s proposal. His mouth fell open.

It was something he had never dared even consider.

“So, are you saying that we should relocate our family headquarters?”

“Well.”

The man’s clear eyes, seeming to see straight through him, turned toward Tang Horyong.

“Sword Saint Mae Jonghak said something to me. He said that a war even greater than the Great Faction War would soon break out.”

“The Sword Saint…”

Tang Horyong swallowed a groan.

That could not be the opinion of the Sword Saint alone.

The Shaolin Bloodbath had awakened the anger and vigilance of countless orthodox martial artists, and the new Murim Alliance had already finished preparing to take shape.

The entire orthodox Murim was preparing for the war that would soon arrive.

*Can our family survive in a situation like this?*

The question flashed through his mind, and his heart dropped.

The Sichuan Tang Clan had already suffered a blow without precedent in the history of the family.

Moreover, the Qingcheng Sect and Emei Sect had lost considerable strength as well.

If the enemy invaded once again, there would be little hope of stopping them.

“Haah.”

As Tang Horyong sighed with a vacant expression, a quiet voice reached his ears.

“Sir Tang, why do you think the Sichuan Tang Clan has managed to continue for the past several hundred years?”

“That is…”

“It was solely because it was the Tang Clan. Even if you took away the ‘Sichuan’ from its name, that fact would not change.”

“...!”

“If you make up your mind, the orthodox Murim will help the Tang Clan.”

Tang Horyong trembled, unable to continue speaking. At last, he forced his mouth open.

“We have made countless enemies over the years. There are people among the Nine Sects and One Gang and the Five Great Families who find our family troublesome. Will that really be all right?”

“Everything will be handled fairly and aboveboard. Set your mind at ease and establish a new nest. Henan, Shaanxi, or perhaps…”

A gentle smile appeared around the man’s lips.

“Shanxi would work too.”

“Shanxi?”

“Just say the word. There is plenty of land available.”

Tang Horyong suddenly remembered one fact he had forgotten.

The man standing before him was the leader who had unified the Murim of Shanxi, the foremost landowner in Shanxi Province, and a great tycoon.

“Thank you. Truly, thank you, Sir Jin!”

“Think nothing of it.”

At that moment, the man—Jin Wikyung, the Lesser Family Head of the Jin Family of Taiyuan—respectfully but majestically returned the acting Family Head of the Sichuan Tang Clan’s fist-and-palm salute.

Clunk.

“I heard you called for me.”

When Jin Wikyung spotted a young man cautiously poking his head through the gap in the pavilion door, he let out a lion’s roar.

“Youngest—!”

Thud-thud-thud-thud—wham!

It was a charge like that of an enraged bull.

As Tang Horyong watched the brothers reunite in an embrace—or perhaps a collision—he remembered one of the rumors about Jin Wikyung.

*They say he’s a complete pushover when it comes to his younger brothers.*

The leader who had unified the Murim of Shanxi and the foremost landowner in Shanxi Province was nowhere to be seen.

All that remained was some hopelessly doting fool.

*He is still young, after all. He lacks experience. He cannot compare to my older cousin, who is so cool-headed at all times. Of course. Absolutely.*

Tang Horyong had no idea that Mimi-chan existed.

* * *

“Youngest!”

Jin Wikyung charged at me, scattering tears from his damp eyes, and grabbed me in a tight embrace.

I had been in Murim for two years, so I had plenty of experience with this sort of thing. I had suffered through it so many times that I could easily predict a reaction like this.

Crack!

…But I hadn’t expected this.

What the hell was that? Why could I hear my bones going out of alignment?

I sighed as his embrace tightened around my entire body like an anaconda from the Amazon jungle.

In any case, I let him hug me because I was glad to see him. But his reaction was more violent than ever before.

“Hold on, hyung. Let’s talk after you let go. Let go.”

“Hyungnim?! Didn’t I tell you to call me hyung instead of using such a stiff formality? You’ve changed, you’ve changed!”

“Ah, fine, I get it. Now let me go.”

“You used to speak informally when you were little, so why are you using polite speech now? You’ve changed, you’ve changed!”

“Let go, fuck.”

“Gasp! You never swore, even when you were going through your rebellious phase! You’ve changed—!”

“Wow, your running commentary is killing me.”

*Is his day job a Murim martial artist and his side job a Dementor?*

Feeling as though my soul were being sucked out, I shuddered in revulsion and reached out.

Whirl—crash!

Jin Wikyung’s huge body slammed headfirst into the ground, upside down, and a heavy impact rang out.

A middle-aged man from the Sichuan Tang Clan who had been watching let out a startled groan.

“It’s okay, it’s okay. We’re just playing around.”

“Ah, but still…”

“Look. He’s getting up just fine.”

Just as I said, Jin Wikyung sprang to his feet as though nothing had happened. Tears of emotion glimmered in his eyes.

“You’ve gotten even stronger in the meantime. That’s our youngest.”

At his unchanged behavior, I let out a snort of amusement.

“You’re still the same.”

“Still the same? Do you know how worried I’ve been these past two months? I couldn’t sleep at night, and I had no appetite. I was reduced to skin and bones.”

I looked at his enormous, muscular body and muttered, “You look pretty well-fleshed-out to me.”

In any case, two months.

So much time had already passed.

I realized anew that it was almost time for me to return.

If ten days spent in one world amounted to roughly an hour passing in the other…

*About six hours must have passed. The plane might be landing soon.*

The timing was perfect. I had accumulated quite a bit of fatigue after overcoming the massive obstacle that was the Western Heaven Demon Lord.

Without wasting time on a long conversation, I got straight to the point.

“When are we leaving?”

“Our youngest. You must have suffered so much… Hm?”

Jin Wikyung, who had been anxiously examining me, suddenly stopped.

“What did you say?”

“You came to take me with you, didn’t you? Oh, and Samgoe too.”

Jin Wikyung’s eyes widened.

“How did you know that?”

The middle-aged man, who appeared to be an important figure in the Sichuan Tang Clan, also spoke with a startled expression.

“Sir Jin, did you not come to investigate the full circumstances of the incident?”

“I did. However, some of us, including me, will be returning to Henan. Just before we reached Sichuan, I received a mission to escort Samgoe, one of the principal culprits behind the Three-Sect Bloodbath.”

“Then what about the matter concerning our family…”

“Of course, that still stands. It would simply be difficult for the Tang Clan to do so right now.”

“That’s true. The Family Head is still unable to travel a long distance. We must also seek the consent of the other members of the family.”

“Yes. And…”

After quietly speaking with the middle-aged man for a while, Jin Wikyung sent me a discreet Sound Transmission.

*But how did you know?*

*You hint, I catch on. It just seemed likely from the circumstances.*

*Ah, our youngest. What enormous ordeal did you have to overcome to make you clever, too?*

*…*

*That somehow rubs me the wrong way.*

In truth, I hadn’t figured it out from the circumstances. I knew because a Quest related to escorting Samgoe had popped up.

“So when are we leaving?”

Jin Wikyung had just finished his conversation and answered my question.

“You already knew? That makes things easier. The sooner, the better. Are you ready?”

“The only things I brought with me are my two balls. I just need to bring my body.”

On top of that, I had two bundles of luggage wrapped tightly in bandages.

Jin Wikyung nodded and spoke.

“Sir Tang, where is Samgoe?”

The middle-aged man addressed as Sir Tang answered.

“He is being held with all four limbs bound and under strict guard. Ever since his balls were crushed, he has been trying to kill himself whenever he gets the chance, so you will need to be careful.”

“Oh dear.”

*Even I would want to die if I were him.*

In any case, everything was in place for a swift departure.

After thinking for a moment, Jin Wikyung gave a brisk answer.

“Then half a shichen.[^1] We’ll leave within half a shichen. Is that all right?”

“No problem.”

The moment I answered without hesitation, a frantic commotion arose outside the pavilion, followed by someone shouting.

“The Family Head! The Family Head has awakened!”

Jin Wikyung corrected himself in a lukewarm voice.

“One shichen. Let’s make it one shichen.”

“…Yes. That sounds better.”

What a shame. I could’ve taken the Myriad Poison Ring and bolted.

[^1]: A shichen is a traditional two-hour period.

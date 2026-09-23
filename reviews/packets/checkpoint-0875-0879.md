# Checkpoint Review — 875–879

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

# Chapters 875–879

## Plot

After Prince Shangshan is taken into Qianqing Palace, Jin Taekyung is escorted out through its guarded corridors. He hears Aehyang, the City Lord of Sichuan Province’s former concubine, in a restricted area. Taekyung and Hong Jin later suspect she is pregnant and that the Emperor may intend her child to replace Shangshan, but neither her pregnancy nor the Emperor’s plan is confirmed. Taekyung gave Shangshan the Myriad-Poison Ring for protection.

Hong Jin plans to contact Ma Sanbao about the prince’s danger. He recounts that the late Emperor entrusted Shangshan to him shortly before dying in a confused state; Taekyung suspects Blood Soul Gu may have been involved, but this remains unconfirmed. Taekyung has also made an undisclosed personal request of Ma.

In Hangzhou, Jeok Cheongang receives two letters—one from Taekyung and another from someone close to Hong Jin—reads them, and burns them. Their contents remain unknown. He says the group has been formally invited to the imperial palace. Meanwhile, rumors circulate that Shangshan has returned to the capital and that the Emperor has an heir. An undercover Embroidered Uniform Guard captain arrests people at an inn where the rumors were discussed. The Emperor and a hidden adviser suspect the East Depot, Taekyung, or both of spreading them. The Emperor says they will make the heir rumor true and begins a great celebration; no pregnancy or birth is confirmed. He also says a long-standing target must be removed for his great undertaking, without revealing the target’s identity.

## Continuity

- The Emperor has confined Shangshan in Qianqing Palace. Taekyung left without him and gave him the Myriad-Poison Ring; whether it can protect against Blood Soul Gu is unknown.
- Aehyang is in Qianqing Palace. Hong Jin and Taekyung suspect she may be pregnant, but this and the Emperor’s intentions remain uncertain.
- Hong Jin plans to contact Ma Sanbao about Shangshan. Taekyung’s additional request to Ma is undisclosed.
- The late Emperor died after a period of mental confusion while confined. Taekyung suspects Blood Soul Gu may have been involved. The City Lord of Sichuan Province showed strange symptoms before his death, and Blood Soul Gu was found in his corpse; any connection remains unconfirmed.
- Jeok Cheongang burned the two letters he received. Their contents and the purpose of the group’s imperial invitation are unknown.
- Rumors claim Shangshan returned to the capital and the Emperor has an heir. Their truth and who spread them are unresolved. The Emperor’s long-standing target and great undertaking are also unidentified.
- Taekyung suspects the Emperor is connected to Dark Heaven, but this is unconfirmed.

## Translation Decisions

- Retain “Qianqing Palace,” “Prince Shangshan,” “Myriad-Poison Ring,” “Blood Soul Gu,” “East Depot,” “Embroidered Uniform Guard,” and “Blazing Flame Divine Dragon.”
- Render 기관진식 as “mechanisms and formations”; retain “Third Shadow,” “First Shadow,” “No Shadow,” and “Marquis Within the Passes.”
- Use “imugi,” not “dragon,” for the creature Taekyung killed at Dongting Lake.

## Durable state

{
  "active_continuity": [
    "The Emperor has confined Prince Shangshan in Qianqing Palace; Taekyung returned without him.",
    "Taekyung gave Shangshan the Myriad-Poison Ring for protection against poisoning.",
    "The Emperor and a hidden adviser suspect the East Depot, Jin Taekyung, or both of deliberately spreading rumors that Shangshan returned to the capital and the Emperor has an heir; neither claim is confirmed.",
    "The Emperor says they will make the heir rumor true and begins a great celebration; an actual pregnancy or birth is not confirmed.",
    "The Emperor says a long-standing target must be eliminated for his great undertaking; the target’s identity is undisclosed.",
    "Taekyung suspects the Emperor is connected to Dark Heaven, but this is unconfirmed.",
    "Hong Jin believes Aehyang is very likely pregnant; the pregnancy and the Emperor’s plans remain unconfirmed.",
    "The late Emperor died after a period of mental confusion while confined; Taekyung suspects Blood Soul Gu may have been involved, but this is unconfirmed.",
    "The City Lord of Sichuan Province showed strange symptoms before his death, and Blood Soul Gu was found in his corpse.",
    "Jeok Cheongang received two letters, burned them, and said the group was formally invited to the imperial palace; their contents and the invitation’s purpose remain unknown."
  ],
  "continuity_sources": [
    879
  ],
  "open_questions": [
    "Is Aehyang pregnant, and what does the Emperor intend for her and Shangshan?",
    "Did the Emperor or Dark Heaven use Blood Soul Gu against the late Emperor and the City Lord of Sichuan Province?",
    "Will the Myriad-Poison Ring protect Shangshan from Blood Soul Gu?",
    "Who deliberately spread the rumors, and are they true?",
    "What is the Emperor’s long-standing target, and what is his great undertaking?"
  ],
  "safe_through": 879,
  "temporary_decisions": [
    "Render 기관진식 as “mechanisms and formations”; retain “Third Shadow,” “First Shadow,” “No Shadow,” and “Marquis Within the Passes.”",
    "Use “imugi,” not “dragon,” for the creature Taekyung killed at Dongting Lake."
  ],
  "version": 1
}

## Reading copies

## Chapter artifact 875

# Chapter 875

The farewell was brief.

Before long, the palace attendants returned and led Prince Shangshan away, surrounding him as they guided him through some part of Qianqing Palace’s vast, maze-like corridors.

*For now, this is the best I can do.*

I thought to myself as I watched the young prince’s back, glimpsed now and then between the attendants.

How much time did that child have left?

I didn’t know.

If I’d gained anything from this audience, it was the confirmation that the Emperor wasn’t a complete madman who’d stop at nothing.

*He’s already made plenty of enemies through his coup. He can’t just get rid of his youngest younger brother the same way.*

Everything needs at least some pretext.

Even in an era of absolute monarchy, with the Emperor ruling over all, that was no exception. And the Emperor, who’d brought a bloody storm to the imperial palace more than a decade ago, had dangers lurking out of sight.

Old retainers who longed for the late Emperor.

And the people, who pitied the young prince.

If Prince Shangshan died under unnatural circumstances in this situation, it would provide the perfect excuse for another rebellion.

*The most natural method would be poisoning…but that won’t be easy.*

No one knew exactly how far the Myriad-Poison Ring’s power extended.

But it was a divine treasure that had even absorbed the Formless Ultimate Poison that once spread through Jeok Cheongang’s body. Even the Emperor wouldn’t have an easy time obtaining poison of that caliber.

Unless he eventually discovered the Myriad-Poison Ring and took it by force.

*But this has bought us at least a little time.*

Giving the Myriad-Poison Ring to Prince Shangshan?

I didn’t regret it.

From everything I’d seen so far, the Emperor and Dark Heaven were definitely connected somehow, and if the imperial family fell into their hands, it was all over.

That was why I had to protect Prince Shangshan, even if it meant risking the ring.

He was the anti-Emperor faction’s only hope, and the powerful figure who could rally them.

And he was one of the friends I’d made here.

*Though there’s a bit of an age gap for me to call him a friend.*

I smiled bitterly and watched until Prince Shangshan and his party disappeared from sight.

When I turned away, heavy-hearted, a woman was quietly watching me. I still wasn’t used to seeing her, but one look was enough to make her face linger in my memory for quite some time.

“Have you been waiting long?”

The woman, So Gyo, replied in a calm voice.

“No. This humble woman is carrying out His Majesty the Emperor’s orders. How could I measure the wait as long or short?”

*That’s some serious loyalty,* I murmured to myself and nodded awkwardly.

“Then let’s go.”

The Emperor’s order So Gyo had mentioned was to escort me out of Qianqing Palace.

Of course, “escort” was just a polite way of saying she was keeping an eye on me and kicking me out, but what did it matter?

“I’ll lead the way. Please follow me.”

But I’d barely taken a few steps after So Gyo when I frowned.

“Wait. I don’t think this is the right way.”

“It is. You remember.”

Of course I remembered. In case the worst happened, it was essential to scout an escape route.

I stared at So Gyo, who’d answered so matter-of-factly, and asked incredulously,

“Don’t just say it is. I’m telling you we’re going the wrong way.”

“Qianqing Palace has different paths in and out.”

“What?”

“The life gate can become the death gate, and the death gate can become the life gate. Since you’re a martial artist who travels the martial world, Young Master Jin, I thought you would understand what that means.”

“……!”

I fell silent. A word flashed through my mind like a bolt of lightning.

“Don’t tell me…mechanisms and formations?”

So Gyo gave a slight nod instead of answering, then started walking ahead. I stared after her blankly before hurrying to follow.

I was still absorbing the shock of what I’d just heard.

*Damn it. Even for an Emperor, this is ridiculous. This isn’t a residence; it’s an impregnable fortress.*

There were no fewer than three Supreme Peak masters stationed in Qianqing Palace, not counting the Emperor.

One of them was a master of the concealment technique, guarding the Emperor from the closest possible distance. And even if I lowballed it, there were more than a hundred elite assassins stationed throughout the palace.

And on top of that, mechanisms and formations?

*He’s definitely not normal.*

It was only natural for the Emperor’s security to be thorough, but there had to be limits.

The defenses of this palace were decidedly abnormal.

As though they were a perfect reflection of the Emperor I’d met just moments ago.

*He must have been afraid, too. He’s made so many enemies.*

They said as many as thirty thousand people had been torn limb from limb and beheaded in the last coup.

Among them were members of the imperial family, bound to him by blood; founding heroes who had laid the foundations of the Great Nation; upright officials; and renowned scholars.

Every one of them had died.

In a rebellion against the natural order. At the command of a single man.

It would have been absurd if an Emperor like that had no enemies.

*Then could it be…?*

I followed So Gyo and found myself thinking of the Emperor—not as the ruler above all, but as a Supreme Peak master.

His formidable martial prowess. His face, which looked ten years older than it should have—no, a good twenty years older, considering how young he was.

*Was that why?*

Supreme Peak was a lofty realm no one could enter through innate talent alone.

And yet the ruler of the continent, who had everything anyone could want, had sweated blood to learn martial arts.

He must have swung weapons without pause, like the martial artists of the martial world he called ruffians. At times, he must have groaned under pain that racked his whole body.

But even then, it seemed he couldn’t completely shake off his fear of assassination and the nightmares that came with it.

*It’s only a guess, but it’s certainly possible.*

I’d taken countless lives with these very hands, so I thought I could vaguely understand how he felt.

There was no such thing as a justifiable killing. Only a killing with a pretext.

I’d comforted myself by saying I’d had no choice, that they were people I had to defeat. But that didn’t change the truth.

The countless dead would come to torment me from time to time—maybe even quite often—and I’d wake up drenched in cold sweat.

What about an Emperor who’d killed tens of thousands through a rebellion with no pretext at all?

*His nights must be a real inferno.*

I smiled bitterly and kept walking. So Gyo had led me on in silence the whole time, deeper and deeper into places I couldn’t make sense of.

It was starting to feel unsettling.

“Um, can I ask you something?”

So Gyo stopped and turned around. At the same time, she spoke without hesitation.

“Of course.”

“What?”

“I’m saying you can follow me without worry. Nothing unfortunate will happen, Young Master Jin.”

I fell silent for a moment, then clicked my tongue.

“Wow, right to the heart. Have you learned mind reading or something?”

“No. I simply noticed your breathing become slightly uneven at some point.”

“Oh. I gave it away, huh? You’re perceptive.”

“I’ve learned martial arts as well. Controlling one’s breathing is one of the most important things for a martial artist.”

She was right. The higher a master’s realm, the more often a fight was decided in a split second—not even a full breath.

But regardless, So Gyo’s manner had been almost provocative. Watching her turn away after saying that, I thought,

*So she’s picking a fight with me?*

Probably. No, almost certainly.

It was absurd to have So Gyo, who had no more than First Rate martial prowess, act as if she were teaching me a lesson. But I let it end with a silent chuckle.

Come to think of it, So Gyo was one of the Emperor’s loyal servants, and this was enemy territory. What else could I expect?

*I should be grateful she’s not attacking me.*

There was no point talking about it. I shook my head and was just about to start walking again when—

Crash.

“……!”

It was faint, but I heard it clearly. From somewhere along the dark corridor, among several paths branching off like a crossroads.

And then a voice, full of irritation.

—How dare you, you lowly wretches…!

“Please follow me.”

So Gyo hurried over and stood in my way, but I didn’t care. I raised my internal energy and sharpened my senses.

*A woman. That was definitely a woman’s voice.*

Something was going on. Something I didn’t know about yet.

And if I wanted to accomplish what I’d come to do in this damn imperial palace, I needed to uncover as many clues as I could.

Step.

“Young Master Jin!”

A low shout cut into my ears as soon as I stepped toward the darkness.

So Gyo glared at me with a cold look that was unmistakably a warning, and I became even more certain.

If she was blocking me this firmly, there had to be something here that outsiders absolutely weren’t allowed to see.

But this was the Emperor’s residence. I put on an easy, innocent smile and spoke as if I knew nothing.

“It sounded like something happened. Shouldn’t we go take a look?”

“I told you to follow me.”

“Come on. The imperial palace is a pretty unfriendly place. Who was that just now? From what I could tell, it sounded like a woman.”

“That’s enough. I’ve warned you.”

“One warning means I’m still fine for now, right? But seriously, who was it? I’m so curious I might not be able to sleep tonight.”

“Better that than sleeping forever.”

So Gyo answered with a stern face, then suddenly cried out,

“Out!”

Shhk-shhk-shhk!

It happened in an instant.

A dozen or so blades dropped from the high ceiling and surrounded me.

Black masks as dark as the shadows, with the eyes of killers visible above them.

Surrounded in a flash by the assassins of Qianqing Palace, I spoke in a low, heavy voice.

“You said nothing unfortunate would happen.”

So Gyo put a hand on the flexible sword at her waist. “It won’t. As long as you turn around and leave quietly.”

“I just heard a strange noise and came to take a look. Why are you so touchy?”

“Should I take that as defying His Majesty’s will?”

“That would be a problem.”

“Then turn around and follow me. Quietly.”

“And if I don’t?”

Ssshhh.

I silently drew up my internal energy.

Then, perhaps because my aura pressed down on them from every direction, or perhaps because they anticipated the bloodbath about to come, So Gyo and the assassins’ faces hardened like ice. I looked over them one by one, then quietly raised both hands.

“Fine. I surrender.”

“……!”

“Just finish showing me the way. I need to get back and eat.”

So Gyo let out a small sigh and ordered the assassins to withdraw. I watched them go and smiled to myself.

There was no need to stir up even more trouble here.

Though I’d been stopped in no time, I’d already accomplished what I’d set out to do.

I’d heard it clearly.

That sharp cry from a woman.

And it reminded me of someone’s voice I’d heard a few months ago at the residence of the City Lord of Sichuan Province.

It had been so sweet and dripping with seduction that I couldn’t have forgotten it.

*That woman’s name was…*

Right. Aehyang.

The beloved concubine the City Lord of Sichuan Province had lost to the Emperor.
## Chapter artifact 876

# Chapter 876

Hong Jin fixed a cold stare on the golden armor blocking his way.

His voice, usually high and gentle as a woman’s, had sunk lower than anyone had ever heard it.

“Move.”

“Impossible. You cannot take a single step beyond this place.”

“I said move.”

“Sir! Deputy Military Commissioner!”

“Do you really think you can stop me? You lot dare?”

“……!”

The dozens of Embroidered Uniform Guards looked at one another, their faces stiff.

They already knew the eunuch standing before them was no pushover.

They said no matter how high you climbed, power never lasted ten years, and no flower stayed red for ten days. But things were different when you were talking about the East Depot’s former Investigating Eunuch, who had once enjoyed the late Emperor’s favor.

Besides, plenty of old officials still remained at court, and Hong Jin had surely built up ties with them over the years.

Whether those ties were friendships forged as fellow servants of the late Emperor or secrets he’d seized as a power broker who’d once controlled the East Depot, no one could say. But one thing was certain.

His influence was not to be underestimated.

“Even after more than ten years away from the palace, a few letters are enough to send a low-ranking Embroidered Uniform Guard stationed here to the borderlands. So get the hell out of my way, if you want to keep wearing that shiny armor.”

A cold flame flickered in Hong Jin’s eyes.

Around four hours had passed since his young lord left to meet the Emperor.

The eunuch, renowned even within the East Depot for his cool head, was already at the end of his patience.

*If I’d known it would come to this, I should’ve done whatever it took to go with him.*

Something had clearly happened.

He tried to suppress the unease that kept rising inside him, but he was finding it harder and harder to do so.

Just as Hong Jin bit down hard on his lip without realizing it—

“Everyone, calm down. Take it easy.”

A breezy voice cut in out of nowhere. Hyuk Mujin stepped in front of Hong Jin and waved the Embroidered Uniform Guards down.

“Try to be understanding. It’s taking a while, so he’s worried.”

“Martial artist Hyuk!”

“Come now, Comrade Hong, you should calm down too. What did these people do wrong? We underlings do what we’re told, whether they say ‘get down’ or ‘bark.’ Right?”

The Embroidered Uniform Guards frowned, unsure whether he was taking their side or calling them sons of bitches to their faces. Hyuk Mujin didn’t give them time to think it over before continuing.

“Still, could you at least find out what’s going on? We’re all exhausted as it is. If you make this difficult, nobody’s going to have a good time. Right?”

“Wait. That’s…”

“Oh, you’ll check? Wow! The Embroidered Uniform Guard! The pride of the Great Nation! The guardians of the imperial family! Thanks a fucking lot! If you get the time, drop by the Hyuk Family Textile Shop in the center of the imperial capital. Give them my name and you can get a discount.”

There was no chance to reply. Without waiting for the guards’ answer, Hyuk Mujin quickly turned around, grabbed Hong Jin, and backed away.

He spoke in a low whisper.

“There’s nothing to gain by provoking them right now. You know better than most, so why are you doing this? Get a grip.”

Those words didn’t make the unease in Hong Jin’s heart disappear, but they were enough to make him remember something he’d briefly forgotten.

Hyuk Mujin was right.

If he used his remaining influence at court to move a few powerful figures, all he’d manage to do was get rid of a few hunting dogs.

He wouldn’t touch the body, let alone the head. And reaching the owner holding the hunting dogs’ leashes was out of the question.

Now was the time to hide his claws and sheath his fangs.

Of course, while his head had cooled, his heart was still pounding wildly.

“Aren’t you worried, Martial artist Hyuk?”

At Hong Jin’s sudden question, Hyuk Mujin tilted his head.

“Sorry? About what?”

“You don’t feel any particular loyalty toward His Highness Prince Shangshan. I know that. It’s the nature of martial artists, so I have no intention of criticizing you for it. But…”

“Oh, you mean I’m not worried about what happened to the Captain who went with him?”

Hong Jin nodded weakly, and Hyuk Mujin answered at once.

“Of course I’m worried. I am.”

“Then how can you be so calm?”

“This is the best I can do.”

“What?”

“I’ve been following the Captain around and going through all kinds of things with him. There’s never been a problem he couldn’t solve by getting involved himself.”

“……!”

“No matter how badly things got twisted, in the end, the Captain swept everything away. All those bastards who strutted around bragging about being masters or the masterminds behind it all went off to interview with Yama.”

Hyuk Mujin looked at Hong Jin’s wide eyes and continued in an unruffled voice.

“To be perfectly honest, I’ve never met anyone as strong as the Captain. He’s insanely strong.”

“Martial artist Hyuk, I’m sorry, but I’ll be blunt about this. The imperial palace is practically a living monster. No matter how skilled a Supreme Peak master Young Master Jin is…”

“I wasn’t just talking about martial arts.”

“……?”

“Not his martial arts. The man himself. He’s just a strong person, period. That’s the kind of person the Captain is.”

“……!”

“Even if the palace is crawling with masters a level or two above him, they still won’t be able to handle the Captain. It makes no sense at all, but that’s how the Captain I know has always been.”

“Does that make any sense?”

“It shouldn’t, but somehow it does. Isn’t that why you asked our Captain to look after His Highness Prince Shangshan?”

Hong Jin was struck speechless. Then he suddenly understood.

When he’d first received a secret letter from Ma Sanbao saying the Embroidered Uniform Guard was on the move, why had Jin Taekyung been the first person to come to mind?

Trust between them?

Of course that mattered. But if trust alone had been the deciding factor, he would have brought Li Feng, a lay disciple of Huashan and the Assistant Military Commissioner of Shanxi Province.

Even though Li Feng and Hong Jin had briefly been at odds, Li Feng had spent years offering unwavering loyalty to Prince Shangshan, who’d long been left with no support.

Compared to that, Hong Jin’s relationship with Jin Taekyung… calling it mutual trust was a little embarrassing.

It was true that he had a fairly close business relationship with the Jin Family of Taiyuan.

But why?

Why had he asked for Jin Taekyung, when he could have brought along a proven loyalist or another master from the martial world?

Hong Jin already knew the answer.

“You’re right, Martial artist Hyuk. I’d foolishly forgotten for a moment. I must have let my emotions get the better of me.”

Seeing Hong Jin regain his composure as if nothing had happened, Hyuk Mujin grinned.

“I understand. It happens.”

“Young Master Jin… yes, he really is an unfathomable person. Most of what I’ve heard about him is hard to believe. Of course, some of the information I went to great trouble to obtain must be nonsense.”

“Nonsense? What information?”

“Oh, that?”

Hong Jin answered with a little laugh.

“You’d laugh your head off if you heard it, too, Martial artist Hyuk. Apparently, Young Master Jin caught a dragon in Dongting Lake.”

“That’s definitely a rumor. It was more of an imugi than a dragon.”

“Thought so. I paid a thousand gold pieces for that information, and this is the kind of ridiculous…”

Hong Jin stopped mid-sentence.

After a breathless silence, he finally managed to squeeze out a few words.

“What did you just say?”

“Huh? What do you mean?”

“No, just now. You said it wasn’t a dragon…”

“Oh. An imugi. That’s right. I was there, too. At first I thought I was dreaming, but after a while I realized it wasn’t a dream. Well, it didn’t fly through the sky, so it definitely wasn’t a dragon—it was an imugi.”

“……?”

“By the way, what piece of shit leaked that information? That was supposed to have been handled quietly, under the strictest secrecy.”

“……!”

Still reeling as if time had stopped, Hong Jin realized that everything Hyuk Mujin had said earlier had been true—every last word.

Choosing Jin Taekyung really had been a stroke of genius.

*An imugi? He caught an imugi? A person caught an imugi? Wait, those things actually exist?*

The shock was so great that, for a moment, he even forgot to worry about the young prince.

Just as Hong Jin stood frozen with his mouth hanging open, Hyuk Mujin, who’d been cursing the rumor-monger for some time, cautiously spoke up.

“Um, would you be willing to spend another thousand gold pieces? I saw a talking tiger when I went to Nanman recently…”

“Move!”

A shout rang out, carried on internal energy. It was a voice Hong Jin knew all too well.

Hong Jin whipped his head around. His eyes widened like saucers when he saw who it was, while Hyuk Mujin, who’d been trying to strike a quiet deal, cried out on instinct.

“I’m sorry! Please spare me! I didn’t say anything! May the Captain protect me—long live the Jin Family of Taiyuan!”

“I’m back. I have something to tell you, so let’s get inside… Hyuk Mujin, you little shit, what’s wrong with you? Why is he acting like that?”

Hong Jin had been about to tell him about the talking tiger, but his heart sank.

*Where is His Highness…?*

No matter how many times he looked around, he couldn’t see him.

His young lord. The Great Nation’s last hope.

Hong Jin rubbed his eyes with his sleeve again and again, but only one person came back toward him.

Jin Taekyung, the Blazing Flame Divine Dragon.

*So it’s come to this.*

Something had definitely happened. That cruel Emperor’s hand had finally reached his lord.

But Hong Jin forced himself to hold back the haze gathering before his eyes.

It wasn’t over yet. Surely that young martial artist had found some way out.

And as if to answer Hong Jin’s hopes, Jin Taekyung—who’d nearly knocked the Embroidered Uniform Guards, standing firm as iron towers, flying with a shoulder-check—moved his lips.

“Get inside the pavilion. Right now!”

Of course, he didn’t forget to smack his one loyal subordinate on the back of the head as he passed.

“Glad you returned safely…”

Whack!

“Ow!”

“Yeah, I’m back safe and sound, you little shit.”

* * *

After returning to the pavilion, I used my internal energy to soundproof the place, then quickly laid out what had happened.

As briefly as possible, just the essentials.

First. The Emperor had locked Prince Shangshan inside Qianqing Palace under the pretext of protecting him.

Second. That Emperor was shameless as hell. Like the rabbit in the old folktale who left his liver behind, he seemed to keep his conscience hidden somewhere else. Oh, and he was a Supreme Peak master who looked way older than he was.

Third. It seemed like the beloved concubine the Emperor had taken from the City Lord of Sichuan Province a few months ago was in Qianqing Palace.

My summary was over—successful enough that even a twenty-first-century summary junkie, who treated their eyes and the scroll wheel as mere decorations, would’ve given it a passing grade. Hong Jin’s expression had changed with every sentence; now all that remained was unconcealable shock.

“The City Lord of Sichuan Province’s concubine… is staying in Qianqing Palace?”

“Yes. Almost certainly. But before I draw my own conclusions, there’s something I need to ask you.”

I took a deep breath and asked again.

“Is it normal for the Empress or the imperial consorts to stay in Qianqing Palace?”

“Not at all.”

“Even a consort the Emperor favors?”

“Not at all. The rules of the imperial family are strict.”

“Then…”

“That’s right. There’s only one explanation.”

Hong Jin and I met eyes. The next moment, we spoke at the same time.

“Pregnant.”

“With child.”

Fuck.

The Emperor seemed to have found a new heir for the Great Nation to replace Prince Shangshan.
## Chapter artifact 877

# Chapter 877

It had never made any sense in the first place.

These were members of the imperial family, for crying out loud. These were members of the imperial family, not Chunshik’s family next door. Why would they all gather in Qianqing Palace and live together like one big happy family?

Besides, having been there myself, I could say the place was closer to a fortress or a labyrinth than to the Emperor’s living quarters.

The kind of place where you could wander through roads as tangled as the Yeonsan Rotary in Busan and run into a Minotaur without finding it particularly surprising.

And that wasn’t all.

Assassins swarmed everywhere like Chinese cockroaches, and mechanisms and formations had been set up to deal with any unwelcome visitors.

At this point, even the dormitory dungeons beneath some British school of magic would look like a five-star hotel.

But the Emperor couldn’t have created an environment this hopeless simply because he was crazy.

He had a clear purpose.

Security, quite literally as solid as iron.

He must have surrounded Qianqing Palace with enough force to stop any assassin from breaking through, then filled it with loyal servants he could trust. That was why.

And until now, he’d carried out that purpose perfectly.

Right up until today, when some young ruffian who’d spent his life scraping by in Murim realized Aehyang was there.

Or perhaps until he guessed one of the Emperor’s most closely guarded secrets.

*Pregnant?*

It felt like I’d been hit in the back of the head with a sledgehammer. Hong Jin and Hyuk Mujin, sitting across the table from me, looked just as stunned.

“Pregnant…? Is that true?”

“I can’t be certain yet, but it’s highly likely.”

Hong Jin answered Hyuk Mujin’s dazed question, then added quietly,

“It would be best if all of this were utter nonsense.”

I nodded heavily.

To hell with family ties—the Emperor had seized the throne after practically bathing in his relatives’ blood.

If a child of his own blood were born under these circumstances, it was obvious what would soon happen to Prince Shangshan.

*Pulling up the weeds by the roots.*

The child who’d once had to leave the imperial palace in a rush, wrapped in swaddling cloth, had now grown into a proper young boy. And the seed of a towering tree, sprung from the same root, had taken hold and flourished.

That was more than enough reason for a suspicious Emperor to eliminate Prince Shangshan.

*Clearing the line of succession.*

Just as there couldn’t be two suns in the sky, there couldn’t be two Sons of Heaven.

The current Emperor ruled over the court and the people, suppressing their discontent, but he was still a tyrant and a traitor at heart.

No—like the blood running through his veins, that nature would be passed on to his new successor.

Along with the label of a traitor’s child.

And the powerful men who were forcing down their resentment toward the Emperor certainly wouldn’t welcome that.

The people who’d put together that petition—basically a rolling paper for signatures—already had an excellent alternative in Prince Shangshan.

*If that very prince disappeared from the world, it would be the best possible news for the Emperor.*

The air in the pavilion was heavy and cold, as if everyone were thinking the same thing I was.

Hong Jin had been staring into space, his gaze sunk deep, and a long silence had passed before he suddenly spoke.

“How did you guess?”

“What do you mean?”

“I know a fair amount about the imperial palace, but Young Master Jin couldn’t have made that guess just from knowing that a woman named Aehyang was staying in Qianqing Palace.”

I thought back to the situation and answered.

“I couldn’t have guessed from the sound alone. There was one other thing.”

“What was it?”

“The smell.”

“The smell?”

“Yes. It was faint, but I could clearly smell medicinal herbs. More precisely, a decoction.”

“A decoction…”

“To be honest, I do have people around me who know a lot about that sort of thing, but I don’t know exactly which herbs were used or what went into it. Still, when I thought about it, I could work out the general answer.”

I went on slowly.

“A decoction is ultimately used when someone is sick, or when they need to restore their health. So, given the circumstances, why would the Emperor be giving Aehyang one? Simply because she was ill and he was worried? Or was there another reason?”

When you fitted every circumstance and clue together, a picture began to emerge.

This time was no different.

At least as far as I could tell, the Emperor was far from a lovesick romantic, and Qianqing Palace was an unusual place for a reason.

“I couldn’t believe it myself. That’s why I came back as quickly as I could.”

Hong Jin let out a low groan.

“How likely do you think it is that this is true, Young Master Jin?”

“Do you want the cold, hard answer?”

“Yes. The cold, hard answer.”

“At least ninety percent.”

“……!”

“I’m sorry. But everything fits together too perfectly, as far as I can tell.”

It was a damnable reality, but I had to acknowledge what I saw.

The reason the Emperor, who’d left Prince Shangshan alone for over a decade, had suddenly summoned him to the imperial capital. The reason he’d practically forced him to stay in Qianqing Palace.

And… the reason he might want to harm Prince Shangshan.

One answer resolved every question.

*A new heir.*

Hong Jin couldn’t have missed that, either.

No—he was probably more certain of it than anyone.

Even Ma Sanbao, who’d come to visit the night before, hadn’t said a word about such important information. That meant the Emperor had kept Aehyang’s condition completely secret, even from the East Depot.

Hong Jin, who’d held a fairly high position within the East Depot, couldn’t fail to understand what that meant.

Call it a guess, but read it as certainty.

It was all but a foregone conclusion that the Emperor’s seed was growing inside Aehyang.

*He just wants to deny it.*

I muttered to myself and watched Hong Jin in silence. Then I brought up one of the questions that still hadn’t been answered.

“I know this isn’t the best time to ask, but may I ask you something?”

Hong Jin answered in a subdued voice.

“Anything.”

“Why didn’t the Emperor eliminate Prince Shangshan sooner? I mean…”

“Why didn’t he kill him?”

I nodded silently, and Hong Jin continued.

“I can’t know exactly what was in the Emperor’s heart, but one thing is certain. He was probably afraid of the backlash if he killed even a young prince who hadn’t been weaned yet.”

“Hadn’t he already killed countless people?”

“The purge didn’t end overnight. Especially when it came to the imperial family.”

“Tell me more.”

“Right after the Fourth Prince’s rebellion was successfully concluded, the late Emperor and the other members of the direct imperial family were confined and placed under strict surveillance. Then, over the course of a year, they died one after another, as if they’d all made some kind of agreement. Strange, isn’t it?”

His voice was calm, but he couldn’t hide the shock and fear that still lingered.

Hong Jin drew a long-stemmed tobacco pipe from inside his robe with a trembling hand and lit it.

Whoosh.

He exhaled a pale plume of smoke with a deep breath.

For a moment, I thought I recognized the smell from somewhere. Then I turned my attention back to his story.

“I mobilized the East Depot’s full strength to rescue the late Emperor and the other royals, but every attempt failed miserably. I was already being watched in everything I did. It wouldn’t have been strange if I’d been thrown in prison the very next day.”

“But in the end, the Emperor didn’t kill you.”

“That’s right. Maybe because of our old ties, or maybe out of simple caprice, the Fourth Prince let me live.”

“Old ties?”

“I served in the imperial palace for decades. I was close to the late Emperor, so I also crossed paths with the Fourth Prince quite a few times. He was a talented, sharp-minded boy in many ways. At least back then.”

Hong Jin’s gaze was empty as he watched the smoke drift toward the ceiling.

“Regardless, I survived, and I was finally allowed to see the late Emperor shortly before he passed away. Even though his mind was clouded, almost as if he’d gone mad, he entrusted Prince Shangshan to me.”

“Wait. He’d gone mad?”

“Yes. But why would that—oh.”

Hong Jin realized what I was getting at and asked, his face confused,

“Surely not?”

“It’s possible. What exactly were his symptoms like?”

“I saw him for less than fifteen minutes, so it’s hard to say. He was already old, though he’d been healthy enough to father a child at that age.”

“I know. The rebellion and confinement must have been a terrible shock. But you need to describe exactly what you saw. That’s the only way we can…”

“Find a similarity to the City Lord of Sichuan Province?”

“……!”

Hyuk Mujin, who’d been listening with a dry swallow, widened his eyes. I nodded quietly.

At the words *Dark Heaven*, I remembered that cursed creature I’d seen only about two weeks ago.

*Blood Soul Gu.*

A venomous creature whose traces even the most renowned physicians in Sichuan couldn’t find.

It left almost no trace at all, driving its host to death. It had been created centuries ago by the Five Poisons Sect of Nanman, and had been discovered in the corpse of the City Lord of Sichuan Province, who was no longer among the living.

*And the City Lord of Sichuan Province started showing strange symptoms months ago, on his way back from the imperial capital.*

Could this really be a coincidence?

I thought I could find the answer in Hong Jin’s expression, rigid with unspeakable tension.

“How likely do you think it is?”

Hong Jin answered after a silence.

“Ten percent. No… twenty.”

“Do you know how the other royals who were confined back then died?”

“It was never made public. They were forgotten.”

“Then…”

“I’m going to contact Eunuch Ma tonight at the latest. His Highness’s life… may be in immediate danger.”

Right.

If it really was the Emperor—or Dark Heaven working with him—who had implanted Blood Soul Gu in the City Lord of Sichuan Province a few months ago, and in the late Emperor more than a decade ago, then Prince Shangshan was as good as dead already.

But…

“I entrusted His Highness with a precious artifact I’d been carrying, so there’s no need to worry too much for now.”

The Myriad-Poison Ring.

Though he’d suffered a serious injury, it had detoxified the Formless Ultimate Poison that had even brought down Jeok Cheongang, the giant known as the Fire King. It was the Sichuan Tang Clan’s divine artifact.

Blood Soul Gu was ultimately a venomous creature created by the Five Poisons Sect. It couldn’t escape the Myriad-Poison Ring’s power.

No—it had to work.

“And one more thing. There’s something I’d like to ask Eunuch Ma to do for me personally.”

Hong Jin’s eyes widened at what I said next.

* * *

Hangzhou, in Zhejiang Province, had been one of the most extravagant cities under heaven even before the imperial court moved there.

It had countless scenic landmarks and beautiful views. Vast quantities of goods and wealth passed along its canals, and even late into the night, its brightly lit streets bustled with people.

A city that never slept, in every sense.

And it wasn’t unusual for customers to arrive late at night on the main road of this imperial capital, lined with all kinds of shops.

Though the shopkeeper’s attitude toward this particular customer was a little unusual.

“Go on, take a look around. If you like anything, ask me then.”

The middle-aged employee looked bored to death, his manner dripping with brusqueness. The customer studied him for a moment, then parted his lips.

“I’ve brought a message from the Blazing Flame Divine Dragon.”

“……!”

Beneath a sign that read *Hyuk Family Textile Shop*, the middle-aged shopkeeper—no, Jeok Cheongang, the Fire King—opened his eyes wide.
## Chapter artifact 878

# Chapter 878

The moment the Sound Transmission pierced his ear, Jeok Cheongang moved with remarkable speed—and complete naturalness.

“Oh, you’re looking for the finest Shu brocade? You should’ve said so earlier. Come on in.”

“No, wait. I was only…”

The man disguised as a customer tried to protest, but the terrifying energy coming from Jeok Cheongang’s grip on his wrist left him gaping.

“Gah.”

The pressure felt like it would crush his entire body.

He instinctively summoned his internal energy to protect his wrist, but it was useless.

No—when he saw the flames pouring from Jeok Cheongang’s eyes, even the last scrap of his will crumbled to ash.

*What the hell is with that look…*

This wasn’t a man. He was a beast born to hunt—a predator.

Frozen stiff against his own will, the man was dragged deep into the textile shop.

Between the towering stacks of cotton cloth and silk, two figures emerged like ghosts from a shadowy corner no one had noticed.

Thud.

In the faint lamplight, the faces of two young men—both appearing to be around thirty—came into view.

One had an expression as flat as if he were chewing sand. The other was handsome, but his upturned eyes were so sly-looking they were his one flaw.

By their respective traits, neither had the sort of face that made dealing with people easy.

The especially austere-looking young man spoke first.

In a painfully awkward tone, he said, “Hey, Mr. Jeok. What’s going on?”

Jeok Cheongang answered, “Hey, Mr. Jeok? You’ve got a death wish, don’t you?”

“……Oh. Not right now?”

“Can’t you tell by looking? How did you survive as a wandering martial artist with that kind of sense?”

“I’m sorry.”

The austere young man bowed his head. Song Ilseom carefully spoke up.

“May I ask who that man is?”

“A customer.”

Jeok Cheongang gave the brief reply, then added, “But he used Sound Transmission. He introduced himself with a title that starts with ‘Blazing’ and ends with ‘Dragon.’”

Song Ilseom replied at once. “I’ll close up for today.”

“Make sure the shop is secured. Oh, first, circle the area. If you see anyone suspicious, grab the bastard and bring him here too.”

“Yes. But what if there’s no other choice…?”

“What the hell are you asking me for? In that situation, slit his throat first.”

“Understood.”

“Just clean up after yourself. Make sure no one notices.”

“Leave it to me.”

Song Ilseom bowed politely and left at once. The man who’d heard their conversation felt his knees weaken.

*Is this a textile shop or a slaughterhouse?*

*Could they be… an assassin organization?*

Nothing in his orders had mentioned anything like this.

As his mouth went dry, the other young man who had stayed behind spoke up.

“What should I do?”

“Bring the rest here. Every last one of them.”

“It’ll be difficult to bring everyone right away. One of them is out at the moment.”

“Damn it, what kind of goddamn idiot can’t sit still for a minute?”

“Well, it’s Young Lady Ju.”

“She’s allowed to go out for a while. Right. Of course. She must’ve gone to check on the situation nearby. How thoughtful of her.”

“……”

“Quit looking at me like that and go bring the other freeloaders.”

“Yes.”

“Hey.”

“Yes?”

Jeok Cheongang stopped the young man as he was turning away and frowned.

“I told you not to look at me like that. Do my words sound like a load of bullshit to you?”

“It’s just that my eyes have looked this way since I was a child, so there’s nothing I can do about it… No. I’m sorry. If I get the chance someday, I’ll be reborn.”

“Good. That way you can reincarnate—and learn to look at people properly.”

“Yes…”

With a weak reply, the young man with the sorrowfully upturned eyes, Sama Pyo, left. Jeok Cheongang suddenly reached out toward something.

Swish.

His energy extended without form, and the air around them trembled.

The man’s pupils trembled too as he watched a wooden chest fly toward them, suspended in midair.

*Seizing an Object Through Empty Space!*

The man belonged to a rather extraordinary organization himself, so this wasn’t the first time he’d seen the technique. But he knew even a skilled internal-energy master would have to concentrate to pull in a chest that heavy.

Yet the middle-aged man before him had done it with ease.

With nothing more than a casual flick of his hand.

*Could it be…?*

Something clicked for the man, and he cautiously spoke.

“Could your title be the Fire King?”

Instead of answering, Jeok Cheongang blinked at him as if he were some curious creature. Then he kicked the man in the shin as fast as a flash.

Crack!

“Gah!”

“You little shit! You’re still wet behind the ears, and half your tongue seems to be missing. What was that—‘you’?”

“W-wait! Wait! Hear me out! I…”

“Stay right where you are. Move and you’ll get hurt worse.”

Thwack! Thwack! Thwack!

The man’s grappling technique, which he’d practiced until his arms were bruised, and his footwork technique, which he’d drilled until the muscles in his legs screamed, were useless now.

After getting hit in the shin, the stomach, the chest, and finally the bridge of the nose, the man collapsed like a puppet with its strings cut.

Thump.

Of course, even passing out wasn’t allowed.

“Up.”

He sprang upright, rising far faster than he’d fallen. His voice trembled as he spoke.

“Are you the Fire King, Great Hero Jeok Cheongang?”

His tone could not have been more respectful.

Jeok Cheongang had somehow pulled the chest closer with Seizing an Object Through Empty Space and perched on it. His expression was as satisfied as a surgeon who’d just completed a difficult operation.

“Your severed tongue has finally grown back in the right place. Good. I am Jeok Cheongang. And who are you?”

“I am…”

“I don’t need to know a nobody like you’s name. Just tell me who you work for. I can tell at a glance you’re an eunuch, anyway.”

“……!”

“What? Is that such a big secret?”

The man—or rather, the eunuch—was momentarily speechless. Jeok Cheongang chuckled and continued.

“I’ll admit, you did a pretty good job disguising yourself. That human-skin mask, even your beard—it all looks natural, like it’s your own. But you can’t fool this old man with something as basic as that.”

“Then how did you…?”

“I felt your pulse earlier. You didn’t have nearly enough yang qi for a man. Now, tell me—which is more likely in the imperial palace courtyard: running into a eunuch, or running into a martial artist without balls? I don’t need to spell it out, do I?”

The eunuch swallowed hard. He was impressed by Jeok Cheongang’s keen judgment, of course, but more than that, he couldn’t believe how little the man’s attitude had changed despite knowing he was an eunuch.

“Then you must know where I came from, too.”

“Of course. The only place in the world with the perverse hobby of ripping the balls off perfectly healthy men is the imperial palace.”

“……”

“Stop rambling and answer what I asked. Exactly where in the imperial palace do you serve? Are you under that eunuch who’s Prince Shangshan’s right hand? The East Depot? Or are you one of the ones licking the Emperor’s…”

“The East Depot.”

“The East Depot, huh? The place that gathers the most persistent and vicious eunuchs in the world. But why would an East Depot eunuch come all the way here?”

“The Blazing Flame Divine Dragon—no, your Disciple asked me to deliver a few messages.”

“Is the Emperor laying a trap?”

“Absolutely not. Your Disciple was the one who told us you were staying here.”

“That sounds plausible. But with the East Depot’s intelligence network, it wouldn’t be surprising if you’d found out somehow anyway. How are you going to prove it?”

At the narrowing of Jeok Cheongang’s eyes, the eunuch hurried to answer.

“M-Mong-su-ta.”

“What?”

“Your Disciple told me to say it. I have no idea what it means, but he said if I passed it on, I’d at least avoid shitting blood…”

The eunuch was on tenterhooks, but fortunately, Jeok Cheongang knew exactly what the clumsy-sounding word meant.

*Monster.*

The monsters from the other world that had stained the realm of immortals with blood.

And there were only two people under heaven who knew about them: Jin Taekyung and himself.

“Hmm. So he definitely sent you.”

“Y-yes.”

“If you’d said that sooner, I wouldn’t have had to hit you. Forgive this old man’s rudeness, my good castrate.”

The eunuch wanted to say that calling a eunuch a castrate was about the rudest thing you could do, but he held his tongue.

If he ran his mouth again, he might really end up shitting blood.

His only sensible move was to leave as soon as possible.

He reached deep into his clothing, took out a small sealed tube, and handed it over. Jeok Cheongang’s eyes grew serious.

“Is this the missive Jin Taekyung told you to deliver to me?”

“Yes.”

“And the other one?”

As Jeok Cheongang had said, there were two tightly sealed tubes. The eunuch spoke in a low voice.

“The person I serve ordered me to deliver this one.”

“The person you serve?”

“You seem to know the Deputy Military Commissioner of Shanxi Province.”

“Hong Jin? I haven’t met him, but I heard about him on the way here. Apparently, he’s a pretty decent eunuch.”

“……Yes. The person I serve is on close terms with him. He said the contents would help with what you’re going to do.”

“Is that all? Nothing else to tell me?”

“That’s right. I’m only a messenger.”

That was as far as the eunuch’s orders went.

He hurried out of the vast slaughterhouse—or rather, the textile shop—using a footwork technique. Left alone, Jeok Cheongang broke the seals and took out two rolled-up missives.

Rustle.

The smell of oil-treated paper mingled with the stale air inside the textile shop.

Jeok Cheongang quickly read the information prepared with help from the East Depot, after Jin Taekyung’s missive began with the eloquent line, *“I’m afraid we may be screwed.”* He let out a quiet sigh.

“What a goddamn mess.”

And just then—

Fwoosh.

Flames from Samadhi True Fire consumed both missives, twisting and writhing in the darkness.

As Jeok Cheongang silently watched the missives turn to ash and vanish with a soft rustle in the blink of an eye—

“I brought everyone.”

Sama Pyo, who’d left moments ago, approached with some familiar faces, then stopped short.

“Where is that man?”

“I sent him back a little while ago. Fortunately, he wasn’t suspicious.”

“Did you find out who he was?”

“An eunuch. One Jin Taekyung sent.”

“……What?”

Jeok Cheongang neatly ignored Sama Pyo’s confusion at such a painfully brief explanation and continued.

“Where the hell were those people that it took you so long to bring them?”

*Yaaawn.*

Sama Pyo nudged Taishan in the side as he yawned, his eyes still sleepy, then hesitated.

“Well, you see…”

“Looks like you were holed up in a corner sleeping.”

“I think I dozed off for a bit.”

“Next time, tell him he’ll be sleeping forever.”

“Yes.”

“What about Namho?”

Sama Pyo glanced at the old man, Namho, who was panting in rumpled clothes, and answered.

“He was choking Taishan.”

“Why?”

“Taishan ate all the liquor Elder Namho had hidden away.”

For the briefest moment, Jeok Cheongang imagined choking Taishan and Namho at the same time. Then he let out a deep sigh.

“Quit screwing around and get ready, all of you.”

“Pardon me, but what should we…”

“We’re going to the imperial palace soon.”

“What? How?”

Jeok Cheongang’s eyes gleamed as he answered.

“Don’t worry. We’ve been formally invited.”
## Chapter artifact 879

# Chapter 879

Where there are people, there are rumors.

Hangzhou, Zhejiang Province—the heart of the world and the new imperial capital of the Great Nation—was no exception.

If anything, it was one of the worst places for them.

Wherever you went in Hangzhou, people were packed together, repeating rumors they’d heard from someone else as if they were facts, spittle flying from their mouths.

They talked about the beauty of a high official’s new concubine—the sort of official said to be powerful enough to knock a bird from the sky. They were furious over the story that he’d squeezed the people dry to buy her expensive jewelry. And when they heard the Embroidered Uniform Guard had already begun investigating, they kept raising their cups in celebration.

“Even so, there’s no one you can count on like the Embroidered Uniform Guard. He may have climbed to the throne after committing such a heinous crime, but at least he knows how to get things done…”

“Shh. Shut that reckless mouth of yours. Didn’t you say one of that old man’s sons was in the Embroidered Uniform Guard?”

“I did.”

“And he still got caught? Even with connections in the Guard?”

“Oh, that guy. Apparently, he got fired not long ago.”

“Really? Why?”

“Don’t know. Maybe he was given some secret assignment. He disappeared about a month ago, then came back a few days ago with his face all swollen.”

“Swollen?”

“Yeah. Looks like he got a real beating for something he did wrong.”

The story drifted away as quickly as it had come.

Poets and scholars seeking inspiration from scenic landmarks. Idlers who’d traveled a thousand *li* to visit Hangzhou, the city of pleasure.

Poor scholars quietly sipping liquor after ordering cheap strong liquor and dumplings, and wealthy merchants patting their bulging bellies.

Hangzhou was full of all kinds of people, and they talked freely about what they’d seen and heard.

“I’ve finally seen West Lake. I could die right now without a single regret. If I had my way, I’d stay in Hangzhou for another year.”

“You’ve still got more than a month before you have to go home. What’s the rush? Let’s take our time looking around, then visit the Zhoushan Archipelago before we leave.”

“The Zhoushan Archipelago? Are you thinking of going to Mount Putuo?”

“That’s right. I don’t believe in Buddha, but if a famous mountain like that is nearby, I might as well visit while I’m here.”

“But I heard the nuns there are no different from martial artists…”

“If you mean the Buddhist nuns at Putuo Temple, there’s no need to worry. They disappeared more than ten years ago, when the imperial capital moved here and the martial artists of Hangzhou were driven out.”

The conversation among the poets and scholars who’d come to Hangzhou to visit its famous sights was in fairly high spirits. The merchants seated nearby, on the other hand, kept pouring liquor down with sour expressions.

“Things are looking bad in Sichuan these days. Prices are swinging around so wildly they’re impossible to predict. I’ve taken quite a hit.”

“Then is that rumor true? That foreign forces are about to pour in from Qinghai Province. They say even the Kunlun Sect, based in Qinghai, is in dire straits.”

“Foreign forces? They’re nothing but lawless thugs from the martial world—fanatics thoroughly bewitched by demons, at that. They’ve given themselves a fancy new name, but they’ll still get smashed by the Central Plains sects, just like the Demonic Cult did in the past. The Imperial Guard won’t even need to get involved this time.”

“You’ve been in Hangzhou too long these past few years. You don’t know the first thing about what’s happening in the world.”

“Oh? Have you heard something?”

“A martial artist I’ve known for a long time is with the Murim Alliance now… He says this is far worse than when the Demonic Cult invaded.”

“What? That bad?”

“Just look at what happened in Sichuan a few months ago. Nearly ten thousand troops gathered and fought a bloody battle. At that scale, you can hardly call it an internal dispute within the martial world. It’s practically a war between small nations.”

“……!”

“And that’s not all. Nothing’s been confirmed yet, but there are signs of some kind of movement in Yunnan, too.”

“Yunnan? You don’t mean those Nanman barbarians?”

“That’s right. They say the Nanman Beast Palace is mobilizing all its forces and marching north into the Central Plains. If the rumor’s true, they may have already reached Sichuan or Guangxi.”

“Heh. The fanatics weren’t enough, now the barbarians are eyeing the Central Plains too?”

“No, it’s the complete opposite. They’re joining the Murim Alliance to fight Dark Heaven. But something about it is strange.”

“If that’s true, shouldn’t we be glad? What’s strange about it?”

“Well… I heard those barbarians are fanatics too.”

“What?”

“Apparently they spend all day spouting weird nonsense about how fighting Dark Heaven is a holy war, and how the Earth Mother Goddess watches over them.”

“What kind of fucking nonsense is that?”

“How should I know? I only heard it secondhand through my connections. Anyway, it’s clear something much bigger is happening than anyone thinks.”

The continent was vast. But merchants, whose line of work forced them to keep their ears open, often heard all kinds of information from all kinds of sources.

Whether those rumors were true or not, it was worth remembering them. Someday, one of them might make you a fortune.

And just as the inn had grown noisy with all the conversations and clinking cups, someone tossed out a slurred remark.

“Oh, have you heard the news? They say His Highness, Prince Shangshan, is staying in the imperial palace.”

“……!”

“……!”

In an instant, the air that had been warm with drink went cold.

Silence fell over the inn. Everyone’s gaze had already turned toward the same place.

“Huh?”

Startled by the many eyes suddenly fixed on him, a thoroughly drunk middle-aged man stammered.

“W-Why is everyone looking at me?”

That was when a few people in the now-quiet inn spoke up.

“What did you just say?”

“His Highness, Prince Shangshan, is staying in the imperial palace? Not in Shanxi Province, his fief?”

“Are you sure about what you just said?”

Disaster always came from liquor and loose tongues.

As the questions came flying at him, the middle-aged man realized something was wrong. He felt the alcohol leave his system all at once.

“I-I don’t know if it’s true or not. I only heard it somewhere. It’s probably just a rumor.”

“Even if it’s a rumor, tell us. Everything you know.”

“No, no. I must’ve said something foolish because I’m drunk. I need to leave now, so please let me through…”

His flushed face had long since turned pale.

Though he managed to stagger to his feet, he couldn’t take even one step. Something that had dropped from somewhere had stopped him in his tracks.

Thud.

The object hit the floor with a solid thump, landing right in front of the middle-aged man’s feet. At the same time, the leather cord cinched around its opening came loose, spilling its contents.

Clatter.

Silver nyang spilled from the money pouch, glinting in the dim light.

At a glance, there seemed to be more than thirty.

As people gaped at the enormous sum, a quiet voice reached their ears.

“That was quite an interesting story.”

Everyone turned around again. No—looked up.

On the second floor, a young scholar sat alone at a table, watching the middle-aged man.

“Fifty silver nyang. I’d say that’s enough for the story. What do you think?”

“……!”

The middle-aged man’s eyelid twitched.

He was stunned by the staggering sum of fifty silver nyang—and by the young scholar who’d tossed it down so casually.

Enough?

It was more than enough. It was an absurd amount.

Fifty silver nyang.

As a day laborer on Hangzhou’s canals, he’d never even dreamed of touching so much money. Just looking at it made his heart pound.

But the consequences of the words he’d tossed out so carelessly weighed on him as heavily as that pouch.

“W-Who are you, sir? You look like you come from a good family. Did I say something I shouldn’t have…?”

“There’s no need to worry. I’m simply curious.”

Fifty silver nyang just to satisfy his curiosity?

That was ridiculous.

Even a rich young master wouldn’t throw away that kind of money for no reason.

The middle-aged man grew even more uneasy at the young scholar’s answer, but he couldn’t let a chance to change his life slip away.

Even this vast imperial capital, the center of the world, had its share of poor people. For a middle-aged man like him, fifty silver nyang meant a whole new life.

Clatter.

Having made up his mind, the middle-aged man hurriedly gathered up the spilled silver and stuffed it back into the pouch before anyone could steal it. He swallowed, then spoke to the young scholar.

“Near dawn, I was hanging around a gambling den when I heard the story. They said that more than a few hundred members of the Embroidered Uniform Guard had entered through the North Gate a few days ago. Even in the imperial capital, the streets were guarded more heavily than usual, and the atmosphere was strange that day.”

“Go on.”

“A few sharp-eyed fellows thought something was off, so they risked drawing a reprimand and snuck a look. Would you believe it? Those terrifying guards had surrounded a single carriage so tightly you could barely see it.”

“A carriage?”

“Yes. Not particularly grand, not especially small, either. The sort of thing you’d use to transport goods.”

“And His Highness, Prince Shangshan, was inside?”

“They said they saw it with their own two eyes. A boy’s face appeared at the window—he looked extraordinary at a glance. They said he was definitely the very Prince Shangshan everyone’s heard about…”

“That alone doesn’t seem like enough.”

“Pardon?”

The young scholar cut the man off and continued.

“It’s been more than ten years since His Highness, Prince Shangshan, left the capital. He was very young even then, and even after all these years, he still isn’t fifteen. How could someone who spends his nights hanging around a gambling den recognize His Highness’s face?”

“I-I suppose he guessed after seeing hundreds of guards make such a fuss.”

“Perhaps. But there must have been another reason he made that guess. I’ve already paid you well. You should tell me everything you saw and heard.”

The inn had been bustling with noise only moments ago. Now it was as quiet as a grave.

That was what Prince Shangshan meant to ordinary people.

A noble, yet pitiful, man.

An unfortunate member of the imperial family, exiled to Shanxi Province in a far-off land after losing his entire family to his older brother, who’d defied the bonds of kinship.

And now they said His Highness, Prince Shangshan, had returned to the capital.

After more than ten years—and in secret, surrounded by the Embroidered Uniform Guard.

Under the weight of all those questioning looks, the middle-aged man hunched his shoulders and struggled to speak.

“At first, I thought the same thing as you, Young Master. How could it be true? How could the likes of you recognize His Highness, Prince Shangshan? Why would someone who’d spent more than ten years in the provinces suddenly come to the capital? That sort of thing. But…”

“But?”

“When I heard the rest, it sounded pretty convincing.”

The middle-aged man paused to catch his breath. Then, in a silence so deep not even breathing could be heard, he continued.

“That guy jumped up and said, ‘The Emperor—no, His Majesty the Emperor—has had an heir. Of course his younger brother, His Highness Prince Shangshan, would come. He was surely invited to the celebration that’s about to be held.’”

“……!”

“……!”

For an instant, an invisible shockwave swept through the inn.

A few sharp intakes of breath broke the silence, and the dim lamplight fell on people frozen in place.

The young scholar’s face had gone stiff beyond words, too.

“An… heir?”

“Yes. He didn’t know if it was the Empress or one of the concubines, but he said she was definitely pregnant.”

The young scholar’s eyes sank into shadow.

Some of the more than a hundred customers in the inn looked the same.

The people biting their lips to hide their shock were poets, scholars, and merchants. Unlike the middle-aged man and a few other simpletons, they understood exactly what those words might mean.

*If all of that is true…*

The thought alone filled them with fear.

A new heir to an Emperor who’d long been without one. And the return of Prince Shangshan, the only direct member of the imperial family to survive the bloodshed more than a decade ago.

What could that possibly mean?

*A purge…!*

A silent scream rang in their heads. Their backs were already slick with cold sweat as they sensed the danger.

They should have left long ago.

Whether the rumor was true or not, this was a story they should never have heard in the first place.

At that moment, they felt as if they were standing at the edge of a thousand-*zhang* cliff, one misstep from a fall they could never climb back from.

Unlike the middle-aged man, who was happily counting his silver, and the few others who had yet to grasp the severity of the situation.

“So His Majesty has finally had an heir. What a blessing for the whole country.”

“What blessing? What blessing? The child will inherit the blood of a man who broke the bonds of kinship to take the throne—”

“Please, just shut your mouth. Do you have three or four lives to spare? You want to get me killed too? If someone reports us, we’re all finished.”

“If you’re so afraid of people overhearing, go hide at home. People have always cursed the ruler where he can’t hear them. The Embroidered Uniform Guard aren’t ghosts. How often are you even going to run into them? Honestly.”

“But what will happen to His Highness, Prince Shangshan?”

“What would a nobody like me know? I just hope he stays in the capital from now on. He suffered such terrible things as a child. Who knows what he’s been through? It’s about time he had somewhere peaceful to live.”

Words were always embellished and exaggerated, and people always heard what they wanted to believe.

The unbelievable rumor that had come from the middle-aged man’s mouth had already become a fact backed by solid evidence. Some of the people who’d been afraid from the start moved their trembling legs and crossed the now noisy inn.

To escape a fire too great to contain and survive.

Or to confirm the truth of this information and use it.

But when they finally reached the entrance, they realized they’d stepped into a swamp they could no longer escape.

“Where are you all hurrying off to?”

At the subdued voice, a dozen shadows stepped forward at once, blocking the old doorway.

Step.

For a moment, it was as if the world had stopped.

In the eyes of those hurrying to leave the inn were ten men with bamboo hats pulled low—and, flashing between their wind-cloaks, golden armor.

“The Embroidered Uniform Guard…!”

At those three words, which escaped someone’s lips like a scream, the inn froze over.

Then the young scholar, who’d been sitting silently in thought, spoke.

“That was a truly interesting story. Interesting enough to make fifty silver nyang worthwhile.”

The middle-aged man, clutching the pouch full of silver, stared blankly.

“Young Master, what on earth is going on…?”

“I’m no young master. But I still want to hear more of your story.”

“Y-Young Master! You can’t do this! You can’t…!”

The middle-aged man’s shouts were already out of the young scholar’s mind.

The young scholar—no, the Embroidered Uniform Guard captain—addressed his subordinates, who were blocking the inn’s entrance.

“What are you waiting for? Arrest every one of them.”

“Loyalty!”

With a crisp salute, ten golden figures raced in every direction.

Every one of them was a martial arts master at Supreme First Rate or Peak.

Shouts and tearful pleas burst out from every corner. It took no more than an instant for the cries of those trying to flee or fight back to drown them out.

Bang! Crash!

Amid the crashes ringing through the inn, the Embroidered Uniform Guard captain leaped from the second-floor railing and landed lightly on the ground. He patted the trembling middle-aged man on the shoulder.

“Now, it’s noisy here. Let’s move somewhere else and talk. We’ll discuss everything else you know, who told you that bullshit, and who else has heard it.”

He didn’t bother to tell the man.

This time, he would pay for the story with something other than silver.

And it would shine like silver, yet be incomparably sharper.

* * *

After hearing the report, the Emperor remained silent for a long time, even after the messenger had withdrawn. Only when one person remained nearby did he finally speak.

“What do you think?”

Between the dense strings of pearls and the gauzy silks drifting all around, someone answered.

“Someone must have deliberately spread the rumor.”

“Who’s behind it?”

“Isn’t it obvious? If not the East Depot, then Jin Taekyung, the Blazing Flame Divine Dragon. Or… both.”

“They joined forces?”

“That’s the only possibility for now.”

“I regret it a little. I wonder if it was wise of me to let Jin Taekyung into the imperial palace just because I listened to you.”

The Emperor clicked his tongue and murmured, almost to himself.

“Did the person who sent you to me predict a situation like this, too?”

Someone beyond the silks answered.

“That person is greater and wiser than anyone I know. But Jin Taekyung is unpredictable. He cannot be easily judged.”

Without realizing it, the Emperor nodded.

That audacity, so impossible to fathom. His strength and conviction.

Regardless of their respective positions, Jin Taekyung’s appearance the other day had nearly made even the Emperor laugh out loud.

“We’d better rein him in before he jeopardizes the great undertaking. And what of the target?”

“It won’t be easy. Not at present.”

“Of course. If it were easy, he wouldn’t have been a thorn in our side for more than ten years. But the Great Nation cannot stand firm while he remains. We must do it.”

Rustle.

In place of an answer, a faint breeze from somewhere caressed the silks.

When the Emperor realized that the person who’d been there only moments ago had vanished, he gave a bitter smile and muttered,

“The rumor’s already out. There’s no point hiding it now. We’ll just have to make it true.”

And so began the great celebration commemorating the birth of a new heir to inherit the Great Nation.

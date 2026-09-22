# Checkpoint Review — 690–694

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

# Chapters 690–694

## Plot

Yohi, Muyaho, and the unconscious Jin Taekyung recover inside a hidden healing realm beneath the Poisonblood Grounds. A mysterious Black Tiger saves them, possesses the Water God Dragon’s Origin Essence, and reveals itself as an ancient guardian spirit born alongside the sacred stone that once sustained Ailao Mountain’s Sacred Land. The Black Tiger explains that human wars drained the stone’s power and that Dark Heaven caused the catastrophe at Ailao Mountain.

The legendary Beast King Stone was only a powerless symbol created by Nanman’s first Palace Lord to unite the tribes; the true sacred stone is the cracked boulder at Ailao Mountain’s summit. Regretting that it failed to save the first Palace Lord, the Black Tiger asks Jin to use the Origin Essence to restore the stone. The System designates the Black Tiger as a guardian spirit, reveals the Hidden Sacred Land, and creates the hidden Quest **Last Chance**, but Jin has not yet decided.

While the realm trembles and a pillar of light rises, Nanman’s forces march toward the burning Ailao Mountain to kill Jin, believing him responsible for the disaster. The Black Tiger’s emergence makes every beast halt and bow in submission. At the Inner Palace, Baeksang expels the attendants, gathers ten thousand warriors, and opens the palace doors believing the grand plan is complete. He sees a White Tiger carrying an unidentified figure, followed by an immense host of beasts.

## Continuity

- Jin, Yohi, and Muyaho remain in the hidden healing realm beneath the Poisonblood Grounds; the pond restored Jin’s injuries and saved Muyaho.
- The Black Tiger is an ancient guardian spirit born with the sacred stone and formerly regarded as the lord of Ailao Mountain.
- The sacred stone sustained the land’s abundance and can command beasts, but its power was depleted by centuries of human violence.
- The Beast King Stone was a powerless political symbol created by Nanman’s first Palace Lord, not the actual sacred stone.
- The Black Tiger possesses the Water God Dragon’s Origin Essence and wants Jin to use it to restore the Ancient Sacred Stone.
- The System renamed the Black Tiger as a guardian spirit, revealed the Hidden Sacred Land, and created the hidden Quest **Last Chance**.
- Jin’s decision about the Origin Essence remains unresolved. The pillar of light, the realm’s tremor, the System’s unidentified discovery, and the means of escape also remain unresolved.
- Approximately three thousand Nanman warriors were ordered to kill Jin at Ailao Mountain; the beasts submitted when the Black Tiger appeared.
- Baeksang has expelled the Inner Palace attendants and gathered ten thousand warriors. He believes the grand plan is complete and expects irreversible bloodshed.
- An unidentified figure rides the White Tiger at the head of a vast gathering of beasts.
- Heugung’s fate remains unknown.

## Translation Decisions

- Retain **Water God Dragon’s Origin Essence**, **Ancient Sacred Stone**, **Hidden Sacred Land**, and **Last Chance**.
- Render **수호령** as **guardian spirit**, **신석** as **sacred stone**, and **수왕석** as **Beast King Stone**.
- Render **애뇌산의 망령** as **Apparition of Ailao Mountain** where the designation remains relevant, while using **Black Tiger** for the creature itself.
- Keep **Black Tiger** and **White Tiger** distinct.
- Render **영기** as **spiritual energy** and preserve em-dash formatting for the Black Tiger’s calm, ancient telepathic dialogue.

## Durable state

{
  "active_continuity": [
    "Jin Taekyung, Yohi, and Muyaho remain in the hidden healing realm deep within the Poisonblood Grounds.",
    "The healing pond saved Muyaho from the brink of death and restored Jin's severe injuries.",
    "The Black Tiger is an ancient guardian spirit born alongside the sacred stone and protects the hidden land beneath Ailao Mountain, formerly the Sacred Land.",
    "The sacred stone sustains the land's abundance, and its power to rule beasts is only one of its abilities.",
    "The Beast King Stone was a powerless stone created by Nanman's first Palace Lord as a legend to unite the tribes; the actual sacred stone was never his possession.",
    "Human wars drained the sacred stone's power, while the Black Tiger watched without intervening and later regretted failing to save the first Palace Lord.",
    "The Black Tiger possesses the Water God Dragon's Origin Essence and wants to use it to restore the sacred stone.",
    "The System changed the Black Tiger's designation to guardian spirit, revealed the Hidden Sacred Land, and created the hidden Quest Last Chance.",
    "Jin must decide whether to strengthen the Ancient Sacred Stone with the Water God Dragon's Origin Essence.",
    "A pillar of light appeared around the hidden realm after Yohi and Muyaho witnessed a tremor and the awakening of birds and beasts.",
    "Jin still intends to find an exit and return to Nanman before the Southern Heaven Demon Empress's attack causes further deaths.",
    "The System's unidentified discovery remains unresolved."
  ],
  "continuity_sources": [
    694
  ],
  "open_questions": [
    "Will Jin accept the System's offer to strengthen the Ancient Sacred Stone with the Water God Dragon's Origin Essence?",
    "What consequences will follow from the hidden Quest Last Chance, the pillar of light, and the unidentified figure atop the White Tiger?",
    "How can Jin, Yohi, and Muyaho leave the hidden realm?",
    "Is Heugung truly dead?",
    "What is the System's unidentified discovery?"
  ],
  "safe_through": 694,
  "temporary_decisions": [
    "Render 수왕석 as Beast King Stone, 신석 as sacred stone, and 고대의 신석 as Ancient Sacred Stone.",
    "Render 애뇌산의 망령 as Apparition of Ailao Mountain and 수호령 as guardian spirit.",
    "Render 숨겨진 성지 as Hidden Sacred Land and 마지막 기회 as Last Chance.",
    "Render 흑호's 의념 as telepathic dialogue with em dashes and a calm, ancient voice.",
    "Render 영기 as spiritual energy and 원정 as Origin Essence."
  ],
  "version": 1
}

## Reading copies

## Chapter artifact 690

# Chapter 690

At heart, the Nanman people revered martial prowess.

Like the Han Chinese of the Central Plains, they farmed, raised livestock, and mined gold and silver from the rivers and mountains. But in the end, the thing that mattered most to them was military might.

What good was wealth? Even if the harvest was plentiful and the fences were packed with livestock, strength was still needed to protect them.

Warriors.

And ferocious beasts capable of fighting alongside those warriors.

They were swords that could be driven into the chests of their enemies, but also shields that protected this land.

The Nanman people, who had endured a long history of struggle, understood this well. Even after the Five Poisons Sect was destroyed and the Nanman Beast Palace was established, they continued devoting considerable effort to training both warriors and beasts.

It was the same for the great tribes and the smaller ones alike. In the end, anything without strength was destined to be weeded out and brought to ruin.

The Yao people's Great Chieftain, Yohi, one of the leaders of Nanman's four great tribes, was no different.

No—if anything, her great ambition drove her to pursue it with even more zeal than the other tribal chieftains.

She invested the gold and silver she had received in exchange for turning a blind eye to Baeksang's actions into military power.

She recruited young men and women with talent and trained them as warriors. She studied the strengths and weaknesses of every species of beast and even improved them through selective breeding.

But…

Swoosh.

The moment she came face-to-face with *that thing* as it rose from the shadows, Yohi—who had encountered countless ferocious beasts until then—felt her heart sink.

“……!”

*Would this be what it felt like to be struck by lightning through the crown of the head?*

In terms of sheer size and strength, no beast could compare to an elephant.

It was as large as a small hill, its long, thick trunk strong enough to snap trees, and its sharp tusks capable of piercing even armor.

But *that thing*—that Black Tiger—was different.

Yohi could feel it.

A tremendous, overwhelming aura emanated from the black tiger unlike anything she had ever seen before.

*Th-This is…*

It was not simply a matter of size or appearance.

If an elephant was a small hill, then that Black Tiger was Taishan.

It had neither an elephant's long, thick trunk nor its sharp tusks. Yet simply by standing there, it radiated such immense strength that it seemed capable of cutting through and crushing everything.

The word *beast* could not express it.

A spiritual creature? That was no better.

The Black Tiger reflected in her eyes now radiated an aura far deeper and more overwhelming than that of any spiritual creature.

*What in the world is that…?*

Just as Yohi swallowed a low groan, a cool breeze flowed outward from the Black Tiger and swept through the surrounding area.

Swoooosh.

The grass and flowers filling every direction bent at the waist, and the clear water filling the small pond rippled.

As the wind swept over her entire body, a memory suddenly flashed through Yohi's mind.

*I've felt this wind before. Twice, in fact.*

She had attached no meaning to it at the time.

But now, she thought she understood.

Just before she had completely lost consciousness from the pill Heugung gave her, and when she had first opened her eyes in that enormous, unknown space, a wind like this had blown.

*Then could it be that the one who saved us from Heugung was…*

When her thoughts reached that point, Yohi's eyelids trembled.

But before she could even open her mouth, the Black Tiger—which had been silently staring at the unfamiliar intruder with blue-white eyes resembling Muyaho's—suddenly turned around and disappeared behind the enormous tree.

Swoosh.

At the same time, the wind slowly died down.

Yohi belatedly approached the tree with caution, but for some reason, the Black Tiger was nowhere to be seen beneath the broad shadow.

It had vanished.

Like a ghost.

Without a single trace or sign of its presence.

“……!”

*How?*

It felt as though she had been bewitched. If not for Muyaho's cry reaching her ears the next moment, she might have stood there in a daze for quite some time.

—Grrr.

Tap.

Along with the growl, a damp nose touched her elbow.

Yohi raised her head abruptly, like someone waking from sleep, and remembered the existence of someone she had temporarily forgotten.

*Jin Taekyung.*

Her mind was still tangled with unresolved questions, but there was something more important right now.

Yohi hurried to the pond and first examined Jin Taekyung's condition.

A faint breath flowed from his nose and mouth.

Fortunately, he had merely fallen into a deep sleep from accumulated fatigue. His condition was not bad.

No, he seemed to be doing much better than when Yohi had last seen him.

*Is that just my imagination?*

Yohi tilted her head and grasped both of Jin Taekyung's arms.

No matter how clear the water was, if it seeped into his wounds, his condition would have difficulty improving. She intended to pull him onto dry land, since he was already half-submerged in the pond.

And just as Yohi began exerting force to raise his body—

Thump.

A snow-white forepaw covered the back of her hand.

Yohi vaguely understood the meaning behind the gesture and asked,

“You want me to leave him alone?”

—Grrr.

“I'm sorry, but I can't do th—”

—Grrrr!

Slash. Splash!

It happened in an instant.

Yohi fell into the pond, feeling a sudden burst of pain, and stared at the White Tiger with startled eyes.

A sharp sting lingered across the back of her hand.

Blood flowed from the skin grazed by the beast's sharp claws, dyeing the surface of the pond red.

*Why?*

But her confusion at the unexpected situation lasted only a moment.

Before long, Yohi realized why that extraordinarily intelligent White Tiger had done this.

Hiss.

“The wound… Is it healing?”

That was exactly what was happening.

Yohi's eyes widened as she watched the wound on the back of her hand heal within the clear water.

The cut flesh slowly knitted back together, and the bleeding gradually stopped.

Slowly, but surely.

It was such an astonishing phenomenon that she forgot the pain she felt during the healing process.

When Yohi lifted her hand to watch the miraculous sight more closely, the healing flesh stopped recovering, and a faint trickle of blood began flowing once more.

*The pond. It stopped because I took my hand out of the pond.*

Her guess was correct.

The instant Yohi dipped her hand back into the pond, she confirmed that the wound began healing again and muttered,

“…A pond that heals wounds.”

It was a more preposterous story than the legend of gongcheong seokyu, the elixir said to grant a jiazi's worth of internal energy from a single drop.[^1]

And yet she was no longer surprised.

She had seen and felt everything clearly with her own two eyes.

This bizarre space, which could not be explained even by the four words *Mystic Gate Formation*. The existence of the unknown Black Tiger. And the wound on the back of her hand, which had already healed completely without leaving a trace.

Only now did Yohi think she understood how Muyaho had survived after suffering a sword wound across the nape of its neck.

“So that's why you stopped me. He'll recover faster if he stays in the pond.”

—Grrr.

Muyaho let out a faint growl and slowly licked the back of her hand.

Yohi watched the spiritual creature convey its apology in its own way, then opened her mouth.

“Then did that Black Tiger that vanished a moment ago save us? Was it the one that treated you and Jin Taekyung too?”

Muyaho nodded emphatically.

After confirming that her guess had been correct, Yohi fired off one question after another.

“Why? Do you know what kind of creature that Black Tiger is, or who its master is? Do you know where this place is?”

Muyaho hesitated for a moment, then shook its head.

Only seven days ago, Muyaho had followed the Beast Miao King and Jin Taekyung to Ailao Mountain and already encountered the Black Tiger once. Yet even to an innate spiritual creature like Muyaho, the Black Tiger's existence was an incomprehensible mystery.

“Haah. You don't know much either.”

—Whiiine.

“It's all right.”

Yohi stroked Muyaho's nape as it drooped dejectedly, but her mind remained tangled.

There was far too little information to figure anything out.

Where was this place?

How much time had passed?

And… when would Jin Taekyung regain consciousness?

Even so, there was one fortunate thing in all of this.

That unknown Black Tiger had shown them goodwill.

*At least it has nothing to do with Dark Heaven. If it did, we'd all be dead by now.*

Yohi muttered inwardly, and her gaze suddenly settled on someone.

He lay half-submerged in the water, utterly motionless, like a dead man.

Whether he knew what was happening around him or not, Jin Taekyung slept deeply, his expression utterly peaceful.

*If I had been the one who collapsed instead of him… If Jin Taekyung had been awake, every problem would have been solved.*

It might have been a clumsy thought born from helplessness.

But at some point, Yohi had come to trust Jin Taekyung from the bottom of her heart.

He possessed martial prowess great enough to defeat two Supreme Peak masters on his own, as well as humanity and moral conviction.

Unlike Yohi, who merely wore the hide of a Great Chieftain while being little better than a traitor, he had rushed from place to place more than anyone else to save Nanman from danger.

If she could not trust him, then who could she trust?

*If Baeksang and Dark Heaven have begun moving in earnest, Palace Lord Yayul won't be able to oppose them with his strength alone. There's not enough time.*

Most of the anxiety Yohi felt was becoming reality.

During the passage of time she could not know about, the Beast Miao King had been branded a traitor, escaped the Nanman Beast Palace after it turned into enemy territory, and vanished without a trace.

All of Nanman was boiling like an iron cauldron over a bed of charcoal.

No—perhaps it was lava capable of melting even that iron cauldron.

The warriors of each tribe that had answered the general mobilization order moved in lines toward the Outer Palace.

The Miao people, whose entire leadership had been imprisoned, held their breath in the midst of chaos.

And in a secret refuge known to no one, the Southern Heaven Demon Empress smiled brightly as she stood on the verge of completing her grand plan.

But Yohi did not know any of this.

Nor could she know.

Trapped in this strange, unknown space, all she could do was pray.

*If there is a heaven, please…*

*Please wake him as soon as possible.*

*Even if I have to die, please wake at least one person from this deep sleep.*

But with her eyes squeezed shut and her desperate wish spilling from her heart, Yohi failed to see the tiny yet unmistakable change taking place right in front of her.

Tap.

Someone's finger moved faintly.

Concentric ripples spread across the surface of the water, gradually traveling farther and farther away.

* * *

I dreamed.

The reason I could tell that everything was a dream was simple.

The moment I opened my eyes, I saw a face that was endlessly familiar.

Along with a voice that had slowly faded with time.

“Oh, what got you up at this hour? Why aren't you sleeping more?”

At that moment, my throat closed up and my chest felt heavy.

Holding back the tears surging into my eyes, I greeted him.

*It's been a long time, Dad.*

But contrary to my will, the voice that slipped between my automatically moving lips was thick with sleep.

“Dunno. I just woke up.”

Only then did I realize.

In this dream, the role I had been given was nothing more than that of an observer watching an old memory.

And my father, who had no way of knowing that, merely flashed me a broad grin.

“You little punk, I'm touched. How did this sleepyhead know Dad was leaving for work and wake up all on his own? Huh?”

A rough hand poked my cheeks.

The younger me grumbled at the harmless teasing.

“Ah, stop it. I’m going back to sleep.”

“You punk. Why are you sleeping again? The sun’s already high in the sky.”

“What time is it?”

“Six o’clock. Isn’t that the perfect time to start the day?”

“Yeah. It really doesn’t sound like it.”

The younger me buried his face in the pillow, and my father rose from his seat with a hearty laugh.

“Go to sleep, son. Dad’s going to work.”

“Huh? Already? It’s only six.”

“I have to go out of town early today. I might be home late.”

I repeated the same words endlessly in my heart.

*I can’t let him go like this. Dad, please don’t go. Please.*

But the younger me was different.

He was young and immature.

He had no idea that this moment would become his last memory with his father.

“Yeees. Have a good day.”

The words came out in a voice thick with sleep.

My father grinned at me, then affectionately tousled my hair.

“Okay. See you later.”

That was all.

My father would turn around, and the door would soon close.

A few hours later, I would be summoned by my homeroom teacher.

According to my memories, that was definitely what should have happened.

But…

“By the way, son.”

“……!”

At the sudden voice that pierced my ear, I shot upright.

It was not the younger me who had done it.

It happened through the will of my present self, now in my late twenties.

My father tapped the watch on his wrist and spoke with a laugh in his voice.

“Shouldn’t you be getting up soon?”

At that moment—

Crack.

Everything surrounding me collapsed and shattered.

The familiar ceiling and room. My father’s face. All of it.

And at the same time, something cold washed over my entire body.

Splaash!

Through the spray of water scattering in every direction, I saw a woman’s wide-open eyes.

A trembling voice soon pierced my ears.

“…How?”

*Who knows.*

I muttered inwardly, just like the young, immature boy in the dream that still felt so vivid.

*I don’t know. I just woke up.*

[^1]: *Gongcheong seokyu* is a legendary martial-arts elixir; a *jiazi* is a traditional sixty-year cycle.
## Chapter artifact 691

# Chapter 691

Sometimes, that happens.

Sometimes a dream is so wonderful, so dearly missed, that you don't want to wake up. Sometimes, even after waking up, you keep your eyes closed for a long while, turning over everything that happened in the dream.

But as always, the world never goes the way I want it to.

“Jin Taekyung!”

—Grrr!

Two figures, one large and one small, came rushing at me with a cry that sounded almost like a scream. It wasn't difficult to guess what was about to happen.

Of course, preventing it from happening wasn't difficult either.

Thwack, splash!

I swiftly tripped Yohi, then shoved away Muyaho's muzzle as he approached, drooling all over himself.

Then I closed my eyes again after saying one thing.

“Three seconds. Don't bother me for just three seconds.”

I counted to three in my head. Very slowly, recalling everything I had seen in the dream and etching it into my mind before opening my eyes again.

At the same time, an unfamiliar sky entered my field of vision—a sky so strange that I couldn't even tell whether it was night or day.

*An unfamiliar sky, huh?*

That was pretty new.

You'd think the sky you saw whenever you were bored couldn't possibly feel unfamiliar, but there was no mistaking what I was seeing with my own two eyes.

I sat up with a throbbing body and opened my mouth.

“Let me ask you first. You're not about to tell me that Dark Heaven took over Nanman while I was unconscious or something, are you?”

Soaked from falling into the pond, Yohi looked incredulous as she asked,

“That's what you say after tripping someone the moment you open your eyes?”

“You came rushing at me the moment I opened my eyes, so I tripped you. And look at the sky. I'd believe you if you told me this was hell.”

“What are you going to do if it is?”

“Who knows?”

I looked around.

A pond filled with clear water and lush vegetation. Hidden among the bushes surrounding us on every side were the chirping of mountain birds and the curious eyes of wild animals.

*The scenery is too nice for hell.*

I muttered inwardly and shrugged.

“I’m already dead, so what else can I do? I might as well finish sleeping.”

“……Sleep? Are you in your right mind?”

“No. In fact, everything is still spinning in front of my eyes.”

It was true. Just sitting up made my entire body throb, and dizziness washed over me.

Still…

“I do seem to be alive. Definitely.”

Yes, I had survived once again.

The pain assailing me even now and the System notifications ringing in my ears were proof of that.

Ding.



> **System**
>
> There are unconfirmed notifications.
>
> Would you like to check the new notifications?
>
> Y / N



I was about to check the System window right away when I suddenly remembered something I had forgotten and turned my head.

Bright blue-white eyes that shone despite watching me warily. And when I saw the tail spinning like a propeller, I let out a quiet laugh.

“Yeah. I survived thanks to you.”

—Kraaang!

With a whoosh!

As though he had been waiting for me to say those words, Muyaho's enormous body charged at me.

My not-yet-fully-recovered body screamed as it was crushed beneath his weight, but it was all right. This was a pleasant pain that reminded me I was alive.

Crack.

“……Ah.”

This was starting to feel a little less pleasant.

* * *

Fortunately, Muyaho's assassination attempt—which had made me suspect he might actually be Dark Heaven—ended in failure. After confirming that my ribs were still in place, I asked what I was most curious about.

“But what happened to Heugung? Why can't I see him?”

At the same time, I saw Yohi's face stiffen the moment the name Heugung left my lips.

“Don't even mention that bastard.”

“Wait. Don't tell me…”

“That's right. It's exactly what you're thinking.”

“Heugung proposed to you?”

“……!”

“What a lunatic. No matter how much he likes you, how could he propose in that situation?”

Yohi stared at me as if I were the crazy one, then finally parted her lips.

“He wasn't the Heugung we knew. We were all deceived.”

“That was true. He was pretty easy on the eyes with the Bone-Shrinking Technique.”

“……The Bone-Shrinking Technique? You knew?”

“Of course I knew. He even sent me a secret letter and met with me.”

“Then did you also know that he was a spy planted by Dark Heaven?”

“Of course I knew that too, wha—?”

What had I just heard?

After thinking for a moment, I opened my mouth heavily.

“Is that true?”

“Do I look like I'm lying?”

*Fuck. Looks like it was true.*

Only then did I suddenly remember the Quest to track the tracking scent.

Now I understood why the System had singled out and explicitly named only Yohi.

“All right. I retract saying Heugung looked pleasant. Along with a formal apology.”

I should not have said that.

To hell with whether he looked pleasant or not—the mood had long since turned ice-cold. Yohi answered with a sigh.

“It doesn't matter. I survived thanks to him.”

“Oh, and I'll apologize for bringing up the proposal too.”

“It's all right. He did propose.”

“What?”

“I said it's true. More accurately, it was less a proposal than a threat to toy with my life in the palm of his hand.”

“Th-Then did you accept?”

“I've been meaning to ask this for a while, but are you actually insane?”

“Uh, sorry. My head's a mess, so I keep saying stupid things.”

The back of my head was still throbbing.

It was true that I had once suspected Heugung, but after running into the two old monsters in the Poisonblood Grounds, I had erased even that slight suspicion.

*But Heugung, that bastard, was Dark Heaven's lackey?*

In the end, Heugung had been the knife in the sleeve—a move the Southern Heaven Demon Empress had kept in reserve until the very end.

And the question that came to me again at this point was how Yohi and Muyaho had managed to avoid that move.

Judging from what Yohi had said earlier, they had been in a fairly serious situation.

“What happened to Heugung?”

“He's dead.”

After thinking for a moment, Yohi added,

“Probably.”

“Probably?”

“We don't know the details either. That White Tiger was at death's door, and I lost consciousness from the pill he gave me. When I came to, I was here.”

The rest of Yohi's story was short. They didn't know where this place was or how much time had passed outside.

And Muyaho, who had clearly been on the verge of death, and I, who had suffered severe injuries, had survived thanks to this mysterious pond.

“I get it. It must sound like unbelievable nonsense. But really…”

“I understand.”

“What?”

“I said I understand. All of it.”

What was so remarkable about a pond that healed wounds?

Only people of this world would be unable to understand such a phenomenon.

I had come from the modern world, where potions, Magic, monsters, and Gates existed. Even if a few Orcs crawled out from those bushes right now, I was confident I wouldn't bat an eye.

“……”

On second thought, my eyebrow might twitch a little. No matter how you looked at it, Orcs appearing in the Murim wasn't normal.

*Unless a real Gate opened, like in the modern world.*

I muttered inwardly and reached out to skim the calm surface of the water.

A mysterious pond with an effect much like a potion.

The reason I had been able to shake off the fatigue piled up in my mind and body so quickly probably wasn't only because of my father, who had made an entrance like General Kim Jwa-jin.[^1]

*Item Appraisal.*

Beep.



> **System**
>
> —A mysterious power rejects the System!
>
> —The target cannot be identified!



See?

I had expected it to some extent, but as I thought, everything was a mystery. From one to nine.

And now, a tenth fact slipped between Yohi's lips.

“I saw a Black Tiger. A black tiger that felt stronger and more extraordinary than any wild beast I had ever encountered.”

“……!”

Splash.

My trembling fingertips disturbed the surface of the water, which had been slowly settling. I swallowed a groan as I watched the ripples spread into the distance.

*The apparition of Ailao Mountain…*

The enormous Black Tiger, which I had seen only once but could never forget, flashed through my mind.

It had appeared like a ghost, true to the name apparition, and vanished like one as well. Its image remained vivid even now.

*And that had been the first and last time.*

That night, the Beast Miao King and I discovered the Poisonblood Grounds while pursuing the apparition, but we couldn't find a trace of it anywhere.

The investigation team from the Nanman Beast Palace, dispatched immediately after the battle with the Thousand-Year Spider, had met with the same result. Then, because of the string of major incidents that followed, the apparition's existence had temporarily receded to the back of my mind.

And yet it had appeared here.

*What's more, judging from the circumstances, it definitely saved us.*

I didn't know its intention or its identity.

Frowning, I muttered inwardly.

*Check notifications.*

Ding.

With a clear bell only I could hear, holographic windows that had been held back burst into the air.



> **System**
>
> —Level Up!
>
> —Some injuries have recovered due to the effects of Level Up!
>
> —Some Status effects have been removed due to the effects of Level Up!
>
> —You have achieved the exceptional achievement **The Legend of One Against Two**!
>
> —The achievement Reward has been granted!
>
> —You acquired bonus points!
>
> —You acquired a large amount of EXP and Fame!
>
> —A sudden Quest, **The Knife in the Sleeve**, has been created!
>
> —The sudden Quest has been forcibly canceled!
>
> —You discovered **???**!
>
> —A sudden Quest, **???**, is pending. It will proceed once all activation conditions have been met!



I was only checking them now. Even while I had been unconscious, the System had done its job perfectly.

The problem was that even the System, which was as omniscient as a god, couldn't provide me with any definite information.

*It's normal for those question marks to bug the hell out of me, right?*

As I stared intently at the last two notifications—the ones that bothered me most—Muyaho, who had been circling me for a while, thrust his enormous head at me.

—Nnngh. Ngh.

“Do you need to poop? Go over there and do it. Hyung's busy.”

—Whiiine.

“I said I was bu—”

I suddenly stopped speaking and raised my head.

At the same time, I saw it clearly.

Something was looking down at this place from atop the cliffs encircling the pond, without giving off the slightest hint of its presence.

*That's…*

Before I could finish the thought, an unexpected voice rang out inside my head.

—You've awakened, human.

“……!”

—Come up. We have something to discuss.

At that moment, I remembered something from only a few months earlier.

The time when an imugi that had failed to become a dragon sent a thought into my mind from within a broad, deep river.



* * *

I climbed the cliff alone, leaving Muyaho and Yohi behind.

When I reached the moss-covered cliff with my battered body, I finally came face-to-face with a massive Black Tiger that resembled darkness itself.

The apparition of Ailao Mountain.

Yes—it was the same one.

“What are you…?”

At my first words, the Black Tiger stared at me with eyes of unfathomable depth.

—I don't know.

“What?”

—Even I don't know what I am. Too much time has passed for me to remember everything, and I have been called by many names in that time.

“……The apparition of Ailao Mountain.”

—I haven't heard that name in a long time. Was it around two hundred years ago?

The Black Tiger calmly sent the thought and took a step.

Though it clearly possessed a physical body, it moved like a ghost, without transmitting the slightest presence or sound.

Just as I was seized by the sensation that every hair on my body was standing on end, the thought continued.

—But, human. You know what kind of being I am.

“……”

—Denying it won't help. I have already confirmed his existence through you.

The Black Tiger slowly turned and opened its mouth.

Nestled between its jaws was an object that shone with dazzling blue transparency.

It was the Water God Dragon's Origin Essence.

“When the hell did you steal this, you bastard?”

[^1]: Kim Jwa-jin (1889–1930) was a Korean independence activist and military commander.
## Chapter artifact 692

# Chapter 692

Sometimes instinct beats reason.

Like the moment I saw the Water God Dragon’s Origin Essence sitting prettily inside the Black Tiger’s mouth.

“You bastard. When did you steal that?”

—…….

The words slipped out before I could stop them.

The Black Tiger stared at me with a frigid look before sending a thought my way.

—“Steal” is an excessive word.

It was a little excessive.

Even if he had actually stolen the Water God Dragon’s Origin Essence, he could swallow it whenever he wanted. In that situation, I was unquestionably in the wrong.

“Fine. I’ll apologize. I’m sorry.”

After apologizing cleanly, I politely held out both hands.

“So spit it out now. You can see my palm, right? Spit it out here. Come on.”

—It was astonishing.

“Yeah, I was pretty shocked too. Now that I understand everything, let’s start with that….”

—I felt the power contained within it. Then I saw an immeasurably distant span of time.

I paused and asked,

“Time?”

—Yes. It was several hundred years of time and memory, visible only to beings of the same kind. Everything belonging to an imugi who had failed to become a dragon was contained within it.

“……!”

—At the end of that ancient memory, a human appeared. A young, rough, infinitely reckless human.

The Black Tiger’s blue-white eyes, so much like Muyaho’s, gazed at me. Then a thought resembling the calm voice of a man echoed inside my mind.

—Be grateful to that imugi. If I had not seen his memories, all of you would have met the same end as that unpleasant human.

This world was full of unpleasant humans. If you turned the whole land upside down and shook it out, there would probably be enough to fill the Yangtze and then some. But I had a pretty good idea who the Black Tiger meant.

“Don’t tell me… Heugung?”

—I do not know his name. But unlike you, he had only one forepaw.

Technically, it had been a hand, not a forepaw. But that wasn’t important right now.

I looked at the Black Tiger with renewed interest.

“Hmm. Should I start by thanking you for saving me?”

—It does not matter. It was my choice.

“Then I’ll thank you anyway. I mean it.”

The Black Tiger gave me a brief look, then turned and began walking slowly. I naturally followed behind him and opened my mouth.

“There are a few things I’m curious about.”

—You are bothersome.

“What? You mean you’ll answer all my questions in good faith even though I’m bothering you?”

—No.

“Oh. Thanks for granting permission so readily.”

—……Human communication is truly strange. Is it because too much time has passed?

I let the Black Tiger’s thought wash past me and asked about the most important thing first.

“How much time has passed?”

His tail hung stiffly downward, making his discomfort obvious. Even so, an answer came before long.

—You spent one day here, by human reckoning.

“One day?”

By ordinary standards, that was an absurdly short time.

But under the circumstances, it was a different story.

The Great Snow Fiend and the Black Hand Fist Demon had foretold the bloody storm that would soon sweep across Nanman. With even the Beast Miao King’s whereabouts unknown, there was no one left who could stop the Southern Heaven Demon Empress.

*Damn it.*

The situation had been unavoidable, but it wouldn’t have been strange if thousands—or tens of thousands—had died during the one day I was unconscious.

I clenched my teeth and swallowed the curse before forcing out my next words.

“An exit. Tell me how to get out of here.”

—You intend to leave?

“Yeah. I’m grateful that you saved me, but I don’t have time to hesitate.”

—You intend to save your own kind from danger. Recklessly, as you did last time.

“You…?”

—Be at ease. I cannot read human memories. I merely inferred it from the sight of you remaining in the imugi’s memories. You must have fought so fiercely for a similar reason.

“……You were watching?”

—Yes. From beginning to end. As always, I was watching everything that happened here.

The Black Tiger naturally turned his head to look at me and continued sending his calm thoughts.

—But I found no reason to involve myself in human affairs. At least, not until you pulled out “that.”

“……!”

My eyes widened. Not because I realized that “that” meant the Water God Dragon’s Origin Essence.

I had remembered the moment when, in one last desperate struggle to stay alive, I had reached for the Origin Essence—only to hesitate when a chill wind blew in from somewhere.

At the same time, I had sensed something strange, so I let go of the Origin Essence. Muyaho arrived immediately afterward and saved my life.

“Then that wind…”

My voice trailed off. The Black Tiger’s thought echoed through my head.

—You were about to do something foolish. If you defy what is ordained, that is defying Heaven. Had I done nothing, you would have died, unable to overcome the power left behind by the imugi.

I silently watched the Black Tiger’s back as he walked along the endless cliff.

“Not once, but twice.”

—What are you talking about?

“You saving me.”

The Black Tiger gave a small snort.

—I merely felt sorry for someone who had handed everything they possessed to a foolish human. Without that reason, you deserved to die.

“That’s a little unfair. I don’t know why you’re hostile toward humans, but I’ve never committed a crime that serious in my life.”

—Even after trying to take innocent lives and burning down the home of those who lived in peace?

“What?”

Instead of answering, the Black Tiger pointed his head toward the bottom of the cliff.

Countless beasts, their bodies blackened in places, were drinking from an unnamed stream. There were thousands of them, even by a rough estimate.

If I added all the other beasts that might be living in this boundless space, there was no way to guess the total number.

*What the hell…?*

I stood rigidly atop the cliff, staring blankly at the sight.

—The inferno you unleashed is still devouring the entire mountain. If the flames had spread unchecked, everything would have burned away long ago.

“…….”

—Yes, I led them here. Just as I did seven days and nights ago.

Seven days and nights ago.

That had been the very day the Beast Miao King and I received the emergency report and headed for Ailao Mountain.

I quickly retraced my memories, and a flash of realization passed through my mind.

*The wild beasts.*

I remembered it clearly.

Of the more than three hundred warriors stationed at Ailao Mountain, more than two hundred had returned alive.

But the wild beasts hadn’t.

I hadn’t seen them anywhere—not at Ailao Mountain, and not in the Poisonblood Grounds.

“You were the one who did that too. You saved the wild beasts.”

—Monsters that should never have existed were released. I had not involved myself in human affairs for the past several hundred years, but that time, I could not remain uninvolved.

“Released?”

—You did not know?

A faint contempt appeared in the Black Tiger’s blue-white eyes as he stared at me.

—It was all the work of humans. You have been doing this for a very long time, and I remained here, watching all of it.

*Damn it.*

What had happened at Ailao Mountain had ultimately remained speculation. But the Black Tiger’s words confirmed it.

That, too, had been the work of Dark Heaven.

*If only… If only this had come to light a little sooner.*

With belated regret, I stared at the Black Tiger. I thought I finally understood, at least vaguely, why he had acted as he did that day.

I remembered the Black Tiger’s back as he repeatedly appeared and disappeared, even though he could have escaped at any time.

“You weren’t attacking us that day.”

—Yes. That was not my mission.

“You were just trying to tell us where the Thousand-Year Spider was.”

—I could not simply watch while a foul monster disturbed this mountain. Humans planted the seed, so humans should reap it. That is the natural order.

The Black Tiger continued walking as he answered quietly.

The path along the cliff grew narrower and steeper. Birds nesting on rugged peaks that rose among the clouds watched us with curious eyes.

How long had we walked while talking? The ground below, visible through the clouds and mist surrounding us on every side, looked unimaginably far away.

*I’m pretty sure this place wasn’t this large.*

When I first opened my eyes, I had thought it was a forest surrounding a small pond.

But when I looked around now, I saw enormous mountain ranges, valleys, and green pastures stretching in every direction.

*What the hell?*

I couldn’t even begin to guess anymore. Feeling as though I were surrounded by mysteries, I managed to part my lips.

“Where is this place…?”

—A land where life dwells. A place where everything lives in harmony.

*What kind of nonsense was that?*

At that moment, I suddenly remembered the church deacon who used to hand me spicy rice cakes when I was little and shout, “Jesus, heaven! Unbelievers, hell!”

“Even so, this can’t be heaven.”

—The kingdom of heaven? That is a fairly fitting expression. But this is a place deep within the land that no one can enter without my permission. It is also very close to where you were.

“Then… could this be the Poisonblood Grounds?”

At my muttered words, the Black Tiger’s massive head, several paces ahead of me, gave a small nod.

—It is.

“But this place….”

The words caught in my throat.

The Poisonblood Grounds?

Even if this had been Ailao Mountain, I wouldn’t have been able to believe it.

There were no fierce flames burning here, nor the distinctive eerie atmosphere that had lingered over Ailao Mountain.

—Enough. This is a place that you humans can neither invade nor understand.

He was right.

The Murim contained all kinds of strange and mysterious things, and Mystic Gate Formations were one of them. But the scene spread before my eyes had far surpassed their limits.

“Ha. The Poisonblood Grounds. This is the Poisonblood Grounds.”

I let out a hollow laugh and followed the Black Tiger up the mountain.

As our steps drew us closer to the summit, the Black Tiger’s thought reached me.

—Poisonblood Grounds is its current name. As I did, humans changed many things over the passage of time.

“What was it called before?”

—The Sacred Land.

“What?”

—It is a story from a distant past, as old as the imugi’s memories. In those days, beasts—not humans—were the masters of this land. The few humans who lived in groups within their own territories worshiped us.

“Wow.”

I was rendered speechless.

A forbidden land that no one could approach had once been called the Sacred Land. And if this had been back when the Nanman people were still few in number…

I couldn’t even begin to comprehend how long ago that must have been.

Five hundred years? Or a thousand?

*This is driving me crazy.*

Even if I had dumped every point into Intelligence from the beginning, I would have become an idiot at this very moment.

I shook my head and opened my mouth toward the Black Tiger, who had stopped walking before I noticed.

“Then what about you? What are you, anyway?”

—Did you not say it yourself before? An apparition.

“What I’m asking is what you were called when this place was the Sacred Land.”

The Black Tiger was silent for a moment before moving his massive body. Something wistful passed through his blue-white eyes.

—A guardian spirit.

“What?”

—Long ago, people called me that. The mountain lord[^1] who guarded Ailao Mountain. A guardian spirit born alongside a sacred stone.

[^1]: “Mountain lord” is a traditional epithet for a tiger.
## Chapter artifact 693

# Chapter 693

The Beast King Stone.

For some reason, the words felt familiar. At the same time, a memory from not too long ago rose to the surface.

It was a story from the distant past that the Beast Miao King had told me while we were on our way to Ailao Mountain, roughly seven days and nights ago.

The reason Ailao Mountain had come to be called a forbidden land. The existence of the Five Poisons Sect, which had given rise to the Nanman Beast Palace as it existed today, and the Great War that had stained all of Nanman with blood.

And… the vanished sacred treasure.

*It was a legendary story passed down by word of mouth. The Beast King Stone is the sacred treasure of this Palace, said to have been carried by the first Palace Lord. They say it could make every wild beast beneath Heaven obey.*

I remembered the Beast Miao King’s offhand remark.

—Look.

Along with the low thought that echoed inside my head, the apparition—or rather, the being I should now call a guardian spirit—slowly moved to the side.

And in the next moment, I was finally able to see it.

Ssshhh.

The Black Tiger’s body, which had been blocking my view, moved, revealing a massive boulder standing at the summit of a peak surrounded on every side by thick mist.

*No way.*

I instinctively realized why the Black Tiger had led me here.

And I realized what that enormous boulder was.

Step.

I moved forward as though entranced. Slowly passing the Black Tiger, I stopped in front of the boulder, which stood nearly thirty feet tall.

Ssshhh.

I could feel it.

An unknown energy wrapped around the massive boulder as though embracing it.

At the highest point of this mysterious land, it scattered faint, ink-dark radiance. Its appearance was mysterious—and dangerous.

Like some sacred treasure from a legend buried beneath the passage of countless years.

“…The Beast King Stone.”

The three words escaped me along with the breath I had been holding. The Black Tiger, which had approached my side like a ghost, gave a small nod.

—Correct. Long ago, it passed through the hands of a human and received that name.

“The human you’re talking about wouldn’t happen to be….”

—He was refreshing as the wind, clear as water, and unchanging as a tree. He was also the only human who could freely enter and leave this space without my permission.

“Without your permission? Was that even possible?”

This was a mysterious space that had remained hidden for hundreds of years—perhaps nearly a thousand.

The only reason we had been able to enter was because the Black Tiger had opened the way of its own accord. In response to my question, which was filled with confusion, the Black Tiger answered.

—It was possible. I did not know it myself, but before I gave my permission, the sacred stone that guarded this land accepted him.

I had no trouble understanding that the sacred stone the Black Tiger was referring to was the Beast King Stone’s original name.

At the same time, I felt I could vaguely guess the identity of the human he was talking about.

He was the one and only leader who had united the dozens of tribes that had waged endless wars against one another ever since people began living in Nanman, bringing them beneath a single banner.

*That wasn’t all.*

The man who had etched the five characters Nanman Beast Palace into this land had also been the first and last owner of the Beast King Stone during its brief appearance.

No. Perhaps he had never been its owner at all.

And when I heard the thought that followed, my guess hardened into certainty.

—One day, a great war broke out. Mountains and grasslands were swallowed by flames, and so many beasts and humans died that their corpses filled the rivers. As time passed, this land became more polluted. And as it did, the sacred stone slowly lost its power.

“Lost its power?”

—The power to rule a hundred beasts was only one of the sacred stone’s abilities. It was not all it possessed. It was called a sacred stone because it had protected the abundance of this land for countless ages.

I tore my gaze away from the Black Tiger and glanced toward the massive boulder.

Even now, the enormous stone scattered faint, ink-dark radiance. It was cracked and broken in places.

“No matter how I look at it, abundance seems pretty far from what I’m seeing.”

As for how far removed it was… saying it was at least the distance I had traveled from Henan to Nanman would be about right.

Putting aside its grimy, blackish color, the ominous energy flowing from the sacred stone was so unpleasant that even I felt uneasy.

*This really isn’t what I expected.*

Sacred treasures were not factory products with fixed specifications, but there was still a minimum expectation to meet.

Until now, I had imagined the Beast King Stone as a small, dazzling white stone—not something larger than Seoraksan’s Rocking Stone and radiating a powerful, ominous pressure.

“…I don’t know about abundance, but I think I understand why it was called the Beast King Stone. If you smashed something’s head with this, what beast wouldn’t obey? You could probably rule humans with it too.”

I was amazed that the first Palace Lord of the Nanman Beast Palace had supposedly owned this, even briefly.

How hard had he trained?

Had he hung an elephant from a pull-up bar and put up a five-thousand total on the big three?

The Black Tiger regarded me with a deep, somber gaze as I wondered how that legendary figure had measured his big-three total.

—Because of you humans.

“What?”

—Once, this land was filled with peace and abundance. Everything flowed according to the natural order, and the sacred stone was not as you see it now.

Realizing what the Black Tiger was trying to say, I muttered,

“…It gradually lost its power when humans began living on this land.”

—More precisely, it began when they started killing one another.

I felt as though I vaguely understood.

The sacred stone the people of Nanman called the Beast King Stone was practically the same body as this land. The more death and destruction overflowed from every corner, the more the sacred stone’s power diminished.

“So that’s why you helped the first Palace Lord? Three hundred years ago, as the Five Poisons Sect stained Nanman with blood, the sacred stone’s power would have weakened too?”

—I. No, we…

Some emotion briefly passed through the Black Tiger’s eyes. Perhaps it was longing. Or perhaps it was something that could be called regret.

—I did not help him.

“……!”

I faltered at the unexpected answer. Then the Black Tiger’s calm thoughts continued.

—If protecting the sacred stone was my mission, then merely existing alongside this land was the sacred stone’s duty. We could do nothing but watch.

“You just… watched?”

—Yes. Like a certain being you know.

I suddenly thought of the Water God Dragon I had encountered several months ago. That unknown being had guarded the river while pursuing enlightenment for several hundred years.

The imugi had possessed truly strange and overwhelming power, yet it had protected its territory without actively interfering in the affairs of the human world.

But if that was the case…

“What was the story about the Beast King Stone, then? The legend passed down among the people of this land….”

—A legend. Yes, it was exactly that—a legend. Something that clearly existed, but could only be fabricated as fiction.

Bitterness passed through the Black Tiger’s blue-white eyes.

—He was the only human who could understand our mission, and he wanted peace more than anyone. So, to end this war, he created the Beast King Stone himself.

“……!”

—I watched everything from a place no one could see. I watched him call a powerless stone the Beast King Stone, become a chosen hero, unite the tribes, fight against other humans, and finally fall.

My breath caught in my throat. It was as though a book densely filled with the legend of a distant past had opened before my eyes.

—That was how he died. What the humans worshiped as the Beast King Stone vanished as though it had never existed in the first place. The war continued for another hundred years, and I…

Growl.

The growl that escaped him trembled.

The Black Tiger stared at the sacred stone with eyes that seemed to be looking into the distance, as though chasing something beyond his reach. Then his blue-white gaze shifted toward me.

—I had to regret it for two hundred years.

After his final thought, a brief silence passed.

Standing tall in the wind blowing from somewhere and staring at the Black Tiger, I suddenly opened my mouth.

“For what reason?”

I continued without waiting for an answer. No. I had never expected an answer from the question in the first place.

“Because the land grew barren as the war continued, causing the sacred stone to lose its power? Because you thought that even the tiny bit of power it had left would soon disappear when what is about to happen arrives? Is that why you regretted it? Because you should have helped him back then—a pointless regret?”

The Black Tiger’s heavy thought echoed through my mind.

—Is that a condemnation?

“No. I don’t really care. If anything, I’m grateful that you helped us. Whether you believe that or not.”

I didn’t care about the sacred stone or the guardian spirit. I didn’t think I had any business caring about either.

It had already happened hundreds of years ago, and whatever their mission might have been, the fact remained that they had saved my life and the lives of my companions.

I had simply had that thought out of nowhere.

“For a guardian spirit, you’re pretty petty and cowardly. This much should be okay, right?”

—……!

“Not okay? If I offended you, I’ll take it back.”

The Black Tiger silently looked at me. Unlike his form, which appeared endlessly ominous, his blue-white eyes were large and clear.

And then.

—I regretted it every day, every moment, for two hundred years. I should have saved that human, even if it meant violating the natural order.

“……!”

—Reckless, young human. What you said was not wrong. For a long time, I was consumed by a single mission, and because of it, I made the wrong decision. But could you give me a chance?

“A chance…?”

—I want to restore even a little of the sacred stone’s power. And this time, I want to correct the wrong choice I made in the past.

Ssssh.

The enormous tiger’s jaws slowly opened. At the same time, a crystal of clear blue energy appeared.

Ding. Ding. Ding.

> **System**
>
> New information has been updated because the conditions have been met!
>
> **Apparition of Ailao Mountain** has been changed to **guardian spirit**!
>
> Hidden text has been revealed!
>
> **Hidden Sacred Land** has been discovered!
>
> You have met the conditions to activate a hidden Quest.
>
> A hidden Quest has been created!
>
> The hidden Quest **Last Chance** has been created!

Suddenly, bells rang out along with the System notifications. At the same time, one final holographic window appeared before my eyes.

> **System**
>
> Would you like to enhance **Ancient Sacred Stone** with **Water God Dragon’s Origin Essence**?
>
> **Y / N**

A tooth for a tooth. An eye for an eye.

And then…

*Spiritual energy for spiritual energy, is that it?*

Muttering inwardly, I suddenly looked up at the sky.

It was blue.

Just like the eyes of the Black Tiger who was looking at me now.

Or rather, the guardian spirit.

“I….”

* * *

Some had left their positions. Others had remained behind.

Yohi and Muyaho.

But while they waited near the pond for the one person who had not returned, they had to face a change that arrived before he did.

Rumble, rumble, rumble!

The earth shook, and the water in the pond surged like waves.

Hundreds—perhaps thousands—of birds took flight all at once, while even more beasts rose from the grass.

Yohi reflexively jerked her head up. A faint gasp of shock escaped her lips.

“Th-that….”

Kwaaaang!

A pillar of light shot upward as though piercing the sky, enveloping the unknown space.
## Chapter artifact 694

# Chapter 694

Deep in the night, with even the moon hidden.

In a mountain valley sunk in thick darkness, faint flames began to bloom.

One, two, three. Then, along with the hundreds of torches that soon multiplied, the world began to shake.

Rumble, rumble, rumble!

Tremors traveled through the ground. Beneath the torches swaying in the wind, large and small shadows shifted as rough breaths poured forth without pause.

Growl.

Hoo. Hoo.

An army.

It was a single army made up of countless humans and beasts mingled together.

The Nanman warriors, armed with swords, spears, and bows, sat atop their saddles and ceaselessly probed the darkness with their eyes, while beasts of prey with sharp teeth and claws continued to charge forward.

Their number was no less than three thousand.

And following the command of a single man, their destination had been decided from the moment they left the Outer Palace around noon.

* Ailao Mountain. *

The three words surfaced in the mind of the Captain of the Guards charging at the front. At that same moment, someone shouted from behind him.

“We can see it!”

Just as he said.

Everyone could see it, not just the Captain of the Guards. A massive, blazing inferno unlike anything produced by the torches carried by the three-thousand-strong army was flickering in the distance.

Crack! Whoosh!

Ancient trees of unknowable age fell in rows, while flames greedily devoured everything they touched and continued to swell in size.

A low groan escaped between the lips of the warriors watching a conflagration such as the world had seen neither in the past hundred years nor perhaps in the hundred years to come.

“I—I don’t believe this.”

“So it was true. It was really true….”

Hearing something from someone else was different from seeing it with your own eyes.

Shock and fear flickered through the eyes of the warriors as they gazed at Ailao Mountain engulfed in flames.

*Jin Taekyung.*

*Every rumor about him was true.*

*He shook off that many pursuit parties and made it all the way here. Just what kind of monster is he?*

Naturally, most of the warriors present had never encountered Jin Taekyung themselves.

No—it would be more accurate to say that they had never witnessed his true nature.

To them, Jin Taekyung had been nothing more than a young man from the Central Plains, an outsider with a strange appearance that differed slightly from that of the Nanman people.

But now, they had to fight him.

Their mission was to seal off Ailao Mountain without a single gap and kill Jin Taekyung, who could come bursting out at any moment.

But…

*Can we stop him? That monster?*

One question rose in everyone’s mind.

They had spent their entire lives hearing endless stories about Ailao Mountain, a forbidden land whose history began alongside the Nanman Beast Palace.

And whenever those stories were told, three words always appeared without fail.

The Fire Gate Clan.

An unknown clan said to exist somewhere in the distant Central Plains.

In the distant past, it was said that the Sect Leader of the Fire Gate Clan came to this land and brought the Great War with the Five Poisons Sect to an end—a war that had continued for more than a century even after the founding of the Nanman Beast Palace.

The Five Poisons Sect’s deadly poison, which had claimed countless lives, and the venomous beasts they commanded had melted like candle wax before the flames he summoned.

It was even said that the Sect Leader of the Five Poisons Sect at the time—who had reduced one hundred of the Nanman Beast Palace’s finest warriors to a mere puddle of poisonous water—could not withstand his power and fell to his knees.

*No. They said he was burned alive.*

And now, the old legend they had all enjoyed hearing as children had crossed over from the past and arrived in the present.

Right before their eyes.

Gulp.

The sound of someone swallowing dryly rang out with unusual clarity. Hands that had been loosely holding the reins now tightened with all their strength, and unease spread alongside their restlessly shifting eyes.

Then, in the very next moment, the Captain of the Guards finally opened his tightly closed lips.

“What are you so afraid of?”

“……!”

His voice, infused with internal energy, pierced the warriors’ ears. The Captain of the Guards continued emphatically.

“He is alone. We are three thousand.”

The warriors’ shoulders, which had unconsciously hunched, slowly straightened. Their wavering gazes began to regain their focus one by one.

*That’s right. No matter how strong he is, he is still a human made of flesh and blood.*

*Even if every rumor we’ve heard about Jin Taekyung is true, he can’t withstand this army.*

Three thousand.

Three thousand, no less. As a number meant to kill a single person, it was more than enough—absurdly excessive.

The Sect Leader of the Fire Gate Clan, who had supposedly crushed the Five Poisons Sect through overwhelming martial might?

When they remembered the stories they had grown up hearing, it was true that they felt afraid. But in the end, a legend was only a legend.

No—even if he came back to life, it was impossible for him to face three thousand Nanman warriors and beasts of prey alone.

It had to be impossible.

“Have you forgotten? Jin Taekyung is a traitor who endangered Nanman, a Han Chinese man no better than an animal who has forgotten the debt he owes for the Great Faction War.”

As the massive inferno drew nearer, the Captain of the Guards put even more force into his voice.

Shing.

“Warriors of Nanman! My proud brothers!”

The sword drawn from his waist gave off a sharp edge.

Moonlight pouring down from overhead and the flickering torchlight struck the snow-white blade and shattered across it.

“Pursue and kill him!”

“Waaaaaah!”

Clang, clang, clang!

Hundreds and thousands of weapons were drawn at once, along with the fiercely burning torches. And just as the army of nearly three thousand warriors drove their mounts toward Ailao Mountain with a distant, thunderous roar—

Whoosh!

The Captain of the Guards, along with every human and beast in this place, saw it.

A pillar of light rising through the blood-red inferno, and a black hill casting a shadow before the searing flames.

No. That was not a hill.

Rumble, rumble, rumble!

“What in the world is that…!”

As the world shook alongside the rapidly approaching black hill, the Captain of the Guards stared wide-eyed at the sight.

He did not know that he could no longer feel the wind.

He did not know that the three thousand beasts charging relentlessly toward Ailao Mountain had stopped in place as though by prior agreement.

Growl.

The tiger that had been with the Captain of the Guards his entire life lowered its head with a low growl.

No. It was not the only one.

The leopard, the bear, and the wolf. Every beast of prey, large and small, did the same.

Ssssh.

They curled their tails and lowered their massive bodies to the ground.

It was instinct etched into them from the moment of birth. It was worship toward a king who had returned after traversing the long years. And it was an irresistible command.

—Kraaaaar!

Along with a roar that devoured the world, blue-white eyes shone in the darkness.

* * *

Step. Step.

Soft footsteps echoed through the silent corridor.

At the sharp gazes of the escort warriors, each of whom had reached the Peak, the maids and servants fell facedown in prostration, followed by trembling cries.

“W-We pay our respects to the Palace Lord!”

Their fearful cries were directed toward only one person.

As Baeksang crossed the Inner Palace corridor under an impregnable guard, his gaze swept over them.

Those who worked in the Inner Palace varied in tribe and age.

There were children whose baby fat had not yet disappeared, middle-aged men and women, and…

An old woman whose hair had gone completely white.

The old woman was so aged that her movements were sluggish, and the guards frowned when they saw her floundering alone in the middle of the corridor.

Baeksang, whom they served with all their loyalty, was the master of the Nanman Beast Palace and the king of this land.

No—he had to be.

An old woman merely waiting for the day of her death could not block his path.

Step.

And just as though they had planned it, two of the guards took a step toward the old woman.

“Stop.”

At the low voice, the guards abruptly halted.

Looking toward the old woman who had entered his line of sight, Baeksang offered a greeting she could not hear.

*It has been a long time.*

Despite the long years that had passed, her face was familiar.

Baeksang remembered a young woman who used to sigh deeply whenever he and Yayul Cheok tore through the Inner Palace during their childhood.

*You’ve grown old.*

It was only natural. Unlike him, who had slowed his aging through martial might that had reached the Supreme Peak, she must have accepted the natural order of time in its entirety.

“I—I’m sorry, my lord. This old woman’s body is not what it used to be….”

At the sight of the old woman bowing and groveling without even daring to raise her head, Baeksang suddenly wondered.

Why had he stopped his subordinates?

Was it because she was one of the few people who remembered what he had been like in the past?

If not…

Was it because he wanted to delay *that moment*, which was drawing closer with every passing second even now?

*I don’t know. I truly don’t.*

It was bitter.

Even after coming this far, regret still remained in one corner of his heart.

And so did the fact that the woman who had once scolded him without restraint could no longer even meet his eyes out of fear.

*And this is the path I have walked all this time, I suppose.*

It was all nothing more than empty sentiment.

The days when he had fought back-to-back with his only sworn elder brother on the battlefield, sat atop the corpses of their enemies and shared fruit wine, and secretly watched a man and woman meet beneath the dim moonlight had long since passed.

“…My lord?”

At the escort’s cautious call, Baeksang’s eyes sank into their usual coldness.

“Clear the way.”

“Yes, my lord.”

As though they had been waiting for the order, the guards stepped forward and roughly shoved the old woman aside.

Baeksang looked down at the people who bowed even lower with terror in their eyes, then continued.

“Also. Effective immediately, all palace attendants residing in the Inner Palace are to be expelled.”

“I—I beg your pardon, my lord, but do you mean all the palace attendants?”

“Yes. All of them.”

Palace attendants were, as the name suggested, people who stayed in the palace and handled all kinds of menial work. They included everyone from the kitchen cooks who prepared every meal to those who cleaned and washed the laundry.

Leaving aside the harshness of the expulsion order, the Inner Palace would not function properly if the people responsible for its countless large and small duties disappeared at once.

The question of *why* rose all the way to their throats, but not one of the guards voiced it.

Baeksang’s word was law.

He was both the only Great Chieftain in all Nanman and the only Palace Lord to have received an absolute oath of loyalty from every tribal chieftain.

The five tribes that had left the Outer Palace in rejection of the new Palace Lord had now been stripped of every authority, and even the Miao leadership was imprisoned in the underground prison.

Baeksang’s authority was absolute.

“…Yes, my lord.”

Though the guards wondered at the sudden expulsion order, they obeyed it according to their duty.

Baeksang watched as the palace attendants, beginning with the old woman, were dragged out in a line, their faces drained of color. Then he muttered inwardly.

*Perhaps leaving this place will be a mercy to you.*

Soon, everything would begin.

And end.

Even Baeksang himself did not know how much blood would flow in the process.

*No. I could guess. I simply didn’t want to believe it.*

Perhaps that was why he had been shaken more over the past month than ever before, despite having lived as an iron man for more than forty years for the sake of a single goal.

*Caprice. In the end, it was nothing but a useless caprice.*

Yayul Cheok.

And Jin Taekyung.

Along with the names that flashed through his mind, Baeksang resumed his halted steps.

Step. Step.

One step. Then another.

Countless thoughts passed through his mind with every step.

What had happened to Yayul Cheok and Jin Taekyung after disappearing? Where were they, and what were they doing now?

Did the Southern Heaven Demon Empress know what he had done without anyone’s knowledge—his final act of caprice?

*But it is too late. No one can turn back now.*

Along with that hollow mutter, Baeksang stopped walking.

Before him, there was now only a single door.

Once he opened it, the highest dais in the Inner Palace would be waiting for him.

And below it…

Ten thousand warriors who had gathered in the Inner Palace in response to the general mobilization order.

*Noon. Tomorrow at noon. Gather every warrior in the palace.*

It was certain.

The grand plan had already been completed.

Remembering the Southern Heaven Demon Empress’s message delivered the previous night, Baeksang suddenly opened his mouth.

“The sunlight is hot.”

“…My lord?”

The door had not even opened, yet Baeksang felt heat that seemed capable of burning him alive.

What he was about to do was a terrible sin that could never be forgiven—and should never be forgiven.

But…

*There is no other way now, Hwi-ah.*

Thinking of his beloved son, the father threw open the door with force.

An unobstructed view and open sky appeared before him, along with the countless warriors gathered below.

But Baeksang’s gaze—all of his senses—was directed toward a single place.

Toward the green hill visible beyond the heads of the ten thousand warriors, beyond the walls surrounding the Inner Palace and the fortress walls defending the Outer Palace.

*That is….*

Though it was an immeasurably distant place, Baeksang could see it.

A massive White Tiger standing tall atop a high hill.

Its silver mane shone beneath the noonday sunlight, and another figure was sitting atop its back.

“…You came. In the end.”

At his quiet words, thousands—perhaps even tens of thousands—of beasts appeared behind the White Tiger.

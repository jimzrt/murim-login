# Checkpoint Review — 685–689

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

# Chapters 685–689

## Plot

Jin Taekyung kills the Great Snow Fiend, Hanbaek, by pulling White Flame from his own chest and driving it through Hanbaek’s throat. Critically wounded and near death, Jin summons the Water God Dragon’s Origin Essence, but before he can consume it, Muyaho returns with Heugung and Yohi. Completing the Quest to find Yohi grants Jin enough experience to level up, after which he loses consciousness.

While Jin remains unconscious, Yohi decides to expose Baeksang’s conspiracy with Dark Heaven and travel west to Boshan to rally the Yao people. Heugung reveals that he is actually the Beast Miao King, has been monitoring Yohi and Baeksang under the Southern Heaven Demon Empress’s orders, and intends to take Jin and Yohi to the Inner Palace while blaming Jin and the Murim Alliance for an attack on Nanman. He threatens to massacre the people of Boshan and incapacitates Yohi, but a blade-like wind attacks him before he can take Jin away.

Baeksang responds to Jin’s destruction at Ailao Mountain by evacuating civilians, mobilizing thousands of warriors, pursuing Yayul Cheok, and imprisoning the Miao Head Elder and other Miao leaders after they refuse to betray Yayul. The Southern Heaven Demon Empress orders the Inner and Outer Palaces fortified and announces that Dark Heaven’s grand plan will begin and end within three days.

Yohi awakens in a sealed stone chamber with her internal energy restored but her flexible sword missing. Muyaho emerges through the wall and carries her into a bright, peaceful realm filled with vegetation and animals. There she finds Jin unconscious and half-submerged in a pond. A strange energy-bearing wind scatters leaves from a colossal tree, and a Black Tiger rises beneath it.

## Continuity

- The Great Snow Fiend, Hanbaek, is dead. Jin killed him but remains critically injured and unconscious.
- Jin summoned the Water God Dragon’s Origin Essence but had not consumed it before Muyaho returned.
- The Quest to find Yohi was completed, giving Jin additional EXP and Fame and triggering a level-up.
- Muyaho returned with Jin and Yohi after Hanbaek’s death; the White Tiger collapsed but remains alive.
- Heugung is secretly the Beast Miao King. He was never sealed and used the Bone-Shrinking Technique at Great Completion to conceal his identity for decades.
- Heugung had monitored Yohi and Baeksang as a contingency for the Southern Heaven Demon Empress. He possesses or withheld the genuine antidote and incapacitated Yohi.
- Heugung planned to bring Jin and Yohi to the Inner Palace and fabricate a Murim Alliance invasion, while threatening to slaughter more than five thousand Yao people at Boshan.
- A blade-like wind attacked Heugung while he tried to take Jin; the immediate outcome remains unresolved.
- Yohi resolved to expose Baeksang and Dark Heaven, reach Boshan within several days, rally up to one thousand Yao warriors, and spread the truth across Nanman within seven days.
- Baeksang imprisoned the Miao Head Elder and Miao leadership after they rejected his demand to betray Yayul Cheok.
- The Southern Heaven Demon Empress considers Yayul Cheok and Jin no longer important to the grand plan. She ordered the Inner and Outer Palaces fortified, with the plan scheduled to begin and end within three days.
- Yohi is now awake in an unexplained sealed stone realm. Her internal energy seal has been removed, but her flexible sword is missing.
- Muyaho can pass through the stone walls and carried Yohi into a separate bright realm.
- Jin lies unconscious and half-submerged in a pond in that realm.
- A Black Tiger has appeared beneath a colossal tree after an unknown energy-laden wind scattered its leaves.
- The nature of the realm, Muyaho’s passage through solid stone, Jin’s condition, the Black Tiger, and the fate of Heugung remain unresolved.

## Translation Decisions

- Use **Hanbaek** as the Great Snow Fiend’s personal name.
- Retain **Water God Dragon’s Origin Essence**, **Bone-Shrinking Technique**, **Inner Palace**, **Outer Palace**, and **grand plan**.
- Use **Beast Miao King** for Heugung’s revealed identity.
- Render **Palace Lord** for 궁주 and **four great tribes** / **three great tribes** where applicable.
- Render **dark arts** for 사술.
- Use **Black Tiger** for 흑호 and keep it distinct from the White Tiger.
- Preserve Yohi’s mistaken or unresolved belief that the sealed chamber is an afterlife; do not establish that interpretation as fact.
- Retain Yohi’s incredulous, darkly comic internal voice during her encounter with Muyaho.

## Durable state

{
  "active_continuity": [
    "Yohi is awake in an unexplained enclosed stone realm, with her internal energy seal removed and her flexible sword absent.",
    "Yohi cannot find an exit despite searching for more than two shichen, striking the stone, and climbing the vines.",
    "Muyaho can guide Yohi through the rock wall while carrying her on its back.",
    "Yohi and Muyaho are now in a bright, warm realm filled with living vegetation, flowers, and animals behaving peacefully together.",
    "Jin Taekyung lies unconscious and half-submerged in a pond within the realm.",
    "An unknown energy-laden wind and falling leaves preceded the appearance of a Black Tiger beneath a colossal tree."
  ],
  "continuity_sources": [
    689
  ],
  "open_questions": [
    "What is the enclosed stone realm and how does Muyaho pass through its walls?",
    "Why was Yohi's internal energy seal removed, and where are Heugung and the others?",
    "What is Jin Taekyung's condition, and can Yohi reach him?",
    "What is the identity and nature of the Black Tiger?",
    "Is the bright realm connected to the dark arts or to the unexplained energy in the wind?"
  ],
  "safe_through": 689,
  "temporary_decisions": [
    "Treat Yohi's afterlife conclusion as mistaken or unresolved until the realm is explained.",
    "Keep Black Tiger distinct from White Tiger in terminology."
  ],
  "version": 1
}

## Reading copies

## Chapter artifact 685

# Chapter 685

FWOOSH. KWAANG!

Blue-white light-flames filled the Great Snow Fiend’s entire field of vision.

Then, accompanied by an explosion that announced the end of everything, an old body flew in a parabola and slammed into a massive boulder, shattering it.

KRRRUNCH.

His blood-red vision was hazy, and the sounds reaching his ears seemed to come from hundreds of *li* away.[^1]

[^1]: A *li* is a traditional unit of distance, roughly one-third of a mile.

But why?

Even in this situation, my consciousness remained startlingly clear.

Like a candle that burned brightest in its final moment.

*Final rally.*

The four characters flashed through the Great Snow Fiend’s mind.

At the same time, something hot overflowed from his throat.

COUGH.

Dark-red blood soaked his lower body. As he stared blankly at it—the blood mixed with pieces of internal organs—the Great Snow Fiend suddenly thought of something.

No. It was a certainty.

A certainty that would never change this time.

*It’s over. All of it.*

Paradoxically, the moment human beings confirm that they are alive is when they feel pain.

Yet even now, with the meridians throughout his body torn apart by Scorching Yang Qi and his flesh and bones crushed, the Great Snow Fiend felt no pain.

He felt only one emotion.

Fear.

Fear of the death finally looming before him—and fear of the one person approaching through his blood-red field of vision.

“Jin… Taekyung.”

A voice like a moan slipped between his trembling lips.

But no answer came to the old man standing before death.

No. More accurately, Jin Taekyung could not answer.

DRIP. DRIP.

With every step forward, drops of blood fell to the ground.

His body staggered as though it might collapse at any moment, and his eyes were clouded.

But he—Jin Taekyung—was unquestionably alive.

With his cherished weapon buried near his ribs, he was approaching the Great Snow Fiend while driving back even the death closing in around him.

*What is this…?*

The Great Snow Fiend’s entire body trembled faintly, and it was not solely because of death or the cold.

He was genuinely afraid.

And, at the same time, he was curious.

They were both human beings made of the same flesh and blood, so how could that young monster still be standing on two feet?

What had brought Jin Taekyung and himself to this situation?

*Where did it begin? What went wrong?*

Nearly half a century had passed since he left his homeland alone, abandoning his family, subordinates, and friends.

To overcome the limits placed upon him, he created new martial arts and devoted his entire life to perfecting them, crossing the threshold of death countless times along the way.

The righteous path?

He had never cared about such a shallow word, one that hypocrites loved to prattle about.

He had to survive by any means necessary, and to return to his homeland, he had to become strong enough that no one could ignore him.

Without that single-minded resolve, he would never have accepted the hand Dark Heaven extended to him all those decades ago.

*The day the Lord of Heaven descends upon this land, everything you desire will come true.*

*Everything…?*

*Yes. If that is what you want.*

The Great Snow Fiend had believed those words.

He had pledged his loyalty to Dark Heaven, and under the orders of the Southern Heaven Demon Empress, he had taken on a successor he had never expected to have and passed down the unique martial arts he had created himself.

All while waiting for *that day* to arrive someday.

And yet, why?

“Why should someone like this old man—why should I—die by your hand? Why!”

With that strangled cry, the Great Snow Fiend raised his head.

He saw a pair of eyes that still held an undying flame.

Then a faint voice pierced his ears.

“Because I have a reason.”

“What?”

“A reason I have to survive somehow. A reason I sometimes have to risk even death.”

“……!”

“That’s the biggest difference between us.”

Jin Taekyung answered quietly and reached out with a trembling hand.

His blood-soaked fingers closed around the spear buried in his chest.

FWOOSH. DRIP, DRIP.

As the spearhead slowly emerged, the blood flowing out with it sprayed across the Great Snow Fiend’s face.

Watching Jin Taekyung convulse from the horrible pain, the Great Snow Fiend laughed aloud as if he had lost his mind.

“Follow me soon. I’ll be waiting in the afterlife.”

SWISH.

Instead of an answer, the wavering spearhead touched his throat.

Jin Taekyung muttered in an exhausted voice.

“You idiot. Go find your parents.”

And that was the end.

THRUST.

He felt the cold blade pierce his throat.

Within the slowed passage of time, where everything had come to a stop, the Great Snow Fiend watched the world slowly darken.

It was far too short a moment to look back on the entirety of the century he had lived through.

*Damn it.*

Along with the curse he could never quite spit out, the old monster who had dominated an entire era tumbled into deep darkness.

* * *

No one could survive having their throat pierced by a spearhead.

That fact would not change even if the person were a Supreme Peak master possessing several jiazi of Yin-Cold Qi, or a fiend who had lived for nearly a century.

Just as it was now.

THRUST.

The transparent spearhead pierced his throat.

That was the end.

The Supreme Peak master once called the Great Snow Fiend no longer existed.

I stared blankly down at the corpse, its eyes wide open and its body frozen in place, then let out a short groan.

“……Ah.”

It was over.

Finally.

The moment I recognized reality along with the thought filling my mind, the world tilted.

SLIP.

No. It was my body that was tilting.

I tried to keep myself upright somehow, but there was nothing I could do. The last handful of strength remaining in my hand drained away, and the spear shaft slipped free.

THUD.

My vision grew distant.

The pain and exhaustion I had forgotten for even a moment, along with the relief, swept over me like a wave and crushed my entire body.

I collapsed where I stood and stared up into the air, gasping for breath.

> **System**
>
> - You have defeated **Level 155 Hanbaek**!
>
> - You have acquired a massive amount of **EXP**!
>
> - You have acquired a massive amount of **Fame**!

That was all.

There were three numbers in the holographic window visible through my blurred vision. None of them announced a level-up, and the System remained silent.

And I…

*This would be pretty lame if it were a hidden-camera prank.*

I laughed at the ridiculous thought.

For no particular reason, the corners of my mouth—dried stiff with blood—lifted, and a hollow chuckle escaped me.

*Fuck. Hidden-camera prank, my ass.*

*Right. So that’s how it is.*

How long could I last in this condition?

*Fifteen minutes? Or seven and a half?*

*Should I just be glad that at least Muyaho made it out alive?*

It was strange.

Even though the last hope I had clung to until the very end had collapsed, my heart remained so calm that even I was surprised.

Perhaps I had already sensed it vaguely.

*Luck doesn’t come twice in a row.*

The level-up I had received after defeating the Black Hand Fist Demon had practically been a gamble.

Since I could not see the exact amount of EXP I possessed, all I could do was make an educated guess.

*Ah. I must have enough to level up now.*

Or:

*No, this much won’t be enough.*

Unfortunately, this time it was the latter.

The Great Snow Fiend had died after leaving behind the massive amount of EXP the System had announced, but it was still less than the EXP I had acquired on the way to the Poisonblood Grounds combined with the EXP from the Black Hand Fist Demon.

Or perhaps the absolute amount required to level up had increased because of the luck that had come before.

Either way, the conclusion was simple.

My first gamble had succeeded, and my second gamble had failed.

As though Heaven had decided my fate from the beginning.

*Damn fate.*

Yes. Fate.

I had hated that word for a long time.

It could be used positively, but I had always thought it was a two-character word that could lump together every fucking thing that happened in this world.

Sometimes, the things that happened in life were too harsh and hopeless to dismiss as mere fate.

Like the memory of a certain day I kept hidden in one corner of my heart.

“Um. Mr. Kim?”

“Oh, yes. Vice Principal. But what brings you here all of a sudden…?”

“I’m sorry to interrupt your class, but could we talk outside for a moment?”

Even now, it felt like a scene from a cheap black-and-white movie.

Scene one: The bald vice principal appeared with a clearing of his throat, then left with my homeroom teacher.

Scene two: Through the glass window in the classroom’s front door, I watched my homeroom teacher’s bewildered face slowly harden.

And scene three: After returning to the classroom, my homeroom teacher called out a student’s name after a brief silence.

“Taekyung. Could you step outside for a moment?”

That was how I went from Extra Number One to the protagonist of the movie.

No.

I had never wanted to be the protagonist in the first place. If everything had only been a scene from a movie, I would have been happy.

If that had been the case, I would have half-killed the screenwriter and director who had come up with this shitty story just to force them to call for a retake.

But life is *One Take*.

With every moment and every choice, the story flows with me at its center.

Until then, I had never seriously thought about life even once.

It was only when I saw my father covered by a white sheet that I finally understood.

Cause: a monster wave.

Cause of death: crushing.

Because of the two damn characters called fate, my father’s story had ended, and mine had begun.

“……COUGH.”

SPLASH. DRIP, DRIP.

But I didn’t want the final scene of my story to be me dying on the cold ground while blood poured from my seven apertures.

I had no interest in an ending-credits sequence accompanied by soft background music and listing the names of my family, friends, and comrades.

I still had a chance to resist this damn fate.

A third chance to put my life on the table once more before it turned to ash and scattered in the wind.

*I want to live.*

That was the only thought filling my mind.

I meant it literally.

I didn’t want to die like this. There were still too many things I had to do, and too many people I had left behind.

CRUNCH.

I squeezed out what strength remained and bit down on my tongue.

The sharp pain made my fading vision and consciousness a little clearer.

This was the moment.

I spread open my trembling hand and muttered the command inside my mind.

*Inventory Open. Summon.*

SWISH.

A cool, smooth sensation traveled through my palm.

At the same time, contrasting System alerts pierced my ears.

DING.

> **System**
>
> - **Water God Dragon’s Origin Essence** has been summoned successfully!
>
> - **Water God Dragon’s Origin Essence** contains an immense reserve of qi unlike that of ordinary elixirs. Use it with extreme caution!
>
> - Your **Scorching Yang Qi** is mutually incompatible with the water qi contained in **Water God Dragon’s Origin Essence**! This is extremely dangerous. Proceed with caution!

I knew.

I knew this was crazy.

What I was about to attempt ran counter to the Yin-Yang and Five Elements theory that formed the foundation of most internal energy cultivation techniques.

Pouring water onto fire.

It was no different from trying to evolve Charmeleon into Blastoise.

But…

*I’m out of time.*

This was no time to worry about elemental incompatibility or any other bullshit.

Whether I died vomiting blood fifteen minutes from now or exploded because I couldn’t withstand the power contained within the Origin Essence, the result would be the same.

I would be dead either way.

I had to stake my life on the latter, which at least offered the sliver of a possibility.

GULP.

After vomiting another mouthful of blood, I squeezed out the tiny amount of strength left to me and raised my upper body.

Then, enduring the pain that made it feel as though my body were being crushed apart, I crossed my legs and finally looked up at the sky.

*Damn, look at those storm clouds. Of course the sky has to be fucking dark too.*

It was partly because it was nighttime, but no matter how I looked at it, this was a perfect day to hate dying.

There was no one watching over me, and no one around to put a cigarette between my lips.

Of course, even if someone had handed me one, I wouldn’t have smoked it.

WHOOSH.

Instead of cigarette smoke, my trembling breath scattered through the air.

The darkness that had begun to cloud the vision that had briefly become clear was not only because the night had grown deep.

I was dying.

And I was dying quickly, even now.

The time to begin my final gamble had already arrived at my doorstep.

*Right now.*

I brought my convulsing hand to my mouth.

Then I immediately swallowed the blue pearl filled with an extremely pure and dangerously massive energy.

Or rather, I tried to swallow it.

Until cool qi suddenly swept in from somewhere and engulfed me.

FWOOSH!

*What is this?*

With the sensation of every hair on my body standing on end, I froze like a statue.

At the same time, one word flashed through my mind.

*Enemy!*

But it wasn’t.

Something had clearly brushed against my body, yet I was still alive.

Then a thunderous roar from far away swept away all my questions.

“GRAAAAH!”

“……!”

I had thought he had escaped.

I had thought it was fortunate that at least he had survived.

*You came back. In the end.*

Although my vision was blurred, it was not difficult to recognize the snow-white body shining brightly in the darkness.

Nor was it difficult to make out the figures of two people sitting on the back of the White Tiger as it raced toward me like the wind.

Heugung.

And Yohi.

As I confirmed the faces of the approaching man and woman, I suddenly remembered the Quest I had briefly forgotten.

Then I stared blankly up at the sky and muttered:

“Just as I thought. This is a perfect day to hate dying.”

DING.

> **System**
>
> - **Mission:** Find Yohi (**Complete**).
>
> - Quest, **I Can See Your Tracking Scent**, has been completed successfully!
>
> - You have acquired a substantial amount of **EXP**!
>
> - You have acquired a substantial amount of **Fame**!
>
> - **Level Up!**

I could feel it.

The death scattering away before my eyes.

The warm presence wrapping around my wounded, exhausted body.

DING. DING. DING.

As clear bell chimes rang out beneath the storm-cloud-filled sky, I slowly closed my eyes.

SLIP.

Instead of the unseen moonlight, the demon of sleep poured down over me.

It was stronger than any opponent I had ever faced.
## Chapter artifact 686

# Chapter 686

Jin Taekyung’s plunge into a deep sleep that was almost like unconsciousness and Muyaho’s halt after racing like the wind occurred almost simultaneously.

THUD.

His head drooped weakly as he leaned his back against a shattered boulder.

Yohi swallowed a sharp breath at the sight. Heugung had already climbed down from Muyaho’s back and was checking Jin Taekyung’s pulse.

He let out a sigh.

“Whew. Fortunately, he’s still alive.”

It was good news, but Yohi’s complexion did not brighten.

“Still?”

Only then did Heugung realize his mistake and correct himself.

“I misspoke in my haste. He doesn’t seem to be at the point of hovering between life and death, so I don’t think you need to worry too much.”

“Not at the point of hovering between life and death? In that condition?”

Yohi’s doubt was hardly excessive.

Jin Taekyung was currently drenched in blood from head to toe. His clothes were covered in tears and cuts, while the unidentified armor draped over his upper body had been shattered around the chest as though something had pierced straight through it.

He looked so bad that it was strange to think he was alive at all.

Yet just as Yohi’s question was reasonable, Heugung’s words were also an undeniable fact.

“Having examined him directly, I can say that his injuries aren’t as serious as we thought. However, these marks… Even I find them difficult to believe, despite seeing them with my own eyes.”

Although their internal energy had been sealed for the time being, both of them were martial artists who had reached the Peak realm.

The two Great Chieftains found Jin Taekyung’s condition difficult to reconcile with the wounds they had identified, but they still let out relieved sighs at the fact that he was not hovering on the brink of death.

Before that relief had even faded, however, they discovered someone embedded in the massive boulder Jin had been leaning against—and were stunned.

“Hup.”

Yohi swallowed a short cry and realized it the next moment.

The unidentified old man, frozen in place with his eyes wide open, was already dead.

Blood was still flowing from his throat, which had been pierced by a snow-white spearhead.

THUD. DRIP, DRIP.

Yohi stared at the old man, who looked just as blood-soaked as Jin Taekyung, then suddenly muttered:

“That’s him.”

“Who are you talking about?”

“Black Hand. The owner of the voice that treated that old man like a subordinate.”

“Ah.”

“And if my guess is right…”

Yohi’s gaze swept rapidly across the surroundings before stopping.

There lay the corpse of the Black Hand Fist Demon.

The man who had slaughtered the warriors of the Western Yao Estate with a martial prowess worthy of a fiend was dead, his chest blown wide open.

*This is impossible.*

Yohi’s eyebrows trembled.

She had wondered if it might be so when she discovered the corpse of the unidentified old man, but the situation before her went far beyond anything she had imagined.

And it was not just Yohi who thought so.

“How could this…”

Heugung muttered under his breath, then swallowed the rest of his words.

It was utterly incomprehensible, but the scene spread out before them was undeniably real.

The surroundings had been turned to rubble by an unprecedented force. Two old men lay dead, while a lone young man had fallen into a deep sleep.

The conclusion was obvious.

Jin Taekyung had fought—and won.

He had defeated two Supreme Peak masters who had devoted several times as much of their lives to martial arts as he had.

“…The Blazing Flame Divine Dragon.”

The four words slipped between Yohi’s red lips like a groan. Awe filled her eyes as she looked at Jin Taekyung.

Whether such a thing was possible no longer mattered.

Jin Taekyung had made the impossible possible, willingly risking his life to save them, who were nothing more than southern tribespeople.

So now, they had to act for him.

*It may already be too late, but I have to act now.*

At certain times, some of Nanman’s venomous creatures shed their skins.

This process was known as molting.

But how could gaining a new body ever be easy? If the molting succeeded, the creature would gain a more beautiful and powerful body. If it failed, it would slowly die in its old, diseased one.

Yohi had chosen the former path.

*If I delay any longer, it’ll all be over. I have to let everyone know about this somehow.*

They had to expose the conspiracy connected to Baeksang and stop Dark Heaven.

Yohi’s own mistakes would be revealed in the process, but she had already made her decision.

She would accept the full price for the path she had chosen.

*I never should have done it.*

When she looked back, all she felt was regret.

Baeksang had laid out a broad and beautiful silk road before her, and Yohi had come all the way here by walking along it, turning a blind eye to everything happening around her.

But when she reached the end and happened to look down, she saw that her feet had long since become covered in blood.

Not her own blood.

The blood of other Nanman people.

Now…

She wanted to wipe that blood away. And if she could not, she would cut off her feet and be done with it.

One person had played a major role in bringing Yohi to this decision.

*Jin Taekyung.*

A stranger from a foreign land.

Yet he had fought for Nanman more than anyone else—just as the former Sect Leader of the Fire Gate Clan, now nothing more than a legend, had done centuries ago.

*I may be a Great Chieftain, but I can’t be worse than a Han Chinese person.*

*If a bitch like me can even call herself a Great Chieftain…*

Yohi swallowed the self-mocking words and immediately sprang into action.

RRRIP.

Her slender white hands tore into her ornate gown without a moment’s hesitation.

She removed the jewelry adorning her in gold and silver, exposing her arms and legs. Heugung’s eyes widened at the sight.

“Yohi.”

“There’s no time to talk. We have to move right now.”

Heugung stared at Yohi in silence for a moment, then nodded.

“You’re right. We don’t know when more enemies might come rushing in.”

“Considering how quiet it’s been around us until now, it’s safe to assume there aren’t any others. No, they probably decided Dark Heaven didn’t need to send more support after arranging for two Supreme Peak masters to come here.”

“That must be it. They already knew you possessed the tracking scent, and they probably intended to use us as bait to draw in the Palace Lord, Yayul. He would have been Dark Heaven’s greatest obstacle at present.”

But the bait had been taken by Jin Taekyung instead of the Beast Miao King, and the hunters who had prepared the hunt had been hunted by him.

No one could have predicted such a situation—not even Dark Heaven.

Yet the more the conversation continued, the heavier Yohi’s heart became.

“But what if Jin Taekyung didn’t come in the Palace Lord’s place… What if the Palace Lord was in a situation where he couldn’t come?”

“That…”

“My tribespeople—the Western Yao Estate—were massacred. It’s an unprecedented disaster, so by now the Inner Palace must be in an uproar.”

“Then shouldn’t we go to the Inner Palace as quickly as possible?”

Yohi silently shook her head.

She had merely closed her eyes and ears for the sake of her ambition. She was not a fool.

Dark Heaven had won over Baeksang, the Beast Miao King’s sworn younger brother, and waited for the right moment for several decades.

Yohi suddenly remembered the words spoken by the unidentified old man who had used the boulder as his coffin.

> “If you act rashly with the grand plan right before you, I will never forgive you.”

*The grand plan.*

He had definitely called it the grand plan.

Yohi sensed indescribable danger and anxiety in those two words. She also realized that their abduction had been a carefully calculated act.

The Western Yao Estate, massacred.

The Inner Palace, which must have been swept up in chaos.

Baeksang, who had built a support base comparable to—or even greater than—the Palace Lord’s.

And Dark Heaven, which had planned all of it.

Finding the answer was not difficult.

“Yohi?”

Heugung’s voice abruptly pulled Yohi from her thoughts. She bit her lip.

*If the thought that just crossed my mind is correct…*

The Inner Palace was no different from a demon-slaying battleground, with all sorts of fiends and sinister schemes lying in wait.

“We shouldn’t go to the Inner Palace. We have to go west.”

“The west? Could it be…”

“Yes. I intend to go to Boshan.”

Each tribe was scattered throughout Nanman, but they all had a base. Of them, Boshan was home to several thousand Yao people.

“By now, Baeksang has joined hands with Dark Heaven and taken control of the Inner Palace. If the tribal chieftains and the Tribal Grand Council decided to put him in power, even the Palace Lord wouldn’t be able to do anything.”

“Hmm.”

“Believe me. If we head to the Inner Palace now, we’ll be eliminated before we even manage to enter it.”

Heugung stared at Yohi with deeply sunken eyes.

“What if we head to Boshan?”

“I’m the Great Chieftain of the Yao people. Do I really need to say more?”

“How many warriors can you mobilize?”

“A thousand if I gather every last one. That’s nowhere near enough to stand against Baeksang with Dark Heaven at his back, but I don’t know if they’ll continue following him after learning what happened.”

“The people’s hearts will surely waver, and the warriors will defect.”

“I’ll send messenger pigeons and messengers to every tribe and village. Seven days at most. Within that time, all of Nanman will know about Baeksang’s atrocities.”

Heugung let out a quiet exclamation as Yohi continued speaking without hesitation.

“You’re truly astute. More so than the woman I knew.”

At those words, Yohi briefly forgot the situation and let out a quiet laugh.

“It feels strange hearing that from you. Especially since you’ve become a completely different person.”

“I had no choice. To avoid Baeksang’s eyes and ears, I had to hide myself first.”

Heugung calmly replied and handed her something.

Wrapped in yellow paper was a round pill.

“Take it.”

“What is this?”

“An antidote the Black Hand Fist Demon was carrying. I found it when I searched his clothes a moment ago. With our internal energy sealed like this, Baeksang’s warriors will hunt us down before we reach Boshan.”

Heugung was right.

No matter how outstanding a warrior was, they could not shake off a pursuit party unless they had trained in external arts. Yohi’s martial prowess was not particularly high to begin with.

SWISH.

Yohi did not hesitate. She chewed and swallowed the pill.

Its bitter taste made her brow wrinkle involuntarily, but it was still a hundred times better than dying without putting up a proper resistance even once.

“How long will it take us to reach Boshan?”

“We’re in Ailao Mountain, so… Three or four days should be enough. First, though, we need to get out of these Poisonblood Grounds.”

On the way there, they had seen venomous beasts they had never encountered before and a swamp made of deadly poison. They had already determined their location.

“By then, he should have woken up.”

“Yes, he should. If he wakes up, he’ll be an army unto himself.”

As Heugung quietly answered, he lifted Jin Taekyung’s body and slung it over his back.

Muyaho, who had been urinating on the dead Black Hand Fist Demon’s face, came running over and lowered his back.

“Grrr.”

Heugung gazed at the White Tiger’s blue-white eyes.

“Isn’t he truly strange?”

“Pardon?”

“I’m talking about this one the Young Palace Lord commands. Whenever I encountered him in the Inner Palace, he always bared his teeth at me. But now that Jin Taekyung is beside him, he’s as gentle as a lamb.”

“He must have opened his heart to him. They say spiritual creatures have always been able to recognize people.”

Yohi answered absentmindedly, then suddenly sensed that something was strange.

Heugung let out a quiet laugh.

“Yes. I think you’re right.”

THWACK! THUD.

Blood sprayed, and the enormous silver body tilted.

As Yohi stared blankly at the sight, Heugung’s voice reached her ears.

“Didn’t I tell you? I had to hide myself first.”
## Chapter artifact 687

# Chapter 687

SLICE. THUD!

For a moment, it seemed as though the world had stopped.

“Grrrk.”

A massive White Tiger lay collapsed like a rotten log, panting for breath. Jin Taekyung had lost consciousness completely.

And reflected in Yohi’s eyes was the sight of one man holding him in his arms and calmly continuing to speak.

“I told you. I should have hidden myself first.”

“……!”

Enlightenment and shock flashed through Yohi’s mind like lightning.

Her eyes, which had always held a deep and gentle light, flew wide open.

“Heugung, you!”

“You don’t call me big brother anymore. I rather liked hearing it.”

It had certainly been that way—until only a few shichen ago.

But Yohi would never be able to use that title again.

The middle-aged man with the kindly, heavyset build standing before her was not the Heugung she knew.

“Why?”

Her voice was filled with questions. Heugung shrugged and answered.

“It’s a simple story. Just as you used me, I used you.”

“……So you were on Baeksang’s side after all. You too.”

“That is a strange way to put it. Weren’t we all on the same side?”

“……!”

At the sight of Yohi stiffening, Heugung let out a quiet laugh.

“Don’t deny it. I was the person who watched you and Baeksang from closer than anyone else.”

“Then what about your sudden appearance at the Western Yao Estate?”

“That was all part of the plan. You, Jin Taekyung, the Beast Miao King, and even Baeksang. Of course, none of you knew my true identity… Though, when you think about it, calling us all allies is rather amusing.”

Yohi swallowed a low groan as she realized something from Heugung’s answer.

She could understand why she had not known. Although she had sided with Baeksang, she had only been an indirect accomplice whose involvement amounted to tacit acquiescence.

But the fact that he had hidden his identity even from Baeksang meant…

“You were watching us all this time. Baeksang and me.”

“Congratulations. You’ve taken one step toward the answer. Two more remain.”

“Was it the Demon Empress’s order?”

“Good. One final step.”

“You were the knife hidden up the Demon Empress’s sleeve in case something went wrong.”

Clap. Clap.

Heugung slowly brought his hands together and smiled.

“You’re quite perceptive. Correct. Though even I never dreamed things would go this far.”

Heugung slowly looked around.

The entire area had been reduced to ruins. His gaze passed over the two dead old monsters before finally coming to rest on one person.

“Jin Taekyung, the Blazing Flame Divine Dragon. The Third Young Master of the Jin Family of Taiyuan, and the heir of the Fire King who will one day inherit the orthodox lineage of the Fire Gate Clan.”

His voice continued in a low murmur.

A glint flashed in Heugung’s eyes as he stared at Jin, who was sleeping as though he had fainted in his arms.

“When I found him here, I realized things had gone wrong. If everything had proceeded according to plan, he would have been thrown into the underground prison—or the Demon Empress would already have taken him. But…”

Jin Taekyung had followed the tracking scent to the Poisonblood Grounds, killed the two Supreme Peak masters waiting for the Beast Miao King according to the Demon Empress’s arrangements, and survived.

“Fools. The Demon Empress told them to be so careful.”

Heugung muttered under his breath and spat out a wad of phlegm. Then, as though he had never done such a thing, he looked back at Yohi with a friendly smile.

“I don’t know whether capturing him alive is still the right choice after things have reached this point… But at least it’s fortunate that I can clean up the mess. Ah, before that, I suppose I should tell you that our destination has changed.”

“……The Inner Palace. You intend to head to the Inner Palace.”

At Yohi’s mutter, which sounded almost like a groan, Heugung nodded.

“If I return, something quite interesting will probably happen. Nanman will be thrown into turmoil by the testimony of the Great Chieftain who survived the Han Chinese’s wicked conspiracy, and every warrior and beast in this land will gather at the Inner Palace.”

“To fight the Central Plains.”

“But people aren’t fools. Everyone will wonder how you, a man who is only at the Peak realm, managed to escape from a deadly place all by yourself.”

“You’re quite sharp. But what if I were a Supreme Peak master?”

“What are you talking about…?”

“A Supreme Peak master whose martial prowess is great enough, by the public’s understanding, to subdue Jin Taekyung. Someone who also possesses virtue and prestige, and can embrace even those who would never side with Baeksang. Wouldn’t everyone believe such a person?”

At that moment, Yohi’s body stiffened.

“You… Don’t tell me!”

“That’s right.”

Heugung smiled faintly and released his internal energy.

From the Western Yao Estate until now, his internal energy had never once been sealed. It moved his bones and flesh and twisted his muscles.

CRACK. CRACK.

The eerie sounds of flesh being torn apart pierced Yohi’s ears.

Under the faint moonlight that had appeared between the clouds, Heugung’s shadow began to shift.

It grew taller. Stronger.

“Ghk.”

When every change was complete with a brief, pain-filled groan from Heugung, a short title slipped from Yohi’s frozen lips.

“……Palace Lord?”

In Yohi’s wide, disbelieving eyes, one person was reflected.

He was Heugung and the Beast Miao King. The Beast Miao King and, without a doubt, Heugung.

He gazed at his enlarged shadow and smiled with satisfaction.

“People think the essence of the Bone-Shrinking Technique lies solely in reducing one’s size. But when you reach its pinnacle and attain Great Completion, you can be reborn as an entirely different person.”

“……!”

“Now, let’s put it this way. I—or rather, the Beast Miao King—came here and subdued Jin Taekyung. You survived his wicked conspiracy, then returned to the Inner Palace and told everyone this.”

Heugung slowly continued, speaking to Yohi, who stared at him in a daze.

“That everything that has happened recently was a conspiracy by Jin Taekyung and the Murim Alliance to swallow Nanman whole. That we must mobilize every human and beast in this land, regardless of age or sex, and invade the Central Plains. What do you think?”

Yohi did not answer.

No, she could not answer. Fear and rage constricted her entire body, making it difficult to breathe and causing her vision to swim.

“H-How could you…”

“Ah. I forgot to tell you one thing. If you refuse my proposal, Boshan will run red with blood. And the four great tribes that dominate Nanman will become three.”

CRUNCH.

A thin line of blood trickled between Yohi’s red lips as she struggled to contain her rage.

She glared at Heugung with blazing eyes and spat out the words.

“You son of a bitch.”

“My heart aches. To think you would say such a thing to the man who will soon become your husband.”

“Shut your mouth. Who said I was going to marry you?”

“You probably will if you have to watch more than five thousand Yao people lose their heads one after another before your eyes.”

“……!”

“You’re a stubborn woman, and I’m a patient man. So I’ll wait. Until all five thousand heads have fallen to the ground.”

Heugung answered in a leisurely voice, then beamed at Yohi.

It was the same bright smile he had always worn, as though nothing had happened.

“I love you, Yohi.”

A chill rose over Yohi’s body, making every hair stand on end. She squeezed her eyes shut.

It was unbelievable.

This plan, whose beginning she could not even identify, and the true nature of the wastrel everyone had ignored.

And the dark shadow of Dark Heaven hanging over her head.

Haa.

A great many thoughts flashed through her mind along with her scattering breath.

A moment later, Yohi slowly opened her eyes, drew the flexible sword from her waist, and spoke.

“You filthy traitor.”

“A filthy traitor? Please don’t be so hard on yourself.”

“I won’t deny it. In the end, I was a traitor too. But will Dark Heaven—the Southern Heaven Demon Empress—allow you to live? What about the Yi people you lead?”

Her voice rang out like a sharp cry.

Heugung blinked for a moment, then suddenly burst into hearty laughter.

“That has nothing to do with me.”

“What?”

“More than forty years ago, when the former chieftain of the Yi people lost his life in the Great Faction War, his only legitimate son remaining in Nanman was only six years old. The strong men and women went to the battlefield. His mother died before she could even see her child’s face, and the only person left at his side was an old nurse whose eyes and ears had grown dim.”

“……!”

“Yohi.”

Heugung—or rather, the man who had become Heugung—continued with a faint smile.

“I have never been a traitor. Not for a single moment.”

CLANG.

The flexible sword slipped from Yohi’s grasp and struck the ground with a clatter.

She breathed heavily and tried to pick it up, but for some reason, her body would not obey.

*What is this?*

Yohi’s eyelids trembled.

Was it because of the upheaval in her heart caused by the succession of shocking revelations?

No.

She could not move because of the sinister, sticky energy that had already spread through every corner of her body.

“You…”

Her voice and vision faded weakly.

Heugung’s approaching figure wavered like a heat haze, and the voice that followed felt as though it were coming from far away.

“This is why I can’t help loving you. Not only are you dazzlingly beautiful, you’re this naïve too.”

“That wasn’t an antidote…”

“Unfortunately, I’m not the Beast Miao King, and even crossing swords with you would be too much for me. Please understand this sorry husband of yours, my dear wife. When you wake up again, I hope you’ll make the choice that is best for everyone.”

Yohi wanted to scream.

She wanted someone to come and kill this horrible man. She wanted to shout for someone to pull them out of this dark pit and stop the enormous conspiracy that would swallow Nanman whole.

But contrary to her desperate wishes, the scream that surged up through her throat could not escape her lips.

And Jin Taekyung, seized by the monster known as the sleep demon, did not open his eyes until the very end.

Then, in the next moment—

SWISH. THUD.

Heugung gently caught Yohi’s body as it collapsed like a puppet with its strings cut.

A smile appeared at the corner of his mouth, which now wore the face of the Beast Miao King.

“Even the way you sleep is beautiful.”

Heugung truly loved Yohi. The fact that she did not want him did not matter.

Yohi would eventually make the right choice.

And, in the end, she would come to love him.

Dark Heaven—the Southern Heaven Demon Empress—would keep her promise.

The price for hiding his identity and suffering through all these years would return to him tenfold, twentyfold.

Of course, before that…

*I need to finish this.*

Heugung kissed Yohi on the forehead, then slowly turned around.

He walked toward the culprit who had dared to jeopardize the grand plan.

*Jin Taekyung.*

He had been a variable no one could have predicted, and his existence had dealt a severe blow to the grand plan that stood on the verge of success.

Two Supreme Peak masters whose very presence could turn the tide of battle had been sacrificed.

But nothing had changed.

*The grand plan will succeed, and there are still hands and feet left to replace them.*

Jin Taekyung would not regain consciousness for at least several days.

If Heugung brought Yohi and Jin Taekyung back to the Inner Palace, everything would be over.

*Yes. It will be over.*

He smiled in satisfaction, passed the panting White Tiger, and grabbed Jin Taekyung by the nape to lift him up.

No—he was just about to lift him when it happened.

WHOOSH!

A bleak wind blew in from somewhere, and Heugung suddenly raised his head.

Beneath the pale moonlight, the shape of something appeared in his eyes.

“What is that…?”

At the very moment he began to voice his question—

SHWAAAASH!

The bleak wind turned into a blade and engulfed his entire body.
## Chapter artifact 688

# Chapter 688

Baeksang was staring at himself in a full-length mirror.

Unlike an ordinary mirror, the one Southern Heaven Demon Empress had given him was large enough to reflect his entire body, and its surface was smooth without a single scratch.

It was the finest mirror one could find—not only in Nanman, but even in the Central Plains.

But there was only one reason Baeksang was looking into it.

He could see the face of his son, who looked exactly like him.

*This has never happened before.*

It had been more than forty years. He had steadied himself countless times whenever he wavered, and made it all the way to this position.

And yet his heart was more shaken now than ever.

*That must mean this grand plan, which has endured for decades, is finally nearing its end.*

Just then, a door opened behind him, and a familiar face appeared.

Baeksang met the Captain of the Guards’ eyes in the mirror and spoke.

“Have they brought him?”

The Captain of the Guards had momentarily hesitated at the sight of his lord’s back, which was sunk deep in thought. He answered.

“He is on his way.”

“Then what is the matter?”

“An urgent report has arrived.”

“An urgent report…”

Baeksang let his words trail off and crooked a finger.

The Captain of the Guards understood the gesture and approached, then whispered in a low voice.

“Last night, a massive wildfire was spotted to the north, three hundred li away.”

“Ailao Mountain.”

“Yes.”

“The one who started the fire would be Jin Taekyung.”

“We need further confirmation, but considering everything that has happened so far, he is the most likely culprit.”

“It was Jin Taekyung. Once again, it seems glory-blinded moths have rushed toward the flames.”

“They say the small and midsized tribes near Ailao Mountain joined forces. They attacked him with five hundred warriors and one hundred beasts, but…”

Baeksang waved a hand, cutting him off.

There was no need to hear the rest.

Jin Taekyung was not someone five hundred hastily gathered stragglers could do anything about.

The saying *the few cannot overcome the many* meant different things depending on who the opponent was. Jin Taekyung clearly lay outside the equation.

“I can already guess the result. What happened to Jin Taekyung afterward?”

“They say he routed the warriors, then headed toward Ailao Mountain alone.”

“He must have had a purpose. Could it have been the Poisonblood Grounds?”

“The fire was too fierce to confirm anything that far in. The flames began at the mountain’s entrance and have already spread halfway up.”

“He must have made up his mind.”

Ailao Mountain was one of Nanman’s most renowned precipitous mountains.

Its terrain was harsh, its valleys deep, and its winding mountain range stretched for one hundred li. Ancient trees of unknown age covered it endlessly.

Now that a wildfire had settled over Ailao Mountain, it would take at least three full days and nights before there was even a sign of the flames dying down.

*Perhaps the entire mountain will be burned to ash.*

If it had been a coincidence, it was a remarkable one.

It had been more than two hundred years since wildfire had invaded Ailao Mountain. And the person who had used the entire mountain as firewood to destroy the Five Poisons Sect at that time had also belonged to the Fire Gate Clan.

*That was how Nanman found peace again.*

But would it happen that way this time, too?

Baeksang silently stared at his own face in the mirror before opening his mouth heavily.

“Evacuate every tribesperson living nearby. Select three thousand capable warriors and blockade Ailao Mountain.”

The Captain of the Guards had continued his report impassively, but a flicker of agitation crossed his face.

“Three thousand? Even though a general mobilization has already been declared throughout Nanman?”

“We must tie his feet, if only to prepare for the unexpected.”

“But my lord, even with that force, surrounding all of Ailao Mountain…”

“Ailao Mountain is vast, but it has few entrances that can actually be used. Take that into account when deploying them.”

After thinking for a moment, the Captain of the Guards bowed his head.

“Understood.”

“What is the situation with the other chieftains?”

“As I reported, five chieftains have disappeared. The warriors under the two chieftains who departed earlier with the scouting party have disappeared as well.”

“So it comes to this in the end. They must be refusing to accept reality.”

Baeksang murmured calmly.

The missing chieftains were the ones who had never switched sides.

Their loyalty to the Beast Miao King had been unshakable. Some of them had even spat at Baeksang while mocking him for trying to win them over.

“My lord, there is no doubt that they have betrayed us. It is not too late. We should send a pursuit party even now…”

At the Captain of the Guards’ suggestion, Baeksang shook his head.

“Not long ago, someone told me this: Just because one tree is diseased, it does not mean the whole forest is sick. All you have to do is thin out the diseased trees.”

“What do you mean…”

“For the past several hundred years, thirty-two tribes have coexisted on this land. But I often found myself wondering how long we would have to preserve that arrangement.”

“……!”

The Captain of the Guards’ eyes widened as he understood Baeksang’s meaning.

Baeksang continued in a deeply sunken voice.

“Thirty-two is too many for everyone to join their hearts and unite behind one purpose. From now on, it is time to thin out the diseased trees and put the forest in order.”

Expulsion.

Or elimination.

The meaning of the new power who had driven out the king that had ruled this land for so long and climbed onto the throne himself was unmistakable.

The Captain of the Guards stared at his lord with his mouth open, then spoke in a heavy voice.

“What should we do?”

“If they leave, let them go. If they return to their bases and rally their warriors, we will gain both justification and strength.”

The Captain of the Guards knew it as well.

The scales of power had tipped a long time ago.

But there was one person he was worried about.

“If the Palace Lord—or rather, Yayul Cheok—joins them, things will not proceed so easily.”

Baeksang stared quietly at the Captain of the Guards before speaking.

“When I lived in the Central Plains long ago, I heard an interesting story.”

“My lord?”

“It was about a monkey born from stone. Its temperament and strength were so violent and powerful that Shakyamuni, whom the monks of the Central Plains worshiped, stepped forward and proposed a wager. He asked whether the monkey could escape from the palm of his hand.”

His calm voice pierced the Captain of the Guards’ ears.

“The monkey snorted and accepted. It rode the clouds to the edge of the world, where it even scribbled graffiti on five pillars. But when it returned, it discovered that the pillars it had seen were Shakyamuni’s fingers.”

Baeksang slowly spread one hand toward the mirror.

The enormous Palace Lord’s Hall seemed to fit inside his palm.

The sky and rivers. The earth and mountains.

Even if it reflected all of Nanman, it would still fit there.

“Yayul Cheok is the same. Now that I have risen to this position, he will never escape.”

“That means…”

“We have information that he headed east. Personally lead one thousand Bai warriors and pursue Yayul Cheok.”

“Understood.”

At that moment, the Captain of the Guards bowed and moved his lips.

“I beg your pardon, but our opponent is the Beast Miao King. To prepare for the unexpected, perhaps you should use the Baekcheon Unit.[^1]”

But Baeksang silently shook his head.

The Baekcheon Unit was the blade he had secretly honed for decades.

He had to draw and wield it when it was most needed.

“That is all. We have a distinguished guest, so you may withdraw.”

He was speaking to the Captain of the Guards, but his gaze, which had been fixed on the mirror from the beginning, had already shifted to an old man standing before the open door.

“Then I shall take my leave.”

After confirming that the Captain of the Guards had left the Palace Lord’s Hall, Baeksang slowly turned around.

“You have arrived, Head Elder.”

It was a dispassionate greeting.

But the reply was a sharp one.

“Can you not shut that filthy mouth of yours?”

THUD.

An old man whose face was covered in age spots approached with a cane.

Every inch of exposed flesh was covered in wrinkles.

Anger that he could not hide flickered in his eyes, clouded with discharge.

“You wretched bastard.”

“It seems you overheard our conversation.”

“Do you think this old man cannot see through your pitch-black intentions? Was that not why you said it aloud?”

“If you mean Yayul Cheok—the criminal who defied the will of the Tribal Grand Council to save a murderer and then betrayed the Nanman Beast Palace—then yes.”

“You bastard!”

WHOOSH! CLACK.

The old man swung his cane with all his strength, but Baeksang caught it in one hand.

There was no notable force or internal energy in the blow.

Baeksang easily took the cane away, then lightly shook his sleeve.

An invisible force made the old man’s aged body sit down where it stood.

“You have aged considerably since I last saw you. Though your fiery temper seems unchanged.”

The old man’s body trembled.

“If I had known you would do something like this, I would have beaten you to death with these hands long ago.”

“But too much time has passed for that now. Yayul Cheok betrayed the Palace and fled, while the fate of the Miao people rests on a child who long ago was caught stealing fruit wine and received a harsh scolding from you.”

“……!”

“Now is the time to leave that stale past behind and think about the future. With the Chieftain and Lesser Chieftain gone, everything depends on what choice the Great Chieftain of the Miao people makes.”

The old man, the Head Elder of the Miao people, glared at Baeksang in silence before slowly parting his lips.

“So you finally seized Nanman with that hideous greed of yours.”

“Call it whatever you like. There is nothing I will not do to obtain what I desperately desire.”

“You are now the Palace Lord of the Nanman Beast Palace. What more do you want? Do you wish to obtain the Beast King Stone and become a god?”

Baeksang shook his head.

“I have no interest in some ancient sacred treasure passed down only by word of mouth. What I want now is the future—and your wise choice, Head Elder.”

“The boy I remember was not like this.”

“I changed. Just as everything else has.”

“The Palace Lord trusted you. Even though I told him to be so wary, he trusted his one and only sworn brother.”

“There is no need to repay every act of trust.”

“It is not too late. Even now…”

“I crossed the river a long time ago. Once you are riding a tiger, you cannot get off. Now it is your turn to climb onto the tiger’s back, Head Elder.”

CRACK.

The sound of bones shifting came from the old man’s tightly clenched, wrinkled fist.

“So in the end, you are telling this old man to betray the Palace Lord?”

“Of course not.”

Baeksang picked up a teacup as he continued.

“I want every member of the Miao people, including you, to betray him.”

“……!”

“You should read the flow of things carefully. If you want to save more than ten thousand of your people.”

“You bastard!”

“Remember this. This is the first and last offer.”

Baeksang tilted the teacup.

The Head Elder squeezed his eyes shut.

A short silence passed before his hoarse voice broke it.

“Impossible.”

CLACK.

Baeksang set down the teacup and stared at the Head Elder with deeply sunken eyes.

“Will you not regret that answer?”

“Kill me instead. Ask anyone among the Miao people, and the answer will be the same.”

“You have not disappointed my expectations.”

Baeksang answered briefly, then snapped his fingers.

The closed door opened, revealing Bai warriors.

“Lock up the entire Miao leadership in the underground prison, including the Head Elder.”

The Bai warriors bowed, seized the Head Elder from either side, and lifted him to his feet.

The old man, whose day of death was approaching, cried out in a ringing voice.

“Baeksang! You bastard! Are you not afraid of Heaven?”

By the time his scream had gradually faded into the distance, Baeksang was looking down at the empty teacup and muttering.

“What more could I fear? What brought me this far was also Heaven’s will.”

There had certainly been a time when he resented Heaven.

After the Great Faction War ended and Baeksang returned to Nanman, he had been drunk every day.

He had poured alcohol down his throat as though each day were his last, then despaired when the sunlight woke him the following morning.

*Why did you save me? Why?*

Those days had been more painful than death.

But he could not writhe in sorrow forever.

He had things to do.

Things he absolutely had to do.

Baeksang looked at the blue sky beyond the window and murmured inwardly.

*Is this truly your will? No… Have you ever watched over me even once?*

And as always, no answer came, no matter how long he waited.

Except for the unfamiliar voice that pierced his ears the next moment.

“Um… Shall I refill your tea?”

Baeksang turned his head toward the voice.

A pretty-looking maid stood before the half-open door, looking at him.

“There is no need.”

“But your cup is empty.”

“I said there was no need…”

His words suddenly trailed off.

After staring at the maid for a moment, Baeksang spoke.

“Come in.”

At his subdued command, the warriors who had been about to stop the maid withdrew, and the door closed firmly behind her.

The maid took quick, small steps until she reached Baeksang, then slowly tilted the teapot in her hand.

Trickle.

Steam rose, carrying the fragrance of tea through the room.

But why?

Why did this throbbing sensation feel as though he had inhaled Poison Mist?

Baeksang silently watched the teacup fill before suddenly speaking.

“Whose face is that, Demon Empress?”

The maid—or rather, Southern Heaven Demon Empress—smiled sweetly and answered.

“Some girl who worked in the Inner Palace. She was still so fresh and lively. Cute enough to be unbearable.”

“Did you kill her?”

“Oh my. Is that so important?”

“That…”

“How interesting. Hundreds of people have already died, and you are worried about the life of one maid.”

Baeksang answered in a calm voice after a moment of silence.

“I was merely asking because I wondered whether it might interfere with the plan. Things that happen in the Inner Palace are discovered quickly.”

“Aha. Well, if that is what you mean…”

The Southern Heaven Demon Empress smiled coyly and picked up the teacup.

“The thing you are worried about will not happen. If anything has gone wrong, it would be at Ailao Mountain, not in the Inner Palace.”

“If you mean Ailao Mountain, then could it be…”

“Yes. Jin Taekyung. That child caused a little trouble. The fact that there has been no contact yet makes it certain.”

Baeksang thought for a moment before speaking.

“It was a trap?”

“That’s right. A trap laid to catch the old tiger who had left the Palace. I never expected the young tiger to get caught in it instead.”

CLICK.

The Southern Heaven Demon Empress set down her teacup and continued in a voice filled with amusement.

“Of course, I never expected that young tiger to be strong enough to break the trap, either.”

“It must have been a thorough trap, if you were so confident in it, Demon Empress.”

“Two Supreme Peak masters. One was the Black Hand Fist Demon, and the other…”

The Southern Heaven Demon Empress stopped speaking and smiled at Baeksang.

“Anyway, he was strong. Much stronger than the Black Hand Fist Demon.”

“……!”

“It is astonishing. I thought those two would be able to deal with the Beast Miao King. It seems the Lord of Heaven was not interested in that child for no reason.”

For Baeksang, it was one shock after another.

Jin Taekyung had not only killed two Supreme Peak masters single-handedly—the Lord of Heaven himself was also interested in him.

At the same time, Baeksang realized that his own judgment had not been wrong.

*Jin Taekyung.*

The face of an incomprehensible young man flashed before his eyes.

Baeksang looked at the Southern Heaven Demon Empress, who was smiling at him, and spoke.

“From here on, you will move personally, Demon Empress.”

A Supreme Peak master was a powerful asset.

With two such masters dead, Baeksang thought it was inevitable that the Southern Heaven Demon Empress would step forward.

At least, that was what he thought until he heard her answer the next moment.

“No? Why would I?”

The Southern Heaven Demon Empress let out a quiet laugh and continued.

“I do not have time to worry about that. Even if one of the major pieces has died, the current situation will not be overturned. What matters is the grand plan.”

“Do you mean…”

“The Beast Miao King and Jin Taekyung are no longer important. Strengthen the defenses of the Inner Palace and Outer Palace. Then gather every available force.”

The Southern Heaven Demon Empress rose from her seat and began walking as though she were dancing.

Her voice, filled with delight and joy, pierced Baeksang’s ears.

“Three days. Three days at the latest.”

“……!”

“Prepare yourself. On that day, everything will begin—and end.”

THUD.

The door opened.

Then closed.

But even after a long time had passed, Baeksang remained frozen in place, unable to move.

That day was drawing near.

The day he had longed for more than anyone else in the world—and feared more than anyone else.

[^1]: Baeksang’s secret elite unit, cultivated over decades.
## Chapter artifact 689

# Chapter 689

Drip. Drip.

It was cold.

That was the first thought that occurred to Yohi when she opened her eyes.

As she stared blankly at the drops of water falling onto her forehead, memories she had briefly forgotten began returning one by one.

*This is…*

Only now did she remember. Who she was. What kind of life she had lived. What had happened at the Western Yao Estate, and what she had seen in the Poisonblood Grounds.

And…

*“I love you, Yohi.”*

Just remembering the face and voice of that man made her shudder. Behind him lay the massive White Tiger and a young man.

All of it—

“Gasp!”

Yohi shot upright like lightning, barely swallowing the scream that tried to escape between her lips.

She had finally recalled everything that had happened before she collapsed. Overcome by fear and wariness, she looked around.

*Where am I?*

It was an unfamiliar space. Blurred darkness and silence that had settled all around her. There was no real light, making it impossible to distinguish anything clearly, but one thing was certain: she was blocked in on every side.

As though someone had prepared a prison.

*Heugung.*

No—the man who had stolen the name Heugung.

Remembering the man whose entire life had been a lie, Yohi instinctively groped at her waist.

She was looking for the flexible sword she always wore wrapped around her waist like a belt in case of emergencies. But contrary to her hopes, all her hand found was silk soaked with blood and dirt.

*Ah. Back then.*

She remembered losing her flexible sword after being drugged by an unidentified substance.

She had never taken the antidote in the first place, so naturally, her internal energy remained sealed…

“Huh?”

Yohi unconsciously let out a sound and hurriedly covered her mouth. But the surprise she had failed to conceal was plainly visible in her wide, round eyes.

*How?*

After forcing herself to calm down, Yohi examined her body once, twice, then a third time, just in case.

She soon became certain.

*The seal on my internal energy… It’s gone.*

There was no doubt. She could feel the internal energy she had accumulated by consuming all kinds of elixirs filling her lower dantian.

The problem was why—and how.

*Everyone, including me, should have been captured by Heugung.*

Yohi could not understand the situation at all.

Not why she had been left alone in this sealed space, nor why the seal on her internal energy had been removed.

At the final moment, no one had been capable of stopping Heugung.

Jin Taekyung had suffered severe injuries and would not wake for at least several days. And the spiritual creature White Tiger, which was fully capable of matching a Peak master, had been on the verge of death after an unexpected ambush.

There was no need to mention Yohi, who had collapsed without even being able to swing her sword once because of the pill’s effects.

*Then how can the seal be gone?*

She had not even been bound with the usual rope or chains. Even if Yohi’s martial arts were not particularly impressive, she was still at the early stage of the Peak realm.

This was far too clumsy and strange a measure to have been Dark Heaven’s doing.

*Could it be…?*

Yohi swallowed the words that followed with a dry gulp, then carefully rose and examined her surroundings.

By then, her eyes had grown accustomed to the darkness. Once she added her internal energy to the mix, her enhanced vision began to make out what lay beyond it.

*This is…*

The moment she confirmed the nature of the space where she stood, Yohi felt the breath catch in her throat.

It was enormous—too enormous to believe it had been made to imprison a single person.

But if it had merely been wide, it would not have left her so breathless. The area, which seemed to stretch several hundred zhang in every direction, was not important.

The problem was that cold, damp stone covered everything around her, from the floor to the walls and even the ceiling.

Like an impregnable fortress that no one could enter or leave.

*What in the world is this place?*

Yohi was staring speechlessly at the rock filling the space and the thick vines covering it when—

Swoooosh.

The vines swayed in a wind that blew in from somewhere.

Yohi stood with her mouth open, feeling the cool breeze brush over her entire body. Then she suddenly sensed something falling from above and reached out.

Rustle. Tap.

Something landed between her slender fingers.

It had brushed against her fine strands of hair before falling, and its identity was simple: a leaf that had broken off from one of the vines.

Unlike the leaves she had seen in the Poisonblood Grounds, this one was green and brimming with life.

That was when a bolt of realization flashed through Yohi’s mind.

*Wait. Wind?*

If this were a sealed space, no wind could blow through it.

That meant there had to be an opening.

And not just any opening. It had to be large enough for a powerful wind to blow through and shake those thick vines.

But contrary to Yohi’s guess, she could not find a gap no matter how thoroughly she searched.

*That’s impossible.*

She touched the stone blocking her on every side and struck it with her internal energy.

That was not all. On the off chance it might help, she even imitated the Wall Lizard Technique, a martial art she had never learned, and climbed up the vines.

Perhaps there was a gap above that would allow her to escape.

But in the end, every attempt came to nothing.

She no longer felt the despair of having been captured by Dark Heaven, but rather the helpless bewilderment of finding herself in an incomprehensible place.

*There has to be an exit, at the very least.*

And that was exactly how it was.

Yohi had wandered around for more than two shichen after waking up, yet she had not found anything resembling an exit, let alone a gap.

Then who had imprisoned her here—and how?

Overcome with despair, Yohi slumped down and leaned her back against the stone wall.

The warm, soft sensation that traveled up her back made her feel slightly better.

“Hm?”

Something was strange.

After blinking for a moment, Yohi slowly tilted her head back without changing her position.

And in the faint darkness, her eyes met a pair of blue-white eyes looking down at her.

“Ah.”

—Grrr.

A suffocating silence descended in an instant.

Yohi slowly rose to her feet, looking back and forth between the cliff-like rock wall behind her and the massive White Tiger, whose upper body protruded from it as though the rest of its body had been cut away.

Then she thought:

*What is this?*

Yohi did her best to calmly organize the situation.

First. This was an enormous space of unknown origin.

Second. Just like she was trapped inside a cliff, the sky was blocked off by rock walls, and there was no visible exit.

Third. A White Tiger with half its body cut off had appeared from the rock wall. No—it had suddenly burst out of it.

Fourth. In a situation like this, there were only two possible answers.

A dream.

Or the afterlife.

Yohi did not hesitate. She slammed her head against the rock wall.

Thud.

The inside of her skull rang, but she did not wake up.

Which meant it had to be the latter.

And no wonder. The sight of that White Tiger floating around with only its upper body showing was strangely familiar.

*It’s him.*

Snow-white fur, white enough to be called silver, and blue-white eyes.

There was no mistake. It was the White Tiger cherished by the Young Palace Lord, Yayul Mok.

Muyaho should already have been dead. Yet here it was, perfectly healthy, without a single injury, calmly tilting its head to one side.

That convinced Yohi that this was the afterlife.

*No wonder I couldn’t find an exit.*

She had not known. This was her first time in the afterlife.

It felt as though a hopelessly tangled ball of thread were finally coming undone. As enlightenment arrived at last, Yohi’s shoulders began to shake.

“Sniff. Sob. You fucking son of a bitch, Heugung…”

The crisis facing Nanman? The dignity she was supposed to uphold as Great Chieftain of the Yao people?

But what did any of that matter?

She was already dead.

The only gaze watching her now belonged to a half-severed tiger ghost.

And when she remembered her mother, who had died twenty years ago, tears began streaming down her face.

“Waaah! Waaaaah!”

At the cry that sounded almost like the roar of a wild beast, Muyaho approached her. Wearing an expression that seemed to ask whether she might have been one of its kind, the White Tiger began licking her tears.

—Grrr.

Its rough tongue swept across her entire face.

It did seem strange that her senses were so vivid for someone who had already become a ghost, but now that she thought about it, people who claimed the dead lost all sensation were probably just people who had never been to the afterlife.

Yohi buried her face in Muyaho’s soft fur and sobbed.

At least, that was what she did until her hand grasped something soft and swishing.

Grab.

—Hiss!

At first, she had been too busy crying to pay attention. Then she wondered what it was.

When she lifted her head at Muyaho’s sharp cry, Yohi saw it.

The long, snow-white tail of the White Tiger was clutched in her hand.

*What? It’s a tail. I thought it was something else.*

Yohi muttered inwardly and buried her face in the fur again.

A moment later, she lifted her head once more.

One shocking fact had struck her in the back of the head.

*Wait. Why does it have a tail?*

Under normal circumstances, there would have been nothing strange about it. Ordinary tigers had tails. Even the rats swarming through the storerooms at the Western Yao Estate had tails.

But the fact that the White Tiger ghost, which had been floating around with only its upper body visible moments ago, had now become whole was an entirely different matter to Yohi.

*Could it be?*

Yohi hurriedly rose and reached toward the rock wall where Muyaho had first appeared.

Tap.

Just as she had discovered while examining it, the stone was cold and hard. She could not guess its thickness, and there was no visible gap.

But it was too soon to be disappointed.

*There’s something here that I don’t know about. There has to be.*

Her reason, now that she had regained her composure, told her so.

This was neither a dream nor the afterlife. It was simply a bizarre, uncanny situation that could not easily be understood by the human mind.

As though it had read Yohi’s thoughts, Muyaho, which had been circling her, made its move.

—Grrrr.

The massive White Tiger bent its lower body at an angle.

Yohi vaguely understood the meaning in its clear blue-white eyes and asked with a doubtful expression.

“You want me to ride you? On your back?”

—Grrr.

“Hah.”

She had heard that it was intelligent, but she had never imagined it was this intelligent.

Yohi looked at the White Tiger before her with renewed amazement, then carefully climbed onto its back.

When she gripped its snow-white fur, the tiger extended one massive forepaw toward the rock wall.

Clomp.

It was so enormous that a single step brought the rock wall right in front of them. Yohi squeezed her eyes shut.

*Please.*

At the moment she silently repeated the plea with all her heart—

Swoooosh!

Along with a strange sensation, as though she were being sucked into somewhere, Yohi slowly opened her eyes.

An involuntary exclamation escaped her lips.

“Ah.”

It was endlessly bright and warm.

Light instead of darkness. Trees overflowing with life instead of cold rock walls. A place filled with every kind of flower instead of vines.

It was an entirely new world.

For a moment, Yohi was so immersed in its peace and beauty that she forgot everything else.

“W-What is this place…?”

Yohi let her question trail off, but this time, Muyaho did not answer.

The snow-white White Tiger shot forward without hesitation, heading down a path where flowers and plants grew together.

Tap-tap. Swoosh!

A refreshing wind scattered around them, wrapping around their entire bodies. At the same time, beyond the scenery rushing past them, countless animals of every shape and color watched them with curious eyes.

Mountain birds had built nests in trees that stretched impossibly high. A roe deer and a wild boar basked together in the sunlight amid the thick grass.

There was even a bear lending the mismatched pair its body to lean against.

*Good heavens. What did I just see?*

But that thought echoing through Yohi’s mind was erased in an instant.

Why was the food chain being ignored? She had no idea.

No—it did not matter.

Simply by existing in this space, everything felt completely natural.

*This… This is truly impossible.*

It was then that two words suddenly flashed through Yohi’s mind.

*Dark arts.*

At that moment, the path that had seemed as though it would continue forever came to an end, revealing a small pond.

And there—

Someone was there.

“Jin Taekyung!”

There was no mistake.

It was him.

His well-balanced, muscular body and red armor covering his upper body stood out clearly even from a distance. He was collapsed, half-submerged in the clear water.

Only about ten zhang remained between them.

But contrary to Yohi’s desperate urgency, the White Tiger’s paws, which had moved forward without pause until now, were fixed in place as though nailed to the ground.

—Grrrr.

It was a low growl, as though calling out to someone.

Yohi sensed something and turned her head in the direction of Muyaho’s blue-white gaze.

She saw it.

No—she sensed it before she even saw it.

Swoooosh.

Along with a cool wind carrying an unknown energy, green leaves began raining down from an enormous tree unlike any she had ever seen.

And at that moment—

Rustle.

Beneath the wide shadow cast by the great tree, a Black Tiger that resembled the darkness rose to its feet.

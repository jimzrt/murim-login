# Checkpoint Review — 710–714

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

# Chapters 710–714

## Plot

Jeok Cheongang arrives at the battlefield and reveals himself as the Blood Monk. When his Flame Divine Palm threatens to kill the Southern Heaven Demon Empress—and Jin Taekyung with her—Jin shields her and tears out her throat before being struck down. Five System level-ups restore Jin, exposing the System to Jeok. The two reconcile and begin treating the survivors, finding only about thirty living Nanman warriors and Baekcheon Unit members.

The guardian spirit explains that the sacred stone can withstand and purify the rift’s darkness. It absorbs the stone and enters the spreading rift, asking Jin and Jeok to kill it if corruption takes hold. As the stone purifies the demonic qi, the guardian spirit remembers its three-hundred-year friendship with Yayul Cheon and realizes that its true mission is protecting the land, not merely guarding the stone. Its sacrifice seals the rift, but it mutates into a divine-beast-like tiger. At its request, Jin and Jeok kill it.

Baeksang survives the collapse and confesses that he knowingly aided Dark Heaven because the Southern Heaven Demon Empress promised to preserve his supposedly dead son, Baekhwi. He had sacrificed Nanman’s warriors and beasts while creating the Baekcheon Unit as a contingency to stop the catastrophe. After warning that Dark Heaven will eventually devour Nanman and declaring his loyalty to the Lord of Heaven, Baeksang asks the Beast Miao King to execute him. The Beast Miao King fulfills their childhood vow with a single punch.

Jin covers Baeksang’s face with Baekcheon, then collapses and remains unconscious for seven days. He awakens under medical care to find Jeok violently demanding answers from a physician and calling for the Beast Miao King. Jin’s dreams feature absurd battles against Dark Heaven and the people he failed to save.

## Continuity

- The rift is sealed; its demonic qi has vanished, and the sacred stone is purifying the remaining corrupted energy.
- The guardian spirit sacrificed itself to seal the rift, mutated, and was killed by Jin Taekyung and Jeok Cheongang at its own request.
- The Southern Heaven Demon Empress is dead.
- Baeksang knowingly served Dark Heaven’s plan and sacrificed Nanman’s forces, while secretly creating the Baekcheon Unit to provide a chance of stopping the catastrophe.
- Baeksang is dead, executed by the Beast Miao King at his own request.
- Baeksang’s warning claims that Dark Heaven will eventually devour Nanman.
- Dark Heaven has kept Baekhwi alive in a deep sleep; Baeksang accepted the Empress’s bargain in hopes of recovering him.
- Jin recovered through five System level-ups after Jeok’s Flame Divine Palm and was unconscious for seven days after Baeksang’s death.
- The Beast Miao King survived but remains severely injured; the surviving Nanman and Baekcheon forces number only about thirty.
- The condition of Baekhwi and whether he can be recovered remain unresolved.

## Translation Decisions

- Retain **Blood Monk**, **Flame Divine Palm**, **Old Master**, **Will**, **sacred stone**, **rift**, **demonic qi**, and **Baekcheon**.
- Render **Blazing Flame Divine Palm**, **Sacrifice and Rest**, and **Mutated Guardian Spirit** as established.
- Continue rendering the guardian spirit’s **의념** as **Will**.
- Render the sacred stone’s cleansing effect as **purification**.
- Retain **Eastern Heaven Demon Lord** and **East-West Heaven Demon Empress** for the directional dream titles.

## Durable state

{
  "active_continuity": [
    "The rift has closed, demonic qi has disappeared, and the sacred stone is purifying the corrupted energy.",
    "The mutated guardian spirit was killed by Jin Taekyung and Jeok Cheongang after sacrificing itself and requesting death.",
    "The Southern Heaven Demon Empress is dead.",
    "Baeksang knowingly served Dark Heaven's plan and sacrificed Nanman's forces to advance it.",
    "Baeksang is dead, having been killed by the Beast Miao King at his own request.",
    "Dark Heaven has kept Baekhwi alive in a deep sleep, and Baeksang accepted the Southern Heaven Demon Empress's bargain to recover him.",
    "Baeksang created the Baekcheon Unit as a contingency to stop the catastrophe.",
    "Jin Taekyung was unconscious for seven days after Baeksang's death and has now awakened.",
    "Baeksang's final public warning claimed that Dark Heaven will eventually devour Nanman."
  ],
  "continuity_sources": [
    714
  ],
  "open_questions": [
    "What is Baekhwi's condition, and can he be recovered from his deep sleep?"
  ],
  "safe_through": 714,
  "temporary_decisions": [
    "Continue rendering the guardian spirit's 의념 as Will.",
    "Render the sacred stone's cleansing effect as purification.",
    "Retain Old Master as Jin Taekyung's address to Jeok Cheongang.",
    "Retain established renderings of Blazing Flame Divine Palm and Sacrifice and Rest.",
    "Render 백천 as Baekcheon and the new directional titles as Eastern Heaven Demon Lord and East-West Heaven Demon Empress."
  ],
  "version": 1
}

## Reading copies

## Chapter artifact 710

# Chapter 710

He could feel it. The death hanging right before his eyes.

His blurred vision could no longer distinguish even the shapes of things, and his once-sharp senses had finished preparing to leave his body.

Within that dark, hazy consciousness, Jin Taekyung thought.

*No doubt about it.*

*This is a dream. Or maybe a hallucination brought on by the death drawing near.*

There was no other way to explain the voice coming from behind him.

“Just whose body do you think you’re laying a hand on, you fucking bitch?”

And yet… it sounded so much like him.

The shrill voice, sharp enough to sound irritable, and those thick curses both brought one person to mind. Even though he knew that person could not possibly be here. Even while he scolded himself for entertaining such an absurd thought, it filled him with foolish hope.

*Has it really come time for me to die?*

At the exact moment that empty mutter echoed through his mind—

“So… how long do you intend to keep sitting there with your head in the clouds?”

“……!”

Jin Taekyung’s eyelids, which had been slowly closing, stopped abruptly.

A massive shock that arrived in an instant awakened his fading consciousness, and his distant senses returned.

*No way.*

*No. It can’t be.*

That was impossible. *He* was supposed to be somewhere in the distant Central Plains.

But someone had once said that hope was what broke human beings down—and what raised them back up again. So Jin Taekyung clung to that invisible thread of hope and opened his eyes.

And then he saw.

“Ah. Aah…”

The Southern Heaven Demon Empress, staggering with both arms gone.

And a single Zen staff planted at an angle beside her as she stood gripped by shock and confusion.

Clatter.

The rings hanging from the Zen staff gave off a terrible racket.

Feeling the Scorching Yang Qi flowing from the staff, which had been heated to a reddish glow, Jin Taekyung opened his mouth with a faint smile.

“Well… you could’ve come a little sooner.”

His voice was so faint that it could be heard only by someone listening right beside him.

But the owner of the Zen staff was different.

He could have heard Jin Taekyung’s voice even from several hundred jang away. No—even from several hundred ri away.

Not with his ears.

With his heart.

With the heart he held for his one and only Disciple.

“I can be a little late, can’t I? What’s with the abuse, you brat?”

Contrary to what he felt inside, Blood Monk—or rather, Fire King Jeok Cheongang—answered gruffly as he took a step forward.

Thud.

And then, the next moment—

Whoosh!

In the blackout that came after the entire stage had ended, a flame larger and more ferocious than anything else burst into being.

Kraaaaaash!

Flame Divine Palm.

A wave of fire filled with horrifying heat advanced through the darkness, devouring it as it went. Without hesitation and without end, it moved for the sole purpose of burning one being.

*Ah.*

The Southern Heaven Demon Empress stared at the approaching heat with hollow eyes.

Neither a groan nor a scream escaped her lips. Her feet were fixed to the ground as though nailed there, and the pain in her missing arms felt distant.

*I have to dodge. Somehow, I have to dodge…*

Her body could not accept the cry that continued inside her head.

No—perhaps everything had ended at the moment she lost her one remaining arm.

The Zen staff that had moved so quickly she could have mistaken it for a flash of light, carrying overwhelming heat, had turned more than just her arm into ash.

Her innate qi.

Even that final handful of strength she had saved to adorn the end of only one person’s life had been stolen away. Indifferently, and mercilessly.

As she observed herself, with not even enough strength left to take a single step, the Southern Heaven Demon Empress finally understood.

*It’s over.*

Her life had been truly long. She did not know exactly where it had begun, but this place, today, would be the period at its end.

Even so, if she had one regret left until the very end, it would only be that she had failed to personally cut off Jin Taekyung’s breath.

*But… it’s all right.*

She did not know why, or because of what trick of fate, Fire King Jeok Cheongang had come here.

But just as she would fall here, Jin Taekyung would be unable to escape death either.

Even if the one who had come was not the Fire King but the Great Firmament Immortal, that fact would not change.

That one unshakable certainty soothed the heart of the Southern Heaven Demon Empress as she accepted the flames.

*Lord of Heaven.*

The call echoed softly within her heart.

Her thoughts had been long, but the moment was brief. The flames shot over Jin Taekyung’s kneeling head opened their maw toward the Southern Heaven Demon Empress.

Whoooosh!

As she watched the light-flames pouring down and melting the darkness, the Southern Heaven Demon Empress closed her eyes.

No—she tried to close them.

And she would have, if someone had not suddenly thrown themselves over her body—too drained to move so much as a finger—just as everything turned white.

Whump!

Within that brief instant, split and split again into smaller pieces, the Southern Heaven Demon Empress saw everything clearly.

“……!”

Jin Taekyung’s face, pale with the approach of death, and his lips slowly parting in a world that had grown sluggish.

And then—

Crack!

Along with a sharp pain spreading from her throat, the Southern Heaven Demon Empress’s vision was swallowed by darkness.

* * *

It was both an unavoidable reality and an enlightenment that came like a flash of light.

*If the Southern Heaven Demon Empress dies now, I die too.*

The greatest reason I’d been able to survive while fighting experts a level above me was the recovery that came with leveling up.

No matter how outstanding my Muscles and Bones were or how many stats I’d raised, they couldn’t stop certain death.

Especially not when, like now, my acupoints had been blown apart and my duodenum—which was supposed to perform its proper function in its proper place—had gone AWOL like a soldier wandering outside his assigned area.

But what if the Southern Heaven Demon Empress died at someone else’s hands in a situation like this?

Then I’d be fucked too.

In the end, the only choice left to me in that final moment was one.

Tank it.

*Fuck.*

Swallowing a low curse, I squeezed out every last ounce of strength and threw myself forward.

No—it would be more accurate to say that I barely managed to raise my body and throw myself over the Southern Heaven Demon Empress.

Crack!

“……!”

I saw her eyes, which had been closing as though in resignation, snap open.

Shock and confusion swirled within the Southern Heaven Demon Empress’s eyes. They seemed to ask a question in place of her voice.

*Why?*

But I had neither a reason to answer nor the time to do so.

If I’d had that much strength and leisure left, I would have picked up White Flame, which had fallen a few steps away, or pulled another weapon from my Inventory and driven it into the Southern Heaven Demon Empress’s heart.

But… damn it. While clinging to consciousness that felt ready to snap at any moment, this was the best attack I could manage.

Crack!

Wrinkled skin mottled with age spots tore away helplessly. The metallic tang of blood filled my mouth, wetting my parched lips.

Of all the attacks I had used in every battle I’d fought so far, this was the most primal and primitive.

Which was why it was more desperate than any attack before it.

And after taking a huge bite out of the Southern Heaven Demon Empress’s throat, I felt an enormous heat reach me from behind.

Along with someone’s scream.

“No—!”

Whoosh! Boom!

An immense impact struck my back. The roar that swallowed even the scream that had been about to continue swept through the surroundings along with horrifying heat, and I felt my body float before I was thrown away.

*Ah.*

Who had said that the greatest pain a human being could feel was burning pain?

They had been absolutely right.

Horrifying pain, too terrible even for a scream to escape, seized my entire body.

My vision had turned pure white, leaving me unable to distinguish even an inch in front of me, and my body, thrown away by the massive impact, did nothing but cut through the air at tremendous speed.

Screeeeeech—boom!

The fierce sound of air splitting, which seemed as though it would continue forever, finally ended, and something rough and hard struck my entire body.

No. It would be more accurate to say that my body, shot forward like a ray of light, smashed through the rubble and buried itself in it.

Cough.

With a cough, what little blood I had left trickled from the corner of my mouth.

My eardrums had already burst, and the buzzing of a swarm of bees roared in my ears. Beyond my blurred vision, the Southern Heaven Demon Empress lay sprawled helplessly, while someone’s silhouette wavered like a heat haze.

“No!”

And at the moment a scream-like cry rang out—

Ding.

Along with the clear ringing of a bell in my ear, a gentle warmth enveloped me.

* * *

Screeeeeech!

At that moment, Jeok Cheongang threw himself forward with all his strength, his heart filled with despair.

*No. It can’t be.*

Each step was heavy.

His heart, aged by more than a century of life, was pounding more violently than ever, and his eyes, fixed on the person rapidly drawing closer, trembled.

Jin Taekyung.

The second—and only—Disciple of his life.

The one and only ember who had suddenly entered the life of a man who had wanted nothing but death and made him realize that he had a reason to live.

*But why? Why the hell would he do that?*

He felt as though he were about to vomit blood.

What he had unleashed at the Southern Heaven Demon Empress was the Flame Divine Palm, driven to a staggering twelve-tenths of its normal limit.

And Jin Taekyung had suddenly blocked that horrifying heat, powerful enough to melt steel.

*You crazy bastard. You stupid bastard!*

He did not know why. No, the reason did not matter.

The curses he had been unable to spit out were directed at himself as well.

The choice made by Jin Taekyung, his one and only Disciple, had always been right. There had always been a reason for it.

But the sorrow and self-reproach of losing Jin Taekyung because of his own hasty judgment tore Jeok Cheongang’s heart to shreds.

“No!”

Along with that scream, the old Master’s footsteps finally stopped before his Disciple.

“Taekyung! You bastard!”

But no answer came to his desperate call.

Jeok Cheongang saw Jin Taekyung lying there with his eyes closed, breathing so faintly that it seemed his breath might stop at any moment, and his heart sank with a heavy thud.

*Ah.*

The shock made his vision swim.

An armor shattered so thoroughly that almost none of its original shape remained. Limbs twisted at unnatural angles.

And on top of that, flesh and bones that had melted or broken beneath the heat of the Flame Divine Palm.

Perhaps thanks to the armor, he was miraculously still breathing.

But that was all.

The time remaining to that young boy amounted to no more than moments.

That fact would not change even if Jeok Cheongang poured every last bit of his internal energy into him.

No—it would only prolong his pain.

Tap.

The hand reaching to take Jin Taekyung’s wrist pulse trembled in midair.

*…Dying? He’s dying? That boy?*

Unable to bear watching Jin Taekyung die before his eyes in this unbelievable reality, Jeok Cheongang squeezed his eyes shut.

He had witnessed countless deaths throughout his life.

Sometimes he had watched from far away. Sometimes he had personally cut off someone’s breath with these hands.

But… Jin Taekyung’s death was different.

That child’s death was different.

He had barely passed twenty. Unlike Jeok Cheongang, he had an abundance of days left to live and happiness left to enjoy.

“Then what could have been… what could have been so urgent that you had to leave already? Why!”

Jeok Cheongang cried out as though he were spitting blood.

He held Jin Taekyung’s hand, which had been half melted by his own martial arts. Holding that hand, still bearing the marks of those horrific injuries, he wept his heart out…

*Huh?*

Jeok Cheongang opened his eyes when he felt something strange beneath his fingers.

His tear-filled eyes reflected Jin Taekyung’s hand.

The back of it was pale and smooth like a newborn baby’s, and yet the veins stood out in thick ridges.

“……?”

It was strange. A moment ago, the flesh had clearly been melted and fused together.

He even thought he had seen some of the bone.

*What the hell is this?*

No matter how he thought about it, there were only two possibilities.

Either those damned infirmities of old age had returned, or else…

Gulp.

After swallowing dryly without realizing it, Jeok Cheongang slowly raised his head.

And then, the next moment, he saw.

A pair of eyes gazing back at him with interest.

“……?”

“……?”

“……!”

“……!”

After a brief exchange of glances, Jeok Cheongang froze rigidly.

Facing him, Jin Taekyung wiggled his fingers sheepishly.

“Um, how about you let go of my hand first, then we talk?”
## Chapter artifact 711

# Chapter 711

Sometimes, a certain kind of silence can take the place of countless emotions and words.

Just like now.

“Um… how about you let go of my hand first, then we talk?”

“……”

To give you the conclusion first, Jeok Cheongang neither let go of my hand nor answered. He simply stared blankly, sweeping his gaze over my face and every part of my body like a man who had lost his soul.

*What the hell is with this guy? Could all this really be a dream?*

That was exactly what his eyes seemed to say, and I understood Jeok Cheongang’s feelings perfectly.

*He can’t possibly react any other way.*

The guy who had been dying right before his eyes had come back to life perfectly intact.

Even that prophet from the neighborhood over who was said to have risen three days after being nailed to a cross still had wounds on his palms. But five level-ups had turned me into a baby’s smooth, unblemished skin.

And Jeok Cheongang had watched the whole thing happen.

Smack!

A crisp sound rang out of nowhere.

Jeok Cheongang had slapped himself across the face with all his strength. He blinked at me, then opened his mouth with a solemn expression.

“Let this old man ask you one thing. Am I dreaming right now?”

I answered carefully.

“No.”

“No matter how I think about it, this feels like a dream.”

“Then try slapping yourself one more time.”

Smack!

Of course he didn’t hesitate.

He must have hit himself pretty damn hard.

Jeok Cheongang spat out a thick mouthful of blood that had gathered in his mouth, then took a deep breath.

“……Damn it. It isn’t a dream. Then is this an illusion created by a Mystic Gate Formation?”

“Uh, I don’t think so. If I were an illusion, whose hand would the Old Master be holding right now?”

“A Dark Heaven sorcerer has overlaid your illusion on himself. Or perhaps it’s the Southern Heaven Demon Empress, whom we thought was dead. They must be preparing a killing blow while this old man is caught in the illusion.”

“Your imagination is incredible. Have you gone senile?”

“Judging by the way you talk, you’re unmistakably you. Haaah. This is truly driving me mad.”

“It’s driving me mad too.”

I was serious.

I had kept the System completely hidden until now, but now I’d been caught red-handed with no way to deny it.

I sighed and looked at Jeok Cheongang, who still wore an absent expression.

I still couldn’t get used to his appearance, no matter how many times I looked at him. He had a roughly shaved bald head and wore a threadbare monk’s robe.

“Putting that aside, what the hell is with your outfit?”

“Can’t you tell by looking? It’s a disguise. Don’t I look more or less like a monk?”

“You look like a defrocked monk who set fire to a temple and ran away.”

“……You insolent brat. Do you think this old man wanted to imitate some bald-headed monk? It couldn’t be helped if I wanted to avoid Dark Heaven’s eyes. My hair was especially conspicuous, so I shaved it all off.”

He had a point. No matter how vast the world was, people with red hair were uncommon. He would stand out wherever he went, and rumors spreading was inevitable.

Of course, that didn’t explain everything.

At least, the Blood Monk I knew was a terrifying great fiend who had dyed Guangxi red with blood all by himself.

“So the man who disguised himself as a monk to avoid Dark Heaven’s eyes went around beating hundreds of innocent Murim practitioners to death?”

“The things those bastards were doing were so—what?”

Jeok Cheongang’s brow furrowed as he tried to continue.

“Innocent Murim practitioners? What nonsense are you talking about?”

“……?”

“It is true that this old man unintentionally attracted attention in Guangxi. The unorthodox faction bastards were taking advantage of the chaos to get up to all kinds of despicable nonsense, so I taught them a lesson.”

“Unorthodox faction? Did you just say unorthodox faction?”

“That’s right. They were committing all kinds of atrocities while disguising them as the work of Dark Heaven. This old man went to find them himself and destroyed about six of their organizations. The remaining small fry fled in every direction.”

“……!”

Only after listening to Jeok Cheongang’s story with my mouth hanging open did I understand what had happened.

*That Murim practitioner who fled from Guangxi.*

The Murim practitioner who had allegedly caught some endemic disease and died as soon as he entered Nanman had actually been a small-time member of the unorthodox faction fleeing Jeok Cheongang’s fiery fists.

A crayfish sides with a crab, and people need to know how to read the room.

Nanman already shunned outsiders. There was no way those people could admit that they were bad guys, and in the process, the unorthodox practitioners killed by Jeok Cheongang had been transformed into righteous heroes who loved justice and peace.

It had happened because Nanman was so isolated and had so little contact with the outside world.

*How the fuck did things turn out like this?*

As I stared blankly at Jeok Cheongang, a thought suddenly flashed through my mind, and I hurriedly opened my mouth.

“Then, on your way here, did you happen to—”

“I don’t know who you mean, but I met them all. The bandits diving for things in the Yangtze, the Nanman people who suddenly came at me with spears and swords, and even your subordinates.”

“Oh.”

“The Escort King’s granddaughter told me the moment she saw me that you were in danger. That Hyuk fellow grabbed me by the trouser leg and cried so hard I nearly broke his wrist.”

I could see it all so clearly just from hearing him describe it. Their appearance, their desperation more than anything else.

And Jeok Cheongang, who had come rushing here without a single question or hesitation the instant he heard that I was in danger.

“But why did the conversation turn this way? I’m the one who needs an explanation.”

Seeing Jeok Cheongang deliberately frown, I suddenly let out a quiet laugh.

“……Are you laughing?”

The absurdity on Jeok Cheongang’s face made my smile grow wider.

“Of course I’m laughing. We survived and met again like this.”

“……!”

“I’m sorry, and thank you. I’m sure you have a lot of questions, but I’ll explain everything later. I promise.”

Jeok Cheongang looked as though he had a great deal to say, but soon answered in a subdued voice.

“You damn brat.”

It was a single sentence filled with countless emotions.

It even sounded as if he were thanking me for staying alive, and that was enough for the two of us.

“Stop smiling. I’ll get attached.”

“For someone who supposedly isn’t attached, you were crying pretty bitterly. Of course, I’m not talking about you, Old Master.”

“……Can you shut that mouth of yours?”

Perhaps he had finally remembered how he had acted a moment ago. Still huffing, Jeok Cheongang took my hand and helped me to my feet.

Pat pat.

The dust and stone grit covering my entire body fell away. The pain had been gone for a long time, but my vision blurred for a moment.

*Hmm.*

I swallowed a groan.

My body, healed perfectly by no fewer than five level-ups, moved according to my will. But my mind, battered by one battle after another without a moment’s rest, was exhausted beyond measure.

*Ah, I want to sleep.*

I desperately wanted to collapse right then and there.

I wanted to sleep deeply, body and mind refreshed, then spend a day gazing at a clear sky as I slowly shook off the drowsiness.

But… not yet.

The sky overhead was still filled with dark clouds, and people covered in injuries both great and small lay scattered everywhere, groaning.

If we left them like this, they would fall into a sleep from which they could never be woken.

Jeok Cheongang looked around belatedly, and his expression darkened as well.

“……If only this old man had hurried more.”

It was pointless regret and needless self-reproach. If Jeok Cheongang hadn’t come, all of us—including me—might have been buried here.

“Let’s hurry. Before it gets any later.”

I nodded at Jeok Cheongang’s words and chose the most accurate and fastest method.

*Skill: Qi Sense activated.*

Ding.

Along with the clear ringing of a bell announcing that the System had activated, a blue circle spread outward from me and enclosed a set area. At the same time, Level display windows rose here and there, and my chest tightened.

*There are too few.*

There were only about thirty Level windows visible to my eyes.

That meant the Nanman warriors, once nearly a thousand strong, and the three hundred members of the Baekcheon Unit had fallen here.

Even in the midst of all this, there was at least one fortunate thing: the condition of those who still had breath was not particularly critical.

*The Southern Heaven Demon Empress must have had to conserve as much strength as possible at the end, too.*

Muttering with a heavy heart, I shot toward the person lying closest to me.

Wang Ho, Commander of the Baekcheon Unit.

I grasped his wrist pulse as he had charged at the Southern Heaven Demon Empress until the final moment, then sent internal energy through his back and along his spine with my other hand.

Ssshhhhhh.

“C-cough.”

After Wang Ho spat out a mouthful of dark blood, color began to return to his pale face.

He had been struck particularly hard because he had fought the fiercest battle among the Baekcheon Unit, but this should let us breathe a little easier.

However, unlike Wang Ho, there were also people whose injuries were grave at a single glance.

Hhh… hhh…

His breath came faintly through his nose. Jeok Cheongang recognized the giant who had collapsed on his knees and let out a low groan.

“……He really got beaten to hell. This fellow never suffered injuries this bad, not even during the Great Faction War.”

The Southern Heaven Demon Empress’s One Strike, delivered with her very life on the line, had been that terrifying.

Countless fragments and pieces of swords were lodged deep throughout the giant’s body.

On top of that, the Beast Miao King had lost consciousness from the severe internal injuries he had suffered while protecting me. His condition was utterly wretched.

“Old Master, what if—”

Before I could finish, Jeok Cheongang realized the concern in my voice and shook his head.

“The Beast Miao King is as tough as iron, so don’t worry. If this old man does his best, he should be able to survive. But…”

His words trailed off.

Unlike his confident first sentence, his hesitant gaze turned toward the enormous White Tiger lying several steps away.

“I don’t know about that beast. It doesn’t seem like an ordinary creature, even for a beast, but is it something you absolutely have to save?”

*We have to. No matter what.*

But before my thoughts could escape my lips, a quiet Will rang out.

—If that is how it turns out, then that too must be the fate given to me.

“……!”

—You have lived a rather long time, old human. Though your face differs from the one I saw in the imugi’s memories, your essence has not changed.

The guardian spirit turned its head away from Jeok Cheongang, whose eyes had widened, and shifted its gaze toward me.

—Come closer.

I bit my lip and approached the guardian spirit.

When I sat beside its head and stroked the back of its neck, which was drenched in blood, a low growl escaped it.

—How insolent. How dare you lay a hand on this body?

What should I say?

As I silently stroked only its neck, the guardian spirit sent another thought to me.

—It is not entirely unpleasant, in truth. A human just as obnoxious as you existed a very long time ago.

I thought I knew who it meant.

The first Palace Lord of the Nanman Beast Palace. The only human to whom the guardian spirit, which had lived for an age beyond imagining, had ever opened its heart.

—It is truly strange. Everything is different, yet when I look at you, I am reminded of him—the one who became earth hundreds of years ago.

“……!”

—Perhaps that is why. Perhaps that is why I saved you on instinct, and entrusted the sacred stone to you, a mere human.

The enormous body of the White Tiger beneath my hand heaved violently.

The guardian spirit breathed roughly, then lifted its blue-white eyes to look at me.

At that moment, I understood instinctively.

Why the guardian spirit needed the sacred stone. What it intended to do with it.

*The rift.*

The guardian spirit was trying to close that dense darkness—the rift—all by itself.

Just as an imugi had done several months ago.
## Chapter artifact 712

# Chapter 712

I hoped I was wrong.

I wanted this thought that had just crossed my mind—this suspicion of mine—to be completely unfounded.

But when the guardian spirit’s Will reached me the next moment, I realized that all of it was true.

—Someone has to do it. Perhaps this is the fate I was given.

Just as I had instinctively understood the guardian spirit’s thoughts, it had done the same.

My face was reflected in its clear, transparent blue-white eyes, so pure they seemed capable of seeing through everything.

—Until that darkness… that thing you call a rift is gone, nothing will end. No, it will be the beginning of another catastrophe.

It was an undeniable fact. We had defeated the Southern Heaven Demon Empress and her subordinates after a fierce, grueling struggle, but the rift they had opened still remained, devouring the space around it.

Even now.

Ssshhhhhh.

The darkness had already passed beyond the Inner Palace and was advancing toward the Outer Palace.

The demonic qi seeping through it would corrupt living things, transform them into beings that had lost their reason, and bring about another disaster.

*It would basically be an army of monsters.*

There was no way to know how far the rift’s power—which reminded me of a Gate—would reach.

But if the demonic qi flowing from the rift was enough to swallow Nanman, or even more than that, this darkness would continue without end.

Until it consumed the entire world beyond Nanman.

—Human. As you have likely guessed, only the power of the sacred stone can withstand that darkness. Someone must enter the center of the rift and endure the darkness alongside the sacred stone.

I knew that, too. Only a few months ago, the Water God Dragon had sacrificed itself to seal the rift.

And I knew what the price of that sacrifice had been.

“What if you become something different from what you’ve been until now?”

I couldn’t bring myself to say that it would become a mutant. The guardian spirit smiled faintly at me.

—Kill me. Without the slightest hesitation.

“……!”

—With your strength and that old human’s, it shouldn’t be too difficult, even if I become a corrupted being.

I stared at the guardian spirit in silence before forcing my mouth open.

It was the thought I had held in my heart from the moment I first understood the guardian spirit’s intentions, and the single question I had reached after a long period of deliberation.

“What if I seal the rift myself?”

The answer to that question came from somewhere other than the guardian spirit.

“Don’t be ridiculous!”

It was Jeok Cheongang’s shout. He had been tending to the Beast Miao King’s Internal Injury.

His expression was graver than ever as he looked at me and continued.

“Impossible. No matter what you say, this old man cannot allow it.”

“But, Old Master—”

“I don’t want to hear it. No matter how great an achievement you’ve made, we have no idea what might happen. How could I allow it?”

“I’ll come back safe and sound without so much as a hair out of place. I promise.”

“Without so much as a hair out of place?”

“Yes.”

I nodded, and Jeok Cheongang stared at me silently before opening his mouth.

“If that is truly your wish. Very well.”

“Then—”

“You will stay here. This old man will go.”

“……!”

“If you can return without a scratch, then it would be even more certain if I went instead. Am I wrong?”

His single remark had struck the heart of the matter, and for a moment I couldn’t get a word out.

Then the guardian spirit’s Will rang out.

—Old human. If that young human becomes a different being because of the darkness, what will you do?

“I’ll kill that child. So he can find peace.”

Jeok Cheongang answered without the slightest hesitation, then continued in a low voice.

“And this old man will choose death as well.”

—Young human, what will you do in the opposite situation?

I didn’t answer, and the guardian spirit saw straight through the meaning of my silence. It smiled faintly.

—Yes. That is why I must go.

“……”

—The humans of this land have already shed enough blood. There is no reason for you and that old human to sacrifice yourselves in my place. You still have many fates ahead of you, while I have already passed through many fates.

The guardian spirit raised its blue-white eyes and looked at Jeok Cheongang.

—Even if the situation becomes irreversible, do not hesitate to kill me.

Jeok Cheongang gave a small nod.

“I’ll give it everything I have.”

—Thank you.

Grrr. The guardian spirit drew a labored breath, then opened its mouth toward me.

—Jin Taekyung. The time has come.

What more could I say?

I reached into my robes and muttered inwardly.

*Inventory open. Summon.*

The next moment, something that gave off a warm, faint light rested on my outstretched palm before the guardian spirit.

Jeok Cheongang felt its mysterious energy and muttered like he was groaning.

“Don’t tell me this is…”

—This sacred stone, which you humans call the Beast King Stone, was my only remaining mission and the reason for my existence. And now, it seems we will be together until the very end.

Ssshhhh.

The sacred stone slowly floated into the air and was drawn into the guardian spirit’s mouth.

Warmth spread outward with its faint radiance.

At the same time, the guardian spirit’s panting grew steadier, and the body that had collapsed helplessly began to regain its strength.

Rustle. Thud.

At last, the enormous White Tiger rose and planted one blood-soaked forepaw on the ground.

Thud. Thud.

One step. Then another.

Its footsteps were heavier than ever, but they were also footsteps no one could stop.

Not even the darkness, now incomparably denser and stickier than at first, could stop them.

Kraaaash!

Pools of blood filled the surroundings, and countless corpses lay strewn everywhere. The darkness that had surged over them like a wave struck the light surrounding the guardian spirit and recoiled.

If the darkness flowing from the rift corrupted everything, then the light contained within the sacred stone possessed the power of purification.

—Kraaaaang!

A fierce roar shook heaven and earth. Its silver mane, stained red, whipped violently in the wind.

Before I knew it, the guardian spirit had become a gust of wind and was racing forward.

Shweeeek!

I watched the guardian spirit’s back as it shot through the darkness.

I watched until that faint but unmistakably brilliant streak of light crossed countless corpses and remnants.

Until it raced across the vast space and reached the cliff swallowed by pitch-black darkness.

And then I realized something.

At the very end, the guardian spirit had called my name for the first time.

* * *

It was out of breath. Its body was drenched in blood and heavy, while the darkness filling the surroundings constricted the guardian spirit from head to toe.

*Imugi. Did you feel this way, too?*

With that unheard question, the guardian spirit took a step with all its strength into the gaping fissure in the cliff.

It had to go, no matter how difficult it was.

It had not known before, but now it did.

This was the only mission it had been given from the beginning. What the guardian spirit had to protect was not the sacred stone, but everything in this land.

Crack.

Its footsteps were heavier than ever, sinking deep into the ground. The closer it came to the center of the rift, the more powerful the darkness and demonic qi became, pressing down on its entire body.

Through its fading consciousness, memories from the distant past flashed across its blue-white eyes.

*Come to think of it, I was always alone.*

It had no father, mother, or siblings.

No. At first, it did not even know whether such things existed in the world.

To one small, pure-white White Tiger, this space it had seen from the moment it first opened its eyes was the world itself. And it had a friend who had always been there with it.

A friend who could not run and play alongside it, and with whom it could not communicate, but who had always remained by its side.

Tap.

Something touched its soft, pure-white forepaw, as gentle as a ball of cotton.

It was a transparent stone, so clear that crystal would have been a more fitting name for it. As always, it was warm and comforting.

Grrr.

The young White Tiger let out a contented growl and soon fell asleep, breathing softly.

And at the feet of the sleeping White Tiger, on a hill drenched in warm light that was neither sunlight nor moonlight, a green sprout suddenly pushed its head above the ground.

Rustle. Tap.

The sprout, which had been no larger than a fingernail, began to straighten its bent stem. It burst into colorful buds, and branches began to grow.

Before long, where the sprout had once been stood a giant tree with roots sunk deep into the earth. Its leaves, hanging from countless branches, cast a broad, cool shade.

Ssshhhh.

A wind blew from somewhere, and the giant tree shook its full crown.

One leaf that had held on stubbornly for quite some time finally broke away from its branch and fell into the shade.

At the soft tap of the leaf landing on it, a being enjoying an afternoon nap opened its eyes.

—Grrr.

The being rose with a low growl.

It was a White Tiger.

It had grown too enormous and powerful to be called a cub, or even an ordinary tiger. It looked around with its blue-white eyes.

No one knew exactly how much time had passed.

They could only guess that quite a lot of time had gone by. It was always daytime in the place where it had been born and raised, and it had always been peaceful.

But even so, there had been change.

Change as certain as the sprout growing into a giant tree, or the small, soft White Tiger cub becoming a huge and powerful being.

*Yes, that one.*

It had first met him three hundred years ago. Despite his bear-like size, he was always grinning broadly. He was a tribal chieftain who led humans and possessed a mysterious power that made beasts follow him.

That was probably why the beasts of the Sacred Land had accepted him even without the guardian spirit’s permission.

“Oh. I’ve never seen a White Tiger this big before. What’s your name?”

At first, the guardian spirit had been surprised that a human had set foot in the Sacred Land without its permission.

When that human bastard fearlessly reached out and stroked the back of its neck, the guardian spirit had been left speechless.

So it asked him.

“And what is your name, then?”

The expression on the insolent human bastard’s face was still vivid in its memory. He had stared at the guardian spirit with his mouth hanging open, then answered in a dazed voice.

“Yayul Cheon….”

“I do not know how you entered this place, but if I see you here again, I will tear you limb from limb and kill you. Do you understand?”

And the next day, the guardian spirit realized something.

That young human bastard named Yayul Cheon had less fear than any living creature it had ever seen.

“I believe I told you not to let yourself be seen.”

“That’s why I was hiding.”

“……Are you joking with me right now?”

“You knew because of my smell, not because you saw me. I’m lying face-down in the grass right now.”

“No, is that supposed to be an answer? …Wait. What is that smell?”

“Grilled meat. I brought some in case you were hungry. Want some?”

“Meat? Did you hunt the beasts?”

“……”

It did not know how it had grown close to him. They simply came to know each other little by little, like clothes slowly soaking through in a drizzle, and time passed swiftly in the process.

Ten years. Twenty years. And then, the day they last faced each other.

“It’s been a long time.”

When he came to visit after several years, he was no longer a young man.

His black hair had already turned half gray, and his eyes were worn out with fatigue.

“I need your help. Only with your power and that of the sacred stone can we win this war and restore peace to Nanman.”

The guardian spirit knew what kind of battle he was fighting, and how evil their enemies were.

But it refused.

The sacred stone and the guardian spirit were nothing more than observers. That was what it thought then.

At least, it had thought so at the time.

And regret always came too late.

*If I had helped you then, would the fate of this land have changed?*

The blue-white eyes, sunk deep in thought, came back to the present.

Turbulent darkness churned before them. It writhed strangely and spewed demonic qi as though it intended to swallow everything.

Ssssss!

Within the warped space, the guardian spirit struggled through its final step and stared at the center of the rift.

Then, with every bit of strength it possessed, it moved its body wrapped in faint light and lunged forward.

—Kraaaaang!

With a single roar, an enormous shock wave burst outward.
## Chapter artifact 713

# Chapter 713

The wait was not a long one.

It happened at the exact moment I had moved the survivors to one place and, with Jeok Cheongang’s help, the Beast Miao King finally managed to lift his heavy eyelids.

Crack. Crack-crack.

The change began.

It was a resonance that I could feel. So could Jeok Cheongang. Even the Baekcheon Unit warriors, whose bodies were still far from recovered, and the Beast Miao King, who had only just regained consciousness, felt it.

Whoooosh.

Space twisted. The darkness that had writhed as though it were alive stopped moving, and the wind began to flow in a single direction.

Beyond the thick darkness that had swallowed the guardian spirit, between the cracks in the cliff that had opened its enormous jaws like some primordial beast—

At the same time, I could clearly see and hear it.

—Kraaaang!

Along with the roar that echoed like thunder, a single streak of light grew clearer as it illuminated the darkness.

*This is…*

I stared at that light in bewilderment. No—everyone here was doing the same.

The survivors, covered in injuries both large and small, even forgot to groan.

The Beast Miao King had only just regained consciousness, but he reached out with a dazed expression toward the light that illuminated the distant darkness all by itself.

It was a light imbued with qi warmer than sunlight and as clear as water.

Just as a silence descended, as though the world itself had stopped, Jeok Cheongang’s quiet voice pierced my ears.

“It’s coming.”

“……!”

And with that single word, time—which had been frozen—began to move again.

Rumble. Boom!

A gigantic explosion.

Everything condensed, then burst outward all at once, sweeping across every direction. Along with a deafening roar, an invisible shock wave surged in, broad as a highway.

Beyond the raging gale, I heard Jeok Cheongang shout.

“Watch out—!”

Kuwaaaang!

The wind—no, the storm—swallowed his voice.

A distant flash of darkness and light mixed together, blocking my vision, while the enormous shock wave battered and flung away everything within its range.

But.

*Now.*

Realizing that the time had come, I brought White Flame down in a diagonal slash.

The hellfire surging along the transparent spearhead burned through the wind. The flames dug into a grain that was invisible but undeniably there, then collided with the shock wave.

No—it canceled it out.

Kuwaaaang! Crack!

The earth shook with a deafening roar. The impact was powerful enough to push back both of my firmly rooted legs.

Jeok Cheongang, who had stepped forward to protect the survivors just as I had, flung both sleeves.

Fwoosh. Boom!

The Blazing Flame Divine Palm, perfected to the pinnacle.

Unlike mine, two complete fire dragons rampaged ferociously, biting into the storm.

The flames surged upward, coiling across a radius of dozens of jang as they consumed the wind and reduced to ash the countless fragments of debris hurled like hidden weapons by the shock wave.

Ssszzzzzt!

Smoke and steam filled every direction. In a world dyed entirely pale white, I exhaled the breath I had been holding and reached out.

Boom!

Compressed air burst outward, driving back the smoke and steam.

And beyond the vision that slowly cleared, the darkness was dispersing, while a collapse that had only just begun awaited us all.

Rumble. Rumble-rumble!

It was collapsing.

A gigantic cliff stretching more than two hundred jang.

The sight of countless strange and enormous rocks pouring down and filling the sky was frighteningly overwhelming. The sunlight beginning to shine down over them little by little meant one thing.

*The rift… closed.*

It was over.

The long and fierce battle had finally come to an end. We had stopped a catastrophe that might have claimed hundreds of thousands—perhaps even millions—of lives.

But why?

Why was the emptiness greater than the joy?

Perhaps it was because I knew better than anyone that there was still something left unfinished.

Ding.

> **System**
>
> **Rift** has closed.
>
> **Demonic qi** is disappearing.
>
> The power of the **sacred stone** purifies energy corrupted by **demonic qi**.
>
> A sudden **Quest**, **Sacrifice and Rest**, has been generated. You cannot refuse this Quest.

As the System notification reached my ears, I suddenly reached out.

The darkness that had writhed painfully in the air like a living creature scattered between my fingers.

The sunlight shining through the slowly dispersing storm clouds was warm. Floating above it was a translucent holographic window displaying only a few short lines.

> **System**
>
> **Quest**
>
> **Sacrifice and Rest**
>
> Now grant him rest.
>
> **Grade:** None
>
> **Restriction:** None
>
> **Objective:** Defeat Mutated Guardian Spirit *(Incomplete)*
>
> **Reward:** ???
>
> **Failure:** ???

It was the first time.

The first time a Quest description had been this short. The first time the restriction field—which usually contained the three characters of my name—had not limited the Quest to anyone at all.

Perhaps even the System knew about his sacrifice.

The choice made by a being that could easily have been called a divine beast—a guardian spirit that had sacrificed itself and fallen into corruption.

Step.

I pushed through the darkness scattering into the wind along with the ash.

Between Jeok Cheongang’s quiet footsteps behind me and the countless strange rocks still collapsing around us, I sensed someone’s presence.

No.

I saw it.

> **System**
>
> **Lv. 155 Mutated Guardian Spirit**

The fur that had once shone silver even in darkness and the blue-white eyes that had been as clear as the Sacred Land’s pond had both turned black.

Its fangs, grown twice as long, flashed at us.

—Grrrrr.

A low growl filled with ferocity.

Then came a movement like a flash of light.

Screeeech!

Along with its blurred form, more than ten jang of distance vanished. Its blood-soaked forepaw struck the ground, and its enormous body sprang upward.

Pop.

Toward the giant body casting a shadow over our heads, Jeok Cheongang and I unleashed our full-strength strikes.

Remembering the request he had given us before he left.

*Kill me. Without the slightest hesitation.*

And we kept that promise.

Shhhk. Slash!

* * *

It was somewhere deep and cold.

Not a single point of light could reach it, and not even the faintest warmth could be felt.

*He* lay curled up there, sensing the presence of death that would soon arrive—or perhaps had already arrived.

Then, at some point, he suddenly felt a warm presence and opened his eyes.

No. It was not warmth. It was heat.

And waiting for him in his blurred vision was someone with a familiar face.

“Jin Tae… kyung.”

A cracked voice slipped between his lips.

The young man who had been quietly staring at Baeksang, now fully awake, answered calmly.

“Yes.”

And with that single word, Baeksang knew that everything was over.

Perhaps it was because of the sunlight visible over Jin Taekyung’s shoulder.

*Yes. So it came to this in the end.*

The words echoed inside his mind.

Baeksang gazed up at the blue sky where the storm clouds had vanished.

It was strange. He had lost everything he had sought, yet he felt no despair.

Only emptiness.

“What happened to the Southern Heaven Demon Empress?”

The answer he received was short.

“She’s dead.”

“The rift must have disappeared as well.”

“……Yes.”

Along with that hesitant answer, Jin Taekyung’s head moved.

His gaze lingered briefly on the enormous tiger lying collapsed nearby.

No.

What Baeksang saw in that moment was countless corpses of beasts and humans.

“Let me ask you one thing.”

Jin Taekyung’s voice continued, sunk deep with gravity.

“Did you know from the beginning that this was how it would turn out?”

Baeksang looked at the corpses filling every direction with hollow eyes.

Then he answered.

“Yes. I knew.”

“……!”

Jin Taekyung clenched his teeth and glared at Baeksang. Baeksang did not avoid the gaze, where flames seemed to pour down in streams.

“To be precise, I learned a few months ago, after receiving a letter from the Central Plains.”

The letter had come from Henan. Along with a proposal to join the Murim Alliance, which would soon be established, it contained a detailed account of the series of events that had taken place in Hubei.

“That was when I realized why Dark Heaven had reached into Nanman, which belonged to the Outer Lands rather than the Central Plains. I realized what the grand plan spoken of by the Southern Heaven Demon Empress was.”

“And even knowing that…”

“I followed orders. I had already ceased to be a human being and become a monster.”

They said that ten years was enough to change the mountains and rivers. Sometimes earthquakes struck and tore down mountains, while violent floods twisted the course of rivers.

Baeksang had spent more than forty years amid earthquakes and floods, gradually becoming a monster that had lost his heart.

Because of the grief of losing his only child.

Because of his desire for revenge against the people of the Central Plains who had caused his child’s death.

But that was not all.

“After the Great Faction War, I hated the Demonic Path more than anyone. If I was a turncoat the Central Plains could never forgive, then they were enemies who had to die.”

Jin Taekyung let out a hollow laugh as he listened to Baeksang.

Dark Heaven and the Demonic Cult were branches of the same tree, with only their limbs differing.

If Baeksang had hated the Demonic Path, he could never have joined forces with Dark Heaven—the ones who had killed his child.

And yet Baeksang had joined hands with the Southern Heaven Demon Empress and brought about this catastrophe.

He had stood by while Dark Heaven opened the rift. Even knowing that countless deaths would follow, he had issued a general mobilization order and drawn nearly ten thousand warriors and beasts into the Inner Palace.

To offer them as living sacrifices.

“You fucking idiot. And you call that something worth saying now…”

For some reason, Jin Taekyung’s words suddenly trailed off.

Baeksang’s bloodstained lips moved.

“Yes. To me, there was something more important than hatred—more important than anything else.”

At that exact moment, someone’s image flashed through Jin Taekyung’s mind.

It was also why the eyes revealed above the mask had felt so familiar, as though he had seen them somewhere before.

“……Baekhwi.”

It was not Jin Taekyung who said it.

Baeksang lifted his blurred eyes and looked toward the figure approaching from the distance.

A huge man drew near with unsteady steps.

Despite Jeok Cheongang’s attempts to stop him, the Beast Miao King came right up to them and asked with a groan.

“Was that child alive?”

Baeksang weakly nodded, and that was enough for the Beast Miao King.

He knew what that child had meant to Baeksang. He knew what his sworn younger brother could do for his only child.

That was why he could not help but feel more sorrow and anger than anyone else.

“Why? Why did you not tell me? Why!”

“I did not want the Palace Lord—my hyung—to die.”

“……!”

“And Hwi… that child. I would have lost him all over again.”

Memories of the past faintly flickered through Baeksang’s eyes.

On the day he first encountered the darkness, he had flatly refused the Southern Heaven Demon Empress’s proposal to join hands.

That was before he heard that his child, whom he had believed the Great Snow Fiend had killed, was still alive.

“I accepted the Southern Heaven Demon Empress’s proposal, and I believed her promise that she would let Hwi live once the grand plan was over.”

He had believed her.

No—he had had no choice but to suppress his distrust.

There had been no other way to reunite with his only child.

After that, whenever his resolve wavered, he went to see the Southern Heaven Demon Empress.

He went to see the face of his child, kept alive by Dark Heaven’s sorcerers and sunk in a deep sleep.

“But at the same time, I knew. I knew what I was doing, and how many people would die because of this choice.”

That was why he created the Baekcheon Unit.

Not for himself, but for someone else—for the hope that he would stop this catastrophe.

“That was something I could not do.”

A child might kill a parent, but there was no parent who could kill their child.

Baeksang was a father.

Even if he could return to that moment dozens or hundreds of times, his choice would remain the same.

Cough.

Baeksang spat up blood and lifted his blurred eyes toward the Beast Miao King.

At that moment, a memory of the saddest and happiest day of his life at once flickered in his eyes.

*Yes. It was that day.*

The day he lost his beloved wife and gained the child he would come to love more than anyone else, Baeksang had cried.

He had sat facing his one sworn elder brother and drunk fruit wine as though it were his last day.

Just as he had decades later, on the day the Southern Heaven Demon Empress came to him.

“I have one last request.”

Baeksang continued with a faint smile.

“Please kill me, hyung.”
## Chapter artifact 714

# Chapter 714

“Please kill me, hyung.”

The moment he heard those words, the Beast Miao King closed his eyes without realizing it.

His chest ached, and he could barely breathe. The request his only sworn younger brother had made after several decades stabbed and carved into his heart like a sharp blade.

*Hyung. He called me hyung.*

It was the word he had wanted to hear more than anything.

And now he wanted to cover his ears.

He would rather become a fool who had never seen or heard anything. He would even accept becoming an incompetent Palace Lord if it meant he could escape this moment.

If only he could.

“This brings back old memories.”

The Beast Miao King opened his eyes at the quiet voice. Baeksang’s face, wearing a faint smile, was reflected in his eyes.

“We were young back then, and I was always desperate to beat you, because I wanted to become the Palace Lord of the Nanman Beast Palace someday.”

“……Yes. You were.”

It had been back when they were so young that they had barely been more than children.

Baeksang had regarded the Beast Miao King, who was several years older, as a rival. To the Beast Miao King, Baeksang had simply been adorable. He had been born an only child and had no siblings.

“But I never caught up to you even once. Whenever I thought I had drawn close, you were suddenly far ahead of me again.”

“That was because you were younger than me. If we had been the same age…”

“Even then, the result would not have changed. We were born with different potential from the start.”

But Baeksang had never given up. Every day, he challenged the Beast Miao King to a duel. Even after losing every time, he would come looking for him again the next day as though nothing had happened.

“And then one day, I suddenly realized that the idiot who was two heads taller than me wasn’t actually all that bad.”

Baeksang remembered it clearly. The sight of the big boy who had pulled him to his feet whenever he fell and brushed the dirt from his clothes.

The shadow of someone who would quietly leave medicinal herbs outside Baeksang’s quarters whenever he was sick, then slip away.

“So I challenged you to one last duel.”

The result had been no different that day.

Baeksang had fought with more strength than ever before—and lost.

If it had ended there, it would have been an ordinary day, no different from any other.

But Baeksang did not push away the hand that helped him up as he usually did, nor did he return to his quarters while huffing in anger.

Instead, he pulled out two bottles of fruit wine he had stolen from somewhere and muttered as though speaking to himself.

“I have wine, but no one to drink it with. If you’re interested, you can come along.”

At the Beast Miao King’s quiet voice, Baeksang’s eyes widened for a moment. Then he coughed up blood and laughed.

“Cough. You still remember that?”

“How could I forget? In my entire life, you were the only twelve-year-old brat who could say something so insolent.”

“Then you must remember how I emptied both bottles by myself.”

“Both bottles?”

The Beast Miao King let out a laugh before he could stop himself. The corners of his crescent-shaped eyes were already damp for reasons he could not name.

“Well, I vividly remember the little brat who collapsed before he had even finished a single cup. I also remember what you said while looking at me with those unfocused eyes.”

Baeksang nodded weakly. His blurred eyes were searching through the distant past.

“I said I would be content with becoming the Great Chieftain, so you should become a great Palace Lord. I had to drink because I couldn’t say those things to you unless I was drunk.”

“And what you said after that? Was that something you could not say unless you were drunk as well?”

“Of course not.”

Baeksang continued in a quiet voice.

“You were… simply my hyung. Perhaps you had been ever since the day we first met.”

The two boys had tasted alcohol for the first time, then collapsed and fallen asleep. When they opened their eyes the next morning in an old shrine, they had become sworn brothers closer than anyone else.

In the mountains. In the fields. By the rivers and in the marshes.

And they had been together on the battlefield as well.

Until a terrible fate came one day and tore them apart.

“Hyung.”

“…….”

“The day we became sworn brothers, you made a vow to me. You said you would become a better Palace Lord than anyone else. That you would care for Nanman above all others and fight for the people of this land.”

“Enough. Stop.”

The Beast Miao King already knew why Baeksang had brought up these memories.

He knew what Baeksang was trying to say.

“Do I really have to… kill you with my own hands?”

Baeksang gave a small nod.

“Far too much blood has already been spilled. Everything happened because of my misguided choices.”

Executing the traitor who had betrayed Nanman and countless tribespeople.

That was precisely what the Palace Lord of the Nanman Beast Palace had to do himself. It was the only way to keep the vow they had made long ago in that old shrine.

“You made a vow, didn’t you? That you would become a better Palace Lord than anyone else.”

A hand that had been raised with difficulty pointed behind the Beast Miao King, whose body had stiffened like a stone statue.

Beyond the fallen ruins stood countless tribespeople and warriors who had returned to the Inner Palace.

“Everyone is watching. You and me. And us.”

Baeksang’s words were the undeniable truth.

The people constantly pouring into the Inner Palace had learned that the catastrophe was over and cheered. Then they were horrified by the sight that unfolded before their eyes. Finally, they fell silent at the sight of their returning Palace Lord and the traitor collapsed before him.

No.

They were furious.

“I can feel it. Their anger directed at me.”

It was the moment Baeksang had feared most, and also the moment he had longed for more than anything.

Because if such a moment had come, it meant someone had stopped him. It meant Dark Heaven and the Southern Heaven Demon Empress’s grand plan had come to nothing.

That was why he could laugh aloud. He could raise his dying body, squeeze out the last of his strength, and shout.

“Remember this clearly!”

His eyes were dim, as though they might go out at any moment.

But the cry that burst from his lips was so clear and powerful that everyone in the Inner Palace could hear it.

“Though the grand plan has failed, the day will surely come when Dark Heaven’s sky devours Nanman!”

“……!”

His ringing cry reverberated in everyone’s ears, passing over countless piles of rubble and corpses.

With every syllable he forced out, blood burst between his teeth and strength drained from his entire body.

But Baeksang did not stop.

He could not stop.

He was a traitor who had betrayed everyone and brought about this catastrophe.

A criminal who had committed an unforgivable crime had to die as a criminal, without sympathy or any tale of why he had done it.

That was… the last thing Baeksang could do.

“That day, which will come before long…!”

Baeksang swallowed the blood surging up his throat, clenched his teeth, and continued shouting.

“Those contemptible Han Chinese bastards of the Central Plains, and you Nanman people who are as primitive as can be, will all kneel and submit at the feet of the great Lord of Heaven!”

Baeksang curled his bloodstained lips into a radiant smile.

At this moment, he was the most loyal servant of the Lord of Heaven and Dark Heaven’s dog.

And for that sworn younger brother, there was only one choice his sworn elder brother could make.

Crack!

The fist that shot through the air crushed flesh and shattered bone.

The single punch buried deep in Baeksang’s chest carried green Force, like the broad fields where they had rolled around together as children.

*Thank you, hyung.*

*You became a truly great Palace Lord, just as you promised.*

Along with a murmur no one could hear, Baeksang stared at the face of one person visible beyond his fading field of vision.

*But why…?*

*Why are you crying?*

The great Palace Lord who had executed a traitor and prevented a catastrophe was crying.

He was crying bitterly, like a child who had lost something precious.

And he shouted as though howling.

“I have executed Baeksang, the traitor who joined forces with Dark Heaven!”

The people’s cheers echoed faintly in the distance. Baeksang’s head, limp and tilted backward, turned toward the sky.

It was clear and blue.

The world was no longer dark.

*Isn’t that right, Hwi?*

He thought of the son who had lost his reason and driven a sword into his father’s chest.

He thought of the child who was already waiting for him in another world, smiling brightly.

Baeksang smiled peacefully.

Thud.

His body collapsed as it lost all strength.

The world was still bright, and the people’s cheers continued without end.

And in place of his sworn elder brother, who was not even allowed to wail, someone closed Baeksang’s eyes.

“……Fuck. What the hell are you grinning about? It’s not like you did anything right.”

Jin Taekyung muttered to himself, then suddenly looked down at the old thing clenched in his hand.

*I don’t know.*

He was definitely someone who had to die. A bad person who had done more than enough to deserve death.

So why did he feel so damn awful?

Why had he brought this here?

*Damn it.*

Along with the curses that never left his mouth, Jin Taekyung covered Baeksang’s face with the object in his hand.

Baekcheon.

The old silk, carrying someone’s years and hopes, fluttered in a cool breeze that had come from somewhere.

Amid the endless cheers, along with voices echoing like distant cries, he heard them.

“Captain!”

“Pavilion Master—no, Young Master Jin!”

“Taishan came! Taishan is sorry he was late!”

“Hey, you bastard! Are you alive?”

*Is this an auditory hallucination?*

With that single question, Jin Taekyung turned around. He stared blankly at the familiar faces slowly drawing nearer, then finally let out a quiet laugh.

And collapsed.

* * *

I had a very long dream.

A terrible nightmare, at that.

Even in the dream, I was struggling desperately. In the modern world, I fought monsters. In Murim, I fought Dark Heaven.

And when I defeated the Southern Heaven Demon Empress after a fierce battle, just as I had already experienced, some masked bastard appeared and said:

—You defeated the Western Heaven Demon Lord and even the Southern Heaven Demon Empress. Not bad.

I was wondering what hole this bastard had crawled out of when the masked man continued.

—But the Western Heaven Demon Lord and the Southern Heaven Demon Empress are nothing more than the weakest of our Eight Great Heavenly Kings.

—……?

—I am the Eastern Heaven Demon Lord, who commands the east. Directly beneath me in rank is the East-West Heaven Demon Empress, who commands the east and west.

*No, fuck this. Four directions were plenty. What the hell is an East-West Heaven Demon Empress?*

The bit had been run so far into the ground that I was speechless.

At this rate, I feared that even if I returned to the modern world, I might find the Dongducheon Demon Lord or the Incheon Demon Empress waiting for me.

But what could I do?

Without even realizing that it was a dream, I fought like hell.

And every time I took another step toward that bastard, people I had killed—or failed to save—appeared before me and blocked my path.

—Just a little more. Just a little farther…

—If you had moved faster, we could have lived.

—We could have returned to our families.

—Why did you survive while we had to die?

—Why? Why? Why?

I could not answer them. I stopped moving, and they sank their teeth into my torso.

Slowly.

But without pause.

I could only stand there and watch, my body frozen like a statue.

Because of the familiar face visible among those who had become mutants.

—I cared for you more than anyone, but in the end, you couldn’t save me.

It was a face that could not be among them.

A face that should not have been among them.

It was Jeok Cheongang.

He approached with both arms gone and a gaping hole through the center of his chest, then sank his teeth into the back of my neck.

Jeok Cheongang greedily swallowed flesh and blood. Then, in a low voice, he whispered into my ear.

—But when is this infuriating bastard supposed to wake up?

And at that moment, I suddenly opened my eyes.

“……!”

A strong, unfamiliar smell hung in the air as an unfamiliar ceiling came into view.

I blinked blankly, slowly becoming aware of reality. Then a familiar voice pierced my ears.

“If you come clean now, I’ll let you off after singeing you a little. You’re a quack, aren’t you?”

“N-no, sir.”

“The child hasn’t woken up for seven days and nights. Does that make any sense? Go get the Beast Miao King.”

“Gasp. Th-that is…”

“I said bring Yayul Cheok here!”

I turned toward the ringing voice and saw Jeok Cheongang gripping a physician by the collar and shaking him violently.

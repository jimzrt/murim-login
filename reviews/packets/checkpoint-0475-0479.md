# Checkpoint Review — 475–479

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

# Chapters 475–479

## Plot

Jin Taekyung and Jeok Cheongang, Mungyeong, and Cheongpung coordinate an all-out raid against the Mutated Water God Dragon. The dragon repeatedly fires Water Breath, grows stronger while its pupils are black, and devastates the battlefield. Taekyung uses White Flame, Heavenly Strike, and summoned spears to exploit gaps in its scales while the others tear through its body. He disappears just before the dragon’s final Water Breath and kills it by driving his spear through the back of its neck.

As it dies, the dragon regains its reason and transfers a fragmented Memory Fragment covering five hundred years. It had been Dongting Lake’s benevolent Two-Horned Beast, ruling the lake and the Yangtze while pursuing ascension. When a Gate or enormous rift began emitting mana and ominous energy, demonic qi mutated the lake’s fish. The dragon fought the creatures, then sealed the rift for seven days and nights by absorbing most of the demonic qi, sacrificing its mind and becoming an evil beast.

Taekyung recognizes Honglan at the corruption site and finds her faintly scented silver hairpin in his own hair. The dragon thanks him, gives him its purified Origin Essence, and dies peacefully. Taekyung identifies Honglan as the “flower snake” responsible for corrupting the dragon and using it to kill many people. Meanwhile, Honglan enthralls Officer Song aboard a military ship and orders him to change its destination. Taekyung completes the Corrupted Spirit Beast Surprise Quest, gaining substantial EXP, Fame, and two Levels.

## Continuity

- The Mutated Water God Dragon is dead. Its restored consciousness revealed that it was originally Dongting Lake’s benevolent Two-Horned Beast.
- The dragon sacrificed its intelligence to contain the Gate or rift’s demonic qi, becoming an evil beast in the process.
- Taekyung received the dragon’s purified Origin Essence, known to humans as an inner core.
- Honglan corrupted the dragon and used it to cause the Dongting Lake and Hubei tragedies. Her motives and full involvement remain unknown.
- Honglan’s silver hairpin carries a faint scent and links her to the corruption site.
- Honglan can seize a person’s emotions and soul, enthralling and controlling them. Officer Song, commander of the military ship carrying her, is currently under her command.
- The Corrupted Spirit Beast Surprise Quest is complete; Taekyung received EXP, Fame, and two Levels.
- The Gate’s creator, purpose, and connection to demonic qi and Dark Heaven remain unresolved.
- The Dongting Fisherman’s exact role in Dark Heaven, the shared Arch Lich/Dark Heaven symbols, the destruction of Donghu Stronghold and the Yangtze River Channel League strongholds, and the missing Moving Formation traces remain unresolved.

## Translation Decisions

- Render 광폭화 as **Berserk**, 원정 as **Origin Essence**, 내단 as **inner core**, and 꽃뱀 as **flower snake**. Retain the explanatory footnote for the last term.
- Render 의념 as **mental intent** when distinguished from 전음, which remains **Sound Transmission**.
- Preserve **Water Breath**, **Force**, **Sword Energy**, **Hellfire**, and **whiskers** as distinct established terms.
- Retain **Jangsu stone bed**, **hyojason**, jang and geun measurements, **live-fish sashimi**, and **bone-in sashimi** with their established footnotes.
- Preserve Taekyung’s profane raid-game humor, Cheongpung’s literal innocence, Mungyeong’s impassive voice, and Jeok Cheongang’s gruff banter.
- Render 대라신선 as **Great Firmament Immortal**.

## Durable state

{
  "active_continuity": [
    "The Water God Dragon died after regaining its reason and giving Taekyung its purified Origin Essence, which humans call an inner core.",
    "The dragon's Memory Fragment showed its five-hundred-year history, including its benevolent rule of Dongting Lake and its sacrifice to contain the Gate's demonic qi.",
    "Taekyung identifies Honglan as the person who corrupted the benevolent Dongting Lake imugi and used it to kill many people.",
    "Honglan's silver hairpin carries a faint scent and was found in Taekyung's hair after the Memory Fragment ended.",
    "Honglan can enthrall people by seizing their emotions and souls; Officer Song is currently under her control and obeying her command to change the ship's destination.",
    "Taekyung has completed the Corrupted Spirit Beast Surprise Quest and acquired substantial EXP, Fame, and two Levels.",
    "The Gate or rift that corrupted the Water God Dragon remains connected to unresolved questions involving demonic qi and Dark Heaven.",
    "Honglan's motives, her exact relationship to Dark Heaven, and the full extent of her role in the Hubei incidents remain unresolved."
  ],
  "continuity_sources": [
    479,
    478
  ],
  "open_questions": [
    "What is the Dongting Fisherman's exact role within Dark Heaven, and how was he connected to the earlier destruction inside the secret refuge?",
    "What are the origin and purpose of the symbols shared by the Arch Lich's magic circle and Dark Heaven's formations?",
    "Did the Mutated Water Dragon destroy Donghu Stronghold and the related Yangtze River Channel League strongholds, and why was no Moving Formation trace left?",
    "Who created or controlled the Gate or rift that corrupted the Water God Dragon, and how is that power related to Dark Heaven?",
    "Why did Honglan corrupt the Water God Dragon and what is the full extent of her role in the Hubei incidents?"
  ],
  "safe_through": 479,
  "temporary_decisions": [
    "Render 광폭화 as Berserk and preserve the System Status distinction.",
    "Render 장수 돌침대 as Jangsu stone bed and 효자손 as hyojason, each with an explanatory footnote when used.",
    "Retain established jang and geun measurements, along with established renderings of live-fish sashimi and bone-in sashimi.",
    "Continue rendering 수염 as whiskers; distinguish Force, Sword Energy, Hellfire, and Water Breath.",
    "Render 원정 as Origin Essence, 내단 as inner core, and 꽃뱀 as flower snake with an explanatory footnote."
  ],
  "version": 1
}

## Reading copies

## Chapter artifact 475

# Chapter 475

The Mutated Water God Dragon.

When you got right down to it, this bastard was a dragon too.

It might have been closer to an *imugi* than a true dragon, considering it could neither roam beneath the azure heavens nor wield a dragon pearl.

But there was one problem…

This identity-confused bastard knew how to use Breath.

And not just any Breath. A fucking powerful one.

*Kwaaaaaaaaaah!*

I stared with my mouth hanging open as an enormous sphere of water spread across a radius of several dozen *jang*.

The ground, built up layer upon layer over centuries by sediment flowing down from the Yangtze, collapsed by nearly half in an instant.

*What the hell…*

A force far beyond ordinary water pressure.

That was not merely an enormous quantity of water gathered together and fired all at once.

Since the immense qi belonging to the Mutated Water God Dragon had infused the sphere of water, it was only right to call it Water Breath from now on.

*Water Breath in the Murim.*

It would have been more natural if some insane undead monster had insisted it was from Atlanta, Georgia, in the United States.

I stared in horror as the Water Breath vomited by the Water God Dragon pulverized everything in its path.

At the same moment, three figures shot away from the ground being reduced to a wasteland.

“Mimi, blow up the water orb!”

“…You’re completely insane. I felt murderous intent for a moment there without even realizing it.”

“That’s normal. This old man has wanted to kill you about five times already.”

One lunatic provoking a horned snake. One rejuvenated old man. And one old man who could hardly look any older.

When I confirmed the three of them were safe, a sigh of relief escaped me.

*Thank goodness they dodged it.*

If they took a direct hit from Breath with that level of destructive power, even a Supreme Peak master could not escape unharmed.

The Water Breath fired by the Mutated Water God Dragon was that powerful. It contained qi that far surpassed the Breath of the Black Wyvern I had personally killed in the past.

*What the hell? It was strong, but I don’t remember it being this strong…*

Was it the effect of Berserk? Or had it finally drawn out all the power lying dormant within it?

I did not know the exact cause, but it unquestionably had something to do with the pupils that had suddenly turned black.

And my goal right now was to bring this bastard down by any means necessary.

—Krrrrrrk.

Its utterly black pupils gleamed.

The monster let out a low growl at the humans who had dodged its attack at the speed of light, then opened its maw again.

*Goooooong.*

Along with an immense flow of qi, the waterspouts circling around it surged upward as though being sucked into its wide-open jaws.

*Already…?*

A second Water Breath.

Even the Wyvern, the modern world’s most prominent dragonkin monster, could not use Breath this quickly or this frequently.

This thing was on an entirely different level.

Before the completed Water Breath could be fired, I swung with all my strength and struck the bridge of its nose, which was slowly spreading wider.

“You wide-mouth bastard!”

*Kwaang!*

The enormous head shook with a deafening boom.

The sudden jolt to its body made the sphere of water, which had been nearing completion, falter. But despite accomplishing what I’d intended, my expression hardened.

*It’s different.*

A punch thrown with everything I had.

Yet the resistance I felt through my fist was incomparable to what I had experienced only moments earlier.

The changes that had occurred in the Mutated Water God Dragon did not consist solely of Breath. Its body had also grown stronger.

To put it simply, it felt like my fist, which should have smashed through ten wooden boards, had stopped after breaking only five.

I clenched my teeth.

*Damn it.*

I should have changed my approach according to the situation, but my thinking had been too complacent. I grabbed White Flame, which I had shoved between the dragon’s scales.

*Store in Inventory. Open. Summon.*

*Shhk!*

In the blink of an eye, White Flame, which had melted into empty space, passed through my Inventory and reappeared in my grasp.

It was a movement that minimized every action. That would have been impossible without the System, and even I had only recently begun mastering this advanced application.

The moment the shaft of White Flame settled into my hand, I had already finished preparing and was bringing it down in a single strike.

*Fwoosh!*

Blue-white flames rose over the transparent spearhead, burning the air and evaporating the moisture filling the surroundings.

Beyond the flames slicing through the dense, foglike steam stood the bridge of the black-scaled monster’s nose.

“Shut your mouth.”

Heavenly Strike.

*Kwaaaaaaaaaah—schk!*

The immense flames summoned by burning internal energy split the scales. They burned through flesh and shattered bone.

Even flesh of astonishing toughness could not stop a strike that fused Ten-Thousand-Year Cold Iron with Force.

Behind everything cleaved apart to either side of the spearhead was the nearly completed sphere of water.

*Cut.*

The Water Breath of the Water God Dragon, which had existed for hundreds of years, met the fire dragon’s claw plunging down like lightning from the heavens.

No.

They collided head-on.

*Gooooooong—*

Along with a deafening boom that numbed my ears, red and blue flashes filled my vision.

* * *

That day, the people present at the scene were not the only ones who heard the mysterious roar.

Everyone staying near Dongting Lake heard it.

*Gugugugugung!*

The mountains, rivers, and trees bowed beneath a tremendous boom unlike any peal of thunder.

Commoners who had secluded themselves indoors to avoid the ominous atmosphere were startled and threw themselves facedown on the spot. Government troops wandering near Dongting Lake to investigate the incident dropped even their spears and fled in terror.

Old men patted grandchildren who had burst into tears and gazed at the sky with worried expressions as they muttered,

“It’s a divine spirit. The divine spirit has grown angry and brought down heavenly punishment on someone. What is going to become of this wretched world…?”

They were half right and half wrong.

From the distant past until now, the supernatural being passed down by word of mouth for hundreds of years had truly existed.

But the spirit beast once worshiped as a divine spirit had fallen into an ugly evil beast, and the heavenly punishment delivered by the enraged Mutated Water God Dragon had been blocked by a single human.

Deep in a part of Dongting Lake that no one ever visited, the battle between the human and the evil beast continued even now.

—Kroaaaaaaaaah!

A pained roar shook heaven and earth in every direction.

The monster, its maw torn open, writhed and threw its body onto the waters of Dongting Lake.

*Kwa-gwa-gwa-gwa!*

The river water, mixed with dark-blue blood, surged to a distant height in an instant.

Waves such as one might see only on the distant open sea rose and crashed in every direction. Three figures no larger than specks beside the monster’s enormous body moved one step ahead of them.

*Shweeeeeek!*

Three figures shot forward like arrows.

But one person chose a direction completely opposite to the other two.

Seeing Jeok Cheongang charge alone toward the monster instead of dodging, Mungyeong sent a Sound Transmission.

—Fire King!

But rather than answer, Jeok Cheongang thrust one palm toward the approaching wave.

*Poom!*

With a heavy sound of splitting air, a hole opened through the center of the enormous wave that had been about to swallow his small, aged body. The water evaporated into steam.

A second and third wave soon came rolling in, driven by the monster’s ceaseless, pain-filled thrashing.

But the next moment, they were cleanly sliced apart.

*Shraak!*

A pure-white streak of light had severed the waves through their middles.

Then the Sword Energy scattered by Cheongpung mingled with the spray and reduced the pebbles flying through it to dust. Mungyeong shook the water from his short sword and spoke to Jeok Cheongang.

“There are a few things I want to ask. Did you happen to learn water arts since we last saw each other?”

Jeok Cheongang glanced at Mungyeong and answered bluntly.

“Do you know what this old man hates most in the world?”

“…?”

“First, getting wet. Second, setting a mountain on fire. And third—the last one—watching a mountain burn while I’m soaking wet. Those three things.”

“What does that have to do with—”

“It was about fifty years ago. I had just finished taking a bath I didn’t want in a nearby valley when I came out and saw Mount Jiuhua burning like a torch. In the end, I hunted down and killed every last one of those bastards.”

It was a story every martial artist knew.

After that day, an old man who had been practicing martial arts deep in the mountains of Mount Jiuhua gained the name Fire King.

“Well, things worked out, more or less, and people around me started praising me as the Fire King and whatnot. But some insane bastards pointed fingers behind my back. They called me a murderous old man like a death fiend who could kill a thousand people without even blinking.”

Mungyeong frowned at Jeok Cheongang’s attitude. The old man was not even looking at him and simply continued saying whatever he wanted.

“I have no idea what you’re talking about. What kind of nonsense is—”

“It’s nothing. To put it simply, this old man liked Mount Jiuhua. I liked it even more because it was the first home I had ever had in my life. Through the Great Faction War, I made sure every bastard in the world understood that anyone who touched what belonged to me would be crushed by any means necessary. But…”

Jeok Cheongang walked toward the writhing monster, his eyes blazing as he continued,

“That damned bastard doesn’t seem to know that. Then again, if it had known, it wouldn’t have touched my Disciple without a shred of fear.”

“You really do whatever you please. It sounds like you never learned water arts after all.”

“Damn it. We’ll figure it out somehow.”

“We have no friendship between us, but I would like to tell you to be careful.”

“Do water arts really matter when dealing with one lousy eel? I’ll hunt it down and crush it by any means necessary.”

Cheongpung joined in with an innocent voice.

“Wow. Do eels really get that big? Are they all about fifty *jang* long?”

“I feel murderous intent rising.”

“If you’re going to kill him, ask the Sword Saint for permission and deal with it quietly. Of course, lend a hand before that.”

Mungyeong lightly adjusted his grip on his short sword, then suddenly spoke.

“Did that fellow Jin Taekyung happen to learn water arts?”

“I remember training him in the deep valleys of Mount Jiuhua. I’ve never seen anyone who was that bad at swimming.”

“…Then we’ll have to drag that monster onto land.”

“I agree. I don’t want to lose my Disciple twice.”

If the battle took place underwater, it went without saying that the Water God Dragon would have the advantage.

But there was no other choice.

If they did not step in, Jin Taekyung would drown.

And just as Jeok Cheongang and Mungyeong exchanged determined looks, Cheongpung suddenly spoke.

“Huh? That’s not right. Benefactor is really good at swimming.”

“……?”

“……?”

“It’s true. On the way here, Benefactor… Uh, what was it again? Oh, right. He asked me to call him Aguaman.”

What the hell was that supposed to mean?

The two old masters stopped short, confusion rising in their eyes.

At that very moment—

—Gwoooooooooar!

*Shraaaaaaaaaah!*

Along with a roar echoing from deep beneath the river, a human figure shot up through the surface.

Jeok Cheongang’s jaw dropped when he recognized the familiar face amid the spray exploding in every direction.

“You, you…”

“*Hk—* form up!”

“What did you say?”

There was no time to resolve his confusion.

The instant the words left his mouth, a huge shadow rippled across the rolling surface.

At the same time, a thunderous shout burst from Jin Taekyung’s lips as he landed on the ground.

“Form an attack formation!”

What burned in his eyes was not the look of a martial artist.

It was the look of a seasoned Hunter.
## Chapter artifact 476

# Chapter 476

When was it?

I once saw a line like that in an old wuxia film whose title I no longer remember.

“Martial arts are only vertical and horizontal. In the end, one of us falls and the other remains standing.”

It was true. The countless battles I had fought in the Murim had always ended in one of two ways.

*Either I knocked them down, or they knocked me down.*

Except for the Blood Lord, who had escaped even after losing an arm, the result had always been one or the other—and it had never been me who fell.

But when I plunged into the deep river while clinging to the Mutated Water God Dragon, I remembered another possibility I had temporarily forgotten.

*What if this bastard runs?*

He had effectively been the master of Dongting Lake and the Yangtze for hundreds of years.

They said even a mutt had half the battle won in its own yard. If the bastard decided to run, there was no way I could stop him.

At the same time, I realized that I had been laboring under a serious misconception.

*This shouldn’t have been a battle. It should have been a hunt.*

This was not a life-and-death duel between two martial artists.

To bring down the monster before me, I had to do whatever it took, without caring about the means.

I had lived as a Hunter for seven solid years, yet without realizing it, I had been pretending to be some hidebound martial artist. I couldn’t help letting out a quiet laugh at myself.

*What a stupid thing to do.*

Hunter and martial artist. Martial artist and Hunter.

Both were part of my identity. I was the one and only modern martial artist—and the Murim’s Hunter.

At the indistinct boundary that had nearly been erased, I reminded myself of that fact once more.

*That’s right. This is it.*

It felt like I had awakened from a very long sleep. I landed lightly on the shore and let out a thunderous shout.

“Form an attack formation!”

“……!”

“……!”

“……!”

The flow of the air changed in an instant, and three pairs of eyes widened. Of the three, Jeok Cheongang and Mungyeong stared at me with trembling eyes before speaking.

“I coddle you a little, and now a greenhorn still wet behind the ears dares speak to this old man like we’re equals?”

“The Fire King did a terrible job teaching his Disciple.”

“…I apologize. It slipped out.”

I’d forgotten who was standing here.

I must have lost my head after getting swept up in the moment.

Unlike the two old men glaring at me with sparks in their eyes, Cheongpung responded enthusiastically.

“Benefactor, that was so cool! Mimi! Form an attack formation!”

*Chirik!*

“I swear to heaven and earth that one day, I will turn that snake bastard into liquor—”

Jeok Cheongang’s oath never reached its conclusion.

The enormous shadow wavering across the rolling surface finally burst through the water and revealed itself.

—Kroaaaaaaaaah!

A more savage roar than any before shook heaven and earth.

Powerful qi exploded from the body as large as a small mountain, pressing down on everything around it. The air trembled beneath the Fear it released.

At the center of it all, dozens of *jang* above us in the distant sky, was a pitch-black pupil looking down at us.

When the single eye, formed from darkness without even a speck of light, gleamed, a groan escaped someone’s lips.

“Ugh…!”

Fear of the unknown.

Everyone except Cheongpung and me remained at least partly vulnerable to the Fear emitted by the Mutated Water God Dragon.

Even if they were Supreme Peak masters counted among the greatest in the world, it made no difference.

But…

*I’m here.*

I was a veteran Hunter who had fought monsters until I was sick of them. That was who I was.

I had stood my ground against an undead army numbering in the tens of thousands, with rotten flesh dangling from their bodies as they charged. I had no reason to tremble in fear just because one eel the size of an aircraft carrier had joined the fight.

“Now that I look at you again, you’re practically a fairy.”

The words had barely left my mouth before the back of my head began to prickle. From the listener’s perspective, it probably sounded like complete madness.

But what I had just said was one hundred percent sincere.

*It’s true that this bastard is powerful, but the Arch Lich was much more difficult—and much stronger.*

If the Skeleton King hadn’t helped me back then, I would have died without question.

But the important thing was that I had survived and brought the bastard down. The fear I had felt while facing the Arch Lich had become experience, carved into my body and mind in its entirety.

*And I’m a fast learner.*

Good experiences and bad experiences alike become flesh and blood. Over the past seven years, I had learned how to survive and how to win.

I drew a deep breath.

At the same time, I raised White Flame’s shaft high into the air.

Then I slammed the end down with all my strength. A level of internal energy never seen before rode the shaft.

*Goooooong!*

The wave of qi that shot outward with the deafening boom pushed back the Fear radiating from the dragon.

The heavy pressure that had surrounded us without a single gap dissipated as though an invisible pane of glass had shattered.

“This is…”

“You…”

The astonished gazes of Jeok Cheongang and Mungyeong touched my face. I stared directly at the dragon and opened my mouth.

“First. Don’t get scared for no reason.”

“……!”

“……!”

Everyone carried fears, great and small, inside their hearts. Fear was a force that stimulated those fears and made people experience terror.

But once those fears were erased, we could finally recognize something we had forgotten.

—Krrrrrrrr.

The enormous monster letting out that low growl was not as powerful or frightening as we had imagined.

I kept my gaze fixed on its gleaming, pitch-black pupil and continued.

“Second. From this point on, follow my instructions and beat the shit out of that bastard without mercy.”

Mungyeong’s dry voice pierced my ears.

“I do not particularly care for the process, but the result sounds rather pleasant.”

“You don’t dislike it because of that, do you?”

“What do you take me for?”

“That was a stupid question.”

The Slaughter Saint.

The greatest assassin in all of Murim history.

To an assassin who eliminated a target by any means necessary, the process did not matter. Only the result mattered.

“Old Master.”

“As far as this old man remembers, I never taught you how to deal with an evil beast like that… We can discuss it after we finish the bastard off.”

*Chiriririk!*

After Jeok Cheongang’s curt reply, Cheongpung answered with purple Sword Force instead of words.

It was an atrocious composition consisting entirely of DPS, without either a healer or a tank. Even so, there could not have been a more powerful raid team.

*Four Supreme Peak masters.*

A combination impressive enough to make even a five-star Jangsu stone bed weep.[^1]

Compared to the enormous body of the Mutated Water God Dragon, we were no more than ants. But inside each of us crouched a giant carrying an unprecedented power.

And now, the four giants were going to hunt a colossal monster.

“You’re dead now.”

As if it understood me, the Mutated Water God Dragon raised its enormous body from beneath the surface and roared.

—Gwooooooooooar!

*Krrrrung, kwaaaaaaaaaang!*

With a single roar, dozens of waterspouts rose and came crashing toward us. Between them, the dragon’s battered jaws opened wide.

*Gooooooooong—!*

The air vibrated faster and more powerfully than before.

But before the third Water Breath could take shape, a shout burst from between my lips and pierced everyone’s ears through the wind and rain.

“Spread out!”

*Shwish-shwish-shwish-shwish!*

As though following a prearranged signal, four figures shot away in different directions and took positions around the dragon.

At last, it was time for the hunt.

* * *

Raid.

As reality was invaded by the unreal and Hunters and monsters began killing one another, this word—once used only in fantasy games—became something even a three-year-old child knew.

But none of the billions of people who had survived the Great Cataclysm could have imagined that a raid was taking place somewhere else, beyond time and space, against a strange monster resembling a dragon.

Nor could they have imagined that a familiar face was caught up at the center of it all.

*Tat-tat, shweeeeeek!*

A heavy body shot toward the air, stepping on fragments of stone as they scattered through the sky.

A massive tail passed within a hair’s breadth, smashing into a half-collapsed cliff and raising a blast of wind pressure.

Through his streaming hair, the eyes of the young man Jin Taekyung gleamed.

*If I cut that tail now… No. Don’t.*

Jin Taekyung restrained the hand that instinctively wanted to swing his spear.

He knew exactly what mattered most in this raid.

He had to block the Mutated Water God Dragon’s escape, lure it as far onto land as possible, and kill it like lightning.

If he struck back and wounded it before then, he might instead alert the monster to the danger.

Of course, someone watching the scene had a slightly different opinion.

“You fucking piece of—!”

*I can’t lose the Disciple I only managed to gain in my old age like this!*

But Jeok Cheongang’s movement as he prepared to launch a palm strike at the monster, accompanied by a thick curse, abruptly stopped at the shout that rang out the next moment.

“Old Master!”

“……!”

*Fwoosh, kwaaaaaaaaaang!*

The Scorching Yang Qi that hastily changed direction burned the innocent ground.

For the briefest instant, puzzlement passed through the dragon’s pitch-black eye. Then it changed into the eye of a savage beast.

—Gwoooooooooar!

*Whoom, bang!*

With a roar, the enormous tail swept across the ground like a broom.

Jeok Cheongang leaped into the air at the last instant to evade the attack and exploded in frustration.

“How long are you planning to make us retreat!”

*Kwaang!*

Far above the ground, Jin Taekyung avoided the monster’s body as it came hurtling toward him and answered,

“I told you I’d give the signal!”

“And when is that going to be?”

“I’ll handle it when the time comes, so please stop shitting all over the place! There’s only so much trolling I can take! Do what you’re told like everyone else!”

“……!”

Jeok Cheongang’s eyes trembled.

Some of the strange words prevented him from understanding exactly what Taekyung meant, but he had heard one thing perfectly clearly.

*A dump? This old man is taking a dump?*

He had only recently been worrying that his infirmities of old age might progress to the point where he started smearing feces on the walls. Now the boy he considered his Disciple was saying something that vile to him.

The shout that followed jolted Jeok Cheongang out of his shock.

“Old Master, now! Retreat thirty *jang* to the rear! Cheongpung, move to the bastard’s rear! Mungyeong, take the flank!”

“Yes, Benefactor!”

“What a strange fellow. I said I would follow your intentions, not that you could speak casually to me.”

“For fuck’s sake, I really can’t stand ranged-DPS assholes who refuse to communicate. Just listen to me!”

“……!”

Seeing Mungyeong struck speechless, press his lips firmly together, and silently do as he was told improved Jeok Cheongang’s mood slightly.

*At least he calls me Old Master.*

He should have been angry. Under normal circumstances, he should have been furious.

But seeing Mungyeong called by his bare name like some nobody from next door made Jeok Cheongang grateful that Taekyung had not simply called him Cheongang.

At the same time, he thought he understood Mungyeong’s feelings as he moved without another word.

*What is this strange feeling?*

How should he put it?

Jin Taekyung was radiating an oddly powerful presence right now.

And in Jeok Cheongang’s estimation, it was not the pressure or bearing possessed by a Supreme Peak master.

It was more like…

*A veteran. Yes, exactly. A battle-hardened veteran.*

Jeok Cheongang had lived his entire life as a martial artist. He had never had any connection to the authorities, nor had he ever been a soldier.

Yet for some reason, he felt as though he understood what it was like for a newly deployed recruit to face a battle-hardened veteran.

“What an incredibly strange fellow, no matter how many times I look at him…”

“Hey, Jeok Cheongang! Snap out of it!”

“……!”

At the moment Jeok Cheongang’s eyelids began to tremble, the words he had been waiting for finally rang out—before he could even unleash his anger.

“Now, strike!”

*Shwish-shwish-shwish-shwish!*

The four giants shot forward at the same time toward the Water God Dragon, which had finally left the waters of Dongting Lake and climbed onto land.

[^1]: Jangsu is a Korean brand known for stone beds marketed for their health benefits.
## Chapter artifact 477

# Chapter 477

*Shwish-shwish-shwish-shwish!*

Front, back, left, right.

The instant the Mutated Water God Dragon noticed the four figures shooting toward it from every direction, its one remaining eye widened.

—Krrk!

*When did they…?*

Even in Berserk Status, the Mutated Water God Dragon could tell that the situation was turning against it.

But its reason had been paralyzed by rage, and the immense strength dwelling within its large, beautiful body caused this strange and terrifying evil beast to underestimate its opponents.

Then someone shouted.

That was enough to sever the last thread of reason that had barely sensed the danger.

“Even if everyone curses you, I believe you’re a good guy. Because you don’t have a single rough edge.”

—Krrrrrr…!

A murderous glint flashed in the pupil, almost as large as a grown man.

It did not matter what that tiny, insignificant human had been babbling about.

What mattered was that he was the one who had plucked out every single one of the whiskers that had been the dragon’s pride, its finest weapon, and practically its companion of the soul for hundreds of years.

*Kill him.*

*No matter what it takes, I will kill that fucking human!*

*Whooooooosh!*

The enormous tail, filled with lethal intent, tore through everything in its path.

At the end of that path, one man’s lips curled slightly upward.

“Got you, you son of a bitch.”

*What?*

The Mutated Water God Dragon felt a chill sweep over its entire body, but it was already too late.

With that much force and speed behind it, pulling back its tail was as impossible as recalling an arrow after it had been fired.

*Whoom, boom!*

Everything was crushed beneath the violently swinging tail.

The cliff that had barely been holding together collapsed completely, and the resulting roar swallowed every other sound.

But what awaited the Mutated Water God Dragon was not the exhilarating sensation of crushing its enemy.

It was pain like being burned alive.

*Fwoosh, thk!*

No.

This was not some illusion.

The next moment, the Mutated Water God Dragon saw it clearly.

Between the slowly dispersing wind, rain, and clouds of dust, a spear wreathed in blue-white flames had pierced straight through its large, beautiful tail.

And the smile of the fucking human gripping that spear.

“Got you.”

—……!

* * *

My mother had always been lenient when it came to raising her children.

She never believed studying was the only path to success. Even when she saw my high school report card—sevens in every subject, like a slot-machine jackpot—she ended her lecture with one short remark.

*“Amazing, my son…”*

Hmm. Now that I thought about it, she may already have given up on me halfway by then.

In any case, even my mother made me read books when I was young.

I think it was in elementary school. She saw me making paper airplanes out of an English workbook and flying them around. She handed me a book and told me to read this instead.

The title of that book was…

Oh, right.

*Gulliver’s Travels.*

Even though I had no talent for studying, I enjoyed novels like that. Sometimes, I even tried applying memorable scenes from them to Hayeon.

For example, the scene where the Lilliputians tied Gulliver up with ropes.

*“Mom! Look! I caught Hayeon! She’ll be quiet now!”*

*“Waaaaaah! Mommy!”*

*“No! Hayeon! My daughter!”*

Of course, the results of my curiosity were not particularly good.

When my mother saw her young daughter bound from head to toe with blue packing tape, she screamed. Then she beat the calves of her now-unfilial son with a *hyojason*.[^1]

[^1]: A Korean back scratcher whose name literally means “filial son’s hand.”

But with a tenacity unusual for an elementary schooler, I didn’t shed a single tear.

I did, however, reflect on my carelessness.

*“Next time, I need to tape her mouth shut too, so she can’t scream!”*

Ah, what fond memories.

Time had passed, and the vicious elementary schooler who had bound his much younger sister in blue packing tape could no longer be found.

But the memory of that day remained vivid.

Along with the ambition I had held as a child: to tie up Gulliver just like in the novel.

*Thk!*

That’s right.

Just like now.

Remembering the childhood dream I’d thought I would never fulfill, I spoke.

“Got you.”

—……!

It was more brutal than the way the Lilliputians had tied up Gulliver, but it was undeniably effective.

I had predicted that the bastard would swing its tail. I dodged just before the enormous, hideous thing lashed across my body, then drove my spearhead in with all my strength.

White Flame, the sturdy and transparent divine weapon bearing that name, became a massive nail and pierced through both the monster’s tail and the ground.

*What, did I need a hammer?*

Obviously, my fist.

And I still had plenty of nails left in my possession.

*Open Inventory. Summon.*

*Thk-thk-thk-thk-thk!*

It happened in an instant.

I summoned five spears from my Inventory like lightning and drove them into the bastard’s tail. Then, instead of a hammer, I brought down my fist.

*Boom! Boom! Booooom!*

*Anchoring complete.*

My powerful punch struck the ends of the spear shafts. The sharp spearheads sank deep into the ground and trembled.

*Hayeon, are you watching?*

I shuddered with a thrilling sense of satisfaction as I watched the scene.

The Mutated Water God Dragon screamed in pain.

—Gwoooooooooar!

But to me, its scream seemed a little premature.

Three people who had been waiting for this exact moment were just about to unleash attacks with everything they had.

The fastest of them arrived first and swung a sword at the dragon’s waist.

*Shk—!*

A ghostlike movement.

A speed too fast for even my eyes to fully follow.

Nothing could block the dazzling flash that shot out from the grayish shadow.

Not even the scales hardened further by Berserk Status.

Not even the iron-tough flesh and bones.

It was none other than the Slaughter Saint’s sword strike.

*Shrrk!*

A clear sound of cutting pierced through the confusion of battle and reached my ears.

Mungyeong’s figure, having dealt a devastating blow with the fastest and most concise sword strike in existence, vanished in a blur.

At the same time, a scream of agony burst from the maw of the monster amid blood surging upward like a waterfall.

—Kuaaaargh!

The attack had not severed the torso completely, but nearly one-fifth of its thickness had been shaved away in a single strike.

That reaction was only natural.

But there was one thing I wanted to tell the bastard.

This was not over yet.

“Two more strikes left.”

Before I had even finished speaking, purple Force resembling a sunset shot through the darkness and illuminated it.

*Shwish-shwish-shwish-shwish!*

Dozens of red plum blossoms appeared amid the swirling wind and rain.

That was no illusion.

The path traced by the purple Force imbued with the Zaha Divine Technique, known as the essence of Huashan, was instantly familiar.

*The Plum Blossom Sword Technique.*

If Mungyeong’s sword was a sharp guillotine that severed its target in a single strike, Cheongpung’s Plum Blossom Sword Technique was a dagger that cut and carved dozens of times.

And at this very moment, those daggers had taken the shape of plum blossoms and were burrowing into the split wound.

*Thk-thk-thk! Shrrk!*

The way to bring down an enormous opponent was surprisingly simple.

Either land one powerful blow so overwhelming that the opponent could not help but collapse.

Or keep hitting the same spot.

And hit it fucking hard.

Before the Mutated Water God Dragon could unleash yet another scream, someone came rushing in to deliver a blow that combined both methods.

“Can’t you just fucking die, you motherless evil-beast bastard!”

A streak of flame crossed the battlefield, accompanied by a filthy crack about the bastard’s parents that was wildly unbecoming of his age.

*The Fire King.*

The illegal resident of Mount Jiuhua.

The firebrand of the Great Faction War.

A nationwide thug who had chewed up the Murim with crazier seniority than the water from Bodhidharma’s skull and even hotter martial arts.

Just looking at him made my heart race and my eyes feel hot.

*Ah, fuck it.*

What happened, happened. I had already dropped the formalities anyway.

Once you were riding on the back of a tiger, there was nothing left to be afraid of.

Feeling my blood boil, I shouted with all my strength.

“Go, Fire King! Flame-Extinguishing Divine Fist!”

“You fucking little—!”

I could not tell who he was cursing, because the next enormous boom drowned him out.

*Fwoosh, kwaaaaaaang!*

Flames erupted from the end of his fist and shot forward, vaporizing all the moisture in their path.

Hellfire carrying superheated flames tore into the gaping wound created by the previous two attacks, burning and devouring everything inside.

—Kraaaaaaaaaah!

I remember hearing somewhere that the most painful death in the world was death by fire.

Anyone who saw this scene would have no choice but to agree completely.

Heat filled every direction, hot enough to evoke the image of hell itself, along with the thick, acrid smell of burning flesh.

And in the center of it all, a gigantic monster writhed while engulfed in hellfire.

—……!

The tremendous scream, unlike anything we had heard before, shook the ground and sent the waters of Dongting Lake surging backward.

The thrashing caused by its pain was so violent that even I, clinging to the embedded spears with all my strength, could no longer hold on.

*Thk, thud-thud-thud!*

When Gulliver came to his senses and untied the ropes binding him, what had the Lilliputians thought as they looked up at the giant rising to his feet?

I could not know for certain.

But at least I was neither shocked nor flustered.

“Oh, look at you.”

It made no difference anyway.

The three extreme ranged-DPS addicts—or rather, three Supreme Peak masters—had followed my orders perfectly, and the Mutated Water God Dragon had taken devastating damage.

Even if it pulled out the spears embedded in its tail and gathered Water Breath now, nothing would change.

*Shiiiiing, tap!*

*Seizing an Object Through Empty Space.*

Like the other spears, White Flame had been unable to withstand the force of the tail and was flung into the air.

Then it was sucked into my hand.

I raised the spearhead of White Flame, wet with dark-blue blood, and pointed it at the bastard.

“From now on… hack away wherever you can.”

The voice that slipped between my lips was hot as lava.

The three people who had grown accustomed to waiting for my orders sprang into action like beasts freed from their leashes.

*Snap!*

Jeok Cheongang, Mungyeong, Cheongpung—and me.

The first and strongest raid team in the Murim shot toward the enormous body of the monster writhing in agony.

*Shweeeeeek!*

Four superhumans took steps toward four different directions.

And four streaks of Force carried unprecedented power.

* * *

*Shwish-shwish-shwish-shwish! Shrrk!*

*Fwoosh, kwaaaaaaang!*

East, west, south, north.

Above, below, left, right.

There was no gap through which the dragon could escape and no direction in which it could dodge.

They were everywhere.

And nowhere.

The body as large as a small mountain was practically the largest target in the world. Its mangled tail could overturn the river and the ground, but it could not touch the figures moving like flashes of light.

The Mutated Water God Dragon.

The greatest advantage of this corrupted being, which had grown enormous over hundreds of years, had now turned into its greatest weakness.

—Kroooooooooar!

There was no shield that could not be broken.

No door that could not be opened.

In a span of time too short to even call a moment, the monster’s body was carved apart by dozens of streaks of Force and left in a pitiful state.

Its dangerously beautiful jet-black scales shattered into pieces.

Its flesh and bones, so hard that ordinary blades could not even scratch them, had already been cut and crushed beyond recognition.

*Craaaack, shaaaaaah!*

Dark-blue blood burst from the wounds and soaked the earth.

The thunder and lightning that had struck without pause began to fade.

The storm winds and rain also slowly died down.

And so did the life of one being.

*Shrrk!*

—Krrk…!

Pain assaulted the Mutated Water God Dragon once more.

Its body writhed feebly, and then a figure appeared in the pupil of its eye.

A young human with a familiar face.

Its enemy.

The one it absolutely had to kill.

—Gwoooooooooar!

And the presence of one man alone—Jin Taekyung—roused the monster’s last fading reserves of strength.

*Gooooooong—!*

At the very moment a massive sphere of water, what someone called Water Breath, was about to be completed after the dragon poured out every last bit of its strength…

The young human vanished from before its eyes.

Then, the next moment, the Mutated Water God Dragon heard a low, level voice.

“You’ve worked hard.”

*Thk!*
## Chapter artifact 478

# Chapter 478

I hadn’t been aiming for that spot from the beginning.

No. I hadn’t even known it was there.

It was like trying to find a squirrel hiding in a dense forest. You simply couldn’t spot it easily.

The Mutated Water God Dragon’s body was truly enormous, and I had never imagined that a weakness could exist in a part of its body that it had protected so thoroughly throughout the battle.

But…

*That.*

There it was.

A weakness capable of severing the windpipe of this gigantic monster.

And I did not let the perfect opportunity to end this fight slip away.

*Thk!*

—Krrk…!

Living creatures were truly strange. They constantly evolved, compensating for their weaknesses to suit the environments around them.

If even humans, with their life expectancy of barely a hundred years, did that, then surely this sublime being, which had lived for hundreds of years, would be no different.

*Was it coincidence? Or fate?*

Either way, it didn’t matter.

The most important fact at this moment was that there had been exactly enough space for one scale to be missing at the back of the monster’s neck, which was covered in its strongest scales.

And I hadn’t missed that gap.

“You’ve worked hard.”

Those final words of encouragement were a privilege only the victor could enjoy.

I had driven my spearhead precisely into the area beneath its neck—where a human’s Adam’s apple would have been—and tightened my grip around the shaft as I shoved it deeper.

*Thk—!*

The dragon’s scaled jaw trembled, accompanied by a short groan like it was sucking in a breath that would never come.

Then its jet-black pupil shook, and the sphere of water that had nearly finished forming at the back of its wide-open maw began to scatter.

*Shhhhhhh!*

The incomplete Water Breath was nothing more than ordinary water.

I did not dodge the deluge pouring down toward the crown of my head. I took it all head-on.

The unusually cold waters of Dongting Lake soaked me from head to toe, and my mind settled into calm.

*I won.*

At the same time, a thrilling sensation surged up my spine.

The end of a long and fierce battle.

I had survived once again and driven a spearhead into the neck of a powerful foe. And as always, the end of a life-or-death battle could be reduced to two words.

Vertical and horizontal.

The victor standing tall and the loser collapsing.

Even an evil beast that had lived for an immeasurably long time could not be exempt from this absolute law of the jungle.

*Whoooooosh. Splash!*

The body that had once held unparalleled resilience and power gave way, then fell onto the waters of Dongting Lake.

Through the spray rising high into the air, I saw an eye blinking slowly and a snout trembling faintly.

No.

I heard it.

—You’re exactly the same.

“……!”

The moment I heard someone’s voice echo inside my head, the strength left my hand, which had been about to drive the spear in once more and finish severing the dragon’s windpipe.

As I stared at the enormous eye of the Mutated Water God Dragon as though bewitched, I felt my body suddenly stiffen.

*What the hell…?*

The monster’s appearance, gleaming entirely in jet black and carrying an ominous murderous aura, could no longer be found anywhere.

Like storm clouds clearing after a day of pouring rain, clear and deep eyes resembling the blue sky were now looking at me.

—There is no need to be surprised. After living for around five hundred years, one naturally acquires abilities like this.

“Sound Transmission?”

—Perhaps it would be more accurate to call it mental intent.

The Mutated Water God Dragon—or rather, this divine being also known by another name, the Two-Horned Beast of Dongting Lake—calmly sent its thoughts to me.

—You do not know me, but I know you. You look exactly as you did when I saw you in a dream long ago. I had forgotten it, thinking it was nothing more than a confused dream… Yes. This, too, must be the natural order.

A dream? The natural order?

*Damn it, what the hell is going on?*

“This is… I mean…”

—Huh.

My hesitation, as I searched for something to say, must have looked rather amusing. A growling laugh escaped the blood-soaked corner of the Water God Dragon’s mouth.

—You can neither understand it nor should you try. It is nothing more than the grumbling of an old imugi that failed to ascend because its cultivation was lacking. If there is one thing I regret, it is that I have no time left.

The Water God Dragon’s words were true. Its body had already reached its limit and stood on the verge of death, while the light was gradually fading from its deep eyes.

*Damn it.*

Even if I regretted it now, the water had already been spilled.

I bit down on my lip.

I felt sorry about the Water God Dragon’s death. And to be perfectly honest, I also felt disappointed.

This mystical being had regained its senses moments before death. It was an important key to solving the mystery.

*Dark Heaven.*

There was no way that a divine and wise imugi had become a mad evil beast that slaughtered humans for no reason.

Someone must have intervened. And if so, Dark Heaven—at the very top of the list of suspects behind every incident currently taking place in the Murim—could not be excluded.

“Who did this, and how?”

It was a short question, but it contained everything.

Yet the Water God Dragon’s mental reply that immediately followed went beyond anything I had expected.

—See for yourself.

“Excuse me?”

In answer to my question, the Water God Dragon simply blinked.

*Slither.*

Blue liquid filled its enormous eye. The thing everyone called tears slowly slid down its scales. The moment it touched my body, I understood what the Water God Dragon had meant.

*Ding.*

> **System**
>
> **Water God Dragon** wishes to convey a portion of its memories to you.
>
> **Memory Fragment** **Acquired**.
>
> The power contained within **Memory Fragment** is leading you into the Water God Dragon’s memories.

Along with the System notification ringing in my ears, the Water God Dragon’s tear spread out like a curtain before my eyes.

*Shhhhhhh.*

Along with the cool sensation of water, the world came to a stop.

* * *

It was exactly what its name suggested: a fragment of memory.

The Water God Dragon’s five hundred years were contained within it in their entirety. But perhaps because of the effects of its mutation, some parts had broken away. Some memories were blurred, while others remained clear.

And the beginning of it all was its birth.

—Guruk?

Somewhere deep beneath the waters of Dongting Lake, a tiny newborn creature looked around in confusion.

It was surrounded by swaying aquatic plants that moved as though dancing and an uncountable number of underwater creatures.

The subjects who sensed the birth of a divine being swam joyfully through the currents.

That day was a joyous one—the day a new master of Dongting Lake was born, and the day a grand enthronement ceremony was held.

—Guruk? Guk!

The new master of the river tilted its head with a curious expression like a puppy, then began swimming with its tiny body.

The moment a being born with dazzling wisdom and power began to move, countless creatures followed behind it, and even the river parted to make way.

*Shhhhhhh!*

Its body, slicing through the waters of Dongting Lake with both flexibility and vigor, gradually grew larger.

Silver scales sprouted across its once-small, soft pink body, and imposing whiskers grew quite long beneath its snout.

It was probably around then.

People who witnessed the divine being appear once every few decades—or perhaps even longer—gave it a new name out of reverence.

A name I knew as well.

*Water God Dragon.*

Perhaps because of the two horns on its forehead, it was also called the Two-Horned Beast. But most people were reluctant to call this beautiful and mysterious being a beast, instead worshiping it as the divine spirit of Dongting Lake.

And the imugi, having received a new name from humans, would occasionally perform acts that truly seemed divine.

It would rescue sailors who had nearly drowned and carry them to remote shores untouched by people. It would also use its innate abilities to calm violent currents.

And that wasn’t all. The one that defeated the evil beast that had once stained the Yangtze with blood was the Water God Dragon.

After defeating the turtle-shaped evil beast in a fierce battle, the Water God Dragon came to rule Dongting Lake and the Yangtze.

Time flowed like water.

After more than five hundred long years had passed, the Water God Dragon had grown beyond comparison with its former self.

It was a benevolent imugi with tremendous strength and profound wisdom, as well as an excellent ruler who knew how to care for its people.

Yet even the Water God Dragon had one concern.

—Huh. Fighting never ends in the Lower Realm.

The devastation it had witnessed throughout its long life was truly horrific.

Humans constantly fought among themselves, and whenever they did, countless rivers of blood and corpses were scattered across the waters.

As two empires fell and wars continued, the Water God Dragon grew worried and weary.

—I have already spent an immeasurably long time in the Lower Realm. When, exactly, will I be able to ascend?

Even when people worshiped it as the divine spirit of Dongting Lake and called it a dragon, the Water God Dragon’s true nature was still that of an imugi that had yet to become a dragon.

For the Water God Dragon, ascension was practically a goal set from the moment of its birth.

But its cultivation progressed so slowly that it came to resent the heavens, and enlightenment never seemed to arrive.

Then, news brought by a school of fish was enough to stir the curiosity of the weary Water God Dragon.

—You say a human has appeared? But no one has visited that place for the past several decades.

An uninvited visitor had entered the deepest, most secret, and most perilous region of Dongting Lake, a place no human had set foot in for a very long time.

Suddenly curious, the Water God Dragon went to the place it had once used as its dwelling. The moment it arrived, it realized that something had gone terribly wrong.

—What is this…!

The Water God Dragon of the past was not the only one to be shocked.

I was the same, staring at the scene through the fragment of memory.

*That couldn’t be…*

Something sticky and unpleasant slowly crawled up my spine.

Overcome by disbelief, doubt, and the shock of being struck in the back of the head, I muttered blankly.

*…A Gate.*

There was no doubt.

Having passed through Gates hundreds, no, thousands of times by then, I was certain.

The black energy pouring in steady streams through the cracks between the enormous rocks was unmistakably mana.

*What the fucking hell…!*

My vision went dizzy, and every kind of profanity echoed inside my head.

If I had not been inside the Water God Dragon’s memories—if I had been able to speak aloud and move freely—I would have smashed everything around me. I would have screamed until my throat split open.

*Fuck, a Gate. Mana!*

My head felt as though it would burst from the countless thoughts racing through it. The shout I could not release scattered at the tip of my tongue.

Eyes wide with shock and fury, I stared blankly at what was unfolding before me.

—Stop! I said stop!

The master of the lake used its entire body to block the countless subjects charging toward it.

The teeth of the fish exposed to demonic qi were sharper than saw blades, and their scales had been dyed completely jet black.

—Please, stop!

But the desperate mental plea could not reach the fish already mutated by demonic qi, and the Water God Dragon was forced to make an extremely difficult decision.

If those strangely powerful and violent fish escaped this place, all of Dongting Lake and the Yangtze would be stained with blood.

A sacrifice was necessary for the greater good.

—…I am sorry.

The battle that took place in the deepest waters of Dongting Lake ended, naturally, with the Water God Dragon’s victory.

But the Water God Dragon was not even given time to grieve.

This wise imugi, which had lived for hundreds of years, understood what it had to do and used its own body to block the enormous rift that constantly poured out ominous energy.

—I do not know what you are, but things will not go as you wish.

*Rumble, rumble, rumble!*

It was the longest and fiercest battle of the Water God Dragon’s entire life.

For seven days and nights, while their strength remained evenly matched, the waters of Dongting Lake and the Yangtze roiled violently, and the people on land grew afraid, believing that the divine spirit had grown angry.

And I already knew the outcome of that battle.

—Krrr…

The Water God Dragon had lost its dazzling intelligence and fallen into an evil beast. It let out a low growl.

It had protected its territory and subjects by absorbing most of the demonic qi, but it could not withstand all that power.

*Hissss.*

Both its eyes slowly turned red.

Yet the last grain of reason remaining inside it caused the Water God Dragon to surge out of the water.

It was the will of an old imugi that wanted to find the culprit behind this terrible atrocity.

*Shhhhhhh!*

On a dark night, the blackened waters parted.

The Water God Dragon rose as though ascending to heaven, and its red pupil reflected a person sitting on a moss-covered rock and splashing their feet in the water.

“The energy here is nice. Coming all this way was worth it.”

A clear, gentle voice.

A dazzlingly white nape.

And a silver hairpin securing long black hair twisted up.

*…Honglan.*

Along with the name of one person surfacing in my mind, the entire world surrounding me shattered into pieces.
## Chapter artifact 479

# Chapter 479

The world collapsed, then was rebuilt once more.

The red pupils filled with ferocity, the surging river water, and the beautifully carved silver hairpin all vanished. What filled their absence was reality outside the memory.

*Whoooooosh.*

I slowly blinked. The curtain of water that had wrapped around my entire body scattered, and the changed surroundings came into clear view.

At the same time, time—which had been frozen as though someone had pressed a pause button—began to move again.

And then, in the next moment, the cold air around me and the System notifications came crashing down like a dam that had burst all at once.

*Ding. Ding. Ding.*

> **System**
>
> **Memory Fragment** has ended!
>
> The Quest information has been updated because the **Mutated Water God Dragon** has regained its reason!
>
> In accordance with the updated Quest information, the mission is recognized as successful!
>
> Surprise Quest, **Corrupted Spirit Beast**, has been successfully completed!
>
> You have gained a tremendous amount of EXP and Fame!
>
> **Level Up!**
>
> **Level Up!**

Along with the Level Up notifications, a mysterious power breathed new vitality into my exhausted body and replenished my depleted internal energy.

But why was it that I could barely breathe?

*Honglan. It was Honglan.*

Yes. It had been her.

The Lower District Sect member who had survived the Dongting Lake tragedy alongside Ju Wongong. A breathtaking beauty capable of swaying an entire nation.

The owner of the hairpin stuck in my hair was the one who had corrupted the benevolent imugi and stained Dongting Lake and the Yangtze with blood—the mastermind behind every incident that had taken place in Hubei Province.

*Why hadn’t I realized it? Where had the lies begun, and where had the truth ended?*

*Gate. Mana. Honglan. Dark Heaven.*

Countless questions and thoughts flashed through my mind in an instant. My overloaded brain felt as though it might burst.

As I trembled at the unbelievable reality, I spotted three figures shooting toward me.

I also saw Jeok Cheongang’s distorted face at the very front.

“You bastard, how dare you—!”

Come to think of it, the scene looked like something anyone would misunderstand.

The conversation I had shared with the Water God Dragon and the time I had spent inside the Memory Fragment had both taken place in an incredibly brief instant. And then, after standing there perfectly fine, I had suddenly begun acting strangely.

Jeok Cheongang’s furious bellow snapped me back to reality, and I shouted like a bolt of lightning.

“Old Master!”

“……!”

We were the kind of people who could understand each other’s intentions with nothing more than a glance.

The moment Jeok Cheongang recognized the emotion in my shout, an exclamation mark appeared in his eyes. At the same time, the fist he had been driving forward forcefully changed direction.

*Whoom, kwaaaaaang!*

It had been a difference of no more than a hair’s breadth.

The Fist Force that had narrowly missed the Water God Dragon slammed into the surface of the lake, which had already grown calm.

The heat carried by the Scorching Yang Qi was so intense that every drop of moisture within a radius of several jang evaporated in an instant.

The Water God Dragon was currently at death’s door.

If it had taken an attack like that, there would not even have been time for one final conversation.

“You bastard, why—!”

—Were you worried about your Disciple? What a good Master.

“Gasp!”

It was obvious that the mental intent the Water God Dragon had sent out had not reached me alone.

Jeok Cheongang sucked in a short breath and took a step backward. Mungyeong and Cheongpung arrived immediately afterward, their expressions changing as though they had seen a ghost.

“What in the world was that just now?”

“Uh, even Mimi can’t do something like that.”

……*Shlick.*

Our reflections appeared in the Water God Dragon’s deep, clear eyes. Jeok Cheongang asked in a trembling voice.

“What in the world are you?”

—Some call me a divine spirit. Others call me a monster. You will have to find the answer to that question yourself.

*Grrr.*

The Water God Dragon exhaled with difficulty and continued sending its mental intent.

—As my final act, I should thank you. If you had not stepped forward, I would have remained an ugly evil beast until the very end…

The mental intent that had rung clearly inside our minds gradually faded.

By then, the light was draining from the Water God Dragon’s clear eyes.

*Is it dying? Just like this?*

I looked at Mungyeong with the last of my hope, but the man who also bore the sobriquet Divine Physician merely shook his head with a grim expression.

“It’s already too late. Even if a Great Firmament Immortal came in my place, it couldn’t stop this.”

—You speak the truth, one who walks between life and death.

At those words, which had precisely seen through one man’s identity, Mungyeong’s neatly arranged brows twitched.

“You… know me?”

—Although I failed to ascend to the heavens, I am a being that cultivated for a long time. I saw all of you here in my dreams.

What exactly had been happening in the dreams the Water God Dragon claimed to have?

The Water God Dragon was an imugi that had lived for five hundred years. Even though it now stood on the verge of death with all its strength exhausted, there remained within it a depth and mystery beyond my imagination.

As though gazing at something beyond human understanding, the Water God Dragon stared into the empty air over our shoulders and sent out its mental intent.

—Unfortunately, this is as far as I am permitted to go. Although I cannot reveal the heavenly patterns… yes, I suppose it would be all right to leave behind one gift on my final journey.

A gift?

None of us were given time to express our questions.

In the next moment, my eyes widened at the faint cloud of light spilling from the blood-soaked corner of the Water God Dragon’s mouth.

*Shhhhhhh.*

It was a pearl that cast off a gentle glow.

As though lifted by an invisible hand, it slipped out from the corner of the Water God Dragon’s mouth and floated into the air. Then it trembled on its own.

*Whoom.*

A vibration traveled through the air.

At the same time, the black stain that had occupied a considerable portion of the pearl melted away and vanished. Whenever it did, the pearl began to shrink noticeably.

*This is…*

What I could see with my eyes was not all there was to it.

I could feel the size and depth of the energy contained within the pearl, and the sight unfolding before me brought one word to mind.

*Purification.*

And finally, when all the changes had come to an end, an irrepressible exclamation escaped someone’s lips.

“Ah.”

*Shhhhhhh.*

By then, the pearl was radiating a light far brighter than before.

Although its size had clearly diminished until it was about the same as an ordinary pill, the crystal of energy, now purified of every impurity, contained an infinitely clear and profound power.

*So pure.*

A truly powerful crystal of energy.

Just as all of us were gazing at it with awe—

*Slither.*

The crystal of energy slowly drifted through the air and stopped in front of me. At the same time, the Water God Dragon’s mental intent rang out.

—This is my Origin Essence. Humans call it an inner core.

“……!”

—Although it is insignificant compared to what it once was, it will surely become a great source of power. Please use it where it is needed.

There was no reason to refuse such an offer.

I stared at the crystal of energy with trembling eyes, then reached out and caught it.

*Ding.*

> **System**
>
> **Water God Dragon’s Origin Essence** acquired!

The System notification rang in my ears.

After giving me everything it possessed, the Water God Dragon slowly blinked.

Its eyes, gazing at the sky that had cleared without a trace, held a faint smile.

—Yes. This is where it ends…

*Grrr.*

Along with the fading mental intent, the final breath of the imugi that had failed to become a dragon escaped from its blood-soaked mouth.

Then, everything came to a stop, and silence descended.

I reached out and closed the Water God Dragon’s eyes, which had grown cold and stiff.

*You’ve been through a lot.*

I was the one who had watched the Water God Dragon’s life through the Memory Fragment.

It was a mysterious being that could not be called an ordinary divine spirit beast, and a benevolent existence that had sacrificed itself to prevent an even greater disaster.

So at least in its final moment, it had the right to meet its own death.

Not die as a sacrifice for someone else’s Level Up, but experience a natural death.

But there was one person—no, one bitch—for whom none of that mattered.

*…Honglan.*

I pulled the silver hairpin from my hair.

I silently stared at the object, which gave off a faint scent that even my sensitive sense of smell could barely detect, then spoke to the still-confused Jeok Cheongang.

“Want to go catch a snake?”

“Tell me what the hell is going on… What? A snake?”

“Yes. A flower snake.”[^1]

[^1]: In Korean slang, a “flower snake” is a woman who seduces men and exploits them.

* * *

A clear peal of laughter rang out across the deck of the military ship, drawing everyone’s attention.

Actually, the laughter was not the only reason people were looking.

Any man with eyes had already been sneaking glances at her before even boarding the ship. She was that beautiful.

“Good heavens. Even her laughter is beautiful.”

When a middle-aged man in a military uniform muttered wistfully, the colleague beside him scolded him.

“Your wife should have seen you just now.”

“Stop saying such unlucky things. I’d rather lock eyes with Yama.”

“You’re old enough to know better, and you have five children as cute as rabbits. Are you seriously acting like this?”

“What about you?”

“I don’t have children yet.”

“You have a wife.”

His fellow officer solemnly declared,

“I won’t have one soon.”

“……You’re completely insane. Have you lost your mind?”

“What’s wrong with me? A man ought to take a shot at it at least once.”

“I guarantee you that will never happen.”

“Are you trying to ruin my mood before I’ve even started?”

“No. Someone much younger, better-looking, and more capable than you has already made the first move.”

His words were true. A military officer with broad, handsome features was already walking boldly toward the woman.

“Young Lady. I assume something pleasant has happened?”

Officer Song, the commander of the military ship, flashed his bright white teeth and grinned.

He came from a wealthy family and was handsome himself. Although the woman before him was the kind of breathtaking beauty he might see once or twice in his entire life, he still had a fair amount of confidence.

*She isn’t the daughter of some great household. She’s just a mere singing courtesan.*

And the moment after he thought that, Officer Song’s confidence crumbled without a trace.

“Yes, something pleasant happened. Something very pleasant.”

Her voice was so pure it seemed to cleanse the soul. Her smile was like a hydrangea in full bloom.

A seductive yet pristine beauty flowed from her—pristine, yet too lofty for anyone to approach.

Officer Song began stammering without realizing it.

“D-do you, do you mean it?”

At his flustered appearance, the woman—Honglan—covered her mouth and laughed.

Her eyes curved like half-moons, and the officers who had been sneaking glances at her without pause let out anguished groans.

*How dare those bastards.*

Officer Song glared at his subordinates, then opened his mouth with his heart pounding.

“It’s a shame. It would be wonderful if I could share that pleasure with you, Young Lady…”

Honglan smiled faintly at his deliberately trailing words.

“I’m not sure. I’m afraid I might trouble our Officer Song’s heart with careless words, so I’m hesitant.”

*Our? Officer Song?*

There was no doubt. This was the green light that supposedly appeared only between a man and a woman who had feelings for each other.

Filled with courage, Officer Song shouted loudly.

“On the honor of my ancestors, that will absolutely never happen!”

“Oh my, how brave you are. Then I’ll tell you specially, Officer Song. Could you bring your ear a little closer…?”

“Yes, yes!”

Officer Song felt his heart pounding as he leaned his ear toward Honglan.

Then her sweet, warm breath tickled his ear.

“The truth is, I used the imugi living in Dongting Lake to kill a great many people.”

“What?”

“But that imugi just died. It’s a shame, in a way, but at the same time, I’m glad.”

Officer Song slowly raised his head and stared blankly at Honglan.

He had no idea what this woman before him was talking about, or what he had just heard.

“Young Lady, what does that—”

“It’s exactly what you heard. I believe you’ll understand me, Officer Song.”

Why was it? Honglan’s languid voice caused Officer Song’s expression to grow hazy.

This was not merely a man’s romantic feelings toward a woman. It was an irresistible attraction, nothing less than a chain that seized a person’s emotions and soul.

“Isn’t that right, Officer Song?”

“……Of course. Naturally.”

“That’s wonderful.”

Honglan looked with satisfaction at Officer Song as he nodded as though under a spell, then gazed out over the wide river.

And she gave the man who had become her captive a request—or rather, her first command.

“Shall we change our destination?”

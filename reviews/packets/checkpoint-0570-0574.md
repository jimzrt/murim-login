# Checkpoint Review — 570–574

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

# Chapters 570–574

## Plot

Lee Dongseok enters Busan’s C-rank Gate, Siren’s Black River, under an assumed identity while carrying a dangerous object for an unnamed person. The Gate abruptly transforms: its magic power reading spikes, a rift opens above Haeundae, and a Monster Wave devastates Busan. A massive wave destroys Gwangan Bridge, killing civilians and trapping survivors as Mermen and Sirens attack.

Taekyung and the Skeleton King respond to separate disaster zones. Taekyung rescues civilians while confronting the intelligent Kraken leading the Monster Wave. The Kraken was empowered by magic power Dongseok gave it on behalf of “that person,” then killed Dongseok and opened a rift to the surface world. Taekyung cuts away most of its tentacles and destroys one eye, but the Kraken reveals that humans gave it power and led it outside.

Taekyung deduces that someone may have deliberately fed the Kraken unpurified Magic Gems, increasing the Gate’s magic power until it became a Mutated Gate and then a Monster Wave. When he holds back from killing the Kraken so he can interrogate it, the creature feigns weakness, poisons and paralyzes him with Kraken’s Ink, and charges toward Gwangan Bridge and the survivors awaiting rescue. Taekyung begins resisting the poison with Scorching Yang Qi, the Myriad-Poison Ring, and Unaffected by a Hundred Poisons, then launches a hellfire-coated White Flame spear at the Kraken. The attack’s outcome remains unknown.

## Continuity

- Busan’s Monster Wave destroyed the middle of Gwangan Bridge and caused extensive civilian deaths; survivors remain near the bridge awaiting rescue.
- Taekyung launched a final hellfire-coated spear at the Kraken as it attacked the survivors. Whether the Kraken survived, and whether Taekyung fully overcame the poison and paralysis, is unresolved.
- The Kraken is intelligent, originated in the black sea, and became vastly stronger after absorbing magic power supplied by Dongseok for “that person.”
- The Kraken claims that humans gave it power and led it outside, imitating an unidentified person’s smooth Korean speech. The supplier, motive, and Dongseok’s full objective remain unknown.
- Taekyung suspects that unpurified Magic Gems were used to raise a Gate’s magic power and deliberately trigger the Monster Wave; this remains an unconfirmed deduction.
- Kraken’s Ink applies Poisoned and Paralyzed and temporarily reduces Strength and Agility. Taekyung’s resistance methods are active but their final effect is unknown.
- The Skeleton King killed a Siren and devastated hundreds of Mermen with bone attacks but cannot openly raise an undead army because of his restriction.
- The worldwide Gate crisis continues to resemble the beginning of a second Great Cataclysm, with rising magic power, increasingly powerful monsters, frequent Mutated Gates, and worsening Hunter shortages.
- Go Jun still controls Ares Guild’s legacy and has seized Song Cheonwoo’s children; Song, Cheon Taemin’s location, and Go Se-won’s growing conflict remain unresolved.
- The Nanman mission, Dark Heaven’s rifts and mutants, the Southern Heaven Demon Empress, Jeok Cheongang’s duel with Nangong Cheon, and Ju Hwaran and Sama Pyo’s broken engagement remain open.

## Translation Decisions

- Retain **Siren’s Black River**, **Mutated Gate**, **Monster Wave**, **Merman**, **Siren**, **Kraken**, **Gwangan Bridge**, **White Flame**, **Force**, **Scorching Yang Qi**, **Myriad-Poison Ring**, and **Unaffected by a Hundred Poisons**.
- Render 통합 언어팩 as **Integrated Language Pack** and 마계어 as **Demon Realm language**.
- Use **Kraken’s Ink**, **Poisoned**, and **Paralyzed** for the established System labels.
- Keep the Kraken’s Demon Realm speech fragmented and stop-start, while rendering its imitation of human Korean as smooth, natural English.
- Preserve Taekyung’s blunt profanity and the distinction between a Murim warrior’s role in fighting and a Hunter’s duty to fight and protect civilians.

## Durable state

{
  "active_continuity": [
    "Taekyung is fighting the intelligent Kraken, which has already lost one eye and is now attacking the survivors near Gwangan Bridge.",
    "The Kraken claims that humans gave it power and led it outside, reproducing an unidentified person's Korean speech; the responsible people are unknown.",
    "Taekyung suspects that unpurified Magic Gems were used to increase Gate magic power and deliberately trigger the Monster Wave, but this remains an unconfirmed deduction.",
    "Taekyung was exposed to Kraken's Ink and received Poisoned and Paralyzed status effects with temporary Strength and Agility reductions.",
    "Unaffected by a Hundred Poisons has begun resisting the ink, while Scorching Yang Qi and the Myriad-Poison Ring are being used to purge it.",
    "Taekyung launched a hellfire-coated White Flame spear at the Kraken as it charged Gwangan Bridge; the attack's outcome is unknown."
  ],
  "continuity_sources": [
    574
  ],
  "open_questions": [
    "Who supplied the Kraken with power, led it outside, and possibly engineered the Monster Wave, and why?",
    "Did Taekyung's final spear attack kill or incapacitate the Kraken?",
    "Will Taekyung fully overcome the Kraken's poison and paralysis?",
    "What further evidence can be obtained from the Kraken about the humans behind the disaster?"
  ],
  "safe_through": 574,
  "temporary_decisions": [
    "Use Integrated Language Pack for 통합 언어팩 and Demon Realm language for 마계어.",
    "Use Kraken's Ink, Poisoned, and Paralyzed as the established System labels.",
    "Keep the Kraken's speech fragmented except when it reproduces the unidentified human's smooth Korean speech.",
    "Keep hellfire for 겁화 and preserve Taekyung's blunt, profane battle voice."
  ],
  "version": 1
}

## Reading copies

## Chapter artifact 570

# Chapter 570

Eight in the morning.

Even though the new year had dawned, people's daily lives remained unchanged.

Office workers in neat suits hurried toward work with exhausted faces, while the roads were jammed with cars.

*Honk! Honk—!*

At the ceaseless blare of horns, the middle-aged man behind the wheel of a midsize van rolled up the window he had left half-open and grumbled.

“Fuck. Even after going through the Great Cataclysm, this goddamn road still hasn’t been fixed. Are we supposed to drive or not?”

Swearing while driving was practically an unavoidable force of nature. Especially when driving in Busan.

The middle-aged man laid on the horn at the compact car trying to cut in without using its turn signal.

*Honk!*

But if the driver had possessed even a shred of common sense, there would have been no reason to honk in the first place.

The compact car drifted away, celebrating its lane change with its high beams in broad daylight. When the middle-aged man saw the message plastered across its rear window, he swore again.

> [A child is on board.]

“……Goddamn it. Is the kid literally on fire? Is that why they’re driving like that?”

Only after he had finished did the middle-aged man realize he had cursed. He looked toward the passenger seat and cleared his throat.

“Ahem. That just slipped out.”

The young man sitting beside him answered calmly.

“It’s all right. These things happen.”

His voice was directed at the middle-aged man, but his gaze remained tilted toward the window. The middle-aged man glanced at him before speaking again.

“Your name was…… Dongseok, right?”

“Yes.”

“That’s a relief. With things blowing up all over the place these days, it’s hard enough to remember someone’s full name.”

“These things happen. Don’t worry about it.”

“Ah, I don’t know if I told you last time, but my name is……”

“I’ll call you Team Leader. It’s more comfortable that way.”

The Team Leader blinked in bewilderment. Lee Dongseok had answered without a moment’s hesitation, and now he added:

“And, Team Leader.”

“Uh, yeah?”

“The light changed.”

*Hooooonk!*

The Team Leader snapped out of it at the blaring horn behind him and stepped on the gas. As the van lurched forward, his brow furrowed.

*What an unbelievable little asshole. That young punk.*

After muttering inwardly, the Team Leader soon changed his mind.

*Well, what does it matter if he’s a little rude? We’re only going to see each other for one day. As long as he does the job he was assigned, that’s enough.*

*Still, he’s a hundred times better than some trembling rookie or some loudmouth who only knows how to talk.*

The Team Leader was a C-rank Hunter who had worked as a freelancer for several years.

As such, he knew better than anyone that a guy who fought well and had no manners was preferable to someone likable and polite.

*At least he won’t shit the bed and disappear like that bastard a little while ago.*

They had needed a temporary team member to replace the man who had made a major mistake in a Gate and then gone into hiding. The result was Lee Dongseok.

His résumé was flawless, and based on the Team Leader’s own assessment, his ability as a Hunter seemed considerable. Almost enough to make it strange that he worked as a freelancer.

*Well, good is good.*

These days, finding people was a job in itself.

Even now, the DJs chatting softly on the radio were discussing the main reason for the recent shortage of Hunters.

—We have a comment from Shin Ayoung, a woman in her twenties living in Pocheon, Gyeonggi Province. “A Mutated Gate appeared near my home three days ago. Something like that happened only ten minutes away, and I’ve been so anxious that I’m suffering from insomnia.”

—Oh, no…… You live in that very neighborhood? That’s awful.

—I remember seeing this on the news, too. It was apparently an extremely dangerous situation that could easily have resulted in massive casualties.

—It’s a miracle it stopped just before a Monster Wave. Truly.

The Team Leader turned up the radio volume.

The Pocheon Mutated Gate, which had appeared only three days earlier, was an incident no Hunter could have failed to hear about.

Even Lee Dongseok, who had been staring out the window, seemed to be listening more closely.

—Fortunately, there were no deaths in this incident either.

—That’s right. Because the Monster Wave was stopped, there were no civilian casualties at all, and the Mutated Gate was quickly subdued.

—The Emergency Rescue Team, correct? The one from Peace Guild?

—That’s right. It wasn’t Hunter Jin Taekyung himself who went out there, but Peace Guild’s Emergency Rescue Team apparently put on an impressive performance.

—The rise in magic power readings has become a serious problem not only at home but overseas as well. Our country has been recognized as responding faster and suffering less damage than any other country in the world.

—It’s truly remarkable. Not only Hunter Jin Taekyung and Peace Guild’s Emergency Rescue Team, but all the Hunters fighting monsters in these circumstances deserve our……

As the DJ’s voice continued, the Team Leader discreetly glanced at Lee Dongseok.

“Come to think of it, you’re pretty impressive too, Dongseok.”

“What do you mean?”

“You know what I mean. Raiding in a dangerous time like this isn’t easy.”

As magic power readings rose, monsters grew stronger, and Mutated Gates that once appeared only once or twice a year were now occurring roughly once every three days and making the nine o’clock news headlines.

As he turned the wheel, the Team Leader continued.

“I’m doing this because I have a family, but you’re still in your twenties, and you’re not even the head of a household. Is it youthful ambition or something?”

“No.”

“Hm?”

“I’m only doing what needs to be done. I have to do it.”

His answer was decisive, and his eyes shone with a clarity they had not shown before. The Team Leader blinked at the unfamiliar side of him.

“R-really?”

“Yes.”

“Well, huh. Good for you. That’s some serious professional dedication.”

The Team Leader was taken aback by the young man’s response—especially by Lee Dongseok’s eyes, which shone with such steadfast resolve that *sense of duty* seemed the only phrase for it.

*What the hell is this guy?*

A rude young man burning with a sense of justice. A youth dreaming of becoming a hero in an age of chaos. Something like that.

Whatever the case, he was definitely an unusual guy.

Still muttering inwardly, the Team Leader slowly pressed the brakes. When he parked in the Gate management office’s lot and got out, the team members who recognized the midsize van came rushing over.

“Hey, Team Leader Kim. You made it.”

“You’re here, hyung.”

“You’re early, oppa. But who’s the person beside you……?”

“This is Dongseok. You know him, right? The guy we hired temporarily this time.”

“Ah, is that right? I could tell at a glance. He looks just like someone from Seoul.”

“He probably is from Seoul. Dongseok, these are our team members……”

The Team Leader naturally turned his head, then blinked.

Something about Lee Dongseok’s condition seemed strange.

“Dongseok. Are you feeling sick?”

“…….”

“Hey. Dongseok?”

Lee Dongseok stared silently at the Gate with a rigid expression before wiping the cold sweat from his forehead.

“No. I suddenly became a little nervous.”

“Hmm. Are you all right?”

“Yes. There’s no problem.”

The Team Leader looked at him suspiciously, but now that they had reached the Gate, there was nothing to be done.

The manager of the office responsible for the C-rank Gate located in Haeundae—*Siren’s Black River*—was already shuffling toward them from a distance.

“Oh, Team Leader Kim. You’re here.”

“Yes. We’re a little late.”

“No trouble, right? Got everyone accounted for?”

The Team Leader glanced at Lee Dongseok and nodded.

“Of course.”

“You sure? You know the regulations have been tightened. If something goes wrong, you and me both……”

“Aw, I know. Have you ever seen me or my team cause trouble? You’re going to inspect everything anyway.”

“Things are so bad these days that I can’t help worrying. And I was going to inspect you regardless.”

The inspection ended quickly. After checking every detail, with Lee Dongseok last, the manager grinned.

“All right. Go on in.”

Once they received permission, everyone, including the Team Leader, began moving noisily. Everyone except one person.

At the very back of the group, Lee Dongseok stared at the Gate with trembling eyes.

*Thump. Thump.*

His heart pounded fiercely. He had suffered from cold hands and feet since his days in the orphanage, but now his palms were drenched in cold sweat as if he had developed hyperhidrosis.

*Don’t get nervous. Not until the very end.*

He had a mission. A mission he absolutely had to complete.

Just as Lee Dongseok took a deep breath, the Team Leader, walking at the front, suddenly looked back.

“Dongseok. You really are all right, aren’t you?”

“……Yes.”

“You don’t look so good. And you were slow to answer. You didn’t leave your mind somewhere else, did you?”

“No.”

The Team Leader would never know that the reason Lee Dongseok had been slow to answer was not because his mind was elsewhere, but because he was still not used to the name.

And Lee Dongseok—or rather, he—had not forgotten his purpose for even a moment.

“Don’t worry. I’ll definitely do it.”

“What?”

The Team Leader looked confused for a moment, then turned away with a look that said the young man was strange.

They were already standing at the entrance to the Gate.

“All right, before we go in, everyone together. Safety first, today too!”

“Safety first!”

After the energetic chant rang out, the Team Leader stepped toward the Gate entrance.

“Then, moving in!”

*Whoosh!*

The rippling mana swallowed the people one after another.

As the others entered quickly, Lee Dongseok suddenly lifted his head and looked up at the sky.

It was a January morning. The sky was blue, and the wind was still cold.

And…… this might be the last sky he ever saw.

*There is a mission I need you to undertake.*

Someone’s voice from several days earlier reached his ears, mingling with the wind.

Along with the answer he had given at the time.

*I’ll do it.*

*It’s a mission that could put your life in danger.*

*The former Vice Guild Master saved my life anyway.*

His mother, whose face he had never seen, had apparently given birth to him in a subway restroom.

The newborn wrapped in toilet paper and thrown into a trash can survived by sheer luck, then was sent to an orphanage secretly supported by Lee Jungryong, where he grew up healthy and strong.

*If I can be of help…… I’ll do anything.*

To Lee Dongseok, Lee Jungryong had been a father, and Ares Guild had been no different from the home he had shared with him.

He could do anything for him.

*Leave it to me.*

At that answer, filled with firm resolve, the other person had smiled deeply.

Then he handed Lee Dongseok an object—something now stored deep inside his subspace pocket.

*You absolutely must succeed.*

That was the last thing.

After receiving his orders, he changed everything, from his face to his name, and came down to Busan.

Carrying the extremely valuable and dangerous object close to him.

“I…… will definitely do it.”

His turn had come before he knew it.

Suppressing his fear and steeling himself with a low mutter, he stepped toward the rippling field of mana.

*Whoosh!*

About an hour later, the people outside the Gate saw it.

*Beep beep beep beep!*

A magic power reading rising at a mad pace. And a transformation beginning at a speed that could not be stopped.

*Kiiiiing.*

A tear split open in the air, and a dense breath of death spread across the sandy beach of Haeundae.

* * *

After arriving in Busan via three Teleportation magic circles, I immediately realized it.

No—I could feel it.

—Aaaaaah!

—Aaargh!

*Kwaaaang!*

The countless screams and tremendous explosions coming from far away. And……

*Kuuung!*

The immense mana that shook the earth.

“……Fuck.”
## Chapter artifact 571

# Chapter 571

Busan.

Both before and after the Great Cataclysm, it was one of the three most populous cities in the country.

A very long time ago, a handsome, clever elementary school student who had come to Busan on a family trip used to spend every night practically glued to the window.

*“Taekyung. What are you looking at so intently?”*

*“That leg! It’s sparkling! It’s pretty!”*[^1]

*“Whoa, you’re right. Is she a fit model?”*

*“……Not that kind of leg, Dad.”*

[^1]: The Korean word *dari* can mean either “leg” or “bridge.”

*“Oh.”*

*“That bridge over there! The long, sparkly one!”*

*“Aha. Gwangan Bridge?”*

*“Gwangan Bridge? What’s that?”*

*“That’s the name of the bridge. You must have noticed it earlier too, but it’s definitely prettier at night, right?”*

*“Yeah, yeah! I want to go there! Take me to Gwangan Bridge right now!”*

The father gazed at his demanding young son with an expression of such overflowing affection that he looked like he might die from it.

*“Oh, my son. Look at you, thinking only of yourself while your poor father is exhausted from driving all day. Who could you possibly take after?”*

*“Then can I ask Mom what a fitting model is?”*

*“……You really are my son. Pack your bag.”*

It was one of the unforgettable moments of my life. Visiting Gwangan Bridge hand in hand with my dejected father left a vivid mark on my young mind.

It was impossibly huge and glittering, and beside me stood my father, who had never been able to spend much time with me because he was always busy.

After threatening my father—who was complaining about a herniated disc in his neck—into carrying me on his shoulders, I felt like I had everything in the world.

*“Dad, let’s come again next week, and the week after that! And next month too! Carry me on your shoulders then too!”*

*“Haha. What should I do? If things go the way you want, I don’t think I’ll be able to come next month.”*

*“Why?”*

*“Because if this keeps up, my neck will be broken by the week after next. How many bowls of rice have you been eating a day lately, Taekyung?”*

*“I haven’t had much of an appetite lately, so only five bowls!”*

*“……That’s my good boy. No wonder the night sky looked yellow.”*

It was a happy memory. That day, they talked about all sorts of things together, and the excited young Taekyung proudly told Hayeon and his mother all about it when they returned to the hotel.

Watching him, his father rubbed his neck, gave a quiet laugh, and made a promise.

*“When Hayeon is a little older, and you’re in middle school, Taekyung, let’s come back to see the ocean. All right?”*

*“Really?”*

*“Of course. Here—promise.”*

The promise was never kept.

As his two children grew, there were more and more things to spend money on. When even his wife, who had pushed herself too hard with a side job, fell ill, his father naturally became busier.

On an ordinary day, he died in an extraordinary accident.

But I remembered that promise.

Even though my father was no longer by my side, the sight of Gwangan Bridge from my childhood remained vividly engraved in my mind even after more than twenty years.

And now—

*Ruuuumble.*

Gwangan Bridge was collapsing before my eyes.

“Ah.”

A sigh escaped between my lips before I could stop it.

My mind urged me to get there with every ounce of strength I had, but my body would not move, as though invisible hands had seized hold of it.

*It’s…… already too late.*

It was not a thought I had alone.

The Skeleton King, who had arrived with me, and the mage who had transported us here were also watching the disaster beginning several kilometers away with exhausted eyes.

“N-no!”

The cry of the mage whose name I did not know was hollow, and the scene spread out in the distance below us was overwhelming.

*That’s……*

A wave.

What had struck the place where a promise could no longer be kept—the place crossed by thousands, even tens of thousands, of vehicles every day—was a gigantic wave dozens of meters high.

*Whoooosh!*

Carrying tremendous weight and force, the wave slammed into the middle of Gwangan Bridge, a suspension bridge thirty-five meters high and 7,420 meters long.

The screams of people were swallowed by spray bursting in every direction and blinding white foam, while hundreds of cars traveling leisurely within the speed limit were tossed around like toys.

*Boom! Crash!*

With a deafening roar, the suspension bridge’s towers and anchors shattered.

The hundreds of cables supporting the bridge snapped and instantly became gigantic whips, lashing out in every direction.

*Whoooooosh—boom!*

It happened in the blink of an eye.

People and cars that looked like ants were swept away by the cables and vanished.

Red blood flowed where they had stood, unable even to leave a final scream behind. Chain explosions, the screams of those who had survived by sheer luck, and the frantic blaring of car horns all reached my heightened senses.

*Honk! Hooooonk!*

—Reverse! Reverse right now, you fucking bastard!

—Aaaaaaah!

—Please! Please get my child out! There’s a kid here……!

It felt hazy, as though I were dreaming.

An advanced civilization built on magic and science was crumbling like a sandcastle.

Gwangan Bridge, which held the memories of my childhood, could not withstand the weight of destruction and death and collapsed. Those who survived abandoned their cars and ran for their lives.

Desperately crying out for someone to help them.

—Save me! Please save me!

—Mommy!

And their screams woke me from where I had stood frozen like a statue.

“Ah.”

I had to save them. I had to stop this disaster.

Only a few dozen seconds had passed while I stood still, but hundreds had already died. If I hesitated any longer, thousands and tens of thousands would die.

*Smack!*

I slapped both cheeks as hard as I could. The sharp pain brought me back to my senses.

After spitting out the blood flowing from my split mouth, I grabbed the Skeleton King by the collar without hesitation.

*Grab!*

“W-wait?”

“I’m going. Get a grip.”

“W-wait a second. Where are you going……?”

Before the Skeleton King could finish his question, I completed my running start and threw him out the window with all my strength.

No.

I shot him out.

*Crash! Whoooosh!*

The reinforced floor-to-ceiling window shattered, and the Skeleton King’s body shot outward like a cannonball.

Hearing his scream disappear into the wind, I kicked off the ground with all my strength as well.

I did not forget to leave one instruction for the mage, who had already collapsed from exhaustion.

“Call for rescue using my name. Anywhere—right now!”

I had no idea whether the mage, exhausted beyond exhaustion, had heard me properly or where he would send the request for help.

Right now, the situation before me mattered more than anything else.

*Boom!*

The force of my leap made the high-rise building tremble—the building where the Teleportation magic circle had been installed.

As I shot through the distant sky, someone’s furious shout reached me.

“You lunatic!”

It was the Skeleton King. Using his own power, he had created wings made of bone and was approaching at high speed with powerful wingbeats.

Or he would have, if I had not blocked him.

“Go somewhere else.”

“What?”

“The range is too wide. We’ll split up and cover it.”

A Monster Wave. And it was happening in Busan, a city with an extremely high population density.

The desert or sparsely populated military zones in the footage I had seen through Magic Johnson were one thing, but here in Busan, thousands of people were packed within a radius of just a few kilometers.

I had to stop the disaster from spreading by any means necessary.

“I’ll take the bridge first. You……”

“Damn it. Got it.”

Time was short, so my words were brief, but they were enough for the Skeleton King to understand.

He swallowed hard and looked down into the dizzying depths below.

His gaze swept over the road swallowed by screams and chaos and the people running for their lives. Then it suddenly began to tremble.

“Damn it, what the hell is that now?”

“What else would it be?”

I answered shortly, pulled a spare spear from my inventory, and aimed it at the ground.

Through my greatly enhanced eyesight, it looked as grotesque as any other monster. The scales covering its entire body and the fins extending down to its jaw were repulsive.

*Merman.*

An aquatic monster that lived in an environment like the sea.

The creature had the form of a male merperson, but it was neither beautiful nor kind like the ones described in fairy tales.

The hundreds of Mermen surging out of the sea at that very moment and descending upon the people made that clear enough.

—Ssssss!

—Karruk!

The creatures charged forward, spewing unintelligible cries, barnacle-covered tridents flashing in their hands.

Beyond those flashing points sat a little girl, collapsed on the ground and crying.

“Waaaaah! Mommy!”

“Minhee!”

The child’s crying. Her parents’ screams as they turned around.

And hundreds of monsters charging toward their first prey.

*Now.*

I shifted my center of gravity.

My body, tilted diagonally as it shot through the wind, abruptly angled downward, and internal energy flowing through my dantian burst from the tips of my feet.

*Bang!*

I began a steep descent, stepping on empty air with **Stepping on Empty Air**.

But no matter how quickly I hurried, the girl would inevitably die before I arrived if things continued like this.

*Go.*

After taking a short breath, I scattered the spear I had been aiming at the ground.

*Whoooosh!*

A single spear plunged down like a bolt of lightning from an unreachable height.

Cutting through the wind, erasing space, carrying the two characters for *certain death*—

It pierced its target.

*Splurch! Crunch-crunch-crunch!*

The Merman leading the charge toward the girl, along with a dozen or so monsters around it, turned into a handful of blood.

At the same time, hundreds of Mermen stopped moving and stared up at the sky with their mouths hanging open.

Half ferocity and half confusion mixed in their eyes as I muttered:

“What are you looking at, you sons of bitches?”

*Inventory Open. Summon.*

*Click.*

The moment two spears appeared in my hands, my arms were already swinging toward the ground.

*Boom! Crack!*

Scales harder than steel shattered, and fins tore apart.

One Merman, lucky enough to lose only half its body, let out a mournful death cry.

—Krruk, krruruk!

So noisy.

*Inventory Open. Summon.*

*Whoosh! Boom!*

Around noon, with the sun high overhead, unexpected fireworks exploded.

Sticky blood trickled down the railing of the tilted Gwangan Bridge.

*More. More. One more time.*

*Open. Summon. And summon. Summon again.*

It happened in the blink of an eye. The System operated instantly, and my movements were faster than the wind and more powerful than lightning.

My hand shot out at the same moment as my thoughts, gripping dozens of spears in the span of only a few seconds before scattering them toward the ground.

*Die.*

*Whoooosh—boom-boom-boom!*

They split apart. They exploded.

Those who tried to block the spears with their tridents died together with their weapons. Those who tried to flee died before they could even take a step.

When the girl who had been crouched and crying just three meters away began to hiccup, there was nothing left around her.

“ hic. Sob.”

She looked about nine years old. Muffled by the small hands covering her mouth, sobbing hiccups escaped her.

How did I appear in those enormous eyes?

A monster that had defeated monsters? Or an angel descending from the sky?

I did not know. But one thing was certain.

*Unlike me…… you won’t have any good memories of this place.*

The aftertaste was bitter. After landing lightly on the ground, I crooked one finger instead of trying to comfort the girl.

*Shhh.*

**Seizing an Object Through Empty Space.** Qi stretched out smoothly and pushed the girl away.

Toward her parents, who were running toward her while screaming.

But that family’s misfortune was not over yet.

*Ruuuumble.*

The sea had turned black despite the shining sun.

As I stared at the *thing* concealed within another wave rising dozens of meters into the air, I lowered the tip of White Flame.
## Chapter artifact 572

# Chapter 572

*How did this happen?*

*The thing* slowly blinked, feeling a question rise in its mind.

Having lived its entire life driven by instinct, it found everything confusing now that it possessed advanced intelligence for the first time.

But *the thing* soon understood what had happened to it.

—Hu. Man.

Yes. That human.

A small, strangely shaped species. Those accursed creatures who occasionally invaded and stirred up the black sea where it lived.

For countless years, *the thing* had fought humans, driven by its innate instincts and rage. Today had been no different.

But……

—What. Was. That. Human?

Several dozen humans had invaded the black sea.

Under the weapons and magic of those humans, even the Mermen with their magnificent fins and the Sirens who lured humans with their beautiful songs collapsed, spilling blood.

And just as *the thing*, sensing defeat, desperately resisted the humans, one of them stepped forward.

“Let’s stop here.”

He looked like an ordinary human. He was smaller than a Merman and not as beautiful as a Siren.

But *the thing* realized instinctively.

That human was the only being here capable of killing it alone.

The other humans, however, were different.

“Mr. Dongseok, sorry, what did you just say?”

“What are you doing in the middle of a raid? This crazy bastard. Move it.”

“That’s going to be difficult. I have something I need to do.”

“Something you need to do? Mr. Dongseok, what does that mean?”

“I told you. I’m going to see it through.”

“Wait. Mr. Dongseok, I’m asking because I really can’t understand what’s going on here……”

*Shing.*

“M-Mr. Dongseok?”

“T-Team Leader Kim! That guy……!”

*Whoosh—slash!*

Confusion became disorder. Disorder became an argument. The argument became a battle, and the battle brought death.

*Crack-crack-crack!*

“Ghk, krrk……!”

One against many.

But the difference in strength was overwhelming.

The human who had slaughtered all his fellow humans who stood in his way now stood before *the thing*, which lay wounded on the ground.

Then he held out an object containing a power that was both incredibly alluring and tremendously strong.

He did so with words whose meaning *the thing* could not understand.

“Absorb it. It’s a gift that person is giving you.”

There was no choice.

Exhausted from the long battle, *the thing* possessed neither the strength nor the energy to kill the human before it.

Only the presence of something that gave off an alluring fragrance filled its mind.

Magic power.

It was magic power in the truest sense of the word.

A primordial force *the thing* had possessed since birth—and a meal so delicious that it was impossible to resist.

*Whoooooosh.*

When the brief meal finally ended, *the thing* realized that it had changed.

Its body had grown to a size incomparable to its former self, and tremendous magic power overflowed from within it.

The expansive black sea where it had lived until now looked strangely unfamiliar today.

It was almost as if……

“It’s cramped, isn’t it?”

The human’s voice came from far below.

Without thinking, *the thing* nodded.

Yes. It was cramped. The black sea that had once seemed so vast was far too small and shabby for it to remain in.

Then what should it do now?

“Go outside. There’s a wider sea.”

It was a remarkably clear answer.

Reborn as an entirely new existence, *the thing* looked down at the human who had neatly solved its problem.

—Thank. You.

“……!”

And that was the end.

*Crack! Crunch!*

Even the human who had seemed so powerful was no match for *the thing*, which had been reborn as an entirely new existence.

Wrapping its tentacles around the insignificant, tiny body, *the thing* crushed it in an instant and stirred the power latent within itself.

*Rumble-rumble-rumble!*

At the same time, the space where *the thing* had lived until now—the black sea—began to shake.

Waves filled with magic power swallowed the corpses of the humans and awakened countless Mermen and Sirens sleeping deep beneath the sea.

Beyond the savage roars and beautiful songs, magic power that had surpassed its limits began to writhe.

A dozen or so swirling columns surged up around *the thing* and twisted in every direction.

*Whooooooosh!*

A storm whipped through the previously tranquil black sea and tore open the space.

Beyond the rift, blinding light and a new world—things *the thing* had never seen even once—were revealed.

*Whoosh!*

Nothing could contain the magic power that had surpassed its limits now.

Realizing that the time had finally come, *the thing* became one enormous wave and moved toward the new sea.

Leading countless Mermen and Sirens clinging to its body.

*Crack! Whooooooosh!*

The sunlight it experienced for the first time was painfully hot. The endless blue sea was unbelievably vast. And the sight of humans frozen in terror was more than enough to awaken the murderous nature *the thing* had briefly forgotten.

—Kill. Them.

Monster Wave.

The beginning of another disaster.

—Aah, aaaaaah!

Humans fleeing from the Sirens’ alluring voices turned around as if bewitched, only to become targets for the Mermen.

*Stab! Stab-stab-stab!*

In an instant, screams and death covered the sandy beach.

Humans with special abilities came running, but they were no match for *the thing*.

*Whoom—crack!*

One strike.

With one powerful sweep of its tentacle, a dozen or so humans were crushed like dust.

Humans were truly insignificant and feeble creatures.

—To. A. Wider. Place.

Having claimed the vast blue sea, *the thing* had nothing standing in its way.

After landing nearly a thousand subordinates one after another, it swam beneath the deep surface.

*Whoooooosh.*

Easy.

Everything was astonishingly easy.

Humans were weak, and it was strong. It had to imprint that fact on those worthless things.

*The thing* raised the magic power coiled within its body. At the same time, it churned the water with dozens of limbs that had multiplied from the eight it originally possessed.

*Whooooooosh!*

A wave dozens of meters high rose and shot forward.

Nothing could stop the wave carrying tremendous magic power.

Everything built by human hands broke apart and sank.

A long, enormous thing built over the sea was no different.

*Ruuuumble!*

The wave slammed into the suspension bridge called Gwangan Bridge.

The wide-range defensive magic installed in case of emergency shattered beneath the wave’s immeasurable magic power, and the bridge was severed precisely through its middle.

“Aaaaaah!”

“S-Save me……!”

*Honk! Hooooonk!*

*The thing* looked upon the scene it had created with its own hands.

The collapsing bridge. The screams of terrified humans. The deafening noises spewed out by unidentified objects.

Everything was satisfying.

Or at least it had been, until that happened.

*Whoooosh! Boom!*

It happened in the blink of an eye.

Some two hundred Mermen were reduced to a handful of blood by flashes of light that rained down ceaselessly from the sky.

And then *the thing* noticed the presence of a human floating high above.

—Sky?

Could humans fly?

The question had barely crossed *the thing’s* mind when the human descended gently and touched the ground.

*Splash.*

The human stepped into a pool of green blood and stared straight at it.

Sunlight shattered against the spearhead held at an angle.

—Guh……!

The painfully dazzling light made *the thing* groan.

Then it made its decision.

—I. Will. Kill. You.

At that moment, red light flashed in the two eyes attached to either side of its head, filled with savage radiance.

Dozens of legs slammed into the surface along with its tremendous magic power.

*Rumble! Whooooooosh!*

Another enormous wave surged upward.

Having blocked out the sunlight with the disaster it had summoned, *the thing* shot forward with a tremendous roar.

—Grrrrrrooooooar!

And where the terror of the sea, the Kraken, was headed, a human stood.

* * *

It was perhaps only natural that the wave that struck Gwangan Bridge had not occurred naturally.

In the aftermath of the Great Cataclysm, many structures had been reborn by combining the strengths of magic and science. Gwangan Bridge, one of Busan’s landmarks, was no exception.

*But the fact that the powerful defensive magic on Gwangan Bridge was shattered by that wave……*

The answer was already clear.

The wave contained more than salt and seaweed.

It was because of some existence that had torn apart the boundary of the world and revealed itself in the present age.

I let out a short breath and tightened my grip around the spear shaft.

“Come at me, you octopus bastard.”

And the creature—the Kraken—did not refuse my invitation.

*Whoooooosh!*

Dozens of tentacles flew toward me with an enormous shriek of displaced air.

The suction cups arranged at regular intervals were so large that they looked like black holes.

*Damn it.*

Who the hell had said octopuses only had eight tentacles?

Internally clicking my tongue at the greater-than-expected number, I circulated internal energy through my legs.

*Crack. Boom!*

Spiderweb-like cracks spread across the hard ground before bursting outward like an explosion.

Launched by the recoil, I skimmed between the Kraken’s enormous tentacles.

An arc of White Flame slashed down like a flash of lightning.

*Slash!*

Three or four tentacles as thick as logs were cleanly severed.

They were comparatively thin at the ends, but pain was pain.

The Kraken’s tentacle, which had been about to strike the section of Gwangan Bridge where I had stood only moments earlier, twitched and trembled before slapping against the surface of the water.

*Splash!*

I had avoided the attack, but it was not over.

*This is a bad place to fight.*

Gwangan Bridge had already collapsed, almost split in two, but survivors were still scattered everywhere nearby.

The screams coming from behind me were proof enough.

If I fought the Kraken here, there was a high chance of causing many unexpected casualties.

*At this rate……*

When I considered the battlefield, the surrounding environment, and my objective, only one answer remained.

*Step. Tap.*

The tip of my foot gently touched empty air.

**Stepping on Empty Air.**

It consumed an enormous amount of internal energy, so I could not use it for long. But I had never intended to drag this fight out in the first place.

*Whoooooosh!*

Nothing was easier to attack than a target suspended in midair.

Toward the Kraken’s tentacles, which whipped around as though dancing, I slashed the spearhead downward at an angle.

*Fwoosh—shhhhhk!*

Blue flames split into dozens of strands and shot through the air.

No matter how powerful the Kraken was, it could not withstand Force.

*Slash! Splash!*

The tentacles swinging toward every part of my body were severed in a single stroke.

*Sizzle.*

The Scorching Yang Qi carried by the Force burned through the severed ends as it cleaved them, and the Kraken let out a roar filled with agony.

—Grrrrrrooooooar!

Of all kinds of pain, burns were the most agonizing.

And I did not miss the instant the creature faltered.

*Bang!*

Compressed air exploded from the tip of my foot.

The spearhead held upright plunged down, slicing through the fierce wind.

At its tip was the face of a gigantic octopus.

*Shhhhhhhk!*
## Chapter artifact 573

# Chapter 573

Everything has an order and a progression.

Naturally, the same applied to Mutated Gates.

When a magic power reading broke through a certain threshold, an alarm sounded to warn of danger, and an evacuation order was issued to everyone nearby.

However, the time it took an ordinary Grade C Gate to transform into a Mutated Gate and then reach the Monster Wave stage was only a few dozen seconds.

The reading was so far beyond anything ever recorded that the Gate management office had no choice but to suspect a measurement error.

Their brief deliberation lasted less than a minute before ending with the Kraken tearing through space and descending upon the present world, smashing the Gate management office first.

*Boom!*

And the flames of disaster spread in every direction in an instant.

The Kraken was the terror of the black sea and a king who possessed immense power. And beneath such a king were savage, loyal soldiers.

—Ssssss!

Fins moved without pause, and gills opened and closed.

At the appearance of a Merman emitting strange cries, the intersection, which had been crowded with vehicles and people, fell silent in an instant.

“What the……”

Someone’s bewildered question never reached its end.

*Whoosh—crack!*

It happened in the blink of an eye.

A barnacle-covered trident pierced through a human body and continued flying, punching straight through even a vehicle waiting at the light.

*Boom!*

Vehicle fragments flew in every direction with the sound of an explosion.

As people stared blankly at the unreal scene, danger signals were transmitted through the alarms installed around the intersection and everyone’s smartphones.

*Weeeeeeeeng!*

*Ding. Beep-beep. Bzzzz.*

Noise shattered the silence.

The people looked back and forth between the vehicle engulfed in flames and the Merman standing upright. Only then did they realize the danger right in front of them.

“M-Monster!”

“It’s a Monster Wave!”

“Aaaaaaaah!”

With screams, the countless people moving through the streets scattered in an instant.

Desperate to put even a little distance between themselves and the monsters—to survive—they no longer had room in their minds for rules or laws.

“Fuck, move!”

“W-wait……!”

*Crash! Crack!*

“Graaagh!”

People knocked one another down, and a vehicle that shot forward without regard for the traffic light plowed into a pedestrian crossing the crosswalk.

*Hooooonk! Thud!*

“Ghk!”

Korea had become the most densely populated country in the world after the Great Cataclysm.

And the intersection in Busan, known as the country’s second city, plunged into a pit of chaos and terror in an instant.

But there were always exceptions.

*Whoosh-whoosh-whoosh!*

Several figures pushed against the current created by the fleeing crowd.

There were only four of them, but their calm gazes and lightning-fast movements were proof that they were seasoned Hunters.

“Three o’clock!”

“Okay. All at once?”

“Let’s cut down the ones in front.”

“Don’t let them scatter!”

They had never seen one another before, but a few brief exchanges were enough.

All of them had fought monsters for at least a year and as long as ten, and they knew exactly what they had to do in a situation like this.

*If we can’t stop them here…… we’re finished.*

*We have to tie them down somehow.*

Fortunately, the number of Mermen that had appeared at the intersection was relatively small. Only around a dozen.

They were not particularly high-rank Hunters themselves, but they thought they could somehow hold out and buy time against that many.

“Spread out into an encirclement!”

However, just as they shouted and charged toward the dozen Mermen, they stopped in their tracks, overcome by deep despair.

*Thud. Thud-thud. Thud-thud-thud!*

—Ssssit!

—Ssssss!

The asphalt road trembled.

The source of the vibration was hundreds of Mermen charging forward with massive bodies.

The main force had arrived—not the vanguard.

Perhaps even this tremendous number of Mermen was only a fraction of the whole.

“……Ah.”

*We’re finished.*

The same thought came to everyone’s mind.

Even facing a dozen Mermen required risking their lives. For four low-to-mid-rank Hunters to deal with that many was practically impossible.

No. It was impossible without support from high-rank Hunters.

“W-we can hold out while waiting for reinforcements……”

“Hold out?”

A middle-aged Hunter muttered through clenched teeth in response to someone’s almost desperate suggestion.

“Getting hacked to death would be a thousand times faster.”

“……Damn it.”

His entire body felt as heavy as cotton soaked in water. He had to fight, but he could not bring himself to do it.

They had families too. They were people who wanted to live.

The only thing keeping their feet from stepping backward was their sense of duty and resolve as Hunters.

But they would not be able to hold themselves back much longer.

—Aah, aaaaaah!

When had she appeared?

From atop a tall building, the song of a pure-white beauty spread in every direction. A pearl crown rested on her head, and long, flowing hair covered her naked body.

A Siren.

A witch who bewitched those who heard her beautiful voice and led them to ruin. The queen of the black sea.

There was only one of her, but her intense yet wistful voice was enough to conquer the wide intersection.

The people who had been screaming and fleeing in confusion stopped when they saw the half-human, half-bird monster floating in the air like an angel, their faces filled with rapture.

The Hunters gritted their teeth as they resisted her magic, but the situation did not improve.

*Drip. Drip.*

Blood that had flowed between their clenched teeth ran down their chins.

The song continued drilling into their ears. Strength drained from the hands gripping their weapons, and the hundreds of Mermen drawing closer by the moment grew hazy before their eyes.

“Goddamn it……”

Death was right in front of them.

The Hunters—and the nearly thousand civilians—could not escape it.

And today’s massacre would continue without end.

Even if high-rank Hunters came to support them, they could never protect all the millions of Busan’s citizens.

*Fuck. I didn’t think I’d die like this.*

It was too late. It could no longer be helped.

The middle-aged Hunter had given up on everything and was staring at the Siren through blurred eyes when it happened.

—Aah, aaaaaah……!

*Fwooooosh—crack!*

With a powerful shriek of displaced air, the song abruptly stopped.

Dark blue blood like the sea burst outward, and the wings that had been beating powerfully snapped.

The half-human, half-bird monster that had been gliding gracefully through the air like an angel fell onto the asphalt.

*Whoooosh—thud!*

“Huh?”

—Ssssit?

The moment the song filled with bewitching magic power stopped, their minds cleared.

The surviving humans and the Mermen who had witnessed their queen’s death stared blankly at the fallen Siren.

Her eyes were wide open and frozen in place. Her pearl crown had been knocked off by the impact, and her hair had spread apart, revealing something long and pointed jutting out between her breasts.

What was this……?

“Bone?”

The middle-aged Hunter had barely voiced his bewilderment when—

*Whooooooosh!*

A strange noise rang out, and a shadow fell over everyone’s heads.

Those who looked up at the sky saw it.

Something enormous and pure white covering the distant heavens.

And a man standing at its center.

“This body. Descends.”

The arrogant yet powerful voice pierced everyone’s ears.

When golden hair flashed briefly in their vision, the unidentified man pointed toward the hundreds of Mermen and continued speaking.

“You. Die.”

—……!

The hundreds of Mermen opened their eyes wide.

At the same time, the enormous white thing casting a shadow over the intersection flashed with light.

*Papapapapat!*

Bone.

That was what it was.

Sharper than spearheads and as fast as arrows, the bones covered the ground in an instant.

*Fwooooosh! Thud-thud-thud-thud!*

Thousands of bones shot down at once, crushing scales and tearing through fins.

A Merman that barely managed to knock away several bone fragments with its spear was immediately turned into a pincushion by another fragment that came flying at it, then collapsed.

*Thud-thud-thud!*

The rain of bones pouring down from the sky was meant for monsters alone.

Amid that horrifying spectacle, the humans stood frozen as they watched the neatly paved asphalt road become stained with monster blood in an instant.

*Thump. Thump. Crash!*

Only a dozen seconds passed.

Nearly half of the two hundred Mermen collapsed in an instant.

No.

They melted.

One Merman who seemed to be a commander let out an urgent cry at the unexpected situation.

—Ssssit, ssssssit!

—Sss. Ssssit!

Mermen were monsters with considerable intelligence, as befitted half-human, half-fish creatures.

At their commander’s order, they moved in perfect formation and built a wall with the enormous scallop shells strapped to their backs.

The unidentified man—the Skeleton King—clicked his tongue.

“What insolent wretches. How dare you resist this body?”

But even so, the outcome did not change.

The Skeleton King’s power existed in a realm that Mermen could never approach.

“I shall make you pay dearly for the crime of defying a king…… Hm?”

*Rrrrk. Boom!*

Sensing something strange, the Skeleton King abruptly turned his head.

Far away, the swarm of Mermen pouring toward him like a colony of ants filled his golden eyes behind the mask.

“……Would you look at these bastards.”

There were more than five hundred at a glance.

And as the Skeleton King found them increasingly insolent, he remembered a fact he had momentarily forgotten.

*Ah. Undead.*

No matter how urgent the situation was, he could not raise an undead army in the middle of a Busan intersection.

Especially not while nearly a thousand humans were watching him with their eyes wide open.

“Oh. This isn’t right.”

After muttering awkwardly, the Skeleton King suddenly felt anger rising within him.

The face of the wicked human who had placed a restriction on him flashed before his eyes.

*That fucking bastard. How dare he put me through all this shit?*

The thought that the bastard had deliberately assigned him the area where the most monsters had gathered made his breastbone feel twisted.

Then the Skeleton King abruptly turned his head toward the distant sky, in the direction Jin Taekyung had headed moments earlier.

He saw it.

*Whoooooosh!*

*Gwooooooar!*

*Boom! Krrrrr-boom!*

Even from this distance, the enormous tentacles were clearly visible and the explosions clearly audible.

The Skeleton King silently watched the scene, then turned his gaze back toward the cluster of Mermen gathered below.

“……Now that I look again, they resemble a girl group.”

It was the first time the hideous Mermen had ever looked beautiful.

* * *

*Whoooosh—boom!*

Seawater surged upward with the sound of an exploding shell.

But unlike the beginning, the attack was much weaker, and the range of the incoming strikes had clearly diminished.

The biggest reason was probably that the Kraken’s nearly thirty tentacles had been reduced to nine.

*Slash!*

No.

Now it had eight.

—Gwooooooar!

“Now that’s a proper octopus.”

I shot forward with all my strength toward the roaring Kraken.

I dodged an incoming tentacle and stepped on empty air to leap higher. Beneath my feet was a gigantic pair of eyes.

It was time to finish this.

*Fwoosh.*

The flames coiling around the spearhead spun sharply.

I poured all my internal energy into it and drove the spear down toward the creature’s eye.

Fire Dragon Divine Spear, Third Form: Takoyaki.
## Chapter artifact 574

# Chapter 574

*Thud!*

The blade of White Flame pierced through the enormous eye.

The Kraken, the terror of the sea, shuddered in agony.

But that was not the end of the pain waiting for it.

*Boom!*

The flames that burst forth evaporated the blood, and the potent qi flowing along the spearhead tore through the Kraken’s insides.

A full three jiazi[^1] of Scorching Yang Qi was more than enough not only to roast one of the Kraken’s eyes but also to inflict grievous internal injuries.

—Gwooooooar!

Overcome by an unimaginable pain it had never experienced before, the Kraken roared and whipped its eight tentacles in every direction.

It was a frantic attempt to shake off its enemy.

But I drove the spearhead deeper as I held on, then slammed my fist into its enormous eye.

*Whoom! Thud!*

I had no particular reason to use my fists and feet when I possessed the divine weapon known as White Flame. But a fist thrown with strength and speed that had long since surpassed the limits of humanity was itself a deadly weapon.

*Thud! Thud! Thuuud!*

Under the fists raining down like rays of light, the Kraken’s massive body writhed once again.

—Ghk, gwooooooar!

*Boom! Splash!*

The eight tentacles slamming into the surface of the water sent up walls of water and raised waves.

I licked my lips after accidentally getting drenched in seawater thick with salt. The sea’s unique briny taste spread across my tongue.

“Stay still. I’m not done yet.”

How many people had died or been injured in this Monster Wave?

The collapse of Gwangan Bridge alone had already caused hundreds of casualties. Every one of them had been someone’s father or mother, or someone’s child whom no one could bear to see harmed.

*You have to pay for it.*

What the Kraken had destroyed was not merely a structure.

What had sunk into the depths of the sea amid the white foam was hundreds of precious lives—and promises made to people who would never be seen again.

*Crack!*

I tightened my grip around the spear shaft. At the same time, the internal energy I released surged through the mythical monster’s body like electricity.

*Boom.*

A small explosion sounded somewhere deep beneath the mollusk’s wet, glistening skin.

—Gaaaaaah! Hu. Maaaan!

I had aimed for its head to end things quickly, but perhaps because of its enormous size, even a devastating blow could not kill it instantly.

But I answered without the slightest hesitation.

“Give up. You’re going to die here anyway.”

That much was an unchanging fact.

At my dry voice, I felt the Kraken’s body stiffen for an instant.

It must have been shocked that a human was using the Demon Realm language, which only monsters with high intelligence could speak.

—You. Are. Clearly. Human.

“Of course I’m human, you fucking bastard. Do I look like an octopus to you?”

All of this was thanks to the System’s **Integrated Language Pack**, but I had neither the need nor the inclination to explain that to the creature.

Instead, I thrust a punch toward its eyelid as it hesitated at the unexpected situation.

*Fwoosh.*

Blue flames flickered over my tightly clenched fist.

The Flame-Extinguishing Divine Fist—the technique that had once turned Tibet’s Potala Palace into a “Crash Mansion.”

The hammer of that mighty Scorching Yang Qi pierced through the Kraken’s magic-power-reinforced skin.

*Gwaaaaaang!*

Even the hardest rock eventually broke if you kept striking it.

And the Flame-Extinguishing Divine Fist, backed by my full internal energy, could bring down not only a rock but also a monster hundreds of times larger than a human.

*Fwoosh!*

The Kraken’s body trembled violently amid a geyser of blue blood.

After thrashing so fiercely that the yachts and fishing boats moored nearby were smashed to pieces, it let out a shallow groan instead of a thunderous roar.

—……You. Human.

“Shut your mouth.”

At last, I could see the end of this desperate battle.

Sensing victory, I pulled White Flame from its eye at lightning speed and drove it downward.

No.

It was just as I was about to drive it down.

—Did you. Humans. Not give me. Power?

“……!”

The spearhead that had been aimed at piercing through the Kraken’s head stopped in midair.

Countless thoughts flashed through my mind. I opened my mouth with a confused look in my eyes.

“What did you just say?”

At my question, the limp body shifted.

The Kraken—it was definitely laughing.

—Interesting.

“Answer my question. Before it stops being interesting.”

—Did I not. Tell you? You were the ones. Who gave me power.

“What do you mean by that……”

Just as I sensed something strange and asked again, the Kraken opened its mouth between ragged breaths.

—It must be cramped. Isn’t it?

“……!”

—Go outside. There’s a wider sea.

I froze.

That was not the Kraken’s voice, and it was not the Demon Realm language.

Unlike the speech until now, the voice that flowed smoothly was unmistakably……

*Korean?*

Yes. It was definitely Korean.

The Kraken was imitating someone whose identity I could not determine.

No—it was closer to reproducing the memory exactly as it had been.

The unfamiliar voice that followed turned my guess into certainty.

—The one who gave me power. The one who led me outside.

A blue stream of blood ran down from the eye that had been burned black, like a tear.

The Kraken looked at me with an eye that was already dead, yet still filled with hatred and despair, and continued speaking.

—They were all human.

“……!”

The moment I heard that two-syllable word—*human*—a chilling cold shot up my spine.

Several circumstances that had never quite made sense flashed through my mind like lightning, then vanished.

The Monster Wave that had progressed so rapidly that no one had been able to respond.

The existence of a Kraken this powerful, even for a named monster.

And the involvement of someone else, which the Kraken itself had admitted.

*If all of this is true……*

*Someone deliberately caused the Monster Wave.*

My teeth clenched at the thought, which was difficult to believe.

An artificially created Monster Wave.

It was something that could not happen—and must not happen.

But……

*Damn it. It’s possible.*

The cause of Mutated Gates and Monster Waves was the total amount of magic power.

If the magic power exceeded the amount a Gate could contain, the two phenomena described above would occur.

And there was definitely a way to artificially increase that amount of magic power.

*Magic Gems.*

At the three words that surfaced in my mind, the scattered pieces of the puzzle began fitting together.

Yes. It was possible with Magic Gems.

If it absorbed a Magic Gem containing a monster’s magic power—an unpurified Magic Gem that had not undergone the purification process at human hands—it could be the only answer to this mystery.

*But who? And why?*

Someone had caused the named monster known as the Kraken to be born by making it absorb Magic Gems, then brought about a Monster Wave and unleashed a disaster.

It was unmistakable terrorism, an atrocity no human should have been capable of committing.

*Who would do such a thing?*

The hand gripping White Flame trembled from the shock. Question after question rose in my mind, leaving it dark and murky, as though covered by clouds.

And ironically, there was only one being who could answer those questions.

“……Tell me. Everything you saw and heard.”

At my voice, muttered as if I were spitting out each word, the Kraken let out a low, rumbling laugh.

—Why. Should I?

“If you don’t tell me right now, I’ll kill you.”

—How frightening. Truly frightening.

The meaning behind its words was obvious mockery.

I pressed the spearhead in slowly to threaten it, but the Kraken continued laughing through its pain without yielding an inch.

—Ask. Your kind.

“You fucking octopus.”

—Kill. Me. Human.

“……!”

I clenched my teeth as hard as I could.

I had to hold back my rising anger—to keep myself from putting a hole through the head of this damned octopus right now.

*Crack.*

I had to kill it. I had to.

I had watched it all with my own eyes—the sight of hundreds of people being sacrificed by the Kraken.

If I included the other monsters under its command, the number of casualties might exceed several thousand.

Even now, somewhere in this city, someone was probably screaming as they died.

But……

“Goddamn it.”

I could not cut off the Kraken’s breath.

Considering what it had done, I wanted to beat it to death a hundred times over, a thousand times over.

But more important was the identity of the culprit who had caused this damned disaster.

If I failed to catch the bastard who had made the Kraken absorb Magic Gems, turned it into what it was now, and brought about the Monster Wave, then this incident would only be the beginning.

*And people would die every time it happened.*

Was it because I had exhausted so much internal energy?

Or because of the unexpected existence of a betrayer?

My body felt as heavy as cotton soaked in water, and a sudden wave of fatigue washed over me.

Feeling the sunlight beating down from above, I muttered inwardly.

*Goddamn it. The weather is pointlessly beautiful.*

That was right.

The weather was fucking perfect, and the situation was shitty enough to match.

I exhaled roughly and pulled White Flame from the Kraken’s head.

*Fsssh!*

Blue blood gushed out along with the white spearhead as it came free.

*I have to keep this thing alive.*

The only witness and source of testimony was a monster.

Feeling the exhaustion come over me, I loosened the hand that had been gripping the spear shaft with all its strength.

*Slide.*

And that was both the only miscalculation I made in this battle and the most painful mistake.

*Whoooooosh!*

“……!”

It happened in the blink of an eye.

The Kraken’s massive body, which had been hanging limp as though half-dead, writhed—and its eight tentacles flew toward me at once.

“Hup!”

*Tap-tap. Whoosh!*

I belatedly came to my senses, stepped on the Kraken’s head, and launched myself into the air.

For a moment, I thought I had avoided the ambush.

Then I realized the Kraken’s true intention.

*Fwoooooosh!*

Black liquid covered the air within a radius of several dozen meters.

This had been calculated meticulously from beginning to end, and I had not left myself enough room to evade every attack after letting my guard down.

*Splash!*

Even though I moved as quickly as possible, I could not avoid all of the wide-ranging attack sweeping toward me.

And the instant the black liquid—perhaps roughly the amount in a cup of milk—touched my entire body, an unexpected System alert rang out.

*Beep.*

> **System**
> You have come into contact with **Kraken’s Ink**!
>
> **Kraken’s Ink** is a deadly poison with tremendous toxicity!
>
> Status Abnormality: **Poisoned** has been applied!
>
> Status Abnormality: **Paralyzed** has been applied!
>
> **Strength** temporarily decreases significantly!
>
> **Agility** temporarily decreases drastically!
>
> **Unaffected by a Hundred Poisons** begins resisting!
>
> Using **internal energy** can rapidly drive out the poison!

“……!”

My body grew heavy along with the System alert.

The black liquid was none other than ink.

And it was a deadly poison with tremendous toxicity.

*Damn it.*

Why had I let my guard down?

Why had I failed to suspect the creature until the very end?

Bitter regret washed over me, but the water had already been spilled.

I drew up Scorching Yang Qi, which countered poison, while putting on the Myriad-Poison Ring I had taken from my inventory.

*Ding.*

Another System alert rang out, and purification began.

But this too was a miscalculation.

The Kraken had accurately seized upon the instant my guard dropped.

And I was not its target.

*Splashhhhh!*

Its massive body surged forward like a ray of light, raising waves.

At the end of its path was Gwangan Bridge, where people who had survived were still waiting to be rescued.

“You……!”

—Human! Try. To. Kill. Me!

The moment was too brief to even be called an instant.

Countless thoughts flashed through my mind.

But the answer had already been decided from the start.

A Murim warrior was someone who fought.

But a Hunter was someone who had to protect others while fighting.

*Crack.*

Though it had drunk its fill of blood, the spear shaft remained cold beneath my tightening grip.

I drew back my shoulder in midair and twisted my waist. Internal energy surged along my spiraling muscles and acupoints, rushing toward the spearhead.

*Fwoosh.*

Beneath the blazing sun, blue flames erupted.

The sunlight pouring down shattered beneath the spearhead.

And then……

*Now.*

*Die.*

I swung my arm with the will to kill.

A spear engulfed in hellfire became a beam of light and shot forward.

*Whooooooosh! Boom!*

Compressed air burst outward, and the sea split apart.

At the end of that path was the Kraken’s enormous body, lunging toward the survivors.

*Boom!*

Blue blood fell like a rain shower.

[^1]: A jiazi is a traditional sixty-year cycle.

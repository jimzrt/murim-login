# Checkpoint Review — 765–769

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

# Chapters 765–769

## Plot

Michael Silbert pressures Jin Taekyung to support his plan to restore the World Hunter Federation and take control through a staged succession involving Cheon Taemin. Jin attacks him but withdraws after Michael makes clear that Jin’s loved ones and the Skeleton King’s identity can be used as leverage. Michael believes Jin will eventually cooperate and expects his plan to succeed within days.

Jin, Team Leader Choi, Magic Johnson, and the Skeleton King determine that Michael orchestrated the Japan operation, the second terrorist attack, and Leviathan’s awakening to expose the Skeleton King rather than target Jin directly. Their three-day investigation of Michael’s past and Siegfried Wassman’s materials finds no way to stop him.

Amid worldwide panic, riots, economic disruption, and civil instability, the UN General Assembly approves the reestablishment of the World Hunter Federation despite opposition and warnings from several major powers. Michael treats the decision as his victory and receives congratulations from the President of France. Jin’s side fails to prevent the Federation’s restoration.

The Skeleton King proposes publicly revealing that he is a monster and having Jin erase him, removing Michael’s leverage. Team Leader Choi believes the public would reject the Skeleton King despite the lives he saved. Jin is horrified and has not accepted the proposal.

## Continuity

- The UN has approved the reestablishment of the World Hunter Federation.
- Michael Silbert expects to become its leader through a staged succession involving Cheon Taemin and Jin Taekyung.
- Michael knows the Skeleton King’s identity and uses that knowledge, along with Jin’s attachments, to control Jin’s choices.
- Michael orchestrated the Japan operation, the second terrorist attack, and Leviathan’s awakening to expose the Skeleton King.
- Jin, Team Leader Choi, Magic Johnson, and the Skeleton King found no actionable evidence against Michael after three days of investigation.
- Michael bears a fresh heat-inflicted wound around his neck, his first injury in more than a decade.
- More than twenty countries are nearing civil war, while riots, fear, and economic disruption are eroding the rule of law.
- The Skeleton King has proposed publicly exposing himself as a monster and having Jin erase him; Jin has not agreed.
- Team Leader Choi believes the public will distrust the Skeleton King despite his past assistance in Sichuan, Busan, Japan, and Munich.
- The unresolved central conflict is whether Jin can remove Michael’s leverage or prevent Michael from controlling the restored Federation without sacrificing the Skeleton King.

## Translation Decisions

- Keep **World Hunter Federation**, **Great Cataclysm**, **second Great Cataclysm**, **Michael Silbert**, **Jin Taekyung**, **Skeleton King**, **Magic Johnson**, and **Siegfried Wassman**.
- Render **마력** as **magical power** and **마정석** as **Magic Gem**.
- Render **소멸** as **Erasure** when referring to the Skeleton King’s destruction.
- Render **길드장님** as **Guild Master** and **진태경 씨** as **Mr. Jin Taekyung** in formal address.

## Durable state

{
  "active_continuity": [
    "The UN approved the reestablishment of the World Hunter Federation after worldwide panic, unrest, and pressure from governments facing civil instability.",
    "Michael Silbert believes the approval has secured his victory and future control of the Federation; the President of France congratulated him directly.",
    "Jin Taekyung and his allies failed to stop the decision despite Russia's support, while more than twenty countries approach civil war and fear erodes the rule of law.",
    "Michael Silbert bears a fresh heat-inflicted neck wound from Jin Taekyung, his first injury in more than a decade.",
    "Jin Taekyung, Team Leader Choi, and the Skeleton King found no actionable evidence after three days investigating Siegfried Wassman's materials and Michael Silbert's history.",
    "The Skeleton King proposed publicly revealing his identity and having Jin Taekyung erase him to remove Michael's leverage.",
    "Team Leader Choi believes the public would not trust the Skeleton King after learning he is a monster, regardless of the lives he helped save."
  ],
  "continuity_sources": [
    769
  ],
  "open_questions": [
    "Will Jin Taekyung accept the Skeleton King's proposal to erase him publicly?",
    "Can Jin's allies find another way to remove Michael Silbert's leverage or prevent his control of the World Hunter Federation?",
    "How will Michael Silbert use the newly reestablished World Hunter Federation?",
    "Can the public be persuaded to accept the Skeleton King's past aid despite his monster identity?"
  ],
  "safe_through": 769,
  "temporary_decisions": [
    "Render 세계 헌터 연맹 as World Hunter Federation.",
    "Render 대격변 as Great Cataclysm and 두 번째 대격변 as second Great Cataclysm.",
    "Render 소멸 as Erasure.",
    "Render 길드장님 as Guild Master.",
    "Use Magic Johnson and Siegfried Wassman as the established English names."
  ],
  "version": 1
}

## Reading copies

## Chapter artifact 765

# Chapter 765

*Whoosh.*

The air inside the private aircraft grew heavy, pressing down on everything within.

By then, the auras flowing from Michael Silbert and me were facing each other across an invisible boundary.

It was a standoff on the verge of exploding, with neither side willing to give even an inch.

But the moment we crossed that boundary and clashed, everything would move in an irreversible direction.

The two of us. Along with one of our deaths.

And I had no intention of backing down from this place.

Now that he had gotten hold of a fatal weakness, taking even one step backward would mean the end.

*Tap. Tap. Crash!*

The coffee cup exploded outward with a crack.

At the same time, I sensed dozens of presences shooting toward us as swiftly as rays of light.

*Bang!*

The alloy door was ripped off in an instant, and a piercing sound rang out.

The loyal hounds entered the private aircraft in the blink of an eye and wagged their tails at their master.

“What happened?”

It was a familiar voice.

Over my shoulder, Michael Silbert calmly spoke to Huginn, who had returned only a few minutes after leaving.

“I believe I told you to wait outside.”

“I apologize. It seemed as though some trouble had broken out.”

“It is nothing. Our guest merely dropped his coffee cup by mistake.”

“I see.”

Huginn glanced at the shards of glass scattered in every direction before continuing.

“I will bring you another one.”

“That will not be necessary. Whatever you bring, my friend will not like it.”

“Then…”

“Go back outside. Do not return until I call for you myself.”

Huginn hesitated for a moment at his superior’s calm but firm tone, then turned around and led his subordinates away.

Once the personal guards had left the aircraft, Michael Silbert suddenly spoke.

“I think it would be best if we stopped here. What do you think?”

“……”

“If this continues, no matter what the result is, we will both lose a great deal. Do you really want that?”

I stared at Michael Silbert before slowly reining in my aura.

I hated it, but what he said was undeniably true.

As long as the world did not realize what he truly was, even if I killed him here and eliminated the threat of future consequences, I would be branded the worst kind of murderer and criminal.

I would have to spend the rest of my life running from pursuit and surveillance worse than those aimed at a public enemy of the Murim, while my family and friends lost their ordinary lives completely.

That was what I feared most, and Michael Silbert had seen straight through it.

“That is much better.”

He brushed the shards of glass from his clothes with a few taps. When he crooked a finger, a new cup and a coffee machine half-filled with coffee floated over.

“Fortunately, I prepared extras. Ah, would you like some as well?”

“If you have plenty of cups you are eager to throw away.”

“I will take that as a no. They were difficult to acquire, so it pains me when they break.”

*Trickle.*

As he carefully filled the cup, Michael Silbert continued.

“Now that you seem to have calmed down, let us get to the point. Help me.”

*Go fuck yourself.*

The words surged up to my throat, but I forced them back down.

Michael Silbert had already seen through the Skeleton King’s identity. He also knew that no matter how furious I became, I could not kill him right away.

Those two weaknesses were the greatest reasons I could not simply storm out of this place.

*Damn it.*

My fist, clenched tightly beneath the table, trembled. I forced myself to speak in a calm tone.

“What if I help you?”

“The World Hunter Federation will take root successfully. Without a single disturbance. Cleanly.”

Michael Silbert dropped a sugar cube into his coffee before adding one more thing.

“Of course, I will be the owner of the newly born federation.”

“That is an excessive amount of confidence.”

“Oh, Jin.”

He let out a small, derisive laugh and shook his head.

“You already know who would sit at the very top if the federation were established under circumstances like these.”

“……”

“Only you and I possess the qualifications to do so. And…”

*Clink.*

The sugar cube melted into the coffee as he slowly stirred it with a teaspoon. Michael Silbert took a sip, and an expression of absolute satisfaction spread across his face.

“After this beneficial conversation ends, I will be the only one who possesses those qualifications.”

“……!”

“By the way, are you certain you do not want any? This coffee has perfect aroma and flavor.”

*Grind.*

My teeth clenched on their own.

At this moment, I felt like the sugar cube in the coffee cup held in his hand.

A sugar cube that slowly melted, regardless of its own will, completing the taste of the coffee.

And then that perfect coffee called the World Hunter Federation would flow into Michael Silbert’s mouth.

A powerful armed organization that disregarded every country and restriction would fall into the hands of a monster wearing a hero’s mask.

*If this continues… it is all over.*

The reason the World Hunter Federation had been praised during the Great Cataclysm was because it had been the sword and shield protecting humanity.

The public good instead of private gain.

They had been heroes who risked their lives to pursue a greater cause instead of immense wealth and power, and after the Erasure of Demon King Asmodeus, they had naturally disbanded.

But Michael Silbert was the exact opposite.

A man who caused disasters without hesitation for the sake of his own interests and power. A monster consumed by endless desire was sitting across from me.

That monster, instead of the true hero who had fallen into an indefinite coma.

“……Cheon Taemin.”

The name slipped from my lips like a groan. Michael Silbert’s face hardened for a moment, but soon a faint smile appeared on it.

“Ah, yes. Sky. He was there.”

*Click.*

There was ease in the hand that set down the coffee cup and in the voice that followed.

“As a matter of fact, I intend to ask him to lead the federation first.”

“What did you just say?”

“I do not understand why you are surprised. He already possesses more than enough qualifications. He is the living savior who rescued humanity from Demon King Asmodeus, the greatest hero in history, and the man who led the World Hunter Federation during the Great Cataclysm. Who could be more suitable?”

The shock felt like being struck in the back of the head with a solid iron club.

Only then did I understand what Michael Silbert wanted, and I bit my lip.

“You son of a bitch… Don’t tell me.”

“Isn’t it terribly unfortunate? Such a great hero, the man who should lead humanity once again and save the world, is too ill to step forward. It is truly the whim of a god.”

“……!”

“But the fortunate thing for the people is that Sky recommended someone else as his replacement. The captain who will lead the newly born ark known as the World Hunter Federation. Another hero of the Great Cataclysm known throughout the world, someone else who stopped the spread of terrorism through a noble spirit of sacrifice.”

Suddenly, I found it difficult to breathe.

Even though none of it had happened yet, I could picture the entire situation as I listened to his voice burrowing into my ears.

Michael Silbert would recommend Cheon Taemin as the Alliance Leader of the federation.

But Cheon Taemin would refuse the position because of his illness, and at the same time recommend Michael Silbert for the seat.

And after that…

“I intend to refuse about three times. I will lower myself and act humble. After putting on that little farce, if you step forward, we will create a very pleasing picture.”

Michael Silbert looked at me with a smile, but I could not smile.

This went beyond simply helping him. It was, in the literal sense, an elevation to power.

Once this series of events, with countless large and small gears meshing together, came to an end, all criticism that he had called for the reestablishment of the World Hunter Federation for the sake of power would disappear completely. Michael Silbert would be led to the throne by everyone’s hands.

Without any disturbance or suspicion.

With the support of Cheon Taemin, the living savior, and me, his greatest obstacle, he would possess impeccable legitimacy.

He would become the next generation’s savior—and a king who had seized overwhelming power.

“You crazy son of a bitch…”

At the groan that forced its way between my lips, Michael Silbert smiled pleasantly.

“Do not worry. If you and your friends willingly follow me, I will also fulfill my duties as the Alliance Leader of the World Hunter Federation.”

“You expect me to believe that?”

“Oh dear. Unfortunately, it seems I have not given you enough reason to trust me.”

“What?”

“You know that everything I said in front of the cameras today was true. The levels of magical power distributed throughout the world have broken through the critical point, and humanity needs the World Hunter Federation.”

He drained the remaining coffee before adding in a calm tone:

“I need that World Hunter Federation.”

“……!”

At those words, something hot surged up from deep in my dantian.

*Grind.*

I glared at Michael Silbert with flames pouring from my eyes.

Both fists were clenched so tightly that they had gone white, ready to erupt like active volcanoes at any moment.

Because of the paltry power he wanted to obtain—because of that—dozens of cities had been destroyed and more than several million people had died.

Was that all?

Black smoke from the forests of collapsed buildings and the streets consumed by flames had even blocked out the sunlight.

The survivors who had barely escaped the sudden disaster were trembling in fear inside bomb shelters and their own homes, clutching their families and friends in their arms.

And yet, what?

“You fucking bastard…!”

*Fwoosh.*

Blue-white flames rose along the fist that had been trembling from the beginning. Powerful Scorching Yang Qi burned the air and melted everything around it.

The next moment, following the fury that had seized my entire body, I thrust out my fist, infusing it with the killing intent that had risen alongside it.

*Whoom! Roooar!*

*Flame-Extinguishing Divine Fist.*

A single punch filled with ultra-high-temperature heat capable of turning everything into ash shot through space.

Toward the monster wearing a human face. Toward the madman who could sacrifice anything for the sake of his goal.

*I will kill him here. No matter what.*

At that moment, I forgot everything in my rage and surrendered everything to it.

And within the world that had slowed to an endless crawl, I saw it.

A dazzling streak of light blocking the fist wrapped in flames.

*BOOM!*

A tremendous roar shook the aircraft in every direction. I endured the shockwave that pushed against my entire body, then stared at Michael Silbert with wide eyes.

At the final moment, the bastard had stopped the Flame-Extinguishing Divine Fist with the sword blade he had drawn like lightning.

*Sizzle-sizzle-sizzle!*

A gray aura resembling its master’s eyes glowed ominously.

From beyond the blade pressed against the blue-white flames, a deeply sunken voice pierced my ears.

“I warn you: if you do not stop here, there truly will be no going back.”

*Shhhk!*

With those words—proof that one final line still remained—I sensed Huginn and the personal guards approaching from behind and closed my eyes.

In the vision that had gone completely black, the faces of my family and friends flashed before me.

*Damn it.*

*Slide.*

The strength drained from my fist, and it separated from the sword blade.
## Chapter artifact 766

# Chapter 766

At some point, I had begun fighting without end.

When I had no power, I fought in Gates for the happiness of my people. After gaining power, I fought to protect them.

But… what an irony.

I had never taken a step back even when facing the threat of death, yet now I was retreating because of a few words.

*Slide.*

The fiercely burning blue-white flames died down.

Without retreating even an inch, I slowly drew back the fist that had been locked against the sword blade.

“That was a wise choice.”

The loathsome voice brushing my ears made my stomach twist. I lowered my fist, trembling with rage.

No. I took advantage of the moment the air around us loosened and thrust out another punch.

*BOOM!*

Another deafening roar rang out, and a wave of scorching heat swept in every direction. At the same time, an enraged shout erupted behind me.

“How dare you!”

*Shh-shh-shhik!*

And at the moment powerful killing intent and sharp, air-splitting sounds hurtled toward me—

“Enough.”

At the quiet voice, dozens of personal guards, including Huginn, came to an abrupt halt.

Michael Silbert conveyed an unspoken order to his subordinates with a calm glance, then opened his mouth.

“I believe I warned you.”

*Grrrrrk.*

The fist and sword blade locked against each other once more, their powerful blue and dark energies trembling violently. I glared at him and replied.

“Yes. You did.”

“Do you intend to see this through to the end, then? Here and now?”

I clenched my teeth.

In my mind, I had already killed Michael Silbert dozens of times. I had broken his limbs, crushed his mouth, and ripped out his heart before bursting it apart.

But this was not the Murim.

No matter what world this was, unless I tore away the mask he was wearing, what I was trying to do would never be tolerated.

“If that had been my intention… I would have done it long ago.”

“You are more reckless than I thought, and even more arrogant.”

“It would be a shame if you thought it was mere arrogance.”

At that moment, Michael Silbert’s expression shifted strangely.

*Slice.*

A faint line of blood appeared on his smooth neck, accompanied by a subtle sound that could only be heard from very close by.

The skin, unable to withstand the immense pressure that had struck in an instant, had been cut a moment later.

“Huh.”

“That was my warning to you. Bear it in mind.”

Michael Silbert calmly replied to my voice, each syllable spat out through clenched teeth.

“I should remove arrogance from what I said earlier and add one more thing. You are more interesting than I thought.”

“You son of a bitch…”

“And thank you for warning me so kindly. At least one thing has become certain.”

“What?”

“Jin. You can never kill me.”

An unmistakable note of amusement seeped into the dry voice that followed.

“Because… at some point, you acquired far too much.”

“……!”

An inexplicable chill ran through me, raising every hair on my body.

It felt as though something sticky and repulsive had stretched out and seized all four of my limbs.

That horrifying sensation of being dragged into a deep swamp made me reflexively knock the sword blade away.

*Crack!*

The two energies mingled for an instant.

Finally, in a flash of light, familiar faces flickered before my eyes. Before I even realized it, I was staggering and breathing harshly.

I did not want to admit it. I could not admit it.

And yet… at the same time, I had no choice but to admit it.

Michael Silbert.

Everything he had said was true.

The moment I severed the life of that man calmly staring at me, seemingly unconcerned with the blood on his neck, my life and the lives of my people would be cut down with it.

They would burn into ashes and disappear without a trace, just like the countless enemies I had defeated until now.

“May I take your silence to mean that my guess was correct?”

I remained silent, and Michael Silbert smiled.

“I look forward to working with you. I will contact you again soon.”

*Swish.*

With a smile that showed he was certain of his victory, he extended his hand.

I never took it. Instead, I turned away.

Tonight, the moonlight never reached Munich.

* * *

Jin Taekyung had left.

Huginn silently watched his back recede into the darkness before opening his mouth.

“Will he cooperate willingly?”

Michael Silbert nodded.

“Without a doubt.”

“But Jin Taekyung’s recklessness is beyond all standards. Has he not always acted in ways that were impossible to predict?”

“Everyone has a weakness. And he possesses one more fatal than anyone else’s.”

“What weakness?”

“Emotion. Jin Taekyung is more emotional than anyone.”

His calm voice continued.

“Someone whose joy, anger, sorrow, and pleasure are so clear is easier to handle than a materialistic person. Wealth and honor can be regained even after they are lost, but people cannot.”

Michael Silbert looked toward his private aircraft, which had been practically destroyed by the aftermath of their clash.

It had been custom-built with every kind of cutting-edge equipment and even Magic, at a cost of hundreds of billions of won. Yet he felt no particular emotion at its destruction.

It was nothing more than a heap of scrap metal.

But people were different. A single life, a single lifetime, was different.

“Jin Taekyung… has more to lose than I thought.”

Perhaps more than I do.

The words that had lingered only at the tip of his tongue, without making a sound, were swallowed back down by Michael Silbert.

He did not want to admit it.

He already possessed wealth that would never run dry no matter how much he spent, along with overwhelming power.

If he also gained the World Hunter Federation that would soon be reborn, he would become the king of this world—truly untouchable by anyone.

And yet Jin Taekyung had more to lose than he did?

*That makes no sense.*

Michael Silbert muttered inwardly and patted Huginn on the shoulder.

“There is no need to worry. In a few days, everything will be concluded successfully.”

“I hope so as well, but…”

Huginn’s gaze continued to follow the back of the man who was no longer visible.

“I am not sure. I do not know whether sending him back like this was the right choice. I cannot shake the feeling that we have made an irreversible mistake.”

“There is no need to feel that way. We had no other choice either.”

“What do you mea—”

*Crash!*

An unfamiliar sound swallowed the rest of his words.

When Huginn turned around, he saw his superior holding a sword that now consisted of nothing but its hilt.

“Guild Master!”

Michael Silbert shook his head at Huginn’s urgent cry, then stared at the shards of the sword scattered around his feet with a strange look in his eyes.

“Well, this is something…”

Only two clashes.

Yet that alone had reduced a cherished sword, crafted from the finest materials and with Magic, to pieces.

If not for the powerful aura that had covered the blade, it probably would not have retained its shape until now.

*He really is more interesting than I thought.*

Michael Silbert had already understood Jin Taekyung’s abilities to a certain extent.

Ever since Jin had first risen to prominence, the eyes and ears of Odin Guild had been fixed on him. Every time a report came in, Michael Silbert had been forced to revise his assessment of the young Asian man.

From a simple recruitment target, to a next-generation S-rank Hunter with considerable potential.

And then… at some point, to the greatest obstacle standing in his path.

*I thought there was no one left except Cheon Taemin.*

That was how it had been. That was how it should have been.

Yet today, calculations that should not have contained even the slightest error had gone completely awry.

*Jin Taekyung.*

Michael Silbert raised his head and looked toward the darkness that had swallowed the young man moments ago.

He pictured the young man, not even half his own age, from head to toe, and once more considered the enormous power coiled within him.

*What if I had used all my power?*

But before long, he let out a derisive laugh.

It was a pointless thought. The reason he had been able to reach his current position was that he had never fought any of the enemies he had faced with all his strength.

The one who uses all his strength wins the battle, but the one who hides his strength wins the war.

And Michael Silbert wanted to win the war.

Not the battle—the war.

He had lived his entire life pursuing dominion rather than survival, and now only the final step toward the throne remained.

*Everything is within reach. There is no need to hurry.*

At least not tonight.

Michael Silbert swallowed the words circling the tip of his tongue and suddenly raised his head toward the sky.

The Munich night sky reflected in his gray eyes was shining more brightly than ever, unlike the sky seen by someone else only moments before.

*Yes. At least not tonight.*

*Crack. Fwoosh.*

Inside his tightly clenched fist, the impossibly solid sword hilt crumbled into fine powder and scattered on the wind.

Michael Silbert was not careless enough to leave an obstacle in the same place after it had once blocked his path.

* * *

Even after I had finished telling them everything, the spacious suite remained filled with heavy air and silence.

*It couldn’t be helped.*

I looked at Team Leader Choi and the Skeleton King, both of whom had gone rigid, and muttered inwardly.

Their reactions were exactly what I had expected.

When a fire was burning on top of your head, no one could remain calm. Given the circumstances, that would be true even if you were not human but a monster.

“This damned mess.”

The Skeleton King was the first to break the silence. After muttering a quiet curse, he opened his mouth with a complicated expression.

“Wicked human. What will happen now?”

“Hmm.”

Under normal circumstances, I would have made a joke. But the matter was too serious this time, and I found it difficult to answer.

The Skeleton King’s thoughts were probably tangled in every possible way.

He must have been filled with confusion over the fact that his identity had been discovered, along with fear about what would happen to him afterward.

As I sat there, unable to speak and merely moving my lips, the Skeleton King opened his mouth in a solemn voice.

“If it is truly difficult to answer, tell me only one thing.”

“Go ahead.”

“Will this body never be allowed to enter the club again?”

For a moment, I did not understand the question. I blinked.

By the time I came to my senses, the tip of White Flame’s spear was already driving into his chest.

*Crack. Crunch.*

“AGH! Aaaagh! It was a joke! A joke!”

“Just die. Please, just die…”

“Please spare me! My ribs! I think I cracked a rib!”

“You thoughtless bastard. Even Myeongnyun Jinsa Galbi[^1] has more sense than you…”

“Mr. Jin Taekyung! Mr. Jin Taekyung! You mustn’t!”

I had definitely lost my temper for a moment.

After briefly experiencing an out-of-body state brought on by rage, I barely came to my senses at Team Leader Choi’s desperate pleas.

Seeing the Skeleton King clutching his chest and trying to force his ribs back into place made my vision turn white again, but I endured through the superhuman mental fortitude befitting a Supreme Peak master.

*Fuck. I think I’m going to suffer qi deviation.*

If I had watched that spectacle for another ten minutes, my qi and blood would have become hopelessly tangled, and I would either have died or been crippled. Michael Silbert would have recruited the Skeleton King as his new right hand while doing a ridiculous little dance.

Fortunately, a visitor arrived one step ahead of qi deviation.

[^1]: Myeongnyun Jinsa Galbi is a Korean all-you-can-eat barbecue chain specializing in pork ribs; its name is used here as an absurd comparison.
## Chapter artifact 767

# Chapter 767

*Bzzzt.*

At the sudden vibration, Team Leader Choi pulled a smartphone from inside his coat.

After checking one of the five—yes, five—devices he carried, he moved his lips toward me.

“Mr. Jin Taekyung.”

The reason he did not say it aloud was obvious. I quickly drew up my internal energy and spread it around us.

*Fwoooosh.*

The moment an invisible barrier of qi sealed the suite without leaving so much as a gap—

*Bzzzt.*

Blue light poured from the screen of the smartphone lying on the table.

In the blink of an eye, it gathered into the shape of a person, and a deep, resonant voice rang out from the hologram.

“I’m sorry I’m late. I just checked your message… But what’s wrong with that guy? Don’t tell me you’ve already gotten into a fight?”

Magic Johnson.

Looking at the towering Grand Mage blinking at the Skeleton King, who had collapsed while clutching his chest, I answered weakly.

“It’s a long story.”

* * *

Unlike the Skeleton King or Team Leader Choi, Magic Johnson’s reaction was brief and clear.

“Fuck.”

Of course, that was not the end of it.

After muttering nonstop about a son and a beach, as well as a certain third hole he normally kept hidden from other people, Magic Johnson rubbed his perfectly smooth, hairless crown.

“This… is truly the worst.”

Only then did one fact I had failed to consider occur to me.

If the Skeleton King’s existence were exposed, I would not be the only one to suffer a serious blow. Neither would Team Leader Choi.

“I’m sorry. I should have been more careful.”

“There’s no need to apologize, Jin. I helped you all of my own accord.”

Magic Johnson waved away my belated apology, then suddenly furrowed his brow.

“But how did he realize it? My illusion Magic should have been perfect.”

Magic Johnson was one of only three Grand Mages in the world.

No—now there were only two.

Given that his meticulously inscribed illusion Magic was involved, its effectiveness and secrecy should have been beyond comparison.

That was why his expression was so tangled with conflicting emotions.

“With Siegfried dead, there’s only one mage left who could see through the true nature of my illusion Magic… But I guarantee you, even Michael couldn’t make her act.”

If Magic Johnson was speaking with such certainty, it had to be true.

I had heard plenty about the other Grand Mage myself, and after decades had passed, most of what I had heard had turned out to be fact rather than rumor.

But even setting that aside, there were already enough clues to point us in the right direction.

And I was not the only one to reach the relevant conclusion at that moment.

“Japan.”

“Leviathan.”

Two voices overlapped.

Although the words were different, they meant the same thing. Team Leader Choi, who had spoken at the same time as me, continued slowly as everyone’s eyes turned toward him.

“As you all know, what happened in Japan was not a simple terrorist attack or Monster Wave.”

“I heard about that from Choi as well. Personally, I believe Michael Silbert is the most likely culprit.”

“But at this point, we need to think about his objective once more.”

“His objective?”

“Why did Michael Silbert awaken Leviathan, which had been sleeping in the depths of the deep sea? And…”

“Why did he deliberately lure Leviathan to Japan when there were so many other countries?”

Taking over from Team Leader Choi, I thought.

The five oceans covered a staggering seventy-one percent of the Earth’s surface, and there was no shortage of countries bordering the sea.

So why had he chosen Japan as the battlefield where Leviathan would run wild?

*And then there was the second terrorist attack that struck places all over the world on that same day.*

The answer to that question already existed.

Just as Team Leader Choi’s next words made clear.

“He calculated everything meticulously from the beginning, taking Japan’s situation at the time and every other factor into account.”

Magic Johnson grasped the meaning behind his words and muttered with a groan.

“Then all of it—including the second terrorist attack—was meant to draw you in?”

“Yes. Without a doubt.”

“But why Japan? If that was the objective, it would have been simpler to lure Leviathan to Korea.”

Team Leader Choi shook his head and continued in a calm voice.

“From Michael Silbert’s perspective, it was the only possible choice. Even setting aside the fact that Korean Hunters are far stronger, our government has been on high alert ever since Go Jun artificially caused two Monster Waves. If magical power had suddenly surged, they would have noticed immediately.”

“The Magic Gem…!”

“That’s right. But Japan had recently been targeted by the first terrorist attack. More precisely, the area around Tokyo must have seemed suitable in many ways.”

This was no ordinary Magic Gem, either. It was an unrefined S-rank Magic Gem.

The amount and concentration of magical power it scattered had been enormous enough to awaken Leviathan, which had been sleeping far away in the depths of the sea.

But around Tokyo, where magical power was already running wild because of the Monster Wave caused by the first terrorist attack, it would not have been easy to notice.

Most importantly, there had been no Gate worth worrying about near Tokyo Bay, which Leviathan had destroyed.

“Yes. Now it all fits together.”

“He drew the outline based on that from the start, then colored it in with the second terrorist attack. Since Japan was fairly far from the major Hunter powers, it would not have been difficult to predict that its own forces would be unable to stop a named monster like Leviathan.”

You could tell just by looking at the Supreme Peak masters of the Murim. Even modern S-rank Hunters differed enormously in strength among themselves.

In that sense, Japan’s S-rank Hunter, Yamamoto Genji, had never managed to leave the lower levels of this pyramid built on the law of strength.

*If he was really as strong as all those Japanese netizens and Japan-worshipping fanboys dickriding him claimed, why had he shown up so late that Leviathan was already dead when he’d had an entire day to get there?*

*It was obvious.*

The Japanese government must have known that, too. That was why they had been forced to swallow their pride and ask for help.

A country that had suffered little damage despite the two terrorist attacks that swept across the world.

An indisputable Hunter powerhouse—and a neighboring country close enough to rescue them faster than anyone else.

That country was Korea, and Korea had me.

No.

*Us.*

“……!”

A chill ran down my spine. I abruptly raised my head as though I had just woken up and stared at the Skeleton King.

He had been listening to the conversation blankly, having even forgotten to set his dislocated bones back into place. At my gaze, he flinched and hunched over.

“I—I was just sitting here.”

“……”

“It was only a joke because things seemed so serious! Don’t you know what changing the mood means?”

“That’s not it.”

“Th—then why?”

Damn it.

A restrained voice slipped through my clenched teeth.

“It was you. From the beginning.”

“You mean this body was the target from the beginning? What in the world are you talking about?”

At that moment, the Skeleton King furrowed his brow.

Team Leader Choi spoke with a deeply grave expression.

“Mr. Jin Taekyung was not Michael Silbert’s target from the beginning. You were.”

“……What?”

“Do you still not understand? The second terrorist attack, Leviathan—everything was carried out with you as the target.”

“……!”

The Skeleton King’s pupils trembled.

Magic Johnson kept his mouth firmly shut as he considered something, then muttered like a sigh.

“So he had already suspected it.”

“He would have needed evidence to turn that suspicion into certainty.”

“Enough evidence to justify casualties on this scale?”

“Do you still not know what kind of man he is? Even if hundreds died—or tens of millions—Michael Silbert would not bat an eye.”

Team Leader Choi’s heavily lowered gaze turned toward me.

His voice was rough, like iron filings scraping against one another, as it forced its way between his lips.

“If he could accomplish his goal. If he could obtain evidence that gave him certainty. He would be able to end all of this immediately.”

“……!”

He was right.

That was all the bastard had wanted: a decisive weakness that would guarantee victory in his war against me.

That was why he had built the entire stage from beginning to end, eliminating any possibility of aid from other countries and creating a situation in which the Skeleton King had no choice but to step in.

*And then… he finally got his hands around that weakness.*

That was not all.

There must also have been a close connection between the reason he had been able to carry out the second terrorist attack so boldly and the International Hunter Federation.

*The greater the damage, the greater the chance that the Federation would be reestablished.*

Just how far had Michael Silbert’s calculations gone?

The question suddenly occurred to me, and I found it difficult to breathe.

It felt as though invisible strings were tightening around my neck. After taking a deep breath, I looked around.

Team Leader Choi. Magic Johnson.

And finally, the Skeleton King.

At some point, all three of them had stopped talking and were looking at me.

No.

More precisely, they were waiting.

Waiting for my tightly closed mouth to open.

Waiting for me to show them the direction they should take.

And after countless thoughts and worries flashed through my mind, I broke the long silence and began to speak.

“I…”

* * *

Three days passed.

Yet everyone remained silent about the enormous boom that had echoed across the vacant lot on the outskirts of Munich, where the Odin Guild Master’s private aircraft had landed a few nights earlier, on the night when a full-blown disaster had swept through.

Of course, the reporters who had left the scene as though they had been thrown out wanted to know what the faint rumble they had heard from a distance really was.

But the German Federal Army controlling the Munich area had given them a firm response.

First: useless questions and attempts to approach the area would be rejected.

Second: anyone who refused to comply would be expelled from the country immediately.

Even the hot-blooded reporters who had bristled at the first clause could only shut their mouths when they reached the second.

With the enormous issue of reestablishing the World Hunter Federation shaking the entire world, getting deported over a needless provocation would have been nothing short of madness.

There were still two key figures in Munich who could not possibly be excluded from the discussion.

One was Jin Taekyung, who had behaved incomprehensibly in front of the cameras the previous night.

The other was Michael Silbert, the one who had lit the fuse on this powder keg.

“Hey, sorry, but have you managed to learn anything about those two?”

“No.”

“Are you saying that because you really don’t know anything, or because you do know something but are saying you don’t?”

“Hmm. Both?”

“In a situation like this, colleagues should help each other out. Those Germans who don’t know how to take a joke are being ridiculously strict. What’s your name, by the way?”

“Franz Meyer.”

“…You’re not German, are you?”

“Most likely. I’m the German who’s strict, foul-tempered, and incapable of understanding jokes.”

“I didn’t say you were foul-tempered—damn it. Sorry. I didn’t mean it.”

“It wouldn’t matter even if you did. But if you’re really sorry, throw me a decent scoop.”

“A decent scoop? Then how about the emergency convening of the UN General Assembly?”

The bearded German reporter let out a short laugh.

“You’re joking, right? Who doesn’t know about that? The meeting started ages ago.”

That was true.

Following the Great Cataclysm, the newly reorganized UN had urgently convened its General Assembly at midnight three days earlier, immediately after the Munich incident. The heads of 185 nations, centered around the six permanent member states, were engaged in fierce debate through a videoconference.

And they had gathered for only one reason.

The proposal to reestablish the World Hunter Federation.

Given the circumstances, this emergency General Assembly was being conducted under exceptionally tight secrecy.

But words had a way of leaking out wherever they went, and influential media outlets had already obtained the information and were keeping a close eye on developments.

“And yet you offer something everyone with half a brain already knows as a decent scoop. Your sense of humor is worse than I expected. You’re in no position to talk about Germans.”

“Hmm, is that so? What if I told you the vote would begin soon?”

The German reporter stopped short.

He stroked his rough beard.

“…Now that’s interesting.”

“I’m glad you think so, but I’m not joking.”

“Are you certain about that information?”

“What in this world can ever be certain? If I had to give you a probability, I’d say about 99.9 percent.”

99.9 percent.

The German reporter quietly repeated the number, so close to perfect, and swallowed.

“That means…”

“Yes. That’s right. The UN will announce it soon.”

The reporter who spoke, Simon, looked about ten years younger than the German reporter standing before him. He continued slowly.

“The World Hunter Federation. The result of the vote concerning the birth of that enormous organization spanning the entire world.”

“……!”
## Chapter artifact 768

# Chapter 768

Marie Antoinette Syndrome.

The name originated from the story that Queen Marie Antoinette’s hair suddenly turned completely white several days before her execution during the French Revolution in the eighteenth century.

Although the exact nature and cause of this strange phenomenon had never been determined, the President of Korea, Baek Hanseong, was certain that its cause was extreme stress.

After all, his current situation was much the same.

*Fuck.*

The profanity he had kept under control ever since his highly publicized debut in politics swirled around inside his mouth.

The sharp-eyed secretary who had been with him since his days as a member of the National Assembly gestured for him to cover his mouth, but President Baek Hanseong did not care.

The entire room was packed with foreigners.

Naturally, none of them were proficient enough in Korean to infer the pronunciation and meaning from the shape of his mouth alone. And they certainly were not free enough to spend their time watching his lips.

It was only natural.

With the rare spectacle of presidents from various countries abandoning all dignity and pointing fingers at one another, why would anyone bother watching his mouth?

“You call that an argument? Of course we have to reestablish the World Hunter Federation!”

“I’m not saying we should never establish it! I’m saying we should put it on hold for now. Don’t you know what ‘on hold’ means?”

“Did you just speak informally to me? Are you insane?”

“You’re the insane one. What are we going to do about the Federation’s overwhelming authority? This isn’t something we can approve half-assedly in a few days without even properly reviewing the revisions!”

“You fucking… What’s your country’s GDP?”

Shouts rang back and forth through the translation devices, accompanied by faces flushed bright red.

For President Baek Hanseong, who held a perfect three-for-three record in the brawls that were a famous feature of Korea’s National Assembly, it was an oddly heartwarming sight.

But after several days of the same situation, he felt as though his head were about to explode.

*What are they, children?*

Of course, it was not always like this.

Sometimes sharp words were exchanged and an uncomfortable atmosphere formed in accordance with international affairs, but the UN General Assembly was supposed to be a place where nations demonstrated their dignity and their leaders showed their character.

However, as the situation spiraled toward the worst possible outcome and the presidents were crushed beneath immense stress and pressure from all sides, they had no choice but to throw off the masks they had been wearing and reveal their true faces.

“We’re all about to die! What do you think will happen if we put off establishing the Federation even now?”

“Exactly! Saudi Arabia strongly supports the establishment of the World Hunter Federation…”

“The Middle East should know when to bow out. You’ve sold more than enough oil, and now you’ve even exported terrorists to the entire world. What more do you want?”

“What?”

At the words of the Russian president, who was old beyond measure, a middle-aged man wearing a turban bulged his eyes.

“How dare you, you dictator!”

“A dictator? That’s rich coming from a king. At least I was elected through fair elections and voting. I wasn’t born into royalty and handed this position like someone else.”

“Ah, are you talking about that fair election where the voter turnout reached 140 percent in the last presidential election?”

“Well, these things happen from time to time. And it’s already in the past.”

More than twenty years ago, Vladimir Furin had become the Russian president for life through the astonishing voter turnout that had surpassed the country’s entire population.

His eyes gleaming, he looked around the room.

Although he had already passed the age of one hundred long ago, he had maintained his health through cutting-edge medical technology and magical potions. He continued in a powerful voice.

“The important thing is that I—and Russia—oppose the establishment of the World Hunter Federation.”

“You…!”

“Let’s be frank. It’s not that I believe the World Hunter Federation is unnecessary. I’m concerned about who will take that position.”

Tap. Tap.

His wrinkled fingers drummed against the table.

The force of the gesture came through the hologram intact, and the representatives of the pro-Federation camp, who had been about to lash out, fell silent for a moment.

“When the establishment of the World Hunter Federation was first discussed, I supported it because I trusted Sky. From the time I met him personally, he seemed like a man with little interest in power.”

“And the circumstances were at their worst as well.”

At the words of the President of the United States, Doramp Junior, Furin nodded.

“Yes, they were. Back then, that damned Asmodeus was sweeping across the entire world.”

“The situation is still serious, but it is not as bad as it was then. I hope everyone will consider that the World Hunter Federation possesses far too much authority for us to make such a hasty decision.”

The Cold War between Russia and the United States had already been over for more than a century. It would have been impossible to say that the deep resentment accumulated over such a long time had completely disappeared, but at least in this room, the two presidents were in agreement.

And that was very welcome news to President Baek Hanseong, who had been the first to argue that the Federation’s establishment should be put on hold.

Especially with the help of another ally who had already promised to stand with Korea.

“Our Zhonghua People’s Republic likewise wishes to express our deep concern once again.”

Chairman Xiao Yang looked at President Baek Hanseong and continued.

“As President Baek of Korea has repeatedly stated, the establishment of the World Hunter Federation must be discussed with great care.”

“Er, Japan also agrees with Kankoku’s opinion…”

“Thank you both.”

*What the hell is that bastard going to say this time?*

President Baek Hanseong hurriedly cut off Prime Minister Koizumi before he could dump shit all over the discussion. He leaned toward the microphone fitted with a translation device.

“As I have already said several times, the World Hunter Federation is an issue that must be handled carefully. Deciding the matter after only three days would be far too hasty—”

“Only three days? Hasty?”

The President of France cut in with a derisive laugh.

“Are you unaware of what has happened outside during those three days?”

“That…”

“I don’t know what the situation is like in Korea, but France has already suffered five large-scale riots. Insane doomsday cultists have poured into the streets screaming, and all business and production have already ground to a near halt.”

“…Please, just listen to me for a moment.”

“If you’re going to repeat the same thing we’ve already heard for three straight days, I must respectfully decline. Half of the Louvre Museum has burned down. What more do you possibly have to say?”

President Baek Hanseong was rendered speechless. Without realizing it, he rubbed his throbbing temples.

*That damned bastard.*

Everyone knew that the French president had risen to his current position with the support of the Odin Guild.

But the reason Baek could not easily refute him was that everything he had said was true.

*Michael Silbert.*

One word from a hero with tremendous public support had set fire to the powder keg of a world filled with anxiety and fear.

Half the world’s population had watched him in real time as he announced the coming of a second Great Cataclysm, and the flames had spread into reality in less than a day.

Demonstrators of a scale bordering on a riot.

The people who had poured into the streets, seized by rage and fear, had very little patience left. It was only natural that flames soon began to rise throughout the cities.

The police? The military?

Their calls, made while fully armed and demanding that the demonstrators disperse immediately, could not reach the ears of people who had already lost half their reason.

If that was the situation in France, one of the ten most advanced countries in the world, the state of every other country was obvious.

“What the people want now is a result. A result that will reassure them. A result that will guarantee the lives of themselves and their families.”

“If the reestablishment of the World Hunter Federation fails… our country is finished. At the very least, the presidential palace will burn, and I won’t come out of it intact.”

“We have no choice but to support it wholeheartedly. The movements of our military factions are already deeply suspicious.”

“You’re insane. You’re opposing it in this situation? Are you watching a fire across the river because you think it’s someone else’s problem?”

The spotlight was bright.

But everything around it was dark.

A small number of developed nations lived amid civilization more advanced than ever before. But out of the 185 countries belonging to the UN, how many could truly enjoy all of that civilization?

Even after Demon King Asmodeus had been defeated, hunger and civil war had not disappeared. More than a few nations were clutching the deep wounds left by the Great Cataclysm while struggling to keep their governments intact.

And for those caught in such circumstances, this incident was not merely a powder keg exploding.

It was a nuclear detonation.

A nuclear detonation that would soon swallow the entire country.

If things continued like this, it was obvious that enraged citizens and military factions—not monsters—would burn down the presidential palaces.

“We can’t delay any longer!”

“Let’s vote!”

“We do not trust the Security Council or the permanent members! We demand a full vote!”

It was not just one or two people.

As shouts erupted simultaneously from every corner of the room, President Baek Hanseong realized that the long meeting was finally drawing to a close.

*This… can’t be stopped anymore.*

Of course, the UN Security Council still possessed immense authority.

The United States, the United Kingdom, France, Russia, and China—the victors of the Second World War.

With Korea, which had joined after the Great Cataclysm, there were six permanent member states in total. And if the United Kingdom, which had chosen neutrality on this matter, and France, which had chosen to support it, were excluded, four permanent members were standing with the opposition camp that was effectively calling for a delay.

But even the veto power held by the permanent members had clear limits now that the UN had been reorganized.

*So this is how it ends.*

The secretary-general’s declaration announcing the start of the vote seemed distant.

At that moment, the only thing ringing clearly in President Baek Hanseong’s ears was the conversation he had exchanged with Choi Minwoo three days earlier.

“UN decisions must be delayed as long as possible.”

“You mean delayed? Not stopped?”

“Yes. If we could stop them, there would be nothing more I’d ask for. But even if the United States and China helped us, that would be nearly impossible.”

“…You mean we need to buy time.”

“Even a few weeks. No, even a few days would be enough. Please do everything you can until we reach the limit of what is possible.”

“Hah. What exactly is happening right now?”

And Choi Minwoo’s answer, which had come after a long silence, had been short.

“It’s war.”

“…Mr. President. Mr. President.”

President Baek Hanseong abruptly came to himself. The chief secretary was looking at him with a face filled with equal parts concern and impatience.

“You have to cast your vote now. We’re the last ones.”

“Ah.”

After letting out a short groan that sounded almost like a sigh, President Baek Hanseong looked at the presidents filling the office.

No—the holograms.

Then, thinking of Choi Minwoo and Jin Taekyung, who were probably preparing for war somewhere by now, he cast the final vote of this miserable meeting.

* * *

Sometimes, communication was possible without facing one another or even saying very much.

The tone of a voice. Its rise and fall.

That alone could convey the meaning and significance contained in the words.

In that sense, Choi Minwoo understood everything the moment he answered the call from President Baek Hanseong.

“I did everything I could.”

The silence that followed those words was long, and the conversation remaining between the two men was empty.

After ending the short call, Choi Minwoo began to walk.

Toward a room filled with documents and monitors.

Toward a person so absorbed in something that he had not even noticed Choi’s arrival.

Then, suddenly, Choi opened his mouth.

“The UN… approved the reestablishment of the World Hunter Federation.”

The answer was short.

“Fuuuck.”
## Chapter artifact 769

# Chapter 769

Even the most clearheaded person in the world could not maintain their composure every moment of every day.

Michael Silbert realized he was shaken only after brewing three cups of coffee in a row.

*Shaken? Me?*

It was quite a shock even to him, and that shock soon turned into displeasure.

A leader must never show weakness. Not to their enemies or their allies. Not even to themselves.

To win this war at all costs, he could not reveal the slightest opening.

During a fierce battle, a person's movements began to grow sluggish from the moment they realized they had been wounded.

Michael Silbert believed he could possess everything only if he could ignore any pain, and he had lived according to that belief.

Ever since the day, long ago, when he had returned from the threshold of death.

But there were two reasons he was shaken like this today.

One was the tremor that came from nearly reaching his grand dream.

The other was…

*It’s probably because of that bastard.*

A face passed through the steam rising from the coffee cups.

The face of a young man much younger than himself, who had claimed the public’s love in an absurdly short time and ultimately become the most troublesome obstacle of all.

*Jin Taekyung.*

Along with the name lingering in his mouth came a faint pain around his throat.

Swish.

When Michael Silbert carefully lowered the turtleneck covering his neck completely, a clearly imprinted, dark-red wound came into view.

Skin warped by heat that had seeped in for only an instant.

It was the first wound he had suffered in more than a decade, and he had been tracing the mark Jin Taekyung had left behind several days earlier when—

Bzzzt.

The sound of a vibration rang from somewhere, and the fingertips stroking the wound that had yet to heal trembled.

Michael Silbert instinctively pulled up his collar to cover the injury, then looked at the name appearing on his smartphone screen.

[Emmanuel]

There were many people in the world named Emmanuel.

But only one Emmanuel could contact him directly without going through Huginn.

Click.

“Congratulations, Guild Master.”

The moment the call connected, the voice of the President of France came through. Michael Silbert laughed aloud and immediately tipped the three cups of coffee in front of him toward the floor.

Along with them, he poured out his anxiety and agitation—and the face that had faintly appeared through the hazy steam.

After everything had been spilled, the only things remaining in the empty cups were joy and triumph.

*I… won.*

The throne had been prepared. All that remained now was a magnificent coronation.

At that moment, Michael Silbert suddenly wondered what expression Jin Taekyung was wearing after hearing the news.

His lips twitched at the scene that rose vividly before his eyes.

* * *

It was strange.

Even though something that absolutely should not have happened had become reality, my heart was strangely calm.

One of the main reasons was probably that I had expected this situation well enough.

“Fuck.”

Still, I had to do what needed to be done. It wasn’t like I could shout, *Yay!*

After letting out a string of curses out of habit, I looked at Team Leader Choi, who had just opened the door and entered.

“In the end… you couldn’t stop it?”

Team Leader Choi nodded heavily.

“Our limits were clear.”

“Even though Russia helped us? Russia, of all countries?”

“Even if the United Kingdom, which remained neutral during this General Assembly, had joined us, the result would not have been very different. We’re already in a situation practically identical to wartime.”

Even someone as blind to politics as I was knew how much authority the permanent members of the Security Council possessed.

I also knew that the international situation experts on television kept talking about was ultimately just a power game between nations.

This place was no different from another Murim, anyway.

If martial artists flaunted their families and martial arts, Great Nations displayed their power through military strength, economies, production capacity, and all kinds of resources, using them to crush weaker countries beneath them.

And during this UN General Assembly, five of the greatest powers in the world—all permanent members of the Security Council—had joined forces to oppose the reestablishment of the World Hunter Federation.

Under normal circumstances, regardless of whether they liked the proposal, the many countries influenced by those nations would have followed their will like mere appendages.

That was, if things had been normal.

“More than twenty countries, including Congo, Syria, Ethiopia, and Myanmar, are on the verge of civil war. Coup factions are rising in various places under the pretext of representing public sentiment. They must have wanted to reach a decision as quickly as possible. The situations in other countries aren’t much different.”

“Damn it.”

“Fear is destroying the rule of law. This must be the situation Michael Silbert wanted.”

This was a matter of survival, apart from politics.

If several big, powerful men blocked the fire hydrant while your house was about to burn to ashes and told you to wait just a little longer, who would obediently turn around and leave?

I understood their position perfectly well.

However…

*It was an entirely different matter if that fire extinguisher turned out to be a flamethrower.*

I admitted it.

The World Hunter Federation was absolutely necessary.

During the last Great Cataclysm, when terrible flames had spread in every direction, they had played the role of excellent firefighters. They had done their best as heroes more devoted than anyone else.

But Michael Silbert was different.

What could be a greater black comedy than the person who had secretly started the fire being appointed as the new firefighter?

That was why, three days ago, I had said it in front of everyone.

We had to stop him. Within the time we had been given, we had to use every ounce of our strength to hold Michael Silbert back.

And now, the grains of sand in the hourglass we had turned over were running out.

After only three days.

“This is… isn’t this too soon?”

It wasn’t just Team Leader Choi and me in the room.

The Skeleton King muttered like a groan and crushed the documents in his hand with all his strength.

A familiar face was visible on the badly crumpled paper between his fingers—a man looking at the camera with an expression younger and more human than the one he wore now.

It was Michael Silbert.

More precisely, Michael Silbert from several decades ago.

Over the past three days, we had investigated every piece of material brought from Siegfried Wassman’s hideout, along with Michael Silbert’s past actions.

We were searching for a clue that could stop him.

But Michael Silbert was one of the most famous people in the entire world. The information that had accumulated over decades, ever since the Great Cataclysm, was simply too vast, and time was not waiting for us.

“Can’t we stop him?”

I could not answer the Skeleton King’s question.

Magic Johnson, who had been put in charge of the material from the hideout, might have discovered something by now, but the possibility was slim.

Even when he had come to us by hologram three days earlier, he had already gone over all the material more than ten times—and then gone over it again.

In the end, the only answer I could give was a guess bordering on despair.

“Yeah. Probably not.”

“……!”

“Everything we’ve found so far has only reconfirmed facts everyone already knew.”

The moment I finished speaking, a heavy silence settled over the room.

The Skeleton King stared at the mountains of documents with trembling eyes before suddenly opening his mouth.

“No. There is still one way.”

“There’s… a way?”

“It is a very simple and easy method. There is no need to take a difficult route.”

The next moment, the Skeleton King said something that I had never expected.

“Wicked human, you need only erase this body.”

“What?”

At first, I thought I had heard him wrong.

But as I stared blankly at him, the Skeleton King continued in a calm voice.

“Of course, not right away. Reveal this body’s identity in front of everyone, before the important humans watching, and then erase me. Only then will it have a definite effect.”

“……!”

“It is a simple solution, is it not? If you have been caught by a weakness so serious that you have no choice but to comply with his demands, then eliminate the weakness. Along with a suitable explanation.”

An icy chill ran down my spine. Every hair on my body stood on end.

I was facing him as usual, but the guy before me felt more unfamiliar than ever.

His deeply sunken gaze. His faint smile. Even his calm voice.

Every last one of them.

“This body is a monster. To you humans, I am practically evil itself, and I am also cunning enough to deceive the eyes of insignificant humans and approach them whenever I wish.”

The Skeleton King grinned.

“You, human. I confess now that you are not particularly devious. You are merely absurdly strong and much stupider. The other humans know that about you as well, so if you demonstrate it through your actions, they should have little trouble accepting it.”

Boom. Boom. Boom.

My heart pounded violently.

Countless thoughts tore through my mind, and voices I could not bring myself to let out circled inside my open mouth.

*This is fucking insane…*

I had never once considered such a thing, which was why it shocked me even more.

Then, as I froze for an instant, a voice pierced my ears like a needle.

“It is a possibility.”

“Team Leader Choi!”

My shout burst out instinctively, but Team Leader Choi did not flinch in the slightest.

His face rigid, he continued.

“A weakness can only be called a weakness when it is exposed and the enemy can exploit it. If you eliminate it yourself, no problem will arise.”

“What the hell are you talking about right now…”

“The public still loves you, Mr. Jin Taekyung. Although the extermination of the terrorist group brought about the appearance of The Prophet, it was done for the sake of a greater good, and you gave everything you had to save people despite the countless accusations thrown at you. In particular, the self-sacrifice you showed against Leviathan and during the Monster Wave in Munich…”

“Enough!”

My second shout finally made him close his mouth.

But Team Leader Choi’s silence did not last long.

“Then what do you intend to do?”

“……!”

“Is there another way? Is there any way to stop Michael Silbert from taking the World Hunter Federation—and the entire world—into his hands?”

I could barely breathe.

The moment I lost my voice, Team Leader Choi poured out the words he had been holding back somewhere inside him without pause.

“We could hide the Skeleton King in some distant, unknown place—or somewhere no one could find him. But if Michael Silbert revealed the truth, would people believe it?”

“But he…”

“Yes, that’s right. He has definitely saved many people. He fought alongside us in Sichuan, Busan, Japan, and Munich. The number of people who survived because of him may exceed several hundred thousand. But!”

Thud.

As he stepped forward forcefully, Team Leader Choi’s face drew close before my eyes.

A pair of eyes filled with countless tangled emotions was followed by a powerful voice.

“People don’t believe it.”

And his final words faded weakly, like a dying campfire.

“Because the Skeleton King… he’s a monster.”

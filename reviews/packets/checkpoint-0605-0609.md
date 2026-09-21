# Checkpoint Review — 605–609

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

# Chapters 605–609

## Plot

Magic Johnson arrives in Korea, learns that Cheon Taemin has survived in a coma for more than twenty years, and teleports Taemin and the others from Ares Guild to Taemin’s former mansion. He fortifies the mansion with powerful defensive, environmental, spatial, and concealment magic, then plans to consult the other Grand Mages about the hidden Area A space and Taemin’s condition. Team Leader Choi is finally reunited with his maternal grandfather, though Taemin remains unconscious.

Magic Johnson reveals that the Texas incident was not a Mutated Gate but a failed terrorist experiment involving an unpurified A-grade Magic Gem. Intelligence indicates that terrorist organizations and African rebel forces are experimenting with Gates and Magic Gems, prompting the Pentagon to request Jin Taekyung’s help.

Jin, Team Leader Choi, and Magic Johnson meet Secretary of Defense Chuck Hagel and President Donald Doramp Jr. at the Pentagon. The United States reports thirty-two terrorist attempts in one day and begins preparing a multinational operation, but UN and legal requirements may delay it for months. Doramp covertly provides a tactical map of suspected enemy headquarters, allowing Jin’s group to begin an unofficial campaign in Africa and the Middle East.

Jin infiltrates Muhammad Saladir ad-Din’s bedroom, kills his elite guards, and forces the terrorist leader to order an all-out war against a rival organization. Over the following week, Jin, Chuck Hagel, Magic Johnson, and their allies attack, capture, or secretly control terrorist and rebel leaders across the desert. Magic Johnson uses custom brainwashing Magic on some captives, while the group’s bounty rises to fifty million dollars.

## Continuity

- Cheon Taemin remains unconscious after more than twenty years and is now hidden in his former mansion inside a fortified, concealed magical environment.
- Team Leader Choi has reunited with his living maternal grandfather but still does not know how to awaken him.
- Magic Johnson believes another Grand Mage may know who created the Area A secret space and its extraordinary magic.
- There are only three Grand Mages in the world.
- The Texas incident was an attempted terrorist use of an unpurified A-grade Magic Gem; the B-rank perpetrator exploded without causing significant casualties.
- Terrorist groups and African rebel forces are experimenting with Gates and Magic Gems, risking uncontrollable monster waves.
- Donald Doramp Jr. is President of the United States; Chuck Hagel is Secretary of Defense and head of the Pentagon’s E-Ring.
- Cheon Taemin was known in the United States as Sky and was previously granted access to the E-Ring equivalent to that of the U.S. President.
- A multinational operation is being prepared against terrorist and rebel forces, but it requires UN Security Council approval and extensive legal and diplomatic preparation.
- Jin Taekyung, Team Leader Choi, Magic Johnson, Chuck Hagel, and their allies are conducting a covert campaign before the official operation begins.
- Muhammad Saladir ad-Din has been forced to command an all-out war against a rival armed terrorist organization.
- Kasim and bodyguards Omari, Sadat, and Nasser are dead; Omar al-Hussein, leader of a Sunni faction, has been captured.
- The covert campaign has lasted one week, and the team’s bounty has reached fifty million dollars.
- Jin’s undisclosed plan for himself and his allies remains unresolved.

## Translation Decisions

- Use **Mutated Gate**, **Grand Mage**, **Magic Gems**, **Gates**, **Area A**, **Middle Dantian**, **Qi Sense**, and **Force** consistently.
- Use **Team Leader Choi**, **Magic Johnson**, **Chuck Hagel**, **Uncle Chuck**, **Sky**, and **Mr. Sky**.
- Use **Building Five** and retain **E-Ring** as the Pentagon designations.
- Use **President Doramp** for Donald Doramp Jr. and **UN Security Council** for the international approval body.
- Render **효자손** as **back scratcher**, preserving the literal Korean wordplay in a footnote.
- Use **Muhammad Saladir ad-Din** for the terrorist leader and **Sunni** for **수니파**.
- Preserve Jin’s crude taunts and profanity, but use a cold, condemning tone when he denounces Muhammad.

## Durable state

{
  "active_continuity": [
    "Donald Doramp Jr. is President of the United States, a wealthy tycoon, and the third father-and-son presidential pair in U.S. history.",
    "The United States is preparing a multinational operation against terrorist groups and rebel forces, subject to UN Security Council approval and international-law constraints.",
    "Jin Taekyung, Team Leader Choi, Magic Johnson, Chuck Hagel, and their allies are conducting a covert campaign against terrorist and rebel forces in the desert before the official operation.",
    "Terrorist groups and African rebel forces are experimenting with Gates and Magic Gems, creating the risk of uncontrollable monster waves.",
    "Muhammad Saladir ad-Din is a terrorist leader forced to command an all-out war against a rival armed terrorist organization.",
    "Chuck Hagel is a large American operative allied with Jin Taekyung who uses illusion Magic and fights in the covert campaign.",
    "Jin Taekyung's team has captured or controlled multiple terrorist and rebel leaders, including Omar al-Hussein, leader of a Sunni faction.",
    "The covert campaign has lasted one week, and the team's bounty has reached fifty million dollars."
  ],
  "continuity_sources": [
    609
  ],
  "open_questions": [
    "Will the UN Security Council approve the planned multinational operation, and when will it begin?",
    "What results will follow from Muhammad Saladir ad-Din's forced order for the rival terrorist organizations to destroy each other?",
    "What are the terrorist groups and rebel forces seeking from their Gate and Magic Gem experiments?",
    "How will the week-long covert campaign affect the wider terrorist and rebel forces?"
  ],
  "safe_through": 609,
  "temporary_decisions": [
    "Treat the President's supposedly accidental tactical-map handoff as deliberate covert cooperation.",
    "Use Muhammad Saladir ad-Din as the full English rendering of 무함마드 살라디르 앗 딘.",
    "Render 효자손 as “back scratcher” while preserving the literal-wordplay footnote.",
    "Use “Sunni” for 수니파 and reserve “Sooni” for the separate name or joke."
  ],
  "version": 1
}

## Reading copies

## Chapter artifact 605

# Chapter 605

“Jacob. How’s the situation over there? You’re not hurt, are you?”

On the holographic TV, an East Asian female anchor with heavily made-up eyes was asking the question. The sturdy Black reporter stationed at the scene winked and answered.

“Thanks to Jenny worrying about me, I’m safe and sound. Everyone else is fine, too.”

“It looks unbelievably peaceful for the site of a Mutated Gate.”

“Of course it does. No one was hurt, and the situation was wrapped up in an instant. Besides, this is Texas. Everyone here is tough, men and women alike.”

“Haha. That’s a relief. But where is the hero who saved everyone in that dangerous situation?”

“Jenny, I’m afraid I owe you and the viewers an apology. The hero who was supposed to grace today’s broadcast, Magic Johnson, has already left. I tried my best, but I couldn’t hold him back.”

“Oh, dear.”

“He refused the interview and disappeared, saying he had something urgent to take care of. He looked so desperate that I thought he was going to meet a secret lover.”

“I see. Anyway, Jacob, about the exact cause of this Mutated Gate…”

Hmm. A secret lover.

Leaning against the sofa and watching the holographic TV, I absentmindedly began to hum.

“When Dad goes to work, Ppoppo. Magic Johnson comes to Korea, Ppoppo.”[^1]

Whoosh! Crash!

I ducked at the sound of something slicing through the air, and a crystal glass narrowly grazed the back of my neck before smashing into the holographic TV.

Shards flew in every direction, and water pooled across the floor. Team Leader Choi, whose eyes met mine, calmly opened his mouth.

“Oh, you dodged that.”

“…”

“I’m telling you this so you don’t misunderstand. It was intentional.”

“…You’re not even going to claim it was an accident?”

“Because it wasn’t an accident. Still, it’s a real shame. If that had been just a little faster, it would’ve smashed Mr. Jin Taekyung’s skull…”

“Hey, you don’t call a person’s head a ‘skull.’ A skull?”

“You keep flapping that obnoxious trap of yours, so yes, I’m calling it a skull. Frankly, even the word ‘skull’ is wasted on a blockhead like you.”

“Whoa, what? ‘Skull’? ‘Trap’?”

“From now on, don’t even think about falling asleep in front of me. If you sleep with your mouth open, I’ll pour cyanide down it.”

“…”

Was that punchline insane or what?

He must have been furious. His words came out as if he were spitting them through clenched teeth, and the venom seeping through them left me momentarily speechless.

I briefly considered taking out the Myriad-Poison Ring, then calmly waved a hand.

“Team Leader Choi. Calm down, calm down. I was completely wrong.”

“Do I look like I can calm down right now?”

“I couldn’t help it in that situation. You saw the news. They said he was busy dealing with a Mutated Gate. What else could I do? I had to get him here first.”

“Even so, do you get to put my lips on the line without asking?”

“But I couldn’t put my own lips on the line, could I?”

“……”

Whoosh! Crash!

Whoa. That one had genuinely been dangerous.

After narrowly dodging the attack once again, I hurriedly shouted.

“Stop! Team Leader! Stop!”

Team Leader Choi picked up a third crystal glass and answered.

“Shut your mouth and stick your head out. Right there.”

“I didn’t kiss him! I didn’t do it in the end!”

“You almost did!”

Team Leader Choi was just about to swing his arm with a roar that could rival a lion’s roar when—

Bang.

The door opened without a knock.

In front of it stood the Skeleton King, brimming with anticipation, and Magic Johnson, looking thoroughly dejected.

“The job’s done. Are we going to a club now?”

「Choi, I’m a romantic too.」

Team Leader Choi stared silently at the club-obsessed parrot and the pure-hearted Grand Mage. Then, with a sigh, he lowered his hand.

* * *

Magic Johnson was not merely an outstanding War Mage, but first and foremost a Grand Mage capable of wielding most forms of magic.

After receiving our call and coming straight to Korea, he heard everything from us.

“Mr. Johnson. There’s something we need to move, actually…”

“Whatever the reason, I want my Ppoppo first. You’re ready, Choi?”

“I’m not ready, I won’t be ready, and I never will be.”

“Then that’s a problem. I don’t know what kind of object you’re trying to move in such strict secrecy, but…”

“Um, it isn’t an object. It’s a person, to be exact.”

“What do you mean, Jin? A person? Are you helping someone escape?”

“I’m not sure whether ‘escape’ is the right word, but it’s similar.”

“Who is it? A heinous criminal? Or a secret lover?”

“He’s my maternal grandfather.”

“Oh, shit. Sorry, Choi. I didn’t mean to—wait. Who did you just say?”

Even after hearing the entire story, Magic Johnson remained silent for a long time. He didn’t speak until he had personally confirmed Cheon Taemin’s face.

“Damn it. What the hell happened here?”

“As you can see, it’s a dogshit situation.”

“There was a reason you couldn’t explain everything over the phone. All right, let’s take care of the urgent matter first. Choi, where are we moving him from this prison-like place?”

After that, everything proceeded at breakneck speed.

Magic Johnson cast Teleport using the coordinates Team Leader Choi had given him, and all of us—no, one person among us, locked in a deep sleep he could not easily wake from—was able to return to the mansion where he had once lived.

To the home he had missed.

It was a return more than twenty long years in the making.

「Space distortion and barriers. Defensive magic is a given, and I’ve even set up humidity and temperature controls. And…」

Like a traveler wandering across a beat, Magic Johnson rattled off every kind of magic without pause before finishing with a breathless sentence.

「So, you can assume that I’ve taken every measure I’m currently capable of taking. Though additional work is still needed.」

The Skeleton King, sulking because he couldn’t go to a club, muttered.

“I understand that it’s impressive, but how impressive are we talking?”

「It means that this place will remain intact unless a Grand Mage on my level—or two or three S-rank Hunters—deliberately attacks it with the intention of smashing it to pieces.」

“That’s some serious performance.”

I agreed with the Skeleton King. Magic Johnson had quite literally taken every measure he could.

He had even made it impossible for most S-rank Hunters to detect Cheon Taemin’s existence or location.

*The combat and magic disciplines operate on different tracks.*

Just as martial arts training had no end, magic was the same.

If I hadn’t opened my Middle Dantian, I would never have been able to find Cheon Taemin so easily.

「By the way, does anyone here know who created that secret space? The same goes for this place called Area A. The level of the magic installed here is definitely not beneath me.」

“This body does not know, human.”

I promptly patted the Skeleton King’s shoulder with dignity.

“He asked whether anyone knew. He wasn’t asking a monster.”

“You’re a real fucking bastard.”

Hmm. His vocabulary was improving every day.

Smack!

After giving him a blow to the back of the head as a reward for his improved vocabulary, I turned to Magic Johnson.

“I’m curious about that, too. Do you have anyone in mind?”

「Hmm, let me think. When you get right down to it, the only people who could have done it are Grand Mages like me. Especially if the magic really is at this level.」

“Then, perhaps…”

「Are you asking whether it was those two?」

I had fallen silent with a doubtful expression, and Magic Johnson shook his head with an unusually serious look.

「Probably not. But it isn’t as if I have no one in mind.」

“Someone you have in mind?”

「Hmm.」

Magic Johnson let out a low hum and seemed to sink into thought before continuing.

「I’ll say no more about this for now. It’s too early to be certain. But just in case, I should visit the other Grand Mages. It’s been a long time since I’ve seen them, anyway.」

“Then I’d appreciate that.”

That was welcome news. Magic Johnson was a Grand Mage with exceptional insight, and he intended to determine the truth for himself.

*There are currently only three Grand Mages in the entire world.*

If a Grand Mage had accepted a request while fully aware of Lee Jungryong’s intentions…

This was not something we could simply let go.

Anyone who had helped imprison a hero who saved humanity from disaster as though he were a criminal would have to answer for that crime.

Even if it was only for one person.

“Team Leader Choi.”

Despite my call, Team Leader Choi remained frozen in place.

Inside the oval-shaped hibernation device made of cold metal, he gazed endlessly at his maternal grandfather, who had fallen into a deep sleep. Then he suddenly spoke.

“I’ve waited for so long… but you still haven’t woken up.”

A clumsy attempt at consolation would have been worse than saying nothing. Knowing that, none of us could bring ourselves to speak easily.

The immortal hero, Cheon Taemin, still hadn’t regained consciousness.

*For more than twenty years.*

We knew neither the cause nor the reason. Unfortunately, everything Team Leader Choi had heard from Song Cheonwoo had been true.

Lee Jungryong and Song Cheonwoo, those two ambitious men, had once tried every possible way to wake him. But in the end, they had achieved nothing.

In this frustrating situation, there was only one thing we could say right now.

“There must be a way.”

「Jin is right. Just as there can be no result without a process, there can be no illness without a reason.」

“Keep your chin up. He definitely isn’t dead yet. Even if he dies, this body will find a way to revive him as a Death Knight…”

The Skeleton King stopped when killing intent poured from both Magic Johnson and me. He stammered out an excuse.

“I-I was trying to comfort him.”

“That’s comfort? You fucking asshole?”

「Monster motherfucker…」

I was berating the Skeleton King in a voice no louder than a mosquito’s buzz so Team Leader Choi wouldn’t overhear when Choi spoke with a faint smile.

“It’s all right. We’ll find a way somehow. It’s a relief that he’s alive.”

Just because someone was smiling didn’t mean they were happy.

I could feel the emotion coming from Team Leader Choi. So could Magic Johnson. Even the Skeleton King, who had not a single finger bone’s worth of tact, could feel it.

And as though we had made a promise, all three of us fell silent.

Team Leader Choi’s voice, sunk deep with emotion, pierced my ears.

“But… at least today, I’d like to rest. Thank you all for your hard work. I truly appreciate it.”

He looked at us one by one, then bowed his head sincerely.

I understood the meaning of that gesture and was the first to walk toward the entrance.

This was a reunion that had come after more than twenty years. For a grandfather and grandson who could not even exchange a single greeting right now, it was time for us to leave them alone.

* * *

One of the most important things to Koreans was rice.

“Have you eaten?”

“Let’s get a meal together sometime when you have time.”

“Are you a rice-dick?”[^2]

The last one was a little strange, but even curses involved rice. That was Korean culture for you.

In other words, when a Korean finished a job, they had to share a meal. And the best kind of meal was rice served in broth.

「Gugbab? What is this?」

Magic Johnson examined Mom’s homemade blood sausage gukbap[^3] with a suspicious expression before putting down his spoon.

「Hey, Jin. Do you have any toast?」

“Come on, just try it.”

「No, it’s fine. I’m not hungry.」

Grrrrr.

「…You really don’t have any toast?」

“Even if there were some, there isn’t. If you’re that reluctant, just try the broth. The broth alone.”

「Damn it. This is Korean soup? Why does it look so strange?」

Grumbling, Magic Johnson picked up his spoon and awkwardly scooped up some broth.

Then he tasted it.

And that meant the game was over.

「Kheeeee. Fuck yeah.」

After repeatedly shouting “Fuck yeah” and devouring two bowls of blood sausage gukbap, Magic Johnson smiled in satisfaction.

「There were so many things going wrong today that I was busy all day. I feel like I can finally breathe.」

“I saw the news earlier, actually. You subdued the Mutated Gate and came straight here without even doing an interview.”

「The Mutated Gate? Did you not watch the news to the end?」

*I couldn’t. Team Leader Choi smashed the TV with a crystal glass.*

I shrugged and asked back.

“Why?”

「Because if you had, you wouldn’t have said that.」

Magic Johnson picked up a toothpick and continued.

「To be precise, it wasn’t a Mutated Gate.」

“What?”

What the hell was he talking about now?

[^1]: “Ppoppo” is Korean baby-talk for a kiss. The line also alludes to *Ppoppo Ppoppo*, a Korean children’s TV program.

[^2]: “Jjotbap” is a vulgar Korean word for a weakling, literally combining “dick” with “rice.”

[^3]: *Gukbap* is a Korean dish of rice served in hot soup. Here, the dish is made with *sundae*, a Korean blood sausage.
## Chapter artifact 606

# Chapter 606

*It wasn’t a Mutated Gate? What the hell was that supposed to mean?*

My confusion lasted only a moment. The next second, I heard the single word Magic Johnson had tossed out and my eyes widened.

“Terrorism?”

“Yeah, terrorism. The culprit was an Arab man who was caught trying to get into the Gate with a forged Hunter license. The problem was that he was a B-rank Hunter affiliated with a terrorist group in the Middle East—and he was carrying an A-grade Magic Gem. Naturally, it hadn’t undergone purification.”

“That sounds a little…”

“It must be a pretty familiar situation to you, Jin. Am I wrong?”

Instead of answering, I clamped my mouth shut. Memories from not long ago flashed through my mind.

Go Jun. Song Cheonwoo. And two monster waves.

Something that should never happen again had kept happening.

“He was after a monster wave.”

“Probably. No, I’m sure of it.”

*Damn it.*

I cursed inwardly and urgently asked, “What about the casualties? How bad was it? Did the news deliberately hide the damage because—”

I couldn’t bring myself to finish the sentence, and my voice trailed off.

The incidents that had taken place recently had been one disaster after another.

It might not have been comparable to Go Jun, but if a B-rank Hunter from a terrorist group had absorbed an unpurified A-grade Magic Gem, it would have caused considerable damage all by itself.

Seeing my expression, Magic Johnson answered in a calm voice.

“Whoa, calm down, Jin. Everything reported in the news was true. By sheer luck, there wasn’t any significant damage.”

“Are you sure?”

“I have no reason to lie to you. Do I?”

“But how?”

“Everyone around the world has already been on high alert because of this incident. Identity checks and Magic Gem inspections have become several times stricter, and the terrorist was caught during that process. As a last resort, he tried to absorb the Magic Gem. What do you think happened?”

Magic Johnson continued, taking a sip of the instant coffee in his paper cup.

“It’s simple. He couldn’t withstand the power contained in the Magic Gem. By the way, this coffee is pretty good.”

“Forget the coffee. If that happened, he should have mutated the way Go Jun did.”

Mana and magical power were forces that could never mix, like oil and water.

The proof was Go Jun himself—a certified S-rank Hunter who had learned the modern mana cultivation method, yet had ultimately been unable to absorb magical power completely.

The real problem was the temporary surge in power it caused.

And the mutation that waited afterward.

*But the result was simple?*

The fact that there had been no significant casualties felt even stranger.

Then Magic Johnson gave me an answer I never could have expected.

“No. He exploded.”

“What?”

“Exactly what I said. He blew apart into pieces. Boom!”

Bang, bang!

Magic Johnson tapped the earthenware pot with his spoon and shrugged.

“And that was the end of everything. All I did at the scene was protect people from the blast’s aftermath.”

“…”

“In a way, yes. You could definitely call it a suicide attack. But that was all it was.”

At those words, I realized something and muttered inwardly.

*It wasn’t that it was like what happened with Go Jun. It was that what happened with Go Jun had only been possible because it was Go Jun.*

I had been thinking about it wrong from the start.

In the end, it was a matter of the vessel.

Not in terms of a person’s character or breadth of mind, but in terms of how much power they could contain without letting it overflow.

And in that sense, the dead Go Jun had possessed a vessel large enough.

He had been capable not only of absorbing some magical power, but of maintaining it for a short while.

*But even Go Jun eventually mutated.*

Go Jun’s vessel had lost its balance after he absorbed two S-grade Magic Gems at once, and he had finally undergone a mutation.

Even if I hadn’t intervened personally, there was a very good chance he would have died after holding out for only a little longer.

*So ordinary Hunters were out of the question.*

The terrorist who had become the star of today’s news had been a B-rank Hunter, yet he had been unable to withstand the power and exploded on the spot.

That meant he hadn’t been able to control even a little of the magical power contained in the Magic Gem.

“Hey, Jin. You look like you’re starting to get it now.”

I let out a hollow laugh as I looked at Magic Johnson, who was grinning.

“That’s a huge relief.”

“It is. From now on, only a complete idiot could try something like this again.”

Magic Johnson had accurately identified the important trend.

It was fortunate that the terrorist attack had caused no damage, but the greater relief was that it would deter similar incidents in the future.

“The terrorist group must have realized it, too. To put it coldly, this was a terrible trade from their perspective.”

Trained Hunters were valuable assets, and Magic Gems were energy sources worth an enormous amount of money.

I had no idea how the terrorist group had smuggled an unpurified A-grade Magic Gem out, but they had failed spectacularly today.

They had thrown away a valuable asset and a Magic Gem easily worth billions.

“The terrorists will change their strategy, too. Just like before, they’ll probably target powerless civilians with that damn magic wand of Allah. But it’s still too early to let our guard down.”

Magic Johnson let out a quiet sigh before continuing.

“Actually, terrorist organizations have been making some alarming moves lately. Apparently, experiments involving Gates and Magic Gems are being carried out particularly in Africa and the Middle East. The information came from the Pentagon, so it’s reliable.”

The Skeleton King, who had spent the entire conversation fiddling with his smartphone without participating, perked up his ears.

“The Pentagon? Are we going there right now? Is much rub-rub possible?”

“Just in case you’re wondering, it’s not a club.”

“Damn it. I thought I was finally going to meet some hot girls.”

*Don’t even dream about it, you bastard…*

The Pentagon was the headquarters of the United States Department of Defense.

If the Skeleton King’s identity were revealed, the researchers at the Pentagon would hold a party all night.

Naturally, they would try all kinds of rub-rub with every experimental tool imaginable in a laboratory protected by ironclad security.

“Hmm. Everyone would certainly be happy if we took that fellow to the Pentagon.”

“That wouldn’t be very good for you or me.”

“That’s true, too. We’d probably have to stand trial for violating international law. Though if a terrorist group caused an incident during the trial, the whole thing might fizzle out.”

Living in this world was difficult.

I knew that because the moment one problem was solved, another one popped up.

*A terrorist group.*

Once the series of incidents caused by Go Jun became known to the world, every country had been thrown into shock and heightened alertness.

But terrorist groups had gained another weapon.

If the information Magic Johnson had obtained from the Pentagon was true, they would find a way no matter what it took.

“…Of all times.”

A question mark appeared over Magic Johnson’s face at my mutter.

“Of all times? What do you mean?”

“Hmm.”

I hesitated, wondering whether I should tell him, then shook my head.

“It’s nothing. You don’t have to worry about it.”

“It sounds like something, and it’s bothering me a lot.”

“It’s just… there’s something I’ve been preparing. But after hearing what you said, I’m hesitating for now.”

“Something you’ve been preparing?”

I nodded slightly.

I hadn’t told anyone about it yet, but it was one of the decisions I had made after returning to the modern era this time.

For my sake.

And for everyone else’s.

After a long period of hesitation, I had made a decision and had been preparing for it…

*But this changes things.*

After the Great Cataclysm, humanity had regained peace, but the entire world was not peaceful.

The newly emerged mana and the existence of Awakened people.

The powerful survivors had rebuilt the world according to their own rules, and conflicts everyone had thought were over still continued to this day.

*No. Some people would even say they’ve only gotten worse.*

Magic Gems were resources with greater value and usefulness than oil, while Gates were mines that constantly spat out diamonds in the form of Magic Gems.

The conflicts surrounding them could only continue endlessly.

Whether in the name of entrepreneurs, Guilds, or rebels.

And the terrorist groups in the Middle East were even more dangerous.

They considered awakening a blessing from God and held it up as proof of God’s existence.

Someone might ask what the hell that had to do with anything when even atheists could become Awakened, but it was already a mistake to look for logic in people like that.

*Warriors chosen by God! Advance!*

*God wills it!*

I had no idea which god or doctrine had encouraged them to do something so idiotic.

But just as singers sang and blacksmiths worked iron, idiots were bound to keep doing idiotic things.

The idiots continued fighting in every corner of the world, dying or ending up crippled.

And that was still happening at this very moment.

*Bastards.*

The Skeleton King was much better by comparison. He might have started out as a monster, but by this point he had shown as much sacrifice and dedication as any Hunter.

*Good lad.*

At the warmth in my gaze, the Skeleton King glared at me ferociously.

“You just cursed this body in your thoughts.”

“…What the hell? That’s absurd.”

“Tell me honestly. This body will forgive you.”

“Johnson. Can’t we just take this bastard to the Pentagon?”

Magic Johnson grinned and answered.

“Should we?”

“You hear that? You’re finished now, you experimental-subject bastard.”

“Now that it’s come to this, going right away wouldn’t be bad.”

“Tell them to prepare a cauldron. We’ll make some bone broth out of this bastard.”

“I don’t know about a cauldron, but the laboratory will be ready whenever we are.”

For some reason, we were getting along perfectly today.

Magic Johnson casually played along with my remark, then took a staff out of his robes and continued.

“Well, now that we’ve eaten, shall we get going?”

“That doesn’t sound bad… Wait a second.”

I had agreed automatically, but then I felt the mana circulating through Magic Johnson’s staff, and my expression turned uneasy.

“Uh, there’s no need to go that far.”

“There’s a Korean traditional proverb that goes something like this, isn’t there? Once a gay draws his magic wand, he has to pierce even a radish.”

“…?”

Somehow, that had been twisted into something strange and impressive.

Confused by the traditional proverb I was hearing for the first time in my life, I swallowed hard.

“Wait. Seriously?”

“Yeah. Seriously.”

“You’re not joking?”

“Two days ago, the Pentagon sent an official request. Jin, they want to receive your advice and help. Preferably as soon as possible.”

“What?”

I blinked, then let out a hollow laugh.

“Oh, I get it now. This is an American joke.”

Magic Johnson stared at me with the profound gaze of a gay man.

“How did you know? I haven’t shown you that memory.”

*What the hell is he talking about? Fuck.*

I stood there blankly for a moment before hurriedly waving my hands.

“…No, I got the pronunciation mixed up. Joke. Joke. A gag.”

“I know. That was a joke, too.”

Magic Johnson grinned, showing his white teeth, then added,

“But the part about the Pentagon wasn’t a joke.”

“…”

“Let’s go. It looks like someone else is already ready. Isn’t that right?”

I turned my head in the direction of Magic Johnson’s gaze.

Along with a familiar presence, someone entered my field of vision.

Team Leader Choi answered in a subdued voice.

“Of course, Mr. Johnson.”
## Chapter artifact 607

# Chapter 607

The Pentagon.

This massive building, shaped like a giant pentagon, was practically impregnable.

More than a thousand guards, every one of them a high-ranking Hunter. The immense flows of mana surrounding the inside and outside of the building alone were enough to convey the Pentagon’s stature.

“Impressive, isn’t it?”

Magic Johnson had just finished the authentication process. Seeing Team Leader Choi and me looking around with our eyes wide, he flashed us a knowing grin.

“Since it was first built during World War II, the Pentagon has only been attacked twice. The 9/11 terrorist attacks and the Great Cataclysm. You both know how those turned out.”

Team Leader Choi nodded.

“Even the Demon King Asmodeus and his monster army’s all-out assault couldn’t bring it down.”

“That’s right. It was the second fiercest battle of my life. The first was obviously the Day of Victory. And both times, one person helped me narrowly escape death.”

Any person on Earth, not just an American, knew that fact.

During the Great Cataclysm and afterward, only one person had ever been able to stop the demon who had descended upon this world—the Demon King Asmodeus.

“Cheon Taemin. If your maternal grandfather—the man Americans called Sky—hadn’t been there, neither I nor this Pentagon would exist today.”

Magic Johnson gazed at Team Leader Choi with distant eyes, as if remembering something, when a voice suddenly rang out.

“I see you’re thinking the same thing as me, Johnson.”

The owner of that voice was neither Team Leader Choi nor me. Naturally, it wasn’t the Skeleton King hiding inside my Inventory, either.

Clomp. Clomp.

Heavy footsteps approached.

The old white man wore wrinkled jeans and a shirt, and his white hair was thoroughly tangled and disheveled. One side of his elderly face was severely distorted.

He strode toward us without hesitation and abruptly held out both hands.

“I don’t know which of you two I should shake hands with first, so I’ll do both at once. I’m Chuck Hagel. You can just call me Chuck.”

His first greeting didn’t merely carry the air of a tough Texan. It overflowed with it.

For some reason, Chuck Hagel’s face looked familiar. I stared at him as I took his hand.

“I’m Jin Taekyung. But, by any chance…”

“You’re wondering if I’m that Chuck Hagel? I am. I may not be as famous as you, but I used to cut down my fair share of monsters back in the day.”

“Oh. Ooooh.”

I’d suspected as much just from looking at him, but the old man before me really was a previous-generation S-rank Hunter known as Uncle Chuck.

I had never imagined I would meet one of the war heroes from the Great Cataclysm whom I had admired as a child. With a cry of delight, I vigorously shook his hand up and down.

“I’m a fan. A real fan. I even collected your Hunter cards when I was in elementary school.”

“Hunter cards? They sold those in South Korea?”

“They probably sold them in North Korea, too. I bought them religiously whenever I got my allowance.”

“Huh. So there was another stupid little brat here who gave me a fortune in royalties. Of course, I spent all the royalties I made back then on alimony from five divorces.”

Chuck Hagel smiled contentedly, instantly destroying one of my childhood memories.

“If you still have any of my cards, bring them to me sometime. I’ll even sign them if you want.”

“Ah, I traded all of them.”

“What?”

“After collecting ten, I traded them for a Cheon Taemin card a friend had. Honestly, Uncle Chuck cards weren’t all that rare.”

“…”

All traces of laughter vanished from Chuck Hagel’s face. He sighed.

“Damn it. And it wasn’t just anyone’s card. It was Mr. Sky’s. I can’t even say anything about that.”

“There’s no comparison in rarity or value. My friend originally wanted twenty cards, but I haggled him down and down until…”

“…I understand. I understand, so stop now.”

Chuck Hagel shook his head repeatedly, then shook hands with Team Leader Choi.

“You look exactly like your maternal grandfather. Nice to meet you, Choi.”

“Nice to meet you, Mr. Hagel.”

“I told you to call me Chuck. If you were one of those other idiots with nothing but shit in their heads, maybe not. But you and the traitor beside you have earned the right.”

*Look at him calling me a traitor just because I sold some cards.*

While I grumbled inwardly, Team Leader Choi answered in a calm voice.

“Please understand, Mr. Hagel. I don’t feel comfortable addressing the person in charge of the Pentagon and the Secretary of Defense of the United States that way.”

“Hm. Is that so? Come to think of it, I suppose you do have to worry about what people think. You’re in charge of two massive Guilds now, after all.”

I blinked as I listened to them.

“The person in charge of the Pentagon? The Secretary of Defense?”

“Hm? You didn’t know?”

“No, I didn’t. Obviously.”

“Really? Everyone else seemed to know. I assumed Johnson had at least told you.”

At the Secretary of Defense’s words, the Grand Mage—widely expected to be elected the next Secretary of Gukbap[^1]—scratched his chin.

“I assumed you knew, too. Jin. You really didn’t know?”

At this point, I felt like I had somehow become an idiot. I replied with some reluctance.

“I really didn’t know. Were you appointed a few days ago? Ah. That must be why I didn’t know.”

Chuck Hagel gave me a short, blunt answer.

“This is my eighth year.”

“…Oh.”

“Well, it’s not as if you particularly need to know. Compared to what we’re about to discuss, it isn’t especially important. Now, everyone, follow me.”

Chuck Hagel naturally pulled a cigar from the breast pocket of his dress uniform and put it between his lips. He took the lead, and we followed behind him.

Every time Chuck Hagel puffed on his cigar, acrid smoke billowed up to the ceiling, setting off an alarm as red lights flashed.

Wee-oo! Wee-oo!

> Fire hazard! Fire hazard!

Bang!

Without a moment’s hesitation, Chuck Hagel smashed the warning light and muttered,

“Fucking siren.”

He had gone beyond being a tough guy or a petty-minded bastard. He was simply insane.

The Skeleton King, who had safely passed through the security checkpoint while hiding in my Inventory, whispered,

“Is he even human? Not a monster?”

I had plenty of doubts myself, but the man matched the description printed on the Hunter cards I had collected as a child.

He was from Texas and had dreamed of becoming a cowboy. There were even unbelievable stories about him taming a minotaur with his bare fists and riding it around, among other things.

Clomp. Clomp.

No one was brave enough to stand in Chuck Hagel’s way as he marched forward without hesitation.

Researchers, Hunters, and employees who appeared to belong to the Pentagon split to either side as if facing a disaster. Moses, who had a cigar in his mouth instead of a staff, crossed between them while spewing smoke like a chimney.

Of course, he didn’t forget to talk trash along the way.

“When is this damn hallway going to get wider? Every time I see it, I want to smash it to pieces.”

“Hey, Smith. Put that electronic cigarette away while I’m asking nicely. If you waft that shitty strawberry scent in front of me one more time, I’ll put you on the list of people who died in the line of duty. Cigars are fine, though.”

“Gordon. A warning light was smashed in Section Three. Go fix it. Who broke it? Listen carefully. Your fucking direct superior.”

No one could stop Chuck Hagel as he rampaged around like an enraged bull.

During the roughly five-minute walk, poor Smith was forced to change his e-cigarette liquid, innocent Gordon ran off with his feet on fire to repair the warning light, and seven more warning lights were smashed after they warned of the fire hazard caused by the clouds of cigar smoke.

Gordon would probably have to repair those, too.

“…”

This guy was seriously out of his mind.

I was wondering who had come up with the insane idea of putting that man in the position of Secretary of Defense when Magic Johnson leaned toward me and whispered,

“Hey, guys. Chuck’s touchy because of the terrorist problem these days. He’s a good guy at heart, so try to understand him.”

The moment he finished speaking, Chuck Hagel slammed his fist into the wall.

“This goddamn hallway! Hallway! Hallway! Hallway! Didn’t I tell you to make the hallway wider?”

Bang! Bang! Kraaang!

Team Leader Choi stared blankly at the hallway as it widened, then asked with complete sincerity,

“Is he really a good person?”

“…Probably. Even if he looks like that, his abilities and drive as Secretary of Defense are second to none.”

Of course they were. Anyone who got even slightly on Chuck Hagel’s nerves would have their life ended.

Along with Magic Johnson’s suddenly much less confident answer, Chuck Hagel passed through a mana-recognition device and pointed toward a firmly closed door.

“We’re here already. Now, everyone. This is Building Five.”

“Building Five?”

“It’s called the E-Ring. And, for what it’s worth, as far as I know, this is the first time a foreigner has entered this place in twenty-five years.”

Chuck Hagel looked at Team Leader Choi and added with a grin,

“There was only one outsider on Earth who could freely come and go here. Mr. Sky. He was treated the same way as the President of the United States.”

Even setting aside everything else, Cheon Taemin’s status was proven by the fact that Chuck Hagel—of all people—referred to him as “Mister Sky” every single time.

“And now his maternal grandson and a young hero have taken up the baton. Both of you… welcome to Building Five.”

The instant Chuck Hagel finished speaking, brilliant light poured out from the entire surface of the door.

Whoosh!

No. This wasn’t light. It was magic.

I accepted the flow of mana sweeping over my entire body instead of resisting it.

Along with the dazzling light filling my vision, the space around us warped.

*This is…*

The moment I realized that this familiar sensation was Teleport, I blinked and found myself in a completely unfamiliar new space.

As my vision rapidly returned, I saw people seated around a pentagonal table.

“Then the forces being deployed to the Middle East front will be… Oh. It seems our guests have finally arrived.”

Beep.

With a mechanical sound, the hologram illuminating the dark conference room vanished. A neat-looking middle-aged man seated at the head of the table stopped speaking and rose from his seat.

His face was more than familiar.

He was a man whose position kept him constantly exposed in every form of media. He looked older than he had on television and radiated even more charisma than he had in the newspapers.

“You’re later than I expected, Secretary Hagel. I hope you haven’t smashed another innocent warning device.”

At the middle-aged man’s amused remark, Chuck Hagel snapped off the glowing end of his cigar with his fingers and answered,

“They can deduct it from my salary.”

“The Secretary of the Treasury asked me to tell you that, as it happens, your entire salary for this month has already gone toward repairing the Pentagon damage you caused.”

“Damn it. Again? At this rate, I’ll be too afraid of alimony to get divorced.”

Chuck Hagel let out a sighing mutter, then turned toward us.

“I suppose introductions aren’t necessary?”

At least this time, they weren’t.

Team Leader Choi knew who the middle-aged man was. So did I. Even the Skeleton King knew.

“Wicked human. Could that old human perhaps be…”

That was right.

I gave a small nod. As the middle-aged man approached with measured steps, I murmured his name in my head.

*Donald Doramp Jr.*

His title was more famous than his name.

He was the President of the United States.

[^1]: *Gukbap* is rice served in hot soup. Jin is deliberately replacing *bang* (“defense”) in *gukbang-bu-jang-gwan*, “Secretary of National Defense,” with *bap*, creating the nonsensical title “Secretary of Gukbap.”
## Chapter artifact 608

# Chapter 608

I stared at the middle-aged man in front of me.

Donald Doramp Jr.

A tycoon with a business empire and a fortune worth trillions of won, he had followed his father, a former U.S. president, to make history as the third father-and-son presidential pair in United States history.

With his neat appearance, almost like an English gentleman, he looked twenty years younger than his actual age, and his smile toward us held genuine warmth.

“Welcome, both of you.”

Unlike his father, President Doramp wore his hair neatly combed back as we shook his hand.

I never thought I would meet the President of the United States in person after seeing him only on television and in online articles. Even seeing him in person, I still couldn't help but marvel.

“Haha, there’s no need to look at me like that. If anything, I’m the one who finds this amazing. I’m finally meeting the two of you after hearing so much about you.”

Team Leader Choi answered in fluent English.

“Thank you for welcoming us, Mr. President.”

“I know that a joint national funeral was held in South Korea. I mourn the victims whose lives were tragically taken by such injustice, and I pray that Mr. Kim, the former Guild Master of the Peace Guild, may rest in peace.”

President Doramp was a gentleman not only in appearance, but in his manner as well.

Even though he had already done the proper thing by sending the U.S. ambassador to South Korea and the Secretary of State to attend the joint national funeral, the fact that he had not forgotten to offer his condolences personally proved it.

“Come to think of it, you already know the Secretary of State, don’t you? Isn’t that right, Jesse?”

At President Donald’s call, the middle-aged woman seated at the pentagonal table smiled and greeted us with her eyes.

Only then did I realize that the people gathered here were the central figures supporting the superpower known as the United States.

*The key figures in the U.S. military and political worlds.*

There were only a few people wearing suits. Since the Secretary of State, whom I had met briefly when she attended the joint national funeral, was one of them, most of the people in suits were probably cabinet-level officials or held equivalent positions.

And the military…

*There are a shitload of them.*

It was literally a feast of stars.

Middle-aged and elderly generals, some with half-gray hair and others with heads full of white hair, stared at us curiously with glittering insignia and stars pinned to their dress uniforms.

“Ah, I’m late with the introductions.”

President Doramp noticed where I was looking and continued.

“Well, everyone. This is Mr. Choi, who oversees the Peace Guild and Ares Guild. And this is Mr. Jin, whom everyone already knows. And the people over here are…”

Jack. Philip. Joey. Liam. Isabella.

Names and titles I had heard at least once in Hollywood war movies flashed past one after another.

Team Leader Choi, who normally seemed to know everything, appeared to recognize all their faces and names. I could only stare blankly and nod.

*Why are there so many departments and positions?*

The only people who really stuck in my mind were the directors of the CIA and FBI. That was probably because those special organizations appeared so often in movies.

“Now that the introductions are over, I should tell you why we brought you here so suddenly.”

Snap. Fwoosh!

The instant President Doramp snapped his fingers, the holograms that had briefly disappeared filled the room in every direction.

*This is…*

A map. Not a map of the entire Earth, but one depicting a specific region in precise detail.

Coordinates were written over countless buildings and various landforms, while markers of unknown significance glittered here and there like stars.

*Oh.*

The place names written on the holographic map. The terrain scattered with deserts.

And the words President Doramp had spoken when we first arrived.

I realized what it was and muttered,

“The Middle East?”

“It’s a tactical map showing the locations of the terrorist groups. The sparkling markers are probably Gates or their bases.”

I wasn’t the only one to speak. President Doramp nodded at the answers Team Leader Choi and I gave almost simultaneously.

“Both answers are correct. However, Mr. Choi’s answer was much more detailed and closer to the truth. Those lights mark locations believed to be terrorist-group headquarters. Hologram, zoom out.”

Whoosh.

The enlarged hologram shrank into the shape of a globe.

As the globe slowly rotated at President Doramp’s gesture, large and small lights glimmered across its surface.

“All of those are terrorist groups?”

“When my late father was president, there were already more than a hundred Islamic terrorist organizations. Of course, after the Great Cataclysm, they multiplied at a frightening rate.”

That was the first I had heard of it.

More than a hundred Islamic terrorist organizations alone—and that had been before the Great Cataclysm. There was no telling how many there were now.

Of course, some of them were probably small terrorist groups that operated on the level of clubs. But the problem was that they were not doing comic-book-club activities. They were carrying out terrorist attacks with the goal of killing people.

*No, seriously. Why are there so many?*

I had known there were plenty of crazy people in the world, but I had never dreamed there were this many.

Team Leader Choi, his eyes dark as he gazed at the hologram, spoke.

“Does that exclude the rebel forces scattered throughout Africa?”

“That’s a good question, Mr. Choi. But fortunately, the rebels are included in that number as well.”

“Just as you said, Mr. President, that truly is fortunate. And I think I understand why you went out of your way to invite us.”

Team Leader Choi continued in a low voice.

“You’re planning to launch an operation to wipe out the terrorist groups, aren’t you?”

“That’s right.”

President Doramp did not deny it. He nodded heavily.

“As both of you know, the United States is still the world’s greatest power, but that also means we face an equal amount of opposition. Therefore, we have no choice but to act cautiously, both militarily and diplomatically.”

No matter how much of a venerable international bully the United States was, it was not powerful enough to chew up every country in the world.

And after suffering the most severe damage during the Great Cataclysm, that was even more true.

“But the terrorist groups and rebel forces operating in the shadows throughout the world must disappear as soon as possible. I’m sure both of you understand why.”

Of course I did.

As Magic Johnson had mentioned, terrorist groups and the African rebels had begun experimenting with Gates and Magic Gems.

There was no way to know what results they would achieve through those experiments, or whether they would succeed or fail. But one thing was certain: the experiments themselves were dangerous enough.

*Like nuclear testing.*

Even when North Korea merely conducted a missile test, the eyes of the entire world turned toward it.

Of course, Koreans just thought, *Those bastards are acting up again,* and went about their daily lives. But that was because they knew those bastards would not actually launch the missiles.

Terrorist groups, however, were just as crazy as North Korea. No, they were even crazier.

“You must have heard about this from Mr. Johnson. Even today, terrorist groups carried out the same kind of operation simultaneously in California, Arizona, and Texas. And this isn’t happening only in the United States.”

President Doramp gently swept his hand through the holograms.

The globe vanished, replaced by dozens of small holographic windows.

> “Surrender! If you put down your weapons and surrender now…!”
>
> “God is great!”
>
> “Run! Run!”
>
> “Kraaaang!”

Dozens of languages, translated by the System, mixed together in a deafening cacophony.

People with different skin colors and appearances fled from explosions or screamed as they were covered in human bones and flesh thrown in every direction.

“There have been thirty-two terrorist attempts around the world today alone. Fortunately, as with the Texas incident reported in the news, the damage has still been minor. But if the terrorist groups finish their experiments using the Gates and Magic Gems they possess…”

Chuck Hagel, fiddling with his cigar, cut in roughly.

“Fuck. Needless to say, everything will go to shit. Monster waves will start occurring whenever the hell they feel like it, just like the recent incident in South Korea.”

Magic Johnson also spoke with a sigh.

“And the rebels won’t stay quiet, either. They’re just as dangerous as the terrorist groups. They kidnap even children, brainwash them, and use them as soldiers. If it meant taking over a country, they wouldn’t bat an eye even if tens or hundreds of thousands of people died.”

Why was I suddenly reminded of the saying that the most benevolent thing in this world, and the most vicious thing in this world, were both human beings?

At the same time, the bodies and screams of the people who had died before my eyes only a few weeks ago resurfaced in my mind, weighing heavily on my heart.

“Hmm.”

I glanced sideways at Team Leader Choi with a low hum.

His gaze was deeply sunken as he remembered someone who had left his side not long ago.

*That must never happen again.*

I didn’t know how cruel people could become.

How many people had to die or be injured before this insane wheel would stop turning.

But at the same time, I thought it was fortunate.

I possessed enough power to stop that endlessly turning wheel, even if only for a moment.

And if I couldn’t stop it…

*Then I’ll have to break it.*

Having already made up my mind, I looked at President Doramp and suddenly spoke.

“When will the operation to wipe them out begin?”

A smile spread across his lips as he recognized the meaning behind my question.

At President Doramp’s signal, one of the people seated at the pentagonal table rose.

“Assuming the entire UN Security Council agrees, we estimate that it will take two months at the earliest to complete all preparations. At the longest, it may take more than six months.”

“Two months at the earliest?”

That was slow. Much slower than I had expected.

I frowned slightly and continued.

“Considering how dangerous you’ve said the situation is, doesn’t that seem like an awfully long time?”

“There’s nothing we can do under international law. In particular, deploying troops to the Middle East and Africa without the consent of those countries would be an obvious violation of their sovereignty.”

“I looked at modern history textbooks, and it seemed like you fought in the Middle East just fine. I even watched a documentary criticizing oil money.”

The key government official who had been listening suddenly lost his ability to speak and cleared his throat.

“Erm… That was because of the 9/11 attacks, and now, under the new international agreements formed after the Great Cataclysm…”

“Forget it, then. Anyway, you’re saying two months is the absolute fastest?”

“Ahem. Yes. That’s right.”

After thinking for a moment, I leaned toward President Doramp and whispered very softly,

“Um, may I ask you one thing?”

“Ask anything you wish.”

“If an unidentified—say, a mysterious stranger—were to wipe out the African rebels or the terrorist groups in the Middle East, would that also violate international law?”

“Huh?”

“Like Batman or Spider-Man. Something like that. And lower your voice before you answer.”

President Doramp stared blankly for a moment, unable to understand what I meant. Then he barely managed to force out his voice.

“So you’re saying that Mr. Jin would hide his identity and launch an operation against the terrorist groups…?”

“Me? Why would I?”

“No, if I interpret what you just said…”

“I never said anything like that. I was just giving an example.”

“W-wait a moment, Mr. Jin.”

“This man is going to cause a disaster. Why would I do something like that alone? Unless I were some lunatic who stormed into Ares Guild headquarters by himself.”

“…”

A suffocating silence descended over the room.

President Doramp stared at me as if I were insane, then finally parted his lips.

“It seems I misunderstood you. To think of such an absurd thing…”

“Right?”

“Yes. In that case, we’ll conclude today’s meeting here. I’ll be accidentally leaving the holographic tactical map behind.”

“Ah, of course. An accident.”

“Yes. It’s top-secret—more secret than any other classified information—so it must never be leaked outside. Especially since it contains the precise locations of rebel forces in the Middle East and Africa.”

“And what else? Is there anything else?”

“Everything you need is included in the materials. Ah, of course, Mr. Jin will have no opportunity to obtain those materials and will be heading straight back to Korea. Isn’t that right, Mr. Johnson?”

Magic Johnson, having caught on, nodded.

“Of course, Mr. President. But I hear Jin likes to travel. I’m not sure whether I’ll be able to spend a few days with him and be away from my post.”

“Ah, is that so? Do you have a preferred region…”

I answered without taking a breath.

“Africa and the Middle East. I especially love deserts. My dream is to pee in an oasis and give Churu to the Sphinx.”

[^1]: Churu is a popular lickable cat treat.

Team Leader Choi added in a calm tone,

“I was born in summer, so I like hot places.”

“What a coincidence.”

“Are you ready, Choi?”

“Of course, Johnson… No, this feels a little strange.”

Amid the confusing yet remarkably smooth conversation, Chuck Hagel bit down on his cigar and brought it to an end.

“A lunatic is going to kill lunatics.”

He was right.

Madmen should be killed by madmen.

* * *

It was an ordinary day.

After interrogating a foreign prisoner and killing one subordinate who had been acting cocky, the leader of an Islamic armed terrorist group returned to his bedroom.

Muhammad Saladir ad-Din encountered an uninvited guest before he could even take off his outer clothes.

“Stand up straight, Hassan.”

“...?”
## Chapter artifact 609

# Chapter 609

“Stand up straight, Hassan.”

“...?”

Muhammad Saladir ad-Din, the leader of a massive Islamic terrorist group, was momentarily taken aback.

Who the hell was Hassan, and whose voice had just spoken in his bedroom, where no one else should have been?

But if he had been the kind of man who lost his composure over something this minor, he never would have risen to his current position.

Muhammad calmly opened his mouth.

“Sorry, but I’m not Hassan. I don’t know who you are, but you seem to have mistaken me for someone else.”

“I don’t think so.”

*Step.*

The uninvited guest emerged from the darkness, speaking flawless Arabic with not a syllable out of place. After confirming the man’s face, Muhammad narrowed his eyes.

*What the hell? What is this strange bastard?*

Although the man’s features were impossible to make out, the mask covering his face was bizarre enough on its own.

It wasn’t a turban or a piece of cloth. It was made of thick red yarn, with gaping holes cut out for the eyes and mouth.

Calling it a mask was strange enough, but Muhammad had never seen a lunatic wearing something like that in the middle of a scorching desert.

He asked, unable to hide his confusion.

“Who are you?”

The man, who appeared to be an assassin, answered.

“I’m Mami…”

“Mami?”

“No, I’m a back scratcher.”

“...?”

A filial son was one thing, and a hand was another. So what the hell was a “filial son’s hand”[^2] supposed to be?

[^2]: The Korean word *hyojason* literally means “a filial son’s hand” and refers to a back scratcher.

One thing, however, was certain: the strange man had not come to visit him in order to practice filial piety.

“Who sent you?”

“Allah.”

“Allah?”

“Yeah. That Allah you’re always sucking off.”

Through the gaping hole in the mask, Muhammad could see the man’s lips curl slightly upward.

“He told me to tell you this. He never told you to do any of that shit, so stop interpreting the scripture however the fuck you feel like.”

“You insane bastard.”

“I never thought I’d live to hear a terrorist leader call me an insane bastard. What a shitty life.”

Muhammad solemnly opened his mouth while considering when to draw the scimitar at his waist.

“You foolish bastard. Do you really think you’ll get away with this?”

“Yep. I think I’ll be fine.”

“You seem eager to die. If you surrender now…”

“Yeah, I think I heard that a minute ago. Hang on.”

The strange man rummaged through his clothes before suddenly pulling something out of his sleeve and throwing it.

*Thud. Roll…*

With a fairly heavy sound, a round object came to rest at Muhammad’s feet.

Healthy bronze skin, like that of a desert warrior, and eyes frozen wide open. Not a drop of blood stained the cleanly severed neck.

“K-Kasim?”

“Why are you so surprised? Do you know the face?”

“...!”

Muhammad froze solid.

Kasim had been the bodyguard and assassin he trusted more than anyone.

An S-rank Hunter unknown to the world, Kasim was an awakened assassin whose victims were too numerous to count.

*But he killed Kasim? And did it so quickly and secretly that no one noticed?*

*Allah help me. This is real.*

Fear seized his entire body, and Muhammad’s voice began to tremble.

“I-I’ll give you one last chance. If you leave now, I’ll forget what happened today and take no revenge.”

“N-No, dumbass. Why would I bother with all that when I can just kill you?”

“T-Then I’ll give you as much wealth as you want! Diamonds! What about diamonds?”

*His ultimate diamond attack!*

“Diamonds? You mean the ones in the safe under your desk? I already took those. They were pretty.”

*But nothing happened! Muhammad’s world went dark!*

“Bodyguards! Bodyguarrrds! Omari! Sadat! Nasser! Where are you all?”

As Muhammad, having lost his composure, shouted the names like a scream, the strange man shouted along with him.

“Omari! Sadat! Nasser! Right here!”

*Thud. Thud. Thud.*

“Woohoo! Bodyguard heads acquired!”

How had all those heads come flying out of that narrow sleeve?

Muhammad was staring in horror at the three heads that had fallen one after another when—

*Bang!*

Despite the commotion inside the bedroom, the firmly closed door suddenly flew open. A huge man wearing the same kind of mask walked in and opened his mouth.

“Is this terrorist asshole still alive?”

The instant Muhammad saw the blood covering the giant’s hands, he froze like a statue. The strange man raised a hand in greeting.

“There’s still work to do. But are you finished cleaning up?”

“More or less. The other two are downstairs looking for this and that. By the way, can’t I take off this shitty mask? I’ve been suffocating in it.”

“No.”

“Damn it. Then at least let me smoke a cigar. My face is covered with illusion Magic anyway.”

“Why not wear your identification around your neck? And if you have even a shred of sense, wouldn’t you have accounted for illusion Magic? You’re already huge, and if you smoke a cigar with those skills, you’ll be practically advertising that you’re Chuck Hagel.”

Muhammad’s eyes widened as he realized something.

“C-Chuck Hagel? You bastards! You’re from the United States!”

“Gasp. How did this bastard figure that out? Chuck, there must be a spy among the U.S. leadership.”

At the strange man’s startled reaction, Chuck Hagel pulled out a cigar and muttered,

“...Crazy Korean.”

“No, Chuck. Are you insane? If you say Korean here, he’ll understand us.”

“I think I’m going to lose my mind. I think I’m going to lose my mind. I think I’m going out to eat lunch…”

But the person who really seemed about to lose his mind wasn’t Chuck Hagel. It was Muhammad himself.

Chuck Hagel’s name alone had been bad enough.

But a Korean?

At this moment, Muhammad could not help thinking of the name of the most famous Korean in the world.

“J-Jin Taekyung?”

“No, I’m a back scratcher.”

“D-Don’t give me that bullshit. Who do you think you’re fooling?”

*Whoosh! Slash!*

The jeweled turban was sliced off, and even the few strands of hair remaining on Muhammad’s head were cut away as if erased.

The strange man—or rather, Jin Taekyung—asked the frozen Muhammad, who had forgotten how to breathe.

“I’ll ask again. Who am I?”

“A-A back scratcher.”

“You said Jin Taekyung a moment ago.”

“I-I was mistaken. I must have mistaken you!”

“Really? Can you swear to God?”

“I-I swear by mighty Allah and the Prophet Muhammad! You’re a back scratcher!”

“How dare you swear by God and lie. I’m Jin Taekyung, you apostate bastard!”

“Gyaaaaaah!”

Muhammad, seized by terror, screamed with all his strength. But the sound vanished without ever leaving the bedroom.

A barrier of qi created by magnificent internal energy had sealed the space without the slightest gap.

“W-Why the hell are you doing this to me?”

Muhammad was crying now. Chuck Hagel let out a quiet laugh.

“Don’t ask us. Ask the god whose name you’ve been peddling. You’ll meet him soon enough anyway.”

“...!”

“Oh. Of course, there’s something you have to do before that.”

Muhammad never heard Chuck Hagel’s final words.

The meaning of what he had heard before already filled his mind to bursting.

*Meet God? I’m going to die? Me?*

Death.

Every human being thought about that word, but not Muhammad. He had always been the one who dealt death, never the one on the receiving end.

A shrill voice slipped between his trembling lips.

“T-That can’t be. It can’t.”

He had joined an armed terrorist organization as a boy. He had held an automatic rifle instead of a pen, and after awakening, he had taken up a sword.

Then, after rising through the ranks, he became the leader of a terrorist organization and kidnapped, imprisoned, and brutally executed countless people.

Muhammad, who shared a name with an ancient prophet, believed himself to be a new prophet and leader.

But. But why?

“I-I’m protected by God. How could this…”

“It’s simple.”

The corners of Jin Taekyung’s mouth, which had been raised through the holes in his mask, slowly sank.

His voice had grown cold.

“You’re a fucking lunatic who used God’s name to commit every kind of insane act. That’s why you’re dying.”

“...!”

“You attacked civilians, kidnapped children and brainwashed them, strapped bombs to their bodies for suicide attacks… I can’t even count them one by one. There were too many.”

*Hack. Ptooey.*

Chuck Hagel spat, and the phlegm landed thickly on Muhammad’s face. His rough voice followed, cutting into Muhammad’s ears.

“So I’ll give you one last chance. You’re a fucking terrorist bastard who deserves to be tormented by Johnson all week, but if you cooperate, you’ll at least have something to say in your defense before God.”

“What, what does that mean?”

“It doesn’t mean we’re letting you live. But you might be able to die with a little less pain.”

“W-What the hell do you want?”

“Orders.”

“What?”

“We know you have countless branches under your command. We also know about the other armed terrorist organization at odds with you. The problem is that wiping them out one by one would never end. So give them orders.”

*Hoo…*

Chuck Hagel exhaled acrid cigar smoke and grinned.

“Start an all-out offensive against the hostile forces right now. Fight until one side is reduced to grains of sand in the desert and crumbles away. Got it, you son of a bitch?”

“...!”

Facing Muhammad, whose eyes were wide with terror, Jin Taekyung pressed his hands together as if in prayer and added one more thing.

“From now on, kill each other.”

Muhammad finally understood.

He had no choices left.

Behind his refusal of this final offer waited nothing but a painful and desperate death.

* * *

If I had been a reasonably popular webnovel author, I could have gotten at least five episodes out of this incident.

A power struggle between large and small armed terrorist organizations, political scenes, and various other ingredients thrown in for flavor could probably have stretched it to ten episodes.

But I wasn’t a webnovel author, and there were far too many terrorist groups and rebel forces that needed to be dealt with immediately.

In short, we had to run our asses off.

*Kaboom!*

*Boom-boom-boom!*

At first, we tried to deal with them quietly. But the area we had to cover was so vast and our numbers were so small that, at some point, we began receiving a warm welcome.

And the single word *enemy* included a hail of gunfire and artillery shells, along with Awakened who called themselves “warriors of God.”

“Kill them!”

“They’re the ones who wiped out the mujahideen!”

“Thirty million dollars immediately to whoever captures or kills them!”

*Shishshishshishk!*

As I dodged the attacks raining down from every direction, I shouted in amazement.

“Wow, our bounty went up!”

“Shut up and dodge!”

“I think it was ten million dollars yesterday. So this is why Luffy goes pirating!”

“Fucking shut up! Motherfuckeeer!”

“Fifty million! Let’s hit fifty million! The Grand Line is just ahead!”

Sometimes we fought pitched battles. Other times, we swept away terrorist groups or rebel forces like stealthy visitors in the night.

And in the Grand Line—no, the desert—we finally arrived at a place where a living treasure was waiting for us.

“Leader of the Sooni sect. Omar al-Hussein, right?”

“It’s Sunni, not Sooni.”

“What are you talking about, you bastard who looks like Jeomsoon from the land steward’s house.”[^1]

“Bastard…!”

“Hey, kid. Spring fists taste best in spring.”

*Crack!*

We didn’t stop.

We fought battles in dozens of regions every day, captured the leaders of terrorist groups and rebel forces, or controlled them with Magic Johnson’s custom brainwashing Magic.

And just like that, a week passed in the blink of an eye.

[^1]: Jeomsoon is a character in Kim Yu-jeong’s short story *Spring, Spring*, the daughter of a land steward.

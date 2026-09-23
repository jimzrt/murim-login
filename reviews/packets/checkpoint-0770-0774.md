# Checkpoint Review — 770–774

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

# Chapters 770–774

## Plot

The Skeleton King asks Jin Taekyung to erase him publicly so Michael Silbert cannot exploit his identity. Jin refuses to sacrifice his friend and instead considers killing Michael, then placing Team Leader Choi and their allies in control of the reestablished World Hunter Federation. Before Jin and Choi can fight over this plan, Magic Johnson sends documents that reveal a possible fourth path: defeat their enemies while keeping themselves and the Skeleton King alive.

Michael uses the UN's approval of the Federation to transform worldwide fear into public hope. He presents Cheon Taemin as the rightful representative and announces the inaugural ceremony in Seoul, while secretly communicating with The Prophet and ordering surveillance of the Skeleton King. Jin, Choi, and their allies return to Korea and organize a covert operation. Choi gives instructions to fewer than ten trusted senior members of the Peace and Ares Guilds, while Jin withholds the new clue from Baek Hanseong because Michael may have spies near the President.

On the eve of the ceremony, Jin refuses to visit his mother and Hayeon, fearing that emotion will compromise him. Felix, Magic Johnson, Chuck Hagel, Faye Chen, and Choi gather for a secret meeting. Jin's Broken Body continues draining his strength, but he proceeds with the plan alongside the Peace and Ares Hunters. At the First National Assembly Hall, Michael prepares to claim Cheon Taemin's former position and ascend as humanity's leader when an unidentified voice interrupts him.

## Continuity

- The World Hunter Federation has been reestablished, with its inaugural ceremony taking place at the First National Assembly Hall in Seoul.
- Michael Silbert intends to occupy Cheon Taemin's former central position and become the Federation's leader.
- Cheon Taemin remains absent, and the Federation's representative has not yet been determined.
- Michael has converted public panic into support for the Federation and is secretly communicating with The Prophet.
- Michael ordered heightened security and surveillance of the Skeleton King, whom he believes is Jin's emotional weakness.
- Jin has rejected sacrificing the Skeleton King and is pursuing a fourth path that may eliminate Michael and their other enemies without killing the Skeleton King or themselves.
- The clue supporting the fourth path remains unverified and is being withheld from Baek Hanseong because Michael may have surveillance or a mole near him.
- Jin and the Skeleton King remain together inside a concealed, imperceptible space; the Skeleton King has been completely silent.
- Team Leader Choi has completed preparations and covertly briefed fewer than ten trusted senior Peace and Ares Guild members.
- Jin's Broken Body still consumes part of his strength, but he is committed to acting.
- Jin has not seen his mother or Hayeon before the ceremony.
- Felix, Magic Johnson, Chuck Hagel, Faye Chen, and Team Leader Choi have coordinated privately before the ceremony.
- The ceremony is not being broadcast live, and its attendee list remains secret.
- Michael is interrupted just as he prepares to claim leadership; the identity and intent of the arriving speaker are unresolved.

## Translation Decisions

- Retain **World Hunter Federation**, **Great Cataclysm**, **Michael Silbert**, **Jin Taekyung**, **Skeleton King**, **Magic Johnson**, **Cheon Taemin**, and **The Prophet**.
- Render **소멸** as **Erasure** when referring to destroying the Skeleton King.
- Render **네 번째 길** as **fourth path** and **발족식** as **inaugural ceremony**.
- Render **최 팀장** as **Team Leader Choi**.
- Render **파이 첸** as **Faye Chen** and **척 헤이글** as **Chuck Hagel**.
- Render **왕자 전하** as **Your Highness**; use **His Highness Prince Felix Alexander Louis** for Felix's formal address.
- Render **제1 국회의사당** as **First National Assembly Hall**.
- Retain **Broken Body** as the name of Jin's ongoing condition.
- Preserve the chapter's use of **Stone King** where that title is used for the monster.

## Durable state

{
  "active_continuity": [
    "Jin and Team Leader Choi have returned to Korea and are operating under heightened security before the World Hunter Federation's inaugural ceremony.",
    "Team Leader Choi has completed preparations, and Peace and Ares Guild Hunters are accompanying Jin to the ceremony at the First National Assembly Hall.",
    "Jin's body remains affected by Broken Body, which drains part of his strength, but he is determined to act anyway.",
    "Jin is withholding the discovered clue from Baek because Michael Silbert may have a mole or surveillance near the President, and the clue may not be genuine.",
    "The Skeleton King remains concealed with Jin inside an unknown space that others cannot perceive and has remained completely silent.",
    "Michael intends to fill Cheon Taemin's former central place in the World Hunter Federation and ascend to leadership.",
    "Cheon Taemin remains absent while the public awaits the Federation's representative.",
    "The inaugural ceremony's attendee list is secret and the event will not be broadcast live."
  ],
  "continuity_sources": [
    774
  ],
  "open_questions": [
    "Is the clue discovered by Jin and his allies genuine, and is their fourth path viable?",
    "What coordinated plan do Michael and The Prophet have for the Federation and the coming crisis?",
    "Who will become the World Hunter Federation's representative while Cheon Taemin remains absent?",
    "Why has the Skeleton King remained silent inside the concealed space?",
    "What will happen when Jin's group confronts Michael at the inaugural ceremony?"
  ],
  "safe_through": 774,
  "temporary_decisions": [
    "Render 파이 첸 as Faye Chen.",
    "Render 척 헤이글 as Chuck Hagel.",
    "Retain World Hunter Federation and inaugural ceremony.",
    "Render 왕자 전하 as Your Highness.",
    "Render 제1 국회의사당 as First National Assembly Hall."
  ],
  "version": 1
}

## Reading copies

## Chapter artifact 770

# Chapter 770

“As for the Skeleton King… it’s because he’s a monster.”

Silence followed as that voice weakly faded away.

Yet Team Leader Choi’s final words continued to ring in someone’s ears like an echo.

*A monster… A monster, huh.*

The Skeleton King muttered the words inwardly and turned over the bitter truth.

It was true. He was a monster.

Humanity’s greatest and worst enemy in all of history.

That was what a monster was, and he was a being who wielded the cursed power of death among them.

Even if he wore a human appearance now, once the Magic wrapped around his entire body was lifted, all that would be revealed was the skeleton of a dead man who had defied the fate of mortality.

That alone was the only truth.

*Yes. This must be all there is.*

The Skeleton King silently stared down at his own two hands, which were no different from a human’s, then suddenly raised his head.

He saw a familiar face—but it belonged to a young human whose expression was twisted enough to seem unfamiliar at the same time.

The strongest being he had ever seen. A human who was also foolish in some ways, and therefore unable to accept the truth before his eyes.

But to move toward the one and only breakthrough, he had to accept that truth and make use of it.

“That human is right. It is all true.”

“……You.”

Countless emotions filled the restrained voice.

A few months ago, he would not have been able to recognize the name of those emotions.

Now, he knew them.

The Skeleton King shook his head at Jin Taekyung, who could not continue speaking.

“No matter what you say, this is the only way.”

“……!”

“This body is a monster. No matter the reason, it is unacceptable for us to remain together.”

Of course, there might be some who would understand even after the truth came to light. They might trust Jin Taekyung and accept that the Skeleton King was different from the monsters they knew.

But…

“How many of them do you think would truly accept this truth?”

The Skeleton King pointed toward the closed window.

Most of the humans living outside were perfectly ordinary. That was why they could not help but hate monsters to their very bones.

Because they had lost their families, their friends, or their beloved partners to monsters.

Monsters killed humans, and humans killed monsters.

The chain forged at the moment of the Demon King Asmodeus’s descent was too thick and sturdy for anyone to break.

Not even a young hero loved by everyone would be an exception.

No. If everything were revealed, he could no longer remain the same hero he had been before.

“Many people will condemn you, and Michael Silbert will gain everything. So…”

His words gradually trailed off. Turning away from Jin Taekyung, the Skeleton King placed his hand on the doorknob and added one last sentence.

“Erase this body in front of everyone.”

Click.

The door closed behind him.

The Skeleton King did not look back as he crossed the hallway in silence. The lights above his head were bright, but the path before him was dark.

Just like that place filled with dense fog and the energy of death.

Just like the Gate he had been unable to leave from the moment he first opened his eyes—until, one unexpected day, a human came and took him away from it.

*What am I, exactly? What is my name? What is my past? Where is my homeland?*

He thought he finally knew the answer to the questions that had begun haunting him at some point.

He was a monster.

A cruel and savage monster with no trace of reason.

A being born from pure evil, one that could never coexist with humans.

That was the truth. No—that had to be the truth.

Faced with a reality he had no choice but to accept, the Skeleton King let out a hollow laugh.

*Damn it. I’ll never be able to go to a club again.*

But why was that?

One corner of his chest felt strangely relieved.

He was a monster who had no heart and could not even harbor ordinary emotions.

He was supposed to be.

* * *

Even if no one ever told you, you naturally came to understand it as you lived from day to day.

Life was a series of choices made at every moment.

Not every choice was something grand. From the moment a person opened their eyes in the morning, small options presented themselves.

*Should I get up or not? If I get up, should I take a shower? Or should I just wash my face and hair before heading out?*

The choice changed depending on the situation at hand.

If you woke up earlier than expected, you could sleep a little longer. If you were worried about being late, it was perfectly fine to skip your shower.

But before making a choice, you had to consider the result it would bring.

A result you had no choice but to bear yourself.

And at that very moment, I stood at a crossroads where neither choice was something I could easily endure.

“You… fucking lunatic.”

The voice I barely managed to squeeze out burst from my mouth.

It could have been a curse directed at someone who had already left, or at another person who remained behind.

Or perhaps at myself, unable to move in either direction.

“Mr. Jin Taekyung.”

My head throbbed from the tangled mess of thoughts inside it. I silently closed my eyes at the quiet call that pierced my ears.

“You must choose.”

It felt as though an invisible awl had pierced straight through my brain.

With every word he continued to speak, my headache grew worse.

“He has already chosen his path. The sacrifice that only he could decide to make…”

Crash!

I didn’t even know.

When had I opened my eyes? And why was I gripping Team Leader Choi by the collar?

Riiip.

The collar of his crumpled designer shirt tore under the force of my grip. Above my whitening knuckles, a pair of eyes silently gazed at me.

“Do whatever you wish. You may beat me until I am reduced to a bloody mess. You may break my limbs, or even kill me. I do not care. But…”

His breath trembled as his voice continued.

“Afterward, you must choose. You must.”

“……!”

“You know that, don’t you? Time will not wait for us.”

At those words and that gaze, all the strength suddenly drained from me.

The energy boiling through my entire body as if it were about to explode, the hand clenched with all its strength—everything felt strangely unfamiliar.

I backed away like someone who had been possessed for a moment.

Along with a powerless apology.

“…I’m sorry.”

I knew it too. Team Leader Choi had done nothing wrong.

Everything he had said was true. It was simply the only solution capable of breaking through this situation.

If the Skeleton King had not declared his intention to sacrifice himself, Team Leader Choi would not have said anything either.

That was the kind of person he was.

Although his cold judgment had already led him to the only solution, he possessed the morality not to force someone else to make the sacrifice.

Some people might call a person like that a hypocrite, but I was not one of them.

Because I knew that to Team Leader Choi, just as to me, the Skeleton King was not merely some monster that had to be killed and eliminated.

*Even if he were the one who had to sacrifice himself, he would have offered it as the solution before anyone else.*

Unlike me, he was a born leader.

If he had been the one with the choice instead of me, he would not have avoided it.

He might have suffered alone, but he would never have cowardly turned his eyes away from the truth.

*Damn it.*

Time would not wait for us.

When I recalled Team Leader Choi’s words, another world waiting for me beyond the horizon flashed before my eyes.

Murim.

If the Login function had not been blocked by the main Quest, and if I could spend much more time thinking about it there, what choice would I make?

No. If I were given enough time, would I finally be able to make a choice at all?

*And can I bear the consequences?*

Until now, I had fought countless battles.

I had struggled to survive and fought to protect my people.

But at the end of the two paths before me, nothing remained except pain.

If I did not sacrifice the Skeleton King, this world would fall into Michael Silbert’s grasp. But if I sacrificed him as things stood…

I did not think I could endure it.

Yes. I did not know when it had happened, but the Skeleton King was my friend.

A comrade who had fought beside me, and a friend.

He was someone I could not sacrifice merely for the sake of two words: the greater good.

*I have to erase him. And I have to do it myself, in front of everyone.*

A pathetic trick like using the Inventory to fake his Erasure would not work. Michael Silbert was not careless enough for that.

Even proving that I had complete control over the Skeleton King would not change the situation.

To humanity, monsters were a raw nerve that must never be touched.

Hadn’t decades of experiments already proven that monsters could never be tamed?

The Skeleton King was an unprecedented existence, and certain truths were rejected the moment they became known.

*In the end… there is only one answer.*

I closed my eyes. Then, after countless thoughts flashed through my mind like bursts of light, I suddenly opened my mouth.

“Team Leader Choi.”

He had been silently waiting for my decision. He answered.

“Yes?”

“Is there any chance the approval to reestablish the World Hunter Federation could be revoked?”

“Why are you suddenly asking that…”

“Just answer me.”

I opened my eyes with a firm voice. Team Leader Choi stared at me with a complicated gaze before speaking.

“There is no chance of the approval being revoked.”

“Are you sure?”

“Yes.”

“Why?”

“The World Hunter Federation is now indispensable. Given the current situation, with magical power levels rising every day, it is the only way to stop a spark that has already been lit from spreading.”

“Even if something happens to me or that bastard in this situation?”

“……!”

His eyes shook violently.

It did not take long for Team Leader Choi to realize what I meant. He shouted furiously.

“Mr. Jin Taekyung!”

But I had already made my choice.

Not the first path. Not the second.

A third path, dark and covered in thorns.

That was right.

I would kill Michael Silbert, the center of all this.

“No!”

“There’s nothing that can’t be done. It’ll just be difficult.”

I answered calmly and continued without giving him a chance to interrupt.

“When what I’m about to do is successfully finished… you’ll have to move then, Team Leader Choi. Magic Johnson will help with everything he has.”

“Stop! Stop it!”

“There’s Chuck Hagel, Pai Chen, and Prince Felix as well. Take control of the reestablished World Hunter Federation by gaining the support of the S-rank Hunters you’ve built good relationships with and the friendly nations.”

“I don’t want to hear this! And how could I possibly…!”

“It is the path your maternal grandfather, Cheon Taemin, walked. If you can make people understand the weight carried by the name Cheon Taemin, it’s worth aiming for. If you think it’s impossible, supporting Magic Johnson is another option.”

I grinned and added,

“Although you’re so smart, Team Leader Choi, I’m sure you’ll manage just fine on your own.”

“……!”

“Still, just to be safe, there’s one more thing I need to ask of you. Even if Michael Silbert’s head is cut off, his body will remain. It would be better to hunt down and eliminate those people first…”

Shing.

At the sudden chill of the sound that rang through the room, I closed my mouth.

A sword blocked my path.

Team Leader Choi had drawn the *Hero’s Sword* without me noticing. He glared at me with a rigid expression.

“You’re not going.”

“Hm. I don’t think you’ll be able to stop me.”

“Nothing is impossible. It’ll just be difficult.”

Team Leader Choi threw my own words back at me, and I stepped toward him.

“Fine. I was planning to rough you up once anyway. This works out.”

“What does that mean…?”

“Who doesn’t know we’re close? If I leave after beating you half to death, people will be less suspicious.”

“……!”

“……!”

Grind. Hssss!

Team Leader Choi clenched his teeth and raised a dazzling aura. The mighty concentration of power rippling along the blade summoned a wind.

Rumble. Whoooosh!

A tremor spread through the entire building. Before long, the fierce wind had turned into a gale.

“You definitely have talent. You’ve improved a lot.”

I smiled calmly and was about to take a step when—

Bzzzt.

A faint vibration ringing from somewhere pierced the tension flowing between us.
## Chapter artifact 771

# Chapter 771

Bzzzt.

It wasn’t difficult to figure out what the vibration was. I had something in my own pocket that made a similar sound, after all.

“Team Leader, it looks like you’re getting a call. Aren’t you going to answer it?”

“Don’t concern yourself with it. That is not what matters right now.”

“What, are you afraid I’ll ambush you while you take the call?”

“That…”

Team Leader Choi let his voice trail off.

The fact that we were standing off against each other like this was absurd to begin with.

No matter how outstanding his natural talent was or how quickly his skills had improved, there was no way he could stop me.

The only reason he was still standing there was entirely because I was holding back.

Holding back for a friend I would have no choice but to bring down.

And, in a way, it was restraint for a reason that made sense.

“A call coming through on a direct line must be pretty important. Go ahead and answer it. I have to wait until enough witnesses gather anyway.”

“Witnesses…?”

“Yes. Witnesses.”

As I watched Team Leader Choi mull over those three syllables, I continued slowly.

“Whatever happens from here on, the more people watching, the better. For everyone’s sake.”

There was no other way.

Team Leader Choi and I had been in the same boat for a long time. If I killed Michael Silbert, it was obvious that Team Leader Choi would be dragged into it as one of my accomplices.

And it wouldn’t stop there. The Peace Guild. The Ares Guild. My family, my friends, everyone connected to me would be hurt.

If that happened, everything would be over.

*To prevent the worst-case scenario, I have to draw the line in front of as many eyes as possible.*

Soon, I would become a criminal as notorious as The Prophet—or perhaps even more so.

A traitor to humanity who, when a longtime comrade confronted him about joining forces with an undead monster, took him down without hesitation and fled alongside the monster.

And… the infamous murderer who killed the hero of the age, Michael Silbert, in broad daylight.

“This won’t end with one or two broken bones. Since you’re taking the call anyway, check that you have a potion ready.”

At my calm suggestion, Team Leader Choi bit his lip.

“…You’re serious.”

“I’ve finished thinking about it. The road I have to take has already been decided.”

At some point, I had gained too many things to protect. Before every choice, I had to think, and then think again.

But once I made a decision, I had to throw hesitation away.

The moment I looked back, hesitation would create an opening.

That was how I gradually learned not to look back.

In Murim. In the modern world.

Amid all the monsters that charged at me intent on killing me, and all the loathsome human crowds even worse than those monsters.

“This is the path I chose, and for now, it’s the best one.”

Sacrifice the Skeleton King, or hand this world over to Michael Silbert.

Faced with that impossible either-or, where I could not choose either option, I had made my decision.

Rather than being manipulated like a puppet, I would become a traitor who killed a hero and joined forces with a monster.

Even if that was what it took, I would uproot the source of this disaster.

*He’s going to die by my hand today.*

Whoosh.

A scorching heat spread throughout my body. Spitting out a single word as though I were chewing it to pieces, I unleashed the qi wave I had drawn up to its limit in every direction.

Rumble!

A violent tremor shook the surrounding area, extending beyond the entire building.

The enormous power was incomparable to what Team Leader Choi had released. The hologram television, which had been playing silently, crackled and shut off, while the alarm devices installed throughout the building let out an enormous wail.

Beep, beep! Weeeeee-oo!

“What the hell is this…? Gasp!”

“Aaaah!”

“Emergency! This is an emergency! Everyone, please evacuate!”

The people who had already been murmuring at the vibration caused by Team Leader Choi instantly broke into screams.

Amid the countless footsteps passing outside the door and the desperate shouts they were vomiting out, Team Leader Choi, who had been staring at me with a hollow expression, suddenly raised the *Hero’s Sword*.

Thunk!

The silver blade plunged into the floor, slicing through it like tofu. He squeezed his eyes shut, then opened them and pulled a smartphone and a potion from inside his clothes as though he had resigned himself to everything.

And then I saw it.

Team Leader Choi’s eyes widening, followed moments later by his fingers rapidly tapping the screen.

Flash.

With the characteristic glow of a hologram, the huge figure of a man appeared in midair. Magic Johnson opened his mouth with a more frantic expression than ever.

—Damn it. Why are you taking so long to answer? Did you look at the materials I sent? I found something strange a little while ago—wait, what the hell is going on here?

Magic Johnson had been babbling until he noticed that something was wrong and looked back and forth between us. But instead of answering him, I strode toward him.

More precisely, toward the documents in his hand.

*This is…*

The documents were filled with several photographs and tiny text.

But with my terrifying visual acuity, I grasped all their contents in barely a dozen seconds. At the same time, I thought of hypotheses I had never once considered before.

*Why the hell is this…? Wait. If that’s true…?*

Thoughts chased after one another, mixing together in a tangled mess.

Just as I was groping through the pale fog that had instantly filled my mind, searching for the truth hidden inside it—

“Ah.”

With that short exclamation escaping between my lips, the energy roiling inside my body as though it were about to explode began to settle.

Fwoosh.

The qi wave dispersed, and the vibration gradually died down.

But my gaze wavered more than ever, as did my mind after glimpsing the true shape of something beyond the fog filling my head.

*If this is true…*

Yes. If it really was…

I let the unfinished words circle inside my mouth, stared blankly at Magic Johnson, and then turned toward Team Leader Choi.

The *Hero’s Sword* was still stuck in the floor in front of him, like Excalibur.

“Team Leader Choi.”

“Yes?”

“Why did you suddenly draw your sword like that? You’re scaring me.”

“What?”

“I need to think, so put the sword away first and calm everyone down. It’s incredibly noisy outside.”

“…What?”

*What the hell? Is he insane?*

Reading the thought plainly conveyed through Team Leader Choi’s eyes, I let out a hollow laugh.

No matter how people around us looked at me, I continued to quietly chuckle to myself like a madman for quite some time before suddenly slapping both cheeks hard.

Smack!

Maybe I had hit myself too hard.

My head rattled from the full-force self-inflicted slap, but thanks to that, my mind—which had briefly gone AWOL—returned before it could make it beyond the garrison limits.

*All right.*

Only after I had completely returned to reality did I open my mouth while looking at the two men staring at me with dazed expressions.

“All right, everyone. From here on, let’s all…”

Good breathing. Good emotion.

I had to make the ending solemn.

“Let’s carve out a fourth path where every last fucking bastard dies and we survive.”

Team Leader Choi and Magic Johnson’s eyes began to twitch at this grand and solemn declaration.

“Mr. Jin Taekyung…”

—Hey, Jin…

What more needed to be said?

I gave a faint smile and nodded as though I understood everything.

At the new hope I had glimpsed in the final moment, a heat different from the Scorching Yang Qi continued to well up from somewhere inside my body.

No—it wasn’t merely welling up. It was overflowing.

Trickle. Splash!

“…What the fuck?”

Was it really going to overflow?

Heat—or rather, a torrent of red liquid—gushed from my nostrils, which had opened up with refreshing force before the fourth path even had a chance to do so. The two men’s gazes went cold.

“You have a nosebleed. A really bad one.”

—It reminds me of the fountain in the plaza of my mansion. More precisely, it looks like the baby angel built into the fountain is pissing like that.

“So you should have hit yourself more gently.”

—I think he’s going to collapse from blood loss. Choi, do you have a potion?

“I already took one out. I didn’t expect to use it in a situation like this, though…”

—Good. Hurry and give it to Jin. By the way, what did you mean earlier about a fourth path? No, never mind. Deal with the nosebleed first, then explain it again.

“Here. Take it. And move back one step, please. Your blood is splattering.”

“…”

As I accepted the potion Team Leader Choi handed me, I thought that perhaps going straight to fight Michael Silbert would have looked much cooler than this.

But this was still me.

A man who struggled somehow toward the best possible result, even if he looked uncool for now and was horribly undignified.

A realistic man busting his ass for the sake of this world where no one could see him, the true man of this era who was—

“What are you doing? Hurry up and swallow it. All at once.”

—Jin, do you have trouble taking potions? If you want, I can help you.

I looked at Team Leader Choi, who was scolding me like a mother-in-law, and Magic Johnson, who had suddenly started licking his lips for some reason, with frightened eyes before hurriedly emptying the potion into my mouth.

Ssshhh.

Then, as the ice-cold energy of healing made a circuit through my body, I found a familiar face on the hologram television, which had returned to normal as the vibration stopped as though it had never happened.

Gray hair. Gray eyes.

The man looked as though he had been born somewhere between light and darkness. He stood before countless camera flashes and cameras, continuing to speak without sound. Stark subtitles ran beneath him.

> **Live:** UN Emergency General Assembly Approves the Reestablishment of the World Hunter Federation by an Overwhelming Vote.
>
> **Michael Silbert:** “I offer my wholehearted praise for the UN’s decision on behalf of humanity, and I propose the first inaugural ceremony of the newly established World Hunter Federation.”

“Disable mute mode!”

Beep.

At Team Leader Choi’s urgent command, the noise trapped inside the speakers rushed out like a flood.

—Does that statement mean that you intend to become the representative of the World Hunter Federation yourself?

—Michael! Can an inaugural ceremony really be held in a situation like this?

—When and where would you like it to be held?

—We’re from the *Washington Post*. Please give us a statement!

Shouts like screams.

So many reporters had surrounded him that the cameras could not even capture them all, throwing questions at him from every direction. Instead of answering, Michael Silbert waved them away with a solemn expression.

Swish.

Even though it was a hologram, and even though he was actually several kilometers away at the very least, everything felt vivid.

The air surrounding a single person. The atmosphere of a scene prepared for one person alone.

The presence of that man, radiating suffocating majesty simply by being seen and heard.

Only Michael Silbert had the freedom to open and close his mouth there now.

—I swear to God, the only reason I proposed the reestablishment of the World Hunter Federation three days ago was for this world—for humanity.

—…!

I could feel it. The tumult wrapping around them.

And there he stood before a spotlight shining more brilliantly than at any moment in his life—a born agitator and orator.

—The representative of the World Hunter Federation should go to someone other than me. A living savior, the hero of the Great Cataclysm who already saved humanity from the Demon King once before!

His voice, infused with internal energy, stretched endlessly outward. Unable to contain their excitement, people looked to the sky and cried out.

Sky. Slayer. Cheon Taemin.

One man, given many names. But at the same time, a considerable number of people were chanting someone else’s name.

Michael Silbert’s name.

And amid the heat spreading like flames, he continued without hesitation.

—The inaugural ceremony will be held without fail. Whether it is the mad terrorist who calls himself The Prophet, any monster whatsoever, or even the return of the Demon King, the Hunters of the World Hunter Federation will gather in one place, choose their representative, and swear that they have become humanity’s sword and shield!

—Hurrayyyyy!

My ears rang. I could hear their roar even without the speakers now.

Through the cracks beneath the tightly closed doors, everyone in the city cried out as one.

No—perhaps from every corner of the world.

From every place where light seeped in and electricity flowed.

Surrounded by countless cheers, that hero shone alone, with no one even guessing that he was behind all of this.

And amid the immense heat that burned so fiercely it burst forth, Michael Silbert opened his mouth with a more powerful gaze and voice than ever.

Toward the frenzied people. Toward the cameras focused on him.

Or…

*Toward me—the one who could do nothing but watch him from here.*

Michael Silbert made a declaration to the entire world.

—Two days from now. Seoul, Korea.

—In that place, the savior’s homeland and where the World Hunter Federation first began, we will rise once again, just as we did then.
## Chapter artifact 772

# Chapter 772

The incitement—at once a speech and a declaration—was over.

But the enormous roar did not end. It continued without pause.

The cameras of the reporters at the scene captured everything—the people pouring out into the streets—and the microphones were filled with cheers shouted in voices gone half-hoarse.

The entire area was steeped in a festival atmosphere.

Only a few days ago, disaster had descended upon the city. Now it overflowed with an inexplicable hope and joy, and those emotions gathered together before flowing toward a single person.

“Michael! Michael!”

They shouted one man’s name and gave him their wholehearted applause.

For a very long time. With all their strength.

Not with the slightest ulterior motive toward the immense power that was the World Hunter Federation, but with gratitude and respect for the true hero who had stepped forward for them more than anyone else.

And their hero, standing on the stage, gazed at the scene with an overwhelmed expression. Then, unable to hold back his tears, he turned and hurriedly left.

A hero who had always seemed so strong could look this beautiful from behind.

From behind, that is.

“You’ve arrived.”

When Huginn, waiting below the stage, gestured with a slight bow, the Hunters of the Odin Guild hurriedly stepped in front of the reporters who were following after Michael.

“Please step back.”

“Just a moment. It’ll only take a moment…”

“I’m sorry, but today won’t be possible.”

As they walked away, the bright lights and the people’s cheers gradually grew more distant.

Michael Silbert wiped the moisture from the corners of his eyes and spoke in a dry voice.

“They responded well. Better than expected.”

“They needed that much hope. And the final tears, too. You were magnificent.”

“Did you think it was acting?”

At the unexpected counterquestion, Huginn’s steps slowed.

“Were they… sincere?”

“They were sincere. Though I don’t know whether I felt the same emotions as they did.”

Tears were truly mysterious.

They could flow from joy, sadness, anger, or even a complicated emotion that the person shedding them could not easily define.

And in that regard, the tears he had shed were closest to the last of those.

*What had they been?*

Joy at finally reaching his grand objective?

Or… the last few fragments of emotion he had left?

Michael Silbert thought about the reason for his tears, which even he did not know, but soon shook his head inwardly.

There was no need to find the right answer every time.

If he had tried to find the correct answer to every problem he had faced throughout his life, he would not be standing here now.

No. He would already be dead.

He would have died on that day, decades ago.

“Guild Master?”

The voice broke through his thoughts, and Michael Silbert gave a short reply.

“Speak.”

“I have something to report. Just before you began your speech…”

“You mean the small disturbance that occurred on the outskirts of the city?”

“You already received the report?”

“No. I sensed it faintly.”

Huginn, who had been following behind him, stopped short. Michael Silbert smiled faintly.

“What? Is that unexpected?”

“To be honest, yes. It is.”

“Yes, I imagine it was.”

It had been quite a disturbance, but the distance had been several kilometers at a rough estimate.

Michael Silbert recalled the sensation that had suddenly swept over him and continued speaking.

“It was an astonishing experience even for me. The sudden heat reaching me from so far away made every hair on my body stand on end. For a very brief moment, it felt as though I were looking down over the entire city.”

“...Guild Master, could it be that—?”

“I know what you’re thinking, but there’s no need to worry that much. I only felt that degree of sensation for an instant.”

Michael Silbert muttered as though speaking to himself.

“I probably overdid my training.”

“You should stop training for the time being.”

“I’ve already been restraining myself. I certainly pushed too hard over the past year. Perhaps I grew impatient without realizing it.”

And he already knew the reason for that impatience.

As well as the identity of the intense heat he had suddenly felt in the distance just before beginning his speech.

“What happened to Jin Taekyung? If it had been an emergency, you would have interrupted me even during the speech, so it can’t have been too serious.”

“According to the watchers’ report, the Stone King left the hotel first, and the surrounding area shook not long afterward.”

“The epicenter must have been the top floor where they were staying.”

“Yes. After that, everything went quiet as though nothing had happened.”

“The monster left first, you say? What else?”

“They tried various types of magic after approaching as closely as possible, but both the view inside and even the sounds were blocked, so…”

“That’s enough. Naturally, it would be.”

Michael Silbert, who had been lost in thought, suddenly murmured.

“It seems discord broke out inside.”

“Discord?”

“Their opinions must have differed. And judging by what Jin Taekyung has shown us so far, he may do something even more reckless than we expect.”

“If it’s reckless enough to be called that, surely you don’t mean…”

“What else could it be? In a situation like this, there aren’t many paths he can choose.”

“...!”

Michael Silbert continued, looking at Huginn, whose eyes had widened.

“Increase security and strengthen the surveillance network until the inaugural ceremony. In particular, don’t take your eyes off that monster for even a moment. He is the most important key to this entire affair—he cannot be left out of it.”

“Understood.”

Huginn answered with a grim expression, then immediately asked,

“Wouldn’t it be better to take advantage of this opportunity and capture the monster?”

“Capture?”

“Yes. If they hide the monster, or choose to uncover his identity and sacrifice him before we can…”

“Huginn.”

Interrupting him in a gentle tone, Michael looked toward his right-hand man and continued.

“I told you before, didn’t I? That Jin Taekyung possesses a fatal weakness more dangerous than anyone else’s. Do you remember?”

“His emotions…?”

“That’s right. And that is precisely why he has no choice but to carry the monster with him to the very end.”

“What you mean is…”

“Yes. At some point, Jin Taekyung began to regard the monster as a friend.”

“...!”

“It’s funny, isn’t it?”

Michael Silbert let out a quiet laugh he could not suppress.

Though he was remembered as one of the heroes of the Great Cataclysm, many walls still stood in his way.

Back then, he had not been an overwhelmingly powerful figure, and the Odin Guild had fallen short of being called a major guild.

That was why he had to become stronger. He had brought down every wall and every rival standing in his path, using any means necessary.

But it was truly laughable.

Now that he had built martial might and a powerful organization no one could afford to ignore, the obstacle standing in his way was, out of every rival he had ever faced, the softest-hearted bastard of them all.

*What an idiot.*

Michael Silbert let out a hollow laugh and continued walking.

By then, he was completely surrounded by a security team—or rather, a personal guard—emanating a razor-sharp aura.

Clomp. Clomp.

The footsteps of dozens of people echoed as one.

When they reached the building where he was staying temporarily, the Hunters escorting him spread out like the ribs of a fan and encircled the area.

A perfect defensive line that no one could break through.

Michael Silbert silently nodded toward Huginn, who was bowing at the front of the formation, then stepped into a space permitted to only one person.

Click. Fwoooong.

As soon as he entered the room, the locks engaged, followed by dozens of defensive and security spells activating in succession.

The cheers of the people, which had been faintly audible from far away only a few seconds ago, abruptly cut off.

Perfect silence had finally arrived.

But instead of leaning back against the sofa, Michael Silbert crossed the broad carpet and stopped in front of a large full-length mirror covered with black cloth.

Then he pulled away the cloth and infused his energy into the transparent mirror.

Hummm.

A finely trembling resonance rang out. At the same time, the flawless surface of the mirror rippled, and everything reflected inside it twisted.

Whooosh.

The spacious room changed, along with the furniture and fixtures scattered throughout it. Finally, the person reflected there changed as well.

In the place where everything had been transformed in an instant, someone wrapped in a thick robe was waiting for Michael Silbert amid complete darkness.

—That was a very moving speech.

The voice revealed neither age nor gender.

As The Prophet’s lips curled slightly beneath the robe, Michael Silbert’s eyes sank deep.

* * *

Winter nights are long.

But the reason that night was especially long was that most people around the world could not sleep.

—The World Hunter Federation will protect humanity!

Michael Silbert.

The declaration of a hero who had proven himself over several decades once again set fire to the hearts of the public, just as it had three days earlier.

People rushed into the streets and shouted cheers. Colorful fireworks shot up throughout the cities, and countless people sang songs as they marched through the streets.

All they had needed was a little hope.

Hope that someone would protect them and their loved ones from that monster. The hope that humanity would win again this time, just as it had in the past.

And Michael Silbert’s declaration washed away the fear that had stained their hearts over the past three days, spreading across every corner of the world.

> **Nigerian Civil War Ends!** “We only wanted to get the answers we were looking for.”
>
> **In Congo, protesters marching toward the presidential palace stop in their tracks.**
>
> **French President:** “The protesters have dispersed. The peace we have now was possible because there was a hero who gave the UN an answer.”

Strictly speaking, all of this had begun with a single word from Michael Silbert, but the public saw him differently.

Michael did everything. He’s a true hero.

└ That’s right. If he hadn’t stepped forward, when would the World Hunter Federation have been reestablished? It would’ve taken at least a month.

└ Fuck. A month? If it were up to those UN bastards, they would’ve dragged it out for a year. By then, I’d already be dead, and so would my family.

└ What the hell are the other Hunters doing? Why did Michael have to solve everything by himself?

└ Commercial appearances.

└ Calm down, everyone. The other Hunters are doing their best, too. It’s fine to praise Michael, but don’t criticize them for that.

└ You sound just like my mother. Is your name Masa?

└ Honestly, watching this unfold left me a little disappointed. Especially when it comes to Sky and Jin.

└ Hmm. I agree.

└ What the hell are those two doing in a situation like this? Everyone around me, myself included, loves them, but… it was hard to understand. Especially Jin—he even cursed at Michael three days ago.

└ I read that Jin is showing symptoms of PTSD. You have to cut him some slack for that much.

└ Fine. I understand. Then what about Sky?

└ Even the President of the United States is probably wondering about that. He hasn’t shown up in far too long.

└ I know one thing about him. He saved my parents.

└ Right, we all know that. But where is he, and what is he doing now?

└ You’ll find out soon, so shut your fucking mouth. The inaugural ceremony is tomorrow. Are you whining like a little brat because you can’t wait even one more day?

Hope. Joy. Questions. Anticipation.

Those countless emotions mixed and merged as the inaugural ceremony of the World Hunter Federation drew closer by the second, and prominent Hunters and Guild Masters from countries all over the world boarded private planes bound for Korea.

Of course, I was one of them.
## Chapter artifact 773

# Chapter 773

It was good to have somewhere to return to. Even better if there were people waiting for me there.

“Team Leader Choi! Taekyung!”

After several hours of flying, we arrived at Incheon Airport. From far away, a hairy giant came thundering toward us with both arms spread wide.

Whump!

The air caught in my throat.

Even while being subjected to a body choke disguised as a hug, Team Leader Choi and I patted Im Kkeokjeong on the shoulder as he sobbed.

Just because it felt like we should.

“Why are you crying? Have you hit menopause already?”

“You’ve been okay—waaah! You’re not hurt anywhere—waaaah!”

“We’re fine. Please calm down.”

“I was so worried, so worried that—sniff!”

Judging by his appearance alone, even the Green Forest Alliance Leader would have to step aside for him. But when it came to sensitivity, no one could compare.

You could say his outside and inside were two entirely different people.

And from over Im Kkeokjeong’s shoulder came a voice as clear and direct as the impression its owner gave.

“You should say *we* were worried, not *I*. What does that make me when you put it like that?”

Song Song stopped walking and carefully looked Team Leader Choi and me up and down.

“Hmm. You both look better than I expected.”

I asked in return,

“Are you sure? At this rate, I’ll be suffocated in five minutes.”

“That’ll be in five minutes. You look fine right now.”

“You don’t see how bloodshot my eyes are? I haven’t slept properly in three days.”

“Why? You look much better than you did on TV a few days ago.”

Song Song added,

“Your eyes looked completely out of it back then. Like you were about to drop dead.”

“…And now?”

“Who knows? You look like you’ll die in about a hundred years.”

I couldn’t think of anything to say, so I just grinned.

Just as Song Song had said, my body was exhausted, but my mind was clearer than it had been a few days ago—by an incomparable margin.

Mine, and Team Leader Choi’s.

“What happened with the matter I asked you to handle?”

At Team Leader Choi’s question, Song Song lowered her voice.

“I delivered your instructions properly—to both the Peace and Ares Guilds. Once I narrowed the list down, there weren’t even ten people. But the ones I chose are all staunch loyalists.”

“Is there any chance the information leaked?”

“I selected only the people among the two Guilds’ senior members whom we could trust without question. Their families are all staying in Korea, too.”

“Well done. From this point on, I’ll issue the instructions myself, so please focus on maintaining secrecy, Miss Song.”

Song Song nodded, then cautiously opened her mouth.

“But is it really Michael Silbert…?”

“Shh.”

As though he had never been crying, Im Kkeokjeong cut her off with a perfectly composed face. He whispered so quietly that only we could hear.

“He’s coming.”

He was right.

Several limousines smoothly crossed the deserted runway and came to a stop in front of us. Baek Hanseong, the President, stepped out of one of them. In the short time since we had last seen him, he seemed to have aged by about ten years.

“I welcome you both back home.”

His voice was as worn out as his face.

* * *

A weekday afternoon.

The airport would normally have been packed with people, but the interior was quiet. No, the situation outside was not much different.

Through the limousine window, we saw police officers and soldiers everywhere we looked. Here and there, people in black suits wearing earpieces caught our eyes.

The Blue House badges on their chests were visible, of course.

“It’s nice and quiet.”

“As you requested, we dismissed everyone in advance for security reasons.”

Baek Hanseong continued as he threw away the red ginseng juice he had finished drinking.

“Of course, it was also the obvious thing to do considering that terrorist.”

The terrorist he was referring to was The Prophet.

Baek Hanseong added that only a few hours earlier, enormous numbers of reporters and well-wishers had surrounded the area. Then he muttered,

“This may not be something I should say as President, but lately, everyone seems to have lost their minds. The atmosphere is becoming far too extreme.”

I agreed with him, and at the same time, I understood them.

People who lacked the power to protect themselves had no choice but to become extreme in the face of a crisis.

They trembled in fear as though humanity would perish tomorrow, then turned blindly fanatical at the word *hope*.

“…That’s what he was aiming for.”

“Pardon?”

“Nothing. I was just talking to myself.”

Baek Hanseong seemed to sense something in my thoughtless mutter and wore a complicated expression, but I silently turned my gaze toward the window.

It was true that he had helped us considerably so far. And considering what would happen in the future, he might be able to help us even more.

But the reason I couldn’t tell Baek Hanseong everything was not that I didn’t trust him. It was that I didn’t trust the circumstances surrounding him.

*There are plenty of ways.*

Michael Silbert’s eyes and ears were everywhere.

There could be a mole among Baek Hanseong’s closest advisers, and there was every chance he was being watched.

The moment anyone was confronted with an unbelievable truth, they were bound to be shaken.

Being an experienced politician did not mean he could hide every emotion. If the enemy noticed something because of that, the situation would become even more disadvantageous.

*And we can’t rule out the possibility that the clue we found isn’t the truth.*

I could read the same thought in Team Leader Choi’s eyes when our gazes naturally met.

He, too, had given instructions only to the smallest handful of the most trustworthy senior members of the Peace and Ares Guilds.

Team Leader Choi’s instructions had been delivered in an extremely covert manner, and even those instructions had nothing to do with the truth we had uncovered.

They were merely a safeguard against the worst-case scenario—a safeguard for use before the grenade’s pin was pulled, or to stop the effects of the explosion from spreading.

But at present, there was nothing we could be certain of.

With less than twenty-four hours remaining before the inaugural ceremony, everyone’s fate would be decided by how it ended.

Michael Silbert and me.

Beyond the simple concept of enemies and allies, the direction in which this world would move from here on out.

Vroooom.

In contrast to my tangled thoughts, the limousine carrying us sped smoothly down the wide-open road, and Baek Hanseong brought us up to date on several matters.

The current international situation. The decision to designate the National Assembly as the location of the inaugural ceremony. The list of participants decided so far.

He even told us how my mother and Hayeon were doing under ironclad protection.

“Your family is very worried after hearing the news. If you wish, we can go see them right now…”

I understood the meaning contained in his trailing words and shook my head.

“No. I plan to visit them after the inaugural ceremony.”

“Are you sure that will be all right?”

“Of course.”

They were the family I missed and longed to see more than anyone else in the world, but I couldn’t meet them in my current state.

No, I shouldn’t meet them.

I was afraid that seeing my family would make me lose my composure.

Once everything was resolved, I wanted to face my mother and Hayeon with a peaceful mind. I wanted to rest in their warm embrace.

*…If that’s possible.*

That one thought, which I couldn’t bring myself to add aloud, lingered on the tip of my tongue before scattering.

Then Baek Hanseong suddenly asked, as though he had just remembered something,

“But where is the other person?”

“Ah.”

“I’m fairly certain he was on the list of people entering the country… Has something happened?”

I hesitated for a moment, then met Team Leader Choi’s eyes. With a bitter smile, I answered,

“He’ll be late. Something came up.”

It was a lie.

The Skeleton King was with us right now.

He was simply maintaining an endless silence within a mysterious space no one else could see or sense.

Even at this very moment.

*How long are you going to stay holed up in there?*

But this time, too, there was no answer.

* * *

That day, the attention of the entire world was focused on a small peninsula in East Asia.

There were no variety shows full of laughter and chatter on television. Countless news and current-affairs channels, along with internet communities, were burning with the first inaugural ceremony of the World Hunter Federation, which was now right before them.

Who’s coming to the inaugural ceremony?

└ No idea. They flat-out said they wouldn’t release the list in the first place because of the terrorist threat. They cleared out the airport, too.

└ I heard they aren’t broadcasting it live, either. They’ll record it, though, so won’t we find out only after it’s over?

└ Why not make it public? If they’re worried about terrorism, they should hold a video conference like they did with the UN.

└ Fact) They participated in person even during the Great Cataclysm.

└ It means they’re declaring that they won’t back down no matter what happens. Until now, it was everyone fighting separately, but now that the Federation is being established, The Prophet is fucked.

└ But Cheon Taemin is obviously the most likely representative, right?

└ Yeah. Who else would do it if not Lord Taemin?

└ Michael Silbert.

└ Jin Taekyung.

└ I like Lord Fuck, but he’s definitely outmatched by Michael Silbert. Michael’s got seniority, and his recent moves have been insane.

└ What does that have to do with anything? It’s obviously Cheon Taemin.

└ That’s true.

└ Maybe it’s because Cheon Taemin hasn’t shown up in so long, but I’m getting chills. Anyone else?

└ Then turn on the boiler.

The conversation over who would attend the inaugural ceremony continued without end. Who would gather in one place, and whom they would choose as their representative.

And as time flowed slowly onward, guests who had crossed thousands, even tens of thousands, of kilometers to reach the peninsula began arriving.

“There will be a brief identity-verification procedure.”

With neatly styled brown hair and subtly green eyes, a young man who looked as though he had just stepped out of a fairy tale spoke in a dignified voice.

“I am Felix Alexander Louis, Duke of Cambridge, Earl of Strathearn, Baron Carrickfergus, Knight of the Order of the Garter, and Knight of the Order of the Chain.”

“Pardon?”

“They are merely empty titles, so feel free to address me casually.”

“Ah, understood. Then, Mr. Felix…”

“Feel free to call me His Highness Prince Felix Alexander Louis. Feel free.”

“…Yes.”

Just as Prince Felix finished the brief identity-verification procedure through the scanner, a large shadow fell over his head.

“It’s been a while, Felix. Or should I call you His Highness?”

At the familiar face looking down at him from far above, Prince Felix seemed about to frown, but then relaxed his expression.

Had it been anyone else, he would have shouted at them. But the person in front of him was one of the few people whose rudeness he could tolerate to a certain degree.

“Mr. Johnson.”

Magic Johnson gave a slight smile.

“Did you just arrive?”

“I did.”

“Faye Chen will be here soon, too. The comrades who fought together in China will all be gathered in one place.”

“That is so. But who is the gentleman behind you?”

“He’s with me. Though he isn’t a gentleman, of course.”

It was his first time meeting him in person, but Prince Felix quickly recognized the identity of the middle-aged man who had come with Magic Johnson.

He was as huge as Magic Johnson, dressed as though he had just stepped out of the American frontier era, and had a cigar clamped between his lips.

“…Chuck Hagel.”

Chuck Hagel, who had been puffing away at his cigar in front of a no-smoking sign, answered,

“Did you call me, Prince?”

At his irritable tone, Magic Johnson subtly stepped forward.

“Since we’ve run into each other, how about a drink? With Faye Chen, too.”

Prince Felix stared at the two men for a moment, then shook his head.

“I have no interest.”

“What a shame.”

“See you tomorrow. Both of you.”

“Sure. Then we’ll do that.”

It was an ordinary conversation, no different from usual.

Prince Felix gave a casual nod, then immediately walked away with his attendants.

He arrived at the lodging assigned to him under tight security, unpacked his luggage, and went to bed early in preparation for the inaugural ceremony the next day.

No. That was how it appeared to everyone else.

But…

Click.

When the locked door opened and the lights came on, Prince Felix—having secretly slipped out of his lodging—saw the figures waiting for him in the darkness, and the young man seated at their center.

“It’s been a while, Your Highness.”

Felix let out a quiet laugh.

Choi Minwoo, Magic Johnson, Chuck Hagel, and Faye Chen laughed along with him.

Their private night, known to no one else, was growing deeper.
## Chapter artifact 774

# Chapter 774

Back when I was a rookie Hunter, I used to cry sometimes.

No—if I’m being honest, pretty often.

Looking back now, I suppose all of it was just growing pains. But that was how it was back then.

It was only natural. At the time, I was a newly minted adult still wet behind the ears, and the Hunter training camp was literally nothing more than a training camp.

What had my first real mission been like?

No matter how hard I tried to remember, the memory remained hazy as fog.

Not because it had passed its expiration date, but because I had half-lost my mind the moment the battle began.

Of course, a few fragments had remained clear.

The backs of the tanks collapsing beneath the monsters’ overwhelming numbers. The thick stench of blood and the foul odor of creatures that did not belong to this world.

The weight of the spear that had felt heavier than ever, and my sweat-soaked grip around it…

That was all.

At the moment of impact, everything around me had grown distant. When I opened my eyes again, the world was a sea of blood.

And the Team Leader, who had been waiting for me to wake up with a cigarette between his lips, had immediately said this:

“You. Rookie.”

“Y-Yes.”

“You fucking bastard.”

“Excuse me?”

“I almost died saving your ass. Did my wife put you up to it? Tell you to kill me and split the insurance payout with her?”

“N-No.”

“You fought pretty well for someone who’d lost his mind, but if you pull that shit again, you’re going to die. Seriously.”

“…I’m sorry.”

“By the way, what’s your name?”

“Jin Taekyung. Jin Taekyung, sir.”

“What year were you born?”

“2020.”

“Holy shit. People were born in 2000?”

The Team Leader had glared at me while puffing furiously on his cigarette. Only then did he tell me his name.

“I’m Hong Cheonsu.”

“Oh. Yes, sir.”

“From now on, when we’re off duty, calling me uncle would be a little weird. Call me hyung instead. Cheonsu hyung.”

“Yes, Cheonsu hyung.”

“This kid doesn’t even know how to refuse politely. And we’re still inside the Gate, you little shit.”

I didn’t know it at the time.

I didn’t know that I would share thick and thin like brothers with that Team Leader who looked so foul-tempered.

I didn’t know that, only a few years later, he would sacrifice himself in my place.

“You did good. Here’s your payout.”

Six 50,000-won bills, after taxes and the Guild’s fee had been deducted.

I took the payment for risking my life that day and returned to my goshiwon.[^1]

When I opened the door, the room—less than four pyeong—smelled of mold. A family photograph sat on a table with a broken corner.

And I cried.

At first, I only sobbed quietly. But before long, I buried my face between my knees and wailed like a little child.

If someone hadn’t opened the locked door, I might have kept the entire goshiwon awake all night.

“Hey, new guy. Sorry for barging in without permission. I’m the manager here, but I kept getting complaints, so I had no choice but to use the master key—”

The manager stared at my tear-streaked face, let his voice trail off, scratched his greasy hair, and closed the door.

I thought that the manager, who looked like some middle-aged man, would never come back.

At least, not until I saw him again a little later, carrying soju and a bag of ramen in his hands.

“Want a drink? Oh, wait. You’re not a minor… obviously. Look at the size of you. Whew.”

Memories from nearly ten years ago.

As time passed, I changed. My fear of monsters and the loneliness I felt being separated from my family gradually faded.

No.

I became numb to them.

Like a hamster placed on a wheel, I simply ran and ran.

Even if I couldn’t move forward, it was better than stopping. There were things I could protect only by keeping that wheel turning.

Family.

Friends.

Companions.

By then, I couldn’t stop anymore.

The tiny hamster wheel inside the cage that had confined me had, at some point, transformed into the enormous wheel of fate. And the word *duty* I carried in my heart had grown increasingly clear—and increasingly heavy.

Maybe that was why.

Maybe that was why I had been able to look into that fading memory, if only in a dream.

Maybe that was why my cheeks had been wet when I opened my eyes to someone shaking me awake.

“…Gyeong. Mr. Jin Taekyung.”

I blinked. At last, my blurry vision came into focus.

The familiar face looking down at me with concern showed no noticeable change in expression. Perhaps because of that, even the smallest emotion stood out all the more.

“Are you all right?”

I rubbed the dampness from the corners of my eyes and answered.

“I don’t know.”

“Were you having a bad dream?”

“I couldn’t say.”

I sat up, my voice hoarse.

Through the gap between the curtains hanging by the window, I could see the dark landscape outside. The clock showed that it had only just passed noon.

“I don’t know whether it was a nightmare or a good dream. I don’t know either.”

Team Leader Choi watched me in silence before speaking in a calm voice.

“Don’t dwell on it. It was only a dream.”

He was right. A dream was only a dream. People were the ones who determined whether something would bring good or bad fortune—and that was my role today.

No.

Our role.

“I haven’t fully woken up yet, so let me ask you something. Was what happened last night also a dream?”

“Last night?”

“Yes. A lot of familiar faces appeared. At the end, I even saw a British prince dressed as a hotel bellboy.”

Only then did a faint smile appear at the corners of Team Leader Choi’s mouth.

“How strange. I had the same dream.”

“Oh, you did? Personally, I thought it was a pretty nice dream.”

“I thought so, too.”

Naturally, that part had not been a dream.

The conversation that had begun in secret had continued until deep into the night, and I had collapsed into sleep beneath the weight of the exhaustion I had accumulated over the past few days.

Perhaps thanks to that, my mind was clear and my body felt light.

Almost unnaturally so.

*Of course, there are a few flaws.*

I focused on the faint pain deep within my body.

The effects of **Broken Body**, which had yet to be healed, were not merely represented as numbers on the System. Like a parasite clinging to its host, they were eating away at part of my strength.

*Can I do it? Even in this condition?*

A single question flashed through my mind.

But I soon shook my head.

This was not a matter of whether I could do it or not.

I had to do it.

For everyone—including me and my people.

“What about the preparations?”

Team Leader Choi answered without hesitation.

“Everything is ready.”

The conviction in his voice was unmistakable—the attitude of someone who had prepared everything he possibly could.

But I asked again.

Not Team Leader Choi, but another person crouching somewhere out of sight.

“What about you?”

Once again, there was no answer.

Even though he had clearly seen and heard everything happening here, he chose silence once more.

As though he were someone trying to sever every last shred of affection between us. As though he were a traveler who had finished preparing to leave.

But…

I had no intention of letting him go.

Especially not for some fucking reason like this.

“Let’s go.”

I left the room in a calm voice.

Team Leader Choi followed immediately, and the Hunters from the Peace and Ares Guilds filled the hallway behind us, trailing after us like a dragon’s tail.

It was time to set the enormous wheel in motion.

* * *

The sky was gray that day.

Dark clouds had spread across the capital region under cover of dawn, spilling a light drizzle, and the air against my skin was chilly.

But to the people, the weather was irrelevant.

They had hope that the clouds would soon scatter and sunlight would shine through.

No.

Perhaps *conviction* was a more accurate word than hope.

The historic inaugural ceremony of the new World Hunter Federation.

That was the sunlight everyone had been waiting for—the alliance of superhumans that would save them from the second Great War that was about to descend upon them, or perhaps had already begun.

The heroes of the past, present, and future would gather in one place and be reborn as Hunters in the truest sense of the word.

They would become humanity’s sword and shield, clearing away those dark clouds and protecting the world from the monsters surging in like waves.

Today.

Here.

*A new history begins.*

Swish.

Michael Silbert ran his fingertips across the table.

The enormous round table had three hundred seats, and its surface was covered in marks left by sharp weapons.

*Records left behind by heroes.*

He still remembered it clearly.

On the day the unprecedented alliance known as the World Hunter Federation was born, Michael Silbert had stood alongside them in that glorious moment.

Beside those who were now dead, he had shouted until his blood ran hot. They had drawn their weapons and pointed them at the sky, then driven their swords into the enormous round table and sworn to become humanity’s sword and shield.

*Yes. Right here.*

It was an unforgettable memory.

Michael Silbert gently stroked the chair where he had once sat.

It carried every mark left by the years. It was rough and creaked beneath his touch, but even that stirred a strange emotion within him.

But that was all.

Michael Silbert merely looked down at the object that held his memories of the past. He did not sit in it or lean against it.

At some point, his gaze had left the chair and turned toward the center of the round table.

The only empty space.

There was no chair there, nor any platform. Isolated by the three hundred seats, it almost seemed as desolate as an uninhabited island.

But in the past, neither Michael Silbert nor anyone else had thought of it that way.

There had always been one person who filled that space.

The strongest and brightest of them all. The hero among heroes, whom even those who envied him had no choice but to regard with awe and fear.

*Sky.*

Michael Silbert suddenly raised his head and looked around.

The First National Assembly Hall, which had since become a World Heritage site.

Stained glass created just after the war ended, depicting the course of humanity’s victory in the Great Cataclysm, glittered on every side.

Monsters and humans locked in fierce battle. Blood flowing like rivers, and corpses piled up in every direction…

His gaze passed over the traces of the old heroes who had etched their names into history with their dazzling accomplishments—heroes who, unfortunately, were now mostly dead.

Then it came to rest on one place.

The highest point within those glorious records.

The two figures carved into the ceiling.

*My, my. You’re still looking down at me from up there.*

Michael Silbert let out a quiet laugh.

The savior who had driven a sword into the heart of Asmodeus, the Demon King who had cast humanity into a pit of flames, was looking down at him.

As though warning him never to forget his existence.

As though he might descend at any moment and pass divine judgment like a god.

But…

*Not anymore, Sky.*

Michael Silbert smiled gently.

In his youth, he had been neither particularly strong nor particularly weak compared to the other heroes.

Now, he had returned as a powerhouse no one could deny.

*But what about you?*

Cheon Taemin—the man Michael had revered, feared, and been forced to keep his head down to avoid drawing attention from—was gone.

All he could do now was remain as a record in this place and watch Michael, who would soon ascend the throne.

That was all the savior of humanity could do.

“I’ll fill the place where you once stood.”

And the moment those words left his mouth in a voice brimming with joy—

Grrrnnng.

The tightly closed door opened, and a voice seeped through the gap along with the light.

“What a load of bullshit. What a load of bullshit.”

[^1]: A *goshiwon* is a very small, inexpensive room-for-rent housing arrangement, often used by students and people with limited means.

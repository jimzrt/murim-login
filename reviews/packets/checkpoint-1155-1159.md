# Checkpoint Review — 1155–1159

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

# Chapters 1155–1159

## Plot

As Morgoth’s forces advance and more countries surrender, public fear grows. A doctor argues that humanity still has a 5.2 percent chance of victory; after a commentator calls for Jin Taekyung and Sky to make a noble sacrifice, the doctor shoots him on live television. The Skeleton King and Chuck Hagel worry that Jin may willingly give himself up, and Hagel believes Morgoth will break his promise.

At the Pentagon, Jin visits the unconscious Cheon Taemin and reveals his suspicions about Taemin’s identity and Asmodeus. Choi Minwoo admits that Jin’s allies have secretly confined him to stop him facing Morgoth alone. Jin breaks the chamber’s protective magic and orders the World Hunter Federation to mobilize for Moscow, while intending to go alone. Soon after, Code Name Blue—Jin’s identity—is reported to have escaped through Area 52, though the escapee is only someone who looks like him. The group finds Hagel alone.

The Skeleton King has taken Jin’s appearance through absorption and reaches Morgoth’s palace, intending to sacrifice himself in Jin’s form. Morgoth reflects on his own unexplained summoning by Asmodeus, then welcomes the arriving hero. The Skeleton King refuses Morgoth’s offer to become his Guardian and attacks with the Hero’s Sword. Morgoth recognizes his absorption abilities and infers he is a Doppelganger; unharmed by the attack, Morgoth launches black magical blades at him.

## Continuity

- Morgoth’s three-day deadline and demand for Cheon Taemin and Jin Taekyung as tribute remain in effect. Russia has surrendered; Morgoth promised to leave its current government in place and require disarmament.
- Cheon Taemin remains unconscious in a recovery capsule in a hidden Pentagon chamber. Jin believes Taemin was the Martial God and The Helper, and suspects Asmodeus may not have been completely erased; neither suspicion is confirmed.
- Jin ordered the World Hunter Federation to mobilize for Moscow but intended to confront Morgoth alone. His allies tried to keep him in the Pentagon chamber; Chuck Hagel and the Skeleton King were not told of their plan.
- Someone who looks like Jin escaped through Area 52. Their identity remains unknown.
- The Skeleton King is fighting Morgoth while disguised as Jin. He absorbed power and some abilities from the Arch Lich, Leviathan, and Behemoth. He wields the Hero’s Sword despite being undead; Morgoth cannot explain how.
- The Skeleton King can hear the dead spirits and considers them his people. He suspects he may once have been human but has no memories; he sometimes experiences déjà vu.
- Morgoth was summoned by Asmodeus from beyond distant stars and space, but does not know why. He says he is not devoted to Asmodeus.
- Morgoth’s attack on the Skeleton King is unresolved.

## Translation Decisions

- Keep the Skeleton King distinct from Jin: he has borrowed Jin’s appearance; Jin is not established as present at Morgoth’s palace.
- Use “Hero’s Sword” for 영웅의 검 and “Guardian” for 가디언 when referring to the role Morgoth offers.
- Render 魔力 as “magical power,” distinct from mana, and 九泉 as “Nine Springs.”
- Retain “Code Name Blue,” “Doppelganger,” “Silver Mountains,” “Archduke of the Demon Realm,” and “Answer the call” as established renderings.

## Durable state

{
  "active_continuity": [
    "Morgoth’s three-day deadline and demand for Cheon Taemin and Jin Taekyung as tribute remain in effect.",
    "Cheon Taemin remains unconscious in a recovery capsule in a hidden Pentagon chamber.",
    "Jin believes Cheon Taemin was the Martial God and The Helper, and suspects Asmodeus was not completely erased; these identities and suspicions are unconfirmed.",
    "The World Hunter Federation was ordered to mobilize for Moscow against Morgoth and his monsters; Jin intended to go alone.",
    "The Skeleton King has reached Morgoth’s palace disguised as Jin Taekyung and is fighting Morgoth after refusing to become his Guardian.",
    "The Skeleton King absorbed power and some abilities from the Arch Lich, Leviathan, and Behemoth; Morgoth inferred he had encountered a Doppelganger.",
    "The Skeleton King wields the Hero’s Sword, an Ego Sword; Morgoth cannot explain how an undead can use it.",
    "Morgoth’s magical attack is now directed at the Skeleton King; the outcome is unresolved.",
    "The Skeleton King can hear the dead spirits and regards them as his people; he suspects he may once have been human, but has no memories and sometimes experiences déjà vu.",
    "Morgoth was summoned by Asmodeus from beyond distant stars and space, but does not know why; he says he is not devoted to Asmodeus."
  ],
  "continuity_sources": [
    1158,
    1159
  ],
  "open_questions": [
    "Were Cheon Taemin, the Martial God, and The Helper the same person?",
    "Was Asmodeus completely erased?",
    "Who escaped through Area 52 in Jin’s likeness?",
    "What will happen when Morgoth’s three-day deadline expires?",
    "Can the Skeleton King survive Morgoth’s magical attack, and how can he wield the Hero’s Sword?"
  ],
  "safe_through": 1159,
  "temporary_decisions": [],
  "version": 1
}

## Reading copies

## Chapter artifact 1155

# Chapter 1155

“Russia has officially declared its surrender. General Vasily Gerasimov, current Chief of the General Staff of the Russian Armed Forces and acting president appointed in the immediate aftermath of the Moscow catastrophe, has…”

Beep.

“Eastern European countries, particularly Ukraine and Belarus, which suffered severe damage in the aftermath of yesterday’s Moscow catastrophe, are mobilizing all available forces and deploying them along their borders…”

Beep.

“We now bring you an update on the current disaster. Over the past eleven days, the world has seen an average of more than four Monster Waves and around fifty cases of Gate mutations every day.”

“That’s truly horrifying news. Amy, what about the magical power distribution?”

“I’m afraid it’s bad news, Steve. Today’s magical power distribution rose by 2.8 points.”

“What?”

“Yes. A full 2.8 points. If you’re having trouble judging what that figure means, please take a close look at this graphic.”

“Here, it says the increase was 5.0 points per day. So what’s the problem, you ask? For reference, this graph shows the changes in magical power distribution at the beginning of the Great Cataclysm.”

“In other words, we’ve caught up to more than half of the magical power levels from the Great Cataclysm. In the Middle East, where Monster Waves and Gate mutations have been occurring in particularly high numbers, it’s no exaggeration to say that a second Great Cataclysm has begun.”

“And on top of that, the situation around Moscow is already… I’m sure everyone knows. There’s only one thing I can say.”

“May God be with you.”

Beep.

“Breaking news. Morgoth has accepted Russia’s surrender. Starting at 16:30 South Standard Time, the Russian Federation will disarm completely and, like the more than twenty countries that surrendered before it, retain its current system of government.”

“Meanwhile, a large number of Hunter groups opposed to this decision have reportedly engaged monsters in battles throughout Russia…”

Beep.

“…I agree with part of what you’re saying. Our situation is extremely difficult right now.”

“Should we understand that to mean humanity ought to surrender?”

“Not at all. I’m simply speaking on the basis of statistical evidence.”

“But according to what you said earlier, Doctor, there’s no chance of humanity defeating Morgoth, is there?”

“At this point, I’m beginning to wonder if your ears are attached to your anus. As I’ve said several times now, it’s exactly 5.2 percent.”

“That’s an embarrassingly low probability. I’m sure our viewers are thinking the same thing.”

“Yes, I won’t deny the odds are low. But remember this clearly: compared with when the Great Cataclysm first began, that figure is dramatically higher.”

“I know. According to that excellent paper that even won you a Nobel Prize, the figure was 0.2 percent.”

“Congratulations. Unlike your ears, your eyes seem to be in the right place.”

“Thank you. But I can’t help pointing out that the 0.2 percent in your paper applied only to the period before Sky appeared.”

“True. But even Sky—”

“—had less than a 20 percent chance of winning right up until the final battle with the Demon King Asmodeus. Yes, I know. But unlike then, humanity has another option now, doesn’t it?”

“You!”

“It’s a reality too appalling to say aloud, but that doesn’t mean we can keep ignoring it forever. Before it’s too late, we need to face the problem right in front of us. Don’t you agree?”

“……”

“Thirty years ago, we had no options. We could only resist with everything we had. But Morgoth is offering peace now, and the countries that surrendered to him really are keeping their governments and calming their people.”

“……Morgoth is a monster. A fucking monster. Do you really not understand what that cunning bastard wants?”

“I know exactly what people want. Peace. A chance to protect the lives of the people they love.”

“Bullshit. Listen, young man, cut the nonsense. You’re nothing but a despicable coward. You’re hypnotizing yourself into thinking you speak for all of humanity while arguing that we should offer up a living sacrifice. And not just anyone—two heroes who’ve done more for us than anyone else.”

“Sky and Jin are heroes who’ll be remembered throughout human history. I’m grateful for their sacrifices, too.”

“If that’s true, then shut your damn mouth and go home right now. Hug your family, one by one. Then go to your study and take out the pistol you’ve hidden there. No need to bother writing a will. Everyone watching this broadcast, myself included, knows why you need to die.”

“My, how rude. I’m simply saying that I expect those two to make a noble sacrifice of their own accord, as great heroes would, for the sake of billions of people—”

“Fine. Then I have no choice.”

“What?”

“Go to hell, you son of a bitch.”

Bang! Bang-bang!

“Aaah!”

“Fuck! Healer! Get a healer in here, now!”

“Doctor, calm down and put the gun down! This is a warn—”

BEEEEEP!

“We apologize for the unfortunate incident during our live broadcast. We will do everything we can to resolve the situation—”

Beep.

At last, silence settled over the room. The Skeleton King stared without a word at the holographic TV, now giving off only a dim glow. Then he spoke.

“Humans.”

The word dripped with unconcealed disgust. Chuck Hagel, who had been staring at the whiskey bottle on the table, answered him.

“As a human, I have to say, that’s a weird thing to listen to.”

“Why don’t you try arguing against it, then?”

“I’m not going to. He wasn’t wrong. Especially that last guy. He deserved to get shot.”

The Skeleton King nodded.

Even he had to admit that the old doctor—one of the foremost scholars on the Great Cataclysm and magical power—had handled the situation remarkably well.

The man looked to be in his nineties and, far from being Awakened, seemed to need a shot of stimulants just to move. But America’s venerable martial art of gun-fu had no age limit.

“Do you think he survived?”

“He wasn’t hit in the head, so probably.”

“Pity.”

“I agree completely. But it’s better for that guy to stay alive. If he died there, it could actually hurt public opinion.”

“……Fair enough.”

In the silence that followed, the Skeleton King replayed the scenes he’d seen on TV.

Anxiety and fear boiling over everywhere.

The magical power distribution soaring toward the levels of the Great Cataclysm—and the nonsense now being broadcast openly across the world.

Things were happening everywhere that the Skeleton King simply couldn’t understand.

“You human, steeped in alcohol and tobacco. May I ask you something?”

“I quit drinking and smoking a few hours ago, but go ahead.”

“What is the essence of humanity?”

“That’s a difficult question to answer. Philosophy isn’t really my field.”

“I already know you’re not particularly intelligent, so don’t worry.”

“……Fine.”

Chuck Hagel, who’d been glaring at the Skeleton King, shrugged.

“All of it.”

“All of it?”

“Yeah. Everything you’ve seen and felt while you’ve been with us. That’s what I think, anyway.”

“Humans are stupid enough to make me want to crack open their skulls and examine their brains, and so greedy and cowardly it’s hard to believe. That’s their essence?”

“I wish I could deny it, but that’s part of it, too. But that’s not all you’ve seen, is it?”

Of course it wasn’t.

If all the Skeleton King had ever seen were those ugly sides of humanity, he never would have lived among them in human form.

He liked humans.

He’d always felt that he was different from ordinary monsters. And ever since he’d met a human in the dark forest inside a Gate, he’d stayed with them.

But…

“Still, this… This shouldn’t be possible.”

“Listen, my bony friend. There’s nothing in this world that’s impossible.”

Chuck Hagel ran his fingers over the whiskey bottle, still unopened after several hours, as if testing the limits of his own patience. Then he added:

“Things that should never happen are just happening anyway.”

“Then…”

“Right. More people will start agreeing with that damn ‘noble sacrifice’ the guy who just got shot was talking about. Humanity’s running out of time, but we still have a choice.”

“Even if humans have evil in them, they’d offer up the heroes who risked their lives fighting for them as sacrifices?”

“Offer them up? What are you talking about?”

“……?”

“I said ‘sacrifice.’ That’s what they really want. To look away without getting their hands dirty or having to hear anyone blame them. To make the people being sacrificed feel like they have no choice but to choose it themselves.”

“……!”

“The biggest problem is that Jin is exactly the kind of person who’d do it.”

For a moment, the Skeleton King bit down on his lip without realizing it.

That was right.

Jin Taekyung was that kind of person.

He was always scolding and teasing him, but he carried a heavier burden than anyone else in the world.

And that was why an even greater unease came over him.

If the world wanted him dead, Jin Taekyung was exactly the sort of person who would sacrifice himself.

“That’s ridiculous. Even if that treacherous human, Jin Taekyung, sacrificed himself alongside Sky, how could we be sure Morgoth would keep his promise?”

“Humans see what they want to see and believe what they want to believe. Morgoth knows that better than anyone.”

It was true.

As the news had just reported, Morgoth had kept his promise.

He’d maintained the governments of the more than twenty countries that had already declared their surrender, Russia among them, and completely restrained the monsters from killing anyone.

And that had given people hope.

Hope that Morgoth was different from the Demon King Asmodeus.

Hope that, even if they couldn’t enjoy the freedom they’d had before, they could still save countless lives.

“But the chance that Morgoth will kill those two and break his promise…”

“Is overwhelmingly high. There’s no question about it. At least, we know that with absolute certainty. But do you think people, half-crazed with fear, are going to think that way?”

Chuck Hagel continued, his voice growing rougher.

“By the time those bastards realize what they’ve done, it’ll be too late. The only Hunter who can fight Morgoth right now will be inside that bastard’s stomach.”

The instant those words of tightly coiled anger rang out, a thought suddenly flashed through the Skeleton King’s mind.
## Chapter artifact 1156

# Chapter 1156

At the very moment the Skeleton King thought of something during his conversation with Chuck Hagel, the subject of their conversation stood alone in the deepest, most secret part of the Pentagon, a place with the highest security.

Or perhaps “stood alone” wasn’t quite right.

Strictly speaking, he wasn’t “alone.”

“I should have come to see you more often, but things came up, and I’m late.”

Jin Taekyung spoke out of the blue and slowly looked around at the vast white space, bright as though hundreds of lights had been switched on, and so empty it felt almost hollow.

“I heard you moved not long ago. I just didn’t expect it to be somewhere like this.”

That was right. He really hadn’t expected it. So when he first set foot inside, he couldn’t help being surprised.

It was that similar.

Similar to that unknown space he called the Inventory, where he’d had an unexpected encounter not long ago.

“Just a coincidence, I’m sure. Probably.”

It had to be. The massive Grand Mage who had painstakingly designed this secret space for a single person wouldn’t even know the Inventory existed, let alone what it looked like.

But…

“Honestly, I don’t know anything anymore. Not even exactly what I know, or what’s true and what’s false.”

At some point, everything he’d taken for granted had begun to fall apart. Faced with a reality brushing against the incomprehensible, reason had grown hazy, and instinct had filled the void.

An awkward instinct, closer to a delusion—one even Jin Taekyung himself could hardly understand.

And the being who could be called the beginning and end of all this was reflected in his eyes at that very moment.

“Are you listening? Can you see me?”

Jin Taekyung lowered his head and looked down.

At the oval recovery capsule, linked to countless Magic Formations and machines.

Within that place, a coffin prepared for the living, lay an old man sunk in a deep sleep no one could wake him from.

“If so, please answer me.”

Of course, Jin Taekyung knew. No matter how long he asked and waited, no answer would come.

Even so, he had to ask.

“Are you the person I think you are?”

The greatest hero humanity had ever produced.

His real name was Cheon Taemin. His titles were Slayer and Sky.

And…

“The Martial God.”

Jin Taekyung let out the breath he’d been holding.

Through the translucent membrane fogged by his warm breath, he stared at Cheon Taemin’s peaceful sleeping face.

“I could feel it. The person I met there, back then… was you. I’m sure of it.”

Crackle!

His voice had grown louder without him noticing, echoing through the space. His hand, tensing on its own, struck the countless protective spells surrounding the capsule. But Jin Taekyung paid no mind to the pain in his skin.

He needed an answer to the half-formed conviction he’d reached only recently.

He needed to confirm that Cheon Taemin and the old man called The Helper were the same person, to learn that he too had been a Player like himself, and to find out how things had come to this.

And more than anything…

“Why—why won’t you wake up?”

No matter how hard he tried to suppress it, he needed somewhere to release the anger that kept churning in his chest.

“……Why?”

Why did someone like me, so far beneath you, have to bear such a heavy burden?

At that moment—

Hiss.

Along with the words he couldn’t bring himself to finish, Jin Taekyung took his hand off the capsule.

Then he turned and blurted out, “What, wasn’t it one visitor at a time?”

The reason he’d stopped speaking earlier wasn’t just that his emotions had been threatening to overwhelm him.

The second visitor, who had just arrived, answered him.

“Well, as far as I know, there’s no such rule. And even if there were, family should be an exception.”

“Wow. When you put it like that, I’ve got nothing to say.”

“For the record, I just got here.”

“They say a guilty conscience needs no accuser. Who said anything?”

His expression and tone were as playful as ever, so different from the person he’d been moments earlier.

Team Leader Choi, Choi Minwoo, watched Jin Taekyung for a moment, then shrugged.

“I should’ve knocked. Not that you would’ve heard me, with the barrier magic.”

“It’s not like you had to go that far.”

“I suddenly thought of my grandfather and went looking for Mr. Johnson. I heard you’d already come here with him. Sorry if I intruded.”

“Don’t be. If anything, I’m the one who interrupted you.”

Jin Taekyung smiled and waved a hand as he started walking.

“May I ask why you came to see my grandfather?”

Jin Taekyung paused for a moment, then gave a short laugh.

“What, worried something might happen?”

There was only one thing to worry about in a situation like this.

Jin Taekyung going to the Dragon Lair alone with Cheon Taemin.

Of course, Cheon Taemin had been unconscious for a long time, and nobody in the Pentagon wanted that to happen. If it did, it would effectively be Jin Taekyung acting on his own.

But unlike the joking question Jin Taekyung had tossed out, Choi Minwoo’s reply came in a low, steady voice.

“Yes.”

“……!”

“To be honest, I’m very worried.”

Before Jin Taekyung could answer, eyes widening, Choi Minwoo added calmly, “I’m worried that you, Mr. Jin Taekyung, might make the stupid choice of fighting Morgoth alone.”

“……”

“Please answer me. You can deny it if you want.”

Jin Taekyung stared at Choi Minwoo in silence, then spoke.

“Fine. Let me make this perfectly clear. I would never do that.”

“I see.”

“Yeah. So, that settles it, right?”

“No.”

“What? Why not?”

“Because I don’t believe you at all.”

“……!”

“Anyone who knows you well would feel the same. Spend enough time around you, and it becomes obvious how recklessly and foolishly you choose to act.”

Choi Minwoo stepped closer and looked at his grandfather sleeping inside the recovery capsule.

“My maternal grandfather must have been the same. The two of you are so alike.”

“Alike?”

“Yes. That’s given me a little personal comfort. Very recently, too.”

“What do you mean…?”

“Even after you came back from the Middle East, you haven’t gone to see your family. Even though you’re staying right here in the Pentagon.”

Family.

At that short word, Jin Taekyung’s eyes trembled.

That was right. His mother and younger sister—his family by blood, more precious to him than anything in the world—had been under the Pentagon’s protection for quite some time.

But he hadn’t gone to see them once.

No, he couldn’t see them.

If he did, the invisible pillar barely holding him up would collapse.

And if he crumbled now, he wouldn’t be able to summon even the smallest shred of courage.

“You’ve also refused to meet with the other Guild members. I’m sure it’s for the same reason.”

Over the years, he’d made connections with countless Hunters, but only two people could still be called Guild members by Jin Taekyung and Choi Minwoo.

Song Song and Im Kkeokjeong.

And Jin Taekyung had avoided them, too.

The path he had to walk was a deadly one, riddled with countless dangers.

Death came for everyone, but it didn’t come at the same speed.

So what would happen if they joined the coming great battle—not S-rank Hunters, not even Supreme Peak masters?

*They’d die. Without a doubt.*

This was a massive gamble with the lives of billions of people at stake, not just Jin Taekyung’s. In a world without the Three Saints or the Fire King, he couldn’t bear that immense weight alone.

So he ran.

From his family. From his friends.

He’d fled from everyone around him and come here.

He wanted, if only for a moment, to face Cheon Taemin again—the only person who could understand him, the answer and key to everything.

And at the next words that drifted into his ears, Jin Taekyung suddenly understood.

“Watching you, Mr. Jin Taekyung, finally made me understand how my grandfather felt when he never came to see his only grandson.”

Something he hadn’t noticed until now.

“Maybe I’m just looking for a reason to believe that. But… I’m going to think of it that way now. That he had no choice but to keep me at a distance because of some danger only he could sense.”

The real meaning in that voice, touched with a bitter laugh—a meaning even Choi Minwoo himself hadn’t realized.

*Some danger only he could sense?*

That couldn’t be. There had been no danger left for humanity at the time.

The Demon King Asmodeus, once so powerful, had been reduced to dust and vanished without even leaving a body. The monster legions that had stained the Five Oceans and Six Continents with blood had become nothing more than prey.

And yet, as soon as peace arrived, the hero who had achieved that great feat had isolated himself from the world.

He’d kept everyone at a distance.

No one was an exception.

Not even his closest companions, practically sworn brothers, or the daughter he’d cherished above all else.

Even when that daughter died in an accident along with her husband, he’d left his young grandson in Butler Kim’s care instead of raising him himself.

Then, one day, without warning, he lost consciousness.

For more than a decade.

*……Were you that afraid, too?*

With those words swallowed on the tip of his tongue, Jin Taekyung gazed at Cheon Taemin, his eyes sinking into darkness.

He’d been right.

He still had no definite proof or testimony, but what Choi Minwoo had just said made him realize it once again.

Cheon Taemin and the Martial God had been the same person from the very beginning.

The shadow of that old hero, sleeping as if dead, stretched across two worlds.

*He knew. He knew it wasn’t over yet. That Asmodeus hadn’t been completely erased.*

There was still so much he hadn’t uncovered, so much he wanted to ask.

But this was enough.

At least now, it was clear what choice he had to make.

Step.

Jin Taekyung turned without hesitation and started walking.

He’d taken only a few steps when he noticed one tiny but important change and stopped.

The door.

There was no door.

More precisely, the only exit from this secret space, created with advanced magic, had vanished without a trace.

“Team Leader.”

At his quiet call, he turned his head. Choi Minwoo stood there, his expression unwavering.

“I’m sorry.”

The brief, calm apology was enough for Jin Taekyung to understand the whole situation.

“Was this your plan from the beginning?”

“As I said earlier, we know exactly what kind of person you are, Mr. Jin Taekyung.”

“We?”

“Of course, this wasn’t a decision I made on my own. Most of them, including Mr. Johnson and me, have already agreed to the plan.”

“Most of them? That means someone must’ve opposed this ridiculous plan.”

“No. No one did. We didn’t tell the people who might have caused trouble from the start, in case they became an unexpected variable. We’ve also made every other preparation we can.”

Thinking of Chuck Hagel and the Skeleton King, who by now knew nothing about this, Choi Minwoo continued in a composed tone.

“So… for the time we have left, you’ll stay here with me, Mr. Jin Taekyung.”

The plan, involving so many people, had only one goal.

Use every means at their disposal to keep Jin Taekyung—their only hope—here until the three days Morgoth had given the world were up.

Fortunately, the secret space Jin Taekyung had found was perfectly suited to carry out the plan.

Countless barrier spells had been installed to keep Cheon Taemin safe.

Even so, there was one variable left: Jin Taekyung himself.

The savior of the new age.

The world’s greatest and strongest Hunter, successor to Cheon Taemin, whom no one else could replace.

That was exactly why they couldn’t let him throw his life away, and Choi Minwoo hadn’t forgotten to take one final measure to stop him.

“No matter how strong you are, Mr. Jin Taekyung, you won’t be able to get out of here.”

“Is that so?”

As Jin Taekyung calmly reached into the air, a silver spear that hadn’t been visible until then appeared in his grasp.

Whoosh.

Dark blue flames surged along the White Flame spearhead.

A refined fire, carrying heat beyond comparison with the last time Choi Minwoo had seen it.

But Choi Minwoo didn’t waver in the slightest.

“Now that I think about it, there’s one thing I didn’t mention.”

The final measure he’d prepared for this plan hadn’t been meant to counter Jin Taekyung’s strength in the first place.

“If you try to forcibly break the barrier spells installed in this space, the resulting damage could bring down the entire Pentagon.”

At least, that was what he thought—

Until he heard Jin Taekyung’s answer.

“You really think so?”

Grgrgrk.

As the space warped beneath the unbearable heat, Jin Taekyung’s quiet voice echoed through it like a distant refrain.

“I think differently.”

“……!”

At the instant Choi Minwoo’s eyes widened—

Slice.

Along a seam only one person could see, the massive wave of mana binding and sustaining hundreds of spells split in two.
## Chapter artifact 1157

# Chapter 1157

When the spearhead, wreathed in dark blue flames, rose high enough to pierce the ceiling, Choi Minwoo wasn’t the only one whose eyes went wide.

“……!”

There wasn’t even time to utter a single curse.

The massive Grand Mage, watching the scene unfold in the secret space he’d designed himself, looked on in shock at Jin Taekyung’s completely unexpected move.

At the same time, he was seized by the feeling that even the hair he didn’t have was standing on end.

*No way. Surely not.*

Magic Johnson swallowed hard.

Why was he so tense?

Simple.

If the magic was forcibly broken, the backlash would leave the caster—himself—battered and broken before it ever shook the Pentagon.

No. Maybe…

*I could die.*

To a mage, mana was another sense beyond the five, as much a part of the body as flesh and bone.

That was why when a spell cast with a mage’s own mana was forcibly dispelled, the mage was bound to suffer a more serious blow than anyone else.

Magic Johnson knew this better than anyone. The only reason he’d done something as insane as packing hundreds of security and barrier spells into the space was that he trusted Jin Taekyung.

He trusted that the Jin Taekyung he knew would never hurt him.

But at that very moment—

Whoosh!

The spearhead swept down without hesitation, mercilessly cutting through the last shred of trust left in his heart.

“Fuuuck—!”

Magic Johnson squeezed his eyes shut, finally letting out the curse he’d been holding back.

And as he felt the mana links connecting him to countless spells snap, he sensed the tremendous backlash that could bring him to the brink of death.

A warm breeze, carrying heat, blew from somewhere.

*……Wait. A breeze?*

There was no earthshaking roar to hear, no tremendous force rocking everything around him to feel.

Only energy, scattering faintly like sea fog meeting the sun.

The massive Grand Mage, unable to make sense of what was happening, twitched his eyelids for a moment, then gathered his courage and opened his eyes.

He stared blankly at the person standing in front of him, then spoke as if he’d made up his mind.

“Jin, be honest with me.”

Jin Taekyung straightened his spear and answered.

“Go ahead.”

“Did I die and go to heaven?”

“Whether you’re really dead is another matter, but heaven seems too bleak. We can’t even see the sky.”

“Everything’s all hazy. Like we’re at the top of Mount Everest.”

“It’s water vapor, not clouds.”

“Damn, you’re right. Then if it’s not heaven, is this a dream?”

“I hope not.”

“Why?”

“If I’m showing up even in your dreams, maybe I’m your type.”

“Oh, dear. I never thought that could be the reason.”

Magic Johnson murmured with a bitter smile.

“Okay. So this is how it ends.”

Jin Taekyung nodded calmly.

“Looks like it.”

“I’m truly sorry. I didn’t want things to go this far.”

“I understand. I’m not just saying that. I really do.”

“Thanks for saying that. I think our friend over there feels the same way.”

Right on cue, Choi Minwoo emerged through the thick steam and looked at Jin Taekyung with a complicated expression.

“You’ve gotten stronger. Even stronger than the last time I saw you.”

In Choi Minwoo’s memory, Jin Taekyung had always been strong.

Even on his first raid, when he’d gone along as no more than a porter rather than a combatant. And after that, too.

Jin Taekyung had always far surpassed Choi Minwoo’s expectations. Today was no different.

And that fact made Choi Minwoo ache.

“To be honest… I don’t know whether I should be happy that you’ve gotten stronger yet again, or sad.”

Choi Minwoo had often thought about it.

“With great power comes great responsibility.” Maybe that famous line from a now-classic superhero movie had been written for Jin Taekyung himself.

That was why, to Choi Minwoo, Jin Taekyung seemed every bit as strong as he was precarious.

The stronger he became, the more he tried to face ever greater threats on his own.

But Jin Taekyung’s reply was light and cheerful, nothing like Choi Minwoo’s words.

“Better to be happy, if you ask me.”

“Is that so?”

“That’s what I’d prefer. There’s always plenty to be sad about anyway.”

“If you died, what would I do then?”

“What kind of question is that?”

Jin Taekyung gave a short laugh and went on.

“Be sad when it happens. As much as you want.”

“……!”

“Let’s not worry about something that hasn’t even happened yet. Though I’m not really qualified to give you advice about that, Team Leader. I’m not good at it myself… But I’ve been through it, and I think that’s the right way.”

Choi Minwoo blinked.

He was different. Maybe it was only Choi Minwoo’s imagination, but Jin Taekyung had changed—noticeably.

Just ten minutes ago, Jin Taekyung had been forcing a smile. Now he was smiling with genuine ease.

Like someone who’d set down a heavy burden.

And only Jin Taekyung knew why.

*If I died…*

Death.

Jin Taekyung turned those two sticky, dark words over in his mind.

Of course death was always frightening. There hadn’t been a day, or a moment, when it hadn’t frightened him.

But only today had he realized it clearly.

What he truly feared wasn’t death itself, but what would happen after he died.

The danger the people left behind would face.

*But this is enough.*

Jin Taekyung didn’t bother turning around, but his five senses were already focused on the person he’d left far behind him.

Cheon Taemin.

Another Player—a person he’d once thought could never exist.

*Even if I really do die, maybe then…*

Jin Taekyung swallowed the rest of the words lingering on the tip of his tongue.

Then he looked squarely at the two men who were close friends and reliable comrades.

“As the Alliance Leader of the World Hunter Federation, I’m issuing a full mobilization order, effective immediately. Destination: Moscow. Objective: the annihilation of Morgoth and the monsters under his command.”

“……!”

“……!”

The two men’s eyes widened at the unexpected announcement. Jin Taekyung added in a firm voice:

“However, no one is to do anything rash until I give further orders. Unless I’m in a situation where I can’t issue orders.”

“Right. You’ve thought this through. We’ll all fight together—wait, ‘unless you’re in a situation where you can’t issue orders’?”

Magic Johnson belatedly realized something was wrong, but before he could finish, Jin Taekyung spoke again.

“I mean if my position becomes vacant.”

Neither man could fail to understand what he meant. Choi Minwoo bit his lip, and Magic Johnson let out a low groan.

“Damn it, Jin.”

“No matter what you say, I won’t change my mind. I’m going to Morgoth. Right now, alone.”

“……Are you sure that’s the best option? You’re really going to bet your life on a crazy gamble with less than a one-percent chance of winning?”

“Yes.”

There wasn’t a trace of hesitation or doubt in his voice or eyes.

For a moment, Magic Johnson was at a loss for words.

But then, suddenly, he remembered someone from decades ago. When everyone had been thrown into utter confusion, that person alone had stepped forward and led the way.

A hero who had made himself a beacon and lit up the world.

*Sky.*

Yes. It was him.

And right now, standing before Magic Johnson was another Cheon Taemin.

No—Jin Taekyung.

“……Ha.”

A sigh slipped through Magic Johnson’s clenched teeth.

At last, he had to admit that, just as Jin Taekyung had said, nothing would change his mind. And he had to admit what their role was.

“Fine, Jin. Go on and tell us what your plan is. But first, I have to say this.”

The massive Grand Mage took a deep breath, then spoke to the savior of a new age.

“Whatever happens, don’t you dare die. If you don’t want me to beat you to death with my staff.”

Jin Taekyung let out a quiet laugh.

“I don’t plan to. I’d rather not die a second time.”

A little while later, just as the two men fell silent after hearing Jin Taekyung out—

Wheeeee!

A siren as piercing as the story they’d just heard shook the deep underground of the Pentagon where they were staying.

Along with it came the panicked voice of an operator, booming through the magical equipment.

“Code Red, Code Red!”

“Code Red?”

“It’s an emergency. The highest alert level. What happened all of a sudden?”

“Unauthorized use of magic detected!”

“Security forces, deploy immediately. Location: Area 52. I repeat, security forces are to deploy to Area 52 immediately!”

“Area 52… That’s where the transport Magic Formation is.”

“You mean the Warp magic?”

“Yeah. But access to the entire Pentagon has been forbidden for a week now. Is an inside collaborator we don’t know about trying to escape because they think they’re about to be found out?”

It wasn’t an unreasonable guess. Of those who had surrendered to Morgoth, most had bowed to him to survive, but there were others who were actively cooperating with him.

In Africa, rebel holdouts that hadn’t been completely rooted out in the previous incident were rampaging. In South America, drug cartels were running wild, more ferocious than the monsters.

So Magic Johnson’s guess was fairly reasonable.

At least, by ordinary standards.

“Emergency! Code Name Blue! Code Name Blue has escaped through Area 52!”

The operator’s shout, now so desperate he was almost panting, brought all three men to silence—but for slightly different reasons.

Jin Taekyung didn’t understand what those words meant at all.

The other two understood all too well.

In the end, the first to break the silence was Jin Taekyung, unable to endure their stares.

“Okay. I get that I’m an idiot, so cut it out and tell me what Code Name Blue is.”

Choi Minwoo blinked and replied.

“Uh, well. It’s only natural you wouldn’t know, Mr. Jin Taekyung.”

“Why?”

“Because it’s a secret from you.”

Magic Johnson looked back and forth between Jin Taekyung, who had no idea what was going on, and the magical equipment installed in a corner of the underground corridor.

“It’s you, Jin.”

“What? What does that mean out of nowhere—”

“Code Name Blue, the one they just mentioned. That’s you.”

“……What?”

It took Jin Taekyung a moment to understand what was going on.

“So someone’s saying I slipped out of the Pentagon without permission?”

“Well, if we’re being precise…”

Magic Johnson already had a good idea who would do something like that.

“Someone who looks like you.”

And the first person they ran into when they hurried to the surface was—

“Goddamn it. Where the hell were all of you, leaving me on my own in a situation like this?”

Chuck Hagel, who had somehow ended up all alone.
## Chapter artifact 1158

# Chapter 1158

It was a ruin.

A complete ruin. There was no need to add or subtract a single word.

But the man who had appeared in a sudden flash of light barely ten seconds ago saw it a little differently.

*A grave.*

That was the first thought that came to him.

He could feel it the moment he looked around—or even before he opened his eyes. The aura of death swallowing everything around him like a thick fog at dawn. The screams of countless vengeful spirits rising from every corner of this enormous grave, where not a ray of light could penetrate the clouds overhead.

“……I suppose so.”

The man muttered bitterly, then kicked off the ground and shot forward.

*Fwoooosh!*

Perhaps it was the magical power swirling in his wake as he streaked forward like an arrow. The spirits reacted to it, stopped screaming, and began following him one by one.

“Don’t follow me. I’m not your enemy.”

*Whoooom.*

Beyond the howl of the wind, the man heard the spirits’ answer and nodded.

“Fine. I’ll go there.”

*Whooom—*

“If that’s what you really want…… Fine, I’ll allow it. There’s no harm in keeping you company for a little while.”

If an ordinary person had seen this, they would surely have been surprised by two things.

First, by the man’s behavior, which made him look insane.

And second, by the fact that this madman was famous all over the world.

But the spirits were different. Just as the man could sense their presence and hear their voices, they could see him as he truly was.

They were certainly different kinds of beings, but they were linked by the word *death*.

“I know. It’s unfair. I’m sorry I couldn’t save you.”

The man continued, as if talking to himself.

“That’s impossible. You did nothing wrong. It was just a simple misfortune. Something that can happen to anyone.”

“You’re asking whether God or heaven really exists? Why?”

“……Your child, huh? I see. But don’t worry. A child that young would have gone to heaven. No—they definitely did.”

“I don’t know what God looks like. It was so long ago that my memory’s a little hazy.”

“You there. Take that back. I’m a great being, far beyond the likes of you. My memory’s just a little bad, that’s all.”

“Yeah, damn it. You’re right. I don’t remember a thing. But ever since I started traveling with a strange fellow, I sometimes get déjà vu. Like I’ve been through something similar several times before.”

“I’ve given it some serious thought, and I think I must have been human once, too. An incredibly noble and excellent human, just like I am now—damn it. Everyone, quiet down. I’m having an important conversation.”

“Oh, don’t cry. I wasn’t talking to you. How old are you? What about your parents?”

“……All right. I can’t promise, but if I find your parents, I’ll make sure you see them.”

The man continued forward, carrying on his conversation with the spirits.

A young man who had only just taken his first steps into adulthood. An old man who had accepted his own death and asked about the afterlife. Parents who had lost a child, and a child who had lost their parents.

The scenery changed in an instant, but the spirits never stopped whispering. They were indignant and furious at the death that had struck without warning, grieving even as they trembled with fear.

And the man never once turned away from their voices.

Because he was their king.

The only being with the right and duty to guide those who had lost everything in an instant and now wandered the Nine Springs—those who had become his people.

But perhaps the spirits weren’t the only ones finding comfort and peace in this strange conversation.

“Why did I come here? Hmm, that’s an excellent question. This is an epic tale that begins with the most handsome and excellent hero in the world.”

The man leaped over the ruins in his path and continued.

“The hero had many talents. He was incredibly strong and had a noble heart. But for all his abilities, he was surrounded by idiots and incompetents. Then one day, he learned that the biggest fool of them all had gotten himself into trouble.”

But the hero knew the surest way to help the fool. It was something only he could do.

Because he was a hero.

“While the hero was deep in thought, some ignorant bastard who was crazy about booze and cigarettes told him that people see what they want to see and believe what they want to believe. So the hero decided to borrow the fool’s appearance for a while.”

It hadn’t been all that difficult. As he’d said, the hero was unbelievably talented, and his greatest ability was “absorption.”

“Actually, I didn’t know I had that ability. No, neither did the hero. But when he tried it, it worked. It wasn’t nearly as good as the Doppelganger’s original ability, though.”

Was it because of his innate ability to grow stronger by absorbing the magical power of monsters that had been destroyed? Or was it because his magical power levels had already reached the point of going berserk?

Amazingly, the hero, who wasn’t human, had gained a new power he’d never discovered before. After traveling thousands of kilometers by way of several Warp Gates, he had made it here.

Of course, there had been some trouble along the way.

He’d threatened the mages who refused to activate the Warp Gate. Or he’d taken a selfie in his current appearance, posted it on social media, and deliberately spread the word far and wide.

But none of those little things mattered to the man.

The grand finale—the most important part of this story—was still to come.

“Most of you figured it out from the start, didn’t you? Yes, that’s right. I am that hero.”

*Fwoosh.*

In the sudden silence, the man blinked after making his solemn declaration.

“Why is everyone so quiet? You’d think you were dead. Oh, right. You are dead.”

“What? You didn’t see it coming? That’s impossible. The foreshadowing was perfect from the start. I said I was the most handsome and excellent man in the world—damn it. Forget it. You stupid humans.”

That was when the grumbling man suddenly stopped walking.

“……I’m already here.”

He murmured and looked at the scenery, now completely transformed.

As if someone had drawn a line dividing the world, a pitch-black landscape lay only a few steps ahead, starkly different from everything behind him.

*Whooom. Whoooooom—*

At the same time, the countless spirits surrounding him let out their screams.

Screams filled with a terror unlike anything they had shown before.

“Don’t be so afraid. Weak spirits like you would have a hard time entering that place anyway. Not that I was planning to take you with me in the first place.”

But the man was different.

The spirits writhed as if burned by fire, but he knew that the closer he got to that ominous, pitch-black landscape, the stronger he would become.

*In the end, only appearances can be faked.*

As the words echoed emptily in his mind, the man drew the sword tucked at his waist.

*Shing.*

Its blade was clear as untainted ice.

The man silently gazed at his reflection in it.

Or rather, at the face of the person who was probably chasing him as fast as he could somewhere out there.

“You’re a step too late this time, you wily human bastard.”

The man—the Skeleton King—snickered. Someone reflected in the blade snickered along with him.

“Yeah, keep smiling like that. Don’t scowl with that ugly face of yours.”

He meant it.

That fool—that Jin Taekyung—deserved to smile.

“Then, here I go.”

With a final farewell that would never reach him, the Skeleton King took a firm step forward.

Using the light spilling from his sword as a torch, he headed for the land of death, where magical power churned, and thought:

*Sacrifice, huh? This isn’t so bad.*

Even if he died, he wouldn’t regret it.

After he met his glorious end in the form of Jin Taekyung—not the Skeleton King or the Stone King—all of humanity would understand.

They would understand how foolish they had been to believe the monsters’ promise to stop the destruction and slaughter if they handed over Jin Taekyung.

And they would understand the only way to escape this catastrophe.

*Fwoooosh.*

The dense fog drifting over the pitch-black land swallowed his retreating figure.

* * *

Morgoth recalled an old saying he’d heard long ago: Sometimes, a certain kind of curiosity can shorten a person’s life.

He’d first heard it while living among humans, and it had fascinated him.

Unlike humans, the Dragon race couldn’t live long without curiosity. Morgoth himself was the perfect example.

He had always been curious.

Ever since he was no more than a Hatchling—or even before he broke out of his egg.

Perhaps that was why Morgoth had become a being unlike any other Dragon.

Nothing short of the very best could satisfy his curiosity.

Humans, of course, but also Dwarves, Elves, and all sorts of other races. Driven by nothing but curiosity, he had spent unfathomable stretches of time among them, learning from them and giving in turn, while also ruling over them.

No matter how often he changed his appearance or location, Morgoth was a born ruler.

His election as Dragon Lord before he had even lived a thousand years was proof of that.

The pride of his race and the king of the world.

He was more complete and absolute than anyone.

At least, he would have been, if not for the one curiosity he had never been able to satisfy.

*The Demon Realm.*

The home of all monsters. The land of demons, where poison, corpses, and death flowed in place of clear rivers.

His curiosity about the unknown deepened with every passing day, until Morgoth took his first step into that forbidden realm.

*Yes. That was where it all began.*

But why? Even after an extraordinarily long time had passed, the curiosity filling Morgoth’s heart had not faded.

And among his unanswered questions was one that, like the saying among humans, might truly shorten his life.

*Asmodeus, why did you choose me of all people?*

Morgoth possessed immeasurable knowledge and power, but he didn’t know why he had come to this world.

He had simply been summoned from beyond distant stars and space, and answered the call.

That made it all the harder to understand.

Unlike the others, he was not devoted to serving Demon King Asmodeus, nor did he intend to give his life for him.

*Besides, how could you, a being who doesn’t exist in this world, have prepared a stage like this?*

But Morgoth did not delve deeply into these questions.

No. To be precise, he had to put them aside for now.

The guest he had truly wanted to meet had just arrived at his palace.

“Come in, hero.”

Morgoth rose from his throne and welcomed his first guest with delight.
## Chapter artifact 1159

# Chapter 1159

Boom. Rumble, rumble.

As the iron doors opened with a heavy roar, the Skeleton King had a sudden thought.

If he’d really been human, he might have mistaken the sound for his own heartbeat.

But even without a heart, he could feel it clearly.

With every step he took, the distance narrowed—and with every iron door that opened in turn, the immeasurable magical power swelled.

At the end of it all, one being—the source of everything—waited for him.

“Come in, hero.”

The last door opened with a low voice, and the Skeleton King swallowed involuntarily.

*This is…*

His eyes, which until now had held nothing but deep darkness, were filled with dazzling light.

Would this be what it looked like if someone brought a palace from the myths of old gods into the world?

The place spanned hundreds of meters in diameter. It was filled with antique furniture steeped in the passage of time and jewels of every color. Countless images were carved into the lofty ceiling and the walls surrounding him.

Beautiful.

No—not just beautiful. Astonishing.

Yet even before this blinding sight, the Skeleton King’s gaze fixed on just one thing.

A being more beautiful than anything else in this space could ever be, no matter how many times you added it all together or multiplied it—and possessing a power more terrifying than anything in the world.

“You seem to like the place. Good.”

The palace’s master smiled as he drifted gently down from the throne towering in the distance, as if he had spread invisible wings.

“I don’t need to introduce myself, do I?”

He certainly didn’t.

Not only the Skeleton King, but all of humanity around the world knew who he was.

“…Morgoth.”

The Skeleton King’s mutter came out like a groan. Morgoth smiled and nodded.

“So you do know me. Still, it wouldn’t hurt to formally exchange names, as is the custom in this world.”

The Skeleton King understood what he meant and replied, thinking once more of the one person who wasn’t here—and shouldn’t be.

“Jin Taekyung. Jin Taekyung.”

“I see. Jin Taekyung…”

Morgoth seemed to mull it over, then asked:

“I’ve heard it several times now, but it’s a very strange name. Does it have some special meaning?”

“Of course it does.”

The Skeleton King shrugged and added the answer that suited Jin Taekyung so perfectly, the real one might have mistaken him for a Doppelganger if he’d been here.

“It means ‘fuck you.’”

Morgoth stared at the Skeleton King, momentarily dumbfounded, then burst out laughing.

“Well, you got me. That’s pretty funny.”

“Get all your laughing out now. After you’ve taken a few hits in a minute, you won’t find it so funny.”

The Skeleton King made no effort to hide his hostility.

The moment he faced Morgoth, he’d understood.

A sneak attack meant to catch him off guard would never work against this opponent.

*How is this possible?*

He’d never felt so overwhelmed just by standing before someone.

To be precise, there had been one time: when he was called the Skeleton Warlord, he’d felt something similar while fighting Jin Taekyung. But the comparison was meaningless.

Just as the Jin Taekyung of then couldn’t be compared to the Jin Taekyung of now, the Skeleton King had grown at a terrifying pace, too.

In fact, if they were comparing nothing but growth rates, he might have even surpassed Jin Taekyung.

Since joining Jin Taekyung, he’d defeated one named monster after another, starting with the Arch Lich, and absorbed their vast magical power like nourishment.

He’d become so powerful that the title of king no longer seemed inadequate.

But…

*We’re on different levels.*

A cursed being: undead.

And, in contrast, a being born with the blessing of all creation: a Dragon.

The two facing each other were at eye level, but everything else about them was different. Their innate natures, and the size and depth of the power that came from them.

And yet, why?

The Skeleton King felt more at ease as he gripped his sword hilt.

Even with Morgoth watching his every move, the motion came naturally, as if he were simply folding his arms.

“Now, are you thinking of fighting me?”

“Why? Didn’t you expect this?”

“No, I did, from the moment you appeared alone. I only wanted to tell you it’s a poor choice.”

“There was never another choice.”

“Never another choice? I find it hard to understand why you think that.”

Morgoth tilted his head and continued.

“I’ve lived for a very long time, and yet you’re a fascinating being. I’ve always had a weakness for exceptional talent.”

“So you’re telling me to surrender?”

“Become my Guardian. You’ll have the honor of protecting the true king at his side, and gain even greater power and eternal life.”

“That’s a tremendous honor.”

“It’s also an entirely reasonable and peaceful solution. What do you say?”

The Skeleton King let out a hollow laugh and spoke.

“Jin Taekyung.”

“What?”

“I told you what it means earlier.”

At that moment—

*Shing.*

A silver blade, its edge cold as frost, finally emerged into the open.

“This is my answer.”

It was Jin Taekyung’s answer, too.

The Skeleton King knew him. He would have acted exactly this way.

Morgoth looked at him and muttered, almost to himself:

“How strange. I just can’t understand it.”

“What, are you that shocked I turned down your shitty offer?”

“I won’t deny that your foolish choice disappoints me. But that’s not what I find so hard to understand.”

*Rustle.*

Morgoth’s obsidian eyes moved slowly, taking in his opponent.

More precisely, the Skeleton King and the [Hero’s Sword] in his hand.

The next words that slipped between Morgoth’s lips were enough to send a shiver through the Skeleton King.

“How can an undead monster like you wield an Ego Sword like that?”

“……!”

“Oh, sorry if that offended you. It’s just a situation I can’t explain with what I know. Can you think of any reason?”

The Skeleton King didn’t answer.

No—he couldn’t.

He had to struggle just to steady himself after the shock that had struck through his whole body like a bolt of lightning.

*He knew. He knew who I was.*

Since when?

When he gave his name? Or when he drew a sword instead of the spear Jin Taekyung always used?

Or… from the moment he first set foot on the pitch-black ground in Morgoth’s territory, despite the spirits’ pleas for him not to?

*Damn it.*

The Skeleton King clenched his teeth.

Then, looking into the Black Dragon’s eyes, as if they could see through everything he was, he spoke.

“You were playing with me. From beginning to end.”

“Oh dear.”

Morgoth let out a soft sigh and continued.

“Don’t let a needless misunderstanding upset you. Everything I’ve said so far was sincere. You’re that special and fascinating. Even in the thousands of years I’ve lived, I’ve encountered few cases like this.”

“Shut your mouth.”

“How rude. But I’ll forgive you. My intelligence and curiosity won’t allow me to destroy something precious in a moment of rage like some inferior race.”

Morgoth wasn’t the least bit shaken.

If anything, he looked at the Skeleton King with even greater interest.

The eyes of the old, cunning Ancient Dragon glittered like those of a child heading to the hills to collect insects.

And all the while, a silver blade charged with powerful energy was swinging down at him.

*Fwoosh—CRASH!*

Fierce wind clawed at the space around them, and the power in the sword swallowed everything within a radius of a dozen or so meters.

It was a blow so savage that even the named monsters who’d once struck terror across the world would have faced death if it had hit them directly.

But before the roar even rang out, the Skeleton King knew.

His all-out attack hadn’t even hurt a single hair on his enemy’s head.

Rumble, rumble…

Beyond the enormous tremor shaking the space, Morgoth had already moved to the towering throne in the distance. He brought his hands together in a heartfelt round of applause.

“Impressive. Truly impressive. Such immense magical power—and there are so many different kinds.”

“You…”

“Oh, right. The Arch Lich, Leviathan, and Behemoth. You absorbed their magical power. But your current appearance doesn’t seem to have been created with magic… Have you ever met a being called a Doppelganger?”

For an instant, the Skeleton King felt his mind turn cold.

Found out.

Too quickly, and with such chilling accuracy.

Morgoth broke into a bright smile at the Skeleton King’s stiff expression.

“So that’s it. You can absorb not only a target’s magical power, but some of their abilities, too. What an astonishing ability. Now I understand how you, a mere undead—a Skeleton, at that—came to possess such power.”

“That mere undead might kill a Dragon here today.”

“A taunt?”

“No. I mean it. It’s a lesson I learned by watching a certain lunatic of a human.”

Morgoth nodded at the Skeleton King’s approach, the words spat out through clenched teeth.

“Yes, of course that could happen. Even the mighty Asmodeus was stopped by a mere human. But…”

Morgoth fixed his gaze on the Skeleton King and continued.

“Just as you learned a lesson through Jin Taekyung, I also realized the most important thing when I heard the news.”

*Goooom.*

Space warped.

Incredibly powerful, pure magical power became invisible blades, filling the space around them.

“His—Asmodeus’s—greatest mistake was arrogance.”

“……!”

“I don’t underestimate any of you.”

At the moment the Skeleton King’s eyes widened—

*Fwoooosh!*

A black flash, deeper and darker than the night sky, shot toward his entire body.

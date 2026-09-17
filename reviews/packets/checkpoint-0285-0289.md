# Checkpoint Review — 285–289

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

# Chapters 285–289

## Plot

Lee Jungryong withdraws with the mutilated Park Jihoon, revealing that his apparent concern was an act. He has Park Tae Seop’s long-standing obedience secured by an old debt, orders the Myeongdong Guild survivors incapacitated and witnesses’ memories altered, and assigns his prized Disciple, Go Jun, to monitor Jin Taekyung. Ares Guild conceals the confrontation and abandons Jihoon after minimal treatment.

Im Kkeokjeong survives after three days unconscious, with both arms reattached. He reunites with his family and chooses to remain with the Peace Guild after learning that the Black Hunter operation leads to Myeongdong Guild, Ares Guild, and Lee Jungryong. Lee visits the hospital and confronts Team Leader Choi and Butler Kim, exposing their shared history: Choi once served Ares, while Kim saved Lee during the Mapo Bridge collapse but now despises him. Lee also invokes Choi’s deceased mother, Soyeong, revealing that she was Cheon Taemin’s daughter and that Choi is Cheon Taemin’s maternal grandson.

Go Jun attacks Taekyung in the hospital but is defeated easily. Lee concludes that Taekyung has learned mana cultivation and possesses extensive combat experience, then orders heightened surveillance of the Peace Guild and Ares Guild’s own personnel. He privately recalls his complicated devotion to Cheon Taemin, whom he regards as an older brother despite their lack of blood relation.

Team Leader Choi offers to dissolve the Peace Guild to protect its members, but Taekyung rejects the proposal and promises to make the Guild strong enough to resist Ares. Choi, Butler Kim, Song Song, and Im Kkeokjeong all choose to remain. Song Song demands doubled pay and hazard compensation, while Im intends to return to Hunter work after recovering. Taekyung then discovers the Martial Arts Manual Creation Skill, which requires at least 300 sheets of A4 paper.

## Continuity

- Lee Jungryong’s concern for Park Jihoon was performative. He considers Taekyung unusually dangerous and ordered Go Jun to monitor him.
- Park Tae Seop has been bound to Lee Jungryong for roughly twenty years after receiving help during a financial crisis; he committed crimes for Lee in return.
- Lee’s forces used sleep magic, illusion magic, and planned memory alteration to conceal the Myeongdong Guild confrontation. Park Jihoon was ordered to receive minimal treatment and be abandoned; his eventual recovery is unknown.
- Go Jun, also called Team Leader Seok, is Lee Jungryong’s prized Disciple and right-hand man. Taekyung defeated him decisively, and Go Jun confirmed that Taekyung’s strength, speed, and combat experience exceed his own.
- Im Kkeokjeong regained consciousness after three days and had both arms reattached. He remains bandaged and must recover before returning to field work.
- Team Leader Choi previously worked for Ares Guild for several years, was sent overseas by Lee, and resigned the previous year. Lee has known him since childhood.
- Butler Kim saved Lee Jungryong during the collapse of Mapo Bridge eighteen years earlier and now deeply regrets doing so.
- Soyeong, Choi’s deceased mother, was Cheon Taemin’s daughter. Choi is therefore Cheon Taemin’s maternal grandson.
- Cheon Taemin is Ares Guild’s Guild Master, humanity’s greatest Hunter, and the Slayer who killed the Demon King.
- Lee Jungryong met Cheon Taemin at age thirty and regards him as an older brother despite their lack of blood relation; the history behind this relationship remains unresolved.
- Ares Guild officially has more than one hundred A-rank Hunters besides Lee Jungryong, countless mid- and low-rank Hunters, and further undisclosed forces.
- The Peace Guild’s remaining core members—Taekyung, Choi, Kim, Song Song, and Im Kkeokjeong—have chosen to remain together despite Ares Guild’s pressure.
- Taekyung’s mana cultivation method and its teacher or source remain unknown.
- Taekyung has discovered Martial Arts Manual Creation, but no manual has yet been created; the skill requires at least 300 sheets of A4 paper.

## Translation Decisions

- Retain **Ares Guild**, **Peace Guild**, **Myeongdong Guild**, **Black Hunter**, **Team Leader Seok**, **Go Jun**, **Disciple**, **Great Cataclysm**, and **Slayer**.
- Render **천태민** as **Cheon Taemin** and **소영** as **Soyeong**.
- Render **마왕** as **Demon King**.
- Render **비급제작** as **Martial Arts Manual Creation**.
- Render **A4 용지** as **A4 paper**.

## Durable state

{
  "active_continuity": [
    "Jin Taekyung, Team Leader Choi, Butler Kim, Song Song, and Im Kkeokjeong remain committed to the Peace Guild despite its coming conflict with Ares Guild.",
    "Taekyung intends to make the Peace Guild strong enough to confront Ares Guild rather than abandon it under pressure.",
    "Ares Guild officially has more than one hundred A-rank Hunters besides Lee Jungryong, countless mid- and low-rank Hunters, and additional undisclosed forces.",
    "Song Song remains with the Peace Guild after requesting double pay and hazard compensation.",
    "Im Kkeokjeong chooses to continue as a Hunter after recovering from his injuries, though his actual return to field work is not yet confirmed.",
    "Taekyung has discovered the Martial Arts Manual Creation Skill, which requires at least 300 sheets of A4 paper.",
    "Lee Jungryong regards Cheon Taemin as an older brother despite their lack of blood relation.",
    "Taekyung's mana cultivation method and the history behind Lee Jungryong's chosen-brother relationship with Cheon Taemin remain unknown."
  ],
  "continuity_sources": [
    289
  ],
  "open_questions": [
    "Who taught Jin Taekyung the mana cultivation method?",
    "What history led Lee Jungryong to regard the unrelated Cheon Taemin as his older brother?",
    "How extensive are Ares Guild's undisclosed forces beyond its officially registered Hunters?",
    "Will Im Kkeokjeong's reattached arms recover sufficiently for him to return to Hunter work?"
  ],
  "safe_through": 289,
  "temporary_decisions": [
    "Render 비급제작 as \"Martial Arts Manual Creation.\"",
    "Render A4 용지 as \"A4 paper.\""
  ],
  "version": 1
}

## Reading copies

## Chapter artifact 285

# Chapter 285

*How dare you touch my Disciple!*

*I only paid him back in kind. That settles the principal, so consult your Guild’s leadership about the remaining compound interest.*

*……You bastard.*

*I’ll take that as your acceptance.*

*I will never forget what happened today.*



That was the conversation I’d had only a few minutes ago.

Lee Jungryong had left after delivering those words, each one dripping with killing intent.

He had administered emergency treatment with the potion he carried, but Park Jihoon’s injuries were too deep to heal with a potion alone. His Disciple had ended up like that, so he must have been in a hurry to get him treated.

“Phew.”

Once the presence of Lee Jungryong, which I could still faintly sense in the distance, disappeared completely, a sigh of relief escaped me.

“Man, that was exhausting.”

The moment I let go of the tension I had been holding until the very end, all the strength drained from my body.

I was tired. My clash with Lee Jungryong had left me with a slight Internal Injury, but the mental exhaustion was even worse.

*I really caused one hell of a mess today.*

Today, I had made an S-rank Hunter recognized throughout the world and a colossal Guild my enemies.

It had been a precarious tightrope walk with a sheer, bottomless cliff as the stage.

Lee Jungryong and I had met at the very center of that tightrope, and in the end, it was the other side that backed down.

*He had no choice. I just targeted the exact point that mattered.*

People with a lot to lose were bound to fear danger.

If the tiger known as Lee Jungryong—or the tiger known as Ares Guild—were to fall, the mountain lord’s[^1] honor would hit the ground, and its carcass would become an excellent meal for the animals of the forest—in other words, its competitors.

*Of course, the cleanest way to settle things would have been to kill me and silence me, but…*

Lee Jungryong knew I wasn’t an easy opponent.

He had confirmed that he held the upper hand after a single clash, but that had still been enough for him to realize that the wolf in front of him was a fairly threatening opponent.

I wiped the blood from the corner of my mouth and thought.

*Three steps.*

Today, I had taken three steps back against Lee Jungryong.

But today’s three steps would soon become two, and before long, those two steps would narrow to one.

And after that…

*I’ll surpass you.*

I had never seen a documentary about a wolf beating a tiger one-on-one, the kind I had mentioned to Lee Jungryong.

But I possessed the potential to grow without end. Just like my epithet, the Hidden Dragon.

*When that time comes, both I and my Guild will be stronger than you ever imagined.*

What I had gained from this incident wasn’t merely revenge for Im Kkeokjeong. I had also obtained a golden opportunity to help the Peace Guild grow.

If the Peace Guild had been frightened and backed down when the Black Hunters first attacked, it would have remained just another mid-sized Guild. But because we had fought back, we had earned revenge and compensation. What happened next would depend on Team Leader Choi’s abilities.

*He’ll handle it well.*

A conversation I’d had with Team Leader Choi several hours earlier suddenly came to mind.



“What are you planning to do?”

“Hard to say. If my hunch is right, I might see red, and even I don’t know what I’ll do.”

“Are you thinking of storming Myeongdong Guild?”

“I can’t promise I’m not.”



Song Song had called me crazy after hearing that, while Butler Kim had only stared at me in silence.

But Team Leader Choi had been different.

What he said had gone far beyond anything I expected.



“Then go.”

“Excuse me?”

“Myeongdong Guild. Go there, smash the place up, and turn it upside down. Ah, I’m not telling you to collapse a building in the middle of Seoul and kill people. If you’re not careful, the prison will become the Guild house.”

“……I thought you were going to stop me.”

“I would have, if you weren’t Jin Taekyung. I would have racked my brain and looked for another way somehow.”

“Then why?”

“Jin Taekyung, you may look reckless at first glance, but you always move with the worst possible situation in mind. And you always bring back the best possible result.”

“Are you really sure this is all right?”

“I intend to make the Peace Guild the greatest Guild in the world. If we back down when one of our Guild members has been attacked, we can never become the best in the world.”

“Then you really want me to…”

“Do it. Whatever the result, I’ll take responsibility.”



Team Leader Choi’s final words seemed to ring vividly in my ears.



“I trust Jin Taekyung. Perhaps more than I trust myself.”



I had repaid the boundless trust he had placed in me.

I had given Park Jihoon more than Im Kkeokjeong had suffered, and I had tacitly secured apologies and compensation from enemies no one could dare approach.

*The greatest Guild in the world, huh?*

Remembering Team Leader Choi’s bold ambition, I let out a quiet laugh.

I took out my phone and made a call.

Someone answered before the phone had even had time to ring properly.

—Yes. This is Choi Minwoo.

Team Leader Choi. It was him.

“I have a lot to tell you. Where should I go?”

—Jin Taekyung! You’re alive!

“……?”

—I thought you were dead. Is this really Jin Taekyung?

“…….”

*You said you trusted me more than yourself, you son of a bitch…*



* * *



“Jihoon! Wake up!”

The master’s anguished cry for his young Disciple, accompanied by hurried footsteps.

Park Tae Seop, the Guild Master of Myeongdong Guild, followed closely behind Lee Jungryong and stared at his back with startled eyes.

*Did Lee Jungryong have this side to him?*

Park Tae Seop had watched Lee Jungryong for many years.

During the Great Cataclysm, he had simply thought of him as someone who was strangely difficult to approach.

But after the war ended, Ares Guild was established, and Lee Jungryong seized its real power, Park Tae Seop came to understand his true nature clearly.

He was as hard as steel, as secretive as a viper, and capable of doing things that would make other people shudder without hesitation.

That was the kind of man Lee Jungryong was in Park Tae Seop’s eyes—a person he never wanted to meet as either an enemy or an ally.

*So he was a human being after all.*

But the strange impression Park Tae Seop had felt vanished without a trace the moment they emerged from the long corridor and entered the hall.

“Welcome.”

“……!”

The speaker was a middle-aged man. His movements were as precise as a soldier’s. His extremely well-trained body could not be concealed even by the black suit he wore.

The same was true of the twenty men and women standing behind him like iron towers. An emblem symbolizing Ares Guild was fixed over each of their chests.

*I didn’t even sense their presence.*

That wasn’t the only thing that shocked Park Tae Seop.

Over the middle-aged man’s shoulder, he spotted roughly a hundred Myeongdong Guild members lying collapsed on the floor. His eyes widened.

“What is the meaning of this…?”

The middle-aged man answered in a dry voice.

“We merely put them to sleep with sleep magic. For now.”

*For now.*

It was a meaningful choice of words. They were only asleep under the power of magic at present, but it also meant they could remain asleep forever.

Park Tae Seop was just about to shout in fury when—

“Is there some problem?”

Lee Jungryong slowly turned around.

The moment Park Tae Seop saw his face, he realized that he had been profoundly mistaken.

*It had all been an act.*

There was no emotion on Lee Jungryong’s expression, and his eyes were sunk deep and cold. There was no trace of the hurried footsteps or anguished cries worrying over his Disciple’s safety.

An icy chill slowly crept up Park Tae Seop’s spine.

“Guild Master Park.”

There was a blade hidden in Lee Jungryong’s gentle voice. It was as though venom dripped from the viper’s tongue every time it moved.

“Was it about twenty years ago? One day, you came to me and abruptly dropped to your knees.”

“……!”

“Do you still remember?”

“……Of course.”

Park Tae Seop clenched his teeth.

How could he not remember? Nearly twenty years had passed, but the desperation he had felt back then remained buried deep in his bones.

A string of massive business failures, debts totaling an enormous sum, and the looks people gave him as though they were staring at a failure…

For Park Tae Seop, it had been a living hell more horrifying than the Great Cataclysm.

After being rejected countless times by the people around him, the person he had gone to was Lee Jungryong.

Lee Jungryong had gazed down at the kneeling Park Tae Seop before asking him a single question.



*If I help you, what can you do for me?*



Park Tae Seop’s answer had come without hesitation.



*I’ll do anything.*

*I like that.*



What would have happened if he had never said those words?

He had asked himself that question hundreds, even thousands of times over the past twenty years, but there was no point. He had already come too far to turn back.

There was no such thing as a favor without a price, and he had been forced to commit all kinds of crimes for Lee Jungryong.

When he came to his senses, all he could see was himself being dragged along with a leash around his neck.

“Whenever I look at you these days, Guild Master Park, I find myself thinking the same thing. The words you said when you came to me back then feel like an empty shell.”

“How could that be?”

“No. That’s simply how human beings are. Even when they receive a favor, they quickly forget their gratitude and do nothing but pile up complaints. Save a man who was about to freeze to death, and his attitude changes as soon as he warms himself by a campfire. What can you do? Ha ha.”

“…….”

Despite the corners of his mouth curling upward, Lee Jungryong’s eyes were as cold as ice.

When Park Tae Seop lowered his head with a hardened expression, Lee Jungryong continued in a gentler voice.

“I only said that so we could continue working well together in the future. Your Guild members will be safe as well, so don’t worry about anything. Isn’t that right, Team Leader Seok?”

The middle-aged man in charge of Lee Jungryong’s security, Team Leader Seok, answered in a flat voice.

“Of course.”

“Well, then, I should be going. I’ll see you again.”

Tap, tap.

Park Tae Seop stood rigidly in place and watched Lee Jungryong’s back as he walked away after patting him on the shoulder.



* * *



Team Leader Seok spoke inside the descending elevator.

“Shall I take care of him?”

“Who? Ah, Park Tae Seop.”

“Yes. His expression looked rather uneasy.”

“That man’s thoughts are written all over his face. He was obedient for the first few years, but once he got comfortable and well-fed, he started entertaining other ideas.”

“He knows too much. And he handled this incident so poorly that the fallout reached the Vice Guild Master.”

For the first time, emotion entered Team Leader Seok’s voice.

Anger.

Lee Jungryong confirmed the steadfast loyalty he held toward him and smiled faintly.

“Leave him for now. Besides, we’ve only just taken a taste, so of course it’s bland.”

“Excuse me?”

At that moment, the elevator doors opened with a ding.

Lee Jungryong continued speaking as he walked.

“I only gave things a little prod. I wanted to see what the response would be.”

“Then…?”

“You occasionally have a tendency to underestimate me. If I had made up my mind, would I have entrusted this work to such half-baked fools?”

Team Leader Seok let out a low exclamation.

“You anticipated all of this.”

“I’ve only taken a spoonful and tasted it. If it doesn’t seem right, I can add salt and pepper.”

“As expected of you, Vice Guild Master.”

At the admiring look in Team Leader Seok’s eyes, Lee Jungryong smiled gently.

But his thoughts were different. There was something he could not reveal even to Team Leader Seok, his right-hand man.

*Jin Taekyung. He’s no ordinary man.*

From the beginning, what had bothered Lee Jungryong was the Peace Guild, not Jin Taekyung.

Even if he had stepped in himself, he could not guarantee that something like this would not have happened. He was not the sort of person who used a butcher’s knife to kill a chicken.

It was certainly an efficient approach, but if an unexpected variable appeared, the plan would fall apart.

*So there was a wolf hiding among the chickens.*

Lee Jungryong rubbed his tingling wrist.

For a moment, he had felt tremendous heat and power radiating from the young man. It was far too strong to dismiss as some fresh-faced brat’s cute little display.

*He knew how to handle mana properly. A man who had been nothing more than an F-rank Hunter until recently—where on earth had he…?*

There was one possibility he could reasonably guess at.

After finishing his train of thought, Lee Jungryong said to Team Leader Seok,

“Keep a close eye on Jin Taekyung.”

“Don’t worry. If he becomes a problem, I’ll deal with him personally.”

Team Leader Seok had always been reliable. He was a born fighting prodigy and the best among the children Lee Jungryong had personally selected and taught, so there was no need to question his skill. Even Park Tae Seop, a top-ranking ranker, was no match for him.

But Lee Jungryong suddenly found himself wondering.

Was Team Leader Seok really superior to Jin Taekyung?

“Team Leader Seok. No, Go Jun.”

His form of address had changed from a title to a name.

Team Leader Seok was not the kind of person who would fail to understand what that meant. If he had lacked even that much awareness, he could never have become Lee Jungryong’s prized Disciple.

“Yes, Master.”

“Hmm. It’s nothing. I was entertaining a ridiculous thought for a moment.”

Lee Jungryong clicked his tongue softly and walked out through the main entrance.

Five men and women were waiting outside the building. They wore robes covered in elaborate patterns and carried staffs.

“We greet the Vice Guild Master.”

“Your outfits are certainly gaudy. Can’t you dress a little more ordinarily?”

“They’ll look ordinary. To everyone else.”

They were A-rank mages directly under Lee Jungryong.

Just as the oldest-looking mage had said, none of the hundreds of people hurrying along the sidewalk paid them any attention.

They did not even know that an incredible battle had taken place above their heads—one that had nearly brought down a high-rise building.

“This is why magic is so convenient.”

In a brute-force move, the mages had blanketed everything within a radius of roughly two hundred meters with an illusion spell. They could pull it off because they were A-rank mages of Ares Guild, which selected only the best.

They would maintain the illusion spell here until all the cleanup was finished.

“Yes. Use that convenient magic to handle things properly so no rumors come out of this. If anyone seems dangerous, use mental magic to tamper with their memories.”

“Yes, sir. Understood. But that man is badly injured.”

“Ah, him?”

Lee Jungryong glanced at Park Jihoon, who was being carried on the back of one of the security team’s Hunters, and tossed out a single sentence.

“Treat him just enough, then dump him somewhere.”

If he died, so be it. Even if he recovered, he would not be able to properly use even half of the skill he currently possessed.

Lee Jungryong had no hobby of collecting spent batteries. He already had countless batteries, and replacing one was all it took.

*Still, he proved useful at the end.*

Through Park Jihoon, Lee Jungryong had gotten a measure of Jin Taekyung’s ruthlessness.

Once blood had been drawn, he should have killed him. If Lee Jungryong himself had been in that position, he would have done so without fail.

*You couldn’t take that one step.*

What good was cutting off both arms and carving up his body? If the enemy was still breathing, it was not complete revenge. It was nothing more than venting one’s anger.

*That half measure will come back to poison you someday.*

Lee Jungryong let out a derisive chuckle and climbed into the car that was waiting for him.

[^1]: *San-gun* (山君), meaning “mountain lord,” is a traditional epithet for a tiger.
## Chapter artifact 286

# Chapter 286

In the early hours of that morning, a short post appeared on a popular forum frequently used by Hunters.

> Hyungs, I had a weird dream. Can someone interpret it for me?

I can’t reveal the specifics, but I’m a member of the Security Team of a major Guild with some clout. Anyway, that part isn’t important.

I was working like usual when I nodded off for a moment. But then Lord Fuck appeared in my dream.

My senior said some weird guy kept hanging around, so we went to catch him together. (He’s a traitor bastard. I think his real name is probably Yamamoto, but he’s hiding it.) And that guy turned out to be Lord Fuck.

But that’s all I can remember clearly. After that, my senior did yutori, and I did irasshaimase.

> **Best comment:** Before we interpret the dream, can someone translate this post? I have no idea what the hell this guy is talking about.
>
> └ Same.
>
> └ Forget everything else. What are “yutori” and “irasshaimase”? There’s no way to figure out the context.
>
> └ Why is his senior a traitor? Did he buy Heattech from Uniqlo?
>
> └ **Author:** Because he keeps using Japanese in this climate. He uses words like yutori and gensei all the time, too.
>
> └ But you said you did irasshaimase.
>
> └ **Author:** Yeah.
>
> └ What a crazy bastard. “Yeah,” my ass. LOL.
>
> └ I can practically smell the problem employee from here. Poor senior.
>
> └ **Author:** But when I told my senior about the dream, he said he’d had a similar one. Lord Fuck beat up a hundred of our Guild members and got into a one-on-one fight with Ares Guild’s Vice Guild Master.
>
> └ I want to beat the author’s ass.
>
> └ **Author:** I’m serious;;; Then he started yelling at me because his phone had disappeared;; He was probably pissed because it was the latest-model AdultPhone.[^1]

> Hello. I’m a practicing shaman. I can sense an unusual energy from your post. Could you tell me more about it?
>
> └ **Author:** Wow, are you really a shaman?
>
> └ No. I’m lying.
>
> └ **Author:** Wow. Are you a crazy bastard?

The post was deleted in less than ten minutes.

The people who had seen it didn’t pay much attention to one attention-seeking lunatic disappearing, and no one suspected that Ares Guild had been involved in the whole sequence of events.

Well, no one except me.

*They must have tampered with everyone’s memories using mental magic.*

It was an obvious criminal act, but it would have been even more ridiculous for people who raised Black Hunters to complain about something like that.

Judging by the comment about the AdultPhone disappearing, it seemed they had thoroughly checked everyone’s phones as well.

*That was decisive evidence.*

My personal cameraman had bolted outside the moment Park Tae Seop and Park Jihoon appeared, and had fallen straight into Ares Guild’s hands.

Well, I wasn’t all that disappointed. I had been searched before leaving the building anyway. They even checked my shared cloud folder before returning it.

They had also been considerate enough to add a warning.



“Just in case you’re hiding something, delete it now. It won’t be fun if you get caught keeping it hidden.”



I was already in a foul mood because they had discovered the porn I’d saved on my phone, and the guy’s tone had been obnoxious beyond belief.

If the situation hadn’t been what it was, I would have given him one good punch.

*I memorized your face, you square-headed bastard.*

He had an angular face and a crew cut. Since he had been in charge of cleaning up the situation, and everyone else had called him “Team Leader,” he seemed to be something like Lee Jungryong’s right-hand man.

The name Qi Sense had revealed was Go Jun. His skill had also played a part in my bothering to find out his name.

*That guy seemed to have learned something resembling martial arts, too.*

Once suspicion had taken root, I could see things more clearly than before.

The Ares Guild members Lee Jungryong had left behind were all extraordinary. Each one of them was skilled enough to steamroll two ordinary A-rank Hunters alone.

But the impression I had gotten from Go Jun was… honestly, it was enough to surprise even me.

The obnoxiousness in his tone came from confidence in his ability.

*How did he raise people like this?*

Could it really be martial arts? Or perhaps a martial art developed independently within Ares Guild. One question after another kept piling up.

That was when I was lost in thought.

“Mr. Lee! Patient Im Hyeokjun is conscious!”

I sprang to my feet at the nurse’s shout from the hallway outside.

Im Hyeokjun. Im Kkeokjeong’s real name, which was almost never used.

He had regained consciousness after three long days.



* * *



“Darling! Jun’s dad!”

“Daddy!”

I desperately held back the urge to throw open the hospital-room door. This was the family’s time.

The cries of the wife and children who had been reunited with their husband and father after three days of unconsciousness drifted through the gap beneath the door.

Only after a wave of wailing had swept through the room, and quite some time had passed, did our turn come.

“Oh, you’re all here?”

Damn it. My throat tightened at his very first words.

Im Kkeokjeong spread his arms with a bright smile, then scrunched up his nose.

“Ugh.”

“Your arm, be careful! Your arm!”

“I thought it would be fine, but it aches a little when I move it.”

“They reattached a severed arm. Did you think you’d be fine right away? Are you a person, or a transforming robot?”

Song Song scolded him as she chanted a healing spell. Im Kkeokjeong’s expression relaxed considerably, as though the pain had subsided.

“Thank you, Miss Song.”

“If you’re grateful, please be careful. Didn’t you hear the healer? You have to rest and avoid overexerting yourself for at least two weeks.”

“And thanks for saying that, too.”

“Uncle!”

“Oh, my ears nearly fell off.”

I never would have imagined how happy it would make me to see him laughing heartily like a bandit.

After bursting into the same boisterous laughter as before, Im Kkeokjeong turned to the others.

“Hyung Kim—no, Guild Master. Thank you so much. The kids’ mother told me how much you looked after me while I was unconscious.”

Butler Kim shook his head slightly.

“There’s no need to thank me. It was only natural. When one of our fellow Guild members suffers something like this, we have to step up.”

“I heard you spent quite a lot of money, too…”

A famous healer had been brought in to treat Im Kkeokjeong, and high-grade potions that casually cost hundreds of millions of won per bottle had been poured into him without restraint.

It may have been the same in the past, but this was a world where even a human life had a price. Who would do this much for a D-rank Hunter whose only thing to show for himself was his years of experience?

Butler Kim gave a low chuckle at Im Kkeokjeong’s voice, thick with emotion.

“If you really must thank someone, thank the one footing the bill. I’m just the figurehead, so leave me out of it.”

At those words, Im Kkeokjeong’s gaze slowly shifted toward the man footing the bill.

“Team Leader Choi.”

His voice was hot, as though it carried Scorching Yang Qi. Before Im Kkeokjeong could continue, Team Leader Choi cut him off.

“This wasn’t your fault, Mr. Im. It happened because our Guild was looked down on. I’m the one who failed to prevent this tragedy, and I’m the one who should be apologizing.”

“Team Leader Choi!”

Im Kkeokjeong was the sort of man who could make a hardened criminal look like a model prisoner simply by standing beside one, and now tears brimmed in his eyes.

When he stretched out his arms to hug him, Team Leader Choi flinched and stepped back.

“B-be careful with your arm.”

“It’s fine. I just want to hug you once.”

“…I’d like to pass that glorious opportunity on to the last person.”

It didn’t seem like much of an honor, but in the end, my turn came around.

“…”

“…”

Silence descended.

There was something I had really wanted to say to Im Kkeokjeong once he woke up, but when I finally stood face-to-face with him, my mouth clamped shut like a clam.

Im Kkeokjeong was the one who broke the silence first.

“What do you think?”

“About what?”

“My wife and kids. Pretty, right?”

His out-of-nowhere bragging about his family made me let out a quiet laugh.

“Yes. They are.”

“Your sister-in-law is quite the beauty.”

“I’ll give you that. Did you imprison or threaten her?”

“No tree survives ten chops. Remember that. I succeeded on the forty-seventh.”

“You just said no tree survives ten chops.”

“There are some trees that ten chops can’t even touch.”

“It’s a miracle you weren’t arrested.”

“You idiot. If I’d given up back then, do you think I could have gotten a beauty like that?”

Im Kkeokjeong’s wife had a puffy face from crying. She covered it with one hand and waved the other dismissively.

His two children, both still in elementary school, stared at me with bright, curious eyes as though they had never cried at all.

“Daddy, who is he?”

“Who is he? Who?”

Im Kkeokjeong pulled the clinging children into his arms and answered.

“He’s your uncle. Uncle Taekyung.”

“Uncle Taekyung?”

“Yeah. I’ve told you about him before, right? The handsome, strong uncle.”

So he had told his family about me.

A warm feeling spread from somewhere in my chest. The children’s eyes sparkled even more brightly as they looked at me.

Children were cute and beautiful by nature, but these sisters could have been child actors. So this was the victory of maternal genes.

“Wow! You’re Uncle Taekyung?”

“Nice ta meet you!”

A pleased smile formed on my face.

I patted both girls on the head and said to Im Kkeokjeong,

“They’re adorable. So innocent.”

“Obviously. Get married and have a daughter yourself. Then you’ll understand why people call men doting dads.”

I’d been nicknamed a doting dad in high school, too. Of course, I hadn’t had a daughter.

In any case, looking at this close-knit family of four made my heart ache with emotion.

Im Kkeokjeong raised his arm with stiff movements and hugged me. His hand, far weaker than before, patted my back.

Tap. Tap.

“Thank you. I’m always grateful.”

The moment I heard those words, I solidified a decision I had been carrying in my heart all along.

*I must not repeat the same mistake.*

I muttered the words inwardly and hugged Im Kkeokjeong tightly.

Today was the day a man returned to the side of his family and friends.



* * *



An hour later, only five Peace Guild members, including Im Kkeokjeong and me, remained in the hospital room.

Im Kkeokjeong’s wife wanted her husband to rest, but his resolve was firm.

“I almost left my beloved wife and kids behind. I need to hear it now. Every single thing that happened, without leaving anything out.”

The good-natured man who had always been softhearted and full of laughter had gained firm resolve and steel in his spine.

After finally hearing the entire story, Im Kkeokjeong’s face had hardened.

“It was Ares Guild?”

“Yes.”

“And the Lee Jungryong you mentioned really is that Lee Jungryong?”

“Absolutely.”

“…Hah.”

A groanlike sigh escaped him.

We had followed the tail called Black Hunter and found Myeongdong Guild. When we stepped on Myeongdong Guild’s torso, the head that emerged was Ares Guild.

The problem was that the head wasn’t an ordinary one.

“We followed a snake’s tail and found a dragon’s head.”

As he said that, he cast a sidelong glance at Team Leader Choi and Butler Kim. Both of them wore their usual calm expressions.

But I had definitely seen it.

Before Im Kkeokjeong regained consciousness, when they first heard the name Ares Guild, a storm had raged in the eyes of both men.

*There’s definitely something going on…*

I didn’t know the exact reason. Song Song and I had sensed something strange and questioned them relentlessly, but they had clamped their mouths shut after giving us the brief answer that they would tell us once Im Kkeokjeong woke up.

*But now it’s time for them to talk.*

Perhaps he sensed Song Song’s and my gazes. Team Leader Choi was just about to open his mouth when—

Thud. Thud.

All kinds of sounds mingled together in the hospital hallway. But their footsteps were different. They were unusually heavy, with a deep, resonant echo.

And there was qi.

“They’re coming.”

At my words, everyone rose from their seats one after another.

Sure enough, the footsteps stopped in front of our hospital room.

Knock, knock.

The door opened with the sound of a knock. A face I had seen only half a day ago appeared there.

*Go Jun?*

Wait. If that guy had come here, could it be…?

I couldn’t finish the thought. Go Jun’s face slipped out of sight as another man strode into the hospital room.

He was nearing seventy, yet his youthful appearance made him look like a man in his forties. He possessed the charisma of a leader and a natural air of intimidation.

*Lee Jungryong.*

His gaze swept past us before stopping dead on one person. The corner of his mouth lifted slightly.

“You’ve grown a lot.”

Team Leader Choi’s gaze sank deeply as he looked at Lee Jungryong.

[^1]: *AdultPhone* is a Korean pun on “iPhone”: *ai* can mean “child,” so the post jokingly replaces “child phone” with “adult phone.”
## Chapter artifact 287

# Chapter 287

Me, Im Kkeokjeong, Song Song, and Butler Kim.

Yet Lee Jungryong’s gaze, the moment he entered the hospital room, fixed on only one person.

Team Leader Choi.

“You’ve grown a lot.”

“……!”

The moment I heard Lee Jungryong’s first words, it felt as though someone had struck me in the back of the head with a sledgehammer.

*So this was what Team Leader Choi had been hiding.*

Their relationship was clearly more than that of an ordinary superior and subordinate at work.

*As far as I know, Team Leader Choi was with Ares Guild for only three or four years.*

Even if I estimated conservatively, he must have met Lee Jungryong when he was in his early to mid-twenties. “You’ve grown a lot” was not something you said to a man like that.

That was the sort of thing you heard from your parents’ friends or relatives during the holidays.

“It’s been a long time, Vice Guild Master Lee Jungryong.”

The stiff title and formal tone made Lee Jungryong stare at Team Leader Choi with an intrigued expression.

“Vice Guild Master? When you were young, you used to call me Grandpa.”

*Grandpa?*

That was the second shock. For a moment, I wondered if perhaps… but I quickly erased the thought.

This was simply a matter of what he had called him. He had only called Lee Jungryong Grandpa as a child. Lee Jungryong could not actually be Team Leader Choi’s grandfather.

*Still, it certainly seemed like they had been close since Team Leader Choi was young.*

That alone made Team Leader Choi’s relationship with Lee Jungryong anything but ordinary.

While everyone else was stunned, only two people maintained their composure: Butler Kim and Team Leader Choi, who answered calmly.

“That was twenty years ago.”

“Time is frightening. I never thought that affectionate little boy would turn out like this.”

“The older I got, the more I began to see things that had been invisible to me before.”

“I received a report that you resigned last year. Thinking back on it, I don’t believe I saw your face even once after you joined the Guild. I have to admit, I was a little disappointed.”

His expression showed no disappointment whatsoever, despite his words. Team Leader Choi’s face was no different.

“I felt the same way. If you hadn’t immediately transferred me overseas so I couldn’t even set foot in headquarters, we might have seen each other more often.”

“Why? Didn’t you like the overseas branch?”

“I felt it wasn’t where I belonged. That’s all.”

“Not where you belonged…”

“Wasn’t that the picture you wanted, Vice Guild Master?”

“You think that was what I wanted?”

Lee Jungryong let out a quiet laugh.

“So you built yourself a new nest? Even going so far as to borrow someone else’s name?”

“I’m sorry to interrupt while you’re speaking.”

Butler Kim, who had remained silent until then, suddenly opened his mouth. His voice was as calm as ever.

“But the young master and I aren’t strangers.”

“Oh, who might this be?”

Lee Jungryong widened his eyes in apparent surprise.

It was an exaggerated reaction. If he knew Team Leader Choi, there was no way he could have failed to know Butler Kim, the person closest to him.

“Kim Hwajong? It is Hwajong, isn’t it?”

“It’s been a long time, Senior.”

Butler Kim did not refuse the hand Lee Jungryong extended. The two men shook hands with even faint smiles on their faces.

*Informal speech? And Senior?*

Putting aside exactly what their relationship was, they seemed to be much closer than I had expected.

“It was a good thing I came in person. The last time we met was… about twenty years ago, wasn’t it?”

“Eighteen years, to be precise. *Ship-pal* years.”[^1]

[^1]: *Ship-pal*, meaning “eighteen” in Korean, sounds similar to *ssibal*, a strong profanity.

Was it just my imagination, or had he put extra force into certain words?

I glanced to the side. Song Song and Im Kkeokjeong looked as though they had seen a ghost.

*Ah. It wasn’t my imagination.*

Close, my ass. My eyes must have been broken.

I take it back. Butler Kim didn’t merely dislike Lee Jungryong.

He fucking hated him. He looked as though he would have preferred Lee Jungryong dead.

As a mage, he simply didn’t carry a knife. His tongue was a blade.

At his vicious words, Go Jun, who had been standing behind Lee Jungryong like an iron tower, took a step forward.

“Watch your mouth.”

“Watch my mouth?”

“He is not someone you may address carelessly.”

Butler Kim gave Go Jun a strange look.

“You look highly skilled at a glance, Hunter. What is your name?”

“I’m Go Jun, responsible for the Vice Guild Master’s security.”

“All right, Team Leader Seok.”

Butler Kim’s characteristic low voice continued smoothly.

“If you’ve said everything you have to say, shut your mouth and get back behind him. This isn’t a place for the likes of you to interfere.”

“……!”

Go Jun’s already expressionless face hardened.

Just as the veins began to stand out on his forehead, Lee Jungryong burst into hearty laughter and motioned for Go Jun to step back.

“I thought age might have mellowed you, but… your temper is still the same. This is the Kim Hwajong I remember.”

“When it comes to foul tempers, I’m still several levels below you, Senior. Wouldn’t you agree?”

Team Leader Choi added a word in a chilly voice.

“Let’s end this pointless conversation and get to the matter at hand.”

How many people in Korea—or in the entire world—could speak so carelessly to Lee Jungryong?

Im Kkeokjeong and Song Song were left gaping at the stormy exchange.

Even I was inwardly astonished by Butler Kim’s behavior, despite having personally witnessed him make Im Chunsoo, the Guild Master of Sangdong Guild, crawl like a dog several months ago.

*What on earth happened between them?*

Team Leader Choi was one thing, but even Butler Kim was completely different from his usual self.

“One of you is young and hot-tempered, while the other still hasn’t managed to abandon the temper he had in his youth. Well, there’s no harm in getting to the point now, I suppose. It’s a little disappointing, considering I came here as an invited guest.”

“Did you just call this an invitation?”

“You’re mistaken. Not one of us would invite you, Vice Guild Master.”

“Think carefully. Surely there’s at least one person who did?”

Lee Jungryong had been looking at the two of them with amusement. Then he suddenly turned his head toward me.

“That fellow.”

Silence descended over the room.

With everyone’s eyes on me, I thought for a moment before carefully opening my mouth.

“What kind of bullshit is that?”

The instant I finished speaking, Go Jun let out a low growl. He looked ready to charge like a hunting dog if Lee Jungryong hadn’t shaken his head.

After restraining Go Jun, Lee Jungryong spoke to me.

“Didn’t you say it yourself? That I should come in person and apologize to the victim.”

“Oh.”

I had definitely said that.

To Park Jihoon and Park Tae Seop.

“You look as though you never expected me to come.”

“To be honest, I didn’t. What are you plotting by coming all the way here?”

“You have a tendency to speak without considering what comes before or after. Since I accepted your invitation, shouldn’t you start by thanking me?”

*Thank him?*

I let out a hollow laugh. The rest of his words were so absurd that they weren’t worth answering.

“Your mouth may be crooked, but at least speak straight. It wasn’t an invitation. It was a demand. A demand for an apology.”

“No. If coming here had not been my own decision, could you—or the Peace Guild, for that matter—have made me move even a single step?”

“That’s…”

“Didn’t you think so yourself? You really didn’t expect me to come.”

It felt as though someone had dumped a bucket of cold water over me. My words caught in my throat.

Everything he said was true.

Though my heart had cried out for anger and revenge, I had never expected Lee Jungryong to come. Even then, my head had coldly compromised with reality.

*Lee Jungryong, the man who effectively ruled Ares Guild, was still a giant I couldn’t force to kneel here through my own strength.*

“A demand is the right of the strong. Words spoken by the weak to the strong can never be a demand. They are always a request—or an invitation.”

“……!”

“That’s why I came in response to an invitation. No matter what weakness you think you have in your grasp and wave around, that fact will not change. I am Lee Jungryong. I am Ares Guild, and Ares Guild is me.”

His voice was quiet, but it carried weight. Everyone in the Peace Guild, myself included, was left speechless.

At least one thing was clear. Lee Jungryong had not come here to apologize.

Having etched the overwhelming difference in power into our minds, he continued with a satisfied smile.

“And you shouldn’t treat a guest who came to visit a patient this way. Especially not a guest who brought a present for the patient. Isn’t that right, Team Leader Seok?”

“That is correct, Vice Guild Master.”

Go Jun answered like a robot and knocked on the door. A Hunter from the security team, who had been waiting outside, entered and placed what he was carrying on the table.

A vase filled with hundreds of flowers.

And an envelope.

“Compensation money. If the amount isn’t enough, tell me and I’ll give you more.”

My gaze remained fixed on the flowers. They were beautiful and white. I had never been particularly fond of flowers, but I had never disliked them, either.

Yet this was the first time in my life that receiving flowers as a gift had made me feel disgusted.

*Lilies as a hospital-visit gift.*

The anger I had forgotten began to crawl back up from the depths.

I rubbed my stiff, tingling neck and muttered,

“What a fucking old bastard…”

This time, even Go Jun couldn’t hold himself back.

With a roar, he charged. His fist lashed toward my lower jaw at blinding speed.

Crack!

Blood sprayed with a chilling sound.

I frowned and slowly turned my tilted head. The taste of sticky, salty blood spread through my mouth.

“Damn it. I bit my tongue.”

Go Jun’s eyes widened. He looked back and forth between his fist and me as though he couldn’t believe what he was seeing.

“How?”

“I’m pretty tough. I drank a lot of milk when I was young.”

“I definitely imbued it with mana…”

If it had been Fist Energy given physical form, I wouldn’t have been standing here like this.

Of course, if that had been the case, I wouldn’t have let him hit me on purpose, either.

I flashed him a grin.

“You should have used everything you had. Enough to finish me in one blow.”

Whoosh!

“Hup!”

Go Jun sucked in a short breath and reached out to knock my arm aside. He was so fast that an ordinary A-rank Hunter couldn’t even compare.

His hand curved like a hook and snapped toward my wrist.

*This really is a grappling technique.*

Remembering the surprise I had felt when fighting Park Jihoon, I smoothly twisted my wrist.

Slip.

As his hand clawed at empty air, I smoothly wound around his wrist and tightened my hold. At the same time, I put my strength into a stomp that drove down onto the top of his foot.

Crack!

“Urgh!”

The weight of a thousand geun crushed Go Jun’s instep and drove it deep into the solid concrete. With a groan of pain, he raised his arm to shield his face.

But…

“You think that’ll do?”

One thing was certain.

I hadn’t avoided the blow.

Go Jun hadn’t been able to avoid it.

Crunch!

My fist struck the exact center of his face, breaking his nasal bone in one blow and flattening the area beneath his nose.

His mouth flew open, and white teeth tumbled out amid the blood.

Clatter. Thud.

“You son of a bitch. Who the hell do you think you are, throwing the first punch?”

“……!”

It all happened in an instant. Everyone in the hospital room was shocked, but one person’s reaction stood out in particular.

“You bastard…”

The voice that had been relaxed throughout trembled faintly. Ripples spread through Lee Jungryong’s eyes.

I quickly spoke first, before things could get worse.

“For the record, that was self-defense.”

But the words I heard next were impossible to anticipate, or even guess at.

“What is your relationship with my older brother?”

“Excuse me? Who?”

“The person who taught you that.”

“If you mean that…”

My eyes snapped open.

*Was this old man talking about martial arts?*

But Lee Jungryong was no longer listening to me. His eyes had sunk deep as he stared at Team Leader Choi.

“Did Soyeong have another man?”

I didn’t know who the name Soyeong referred to.

But apparently, to someone, that name was a dragon’s reverse scale—a point that must never be touched.

Team Leader Choi clenched his fists, and blue flames blazed in Butler Kim’s eyes.

“Senior. Do you want to die?”

“Answer me.”

“You bastard! Lee Jungryong!”

“Now.”

Team Leader Choi’s tightly sealed lips finally parted.

“You know better than I do. What kind of relationship those two had.”

“Then that bastard…”

“You must have already investigated Mr. Jin Taekyung.”

“Are you saying all of that is true?”

“It is exactly as you know it. There isn’t a single lie.”

Lee Jungryong’s eyes trembled.

After looking back and forth between Team Leader Choi and me, he finally turned around slowly. The door opened as though someone had been waiting for the signal, and his steps came to an abrupt halt.

He tossed out a single sentence.

“I’ll send someone soon. Once the negotiations are over, hand over the people you’re holding.”

Click.

The door closed behind the last person to leave—the security team Hunter carrying Go Jun on his back.

It felt as though a storm had just swept through the room.

I turned toward Team Leader Choi, who was silently staring at the tightly closed door.

“Who is Soyeong?”

“She was my mother.”

“……What?”

“The mother who gave birth to me and raised me. She passed away a long time ago.”

My mouth fell open despite myself.

*What the hell is wrong with this old man?*

Lee Jungryong had asked Team Leader Choi whether his late mother had cheated while she was alive—her own son, no less.

“Crazy. Why would he—ah, never mind. You don’t have to answer.”

“It seems the shock was considerable for Vice Guild Master Lee Jungryong. I didn’t expect him to ask so directly, either.”

*To hell with whether he was shocked.*

I frantically waved my hand.

“Team Leader, really, it’s fine. You don’t have to tell me.”

“Sometimes I wonder what it would have been like if my mother had been born as someone other than Cheon Taemin’s daughter.”

“All right, that’s enough…”

My body abruptly froze.

*What did he just say?*

Although I couldn’t move an inch, my mind repeated three syllables faster than ever.

*Cheon Taemin. Cheon Taemin. Cheon Taemin…*

“Did you just say Cheon Taemin?”

“If my pronunciation wasn’t incorrect, then you heard me correctly.”

“Could it be… the Cheon Taemin I know?”

“Yes.”

Team Leader Choi nodded and continued.

“He was my maternal grandfather.”

For a moment, my vision spun and my legs wobbled.

*Cheon Taemin. He said Cheon Taemin.*

I had once harbored doubts about Team Leader Choi’s identity.

A man in his twenties with seemingly limitless ability, whom an A-rank mage known as a hidden hero of the Great Cataclysm called Young Master.

Now I finally understood how all of that had been possible.

It was because his maternal grandfather was Cheon Taemin.

*Humanity’s great hero. The world’s greatest Hunter…*

Among all the words used to describe Cheon Taemin, the title “Guild Master of Ares Guild” was only a small piece.

The name of the largest piece was an immortal achievement no one else could ever attain.

*The man who killed the Demon King. The Slayer.*

That Cheon Taemin’s maternal grandson was standing before me.
## Chapter artifact 288

# Chapter 288

In the back seat of the spacious limousine, Lee Jungryong held Go Jun’s arm and sent his mana flowing into it.

The limp body twitched, and strength soon returned to it.

Go Jun opened his eyes with difficulty and let out a faint groan. Lee Jungryong asked him,

“Are you conscious?”

“……I’m sorry. I should have kept him occupied longer.”

Go Jun lowered his head, his face stiff.

His earlier attack on Jin Taekyung had not been an impulsive act.

Go Jun was Lee Jungryong’s Disciple and the head of his security team. A man with exceptional composure and self-control would never have done such a thing unless it had been ordered by the master he respected beyond words.

*Jin Taekyung. I suppose we’ll have to see what he’s really capable of.*

*What should I do?*

*Keep him occupied as long as possible. Find out everything he’s got.*

*I never liked the bastard from the start. Looks like I’ll get to teach him a proper lesson.*

He should not have said that last part.

He had spoken so boldly, only to fail to withstand even a single blow. He had no face to show Lee Jungryong.

“You’ve exchanged blows with him directly, so you must have felt it yourself. Tell me exactly how strong he is.”

It did not take long for Go Jun to answer.

“He’s strong.”

Jin Taekyung had stormed into Myeongdong Guild alone. Go Jun had known from the beginning that he was not someone to take lightly.

But even after taking a mana-infused punch directly, Taekyung had not fallen—or even taken a single step back. Go Jun had never imagined that someone could possess such absurd toughness.

“I hit him squarely in the jaw, but he was harder than rebar. I’ve never seen anyone like him.”

Go Jun could not understand how Taekyung could look so unharmed without wearing armor or being covered in defensive magic.

The bigger problem was that Jin Taekyung was not simply a man with exceptional toughness.

“His strength and speed were both superior to mine.”

“What if you had gone all-out from the beginning, Team Leader Seok?”

After a brief hesitation, Go Jun answered in a rigid voice.

“……It would have been difficult.”

He remembered Taekyung’s lightning-fast hands.

By the time he realized his mistake, his arm was trapped and his foot had been driven deep into the ground. He had hurriedly raised his arms to protect his face, but the punch carrying monstrous force had broken through them and slammed into his face.

“I don’t know how it happened, but Jin Taekyung has extensive combat experience. He’s on an entirely different level from ordinary Hunters who only fight monsters.”

“And?”

“Pardon?”

“There’s something you haven’t said yet, isn’t there?”

“…….”

“I believe I told you to speak without holding anything back.”

When Go Jun met Lee Jungryong’s gaze, he realized it.

Lee Jungryong had reached the same conclusion.

“You had already guessed.”

“Yes. Today, that suspicion became certainty.”

“You mean…”

Lee Jungryong’s voice sank low.

“There’s no doubt about it. Jin Taekyung has learned a mana cultivation method.”

“……!”

A mana cultivation method.

A tiny ripple appeared in Go Jun’s previously unwavering eyes. The words that had come from Lee Jungryong were that shocking.

“An insignificant F-rank Hunter grew this strong in only half a year. People are babbling about reawakening or a measurement-device error, but that’s just nonsense from people who don’t know anything.”

Go Jun muttered like a groan,

“But how……? Aren’t mana cultivation methods among the most closely guarded secrets?”

“Top secret? That’s a meaningless phrase. As long as someone knows something, it can never be a perfect secret.”

“Could Team Leader Choi have done it?”

Lee Jungryong shook his head.

“That boy Minwoo never learned a mana cultivation method. Neither did Kim Hwajong, who stayed by his side since childhood.”

“Isn’t it something no one knows about? If the Guild Master…”

“Who?”

Go Jun could not finish his sentence. He froze where he sat.

The moment he met Lee Jungryong’s deeply sunken eyes, he realized that he had said something he should not have.

“I believe I told you not to even open your mouth about my older brother.”

“I-I’m sorry. I misspoke…”

Go Jun’s voice trembled like a wounded bird.

He had been so flustered by the news that Taekyung had learned a mana cultivation method that he had broken an unspoken taboo. Cheon Taemin, the Ares Guild Master, was someone who must never be mentioned.

Thud!

Both of Go Jun’s knees struck the floor. He bowed deeply and said,

“Please forgive me, Vice Guild Master.”

“Forgiveness? These things happen in life.”

“…….”

“Get up.”

Even after carefully lifting his knees from the floor and sitting back down, Go Jun could not look Lee Jungryong straight in the eye.

He had spent years at Lee Jungryong’s side, seeing and learning many things.

To Go Jun, Lee Jungryong was an object of both respect and fear.

Go Jun’s usually machine-like expression was now tinged with quiet fear.

“Team Leader Seok.”

Lee Jungryong was the one who broke the suffocating silence.

Go Jun lowered his head even further.

“Yes, Vice Guild Master. Please speak.”

“You’re going to be very busy from now on. If you let your mouth run carelessly like this again, you’ll put me in a difficult position.”

“I’ll keep that in mind. I’ll keep it in mind above all else.”

“Strengthen surveillance on the Peace Guild from now on. Find out whether they have anyone useful.”

Go Jun cautiously raised his head.

“Are you planning to reinforce the security team?”

“Yes. We can’t continue like this. We need to prepare for any situation.”

“Yes. I’ll put it into action as soon as we return to the Guild.”

“And…… don’t overlook the movements of the executives, either. That includes the situation at our overseas branches.”

“I’ll carry it out without a single omission.”

Lee Jungryong’s position within Ares Guild was already secure.

But not everyone followed him blindly like Go Jun did.

There were always people dissatisfied with the status quo, and they watched Lee Jungryong’s actions with suspicious eyes.

The security team, on the other hand, was little more than Lee Jungryong’s personal army.

Having received enormous salaries and instruction in mana cultivation methods, the security team offered absolute loyalty to one person alone: Lee Jungryong.

*Yes. Things have been too peaceful until now.*

Lee Jungryong turned his gaze toward the window. Beyond the spotless glass, the Han River stretched wide into the distance.

Only thirty-some years ago, its waters had been filled with the corpses of humans and monsters. Now they were clear and clean, as though nothing had ever happened.

*Older brother. The world has changed so much.*

Lee Jungryong’s thoughts did not escape his lips.

His eyes had already begun slowly tracing the distant past. Cities engulfed in flames and people dying. Monster armies charging forward, turning heaven and earth upside down……

And in the midst of that hellscape, there had been one person shining alone.

*Don’t take so much as a single step out from behind me.*

Lee Jungryong had been thirty years old and filled with cynicism toward the world. The moment he met that man, he was captivated.

Though they did not share a drop of blood, Lee Jungryong regarded him as an older brother and always looked up to him with respect and fear.

Even now, past the age of sixty, those memories and emotions remained vivid.

Lee Jungryong was staring silently out the window, lost in thought, when Go Jun’s voice brought him back.

“We’ve arrived.”

At the same time, the limousine door slid open. A skyscraper towered before them as though it could pierce the clouds, surrounded by a forest of buildings encircling it like guards protecting a king.

Dozens of Hunters waiting outside bowed toward him. The lapels of their suits bore the emblem of Ares Guild.

“Welcome, Vice Guild Master Lee Jungryong!”

Their shout was perfectly synchronized, as though measured with a ruler.

With a faint smile on his face, the man in power stepped onto the red carpet.

* * *

This was a world where even white-haired old men wore wireless earbuds and watched iTube.

Whenever snow fell and icy roads formed, nursing homes shut down, while Old Man Kim and Granny Park chatted through a voice-chat app and played online Go-Stop.[^1]

If magic was a mysterious realm whose origins were unknown, the internet was the concentrated essence of twenty-first-century civilization.

With just a few clicks and keystrokes, you could learn about events happening all over the world as easily as looking into the palm of your hand.

In a world like this, information about the most famous person among several billion people went without saying.

Tap. Tap-tap.

*Cheon Taemin.*

His name completed itself after I typed only the initial consonants. It even ranked higher in searches than heaven.

People were more interested in the person who had stopped them from nearly going to heaven than in heaven itself.

*I was no different.*

Muttering inwardly, I tapped the search result that read “Cheon Taemin—Profile.”

The face I had seen hundreds, thousands of times since elementary school filled the phone screen.

Thick eyebrows and chiseled features. He looked like a handsome Greek god reincarnated.

And then……

“He looks like him.”

“Now that I see them side by side, they really do look alike.”

“Whoa, they’re identical.”

They really did look alike. Enough to make me wonder if this was why people said you could never hide your bloodline.

I, Im Kkeokjeong, and Song Song all stared at the phone screen, then at Team Leader Choi, our mouths hanging open.

“Ahem.”

Only when Team Leader Choi finally gave an uncomfortable cough did we manage to come to our senses.

No, not yet. Come to my senses, my ass.

*What the hell is going on?*

Things had become spectacularly complicated, with no distinction between the Murim and the modern world.

When Park Jihoon stabbed me in the back and Lee Jungryong suddenly burst onto the scene, I’d been certain nothing could surprise me anymore……

But this was shock and horror in its purest form.

*Not the president’s grandson, but Cheon Taemin’s grandson.*

A president’s term lasted five years, but Cheon Taemin had no term.

The achievements and Fame built in his name would remain immortal and be passed down through the generations.

He had driven a sword into the Demon King’s heart and saved all of humanity. What more needed to be said?

Humanity’s hero. The world’s greatest Hunter, recognized by the entire world.

*Unprecedented and unmatched. He was the very definition of it.*

Team Leader Choi was that Cheon Taemin’s sole grandson through his daughter.

Cheon Taemin had only one daughter, and there was no information about any other relatives. He was probably the only heir.

Good God. Cheon Taemin’s heir.

Even thinking about it made my skin crawl.

I opened my mouth in a trembling voice.

“Team Leader Choi.”

“Yes, please speak.”

Team Leader Choi answered as though he had been waiting for the question. He even looked relieved that the awkward silence had been broken.

“If you don’t mind, may I ask you something?”

“Anything.”

“Then may I continue calling you Team Leader Choi?”

“What?”

Team Leader Choi looked dumbfounded.

“Then what exactly were you planning to call me?”

“Mr. Choi Minwoo. Minwoo hyung.”

“I refuse.”

“There’s one more option……”

“Don’t say it. I don’t want to hear it.”

“Please adopt me. I’ll call you Dad. I’ll be a good son.”

Team Leader Choi’s face turned bright red.

If I had really been his son, he looked ready to disown me on the spot.

A moment later, he let out a deep sigh.

“……This isn’t the time for jokes.”

“I’m not joking. I’m serious.”

“Mr. Jin Taekyung!”

Team Leader Choi continued in a voice that had gone completely flat.

“Didn’t I explain everything? My situation and what I’m dealing with?”

“You did. We all heard it.”

Im Kkeokjeong and Song Song nodded.

An hour earlier, after Lee Jungryong had left and we were still unable to recover from the shock, Team Leader Choi had told us everything.

His true identity and everything that had happened until now. He had also explained why he had no choice but to act as he did.

“Lee Jungryong is an extremely ambitious man. He considered me a thorn in his side and kept me under surveillance at all times. That’s why he kept transferring me from one overseas branch to another so I couldn’t even set foot in the headquarters.”

Team Leader Choi said that his surroundings had been filled with watchful eyes.

Lee Jungryong had assigned him to insignificant posts so he could not achieve any noticeable results, and even then, his placement had to be changed once a year. They were called overseas branches, but it was no different from exile.

“Cheon Taemin—no. Did the Ares Guild Master simply stand by and watch?”

“As I said, my maternal grandfather……”

Team Leader Choi bit down hard on his lip.

“He’s a special person. It’s only a memory from my childhood, but he absolutely didn’t think like an ordinary person.”

Butler Kim, who had been standing quietly nearby, added,

“He was the same in the past, and he remains the same now. I served the old master for many years, but I have never once managed to understand what he was thinking.”

Was this the dark side of the hero that no one knew about?

Team Leader Choi sighed and continued.

“Even after I submitted my resignation and left Ares Guild, they must have continued watching me. Later, I founded the Peace Guild…… but even recruiting one ordinary mid-rank Hunter was difficult.”

As I listened, I learned something for the first time: Im Kkeokjeong and I had not been the Peace Guild’s first members.

Several high-ranking Hunters had joined before us, but after receiving unexpectedly generous contract offers, they transferred to other Guilds. Some of them even suddenly disappeared before signing their contracts.

*It was probably Lee Jungryong’s doing.*

No matter how much money you had, a Guild without Hunters was not a Guild.

Squeezed by pressure from Ares Guild on every side, Team Leader Choi began looking for personnel through the Hunter Office. That was when Im Kkeokjeong and I appeared on his radar.

Fortunately, there had been no significant pressure this time.

*Two low-ranked Hunters probably weren’t worth bothering with.*

And that had been Ares Guild’s miscalculation.

No one could have imagined that an F-rank Hunter who looked useful only as a porter would create a whirlwind like this.

“This situation is no different. When I heard that you had met Lee Jungryong, Mr. Taekyung, I thought it had happened because of me.”

“So?”

“Pardon?”

I scratched the back of my head vigorously.

“So what are you trying to say, Team Leader? You still haven’t said it clearly.”

“The difference in strength is too great for us to make an enemy of Ares Guild.”

“Everyone knows that.”

“Similar things will continue to happen.”

“More detail. Be precise.”

Team Leader Choi gritted his teeth.

“I’ll terminate your contracts. If you cut ties with the Peace Guild, Ares Guild won’t bother any of you.”

His voice was boiling over. Team Leader Choi closed his eyes and clenched his fists.

I stared at him for a moment before opening my mouth.

“I don’t like that.”

“What?”

“I said I don’t like it.”

“…….”

“They’re dinosaurs. We’re ants. We’re weak, so let’s back off before we get hurt worse. That’s what you’re saying, right?”

“Mr. Jin Taekyung.”

“Then it’s simple.”

To Team Leader Choi, who was staring at me wide-eyed, I continued, each word slow and clear.

“Let’s get stronger.”

No.

“I’ll make you strong. I will.”

[^1]: Go-Stop is a Korean card game played with hwatu, traditional flower cards.
## Chapter artifact 289

# Chapter 289

“Pardon?”

Team Leader Choi looked more violently shaken than I had ever seen him before.

Even Butler Kim, who at least looked calm, wasn’t much different.

Lingering anger and bewilderment. And questions about what I had said.

*I didn’t know they could make expressions like that.*

Whenever I charged ahead without thinking things through, these two always took two calm steps back and handled the situation.

For once, they looked like ordinary people just like me.

Feeling a strange stirring in my chest, I opened my mouth.

“The answer is simple. If the enemies are strong, we get stronger too.”

“Mr. Jin Taekyung.”

Team Leader Choi’s voice was quiet and steady. Having gathered his initial emotions, he had returned to his usual calm self.

“This isn’t a math problem that gets solved just because you know the answer. To reach the correct answer, you have to go through a process so difficult it’s beyond imagination.”

“Then that’s fine. If I take on the role of your private tutor, I think we can solve it even if it takes some time. Ah, but let’s change the subject. I’m hopeless at math.”

“Have you forgotten? Our opponent is Ares Guild. You may not know this, but I do. I know exactly how powerful an opponent they are.”

“Unfortunately, the Young Master is right.”

Team Leader Choi and Butler Kim fell silent after that.

One was the maternal grandson of Cheon Taemin, Guild Master of Ares Guild. The other was a core member who had served Cheon Taemin for many years.

Given who they were, they must have seen and experienced a great deal firsthand. Their blood might have been boiling, but their cool heads had already calculated the answer. But…

“Team Leader Choi.”

I looked into his eyes, which had already reached their conclusion, and asked,

“Do you remember what you said to me before we went to Myeongdong Guild?”

“Of course.”

“What did you say back then?”

After hesitating for a moment, Team Leader Choi parted his lips.

“Mr. Jin Taekyung may seem reckless at first glance, but…”

“He always anticipates the worst-case scenario before acting. And?”

“He always brings back the best possible result.”

“You said you trusted me more than you trusted yourself, Team Leader. Did you only say that because it sounded nice?”

“Absolutely not.”

“I may not have been good at studying, but I’m not stupid enough to risk my life on a game with zero chance of winning. This is doable.”

“Doable…”

“If you can’t believe in yourself, then believe in me.”

Team Leader Choi sensed the sincerity behind my words. Light began to seep into his eyes. It was faint, but I knew what that light was.

Hope.

Hope was like a spark. It could flare up or die out in an instant. You had to fan it before it went out.

“Since we’re talking about it, let me ask you something. If I leave the Guild here, will you give up too? Well, shutting down the Guild, retiring, and farming with Butler Kim wouldn’t be so bad. If that happened, Lee Jungryong might even supply the fertilizer.”

“Hunter Jin Taekyung!”

I ignored Butler Kim, who tried to stop me, and continued.

“You said you wanted to build the greatest Guild in the world. If you send me away, send Uncle Kkeokjeong and Song-i away as well, and even the new recruits leave, do you two plan to fight Ares Guild by yourselves?”

“……”

“Team Leader Choi.”

He remained silent. No answer came back.

But the spark in his eyes was still alive.

Before long, a hoarse voice slipped between his lips.

“Ares Guild is an empire. An empire so powerful that even the ten largest Guilds in Korea couldn’t stand against it if they joined forces.”

“Well, looks like we’ll have to work hard to catch up with those guys.”

“I may not know everything about Ares Guild, but I know a great deal. That’s why I think they’re even more dangerous.”

“At the same time, our chances just went up. It means we understand the enemy well. Know your enemy and know yourself, and you can fight a hundred battles without disaster. Right?”

“I’ve thought about it over and over, but the answer to my calculations was impossible.”

“Then calculate it again.”

“Is it really… possible?”

“Yes.”

“Where exactly are my calculations wrong? What on earth gave you such confidence in your answer?”

He wasn’t asking because he failed to understand.

More than anyone, Team Leader Choi wanted his answer to be wrong. He wanted even the faintest possibility of standing against Lee Jungryong.

I was happy to answer that wish.

“The person talking to you right now.”

“……!”

“The process of your calculations was accurate. Except for one thing.”

I slowly raised a finger and pointed at my chest.

“Me.”

At that moment, Team Leader Choi’s eyes shook. I could feel the spark in them beginning to fade.

What filled its empty place was not hope, but disappointment.

“You were included in my calculations, Mr. Jin Taekyung.”

“Of course I was. If you’re the Team Leader Choi I know.”

Team Leader Choi was a brilliant man. He had natural leadership, along with excellent insight and drive.

He had placed Peace Guild and Ares Guild on opposite sides of the same scale, and I must have been included in the weight of Peace Guild.

“The things you’ve shown us until now have always been astonishing. No, they’ve been almost miraculous.”

I already knew what words would follow his fading voice.

“But I’m still not enough?”

Team Leader Choi nodded heavily.

“Ares Guild officially has more than a hundred A-rank Hunters, even excluding Lee Jungryong, an S-rank Hunter. And there are countless mid- and low-rank Hunters.”

The fact that he put such unusual emphasis on the word *officially* meant that there were even more hidden forces.

*And they still have more than a hundred A-rank Hunters.*

I had already heard rumors about it, but hearing it directly from Team Leader Choi made Ares Guild’s military strength feel real.

No matter how strong I was, in the end, I was still only one pair of hands. Team Leader Choi’s judgment was cold and clear.

But…

“If that’s how you’re calculating it, you’ll have to run the numbers again.”

“Pardon?”

“The formula is right, but the numbers are wrong. I don’t know what value you assigned to me, but you’ll have to count me at least several times higher.”

Team Leader Choi wasn’t the only one whose eyes widened. Butler Kim, Im Kkeokjeong, and Song Song all stared at me in shock.

Considering everything I had accomplished until now, their reaction was understandable.

I had hunted a Named Monster alone, crushed nearly thirty Black Hunters, and confronted a major Guild like Myeongdong Guild head-on.

Leaving those people frozen like statues behind me, I fixed my gaze on Team Leader Choi.

“I feel like I’ve told you this repeatedly. I’m a man with more secrets than you think.”

Murim was Murim, and the modern world was the modern world.

There had always been a clear boundary in my mind separating the two worlds. But Lee Jungryong and Ares Guild had erased that line.

If something like this had never happened, I probably would have kept those secrets to myself for the rest of my life.

*Was wanting to live quietly too much to ask?*

Maybe this was the fate of the power I had been given. If so, I had to accept it now. I couldn’t keep running away forever.

To protect the things precious to me from my enemies, I had to become stronger.

“So, what are you going to do now?”

Team Leader Choi was still looking at me with eyes that couldn’t quite believe what he was hearing.

“Mr. Jin Taekyung, you always manage to surprise me.”

“Save it. There’ll be plenty more of that from now on.”

“It will be a dangerous road.”

“I happen to specialize in thorny roads.”

“Nothing you’ve faced until now will compare to it.”

“Nothing to compare it to, my ass. You just don’t know it. This side is already hell…”

He seemed to have taken my words as a joke.

I watched Team Leader Choi as he finally let out a quiet laugh.

“Team Leader.”

“Yes?”

“Sometimes, it’s okay to be honest.”

The smile at the corners of Team Leader Choi’s mouth disappeared. His gaze settled, and he pressed his lips tightly together.

I waited for him to speak. What came next was something I had to hear directly from Team Leader Choi himself.

Fortunately, I didn’t have to wait long.

“I know this is an impertinent request, but… would you continue to stay with Peace Guild?”

*Yes. This was it.*

I grinned and gave Team Leader Choi’s shoulder a light tap. He looked smart and cold on the outside, but he was still softhearted inside.

That was why, despite wanting us to stay, he had tried to send us away out of fear that we would get hurt.

“Let’s do this right.”

“……Thank you.”

Team Leader Choi gave a fleeting smile before turning toward the others.

Butler Kim, his devoted retainer and someone practically no different from family, spoke first.

“I believe you already know what my answer will be.”

“Thank you, Butler Kim.”

Next was Song Song. Team Leader Choi had asked her the same question he had asked me. She heaved several deep sighs before opening her mouth.

“Ares Guild? Ah, this deal doesn’t really add up.”

That was actually the most normal reaction. They were saying they intended to openly make an enemy of Ares Guild. Anyone who welcomed that idea would be strange.

“Set my annual salary at twice its current amount. And add hazard pay.”

“……”

Song Song wasn’t normal either.

When I stared at her in disbelief, she shrugged.

“What? Why?”

“No, nothing. I just thought most people would walk away in a situation like this.”

“Would you like me to?”

“Now, now. Absolutely not.”

“Do you know why I transferred from Ares Guild to Peace Guild? Why I followed Team Leader Choi, even though he was being opposed from all sides?”

“How would I know?”

“Because Team Leader Choi promised me double my salary.”

“……”

“My goal is to retire at thirty. If I earn as much as I can over the remaining two years, I’ll be able to live comfortably for the rest of my life.”

She said it as though it were nothing, but she was only circling around the words *I want to stay with you, too*. Everyone knew that thrifty Song Song had already saved herself a small fortune.

“And, well, you seem to have a plan too, so I’ll trust you for now. It’s hard to find a superior as capable and handsome as Team Leader Choi.”

In any case, Song Song’s decision to stay was now confirmed. Everyone’s eyes, including mine, shifted toward the last person.

“Uncle Kkeokjeong.”

He didn’t answer when I called him. It was only after a long while that he finally parted his lips.

“Taekyung, will I be of any help?”

“More than enough.”

“Even though I’m only a D-rank Hunter?”

“People associated with D are the real protagonists, after all. Why not legally change your name while you’re at it? Im D. Kkeokjeong. How does that sound?”

Im Kkeokjeong laughed out loud and looked straight at Team Leader Choi.

“It wasn’t Team Leader Choi’s fault that I got hurt. So don’t blame yourself.”

“No. It’s all my fault, so please focus on your recovery and rehabilitation first, and think it over at your own pace. Hunter Im, you have a family, don’t you?”

“Team Leader Choi.”

“Yes?”

“When my arms were first severed, do you know what thought came to me first?”

“Your family?”

He was a woman’s husband and the father of two children.

But Im Kkeokjeong calmly shook his head.

*Ah. I guess I can’t work as a Hunter anymore.*

“That was the thought that came to me.”

“……”

“I love this work. I spent twenty years going in and out of Gates, not to make a living, but because of my sense of duty as a Hunter. But…”

Im Kkeokjeong bit down hard on his lip. His gaze remained fixed on his own two arms, wrapped in bandages.

“Can I recover?”

“You can. Absolutely.”

A faint smile spread across Im Kkeokjeong’s mouth.

“Then I’m coming too. I can’t abandon a Hunter’s duty over something like this.”

Something churned deep in my chest at the sight.

People dismissed him as a low-rank Hunter with nothing but the title, but Im Kkeokjeong was one of the few true Hunters left in this age.

*They’re all far too good to stop here.*

All right. They said you should strike while the iron was hot.

Having made up my mind, I opened my Skill window for the first time in a long while.

Then, in the holographic window packed with entries, I found what I wanted.

> **System**
>
> **Skill:** Martial Arts Manual Creation

*Yes. This was the beginning.*

With firm resolve, I touched the holographic window.

Beep!

> **System**
>
> To create a martial arts manual, you need at least 300 sheets of A4 paper!

“……”

What the fuck.

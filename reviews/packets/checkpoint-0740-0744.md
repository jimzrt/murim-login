# Checkpoint Review — 740–744

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

# Chapters 740–744

## Plot

After three days of qi circulation, Jin Taekyung resumes eating and resolves to pursue Michael Silbert and The Prophet despite accepting his own indirect responsibility for the terrorist attacks. Team Leader Choi reveals that Odin Guild controls more than two hundred Gates through an extensive asset network, while The Prophet remains unlocated. Magic Johnson then reports the death of Siegfried Wassmann, the retired Grand Mage who designed A Area.

Jin, Choi, the Skeleton King, and Magic travel to Siegfried’s hidden Swiss laboratory and find his corpse unnaturally desiccated without wounds, rot, or odor. The System forcibly assigns Jin the Supreme Peak Quest **Unknown Death**, requiring him to uncover who killed Siegfried and how. Siegfried’s reverence for Cheon Taemin makes Michael the leading suspect, since Michael knows about A Area and Taemin’s condition, but the source of that knowledge remains unknown.

Michael undergoes a painful transformation that grants him overwhelming new power. He abandons the Swiss investigation as strategically useless, continues secretly funding media attacks against Jin, and orders Huginn to complete an undisclosed operation. Huginn destroys the communication crystal’s remains at sea, expecting its consequences within three days.

Swiss Federal Police Hunters briefly detain and question Jin’s group but release them for lack of evidence. Jin gives Magic a subspace pocket containing Siegfried’s research materials for investigation, while the others focus on locating Michael and The Prophet. They conclude that finding The Prophet is their best chance to prevent another catastrophe, even though the Pentagon has failed to locate him. As magical power continues spreading and damage escalates, an enormous ancient creature awakens in the deep sea, revealing a colossal eye.

## Continuity

- Jin has forcibly accepted the Supreme Peak Quest **Unknown Death**; its reward and failure conditions remain unknown.
- Siegfried Wassmann, one of the world’s three Grand Mages and the creator of A Area, was found dead in his sealed Swiss hideout.
- Siegfried’s body was unnaturally dried out without visible injury or decomposition, indicating an unknown life-draining magic.
- Michael Silbert is the strongest suspect in Siegfried’s death because he knows about A Area and Cheon Taemin’s unconscious condition; no proof links him to the killing yet.
- Magic Johnson possesses Siegfried’s stolen research materials and is investigating them for clues.
- The Prophet remains unidentified and missing, despite a worldwide search and Pentagon involvement.
- Michael has acquired unexplained overwhelming power through a painful transformation.
- Michael and Huginn are manipulating media coverage to damage Jin’s reputation.
- Huginn has completed an undisclosed operation whose effects are expected within three days.
- Mana levels and the distribution of magical power continue rising sharply, with mutation Gates appearing dozens of times daily.
- An enormous ancient monster has awakened in the deep sea; its identity, origin, purpose, and connection to current events are unknown.

## Translation Decisions

- Render **알 수 없는 죽음** as **Unknown Death**.
- Render **마력** as **magical power**, distinct from **mana**.
- Render **아공간 포켓** as **subspace pocket**.
- Render **심해** as **deep sea**.
- Render **선지자** as **The Prophet**, **스켈레톤 킹** as **Skeleton King**, and **A구역** as **A Area**.
- Render **지크프리트 바스만** as **Siegfried Wassmann** and **실베르트** as **Silbert**.
- Preserve uncertainty around Siegfried’s killer, Michael’s source of information, Huginn’s operation, The Prophet’s whereabouts, and the awakened deep-sea creature.

## Durable state

{
  "active_continuity": [
    "The retired Grand Mage Siegfried Wassmann, one of only three Grand Mages in the world and Switzerland's greatest Hunter, was found dead in his sealed hideout.",
    "Siegfried's corpse was unnaturally dried out without wounds, rot, or odor, suggesting that something drained his life force through an unknown form of magic.",
    "Michael Silbert remains the strongest suspect because he knows that Cheon Taemin is unconscious and may know about A Area, but the source of his knowledge is unknown.",
    "The Prophet remains a second major suspect connected to the terrorist campaign, and even the Pentagon has not located him.",
    "Jin has forcibly accepted the Supreme Peak Quest Unknown Death, whose mission is to discover the truth behind Siegfried's death; its Reward and Failure are unknown.",
    "Mana levels are rising sharply, and mutation Gate phenomena continue occurring dozens of times daily while the distribution of magical power has amplified again.",
    "Michael has gained an unexplained increase in power through a painful transformation and now possesses overwhelming strength.",
    "Michael and Huginn are bribing media outlets and sustaining malicious coverage intended to weaken Jin's public support.",
    "Magic Johnson has received stolen research materials from Siegfried's laboratory and is investigating them for clues.",
    "Huginn has completed an undisclosed operation whose consequences are expected to begin within three days.",
    "An enormous ancient monster has awakened in the deep sea after having been believed gone for a very long time."
  ],
  "continuity_sources": [
    744
  ],
  "open_questions": [
    "Who killed Siegfried Wassmann, by what magic, and why?",
    "How did Michael Silbert learn about A Area and Cheon Taemin's condition, and did he order Siegfried's death?",
    "What connection, if any, does The Prophet or the terrorist network have to Siegfried's death?",
    "What is Huginn's undisclosed operation, and can its consequences actually bring Jin down?",
    "What is the identity, purpose, and origin of the ancient monster that awakened in the deep sea?"
  ],
  "safe_through": 744,
  "temporary_decisions": [
    "Render 선지자 as The Prophet.",
    "Render 스켈레톤 킹 as Skeleton King.",
    "Render A구역 as A Area.",
    "Render 마력 as magical power, distinct from mana.",
    "Render 지크프리트 바스만 as Siegfried Wassmann and 실베르트 as Silbert."
  ],
  "version": 1
}

## Reading copies

## Chapter artifact 740

# Chapter 740

Circulating qi and regulating the breath was not solely about increasing internal energy.

Naturally removing the waste that accumulated inside the body and calming the mind were also among the many benefits of circulating qi.

And since circulating qi brought one into a state of supreme concentration, it went without saying that all five senses were heightened to their limits.

*What is this…?*

Thud. Thud. Thud.

Someone’s footsteps sounded like thunder.

Before long, I realized who the uninvited guest pacing outside the door was and brought my internal energy under control.

*Chime.*

Just as a System notification announcing the end of my qi circulation rang out, the doorknob behind me began to turn.

*Click.*

A strong scent wafted through the narrow gap as the door opened cautiously.

After finishing everything with a deep exhale, I spoke.

“I thought I said no one was to come in until I came out on my own… Are you unable to understand human speech because you’re a monster? Or do you just have no intention of understanding it?”

The uninvited guest hesitated before clearing his throat. It was the Skeleton King.

“Ahem. How did you know it was this body?”

“Your presence.”

“My presence?”

“Yeah. Maybe because you’re already dead, but you don’t breathe.”

“…That makes a strange amount of sense, but it’s still unpleasant.”

“There’s no reason for me to go out of my way to make you happy.”

I pulled on the tracksuit I had carelessly taken off nearby and turned around. The Skeleton King stood there like a butler, holding a gleaming silver tray.

“So why are you here?”

Normally, he would have been sulking hard by now, his pout stretching a good thirty feet.

But today, the Skeleton King was different. He kept glancing at me nervously as he lowered the silver tray to the floor.

“Eat. This body personally brought it for you.”

“I told you not to bring me things like this.”

“But you have been fasting for more than three days.”

More than three days?

Taken aback by his unexpected words, I looked around.

It was a room sealed off on all sides, without even a window. I had come in without my smartphone, and whether because of that or because I had not had the energy to care, I had completely lost track of time.

*Has it already been that long?*

Humans were strange creatures. They were even stranger when belated hunger struck the moment you realized how many days had passed.

But…

Did I even have the right to feel hungry?

Thousands had died, and tens of thousands had been injured. I did not know what kind of lives they had led, but most of them must have been innocent people.

Those very people had suffered because of what I had done. They had died, been injured, and lost their precious families and friends.

Until only a short while ago, the people who had raised me up as a hero had turned away one by one, and the arrows of condemnation had reached the people around me as well.

All because they were close to me.

*What exactly went wrong? And where did it begin?*

I had shut myself away in this room to find the answer to that question, which refused to leave my mind. Without eating or sleeping, I had spent each day circulating qi and lost in thought.

And at last, I had found an answer.

It was not an answer that could neatly resolve everything, but it was an insight that allowed me to forget it for a while.

“Smells good.”

“Huh?”

“Not you. The food.”

The Skeleton King froze as if he were buffering before answering.

“Uh, yeah. It’s doenjang jjigae and braised short ribs.”

Even from the smell alone, I could tell who had made it.

I pictured my mother anxiously preparing meals for me over the past several days and lifted the lid covering the silver tray.

*Click.*

I stared blankly at the food as steam rose from it. Then I scooped up a spoonful of doenjang jjigae, something I had not seen in a long time.

The moment I put it in my mouth, I spat it right back out.

*Ptooey.*

“Wh—what? Why?”

What the hell was this?

I looked back and forth between the flustered Skeleton King and the doenjang jjigae before opening my mouth hesitantly.

“Who made this?”

“Your younger sister.”

“…Ah. Right.”

“Is something wrong?”

A problem? There was one. A serious one.

But instead of answering, a quiet laugh escaped me.

I did not know why. It just did.

“I’ll eat and then go.”

“What?”

“I’ll just eat this and go. And I’ll take a shower, too.”

The Skeleton King blinked for a while, as though he had not understood me, then hurriedly nodded.

“Oh? Oh, understood. Then this body will…”

“Yeah. See you later.”

He slowly closed the door and disappeared like a thief, and another inexplicable laugh escaped me.

I set down my spoon, picked up a piece of braised short rib, and took a large bite.

Fortunately, the braised short ribs had been made by my mother.

* * *

“There were vicious dogs going around biting people, so I beat them senseless. But this time, two mad dogs showed up.”

At my first words after several days apart, Team Leader Choi nodded after briefly moving his lips as though he had been about to say something.

“That’s right. And those two mad dogs bit even more people.”

“Do you think it’s my fault too, Team Leader Choi?”

“Mad dogs are nothing more than mad dogs. In the end, it is only a matter of timing and pretext. They would have bared their fangs at people sooner or later.”

“But I’m the one who gave them the opportunity to do it.”

“If you insist on blaming yourself, then say ‘we.’ This wasn’t something Jin Taekyung did alone.”

“That’s right. This body also achieved a great feat in the desert.”

At the Skeleton King’s sudden interruption, Team Leader Choi shrugged.

“That’s what he says.”

“I’m not blaming myself. I just thought I needed to make that much clear.”

Every incident had a cause and an effect.

And since so many people had died or been injured, I could not claim to be free of responsibility for the cause.

Nor did I intend to.

“I understand the people who condemn me. And I’m simply grateful to those who support me.”

“Is that all?”

“No. The most important thing is still left.”

I continued speaking calmly.

“No matter what the world says, I’m going to catch those mad dogs.”

The Skeleton King’s eyes gleamed at my answer, while a faint smile appeared around Team Leader Choi’s mouth.

“You found an answer of your own.”

“It may not be a complete answer, but isn’t it enough of a reason to keep moving forward?”

“That is enough. Then I can deliver some news with a lighter heart.”

“News?”

“Even before this incident occurred, I had been gathering information related to Michael Silbert and Odin Guild. The results came in recently.”

Team Leader Choi had been monitoring the movements of the other major Guilds since before the Mana Cultivation Method was released. Given his meticulous nature, that was only natural.

“What is it? I’d prefer good news, if possible.”

“Unfortunately, there is bad news as well. Which would you like to hear first?”

“It can’t get any worse than this. Tell me the bad news first.”

Team Leader Choi gave a short laugh and pulled a thick bundle of documents from a drawer.

“I organized them as best I could, but there was an enormous amount of information.”

“What is this?”

“Information regarding the assets and businesses owned by Odin Guild. Of course, a considerable portion of them have not been exposed.”

“You mean they’re in other people’s names?”

“Yes. Legally, they have nothing to do with Odin Guild, but in practice, they were operated as though they were subsidiaries of the Guild. Other major Guilds and corporations commonly use the same method, but the scale itself is on another level.”

I was practically illiterate in this area, but even the thickness of the documents piled up before me gave me a sense of the scale.

I skimmed through the pages, which were filled with words and sentences I could barely understand, until I found the closest comparison.

“More than Ares Guild?”

“You would have to combine Ares Guild and Peace Guild, then add three or four major Guilds on top of that.”

“Holy shit.”

“Just counting the number of Gates Odin Guild has taken charge of, there are more than two hundred across the world. Since they are permanent leases, they are effectively the same as ownership, and an enormous quantity of Magic Gems pours out of them.”

Even if a considerable number of those holdings were controlled through unofficial channels, having control of around two hundred Gates put Odin Guild on the level of a small country.

No—considering the strength of the Hunters belonging to it, perhaps it was even more than that.

*It would have been better if he were just a mad dog.*

To put it coldly, Michael Silbert was not simply a mad dog.

He was a Tosa mastiff among fighting dogs—and he was clever, too.

*But he was also a bastard I absolutely had to beat to death.*

I muttered inwardly, then suddenly thought of something.

“Then is it possible that the Magic Gems from those Gates were used in this terrorist attack without being refined?”

“No. At least not according to the documents.”

“Not according to the documents?”

“As you know, Michael Silbert is an extremely thorough person. He had no reason to take the risk of smuggling Magic Gems, and even if he had, he would not have left any gaps in the records. The Magic Gems used in the terrorist attacks most likely came out of the Middle East or Africa.”

It was a convincing explanation.

The Middle East and Africa had been hotbeds of terrorism and civil war even before the Great Cataclysm, and even now, people there were continuing bloody battles somewhere or other.

No one could know exactly how many Magic Gems came from Gates occupied by terrorists and rebels, or how many of them had been left unrefined.

Moreover, Michael Silbert was not alone.

He had a reliable accomplice who was just as much a mad dog as he was.

“The Prophet.”

At the name that slipped from my mouth, Team Leader Choi nodded with a grim expression.

“I searched thoroughly for information on the Prophet as well.”

“What kind of bastard is the Prophet?”

I was genuinely curious.

Who was the madman who had beheaded the leaders of two massive terrorist organizations, rallied the scattered terrorists, and shaken the entire world?

But the answer I heard from Team Leader Choi fell far short of my expectations.

“We don’t know.”

“You don’t know?”

“No. Even after taking every circumstance into account, there is absolutely no information about the Prophet. The Prophet completely vanished after that declaration as well.”

“Wait. Even the United States?”

“Not just the United States. Even with the entire world searching, the situation is still the same.”

I blinked and thought.

*How was that possible?*

The madman who called himself the Prophet had stirred up not only the United States but the entire world. And yet he had disappeared without a trace, evading everyone’s eyes.

“You’re not hiding what you know to protect classified information, are you?”

“I recently managed to contact Chuck Hagel. He swore to God that he didn’t know where the Prophet was.”

Chuck Hagel, who had fought alongside us in the desert, was not only an S-rank Hunter but also the United States Secretary of Defense.

Unless he was lying, if even the Secretary of Defense did not know, then the Prophet really must have shot straight up into the sky.

*Who the hell is this guy?*

Just as I furrowed my brow, Team Leader Choi continued.

“And there’s one more thing. Mr. Johnson contacted us. He said he had found someone among the other Grand Mages who was likely to have been in contact with Michael Silbert. He said we would probably be able to learn more vital information through that person.”

Fortunately, this time, it was good news.

I had not yet heard the person’s name, but that Grand Mage would have to know something about Michael Silbert’s true nature.

He was a key figure who had personally created Ares Guild’s A Area and knew about Cheon Taemin’s condition.

As one of only three Grand Mages in the entire world, he would become a new clue.

Or so I thought.

That was before I heard Magic Johnson’s voice on a call that came to Team Leader Choi not long afterward.

—Damn it. He’s dead.
## Chapter artifact 741

# Chapter 741

*Damn it. He’s dead.*

I’d thought there was no way.

The unease I felt at that one short sentence over the phone had turned out to be exactly right.

“I’m sorry, but you need to come right away. Before this case slips out of our hands, we need to find as many clues as we can…”

“Where are you?”

There was no time to hesitate.

We followed the coordinates Magic Johnson had given us as quickly as possible, and after attempting several long-distance Teleports in succession, we arrived at a snow-covered mountain, its surroundings bleached white.

*Crunch.*

The everlasting snow covering the ground crumbled beneath my feet.

The breathtaking scenery of the Alps, something I had only ever seen on the internet, unfolded before my eyes. But I had no time to admire the view.

And neither did—

“Intruders spotted!”

—the group guarding the area nearby.

“Hold! Hold!”

“Shooters, ready!”

*Chk-chk-chk!*

At the urgent shouts, gun barrels and blades were pointed at us.

The soldiers and Hunters were heavily armed at a glance. Just as I stopped walking, a familiar voice came from among them.

“If you insist on attacking, I won’t stop you. But before you do, it would be in your best interest to check the intruders’ faces.”

“Take one more step and you’ll be shot immediately… Mr. Johnson?”

“Don’t act rashly, Colonel. They’re guests I invited.”

A massive Black man passed by the middle-aged commander in a beret and stood before us.

His face was deeply marked by fatigue and sorrow.

Magic Johnson, whom I had not seen for several weeks—no, several months—gave us a faint smile and greeted us.

“Long time no see, friends. How have you been?”

I smacked my lips bitterly and firmly grasped the hand he held out.

“Not at all.”

* * *

“Who are the people outside? There seemed to be an even split between soldiers and Hunters.”

“They’re the Swiss Federal Police. This area is under their jurisdiction as well, and I contacted them because I wanted to avoid being treated as a murder suspect simply because I was the first person to discover the body. Come with me.”

Team Leader Choi, the Skeleton King, and I followed Magic Johnson.

We passed between the soldiers and Hunters watching us with wary and curious eyes, then entered a forest buried beneath thick snow. A faint sense of déjà vu washed over me.

*This is…*

I closed my eyes and focused my mind. When I slowly extended a hand, I could feel an invisible ripple amid the fierce snowstorm.

“Mana?”

Magic Johnson nodded at my murmur.

“It’s a barrier. It’s hidden well enough to escape even most S-rank Hunters’ notice, and it’s every bit as flawless.”

There was not a hint of exaggeration in his explanation.

Even the Skeleton King had only barely noticed the barrier after hearing him point it out.

“Not bad for the work of humans. But it is still insufficient to deceive this body’s keen gaze. That is because I am not some ordinary S-rank Hunter, but an exceptionally gifted—”

“A monster.”

“……”

The Skeleton King fell silent, crestfallen.

After shutting him up with a single word, I stared at the barrier before me and recalled something that had happened not long ago.

*It’s similar.*

Just as a particular martial art left behind a specific trace, magic worked the same way.

Looking at the mana currents, as distinct as fingerprints, I became certain.

*There’s no doubt. It feels just like it did in A Area.*

As if he had read the thought that had flashed through my mind, Magic Johnson met my eyes and spoke.

“Even before this incident, I had been looking for people connected to A Area at your request. But among the people I know, only one person came to mind.”

The identity of that person—the great Grand Mage who had designed A Area—was something I now knew as well.

I also knew that he had announced his retirement more than a decade ago and vanished from public view.

“I didn’t expect him to be staying in a place like this. But had you been in contact with that person separately?”

“Not at all. He was an eccentric, and he had a very closed-off personality.”

Magic Johnson answered Team Leader Choi’s question, then added:

“But we were friends. We were close enough that he could at least give me a hint about the hideout where he planned to stay someday.”

*Whoosh.*

Mana mingled with mana, and the snowstorm came to a stop amid a flash of pure white light.

No—the scenery around us had changed.

The vast snowfield was gone, replaced by a long, enormous cave that wound like a maze.

“Follow me. Magic, including spatial movement, can’t be cast inside.”

We followed Magic Johnson as we moved through the cave and continued talking.

And as one might expect, the current situation was not going smoothly for Magic Johnson either.

“You’ve seen the news, so you already know, but our L.A. branch was hit. It was located on the outskirts of the city, but there were so many people coming and going nearby that we couldn’t prevent casualties.”

Magic Johnson was a Grand Mage and the master of the massive Wizard Guild.

Although it had been pushed out of the rankings several years ago, the Wizard Guild had once been one of the world’s top ten Guilds, even if only in last place.

Yet neither the Wizard Guild, with its many mages, nor Magic Johnson had been able to stop the planned terrorist attacks that unfolded with lightning speed.

“By the time I arrived, it was already too late. After that, I was too busy dealing with the other problems to even think straight.”

I did not ask what had kept him so busy.

Everyone present already knew the reason.

The so-called “vigilante incident”: the campaign to eliminate the Middle Eastern terrorists and African rebel groups.

That incident had provided the justification and the means for the current terrorist attacks, and the public had heaped blame upon it. Magic Johnson, who had been one of the vigilantes, could not escape that condemnation either.

No. None of us could.

It was simply that I was the one who had taken the largest and heaviest blow from the media.

“I’m sorry.”

“What?”

“I thought I should at least apologize. If I hadn’t stepped forward and made that proposal, we wouldn’t be getting cursed out by the entire world like this…”

“Damn it. So that’s what you were talking about.”

Magic Johnson abruptly stopped walking and shook his head.

“Listen, Jin. This isn’t your fault. You don’t need to apologize to me, either. Understand?”

“Of course, but—”

“Let me ask you one thing. If you could go back to that time, what choice would you make? Would you have left those bastards alone?”

I did not need long to think.

It was a question I had considered over and over in a room where not even light could enter.

“No.”

“What about you two?”

Team Leader Choi and the Skeleton King looked at each other, then spoke almost simultaneously.

“Nothing would change. If anything, I might have dealt with them even more decisively.”

“This body will kill that bastard called the Prophet without fail.”

“Good. We have clear answers.”

Magic Johnson shrugged at the two different but identical answers.

“And I’m saying this just in case, but no matter what people say about that incident, I don’t regret it in the slightest. Chuck Hagel feels the same way, even though he isn’t here right now.”

Chuck Hagel.

The image of him beating down terrorists despite suffering from cigar withdrawal rose before my eyes.

According to what Team Leader Choi had briefly told me on the way here, he was going through more than a little trouble as well.

“How has Chuck been lately?”

“Not well.”

“That answer came awfully fast.”

“Because it’s true. The external and internal pressure coming down on him is tremendous. At this rate, it wouldn’t be strange if he were dismissed from his position as Secretary of Defense before long.”

Team Leader Choi spoke in a calm voice.

“The pressure must be so intense that even the President can’t shield him.”

“It’s a different matter for him than it is for you. Chuck Hagel is a high-ranking government official of a country—even the Secretary of Defense of the United States. Even if our actions were something the President had tacitly approved, that only applied as long as they remained undiscovered.”

“But the entire world found out. And it was revealed directly by a terrorist of historic proportions called the Prophet.”

“……Yeah. Thanks to some damn traitor.”

The operation had been carried out with the tacit approval of the President of the United States.

Under normal circumstances, the vigilantes’ mission should never have become known to the world.

That belief was the reason I had been able to act so boldly in the modern world, where countless restrictions existed.

Interfering with the satellite surveillance system and destroying every related record.

But information about us had leaked out in plain sight, and I vividly remembered what Michael Silbert had said amid the ruins of Paris.

*I’ll give you one piece of advice. There are no perfect secrets in this world. Not even if it’s the Pentagon.*

The United States was still the most powerful nation in the world, and the Pentagon was the United States Department of Defense headquarters, renowned for having the tightest security in the country.

And yet information that should have been classified even within the Pentagon had leaked to the outside.

It had happened so easily.

But…

*If it was him, it wasn’t surprising.*

I was accepting reality with a surprising degree of calm.

Because the opponent was Michael Silbert. He was stronger than any Hunter I had ever encountered—and even more insane than he was strong.

And on top of that, there was the unidentified madman called the Prophet.

*An ordinary person couldn’t do something like this. No—no person could even attempt it.*

Even evil had its limits.

In that sense, the path those bastards had taken had already crossed the line by an absurd distance.

Thousands of people had already died, and more than ten times as many had been injured.

Not every crime committed throughout the world over the course of the week—including the day the Paris branch collapsed—could have been their doing, but it was obvious that they had exerted a considerable influence.

Fear paralyzed reason and summoned even more madness.

Along with the ten terrorist attacks accompanied by Monster Waves, the mana distribution continued to rise at an even steeper rate, and mutation Gate phenomena were now occurring dozens of times a day.

Some terrified people were already speaking of the end of the world. With crosses hanging at their waists and microphones in their hands, they shouted about God’s mercy at the top of their lungs in the streets.

Just as their parents had done a very long time ago.

But I did not search for God.

They were not devils, but mere humans, and I was ready to bring them down.

There was only one problem…

*The thread leading to one of them had been severed just like that.*

As I muttered inwardly, I stopped walking. At some point, the long, winding passage of the cave had come to an end.

And waiting for us at the end was a corpse.

Every bone and scrap of skin on its body had dried up and shriveled tight, like a mummy.

“……What is this?”

Team Leader Choi’s voice reached my ears, escaping like a groan.

At that moment—

*Chime.*

> **System**
>
> **A new Quest has been generated!**

The clear ringing of a bell echoed more ominously than ever.
## Chapter artifact 742

# Chapter 742

> **System**
>
> A new Quest has been generated!
>
> An Unexpected Quest, Unknown Death, is being forcibly accepted!
>
> **Quest**
>
> **Unknown Death**
>
> The reclusive Grand Mage, Siegfried Wassmann, has died for an unknown reason.
>
> Yet everything has a cause.
>
> Discover how and by whom he was killed.
>
> **Grade:** Supreme Peak
>
> **Restriction:** Jin Taekyung
>
> **Mission:** Reveal the truth behind his death (Incomplete)
>
> **Reward:** ???
>
> **Failure:** ???

I stared at the Quest window floating in midair.

The name of the deceased in the first line of the description told me that this corpse, which had met such a gruesome end, belonged to one of only three Grand Mages in the entire world.

*Siegfried Wassmann.*

Also known as the “Hero,” Siegfried.

The greatest Hunter Switzerland, a perpetually neutral nation, had ever produced—and a Grand Mage who had displayed exceptional talent in summoning and barrier magic.

If Magic Johnson was a War Mage specializing in actual combat and killing, Siegfried was one of the few scholarly mages who had delved deeply into magic itself.

At least until today, when he was found dead in his own hideout.

“Was he already like this when you first arrived?”

At my question, Magic Johnson nodded somberly.

“Yes. At first, even I had trouble believing it. It was only after checking several times that I realized the corpse was Siegfried.”

“What was your usual contact like?”

“After he went into hiding, we only contacted each other once or twice a year. Even then, I had to call him about ten times before he would answer, usually much later. This is my first time coming here. He was so reclusive that he absolutely hated that kind of visit.”

“Then your last contact was…”

“Hmm. Probably around three years ago.”

“Three years ago. I heard it’s been nearly ten years since he disappeared.”

“When we met shortly before his retirement, he gave me a communications artifact he had made himself. He told me to use it if anything truly urgent came up.”

I accepted the artifact Magic Johnson pulled from inside his clothes.

As if to prove that a Grand Mage had made it himself, the object radiated a considerable amount of mana. It was a crystal ball roughly the size of an adult’s fist.

*Of course. Normal radio signals and communications would have been impossible inside a space surrounded by layers upon layers of barriers. He probably intended it that way.*

I had never met Siegfried Wassmann face-to-face, but his public reputation was that of an unmistakable shut-in.

On top of that, he avoided people’s attention and interest to an extreme degree, and whenever he became interested in a subject, he was the kind of obsessive who had to pursue and dissect it to the very end.

“I reached out every Thanksgiving and Christmas, but starting three years ago, he stopped replying. I knew what he was like, so I didn’t think much of it. He was uncomfortable with people praising him as a hero, and he hated the media’s attention. Even after the Great Cataclysm ended, he would sometimes bury himself in long-term research.”

I could not make sense of it.

A Grand Mage who had vanished from the public eye to escape people’s attention had died in such a horrible state inside his own hideout.

But one thing was certain.

“This wasn’t an ordinary natural death. Even if he died for some reason, a corpse couldn’t change this much in only three years.”

Maybe it would have been impossible even after three hundred years.

Would the hideout of a shut-in Grand Mage whose hobby was magic research and whose special talent was staying home run on gas or electricity?

This enormous cavern, which could only be entered by breaking through its barriers, was filled with all kinds of magic. Everything, from the temperature to the humidity, was controlled perfectly.

Besides, the corpse of Siegfried lying in front of me showed no trace of the natural rot or stench one would expect from decomposition.

*It’s simply… dried out. As though something had sucked away all its life force.*

I had never witnessed a death this mysterious, not even in the Murim.

That only made me wonder even more.

How exactly had he met his end in his own hideout?

How closely was the death of this Grand Mage connected to my enemies?

“Michael Silbert. And The Prophet.”

The two most likely suspects.

Magic Johnson realized what my mutter meant and spoke in a grave tone.

“If I had to choose between the two, I’d pick the former without hesitation.”

“Why?”

“Because there’s a definite connection between him and Siegfried, at the very least. Judging from everything that’s happened so far, Michael Silbert clearly knows that Sky is unconscious. Otherwise, there’s no reason he would join hands with terrorists and carry out something this insane.”

It was a sufficiently credible hypothesis.

Siegfried had created A Area, which had been hidden inside Ares Guild’s headquarters. There was a strong possibility that he had learned the truth about Cheon Taemin’s condition in the process.

But…

“I’m asking because I don’t know, but was Siegfried close to Michael Silbert when he was alive?”

“That…”

“Then what are the chances that he would have revealed that level of classified information to him?”

Magic Johnson hesitated briefly, then let out a low groan.

“Not very high. No, you could consider them nonexistent. There were very few people who had any kind of relationship with him, myself included. And beyond those mere connections, there was only one person Siegfried openly said he genuinely respected.”

I felt as though I already knew the name without hearing it.

“Cheon Taemin.”

Magic Johnson nodded to confirm it, then continued.

“That’s right. Siegfried genuinely respected Sky. From the conversations I had with him about Sky, his feelings were practically close to worship. In the past, he even mentioned Sky himself during an interview with the media.”

“Oh. I think I know what you mean.”

I had a faint memory of seeing that interview myself.

With famous Hunters, all kinds of information about them had been compiled into documents online, and Siegfried Wassmann had been one of them.

It was unusual for him to give an interview to the media, and even more unusual for him to express that degree of admiration and emotion toward someone else. I heard it had made major headlines at the time.

“Perhaps… that’s why Lee Jungryong commissioned Siegfried to build A Area.”

Team Leader Choi spoke up suddenly, then continued slowly.

“Siegfried Wassmann was a master in that field, and he had very few personal relationships. On top of that, he deeply respected my maternal grandfather. He would have kept the secret.”

Magic Johnson gave a small nod.

“That’s true. Even I, who was among the people closest to him, knew absolutely nothing about A Area. No, I never even imagined that friend of mine would accept a commission from anyone.”

“At least when it came to maintaining secrecy, Lee Jungryong’s judgment was accurate. But if the information wasn’t leaked, the question that remains is…”

“How did Michael Silbert learn about it?”

I muttered the question and examined the corpse thoroughly once more.

I was looking for any possible signs of torture, but even after examining it with every sense on high alert, nothing about the facts changed.

*If this wasn’t simply a lizard shedding its tail, then there had to be a reason he needed to be killed.*

I had no clear proof, but Michael Silbert was still the most likely suspect by far.

Uncovering the truth would be the first step toward bringing him down.

*There’s definitely something here. Something…*

I continued to examine the corpse while repeating the thought over and over in my mind.

After a long while, I raised my head in frustration—and saw someone standing there.

More precisely, it was a monster shaped like a human.

“Why are you standing over there trying to look cool? You’ve been quiet for a while.”

The Skeleton King, who had been standing with his arms crossed and thinking deeply about something, furrowed his brow.

“Be silent, foolish human. This body was engaged in profound contemplation.”

“What kind of bullshit were you thinking up this time?”

“Can you not feel it?”

I paused and asked him back.

“What?”

“This space. The concentration of magical power is denser here than elsewhere.”

If the Skeleton King had been talking about mana, I would have immediately argued with him.

My Qi Sense was better than anyone else’s here, and I had not felt anything strange so far.

But if he meant magical power, that was a different story.

The Skeleton King was an S-rank monster in the truest sense. When it came to magical power, even I could not match him.

“Large human. You did not feel it?”

At the Skeleton King’s question, Magic Johnson scratched the back of his head.

“Not as well as you, but I did feel it. I just didn’t think it was particularly strange.”

“You are infinitely more foolish than this body. Why?”

“This isn’t just a house. It’s also a laboratory equipped with everything Siegfried could want. You could rummage through a single storage room and find mountains of monster corpses and Magic Gems.”

“…Huh?”

Now that he mentioned it, he was right.

Just as filtering shit water wouldn’t make it perfectly clear, the same was true of Magic Gems and monster corpses.

No matter how thoroughly they were purified, some magical power always remained.

Siegfried’s hideout was filled with objects that held all kinds of magical power. The concentration here was bound to be denser as a result.

“I understand what you’re thinking, but the monster corpses being the reason for the high concentration of magical power doesn’t change anything. Even if a monster killed Siegfried, there should at least be signs of a battle.”

“…Huh? Huh?”

I was an idiot for getting my hopes up.

As the Skeleton King blinked at Magic Johnson’s logical rebuttal, I muttered quietly.

“Fucking stupid bastard.”

“How dare this treacherous human insult whom!”

“Be quiet before I separate your jawbone. I’ll overlook it because you at least managed to think about something.”

“…”

“Who do you think you are, throwing the investigation into confusion? My head already feels like it’s about to explode.”

The demon realm was far away, but my fist was close.

Just as the Skeleton King shut his mouth with an offended expression, Team Leader Choi, who had been examining the corpse persistently, clicked his tongue.

“If this was an assassination, there should at least be some kind of injury. But there are no wounds on the corpse. It’s completely clean.”

“Then…”

“At least as far as common sense goes, that leaves only magic.”

But Magic Johnson, a Grand Mage himself, looked troubled.

“Even though I specialize in offensive magic, I’ve truly never seen or heard of magic like this. It’s far more complicated and sinister than the ordinary magic we use. For example, it’s closer to that fellow’s kind of magic.”

At that, the “fellow” who had kept his mouth firmly shut frowned.

“This body merely infuses resentful spirits into dead flesh. This body knows nothing of such wicked magic.”

“…”

“…”

“…”

*Wasn’t that already fucking evil magic?*

But since he said he did not know, what could I say? Besides, he was quite unlike an ordinary monster, so he had no reason to lie.

*Damn it. It has to be him.*

Michael Silbert.

That name alone kept circling through my mind.
## Chapter artifact 743

# Chapter 743

A space permitted to only one person.

In the light that faintly illuminated the darkness, an eerie sound of flesh tearing echoed through the air.

*Crack. Crack-crack.*

Bones and muscles twisted. A tremendous force surged in time with the beating of a heart, bringing about a transformation.

The weak became strong.

The strong became stronger still.

The entire body of the man, his veins standing out prominently, was already drenched in cold sweat. A thin line of blood slipped from between his tightly pressed lips and ran down his chin.

*Drip.*

Drops of blood fell one by one.

And yet, despite the terrible agony that seemed to squeeze every inch of his body dry, there was no trace of fear or pain in the man's gray eyes.

For this pain, which was worse than death to some, was already familiar to him.

The reward for enduring pain was always sweet.

Just like now.

*Hssssss.*

The sound of flesh tearing abruptly stopped.

At the same time, the energy churning wildly within him quickly settled down.

The veins that had stood out so grotesquely across his body gradually receded, and the muscles that had convulsed naturally in response to the stimulation stopped trembling as well.

And once again, the man received his “Reward.”

*Whoosh—boom!*

In the blink of an eye.

A tremendous qi wave erupted from the man's body and swept in every direction.

The light that had faintly illuminated the space vanished, and everything within a radius of more than ten meters crumbled like dust.

It was power.

Overwhelming power.

Just as the man, Michael Silbert, lifted the corners of his mouth after confirming the change that had taken place within him—

*Vrrrrr.*

A faint vibration reached him from somewhere.

Michael knew exactly what that vibration meant. Without hesitation, he rose from his seat.

When he silently extended a hand, a hidden door opened, and light poured out from beyond it.

*Step. Step.*

His footsteps were powerful enough to make what had happened moments earlier seem unreal.

He slowly crossed his study, which was not merely large but vast, and stopped in front of a huge mirror.

The full-length mirror glowed as it faintly vibrated.

Michael stared at his reflection in the flawless surface, then placed a hand against it.

*Tap.*

And in the next moment—

*Flash!*

With a brief glimmer of light, everything within the mirror changed.

Michael and the scenery inside the study disappeared without a trace. In their place, the mirror's surface filled with an endless horizon, slowly moving buildings, and a single figure.

Dark skin and golden eyes. A silk top hat and a monocle, both rarely seen in this day and age.

Michael greeted his loyal retainer, who had been with him for a long time.

“You’ve been working hard, Huginn.”

Huginn lifted his silk top hat slightly upon facing his superior.

“Not at all, Guild Master.”

That was enough of a greeting.

As if they had planned it in advance, the two of them moved straight to the point.

“One hour ago, the Swiss Federal Police recovered Siegfried Wassmann’s corpse.”

“What about those bastards?”

It was a short question, but there was no need to wonder whom he meant.

Huginn immediately reported what he knew.

“They were all released after undergoing only brief questioning as witnesses. If we make every effort, we may be able to drag them as far as the International Court of Justice, but I doubt we can go any further.”

“That conclusion wasn’t based solely on your own judgment. Where did the information come from?”

“First of all, within Switzerland, Minister Berse.”

“Berse?”

At the name of the Minister of the Interior, whose election as Switzerland’s president next year was considered almost certain, Michael calmly nodded.

“Then there’s no need to hear any more. It would be best to wrap things up at an appropriate point.”

“I agree with you, Guild Master. However, considering the circumstances, I think it might also be worthwhile to keep pursuing the matter to the very end.”

“To somehow throw them into a pit of filth?”

“Shouldn’t we grab them by the collar and throw them in? The moment this becomes known, the eyes of the entire world will turn toward it, and many people will question the death of Siegfried Wassmann, whose cause of death remains unknown. If that happens…”

“All sorts of conspiracy theories will run rampant. They’ll become the primary targets of those theories.”

“Yes. Under the current circumstances, wouldn’t that have a considerable effect?”

But Michael shook his head without hesitation.

“The essence of a conspiracy theory is ultimately nothing more than absurd nonsense. Only idiots obsessed with gossip and filled with fantasies would suspect them.”

Siegfried Wassmann was a major figure who possessed tremendous stature not only in Switzerland but throughout the entire world.

Using his death to spread conspiracy theories about his enemies would have been easy for Michael, but it was obvious that doing so would backfire.

If he forcibly dragged his enemies into a pit of filth, some of that filth would splash onto him as well.

“Most of the public won’t even give it the time of day. Some may even begin to suspect that the series of circumstances surrounding them was contrived. The people cursing them today will turn around tomorrow.”

As far as Michael knew, that was simply what human beings were like.

They were quick to condemn someone after being deceived by one tiny false aspect, then quickly changed their attitude once the whole truth came to light, gently embracing the person they had cursed.

As though nothing had happened.

As though the entire world had cursed him, while they alone had not.

And that was not the development Michael wanted.

The structure of this scenario, whose conclusion was still uncertain, was one thing. More importantly, its central character was missing.

*Jin Taekyung.*

A name that lingered at the tip of his tongue.

Siegfried Wassmann’s death could be used to pressure Magic Johnson, at most.

Of course, even that possibility was slim. Unless he brought down Jin Taekyung, who stood at the center of everything, it would amount to nothing more than wasting his energy.

“Withdraw from the Swiss matter. There’s nothing to gain.”

Huginn answered Michael’s calm but firm order.

“Understood. I’ll relay that to Minister Berse as well.”

“That will be enough. How are things with the media outlets progressing?”

“Successfully. We added firewood, and they flared up. However, there is something I need to report concerning that…”

“Money?”

“Yes. They’ve demanded a much larger amount than we expected.”

“They’re greedy. What they’ve already received should have been more than enough.”

“That’s why I consider it fortunate. All we have to do is give them as much as they want.”

Michael let out a quiet laugh at Huginn’s answer.

He was right.

If you satisfied the size of someone’s greed at the right moment—no, if you gave them something that exceeded even that greed—then they would never betray you.

“I’ll hand some of my secret accounts over to you. Take whatever you need.”

“May I understand that as an order to give them enough to make them gasp?”

“Exactly. You’ve become quite the villain.”

“I learned a great deal from a certain someone.”

“There’s an interesting saying among Easterners: ‘When three people gather, they can make a tiger.’[^1] Keep the media under control until everything is finished. Just as you are now.”

“I’ll keep that in mind.”

Michael knew the power of the media.

He also knew how shallow and terrifying the psychology of a crowd could be.

At the same time, part of him found his own situation ridiculous for having to go this far.

*I was certain that no one except Cheon Taemin could stop me now.*

The Ares Guild, once called the best in the world. Lee Jungryong, who had filled the void Cheon Taemin had left behind. Even the heroes of the Great Cataclysm, including Magic Johnson.

None of them had been Michael’s match.

Until Jin Taekyung appeared.

*How is that even possible?*

Michael simply could not believe it.

It had taken Michael—a young man from the slums with nothing to his name but poverty—a very long time and immense patience to reach his current position.

But Jin Taekyung had been different.

He had suddenly risen to prominence one day, then built up tremendous achievements and Fame in barely more than a year, winning the love of the entire world.

Just like someone from the distant past who remained vividly etched in Michael’s memory.

*Sky.*

One week ago, Michael had sensed a trace of Cheon Taemin in the young Asian man he met for the first time in the ruins.

His appearance and the impression he gave off had been different, but his instincts had shouted at him.

*This man is dangerous.*

*He’ll become the greatest obstacle standing in my way.*

And Michael’s instincts had been correct.

Even now, while countless media outlets poured out every kind of malicious news, voices supporting Jin Taekyung had not stopped.

The people swept up in the fear caused by the terrorist attacks and the mob psychology planted by the media were simply louder. Jin Taekyung himself was still standing.

*But if my guess is correct… it’s only a matter of time before he falls.*

Michael thought to himself as he recalled Jin Taekyung’s eyes, blazing with rage.

And someone who had been standing beside him.

One step.

Only one step remained before he reached the high ground he had longed for so desperately, and in his hand he held the flag that would announce he had seized it.

“Huginn.”

Huginn, who had silently waited for his superior while Michael was lost in his thoughts, answered.

“Yes, Guild Master.”

“There can be no mistakes or unforeseen complications in this mission.”

“Don’t worry. I handled everything flawlessly, exactly as you ordered.”

Michael smiled at the immediate answer from his loyal retainer, the man with whom he had spent so many years and shared so many secrets.

“Good. That’s all that matters.”

“I will not disappoint you.”

The one who had given the order.

And the one who had carried it out.

Both men knew what consequences their actions would bring.

They also knew that countless people would die or be injured in the process.

But to Michael, that was only a very small part of the whole.

An unavoidable sacrifice that had to be paid to reach the destination he had longed for so desperately.

If he could obtain what he wanted, then the sacrifice of those who would die somewhere in this vast world was an absurdly cheap price.

* * *

*Crash!*

The magically treated glass shattered in an instant.

The countless fragments that had been a communications crystal ball only moments earlier were swept away somewhere by the wave that came after.

*Whooosh.*

Wind swept across his entire body.

Standing tall at the stern, Huginn gazed silently at the rolling seawater.

*Three days at the latest. It’ll probably begin by then.*

What he had thrown into the depths of the sea was not merely the fragments of the communications crystal ball. The result would soon be revealed before the eyes of the entire world.

*The calculations were perfect. The mission was a success.*

There was no guilt.

Only the sense of accomplishment that came from having carried out his orders perfectly—and a small, unresolved question.

*Can this really bring him, Jin Taekyung, down completely?*

But Huginn soon shook his head.

The superior to whom he had pledged his loyalty was always meticulous, and the path he chose had always been the correct one.

“We’re heading back. Make preparations.”

At Huginn’s brief command, the ship changed direction.

Behind the slowly receding ship, Tokyo’s forest of buildings rose high into the sky.

[^1]: A proverb meaning that repeated rumors can make people believe something untrue.
## Chapter artifact 744

# Chapter 744

A thought suddenly occurred to me.

I wished that everything tormenting me right now was merely a scene from some movie or novel. Something like that.

*Then at least some evidence would pop up somewhere.*

Of course, contrary to the hope I had secretly been holding on to, nothing of the sort happened.

Everyone, myself included, searched every inch of Siegfried Wassmann’s hideout, but what popped out wasn’t evidence concerning his death. It was a person.

More precisely, it was over a hundred Hunters from the Swiss Federal Police who had followed us and arrived late.

“Everyone, please stop.”

“From this point on, we will take control of the scene according to legal procedure. Put down whatever you’re holding immediately and…”

Well, what else could we do?

If they had abruptly pointed swords at us, I would have answered with my spear. But they were carrying out official duties, and instead of swords, they had thrust forward the invincible cheat code known as legal procedure.

Even unorthodox swordsmen who reached for their weapons whenever things went slightly wrong tended to hesitate in front of government soldiers.

And as a twenty-first-century modern man with a logical mindset, my answer had been decided from the start.

“Are you going to put us in handcuffs too?”

“…Excuse me?”

“Actually, that might be going a little overboard. So what do we do now?”

With countless media outlets currently hurling every curse imaginable at me while praying for my long and healthy life, causing another incident would have been insane.

My companions and I cooperated so obediently that even the Swiss Hunters were surprised. After undergoing a thorough body search and brief questioning, we were released.

That came with a single remark from a high-ranking official who introduced himself as the person in charge of the investigation.

“Additional investigations related to this case will be conducted, so we ask for your continued cooperation in the future.”

That was all.

We hadn’t done anything in particular that they could hold against us, but even so, their matter-of-fact response was quite unexpected.

According to Team Leader Choi’s investigation, Michael Silbert’s influence reached the leadership of countries all over the world. Switzerland, in particular, was a tax haven for his astronomical wealth.

*I was sure that bastard would use Switzerland to pressure us somehow.*

And Team Leader Choi neatly cleared up the question I had raised.

“They deliberately let us go. Since it was clear that neither the evidence nor the circumstances had anything to do with us, they must have judged that pursuing the matter any further would be difficult.”

“That bastard Michael let us go on purpose? Just getting dragged into this case would already hurt us.”

“The public is fickle. Right now, quite a few people are cursing us because they’re being controlled by the media and mob psychology. But that’s because The Prophet and terrorism provide a plausible justification at first glance.”

“And if the justification isn’t convincing, the public won’t let itself be fooled?”

“Human beings have acted according to justifications for thousands of years. But if such an important justification begins to waver, many of the people who were criticizing us will change sides.”

“Oh.”

Come to think of it, that was a pattern people displayed often—no, quite frequently.

You could see it everywhere just by looking at the entertainment news posted on online portals.

Whenever a celebrity became embroiled in controversy, countless netizens swarmed them like bees and clung to the honey dripped by the media.

There were the genius prophets who claimed they had known it would happen ever since the celebrity’s debut, and even twenty-first-century physiognomists insisting that face-reading was a science.

And around the time the winner of that world’s greatest malicious-comment contest was crowned by upvotes, a new fact would emerge and turn the situation around, and the swarm would change its tune in an instant.

Why did they do that?

It was simple.

*Because they no longer had an excuse to keep cursing them.*

This incident surrounding Siegfried Wassmann’s mysterious death was exactly that kind of case.

Michael Silbert had seen through human psychology and knew precisely when to move forward and when to stop.

“Michael is, in a word, a mad bastard.”

Magic Johnson abruptly broke the silence in a subdued voice.

“But the biggest reason we need to be wary of him is that this mad bastard is more meticulous and stronger than anyone.”

The Skeleton King also spoke with a grave expression that was rarely seen on his face.

“I agree. When I first saw that bastard in Paris, I felt something so eerie that it was difficult to believe he was human.”

Most madmen ended up in prison or a mental hospital.

But when a madman like Michael had everything, the world called him by another name.

The powerful.

Among those I had met in the modern world, Lee Jungryong had been one. Even Go Jun, who was inferior to his Master in many ways, was more than strong enough to belong among the powerful.

But that bastard…

He had already gone beyond that category.

A madman you’d get only by adding those two together—and then multiplying them.

Michael Silbert was a monster who had given up on remaining human.

*Why? What could he possibly want to go this far?*

I raised my head with those questions in mind. The sky was clear as hell, and the surrounding scenery, which still retained the beauty of northern Europe, was beautiful in contrast to the situation we were in.

*Fuck.*

I muttered a quiet curse inwardly, then pulled a small pouch from inside my clothes and handed it to Magic Johnson.

“Here.”

“This is… a subspace pocket.”

“Don’t open it now. Take it with you and examine it carefully. Team Leader Choi and I are both hopeless with magic, so we wouldn’t understand much even if we looked at it.”

“Magic? Jin, what are you suddenly talking about?”

Magic Johnson wore a bewildered expression, then suddenly realized something and opened his eyes wide.

“Don’t tell me…”

“Yes. I slipped it out earlier. I’m sure the deceased will understand.”

“…”

“…”

“…”

The three people standing there with their mouths hanging open—or rather, two people and one monster—made me let out an exaggerated sigh.

“Your reaction is pretty disappointing. Should I just return it now?”

Snatch.

Magic Johnson grabbed the subspace pocket and stammered.

“N-no, that’s not what I meant. But how did you…”

“The Hunters assigned to me were pretty lax with their body search.”

Team Leader Choi, who had been blinking silently, asked, “They were lax?”

“Yes.”

Naturally, that was a blatant lie.

A Grand Mage’s magical research materials were incredible treasures in and of themselves.

The Swiss Hunters had thoroughly searched the subspace pockets we carried, worried that even one of the materials might be smuggled out.

They just hadn’t searched my Inventory.

*More precisely, that would have been impossible from the beginning.*

The moment I gave up on finding evidence in the corpse, I began sweeping up every kind of material I could find.

Anything that seemed even remotely useful. I took it all without discrimination.

And the result of that theft was the subspace pocket currently in Magic Johnson’s hands.

“We didn’t notice a thing. When on earth did you get all this?”

“I told you. Their surveillance was lax, so I secretly slipped it out.”

“You secretly slipped it out?”

Magic Johnson opened the pocket and checked its contents before muttering,

“…Jin, you didn’t steal the entire laboratory, did you?”

“…”

“…Jin?”

Well. I had picked up this and that, so I had brought quite a lot.

Of course, everyone had been so distracted, and there had been mountains of documents besides these, so it probably wasn’t obvious.

*Probably.*

“Anyway, is that enough material?”

“Enough? Is that even a question? It’s more than enough.”

“Then please investigate it based on those materials for the time being.”

“But with the situation as it is, focusing only on the investigation… No. I’ll do my best. If we can find even the smallest clue in these materials, Michael won’t be able to run wild like this.”

I nodded.

“Please do.”

The distribution of magical power had amplified once again, causing even more damage to occur.

Magic Johnson taking an active role in dealing with the damage would obviously be a great help, but we had to solve the fundamental problem before that.

“We’ll gather information through other channels. If we can determine even one person’s whereabouts, we may be able to prevent the worst-case scenario.”

At Team Leader Choi’s words, Magic Johnson answered with a sigh.

“The Prophet.”

“Yes. If even one of the two heads disappears, the situation should improve considerably.”

“Eliminating The Prophet would be ideal. We have Jin on our side, so if we can find out where he is, he’s as good as dead. The problem is…”

“I know. I heard that even the Pentagon hasn’t determined his location yet. But we have to try somehow, don’t we?”

Michael Silbert and The Prophet.

The Prophet and Michael Silbert.

They were two madmen who moved as though they were one body, but The Prophet was a much easier target for me to eliminate.

If I killed the master of the world’s greatest Guild, I’d be a fucking bastard on par with Demon King Asmodeus. But if I brought back the head of a mad fanatic terrorist, the entire world would cheer.

“We have to find him.”

I added calmly, but with anger in my voice,

“Even if we have to turn over the entire desert.”

* * *

The civilization humanity had built was magnificent.

The sight of people cheering after discovering fire for the first time in the distant past could no longer be found anywhere.

Those groups that had once wandered from place to place eventually formed agricultural societies. Before long, they built factories over the land once filled with fields and rice paddies, completing the modern world with countless tons of steel and blood.

Humanity, once the weakest of all, had thus become the master of this blue planet.

They flew through the sky at speeds faster than light, ventured into space, and even used the weapons born from that process to kill one another.

Humanity was the ruler of this land, its people, and an explorer forever moving forward.

But even humanity could not accomplish everything.

There were unknown realms that humanity had been unable to reach despite hundreds of millions of years passing—realms that could not be explored even with the power of magic.

One was the universe, which contained infinite space. The other lay deep beneath the sea, where even light could not reach.

The deep sea.

Even adventurers who had discovered the five oceans and six continents and reached into the domain of outer space had never set foot there. It was still filled with countless speculations and secrets.

No—perhaps it was a secret that should never have been pried into.

*Sssrrk.*

Something enormous moved.

Hundreds of deep-sea fish that had mistaken it for part of the terrain and wandered nearby were unable to withstand the power contained within it. They were torn in half.

*Crack.*

At that moment, the darkness of the deep sea, where even light could not reach, swallowed the red blood.

*Hssss.*

A faint light spread beyond the darkness.

Each time the scales covering something enormous, several meters in radius, shifted, the surrounding space alternately brightened and darkened.

Finally, the center of the light shone clearly.

But it was not some luminous organ possessed by a few deep-sea fish. It held a power that could not even be compared to them.

It was an eye.

The eye of a creature so enormous that it was difficult to believe.

A monster everyone had believed had disappeared long ago had awakened, transcending an unfathomably long span of time.

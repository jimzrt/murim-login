# Checkpoint Review — 345–349

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

# Chapters 345–349

## Plot

Jin Taekyung obtains the Sichuan Tang Clan’s Myriad-Poison Ring from Tang Sadok after offering to help pursue Tang Taesang’s killer. The ring completes the treatment requirements for Jeok Cheongang, and the Divine Physician begins a fifteen-day treatment in the deepest cell of the Tang Clan’s underground prison. Taekyung recognizes Jeok as his Master and guards the treatment room.

The Western Heaven Demon Lord, a one-armed middle-aged man, massacres Tang Clan personnel, reveals that he killed Poison King Tang Taesang and the Heaven-Shaking Venerable Nun, and summons hundreds of black-robed hunters through a concealed Mystic Gate Formation. The Qilian Three Fiends submit to him as he prepares to hunt Emei, Qingcheng, and the Sichuan Tang Clan.

On the fourth day of treatment, Taekyung encounters the Heavenly Power Demon, an elderly prisoner who has spent more than forty years in the Tang Clan’s underground prison. The Heavenly Power Demon was formerly an Elder and commander of the Great Heavenly Demon Divine Cult, led the conquest of Qinghai, and opened the first front of its holy war. He explains that the Great Faction War was morally complicated, that the Divine Cult survived in diminished form in the Tianshan Mountains, and that its former Cult Leader became corrupt. Taekyung begins clarifying that the Yin-Yang Twin Ghosts later served Dark Heaven, but Cheongpung interrupts.

## Continuity

- The Divine Physician and Mungyeong are on day four of a fifteen-day treatment of Jeok Cheongang using the Myriad-Poison Ring and Cold-Ice Stone.
- Jeok remains unconscious and critically ill with Formless Ultimate Poison. Taekyung recognizes him as his Master and is guarding the treatment room.
- The Myriad-Poison Ring is in Taekyung’s possession, but Item Appraisal still requires an unknown special condition.
- The Western Heaven Demon Lord killed Poison King Tang Taesang and the Heaven-Shaking Venerable Nun, losing one arm in the process.
- The Western Heaven Demon Lord commands hundreds of black-robed hunters and intends to attack Emei, Qingcheng, and the Sichuan Tang Clan. The purpose and identity of the Lord of Heaven he invokes remain unresolved.
- The Qilian Three Fiends have submitted to the Western Heaven Demon Lord.
- The Heavenly Power Demon remains imprisoned with a ruined dantian, severed limb sinews, and heavy restraints.
- The Heavenly Power Demon’s account establishes that the Great Heavenly Demon Divine Cult survived the Great Faction War in a diminished state and was driven into the Tianshan Mountains; its former Cult Leader became corrupt.
- The Yin-Yang Twin Ghosts later served Dark Heaven rather than participating in the Demonic Cult’s attack on Shaolin.
- Venerable Myoryeong remains under treatment for the Black Hand Seal.

## Translation Decisions

- Use **Myriad-Poison Ring**, **Cold-Ice Stone**, **Western Heaven Demon Lord**, **Qilian Three Fiends**, and **Heavenly Power Demon**.
- Use **Great Heavenly Demon Divine Cult** for 대천마신교; render 천마신교, 신교, and 본교 contextually as **Heavenly Demon Divine Cult** or **Divine Cult**.
- Use **Yin-Yang Twin Ghosts** and **Yang Ghost** for 음양쌍귀 and 양귀, keeping them distinct from **Yin-Yang Twin Freaks**.
- Use **Heaven-Shaking Venerable Nun**, **Mystic Gate Formation**, **Emei Sect**, and **Sichuan Tang Clan**.
- Preserve the Heavenly Power Demon’s gruff formal self-reference as **this old man**.

## Durable state

{
  "active_continuity": [
    "Jin Taekyung possesses the Myriad-Poison Ring, but Item Appraisal says a special condition is required to appraise it.",
    "The Divine Physician and Mungyeong are on the fourth day of a fifteen-day treatment of Jeok Cheongang using the ring and Cold-Ice Stone in the deepest underground prison cell of the Sichuan Tang Clan.",
    "Jeok Cheongang remains unconscious and critically ill with Formless Ultimate Poison, and Jin Taekyung recognizes him as his Master while guarding him.",
    "Venerable Myoryeong remains under treatment for the Black Hand Seal.",
    "The Western Heaven Demon Lord is a one-armed middle-aged martial artist who killed the Poison King and the Heaven-Shaking Venerable Nun.",
    "The Western Heaven Demon Lord commands hundreds of black-robed hunters summoned through a concealed Mystic Gate Formation and intends to hunt Emei, Qingcheng, and the Sichuan Tang Clan.",
    "The Qilian Three Fiends from the Qilian Mountains have submitted to the Western Heaven Demon Lord.",
    "The Heavenly Power Demon is imprisoned in the Sichuan Tang Clan's underground prison with severed limb sinews, a ruined dantian, and heavy restraints after more than forty years of captivity.",
    "The Heavenly Power Demon was once an Elder and commander of the Great Heavenly Demon Divine Cult who led the subjugation of Qinghai and opened the first front of its holy war.",
    "The Great Heavenly Demon Divine Cult survived the Great Faction War in a diminished state and was driven into the Tianshan Mountains; the Yin-Yang Twin Ghosts later served Dark Heaven.",
    "The Heavenly Power Demon says the Divine Cult's former Cult Leader became corrupt and that the Great Faction War cannot be reduced to a simple division between righteous and evil sides."
  ],
  "continuity_sources": [
    349
  ],
  "open_questions": [
    "Will the Divine Physician's fifteen-day treatment save Jeok Cheongang?",
    "What special condition is required to appraise the Myriad-Poison Ring?",
    "Can Emei, Qingcheng, and the Sichuan Tang Clan withstand the Western Heaven Demon Lord's planned hunt?",
    "What is the identity and purpose of the Lord of Heaven invoked by the Western Heaven Demon Lord?",
    "Will Venerable Myoryeong fully recover from the Black Hand Seal?"
  ],
  "safe_through": 349,
  "temporary_decisions": [
    "Render 한빙석 as Cold-Ice Stone.",
    "Render 서천마군 as Western Heaven Demon Lord.",
    "Render 만독지환 as Myriad-Poison Ring.",
    "Render 대천마신교 as Great Heavenly Demon Divine Cult and 천마신교, 신교, and 본교 as Heavenly Demon Divine Cult or Divine Cult according to context.",
    "Render 음양쌍귀 as Yin-Yang Twin Ghosts and 양귀 as Yang Ghost."
  ],
  "version": 1
}

## Reading copies

## Chapter artifact 345

# Chapter 345

No matter how much the Murim was a veritable death zone crawling with murder and violence, people in every field learned to observe some decorum once they reached the upper ranks.

*Especially when you were the Family Head of the Sichuan Tang Clan, one of the Five Great Families.*

In that regard, Tang Sadok could speak bluntly enough, but he was not accustomed to hearing blunt words himself.

Like now.

“Please lend me the Myriad-Poison Ring.”

“……!”

It was a blow from completely out of left field.

For a brief moment, the corners of Tang Sadok’s eyes trembled before he opened his mouth.

“You still believe that ridiculous nonsense? I knew you were young, but you’re a complete child.”

“I saw your eyes twitch just now.”

“Ridiculous!”

“Your voice gets louder whenever you’re feeling guilty, doesn’t it?”

“I already told you it wasn’t!”

“Oh, you’re clenching your fist now.”

“I told you I don’t have it!”

“If it falls out when you empty your pockets, can I have it?”

“Fine! Search me! If you search me and it isn’t there, I’ll put your neck in there instead!”

“Oh, so you hid it somewhere else. Then I’ll take that back.”

“Grrr…!”

“What a loss…!”

“You insolent little bastard!”

I probably should have held back that last one.

After being hit by a fantastic barrage of combo attacks, Tang Sadok’s eyes rolled back.

I hurriedly shouted before he could scatter his hidden weapons.

“I’m only asking you to lend it to me once! Just once!”

“I already told you it doesn’t exist!”

“Fine, let’s assume it doesn’t. Just hear me out.”

“Nothing you say will change that.”

“Even if I offered to deal with the culprit?”

“What did you say?”

“The culprit who harmed Great Hero Tang Taesang, the Poison King.”

The next moment—

“This little blood brat, I’ve been letting you talk, but now you—!”

Whoosh!

Green qi rose like a haze from Tang Sadok’s entire body. He glared at me with burning eyes, then spoke in a low, settled voice.

“Do you truly wish to die?”

“I have a bright future ahead of me. I’d rather not.”

“Punishing the culprit is our family’s responsibility. How dare an outsider like you—!”

Whoom!

An aura like a raging gale erupted and shook the pavilion. I stepped in front of the trembling Divine Physician and Mungyeong before answering.

“So how did that turn out?”

“……!”

“The culprit is a master powerful enough to defeat the Poison King. And he managed to evade the Tang Clan’s eyes in Sichuan itself and cause a bloodbath at the Emei Sect. His strength clearly isn’t limited to martial arts.”

Sichuan was vast, but it was still the land where the Tang Clan had put down roots over countless years.

It was like losing an enemy of the family in your own front yard. Tang Sadok had led most of his family in pursuit, only to return empty-handed. His face hardened.

“Are you blaming our family for being incompetent?”

“Of course not.”

If the Sichuan Tang Clan was incompetent, most of the sects scattered throughout the world might as well bar their gates and shut themselves off from the martial world.

The Nine Sects and One Gang and the Five Great Families were giants who supported the entire Murim. The current situation was not proof that the Sichuan Tang Clan or Emei Sect were incompetent.

The culprit was simply a monster.

“I’m only pointing out a possibility.”

“A possibility?”

“He possesses martial arts comparable to the Ten Kings, and he’s also exceptionally skilled at escaping. If more hands joined the search, wouldn’t our chances of catching him improve?”

“Our Green Shadow Squad is already pursuing him. I merely returned for a while in case of an emergency. I will hunt him down and kill him before long.”

Tang Sadok’s sharp gaze swept over Cheongpung and me.

“We are the great Sichuan Tang Clan. We have no need for help from outsiders. Least of all from brats like you.”

“……Ah. Right.”

I had long since left the level of a young prodigy behind, hadn’t I?

*Especially that guy.*

I glanced at Cheongpung, who was standing there watching everything with a blank expression, and scratched the back of my head.

*Well, I suppose I expected things to go roughly like this.*

Considering the Sichuan Tang Clan’s family tradition of doing everything their own damn way, this was more or less what I had anticipated.

That was why I had come up with a more appealing plan on the way here.

“Then what about the Fire King instead of brats whose origins are unknown?”

“……!”

“Let’s say you somehow track down the culprit. Do you think he’ll stick out his arm and say, ‘Hurry up and stick poison needles into my veins’? That’s not how it’s going to work.”

One side would be fighting to survive. The other would be fighting to kill. A fierce battle was inevitable.

If the Sichuan Tang Clan committed all its strength, they might be able to avenge the Poison King—but they would also have to prepare for enormous losses.

Countless members of the Tang Clan, whether from the collateral branches or the direct line, would die.

“Old Master—no, my Master—and we will help. We’ll minimize the Sichuan Tang Clan’s losses, and leave the culprit’s punishment to you, Family Head.”

“……Impossible. No matter what losses we must endure, we will accomplish it with our own strength.”

“Your answer came half a beat late.”

“This is the path our ancestors took. It is the path our family has walked until now. It is what made the Sichuan Tang Clan what it is!”

“I know. I know what path the Sichuan Tang Clan has walked.”

A tightly bound family connected by blood. They never forgot a grudge once it had been formed, and their vengeance was merciless.

That was the path the Tang Family had walked—and the reason people respected and feared them at the same time.

I continued in a quiet voice.

“But people won’t point fingers at you just because you sometimes take a shortcut. Especially if you chose that shortcut to reduce the sacrifices among your family.”

Tang Sadok bit down hard on his lip.

Perhaps he was not as cold as he appeared.

No. Even if he was, he was not the sort of ruthless Family Head who would place revenge above everything else.

*If he were, he wouldn’t have returned to the family.*

But the Myriad-Poison Asura Tang Sadok had returned. To protect his family from even the slightest possible danger. To protect the powerless members left behind after he had departed.

“What will you do?”

The answer did not come until a long while later.

“……If—and I mean if—the Myriad-Poison Ring exists, can you treat Great Hero Jeok?”

“A certain person I know says it can.”

At my glance, the Divine Physician opened his mouth.

“We have nearly finished preparing. If the Myriad-Poison Ring is added, there will be no problem with the treatment.”

“How long will it take?”

“Fifteen days. Fifteen days will be enough.”

“Fifteen days…”

Tang Sadok let out a low groan before looking at the Divine Physician.

“I examined Great Hero Jeok’s condition once before. Though my medical knowledge is shallow compared to my expertise in poison arts, I could not determine what sort of symptoms he was suffering from. Is it truly possible?”

“It is possible.”

A clear voice rang out.

Mungyeong stepped forward and added a single sentence.

“The Divine Physician can do it.”

“What an audacious young man. Is he your Disciple?”

The Divine Physician answered Tang Sadok’s question with a faint smile, then spoke.

“The Myriad-Poison Ring is essential for the patient’s recovery. I understand your desire to conceal such a sacred artifact, but please show your generosity and extend your benevolence.”

“Benevolence. Do you think so too?”

“Why all of a sudden?”

“Speak. I want to hear your thoughts.”

“If you insist.”

I shrugged and answered.

“Rather than benevolence, let’s call it gratitude and grudges.”

“Why?”

“Because this is the Murim. If someone helps you, isn’t repaying them the martial world’s code?”

A faint smile appeared at the corner of Tang Sadok’s wrinkled mouth.

“That sounds much better.”

“It sounds better, and it isn’t empty flattery.”

“What will you do if the culprit flees to some far-off foreign land while Great Hero Jeok is being treated?”

“I’ll pursue him alone and bring him back. Ah, of course, I’m not saying I’ll leave right away. I won’t move an inch until my Master wakes up.”

“You’re an amusing bastard. Even tearing the culprit limb from limb wouldn’t be enough, but he is also an extraordinary master. Do you think a wet-behind-the-ears brat like you can capture someone like that?”

“If there’s absolutely no way to capture him, I’ll have to kill him.”

“Ha… hahahaha!”

Tang Sadok burst into uproarious laughter. Then, once he had finished, he casually threw out a single sentence.

“The Myriad-Poison Ring does not exist.”

“……What?”

What the fuck was he talking about?

Had this old man been playing with me the entire time?

Just as I felt the back of my head going numb, Tang Sadok continued.

“The Myriad-Poison Ring is nothing more than an old legend. Even among our blood relatives, it is merely a stale tale.”

“What do you mean, it doesn’t exist? It really doesn’t?”

“No one knows, and no one must know.”

“Fuck! Then you should have said that from the beginning! Have you been messing with me this whole—”

Ssssss.

I could not finish my sentence. I shut my mouth.

A pure white snake had slowly crawled out from inside Tang Sadok’s robes and was staring fixedly at me, flicking its tongue.

*What is that?*

This wasn’t Voldemort. Why was a snake suddenly appearing here?

To make matters worse, it had horns, which snakes were not supposed to have. As I stared into the snake’s black eyes, the Divine Physician muttered as if groaning.

“The Thousand-Year Poison Horned Snake…?”

The name alone sounded like a deadly viper.

Tang Sadok gave a quiet laugh at my slow retreat and stroked the snake’s triangular head.

“Don’t be afraid. It isn’t dangerous, so there’s no need to back away.”

“The name alone sounds fucking dangerous.”

“The Thousand-Year Poison Horned Snake?”

“Yes. What kind of name is that? It’s not a golden retriever. It’s a Thousand-Year Poison Horned Snake… Never mind. Does the Myriad-Poison Ring really not exist?”

“It isn’t the Thousand-Year Poison Horned Snake. It’s Mimi.”

“Excuse me?”

“Tang Mimi. That is the name I gave it.”

What was that supposed to mean? Terrifying…

As Tang Sadok stroked Mimi-chan with a hand full of affection, he suddenly looked at the Divine Physician.

“You must know. This creature is not an ordinary Thousand-Year Poison Horned Snake.”

The Divine Physician nodded.

“As far as I know, a Thousand-Year Poison Horned Snake is a rare venomous creature that carries an extremely deadly poison. Its entire body is black, and its temperament is so ferocious that it can never be tamed. However…”

“As you can see, this one not only looks different, but is also exceptionally gentle.”

“But we do not know when it might suddenly turn on us. Is it not a venomous creature capable of killing a hundred cows with a single drop of its venom?”

“You have nothing to worry about. This one has no venom.”

“What?”

“To be precise… it would be more accurate to say that its venom is gone.”

After finishing his sentence, Tang Sadok met the gaze of Mimi-chan—or rather, the Thousand-Year Poison Horned Snake.

It lasted only a brief moment, but it was clearly a moment of communion. The clever snake had evidently understood its master’s intentions.

Hiss! Ssssss!

The snake lowered its head and let out a metallic hiss before spitting something onto Tang Sadok’s palm.

With a soft plop, the object emerged from the slime covering it.

*That’s…*

A ring.

A black gemstone was set into it, as if it had trapped the darkness of the entire world inside.

It had absorbed even the Thousand-Year Poison Horned Snake’s deadly venom, and now it gleamed with a beautiful yet ominous light.

“No way…”

As I stared at the ring, half dazed, Tang Sadok’s low voice pierced my ears.

“Remember this. No one knows, and no one must know.”

“Then…”

“Yes.”

Tang Sadok held it out toward me.

“It is our family’s sacred artifact.”

The moment I picked up the ring with trembling hands, the bell I had been waiting for rang out.

Ding.

> **System**
>
> - Quest Condition complete: **Myriad-Poison Ring Acquired**!
>
> - Chain Quest **Myriad-Poison Ring** has been successfully completed!
## Chapter artifact 346

# Chapter 346

I examined the small ring closely. It was light and strange.

The ring was made of some unknown metal and engraved with unfamiliar patterns, while the gemstone set in its center glittered with a dark light, as if it held the night sky inside.

*So this is the Myriad-Poison Ring.*

The sacred artifact of the Sichuan Tang Clan—said to detoxify any poison—had fallen into my hands.

Its effectiveness had to be genuine if it could turn a Thousand-Year Poison Horned Snake, said to contain an incredibly deadly poison, into a pet snake named Mimi-chan. Still, there was no harm in checking.

*Item Appraisal.*

Beep.

> **System**
>
> - Item Appraisal failed!
>
> - A special condition must be met to appraise this Item!

“Huh?”

“What is it? Is there a problem?”

I vaguely brushed off Tang Sadok’s puzzled question.

“No. It’s nothing…”

“Nothing what?”

“It’s just that the gemstone is pretty. Its color is similar to a snake’s eyes.”

I saw a wrinkle form on Tang Sadok’s forehead.

I had momentarily forgotten that the old man standing before me was not only the Family Head of a great clan, but also a seasoned martial artist who had spent his entire life in the Murim.

As expected, Tang Sadok widened his eyes and bellowed.

“What nonsense are you spouting?”

“Family Head, the thing is…”

“Our Mimi’s eyes are prettier!”

“Huh?”

“Is that all? I wipe her body down with fragrant oil every morning and evening, so she smells wonderful. And her teeth are sparkling white!”

“Ah… yes.”

A seasoned martial artist, my ass. He was just a snake fanatic.

What kind of Family Head liked his pet snake more than his family’s sacred artifact?

At this point, I was starting to wonder whether Mimi-chan was actually the sacred artifact of the Sichuan Tang Clan.

*But why can’t I appraise this?*

I tried Item Appraisal again, just in case, but the result did not change. If a special condition was required to appraise it, then the sacred artifact really was a sacred artifact.

*It bothers me that I can’t confirm what it does, but its effects have to be genuine.*

I turned toward the Divine Physician. Wearing a smile, he spoke as though he had been waiting for me.

“The Thousand-Year Poison Horned Snake is not an ordinary venomous snake, but a spiritual creature. Yet the ring rendered the venom gland of such a creature useless… We will have to try it to know how much poison it can detoxify, but it is worthy of the name Myriad-Poison Ring.”

“If that’s the case…”

“Without the Myriad-Poison Ring, the chance would have been just one percent. Now, I believe it is over seventy percent.”

“Even with the Myriad-Poison Ring, only seventy percent…?”

“I shall make up the remaining thirty percent with this old man’s medical skill.”

“Whew. You should have said that from the beginning.”

The Divine Physician laughed heartily at my sigh of relief and stroked his beard.

“Now, only one thing remains.”

“What is it?”

“A place to conduct the treatment.”

Tang Sadok cut in bluntly.

“Have you forgotten where you are?”

“I’ve heard there is a clinic inside the Sichuan Tang Clan. But Great Hero Jeok’s case requires two conditions.”

“Tell me.”

“First, it must be a secluded place where people cannot easily come and go. Second, it must be somewhere untouched by sunlight, with a bitter cold that seeps into the body.”

“A secluded, dark, and cold place…”

Tang Sadok thought for a moment, then let out a quiet laugh.

“As it happens, I know the perfect place. I shall take you there myself.”

“Thank you for your generosity, Family Head.”

“I am not the Great Hero of benevolence you speak of. This is merely a matter of gratitude and grudges between us. And if you reveal the existence of the Myriad-Poison Ring later, or let it become known outside the clan in any way…”

I sighed and finished for him.

“I’ll be dragged away, made to take a half-body bath in a vat of poison, and have holes poked in me with needles.”

“You have a poor imagination. Whatever you imagine, you will suffer something worse.”

“Unless I’ve gone insane, that won’t happen.”

“I certainly hope so… What are you doing here?”

Good question. What was that guy doing here?

While we were talking, Cheongpung had crept over and was reaching toward Mimi-chan.

“Wow, she’s pretty. Can I touch her?”

“No.”

“Why not?”

“Hmph. Do you think she lets just anyone handle her? If I had not called her, she would not even have shown herself in front of you.”

“Mimi, Mimi. Come here.”

“What are you doing, you ridiculous—”

Hissssss.

Mimi-chan slid down Tang Sadok’s shoulder and licked the back of Cheongpung’s hand.

“Gasp!”

“Mimi, Whirlwind!”

Whirlwind, my ass. He was telling her to perform a technique even a person wouldn’t understand.

As expected, there was no telling what went on inside Cheongpung’s head.

Sssshk, sssshk, sssshhhk!

“…What the fuck?”

What had I just seen?

My mouth fell open as Mimi-chan spun her body wildly in a spiral.

“Wow! Good job, Mimi!”

“This can’t be! How could Mimi use Whirlwind on someone she’s never met before?”

“Wait, is that actually a real technique?”

“That isn’t important right now!”

It seemed pretty important to me. At this rate, I wondered whether she might start firing a million volts or a Hyper Beam.

*Can she evolve, too…?*

As I wondered whether the Myriad-Poison Ring or Mimi-chan was the real sacred artifact, Cheongpung smiled brightly and spoke.

“I get along well with those animals. When I lay down in the grass on Huashan, birds, deer, and even tigers would come play with me. Hehe.”

What was he, some kind of Huashan druid?

Tang Sadok stared at Cheongpung with a dazed expression, still reeling from having Mimi-chan stolen from him.

“Wait. There seems to be something strange mixed in at the end there. Why was there a tiger? How dare you tell such an obvious lie in front of this old man!”

“We were playing together and were about to part ways when the tiger tried to eat the deer, so I knocked it out with Crouching Tiger Fist!”

“…”

“…”

Anyone would have thought that was insane. But it was probably true.

In the silent main hall, Mungyeong’s mutter rang out with unusual clarity.

“Is the Huashan I know not the same Huashan?”

I didn’t know about that, but one thing was certain.

If the heavens and earth were overturned and Cheongpung somehow became Huashan’s Sect Leader, from that day on, it would become *your* Huashan.

“…Let’s go. You said you would show us the place.”

“…Very well.”

* * *

Following Tang Sadok, we arrived at a cave on the distant outskirts of the Sichuan Tang Clan’s grounds.

The mouth of the cave gaped open like a pitch-black maw.

Aside from two large braziers installed on either side, there was no one in sight.

“Where are we? There doesn’t seem to be anyone guarding it.”

“Since no one is here, I suppose it must be feeding time.”

“Feeding?”

“You will find out once we enter. Follow me.”

Unlike the Jin Family of Taiyuan’s training hall, the cave was not arranged in a straight line.

I had no idea how far we descended the stone stairs leading deep underground before a narrow passageway, barely wide enough for two people to pass through, appeared before us. A familiar smell entered my nostrils.

*Is this… the smell of blood?*

Something felt wrong, so I looked around. Doors reinforced with iron bars appeared at irregular intervals.

“No way…”

“That is correct. This is our family’s underground prison.”

“…Not a torture chamber?”

“Oh, you will see plenty of those once we get inside.”

What the hell had I just heard?

As everyone, myself included, stared at him, Tang Sadok spoke in an unconcerned tone.

“Except for the Family Head’s Hall and a few other pavilions, this is the oldest space in the family compound. It must be well over two hundred years old by now. In any case, it is a historic place steeped in history.”

I did not know about it being steeped in history, but I felt like I ought to write a will before I was dragged any farther inside.

“Isn’t it still just a prison?”

“Is there a problem?”

“Of course there is! You want us to treat Old Master—no, my Master—in here?”

“Not a ray of sunlight enters this place, and a bitter chill seeps through it until it reaches your bones. This is the most suitable location.”

“You said you conduct torture here, too.”

“Of course. Is that even worth asking?”

“…”

Anyone listening would have thought he was asking whether I wanted extra toppings on my pizza.

Just as I ran out of things to say, a hunched old man came limping toward us from the distance, accompanied by a faint light.

“Family Head, what brings you here?”

“Ah, Old Man Gung. You’ve been working hard. How are they?”

“Nothing much. Same as usual. I just went in to check whether they were still breathing. But who are these people…?”

“They are guests of our family. They will be staying in the prison for fifteen days due to certain circumstances. They will not be too noisy, will they?”

“No, sir. The ones still alive are hardly any different from walking corpses, so it should be quiet.”

“When I saw him a few months ago, the Heavenly Power Demon still seemed to have plenty of energy.”

“Ah, that one? You needn’t worry about him anymore.”

The hunched old man grinned, exposing teeth that had almost entirely rotted away.

“He was so noisy that I drained every last bit of energy from him. And while I was at it, I took a few other things, too. Hehe.”

“You are always working hard.”

“Oh, Family Head, you flatter me. I only do it because I enjoy it.”

As I listened to their conversation, I made a resolution.

I must never become enemies with the Sichuan Tang Clan.

After exchanging a few more words with Old Man Gung, Tang Sadok spoke with a bright expression.

“Excellent. It seems the deepest and largest cell has just been emptied. We can use that one.”

I did not need to hear why it had been emptied.

It was not as if someone had checked out at the prison’s front desk and walked away.

*They must have checked in with the afterlife by now.*

Even if this place met all the necessary conditions, could we really conduct a medical treatment here?

The Divine Physician had clearly thought the same thing. Mungyeong addressed his Master, who had put on a frown, in a calm voice.

“Master, are we not physicians? For the sake of our patient, you must endure it even if you dislike the place.”

The Divine Physician let out a low groan before answering.

“…Yes. You are right. We shall do so.”

“And the people imprisoned here are certainly evil men who have committed countless murders. Please do not let it trouble you too much.”

Tang Sadok, who had been listening to their conversation, added a word.

“Well, well. You are quite mature for a young medical apprentice. Divine Physician, as that boy said, everyone imprisoned here is a vicious demonic criminal, so do not think poorly of our family.”

“I committed a discourtesy out of concern. Please forgive this old man with your generous heart.”

“I will gladly forgive you. Of course, not those men who harmed members of our family. Isn’t that right, Old Man Gung?”

Old Man Gung laughed with a bizarre metallic sound and picked up a torch.

“Come now. I shall show you the way.”

“…”

For some reason, I felt as though I were following the Grim Reaper.

*Judging by the atmosphere alone, that old man seems more dangerous than the culprit who killed the Poison King.*

It had to be my imagination. It was definitely my imagination.

And so, we began walking toward the suite boasting the finest facilities in the Sichuan Tang Clan’s prison.

* * *

“Hm?”

The middle-aged man suddenly looked around.

Winter had passed. The sky was clear, and the bare mountain forest was gradually regaining its green color.

The valley of the nameless mountain was peaceful, as it always was. Yet no matter how much he thought about it, he could not understand why he felt such a strange sense of déjà vu.

“What a strange thing. Such a strange thing…”

The middle-aged man muttered softly, then turned his head and asked,

“Don’t you think so, too?”

Grrk. Gk.

Blood bubbled up from the man’s gaping throat.

The fallen man glared at the middle-aged man with eyes full of resentment.

“M-my family will make you pay…”

“Those are boring last words. Then again, the Sichuan Tang Clan has always been like that.”

Crunch!

The middle-aged man wiped the leather shoe soaked in blood and brain matter against the grass before straightening his back.

Four bodies lay scattered around him.

Then he smiled at the one man still alive.

“So, will you answer my questions obediently, or would you rather writhe in unimaginable pain until you die?”

“……!”

“For your information, the Poison King chose the latter. He lasted four days before finally dying.”

The man shuddered and slowly closed his eyes.

A deep smile spread across the middle-aged man’s lips as he saw the man prepare himself for death.

“Good. Let’s find out how long you can last.”
## Chapter artifact 347

# Chapter 347

The Sichuan Tang Clan’s underground prison was dark and damp. There was also something about it that sent a chill down the spine.

Perhaps that was only natural. Countless people must have met their deaths here since the underground prison was built.

“Care for a drink?”

In that sense, the old man holding out a worn gourd was practically the Grim Reaper of the underground prison.

I briefly wondered how many people this diminutive, hunchbacked old man had dealt with before answering.

“No, thank you.”

“If that’s what you want, then.”

Gulp, gulp.

Old Man Gung tilted the gourd back and wiped his mouth with his sleeve. The sleeve was so worn it looked ready to crumble, and it was covered in dark red stains that looked like blood.

“Ahh, that’s good.”

The potent scent of liquor drifted through the stench of blood lingering in the corridor and tickled the tip of my nose.

Drinking on duty. At the Jin Family of Taiyuan, that would have been grounds for a disciplinary report, but it seemed that rule did not apply in the Sichuan Tang Clan’s underground prison.

“I heard you’re one of the most renowned young prodigies in the Murim.”

It was obvious who he was talking to. Cheongpung and Tang Sadok had disappeared somewhere early on, while the Divine Physician and Mungyeong were busy purifying the prison and turning it into a treatment room.

I answered reluctantly.

“I’m not that renowned. I can fart a little, though.”

“What I’ve heard says otherwise. As the Fire King’s successor, you could piss on the plaques of the Nine Sects and One Gang and get away with it.”

Old Man Gung grinned, baring teeth that had almost entirely rotted away.

“We’ve got a fellow locked up here who did just that.”

“Did what?”

“The fellow who pissed on the plaque of one of the Nine Sects and One Gang. I believe it was the Kunlun Sect, if memory serves.”

“…There are all kinds of people in this world.”

“Heh heh. He was once notorious even among the Demonic Cult’s fiends. Now he’s tied to a rack and does nothing but shit blood. You must have seen him on your way in.”

“Did I?”

The Sichuan Tang Clan’s underground prison was as winding and complicated as a maze. On the way here, I had seen dozens of cells and more than ten prisoners.

*That fellow who pissed on the Kunlun Sect’s plaque was probably one of them.*

They were people paying the price for their evil deeds. I did not feel even the slightest bit of sympathy.

No, it would be more accurate to say that I had no room to worry about something like that.

*I didn’t expect to be this nervous.*

The peculiar unease I had felt ever since entering the prison refused to fade.

It was the same feeling I had experienced several years ago, when my mother went into the operating room and I sat in a quiet corridor waiting for the results.

*It’ll be fine. Everything will be all right.*

As I muttered those words inwardly, the tightly closed prison door opened, and a dozen servants carrying various cleaning tools came rushing out.

I asked the last person to emerge.

“Is it done?”

The Divine Physician nodded with a bright expression.

In the space of two shichen, the prison cell visible behind him had been transformed into a fairly convincing treatment room.

“It is still far from satisfactory, but this should be enough to make it functional.”

“Then…”

“Yes. We begin now.”

At last, all the preparations were complete.

The various medicines made by combining the twenty-four herbs gathered from the Cold-Ice Land had already been brought here. The treatment room was ready. Only one thing remained.

“Thank you all for your hard work. Would you mind stepping outside for a moment?”

At my words, the people of the Sichuan Tang Clan, including Old Man Gung, began to leave. I waited until they had disappeared, then reached into my robes.

*Inventory Open, Summon.*

A hard object appeared in my previously empty palm. For safety’s sake, I had kept the Myriad-Poison Ring with me for a while, but now I handed it to the Divine Physician.

The Divine Physician accepted the ring, slipped it onto his finger, and entered the prison cell while gesturing to me.

“Would you bring the patient in?”

I lowered the pack frame from my shoulders. Along with the faint sound of breathing, a small figure emerged.

“Over here.”

I stepped into the prison cell with Jeok Cheongang in my arms. The floor was clean, but the stench had not completely disappeared and still lingered at the tip of my nose.

None of that mattered, however. The weight of Jeok Cheongang, light as a feather, made my chest ache unusually badly.

*You’ve grown so weak.*

A month and a half had passed since we left the Murim Alliance in Henan and began our journey.

We had found the Divine Physician and secured his treatment far more quickly than I had expected, but Jeok Cheongang had continued to weaken day by day.

I carefully laid him down on the smooth white stone prepared in the center of the room.

It was a special object called Cold-Ice Stone, which Tang Sadok had provided. The Divine Physician had said it would be a great help in treating Jeok Cheongang.

“He’s sleeping soundly.”

Jeok Cheongang’s face was gaunt as he lay there, but it was peaceful all the same.

I stared at his face, covered in wrinkles and age spots.

Memories from our first meeting until now flashed before my eyes.

*What an interesting kid.*

*The more I look at you, the stranger you seem. Whose disciple are you?*

I remembered that ill-tempered old man I had met at Jang Taebo’s house a year ago.

*The roof is old. It leaks.*

I also remembered the master who, unable to stop the wretched disciple he cherished like family, blamed a perfectly good roof and shed tears of regret.

*If you kill that bastard, I’ll kill you too.*

*I entrusted the Fire Gate Clan’s sacred artifact to that kid.*

*I’ll pass on everything I have to you.*

From Shanxi to Henan, and from Henan to Anhui. Then there was the year at Mount Jiuhua. I remembered every moment I had spent with him.

Jeok Cheongang had led me outside the Jin Family of Taiyuan, and I had followed him into the vast world beyond. We had always been together.

*How is it? Just as I told you, right?*

*What are you talking about?*

*The Dance of the Fire God and Demon. Wasn’t it incredible?*

His face and voice came back to me—the faint smile he wore even while vomiting blood.

Even the single remark he had tossed out on a day when the moon shone brilliantly, while trying to sound gruff.

*Master, my ass. Call me Old Master.*

“Old Master.”

Even when I called out loud, no answer came back.

I knew that, yet I still called out—not because I hoped he would hear me, but because there was something I wanted to tell him.

“Did you know?”

*I don’t, you idiot!*

A dry laugh escaped me at the voice that seemed to echo from somewhere. I gripped Jeok Cheongang’s wrinkled hand tightly and whispered,

“I’ve always wanted to call you Master.”

I did not know when it had happened. But at some point, I realized it.

He was my Master, and I was his Disciple.

We had both been quietly turning those words over in our hearts.

“Young Master Jin. It is time.”

At the Divine Physician’s words, I tore my gaze away from Jeok Cheongang’s face.

Then I politely saluted the old physician standing there with a composed expression, along with his young Disciple.

“Please… take good care of my Master.”

The two men returned the salute.

“We will do our best.”

“I will help my Master and do everything I can as well.”

Yes. That was enough.

Do everything one could and leave the rest to heaven.

We had done everything humans could do. Now all that remained was to leave it to the heavens.

God, Buddha, Allah, the Jade Emperor.

*Whoever you are, if you help me just this once, I will never forget it.*

I did not believe in gods, but I did believe that an omniscient and omnipotent being existed somewhere above the heavens.

As I offered a brief prayer to that being, whose face and name I did not know, the Divine Physician spoke in a solemn voice.

“Remember this. Fifteen days—fifteen days. Until then, no one may approach.”

*What should I do if it takes longer than fifteen days?*

I swallowed the words hovering on the tip of my tongue. Now, I had no choice but to trust the two of them. There was only one thing I could say.

“I will stop anyone who tries to enter, even if I have to stake my life on it.”

* * *

“Is that everything?”

The middle-aged man looked down at the man before him with numb eyes.

The man’s limbs were twisted at grotesque angles, and his skin had been flayed away. Drenched in blood, he wheezed in a voice as tiny as an ant.

“I—I’ve already told you everything I know…”

“Aren’t you leaving out the most important part?”

“I don’t know. I truly don’t.”

Blood tears flowed from his one remaining eye, while the trouser legs already soaked in blood grew wet with urine.

The man forced out a trembling voice.

“Please… just kill me now…”

The middle-aged man watched the man’s eyes, which looked ready to go out at any moment, then clicked his tongue.

“Judging by this, it seems you were telling the truth.”

The man had already endured half a day of unimaginable torture.

If he had begged to be spared, there might still have been room for doubt. But once the word *death* escaped his lips, the middle-aged man had to accept that he was telling the truth.

Until now, no one had ever lied to the middle-aged man.

With one exception—the Poison King, Tang Taesang.

“I’ve seen your half-day’s worth of courage. You can rest now.”

Whoosh—thud!

Along with the sound of a single gust of wind, the blood-soaked head jerked backward. A flick of the middle-aged man’s finger had pierced the man between the brows, and he died with a peaceful expression.

The middle-aged man stared down at the body of the man who had been a member of a collateral branch of the Sichuan Tang Clan and an operative of the Green Shadow Squad. Then he stretched out a hand.

Boom!

A pit a zhang deep appeared with a thunderous roar.

The five bodies scattered around him were neatly stacked inside it, and the entire process—from burying them beneath the earth to covering the pit—took no more than an instant.

“The Green Shadow Squad… So those gnats have latched on.”

The middle-aged man muttered quietly as he looked beyond the winding mountain ridge. His gaze was directed west, toward the Sichuan Tang Clan.

*I should have killed Tang Sadok when he came out.*

It had been a mistake. The Poison King’s resistance had been stronger than expected, and it had taken considerable time to drive the poison out. He had even lost one of his arms.

Emei or Qingcheng might have been another matter, but the Sichuan Tang Clan was highly vigilant and thoroughly defended. Even for him, storming the place alone with one arm missing would be too much.

*But his life has only been extended by a few days. The outcome will not change.*

He had long since grasped every movement taking place in Sichuan.

All preparations were complete to hunt the three tigers crouching in Sichuan—Emei, Qingcheng, and the Tang Clan.

Now…

It was time to call in the hunters.

Whoosh!

The middle-aged man moved as smoothly as if he were sliding. With every step, distance vanished beneath him and the scenery blurred past.

At last, he stopped before a cliff deep in the mountains.

“This is the place.”

Without hesitation, the middle-aged man reached out and touched the cliff.

The next moment—

Vwoom.

Along with a resonant hum, the cliff collapsed.

No. It would have been more accurate to say that space itself had warped. The weathered stones and boulders vanished, revealing a vast hollow that had been hidden from sight.

*The sorcerers’ Mystic Gate Formation. It never stops being impressive.*

But compared to what he was about to do, even this was nothing more than a parlor trick.

Step. Step. Step.

At the center of the hollow, where darkness had settled thickly, the middle-aged man stood in the middle of a strange pattern carved into the floor and raised his internal energy.

The instant the dark red haze pouring from his entire body touched the pattern—

“Lord of Heaven!”

Flash!

At the middle-aged man’s cry, the pattern began to shine. A black flash—dark yet bright, impossible to describe—filled the hollow.

Then, filling the space left behind after the light vanished, came a thunderous roar.

“We pay our respects to the Western Heaven Demon Lord!”

“We pay our respects to the Demon Lord!”

Hundreds of tiger hunters in pitch-black robes stood before him, their eyes devoid of emotion and their auras as sharp as blades.

A faint smile formed at the lips of the middle-aged man—the Western Heaven Demon Lord.
## Chapter artifact 348

# Chapter 348

The black-robed men stood in neat ranks and files. The sheer number of them—several hundred—was not the only thing filling the enormous cavern.

It was their aura.

The suffocating aura emanating from the men—their eyes deep-set, their bodies upright as iron towers—was swallowing the cavern.

And towering over them all stood one man—a giant in his own right.

“The Three Fiends.”

Vwoom.

The voice, infused with profound internal energy, pierced the black-robed men’s ears, and their bodies shuddered. The three old men at the front were no exception.

They stepped forward several paces, then prostrated themselves at the middle-aged man’s feet—none waiting for the others—and cried out in unison.

“The juniors of the Qilian Mountains pay their respects to the Western Heaven Demon Lord.”

Their faces, builds, and voices.

The three old men were brothers born of the same mother, and they looked astonishingly alike in every way.

Their mother had died giving birth to them. Their father had abandoned his young children and left. The three brothers, left behind in the barren land of Qinghai, hid near the vast mountain range to escape the people’s scorn.

Then, one day, after they had been forgotten by everyone, the three brothers returned.

They returned under the name of the Qilian Three Fiends.

“You’ve aged quite a bit since I last saw you. I suppose I can call you the Three Old Men now.”

“N-no, my lord. How could we presume to call ourselves that when Your Excellency is here?”

The Qilian Three Fiends had once been fiends who dyed Qinghai Province red with blood. Yet before the Western Heaven Demon Lord, they were nothing more than docile lambs.

The Qilian Three Fiends swallowed hard, then opened their mouths at the same time, as if they were one person.

“B-but, my lord. Forgive us for saying so, but your arm…”

“This?”

The Western Heaven Demon Lord looked down at the empty sleeve where one of his arms should have been and answered in a dry voice.

“It was the price I paid to take two lives.”

“Does that mean…”

“The two old fossils from the Tang Clan and Emei are no longer of this world.”

“……!”

The air inside the cavern trembled with agitation.

Who were the Poison King and the Heaven-Shaking Venerable Nun? They were giants who had left their mark on the history of the Murim, Supreme Peak masters who had dominated an entire era.

And yet…

They had both met their end at the hands of a single man.

The Qilian Three Fiends and the black-robed men stared at their leader with awe.

“Th-then…”

“Yes.”

A strange light flashed in the Western Heaven Demon Lord’s eyes.

“The time has finally come.”

* * *

Right now, my eyes are closed.

I focus my mind in the quiet darkness. As a voice pierces my ears, someone’s figure takes shape in the darkness.

Neither tall nor short, the young man hiding claws behind a bright smile is Cheongpung.

“First, I’ll target my Benefactor’s shoulder, chest, and stomach in that order with Crouching Tiger Fist.”

Cheongpung’s form, created by my imagination in the darkness, moved.

Fast.

He erased the distance in a single step and charged at me. His fist blurred, and I could almost hear the fierce sound of air splitting somewhere nearby.

“I can dodge that easily. I’ll retreat half a step diagonally and throw a fist at your flank.”

“I’ll use Chaotic Flower Hand to redirect the force as I retreat, then counter with Thirty-Six Plum Blossom Swords.”

“What form?”

“One Cut Under Heaven.”

One Cut Under Heaven was among the most powerful supreme forms in the Thirty-Six Plum Blossom Swords.

Even back when I had frequently sparred with Cheongpung, I had chosen to evade that technique rather than block it.

“Isn’t that a little too much?”

“Given who my opponent is, I have to give it everything I’ve got.”

“What happened to calling me Benefactor?”

“That’s one thing, and this is another. Hehe. Anyway, One Cut Under Heaven.”

One Cut Under Heaven.

It wasn’t difficult to imagine how the attack would come in.

In the darkness, Cheongpung redirected the force with Chaotic Flower Hand and retreated without taking a hit. At the same time, his hand reached for his waist, and a flash burst forth.

Sshk!

Along with a spine-chilling hiss, Sword Energy burst out horizontally.

I could see it clearly before me.

How should I respond?

I didn’t have to think long.

“I’ll deflect it. First form of the Fire Dragon Divine Spear. Fire Dragon’s Single Tail.”

“You won’t be able to block it.”

“When was the last time we fought?”

“Hmm. About a year ago.”

“If you think about it one way, that’s short. If you think about it another, it’s a long time. It was long for me. Long enough for a single day to feel like ten years.”

“……!”

“Think about it again. Are you sure I can’t block it?”

Cheongpung was silent for a moment before answering. His voice had sunk low.

“I was thinking about it wrong. If it’s you, Benefactor… I think you can.”

“Then let’s continue.”

Cheongpung and I devoted ourselves to discussing martial arts for a long while.

It had been more than a year since we had directly crossed hands, but we knew each other’s martial arts and skill levels well—from the Star-Array Grand Banquet until now. That was what made this possible.

“Three steps to the left. Plum Blossom Five-Point Finger.”

“Plum Blossom Five-Point Finger is an excellent martial art, but as long as I watch out for the vital points, it won’t matter. I’ll follow you in and aim Flame-Extinguishing Divine Fist at your chest.”

Within the images each of us had drawn, the back-and-forth exchange continued.

A hundred, two hundred…

Before long, once our imagined bout had passed five hundred exchanges, Cheongpung suddenly spoke.

“I’ll use Dark Fragrance Drift to close to within two steps, then Plum Blossom Three-Ridge Sword.”

Suddenly?

Cheongpung was weaker than me in close combat. He had learned Huashan’s outstanding supreme martial arts, but perhaps because the sect’s roots lay in sword techniques, the Fire Gate Clan had a slight advantage when it came to palm techniques.

And yet he was closing in like this…

*Ah. So that’s it.*

I had guessed as much, but of course it was Cheongpung.

I opened my eyes with a hollow laugh. When I didn’t answer for a long while, Cheongpung cautiously opened his eyes to a narrow slit and asked,

“Benefactor, why?”

“That’s enough for today.”

“Ah! Why?”

“Because it would be a shame.”

“What?”

“Let’s fight for real later. Not this kind of swordplay discussion. Let’s actually cross weapons.”

It was too disappointing to settle things through a mere exchange of imagined techniques. I meant that we should fight later with both of us giving it everything we had.

Cheongpung was as innocent as a child, but he was by no means stupid. Surely that much would be enough for him to understand—

“Why would we cross weapons? Don’t they just collide?”

“…….”

No.

Maybe he really was just an idiot.

As I regretted my hasty judgment, Cheongpung began pestering me.

“I’m bored, Benefactor. Can’t we just keep going?”

“Oh, Young Hero Cheongpung. Did you happen to hear?”

“Hear what?”

I gazed intently at Cheongpung and parted my lips.

“I heard there’s a former imperial chef in the Sichuan Tang Clan.”

“An imperial chef?”

“They say he makes incredible food. Especially pastries and sweets.”

Gasp.

Cheongpung’s eyes grew hazy for a moment, but he soon shook his head vigorously.

“N-no. I have to stay here with you and watch over Grandpa Jeok.”

“It’s fine. I’m staying here anyway, so—”

“Then I’ll be back!”

“……Sure. Go ahead.”

Whoosh!

What was that? Some kind of bullet movement technique?

The moment Cheongpung vanished at the speed of light, I looked around.

It was a space where a bleak chill coexisted with a foul stench—the underground prison. I hadn’t left it even once since the treatment began.

“It’s only been four days.”

The words slipped from my mouth like a sigh.

Time passed far more slowly in the underground prison than I had imagined. Not because the place never saw a ray of sunlight, but because of the anxiety and tension felt only by those who were waiting.

Perhaps that was why every day felt like my blood was drying up.

“Maybe I should have stayed in front of the treatment room.”

Even as I said it, I shook my head. There was nothing I could do by pacing in front of the treatment room door anyway.

With my five senses already sharpened to their limit, I would have listened to every sound coming from inside before eventually being unable to endure it and pacing around the underground prison at a distance.

Just as I was doing now.

*Still, it’s awfully quiet with me here alone.*

After Cheongpung, who had clung to me like a burr for the past three days, disappeared, I felt strangely empty.

By Tang Sadok’s order, even Old Man Gung was forbidden from entering the prison. That meant I was completely alone now.

*No. Come to think of it, I’m not alone.*

I wasn’t talking about the Divine Physician and Mungyeong, who were likely completely absorbed in treating Jeok Cheongang.

There were ten or so prisoners trapped in the underground prison, waiting for the day they would die.

They were my roommates.

*Not exactly the best roommates, though.*

They weren’t the kind who left the toilet unflushed or constantly brought their lovers over. Every one of them was a fiend who had earned a notorious name throughout the martial world.

Even if they were imprisoned, there was no way sharing a space with men like that could be enjoyable.

And the most troublesome part was…

Dong. Ddong. Ddeeeong.

*I’m the one who has to feed them.*

I frowned at the familiar sound of the bell.

With Old Man Gung away, someone had to check whether the prisoners were still alive and feed them.

That someone was me.

The bell that had just rung was the signal from outside announcing mealtime.

*At least it’s only once a day.*

Still, bothersome was bothersome. I sighed and started walking.

In a corner of the prison, a thoroughly battered wooden barrel waited for me, along with food haphazardly mixed together inside it.

It had been poured down through a hole connected to the surface. Calling it a meal was generous. It was basically a slop bucket.

*No one’s around, so I guess it’s feeding time.*

There had been a reason Tang Sadok had used the word *feed* three days ago.

The Sichuan Tang Clan treated the prisoners here like dogs and pigs.

No, dogs and pigs had it better. At least livestock wouldn’t have to worry about surprise events where Old Man Gung approached with all kinds of torture implements while wearing an eerie smile.

“Heave-ho.”

With the mindset of a zookeeper, I carried the slop bucket around the prison.

Beyond the thick iron bars, prisoners sat with their arms and legs bound by steel chains. All I had to do was open the door, step inside, scoop up a full ladleful, and pour it into the battered bowls set before them.

Whenever I did that, the prisoners, who had been lying limp and helpless after prolonged imprisonment and torture, would make their eyes flash and strike up a conversation.

“Never seen your face before.”

“I’ve seen you for three days. What kind of bullshit is that?”

“Release me. I’ll teach you martial arts that can look down on all under heaven.”

“Judging by the fact that you’re rotting in here, they sound like martial arts the whole world can look down on.”

“You insolent bastard… The moment I get out of here, I’ll tear you apart and kill you myself.”

“Oh, impressive. I’ll be sure to pass that along to Old Man Gung.”

“Please, anything but that!”

All kinds of attempts at persuasion continued without end.

Some offered to teach me their martial arts. A middle-aged beauty who had once drained the vitality of the Tang Clan’s direct line through a technique of harvesting yang to replenish yin even tried to seduce me.

“Child. Why don’t you come a little closer? I’ll show you heaven.”

“Kirara Asuka. Grandma Uehara.”[^1]

[^1]: A riff on Japanese adult-film performers Kirara Asuka and Ai Uehara; *ai* sounds like the Korean word for “child,” prompting Taekyung to replace it with “grandma.”

“……What?”

“The mainland still has a long way to go compared to the island nation. Stop talking nonsense and eat your food.”

“You little—Hey! You turtle bastard!”

I ignored her spiteful shouting and headed toward the last prison cell.

In the most secluded and damp corner was a strange man with disheveled hair.

*He’s the quietest old man in this prison.*

He was also the most dangerous.

The severed sinews and meridians in his limbs, along with the restraints several times heavier and sturdier than those worn by the other prisoners, were proof enough.

Rattle. Thump.

The old man stared silently at the bowl containing the unidentified food, then suddenly opened his mouth.

“I heard you talking about this old man.”

I stopped short.

Not because it was the first time I had heard his voice in three days, but because I couldn’t understand what he meant.

“Talking about you? When did I ever do that?”

“Three days ago. Didn’t that Gung fellow say so?”

“Gung fellow? Old Man Gung?”

After searching through my memories for a moment, I looked at the old man with fresh surprise.

“Oh. Then are you the one who pissed on the Kunlun Sect’s signboard?”

“Yes. This old man is the Heavenly Power Demon—”

“So you were the Kunlun Sect’s public-pissing criminal.”

“…….”

The old man—the Heavenly Power Demon—had an eyelid that twitched.
## Chapter artifact 349

# Chapter 349

After a brief silence, the Heavenly Power Demon parted his lips.

“……A public-urination criminal? Do not address this old man by such a disgraceful name.”

*Ah. I messed up.*

It seemed the former fiend who had once made his name known throughout the world found that name rather unpleasant.

After thinking for a moment, I offered him a more suitable term than public-urination criminal.

“Hmm. Or how about a bedwetter?”

“Y-you little…”

“If you don’t like that, then *Little Pee-er of the New Nation*.”

“This old man did not piss himself!”

“Then *The One Who Peed*. *A Midsummer Night’s Pee*, featuring the Kunlun Sect.”

“……!”

I clicked my tongue as I looked at the Heavenly Power Demon, who couldn’t even come up with a proper retort.

“I don’t know what got into you that made you suddenly start talking to me, and I don’t want to hear it or exchange words with you. So eat your food and shit as much as you like. Shit or piss, I don’t care. Do both at once, for all I care.”

“W-wait.”

Good grief. What a pain.

I had finished handing out the food and was just about to leave the underground prison when I turned around with an irritated expression.

“What?”

“There is something I wish to ask.”

“If you have something to ask, am I obligated to answer?”

But the Heavenly Power Demon, seized by an inexplicable desperation, refused to back down. Wearing scraps of what might once have been called clothing, he opened his mouth with a gleam in his eyes.

“The Divine Cult. What has become of the Divine Cult?”

“The Divine Cult?”

“Yes, the Heavenly Demon Divine Cult!”

“Oh. The Demonic Cult.”

I had been momentarily confused because the two sides called it by different names.

To most Murim warriors, including me, it was *your* Demonic Cult. But from the Demonic Cult’s perspective, it could only be *our* Divine Cult.

Especially for the Heavenly Power Demon standing before me. Wasn’t he a fiend whose notoriety had once been considerable even among the Demonic Cult’s members?

“What, have you been locked up so long that you’re feeling homesick?”

“Tell me.”

“That’s not difficult.”

I gave a short laugh and continued.

“I don’t know either.”

“……What did you say?”

“How would I know what that Demonic Cult buried way off in the distance is doing? If some new inmate from the Demonic Cult ends up using the cell next to yours, you can ask him.”

The Heavenly Power Demon looked at me as if he couldn’t understand me at all.

“You are the Fire King’s successor. Yet you claim to know nothing about the Divine Cult?”

“……How did you know that?”

“Although my dantian is ruined, these old ears still function.”

“You’re quite spry for a man old enough to have one foot in the grave. How much do you know?”

“That the Fire King is here receiving treatment for his injuries.”

“Hmm.”

He was a rather perceptive old man.

Cheongpung had mentioned Jeok Cheongang’s name several times, but never loudly enough for the other prisoners to hear. Even if the Heavenly Power Demon had heard him, it would have been difficult to infer the circumstances from their conversations.

*He keeps his mouth shut but his ears open.*

He was different from the other prisoners, who tried to persuade anyone they could at the slightest opening.

I found myself growing slightly interested in the old man before me.

“But why are you so curious about news concerning the Demonic Cult? You’ve been captured for a long time already.”

“It has been more than forty years.”

“The Great Faction War had already ended around then. Don’t you have some idea of what happened?”

“Some idea?”

The Heavenly Power Demon gave a bitter smile and continued.

“Few people know the Divine Cult better than this old man.”

“Sounds like you pissed on things there too.”

“This old man was once an Elder of the Great Heavenly Demon Divine Cult. It was I who, obeying the solemn command of the Cult Leader, subjugated Qinghai Province and opened the first front of the holy war.”

“Holy war my ass.”

Despite my curt response, I was secretly surprised.

*He’s a bigger deal than I expected.*

From the bits and pieces I had heard, the Demonic Cult had something called the Ten Elders or the Seven Elders—great fiends who held tremendous power.

I had assumed he wasn’t an ordinary fiend after seeing him piss all over the Kunlun Sect’s signboard. But I had never imagined that the shabby old man waiting to die in an underground prison had once been an Elder of the Demonic Cult.

“You knew nothing about this old man, I suppose.”

“Of course not. That was ages ago. I heard the title Heavenly Power Demon for the first time today.”

“……Heh. Has it truly been that long?”

As I watched the Heavenly Power Demon let out a hollow, self-deprecating laugh, I leaned my back against the wall of the prison.

“So what does a former Elder of the Demonic Cult from forty years ago want to ask me?”

“Tell me everything you know about the Divine Cult. All the news you have heard recently, without leaving anything out.”

“I don’t know. Something about this feels unpleasant.”

“This old man has already passed his ninetieth year. Both body and spirit are exhausted. This is the final request of an old man who has already been given his day to die.”

“The request of a fiend who committed all kinds of atrocities, you mean.”

“Atrocities…”

“I will willingly accept punishment for the lives I have taken. But what, exactly, does it mean to be a demon? The Divine Cult and your people opposed each other for many years, each relying on its own beliefs, and we merely lost a battle in which we wagered our fate. That is all.”

The Heavenly Power Demon continued in a clear voice, almost lamenting.

“Do you claim that such a thing alone is enough to determine who was right and who was wrong? The world back then was like a keg of explosives that could go off at any moment. If your side had been the first to cross Gansu and Qinghai and reach the Divine Cult, you would have slaughtered our followers under the shabby pretexts of the greater good and rooting us out at the source.”

“But from what I’ve heard…”

“Boy.”

I closed my mouth at the quiet voice.

A pair of eyes, blazing more fiercely than ever, stared at me.

They did not belong to an old man whose martial arts had been completely crippled and who was waiting for the day he would die.

They belonged to a general and Supreme Peak master who had once led an entire force and swept across the world.

“This old man saw it and experienced it firsthand. I saw how cruel human beings could become in a war of killing and being killed. Neither the followers of the Divine Cult who shouted for a holy war nor the Sect Leaders of the Nine Sects and One Gang who called for the destruction of demons were exceptions. Even…”

At that moment, the fire in his eyes faded, and only his bitter voice remained, scattering through the air like ash.

“Even the Cult Leader of the Divine Cult was like that. He lost the beliefs he had started with and fell into corruption. Yes. Perhaps, as you orthodox faction warriors claim, the Divine Cult really was a Demonic Cult.”

The Heavenly Power Demon’s words left my thoughts tangled.

In a way, what he had just said overlapped with something I had realized recently.

*There are good people and bad people everywhere.*

The Demonic Cult and the orthodox Murim had been at odds for ages, each holding a match and watching the other beside a powder keg that could explode at any moment.

The Demonic Cult had been the one to light the fuse in the end. But what if the orthodox faction had lit it first?

Would the Roaring Fury Swordsman and the Taeeul Merciless Sword have left ordinary Demonic Cult civilians who knew nothing about martial arts alone?

*No way.*

For a moment, those two men and the Heavenly Power Demon overlapped in my mind.

Who was white, and who was black? Was there something unknown hidden in the history that had already passed?

*Damn it. I don’t know.*

I bit my lip hard and pulled my back away from the cold wall.

“Telling me things like that won’t do you any good.”

The Heavenly Power Demon nodded weakly.

“……I know. Nothing is more futile than talking about the past that has already passed.”

“I’m not as well-versed in the Demonic Cult as you think. If a knowledgeable beggar had been here in my place, he might have been able to give you the news you want.”

“Did the Divine Cult fall?”

“I don’t know. It doesn’t seem that way. From what I’ve heard, it has managed to maintain its existence somehow.”

It was only because the name Dark Heaven had been attracting so much attention lately, but the Demonic Cult was still the orthodox Murim’s eternal archenemy by default.

On top of that, with its connection to Dark Heaven now under suspicion, the Murim Alliance’s headquarters in Henan was probably busy investigating both the Demonic Cult and Dark Heaven.

“I did hear that it shrank miserably after suffering an enormous blow during the Great Faction War.”

The Central Plains was not called the center of the world for no reason.

Unlike the orthodox Murim, which had recovered a considerable portion of its losses by absorbing the region’s abundant resources, goods, and population like a sponge, the Demonic Cult had been forced into the Tianshan Mountains while bearing the full weight of its tremendous losses.

“……Of course. It was a war that mobilized the full strength of the Divine Cult.”

He muttered quietly, a self-deprecating smile appearing at the corner of his mouth.

“Heh. We once devoured half the world, and now we are utterly pathetic. I should have stopped the Cult Leader, even if it cost me my life, when he accepted vicious criminals like the Qilian Three Fiends and the Yin-Yang Twin Ghosts. Though, come to think of it, that was when the Cult Leader began to change as well.”

“The Yin-Yang Twin Ghosts?”

“You may not know them, but there were men like that long ago…”

“Oh, I know them.”

“What? You know the Yin-Yang Twin Ghosts?”

I nodded as if it were obvious.

“I don’t know much about the Qilian Three Fiends, but I know the Yin-Yang Twin Ghosts.”

“How could someone who has never even heard this old man’s title know the Yin-Yang Twin Ghosts?”

“Well, you see…”

I scratched the back of my head and continued.

“I tend to remember the title of anyone I’ve fought. Especially when they’re masters of that caliber.”

“……W-what? You fought the Yin-Yang Twin Ghosts?”

“Technically, I only fought one of them—the Yang Ghost. Our Old Master—no, Master—killed the Yang Ghost. The Yin Ghost was killed by some crazy bastard and followed his friend to the afterlife. Anyway, do these fucking bastards think Henan is Gotham City…?”

“……!”

The Heavenly Power Demon froze with his mouth hanging open. Then he hurriedly poured out his words.

“T-the Yin-Yang Twin Ghosts! How did those men survive and emerge into the Murim? And in Henan, no less? Did the Divine Cult raid Shaolin?”

“They did make a hell of a mess at Shaolin. But it wasn’t the Demonic Cult’s doing.”

“Th-then who did it? Whose doing was it?”

I had expected as much, but the Heavenly Power Demon really knew nothing about how the current Murim worked.

The only outsider he had spoken with was Old Man Gung.

*Well, it’s not like that old man is the type to kindly explain things.*

Not unless he considered severing tendons a form of kindness.

After thinking for a moment, I decided to tell him the truth.

The Heavenly Power Demon had no chance of leaving the underground prison before his death anyway.

And now that Dark Heaven, once a top-secret matter, was gradually spreading through word of mouth among several major sects, there was no reason it would cause trouble.

“Um, I’m not sure how to put this.”

“Tell me. Quickly!”

“Wait a second.”

Ah, right.

At last, I found the right term. Admiring my own cleverness, I opened my mouth.

“They changed jobs.”

“……?”

“I’m not sure whether it was a job change or an internal departmental transfer, but until they died, they were working for someplace called Dark Heaven instead of the Demonic Cult…”

In the end, I couldn’t finish speaking.

The sound of hurried footsteps approached, and a familiar face appeared.

“B’factor!”

“Swallow what’s in your mouth before you talk.”

“B’factor! B’factor! Try this too! It’s delish!”

“What’s with all the ‘B’factors’? Are you looking for the police chief who lives in Namcheon-dong?”

“B’factor!”

“Yeah, yeah. You probably hit the sauna, ate together, and did the whole nine yards.”

“It’s weally delish!”

Cheongpung had stuffed both cheeks full of snacks, and he was still carrying an armful of food wrapped in paper.

I pulled out a well-roasted duck leg and was about to bite into it when I held it out toward the person I had momentarily forgotten.

“Want some?”

And at last, I came face-to-face with the sight of the Heavenly Power Demon, frozen like a stone statue.

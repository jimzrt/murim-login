# Checkpoint Review — 480–484

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

# Chapters 480–484

## Plot

After the Water God Dragon’s rampage, Mungyeong treats Gwak Bongchul, an elderly boatman who survived the disaster, and uses internal energy to suppress his memories. He gives Gwak a cover story and warns him to sell his boat and remain silent, fearing the Hubei City Lord may eliminate witnesses.

Clinic rumors reveal that the authorities are blaming captured dark-path figures for the Hubei incidents. Mungyeong, Jeok Cheongang, and Taekyung discuss the Dongting Fisherman’s critical injuries when Gung Gibang reports finding Honglan’s trail. Her military vessel is discovered at Red Cliffs: ninety-four people have killed themselves under her Soul-Seizing Technique, while the surviving officer, Song Ho, is remotely controlled. Honglan speaks through him, identifies herself as the Southern Heaven Demon Empress, confirms her connection to Dark Heaven and Lord of Heaven, and then abandons the officer, killing him.

Cheongpung reports that Zhuge Feng located the Gate from the Water God Dragon’s memories. Taekyung’s group travels to the site, passing security provided by Wudang, the Zhuge Clan, and the Beggars’ Sect. Zhuge Feng explains that the area was enclosed and drained for investigation. Taekyung discovers a massive fissure running through the ancient cliff and triggers an ominous System notification when he touches it. Meanwhile, Honglan travels toward Yunnan in an Escort Bureau carriage, anticipating further deaths.

## Continuity

- The Water God Dragon is dead; its purified Origin Essence became Taekyung’s inner core.
- Honglan corrupted the benevolent Dongting Lake imugi and used it to cause the Hubei and Dongting Lake tragedies.
- Honglan is the Southern Heaven Demon Empress. She serves Lord of Heaven, belongs to Dark Heaven, and can enthrall people, remotely control them, and speak through their bodies.
- Honglan killed ninety-four people aboard the military vessel through the Soul-Seizing Technique. Song Ho, the sole survivor, died after she abandoned his body.
- Honglan is traveling toward Yunnan and expects to cause further deaths.
- Hubei authorities concealed the Water God Dragon incident, blamed local dark-path figures, and redirected public anger toward Dark Heaven.
- Gwak Bongchul survived but was instructed by Mungyeong to forget the disaster and follow a fabricated account; whether the memory alteration holds is unresolved.
- The Dongting Fisherman remains alive but severely injured after the encounter at Donghu Stronghold.
- Jin Wikyung and Gung Gibang pledged the Jin Family of Taiyuan and the Beggars’ Sect to Taekyung’s defense.
- Zhuge Feng located the Gate site from the Water God Dragon’s memories. The exposed fissure there triggered an ominous System notification when Taekyung touched it.
- The fissure’s contents, the Gate’s creator and purpose, its relation to demonic qi and Dark Heaven, the Dongting Fisherman’s exact role, and the shared symbols linking Dark Heaven to the Arch Lich remain unresolved.

## Translation Decisions

- Render 광폭화 as **Berserk**, 원정 as **Origin Essence**, 내단 as **inner core**, 꽃뱀 as **flower snake**, 섭혼술 as **Soul-Seizing Technique**, and 남천마후 as **Southern Heaven Demon Empress**.
- Preserve established terms including **Water God Dragon**, **Dark Heaven**, **Gate**, **Force**, **Sword Energy**, **Hellfire**, **Water Breath**, **whiskers**, **Jangsu stone bed**, **hyojason**, **live-fish sashimi**, **bone-in sashimi**, **workers’ compensation**, **tearing apart by chariots**, **Miao people**, **femibista**, **Great General**, and **Great Government War**.
- Retain explanatory footnotes for **flower snake**, **Jangsu stone bed**, **hyojason**, and **gukbap** where used.
- Preserve Taekyung’s profane contemporary humor, Cheongpung’s literal innocence, Mungyeong’s calm coercion, and Jeok Cheongang’s blunt threats.

## Durable state

{
  "active_continuity": [
    "The Water God Dragon died after regaining its reason and giving Taekyung its purified Origin Essence, which humans call an inner core.",
    "Honglan corrupted the benevolent Dongting Lake imugi and used it to kill many people.",
    "Honglan can enthrall people by seizing their emotions and souls, and she can speak remotely through a controlled person's body.",
    "Honglan identifies herself as the Southern Heaven Demon Empress, serves Lord of Heaven, and confirms that Dark Heaven has many eyes and ears, including Blood Lord's reports.",
    "The Gate or rift that corrupted the Water God Dragon remains connected to unresolved questions involving demonic qi and Dark Heaven.",
    "The Dongting Fisherman is alive but severely injured and may be connected to Dark Heaven and the earlier destruction inside the secret refuge.",
    "Gung Gibang traced the vessel connected to Honglan to Red Cliffs.",
    "Cheongpung reported that Zhuge Feng found the Gate site from the Water God Dragon's memories.",
    "Jin Wikyung and Gung Gibang pledged the Jin Family of Taiyuan and the Beggars' Sect to Taekyung's defense.",
    "The Southern Heaven Demon Empress is traveling toward Yunnan and expects to cause further deaths.",
    "Hubei authorities concealed the Water God Dragon incident and suppressed local dark-path forces to redirect public anger toward Dark Heaven.",
    "The exposed fissure at the Water God Dragon's site triggered an ominous System notification when Taekyung touched it."
  ],
  "continuity_sources": [
    483,
    484
  ],
  "open_questions": [
    "What lies beyond the exposed fissure, and why did touching it trigger an ominous System notification?",
    "Where is the Southern Heaven Demon Empress ultimately headed, and what does she intend to do in Yunnan?",
    "What is the Dongting Fisherman's exact role within Dark Heaven, and how was he connected to the earlier destruction inside the secret refuge?",
    "What are the origin and purpose of the symbols shared by the Arch Lich's magic circle and Dark Heaven's formations?",
    "Who created or controlled the Gate that corrupted the Water God Dragon, what is its purpose, and how is that power related to Dark Heaven?"
  ],
  "safe_through": 484,
  "temporary_decisions": [
    "Render 광폭화 as Berserk and preserve the System Status distinction.",
    "Render 장수 돌침대 as Jangsu stone bed and 효자손 as hyojason, each with an explanatory footnote when used.",
    "Retain established jang and geun measurements, established renderings of live-fish sashimi and bone-in sashimi, and gukbap with an explanatory footnote.",
    "Continue rendering 수염 as whiskers; distinguish Force, Sword Energy, Hellfire, and Water Breath.",
    "Render 원정 as Origin Essence, 내단 as inner core, 꽃뱀 as flower snake, 산재처리 as workers’ compensation, 거열형 as tearing apart by chariots, 섭혼술 as Soul-Seizing Technique, 남천마후 as Southern Heaven Demon Empress, 묘족 as Miao people, 페미비수타 as femibista, 대장군 as Great General, and 정관대전 as Great Government War."
  ],
  "version": 1
}

## Reading copies

## Chapter artifact 480

# Chapter 480

“Ugh.”

The wrinkled skin around the old man’s eyes twitched. He tossed and turned with a groan, then finally opened his eyes after a long while.

*Where is this…?*

Instead of damp, yellowing wallpaper, he saw a ceiling so starkly white that it was almost oppressive.

The old man lay there blankly, unable to make sense of the situation, until a calm voice reached his ears.

“Are you awake?”

“U-uh…?”

Finding the owner of the voice was not difficult.

The old man sat up with a start and saw a young man sitting before a small brazier and looking at him.

“Wh-who might you be?”

“There are ultimately only two kinds of people in a clinic: medical apprentices and patients. Since you still belong to the latter category, you should lie back down.”

“Ah.”

Only then did the old man realize that this unfamiliar place was a clinic. He also realized the identity of the young man, who looked barely more than a boy.

“So you’re a medical apprentice, sir. But why am I in a clinic… Ow.”

The old man had been speaking with a bewildered expression when a sudden headache rose through him, and he let out a groan.

Only now did he realize that his already-aged body ached everywhere, and that he was trembling, drenched in sweat.

*Good heavens. What on earth happened?*

The young medical apprentice had already crossed the room and came to his rescue.

“I’m going to place a few needles now. Relax and breathe slowly. All right. One. Two…”

*Tap.*

“Wha—?”

The old man’s eyes went round. The crown of his head prickled as though an ant had bitten him, and then his headache vanished as if it had been washed away.

The young medical apprentice smiled faintly as he held a slender needle and watched the old man stare at him in surprise.

“Are you all right?”

“Pardon? Yes.”

“Then lie back down. From what I’ve observed over the past two days, there doesn’t seem to be anything seriously wrong, fortunately… but you still shouldn’t be moving around yet.”

“Ah, I-I understand.”

His medical skills were nothing short of miraculous. On top of that, there was something about his presence that made both body and mind feel inexplicably at ease.

Up close, he looked much younger than expected, yet he seemed more seasoned than even an elderly medical apprentice.

“I’ll help you. Relax your body and lie down slowly.”

“Yes, yes.”

As the old man lay back down as though entranced, the young medical apprentice raised several fingers.

“I need to perform a simple check. Elder, how many fingers am I holding up?”

“It looks like three.”

“And now?”

“Two.”

“Correct. Where do you live, and what is your name and age?”

“…Do I have to tell you that too?”

“I need to make sure your mind is completely clear.”

“Hmm. Let me think.”

Unlike before, this required him to use his head a little.

The old man had only just awakened, and his condition was still unstable. Feeling a faint headache, he slowly opened his mouth.

“I’ve lived my whole life near Wuhan and Dongting Lake. My name is Gwak Bongchul. No one kept proper track when I was growing up, so I don’t know my exact age, but I reckon I must be past seventy.”

“So you’re Elder Gwak. You’re remarkably fit for your age. What do you do?”

“I… Well, I…”

The old man frowned and hesitated, but then he remembered his occupation.

“I row a boat.”

“You’re a boatman.”

“Yes. When I was young, I worked as a deckhand on a merchant ship. After buying my own boat, I mostly carried passengers around Dongting Lake and showed them the sights.”

Before long, the old man—no, the elderly boatman—began dredging up old memories and talking on his own. Each time he did, the young medical apprentice responded with a gentle smile and a nod.

“I had a close hyung I worked with. He told me that, ever since olden times, a man who bought a boat would soon find himself a woman. So I took the plunge and bought myself a sleek one. It was a boat made in Baekchu.”

“Is that so?”

“I wonder if you know Baekchu, sir. These days, you can find those boats everywhere at the Wuhan ferry docks, but when I was young, a man who piloted a vessel made in Baekchu was considered a first-rate husband prospect. Or an Audi. You know, the one with four circles on the bow.”

“That sounds somewhat like Five Qi Returning to Origin.”

“Huh? What’s Five Qi Returning to Origin?”

“It’s something. Let’s move on.”

“Anyway, that boat I bought back then was sleek and beautiful. It attracted plenty of women, too. Once, a widow from the neighboring village came to see me late at night and asked me to show her the Baekchu. Then she suddenly yanked her dress ties open…!”

“…Let’s skip a little farther ahead.”

The young medical apprentice listened with patience far beyond his years, and as the story continued, the dam blocking the boatman’s memories slowly began to crumble.

Then, as the boatman cheerfully continued talking without even noticing his aching body, one particular memory suddenly came back to him.

He froze like a stone statue.

“……!”

It was a bolt of lightning.

A memory like a nightmare.

*Rumble. Boom!*



*Graaaaaaah!*



Thunder and an enraged roar rang clearly in his ears.

He slowly blinked, and the figure of a massive being standing against a black sky flashed before his eyes.

“Gah!”

The boatman sprang upright without realizing it and stared blankly into the air.

“W-wait. Wait a moment.”

His voice trembled, and his eyes were wide open.

Perhaps because he had exerted himself so suddenly, every part of his body began aching again. But the boatman paid no attention to any of it.

The memories that had surfaced as the dam in his mind collapsed were all he could think about.

“Me-medical apprentice! What did you say to me earlier?”

“What are you referring to?”

“Two days! Didn’t you say that two days had passed?”

*Grab!*

A grip far too strong for a man over seventy clamped around the medical apprentice’s slender wrist.

But the young medical apprentice did not so much as twitch an eyebrow as he calmly replied,

“That is correct.”

“Good heavens. How could this happen?”

“Calm yourself, Elder.”

“T-this is no time to be calm. We must tell the people and report this to the higher-ups at once!”

The boatman was half out of his mind.

His entire body was drenched in sweat and trembling without his realizing it, while his unfocused eyes darted anxiously in every direction.

It was as though something might devour him at any moment.

“We have to get away as quickly as possible. Hurry!”

That was when the young medical apprentice reached out toward the patient shouting as though he were having a fit.

*Swish.*

A perfectly white hand, without even a callus, touched the old man’s slightly hunched back. Warmth flowed from the hand and filled his body.

The inexplicable phenomenon finally calmed the boatman, and he gasped for breath.

“Wh-what was that?”

“Think of it as a miscellaneous technique I’ve practiced from time to time. And, Elder.”

“Gasp.”

Why, he could not say, but the boatman met the medical apprentice’s deep, clear eyes and felt the words catch in his throat.

The young medical apprentice gazed at him for a moment before slowly continuing.

“The thing you’re worried about will never happen. Do you understand?”

“Pardon?”

“It’s simple. Erase everything you saw, heard, and experienced from your mind. Two days ago, you were summoned to Dongting Lake with the government troops, but you collapsed because you were feeling unwell. You woke up today.”

“P-please wait a moment.”

“Everything I’m telling you is true. It must become true. That day, you did not take any passengers, and you did not see the divine spirit of Dongting Lake.”

“……!”

The boatman shuddered as though he had been struck by lightning.

The young medical apprentice’s words were that shocking.

“D-does that mean you saw the divine spirit too, sir…?”

“That may be the case, or it may not. But there is one thing you must remember… You must forget everything you remember about those events.”

The boatman swallowed hard at the young man’s gentle yet blade-cold voice.

The next moment, the suffocating silence in the room was broken by the last bit of courage possessed by a man over seventy.

“D-do you intend to kill me?”

“Me? No.”

The young medical apprentice slowly shook his head and continued.

“But someone else may think differently. For example… the City Lord of Hubei Province, who would not want ominous rumors spreading.”

“T-the City Lord!”

The City Lord of Hubei Province.

An official who governed a city under the Son of Heaven’s orders—a figure who, at least within Hubei Province, was no different from a king.

The boatman cried out reflexively at the unexpected appearance of such a high-ranking person. Then he realized his mistake, and his vision went dark.

*What a stupid fool! What if someone heard me?*

Unlike him, however, the young medical apprentice’s expression remained relaxed.

It was the composure of someone who had ensured that none of their conversation could leave the room.

No—even if their words did leak out, the young medical apprentice would not bat an eye.

He had taken these precautions solely to preserve the boatman’s life.

Unaware of that fact, the boatman spoke again in a tightly hushed voice.

“I-I want to live. Why on earth would the City Lord want to kill an insignificant boatman like me?”

“When floods come, droughts strike, and plagues spread, people die in every direction, and wars break out everywhere. Then the rebels who dream of becoming kings and high officials speak with one voice. They say that the will of Heaven has left the Son of Heaven. That we should overthrow this rotten country.”

The young medical apprentice clicked his tongue softly, stood up, and tossed out one final remark.

“Even disasters beyond human power lead to this sort of thing. So what would happen if a divine spirit as enormous as a mountain went berserk in Dongting Lake?”

“……!”

“Thousands died. The Yangtze and Dongting Lake were filled with corpses and blood, and the streets that once shone like daylight were swallowed by darkness. With the frightened people watching Hubei Province, what do you think would happen if everyone learned what you saw and heard?”

He did not finish the sentence, but in the suffocating silence, the boatman arrived at the answer on his own.

*I’d die. Without a doubt.*

He had been born into a poor tenant farmer’s family and lived his entire life illiterate, but he had not spent more than seventy years with his eyes and ears closed.

If anything, carrying countless passengers by boat had allowed him to learn how the world worked by listening to their conversations.

*If I so much as speak the facts I know aloud…*

It would all be over.

Neither the Son of Heaven seated upon the throne nor the City Lord of Hubei Province would want people to learn that the mad divine spirit of Dongting Lake had killed thousands.

No, perhaps they would eliminate everyone involved in the matter immediately.

A martial artist from a prestigious sect might be another story, but an old boatman over seventy could be killed without anyone ever knowing.

“Good heavens. Oh, good heavens…”

As the boatman exhaled as though his soul had left his body, a lifeline was extended to him.

“Erase everything from your memory. Sell your boat and spend the rest of your life in silence. If you do that, nothing will happen.”

“W-will that really be enough?”

“That is all I have to say.”

The young medical apprentice finished speaking and rose from his seat. The boatman stared at his departing back with a dazed expression, then hurriedly called out.

“A-are you really a medical apprentice, sir?”

“Of course.”

The young medical apprentice, Mungyeong, answered without hesitation and released the doorknob.

Then he pointed to the brazier still burning in the corner of the room and the kettle slowly boiling atop it.

“I boiled that decoction myself. Three times a day. After meals. Make sure you take it.”

Caring for a patient until the very end was a medical apprentice’s duty.
## Chapter artifact 481

# Chapter 481

*Click. Thud.*

After closing the door and leaving the boatman alone, Mungyeong thought to himself,

*This should be enough.*

Perhaps because he had lived a long life, the boatman was far more perceptive than Mungyeong had expected.

Although he would have to live under the authorities’ watch, that was still a hundred times better than being found dead somewhere without anyone knowing what had happened.

His deal with the City Lord of Hubei Province was already settled. As long as the boatman kept his mouth shut, he could spend the rest of his life in peace.

*No. Even if he tried to tell anyone, they’d obviously just treat him like a crazy old man.*

*And he won’t have to worry about money anymore. This should be a fairly decent arrangement for him.*

Mungyeong suddenly wondered what expression the boatman would make when he found the money pouch left beside the brazier.

And when he heard the words of the person who had handed it over and asked Mungyeong to deliver it.

*Still, he followed us for no reason and nearly died. He deserves hazard pay and workers’ compensation.*

Workers’ compensation?

It was a bizarre term Mungyeong had never heard before, but then again, Jin Taekyung had always been like that.

A boy so young he was practically yellow instead of merely green. And a boy who never stopped surprising him.

*I can’t make sense of him at all.*

Mungyeong could have listed his peculiarities forever, but after everything that had happened, that impression had only grown stronger.

He remembered how Jin Taekyung had rampaged even more wildly instead of shrinking back in the presence of that enormous monster, unlike anything Mungyeong had ever seen or heard of. His brow furrowed.

*Natural courage? That may be part of it, but there was something else… Yes. He looked used to it. Like a battle-hardened veteran who had fought countless battles.*

Had Jin Taekyung become accustomed to strange beings called supernatural powers while fighting Dark Heaven?

Or was there some secret about Jin Taekyung that no one knew?

Mungyeong was lost in thought as he continued walking when he heard voices.

“Physician Song. I heard those bastards who deserve to be beaten to death were captured.”

“Good heavens, ‘bastards who deserve to be beaten to death’? Hyang, you’re a medical apprentice. How can you use such harsh language…?”

In the courtyard of the clinic, where people came and went, a middle-aged medical apprentice of respectable age scolded a young female medical apprentice who did not even look old enough to be twenty. She pouted.

“A medical apprentice is still a person, isn’t she? Besides, those men deserve to die.”

“Ahem. Watch your words. You may be right, but I’m afraid someone might hear you.”

“You’re saying that because of that gentleman, aren’t you? What does it matter? He’s too far away to hear us anyway.”

Of course, unlike the young woman’s carefree assumption, Mungyeong was taking in every sound and movement around him without missing a thing.

The conversation between the two of them was no different.

“What do you think, Physician Song?”

“What are you talking about?”

“Oh, come on. Don’t pretend you don’t know. What else could I mean besides the dark-path figures of Murim who committed those heinous crimes at Dark Heaven’s instigation?”

“What could a mere medical apprentice like me possibly say? Still, I’m simply grateful that the culprits have finally been captured, and I intend to focus on my duties.”

“But isn’t it strange? The Sea Serpent Society ship that sank at Red Cliffs, the tragedy at Dongting Lake, and even the deaths connected to the river bandits beyond Tianling Falls. They’re saying all of it was done by those men.”

“Strange? What do you mean?”

“Well, it’s just… Hmm. You know Sister Hwang, right?”

“You mean the Medical Apprentice Hwang I know?”

“Yes. She told me something. Um…”

The young medical apprentice broke off and turned to look around. Then she rose onto her toes and whispered.

It still sounded as loud as thunder to Mungyeong.

“She said the patient she’s looking after is a pretty famous wandering martial artist, and when he heard the story, he snorted. He said that no matter how many dark-path figures there were, there was no way they could have been a match for the Yangtze One Saber.”

“The Yangtze One Saber?”

“That’s the name—or rather, the sobriquet—of the river bandit chief who suffered a disaster this time. Apparently, his martial arts are so powerful that there isn’t a martial artist anywhere who hasn’t heard of him.”

“…And?”

“According to what the wandering martial artist said, the authorities rounded up so many dark-path figures this time to cover something up.”

Mungyeong let out a quiet laugh inwardly, while the middle-aged medical apprentice’s face stiffened.

“Hyang, have you told anyone else this story?”

“No. I was listening to it just now when Physician Song called for me, so I came straight here.”

“What about Medical Apprentice Hwang? Did anyone else hear it besides you?”

“Why are you suddenly acting like this, Physician Song?”

“Answer me.”

The genial-looking middle-aged medical apprentice’s face hardened as he questioned her. The young woman replied in a tiny voice,

“No one else was there—it was just the two of us. And I was the first person Sister Hwang told.”

“Phew. That’s fortunate, at least.”

“Did I do something wrong?”

“No. You and Medical Apprentice Hwang were merely careless because you’re both still young. But from now on, it would be best not to discuss this matter. Do you understand?”

“Ah. Yes.”

“Hyang.”

The middle-aged medical apprentice gently patted the young woman’s head as she shrank in on herself, then continued kindly.

“Those dark-path mongrels who committed such heinous crimes will be put to death at noon tomorrow—some beheaded, others torn apart by chariots. Their severed limbs will be rolling through the streets of Wuhan, and the ground will be soaked in blood.”

“What?”

“This is all thanks to the City Lord, who acted on the orders of His Imperial Majesty the Emperor, and to Great Hero Jin Taekyung of the Jin Family of Taiyuan, who personally exterminated the culprits. So don’t let yourself be swayed by rumors. Praise those noble men instead.”

“Yes, yes.”

“No, not like that. Repeat after me. May His Majesty the Emperor live ten thousand years! A thousand years to the City Lord! A thousand years to Great Hero Jin Taekyung!”

“L-long live His Imperial Majesty the Emperor…”

“Louder!”

*Is he insane?*

Mungyeong stared at the middle-aged medical apprentice in disbelief and clicked his tongue inwardly.

If even a medical apprentice who could be considered educated acted like this, then the reaction of ordinary people was obvious.

*They’ll praise the Son of Heaven without a shred of doubt. It’s only been two days, so the report about this incident probably hasn’t even reached the imperial palace yet.*

A fabricated lie. A hidden truth.

The world truly never changed.

Mungyeong gave a small shake of his head and continued walking.

After leaving the clinic entirely—it was part of the vast Hubei provincial government compound—he headed straight for a large estate among the many pavilions, one reserved for honored guests.

And there, he found a master and Disciple proudly displaying the depth of their affection for each other.

“Say that again. What? Jeok Cheongang? Shitting?”

“Old Master, please calm down…”

“I’ll pin your limbs down and shit on your face.”

“Whoa. Is that your thing?”

“You fucking piece of—”

“Dormammu, I came to take a shit. Ah, sorry. Muscle memory.”

“I swear on the ancestors of our sect, I’ll stuff shit into your mouth!”

“Waaah! Somebody save me!”

“Get over here this instant!”

*Swish! Swish! Swish! Whoooosh!*

“…”

Watching the fierce chase unfold, Mungyeong suddenly thought,

*What an affectionate—and filthy—master-and-Disciple relationship.*

* * *

Fortunately, Jeok Cheongang did not end up shitting in my mouth.

Of course, that didn’t mean things ended peacefully or normally.

*Bam!*

“Ah, wait a second. That hit bone…”

*Boom!*

“Ugh!”

*Damn it. Isn’t using Flame Divine Palm going too far?*

He had drastically reduced its power, presumably because he possessed at least a shred of human conscience. But still—how could he use Flame Divine Palm against his Disciple? No, against me, who was practically his Disciple?

*My insides are getting nice and warm.*

I didn’t need gukbap.[^1] One bowl of Flame Divine Palm, and my stomach felt stuffed to the brim.

“Ugh…”

As I groaned while clutching my chest, Jeok Cheongang spoke in a sinister voice.

“Stop whining and get up.”

“Is it… over?”

“It’s still far from over. How dare you speak so casually to a master as high as the heavens…”

“Master?”

“Ahem. Not merely a master as high as the heavens, but this old man, who is even higher than the heavens. Do you think I raised you so I could be treated like this?”

“…My mother raised me, though. Why are you taking credit, Old Master?”

“You insolent brat!”

Just as Jeok Cheongang lit both his eyes like candles, a lifeline descended from heaven.

“That’s enough.”

Someone had entered without making a sound. At Mungyeong’s single remark, Jeok Cheongang frowned.

“If you came in, you should have quietly watched. Why did you have to interfere?”

“It seemed excessive, so I stepped in. Is there a problem?”

*Damn. He’s got so much charisma. No wonder his targets ended up in the grave when he was an assassin.*

I looked at Mungyeong with eyes overflowing with emotion.

“Oh, what a saint…”

“Look at this brat. He’s babbling nonsense again. I suppose he’ll need to be beaten for quite a while before he comes to his senses.”

Jeok Cheongang ominously rolled up his sleeve, but Mungyeong shook his head.

“Stop. This is excessive.”

“You’ve been irritating me for a while now. Why do you keep telling me what to do in someone else’s house…?”

“No matter how I look at it, this is excessive. Shouldn’t I get a turn too?”

“Ah. I admit that.”

“…”

*Damn it. So that’s what he meant.*

The moment Jeok Cheongang graciously stepped aside to let the next person take his turn, a pure-white silver line lashed out like a whip.

*Swish. Shhk!*

A chill ran down my spine, and cool air slipped through the gap in my severed clothes.

I swallowed hard as I watched the upper half of my outfit split cleanly into two pieces, left and right.

*Crazy.*

It had come down to a single hair’s breadth.

I stood there with my heart pounding as Mungyeong gazed at me impassively.

“You didn’t dodge.”

“I couldn’t sense any killing intent.”

“You could have dodged anyway.”

“What would have been the point? If I dodged, I’d just get hit twice instead of once. You weren’t planning to kill me anyway, were you?”

“As expected, you’re strange. Strange enough to put me in a bad mood.”

*Really? For someone who’s in a bad mood, your expression is pretty ambiguous.*

Jeok Cheongang, on the other hand, looked unmistakably pissed off.

“How dare you swing a sword at my Disciple?”

“Disciple?”

At Mungyeong’s questioning repetition, Jeok Cheongang hastily corrected himself.

“How dare you swing a sword at that bastard who isn’t even fit to be called my Disciple?”

“Is that really something you can say after beating him like a dog while using martial arts?”

“Whether I beat him like a dog or drive him like an ox, I’m the only one allowed to do it! And use your fists! Not a sword!”

“…”

I knew he was trying to look out for me, but somehow, that only made me feel sad.

Mungyeong narrowed his eyes as he listened to Jeok Cheongang’s utterly incoherent argument.

“Just standing here is making me feel my innate qi withering away. Enough. I didn’t come here for this sort of pointless exchange.”

Before Jeok Cheongang could say anything else, I hurriedly spoke up.

“Are you coming back from the clinic?”

“Yes. I went to check on the Dongting Fisherman and meet the boatman.”

“How are they?”

“The boatman has regained consciousness. There are no unusual symptoms, and he understands everything clearly. The Dongting Fisherman, on the other hand… isn’t doing well.”

I nodded heavily.

The boatman had lost consciousness from a Pressure-Point Strike before he was properly exposed to Fear.

The Dongting Fisherman was the exact opposite. This was only my guess, but he had evidently encountered the Water God Dragon in Donghu Stronghold and been seriously exposed to Fear.

“He must be in pretty bad shape. Though I suppose it’s only natural that he’s not in his right mind…”

“His injuries are severe.”

“What?”

“His limbs were crushed, and he has considerable internal injuries. He’s a Supreme Peak master, and the City Lord gave him an elixir, so he should recover quickly. But it seems that imugi really did a number on him.”

“…”

“What’s wrong?”

“…Nothing. It’s nothing.”

It seemed I had forgotten to tell him.

I had truly, genuinely forgotten.

I’d had plenty of opportunities to mention it during the past two days, but I had forgotten anyway.

*I’d also been a little preoccupied.*

Of course, the reason for that was because I had been pursuing one person.

Honglan. The mastermind behind this entire incident.

The woman who had corrupted the imugi that had guarded the Yangtze and Dongting Lake for more than five hundred years, bringing countless deaths in its wake.

And the woman I had never managed to find.

*Where the hell did she run off to?*

I was lost in thought as I stared at the silver hairpin I had taken out without realizing it.

*Bang!*

Someone burst into the courtyard, throwing open the main gate as if they intended to break it down.

Gung Gibang must have used his movement technique at full speed to get here, because he was breathing heavily when he spoke.

“Huff. Hah… I found a trace of Honglan.”

“……!”

[^1]: *Gukbap* is rice served in a hot, hearty soup, a common Korean comfort food.
## Chapter artifact 482

# Chapter 482

“We found a trace of Honglan.”

Gung Gibang’s announcement did not agitate only me. Immediately after the battle with the Water God Dragon ended, Jeok Cheongang and Mungyeong—both of whom already knew what we had learned about Honglan’s identity—reacted as well.

“You found that goddamned bitch?”

“What happened?”

After Jeok Cheongang’s blunt question and Mungyeong’s infuriating inquiry, still made while concealing his identity, I spoke with a hardened expression.

“A trace?”

The result was what mattered.

Gung Gibang had not said they found Honglan. He had clearly said they found *a trace of Honglan*, and the meaning was obvious.

“You didn’t find her.”

Gung Gibang, who had only just caught his breath, nodded.

“Not yet. But I’ve sent messenger pigeons to not only the disciples of our sect but also Wudang, the Zhuge Clan, and the government troops, so soon—”

“No. You won’t find her.”

I answered firmly and continued.

“If she were easy enough to catch, we would have picked up her trail long ago.”

The government troops were idiots with nothing but numbers. The Beggars’ Sect, Wudang, and the Zhuge Clan were at least reliable, but the idea of them finding Honglan…

Well. No matter how I looked at it, the odds were slim.

Even setting aside my gut feeling that there was no way she would be caught this easily, if she had a Moving Formation hidden nearby, we would all be left like dogs staring helplessly at the roof after the chicken got away.

“But what exactly did you find a trace of, and where? Tell me everything.”

“A military vessel was found at Red Cliffs.”

“Could the military vessel you’re talking about be…”

“That’s right. It’s the very vessel where Honglan was last seen. The authorities have already confirmed it.”

Two days ago, shortly after we left to find the Dongting Fisherman, the government troops had tried to move Honglan to the Hubei provincial government.

She was the only survivor who had lived through the incident alongside the imperial relative Ju Wongong. On the surface, she was also the chief contributor who had rescued Ju Wongong alongside me. From the authorities’ perspective, it was the obvious choice.

*Though that was the last time anyone saw her.*

After that, the military vessel Honglan had boarded vanished like a ghost.

So did the roughly one hundred government troops and sailors aboard it.

And now Gung Gibang had brought us news that the very same vessel had been found.

“…And? What happened?”

In truth, I already knew the answer before I asked.

*They’re probably all dead.*

I had already heard that the people who boarded the vessel with Honglan were ordinary men with no connection to Dark Heaven.

There was no way Honglan had tossed them a few coins for their trouble, waved goodbye peacefully, and gone on her way.

The grim expression on Gung Gibang’s face only supported my guess.

Except—

“Ninety-four in total. Every one of them committed suicide by stabbing themselves in the throat.”

“What?”

I had not expected that.

I blinked silently, then somehow managed to force out my voice.

“All those people… committed suicide together?”

“Without a doubt. They used the daggers that government troops carried as standard equipment and stabbed themselves in the throat. When the bodies were examined, they were said to have died with smiles on their faces. Of course, Honglan was nowhere to be found.”

“What the hell?”

I would not have been this shocked if Honglan had simply killed them herself.

But this was a kind of death far beyond anything I had expected.

A mass suicide.

And they had been smiling?

For a moment, I could not continue. Then Mungyeong and Jeok Cheongang both spoke almost simultaneously.

“This is…”

“Yeah. It has to be the Soul-Seizing Technique. And a very powerful one.”

The Soul-Seizing Technique.

As the name suggested, it was one of the monstrous martial arts and supreme techniques that bewitched and controlled an opponent’s soul.

I knew what it was because it had often appeared in the wuxia novels I had read in the past, but this was the first time I had encountered it in the Murim.

“Wait. That actually exists?”

Jeok Cheongang stared at me as though I had said something absurd.

“Is that something the man who took down a five-hundred-year-old imugi should be saying?”

“…Well, when you put it that way, I don’t really have anything to say.”

“For ages, the Demonic Cult has been the central seat of the Thousand-Year Demonic Path. Dark Heaven is the successor of that very Demonic Cult. It would hardly be strange for people who use the Soul-Seizing Technique to be running wild.”

“But you said before that the Soul-Seizing Technique was nothing special.”

“That’s only true against this old man. The reason that wretched witch Honglan didn’t use it on you from the beginning is probably similar.”

“Because I’m a Supreme Peak master?”

“Breaking through a wall means that one’s body and mind have reached a supreme realm. And how much more so for you, with your Middle Dantian awakened?”

Jeok Cheongang paused there, then suddenly frowned and added,

“No. Perhaps what that bitch wanted was for you to fight the imugi.”

“Either way, what matters is that the culprit is a master of the Soul-Seizing Technique and that she vanished like a ghost.”

Mungyeong quietly joined the conversation. Gung Gibang shook his head.

“There’s one more thing.”

“…What?”

“The investigation found that there were ninety-six people aboard the military vessel in total. Even excluding Honglan, that leaves one person.”

“Wait. If that’s the case…”

“There’s one survivor. The officer in charge of the military vessel, and a military officer attached to the Hubei provincial government.”

“……!”

A survivor?

Everyone, myself included, stared wide-eyed at Gung Gibang. After swallowing hard, he continued.

“He’s on his way here now.”

A brief silence followed.

Then Jeok Cheongang spoke with a stiff expression.

“By the way, is speaking informally to this old man a trend among young people these days?”

“…I wasn’t speaking to Great Hero Jeok.”

“You won’t come to your senses until you’ve been beaten like a dog on slaughter day. Get down.”

* * *

“His name is Song Ho. He is the son of a prominent merchant family in Hubei Province, and his father pulled strings to secure him a post under the City Lord of Hubei Province. Two days ago, the City Lord dispatched him with orders to bring in the culprit.”

The middle-aged man, whose looks must have broken plenty of women’s hearts in his youth, continued in an anxious voice.

“He was a womanizer and had been involved in several scandals, but it’s true that he showed talent in both literary and martial pursuits from a young age. The City Lord kept him close not merely because of his father’s influence, but because he was sharp and dependable when it came to handling matters.”

I didn’t know what he had been like before, but he certainly didn’t seem that way now.

I ignored the middle-aged man—the Hubei Branch Leader of the Lower District Sect—and watched the young man sitting there bound in ropes.

His skin was dry and rough. His eyes were unfocused, as though he had been possessed by a ghost, and clear saliva dripped from the corner of his open mouth.

*Drip. Drip.*

Jeok Cheongang watched the young officer mindlessly drooling and narrowed his brow.

“He’s been thoroughly caught by the Soul-Seizing Technique. He isn’t in his right mind anymore.”

I agreed with Jeok Cheongang completely.

There was no trace of reason left in the young man before us. Instead of a promising military officer, a doll with its soul pulled out was sitting there.

“How is his condi—how is he?”

At my hurried correction, Mungyeong slowly shook his head.

“It’s hopeless. I cannot say what prolonged observation might reveal, but at present, he does not appear to have even the slightest chance.”

“If there’s no hope, how bad is he?”

“When one’s soul has left the body, it is no different from death. In this state, he will not be able to speak or act on his own.”

His condition was far worse than I had expected.

Jin Wikyung, who had hurried over after hearing that the sole survivor had been escorted here, spoke up.

“Would another renowned physician have a different opinion?”

“No matter who examines him, they will reach the same conclusion. If their opinion differs from mine, they are probably a quack.”

“Good heavens. Even if the Divine Physician examined him?”

“…Yes.”

*Hyung. That’s the guy.*

I swallowed the words rising in my throat. The Hubei Branch Leader of the Lower District Sect—who had briefly been treated as an agent of Dark Heaven after mistaking Honglan’s identity—bowed repeatedly and withdrew.

And it was at that exact moment, while the room was briefly silent, that—

“Ah… uh… oh.”

“……!”

A cold chill rose up my spine.

Everyone around me, myself included, stared at the young officer with our eyes wide open.

His two eyes were still hazy and unfocused. But his slack mouth began to twitch little by little, and a voice seeped out.

“Uh… ah.”

“…That’s impossible.”

Mungyeong muttered with an expression of disbelief.

He had cared for and treated countless patients. With medical skill worthy of the title Divine Physician and the martial prowess of a Supreme Peak master, Mungyeong’s confident diagnoses were practically absolute laws.

Or at least they had been until a few seconds ago.

“What is this?”

Mungyeong rarely raised his voice, but now he did as he swiftly took the officer’s pulse.

His expression grew as complex and subtle as it had been when he looked at the Water God Dragon.

“It’s definitely unchanged. So why?”

And then everyone present, myself included, heard it.

The voice that flowed between the officer’s lips.

“Nothing is absolute, and nothing remains unchanged forever. You’d think you would have learned that by now. Don’t you agree?”

“……!”

It was unmistakably a man’s voice, and unquestionably the officer’s.

But Gung Gibang and I both recognized the trace of someone else in it. We looked at each other and shouted the same name at the same time.

“Honglan!”

It felt as though a bolt of lightning had pierced the crown of my head.

If Hyuk Mujin and Cheongpung had been here, they would have reacted the same way.

I looked at the young officer—or rather, at Honglan, confronting me from some distant place through the officer’s body—with a sunken gaze and spoke.

“Where are you, you fucking bitch?”

“Oh my. Our Young Master has a rougher mouth than I expected. Men who swear at women aren’t very popular, you know.”

“Fuck that. I’ve never been popular anyway.”

“I didn’t expect that answer. You really are a masterpiece.”

“Cut the bullshit and tell me where you are. I’ll turn you into a rag.”

“You’re cuter than I’d heard. And you’re funny, too.”

Her familiar, clear laughter slipped out through the officer’s lips.

The corners of his mouth remained the same while only her voice came out of them. The sight was enough to raise goose bumps.

Even so, I did not miss one important phrase.

“…Than you’d heard?”

“You already know, don’t you? We have many eyes and ears. Blood Lord did most of the talking.”

“Dark Heaven. Yeah, figures.”

Even a 99.9 percent possibility was nothing more than a guess if it lacked the final 0.1 percent.

Honglan had revealed her affiliation without the slightest hesitation and continued in a bright voice.

“I was surprised. You’ve become much stronger than Blood Lord said you were. Still, if you were only that strong even now, the Western Heaven Demon Lord would have killed you before the imugi got to you.”

Why was this happening?

My anger showed no sign of fading, yet my mind and voice were growing calmer instead.

Unlike before, I asked in a surprisingly composed voice,

“Who are you?”

It was nothing more than a genuine question.

Even as I asked, I did not expect her to answer willingly.

But Honglan shattered my expectations with a single word.

“The Southern Heaven Demon Empress.”

“The Southern… Heaven Demon Empress?”

*These fucking bastards are really screwing around in every direction—east, west, south, and north.*
## Chapter artifact 483

# Chapter 483

“Southern Heaven… Demon Empress?”

Honglan—or rather, the Southern Heaven Demon Empress, inhabiting the body of a young military officer—spoke in a lighthearted tone.

“It’s embarrassing to hear that sobriquet from someone else’s mouth.”

“Embarrassing my ass. You bastards are raising hell in every direction—east, west, south, and north. So is the eastern one the East Virgin Forever-Alone, and the northern one North Korea’s Kim?”

“You got them roughly right, despite the different sobriquets. You’re smarter than I expected.”

“…Damn it.”

Western Heaven Demon Lord and Southern Heaven Demon Empress.

Even Mimi-chan could tell that those sobriquets had been created with the four directions in mind.

The Western Heaven Demon Lord was already a monster I had barely managed to take down after several brushes with death. And there were at least three more like him?

But an even more important question remained.

I stared at the military officer’s vacant expression and opened my mouth.

“How did you do it?”

“Oh my. What could possibly have our Young Great Hero so curious?”

“You know what I’m talking about.”

A strange light suddenly flashed in the officer’s slack eyes.

The Southern Heaven Demon Empress, gazing at me through someone else’s eyes, casually tossed out a single sentence.

“You saw it, didn’t you?”

“……!”

“There’s no way you found it in only two days. So I suppose a spirit creature really is a spirit creature. Then again, a five-hundred-year-old imugi would certainly qualify as a mystical being.”

The Southern Heaven Demon Empress grasped everything in an instant and smoothly added,

“Then you must know that I won’t answer you.”

The fragments of memory still felt vivid. The traces of the Gate I had glimpsed through the dragon’s memories. The Water God Dragon becoming stained by the demonic qi that had flowed from it.

That was something that could not—and should not—have happened.

At least not here, in the Murim. It was an incomprehensible phenomenon that should never have appeared.

Yet the Southern Heaven Demon Empress and Dark Heaven had dragged the impossible into reality. It was enough to make me wish it were a lie.

“What the hell are you people after?”

“After?”

The next moment, a clear laugh flowed between the officer’s lips. It was filled with genuine amusement, not something she had forced.

After laughing aloud for a while, the Southern Heaven Demon Empress continued.

“Child. I am merely a lowly servant who acts according to orders. No one—not anyone—can presume to know that person’s will.”

That person.

Everyone present knew whom those two syllables referred to.

Jeok Cheongang muttered in a voice that seemed to boil like lava.

“Lord of Heaven.”

Crack.

With the sound of bones shifting, the officer’s head turned toward Jeok Cheongang like a creaking wooden puppet.

“I’ve heard that an old monster who went mad lives on Mount Jiuhua. Fire King Jeok Cheongang, you’re right. It is indeed that person. The greatest and noblest of all…”

“You’re talking about a fucking bastard who wouldn’t be worth the satisfaction of burning alive. How dare you wag that wicked tongue before this old man?”

A brief silence descended at Jeok Cheongang’s words, which carried cold flames.

Then the officer’s tightly closed lips slowly opened, and a low voice flowed out.

“You should choose your words more carefully if you want to hold on to your stubborn life a little longer.”

“My life?”

Jeok Cheongang snorted and asked me,

“You tell her. What happened to the people who came running to cut this old man’s lifeline?”

“They died. Every last one of them.”

“Then how about this old man adds a bitch instead of a bastard to his kill list? What do you think?”

There was no question about it. I gave him a vigorous thumbs-up.

“You’re a true feminist of this era.”

“Femibista? What’s that?”

“It means you’re a fair person. You beat the shit out of everyone equally, regardless of sex or age.”

“Is that some word young people use these days? Whatever the case, I like the meaning.”

Jeok Cheongang nodded with satisfaction, then glared at the Southern Heaven Demon Empress inhabiting the officer’s body.

“You heard that? This femibista intends to punish you and that Lord of Heaven fellow, or whatever his name is. So wash your neck and wait.”

*Uh. Should I stop him now before the Flame-Extinguishing Divine Fist turns into the Feminist Fist?*

Still, I felt much better. The confusion in my head had been neatly sorted out.

*Yeah, fuck it. We just need to beat the shit out of all of them.*

Wasn’t that the Fire Gate Clan’s motto, anyway? Smash, break, and burn anyone we decided was an enemy.

The Southern Heaven Demon Empress was never going to answer my questions. If that was the case, then all I had to do was keep moving forward and smash through whatever Dark Heaven did.

*I don’t have a choice anyway.*

Once you climbed onto the back of a tiger, there were only two paths left.

And rather than be thrown from its back, I would end this insane struggle even if I had to smash the tiger’s skull to do it.

No. I had to.

“Phew…”

I exhaled the breath I had been holding, then leaned close to the military officer. Looking through the soul-less eyes at some distant place, I spoke.

“When we meet again… you will die.”

The officer’s lips twitched.

“Yes. I, too, look forward to that day. And when it comes, no one here will survive.”

The head slowly turned. Its unfocused, milky eyes looked over everyone in the room one by one.

But no one avoided that chilling gaze. Mungyeong was no exception.

“You should stop this futile killing. Blades eventually turn back on the person wielding them.”

His tone and voice were polite, clearly conscious of the eyes around him. But hidden within them was a blade only a handful of people could detect.

That was the true nature of the greatest assassin in history—a supreme martial artist known as the Slaughter Saint, who had walked nothing but blood-soaked paths.

“…What an unusual child. Unusual enough to make me curious about this person called the Divine Physician.”

But the Southern Heaven Demon Empress, borrowing someone else’s body, did not seem to have grasped Mungyeong’s true identity.

She might have known his superficial identity as the Divine Physician’s Disciple, but the connection between the Slaughter Saint who had vanished forty years ago and a young medical apprentice was far too faint.

And before the Southern Heaven Demon Empress’s suspicions about Mungyeong could deepen, Jin Wikyung spoke in a heavy voice.

“I swear on the name of the Jin Family of Taiyuan that you will never lay so much as a fingertip on our youngest.”

“The Jin Family of Taiyuan. Can that paltry family and its feeble martial arts really protect that child?”

“Even a sewer rat will fight a tiger for the sake of its young. If you’re curious, come and see for yourself. I’ll have no choice but to show you.”

Even in the face of a bizarre phenomenon far beyond the bounds of common sense, Jin Wikyung did not lose his composure.

The moment he finished speaking, calm yet resolute, Gung Gibang scratched his matted hair.

“Great Hero Jin, it would hurt my feelings if you left our Sect out.”

“I forgot the Beggars’ Sect. Will you join us?”

“My Master used to say that a single dog-beating stick can only catch a neighborhood cur, but when a hundred of them gather, they can beat even a tiger to death. What do you think would happen if a hundred thousand Beggars’ Sect disciples gathered?”

The true strength of the Beggars’ Sect came from its overwhelming numbers.

Their forces were so vast that no one could object even if they were broadly called the hundred-thousand-strong Beggars’ Sect.

Gung Gibang, the Successor Beggar who stood one step short of reaching the summit of the Beggars’ Sect, flashed his yellow teeth in a grin.

“You were such a lovely young lady. It’s a shame to see you like this. But what can we do? Don’t resent me too much when I smash that pretty face of yours with my club.”

“Resent you?”

The corner of the officer’s mouth slowly rose.

Borrowing his mouth to form a grotesque smile that seemed to split the skin, the Southern Heaven Demon Empress addressed everyone.

“There’s no need to be so impatient. It won’t take much longer…”

Her voice faded like a campfire slowly dying out.

By then, dark red blood was already flowing from between the officer’s lips. Without hesitation, I seized his wrist and felt for his pulse.

Whoosh.

Internal energy surged from my dantian in an instant and flowed into his body, but the death that had already begun could not be reversed.

Things that had outlived their usefulness were discarded.

Perhaps that was the reason the Southern Heaven Demon Empress had kept the officer alive.

*A puppet whose body she could borrow for a while.*

Blood gushed from his mouth, then spilled in a stream.

It wasn’t only his mouth.

Dark red blood poured from his eyes, nose, ears—in other words, from the seven openings of the human body.

A death that could not be stopped by several jiazi of internal energy or even a Pressure-Point Strike loomed before the officer’s eyes.

“It’s too late.”

At that exact moment, Mungyeong’s voice rang in my ears.

Along with a flood of blood, one final sentence slipped from the officer’s slowly opening lips.

“Everything is according to that person’s will.”

Swish. Thud.

That was the end.

The officer’s head drooped as all his vitality was exhausted, and his breath stopped.

As silence descended with one man’s death, the presence approaching the estate stopped outside the door.

“Um… may I come in?”

The voice was familiar.

A young man cautiously poked his head through the slowly opening door and spoke.

“Benefactor, Great Hero Zhuge Pong is looking for you.”

“Not Zhuge Pong. Zhuge Feng.”

“Yes. Great Hero Zhuge Pong.”

“…I should just stop talking.”

I sighed and stood up.

I didn’t ask where Crouching Dragon Guest Zhuge Feng was now, where I needed to go, or why he was looking for me.

I was the one who had told them about *that place* in the first place.

“So, did you find it?”

“Yes.”

Cheongpung’s eyes lit up as he continued.

“It’s exactly the place you described, Benefactor.”

That place was the very location from the Water God Dragon’s memories.

Yeah. The damn Gate.

* * *

Honglan—or rather, the Southern Heaven Demon Empress—opened her closed eyes.

She lifted the silk curtain of the gently swaying four-horse carriage. Outside the lattice window was dense undergrowth, along with the Escort Bureau’s men sweating in the hot, humid weather of the southern regions.

“Hm.”

With her chin resting in her hand as she gazed out the window, the Southern Heaven Demon Empress looked like a painting all by herself.

Then, over the heads of the Escort Bureau men sneaking glances at her as if entranced, a thunderous shout rang out.

“Stop gawking and focus on the delivery! Unless you want to get yourselves killed by the Miao people we’ll meet in a few days!”

Despite the rough words, the speaker was a woman of dazzling beauty.

Beneath the bamboo hat pulled low to block the sunlight, her long, straight nose was sharp as a blade, and her lightly tanned skin was pleasing to the eye.

*A female escort? You don’t see that every day.*

It did not take long for the female escort, who had been loudly berating the rough men, to notice the Southern Heaven Demon Empress’s gaze.

She loosened the reins, drew alongside the carriage, and spoke toward the window.

“Is there a problem?”

“No problem. Thanks to your hard work, I’m traveling very comfortably.”

“Then why have you been looking at me like…?”

“Just because.”

“Pardon?”

The Southern Heaven Demon Empress smiled sweetly and added,

“Because you’re so young and pretty. That’s why I was looking.”

“Ah, thank you.”

The female escort, the Young Bureau Head of a small-to-medium Escort Bureau, was flustered but did her best to hide it.

The fact that the woman complimenting her was beautiful enough to make even other women fall for her was one thing. More importantly, she was a passenger who had paid a considerable sum, so the Young Bureau Head’s reaction was only natural.

But at the next words, she could no longer conceal her bewilderment.

“You’re making me want it. Enough to want to stick it onto my own face.”

“……!”

“I’m joking. Just joking.”

Her laughter rang out brightly. Facing the frozen female escort, the Southern Heaven Demon Empress continued in an amused voice.

“So, how much longer until we reach Yunnan?”

At that moment, the Southern Heaven Demon Empress was almost unable to contain her delight.

Delight at the screams and deaths that would soon be heard in another place.

And delight at having met a new face.
## Chapter artifact 484

# Chapter 484

It wasn’t difficult to find our destination. The boatmen had already made one round trip and learned the waterways, so they guided the vessel forward with practiced ease.

*Whoosh…*

It was hard to believe that a storm had raged only two days ago. The river was calm, and the breeze was refreshing.

Sitting at the bow and basking in the sunlight pouring down over my head, I spotted something familiar among the passing scenery.

*That’s right. It was around here.*

The *Memory Fragment* contained the memories left in the Water God Dragon’s mind, and I had seen and felt everything from its perspective.

Naturally, I knew the way to *that place* as well.

“Wait. Young Hero Cheongpung, are we sure this is the way?”

At my sudden question, Cheongpung tilted his head.

“It is. Why do you ask?”

“It just looks a little different from what I remember. Especially that cliff over there…”

“Oh, that? There were some circumstances.”

“What circumstances?”

“Yes. We followed the route you told us about, but the gap was so narrow that only a hand could fit through.”

“Oh.”

So that was why no one had set foot there for so many years. As the ages passed and sediment accumulated, the cliff had eventually blocked the passage.

The Water God Dragon had never needed to pass through the cliff. It could simply swim underneath it. Humans, however, were a different story.

“So?”

“We cut through it.”

“…You cut through it?”

“Yes. The Wudang grandpa and I sliced it up with our swords.”

*What the hell? He’s talking about cutting through a cliff like he’s trimming paper.*

But with Origami Man—no, Perfected Being Hyeongong, the Supreme Peak master Wudang was so proud of—and Cheongpung, it was entirely possible.

I could have managed it without much difficulty myself.

“Anyway, we carved straight through it. It wasn’t too hard. I heard the others who came with the second wave polished the rest.”

“…Uh. Right.”

Sometimes I forgot.

I forgot that monsters were everywhere around me.

And that I was one of them.

Jeok Cheongang, who had been listening to Cheongpung and me, poked Mungyeong in the ribs.

“Is the world going mad? I don’t remember things being like this when we were young. Or are those two simply monsters?”

“Don’t lump me in with you. It’s insulting.”

“So how old were you when you became a Supreme Peak master?”

“…”

“They’re the monsters.”

“Yes. That must be it. Hah. Perhaps the heavenly patterns have grown clouded. The Murim has changed. It certainly has.”

While Jeok Cheongang lamented, the vessel continued forward between cliffs that had been cut with such unnerving precision that they looked almost artificial.

Then a new landscape—and new people—gradually came into view.

*Whoosh! Splash!*

Masters who had reached the Peak realm landed on the river after stepping across the water with the movement technique known as Rising on Duckweed, Crossing Water. They blocked the vessel with imposing auras.

“Stop! Everyone aboard must state their names and sobriquets. Once the identity verification process is complete—”

Jeok Cheongang, already sensitive after living a water-friendly life for the past few days, stuck his head out with a fiendish expression.

“This old man is the Fire King.”

“Gasp!”

“If you stop us, you die.”

“Yes, sir!”

“O-open the way! Let no one stop them!”

*Whoosh!*

Gung Gibang watched the figures vanish at twice the speed with which they had first appeared and muttered,

“Was the Wudang Sect’s movement technique always this impressive? Our sect will have to stay on its toes.”

No. They had probably realized they were completely fucked and fled for their lives.

Either way, everything proceeded smoothly after that. The vicious Fire Pokémon Jeok Cheongang needed no explanation, and my face was famous enough that anyone who failed to recognize me might as well have been working for Dark Heaven. Besides, Cheongpung and Gung Gibang were with me.

“Oh, did someone just recognize me?”

“Of course. You’re the only beggar who travels with me.”

“…”

“Wow! Someone recognized me just now, too!”

“Of course. You’re the only human who travels around with a horned water snake.”

“Yes…”

I ignored the dejected Gung Gibang and Cheongpung and focused on the scene ahead.

Archers had somehow climbed to the tops of the impossibly high cliffs and stood ready to fire. I could also sense the presence of masters hiding in various locations.

*Wudang, the Zhuge Clan, and it looks like the Beggars’ Sect came too.*

The security was nothing short of formidable.

But considering the weight and importance of what had happened, it was only natural.

“Did the City Lord of Hubei Province decide to bury this matter completely?”

Jin Wikyung nodded gravely.

“For the time being. No ordinary citizen would take the news well that a five-hundred-year-old imugi had gone berserk.”

“That’s true.”

The people’s support was a double-edged sword.

Under ordinary circumstances, the simple folk who fawned over the Son of Heaven would pull a Hyuk Mujin-level about-face the moment a flood or earthquake struck, declaring it an omen of the nation’s ruin.

And if a plague came along as part of a buy-two-get-one-free deal, the people of this era would grab the pickaxes they had been using to till their fields and charge out to overturn the country.

How much worse would it be if an imugi, worshiped by countless people as a divine creature, suddenly went mad and killed several thousand people?

The City Lord of Hubei Province would want to hide that truth as much as possible.

“He does agree, at least in part, that Dark Heaven is an extremely dangerous organization.”

“…He agrees *in part*? Even after all this?”

I took back what I had said.

I could understand concealing the existence of the Water God Dragon. But how many people had died because of this incident? And he only agreed *in part*?

He clearly still hadn’t come to his senses.

“It is an illusion born of arrogance. He believes the Murim is merely the Murim, and that it will pose no problem for them to govern the country. I tried to persuade him as much as possible, but it was of little use.”

Jeok Cheongang suddenly cut in with a disgruntled voice.

“Those idiot government officials haven’t changed at all. They were exactly the same during the Great Faction War. When the Demonic Cult pushed down through Sichuan, they sat on their hands. Only after the civilian casualties grew did they hurriedly gather troops.”

“What happened then?”

“What do you think happened? By then, the Demonic Cult had already been defeated and withdrawn, and some bastard who called himself a Great General came strutting over and taking credit. He said it was all thanks to His Imperial Majesty’s grace and this and that. Since the Emperor was the master of the country anyway, it didn’t matter who won, but congratulations on your victory. That sort of bullshit.”

“You showed remarkable restraint. For you, Old Master, that was practically the patience of a Buddha.”

Jeok Cheongang looked at me as if I had just said something incomprehensible.

“Why would this old man have put up with that? I tried to beat him to death. If Hong Dao hadn’t stopped me, it wouldn’t have been the Great Faction War. It would have been the Great Government War, or something like that.”

“…Ah. Right.”

“In any case, don’t expect much from the government officials. We should be satisfied that they at least turned the dark-path figures who had been sitting quietly into Dark Heaven’s lackeys.”

Jin Wikyung answered with a bitter smile.

“Yes. Fortunately, since then, the people’s anger and wariness toward Dark Heaven have reached the heavens.”

“They had nothing to do with this incident, but what can we do? They aren’t completely innocent, either. They’re dark-path figures, so it wouldn’t be a bad idea to take this opportunity to uproot them.”

The government had worked with the Murim to crush Hubei Province’s dark-path figures as sacrifices to appease the people’s anger. Since both sides had gained what they wanted, it could be called a form of give-and-take.

Of course, there was no need to mention that my companions’ and my reputations had skyrocketed once again in the process.

*Whether the government would actually act even if Dark Heaven became more aggressive was another question.*

As I thought about that, the vessel that had been charging forward finally came to a stop.

We docked at a temporary pier built against the cliff, and people’s gazes poured toward us.

“That’s Great Hero Jeok Cheongang.”

“The Successor Beggar is beside him, too. I was wondering where the Huashan Divine Dragon had gone.”

“Wait. Isn’t that young man the Blazing Flame Divine Dragon?”

“Did you hear? There’s a rumor among the leaders that the Blazing Flame Divine Dragon was the one who took down the imugi…”

They thought they were whispering quietly, but I could hear every word.

*You idiots.*

I found the muttering irritating and deliberately scowled, causing the surroundings to fall silent in an instant.

Then, the next moment, a shout broke through the silence.

“Oh, you’ve arrived!”

The middle-aged man running toward us was drenched from head to toe in mud and river water. Unfamiliar aquatic plants were tangled in his disheveled hair.

As he came splashing through the river, I muttered inwardly,

*That man is the Family Head of the Zhuge Clan?*

It was something I had only just realized, but Crouching Dragon Guest Zhuge Feng was unquestionably regarded as an eccentric even within the Murim.

“Family Head, I normally wouldn’t say anything, but there are outsiders present. Please show some decorum…”

“Ah, please move aside, Uncle.”

“Family Heaaad!”

He had definitely left his decorum in a mailbox somewhere.

Shrugging off the family elder who tried to stop him, Zhuge Feng ran toward us and opened his mouth with a flushed face.

“We found it. We found it!”

“Yes, I know. Young Hero Cheongpung told me…”

“At first, I thought, *What kind of bullshit is this?* But it was really sitting right there in the place you described!”

“…”

Wasn’t that a little too honest?

I had explained everything so earnestly, and he had dismissed it as bullshit?

Seeing my expression, Zhuge Feng continued with a solemn face.

“Our ancestor, Zhuge Wuhou, once said that one should tap even a stone bridge before crossing it. Don’t take it too personally.”

Was constantly invoking the ancestors of the family a Zhuge Clan motto, or was it hereditary?

I stared at Zhuge Feng suspiciously.

“…Did Zhuge Wuhou really say that? As far as I know, that’s a proverb from another country.”

“He must have said it at least once in his life. Is that important right now?”

*Unbelievable.*

Whether it was the Chinese over there or the Chinese over here, they were both astonishingly talented at copying other people’s work.

But before I could say anything, Zhuge Feng abruptly turned around and started walking ahead of us.

“Follow me.”

Jeok Cheongang, who had been trembling with delight at finally being able to set foot on even a temporary pier, narrowed his eyes.

“‘Follow me’? Was that directed at this old man?”

“…I wasn’t speaking to Senior.”

“Then watch your mouth from now on, and straighten that folded tongue before this old man kills you in half.”

“Yes, sir.”

“And why are you walking so slowly? Even this old man’s grandmother would be faster than you.”

“Ah!”

Why did he suddenly start shouting battle cries?

Zhuge Feng became as brisk and alert as a model trainee and activated his movement technique, racing ahead. Not long afterward, I encountered a bizarre sight that I had never seen in the *Memory Fragment*.

“What is that…?”

“I invented that device when I was nine. It took quite a bit of effort to bring it here over the past two days. What do you think?”

I nodded as I stared at the enormous stone wall standing in the river like a barrier.

“Wow. That’s incredible.”

“It’s impossible to investigate underwater for long, so we used stone taken from the cliff to enclose all four sides and drained out all the water inside. If ordinary laborers had done it, it would have taken several months at least.”

The mechanical device Zhuge Feng had developed had played a major role, but without martial artists who had trained in martial arts, they would never even have considered building something like this in two days.

“Would everyone clear out for a moment?”

The moment we descended beneath the stone wall, Zhuge Feng uttered those words, and the people who appeared to be formation experts from the Zhuge Clan withdrew like the receding tide.

Only then could I see it.

A towering cliff that must have stood in the same place for countless years—and an enormous fissure running precisely across its center.

*Swish.*

The instant my hand stretched out instinctively and touched the gap—

> **System**
>
> *Beep.*

An utterly ominous System notification pierced my ears.

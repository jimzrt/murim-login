# Checkpoint Review — 730–734

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

# Chapters 730–734

## Plot

Odin Guild sends Huginn, a powerful messenger, to Ares Guild with a veiled threat: cancel the public release of the Mana Cultivation Method or face consequences. Jin Taekyung exposes the intimidation, while Choi Minwoo pretends to cancel the release and secretly has Jin publish the prepared file through his enormous social-media account. Huginn briefly releases S-rank-level pressure but withdraws after Choi warns him not to act rashly.

The release becomes an immediate worldwide event. Choi suspects Odin may have come partly to confirm Cheon Taemin’s absence and considers whether a Grand Mage-level assistant connected to Lee Jungryong leaked information about Taemin’s condition. The next morning, Jin learns that Wu Shaiming and more than fifty members of the Wu family, including children, were found dead in Beijing. Jin and Choi suspect Odin ordered the extermination to prevent the Wu family's Mana Cultivation Method from spreading or to retaliate for their defiance. Jin plans to confront Odin's master in Paris, but Choi persuades him that attacking without a defensible pretext would only bring an Interpol wanted notice.

Odin’s earlier demands on China are reviewed: a ninety-nine-year lease for ten Sichuan cities and authorization to establish a Beijing branch. China rejected them, while Odin secured French political protection. Before Jin and Choi can act, the Skeleton King reports that Odin has publicly declared support for Ares and unveiled its own Mana Cultivation Method, claiming it was prepared over several years. The sudden reversal leaves Jin stunned and the real purpose of Odin’s maneuver unresolved.

Separately, investigators discover that Go Jun’s necklace vanished from locked, magically protected evidence storage without triggering any alarms or anti-theft systems.

## Continuity

- Jin Taekyung has released the prepared Mana Cultivation Method through his personal social-media account, whose follower count exceeds five hundred million.
- Odin Guild opposed the release, sent Huginn to threaten Ares, and demonstrated that it possesses at least one operative with S-rank-level power.
- Choi Minwoo is willing to bluff Odin and treats Jin as a decisive Joker card.
- Only Jin, Choi, Song Song, Im Kkeokjeong, the Skeleton King, and Magic Johnson know that Cheon Taemin is in a vegetative state; the other known holders of the secret are dead.
- A Grand Mage-level assistant connected to Lee Jungryong constructed Ares Guild’s Area A and may have enabled information to leak.
- Wu Shaiming, Wu Heixing’s family, and more than fifty Wu relatives were killed simultaneously by apparent sudden cardiac arrest while imprisoned in Beijing.
- Xiao Yang had been trying to obtain the Wu family’s Mana Cultivation Method, which enabled Wu Heixing to become an S-rank Hunter.
- Jin and Choi will not immediately confront Odin because they need legal justification and public support.
- Odin demanded a ninety-nine-year lease of ten Sichuan cities, including Chengdu, Meishan, Ziyang, and Suining, plus an official Beijing branch; China rejected the proposal.
- Odin contacted the French government and benefits from the political protection of its Paris base.
- Odin now publicly supports Ares and claims its newly revealed Mana Cultivation Method was prepared for years.
- Go Jun’s necklace remains missing from secured evidence storage; the thief bypassed both the room’s locks and its protective Magic.
- Open questions: Odin’s reason for reversing its position, whether its support is genuine, how it obtained or developed its method, whether it ordered the Wu family’s extermination, the identity of Odin’s master, and the identity and purpose of the necklace thief.

## Translation Decisions

- Render **후긴** as **Huginn** and **무닌** as **Muninn**.
- Render **오딘 길드** as **Odin Guild** and **크로노스 길드** as **Chronos Guild**.
- Render **마나 연공법** as **Mana Cultivation Method**.
- Render **최 팀장** as **Team Leader Choi** and **샤오 양 주석** as **Chairman Xiao Yang**.
- Render **멸문지화** as **the annihilation of an entire household**.
- Render **아크 리치** as **Arch-Lich** and **벙어리 삼룡이** as **Samryong the Mute**, retaining the cultural allusion with a brief explanatory footnote.
- Preserve Jin Taekyung’s hungry, dry, profane mockery; Choi’s measured formal speech; Huginn’s polished coercion; and the Skeleton King’s archaic grandeur.
- Preserve uncertainty around Odin’s master, the Wu family’s deaths, the sudden policy reversal, and the stolen necklace.

## Durable state

{
  "active_continuity": [
    "Jin Taekyung, Team Leader Choi, and the Skeleton King remain together at Cheon Taemin's heavily protected mansion.",
    "Jin and Team Leader Choi have decided not to immediately confront Odin Guild because they lack a defensible pretext and would risk an Interpol wanted notice.",
    "China rejected Odin Guild's demand for a ninety-nine-year lease of ten Sichuan cities and authorization for an official Beijing branch.",
    "Odin Guild had contacted the French government before withdrawing from negotiations over support during the Sichuan Province monster wave.",
    "Public sentiment supporting Jin, Ares, and the Mana Cultivation Method is a major strategic weapon and shield.",
    "Odin Guild has publicly declared support for Ares and revealed a new Mana Cultivation Method, claiming it was prepared over several years.",
    "Team Leader Choi is Cheon Taemin's maternal grandson and a controlled, trusted ally who is candid with Jin.",
    "Chairman Xiao Yang provided Team Leader Choi with the unofficial Chinese proposal sent to Odin Guild."
  ],
  "continuity_sources": [
    734
  ],
  "open_questions": [
    "Why has Odin Guild suddenly declared support for Ares and revealed a supposedly long-prepared Mana Cultivation Method?",
    "Is Odin Guild's public support genuine, or is it a political maneuver connected to the Wu family's extermination and the previous night's events?",
    "Who is Odin Guild's master?",
    "How did Odin Guild obtain or prepare its Mana Cultivation Method?"
  ],
  "safe_through": 734,
  "temporary_decisions": [
    "Render 최 팀장 as Team Leader Choi.",
    "Render 샤오 양 주석 as Chairman Xiao Yang.",
    "Render 메이산 as Meishan, 쯔양 as Ziyang, and 쑤이닝 as Suining."
  ],
  "version": 1
}

## Reading copies

## Chapter artifact 730

# Chapter 730

Knock. Knock.

The sudden sound of someone knocking drew everyone’s eyes toward the door.

Even the janitor at Ares Guild knew that the entire leadership was gathered in the conference room to discuss something important.

So if someone knocked on the door under circumstances like these, there were only two possibilities.

Either the matter was that important—or they had already written their resignation letter.

And unlike Seok Go Jun, who would have started by spitting out every curse in the book, their new City Lord didn’t so much as twitch an eyebrow despite having his favorable momentum interrupted.

“Come in.”

Click.

A middle-aged man appeared through the half-open door.

He held the title of Chief Secretary, and he immediately approached Choi Minwoo and bowed.

“I’m sorry to interrupt the meeting, Vice Guild Master.”

Choi Minwoo answered calmly.

“It’s fine. Assuming you have a good reason.”

The Chief Secretary swallowed hard.

Although he had only been employed for a short time, he knew very well that the employer before him was clear about rewarding and punishing people.

On top of that, the report that had just come up from the lobby’s Security Team one minute earlier was not something he could handle on his own.

“An important guest has arrived.”

The Chief Secretary extended a trembling hand.

Choi Minwoo’s eyes sank as he looked at the object being offered to him.

*This is…*

Several thoughts flashed through his mind the instant he realized what it was.

But his hesitation was brief. Choi Minwoo made up his mind.

“Where is the guest?”

“Still in the lobby…”

“Take them to my private office. I’ll be there shortly.”

“Yes, sir.”

The Chief Secretary answered as though he had been waiting for those words and left the conference room. Choi Minwoo turned toward the executives seated around the table.

“It seems we’ve more or less finished discussing the urgent matters. What do you all think?”

“Pardon?”

“Vice Guild Master, are you saying…?”

“If you would all understand, I think we should end today’s meeting here.”

Several executives stared at Choi Minwoo with stunned expressions.

This was too much, no matter how they looked at it.

Even if an important guest had arrived, how could he end a meeting attended by every overseas Branch Leader like this?

Scrape.

“Vice Guild Master!”

The moment one executive gathered his courage and shot to his feet—

Bam!

A sudden thunderclap swallowed his voice.

Jin Taekyung had left the imprint of his palm in the alloy table. He muttered:

“Did they lay eggs or something? What kind of damn bugs keep flying around? Should we tear up the conference room again?”

“……!”

“Oh, sorry. Please continue what you were saying. Vice Guild Master, what was it after that?”

At Jin Taekyung’s question, the executive who was still standing looked at Choi Minwoo with a stiff expression.

“Since things have turned out this way, I’d like to say something.”

His voice carried the determination not to back down this time. Several executives’ eyes gleamed, and Choi Minwoo calmly nodded.

“Yes, go ahead.”

“Then may I leave work early?”

“…….”

“Today is my wedding anniversary, actually…”

The other executives looked at their colleague with eyes that had gone ice-cold.

He had been divorced for three years already.

* * *

The Team Leader Choi I knew was a very reasonable person.

Even if he had the power to crush someone, he knew when to back off, and he usually wrapped things up in an atmosphere that was as calm and gentle as possible.

In other words, he wasn’t the sort of person who would send dozens of executives home with a few words over just any matter.

Which only made me more curious about the identity of the guest who had arrived so suddenly.

Ding.

“You ended the meeting because of that person, right? The important guest?”

The moment the private elevator doors closed, I spoke up. Team Leader Choi answered:

“Half and half. I called the executives together to reassure them. There was never any room for trouble to begin with.”

“True. Most of the executives who remain are friendly, after all.”

“Even if someone had complaints, there was no reason for the Guild to oppose making this public.”

“Because it also suggests that Cheon Tae… no, that your maternal grandfather is still going strong, Team Leader Choi. Right?”

“Yes. The reason Ares Guild hasn’t enjoyed its former standing is my maternal grandfather’s absence. In that sense, Mr. Jin’s proposal to use his fame was the best option for all of us.”

There was no denying that the existence of a man named Cheon Taemin was practically a cheat code in this world.

With only his name, he could draw the attention of the entire world and make the hyenas lurking somewhere, waiting for an opening, take a step backward.

Just like…

*That’s right, like the Martial God.*

The thought that had suddenly crossed my mind lingered at the tip of my tongue before scattering.

Team Leader Choi continued in a low voice.

“But unlike the executives of Ares Guild, this must have been unwelcome news to someone else.”

“Someone else being…”

Team Leader Choi held out his hand and gave me something.

“The owner of this business card.”

Ding.

The elevator doors opened. We continued our conversation as we crossed the empty corridor that had been cleared according to his instructions.

“A business card? This is?”

I frowned as I looked at the object I had just received.

Its size and shape were exactly those of a business card, but I wondered whether it could really be called one.

The shining platinum-colored card did not have a name, a title, or even a phone number written on it.

The only thing I could guess was that its owner was an unimaginably wealthy magnate.

“This is heavier than I expected. It’s not just the appearance—it’s actually platinum. Is the other person Middle Eastern royalty?”

“If that were the case, I would have finished the meeting and come.”

“Then what?”

“Take a close look at the edge of the card.”

Following Team Leader Choi’s words, I examined the card again.

Only then did I notice that two birds had been engraved on the front and back.

“This is…”

“Do you recognize what kind of birds they are?”

“Not really.”

“They’re ravens.”

“Ravens?”

“Their exact names are Huginn and Muninn.”

“What, ravens have names? A raven is a raven.”

“Someone without an interest in the subject might not know. They’re creatures from mythology.”

“Mythology?”

“Yes. Ancient Norse mythology.”

Step. Step.

The footsteps rang unusually loudly as they drew closer. Looking toward the office door that was slowly approaching, Team Leader Choi continued.

“Huginn and Muninn are two ravens from that very Norse mythology. They symbolize one of its gods.”

“Who?”

“Odin.”

“……!”

“It’s a name you’ve heard many times, isn’t it?”

I remained silent for a moment before nodding.

I had heard the names Huginn and Muninn for the first time today, but Odin was different.

*Yes, very different.*

Not merely because he was a famous god whose name everyone had heard at least once, or because he had appeared as a character in the superhero movies I had enjoyed as a child.

The two syllables of Odin were known by everyone, regardless of where they lived in the world.

Because that Odin was…

the world’s greatest Guild, recognized by everyone.

Step.

The final footstep arrived.

Beyond the door blocking our way, I could feel a massive energy neatly contained.

Team Leader Choi’s calm voice slid across the quiet corridor.

“Let’s go.”

Click.

At last, the door opened.

A person standing before the fireplace slowly turned around.

* * *

At first, everyone thought it was a minor incident.

Work had been busy, everyone had been preoccupied with various problems that needed immediate attention, and *the incident* had happened and ended in the blink of an eye.

But it was no minor incident at all.

The first person to realize that was the youngest employee working in the evidence storage room.

“Um, Manager. I think some of the evidence is missing.”

“What? What are you talking about?”

“I just checked the inventory, and it looks like one item is missing…”

“You idiot, check again instead of wasting time talking nonsense. Nothing’s been taken out of the storage room in over a week.”

The manager frowned and continued scrolling through his stock screen with his legs crossed.

That was what he was doing until thirty minutes later, when he heard the words of the youngest employee, who had disappeared while scratching the back of his head.

“Manager, I really think something’s missing. One item from the Go Jun-related evidence is gone.”

“Hey, I told you before. The storage room has been locked for a week. I’m already pissed because my stock hit limit down, so stop talking no—”

The manager stopped speaking mid-sentence.

“What did you just say?”

The youngest employee answered with a cowed expression.

“I told you. It really is gone.”

“No, not that. What did you say right before that?”

“Huh? Oh, the Go Jun-related evidence?”

“……!”

At the three syllables that once again slipped from the youngest employee’s mouth, the manager felt a chill run down his spine.

Go Jun.

Not just anything, but evidence related to the Go Jun incident had disappeared.

“Hey, the door. The door! Open the storage room right now! Get the others too—no, wait. Don’t call them yet!”

The manager leaped to his feet and ran toward the evidence storage room.

Then, after spending several hours tearing the place apart with the youngest employee, he finally realized the truth.

*For fuck’s sake…*

It was gone.

It had really disappeared.

The report from that clueless youngest employee had not been nonsense, and the stock he had bought two days ago hitting the limit-down price no longer mattered at all.

If this became known, his entire life would hit the limit-down price.

*What the hell is this?*

Half out of his mind, the manager stared blankly around the evidence storage room. It was completely incomprehensible.

The last time the inventory had been checked was only last week.

Yet an item had vanished without a trace from a storage room no one had entered during the past week.

Even the anti-theft Magic installed on each piece of evidence and the alarm Magic covering the entire storage room had not activated.

*And it had to be evidence related to Go Jun.*

The mere disappearance of evidence was already enough to require him to write an incident report, but if evidence related to Go Jun had disappeared, this would not end with ordinary disciplinary action.

Even if the higher-ups had already collected the important items, it had been an enormous case.

“Seriously, I’m screwed.”

The manager felt the future go dark before his eyes. A civil servant’s lifeline might be long, but it wasn’t a steel cable. It could still be cut.

When he thought of his tiger-like wife and rabbit-like children waiting at home, he couldn’t bring himself to report what had happened.

*That’s right. Bury it. For now, bury it and see how things develop.*

If he could just sweet-talk the clueless junior employee, he might still be able to figure something out later.

Having made up his mind, the manager called out to the youngest employee somewhere in the vast storage room in the kindest voice he could muster.

“Are you there?”

“Ah, yes. I just got here.”

“You went somewhere. Come over here for a moment. I have something important to discuss with you…”

Then the manager turned around—and saw them.

The youngest employee, his eyes shining brightly, and behind him, the Security Team Leader standing like an iron tower.

“What is it? I heard there was a problem.”

“……?”

“Manager Kim?”

*Shit. I’m fucked.*

The manager barely swallowed the curse and spoke in a desperate tone.

“It’s gone.”

“Pardon?”

“The necklace that came in with Go Jun’s personal effects. It’s gone.”
## Chapter artifact 731

# Chapter 731

Step.

A pair of glossy dress shoes pressed into the carpet.

The next moment, when I finally faced the person who had turned around, a thought suddenly crossed my mind.

*He looks like a crow.*

Black from head to toe, he looked like a European gentleman who had wandered in from somewhere around the nineteenth century.

A suit without a single wrinkle, a high-collared coat, and—on top of that—a silk hat that had been out of fashion for roughly a hundred years.

He was unmistakably Black, but the eyes visible behind his transparent monocle glowed a mysterious golden color.

After staring at us for a moment, he lightly touched the brim of his hat and greeted us.

“Pleased to meet you both.”

Smooth Korean flowed from his mouth through translation Magic.

He was an uninvited guest who had shown up without an appointment, but if he was a messenger sent by Odin Guild, we couldn’t openly treat him coldly.

Besides, anyone carrying this much mana…

*He isn’t an ordinary messenger.*

I gave the unfamiliar guest a small nod, and Team Leader Choi gestured toward a seat.

“Please, sit down first.”

The three of us, myself included, sat across from each other with a solid wood table between us.

A strange atmosphere lingered for a moment before the other man broke the silence.

“My apologies for introducing myself so late. I am Huginn of Odin Guild.”

“That crow?”

At my inadvertent mutter, the man gave a faint smile.

“Ah. Of course, I have another real name. However, I have been called Huginn ever since I began serving the Guild Master, so I believe you may call me that as well.”

Hunters whose names had become known to a certain extent were usually called more often by epithets based on their abilities than by their actual names.

But no matter how hard I searched my memory, the man before me, Huginn, was a complete stranger.

*Is he some kind of hidden right-hand man of Odin’s Guild Master?*

Even the major Guilds in Korea were hiding plenty of secrets. As a field agent responsible for the front lines, it was difficult for me to know the details of foreign affairs as well.

*Especially since he’s from Odin Guild.*

There had certainly been a time when Ares Guild was known as the greatest Guild in the world.

But a little over twenty years ago, Cheon Taemin disappeared from the public eye without a trace.

People questioned what had happened, and no matter what kind of skill Lee Jungryong brought to bear as Ares Guild’s new captain, he couldn’t fill the void left by Cheon Taemin.

One year. Five years. Then ten.

Even now, countless people who passionately followed Cheon Taemin still called Ares Guild the best.

But the people who knew reality—especially the Hunters—thought differently.

*To put it coldly, Ares Guild had been a setting sun. For the past ten years already.*

Odin Guild, on the other hand, was a newly rising sun.

Based in Europe, they had rapidly expanded their influence while Ares Guild was faltering. Along the way, they acquired and merged with several major Guilds, rising into a giant that no one could deny.

A giant powerful enough to send a mere messenger to Ares Guild’s new master.

“The reason I came to visit so suddenly today is to deliver the Guild Master’s congratulations.”

At Huginn’s words, Team Leader Choi calmly opened his mouth.

“Is that so?”

“Yes. He is very pleased that an outstanding young man with the qualifications and ability to do so has taken charge of Ares Guild.”

At a glance, it sounded like praise, but the meaning behind it was different.

I licked my lips and muttered inwardly.

*Look at these bastards…*

Some things couldn’t conceal their true contents no matter how thickly they were wrapped. The same was true of Huginn’s polite voice and demeanor.

*They’re looking down on us from the very beginning.*

It felt as though we were receiving an envoy from our suzerain.

And the Team Leader Choi I knew wasn’t stupid enough to miss something like that, nor was he impulsive enough to openly show his displeasure.

“That is excessive praise while my maternal grandfather is still around, but I am endlessly grateful for the sentiment. I almost wish I could meet him in person and thank him.”

But Huginn didn’t lose his smile despite the barb in Team Leader Choi’s words.

“Ah, he was also very sorry that he could not come in person.”

“The Guild Master must be very busy. As far as I know, he has not engaged in any outside activities for several years now… It seems rumors really are not worth believing.”

The higher someone rose, the harder it became to pry them out of their seat. That was an eternal truth.

Cheon Taemin was merely an extreme case, since he was known to have vanished completely.

Most Guild Masters of major Guilds avoided contact with the outside world, and Odin’s Guild Master was no different.

“Even so, he is someone I have always respected, so I would like to visit him and pay my respects. What do you think?”

“Haha. Well…”

Huginn laughed out loud, interlaced his fingers, and continued.

“I’m sorry to say this, but he has become so busy lately that it will probably be difficult.”

“It sounds as though something has happened.”

“Yes. It is a minor matter, but also a rather troublesome one, so he seems to be spending a great deal of time wondering how to handle it. The others are in the same situation.”

“The others?”

“Acquaintances he has known for many years. The person he is scheduled to meet today is from Chronos… Ah, my apologies. I seem to have said something unnecessary.”

The name of another major Guild, one of the world’s Ten Great Guilds alongside Ares, slipped out.

Team Leader Choi quietly muttered.

“Chronos Guild.”

“I would appreciate it if you could pretend you didn’t hear that. I make mistakes like this from time to time and end up being called in and reprimanded by the Guild Master.”

At Huginn’s troubled expression, I couldn’t hold back a quiet laugh.

“What mistake?”

“Pardon?”

“Hey, Mr. Crow. Stop the half-assed theatrics and let’s have an honest conversation from here on.”

*Hmm. Maybe I should have just kept watching.*

That thought crossed my mind, but listening to him was beginning to feel like I had wolfed down a hundred sweet potatoes without a drop of dongchimi broth to wash them down.[^1] I couldn’t take it anymore.

I leaned back against the plush sofa and opened my mouth.

“To put it bluntly, you came because of the Mana Cultivation Method that’s about to be released, right? Stop at a reasonable point. If you go any further, this won’t be fun. We can join hands with another major Guild like Chronos and bury you, so don’t get cocky. That’s what you wanted to say, isn’t it?”

“……”

“No, for fuck’s sake. We all know what’s going on, so why are we dancing around the subject and giving ourselves headaches? We aren’t recording this conversation. Just say what you came to say and leave. Isn’t that right?”

Huginn silently listened to the words pouring out of me like a waterfall before suddenly turning toward Team Leader Choi.

“I did not mention this because I thought it might be discourteous, but is there truly a reason Mr. Jin needs to be present here?”

“Of course.”

Team Leader Choi answered calmly.

“Mr. Jin is that important. And if you wanted a private meeting, you should have said so from the beginning.”

“Then may I ask for a private meeting from this point onward?”

“I refuse.”

At Team Leader Choi’s answer, given without a moment’s hesitation, Huginn blinked his golden eyes.

“This is quite… awkward.”

“We feel the same. If you had made an appointment beforehand, we could have coordinated several matters.”

“Hm.”

Huginn adjusted his monocle before opening his mouth.

“Then, since I was the first to behave rudely, I will formally apologize to you both.”

*Look at this guy.*

At first, I had wondered whether the whole crow thing was some kind of gimmick, but there was a reason he had gone to the trouble of dressing like a gentleman.

Huginn’s manner was fairly courteous, so I answered him like a gentleman as well.

“Since you were the one who made the mistake first, I won’t apologize.”

“……”

“I already understand how you feel, so don’t stare at me like that. As I said earlier, let’s just have an honest conversation. Okay?”

Huginn sighed and nodded.

“All right. Since you are being this direct, I have no choice but to speak directly as well.”

“Keep it short. Get to the point.”

Beneath the lighting Magic installed in the office, Huginn’s monocle flashed brightly.

The brief silence ended almost at once. After staring silently at Team Leader Choi and me, he opened his mouth.

“Stop the release of the Mana Cultivation Method. If you refuse this proposal, there will be repercussions.”

It was a single sentence that fulfilled my request to get straight to the point one hundred percent—and made us feel even worse than I had expected.

“Well, I already had a feeling, but… hearing it said out loud like this still feels like shit. Doesn’t it?”

Team Leader Choi shrugged at my question.

“Still, isn’t this much better than him talking in circles like he did a moment ago?”

“That’s true. If he’d kept talking like that this time, I really would have…”

“You must control yourself.”

“I was going to hold back even without you telling me. I don’t want to make this into a bigger problem. But I think I would have told him to take off the monocle first.”

Team Leader Choi gave a quiet laugh at my answer, and Huginn’s eyes narrowed.

“You are very rude. Just as I had heard.”

“You’re being pretty damn unpleasant too. I’d never heard of you, much less seen you.”

“Are you planning to put on a show of force right here?”

“If necessary. If you take off that monocle.”

“……”

“Listen, Mr. Jin.”

“Yes, hello? Go ahead.”

“Do not lose your temper. This is merely a proposal.”

“Your mouth may be crooked, but you should still speak straight. To my ears, that sounds like a threat, not a proposal.”

“If you heard it as a threat, then perhaps it may really become one. But what matters to me is not what you think.”

Huginn answered firmly, then turned toward Team Leader Choi.

“What will you do, Mr. Choi?”

His golden eyes gleamed coldly. A voice filled with force slipped between Huginn’s lips.

“Choose. You personally.”

* * *

Huginn was certain.

*This is a proposal he cannot refuse.*

An ultimatum in all but name.

Anyone with even a little sense would have no choice but to take a step back.

Jin Taekyung was an unpredictable man—more than unpredictable, half-mad—so he was an exception. But the young Asian man before him, Choi Minwoo, would make a different choice.

Besides…

*The Slayer will not intervene. Since Master said so, it is a fact.*

Those were the words of none other than his Master.

Huginn offered absolute loyalty to his superior.

His words had never missed the mark, so Choi Minwoo’s answer was as good as decided already.

Perhaps that was why.

When Choi Minwoo’s answer came a moment later, it felt entirely natural to Huginn.

“Since things have come to this, I suppose there is no choice. All right.”

“As expected. Mr. Choi is wise.”

His composure, shaken by dealing with Jin Taekyung, seemed to settle back into place.

Only then did Huginn recover the smile he had briefly lost and continue.

“Then may I understand that tomorrow evening’s scheduled release of the Mana Cultivation Method has been completely canceled?”

“Of course. I changed my mind.”

“Excellent. He will be pleased to hear this.”

Huginn rose from his seat and added one more thing.

“So will the others.”

Choi Minwoo answered calmly.

“I hope they will.”

“They are reasonable people. From now on, we should be able to establish a good relationship in a more amicable atmosphere.”

With those pointed words, Huginn looked toward Jin Taekyung.

Only moments ago, Jin had been spouting vulgarities right to his face. Now, he was sprawled against the sofa as though lying down, fiddling with his smartphone.

*He is rude to the very end.*

But Huginn felt more exhilarated than offended. He was the winner of today’s encounter, after all.

Before leaving, Huginn adjusted his silk hat like a cultured gentleman and extended his hand toward Jin Taekyung.

“Mr. Jin, I behaved discourteously today despite my intentions. I hope we can meet with smiles next time.”

The right to mock a loser with kind words was a privilege only a winner could enjoy.

And when Jin Taekyung didn’t even take the hand he offered and instead answered curtly, Huginn felt even better.

“You’re in a hurry. I haven’t even finished uploading yet.”

“I have something urgent to attend to. Then I will be going.”

His business here was finished.

After politely bowing toward Choi Minwoo, Huginn turned without hesitation and walked toward the door.

Step. Step.

His light footsteps crossed the carpet. But Huginn was forced to stop in front of the door.

It was because of the one sentence he had just heard—a sentence he could not possibly dismiss.

“Did you just say…”

He turned around, the end of his words trailing off. Huginn stared at Jin Taekyung with an expression that said *surely not*.

Jin blinked.

“Hm? Oh, uploading?”

“Uploading…?”

“Yes. It’s nothing important, so you can go now. You look busy.”

Uploading. Uploading. Uploading.

The word echoed in his ears, pounding in time with his heartbeat.

“What. Exactly. Did you. Upload?”

And the answer to his clipped question came not from Jin Taekyung, but from Choi Minwoo.

“Didn’t I tell you? I changed my mind.”

“No way.”

“The Mana Cultivation Method. We’ve decided to release it today.”

“……!”

[^1]: Dongchimi is a watery radish kimchi whose chilled broth is often used to refresh the palate.
## Chapter artifact 732

# Chapter 732

Civilization sure is convenient.

You can store an enormous amount of data on a smartphone smaller than your palm, and share whatever information you want with everyone else using nothing but a few movements of your fingers.

Of course, this advanced civilization had restricted my actions up until now, but at least this time, the opposite was true.

“Mr. Jin Taekyung. Do you happen to have the file with you right now?”

Only a few minutes earlier, Team Leader Choi had sent those words into my ear through Sound Transmission. Remembering them, I let out a quiet laugh.

I waved the smartphone in my hand at Huginn, who was frozen like a stone statue.

“Can you see this?”

The light from the smartphone flickered in Huginn’s golden eyes.

At Team Leader Choi’s request, I had uploaded the file to a personal social media account I’d created months ago and never used. The words **Post published** were displayed on the screen.

“Is it because this is the Vice Guild Master’s office? Even the Wi-Fi speed is on another level. It may not look like much, but the file size is pretty hefty.”

“……Mr. Jin.”

His voice sounded as though it were boiling. I blinked my deer-like eyes innocently and asked:

“Hm? Why?”

“What, exactly, do you think you are doing?”

“Being a good boy.”

Huginn’s skin instantly flushed a dark red. After taking a deep breath, he spoke in a calm voice.

“Delete it now. It is not too late.”

I muttered with a deliberately serious expression.

“Should I? To be honest, I’m a little nervous too.”

“An incorrect choice can still be corrected.”

“Easier said than done. Do you have any idea how scary the world is these days? It’s probably already spreading everywhere.”

Buzz. Buzz. Bzzzz.

Before I had even finished speaking, my smartphone began vibrating nonstop.

When Huginn realized that the vibrations were sharing notifications, a look of anxiety settled over his face.

“It has only been a few dozen seconds. At this point, we can still contain it.”

“Oh? Really?”

“I give you my word.”

“But people are going to curse me out. They’ll say I baited everyone and then deleted the post and ran. I already scattered so much bait everywhere that this won’t end with just a moderate amount of abuse.”

“We could announce for now that the Mana Cultivation Method requires further improvements… No, rather than wasting time, would it not be better to delete it as quickly as possible?”

At Huginn’s urging, I let out a quiet sigh.

“I want to do that too, but there’s one thing that keeps bothering me.”

“Tell me at once. I will resolve it for you.”

“What should I have for dinner tonight?”

“……?”

“The dinner menu. What should I eat so people will say I really enjoyed the meal? What do you think, Team Leader Choi?”

“Let’s have kimchi stew.”

“Kimchi stew?”

“Yes. Kimchi stew boiled with plenty of pork. And white rice.”

“Damn, you know your food.”

The moment I exclaimed in admiration—

Crack.

The sound of bones shifting rang out from someone’s tightly clenched fist. After trembling for several seconds, Huginn spoke in a voice that had sunk deep.

“So you have chosen… to make a foolish decision after all.”

I shrugged.

“Why? You don’t like Korean food?”

“I promise you. You will regret this.”

“If you insist that much, I can’t help it. Then instead of kimchi stew, we’ll have soybean paste stew tonight. What do you think, Team Leader Choi?”

Team Leader Choi nodded.

“Anything is fine with me. I happen to be hungry, too.”

“That’s because you’ve been listening to bullshit since early evening. Barking is cute once or twice, but it gets tiring when you have to keep listening to it.”

I looked at Huginn and added:

“Especially when it isn’t my dog, but a mutt raised in the neighborhood next door.”

“……!”

“I don’t know who the owner is, but the world’s really gone to hell. Who lets a dog loose these days without a leash or muzzle?”

I muttered as if speaking to myself, then glanced down at my smartphone.

Five in the afternoon.

That was late enough that it wouldn’t be strange to have dinner soon, but for some reason, I felt strangely unhungry today.

And the reason was probably…

Buzz. Buzz. Bzzzz.

The sharing notifications that continued ringing without pause even now.

“Team Leader Choi. How many followers did my account have again? I only created the account and barely ever checked it, so I don’t really know.”

Team Leader Choi answered calmly.

“As far as I know, more than five hundred million.”

“Five hundred million? There are that many?”

“It is a globally famous social media platform, regardless of race or country. Of course, nearly half of them are Chinese.”

“Good grief. I should thank the Arch-Lich.”

Huginn, who had been listening to our conversation, spoke in a cold voice.

“I recall once hearing that Korea has a proverb: ‘After losing the cow, repair the pasture.’”

“You didn’t hear that from a Korean, did you? It’s not a pasture. It’s a barn.”[^1]

“Whether it is a pasture or a stable, what difference does it make? The important thing is that the two of you have made the worst possible choice today.”

“Who knows? We’ll have to wait and see.”

“I guarantee that you will lose everything before long. And when that happens, there will be nothing left to repair.”

At Huginn’s vicious words, I snorted quietly.

“The more I look at him, the harder it is to tell whether he’s a crow or a mutt.”

“……Mr. Jin.”

“For a servant sent here to deliver a message, you sure talk a lot. If you want to say more, bring your master here. And tell him not to put on airs as if he really is a god.”

The moment I finished speaking—

Whoosh!

A gust of wind blew in from somewhere.

The enormous mana pouring from Huginn’s entire body writhed.

It was an aura powerful enough to be called that of an S-rank Hunter without the slightest exaggeration—just as I had expected, and even more powerful than I had expected.

But the power that seemed ready to overflow in every direction stopped dead at Team Leader Choi’s quiet words.

“I cannot take responsibility for what is about to happen.”

“……”

“If you are prepared for that, do as you wish, Mr. Huginn.”

A brief silence passed.

Fwoosh.

The surging mana gradually subsided.

His golden eyes lost their icy chill, and the hand that had twitched as if to retrieve something from inside his clothes settled back where it had been.

Pat. Pat.

After briefly straightening his disheveled clothes, Huginn spoke with a rigid expression.

“I have been discourteous. I apologize.”

I smacked my lips at his straightforward acknowledgment.

It was unfortunate that I hadn’t been able to smash that neat monocle of his, but there was nothing to be done. For now, the friction we had created here today was more than enough.

*There’s no need to provoke him any further.*

Odin Guild was an undeniable giant.

And just as massive as its body was the shadow it cast.

Huginn alone, standing right in front of us, was someone whose existence was unknown to the outside world.

It was difficult to guess how many hidden S-rank Hunters Odin Guild possessed.

*And the other major Guilds will probably side with Odin, too.*

In a situation like this, half-crushing Huginn’s face would bring us more losses than gains.

Team Leader Choi understood that perfectly. So did Huginn, despite briefly losing his composure.

“I should be going now. I am sure we will meet again before long.”

After pretending to be a gentleman to the very end, Huginn left the room with those pointed words. Team Leader Choi didn’t forget to give him one final reply.

Or, to be more precise, a bluff.

“I will remember Odin Guild’s intentions clearly. So will Mr. Jin Taekyung. And so will my maternal grandfather.”

“……I understand.”

Whether it was surprise or confusion, some unknowable emotion surfaced in Huginn’s eyes as he answered. Then he disappeared.

Click.

Team Leader Choi stared silently at the firmly closed door and muttered:

“So it begins.”

“Well, we knew there would be opposition. Now that the release has already been announced for tomorrow, they had no reason to hesitate either.”

“It was more blatant than I expected. And besides…”

His voice trailed off. Team Leader Choi glanced briefly at the empty space Huginn had left behind before continuing.

“I do not think they sent a messenger solely because of the Mana Cultivation Method.”

“What do you mean?”

“I had the feeling he came to confirm someone’s absence. Someone who is just as important to them as the Mana Cultivation Method that will be revealed to the world tomorrow—or perhaps even more important.”

I closed my mouth and quietly repeated one person’s name.

*Cheon Taemin.*

A living savior. An unprecedented Hunter who had never existed before and would never appear again.

If it became known that a man revered throughout the world and said to possess power no one could rival was unable to step forward, the enemies hiding in the shadows would not hesitate to attack.

“But information about his condition is the most confidential secret there is.”

Only six people knew that Cheon Taemin was currently in a vegetative state.

Team Leader Choi and me. Song Song and Im Kkeokjeong. And the Skeleton King and Magic Johnson.

Everyone who had known the truth before them was already dead.

Lee Jungryong, Song Cheonwoo, and finally Go Jun.

In the past and even now, the truth about Cheon Taemin was something that could never be revealed to the outside world. And Magic Johnson, whom we had been forced to ask for help, was someone Team Leader Choi had more than enough reason to trust.

Wasn’t he the one who had moved Cheon Taemin out of the secret area and taken measures to protect him with various kinds of Magic?

*Wait. Magic?*

My face stiffened as a thought suddenly crossed my mind. Team Leader Choi nodded at me.

“Do you remember what Mr. Johnson said in Ares Guild’s Area A?”

“……A mage.”

“Yes. Lee Jungryong had an assistant. Mr. Johnson said that a mage of Grand Mage level had constructed Area A.”

“Then, could it be…”

“There was always a chance that the secret had leaked from the very beginning.”

“……!”

“And if they already know that…”

After taking a breath, Team Leader Choi continued.

“It could become a difficult fight. Much more difficult than we expected.”

But why was that?

Contrary to the serious content of his words, his tone and expression were as calm as could be.

“Why are you looking at me like that?”

I scratched my chin and answered:

“I don’t know if it’s just my imagination, but you look pretty relaxed for someone saying all that.”

“Pardon?”

“No, it feels like your words and actions don’t match. You’ve always been the kind of person who put safety first, but just now, you didn’t even blink before using your grandfather’s name to make a bluff.”

Team Leader Choi blinked for a moment at my words, then gave a quiet laugh.

“Isn’t it obvious?”

“What’s obvious about it?”

“Because you are here, Mr. Jin Taekyung.”

“……Huh?”

“No matter how powerful a card our enemies play, I have a Joker card named Jin Taekyung. Naturally, that makes me bolder.”

For a moment, I couldn’t find anything to say. As I stood there stammering like Samryong the Mute,[^2] the smile around Team Leader Choi’s mouth deepened.

[^2]: Samryong the Mute is the title character of a well-known Korean short story by Na Do-hyang.

“Oh, and…”

“And? What else?”

“I’m hungry. Let’s have kimchi stew tonight, just as we originally decided.”

Pat, pat.

Team Leader Choi tapped me on the shoulder, picked up his coat, and left the office. I stood there dazed for a moment, watching his back with an incredulous expression.

Team Leader Choi had changed. He hadn’t used to be this kind of person.

But still…

*It doesn’t feel so bad.*

I muttered inwardly and followed him.

Even now, the smartphone in my pocket continued to buzz without end.

[^1]: A Korean proverb meaning that people often take corrective action only after it is too late; literally, “after losing the cow, repair the barn.”
## Chapter artifact 733

# Chapter 733

At some point, my body had become sturdy enough to stay perfectly fine even after going three days and nights without rest. Even so, being able to get a full night’s sleep was a wonderful thing.

Especially when I woke up refreshed in a place where I was staying with my precious family.

“Home really is the best.”

Sounding refreshed, I took my seat, and Team Leader Choi looked at me sourly from across the enormous dining table.

“This is my home, technically.”

“Is that what matters right now?”

“It is not a trivial matter. We are discussing legal ownership.”

“I’m starting to wonder if homeless people can even bear to live.”

“Anyone listening to you would think you truly had neither a home nor money.”

As if.

I had a house under my own name now, and more money than I knew what to do with.

But even if trillions of won were sleeping in my bank account, finding a safer place for my family and me to stay would be nearly impossible.

*No. At least not anywhere in Korea.*

From the outside, it looked like nothing more than an enormous mansion. In reality, it was an impregnable fortress wrapped in layer upon layer of protective Magic.

And since the public still knew it as Cheon Taemin’s mansion, it would not be an exaggeration to say that it carried more symbolic weight than even the Blue House.

*With everyone watching, breaking in is practically impossible. Even if an S-rank Hunter attacked, we could buy more than enough time.*

For someone like me, who put my family’s safety above all else in every situation, it was the perfect place.

Of course, Team Leader Choi’s perspective might have been a little different, considering he had suddenly ended up living with us.

“Now that I think about it, I am taking advantage of you a bit. Should I start paying rent this month?”

“I will accept it if you offer. At ten million won per person, forty million won a month should be about right.”

I gazed out the window at the sunlight pouring down and muttered:

“Ah, the weather’s nice.”

“……”

“By the way, why is it so expensive? You even got the calculation wrong.”

“My calculations are always accurate.”

“What are you talking about? Ten million per person means thirty million, not forty. My father died ages ago.”

“There is one more person.”

No sooner had Team Leader Choi finished speaking than a blond foreigner came shambling down the hall and dropped heavily into a chair.

“Give me food.”

Speak of the fucking devil.

Putting everything else aside, the very first thing he said after getting up and seeing our faces made it clear he was a first-rate lout.

“You gonna get your own damn food, or eat after I smack you?”

After considering the question carefully, the Skeleton King answered:

“I shall get my own food.”

“Good choice. While you’re at it, bring mine, too.”

“……?”

“Oh, and make sure you bring the soup. If you forget, you’ll die.”

One of the mansion’s greatest advantages was that the artificial intelligence installed in the kitchen was always preparing hot food.

A short while later, the Skeleton King returned with my meal despite grumbling the whole way, and Team Leader Choi stared intently as I devoured the yukgaejang.[^1]

“Mr. Jin Taekyung, you always eat well.”

“People aren’t machines. You have to eat to live.”

“Did you sleep well?”

“Yes. It’s been a while. I probably collapsed almost the moment I lay down.”

Team Leader Choi nodded as if he had expected that answer.

“So that is why you could not answer your phone.”

“My phone?”

“You received calls from several places during the night. Have you still not checked?”

“Huh?”

Only then did I check my smartphone. It had vibrated so much that I had switched it to silent, but there were now more than a hundred missed calls and messages that had piled up since last night.

*What the hell is this?*

The names appearing among them were far too familiar and illustrious to dismiss as advertisements or spam.

Prince Felix of the United Kingdom, whom I had met during the operation to suppress the Arch-Lich. Faye Chen, an S-rank Hunter.

Chuck Hagel of the United States, with whom I had destroyed a terrorist organization only two weeks ago by modern reckoning, and Magic Johnson, a name that had become impossible to leave out.

But it did not end there.

President Baek Hanseong was on the list, of course. So were President Doramp Jr. of the United States, whom I had met during my visit to the Pentagon, and Chairman Xiao Yang of China.

“It was a long night. Longer than I expected.”

Team Leader Choi tilted his coffee cup with a tired expression before continuing.

“Of course, that also allowed me to hear several pieces of news.”

“News?”

“Yes. Chairman Xiao Yang, in particular, gave me some rather interesting information.”

Tap, tap.

Team Leader Choi tapped the tablet PC in front of him with one long finger. A hologram rose above the screen and projected dozens of images.

Flash.

“……What is this?”

When the images finally finished loading, I narrowed my eyes and put down my spoon.

No matter how strong my stomach was or how accustomed I was to gruesome sights, I couldn’t keep eating while looking at something like this.

“Why are there so many corpses?”

“They were prisoners who were alive and well and incarcerated at Beijing Special Detention Center as recently as last night. And among them are some faces you know, Mr. Jin Taekyung.”

“People I know?”

Swish.

Instead of answering, Team Leader Choi waved his hand. The dozens of images scattered and vanished, leaving only one behind. That image expanded.

“Do you recognize him now?”

I stared silently at the image.

The face of the middle-aged man lying peacefully, as though he had fallen into a deep sleep, was unmistakably familiar. But the first person to recall his name was not me. It was the Skeleton King.

“That man. His name was, uh…… Wu Shaiming? Something like that. An odd name, in any case.”

The Skeleton King smiled confidently under the gaze of Team Leader Choi and me.

“Ha-ha. You underestimate the information-gathering abilities of this body. Unlike lazy creatures such as yourselves, I devoted myself to my smartphone even at the expense of my sleeping hours.”

“You just couldn’t sleep. You’re dead, after all.”

“……”

The Skeleton King grew dejected and began picking at his yukgaejang. Team Leader Choi nodded before speaking.

“Former Premier of the State Council of the People’s Republic of China and member of the Standing Committee of the Politburo. And……”

I finally remembered everything about Wu Shaiming and cut in.

“He was Wu Heixing’s father—the man who joined forces with Lee Jungryong and tried to kill me.”

“Correct. Wu Shaiming was China’s de facto second-in-command and the leader of the Crown Prince Party, the faction whose head was Chairman Xiao Yang’s greatest political rival.”

There was no way I wouldn’t know that.

After the operation to suppress the Arch-Lich, Wu Shaiming had raised suspicions about his son’s death, which had led me to learn more about him.

One of the main reasons Wu Heixing had been able to cause all kinds of trouble and still escape unscathed was that his father’s family, the Wu clan, was one of China’s most prestigious families.

But then……

“Didn’t that old man Wu Shaiming get knocked out after all the corruption he’d committed came to light? The last time I saw the news, he was waiting for trial.”

“That is correct. Chairman Xiao Yang did not miss the opportunity, and most of the Crown Prince Party—including Wu Shaiming—was imprisoned.”

“But Wu Shaiming suddenly died?”

“Wu Shaiming was still middle-aged, and he had spent decades drinking potions like water for the sake of his health. His cause of death was sudden cardiac arrest, but there is no way he and some fifty of his relatives could all die the same way at the exact same time.”

“His relatives? Then the pictures I saw earlier……”

“According to Chairman Xiao Yang’s information, they were all members of the Wu family. There were children among them, too.”

“……!”

*The annihilation of an entire household.*[^2]

The words, the sort of phrase one might only hear in Murim, sent a chill down my spine. At the same time, an unbelievable thought flashed through my mind.

“Team Leader Choi. Could it be that……”

But before I could finish, Team Leader Choi shook his head.

“It was not Chairman Xiao Yang’s doing. If anything, he must have wanted to persuade Wu Shaiming more than anyone.”

Persuade him.

Wu Shaiming had been Xiao Yang’s most powerful political rival.

Now that he had been rendered incapable of making a comeback, there was no particular reason to kill him—but there was not the slightest reason to keep him alive, either.

So what exactly had Xiao Yang wanted to gain by persuading him? What had Wu Shaiming possessed?

The Crown Prince Party’s influence, which had already collapsed? Or the enormous fortune that was practically destined to be seized?

I silently rolled the word *persuade* around in my mind. Before long, I realized the answer.

“……The Mana Cultivation Method.”

At the single word that escaped like a groan, the Skeleton King blinked, and Team Leader Choi answered in a low voice.

“Yes. Chairman Xiao Yang was trying to win Wu Shaiming over in order to obtain the very Mana Cultivation Method that had turned Wu Heixing into an S-rank Hunter.”

An S-rank Hunter with that level of power would naturally discover a unique training method of his own at some point.

But Wu Heixing had been different. He had already learned a Mana Cultivation Method passed down through his family, and after his death and Wu Shaiming’s downfall, I had stopped paying much attention to the matter.

*But the fact that Wu Shaiming and all his relatives suddenly died last night means……*

I had no interest in what Xiao Yang intended to do with the Mana Cultivation Method.

What mattered was that the annihilation of the Wu family had caused his attempt at persuasion to fail—and who had committed such an atrocity.

And I already knew the answer to that question.

“It must have been Odin Guild.”

A dry voice, unfamiliar even to me, slipped between my lips. Team Leader Choi ran his fingers over his coffee cup, which had gone cold.

“That is the most likely possibility.”

“……”

“According to Chairman Xiao Yang, Wu Shaiming had been prepared to accept the offer because he had no other choice. If he refused to hand over the Mana Cultivation Method, it would have been perfectly possible for him to receive at least a life sentence, or even the death penalty. But……”

Team Leader Choi suddenly let his words trail off and bit his lip.

“Someone else would not have wanted that.”

It felt as though the blood throughout my body had frozen.

*They had made their move.*

Much faster than I had expected, and in a far more brutal way.

*But even so, to wipe out an entire household……*

I stared at the hologram that had yet to disappear. Women, children, and old people. Every one of them had fallen into a deep sleep from which they would never wake.

Simply because they had been born into the Wu family.

*Were they willing to go this far to prevent the Mana Cultivation Method from leaking, or……*

*Was this a reply to what happened last night?*

Several thoughts lingered on the tip of my tongue before scattering. As I silently gazed at the faces of the dead, I suddenly spoke.

“Team Leader Choi.”

“Yes. Please, go ahead.”

“If you have time, would you like to go out for a cup of coffee with me?”

“I have no objection. But where are we suddenly going……”

“I wonder. Was it Paris?”

“What?”

As Team Leader Choi looked at me in confusion, I continued calmly.

“Odin Guild. I feel like going to see the boss’s ugly mug.”

“……!”

[^1]: Yukgaejang is a spicy Korean soup made with shredded beef, vegetables, and red pepper seasoning.

[^2]: A classical expression for the complete destruction of a family and its relatives, often including children.
## Chapter artifact 734

# Chapter 734

Team Leader Choi usually shows almost no change in expression.

He never reveals his feelings easily to other people, and he always keeps his interviews with the press short and focused on the essential points. Even veteran reporters—the kind who supposedly picked up a microphone at their first-birthday celebration—were reduced to stammering in his presence.[^1]

But even Team Leader Choi was ultimately a man of flesh and blood. Sometimes, he showed a surprisingly wide range of emotions.

Especially when he was talking with me. That was when he tended to pour out all the feelings he kept hidden.

Just like now.

“Odin Guild. I feel like going to see the boss’s ugly mug.”

“……!”

The instant I finished speaking, his mouth fell open in a daze. Beneath his trembling eyelids, his pupils were already shaking like an earthquake.

*This bastard’s planning to cause trouble again.*

Team Leader Choi stared at me with exactly that look in his eyes. After a long silence, he finally managed to force out his voice.

“Are you being serious right now?”

“Hm.”

After thinking for a moment, I continued.

“Probably fifty-fifty?”

“So you’re saying you’re half-insane.”

“Does it work like that?”

“This is a genuine question: where did the insane idea of going to see the Odin Guild Master right now come from? Your heart? Your head?”

“My heart.”

At my brief answer, Team Leader Choi sighed.

“That is a relief, at least. You are not completely insane yet.”

“You’re calling a perfectly sane person crazy? I’m just planning to look the man in the face and have a cup of coffee with him. Ares Guild has branches in France anyway, so I can use that as an excuse and kill two birds with one stone……”

“They are not chain stores. They are Guild branches. And you expect me to believe that? Are you joking?”

At Team Leader Choi’s utterly serious question, I smacked my lips.

“Well, if the conversation doesn’t go smoothly, there might be a little trouble.”

“I will interpret that as meaning there will be an enormous amount of trouble.”

I almost asked him what he was making such a big deal about, but I held back.

Even I could not honestly claim that Team Leader Choi’s concern was exaggerated.

It had only been a few weeks by modern reckoning since I had stormed into Ares Guild alone and smashed Go Jun’s head in.

*I’ve caused enough trouble that I can’t exactly argue with him.*

Besides, I was not an idiot.

I was fully aware that if I acted on what my heart was telling me right now, the outcome would probably be less than pleasant.

“All right.”

“The Eiffel Tower collapses, the Guild collapses, public opinion against us turns into a wasteland…… What?”

“I said all right.”

Team Leader Choi, who had already been suffering from vivid hallucinations one step ahead of me, blinked.

“Really?”

I nodded slightly as I answered.

“We don’t have a pretext in the first place.”

Even in Murim, where human lives were treated as no more valuable than livestock, you needed at least some justification. If I flew to Paris right now and picked a fight with Odin Guild, the only thing I would gain was an Interpol wanted notice.

*At least I had public support when I dealt with Go Jun.*

Even though that incident had caused a major stir around the world, it had taken place in Korea. Unlike this situation, there had been clear testimony and evidence.

And on top of that, the public had been furious with Go Jun for committing all kinds of crimes against humanity.

Those were the reasons I had been able to act outside the boundaries of the law without becoming a criminal myself.

*But Paris would be different.*

My heart was screaming at me to storm into Paris and raise hell, but the part of my reason that was still alive was facing reality.

At my decision, Team Leader Choi’s eyes grew round. The Skeleton King, who had been enthusiastically shoveling yukgaejang into his mouth while staring at his smartphone, dropped his spoon.

“This cannot be! Did you just say ‘justification’?”

“No way. You bastard, you’re a monster! What have you done to the treacherous human?”

“……”

“Mr. Jin Taekyung, this is merely a simple verification procedure, so please do not take offense. Where was the first place we met?”

“Doppelganger! Leave the treacherous human’s body!”

*These two were acting like fucking idiots.*

Instead of answering, I grabbed the spoon sitting on the dining table and smacked the Skeleton King on the crown of his head.

Crack!

“My skull! My beautiful skull!”

Team Leader Choi watched the Skeleton King howl and nodded.

“Thank goodness. You really are Jin Taekyung.”

“……”

After completing that strangely unpleasant verification procedure, Team Leader Choi let out a sigh of relief.

“In any case, I am glad you changed your mind.”

“If this were a problem that could be solved that way, I would have bought a ticket to Paris and left already, to hell with international crime and everything else.”

“That is true. If Odin Guild disappeared, another Odin Guild would appear.”

It was the same as when Ares Guild had been our enemy.

The world was vast, and the empty space left by a defeated enemy would always be filled by another one.

Just as we had taken Ares Guild by siege, the same was true of them. Now it was a lord’s duty to defend his castle from the competitors swarming around it and expand his territory as much as possible.

Besides, Odin Guild was not some wolf that nobody knew where had rolled in from.

It was a predator with a massive body and sharp claws.

It was even greedy. Just like the information written on the tablet PC Team Leader Choi had placed in front of me.

“What is this……?”

“This is the participation proposal the Chinese government sent to Odin Guild during the monster wave in Sichuan Province. Of course, it was unofficial and had no legal force.”

An unofficial proposal.

I wondered how Team Leader Choi had obtained material that should have been almost impossible to leak, but the answer came quickly.

“Grandpa Jongseok gave it to you?”

“Not Grandpa Jongseok. Chairman Xiao Yang.”

“Yes. So, Grandpa Jongseok.”

“……”

“What? It’s friendly. Besides, that old man likes me a lot, too.”

Team Leader Choi looked at me with an expression that suggested he had half given up and continued.

“As you know, Mr. Jin Taekyung, during the early stages of the crisis, China’s State Council and Politburo Standing Committee were reluctant to request help from abroad. They were especially vehemently opposed to support from the West.”

The Skeleton King, who had been tenderly stroking his skull, suddenly interrupted with an expression of confusion.

“They opposed it? Why?”

*Well, why would that be?*

There could have been many reasons, but in the end, they all led to one answer. In a kind voice, I gave him the correct response.

“Because it’s China.”

“What does that mean? Humans are dying either way!”

“Because it’s China.”

“No, treacherous human. It appears you have failed to understand this body’s question……”

“Yeah. China.”

“……?”

“Some things are just like that. You might not understand yet.”

Leaving the Skeleton King’s face covered in question marks behind me, I turned back toward Team Leader Choi.

“But you did ask the West for help eventually, didn’t you? Prince Felix of the United Kingdom and Magic Johnson, too.”

“Yes. Once the damage caused by the Arch-Lich reached astronomical levels, China’s leadership had no choice but to accept Chairman Xiao Yang’s argument. However, they would have to pay an appropriate diplomatic and material price once the crisis ended, so they had to take that into account when assembling their forces.”

That was how four S-rank Hunters had gathered, even without counting me.

Of course, that alone constituted an incredible force. But what mattered now was that Odin Guild, which should have been one of the central pillars alongside Ares Guild under Lee Jungryong’s leadership, had withdrawn.

“But why did they reject the proposal? At this amount, it seems like enough money for Odin Guild to accept without hesitation. No, they absolutely should have accepted it.”

I had asked because the employment fee written in the unofficial proposal on the tablet screen was truly staggering.

It was nearly twice the fee I had once heard Ares Guild received, and there were several other options attached as well.

It was the best possible treatment, paying full value for the name Odin.

But Team Leader Choi’s next words neatly answered my question.

“The Chinese government was the one that ultimately rejected it.”

“What?”

“When the negotiations were nearly complete, Odin Guild added an additional condition.”

“What kind of additional condition……?”

Team Leader Choi took a sip of his lukewarm coffee before speaking in a low voice.

“They wanted China to lease ten cities—including Chengdu, Meishan, Ziyang, and Suining, the representative administrative districts of Sichuan Province—to Odin Guild for the next ninety-nine years, as well as authorize the establishment of an official branch in Beijing.”[^2]

“……!”

“In effect, they were asking China to cede Sichuan Province. The authorization to establish an official branch, which the Chinese government prohibited, was merely an added bonus.”

*Good God. What did I just hear?*

I stared blankly at Team Leader Choi and muttered:

“Wow, those bastards are insane. They’re worse than Chinks.”

“According to the information Chairman Xiao Yang provided, Odin Guild contacted the French government just before the negotiations.”

“Even so, how could they make such a completely insane proposal?”

“They’re French.”

“Even so, there’s such a thing as common sense.”

“They’re French.”

“……Excuse me, Team Leader Choi?”

“French.”

“……”

For some reason, I felt a strange sense of déjà vu. Was it just my imagination?

As I stared at him with a sour expression, Team Leader Choi spoke to me in a gentle voice.

“Mr. Jin Taekyung, did you know that Koreans call the French by another name?”

“Oh.”

With a sudden flash of insight, I let out an exclamation.

“European Chinks……!”

Team Leader Choi nodded as he looked at me.

“Their skin color and culture are different, but they are still ‘that sort.’ Whether the President commits adultery or does anything else, the French do not care. It is not a coincidence that Odin Guild has its headquarters in Paris. Even when scandals arise, they cause very little commotion.”

“But wasn’t that just an Internet meme?”

“I remember my school days in Paris. When a photograph of my maternal grandfather appeared in our history textbook, everyone in the classroom looked at me and pulled their eyes into slits.”

“Oh.”

“The teacher did it, too.”

“Oh, no. Oh……”

“It is all right. That happened long ago.”

Team Leader Choi put away the painful memory from his childhood that had suddenly resurfaced and continued.

“More important than anything else is the fact that even Odin Guild, with that kind of French government behind it, cannot move freely. Just as when they assassinated Wu Shaiming’s family this time, they have no choice but to stop at a warning rather than pose a direct physical threat to us.”

That was true.

The flag of Cheon Taemin was flying above the walls of Ares Guild, and the image I had shown the world until now could not be ignored, either.

Even if the opponent was Odin Guild, considered the greatest Guild in the world, or any other massive Guild, the same applied.

And more than anything else……

“People around the world are cheering for us. The media may not be able to openly criticize the major Guilds, but there is still a considerable amount of public sentiment condemning them.”

*Public sentiment.*

The strongest weapon—and shield—we had gained by releasing the Mana Cultivation Method.

We had to make the fullest possible use of the public sentiment in our hands. We had to make sure even Odin Guild could not approach us……

“Um, sorry to ruin the mood.”

The Skeleton King suddenly spoke and held out his smartphone.

“Is this the cheering you were referring to?”

On the screen of the smartphone he offered me was a breaking-news alert that had been posted only a few dozen seconds earlier.

> **Odin Guild Announces Its Support for Ares**

> **Odin Guild Reveals a New Mana Cultivation Method**

> **Senior Official: “This Project Has Been in Preparation for Several Years”**

> **“Though We’re a Step Late, We Want to Change the World with Them.” The World’s Greatest Guild Shows Its Class**

*Fuck. What the hell is this now?*

[^1]: A **doljanchi** is a Korean child’s first-birthday celebration, traditionally featuring a ceremony in which the child chooses an object symbolizing their future.

[^2]: Meishan, Ziyang, and Suining are cities in Sichuan Province.

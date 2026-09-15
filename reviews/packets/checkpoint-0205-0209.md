# Checkpoint Review — 205–209

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

# Chapters 205–209

## Plot

Jin Taekyung awakens after seven days of recovery from Jeok Cheongang’s successful opening of his Conception and Governor Vessels. His perception and control of qi have improved dramatically. Ak Bulgun and Jin Wikyung tell him about the Star-Array Grand Banquet in Henan, a gathering founded by the absent Martial God. Taekyung decides that he wants to pursue greater strength because he enjoys martial arts.

After logging out, Taekyung allows Seong Jinho to stay with him after Jinho loses his housing deposit to Kim Jong-su. During Taekyung’s commute, an unidentified black sphere causes a Gate to open near a tollgate. B-rank ogres overwhelm the assembled Hunters, and the System forcibly assigns Taekyung the Peak-Grade Gate Suppression Quest. Taekyung rescues civilians, kills the ogres, gains at least one Level, and prevents arriving military Hunters from taking the remaining monsters before collecting their valuable parts.

The incident causes four deaths and five severe injuries, while another Gate in Yangju City causes even heavier casualties that the government attempts to conceal. Reporter Kim identifies Taekyung as a C-rank Hunter, and the media names him the “Tollgate Hero.” His identity becomes public, he reaches number one in real-time searches, and he waits at KPS for a live Nine O’Clock News Desk interview.

Meanwhile, the remodeled Peace Guild House is revealed to contain extensive magical security and communication equipment. Sangdong Guild had used Familiars to monitor the Peace Guild members during their vacation, though the surveillance has since been handled.

## Continuity

- Taekyung’s Conception and Governor Vessels are open, greatly improving his qi perception, control, circulation, and explosive power.
- The rewards for the Conception Vessel Opening Achievement and the rare Achievement from completing the vessel Quest remain unrevealed.
- The Star-Array Grand Banquet is held every two or three years in Henan; the Martial God founded it but has not appeared for many years. The Martial God’s true condition remains unknown.
- Jin Mukyung remains secluded and has not returned to Heaven’s Gate Temple.
- The Jin Family has received the invitation to the Star-Array Grand Banquet; whether Taekyung will attend remains unresolved.
- Seong Jinho is staying with Taekyung after Kim Jong-su absconded with his five-million-won housing deposit.
- Taekyung remains officially registered as a C-rank Hunter in Hope Guild.
- An unidentified black sphere opened the tollgate Gate after destroying Mr. Park’s taxi.
- The System forcibly accepted the Peak-Grade Gate Suppression Quest. Its Reward and Failure conditions remain unknown.
- The tollgate Gate produced ten B-rank ogres after widening. Taekyung defeated more than ten, including a Lv.85 Ogre, and collected their valuable parts.
- The tollgate incident caused four deaths and five severe injuries. An earlier F-rank Gate near Yangju City caused ten deaths and more than twenty severe injuries, despite official reports understating the casualties.
- Taekyung’s identity and C-rank status are now public. He is known as the Tollgate Hero and is awaiting a live KPS interview.
- Sangdong Guild’s Familiars monitored the Peace Guild members during their vacation; Im Kkeokjeong did not notice that he was being watched.
- Jeok Cheongang still anticipates an unexplained event occurring sooner than expected and says he must endure for several more years.

## Translation Decisions

- Retain “Heavenly Martial Physique,” “Heavenly Dragon,” “One Step Back,” and “Scorching Yang Qi.”
- Render 임맥 타통 as “Conception Vessel Opening” and 임독양맥 as “Conception and Governor Vessels.”
- Render 성라대연 as “Star-Array Grand Banquet.”
- Render 게이트 진압 as “Gate Suppression” and 오우거 as “ogre.”
- Render 톨게이트 영웅 as “Tollgate Hero.”
- Preserve “Old Master” for Taekyung’s private address to Jeok Cheongang.
- Retain “goshiwon,” “officetel,” “Hope Guild,” “EXP,” “tollgate,” “Feather Fall,” and “Grease.”
- Render 상도의 as “professional courtesy” and 호적 메이트 as “sibling-on-paper.”

## Durable state

{
  "active_continuity": [
    "One Step Back granted Taekyung two level-ups and 20 Bonus Points.",
    "Jeok Cheongang selected three Scorching Yang Qi elixirs for Taekyung's Fire Gate Clan training and successfully opened Taekyung's Conception and Governor Vessels.",
    "Taekyung is publicly recognized as Jeok Cheongang's Disciple and heir to the Fire Gate Clan's orthodox lineage.",
    "Jin Mukyung remains secluded in the training hall and has not returned to Heaven's Gate Temple.",
    "The Jin Family received an invitation to the Star-Array Grand Banquet in Henan.",
    "Seong Jinho is staying at Taekyung's new family home after losing his housing deposit to Kim Jong-su.",
    "Taekyung remains officially registered as a C-rank Hunter belonging to Hope Guild.",
    "A Gate previously caused casualties at Uldae-ri, Jangheung-myeon, Yangju City; Hunters and the military reported exterminating fifty-eight goblins.",
    "An unidentified black sphere destroyed Mr. Park's taxi, but Taekyung rescued him.",
    "A Gate opened on a congested commute roadway near Hwang Cheol Soo's tollgate.",
    "The System forcibly accepted the Peak-Grade Gate Suppression Quest.",
    "The Gate released ten B-rank ogres after widening, overwhelming the tollgate Hunter team.",
    "Taekyung defeated more than ten B-rank ogres, including a Lv.85 Ogre, and gained at least one Level.",
    "Taekyung blocked an arriving military Hunter team from taking the remaining ogres and collected their valuable parts.",
    "The tollgate incident caused four deaths and five severe injuries; an F-rank Gate near Yangju City had caused ten deaths and more than twenty severe injuries earlier that day.",
    "Government personnel acknowledged that Gate casualties were being downplayed and concealed.",
    "Reporter Kim learned Taekyung's identity and C-rank status while preparing a newspaper report about the tollgate incident.",
    "The Peace Guild House has been extensively remodeled and equipped with magical communication, observation, and alarm systems.",
    "Sangdong Guild Familiars monitored the Peace Guild members during their vacation; Im Kkeokjeong was watched without realizing it, while the others became aware of the surveillance.",
    "Taekyung's identity and C-rank status are now public, he is ranked first in real-time searches as the Tollgate Hero, and he is waiting for a live KPS news interview."
  ],
  "continuity_sources": [
    209
  ],
  "open_questions": [
    "What are the rewards for the Conception Vessel Opening Achievement and the rare Achievement earned after completing the Conception and Governor Vessels Quest?",
    "Will Jin Mukyung return to Heaven's Gate Temple before the appointed deadline?",
    "What event does Jeok Cheongang believe may occur sooner than expected, and why must he endure for several more years?",
    "What is the true condition of the absent Martial God?",
    "Will Taekyung attend the Star-Array Grand Banquet, and what exactly was the answer that changed the three men's expressions?",
    "What are the Reward and Failure conditions of the Gate Suppression Quest?",
    "How will the Gate near Hwang Cheol Soo's tollgate ultimately be contained, and what further monsters may emerge?"
  ],
  "safe_through": 209,
  "temporary_decisions": [
    "Render 혈도 타통 as “Acupoint Opening.”",
    "Render 회음혈 as “Huiyin Acupoint.”",
    "Render 임맥 타통 as “Conception Vessel Opening.”",
    "Render 성라대연 as “Star-Array Grand Banquet.”",
    "Render 노야 as “Old Master” when Taekyung addresses Jeok Cheongang privately.",
    "Render 고시원 as “goshiwon” and 오피스텔 as “officetel.”",
    "Render 오우거 as “ogre” and 게이트 진압 as “Gate Suppression.”",
    "Render 상도의 as “professional courtesy.”"
  ],
  "version": 1
}

## Reading copies

## Chapter artifact 205

# Chapter 205

How long had I been unconscious?

My body felt as light as a feather, and my mind was clear. It felt as though I had only slept for a moment, but while I was out, the world had changed a great deal.

*What is this?*

The room contained only simple furniture and a few decorations. The faint scent of wood lingered in the recently built room.

It was a familiar sight, one I had seen countless times before. And yet it had never felt so strange.

*This is…*

I looked around with trembling eyes.

I could feel qi saturating the air, and everything around me was so bright that it was as if someone had implanted night-vision goggles in my eyes.

Even the moon visible beyond the latticed window seemed bizarre.

Why was the moon out when it was this bright? Wasn’t that actually the sun?

I sat there dazed for a long while, as though bewitched by a ghost, before finally realizing the truth.

“Oh.”

This world—the Murim—was exactly as I remembered it. Nothing had changed except me.

A small voice slipped from my lips before I realized it.

“The Conception and Governor Vessels…”

When a blocked tunnel is opened, light pours in.

Anyone accustomed to the darkness inside a tunnel would naturally find that light strange. That was exactly how I felt now.

Only after removing the enormous obstacle known as the Conception and Governor Vessels could I finally see a light I had never known existed.

“You’re awake.”

The owner of the sudden voice stood leaning against the doorway.

There wasn’t even a lamp in the room, yet every age spot and wrinkle covering his face stood out clearly to my eyes.

“Old Master.”

Fire King Jeok Cheongang answered as if he had been waiting for me.

“Good.”

“You’ve gotten really old.”

For a moment, he was struck speechless. I added one more thing.

“And you’re strong. Stronger than anyone I’ve ever seen.”

This wasn’t a way of taking back what I had just said, nor was it simple flattery. It was one hundred percent sincere.

Now that I had opened the Conception and Governor Vessels, I could glimpse, however faintly, the terrifying martial arts hidden within that small frame.

“Ahem. What an obvious thing to say.”

Jeok Cheongang cleared his throat awkwardly and changed the subject.

“So, how is your condition?”

“It’s the best.”

There was no need to read a System message or circulate my internal energy to examine my body. I could feel it the moment I opened my eyes.

The corners of his mouth twitched at my immediate answer.

“Of course it is. Do you have any idea how much trouble this old man went through—no, I handled it with ease, but it’s still not something just anyone could do. Yes, indeed.”

“……”

“I’m telling the truth!”

“I didn’t say anything.”

“Wasn’t that look on your face disrespectful? Your expression!”

That was because his intentions were painfully obvious.

Compared to the unfathomable depth of his martial arts, his personality was completely transparent.

Violent and eccentric to an unbelievable degree, yet surprisingly easy to understand—that was the image Jeok Cheongang had given me.

“I have ptosis, so people often misunderstand my expression.”

I put on an utterly shameless face and denied everything. Jeok Cheongang began to snort.

“Why is everyone here like this? That so-called Lesser Family Head keeps neglecting major family business to come by and see you, and those physicians are all quacks who do nothing but gossip about whether you’re going to live or die.”

“Wait a second. Die? Did someone get seriously hurt?”

“Who else would it be?”

At his meaningful stare, I asked with a sinking feeling:

“Are you talking about me?”

“That’s right. The whole place was turned upside down for the past seven days and nights. If I’d known this kind of uproar would happen, I would’ve buried you under a rock until you came to your senses.”

I didn’t hear the rest. I blinked at him in a daze.

“I was unconscious for seven whole days and nights?”

“Not *seven whole days and nights.* It was only seven. I thought you’d be lying there for at least a month, but the Heavenly Martial Physique really is something.”

“This isn’t some kind of side effect, is it?”

“Listen to the insolence in this brat’s voice. I went through all that trouble to open your Conception and Governor Vessels, and what do I get? ‘Side effect?’”

“You said it was easy.”

Jeok Cheongang froze, then shouted:

“That’s beside the point! Even after you take a shit, you still have to wipe your ass. I removed all the turbid qi that had been piling up inside your body, layer upon layer. Obviously, you’d need time to adjust to your new body!”

“……”

He was so worked up that his analogy was a little strange, but I understood what he meant.

*Some kind of optimization process, maybe?*

Come to think of it, it would be strange for someone on the verge of death to leap to his feet just because his Conception and Governor Vessels had been opened. Even after leveling up, mental fatigue could still build up and knock a person unconscious.

Even so, a whole week?

“Then the gathering must be over.”

“The gathering—or half a gathering—ended three days ago.”

Jeok Cheongang was still visibly sulking as he continued.

“That fellow Ak Bulgun is still here.”

I tilted my head at the unexpected name.

Ak Bulgun, an Instructor at Heaven’s Gate Temple, had originally come to the Jin Family of Taiyuan to take Jin Mukyung back.

Could he really be planning to wait until Jin Mukyung finished his seclusion?

“Why is Sir Ak still here?”

“Ask him yourself.”

“Come on. I was wrong, so stop being angry and tell me.”

Jeok Cheongang replied curtly:

“Do I look that petty to you? I mean that he’s on his way here, so you can hear it from him directly.”

“Oh.”

Sure enough, he was right. Not long afterward, two people appeared, accompanied by the sound of approaching footsteps.

“Little brother!”

Jin Wikyung’s voice trembled with emotion when he saw that I had awakened after seven days and nights. Behind him came Ak Bulgun’s blunt voice.

“It seems Great Hero Jeok is here as well. I have something important to discuss with you. Would that be all right?”

Jeok Cheongang answered firmly:

“No. Get out.”

“It concerns Young Hero Jin’s future as well.”

“……Damn it.”

Jeok Cheongang muttered a quiet curse and sat down on a chair.

* * *

As his appearance suggested, Ak Bulgun was not much of an orator. After listening to his dry explanation, I spoke.

“So you’re inviting us to that… Star… Star-Array…”

What was it called again? His explanation had been so boring that I could barely remember what I had heard.

When I hesitated, Jeok Cheongang supplied the name for me.

“The Star-Array Grand Banquet.”

“Ah, right. The Star-Array Grand Banquet.”

“It is a grand event where martial artists from across the world gather in one place to test their strength and reinforce their bonds. It is held once every two or three years, and this year’s Star-Array Grand Banquet will take place in Henan.”

At Ak Bulgun’s additional explanation, Jeok Cheongang gave a derisive laugh.

“Reinforce the bonds of the Murim, my ass. It’s a place where powerful people cheer each other on, flatter one another, and build connections.”

Talk about a mercilessly blunt assessment.

Ak Bulgun gave a small nod without offering any real objection. It seemed Jeok Cheongang wasn’t wrong.

Jeok Cheongang continued in a cutting tone:

“It was the same forty years ago. The Demonic Cult had barely been driven out, and already they were fighting over their interests… I saw nothing but things no decent person would want to witness.”

I could more or less picture what it had been like.

A time of chaos was also a time of opportunity. The greedy and powerful never let an opportunity pass them by.

It might even have been partly related to why Jeok Cheongang had gone into seclusion on Mount Jiuhua again.

*Still, it sounds like an enormous event.*

Jeok Cheongang narrowed his eyes at my curious gaze.

“What are you looking at?”

“It’s nothing. I was just wondering why someone who hates crowds and anything troublesome would go to a place like that.”

“I was asked to.”

“……?”

Was Jeok Cheongang really the sort of person to comply simply because someone asked him to?

The question vanished as soon as I heard the title of the person who had asked.

“The Martial God.”

“Oh.”

The Martial God I had only heard about in stories.

They said there were Ten Kings on earth, Three Saints in the heavens, and one god above them all.

If it had been a request from that Martial God, even Jeok Cheongang probably couldn’t have refused easily.

“He was the one who created the Star-Array Grand Banquet and asked this old man to attend. That was the first and last time the One God, Three Saints, and Ten Kings gathered in one place.”

As though recalling those days, Jeok Cheongang tapped the armrest of his chair with a distant look in his eyes. Then he suddenly turned his gaze toward Ak Bulgun.

“How is he doing?”

“He has not shown himself for a very long time. There are even unpleasant rumors circulating…”

“You’re worried the Martial God might be dead? Ha. There are far too many idiots with nothing but shit in their heads.”

After letting out a hollow laugh, Jeok Cheongang turned back to me.

“So, what do you think?”

“Hmm.”

“Even if it is a feast for the powerful, there is no denying that the Star-Array Grand Banquet is a gathering of martial artists from across the world. Anyone can display their abilities to the fullest, regardless of their background.”

“I’m not sure.”

I scratched the back of my head, unable to answer easily.

The Star-Array Grand Banquet. A gathering where martial artists from across the world assembled to reinforce their bonds and test their strength.

It was a chance to fight outstanding masters and make a name for myself throughout the Central Plains.

But…

*Was that really so important?*

Ever since I came to the Murim, I had occasionally found myself wondering about that.

Why did I practice martial arts? Why did I keep training even after becoming strong enough to protect my life and the people precious to me?

After thinking about it for a long time, I finally found the answer not long ago.

*Because it’s fun.*

Just as I had told Cheongpung, I liked martial arts. They were fun.

Even if I obtained more money and fame than I could possibly imagine, I would never stop training.

I was already addicted to martial arts. I had discovered how much pleasure and satisfaction there was in becoming stronger.

“Young Hero Jin.”

Ak Bulgun’s quiet voice broke through my thoughts. It was time to answer.

I took a deep breath and opened my mouth.

“I…”

After hearing my answer, the expressions of all three men changed strangely.

* * *

The three men left.

Alone in the room, I thought back to the conversation I had shared with Jeok Cheongang at the end.

*You want to become stronger. Is that your answer?*

*Yes.*

*Does that mean you’ll attend the Star-Array Grand Banquet?*

*It doesn’t matter where I go. If it can make me stronger than I am now.*

*You’re still young, and you’re already strong enough. If you attend the Star-Array Grand Banquet, you could etch your name into the Murim and gain wealth and fame. Aren’t you tempted by those things?*

*I’m tempted. By martial arts. By a higher realm.*

*……!*

Jeok Cheongang had stared at me with trembling eyes for a long while before leaving me with a single sentence.

*Come to my quarters when the sun rises.*

I recalled his final words as I sat down on the bed.

My field of vision was as bright as midday, and I could hear the footsteps and breathing of people outside the pavilion as clearly as if they were right beside me.

*You’re already strong enough.*

Those were the words Jeok Cheongang had spoken himself before leaving. Fire King Jeok Cheongang had acknowledged me.

But there was something else I wanted to hear.

*You’re stronger than anyone.*

Back when I was an F-rank Hunter, my wish was to become an E-rank Hunter. When I first set foot in the Murim, my goal had been to surpass Hyuk Mujin.

As time passed, I grew stronger, and my dreams became more ambitious.

Some people might call that greed. But greed and dreams were different.

I had a dream now. Fire King Jeok Cheongang was the guide who would help me move toward it.

*I’m looking forward to morning.*

There were roughly three shichen[^1] left until dawn.

It looked like tonight would be a long one—for both me and Jeok Cheongang.

*Especially for me. It’ll be a night longer than I can even imagine.*

I lay down straight on the bed.

It was time to leave behind all the things that had happened in the Murim and return.

*Logout.*

Ding.

With the cheerful system alert, my eyes slowly closed.

[^1]: A shichen is a traditional time unit of approximately two hours.
## Chapter artifact 206

# Chapter 206

Ding.

> **System**
> Logout completed.

I hadn’t opened my eyes, but I knew.

Everything around me had changed at the same time as the System notification.

Instead of a fur-covered bed and a hard wooden pillow, I felt the soft cushions of a sofa beneath me. Along with the bubbling sound of boiling water, a familiar smell stabbed at my nose.

*Th-This is…*

The smell of ramen. And not just any ramen—it had been cooked spectacularly well!

The moment I realized what it was, my stomach, which had been craving seasoning after spending more than a month in the Murim, began to churn violently.

“I’m hungry!”

My shout came straight from the soul. I opened my eyes, and a familiar face poked out from the brightly lit kitchen.

Jinho hyung’s sparse beard and greasy hair were just as I remembered them. He rubbed at his glasses, which were completely fogged over with steam, and beamed at me.

“Oh, my beloved little brother Taekyung. Did you sleep well?”

His tone was disgusting in a way it normally wasn’t, but I had already lost my mind at the smell of ramen.

“Ramen!”

“Jesus, what’s gotten into you?”

“Kimchi!”

“You really were sleeping soundly. I tried shaking you awake.”

“Cold rice! At least five bowls!”

“……Uh, got it. I was about to bring it over anyway.”

A little while later, I stared at the pot filled to the brim with broth and noodles and murmured in a blissful voice:

“This is insane…”

“Lift just the top layer of noodles a little. There’s a soft-boiled egg underneath.”

“Gasp.”

Just as he said, a soft-boiled egg appeared beneath the noodles, still holding its perfect shape.

As I swallowed a breath, Jinho hyung handed me two small side dishes.

“Here, kimchi and pickled radish. The rice is plain white rice I took out an hour ago. Once you finish all the noodles and drink a few mouthfuls of broth, drop in the cold rice and…”

“Are you…”

“Hm?”

“Are you God?”

Jinho hyung placed an exam-prep book beneath the pot and answered solemnly:

“Genesis, chapter one, verse one. Thus spoke Seong Jinho: ‘If you do not eat now, the broth shall grow cold, and the noodles shall become hopelessly soggy.’”

“Ah, ah…”

“Little lamb, how can you wag your mouth when ramen is sitting before you? Lick up every last drop of broth.”

I had lived my entire life without religion, but that was no longer the case.

I gazed up at Jinho hyung and picked up my chopsticks.

“Amen.”

“Ramen.”

Today, I wouldn’t have minded dying with my nose buried in ramen broth.

I buried my head over the huge pot and moved my chopsticks without pause. Because the distance between my mouth and the chopsticks was so short, the noodles kept disappearing into me.

Slurp! Slurp! Slurrrrrp!

Springy noodles, spicy broth. When I burst the soft-boiled egg, I couldn’t hold back the bliss and regret, and a single tear rolled down my cheek.

*It’s delicious. So delicious.*

I love seasoning. It’s the best.

I lost myself in that artificial flavor that could only be enjoyed in the modern world and kept inhaling the food for quite some time.

When I finally came to my senses, only empty pots and bowls remained before me. Even the bowl that had been piled high with cold rice was spotless.

“Buuurp.”

“You’ve got to be kidding me.”

Jinho hyung stared at me in horror as I rubbed my stomach after letting out a huge belch.

“You ate seven packets of ramen and five bowls of rice by yourself in ten minutes? Are you even human?”

“Carbonation! Cola!”

“……C-Calm down. I’ll get some.”

It was only after I downed three consecutive 1.5-liter bottles of cola that my senses finally returned to something resembling normal.

“Whew. That was good. I’m full.”

“That’s strange. Why am I hungry?”

“Bear with it. You would’ve done the same if you were me.”

I answered absentmindedly and collapsed back against the sofa behind me.

Hadn’t they said it was made from some kind of monster hide? Maybe that was why it felt so incredible.

“Oh, this is comfortable.”

If this had been a goshiwon studio,[^1] there wouldn’t have been enough room to fit a sofa.

Jinho hyung would have had to cook ramen in the communal lounge instead of the kitchen, or bring in a portable burner.

“Moving here really was the right choice.”

“Yeah. It’s a nice place.”

Jinho hyung scraped the bottom of the pot with a spoon as he answered.

“Right? Mom and Hayeon are going to love it when they see… it.”

A flash of realization passed through my mind.

I stared blankly around the room, my mouth hanging open. The space and furniture were far larger and finer than anything in a goshiwon.

And there was one person who fit naturally into this space and situation.

“Should I make some more Jjapagetti? I’m hungry.”

“……”

“This time, I’m not giving you any. If you want some, say so now.”

I barely managed to force out my voice.

“……You.”

“Hm?”

“Why the hell are you here, you bastard!”

My roar erupted in the dark dawn and shook the residential neighborhood of Ilsan.

* * *

After hearing the entire story, I could only ask in disbelief:

“You were inside the capsule?”

Jinho hyung knelt politely with both arms raised and answered while avoiding my gaze.

“Yeah. I held my breath and stayed perfectly still.”

No wonder the mover had struggled so much.

Even I hadn’t sensed anything particularly strange. Compared to when I had first found and moved the capsule, my physical strength had increased several times over. And back then, my Qi Sense hadn’t been nearly as sharp as it was now.

There was one more thing, too.

*No, for fuck’s sake. Who would’ve imagined that?*

No matter how expensive and sophisticated an alarm system was, it couldn’t detect an intruder if the power was off.

I never would have expected someone to be hiding inside the capsule.

“Whew. What happened to that place you said you were going to find? Didn’t you say you’d get a room with your friend and move out?”

“Y-You know Kim Jong-su, right? My college classmate. You had a drink with us once a couple of years ago.”

His face was hazy in my memory, but I definitely remembered that happening.

Hadn’t he been a fairly successful used-car dealer at the time? If he hadn’t bought us beef that day, I probably would have forgotten him entirely.

“Is that the friend you said you were going to live with?”

“Yeah. Though he’s not my friend anymore.”

“Hyung, did he…”

“Five million won for the deposit. That bastard took it and ran.”

Why did bad premonitions always come true?

I rubbed my throbbing forehead.

“How did that happen?”

“Well, I told him I’d be taking the exam soon, so he said he’d handle all the details…”

I raised a hand to stop him before he could continue.

I didn’t need to hear the rest. It was clichéd, but it was one of those methods that always worked.

“You just handed it over to him without looking into it properly?”

“I’d known him for more than ten years. How was I supposed to know he’d do that over a few million won?”

“But those few million won were your entire fortune, weren’t they?”

“……”

If he had gone so far as to sneak into my place inside a capsule, he clearly didn’t even have enough money left for this month’s goshiwon rent.

*Was he from Jeju Island or something?*

A premium-grade black cow.[^2]

There wasn’t a bigger black cow—a bigger sucker—anywhere.

[^2]: “Black cow” is Korean slang for a sucker; Jeju is also known for its native black cattle. At the look in my eyes, Jinho hyung lowered his head completely.

“I was only planning to impose on you for a couple of months, until I could get some money together.”

“You should’ve just told me.”

“I agonized over it by myself, but I couldn’t bring myself to say anything. I’m your older hyung. I can’t burden my little brother.”

“……”

What on earth did this man consider a burden?

“I’m sorry. I really am.”

With his mournful voice, Jinho hyung lowered his arms. His eyes had grown moist before I knew it.

“Taekyung…”

“Jinho hyung…”

I continued in a sympathetic voice:

“Who told you to lower your arms?”

“Hm?”

“Put them back up. Before I beat you.”

“……Yes, sir.”

Jinho hyung hurriedly returned his arms to their original position, and I let out a sigh despite myself.

The unexpected situation was absurd, but at the same time, I felt heavyhearted.

*You should’ve told me sooner.*

Maybe that wouldn’t have been possible in the past, but the current me had more than enough ability to help Jinho hyung. No, even back then, I would have supported him in every way I could.

*After all the time we’d spent together.*

We weren’t related by blood, but he was as good as my real brother. That was who Jinho hyung was.

I had even considered asking him to live with me for a while, because I felt uneasy about leaving him on his own.

*I was planning to tell Mom and Hayeon after the college entrance exam anyway, so I still have some time, but…*

I looked around the house with a troubled expression. It wasn’t exactly like the place I remembered from my childhood, but it was still the home my family had finally reclaimed.

The house that still held traces of my father, whose voice had grown blurred in my memory.

At last, I made up my mind and opened my mouth.

“This house won’t work, hyung. I know you’ll be disappointed, but try to understand.”

Jinho hyung forced a bright expression and shook his head.

“What’s there to be disappointed about? It’s all my fault.”

“What about your luggage? Have you unpacked?”

“Not yet. It’s only a few books and some clothes, so it’s light. I’ll just leave with you when you go to work.”

Come to think of it, the sky outside had been bright for a while now. It was already eight o’clock. Considering the traffic and the distance between Ilsan and Bucheon, I was cutting it rather close for work.

“I think we’ll have to go separately. Get everything ready for now.”

“Okay, got it.”

“And clean the whole new place before I get off work.”

“……Huh?”

“Don’t get the wrong idea. I’m not talking about this place. Just wait a second.”

I pulled out my phone and searched through my messages.

At last, I found the address I was looking for in my chat with Team Leader Choi, saved under the name “Designer-Brand Junkie.”

“Ah, here it is. I sent the address to your number, so find your way there.”

“Wait. What address?”

“An officetel.”

“Huh?”

“There’s a place the Guild said they’d provide for me. I turned it down last time because it felt like too much, but I might as well accept it now.”

A small laugh escaped me when I saw Jinho hyung’s eyes widen.

“Why are you so surprised? I’m doing pretty well these days.”

“……!”

“This house needs to be remodeled anyway, so let’s live there together. It’ll be convenient for me to commute, too.”

“Ta-Taekyung.”

I turned away, pretending not to hear the tremor in Jinho hyung’s voice.

I had no interest in dealing with an embarrassing scene first thing in the morning. And I didn’t particularly want to hear thanks from the person who had comforted me during the hardest period of my life.

*It’s fine.*

Yes. This was enough.

* * *

Mid-September. The heat had finally weakened, but the morning commute remained unchanged.

The taxi driver honked at the occasional inconsiderate driver cutting into traffic on the congested road, then turned up the radio.

> An F-rank Gate has appeared in Uldae-ri, Jangheung-myeon, Yangju City, and an immediate evacuation order has been issued. With nearby Hunters and military units cooperating to suppress it quickly, the confirmed number of casualties currently stands at six…

“Goddamn it. As if traffic wasn’t bad enough, now those monster bastards are causing trouble, too.”

After spitting out the colorful curse, he glanced at me in the passenger seat.

“You’re a Hunter too, right?”

“For now.”

At this point, I wasn’t entirely sure whether I was a Hunter or a Murim warrior.

Officially, at least in the modern world, I was a C-rank Hunter belonging to Hope Guild.

The taxi driver grinned at my answer.

“I knew it. You can tell a Hunter at a glance.”

“I suppose you can.”

It was like the difference between a herbivore and a carnivore.

There were exceptions, but everyone gave off a certain impression. Someone my size, carrying a large case, had to be one of two things:

A musician who liked working out, or a Hunter.

*You can tell right away.*

It wasn’t anything particularly special, especially not to a taxi driver who met countless passengers every day.

But this middle-aged man didn’t know how to stop talking.

“Hey, can I ask you something?”

“Sure.”

“It seems like Gates have been opening more often lately. Can’t anything be done about it?”

“……What?”

“I mean, how are ordinary people like me supposed to live without worrying? A Gate could open in my apartment parking lot the moment I wake up in the morning. What’s the point of working my butt off taking fares when safe-zone land costs a fortune?”

I answered with an incredulous expression:

“That’s true, but why are you asking me?”

“I know you can’t do anything about it. I’m just frustrated, that’s all. Frustrated.”

“……I’m frustrated too.”

I was a Hunter, not a prophet.

How was I supposed to know something even Nostradamus couldn’t predict?

No one could predict when a Gate would form. The only reason they could suppress them quickly was because they had spent astronomical sums installing mana measuring devices all over the place.

Just like the breaking news currently coming through the radio.

> Breaking news. The F-rank Gate that appeared earlier in Yangju City has stabilized. Hunters and the military have exterminated a total of fifty-eight goblins and are conducting a search for any remaining monsters…

“Every time you turn around, it’s Gates and monsters. I’m sick to death of it.”

Beep.

The taxi driver turned off the radio with an irritated motion.

An uncomfortable silence filled the car, but I was more than happy to reach my destination in peace.

*I wonder what Mom and Hayeon are doing right now.*

I was lost in thought as I stared out the window when it happened.

Honk! Hoooonk!

A faint horn drilled into my ears, followed by a jumble of tangled noises. I hurriedly rolled down the window.

*What is that? Was there an accident?*

The taxi driver looked bewildered by my sudden movement.

“Why are you opening the window when I have the air conditioning on—”

“Wait. Just wait a second.”

The taxi driver fell silent at my serious tone, and I circulated my internal energy.

As my hearing and eyesight, already far beyond the limits of ordinary humans, swept over the congested road—

“Huh?”

Far in the distance, a single black dot shot up into the air.

I watched it fall in an arc and recognized what it was.

“……A car?”

Though it had been crumpled into a ball, I could see it clearly.

The crumpled hood. The twisted scrap metal.

And I could see exactly where it was going to land as it came flying toward us, scattering a shower of glass.

Whoooooosh!

*Oh, shit.*

Why here of all places?

[^1]: A goshiwon is a very small, inexpensive room-for-rent housing arrangement, often used by students and exam candidates.
## Chapter artifact 207

# Chapter 207

Whoooosh.

An unidentified black sphere plummeted with a terrifying roar as it tore through the air.

The shadow cast over the taxi made its driver, Mr. Park, sense death.

*So this is how it ends.*

The faces of his daughter, who had entered high school that year, and his beloved wife flashed before his eyes. They had planned to go out for seolleongtang after work. Who knew that would be foreshadowing?

*And I’d already had such an unlucky day.*

He didn’t even wonder what the thing was. Knowing wouldn’t change the fact that he was going to die.

All he could do was sit frozen like a stone statue and stare helplessly at death as it drew closer by the second.

Whoooom!

It was time to leave for the afterlife.

Mr. Park squeezed his eyes shut beneath the sphere’s shadow, which had completely covered the driver’s seat, and finally screamed.

“Gaaaaaaaaah!”

Boom! Craaash!

The sheet metal crumpled like paper, and shattered glass flew in every direction. Then, in the next moment—

“Whoa, my eardrums almost burst. You’ve got quite a set of lungs on you.”

“Gaaah… Huh?”

A voice pierced his ears.

Mr. Park stopped screaming and blinked.

“Huh? Huhhh?”

He couldn’t tell whether he was dreaming or awake.

He had definitely been sitting in the driver’s seat a second ago—no, half a second ago—but now he was sitting on the shoulder of the road roughly five meters away.

“W-What the hell…”

Mr. Park stared blankly at his taxi, which had been flattened into a sheet of metal, then lifted his head.

His savior was standing there—the person who had rescued him from the brink of death.

“Y-You’re the passenger?”

The sturdily built young man, Jin Taekyung, did not answer. Frowning as he glared at something in the distance, he opened his mouth.

“Sir.”

Mr. Park’s heart pounded. He had already realized it instinctively. Something enormous was happening, and if he wanted to survive, he had to follow the Hunter passenger’s instructions.

“Run back the way you came. Don’t look back. Just keep running.”

“Y-Yes, sir!”

“And don’t forget to tell everyone else.”

“T-Tell them what?”

Jin Taekyung pointed ahead.

Unlike the sky, where bright morning sunlight poured down, darkness was spreading over the place his finger indicated.

He spoke calmly to Mr. Park, who stood there with his mouth hanging open in shock.

“A Gate has opened.”

At the same time, a roar that made the hair on the back of one’s neck stand on end erupted from the far end of the road.

—Gwooooooar!

* * *

The monster’s roar was more effective than any loudspeaker.

Those who realized what was happening abandoned their cars and began running.

“A Gate! A Gate has appeared!”

“Run!”

“Seokjun! Honey!”

The congested road was engulfed in chaos in an instant.

Shrill screams and frantic voices rang out from every direction.

Avoiding the people sprinting back the way they had come for dear life, I advanced across the roofs of the cars. A System notification rang in my ears.

Ding.



> **System**
>
> - A sudden Quest, **Gate Suppression**, has been created.
>
> - You cannot refuse the Quest.
>
> - The Quest has been forcibly accepted!



*Now it isn’t even giving me a choice.*

Couldn’t it at least ask first?

I clicked my tongue inwardly and opened the Quest window. A translucent holographic window abruptly appeared in the air.



## Quest

### Gate Suppression

An unexpected Gate has appeared!

The monsters that have set foot on Earth are hungry for blood, and delicious prey is spread out all around them.

Minimize casualties and eliminate the monsters to suppress the Gate.



**Grade:** Peak

**Restriction:** None

**Mission:** Eliminate monsters (Incomplete)

**Reward:** ???

**Failure:** ???



This was a goddamn disaster.

Of all places, a Gate had appeared on a road jammed with people on their way to work—not at sea or in the mountains.

The bigger problem was that the monsters weren’t insignificant riffraff like goblins or orcs.

—Gwoooooooooar!

Boom! Krrr-boom!

They were larger than cargo trucks, with fangs bigger and sharper than industrial saw blades. Every time they swung the dark, iron clubs in their hands, concrete and cars were smashed to pieces.

By both strength and appearance, they were monsters in every sense of the word.

I never thought I’d encounter creatures I had only seen in monster encyclopedias on my way to work.

I muttered under my breath.

“Ogres…”

They were classified as B-rank monsters, but the strength and destructive instincts they possessed were far beyond that.

For example, during the early days of the Great Cataclysm, it had been ogres who served as the vanguard of the monster legions and destroyed countless cities.

*That must be why they’re considered the strongest among B-rank monsters.*

And monsters like that had appeared right here.

The Gate had not fully opened yet, so there were only five or six of them. But even that was an enormous threat.

*I have to stop them before the casualties get any worse.*

I wasn’t the only one who had thought of that. Eight hundred meters ahead, I saw about twenty figures charging toward the ogres, who were swinging their weapons in every direction.

“Hold the line!”

Clang-clang-clang!

Their identity was obvious from the gleaming armor, shields, and assortment of weapons they carried.

They were Hunters.

* * *

B-rank Hunter Hwang Cheol Soo broke out in a cold sweat.

*A Gate… has appeared?*

What were the odds of a Gate appearing? He didn’t know the exact figure, but he had heard they were lower than those of most natural disasters.

After the death of Demon King Asmodeus brought the Great Cataclysm to an end, the number of Gates forming across the world had visibly declined from dozens a day. Leading scholars had rushed to publish papers about the situation.

[Humanity’s Victory, the End of Gates.]

[The Connection Between Demon King Asmodeus and the Gates.]

[Complete Peace Within Ten Years.]

But they had all been wrong.

Gates had once appeared only once or twice every year or two, but this was already the fourth one in the country this year.

The bigger problem was that this fourth Gate had opened at the tollgate Hwang Cheol Soo was responsible for.

*And it’s a B-rank Gate, on top of that.*

That alone was horrifying enough. But the creatures emerging from the Gate were ogres, classified among the strongest of all B-rank monsters.

Boom! Thud-thud-thud!

“Guh!”

“Healer!”

“Archers, keep firing! Tanks, draw their attention!”

Thud-thud-thud!

The tollgate team, made up of two B-rank Hunters and fifteen C-rank Hunters, was being pushed back helplessly.

After only two or three blows from an ogre’s iron club, tower shields shattered and the tanks went flying one after another.

*What am I looking at?*

Hwang Cheol Soo was only thirty years old.

He had no particular combat sense or command ability. He was merely a civil-servant Hunter who had been promised a comfortable job and a generous pension thanks to receiving a high rank.

*What do I do? What am I supposed to do…?*

As Hwang Cheol Soo stood frozen like a plaster statue, the assistant team leader shouted.

“Team Leader! Pull yourself together! We have to hold out until support arrives, no matter what it takes!”

“Y-Yeah. Right. We only have to hold out for five more minutes.”

“We can take them once the special forces regiment and the nearby Hunters arrive. So…”

Wham! Boom!

Hwang Cheol Soo stared blankly at the assistant team leader, who had been slammed into a refrigerated truck.

A huge piece of concrete had flown from somewhere and struck him.

“Healer!”

At the same time as he shouted, Hwang Cheol Soo realized the truth.

There were only two healers on the team, and the assistant team leader had been the last one still standing.

Of the seventeen team members, including Hwang Cheol Soo, fewer than half were still on their feet.

“W-What the hell…”

Only one minute had passed since the battle began.

But the outcome had already been decided.

The gap between top-tier B-rank monsters and Hunters who had been lulled into peace while playing mobile games at a tollgate was simply overwhelming.

Yet the ordeal was not over.

“Team Leader!”

“The Gate! Look at the Gate!”

Grkkk, grkkk—

As the team members shouted, the rift in the air began to widen.

Pitch-black darkness. Mana churned within it as it spewed out enormous bodies.

—Gwoooooar!

—Kraaaagh!

Boom! Boom! Boom!

Groaning ferociously, the ogres landed on the ground. Sighs escaped from every direction.

“Fuck…”

“A-Ah…”

They had already been overwhelmingly outmatched despite having nearly three times as many fighters.

Now that the number of ogres had grown to ten, despair settled heavily over the Hunters.

“T-Team Leader…”

“W-What do we do now?”

“…”

Hwang Cheol Soo swallowed dryly.

The difference in strength was already overwhelming, and the outcome was no longer something worth debating.

But one thought filled his mind.

*Can I survive?*

It wasn’t only his question. Everyone here was wondering the same thing.

And they waited for the commander to give them the answer they wanted to hear.

“Team Leader!”

“I-I…”

Before he could finish speaking, Hwang Cheol Soo’s feet were already moving backward.

In the past, he had sworn to become humanity’s shield and protect the people from the threat of monsters.

But he wasn’t interested in dying a pointless death like this.

*Even if reinforcements arrive, they can’t kill those things.*

If so, there was only one option left.

“B-Based on the commander’s judgment, we should make a strategic retreat…”

The moment Hwang Cheol Soo began speaking in a trembling voice—

Whoooooosh! Boom!

A streak of light shot forward.

It passed over the heads of the Hunters who had been slowly backing away, pierced its target with perfect accuracy, and exploded it at the same time.

Splash.

What fell in scattered droplets from the air was not rain, but blood. Then pieces of flesh giving off a rotten stench came pelting down like hail.

“…Huh?”

Boom.

Along with someone’s dazed voice, the ogre’s massive body collapsed like a rotten old tree.

—Gwo?

“What is this…?”

Humans and monsters alike stared blankly at the surreal sight.

Then—

“Whoa. What kind of destructive power is that?”

The bright voice did not fit the situation at all.

Hwang Cheol Soo hurriedly turned around to find the source of the voice, and goose bumps ran down his skin.

“Gasp.”

He hadn’t sensed the slightest trace of the man’s presence. Even now, while looking directly at him, he still couldn’t sense him.

But the figure standing tall on the roof of a tour bus was neither a ghost nor a monster.

His eyes curved like half-moons between his roughly tousled black-brown hair.

“Hello.”

“W-Who are you?”

“I’m just someone on his way to work.”

“Y-Yes?”

“Um, may I skip the formalities and get to the point?”

That was exactly what Hwang Cheol Soo wanted. The ogres had already recovered from their brief confusion and were approaching, scraping the ground with their iron clubs.

At the Hunters’ frantic nods, the young man, Jin Taekyung, smiled.

“If you’re all not going to fight, squeeze yourselves into a corner.”

“…”

“Oh, and if I catch you stealing EXP, you’re dead.”

EXP? Stealing?

Before they could even figure out what he meant, the spear in Jin Taekyung’s hand turned into light and shot forward.

Whoooooosh!



* * *

Shriiiing! Crunch!

The spearhead pierced through a thick jaw.

It tore through hide, flesh, tongue, and the roof of the mouth in succession before jutting out through the top of the ogre’s head.

At that moment, iron clubs came rushing in from both sides.

Whoooosh!

The terrifying sound of air splitting.

But I was no longer there.

I had already slipped into one of the ogre’s arms and was driving a dagger from my Inventory precisely into its Huiyin Acupoint.

Stab!

—Gwoooooooooooooooooar!

“Congratulations on opening the Conception Vessel.”

There was a world of difference between clearing a pathway and opening one up.

With a howl that seemed to contain its very soul, the ogre dropped to its knees.

Before it had time to feel any more pain, I slashed its throat with the dagger.

Squelch!

The monster’s blood and screams mixed together, while a series of sweet sounds continued tickling my ears.

Ding. Ding. Ding.



> **System**
>
> - You have defeated **Lv.84 Ogre**!
>
> - You have acquired a considerable amount of EXP!
>
> - You have defeated **Lv.83 Ogre**!
>
> - You have acquired a considerable amount of EXP!



*Buuuuurp.*

*Man, I’m stuffed.*
## Chapter artifact 208

# Chapter 208

Unstoppable in every direction.

That was me now. Wherever my eyes could see and my hands could reach, I cut, stabbed, and smashed without restraint. Every time the spearhead flashed, blood spurted, and flesh and bone split apart.

I moved freely among the enormous ogres without the slightest hindrance.

Srrk! Krrrunch!

—Gwooooooar!

With a death rattle, the three-meter-tall body dropped to its knees.

The Gate continued spewing out ogres, but they posed no problem for me. When two came out, I killed three. When three came out, I killed four.

*This is easy. Almost ridiculously so.*

The last time I had applied points was during my duel with Chulwoo.

But opening my Conception and Governor Vessels had pushed my control and explosive power over my internal energy, along with my senses, to an extreme level.

Even when the ogres’ iron clubs, packed with immense force, came crashing down from every direction, they looked unbelievably slow.

The ogres in my eyes were nothing more than idiots who had no idea how to use their strength properly.

Whoooosh! Thud!

—Grrrgh…

Another ogre, one of countless by now, dropped to its knees with a wet, blood-choked rattle.

The furry hand that had tried to grasp the spearhead piercing straight through its Adam’s apple suddenly lost its strength and fell limply to the ground.

Ding.



> **System**
>
> - You have defeated **Lv.85 Ogre**!
>
> - You have acquired a considerable amount of EXP!
>
> - Level Up!

“Oh.”

I had already leveled up.

The rate at which I was sucking up EXP while clearing them out by myself was no joke.

*Is it because every one of these bastards is higher-level than me?*

My current Level was somewhere in the mid-to-high seventies, so I was five to ten Levels below the ogres.

Since I was slicing them up like pork shoulder at a butcher shop, it was only natural that my Level would rise quickly.

The EXP was far more generous than I had expected.

*No, wait.*

A thought suddenly flashed through my mind.

I gazed at the Gate, which continued to churn and spit out ogres, my eyes shining.

This was completely…

*This is a popular restaurant.*

The Gate kept spitting out EXP—or rather, monsters—and I kept killing them. If that continued steadily, then…

*So this was where the conveyor-belt sushi place was.*

The EXP I got from the ogres was sweeter than tuna belly.

My mouth curved upward as I imagined chewing every ogre that came out and digesting it into points.

That was when it happened.

Vroooom. Rat-a-tat-tat-tat!

—Hold! Hold!

—Descend!

Three or four combat helicopters flew in with the roar of fierce winds, circled overhead, and then dropped around twenty Hunters like lightning.

Shu-shu-shu-shu!

They were falling from a height of more than twenty meters. At that height, even Hunters outfitted with magical Equipment were bound to strain their knees on landing.

But these weren’t the incompetent amateurs who had been here before I arrived.

“Feather Fall.”

With the mage’s incantation, a ripple of energy passed through the air.

The bodies that had been plunging downward quickly and violently began to slow.

The ogres, which had been about to swing their iron clubs, hesitated after missing their timing. Then the second spell was cast.

“Grease!”

—Gwo?

Boom! Crash!

The four remaining ogres lost their balance. Some staggered, while others collapsed onto the ground.

“Now!”

At the shout, the spell slowing their descent was dispelled, and the melee fighters shot forward like streaks of light.

The ogres let out low growls, sensing their imminent deaths.

That was when—

Clang! Clang-clang!

“…Huh?”

The Hunters who had just been about to drive their weapons into the ogres’ chests stared at me with baffled expressions.

*What the hell did this bastard just do?*

*Is he insane?*

That was exactly what their faces said.

I had knocked away all their attacks with a single swing. In a mild voice, I said, “Come on, let’s observe some professional courtesy.”

“…”

These bastards were trying to steal mobs I already had dead to rights.

* * *

“That really happened?”

At the captain’s question, the Hunter Team Leader nodded.

“Yes. I’ve been on the support team for two years, and I’ve never seen anyone like him.”

“He sounds interesting.”

“Interesting? He’s a complete psycho.”

“Perhaps.”

The captain slowly looked around.

The tollgate had collapsed so completely that it was impossible to recognize its original shape. Monster blood was scattered across the half-destroyed road.

There were overturned and wrecked cars as well, but not many.

“How many casualties?”

Soldiers and Hunters had different statuses, but both were registered with the government as members of military support teams.

The Hunter Team Leader promptly answered his superior’s question.

“So far, four dead and five with severe injuries. We’ll know more once we finish checking.”

“Four dead and five with severe injuries.”

The captain repeated the figures calmly before continuing.

“This is the second Gate occurrence today.”

“Tell me about it. An F-rank Gate erupted near Yangju City about an hour ago. I don’t know if something serious is going on.”

The captain clicked his tongue.

“Hey, Team Leader Jeong.”

“Yes, sir.”

“An F-rank Gate that appeared in the town center, or a B-rank Gate that appeared in the middle of a road packed with commuters. Which one looks more serious?”

“Well…”

“But there were more casualties on the F-rank Gate side. Ten dead and more than twenty with severe injuries.”

“What? That can’t be right. The breaking news said…”

“Downplaying it. Covering it up. After two years, you should be getting a feel for what kind of place this is.”

The captain let out a deep sigh.

“From our perspective, a hundred bows wouldn’t be enough to thank him. He’s a civilian hero who stopped a major catastrophe all by himself.”

“That’s true. He does seem a little crazy, though.”

“Team Leader Jeong.”

“Ah, no, that’s not what I meant. I mean he’s an insanely strong crazy person. He killed more than ten ogres by himself, so he must be an A-rank Hunter or something.”

“Either way, watch what you say. There are plenty of ears around.”

“They’re all our people. What ears could there be—ah.”

The Team Leader turned toward the place the captain indicated and immediately scowled.

A skinny, middle-aged man carrying an expensive camera was approaching them with an excited stride.

“Captain Yoo! Team Leader Jeong! Where have you two been hiding? I’ve been looking everywhere.”

The Hunter Team Leader replied with a deeply displeased expression.

“To avoid you, Reporter Kim.”

“Oh, come on. Why are you so prickly today, Team Leader Jeong? I’m part of the support team too.”

“You’re only part of the team at times like this, huh? The rest of the time, you’re a military correspondent. You’re usually drowning in a hangover—aren’t you getting a little too excited just because you landed one scoop?”

The reporter flinched, and the captain stepped in for him.

“That’s enough. And Reporter Kim, please be more careful in the future. This is an accident scene, and running around excitedly because you found a scoop doesn’t look good.”

“…Ahem. I’ll be more careful from now on.”

Even as he answered, the reporter’s eyes sparkled with anticipation.

A Gate occurrence was nothing short of a natural disaster. In some ways, it was even worse.

If a typhoon was going to hit the Korean Peninsula, people could at least predict when and how it would arrive and which areas would suffer damage. The creation of a Gate, however, was impossible to predict.

*Two Gates appearing in one day was unprecedented, and now one of them was even B-rank.*

The tollgate’s security team being helplessly overrun, followed by the heroic appearance of an unknown Hunter who stopped a major catastrophe during rush hour!

It was a great story.

The reporter had already finished sketching it out in his head, and he was practically buzzing with excitement.

“So where’s our hero? He’s an A-rank Hunter, right? What’s his name? A fresh new face would sell better for something like this.”

“A new face? Give me a break.”

The Hunter Team Leader pointed behind the reporter.

“He’s over there. The new face.”

“Where? I don’t see him.”

No matter how many times he looked around, there was no hero wearing gleaming armor in sight.

All he could see were military personnel busily cleaning up the accident scene.

The reporter’s eyes swept frantically over the area before stopping abruptly.

“There, Team Leader Jeong. Is that him? In front of the ogre’s corpse…”

“The man wearing the tracksuit pants? Yes, that’s him.”

Swish. Srrk, srrk.

Squatting like someone making a huge batch of kimchi[^1], the young man deftly separated the fat, meat, and hide from the corpse. The reporter muttered,

“…That’s too new a face.”

“Fresh, right? Isn’t that the picture you wanted?”

“The ogre meat certainly looks fresh.”

“He’s been at it for a while. The staff offered to do it for him, but he won’t let them touch it. Says it’s all his.”

The even funnier part was that his butchering technique was unbelievably good. In fact, the two employees assigned to process the corpses were stealing glances at him and trying to imitate the movements of his hands.

“Is he really an A-rank Hunter?”

“Who knows? If he can wipe out ogres by himself, he definitely should be. But the more I look at him, the less convinced I am.”

“Team Leader Jeong asked him, but he said they could talk once he finished butchering.”

The three men exchanged looks filled with a mixture of belief and doubt.

That was when—

“Whew. Finished.”

The A-rank Hunter, who had cut the notoriously tough ogre meat into pieces like mackerel, straightened his back and stood up.

The reporter looked at the training pants stretched out around the knees and the three-stripe slippers, then muttered,

“Why does a guy who makes that much money live like this?”

*Was this some kind of humblebrag?*

It was absurd, but the longer he looked, the fresher it seemed. After all, the most important thing in the media was character.

*A down-to-earth A-rank Hunter with a fierce sense of justice. This picture could turn out great. He’s handsome, too, with such an open, striking face.*

Yes, this was better than some polished, model-student image.

The reporter grinned and raised his camera.

He wanted to capture a natural shot with absolutely no staging.

* * *

*As expected of an ogre. Nothing to waste.*

I looked over the neatly separated by-products with a satisfied smile.

Ogres were practically symbols of strength, which made them popular among men.

There were plenty of people looking for ogre products, but since ogres were monsters classified as the upper tier of B-rank, the supply was rather limited.

*Good thing I only went for their vital spots.*

I was humming as I sorted the by-products when—

Click.

“…Huh?”

I turned my head toward the mechanical sound that had suddenly come from nowhere.

A middle-aged man who had been pressing his camera shutter repeatedly was smiling amiably at me.

“Oh dear, did I startle you?”

*What the hell is this guy?*

I asked incredulously, “Most people are surprised when they get photographed without permission. Are they supposed to be happy about it?”

“You might be happy when you appear in tomorrow’s newspaper.”

“The newspaper?”

“Ah, I’m afraid I haven’t introduced myself. Here, let’s start with my business card.”

I accepted the business card, which had a military camouflage pattern printed on it, and read it aloud.

“Military correspondent.”

“You know the Capital Defense Command, right? The Capital Defense Command. I’m the military reporter assigned to Support Team 25.”

“Ah, yes.”

“And the two gentlemen coming up behind me are from the support team as well.”

The reporter gave me a smile and raised his thumb as two men approached from behind him.

One wore a Special Forces uniform and the other armor. They were, well, dressed like a stereotypical soldier and Hunter.

“Nice to meet you. I’m Captain Yoo Sijin, Team Leader of Support Team 25.”

“Ah, yes.”

*Somehow, his name sounded less like a descendant of the sun and more like the sun’s regret.*

I tilted my head and exchanged introductions with the two men.

As soon as the perfunctory introductions and praise for the great thing I had done were over, the military reporter, who had been staring at me with fervent eyes, spoke up.

“You said you’re Hunter Jin Taekyung, correct?”

“Yes. Why?”

“Given the field I cover, I know nearly every A-rank Hunter worth knowing. But…”

Ah, I roughly knew what he was trying to say.

It was something I would have to deal with sooner or later.

I answered readily, “I’m not A-rank.”

“What?”

“And I’m not S-rank either, of course.”

“…”

Three question marks seemed to appear on their faces at the same time. I couldn’t help but chuckle. *This was fun.*

*After being knocked around this way and that in another world, I hide my strength in reality.*

That would make a decent novel title.

When I just kept smiling without saying anything, the reporter spoke in a faltering voice.

“Th-Then perhaps you’re B-rank?”

“No. I’m C-rank.”

“…C-rank? You mean C-rank, not C-cup?”

“Yes.”

*What kind of bullshit is C-cup? And why the hell is he looking at my chest?*

I ignored their waves of disbelief and continued, “I was on my way to the Guild when a Gate happened to open…”

“Th-Then what?”

I couldn’t answer the reporter’s urgent question.

I had just remembered something I’d momentarily forgotten.

“…By any chance, what time is it now?”

Damn it. I’m late.

[^1]: Kimchi-making, especially in large batches, is traditionally a communal household activity in Korea.
## Chapter artifact 209

# Chapter 209

Ten in the morning.

Im Kkeokjeong, a D-rank Hunter of the Peace Guild who had come to work after spending a vacation as sweet as honey, stood there with his mouth hanging open.

“Whoa. What is this?”

It was understandable.

Before his vacation—in other words, just a week ago—the Guild House had been nothing more than a rundown neighborhood corner store.

But now, right before his eyes, stood a sign made of gleaming marble and luxurious lettering.

**<Peace Guild>**

“Wow. They went all out with the remodeling.”

Just as Im Kkeokjeong was admiring the exterior, a familiar voice came from somewhere.

“Why are you standing outside instead of coming in?”

Startled, he looked around. But when he saw neither the usual CCTV nor even an intercom, he cautiously opened his mouth.

“Te-Team Leader Choi? Is that you?”

“Yes. It’s me.”

“What is this? How are you talking to me?”

The reply came without the slightest hesitation, as though he had been waiting for that exact question.

“It’s nothing special. We commissioned the Vercheni family, a venerable Italian family of artisans, to make it especially for us. It includes message, observation, and alarm magic…”

“Ah, no. You don’t have to explain all that.”

“Oh. Then, if you open the mahogany door wrapped in salamander leather resistant to flames and come inside…”

“I’m coming in! I said I’m coming in!”

“…Yes.”

Click.

Along with that somehow dejected voice, the locked door slid open.

The interior of the Guild House had changed just as dramatically as the exterior. Three people were waiting for Im Kkeokjeong inside.

“Welcome.”

“Hunter Im.”

“Uncle’s here?”

Team Leader Choi, the practical owner of the Peace Guild; Butler Kim, who nominally served as its Guild Master; and Song Song, the guild’s lone woman.

The three of them were seated around a round table. As they greeted him in turn, Im Kkeokjeong let out a good-natured laugh.

“Maybe it’s because it’s been so long, but it’s good to see you all. Did you get plenty of rest during your vacation?”

The moment he finished speaking, the expressions of all three changed strangely.

After a brief silence, Song Song spoke.

“I rested. But there were so many bugs in the house that it bothered me.”

“Bugs?”

“Yes. Weren’t there any bugs at your place, Uncle?”

At Song Song’s question, Im Kkeokjeong tilted his head.

Come to think of it, his wife had complained about something similar several times during their vacation.

“Nothing much, just a fly or two. She said they kept coming in no matter how many she caught, so I left them alone, and then they quieted down. They hardly flew around, either.”

“Oh, really?”

“Yeah. They were the most well-behaved flies I’ve ever seen.”

Song Song shuddered uneasily.

“There were so many that I felt too uncomfortable even to shower. It felt like the bugs were watching me.”

“The bugs? Ha-ha-ha! Miss Song, you’re quite the joker.”

“…”

Im Kkeokjeong threw his head back and laughed. He failed to notice the other three exchanging meaningful looks and words he could not hear.

*He doesn’t seem to know.*

*Looks like he didn’t notice.*

*Wow. Is this guy seriously that dense?*

Unlike the three people who had been watched throughout their vacation by Familiars sent by the Sangdong Guild, Im Kkeokjeong had returned from a truly blissful vacation without knowing a thing.

It wasn’t that he hadn’t been watched. He had been watched; he simply didn’t know it.

The saying *ignorance is bliss* could not have been more fitting.

“Those fucking perverts. If I catch them later, I’m going to rip their balls off.”

If the mages of the Sangdong Guild had heard Song Song muttering those words, they would have felt the hair on the back of their necks stand up.

Im Kkeokjeong’s laughter abruptly stopped.

“Huh? What did you just say? Perverts?”

“No. I just said the bugs were disgusting.”

“Is it still that bad? I know someone who works for a company in that field. Want me to ask them about it?”

Song Song gave a quiet laugh at his genuine concern, then pressed her lips together and pointed at the two people sitting beside her.

“They’re all gone now. Those two put in a lot of effort. Especially Butler Kim.”

“Really? Kim hyung—I mean, Guild Master. Looks like you know a thing or two about that sort of thing.”

Butler Kim answered with an awkward smile.

“Not at all. I happened to know a junior who worked in that field.”

“Oh, exterminating pests?”

“…Yes, something like that.”

In a way, monsters were just enormous pests, so he was not technically wrong.

Im Kkeokjeong, who had effectively turned one of Bucheon’s leading Hunter Guilds into Cesco,[^1] continued in all seriousness.

“Your junior must be pretty skilled.”

“Ah, yes. He’s quite good.”

He was so good at beating them down that he was one of the war heroes of the Great Cataclysm.

Of course, to Butler Kim, Sangdong Guild Master Im Chunsoo was nothing more than one of the trainees he had once worked like a dog.

“Let’s stop talking about that. More importantly…”

Team Leader Choi had been grimacing as he struggled to hold back his laughter for some time. He hurriedly changed the subject.

There happened to be one person who made for a much more suitable topic.

“Why isn’t Jin Taekyung here?”

While they laughed and chatted, the appointed start time had long since passed.

Only now realizing Jin Taekyung’s absence, Im Kkeokjeong nervously stroked his beard.

“What happened? That kid Taekyung has never been late before. When it comes to diligence, he’s the best person I know.”

“I’m well aware of that.”

Team Leader Choi nodded.

He had already thoroughly investigated Jin Taekyung’s past once. Judging by the years of activity recorded in the report and what he had personally witnessed since then, Taekyung’s diligence and persistence were genuine.

*The raid starts in two hours…*

Had something happened?

As Team Leader Choi pondered the matter and picked up his phone, Song Song, who had been quiet for a while, suddenly spoke.

“Taurus—I mean, Jin Taekyung.”

“…”

“He’s right there.”

Her pale, slender finger pointed over Team Leader Choi’s shoulder.

The next moment, the guild members naturally turned in the direction she indicated, and their mouths fell open.

A familiar face filled the eighty-inch television screen mounted on the wall of the Guild House.

“…Huh.”

“Taekyung! Isn’t that Taekyung?”

“I believe that is indeed Hunter Jin Taekyung.”

Butler Kim was usually calm, but he was so flustered that even he began to stammer.

The guild members, however, had already lost all interest in anything except the caption appearing beneath Jin Taekyung’s face.

**Jin Taekyung** *(Bucheon City, Wonmi-gu. C-rank Hunter)*

**Live broadcast) Tollgate Hero**

“Tollgate Hero? What’s that supposed to mean? Why can’t we hear anything?”

“It’s muted! It’s in mute mode! Turn the sound on, quick!”

Only after someone hurriedly fiddled with the television did the blocked sound begin to spill out.

“Fwoosh-fwoosh-fwoosh-fwoosh! Ta-ta-ta-ta-ta!”

Along with some incomprehensible noise, Jin Taekyung’s voice continued.

“…And that’s how it happened.”

“Yes, I see. Then, finally, could you give us a few words about how you feel?”

“Uh, first of all, I love my family very much, and I’m incredibly grateful to all the members of the Peace Guild. And the person I like…”

“Yes! I see.”

“W-Wait a second.”

“That concludes our interview due to time constraints. Viewers, you have just watched an interview with Jin Taekyung, the Tollgate Hero!”

The screen showed the reporter’s beaming face one last time before switching to a cosmetics commercial.

Im Kkeokjeong shouted, “What the hell was that? I couldn’t hear anything!”

“Just a moment. I’ll search for it right away. Tollgate Hero, Tollgate Hero… Holy crap.”

“Song-i. What is it?”

Song Song had gone rigid, her eyes round. Without saying a word, she held out her phone.

The main page of the web portal was displayed on the screen. The three syllables of Jin Taekyung’s name were plastered across it.

“Jin Taekyung is number one on the real-time search rankings.”

The inside of the Guild House went silent, as though everyone had been doused with ice water.

No one had expected anything like this. They all sat in silence, unable to find the words.

Then—

“Fwoosh-fwoosh-fwoosh-fwoosh! Ta-ta-ta-ta-ta!”

“Whoa.”

“No way.”

It was the same sound they had heard during Jin Taekyung’s interview only a few dozen seconds earlier.

The group hurriedly turned toward the television. They let out sighs when they saw that the cosmetics commercial was still playing.

But only for a moment.

“Wait. Then why can we still hear it?”

Team Leader Choi and Butler Kim were the first to realize where the noise was coming from. They shouted together.

“Outside!”

“It’s outside! It isn’t the television!”

Crash!

The moment they finished speaking, everyone sprang to their feet.

“Wow, what the hell?”

“Is this the right place?”

“Yeah, this is the Peace Guild. I heard they were remodeling, but it looks incredible.”

“Would it be possible to interview the guild members too?”

“No. You cut my interview short earlier.”

“Hunter, about earlier…”

The conversation came through the speaker spell with perfect clarity.

As the guild members watched, Team Leader Choi steadied his breathing and brought the message-magic Equipment to his mouth.

“Jin Taekyung. It’s me.”

“Whoa, what the hell? Sound Transmission? Is that Team Leader Choi?”

“Yes.”

“What was that? How did you do that?”

Team Leader Choi opened his mouth without hesitation.

It was an instinct etched deep into his bones.

“It’s nothing special. We commissioned the Vercheni family, a venerable Italian family of artisans, to make it especially for us…”

Im Kkeokjeong muttered a string of vicious curses under his breath.

* * *

*I went to sleep and woke up a star.*

I had never imagined I would experience that saying for real in my lifetime.

And not merely overnight. I was experiencing it in real time.

“Hey, sibling-on-paper. I just saw something I can’t believe.”

“Sibling-on-paper? Are you trying to die?”

“No, that’s not the issue right now.”

Hayeon’s voice on the other end of the phone was filled with shock and disbelief.

“Oppa, your name is on Naver’s real-time search…”

I could easily guess what she was about to say.

I had already received dozens of calls with similar questions over the past few hours.

I cut Hayeon off before she could continue.

“Number one on the real-time search rankings. Yeah, that’s me. It really is.”

“…Seriously? The Seoul Outer Ring Expressway tollgate hero? That’s you?”

“Don’t call me that. I’m dying of embarrassment.”

“Wow. I guess it really is you. When I tapped your name, your profile picture even came up under ‘Person in the News.’ Even after seeing that, I thought, *No way.*”

I had not expected it to cause such a huge reaction, either.

Only a few hours had passed, but if I searched my name online, dozens of clickbait articles came streaming out.

“What on earth happened? I read the articles, and it sounded insane. You’re not hurt, are you?”

“I didn’t even get a scratch, and it’d take too long to tell you the whole story. What about Mom? Has she heard the news about me?”

“Not yet. But if she finds out you fought monsters like that, she’ll faint.”

Hayeon was not exaggerating.

What kind of creature was an ogre?

Even someone who knew nothing about monsters could search a few times and learn that they were every bit as powerful as their grotesque appearance suggested.

I could already picture how Mom would react to hearing that her son had fought such monsters.

“Damn. You’re right about that.”

“Ugh, I don’t know. Come home before everything blows up and at least show her your face.”

“Okay. I’ll stop by after the interview.”

“Interview? Are you doing an interview right now?”

“Yeah.”

“Where? For a women’s magazine or something?”

“The KPS Nine O’Clock News Desk. I’m waiting for my turn.”

“…Holy crap.”

Just as I was about to answer Hayeon, a television-station producer weighed down with Equipment urgently waved at me.

“This is live, so I have to go. See you at home later.”

“Uh-huh? O-Okay…”

I hung up and walked toward the news studio I had only ever seen on television.

Broadcasting Equipment filled the room in every direction, and the eyes of the station staff were fixed on me. My lips went dry, and my legs trembled.

*I’d rather fight a hundred ogres.*

At a time when every second felt like an eternity, the signal I had been waiting for finally came.

“We’re going live. Stand by… cue!”

[^1]: Cesco is a Korean pest-control company.

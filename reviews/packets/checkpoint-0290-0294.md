# Checkpoint Review — 290–294

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

# Chapters 290–294

## Plot

Jin Taekyung uses Martial Arts Manual Creation to produce a manual for the Jin Family’s Cultivation Technique, disguising its origin as a family health regimen. He secretly teaches the technique to Team Leader Choi, Butler Kim, Song Song, and Im Kkeokjeong. During Choi’s instruction, Taekyung discovers a huge, mysterious mass of qi in Choi’s dantian. A Sudden Quest requires him to absorb only half of it; he consumes half while guiding the remainder, allowing Choi to complete his first circulation, become a martial artist, control his mana directly, and nearly double his reserves.

The absorption raises Taekyung’s internal energy to one hundred years, advances the Fire Gate Divine Technique to Seven Stars, grants him the title I’m a Master, and triggers a level-up. He nearly reaches Three Flowers Gather at the Crown but fails to enter the Supreme Peak realm for an unknown reason. Taekyung then guides all four core members through the technique; they learn the Small Circulation, with Im Kkeokjeong showing the greatest unexpected potential as a Second Awakener. Taekyung’s title changes from Trainee to Training Instructor.

During the following week, the Peace Guild completes a secret settlement with Lee Jungryong’s side, gaining exclusive rights to more than twenty Gates, real estate, and enormous compensation. Taekyung turns the Guild’s recruitment program into severe practical training, leading new Hunters through repeated Gate raids. In Black Wizard’s Black Forest, he lures a large undead force into the trainees’ formation. Three Skeleton Knights appear, two kneeling to the first, which transforms into a Level 105 Skeleton Warlord and orders the humans to descend.

## Continuity

- Taekyung can create manuals for martial arts at Great Completion through Martial Arts Manual Creation, but the skill requires physical materials and sufficient Intelligence.
- Taekyung has secretly taught the Jin Family’s Cultivation Technique to Team Leader Choi, Butler Kim, Song Song, and Im Kkeokjeong. All four completed an initial complete circulation and can perform the Small Circulation independently.
- Team Leader Choi is now a martial artist with greatly improved mana control and nearly twice his former mana reserves. The origin and remaining nature of the enormous qi mass in his dantian are unresolved.
- Im Kkeokjeong remains a D-rank Hunter recovering from his injuries, but his Second Awakening and rapid adaptation suggest exceptional potential. His return to field work and the effect of his reattached arms remain unresolved.
- Taekyung has one hundred years of internal energy, the Seven Stars Fire Gate Divine Technique, and the title I’m a Master. His attempted breakthrough into the Supreme Peak realm failed immediately before completion; the cause is unknown.
- The Peace Guild settlement provides more than twenty Gate monopolies, real estate, and substantial cash compensation. The Guild continues recruiting while accepting that Hunters may quit or transfer.
- Taekyung personally conducts harsh accelerated training raids. Kim Jinsoo leads the third-week trainees and serves as Taekyung’s trusted operational aide. Injuries have occurred, but no trainee has died.
- Two further Mutated Gate accidents occurred during the week after the cultivation training.
- Black Wizard’s Black Forest contains powerful undead and is associated with a black wizard or necromancer. The three Skeleton Knights and the Level 105 Skeleton Warlord are anomalous; the Warlord’s origin, allegiance, and purpose remain unknown.

## Translation Decisions

- Render **비급제작** as “Martial Arts Manual Creation,” **마나 연공법** as “Mana Cultivation Method,” **진기도인** as “True Qi Guidance,” **소주천** as “Small Circulation,” and **일주천** as “complete circulation.”
- Render **삼화취정** as “Three Flowers Gather at the Crown,” **내가고수** as “I’m a Master,” **칠 성** as “Seven Stars,” and **무아지경** as “Trance.”
- Render **수련자** as “Trainee” and **훈련 교관** as “Training Instructor” for System titles.
- Render **흑마법사의 검은 숲** as “Black Wizard’s Black Forest,” **골검** as “Bone Sword,” and **스켈레톤 워로드** as “Skeleton Warlord.”
- Render **도사견** as “Tosa mastiff,” **댕댕이** as “pup,” and **피리 부는 사나이** as “the Pied Piper.”

## Durable state

{
  "active_continuity": [
    "Jin Taekyung, Team Leader Choi, Butler Kim, Song Song, and Im Kkeokjeong remain committed to the Peace Guild despite its conflict with Ares Guild.",
    "The Peace Guild has received more than twenty Gate monopolies, real estate, and enormous cash compensation through negotiations with Lee Jungryong’s side.",
    "The Peace Guild continues recruiting and training Hunters through highly selective intake, unusually generous allowances, and exclusive rights to more than twenty Gates.",
    "Taekyung personally leads harsh accelerated training raids for new Peace Guild Hunters, using monster luring and formation drills to build their discipline.",
    "Kim Jinsoo is the informal leader of the third-week trainees and Taekyung’s trusted operational right hand during raids.",
    "Several recruits have quit the accelerated training or transferred to other teams; Taekyung regards continuing as their own choice.",
    "The A-rank Gate Black Wizard’s Black Forest is ruled by a black wizard or necromancer and contains powerful undead monsters.",
    "A group of three Skeleton Knights appeared in Black Wizard’s Black Forest; two submitted to the first, which transformed into a Level 105 Skeleton Warlord.",
    "Taekyung has completed repeated training raids without any trainee deaths so far, though injuries have occurred."
  ],
  "continuity_sources": [
    294
  ],
  "open_questions": [
    "Who actually taught Jin Taekyung the Jin Family’s Cultivation Technique?",
    "What history led Lee Jungryong to regard the unrelated Cheon Taemin as his older brother?",
    "How extensive are Ares Guild’s undisclosed forces beyond its officially registered Hunters?",
    "Will Im Kkeokjeong’s reattached arms and trauma recover sufficiently for him to return to Hunter work?",
    "What is the origin of the large qi mass in Team Leader Choi’s dantian?",
    "What prevented Taekyung from completing his breakthrough into the Supreme Peak realm?",
    "What is the origin and nature of the Skeleton Warlord that appeared in Black Wizard’s Black Forest?"
  ],
  "safe_through": 294,
  "temporary_decisions": [
    "Render 비급제작 as “Martial Arts Manual Creation.”",
    "Render 마나 연공법 as “Mana Cultivation Method.”",
    "Render 진기도인 as “True Qi Guidance,” 소주천 as “Small Circulation,” and 일주천 as “complete circulation.”",
    "Render 삼화취정 as “Three Flowers Gather at the Crown,” 무아지경 as “Trance,” 내가고수 as “I’m a Master,” and 칠 성 as “Seven Stars.”",
    "Render 수련자 as “Trainee” and 훈련 교관 as “Training Instructor.”",
    "Render 흑마법사의 검은 숲 as “Black Wizard’s Black Forest,” 도사견 as “Tosa mastiff,” and 댕댕이 as “pup.”"
  ],
  "version": 1
}

## Reading copies

## Chapter artifact 290

# Chapter 290

> **System**
>
> **Skill Window**
>
> **Martial Arts Manual Creation**
>
> **Grade:** None
>
> **Restriction:** Martial arts at Great Completion
>
> **Description:** The caster can create a martial arts manual only for martial arts they have achieved Great Completion in. If their understanding of the martial art is deep, they may produce an even better result.
>
> **Special Note:** Materials are required to create a martial arts manual.

I stared at the Skill information window and thought.

*Hold on. When did I get this?*

*Was it when I achieved Great Completion in the Jin Family's Manoeuvre Technique? Or the Jin Family's Spear Technique?*

It had been over a year, so my memory was hazy.

I had somehow received the Skill, but I had never used it even once because I had no opportunity to do so.

*No, that's not quite right. It wasn't that I had no opportunity. I just never intended to use it.*

Whenever I faced the members of Peace Guild after returning to the modern world, I occasionally felt the urge. But every time, I reached the same final conclusion.

*What kind of trouble would I get into if I leaked martial arts?*

Imagine one person fighting with bronze weapons when some idiot showed up with a steel sword and started hacking everyone apart.

Everyone would envy him, and they'd swarm him like a pack of dogs to get their hands on that steel sword.

It wasn't that I didn't trust the members of Peace Guild, but at least at the time, I thought it was the right decision.

*But there's no reason to hesitate anymore.*

After directly crossing blows with Lee Jungryong and his subordinates, Park Jihoon and Go Jun, I had realized that there were secrets in the modern world I knew nothing about.

Their movements and use of mana were clearly closer to those of Murim people. If the enemy was armed with steel swords, we needed to equip ourselves with something similar.

“Hoo…”

As I drew in a deep breath, the foul stench was sucked into my nostrils.

The place where I was squatting right now was a bathroom stall.

The environment was terrible, but it was the perfect place to avoid being seen while creating a martial arts manual.

*Then let's get started.*

I spread out the A4 paper and pen I had bought from the convenience store inside the hospital.

Then I muttered inwardly.

*Activate Martial Arts Manual Creation.*

Beep.

> **System**
>
> All materials are ready.
>
> The **Martial Arts Manual Creation** Skill is activated. You can create a martial arts manual for martial arts that have achieved Great Completion.
>
> **Currently available:** Jin Family's Cultivation Technique, Jin Family's Manoeuvre Technique, Jin Family's Spear Technique.
>
> Select the martial art you want.

None of the Fire Gate Clan's martial arts I had learned had reached Great Completion.

The Jin Family of Taiyuan's hereditary martial arts, on the other hand, were stable, and their power was just right.

Of those, I chose the most fundamental one.

*Select Jin Family's Cultivation Technique.*

Beep.

> **System**
>
> Create a martial arts manual for **Jin Family's Cultivation Technique**?
>
> **Y / N**

*Yes.*

Beep! Beep!

> **System**
>
> Intelligence insufficient! Brainpower insufficient!
>
> Teaching is several times more difficult than learning!
>
> To create a manual for a **Peak**-Grade martial art, you need at least 100 Intelligence!

“...You bastards. Seriously.”

With tears of blood streaming down my face, I opened my Status Window.

As I invested my precious points into Intelligence, the hand holding the pen began to race across the A4 paper like lightning.

Scritch-scritch-scritch-scritch!

“Gasp!”

I was surprised twice.

Once by that incredible speed, and a second time by the fact that everything being written was in Chinese.

“...”

Fuck, I can't work like this.

I began searching for the language settings.

* * *

Slide.

I entered the hospital room where the Peace Guild members were staying. The people who had been huddled together talking turned their heads toward me.

“Where did you go that took so long... Wait, did you go to the bathroom?”

At Song Song's words, spoken while she held her nose, I answered gloomily.

“How did you know?”

“The smell of shit was overwhelming.”

“Is it that bad?”

“Yeah. It felt like a giant turd was walking toward me.”

“Thanks for the kind words. I feel invigorated.”

After spending more than an hour inside a stinking bathroom stall, my nose had gone numb.

I answered in a completely drained voice and handed her the stack of A4 pages I had stapled together.

“Here.”

“What is this?”

“A love letter for you. I wrote it while having diarrhea.”

“Blech! Bleegh!”

“What a passionate reaction.”

“Bleeeggh!”

“...”

That wasn't a reaction. She was genuinely sick.

I thought things between us were already over, but I couldn't help the dull ache in a corner of my heart.

“I loved you...”

“Bleeeggh!”

“Hunter Song Song, are you all right?”

As her retching grew more violent, Butler Kim flew over to pat her on the back.

In the meantime, the A4 pages Song Song had been waving around like the Taegeukgi[^1] passed into someone else's hands.

After reading the words on the first page, Team Leader Choi let out a quiet laugh as he looked at me.

“Jin Family's Cultivation Technique? That's an unusual title for a love letter.”

“The contents are even more unusual.”

“...Pardon?”

“Keep reading.”

Team Leader Choi was quick on the uptake. He immediately straightened his posture and turned the pages with a solemn expression.

A pair of eyes moved busily over handwriting so mechanical that it was hard to believe I had written it myself.

Flip. Flip. Flip…

His pace grew faster and faster, and hot breaths escaped between his lips.

After rapidly reading through more than ten pages, he suddenly lifted his head. His eyes had widened like trays.

“This is...!”

His reaction surprised even me.

*He knows what this is?*

It was called a martial arts manual, but once I had actually created it, the manual for the Jin Family's Cultivation Technique looked enough like a book of traditional medicine that anyone unfamiliar with it might mistake it for one.

It showed the locations and functions of the countless acupoints in the human body, along with the paths used to circulate internal energy.

Song Song would have read a few pages and closed it, but Team Leader Choi's reaction was far beyond what I had expected.

“Do you recognize what this is?”

“Yes. Of course.”

Then a name I was hearing for the first time slipped between his lips.

“This is a Mana Cultivation Method.”

“A mana what?”

“A Mana Cultivation Method!”

*Mana Cultivation Method?*

What a bizarre name. Whoever came up with it had a strange naming sense.

At that moment, Butler Kim hurried over after hearing Team Leader Choi's raised voice.

“Did you just say Mana Cultivation Method?”

“Yes, here.”

Butler Kim took the manual from Team Leader Choi and frantically turned the pages.

Before long, he gave a similar reaction.

“Gasp.”

“What do you think, Butler Kim?”

“It’s certain. This is definitely a Mana Cultivation Method. But where on earth did you...?”

I got it from the bathroom.

Team Leader Choi raised a finger and pointed at me.

“Mr. Jin Taekyung...”

“Hunter Jin Taekyung?”

Whip! Crack!

Before Team Leader Choi could even finish speaking, Butler Kim's head snapped toward me with a violent sound.

“How does Hunter Jin Taekyung possess a Mana Cultivation Method?”

I answered calmly.

“For starters, I don't know what a Mana Cultivation Method is. Naturally, this is the first I've heard of this being one. By the way, is your neck all right? I think I just heard a bone break...”

“Is that important right now? This little neck of mine can break for all I care.”

“...It sounds pretty important to me.”

What do you mean, it can break? This old man seemed to be getting tougher by the day.

Of course, that only meant this matter was that important.

*So Lee Jungryong learned a Mana Cultivation Method.*

It had sounded strange at first because it was a kind of compound word, but after muttering it a few times, it rolled smoothly off my tongue.

It wasn't difficult to infer from the meaning of the word that this was the internal cultivation technique used by Hunters.

And that this was precisely what Lee Jungryong and his subordinates had learned.

“Could you answer my question, please?”

“Taekyung, this is an extremely important matter.”

Butler Kim and Team Leader Choi looked more serious than ever.

I rolled my eyes as if flustered, then gave them the answer I had prepared in advance.

“Well, my father taught it to me when I was young...”

“Pardon me, but are you referring to your late father?”

“Yes.”

Team Leader Choi furrowed his brow.

“I understand your late father was an ordinary man.”

“That’s right.”

“Then how did he know a Mana Cultivation Method...?”

“He probably didn't know either. When he taught it to me, he told me it was just a health regimen passed down through our family.”

“A health regimen?”

“A Mana Cultivation Method passed down through the family...”

I pointed at the cover as the two of them stared at me in disbelief.

Four neat characters were written on it in a font as orderly as that of an office document.

**Jin Family's Cultivation Technique**

The name was perfect.

If there was a Jin Family of Taiyuan in Shanxi Province, then there was a Jin Family of Goyang in Gyeonggi Province. That was all there was to it.

If I claimed it was a family heirloom passed down through the generations, they wouldn't have much to say.

Just as I had expected, both of them were briefly rendered speechless. I continued.

“It’s a kind of breathing method. My father taught it to me from a young age, saying it would make me healthier if I practiced it. He even made me memorize something called a formula.”

“It is similar to a Mana Cultivation Method, but...”

“Could we see the original? The original manual?”

“After my father passed away, I was too distracted by everything that happened... I looked for it after we moved, but it was gone.”

“Ah...”

“That’s unfortunate.”

“It is. Fortunately, I memorized every word of it.”

It was true that something I owned had disappeared. I had simply inserted the nonexistent original manual for the Jin Family's Cultivation Technique into the story.

Perfect destruction of evidence. When I said even the original was gone, I could see both of their shoulders droop.

*It would be interesting to see their faces if they knew this was the original.*

The martial arts manuals people imagined all looked more or less the same.

Half-rotted bamboo slips. Ancient books that smelled of rat urine.

Tell them to go play jokgu.[^2] I don't have any of that crap.

I stood the stiff stack of A4 paper neatly upright and slammed a stapler into it. Murim people would have been aghast, but a twenty-first-century martial arts manual had to look something like this.

“By the way, this is incredible. A cultivation technique... I never imagined something like this existed.”

“I’ve seen things like this mentioned a few times in novels and movies. I think they called them martial arts.”

“You are right, Young Master. In a way, a Mana Cultivation Method is also a form of martial arts. If you look here, it says that channeling circulates and accumulates qi, doesn’t it? This follows the same general principle as a Mana Cultivation Method...”

*Yeah, it is martial arts.*

While I held back the words itching to escape my mouth, Team Leader Choi asked,

“So, Mr. Jin Taekyung, you’ve been practicing Mana Cultivation Method—or rather, the Jin Family's Cultivation Technique—since you were young?”

“Yes.”

“I’m sorry to put it this way, but its effects seem to have been somewhat less impressive than expected...”

Translated directly, he was asking, *If you had this, why did you spend seven years as an F-rank Hunter?* It was a sharp question. And one I had expected.

I calmly opened my mouth.

“As you know, I was quite skilled for an F-rank Hunter. I even received a commendation as the top graduate of my training center.”

“Ah, yes. I’ve heard about that. I also know that you served as a deputy team leader at your former Guild.”

It had been a tiny, weak Guild, but F-rank Hunters were treated like punching bags wherever they went and like dog shit on the street.

Unless they were related by blood to the Guild's leadership, it was extremely rare for an F-rank Hunter to serve as a deputy team leader. That was why my appointment had been a subject of conversation within the Guild for quite some time.

“There was a lot of talk about it. People complained about seniority and all that, while Hunters with higher ranks and more experience than me grumbled about the pecking order... In the end, I proved myself through my ability. And the reason I was able to do that was the Jin Family's Cultivation Technique.”

“Hmm.”

“Looking at that, it does seem to have had an effect.”

I knew it. This alone wouldn't be enough to convince them of my past or the effectiveness of the Jin Family's Cultivation Technique.

I smiled faintly as I looked at the others. By then, Song Song had stopped retching, and even Im Kkeokjeong was watching my mouth with eyes full of curiosity.

[^1]: The Taegeukgi is South Korea’s national flag, commonly waved by hand at public events.
[^2]: *Jokgu* is Korean foot volleyball. Here, the phrase also works as a minced oath meaning “fuck off.”
## Chapter artifact 291

# Chapter 291

“Suppose you roll a snowball the size of your fist down a hill. What happens? Anyone know?”

Song Song snorted at my question.

“Even a kindergartener could answer that.”

“Then answer it.”

“It obviously gets bigger as it rolls downhill, doesn’t it?”

“Why?”

“Because it picks up the snow piled on the hill.”

“Yeah, just like my feelings for you.”

“Blegh! Bleeeggh!”

This was addictive.

Using Song Song’s renewed retching as background music, I continued.

“What Song-i just said is correct. But the premise is different here. This isn’t a snow-covered hill. It’s a hill where the snow has melted. No matter how hard you roll it all the way down there, the snowball won’t get much bigger.”

“The snowball you’re talking about is mana, then.”

“Team Leader Choi, you catch on fast. Yes, a Mana Cultivation Method works the same way. If what you start with is a speck of dust, it stays a speck of dust no matter how much you roll it.”

“The lower the rank, the lower the ceiling. Is that what you mean?”

“Exactly.”

There was a saying that once you were an F-rank, you were an F-rank forever.

That was how difficult it was to escape the rank you had been assigned.

But on extremely rare occasions, there were people who managed to pluck that star from the sky.

Second Awakeners. That was what they were called—and it was also the mask I was wearing at the moment.

“After awakening a second time as a C-rank Hunter, the effects increased dramatically. That was when a little snow finally began to pile up on the hill that had previously been nothing but grass.”

“Come to think of it, the results at the time were…”

“My mana reserves were C-rank. But even then, my control ability was A-rank. You know why, right?”

“The Jin Family’s Cultivation Technique.”

Team Leader Choi groaned.

“So it wasn’t a mistake on the Association’s part.”

As I became famous and my past actions came to light, that part was concluded to have been a measurement error.

As a result, the Bucheon Association, which had carried out the remeasurement at the time, took a considerable amount of abuse. From their perspective, it must have been deeply unfair.

“The Jin Family’s Cultivation Technique, which you and Butler Kim call a Mana Cultivation Method, has two effects. The first is an increase in mana. And the second is…”

Butler Kim picked up the thread.

“Mana control on an entirely different level.”

“Correct.”

Mana—or qi, as internal energy is called—could differ as greatly as heaven and earth depending on how it was used.

The Jin Family’s Cultivation Technique was a Peak martial art. It accumulated qi slowly, but its stability rivaled that of a Supreme Peak martial art.

“Just learning it should produce dramatic gains. We’ll keep an eye on the new recruits for now… For the time being, only those of you here should focus on learning the Jin Family’s Cultivation Technique. And of course, this must be done in absolute secrecy.”

“…”

“…”

What was with their reactions?

A heavy silence descended over the hospital room. Four people stared blankly at me with their mouths hanging open.

“Did you just say… you were going to teach us a Mana Cultivation Method?”

“Not a Mana Cultivation Method. The Jin Family’s Cultivation Technique.”

“Yes, yes. The Jin Family’s Cultivation Technique.”

Team Leader Choi’s eyelids trembled.

“You’re going to teach it to us?”

“That’s why I brought it, obviously. Did you think I brought it here just to show off?”

I looked around at everyone and continued.

“As you all know, we won’t last long at our current level. Lee Jungryong won’t come after us right away because of the recent incident, but it’s only a matter of time. But… what if we had the Jin Family’s Cultivation Technique?”

Im Kkeokjeong, who had been sitting with his mouth wide open, shouted.

“Jin! Family’s! Cultivation! Technique!”

“Ah, that’s a good reaction. In any case, this was a decision I made after careful consideration, so I’d like you to follow my instructions without complaint for the time being. Understood?”

The four people here were first up. Next would be the newly hired Hunters.

I would select them through a thorough screening process, then turn them into both Hunters and martial artists.

Elites who could comfortably handle two or three Hunters of the same rank.

“Well, then…”

I looked over the people who were still only half-present, one after another. Then I crooked a finger at one of them.

“Let’s start with Team Leader Choi.”

At that moment, a holographic window appeared over his face, which still looked stunned.

Ding.

> **System**
>
> A Quest, **Back, Back—Let’s See Your Back!**, has been generated!

“…”

That was a title that made me not want to do it for some reason.

* * *

> **System**
>
> **Quest**
>
> **Back, Back—Let’s See Your Back!**
>
> Unlike the Murim, modern life had been peaceful.
>
> But reality is a cesspool!
>
> Feeling a sense of crisis at this reality, you have decided to pass martial arts on to trustworthy friends.
>
> Whether this choice becomes a poison or a boon… depends on your choice and ability.
>
> May fortune in the martial arts be with you!
>
> **Grade:** Peak
>
> **Restriction:** Jin Taekyung
>
> **Mission:** Guide the learning of **Jin Family’s Cultivation Technique** *(Incomplete)*
>
> **Reward:** A considerable amount of EXP
>
> **Repeat Quest**
>
> **???**
>
> **Failure:** In the worst-case scenario, suffer **qi deviation**

“…”

Who the hell came up with this quest title?

I really did need to see his back, since I had to send internal energy into the Mingmen acupoint located in his lower back and teach him how to circulate it. But after seeing the title, I suddenly felt like I really, really didn’t want to do it.

“Whew. Team Leader Choi.”

“Yes.”

“Your back.”

“What?”

“Ah, never mind. Take the position I’m about to show you. Butler Kim and everyone else, guard the hospital room so no outsiders can enter. And above all, no one is to touch our bodies. Understood?”

“Of course.”

Butler Kim nodded firmly and cast a spell. Each time he waved his staff through the air along with the incantation, an invisible barrier spread around the hospital room.

In the meantime, Team Leader Choi removed his shirt, awkwardly sat cross-legged, and presented his back to me.

“What are you planning to do to me from here?”

“…You really know how to phrase things strangely.”

*I ought to give him qi deviation. Damn it.*

I placed my hand on Team Leader Choi’s Mingmen acupoint.

I had to be extremely careful from this point on. Even the most formidable Murim master was practically defenseless while circulating their qi.

“Now close your eyes and focus on the mana inside your body. Whatever happens, endure it. Is anything bothering you right now? If so, tell me now.”

“My right shoulder blade is a little…”

“Does it hurt?”

“It’s itchy.”

“…This is driving me crazy. Here?”

Scratch, scratch.

When I reached out and scratched it for him, Team Leader Choi’s voice became much more relaxed.

“Yes, right there. That feels wonderful.”

“They used to call me the Filial Son’s Hand.”[^1]

“And the area around my underwear is a little tight, so…”

“Are you crazy? You handle that part yourself. Did I put handcuffs on you?”

“Ah, so that was an option. I’m really tense right now.”

“Whew. It’s all right. I’m sorry I got worked up for no reason.”

“It isn’t your fault, Taekyung. If I’d known this was going to happen, I should have worn a thong.”

*Does this guy actually know his way around underwear…?*

I warned Team Leader Choi, who was blurting out anything that came to mind because he was nervous, in a low, level voice.

“From now on, if you open your mouth, you’re dead. Focus on only one thing: where and how the mana is flowing.”

“Understood.”

“Even if your shoulder blade itches, endure it. Even if something gets caught in your underwear, endure it. Do you understand?”

“May I ask what exactly we’re about to do?”

“I’m going to move your mana through True Qi Guidance. After that, I’ll perform a Small Circulation according to the formula of the Jin Family’s Cultivation Technique, then finish by circulating your qi and regulating your breathing.”

“…”

“Did you understand roughly? Be honest.”

“Be honest?”

“Yes.”

After a brief silence, Team Leader Choi answered.

“I don’t even know what True Qi Guidance is.”

“Then just close your eyes and shut your mouth. If you start wiggling your ass while saying things like, ‘Something’s caught in my underwear,’ I’ll kill you before I die.”

“I’ll keep that in mind.”

His answer was filled with resolve. I could feel Team Leader Choi’s body, which had been rigid with tension, gradually relaxing.

He was a novice taking his first step into the unfamiliar world of martial arts.

It didn’t matter how much social experience Team Leader Choi had accumulated, how many languages he spoke, or what kind of knowledge he possessed.

“Then we’ll begin.”

Everything depended on me now.

After steadying my breathing, I drew internal energy up from my dantian and sent it through my palm and into Team Leader Choi’s Mingmen acupoint.

Slowly. And carefully.

The moment the Scorching Yang Qi, imbued with Extreme Yang energy, entered his body, the System fired its signal flare as if it had been waiting for this.

Ding.

> **System**
>
> **True Qi Guidance** begins.

* * *

I had removed the waste accumulated inside Mom and Hayeon’s bodies once before.

But in terms of difficulty, the difference was like heaven and earth.

True Qi Guidance meant leading the energy inside another person’s body in whatever direction I wanted.

The mana Team Leader Choi possessed was abundant beyond anything an ordinary person could compare with.

*And cleaner than I expected.*

No, let me correct that. It wasn’t merely cleaner than expected. At this level, it was exceptionally clean.

His muscles and bones were sturdy, his sinews and meridians were strong, and his acupoints were as clear as a highway at dawn. There was hardly any waste inside him.

*What the hell? He said he hadn’t learned a Mana Cultivation Method.*

Team Leader Choi’s Hunter license was B-rank. The energy I usually sensed from him was exactly at that level.

If there was anything that set him apart from an ordinary B-rank Hunter, it was his combat sense, sharpened by his clever mind, and the power of expensive equipment.

*Honestly, for Cheon Taemin’s only blood descendant, there had always been something disappointing about him.*

Outstanding leadership. A sharp mind and the ability to make decisions.

And yet, he was inevitably underestimated.

In the presence of Cheon Taemin, the hero who had saved all of humanity, anyone’s color was bound to fade.

But now I had changed my mind a little.

*At this level… with a little help, he could reach a higher realm in no time.*

An A-rank Hunter? No. I intended to turn Team Leader Choi into a Peak master. His basic hardware was too good to leave to rot like this.

*If the others were even half as capable as Team Leader Choi, things would be much easier.*

With that carefree thought, I sent the Scorching Yang Qi flowing through him. Before long, more than one jiazi’s worth of internal energy began to wind its way through his body.

Whoosh!

I felt the body beneath my palm twitch.

By now, he was probably experiencing heat unlike anything he had ever felt before.

I ignored it and gathered the energy scattered throughout his body, driving it through dozens of acupoints.

Team Leader Choi had to remember this. From now on, he would have to travel this path on his own thousands, tens of thousands of times.

*Once the body remembers it, the rest is easy.*

His progress was astonishingly fast.

Before long, the energy I was guiding had reached half a jiazi, and the little waste that remained was cleanly destroyed by the heat of the Scorching Yang Qi.

*Now for the last step.*

I had gathered the scattered energy. It was time to store it in the dantian. Once that was done, a complete circulation would be achieved, and he could be said to have taken his first step as a martial artist.

But then…

*What the hell is that?*

When I reached Team Leader Choi’s dantian, I stopped dead.

A massive mass of qi occupied half of his dantian.

And then came the System notification.

Ding.

> **System**
>
> A Sudden Quest, **I’ll Take Only Half the Internal Energy I Digest.**, has been generated.
>
> Will you accept it?
>
> **Y** / **N**

[^1]: The Korean term *hyojason* means a back-scratcher and literally translates as “filial son’s hand.”
## Chapter artifact 292

# Chapter 292

Ding.

> **System**
>
> A Sudden Quest, **I’ll Take Only Half the Internal Energy I Digest.**, has been generated.
>
> Will you accept it?
>
> **Y** / **N**
>
Damn it. Why now?

I was dying to check the Quest window.

But I was in the middle of True Qi Guidance. Circulating my own qi would be one thing, but if I let go of control here, I could easily suffer an Internal Injury.

> **System**
>
> - If you do not answer within five seconds, the Quest will be canceled automatically.
>
> - Five, four, three…

*Do I go for it or not?*

The Quest title made it sound as though I was supposed to try touching that thing in Team Leader Choi’s dantian. Even at a glance, it contained well over one jiazi’s worth of energy.

> - Two, one…

*Fuck it. I don’t know. It’s not like I’m going to die.*

*Accept!*

Ding.

That had been close. Along with the notification that the Quest had been accepted, I realized what I had to do.

> **System**
>
> The mysterious qi has been dormant for a long time, and its owner lacks the power to control it. Now is the time for you to step forward!

*Just as I thought.*

I had experienced a situation like this once before in the Murim.

I dug up an old memory.

*Snow ginseng.*

From the moment I first opened my eyes in the Murim, the internal energy of a hundred-year-old snow ginseng had been curled up inside my dantian.

It was internal energy that the Third Rate wastrel Jin Taekyung—not me—had been unable to fully digest.

That was when I first learned that even if you consumed an elixir, you couldn’t make it your own if you lacked the ability to digest it.

*Just like Team Leader Choi now.*

Compared to a Third Rate wastrel, he was an outstanding talent. But Team Leader Choi didn’t know a Mana Cultivation Method, and therefore lacked the ability to control the massive energy equivalent to more than one jiazi.

The Quest had assigned me the role of a digestive aid.

*But how does Team Leader Choi have that much energy in the first place?*

Now that I thought about it, it pissed me off.

I had crawled through hell in the Murim, pushing myself like a dog, and had only barely accumulated a little more than one jiazi. Meanwhile, what had this guy done to have such monstrous energy stored in his dantian?

*Ah, right. His maternal grandfather was Cheon Taemin.*

Was this what they meant by being born with a hero’s silver spoon?

I gave up on thinking about it. Right now, I needed to focus on tackling that mysterious energy whose origins I couldn’t identify.

And this time, I was confident.

*Shall we?*

A bolt of Scorching Yang Qi shot forward like a spear and plunged into the solid mass of qi. A combined total of more than two jiazi’s worth of qi collided and tore into each other.

Rumble.

As the clash erupted inside his dantian, Team Leader Choi’s body began to shake violently.

* * *

The hospital room had become an impregnable fortress that no one could enter.

Butler Kim, Im Kkeokjeong, and Song Song watched the two young men with fascinated expressions.

“Hngh.”

“Hup.”

“Ugh.”

“Kk.”

Every time the veins bulged on Jin Taekyung’s forearm, Team Leader Choi’s body trembled.

Before long, his back arched, and a groan escaped through his clenched teeth.

“Haaagh!”

Watching the scene, Song Song muttered,

“His back arched like a bow…”

Im Kkeokjeong, who was lying on the bed, asked,

“What did you just say, Miss Song?”

“Nothing. I was just saying it was disgusting and fascinating.”

“Ah, you mean that black sweat?”

“…Yes.”

Song Song had a lot she wanted to say, but she held it in and nodded.

The black sweat pouring from Team Leader Choi’s entire body was just as disgusting and fascinating.

“My God, what is that supposed to be?”

As a Hunter, you saw all kinds of things. But this was the first time she had ever seen someone sweat black.

It was pitch-black and sticky. There wasn’t much of it, but it gave off an unbelievable stench.

“Ugh, it stinks.”

“Damn, that smell is awful.”

Just as the two of them covered their noses, Butler Kim spoke.

“That is waste that had accumulated inside his body being expelled through his sweat. It is one of the effects of a Mana Cultivation Method.”

“Waste?”

“Kim hyung, is that really so impressive?”

“Of course. Even healing magic cannot remove waste from inside the body.”

Song Song thought for a moment before answering.

“It’s possible. If you have a truly top-tier healer. But if what you’re saying is true… that’s amazing. Even the potions used for treatment retain a trace of Troll toxicity, so you’re saying this can wash even that away.”

“That is one of the remarkable aspects of a Mana Cultivation Method.”

“Who exactly created this Mana Cultivation Method, and how?”

Song Song had considerable experience as a Hunter, but she had never heard the term *Mana Cultivation Method* before. Im Kkeokjeong, who had been a Hunter for twenty years, found it just as unfamiliar.

“Exactly. I’ve spent my whole life as a Hunter, and this is the first I’ve heard of some kind of martial art—or sorcery, or whatever you want to call it.”

“During the Great Cataclysm, the Elder created the first Mana Cultivation Method. It has been treated as such a closely guarded secret that it is only natural for the two of you not to know about it.”

“When you say the Elder…”

“You are thinking of the right person.”

Cheon Taemin. The hero who had saved all of humanity, and the greatest Hunter in the world.

Butler Kim continued slowly.

“A Mana Cultivation Method is a powerful weapon in its own right. Many incidents have occurred because of it, and most of them have vanished from history. It truly was an age worthy of being called a cataclysm.”

What had happened? Why had Cheon Taemin’s Mana Cultivation Method fallen into the hands of an ambitious man like Lee Jungryong instead of his only flesh and blood?

Song Song and Im Kkeokjeong had many more questions, but they fell silent.

It wasn’t only because Butler Kim’s expression had become unbearably bitter. Something extraordinary happened at the very moment he finished speaking.

“Nggh!”

“Hup!”

Jin Taekyung and Team Leader Choi groaned at the same time.

Thick veins bulged across their exposed skin, and deep furrows formed between their brows.

Team Leader Choi’s reaction grew increasingly violent. His entire body trembled as if an earthquake were shaking it.

“Team Leader Choi!”

“Is something seriously wrong?”

Song Song and Im Kkeokjeong took an involuntary step forward, but Butler Kim reached out and stopped them.

“No. There can be no physical contact while practicing a Mana Cultivation Method.”

“But…”

“Hunter Jin Taekyung is not someone who would put the Young Master in danger.”

Butler Kim looked at the two of them with eyes filled with both concern and trust.

The trembling and pained groans grew stronger.

Before long, his faith became reality.

“Haaah…”

At some point, Team Leader Choi’s lips parted, and a calm breath escaped him.

It was the sign that his first complete circulation had just ended. It also meant that he had become a martial artist who had learned the Jin Family’s Cultivation Technique.

“Young Master?”

At Butler Kim’s call, the eyes that had been closed slowly opened. His pupils were filled with astonishment and joy.

“This is…”

Team Leader Choi—Choi Minwoo—clenched his fists tightly.

The massive energy surging from his dantian raced through him without resistance.

Normally, his mana should have been scattered throughout his body. Now he could move it freely.

Not only that, but the amount of mana he possessed had nearly doubled.

*So this is a Mana Cultivation Method.*

As Choi Minwoo calmly examined his condition, he reconsidered.

*No. It isn’t the power of a Mana Cultivation Method. It’s the power of the Jin Family’s Cultivation Technique.*

And it had only been possible because of one person’s ability.

“Mr. Jin.”

Choi Minwoo slowly turned around. Jin Taekyung was still sitting with his eyes closed, taking deep breaths.

He could feel the air trembling around him. There was an active volcano there, ready to explode at any moment.

*He’s strong. Impossibly strong.*

*Was he always this strong?*

Now that he could properly control his mana, Choi Minwoo could catch the faintest glimpse of Jin Taekyung’s power.

Every time Jin Taekyung exhaled, waves of fire qi poured out and heated the hospital room.

It was November. A week had passed since the first snow, yet people began to feel thirsty, and heat haze rose from the floor.

Just then, Choi Minwoo’s eyes slowly widened.

*What… is that?*

Was it an illusion created by the heat haze? Or was it real?

He didn’t know. Before he realized it, everyone in the hospital room was staring at the scene before them with their mouths hanging open.

Ssshhk.

Jin Taekyung, sitting cross-legged, was rising into the air.

Little by little. Slowly, without stopping.

Above his head, blazing blue flames formed the shape of flower petals.

One flower. Then two.

And just as the final, third flower was about to be completed, Jin Taekyung’s eyes flew open.

Whoosh! Thud!

Like a bird struck by an arrow, Jin Taekyung fell helplessly and slammed his butt onto the floor. A scream tore from his throat.

“Fuck! My tailbone!”

The air in the hospital room froze solid.

* * *

I screamed at the top of my lungs.

“Aaaargh!”

It hurt. My tailbone hurt from slamming into the floor, but my heart hurt ten times more from losing the perfect opportunity.

“It was almost done! It was done!”

Damn it. With only one step left, the Supreme Peak realm had slipped far away.

I didn’t know whether it was because I lacked sufficient depth in martial arts or because there was some other reason.

Maybe it was both. But the important thing was that I had no idea when another opportunity like this would come.

“Damn iiiit!”

I could have achieved Three Flowers Gather at the Crown in one stroke and become a Supreme Peak master!

As I pounded the floor and wailed, System notifications pierced my ears.

Ding. Ding. Ding.

> **System**
>
> - **Trance** has been dispelled!
>
> - **Internal energy** has risen to 100 years!
>
> - You have achieved a great feat! You have acquired the Title **I’m a Master**!
>
> - The Sudden Quest, **I’ll Take Only Half the Internal Energy I Digest.**, has been successfully completed!
>
> - The Repeat Quest, **Back, Back—Let’s See Your Back!**, has been successfully completed!
>
> - The realm of **Fire Gate Divine Technique** has risen to **Seven Stars**!
>
> - You have acquired a massive amount of EXP!
>
> - **Level Up!**
>
> …
>
> …
>
> …

“Leave me alone!”

Everything had been perfect. While melting the energy that had been solidified in Team Leader Choi’s dantian, I had absorbed half of it. My mind had gone blank, and I had momentarily slipped into a trance.

But…

“Why! Why can’t I be happy!”

Gaining nearly half a jiazi’s worth of internal energy? Great!

Acquiring a Title, completing Quests, raising the realm of the Fire Gate Divine Technique by one stage, and even leveling up—all of it was great. It was all good, so why!

“Why didn’t I reach the Supreme Peak realm!”

As I howled toward the ceiling, whispers reached my ears.

“What happened to Mr. Jin?”

“I’m not sure, but I heard that some people end up crippled while practicing a Mana Cultivation Method…”

“More importantly, did everyone see those flower petals just now? Was I the only one? Why is nobody saying anything?”

“Song-i, did you see them too? I thought I was at the Goyang flower exhibition.”

Hearing the worried and astonished voices, I suddenly came to my senses.

That’s right. It wasn’t over yet. If those three had even half as much as Team Leader Choi, I might still have a chance to advance to the Supreme Peak realm.

*I still have three test subjects.*

I spoke with the same resolve Admiral Yi Sun-sin had before the Battle of Myeongnyang.[^1]

“Everyone, pay attention.”

“...?”

“...?”

“...?”

“Take off your tops immediately. Do it.”

Ding.

> **System**
>
> - The Repeat Quest, **Back, Back—Let’s See Your Back!**, has been generated!

“Back, back—let’s see your back!”

The others retreated step by step, their faces pale with fear.

[^1]: The Battle of Myeongnyang was Admiral Yi Sun-sin’s famous 1597 naval victory, achieved against overwhelming odds.
## Chapter artifact 293

# Chapter 293

Ssshhk. Hoooh.

Only the quiet sounds of breathing drifted through the hospital room. Standing across the doorway, I watched the people absorbed in circulating their qi.

Their cross-legged postures, awkward at first, were gradually starting to look more natural.

*Not bad.*

Team Leader Choi, Butler Kim, Song Song, and finally Im Kkeokjeong.

Before sunset, all four had succeeded in completing a complete circulation. Before long, they were able to perform the Small Circulation on their own.

*Not bad for a first step. No, this is better than I expected.*

None of the others possessed energy as vast as Team Leader Choi’s, but Kim and Song Song were mages, so they were skilled at handling mana and adapted quickly.

But the person who showed the most unexpected performance was someone else.

Im Kkeokjeong.

*I thought he’d struggle for a long time…*

I’d forgotten something. Im Kkeokjeong was the only Second Awakener among everyone I knew. Was it the result of blood-soaked effort? Or heavenly luck?

Whatever the reason, Im Kkeokjeong had already once broken past the limits given to him.

*So there was a reason he underwent a Second Awakening?*

Judging by what he had shown me, Im Kkeokjeong might be the person with the greatest room for growth.

He was still a D-rank Hunter. He had plenty of steps left to climb.

*I won’t have to worry about the aftereffects of his injuries, either.*

Repeatedly circulating his qi would naturally improve his Muscles and Bones and Sinews and Meridians.

If Im Kkeokjeong could overcome the psychological issues, such as his trauma, he would be able to return to the Guild before long.

And then…

*The Guild will have changed quite a bit by then, too.*

The changes had already begun. Lee Jungryong had already turned the knife hidden up his sleeve against us, and now he was in a position where he had to pay us the price.

With that compensation, the Peace Guild would achieve dazzling growth. These people needed to be at the forefront of it.

Someone would have to run the Guild, while someone else would have to select talented and trustworthy people and turn them into loyal servants of the Peace Guild.

And those people would be given martial arts.

*We need blades, too.*

The moment I thought that, Team Leader Choi finished his Small Circulation and opened his eyes with an exhale. A sharp glint flashed across his pupils.

Starting with him, the others began opening their eyes one after another.

Ding.

> **System**
>
> Thanks to your excellent instruction, several people have reached One Star in the **Jin Family’s Cultivation Technique**.
>
> - The Title **Trainee** has changed to **Training Instructor**!

A martial arts drill instructor, huh.

Was heaven telling me to work them to death for a while?

I looked at the people still immersed in the aftereffects of circulating their qi and grinned.

* * *

A week passed in the blink of an eye.

During that time, Lee Jungryong and the Peace Guild secretly completed their negotiations. Two more mutated Gate accidents occurred, and a post that attracted a great deal of attention appeared on a Hunter community site.

**Peace Guild Final Acceptance Review**

I’m a C-rank Hunter who used to work on a Guild Security Team.

I was originally with a major Guild, but my senior coworker was such a pain in the ass (he’s a traitor to the country) that the stress got too bad. I quit a few days ago and was browsing job sites when I saw that the Peace Guild had opened its general recruitment. So I applied on a whim, you know?

Then I didn’t hear anything back, so I figured I’d been rejected.

I already knew their selection process was brutal, so I wasn’t expecting anything in the first place.

But they contacted me after two weeks and told me to report to work tomorrow!

Anyone else joining with me tomorrow, raise your hand!

**(Best comment)** You got accepted after only submitting an application to the Peace Guild? Hahahahahaha. Some unemployed bastard is sitting there writing a web novel.

└ ???: Big bro. This guy’s laughing.

└ ???: Leave him alone. He must be dreaming about joining the Peace Guild.

└ That ending.

└ The OP is seriously an idiot. If you’re going to write fiction, at least make it believable. The Peace Guild rejected people from the first team of major Guilds, but a C-rank Security Team guy submits an application and gets accepted? Hahaha. I’m leaving after having a good laugh.

└ Is it really that brutal?

└ I actually applied this time, and the competition is 47:1. They even made us take a personality and aptitude test before the interview.

└ What the hell? A personality and aptitude test? Is this high school?

└ Proof that the Peace Guild thinks Hunters are a bunch of weaklings.

└ On the other hand, their basic allowance and incentives are incomparably higher than anywhere else.

└ Please think I’m a weakling.

└ Come to think of it, the Peace Guild must have solid finances. People are transferring over from major Guilds.

└ Exactly. I heard they have exclusive rights to more than twenty Gates alone.

└ **(OP)** I’m the person who wrote the post. I just called the HR department, and they said they hired me because Jin Taekyung told them to.

└ Hahahaha. How would Lord Fuck know an unemployed loser like you well enough to hire you? Stop writing fiction and go to sleep.

└ Thanks for the web novel. I enjoyed it.

└ By the way, are there any web novels worth reading these days?

└ I recommend *Login Murim*. It’s pretty good if you can get through the early modern-world chapters.

└ Welcome, Zerobic.

└ That author has been serializing for ten years and has never once done a bulk update.

Under normal circumstances, it would have been dismissed as the nonsense of an attention seeker.

However, the post proudly took first place in the weekly rankings, accompanied by countless recommendations and comments from people making a pilgrimage to the site.

That was because of another post uploaded the following evening.

**Guys, that web-novel villain from yesterday was for real;**

I’m one of the people who got accepted by the Peace Guild this time. Today, I was touring the Guild house with the other new hires when I saw Lord Fuck, you know?

I was just watching him from a distance, terrified by the majesty of him dragging around slippers with the soles torn off, when he suddenly made a U-turn, grabbed one of us, and asked if he was from the \*\* Guild Security Team.

When the dopey-looking guy said yes, Lord Fuck laughed like a maniac, went, “Irasshaimase!” and all that shit, then walked away.

I knew Lord Fuck had a weird personality, but he seems to be an even bigger lunatic than I imagined.

*(Photo attached.)*

I’m posting all the proof so you won’t think I’m lying.

**(Best comment)** I’m the person who got the best comment last time. In apology, I’m going to perform a full-body prostration and leave.

└ Looking at the verification photo, this really seems to be true…?

└ Wait, what? How does a C-rank Hunter from a Security Team end up at the Peace Guild?

└ It actually happened…

└ **(OP)** The web-novel villain was assigned to the Security Team instead of a raid team.

└ Oh, then it’s possible. At that level, it isn’t a parachute appointment so much as an ordinary job transfer.

└ They say Korea runs on blood ties, regional ties, and school ties. It can’t be helped—he’s only human—but I’m a little disappointed in Lord Fuck.

└ Who are you to be disappointed?

└ The reason the idiots bashing Lord Fuck right now are idiots: Lord Fuck, who walks around in slippers with the soles torn off, donated nearly his entire fortune to a foundation for Gate victims.

└ The comment above is a fact. Anyone insulting Lord Fuck needs to be beaten half to death with slippers before they come to their senses.

└ You keep doing favors, and they take you for Dooly.[^1]

But where did the OP go? Tell us more of the story.

└ **(OP)** I’m on my way to a company dinner.

└ A welcome party for the new hires?

└ **(OP)** Yeah. I’ve been in the car for an hour already. We must be going somewhere far away.

└ Oh. Is Lord Fuck coming too?

└ **(OP)** Yeah. But I don’t see the Guild Master or the other Team Leaders.

└ The Peace Guild must be good at team building. Maybe it’s because they’re still a new Guild?

└ **(OP)** I’m not sure about that, but… the atmosphere feels kind of bad. I asked a Senior who joined earlier than me, and he told me to sleep as much as I could on the way there.

└ Why?

└ Maybe the company dinner is going to last a long time. Who likes drinking with people they aren’t even close to?

└ **(OP)** Is that it? Oh, I guess we’re here.

└ Don’t drink too much. Don’t forget to bring us the rest of the story later.

└ Have a good time!

└ **(OP)** It looks like a good restaurant. I’m looking forward to seeing what we’re having for dinner, haha. I’ll be back soon.

And that was the OP’s final comment.

* * *

“We’re having dinner at a Gate.”

Murmurs rose from all around at my declaration.

“Excuse me?”

“Huh?”

“Sorry, but did I hear you correctly?”

“I think you said we’re having dinner at a Gate. I must have misheard.”

“Ah, yes.”

I didn’t even need to look at their faces to know. The people having that innocent conversation were new hires on their first day.

The people who had joined only two or three weeks earlier, however, were different.

“I knew this would happen.”

“Fuck…”

“Good thing I brought potions.”

“Big bro, do you have any arrows left?”

“Yeah. I brought another two hundred as emergency spares, just in case.”

“Then could I get a hundred?”

They had less than a month’s difference in their employment dates, but their reactions were worlds apart.

After tossing out a string of curses like sighs, they swiftly pulled armor and equipment from the backpacks they had been carrying.

Clack! Clack! Clack!

Was this what a teacher felt like?

The effects of repetitive learning filled me with satisfaction, and a pleased smile spread across my face.

I turned toward the greenhorns who still had no idea what was happening and asked,

“You all brought all your luggage, right?”

The new hires nodded.

“Ah, yes. You told us to bring it, so…”

“Put it down, take out your equipment, and put it on.”

“Excuse me? Is this some kind of mock battle?”

“What mock battle? You don’t improve much doing that. Real combat is best.”

“...?”

Suspicion crept into their innocent eyes.

“Then, perhaps…”

“Are we really going to a Gate?”

“Yes. A raid to celebrate joining the Peace Guild! What do you think? Nice, right?”

“...”

“The new people don’t seem to like it much. What do the rest of you think?”

The people who had already been worked to the bone for the past few weeks gritted their teeth and shouted.

“That’s a wonderful idea!”

“As expected of King Taekyung.”

“Wow. This. Is. Great!”

Hmm. Just as I thought.

This was also the effect of learning. They clearly remembered what had happened to the few brave souls who had openly contradicted my opinions.

The logic of *I can’t be the only one who suffers* must have played a part, too.

*Right. Everyone should suffer together.*

If the new hires were Pomeranians, the others were already Tosa mastiffs.

With the atmosphere blazing with the determination to die together, the new hires hesitated before shouting,

“B-But we weren’t told this! The notice said that only a simple workshop would be held during the first week after joining the Guild…”

“Yes. What we’re about to do is the workshop.”

“What Guild holds a workshop at a Gate? For an entire week?”

“The Peace Guild.”

“That’s impossible!”

“Do the others think so, too?”

I turned my head slightly. The Senior Tosa mastiffs who had tasted hell for several weeks bared their teeth and shouted.

“Why wouldn’t it make sense? It does! Absolutely!”

“Of course this is a workshop!”

“Who rents a vacation house for a workshop these days? You’re supposed to grow closer by killing monsters together at a Gate!”

“We can’t be the only ones getting screwed!”

That last shout was so blatant that it bordered on desperation. Hearing it made me deeply reflect on things.

*I guess I need to work them even harder.*

They couldn’t be allowed to think of this as suffering. I planned to condition—or rather, train—them until they accepted every bit of this as natural and ordinary.

“Now, everyone quiet!”

Ding.

> **System**
>
> - The effect of the Title **Training Instructor** activates!
>
> - The trainees who heard your shout become tense!

“Form ranks!”

“Form raaanks!”

“Too quiet. Form ranks!”

“Form raaanks!”

Even after repeating the command back in unison, they all looked dazed.

I smiled at their sour faces.

“Now, follow me inside one at a time. Left foot. Left foot.”

Clack! Clack! Clack!

A human train set off toward the Gate.

[^1]: A pun on *houi* (“goodwill”) and Dooly’s catchphrase, “Hoi!” The original saying means that repeated goodwill gets mistaken for an entitlement.
## Chapter artifact 294

# Chapter 294

A week ago, after several days of tenacious negotiations with Lee Jungryong’s side, Team Leader Choi got everything he wanted.

Exclusive rights to more than twenty Gates, real estate, and an enormous amount of cash. I didn’t know the exact figure, but its value was clearly astronomical.

They were valuable spoils we could never have obtained if the ten Black Hunters and the close aides dispatched by Myeongdong Guild Master Park Tae Seop hadn’t fallen into our hands.

*This place was no different.*

I shouted out commands as I passed through the mana field first.

Ssshhhk.

With that sticky, unpleasant, yet familiar sensation unique to mana, everything surrounding me changed.

Ding.

> **System**
>
> You have entered the A-rank Gate, **Black Wizard’s Black Forest**!
>
> Quest **Gate Raid** has been automatically generated!

“Left foot, left foot! One, two, three, four! Halt!”

“One, two! Fall in!”

By the time the human train came to a stop amid crisp call-and-response, more than fifty people had entered the Gate.

Darkness had settled over the forest, and faint moonlight filtered through the gaunt branches.

The new hires who realized what was happening too late looked around in panic.

“Gasp!”

“W-We’re screwed.”

“Wait a second. What rank is this Gate for it to be this huge?”

The third-week Tosa mastiffs, on the other hand, were completely calm.

“Black Wizard’s Black Forest again?”

“Ugh, I’m going to puke.”

“Good thing I brought my war hammer.”

They had joined less than a month apart, but the difference between them was enormous.

The day-one pups listening to the Tosa mastiffs turned pale.

“B-Black Wizard’s Black Forest?”

“It’s an A-rank Gate!”

An A-rank Gate: Black Wizard’s Black Forest.

Even people who knew nothing about this place could get a rough idea from its name alone. The eerie atmosphere and the forest scenery that sent chills down your spine just by looking at it.

This was a realm ruled by a black wizard—a necromancer.

“Lord Fuck! Senior Jin Taekyung!”

One of the pups hurried over and spoke with an earnest expression.

“Please, can’t you let me out?”

“Why?”

“I’m really scared of ghosts. Regular monsters are fine, but ghouls and skeletons… I don’t think I can handle those.”

“Trauma?”

“Not to that extent. I’m just scared.”

“Perfect. This is a good chance to experience the full 4D version. They’re monsters, anyway.”

“No, it’s just…”

“And I’m pretty sure you wrote on your Guild application that you didn’t have any problems like that.”

“I only wrote that so I’d get accepted in the first place… Please. I can’t even watch horror movies with my girlfriend.”

“Oh, you have a girlfriend. I see. Over here!”

I crooked a finger.

One of the people standing among the Tosa mastiffs, all of whom were watching me with sly grins, shot forward like a bullet.

“Did you call for me?”

“Yeah.”

It was Kim Jinsoo, who had quietly taken on the role of leader among the Tosa mastiffs.

He had a certain amount of leadership and excellent combat ability, so whenever we raided together, he acted as my hands and feet.

Of course, I’d started speaking casually to him long ago.

“I have a separate instruction for you. It concerns this person here.”

“Yes.”

“Put him at the front.”

The pup, who had been sighing in relief, swallowed hard.

“D-Did you say the front?”

“Why? Is there a problem? Judging by that tower shield, you’re clearly a tank.”

“But…”

“If you want to sit out, go ahead. Just be prepared to get fired.”

“F-Fired?”

“If you refuse to raid because you’re afraid of ghosts, why would I have any reason to employ you? And are there ghosts in a Gate? They’re all monsters. Jinsoo, am I wrong?”

Kim Jinsoo answered immediately.

“You are absolutely right—a hundred, a thousand times over.”

“If all the things here were ghosts, why would I bring Hunters? I’d bring exorcists instead. Isn’t that right?”

“Absolutely right—a thousand, ten thousand times over.”

“As expected of Jinsoo. You really know how to put things nicely.”

“Thank you.”

“So, will you continue being a Hunter for the Peace Guild, or will you get fired and switch careers to become an exorcist?”

The pup replied, his face rigid.

“I-I’ll be a Hunter.”

“Then if you run away during combat, I’ll send you to heaven with my own hands. Okay?”

“O-Okay.”

“Okay. Front! Okay! Heaven!”

I waved my hand, and Kim Jinsoo grabbed the man by the arm and dragged him away.

We’d gone through a fairly meticulous selection process to pick these people, but no matter where you went, there was always one guy like that mixed in.

*What? He’s so scared of ghosts that he can’t even watch a horror movie with his girlfriend?*

Damn it. What a load of bullshit.

I wasn’t angry about the girlfriend part. Really.

“…”

Whooosh.

The eerie wind circling through the forest made the empty space at my side feel cold. I shuddered once, then stepped toward the trees.

I could hear the conversation gradually fading behind me.

“E-Excuse me, mister.”

The frightened voice of one of the pups mixed with the Tosa mastiff’s blunt reply.

“What?”

“Where is Hunter Jin Taekyung going?”

“He’s going on a drive hunt.”

“A what?”

“That guy’s nickname is the Pied Piper.”

The Tosa mastiff added in a cheerful voice,

“I can’t be the only one going through hell. Let’s do our best together.”

“…”

* * *

I made my way around the forest, making enough noise for them to hear me, and the effect appeared almost immediately.

Crack! Rumble!

- Guaaaar!

- Ngh… nghhh…

Click, clack, clatter-clatter-clatter!

With grotesque cries, corpses sleeping beneath the ground and in their graves began to awaken.

Ghouls that shed rotting flesh with every movement. Skeletons whose flesh had completely disappeared, exposing their gaunt white bones.

The cursed dead known as Undead Monsters covered the forest and hills in an instant.

“Hey, hey! I’m going slowly, so make sure you keep up! Got it?”

- Guaaaaaar!

Rat-tat-tat-tat!

The image of zombies dragging their limp bodies around with a stagger had become outdated.

Whenever I saw these bastards running, I wondered if they had come from the national athletes’ training center. It had happened more than once or twice.

Of course, they still weren’t fast enough to catch me.

*There are new hires today, too, so I should bring back a smaller group.*

I sprinted forward, checking their numbers with occasional glances over my shoulder.

There were roughly a hundred and fifty of them.

That was three times the number of people on our side, but even this was fewer than usual.

For one thing, ghouls and skeletons weren’t particularly powerful monsters. For another, our side had gained thorough preparation and plenty of nerve.

*There’s a reason they call them Tosa mastiffs.*

After dragging along monsters that outnumbered them three to one as a matter of course—and sometimes more than ten to one—and showing them the gates of hell several times, their eyes had begun to brim with fierce determination.

Of course, whenever things seemed genuinely dangerous, I stepped in from time to time even if I had been watching from the sidelines. Thanks to that, we had suffered injuries, but there had been no deaths.

After repeating that several times a day, I had become both their common enemy and someone they trusted.

*I don’t want to go this far, but… it can’t be helped.*

This was an accelerated crash course. I needed to plant weeds that could survive in harsh conditions in the Peace Guild’s yard as quickly as possible.

In less than a month, several people had already announced that they were quitting and moved to other teams. I hadn’t bothered to stop them, and I didn’t feel disappointed, either.

*The decision is theirs to make.*

Everyone had a life of their own. I had only stepped into their lives for a little while.

I could present them with choices, but I had no right to force them to choose.

Ssshhhoooom!

As befitted an A-rank Gate, **Black Wizard’s Black Forest** was vast.

But the area I had explored was only a tiny fraction of it. As I adjusted my speed and ran, the Gate entrance soon began to come into view.

“It’s coming!”

“Jin Taekyung, you bastard…”

“Still, maybe because it’s their first time, there aren’t that many.”

“Gasp! Skeletons!”

Some shouted loudly to announce the monsters’ arrival. Others cursed me or calmly counted the enemies.

They were still greenhorns, with no real combat experience to speak of, and I could see them shrinking back.

Of course, the human Tosa mastiffs who had been given a taste of my hard training weren’t about to stand by.

“What the fuck are you doing over there? The line’s getting pushed back!”

“Don’t back up. Grip your shield tightly. What? You need to piss? Then fight like that!”

“New people, get a grip. That Jin Taekyung bastard isn’t going to help you. He even started a charity foundation in advance because someone might die here!”

“…”

They were making me out to be a complete piece of trash.

It was ridiculous, but I held back. Right. If they wanted to keep the new people mentally focused, they had to go that far to snap them out of it.

*People curse even the king when he isn’t around. What can you do?*

Of course, I remembered all their faces.

As I drew closer to the Hunters who had already formed a formation, I quickly climbed the tallest tree and shouted,

“Close ranks with your shields!”

Rumble!

The movement was perfectly coordinated.

The undead monsters, reduced to dogs that had lost the chicken they were chasing, looked up at the distant treetops before turning their grotesque faces.

On the hill where the Gate entrance was located, they spotted the more than fifty Hunters who had formed a battle line.

One of the skeletons raised a Bone Sword high and let out a hideous shriek.

- GRAAAAR!

It wasn’t an ordinary skeleton.

Bones that should have been exposed were wrapped in battered armor, and the Bone Sword raised as if to stab the moon was engulfed in a dark, ominous aura blacker than the night sky.

“A Skeleton Knight?”

Just because they were all skeletons didn’t mean they were all the same rank.

Skeleton Soldiers, Mages, Warriors…

Their abilities and strength varied wildly from one individual to the next, and the Skeleton Knight was a powerful monster universally recognized as A-rank.

*I’ve encountered them often in the Black Forest, but that one is different somehow.*

Encountering an A-rank monster like a Skeleton Knight in an A-rank Gate was only natural. They were positioned throughout the Black Forest, commanding lower-level Warriors and Mages beneath them.

I was narrowing my eyes as I watched it when—

- GRAAAH!

- GROWL!

Tss-tss-tss-tss!

Two more monstrous cries rang out, followed by two surging streams of aura.

I muttered in a voice tinged with surprise.

“Three Skeleton Knights in one group?”

That was a first.

A skeleton group was an army, and a knight was the general leading that army. An independent army only had one general.

*Did three groups form an alliance?*

But my prediction was spectacularly wrong.

The two newly appeared knights rattled their bones as they approached the Skeleton Knight that had appeared first. Then they dropped to one knee and drove their Bone Swords into the ground.

It was an unmistakable act of submission.

Purple light flashed in the empty sockets where the first knight’s eyes should have been.

Fwoooosh!

The light that burst from the abyssal darkness was intense.

The moment I met its gaze, the light transformed into flames and blazed brightly.

- GRAAAAR!

Krrrck!

Along with its roar, the creature’s body began to change.

Every bone grew thicker and longer, and an unknown black sheen flowed across its surface.

The transformation didn’t end there.

Shrrrraaaak!

Its armor, rusted and cracked in places, was restored as if time had been reversed. Broken chains reconnected, and the faded skull emblem on its chest regained its vivid color.

Finally, a dark green cloak fluttered in the wind.

When the creature had finished changing, it stared at its own palm.

Instead of white bones, the hand was covered by a sturdy gauntlet.

And then—

- Not. Bad.

“…”

The air surrounding the forest trembled.

Everyone, myself included, stared at it without a word.

A Skeleton Knight. A great knight reduced to a fallen undead.

But it was no longer a Skeleton Knight.

> **System**
>
> **Level 105 Skeleton Warlord**

- Come. Down. Hu. Man.

The burning purple light in its eyes fixed directly on me.

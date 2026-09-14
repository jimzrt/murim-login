# Checkpoint Review — 70–74

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

# Chapters 70–74

## Plot

Jin Taekyung endures Jin Mukyung’s brutal training, repeatedly losing consciousness but steadily demonstrating exceptional spear instincts and rapid growth. Mukyung teaches him through real combat, exposing Taekyung’s reliance on luck and forcing him to develop caution, physical conditioning, and the ability to read an opponent’s intent. After ten days, Taekyung masters the Jin Family’s Spear Technique and Manoeuvre Technique, earns the Martial Arts Manual Creation Skill, gains substantial Stats and Levels, and receives Mukyung’s recognition. The Training? Trial! Quest is completed, placing its Reward in his Inventory and promising an additional Reward.

Jin Wikyung assigns the brothers to visit the Mount Heng Sword Sect at the request of its new Sect Leader, Lee Seowol. The System forcibly creates the First Rate Quest [Yesterday’s Enemy, Today’s Ally], requiring Taekyung to deliver the Jin Family’s New Year’s Day invitation to the sect. Mukyung accepts because Seowol may reveal some of Mount Heng’s Peak martial arts. Taekyung, Mukyung, and the injured Hyuk Mujin depart for Eung-hyeon in a four-horse carriage, while Taekyung prepares to log out during the journey.

## Continuity

- Taekyung has mastered the Jin Family’s Spear Technique and Manoeuvre Technique and possesses First Stage Martial Arts Manual Creation, currently usable for those two arts.
- Mukyung’s final spar ended with Sword Energy cutting Taekyung’s uniform without injuring him; Mukyung recognized Taekyung’s progress and declared training complete.
- The Training? Trial! Quest succeeded. Taekyung received a Level Up, has its completion Reward in his Inventory, and was notified of an additional Reward.
- Lee Seowol is the new female Sect Leader of the Mount Heng Sword Sect, Lee Cheonbaek’s third child, and the younger sister of the deceased Young Sect Leader and Lee Seogeun.
- [Yesterday’s Enemy, Today’s Ally] remains incomplete. Its objective is to deliver Jin Wikyung’s invitation for the coming New Year’s Day; its Reward is unknown and its Failure penalty is None.
- Taekyung, Mukyung, and Hyuk Mujin are traveling to Eung-hyeon, expected to arrive in approximately three days. The regular attendants and coachman were dismissed, and Mujin remains because he obeys Taekyung as squad leader.
- Hyuk Mujin is still badly injured and under treatment. The assassin’s identity and sponsor remain unknown, as does any connection to Song Sword Sect.
- Jin Wikyung still intends to summon Shanxi’s sects on New Year’s Day and may seek the Alliance Leader position.
- Taekyung’s prior relationship with Lee Seowol and the missing details of his memories remain unclear. Whether he can complete the new Quest and successfully log out is unresolved.

## Translation Decisions

- Retain established terminology: **First Rate**, **Peak**, **Sword Energy**, **Martial Arts Manual Creation**, **Quest**, **Reward**, **New Year’s Day**, **Alliance Leader**, **Hyung-nim**, **four-horse carriage**, and **Eung-hyeon**.
- Render [昨日之敵 今日之友]’s Quest title as **[Yesterday’s Enemy, Today’s Ally]**.

## Durable state

{
  "active_continuity": [
    "After ten days of Mukyung's training, Taekyung has mastered the Jin Family's Spear Technique and Jin Family's Manoeuvre Technique; Mukyung is astonished by his growth and feels jealousy and fighting spirit.",
    "Mukyung's final spar with Taekyung ended when Mukyung used Sword Energy to cut Taekyung's uniform without injuring him, then declared training complete.",
    "The Training? Trial! Quest succeeded according to Mukyung's evaluation; Taekyung received a Level Up, a Quest completion Reward in his Inventory, and notice of an additional Reward.",
    "Taekyung has the First Stage Skill Martial Arts Manual Creation, which can create manuals for mastered martial arts; the available manuals are the Jin Family's Spear Technique and Jin Family's Manoeuvre Technique.",
    "Hyuk Mujin remains badly injured and under treatment after the attack.",
    "The Jin Family is pursuing an unidentified assassin believed possibly to be the Head Elder's hidden disciple.",
    "Jin Mukyung reunited with Jin Wikyung after three years but remains detached and prioritizes sword training.",
    "Jin Wikyung plans to summon every sect in Shanxi Province on New Year's Day and may seek to become Alliance Leader.",
    "Wipeng leads thirty elites south under the pretext of pursuing the nonexistent assassin, visits Song Sword Sect, and delivers Wikyung's summons as both summons and warning.",
    "Jin Wikyung searched the family records for Dark Heaven but found no information.",
    "Gong Yacheong is recovering and will take charge of the rebuilt Sakju Branch; Socheon and Soyul will accompany him in six months.",
    "Soyul is five years old and does not know that her parents are dead.",
    "The Returnee title grants Taekyung All Stats +10 and activates the Login and Logout functions.",
    "Taekyung accepted that he was half-finished, asked Mukyung for help, and received a System time limit of 9 days 20 hours 23 minutes.",
    "Childeuk is an injured former meal-delivery servant who recently became a Level 12 martial artist directly under Jin Wikyung; Wikyung publicly embraces and praises him after acknowledging a minor misunderstanding.",
    "Jin Wikyung is exhausted by the Jin Family's administrative workload but has restored his office to an orderly state.",
    "Lee Seowol is the new female Sect Leader of the Mount Heng Sword Sect and personally requested Taekyung and Mukyung's visit.",
    "Taekyung received the forcibly created Quest [Yesterday's Enemy, Today's Ally] to deliver an invitation to the Mount Heng Sword Sect for New Year's Day; the Quest is incomplete, has an unknown Reward, and has no Failure penalty.",
    "Taekyung, Mukyung, and Hyuk Mujin have departed for Eung-hyeon in a four-horse carriage; Mukyung accepted the trip because Peak martial arts may be revealed to him."
  ],
  "continuity_sources": [
    74
  ],
  "open_questions": [
    "The identity and sponsor of the assassin who attacked Taekyung and Hyuk Mujin remain unconfirmed.",
    "It remains unresolved whether Hyuk Mujin will actually become the next Master of the Gatekeeper Pavilion.",
    "It remains unresolved whether the Shanxi sects will answer Jin Wikyung's summons and whether he will become Alliance Leader.",
    "It remains unresolved whether Song Sword Sect has any connection to the attack.",
    "The reason the System displayed the same 2-hour-22-minute Time Limit twice remains unexplained.",
    "The nature of the minor misunderstanding that injured Childeuk remains undisclosed.",
    "Taekyung's prior relationship with Lee Seowol and the missing details of his memories about her remain unclear.",
    "It remains unresolved whether Taekyung will complete the forced Quest and successfully log out from the current prompt."
  ],
  "safe_through": 74,
  "temporary_decisions": [
    "Use gongcheong seokyu for 공청석유 with a footnote explaining the elixir and petroleum pun; use junzi for 군자 and Junzi Sword for 군자검 with a cultural footnote.",
    "Retain Hyung-nim for 형 and 형님 in Taekyung's deferential speech; use Three Questions Gorge for 삼문협, Great Hero for 대협, and Ghost Sword for 귀검.",
    "Use Alliance Leader for 맹주 and summon for 소집; use New Year's Day for 원단 and close the sect's gates for 봉문.",
    "Use Sleep Mode for 수면 모드, Medicine King Hall Master for 약왕당주, and four-horse carriage for 사두마차.",
    "Use Return for 귀환, Returnee for 귀환자, Ren and Du meridians for 임독양맥, Heart Demon for 심마, Paralysis Acupoint for 마혈, and Mute Acupoint for 아혈.",
    "Use fist-and-kicking technique for 권각술 and recognition for 인정; render 낙류검 as Falling Flow Sword, 질풍십이권 as Twelve Gale Fists, 화염신장 as Flame Divine Palm, and 분근착골 as Tendon-Splitting and Bone-Twisting.",
    "Render 비급 제작 as Martial Arts Manual Creation, 맷집 as Toughness, 천무지체 as Heavenly Martial Physique, 장칠득 as Jang Childeuk, 장 무인 as Martial Artist Jang, 인의예지 as benevolence, righteousness, propriety, and wisdom, 호환 as killed by a tiger, and 일각 as fifteen minutes.",
    "Use Squad Leader for 조장님, Third Young Master for 삼공자님, Mujin for 무진아, and seventh-tier student for 내신 칠 등급."
  ],
  "version": 1
}

## Reading copies

## Chapter artifact 70

# Chapter 70

Outside, dawn was dim. The winter air was cold as ice, and frost crumbled underfoot with every step across the training ground.

Jin Mukyung, who had already been warming up, grinned at me.

“Well, have you finished preparing yourself mentally?”

Of course not. But I hid my churning stomach and nodded.

Someone once said that if you couldn’t avoid something, you should enjoy it. When I thought of this as just another part of becoming stronger, I felt a little more at ease…

Shing.

“Then let’s see that impressive skill of yours.”

*Is this bastard Korean? Why is he so impatient?*

I had no time to avoid him. Jin Mukyung rushed toward me in an instant, and I hurriedly swung my spear shaft at him.

Clang! Kaga-gang!

Jin Mukyung’s breath drifted between us through the weapons we had crossed.

“Your stance isn’t bad.”

It had to be. I had survived seven years in a Gate where my life had been on the line, using nothing but a spear. The experience I’d built up with the spear was on a completely different level from my fists and kicks.

I glared into his eyes and answered.

“This time, it won’t be easy.”

One word at a time. Clearly and distinctly.

“You…”

Perhaps he sensed that something about my momentum was different. Jin Mukyung’s pupils trembled.

“Can’t you keep your damn eyes open?”

“Oh.”

* * *

Swoosh. Thud!

Jin Taekyung collapsed. It was not particularly surprising. This was already his fifth knockout.

The truly surprising thing was something else.

*I can’t believe he lasted two hundred exchanges against me.*

Five spars over two hours.

Anyone would naturally become exhausted. But Jin Taekyung was different. He kept getting back up like a roly-poly toy, growing stronger each time. By the end, even Jin Mukyung had been forced to face him seriously.

*What the hell is this guy?*

When he fought unarmed, his movements had been awkward enough to resemble those of an eighty-year-old man. But the moment he picked up a spear, everything changed.

The coward who had fawned over Jin Mukyung to avoid getting hit had vanished. In his place stood a seasoned spearman.

*He was like a wandering martial artist. Someone who had survived countless brushes with death.*

His movements were simple to the point of seeming crude. His attacks and evasions were irregular, relying on his own instincts. There was nothing fixed about the way a wandering martial artist fought.

That was exactly what Jin Taekyung looked like to Jin Mukyung.

And that was why the question only grew larger.

*How?*

Even among the heirs of prestigious families who picked up a sword as soon as they learned to walk, countless people only hovered around the threshold of First Rate. Yet this man had stood before the wall of the Peak realm in just three years.

And he did it while giving off not the scent of a courtesan’s powder, but the strong scent of a seasoned wandering martial artist. The more Jin Mukyung thought about it, the more absurd it seemed.

*Was something like this even possible?*

It was possible.

Having a Supreme Peak master cleanse his tendons and marrow. Improving his constitution with elixirs. Then swinging a spear until he shit blood while building real combat experience.

For three years without missing a single day!

“…That’s ridiculous.”

Jin Mukyung muttered hollowly and scratched his head.

If that was the case, only one answer remained.

*A genius.*

That one word resolved every question with perfect clarity.

Why?

Because he was a genius. Someone blessed by heaven, just as the word implied. Someone born with talent.

Geniuses were ahead in every way. They started from a completely different place.

“Zzz… Hoo…”

“…”

But of all people, this guy was a genius?

That was impossible. It couldn’t be true!

A sudden surge of anger rose within Jin Mukyung, and he kicked his younger brother in the rear.

“Prrrblblbl.”

Jin Taekyung rolled away several times before shuddering all over.

“W-Wolhwa noona. Not there.”

“…”

“If you suddenly do this… Ah. Aah!”

Crack.

The last thread of Jin Mukyung’s patience snapped.

* * *

Beep!



> **System**
>
> - Sleep Mode has been forcibly terminated!

*So it can be forcibly terminated?*

My joy at discovering a new function lasted only a moment. Why had Sleep Mode been forcibly terminated?

Because someone had woken me up, obviously.

“In the sacred training hall, you say what? ‘Not there’? ‘Not there’?”

Whack! Whack! Whack!

I curled up like a shrimp and spoke in a dying voice.

“Please, spare me…”

“No!”

Thwack-thwack-thwack!

I had no idea how many times I was hit. My consciousness had cut out twice in the middle of it.

My last memory was of squeezing out my remaining strength to leave a dying message on the training hall floor before collapsing.

When I opened my eyes, it was already night.

*What did I do for it to be night already?*

I felt like a time traveler. Ever since I had met Jin Mukyung, entire days had been flying by.

I muttered as pain swept through my entire body.

“Jin Mukyung is really strong.”

Excluding Jin Mukyung, I had faced two Peak masters so far.

The Head Elder and Jopil.

*The Head Elder doesn’t count.*

In his case, I had to admit that heaven itself had helped me. If not for the sacrifices of the Jin Family of Taiyuan’s martial artists and Lee Cheonbaek’s surprise attack, he was a master I could never have defeated, even if I had died and come back to life.

*Then what if I compare Jopil and Jin Mukyung?*

I did not have to think for long.

I had experienced fighting both of them, so the choice was easy.

*Jin Mukyung is stronger.*

Jopil was unquestionably a monster. Even now, I got goose bumps whenever I remembered the savage heat pouring from his Flame Divine Palm.

But how should I put it? He was strong like a Peak master, and he used the deadly Flame Divine Palm, but that was all.

*More precisely, it was a difference in how they used their martial arts.*

Jin Mukyung was different from Jopil. Even during our spar, he had used at least ten different martial arts to completely shut down my attacks.

To a martial artist, martial arts were another weapon. Jin Mukyung knew how to draw out the right weapon at exactly the right moment.

*Compared to him, what did I have?*

I could exclude the Jin Family’s Cultivation Technique, which I had possessed from the beginning. As for martial arts I had learned in Murim, I had only the Jin Family’s Spear Technique and the Jin Family’s Manoeuvre Technique.

Of course, both were unquestionably First Rate martial arts.

But put another way, they were only useful up to the First Rate level.

The limits of martial arts. Jin Wikyung could not possibly have failed to notice what I had felt.

*That was why he had sent me to Jin Mukyung. Ugh.*

My brow furrowed automatically from the pain. I had only raised my upper body a little, but every joint in my body throbbed, and my skin ached.

It seemed even Sleep Mode had its limits when it came to rest.

*Well, I did get beaten half to death.*

To complete the Quest by earning Jin Mukyung’s recognition, I would have to endure days like today—or even worse ones.

Maybe I would simply get beaten senseless and fail the Quest anyway.

*It really is one mountain after another.*

And that made me happy.

As an F-rank Hunter, I had not even been given the right to climb a mountain. But everything had changed.

There was a mountain I had to climb, and I had been given the right to climb it.

And I could do it faster than anyone else!

*This isn’t the time for this.*

I rose from my place, forgetting the pain. Every minute and second I wasted felt unbearable.

* * *

Jin Mukyung was in the underground training hall.

I descended the stairs leading underground, keeping my footsteps as quiet as possible, and saw him.

“Hah!”

With a short shout, his sword moved.

Whoosh! Shh-shh-shhk!

The wind split along the blade.

Jin Mukyung’s movements were as unrestrained as he thrust and slashed through the empty air at the speed of a ray of light.

About fifteen minutes passed.

Jin Mukyung lowered his sword and let out a long breath.

“Hoo.”

He wiped the sweat from his brow with his sleeve, then turned his head toward me.

It seemed he had noticed my presence some time ago.

“Tell me.”

The words came out of nowhere.

Confused, I reflexively asked:

“Tell you what?”

“About the martial art I just performed.”

“Uh, well, first of all, it was really fast…”

“For the record, if you say some pointless bullshit like ‘It was fast’ or ‘It was strong,’ I’ll kill you.”

*What a ghost.*

I racked my brain for an answer that would keep me alive.

What had Jin Mukyung’s martial art been like?

As I thought about it carefully, a vague impression began to surface.

“Rough?”

Jin Mukyung’s eyebrow twitched.

*Was that the right answer?*

“Did you just speak informally to me?”

“…It seemed rough.”

“Even a little kid could say that. Be more specific.”

The image in my head gradually became clearer.

I remembered the sword blades pouring toward an imaginary enemy and the movements that accompanied them. Fast, unrestrained motions. And an aura that seemed to press down from every direction.

It was like…

“A waterfall?”

“…”

“Huh?”

*What? Was that the right answer?*

After remaining silent for a while, Jin Mukyung suddenly swung his scabbard.

Smack!

“Ow! Why did you hit me?”

“Just because.”

He stared at me with a strange look in his eyes.

“How did someone like you ever come out?”

Was that an insult or a compliment?

I had no idea what he truly meant, but I had to hear the answer to his question if only to soothe my wounded pride. Rubbing my throbbing forehead, I asked:

“So, was that the correct answer?”

“There are thousands of martial arts manuals in Heaven’s Gate Temple. They were arrangements left behind by the departed Seniors who hoped to cultivate the younger generation of the orthodox Murim.”

“And?”

“The Falling Flow Sword you just saw is one of them. I found it buried deep in the archives.”

Falling flow. In other words, water falling down.

A waterfall.

I had only said the first thing that came to mind, but it had actually been the right answer.

“Oh, ooh.”

*Am I really a genius?*

If I could recognize martial arts like this after only two months of learning them, I was afraid of how strong I might become in the future. Even I found myself frightening.

“Surely you’re not having the embarrassing thought that you’re a genius or something after managing only that much?”

“…”

*He really is a ghost.*

Still, I seemed to have at least a little talent.

Unable to let go of the thought, I cautiously asked:

“Can everyone normally do this much?”

Jin Mukyung flinched.

“O-Of course. Anyone with eyes should be able to guess this much.”

“Come on.”

“‘Come on’? Do you want me to pluck out one of your eyes?”

“…That might be a bit much.”

*Why is this bastard being especially stone-faced today? Did something unpleasant happen?*

Even after I backed down, Jin Mukyung could not contain his anger. He snorted irritably.

“It’s basic. Basic. Everyone can do it.”

“I get it. Why do you keep getting angry? You’re scaring me.”

“Are you rebelling against me? Is it because you’re going through the storm-and-stress stage of adolescence? Do you want to get beaten with the Twelve Gale Fists?”

I did not know what the Twelve Gale Fists were, but getting hit by them sounded painful.

I shook my head fiercely, but Jin Mukyung’s anger showed no sign of fading.

“Do you know martial arts? Huh?”

“N-No, sir.”

“How long have you been learning martial arts?”

The answer slipped out reflexively.

“Two months. Two months.”

“Right, a bastard who’s only been at it for two months… What? Two months?”

Jin Mukyung glared at me with bloodshot eyes.

“Not three years, but two months?”

This was an emergency.

The social instincts I had gained through seven years of working life shone at that moment. I hurriedly opened my mouth, making sure to emphasize one particular part.

“Three years! Plus two months!”

Jin Mukyung’s fist had been trembling as though he had suffered a stroke, but it steadied again. For some reason, even his voice seemed slightly gentler.

“You little bastard. You startled me.”

*You startled me even more, you son of a bitch.*

*Does he have anger-management issues?*

If Jin Mukyung asked Jin Wikyung, my lie would be exposed immediately. But at least I would not have the misfortune of experiencing the Twelve Gale Fists right now.

In any case, Jin Mukyung’s anger subsided in the meantime.

“I’ll say this only once. Listen carefully.”

“I’ll engrave it on my heart.”

I bowed deeply, and he declared in a domineering tone:

“I teach, and you obey.”

“…”

*Is this a dog-training school or what?*

“There will be no objections. Why? Because I’m stronger than you.”

It was true, so I had no desire to argue.

Money, power, and force. Their forms might differ, but the world always revolved around the strong.

I wanted to stand at its center.

“What will you do?”

My answer had been decided a long time ago.
## Chapter artifact 71

# Chapter 71

The Jin Family’s Spear Technique consisted of seven forms in total. The final form, Sky-Piercing Strike, smashed into the steel dummy.

Boom!

With a deafening crash, the steel dummy’s chest caved in and it slammed into the wall. As I withdrew my spear, Jin Mukyung’s voice reached my ears.

“The Jin Family’s Spear Technique is passable.”

“Uh, yes.”

“The Jin Family’s Manoeuvre Technique is similar.”

Wait. Had I ever told him what martial arts I had learned?

As I searched my memory, Jin Mukyung gave a quiet laugh.

“Do you know why I entered Heaven’s Gate Temple?”

“Um. Because you couldn’t stand the sight of me?”

“…That’s not entirely wrong.”

He muttered under his breath and nodded, then suddenly came to his senses.

“Ahem. There was a more important reason than that.”

“What was it?”

“There was nothing left for me to learn in our family.”

“What?”

“I needed something new. As luck would have it, Heaven’s Gate Temple offered me admission, and I had no reason to refuse.”

“Then what about the Jin Family’s Spear Technique?”

“I just told you. There was nothing left for me to learn.”

“No, but you’re a swordsman.”

“So?”

“Huh?”

“Don’t you eat side dishes with your rice?”

“That’s different.”

“It’s the same to me.”

*It’s different to me.*

*I’ve learned several different weapons, too, but…*

My situation was completely different from Jin Mukyung’s. That had not been martial arts. It had been a desperate struggle to survive my battles with monsters.

Once I became accustomed to the spear, I had not had the time to look elsewhere.

Focusing on just one thing was already difficult enough.

“You look like you don’t understand. It’ll be faster if I show you.”

Shing.

Jin Mukyung drew his sword and stood before the steel dummy.

After casually warming up with a few movements of his hands, he spoke in a quiet voice.

“Let’s try this.”

His legs crossed rapidly. A flash shot out right after and slammed into the steel dummy’s chest.

Swoooosh! Boom!

I was speechless. The form was slightly different, but the movements were familiar. There was no way I could fail to recognize them.

“This is…”

“Sky-Piercing Strike. The final form of the Jin Family’s Spear Technique. Though in this case, I suppose I should call it the Jin Sword Technique.”

For a moment, I could not speak. Then I remembered something I had temporarily forgotten.

Jin Mukyung was a genius. An ordinary person might struggle just to finish a bowl of plain rice, but Jin Mukyung could digest an eight-dish spread without trouble.

*Genius. Genius. I’d only ever heard the word before.*

With just a few simple changes to the movements, he had transformed the Jin Family’s Spear Technique into a sword technique.

He truly was a genius of martial arts. The rumors had not been exaggerated.

*This bastard… He’s the real deal.*

The System helped its user grow quickly. It did not turn them into a genius. But Jin Mukyung had been born one.

The move he had just shown me had probably been no more than the tip of the iceberg. A chill ran down my spine.

“Are you listening to me?”

I only came to my senses when I heard his cold voice.

“Ah, yes.”

“Your hyung went to the trouble of giving you a demonstration, and you dare look away?”

Flick!

“Gah.”

My vision flashed. Jin Mukyung watched me suffer with satisfaction before speaking again.

“I’ll explain it one more time, so concentrate. Understand?”

“Gnh. Yes, sir.”

“Anyway, martial arts are…”

“…”

“Uh, martial arts are… Ah, damn it.”

Jin Mukyung’s face flushed red as he shouted.

“I forgot because of you!”

Whack!

*You fucking bastard…*

* * *

In the end, Jin Mukyung chose conversation as his method.

A physical conversation.

“You don’t understand very well when things are explained verbally. It’s faster for you to experience them with your body.”

“W-Wait a moment.”

“There’s no such thing as ‘wait a moment’ in real combat. Would you say that to someone who came to kill you? ‘I’m nervous, so I’ll go take a piss first.’ Would you expect him to say, ‘Then go take a shit, too’?”

“We’re sparring right now!”

“Huh? You’re using informal speech again. You’re dead.”

Jin Mukyung gripped his wooden sword tightly and charged at me like a leopard.

I launched myself away without waiting to see what happened.

Boom!

Leaving the bone-rattling crash behind me, I snatched a wooden practice spear from the rack. An ominous voice followed me.

“From now on, I’ll teach you a lesson.”

Swoooosh!

The sound of the air being torn apart was anything but ordinary. I turned and swung my spear at the same time, but I was already too late. The faintly upturned corner of Jin Mukyung’s mouth was right in front of me.

“First.”

Thud!

His fist shot up from below and struck my lower jaw. My feet left the ground against my will.

Through my shaking vision, Jin Mukyung’s voice continued.

“When fighting someone more skilled than yourself, be cautious.”

The next moment, Jin Mukyung’s palm struck my chest. With a bang like a bursting balloon, I flew backward and slid all the way into the wall.

“Cough.”

My organs did not spill out with a mouthful of blood. When I lifted my head, I saw Jin Mukyung slowly walking toward me.

“You’re such a coward. Did you really think your hyung would use internal energy against his younger brother?”

I answered gruffly.

“Then throw away the wooden sword.”

“I can’t. The feel of hitting things is better with this.”

That was the confidence of the strong. Even so, he was not careless enough to discard his weapon.

*This is going to be difficult.*

Fortunately, Jin Mukyung was easy to provoke.

Especially when it came to me.

“Did you chicken out?”

“What?”

The smile disappeared from Jin Mukyung’s face. I was afraid of what he’d do to me later, but that was a problem for later. Right now, I wanted to beat the bastard in front of me somehow.

“I asked if you chickened out.”

“I don’t really know what that means… but it’s really pissing me off.”

The moment I finished speaking, Jin Mukyung rushed toward me. His movements were noticeably rougher than before. I knocked aside the wooden sword descending toward my shoulder with the shaft of my spear.

Krrrk.

*Did they coat this wooden sword with glue?*

I needed to widen the distance, but the sword would not come away. It wrapped around my spear shaft like a snake and stabbed inward.

“What the hell is this?”

“What else would it be? The Jin Family’s Spear Technique. No, the Jin Sword Technique.”

*The Jin Sword Technique? This?*

“It’s completely different from what you showed me earlier!”

“Ah. I mixed in a few other sword techniques.”

“That’s cheating!”

“Second. Never forget that while you were drinking your ass off with women, I was training until I was covered in blood and sweat.”

At the same time, the wooden sword slammed into my side.

Thud!

The pain was secondary to the wave of fury that surged through me.

*What? Drinking with women?*

*While everyone else was holding their girlfriends’ hands and going on dates for Christmas, I was having a group date with monsters in a Gate, you fucking bastard!*

Whack-whack-whack!

The wooden sword pounded my thigh and forearm in succession, but I felt nothing. My anger had overwhelmed the pain.

I gritted my teeth and sent my spear flying in every direction.

Sshh-shh-shhk! Clang!

Under my sharp offensive, Jin Mukyung began to retreat little by little. Combat was all about momentum. My instincts, honed through countless real battles, whispered to me.

*Now!*

I brought my spear down with all my strength toward the crown of his head.

Boom!

The crash was loud enough to leave my ears ringing. But the attack had not landed properly.

Jin Mukyung raised his sword and blocked the spear with ease. He snorted.

“Too obvious.”

“Yeah. If it’s too obvious, it’s no fun.”

With a triumphant grin, I thrust one fist toward his abdomen.

*It’s a feint, you bastard!*

The provocation and the attack before it had all been for this moment.

When you were standing this close, martial arts did not matter. One punch to the solar plexus, and not even a Peak master’s grandfather would stand a chance.

*It’s over.*

My fist, carrying all the resentment I had built up, slammed into Jin Mukyung’s solar plexus.

Clang!

…Clang?

*What the hell was that?*

I was confused for only a moment before a scream burst out.

From my mouth.

“Argh! My hand!”

It hurt! And it hurt like hell!

Through my pain-filled vision, I saw Jin Mukyung shyly lifting his shirt. A bulging leather vest beneath his martial arts uniform came into view.

*What is that?*

A bulletproof vest? No, it was not one. But it looked like it could stop bullets. Every pocket in the leather vest had been packed full of iron ingots.

“Third…”

Jin Mukyung pulled a dented iron ingot from one of the pockets near his solar plexus. My fistprint was clearly visible.

“Fight only after discerning your opponent’s intentions.”

“Why the hell are you wearing that?”

“Fourth. Never neglect physical conditioning, even in everyday life.”

“Damn it!”

Martial arts? Forms? There was no more of that nonsense. I threw off the awkward appearance of a martial artist and returned to being a Hunter with seven years of experience.

My hand was already injured, so properly using the Jin Family’s Spear Technique would be difficult. Besides, Jin Mukyung knew every martial art I had learned.

*I’ll show you what a real fight looks like.*

With all my strength, I kicked Jin Mukyung in the shin as he grinned triumphantly. It was a decisive technique known as a soccer kick, or simply a shin-kick.

I had never seen anyone stay fine after taking one of these.

Clang!

Add one more to the list.

“You fucking—”

“You idiot.”

Jin Mukyung looked down at me as I collapsed, clutching my foot. His expression seemed to say that I was the most pathetic person alive.

“Fifth… Never mind. Talking is exhausting.”

He pulled a flat metal plate from beneath his pant leg and strode toward me. I tried to stand, limping, but he kicked my ankle and made me sit back down.

*Damn it.*

It was over.

If I used Inventory, I might have a chance to turn things around, but I did not want to blatantly do something that would obviously make him suspicious. I lowered my head with a sigh.

“Let’s stop.”

“You want to stop?”

I lifted my head at his hard voice. Jin Mukyung’s face had gone cold.

“After only this much?”

The man who had been grinning and enthusiastically beating me only moments ago was nowhere to be seen.

His emotionless gaze made my skin prickle, and my Adam’s apple bobbed.

Gulp.

Almost simultaneously with the sound of me swallowing, the wooden sword slammed into my right shoulder.

With a thud, my arm bent uselessly and I lost my balance.

“Guh. What the hell are you doing…?”

Jin Mukyung did not care. He swung the wooden sword again. The Jin Mukyung standing before me now seemed unable to hear the voice of the defeated.

Thud. Thud. Thud.

He struck my left arm, then both legs. Only then did his hand stop.

“You just had all four limbs cut off. By a vicious Peak master of the dark path who is several times stronger than you.”

“…”

“If he were even nastier, there would be other methods, too.”

Tap-tap-tap.

The moment Jin Mukyung’s hand blurred, my entire body stiffened and my tongue curled up. The System immediately announced the abnormal condition.

Beep!



> **System**
>
> - The **Paralysis Acupoint** has been subdued. You will be paralyzed for two hours!
>
> - The **Mute Acupoint** has been subdued. You will be unable to make a sound for two hours!

I could not move even a hair, and I could not speak.

A breathing corpse. In my current state, even a child could kill me.

*Jin Mukyung. You insane bastard!*

The curses circled only inside my head and could not escape my lips. All I could do was glare at him. Jin Mukyung calmly met my furious gaze.

“Tendon-Splitting and Bone-Twisting is a cruel technique. Within an hour at most, your qi and blood will twist and all the bones in your body will be crushed. Even if you miraculously survive, you’ll either become a madman or live the rest of your life crippled.”

“…”

“Do you think you could endure that pain? You’d probably forget who you are within fifteen minutes.”

My stomach churned. Not because of his explanation of Tendon-Splitting and Bone-Twisting.

It was Jin Mukyung’s eyes. There was no emotion in them. Those black eyes were unfamiliar and frightening.

*Could Jin Mukyung really be about to kill me?*

No. That was impossible. I was Jin Taekyung. A direct descendant of the Jin Family of Taiyuan, and Jin Mukyung’s only younger brother.

But what he did next went far beyond anything I had expected.

“Don’t worry. I’ll send you off without pain.”

A quiet voice accompanied something cold touching my throat. It was the metal plate Jin Mukyung had pulled out earlier. Its thin, sharp edge slowly pressed into my flesh.

*Die? Like this?*

I had survived dozens of brushes with death. In Gates, and in Murim. I had struggled all this time to survive somehow…

And now I was about to die without even being able to blink.

To a so-called biological older brother who did not share a single drop of blood with me!

*What the fuck kind of situation is this?*

My body rigid, I stared only at the ceiling. Then the voice of the Reaper reached my ears.

“Die.”

Slice.

The strength drained from my entire body. I felt hot blood trickling down my neck.

Jin Taekyung. Aged twenty-seven. Gone to sleep in Murim.

I slowly closed my eyes.

“…”

No, wait. Something was wrong.

*I was hit at an acupoint, but I closed my eyes?*

At that moment—

Ding.



> **System**
>
> - The **Paralysis Acupoint** has been released. The paralysis has ended!
>
> - The **Mute Acupoint** has been released. You can speak freely!

“Get up.”

“…”

At Jin Mukyung’s voice, I slowly opened my eyes. All five of my senses were sharp and clear, proof that I was alive.

*How?*

I hurriedly felt the back of my neck. The cut stung, and blood came away on my fingers, but there were only a few drops of it. Everything had been an illusion brought on by the fear and tension of death.

“Remember.”

His cold voice continued—the same voice that had pronounced my death only seconds earlier.

“You died once today.”
## Chapter artifact 72

# Chapter 72

“You died once today.”

The cold voice continued.

“Your limbs were cut off, you were subjected to Tendon-Splitting and Bone-Twisting, and your throat was cut. The degree and form of the pain may have been different, but you died. Without a doubt.”

Once the relief of being alive faded, anger took its place.

I stood on trembling legs. After swallowing the blood pooled in my mouth, I glared at Jin Mukyung.

*What a fucking lunatic.*

I wanted to drive my fist into that smug face right away, but I held myself back. Not because I was weaker than Jin Mukyung. Because I knew he was right.

“…So? What are you trying to say?”

His answer came immediately, as if he had been waiting for me to ask.

“That you don’t have much life left.”

“What?”

“You’re only half-finished. You’re neither a martial artist nor a wandering martial artist. A half-baked mess. Someone as sloppy as you is just begging to die the moment he enters the Murim.”

Half-finished.

That might have been the most accurate description of my current state. I was a Hunter and a martial artist at the same time.

“Sleeping Dragon of Shanxi? First Rate master? Even a passing dog would laugh. You’re just a brawler. You’re sloppy for a martial artist, and you don’t even fight as pragmatically as a wandering martial artist. Don’t mistake surviving through good luck for skill.”

I barely managed to open my mouth.

“Then what about Jopil? Was that luck too, according to you?”

“Jopil, One Question, One Kill? He was obviously stupid enough to let his guard down in front of an enemy. You just happened to have one last move capable of turning the situation around.”

“……!”

“What? Do you think I guessed too accurately despite not seeing it myself?”

Jin Mukyung clicked his tongue.

“Even a deaf old man knows that the Third Young Master of the Jin Family of Taiyuan is a wastrel. Did Jopil not know? The moment he let his guard down, he was finished too.”

*What is this guy, a stalker?*

I felt like Sun Wukong trapped in the Buddha’s palm. His guess was that accurate.

“Let me make this clear.”

Jin Mukyung fixed me with a somber gaze.

“That luck of yours stops working here.”

“……”

“The Murim is crawling with all kinds of monsters. And they don’t let their guard down like Jopil did. You’re no longer the Jin Family’s wastrel of a Third Young Master. You’re the Sleeping Dragon of Shanxi.”

Every word stabbed straight into my vitals. Everything Jin Mukyung said was true, and it was time for me to face reality.

“Damn it.”

He was right. I was half-finished.

Thanks to the greatest stroke of luck in my life—the System—I had somehow survived this long. But it seemed that luck had taken me exactly this far.

*But… I really am lucky.*

Not only had I discovered the problem early, but an excellent problem-solver was standing right in front of me to help solve it.

“Help me.”

Jin Mukyung.

A fully realized Peak martial artist and a genius of martial arts.

And—

“…Hyung.”

My older brother.

Ding.

> **System**
>
> **Time Limit:** 9 days 20 hours 23 minutes

* * *

Murim people were a proud lot. Even a Third Rate wandering martial artist who wore a rusty sword at his waist and drank cheap baijiu was like that, so the arrogance of scions from prestigious sects reached the heavens.

“Help me, hyung.”

In that sense, this guy had become a decent human being. Three years ago, he would have run to his eldest brother with tears in his eyes… but he had grown. Far more than expected.

*He’s a strange one.*

Neither his personality nor his martial arts could be easily understood. That was both a strength and a weakness. But one thing was certain: nothing worked against a *true master*.

*But his talent is real.*

Over the past three years at Heaven’s Gate Temple, Jin Mukyung had encountered countless prodigies, but Jin Taekyung’s rate of growth was unmatched.

*He has advantages they don’t.*

He could understand martial arts at a glance. He had excellent combat instincts, and he also knew how to listen to other people’s advice.

*Though for now, he’s still a half-finished mess with everything jumbled together.*

As time passed, his weaknesses would be filled in and his excesses would be smoothed out. When that happened, Jin Taekyung’s martial arts would be complete.

Like taiji achieving harmony.

*Taiji? Is that a little too grandiose?*

This was starting to become burdensome.

But he could not stop wondering. How would that bastard grow? How far would he climb?

*I’m going to be busy.*

He had to leave and return to Heaven’s Gate Temple within fifteen days at the latest. Jin Mukyung finally opened his mouth.

“What are you doing? Pick up your spear.”

“Hyung!”

Seeing Jin Taekyung’s face brighten, Jin Mukyung suddenly had a thought.

*When did this bastard start speaking informally to me?*

That was the moment the intensity of his training rose another level.

* * *

Bang.

Jin Wikyung stamped his seal onto the final document with heavily bloodshot eyes.

He had been freed from nearly twenty hours of backbreaking labor, but he was not happy at all. New work would be piled up by tomorrow morning anyway.

*Are these things breeding when I’m not looking?*

The only comfort was that he could finally see the end.

After completing his final review, Jin Wikyung rang a small bell. Before its clear sound had even faded, two sturdily built servants appeared.

“Did you call, Lesser Family Head?”

“Take these away.”

“Yes, sir.”

The servants skillfully stacked the documents onto a cart. Just as they were about to leave, Jin Wikyung spoke.

“Ah. You stay.”

The servant he had pointed to blinked in surprise.

“Me, sir?”

“That’s right. You.”

Once he was alone with the servant, Jin Wikyung began speaking in a solemn voice.

“So, how have you been finding the work lately?”

“Very well, sir. It’s all thanks to your kindness, Lesser Family Head.”

“Nothing causing you any inconvenience?”

“Oh, goodness, of course not.”

The servant, Childeuk, did nothing but nod repeatedly. He was illiterate and could not even get through the Thousand Character Classic, but he still had ears to hear and eyes to see.

After its victory in the recent war, the Jin Family of Taiyuan had risen to become the foremost family in Shanxi. Its Lesser Family Head, Jin Wikyung, had begun to be called the Junzi Sword[^1] for his swift recovery efforts and fair handling of the aftermath.

*Why would such an esteemed person want me?*

His heart pounded with nerves. Had he made some mistake? Or had Jin Wikyung perhaps noticed his talent for martial arts?

The former would be disastrous. The latter would be a chance to turn his life around.

*My bones and muscles are sturdy, at least. I never even had a stomachache as a child.*

He could already see himself wearing a sword at his waist and letting his hero’s headband flutter in the wind.

But when Jin Wikyung saw Childeuk’s eyes growing hazy, he flinched.

*What the hell is wrong with this guy?*

Childeuk’s eyes were filled with desperate longing, as if he were willing to offer his soul to obtain whatever he wanted.

They were not the kind of eyes one man should direct at another man.

*Don’t tell me…?*

Male love, something he had only heard about…

No, that was not it. He could not jump to conclusions. Childeuk was a member of the Jin Family, someone he should trust and cherish.

Jin Wikyung forcibly erased his suspicions and spoke.

“I’ve heard a lot about you.”

“Y-You have, sir?”

“Of course. I’ve been keeping an eye on you for a long time.”

More precisely, not for a long time. Only for the past three days.

Jin Wikyung had been searching for a reliable servant to entrust with a very important task, and Childeuk was the ideal candidate he had personally selected.

“A talented man possessing all four virtues—benevolence, righteousness, propriety, and wisdom. That’s you.”

“How can this be…!”

Childeuk, an exceptional servant possessing all four virtues, shuddered with emotion. He had no idea what those four virtues meant, but he understood the word “talent” perfectly.

*I’m talented?*

He had been praised for his strength and diligence, but this was the first time anyone had called him talented. And to receive such an assessment from the Lesser Family Head himself, a man as lofty as the heavens…

Was this a dream or reality? Childeuk was swept up in overwhelming excitement. He was so excited that even his tongue became tangled.

“I’ve always been watching you too, Lesser Family Head!”

Jin Wikyung’s body flinched.

*What did I just hear?*

“…What do you mean?”

“I’ve dreamed of this moment for a long time. The day I would stand behind you, Lesser Family Head!”

“Wait. That sounds strange. Why would you stand behind me?”

“Ah.”

Childeuk swallowed. Jin Wikyung was telling him not to stand behind him. In other words, he wanted Childeuk to take the lead and win glory.

“Then I’ll stand in front!”

“No! That’s strange too!”

But Childeuk’s charge, like a wild stallion, did not stop.

“I will gladly offer this one body of mine!”

Jin Wikyung’s vision went dark.

“No. Don’t do it! Don’t offer it!”

“Lesser Family Head!”

Huff, huff.

Childeuk breathed heavily, and Jin Wikyung gathered his internal energy.

*I never thought something like this would happen.*

No matter how open-minded he was, this was too much.

Personal sexual preferences were one thing, but he had no desire to be the object of them. Jin Wikyung swallowed hard.

“Then… are you really into men?”[^2]

Childeuk’s eyes flashed. He was thinking about wearing the navy-blue uniform worn by the Jin Family’s martial artists.

“Yes! Just tell me to do it!”

“How dare you set your sights on me? Not a chance, you bastard!”

Smack!

A slap from a Peak master was powerful. Childeuk collapsed like a puppet with its strings cut, and Jin Wikyung stared down at him while breathing heavily before hurriedly ringing the bell.

Ding. Ding.

“Lesser Family Head, did you call—? Gasp. Childeuk!”

Jin Wikyung spoke to the horrified servant.

“Take him out immediately!”

“W-What happened?”

“That bastard tried to… No, never mind.”

It was not something he could say to one of his family’s servants. For the first time in his life, anger and wounded sorrow brought him close to tears.

“I-I’ll take care of it.”

Just as the quick-witted servant hoisted Childeuk onto his back, Jin Wikyung added the most important part.

“And that man.”

“Yes?”

“Remove him from his post.”

“Ah.”

The servant suddenly remembered Childeuk’s assignment.

*Delivering meals.*

The most important duty given to Childeuk, an exceptional servant possessing all four virtues, was to bring every meal to Jin Mukyung and Jin Taekyung.

“Don’t let him go anywhere near my younger brothers. Understood?”

“Yes, sir!”

* * *

### Training Day 1

I decided to start keeping a diary today.

So I would not forget what I learned during this training.

Under Jin Mukyung’s guidance, I did nothing but swing a spear all day. Every day begins and ends with a spar. I got beaten half to death, but it’s bearable.

This is my first time grinding ink, and it’s surprisingly fun.

### Training Day 2

I swung my spear to the point of death again today. Perhaps because of that, my Strength and Stamina stats increased, and the Jin Family’s Spear Technique reached the ninth stage.

It’s progressing much faster than when I trained alone, but I can’t help thinking that I would be better off learning another Peak martial art during this time.

Still, Jin Mukyung must have his reasons.

Grinding ink has become a little annoying. I’m tired.

### Training Day 3

The Jin Family’s Spear Technique again. I asked him to teach me another martial art and got beaten half to death. He said my mind was rotten.

While desperately dodging his attacks, the Jin Family’s Manoeuvre Technique rose to the eighth stage. Damn it. This is surprisingly effective.

### Training Day 4

Since starting training, I haven’t slept more than two hours in a day.

Most of my time is spent repeating training, sparring, training, and sparring with Jin Mukyung. Starting yesterday, I began using fasting pills instead of wasting time eating.

Even with the System, I’m reaching my physical limit.

### Training Day 5

My arms hurt, so I only ground a little ink.

The sky is yellow.

Going to sleep.

### Training Day 6

I don’t understand why the System doesn’t have a notepad function.

I got angry while grinding ink and broke the inkstone. Jin Mukyung beat me.

### Training Day 7

The Jin Family’s Manoeuvre Technique reached the ninth stage. My Level also increased by one.

I’ve practiced it so obsessively that these days, I even use the footwork when I’m simply walking around.

I got goose bumps.

### Training Day 8

My hands and feet keep getting tangled today. It feels like the martial arts I know, but not quite.

The martial arts I’ve performed thousands—even tens of thousands—of times feel unfamiliar. Jin Mukyung said it was a natural phenomenon.

*What the hell is he talking about?*

I got beaten because my expression was disrespectful.

### Training Day 9

I think I get it.

* * *

Bang!

Compressed air erupted from the tip of the wooden spear. Jin Mukyung skidded backward and clicked his tongue as he looked at his broken sword.

“That was a narrow success.”

I did not answer. I stood there blankly, gripping my spear.

*So that’s what it was.*

I thought I knew the martial arts I had learned inside and out. But I had been wrong. I had merely mistaken the middle of the mountain for the summit.

Whenever my martial arts rose to a new level, a new landscape came into view.

*Just like now.*

Ding. Ding. Ding.

> **System**
>
> - You have achieved mastery of **Jin Family’s Spear Technique**!
>
> - You have achieved mastery of **Jin Family’s Manoeuvre Technique**!
>
> - Achievement **Master a First Rate Martial Art** completed!
>
> - As a reward, a new Skill, **Martial Arts Manual Creation**, has been generated!
>
> - All Stats have increased significantly!
>
> - Level Up!
>
> - Level Up!

A wave of System notifications swept over me.

[^1]: *Junzi* is a Confucian ideal referring to a morally upright and cultivated gentleman.

[^2]: In Korean, *nam-saek* can refer both to male homosexuality and to the color navy blue, creating the misunderstanding between Jin Wikyung and Childeuk.
## Chapter artifact 73

# Chapter 73

Ding. Ding. Ding.

The flood of System notifications was enough to make my ears hurt. I opened my mouth wide and dismissed the message windows filling my vision one by one.

*Why are there so many rewards?*

Two Level Ups, an increase to all my Stats, and a new Skill for completing an achievement.

*Martial Arts Manual Creation?*

Ding.

> **System**
>
> **Skill Window**
>
> **Martial Arts Manual Creation**
>
> **Grade:** None
>
> **Realm:** First Stage
>
> **Description:** Can create martial arts manuals for martial arts that have reached mastery.
>
> **Martial Arts Manuals Available:** Jin Family’s Spear Technique, Jin Family’s Manoeuvre Technique

After reading the description, I realized it was exactly what I had guessed.

*It’s a Skill, so it’s better than nothing, I suppose…*

For now, though, it did not seem particularly useful. I was mostly fascinated that the System would give me a Skill for some kind of production job.

*This really does feel like a game sometimes.*

There were still far too many things in this world that I had never experienced.

Everything was unfamiliar and unreal. Even now, I was still unsure whether Murim was a game or another reality altogether.

Smack!

“Ah.”

I turned around, clutching the back of my stinging head. Jin Mukyung was looking at me with a contemptuous expression, a wooden sword broken in half in his hand.

“Not concentrating?”

“Seriously. Why do you keep hitting me in the head? It’s annoying.”

“This bastard is slipping back into informal speech again.”

Jin Mukyung narrowed his eyes, but he was not very frightening anymore.

*It’s not like this is the first or second time I’ve been hit.*

Today marked the tenth day since the hellish training began.

I had realized one important fact right from the start.

*I get hit even when I use polite speech!*

I had been beaten black and blue. I had even gained the **Toughness** Stat on only the second day, which said everything that needed to be said. No matter what I did, I was going to get beaten anyway. If so, using informal speech while getting beaten at least let me claim a moral victory.

Smack!

“This much is just a tickle.”

The Toughness Stat had not appeared for no reason.

Just as flowers grew with sunlight and water, my Stats had flourished under merciless violence and hellish training.

Whack!

“Hey, wait. You hit bone. Bone.”

“The spar isn’t over.”

Thud-thud-thud!

While taking hits from the wooden sword as it struck my vital points with practiced precision, I swung my spear as well.

Sshh-shh-shhk! Crack!

Ten days of hellish training.

At last, the Jin Family’s Spear Technique and Jin Family’s Manoeuvre Technique flowed out as naturally as breathing, having reached mastery.

Ding.

> **System**
>
> **Time Limit:** 2 hours 22 minutes

Ding.

> **System**
>
> **Time Limit:** 2 hours 22 minutes

“…?”

What the hell? Why did it ring twice?

* * *

Sshh-shh-shhk!

Clang!

Blocking the spear pressing in on him, Jin Mukyung swallowed a laugh that was about to escape.

*Look at this bastard.*

Ten days. It was a short time if you thought of it one way, and a long time if you thought of it another. But if that was how long it took to achieve mastery of a First Rate martial art, the matter was entirely different.

*What kind of person is this?*

He had thought the same thing dozens of times over the past ten days. Jin Taekyung’s rate of growth was beyond even the saying “hear one, know ten.”

*Knowing something and making it your own are different.*

To achieve mastery of a martial art meant that one understood it perfectly and could wield it as such. Jin Taekyung had made two First Rate martial arts completely his own in only ten days.

Even taking into account the fact that he had already reached a certain level, this was an astonishing achievement.

*So it really is possible.*

Jin Mukyung was dumbfounded. What had his initial estimate been again?

One thing was certain: Taekyung had far surpassed his original goal.

*I was only trying to cure his habit of throwing out his hands and feet whenever he felt like it and make sure his fundamentals were solid…*

But once training began, things had changed.

Fundamentals? Jin Mukyung could not have known it, but Jin Taekyung had trained relentlessly for seven years. Training to become stronger. Struggling desperately to survive.

His palms split open and healed dozens of times, and with each cycle, his spear became faster and stronger. Because of that, there was nothing to criticize in Jin Taekyung’s fundamentals except for a few issues with his posture.

*The same goes for everything else.*

Horse-stance training would have been nothing more than a waste of time.

Strength, Stamina, Agility—every one of his physical abilities far surpassed those of martial artists at the same level, and they had developed with remarkable balance.

*So surviving until now wasn’t simply a matter of luck.*

Look at his tall, lanky frame and long limbs. At his lean, solid muscles. Was this really the same skinny brat who had built abdominal muscles three years ago to impress courtesans?

*Damn, was he some kind of heavenly martial physique?*

Jin Mukyung was feeling dumbfounded all over again when it happened.

Swoooosh!

A spear thrust forward with powerful momentum.

Jin Mukyung stepped back using his footwork, but Jin Taekyung tenaciously followed and continued his attack.

Sshk! Sshh-shh-shhk!

Even the same martial art changed depending on who wielded it and how they wielded it. Every move carried the wielder’s temperament and disposition.

The Jin Family’s Spear Technique Jin Mukyung was using now was no different.

*Was this what the Jin Family’s Spear Technique was supposed to be?*

Martial artist and wandering martial artist. Movements that had been awkward and uneasy in some indefinable way were gradually beginning to harmonize.

*He’s already made it his own.*

Ten days ago, Jin Taekyung had been half-finished, but the change had already begun. Jin Mukyung was proud of his younger brother’s achievement. At the same time, heat began to build in his stomach.

*This feeling…*

It was an emotion he had felt once before, toward someone else. He had never imagined that Jin Taekyung would become its object.

*Jealousy. And fighting spirit.*

Jin Mukyung froze in place.

Toward that momentary opening, the final form of the Jin Family’s Spear Technique, Sky-Piercing Strike, shot forward.

“Haap!”

Whoooosh!

The wind spiraling around the spear swallowed Jin Taekyung’s shout. At the moment when it seemed the spear was about to pierce straight through his chest, Jin Mukyung’s hand seized his sword hilt.

Fwoosh!

A flash erupted from his waist and cleaved through the wind.

At its end stood Jin Taekyung.

* * *

Sshk!

With a short rush of wind, my upper body suddenly felt breezy. Starting from my right waist and ending at my left shoulder, my martial arts uniform had been sliced cleanly apart, and the chilly air of the underground training hall seeped through the gap.

Only after confirming that I had not been injured did I let out a relieved sigh.

“Whew.”

A Sword Energy attack out of nowhere? My heart had nearly jumped out of my throat.

“Crazy. You said you weren’t going to use Sword Energy.”

“……Only an idiot would take that at face value.”

Jin Mukyung answered with a distinctly uneasy expression and sheathed his sword.

“Training ends here.”

Ding.

> **System**
>
> - **Jin Mukyung** has declared the training complete.
>
> - The remaining **Time Limit** has vanished.
>
> - Quest success will be determined according to **Jin Mukyung’s** evaluation.

Success? Or failure?

With my eyes shining expectantly, he opened his mouth.

“You’re nowhere near good enough.”

“Ah.”

“To think this is all you managed to keep up with me after ten days. What a waste of my ti—”

Jin Mukyung stopped speaking and made a sour face.

“What’s with that expression?”

“Huh? What expression?”

“That bizarre expression you’re making right now!”

“I’m not making one. I have no idea what you’re talking about.”

But Jin Mukyung was right.

I had to make a tremendous effort to hide the corners of my mouth, which kept trying to rise. The reason was the System message floating in the air.

Ding.

> **System**
>
> - You have fulfilled the conditions for quest success!
>
> - Quest **Training? Trial!** has been completed!
>
> - Level Up!
>
> - The Quest completion Reward has been moved to your Inventory!
>
> - Excellent work. An additional Reward will be granted!

“Hm. You’re a shy child, aren’t you?”

Jin Mukyung. An honest young man.

“You bastard! What the hell is that supposed to mean?”

“No, forget it. At twenty-three, you’re still at the age when you get embarrassed easily.”

“You little—”

Jin Mukyung’s eyes went wild, and he was just about to charge at me.

At that moment—

Creak.

The door leading to the surface opened, and a servant cautiously poked his head inside.

> **System**
>
> **Level 12: Jang Childeuk**

“Um, Young Masters?”

He was the servant who had brought us meals regularly until about three days ago. Something had clearly happened while we had not seen him. His face was covered in bruises, and four or five of his teeth were broken.

He continued speaking through his damaged mouth.

“The Lesser Family Head is looking for you.”

“……Damn it.”

Jin Mukyung looked back and forth between Childeuk and me, then reluctantly lowered his fist.

* * *

We moved according to Childeuk’s directions. Jin Mukyung walked along with a sour expression, staring only at the ground as if everything offended him. Childeuk kept groaning whenever pain shot through him with each step.

“Ow. Good grief. Urgh.”

“……”

What a pain in the ass.

“How did you get hurt?”

“There was a small misunderstanding.”

That seemed like a fairly serious injury for a small misunderstanding.

In the modern world, there were potions, so there was no ailment they couldn’t cure. Murim was different. I clicked my tongue as I looked at Childeuk’s broken teeth.

“That must hurt.”

“It’s all right.”

Childeuk puffed out his chest with stoic resolve.

“A martial artist of the Jin Family of Taiyuan must be able to endure this much.”

“……”

He had been acting like he was about to die from the pain just moments ago.

But wasn’t this man a servant?

*Come to think of it, his clothes have changed.*

He was wearing the dark navy martial arts uniform worn by martial artists of the Jin Family. I thought he had been wearing a servant’s clothes before.

Noticing my gaze, he smiled shyly.

“Oh. I officially became a martial artist a few days ago.”

“A martial artist?”

Jin Mukyung, who had been walking silently behind us, suddenly spoke.

“Under whose command?”

I might have made a name for myself lately, but I was still nowhere near as famous as Jin Mukyung. Childeuk answered with an awestruck expression.

“I’m directly under the Lesser Family Head.”

“Only specially selected martial artists within our family can serve directly under our eldest brother.”

Jin Mukyung looked Childeuk up and down. His gaze was not contemptuous so much as observant, as though he were estimating Childeuk’s level.

“Your physique is decent, but you don’t seem to have learned any martial arts.”

“Yes. I’m still bewildered myself. I’ve never properly performed even a single form of martial arts.”

Childeuk’s Level, as determined through **Sense**, was twelve. That was high for a servant who had done nothing but carry food, but he was Third Rate by martial-artist standards.

*The First Rate masters directly under Jin Wikyung are at least Level 40.*

What was going on? Did he have powerful backing?

Jin Mukyung seemed to have reached the same conclusion. His brow furrowed.

“You must have good connections. What does your father do?”

Childeuk blinked his large, calf-like eyes.

“He died ten years ago.”

“……”

“……”

“He was a famous herbalist, but he was killed by a tiger.”

For a moment, my vision went hazy. As befitted a Peak master, Jin Mukyung was the first to regain his composure and hurriedly tried to smooth things over.

“Whew. He sounds like he was an excellent man.”

“Even now, I remember him as such an innocent man. He and my mother were very loving, too.”

“Then your mother, perhaps? No, never mind.”

“She’s doing well.”

Just as we let out sighs of relief, Childeuk gazed wistfully at a distant mountain.

“I buried her beside my father, so I’m sure they’re both doing well.”

“……”

“……”

What followed was a march of death. I wanted to run away at full speed, but I gave up after hearing Childeuk muttering to himself.

“Oh, I haven’t seen those flowers in a long time. I used to see them everywhere when I went into the mountains with my father.”

“……”

“……”

If we had walked together for another fifteen minutes, Jin Mukyung might have killed himself. Fortunately, after five minutes that felt like five hours, we reached our destination.

“Oh, you’re here!”

Seeing Jin Wikyung waiting in front of the pavilion nearly brought tears to my eyes. We cried out in voices thick with emotion.

“Hyuung!”

“Hyung-nim!”

Childeuk awkwardly clasped his hands in a formal salute.

“As ordered, I have escorted the Young Masters here.”

Jin Wikyung, who had been hurrying toward Jin Mukyung and me, suddenly stopped and embraced Childeuk.

“Jang Childeuk, a man of benevolence, righteousness, propriety, and wisdom! Is that you, Martial Artist Jang?”

“Yes, sir, Lesser Family Head!”

“You’ve completed a very important mission! Go and rest now.”

What on earth was happening? Jin Mukyung and I stared blankly at the scene.

Then a voice reached my ear through Sound Transmission.

*There was, uh, a minor misunderstanding between me and this fellow…*

“……”

Somehow, I thought I knew who was backing Childeuk.
## Chapter artifact 74

# Chapter 74

“You’ve changed.”

Those were the first words Jin Wikyung spoke after we entered his office. After giving me a careful once-over, he patted Jin Mukyung on the shoulder.

“You’ve worked hard.”

But despite the warm words, Jin Mukyung answered with a sullen expression.

“I almost called a mortician.”

“You really know how to say beautiful things.”

“You—hngh. I’ll let it slide because we’re in front of Hyung-nim.”

“I’m grateful for that too.”

Jin Wikyung gave a short laugh and gestured for us to sit. I took a seat, sipped some warm tea, and looked around.

“This place has changed a lot too. It was a mess the last time I came.”

The office was neat and orderly. When I had visited fifteen days ago, it had been a disaster area covered in all sorts of objects.

Now, even the table that should have been buried beneath stacks of documents was spotless.

“……It was a difficult time.”

Jin Wikyung muttered with a clouded expression.

“But it’s almost over. Just a little longer. If I hold out just a little longer, I can do it.”

“……”

This guy had lost half his mind too. Then again, he had handled that enormous workload alone. It would have been stranger if he were still perfectly sane.

*If it were me, I would have made a midnight escape long ago.*

This applied to me too, but martial artists were, to put it kindly, men of action and, to put it unkindly, blockheads. I wasn’t trying to disparage them. That was simply the truth.

*The family elders were much the same.*

Some of that might have been because the Head Elder had installed puppets, but even the senior members who sided with Jin Wikyung were far from capable administrators.

Despite being born into a prestigious martial family, Jin Wikyung was skilled at administration and outstanding in martial arts. In other words, he was an oddity.

“I want to rest for just one day. Just one day. I want to rest. I want to rest.”

As Jin Wikyung muttered the same words like a man with obsessive-compulsive disorder, Jin Mukyung clicked his tongue.

“It’s a good thing I was born second.”

I nodded.

“Agreed.”

If taking care of my family was already enough to break my back, then if I had entered Jin Wikyung’s body instead of Jin Taekyung’s when I first logged in…

It would have been nothing short of bleak.

The Jin Family of Taiyuan even had hundreds of retainers under its command. The only advantage was that, as the homeowner, I wouldn’t have to worry about my jeonse deposit going up.[^1]

[^1]: Jeonse is a Korean rental system in which a tenant pays a large lump-sum deposit instead of monthly rent.

“The eldest son is supposed to carry a heavy burden.”

Jin Mukyung snorted at my words.

“You’re not qualified to say something like that, so shut up. Isn’t that right, Hyung-nim?”

Jin Wikyung stared at me with moist eyes.

“How does he always manage to pick such touching things to say?”

“No, Hyung-nim.”

“You’ve grown up. You really have.”

“……Am I allowed to curse at him?”

The cold exchange continued, but Jin Wikyung seemed not to hear a thing. He still looked deeply moved as he spread both arms wide.

“Let me hug our youngest just once.”

“Yes, hyung.”

“My youngest!”

Whump!

Jin Mukyung muttered with a face like he had bitten into something foul.

“This damned household. Don’t expect me to come back.”

“Mukyung, you come here too.”

“No. Even if you beat me to death, I’m not going.”

“We’ve all gathered in one place for once, and you can’t grant your only older brother’s request?”

At the wounded tone in his voice, Jin Mukyung flinched.

“……Just this once.”

The moment the words left his mouth, a hand as large as a pot lid pulled Jin Mukyung closer.

Buried against Jin Wikyung’s chest alongside me, he mouthed the words:

*You. Are. Dead.*

*Hmm. I should stay out of sight for the time being.*

Apparently he would be leaving soon anyway. I only had to avoid him for a few days.

*If things get too bad, I can always log out.*

I had completed the Quest, and I had already been thinking about returning soon. There was also the matter of my contract with Team Leader Choi. More than anything, my body was itching to test the newly refined martial arts in a Gate.

“Thank you. I feel invigorated thanks to you two.”

After ending the emotional embrace, Jin Wikyung dabbed at his eyes with his sleeve.

“There’s just so much work. So much work.”

“……”

He really must have been suffering.

The tears of a human weapon made me solemn in spite of myself. I patted Jin Wikyung on the back.

“Keep your spirits up.”

Jin Mukyung, who had been wearing a death mask until moments ago, also gave Jin Wikyung a sympathetic look.

“Hyung-nim. If it’s really that difficult, take this guy and put him to work.”

“……?”

What the hell was he talking about? I asked, dumbfounded.

“Usually, at a time like this, shouldn’t you at least say, ‘I’ll help,’ even if you don’t mean it?”

Jin Mukyung answered confidently.

“A martial artist does not make empty promises.”

“Then why drag me into it while I’m sitting here?”

“You have plenty of time.”

“I don’t!”

“I have even less. I need to train. Besides, I’m hopeless at looking over documents.”

“I was a seventh-tier student!”

“What nonsense are you talking about?”

“I mean I was terrible at studying.”

Jin Mukyung thought for a moment, then frowned.

“A completely useless bastard. Hyung-nim, he does have good strength, so he would make an excellent laborer. I’ll be going now.”

“Wait.”

The nape of the man who had turned around so quickly was caught by a giant forepaw—no, hand. Its owner was, naturally, Jin Wikyung.

“Where do you think you’re going?”

“Pardon?”

“You have to hear why I called you two before you leave.”

“……What is it?”

An uneasy expression spread across Jin Mukyung’s face. I had no mirror, but I was probably making a similar face.

*I smell trouble.*

I was uncannily good at recognizing this kind of smell.

The smell of bad luck. The feeling that something bothersome was about to happen. Jin Wikyung’s next words turned that premonition into certainty.

“You’ll have to go to the Mount Heng Sword Sect.”

Ding.

> **System**
>
> - A Quest has been forcibly created.

“……”

Goddammit. Now it doesn’t even ask.

* * *

I stared at the translucent Quest window.

> **Quest**
>
> **[Yesterday’s Enemy, Today’s Ally]**
>
> Now that all the truth has been revealed, the Mount Heng Sword Sect is not an enemy but an ally with whom you must join hands. Invite them to the Jin Family of Taiyuan for the upcoming New Year’s Day.
>
> **Grade:** First Rate
>
> **Restriction:** Jin Taekyung
>
> **Mission:** Deliver the invitation (Incomplete)
>
> **Reward:** ???
>
> **Failure:** None

After reading it two or three times, my initial bewilderment had mostly subsided.

*Not bad.*

The Quest difficulty was not high, and there was no failure penalty. It was a simple mission that would end once I delivered the invitation.

More importantly…

*Logout.*

Ding.

> **System**
>
> - Would you like to log out?

That meant there was no problem with logging out. The Quest had been forced on me, so it still felt unpleasant, but this much was acceptable.

*Not that I’m in a position to refuse anyway.*

Unlike me, who had already accepted reality, Jin Mukyung was resisting with all his might.

“So……”

Jin Mukyung struggled to continue.

“You’re saying we should invite the Mount Heng Sword Sect for the coming New Year’s Day?”

Jin Wikyung answered.

“Yes. They are guests we cannot afford to miss.”

“Then why do we—or rather, why do I—have to go?”

“……”

Look at him, struggling to exclude himself.

Still, I agreed with part of his question.

*Why us?*

Jin Wikyung’s answer only made the question larger.

“The Sect Leader of Mount Heng Sword Sect requested it personally.”

I blurted out a question before I could stop myself.

“The Sect Leader?”

I had watched the Blood Wolf Sword Lee Cheonbaek die right before my eyes. Lee Seogeun, the Second Young Master, had been poisoned, and the Young Sect Leader whom I had never even met had reportedly died an absurd death during a mounted-bandit raid on the undefended sect.

*I thought the Mount Heng Sword Sect’s main force had also been wiped out at Eight Spring Gorge.*

But the Sect Leader?

Jin Mukyung’s reaction was not much different.

“The damage must have been severe. I only heard about it through rumors, but wouldn’t it be understandable if they closed the sect’s gates?”

Jin Wikyung shook his head.

“They were once one of the pillars of Shanxi Murim. Don’t underestimate their strength. If they have a rallying point, they can aim for a revival.”

A rallying point.

The new Sect Leader of the Mount Heng Sword Sect—the person who had requested that Jin Wikyung send Mukyung and me—seemed to be that new rallying point. I asked:

“Who is it?”

“Lee Seowol.”

“Lee Seowol? Lee Seowol……”

It was the first time I had heard the name. Judging by her surname, she seemed to have some connection to Lee Cheonbaek.

“You don’t remember the name?”

“A hidden son? A distant relative? I’m not sure.”

“As expected, you don’t remember.”

“Pardon?”

What did he mean, I did not remember?

*Is she someone I know?*

As I tilted my head, Jin Wikyung looked at me strangely.

“The new Sect Leader of the Mount Heng Sword Sect is a woman. She is Lee Cheonbaek’s third child, the one and only younger sister of the deceased Young Sect Leader and Lee Seogeun.”

At that moment, a fragment of memory flashed through my mind.

The scene in my memory was the main arena. The actor was Lee Seogeun. His face was flushed bright red as he shouted at me.

*You shameless bastard! You tore my sister’s clothes and tried to violate her!*

Ah!

“Could it be her?”

“That’s right.”

“……Damn it.”

Only Jin Mukyung, who had no idea what we were talking about, blinked both eyes.

“What does that mean? Hey, do you know her?”

“Uh, well. You could say I know her, and you could also say I don’t.”

“What the hell does that mean? So what exactly is your relationship with her?”

“Hmm.”

*A former girlfriend whose face I don’t even know? Or a honey-trap scammer?*

*One thing is certain.*

Neither of us was particularly happy about meeting the other.

I let out a deep sigh.

* * *

To cut to the end of the story, Jin Mukyung agreed to go to the Mount Heng Sword Sect as well. Jin Wikyung had used the masterstroke he had been saving.

*I heard the Mount Heng Sword Sect has a lot of martial arts manuals…*

*Even if they do, what good is that? It’s not like I can read them.*

*It does matter.*

*Pardon?*

*The new Sect Leader has you figured out. She said she would be willing to show you some of their Peak martial arts if you came.*

*……When are we leaving?*

*Right now.*

Everything moved at lightning speed. It had been only two hours since we boarded the four-horse carriage after receiving Jin Wikyung’s farewell.

Jin Mukyung sat across from me and grumbled.

“A carriage? It’ll take an age just to get there.”

The land was so vast that even making a rough estimate, it would take three days to reach Eung-hyeon (應懸), where the Mount Heng Sword Sect was located.

For Jin Mukyung, who wanted to see the Mount Heng Sword Sect’s Peak martial arts as soon as possible, three days was an eternity.

“Hey, coachman, can’t you go any faster?”

A reply came from the driver’s box beyond the partition.

“First of all, I’m not the coachman. And no, I can’t go any faster. You may not know this from inside, but it’s freezing outside and I’m about to die of hypothermia. Anyway, that’s how things are.”

“Use the whip and spur the horses on! A coachman should be able to do at least that much.”

“I’ll say this one more time: I’m not the coachman. And the whip is frozen solid, so it would be more accurate to call it an icicle. If I jab the horses in the rear with this icicle, I think they’ll get very angry……”

“What? Why is someone who isn’t a coachman sitting there?”

“Before we left, you shouted that the attendants were getting in your way and ordered all of us to get lost. The coachman got lost too.”

Jin Mukyung thought about it carefully, then smacked his forehead.

“Oh, right.”

“……”

As expected, this guy was not normal either.

“Then who are you?”

Recalling the law of conservation of idiots, I answered.

“Hyuk Mujin.”

“Who’s Hyuk Mujin?”

“You’ll know when you see his face. Hey, Mujin!”

The partition dropped, revealing Hyuk Mujin’s face, which was covered in frost. His teeth chattered constantly as Jin Mukyung studied him carefully. Then Mukyung snapped his fingers.

“Oh, that guy.”

Hyuk Mujin answered curtly.

“Yes. I’m that guy.”

“Why didn’t you leave too? Why not bring the coachman instead?”

As if he had been waiting for that question, Hyuk Mujin proudly puffed out his chest.

“I only obey my squad leader’s orders.”

“Squad leader?”

“The Third Young Master.”

Jin Mukyung’s head snapped toward me.

“Did you call him?”

“No. He was already there without me calling him.”

“That’s what he says?”

Hyuk Mujin looked back and forth between us with a wounded expression.

“You two really are brothers, I suppose.”

“Did you say your name was Hyung Mujin? Explain exactly what that means.”

Jin Mukyung spoke in a sharp, offended voice, but I yawned hugely.

Hyuk Mujin clowning around was nothing new; when it came to dealing with that, I already had a full sixty-year cycle of internal energy.

“It’s not Hyung Mujin. It’s Hyuk Mujin. I’ll try jabbing the horses’ backsides with this thing, whether it’s a whip or an icicle.”

Tap.

Jin Mukyung glared at the partition, which had quickly slammed shut, then sighed and settled back into his seat.

“I shouldn’t have expected anything. If the water upstream is filthy, the water downstream can’t be clean either…… What are you doing?”

I wrapped a fur hide around my body as I answered.

“I’m going to circulate my qi.”

“Really?”

“Yeah. Circulate my qi.”

“Then why does it look to me like you’re getting ready to sleep?”

“That’s your imagination.”

“Then why are you covering yourself with a fur hide?”

“I get cold easily.”

I deliberately sat cross-legged. I also pressed my body tightly against the carriage wall so I would not fall over.

*I can’t entrust my precious body to that guy.*

I absolutely refused to return and find that my arms or legs had been broken. It would be much better to make sure he could not touch me at all.

“You know what happens if you touch me, right? Huh? Do you know what qi deviation is or not?”

“Seriously, this bastard’s been getting on my nerves for a while now…”

The moment Jin Mukyung raised his fist, I hurriedly closed my eyes. To anyone watching, it would look as though I had begun circulating my qi. As expected, no fist came flying at me.

All right, then. Now……

*Logout.*

Ding.

> **System**
>
> - Would you like to log out?

There was only one possible answer.

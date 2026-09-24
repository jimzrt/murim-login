# Checkpoint Review — 990–994

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

# Chapters 990–994

## Plot

Peng Cheolhu’s death and the Eight Heavens Blood Calamity spur widespread grief and mobilization against Dark Heaven. In Qinghai, Cheongpung encourages a boy who admires Jin Taekyung, then is scolded by the Slaughter Saint for wandering off.

Taekyung awakens from a dream of a father comforting a child named Taekyung. He recognizes it as a memory of the original Jin Taekyung, the former owner of his body. He and Jeok Cheongang privately consider whether the original’s consciousness remains within him, but cannot determine the truth. After Jeok confirms Peng died smiling, Taekyung checks the System and receives rewards for completing the internal-energy transfer, reaching Supreme Peak, and undergoing Bone Transformation.

A painful fragment of memory brings back an unknown voice telling him he made a good choice, “just like back then.” The System assigns him the forced Unknown Voice Quest: continue surviving. Taekyung suspects the Martial God may be the voice’s owner and possibly a System user, and wonders whether the Martial God and Cheon Taemin are separate people. He tries to log out to investigate Cheon Taemin and the Doppelganger’s final words, but the System disables Logout for Temporary Maintenance. Jin Wikyung enters his room looking grave.

## Continuity

- Peng Cheolhu is dead; his death and the Eight Heavens Blood Calamity are driving widespread mobilization against Dark Heaven.
- Taekyung has absorbed the internal energy passed on by the Heavenly Power Demon and Peng Cheolhu, fully opened his Middle Dantian, reached Supreme Peak, and completed Bone Transformation.
- Memories of the original Jin Taekyung have surfaced. Whether the original’s consciousness remains within Taekyung is unknown; he and Jeok Cheongang will discuss it privately.
- The System’s forced Unknown Voice Quest has the objective “continue surviving.” Its reward and failure conditions are unknown; it says Taekyung may meet the voice’s owner in the near future.
- Taekyung suspects the Martial God may have been a System user and may be the unknown voice, but these are unconfirmed hypotheses. His questions about the Martial God, Cheon Taemin, and the Doppelganger’s final words remain unresolved.
- Logout is temporarily disabled after a System error, leaving Taekyung in Murim. Jin Wikyung has entered his room with a grave expression.

## Translation Decisions

- Render 팔천혈겁 as “Eight Heavens Blood Calamity.”
- Render 알 수 없는 목소리 as “Unknown Voice” for the System Quest title.
- Render the System’s temporary service interruption as “Temporary Maintenance.”
- Render 등봉조극 (登峰造極) as “Supreme Peak” when naming the realm.
- Preserve the boy’s distinction between the respectful 그분 and the less respectful 그 사람 when he insists Jin Taekyung be spoken of with respect.

## Durable state

{
  "active_continuity": [
    "Taekyung has fully opened his Middle Dantian, reached the Supreme Peak realm, completed Bone Transformation, and absorbed internal energy passed on by the Heavenly Power Demon and Peng Cheolhu.",
    "Taekyung is resolved to repay the dead by helping bring about the peace they wanted; he aspires to reach the upper dantian.",
    "The System has forced Taekyung to proceed with the Unknown Voice Quest, whose objective is to continue surviving.",
    "Taekyung suspects the Martial God may have been a System user, or Player, and may be the unknown voice's owner; these are unconfirmed hypotheses.",
    "Logout has been temporarily disabled following a System error, preventing Taekyung from returning to the modern world as planned.",
    "Taekyung intends to investigate Cheon Taemin and the Doppelganger's final words when he can return to the modern world."
  ],
  "continuity_sources": [
    993,
    994
  ],
  "open_questions": [
    "Who was the unknown voice, and will Taekyung meet its owner?",
    "Was the Martial God a System user, and is he connected to Cheon Taemin?",
    "What did the Doppelganger mean by its final words, and what was it trying to accomplish?",
    "What are Dark Heaven and the Lord of Heaven planning?",
    "What does the Bow Saint know about the chosen one?"
  ],
  "safe_through": 994,
  "temporary_decisions": [],
  "version": 1
}

## Reading copies

## Chapter artifact 990

# Chapter 990

The Thunderbolt Saber King, Peng Cheolhu.

The news that yet another giant born of the Great Faction War—the Grand Family Head of the Hebei Peng Family—had fallen spread like a raging wildfire.

“I believed he of all people would hold firm… And yet it’s come to this.”

“Even so, who could’ve imagined the Saber King would meet such a pointless end?”

“Pointless? Don’t ever say that in front of me again. Great Hero Peng held fast to his chivalrous spirit until the very end.”

“Enough. You think he said that because he didn’t know? He’s just heartbroken.”

“I know. Damn it. I know that, too.”

The martial artists who received the unexpected and tragic news could not hide their grief.

To them, the title of one of the Ten Kings carried a meaning unlike any other.

But even Hong Dao, the Dharma King who had earned everyone’s respect.

Even Tang Taesang, the Poison King who had driven countless members of the Demonic Cult to terror.

At last, even the Thunderbolt Saber King—the man who had been the de facto leader of the Ten Kings, apart from the overwhelming presence of the Fire King, Jeok Cheongang—had met his death.

And their deaths had not been from old age or illness.

“Don’t forget. They died honorably, fighting for justice and chivalry to the very end. It’s our duty to avenge them.”

The successive deaths of old masters who had been symbols of the orthodox Murim and paragons of justice.

The martial artists of Murim layered anger over their grief.

To avenge those who had left them.

To defeat the new enemy, which had emerged for the first time since the Demonic Cult and revealed a power more threatening than ever.

“Who will stand against Dark Heaven!”

“Take up your swords! For the Nine Provinces, for justice and chivalry—rise up and fight those fiends!”

The rousing shouts that rang out from streets everywhere had become an everyday occurrence.

Learning from the Murong Family’s example, Sect Leaders and Family Heads of various factions met often and put old grudges behind them. Young people, their blood burning with fervor, swung weapons they had never so much as bloodied until their palms split.

Even a stone leaves a mark when it moves. Imagine how much more so a mountain.

The bloody battle in Shanxi Province, fought across a narrow gorge.

The incident that came to be known as the Eight Heavens Blood Calamity, and the death of the Thunderbolt Saber King, had been the final sparks that set everything ablaze.

Even those who had feared Dark Heaven’s actions—stirring up bloodshed all over the world despite its full strength still being unknown—and martial artists caught between the orthodox and unorthodox factions, who had once been lukewarm about opposing it, now understood.

The razor-sharp blade in Dark Heaven’s hands was aimed not only at the orthodox Murim, but at the entire world.

And the consequences had long since spread far beyond the confines of Murim.

“So, who are you, and where did you come from?”

“I’m Jang-pal, from Jeong Family Village.”

“Jang-pal? You say you’re from Jeong Family Village, so why is your surname Jang?”

“Pardon?”

“Why are you called Jang-pal?”

“Oh, well…”

“Well, what?”

“My father’s from somewhere else.”

“Somewhere else, huh? So he married into the family and settled in Jeong Family Village.”

“Yes, yes. That’s right.”

“How old are you?”

“I’ve come of age this year.”

The low-ranking official assigned to recruit soldiers looked the young man—or rather, the applicant who ought to have been called a boy—up and down.

“Come of age?”

“Yes, sir!”

“I see. Then what is your mother’s full name?”

“What?”

“Listening to you, your face looks kind of familiar. I feel like you might be someone I know. You never know—it could work out well for both of us. If you’re right, I can send you somewhere you’ll have a good chance to earn military merit.”

At the official’s coaxing tone, the boy’s eyes lit up.

“Y-you really mean it?”

“Of course. So, what’s your mother’s name?”

The boy hesitated for a moment, but not for long.

He might not have his family’s permission, but the sense of justice in his heart and his dreams of making his mark on the world had never burned brighter.

If his parents were acquainted with the official in front of him, this was the perfect chance to be posted to a good battlefield, earn brilliant merit, and become a young general.

*Me, too. I’ll definitely become like him.*

He had already made up his mind.

Thinking of the idol he had never once seen in person, the boy found his courage. He gripped the bamboo spear he had clumsily whittled himself and opened his mouth.

“Th-the second daughter of the Oh family from the house by the persimmon tree. She said people nearby would know her…”

“Go home.”

“What?”

“Your father’s a Jeong, your mother’s an Oh, so why do you live in Jeong Family Village?”

“……!”

“What, still got something to say?”

The low-ranking official glared at him with sharp eyes, as if he already knew everything. The boy stiffened, then barely managed to force out a reply.

“Actually, my entire family came from somewhere else…”

“What are you waiting for? Drag this punk out!”

“Gah, sir! No! You can’t! You’ll really regret turning me away!”

The boy’s eyes widened with fierce determination. Deeply moved by the sight, the low-ranking official gave an order to the guards holding the boy by both arms.

“Give him three swats on the rear and toss him out. Come of age, my ass. You little brat—first you lie, and now you’re glaring at your elders?”

“Siiir!”

His desperate cries changed nothing.

Ever since the Emperor’s proclamation had spread throughout the land, government offices in every province had been packed with people who couldn’t resist their dreams of rising in the world and the fire in their veins.

The low-ranking official, who was in danger of dying from overwork before Dark Heaven ever got to him, had reached the end of his rope with boys trying to enlist by lying about their age.

“Give him two more!”

“Nooo!”

“Yes!”

In the end, the guards gave the boy a sound kick to the rear and drove him out. The applicants, whose line stretched all the way outside the government office, watched him go and murmured among themselves.

“He looks younger than my little brother.”

“Still, the kid’s got a decent sense of justice. Shame his head’s a complete rock.”

“But where did he say he was from again?”

“Doesn’t matter. It was obviously made up.”

“No, I still need to know.”

“Why are you so hung up on it?”

“I made mine up, too.”

“……”

“I can’t have the place name overlapping by accident. They’ll catch me, and I’ll end up like him.”

“…How old are you, by the way?”

“Sixteen.”

“Cut the crap. You’ve got the face of a grizzled veteran.”

“Thank you, sir. Looks like I’ll get through safely. And please keep this a secret.”

“……Wait, you weren’t joking?”

Just as everyone was falling into a pit of shock, an applicant with an old-looking face spoke to the boy as he staggered to his feet.

“How old are you?”

The boy, staring blankly at the government office, answered.

“Sixteen.”

“Same age as me. Since we’ve met, let’s drop the formalities.”

“Not even a stray dog would believe that. I’m in a lousy enough mood already.”

“I’m serious.”

“I’m not falling for… that, sir.”

“By the way, where’d you get that spear?”

The boy fidgeted before answering.

“I whittled it myself…”

“People our age usually use swords, don’t they? Like me.”

In an instant, the boy’s complicated expression twisted.

“Who the hell says that? The spear is the king of all weapons.”

“You’re finally talking casually. And I never said swords were the best. I just said they’re what people usually use.”

“Oh.”

“Seeing you get worked up over weapons tells me one thing. You came here because you want to be like ‘that person,’ didn’t you?”

At the knowing question, the boy hesitated for a moment, then answered in a much softer voice.

“Show him some respect.”

“What?”

“Don’t call him ‘that person.’ Speak of him with respect.”

The boy’s dejected look was nowhere to be seen now.

As if nothing had happened, he seemed to have forgotten he’d just been thrown out of the government office. His eyes brightened as he continued.

“Blazing Flame Divine Dragon Jin Taekyung. I’m going to be like him. I mean it!”

Everyone had a goal they wanted to reach.

For the boy, Jin Taekyung was that goal.

A young hero of the martial world, watched by the entire land, and a noble marquis personally appointed by the Son of Heaven.

He admired him. He respected him.

When he’d come here with a proud stride, he’d been full of confidence that before long he’d stand shoulder to shoulder with him.

Of course, reality had kicked him in the rear and thrown him out.

“Damn it.”

The boy lowered his head gloomily.

Then a strange voice suddenly rang out from somewhere.

“Wow! That’s so cool!”

The boy looked up and blinked at the speaker. Everyone waiting outside the government office did the same.

*Who’s that?*

*When did he show up? I don’t think he was here a moment ago.*

*Huh. Or was he?*

*Now that I think about it, maybe he was here the whole time…*

Their exchanged glances were full of bewilderment and questions.

But before anyone could make sense of it, the young man who had suddenly appeared in front of them was smiling brightly at the boy.

“I heard from my grandfa— No, from someone else. They said it’s good to have a goal you want to achieve!”

“Y-yes?”

The boy stared at the young man, bewildered.

Maybe it was the long robe caked in dust. His appearance seemed not just ordinary, but downright shabby.

Perhaps that was why the shock of his sudden appearance and his attempts to strike up a conversation soon gave way to an inexplicable sense of familiarity—not only in the boy, but in everyone else, too.

It was like… like…

Right.

*That one not-quite-right older guy every neighborhood seems to have.*

Everyone thought the same thing at that moment, and couldn’t help but believe it.

Just look at that completely spotless, pure-white smile.

There wasn’t a speck of malice in his eyes. They were clearer than a stream, and then he grabbed the boy’s hand and shook it over and over—the way a little kid might.

“That’s so cool! You want to become the Blazing Flame Divine Dragon! That’s amazing!”

The boy, eyes wide and both arms trapped in the man’s grip, managed to pull himself back to reality thanks to the ache spreading through his shoulders.

“P-please let go.”

“Oh, sorry. I got excited. Did I hurt you?”

They said you couldn’t spit in a smiling face. Looking at that genuinely worried expression, the boy couldn’t bring himself to complain.

“…No, I’m fine. But who exactly are you?”

“I’m just a passing hero. Someone who wants to save the world, like you, Young Hero!”

With his chest puffed out, he proclaimed this proudly. The boy and everyone else reached the same conclusion.

*Yep. Definitely not quite right.*

And, proving their suspicions, the young man kept babbling about whatever came to mind, oblivious to the strange atmosphere.

“But, Young Hero, if you want to become like the Blazing Flame Divine Dragon, why come to the government office? Wouldn’t it be better to go straight to the Jin Family of Taiyuan?”

“Oh, it’s just so far away. I’ve never been more than a hundred li from home in my life. How could I…”

“It’s far, but it’s not that far.”

“It’s not that far? From here in Qinghai to Shanxi?”

“It goes by faster than you’d think. As long as you keep running hard and don’t give up.”

Snickers broke out here and there.

From Qinghai Province to Shanxi Province was nearly ten thousand li, give or take a little exaggeration.

Even old peddlers who roamed the land with a few packs on their backs, and even the major Escort Bureaus, avoided taking on journeys that long whenever possible.

They were that grueling and mind-numbingly dull.

If even people who made their living on the road felt that way, what about the people of Qinghai Province, on the far western edge of the realm?

It was the sort of nonsense only a fool would say.

Of course, to the boy who dreamed so wildly that others laughed at him, it sounded a little different.

“As long as you don’t give up and keep at it?”

“Yep. That’s right! And even if the Jin Family of Taiyuan is too far away, there are other options. For example…”

“Do you mean the Kunlun Sect?”

“Oh, you know about it?”

“Yes. I’m from around here, of course I do. And I know I’m too old to join the Kunlun Sect.”

The boy let out a deep sigh and continued.

“But I don’t want to join the Black Dragon Demon Gate. I know it’s part of the Murim Alliance, but it’s still an unorthodox faction. And it seems like there are still some pretty bad rumors about them.”

“Hmm. Then what about the other sects…”

“They’re all more or less the same, in the end. I might as well join the military, learn strategy, and someday become a general leading an army. That would bring me at least a little closer to his fame.”

After pouring all that out, the boy suddenly let out a self-deprecating laugh.

He wondered what good it did to tell all this to a complete stranger who looked so dim-witted.

“I should get going. Maybe I’ll see you again sometime.”

“Hey, wait a second.”

The boy kept trudging off despite the young man calling after him.

The young man watched him leave with a dejected expression. Then a round face popped up beside him.

“Hyung, what are you doing here? I’ve been looking all over for you.”

People assumed the child with bright, alert eyes had come looking for the not-quite-right older guy. They chuckled and lost interest.

Little did they know that, at that very moment, the adorable child was jamming a sinister voice into the young man’s ear—one nobody else could hear.

—Didn’t I tell you? Disappear without a word one more time and I’ll kill you. I don’t give a damn if you’re the Sword Saint’s Disciple.

Cheongpung answered innocently.

—Sorry. I was only going to be gone for a little while.

—Did you hold a grudge against this old man in a past life or something? Why do you keep doing this?

—I had a reason.

—Then tell me.

—I ran out of candied hawthorn skewers[^1].

—You little shit…!

As he listened to the Slaughter Saint’s deep sigh, Cheongpung watched the boy’s retreating back.

Then he thought of someone and smiled to himself.

—Hehe. Did I ever tell you? When my Benefactor first saw me, the candied hawthorn skewers—

—Shut up. Please.

In Qinghai Province, the Slaughter Saint was suffering.

[^1]: *Bingtanghulu* are fruit skewers coated in hardened sugar, traditionally made with hawthorn berries.
## Chapter artifact 991

# Chapter 991

Whenever I lost consciousness or fell into a deep sleep, getting caught up in some kind of dream was nothing special anymore.

As someone once said, dreams were a window into the mind. Worries I hadn’t managed to shake off and memories that still lingered would get mixed and mashed together, then surface as the illusion we called a dream.

In the end, everything in this world had a cause or a reason. Dreams were no different.

Right.

That had to be true.

At least, as far as I knew.

But then why…

*Why am I having this dream?*

I slowly blinked in the blur of my vision.

Everything was hazy.

Unlike my other dreams, which had been horrifyingly vivid, I couldn’t even make out the illusions around me.

But when someone’s voice suddenly reached me, I finally understood the source of this haze.



*You look awfully sleepy, kid.*



Sleepy.

As the realization finally sank in, I lifted my head.

No—“my head was lifted” might be more accurate.

The eyes that had been blinking from the start, that movement of my head, and even the voice slipping between my lips now weren’t under my control.



*Yeah. I’m sleepy.*



The voice sounded muffled, as though I were underwater, but one thing was clear.

I was a child.

A child so young that hearing myself whine didn’t feel strange at all.

That answered one question, but a new one quickly took its place.

Who was the unfamiliar man whose voice was patiently indulging the child’s whining?

*I’ve never heard his voice before.*

A voice wasn’t exactly an ID card. I couldn’t be expected to recognize someone the instant I heard them. Still, anyone who showed up in my dreams ought to be familiar to me.

But everything seemed unfamiliar now.

The voice reaching me through my blurry vision. The illusion playing back in slow motion, like a TV screen full of static.

And when I heard the child’s words slip between lips that weren’t mine, I understood where this strange sense of unfamiliarity came from.



*Dad. Can I go to sleep?*



If I’d been able to speak of my own accord, I would’ve let out a groan without realizing it.

The truth I’d stumbled across was that astonishing—and that hard to understand.

*Dad?*

No. That couldn’t be.

I could turn over and shake out the oldest drawer of my memories, and still find no memory like this.

The voice of my father that remained in my mind, however faint, was nothing like the man’s voice coming through my hazy vision.

So this was—

*Not my memory.*

Just then, an inexplicable chill ran down my spine.

The unfamiliar man, the one the child had called Dad, spoke into my ear.



*Have a good dream, son.*



A warm hand stroked my hair. His voice was gentle.

As my vision plunged into darkness, the man’s final words rang faintly in my ears.



*…a.*



It was faint, but I’d heard it clearly.

A father’s voice speaking to his son. His son’s name.

And at that moment, my thoughts ground to a halt with the shock of something I’d never expected.

Fwoosh.

Light poured down from beyond the pitch-black darkness, wrapping around the child lost in deep sleep.

No—around me.



* * *



If someone asked what I saw first whenever I regained consciousness, I’d say the ceiling.

Or Hyuk Mujin, snoring in a corner of the room under the pretense of standing guard. Or Jeok Cheongang, who’d stayed by my side until I woke up.

But this time, it was none of those.

“Hah… hah…”

I shot upright like a spring and sucked in ragged breaths.

Was this what it felt like to be on the verge of suffocating?

The vision I’d only just regained wavered like melting candle wax, and the voices coming from all around me rang in my ears like thunder.

“Medicine King…! Come! Hurry!”

“…tain, Captain!”

“What the hell…!”

Was I still dreaming? Or was this real?

I couldn’t tell one from the other. Caught in confusion, I kept batting away the hands reaching for me on instinct.

Then someone grabbed me by the shoulder.

Firmly.

Even in the middle of all that, I could feel the strength in that hand with perfect clarity.

A faint pain came with it, along with an unfamiliar warmth.

Shaa…

My whole body, tense as a board, slowly relaxed.

Only then did I realize whose energy was flowing along the acupoint pathways known to just two people in this vast world—the Extreme Yang qi flowing through me.

“...Old Master.”

At the words I breathed out along with the breath I’d been holding, a voice I knew all too well answered me.

“Stay just as you are for a moment. Just a moment.”

I closed my eyes as Jeok Cheongang told me to.

I reminded myself that this place I was in was real, not an illusion, and slowly calmed my heart, which was pounding without pause.

How much time passed like that?

At last, I opened my eyes and faced a world that was both quiet and clear.

And a familiar face looking at me with concern.

“You fool. Are you finally coming around?”

I hesitated a moment before answering his blunt question.

“More or less.”

“So you’re not quite there yet.”

“Could you hit me hard once?”

“What?”

“Just once. Don’t hold back at all. Put your whole heart into it.”

“……”

“Please.”

At my solemn request, Jeok Cheongang sighed and raised his fist.

“Fine. You asked for it.”

Whoosh.

White flames sprang up in an instant, wrapping around his tightly clenched fist.

As I watched him prepare to fire off a move from the Flame-Extinguishing Divine Fist without another word, I calmly spoke up.

“Wow, that’s hot.”

“What kind of nonsense is that? The Fire Gate Clan’s martial arts have always been like that.”

“If I can feel how hot it is, I think I’ve definitely come to my senses.”

Jeok Cheongang shook his head.

“Doesn’t look like it to me.”

“I’ve changed my mind. I think I’m all right.”

“You said to put my whole heart into it.”

“Not quite that much.”

“Weren’t you the one who asked?”

“If you were going to take me that seriously, you should’ve refused three times first. Isn’t that just good manners?”

“You lunatic. Do you think I’m Zhuge Cheongang? Quit flapping that mouth and brace yourself.”

Despite his words, Jeok Cheongang lowered his fist. He flicked his hand, and a water bottle on the bedside table shot toward me.

“What are you waiting for? Drink something.”

“Thank you.”

I drained the full bottle in one go without stopping to breathe.

The cold water ran down my parched throat, and at last I felt like I could breathe again.

“Whew.”

“Well? Can you tell whether you’re dreaming or awake now?”

“More or less.”

At the same answer I’d given before, Jeok Cheongang clenched his fist again.

“And now?”

“...Whoa, I’m awake! Definitely awake! The whole world is beautiful! I’m so happy to be alive!”

“Good. You’re finally back to the reckless little brat I know.”

“Was I not a moment ago?”

“Do you really have to ask? You woke up and immediately started thrashing around like you couldn’t tell up from down, so I sent everyone else out.”

“Hmm.”

Now that I thought about it, that did sound familiar.

I’d been overwhelmed by confusion, fighting against the hands trying to hold me back.

And I had undeniable proof right there in front of me.

“What a mess.”

I muttered as I looked at the fragments scattered everywhere, their original forms lost. Jeok Cheongang nodded emphatically in agreement.

“It’s a hell of a mess.”

“Did I do this, too?”

“You’re half right and half wrong.”

“What do you mean…?”

“Your eldest brother was the one who made a scene. Built like a mountain, bawling his eyes out and insisting he couldn’t leave. I had no choice but to deal with him myself.”

I stared at Jeok Cheongang, eyes wide.

“Did you kill him?”

“Want me to kill you first?”

“No. I’m joking.”

“I’m not.”

“Oh.”

A long time ago, I would’ve been clutching my ass, which came equipped with a built-in stick of dynamite, and counting down. Not anymore.

I gave a quiet laugh without answering. Jeok Cheongang clicked his tongue.

“Damn it. Now you really do think I’m worth less than dirt.”

“Come on, you’re always snapping at me. You know I know better.”

“Know what, my ass. More importantly… what caused this?”

The question came with a brief pause, his voice trailing off.

I opened my mouth, feeling the sweat that had soaked my back.

“It was just a dream.”

“What sort of nightmare was it?”

“No, I wouldn’t call it a nightmare… I don’t know. It was a strange dream I can’t really describe.”

Even as I answered, an odd feeling crept over me. I frowned.

*What is this?*

The situation felt strangely familiar.

But the sense of déjà vu that had come over me vanished when Jeok Cheongang spoke again, his voice grave.

“Tell me more. That nightmare might have been a trace of the Heart Demon inside you.”

I pushed aside my brief hesitation and answered.

“I don’t think so. It was just a memory.”

“Even an unhappy memory can leave a trace of the Heart Demon. I’ve seen people who were trapped by such a past until it brought them to ruin.”

I knew what Jeok Cheongang was worried about.

In modern terms, it was something like trauma.

For a Murim martial artist to break past their limits and reach the highest realms, powerful internal energy and martial arts weren’t enough.

They needed spiritual insight gained through training the mind.

Whether good or evil, they had to gain an understanding of their own before they could keep walking that path.

And for anyone who’d begun that mental training, an illness of the heart left untreated could be devastating.

*Like how Old Master suffered from the infirmities of old age after losing Jopil. No—Jangcheon.*

That was why Jeok Cheongang’s serious concern wasn’t an overreaction at all.

People knew the Fire King Jeok Cheongang for a temper like hellfire, but beneath that burned the caution and wisdom he’d honed over a lifetime.

But this time, I could answer his concern without hesitation.

“It’s not the Heart Demon.”

I met Jeok Cheongang’s gaze as his expression hardened, then continued slowly.

“Because the memory I saw in the dream wasn’t mine to begin with.”

“What do you mean, it wasn’t yours?”

I swallowed a breath that had begun to tremble.

And at the same time, I remembered.

The man’s voice, faintly seeping into the ear of a child falling into a deep sleep in that hazy dream.

No—the voice of another father.



*Have a good dream, my son… Taekyung.*



It was my memory, and at the same time, the memory of someone I could only call *you*.

Jin Taekyung, Third Young Master of the Jin Family of Taiyuan.

The family’s disgrace, and the original owner of this body.
## Chapter artifact 992

# Chapter 992

The fact that Jeok Cheongang was the only person left in the room was a huge relief.

He already knew the truth about me, and he hadn’t dismissed the things I’d said in a trembling voice as the ramblings of some lunatic.

“……So that was the last of it?”

“Yes. After I woke up, well, you know the rest, Old Master.”

Was it the shock of finally facing the truth?

Or had something actually changed inside me?

I didn’t know the exact reason, but I’d been left to flounder alone in a state of utter confusion.

No—maybe I still was.

“Damn it. That’s downright bizarre.”

Jeok Cheongang muttered like a groan, then studied me with a cautious look.

“What is it?”

“No, well… Has anything changed?”

“Changed? Of course.”

“What!”

Jeok Cheongang cried out in shock.

I went on, feeling the unpleasant stickiness of cold sweat that still hadn’t completely dried, and—separately from that—power surging through my whole body.

“Well, my mood’s in the gutter, but I feel great physically.”

Jeok Cheongang swallowed.

“Th-then?”

“That’s it.”

“……That’s all?”

“Yes.”

Jeok Cheongang stared at me with a flat look, then let out a sigh.

“Fine. In a situation like this, that’s probably for the best.”

I secretly agreed.

As awful as I felt, nothing had happened to me. Not yet, anyway.

The bigger problem was what on earth this incomprehensible phenomenon meant.

“Just to be safe, let me ask you something. Has anything like this ever happened before?”

“No. Not once, from the beginning until now.”

I answered firmly, then added:

“That’s what makes it so strange. If this is a sign of something to come…”

“Don’t say that. Words have a way of coming true. Keep that rotten-luck talk to yourself.”

“Seeds don’t need someone to water them before they sprout. It’s a hundred times better to predict what we can and prepare as much as possible.”

“……Even in a situation like this, you’ve got a silver tongue.”

Jeok Cheongang said it with a sour expression, but he didn’t exactly argue with me.

With his far greater life experience, he must have known deep down.

That what was going to happen would happen, one way or another.

And that this wasn’t just a simple coincidence.

“If your consciousness and Jin Taekyung’s had been mixed together from the beginning… Damn it. I don’t know what to call him. Fine, if your consciousness and that good-for-nothing’s had been mixed together, wouldn’t that make sense?”

After a brief silence, Jeok Cheongang asked his question. I thought about it for a moment, then shook my head.

“I don’t think so. No, I’m sure that’s not it.”

“What makes you say that?”

“I had no memories from the start. If our consciousnesses had merged, as you say, then I should’ve had at least one small memory. That’s the only way it would add up.”

I still remembered that time clearly.

When I first opened my eyes in the pleasure house, I didn’t even know Murim was another world rather than a virtual reality game.

I spoke with Wolhwa without knowing exactly who I was or where I was, and that was how I managed to get even the bare minimum of information.

*Of course, even that was so basic I had to lie to Jin Wikyung and tell him my memories were jumbled.*

If even the tiniest fragment of a memory had remained, I could’ve adjusted to this strange world much faster.

You know, like how the protagonist in some web novel gets hit with a splitting headache and suddenly absorbs a flood of memories.

But reality and fiction were worlds apart.

All I’d been given when I first set foot here was the same three-syllable name I’d had in the modern world.

And a body half-rotted from drink and women.

“……”

Now that I thought about it, I was fucking pissed.

Anyway, my conclusion was simple.

My consciousness and that of this world’s Jin Taekyung, who’d been nothing but a good-for-nothing, were completely separate.

No—we had been separate.

At least, until today, before I had that strange dream.

“You’re so certain, so I’ll take your word for it for now. But the fact that that good-for-nothing’s memories showed up in your dreams, at least…”

His words trailed off.

Jeok Cheongang stared at me with a grave look, then finally continued.

“Maybe some part of that good-for-nothing’s consciousness was inside you from the beginning.”

A groan escaped me before I could stop it.

It was one of the theories I’d been considering myself, but hearing it from someone else gave it a whole different weight.

*Damn it. What is this, one house with two families?*

There had been a time when I’d wondered about this, too.

It was after I’d spent a while living as Jin Taekyung of the Jin Family of Taiyuan—more precisely, after I realized this strange world wasn’t a game but another reality.

Two worlds.

Two people who’d lived different lives under the same name.

Even if my head were made of Ten-Thousand-Year Cold Iron, it would’ve been only natural to wonder about it at least once.

If this body wasn’t a game character…

Then what had happened to its original owner?

Where was that good-for-nothing’s soul, now that his body remained?

But at some point, I had to stop thinking about it. The crises that kept looming over me at every turn were too relentless for me to keep dwelling on a question with no answer.

I’d simply assumed he’d disappeared the moment I took over this body.

Maybe whoever had made that piece-of-junk capsule that brought me here had considered that the better outcome, too.

*But that wasn’t what happened?*

For once, I didn’t know what to say.

With a strange expression I couldn’t put into words, I rubbed my stomach.

Jeok Cheongang watched me in silence until he finally spoke.

“I understand you’re feeling conflicted, but what the hell are you rubbing your stomach for? It’s not like you’re pregnant. You’re a hairy man, for crying out loud.”

“……I mean, I could do it without thinking. Why do you have to put it like that?”

Was this the danger of media?

The moment I thought there might be something inside me, my hand had instinctively gone to my stomach.

*Must be a side effect of watching too many commercials about babies and toddlers,* I muttered to myself. Then I quietly moved my hand from my stomach to my chest and looked at Jeok Cheongang.

“Did something land on your chest, too? Are you all worked up, huh? Burning up with rage?”

“……I was just trying it out.”

“Fine, let’s say so. You went from your stomach to your chest. Where were you planning to touch next?”

“My head.”

Jeok Cheongang replied without a hint of hesitation.

“Don’t. You’ll look like an idiot.”

“Yes, sir.”

I was already starting to regret doing it.

Jeok Cheongang let out a deep sigh as he watched me snatch my hand back.

“What’s wrong?”

“I’m worried, seeing the way you carry on.”

“About what?”

“From what I’ve heard about that good-for-nothing, he was a complete idiot. If he suddenly took over your body one day, I might not even notice.”

“Ah, because I’m just as much of an idiot?”

“You understood perfectly. Not a word to add or take away.”

“Come on, that’s a little harsh. You’re hurting my feelings.”

“What are you going to do if your feelings are hurt? What can you even do? Hm? You…”

“Hey, why are you getting worked up all of a sudden? Calm down. Take it easy.”

At the last moment, Jeok Cheongang thankfully came to his senses. As though nothing had happened, he spoke in a calm voice.

“Anyway, keep discussing this with me. Do you understand?”

“I was planning to. Who else could I talk to about something like this, if not you?”

This wasn’t a choice. It was a necessity.

If I told people and even one word got out, I’d go from Divine Dragon to Mad Dragon in no time.

At least Jeok Cheongang believed me because he’d seen and experienced it firsthand. But if the truth about me got out to the world right now, the orthodox faction’s chivalrous heroes would be lining up to tear me apart for using dark arts without precedent.

Who knew? Maybe I’d become the Lord of Heaven’s classmate as a public enemy of Murim.

But in response to my obvious answer, Jeok Cheongang shook his head.

“No. There’s one more person besides me. Have you already forgotten?”

“Who… Oh.”

I’d asked on instinct, then clicked my tongue.

Right.

There was someone else.

Someone who wasn’t close enough for me to have a deep conversation with about something like this, but who was still somewhat near the truth.

*That’s right. The Bow Saint.*

But I was still a little wary of the Bow Saint.

No—not a little. Very.

*I have no idea what she’s thinking.*

That was exactly it.

The distance between the Bow Saint and me never seemed to shrink.

Even when we’d had several chances to talk at length while staying in the Imperial Palace, we’d never crossed the line she’d drawn.

An invisible wall.

It stood between the Bow Saint and me.

No, it seemed she treated everyone that way.

Whenever anyone tried to break through that wall and get closer, she would quietly withdraw.

As if we were magnets with the same pole.

As if that were the answer.

*But the Bow Saint might know something. She knows at least part of the truth.*

She’d believed the outlandish contents of a letter and spent decades wandering the world in search of me—or, more precisely, the “chosen one.”

Aside from Jeok Cheongang, who was standing right in front of me, and the mysterious absolute being known as the Martial God, whose very survival was uncertain, the Bow Saint was unquestionably the right person to ask.

Of course, first she’d have to agree to have this conversation.

“Old Master. Then, by any chance…”

But before I could finish, Jeok Cheongang shook his head, guessing what I was about to say.

“Meeting the Bow Saint right now isn’t possible. She still hasn’t returned from Hebei.”

“Hebei…”

“The situation hasn’t fully settled down, and even the Family Head of the Peng Family hasn’t been able to return yet. It’ll probably take a little longer.”

Hebei. And the Peng Family.

At the sound of those two words, something stirred in a corner of my chest.

Someone came to mind—someone who’d done his best for everyone until the very last moment of his life, then left.

“Could I ask about him? The Thunderbolt Saber King…”

“He’s gone.”

Jeok Cheongang answered briefly, then added out of the blue:

“He was smiling. Brightly enough to make me sick.”

“……!”

“That’s enough. That’s all that matters.”

Instead of answering, I quietly nodded.

And then, in the empty place where Jeok Cheongang had been, silence settled in.

A quiet that had finally come at long last—one I hadn’t felt in a very long time.

*Open System window.*

Ding.

A clear chime shattered the silence.
## Chapter artifact 993

# Chapter 993

*Open System window.*

The moment I muttered that short command in my mind—

Ding. Ding. Diiiing!

A familiar, clear chime rang out, and countless holographic windows poured from the air as if a dam had burst.



> **System**
> Sudden Quest, **Transmitting Internal Energy Across the Body**, completed successfully!
>
> Quest rewards have been issued!
>
> Your **internal energy** has increased dramatically!
>
> You have gained a large amount of **EXP**!
>
> You have received 20 bonus stat points!
>
> Level up!
>
> **Transmitting Internal Energy Across the Body** is a technique with such a low chance of success that no martial artist dares attempt it anymore. We commend your patience and audacity in succeeding at the process twice.
>
> You have earned the rare achievement **You Did That Twice. You Did That Twice.**
>
> Achievement rewards have been issued!
>
> You have gained a large amount of **EXP**!
>
> Your **Endurance** has increased dramatically!



The first things that caught my eye were the System messages announcing the completed Quest and earned achievement.

I’d only leveled up once, but the stat increase from successfully completing Transmitting Internal Energy Across the Body was enormous.

I quickly skimmed the messages, then erased a dozen or so with a single wave of my hand.

There were still more holographic windows I needed to check.



> **System**
> Successfully absorbed the internal energy of the **Heavenly Power Demon**!
>
> Successfully absorbed the internal energy of the **Thunderbolt Saber King**!
>
> The nature of **Scorching Yang Qi** is changing. The new flame born deep within your body will burn fiercer and hotter than ever!
>
> He who conquers the great sea will look down upon the world, but he who climbs the peak closest to heaven will look down even upon the great sea.
>
> Congratulations! Your **Middle Dantian** has been fully opened!
>
> You have reached the **Supreme Peak** realm!
>
> Sudden Quest, **Bone Transformation**, has begun. You cannot refuse this Quest!
>
> Sudden Quest, **Bone Transformation**, completed successfully!
>
> You can now draw in and release qi with great freedom. Your Muscles and Bones, now perfect in themselves, even reject impure qi!
>
> You have earned the great achievement **Full-Body Plastic Surgery**!
>
> Quest and achievement rewards have been issued!
>
> All attributes have increased significantly! Open the **Status Window** to check the details.
>
> You have received 30 bonus stat points!
>
> You have gained a large amount of **EXP** and **Fame**!
>
> Level up!



As I read through the holographic windows pouring out one after another, only one thought came to mind.

*This is insane.*

Of course, I’d expected massive rewards.

The Thunderbolt Saber King, Peng Cheolhu.

The power that giant, who’d defined an entire era, had passed on to me at the cost of what little life he had left was just as pure as it was immense.

Even so, the rewards listed by the System went far beyond what I’d expected.

Two level-ups, a huge number of bonus points on top of that, and a boost to all my attributes.

*I’ll have to check the details to see just how much my attributes increased, but even so, if I add all this together…*

It wouldn’t be an exaggeration to say I’d gained more than ten levels in one go.

No, in practice, it was even better than that.

The stronger I got, the farther away my next level-up seemed. The EXP required rose exponentially with each level, but the huge number of stat points I’d just received as a reward was pure bonus.

*I’m in debt. Deep in debt.*

Even with all those incredible rewards, I felt conflicted.

Overwhelmed by both joy and bitterness, I remembered the Thunderbolt Saber King smiling brightly as he said he would pass everything he had on to me.

And with him, I remembered all the victims who’d fallen at Eight Spring Gorge that day, when the chrysanthemums covering the mountain had turned red and the bodies of people and horses had piled up like mountains.

At the same time, I engraved one thing deep in my heart.

This enormous reward I’d been given was payment for the lives of the dead.

*I’ll repay this debt… no matter what.*

I’d never had much of a comfortable life, and debt had always been a miserable thing to me. But not this time.

I was looking toward the same place they were.

The day I finally cleared this entire debt, the peace everyone wanted would arrive.

And to make that happen, I had to endure and overcome whatever hardships and adversity came my way.

I couldn’t let grief make me collapse, or settle for the present. I had to keep moving toward higher places, never giving up.

Toward the place I’d glimpsed while completing Transmitting Internal Energy Across the Body, hidden behind thick clouds.

Toward the sky above the summit.

*Right. The upper dantian.*

Of course, I knew it was no easy feat.

Even the Three Saints, the greatest masters in the Central Plains, and Jeok Cheongang, who stood shoulder to shoulder with them, might not have opened their upper dantian. I couldn’t be sure.

*No, even if they’ve already reached that stage, there must still be differences between them.*

Everything had its proper order.

I’d widened a narrow stream into a vast sea. Now I had to climb a mountain peak that rose as if it would pierce the clouds.

Until now, I’d grown at a terrifying pace thanks to the System I’d gained by chance and countless fortuitous encounters. But even I had been stopped by the clouds.

I still couldn’t reach the absolute beings who looked down on the lower world from above them.

*What if I’d ridden that momentum and kept pushing forward back then?*

A pang of regret suddenly crossed my mind.

But I already knew the answer.

*I would’ve failed. And the odds would’ve been very high.*

Trying to break through to the upper dantian in those circumstances wouldn’t have been a challenge. It would’ve been a gamble.

Even I, despite having fully opened my Middle Dantian and feeling an intense surge of elation, had instinctively understood the difference between courage and recklessness—and pulled back.

The more I thought about it, the more indescribably frustrating it felt. But looking at it objectively, it had been a very good decision…

*Wait.*

What was this feeling?

I suddenly furrowed my brow as I remembered the excruciating process of Transmitting Internal Energy Across the Body and the strange dream that had come from memories that weren’t mine.

But that wasn’t all.

The inexplicable déjà vu that had suddenly taken hold of my entire body was telling me there was a trace of a memory, somewhere in between, that had been ground away.

“Decision. A good decision… I’m sure I heard that somewhere.”

My lips moved on their own. The voice that came out sounded unfamiliar, as though it belonged to someone else.

How much time passed?

Staring blankly into empty air like a man in a trance, muttering the same words over and over, I eventually recovered part of a memory that had been forgotten.

*Someone definitely said something like that. Not in reality, but inside my consciousness.*

My eyes stung. I’d forgotten even to blink.

My head had grown hot from turning the thought over and over for so long.

No—invisible little awls were slowly burrowing into my mind.

A headache spread through me.

But even as the pain made me wince, I kept rummaging through my thoughts. I searched the darkness for a tiny fragment hidden beneath larger memories.

And finally—

I remembered.

I remembered myself, realizing it wasn’t time yet and turning away from the upper dantian beyond the clouds.

And then, as I slipped into a trance where I lost all sense of self, someone’s words echoed faintly in my ear.



*That was a good decision. Just like back then.*



“……!”

Before I knew it, my eyes had flown wide open.

Was it because I’d realized who the voice belonged to?

No.

It was because an immense pain had suddenly struck me.

Hngh.

The unexpected pain made me suck in a breath on instinct. I clenched my teeth and squeezed my eyes shut.

The headache that had been slowly burrowing into my mind like an invisible awl had grown as huge as the long acupuncture needle the Medicine King Hall Master carried around like a prized weapon, and it was now tearing through my head.

*What the hell is this…!*

With my vision gone white, I flailed my limbs like someone on the verge of drowning.

Even in the middle of all this, though, I couldn’t let go of the one question in my mind that remained unanswered.

Who was the owner of that voice that had rung out like a hallucination at the last moment?

Who could speak to me in a space inside my mind, rather than in the real world?

*How? How could they do that?*

There was one thing I could be sure of.

The voice I’d heard at that moment belonged neither to Jeok Cheongang nor, even less so, to the Thunderbolt Saber King.

And aside from those two old martial-world veterans, no one else could have communicated with me then.

*Then who was it?*

I genuinely wanted to know. Even as it felt like my head was splitting open, I wanted to know.

Who owned that voice, and how had they approached me and whispered without any of us noticing?

At the same time, I wanted to ask:

How did you know me?

*They said, “Just like back then”… They definitely did.*

There was no doubt.

I didn’t know them, but they knew me.

I couldn’t say when or where we’d met, but today wasn’t the first time we’d encountered each other.

But…

*Why can’t I remember anything? Why?*

I remembered only what they’d said. I couldn’t distinguish the pitch or depth of their voice, or even their gender.

I couldn’t guess whether they were a woman or a man. And if they were a man, I couldn’t even tell whether they were young or old.

All I could vaguely recall was the sensation of that moment—the feeling I’d dredged up while enduring that terrible headache.

*A strange familiarity.*

It felt as unfamiliar as something I’d never heard before, and yet there was a faint, peculiar sense that I knew it.

And that was all I managed to recover.

Whoosh!

A flash of light exploded. The whiteness in my vision slowly receded, and focus began to return to my blurry eyes.

“……Ah.”

I let out the breath I’d been holding and realized that the pain, which had seemed like it would go on forever, had finally ended.

Along with the pain, the memory I’d been allowed to recover had reached its limit, too.

*Damn it.*

I stared silently at my fingertips, trembling with the remnants of the pain, then clenched them tight.

Crack.

The skin of my palm, now almost like iron after undergoing Bone Transformation, pressed taut against my sharp fingernails.

Perhaps it was because my emotions were surging so strangely.

At that very moment, a vast energy sleeping inside my body began to boil—

Ding.



> **System**
> A new Quest, **Unknown Voice**, has been created.
>
> You cannot choose whether to accept this Quest.
>
> The Quest will proceed by force.
>
> Would you like to check the newly updated Quest information?



Unknown Voice.

As I stared at the Quest title on the holographic window, I opened my tightly shut lips.

“Yes.”
## Chapter artifact 994

# Chapter 994

The System often—no, maybe pretty frequently—sprang cryptic clues on me in the form of Quests, their meaning impossible to pin down.

Just like now.



> **System**
> **Quest**
>
> **Unknown Voice**
>
> At some point, you became aware of the voice of someone whose identity you cannot determine.
>
> This may or may not be the first time this has happened, but one thing is certain.
>
> In the not-too-distant future, you may come face-to-face with the owner of that voice.
>
> May that moment of meeting not be an unhappy one.
>
> **Grade:** None
>
> **Restriction:** Jin Taekyung
>
> **Objective:** Continue to survive (In progress)
>
> **Reward:** ???
>
> **Failure:** ???



The moment I saw the translucent holographic window, only one thought came to mind.

*Here we fucking go again.*

What, would the screen go blue if it gave me a straight answer?

Vague explanations from beginning to end, as if they were shrouded in fog.

Of course, this wasn’t the first time I’d received a Quest like this. That didn’t make it any less impossible to get used to.

But at the same time—

*This is a process I have to go through.*

As I knew from experience, the System wasn’t an answer sheet.

It was more like a signpost, pointing me in a direction and telling me what lay beyond.

Depending on my choices, the arrows on the sign might change. Sometimes, like now, I had to interpret them myself.

So I read the words in the holographic window again and again.

Trying to figure out the meaning hidden in those twenty-questions-style clues.

And in that regard, the last two sentences in the Quest description were more than enough to catch my eye.

*I might meet the owner of that unknown voice? And in the not-too-distant future?*

Not too distant, huh.

Time was relative, so that was a pretty vague way to put it.

A year could feel like an eternity to a little kid with a runny nose, but to a white-haired old man, it might be no more than a fleeting moment.

So I had no way of guessing how much time the System meant by “not too distant.”

A few days. A few months. Or… No. Even the System couldn’t be so shameless as to call it “not too distant” if it meant years.

*Days would be too soon, and years would be too long. It makes sense to take it as something that’ll happen within a few months.*

Then what was that last line about it not being an unhappy moment?

And who on earth was the owner of that unknown voice—the very person who’d brought about this riddle of a Quest?

*Someone who could approach me without being noticed by me, the Thunderbolt Saber King, or even the Old Master. Someone who could intrude into my private inner world.*

When Transmitting Internal Energy Across the Body was taking place, the Thunderbolt Saber King and I were too busy giving and receiving energy to do much else. But Jeok Cheongang was different.

He’d stood guard for this dangerous technique, and he’d been straining every sense he had.

It should’ve been impossible to evade his notice and speak to me—especially when he was a Supreme Peak master who now stood shoulder to shoulder with the Three Saints, beyond even the Ten Kings.

Well, strictly speaking, it wasn’t completely impossible.

*If they were the greatest assassin of all time, with a concealment technique without precedent, or a master at least two moves ahead of the Old Master…*

And as far as I knew, only two people in the world could meet even those minimum requirements.

The first was undoubtedly the greatest assassin of all time, but I couldn’t think of a reason they’d do something like this—or be sure they could pull it off.

But the other one was different.

A wonder of the entire world.

The sky itself, looking down over this vast land alone. A being who, though born human, had come to be called a god.

“……The Martial God?”

The two syllables slipped from my lips before I realized it. A shiver ran down my spine.

The Martial God. The Martial God himself?

*That can’t be right.*

It had been half a century since the Martial God disappeared.

He’d vanished as suddenly as he’d appeared in the world, and no one under heaven knew where he was now.

No one could even say for sure whether he was alive or dead.

Not even the Bow Saint, who’d found me through the letter the Martial God had left behind.

And now he’d suddenly reveal his presence like this?

*No way.*

But realistically, the only person who could’ve done something like this was the Martial God.

As far as I knew, he alone was an overwhelming presence beyond the superhumans known as the Three Saints.

And perhaps I was the only person under heaven who knew more than anyone else about the truth hidden behind the Martial God.

*If my guess is right…*

A thought flashed through my mind, and my heart began to pound.

The first deep conversation I’d had with the Bow Saint at the Imperial Palace.

Amid the hectic days that followed, the name of someone I could only turn over in the back of my mind filled my thoughts.

*Cheon Taemin.*

Another absolute being who existed beyond a distant space.

Just as the Martial God had opposed the Heavenly Demon and restored peace, he was a hero who’d saved humanity from the demon known as the Demon King Asmodeus.

I could still see him clearly: unconscious, seemingly deep asleep, hooked up to a life-support system combining Magic and science in the Ares Guild’s restricted area.

And over that image, the voice of a woman faintly overlapped.



*“He left a message for the chosen one.”*

*“A message? What does that mean?”*

*“Divine strength. He said the chosen one should overcome the crisis with that divine strength and a Will like steel. Just as…”*



That day, the Bow Saint’s eyes had been fixed on me, deep and solemn.

And then, that voice had echoed faintly in my ears like a distant refrain.



*“Just as you did.”*



I still remembered the shock I’d felt in that moment.

No—I’d never forget it, even on my deathbed.

A piece of a puzzle I’d never imagined suddenly falling into place, after I’d turned it over vaguely in my mind and then laughed it off.

Divine strength.

A strange power possessed only by the chosen one.

The supernatural ability that belonged to me now—and to the Martial God in the past.

If the message the Martial God had left the Bow Saint was what I thought it was, that could mean only one thing.

*System user. Player.*

That was probably the Martial God’s true identity.

The truth hidden behind an unparalleled hero the likes of whom had never been seen before, and would never be seen again: a man who’d appeared out of nowhere, saved a world in turmoil, then disappeared.

But if that theory was true…

*Cheon Taemin and the Martial God can’t possibly be the same person.*

According to the capsule’s user manual, the System was a power granted to only one person.

The moment I reached that thought, a headache came over me.

Two heroes from separate worlds.

Their actions were astonishingly alike, and the more I learned about them, the more I found myself wondering whether Cheon Taemin or the Martial God might have had the same ability as me.

Whether the two of them might be the same person.

But now I didn’t know anymore.

What connection, if any, existed between the Martial God and Cheon Taemin.

If they were two entirely different people, not one and the same, what truth were they hiding?

I did know one thing: there was a way to resolve even a little of this doubt, this headache that was still stabbing my mind like a needle.

*I’m going back. Right now.*

That’s right.

There wasn’t just one place to find the answer.

In the modern world and Murim—in two worlds connected by a power I couldn’t begin to explain—I had to find a clear answer to this question.

And right now was the perfect time.

I’d completed the important Quest concerning the crisis in Shanxi Province, and the Logout function that had been blocked because of it was free again.

*One month. Maybe two. That should be enough.*

And it wasn’t just to learn more about Cheon Taemin.

I also had to deal with the fallout from the Doppelganger incident, which had happened right before I last Logged In.

On top of that, the ominous words it left behind before it vanished hinted at more trouble to come. Even with all the frantic activity in Murim, they’d been bothering me like a fish bone stuck in my throat.

*I’ll find out when I get back. Why the Doppelganger said those things. What it was willing to go that far for.*

Now that I’d made up my mind, there was no hesitation. I lay straight on the bed and pulled the covers up to my neck.

Even if I spent a couple of months in the modern world, only about three shichen would pass in Murim.

I didn’t know whose presence was hurrying toward me from somewhere in the distance beyond the window, but by the time they reached my room, all they’d find would be me already gone to the modern world—or, well, fast asleep.

*Logout.*

I slowly closed my eyes and recited the familiar command. The next moment, I realized something.

Some things in this world didn’t go the way you expected.

Bip-bip-bip!



> **System**
> Logout failed!
>
> The System has rejected your Logout command!
>
> Error! Error!
>
> Due to a System error, the Logout function has been temporarily disabled!
>
> Unknown error! Temporary Maintenance has begun!



……What?

My eyes flew open, even though I hadn’t meant to open them.

But neither the System’s voice that had pierced my ears nor the dozens of error messages floating in the air changed. I was thrown into utter confusion.

*Logout rejected? Why on earth?*

This had never happened before.

No—it had happened before, but only when I was in the middle of an important Quest, and even then it hadn’t happened like this.

*System error? Temporary maintenance?*

An update, sure. But I’d never heard of anything like that.

An error in the System, which had always been absolute? How could that be possible?

“What the…!”

A groan slipped from my lips on instinct. I bit down hard and shouted over and over in my mind.

*Logout! Logout!*

But nothing changed.

Nothing at all.

The holographic windows that poured out with every command showed only the words “System error.” Faced with this unbelievable reality, all I could do was stare blankly and take it in.

Actually, if I had to name one more thing I could do, it was let the person whose presence had drawn close to the door know that he was an unwelcome guest before he entered my room.

“Don’t come in. I’m… damn it. Anyway, I’m busy.”

Without even looking, I assumed it was Hyuk Mujin. If it wasn’t him, I figured it had to be one of the Fire Dragon Pavilion members.

But my guess was just as spectacularly wrong as I’d been when I tried to Logout.

Click.

“Must be because we’re brothers. Even on this, we’re of one mind.”

The next moment, the unwelcome guest opened the door without hesitation. No—it was Jin Wikyung, his expression heavy and grave.

The sight of him sent a chill down my spine.

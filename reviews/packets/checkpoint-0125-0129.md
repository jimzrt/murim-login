# Checkpoint Review — 125–129

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

# Chapters 125–129

## Plot

The surviving Mount Heng Sword Sect members thank Jin Taekyung, Jin Mukyung, and Hyuk Mujin for saving Lee Seowol and preserving the sect, while formally apologizing for Lee Cheonbaek’s crimes. Taekyung refuses their apology, saying the Jin Family of Taiyuan is the party entitled to receive it. Seowol will visit the Jin Family on New Year’s Day and still awaits Taekyung’s answer to her marriage proposal.

On the journey home, Taekyung examines Pung Yang’s Temporary Strength Pill. It grants enormous temporary power, fifteen years of internal energy, Body-Protecting Qi, and +100 combat-related stats, but its maker, Grade, and price are initially unknown. After Wipeng unconsciously names Dark Heaven, the System identifies it as the pill’s manufacturer. Wikyung and Wipeng refuse to explain Dark Heaven’s identity or connection to the Jin Family.

Wikyung and fifty elite guards arrive at Sakju to retrieve the Jin group. The family celebrates Taekyung, Mukyung, and Hyuk Mujin’s survival, while Mukyung learns that Taekyung possesses the dangerous pill. The group drinks for three days; Wipeng becomes known as the God of Drinking, while Taekyung gains the rumor-based title Night King and additional Fame.

As the Jin group travels onward, Taekyung’s Sleeping Dragon of Shanxi Title strengthens, raising its effects to all stats +15 and Fame +200. He reaches Level 61 with Fame 2,100 (+250) and sixty unspent stat points. Taekyung and Hyuk Mujin deliberately exaggerate their victory over the Red Wind Band, earning public awe and prompting a county magistrate to deliver an invitation from Shanxi’s City Lord.

The ten-year-old City Lord, a Prince and the Emperor’s youngest brother, invites Taekyung to a luncheon with young prodigies. Taekyung intends to refuse, but Hyuk Mujin accepts on his behalf, causing the System to create and lock in The City Lord’s Invitation Quest. Jin Mukyung reveals that he met the City Lord three years earlier and remembers the encounter as a nightmare.

## Continuity

- Pung Yang is dead, the Red Wind Band has been annihilated, and the wider Murim’s response remains unresolved.
- Jin Mukyung survived his battle with Pung Yang but remains incompletely recovered; his chest wound reopened during the drinking gathering.
- Lee Seowol remains the seventeen-year-old Sect Leader of the Mount Heng Sword Sect. Only a small group survived, and the sect’s reconstruction remains uncertain.
- Seowol apologized to the Jin Family through Taekyung, accepted the New Year invitation, offered the sect’s territorial rights, and proposed marriage to Taekyung in exchange for the Blood Wolf Sword Technique, Blood Wolf Footwork, and Shura Annihilating Fist. Taekyung intends to reject the proposal because he loves Song Song.
- The Temporary Strength Pill is in Taekyung’s Inventory and is known to Jin Wikyung, Jin Mukyung, and Wipeng. It is a Dark Heaven product restricted to Peak martial artists or higher; it temporarily grants +100 combat-related stats, fifteen years of internal energy, and Body-Protecting Qi at an unspecified price. Its Grade and long-term aftereffects remain unknown.
- Dark Heaven’s identity, purpose, relationship to the Jin Family, and possible connection to the Demonic Cult’s Blood-Exploding Pill remain undisclosed.
- Taekyung fully absorbed the Blazing Flame Divine Pill and possesses forty-five years of internal energy with the Scorching Yang Qi attribute.
- Taekyung is Level 61 with Fame 2,100 (+250), sixty unspent stat points, and a strengthened Sleeping Dragon of Shanxi Title granting all stats +15 and Fame +200.
- Wipeng is called the God of Drinking, and Taekyung is rumored to be the Night King.
- The City Lord’s Invitation Quest has been accepted on Taekyung’s behalf and requires attendance at the City Lord’s luncheon with young prodigies the following day. Its reward depends on the City Lord’s reaction, and rejection may cause him to sulk.
- Shanxi’s City Lord is a ten-year-old Prince, the Emperor’s youngest brother, and a direct member of the Zhu imperial family. He has held the office since age five.
- The current Emperor is rumored to have assassinated his older brother, the Crown Prince, to seize the throne.
- The government and Murim recognize each other’s authority and generally avoid interference; the Jin Family is not yet one of the Nine Sects and One Gang or the Five Great Families and must avoid provoking the government.
- The Fire King’s status remains unknown, and the truth of Jopil’s claim to be the nineteenth-generation successor of the Flame Divine Palm remains unresolved.

## Translation Decisions

- Retain **Peak**, **Supreme Peak**, **Internal Injury**, **Body-Protecting Qi**, **Scorching Yang Qi**, **Red Wind Band**, **Sect Leader**, **Benefactor**, **Taiyuan Jin Family**, **Dark Heaven**, **God of Drinking**, and **Night King**.
- Render 잠력단 as **Temporary Strength Pill**, 폭혈단 as **Blood-Exploding Pill**, 열화신단 as **Blazing Flame Divine Pill**, 만년한철 as **Ten-Thousand-Year Cold Iron**, and 이름 없는 검 as **Unnamed Sword**.
- Render 혈랑검법 as **Blood Wolf Sword Technique**, 혈랑보법 as **Blood Wolf Footwork**, 파천신권 as **Shura Annihilating Fist**, and 절정 무공 as **Peak martial arts**.
- Render 현령 as **county magistrate**, 성주 as **City Lord**, 성주의 초청 as **The City Lord’s Invitation**, 친왕 as **Prince**, 주씨 as **Zhu**, and 태자 as **Crown Prince**.
- Render 구파일방 as **Nine Sects and One Gang** and 오대세가 as **Five Great Families**.
- Render 전서응 as **messenger eagle**, 원단 as **New Year’s Day**, 갑자 as **jiazi**, and 시진 as **shichen**.
- Preserve the Samsung/Samseong pun with a clarifying footnote and retain **Jaringobi** with its explanatory footnote.

## Durable state

{
  "active_continuity": [
    "Pung Yang is dead; Jin Taekyung killed him after the Unnamed Sword's Ten-Thousand-Year Cold Iron destroyed his Body-Protecting Qi and pierced his chest.",
    "Taekyung fully absorbed the Blazing Flame Divine Pill and possesses forty-five years of internal energy with the Scorching Yang Qi attribute.",
    "Jin Mukyung survived his fight with Pung Yang and returned to the Jin Family of Taiyuan, but remains incompletely recovered.",
    "Cheol Mubaek remains severely injured and needs extended recuperation; Lee Seowol remains the seventeen-year-old Sect Leader of the Mount Heng Sword Sect and vows to preserve it.",
    "The Lower District Sect sent a relief force with physicians, cooks, and laborers after the battle.",
    "Wolhwa's real name is Eun Sowol, and she is the Lower District Sect's Shanxi Branch Leader with authority over more than thirty Shanxi branches.",
    "Lee Seowol accepted Jin Wikyung's invitation to the Jin Family of Taiyuan's New Year gathering and offered the Mount Heng Sword Sect's territorial rights to the Jin Family as an apology.",
    "Lee Seowol proposed marriage to Jin Taekyung in exchange for the Blood Wolf Sword Technique, Blood Wolf Footwork, and Shura Annihilating Fist; Taekyung decided to reject the proposal because of her age and because he loves Song Song.",
    "Forty-seven mounted bandits survived the battle, but the Lower District Sect can save only about thirty with its available medicine; the sect is spreading a rumor that the two Jin brothers defeated Pung Yang and rescued Mount Heng.",
    "Cheol Mubaek and Lee Cheonbaek first met more than thirty years ago, fought, and became close friends; Cheol is the ninth-generation successor of the Shura Annihilating Fist.",
    "Jopil is dead and left behind the Supreme Peak martial art Flame Divine Palm; the Fire King is a Supreme Peak master and the Fire Gate Clan has a single successor, but his current status is unknown.",
    "The Mount Heng Sword Sect formally apologized for Lee Cheonbaek's crimes, but Taekyung refused the apology and directed responsibility toward the Jin Family of Taiyuan.",
    "The Temporary Strength Pill is stored in Taekyung's Inventory and has been revealed to Jin Wikyung, Jin Mukyung, and Wipeng; its System description identifies Dark Heaven as its manufacturer and records its unknown Grade, Peak restriction, temporary power increase, +100 combat stats, fifteen years of internal energy, and Body-Protecting Qi effect.",
    "Jin Wikyung and Wipeng traveled to Sakju with fifty elite guards after receiving an emergency report about Pung Yang, the Red Wind Band, the Mount Heng Sword Sect, and the Jin brothers.",
    "The Jin Family of Taiyuan displayed a huge Sakju banner celebrating the safe return of Mukyung, Taekyung, and Hyuk Mujin.",
    "Taekyung, Mukyung, Wikyung, and Wipeng drank through the night for three days; Wipeng is called the God of Drinking and Taekyung is rumored to be the Night King.",
    "Taekyung's Sleeping Dragon of Shanxi Title effect strengthened to all stats +15 and Fame +200; his current Status Window shows Level 61, Fame 2,100 (+250), and 60 remaining points.",
    "Hyuk Mujin and Taekyung publicly exaggerated the battle's death toll and achievements, and the county magistrate and assembled crowd reacted with awe.",
    "Hyuk Mujin accepted the City Lord's Invitation Quest for Taekyung, which requires attendance at the City Lord's luncheon with young prodigies tomorrow; its reward depends on the City Lord's reaction and rejection may make him sulk.",
    "The City Lord of Shanxi Province is a ten-year-old Prince and the Emperor's youngest brother, appointed at age five; Jin Mukyung met him after being summoned three years earlier and considered the encounter a nightmare."
  ],
  "continuity_sources": [
    129,
    128
  ],
  "open_questions": [
    "How will the Jin Family of Taiyuan respond to Lee Seowol's proposed transaction and territorial transfer?",
    "Can Lee Seowol preserve or rebuild the Mount Heng Sword Sect with so few survivors?",
    "What are the Temporary Strength Pill's exact price and long-term aftereffect, and is it related to the Demonic Cult's Blood-Exploding Pill?",
    "What is Dark Heaven, and why do Jin Wikyung and Wipeng refuse to discuss it?",
    "What consequences will Pung Yang's death have for the Red Wind Band and the wider Murim?",
    "Is the Fire King still alive, and if so, where is he?",
    "Was Jopil truly the nineteenth-generation successor of the Flame Divine Palm, and how did he acquire it?",
    "What will happen at the City Lord's luncheon and how will the City Lord react to Taekyung?"
  ],
  "safe_through": 129,
  "temporary_decisions": [
    "Render 잠력단 as Temporary Strength Pill and 폭혈단 as Blood-Exploding Pill.",
    "Render 만년한철 as Ten-Thousand-Year Cold Iron and 이름 없는 검 as Unnamed Sword.",
    "Render 열화신단 as Blazing Flame Divine Pill and 반 갑자 as half a jiazi, clarified as thirty years.",
    "Render 완전 회복 as Full Recovery and 회광반조 as final rally in this death-and-recovery context.",
    "Render 운칠기삼 as seven parts luck and three parts skill, and 운구기일 as nine parts luck and one part qi, with a footnote explaining the variation.",
    "Render 은공 as Benefactor, 절정 무공 as Peak martial arts, 급식 as school lunch, 고딩 as high schooler, 철컹 as clank, 산서성 as Shanxi Province, 총지부장 as Chief Branch Leader, 원단 as New Year's Day, 갑자 as jiazi, and 시진 as shichen.",
    "Render 일인전승 as single successor, 비인부전 as transmission only to the worthy, 구 대 계승자 as ninth-generation successor, 천하십대권법 as the ten greatest fist techniques in the world, 열화문 as Fire Gate Clan, 화왕 as Fire King, 삼성 as Three Saints, 십왕 as Ten Kings, 진무보법 as Jin Family's Manoeuvre Technique, 아이템창 as Item Window, 전서응 as messenger eagle, 고원 as Gaoyuan, 구주 as Nine Provinces, 사술 as dark arts, 마기 as demonic qi, 선천지기 as innate qi, 소음인 as Soeumin, 태양인 as Taeyangin, 암천 as Dark Heaven, 주신 as God of Drinking, 야왕 as Night King, 화주 as fire liquor, 화북 as North China, 현령 as county magistrate, 성주 as City Lord, 장 노인 as Old Man Jang, 적토마 as Red Hare, 여포 as Lü Bu, 성주의 초청 as The City Lord's Invitation, 친왕 as Prince, 주씨 as Zhu, 천자 as Son of Heaven, 황상 and 황제 as Emperor, 태자 as Crown Prince, 구파일방 as Nine Sects and One Gang, and 오대세가 as Five Great Families."
  ],
  "version": 1
}

## Reading copies

## Chapter artifact 125

# Chapter 125

“Benefactor.”

Lee Seowol was especially beautiful today. She wore a snow-white formal robe, and her hair, twisted up with a jade hairpin, gleamed.

She still looked haggard from everything she had been through, but her beauty was so dazzling that even her exhaustion seemed charming.

*No. What am I thinking?*

Beautiful? Charming? At seventeen, she was at the age when she should be wearing a school uniform and preparing for her grades, not marriage.

She was two years younger than Hayeon, which put ten years between us. With an age gap like that, she might as well have been my niece.

*Still, she certainly seems mature for her age… No. Get a grip.*

Avoiding Lee Seowol’s deep gaze, I clasped my hands in a formal salute.

“Greetings.”

“I greet the Sect Leader.”

Lee Seowol was no ordinary girl. She was the Sect Leader responsible for an entire sect. Just as she was about to return Jin Mukyung’s and my polite greetings—

“Imagine the Sect Leader of the great Mount Heng Sword Sect coming out to greet us in person. I, Hyuk Mujin, am deeply honored!”

Of course. It wouldn’t be complete without you.

Hyuk Mujin kept his gaze fixed on her while repeatedly bowing at the waist. All I could do was sigh.

“I apologize. He’s a little short in the head.”

“...Captain.”

“You saw that, right? He’s pretending to be close to you even though you two have nothing to do with each other. You’ll be better off ignoring him.”

A faint dimple appeared beside Lee Seowol’s mouth.

“Not at all. He’s also a Benefactor who fought for our sect.”

“It’s fine. He didn’t lift a finger, so you don’t have to count him as a Benefactor.”

“...Oh. I see.”

Her smile had just turned awkward when a rough voice came from behind her.

“He’s a Benefactor to me.”

The speaker was a middle-aged man with half-gray hair. Sitting in a clattering wooden cart, he gave us a nod.

“Please excuse me for being unable to stand. Well, growing old has made me less sturdy than I used to be.”

No one here could match the middle-aged man before us in either age or fame.

At the appearance of Cheol Mubaek, the Tiger of Mount Heng, Hyuk Mujin quickly bent at the waist.

“I greet Great Hero Cheol Mubaek—”

“Is this the first time you’ve seen my face? Skip the troublesome formalities.”

“But you’re a great senior of the Murim, renowned throughout the martial world...”

“Senior, my foot. If you worry about things like that one by one, life in the Murim gets tiring.”

“...”

The old man had quite the laid-back personality.

Even Hyuk Mujin, who was shameless enough to rival anyone, quietly shrank back. That left Jin Mukyung.

“You’ve arrived.”

Nothing special. He simply clasped his hands in a brief salute. Yet Cheol Mubaek’s face lit up the instant he saw him.

“Well, look at that. Isn’t this our Heaven Shaking Sword? So, you’re leaving now?”

“It seems so.”

“Why don’t you stay a little longer? We could have a serious discussion about martial arts later. Hmm?”

“I’m sorry, but I’m pressed for time.”

“Oh, what a shame. It can’t be helped, then. How about coming to see this old man sometime?”

“If a great senior of the martial world is willing to teach me, then I’m the one who should be asking for such an opportunity.”

“Ha-ha-ha! Senior, huh? That sounds nice.”

What was I looking at?

They had only spent three or four days together, but they looked like a close grandfather and grandson.

And what about that? Hadn’t he just said that life became tiring if you worried about seniority and junior status? Look at him changing his tune.

I shot Hyuk Mujin a glance.

*What’s with those two?*

*No idea. He called me a Benefactor before. Is it really okay to treat people this differently?*

*But if you’re being honest, you didn’t actually do anything.*

*...*

He clamped his mouth shut with an irritated expression. My meaning seemed to have gotten through.

“All right. Make sure you come next time.”

Cheol Mubaek looked at Jin Mukyung with a satisfied grandfatherly smile before turning toward me.

“What about you? Don’t you have anything to say?”

For a moment, I could have sworn I felt the gaze of a predator.

I decided to follow the better of the two examples I had just witnessed.

“You’ve arrived.”

“Of course I have. Did I go somewhere?”

“...”

That wasn’t it.

But smiling in hard times was the mark of a First Rate man. I put on a smile without panicking.

“Are you feeling all right?”

This time, Cheol Mubaek shook his splinted limbs.

“Do I look all right?”

“...No.”

“If I were all right, I would have walked here. These days, those mounted-bandit bastards work people without even a retirement age. What chance does an old man like me have?”

“...”

The old man had quite a memory. He still seemed to be holding on to the mistake I had made when we first met.

Lee Seowol, who knew nothing about the situation, shouted in embarrassment.

“Uncle!”

“Good grief, my old ears are going to fall off.”

After grumbling, he suddenly bowed his head politely.

“Thank you, everyone.”

This wasn’t a reluctant gesture. Cheol Mubaek, the Tiger of Mount Heng, was an old master who had walked his own path for many years. He was speaking from the bottom of his heart.

“It’s not because you extended the life of an old man with little time left. Seowol—thank you for protecting that child. Thanks to all of you, the Mount Heng Sword Sect survived.”

He gazed calmly at me, Jin Mukyung, and Hyuk Mujin in turn.

“I’ve learned something after living for more than a jiazi.[^1] Gratitude and grudges must be repaid, no matter what it takes. I swear here and now that I will never forget what happened, not until the day I die. If you wish it, I’ll repay you even if it costs me my life.”

Lee Seowol immediately took up his words.

“The Mount Heng Sword Sect will remember our Benefactors. I would also like to apologize here for the wrongdoing committed by my late father...”

“We apologize!”

“Please forgive us!”

The thunderous cries burst from the mouths of the Mount Heng martial artists.

All of them bore injuries, both major and minor. Kneeling in the snow that had not yet melted, they waited for our answer.

A tap.

*You answer.*

At Jin Mukyung’s Sound Transmission, I licked my dry lips.

*Forgiveness.*

We had won the war, but wounds remained.

Martial artists had fought and died without end on the orders of their superiors. Even women and children who had never learned martial arts had been sacrificed. It was all the work of Lee Cheonbaek, who had been blinded by his desire to avenge his son.

The wounds left by the war with the Mount Heng Sword Sect ran deep, and it would take a long time for them to heal.

*And scars will remain.*

Some scars could never be erased.

The young siblings who had lost their home and parents in an instant would carry such scars. So would I. Even now, I could still see the face of the man who had dreamed of becoming the greatest under heaven.

But I couldn’t deny that the wounds were beginning to close.

*The people who caused them are all dead.*

The Head Elder and Lee Cheonbaek, each of whom had dreamed of revenge, had already met their ends.

Wasn’t that why we had raced here day and night to save the Mount Heng Sword Sect?

With a sincere apology and forgiveness... wounds could heal, even if scars remained.

Just as they were now.

“I won’t accept your apology.”

The words came out only after considerable thought. Without waiting for anyone else to react, I continued.

“I’m not someone with the right to receive an apology from you or to forgive you.”

No one here had that right. The people they needed to apologize to were in the Jin Family of Taiyuan.

Apparently understanding what I meant, Lee Seowol and Cheol Mubaek both nodded.

“I’ll see you on New Year’s Day.”

“Taiyuan. It will be my first time venturing out in thirty years.”

The Mount Heng Sword Sect was hardly a welcome guest. Especially in its current, pitifully diminished state, it might have to endure all kinds of humiliation and disgrace.

But that was something they would have to bear themselves. There was nothing I could do, nor any reason for me to interfere.

*Well done.*

With Jin Mukyung’s brief Sound Transmission in my ear, I offered one last farewell.

“Then, we’ll be going.”

I had just turned toward the carriage when Lee Seowol called out.

“Benefactor.”

“Yes?”

“Did you know that there are fewer than fifteen days left until New Year’s Day?”

Her voice flowed like a little stream.

“I’m looking forward to hearing the answer I didn’t get last time.”

I could only open and close my mouth in confusion. Jin Mukyung grabbed me and pulled me away.

The carriage set off at full speed, with the sound of Cheol Mubaek’s distinctly displeased cough following us from behind.

* * *

The journey back to the Jin Family of Taiyuan was quick and smooth. The coachman’s skill played a part, but with the impatience in my heart gone, everything seemed easier.

“Phew.”

Jin Mukyung had just finished circulating his qi when he suddenly muttered,

“Now that I think about it, I didn’t even get to see a Peak martial art.”

He had joined the journey after being lured by Jin Wikyung’s claim that he could see Peak martial arts if he went to Mount Heng. I answered him calmly.

“It’s fine. Thanks to Pung Yang, you got to see Mount Beimang.”

“You call that consolation?”

“No. I was teasing you.”

The sound of bones cracking came from Jin Mukyung’s hand.

“You’ve grown a lot.”

“Would you like to spar once your injuries have fully healed?”

“I could do it right now... Urgh.”

Jin Mukyung tried to spring to his feet, then immediately frowned.

No matter how quickly he recovered, it had only been four days. That was nowhere near enough time for his injuries to heal completely.

He collapsed back into his seat and glared at me.

“You should consider yourself lucky.”

“I don’t know about lucky, but my lifeline sure is damn tough.”

The fact that I kept surviving despite facing the brink of death every time suggested that I had been born with an unusually sturdy lifeline. Either that, or I had been blessed with heaven’s fortune.

“Anyway, you did well.”

“Huh?”

“Eeeh?”

Hyuk Mujin and I both widened our eyes at the unexpected praise sticker. The person who had given it looked at us as if he couldn’t understand what was wrong.

“Why are you looking at me like that? You look as if you’ve heard something you weren’t supposed to.”

“You’re like a ghost.”

“Wait, could it be that you already died to Pung Yang and became a vengeful spirit, and you’re here with us?”

It was a fairly plausible theory, but around Jin Mukyung, you had to watch your mouth at all times.

I felt around inside my clothes while watching Hyuk Mujin get beaten until dust flew.

*Inventory open. Summon.*

The next moment, my fingertips touched something round and hard.

It was the only thing Pung Yang had left behind.

Or rather, the only thing I had taken from Pung Yang.

*Check item.*

*Ding.*



> **System**
>
> **Item Window**
>
> **Temporary Strength Pill**
>
> **Type:** Elixir  
> **Grade:** ???  
> **Restriction:** Peak martial artist or higher  
> **Description:** A pill manufactured by an unknown person. It greatly raises the user’s latent power for about one shichen, but a price must be paid in return. Do not take it except in the worst-case scenario.  
> **Effect:** Combat-related stats +100  
>
> **Internal energy:** +15 years  
>
> **Body-Protecting Qi:** Available

Even with the short time limit, the effect was absurd. It was easy to understand why Pung Yang had been so confident.

I had no idea how severe the aftereffects were, but if my life were in danger, I’d eat twenty of them, not two. Obviously.

But the part that bothered me was something else.

*An elixir manufactured by an unknown person.*

The Item’s Grade was marked with question marks, its exact aftereffects were not listed, and even its maker was shrouded in mystery.

What kind of bastard had created such a bizarre thing?

*This thing reeks of something shady.*

I was turning the Temporary Strength Pill over in my hand and lost in thought when a distant cry reached us.

“Mukyuuung! Taekyuuung!”

Jin Mukyung, who had been enthusiastically hammering Hyuk Mujin on the forehead, suddenly stopped.

“Was that a hallucination?”

Yeah, no.

[^1]: A jiazi is a traditional sixty-year cycle.
## Chapter artifact 126

# Chapter 126

Four days ago, after completing every mission and returning to the Jin Family of Taiyuan, Wipeng deeply regretted how efficiently he had handled things.

*I should have come back a day later.*

But it was already too late. Jin Wikyung had received a messenger eagle from the Lower District Sect and was raging with his eyes bulging out of his head.

“Those goddamned mounted bandits dare!”

“What happened now?”

“Pung Yang, the Red Wind Band, the Mount Heng Sword Sect, my brothers—they’re in danger! Great danger! We leave at once!”

“...I’ll assemble the guards.”

Now that every obstacle had been removed, Jin Wikyung’s authority was absolute. Before even half a shichen had passed, the two of them left the family with fifty elite guards and raced off without stopping.

Two days later, while changing horses at a Lower District Sect branch, they received new information.

“What? Pung Yang is dead, and the Red Wind Band has been annihilated?”

“Yes! According to what our sect has learned, most of the enemy forces, numbering around three hundred, were slaughtered. Young Master Jin Taekyung defeated Pung Yang himself.”

“Oh. Ohhh. Taekyung!”

Jin Wikyung’s laughter, as if he had gained the whole world, vanished at the next words.

“Tell me again. What happened to Mukyung?”

“Th-that is... He suffered a considerable injury in his life-and-death duel with Pung Yang... But his life is not in danger, and he is recovering quickly, so you likely have nothing to worry about.”

It was already over. Jin Wikyung had probably heard nothing except *considerable injury*.

When his younger brothers were children, if even a thorn pierced one of their fingers, he would raise such a commotion that you would have thought the finger had been severed.

*And it wasn’t a minor injury. It was a considerable one. This is going to be a disaster.*

Based on his experience so far, Wipeng predicted what would happen next.

Sure enough, he was exactly right.

“Mukyung is hovering between life and death?!”

At Jin Wikyung’s roar, the Lower District Sect member blinked.

“Y-yes?”

“Pung Yang! You dare kill my little brother!”

First Jin Wikyung turned a considerable injury into hovering between life and death, and now he’d pronounced Mukyung dead outright. The Lower District Sect member finally came to his senses and hurriedly opened his mouth.

“Lesser Family Head, I think there’s been a terrible misunderstanding...”

“I’ll tear your limbs to shreds and scatter them across the Nine Provinces!”

“...”

“...”

Jin Wikyung’s anger did not subside until another day had passed.

“Mukyung and Taekyung left the Mount Heng Sword Sect yesterday?”

“Yes. So please take it down a notch.”

“Are they both safe?”

“If they weren’t, would they be coming in a carriage instead of being carried in on a cart?”

“Then...”

“You should be able to see them around noon tomorrow.”

The thought that he could finally rest brought Wipeng immense relief.

*Who am I?*

He was a Peak master, a skilled martial artist known by the epithet Ghost Sword. He had enough ability to claim an important position wherever he went, yet because he had chosen the wrong lord to serve, he was being subjected to this extreme labor.

*When was the last time I had a drink?*

Today, at last, he would be able to enjoy some roast duck with a warm glass of liquor.

A satisfied smile had just appeared around Wipeng’s lips when Jin Wikyung spoke.

“Good. Then let’s get ready.”

“Pardon? Get ready for what?”

“My brothers overcame countless hardships and successfully completed their mission. We have to hold a welcoming ceremony.”

“...Did I spend more than half a month touring the martial world for fun?”

“Hm? Who? Oh, you?”

Jin Wikyung blinked at Wipeng, then let out a hearty laugh.

“Of course that includes you! Surely you didn’t think I’d forgotten?”

*I’d thought surely not, but this guy had definitely forgotten.*

As Wipeng stared at him in disbelief, opening and closing his mouth without a word, Jin Wikyung continued.

“Oh, have your subordinates buy some cloth from a nearby fabric shop. As large as possible.”

“Cloth? Why do we suddenly need that?”

“I have an idea.”

* * *

“...And that’s how it happened.”

Listening to Wipeng, who looked ten years older than when I’d last seen him, I glanced around.

We had reached Sakju two days after leaving the Mount Heng Sword Sect. The city was unexpectedly packed with people, and at the entrance, a gigantic white cloth bearing black writing fluttered in the wind.



Congratulations on the safe return of Jin Mukyung, Jin Taekyung, and Hyuk Mujin!

—Everyone in the Jin Family of Taiyuan—



A groan escaped me before I could stop it.

“Oh, fuck. What the hell is that...?”

In all my life, I had never seen anything like it.

The banner was more than twenty jang—over sixty meters—wide.[^1] Strung between the tops of two pavilions facing each other across a broad avenue, it looked as though it might even be visible from the Mount Heng Sword Sect.

*Look at that unnecessarily flamboyant calligraphy.*

Even overbearing parents whose child had been accepted into a prestigious university wouldn’t go this far.

Jin Mukyung, Hyuk Mujin, and I all stared at the banner with our mouths hanging open, as if we had planned it.

“Why is my name so small?”

I looked again to see what he meant. Hyuk Mujin’s name had been included in tiny letters.

“Are you disappointed that the letters are small? I’d be happy if I were you.”

“It’s strange. You can barely see it from below.”

“Want me to remove my name and put yours there instead? I’m serious.”

Hyuk Mujin thought about it for a moment before answering.

“Now that I think about it, this is fine as it is.”

“Then shut up.”

“Yes, sir.”

The conversation could go no further. The overbearing parent—no, Jin Wikyung—came running toward us with the brightest smile in the world.

“You little rascals!”

Was he a man or a brown bear?

The giant, well over two meters tall, dragged Jin Mukyung and me close with hands as large as pot lids. His brute strength was so tremendous that it would not have been strange if he had crushed us to pieces.

“I’m so glad you’re safe. Really, so glad!”

We had been safe.

Right up until Jin Wikyung hugged us with all his strength.

*Crack.*

“Guh!”

“Mukyung!”

...He doesn’t look very safe now.

The perpetrator, still embracing his victim as he trembled in pain, shouted,

“Doctor! Doctor!”

“I think we should call a doctor. He looks like he’s in real pain.”

Wipeng answered my question with a weary expression.

“Is this your first day dealing with him? I knew this would happen, so I called one in advance.”

“Ohhh.”

It was the first time I had ever thought Wipeng was magnificent.

* * *

The three Jin brothers of the Jin Family of Taiyuan, including me, and Wipeng gathered together shortly after sunset.

When Jin Mukyung appeared wrapped in even thicker bandages, Jin Wikyung cautiously studied him.

“Are you all right?”

“Would you be all right if it were you, my lord? How could you handle someone who was already injured so roughly?”

“I was being as gentle as I could...”

Jin Wikyung might not have been the strongest in martial arts, but when it came to raw physical strength, he was number one in Shanxi.

I quietly slid my chair farther away, while Jin Mukyung answered with a haggard expression.

“I’m fine.”

“...”

He looked anything but fine.

It was fortunate that Jin Mukyung was a Peak master. If he had been an ordinary civilian who had never learned martial arts, he would not have been able to walk.

Wipeng spoke up.

“I heard that the Second Young Master was injured, but I didn’t realize it was this severe. His Internal Injury hasn’t even healed completely yet...”

“Was this really the work of that Pung Yang bastard?”

In response to their questions, Jin Mukyung nodded calmly.

“He was strong. Stronger than I expected.”

Who was Jin Mukyung? He was a promising young prodigy who drew attention throughout the realm. Based on his dazzling talent and relentless effort, he had reached the Peak realm at a young age—yet he had been defeated by a mere mounted-bandit leader.

“You mean he was truly that powerful?”

“Pung Yang... I’ve heard that there are some fairly skilled masters among the mounted bandits of the plateau. But still...”

Their gazes suddenly turned toward me.

It was a silent demand that I stop stuffing my face with roast duck and say something.

I swallowed the food filling my mouth and opened it.

“It’s true. You’ve heard the news about the Great Hero known as the Tiger of Mount Heng, right? He got his arms and legs wrecked too. These days, he gets around in a wheelchair.”

“What is a wheelchair?”

“Ah, a cart. A cart.”

Jin Wikyung tapped the table with one thick finger.

“A master of that caliber would have been known long ago. Mukyung, is it possible that you let your guard down?”

This time, Jin Mukyung shook his head without hesitation.

“I was caught by a move I hadn’t anticipated, but that cannot be an excuse. Even if we fought again, the result would be the same.”

“...Was he really that strong?”

“He used Body-Protecting Qi. It was overwhelming.”

Jin Wikyung and Wipeng both opened their eyes wide.

“Body-Protecting Qi!”

“Second Young Master, is that true?”

There was no need for an answer. Jin Mukyung had no reason to tell such an obvious lie. Facing their shock, he continued.

“He was the strongest opponent I’ve ever fought. No—in exact terms, it would be more accurate to say that he became stronger.”

“Became stronger?”

“What do you mean by that...?”

“The moment he swallowed a crimson pill, he became terrifyingly powerful.”

At last, the conversation had reached the Temporary Strength Pill.

I tried to act as naturally as possible.

*I can’t let them find out I have it.*

The Temporary Strength Pill was a poisoned chalice. It was unquestionably ominous and suspicious, but there was no denying that it possessed tremendous power.

I had already decided to use it as a second-worst contingency for the worst possible moment—when I was facing death.

“It was only for a brief moment, but when he was about to take the pill, I clearly saw that one pill remained inside the wooden case...”

Jin Mukyung let his voice trail off and looked at me.

“Did you happen to find anything on Pung Yang’s person afterward?”

“Something like what?”

“A wooden case. Or the red pill I mentioned.”

I deliberately furrowed my brow.

“I’m not sure. I searched him later to see if he had anything, but all that came spilling out were piles of wooden scraps. Could those have been fragments of the case?”

“Then the pill? The pill?”

“No idea. I was exhausted enough to die myself. How was I supposed to search through everything?”

It was a fairly convincing excuse.

It wasn’t as if only one or two people had died, and the battle had been brutally fierce. It was only natural that I had been too exhausted to search properly. What more could he say?

“Is that so?”

“The people from the Mount Heng Sword Sect might have found it. Or it could have melted into one of the countless pools of blood scattered across the ground.”

“Hmm.”

Jin Mukyung stared at me with faint suspicion, but I merely shrugged.

*You won’t find it even if you search, idiot.*

I had tucked it safely into a corner of the greatest vault in existence—my Inventory, which only I could open and close. Neither Jin Mukyung nor the greatest thief under heaven could touch a hair of the Temporary Strength Pill.

*It really is convenient.*

As I marveled at the convenience of the system once again, Jin Wikyung and Wipeng began speculating about the pill’s origin.

“It must be a relic of demonic, heterodox arts. I remember hearing that quite a few pills with similar effects were used during the Great Faction War.”

“There was a time when the northern part of Shanxi, including Gaoyuan, fell into the hands of the Demonic Cult. If Pung Yang discovered traces of it, that would make sense.”

I had been listening with my ears perked up when I suddenly froze.

*Wait. The Demonic Cult?*

The Demonic Cult was a regular fixture you could never leave out of a Murim novel, the licorice in every medicine shop, and Geum Jandi’s honorary firefighter.[^2]

Of course, it wasn’t a religious organization devoted to world peace and helping the poor. It was more like IS—the Islamic terrorist group.

In short, it was a fanatical organization with absolutely nothing to gain from getting involved with it.

*If the Demonic Cult created the Temporary Strength Pill...*

Pung Yang’s eyes had been stained red, like a demon that had just climbed out of hell. The pill had granted him an absurd amount of power, even if only temporarily.

*I was starting to get the picture.*

It felt bad. Really, really bad!

But nothing could be gained without suffering. The side effects should be something I could endure...

“The most famous thing the Demonic Cult used back then was the Blood-Exploding Pill, if I remember correctly.”

“I’ve only heard of it. They say that once two shichen pass, all the blood vessels in the body burst and the user dies?”

“That was the price of trying to gain power through dark arts.”

“If the Blood-Exploding Pill was that bad, how severe would the side effects of the one Pung Yang used be?”

“I don’t know, but they must be beyond imagination. It wouldn’t just damage his innate qi. Once the time limit ended, his body would suffer tremendous strain. In the end, the pill uses the body itself as kindling and burns it for a brief period.”

I swallowed dryly. Before I knew it, my voice had jumped out.

“What happens after that?”

“It was made by the Demonic Cult. What else would you expect? Once the demonic qi surges into your very marrow… you’d become a murderous fiend who knows nothing but blood.”

“...A murderous fiend? The demonic qi surges into his marrow?”

“If such an object fell into the hands of a villain, it would be a truly terrible disaster... Taekyung, what’s wrong?”

Jin Wikyung looked at me with concern. I rubbed my forehead and found it covered in beads of sweat.

“Nothing. I’m just a little hot.”

“What are you talking about? It’s snowing outside.”

“What would a Soeumin know? I’m a Taeyangin.[^3] That’s why…”

Damn it. I didn’t even know what I was saying anymore.

I gave the other three an awkward smile.

“There’s something I forgot earlier.”

“...?”

“...?”

“...?”

“That pill. Now that I think about it, I have it. Heh-heh. Heh-heh-heh.”

“...!”

“...!”

“...!”

[^1]: A jang is a traditional Korean unit of length measuring roughly three meters.

[^2]: Geum Jandi is the heroine of the Korean drama *Boys Over Flowers*.

[^3]: Soeumin and Taeyangin are two of the four constitutional types in traditional Korean Sasang medicine.
## Chapter artifact 127

# Chapter 127

It didn’t take long for the question marks to turn into exclamation points, and the exclamation points to turn into bewilderment and rage.

Jin Mukyung was the first to break the silence.

“You…”

His face was flushed red, and his breathing was rough. His fist twitched as if he wanted to plant one right in my mouth.

*Well, he’s really pissed.*

It was chilling. A dagger had flown straight into my chest.

But don’t worry. I had a sturdy shield.

“Now, now, Mukyung.”

At the quiet voice, Jin Mukyung’s face twisted violently.

“Eldest brother!”

“Taekyung must have had his reasons. Isn’t that right?”

I deliberately lowered my eyes.

“No, eldest brother. I was short-sighted.”

“Hm?”

“I let my curiosity get the better of me… But after hearing what Eldest Brother said, I realized something. It’s an object that should never be kept—or hidden.”

I didn’t forget to make a show of trembling my fist, as if merely thinking about it made my teeth chatter with rage.

“The Demonic Cult! Just hearing the name of those vile bastards makes me tremble with fury!”

This part was sincere. If you’re going to make something, make it properly. Why did it have such a serious defect that it turned people into deranged murderers?

“Good heavens.”

Jin Wikyung looked at me with eyes full of affection.

“I remember a small, adorable little boy who said he would grow up to become a chivalrous hero. You were six years old then. Do you remember?”

Of course I didn’t.

The events of the year before last were already hazy. How was I supposed to know what the original owner of this body had done at age six?

Still, I nodded solemnly.

“I remember it clearly. It was my only dream.”

Whether it was a chivalrous hero or the governor of Gyeonggi Province, as of this moment, that was my career aspiration at age six.

“Ha-ha. To think that little boy would grow up so splendidly.”

After laughing with satisfaction, Jin Wikyung turned toward the other two people.

“You were there too, Wipeng. Do you remember?”

Wipeng answered without even taking a breath.

“I don’t remember that, but I do remember him starting to womanize exactly ten years later. When I asked what he wanted to be when he grew up, he said he’d become the greatest ladies’ man under heaven.”

“A hero ought to know how to enjoy romance.”

“He doesn’t know squat about martial arts, so what good is knowing about romance? Is the hero you’re talking about a hero of the night, a hero to courtesans, or something?”

“Be quiet. Our youngest showed unusual promise from an early age.”

“So that promise… Ah, never mind. I should just stop talking.”

Glug, glug.

Jin Wikyung completely ignored Wipeng, who was pouring liquor straight from the bottle, and turned his attention to the next man in line.

“Mukyung. Now that you understand your little brother’s sincerity, let go of your anger.”

Jin Mukyung, who had been making a face like he’d swallowed something foul, finally spoke.

“Can’t I hit that bastard just once?”

“Now, now.”

“Just once. Please.”

At the icy voice, I quickly lowered my head.

“Please forgive this foolish little brother, Second Brother.”

“The bastard who’s been speaking casually to me this whole time is suddenly calling me ‘brother.’”

“Pardon? I am?”

“That’s enough. This is your final warning.”

“No. Hit me instead. If that would ease your anger, this little brother will gladly endure it.”

“You little shit!”

Jin Mukyung shot to his feet, then sank back down with a gasp. The bandages tied around his chest were turning red. It seemed his wound had reopened.

“Oh, no! Second Brother, are you all right?”

“This bastard, again… Guh!”

“Doctor! Doctor!”

The drinking party became a complete disaster in an instant.

Wipeng quietly picked up his second bottle and muttered,

“This family is really something…”

And how something it was—the foremost family in Shanxi.

* * *

The atmosphere finally settled down after the physician had come and gone.

I ignored Jin Mukyung’s murderous glare and took the Temporary Strength Pill from inside my robes.

“This is it.”

The pill was entirely red, as if blood had been condensed into a single sphere.

Jin Wikyung and Wipeng examined it closely.

“Wipeng, what do you think?”

“Just looking at it makes me smell blood. It’s a vicious object.”

“Could it really have been made by the Demonic Cult?”

“I couldn’t say. If it were, we should be able to sense demonic qi… but I can’t be certain.”

“Right? There’s something different about it.”

Both of them looked extremely serious. I was just as curious about where the Temporary Strength Pill had come from and who had made it, so I decided to give them a hint.

“They called it a Temporary Strength Pill.”

“A Temporary Strength Pill?”

“Yes. I heard it directly from Pung Yang.”

Jin Mukyung suddenly cut in.

“Pung Yang? When did you hear that?”

“While you were unconscious.”

“…Hoo. Hoo…”

I was the only eyewitness and witness, no matter what anyone said. As Jin Mukyung, who had gotten nowhere with his interruption, steadied his breathing to calm himself, the furrows between the other two men’s brows only deepened.

“A Temporary Strength Pill, Wipeng?”

“I’ve never heard of it either. If an object with this level of efficacy belonged to the Demonic Cult, it must have been used during the Great Faction War…”

“Could it not be the Demonic Cult?”

Their gazes turned toward me.

“Not the Demonic Cult?”

“What makes you think that?”

“I’m saying there’s no need to decide that from the start.”

In truth, I had said it out of hope that I might be able to take the pill back if it hadn’t been made by the Demonic Cult.

Of course, I had another thought as well.

*The Head Elder.*

The Mount Heng Sword Sect had certainly been the enemy that appeared on the surface during the last battle, but the true enemy had been the Head Elder himself.

Rather than making a simple either-or assumption, I believed we always had to keep open the possibility that there might be a third faction involved.

“Well, it just suddenly occurred to me.”

After hearing me out, the other two men’s expressions grew strange. Then, in the next moment, a very quiet voice escaped Wipeng’s lips.

It was a single word that slipped out unconsciously, like a groan.

“Dark Heaven…”

“Wipeng.”

Jin Wikyung’s sharp gaze cut off whatever he had been about to say.

“Ah, I apologize. I misspoke.”

Wipeng hurriedly tried to cover it up.

But it was already too late.

The two words *Dark Heaven* had been deeply etched into my mind.

*Dark Heaven? What is that?*

Then something unexpected happened.

> **System**
>
> You have obtained a small amount of information about **Dark Heaven**.
>
> The item description for the **Temporary Strength Pill** will be updated.

It was a completely sudden System notification. I held out my hand toward Wipeng, who was holding the Temporary Strength Pill.

“May I take a quick look?”

“Of course.”

*Item check.*

As soon as I muttered the words in my mind, information about the Temporary Strength Pill appeared.

Finding the changed information was easy.

> **System**
>
> **Item Window**
>
> **Temporary Strength Pill**
>
> **Type:** Elixir  
> **Grade:** ???  
> **Restriction:** Peak martial artist or higher  
> **Description:** A pill manufactured by **Dark Heaven**. For approximately one shichen, it dramatically raises the user’s latent power, but a price follows. Do not take it except in the worst circumstances.  
> **Effects:** Combat-related stats +100  
> Internal energy +15 years  
> Body-Protecting Qi available

The phrase *Someone Unknown* had disappeared, replaced by the unfamiliar term *Dark Heaven*.

*Judging by the context, it’s definitely some kind of organization…*

Well, anyone capable of making something like the Temporary Strength Pill was bound to be no better than the Demonic Cult. Same rotten lot, different name.

*Dark Heaven.*

Whoever came up with the name had incredible instincts. Two words were enough to tell everyone they were suspicious bastards.

*These guys definitely have something rotten going on behind the scenes. Ninety-nine percent sure.*

*Jin Wikyung and Wipeng seem to know something.*

The problem was that, judging by their reactions, they were extremely reluctant to reveal anything about Dark Heaven.

*Should I poke at them once?*

But before I could open my mouth, Jin Mukyung beat me to it.

“Dark Heaven? What is that?”

“Well…”

A troubled look crossed Jin Wikyung’s face.

“I’m sorry. I can’t tell you yet.”

Those words came from a man who cared deeply for his younger brothers.

If Jin Wikyung was unwilling to speak, there was no need to ask Wipeng.

“I apologize, Young Masters, but I cannot tell you until the matter becomes clearer.”

His attitude was firmer than anything I had seen from him before. Both Jin Mukyung and I realized that we had to withdraw for today.

But the more they tried to hide it, the more curious I became about Dark Heaven.

*So it’s a secret they have to keep hidden even from us.*

Even putting aside the fact that Mukyung and I were direct descendants of the family, we were core masters of the Jin Family of Taiyuan. If Wipeng was Jin Wikyung’s right arm, the two of us were each more than qualified to serve as his left arm or one of his legs.

*Then it must be a top-secret matter known only to those two, even within the family.*

I was only human, so I couldn’t help being curious. The fact that the System had reacted this time, despite remaining silent during the Mount Heng Sword Sect incident, also played a part.

*Dark Heaven. The Temporary Strength Pill. A top-secret matter known only to Jin Wikyung and Wipeng.*

Several keywords flashed through my mind.

All right. I’d made up my mind.

*I’ll ignore it and go on living.*

Excessive curiosity had a way of shortening one’s life. It had only been a few days since I’d gone to deliver the mail to the Mount Heng Sword Sect and nearly died.

A mysterious organization whose very name was ominous? If I got involved with them, it was obvious things wouldn’t end well.

“Well, let’s stop talking about this and have another drink.”

Jin Wikyung forced the mood back to normal.

Wipeng, who had already demolished two bottles by himself, was filling his glass, and so was the injured Mukyung. How could I be the only one to sit out? I accepted the liquor Jin Wikyung poured and downed it in one gulp.

Gulp, gulp.

The notorious fire liquor burned its way down my throat with a fierce heat.

“Guhhh.”

Wow. This was no joke.

I knew it was strong, but drinking it myself, it was far more potent than I’d expected. At this strength, soju and beer couldn’t even hold a candle to it.

Unlike me, who shuddered from head to toe, the other three immediately filled their empty glasses to the brim.

“Drink!”

“Down it!”

“Let’s keep going until we drop!”

“….”

I didn’t learn that Shanxi Province belonged to North China, or that every man from North China was an incredible drinker, until after we spent the entire night drinking.

* * *

The next day at noon, Hyuk Mujin stared at me as if I were a monster when I mounted my horse in a perfectly refreshed mood.

“Is your stomach all right?”

“Yeah. Why wouldn’t it be?”

“Don’t tell me you were the only one who didn’t drink yesterday. Or did you fall asleep halfway through?”

“No. The four of us kept drinking.”

“…All of it?”

His mouth fell open.

“Is that even possible? Are you human?”

“It all fit.”

“My goodness. How many bottles did you drink through the night?”

He had the wrong unit.

It wasn’t bottles. It was barrels.

We kept emptying massive casks of liquor—the kind I’d only ever seen in pirate movies—and then emptying more.

“I think it was close to twenty barrels. I stopped counting after ten, so I’m not sure.”

“Wow. That’s incredible.”

Hyuk Mujin raised his thumb in admiration when the inn door suddenly opened.

And three zombies—or rather, three Peak masters—appeared.

“Uuugh.”

“Urk.”

“Huff, huff.”

Their faces were pale, their lips parched, and their eyes sunken.

Without a single exception, they dragged their feet and climbed straight into the carriage. The martial artists of the escort force stared at them with their eyes wide.

“Why are they suddenly getting into the carriage…?”

“They look really unwell.”

“That can’t be. Haven’t you ever drunk with our Commander? Wipeng, the God of Drinking? You don’t know?”

“Wasn’t the Commander’s epithet Ghost Sword?”

“Whatever else you might say, when it comes to drinking, he could probably beat even the Martial God. They’re probably just like this because all the fatigue they’ve accumulated finally caught up with them.”

As the martial artists whispered among themselves, the carriage door suddenly flew open, and one person hurriedly dashed out and bent over.

“Urrp, buuurrgh!”

Splaaarsh.

After pouring out a pale liquid for quite some time, Wipeng staggered back into the carriage. One of the martial artists who had been talking animatedly muttered in a dazed voice,

“…This can’t be.”

“It absolutely can. Anyone can see that’s a hangover. They drank all night without sleeping. Of course they’d end up like that.”

“Then why is the Third Young Master so perfectly fine?”

The escort force’s gazes all turned toward me.

The smell of liquor radiating from my entire body was strong enough to send chills down the spine. But in complete contrast, my face looked unbelievably refreshed, and my breathing was calm.

“No way…”

“The Third Young Master beat the Commander? That God of Drinking?”

The courtyard buzzed with excitement.

Hyuk Mujin’s look of admiration had gone beyond admiration and become outright reverence.

“Ah, I knew it! That’s our Captain—the man who used to drink with courtesans every damn day!”

“….”

“I remember what the Chief Steward said. If Captain had kept drinking for three more years, he would have uprooted the family’s entire foundation. So this is why you always had to steal from the family coffers!”

“…Hey, you punk.”

It wasn’t as if we were alone. If he talked like that, what would happen to my image?

As if the stares pouring in from every direction hadn’t already made my face feel hot enough.

“Ahem. Ahem!”

I cleared my throat and glanced around. And what do you know? The eyes of all those rough-looking men were sparkling brighter than stars in the night sky.

“A true God of Drinking. He really is.”

“He’s famous in Taiyuan’s red-light district. Haven’t you heard of the Night King?”

“The Night King? I can tell just from the epithet. So he was already renowned for his drinking.”

“No, not that… The other thing. That.”

“Gasp. Is it true?”

“How would I know? I’ve never seen it.”

“Turns out he really is a man among men.”

> **System**
>
> Everyone gathered here is impressed by your drinking capacity and imposing presence!
>
> **Fame** rises by 20!
>
> **Fame** rises by 22!
>
> **Fame** rises by 25!
>
> If a particular rumor spreads, you may obtain a related **Title**.

“….”

What the fuck was with my Fame shooting up like that?

And what did it mean, a related Title? No, it was fine. Put that away. Please, just let me be satisfied with the Sleeping Dragon of Shanxi.

*Stop it, you lunatics…*

With a mysterious sense of shame, I turned my head—and came face-to-face with Hyuk Mujin, who was staring intently at a certain part of me.

“…What are you doing?”

“Oh, I was just taking a rough measurement with my eyes.”

His answer was so straightforward that I was almost thrown off. Hyuk Mujin cheerfully extended his forearm.

“Wow. As expected, you’re amazing. Hehe.”

In return for the forearm, I offered him my fist.

Thwack!
## Chapter artifact 128

# Chapter 128

Old Man Jang woke to the sound of a commotion.

*What goddamn bastards are making all that noise?*

He was old enough that his hours of sleep were gradually dwindling, so this was hardly a welcome development.

*I’ll go see what their faces look like.*

Dragging his stiff body out of the thatched cottage, Old Man Jang’s eyes immediately fell on a crowd gathered like clouds.

There were hundreds of them, by his rough estimate. It looked as if everything in the village with legs—human or animal—had gathered in one place.

“What’s all this about?”

It was a small, unremarkable village, so he knew most of the faces.

At Old Man Jang’s muttering, a familiar market merchant greeted him.

“You’re awake, sir.”

“With this kind of racket, how could I stay asleep?”

“Ha-ha, please understand, sir. Everyone’s gathered because they heard an important guest was coming.”

Old Man Jang grunted.

“An important guest? Is the Emperor coming?”

“Oh, there you go again. Is the Emperor your friend?”

“By age, I’d be his father.”

“You’ll get arrested for treason talking like that. Can’t you see the government soldiers over there?”

“Government soldiers?”

Following the merchant’s nod, Old Man Jang spotted dozens of government troops and a man dressed in an official robe—the county magistrate. His eyes narrowed.

“That fellow never showed his face when the mounted bandits were prowling around, but now he’s dressed up in his official robes too? Is this important guest some high-ranking official?”

“Not a high-ranking official, but in Shanxi Province, they’re number one.”

The merchant raised his thumb.

At that very moment, an uproar erupted from the assembled crowd.

“They’re coming!”

“They’re here!”

Old Man Jang turned his head in the direction of everyone’s gaze. When he saw fifty mounted riders charging toward them from the distance, their flags snapping in the wind, he finally understood who the important guests were.

*The Jin Family of Taiyuan.*

Old Man Jang had little interest in the affairs of the world, but he had heard the name of the Jin Family of Taiyuan until his ears rang.

A prestigious family that had maintained its lineage for three hundred years, and the hegemon that held Shanxi Province in its grasp.

As Old Man Jang watched the imposing procession, his brow suddenly furrowed.

*Who was that fellow again? That… what was it? Shanxi, Shanxi… some kind of dragon?*

Age had weakened his memory as well. As Old Man Jang lamented the passing years, one person caught his eye.

“Say, who’s that young man?”

“Ah, that Young Hero?”

There were dozens of martial artists from the Jin Family of Taiyuan alone, all clearly visible. Yet the merchant immediately understood whom he meant.

An awl in a pocket. The young man’s presence was like an awl tucked inside a pouch, bound to stand out wherever he went, so there was nothing strange about it.

“That’s the Sleeping Dragon of Shanxi.”

Shing—

As if he had heard those words, the young man at the head of the procession drew the sword at his waist.

The transparent blade flashed in the sunlight, and a thunderous cheer erupted.

“Waaaaaah!”

“Jin Family of Taiyuan! Sleeping Dragon of Shanxi! Heaven Shaking Sword!”

* * *

“Sleeping Dragon of Shanxi! Jin Taekyung! Sleeping Dragon of Shanxi! Jin Taekyung!”

My epithet and name rang out from every direction. Even though I’d already experienced this several times over the past few days, it still made me feel proud.

*Is this how idols feel?*

It was just like that thing. *Milky-skinned Jin Taekyung. We love you, Jin Taekyung.*

An idol fan club, the kind I’d only ever seen on music variety shows, was right in front of me. Smiling contentedly, I drew the [Unnamed Sword] from my waist.

Shhhng. Flash!

Maybe it was the Ten-Thousand-Year Cold Iron brand, but nothing else came close when it came to visual effects.

“Waaaaaah!”

“Eeeeek! Young Master, take me!”

“Wah! Wah!”

A man for everyone, like something rated for all audiences—men and women, young and old.

That man was me.

Ding.



> **System**
>
> **Fame** rises by 19!
>
> **Fame** rises by 26!
>
> **Fame** rises by 31!
>
> …
>
> …
>
> **Fame** rises significantly!
>
> Due to the increase in **Fame**, the effect of the **Sleeping Dragon of Shanxi** **Title** has been strengthened!

*The Title effect has been strengthened?*

That was an unexpected bonus. I opened my Status Window to check the changes.

Ding.



> **System**
>
> **Status Window**
>
> **Lv. 61 Jin Taekyung**
>
> **Class:** First Rate martial artist
>
> **Fame:** 2,100 (+250)
>
> **Titles:** 4 (Title effects active)
>
> — Returned One (All stats +10)
>
> — Sleeping Dragon of Shanxi (All stats +15, Fame +200)
>
> — Scion of a Prestigious Family (All stats +5, Fame +50)
>
> — Gambler (Combat-related stats +10% in one-on-one combat)
>
> **Strength:** 196 (+30)  
> **Stamina:** 195 (+30)
>
> **Agility:** 192 (+30)  
> **Intelligence:** 35 (+30)
>
> **Charm:** 35 (+30)  
> **Internal energy:** 45 years
>
> **Toughness:** 155 (+30)
>
> **Remaining points:** 60
>
> — Distribute your remaining points.



The Sleeping Dragon of Shanxi’s Title effect had definitely changed from All stats +10 and Fame +100.

*So my name carries more weight now?*

Titles didn’t simply drop from the heavens.

In my case, rumors about me being some kind of sleeping dragon had gradually spread, and at some point, my Fame rose and I gained the Title Sleeping Dragon of Shanxi.

It seemed that the effect of a Title increased along with one’s Fame.

*My Level has already passed sixty, too.*

The Status Window, which I hadn’t checked in a while, had grown by leaps and bounds. My Fame had shot up, my combat-related stats were approaching 200, and I had a solid forty-five years of internal energy.

*Hehehe. Innkeeper!*

I shuddered with exhilaration, and Hyuk Mujin, who was carrying a flag on my right, looked at me as if I were mentally ill.

“Are you really that happy?”

I deliberately put on a serious face.

“Who said I was happy? People like me, so I was just helping to liven up the mood.”

“……I have a lot to say, but I won’t.”

“Wise choice.”

Walking amid the crowd’s cheers, we pulled on the reins and slowed down.

Dozens of men had poured out into the street and blocked our path.

Among them, a fat man dressed in splendid red robes smiled broadly at me.

“Heh-heh, you’re every bit as dignified and handsome as I’d heard. I’ve long been familiar with the great reputation of the Sleeping Dragon of Shanxi.”

“Ah, yes.”

Confused, I asked,

“But who are you?”

Hyuk Mujin hurriedly whispered,

“He’s the county magistrate. The county magistrate.”

“What’s a county magistrate?”

“What? You don’t even know what a county magistrate is?”

“Is he like a village head?”

“Wow, this is driving me crazy. Just think of him as an official.”

“An official. Then are the people behind him government troops?”

“……Why are you acting like you’ve never seen government troops before?”

“No, I just find it interesting.”

In fact, I really had never seen them before.

I studied the fat man—no, the county magistrate—and his subordinates carefully.

I knew that this world had a government, official offices, and law-enforcement agencies, but this was the first time I’d actually encountered them.

*How could they never show even the tips of their noses?*

Violent crimes happened dozens of times a day in this neighborhood, yet I had never once seen government troops drag away a criminal.

Then again, considering the authorities hadn’t intervened in the Battle of Eight Spring Gorge, where roughly two thousand people had clashed, or in this latest incident involving the Red Wind Band, perhaps that was only natural.

*It’s not as if they’re even beating up the mounted bandits who loiter around.*

What exactly did these bastards do?

I was imagining that, if this were modern times, half the martial artists in the Murim would be locked in solitary confinement for murder when the county magistrate cleared his throat.

“Ahem. Ahem!”

His face flushed red as he coughed awkwardly.

He was an official with a certain position, after all, and seemed offended that I had ignored him.

“Oh, I’m sorry. I injured my head a while ago, so I keep spacing out.”

I’d only offered a reasonable excuse, but the county magistrate’s expression relaxed slightly.

“Ahem, no, no. You must have gone through great hardship dealing with those vicious mounted bandits. Ah, I heard you killed more than five hundred of them?”

“Uh… five hundred?”

“That’s right. I was overjoyed to hear the tales of valor of the two heroes, the Heaven Shaking Sword and the Sleeping Dragon of Shanxi. Ha-ha.”

I had no idea where that number had come from.

Even if you counted every mounted bandit who took part in the battle, there might have been three hundred at most. And by the time Jin Mukyung and I arrived, fewer than a hundred of them had remained.

*In reality, there was Pung Yang and maybe seventy mounted bandits who were already exhausted. Something like that.*

Well, rumors were usually exaggerated.

“Come on, that’s too—”

Just as I was about to explain the truth, murmurs spread through the people who had been listening to my conversation with the county magistrate.

“Five hundred? Didn’t the Sleeping Dragon of Shanxi and the Heaven Shaking Sword go there alone?”

“Good heavens. The two of them defeated a mounted-bandit force of more than five hundred?”

“How can human beings be that strong?”

Ding.



> **System**
>
> People are looking at you with awe.
>
> **Fame** rises by 40!



“Too what did you say?”

I continued speaking to the bewildered county magistrate.

“That’s a serious understatement. In reality, there were nearly six hundred.”

“Six hundred!”

“My second brother and I took half each.”

“Then three hundred each!”

“Hmm. More precisely, about 285?”

The county magistrate—and even the government troops—gaped at me.

“Ooh!”

“Two hundred and eighty-five! And he even knows the exact number!”

Ding.



> **System**
>
> People are looking at you with awe.
>
> **Fame** rises by 40!



This time, Hyuk Mujin whispered to me with an expression usually reserved for looking at a bug.

“Do you really want to take it this far?”

“Yep.”

“What are you going to do if you inflate your achievements for no reason and get caught lying?”

“You, Wolhwa, and the Mount Heng Sword Sect just have to keep your mouths shut. So hurry up and back me up.”

“I refuse. Hyuk Mujin may not look it, but I’ve lived a truthful life without a single shameful moment before the heavens.”

I stared at him in disbelief.

“When Jin Mukyung destroyed my pavilion, weren’t you the one who fought assassins that didn’t even exist?”

“…….”

“If you have nothing to say, shut up and manage your expression. My two hundred and eighty… How many was it?”

“Two hundred and eighty-five.”

“Right. I’ll count about thirty of them as your kills. If you were born with balls, you ought to make Master of the Gatekeeper Pavilion in the Jin Family of Taiyuan at least once in your life. Don’t you think?”

“……!”

Hyuk Mujin, who had lived a truthful life without a single shameful moment before the heavens, used his dazzling tongue to completely win over the county magistrate.

The mounted bandits, most of whom had been Second Rate or Third Rate, became First Rate masters to a man—each a Lü Bu astride Red Hare. Pung Yang became an invincible master who could cleave mountains and seas with a single sword strike.

*From now on, I’m filtering anything that comes out of this bastard’s mouth.*

He was such a skilled liar that even I found myself wondering whether it was true. If even I, the person involved, was confused, there was no hope for anyone else.

“……and that was how Pung Yang, the absolute ruler of Gaoyuan, and the vicious Red Wind Band came to meet their end at the Mount Heng Sword Sect.”

The moment Hyuk Mujin finished his bullshit—his story, I mean—sighs of disappointment rose from all around us. The county magistrate’s reaction was the most enthusiastic of all.

“Whaaaat? How could such a thing happen? The Murim is truly a wondrous yet terrifying place.”

Hyuk Mujin swept his gaze over the crowd with melancholy eyes.

“A martial brute like me has no fear. Ever since I took up the sword, I’ve lived with death as my companion. But if I have one wish…”

“One wish?”

“To die by the sword of someone strong. That is all I could ask for.”

“…….”

At this point, this was a bumper crop of bullshit.

Suppressing the urge to smack Hyuk Mujin in the back of the head, I stepped forward.

I had already milked the Fame for all it was worth, and there was no reason to keep talking to a potbellied middle-aged man.

“Sorry to interrupt, but we’re in a hurry.”

The county magistrate, who had been gazing at Hyuk Mujin with dazed eyes as if hypnotized, suddenly came to his senses.

“Ah, my apologies. I didn’t mean for this to happen.”

“Then do you have some other business?”

“Could I meet Great Hero Jin? I mean, the Lesser Family Head.”

The county magistrate’s gaze shifted toward the carriage behind me.

They couldn’t be seen from outside, but Jin Wikyung, Jin Mukyung, and Wipeng were inside.

*Because they were drunk out of their minds.*

They were the losers who had been utterly crushed by me in our drinking contest over the past three days. But how could I tell him the truth? Without changing my expression, I lied.

“I’m sorry, but he’s currently circulating his qi and won’t be able to see you. As you know, County Magistrate, it’s quite dangerous.”

“Ah, I see. Then it can’t be helped.”

The county magistrate clicked his tongue, then pulled a tightly rolled piece of paper from his sleeve and handed it to me.

“What is this?”

“An invitation from the City Lord. After hearing about your recent exploits, Young Hero Jin, he seems to have been deeply impressed, so he arranged a gathering with several young prodigies.”

Ding.



> **System**
>
> A **Quest** has been created.
## Chapter artifact 129

# Chapter 129

Ding.

> **System**
>
> A **Quest** has been created.
>
> **Quest**
>
> **The City Lord’s Invitation**
>
> High renown is bound to attract attention.
>
> The City Lord of Shanxi Province, having heard rumors about the Sleeping Dragon of Shanxi, invites you to a luncheon with several young prodigies tomorrow.
>
> **Grade:** Third Rate
>
> **Restriction:** Jin Taekyung
>
> **Objective:** Attend the luncheon hosted by the City Lord (Incomplete)
>
> **Reward:** Varies according to the City Lord’s reaction.
>
> **Failure:** The City Lord becomes extremely depressed.
>
> Would you like to accept the Quest?
>
> **Y / N**
>
> ※ If you reject the Quest, the City Lord may sulk.

*The City Lord wants me?*

It was certainly unexpected, but not all that surprising. A person’s fame was often used by politicians, after all.

Of course, this was a world where media had almost no reach, so personal curiosity was probably the greater factor.

But…

*What do you mean, the City Lord might sulk if I reject the Quest?*

What was there to sulk about? The thought of a five-chin-folded middle-aged man sulking sent goose bumps all over my body.

“Young Hero?”

Pretending not to notice the county magistrate’s puzzled expression, I scratched my chin.

*Hmm. What a pain.*

It was only a Third Rate Quest. The EXP and Fame I could gain would probably be minimal, and I’d have to carefully flatter the City Lord to obtain the reward.

Wouldn’t it be better to spend that time practicing martial arts instead?

*It’s not like I’m someone who has to come running the instant the City Lord calls.*

I was on my way back after a battle in which I had nearly lost my life. I didn’t particularly want to have lunch tomorrow with some middle-aged man called the City Lord whose face I had never even seen.

If I rejected the Quest, the worst that could happen was that he’d sulk. Whatever. He could sulk as much as he wanted.

I was just about to turn him down as politely as possible when—

Grab.

“We’ll go. Absolutely!”

Hyuk Mujin suddenly stepped forward and snatched the invitation. The county magistrate frowned.

“I don’t believe I invited you.”

His voice was cold, unlike before. Hyuk Mujin didn’t care in the slightest. He simply flashed a shameless smile.

“Oh my, of course you didn’t. It’s just that our Young Master has always respected the City Lord so deeply that he was too moved to speak.”

The county magistrate stared at me through narrowed eyes.

“Hmm. Is that true?”

Of course it wasn’t.

I was about to say so when Hyuk Mujin, having turned his back to the county magistrate, silently mouthed at me.

*You absolutely have to go?*

Unlike usual, he looked strangely desperate.

I made a quick decision.

“Of course. Is there anyone in Shanxi who doesn’t respect the City Lord?”

“Ha-ha, truly the words of a citizen of a great nation. The City Lord will be delighted to hear that.”

Only then did the county magistrate relax his face and smile with satisfaction. He turned around.

“Then I’ll consider it accepted and take my leave. Please convey my regards to the Lesser Family Head and the Heaven Shaking Sword.”

“Ah, of course.”

Ding.

> **System**
>
> You have accepted the **The City Lord’s Invitation** Quest!

The System notification rang out.

*Now I can’t even cancel it.*

Once the county magistrate and the government troops had moved away, I whispered as I pressed my foot down on Hyuk Mujin’s.

“I think you have something to tell me, don’t you?”

“I’ll explain. First, let’s get out of here.”

There were still too many eyes watching us. Amid the people’s cheers, we mounted our horses again.

We proceeded farther into the village and reached our destination. A little errand boy shot out like a bullet and bowed at the waist.

“Welcome—gasp.”

He was startled once by the fifty mounted riders and the intimidating presence of the escort, then a second time when he recognized Hyuk Mujin and me.

He was the errand boy from the Phoenix Inn. I had seen him a few days ago.

“The private annex is fifty nyang of silver for one night. That’s right, isn’t it?”

“Uh, you’re the one from back then?”

“Hey, you little brat. Are you pointing at a guest as lofty as the heavens?”

After scolding the boy in a stern voice, Hyuk Mujin tossed him a heavy money pouch.

The little boy glanced nervously between us, then inhaled sharply when he saw the pouch packed with silver.

“Gasp. Th-this much?”

“From this moment on, the Phoenix Inn is under the control of the Jin Family of Taiyuan.”

“…Are you some kind of two-knife gangster?”

Anyone watching would have thought we were members of organized crime.

* * *

The three zombies climbed out of the carriage and began gulping down the broth the moment the food arrived.

It was understandable, considering they had spent three days drinking to excess without taking a single day off. No—if they hadn’t practiced martial arts, they might have died of alcohol poisoning on the first day.

“Guhhh, I feel alive again.”

The instant Jin Wikyung leaned back in his chair after finishing his hangover cure, Wipeng’s nagging flew at him.

“My lord, please maintain your dignity. Your dignity.”

“What does it matter? We’re the only ones here.”

“Even so, what will your subordinates think if you keep showing them this side of yourself?”

“It’s fine. I didn’t throw up.”

With a single sentence, Jin Wikyung silenced Wipeng. Then he turned to me.

“So, the county magistrate came by?”

“Yes. He said the City Lord was inviting me to a luncheon tomorrow.”

“The City Lord?”

“I don’t know why, but he seemed interested in me. I was planning to reject it, but some thoughtless idiot accepted it without hesitation.”

“Did he? Who on earth would do that?”

Hyuk Mujin, who had been sitting in the corner of the table and nervously watching our expressions, answered in a tiny voice.

“That would be me, Lesser Family Head.”

“Ah, I see. You’re the fellow who’s supposed to be our youngest brother’s right-hand man. The one who was in the Gatekeeper Pavilion until recently. Your name was… Hyuk Mujin, wasn’t it?”

Compared to the modern world, the Jin Family of Taiyuan was a conglomerate, while Jin Wikyung was the chairman’s eldest son and the actual head of the company.

Assistant Manager Hyuk, who had spent all his time being bullied under a foul-tempered boss, answered in a deeply moved voice.

“Ah, thank you for remembering me.”

“I should be thanking you. Our youngest brother still has some rough edges, so continue helping him as you did today.”

“A-as you command!”

“Ha-ha. It’s good to see such spirit.”

Jin Wikyung laughed cheerfully, then turned back to me.

“Accepting the City Lord’s invitation was absolutely the right thing to do.”

“Really? From what I’ve experienced so far, he doesn’t seem to have much to do with the Murim.”

“For a long time, the government and the Murim have maintained a relationship of noninterference. Do you know that?”

“Yes, more or less.”

I had learned about the Murim through novels. The common settings in martial-arts fiction weren’t all that different here in the Murim.

“They recognize each other’s domains, but there is nothing to be gained by offending the government. The Murim is merely one part of the world. The world is not the Murim.”

Jin Wikyung pointed toward the bowl in front of him. It contained half a bowl of broth and one large chunk of meat.

“Do you understand what I mean?”

I nodded.

The bowl was the world, and the chunk of meat inside it was the Murim.

“We are martial artists, but it is the Emperor who rules the world. Among the people, the authority of the Son of Heaven is absolute. The City Lords govern their respective provinces under the Emperor’s command, so they possess considerable power and authority.”

“More than the Jin Family of Taiyuan?”

“In terms of authority alone, yes. We simply recognize and respect each other’s power. Murim sects sometimes take responsibility for maintaining public order when the government cannot resolve a problem, and they also dispatch martial arts instructors to train government troops. The government offers assistance in return, so the two sides help each other.”

So the government and the Murim were like the crocodile and the crocodile bird.

After thinking for a moment, I finally voiced the question that had been bothering me since earlier.

“Then why do you sit back and do nothing when mounted bandits run wild or large-scale battles break out between sects? I can understand staying out of the last war because it was a matter between martial artists, but the mounted bandits are different, aren’t they?”

Lee Cheonbaek had massacred everyone at the Sakju Branch and committed the insane act of killing children, but the victims had belonged to the Jin Family of Taiyuan.

Strictly speaking, they could be considered people who had been sacrificed to the gratitude and grudges between Murim sects.

But the mounted bandits killed indiscriminately and burned everything in their path, didn’t they?

*From the mounted bandits’ perspective, commoners were easy prey.*

They were weak before the strong and strong before the weak. That was what mounted bandits were.

The important point was that I had encountered dozens of mounted bandits on the way to the Mount Heng Sword Sect, yet I hadn’t even seen a government soldier.

“That’s…”

Jin Wikyung let his voice trail off. Jin Mukyung, who had been silently inhaling his food until then, suddenly spoke.

“Because the City Lord is incompetent. No, in this case, is the Emperor incompetent?”

The moment he finished speaking, Hyuk Mujin had a fit, while Jin Wikyung and Wipeng deliberately hardened their expressions.

“Hey, Mukyung.”

“It’s just us here. No one can overhear us. And I haven’t said anything untrue.”

“Second Young Master, our family does not yet stand alongside the Nine Sects and One Gang or the Five Great Families. Please refrain from saying anything that could cause trouble.”

I asked Jin Mukyung, who reluctantly nodded.

“What do you mean, the City Lord is incompetent?”

“Do you not know the meaning of the word incompetent?”

“Should I report you to the authorities for insulting the Emperor?”

“Treason gets at least three clans punished. Congratulations, little brother.”

*This guy Jin Mukyung has gotten pretty good with words.*

“Do you know who the City Lord is right now?”

“Kim Chunbae?”

“…If you don’t know, just say you don’t know.”

He looked at me as if I were a bug, then continued.

“The current City Lord of Shanxi has the surname Zhu.”

“So?”

“What do you mean, ‘so’? He’s a member of the imperial family. The imperial family!”

“Oh, really?”

It seemed to be a Zhu dynasty. I had been branded an ignorant fool who didn’t even know the Emperor’s surname in the space of a moment.

Still, it wasn’t as if this sort of thing had only happened once or twice. I wasn’t even embarrassed anymore.

“Fine, I get it. Continue.”

Jin Mukyung sighed deeply and went on.

“The current City Lord is the Emperor’s youngest brother. His imperial title is a Prince. He is a direct member of the imperial family, so he stands on a different level from the other City Lords. He is someone whose invitation we must accept, even if only to preserve his dignity.”

“Oh.”

He really was on a different level. Not just an ordinary City Lord, but the Emperor’s brother. An actual king, no less.

Born the son of the Son of Heaven and then becoming the younger brother of the Son of Heaven, he wasn’t merely born with a silver spoon in his mouth. He had a vibranium spoon.

The North Korean nuclear spoon of the modern world—and then some.

“Then how can someone who’s practically a king be so incompetent? If he writes his brother a single letter, he could get all the support he needs from above. Are they on bad terms?”

“Who knows? I don’t know the details of that family’s circumstances, but they don’t seem particularly close. There are rumors that the current Emperor assassinated the Crown Prince, the brother immediately older than him, before ascending the throne.”

“Talk about a hunger for power.”

“People kill over a single dumpling. Imagine what they’d do for the imperial throne.”

Jin Wikyung and Wipeng’s mouths fell open, while Hyuk Mujin had another fit.

“Judge, I didn’t hear anything. I truly know nothing. In fact, I haven’t been able to hear for a long time…”

As Hyuk Mujin muttered like a madman, Jin Mukyung smacked him across the back of the head. I asked,

“Does he not receive support because he’s on bad terms with the Emperor? Or is he simply lost in alcohol and women?”

“Alcohol? Women?”

Jin Mukyung let out another quiet laugh.

“He’s only ten years old. It’s too early for him to lose himself in wine and women.”

“What, ten? You mean a ten-year-old is the City Lord?”

“He’s a direct member of the imperial family. He has the bloodline to become more than a City Lord.”

The System message I’d seen earlier suddenly came to mind.

> If you reject the Quest, the City Lord may sulk.

I had thought it was ridiculous for a middle-aged man to act so childish, but now that I knew he was a ten-year-old boy, it finally made sense.

Wasn’t that the age when you’d sulk at a falling leaf?

“The more amusing fact is that he was first appointed City Lord five years ago.”

“…Five years old? That’s insane.”

What could a five-year-old possibly know? I could roughly guess why the public order in Shanxi Province had become such a mess. I also understood why Jin Mukyung had said that the Emperor, rather than the City Lord, was more incompetent.

This wasn’t some neighborhood convenience store. They had put a child in a position that demanded ability and responsibility. There was no way things could run properly.

“How do you know all this?”

I asked because it was surprising that Jin Mukyung, who had been obsessed with martial arts and nothing else, was so well-informed about current affairs.

The answer I received was unexpected.

“Because I’ve met him before. More accurately, I was summoned.”

“Oh, really?”

“Three years ago.”

Well, if I was the rising super rookie of the moment, Jin Mukyung was already an established Peak master. It made sense that he would have been invited before me.

“What was he like?”

Jin Mukyung looked at me with a strange glint in his eyes.

Then, wearing an ominous expression that mixed laughter with irritation, he spoke.

“He was a fucking nightmare.”

# Checkpoint Review — 190–194

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

# Chapters 190–194

## Plot

Jin Taekyung defeats Chulwoo by exploiting his superior speed, completing the quest *There Is a Man Who Loved You So Much* and winning the Jin Family of Taiyuan Duel Tournament. The victory brings level-ups, Fame, EXP, and bonus stat points. Baek Museong acknowledges Taekyung’s talent and apologizes for his earlier contempt.

The celebration is interrupted by Song Il, the Roaring Fury Swordsman and an Elder of the Zhongnan Sect. Claiming that Cheongpung seriously injured Gong Ilhyuk, Song demands compensation, insults the Jin Family, and orders it to seal its gates. When Jin Wikyung and Taekyung reject his authority, Song attacks Taekyung with the Heavenly River Thirty-Six Swords.

Jeok Cheongang, the Fire King, intervenes and reveals that he entrusted Taekyung with the Fire Gate Clan’s sacred treasure—the Unnamed Sword. He humiliates Song, forces him to swear not to pursue the Jin Family, and later breaks his wrist and strikes him with the Flame Divine Palm after Song attacks the Three Hands of Zhongnan. Jeok threatens to destroy the Zhongnan Sect and Mount Zhongnan if Taekyung or the Jin Family is harmed.

Jeok then returns to the Jin Family and dominates a banquet with his shameless demands and gruff humor. He accepts gifts from merchants and martial artists, including a Poison-Averting Ring and bank drafts tied to a vague request involving the Hebei Peng Family. He denies being friends with the Thunderbolt Saber King, explaining that their only meeting ended in a drinking session followed by a fight. Before leaving to rest, Jeok gives Taekyung the accumulated treasures, elixirs, and bank drafts, leaving Taekyung to wonder whether Jeok intends to make him his Disciple.

## Continuity

- Taekyung defeated Chulwoo, completed *There Is a Man Who Loved You So Much*, won the Jin Family tournament event, and reached Level 73. His Strength is above 300, and he has seventy allocated stat points.
- Song Il is a Zhongnan Elder, the Roaring Fury Swordsman, and the senior brother of Sect Leader Gong Iljung. He attacked Taekyung, was defeated and humiliated by Jeok Cheongang, and swore not to pursue the Jin Family.
- Jeok Cheongang is the Fire King, has reached the Supreme Peak realm, and publicly confirmed that the Unnamed Sword is the Fire Gate Clan’s sacred treasure entrusted to Taekyung.
- Jeok threatened to destroy the Zhongnan Sect and Mount Zhongnan if Song Il or Zhongnan harms Taekyung or the Jin Family. Song ordered the unconscious Three Hands of Zhongnan to return to Zhongnan.
- Gong Ilhyuk provoked the confrontation and was rendered unconscious by Song Il along with the other two members of the Three Hands.
- Jeok’s past with the Thunderbolt Saber King was one drinking encounter followed by a fight, not friendship; Jeok says the Peng Family fabricated the later story of mutual recognition.
- Jeok offered Taekyung all gifts collected at the banquet, including treasures, elixirs, and bank drafts.
- Jeok’s possible intention to take Taekyung as a Disciple remains unresolved.
- Jang Taebo’s Ten-Thousand-Year Cold Iron spear for Taekyung is still unfinished, and the Treasured Jade remains unaccounted for.
- Dark Heaven’s objective, the identities and potential information of the three surviving remnants, and the reason for targeting Shanxi remain unresolved.
- The consequences of Woo Hwangtae’s conflict with Chulwoo and the Jin Family remain unresolved.
- Lee Seowol and the Mount Heng Sword Sect remain vassals of the Jin Family; Chulwoo remains in love with Seowol.

## Translation Decisions

- Render 화왕 as “Fire King,” 화염신장 as “Flame Divine Palm,” 만년한철 as “Ten-Thousand-Year Cold Iron,” and 이름 없는 검 as “Unnamed Sword.”
- Render 열화문의 신물 as “Fire Gate Clan’s sacred treasure,” referring to the Unnamed Sword.
- Render 암천 as “Dark Heaven,” 전음 as “Sound Transmission,” 육합전성 as “Six-Harmonies Voice Transmission,” and 천하삼십육검 as “Heavenly River Thirty-Six Swords.”
- Render 피독지환 as “Poison-Averting Ring,” 철혈도 as “Iron Blood Saber,” 양천상회 as “Yangcheon Merchant Association,” and 종남산 as “Mount Zhongnan.”
- Retain “Roaring Fury Swordsman,” “Three Hands,” “Tongue King,” and “Young Lady” as established names or forms of address.
- Preserve Jeok Cheongang’s gruff, shameless, teasing voice and Taekyung’s blunt profanity when they reject Song Il’s abuse of authority.

## Durable state

{
  "active_continuity": [
    "The Unnamed Sword is the Fire Gate Clan’s sacred treasure, and Jeok Cheongang entrusted it to Jin Taekyung; this secret is public before the Jin Family and Zhongnan visitors.",
    "Jeok Cheongang publicly threatened to destroy the Zhongnan Sect and Mount Zhongnan if Song Il or the Zhongnan Sect harms Taekyung or the Jin Family.",
    "Song Il left the Jin Family humiliated and injured, ordered the Three Hands of Zhongnan to return to Zhongnan, and abandoned his threat after Jeok’s warning.",
    "Gong Ilhyuk incited Song Il to confront the Jin Family and was rendered unconscious by Song Il along with the other two members of the Three Hands.",
    "Three Dark Heaven remnants survived interrogation under powerful restrictions, and Wipeng was ordered to keep them alive as the Jin Family’s only physical evidence.",
    "Jin Wikyung suspects Dark Heaven’s attack on Shanxi Province was only the beginning and considers the Jin Family’s victory suspiciously easy.",
    "Lee Seowol and the Mount Heng Sword Sect swore loyalty to the Jin Family of Taiyuan on New Year’s Day, and the Jin Family accepted the sect as its vassal.",
    "Chulwoo is twenty-five, has fallen intensely in love with Lee Seowol, and lost his challenge to Taekyung after seeing him interact with Seowol.",
    "Taekyung is a Peak Master with Sound Transmission access, current Strength above 300, Level 73, and seventy allocated stat points; he completed the duel Quest and won the Jin Family tournament event.",
    "Cheongpung says Taekyung’s victory relied on extraordinary speed and that Taekyung read and countered Crouching Tiger Fist after two days.",
    "Song Il is an Elder of the Zhongnan Sect, the Roaring Fury Swordsman, and the senior brother of Sect Leader Gong Iljung; he attacked Taekyung with the Heavenly River Thirty-Six Swords before Jeok stopped him.",
    "Jeok Cheongang is the Fire King, whose presence and voice demonstrate Supreme Peak power; he fought Sword Saint Mae Jonghak to a draw and later rescued and accepted Jangcheon as his Disciple.",
    "Jeok Cheongang regards Jangcheon as an only son and grandson despite their lack of blood relation, but Jangcheon became Jopil and was killed by Taekyung.",
    "Jang Taebo agreed to forge Taekyung’s Ten-Thousand-Year Cold Iron into a spear, but the work is not yet complete.",
    "The Treasured Jade remains missing, and Jopil’s possession or loss of it has not been resolved.",
    "Woo Hwangtae’s conflict with Chulwoo and the Jin Family remains unresolved.",
    "Jin Wikyung is thirty-six years old and unmarried.",
    "Jeok Cheongang’s past with the Thunderbolt Saber King was a drinking encounter followed by a fight, not friendship; Jeok says the later mutual-recognition story was fabricated by the Peng Family.",
    "Jeok Cheongang accepted numerous gifts at the Jin Family banquet and offered the accumulated treasures, elixirs, and bank drafts to Taekyung."
  ],
  "continuity_sources": [
    194
  ],
  "open_questions": [
    "What is Dark Heaven ultimately seeking, and why was Shanxi Province targeted?",
    "Who are the three surviving Dark Heaven remnants, and what can be learned from them?",
    "Does Jeok Cheongang intend to take Jin Taekyung as his Disciple?",
    "When will Jang Taebo complete Taekyung’s commissioned weapon?",
    "Who has the Treasured Jade, or was it lost by Jopil?",
    "What consequences will follow Woo Hwangtae’s conflict with Chulwoo and the Jin Family?",
    "Will Song Il honor his pledge after returning to Zhongnan, and what consequences will follow his confrontation with the Jin Family?",
    "How will the public revelation of Taekyung’s entrusted Fire Gate Clan treasure affect the Jin Family?"
  ],
  "safe_through": 194,
  "temporary_decisions": [
    "Render 화왕 as “Fire King” and 화염신장 as “Flame Divine Palm.”",
    "Render 만년한철 as “Ten-Thousand-Year Cold Iron” and 이름 없는 검 as “Unnamed Sword.”",
    "Render 열화문의 신물 as “Fire Gate Clan’s sacred treasure”; it is the Unnamed Sword entrusted to Taekyung.",
    "Render 암천 as “Dark Heaven.”",
    "Render 전음 as “Sound Transmission,” 육합전성 as “Six-Harmonies Voice Transmission,” and 천하삼십육검 as “Heavenly River Thirty-Six Swords.”",
    "Render 대연무장 as “Grand Training Ground” and 종남산 as “Mount Zhongnan.”",
    "Render 주모 as “Lady of the House,” 권기 as “Fist Qi,” and 화산제일의 기재 as “Huashan’s greatest prodigy.”",
    "Render 사자후 as “lion’s roar,” 봉문 as “seal its gates,” 피독지환 as “Poison-Averting Ring,” 철혈도 as “Iron Blood Saber,” 양천상회 as “Yangcheon Merchant Association,” and 마이클 천강 as “Michael Cheongang.”"
  ],
  "version": 1
}

## Reading copies

## Chapter artifact 190

# Chapter 190

Crash!

Baek Museong's body shot upward as though it had been bounced into the air.

The chair he had been sitting in moments ago clattered loudly across the ground, but he paid it no attention. Neither did anyone else present.

“What is this?”

“What happened?”

“W-What just happened?”

They had thought it was over. Jin Taekyung had displayed far greater skill than expected, but in the end, he had lost his weapon to Chulwoo's Fist Qi.

A spearman without a spear against a Peak fist fighter. The result was obvious.

No—it had only looked obvious.

Until just now.

“How did this happen?”

“I…”

At Lee Seowol's question, Baek Museong's lips twitched. It was still difficult to believe, but he had lost sight of Jin Taekyung's movements for an instant.

All he had seen was something pale and fleeting.

*It feels like I've been bewitched by a ghost.*

Something impossible had happened.

After remaining silent for a moment, Baek Museong opened his mouth. His voice came out tinged with embarrassment.

“I don't know.”

Another wave of shock rippled through the crowd. Eunhyang, who had watched Baek Museong more closely than anyone else, widened her eyes.

“Big Brother—no, Senior Brother.”

“It’s true. Don't say anything.”

He had entered Huashan at the age of five, become the Disciple of the Heavenly Sword True Person, and earned the title of Huashan's greatest prodigy.

He was still young at thirty, yet his standing was already more than enough to place him shoulder to shoulder with the Elders.

*Huashan's greatest prodigy… Even a passing dog would laugh.*

With a bitter smile, Baek Museong turned his head. One person came into view, smiling brightly.

Ten years ago, after meeting Cheongpung only once, Baek Museong had realized the truth.

He was not Huashan's greatest prodigy.

“Martial Uncle Cheongpung.”

“Speak, Martial Nephew.”

Cheongpung answered without turning his head. His eyes remained fixed on the Grand Training Ground, gleaming with interest.

“Please tell me. How did he move?”

With everyone's eyes upon him, Cheongpung opened his mouth.

“He was fast.”

Everyone's excitement drained away. Fast? They hadn't been looking for such a simple, obvious answer.

Baek Museong spoke in an anxious voice.

“That isn't what I meant.”

“I know. But that's all there is to it.”

“…What do you mean?”

“My Benefactor has only learned one footwork technique and one spear technique. They're rough but practical martial arts. But none of them can be called a divine art.”

Cheongpung smiled brightly.

“He was simply faster. Much faster than Martial Nephew Chulwoo.”

Baek Museong was left speechless.

Jin Taekyung had learned no supreme martial art and possessed no peerless internal energy. To Baek Museong, he had been nothing more than a young prodigy from a frontier martial family with exceptional martial talent.

*How could such a thing be possible?*

The human body had limits. Murim martial artists were special because martial arts and internal energy allowed them to surpass those limits.

Yet Cheongpung was saying that Jin Taekyung had surpassed those limits without any particularly extraordinary martial arts.

Baek Museong blurted out a vehement denial.

“Impossible.”

Cheongpung shook his head.

“It's possible. For my Benefactor.”

“…”

“He read the pattern of Crouching Tiger Fist and counterattacked after only two days. If Martial Nephew Chulwoo had known that, he would have found another way.”

“Crouching Tiger Fist—in two days?”

Crouching Tiger Fist was unquestionably an advanced martial art. True to its name, it was powerful enough to subdue a tiger, and its forms were exceptionally intricate.

Even Huashan Disciples whose talent had already been recognized needed a full year just to learn its structure and forms.

And this boy had done it in only two days.

*My second junior brother was bound to lose.*

Baek Museong's eyelids trembled faintly.

He thought he now understood why the young Martial Uncle before him wanted to remain at Jin Taekyung's side.

*There was another monster.*

Jin Taekyung, the Sleeping Dragon of Shanxi.

He was exactly what the name implied. Though he was currently hidden beneath the shadow of the frontier, before long he would spread his wings and soar into the open sky.

*I was far too arrogant.*

Baek Museong clenched his fists. His nails dug into his skin, but the shame hurt more than the pain.

Had he become intoxicated by the name of Huashan?

Before the duel had even begun, he had already decided who the winner and loser would be.

*I always tell my junior disciples to remain humble, yet I failed to do so myself.*

It had been a day full of things to think about.

Baek Museong let out a quiet sigh and gave Jin Wikyung a clasped-fist salute.

“Great Hero Jin, I apologize for my earlier rudeness.”

“Ah, no.”

Jin Wikyung's expression was stiff as he accepted the apology.

As far as Baek Museong knew, Jin Wikyung treasured his two younger brothers like precious jewels. After belittling Jin Taekyung in front of him, he could hardly have expected Jin Wikyung not to be angry.

Baek Museong continued politely.

“Both my Junior Brother and I have learned a great deal. It seems the winner has now been decided, so perhaps we should end the duel.”

“That would be best.”

Jin Wikyung nodded gravely and rose from his seat.

A murmur so quiet that no one could make it out escaped between his lips.

“…Wow. This actually worked.”

Jin Wikyung had never expected him to really win.

* * *

The Grand Training Ground was as quiet as though everyone had been drenched in cold water. The commoners and martial artists alike wore expressions as if they had seen a ghost.

Though I couldn't see his face, Chulwoo was probably wearing a similar expression. The guy who had been frozen like a statue asked in a trembling voice,

“H-How?”

“By being good.”

“C-Could it have been Shifting Form and Position?”

“Your hyung's pretty fast, you know. Surprised?”

“You dodged Crouching Tiger Fist that easily…”

“You were much slower than your Martial Uncle. You'd better train hard when you get back.”

It was true. Compared to Cheongpung's Crouching Tiger Fist, Chulwoo's was far slower, and his movements were much larger.

His pattern was plain as day. There was no reason I couldn't evade it—especially with an Agility stat that had broken through 300.

“Destructive power only means something when you hit your opponent with fast and accurate movements. Got it?”

“…Who the hell do you think you are, lecturing me?”

“Who do I think I am? Lecturing you? You still haven't figured out the situation?”

I snorted quietly and poked the back of Chulwoo's neck with the steel flute.

Its sharp edge pierced his skin, and his massive body trembled. Oh, this was fun.

“Don't worry! Huashan's Serial Confession Man has been taken care of by the Taiyuan Jin Family's Steel Flute Murderer!”

“You little shit!”

“Now, don't move. I don't want to see blood.”

“You're dead the moment you come down.”

“Maybe. But the duel seems to be over, so you can try again next time.”

Just then, I spotted Jin Wikyung rising from his seat.

Chulwoo wasn't the type to surrender first, so it seemed Jin Wikyung intended to end the duel here.

A voice filled with internal energy soon rang across the Grand Training Ground.

“You both fought well!”

“Waaaaah!”

The crowd, having regained its senses, answered with a deafening cheer.

They had just watched a duel between Peak masters—something difficult to see even for money. Their reaction was understandable.

“All right, that's enough. Good work.”

The Quest had been much easier than expected.

The moment I pulled the steel flute away from Chulwoo's neck with a fresh smile—

Grab!

A hand as large as a pot lid clamped around my wrist.

“Huh?”

“It isn't over yet!”

For a moment, I had forgotten what kind of man Chulwoo was.

A man blinded by love. A man who had been dead for twenty-five years before his heart suddenly started beating. A man who could neither live nor die without Lee Seowol's permission…

In short, he was insane. A close synonym was fucking bastard.

*There was no way a man like that would give up easily.*

Whatever else you could say about him, he'd been born with one extraordinary gift: superhuman strength. Even Cheongpung couldn't match him in that regard.

Chulwoo spoke with absolute confidence.

“Once a guy gets caught by me, it's over.”

Sure, I'd let my guard down, but weren't this bastard's manners absolute shit?

Ah, a man blinded by love.

I let out a heavy sigh.

“Chulthetic, Pawoo.”[^1]

“Are those your last words?”

“No. Words of wisdom.”

[^1]: Taekyung mangles “Pathetic, Chulwoo” by swapping their opening sounds.

“You spout nonsense whenever you get the chance. Give up on Young Lady Lee, and I'll let you off here.”

“Did I ever tell you?”

“What?”

“Young Lady Lee proposed to me.”

“You goddamn so—!”

A scream erupted from the crowd.

Veins bulged across every muscle in Chulwoo's body as he hurled me toward the ground with tremendous force.

Or tried to.

“What are you doing?”

“Hnnnnngh!”

His red-hot face turned pale, then purple.

An immense force pulled on my wrist, but I didn't move an inch.

“Oh, you've got some strength.”

With the temporary boost from the **Gambler** Title and the points I'd just allocated, the strength coursing through my body now far surpassed human limits.

Not even Chulwoo, with his massive frame and innate superhuman strength, could overpower me.

“At this level, your Strength stat must be well over 200.”

“W-What is this?”

“You little shit.”

My grinning face was reflected in his horrified eyes.

“Your hyung's Strength alone is over 300. I was stronger than you even before allocating the points.”

Fist Qi? It didn't matter if it couldn't reach me. In strength, speed, and every other respect, I was ahead. Even if we had continued fighting as we were, I would have been the final winner.

Even so, there was a simple reason I had bothered allocating the points.

“People like you need to be stomped properly, or you won't stop acting up.”

“You damn—!”

Crack!

My fist shot out like lightning and struck him precisely in the temple. The muscular giant staggered, then collapsed limply.

Crash!

At the same time, the sound I had been waiting for rang out.

Ding.

> **System**
>
> - The **Quest** **There Is a Man Who Loved You So Much** has been successfully completed!
>
> - You received a large amount of **EXP** as a **Reward**!
>
> - You received a large amount of **Fame** as a **Reward**!
>
> - **Level Up!**
>
> - **Level Up!**

“Buuurp. That was delicious.”

After a brief silence, tremendous cheers engulfed the Grand Training Ground.

* * *

At the main gate of the Jin Family of Taiyuan, some six hundred meters from the Grand Training Ground, a low-ranking martial artist who had been listening with perked ears to the resounding cheers made a fuss.

“Did you hear that?”

Someone leaning crookedly against the gate answered.

“I did.”

“They say the Third Young Master defeated the Defeated Flower Fist!”

“Yeah.”

“…Why are you reacting like that? The Defeated Flower Fist! One of Huashan's Three Plum Blossom Elites!”

“I know, you idiot.”

“Third Young Master defeated the Defeated Flower Fist! Captain, aren't you surprised?”

“No. It doesn't surprise me anymore.”

Hyuk Mujin yawned widely and continued.

“I've followed that fellow around and seen all sorts of things. Beating the Defeated Flower Fist is the least he has to do before I can call him my lord.”

“Gasp! You've already thrown your lot in with him?”

“What do you mean, thrown my lot in?”

Hyuk Mujin snorted.

“One day, my lord said to me, ‘Listen, Hyuk martial artist. Become my right hand. Without you…’”

The low-ranking martial artist cut in with a suspicious expression.

“Wait a second. Are we talking about the Third Young Master? That doesn't sound like the way he talks at all.”

“Did you just interrupt me?”

“Captain, that's not what I meant.”

“Why, you little—are you close with that fellow? Do you know him better than I do?”

“No.”

“Listen here, kid. I've crossed through life-and-death situations with him! I've eaten with him! I've done everything with him!”

“…Yes. Please continue.”

“You should've said that from the start. Anyway, back then, my lord…”

That was when Hyuk Mujin, having calmed down, was about to continue.

“This is excessively noisy for a gathering.”

“What would the likes of them know? Looks like they let every Tom, Dick, and Harry in just because they were in a good mood.”

“Tsk, tsk.”

Voices came from beyond the faint darkness that had settled over the area.

Hyuk Mujin clicked his tongue and asked the low-ranking martial artist,

“Weren't all the distinguished guests on the list already here?”

“Well, everyone who said they would visit today has arrived, at least.”

“Then what is this? Someone who heard the rumors and came here?”

“Wouldn't that be likely?”

“First, double-check the list and stay here.”

“Yes, sir.”

Hyuk Mujin grumbled inwardly as he straightened from where he had been leaning at an angle.

Then he shouted toward the four silhouettes drawing closer.

“Halt! I am Hyuk Mujin, Captain of the Gatekeepers of the Jin Family of Taiyuan. State your identity and purpose!”

An elderly voice answered.

“Roaring Fury Swordsman.”

“Roaring Fury Swordsman, is it? What sect are you from?”

“Zhongnan Sect.”

“Zhongnan Sect, then. I need to check the other guests' faces as well, so come closer… oh.”

Hyuk Mujin stopped as he hurriedly scrawled the three characters meaning *Zhongnan Sect* on the wooden board.

When he slowly raised his head, he saw a gaunt old man and three middle-aged martial artists with arrogant expressions.

“Z-Zhongnan Sect?”

The old man at the front stared at Hyuk Mujin with blazing eyes.

“Jin Taekyung and Cheongpung. Take me to those two bastards at once.”
## Chapter artifact 191

# Chapter 191

As the unconscious Chulwoo was carried away, Jin Wikyung stepped forward.

“Is there anyone else who wishes to challenge him?”

I had literally wiped the floor with Chulwoo, who had been so overwhelmingly strong. There was no chance anyone else would step up.

When no one came forward, Jin Wikyung shouted with an expression of pure delight,

“Then the final winner of this duel tournament is the Sleeping Dragon of Shanxi, Jin Taekyung!”

Ding.

> **System**
>
> - You became the final winner of the **Jin Family of Taiyuan Duel Tournament** Sudden Event!
>
> - **Fame** increased!
>
> - You gained **EXP**!
>
> - **Level Up!**
>
> - You acquired 10 bonus points as an event **Reward**!

At the same time as the unexpected alert, the Grand Training Ground turned into a literal cauldron of madness.

“Waaaaah!”

“Ten thousand years for the Jin Family of Taiyuan! Long live the Sleeping Dragon of Shanxi!”

“The Sleeping Dragon of Shanxi defeated the Defeated Flower Fist!”

“Kiyah-hoo!”

Who was that? Did he know how to have fun?

In any case, the atmosphere in the Grand Training Ground grew hotter than anything a rock festival could offer.

A child threw the candied fruit he had been holding into the air, while a white-haired old man let out a wild cry and broke his cane over his knee.

“Waaaah!”

“Hiyah!”

The martial artists’ reactions were no less intense. If anything, they were even more enthusiastic.

Shanxi Murim had been treated as a backwater for a long time. I had only defeated one Serial Confession Man, but to them, it was practically the same as winning a battle of pride against Shaanxi Murim.

“Lady of the House! Bring me a bottle of huangjiu!”

“The dumplings that got stuck twenty years ago are sliding right down! Order whatever you want—I’m paying for everything today!”

Don’t call the Lady of the House. And don’t order everything.

It was all coming out of the Jin Family of Taiyuan’s pockets anyway, but the people high on Shanxi pride had completely lost their minds.

*They’re going wild.*

Since a large portion of them were martial artists, carrying weapons was standard. I was worried that someone might get drunk on the excitement and cause trouble.

Sure enough, a lunatic suddenly shouted,

“Everyone, draw your swords!”

Clang-clang-clang!

Hundreds of weapons were drawn in a flash of reflected light.

“Wave them from the front, one row at a time!”

“Waaaaah!”

Clang-clang-clang! Clang-clang-clang!

Wait, were they doing the wave here?

As I watched this cutting-edge new cheering culture unfold, I muttered in disbelief,

“This is completely…”

“A total shitshow.”

I had started the sentence, but I hadn’t said the second half.

An elderly voice pierced my ears with perfect clarity. I looked around, but all I could see were excited people.

*Who was that?*

Even amid the cacophony, the voice had sounded as though the speaker were standing right beside me. Whoever it was, he was a master—one with profound internal energy at that.

Just as several of us turned our heads in search of the voice’s owner—

“Ha!”

Gooooong.

Was this what the lion’s roar I had read about in martial arts novels sounded like?

The ground trembled, and the air shuddered. The more timid commoners fainted or collapsed with screams.

“Eeeeeek!”

“Gah!”

The Grand Training Ground, which had been filled with a festival atmosphere, instantly became an utter madhouse.

The commoners were trembling, and the martial artists had frozen in place. Through the scattered crowd, which had fled as though a bomb had gone off, an old man strolled leisurely into view.

“Much better.”

He was tall and emaciated. His sharp gaze swept across everyone before meeting mine.

I was standing at the center of the duel platform, and as a young man still standing there unharmed and staring back, I was bound to catch his attention.

After looking me up and down, the old man opened his mouth.

“Are you the one?”

“Excuse me?”

“Cheongpung or Jin Taekyung. Which one are you?”

What the hell was going on?

All sorts of thoughts flashed through my mind. After making a decision in that brief moment, I answered,

“Neither.”

“You’re not?”

“No. You must have mistaken me for someone else.”

Whatever was going on, I might as well deny everything and see what happened.

I could tell at a glance what kind of situation this was. I didn’t know who he was or where he had come from, but he certainly didn’t seem to have any warm feelings toward me.

“Really?”

“I’ve never heard that name in my life.”

The old man gestured behind him.

“Come here.”

“Yes, Elder.”

Four people hidden among the crowd emerged. As it happened, I was acquainted with every one of them.

One face in particular was impossible to mistake.

*Hyuk Mujin?*

Why was the guy who was supposed to be standing guard over there?

Hyuk Mujin, pale as a sheet, walked forward as though the three middle-aged men beside him were dragging him along. Their faces were familiar too.

But what were their epithets again?

*Oh, right. The Three Hands of Zhongnan.*

Just as I finally remembered the extras’ epithets, the unidentified old man spoke to the four of them.

“Find them.”

Hyuk Mujin and the middle-aged man with a splint on his arm, Gong Ilhyuk, pointed at me at the same time.

“Captain! Please save me!”

“It’s him! That guy is Jin Taekyung!”

“…”

“…”

Well, so much for that.

After a brief silence, the old man asked me,

“Are you really Jin Taekyung?”

I bowed as politely as I could.

“Nice to meet you. My name is Jin Taekyung.”

“…What kind of lunatic is this?”

Just as the old man stared at me in disbelief, three people landed lightly with a rush of wind.

Jin Wikyung, Baek Museong, and Cheongpung.

“I am Jin Wikyung, Lesser Family Head of the Jin Family of Taiyuan. May I ask this Senior’s name?”

“Ahem. You’re the Lesser Family Head of the Jin Family of Taiyuan?”

The question had been directed at the old man, but Gong Ilhyuk was the one who stepped forward.

Jin Wikyung’s brows drew together at the interruption.

“That is correct. And who might you be?”

“I am Gong Ilhyuk, one of the Three Hands of Zhongnan. I am a second-generation Disciple of the Great Zhongnan Sect, and Great Hero Gong Iljung, the Wind-and-Cloud Sword Lord and Sect Leader, is my father’s cousin.”

That guy was still constantly playing up his father’s cousin.

I wanted to smack him in the mouth with the drumstick of a boiled chicken.

Jin Wikyung learned Gong Ilhyuk’s identity and muttered as though groaning,

“The Zhongnan Sect?”

Gong Ilhyuk was a well-connected hack who threw his weight around, but the name of the Zhongnan Sect was another matter.

The Nine Sects and One Gang and the Five Great Families were the great trees that moved the Murim of the present age.

Emboldened by the momentum, Gong Ilhyuk continued smugly,

“And this gentleman here is Elder Song Il of our sect.”

*That old man is an Elder of the Zhongnan Sect?*

I had expected him to be a master, but it seemed his status was even more impressive than I had imagined. Jin Wikyung and Baek Museong’s expressions hardened.

“The Roaring Fury Swordsman…”

“This junior of Murim, Baek Museong, pays his respects to Senior Song.”

The old man—the Roaring Fury Swordsman—silently looked down at the two of them as they hurriedly paid their respects.

His voice carried the composure and arrogance of a powerful man.

“Baek Museong? Are you Huashan’s Lone Crane?”

“Yes. It’s an epithet far too generous for me.”

“So it seems. You’re inferior to your Master in his youth.”

What an insufferable old bastard.

Still, I had to acknowledge that his clout was extraordinary.

It wasn’t enough for the Roaring Fury Swordsman to casually trample Baek Museong, who was practically an object of admiration, in front of everyone. He had also spoken of the Sect Leader of Huashan, the Heavenly Sword True Person, as though he were an old neighborhood friend.

His seniority in Murim seemed to be just as impressive as his martial arts.

“I will continue striving.”

“Hm. You certainly know how to dress up your words. But if the Heavenly Sword True Person sent you…”

As he watched Baek Museong bow his head without another word, the Roaring Fury Swordsman’s eyes flashed.

His gaze had shifted to Cheongpung, who stood there blankly.

“So it’s you. The Sword Saint’s heir.”

Cheongpung asked with a puzzled expression,

“You know my grandfather?”

“Of course I do. How could I not know him?”

Judging by his expression, they probably hadn’t shared a particularly pleasant relationship.

As the situation grew more serious, Jin Wikyung asked with a stiff face,

“May I ask why you have come to visit?”

“I came to collect a debt.”

“A debt?”

“Yes. The debt for daring to mock the Great Zhongnan Sect and injure one of our Disciples.”

A blade-sharp gaze shot toward Cheongpung and me.

Gong Ilhyuk stepped forward, shaking his splinted arm.

“Do you see this? I suffered this injury at Prince Shangshan’s residence when I visited after receiving an invitation. I showed it to a physician, and he said I would need at least six months of recuperation.”

Cheongpung opened his mouth with an apologetic expression.

“I hit you gently… Did it hurt a lot?”

Cruel bastard. He was killing Gong Ilhyuk twice over.

Gong Ilhyuk’s face flushed red from the public humiliation.

“You bastard! After ambushing me, you still have the nerve to say that!”

I muttered in disbelief,

“Don’t make me laugh. You grabbed him by the collar first and got your ass handed to you.”

“Can’t you shut up? When I think about how you two mocked our sect and what you did to me, it wouldn’t satisfy me even if I chewed you up and swallowed you!”

That was how childish fights turned into fights between adults.

Jin Wikyung and Baek Museong’s faces twisted sharply.

“Chew him up and swallow him? Are you talking about our youngest brother?”

“How dare you call him a bastard! Great Hero Gong, watch your words! Though our sects may differ, seniority still matters in Murim. How could you…”

“Heh heh heh.”

At the Roaring Fury Swordsman’s irritating laugh, Jin Wikyung and Baek Museong fell silent.

“Seniority. You chose your words well.”

“…”

“…”

“This old man is the Senior Brother of our sect’s Sect Leader, the Wind-and-Cloud Sword Lord. I am of the same seniority as the Heavenly Sword True Person of Huashan, so there should be no problem.”

Bringing up seniority had been a mistake.

The Roaring Fury Swordsman’s martial arts were already formidable, and he was using his years of seniority to overwhelm them. Neither Jin Wikyung nor Baek Museong could stand against him—not even Cheongpung, the Sword Saint’s Disciple.

“Is this old man wrong?”

When no one answered, the Roaring Fury Swordsman spoke to Cheongpung.

“You injured a Disciple of the Zhongnan Sect. Are you prepared to face the consequences?”

This was why words were frightening.

There was no explanation of how it had happened. Only the result remained.

Baek Museong hurriedly cut in.

“Senior, we must clearly determine right and wrong in this matter.”

Cheongpung also muttered with his body drawn inward,

“I only gave him a light tap.”

“Are you saying you didn’t do it?”

“That’s not what I mean. I did hit him, but I didn’t know he would get hurt that badly.”

Gong Ilhyuk seized the opening and lunged in.

“It was an obvious attempt to kill!”

“Did you hear that?”

“I really didn’t mean to.”

While Cheongpung fumbled for words, the Roaring Fury Swordsman’s sharp voice continued.

“I will formally lodge a complaint with Huashan over this matter, so don’t you dare think you can wriggle out of it.”

“Elder, the government and Murim do not interfere with each other. Besides, the government officials who were present were friendly toward them, so I fear they may give false testimony.”

“You’re right. I will take measures.”

It was practically a fixed game from the start.

Baek Museong bit down hard on his lip at the unfair treatment, and the next target of their arrows was obvious.

“The Jin Family of Taiyuan will seal its gates until our sect sends someone.”

“…”

“What did you just say?”

Jin Wikyung said what I wanted to say for me. No—everyone nearby who had heard the Roaring Fury Swordsman must have been thinking the same thing.

*Seal its gates?*

What kind of bullshit was that?

It was true that I had humiliated Gong Ilhyuk somewhat.

But that had been limited to Gong Ilhyuk himself. I could swear that I had never mocked or insulted the Zhongnan Sect.

And yet they wanted to seal the Jin Family’s gates over something like this?

Even with the condition that it would last only until the Zhongnan Sect sent someone, the order itself was already humiliating.

“That is unjust!”

At Jin Wikyung’s shout, the Roaring Fury Swordsman raised his eyes.

“What did you say?”

“How can you order us to seal our gates before even investigating what happened and determining right and wrong? Is this the way of the Nine Sects and One Gang—or rather, the way of the Zhongnan Sect?”

“How dare you!”

“Our family will not accept this!”

“If you refuse to accept it?”

Ssssss.

A powerful aura rose from the Roaring Fury Swordsman’s entire body like a wildfire.

It felt as though a sword were aimed directly between my brows. My skin prickled.

“If you refuse to accept it, what are you going to do?”

“…”

“This is Murim. Have you forgotten?”

A sudden surge of irritation welled up inside me.

I knew how the world worked. I had already experienced it more times than I cared to remember.

People ignored you because you had no money, looked down on you because you lacked powerful backing, and scorned you because your talent was insignificant.

*It’s exactly the same here.*

Murim and the modern world were different, yet so much alike.

Those with power turned lies into truth and truth into lies.

Pressuring and crushing the weak—it all came naturally to them. It was simply the way things were, just as it was to the Roaring Fury Swordsman standing before me.

Drip. Drip.

Blood began to flow from my tightly clenched fist.

I stared down at the drops landing one by one on the ground and exhaled a hot breath.

“Ah, fuck. This is fucking bullshit.”

No one dared to speak.

Everyone heard the profanity that had burst from my mouth.

It felt as though something invisible had shattered with a sharp crack.

The Roaring Fury Swordsman asked with an expression of disbelief,

“…What did you just say?”

Swearing had been a mistake. Since I was the reason this had happened, I should have swallowed it no matter what.

That was the best way to resolve the situation smoothly.

But…

“It’s fucking bullshit. I said it’s fucking bullshit. You fucking assholes. There’s a limit to how much you can throw your weight around.”

I couldn’t take it anymore.

They could call me thoughtless or a young fool who knew nothing about the world. I didn’t care.

I had no desire to replay all the things I had been sick of experiencing in reality here in Murim.

I apologized to Jin Wikyung.

“I’m sorry. I know this is something I’m supposed to put up with even if it’s fucking bullshit, but they were being so fucking shitty about it that it became twice as fucking shitty, and I couldn’t let it slide.”

Jin Wikyung, who had been half out of his senses, displayed an astonishing variety of expressions.

His face twisted, then relaxed. After showing several different expressions in a short span of time, he finally let out a quiet laugh.

“To be honest, I thought it was fucking bullshit too.”

Those words pulled the trigger.

Flames hotter than lava poured from the Roaring Fury Swordsman’s eyes.

“You bastards… must be desperate to die.”

Shing.

Along with the words he spat through clenched teeth, he drew his sword. Layer upon layer of Sword Energy coated the snow-white blade.

It burned more fiercely than any Sword Energy I had ever seen.

And the moment it aimed at me—

“If you kill that guy, you die too.”

At the clear, ringing voice that came from somewhere, the Roaring Fury Swordsman’s body abruptly froze.
## Chapter artifact 192

# Chapter 192

“Ah, fuck. This is fucking bullshit, seriously.”

…What?

Song Il thought he was dreaming.

*Who was he?* He was the Roaring Fury Swordsman, Song Il. Even now that his junior brother, the Wind-and-Cloud Sword Lord, had become Sect Leader, he still treated Song Il with the utmost courtesy and respect.

And yet—what the fuck? This is fucking bullshit?

*Did I hear that wrong?*

The Sleeping Dragon of Shanxi, Jin Taekyung. The youngest son of the tiny Jin Family of Taiyuan.

A brat who had only just turned twenty with the change of the year.

He couldn’t believe that such a brat had said those words to him—a Great Zhongnan Sect Elder and one of the heroes of the Great Faction War.

No. He couldn’t accept it.

“What did you just say?”

Any hope that he had misheard was crushed the next moment by Jin Taekyung’s reply.

“It’s fucking bullshit. I said it’s fucking bullshit! You fucking assholes! There’s a limit to how much you can throw your weight around.”

“…”

After cursing up a storm, Jin Taekyung turned to Jin Wikyung.

“I’m sorry. I know this is something I’m supposed to put up with even if it’s fucking bullshit, but they were being so fucking shitty about it that it became twice as fucking shitty, and I couldn’t let it slide.”

“To be honest, I thought it was fucking bullshit too.”

Those words from Jin Wikyung were the finishing touch.

The disbelief in Song Il’s eyes slowly gave way to light. A blazing light.

It was an immense fury he hadn’t felt in a very long time.

“You bastards…”

Hot breath escaped between Song Il’s teeth as he lost control of himself.

“You must be desperate to die.”

Shing.

His treasured sword, which had cut down countless enemies, emerged from its scabbard. It didn’t matter whether the Jin Family of Taiyuan belonged to the orthodox faction, the unorthodox faction, or even practiced demonic, heterodox arts.

If Song Il had thought about the consequences before causing trouble, he never would have earned the title Roaring Fury Swordsman.

*I’ll kill every last one of you.*

Song Il truly intended to kill them. As though to prove it, powerful Sword Energy surged like waves.

He had trained in the Zhongnan Sect’s ultimate technique, the Heavenly River Thirty-Six Swords, all his life.

Although he had not achieved complete mastery, it was more than enough to turn these insolent fools into minced meat with a single sword strike.

*I’ll kill you first.*

He had already decided who would die first.

The Sleeping Dragon of Shanxi, Jin Taekyung. He would chew up that young brat’s tongue and swallow it.

And just as Song Il was about to shoot his Sword Energy with bloodshot eyes—

“If you kill that guy, you die too.”

At the voice that came from somewhere, Song Il’s body abruptly froze.

It wasn’t because of the meaning behind those words. He couldn’t determine where they had come from at all.

*I can’t tell? Me?*

That was impossible.

But the voice that followed made it clear that this situation was real.

“A man your age, picking on a child like this. Tsk, tsk.”

Front, back, above, below, left, right.

Song Il couldn’t distinguish where the voice was coming from. Its owner was nowhere and everywhere at once.

*Th-this is…*

At last, Song Il realized the identity of the voice, and his body trembled.

*Six-Harmonies Voice Transmission!*

If Sound Transmission, the art of transmitting sound through internal energy, was exclusive to Peak masters, Six-Harmonies Voice Transmission was a martial art permitted only to those who had reached the realm beyond it.

The Supreme Peak. A great realm that only a tiny fraction of the chosen few could enter.

*How could someone like that…*

Why? Why was such a person interfering with him?

Song Il shouted as though having a fit.

“Who are you! I am Elder Song Il of the Great Zhongnan Sect, the Roaring Fury Swordsman! Show yourself at once!”

“‘This old man’? ‘Elder’? Hahahahahaha!”

Thunderous laughter rang out from every direction. The internal energy behind it was so vast that no one dared guess at its limits.

The commoners who had never learned martial arts fell flat on their faces, crying out to the Jade Emperor, while the martial artists trembled in awe.

“Can you not hear me!”

“Ha, hahaha! Ah, I’m laughing so hard my stomach’s going to split.”

“You insolent—!”

Song Il had lost his composure to anger and fear. And in his eyes, he saw Jin Taekyung.

Unlike the people staring around in shock, Jin Taekyung alone was gazing into the empty air. There was even an enigmatic smile on his lips.

Almost as though he were mocking Song Il.

*That bastard!*

Ssssss!

The Sword Energy that had faltered for a moment surged again. Pointing his sword at Jin Taekyung, Song Il looked around and shouted,

“Show yourself at once! Or I’ll kill this bastard!”

The laughter that had shaken heaven and earth abruptly stopped.

“What? Kill that guy?”

“I’ll count to three.”

A triumphant smile spread across Song Il’s lips.

He didn’t know where the voice’s owner was, but the troublemaker’s weakness was Jin Taekyung. The fluster in the other man’s voice was proof.

“One!”

“Heh, look at you. You’ve grown even more venomous since I last saw you.”

*Since they last met?*

Song Il’s mind raced. Judging by those words, they had clearly met before, but…

*Wait. Could that voice be…*

Song Il flinched as he thought of someone, but quickly gritted his teeth.

That was impossible. There was no way that old monster was still alive.

As though trying to shake off his fear, he shouted even louder.

“Two!”

“Phew. Fine, I understand. I’ll come out now, so wait right there! But if you touch even a single hair on him, I’ll make you pay for it!”

Song Il’s strength left him all at once.

His gamble had worked. The unidentified Supreme Peak master wanted Jin Taekyung alive. And he was farther away than Song Il had expected.

“Fifty jang. Don’t come within fifty jang. If you come any closer, this bastard is as good as dead—”

It was at that exact moment.

“Three.”

Song Il doubted his own eyes and ears.

Barely three jang away, Jin Taekyung calmly opened his mouth again.

“I said three. You fucking old bastard. Are you deaf?”

“You bastard. Are you desperate to die?”

“Try killing me. If you can.”

“…What?”

“You know what? If you can’t kill me with one sword strike, you’re next.”

“……!”

“Let’s see who dies.”

Jin Taekyung smiled brightly and spread both arms.

“He’s coming.”

He was coming. Those two words sent a chill down Song Il’s spine.

Song Il unconsciously took a step back.

Then—

Whoosh.

A faint sound of wind pierced his ears. A presence was rapidly drawing close from behind him at an unbelievable speed.

*This is…*

Every hair on Song Il’s body stood on end. The instincts he had honed by crossing the threshold of death countless times whispered to him.

*It’s already too late. Fall back. Now.*

But—

*I am the Roaring Fury Swordsman, Song Il!*

Sssshhhhh!

The Heavenly River Thirty-Six Swords, which he had brought to nine-tenths mastery, erupted. Sword Energy split into twenty-four streams and shot forward.

In the slowed world, Jin Taekyung’s figure was reflected in Song Il’s wide-open eyes.

Swish, swish, swish, swish, swish!

He narrowly evaded the twenty-four blades of Sword Energy as they rushed in, covering all twenty-four directions.

The price he paid for avoiding the Roaring Fury Swordsman’s sword strike was limited to torn clothing and blood dripping here and there.

“This is impossible—!”

Song Il, still in shock, was given no chance to attack again.

Something firm and hot had seized his wrist as he tried to unleash his second form.

His hand clamped down.

“You fucking bastard… Didn’t I tell you not to touch a single hair on him?”

A low voice. Two eyes blazing so fiercely that their red seemed to burn blue.

Only then did Song Il realize.

He could no longer hear the sound of the wind.

And he had touched someone he never should have touched.

“You—you’re… How could you…”

“The Zhongnan brat has grown a lot. You can’t even recognize an adult anymore.”

The old monster who had inflicted an unforgettable humiliation on him long ago had come back to life in his memories—and was now standing before him.

Song Il let out a shrill scream.

“Fire King—!”

A terrifying smile appeared on Jeok Cheongang’s wrinkled lips.

“Yes. It’s me.”

On New Year’s Day, the Fire King descended upon the Jin Family of Taiyuan.



* * *



The Fire King, Jeok Cheongang.

The weight carried by that name pressed down upon the entire training ground.

One God, Three Saints, Ten Kings.

They were gods, stars, and kings who stood above the countless martial artists of Murim. Absolute beings who stood closest to the title of the greatest under heaven.

Jeok Cheongang was dressed in shabby clothes and had a slight frame, but the presence he gave off was that of a giant itself.

And the giant’s eyes turned toward me.

“You crazy bastard. Are you desperate to die?”

I never thought that voice could sound so welcome. I sank down on the spot.

“Whew. I almost died for real.”

“You would have if this old man hadn’t stepped in.”

“Yes, thank you. I won’t forget this kindness.”

At my soulless reply, Jeok Cheongang glared at me.

“You lost your fear in half a day. Do you want to die?”

*Only half a day?*

Thinking about it, I had parted with Jeok Cheongang that very morning.

The first day of the new year had been so eventful that it felt as though a month had passed.

I answered in an exhausted voice.

“If you’re going to kill me, please put it off as long as possible.”

“That is the plan.”

Jeok Cheongang turned his head and added,

“First, I’ll deal with this insolent bastard.”

*Insolent bastard?* How many people in the world could call the Senior Brother of the Zhongnan Sect’s Sect Leader—and an Elder at that—something like that?

“Ah, ah…”

The Roaring Fury Swordsman Song Il was trembling from head to toe.

Judging by the way Jeok Cheongang kept calling him a brat, they must have known each other in the past. Apparently, it hadn’t been a particularly warm relationship.

“It’s been a long time. So, did those broken bones heal properly?”

“H-how could you…”

“‘You’? Was that directed at me?”

The Fire King blinked as though he were looking at some fascinating creature, then gave a hollow laugh.

“You’ve grown a lot.”

Smack.

It was a sight that would have been difficult to see even if you paid for it.

Jeok Cheongang slapped the Roaring Fury Swordsman across the face with his wrinkled hand. Though his hand moved infinitely slowly, the Roaring Fury Swordsman couldn’t dare evade it even while watching it approach.

“I remember when I first saw you. You were barely twenty, a young pup.”

Smack.

“You were arrogant and rude, causing all kinds of trouble while relying on your sect’s halo. And now you’re an Elder of the Zhongnan Sect?”

Smack.

“Once, I saved you when you were about to die, and the thing you said afterward was unbelievable. Was it, ‘Why are you stealing someone else’s battle credit?’”

Smack.

“If it hadn’t been for your Master’s request, I would have broken your neck instead of your leg.”

Smack, smack, smack!

The ordinary slaps carried not a trace of internal energy, yet the half-gray-haired Roaring Fury Swordsman shrank like a beaten child.

The eyes that had shone with a powerful man’s confidence and arrogance were now buried beneath humiliation, fury, and fear.

Jeok Cheongang spat out the words with the expression of a man looking at a bug.

“You fucking moron. Did all those years go straight up your ass?”

*What should I do?*

I was starting to like the old man more and more.

Jin Wikyung and Hyuk Mujin were already gazing at Jeok Cheongang with eyes full of love.

“You call yourself an Elder of the Nine Sects and One Gang, yet you threaten commoners and use your power to arbitrarily order a sect to seal its gates? If your Master saw this, he would be wailing in the afterlife.”

“…”

“Who is the Sect Leader now?”

The Roaring Fury Swordsman answered in a stammering voice.

“M-my junior brother. The Wind-and-Cloud Sword Lord…”

“Wind-and-Cloud Sword Lord? I’ve never heard of such a title in my life. Is that why a piece of trash like you struts around calling yourself an Elder of the Zhongnan Sect?”

What audacity—to treat the Sect Leader of the Zhongnan Sect like some nobody.

It wasn’t enough that his sect had been insulted. The Roaring Fury Swordsman had suddenly been reduced to a piece of trash, and his face twisted violently.

When he silently lowered his head to hide his humiliation and anger, Jeok Cheongang widened his tiger-like eyes.

“Is your mouth just for decoration? Why aren’t you saying anything?”

“…Great Hero Jeok. I—I merely…”

“Shut your mouth!”

I made up my mind.

I was going to create a fan club.

At this very moment, the Fire King, Jeok Cheongang, was no different from an idol—the undisputed star of the Jin Family of Taiyuan.

*Is this what it feels like to bathe in a hot spring of soda?*

Even my white blood cells were fizzing.

It felt like chugging an ice-cold can of beer after a raid on a sweltering summer day.

A three-layer wave of refreshing exhilaration swept over my entire body.

*Fire. King. Is. The. Best.*

Of course, that was from the perspective of someone watching.

The Roaring Fury Swordsman had been publicly humiliated in front of countless commoners and martial artists alike. Perhaps that was why the humiliation and anger he felt in that instant overcame his fear of the Fire King.

“T-this is a matter between our sect and the Jin Family of Taiyuan.”

“What?”

“I’m saying that this is not something for Great Hero Jeok to involve himself in.”

“This old man has no business involving himself?”

Jeok Cheongang stared blankly at the Roaring Fury Swordsman, who had finished speaking in a trembling voice.

His tightly clenched fist twitched, as if he were considering where to hit him so people would say he had chosen the perfect spot.

*Hit him! Please, just hit him once!*

As though he had heard my encouragement, Jeok Cheongang raised his hand high.

Then, the next moment, his wrinkled finger was pointing at me.

“Do you see that bastard?”

“…?”

What the hell? Why was I suddenly involved?

Just as everyone’s faces, mine included, filled with confusion, the Fire King continued.

“I entrusted the Fire Gate Clan’s sacred treasure to that boy.”

“……!”

“……!”

Silence descended over the Grand Training Ground.

Wordless shock spread endlessly through the crowd.
## Chapter artifact 193

# Chapter 193

## The Fire Gate Clan’s Sacred Treasure

The moment that unfamiliar phrase sprang from the Fire King’s mouth, the Roaring Fury Swordsman’s eyes bulged as though they were about to tear apart.

“W-what do you mean?”

“You haven’t even turned seventy, and your ears are already clogged? I’ll say it one more time, so listen carefully.”

Jeok Cheongang jerked his chin toward me with an irritated expression.

“This old man entrusted our sect’s sacred treasure to that brat. Got it?”

“…”

“…”

*What do you mean, got it?*

I looked around with a bewildered expression. Everyone, including Jin Wikyung and Baek Museong, was staring back and forth between Jeok Cheongang and me in shock.

Amid this chaotic mess, one person alone remained unaffected.

“Benefactor, what’s the Fire Gate Clan’s sacred treasure? Show me, too.”

I couldn’t answer Cheongpung’s question.

*I don’t know either, you little shit.*

The Fire Gate Clan’s sacred treasure? What was he talking about?

I swore I had never heard or seen such an item.

The only things I had received from Jeok Cheongang were the martial arts manual for the Flame Divine Palm and a sword…

*Wait.*

“Could it be?”

At my doubtful gaze, Jeok Cheongang clicked his tongue.

“You’ve been carrying it on your back and still didn’t know? What a moron.”

It felt as though I had just been hit in the back of the head with a hammer.

I hurriedly untied the knot holding it firmly in place. When I unwound the layers of cloth, an old, crude scabbard appeared.

*The Unnamed Sword.*

The very item Jopil had stolen from his Master—and which I had taken from him.

I gripped the hilt and drew.

Shing!

With a sound that made every hair on my body stand on end, the pure-white blade emerged.

Beneath the darkness, it shone like a holy sword from legend, drawing gasps from the people around us.

*So this really is… the Fire Gate Clan’s sacred treasure?*

I had never once suspected it.

Why Jopil had stolen it from Jeok Cheongang. Why it had been given the strange description *Unnamed Sword*, unlike the Flame Divine Palm or the Blazing Flame Divine Pill.

I was staring blankly at the blade when—

“T-this is impossible!”

It was the Roaring Fury Swordsman. Unlike him, overwhelmed by extreme confusion and excitement, Jeok Cheongang’s expression was perfectly calm.

“What is?”

“T-that…”

“This old man entrusted the Fire Gate Clan’s sacred treasure to that brat. You may have nothing but shit in your head, but surely you understand what that means.”

I suddenly came to my senses.

I had been so distracted by the sword that I had briefly forgotten what it meant for a sect’s sacred treasure to have been entrusted to someone—especially the sacred treasure of the Fire Gate Clan, which had been passed down through a single lineage for hundreds of years.

At the same time, Cheongpung’s words from barely half a day ago flashed through my mind.

*“Are you going to take Benefactor as your Disciple?”*

At the time, I had thought it was ridiculous nonsense and laughed it off.

But now…

*Fuck. I don’t know either.*

As I swallowed dryly, the Roaring Fury Swordsman pointed a finger at me.

But before he could even speak, Jeok Cheongang’s terrifying gaze bound him in place.

“This old man said he entrusted our sect’s sacred treasure to him.”

That was all.

But his opponent was none other than the Fire King.

The Roaring Fury Swordsman no longer had the courage to argue. He chewed on his lips, then suddenly glared at me.

“You bastard. You’re lucky.”

*Why is this old man starting shit with me again?*

Jeok Cheongang said nothing. Was he telling me to handle something this minor on my own?

I shrugged at the Roaring Fury Swordsman.

“You’ve got the wrong man. I’m actually really unlucky.”

*If I were lucky, do you think I would’ve met a piece of shit like you?*

I didn’t know whether Jeok Cheongang’s arrival in a situation that had been on the verge of exploding counted as great misfortune or great fortune.

“Anyway, it was nice meeting you. Have a safe trip home.”

“You cunning bastard. Why don’t you try what you did earlier?”

“What, earlier? Oh, you mean when I said you were fucking shitty?”

Before the Roaring Fury Swordsman could say anything, I bowed my head.

“I apologize for that. I have a hard time tolerating injustice. Please forgive a slip of the tongue from a junior far beneath you. Great. Hero.”

“……!”

The Roaring Fury Swordsman’s body trembled. Blood dripped from his tightly clenched fists.

Looking at him, I saw myself from a few minutes earlier. The difference between us was that I had not bowed to the Roaring Fury Swordsman, while he had submitted to the Fire King.

Those who rely on power kneel before greater power. Realizing that fundamental truth of the world again was satisfying, but not entirely.

No, it was even bitter.

*This leaves a bad taste in my mouth.*

If Jeok Cheongang had not been here, the humiliation and fury that man felt would have belonged to me and the Jin Family of Taiyuan.

If only a few people here stepped forward, defeating the Roaring Fury Swordsman himself would not be difficult. But behind him stood the Zhongnan Sect.

I hated admitting it, but the gap between them and us was vast. For now, it was a distance that could never be closed.

*For now.*

I had been a perpetual F-rank Hunter, yet I had still made it this far. No one knew what the future held.

Maybe one day the Jin Family of Taiyuan would stand shoulder to shoulder with the Nine Sects and One Gang and the Five Great Families.

*Am I getting ahead of myself?*

It was like a rural township chief running for president.

I snorted quietly at the thought, and the Roaring Fury Swordsman ground his teeth.

“How dare you laugh at me?”

“I was born with a smiley expression.”

“Shut that mouth of yours!”

At the moment his furious shout erupted, Jeok Cheongang’s right foot shot out like lightning and kicked the Roaring Fury Swordsman in the shin.

A Supreme Peak master’s joint kick.

Thud!

“Guh!”

“You shut up. Where does a young bastard like you raise his voice in front of an elder?”

“What do you think you’re doing?”

“Look at this bastard. I tried to end things nicely, and now you’re begging for a beating?”

Wham!

“Urgh!”

*Wow. That one landed.*

With a heavier impact than before, the Roaring Fury Swordsman clutched his shin and collapsed.

*Even an Elder of the Great Zhongnan Sect is helpless against him.*

He was over sixty and held a high position in society, but his opponent was simply on another level.

Age, martial arts, status. There was no way to catch up to the Fire King, Jeok Cheongang, in any of them.

“Carrying on like that is a disease. You’ve done enough, so get the hell out of here.”

“…Very well.”

The Roaring Fury Swordsman glared at me with a resentful gaze as he rose, his body covered in dirt. Then a cold voice followed.

“Also, I will let today’s events pass, so never speak of this matter again. Do you understand?”

*I really should start a fan club.*

I had acted on impulse, but I had been worried on some level. If the Roaring Fury Swordsman later used the Zhongnan Sect to retaliate, the Jin Family of Taiyuan would have no way to stop him.

But with Jeok Cheongang mediating, things were different.

*Whether this is mediation or a threat, I’m not sure.*

The resentment over today’s events would remain, but at least he would not be able to bring official pressure against us.

Even if he did, having the Fire King as a sturdy shield made the burden far lighter.

“Why aren’t you answering?”

The Roaring Fury Swordsman’s face twisted hideously, his cheap ploy having been seen through. Jeok Cheongang, of course, did not care.

“Say it yourself. Right now.”

“…Understood. I swear it on my name.”

“What name do you have worth staking? Swear it in the name of the Zhongnan Sect.”

“Grrk… Understood.”

Only then did a satisfied smile appear at the corners of Jeok Cheongang’s mouth. He laughed heartily and patted the Roaring Fury Swordsman on the shoulder.

“Where did a young bastard like you learn to grind your teeth like that? Should I just yank every last one of them out?”

“…”

“Hahahaha! This old man is old, so I can’t do that in front of all these people. Hahahaha!”

It was the first time I had learned that the laughter of a white-haired old man could be so frightening.

Everyone listening flinched at once—not only the Roaring Fury Swordsman.

Jeok Cheongang, who had been laughing like an evil spirit, turned his head toward me.

“You’re not blameless, either. No matter the circumstances, how could you hurl such abuse at an elder far above you in age? Are you out of your mind?”

I immediately bowed my head. Regardless of what had happened, facts were facts, and I also thought it was time to bring things to an end with the Roaring Fury Swordsman, an Elder of the Zhongnan Sect.

“I’m sorry.”

“Even if he ate his age through his asshole, he’s over sixty. It wouldn’t be strange for him to have a grandchild your age.”

“…Ah. Yes.”

“No matter how much of a bastard he is, he’s still an elder and a great Senior of Murim. It may be dirty and unfair, but from now on, show him the proper respect.”

“Great Hero Song. I sincerely apologize.”

When I straightened from my deep bow, I saw the Roaring Fury Swordsman’s face, red with anger.

Even after receiving my apology, he probably didn’t feel as though he had received one.

Meanwhile, despite apologizing to someone I disliked, I felt refreshed, as though I had just circulated my qi.

*Is this what comes with age?*

Take a look at that verbal skill forged over a hundred years.

He wasn’t just a Supreme Peak master in martial arts. At this point, he could change his title from Fire King to Tongue King.

After completing every step of the settlement under his supervision, the Tongue King announced in a solemn voice,

“All right. Now all the uninvited guests can get the hell out. If you’re hungry, have a bowl of rice before you go.”

He was treating them like beggars now.

The Roaring Fury Swordsman trembled with humiliation, then finally opened his mouth after a long while.

“…Then we will take our leave.”

“I won’t see you out.”

“Let’s go!”

As though he had been waiting for those words, the Roaring Fury Swordsman turned sharply around. Gong Ilhyuk and the other two members of the Three Hands of Zhongnan, who had been making all kinds of ugly faces, followed him.

Scorching gazes pursued the backs of the four men. Just before stepping through the main gate, the Roaring Fury Swordsman suddenly turned his head and stared at me.

A line of Sound Transmission filled with killing intent accompanied his words.

— I don’t know what connection you have to that old man… but as long as I’m alive, I will definitely punish you and the Jin Family of Taiyuan.

It happened in a moment brief enough to be called an instant.

As the Fire King watched the Roaring Fury Swordsman’s back disappear into the darkness with an unreadable expression, he tossed out a single remark.

“I’ll step out for a while.”

“Yes? Where are you going?”

“At my age, do I need to report every time I go relieve myself?”

He gruffly disappeared with a bowlegged gait.

* * *

Once the Roaring Fury Swordsman had moved a good distance away from the Jin Family of Taiyuan, he suddenly drew his sword and swung it.

Whoosh! Boom!

Dozens of streams of Sword Energy cut through trees and smashed rocks. After raging for quite some time, he finally turned his fury toward the Three Hands of Zhongnan, including Gong Ilhyuk.

“You bunch of idiots…”

“E-Elder.”

“Do you know what kind of humiliation this old man suffered because of you?”

“I-I’m sorry. Please forgive your foolish Disciple.”

The Three Hands of Zhongnan froze.

Gong Ilhyuk was especially terrified. If he had not incited the Roaring Fury Swordsman to come to the Jin Family of Taiyuan, none of this would have happened.

“E-Elder, please calm down and listen to me.”

“I let things slide a few times because you’re related to my Junior Brother, the Sect Leader, and now it seems you’ve forgotten your place.”

Crack!

The Roaring Fury Swordsman’s emaciated hand clamped around Gong Ilhyuk’s neck.

“Guh… I-I’m the Sect Leader’s…”

“Do you think my junior brother, the Sect Leader, would bat an eye if this old man punished one of you? You worthless piece of trash.”

Gong Ilhyuk’s face went deathly white.

Then—

Thump. Thump. Thud.

His body went limp, his head lolling to one side. The other two members of the Three Hands, who had been frozen with terror, also collapsed helplessly where they stood.

“W-why did these bastards suddenly…”

The Roaring Fury Swordsman, briefly confused, turned his head. He stared intently into the darkness before speaking.

“Do you still have business here?”

“Why else would I have come looking for you?”

Along with that calm voice, an old man of small stature appeared.

The Fire King, Jeok Cheongang.

He clicked his tongue as he looked at the fallen Three Hands of Zhongnan.

“Tsk, tsk. It seems I ended up saving those bastards by accident. Perhaps I should have come a little later.”

“Why have you come back?”

“It’s been a long time. I didn’t want to send you away just like that.”

The Fire King smiled faintly and added,

“There was also something I forgot.”

“Something you forgot? What do you mean…”

At that moment, Jeok Cheongang’s figure vanished like a phantom.

At the same time, Sword Energy erupted from the Roaring Fury Swordsman’s waist.

Sshh-shh-shh-shh-shk!

A dense net of Sword Energy spread across a three-jang radius, slicing through bone and flesh the instant it touched them.

But the big fish had already swum upstream.

“I told you earlier. Don’t touch even a single hair on that boy.”

Crack!

The hilt fell from the Roaring Fury Swordsman’s grip. His wrist broken, he screamed and drove his knee upward.

“Gyaaah! You fucking old bastard!”

“When will you finally become a proper human being?”

At the same time, a palm engulfed in pure-white flames pressed against the Roaring Fury Swordsman’s chest.

Boom!

“Guh…!”

An unavoidable palm strike.

His Body-Protecting Qi shattered, and his flesh and bones began to cook. Blood burst from his mouth as he fell to his knees, his eyelids trembling.

“Cough… F-Flame Divine Palm…”

“Raise your head and look at me.”

The old man’s voice was so cold that it made the title Fire King seem meaningless.

The Roaring Fury Swordsman barely managed to lift his head—and met a pair of eyes in which blue ghost flames flickered.

“F-Fire King.”

“That’s right. This old man is the Fire King.”

The Roaring Fury Swordsman had briefly forgotten just what kind of monster the Fire King, Jeok Cheongang, truly was.

Jeok Cheongang had been active in Murim for only a single year in his entire life. Yet with a single battle, he had become a legend and carved his mark into Murim history.

He was an opponent the Roaring Fury Swordsman could never stand against.

Deep despair settled over the Roaring Fury Swordsman’s face.

“Are you… are you planning to kill me?”

“If killing you would have ended everything, this old man would have done it long ago.”

“Then…”

“Remember one thing.”

The Fire King slowly parted his lips.

“You may kill Jin Taekyung. Even if you wipe out the Jin Family of Taiyuan, I will stand by and watch. But if that happens, I will go to the Zhongnan Sect.”

“……!”

“I will smash the Zhongnan Sect’s signboard and burn down Mount Zhongnan. If you abandon your main sect and flee, I will chase you to the ends of the earth and kill every last one of you. I will do so until the day my breath stops.”

The Roaring Fury Swordsman’s entire body trembled beneath the terrifying killing intent.

Everything Jeok Cheongang was saying was sincere. He was declaring that he would face the Zhongnan Sect alone.

If such a thing happened, it was impossible to imagine how many sacrifices would be required.

“What… what am I supposed to do?”

“The choice is yours. The punishment for it belongs to this old man.”

Jeok Cheongang left those words behind and vanished without a trace.

It was a long while before the Three Hands of Zhongnan finally woke. They were startled to find the Roaring Fury Swordsman sitting there in a daze.

“E-Elder!”

“What happened?”

“Who in the world did this?”

The Roaring Fury Swordsman opened his mouth only after a very long time.

“We’re going back. To Zhongnan.”

There was terror and fear in his voice, and the Three Hands of Zhongnan could say nothing.
## Chapter artifact 194

# Chapter 194

“Ahh, that hit the spot.”

Jeok Cheongang, who had said he was stepping away for a moment to relieve himself, returned a quarter-hour later. Something felt suspicious, and I narrowed my eyes.

“Why are you looking at me like that?”

“Did you really just go relieve yourself?”

“Do you need to smell me before you’ll believe me?”

“But it took you a whole quarter-hour. Could it be that—”

“This old man has stamina to spare.”

“…”

How much stamina did he have if it took him fifteen minutes to pee?

At that point, wasn’t it less a stream and more a fire hose?

When I stared at him in disbelief, Jeok Cheongang raised his eyes.

“What? You got a problem?”

“Of course not.”

A problem? Me?

Considering all the help he had given me today, I could bow to him a hundred times and it still wouldn’t be enough.

*And then there’s the other thing…*

I pushed aside the thought that had suddenly occurred to me.

The Fire Gate Clan’s sacred treasure. The Fire King’s Disciple.

I also pretended not to hear the voices that had been whispering nonstop ever since.

*Disciple? That’s ridiculous.*

It was an issue I had never once considered before.

Why would a man accept as his new Disciple someone he had known for only a day—someone who had killed the Disciple he had cherished like a son?

*Even if that Disciple had been a colossal son of a bitch.*

As I was thinking about it, Jin Wikyung approached and respectfully cupped his hands toward Jeok Cheongang.

“I, Jin Wikyung, a junior of Murim, pay my respects to the Fire King Jeok Cheongang, whose fame resounds throughout the world.”

“Are you from the Jin Family?”

After scanning Jin Wikyung from head to toe, Jeok Cheongang nodded as though he had figured something out.

“Then you’re this brat’s father?”

“What?”

“Teach your son properly. The boy is young, yet he’s already getting hotheaded and causing trouble. His manners are terrible, too.”

Jin Wikyung answered with the darkest expression I had ever seen on his face.

“…”

“He’s my younger brother.”

“Hm?”

“I’m Taekyung’s eldest brother.”

Jeok Cheongang’s face turned serious.

“Don’t joke around. I understand wanting to look young, but getting too greedy will bring down Heaven’s punishment.”

“It’s the truth. I am Jin Wikyung, the Lesser Family Head of the Jin Family of Taiyuan.”

“…”

“By any chance, how old are you?”

“I turned thirty-six this year.”

Jeok Cheongang muttered with an expression of disbelief.

“You look forty-six.”

His face was, admittedly, somewhat—quite a lot, actually—more weathered than his age suggested. I had mistaken him for my father at first, too.

At least his hair was still thick, but there seemed to be no solution for a face that had taken a 160-kilometer-per-hour fastball from time.

Seeing the sadness on Jin Wikyung’s face, Jeok Cheongang tried to comfort him.

“It’s all right. A man is judged by his abilities. You’ve got a pretty wife and adorable children, so what more do you need? Heh heh.”

“I’m still single.”

“…At thirty-six?”

In modern times, that would only be around the age when people started thinking about marriage. But in Murim, where early marriage was common, thirty-six was old enough to have grandchildren.

The single Jin Wikyung answered shortly.

“Yes.”

“…”

This silence lasted a while. The Fire King furrowed and relaxed his brow several times, flaring his nostrils before finally heaving a deep sigh.

“Damn it. I could really use a drink.”

I snorted quietly. It was a feast day like this one—how could there be no alcohol? There was enough of it lying around to drown in.

“Would you like a drink?”

Jeok Cheongang’s eyes went round.

“You insolent brat. Are you making fun of this old man?”

“What?”

“Bring me the whole crock.”

* * *

A mood was like a spark. Once it went out, it was difficult to set alight again.

Yet even after the uninvited guests from the Zhongnan Sect had poured cold water over everything, the spark had not died.

No—in the presence of the Fire King, it had begun blazing even more fiercely.

“Wooooo!”

“Drink! I said let’s drink!”

“I never thought I’d live to see the Fire King in person!”

“When the Fire King gets flustered, he goes Right Fire King, Left Fire King![^2]”

[^2]: This puns on *jwa-wang-u-wang*, a Korean expression for being flustered or running around in confusion; *jwa* and *u* mean “left” and “right,” while *wang* means “king.”

“…”

I didn’t know who that was, but that bastard had nearly put out the spark just now.

At my glance, Hyuk Mujin, who had been standing by, quietly slipped away to hunt down the mood killer.

Meanwhile, Jeok Cheongang was receiving greetings from countless people.

“Great Hero Jeok! It’s the honor of a lifetime to meet you!”

“Please do us the honor of visiting our sect sometime…”

“Please grant us your guidance!”

It was truly a sea of people.

The name Jeok Cheongang, the Fire King, was practically a living legend.

Moreover, his whereabouts had been unknown for decades, so most people had accepted his death as an established fact.

And now the Fire King, whom everyone had thought dead, had appeared—not in the Central Plains or Mount Jiuhua, but right here at the Jin Family of Taiyuan in Shanxi Province.

*Of course everyone’s going to lose their minds.*

Perhaps this was what it would be like if a legendary singer once called the Emperor of Pop came back from the dead.

Yet despite the enthusiasm of his local Shanxi fans, Michael Cheongang looked thoroughly displeased.

Jin Wikyung seemed to notice, too, and sent me a Sound Transmission.

—Youngest.

The only people who could carry on a lengthy conversation with the eccentric Jeok Cheongang were Cheongpung and me. But Cheongpung was impossible to predict, so in the end, I had no choice but to act as the messenger.

“Is there somewhere uncomfortable?”

“Look at the state I’m in. Wouldn’t you be uncomfortable if you were me?”

Jeok Cheongang glared at the wine crock beside him. Quite a bit of time had passed, yet hardly any of it had been emptied.

It wasn’t that he disliked alcohol. He simply hadn’t had enough time to drink.

“Damn it. It shouldn’t be this hard to have a single drink.”

There were people asking him to accept them as Disciples, Sect Leaders and merchants begging to host him as an honored guest.

One heavily pregnant woman had even asked if she could touch his nose. She wanted to receive the Fire King’s qi so she could give birth to a great person, or something like that.

*Was he a dol hareubang or something?[^1]*

It was enough to make even the onlookers snicker. How much worse must it have been for the person at the center of it all?

Frankly, the fact that Jeok Cheongang had endured this much was impressive in itself.

“Why don’t we move somewhere I prepared in advance? It’s quieter there.”

“Ugh. Forget it.”

“You said you were uncomfortable.”

“I said forget it. Why are you so damn talkative?”

Even while grumbling, Jeok Cheongang stubbornly refused to leave. I tilted my head.

*What’s going on?*

We had known each other for only a short time, but I had gotten a fairly good sense of his personality.

It was obvious that he hated noisy places and found people’s attention bothersome. That was probably why he had spent his entire life on Mount Jiuhua in the first place.

*Then why?*

I watched Jeok Cheongang carefully.

In front of him, the owner of a merchant association with considerable influence in Shanxi Province was bowing and scraping.

“Great Hero Jeok! I’ve heard all about your thunderous reputation throughout the world. When I was young, I admired you so much…”

“Get to the point.”

“I have always admired you from the bottom of my heart, so I prepared a small token of my sincerity.”

“A small token?”

“Yes. It’s something I acquired recently, but I suppose every item has its rightful owner.”

The merchant took a small wooden box from inside his robe and opened the lid. A ring set with clear jade appeared inside.

“It is a Poison-Averting Ring.”

“A fairly valuable item. It must have been difficult to obtain.”

The merchant waved his hands exaggeratedly.

“Having the honor of seeing your noble face, how could price possibly matter? It only cost a thousand silver nyang. Heh heh.”

A thousand silver nyang for a single ring. It was among the most expensive gifts the Jin Family of Taiyuan had received so far.

Jeok Cheongang, however, merely nodded without much interest.

“Well, you’re giving it to me, so I’ll accept it gratefully. What was your name and where are you from?”

“I’m in charge of the Yangcheon Merchant Association…”

“Yangcheon? That’s near Hebei.”

The merchant had been interrupted before he could even give his name, but he bowed as though he had received an honor.

“Yes. We are trying to begin trade with the Hebei Peng Family, but it has been difficult.”

That was the merchant’s real purpose.

The reason he had come to Jeok Cheongang, even after offering a token of sincerity that was anything but small.

In short, he wanted Jeok Cheongang to help him establish a business relationship with the Hebei Peng Family.

“The Peng Family. Who’s the Family Head these days?”

“It is Great Hero Peng Cheolyeong, the Iron Blood Saber.”

“I’ve never heard of him. Is he the Thunderbolt Saber King’s son?”

“Yes, yes. The Thunderbolt Saber King retired from the front lines and passed the position of Family Head to him.”

“This old man once had a drink with the Thunderbolt Saber King when I was young. All right, I understand.”

That was the end of the conversation. The merchant left, grinning from ear to ear, after setting down the wooden box.

Beneath it lay a stack of bank drafts that had not been there moments ago.

I took advantage of the merchant’s retreat to whisper to Jeok Cheongang.

“You know the Thunderbolt Saber King?”

As his title suggested, the Thunderbolt Saber King was one of the Ten Kings, a Supreme Peak master just like Jeok Cheongang.

Jeok Cheongang took a sip of wine before answering.

“I told you. We had a drink together.”

“Wow.”

He spoke of the Thunderbolt Saber King as though he had met an old neighborhood friend. Every time he did something like this, I was reminded just how extraordinary Jeok Cheongang was.

When I gaped at him in admiration, Jeok Cheongang puffed out his chest.

“I flattened that bastard’s nose back in the day.”

“…What?”

“I was having a drink with the Sword Saint when he barged in without a word and picked a fight. We went a few rounds, and I taught him a lesson.”

What the hell was he talking about?

“Weren’t you two friends?”

“Me? With that guy?”

Jeok Cheongang furrowed his brows.

“What would I gain from associating with such an uncultured bastard? We never saw each other again after that.”

“…”

“Later, some strange rumor even started going around. They said that the Peng Family’s man and I had exchanged over a hundred moves, acknowledged each other, and withdrawn. The bastards from the Hebei Peng Family must have pulled some kind of trick.”

I was dumbfounded, and so was everyone around me.

The story about the Thunderbolt Saber King was absurd enough, but if it was true, the merchant’s request had just gone up in smoke.

“Th-then the Yangcheon Merchant Association can’t do business with the Hebei Peng Family, can they? Mentioning Great Hero Jeok’s name will only make things worse.”

Jeok Cheongang blinked.

“The Yangcheon Merchant Association? What’s that?”

“…”

“Ah, you mean that guy from earlier? Why should I care about him?”

“But you said you would help him trade with the Hebei Peng Family.”

“He asked me to meet him, so I met him. It’s also true that I had a drink with the Thunderbolt Saber King. Is there even a shred of falsehood in anything I said?”

“…”

I wasn’t sure about that, but he certainly seemed to be missing even a shred of conscience.

His shamelessness was so impressive that I almost felt respect for him.

*Fire King, are you even human?*

He had more than one or two victims. The people who had believed Jeok Cheongang’s empty promises and offered him a “small token of sincerity” would soon realize that everything had been complete bullshit and pound the ground in despair.

*At this point, this is organized fraud.*

But there would be no victims.

No one brave enough to come to the Fire King, Jeok Cheongang, and demand their gifts back existed.

“We would be honored if you would visit our sect sometime…”

“Hmm. I’ll drop by one day.”

That meant he would visit after he died and wandered the netherworld.

“This is my small token of sincerity…”

“I’ll accept it.”

*No. He really is just taking it.*

As I watched the various treasures, elixirs, and bank drafts piling up like a mountain, I realized something.

*Was this why he had stayed behind?*

It was clearly a grand plan to make one big haul in his old age.

Eventually, after dealing with dozens of suckers, Jeok Cheongang opened his mouth.

“Hm. This is quite a haul. Aren’t there any more?”

Jin Wikyung answered with an exhausted expression.

“Yes. It seems that everyone who was likely to come has already arrived.”

“A shame. I could have squeezed more out of them.”

*Look at the greed on this old man.*

Jeok Cheongang gazed at the spoils he had earned by drinking instead of sweating, then stretched his arms high above his head.

“Good grief, this is tiring.”

“…”

“Why are you looking at me like that?”

I subtly averted my gaze from Jeok Cheongang’s round eyes.

“It’s nothing. I was just admiring you.”

“From where I’m standing, it doesn’t look like admiration.”

“I’m serious. There’s nothing wrong with having a lot of money.”

“Is that so?”

Jeok Cheongang let out a quiet laugh before casually tossing out another remark.

“Then you take it.”

“What?”

“I’m saying I’ll give all of it to you.”

“All of that?”

“It’s completely useless to this old man, but it’s different for you. Whether you scatter it across the street or do anything else with it, I won’t care. Take it.”

What was going on?

I stared at Jeok Cheongang with a bewildered expression.

*Why all of a sudden?*

He had already helped me immensely. Naturally, I wanted to know why he was showing such excessive favor to me and the Jin Family of Taiyuan.

Could it really be what I thought? Could he truly mean it?

I swallowed dryly and opened my mouth.

“Great Hero Jeok, by any chance…”

At that moment, Jeok Cheongang rose from his seat and spoke with a drunken expression.

“Ahh, I’m drunk. I’m going inside to rest. See you tomorrow.”

“…”

I watched Jeok Cheongang stagger away before turning my gaze back to the wine crock.

The moon was reflected in the crock, which he had not even emptied a quarter of.

[^1]: A dol hareubang is a stone guardian statue from Jeju Island. Folk beliefs associate touching its nose with fertility.

# Checkpoint Review — 120–124

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

# Chapters 120–124

## Plot

Jin Taekyung kills Pung Yang with the Unnamed Sword after its Ten-Thousand-Year Cold Iron destroys Pung Yang’s Body-Protecting Qi. The victory completes the Temporary Strength Pill Quest, restoring Taekyung’s health and granting five level-ups, substantial EXP and Fame, and medicines that save many wounded Mount Heng Sword Sect survivors. Taekyung also fully absorbs the Blazing Flame Divine Pill, reaching forty-five years of internal energy with the Scorching Yang Qi attribute.

The Mount Heng Sword Sect is devastated, but Lee Seowol remains Sect Leader and vows to rebuild it. She accepts Jin Wikyung’s invitation to the Jin Family of Taiyuan’s New Year gathering and offers the Jin Family the sect’s territorial rights as an apology. She also offers the Blood Wolf Sword Technique, Blood Wolf Footwork, and Shura Annihilating Fist in exchange for marrying Taekyung. Taekyung initially rejects the proposal because Seowol is seventeen and because he loves Song Song, while Jin Mukyung insists that the three Peak martial arts make the marriage worthwhile.

Taekyung reveals that Jopil left behind the Flame Divine Palm, a Supreme Peak secret art of the Fire Gate Clan restricted to practitioners with Scorching Yang Qi. Mukyung warns that possessing another sect’s secret technique could make the Jin Family thieves in the eyes of the Murim. The art belonged to the Fire King, one of the world’s twenty greatest experts, whose survival after a legendary battle at Mount Jiuhua remains unknown. Mukyung returns to the Jin Family while still recovering, accompanied by Hyuk Mujin. Wolhwa departs to tour northern Shanxi and promises to maintain close ties with the Jin Family. After the carriage leaves, Lee Seowol appears and addresses Taekyung as Benefactor.

## Continuity

- Pung Yang is dead, and the Red Wind Band’s remaining forces and wider response to his death remain unresolved.
- Taekyung has fully absorbed the Blazing Flame Divine Pill and possesses forty-five years of internal energy with the Scorching Yang Qi attribute.
- The Temporary Strength Pill Quest granted Taekyung five level-ups, major EXP and Fame, and Full Recovery; the pill’s origin and long-term effects remain unknown.
- Jin Mukyung survived his Internal Injuries and can travel, but he is not fully recovered.
- Cheol Mubaek has broken limbs and serious Internal Injuries and requires at least four months of recuperation.
- Twenty-five Mount Heng survivors remain, including Lee Seowol; five were initially unlikely to survive. The sect’s reconstruction remains uncertain.
- Lee Seowol is seventeen, remains Sect Leader, accepted the New Year invitation, and has proposed marriage to Taekyung in exchange for three Peak martial arts.
- Taekyung intends to reject Seowol’s political marriage because he loves Song Song, but the proposal and territorial transaction have not been resolved.
- Cheol Mubaek gave Lee Seowol the Shura Annihilating Fist manual despite its single-successor, transmission-only-to-the-worthy tradition.
- Taekyung possesses Jopil’s Flame Divine Palm manual. Jopil claimed to be its nineteenth-generation successor, but how he obtained it and whether the claim is true remain uncertain.
- The Flame Divine Palm is a Fire Gate Clan secret art restricted to owners of Scorching Yang Qi. The Fire Gate Clan follows a single-successor tradition.
- The Fire King, the art’s legendary master, may still be alive.
- Wolhwa is Eun Sowol, the Lower District Sect’s Shanxi Branch Leader, and plans to tour northern Shanxi while preserving the alliance with the Jin Family.

## Translation Decisions

- Retain **Peak**, **Supreme Peak**, **Internal Injury**, **Severe Injury**, **Body-Protecting Qi**, **Scorching Yang Qi**, **Red Wind Band**, **Sect Leader**, **Benefactor**, and **Taiyuan Jin Family**.
- Render **잠력단** as **Temporary Strength Pill**, **열화신단** as **Blazing Flame Divine Pill**, **완전 회복** as **Full Recovery**, **만년한철** as **Ten-Thousand-Year Cold Iron**, and **이름 없는 검** as **Unnamed Sword**.
- Render **혈랑검법** as **Blood Wolf Sword Technique**, **혈랑보법** as **Blood Wolf Footwork**, **절정 무공** as **Peak martial arts**, **파천신권** as **Shura Annihilating Fist**, and **열화문** as **Fire Gate Clan**.
- Render **화왕** as **Fire King**, **구화산** as **Mount Jiuhua**, **진무보법** as **Jin Family’s Manoeuvre Technique**, **일인전승** as **single successor**, and **비인부전** as **transmission only to the worthy**.
- Preserve the Samsung/Samseong pun with a clarifying footnote; retain **Jaringobi** with its explanatory footnote.

## Durable state

{
  "active_continuity": [
    "Pung Yang is dead; Jin Taekyung killed him after the Unnamed Sword's Ten-Thousand-Year Cold Iron destroyed his Body-Protecting Qi and pierced his chest.",
    "Taekyung fully absorbed the Blazing Flame Divine Pill and possesses forty-five years of internal energy with the Scorching Yang Qi attribute.",
    "Jin Mukyung survived his fight with Pung Yang and has recovered enough to return to the Jin Family, though he is not fully healed.",
    "Cheol Mubaek and the other wounded Mount Heng martial artists are recovering; Cheol has broken limbs and serious Internal Injuries and needs at least four months of recuperation.",
    "Lee Seowol remains Sect Leader of the Mount Heng Sword Sect and vows to preserve it for those who died defending it.",
    "The Lower District Sect sent a relief force with physicians, cooks, and laborers after the battle.",
    "Wolhwa's real name is Eun Sowol, and she is the Lower District Sect's Shanxi Branch Leader with authority over more than thirty Shanxi branches.",
    "Lee Seowol accepted Jin Wikyung's invitation to the Jin Family of Taiyuan's New Year gathering.",
    "Lee Seowol offered the Mount Heng Sword Sect's territorial rights to the Jin Family of Taiyuan as an apology.",
    "Lee Seowol proposed marriage to Jin Taekyung in exchange for the Blood Wolf Sword Technique, Blood Wolf Footwork, and Shura Annihilating Fist.",
    "Lee Seowol is seventeen years old.",
    "Jin Taekyung has decided to reject Lee Seowol's political marriage proposal because of her age and because he loves Song Song.",
    "Forty-seven mounted bandits survived the battle, but the Lower District Sect can save only about thirty with its available medicine.",
    "The Lower District Sect is spreading a rumor that the two Jin brothers defeated Pung Yang and rescued the Mount Heng Sword Sect.",
    "Cheol Mubaek is the ninth-generation successor of the Shura Annihilating Fist and gave its manual to Lee Seowol despite its inheritance traditions.",
    "Cheol Mubaek and Lee Cheonbaek first met more than thirty years ago, fought, and then became close friends.",
    "The Shura Annihilating Fist was an ancient top-ten fist technique whose lineage was believed to have ended and is no longer a current top-ten technique.",
    "Jopil is dead and left behind the Supreme Peak martial art Flame Divine Palm.",
    "Jin Taekyung possesses the Flame Divine Palm manual, a Fire Gate Clan secret technique restricted to owners of Scorching Yang Qi.",
    "The Fire King is a Supreme Peak master among the world's twenty greatest experts; his current status is unknown, and the Fire Gate Clan has a single successor."
  ],
  "continuity_sources": [
    124,
    123
  ],
  "open_questions": [
    "How will the Jin Family of Taiyuan respond to Lee Seowol's proposed transaction and territorial transfer?",
    "Can Lee Seowol preserve or rebuild the Mount Heng Sword Sect with so few survivors?",
    "What is the origin and full long-term effect of the Temporary Strength Pill?",
    "What consequences will Pung Yang's death have for the Red Wind Band and the wider Murim?",
    "Is the Fire King still alive, and if so, where is he?",
    "Was Jopil truly the nineteenth-generation successor of the Flame Divine Palm, and how did he acquire it?"
  ],
  "safe_through": 124,
  "temporary_decisions": [
    "Render 잠력단 as Temporary Strength Pill and 호신강기 as Body-Protecting Qi.",
    "Render 만년한철 as Ten-Thousand-Year Cold Iron and 이름 없는 검 as Unnamed Sword.",
    "Render 열화신단 as Blazing Flame Divine Pill and 반 갑자 as half a jiazi, clarified as thirty years.",
    "Render 완전 회복 as Full Recovery and 회광반조 as final rally in this death-and-recovery context.",
    "Render 운칠기삼 as seven parts luck and three parts skill, and 운구기일 as nine parts luck and one part qi, with a footnote explaining the variation.",
    "Render 은공 as Benefactor, 절정 무공 as Peak martial arts, 급식 as school lunch, 고딩 as high schooler, 철컹 as clank, 산서성 as Shanxi Province, and 총지부장 as Chief Branch Leader.",
    "Render 일인전승 as single successor, 비인부전 as transmission only to the worthy, 구 대 계승자 as ninth-generation successor, and 천하십대권법 as the ten greatest fist techniques in the world.",
    "Render 열화문 as Fire Gate Clan, 화왕 as Fire King, 삼성 as Three Saints, 십왕 as Ten Kings, and 진무보법 as Jin Family's Manoeuvre Technique; retain the Samsung/Samseong clarification footnote."
  ],
  "version": 1
}

## Reading copies

## Chapter artifact 120

# Chapter 120

*Shwick!*

A sword thrust forward—slowly, but with tremendous force.

For the briefest moment, a mocking smile appeared at the corner of Pung Yang’s mouth.

*I knew this was coming.*

He had spent decades living on a plateau where every kind of underhanded trick ran rampant. If he had been foolish enough to fall for the same trick twice, he would have become wild-dog food long ago.

*But where did that sword come from?*

It wasn’t a dagger. Where had the brat hidden a longsword that size?

With that slight question in mind, Pung Yang drew up his Body-Protecting Qi.

*Fssssss.*

He had expected this, so his response was quick. Red qi surged upward in an instant and wrapped tightly around his body.

Body-Protecting Qi was invincible armor that nothing short of powerful Sword Energy could put so much as a scratch on. The young brat’s futile struggle was nothing but laughable.

*What an annoying bastard. Just die already.*

He was about to snap Jin Taekyung’s neck in a single motion when—

*Thud!*

“……Huh?”

A chilly coldness pierced into his body, followed by searing pain. Pung Yang stared wide-eyed at the sword that had pierced straight through his chest.

*What the hell?*

His Body-Protecting Qi had vanished.

No—it had been destroyed.

Jin Taekyung’s sword sliced through it as easily as cutting tofu, then pierced Pung Yang’s chest as well.

Pung Yang looked down at the transparent blade, not a drop of blood staining it, and muttered like he was groaning.

“Ten-Thousand-Year Cold Iron……?”

He had heard of it before. Stories about a divine weapon said to be capable of cutting and breaking anything in the world.

“How did you get this?”

Pung Yang glared at the sword’s owner with a twisted expression. The young brat from the Jin Family of Taiyuan blinked innocently before opening his mouth.

“Wow. This actually worked.”

“You fucking bastard……!”

He wanted to snap the brat’s neck right away, but his vision suddenly went hazy, and the strength drained from his fingers. The power that had filled his body vanished like the outgoing tide, leaving only helplessness in its wake.

*The Temporary Strength Pill had to wear off now of all times.*

Blood began flowing from the seven openings in Pung Yang’s face as he staggered backward.

His various injuries, both great and small, combined with the dispersal of his Body-Protecting Qi. The internal energy surging backward through his body began driving him rapidly toward death.

*I can’t die like this. I can’t.*

Pung Yang hurriedly searched inside his robes.

He still had one Temporary Strength Pill left. If he took it, he could beat the bastards to death in a single stroke and leave this place. He had lost quite a lot, but he could recover, then return to the Murim.

Yes. If he just took the Temporary Strength Pill……

*Clatter.*

Damn it. He was too desperate.

The wooden box slipped from Pung Yang’s frantic hand, struck the ground, and sprang open. A pill tinged with a blood-red color rolled across the ground before coming to a stop beneath someone’s foot.

“Oh, is this the Temporary Strength Pill?”

Jin Taekyung picked it up and examined it with curiosity. Pung Yang shouted at him.

“G-Give it to me! Hurry!”

“Here’s a question. Do you think I’ll give it to you just because you ask?”

“You bastard!”

Pung Yang threw himself forward with all his remaining strength, but his ruined body had already reached its limit. Before he could reach Jin Taekyung, his legs gave out and he collapsed.

Only one path remained to Pung Yang now.

“Please. I’m begging you. Give it to me. Give it to me!”

“What if I do?”

Pung Yang cried out desperately.

“You’ll never see me again. No—instead, I’ll swear my loyalty to you from now on!”

“Oh, having a Peak master as a subordinate. That sounds pretty good.”

“R-Really? Then hurry and give me the Temporary Strength Pill!”

“First, I’m taking my property back.”

“Your property?”

His question was answered a moment later. Jin Taekyung approached and yanked the sword from the center of Pung Yang’s chest.

Blood poured out like a waterfall, accompanied by dizzying pain.

“Gueeeeegh!”

Pung Yang did not even notice that chunks of his internal organs were mixed into the blood he vomited.

All he felt was his vision gradually darkening and the sounds around him receding into the distance.

He was dying, and desperation had driven him half-mad.

*I want to live.*

Pung Yang had spent his entire life as a ruthless marauder.

He had stolen the wealth—and sometimes the lives—of countless people, but he had never once imagined that he would meet an end like this.

“Now, now, please give me the Temporary Strength Pill……”

Through his blurred vision, he saw Jin Taekyung shake his head. Pung Yang mumbled piteously.

“Why? Why not?”

But the answer came from somewhere else.

“What? Why?”

“That bastard deserves to be torn limb from limb!”

The surviving martial artists of the Mount Heng Sword Sect gripped their weapons, their eyes brimming with killing intent.

Lee Seowol also bit down on her lip and drew her bow toward Pung Yang, but Jin Taekyung hurriedly stopped her.

“Let’s lay off the finishing blow for now…… No, he’s too vicious to let him die comfortably. It’s better to leave him there and let him die slowly.”

For a brief while, Lee Seowol struggled with herself. In the end, she lowered her bow. Jin Taekyung approached Pung Yang and whispered softly into his ear.

“I’m starting to get tired too. Let’s just die now.”

Pung Yang didn’t know what he meant, but one thing was certain.

Death.

Pung Yang realized that his own death was almost upon him.

“Even as a vengeful ghost, I’ll have my revenge.”

“Amen. In your next life, be satisfied with Viagra.”

Pung Yang gave a hollow laugh. It was absurd that he had to listen to that bastard’s incomprehensible nonsense until the very end.

*Damn. What terrible weather.*

He raised his head and looked at the sky. It was dyed entirely red.

Then it was swallowed by darkness.

* * *

As Pung Yang’s head lolled to the side, celebratory fireworks burst overhead.

*Ding. Ding. Ding!*

> **System**
> - Defeated **Lv. 85 Pung Yang**!
> - Successfully completed the **Temporary Strength Pill** Quest!
> - Obtained a massive amount of **EXP** and **Fame**!
> - Level Up!
> - Level Up!
> - …

After announcing five level-ups and an increase in Fame, the System window delivered even better news.

> **System**
> - The Quest success reward has been delivered to your **Inventory**!
> - **Full Recovery** has taken effect immediately as the Quest success reward!

*Full Recovery?*

It said the effect would be immediate, and the change happened exactly as promised.

Cracked and broken bones knitted back together. Cuts and punctures healed as if they had been washed clean. The changes did not stop at the surface.

*The Internal Injuries……*

Invisible healing took place inside my body as well. I had expected all my Internal Injuries to heal, but there was an even greater benefit than I had imagined.

> **System**
> - All **Internal Injuries** have healed!
> - Your stabilized body accepts new qi!
> - The **Blazing Flame Divine Pill** has been fully absorbed!
> - Your **internal energy** has risen to 45 years!
> - Your **internal energy** has gained the **Scorching Yang Qi** attribute!

The Blazing Flame Divine Pill had been completely absorbed.

And my internal energy had risen explosively.

I could feel power filling every limb and bone. The Scorching Yang Qi that had burned through my body like lava had somehow become a warm spring breeze.

*I did it.*

I had planned to circulate my qi and control the Scorching Yang Qi once my body recovered somewhat from the level-ups, but thanks to the System, I had handled the difficult part with ease.

*Forty-five years? How much is that?*

Compared to what I had originally possessed, it was three times as much—an additional half a jiazi, or thirty years, of internal energy.

*A half jiazi.*

Under normal circumstances, I would have put off taking the Blazing Flame Divine Pill. But the gamble I had taken had come back as a masterstroke.

*I would have died if luck hadn’t been on my side, though.*

Two strokes of heavenly luck.

One was the Blazing Flame Divine Pill, and the other was the **Unnamed Sword** in my hand.

Both were loot I had obtained after defeating Jopil several months ago.

*I would have been in serious trouble without this.*

I had thought it was merely a sword that was a little sharper and harder than other swords. I had never dreamed that it was actually Ten-Thousand-Year Cold Iron, or that it possessed such an ability.

In that sense, the saying *seven parts luck and three parts skill* didn’t suit me today. *Nine parts luck and one part qi* was much more appropriate.[^1]

*Though I’m not sure this can really be called good luck.*

I slowly looked around.

A graveyard of weapons stood with their hilts buried upside down. Some people had died with their faces planted in pools of blood. Others stared wide-eyed at the sky as dawn began to break.

There were hundreds of corpses like that.

“There’s a survivor here!”

“Chunsam! Come around!”

Amid that horrific scene, the martial artists of the Mount Heng Sword Sect moved tirelessly. As I watched them rescue the few survivors with disciplined efficiency, I was suddenly seized by an inexplicable sense of wrongness.

*What is it?*

It felt like I had forgotten something important……

Just as I was frowning, one of the corpses that had been lying motionless raised its upper body.

“Guuuuuh.”

“Oh.”

Right. Good to see you, Mukyung.

* * *

By the time the four-hour search was over, Lee Seowol’s body was soaked in blood.

“How many survivors?”

“Twenty-five, including you, Sect Leader.”

“How many did you say?”

“Twenty-five. Five of them probably won’t make it through today.”

Both Lee Seowol, who had asked the question, and the martial artist who answered it fell silent.

The Mount Heng Sword Sect, which had once divided control of Shanxi with the Jin Family of Taiyuan, no longer existed. All that remained were the injured and a young Sect Leader who was not even twenty years old.

*If I had abandoned this place and fled, if I had accepted Pung Yang’s marriage proposal from the beginning, could I have saved them?*

Regret was always pointless.

But Lee Seowol had to regret.

Although few remained, she was still the Sect Leader of a sect. Only by agonizing over her mistakes and regretting them to the bone could she avoid making the same mistakes again.

That was her atonement to those who had died today and her effort on behalf of those who remained.

*The Mount Heng Sword Sect will survive. If only for those who gave their lives for our sect.*

Lee Seowol clenched her fist. Her fingernails, broken from drawing the bowstring, dug into her flesh as she clenched her fist. Blood seeped out, but she felt no pain.

“What about the others?”

“They’re all in the main hall. There’s a woman from the Jin Family of Taiyuan who knows a fair amount about medicine, and she’s treating the wounded, but……”

The martial artist’s expression darkened. It was proof of just how bad the condition of some of the wounded was.

Lee Seowol did not ask anything else and headed toward the main hall.

*I’m sending them off again before we’ve even had time to recover.*

Unbearable fatigue pressed down on her entire body, but she held on through sheer willpower.

At the very least, she had to see off those who were leaving.

*Creeeeak.*

When Lee Seowol entered the main hall, the people from the Jin Family of Taiyuan were nowhere in sight. The wounded lying on the floor immediately caught her eye.

The Tiger of Mount Heng, Cheol Mubaek, and more than a dozen martial artists noticed her and called out.

“Ah, Seowol. You’ve come?”

“You’re here, Sect Leader!”

“We greet you, Sect Leader!”

“……?”

Was it just her imagination?

For people who were supposedly dying, they seemed strangely full of energy. After silently staring at them for a while, Lee Seowol realized what that energy meant.

“A final rally……”

Only then did she see the dark shadow of death lying heavily across their faces.

Just as she hurriedly turned away to hold back her tears—

*Bang!*

Lee Seowol staggered after striking her forehead against something solid. As she began to fall, a large, firm hand caught her shoulder.

“Oh, careful there. Are you all right?”

“Ah, yes.”

“Then we’re good.”

Jin Taekyung looked down at Lee Seowol and let out a short laugh.

* * *

*Some final rally.*

I barely held back a snort.

Cheol Mubaek and the other wounded were all recovering vigorously.

Of course, Jin Mukyung was no exception.

*What would they have done without me?*

To be precise, if not for the Quest rewards, there might have been funerals for half of them.

The thirty **Superior Wound Medicines** and thirty **Ten-Year He Shouwu** I had received as rewards each had remarkable effects on external and Internal Injury healing.

*I did consider saving them in case of an emergency……*

But I wasn’t heartless enough to ignore people dying right in front of me.

Of course, the sheer quantity had played a part too.

“Aren’t you coming in?”

“What?”

“If you’re not going in, I’ll go in first.”

I was about to walk past Lee Seowol, who was standing there in a daze, when I suddenly remembered something I had forgotten.

*Wait. Where did I put that?*

“Ah, here it is.”

I pretended to rummage around inside my robes and pulled a bamboo slip from my Inventory.

“Here. It’s from my hyung…… no, from the Lesser Family Head.”

Lee Seowol accepted the bamboo slip with a bewildered expression.

The System notification rang the instant she took it.

*Ding.*

> **System**
> - Invitation delivery complete.
> - Quest **Yesterday’s Enemy, Today’s Ally** completed!

Invitation delivery.

If I had to do that twice, someone was going to die.

[^1]: A playful variation on the Korean saying *seven parts luck, three parts skill*, replacing skill with *qi* and shifting the balance even further toward luck.
## Chapter artifact 121

# Chapter 121

It had been a fierce battle—fierce enough for corpses to pile up into mountains and blood to flow like rivers—yet most of the Mount Heng Sword Sect’s buildings remained standing, largely undamaged.

Like this pavilion, for instance.

I collapsed into a chair and leaned back.

“Ugh. I’m dying.”

A major battle like the one we had just fought always left exhaustion in its wake.

Leveling up could restore the fatigue in my body, but there was nothing I could do about mental exhaustion.

And after skirting the brink of death like I had today, it was even worse.

*That was seriously dangerous.*

Jopil. The Head Elder. Pung Yang.

I had never come out ahead after getting tangled up with Peak masters. More than once, I had wished I had about five lives.

“Squad Leader, you worked hard.”

“Yeah, yeah.”

“Oh, your shoulders are really tense.”

Hyuk Mujin approached with an ingratiating smile and began massaging my shoulders.

Wolhwa and Hyuk Mujin had been protecting Cheol Mubaek outside before joining the survivor search once things had more or less settled down.

“If I’d been there, I would’ve really laid into that bastard Pung Yang. You know what I mean, right?”

“Of course I do. You would’ve gotten yourself killed on the spot.”

“……”

“What? Come on, massage a little harder.”

Hyuk Mujin grumbled, but he put more strength into his hands and kneaded my shoulders.

“What about Jin Mukyung? I mean, my second brother?”

“We’ve already moved him elsewhere. The physicians said there’s no need to worry. They also said the other wounded are recovering quickly.”

“Really? That’s a relief.”

“Aren’t they quacks? I heard the Second Young Master and Great Hero Cheol Mubaek both suffered fairly serious Internal Injuries.”

“They were sent by the Lower District Sect. Let’s trust their skills.”

In truth, it wasn’t the physicians I trusted. It was the efficacy of the Items.

If not for the **Superior Wound Medicine**, which could heal most wounds within a few days, and the **Ten-Year He Shouwu**, which was exceptionally effective at treating Internal Injuries, some of them would already have crossed the River Jordan.

*I’ve given them the minimum emergency treatment. The physicians can take care of the rest.*

The Lower District Sect—or rather, Wolhwa—had moved quickly without any of us realizing it. Several days ago, when she sent one of her subordinates back from the shrine, she had apparently issued a mobilization order to a nearby branch.

The Lower District Sect’s support force arrived half a day after the battle ended and immediately began dealing with the aftermath.

*While everyone else was looking ahead, she was thinking about what came after.*

The Lower District Sect’s support force had been organized for rescue work, not combat.

They had brought not only physicians, but cooks and laborers as well. Their foresight and preparation were enough to make me whistle in admiration.

*She really isn’t an ordinary person.*

The Lower District Sect was an information organization found throughout the land, but it was also a Murim sect.

And Wolhwa, who had taken on the position of Branch Leader in a sect of that size while still in her mid-to-late twenties, was certainly no ordinary person.

*Come to think of it, Wolhwa isn’t even her real name.*

The name I had sensed through Qi Sense was Eun Sowol. As for why she had gone out of her way to hide her name from us, I supposed it was something like a code name in a spy movie.

One thing was certain: making an enemy of someone that capable would be exhausting.

*Don’t get too close. Keep a reasonable distance and stay within proper boundaries. Yes, that sounds about right.*

Fortunately, that wouldn’t be too difficult. Wolhwa had shown me inexplicable goodwill and curiosity from the very beginning.

Whether those were genuine feelings or simply the curiosity of a veteran information merchant was something I would have to watch a little longer to determine.

“Mujin-ah.”

“Should I massage harder?”

“No, not that. What do you think about Young Lady Wolhwa?”

“She’s pretty.”

“And?”

Hyuk Mujin thought hard before answering.

“She’s extremely pretty.”

“……”

“Massage my forearms instead of my shoulders.”

I was the idiot for asking that guy anything.

Hyuk Mujin looked wounded and was about to say something when light footsteps slowly approached and stopped in front of the door.

*Wolhwa?*

No. The qi I sensed outside the door was far weaker and smaller than Wolhwa’s.

After a brief silence, an unexpected guest spoke.

“Young Master Jin, may I come in?”

Her voice was clear and distinct.

It was Lee Seowol.

* * *

Once Hyuk Mujin left the pavilion, I was alone with Lee Seowol.

I gazed out the window at the sky slowly darkening and gave a pointless cough.

“Ahem. Ahem.”

Being alone with a woman at this hour—especially a stunning beauty—was a trial in itself.

To make matters worse, she was the Sect Leader of the Mount Heng Sword Sect, which I had been fighting like a sworn enemy only a short while ago.

They said new wine belonged in new wineskins, but she was the only daughter of Lee Cheonbaek, the man who had tried to bring down the Jin Family of Taiyuan, and she and I were already connected by a scandal.

*What the hell am I supposed to say?*

*May the deceased rest in peace?*

No. That would make the atmosphere far too heavy. It wasn’t enough that she had lost her family recently—she had also lost most of her subordinates in the battle against Pung Yang.

After agonizing over it, I finally opened my mouth.

“Have you eaten?”

“……”

“I know you’ve been through something difficult, but it’s even more important to keep your strength up at times like this, so……”

I stopped myself.

“Sorry.”

*Damn it. I should’ve just kept my mouth shut.*

As I was regretting my words from the bottom of my heart, Lee Seowol rose from her seat and bowed deeply to me.

“Lee Seowol of the Mount Heng Sword Sect pays her respects to her benefactor.”

It happened before I had a chance to stop her.

Flustered, I hurriedly helped her back to her feet.

*Benefactor?*

It was accurate, but hearing it made me cringe.

“Oh, come on. What are you doing? You don’t have to call me your benefactor.”

“No. A person ought to receive kindness and know how to be grateful for it. Please do not make me feel ashamed, Benefactor.”

Her tone was so resolute that I couldn’t stop her anymore.

*She’s not wrong.*

If not for Jin Mukyung and me, the Mount Heng Sword Sect would have shut its doors today. A deep bow wasn’t enough. They could have erected statues of us and it still wouldn’t have been sufficient.

Maybe they could designate today as the day the Sleeping Dragon of Shanxi came to visit and make it an annual holiday for the Mount Heng Sword Sect—

*That might be taking things too far.*

“Now, calm down and sit.”

“I will follow my benefactor’s instructions.”

“Could you not call me that?”

“Yes, Benefactor.”

*This is driving me crazy.*

Only after Lee Seowol answered with a calm expression and sat down was I finally able to hear why she had come to see me.

“I came to give you my answer regarding the letter.”

“The letter? Oh.”

She was talking about the invitation.

The polite invitation to have a meal at the Jin Family of Taiyuan on New Year’s Day, which was fast approaching—a summons disguised as a dinner invitation.

Now that the Jin Family of Taiyuan had Shanxi Murim firmly in its grasp, it was obvious that things would not go well for any sect that refused the invitation.

The Mount Heng Sword Sect, which had only barely escaped annihilation, was no exception.

“So what’s your answer?”

“We will gladly accept your sect’s proposal.”

It was the answer I had expected.

But Lee Seowol didn’t stop there. She continued speaking.

“Additionally, as an apology for what happened, I will transfer all the rights held by our sect to the Jin Family of Taiyuan.”

“Rights?”

“Yes. All rights to the territory currently occupied by our sect.”

In other words, she was saying that she would hand over all of northern Shanxi to the Jin Family of Taiyuan.

*She’s going this far?*

The fact that the Mount Heng Sword Sect had bowed its head to the Jin Family of Taiyuan was already a given. Jin Wikyung would demand a great deal in compensation, but even he couldn’t completely swallow the sect whole.

Wolhwa had said something similar during our previous conversation.

*And now she’s serving it up to us without even being asked.*

After calling me her benefactor over and over, it seemed she hadn’t just been paying lip service.

Yes. Gratitude shouldn’t end with words. Hm.

“Thank you. My eldest brother will be pleased.”

“There’s more.”

*What? She isn’t finished yet?*

Lee Seowol took three books from inside her robes and held them out to me.

I slowly read the titles written on their covers.

“Blood Wolf Sword Technique, Blood Wolf Footwork. And……”

“Shura Annihilating Fist. The sword technique and footwork technique were created by my father himself. The Shura Annihilating Fist is Uncle Cheol’s secret ultimate technique. Every one of them is an outstanding Peak martial art.”

“Peak martial arts……”

I swallowed hard.

One of the things I had learned painfully in the Murim was the importance of martial arts. Even I was barely able to make up for my deficiencies by relying on the System. For ordinary martial artists, it went without saying.

To martial artists, an excellent Peak martial art was a priceless treasure.

*These are worth more than the rights to northern Shanxi.*

If the rights to northern Shanxi were the branches of a tree, then the three martial arts manuals lying before me were its roots.

Lee Seowol had placed her father’s legacy—the most valuable things possessed by the Mount Heng Sword Sect—on the scale.

“Is this a gift too?”

“No. This is a transaction.”

*I knew it.*

A transaction.

If it was Jin Wikyung, he would accept the deal by any means necessary. Three Peak martial arts were at stake, after all.

*What on earth is she going to demand?*

Wealth? A guarantee of safety? Or something else entirely?

Lee Seowol—or rather, the Mount Heng Sword Sect—was in a situation so desperate that it had nearly become hopeless. Even if they were offering their martial arts at a bargain price, whatever they wanted in return was certain to be a difficult demand.

I cautiously backed away.

“I am curious what kind of transaction you have in mind, but I don’t know if you’re aware of this—I don’t have that kind of authority.”

Lee Seowol gazed steadily at me with eyes as clear as a lake.

“Is that so?”

“Yes. I don’t have a particular position, either. I think it would be best for you to discuss this separately with my eldest brother later.”

“My thoughts differ from yours, Benefactor.”

“Excuse me?”

“This is a transaction you are fully capable of deciding. Of course, there would need to be many discussions.”

“A transaction worth trading three Peak martial arts for…… Then what would our side have to give?”

“A person.”

“A person?”

For an instant, a smile flickered across Lee Seowol’s lips.

It was the second time I had seen her smile, and this time, I knew I hadn’t imagined it.

“Please marry me.”

* * *

“Well, I’ll be going.”

Hyuk Mujin, who had been pacing around the pavilion’s front courtyard, turned at the sound of the woman’s voice behind him.

A beauty who made one’s chest tickle just by looking at her was descending the pavilion steps.

*Good heavens. She’s breathtaking.*

Though she was dozens of paces away, it almost seemed as if the cold midwinter wind carried the scent of flowers with it.

*Our squad leader sure is lucky.*

He had a handsome face, was the youngest Young Master of the Jin Family of Taiyuan—the universally acknowledged First Family of Shanxi—and possessed excellent martial arts.

When he was with Wolhwa, the words *a celestial beauty and a handsome man* fit them perfectly.

And now the Sect Leader of the Mount Heng Sword Sect had been added to the list.

Hyuk Mujin let out a deep sigh as he watched Lee Seowol’s back disappear into the distance.

*I loved you for a moment, Young Lady Lee.*

When Hyuk Mujin returned to the pavilion, he found Jin Taekyung sitting there half out of his mind.

“Squad Leader, what’s wrong?”

“……”

“Squad Leader. Please come to your senses!”

Only after Hyuk Mujin grabbed him by the shoulders and shook him did the unfocused eyes finally clear.

Hyuk Mujin asked with a worried expression.

“Did something happen? Why are you suddenly acting like this?”

*Gulp.*

Jin Taekyung swallowed hard and barely managed to open his mouth.

“Mujin.”

“Yes.”

“Do you know how old Lee Seowol is?”

“What do you mean, ‘Lee Seowol’? You should call her Sect Leader or Young Lady.”

“If you don’t want me to start calling you the late Hyuk Mujin, shut up and answer me.”

“……”

Hyuk Mujin thought for a moment.

“How old was she again? I think she was about the age when people started getting married.”

He suddenly slapped his forehead.

“Oh, I remember.”

“H-How old is she?”

“Seventeen.”

Jin Taekyung’s mouth fell open.

“Fuck, she was still a high schooler?”
## Chapter artifact 122

# Chapter 122

There were two things that mattered when conveying information: speed and accuracy.

To that end, the Lower District Sect, a sect that dealt in information, had built an extensive information network at every branch.

Wolhwa had the authority to issue mobilization orders to the more than thirty branches established throughout Shanxi Province.

“How’s it going? Are you finished?”

A clean-cut middle-aged man answered her question. He was the Jeongyang Branch Leader of the Lower District Sect.

“We separated and moved all the corpses. There were no more survivors from the Mount Heng Sword Sect, but some of the mounted bandits were still breathing.”

“How many?”

“Exactly forty-seven.”

“That’s quite a lot who survived. How many of them can we save?”

“With the medicine we currently have, thirty at most.”

“We don’t need to save every last one.”

At Wolhwa’s words, the Jeongyang Branch Leader lowered his head.

“I’ll take care of it.”

That decided the surviving mounted bandits’ fates.

Those with serious injuries would rejoin the mountain-high pile of their comrades, while those with minor injuries might live a little longer.

Of course, the moment their treatment was finished, they would be sold as slaves to the mines or fighting pits.

“Next. Honju Branch Leader?”

“No problems on our end, either.”

The Honju Branch Leader was a hulking man whose face was covered in sword scars. He scratched at his stiff, wirelike beard and continued.

“Truth is, we didn’t even need to step in. They must’ve heard Pung Yang was dead and the Red Wind Band had been wrecked, because they didn’t come anywhere near the area.”

“For now, that’s enough. Pick the swiftest and most loose-lipped people you have and spread the rumor. They’ll run away on their own.”

Although Pung Yang and his subordinates had been dealt with, a considerable number of mounted bandits were still prowling around the area like wolves.

They were waiting for an opportunity to sink their teeth into the easy prey that was the Mount Heng Sword Sect.

“The Sleeping Dragon of Shanxi and the Heaven Shaking Sword beat Pung Yang to death with a single blow. If the others hear that, they’ll be scared out of their minds.”

“It’s not exactly true, but… Add enough seasoning. We can’t bleed for someone else’s fight, can we?”

The truth of the rumor was unimportant. All that mattered was that people learned the two brothers of the Jin Family of Taiyuan had rescued the Mount Heng Sword Sect from Pung Yang and the Red Wind Band.

“Besides, the Jin Family of Taiyuan will make a move within a few days. Unless they’re complete idiots, they’ll return to the plateau if they want to live.”

The fact that the great tiger known as the Jin Family of Taiyuan stood behind the Mount Heng Sword Sect would soon spread far and wide. Wouldn’t one roar from the mountain king be enough to send those bandits running?

“Five days at most. Let’s put in some effort until then.”

The two Branch Leaders nodded.

“What effort? It’s the Chief Branch Leader’s order. Of course we have to follow it.”

“I like it. Maybe it’s because the plateau is right next door, but there’s something fun about riding across all this open land.”

“Then that’s a relief.”

Wolhwa gave a short laugh and drew on her long-stemmed tobacco pipe.

“Um, by the way…”

“Yes?”

The Honju Branch Leader, considered the most aggressive and martial-arts-obsessed of her subordinates, had a bright gleam in his eyes.

“I heard from the wounded that bastard Pung Yang took down the Tiger of Mount Heng and the Heaven Shaking Sword all by himself. Is that true?”

“It is. Though I didn’t see it myself.”

“Wow. That’s impressive.”

“It is impressive. The fact that he grew so strong so quickly reeks of something fishy, though.”

The Peak realm was a domain of enlightenment. From that point onward, a martial artist had to see through the principles of martial arts rather than merely train the body in order to advance to a higher realm.

But Pung Yang had been defeated by Cheol Mubaek, the Tiger of Mount Heng, only a short while ago. No matter how much enlightenment supported him, he had become far too strong in far too little time.

Wolhwa, who still knew nothing of the Temporary Strength Pill, focused on that point.

“He definitely used some kind of trick… I’ll have to look into it more closely.”

The quick-witted Jeongyang Branch Leader offered a silent bow, while the Honju Branch Leader vigorously scratched the back of his head.

“Of course, Pung Yang, that mounted-bandit bastard, is impressive too. But I was talking about someone else.”

“Who? Ah.”

“The Sleeping Dragon of Shanxi. Isn’t he incredible? According to what our sect has determined, his martial arts are still only First Rate, but he keeps defying our expectations.”

Information had to be based on objective facts. As members of the Lower District Sect, they coolly judged how information could be used from a third-party perspective, then applied it to people and situations.

In that regard, Jin Taekyung was a headache. Every prediction concerning him had been wrong.

“But the strange thing is, I’m starting to look forward to it more and more.”

“Look forward to what?”

“Wondering how he’ll defy our expectations next time. That kind of anticipation.”

The Honju Branch Leader had been grinning broadly, but he stopped smiling when he saw Wolhwa’s impassive expression.

“I’m sorry. I was running my mouth.”

“At least you know it. Go outside and handle your work.”

After driving the two Branch Leaders out, Wolhwa put her pipe back between her lips.

A tiny voice slipped from her barely moving lips along with the smoke.

“Jin Taekyung. Jin Taekyung.”

She suddenly remembered a conversation she had once shared with her Master.



*There are people like that. People who always defy prediction, people who cannot be judged through information.*

*Then what should I do?*

*Don’t judge them. Just watch them until you can reach your own conclusion about them.*

*What if I still can’t reach a conclusion after going that far?*

*Unpredictable. If there is such a person, wouldn’t they be the sort of talent capable of moving the world someday?*



*A talent capable of moving the world…*

Wolhwa tapped the ash from her pipe and left the pavilion.

Night had fallen thick and dark. Guided by blazing torches that served as landmarks, she walked until she stopped in front of the pavilion where Jin Taekyung was staying.

“What are you doing out here?”

Hyuk Mujin, who had been sitting miserably in a crouch before the pavilion, brightened when he saw Wolhwa.

“Oh, you’re here?”

“I’ve mostly finished dealing with things, so I stopped by for a moment. Young Master Jin is inside, right?”

In truth, there was no need to ask. Bright light was spilling out through the pavilion.

But Hyuk Mujin shook his head with a grim expression.

“He isn’t inside?”

“No, he is. It’s just that…”

Hyuk Mujin let out a deep sigh before continuing.

“His condition isn’t very good. He’s been muttering things that make no sense for a while now. I get goose bumps just looking at him.”

“Things that make no sense?”

“Yes. Do you happen to know what ‘school lunch’ means?”[^1]

“School lunch?”

Wolhwa tilted her head. She had read a considerable number of books, but it was the first time she had ever heard the word used that way.

“I don’t think so. It sounds unfamiliar.”

“Right? I wondered if I was just too ignorant to know.”

“And then?”

“You know what our Squad Leader is like. He kept saying ‘school lunch, school lunch,’ so I asked him what it meant. Then I got kicked out.”

Judging by the way Hyuk Mujin miserably rubbed his forehead, it seemed he had not been politely shown the door.

*What happened?*

Wolhwa was just about to knock when an eerie voice seeped through the gap in the door.

“School lunch, high schooler, clank, clank…”

A chill ran over Wolhwa, and she took a step backward without realizing it.

“D-Did you hear that?”

“He’s been like that for a while.”

Even as the incomprehensible muttering continued, she slowly backed away.

“I-I’ll come another time.”

She realized it once again.

The man named Jin Taekyung was still utterly unpredictable.



* * *



Two days flew by in the blink of an eye. Lee Seowol did not come back after that night, and I didn’t bother leaving the pavilion, either.

Even while spending most of my time learning to control the newly acquired Scorching Yang Qi, her final words kept coming back to me.



*Marriage is one of life’s great human obligations, so take your time thinking it over.*



I had been so flustered at the time that I could only open and close my mouth.

Who would have thought I’d receive a proposal from a woman first—and from a girl who looked so much younger than me, at that?

Although it was a cold political marriage proposal—cold enough that calling it a transaction wasn’t an exaggeration—it was still a proposal.

But there was an even greater shock waiting for me.

*Seventeen years old? Is this for real?*

A first-year high school student was right in the prime school-lunch-eating years.

She was two years younger than my late-born little sister, Hayeon, and a full ten years younger than me.

*That’s the Murim for you…*

Getting married in middle school and becoming a parent in high school wouldn’t even be strange in this world. In fact, the three brothers of the Jin Family of Taiyuan looked like the oddballs for remaining unmarried at our age.

No, wait a second.

“What are you staring at?”

Jin Mukyung noticed my gaze and asked irritably. He had suffered considerable injuries at Pung Yang’s hands, but he had now recovered enough to move around on his own.

*Come to think of it…*

I had never heard whether Jin Mukyung was married.

I opened my mouth, half expecting the worst.

“Just asking in case.”

“What?”

“Are you married?”

Pffft!

Jin Mukyung spat tea into my face and hurriedly shouted.

“What kind of nonsense are you talking about?”

“If you’re not, then you’re not. Why are you so flustered?”

After receiving that unexpected facial wash, I wiped my face with my sleeve and continued asking questions.

“Why aren’t you?”

Jin Mukyung looked flustered for a moment, then answered readily.

“I’m too busy training in martial arts. Women are a luxury to me.”

“You make it sound downright frugal.”

“Don’t lump me in with a lecherous idler like you. That’s an insult to me.”

“…”

Lecherous, my ass. I had spent twenty-seven years as a lifelong single.

If dating was a luxury, then I was the very definition of a miser. The only slight difference was that while Jaringobi ate rice while staring at a strip of dried fish, I had a USB drive.[^2]

“What’s with that expression? You look incredibly sad.”

“Maybe it’s regret over the life I’ve lived.”

“At last, you’re becoming a human being.”

He seemed to have a different interpretation of my past life, but fine. He could interpret it however he wanted.

“But why did you suddenly ask about marriage? It’s something you already know perfectly well.”

“Oh, because the Sect Leader of the Mount Heng Sword Sect asked me to marry her.”

Pffft!

“…For fuck’s sake. Stop spitting.”

While I wiped away the second mouthful of tea, Jin Mukyung regained his composure and spoke.

“The Sect Leader of the Mount Heng Sword Sect?”

“Yeah. She said it two days ago.”

“Why on earth would she marry someone like you… Ah, of course. It must be a political marriage.”

“…”

He wasn’t wrong, but it was still pretty damn irritating. At this point, wasn’t I prime husband material both in the Murim and in the real world?

“So, are you thinking of doing it?”

“Of course not. How could I marry a girl so much younger than me?”

“You’re barely twenty, and you say things like that.”

*My body is twenty, but my mind is twenty-seven, you bastard.*

Besides, I had decided on my answer to Lee Seowol’s proposal a long time ago.

You can’t set up two households when there’s someone you love. There was only one person in my heart right now.

*What could Song-i be doing right now?*

Just imagining it made me happy. I tilted my teacup with a blissful smile, and Jin Mukyung stared at me with a bizarre expression.

“What a disgusting look.”

“Anyway, I’m turning down the marriage for various reasons.”

“You made the right decision. At the very least, a political marriage has to offer us something in return. If you marry someone you have no feelings for and gain nothing from it, there’s no reason to enter into a political marriage.”

I had thought he was a fool who knew nothing but martial arts, but every now and then, he turned into a surprisingly sharp realist.

“And no matter what she offers, it’s out of the question as long as our eldest brother is around. He isn’t the sort of person who’d arrange a political marriage for you.”

“They did make a pretty substantial offer, though.”

“Hm. What did she say they would give you?”

Jin Mukyung tilted his teacup with an uninterested expression.

“The Blood Wolf Sword Technique, the Blood Wolf Footwork, and the Shura Annihilating Fist.”

Pffft!

“…Ah, fuck.”

This time, I didn’t even have time to wipe it away. Jin Mukyung grabbed me by the collar and shook me hard.

“Marry her right now!”

[^1]: “School lunch” is Korean slang for a school-age kid, while “clank, clank” evokes handcuffs or prison bars—the joke is that sexual interest in a high schooler could land someone in jail.
[^2]: Jaringobi is a traditional Korean image of a miser who stares at dried fish while eating rice rather than eat the fish.
## Chapter artifact 123

# Chapter 123

A middle-aged man lay in bed with bandages wrapped around his entire body.

His brow was deeply furrowed, as if something was bothering him, and his body kept fidgeting without a moment's rest.

“Ugh.”

The moment he let out a groan, a sharp rebuke came flying.

“Please don’t move so much.”

“That’s not it…”

“Uncle Cheol, didn’t you hear what the physician said?”

Here we go again. Cheol Mubaek, the Tiger of Mount Heng, stared blankly at the ceiling. Lee Seowol pulled a thick cotton blanket up to his chest and continued.

“You need to recover as quickly as possible. I know you’re feeling restless, but please stay in bed. At least get some more sleep.”

“I’ve already slept enough.”

“You only slept for two hours.”

“Only? Two hours is plenty.”

“You’ll just make yourself worse.”

“I’ve lived like this for more than thirty years. I’ll be fine.”

“That’s only because you’ve never been this badly injured before.”

“...Urgh.”

Cheol Mubaek fell silent at Seowol’s pointed remark.

She was right. He had never suffered injuries this severe since learning the Shura Annihilating Fist. Broken limbs and serious internal injuries. According to the physician, they were severe enough that he would need at least four months of recuperation.

“I wasn’t this badly hurt even when I met your father.”

Seowol reacted to his complaint.

“My father?”

“Yes. That friend of mine, Cheonbaek.”

“What happened between the two of you?”

“I never told you?”

“I only knew that the two of you became friends because you hit it off.”

“That’s true. But at first, we fought with our lives on the line.”

“You fought?”

Cheol Mubaek smiled faintly.

“What else would two martial artists do when they met? We were both young, and our competitive pride was strong. The answer was obvious.”

Cheol Mubaek looked out the window. More than thirty years ago, somewhere along those towering mountain ridges, the two men had met for the first time—and fought.

“He said he’d searched the mountain range for three months, combing through it inch by inch to find me. He looked like a beggar, but his aura was anything but ordinary.”

Masters recognized masters. Cheol Mubaek had secluded himself in a remote valley that no one visited, training in martial arts alone. Lee Cheonbaek had perfected his own martial arts through countless battles.

It had been the first meeting between two Peak masters.

“He told me to become his subordinate. He said he was going to establish a sect at the foot of the mountains and wanted me to lay its foundation with him.”

“That sounds like Father. So what happened?”

“What else needed to be said? We fought. And we fought viciously.”

Seowol snorted softly.

“I see.”

“Aren’t you curious what happened?”

“Do I need to hear it? I can tell just from the fact that you’ve remained unaffiliated all this time, Uncle Cheol. Isn’t this one of those embarrassing stories men tell about becoming friends after being moved by each other’s martial arts?”

“Ha-ha-ha! That’s right! The fight was decided in exactly five hundred exchanges… ugh.”

Cheol Mubaek had been laughing loudly when a sudden stab of pain made him flinch. Seowol sighed.

“I think I’m making your condition worse by being here… It might be better if I left.”

“Seowol. Don’t you feel sorry for an uncle who’s growing old all alone?”

“If you’re interested, just tell me anytime. I’ll even find someone to set you up with.”

“Forget it. What would I do at my age?”

Although he had said the words himself, they left a bitter taste in his mouth. Cheol Mubaek muttered inwardly.

*Yes. Somehow, I’ve grown this old.*

He did not even know exactly how many years had passed since the day he lost his family.

His deep internal energy and highly trained body made him look younger than his true age, but his mind had been growing old for a long time.

*My one and only friend is gone, and the martial arts I spent my entire life honing have been broken so thoroughly. Heh.*

Only now could he finally admit it. The Tiger of Mount Heng had grown old.

But Cheol Mubaek still had something left to protect.

“Seowol.”

Seowol answered him warmly.

“Yes, Uncle?”

“I want you to be happy.”

“I know.”

“It’s not too late. Marry the person you love. With the Jin Family of Taiyuan’s help, you could build a safe and happy home anywhere in Shanxi.”

“What I want isn’t a family. It’s the Mount Heng Sword Sect.”

A trace of sorrow crossed Cheol Mubaek’s eyes. He had watched Seowol since she was a baby. Rebuilding and reviving a fallen sect was far too heavy a burden for a girl who was not even twenty.

“You may regret the choice you’re making now.”

“But no matter what choice I make, you’ll believe in me, won’t you?”

“If I didn’t, I wouldn’t have given you the martial arts manual for the Shura Annihilating Fist.”

Seowol grasped Cheol Mubaek’s wrinkled hand.

She, too, was the daughter of a martial household. She understood what a momentous decision the old martial artist before her had made.

“Thank you, Uncle.”

At the moisture in her voice, Cheol Mubaek waved a hand.

“I’m old. I was having trouble taking on a Disciple at this point in my life anyway. This was simply a good opportunity.”

The Shura Annihilating Fist followed the principles of a single successor and transmission only to the worthy. Its intent was to find a successor of upright conduct and good character and pass the martial lineage on to them.

Yet Cheol Mubaek, the ninth-generation successor, had broken that principle and handed the martial arts manual to Seowol. Although she had not received direct instruction, he had still broken the tradition passed down through the sect’s generations.

But Cheol Mubaek had his own reasons.

*If she has the Heaven Shaking Sword and the Sleeping Dragon of Shanxi, they’ll be able to protect Seowol.*

If Seowol had decided to enter a political marriage, those two were the best options.

Their talent for martial arts went without saying, and they also possessed the chivalrous spirit to risk their lives standing against injustice.

*Still, I’ll have to watch and see what they’re really like…*

If everything went well, this could satisfy both the purpose of a political marriage and the traditions of a single successor and transmission only to the worthy.

“So, speaking of that…”

Cheol Mubaek continued in a suggestive tone.

“Which one did you choose?”

Seowol tilted her head as if she had no idea what he meant.

“My goodness. Which one?”

“Don’t play dumb. Is it the Heaven Shaking Sword? Or the Sleeping Dragon of Shanxi?”

“I’m not sure.”

“They’re both more or less the same sort, but… Wouldn’t the Heaven Shaking Sword be better?”

“You don’t like the Sleeping Dragon of Shanxi?”

“It’s not that I dislike him…”

Cheol Mubaek frowned. Even he, who spent most of the year deep in the mountains, had heard the rumors about the Jin Family of Taiyuan’s notorious delinquent.

“Even if he has truly reformed, old habits die hard. I’m worried he might break your heart someday.”

“What about the Heaven Shaking Sword?”

Cheol Mubaek’s crumpled expression smoothed out.

“They say a younger brother can’t measure up to his older brother. I spoke with him briefly yesterday, and he seems like a fine person. His talent for martial arts is outstanding.”

“I heard he knows nothing but martial arts.”

“Hey! He’s far better than chasing women. His speech and conduct are both dignified and weighty. That’s how a man ought to be, yes. Absolutely.”

Cheol Mubaek smiled contentedly.

* * *

Jin Mukyung grabbed me by the collar and shook me violently, his eyes half rolled back in his head.

“Marry her right now!”

“Cough, cough!”

Tea had gone up my nose and made me choke, and now Mukyung was shaking me by the collar without pause. I couldn’t think straight.

“Let go! Are you going to let go?”

“The Shura Annihilating Fist! The Blood Wolf Sword Technique! The Blood Wolf Footwork!”

“Fine, but let go first!”

“You stupid bastard! Do you even know what kind of martial art the Shura Annihilating Fist is?”

“Let go and then we’ll talk!”

“A single successor! Only the worthy may inherit it!”

“Enough, you crazy bastard!”

A short while later, by the time I finally pried Mukyung’s hand away, the inside of the pavilion looked as though a storm had passed through it.

“Huff… huff…”

I caught my breath and looked around.

The table had collapsed, the chairs were smashed to pieces, and fragments of broken teaware rolled across the floor.

Mukyung calmly straightened his clothes and spoke.

“Hmm. I’ve calmed down.”

“…”

This guy was even crazier than I’d thought.

I scrubbed my face with the sleeve that was relatively dry.

“Is the Shura Annihilating Fist some kind of greatest martial art in the world? Why are you so obsessed with it?”

“It was one of the ten greatest fist techniques in the world. No—it was.”

“It was?”

“It was two hundred years ago. Even in the library of Heaven’s Gate Temple, which contains thousands upon thousands of books, the only records of this martial art are written accounts. And yet the Great Hero Tiger of Mount Heng was the current successor to the Shura Annihilating Fist!”

His cheeks flushed with excitement at the thought.

I snorted the tea out of my nose and asked, “So?”

“What do you mean, ‘so’?”

Mukyung stared at me as if he couldn’t believe what he was hearing.

“I’m talking about the Shura Annihilating Fist! A Peak martial art whose lineage was believed to have died out long ago!”

“And it was one of the ten greatest fist techniques in the world two hundred years ago?”

“That’s exactly it!”

“Wait a second.”

I picked up a thick wooden stick rolling across the floor. Until five minutes ago, it had been called one of the table legs.

“Do you know what this is?”

“A club?”

“You know your stuff.”

“What does that have to do with anything?”

“Wouldn’t this have been one of the ten greatest weapons in the world around two thousand years ago?”

He wasn’t so stupid that he couldn’t understand what I was saying.

Mukyung’s eyes widened.

“How dare you compare the Shura Annihilating Fist to something like that.”

“Then what’s the difference?”

“That…”

“Of course, it’s far more valuable than a wooden club like this. But is it still the same now?”

In the past, humans fought with stones and clubs. But once bronze and iron appeared, those weapons were pushed aside by the march of the ages.

The Shura Annihilating Fist was no different.

“Of course, it’s still an outstanding Peak martial art that everyone would want.”

Cheol Mubaek himself had proven that. He had become a renowned Peak master in Shanxi Province through the Shura Annihilating Fist.

“But it isn’t still one of the ten greatest fist techniques in the world, is it?”

Just as stone and clubs had been replaced by steel, martial arts advanced as well.

I had no idea what the ten greatest fist techniques in the world were now, but Mukyung’s expression proved that I wasn’t wrong.

“To put it bluntly, if the Shura Annihilating Fist were really that powerful, Pung Yang wouldn’t have defeated him. And this is the most important part…”

I tossed the table leg carelessly into a corner and drove home the final point.

“I have no intention of getting married.”

“...!”

“If the person involved says he won’t do it, what can you do? Right?”

“Well… That’s true.”

Mukyung let out one deep sigh after another. I’d been prepared to fight him if he kept insisting, but he seemed surprisingly willing to accept it.

His wistful gaze still suggested that he couldn’t stop thinking about the martial arts manual for the Shura Annihilating Fist, though.

*This guy is a martial arts nut too.*

Then again, he had gone to Heaven’s Gate Temple because he wanted to learn more martial arts.

And now he had discovered a martial art from several hundred years ago that existed only in the records of that very same temple. Of course he couldn’t contain his excitement.

“Hoo…”

Mukyung let out a sigh deep enough to make the earth cave in and muttered,

“What a shame. What a shame.”

“It’s not that big a deal. If fate brings it around, we can get it another time.”

“You idiot. Do you think Peak martial arts just drop out of the sky?”

“Really? Mine did.”

“Even at Heaven’s Gate Temple, where all the martial arts in the world are gathered, Peak martial arts are strictly controlled… What did you say?”

“I said mine fell out of the sky.”

I pulled an old book from inside my clothes. The four characters written on its cover had been blurred by the ravages of time, but they were still clear enough to read.

**Flame Divine Palm.**

A tiger leaves its hide when it dies, and Jopil left behind Supreme Peak martial arts.

“Flame, Flame, Fla…”

Today was probably the most astonishing day of Jin Mukyung’s entire life.

I grinned at him as he stared wide-eyed, looking back and forth between me and the martial arts manual.

“From now on, call me hyung.”
## Chapter artifact 124

# Chapter 124

I was only human, so I couldn’t help wavering when Lee Seowol presented me with three martial arts manuals two nights ago.

They were Supreme Peak martial arts, no less. Now that I had mastered the Jin Family’s Spear Technique and Jin Family’s Manoeuvre Technique, I had already been feeling the need to learn something new. And then, right in front of me, someone had dangled such a tempting offer.

*This won’t do.*

My fight with Pung Yang had been brutal. If I hadn’t had the Unnamed Sword I’d obtained from Jopil, I wouldn’t have survived even if I’d had two lives.

It was time to learn more martial arts and enter a new realm.

*Peak master.*

The Blood Wolf Sword Technique, Blood Wolf Footwork, and Shura Annihilating Fist were all proven Peak martial arts. They were sturdy hammers, strong enough to break through that supposedly insurmountable wall of the Peak realm. But…

*If those are hammers, then this is an excavator.*

I gazed proudly at the old book in my hand.

This one martial arts manual was the reason I could reject Lee Seowol’s proposal without much regret.

“Fl, fl, fl, fl…”

After buffering for quite some time, Jin Mukyung finally managed to spit out a single word.

“Flame Divine Palm!”

“Oh, you know it? Correct.”

Jin Mukyung knew even the ten greatest fist techniques in the world from two hundred years ago, so perhaps it was only natural that he knew about the Flame Divine Palm. This martial art was even more incredible than those.

*Check item.*

*Ding.*



> **System**
>
> **Item Window**
>
> **Flame Divine Palm**
>
> **Type:** Martial arts manual  
> **Grade:** Supreme Peak  
> **Restriction:** Owner of Scorching Yang Qi  
> **Description:** One of the secret techniques of the Fire Gate Clan. A martial art based on powerful fire energy.  
> **Effect:** Acquisition of Flame Divine Palm.



Jin Mukyung asked with an expression of utter disbelief.

“How did you get this…?”

“Some generous soul gave it to me before he left.”

“He gave it to you?”

“Yeah.”

He gave it to me and then flew away to heaven.

The Unnamed Sword, made of Ten-Thousand-Year Cold Iron capable of destroying even Body-Protecting Qi. The Blazing Flame Divine Pill, which could grant me thirty years of Scorching Yang Qi.

And finally, the Flame Divine Palm, a Supreme Peak martial art.

Thinking of Jopil, who had given me so much before leaving this world, I gazed at the blue sky beyond the window.

*I hope you’re doing well.*

That was when Jin Mukyung abruptly cut in.

“Stop spouting nonsense and tell me the truth. How did a secret technique of the Fire Gate Clan end up in your hands?”

“I told you. Someone gave it to me before he left.”

“It seems you’re under some kind of misunderstanding…”

Jin Mukyung continued with a serious expression.

“This isn’t a situation you can gloss over with a joke.”

“Why not?”

“Because you could end up branded a thief who stole another sect’s martial arts. If things go badly, the Jin Family could be condemned by the entire Murim.”

That was a problem I hadn’t considered.

Martial arts were the foundation and history of a sect. The Flame Divine Palm was not only a Supreme Peak martial art but also a secret technique of the Fire Gate Clan. That went without saying.

“Damn it.”

“I’ll ask you one more time. Where and how did you acquire the manual for the Flame Divine Palm?”

I let out a deep sigh before answering.

“From Jopil.”

“Jopil? The One Question, One Kill Jopil I know?”

“That’s right. I defeated Jopil and obtained it as spoils.”

“Do you know how that bastard came to possess the Flame Divine Palm manual?”

“Not really…”

After thinking carefully, I remembered what Jopil had said at the time.

“He claimed he was the nineteenth-generation successor of the Flame Divine Palm.”

“How could someone like Jopil be… Are you sure you didn’t hear him wrong?”

“No, I’m sure. He didn’t look like he was lying, either.”

At the time, Jopil had been drawing on his innate qi, and he had already been dying rapidly. Words spoken by someone standing on the brink of death were usually close to the truth.

*Of course, I have to consider the possibility that Jopil was lying.*

Jin Mukyung had been lost in thought. Then he spoke with an expression of confusion.

“If he was a successor of the Flame Divine Palm, how did he lose to someone like you?”

“…”

Well, that pissed me off, but he had a point.

It was suspicious enough that Jopil had been living as a wandering martial artist despite having learned a Supreme Peak martial art.

*Now that I think about it, he couldn’t even use Sword Energy properly.*

These days, every martial artist I met came with Sword Energy as standard and Body-Protecting Qi as an optional extra. One Question, One Kill Jopil had been among the weakest Peak masters I had fought so far.

“Is the Flame Divine Palm weaker than I thought?”

“What? The Flame Divine Palm is weak?”

Jin Mukyung looked at me as if I were the craziest person he had ever seen.

“You lunatic. You’re probably the only person in the world who would call the Fire King’s signature martial art weak.”

“Who’s the Fire King?”

“I’m not in the mood for jokes.”

“Neither am I.”

“Stop it. You’re not funny.”

“Okay. So who’s the Fire King?”

This silence lasted a little longer. Jin Mukyung opened and closed his mouth like a goldfish before letting out a deep sigh.

“Count your fingers and toes. How many are there altogether?”

“Twenty.”

“Right. Even if you turned the entire world upside down and shook it out, the Fire King would still be among the twenty greatest masters in it.”

“…Whoa.”

“One God, Three Saints, Ten Kings. You’ve never heard of them? You really don’t know?”

He looked ready to twist my neck if I said I had never heard of any of them.

Under Jin Mukyung’s ringed eyes, I cautiously opened my mouth.

“I’ve heard of the Three Saints, at least…”

“That’s something.”

I meant Samsung,[^1] not the Three Saints, but whatever.

[^1]: The Korean name “Samsung” is pronounced *Samseong*, the same as the Korean term rendered here as “Three Saints.”

That wasn’t important right now.

“Then if the Fire King finds out that I have the Flame Divine Palm…”

“Something you won’t particularly want to imagine will happen.”

Damn it. A Supreme Peak master ranked among the twenty greatest experts in the entire world. If the Fire King learned about this and came looking for me, the entire Jin Family of Taiyuan could attack him together and still lose.

*After everything it took to obtain this martial art…*

My gut twisted at the thought that I might have to hand it over without even learning it.

At that moment, Jin Mukyung, who had been gazing sorrowfully at the Flame Divine Palm manual just as I was, added one more thing.

“If the Fire King is still alive.”

“What?”

“The last time the Fire King appeared was forty years ago.”

“Forty years ago?”

“When he first appeared in the Murim, the Fire King was already an old man. If not for the Great Faction War, he might have lived his entire life as a secluded eccentric.”

Jin Mukyung continued.

“The Demonic Cult’s morale soared after it defeated the Nangong Family and occupied Anhui Province. They carried out countless acts of looting, murder, and arson, and apparently, setting fire to Mount Jiuhua was what finally provoked the Fire King.”

“And then?”

“A thousand people died over four days and nights, and the old man who had been living in seclusion deep within Mount Jiuhua gained the name Fire King.”

“…A thousand people?”

“Yes. The Demonic Cult suffered such heavy losses at Mount Jiuhua that it could not hold out for long and had to withdraw from Anhui Province.”

A thousand people, huh…

After careful consideration, I opened my mouth.

“Let’s give it back.”

I wanted to live a long life. I didn’t want an event involving some insane old man who had killed a thousand people by himself added to my life.

“We should leave right away. Anhui Province? Do people still say he lives there?”

“No one knows. Perhaps that still hadn’t been enough to quell the Fire King’s anger. He spent an entire year crushing every Demonic Cult member he could find before disappearing into seclusion again.”

“The Fire Gate Clan! We can find him if we go to the Fire Gate Clan.”

“The Fire Gate Clan has a single successor. It’s a situation similar to Great Hero Cheol’s.”

“…”

Even if I wanted to return it, I had no one to give it to.

And the person who had probably been closest to the Fire King was Jopil, but he was already dead. There was no way to find him.

*The best-case scenario would be that the Fire King is already dead…*

He had already been an old man forty years ago, so it was certainly possible.

On the other hand, as a Supreme Peak master, he might have lived an extraordinarily long life.

“Hmm.”

Was this a priceless treasure or a useless burden? As I stared at the Flame Divine Palm with a conflicted expression, Jin Mukyung said,

“If the Fire King is dead… then you’re the master of the Fire Gate Clan now.”

* * *

Jin Mukyung recovered quickly. His Internal Injuries from Pung Yang had been considerable, so it would still take some time for him to recover completely, but he had enough strength to return to the Jin Family of Taiyuan.

“We’re finally going home.”

Hyuk Mujin muttered with deep emotion.

“They say leaving home means hardship. From now on, I will never, ever leave the family grounds again!”

“…Anyone listening to you would think you were the one who suffered the most, you punk.”

“What are you talking about? I have my own hardships, you know.”

“Try saying that to the person behind you.”

Jin Mukyung, who still hadn’t been able to remove his bandages, came flying over and smacked Hyuk Mujin on the back of the head.

*Whack!*

“Urk!”

“Stop spouting nonsense and drive the carriage.”

“There’s a coachman. Why do I have to…?”

Just as Hyuk Mujin said, we had a separate coachman—a member of the Lower District Sect whom Wolhwa had assigned to us.

Wolhwa had come out ahead of time to see us off.

“Goodbye. It’s a shame to part now that the time has come, isn’t it?”

“Then would you like to come with us now?”

I spoke jokingly to her as she winked at me. I was still wary of her, but after traveling together, we were close enough to exchange jokes.

“Oh, I would like that, but… I’m planning to take this opportunity to make a full tour of northern Shanxi.”

Northern Shanxi, which had been under the strict control of the Mount Heng Sword Sect until now, had become an open market. It was only natural that Wolhwa, the Lower District Sect’s Chief Branch Leader in Shanxi Province, would be busy.

“Things must have gone well with the Mount Heng Sword Sect?”

“Secret. I may be the Chief Branch Leader, but I can’t go around telling outsiders the sect’s confidential information.”

Her words said one thing, but her bright, carefree smile was answer enough.

She was the sort of woman who could have nine tails and no one would find it strange, so she had probably obtained a more than satisfactory result.

“We’ll meet again at the Jin Family of Taiyuan next time.”

“Oh, really?”

“We were allies once. Wouldn’t it be better for both of us if we continued to maintain a close relationship?”

Wolhwa gave a coy smile and lifted the hem of her skirt slightly.

“Make sure you come see me again then. Well, I’ll be off.”

As soon as she climbed into the carriage waiting nearby, the coachman cracked his whip. Two pairs of eyes gazed blankly at the carriage as it quickly disappeared into the distance.

“Tsk. She could’ve stayed a little longer.”

“Hmm. Mmm…”

Hyuk Mujin was one thing, but why was Jin Mukyung doing that?

As I watched his wistful gaze, a thought suddenly occurred to me.

*Could that bastard possibly…?*

Was he interested in Wolhwa?

Good heavens. I couldn’t believe it. The man who knew nothing but martial arts was showing an interest in a woman.

I couldn’t keep this earth-shattering news to myself. I moved close to Hyuk Mujin and whispered in a voice as small as an ant.

“Hey, Mujin.”

“Ah! You startled me. What is it?”

“Shh. Listen, but don’t be surprised. Don’t show even the slightest reaction. This is a secret we have to take to our graves.”

Hyuk Mujin answered in a stiff voice.

“Gasp. Yes. Go ahead.”

“I think that guy is interested in Young Lady Wolhwa.”

“…”

“Don’t tell anyone. This is a secret only I know, and I’m telling you alone.”

Despite my serious whisper, Hyuk Mujin replied with a sour expression.

“Oh, yes. Thank you. I’m so grateful I don’t know what to do with myself.”

*Why, this little shit…*

I was wondering how to correct that rude tone when—

“Benefactor.”

I slowly turned around.

Lee Seowol stood there, dressed in a snow-white formal robe.

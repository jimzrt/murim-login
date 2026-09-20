# Checkpoint Review — 585–589

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

# Chapters 585–589

## Plot

Jin Taekyung kills the Level 150 Behemoth with One Annihilation. The level-up restores his Exhaustion and Internal Energy Depletion, but Kim Hwajong is beyond saving after burning away nearly all his innate qi while restraining the monster. Hwajong dies peacefully after asking about Choi Minwoo and receiving Taekyung’s comforting lie that Minwoo is approaching. Skeleton King’s potion and magic absorption cannot save him.

Taekyung places the unconscious Minwoo beside Hwajong, then extracts Behemoth’s surviving Supreme Peak Magic Gem, Behemoth’s Turbid Abyss. The gem reveals that Behemoth absorbed mana from another source, confirming Taekyung’s connection between the Monster Waves, the deaths of Hwajong and Minwoo’s allies, and Go Jun’s scheme. Taekyung withdraws from the Peace Guild, leaves Skeleton King to protect it, and takes the Guild’s members to Ares Guild.

In Ares’s concealed Area A, Go Jun learns that Minwoo survived and blames Taekyung for ruining his plan. He orders Go Se-won to use Ares’s political, prosecutorial, corporate, and media influence to cover up the Pyeongchang disaster and plans to conceal Song Cheonwoo’s disappearance. Se-won rejects the orders and says he will resign if he survives the coming confrontation. As the headquarters shakes and emergency sirens sound, Taekyung arrives in Jongno, enters Ares headquarters, and demands Go Jun.

Ares declares Code Red and sends roughly two hundred Hunters against Taekyung. He overwhelms the Security Team Leader, mage unit, and combined formation with White Flame, the Fire Dragon Divine Spear, Finger Qi, and the Inner-Family Heavy Hand. Though he could kill them, he deliberately leaves the Hunters incapacitated. After warning the survivors not to obstruct him again, he launches the Flame-Extinguishing Divine Fist at the lobby ceiling.

## Continuity

- Kim Hwajong died after sacrificing himself to restrain Behemoth. Choi Minwoo remains unconscious after being placed beside Hwajong and later transported from the battlefield.
- Jin Taekyung killed Behemoth with One Annihilation and identified Go Jun as the culprit behind the Monster Wave and the deaths of Hwajong and Minwoo’s allies.
- Behemoth’s Turbid Abyss is a Supreme Peak Magic Gem that absorbed mana from another source, became turbid and stronger, and requires purification before use.
- Taekyung has withdrawn from the Peace Guild and left Skeleton King to protect its people. He has now entered Ares Guild headquarters to confront Go Jun.
- Go Jun intends to kill Taekyung within one year and relies on Ares’s entrenched influence and Lee Jungryong’s corruption ledger for protection.
- Go Se-won opposes Go Jun’s crimes and cover-up orders and intends to resign if he survives the confrontation.
- Taekyung has incapacitated roughly two hundred elite Ares Hunters while deliberately restraining lethal force. The consequence of his attack on the lobby ceiling is unresolved.
- Cheon Taemin’s collapse more than twenty years ago, his continued unconsciousness, and the suspected Area A connection remain unexplained.
- The unidentified being linked to Go Jun’s plan, the monster that killed Song Cheonwoo, Song’s pocket object, and Go Jun’s old necklace remain unresolved.

## Translation Decisions

- Use **Skeleton King**, **Young Master**, **final rally**, and **Internal Energy Depletion**.
- Use **Behemoth’s Turbid Abyss** and **Supreme Peak Magic Gem**.
- Use **Code Red**, **Multi Shot**, **Binding**, and **Tower Shield**.
- Use **White Flame**, **Fire Dragon Divine Spear**, **Finger Qi**, **Inner-Family Heavy Hand**, and **Flame-Extinguishing Divine Fist**.
- Preserve Taekyung’s deliberate restraint, dry profanity, and distinction between Code Red’s kill authorization and his choice not to slaughter incapacitated Hunters.

## Durable state

{
  "active_continuity": [
    "Kim Hwajong died after sacrificing himself to restrain Behemoth, and Choi Minwoo remains unconscious after being transported from the battlefield.",
    "Behemoth's Turbid Abyss is a Supreme Peak Magic Gem that absorbed another source of mana and requires purification before use.",
    "Jin identifies Go Jun as the culprit behind the Monster Wave and deaths and has entered Ares Guild headquarters to confront him; Skeleton King remains to protect the Peace Guild and its people.",
    "Go Jun intends to kill Jin Taekyung within one year and relies on Ares's political, prosecutorial, corporate, and media influence plus Lee Jungryong's corruption ledger for protection.",
    "Go Se-won openly opposes Go Jun's crimes and cover-up orders and intends to resign if he survives.",
    "Cheon Taemin collapsed more than twenty years ago and remains unconscious at an unknown location, with Area A only suspected.",
    "Song Cheonwoo and Lee Jungryong concealed Taemin's condition and purged those who knew the truth.",
    "Busan's Kraken is dead, but more than one thousand Mermen remain across Haeundae and Gwangalli.",
    "Go Jun seized Song Cheonwoo's children, used an S-grade Magic Gem to cause the Busan Monster Wave, and targeted Choi Minwoo.",
    "Song Cheonwoo was killed by an unidentified monster after falling into an abyss; the object in his pocket released darkness that became light.",
    "Jin has incapacitated roughly two hundred elite Ares Hunters in the Guild lobby while deliberately restraining lethal force."
  ],
  "continuity_sources": [
    589
  ],
  "open_questions": [
    "What caused Cheon Taemin's collapse, and what happened during his more than twenty years of unconsciousness?",
    "Is Cheon Taemin actually being kept in Area A of Ares Guild headquarters?",
    "What is the unidentified being involved in Go Jun's plan, and is it connected to the monster that killed Song Cheonwoo?",
    "What was the object Song Cheonwoo kept in his pocket, and what did its release of darkness and light accomplish?",
    "What is the old necklace Go Jun wears, and why does it matter to his plan?"
  ],
  "safe_through": 589,
  "temporary_decisions": [
    "Use Yeti's Winter Range for 예티의 겨울 산맥, Stone King for 스톤 킹, Behemoth for 베히모스, and Behemos for 베헤모스.",
    "Use Area A for A구역 and Mount Balwang for 발왕산.",
    "Use Hero's Soul for 영웅의 혼, Hyung for 형님, S-grade Magic Gem for S급 마정석, Hell Fire for 헬 파이어, and Hellfire Mage for 겁화의 마법사.",
    "Use final rally for 회광반조, Young Master for 도련님, Rodin's The Thinker for 로댕의 생각 난 사람, and Teleport for 텔레포트.",
    "Use Code Red for 코드 레드, Multi Shot for 멀티 샷, Binding for 바인딩, Tower Shield for 타워 실드, and great tiger for 대호."
  ],
  "version": 1
}

## Reading copies

## Chapter artifact 585

# Chapter 585

Kwoooosh!

At the fierce sound of air being torn apart overhead, the footsteps of thousands of people fleeing in every direction came to an abrupt halt. From among the tourists looking up at the sky, a dazed voice slipped past one person’s lips.

“……Huh?”

It was not a question held by only one person.

The civilians fleeing from the monster, the hundreds of support troops dispatched to stop it, and even the Peace Guild Hunters hurrying down the mountain in accordance with their Guild Master’s final wish—all of them watched the scene and thought of the same question.

*What is that?*

But each group had a different perspective and field of vision. While the civilians looked at the streak of light cutting across the sky with simple bewilderment, the high-ranking Hunters among the support troops sensed a powerful flow of mana in the distant sky for the briefest instant.

At the same time, the Peace Guild members on the mountainside, much closer to the scene, realized how the streak of light overhead had appeared out of thin air.

*……Teleport?*

Who? How? Why?

Countless questions flashed through the minds of countless people. But the one who saw and felt the entire scene more clearly than anyone else was Kim Hwajong.

The old butler, sitting at death’s doorstep, realized the identity of the blue streak spreading outward as it pressed down on the black mist made of magic power.

*That is…*

Something more destructive than anything else. Pure power.

Flame. It was flame.

Flame more intense than sunlight and as fierce as the sun itself streaked across the sky as a beam of light. For a moment, within the dazzling flash so bright that he could barely look at it, a face seemed to pass across his blurred vision.

*Yes. It’s you.*

Just as the smile at the corners of the old butler’s mouth deepened, the primordial monster that had risen from myth opened its enormous jaws toward the streak of light shooting at it.

Kwoooooom—

The wind split apart, and the air scattered. Within the jaws opened wide enough to swallow a mountain, an energy resembling an abyss churned.

But the streak of light did not stop. It grew sharper and larger, transforming into a blue-white flame that whipped through the air.

Gooooooong.

The world stopped. Two forces that swallowed all space and sound as they advanced collided.

And in the next moment, Kim Hwajong could see. He could hear.

Fwoooooosh!

Darkness being torn to shreds beneath the blue sky.

Blue-white flames racing forward while burning everything in their path, and one person’s voice ringing clearly through a dazzling world filled with silence.

“One Annihilation.”

Space warped. The unprecedented flames that fell like a meteor pierced through Behemoth’s jaws before they could fully close.

Watching the monster tilt to one side with a death cry like thunder, the old butler forgot his pain and laughed aloud.

* * *

Even the greatest master in the world, even an ancient monster who seemed fit to appear only in myth, could not escape death. Especially not when a full-powered One Annihilation had pierced through its entire body via its mouth.

—Ho…w……

Bewilderment and death settled at once in the eyes of the monster—a creature unlike any ever seen or heard of. Its enormous body, staring blankly at me, slowly tilted.

Krrrrrrrung!

When the body emptied of life collapsed, the entire mountain trembled. At the same time, amid the enormous clouds of dust rising from every direction, I had to grit my teeth to endure the pain and fatigue surging over me like waves.

*I must not collapse.*

One Annihilation was a double-edged sword that poured all of its caster’s power out at once.

But not yet. At least not in a situation like this. I couldn’t collapse now. The one fortunate thing was that I possessed an unusual power unlike that of ordinary people.

> **System**
>
> You have defeated **Lv. 150 Behemoth**!
>
> You have acquired an enormous amount of **EXP** and **Fame**!
>
> **Level Up!**
>
> The Status effect **Exhaustion** has been removed!
>
> The Status effect **Internal Energy Depletion** has been removed!
>
> Some fatigue and Status effects have disappeared due to the effects of **Level Up**!
>
> …
>
> …
> 
> …

*Damn it.*

I barely steadied my staggering body.

Leveling up was certainly one of the System’s most broken features, but it was not omnipotent unless its effects stacked. The fatigue accumulated in my body and mind was that severe, and my hands and feet tingled as though I had been electrocuted from the aftereffects of using One Annihilation.

But I couldn’t stop, and I couldn’t collapse. Along with the level-up, I drew up the internal energy filling my dantian and released it forward.

Boom!

The compressed air burst outward, scattering the dust cloud. Beyond the view that finally cleared, a rounded shape covered in pure white bones appeared.

Step. Step.

With every step I took across the devastated ground, my heart pounded violently. The breath escaping my lips was mixed with tension and fear that could not be hidden.

That was right. I was afraid of the person I was about to face.

I was afraid he might look different from what I wished for. Afraid I might have to say goodbye before I was ready.

Tap. Shrrr…

When I carefully placed my hand against it, the membrane made of bones scattered as though it were melting. And then I could finally see.

A grim-faced blond foreigner, and a middle-aged man with half-gray hair leaning against him, continuing to breathe as though each breath might be his last.

*This is…*

For a moment, it felt as though my heart had stopped.

Though it lasted only an instant, it was not difficult to understand the situation. The bottle of top-grade potion rolling weakly at Skeleton King’s feet was empty, and strength was already slowly leaving the middle-aged man’s entire body, even though he appeared to have recovered without any visible problems.

Feeling my vision grow distant, I opened my mouth.

“……Butler Kim.”

At my call, his half-closed eyelids trembled faintly. When our eyes met—his gaze on the verge of fading—his bloodstained lips curved gently upward.

“You came.”

“……!”

“Yes. I knew it would be you. That light was truly warm.”

I gritted my teeth to hold back a groan. Butler Kim had already accepted everything that had happened to him. That was probably why his tone was different from usual.

The man before my eyes was neither Butler Kim nor the Guild Master of the Peace Guild. He was simply a human being, Kim Hwajong, saying goodbye.

But…

*I’m not ready yet.*

I couldn’t accept this sudden farewell. I had no intention of smiling as I sent him away. I would do anything to return the man who had become Kim Hwajong the human being in the face of death to Butler Kim, to the Guild Master.

“But I’m a little cold now. It was so warm earlier.”

I took Kim Hwajong’s hand as he muttered in a faint voice and slowly sent Scorching Yang Qi into it as I answered.

“It’s because we’re on a mountain. You’ll be warm soon.”

“Is that so?”

I forced a smile at his feeble question.

“Yes. It’s still winter, after all.”

Feeling the warmth seep into him, Kim Hwajong gave a faint smile.

“It really is. Just as you said.”

“You’ll be all right. Don’t worry. I’ll take care of everything…”

I could not finish the sentence. It was not only because my chest had tightened. The condition of his body, which I had examined with the internal energy I sent through him, had sealed my lips.

*What in the world…*

The human body contained an energy possessed from birth: innate qi. It was no different from the source and root of all energy. But almost none of that innate qi remained in Kim Hwajong’s body.

No. Even that was slowly burning away.

*Like a dying flame.*

Jeok Cheongang’s innate qi had also been damaged in Henan in the past, but it had never been this bad. In Kim Hwajong’s case, it had reached the point of no return.

I could tell enough just by observing his condition through my internal energy.

The resolve with which he, Kim Hwajong, had faced Behemoth. What he had sacrificed to tie down the feet of the monster that had crawled up from the depths of darkness. And…

Who he had used his one and only life as kindling for.

“Young Master… Is Minwoo, is that child safe?”

I answered his fading question in as bright a tone as I could manage.

“He’s safe. I caught a glimpse of him on the mountainside, and there’s nothing wrong with him.”

“Yes. That’s a relief. A real relief.”

*What is there to be so relieved about? You’re the one who ended up like this.*

Just as I bit down firmly on my lips, along with the question I could not bring myself to speak, the thought Skeleton King sent out rang through my mind.

—Though I absorbed the magic that had seeped into his bones and used a top-grade potion, it was already too late. Even after this body stepped in, there was nothing I could do.

I knew. That was why I could not blame him. I knew he had done everything he could.

Though everything about him was an illusion created by illusion magic, the guilt and sorrow on Skeleton King’s face were real.

—……I’m sorry, human.

A question suddenly occurred to me. It was a question about everything happening to me right now.

Why was this guy apologizing?

Why was Kim Hwajong, who had been sitting at the table with us, eating and laughing as we talked only a few days ago, now lying here in a state beyond recovery?

And why had I been unable to stop it?

*Why?*

I had power. The power to stop disasters and prevent tragic deaths.

It all began with the mysterious capsule that had suddenly intruded into my life one day. With it, I changed the fate I had been given and met new, precious connections. And now one of those connections was about to be severed. Someone was about to leave my side.

Then why couldn’t I stop it?

In Shanxi, Henan, Sichuan, and Hubei. In Sichuan, and in Busan…

I had saved so many lives while traveling between the Murim and the modern world. So why couldn’t I save the one person about to leave before my eyes?

*Why?*

It was then, as I sank into an irresolvable question and helplessness.

Ssssh. Tap.

A cold hand covered my trembling fist. Kim Hwajong looked at me with warm eyes and opened his mouth.

“It isn’t your fault.”

“……!”

“You did your best.”

His blurred eyes and fading voice were nowhere to be found now. Seeing him warmly comforting me made my breath catch in my throat.

*The final rally.*

The last flame raised at the edge of death.

No. I still couldn’t let him go. Gritting my teeth, I sent even stronger internal energy into Kim Hwajong’s body. But contrary to my desperate wish, strength was slowly leaving the body that had reached its limit.

*More. Just a little more!*

I poured out the internal energy coiled in my dantian without holding anything back. I held open the acupoints that were slowly closing and fanned the flame dying deep within his body.

But despite my attempts, the end was approaching at a frightening speed.

“It’s cold. I don’t know whether it’s because it’s winter, like you said, or because night has already fallen.”

That was impossible. Even now, an enormous amount of Scorching Yang Qi was flowing into his body, and the afternoon sun was still in the sky.

The cold and darkness that had come over Kim Hwajong were things only he could feel. Death that had reached his doorstep was freezing his body and blocking his view.

I mumbled haltingly toward the old butler, whose breathing had grown thin.

“It’s all right. You’ll be able to see Team Leader Choi soon, so just trust me…”

Thud.

A hand seized my wrist. When I saw Skeleton King shaking his head with a dark expression, I finally realized.

No words or actions could stop one person’s final moment.

Now…

It was time to let him go.

So that he—so that Kim Hwajong—could leave with even a little peace of mind.

“Young Master… Is Minwoo, is that child safe?”

His eyes had grown cloudy without my noticing. Though I had already heard the feeble question he muttered, it did not matter. I could answer him a hundred or a thousand times.

“He’s safe. He hasn’t been hurt in the slightest.”

“I want to see him. Just one last time…”

“You’ll be able to. He’s already on his way here.”

“Is that really true?”

“Yes. Ah, there he is.”

It was a lie. A bright red, pure white lie.

On the nameless mountainside swept by a wave of chaos, there were only the three of us and the monster’s corpse.

But Kim Hwajong could not tell that it was a lie. With only his cloudy vision and fading mind remaining, he reached a hand toward empty air.

As though someone he had been desperately waiting for would take his hand.

Grab.

At my call and the look that accompanied it, Skeleton King firmly took that hand. The old butler’s eyes curved like crescent moons, and a radiant smile spread across his lips.

“You’ve come.”

And then, in the next moment—

“My grand…son.”

The flame that had burned for one person and refused to go out for this moment finally guttered.

Sssrrk. Tap.

The world went black.
## Chapter artifact 586

# Chapter 586

Sometimes, certain kinds of truth are cruel and cold.

People who face such truths often turn away from them because they cannot believe the situation they are in—or because they do not want to believe it.

Like me right now.

“……Human.”

When Skeleton King’s voice broke the silence and pierced my ears, I felt as though I had awakened from a long, terrible dream.

And in the next moment, I realized that none of it had been a dream. It was reality.

*He’s gone. Truly.*

Kim Hwajong had finally met his death. His face was peaceful, and joy lingered at the corners of his lips, which had stiffened in an upward curve.

It was the smile left by a dead man who had been able to fulfill his final wish before departing.

But I continued sending Scorching Yang Qi through his body, along with questions that would never reach him.

*Are you still cold? Is it still dark?*

Perhaps the old butler I remembered was still wandering through an endless winter night.

Perhaps he was shivering in the cold, searching for someone in darkness so deep that he could not see even an inch ahead.

That was why I could not stop.

That was why I continued forcing warmth into his body as it grew colder and colder.

Thud.

A cold hand touched my shoulder. Skeleton King’s voice reached my ears, low and subdued.

“Human.”

“Let go.”

“It is enough now. Stop.”

He was wrong. It wasn’t enough. So I couldn’t stop.

Just as I was about to roughly shake off the hand on my shoulder, Skeleton King continued.

“He will not be cold anymore, so let that human go…… Let that person rest.”

“……!”

Why did all the strength leave my body the moment I heard those words?

I truly did not know.

Perhaps it was because Skeleton King had used honorific speech toward a human for the first time. Or perhaps it was because the voice that had pierced my ears sounded unusually powerless.

If it was neither of those things, then perhaps it was because of the guests who had returned to this nameless mountain ridge after the disaster had passed through.

Crunch.

Cautious footsteps pressed into the snow.

I turned my head toward the sound and finally saw five men and women emerge into view.

They were faces I had encountered once or twice inside the Guild House, exchanging greetings in passing, so I had no trouble recognizing them.

*Peace Guild members.*

They had undoubtedly returned after realizing that the situation had changed.

They had already fought Behemoth desperately ahead of me, exhausting themselves and suffering injuries. With vacant eyes, they stared at the monster collapsed before them. Then they turned their heads and looked in this direction.

And then…

“No!”

“Guild Master!”

Shouts and screams rang out together.

The person who greeted them as they hurried over Behemoth’s corpse was Kim Hwajong, fallen into a deep sleep from which he would never awaken.

“H-How could this happen?”

“……Damn it. I knew this would happen. I knew it!”

Their voices were filled with grief and tears.

Though I had not been there, I could clearly imagine how everything had unfolded.

*He must have told them to go. Told them to run with Team Leader Choi because he was all right.*

That was the kind of person Kim Hwajong was.

There was something more precious to him than his own life. A young man who could be called his Young Master—or, more accurately, his grandson.

I had stood there as though nailed to the ground, watching everything. Then I suddenly opened my mouth.

“Team Leader Choi.”

“Y-Yes?”

A rough, hollow voice slipped from my lips. It sounded unfamiliar, as though it belonged to someone else.

“Lay Team Leader Choi down beside him.”

“……!”

“Hurry.”

The Guild members stared blankly at me. Then, realizing what I meant, they nodded.

They carefully laid Team Leader Choi down on the ground. He had lost consciousness after exhausting every last bit of his strength.

The two men lying side by side looked nothing alike, and yet they resembled each other.

*You finally met, the two of you.*

Without a word, I placed their hands together.

Was it only my imagination? For a moment, the smile at the corners of Kim Hwajong’s lips seemed to grow brighter.

“Hunter Jin Taekyung. Wouldn’t it be better to wake the Team Leader……?”

One of the Guild members spoke carefully. I shook my head.

“No.”

“But…….”

“We can’t do that. At least not right now.”

I cut him off firmly. It wasn’t as though I hadn’t considered it myself.

If Kim Hwajong had not yet met his death, I would have done anything necessary to wake Team Leader Choi and let the two of them meet.

But…

*It’s already too late.*

Kim Hwajong was already dead, and accumulated fatigue had pushed Team Leader Choi’s weakened body to its limit.

Even if I forced him back to consciousness and gave him a potion, the backlash would hit him several times harder—along with immeasurable grief and rage.

The dead had found rest after suffering, but the living had to continue on while carrying their pain.

I had realized that three years ago. I could not wake Team Leader Choi, whose body was already in such poor condition, only to tell him that cruel reality.

There was just one thing I could promise.

Before Team Leader Choi regained consciousness, I would bring him a gift that could soothe even a little of the rage and grief he would feel.

Whoosh! Slash!

The tip of the spear I swung without any preparation split the air.

Force shot out in the shape of a half-moon and sliced through Behemoth’s enormous body, which lay collapsed on the ground. Skeleton King muttered like a sigh.

“Stop.”

Instead of answering, I swung the spear in my hand again.

Once. Twice. Three times……

Slash! Slash! Fwoosh!

The body was cut into pieces, and the blood remaining in the corpse spurted upward like a fountain.

The powerful magic Behemoth had once contained was gone. Now, it was nothing more than a mass of meat.

I cut it apart without hesitation, like a butcher.

That continued until Skeleton King could no longer stand the sight and shouted.

“I said stop! What difference will this make……!”

I cut off his shout in a quiet voice.

“It can make enough of a difference. That’s why I’m doing this.”

“What?”

Skeleton King asked with a puzzled expression.

“What in the world are you talking about?”

I did not answer. I simply stepped forward.

In a single step, I closed several meters of distance, bringing Behemoth’s corpse right before me.

I stared at the chopped-up remains, so mutilated that none of its former majesty remained.

At last, I found what I had been searching for.

No. It had announced itself before I could even find it.

Vrrrrrrm.

A faint vibration traveled through the air. At the same time, I sensed a murky yet powerful energy.

“……Found it.”

I had worried that it might have been erased by the One Annihilation I had fired earlier, but fortunately, *it* was unharmed.

I muttered with a hint of relief and reached out without hesitation.

Whoosh—clack!

Seizing an Object Through Empty Space sent *it* flying into my hand. I stared at it with a solemn gaze.

Then I muttered inwardly, where no one could hear.

*Item Appraisal.*

Ding.

> **System**
>
> **Item Window**
>
> **Behemoth’s Turbid Abyss**
>
> **Type:** Magic Gem  
> **Grade:** Supreme Peak  
> **Restriction:** None  
>
> **Description:** The abyss contained within Behemoth, a Named Monster and primordial beast, and the source of its mana.
>
> For some reason, it absorbed mana from another source. Its once-pure darkness became turbid and grew even more powerful.
>
> An extremely difficult and painstaking purification process must be completed before this can be used.

The moment I read the System Window floating in the air, my eyes grew hot.

But my mind was colder and clearer than ever as it turned over the information.

*Behemoth’s Turbid Abyss.*

The System had never lied to me. That meant the contents of the description were also facts without the slightest error.

*It absorbed another magic power for some reason. So that’s how it is.*

The questions that had been drifting through my head for the past several hours, ever since my conversation with Kraken, began to fall into place one after another.

Who had given Kraken the Magic Gem and caused the Monster Wave? Who was behind him, giving the orders?

Why had Team Leader Choi, who was so busy, left Seoul and come all the way to Pyeongchang in Gangwon Province? Why had another Monster Wave occurred here of all places?

And what did the description of the Magic Gem left behind by Behemoth mean?

*Why? Why? Why?*

I asked myself the questions, then found the answers myself.

A short time passed—though it felt like several hours.

After that, I was able to derive the answer to every question.

Except for one final piece of the puzzle.

*Yes. The last one.*

But I did not hesitate. I already knew where to find the final piece.

“Why did you come here today?”

My question was directed at the Peace Guild members.

When everyone’s attention turned toward him, the middle-aged Hunter who appeared to be the highest-ranking among them answered with a dark expression.

“There was someone Team Leader Choi had to meet in secret. A man who had changed his appearance with illusion magic. He looked extremely anxious.”

“Who was he?”

“I’m sorry, but…… None of us, myself included, knows his identity.”

The middle-aged man was probably telling the truth. But I was not disappointed.

I had heard the man’s identity directly from Team Leader Choi himself not long ago. Even the temporary Head of Security had not been informed.

*Song Cheonwoo.*

A hero of the Great Cataclysm and the European regional director of Ares Guild.

And…… the political rival who had opposed both Lee Jungryong and his disciple Go Jun across two generations.

But I already knew about the secret temporary alliance between him and Team Leader Choi. I was not foolish enough to think Song Cheonwoo was the culprit.

*There was no reason for him to do it. Not one.*

Song Cheonwoo was an ambitious man whom even the passage of time had failed to tame.

Setting everything else aside, the idea that he would try to kill Team Leader Choi—a reliable ally who was working to bring down Go Jun—was absurd from the outset.

In the end, that meant someone else was behind everything that had happened today.

The person who would gain more than anyone from the deaths of the two men.

The person who could use an S-grade Magic Gem of astronomical value and rarity to cause a Monster Wave.

*Go Jun.*

The moment the last piece of the puzzle fell into place, I realized what I had to do.

I also realized that the repercussions of the choice I had just made could spread to the people around me.

*In that case……*

I slowly closed my eyes.

There was no turning back now. Regardless of whether it was right or wrong, this was something I had to do.

When I opened my eyes again, there was not the slightest tremor in my heart or voice.

“If Team Leader Choi wakes up while I’m gone, please make sure someone tells him.”

“Pardon? Tells him what……?”

“S-grade Hunter Jin Taekyung.”

The unfamiliar, dry voice that sounded as though it belonged to someone else continued.

“As of this moment, I am withdrawing from the Peace Guild.”

“……!”

“……!”

The frozen expressions of the people before me came into view.

Along with someone’s twisted face.

“You bastard, don’t tell me……!”

“You stay here. Just in case, protect the people and the Guild.”

Those who were leaving had to leave, and those who were staying had to stay.

I shook my head at Skeleton King when he tried to stop me again, then asked the Guild members who had gone rigid like statues.

“Is anyone here capable of Teleport? Hands.”

“H-Hand.”

A mage raised his hand without thinking and asked with a dazed expression,

“B-But where are we going?”

“Jongno. No……”

I looked at the old butler who had fallen into a sleep from which he would never awaken, then continued.

“Let’s go to Ares Guild.”
## Chapter artifact 587

# Chapter 587

The air. Time.

Everything seemed to have stopped.

That was how it felt to the master of Area A, hidden in the strictest secrecy within Ares Guild in Jongno, Seoul.

*How?*

Only that question circled through his mind.

Seok Go Jun had forgotten that Go Se-won was standing beside him. With a rigid expression, he stared at the holographic television mounted on the wall.

Footage transmitted from dozens of unmanned reconnaissance drones deployed by the government and various media outlets was streaming live.

“Right now, you’re looking at Mount Balwang, near Pyeongchang in Gangwon Province, where the Monster Wave occurred. And…”

The voice of the anchor of the public broadcaster’s nine o’clock news flowed through the room. Unlike his usual calm, serious delivery, the unseen anchor sounded highly agitated.

“Can you see this, everyone? This is the corpse of the Named Monster Behemoth! Around it, survivors of the disaster are being transported by emergency helicopters…”

Go Jun’s eyelids trembled.

The brutally dismembered corpse of the monster. The survivors. The voices of the Peace Guild members and the anchor explaining the situation.

All of it stoked his fury.

Bang!

With a thunderous explosion, the latest-model holographic television—replaced more than ten times over the past month—burst apart and scattered into dust.

Go Jun did not care.

The instant Choi Minwoo appeared on the screen, being transported with a respirator over his face, everything else became meaningless.

*He survived. Choi Minwoo survived.*

That fact weighed heavily on his heart.

To Go Jun, Choi Minwoo was a bastard who deserved to die. A bastard who had to die.

That was why he had laid the trap.

He had lured Jin Taekyung to Busan and used Song Cheonwoo to make his enemies destroy one another, ensuring that both sides would be crippled.

But…

*What went wrong?*

A red light flickered in Go Jun’s eyes. In his hand, two unpurified S-grade Magic Gems were grinding constantly against each other.

Crk. Crk.

What had he missed?

Crk. Crk.

He had thought the plan was perfect.

No—perhaps it really had been perfect.

If there had been one flaw in that perfect plan, it was the fact that something beyond perfection had stood on the other side.

*Jin Taekyung.*

It had to be him. The Behemoth’s mana barrier had blocked every media outlet from learning the details of the situation, but there was no doubt.

That bastard who had killed Lee Jungryong—his Master, a man who had seemed like a living god—and carved an indelible terror into Go Jun’s mind had interfered yet again.

Even after he had laid a trap that should have been impossible to avoid. Even then, once again!

Crkkkk!

Instead of a roar filled with resentment, a chilling grinding sound filled the office.

Suppressing the fury surging inside him, Go Jun barely managed to force out his voice.

“Song Cheonwoo… What about Song Cheonwoo?”

When no answer came, a thunderous shout erupted.

“I asked what happened to him!”

“……”

“Team Leader Go! Go Se-won!”

Go Se-won, the Head of Security, had been silently watching his superior vent his rage. He answered in a dry voice.

“He isn’t on any of the survivor or casualty lists we obtained.”

“What about the Gate access records?”

“Nothing there either. We believe the Peace Guild, which effectively owns that Gate, deliberately left no traces behind.”

“Of course. That makes sense. Even if Choi Minwoo is a little bastard, he’s extremely careful. Isn’t he?”

“……Yes.”

A secret that never crossed the walls was both the advantage and the disadvantage of complete secrecy.

Go Jun roughly ran a hand through his hair. Then he lifted the whiskey in front of him and drank straight from the bottle before muttering.

“Fine. Even if things went to hell, there’s nothing they can do about it. Song Cheonwoo can either prove his alibi with the double we prepared in advance, or, if that becomes difficult, we can make it look like he acted alone. There were no traces left in Busan, so we don’t need to worry about that. Right?”

“But, Vice Guild Master, the Pyeongchang incident is too serious to be handled as Song Cheonwoo’s lone crime. According to the information we obtained, Kim Hwajong—the nominal Guild Master of the Peace Guild—died, and Song Cheonwoo is unquestionably a member of Ares…”

“Listen, Team Leader Go.”

At that moment, Go Se-won felt a chill seize his entire body. His frozen figure was reflected clearly in Go Jun’s red eyes.

“Then make the serious matter smaller.”

“V-Vice Guild Master.”

“Whether it costs tens of billions or hundreds of billions, I don’t care. Scatter money through the prosecutors’ office. Threaten the old men sitting in the National Assembly. Grab the collars of anyone carrying a camera or microphone. Isn’t that your job?”

“……!”

Go Se-won’s eyes trembled violently. The malice radiating from one man, along with his horrifying aura, pressed down on him.

*How can someone become like this…?*

It was more than astonishing. It was horrifying.

Could a person really change this much in only a few months? Could someone really fall this far?

And what, exactly, was the overwhelming power bearing down on him now?

As Go Se-won stared at Go Jun in stunned disbelief, Song Cheonwoo’s voice from several days earlier suddenly echoed through his mind.

*The boundary between humans and monsters. That bastard Go Jun… has already become a monster.*

It was true.

Go Jun—his superior—had already become a monster.

He had used the loyalty of his subordinates, bordering on religious devotion, to send them to their deaths. He had artificially caused two Monster Waves that could result in thousands, tens of thousands, perhaps even hundreds of thousands of casualties.

All for the single purpose of eliminating his enemies.

*A monster that has forgotten even the minimum duty a human being should possess.*

As Go Se-won struggled desperately to hide his agitation, Go Jun opened his mouth again.

“Deal with it properly. Choi Minwoo survived, but at least Song Cheonwoo has been taken care of. If we get through this one time, there shouldn’t be a problem.”

Go Jun had regained his composure, and his voice was cold.

He had failed to bring down the external enemy, but he had eliminated the internal one. That was as good as achieving half a victory.

Once the fake Song Cheonwoo he had installed went through the retirement process and disappeared, everything would be over.

No rumor or condemnation would be enough to bring down Ares Guild.

“It’s been thirty years. Thirty whole years. Politics, business, the prosecutors’ office, the media… They all grew beneath Ares’s shadow.”

Crk. Crk.

Cheon Taemin had built the foundation, but after Taemin lost consciousness, it was Lee Jungryong who had built the pillars and roof.

The young politicians Ares had supported long ago had become prime ministers, ruling-party leaders, and opposition heavyweights. The corporate world, the prosecutors’ office, and the media were no different.

Some portion of the astronomical sums Ares Guild earned from Gates—the diamond mines of this world—had been scattered everywhere as dirty money. Those seeds had grown into a dense forest surrounding an impregnable fortress.

Go Jun was one of the people who knew that fact better than anyone.

Among the things he had inherited from his Master was a ledger filled with every kind of corruption and weakness.

“Even if everyone points fingers at us, this world itself is what protects us.”

He had forgotten that in his impatience and fury.

He had forgotten just how much power he possessed.

And just as Go Jun’s confidence fully returned and a deep smile spread across his lips—

“You’re wrong.”

“What?”

Go Se-won looked straight at the monster before him—his superior—with an indescribable expression.

“The old politicians raised in Ares’s name, the Prosecutor General, the corporate dynasties and media conglomerates whose roots stretch back to the Japanese occupation—they won’t protect you, Vice Guild Master.”

“Team Leader Go. What are you saying right now…”

“Some of what you said is true. Ares’s name will not collapse over something as simple as pointing fingers and condemnation. But even if the entire world protects you, there is one person it cannot stop.”

“……!”

Go Jun’s body abruptly froze.

The thought of grabbing the Head of Security by the collar for daring to spout nonsense in his face had already flown far away.

It was because of the name of the one person who had struck him in the mind.

*Jin Taekyung.*

Reading the thought in his trembling superior’s eyes, Go Se-won continued in a low voice.

“Have you forgotten? Whose hands brought down the person who personally cultivated the world you now trust?”

“……!”

The shock struck Go Jun like a blow to the back of the head. He clenched his teeth without realizing it.

Unfortunately, the words being spoken by the bastard in front of him were not nonsense. They were all facts.

*Master.*

It was true. Lee Jungryong—Ares’s master and a man who had been no different from the king of Korea—had ultimately been killed by Jin Taekyung’s hand.

The entire world had belonged to Lee Jungryong, yet no one had been able to protect him.

A boiling voice seeped through Go Jun’s clenched teeth.

“Team Leader Go… You little bastard.”

“I only said what someone had to say.”

“Shut up.”

“If that is your order, Vice Guild Master, I will obey. But please don’t dismiss my words without hearing them.”

“I said shut your mouth.”

Rumble!

A massive aura burst from Go Jun’s entire body like an explosion. The office shook as though an earthquake had struck.

Go Se-won’s face turned pale before that truly overwhelming power, but compared to the disgust he felt now, the fear was nothing.

*Monster.*

Go Jun read the emotion passing through Go Se-won’s eyes and bared his teeth.

“Team Leader Go, have you suddenly gone mad? Have you lost your mind?”

“……”

“I only put you in the position of team leader because your abilities were at least useful. Did wearing a title that was never meant for you suddenly make the world look different?”

Go Jun let out a laughter filled with fury before continuing.

“Team Leader Go, you’re a coward and a piece of trash. You wrapped it in pretty words and called it loyal counsel, but you’re more afraid of Jin Taekyung than you are of my Master and me.”

“……That isn’t true.”

“It’s too late to deny it. Let’s at least admit what we both know. Yes, that bastard Jin Taekyung is strong. That’s a fact. But how long can he stay above my head? Hmm?”

Crk. Crk!

“It’s only a matter of time. Now that I—now that I’ve decided to kill that bastard—I’ll find a way worthy of it… Damn it. Do you understand?”

Crkkkk!

His chilling voice mingled with the grinding sound. Go Jun glared at Go Se-won with eyes that had reddened until they were nearly blood-colored.

He leaned his upper body forward toward the subordinate who had dared to commit an unforgivable crime. An old necklace slipped out and spun slowly in front of Go Se-won’s eyes.

“Team Leader Go. Go Se-won. You ungrateful piece of trash.”

“……”

“A year at most. Jin Taekyung… That bastard you’re so afraid of will die by my hand. I don’t care whether it’s Sichuan or Seoul. I’ll kill him without anyone realizing what happened—the same way Master was killed.”

“……”

“Until then, this world is on my side. Until I leave this fortress myself, no one can touch me. You stupid bastard.”

The joy of revenge and the madness directed at one person had become intertwined. Go Se-won silently watched those impossibly murky eyes before suddenly opening his mouth.

“One year. That’s a long time.”

“What?”

“I don’t know what method you found, Vice Guild Master, but… Jin Taekyung won’t wait that long.”

“What, do you think he’s going to come charging in right now?”

“Yes.”

At the short answer, Go Jun laughed aloud. He laughed until his face twisted and the office seemed ready to fall apart from the sound. Then, suddenly, his expression sank, and he parted his lips.

“You pathetic idiot. This is Ares Guild. If we fall forward, we hit the Blue House; if we fall backward, we hit the National Assembly. Do you really think he’ll do something insane enough to make the entire world his enemy?”

“I hear someone I know artificially caused a Monster Wave. Do you really think Jin Taekyung is incapable of doing something less insane than that?”

“……!”

“And, Vice Guild Master.”

Go Se-won let out a bitter laugh without realizing it. He had remembered what he learned while monitoring Jin Taekyung’s every move and investigating his past.

“Jin Taekyung is a lunatic. Didn’t you know?”

“You bas—!”

At that moment, Go Jun’s eyes widened.

Rumble-rumble-rumble!

Ares Guild headquarters shook. The skyscraper of more than one hundred floors trembled from top to bottom.

Beyond the thunderous roar as it began to subside, Go Se-won’s voice pierced Go Jun’s ears.

“Dealing with that lunatic will probably be my final mission. Thank you for everything, Vice Guild Master. If I survive, I’ll submit my formal resignation.”

Carrying both his gratitude for everything until now and his disgust toward Go Jun as a human being, Go Se-won bowed deeply.

Then he flung open the tightly closed door.

Sirens announcing an emergency were waking Ares Guild.
## Chapter artifact 588

# Chapter 588

That day, the air in Korea was heavy with unease.

The Monster Waves that had erupted one after another in Busan and Pyeongchang had been successfully contained, but not without a substantial number of casualties.

People who had been going about an ordinary day were confronted with shocking news and began trembling with anxiety.

“Manager, did you see the news?”

“I did. That’s why I abandoned my work and came out here.”

“I can’t focus on anything either. What if there’s really a Monster Wave near our homes or workplaces…?”

“Hey, don’t say things like that. You’ll make them come true. Come on, let’s have a cigarette.”

Office workers escaping their suffocating workplaces and heading for cafés. Students who had just finished class and were on their way home. Children clinging to their parents and begging to keep playing, unaware of what was happening, and parents dragging their children away just in case.

It was an uneasy afternoon, and people’s hearts were in turmoil. Eyes filled with worry and fear remained fixed on smartphones broadcasting emergency news alerts.

> — You are now looking at the collapsed Gwangan Bridge. In the nearby waters lies the corpse of the Named Monster Kraken, the cause of the Busan Monster Wave…

> — The number of casualties tallied so far is approaching four thousand. Rescue and search operations are still underway, and the list of confirmed casualties can be viewed through the *Monster Disaster* app…

> — I am currently at Mount Balwang in Pyeongchang, Gangwon Province. The Monster Wave has ended with the death of the Named Monster Behemoth, but more than seven thousand citizens who had visited nearby condominiums and ski resorts remain terrified.

> — The Pyeongchang Monster Wave resulted in 371 casualties. Of the forty-five confirmed dead, the Guild Master of the Peace Guild, Mr. Kim Hwajong, is included, causing tremendous shock…

Every report was horrible and shocking. Public broadcasts, cable channels, online news articles—everywhere was in an uproar, as though someone had stirred up a hornet’s nest.

People in the streets swallowed dryly as they looked at the ruin of Gwangan Bridge and were left speechless by the sight of a city drowned in blood.

It was a disaster. There was no other word for it.

But the media’s attention was not focused solely on the damage.

No, there was one name that could never be left out when discussing the Monster Waves.

> — This is an unprecedented event, unlike anything Korea has experienced since the Great Cataclysm. Two Monster Waves occurred two hours apart and caused tremendous damage, but a flawless initial response brought the chaos under control quickly. And, amazingly, one person was present during the suppression of both Monster Waves.

> — The whereabouts of S-rank Hunter Jin Taekyung, a young hero who appeared like a comet and killed two Named Monsters in a single day, remain unknown. The Peace Guild has yet to issue an official statement regarding the matter…

A hero who had calmed the chaos and then vanished without a trace. Naturally, everyone’s attention focused on that one fact.

As soon as the government announced that Jin Taekyung’s whereabouts were unknown, various media outlets began pouring out speculation before even a few minutes had passed.

Some claimed he was dead or missing. Others said he had fallen unconscious from the aftereffects of the battle.

Most of them were Third Rate media companies famous for dealing in rumors and wild gossip, but ordinary people were wondering the same thing.

*Did something really happen to him?*

A man who had no reason to disappear had vanished without a trace. Without saying a word. Without showing himself to anyone.

The young hero had already disappeared by the time the support forces arrived, and the Peace Guild had issued no official statement.

As the news swept across Korea and reached other countries, the questions grew like a snowball.

And then…

That snowball rolled and rolled, growing larger and larger, until it came to a stop amid the skyscrapers of Jongno.

Step.

No one knew when or how he had appeared.

But the people hurrying through the densely packed forest of buildings for their own reasons realized something.

The person in the profile photo filling the smartphone screens in their hands had appeared right before their eyes.

Drip. Drip-drip.

He was red, and he was blue.

Every time he moved, red and blue blood soaked into the sidewalk beneath him. He was covered in the blood of humans and monsters.

His nearly six-foot-four frame moved slowly forward, his perfectly balanced body stepping through the blood.

“…Jin Taekyung?”

Someone’s dazed voice broke the silence that had suddenly settled over the street.

But instead of cheering at the young hero who had finally appeared, approaching him, taking out their smartphones to photograph him, or reporting his presence to the media, the people fell silent and stopped where they stood.

Perhaps it was because his eyes, visible between his blood-soaked hair, had sunk into unfathomable depths.

Step. Step.

Perhaps it was because profound exhaustion seeped from every one of his footsteps.

Huff.

Perhaps it was because the white breath escaping between his split lips carried the sorrow of someone who had lost another person.

But one thing was certain.

Everyone filling the surrounding streets instinctively understood.

They must not stand in his way.

Swish. Swoosh.

Hundreds of people parted to either side.

Instead of the staff of a prophet from myth, the young man carried a pure-white spear as he crossed a human wave made for a single person.

Those who had followed his back with dazed eyes began walking after him.

No one there knew why, but everyone moved as though under a spell. Hundreds became hundreds more, and thousands became thousands more.

Before long, the crowd had grown into the thousands. Like people under hypnosis, they walked and kept walking.

The massive procession, which had begun with one man’s footsteps and seemed as though it would never stop, came to a halt for the same reason: one man’s footsteps stopped.

Step.

The final step.

The young man suddenly raised his head and looked at the sky.

It was five in the afternoon. A particularly cold, exhausting, and sorrowful day in January was slowly drawing to a close beneath a reddish glow.

But not for one person.

*It’s beginning now.*

The sunset stretching from the west flashed across the towering skyscrapers.

Among them, the enormous letters mounted on the top floor reflected in his eyes.

**ARES GUILD**

An impregnable fortress that could not be brought down, and a magnificent royal palace.

How many Hunters were inside this place? How many enemies would he have to defeat to face the bastard sitting on the throne?

*Hundreds? Thousands?*

It didn’t matter. Hundreds or thousands.

Beneath the red sky, the young man, Jin Taekyung, muttered,

“Well, this is perfect weather for fucking someone up.”

Whoosh!

Flames resembling the sunset coiled around his arm and surged upward. The crowd, gazing at the sight as if entranced, swallowed hard and retreated.

At that moment—

“I’m here, you fucking bastard.”

Whoooooosh—BOOM!

An unprecedented force shook the skyscraper.

* * *

Rumble-rumble-rumble!

A massive vibration shook everything in every direction. The entire area trembled as though an earthquake had struck.

Spiderweb cracks spread across the marble covering the floor without a gap, and the splendid, valuable works of art decorating the lobby fell like a sudden shower onto the cracked marble.

Crack! Crash!

That was the sight I saw the instant I entered the lobby.

The thing that had just shattered was a plaster statue depicting some man, but I couldn’t remember its name at all, so I had no choice but to ask someone nearby.

“What was that statue that just broke? I saw it in an art textbook. Was it Rodin’s *The Man Who Had a Thought*?”

“…Ah. Ahh.”

A young Ares Guild member who appeared to belong to the Security Team stammered with a frozen expression.

He looked so pitiful that I changed my question.

“Then what are your personal thoughts on today’s Monster Wave?”

“P-Pardon?”

“You’re lucky. You’re just a low-ranking grunt who doesn’t know anything.”

And that was what saved the man’s life.

Whoosh!

With a stealthy whistle through the air, the Finger Qi I fired struck the man’s acupoints.

At the same time, a streak of light came rushing forward over his rigid body as he collapsed.

Screeeeech! Boom!

The arrow that grazed my ear smashed into the entrance door. A middle-aged man who appeared to be an A-rank Hunter stood there with a hardened expression, his bowstring drawn taut as he aimed at me.

No, that was not the only weapon pointed at me.

Swish, swish, swish!

Dozens of Security Team members. Hundreds of Hunters filling the lobby. They watched me with tense expressions.

Their hands held flames and ice, spears and swords and other bladed weapons, or bows.

A middle-aged Hunter presumed to be the Security Team Leader spoke in a rigid voice.

“Step back, Mr. Jin.”

Step back?

Unable to hold back a hollow laugh, I answered,

“That’s going to be difficult.”

“Why are you doing this?”

“There are a lot of reasons. But I’m not sure you’ll believe me even if I tell you right now.”

“Mr. Jin Taekyung. You…!”

I looked at the people filling the lobby with hollow eyes.

*Who should I kill, and who should I spare? Which of them is directly connected to what happened today?*

Suppressing the murderous intent that arose as naturally as breathing took all the strength I had.

*Don’t forget. I’m not a monster.*

If I killed everyone here today, I would become a monster. But I wanted to remain a human being until the end.

At the very least, I wanted to ensure that innocent people were not killed for something their superior had done.

I thought that was the path that was best for Kim Hwajong—and for everyone.

“Let’s make this easy for everyone.”

I looked straight into hundreds of pairs of eyes and said one thing.

“Bring Go Jun.”

“……!”

“……!”

An invisible resonance swept through the lobby and the hundreds of Hunters.

Within the air vibrating with a sharp ringing, I continued slowly.

“Right now.”

The Security Team Leader answered with a stiff expression.

“I don’t think that will be possible.”

“Why not?”

“I received orders. I was ordered to stop Mr. Jin Taekyung by any means necessary.”

“I see.”

“I don’t know what business brought you here, but you should turn around and leave while you still can. How many Hunters do you think there are in this building—in Ares Guild House?”

“There are already this many in the lobby, so there must easily be a thousand in total.”

“I guarantee that if you don’t leave now, every person in this building will be targeting you within five minutes at the latest.”

I answered calmly.

“And I guarantee that if you don’t put down your weapons and run right now, within five minutes, every last one of you will be physically incapable of functioning normally.”

“……!”

“So disappear from my sight. I don’t want to cripple people who have nothing to do with this.”

Whoooooosh!

A sudden gust of wind swept through the lobby.

Crushed beneath the powerful wave of qi flowing from my entire body, the Security Team Leader clenched his teeth.

The polite tone he had tried to maintain until the end had flown far away beneath pressure that surpassed anything he could have imagined.

“Why… Why are you going this far?”

“Because I’m a Hunter.”

“What?”

“Go Jun, that bastard, is a monster. Hunters don’t need a reason to kill monsters.”

Go Jun obviously wouldn’t have broadcast what he had done far and wide, so most of these people would not easily understand what I was talking about.

But they would have realized one thing for certain.

If they stood in my way, things would not end well for them.

The Security Team Leader looked at me with a complicated expression and muttered,

“Fuck. We’re seriously screwed.”

“I like your honesty. So, what’s your answer?”

That question was not directed at him alone.

A conflicted light appeared in the eyes of the Security Team Leader and the roughly two hundred people surrounding me from every direction.

Their hands trembled around their weapons.

Then—

> — Code Red. Code Red. All Ares Guild members are to respond. The target is…

A voice rang thunderously throughout the skyscraper from the large speakers installed in various places.

> — Jin Taekyung.

“……!”

“……!”

The air around us trembled.

And in the next moment, I saw it.

The conflict vanished from hundreds of wide-open eyes, and countless streaks of light burst from their hands, becoming a gigantic flash that flooded every direction.

Kuwaaaaaaah!

Red, blue, and white.

I swung the dazzlingly white blade of my spear toward the enormous flash.

Whoooooosh!
## Chapter artifact 589

# Chapter 589

Countless rays of light gathered and gathered until they transformed into a massive pillar of light.

Attack Magic and debuffs covered the space overhead, while spears, arrows, and other weapons launched with full force rained down like a sudden shower.

But…

It was already too late to retreat. For me, and for them.

Step.

I advanced toward the multicolored flashes.

As I moved, scorching heat erupted from White Flame’s spearhead as I slashed diagonally downward, setting everything around me ablaze.

Sssshhhhh!

Space warped. The searing blue-white hellfire forcibly dispelled every spell and devoured the weapons hurtling toward me at tremendous speed, still infused with mana.

Whoooosh!

“……!”

“……!”

Heat boiled, and a mirage rose with it. Beyond the haze, I could see hundreds of pairs of eyes filled with shock.

The Security Team Leader realized that every attack had failed pointlessly. He drew his bowstring again and fired ten arrows with Multi Shot as he shouted,

“Formation!”

Screeeeech!

Contrary to the arrows he had fired, his body moved like the wind, retreating behind the tanks.

His quick judgment and precise attack were excellent, as befitted an A-rank Hunter belonging to Ares Guild, but…

*This time, you picked the wrong opponent.*

I muttered the thought inwardly and thrust out my fist. The single punch driven along my smoothly rotating shoulder and arm smashed through the empty air.

Whoom! Bang!

A short but powerful straight punch.

At the same time, compressed air burst outward, and a small typhoon roared around me. The ten arrows rushing in like rays of light bent when they collided with the storm.

Swish-swish-swish! Boom!

The moment the deflected arrows slammed into various places throughout the lobby, I had already launched myself ahead of them and erased the dozen or so meters between us, arriving before the Security Team Leader.

“You should’ve shot more gently. Then I would’ve made it hurt less.”

“……!”

They were far too close for him to draw his bowstring again.

Instead of answering, the Security Team Leader swung the bow in his hand. With a faint metallic click, a blade sprang from the tip of the bow and flew toward my chest.

Sssshhh!

It was probably a movement he had mastered through thousands, perhaps tens of thousands, of repetitions.

But speed was relative. To my eyes, his attack was so slow and feeble that it made me want to yawn.

Slow enough to catch with one hand.

Clack.

The blade stopped half a handspan from me and trembled.

In a moment too brief to even call an instant, I saw unmistakable shock pass through the Security Team Leader’s eyes. I tightened my grip around the middle of the bow.

Crack!

Strength beyond human limits bore down on the weapon, shattering the defensive Magic covering it and breaking the bow made from the hardened bones of a monster.

Before the archer who had lost his cherished weapon could even cry out, my palm pressed against his chest.

Boom!

The Inner-Family Heavy Hand—a technique that struck the outside to damage the inside.

With a small explosive sound, the Security Team Leader’s body shot backward like a cannonball.

The instant he slammed into the lobby wall and vomited blood, screams and shouts erupted from every direction. Countless attacks poured toward me.

Swish-swish-swish! Boom-boom-boom!

Front, back, left, and right. Thirty-six directions.

Watching the rays of light shoot toward me from every side, I let out a hollow laugh.

Three jiazi of Scorching Yang Qi rose from my dantian and entered my spear, becoming a fire dragon.

Fire Dragon Divine Spear, First Form: Fire Dragon’s Single Tail.

Fwoosh! Whoooosh!

I smoothly rotated my body and swung the spear. At the same time, flames surged upward in a whirl, blocking and burning everything in their path.

The instant I stepped forward without hesitation, the marble beneath my foot crumbled like sand.

Sssshhh!

A fierce wind brushed past my ears. Someone’s desperate shout mingled with it.

“Stop him—!”

Boom!

The explosive roar swallowed the rest of the voice. Dozens of tanks who had frozen in place to block my path were flung away, their screams filling the silence.

“Guh!”

“Graaaah!”

Their bodies were as hard as steel, and they had learned through hundreds of raids how to fight.

But none of that was of any use at this moment.

Overwhelming power was enough to crush and destroy everything that stood in its way.

Yet the Hunters in the lobby, who had turned against me after wavering, continued rushing at me without rest.

The weapons in their hands flashed as they caught the light of the half-shattered chandelier, surging toward me from every direction.

Pap-pap-pap!

Cheeks, throats, armpits, waists, and calves…

I saw and felt everything.

It wasn’t only my body that had transcended human limits.

Before my brain could even send the information pouring in through my keenly sharpened senses to my body as a thought, I was already moving.

Crack!

I trapped the arm of someone wielding a sword beneath my armpit and broke it.

Thud!

I struck another person in the solar plexus with my elbow and knocked them down.

Tap—swish-swish-swish!

I snatched an arrow flying toward my throat and flung it back the way it had come.

The instant I turned toward the enemies closing in from all sides, short screams pierced my ears.

“Gah!”

“Ugh!”

This wasn’t happening in only one place. Screams continued pouring out from all across the lobby.

Every time I dodged a flying weapon, thrust out a fist or foot, or swung the shaft of my spear, someone screamed as their body collapsed or was flung away like a cannonball.

“Don’t hesitate! Fight!”

Boom! Whooooom!

“Take him down all at once!”

Swish-swish-swish!

A battle of two hundred against one.

No—a raid launched for the sole purpose of fighting one human being. But the ones retreating were not me. They were the others.

Magic? Weapons?

Nothing could touch me. I plunged deep into their formation and tore through it like a madman, destroying it from within. Not enough to stop their breathing.

But enough to carve a fear into them that would keep them from charging at me again before today’s battle ended.

Crack-crack-crack!

“Graaaah!”

Boom!

Before one person’s scream had even ended, three people fell. By the time three screams rang out, five had collapsed.

They were sheep, and I was no different from a great tiger.

There was one difference.

I had the patience to restrain the slaughter.

*I’m not a monster. I’m not a monster.*

I had to repeat it endlessly in my mind to calm the rage swelling inside me to the point of bursting.

Those who crossed to the other side of the river never returned.

Jopil had done so. The forces of Dark Heaven had done so. And Go Jun, who had stepped into the realm of monsters for the sake of his purpose, had done so as well.

But I was a Hunter. I was a Murim martial artist.

I suddenly remembered something a certain person had once told me—a person who had gone from being the greatest assassin of all time to the greatest physician under heaven.



*The weak kill people, but the truly strong can get by saving lives. It means that, no matter the circumstances, they can prevent innocent deaths.*



If I had been weaker than I was now—if I had been weak and evil at the same time—they would all have died.

But I was a human being, not a monster, and I had the power to save lives.

“Everyone… move aside.”

Boom!

The palm force I thrust out swept away dozens of people and sent them flying.

Perhaps it was because of the battle that had continued without pause for several hours, or the aftermath of One Annihilation. I was endlessly exhausted and worn out.

But contrary to that, everything was slow and clear. Their movements. Their expressions. I could recognize every single detail.

The mages’ staffs shining amid the fragments of the Tower Shields shattered into pieces were no different.

Vrrrrrrm!

The Magic Gems embedded in the heads of the staffs vibrated faintly and emitted a dazzling radiance.

But before the Magic could even take complete shape, I had already plunged between the roughly twenty mages.

“Ma—Magic Shi—!”

Unfortunately, it was already too late.

Swish—thump!

A mage hurriedly attempting to cast a defensive spell collapsed, his body stiff and rigid.

No, he wasn’t the only one who fell.

The instant ten fingers released ten streams of Finger Qi that brushed past their acupoints, the mages crumpled like a wall giving way.

But this was Ares Guild’s headquarters, a place said to select only the best of the best.

It was filled with so many high-ranking Hunters that ordinary Hunters rarely even encountered them.

“Binding!”

Shrrrriiiip!

Between the broken marble, vines burst from the wall where an unknown oil painting had once hung and wrapped around my ankles like whips.

Crack!

A magical rope appeared from the empty air and bound my wrists with tremendous force.

Was he perhaps the Team Leader commanding the mages?

An A-rank mage I had once seen on television spoke, killing intent burning in his eyes.

“Kill him.”

At that moment—

Swish!

The air above my head rippled, and a pale shadow like mist dropped toward the crown of my head.

Realizing that the sound cutting through the air came from a short sword, I let out a hollow laugh inwardly.

*Look at these bastards.*

I realized two things.

First, Code Red meant that the target was to be dealt with regardless of whether they lived or died.

And second, there was no reason to hold back against people who were truly trying to kill me.

*In that case…*

I welcomed it.

Boom!

The instant a short flame erupted, the assassin was flung away with his limbs twisted, unable even to scream amid the explosive roar.

Reflected in the wide-open eyes of the A-rank mage was the sight of me burning away every rope and vine while casually turning over the assassin’s short sword in my hand.

“What are you doing? Why aren’t you using Magic?”

“I-Ice Blo—!”

Crash! Thunk!

The short sword shot forward like a ray of light, shattered the Magic Gem in the staff, and plunged deep into the mage’s abdomen.

The pain that came with the backflow of mana must have been tremendous.

I struck the chest of the mage, who was screaming loudly enough to shake the lobby.

Boom!

The Inner-Family Heavy Hand was fatal to anyone, but it possessed even greater destructive power against those who directly handled mana, such as mages and healers.

In that sense, even if the man now lying unconscious with his eyes rolled back survived, his days as a mage were over.

I stared calmly at the mage, unconscious with an irrecoverable injury, and suddenly opened my mouth.

“Anyone else want to retire while we’re at it?”

“……!”

“If not, go to sleep.”

Swish-swish-swish! Thump!

As another volley of Finger Qi flew out, the remaining mages collapsed obediently, and silence fell over the lobby.

The clock hanging directly ahead told me that only three minutes had passed since the battle began. Yet of the roughly two hundred Hunters, fewer than one in ten were still standing on both feet.

Wheeeeeeeeeeng!

Beneath the unending, piercing alarm, the scene was horrific.

The tanks were embedded in the walls, the damage dealers were gasping in pain, and the mages lay rigid, staring only at the ceiling.

And then there was me.

I stood over them all.

My voice came out through parted lips, hoarse and cracked.

“Don’t ever stand in my way again. There won’t be a second time.”

“……!”

“……!”

The survivors and the fallen alike stared at me with trembling eyes.

They must have realized it by now. The reason they were still alive was not that they had been lucky.

Step.

Amid the blaring alarm and the people swallowed by silence, I slowly moved forward and stopped in the center of the lobby.

Then, channeling three jiazi of internal energy, I kicked off the ground and shot upward.

Screeeeech!

The lobby ceiling rushed toward me with the fierce wind. At the same time, blue-white flames flickered over my clenched fist.

The Flame-Extinguishing Divine Fist burst forth, burning through the air.

Kuwaaaaaang!

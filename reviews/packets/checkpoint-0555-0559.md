# Checkpoint Review — 555–559

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

# Chapters 555–559

## Plot

Go Jun confronts Prime Minister Jang Taekhwan before Lee Jungryong’s national funeral and forces him to arrange a private meeting with the President. Now Ares Guild’s Vice Guild Master and Lee’s chief mourner, Go Jun presents himself as the guardian of Lee’s legacy while secretly swearing vengeance against Jin Taekyung and Choi Minwoo. He also acquires a battered necklace from the ruins of the Arch Lich’s stronghold, believing it to be significant despite its not being Lee’s keepsake.

An unidentified Hunter party becomes trapped in a low-level Gate after it erupts with overwhelming mana and transforms into a Mutated Gate. Jin Taekyung and the Skeleton King enter the crisis, rescue twenty low-level Hunters, and are forcibly transported into a jungle-like Gate containing a Cyclops and hundreds of corrupted Ents. Taekyung creates the Unexpected Quest Forest of Giants, activates One Against a Thousand, and battles the Level 130 Named Monster ‘Red Eye’ Cyclops while the Skeleton King protects the unconscious Hunters.

After the incident, Team Leader Lee Seungyeop awakens in an ambulance and learns that his entire team survived. At the Peace Guild, Taekyung learns that Mutated Gates are appearing with increasing frequency. Magic Johnson arrives and gives Team Leader Choi thirty-two recordings of recent Gate disasters: two Monster Waves and thirty Mutated Gates, all occurring within one week. One concealed Mojave Desert incident killed twenty-two people and injured thirty-five at a restricted military base. The United States Ministry of National Defense suppressed the event, forcing Taekyung to confront the same moral dilemma surrounding Dark Heaven’s existence: whether dangerous truths should remain hidden until the public is prepared.

## Continuity

- The Fire Dragon Pavilion’s six-member mission remains underway: Jin Taekyung, Ju Hwaran, Song Ilseom, Sama Pyo, Taishan, and Hyuk Mujin are traveling secretly from Henan to Nanman through the Journey to Nanman Quest.
- Taekyung and the Skeleton King have survived the Forest of Giants encounter. The twenty rescued Hunters remain unconscious but alive inside the Skeleton King’s reinforced bone barrier; the Mutated Gate’s final status is unresolved.
- Taekyung destroyed many Corrupted Ents and confronted the Level 130 Named Monster ‘Red Eye’ Cyclops. The Skeleton King fought the remaining Ents.
- Go Jun is Ares Guild’s Vice Guild Master and chief mourner for Lee Jungryong, with dozens of A-rank Hunters under his command. He intends to preserve Lee’s legacy and treats Taekyung and Choi Minwoo as enemies.
- Team Leader Choi still plans to acquire Ares Guild’s reputation, influence, and power before removing Lee’s corruption. He knows Taekyung is concealing his identity.
- The Peace Guild is piloting a free emergency rescue service for capital-region Hunters, including transport, treatment, and psychological counseling. Song Song is its temporary leader, and Taekyung is the program’s patron.
- Magic Johnson, one of humanity’s three Grand Mages, has supplied Choi with evidence of thirty Mutated Gates and two Monster Waves occurring worldwide within the past week.
- Mutated Gates and Monster Waves are accelerating, while governments are concealing at least some incidents. The cause of the outbreaks remains unknown.
- Dark Heaven’s second rift, the Lord of Heaven’s identity, Dark Heaven’s method of opening Gates, and the relationship between Mutated Gates and Dark Heaven’s mutants remain unresolved.
- The Southern Heaven Demon Empress may be moving toward Nanman, where Song Ho’s dispatch has gone unanswered. The outcome of Jeok Cheongang’s duel with Nangong Cheon and the reason for Ju Hwaran and Sama Pyo’s broken engagement also remain unresolved.

## Translation Decisions

- Render 변이 게이트 as **Mutated Gate**, 몬스터 웨이브 as **Monster Wave**, 거인의 숲 as **Forest of Giants**, 돌발 퀘스트 as **Unexpected Quest**, 사이클롭스 as **Cyclops**, 엔트 as **Ent**, and 타락한 엔트 as **Corrupted Ent**.
- Render 일기당천 as **One Against a Thousand**, 거인의 포효 as **Giant’s Roar**, 붉은 눈 as **Red Eye**, and 치코리타 as **Chikorita**. Retain the abrupt taunt “Welcome, Chikorita.”
- Render 대마도사 as **Grand Mage**, 순간이동 as **Teleportation** in narration, and 텔레포트 as **Teleport**.
- Render 국가장 and 국장 as **national funeral**, 상주 as **chief mourner**, 유지 as **dying wish**, and 아크 리치 as **Arch Lich**.
- Retain **Nanman**, **Nanman Beast Palace**, **Fire Dragon Pavilion**, **Pavilion Master**, **Murim Alliance**, **Dark Heaven**, **Five Kings Hall**, **Peace Guild**, **Ares Guild**, **Skeleton King**, **White Flame**, **Finger Qi**, and **Scorching Yang Qi**.
- Preserve Taekyung’s dry profanity and self-mockery, the Skeleton King’s archaic insults, Magic Johnson’s and Im Kkeokjeong’s banter, and the unresolved moral tension over concealing public threats.

## Durable state

{
  "active_continuity": [
    "The Fire Dragon Pavilion’s six-member first mission is entering Nanman through the Journey to Nanman Quest, whose reward is a linked quest and whose failure penalty is the Title Can’t Go to Nanman; the party secretly departed Henan.",
    "Taekyung is a Supreme Peak master with Three Flowers Gather at the Crown, advanced Qi Sense, exceptional resistance to monster Fear, public S-rank-level recognition while retaining an A-rank license, leadership of the Fire Dragon Pavilion’s first mission to Nanman, and the Peace Guild’s modern-world patronage.",
    "Mungyeong ended Taekyung’s direct training and assigned him the final task of incorporating martial principles into his learned martial arts; Cheongpung accompanies Mungyeong and learns through observation.",
    "Mungyeong considers Nanman a plausible site for Dark Heaven’s second rift, while Dark Heaven remains a monster-like threat capable of causing rifts and creating mutants; the mechanism behind Jang Sam’s transformation remains unresolved.",
    "The Mount Song Resolution restored the Murim Alliance with Mae Jonghak as Alliance Leader and Jeok Cheongang heading the Five Kings Hall; Zhuge Feng’s Demon-Sealing Formation still blocks mana from the exposed Gate while Jang Taebo processes the Water God Dragon’s remains.",
    "The Southern Heaven Demon Empress is believed to be moving toward the suspected next target, while Song Ho’s dispatch there has received no reply for more than seven days.",
    "Taekyung is in the modern world on January 1, 2047, staying with Kim Jeonghee and Hayeon at Team Leader Choi’s mansion, where Cheon Taemin once lived.",
    "The public believes the Lich killed Lee Jungryong and Wu Heixing; Lee is being honored as a Great Cataclysm hero, while Taekyung knows the actual deaths were caused by him.",
    "Go Jun is now Ares Guild’s Vice Guild Master and chief mourner for Lee Jungryong, with dozens of A-rank Hunters serving as his new subordinates; he intends to preserve Lee’s legacy and regards Jin Taekyung and Choi Minwoo as its enemies.",
    "Team Leader Choi deliberately revealed his connection to Cheon Taemin as the old hero’s only living blood relative and intends to acquire the Ares Guild with its influence intact before removing Lee’s corruption.",
    "Go Jun possesses a battered necklace recovered from the ruins of the Arch Lich’s former stronghold; it is not Lee Jungryong’s keepsake, but Go Jun bribed an investigation leader to obtain it because he considers it meaningful.",
    "The Peace Guild is piloting a free emergency rescue service for Hunters in the capital region; Mutated Gates are increasing sharply in Korea, while Magic Johnson’s obtained US materials document thirty Mutated Gates and two Monster Waves from the past week."
  ],
  "continuity_sources": [
    559,
    558
  ],
  "open_questions": [
    "What is the Lord of Heaven’s identity, how is he connected to the dangerous force Taekyung associates with his original world, and how can Dark Heaven open Gates?",
    "What will Taekyung’s party find in Nanman, and what does the Southern Heaven Demon Empress intend there?",
    "What is the outcome of the duel between Jeok Cheongang and Nangong Cheon, and why did Ju Hwaran and Sama Pyo’s political engagement end?",
    "What process created Jang Sam’s mutant form, whether Dark Heaven’s mutants can absorb human energy, and whether it relates to the Mutated Gate?",
    "How many additional Gate disasters are being concealed, and what is driving the accelerating Mutated Gate and Monster Wave outbreaks?"
  ],
  "safe_through": 559,
  "temporary_decisions": [
    "Render 건량 as dry rations, 광서 as Guangxi, 대별산 as Mount Daebyeol, 만리행 as Ten-Thousand-Li Journey, and 고잉메리호 as Going Merry.",
    "Render 반 시진 as half a shichen and retain Nanman, Nanman Beast Palace, Fire Dragon Pavilion, Great Hero, and Young Lady Ju.",
    "Render 남만행 as Journey to Nanman, 남만을 못 가 as Can’t Go to Nanman, 면구 as disguise mask, 역용술 as disguise technique, 각주님 as Pavilion Master, 로그아웃 as Logout, and 동기화 as Synchronization.",
    "Render 일기당천 as One Against a Thousand, 거인의 포효 as Giant’s Roar, 타락한 엔트 as Corrupted Ent, 붉은 눈 as Red Eye, 치코리타 as Chikorita, and 대마도사 as Grand Mage; retain the established renderings for Small Cataclysm, Arch Lich, Skeleton King, Forest of Giants, Cyclops, and Ent.",
    "Render 순간이동 as Teleportation, 텔레포트 as Teleport, 변이 게이트 as Mutated Gate, 몬스터 웨이브 as Monster Wave, 모하비 사막 as Mojave Desert, and 애리조나주 as Arizona."
  ],
  "version": 1
}

## Reading copies

## Chapter artifact 555

# Chapter 555

He was a man with the build of an iron tower. His expression was flat and hard as stone, and his lips were pressed tightly together.

And then… there were his eyes.

A pair of bloodshot eyes. An indescribable mixture of rage and grief, along with several other emotions. Just looking into those eyes sent a chill down the spine.

Even the Prime Minister of Korea—a permanent member of the UN Security Council and one of the world’s great powers—was no exception.

*What the hell is with that look…?*

The Prime Minister flinched at the gaze that pierced into him like a blade the moment he entered the room, then forced himself to calm his trembling heart.

His opponent was one of the most skilled Hunters in Korea, but the Prime Minister himself had spent decades rolling through the political mud and was now sixty.

There was no reason to be intimidated before the conversation had even begun.

*Especially not in a situation like this.*

Having recovered some of his composure, the Prime Minister extended his hand toward the man.

“Oh, there you are. Mr. Go Jun.”

Go Jun stared blankly at the hand held out to him and answered in a dry voice instead of shaking it.

“It’s been a while, Prime Minister Jang.”

It showed neither proper respect for someone considerably older nor the appropriate conduct toward his country’s prime minister. Deep wrinkles gathered across Prime Minister Jang’s forehead.

“…Ha. I suppose you’re more grief-stricken than I expected. I understand how you feel.”

“Understand?”

Go Jun’s eyes grew even redder. No one could understand what he was feeling now.

And yet this old raccoon of a man had the nerve to smile and say something like that.

*Crack.*

The bones in his clenched fist shifted with an audible snap.

Once taciturn and as expressionless as a statue, Go Jun had become an entirely different man after the death of Lee Jungryong, the person he had respected and followed more than anyone.

“Ahem.”

Prime Minister Jang was not so oblivious that he failed to notice. He glanced nervously at Go Jun’s fist before lowering himself awkwardly into a chair.

“I seem to have misspoken. If I offended you, I apologize.”

“…It’s fine. I let my emotions get the better of me as well.”

Go Jun forced down his boiling anger.

He was no longer the orphan from thirty-odd years ago who had nothing left to lose. He had a mission to protect what his Master had passed down to him, and there was a mountain of work he had to deal with in order to fulfill it.

“But did you really come alone, Prime Minister?”

At last, the moment had come. At Go Jun’s sudden question, Prime Minister Jang answered as calmly as he could.

“I did.”

“Then where is the President?”

“I imagine you already know where he is.”

Prime Minister Jang glanced toward the tightly covered window.

The specially treated blackout curtains hid the view for now, but if they were drawn back, the Blue House would be visible immediately.

“The President has a great deal of work to deal with right now. He’ll come when the national funeral officially begins in three hours. I believe the presidential office already conveyed that to you…?”

Prime Minister Jang let his sentence trail off. Go Jun’s eyes sank into a deeper stillness.

“That’s why I asked again. I couldn’t believe what I was told.”

“What?”

“Prime Minister Jang. No…”

*Swoosh.*

Go Jun leaned his upper body forward from where he had been resting against the sofa.

The old politician’s reflection appeared in his red eyes, and a chilling voice slipped between his lips.

“Mr. Jang Taekhwan.”

“……!”

“Stop screwing around and let’s speak frankly. Go back and arrange a private meeting with the President right now. There are still three hours before the national funeral proceedings begin, so I’ll give you one hour.”

“H-Hey! How dare you—”

“How dare I?”

*Crsh.*

Prime Minister Jang’s eyes flew open. The sturdy crystal glass in Go Jun’s hand was crumbling into fine powder and spilling between his fingers.

At the same time, the change in Go Jun’s tone cut into the Prime Minister’s ears.

“That’s right—how dare you. You don’t get to act like this. Have you forgotten who paved the easy road you’ve walked all these years?”

“Y-You…”

The old politician’s voice trembled.

Go Jun was telling the truth. The name Ares Guild was an indelible stain on the Prime Minister’s decades-long political career.

They were the ones who had cleaned up the filth Prime Minister Jang left behind, wiped his ass, and loaded heavy boxes into his car trunk.

But…

“That—that was Vice Guild Master Lee Jungryong! Not you!”

“That’s right. It was all the Vice Guild Master’s doing. No—my Master’s.”

A dry smile touched the corners of Go Jun’s mouth.

“And now it’s my job.”

“……!”

“Don’t get the wrong idea. Even though he has passed away, the Ares Guild is still standing.”

The Ares Guild was an impregnable fortress.

Cheon Taemin, the immortal hero and savior who had rescued humanity, had laid its cornerstone, and Lee Jungryong had built an iron wall that no one could challenge.

“There isn’t a place in Yeouido—or in this country—where our hands can’t reach.”

This was a world ruled by the laws of capitalism.

None of the ten largest Guilds in the world appeared on the corporate rankings published in Forbes magazine every year, but everyone knew.

They knew the power and immense wealth held by the great Guilds. And among them, they knew the influence of the Ares Guild, one of the greatest of all.

And now…

That power would pass from the dead to the living.

“Do you think all he left me was his dying wish?”

“W-What?”

Prime Minister Jang’s eyes widened. According to the information he had received from the NIS, Lee Jungryong had left no will.

No—he was supposed to have left no will.

The ignorant public had been talking about it endlessly, but the Prime Minister had firmly believed the information he had received.

“Then you…”

For an instant, Go Jun’s eyes glowed red.

“You should call me Vice Guild Master, not ‘you.’”

“……!”

The old politician’s entire body trembled faintly. After a suffocating silence, Prime Minister Jang spoke in a weak voice.

“Mr. Go Jun. No, Vice Guild Master Go. The situation isn’t as simple as you think.”

The red light in Go Jun’s eyes gradually faded. His voice remained dry, but his tone softened somewhat.

“I know. That’s why our Prime Minister Jang needs to try harder. Along with the others.”

“Whew. That’s… not easy. There are also a number of rumors.”

“Rumors?”

“Hunter Jin Taekyung. No—I’m not trying to talk about him. Of course, he is connected to this to a considerable degree.”

Prime Minister Jang hurriedly explained himself after seeing Go Jun react immediately to the name Jin Taekyung, then continued.

“You already know about the young Team Leader from the Peace Guild, don’t you? His name is Choi Minwoo, I believe.”

“…Go on.”

“Ever since the late Vice Guild Master Lee Jungryong passed away, people around us have been saying all sorts of things. Even if there is someone to succeed him, it’s true that the Ares Guild isn’t what it used to be.”

Lee Jungryong had been a symbolic figure all by himself.

He was a hero who had suppressed the Great Cataclysm at Cheon Taemin’s side, as well as an S-rank Hunter counted among the very best in the entire world.

The Ares Guild would not collapse in an instant simply because he had died, but it was only natural that its strength and influence would be greatly reduced.

*Damn it.*

Go Jun knew that better than anyone. No—he knew it better than anyone else.

The noise and resistance coming from various places inside the Guild were proof enough. So was the attitude Prime Minister Jang had dared to display—an attitude that would once have been unthinkable.

*If Master had been here. If Master were still alive…*

The mutter that hovered at the tip of Go Jun’s tongue never escaped his lips.

He could not show himself wavering any longer. Having made that resolution, he spoke with his face hardened like stone.

“Prime Minister Jang seems to have plenty of worries and plenty of time.”

“What does that—”

“That’s something the Ares Guild will handle. You should do what you need to do, Prime Minister.”

“No, that’s not what I—”

Go Jun stared silently at the Prime Minister trying to make excuses, then leaned back against the sofa.

“Fifty minutes.”

“F-Fifty minutes? What do you mean?”

“Ten minutes have passed since the one hour I mentioned earlier, so that leaves fifty minutes. It seems you no longer have time to sit around here. Am I wrong?”

“……!”

The meaning was clear: Prime Minister Jang was being ordered to arrange a private meeting with the President by any means necessary before the national funeral began.

Prime Minister Jang rose on trembling legs and turned toward the door. A quiet voice reached his ears.

“One more thing. That person… the Guild Master won’t be coming. Keep everyone in line so there’s no gossip.”

What more was there to say?

Prime Minister Jang nodded weakly and left the room.

*Click.*

The sound of the closing door echoed unusually loudly.

Go Jun stared silently at the empty space, then his gaze shifted toward his left arm.

A mourning band marked with two black stripes. With no suitable blood relative to serve in the role for Lee Jungryong, Go Jun had become the chief mourner.

*Master. Are you at peace there?*

Go Jun could not even remember his parents’ faces, yet he desperately missed the face of Lee Jungryong, who had not shared a drop of his blood.

He would probably never forget his Master for the rest of his life.

Nor would he forget the two names that clung to him like tags.

“…Jin Taekyung. Choi Minwoo.”

The man who had killed his Master.

And the man who intended to take everything his Master had built.

The voice that escaped through his clenched teeth was hot, and his eyes burned redder than ever.

Still trembling with rage, Go Jun suddenly reached up and touched his neck.

*Clink.*

His fingertips brushed against cold metal.

Go Jun unclasped the necklace and stared down at it in silence. Its plating had worn away in places, leaving it with an ugly, battered appearance.

*Master.*

He knew.

This necklace was not Lee Jungryong, nor was it a keepsake he had left behind.

But one thing was certain.

It was the only thing fortunate enough to have retained its shape amid the ruins that had once been the Arch Lich’s stronghold.

It was nothing more than a worthless trinket, but to Go Jun, it had been worth bribing the head of the investigation team with a fortune to smuggle it out.

“…Whew.”

Go Jun let out a deep sigh and rose from his seat.

He was the chief mourner at this grand funeral.

He had to greet the countless people waiting for him outside, appear before media outlets from around the world, and show them who the new power behind the Ares Guild was.

*Click.*

When he opened the door, dozens of men and women standing in formation along the hallway lowered their heads.

Their eyes were intense, and every small movement was filled with power, as though each one were proving that they were an A-rank Hunter.

These were Go Jun’s new hands and feet.

“Let’s go.”

At Go Jun’s quiet command, dozens of pairs of footsteps crossed the hallway.

* * *

The national funeral of Lee Jungryong, the former Vice Guild Master of the Ares Guild, was held on a grand scale for five days.

Media outlets and powerful figures from around the world traveled to Korea, while hundreds of thousands of citizens took to the streets to mourn throughout the funeral.

But not everyone mourned.

For people who were hungry today, someone else’s death was not something that touched them very deeply.

*Slash!*

*Stab-stab-stab!*

“Kill it! Stab it now!”

“Keep your distance! Hey, you bastard! Don’t rush out!”

—Kieeeek!

Inside a damp, dark cave, shrill cries rang out.

Weapons whose shine had been dulled by deliberately coating them in mud moved without pause, seeking to cut off the enemy’s breath.

*Whoosh—thud!*

“Seongha!”

“You monster bastards!”

—Kik. Kiririik!

The battle between the Hunters and the monsters was fierce—and, in its own way, desperate.

Then, just as the blood of the two species, each a different color, spurted in every direction—

*Rumble-rumble-rumble!*

The earth shook, and stalactites fell from the ceiling of the cave.

At the same time, powerful mana erupted from somewhere and swept through the Gate. The humans cried out.

“A Mutated Gate!”

“Fuck…”

This was not mana that could come from a low-level Gate.

At least mid-level.

No—high-level.

Maybe even higher.

*Th-This is…*

*It’s over.*

Just as despair descended before everyone’s eyes alongside the word *death*—

“Fuck. Brings back old memories.”

Someone’s sighing voice echoed through the pitch-black cave.
## Chapter artifact 556

# Chapter 556

*Whew.*

I swept my gaze around with a sigh.

A damp, chilly cave. Narrow passages tangled together like a maze, with sharp stalactites hanging from the ceiling. Faces exhausted and terrified out of their minds.

*Just like back then.*

Three years ago. No—if I included the time I’d spent in Murim, it had been four years.

The accident that day remained seared into my heart like an indelible brand, and even now, after taking my revenge, I still couldn’t completely forget it.

“Fuck. This brings back memories.”

Unlike me, who muttered the words thickly under my breath, the Skeleton King smiled fondly.

“I feel the same. It is as though I have returned to what you humans call one’s homeland.”

“……”

You’ve got it wrong, man.

It seemed like we were remembering entirely different things.

For all I knew, this guy might have been Skeleton One—the skeleton I had encountered while spending day after day in low-level Gates.

*Anyway…*

*Rumble-rumble-rumble!*

*The mana wave is much stronger than I expected.*

It was lucky we had been nearby. Otherwise, twenty hardworking living people would almost have been wiped out.

I waved toward the Hunters staring blankly in our direction.

“It’s dangerous, so come over here.”

A man in his late twenties who appeared to be the Team Leader blinked.

“W-What?”

“I said come over here. Hurry.”

“W-Who are you?”

The cave was dark, and they were standing a considerable distance away. Their level was far too low for them to make out my face from that far.

I awkwardly scratched my chin before opening my mouth.

“I’m… Uh, look behind you.”

“What?”

Their reaction was slow. Instead of answering, I snapped my fingers.

*Whoosh—boom!*

With a faint whistle through the air, green blood splattered in every direction. At the same time, a rusty ax slipped limply from the hand of a goblin approaching one of the Hunters from behind.

Then the headless body collapsed like a rotten log.

*Thud!*

“Gah!”

“Behind you! Watch your backs!”

“What the hell is this?”

What else would it be? Finger Qi.

I muttered inwardly as I watched the Hunters hurriedly reform their ranks, then realized something.

*It’ll be faster if I go to them than if they come to me.*

Judging by how they were floundering against goblins before they’d even made it halfway through the Gate, they weren’t just low-level Hunters—they weren’t particularly experienced, either.

The Skeleton King swept back his blond hair and put on a solemn expression.

“Hmph. It seems the time has come for this body to take the field.”

“Stay put. Don’t get cocky.”

“……”

Now that I knew what needed to be done, there was no reason to hesitate. I walked toward them at a pace that was neither hurried nor leisurely.

*Step.*

One step.

At the same time, ten streams of Finger Qi shot through the air from my wide-open hands.

*Whoosh—thud-thud-thud-thud!*

One more time.

*Whoosh-whoosh-whoosh!*

Again.

*Boom!*

By the time the last one—a hobgoblin who looked like the leader—fell, nearly thirty goblins had become headless corpses sprawled across the ground.

And then…

*Step.*

With my third and final step, a sphere of light summoned by an unknown mage using Light magic illuminated my face.

*Flash.*

“……!”

“……!”

An invisible shock wave and wave of agitation swept through the cave.

Everyone was staring at my face with vacant expressions when, like a dam suddenly bursting, cries erupted from every direction.

“L-Lord Fuck!”

“Lord Sibu-leol!”

“J-J-Jin Taekyung!”

The last one was at least better.

The stutter might have stretched my name to six syllables, but compared to the nicknames that came before it, it was downright respectable. About as respectable as a deputy minister.

Come to think of it, the name fit the current situation pretty well.

The vibrations had steadily intensified, and now the whole cave was sh-sh-sh-shaking like a fucking earthquake.

*Rumble-rumble-rumble!*

The Skeleton King sauntered over, dodging a stalactite dropping from above, and muttered,

“This much commotion is most unsettling.”

“Tell me about it.”

The mana here was as far removed from the mana of this Gate—which was E-rank at best, or perhaps F-rank—as Henan was from the Nanman Beast Palace.

I clicked my tongue softly and waved toward the still-stunned Hunters.

“As I said before, it’s dangerous, so come over—”

*Patter-patter-patter-patter!*

“Whoa. You startled me.”

“Undead, have mercy.”

What was this? A Blink spell?

There were certainly advantages to being famous.

Even some old lady named Kim living in the middle of nowhere had probably heard my name. How could Hunters in the same profession not know me?

Before I could finish speaking, all twenty Hunters came running at the speed of light. They stared at me with eyes full of fear and trust.

“Hyung. I’m a fan. A genuine fan.”

“Eek! What do I do? What do I dooo?”

“……I appreciate it, but are you all out of your minds?”

Apparently, they could say things like that in a situation like this. I shook my head in disbelief and searched for the Team Leader.

At least he seemed to understand how serious the situation was. His face rigid, he rummaged through his pocket and handed me something.

“Could I get your autograph? Please write, ‘Go, Hunter Lee Seungyeop!’”

“……”

“Please. I’ll preserve it as a family heirloom and pass it down for generations.”

“……”

Ah. Fuck. I was speechless.

With a miserable look on my face, I scrawled my signature across the briefing board. The Team Leader cautiously added,

“And if it wouldn’t be too much trouble, could you swear once?”

“What?”

“Swear at me. It’s my lifelong wish.”

“……You fucking bastard.”

“Thank you! Thank you!”

“I was serious.”

“Gasp.”

And there was one person—or rather, one monster—watching the scene with profound envy.

“You are rather popular. Wretched human. They say that if one defecates, one becomes famous and the people applaud.”

“……”

Something about that order seemed backward.

Defecating in public might make you famous, but wouldn’t people usually slap you instead of applauding?

Unfortunately, I didn’t have enough time to correct the Skeleton King’s distorted understanding.

The moment I was about to speak, a sudden movement swept through the cave, which had been shaking as if an earthquake were taking place.

*Rumble-rumble—crack!*

The ground split apart, while cracks spread across the ceiling like a spiderweb. One of the Hunters muttered with a groan,

“Collapse…?”

Half right. Half wrong.

While everyone stared at the ceiling, which looked ready to come crashing down at any moment, I was the only one who knew what was happening below as well.

*Crack. Crack-crack.*

A sprout pushed its way through the solid rock covering the ground.

It was dark red, and even as I watched, it grew at a terrifying speed.

Thorns formed. A flower bud burst open. Then the seeds it scattered began spreading in every direction.

*Crack-crack-crack-crack!*

“W-What is that?”

“Eeeeeek!”

“Ugh!”

“Cut it! Chop it down!”

The Hunters had finally noticed what was happening and sprang into action.

But their screams and frantic swings did nothing to stop the undergrowth as it continued stretching endlessly outward.

Because this wasn’t happening only here.

Even if the Skeleton King and I joined in, there was no way we could travel through the entire Gate and deal with all of it in this short a time.

*This is…*

This wasn’t a simple collapse.

It was a transformation.

The entire Gate was changing into an entirely new form.

*Mutation. In the truest sense of the word.*

As the people watched in horror, the Mutated Gate was nearing the end of its final transformation.

*Rumble-rumble-rumble. Boom!*

The hairline cracks spreading across the ceiling darkened, and the gaps opened wide.

It looked as though a gigantic egg in the shape of a cave were breaking apart.

And then…

*Crack!*

Beyond the ceiling, where nothing should have existed, something emerged, wreathed in red light and a murky mist.

A vast space that dwarfed the cave. Dense vegetation. A sweltering temperature like a wet sauna.

“What is that?”

“I-Is it a jungle?”

Everyone was too shocked to speak. Then the Skeleton King whispered in a voice only I could hear.

“Wretched human. This body’s power is growing stronger.”

Although he was hiding his true appearance with illusion magic, the Skeleton King’s true nature was that of a monster.

If his power had grown stronger, that meant only one thing.

*The quantity and density of the mana.*

I couldn’t see it.

But I could feel it.

*Whoosh…*

The immense mana consuming every inch of space.

The mana had swelled to the point of bursting, pressing down on the jungle.

It was a level of mana that would be difficult to sense even in an A-rank Gate. There was no chance ordinary low-level Hunters could withstand it.

“Hhk. Hhk.”

“I-I can’t… breathe…”

Their pupils slowly unfocused, and their bodies staggered.

Not one of the twenty Hunters was spared. One after another, they fell unconscious at an alarming rate.

The Skeleton King frowned as he watched me calmly stand there.

“Wretched human. You…”

“This is better.”

“What?”

“There’s no point in letting them stay awake.”

“……!”

I had to conceal the Skeleton King’s existence as much as possible. If so, it was better to remove these people from the situation from the beginning, as long as doing so didn’t endanger their lives.

The fewer witnesses, the better.

*Thud.*

When the last person finally lost consciousness, the Skeleton King nodded at my signal and snapped his fingers.

*Crack-crack-crack!*

Countless bones rose from somewhere and tightly surrounded the Hunters without leaving a gap. The Skeleton King spoke with a smug expression.

“Done. Since this body has personally demonstrated its abilities, the safety of those humans is guaranteed.”

I studied the small dome-shaped barrier and muttered,

“I don’t know. I think it needs a little more reinforcement.”

“Tsk, tsk. What a wretched and distrustful human you are. Even if a horde of ogres attacked, this would not budge.”

Ogres were monsters whose terrifying strength was always considered among the highest, regardless of their Grade.

But even despite the Skeleton King’s boast, my opinion did not change.

“It’d probably be fine against ogres. But those things look a little different.”

“Huh?”

The Skeleton King turned his head with a foolish expression.

In the vast jungle, something was slowly rising to its feet.

Twenty meters tall.

Arms and legs thicker and longer than the countless giant trees filling the jungle.

And…

A gigantic single eye gazing down at the earth.

A Cyclops.

The one eye of the mythical giant, its entire body wrapped in mist, turned toward us.

Then a chilling voice boomed like thunder.

—Intruders. Humans. Kill.

And the next moment—

> **System**
>
> You have been forcibly moved to the Mutated Gate!
>
> An Unexpected Quest, **Forest of Giants**, has been created.

*Rumble-rumble-rumble!*

Along with the System notification drilling into my ears, the jungle shook.

No. It would be more accurate to say that it came alive.

*Flap-flap!*

Beneath the wingbeats of nameless birds shooting into the sky, something rose with a monstrous cry.

It was none other than hundreds of trees.

Ancient tree spirits featured in countless tales. The Ents awoke from their slumber and roared.

—Gwoooooar!

—Grrrrrrrr!

And there was one person—or rather, one monster—who had been silently watching the entire scene.

He quickly changed his mind.

“……I shall reinforce the humans’ barrier.”

“Uh, yeah.”

*Crack-crack.*

Countless bones, far more numerous than before, shot upward and piled atop one another in layer after layer.

After carefully completing the reinforcement, the Skeleton King stared solemnly at the jungle advancing toward us.

“Ready, Jin?”

“Of course, King… Wait, where the hell did you learn this kind of thing?”

“The internet. It is entertaining.”

“You bastard. Once we get out of here, I’m confiscating your phone first.”

After threatening the Skeleton King, I muttered under my breath,

“Inventory open. Summon.”

At the command, the shaft of White Flame appeared in my empty hand.

The familiar sensation was one I hadn’t felt in a long time.

As I looked around at the surroundings that had transformed into a battlefield, a smile suddenly touched my lips.

*Let’s go.*

*Whoosh.*

Three jiazi of Scorching Yang Qi surged up from my lower dantian, transformed into a fire dragon, and spread through every limb and bone in my body.
## Chapter artifact 557

# Chapter 557

*Whew.*

My breath mingled with the muggy air of the forest. Watching the enemies closing in from every direction, I quietly muttered to myself.

*Keep my center low. Keep my lower body firm. When launching an attack…*

*Be fierce. Without hesitation.*

*Flash.*

The instant I half-opened my eyes, I kicked off the ground.

*Bam—!*

Compressed air burst from my toes, and tremendous wind pressure swept over my entire body.

But my superhuman physique pushed through the pressure. My body tilted at an angle and shot forward like a cannonball, flying against the wind.

*Whoooosh!*

My hair whipped wildly around my face. The scenery rushed past in a blur amid the fierce wind.

The Skeleton King’s voice, shouting that he wanted to come with me, was swallowed by the sound of the air splitting apart.

The hundreds of monsters advancing through the deep, viscous swamp and trampling the dense undergrowth were suddenly right in front of me.

—Gwoooooar!

Hundreds of them.

Or perhaps hundreds of trees.

I didn’t know which word I was supposed to use to count those monsters called Ents, but at least one thing was certain.

*I’ll win.*

This wasn’t a guess. It was absolute certainty.

Even the Cyclops watching us from behind the Ents as though it were their king was no exception.

The three jiazi of mighty Scorching Yang Qi flowing through my entire body were proof of that certainty. I myself—standing here after defeating countless powerful enemies—was its witness. And the blue-white Force surging around the blade of White Flame was its judge.

The verdict was swift.

And destructive.

*Now.*

*Hiss.*

Blue flames evaporated the moisture around me. In a moment too brief to even call an instant, the transparent spearhead of White Flame had already swept diagonally across the Ents at the front.

*Shwaak!*

There was no explosive sound.

No scream.

There was only a single gust of wind, and the Extreme Yang energy clinging to the spearhead had drawn a faint line through the air.

The line resembled part of something that ought to exist only in legend.

*Fire Dragon Divine Spear. First form.*

*Fire Dragon’s Single Tail.*

Before I could finish muttering the four words that should have followed in my mind, the faint line suspended in the air began to ripple.

Blue-white flames that had been lying dormant awoke from their brief slumber.

*Fwoosh.*

The tiny embers flared to life.

The trunks, branches, and lush leaves of the Ents became kindling. The flames transformed into hellfire and devoured everything the line had touched.

*Kraaaaaash—!*

Blue-white light burst outward, illuminating every direction.

Where the flames had passed, the ground was blackened and melted. Hundreds of Ents stood rigid and motionless.

And somewhere in the distance, a clear bell rang.

*Ding. Ding. Ding.*

> **System**
>
> - Critical Strike!
>
> - You defeated **Level 95 Corrupted Ent Great Warrior**!
>
> - You defeated **Level 90 Corrupted Ent Vanguard**!
>
> - You defeated **Level 89 Corrupted Ent Vanguard**!
>
> - …
>
> - …
>
> - …
>
> - Since the level difference between you and the defeated targets is 20 or more, the EXP gained is reduced.
>
> - Since you defeated 20 or more **Corrupted Ents** with a single strike, bonus EXP has been awarded!
>
> - You obtained a large amount of EXP and Fame!

But the System notifications did not end there.

*Ding.*

> **System**
>
> - You have been surrounded by a great many enemies. But do not be afraid. It is not you who must retreat, but the enemy.
>
> - The effect of the Title **One Against a Thousand** has activated!
>
> - Number of identified enemies: 281
>
> - Since you are facing a large number of enemies, all your attributes will temporarily increase according to the number of enemies.
>
> - When fighting a large number of enemies, your Stamina consumption during battle is greatly reduced, and you will not easily feel fatigue!

**One Against a Thousand.**

Two months ago, I had single-handedly swept away the undead army serving the Arch Lich. The Title I had earned then was finally showing its worth.

*Ding. Ding. Ding.*

Along with the bells ringing one after another, all my attributes—including **Strength** and **Stamina**—rose slightly.

But that wasn’t the end.

One of the greatest effects of **One Against a Thousand** was its ability to maximize a single attribute.

> **System**
>
> - **Intimidation** has increased dramatically!
>
> - Your majesty and aura, rising like a wildfire, are overwhelming your enemies!
>
> - Your enemies are greatly intimidated by your **Intimidation**!
>
> - Your allies’ morale is greatly increased by your **Intimidation**!

*Intimidation.*

The power to suppress enemies and encourage allies. An ability that could change the flow of an entire battlefield instead of affecting only me.

The information the System had given me was not wrong in the slightest.

The encirclement that had been closing in from every direction began to falter. The thick branches that had been moving violently and relentlessly came to a sudden stop.

—Gwooooo…

The Ents—evil spirits dwelling within gigantic trees—let out timid cries.

Hundreds of pairs of black eyes trembled faintly between their hard bark.

*Fear.*

It was a familiar emotion.

Once, it had belonged to me.

Now it belonged to the enemies standing before me.

Feeling exhilaration welling up from deep within my chest, I took a step forward.

*Step.*

—Gwoooooar…

—Grrk. Gwooooo…

*Rumble-rumble-rumble.*

The Ents retreated as I advanced.

No—the entire jungle moved.

The mana released by the Ents as they gathered together was crushed beneath the aura and Intimidation radiating from my entire body.

*Strength. Momentum.*

Neither of the two factors that decided a battle could match me.

So there was no reason not to fight.

And no reason I couldn’t win.

Of course, there was still one variable.

—Kraaaaaaaar!

The Cyclops.

The roar of the mythical giant with a single eye larger than a boulder shook the entire jungle.

The Ents, which had been edging backward on their roots, flinched.

*Ding.*

> **System**
>
> - **Giant’s Roar** has activated!
>
> - The effect of **Intimidation** has been slightly neutralized!
>
> - Some enemies have escaped the pressure of **Intimidation**!

It was a fitting ability for the boss monster of this Gate.

But even the Cyclops couldn’t completely dispel my pressure, and I had no intention of giving it enough time to do so.

No.

Correction.

Not me.

Us.

“Haaap!”

*Krkrkrkrk! Pow-pow-pow!*

With a powerful shout, a spear of bone shot through the air and pierced the Ents.

The Skeleton King had arrived behind me at some point. He went completely berserk as he screamed,

“Come at me, you worthless monsters!”

“……”

This bastard had completely lost his identity.

And perhaps he was benefiting fully from the effect of **One Against a Thousand**, because the Skeleton King was so exhilarated that he charged forward without a thought.

“How dare you oppose this exalted body! Die! Die! Dieee!”

*Papapapat!*

The Skeleton King might have been a little off his rocker, but he was still a Named Monster who had undergone an entire evolution.

No one could deny the power he possessed. Bones erupted from the ground and the air, breaking branches without pause and piercing the Ents’ trunks.

*Pow-pow-pow!*

“How dare you wave those adorable little leaves before this body!”

*Craack!*

“No matter how many of you attack, it is nothing but an egg striking a boulder of bone!”

—Gwoooooar!

The plaintive cries of the Ents rang across the scene of forest destruction.

The Skeleton King’s intrusion had left the path completely empty, and I shot forward along it like an arrow.

*Whoooosh! Slash!*

As I passed through like the wind, I swept my spearhead in every direction. Flames crossed through the air, and the Ents vanished without even having the chance to scream.

*Ding. Ding. Ding.*

I twisted my body at the sound of the bells ringing loudly in my ears.

A tree trunk shot toward me with tremendous force, grazed my side, and pierced the ground.

*Boom!*

Mud burst out like an explosion.

I stepped on another trunk whipping toward me and lightly propelled myself into the air.

*Tap. Swish.*

My movements had become smoother and more precise after receiving Mungyeong’s teachings.

My body glided forward like a feather, and before I knew it, I had arrived before an unusually massive tree.

**Level 102 Corrupted Ent Elder**

—H-u-man! D-i-e!

Apparently, its level wasn’t the only thing that was high. It possessed considerable intelligence as well, since the Ent Elder could speak.

Without hesitation, I brought my spearhead down diagonally.

“Welcome, Chikorita.”

—……!

*Whoosh. Slash!*

The hundreds of branches it hastily gathered for defense were useless.

The thorns it shot at me were useless, too.

Along the path traced by my spearhead, the massive tree—with a circumference of several meters—slowly split apart.

*Crash! Fwoosh!*

The fallen tree burst into flames amid a thunderous roar.

I kicked off the stump, its dense growth rings exposed, and shot upward.

At last, I came face-to-face with the gigantic being blocking the sky.

**Level 130 ‘Red Eye’ Cyclops**

It was the one.

The master of this jungle.

A savage one-eyed giant that had made hundreds of Ents its slaves.

Its identity was finally confirmed. It was a Named Monster with a level higher than any monster that had served under the Arch Lich during the Small Cataclysm—and it even possessed an epithet.

*There’s a Named Monster in a low-grade Gate like this…*

My mood suddenly grew heavy, but I had to put that thought aside.

A gigantic shadow was plunging down from the distant sky.

*Whoom!*

A rock more than ten meters in diameter.

No—a boulder closer to a meteorite smashed through the wind as it fell.

And I chose to break through head-on rather than evade.

*Finish it quickly.*

I shot upward from below.

The rock plunged downward from above.

At the unavoidable moment of impact, I poured the Scorching Yang Qi within White Flame into the tip of my spear and thrust toward the exact center of the rock.

And then…

*Slash.*

The spearhead smoothly burrowed into the rock as though it were a hot knife cutting through cheese.

It rotated.

*Krkrkrk.*

The spear broke through a precise single point, and mighty Force tore through the rock’s interior.

A clear crack appeared across the surface of the massive boulder.

Then—

*Kraaaaaaang!*

With a thunderous roar, the rock shattered into hundreds and thousands of fragments that scattered in every direction.

—……!

The Cyclops opened wide its single red eye and staggered, unable to withstand the force.

*Rumble. Crack!*

—Gwoooooar!

The ground broke beneath the giant’s movements. Small-bodied Ents were trampled underfoot and screamed.

But neither the Cyclops nor I paid any attention to what was happening below.

Defeating the enemy in front of us.

That was all that mattered.

—Huuuuuu… maaaaan…

The Cyclops’s roar felt as though someone had slowed it to 0.1 speed.

In the slowed world, I stepped on empty air without hesitation and shot upward once more.

*Bam!*

**Stepping on Empty Air.**

Compressed air exploded beneath my toes, propelling me farther and higher.

*Whoooom.*

The Cyclops, sensing danger, swung its fist too late.

It was slow enough to make me yawn.

*Boom!*

The punch produced a terrifying sound as it split the air.

But when the giant’s fist slammed into empty space, I had already passed through and shot upward above its crown.

*Gooooong.*

Blue flames spread across the spearhead, which held immense Scorching Yang Qi.

A sharp yet destructive force.

The second and final form of the Blazing Flame Divine Spear, which concentrated three hundred years of the Fire Gate Clan’s macho spirit—the time-honored clan with absolutely no concept of retreat.

*Heavenly Strike.*

Blue flames descended upon the giant’s head.

*Shwoooooosh. Slash!*
## Chapter artifact 558

# Chapter 558

*Flash.*

The man suddenly opened his eyes.

For a moment, his dazed gaze stared blankly into the air. Then he slowly began retracing the memories that had passed.

*An F-Rank Gate, goblins, an earthquake, and…*

*Jin Taekyung.*

At that final keyword, which brought everything rushing back, the man remembered it all. He sprang up from where he had been lying like a released spring.

“Gaaaaah!”

There was just one problem: the space wasn’t very large, and the man had the kind of massive build expected of a tank.

*Thump. Bang!*

“Gah! Huh?”

After hitting his head on the ceiling and crying out, the man stopped and opened his eyes wide.

It hurt. It really hurt.

But feeling pain meant…

*I-I’m alive!*

He never thought he would be having the kind of thoughts usually reserved for webnovel protagonists.

Only after the tension finally drained out of him did the man realize that he had been lying inside a vehicle.

More precisely, an ambulance.

*An ambulance?*

Escaping the brink of death was fortunate, but it wasn’t exactly a good sign. If he had survived only to become disabled, that would be a misfortune too.

The man hurriedly came to his senses and began checking his entire body.

That was when—

*Bang. Rattle.*

The door flew open, and light poured in. The man covered his face with both arms.

Or perhaps the dazzling beauty of the woman who had opened the door was the real reason.

“Oh, you’re awake. I heard a strange noise while I was passing by.”

The man opened his mouth toward the beautiful woman who had appeared without warning.

“W-Who are you?”

“You’re Team Leader Lee Seungyeop, right? You’re a free agent with no Guild affiliation, and you’re thirty-three.”

“H-How do you know that?”

“Questions later. First, are you feeling all right?”

Her tone was gentle but firm enough to cut him off. The man reflexively nodded.

“Though you should be fine. All you had were abrasions—barely enough to call them injuries. The others…”

*The others?*

At that casually mentioned word, the man’s eyes snapped wide open.

“R-Right! My team! Are my team members all right? Did anyone die? Is anyone hurt?”

“Hmm. Your team members are all safe, but if you keep shouting like that, my ears won’t be.”

“Really? Are you sure? Guh, is that really true?”

“I know someone who always stakes something dirty in situations like this. I don’t have any testicles, so I’ll stake my ovaries. Does that work?”

Her answer radiated such effortless cool that her voice continued without pause.

“And to answer your earlier question, I checked your belongings. Thanks to that, we were able to complete your identity verification quickly.”

*Tap.*

What she set down was a small extradimensional Pocket and a briefing board.

A short message had been scrawled across the brilliant white surface in atrocious handwriting.

<br>

**Go, Hunter Lee Seungyeop!**

—Jin Taekyung

<br>

The beautiful woman quietly laughed.

“Actually, that had fallen on the ground, but someone personally handed it to me. He said it was something that would become a family heirloom, so you absolutely couldn’t lose it.”

Team Leader Lee Seungyeop’s eyes grew wide.

“Really? Then the person who gave it to you was…”

“If a certain name just came to mind, that’s the correct answer.”

Her neatly arranged eyebrows lifted. Her voice was as clear and refreshing as her features.

“Oh, come to think of it, I’m late introducing myself. I’m Song Song.”

“Song? What kind of song?”

“…”

“It’d be faster to give you my business card from the start. Here.”

*Swish.*

The Team Leader accepted the business card held between her long, pale fingers and opened his eyes wide.

“Peace Guild?”

“My official title is Healer Team Leader. I’m also temporarily in charge of the emergency rescue team.”

“…”

The Team Leader swallowed a breath.

No matter how busy he was making a living, he knew enough about the Peace Guild.

*You’d have to be a monster not to know.*

It was the Guild that none other than Jin Taekyung belonged to.

With its enormous financial resources and the kind of buzz that drew public attention, the Peace Guild had grown explosively within a few months. It was no longer some unremarkable small or medium-sized Guild.

*I heard it’s harder to get into the Peace Guild than Ares Guild these days.*

The Guild offered some of the best treatment in the industry, and its potential for future growth was limitless. Naturally, talent flocked to it.

After Lee Jungryong’s national funeral a week earlier, he had even heard that Hunters from Ares Guild had transferred to the Peace Guild rather than renew their contracts.

And the beautiful woman in front of him was a team leader-level figure in that Peace Guild.

For someone who looked barely into her twenties, she was quite a major figure.

Now that he thought about it, her celebrity-like face seemed familiar too. He might have seen her once or twice on television.

“But… what exactly is the emergency rescue team? I haven’t heard of it before.”

“Exactly what it sounds like. An emergency rescue team. It was newly established for the sole purpose of rescuing people.”

“I know that Guilds of a certain size have rescue teams. But neither my team nor I belong to the Peace Guild.”

Freelance Hunters and small Guilds received help from government agencies, while it was common knowledge that even medium-sized Guilds operated their own rescue teams.

He couldn’t quite understand why the Peace Guild had suddenly appeared.

“Does that bother you?”

“N-No. How could I possibly think that? Of course I’m extremely grateful. You saved us when we were about to die after being caught in a Mutated Gate.”

Song Song quietly laughed.

“Then that settles it. That’s why we came.”

“What?”

“Our Peace Guild emergency rescue team is being piloted primarily at medium- and low-grade Gates in the capital region. We’re working with government agencies, and the service is available to all Hunters. If I had to put it simply, you could call it volunteer work for public safety.”

“Volunteer… work?”

“Of course, I and the others are getting paid.”

He opened his eyes wide and looked over Song Song’s shoulder.

Even now, dozens of Hunters were moving busily in every direction. Every one of them wore the Peace Guild emblem on their chest.

*Volunteer work? With this many people?*

No matter how much of a golden goose a modern Hunter Guild was, most of its income ultimately came from Gates.

That was why Guilds paid Hunters enormous salaries and then generated even greater profits from Gates.

But the Peace Guild had sent these people out not for raids, but for rescue work.

And it was even paying them appropriate compensation.

*They all look like at least mid-grade Hunters.*

There were dozens of Hunters dressed in equipment that looked expensive at a glance.

As a low-grade Hunter, he had no way of guessing how much the Peace Guild had paid them all today.

“Um. You said your name was Team Leader Song Song, right?”

“Yes. Go ahead.”

“Th-There’s something I wanted to ask. Are there any treatment fees or rescue fees or anything like that?”

“There aren’t. Have you ever seen a firefighter rescue a citizen and then send them a bill?”

“Then…?”

“Obviously, everything from transportation to treatment is free. Oh, and if anyone has suffered psychological injuries, we also provide counseling. Trauma and things like that.”

“…”

*Wait a minute. What kind of treatment? Did I hear that right?*

He stared blankly at Song Song before asking with genuine feeling,

“Does the Peace Guild run on money it digs out of the ground?”

Song Song gave him a playful wink.

“Not exactly. Our patron has quite a lot of money.”

“Your patron?”

“You must know who I mean. You even got his autograph.”

“…”

“Anyway, there’s someone like that. He complains every day that he feels as though he’s being bled dry, but he keeps smiling.”

A smile formed at the corner of Song Song’s mouth as she thought of him.

When she had first met him, she had wondered what kind of lunatic he was.

But after watching him from nearby, she had come to understand.

What it meant to be a true Hunter.

What it meant to have a human heart.

<br>

*You. Let’s do a job together.*

*…That sounds like a line I’ve heard somewhere before. First, just know that I’m not ethnic Chinese.*

<br>

That was what Jin Taekyung had suddenly said to her a week ago.

For a moment, she had wondered whether he was asking her to join Gold Moon—or rather, Ares Guild—and work as a spy.

But what he said next was nothing like what she had expected.

<br>

*You’re better than I expected, Taurus.*

<br>

To be a little more honest, he had been kind of cool this time.

It had been the same when he used the money from selling the Black Wyvern’s carcass to establish a charitable foundation.

Every now and then, he showed her an unexpected side of himself.

*Heh.*

Song Song let out a quiet laugh, then suddenly turned her head toward the sky.

It was January, and the cold had not yet faded.

But the sunlight shining down from overhead was warm.

* * *

*Kiiiiing.*

—Jin Taekyung. Iris recognition complete.

A red light swept across my pupil as the mechanical voice rang out.

I stepped through the automatically opened door and entered the Guild House.

Everyone who had been moving around to handle their own work stopped dead, as though they had planned it together.

“W-Welcome.”

“Welcome!”

“Thank you for your hard work!”

“Ah, yes. Hello, everyone.”

*I told them not to do this. What is this, a gangster office?*

I gave an awkward smile at the sight I still couldn’t get used to. The Skeleton King whispered beside me.

“Wretched human. This seems somewhat inappropriate.”

“You, of all people? You have thoughts like that too—”

Before I could finish speaking, the Skeleton King strode forward and pointed at a Hunter who looked like a new recruit.

“You there. You’re only bending eighty degrees at the waist. Make it ninety. Or you could try a grandjeol.[^1]”

[^1]: A comically exaggerated form of the Korean full bow, often performed with the body inverted.

“Yes, yes! Understood!”

“…”

*Don’t adjust the angle however you feel like it. And what exactly do you understand?*

It was enough to make me lose my mind just by looking at it.

I stopped the Guild member from attempting a grandjeol and kindly advised him not to take anything this idiot said seriously. Only then was I able to head toward my destination.

And familiar faces were waiting for me there.

“Taekyung!”

“Welcome.”

The first was Im Kkeokjeong, who was welcoming me with both arms spread wide. The second was Team Leader Choi, who was busy handling something.

“Take it easy, Kkeokjeong hyung. Take it easy. What if you reopen your wounds?”

“I’m just happy to see you, punk.”

“We see each other every day.”

As soon as I sat Im Kkeokjeong down—he was still undergoing rehabilitation training—Team Leader Choi suddenly spoke.

“I received a report over the hotline. A Named Monster appeared?”

“It was a Cyclops. With three hundred Ents thrown in for free.”

“A Cyclops in an F-Rank Gate… It was a stroke of luck that Mr. Jin Taekyung happened to be nearby.”

The Skeleton King spoke with exaggerated dignity.

“They all knelt before this body’s majesty.”

“One more word, and you’ll learn to listen while kneeling.”

“…Sorry.”

That single sentence was enough to shut him up.

Team Leader Choi handed me a folder.

“What’s this?”

“The material you asked for last time. I compiled the number of Mutated Gates that have appeared recently in Korea and throughout Asia.”

It didn’t take long to look through the folder.

A short while later, after confirming everything I wanted to know, I muttered like a groan,

“Five times in Korea alone over the past month…”

“The probability of Mutated Gates appearing is rising explosively. The incident in Sichuan Province is the most notable example.”

Mutated Gates occurred with an extremely low probability.

Even in Korea, where more than several hundred Gates existed, they appeared only once or twice a year—three times at most.

But there had already been more than five last month.

*And this month, it’s already happened twice, counting the one I just dealt with.*

It was a bizarre phenomenon that defied explanation.

But there was no way it was a coincidence that events in the Murim had come to mind at this exact moment.

*Something is happening.*

*Tap. Tap-tap.*

I tapped my fingers against the table without saying anything, then asked,

“What’s the situation in North America and Europe?”

“Based on my expectations, it should be similar. But I requested data from someone reliable to obtain more certain information.”

“Someone reliable?”

The moment after I asked Team Leader Choi that question, I felt every one of my senses snap awake.

*Whoooooosh.*

A sudden storm of energy.

An enormous amount of mana—far beyond even an A-rank Hunter—was converging somewhere inside the Guild House.

*This is…*

I knew it.

The flow of mana.

And the distinctive presence I could sense within it.

“Team Leader Choi, don’t tell me…”

“It’s the person you’re thinking of. I didn’t expect him to come in person, though.”

At Team Leader Choi’s calm answer, the Skeleton King turned to me with a bewildered expression.

“Wretched human. Whom are you talking about?”

“Your dad.”

“…”

The confusion lasted only a moment.

As someone’s message magic burrowed into everyone’s minds, a smile spread across the Skeleton King’s face.

—Have you all been doing well?

The voice carried a distinct hip-hop soul and groove.

I quietly laughed and thought of one man.

*Magic Johnson.*

The American Grand Mage had come to visit the Peace Guild.
## Chapter artifact 559

# Chapter 559

Teleportation.

The spatial-transference magic commonly called Teleport was infamous for being extraordinarily difficult, even among mages.

One wrong coordinate and you could be killed in an instant. The mana consumption was so extreme that anyone attempting long-distance travel was liable to clutch the back of their neck and collapse.

*The ultimate shitty cost-to-benefit ratio.*

But no matter what it was, in the end, everything depended on *who* was using it.

Just as the Three Calamities Sword Technique performed by a Supreme Peak master was no different from some divine technique, the same held true for the Grand Mages—of whom only three existed among the seven billion people in the world.

“Fucking Korea. I think this every time, but it’s too damn far away. I almost got motion sickness on the way here.”

I gave a quiet laugh as I watched the dark-skinned Grand Mage, Magic Johnson, grumble.

“Getting motion sickness while traveling between continents is a small price to pay. If another mage had done it, they’d be seasick on the Sanzu River by now.”[^1]

[^1]: The Sanzu River is a Buddhist river associated with the boundary between life and death.

“Sanzu River? What’s that? Is it something like Cheonggyecheon in Seoul?”

“...It’s a little different. Yes. Anyway, let’s move on.”

Magic Johnson, who had turned Seoul into a city of hell in one sentence, spotted the people inside the room and broke into a wide smile.

“Hey, what’s up, guys! It’s been a while.”

In response to the greeting from Time magazine’s pick for the “world’s most influential LGBTQ person,” Team Leader Choi answered in the world’s most decisive voice.

“It’s *guys*, Mr. Johnson. Not gays.”

“Choi, now you’re hurting my feelings. I came running the moment you asked.”

“I appreciate you coming in person, but couldn’t you have sent the information through a secure email?”

“Is that any way to treat someone you haven’t seen in a while?”

“If I remember correctly, it hasn’t even been a week since we last met. Isn’t that right, Mr. Jin Taekyung?”

I nodded.

“That’s true. Johnson was here for the national funeral, too.”

The national funeral held this time had been enormous. Nearly a million citizens had come to pay their respects, and influential figures from countries around the world had traveled to Korea.

To show just how much influence Lee Jungryong had possessed in life, quite a few of the mourners had been presidents. One news outlet had even called it a “summit meeting.”

Among those heavyweights had been Magic Johnson, one of the symbols of the United States.

“Hey, Jin. Is this how you’re going to act? I didn’t come to meet you people. I came simply to pay my respects.”

“Pay your respects?”

“That’s right. I only came to see an old comrade off.”

“Then why did you go to a gay bar in Itaewon? And why did you even change your face with illusion magic?”

“...Who told you such ridiculous nonsense?”

“The guy who went to the gay bar with Johnson told me. His testimony was pretty conclusive.”

The warm welcome from earlier had vanished without a trace.

The victim of that day, the Skeleton King, spoke with an enraged expression.

“I realized something had gone wrong when something touched this body’s backside. That damned human deceived me.”

“You ungrateful monster motherfucker...”

Look at that expression. I could believe it if Time magazine had named him the “world’s most violent LGBTQ person.”

Magic Johnson muttered in a threatening voice, then noticed everyone’s eyes on him and quickly adopted a serious expression.

“Don’t misunderstand. I only went there to experience Korean culture.”

“Did you sell your tribute to an old comrade on eBay?”

“Jin, don’t be like this. Paying my respects ended when I attended the funeral. You know better than anyone what Mr. Lee was like.”

I did.

Who could possibly know better than me?

And Magic Johnson was one of the very few people who knew what had happened at the Arch Lich’s stronghold.

“Anyway, we’re meeting again, so let’s stop talking about this. You there, you agree, don’t you? Your name was... Robin Hood, right?”

Unfortunately, Korea’s Robin Hood—Im Kkeokjeong, who didn’t have a translation Item—answered with a frozen expression.

“I-I’m fine, thank you. And you...”

“I’m obviously fine. But from this point on, I’m afraid I have no choice but to tell you a rather unpleasant story.”

*Swish.*

With a sigh, Magic Johnson held out a tiny memory chip no bigger than a fingernail.

Team Leader Choi accepted it and examined it. His eyes sharpened.

“Is this the information I asked for?”

“That’s right. I had to pull a few strings for the first time in a while.”

“I’ll save my thanks until after I’ve reviewed the material.”

“Take all the time you need.”

*Tap. Whoooooosh.*

It happened in the blink of an eye.

When Team Leader Choi tapped somewhere beneath the table, every window and opening in the private office was covered, and invisible mana descended like a curtain.

*Magic?*

There was no way the Grand Mage, Magic Johnson, hadn’t noticed what I had.

He looked around the office with interest.

“Seven overlapping spells. Your security is more thorough than I expected. There are only a handful of mages in our Guild capable of magic at this level... Whose work is this?”

“Someone who has been my hands and feet since I was young.”

Team Leader Choi answered briefly.

Kim the Butler and Magic Johnson had never met face-to-face.

When Choi inserted the memory chip into his smartphone, a holographic video suddenly sprang up above the screen.

—Krrrraaaaaash!

With a vivid, thunderous roar, the ground within a radius of several dozen meters overturned, sending grains of sand flying in every direction.

It looked like an earthquake.

Around a hundred Hunters of different ethnicities shouted and cursed.

—Fuck!

—Spread out! Spread out immediately! They’re coming!

—Healer! Healeeer!

Screams and shouts filled the scene. Between the dead trees and the sand dunes stretching in every direction, several buildings were visible as they collapsed.

Im Kkeokjeong’s eyes widened as he realized what it meant.

“M-Monster Wave?”

Correct.

There was no way modern buildings could exist inside a Gate.

Every Gate contained at least a minimal amount of mana, and its Grade was determined by the total amount of mana it held.

But if a monster appeared that far exceeded the Gate’s Grade, the situation changed.

*That was a Mutated Gate.*

A Mutated Gate was already a serious problem. But if the presence of the higher-grade monster caused the Gate’s mana to exceed the total amount it could contain, an even greater disaster awaited.

*A Monster Wave.*

If a sturdy dam couldn’t withstand the pressure and collapsed, the water it had been holding back would overflow.

The scene visible through the hologram was exactly like that.

—Sssshhhk!

More than ten enormous scorpions let out strange cries.

The creatures had burrowed deep into the sand; their tails shot up through the surface, and screams and spurts of blood erupted in every direction.

—Gaaaaah!

—Joseph! Save Joseph!

—Commence volley fire!

*Krrrraack!*

At the very moment humans and monsters threw themselves at one another in an attempt to kill each other—

*Flick.*

The holographic video filling the office vanished as though it had been washed away.

Team Leader Choi stopped the transmission and spoke in a subdued voice.

“When did this happen?”

Magic Johnson answered with a dark expression.

“Four days ago. The Mojave Desert. The desert region stretches across several states, but it was somewhere closer to Arizona. I don’t know the exact coordinates.”

I had been listening closely to their conversation when I suddenly furrowed my brow.

“Four days ago?”

“That’s right. Four days ago.”

“At that point, there should already have been an official announcement.”

Gates were like ticking time bombs that exploded only with a very low probability. That was why every country in the world kept a constant watch on them.

It was also why government Hunters—often called “bomb disposal squads”—were stationed throughout each region, and why the authorities were required by law to announce such incidents within a specified period.

*Then why has everything been so quiet?*

Mutated Gates were rare enough, but Monster Waves occurred dozens of times less frequently than that.

An incident of this scale should have made headlines and become a global sensation.

With me and Team Leader Choi keeping a close eye on news from all over the world lately, it made no sense that neither of us had heard about it.

In the end, only one answer remained.

“There was no official announcement.”

At my muttered words, Magic Johnson gave a small nod.

“That’s right. The Ministry of National Defense stepped in and covered everything up neatly. Just like that desert, which the monsters turned upside down.”

“They can do that?”

“Can they? Come on, Jin. This was something the United States Ministry of National Defense handled in secret. You should’ve asked what they *can’t* do.”

Magic Johnson let out a dry laugh and continued.

“Twenty-two people died and thirty-five were injured, but that doesn’t change anything. Since it happened at a military base where civilians weren’t allowed, it was probably easy to conceal.”

“But this is... literally a cover-up.”

“It is. It also violates the constitution, which was extensively revised after the Great Cataclysm. But sometimes a kind lie is better than a cold truth.”

“...!”

For a moment, it felt as though someone had struck me in the back of the head.

I knew this was wrong.

And yet I had realized that I was thinking the same thing as Johnson.

*Dark Heaven.*

People who weren’t prepared would inevitably be thrown into confusion by a truth that arrived without warning.

That was exactly what Dark Heaven’s existence had been like in the Murim, and I agreed that it was too soon for their identities to become known.

But that wasn’t the only reason the back of my head felt numb.

I was also shocked that the vague anxiety I had been sensing had finally revealed itself as something real.

“How many times?”

It was a question without a subject.

But Magic Johnson’s rigid expression was proof that he understood exactly what I meant.

“Johnson.”

“...Fuck.”

He muttered the curse like a sigh, then turned toward Team Leader Choi.

“Choi, how many videos are stored on the chip I gave you?”

Team Leader Choi stared silently at the smartphone screen before answering in a voice that sounded almost like a groan.

“Thirty-two.”

“That’s right. Two of them were Monster Waves, and the rest were Mutated Gates. The important thing is that those are only the materials I managed to obtain.”

Magic Johnson’s position, status, and influence in the United States were undeniably immense.

But even he could not compare with the intelligence-gathering capabilities of the Ministry of National Defense of the United States, which still claimed to be the most powerful nation in the world.

*Thirty-two incidents in the data Johnson managed to acquire alone.*

How many more events had taken place?

At that moment, Team Leader Choi and I fell silent at the same time, as though we had arranged it in advance.

“Wait. Just wait.”

The Skeleton King had been diligently counting something on his fingers. Now he looked at Magic Johnson with eyes as round as lanterns.

“Human I am no longer grateful to, according to what you just said, doesn’t that mean incidents like this happened every single day?”

“You loose-lipped monster, aren’t you taking this situation a little too lightly?”

“Huh?”

What Magic Johnson said next was something I almost would have preferred not to hear.

“Not over the course of a month. These incidents happened within the past week.”

“...!”

“...!”

In the suffocating silence that pressed down on everyone, a single voice rang out—the only person present who hadn’t understood what Johnson meant.

“I-I’m fine, thank you. And you?”

“...”

“...”

*To hell with ‘and you.’ Holy shit. Fuck.*

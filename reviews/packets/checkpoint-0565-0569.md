# Checkpoint Review — 565–569

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

# Chapters 565–569

## Plot

Magic Johnson’s chip reveals more than twenty simultaneous Gate and monster crises worldwide, along with a seven-percent annual rise in mana. Taekyung suspects the beginning of a second Great Cataclysm. Team Leader Choi confirms that concealment is no longer viable and prioritizes strengthening Gate defenses while continuing his move against Ares Guild.

Choi’s Ares ally is Song Cheonwoo, a former top-ranked Hunter, Great Cataclysm veteran, and longtime rival of the late Lee Jungryong. Song knows where Choi’s missing maternal grandfather, Cheon Taemin, is hiding. Go Jun responds by ordering Go Se-won to seize Song’s family in London. Thirty Ares security personnel carry out the operation, leaving two dead and the family captured as leverage.

Song is lured to Go Jun and learns that his children have been taken. After Go Jun frames the abduction as protection, Song warns Se-won that Go Jun has become a monster and asks him to save the children before teleporting away. Se-won realizes Go Jun likely intends to eliminate Song while making the death appear natural.

Meanwhile, Taekyung trains in isolation for up to three days, developing an unfinished new martial endeavor. The Skeleton King, now trusted to handle suitable emergencies alone, interrupts him to report an abnormal Mutated Gate with an enormous magic power reading and request assistance.

## Continuity

- The worldwide Gate and monster crisis may signal a second Great Cataclysm; Taekyung intends to accelerate his efforts to protect Korea.
- Team Leader Choi is strengthening Peace Guild’s Gate defenses while working with Song Cheonwoo against Go Jun.
- Song Cheonwoo knows Cheon Taemin’s location; Cheon Taemin remains hidden.
- Go Jun has seized Song’s children and appears to be arranging Song’s quiet elimination.
- Go Se-won remains complicit in Go Jun’s operations but is increasingly morally conflicted.
- The Skeleton King has adopted the fabricated identity King Fury, earns six hundred million won annually through Peace Guild, and can now respond to suitable Gate emergencies independently.
- Taekyung’s new martial project is nearly complete but its nature remains unidentified.
- The Skeleton King has reported an abnormal Mutated Gate with an enormous magic power reading.
- The Nanman mission, Dark Heaven’s rifts and mutants, the Southern Heaven Demon Empress’s intentions, Jeok Cheongang’s duel with Nangong Cheon, and Ju Hwaran and Sama Pyo’s broken engagement remain unresolved.
- The survival of Song Cheonwoo’s family remains unknown.

## Translation Decisions

- Retain **Mutated Gate**, **Monster Wave**, **Nanman**, **Nanman Beast Palace**, **Fire Dragon Pavilion**, **Journey to Nanman**, **Can’t Go to Nanman**, **Peace Guild**, **Ares Guild**, **Skeleton King**, and **Teleportation**.
- Render 송천우 as **Song Cheonwoo**, 송 이사 as **Director Song**, and 세종 기지 as **King Sejong Station**.
- Render 킹 퓨리 as **King Fury** and 배리어의 국장 contextually as **Director of Barrier**.
- Render 마력 수치 as **magic power reading** and 정도 in the moral context as **a line a person should not cross**.
- Preserve the Skeleton King’s melodramatic mock-archaic register, Taekyung’s blunt profanity, and the capitalism, slavery, and superhero-identity running jokes.

## Durable state

{
  "active_continuity": [
    "The worldwide Gate and monster crisis may mark the beginning of a second Great Cataclysm, and Taekyung intends to accelerate his project to protect Korea.",
    "Team Leader Choi says the crisis has exceeded the limit of national concealment and is prioritizing Gate defenses despite reducing Peace Guild's raid capacity.",
    "Choi is working with Song Cheonwoo against Go Jun's control of Ares Guild, while Song knows where Choi's maternal grandfather Cheon Taemin is located and Cheon Taemin remains hidden.",
    "Taekyung is a Supreme Peak master publicly recognized as S-rank-level while retaining an A-rank license, leads the Fire Dragon Pavilion's first Nanman mission, and is Peace Guild's wealthy modern-world patron.",
    "The six-member Fire Dragon Pavilion mission is entering Nanman through the Journey to Nanman Quest, whose reward is a linked quest and whose failure penalty is Can't Go to Nanman.",
    "Mungyeong ended Taekyung's direct training and assigned him the final task of incorporating martial principles into his learned martial arts; Cheongpung accompanies Mungyeong.",
    "Dark Heaven remains a monster-like threat capable of causing rifts and creating mutants, while the mechanism behind Jang Sam's transformation remains unresolved.",
    "The Mount Song Resolution restored the Murim Alliance with Mae Jonghak as Alliance Leader and Jeok Cheongang heading the Five Kings Hall; Zhuge Feng's Demon-Sealing Formation still blocks mana from the exposed Gate while Jang Taebo processes the Water God Dragon's remains.",
    "Go Jun has become increasingly ruthless, controls Ares Guild's legacy, has seized Song Cheonwoo's children as leverage, and appears to be arranging Song's quiet elimination.",
    "Go Se-won commands Ares Guild's thirty-member A-rank security team and remains obedient to Go Jun despite growing moral conflict; he personally ordered and cleaned up the abduction of Song's family.",
    "The Skeleton King was the person who applauded Taekyung and appeared as King Fury; Taekyung now trusts him enough to handle suitable emergencies alone and has granted him greater freedom.",
    "Taekyung has spent up to three days isolated in training, nearly completing an as-yet-unidentified new martial endeavor, while abnormal Gates and emergency rescue demands increase."
  ],
  "continuity_sources": [
    569,
    568
  ],
  "open_questions": [
    "What is the Lord of Heaven's identity, how is he connected to the dangerous force Taekyung associates with his original world, and how can Dark Heaven open Gates?",
    "What will Taekyung's party find in Nanman, and what does the Southern Heaven Demon Empress intend there?",
    "What process created Jang Sam's mutant form, whether Dark Heaven's mutants can absorb human energy, and whether it relates to the Mutated Gate?",
    "What will result from the duel between Jeok Cheongang and Nangong Cheon, and why did Ju Hwaran and Sama Pyo's political engagement end?",
    "Will Song Cheonwoo's children survive Go Jun's plan, and what will Taekyung's unfinished training project become?"
  ],
  "safe_through": 569,
  "temporary_decisions": [
    "Render 건량 as dry rations, 광서 as Guangxi, 대별산 as Mount Daebyeol, 만리행 as Ten-Thousand-Li Journey, and 고잉메리호 as Going Merry.",
    "Render 반 시진 as half a shichen and retain Nanman, Nanman Beast Palace, Fire Dragon Pavilion, Great Hero, and Young Lady Ju.",
    "Render 남만행 as Journey to Nanman, 남만을 못 가 as Can't Go to Nanman, 면구 as disguise mask, 역용술 as disguise technique, 각주님 as Pavilion Master, 로그아웃 as Logout, and 동기화 as Synchronization.",
    "Render 일기당천 as One Against a Thousand, 거인의 포효 as Giant's Roar, 투로 as combat sequence, 타락한 엔트 as Corrupted Ent, 붉은 눈 as Red Eye, 치코리타 as Chikorita, 대마도사 as Grand Mage, 순간이동 as Teleportation, 텔레포트 as Teleport, 변이 게이트 as Mutated Gate, and 몬스터 웨이브 as Monster Wave.",
    "Render 현혹 마법 as enchantment magic, 장거리 텔레포트 마법진 as long-distance Teleportation magic, 킹 퓨리 as King Fury, 배리어의 국장 as Director of Barrier, 세종 기지 as King Sejong Station, and 마력 수치 as magic power reading."
  ],
  "version": 1
}

## Reading copies

## Chapter artifact 565

# Chapter 565

After Magic Johnson left, I sent a text to Team Leader Choi, who still wasn’t answering, then headed straight for the private office on the top floor of the Guild House.

*Bang.*

Hearing the door slam shut behind me, I dropped heavily onto the floor.

It was a space of over a hundred pyeong, but all it contained was a small desk and a single chair.

The place was called an office, but it was really a training ground. I immediately took out my smartphone and inserted the chip.

*Click.*

The latest model I had bought a while ago had every feature imaginable.

That included holographic video playback, which had begun to spread throughout society more than a decade ago.

*Bzzzz.*

Light flowed out of the player mounted on the smartphone with a faint hum.

I quickly used Seizing an Object Through Empty Space to draw the blackout curtains, then focused on the holographic footage beginning to fill the dark office.

*Crackle. Crackle.*

Noise.

*Boom! Kraaang!*

A deafening roar.

*Shrieeeek!*

A monster’s cry.

“Aaaah!”

A human scream.

All of it mixed together before my eyes, then scattered. The place, lined with large and small tents and buildings, had suddenly transformed into a horrific battlefield.

*Mutated Gate.*

Those five syllables naturally flashed through my mind.

Then—

“In the name of Allah!”

“Waaaaah!”

A group wearing military caps and turbans advanced with desperate shouts.

Their bodies, presumably Arab, were soaked in someone else’s red blood.

Among them was even a child who looked no older than an elementary school student.

*A child…*

There was no way people like these were regular soldiers.

I had suspected as much from their mismatched, chaotic clothing, but they were clearly Arab rebels—the same kind who had stained the Middle East with blood even before the Great Cataclysm began.

And then—

“Aaaah! G-God is great!”

Along with the terrified cry of a little boy, countless firearms in their hands opened fire.

*Rat-tat-tat-tat!*

*Whoosh! Boom!*

A torrent of firepower that would have turned ordinary humans into pincushions poured forth all at once.

But their enemies were neither ordinary nor human.

*Kraaang!*

A massive blaze rose with the explosion.

The rebels were panting roughly as they stared at the black smoke filling every direction.

Then the smoke split apart, and a flash of light gleamed.

*Whoosh. Shing!*

A single strike was enough.

Dark red mana shot outward in the shape of a crescent moon, cutting through everything in its path.

Necks, waists, chests. The exact wounds differed, but the result was the same.

Death.

*Splaaash!*

A moment later, fountains of blood erupted and stained the sand red.

The rebels stared wide-eyed at the horrific deaths of nearly twenty comrades before them.

“M-Masoud!”

“My God…”

But their god neither appeared nor answered the voices of his worshippers.

What appeared in his place was a monster covered from head to toe in green armor.

*Chirr. Chiriririk.*

With a triangular head, two trembling antennae, and forelegs curved like scythes, the monster was a mantis.

It was so enormous that it could look down at an adult man. Its body radiated powerful mana, yet it did not have a single scratch from the firepower the rebels had just unleashed.

“G-Giant Mantis…”

The instant someone muttered the name like a groan, the enormous foreleg once again swept down through the air.

*Whoom. Shing!*

The body of a rebel who had frozen in place was split in two.

The mana infused into the foreleg flew outward like arrows, shredding everything around it.

*Shing! Shing! Kraaang!*

Humans. Weapons. Even the tanks hurriedly sent into battle could not withstand the mana.

Explosions and screams rang out in succession as the attack cut through everything in every direction.

Before long, the number of Giant Mantises had increased to five, and they leaped toward the humans.

*Chit-chit-chit!*

*Chiriiit!*

*Crack! Splaaash!*

Whenever the strange cries rang out, the limbs of rebels numbering over a hundred went flying, and blood sprayed through the air.

Those who struggled while screaming for their god and those who fled in terror alike collapsed onto the desert sand, never to rise again.

“Aaah! Aaaaah!”

*Thud!*

A scythe-like foreleg slashed through the rebel’s back and shattered his breastbone.

The Giant Mantis that had driven its strike into the back of the last resisting rebel suddenly turned around.

A red eye protruding from the side of its face stared directly at the screen.

*It found the camera.*

It saw the camera, and I saw it.

Then, just as the Giant Mantis sensed something strange and cautiously began approaching the camera—

“May the flames of God descend upon this place. Fire Rain!”

*Fwoosh!*

An aged voice shouted. At the same time, dozens of fireballs formed from mana poured down like meteors over the Giant Mantis’s shoulder.

*Chiririririt!*

The Giant Mantis let out a strange cry and swung its foreleg at the fireballs.

*Boom!*

At the moment of impact, the screen—or rather, the entire room—was dyed red.

From far away, dozens of Hunters appeared and sprinted across the battlefield through the fireballs bursting around them.

“Allahu Akbar!”

“God is great! Kill every one of those devils!”

*Krrk, chiiit!*

Humans and monsters.

Monsters and humans.

The two species began killing one another once again.

But I couldn’t watch the outcome of this battle all the way to the end.

*Crackle. Crackle. Pop!*

It happened in the blink of an eye.

The holographic footage that had filled the room vanished without a trace amid a burst of intense static.

“…Whew.”

I exhaled the breath I had been holding and picked up the smartphone I had set aside.

When I checked the list stored on the chip, I found that more than twenty videos remained.

*Fuck. How long has it even been since the last time I got a batch of videos? And there are already more.*

Worldwide mana levels had risen by seven percent compared to the previous year.

Some idiots might think that was *only* seven percent.

But just as the world would be thrown into chaos if the oxygen concentration dropped by even a few percentage points, this was proof that things were going to hell.

No.

Maybe…

*This could be the beginning of the second Great Cataclysm.*

And the more I checked the remaining videos one after another, the anxiety I carried inside began to take shape.

*Europe. The Middle East. West Africa. Southeast Asia… What is this, some kind of worldwide festival?*

Changes were already taking place simultaneously all over the world.

A new Gate appeared amid the green hills of Switzerland, where you could imagine Patrache running around with a dog biscuit in his mouth.[^1]

While rebels and regular soldiers bombarded one another, monsters poured out of low-rank Gates that had been left unattended.

Some of the videos showed places where the defenses had been thorough enough to suppress the situation early.

But in more than half of them, the monsters could only be defeated after causing considerable damage.

*This…*

I continued replaying the videos, then suddenly furrowed my brow.

I had realized that the damage was not simply the result of inadequate Gate defenses.

And at that moment, more than insight came to me.

*Ding.*

Along with the faint sound of the elevator entering my ears, I sensed the presence of two people slowly drawing closer.

I recognized the identities of the uninvited guests and reached out.

*Fwoosh.*

A warm breeze blew through the room.

The qi flowing from my palm gently pushed the door open, bringing familiar faces into view.

“What took you so long? It’s been ages since I texted you.”

“I apologize. I was in a situation where I couldn’t receive any messages for a while.”

I had been about to chew out the latecomers, but I tilted my head.

“You couldn’t receive any messages? Did you go to a Gate or something?”

“Something like that.”

“…Either it happened or it didn’t. What does ‘something like that’ even mean?”

“There was somewhere I needed to stop by with Butler Kim. It was an important errand, so it couldn’t be helped.”

Team Leader Choi answered smoothly as he stepped inside.

Butler Kim followed naturally behind him, closing the door and giving me a slight nod.

*I haven’t seen that guy in a while.*

Butler Kim had hardly shown his face at the Guild lately. What kind of important errand had brought him here with Team Leader Choi?

Seeing him again after about a week left me with a lingering question, but something more urgent was waiting.

Team Leader Choi obviously knew that as well, because he spoke first.

“We can discuss this later. For now, we should check the information Mr. Johnson gave us.”

“Oh. Here.”

The holographic footage began playing again.

After some time had passed, the expressions of the two men who had checked every video and its attached materials had hardened.

“Worldwide mana levels up seven percent?”

Butler Kim’s usually gentle voice came out cracked.

He muttered the words like a groan, then turned toward Team Leader Choi.

“Young Master.”

“Yes. It’s progressing faster than we anticipated. The situation is serious.”

Seven percent could not be called a rise. A surge—or even a skyrocketing increase—would have been more appropriate.

And that sharp change in mana levels was especially obvious in the footage.

“The monsters…”

I nodded and picked up Team Leader Choi’s words.

“Yeah. They’ve gotten fucking strong.”

A rise in mana levels meant that monsters were becoming stronger as well.

The Giant Mantis holding its own even after being hit by Fire Rain in the first video was proof enough.

*It was like watching Chikorita get a tan from Charizard’s flames.*

Type advantages were supposed to exist for a reason, but along with the rise in mana levels, the strengthened monsters were gradually beginning to ignore them.

With things this fucking bad, places that had been deploying the bare minimum of precious Hunter manpower as a precaution had no choice but to collapse helplessly.

To sum up the current situation in one phrase…

“We’re fucked. We’re five minutes from total chaos.”

The pace of this madness was incredible.

If things continued like this, monsters might start appearing in the weather forecast by the end of the year.

Some beautiful weathercaster lady would point to a map of the Korean Peninsula no bigger than a booger and explain everything in detail.

“Tomorrow, goblins are expected to fall in Cheorwon, Gangwon Province, instead of heavy snow. They’re expected to pile up to a height of twenty meters, so residents should grab their shields and antidotes and evacuate immediately.”

“…”

*Fuck. Snow is annoying enough, and now monsterfall is for real?*

Monsters raining down from the sky.

Just imagining it made my heart shrivel.

Of course, I wasn’t going to sit around twiddling my thumbs until then. I had to stop Korea from becoming a hellish peninsula, no matter what it took.

*I had kept it in mind as a possibility, but… the situation is definitely progressing too quickly.*

I had thought we still had a little time.

But the realization that I needed to bring forward *that thing*—the plan I had been working on little by little ever since Murim—made my heart heavy.

That was when Team Leader Choi spoke.

“At this point, we can no longer keep it hidden.”

He turned off the holographic footage and continued in a subdued voice.

“We have already passed the limit of what can be concealed at the national level. If we wait any longer to announce it, we will only increase the confusion.”

This was not a wave that would simply pass.

It was a tsunami that might sweep away entire cities.

I sighed and opened my mouth.

“What are you planning to do, Team Leader Choi?”

“For now, reinforcing Gate defenses is our top priority. We need to build a breakwater before the tsunami hits.”

“Strengthen the Gate defenses?”

“If we do that, our raid personnel will decrease, and we won’t be able to make full use of every Gate owned by Peace Guild. But I know what needs to come first.”

“That’s a relief.”

I let out a quiet laugh at the welcome news.

Team Leader Choi definitely stuck to what was right.

Even though he had the grand ambition of swallowing up Ares Guild, he was someone who knew when to move forward and when to stand still.

*That’s also the biggest difference between him and Lee Jungryong.*

I muttered to myself and spoke again.

“Then we should focus on the Gates for now. It’s unfortunate, but we’ll have to put matters concerning Ares Guild on hold for a while…”

“Mr. Jin Taekyung.”

“Yes?”

By then, Team Leader Choi’s clear eyes were staring straight at me.

“I said that I would make Gate defenses my top priority. I never said I would put matters concerning Ares Guild on hold.”

“…”

*What?*

I involuntarily widened my eyes, and Team Leader Choi’s voice continued.

“I told you, didn’t I? I had an important errand to take care of first.”

“Then that important errand was…?”

“One of Ares Guild’s major figures. He was a war hero who helped my maternal grandfather suppress the Great Cataclysm in the past, once the friend Lee Jungryong trusted most, and is now the head of the largest internal faction threatening Go Jun.”

His voice was gentler than ever, but there were thorns hidden beneath it.

“Everything crumbles from the inside.”

[^1]: Patrache is the dog from the story commonly known in Korea as *A Dog of Flanders*.
## Chapter artifact 566

# Chapter 566

What came out of Team Leader Choi’s mouth was completely unexpected.

If the rate at which mana levels were rising hadn’t been so high, it might even have been the part that interested me most.

*A traitor?*

A few Ares Guild members had transferred over to our side because of this incident, but that had been nothing more than a simple job change. They were ordinary Guild members whose positions within Ares were a dime a dozen.

But an internal traitor was on an entirely different level.

*Especially if that traitor is a big shot.*

In Murim terms, he was a master from the previous generation.

The fact that he belonged to the elder generation that had lived through the Great Cataclysm was already enough to pique my interest, but apparently he was also the head of an internal faction powerful enough to threaten Go Jun.

*Oh, now that’s appetizing.*

“……Mr. Jin Taekyung?”

“Oh, yes. What is it?”

“Here, first of all.”

I wondered what he meant, only to find a handkerchief. When I blinked at him, Team Leader Choi pointed awkwardly at my chin.

“I don’t know why, but you have quite a bit of drool around your mouth.”

“……Oh.”

“It looks like it’s about to dr—ugh.”

What the hell was that reaction? Anyone could drool a little.

I wiped the corner of my mouth with my sleeve and got straight to the point.

“So who is it? The traitor.”

“Traitor. That’s a word he wouldn’t like very much if he heard it. How should I put it… He would probably prefer to call himself a business partner. Or perhaps the next Vice Guild Master of Ares Guild.”

“What kind of bullshit is that? From what you’ve said, you’ve already more or less struck a deal with him. If it looks like betrayal, I’m going to call him a traitor. Is he just telling himself otherwise to feel better?”

Team Leader Choi wasn’t the one who answered my question.

Butler Kim, who had been standing quietly and listening to our conversation, spoke in a low voice.

“He is a man with a great desire for honor.”

“Honor?”

“When a person grows old and begins to approach death, they often become obsessed with honor. No… Considering the life he has lived, the word *greed* might be more appropriate.”

Had Butler Kim ever spoken so harshly about anyone?

If I had to name one person, it would be Lee Jungryong. But if the emotion Butler Kim had shown toward Lee in the past was anger, then what he felt toward this person was closer to contempt.

*It’s rare for that old man to show his feelings so openly.*

From everything I had personally seen and heard, Butler Kim was a man of character on par with Jesus or Buddha.

Well, he seemed to have had quite a fiery temper in his younger days, but that was exactly what it was—something from his younger days.

*But who is it, really?*

Judging by how severely he was criticizing the man’s entire life, they clearly knew each other well. But there were so many Ares Guild executives who wielded considerable influence that no name immediately came to mind.

Then, as if he had noticed my curiosity, Team Leader Choi spoke up.

“Director Song. Song Cheonwoo is that kind of person.”

“Song Cheonwoo. Song Cheonwoo……”

The name felt oddly familiar. When I searched for it on my smartphone, a small amount of information about one person appeared.

Calling it information was almost embarrassing. There was a date of birth, a few lines about his life up to the present, and two photographs of the same man displayed side by side at the top of the page, including one from his younger days.

Still, it wasn’t completely useless.

“Huh? Is this man perhaps…?”

“Have you seen him before?”

“Yes. I think I’ve seen him in one of the framed photographs that are always hanging in the halls of the Hunter training center. Am I mistaken?”

“Your memory is probably correct. More than twenty years ago, he briefly served as the head of the Hunter training center.”

“Oh.”

Although this had been before the regulations were properly established, the position of head of the Hunter training center could only be held by a top-ranking ranker with an impressive record of achievements.

*He really does seem like a big deal.*

But compared to his reputation, the information available on him was pitifully sparse.

Someone with a career like this should have accumulated plenty of achievements and stories by now, yet all there was were two or three lines of biography. The last update to his profile had been three years ago.

*Three years ago?*

Even a middling B-list celebrity would have more information than this. I frowned and began tapping at the screen in search of something else.

That was when it happened.

*Bzzzz.*

Along with a faint vibration, a notification appeared on my smartphone screen.

> **Team Leader Choi**
>
> **Team Leader Choi**
>
> *[File attached]*

“What’s this? Why all of a sudden?”

“I thought this would be faster. You will probably have difficulty finding detailed information about him through an Internet search.”

“Come on. What kind of world do we live in these days?”

“Then I’ll delete the attached file.”

“But since you went to the trouble, I’ll read the file you sent.”

“……”

“Listen to the end when someone is speaking Korean.”

After giving Team Leader Choi some advice that would surely nourish his body and soul, I opened the attached file.

Unlike what I had seen online, this time the file was dozens of pages long.

I began rapidly absorbing the information appearing on the screen.

His name was Song Cheonwoo. He was in his seventies.

Naturally, he was an A-rank Hunter, and twenty years ago, he had been a top-ranking ranker who had reached third place in Korea.

Considering that the people in first and second place at the time had been Cheon Taemin and Lee Jungryong, it was clear that this man was also an extraordinary fighter.

His achievements during the Great Cataclysm included dozens of records of participation in major battles. Perhaps because his accomplishments had stood out more overseas than in Korea, he had even received medals from eight countries, including the United Kingdom, Germany, and France.

As for the rest of his career…

There was so much of it that it was a pain to go through piece by piece.

“His career is incredible. How did I never remember this man?”

“He is not as well known in Korea as you might expect. His past achievements were more prominent overseas, and his activities in Korea after the war were also very brief.”

“Ah. I see.”

He had a major career as head of the Hunter training center, but the file said that he had voluntarily resigned before completing even half of his four-year term.

The official reason was health problems, but……

“Two months later, he was appointed head of Ares Guild’s European regional branch.”

When I read the passage aloud, Team Leader Choi nodded.

“That was his last position in Korea. From twenty years ago until now, Song Cheonwoo’s position has remained fixed as head of the European regional branch. That is why Hunters of the younger generation, like me and Mr. Jin Taekyung, do not know much about him.”

“Leave yourself out of that. You’re probably one of the people who knows Song Cheonwoo better than anyone else. Am I wrong?”

“Why do you think that?”

“Who do you take me for, an idiot? Cheon Tae—sorry. Anyway, you seem to have quite a connection with that person, and Butler Kim knows him too, so there has to be a link. To give one more example……”

“For example?”

I didn’t need long to think. I pulled out one relatively recent memory and tossed out a single phrase.

“Head of the European regional branch.”

“……!”

“You said it yourself before. When you were with Ares Guild, you were constantly being sent around to overseas branches. I think one of those places was Europe.”

A faint smile spread across Team Leader Choi’s lips.

I had guessed correctly.

“You actually remember that.”

“I’m not as stupid as you think.”

“Your guess is correct. Song Cheonwoo had followed my maternal grandfather since before I was born. Five years ago, when I was assigned to the European branch, he used his authority as branch director to keep me close.”

“Then perhaps you had some personal relationship with him……”

“Now that I think about it, ‘kept him close’ is not the right expression. Let me correct that to surveillance and isolation.”

“Then you don’t have even the tiniest bit of a personal relationship. Right. Please continue.”

“From what I personally saw and experienced, Song Cheonwoo is a man whose abilities fall short of the size of his ambitions. That may also have been because his past rival was exceptionally formidable.”

His rival?

There was no need to think about it.

I murmured one man’s name.

“Lee Jungryong.”

“There can only be one master of a mountain. Even if the two of them had once been friends, one of them had to leave the mountain.”

Everything finally fell into place.

Why a man of this caliber had been forced to leave Korea not long after the war ended.

Why he had been made to remain in the impressive-sounding position of head of the European regional branch for no less than twenty years.

*He was demoted.*

That was right. This was an unmistakable demotion.

After winning the power struggle within Ares Guild, Lee Jungryong had exiled his rival, Song Cheonwoo, to Europe, where he had slowly faded from people’s memories.

No.

If it had been Lee Jungryong, he would have made sure Song Cheonwoo was *forgotten*.

*Then this is…*

The material I was reading was not some piece of trash scraped together from the Internet.

It was an exhaustive investigation polished by experts, and more than that, it was close to surveillance.

*So that’s why he sent me a separate file.*

I muttered inwardly as I stared at the smartphone screen.

Unlike the online profile, whose updates had stopped five years ago, the final page of the file dealt with recent events.

- **November 15, 2046.** Discussed retirement during a party hosted by the British ambassador. Audio file attached.
- **November 28, 2046.** Purchased a two-story mansion on a 300-pyeong lot in Samseong-dong, Seoul. Appears to be intended as his residence after retirement.
- **January 1, 2047.** Entered Korea through Incheon International Airport. Held a secret meeting with key figures on Ares Guild’s board of directors. Exact number and names attached in supplemental materials.
- **January 2, 2047.** Attended Lee Jungryong’s funeral. Held a second meeting with major figures in the political and business worlds, as well as key members of the Guild.
- **January 4, 2047.** Official Ares Guild board meeting concerning the appointment of a Vice Guild Master. After three revotes, Go Jun’s appointment was approved.

.

.

.

The file was packed with information about Song Cheonwoo’s movements from roughly two months ago until the present.

And simply by reading the text, I could clearly tell that something had changed in his state of mind.

“Song Cheonwoo is dreaming of a very ambitious comeback.”

Team Leader Choi nodded at my words.

“In November, he subtly expressed his intention to resign in a private setting, and he even purchased a mansion in Korea where he could stay after retirement. But……”

“Lee Jungryong died.”

“Yes. It must have been an upheaval that no one expected. For someone on the verge of retirement, it would have seemed like one last opportunity.”

“And his opponent wasn’t Lee Jungryong, but Go Jun. He must have thought that if he joined forces with you, he had a chance.”

The fact that Go Jun had needed three revotes to assume the position of Vice Guild Master was proof of that.

Song Cheonwoo, a man in his seventies approaching retirement, was gathering support from every direction and aiming for one final strike.

“He’s a pretty energetic man for someone his age.”

Team Leader Choi let out a quiet laugh at my muttering.

“Isn’t that the magic of power? It is also thanks to that magic that I was given an opportunity.”

“Fine. That’s all well and good, but……”

What was this feeling?

My mouth felt gritty, as if I had chewed on a handful of sand.

I had been silently staring at Song Cheonwoo’s face displayed on the screen when Team Leader Choi’s quiet voice pierced my ears.

“And if this succeeds…… a grandparent and grandchild may finally be able to meet face-to-face after a long time.”

“What hand?”

I blinked blankly. It didn’t take long for me to realize what he meant.

“No way?”

The savior of the twenty-first century who had rescued humanity.

The immortal hero who would be remembered forever in people’s hearts, yet had suddenly vanished one day behind an invisible curtain.

*Cheon Taemin.*

Even when his only blood relative was in danger, and even after Lee Jungryong’s death, he had never shown himself.

And his maternal grandson, born of the hero’s blood, spoke with the smile gone from his face.

“Song Cheonwoo knew where my maternal grandfather was.”

* * *

Go Se-won, the Head of Security, quietly looked down at the teacup sitting before him.

The tea that had once been warm had already gone cold, and tea-leaf residue floated on the small amount of tea he had deliberately left behind.

*This situation is just like me.*

He had spent more than an hour staring at the teacup after finishing his report. He had almost grown attached to it.

But there was nothing he could do.

All he could do was report the facts exactly as they were. He was not the one who gave orders.

Besides, considering the gravity of what he had just reported, it was fortunate that his superior had not destroyed everything around him as he had last time.

*Long deliberation. The longer he thinks, the better the result will be.*

But the next moment, one word from his superior made Go Se-won realize that his hopes had been completely misplaced.

“Kill him.”

“Excuse me?”

“I said kill him. His children. His grandchildren. His daughters-in-law. All of them.”

*Thud.*

The file folder fell from the table, struck the floor, and opened.

The three Korean characters spelling *Song Cheonwoo*.

Flames flickered in Go Jun’s eyes as he stared at the photograph of the man with prominent cheekbones.

“This old bastard has gone senile……”
## Chapter artifact 567

# Chapter 567

“Has this old man gone senile…?”

Go Se-won had lost count of how many times he had met those red eyes.

The look in Go Jun’s eyes had gone beyond ominous and become downright chilling. Go Se-won swallowed dryly without realizing it.

But he was the Head of Security.

He was the only brake capable of stopping Go Jun’s rampage, even if only for a moment, and it was his duty to dissuade his superior from making a disastrous move after such long deliberation.

“Vice Guild Master.”

Go Jun’s gaze turned toward him. A chill ran down Go Se-won’s spine, but he managed to force out his voice.

“What you just said…… Were you serious?”

Go Jun frowned.

“Of course not. Do I look that much like an idiot to you, Team Leader Go?”

“Oh.”

Go Se-won had waited for the answer with a sinking feeling, so he let out a quiet sigh of relief.

Come to think of it, that would have been absurd.

It was true that Go Jun’s personality had grown violently harsher of late, but there was no way he would order every member of Song Cheonwoo’s family killed……

“Don’t kill them. Bring them here.”

“Excuse me?”

“Didn’t you hear me?”

Of course he had.

Go Se-won was an A-rank Hunter who could hear the flutter of a mosquito’s wings from ten meters away.

The reason he asked again was that he had heard something he would almost rather not have heard.

“Would you repeat that, please?”

*Bang! Crack!*

The table that had been replaced only a few days earlier was smashed to pieces once again. Flames rose in Go Jun’s eyes.

“Bring them here. I don’t care if it’s the grandchild Song Cheonwoo dotes on every day or some white grandmother he met at a retirement community in Europe. If it can be used to get that old man by the throat, bring me anything!”

His shout rang through the room. The veins in his neck stood out as he yelled, but then his voice suddenly sank low.

“So, Team Leader Go. Send the men out and bring them here immediately.”

“……!”

“What? Didn’t you hear me this time either?”

There would not be a third warning.

Realizing that there was nowhere left to retreat, Go Se-won lowered his head slightly.

“No, sir. I heard you clearly.”

“Then get moving. Ah, where did you say that old man’s family lived?”

“On the outskirts of London. The entire family lives together in a huge mansion built by renovating a castle.”

They lived a life worthy of European nobility.

Song Cheonwoo had been able to live that way because of Lee Jungryong’s tacit approval and support, despite having lost the internal power struggle long ago.

Old affection between friends? Mercy? To Lee Jungryong, those were words as useless as cabbage.

It had merely been the arrogance visible only in someone who looked down on another person by several moves, and that arrogance was the leisure of a strong man possessing overwhelming power.

*That man completely controlled his only political rival in the palm of his hand. But the successor who came after him is already thinking about kidnapping the rival’s family.*

Innate temperament.

In other words, the difference in the size of their vessels.

Go Se-won quickly pushed the thought from his mind and continued.

“There are about thirteen of them, counting his children, their spouses, and his grandchildren. Some of the grandchildren commute to school by helicopter or through Teleportation magic circles. Of course, we receive their locations in real time.”

“You made a move? When?”

“Immediately after Song Cheonwoo entered the country. I reported it at the time, but you seemed extremely busy, so I took care of it on my own authority first.”

“You’re good at your job, Team Leader Go. I thought you’d lost your touch after getting married.”

“……Thank you.”

The single remark contained both praise and criticism. As Go Jun looked down at Go Se-won, who bowed his head again, he suddenly muttered in a chilling voice.

“Come to think of it, what an ungrateful old man. He should have been grateful that I let him keep his position all this time. How dare he stab me in the back like this?”

Song Cheonwoo should have retired before the new year arrived.

But the Monster Wave in China and Lee Jungryong’s death had fanned the embers of ambition the old lion had been unable to abandon until the end, and the hyenas that caught its scent had quietly lined up behind him.

The influential members of the elder generation, just before a sweeping change of generations.

They were the pack of hyenas.

“Damn old bastards.”

Go Jun abruptly rose from his seat and began pacing around the room.

“What about him?”

*Him.*

It was a reference to someone whose name had not been spoken even once, but Go Se-won immediately understood.

In truth, the greatest concern in the current situation was not the old lion leading the pack of hyenas.

It was the young male lion prowling the grassland outside Ares Guild’s tall fences, waiting for an opportunity.

“Choi Minwoo has returned to Peace Guild.”

“Are you certain he met with that old man, Song Cheonwoo?”

Go Se-won answered immediately.

“The meeting itself was extremely secretive, and they disguised it with advanced illusion magic, but yes. We’re certain.”

“What about Director Hong? Is he trustworthy?”

Director Hong was one of the elder-generation figures who had been approaching honorary retirement alongside Song Cheonwoo. He was also the useful informant who had passed along word of today’s meeting.

Go Se-won nodded.

“Yes. He judges situations quickly.”

“That man has always been uncannily perceptive. Still, don’t let your guard down. He’s known Song Cheonwoo for more than thirty years.”

“We’re monitoring his every move without crossing the line where he would notice.”

It was betrayal layered on betrayal. Everyone was struggling to achieve their own goals, and Director Hong had simply chosen comfort and survival for the small amount of life he had left.

“What about the security team?”

“All thirty members are on constant standby.”

The security team consisted of elite personnel specially selected from within Ares Guild.

Every one of them was an A-rank Hunter. Their ability went without saying, and their loyalty was exceptional as well.

Their master had suddenly changed, but they were servants who could solve something like murder without batting an eye.

*And I’m no different.*

Go Se-won muttered inwardly.

He had gotten his hands dirty with all kinds of filthy work while serving under Lee Jungryong.

Sometimes he felt disgusted by the person he had become, but until now, he had been able to endure it more or less.

Thanks to it, he had amassed wealth that other people could never dream of in their entire lives. And in his forties, he had met his beautiful, loving wife and married late.

But……

*Have I been doing this for too long?*

He did not know whether it was the hypocrisy of someone who had forgotten hunger or the disgust he had suppressed all this time.

Perhaps it was because of his son, who had only recently begun taking his first steps, and his wife, who had become pregnant with their second child not long ago.

*Song Cheonwoo. His youngest grandson was about the same age as our Sangho, wasn’t he?*

The thought of passing along orders to his men to abduct a child who was too young even to speak properly made him feel strange already.

*No. It would be fortunate if it ended with kidnapping.*

Go Jun had changed over the past month or two.

No one knew what the man would do next now that he had become so violently ruthless.

Even Lee Jungryong, who had never cared what means he used, had never laid a hand on children……

“Team Leader Go.”

At the sound of his superior calling him, Go Se-won’s back straightened.

“Yes, Vice Guild Master.”

“Prepare the security team. You understand what I mean, don’t you?”

His voice was gentler than before, and Go Se-won’s hair stood on end. After a brief silence, his lips parted.

“Yes.”

“I’d like to see the results as soon as possible. Is that too much to ask?”

Go Se-won already knew what his answer would be.

In the end, he was just another piece of shit in the same shit pit. Once he had stepped into the mud, it was too late to turn back.

“No. I’ll bring you good news by tomorrow at the latest.”

“Good. You may go.”

The conversation ended there.

Go Se-won moved his stiff legs and left the office, then raised a hand to his ear.

*Beep.*

A faint mechanical sound rang out, and the communicator he had turned off for a while lit up.

“Report the current personnel.”

As soon as the brief command ended, a sharp voice came through the communicator.

—Team One standing by in full. No abnormalities.

—Team Two standing by in full. No abnormalities.

—Team Three standing by in full. No abnormalities.

The three teams had thirty members in total. Even within Ares Guild, where only the best were gathered, they had been chosen from among the best of the best.

Go Se-won possessed overwhelming skill befitting the Head of Security, but even he could not easily guarantee victory if five or more of these men joined forces. No matter how thoroughly the target had prepared, there was no way to stop them.

“It’s the Vice Guild Master’s order. One hour from now, finish all preparations and move to the assembly point. The final destination is……”

Go Se-won paused, then spoke in a low voice.

“The United Kingdom. London.”

This trip did not require passports.

With advanced illusion magic and special makeup concealing their faces, names, and even fingerprints, they assembled in front of a long-distance Teleportation magic circle exactly one hour later.

Then they walked into the dazzling mass of light.

*Whooosh!*

* * *

The following morning, Go Jun heard the answer he had been waiting for from his Head of Security.

“It was a success. Of the thirty members of the security team, excluding the two fatalities……”

“What about Song Cheonwoo’s family?”

“……They were all captured alive. Teams One and Two remained behind, disguised as the existing security personnel, and have occupied the mansion. They’re keeping watch.”

“Well done. I knew I could count on you, Team Leader Go.”

“The team members paid a heavy price. We exploited every advantage we had and launched a surprise attack, but the mansion was guarded more heavily than expected, and two men were killed…”

“It’s fine. You handled the cleanup without any problems, right?”

After a short silence, Go Se-won’s tightly closed lips opened.

“Yes. We’ve seized their communications network, and we used enchantment magic to learn all their passwords and reporting procedures. Even if their people contact us, they’re unlikely to suspect anything.”

“How long do you expect it to hold?”

“Up to four days.”

“That’s enough time to finish the job. Contact that old man, Song Cheonwoo. Tell him the Lunar New Year is coming soon and that we should meet face-to-face after all this time.”

Imagining the expression on the face of the old traitor he would soon meet, Go Jun laughed aloud. Then he suddenly looked up.

“Oh, and Team Leader Go.”

Go Se-won, who had been staring at his superior with an inscrutable look, quickly composed his expression.

“Yes, Vice Guild Master.”

“Sorry. I heard such good news that I forgot.”

“Oh.”

“As you know, I’ve been out of sorts lately. You understand, don’t you?”

“Of course not!”

The answer came out with more force than before.

*That’s right. No matter how much a person changes, he wouldn’t do something like this.*

Go Se-won muttered inwardly and waited for the words he had been hoping to hear. But at Go Jun’s next remark, he froze in place.

“You’re always working hard. Put this aside for yourself.”

“……!”

*Swish.*

A spotless white envelope was placed on the table.

Considering the nature of the matter, it obviously contained a check for a substantial sum. Judging from his experience, it was probably at least ten billion won.

But the envelope Go Se-won wanted was not one containing a bonus.

And yet……

“Thank you, Vice Guild Master.”

Go Se-won accepted the envelope politely and bowed deeply.

By then, his gaze had grown deep and unreadable as he stared at the man reflected in the spotless, gleaming marble.

* * *

Martial arts consist of countless movements.

Thrusting and cutting. Striking and smashing.

When movements like these are linked together, they can finally be called a form.

*Whoosh. Boom!*

I punched into empty space. Compressed air exploded, and my hair fluttered.

I continued performing forms against an invisible opponent I had imagined before me.

*Whoosh-whoosh-whoosh! Slash!*

The insights I had directly witnessed and absorbed until now flowed into each form. They linked together naturally and continued without pause.

The connection between forms.

That was a combat sequence.

*Boom-boom-boom!*

The edge of my hand. My elbow. My shoulder. Every part of my body rotated and twisted as I struck in every direction.

If learning martial arts had taught me one thing all over again, it was that the word *weapon* did not apply only to sharpened blades.

*Anything that can wound an enemy is a weapon.*

That was why training mattered. A person could break someone’s neck with a single finger, or cut through a rock with a rusty carving knife.

*Whoom. Boom!*

My heel came down like lightning and slammed into the ground. Even an A-rank monster with a hard outer shell would have had its skull crushed instantly by that strike.

But there were no enemies to bring down in this space.

The corpses of a hundred or so human enemies—or perhaps a hundred or so monsters—were nothing more than phantoms I had conjured in my imagination.

“Hoo……”

At the moment I quietly exhaled—

*Clap, clap, clap.*

A vigorous round of applause rang out from behind me.
## Chapter artifact 568

# Chapter 568

*Clap, clap, clap.*

A vigorous round of applause rang out. At the same time, the voice of the person I had sensed for a while now echoed through the room.

“Impressive. Very impressive.”

*Click.*

Shiny black dress shoes moved toward me.

He wore suit pants with razor-sharp creases and not a wrinkle in sight. Over them, he had donned a leather coat that reached down to his knees. He stopped in front of me.

“Mr. Jin, I’ve heard a great deal about you…… but coming all the way here was worth it. You’re even more impressive than I expected.”

The sudden situation left me confused. At the look on my face, which clearly said I had no idea what was going on, he answered with a relaxed expression.

“There’s no need to be so flustered. The time has simply come.”

“The time has come?”

“Yes. Did you think you were the only hero in this world?”

“What?”

“From this moment on, you’ve become part of a much greater world. You simply don’t know it yet.”

“……!”

A sharp current ran through my entire body. I let out a low groan and glared at the unwelcome guest.

“What the hell are you?”

“There aren’t many people who know my true identity.”

He gave a quiet laugh and continued.

“If I were to introduce myself……”

“No, I’m asking what the hell you’re doing.”

“Huh?”

His eyes went round, his face showing that this wasn’t how things were supposed to go. I silently stared at his face, then waved a hand.

“Never mind. Keep going. You still have lines left, don’t you?”

“Would that be all right?”

“Of course. Finish it.”

“Ahem.”

He audibly cleared his throat, then continued with a deeply serious look in his eyes.

“My name is King Fury. Director of Barrier……”

*Wham!*

“Urgh.”

I punched him square in the face.

The Skeleton King staggered like a drunk. I didn’t let the opportunity pass and hammered him with a series of punches.

*Wham! Wham! Crack!*

“Urgh! Ugh! Wait! Wait! My jawbone!”

“Like hell I’m waiting, you bastard.”

This guy needed to get beaten up.

While some people were working their asses off day and night to build a bright future even in times like these, he had suddenly popped up dressed like a movie character.

I’d wondered why he had shown up wearing a leather coat he never usually wore.

“Are you having fun? Are superhero movies really that entertaining?”

The Skeleton King, who had been taking hits without a break, suddenly hardened his expression and raised his thumb.

“Totally fucking awesome.”

“…….”

“I hate them three thousand.”

“What the hell is wrong with you?”

“Wait! You cracked one of my bones!”

*Wham! Wham!*

“How can you call yourself human? Huh?”

“I—I’m a monster!”

“This bastard only starts screaming about being a monster when he wants to. Is your species a buffet? Are you choosing between two options?”

*Wham! Wham!*

“Wait! Stop for real this time! I’ve got an orbital fracture!”

“…….”

For a monster, he had a surprisingly accurate diagnosis.

My fist hesitated for a moment at the professional medical terminology. The Skeleton King quickly pulled away and fled, his entire body trembling with humiliation.

“You vile human. You aren’t even a person.”

“My God. What did I just hear from a monster?”

“You devilish creature. When Judgment Day arrives, may you fall into hell.”

“Have you been going to church lately? Your choice of words is unusually sophisticated.”

The Skeleton King paused and coughed awkwardly.

“Ahem. A human woman……”

“What?”

“A beautiful human woman spoke to me first. I met her at the crosswalk up ahead. She said that if I followed her, we could all sing together and eat delicious food.”

“……And?”

“So I went. It wasn’t particularly fun, but it wasn’t bad. A man called a pastor must have recognized the nobility of my person, because he even offered me a gift.”

“My God.”

An undead monster going to church.

Was this for real?

Just as I ran out of things to say, the Skeleton King lowered the coat collar he had turned up in the style of a middle-aged man from forty years ago.

“Heh heh. Behold.”

If I had doubted my ears before, now I doubted my eyes.

Peeking proudly out from between the coat collars was none other than a cheap cross necklace.

“This is the symbol of a noble king.”

“…….”

Wasn’t that a symbol of exorcism?

For a moment, I wondered if he had met an exorcist rather than a pastor. But Magic Johnson’s Illusion Magic was so perfect that I couldn’t find even the slightest hint of incongruity.

The Skeleton King’s followers on social media, which had multiplied exponentially, were proof of that.

*Click.*

“You’re taking selfies at a time like this? Should I smash your smartphone?”

“I bought it with my own money. A vile human has no right to say anything, so keep your mouth shut.”

A monster who had adapted to capitalism.

Wasn’t that the definition of a true monster?

Besides, he had bought it with his own money, so I had nothing to say. It wasn’t even secretly sponsored. He had paid for it legitimately with the money he had recently received from the Peace Guild.

“I’m quite a high-income earner among humans now. I hear that the people of this world divide themselves into classes based on their annual income. Mine is as much as six hundred million won. Heh heh. And that’s for the next ten years!”

“…….”

Welcome to ten years of slavery.

The Skeleton King was more than qualified to enter the S-rank if he were a Hunter, yet they were working him for the annual salary of a mid-level Hunter.

Team Leader Choi’s cruelty made me want to give Hyuk Mujin’s balls a sharp tap.

“What is that expression?”

“Nothing. Don’t worry about it. Just keep making lots of money.”

The Skeleton King narrowed his eyes and looked me up and down.

“Suspicious. It isn’t only now. Your behavior has been strange these past few days.”

“Who? The undead monster who went to church?”

“I’m talking about you, you vile human!”

The Skeleton King shouted angrily, then continued.

“You keep sinking into thought even in Gates. A man with not so much as a finger joint’s worth of culture draws pictures and even takes notes. Yesterday, you even refused an emergency rescue team call, forcing this king to make the journey himself!”

He was surprisingly perceptive for a monster. Maybe it was because he had been the one closest to me most often lately.

I scratched my chin, then countered the Skeleton King, who had just finished his impassioned speech.

“I know what you’re trying to say. So what?”

“Huh?”

“What do you want me to do about it? Am I not allowed to think? Am I not allowed to draw a few pictures and take some notes?”

“I—I’m not saying that.”

The Skeleton King faltered for a moment, then immediately began arguing back.

“Even if we set all that aside, the emergency rescue team call……”

“I delegated it because I could. Even if I wasn’t there, they still had you.”

“Wha—what?”

“It wasn’t a Mutated Gate, and when I saw how much the mana level had risen, I figured it would be fine. So I sent you instead of going myself.”

“Y—you sent me instead?”

The Skeleton King blinked with his mouth hanging open, then stammered out a question.

“Why?”

“Because I can trust you to handle it.”

“……!”

“Until now, I kept going with you just in case. But I’d seen what you could do firsthand, and after listening to what the people around us had to say, I figured you could go alone.”

The Skeleton King was a Named Monster in every sense of the word.

He had possessed powerful abilities even back when he was called a Warlord, but after his battle with the Arch Lich, he had evolved into an even more powerful being.

*An ordinary Named Monster wouldn’t stand a chance against that guy.*

From everything I had directly witnessed while fighting alongside him, he possessed excellent physical abilities. On top of that, he could use his own Authority to create a one-man army.

In that regard, none of the S-rank Hunters currently alive could match the Skeleton King.

Well, a Grand Mage who could dominate a battlefield like Magic Johnson might be another story.

*And then there’s me.*

Even without considering anything else, the undead Lü Bu was more than capable of sweeping through a Gate by himself.

There had been only one reason I had deliberately kept such a powerful Skeleton King at my side.

*His absolutely insane lack of social skills.*

He had never revealed his identity in so many words, but he went around advertising to everyone that he had been born to be a monster.

If I had taken him to the official Blue House press conference last time, he would have referred to President Baek Hanseong as a “human male.” Then the Liberation Army, led by the Lady of the House, would surely have risen up, waving Korean flags and demanding that they investigate the identity of that long-nosed bastard.

But now……

“This hyung is relieved. You even went to church, kid. From now on, try living a little more freely.”

*Pat, pat.*

The Skeleton King’s eyes widened at the warmth of my hand as I patted his shoulder. Or perhaps it was because of the one word I had just used.

“F—freely?”

“Yes. You’ve reached the point where I can trust you with things, so I should give you that much freedom.”

“Vile human. Weren’t you watching me?”

“Watching you?”

I gave a quiet laugh and continued.

“After you saved my life in China?”

“That was……”

“Of course, you owe me something too. Neither of us needs to say it out loud, but just know that I’m always grateful.”

“……!”

His golden eyelids trembled faintly. The Skeleton King stared at me with an expression difficult to describe, then opened his mouth with moist eyes.

“Vile human.”

“Oh, shit. Don’t say anything.”

“But I have to say this.”

“Don’t. Seriously. I don’t like this kind of atmosphere.”

It felt as if soft background music were playing somewhere. Uncomfortable, I looked off toward a distant mountain, and the Skeleton King’s voice reached my ears.

“Then can I go to a club tonight?”

“…….”

“I’ve been tricked by that mage and gone to a gay bar twice already. This time, I absolutely want to achieve a noble grinding session at a club.”

“…….”

A noble grinding session, my ass.

Give me back my emotions, you bastard.

“Please, vile human. I swear I’ll return before midnight!”

“Fine. Go.”

“R-really?”

“Yeah. Go. If you want to die.”

“…….”

“Crazy bastard. A club, my ass. What kind of trouble are you planning to cause?”

Hearing that he had gone to a gay bar twice did make me feel a little sorry for him, but the Skeleton King still wasn’t socially developed enough for that.

It wasn’t because I had never been to a club myself.

……It really wasn’t.

“Why? How can this happen when I’m so handsome!”

Just as the Skeleton King let out a sorrowful howl, the smartphone in his hand began to vibrate.

*Bzzzz.*

The moment he checked the screen, his face twisted miserably. I didn’t need to look to know why. The answer might as well have been projected as a hologram.

“Did you get an emergency call?”

“……Damn it.”

The timing was unbelievable. After checking the contents of the call, I raised my head and stared directly at the Skeleton King.

“What are you waiting for? Why aren’t you going?”

“I refuse, vile human. You go this time.”

“What are you talking about? You can tell what the situation is as soon as you look at it. This is more than manageable for you alone.”

“Damn it. Why are you playing around here while I’m the one working?”

Playing around? Who was playing around?

But there was no way the Skeleton King could know what I was doing.

I gave a quiet laugh and raised a hand instead of answering. The moment he noticed what I meant, he quickly slipped out the door.

*Bang!*

The door closed with a resounding crash.

It did not open again from sunset until the following morning.

And then……

*Inhale. Exhale.*

*Whoosh. Boom!*

In that quiet, isolated space, I endlessly repeated circulating my qi and training.

It was a long journey in search of a new path I had never traveled before, holding on to a faint thread of understanding in my hands.

* * *

A pale complexion. Trembling fingertips.

When had it begun?

Partway through listening to the story, a bead of cold sweat ran down the back of his neck and dropped with a soft *plop*.

“W-what did you just say?”

He had the imposing build of a man whose age of seventy seemed impossible, along with the face of a middle-aged man. But the voice that slipped between his lips was as faint as that of someone standing on the brink of death.

The story he had just heard from another person contained information that was every bit as shocking as that.

“Th-that is……”

Even remembering what he had heard made his vision swim. The old man barely pulled himself together and forced out his trembling voice.

“You—you kidnapped our children?”

“‘Kidnapped’ is a rather unpleasant way to put it. Someone might misunderstand.”

“H-how dare you.”

“So let’s call it protection.”

Beyond a table covered with all manner of elaborate dishes, Go Jun answered in a light tone and bit into a steak.

Juice from the rare-cooked beef ran down his angular jaw. Along with it, the single remark he added as though in passing dug into the old man’s ears.

“For now, at least.”

“……!”

As he watched the old man—Song Cheonwoo—stare back with a frozen expression, Go Jun smiled pleasantly.
## Chapter artifact 569

# Chapter 569

*Boom.*

The sound of the door closing behind him rang out like thunder. At the same time, Song Cheonwoo’s sturdy frame—one that made it hard to believe he was seventy—staggered.

*Slide. Tap.*

His powerful mana and the experience he had built up after weathering countless hardships were useless at that moment.

As he clutched the wall and glared at the floor, a pair of black dress shoes suddenly intruded into his field of vision.

“Are you all right?”

The businesslike voice pierced his ears. Song Cheonwoo raised his head to confirm the owner of the shoes and gritted his teeth.

“Does this look all right to you?”

At the fire flashing in his eyes, Head of Security Go Se-won bowed his head.

“I’m sorry if that sounded insensitive.”

“Spare me the empty words. Before I break your neck!”

“I wouldn’t recommend that. You’d gain nothing and only stand to lose.”

As he spoke, Go Se-won gently waved one hand.

The security-team members who had just begun moving from the far end of the hallway, having noticed that something was wrong, stopped where they were.

“They’re my men. As you know, Director, they’re quite capable. And when the situation calls for it, they don’t care what they have to do.”

“You…”

“Please don’t misunderstand me. I’m saying this because I don’t want you to make the situation any worse.”

*Crack.*

As strength surged through the hand braced against the wall, the marble surface—reinforced with magic—split like a spiderweb.

Song Cheonwoo glared at Go Se-won with bloodshot eyes and spat out the words through clenched teeth.

“So you kidnapped my children even though they had nothing to do with this and had committed no crime?”

“They were exceptionally well guarded for people who supposedly had nothing to do with it. That means you had at least considered the possibility, Director.”

Even though the entire security team had launched the attack, two of them had died.

Considering the level of the elite Hunters who were regarded as the best Ares Guild had to offer, those two deaths deserved the words *no fewer than* in front of them.

“I do regret what happened to your family. But if you suspected something in advance, you should have protected them by deploying even more forces.”

“……!”

“I shouldn’t have said that. I apologize.”

Go Se-won’s words had been sincere. Song Cheonwoo was already in a situation no different from that of an old lion who had been given a date for his death. There was no need for Go Se-won to step forward and drive a dagger into his heart as well.

*If I say those words simply slipped out because I felt sorry for him, will he believe me?*

He was a father too. His first son, born after he turned forty, and his second child, due in a few months, were already unimaginably precious to him.

Go Se-won could give his life for the safety and happiness of his children. That was what it meant to be a father. To be a parent.

But Song Cheonwoo had placed his ambition and his family’s safety on opposite sides of a scale.

Then again, if he had considered the worst-case scenario, he would never have tried to make Go Jun his enemy in the first place.

*……It isn’t my place to say that.*

Go Se-won felt like a pathetic villain.

For nearly fifteen years, he had lived a life that was better described as that of a fixer than a Hunter.

Ever since Lee Jungryong had taken notice of him and brought him into the security team, his primary targets had not been monsters but people.

He was the one who had ordered his men to kidnap Song Cheonwoo’s family and then cleaned up the aftermath.

*And I have the nerve to lecture someone else.*

In the end, they were all just pieces of shit in the same cesspool.

Song Cheonwoo had been consumed by ambition on the verge of retirement and brought danger upon himself. Go Jun had wielded his blade without regard for means or methods. And Go Se-won had become the sword in his superior’s hand and kidnapped Song Cheonwoo’s family.

*A war between bastards. In the end, all that remains are the victor and the defeated.*

And he was nothing more than a component.

Just as Go Se-won was bitterly savoring that thought—

*Lunge!*

A powerful hand that was hard to believe belonged to a seventy-year-old man seized him by the collar.

“Team Leader!”

“Enough. Stay at your posts.”

Go Se-won restrained his men and calmly looked up at Song Cheonwoo, who was a full head taller than him.

“I already told you. You’ll suffer more losses than gains.”

“You bastards dare lay a hand on my children…”

“The Vice Guild Master is listening inside. I don’t know what the two of you discussed, but I hope there won’t be any more unnecessary sacrifices.”

“……!”

In other words, do not provoke Go Jun, who held the lives of his family in his grasp.

Song Cheonwoo immediately understood the meaning behind those words, and his eyelids began to tremble.

He continued glaring at Go Se-won with his teeth clenched, but the strength gradually seeped out of his grip.

“You made the right choice.”

“……Shut your mouth. I want nothing more than to smash your face in right now.”

“I’m sure you do.”

A bitter smile crossed Go Se-won’s lips. He would have reacted the same way in Song Cheonwoo’s position.

And by any objective assessment, Song Cheonwoo was still an extraordinary fighter, even though twenty years had passed since he retired from active service.

His abilities had simply fallen short of his ambition. The fact that he had once been Lee Jungryong’s political rival was enough to explain what kind of man he was.

*That’s why he chose such a filthy method.*

Go Jun’s method this time displeased him, but for all its filthiness, its effectiveness was undeniable.

Song Cheonwoo would be eliminated soon. Naturally—so naturally that no one would suspect a thing.

“Follow me. I’ll escort you outside.”

Go Se-won gave a slight bow and walked ahead. Song Cheonwoo glanced once more at the tightly closed door, then followed him.

*Step. Step.*

Because Go Se-won had sent his team members away, only the footsteps of the two men echoed through the hallway.

The silence that followed was broken by Song Cheonwoo’s voice.

“What you said earlier. Was it true?”

“……?”

“You said you didn’t know what Go Jun and I had discussed. Was that true?”

Go Se-won thought for a moment about the meaning behind the question, then quietly nodded.

“I see. Then again, according to what I investigated, you’re hardly the strategist type.”

“What does that mean?”

“You’re apparently not as trusted a subordinate as I thought. Or perhaps he wanted to hide it even from his closest aide.”

At the sight of Go Se-won frowning, Song Cheonwoo let out a weak, hollow laugh.

“Go Se-won.”

In the brief span of time between one breath and the next, he seemed to have aged ten years. No—twenty. He continued in a desolate voice.

“There’s such a thing as a line a person shouldn’t cross. You know that?”

“……If you’re going to criticize the Vice Guild Master, I’d like to ask you to stop there.”

“Criticize? That’s a much gentler word than I expected. It’s far too mild for that bastard Go Jun.”

“I understand how you feel. But no one involved in this matter has the right to condemn anyone else. I know that you haven’t lived a particularly clean life either, Director.”

“Hah. That’s true. There was a time when I didn’t care what means I used to achieve my goals. But I never went this far.”

At Song Cheonwoo’s empty, almost deranged laughter, Go Se-won suddenly fell silent.

He realized that Song Cheonwoo was not talking only about the kidnapping.

*What is this?*

His heart pounded. Electricity ran down his spine.

This was a warning. A danger signal telling him not to listen.

But his body moved contrary to his thoughts.

“What do you mean by that line, Director?”

“A monster who has forgotten even the most basic duty of being human.”

“What?”

*Step.*

Song Cheonwoo abruptly stopped walking. He stared silently at the Teleportation magic circle leading outside, then continued.

“The boundary between humans and monsters. That bastard Go Jun…… has already become a monster.”

For a moment, the old man’s empty gaze swept across the air.

As he rummaged through the memories of a brilliant past, Song Cheonwoo weakly stepped toward the magic circle.

He left behind one final plea.

“I apologize for what I did to you. So please, stop those children from dying a meaningless death.”

That was the last thing he said.

*Flash!*

Before Go Se-won could ask what he meant, Teleportation magic manifested, and dazzling radiance swallowed Song Cheonwoo’s body.

Left alone, Go Se-won stared at the spot where Song Cheonwoo had been standing with a bewildered look in his eyes. Then he suddenly turned his head.

A hallway made entirely of pure white marble.

At the end of the hallway that stretched endlessly ahead stood a tightly closed door. Behind it was someone who was probably sipping wine in satisfaction.

*What in the world…… have you done?*

Go Se-won muttered toward something deep inside his heart.

Section A, which was always filled with light, felt like a pit overflowing with darkness today.

* * *

I had no idea how long I had been shut away in the training ground—a place people in the modern world called a training room.

A day. Two days. Maybe three.

With walls surrounding me on every side and the temperature regulated, I had become so absorbed in martial arts that I could not properly feel the passage of time.

Even though I had a smartphone, I never looked at it, so I had no way of knowing. Perhaps they vaguely understood my situation, because no one from the Peace Guild came to see me or contacted me.

“…….”

Now that I put it that way, I sounded like a complete loner. But that was absolutely not the case.

……Probably not.

*The Skeleton King hasn’t come to see me even once since then, either.*

It was good news that he seemed to be handling things better than expected, but that also meant the emergency rescue team had grown busier and that more Gates were exhibiting abnormal phenomena. It was not something I could simply celebrate.

And in that sense, the fact that what I was attempting was almost complete was definitely good news.

*Of course, it’s still unfinished.*

Perhaps because it was my first attempt, the process so far had been far from easy.

The pressure of having to create something exceptional while the current situation was on the verge of exploding may have contributed as well.

*What I have so far seems good enough……*

Should I just take the plunge and go with it?

I was repeating that same dilemma in my head—the one that had occurred to me dozens, perhaps hundreds, of times—when the tightly closed door to the training room opened with a familiar mechanical sound.

“So this is where you were. I need your help, as it happens.”

*Step. Step.*

Polished combat boots. A blue skin-tight suit and a shield emblazoned with a skull.

I looked at him with a gaze colder than the snow piled atop the King Sejong Station building in Antarctica.

“Look at that fucking bastard.”

“You heard from Director King Fury, didn’t you?”

“……Are you playing two roles now?”

“Heh heh. Surely any citizen of the United States of America should be King-tin America.”

“This bastard keeps changing his name however he wants. I’m going to beat you so badly you’ll want to go back to the glacier.”

“I can do this all day.”

*Whoosh! Boom!*

The White Flame spearhead shot out like a streak of light, grazed his neck, and pierced through the wall of the training room.

The Skeleton King stared back and forth between me and the spear embedded in the wall all the way to its shaft, then muttered.

“Doing this all day might be a little difficult……”

“Cut the bullshit. Why are you here? And for the record, if you just stopped by because you were bored, you’re going to die. I mean it.”

The Skeleton King hurriedly answered.

“N-no, it’s not that. It’s a mission. A mission!”

“A mission?”

“That is correct, wicked human.”

He nodded and continued.

“It is not an ordinary Mutated Gate. The magic power reading is enormous.”

“……!”

Damn it.

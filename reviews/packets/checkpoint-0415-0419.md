# Checkpoint Review — 415–419

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

# Chapters 415–419

## Plot

The coalition launches its assault on the Arch Lich’s monster army. Magic Johnson and Faye Chen devastate the advancing forces while Ares Guild and the suicide squad push forward. Jin Taekyung, Lee Jungryong, and Wu Heixing break through together as a three-S-rank strike force and enter the Arch Lich’s stronghold, a city being transformed into one enormous Gate.

The System activates the quest **One Who Returned from Death** and disables Login until it ends. Inside the city, Jin exposes Lee and Wu’s plan to betray him and use him as a disposable fighter. Wu admits he expected Jin to die, while Lee intends to prolong the war for profit. Jin kills Wu, then defeats Lee in a fierce battle after recognizing and overcoming his own underestimation of Lee’s qi and swordsmanship. Lee dies without regretting his choices, and Jin gains two levels.

Before dying, Lee preserves an edited hologram of Wu’s death that can portray Jin as a murderer and damage the Peace Guild, his mother, and Hayeon. With the Gate transformation still underway, Jin prepares to confront the Arch Lich, but the Skeleton Warlord trembles and warns him that the Arch Lich is near.

## Continuity

- Jin Taekyung, Lee Jungryong, and Wu Heixing entered the Arch Lich’s city stronghold after breaking through the monster army.
- The city is undergoing **Gate transformation** through the Arch Lich’s anchored mana; the process is not yet complete.
- Jin killed Wu Heixing and Lee Jungryong. Lee died believing his actions were the ending most suited to him and claiming he had no regrets.
- Jin gained two levels after defeating Lee and remains capable of fighting the Arch Lich.
- Lee’s edited holographic recording of Wu’s death remains a serious threat to Jin, the Peace Guild, Jin’s mother, and Hayeon if released.
- Lee’s life was defined by Cheon Taemin, whom he regarded as an older brother, unreachable hero, and sworn-brother figure.
- The quest **One Who Returned from Death** remains active, keeping Login unavailable.
- The Arch Lich is now present before Jin.
- The Skeleton Warlord remains frightened and trembling, suffering unexplained dizziness and nausea while urging Jin to turn back. The cause of his reaction is unresolved.
- The coalition’s battle outside the city and the fate of the Arch Lich’s remaining army remain unresolved.

## Translation Decisions

- Render **아크 리치** as **Arch Lich**.
- Render **게이트화** as **Gate transformation**.
- Render **어둠에 잠식된 도시** as **City Consumed by Darkness**.
- Render **죽음에서 돌아온 자** as **One Who Returned from Death**.
- Render **착짱죽짱** as “The only good chink is a dead chink.”
- Render **형님** as **hyung** when Lee uses it, without resolving the identity.
- Render **의형제** as **sworn brothers**.
- Retain **Force**, **EXP**, **Hero’s Soul**, **Formation J**, and **suicide squad** as established renderings.

## Durable state

{
  "active_continuity": [
    "Jin Taekyung killed Lee Jungryong, who died believing his actions were the ending most suited to him and claiming he had no regrets.",
    "Lee Jungryong first met Cheon Taemin during the early Great Cataclysm, regarded him as an older brother and unreachable hero, and spent much of his life in his shadow.",
    "Jin Taekyung gained a massive amount of EXP and leveled up twice after defeating Lee Jungryong.",
    "Lee Jungryong's edited hologram of Wu Heixing's death remains capable of turning public opinion against Jin and those he protects.",
    "The city remains in the process of transforming into one enormous Gate through the Arch Lich's anchored mana.",
    "The Arch Lich, responsible for the city's Gate transformation, is now present before Jin Taekyung.",
    "The Skeleton Warlord remains frightened and trembling in the Arch Lich's presence, with the cause of his reaction still unexplained.",
    "The Quest One Who Returned from Death remains active, keeping Login unavailable until the Quest ends."
  ],
  "continuity_sources": [
    419
  ],
  "open_questions": [
    "Can the three Hunters stop the city's Gate transformation?",
    "What is causing the Skeleton Warlord's fear, dizziness, nausea, and insistence that they turn back?",
    "What will the Arch Lich do now that it has appeared before Jin Taekyung?"
  ],
  "safe_through": 419,
  "temporary_decisions": [
    "Render 아크 리치 as Arch Lich.",
    "Render 어둠에 잠식된 도시 as City Consumed by Darkness.",
    "Render 죽음에서 돌아온 자 as One Who Returned from Death.",
    "Render 착짱죽짱 as “The only good chink is a dead chink.”",
    "Render 형님 as hyung when Lee uses it, without changing the established Cheon Taemin relationship."
  ],
  "version": 1
}

## Reading copies

## Chapter artifact 415

# Chapter 415

The battle began quickly.

Before the tens of thousands of monsters and the thick fog that rolled over the wasteland like waves, a black-skinned Archmage stood tall, stepping on empty air, and uttered the first word of the battle.

“Fire Cannon.”

*Fwoooooosh.*

An enormous amount of mana swirled around him. Five flames rose from empty air, swelled in size, and shot forward like cannonballs.

*Fwoooooosh—BOOM!*

The black wave composed of tens of thousands of monsters split apart. Superheated air burned flesh and bone and melted the ground.

An area-of-effect spell that reduced at least a thousand soldiers to ash.

But the monsters did not stop.

And neither did Magic Johnson.

“Water Blaster.”

The air, dry as sand when he cast Fire Cannon, grew damp with moisture.

When Magic Johnson spread both arms, a massive wave rose behind him.

It was a sight that defied every law of the world.

It was magic in the truest sense of the word—the very embodiment of the supernatural power displayed by the greatest War Mage among countless mages.

“Cover them.”

The cheerful man who was always laughing was nowhere to be seen.

Magic Johnson flung both hands out, his gaze grave. A wave dozens of meters high cast a broad, dark shadow over the tens of thousands of monsters.

*Roooooar!*

The wave, brimming with mana, crashed down. Under the tremendous water pressure, the monsters’ bodies burst apart and were torn into pieces.

The flames left behind by Fire Cannon went out, and the surrounding area was flooded with water.

Magic Johnson knew exactly what he had to do next.

“Rain down. Lightning Rain.”

It happened in an instant.

Black storm clouds gathered over the monsters’ heads, and dozens of bolts of lightning came crashing down.

*BOOM! Crackle!*

—Kraaaaaaar!

—Kyaaak!

The lightning struck targets in the air and on the ground indiscriminately.

Blackened Gargoyles and Griffins fell from the air, while the ground, soaked by Water Blaster, carried the current.

The living monsters trembled violently and dropped to their knees with a single shriek. The undead collapsed into piles of ash.

At the unbelievable sight unfolding before our eyes, a groan escaped someone’s lips.

“This is an Archmage…”

The result of only three area-of-effect spells was staggering.

At least several thousand monsters had either died or been rendered incapable of fighting, and one flank of the monster army had collapsed.

But the Archmage who had single-handedly caused a natural disaster could not help but feel exhausted.

“Fuck. If I’d known this would happen, I would’ve saved a few more spells.”

Casting magic was difficult. Magic Johnson’s specialty, area-of-effect magic, consumed an incredible amount of mental strength and mana in proportion to its destructive power.

Considering the magic he had poured out on the front lines before arriving here, this was his limit.

“Mrs. Chen. I guess I’m getting old too.”

“Move aside. Old people have to help one another. And…”

Faye Chen threw away the whiskey bottle in her hand, drew the bow strapped to her side at lightning speed, and pulled back the string.

An arrow made of mana formed on the empty bowstring.

“Not Mrs. Chen. Miss Chen. Who decided I was married?”

Faye Chen snorted and released the bowstring.

The mana arrow, scattering a dazzling radiance, shot forward with a sharp whistle. It erased the space in its path and split through the thick fog.

And then—

*BOOM!*

A huge explosion erupted.

After confirming that the Death Knight hiding among the countless monsters had vanished without even managing a final cry, Faye Chen pulled back her bowstring again.

*Thrum-thrum-thrum!*

The arrows shot in the blink of an eye became streaks of light that crossed the wasteland. Thunderous booms and explosions rang out. With every arrow, dozens of monsters were swept away and annihilated.

If Magic Johnson was an Archmage counted among the top three in the world and the greatest War Mage alive, Faye Chen was the world’s finest archer.

But…

—Gwooooooar!

—Kyaaaaa!

The monster army numbering in the tens of thousands ignored everything and charged.

Whenever dozens fell, dozens more filled their places. Whenever hundreds fell, hundreds more took their place.

Surging through the thick fog, they were stronger and more ferocious than ordinary monsters.

Now, only an unavoidable frontal battle remained.

The two of them stepped forward at the same time, facing the oncoming monster army.

“Ares Guild. Formation B. Break through them.”

*Clatter-clatter-clatter!*

At Lee Jungryong’s low voice, the elite Guild members who had reached this place without suffering a single casualty moved as one.

Jin Taekyung watched them closely, then spoke to the suicide squad he had brought from the Western Front.

“Everyone, Formation J.”

“Yes, sir!”

“Formation J! Get into position!”

With thunderous call-and-response, the suicide squad moved swiftly.

Behind Jin Taekyung, Wu Heixing had been gathering the handful of Red Guard Gang Hunters who remained. He grabbed one of the Western Front suicide-squad members and asked,

“Hey, rookie. What the hell is Formation J?”

Shao Shen, who recognized Wu Heixing, frowned and answered,

“Hyung is the one who came up with this battle formation.”

“So what does that mean?”

“Nothing special. He said it means, ‘Just fucking fight.’”

“…”

Wu Heixing was momentarily speechless, and Lee Jungryong and Jin Taekyung launched themselves forward at the exact same time, as if they had planned it.

Prince Felix and ten thousand Hunters followed fiercely behind them.

“Aaaaaaaaah!”

—Kraaaaaaaargh!

Humans and monsters.

Monsters and humans.

Deafening battle cries and killing intent erupted. Crossing the wasteland at blinding speed, the two sides thrust teeth, spears, and blades at one another.

*Fwoooooosh—Kra-d-d-d-d-k!*

The great battle had begun.

* * *

I leaned back, putting strength into my shoulder. With a fluid motion, I whipped my arm forward with all my strength.

*Whoosh—thud-thud-thud-thud!*

White Flame shot from my hand and pierced through dozens of monsters, opening a path.

A gap suddenly appeared.

Without hesitation, I plunged into the opening and swung my arms and legs at anything within reach.

*Crack!*

My fist shot forward at a speed too fast to see, and the head of the Lycanthrope charging at me crumpled like a watermelon.

Before the brain matter flowing from its skull could even reach the ground, I leaped upward.

*Tap—whoosh!*

It stood nearly four meters tall. My reflection appeared in its pale pupils, long since drained of light.

But before the Undead Troll could swing the club in its hand, my palm struck its chest.

*Boom!*

Along with tremendous heat, smoke rose from the Undead Troll’s seven openings. It had suffered massive internal damage and met its final death before it could even bring its characteristic regenerative power into play.

—Wicked human! Behind you!

*I know, idiot. Who asked for your advice?*

I turned my head. A lance infused with black magic skimmed dangerously past my neck and shot into the air.

It was a thrown spear aimed at the moment I was airborne. The timing was good, but the enemy had made one mistake: it had underestimated me.

“Fuck. Why are there so many Death Knights? This isn’t a chicken joint.”

A Death Knight riding a skeletal horse charged rapidly toward me.

—This. Is. As. Far. As. You. Go!

*Fwoooooosh!*

Along with its shout, the sword infused with ominous magic swung toward me. It could not compare to an S-rank Hunter, but the energy it radiated was comparable to that of a top-tier A-rank Hunter.

Or perhaps…

*This Death Knight must have been a Hunter once too.*

Maybe that was why.

The Death Knight’s appearance reminded me of Lei Fei, and a bitter feeling briefly settled over me.

Seeing me like that, the Skeleton Warlord screamed.

—Dodge, human!

*Thud!*

The magic clinging to the sword vanished as if it had been washed away.

The Death Knight stared blankly at the transparent spearhead that had pierced through its chest and emerged from its back. Then it muttered weakly,

—How…

“This is as far as you go.”

I returned the Death Knight’s own words to it and brought down the edge of my hand.

“I don’t know who you were, but you’ve been through a lot.”

*Slash—thud!*

The skeletal horse and the Death Knight split in two and vanished.

Using Seizing an Object Through Empty Space to pull White Flame toward me, I cut down a monster just as I had before, then suddenly opened my mouth.

“How come you’re not pestering me for food today?”

—Ahem. What do you take me for? How dare you mistake this commander for—

*Slash!*

“Food parasite. You call yourself a pacifist, but you only drool at times like this. Shameless bastard.”

—What did you say?

“Why? Isn’t every word true?”

—You, wicked human, agreed that I should not participate in the battle! And when you told me I couldn’t let the other humans find out about me, when did you suddenly change your tune?

“Quit making excuses. So, are you going to absorb that mana or not?”

—…

*Crack!*

“Hey. You hear me?”

—Hmm. I don’t particularly want to absorb it.

“…What?”

*Fwoooooosh!*

I was so startled that I almost let an attack hit me.

After swinging my spear in a wide arc and sweeping away a dozen monsters, I asked seriously,

“What’s wrong? Is it time for you to vanish?”

—Hmm… I don’t know either. I just feel this way.

“Feel this way?”

—Yes. I’m undead too. Sometimes I feel unsettled. Leave me be.

“…When does an undead get unsettled?”

Normally, he would have charged in like a Beggars’ Sect disciple who had not eaten in four days. Why was he acting like this?

*Can undead go through puberty too?*

No matter how strange a monster the Skeleton Warlord was, that made no sense.

I gave up on thinking about him and continued cutting down monsters.

That was when it happened.

*Rooooooar!*

Aura—no, Sword Energy—covered a radius of more than ten meters.

A person landed lightly in the center of the front line, which had suddenly been emptied.

“There are too many monsters. It’s impossible to make a path for the entire suicide squad to get through.”

I understood exactly what Lee Jungryong meant.

“You’re saying we should go with a small elite force?”

“That’s right. Duck.”

At Lee Jungryong’s words, I leaned backward, and a crescent of Sword Energy flew past me, slicing three or four enormous monsters apart like cheesecake.

*What if that Sword Energy had been aimed at me? If Lee Jungryong and I fought…*

“You, me, and Wu Heixing. The three of us should be enough.”

I licked my dry lips and answered,

“That’s a strange thing to say.”

“What is?”

“You never know until you fight. We’ll only know how strong the Arch Lich is after we face it.”

“There are three S-rank Hunters here. No matter how strong the Arch Lich is, it cannot stand against us.”

*Us…*

It was a wonderful word. So why did I dislike the way it felt rolling off my tongue?

Maybe it was because of the people included in that word.

But I had already made up my mind when I proposed the suicide-squad operation. In that sense, Lee Jungryong’s suggestion was the best option.

“Let’s do that. Where is Wu Heixing?”

*Kra-d-d-d-d-k!*

Before I had even finished speaking, Wu Heixing appeared, tearing through the monsters.

Unlike Lee Jungryong, who looked so clean that it was hard to believe he was in the middle of a battle, Wu Heixing was in terrible shape. But the fierce light in his eyes proved that he still had plenty of strength left.

“Good. You made it in time.”

Wu Heixing let out a ragged breath. “Mere monsters could never stop me.”

*Didn’t that bastard nearly die to those very same monsters about an hour ago?*

A moment later, a shout came from far away.

“Mr. Jin!”

Team Leader Choi’s voice.

His face appeared and vanished in the distance, beyond the hundreds of monsters between him and me.

Then something flashing spun through the air and struck the ground nearby.

*This is…*

I recognized it without difficulty.

It was **Hero’s Soul**.

From somewhere I could not see, Team Leader Choi shouted,

“I’m not going to say I’ll go with you, so take that sword with you instead. And… be careful!”

His words carried many meanings.

Without saying anything, I pulled **Hero’s Soul** from the ground.

Beyond the countless monsters still filling my field of vision, I could see a city shrouded in darkness.

“Let’s go.”

Lee Jungryong smiled gently.
## Chapter artifact 416

# Chapter 416

Breaking through a fierce battlefield where an army numbering in the tens of thousands was locked in combat was nearly impossible.

But…

“Rage forth. Blizzard!”

“Johnson. Aren’t you pushing yourself too hard? If you keep this up, I can’t just stand by either.”

If the war hero of the Great Cataclysm and the world’s greatest War Mage and archer unleashed area-of-effect magic of tremendous power and arrows like bolts of lightning…

“For Her Majesty the Queen!”

“Long Live The Queen!”

If an S-rank Hunter who had appeared like a comet—the prince of the United Kingdom—led the kingdom’s elite royal knights into a charge…

“Formation J! Wipe them all out!”

“Just fucking fight!”

“Yeeeeeeah! Let’s gooo!!!”

And if the hundreds of members of the suicide squad who had come this far prepared to make a noble sacrifice advanced as one…

*Roooooar!*

*Crack-crack! Slash!*

A path opened.

A path meant for only three people.

It was the last way out that could end the war, and they crossed through the tens of thousands of monsters like a streak of light.

*Shraaaaaaash!*

A dazzling storm of light erupted from two swords and a single spear, sweeping through the monsters.

The head of a Lycanthrope that had bared its sharp fangs shot into the air, while the limbs of the six-meter-tall boss monster, the Twin-Headed Ogre, were torn apart.

Five Death Knights who had each been commanding a legion appeared and moved to block them, but nothing changed.

—In. The. Name. Of. Our. Lord.

—Let. Death. Descend.

Jin Taekyung tossed out a single remark.

“Two, two, one. Sound good?”

Lee Jungryong nodded.

“Let’s do that.”

“Wait. What the—!”

Before Wu Heixing could finish objecting, the other two had already dashed forward.

They closed the distance in an instant with only two steps, then swung the sword and spear in their hands without hesitation.

*Boom!*

The first exchange. The Death Knight staggered after blocking the Force that had curved like a whip.

Its eyes widened at the sight of the magic-infused sword shattering into pieces.

—How…!

*Boom! Crunch!*

The second exchange. The third. And then—

*Slash!*

A lightning-fast One Strike that signaled the end.

The upper half of the Death Knight’s body, armor and all, slowly slid away. Between the gaps of its deeply lowered helmet, the light in its eyes flickered like a candle before the wind, then vanished.

Before the bodies of the Death Knights they had each taken responsibility for even touched the ground, Jin Taekyung and Lee Jungryong were already charging toward another enemy.

“Damn it! I’m here too!”

Wu Heixing joined them a moment late.

The fate of the three remaining Death Knights was already as good as sealed.

The monsters that witnessed their commanders’ destruction instinctively felt fear and retreated.

*More. More. More.*

*Slash! Shraaaaaash!*

Jin Taekyung cut and smashed his way through everything around him as he advanced. Then, at some point, he realized it.

*They’re gone.*

The monsters that had endlessly blocked their path were nowhere to be seen anymore. Only a ruined road and vast plains stretching out on either side remained.

At the end of them, a city shrouded in thick fog awaited them.

* * *

Lee Jungryong, Wu Heixing, and I raced toward the city where the Arch Lich was waiting.

—Wicked human. This commander has a long-held wish.

*What is it?*

—It is to return to my homeland and enjoy a peaceful daily life.

*You don’t even remember where your homeland is.*

—…How could you say something so cruel?

*Ah, sorry. I didn’t mean it like that. So, where is your homeland?*

—The first place where I regained consciousness. Korea. I have decided to make it the homeland of my heart.

“…”

I faltered as I ran toward the city.

*Is he insane?*

A monster trying to obtain citizenship. An undead illegal immigrant who had slipped into the country through a Gate, and yet he had no shortage of things to say. His intention was obvious, of course, even if he was going this far.

—So please, let’s turn back.

*No.*

—My head has felt dizzy and my stomach has been churning for a while now.

*That’s strange. The more I talk to you, the more I think I’m developing similar symptoms.*

—It isn’t too late yet! Please stop! If we go in there, there really will be no turning back!

*No.*

*It’s already too late.*

I muttered the words inwardly and took another step.

As we entered the city, unnaturally thick fog and frigid air greeted us first.

At the same time, a familiar energy that I had felt countless times before—but somehow different—brushed across my entire body.

“This is…”

It was a sticky, unpleasant energy. It did not take me long to realize what it was, and Lee Jungryong and Wu Heixing reached the same conclusion.

“Mr. Lee…”

“Yes. I see.”

Lee Jungryong swept his surroundings with a somber gaze, then spoke.

“It’s a Gate. I wondered where so many monsters were pouring out from, and now we know. There was a reason for it.”

Lee Jungryong’s guess was wrong.

Or rather, it would be more accurate to say he was half right.

I gave a small shake of my head and corrected him.

“I don’t think the Gate transformation is complete yet.”

Wu Heixing swallowed hard and asked,

“How do you know that?”

“Just a feeling.”

“What?”

“If you don’t believe me, never mind.”

“…What kind of person says something like that?”

As I expected, Wu Heixing looked dumbfounded. Lee Jungryong, however, was different.

The emotion in his gaze as he looked at me was clearly a mixture of suspicion and surprise.

“How did you know?”

“You already knew?”

“I just realized it. It was a sensation I felt in North America a very long time ago, during the Great Cataclysm.”

“I see.”

“But it hasn’t happened even once since the Great Cataclysm. How did you know?”

“As I said, it’s just a feeling. I had a hunch.”

“You had a hunch…”

Lee Jungryong looked at me with an unreadable expression after my firm answer.

But that was all I could say. Even if I told him the truth, he would not be able to understand it anyway.

*It’s not as if I can show him the System window.*

I raised my head and glanced at the empty air. A System message had appeared before my eyes the instant we entered the city.

*Ding.*

> **System**
>
> You have entered a ???-Grade Gate, **City Consumed by Darkness**!
>
> You have infiltrated the stronghold of the **Arch Lich**!
>
> The city consumed by mana is already transforming into one enormous Gate. Defeat the Arch Lich, the source of everything, to stop the city’s transformation and prevent the catastrophe that will follow.
>
> Quest **One Who Returned from Death** has been created!
>
> You cannot use the **Login** function until the Quest ends!

*Gate transformation.*

It was something I had only read about in textbooks—a phenomenon from the distant past.

Lee Jungryong gazed beyond the thick fog and spoke.

“Gate transformations were rare even during the Great Cataclysm. For one to occur, an extremely powerful monster had to serve as its core and anchor its mana in the area.”

There was no need to consider which extremely powerful monster that might be.

I blurted out a single name.

“The Arch Lich.”

“Yes. It has to be him. He must be contaminating the city with mana and turning it into one enormous Gate. That must also be why he has not shown himself on the battlefield until now.”

The number of monsters that had revealed themselves on the battlefield so far was close to two hundred thousand.

That alone was an unprecedented catastrophe. But if the Gate transformation were to be completed…

*We’re finished.*

Humanity would undoubtedly emerge victorious in the end, but countless cities would be destroyed, and hundreds of thousands—no, perhaps millions—of people would die.

We had to stop it before it was too late.

“We don’t have much time. We need to hurry.”

Lee Jungryong nodded at my words.

“We should avoid the monsters as much as possible. We’ll need to conserve even the smallest amount of strength to face him. Mr. Wu, you as well.”

“…Yes.”

We began moving through the thick fog.

Unlike the small city where I had fought Lei Fei last time, this place—the Arch Lich’s stronghold—covered more than ten times the area and still bore traces of having once been a bustling city.

A forest of collapsed skyscrapers. A downtown district that must once have been the most dazzling part of the city, but was now desolate…

We moved as quickly and quietly as possible.

After traveling for some time with our senses stretched to their limits, Lee Jungryong, who had been leading the group, suddenly spoke.

“Did you know?”

“If you put it like that, of course I don’t. And this doesn’t seem like a particularly good time to play Twenty Questions.”

Lee Jungryong let out a low laugh at my immediate answer.

“These days, I find myself thinking about you more than usual.”

“Are you confessing your feelings to me? This is a bad time for that too.”

“In a sense, perhaps I am. How should I put it? I find myself thinking that you will surpass me someday.”

“You don’t have to worry about that. Even after ten years, I won’t be able to catch up to your heels, Vice Guild Master.”

“Haha. Do you really think so?”

“No. I just said it because I thought you’d like to hear it.”

“You’re as honest as ever. Just like when I first met you.”

“That first blind date was certainly a strange atmosphere.”

My memory was not particularly good, but I could still remember my first meeting with him vividly.

And it seemed Lee Jungryong felt the same way.

“We began as enemies bound by a bad fate. The more I think about it, the more regrettable it seems.”

“Tell me about it. If we had talked things out from the start instead of cutting someone’s arm off, we might have been able to begin on relatively friendly terms.”

“Park Jihoon, that boy, made a mistake in the heat of the moment. I apologize.”

“How could that have been the Disciple’s fault alone?”

“Heh. I see. Then it was also my fault for failing to teach him properly.”

I watched Lee Jungryong’s back as he moved ahead of us. He leaped between buildings with effortless movements, and I wondered what expression he was wearing now.

Lee Jungryong let out another quiet laugh and continued.

“You seem to have grown quite close to Minwoo.”

“We’re reasonably friendly.”

“You two seem to get along surprisingly well.”

“He pays me a lot.”

“A business relationship. That’s good to hear. Then do you think I could become close to you as well?”

I answered with a snort of laughter.

“Maybe seven years ago? I ate red bean bread as a snack at Hunter training camp. It tasted so good that I cried. But when I ate it after entering society, it wasn’t very good. I haven’t really eaten it since.”

“So now you’re full?”

“I’ve already earned enough for several generations to live without working. My stomach is already full, so what’s the point of forcing more down? I’ll just burst and die.”

“You’re wrong. Humans are always hungry creatures. No matter how much they stuff themselves, they never know satisfaction. Do you know why?”

“Hmm. Do you happen to suffer from binge-eating disorder?”

Lee Jungryong continued in a gentle voice.

“Greed. More money, more honor, or the opposite sex. We constantly desire and crave more.”

“Like you, Vice Guild Master?”

“That’s right. Like me.”

Lee Jungryong laughed aloud. His fairly loud laughter spread through the thick fog, but he did not seem concerned in the slightest.

“Laughter is supposed to bring good fortune, but in this case, don’t you think it might bring monsters instead?”

“There aren’t any monsters in this area. You know that too, don’t you?”

“Well, I’m just saying we should be a little more careful.”

*Whoooooosh!*

A foul-smelling wind brushed across my entire body.

From building to building. Leaping across gaps of more than twenty meters, we continued running.

We could not sense any monsters, and the buildings around us gradually grew fewer.

“Let’s slow down from here.”

“It’s dark. And narrow.”

“Bear with it for a little longer. More importantly, may I ask you one more thing?”

“Anything.”

“What did Minwoo say about this operation?”

“He didn’t say much…”

I looked at Lee Jungryong and Wu Heixing in turn before continuing slowly.

“He told me not to go.”

“More precisely?”

“Don’t go with people you can’t trust. Something like that.”

The smile around Lee Jungryong’s mouth deepened.

“Do you suspect me and that fellow too?”

“No.”

“Then?”

“If anything…”

I continued with a smile.

“If anything, I’m certain.”

“Certain?”

“Yes.”

I kept smiling as I went on.

“These fucking bastards are more interested in the back of my head than the Arch Lich. That’s what I’m certain of.”

Lee Jungryong’s footsteps stopped dead.
## Chapter artifact 417

# Chapter 417

It wasn’t that I didn’t know. I had only been waiting.

Waiting for the moment they sank their fangs into me.

“Rather… certainty.”

“Certainty?”

“Yes.”

The corners of my mouth rose before I could stop them. I threw out the one thing I had pressed down and held back time and time again.

“I’m certain these fucking bastards are more interested in stabbing me in the back than fighting the Arch Lich. Something like that.”

“……!”

“……!”

The moment the brief farce came to an end—

*Step.*

Lee Jungryong’s footsteps stopped.

*Fwish!*

The sound of displaced air rang out behind me. Three streaks of wind bored toward vital points across my body.

I did not need to turn around to see where the daggers Wu Heixing had thrown were headed.

And I knew what I had to do.

*Fwish-fwish-fwish!*

The three daggers aimed at my nape, spine, and right arm failed to reach their targets and pierced empty air.

*No. That’s not it.*

Maybe it was because I had raised my senses to their absolute limit.

Everything was slow and clear.

I reached out and caught the hilt of the dagger that had skimmed past my right arm. At the same time, I twisted my waist and whipped my arm forward like lightning.

*Shraaaaaaaaaash!*

“Hup!”

Wu Heixing, who had been charging toward me, hurriedly swung his sword.

*Boom!*

Along with a muffled, thunderous roar, his body was knocked backward. A low voice stopped Wu Heixing as he prepared to charge again, his face twisted in anger.

“Enough.”

“Mr. Lee. Why…!”

“He’s not someone you can handle. Wait here for a moment.”

Lee Jungryong restrained Wu Heixing and gazed at me with calm eyes.

“Your instincts are quite good.”

His tone had changed so completely that I let out a quiet laugh.

“An old man who knows everything is saying something obvious. If I didn’t have even this much sense, I’d have died a long time ago.”

“When did you know?”

I answered without hesitation.

“The moment we first met.”

The day I stormed into Myeongdong Guild alone. From that moment, Lee Jungryong and I had stood at an impassable point of opposition.

It had been decided the day that bastard Park Jihoon sent Black Hunters to cut off Uncle Kkeokjeong’s arms.

“If you’re going to say that was merely the result of your subordinates’ excessive loyalty, roll up that white-coated tongue and shove it back in your mouth.”

“Of course I wouldn’t. I merely find it regrettable.”

“What do you regret? The future where you’ll be smelling funeral incense behind a folding screen?”

Lee Jungryong shook his head.

“No. I had taken quite a liking to you.”

“Then you shouldn’t have cut off my man’s arms.”

“It was a light warning. I wanted to teach Choi Minwoo that boy a lesson. At the time, a fledgling named Jin Taekyung was not someone we needed to take seriously.”

“And now?”

Lee Jungryong answered with a gentle smile.

“I came here myself. Is that answer enough?”

“That’s more than enough.”

I leaned my back against a pile of collapsed concrete, holding White Flame at an angle.

Wu Heixing stood to my left. Lee Jungryong stood to my right. There were more than ten meters between us, but that was a distance any of us could erase in the blink of an eye.

“But this is unexpected. I thought you’d at least wait until after we killed the Arch Lich before making your move.”

“Pfft! You stupid peninsula bangzi!”

Wu Heixing cut in out of nowhere and snickered.

Only a few days ago, he had been unable to meet my eyes properly. Now he declared triumphantly,

“Fighting the Arch Lich is your job, Jin Taekyung.”

“What kind of bullshit… Ah.”

A certain thought flashed through my mind, and a hollow laugh escaped me.

I had wondered if that could really be the case, but they had actually gone that far.

Their brains were built completely differently from mine.

“Hah. Look at how neatly these fucking bastards thought this through. It’s beyond anything I imagined.”

“Do you understand now? Do you understand what kind of situation you’re in?”

“So… you never intended to fight the Arch Lich in the first place?”

Wu Heixing curled his lips and spoke.

“Why—why should I take that kind of risk?”

“……!”

“Today’s battle will go down as a defeat. And your name will be written at the very top of the list of the war dead. I’ve already decided on your epitaph.”

Wu Heixing spread his arms like a stage actor.

“Bangzi from Korea, killed by the Arch Lich. How about it? Isn’t that a fine epitaph?”

Even after Wu Heixing finished speaking, I could not find anything to say for a while. I stood there blankly, like a madman, and the goose bumps covering my body refused to fade.

Was it because of the scheme he had devised?

No.

One question Wu Heixing had thrown back at me continued to circle through my empty mind.

*Why should I take that kind of risk?*

It felt as though I had been struck in the back of the head.

At the same time, the countless deaths I had witnessed over the past month flashed before my eyes, along with the bodies that had been horribly mutilated.

Young parents who had met their end while holding their precious child tightly, hoping against hope that their little one might survive.

The old and infirm, unable to escape, who had been torn apart and eaten alive.

A pregnant woman who had died clutching her heavily swollen belly.

And…

*The day I became a Hunter, I swore that I would fight monsters until the moment my life ended. That oath still stands.*

Lei Fei, who had fulfilled his mission until the very last moment.

The five hundred Public Security Armed Forces Department Hunters who rose in defiance of death and charged valiantly.

Team Leader Choi and Shao Shen, who had bound their hands to their sword hilts with strips of cloth, prepared to kill one more monster despite knowing they were facing their final moments.

*You’re right. Why did all of them take such risks? Like fucking idiots.*

The face of each and every one of them flashed before my eyes.

My insides burned as though I had swallowed a fireball, and I exhaled a hot breath.

After taking a deep breath, I looked at one person.

“Tell me.”

“What should I tell you?”

“Whether you think the same way as that bastard.”

“I don’t. I’m very different from him. That fellow is afraid of the Arch Lich, but…”

Lee Jungryong continued in a gentle voice.

“I seized an opportunity. The longer this war lasts, the more I stand to gain.”

After a brief silence, I nodded faintly.

“I see.”

I pulled my back away from the concrete rubble. Scorching Yang Qi boiled like lava, surging through my four limbs, bones, and hundreds of acupoints. Blue flames danced along the spearhead of the White Flame in my hand.

“Let me ask you one thing, too.”

“Ask me anything.”

“‘The only good chink is a dead chink. Fucking Lee Jungryong.’ Those are the epitaphs I just came up with for you two. Do you like them?”

“……!”

“……Heh.”

Wu Heixing’s face crumpled, while the corners of Lee Jungryong’s eyes curved like crescent moons.

Then—

*Fwoooooosh!*

Blinding flashes burst from both sides.

* * *

Lee Jungryong had already made up his mind.

*I must not let my guard down. I’ll kill him by any means necessary.*

A lion gave its all even when hunting a rabbit.

All the more so when hunting a wolf named Jin Taekyung. To bring him down, a lion had to use every ounce of its strength.

No matter how much of a lion Lee Jungryong was, he could not afford to ignore the wolf’s fangs.

*Fwish!*

With a single step, Lee Jungryong closed the distance of more than ten meters in an instant, and his hand blurred.

A longsword had already left its scabbard, transforming into a dazzling flash as it shot forward.

Straight at one person—Jin Taekyung.

*Fwoooooosh!*

It was a full-power strike from Lee Jungryong, the likes of which he had not unleashed anywhere else in this war.

And Wu Heixing had joined the attack as well.

Compared to Jin Taekyung, Wu Heixing was a fledgling far behind him in ability, but he was still an S-rank Hunter who used an Aura Blade.

“Dieeeee!”

The instant Wu Heixing shouted with his eyes bloodshot, Lee Jungryong saw it clearly.

Jin Taekyung’s smooth movement, as fluid as sliding across ice.

The spearhead wrapped in blue flames.

*Boom!*

Two swords and one spear collided.

The tremendous wave of qi that erupted with a thunderous roar collapsed buildings and pulverized concrete.

*Rumble! Rumble-rumble-rumble!*

It looked as though a bombardment had taken place.

The ground caved in, and an immense tremor swept across a radius of several hundred meters.

But this was only the beginning of everything that followed.

*Fwish-fwish-fwish-fwish!*

Dozens, then hundreds of lines slashed through the air.

Lee Jungryong’s sword moved too quickly for the eye to follow, shredding Jin Taekyung.

Or rather, Lee Jungryong had been certain that was what would happen.

Until Jin Taekyung struck Wu Heixing in the chest with a palm engulfed in flames and sent him flying, then brought his spear down.

*Fwoosh—whoooooosh!*

Superheated flames blazed up, burning the air.

The spearhead devoured the thick fog that had consumed the entire city and the moisture brought by the weather, then slashed diagonally toward Lee Jungryong’s entire body with ferocious force.

It looked just like the claw of a dragon striking down from the heavens.

*What is this…?*

Lee Jungryong frowned.

Jin Taekyung’s spearhead was rushing toward him, erasing the Aura he had scattered.

The tremendous heat caught his breath and made his body lock up.

The young man before him, not even thirty years old, was no longer the person Lee Jungryong had known.

*How did he improve this much in such a short time…?*

But Lee Jungryong was not merely surprised by Jin Taekyung’s ability, which had far surpassed his expectations.

Lee Jungryong himself was a superhuman who exceeded even the other S-rank Hunters.

In a split second, he turned his blade sideways and blocked the spearhead.

*Kwaaaaaaaaaang!*

Jin Taekyung’s spear was faster and stronger than Lee Jungryong had expected.

But the same was true of Lee Jungryong.

*Swing—fwish-fwish-fwish-fwish!*

Within a moment divided into even smaller moments, spear and sword tangled and collided.

Flashes like lightning and thunderous roars rang out without pause.

*Clack-clack-clack!*

Jin Taekyung pressed down on Lee Jungryong’s sword with his spearhead, then reached out.

Just before the palm strike carrying the heat of the Flame Divine Palm could slam into Lee Jungryong’s chest, Lee Jungryong’s fist shot forward like lightning and met Jin Taekyung’s palm.

*Boom!*

With the sound of compressed air bursting apart, the two men stepped backward as though they had planned it.

And the result was astonishing to Lee Jungryong.

He had retreated two steps.

Jin Taekyung had retreated only one.

*Was I pushed back?*

Lee Jungryong had accumulated an enormous amount of qi over the course of many years.

And yet a fledgling barely in his late twenties had forced him backward.

It was impossible to believe that such a change had occurred in the short span of just over a month.

*That isn’t all.*

His incredible power and speed seemed to have no bottom. His movements, too—everything about him was astonishing. Beyond anything that could be put into words.

Just as he was now.

*Whoooooosh! Fwish!*

Lee Jungryong twisted his head aside.

The spearhead that had passed within half a span of his body changed direction in midair.

*Slash!*

A sensation like being burned, followed by droplets of blood scattering through the air.

Lee Jungryong felt the sensation of pain for the first time in a very long while and swung his sword.

*Boom!*

The weapons met as the two men faced each other.

Through the transparent spearhead, Lee Jungryong could see the young man’s burning eyes.

From between his lips, which had remained tightly sealed the entire time, came a low, flat voice.

“You’re fucked.”

Hearing Jin Taekyung’s chilling words, Lee Jungryong suddenly realized that he needed to correct the assessment he had made earlier.

*A lion.*

He had been wrong.

Jin Taekyung was not a wolf.

He was a lion—a powerful young male lion who might drive out the old lion that had ruled the pride for so long and become the new king.

*Craaaaaack! Boom!*

The old lion was sent flying by an irresistible force.

Lee Jungryong flipped his body in midair and landed on the ground.

The first thing he saw was the young male lion gripping Wu Heixing by the throat after Wu had attempted a surprise attack.

“Guhk! M-my father is with the Crown Prince Party…!”

“I don’t care.”

“If you let me live, I’ll repay you! Guh! Please!”

“Me? Let you live after you tried to kill me?”

A reddish gaze turned toward Wu Heixing.

Then a sentence Lee Jungryong had heard somewhere before slipped from Jin Taekyung’s lips.

“Why—why should I take that kind of risk?”

“……!”

*Crunch!*
## Chapter artifact 418

# Chapter 418

Sometimes, whenever I took someone's life, whenever I met the desperate voices and eyes of enemies begging for their lives, I found myself wondering.

*Why? Why on earth?*

Why didn't they stop to think about what they themselves had done? Why did they look to others for the causes of everything that happened?

*Too late.*

If you tried to kill someone, you had to consider the possibility of the opposite happening, too.

The seeds had already been sown, and at last, it was time to harvest.

I stared into Wu Heixing's bloodshot eyes and whispered,

“Why should I take that kind of risk?”

「……!」

I hadn't asked the question to hear an answer.

There was nothing more to hear or see. Without hesitation, I grabbed Wu Heixing by the neck and twisted.

*Crunch.*

Flesh was crushed and bones splintered beneath a grip strong enough to tear steel like paper.

The last light faded from his wide, frozen eyes.

As his struggling body went limp, a System notification rang out.

> **System**
>
> - Defeated **Lv. 135 Wu Heixing**!
> - Gained a substantial amount of **EXP**!
> - Gained no **Fame**. If it becomes known that you killed this person, significant repercussions are expected!

That was when Lee Jungryong, who had been standing more than twenty meters away, rose to his feet and spoke.

“You don't hesitate at all.”

I threw Wu Heixing's lifeless body aside and answered,

“He was someone who needed to die.”

“Do you know who that boy's father is?”

“I've heard of him. Apparently, he was one of the men who took a sledgehammer to Confucius's tomb decades ago.”[^1]

“And that young Red Guard grew up to become the most powerful man in Chinese politics and the leader of the Crown Prince Party. Even Chairman Shao Yang dares not touch him.”

“Damn, this continent is fucking amazing. In our country, it'd be like the arsonist who burned down Sungnyemun becoming President. Don't you think?”

“There is no need to try to understand it. But there is one fact you must know. You killed, with your own hands, the only son that the most powerful man among one billion people had after turning fifty.”

“I did? No, I didn't.”

I smiled shamelessly.

“Wu Heixing died after engaging in a fierce battle with the Arch Lich.”

“……!”

“I told you, I already decided on the epitaph. *The only good chink is a dead chink.* Of course, your gravestone will be right beside his.”

Lee Jungryong stared at me with an inscrutable expression, then let out a quiet laugh.

“You're a crafty one.”

“I liked the scenario you two came up with. Let me use it.”

“Do as you please. It won't go according to your wishes anyway.”

“Maybe…”

I continued, gesturing toward Wu Heixing's sprawled corpse with my chin.

“So far, it looks like things have gone more or less according to my wishes.”

“Yes. In that respect, you're like me.”

“What?”

As I frowned, Lee Jungryong gazed at me with a faint smile.

“Wu Heixing is easily swayed and loose-lipped. He's a terrible choice for plotting anything together, but even a man like that has his uses.”

“...What the fuck are you talking about?”

“In other words, this is what I mean.”

When Lee Jungryong pressed something in his hand, a beam pierced through the thick fog and struck a piece of concrete, projecting a hologram.

The short holographic video, barely ten seconds long, showed Wu Heixing begging for his life and me breaking his neck without a moment's hesitation.

“Huh.”

I let out a hollow laugh.

“That's some good image quality. The kind of video that would be perfect for giving people the wrong idea.”

“Exactly. Especially for an old father who has lost his late-born only son.”

“Are you planning to show them the unedited version?”

“Perhaps because of the mana's influence, an error will probably cause the beginning of the video to be lost.”

“What an incredible coincidence.”

“Anyone who sees this will have no choice but to be outraged. Not only those who enjoy slandering others, but even the people who worshipped you will turn away. The people you cherish so dearly will slowly crumble beneath the public's condemnation.”

The Peace Guild.

And Mom and Hayeon.

Those were the names and faces that flashed before my eyes the moment I heard Lee Jungryong's words.

I stepped forward, pressing my foot onto Wu Heixing's corpse.

*Step.*

“Did you plan this from the beginning?”

“Wu Heixing was merely a tool from the start. He could never become anything more.”

*Step.*

Lee Jungryong also began walking toward me.

But the qi flowing from his entire body was on an entirely different level from before.

That was why he had remained calm even after Wu Heixing's death.

The crafty beast had achieved its objective and finally drawn the claws it had kept hidden.

“Damn it. No wonder it seemed so easy.”

At my complaint, Lee Jungryong gave a dry laugh.

“I'll praise you for one thing. You far exceeded my expectations.”

“Let me ask one last time. Why are you going this far?”

“Could a brat like you possibly guess?”

*Step.*

“Were you really that afraid of Team Leader Choi—no, Choi Minwoo?”

“Can't you shut that mouth of yours?”

*Kuwaaaaaaaang!*

A massive wave of energy surged forth, driving back the fog and seizing control of the space.

The sharply honed killing intent made my skin prickle. Anger unlike anything I had ever seen rose in Lee Jungryong's formerly placid eyes.

“This is a position I earned entirely through my own strength. An empire of my own, built over the course of my entire life!”

It was anger he had kept pressed down, an emotion he was expressing for the first time in a very long while.

Lee Jungryong glared at me with eyes that seemed to pour fire and spat out each syllable as though chewing on it.

“No one can bring it down. Not you, not that boy Minwoo, and... not even my hyung!”

Hyung?

I wasn't given time to question that unexpected word.

*Step.*

One step left behind an unusually heavy, profound sound.

At the same time, Lee Jungryong's form rippled like water.

The beast that vanished, leaving behind an afterimage, had already arrived right in front of me.

*Fweeeeeeeeng!*

A mass of light filled my vision. I twisted my waist and swung White Flame.

The moment light and flame collided, a thunderous roar rang out as though the sky itself had split apart.

*Kwaaang!*

* * *

The explosion was enormous.

The high-rise building that had barely been holding together collapsed as if it had burst apart, while glass and concrete broke into countless tiny fragments that pierced through everything in every direction.

The aftershock of the clash was powerful enough to be felt dozens of kilometers away.

Amid the successive collapses and thunderous booms, I thrust out my foot.

*Fwish!*

Beyond the split dust cloud, a man standing tall in midair appeared.

His transparent eyes, which had always been impossible to read, were spewing flames.

“Jin Taekyung!”

Neither of us waited for the other.

I shattered the ground as I leaped upward, while he stepped on empty air and drove himself downward.

The trajectories of the sword and spear we swung at each other met with perfect accuracy, and an immense shock wave swept across our bodies.

We were hurled backward at the same time, as though we had planned it. Then we kicked off the structures of the already-ruined city and shot toward each other again.

*Shweeeeeek—Kwang!*

With a thunderous boom, Lee Jungryong's sword swept my spearhead aside and thrust straight toward my throat.

*Boom!*

I twisted my head aside, and severed strands of hair scattered through the air with a sharp whistle.

But it wasn't over.

*Shwish-shwish-shwish!*

Lee Jungryong's sword shot forward as a streak of pure white light.

A net of Force flowed along the blade.

Faced with a spectacle of light filling my vision, I awakened all the internal energy sleeping in my dantian.

Three jiazi of Scorching Yang Qi rose like a wildfire and seeped into my four limbs and hundreds of bones. Blue hellfire surged along the transparent spearhead, rippling smoothly like a dragon's tail.

*Fire Dragon's Single Tail.*

*Whoooooosh!*

A single swing.

Part of the Force rushing toward me vanished beneath the fire dragon's tail, which spread outward like the ribs of a fan.

Now it was time to tear apart the loosened net with sharp claws.

*Heavenly Strike.*

The Fire Dragon Divine Spear consisted of only two forms.

And yet the former Sect Leader of the Fire Gate Clan who created it earned the epithet of the greatest spearman under heaven, leaving behind a brief final testament about his martial arts.

*“A martial art I devoted my entire life to but failed to complete. Even so, it is a spear art worthy of being called the greatest under heaven.”*

His words had been true.

That was what the Fire Dragon Divine Spear was. A spear art that could proudly call itself the greatest under heaven after only two forms, and...

*Kuwaaaaaang!*

Heavenly Strike, unleashed with all my power, tore through the net of Force and swept across everything ahead of it.

Lee Jungryong, watching the flames rush toward him in an instant before he had any chance to react, brought his sword down with a powerful shout.

“Ha!”

*Fwish!*

The flames split at the tip of his sword.

His form shot forward like an arrow along the paths of flame that opened to either side, unleashing countless sword strikes.

*Shu-shu-shu-shu-shuk!*

Chest, throat, shoulder, arms, legs...

Within a span of time so short it could be called an instant—

As I faced the sword's trajectories, swinging and cutting like rays of light, I was suddenly seized by wonder.

*How? How can this be possible?*

I was a Hunter. At the same time, I was a martial artist.

No. Perhaps I was a being better suited to the name *Player*.

On a sweltering summer day, I had picked up a discarded VR capsule at a recycling station and gained a new power called the System. I had become the only being who stood astride both the modern world and the Murim.

But still...

*Boom!*

Movements without a single wasted inch, nearly perfect control of power, and even control over qi.

After parrying Lee Jungryong's attack, I was inwardly amazed. It had nothing to do with what kind of person Lee Jungryong was. I was simply stunned by the skill he possessed.

*So he was this strong.*

After reaching the Supreme Peak realm, I had thought there would not be many people in the modern world capable of matching me.

After coming to Sichuan and meeting several S-rank Hunters, that belief had only grown stronger.

No matter how much energy each of them possessed, martial arts did not exist here.

The so-called Hunters could fight efficiently, but when it came to efficient qi manipulation, they were practically illiterate.

Lee Jungryong? I knew he had learned a cultivation technique called a mana cultivation technique in the modern world, but I had assumed it wouldn't be much different.

And now I realized it.

My arrogance had led me to the wrong conclusion.

*Shlack!*

My thigh suddenly felt cool, followed by a pain as hot as fire.

But why did my mind clear and my vision sharpen as though I had just awakened from a long sleep?

*Shlack, shlack, shlack!*

My arm, calf, and the back of my neck.

Blood spurted out, and the qi carried through his Force disrupted the flow of my internal energy.

I looked at Lee Jungryong's face as he continued raining sword strikes down upon me while I staggered.

His forehead glistened with sweat. At the same time, his eyes seemed certain of victory, and a smile hung at the corners of his mouth.

*Ah, I don't like this.*

I didn't like that smile. I didn't like the fact that a man like him possessed this level of strength.

Feeling something surge up inside me, I swung White Flame.

*Kwaang!*

The first clash.

Blood flowed from the cuts inflicted earlier, and pain spread through me. But without a word, I thrust the spear forward again.

Lee Jungryong, who had stepped back, charged into me with a calm smile.

*Boom!*

The second clash.

Lee Jungryong stepped back twice and looked at me with an expression of surprise.

*Did he still have that much strength left?*

His thoughts were written plainly across his face.

*Of course I do.*

I muttered inwardly, adjusted my grip on the spear, ignored the faint pain spreading through me, and stepped forward.

*Boom! Boom! Kwaang!*

Three times. Four times. Five times.

Each time spear and sword collided and thunderous roars burst forth, Lee Jungryong's expression grew harder.

The smile that had lingered around his mouth had disappeared long ago.

“You bastard...!”

Hearing that growling shout instead of the voice that was usually as soft as a cat's paw somehow made me laugh.

Intoxicated by my own strength, I had underestimated his abilities and made a foolish mistake.

But Lee Jungryong had done the same.

The claws he had revealed were certainly strong and sharp, but they weren't enough to finish me off.

“Jungryong.”

I drew in a deep breath, and stale air and a foul stench flooded my lungs.

Even so, I felt refreshed, as though something inside me had been blown wide open.

Yes. Now I understood.

“Let's clip those claws.”

Lee Jungryong would die here today.

[^1]: The reference is to the Red Guards' attack on Confucius's tomb during the Cultural Revolution.
## Chapter artifact 419

# Chapter 419

Lee Jungryong suddenly wondered.

*Where had things gone wrong? And what had gone wrong?*

Driving out his hyung’s bloodline and seizing control of Ares Guild?

Committing all manner of crimes to make the Guild grow without pause, then continuing to feed his greed without ever learning satisfaction?

Or perhaps…

*That I became enemies with him?*

Lee Jungryong’s gaze settled on one person—a young man whose body was stained with blood from the bleeding wounds covering him.

After looking up at the sky and taking a deep breath, the young man parted his lips.

“Jungryong.”

Why was it? The moment Lee Jungryong heard that quiet voice, a chill ran down his spine. Though he had not suffered a single wound, he felt as if he had been cut by a blade.

Looking at him, Jin Taekyung formed a feral smile.

“Let’s clip those claws.”

“……!”

*Fwish!*

The wind blew, and in the instant the space between them vanished, Lee Jungryong swung his sword with a sharp whistle.

*Shwick!*

A dazzling concentration of qi sliced through Jin Taekyung’s body. But instead of blood, wind scattered through the air.

An afterimage. Not the real thing.

A red alarm bell rang in Lee Jungryong’s mind.

*Behind me!*

It was too late to swing his sword. Lee Jungryong spun around like lightning and drove out his fist.

A fist wrapped in pure-white Force collided with a palm carrying blue flame.

*Kwaang!*

The world shook.

No—the thing shaking was Lee Jungryong’s vision.

Flung backward by an irresistible force, he twisted his body in midair and righted himself.

His fist throbbed, and something surged up from inside him. But he was not even given time to spit out the blood.

*Shweeeeeek!*

A spearhead had already rushed up to his face.

The spear Jin Taekyung had hurled was aimed at Lee Jungryong’s chest. Gritting his teeth, Lee Jungryong poured all his strength into knocking the spear upward with his sword.

*Kagagagagak! Kwaang!*

The spear narrowly missed and smashed through the concrete, leaving behind a massive crater.

Lee Jungryong succeeded in deflecting it, but the spear’s terrifying power and spin tore his hand open, sending blood spraying into the air.

He paid it no mind and thrust his foot through the thick cloud of dust.

*Boom!*

The dust and fog, unable to withstand his blinding speed, scattered in every direction.

At the end of Lee Jungryong’s step stood a single person.

“Reckless, aren’t you? My kind of guy.”

Jin Taekyung was already holding a new spear. He slashed the spearhead down in every direction. Space split apart, and flames surged upward.

The tip of Lee Jungryong’s sword pierced straight through the center.

*Whoom! Boom!*

Compressed air burst outward. The flames parted, opening a new path.

Lee Jungryong’s body shot forward like an arrow along it, charging toward Jin Taekyung.

*Die.*

The sword held a single thought. It shone brilliantly and moved as fast as light.

Yet Jin Taekyung’s eyes, seen within the slowed-down world, were clearly smiling.

*This is…*

Something was wrong.

Before Lee Jungryong could finish the thought, Jin Taekyung’s hand gripping the spear blurred.

At the same time, a tremendous force struck the sword blade that had seemed ready to pierce Jin Taekyung’s throat.

*Shick! Kwaang!*

A thunderous boom rang out, loud enough to leave his ears ringing.

Lee Jungryong slid more than ten meters against his will and swallowed the blood rising in his throat.

*It isn’t over yet.*

He could not fall. He could not show weakness.

He was Lee Jungryong—the one who had made his way through the vortex of the Great Cataclysm, the most violent upheaval in human history, and a ruthless hero born of his age.

Lee Jungryong gripped his sword, now webbed with fine cracks.

*I won’t die. I can’t die.*

There had been countless twists and turns on the road that had brought him here. He had endured distant despair and days of unbearable rage.

He had spent half his life in someone else’s shadow, branded as number two.

No. Perhaps even now…

But—

“Not anymore.”

*Crack. Crack-crack-crack.*

The veins across his body stood out, and his muscles swelled.

Powerful qi erupted from Lee Jungryong’s entire body, pressing down on everything around him.

He dragged up every last scrap of strength he had saved for the very end and glared at Jin Taekyung with bloodshot eyes.

“He’s practically a man who no longer exists. The greatest in the world is… me.”

*Vrrrrrrm.*

Everything surrounding Lee Jungryong trembled.

Jin Taekyung watched him with calm eyes that held not the slightest hint of wavering.

“I don’t think so.”

*Kuwaaaaaang!*

The waves of energy flowing from both men clawed at everything around them.

In a fleeting instant split into countless fragments, they charged toward each other at the same time.

* * *

*Kwaang!*

Their collision was like a flash of light, and the aftermath was enormous.

Amid thunderous booms that shook the world, they became two streams of wind twisting together.

A spearhead wrapped in blue flame and a sword enveloped in dazzling light flew toward each other.

*Shwish-shwish-shwish-shwish!*

Masses of light tore through space as they charged.

Jin Taekyung kicked off the ground and rose into the air, driving his spear down with tremendous force.

One strike. Two strikes. Three.

Every time spear and sword collided, thunderous booms erupted along with immense shock waves.

Before long, blood spilling from the corner of Lee Jungryong’s mouth scattered in droplets.

“Cough.”

His body staggered for an instant.

At the brief glimpse of weakness shown by the old lion, the young male lion bared his teeth.

The spearhead swept horizontally, slashing fiercely toward Lee Jungryong’s side.

*Kwaang!*

The ground shook as though an earthquake had struck.

The two men were so close that their breaths nearly touched. Lee Jungryong barely blocked the spear, and through the weapons pressed against each other, his eyes met Jin Taekyung’s—a pair of eyes pouring flame.

*He’s young. Just as I was in the past.*

Why?

Why had such a thought suddenly come to him at a time like this?

Was it because he was remembering his own old, pathetic self that he failed to block Jin Taekyung’s palm as it came flying through the flames?

*Boom!*

It was hot.

The qi that had been protecting his entire body without a gap shattered, and terrible heat seeped deep into his lungs.

Amid the blue flames filling his vision and the pain, old memories flashed through Lee Jungryong’s mind like arrows.

“Your name?”

“Pardon?”

“Ah, yes. I meant you.”

“What’s this sudden exchange of names?”

“Just because. You looked about my age, and it was nice to see someone my age.”

“Young fellow, suddenly dropping the honorifics, are we? You look much younger than me.”

“Then should we be friends? I don’t mind.”

“……Do you really have time to say things like that in a situation like this?”

“Maybe not.”

A man he had met during the early days of the Great Cataclysm, when they were surrounded by countless monsters in a desperate, life-or-death situation.

Lee Jungryong had thought he was half-mad with fear of death.

At least, he had thought so until that madman suddenly stepped forward and swept away more than a thousand monsters.

*Crack-crack-crack!*

“What the hell…”

“Now! Charge!”

After the battle ended, the man came back and asked him the same question as before.

“Your name?”

“Lee Jungryong… sir.”

“Cool name. How old are you? Oh, I’m five years older. That’s not much of a difference. Should we just be friends?”

“No. Hyung.”

He looked absurdly young and was unbelievably strong.

At their first meeting, A-rank Hunter Lee Jungryong discovered his hero—and, at the same time, an immense mountain range he could never cross.

“By the way, hyung.”

“Yeah?”

“What’s your name…?”

“Oh, I haven’t told you yet.”

The man had grinned and said,

“Cheon Taemin.”

Cheon Taemin. Cheon Taemin. Cheon Taemin…

No matter how many times he repeated the name, it left behind a deep resonance.

Even when he tried to forget it, the face remained etched in his mind.

A giant who cast a massive shadow over Lee Jungryong’s life.

“Get lost! I said get out of my sight right now—!”

Lee Jungryong cried out in a boiling voice.

The vision that had been bleached white with pain shattered like glass, and the wind rushing past his ears was fierce.

When he came to his senses, Lee Jungryong was crashing through a high-rise building and slamming into cold concrete with tremendous force.

*Kwa-gwa-gwang!*

“Cough.”

Dark-red blood spurted between his lips.

His vision was blurred, and pain surged through every part of his body.

Perhaps his shattered ribs had pressed against his organs, because breathing was difficult. His broken left arm and leg dangled uselessly.

*A potion. The potion…*

This was his last chance.

While the attack had stopped, even if only briefly, he needed to heal his wounds.

Lee Jungryong groped at his side with his relatively uninjured right arm, but the place where his dimensional pouch should have been was empty.

Instead, he saw someone approaching him from far away.

“Ah, are you looking for this?”

*Rrrrrroll. Clink.*

A magic-enhanced glass bottle rolled over and came to rest by Lee Jungryong’s feet.

It was a top-tier potion, a miraculous medicine said to save anyone as long as they still had breath in their body.

There was, however, a considerable difference between it and the state Lee Jungryong remembered.

“I was so thirsty that I drank it. Man, it was refreshing. Did you just come back from a mineral spring?”

As Jin Taekyung approached and spoke as casually as ever, Lee Jungryong let out a hollow laugh.

*Jin Taekyung.*

His name, face, and personality were all different.

But at that moment, Lee Jungryong finally understood.

The familiar feeling he had deliberately ignored when he first encountered Jin Taekyung, covering it with the two words *anxiety* and *interest*.

“Jungryong.”

The quiet voice pierced his ears.

Jin Taekyung’s face had drawn close, and superimposed over it was the image of another person.

Lee Jungryong muttered like a groan.

“Who are you? Who the hell are you?”

He wanted to ask. He was desperate to know.

How could Jin Taekyung resemble him so much?

Why could some F-rank Hunter like that grow stronger, rather than Lee Jungryong—the man who had followed in Cheon Taemin’s footsteps, achieved countless feats, and been hailed as a hero?

“Me?”

The next moment, Jin Taekyung smiled and continued,

“Jungryong’s personal bully.”

Then, like an echo rebounding from far away, the face and voice of someone from the depths of Lee Jungryong’s stale memories overlapped with his.

“Brothers. Sworn brothers.”

The two men, speaking different words with different meanings, were both smiling.

Lee Jungryong stared blankly at those goddamn similar smiles, then slowly—very slowly—opened his mouth.

“I…”

Decades of his life and countless emotions rose and faded.

After a wait that lasted no more than an instant yet felt like eternity, a hollow voice forced its way between his lips.

“I don’t regret it. Never.”

If someone asked whether he had not even a handful of regrets, the answer was no.

But Lee Jungryong could not regret it. He did not want to regret it.

He simply believed this was the ending most suited to him.

“Kill me.”

A cold sentence fell toward Lee Jungryong, who was smiling brightly.

“Your last words. I heard them.”

*Fwoom.*

The words were cold. The spearhead that followed them burned with blue flame.

* * *

The flames, carrying heat hot enough to melt anything, roared to life in an instant. After burning everything, they finally died away.

All that remained in the melted concrete and blackened ruins was a trace that someone had once been there.

And the sound of a bell that only one person in the world could hear.

*Ding.*

> **System**
>
> - Defeated **Lv. 153 Lee Jungryong**!
> - Gained a massive amount of **EXP**!
> - Level up!
> - Level up!

Listening to the cheerful System notification, I slowly lowered my spear.

*Damn old man.*

That final smile kept coming back to me.

What kind of life had Lee Jungryong lived? What had he been thinking at the end? And then there were the movements he had shown and his strange behavior…

*No. I’ll think about it later.*

The fight with Lee Jungryong had not been easy for me, either.

A wave of mental exhaustion suddenly washed over me, but ironically, my body felt lighter than ever after receiving the effects of a top-tier potion and leveling up.

And more than anything, I had a reason to keep moving forward.

*The Arch Lich.*

The source of all this.

Before that bastard transformed the enormous city into a Gate, I had to kill—

“H-human.”

The Skeleton Warlord’s trembling voice reached me.

I raised my head, a sensation like every hair on my body standing on end washing over me.

There he was.

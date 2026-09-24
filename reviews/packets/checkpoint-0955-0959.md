# Checkpoint Review — 955–959

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

# Chapters 955–959

## Plot

After seven days and nights of nonstop travel, Taekyung rests with the Bow Saint and Jeok Cheongang. The Bow Saint urges him to trust the people he is trying to save and to share the burden. Taekyung accepts this and prepares to continue toward Taiyuan, still about two days away.

At Eight Spring Gorge, Jin Mukyung’s sword and the defenders’ armor—made from the Water God Dragon’s remains—help blunt the steppe assault. Arrows, rocks, and the defenders’ attacks kill hundreds, but the Chinggen impostor breaks through the cliff defenses. The Dongting Fisherman confronts him, fighting out of gratitude to the Jin Family and a desire for revenge on Dark Heaven; the fisherman is later killed.

Jamukha orders the Keshik to continue the assault and has a retreating chieftain and his followers slaughtered. Temur recognizes that his choice to survive has helped bring his people to ruin. Three of Jamukha’s commanders of a hundred die, and Jamukha orders the remaining Keshik to wear down the defenders while sparing his personal guard further losses.

The impostor reveals that the real Chinggen is dead and that Temur was spared to help control the western tribes. He offers to make Mukyung his disciple. After the impostor tells Jin Wikyung that the Dongting Fisherman has died, Wikyung accepts that the Jin Family owes a debt to the fisherman and the other fallen. The impostor reveals his true identity as the elderly Demon Bird and repels an attack by Mukyung, Wikyung, Wipeng, and Cheol Mubaek. He calls himself Mukyung’s master, expels him for the ambush, and faces the defenders as the battle resumes.

## Continuity

- The battle at Eight Spring Gorge has resumed. Jin Mukyung, Jin Wikyung, Wipeng, and Cheol Mubaek face the Demon Bird; the outcome is unresolved.
- The real Chinggen is dead. The impostor who wore his face is the Demon Bird, an elderly and overwhelmingly powerful martial artist. He killed the trapped nomads and left Temur alive to help control the western tribes.
- The Dongting Fisherman died fighting the impostor. Jin Wikyung considers the Jin Family indebted to him and the other fallen.
- Jamukha ordered the Keshik to wear down the defenders while limiting losses to his personal guard. Three of his commanders of a hundred have died.
- Temur chose survival over loyalty and feels guilty that his actions led his followers into danger. Jamukha has threatened him into obedience.
- Taekyung is resting with the Bow Saint and Jeok Cheongang en route to Taiyuan, still about two days away. He has resolved to trust his allies rather than bear every burden alone.
- The Emperor remains gravely ill with Blood Soul Gu; saving him requires him to die once, and Taekyung’s treatment remains unresolved. Jang Sam remains unconscious after his sudden rise in level and attack on Taekyung; the improved Temporary Strength Pill’s source, effects, and distribution remain unknown.
- The Martial God’s identity and connection to the chosen one and the Bow Saint remain unknown. The Eastern Heaven Demon Lord’s papers and silk pouch remain unexplained.

## Translation Decisions

- Keep “Sword Demon” for 검귀 and “life-and-death duel” for 생사결.
- Render 마조 as “Demon Bird,” the title the impostor gives as his name.
- Render the impostor wearing Chinggen’s face as Chinggen when the scene uses his name, without implying the real Chinggen has returned.

## Durable state

{
  "active_continuity": [
    "The battle at Eight Spring Gorge has resumed; Jin Mukyung, Jin Wikyung, Wipeng, and Cheol Mubaek face the Demon Bird.",
    "The real Chinggen is dead; the impostor who wore his face is the Demon Bird, an elderly and overwhelmingly powerful martial artist who left Temur alive to control the western tribes.",
    "The Dongting Fisherman died fighting the impostor. Jin Wikyung considers the Jin Family indebted to him and the other fallen.",
    "Jamukha ordered the Keshik at the gorge to wear down the defenders while limiting losses to his personal guard; three of his commanders of a hundred have died.",
    "Temur chose survival over loyalty and feels guilty that his actions led his followers to slaughter; Jamukha threatened him into obedience.",
    "The Emperor remains gravely ill with Blood Soul Gu; saving him requires him to die once, and Taekyung’s treatment remains unresolved.",
    "Jang Sam remains unconscious after his sudden rise in level and attack on Taekyung; the improved Temporary Strength Pill’s source, effects, and distribution remain unknown.",
    "The Martial God’s identity and connection to the chosen one and the Bow Saint remain unknown.",
    "The Eastern Heaven Demon Lord’s papers and silk pouch remain unexplained.",
    "Taekyung resolved to trust his allies rather than bear every burden alone."
  ],
  "continuity_sources": [
    958,
    959
  ],
  "open_questions": [
    "How will the battle at Eight Spring Gorge end, and can the defenders defeat the Demon Bird?",
    "Who gave Jang Sam the silk pouch, and what are the improved pill’s effects and distribution?",
    "What is the Martial God’s identity and connection to the chosen one and the Bow Saint?",
    "What do the Eastern Heaven Demon Lord’s papers and silk pouch contain?",
    "What will become of Temur and the followers he led into battle?"
  ],
  "safe_through": 959,
  "temporary_decisions": [
    "Taekyung intends to keep the pocket watch for half a month before deciding whether to give it to Mujin."
  ],
  "version": 1
}

## Reading copies

## Chapter artifact 955

# Chapter 955

Tap.

At the sudden touch of something cold, I abruptly opened my eyes.

My body moved on instinct, too.

*Whoosh!*

A punch cut through the air.

As my vision snapped back into focus, the Bow Saint—watching me from the tree across from us—spoke with a calm expression.

“Looks like you had a nightmare.”

“Ah.”

Only then did I realize it.

I’d been in such a deep sleep that I hadn’t even known when I’d fallen asleep.

And, just as the Bow Saint had said, everything I’d seen and experienced in it had been the worst of the worst.

“How long was I asleep?”

I asked as I tried to steady my ragged breathing. The Bow Saint dropped lightly from the branch and answered.

“Let’s see. About two hours.”

“Two hours…”

“You should sleep some more. At least until daybreak.”

It was the dim light of early morning.

Above us, the morning dew that had woken me was slowly rolling down a leaf, and now and then the only sound in the deserted mountain woods was the chirping of insects.

“W-wait, no. Master—where is he?”

“Hunting. We’ve been eating nothing but jerky and drinking nothing but water for more than seven days. He ought to do at least that much. And…”

The Bow Saint tossed a dry twig onto the dying campfire and continued.

“You don’t need to worry about what to call him. I’ve already figured out the general situation. For men as rough-looking as you two, you’ve been surprisingly sentimental.”

“How did you—”

“If you have the energy to ask me about every little thing, come over here and warm yourself.”

I hesitated a moment, then stood and started walking.

Not toward the campfire, but toward somewhere in the still-dark woods.

“Where are you going?”

“I’ll go on ahead, slowly. Once Old Master comes back, we can go together…”

“You really are a stubborn brat.”

The Bow Saint clicked her tongue and reached out.

*Fwish!*

A blast of Finger Qi shot toward me with the sound of tearing wind, grazing the back of my neck. That chilling whistle made every trace of sleepiness vanish in an instant.

“…What are you doing?”

“For a disobedient child, a beating is the best medicine. While I’m still asking nicely, sit by the fire. Or lie down and go back to sleep.”

I’d forgotten.

That woman, who looked like she was barely in her thirties, was still a Murim martial artist who favored force over words.

And the Three Saints were, among other things, a top-tier corporation—no, a nationwide gang.

I stared at the Bow Saint in silence, then spoke.

“We have to go.”

“Of course we do.”

“I mean right now.”

“I’m talking about a little later.”

“So this is how you’re going to play it?”

“If I do, what are you going to do about it?”

The Bow Saint answered calmly, prodding the fire as she went on.

“There was a time when I was like that, too. I struggled with everything I had to save even one person. I risked my life to shave off moments—short as they were.”

“Not anymore?”

“Who knows.”

Her answer sounded hollow.

She gazed at the fire as it began to stir back to life, lost in thought as if recalling old memories. Then she spoke.

“I’ve only come to understand one small thing.”

“One small thing?”

“That my impatience was only driving me further into danger.”

“…”

“I gave every moment my best, but the results still fell short. There wasn’t even time to sit back and enjoy a meal or a cup of tea. I had to kill people and watch others die. Even after I discovered the inner demon that had taken root deep in my heart, that didn’t change.”

The Bow Saint’s eyes, fixed on the fire, glowed red.

Like the flames of war she must have witnessed countless times long ago.

“I don’t like the word ‘fate.’ If everything is going to happen as it’s already been decided, no matter how hard we struggle, then even the meaning of that struggle fades away. But…”

*Crack. Fwoosh.*

The flames, which had been gradually coming back to life, suddenly leapt higher.

Beyond the faintly drifting embers, the Bow Saint looked at me with a gaze sunk deep in thought.

“If something can’t be stopped even by someone who’s run without rest for seven whole days and nights… Then yes. That, surely, is fate.”

I gritted my teeth.

And felt my body, drenched in exhaustion like a waterlogged cotton rag.

I knew it myself.

The Bow Saint was right.

To me, fate had the most goddamn meaning of any word in the world. And yet there were times when I had no choice but to admit it existed.

Because I was only human.

Not an all-knowing, all-powerful god.

“I had a dream. A nightmare.”

A cracked voice, strange as if it belonged to someone else, slipped between my lips.

The reason my back had been damp since I first woke wasn’t the morning dew. It was cold sweat.

“When I finally got there… everyone was dead. Every last one of them. Not a single exception.”

“Is that so?”

My voice trembled. The Bow Saint remained calm.

“You must have been terribly sad.”

I shook my head.

It wasn’t sadness. It was despair.

Despair that felt like it had punched through the earth and plunged deep into the ground below.

Even now, after waking from the dream, the sight of them, all horribly dead, still seemed to hover before my eyes.

“That’s why I have to go. Before it’s too late. As soon as possible.”

At first, I’d thought this was just a game.

I’d figured it was nothing more than data created by bespectacled developers in black turtlenecks or plaid shirts.

But before long, I’d realized the truth.

This was another world, and the people here were individuals, each with their own feelings and will.

So I’d opened my heart.

To the Lesser Family Head of the Jin Family of Taiyuan, who firmly believed I was his own flesh and blood. To the young gate guard who’d picked a fight with me at our very first meeting, looking at me like he couldn’t stand the sight of me.

And even to that deranged old man who’d wandered the world searching for the Disciple who remained his last regret and lingering attachment.

The sincerity they’d shown me had settled in my heart—and before I knew it, it had overflowed.

Another friend and comrade. A Master and family.

When I closed my eyes, the faces and names of everyone I’d met came to me in the darkness.

That was why I had to run, even if it meant wringing every last bit of strength from this tired, impatient body.

*Just as I had over the past seven days and nights.*

I’d given it everything I had.

I’d crossed rugged mountains that even seasoned hunters avoided. I’d thought even waiting for a boat was a waste of time, so I’d burned through a tremendous amount of internal energy to cross the river using Rising on Duckweed, Crossing Water.

That was how I’d made it here. To this place.

*Now, Taiyuan is only about two days away.*

Maybe I’d already passed the imperial messengers—or the messenger eagles.

I’d abandoned even the fine horse the Son of Heaven had given me. I’d sought the fastest route and run without rest, day or night.

But those two short days were also enough time for the nightmare I’d had today to become reality.

*I can’t let that happen.*

*Clench.*

I curled my hand into a tight fist. My nails dug into my flesh, and I felt hot blood well up.

The Bow Saint had been watching me in silence. Just then, she spoke.

“Strange, isn’t it?”

“What do you mean…?”

“You treasure them beyond measure, and yet at the same time, you don’t trust them at all.”

“…”

“Sometimes, just trust them. They aren’t as weak as you think, and they aren’t so easily uprooted.”

My whole body stiffened. For a moment I was at a loss for words, and then the Bow Saint’s voice continued in my ear.

“Of course, you can do a great deal. You could shatter a boulder weighing ten thousand *geun* with one hand, and split a river with the other. But what if it were a mountain instead of a boulder? An ocean instead of a river? Would you just quietly bear it alone, like Yu Gong long ago?”

Yu Gong.

The story of an old man, considered foolish, who tried to tear down a great mountain by digging up earth and hauling away rocks.

In the end, the Jade Emperor had been moved by his devotion and helped him achieve his goal. But it hadn’t been done by Yu Gong’s own effort and strength alone.

“What if the countless people who heard Yu Gong’s story hadn’t laughed at him for being a fool, but had joined forces to help him?”

I didn’t answer, but I thought to myself:

With their help, the old man would have accomplished his goal in the end.

Not through the Jade Emperor, but through the people who believed in him and followed him.

Through all of them.

*Ah.*

Something stirred in a corner of my heart. I looked down at my hands, which were smudged with dirt here and there.

Just as the Bow Saint had said, I had tremendous power.

I could crush a huge boulder with a single punch, or split a small river for a short while with one palm.

But that still wasn’t nearly enough to move a mountain or an ocean.

The same was true of the disaster looming over Shanxi Province.

To sweep away the dark clouds filling the sky, I’d need everyone’s help.

“Let me ask you something.”

Her gaze was calm, but for some reason it felt warm.

The Bow Saint looked at me and spoke slowly, like a grandmother gently chiding her petulant young grandson.

“What do you believe in—the heavens, or people?”

Instead of answering, I looked toward the east, where the light was slowly spreading.

Then, quite suddenly, I spoke.

“Do you happen to know what the Jade Emperor looks like?”

“What?”

“I have a bit of a suspicion problem. I can’t really believe in something unless I see it with my own eyes.”

“…”

The Bow Saint blinked at my unexpected answer. Then she realized what I meant and gave a quiet laugh.

“If the Daoists heard you, they’d be horrified.”

“It’s all right. The person behind me may not be the Jade Emperor, but he’s at least Yama.”

*Shff.*

Footsteps, deliberately loud.

I turned my head and saw the King of the Underworld—no, Jeok Cheongang—standing there with a frown.

*Thump.*

Jeok Cheongang set down a large deer, who knew where he’d caught it, and spoke.

“You cheeky brat. I leave for a moment, and what’s this about Yama?”

His tone was gruff, and his brow was deeply furrowed.

But the corner of his mouth was twitching even now—a sure sign that he was trying to hide a smile.

He’d obviously heard the conversation between the Bow Saint and me. Still, he pretended nothing had happened and asked me as if it were all quite ordinary.

“Enough. Spare me the excuses. What do you say? Feel like tearing into some meat for a change?”

Meat, when every second mattered.

I glanced toward the overgrown woods to the north, then answered with a faint smile.

“Sounds good.”

I wasn’t Yu Gong. I was Jin Taekyung.

And so, now, I believed.

In all of them.

*Don’t die. Not a single one of you.*

I repeated the words silently, though they couldn’t hear me, and sat down in front of the campfire.

A proper rest, at last, after seven days and nights.

I had to save my strength as best I could for the two days or so still ahead.
## Chapter artifact 956

# Chapter 956

Eight Spring Gorge was a little over a hundred *jang* long.

A natural gateway surrounded by towering cliffs some thirty *jang* high.

Its narrow width—barely enough for thirty grown men to stand shoulder to shoulder—made it the worst possible place to attack. But there was a reason two great battles with Shanxi Province’s fate at stake had been fought in this jar-shaped gorge.

“Break through! Trample them and keep going!”

“Brothers of the Great Steppe! Once we cross this godforsaken gorge, Shanxi Province will be ours!”

Eight Spring Gorge was the greatest strategic stronghold in the Shanxi region.

It was the quickest route through the rugged mountains covering the north, and the last passage leading to the central plains.

If they took this place, positioned on the border between north and central Shanxi, nothing would remain to stop tens of thousands of cavalry charging side by side, shaking the earth beneath their hooves.

And even if something did stand in their way, they could simply trample it.

A wave could never be held back by a handful of sand and gravel.

That was precisely why the defenders had to stop the invaders before them, by any means necessary.

“Hold the line! Don’t give up a single step!”

“Proud people of Shanxi! Defend your homeland from these merciless barbarians!”

“Raaaaaah!”

Screams of defiance pierced the darkness and echoed through the gorge.

And amid the dense rain of arrows both armies loosed at each other, one streak of light moved with graceful ease, seemingly apart from everything else.

*Shing!*

Space split apart.

The dozen or so mounted warriors charging with the steppe nomads’ distinctive cries suddenly felt the wind.

Not just a wind brushing past their bodies, but a cold gust sweeping through them to their very cores.

“…Huh?”

Their eyes widened. Their vision wavered.

And then—

*Shhk.*

An eternal blackout, one that light would never pierce again.

*Fwoosh!*

Fountains of blood surged into the air. The things that had once been people and horses were severed into pieces and flung in every direction.

They flew on with the same force they’d charged with—

toward the enemies they had chosen as their first targets, but never reached alive.

*Crunch!*

Even the lightest of them had weighed hundreds of *geun* in life, some nearly a thousand.

Jin Mukyung calmly looked down at the enormous chunks of flesh, caked in dirt and blood, that had carved deep furrows as they slid to his feet.

More precisely, he looked at their impossibly clean cut surfaces—and the sword in his grasp.

*As sharp as ever. Almost unbelievable.*

Admiration flickered in Jin Mukyung’s eyes as he gazed at the blade, its cold edge gleaming even in the dark.

Only two days earlier, he’d felt the new sword’s excellence in battle against a thousand enemies. And yet he couldn’t help being surprised all over again.

He was, after all, a swordsman with a desire for fine blades.

*I wondered what was going on when he suddenly handed me a sword I’d never seen before. If I’d refused, I’d have regretted it for the rest of my life.*

To a martial artist, a cherished weapon was their closest friend and family.

But just before Jin Mukyung’s first campaign, as he was polishing his beloved sword, a sturdy old man came to see him. He dropped a long bundle of cloth in front of him and said:

*“Get rid of that one. Use this from today on. I forged it for you well in advance, Second Young Master.”*

At first, he’d thought the old man was out of his mind.

He was telling him to discard the sword he’d used for over ten years—the one his older brother Jin Wikyung had spent enough to tear out one of the pillars of the Jin Family of Taiyuan to make.

But when a sword appeared from between the folds of the cloth, and at last its gleaming white blade emerged naked from its scabbard, Jin Mukyung understood.

The lunatic old man standing before him was an outstanding artisan unlike any he’d ever seen.

An artisan with more than enough skill to forge a divine weapon.

*“You’ve got a good eye, judging by your face. That’s a relief. You look worthy of being its owner, at least.”*

*“What is this…?”*

*“Can’t you tell? It’s one of the finest things this old man has ever made, and I worked myself to the bone making it in my old age. I forged it from something that can rival Ten-Thousand-Year Cold Iron, so take good care of it.”*

The old man had left without hesitation after saying that. Jin Mukyung remained absorbed in his new sword for a long while, until one of the family retainers finally told him who the old man was.

*“Come to think of it, Second Young Master might not know. The Ironcraft Hall was newly established in our family while you were in secluded training.”*

*“The Ironcraft Hall? Then that old man was…”*

*“Yes. He’s Hall Master Jang Taebo, head of the Ironcraft Hall. In the past, he spent over thirty years as Guild Leader of the Ironcraft Guild.”*

*“……!”*

Even Jin Mukyung, who had devoted himself to martial arts at the Jin Family of Taiyuan and Heaven’s Gate Temple, knew of the Ironcraft Guild.

A place where the finest artisans in the world gathered.

A group so proud of its skill that it would never sell a weapon to someone who lacked the qualifications, no matter how much gold they offered.

The retainer didn’t know why Jang Taebo, who had reigned as the guild’s greatest artisan for decades, was now at the Jin Family of Taiyuan. But there was one thing he knew for certain.

*“I believe he formed a connection with the Third Young Master. So, around the time you entered secluded training, he reversed his retirement and joined our family.”*

*“Taekyung? That guy?”*

*“Yes. And somehow, Hall Master Jang brought a great many artisans who’d belonged to the Ironcraft Guild along with him. It was probably because of his old ties to them.”*

But there was something neither the retainer who’d given him that information nor Jin Mukyung, fresh out of secluded training, knew.

The artisans who had left everything behind and rushed to the Jin Family of Taiyuan had not been moved by loyalty at all.

What had brought even the old Master Artisans who’d left their forges before Jang Taebo back to work was the final gift of a great spiritual creature, one that had once swum in a deep river more than ten thousand *li* away.

The Water God Dragon.

The imugi had failed to become a dragon, never obtaining the dragon pearl, and had ultimately been corrupted by Dark Heaven. But with a young man’s help, it found eternal rest and left behind its sacred body.

An ingredient for working metal so rare that even a meteorite fallen from the heavens or Ten-Thousand-Year Cold Iron might pale in comparison—something no famous artisan could resist.

And, naturally, a considerable amount of it had secretly made its way to the Jin Family of Taiyuan.

Its flesh and blood, imbued with spiritual power over hundreds of years, had become elixirs in their own right. Its incredibly strong bones had been made into weapons, and its thick, sturdy tendons and muscles had become parts of armor.

Before long, the Water God Dragon’s remains had been worked into every corner of the Jin Family of Taiyuan.

Just as they were at this very moment.

*Whoosh!*

No matter how fine the net, how could it catch every minnow?

With their path blocked by Jin Mukyung alone, the steppe nomads had faltered at the sight of their comrades’ gruesome deaths. The arrows they loosed to keep the Jin forces at bay slipped between the government troops’ shields and struck a martial artist of the Jin Family of Taiyuan in the chest.

Or at least, that was what it looked like for a moment.

*Thunk!*

The arrow bounced away without force, its earlier, powerful whistle now seeming absurd.

The martial artist of the Jin Family, who had felt certain he’d been mortally wounded and had been about to scream, stared with wide eyes.

“Guh—huh?”

He blinked blankly, then finally remembered.

The thin something he’d strapped over his chest beneath his uniform, on the Lesser Family Head’s strict orders.

It was so light, and glimmered so strangely, that he couldn’t tell whether it was iron or leather.

And as soon as he remembered, he burst into loud laughter as if nothing had happened.

“You stupid barbarian bastards! You couldn’t hit our family dog shooting like that!”

“……!”

“……!”

The nomads, who had been ready to trample those weak Han Chinese, could only look at one another in dismay.

Their bows had the power to pierce most leather armor with ease. And now they were useless.

It was only natural for unease to spread at the thought that one of the grasslands’ greatest weapons had been taken away from them.

Of course, they soon realized that even that brief moment of unease was a luxury they couldn’t afford.

“Now! Now’s the time!”

“Loose!”

At that moment, the nomads who now filled the gorge heard a powerful shout from far above, high on the steep cliffs rising on either side.

Then darkness fell like another layer over their heads.

*Shhhhhhh.*

A bleak roar like the sound of waves filled the air. Countless arrows blotted out even the faint moonlight as they plunged down, covering the entire gorge.

“E-everyone, shields—!”

Someone’s cry burst out like a scream, then was swallowed without a trace.

*Clang-clang-clang!*

Sparks bloomed where arrowheads struck the cliffs.

In the slowed world, through that brief, hazy light born of friction, they could see countless men and horses collapsing, spattering blood.

*Whoosh—thud-thud-thud!*

By the time they heard the fierce whistle of arrows, it was already too late.

The steel rain plunging straight down from a height of thirty *jang* drenched everything in its path with a force that outdid the nomads’ composite bows.

With dark red blood. With cries of pain.

“Raaaaagh!”

“Neigh!”

A huge mass of screams, from no one in particular, filled the gorge.

A nomad who had raised his head to look up on instinct writhed on the ground, clutching the arrow stuck in his eye. A steppe horse thrashed with all its might, forgetting even its rider’s safety. And a lucky hundred-man commander who’d saved his life with a tough leather shield let out a relieved sigh.

Before that sigh had even ended, he heard an ominous sound above him.

*Rumble. Rrrrattle.*

*Thunder?*

No. Wrong.

He soon saw the answer to the question that had flashed through his mind.

“Ah.”

A hollow sigh.

*Thump.*

The porcupine of arrows that had been his shield slipped from his weakened grasp, but the middle-aged hundred-man commander didn’t care in the slightest.

He already knew that even the shield that had saved his life couldn’t stop the enormous things rushing at him through the darkness.

*Rrrrrumble!*

Black spheres poured down the rock face out of the darkness, shaking the earth as they came.

Just as the steel rain stopped, the avalanche of rocks came crashing down. The hundred-man commander glanced at the sky, where not even the moonlight could reach.

“……Tengri.”

*Ka-boom!*

With no answer, his sky closed over him.

* * *

*—Isn’t this dangerous?*

Jamukha moved his lips with a calm expression as Chinggen scratched his chin and asked.

*—How many did you send in?*

*—Five or six hundred-man companies?*

Chinggen smacked his lips, then added:

*—Though there aren’t any left now.*

A mere half an hour.

That was how long it took for more than five hundred troops to vanish.

And they hadn’t even had a proper chance to begin fighting.

Their enemies were performing better than expected.

*—That man’s quite something.*

Jamukha knew who Chinggen meant. He nodded quietly.

*—He has the makings of a Sword Demon. Just like you.*

*—He must have been the one who annihilated the vanguard, too.*

*—So, you want him?*

*—If I asked, would you let me have him?*

Chinggen’s eyes gleamed red.

How many years had he spent in a ger reeking of horse manure? At the scent of prey, his blood was boiling for the first time in ages. Jamukha clicked his tongue softly.

*—You’re still young. Even at your age, you haven’t managed to break that habit.*

*—I still haven’t heard your answer.*

*—I’ll give it to you now. No.*

*—What a shame.*

Chinggen frowned, and Jamukha continued.

*—No need to be disappointed. There’s prey elsewhere.*

*—You mean…*

*—Take the cliffs. They’re being a nuisance, so we should deal with them before any more time passes.*

*—Now that’s an excellent choice.*

Chinggen beamed.

Then he set off toward the prey waiting for him on the high cliffs.
## Chapter artifact 957

# Chapter 957

The cliffs flanking Eight Spring Gorge were practically enormous walls in their own right.

How could they not be?

They stood more than thirty *jang* high.

Even the Great Wall, built long ago by a tyrant who unified the continent by squeezing the lifeblood out of his people, was barely three *jang* tall.

To go around the cliffs and reach this place, an army would have to spend days crossing rugged mountain ridges. To break through head-on, they would have to climb the sheer rock face rising into the sky.

Of course, that wasn’t impossible in itself.

It was commonly accepted that even an experienced Mountain Herb Gatherer or hunter could climb one over a long period of time, provided they made sufficient preparations.

The uneven cliff face gave them footholds for their hands and feet, after all.

But—

If a thousand archers filled the cliffs on either side of the gorge and had no intention of welcoming their uninvited guests, that changed everything.

Just as it did now.

“AAAAAAAH!”

The nomads surged toward the cliffs like a swarm of ants, their cries impossible to distinguish as screams or battle shouts.

At that very moment, the officers, their sharp eyes fixed on the scene in the darkness below, spoke as one.

“Everyone!”

“Loose!”

*Flap!*

A red flag, its color barely discernible in the dark, plunged down like lightning. At once, a thousand tightly drawn bowstrings were finally set free.

*Thrum-thrum-thrum! Fwoooooosh!*

The sound of waves echoed through the deep mountains.

Arrows shot through the faint moonlight quivered as they flew, as if they knew what awaited them at the end of their brief journey.

*Clang! Thud-thud-thud!*

“Gaaah!”

“No! Holrogu!”

Bodies tumbled in every direction amid the screams.

But the expression of the man watching the gruesome sight from atop the distant cliffs remained grim.

*Even with every archer firing in a concentrated volley, we only got a hundred.*

A faint, clear light shone in his eyes—a sign that he had mastered high-level martial arts, and that he could pierce the darkness spread out below.

*Their losses are smaller than expected. Even if they abandoned their horses in advance and used shields to protect themselves, this is…*

There was only one answer.

After a moment’s thought, the man made his decision and raised his baton. His adjutant, standing by with a tense expression, tied his superior’s order to an arrow and shot it toward the opposite cliff.

*Fwish.*

It was still an arrow, though it traced a smooth arc.

And yet the moment it arrived with a sharp whistle, it was caught as if sucked into someone’s hand.

Effortlessly, at that.

*Tap.*

The old man caught the arrow without looking, untied the missive fastened to its shaft, and handed it to an officer nearby. Clad in armor, the officer quickly scanned its contents.

“Well? What does it say?”

“He says that, judging by how sharply their casualties have fallen, the enemy must have sent in their elite troops.”

“That’s a headache, but… well, it might actually be a good thing for us.”

The old man stroked his snow-white beard.

These towering cliffs were the perfect position for a siege defense.

They were one of the main reasons Eight Spring Gorge had become a natural fortress—and why the defenders had won decisive victories in both of the great battles fought here.

The enemy elites sent to scale the cliffs were about to see a hellscape.

“And what else?”

“He asked our left wing to deal with the men climbing the cliffs, while the right wing keeps the enemy attempting a frontal assault through the gorge in check.”

“Asked? I may be the senior one by age, but on a battlefield like this, I follow the general’s orders. Don’t I?”

The officer offered no answer, only an uncertain smile.

As far as he knew, the old man before him was an astonishing master with a great reputation in Murim, while the man on the opposite cliff was his superior by far.

As a middling commander, he couldn’t think of an answer to give.

All he could do was follow orders and offer a cautious suggestion.

“The Assistant Military Commissioner did ask…”

“That’s enough. Enough. In the end, it means this old man has to get involved, doesn’t it?”

The old man waved a hand, slapped his lower back, and stood up. Something dark and dull was already in his hand.

*Thump.*

It was far too long to be called a cane, reaching nearly a *jang*. And it struck the rock with a weight that made it hard to call it wood.

*What in the world is that?*

Leaving the officer’s unspoken question behind, the old man walked to the front of the archers who were firing without pause and plopped himself down.

He recalled the conversation he’d had with Jin Wikyung before the battle began.

*“Senior, I’ll need you to take charge of the cliffs.”*

*“I owe you a debt, so of course I’ll do as you ask… but this doesn’t sound like you. Wouldn’t I be far more useful down below?”*

The old man’s objection was reasonable on the face of it.

Of the fifteen thousand troops, a thousand carefully selected archers held the cliffs and poured down a rain of arrows. How many of the enemy would make it up alive? And why would they need a master with profound skill?

But Jin Wikyung’s immediate answer had been firm.

*“You’re right. They’ll think the same thing.”*

*“……!”*

*“They’ll climb the cliffs. They’ll have to.”*

*“You’re already certain of it.”*

*“Our allies on the ground will fight to the death with everything they have. It’s only a matter of time before the enemy targets the cliffs. And their very best elites will be among them.”*

*“And you want this old man to stop those elites?”*

*“If we can stop them from scaling the cliffs, we can deal them a major blow. If we hold that position to the end, we can level the scales, even though they’re tipped so heavily against us.”*

Only then had the old man remembered.

Though he’d known him for less than a year, the Lesser Family Head of the Jin Family of Taiyuan had always made the wise choice.

*“Fine. I’ll land you a big fish in this battle, just like you want.”*

*“Don’t push yourself too hard. I know you’ve recovered completely, Senior, but you still need time to recuperate…”*

*“Don’t worry. I’ve already owed the Jin Family of Taiyuan my life twice. This time, I’ll repay every bit of it.”*

People of Murim did not forget gratitude and grudges.

The older they were, and the more Fame they had built, the more so.

And the old man was both old and renowned.

He had spent his whole life in his hometown, never belonging to any sect. Even after reaching the lofty realm of Supreme Peak, he had never left it.

He’d intended to lay his bones in the place where he was born and raised.

That is, until the day he lost his mind, soon after meeting a woman of extraordinary beauty.

“At last… the time has come to repay my debt.”

The old man murmured in a low voice.

The Jin Family of Taiyuan was not the only one to whom he owed a debt. They had restored the mind that had been taken from him against his will and spent months treating his grievous injuries.

There was also Dark Heaven.

He owed them a debt of vengeance, too.

No—he had to take revenge.

“Come on, then.”

The small-framed old man smiled faintly and gripped his beloved weapon. Then, with the same motion he’d repeated countless times since childhood, he swung both arms with force.

*Whoom.*

His weapon—an impressive three *jang* long—whipped and bent as it scattered a dark, dull flash.

A white-silver line and hook trailed from its tip, shooting toward the enemies who were climbing the cliff to evade the rain of arrows.

*Shwaaaaa! Shhk!*

White streaks of light tore through everything around them.

Flesh and bone split like tofu. Dozens of severed limbs, armor and all, slid down the cliff.

Overwhelming power.

The enemies had no way to evade the old man’s attack, which combined his personal martial prowess with the advantage of the terrain.

Or so it seemed.

Until, the very next moment, a flash of red flickered through that dense silver net spread across the cliff.

*Shhk. Shhk!*

A faint whistle, quieter than the wind.

But the old man felt it clearly.

The blow had severed part of the silver line that writhed like a living thing as it tore the enemy to pieces.

And the power behind that red flash was in no way beneath his own.

*Force…!*

No doubt about it.

Only the same kind of power could sever Heavenly Silkworm Thread imbued with Force in a single swing.

“How dare you!”

*Shwick!*

The old man’s hand blurred as he roared.

His beloved weapon, imbued with strength and speed, thrashed like an imugi. The archers, sensing something was wrong, gritted their teeth and drew their bows.

“Concentrate your fire!”

“That one! The man at the front is their leader! Fire together!”

*Thrum! Sh-sh-sh-shhk!*

*Thud-thud-thud!*

“Gah… urk!”

“Aaaah!”

Whistles and screams rang out without pause.

But nothing could stop the figure that had slipped through the mighty web of arrows covering the cliff.

*Clang!*

He batted away the old man’s next attack.

*Whoosh!*

He twisted his body, dodging dozens of arrows aimed at him from every direction as if performing an acrobatic feat.

*Tap.*

He stepped onto the steep cliff.

No—he blasted off it.

*Ka-boom! Fwoooooosh!*

It was a run and a flight at once.

He moved so fast that even a master of the Wall Lizard Technique could not have replicated the feat, charging straight against the laws of the world laid down since time immemorial.

And finally—

*Tap.*

The figure reached the edge of the distant cliff and faced the old man waiting for him.

Or, more precisely, the silver flash whipping around at the old man’s fingertips.

*Whoom. Shwaaaaa!*

Space split apart.

Amid the wind cut into dozens, then hundreds of pieces and the brilliant white glow of Force, the old man saw the figure’s face.

A gaunt build. Sharp eyes.

The man was unmistakably a nomad—and at that moment, he was smiling.

“……!”

*Crack!*

A section of the cliff crumbled helplessly under the tremendous force.

But there was no sign of death anywhere.

As the archers on the cliff wavered, the old man clicked his tongue and suddenly spoke to the man standing upright on empty air.

“Who are you?”

The man answered.

“A hunter.”

“Then you’ve come to the wrong place.”

“That’s what I thought at first, too. But I changed my mind.”

The man—Chinggen—looked at the old man and licked his lips.

“You’re a little old, but you look pretty appetizing. Don’t you think?”

The old man snorted.

“Third Rate hunter. You don’t even know that the older you get, the tougher you are.”

“That’s fine. My teeth are strong.”

Chinggen bared his teeth in a grin, then asked,

“So who are you?”

“A fisherman.”

The old man answered calmly, then added,

“I thought this place was full of minnows, but I’ve just caught a whopper I never expected. It’s put me in a pretty good mood.”

“That fish looks too big for an old man like you to catch.”

“What can a brat like you do, no matter how much you flop around? I’ll grab you by the tail and smack you against the ground a couple of times. That’ll be the end of it.”

“Oh, yeah?”

The hunter looked at the fisherman and smiled. At that moment, the title of someone who resembled the old fisherman before him was circling through his mind.

A previous-generation master who had reached great heights, yet never left the riverbank—and wielded a strange weapon.

“We’ll soon see who succeeds in the hunt. Won’t we, Dongting Fisherman?”

The old man, Dongting Fisherman, raised his beloved black-wood fishing rod and answered,

“Indeed. What a catch.”

*Shwaaa!*

Two currents of wind collided head-on.
## Chapter artifact 958

# Chapter 958

*Ka-boom!*

A faint tremor followed the explosion.

Jamukha stroked his beard as he watched a pale cloud of dust rise atop the distant cliffs, visible even in the darkness.

*Looks like they’ve started.*

Jamukha knew Chinggen—or, more precisely, the person wearing Chinggen’s face—well.

Cruel, savage, and strong.

No matter who he ran into up there, he would carry out his assigned task. And he would do it exceedingly well.

*Clang! Krrrunch!*

Flashes of light flickered without pause through the dust cloud, followed by more deafening crashes.

Below, the nomads had shed their armor and taken up hooks and daggers. As the archers’ fire slackened, they seized the opportunity and rapidly climbed the cliffs.

“Loose!”

*Fwish-fwish-fwish!*

Arrows continued to fly, accompanied by occasional shouts, but that was all.

The archers’ composure and accuracy—and the dense crossfire pouring down from both sides—had faltered beyond comparison with what they’d been moments before.

Of the thousand archers holding the two cliffs facing each other, half had already been tied up by Chinggen. The other half also had to keep the ground forces in check as they surged into the gorge once more.

A net stretched thin would eventually tear.

Jamukha intended to bring that moment a little closer.

“Mukal. Jerme.”

“Yes.”

“Give your orders, Khan.”

At Jamukha’s quiet summons, two men stepped forward.

Their clothing alone set them apart from the other nomads. Among the Keshik Jamukha had personally trained over many years, they were two of the most capable.

Following the example of the great conqueror who had once crossed the steppe and ruled the continent, Jamukha called them the Five Steeds and Five Hounds.

Five fine steeds and five loyal hounds.

The ten commanders of a hundred were outstanding leaders and fearsome warriors alike. For decades, they had been Jamukha’s most loyal servants.

Though only days ago, he had lost one of them in vain.

“There are cowards hiding up there, doing nothing but shooting arrows. What should we do?”

“We’ll break their bows, cut their throats, and return.”

“It’s close to the heavens. Tengri will be watching over us.”

The two commanders struck their studded armor with clenched fists, then turned away.

Jamukha watched them lead a hundred Keshik apiece, deflecting the arrows as they quickly began climbing the cliffs. Then he spoke again.

“Tiraun. Boorchu. Ongge.”

Three this time.

Jamukha pointed toward the gorge, where screams rang out without end.

“Your sworn brother’s killer is there.”

“……!”

“……!”

“……!”

The corners of the three men’s eyes twitched.

It wasn’t just because they remembered their sworn brother, who had left days ago at the head of the vanguard with a hundred Keshik under his command, only for his head to return without him.

It was pride.

Their lord was telling them to join forces and avenge the sworn brother who had died before them.

“Khan. I’m more than enough for him on my own.”

“The same goes for me, Tiraun!”

“Please send me, Ongge!”

Jamukha watched the three commanders step forward, one after the other.

Their bulging temples and sharp, shining eyes showed that these masters had reached the upper reaches of the Peak realm.

But Jamukha was both their lord and their teacher.

He knew them better than anyone.

A few days ago, his subordinate’s severed head had returned instead of news of victory. Jamukha had seen the wound on its neck, leaving him no choice but to make this decision.

*He’s no pushover.*

Send one man, and he wouldn’t return. Send two, and only one would make it back. Send three, and they would surely return with the man’s head.

That was why Jamukha’s resolve did not waver, despite the three commanders’ fighting spirit.

“Go.”

His voice was calm, but its chill was unmistakable.

This was an order. They could not refuse it.

Realizing there was no way to defy Jamukha, the three commanders bit their lips and turned away.

Then, like their comrades who had set off for the cliffs ahead of them, they led their Keshik forward at a run.

Hundreds of figures shot across the gorge at speed, having left their horses behind. They clambered over the bodies of men and mounts, and over rocks.

Their first victims were not the Shanxi defenders, who continued to resist fiercely, but their own allies, stumbling backward in fear.

“T-this isn’t right! This isn’t right!”

“Black Sheep Clan, withdraw at once! Fall back and regroup—!”

*Shhk!*

The old chieftain’s head flew into the air.

Hundreds had joined the battle after the Great Steppe’s call to arms, but now the survivors of the small clan—reduced to half their original number—stared wide-eyed.

“C-Chieftain!”

“How dare you!”

But dozens of spears and swords were already closing in from every direction.

*Fwoooosh! Thunk!*

“Guh—!”

With every flash of a blade, heads and limbs rolled across the ground.

The Keshik slaughtered a hundred or so clansmen in moments with their lances and scimitars. The entire gorge froze at the sight.

So did someone watching from far away.

“W-what are you doing?!”

Temur’s voice shook as if he were caught in an earthquake.

But the answer that came back, in both voice and gaze, was drier than the steppe’s bitter wind.

“They disobeyed the Khan’s orders and ordered a retreat on their own. We simply carried out the summary execution.”

“B-but they’re under my command—”

“That’s right. They’re your people, Khan Temur.”

A voice slipped between Jamukha’s lips, too quiet for anyone else to hear.

“And the man who commands them is standing right beside me.”

“……!”

“Is there a problem? If you have any complaints, speak now.”

Temur suddenly understood, under the pressure that felt like it was gripping his heart.

The other man had drawn a line, and that was as far as Temur was allowed to go.

If he crossed it even slightly, he would meet the same fate.

“N-no problem.”

“I can’t hear you very well. I must be getting old.”

“N-no problem.”

At last, Jamukha nodded at the words Temur forced out through his fear and humiliation.

“A wise choice. Military discipline must always be strict. Don’t you agree?”

Temur trembled instead of answering.

He had expected it when he begged for his life in front of Chinggen’s corpse, but had tried to look away. Now the terrible future he had feared was laid out before his eyes.

*Clang-clang-clang!*

*Raaaagh!*

From the cliffs. From the gorge.

The constant clashes of weapons and screams still ringing through the air mostly belonged to the clansmen who had followed him into battle.

But as they died, those men would never know that the two young Great Chieftains who had brought them a brief peace and prosperity had already betrayed them.

*No. I’m the only traitor. I’m the one who led them to their deaths.*

Temur clenched his teeth until they drew blood.

Chinggen had died with his courage intact. Temur had survived in shame.

He had fallen for the promise that if he cooperated fully, they would spare his life and let him keep his position as Khan.

No—that was just an excuse.

He had simply—

*Wanted to survive. No matter what it took.*

Yes. That was the only truth.

And this was the result.

Leading twenty thousand clansmen who followed him and Chinggen into that dreadful gorge as arrow fodder, as human shields.

“Damn it.”

Jamukha’s brow furrowed at the mutter that slipped through Temur’s clenched teeth. Just then—

“Khan!”

A figure approached at a run, accompanied by an urgent shout.

Jamukha recognized him as one of the Keshik who had headed into the gorge with the three commanders moments earlier. His gaze darkened at the sight of the weapons in the man’s hands.

A lance, a scimitar, and a bow.

Even at a glance, the three weapons gave off a cutting edge far beyond that of anything the other nomads carried. They were familiar to Jamukha.

They had been specially made as gifts for the ten commanders of a hundred who had excelled above all others among the Keshik, his personal guard.

Jamukha didn’t need to ask what fate had befallen their owners.

“Did those boys pass in peace?”

The Keshik lowered the weapons that had become keepsakes and bowed his head.

“They fought bravely as warriors. Surely they’re now in Tengri’s embrace.”

“Yes. I see.”

Jamukha murmured softly.

Kill someone, and be killed by someone.

That was the inescapable fate of a warrior of the Great Steppe.

And it was the same for everyone else.

“What of the other losses?”

Everyone present already understood what he meant.

Even now, dozens of nomads were bleeding and falling somewhere in the gorge, but their lives were not part of any calculation.

Jamukha cared only about the losses among his personal guard.

“Though three commanders of a hundred have fallen, our overall casualties are small. Only around twenty are dead or wounded. The rest have withdrawn to the rear and await new orders.”

Three commanders had died, but their troops had suffered few losses. That could only mean one thing.

Remembering the commanders’ confidence that each of them was enough on his own, Jamukha let out a quiet laugh.

“They disobeyed my order.”

There was no doubt those three had fought a life-and-death duel.

One after another.

Foolish as commanders, brave as warriors.

And one by one, they must have lost their lives to the young Sword Demon of the Jin Family of Taiyuan.

“Those pathetic fools.”

Jamukha silently looked down at the Keshik, who could only bow his head even lower rather than agree. Then, abruptly, he spoke.

“Order the Keshik still in the gorge to charge.”

“Khan. You mean—”

“The senior ten-man commanders will temporarily take the vacant posts of commanders of a hundred. Minimize our losses as much as possible and wear them down.”

There would be no more reinforcements.

Several other commanders of a hundred remained at Jamukha’s side, but Eight Spring Gorge was only the first hill they had to cross.

He had no intention of wasting more strength in this narrow gorge—or of trusting the commanders who might do something foolish again at any moment.

He wanted a sure bet instead.

Not a fine steed or loyal hound that raced like the wind according to the direction of Jamukha’s reins, but a vicious dog that served the same master as he did.

*Ka-boom!*

Jamukha watched calmly.

Amid the tremendous roar that shook heaven and earth, a streak of red light came hurtling down toward the ground along with a section of the cliff.

* * *

*Fwoosh.*

The breeze felt cool as it brushed his hair.

It was a refreshing sensation he could never have experienced in the training hall deep inside the cave.

Like a reed swaying in the wind, Jin Mukyung twisted his body with ease.

*Shwaack!*

Five lances grazed his arms, legs, and waist as they passed.

Jin Mukyung reached out, and a gleaming white-silver blade slid along the steel shaft of a lance.

*Shhk!*

A cold slicing sound announced another death.

At the same moment, the strength and weight behind the shaft vanished.

Jin Mukyung seized the shafts that had crossed past him, grazing his body, and spun rapidly.

*Krrrunch!*

There were no screams. Only a thick mist of blood.

Using the five spears as the teeth of a gear and his own body as its axis, Jin Mukyung ground everything within a three-*jang* radius to pieces. He realized there were no enemies left around him.

And he realized that it wasn’t solely because of his own skill.

*Ka-boom! Rrrumble!*

The gorge shook.

Amid a deafening roar that seemed to split the sky, enormous and small rocks came pouring down. A streak of red light, bending like a living creature, flashed across Jin Mukyung’s eyes.

*Clang!*

A powerful impact struck his sword.

As Jin Mukyung retreated, a dull ache running up to his wrist, an exuberant voice reached his ears.

“Now that’s a shame. If I’d gotten a little more used to it, I could’ve landed a whopper.”

Chinggen.

He tossed aside his black-wood fishing rod, soaked in dark red blood, and raised two swords, one long and one short. He smiled.

At his new prey.
## Chapter artifact 959

# Chapter 959

Everything in the world had its own color, and people were no exception.

Their eyes, their expressions, the distinctive energy surrounding them—all of it described and revealed who they were.

And in that sense, the moment Jin Mukyung saw the man before him, instinct told him what he was.

*A demon.*

The two syllables flashed through his mind.

There was no mistake.

The eyes drunk on killing intent. The corners of his mouth, curled in a lazy smile.

And the scent of blood seeping from every inch of the man’s body was so strong it stung the tip of Mukyung’s nose just standing near him.

*What… is this bastard?*

Jin Mukyung stared at the man with a steady gaze.

He could feel it in his skin. He understood it in his mind.

This new enemy who had appeared out of nowhere was on an entirely different level from an ordinary villain.

Even Pung Yang, the Red Wind Band Leader, who had once raided the Mount Heng Sword Sect and dealt Mukyung a serious Internal Injury with a level of skill no one had expected, seemed like nothing more than a mounted bandit compared to this man.

A different breed. A different class.

Not only in the slaughter he had wrought, but in his own martial prowess.

Looking back at Mukyung, Chinggen grinned.

“Just as I thought. You’ve got good eyes.”

*Step. Whish!*

The instant Chinggen took a casual step forward, as if out for a stroll, Mukyung sprang back a great distance and raised his sword at an angle.

“Your Qi Sense is useful, too.”

Chinggen nodded with satisfaction.

He had let only the faintest trace of killing intent slip—and Mukyung had reacted without a moment’s hesitation.

Though they were enemies, Chinggen rather liked the young Sword Demon before him. More than he should like mere prey.

“You’ve got the gloomy air of an old man on his last legs, but you’re still a young brat… Who are you? Want to be my Disciple?”

At those words, which no one could have expected, the battlefield—briefly stilled by Chinggen’s arrival—stirred.

More than anyone, the hundred or so nomads groaning amid the gaps in the collapsed rocks stared wide-eyed at their Great Chieftain, doubting their own eyes and ears.

They belonged to the western grasslands ruled by Temur and Chinggen. They knew the two young Great Chieftains well, which made this all the harder to believe.

Chinggen had taken the position of Khan through his strategy and ability to rule, rather than his personal martial prowess. And now he was making such an offer to the man who had slaughtered hundreds of their brothers on the grasslands all by himself, using an extraordinary level of martial skill.

“K-Khan!”

“What are you saying…?!”

Shocked cries rang out from every direction.

The joy they’d felt at the arrival of Chinggen and the Keshik had vanished long ago.

Chinggen smacked his lips at the sight of the nomads staring at him with wide eyes, each nursing injuries of varying severity.

“Though I guess it’s a pretty strange time to make an offer, huh? Especially with so many people watching.”

It happened then.

The short sword in Chinggen’s left hand blurred.

*Shk. Rrrrrumble!*

With a cold, slicing sound, the piled rocks—barely holding together—came crashing down on the nomads.

Their screams as they waited for rescue were swallowed by the roar, then disappeared completely.

“Useless, worthless things. Always running their mouths. That’s the problem with them.”

“……!”

“Now that there’s no one watching, let’s get back to what we were talking about. Hmm?”

In the sudden silence, Jin Mukyung fixed Chinggen with a deep, steady gaze and spoke.

“So you’re Chinggen, you bastard?”

“Hey, now. ‘You bastard’?”

Chinggen clicked his tongue and continued.

“Even if you’re a brat, that’s no way to speak to your Master. I ought to rip that tongue right out.”

His easygoing manner, and the confidence of a master he couldn’t hide.

Mukyung had no trouble realizing that the man before him, with his hair tied in the distinctive nomad style, was a being made up of countless secrets.

“You’re using a disguise technique. Where is the real Chinggen?”

Chinggen considered the question before answering.

“Who knows? Maybe inside an eagle’s belly by now.”

“And the other one?”

“The other one? Oh, I left Temur alive. One of them had to survive if we were going to keep the westerners under control.”

Chinggen answered without hesitation.

The Keshik controlled everything within a radius of several dozen *jang*. Jamukha had spent many years raising them into his personal guard, and they would never betray their master.

Even the fiercest hunting dog wouldn’t bite its owner.

“Well, I think I’ve answered enough of your questions. So, what do you say to my generous offer?”

Chinggen was looking at Mukyung with great anticipation when—

“Impossible.”

A low voice rang out unexpectedly.

Chinggen frowned at the face he saw over Mukyung’s shoulder.

“Impossible? Why not? No, first—who the hell are you?”

The uninvited guest who had interrupted the conversation answered calmly.

“How could a wolf serve under a mangy dog? He’s my little brother, whom I’ve cherished like my own son. As his older brother, I can’t let that happen.”

“Little brother? Older brother?”

Chinggen looked at the uninvited guest, Jin Wikyung, his eyes widening slightly, then gave a quiet laugh.

“Brothers from the Jin Family… Well, that’s a much bigger catch than I expected.”

*A big catch.*

At those words, Jin Wikyung’s expression grew grave.

He remembered the old fisherman who had laughed heartily before the battle and promised to bring back a big catch.

“What happened to Senior?”

He had an idea, but still wanted to hear it from the man’s own mouth.

What had happened to the Dongting Fisherman, who had risked his life for the Jin Family of Taiyuan—the owner of that dark fishing rod lying on the ground?

And foreboding was rarely wrong.

“Oh, that old man.”

Chinggen continued with a faint smile.

“He was pretty good at fishing, but he didn’t have the strength for it. He hooked something way too big for him and snapped. Just like that fishing rod.”

“……!”

“Actually, ‘snapped’ isn’t enough. More like crushed to pieces. He was slammed more than thirty *jang* down.”

Jin Wikyung swallowed a groan.

Soaked in dark red blood and cracked in several places, the black-wood fishing rod showed how fiercely the Dongting Fisherman had fought.

The old fisherman, who had always said he wanted his ashes scattered in a blue river when he died, had buried his bones here today, in this gray gorge.

He had given his life for the Jin Family of Taiyuan, repaying the life he owed them.

And now the Jin Family owed him a debt in return.

Not only to the Dongting Fisherman, but to everyone who had died so far.

“Give me your name and title.”

“What?”

“I need to know who you are, so I can speak with my head held high when we offer a memorial rite for the dead in the future.”

Jin Wikyung fixed Chinggen with a cold gaze and continued.

“So we can say we personally tore apart and killed the bastard who dared invade Shanxi Province and harm you all.”

“……!”

“No matter how badly the world’s gone to hell, isn’t that the proper thing for people to do?”

Chinggen blinked his wide-open eyes, then suddenly burst into loud laughter.

“Ha! Hahahahaha!”

His laughter boomed through the gorge, pressing down on everything around it.

No—it could no longer be called a mere sound.

*Vrrrrm. Rrrrattle!*

The air swelled.

A tremendous pressure shook the earth and cliffs as if an earthquake had struck, and groans escaped from all around.

“Urgh…!”

Was this what it would feel like to be caught in a giant’s grasp?

The immense energy carried by Chinggen’s uproarious laughter made those nearby lose their balance and stagger.

Some of the lower-level martial artists, with only a little internal energy, went pale and even spat blood.

“A Supreme Peak master…!”

The words slipped from someone’s lips like a groan. The shock in them spoke for everyone.

No. Even that wasn’t enough.

Just as dozens of mountain peaks varied in height, the man before them, wearing Chinggen’s face, could not be fully described by the words Supreme Peak.

*Sssssss.*

At that moment, the martial artists of Shanxi Province could hardly believe their eyes.

Shattered fragments of rock, large and small, were rising into the air as if attached to invisible threads.

There were more than a hundred of them.

Their jagged edges were hidden weapons in their own right, and the man standing tall at their center was nothing less than a monster.

A monster of endless change, wearing human skin.

*Crack. Crrrunch!*

Bone shifted, flesh crushed—the man’s appearance changed with a series of chilling sounds.

Everyone stared, stunned by the sight. Then three streaks of light flashed from somewhere.

*Shwaaa!*

The air split.

Three people crossed the space like bolts of lightning, so fast even the Keshik couldn’t react in time. As if they’d rehearsed it, all three attacked at once.

*Whoom. Whish!*

A mighty punch and two swords blazed with brilliant light as they rushed toward Chinggen—

“How dare you!”

*KABOOM!*

With an enraged shout, an enormous force burst out like lava and drove everything around him away.

A violent gale whipped through the gorge.

*Fwoooooosh!*

A thick cloud of pale dust rose, obscuring everything beyond arm’s reach.

The three attackers were thrown back three *jang* by the irresistible force. They exchanged deep, steady looks—when—

*Pop!*

With a sharp crack of displaced air, Chinggen—or rather, someone entirely unfamiliar, whom none of them had ever seen—appeared.

*Thud.*

A heavy footstep.

The old man, whose body was as big as two or three ordinary men, wiped the sweat from his brow with his sleeve and muttered,

“Damn it. I just can’t get used to this.”

The man who had been called Chinggen moments before ran his hands over his own face, returned to him after so long, and his flesh, which seemed ready to burst at any moment.

Old and ugly.

That alone was more than unpleasant enough, but being ambushed while painfully reversing his disguise technique and Bone-Shrinking Technique had put him in the foulest of moods.

“You ungrateful little bastard…”

The old man glared at the rats who had dared to ambush him. His eyes were so narrow and buried in fat they seemed impossible to see.

At this moment, he was truly furious.

All the more so because Jin Mukyung, who had won his heart for the first time in a long while, was among them.

“How dare you ambush your Master? You’re expelled.”

At the old man’s declaration, Jin Mukyung found himself wondering what his troublesome younger brother would have said to such nonsense, had he been here.

And soon enough, he found a plausible answer.

“Go suck a dick.”

“……!”

“Oh. And you’re a fat pig, too.”

The old man’s eyes, reddening in an instant with anger, reflected the two men grinning on either side of Jin Mukyung.

“And who are you two?”

The two men, one young and one old, answered readily.

“Ghost Sword Wipeng.”

“Tiger of Mount Heng, Cheol Mubaek.”

At the answers from the two Peak masters representing the Jin Family of Taiyuan and the Mount Heng Sword Sect, the old man licked his lips with a nimble tongue that didn’t match his size.

“So, one of you’s about to die and become a ghost, and the other’s a dog from Mount Heng. Good to know.”

*Shing.*

The cold scrape of metal.

The old man crossed the two swords in his hands and spoke.

“When you get to the underworld, tell them the Demon Bird sent you.”

Those words were the signal.

A signal that threw the stopped time of the battlefield, and the wick that had barely remained, into a blaze of blood-red flame.

“Waaaaaah!”

With a great roar that woke the deep night, two waves crashed into each other.

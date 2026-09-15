# Checkpoint Review — 175–179

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

# Chapters 175–179

## Plot

Jin Taekyung awakens after Jeok Cheongang’s attack with only a minor Internal Injury. When Taekyung and Hyuk Mujin attempt to flee, Jeok confronts them and questions Taekyung about Jopil. Jeok recounts how he rescued the orphan Jangcheon during an epidemic, raised him as a Disciple, and later discovered that he had become the remorseless killer Jopil. Jeok followed Jangcheon for four months, witnessed him murder a captive, and could not bring himself to kill the Disciple he regarded as family. Jangcheon escaped after taking Bone-Melting Powder.

Jeok admits that he asked the Azure Sky Sword King to help Jopil escape and would make the same choice again despite the decade of regret that followed. Learning that Jopil died fighting Taekyung, Jeok acknowledges that Taekyung did what he should have done and apologizes for his own rash attack. He accepts a debt to Taekyung before dismissing the group.

On New Year’s Day, Taekyung, Cheongpung, and Hyuk Mujin prepare to return to the Jin Family of Taiyuan, already late because Taekyung forgot Wipeng’s warning. Jang Taebo accepts Taekyung’s commission to forge the Ten-Thousand-Year Cold Iron into a world-shaking weapon and asks only that Taekyung rebuild his destroyed home. Taekyung tries to return the Flame Divine Palm martial arts manual and Unnamed Sword, but Jeok tells him to keep them for now. Jeok reveals that the Fire Gate Clan’s Treasured Jade is missing, warns that all Fire Gate Clan items will eventually be reclaimed, and leaves with Cheongpung after threatening Taekyung if the items are stolen or exposed.

## Continuity

- Jeok Cheongang rescued Jangcheon during an Anhui epidemic, raised him as his Disciple, and later discovered that he had become Jopil, a killer who embraced Might Makes Right.
- Jeok followed Jopil for four months, witnessed his murders, and could not execute him. Jopil escaped after taking Bone-Melting Powder and later died fighting Jin Taekyung after drawing on his innate qi.
- Jeok asked the Azure Sky Sword King to help Jopil escape and says he would have saved him again, despite regretting the consequences.
- Jeok acknowledges that Taekyung did what he should have done ten years earlier, owes Taekyung a debt, and apologized for attacking him and his companions.
- Taekyung, Cheongpung, and Hyuk Mujin are leaving on New Year’s Day for the Jin Family of Taiyuan. Taekyung is already late despite Wipeng’s warning.
- Jang Taebo accepted the Ten-Thousand-Year Cold Iron commission without payment and wants his home, destroyed by Jeok’s Flame Divine Palm, rebuilt.
- Taekyung retains the Flame Divine Palm martial arts manual and Unnamed Sword. Jeok says the missing Treasured Jade may have been lost by Jopil or withheld by someone who deceived Taekyung.
- Open hooks: the consequences of Taekyung’s late return, the location of the Treasured Jade, and the completion time of Taebo’s weapon.

## Translation Decisions

- Render 화골분 as “Bone-Melting Powder,” 강자지존 as “Might Makes Right,” and 살성 as “Slaughter Saint.”
- Render 원단 as “New Year’s Day.”
- Render 화염신장 비급 as “Flame Divine Palm martial arts manual.”
- Render 보옥 as “Treasured Jade.”
- Use “Sir Jeok” for 적 대협 in direct address.

## Durable state

{
  "active_continuity": [
    "Jeok Cheongang rescued the orphan Jangcheon during an Anhui epidemic and eventually accepted him as his Disciple; Jangcheon later became Jopil.",
    "Jopil rationalized murder through Might Makes Right and became a Slaughter Saint who took pleasure in killing.",
    "Jeok Cheongang secretly followed Jopil for four months, confronted him after witnessing his murders, and could not bring himself to kill him.",
    "Jangcheon took Bone-Melting Powder and declared that he would leave and never return.",
    "Jopil died fighting Jin Taekyung after drawing on his innate qi.",
    "Jeok Cheongang asked the Azure Sky Sword King to help Jopil escape and would have saved Jopil again despite his later regret.",
    "Jeok Cheongang acknowledges that Taekyung did what he should have done ten years earlier and owes Taekyung a debt.",
    "Jeok Cheongang apologized to Taekyung and his companions for his rash actions.",
    "Taekyung, Cheongpung, and Hyuk Mujin spent the night at an inn and are now departing for the Jin Family of Taiyuan on New Year's Day.",
    "Wipeng warned Taekyung to return to the Jin Family, but Taekyung forgot the warning and is already late.",
    "Jeok Cheongang and Jang Taebo were drinking together at the inn and appeared to have become friendly.",
    "Jang Taebo accepted Taekyung's commission to forge the Ten-Thousand-Year Cold Iron into a world-shaking weapon without requiring payment.",
    "Jang Taebo's home was destroyed by Jeok Cheongang's Flame Divine Palm, and he asked Taekyung to have it rebuilt.",
    "The Flame Divine Palm martial arts manual and Unnamed Sword are in Taekyung's possession after being handed to him by Gong Yacheong and Socheon.",
    "Jeok Cheongang says a Fire Gate Clan treasure called the Treasured Jade is missing; he believes someone deceived Taekyung or Jopil lost it.",
    "Jeok Cheongang orders Taekyung to keep the manual and sword for now and says all items originating from the Fire Gate Clan will eventually be reclaimed."
  ],
  "continuity_sources": [
    179
  ],
  "open_questions": [
    "What consequences will follow Taekyung's late return to the Jin Family of Taiyuan?",
    "Who has the Treasured Jade, or was it lost by Jopil?",
    "How long will Jang Taebo need to complete the commissioned weapon?"
  ],
  "safe_through": 179,
  "temporary_decisions": [
    "Render 화골분 as “Bone-Melting Powder.”",
    "Retain 강자지존 as “Might Makes Right.”",
    "Render 살성 as “Slaughter Saint.”",
    "Render 원단 as “New Year's Day.”",
    "Render 적 대협 as “Sir Jeok” in direct address.",
    "Render 화염신장 비급 as “Flame Divine Palm martial arts manual.”",
    "Render 보옥 as “Treasured Jade.”"
  ],
  "version": 1
}

## Reading copies

## Chapter artifact 175

# Chapter 175

Inside an old guest room, a short, squat old man quietly looked down at the young man lying on the bed.

*So this is Jin Taekyung of the Jin Family of Taiyuan.*

Jin Taekyung’s face was peaceful, even though he still had not regained consciousness. At a glance, he looked as though he had fallen into a deep sleep.

*He took the Flame Divine Palm and this is all that happened to him?*

The old man, Jeok Cheongang, clicked his tongue inwardly.

That had been a Supreme Peak martial art unleashed by none other than his own hands.

He had held back, but even so, it was not the kind of power a young punk who had only just crossed the wall into Peak could withstand.

There was only one answer, and Jeok Cheongang already knew it.

*This boy has cultivated the same kind of Scorching Yang Qi as I have.*

Not all Scorching Yang Qi was the same.

In some ways, internal energy resembled a weapon. Its essence was one thing, but its forms were many.

Advanced internal cultivation techniques could each reveal their own distinct characteristics, like Huashan’s Zaha Divine Technique.

The same was true of the Fire Gate Clan, where Jeok Cheongang currently served as Sect Leader.

*There’s no way that boy learned the Fire Gate Divine Technique.*

For the past several hundred years, the Fire Gate Clan had strictly upheld the principle of passing its teachings down to only one person at a time.

Jeok Cheongang, the current Sect Leader, knew better than anyone that not a single thing had leaked during the process of succession.

And yet, traces of his own school could be seen in Jin Taekyung…

*It must be that, after all.*

The Blazing Flame Divine Pill.

No matter how he thought about it, that was the only answer.

Jeok Cheongang smiled bitterly. If anyone who knew him had seen that lonely expression, they would have doubted their own eyes.

“So it ended up this way.”

His aged voice drifted emptily through the old guest room before scattering.

After chasing something that could neither be seen nor grasped for quite some time, Jeok Cheongang’s gaze finally settled on Jin Taekyung’s face.

It was twisted horribly, as though he were suffering through a nightmare.

“What should this old man do with you…?”

At that moment, Jin Taekyung muttered in a voice resembling a groan.

“Mmmmmm, kimochiii.”

“…”

Kimo… what?

Jeok Cheongang could not understand the word, but hearing it somehow made him feel unpleasant.

He watched Jin Taekyung twitch repeatedly and continue chanting “kimochi,” then slowly shook his head.

*What a strange fellow.*

He did not leave until “kimochi” changed to “yamete.”

By the time Jeok Cheongang could no longer endure the discomfort and fled from the room, goose bumps had broken out all over his forearms.

*…Could this be some kind of dark art?*

His suspicions had just deepened.

* * *

When I opened my eyes, I saw an old ceiling.

I could also see a red oil lamp flickering and the darkened view outside the window. Before I knew it, a sigh of relief escaped my lips.

“Pheeeew.”

I was alive.

I had suffered a minor Internal Injury, but I was grateful it was only this bad.

No, considering that my opponent had been the Fire King, it was nothing short of a miracle.

*Was he really not trying to kill me?*

No matter what I did, I could not beat the Fire King. The same went for Cheongpung.

And yet, here I was, lying on a bed…

“Are you awake?”

“Gah!”

I sprang up like a carp.

Something that had been crouching in a dark corner slowly stood up.

“You scared me, you crazy bastard!”

Hyuk Mujin answered gruffly.

“What are you so surprised about? It’s not like you’re seeing this face for the first time.”

“Look at your face. Do you think anyone could get used to it?”

“What’s wrong with my face? I’m handsome enough. Even my parents used to worry about me when I was young.”

“Worried you’d have trouble living with that face?”

“No. They were worried I’d be kidnapped because I was so pretty for a boy.”

Was he out of his mind?

With an impression like that, I would not have worried about being kidnapped. I would have worried about him becoming a kidnapper.

“…Tell them they don’t have to worry anymore.”

“Later.”

Hyuk Mujin shuffled toward me, then let out a gasp and dropped down onto the floor.

“Ah, aagh! Hold on.”

“What’s wrong?”

He answered with a pained expression.

“I-I’ve got a cramp.”

“…You’ve really done one thing after another today. Are you sure you’re a martial artist?”

“That can happen if you sit for too long. Who do you think I was stuck in that corner because of?”

“How is that my fault?”

“You kept making those strange noises. Gimokji, yamakdae.”

It was like a language carved into my soul.

It was so familiar that it was practically intimate. I asked, startled,

“…I did?”

“Yes. It gave me goose bumps, so I went outside. Then Great Hero Jeok told me to stay inside quietly if I didn’t want to burn to death. He also told me to report to him as soon as you woke up.”

Hyuk Mujin continued with an aggrieved expression.

“He said it might be some kind of dark art, so I should cover my ears. But you just kept going. You were all, ‘Uh? Ah, gimokji, gimokji…’”

“…Stop it, you bastard.”

This was the greatest humiliation of my life.

No wonder I had felt so electrified when I woke up. I must have been having a pretty good dream.

Just in case, I carefully slipped a hand beneath the blanket.

*Hmm. Clean. No problems.*

Now that I had dealt with one problem, it was time to worry about another.

In terms of importance, this problem was incomparably greater than the one before.

My life was on the line, after all.

“Where’s that old geezer now?”

There was no doubt who I was referring to. Hyuk Mujin answered in a lowered voice.

“He’s on the first floor. He’s drinking it up with Young Hero Cheongpung.”

“He is? How long?”

“I don’t know exactly. I only woke up not long ago, but I asked the server earlier. He said it had already been more than three shichen.”

I did not need to focus my internal energy.

My hearing had sharpened by a level when I reached Peak, and it clearly carried the drunken shouting and singing from downstairs to me.

*Look at them, carrying on like they’re having the time of their lives.*

One old man who threw punches before asking a single question, and one idiot who had barged in without reading the room and caused this whole disaster.

I wanted to smash those villains’ heads in with a liquor bottle and shout, “Justice has been served!” But I held myself back.

…To be precise, I had no choice but to hold myself back.

“Phew.”

Being powerless was a sin. A sin.

As I let out a deep sigh, Hyuk Mujin cautiously spoke up.

“Captain.”

“What?”

“I think we should head downstairs soon.”

“Why would I go down there?”

“Great Hero Jeok told me to bring you down as soon as you regained consciousness…”

“Great Hero, my ass. How is that old man a Great Hero?”

“You’d call him Great Hero if you were standing in front of him, too.”

“…”

That was true.

But going downstairs at his command would be no different from jumping straight into a tiger’s mouth.

I began pulling on the clothes draped over the table at the speed of light.

“What are you doing?”

“Getting ready to bolt.”

“What?”

“I said I’m running. What about it? Do you want to come with me?”

Hyuk Mujin grabbed my arm in a panic.

“Why are you running away?”

“I don’t know when that old geezer might lose his temper and burn me to death. If you were me, wouldn’t you want to run?”

“Is this because of what happened earlier?”

“If you mean the Head Elder?”

“Yes. If that’s what you mean, Young Hero Cheongpung and I already…”

I cut him off firmly.

“You must have explained everything ages ago. The misunderstanding should be cleared up by now.”

“Oh, you know?”

“Do you think I’m an idiot?”

I had passed out around noon, so at least half a day had gone by. Even if Jeok Cheongang was a hot-tempered old man, he surely would have investigated the matter and found out the truth.

Cheongpung and Hyuk Mujin must have tried to clear up the misunderstanding as well.

Hyuk Mujin tilted his head.

“Then isn’t everything fine? You have no reason to run.”

Every minute and second was precious.

I quickly rummaged through my clothes, pretending to search them, then pulled out an item from my Inventory and waved it.

“Here. This is the reason.”

**Flame Divine Palm**

After checking the cover of the old martial arts manual, Hyuk Mujin muttered,

“Ah, shii…”

“All right, here’s a question. What exactly is the relationship between Jopil, who possessed the Fire Gate Clan’s Flame Divine Palm manual, and Jeok Cheongang?”

“…”

“You’re starting to get the feeling too, aren’t you? I’d stake my wrist and my entire fortune that they’re master and disciple. What are you willing to bet?”

Hyuk Mujin bet nothing.

Instead, he spread the wings of his desperate imagination, full of dreams and hope.

“W-wait a second. The two of them might not be master and disciple.”

“If they aren’t master and disciple, what are they? Father and son? Considering how foul-tempered they both are, that actually has some merit. Don’t you think?”

“Jopil might have stolen Great Hero Jeok’s belongings.”

I snorted.

I snorted so hard that a booger nearly flew out of my nose.

“Do you think the Fire King is some old man from the neighborhood? Who would steal from that old geezer?”

The Fire King was the man who had killed a thousand Demonic Cultists because they had set fire near his home.

Jopil might have been crazy, but unless he had gotten Botox injected into his liver, he could not even have dreamed of doing such a thing.

After hesitating for a moment, Hyuk Mujin nodded.

“…All right. Let’s say he was his Disciple.”

“I’m telling you, they were definitely master and disciple. And if you aren’t coming, let go of me. I’m busy.”

Hyuk Mujin continued speaking as though he had not heard me.

“Even if Jopil was Great Hero Jeok’s Disciple, we merely did our duty. He was the one who charged at us and tried to kill us first.”

“Right. You and Cheongpung will be safe either way, so tell him that for me. I’m leaving.”

“Captain!”

“Fine, Mujin. Let’s assume that’s true. Let’s also assume that the foul-tempered old man acknowledges his Disciple’s wrongdoing and lets it pass. That could never happen, of course, but let’s assume it does.”

I peeled his hand away from my arm one finger at a time and asked,

“Then we’d have to return what Jopil stole, wouldn’t we?”

Hyuk Mujin nodded vigorously.

“Of course. Do you want to keep it and burn to death?”

“But what do you think would happen if we told him we couldn’t return it?”

“What? Captain, are you perhaps tempted by the Flame Divine Palm…?”

“Am I insane? Living a long and uneventful life is my philosophy. That’s why I even make my dumps thin and long on purpose!”

Under normal circumstances, he would have made a disgusted face and complained about my dirty talk. But now, he merely kept gulping dryly.

“Then what’s the problem?”

“The problem is that Jopil possessed more than just the Flame Divine Palm manual.”

I held up three fingers and began folding them down one by one.

“One: the Flame Divine Palm. Two: the Ten-Thousand-Year Cold Iron sword. And finally, three…”

I folded down the last finger.

“The Blazing Flame Divine Pill.”

Hyuk Mujin had already been gaping at the mention of the Ten-Thousand-Year Cold Iron sword. Now he asked with an uncertain expression,

“…Are you talking about that thing from back then? The one that tremendously boosts your internal energy, but makes your body burn up?”

“Yeah. The one I was planning to give you along with the Flame Divine Palm manual a long time ago.”

“Where is it now? Where is that thing?”

“Mujin.”

I gazed out the window with moist eyes.

To the north, in the direction of the Mount Heng Sword Sect.

“Do you remember when we went to the Mount Heng Sword Sect last time?”

“Why are you suddenly bringing that up?”

“The Red Wind Band Leader was stronger than I expected. How was I supposed to beat a man who had defeated Cheol Mubaek and even Jin Mukyung?”

“H-hold on. Then back then…?”

“Yeah. It worked like a charm.”

I stroked my stomach with the feelings of a woman three weeks pregnant who had just checked a pregnancy test.

“I put it in here. The Blazing Flame Divine Pill.”

“…”

“They say it’s a secret divine elixir of the Fire Gate Clan. If I want to return it, I’ll have to cut open my stomach and drain the blood.”

“…”

“So stop holding me back. I’m casting off every shackle and restraint in this world and setting out to find a way to survive…”

At that moment, Hyuk Mujin moved with unprecedented agility.

“Tap-tap-tap—whoosh!”

Clutching the satchel he always carried, he flung himself through the wide-open window.

In that sight, I saw a bird.

*That bastard.*

How dare he try to escape before me?

And with a satchel containing silver nyang and food, no less?

“Hey, Hyuk Mujin!”

By the time I let out my hushed shout, it was already too late.

Hyuk Mujin glanced back at me with an expression of utter liberation.

Then his body dropped straight down.

“Goddammit.”

I had to get out of there too.

I hurried toward the window and was just about to fling myself outside when—

*Crack! Thud!*

Hyuk Mujin, who had been running away with all his might, suddenly crumpled as though he had been shot.

The object that had struck him squarely in the temple was one I knew all too well.

“…A chicken bone?”

The next moment, an old voice rose from below.

“You stupid fool. Can’t you tell a chicken from a duck?”

Step. Step.

A small shadow swayed beside the lantern at the inn’s entrance.

A wrinkled face suddenly appeared. It looked up at me, my body draped over the window, and grinned.

“Where were you headed?”

After seeing 14,000,605 futures, I arrived at the most appropriate answer.

“To the privy.”

“Do you want to shit blood?”

“No.”

Yeah, I knew that wasn’t going to work.
## Chapter artifact 176

# Chapter 176

I feel like I’ve gone back to high school.

I was running away to avoid evening self-study when the school disciplinarian caught me. Of course, the despair I felt back then was nothing compared to this.

The person holding my ear right now wasn’t a school disciplinarian.

He was the Fire King.

*Crack.*

“Ah! Aaaagh! It hurts! Something just made a weird noise in my ear!”

Jeok Cheongang glared at me.

“Shall I make sure you can never hear another sound?”

“…”

Judging by everything he had said and done so far, he was more than capable of following through.

I clamped my mouth shut and let Jeok Cheongang lead me wherever he wanted.

“Sit.”

“Yes, sir.”

I sat down on a shabby wooden chair and looked around.

The inside of the old, gloomy inn was deserted. I couldn’t see the owner anywhere, and a server who looked barely twenty was sitting at a table near the entrance, nodding off.

*Damn it. There aren’t even any other customers.*

I must have been unconscious for longer than I thought. There were only four people on the first floor.

The dozing server, Jeok Cheongang, me—and Cheongpung, who was already passed out drunk, face-down on the table and drooling.

It was the perfect place to die without a mouse or bird ever knowing.

*No. They say that even if you enter a tiger’s den, you’ll survive as long as you keep your wits about you.*

Even so, I needed some kind of life insurance, just in case.

Unfortunately, the only brake capable of stopping Jeok Cheongang was currently snoring with his face planted on the table.

*Cheongpung, you have to wake up if I’m going to survive this.*

I was carefully stretching my leg beneath the table, preparing to step on Cheongpung’s foot, when—

“Leave him sleeping.”

“Huh?”

“I said leave him alone. Don’t bother someone who’s sleeping for no reason.”

At this point, he was practically a ghost.

I hadn’t made a sound or given away my movement, yet he knew exactly what was happening beneath the table.

“Your answer?”

“…I’ll stay still.”

“You’re not entirely oblivious, I see. You might live a long time.”

Jeok Cheongang muttered something that could have been either praise or an insult, then tilted the liquor bottle.

The empty cup slowly filled with a trickle of liquor, and the cheap scent stung my nose.

“I have something to ask you.”

“I’ll explain everything in detail about the Head Elder—no, my great-uncle.”

“I’ve already heard. He committed more than enough crimes to deserve death. He was a fairly sharp fellow once, but time has ruined a lot of people…”

Jeok Cheongang downed his drink in one gulp and muttered bitterly,

“That child was like that, too.”

“…”

“Where did you meet him?”

It was an unexpected question, but I understood immediately.

The “child” Jeok Cheongang had just mentioned was Jopil.

He already knew that Jopil and I were connected.

The worst possible situation had become reality.

“If you’re thinking of telling a lie, you’d better abandon the idea now. You’ll end up telling the truth anyway.”

Jeok Cheongang’s voice sank like an abyss, sending a shiver down my spine.

There was no point in lying or making excuses anymore. Right now, he was the prosecutor, the defense attorney, and the judge who could hand down any sentence he wanted.

*Damn it.*

My mouth was so dry it tasted bitter. He wasn’t even releasing Scorching Yang Qi, yet my thirst was so severe that I could barely speak.

“Give me a drink, too.”

“You cheeky bastard.”

Despite saying that, Jeok Cheongang obediently filled my cup.

I hurriedly gulped down the strong liquor, and only then could I breathe again.

Right. It wasn’t over yet. The more dangerous the situation, the more carefully I had to think if I wanted to escape it.

I took a deep breath and opened my mouth.

“It was about two months ago. That’s when I met Jopil.”

“Jopil?”

“Yes. One Question, One Kill, Jopil. He was a fairly famous wandering martial artist.”

“Judging by his alias, he probably wasn’t famous for anything good.”

“…That would be accurate.”

Not just accurate. He had been practically insane.

At the time, I had seen Jopil as nothing more or less than a man who was addicted to killing. He genuinely enjoyed it.

“Is this his face?”

Jeok Cheongang pulled a piece of paper from inside his robe.

The paper was extremely old, crumpled all over, and yellowed with age. Even so, the face of the young man drawn on it was easy to recognize.

“Is that Jopil when he was young?”

“It seems it was him after all. So this is what became of him.”

His response sounded more like a monologue than an answer to my question.

After remaining silent for a while, Jeok Cheongang suddenly spoke again.

“More than twenty years ago, a terrible epidemic swept through Anhui Province. Countless commoners died, and even more children were left orphaned. He was one of them.”

The moment Jopil’s true identity—unknown to everyone—was revealed had arrived. Depending on what Jeok Cheongang said next, my future would be decided.

I held my breath and listened.

* * *

Jeok Cheongang continued slowly. As clear liquor rippled in the glass, memories of that time rose vividly to the surface.

“He was a child struggling desperately to survive. Even while a dozen or so people surrounded him and trampled him, he shoved a dirt-covered dumpling into his mouth.”

“…”

“I liked the fierce look in his eyes, and at the same time, I felt sorry for him. I gave him the name Jangcheon, meaning “Vast Sky.””

That was how Jangcheon came to live in a hut deep in Mount Jiuhua.

It was the first time an outsider had set foot there in fifty long years, ever since Jeok Cheongang had seen his Master off.

“At first, he knew nothing. It wasn’t until a year later that he realized I was a martial artist. Soon afterward, he began begging me to teach him martial arts.”

To an orphan with no one in the world, raised amid contempt and hunger, martial artists might as well have lived above the heavens.

The boy wanted to become a martial artist and change his life. That was why he desperately clung to the old man who had saved him.

“Please accept me as your Disciple.”

“No.”

“Master!”

“Master? Who said I was your Master? You lack both the physique and martial talent to learn our sect’s arts.”

“I’ll do it. I’ll prove I can somehow. Even if it kills me, I won’t disappoint you, Master!”

“…Don’t be ridiculous.”

Jeok Cheongang thought Jangcheon wouldn’t last long.

But the boy’s longing was far more tenacious than he had expected. For an entire year, Jangcheon tried to persuade him every single day without fail. Later, he even went so far as to injure himself or starve himself.

Every time he did, Jeok Cheongang was the one who sweated bullets.

“You fool. Why would you do something like this?”

“I want to learn martial arts. Please accept me as your Disciple.”

“…I can’t.”

“Is it because I’m lacking?”

“To continue the sect’s lineage, this is unavoidable. It will be a difficult time for you, too.”

“No matter how hard it is, I can endure it!”

“No. If you insist on being this stubborn, I’ll have no choice but to send you down the mountain. Is that what you want?”

In truth, Jeok Cheongang was the one who didn’t want to part.

Old age had begun to catch up with him, and it seemed he had grown lonely for human company. The past year had been more than enough time for him to grow attached to the wounded, taciturn boy.

But…

“Then do it. I’m going to die sooner or later anyway.”

“What?”

“If I can’t have you as my Master, I’ll kill myself. No—kill me right now. Kill me with the hand that saved me.”

“You little—!”

What was martial arts worth, anyway?

Seeing Jangcheon prepared to throw away his own life over it, Jeok Cheongang felt hurt and furious.

But at the same time, another thought occurred to him.

“Even if his martial talent and physique were lacking, with resolve that fierce, he would surely achieve great success one day. That was what I thought.”

Jin Taekyung, who had been listening quietly, asked with an uneasy expression,

“That kind of resolve… Is that why you accepted him as your Disciple?”

“Yes.”

Jeok Cheongang added with a sigh,

“It was a mistake.”

That was the most painful mistake he had made in all the hundred years since his birth.

“For several years, things went smoothly. He grew so quickly that my concerns from before I accepted him as my Disciple became meaningless.”

Jangcheon faithfully followed his Master’s instructions.

No—that was closer to absolute obedience.

He swung his sword like a madman all day long and devoted himself to training his stamina. Even when learning the smallest, most basic techniques, he poured his entire being into them as though he were practicing the greatest martial art under heaven.

With his Disciple devoting so much passion and effort to his training, Jeok Cheongang couldn’t help but be deeply moved. He also did everything in his power to help Jangcheon grow.

Jangcheon had only slightly more talent and physical aptitude than an ordinary person, but Jeok Cheongang gradually improved his constitution by cleansing his sinews and washing his marrow.

A Master and Disciple who trusted and relied on each other.

Remarkable achievements.

Everything seemed to be falling perfectly into place.

“The problem came after that.”

The old man remained old, but the boy grew into a young man.

Yet compared to his physical growth, the young man’s martial arts failed to progress. Jangcheon grew furious at himself for treading water for years, and at last, something happened.

“I still remember it clearly. I couldn’t sleep that night, so I was sitting on a rock when he came up from below. He hadn’t shown himself for several days, claiming to be in closed-door cultivation.”

Jin Taekyung tilted his head.

“What do you mean, he came up from below?”

“He had gone to the village. The wind carried the musk courtesans use.”

“Oh. A pleasure house?”

“I understood perfectly. He had spent more than ten years learning nothing but martial arts, barely ever leaving the mountain. And the man who called himself his Master couldn’t offer much help and only focused on his own cultivation. What could I say?”

At the time, Jeok Cheongang had been immersed in training to open his upper dantian.

Opening the upper dantian meant entering the Martial Extremity realm. It would raise his martial arts to another level while also treating the old-age illness that was gnawing at him with every passing moment.

“But it wasn’t easy. It required a long period of preparation, time, and enlightenment.”

As a result, the Master and Disciple gradually began seeing less of each other.

Jeok Cheongang believed that his Disciple, who had always worked hard, would gain enlightenment on his own, so he focused on cultivating his upper dantian.

The only time he noticed his Disciple had gone down the mountain was when various smells came mixed in with the wind.

“Then one day, a visitor came.”

“A visitor?”

“The Azure Sky Sword King. I had never seen his face before, but I recognized him immediately. He was exactly as I’d heard.”

Jin Taekyung’s jaw dropped.

“The Azure Sky Sword King? One of the Ten Kings?”

“Yes. He was also the Grand Family Head of the Nangong Family.”

“Why did he come?”

Jeok Cheongang tilted the liquor bottle without a word.

He had already emptied several bottles by himself, but his mind was growing clearer by the moment. The same was true of the words spoken by the Azure Sky Sword King when he appeared without warning.

“These days, the brats in my family have been throwing a fit. There’s some vicious bastard running wild in Anhui, but they say they can’t catch him. They begged me so desperately that I had no choice but to come see you.”

Jeok Cheongang had been bewildered.

The influence the Nangong Family wielded in Anhui was truly immense.

If even their power had proven insufficient, to the point that the Azure Sky Sword King himself had to step in, then just how powerful was this bastard?

“Then why did you come to me? Are you saying this fellow has become a Martial God?”

“If he were a Martial God, he wouldn’t be killing only innocent women and mediocre wandering martial artists. I happened to see him once from a distance, but I let him go.”

“What does that—”

“A Master should correct his Disciple’s mistakes, shouldn’t he?”

Not long after the Azure Sky Sword King left, Jeok Cheongang stood absentmindedly on the rock and caught a scent carried on the wind.

It was the smell of blood.
## Chapter artifact 177

# Chapter 177

*Why hadn't I known?*

It might have been the trust I placed in a Disciple I had raised like my own blood—or it might have been indifference. But there had unquestionably been a scent of blood clinging to Jangcheon when he staggered up the mountain that day.

“Where have you been?”

“Ah, Master.”

His eyes were red from drunkenness—and from something else.

“I went down to the village for a little while. I’ve been feeling restless lately, so I had a drink.”

“Drinking. Was that all?”

“It’s a little embarrassing to say it myself. Hahaha! I’m sorry you had to see me like this.”

The pungent musk courtesans used stung his nose. But that was merely a veil laid over the truth to conceal it.

Jeok Cheongang could smell the faint scent of blood hidden beneath it. It was the smell of death, the smell of a killer—the smell he had forgotten since the Great Faction War.

“You went to a pleasure house…?”

“As expected, I can’t fool you, Master. Yes. This useless Disciple was troubled and sought out women.”

The Disciple he met again after so long had become an entirely different person.

He had gone from a taciturn boy who never smiled to a smooth-talking killer who concealed his murders without the slightest concern.

“But what brings you out at this late hour? Have you made any progress in your closed-door cultivation?”

“…It felt like a long time since I’d seen your face, so I was waiting.”

He had apparently murdered dozens of innocent commoners in horrific ways.

His Disciple had committed a crime that made heaven and earth furious. The right thing to do would have been to sever his Sinews and Meridians and cripple his dantian at once. That was what a Master should do.

But—

“I see. I’m very glad to see you too, Master.”

At Jangcheon’s faint smile, Jeok Cheongang found himself unable to speak. He felt neither anger nor betrayal. Something simply welled up from deep within him and left him choked up.

In the end, there was only one thing he could say.

“It’s late. Go get some rest.”

Jin Taekyung listened to Jeok Cheongang and asked in disbelief,

“Wait. That’s it?”

“I wanted to believe in that child.”

“You already knew everything. You knew Jopil—or rather, Jangcheon—was lying.”

“I knew.”

“And you still let the bastard go?”

“Yes. Even so.”

The old man’s weary voice continued.

“Do you have any blood relatives?”

“Yes.”

“I have none. Even when I recall my earliest memory, I was alone. He was the same.”

Jeok Cheongang looked down at his hands. The hands covered in age spots and wrinkles bore the weight of the years in layer upon layer.

“My Master was a strict man. His training was harsh and painful, but I liked even that when I was young. I was happy that someone cared about me and stayed by my side. My Master was the only person I could rely on.”

But his time with his Master had been short. He was left alone once again, and over the years, his loneliness had slowly dulled.

That was how it had been until he met a child struggling desperately to protect a single dumpling in the marketplace.

“I was the only person that child could rely on. Even if all under heaven pointed fingers at him, I had to believe in him.”

At some point, Jangcheon became more than a Disciple to Jeok Cheongang.

He was his only son and his grandson. Their blood was not connected, but Jeok Cheongang loved him with an affection greater than blood.

“But what that child did was far too horrible. I had to make him stop. Somehow.”

Before that, he wanted to see his Disciple’s atrocities with his own eyes.

The fact that the Azure Sky Sword King had come in person meant that all the circumstantial and physical evidence was already in hand. But that alone was not enough.

“So I began secretly following him.”

From that day on, Jeok Cheongang followed his Disciple. It was easy to avoid Jangcheon’s notice, since he had not yet broken through the wall to the Peak realm.

Once, twice, ten times…

The despair he had felt at first grew fainter with every pursuit.

Jangcheon merely visited pleasure houses, drank, and embraced women like any other wastrel. When he returned to his hut flushed with drink, he resumed his identity as a martial artist and trained diligently.

Everything seemed perfectly normal.

“Then, suddenly, I began to wonder if there had been some mistake. Maybe the Nangong Family and the Azure Sky Sword King had simply misjudged him.”

Jin Taekyung stared at him in disbelief.

“I think you’re the one who misjudged him, Sir Jeok.”

Jeok Cheongang laughed hollowly.

“Yes. I did. Like a fool, I desperately turned away from the truth.”

“So did you confirm it yourself?”

“…”

Jeok Cheongang silently tipped back the bottle and drank straight from it.

The ceiling looked blurry—not because the liquor was strong, but because the memory of that day had risen vividly before his eyes.

* * *

Thud. Thud. Thud.

In a back alley of the red-light district, beneath the thick darkness of night, muffled groans mingled with spurts of blood.

The back of the masked man stabbing and prodding someone’s limbs with a sharp dagger was more familiar than anything—and more foreign than ever.

“…Jangcheon.”

At the quiet call, the hand holding the dagger abruptly froze. The masked man slowly turned his head, and his eyes met Jeok Cheongang’s.

The Disciple’s eyes curved like a crescent moon at the sight of his Master after so long.

“Ah, Master.”

“What… What are you doing?”

“What does it look like? Exactly what you see.”

Jangcheon grinned and drove the dagger down.

Thud. Thud. Thud.

The middle-aged man, his limbs bound, writhed in agony.

“Stop at once!”

“Why should I stop?”

“…W-What did you say?”

“It’s been a long time since I came down here, and all kinds of people are running wild. Wandering martial artists swaggering around because they know a few Third Rate martial arts, merchants with fat bulging from their bodies, and women whose only property they can sell is their own bodies. What a madhouse.”

Jangcheon smiled, showing all his teeth.

“This man is just one of them. What difference does it make if I kill one such person? He’s nothing more than a two-legged beast with no reason to live.”

Everything felt like a dream to Jeok Cheongang. The hope he had held while watching his Disciple for the past four months had already vanished like a bubble.

“Why… Why would you do something like this?”

“Because I’m strong.”

Jangcheon continued in an excited voice.

“Might makes right. Didn’t you teach me that, Master? Murim—or rather, the entire world—is like that. The weak die to the strong.”

“You killed innocent people for that reason?”

“Innocent? How do you know they were innocent, Master?”

“Then what great sin had those you killed committed?”

He had wanted to believe they had deserved death.

He had wanted them to be corrupt merchants who preyed on the blood and sweat of others, or ruffians who committed murder as easily as they ate—not simple commoners who knew nothing of the world and lived like oxen.

But…

“How should I know?”

“…!”

“Who in this world lives without sin? They were merely unlucky. This man who happened to catch my eye was the same.”

Jeok Cheongang felt the world grow distant before him.

The Disciple he loved like his own blood had already crossed a river from which there was no return.

Those who crossed to the other side could never come back. They would live out their entire lives as blood-soaked killing fiends.

“Jangcheon.”

“Yes, Master.”

The face of the emaciated child he had met in the marketplace more than a decade ago overlapped with the face of the blood-soaked young man before him.

“What on earth made you like this?”

“What do you mean?”

“You… You weren’t this kind of child. You say the weak die to the strong? Have you forgotten your past self, struggling desperately just to survive?”

“I haven’t forgotten. That’s why I am who I am now.”

“No. You were kind and diligent…”

“Master.”

Jangcheon cut him off in a gentle voice.

It was the first time the Disciple had ever interrupted or contradicted his Master. But now, even open mockery lingered at the corners of Jangcheon’s mouth.

“I remember the day I first met you very clearly. I had gone hungry for several days and was wandering through the marketplace when I found a dumpling covered in dirt. Even while the others, who were in the same situation as me, trampled me, I forced it into my mouth.”

“That’s right. You did it to survive. Why can’t you remember that you were once weak too?”

The corners of Jangcheon’s mouth twisted.

“Wangpal, Hong Sochil, So U-pyeong.”

“…?”

“They were three of the fifteen who tried to take my dumpling. Unfortunately, the rest were already dead.”

The three names that came from his Disciple’s mouth.

Their meaning was clear. Those three were no longer among the living. And until the moment their breathing stopped, they must have suffered tremendous pain.

“They didn’t remember me, but I never forgot them for a single day. That day, more than a decade ago, as I chewed that dirt-covered dumpling, I realized something. This is what the world is. The weak are trampled, and the strong do the trampling. So I must become strong. I must enjoy the rights of the strong.”

As Jangcheon spoke of the vow he had made that day in a bleak voice, Jeok Cheongang understood.

“You… You…”

“Yes. I never changed. Not once, from the day I first met you until now.”

His white teeth appeared in the darkness. Jangcheon was giggling.

“It was thrilling. At first, they begged me to let them live, but later they wailed for me to kill them. When they finally went quiet, I felt empty inside. Even after drinking myself senseless at a pleasure house and embracing a woman, I couldn’t get rid of that feeling.”

He was a born Slaughter Saint.

The only way to fill that emptiness was murder. Jangcheon would probably never stop killing until the moment his breath left his body.

“The timing was perfect. You happened to be so absorbed in your training that you neglected me, and thanks to that, I could run wild to my heart’s content.”

Jeok Cheongang wanted to cover his ears. He wanted to cover his ears, close his eyes, and erase the memory of that day, which had been branded into his mind.

His body trembled with betrayal and fury toward the Disciple he had raised with the affection of a blood relative.

But what tormented him most was the affection for his Disciple that still remained.

“Of course, it wasn’t as though I felt at ease either. Was it four months ago? I returned after taking care of some business and found you waiting for me. When I saw how different you were from usual, I realized I had been found out.”

“Stop.”

“There was no way you would suddenly follow me when you trusted me so completely, so someone must have tipped you off… Ah, it was obviously the Nangong Family.”

“I said shut up!”

A powerful wave of qi swept through the alley.

At the sight of his Master’s fury—something he had never seen before—Jangcheon’s eyes widened.

“Master?”

“You bastard! How dare you call me Master with that mouth? Have you still not realized what you’ve done?”

“Why are you acting like this? Surely you don’t intend to throw away your only Disciple over something this minor?”

“Minor? Did you just call this minor?”

“Master, you’re like a father to me. I believed that even if everyone under heaven cursed my faults, you would understand. Because you’re my father.”

Father.

It was the word Jeok Cheongang had wanted to hear so desperately.

He gritted his teeth.

“You’re wrong.”

“Wrong?”

Jangcheon smiled faintly.

“Then why don’t you strike me dead right now? You had countless chances, both now and throughout the past four months.”

“That’s—”

“Am I wrong?”

Jeok Cheongang was unable to speak. Everything Jangcheon had said was true. He had deliberately turned away from the truth and tried to justify it.

Because he wanted to believe in his Disciple, even if it took that.

Only after a long time did he finally open his mouth.

“I’ll sever your Sinews and Meridians.”

“My Sinews and Meridians. And then?”

“I’ll cripple your dantian. You’ll spend the rest of your life repenting for the crimes you committed.”

“Face-the-wall meditation until I die. That sounds terrifying.”

Despite his words, Jangcheon’s face was full of laughter.

“But did our sect’s rules happen to change while this useless Disciple was looking the other way? As I understand it, a case like this calls for immediate execution without further examination.”

“…This is my final mercy. Put that man down at once and step away.”

Jangcheon blinked as though he had forgotten something important.

In his arms, the middle-aged man—his entire body drenched in blood—was still struggling to breathe.

“Oh, right. This fellow was here.”

Slash.

A fountain of blood burst into the air.

Jeok Cheongang watched it with trembling eyes.

There had not been even a moment’s hesitation in Jangcheon’s hand. The man’s throat had been cut. He shuddered violently, then breathed his last.

“Is this your answer?”

“It’s already too late. Even if I saved him, he would spend the rest of his life crippled. Wouldn’t it be better to give him a clean death?”

“You… You’re no longer the child I knew.”

“I am exactly the child you knew, Master. You simply misunderstood me from the beginning.”

“Enough. Your evil deeds end today.”

“Do you really intend to cripple me and make me spend the rest of my life facing a wall?”

There was a faint trace of fear on his Disciple’s face.

Jeok Cheongang clenched his fist until blood seeped from his palm. One move—just one move—and he could erase Jangcheon from this world.

But he knew he could not bring himself to do it.

Severing his Disciple’s Sinews and Meridians, crippling his martial arts, and imprisoning him was the best he could do.

“Do you regret it?”

“Regret?”

“Yes. Regret.”

Nothing would change, but he wanted to hear the answer from Jangcheon’s own lips.

Yet in the next moment, all traces of fear vanished from Jangcheon’s face.

“I was relieved.”

“What?”

“I couldn’t see or hear you, but I knew you had been watching me for the past four months. Why else would I have done this right in front of your eyes?”

Jangcheon’s face was reflected in Jeok Cheongang’s vacant eyes. He continued speaking with a relaxed expression.

“You can’t kill me, Master. It wouldn’t matter if I killed not dozens but hundreds. Before I left, I wanted to confirm that one last time.”

“Before you leave? What are you talking about?”

“There may be fathers who blame their children for their faults, but there is no father anywhere in this world who kills his own child with his own hands.”

“…!”

“Thank you, Master. Thank you for raising me as your child rather than your Disciple. Thank you for trying to keep a child like me alive until the very end. Thanks to you, a single path to survival has opened for me.”

As Jeok Cheongang stood frozen, as though his breath had stopped, Jangcheon gave him a deep, sincere bow.

When he raised his head again, a small white porcelain vial was held between his lips.

“It’s Bone-Melting Powder.”

Bone-Melting Powder was a deadly poison that dissolved flesh and bone.

Even a tiny amount would be fatal if the vial shattered inside his mouth. Not even a celestial immortal could save him.

Jeok Cheongang let out a furious roar.

“Jangcheon! You bastard!”

“That bow I just gave you… was my final farewell. I’m leaving now. I’ll go far away and never return.”

“You think I’ll let you leave like this?”

“Then kill me. That’s the only way.”

“…!”

“Kill me.”

*Kill me.*

Those were his Disciple’s final words.

* * *

Jeok Cheongang blinked. The ceiling had seemed blurry for a while, but now something was running down his cheek.

“The inn is old. Rain must be leaking through.”

It had been the night before New Year’s Day.
## Chapter artifact 178

# Chapter 178

“The inn is old. Rain’s leaking in.”

I stared at the innocent ceiling.

“It is a little old here.”

Of course, no rain was falling, and the ink-dark sky was perfectly still.

It wasn’t the inn that was old. It was Jeok Cheongang’s heart. Remembering the painful memories of long ago had made rain leak from his eyes.

*I thought the old man had no blood or tears in him.*

Fire King Jeok Cheongang.

I had never imagined that this irascible Supreme Peak master had a past like this. I also had to revise my assessment of Jopil, whom I had thought was merely a madman.

*He was crazier than I could have imagined.*

He had thoroughly used and discarded the Master who had saved him when he was on the verge of death. From what I had heard, it was clear that he hadn’t felt even a shred of guilt until the very end.

I was shocked that someone could be filled with such pure malice—and relieved that Jopil no longer existed in this world.

“But he somehow managed to survive and escape. The Nangong Family must have been watching him closely, too.”

The Nangong Family—a staple of martial arts novels.

They were one of the Five Great Families of the world, said to rival the Nine Sects and One Gang. As far as I could tell, catching and killing a single fugitive would have been nothing to them.

Unless someone had helped him.

“Could it be…?”

At my question, Jeok Cheongang calmly nodded.

“I went to the Azure Sky Sword King and asked him for help. It was the last duty I could perform.”

The Disciple had abandoned his Master and left, but the Master had protected that Disciple to the very end.

The more I heard, the more unbelievable their Master-Disciple relationship became.

“…That’s incredible.”

“Incredible? Me? I raised a Slaughter Saint like him as my Disciple, then let him loose upon the world because I was blinded by personal affection. That was a foolish choice.”

Jeok Cheongang continued with a self-deprecating laugh.

“The Azure Sky Sword King told me the same thing. He said I would regret it. He was right. Every moment of the past ten years was filled with regret.”

“If you could go back to that day, what would you do?”

There was no hesitation in his answer.

“I would save him. And I would regret it all over again. Even if I had a hundred chances, the me back then would have done the same.”

*The me back then would have done the same?*

It was a significant choice of words. It also meant that the Jeok Cheongang of today was different.

*Could it be…?*

I wondered if those ten years had been a period of preparation in his own way.

Mental preparation to personally kill the Disciple who might still be committing evil somewhere in the world.

*If that was the case…*

A thought suddenly flashed through my mind, and I asked very carefully—extremely carefully.

“Um.”

“Speak.”

Jeok Cheongang’s voice was low. His deep gaze seemed to see through everything, and my heart pounded.

I swallowed and opened my mouth.

“I believe there’s something you want to ask me.”

We weren’t sitting face-to-face to reminisce about old memories.

He had questions for me, and I had questions for him.

We had things to ask and answer each other. And I wasn’t the one holding the sword hilt.

“I’ll answer. Anything.”

“…”

The one holding the sword hilt, Jeok Cheongang, silently ran his fingers over the empty wineglass.

It was a silence with no end in sight. A quarter of an hour? The time it took to eat a meal? Or half a shichen? I had no idea how much time passed.

A cold wind howled outside, but perhaps because of the tension, my entire body was drenched in sweat.

At last, the long silence was broken.

“…Is he dead?”

His voice was terribly hoarse. He was trying hard to sound calm, but the question was tangled with numerous emotions.

When I nodded, the old man’s gray eyes trembled.

“So he is. In the end, that’s how it turned out.”

Jeok Cheongang unconsciously tried to tip back his wineglass, then noticed that it was empty and gave a hollow laugh.

“I had some idea. I sensed traces of our sect in you.”

It was because of the internal energy I had gained from the Blazing Flame Divine Pill. Just as I had guessed that Jeok Cheongang was the Fire King through his internal energy, he had done the same with me.

“Did he die peacefully?”

“That…”

The image of Jopil struggling as blood poured from his seven apertures came to mind.

After drawing on even his innate qi, he had fought me to the death before half his upper body was blown away and he died.

When I hesitated to answer, Jeok Cheongang waved his wrinkled hand.

“Enough. It was my fault for asking something pointless. Where is there a peaceful death in a battle between martial artists?”

“His suffering would have been brief.”

“A fellow who spent his entire life giving countless people nothing but pain. A death like that was more than he deserved.”

His face was bitter despite his words.

If Jeok Cheongang had encountered Jopil, he would have used the best move available to him.

He would have given him the swiftest and most painless death possible.

*Maybe that was why he had returned to the world.*

But Jeok Cheongang’s goal had not been fulfilled. Jopil encountered me before his former Master could reach him, and lost his life.

I wondered how Jeok Cheongang would react—

“I owe you a debt.”

“Pardon?”

“Did you not hear me? I said I owe you.”

“No, I heard you.”

I was just dumbfounded.

I truly had never imagined that such words would come out so easily and simply.

As I blinked at him, wondering what on earth was going on, Jeok Cheongang continued.

“Someone had to stop that child. You did in my stead what I should have done ten years ago. And…”

Suddenly, Jeok Cheongang’s lips twitched, as if he were someone saying such a thing for the first time.

After hesitating briefly, he finally spoke.

“I’m sorry. I sincerely apologize to all of you for my rash actions the other day.”

The words burst out of me before I could stop them.

“Whoa.”

“Whoa?”

“Ah, nothing. I was just so surprised that it slipped out.”

“Is it really so surprising for this old man to apologize?”

It seemed surprising enough to me. And he looked incredibly uncomfortable himself, so what was he complaining about?

“…Well, you see…”

I let my words trail off awkwardly, but when I saw Jeok Cheongang’s face twist, I quickly changed my tune.

“The famous Fire King Jeok Cheongang, Great Hero, personally apologizing to a much younger junior like me! I can only bow before your broad-minded nature and humility.”

“…”

“…”

Look at his face. It was a full-blown battle between Jekyll and Hyde.

Jeok Cheongang expressed his intense inner conflict over whether to hit me through every muscle in his face. Eventually, he sighed.

“You’re an utterly unreadable fellow. You may leave now.”

“Yes, sir.”

“And take those children with you, too.”

Cheongpung was fast asleep with his forehead pressed against the table, and Hyuk Mujin was still sprawled facedown in the courtyard.

Before Jeok Cheongang could change his mind, I quickly rounded up the two deadweights and headed for the second floor. Then I remembered something I had forgotten.

*Oh, right. I have to return the Flame Divine Palm martial arts manual and the sword.*

I had already swallowed the Blazing Flame Divine Pill, so there was nothing I could do about that, but I needed to return the remaining items.

I desperately wanted to put things between Jeok Cheongang and me to rest after today.

“Um, Sir Jeok. I’m sorry, but there’s one more thing I need to say…”

I turned around with a voice as tiny as an ant’s, then stopped short.

*Glug, glug.*

Left alone, Jeok Cheongang was pouring wine.

One glass, then a second. He set a wineglass down at the empty seat across from him and began drinking in silence.

I stared at him for a while, then suddenly thought:

*He looks small.*

The back of the giant called the Fire King looked small and lonely, and I quietly turned away and climbed the stairs.

* * *

When the presence behind him disappeared, Jeok Cheongang muttered,

“You deserved to die.”

He had killed dozens in Anhui alone. There was no way to guess how many people had fallen victim to his Disciple’s hand over the past ten years.

“You called it Might Makes Right, didn’t you? You’re the same. In the end, you died at the hands of someone stronger than you.”

There was no one who remained strong forever, nor anyone who remained weak forever.

Even Jeok Cheongang, a Supreme Peak master, was the weaker party to someone.

Yet people occasionally forgot that fact. Drunk on their own strength—or on blood—they strayed down the wrong path.

“What a pathetic fool.”

Jeok Cheongang drained his drink. It was as if his Disciple’s words from that distant day were echoing in his ears.

*I have never changed. Not once, from the day I first met you until now.*

He had turned those words over countless times during the past ten years. That single sentence had lodged like a dagger near his heart and tormented him.

“Are you saying you truly never changed? Not even once?”

They had spent a long time together. At times, he had been a strict teacher, and at others, he had cared for his Disciple like a loving father.

No—he had believed that was what he had been.

But all of it had been an illusion. If it had truly been so, Jangcheon would have chosen a very different path.

“How could drawing paper be black from the beginning?”

Coming into this world was like being handed a sheet of drawing paper.

The countless moments a person passed through from birth to death.

When death finally arrived, a painting filled with all those moments was complete. The painting Jangcheon had drawn was… entirely ink-black.

Jeok Cheongang had watched it from the closest distance, yet he hadn’t known.

“Cheon.”

The old man stared at the seat opposite him, where a wineglass had been set. One after another, visions like phantoms appeared in the empty space.

A child hunched over and stuffing dumplings into his mouth. A boy gripping the wooden sword his Master had made for him, his cheeks flushed bright red.

His arms and legs grew longer, and his gaze sharpened. Before long, a tall young man was glaring at the old man.

*Kill me.*

That day, Jeok Cheongang could not answer his Disciple’s sharp words.

But if he ever met his Disciple again, there was something he wanted to say more than anything.

“I’m sorry. I’m sorry.”

Whoooosh.

A cold wind slipped through the door of the old inn and brushed across the wineglass.

* * *

“Benefactor!”

I woke to a terrible racket. Cheongpung, who seemed unusually excited, was bouncing up and down.

“This is my pavilion, so why… Ah.”

Right. This wasn’t the Jin Family of Taiyuan. It was an inn.

At the same time, yesterday’s events flashed through my mind like a panorama. It wouldn’t be an exaggeration to say that I had crossed the boundary between life and death.

But that aside—

“Stop jumping around. There’s already enough dust in here.”

“Today, I’m allowed to jump!”

Could anyone sleep with him making such a racket?

Hyuk Mujin, who had been sleeping curled up on the floor in a corner like a shrimp, also opened his eyes blearily.

“Is this… paradise?”

That guy started talking nonsense the moment he opened his eyes.

It was absurd, but then I remembered that yesterday, while trying to run away on his own, he had been knocked unconscious by a duck bone Jeok Cheongang threw at him.

“You’re awake?”

“Captain?”

Hyuk Mujin’s eyes widened when he saw me, and he sighed.

“So this isn’t paradise.”

“…What the hell is that supposed to mean, you bastard?”

“I’m joking. Joking. I’m just glad to see you alive again.”

“Says the guy who tried to run away on his own.”

“Come on. Why do you keep putting it like that?”

Hyuk Mujin grinned and looked around. More precisely, he looked at Cheongpung, who was running through the room like a train.

“What’s all this commotion so early in the morning? What good thing happened to make him run around like that?”

“Don’t know. He says he’s allowed to jump today.”

“He must’ve eaten something tasty.”

“…”

It was unquestionably bullshit, but when Cheongpung was the one in question, its credibility skyrocketed.

With a doubtful look, I asked Cheongpung,

“What day is it today?”

Cheongpung, who had been circling the room and driving me crazy, suddenly stopped.

“Benefactor, you don’t know even that?”

“…Let’s refrain from remarks like that. Hearing it from you deals ten times the damage.”

“It’s the first day of the new year. New Year’s Day!”

Hyuk Mujin and I nodded at the same time.

“Ah, so it was New Year’s Day.”

“Right. It’s already New Year’s Day.”

“I thought it was something els—”

“Yeah. It’s already been a yea—”

After a brief silence, a great realization came over us.

*Ah. The Jin Family of Taiyuan.*

At that moment, Wipeng’s threat from before I left the family rang vividly in my ears.
## Chapter artifact 179

# Chapter 179

It really was New Year’s Day.

It had only been two days since Wipeng had given me strict instructions before I left the Jin Family of Taiyuan, yet I had completely forgotten about them.

Hyuk Mujin swallowed a hollow breath and spoke.

“W-What do we do?”

“What do you mean, what do we do? Even if we’d remembered, we wouldn’t have made it back in time.”

And it wasn’t just anyone. It was the Fire King.

Considering the atmosphere yesterday, if I’d told him I had family business to attend to and needed to leave, he would have sent me off with a hearty laugh.

Of course, he would have sent me off on the road to the underworld.

“Great Hero Wipeng is going to kill me.”

I patted Hyuk Mujin’s shoulder as his complexion turned ashen.

“Don’t worry. He can’t kill me.”

“Oh, me neither!”

“…”

This was the sorrow of having no one powerful backing you.

Still, I had no intention of deliberately delaying our departure.

It was the day the Jin Family of Taiyuan would rise as the undisputed ruler of Shanxi Province. How could the youngest son of the family show up late?

“Pack your things. We’re leaving right now.”

Not that I had much to pack. I had one travel bundle, and that was it.

We finished preparing in an instant and went down to the first floor. The inn had been decorated entirely in red to celebrate New Year’s Day, and despite the early hour, it was bustling with people.

Among them, two men stood out in particular.

“Oh, you’re up?”

“Tsk, tsk. What’s the world coming to when young fellows sleep this much?”

“That’s what I’m saying. When I was young, there were countless days when I couldn’t sleep for even one shichen.”

“Only one shichen? Back in my day…”

The two old men raised their hands in greeting, then went right back to passing wine cups between themselves.

Their flushed faces and the wine jar beside them were proof that they had already been drinking heavily since morning.

Hyuk Mujin, following behind me, whispered in a small voice,

“What kind of combination is that?”

“I don’t know either.”

One was a huge old man whose body was larger than that of most strapping young men. The other had such a small, frail frame that a breath might have blown him away.

The Fire King was one thing.

*But when did Jang Taebo get here?*

Had he come because of the commission?

In any case, the two old men—each a master in his own field—looked as though they had become quite close at some point.

“The atmosphere’s kind of chaotic. Can’t we just slip out?”

“Slip out, my ass. Don’t you remember getting knocked unconscious with a duck bone yesterday?”

“That was a duck bone? Damn, no wonder my skull was ringing.”

“If we pretend nothing happened and leave, he’ll crack your skull open.”

“I’d rather avoid that.”

“What do you say? Want to run?”

Hyuk Mujin let out a gloomy sigh.

“Phew. What a rotten way to start the new year.”

I agreed wholeheartedly. There wasn’t a single person in the world who wanted to meet Fire King Jeok Cheongang first thing on New Year’s Day.

“Grandpas, do you have any dumplings?”

“There’s plenty of meat, too. Eat.”

“Yaaay!”

…Except for that guy.

Hyuk Mujin and I walked forward with heavy hearts, like oxen being dragged to the slaughterhouse.

Cheongpung, who had been shoveling food into his mouth at the speed of light, beamed as he held out several plates.

“Hewe! It’s delishush! Try shome!”

“…You eat plenty.”

“Thanksh, I will!”

The fact that someone like him was a Peak master was proof that reality was unfair. I couldn’t contain my anguish over the future of the Murim.

Jang Taebo spoke to me.

“So, what are you two planning to do now?”

“We’re thinking of returning to our family first. We have some business to take care of.”

“Ah, I see. You said there was going to be a gathering at the Jin Family of Taiyuan?”

At present, every move the Jin Family of Taiyuan made within Shanxi Province was a hot topic.

The Jin Family of Taiyuan, once treated as an old tiger past its prime, had reclaimed the throne of Shanxi Murim after many years. It was only natural that the interest and expectations surrounding them were extraordinary.

Even Jang Taebo, who spent his days living as a homebody in a small village like Jang Family Village, had heard about it.

“Whenever people gather these days, that’s all they talk about. Even ordinary people with no connection to the Murim are flocking there just to see the spectacle. That tells you everything.”

“Surely that many people won’t come.”

“A grand feast always attracts all sorts of riffraff. Shanxi Province may be a frontier region, but this is the seat where one becomes the hegemon of an entire province. I may not be a martial artist, but I have enough worldly experience to know. Just wait and see. Ah, and…”

Jang Taebo lowered his voice and added,

“Don’t worry about the commission.”

The commission. Hearing that word reminded me of something.

It was something I hadn’t had the time to ask about back then.

“By the way, is there anything else you need?”

“What do you mean?”

“Anything at all.”

Even the neighborhood laundromat charged a fee for repairs. Jang Taebo was a master artisan renowned throughout the world. He might not have been as skilled as he was in his prime, but I didn’t believe his abilities had vanished over the past ten years.

There had to be a proper price for his work…

Realizing what I meant, Jang Taebo stroked his white beard.

“You mean you want to pay me? Something like that?”

“To be honest, I can’t give you as much as you might be expecting.”

“Then just give me ten thousand nyang.”

Ten thousand nyang was a hundred silver nyang. It was certainly an enormous sum, but considering his fame, it felt like nothing more than a special discount.

I nodded readily. It wasn’t my money, anyway.

“I’ll prepare it and send it to your home.”

“Ten thousand silver nyang? You’d have to pull up every last pillar of the Jin Family of Taiyuan.”

“…Ten thousand silver nyang?”

“Of course. Did my worth look that cheap to you?”

“Then that’s a whopping million nyang.”

“Not a whopping million nyang. A mere million nyang. You can obtain the greatest divine weapon under heaven with that much. Is a little money really so important?”

“…”

Of course it was.

How much would a million nyang be worth in the real world? Hundreds of billions? Or would it be in the trillions?

Jang Taebo chuckled when he saw my expression.

“I don’t need it.”

“I’m sorry, but could we make a quick deal for ten thousand nyang—pardon?”

“I said I don’t need it. What would I do with the money? I wouldn’t be able to spend it all before I died. The fact that I was given an opportunity like this while I’m still alive is enough.”

Was this what a true artisan’s spirit looked like?

What a shining example, this Jang Taebo. Every blacksmith under heaven should follow his example and Taebo accordingly.

Just as I was trembling with emotion, Hyuk Mujin cut in with an admiring expression.

“Then why don’t you take the ten thousand nyang for now and give it to me?”

That bastard could probably write an autobiography. He could call it *A Hundred Ways to Get Yourself Beaten to Death*.

I smacked him on the back of the head, then bowed politely to Jang Taebo.

“Then I’ll leave it in your hands.”

“I’m the one who should be asking a favor. I can’t promise how long it will take, but I’ll definitely produce something that will make the world tremble. So until then, make sure you acquire the strength and qualifications worthy of it.”

“I’ll do my best.”

“Good. Then that settles it. I have no choice but to trust you.”

Jang Taebo nodded, then suddenly stopped.

“Ah. And could I ask one more favor?”

“…?”

“Build my house again. It all burned down, and I don’t even have anywhere to sleep.”

The house Jang Taebo had purchased after retiring—a precious space where he had enjoyed a peaceful old age—had vanished overnight.

At his sorrowful voice, my eyes instinctively shifted to the side. Jeok Cheongang, who had been quietly tipping back his wine cup while we talked, raised his eyes.

“What are you looking at?”

The emotional, serious Jeok Cheongang from last night was nowhere to be seen. I subtly averted my gaze.

“…Nothing.”

“If you have something to say, say it. This old man isn’t that petty.”

“Are you really sure?”

“Go on.”

The moment he finished speaking, the space beneath the table began to heat up.

It wasn’t as though the innkeeper were a modern man who had brought in an electric heater…

*Fuck. Flame Divine Palm.*

I answered with tears in my eyes.

“I was just thinking that you looked a good ten years younger than usual today.”

Jeok Cheongang frowned.

“What did you say? Ten years?”

Damn it. If you took ten years off a hundred, he was still ninety.

I hurriedly changed my answer.

“Twenty years…”

“Twenty years?”

“Thirty years…”

In barely three seconds, Jeok Cheongang had grown thirty years younger. He nodded in satisfaction.

“I thought you were a fellow with nothing but shit in your head, but you do have some fairly plausible thoughts after all.”

“…”

Hyuk Mujin looked as though he had something to say, but he firmly kept his mouth shut.

Apparently, he had no desire to make *A Hundred Ways to Get Yourself Beaten to Death* his final work.

Instead, he kept poking me in the side, looking desperate to leave this place immediately.

*Of course, I feel the same way.*

But first, there was one thing I needed to finish.

I opened my mouth in the most polite tone I could manage.

“I have several items in my possession.”

Jeok Cheongang, who had been tilting his wine cup with his flushed face, gave a quiet laugh.

“Did you ever intend to return them?”

“Of course I did.”

“That’s right. If you don’t return them, you’ll see something ugly.”

“…”

The old man could see straight through people’s hearts like a ghost.

I forced a smile and placed the items I had already taken out on the table.

The Flame Divine Palm martial arts manual I had obtained from Jopil. And the Unnamed Sword made of Ten-Thousand-Year Cold Iron.

“Although you already know this, Sir Jeok, the Blazing Flame Divine Pill…”

“You swallowed the damn thing.”

“Yes. That’s right.”

“But…”

His wrinkled finger tapped against the table. Jeok Cheongang’s dry voice continued.

“Where is the treasured jade?”

“Pardon?”

“The treasured jade. The jade.”

The jade? A treasure, a gemstone—something like that?

Jeok Cheongang didn’t seem like the type to fixate on ordinary jewels, so it was clearly something extremely important.

But since I had never even known the jade existed, I could only stare at him in bewilderment.

“These are the only things I received.”

“Received? You mean you didn’t collect them yourself?”

“No. There were circumstances. I was handed them right after I woke up.”

“Is there anyone among them you suspect?”

The people who had handed Jopil’s belongings over to me were Gong Yacheong and Socheon. Neither of them was the sort to quietly pocket something behind everyone else’s back.

The members of the reconnaissance squad who had been there were the same. I didn’t know what had happened, but my trust in them remained unchanged.

“They wouldn’t have. No, absolutely not.”

Jeok Cheongang stared at me for a moment before speaking.

“It must be one of two things. Someone deceived you, or that child lost it.”

“…”

“This has become troublesome. What a nuisance.”

The reason Jeok Cheongang had returned to the world was probably not only to find his Disciple. He also wanted to recover the treasures of the Fire Gate Clan that had been scattered because of him.

The jade he was talking about seemed to be one of them.

It was a treasure that even the Fire King was willing to endure the trouble of searching for at all costs.

*Damn it. I never even got to see it.*

Just as a creeping sense of danger began to outweigh my curiosity about what the jade actually was, Jeok Cheongang spoke.

“It can’t be helped. For now, keep it in your possession.”

That single offhand remark brought my thoughts to a halt.

In other words…

“You want me to keep these?”

“Yes.”

“Both of them?”

“There are three. Did you forget the one in your stomach? Anything originating from our sect will be reclaimed. One way or another.”

“...!”

“I’m joking.”

“Phew.”

“Tsk, tsk. You’re young, but your nerve is already the size of a bean.”

Whether my nerve was the size of a bean or a cannonball, it didn’t matter.

I wanted nothing to do with being entangled with that terrifying old man ever again.

I took a deep breath and opened my mouth.

“I’m sorry, but I’ll have to decline—”

“If you refuse, I’ll reclaim them right now. All three.”

“…”

“This time, I’m serious.”

Once again, the space beneath the table grew scorching hot. There was no need to guess which technique it was.

*What the fuck?*

I was trying to return the items to their rightful owner. And I couldn’t even do that?

Overcome by indignation and a sense of injustice, I asked,

“Why are you doing this to me?”

“Do you expect an old man like me to carry those cumbersome things around? I don’t have the strength for that.”

“What if someone steals them from me?”

“Then you’ll die by this old man’s hand.”

“What if I learn the martial art?”

“Then you’ll die even more painfully.”

What kind of bullshit situation was this?

While I stood there dumbfounded, the Fire King rose from his seat.

Cheongpung, who was still stuffing food into his mouth, looked up.

“Gwandpa, awe you leaving?”

“…You’re worse than your grandfather. Eat slowly.”

After exchanging a silent glance of farewell with Jang Taebo, Jeok Cheongang turned away and tossed out one meaningful remark.

“Let’s meet again soon.”

I didn’t want to see him.

Ever.

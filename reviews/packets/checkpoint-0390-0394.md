# Checkpoint Review — 390–394

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

# Chapters 390–394

## Plot

Jin Taekyung’s western-front force destroys more than a thousand monsters with minimal casualties while the following army removes corpses and rescues civilians. After reserve Hunters diverted by General Liao are massacred in a ruined city by a black knight and ten Death Knights, Jin arrives too late; the Unexpected Assault is canceled, costing him 10 Strength. He prevents Shao Shen from killing Liao, then breaks Liao’s arms and crushes his kneecaps after Liao admits the operation was intended to succeed.

The Arch Lich orders the undead legions to withdraw and lure the human army deeper into the battlefield, revealing that it serves an unknown true king. Monster armies subsequently retreat from every Sichuan front except the deeply penetrated western front. Faye Chen condemns Wu Heixing for abandoning his post, while Wu, increasingly resentful and frightened of Jin, begins considering how to eliminate him after recalling Lee Jungryong’s proposal. Team Leader Choi manipulates rumors and pays soldiers to protect Jin’s reputation after the attack on Liao. Magic Johnson then reports that a military conference has been called in Chengdu and prepares to withdraw personnel from the southern front.

## Continuity

- Jin is Level 121, has crossed into true mastery, retains the Undead Hunter Title, and keeps the strengthened Skeleton Warlord, Bones, in his Inventory.
- **The Desperate War Situation** remains active. **Unexpected Assault** was canceled when its target disappeared; its failure reduced Jin’s Strength by 10.
- The Skeleton Warlord cannot raise undead deep inside the battlefield because the Arch Lich’s control is stronger there.
- Zhang Wei’s company and many of Shao Shen’s Hunters were massacred in the ruined city. The black knight spared a hidden family with a child and withdrew with ten Death Knights.
- Shao Shen survived Jin’s Paralysis, Mute, and Sleep Acupoint strikes and still seeks revenge against General Liao. Jin’s assault on Liao risks political consequences because Liao is a senior Central Military Commission general and Crown Prince Party member.
- The Arch Lich remains weakened, serves an unidentified true king, and has ordered the black knight and undead legions to withdraw and draw human forces inward.
- Monster armies withdrew overnight from every Sichuan front except the western front, where Jin’s force remains deeply advanced.
- Faye Chen remains hostile toward Wu Heixing after his abandonment of the eastern-western command area. Wu intends to act against Jin after recalling his conversation with Lee Jungryong.
- Team Leader Choi has engineered favorable public rumors about Jin’s confrontation with Liao.
- Magic Johnson commands the southern front, has temporarily withdrawn personnel for the Chengdu conference, and remains strongly flirtatious toward Team Leader Choi.
- Lei Fei, his missing unit, and the Second Fiend assigned to Qingcheng remain unresolved.

## Translation Decisions

- Retain **Arch Lich**, **black knight**, **Death Knight**, **warhorse**, **Bones**, **Sudden Quest**, **Unexpected Assault**, **Strength**, **Paralysis Acupoint**, **Mute Acupoint**, **Sleep Acupoint**, and **high-grade potion**.
- Use **Jin Taekyung**, **Shao Shen**, **General Liao**, **Zhang Wei**, **Faye Chen**, **Wu Heixing**, **Lee Jungryong**, **Team Leader Choi**, **Magic Johnson**, and **Michael Johnson**.
- Use **Public Security Armed Forces Department**, **13th Group Army**, **Regimental Commander**, **company commander**, **Crown Prince Party**, and **martial law**.
- Render **형님** as **hyung** when Shao Shen addresses Jin and preserve Team Leader Choi’s formal **Mr. Jin**.
- Preserve the established **Lord Fuck/Lord Fuuuck** wordplay, Jin’s crude humor, and the hostile, profane tone of Faye’s confrontation with Wu.

## Durable state

{
  "active_continuity": [
    "Jin Taekyung is Level 121, has the Undead Hunter Title, and keeps the strengthened Skeleton Warlord in his Inventory under the mocking name Bones.",
    "Jin has crossed the wall into true mastery and can use overwhelming physical force without internal energy when he restrains himself.",
    "The Arch Lich's three incomplete Liches were destroyed at Chengdu International Airport, and their testimony identified the Arch Lich as responsible for the undead army's actions.",
    "The Skeleton Warlord cannot raise undead deeper inside the current battlefield because the Arch Lich's control grows stronger there.",
    "Sichuan Province remains under martial law amid a Monster Wave exceeding 100,000 monsters, at least 300,000 initial casualties, magical communications interference, and a large undead army.",
    "The Sudden Quest The Desperate War Situation remains active, while the Unexpected Assault was canceled and its failure cost Jin 10 Strength.",
    "The Arch Lich remains weaker than its former self, serves a separate true king, and has ordered the black knight to withdraw the undead legions.",
    "Monster armies withdrew overnight from every front in Sichuan Province except the western front, which remains deeply penetrated because of Jin's advance.",
    "The western-front force suffered a major massacre near the city, Wei Fenghu remains China's Minister of National Defense, and Lei Fei remains missing with his unit.",
    "Faye Chen remains hostile toward Wu Heixing, while Wu Heixing intends to act against Jin after recalling his conversation with Lee Jungryong.",
    "Team Leader Choi has engineered favorable rumors about Jin's confrontation with General Liao by paying soldiers and leveraging existing hostility toward Liao.",
    "Magic Johnson commands the southern front, has temporarily withdrawn personnel for a military conference in Chengdu, and has a strongly flirtatious interest in Team Leader Choi."
  ],
  "continuity_sources": [
    394,
    393
  ],
  "open_questions": [
    "Who is the Arch Lich's true king, who is the black knight, and why did the undead legions withdraw now?",
    "What happened to Lei Fei and the Hunters who disappeared with him?",
    "What happened to the Second Fiend assigned to the Qingcheng attack?",
    "What is Wu Heixing planning after recalling his conversation with Lee Jungryong?",
    "What does Shao Shen know about the consequences of Jin's confrontation with General Liao?"
  ],
  "safe_through": 394,
  "temporary_decisions": [
    "Render 파이 첸 as Faye Chen and 매직 존슨 as Magic Johnson.",
    "Render 형님 as hyung when Shao Shen addresses Jin Taekyung, and retain Mr. Jin for 진태경 씨 in Team Leader Choi's formal address.",
    "Preserve the hostile, profane tone of Faye Chen's confrontation with Wu Heixing.",
    "Render 마이클 존슨 as Michael Johnson and retain Rao Yang for 롸우양.",
    "Preserve Jin's dry first-person humor, sports-car metaphors, and crude Lord Fuck wordplay."
  ],
  "version": 1
}

## Reading copies

## Chapter artifact 390

# Chapter 390

Whoosh!

Where the Force brushed past, hot blood spurted from rising necks.

I stepped on the body of an ogre collapsing like a bundle of straw and soared high into the air. Sunlight warmed the back of my neck.

*Perfect weather for a fight.*

It was noon. The location was a wasteland without a single tree.

In the middle of more than a thousand gathered monsters, my shadow appeared with the sun at my back.

So did the movement of the spearhead descending with my dive.

*Heavenly Strike.*

Boom!

The fire dragon’s claw raked the ground.

A deafening roar like the sky itself was splitting apart. The earth sank several meters deep, and dirt and fragments of stone flew in every direction.

A whirlwind of hot air that erupted in the middle of the battlefield transformed into blades and swept across the monsters.

Boom!

> **System**
>
> Ding. Ding. Ding…

Through the dust-blurred haze, green blood pattered down alongside the System notifications announcing the monsters’ deaths.

I casually waved a hand, scattering the cloud of dust. The monsters staring at me with dazed expressions came into view.

“Chirrik?”

“Krruk?”

Their eyes seemed to ask what in the world was happening. Drawing in a deep breath, I let out a shout loaded with internal energy.

“Wipe them out—!”

And then—

“Waaaaaaaaah!”

Along with an ear-deafening roar, more than a thousand Hunters who had arrived before I knew it descended on the monster army like a wave.

Crunch!

Wham!

As I watched the monsters collapse helplessly, one certainty took shape in my mind.

*We’ve won this battle.*

The farming was over. Now it was time to harvest.

I headed toward the Twin-Headed Ogre that looked like the boss monster.

It was for the sake of my precious EXP. No—for the sake of minimizing allied casualties.

“That one’s the leader! Ranged unit!”

“Hey, hey! Hands off! I’ll handle it, so don’t touch a single hair on its head!”

I swear to heaven, I didn’t have even the slightest ulterior motive.

……

Well, now that I thought about it, there was no need to swear.

“You despicable human. Your scheme to claim the spoils is obvious. You didn’t even hide your greed while slaughtering my army!”

“Shut up and do your job, will you? Hurry up and start having the undead slaughter their own kind.”

“I was already going to. Grow, skeletons, gro—huh?”

“What’s wrong?”

“Why isn’t my power working? Is this a bug?”

“……”

“Where did you even pick up a word like that?”

The increasingly modernized Skeleton Warlord spoke in a dejected voice.

“It seems the Arch Lich’s control grows stronger the farther inside we go. Ah, a commander without an army. I cannot express the depth of my sorrow. At this rate, I am as good as dead!”

……

What did this bastard think he was?

I was tired of telling him that he was already dead. Suppressing an inward sigh, I charged toward the leader.

* * *

“It’s a crushing victory! Another crushing victory!”

Shao Shen shouted with a face flushed red. Team Leader Choi and I had now seen this scene more than ten times, so we simply took it in stride.

*Well, I suppose he has reason to be excited.*

It had taken barely two hours to annihilate an army of more than a thousand monsters.

And we had finished the battle without a single fatality. It really was a monumental victory. In a situation like this, acting calm would be stranger.

“Our casualties are only twenty-three severely wounded and thirty lightly wounded. Ah, this is really…!”

Shao Shen trembled like a puppy that needed to pee and looked at me with shining eyes.

“How can this happen every time?”

“Hmm. Maybe it’s because I’m strong.”

Team Leader Choi gave me a look of mild disbelief.

“Why?”

“Usually, wouldn’t you say something modest, like that you were lucky?”

“That’s usually how it goes. But what can I do when it isn’t because I’m lucky? I’m actually that strong. Right, Shen?”

Shao Shen nodded at tremendous speed.

“That’s right! Hyung is the best!”

“You rascal. You’re a splendid example of flattery.”

……

Watching us trade lines back and forth, Team Leader Choi slowly shook his head.

“What?”

“Nothing. I suppose this is very much like you, Mr. Jin.”

What was that supposed to mean? Somehow, it sounded unpleasant.

I shrugged and asked Shao Shen,

“More importantly, what about headquarters?”

“Ah, I contacted them before the battle began.”

Contacting them meant that he had dispatched several Hunters under his command in advance.

In a world like this, one might wonder why anyone was still using messengers, but there was no choice. With magic making communication and satellite surveillance impossible, our only options were to run like hell or use vehicles.

At least we still had various modern conveniences, including flares.

“They’ll take a while, then.”

“They were following behind us, so it shouldn’t take too long.”

“You’re probably tired, but pitch some tents and let the men rest. The battle ended quickly, but fighting drains you completely.”

“Shouldn’t we take care of at least the large monsters ourselves? They’d probably be difficult for headquarters to move…”

“That’s a fair point.”

By headquarters, he meant the military forces moving along with us.

When the Hunters of the Public Security Armed Forces Department, myself included, defeated the monsters at the front, the military forces following behind would ‘clean up’ the area and the monster corpses.

The reason I called it cleaning up was that the goal wasn’t to collect byproducts.

This was cleaning in the literal sense. The army assigned to the western front had spent most of its time cutting up the dead monsters and transporting them to the rear so they couldn’t be resurrected as undead.

“Um, hyung.”

“Yeah? What is it?”

“I was too embarrassed to mention this before, but… it seems some of the high-ranking officers have been saying various things.”

“Saying what?”

Shao Shen studied my expression before whispering cautiously.

“They’re a little dissatisfied with the roles they’ve been assigned…”

……

What in the world was he talking about?

It took me quite a while to understand Shao Shen’s words. After a long, heavy silence, I finally parted my lips with a sinking feeling.

“Don’t tell me they want to stop cleaning up monster corpses and distinguish themselves by making some kind of achievement.”

“……”

“Yes.”

“Would you look at these crazy bastards.”

The situation was enough to make curses spill from my mouth. Soldiers were dying every day on the other fronts, and these people were tired of cleaning up monster corpses?

Team Leader Choi, who had been listening quietly, spoke in a calm voice.

“Don’t be surprised. A chink did what chinks do.”

I wondered whether that was really something to say in front of nearly a thousand Chinese people, but Chinese people and chinks were, strictly speaking, different races.

Shao Shen, the representative of all good Chinese people, had turned red with embarrassment.

“I-I’m sorry. But as far as I know, it isn’t all the officers. Only some of them are dissatisfied.”

“Some of them. Naturally. But there’s one thing I’m curious about…”

I frowned and pointed over Shao Shen’s shoulder.

“Does that ‘some’ include the man coming over there?”

In the distance, more than a hundred armored vehicles and tanks were approaching us, kicking up clouds of dust.

* * *

Rattle, clunk!

The vehicle driving along the ruined road bounced up and down. Through the window of the military vehicle I was sitting in, I began to see wrecked rice paddies and fields, along with collapsed homes scattered here and there.

After the cleanup was finished, I—or rather, ‘we’—were on our way to a nearby small city.

“Haha, you’ve really worked hard, Mr. Jin!”

The paunch that even his tightly fastened belt couldn’t conceal. His bald crown gleaming beneath the sun.

If not for the military uniform he wore and the three stars on his shoulder, I would never have had any reason to meet the middle-aged man before me.

“I contacted the higher-ups this morning, as it happens. Your victory report has thrown not only the United Nations Security Council but the entire world into an uproar! I don’t know what it means, but apparently Korea calls today the Lady of the House’s memorial day….”[^1]

That was enough of his nonstop nonsense. Unable to hold back any longer, I abruptly opened my mouth.

“I don’t care whether the Lady of the House is dead or alive. May I ask you one thing?”

“Mr. Jin?”

General Liao, commander in chief of the 13th Group Army of the Chengdu Military Region, which included seven divisions and brigades, looked at me uneasily.

“Why—why are you acting like this? Did something happen?”

“I heard something strange today, so I’m a little sensitive.”

“Who dared upset you, Mr. Jin? Ask me anything.”

“Right. What I wanted to ask was…”

I continued while staring at General Liao’s greasy, glistening face.

“I heard that some officers are extremely dissatisfied because they want to distinguish themselves. I was wondering if you knew anything about that.”

“Ahem.”

So he did know.

The fact that he had known and still left things alone was so absurd that I had become numb to it.

Still, he was technically an ally and a three-star general from another country. I asked as calmly and politely as possible.

“Could I see the faces of those fucking bastards?”

“Ahem!”

“I mean, what kind of insane idiots are throwing a fit about wanting to distinguish themselves at a time like this? To put it bluntly, it’s not as if they’re going to go out and fight themselves. They’ll just stand behind ordinary soldiers and wave their batons around while giving orders, won’t they?”

“Ahem!”

“What the hell do they mean, they’re tired of cleaning up monster corpses? What, they’ve seen so many that the bodies have become familiar and comforting, and now they want to become corpses themselves? They really won’t come to their senses until they actually die. Goddamn idiots.”

“Ahem!”

“If there are people like that, tell them to come see me. I’ll put Equipment on them and place them at the front. They’d make perfect meat shields—”

I suddenly stopped in the middle of my tirade. Cold sweat was pouring from General Liao’s forehead like water from a sprinkler.

……

This man was one of those insane idiots too.

I had suspected he wasn’t a normal lunatic ever since he had started babbling about whether to launch a nuclear weapon from an underground bunker. Now it was clear that he was insane to an impressive degree.

“…General. Are you in your right mind?”

“I-I mean, we also need to show them something. Just a little…”

“What more do you want to show them? We’ve been advancing steadily without taking casualties. The Hunters are clearing the path ahead, while the army follows behind, cleans up, and rescues civilians. We’re doing a good job. What more are you trying to show them?”

Crack.

At the sight of me popping my knuckles, General Liao hurriedly waved his hands.

“Now, now! Let’s not use informal speech with each other. Considering both my age and my rank, I’m not someone who should be treated this way by you, Mr. Jin.”

“How about I show you some respect by smashing a bowl over your head?”

“What did you say?”

“Nothing. You must have heard me wrong. Anyway, I understand. Don’t entertain any foolish ideas. From now on, let’s advance slowly, keeping casualties to a minimum while rescuing civilians. Understood?”

……

Why was this man reacting like that?

The moment I saw General Liao’s eyes rolling around instead of answering, a chill ran down my spine.

*No way…*

“Have you already given the order?”

“Well, the thing is, I’m currently implicated in a military procurement corruption scandal. This is the point where I need to accomplish something independently…”

“You fucking bastard!”

Bang!

My kick tore the armored door from its hinges. The driver in the front seat hurriedly slammed on the brakes.

Screeeeeech!

“Eek!”

General Liao huddled up and trembled before answering in a stammering voice.

“I-I thought there might be monsters in the small city we’re heading toward, so I deployed some of the Public Security Armed Forces Hunters who had been held in reserve…”

I didn’t need to hear anything more. Before I could even press him for details, a tremendous roar rang out from the city, which had already drawn close.

Boom!

A massive explosion. Flames and smoke shot into the sky.

And then—

Ding.

A System notification announced a Sudden Quest.

[^1]: In Korean internet slang, the “Lady of the House” is a tavern proprietress; calling a day her memorial day is a joke about celebrating a victory with drinks.
## Chapter artifact 391

# Chapter 391

Zhang Wei, commander of the Sichuan Province Public Security Armed Forces Department's 2nd Company, had remained in the rear, and he had felt uneasy about this operation from the very beginning.

*Go ahead with the army and occupy the city? That's different from the orders Colonel Xiao gave me.*

The doubt in Zhang Wei's mind had only grown when they deliberately bypassed their allies engaged in combat up ahead and advanced farther in.

“Colonel Wang, are you certain our regimental commander agreed to this operation?”

A high-ranking, middle-aged officer frowned at Zhang Wei's question.

“Why are you curious about that?”

“No matter how I think about it, something feels wrong. Our regimental commander clearly told us to conserve our strength in the rear and guard headquarters…”

“Ah, you mean that little regimental commander.”

Zhang Wei's expression hardened at the senior officer's mocking tone toward Xiao Shen.

“Regimental Commander Xiao Shen holds the same rank as you, Colonel Wang. And he's about to be promoted to major general.”

“That child knows nothing about the world. He was lucky, that's all. As if awakening as an A-rank Hunter wasn't enough, he even made the promotion list this time thanks to that Korean bastard's exploits. Looking at how quickly he's risen through the ranks, I wonder if he has some decent guanxi[^1] in political circles.”

“He may be young, but he's exceptionally capable. He's highly respected, and he's close enough to us to treat us like brothers.”

The senior officer ran his hand along the command baton he was holding.

“I know perfectly well that Hunters don't recognize ranks. But this is wartime. This order came from General Liao, the commander.”

“From the commander himself…?”

“That's right. So if you don't want to follow the order, go back now. But I hope you understand that what you're doing right now constitutes disobedience.”

“……!”

“We're only trying to shorten our advance time. Given the circumstances, it's unlikely, but if there are any monster stragglers left, we'll wipe them out and rescue any civilians in danger. That's all. Do you understand?”

Zhang Wei remained silent for a long while before nodding and stepping away.

The Public Security Armed Forces Department was generally treated as a separate organization that did not belong to the military. But this was wartime. Defying General Liao, the commander of the western front, was by no means a wise choice.

“What did he say?”

Zhang Wei answered the subordinate who asked in a lowered voice.

“He said to shut up and follow because it's an easy operation. Refusing would be disobedience.”

“Do you believe him?”

“If you're asking whether I believe the first part, of course not. But the second part is probably true. What do you think?”

“Of course I don't believe him. That bastard Colonel Wang has made it this far on nothing but his guanxi with the Crown Prince Party, despite having no ability of his own. Everyone says he's General Liao's obedient dog.”

“It is an order from that very General Liao. Even if it smells rotten, we have no choice but to endure it for now.”

“……Damn it.”

“But Colonel Wang might be telling the truth. Most of the monsters in the surrounding area are probably engaged in combat with our allies. With our current strength, we should be more than capable of handling a few monster stragglers.”

Zhang Wei looked around.

In addition to the hundred Hunters, including himself, there were more than twenty tanks and five hundred infantrymen. Three attack helicopters were advancing overhead, keeping watch on the surroundings.

*Please, let there be no serious casualties.*

Perhaps Zhang Wei's wish had reached the heavens, because what he feared did not happen.

The small city near Suining that they entered with every sense alert had been utterly devastated by monsters, but the ruined downtown was completely silent.

Monsters such as goblins and Orcs occasionally sprang out, but they posed no threat whatsoever.

“Kieeeek!”

Slash!

After killing a dozen or so monsters at the very front, Zhang Wei felt a little less tense.

“The monsters are appearing separately, even by species. They must have broken away from their groups.”

“Just as I expected. What did I tell you?”

The officer's arrogant tone was unpleasant, but this was still preferable.

Thinking that, Zhang Wei silently nodded. Then he stopped short at the senior officer's next words.

“You want us to split up?”

“That's right. In a situation like this, we need to find the survivors as quickly as possible.”

“But, Colonel Wang. We haven't even been inside for an hour yet. We should advance a little farther toward the center first…”

“Don't get insolent.”

“Excuse me?”

“You Hunters may be better at fighting, but I'm several steps ahead of you when it comes to tactics. I have command authority right now, so shut your mouth and follow orders.”

“……!”

“Didn't you hear me? Should I give the order to your men myself?”

“……I'll do it.”

“You have a detailed map, I assume. Then we'll meet at the central square in two hours.”

The officer gave Zhang Wei an unpleasant smile and was just about to climb into an armored vehicle when—

Whoooooosh! Boom!

Zhang Wei blinked blankly.

When he wiped his face with his palm, a large amount of sticky blood came away on it.

It was unmistakably human blood, an endless shade of red, and the body of the officer—whose upper torso had already vanished without a trace—was rolling out of the armored vehicle.

Thud.

A suffocating silence fell.

Zhang Wei was the first to recover.

“Everyone, prepare for battle—!”

“Monster! Monsters have appeared!”

“Tank!”

“The regimental commander has been killed!”

The Hunters of the Public Security Armed Forces Department reacted first to the shouts. The soldiers understood what had happened a beat later.

And waiting for them, already thrown into utter chaos by the sudden death of their commander, was an even more horrific death.

Whoooooosh!

There was only a single sound of something piercing the air.

A beam of light shot forward at an invisible speed and swept through the soldiers advancing in orderly ranks and files.

Boom-boom-boom!

The beam burst dozens of people like balloons as it passed through them. Its final target was the armored vehicle moving under the protection of the infantry.

The beam pierced through the hard outer shell and bored deep into the vehicle's interior.

Zhang Wei witnessed the sight and shouted like a thunderclap.

“Everyone, get clear!”

But before his voice could reach them, the deafening roar that erupted in the next moment swallowed everything.

BOOM!

Along with a red flash and black smoke, fragments of the armored vehicle shot in every direction, becoming hundreds—thousands—of blades that ripped through everything around them.

Soldiers and lower-ranking Hunters who had been unable to react in time alike fell like bundles of straw.

The bodies of those who were already dead did not move at all.

“……!”

“W-what the hell is this…?”

Zhang Wei bellowed at the people frozen like statues.

“Spread out! Everyone, spread out! Get as far away from the tanks and armored vehicles as possible!”

But the bodies of soldiers experiencing actual combat for the first time had gone rigid, and the unseen enemy never failed to take advantage of the enemy's confusion.

Whooooooosh!

The sound of death came again.

But unlike before, there was more than one beam of light.

Boom! Boom-boom-boom!

“Aaaaaagh!”

Flames shot upward, and screams flooded the air.

The more than twenty armored vehicles and tanks were rendered useless in no more than an instant.

The three attack helicopters circling overhead were also reduced to countless fragments and came crashing down to the ground.

Boom! Rattle-rattle-rattle.

In the horrific scene that could only be called a sea of corpses and blood, Zhang Wei felt a chill run down his spine.

*At least A-rank monsters. And there isn't just one or two of them.*

Ironically, it was the most accurate judgment Zhang Wei made that day.

Sssssss.

Between dark alleys and collapsed buildings. On the rooftop of a building that was still burning.

Ten figures that had appeared like black mist stared down at the hundreds of surviving humans with burning violet eyes.

When Zhang Wei spotted the figures mounted on warhorses with nothing but bones left on them, a groan-like word escaped between his lips.

“……Death Knights.”

Knights of death who had once been noble, but had been corrupted by black magic.

The very Death Knights who had vanished along with the Lich after the Great Cataclysm had appeared. There were no fewer than ten of them.

The first word that came to Zhang Wei's mind was *death*.

*Is this where it ends?*

Death Knights were beings that had surpassed A-rank monsters.

A hundred Hunters and a military force still remained, but Zhang Wei already knew.

They could not escape the net the monsters had spread.

But…

“I have no intention of dying quietly.”

Zhang Wei was not the only one who felt that way.

Unlike the soldiers, who were too frightened to even hold their guns properly, the Hunters of the Public Security Armed Forces Department raised their weapons with determined eyes.

“You don't have to go this far.”

One of the platoon commanders answered Zhang Wei's low murmur bluntly.

“And you're allowed to?”

“I'm sorry. I shouldn't have brought you here.”

“No one brought us. We followed you. We've survived more than ten times thanks to you, so it was about time we did this at least once.”

He spoke casually, but he could not hide the trembling in his voice.

Zhang Wei licked his parched lips as he stared at the ten Death Knights standing completely motionless.

“Fight with everything you have, and make sure at least one of you survives. That's all I have to say.”

A booming cheer erupted instead of an answer.

The Hunters' eyes shone like morning stars, having driven away their fear.

If they had wanted a safe and prosperous life, they had other paths available to them.

But they had chosen the Public Security Armed Forces Department instead of becoming bodyguards for wealthy entrepreneurs or working as mercenaries because of their honor and sense of responsibility as Hunters.

This was a fight they could never retreat from.

“Go! Sons and daughters of the people, descendants of Zhonghua!”

Just as Zhang Wei finished shouting with all his strength and was about to charge toward the nearest Death Knight—

Rrrrrumble!

It was almost instinctive.

A massive energy could be felt alongside the violent tremors. The surviving humans turned their heads, terror making every hair on their bodies stand on end.

Where all those eyes turned, a black knight was slowly crossing the ruined downtown.

Red eyes flashed beneath the deeply lowered helmet. The breath of death poured through its bloodless lips.

“—Sar, Garrosh.”

It was a language from the demon realm that no one could understand.

Yet in the next instant, Zhang Wei realized what those words meant.

*Kill them all.*

Reflected in Zhang Wei's widened eyes were the ten Death Knights charging in from every direction.

Slash!

The slaughter had begun.

* * *

Splash.

A horse hoof made of nothing but bone stepped into a pool of blood.

The Death Knights who approached the black knight, who was staring down at the corpse of the middle-aged Hunter Zhang Wei—the last to resist—knelt on one knee.

“—Lord. Your next command.”

His next command.

The black knight was silent for a moment before suddenly extending a hand.

Whoosh! Slash!

A black beam lashed out like a whip and sliced through concrete and rebar.

A building collapsed at an angle. In the exposed space inside, several humans crouched together, desperately covering their mouths.

“Jinjin. Honey. It's okay, it's okay…”

“Sniff… sob…”

“Dadda?”

A human male and female. And…

A being so small and light that it was impossible to distinguish its sex.

*Was that what they called a child?*

*Child. Child?*

Where had he heard that word before?

The black knight pushed the question aside and extended his hand. Every human in sight had to be annihilated. That was the command he had received.

But—

“……?”

For some reason, his hand would not move.

They were undoubtedly weak beings who would turn into a handful of blood and vanish from a mere flick of his finger, yet it was as though an invisible barrier surrounded and protected them.

“What are you?”

At the black knight's eerie voice, the child squirming in its parents' arms suddenly began to wail.

“Waaaaah!”

“This is…”

The black knight abruptly raised his head and looked beyond the ruins, then turned his mount around.

The Death Knights expressed their confusion at their leader's sudden action.

“—Lord?”

“We're going back. Now. At once.”

“Then shall we deal with the humans—”

“We're going back. Now. At once.”

That was all.

The ten Death Knights bowed on one knee in deference before riding after their leader.

Just before their figures vanished like mist, the black knight's red gaze fell upon the three humans who had survived as if by a miracle, then moved away.

Whooooooosh.

Wind carrying the smell of blood swept through the ruin filled with corpses.

[^1]: *Guanxi* refers to influential personal connections and relationships, especially those used within social or political networks.
## Chapter artifact 392

# Chapter 392

*Damn it. Faster. Faster.*

Whoooooosh!

I squeezed out every last ounce of strength and activated my movement technique. Each time the scenery flashed past, the ruined city drew closer at terrifying speed.

But I could tell how things had ended before I even arrived. No—I should say someone had told me.

Beep.



> **System**
>
> ??? has completed its objective and disappeared.
>
> Sudden Quest, **Unexpected Assault**, has been canceled.
>
> You failed to complete the Quest. As a failure penalty, a random stat decreases by 10.
>
> **Strength** decreases by 10.

The moment I heard the System notification, the tension that had been wound tight inside me abruptly released.

It wasn’t because I had failed the Quest, nor because my stat had decreased. I knew what this meant.

The silence I felt as I drew closer to the city, followed by the scene that unfolded before my eyes moments later, changed my suspicion into certainty.

“……”

Blood covered the area in every direction, and corpses lay scattered in horrifying positions. Even I, who had grown accustomed to death after fighting countless battles, froze for a moment.

*Massacre.*

Yes. This was a massacre. They had blown people apart, torn them to pieces, and crushed them.

The sight of living humans having been hunted down and killed like ants made it hard to breathe.

If even I, an outsider from another country who had never met these people, felt that way, then the grief and rage of the Hunters from the Public Security Armed Forces Department who arrived behind me could not be expressed in words.

「Zhang Wei! Langlang!」

「W-Who the hell did this? Who the hell…? Sob…」

「No! Aaaaaah!」

These were the comrades who had entrusted each other with their backs. Among the people lying there as cold corpses were their brothers and their lovers.

Amid the endless wailing and shouting, one person who had been standing silently suddenly took a step forward.

Thud. Thud.

Perhaps his hollow footsteps sounded especially loud because, unlike his usual self, his face was utterly numb and devoid of emotion.

Team Leader Choi, standing beside me, called my name in a low voice.

“Mr. Jin.”

“I know. Me too.”

Sometimes there were things you had to do even when you didn’t want to. This was one of those times, and I painfully forced my lips apart.

“Shen.”

「…….」

“Shao Shen!”

Thud. Thud. Thud.

Despite my forceful shout, Shao Shen’s footsteps did not stop. He simply continued walking toward some unknown place in search of the criminals who had killed his subordinates.

In the end, I had to approach him myself and grab his shoulder.

Smack.

“Stop.”

A dry, lifeless voice spilled out.

「……Let go. I have to go.」

“Where?”

「Where?」

Shao Shen looked around with empty eyes before continuing.

「I don’t know. But they must be somewhere.」

“You…”

「I have to chase them. I’ll find them somehow, no matter what it takes, and I’ll have my revenge.」

“……!”

For a moment, I was unable to speak.

The man I saw before me was not Shao Shen. He was me, a few years ago.

That was why I couldn’t easily say what needed to be said.

*Because I know how he feels.*

He wanted to kill them, and he probably wanted to die as well.

The feelings left behind by the deaths of those close to you weren’t only rage and grief. For the survivor, there was guilt waiting—heavier than those two emotions combined.

The guilt left behind by a hundred deaths was far too heavy for a twenty-one-year-old young man to bear.

*Damn it.*

I swallowed the curse circling the tip of my tongue and tightened my grip on his shoulder.

“You’re too late.”

「…….」

“It’s already too late. We can’t find them right now. This isn’t a guess. I know it for certain.”

The System notification had told me so. There was no way I could be wrong.

Shao Shen met my confident gaze and muttered blankly.

「I’m too late. It really is too late.」

“I don’t want to admit it either, but… yes. That’s reality.”

I thought he would finally let his suppressed rage and grief erupt.

Just as I had done years ago, I thought he would cry out loud and smash anything he could see.

But I was wrong. The object of Shao Shen’s desire for revenge wasn’t limited to the monsters.

Rattle-rattle. Thud.

The tanks were only now entering the city.

As Shao Shen watched the advancing column draw closer from a distant speck, his eyes burned like flames.

「Then I suppose I’ll have to kill that bastard, at least.」

It was obvious who *that bastard* referred to.

General Liao. The man responsible for issuing this goddamn order.

Because of a single ridiculous order from that bastard, a hundred Hunters and hundreds of soldiers had died. Even I thought he was someone who absolutely had to pay the price.

But…

“Fuck. I’m sorry.”

Feeling wretched, I reached out.

Shao Shen sensed something was wrong and tried to evade me, but my hand moved fluidly and had already brushed his acupoints.

Tap. Tap-tap!

The Paralysis Acupoint, the Mute Acupoint, and the Sleep Acupoint.

Shao Shen’s entire body went rigid, his voice was cut off, and deep sleep began to overtake him.

His eyelids trembled as though he were struggling with all his strength to resist the drowsiness pouring over him.

“For now… get some proper sleep. Their deaths weren’t your fault.”

Sshk.

In the end, his eyelids closed firmly. The last thing I saw in Shao Shen’s eyes was unmistakable confusion.

*Why? How come?*

And Shao Shen wasn’t the only one who felt that way.

「Regimental Commander!」

「Jin Taekyung, you!」

Whoooooosh! Shing!

Along with furious shouts, five sounds of air being split apart rang out.

They were A-rank Hunters under Shao Shen’s command, men called company commanders.

I swept a hand toward them as they charged without hesitation.

Boom!

With the sound of compressed air exploding outward, the weapons flying at me abruptly changed direction.

The company commanders barely blocked the palm force that had torn through the air toward them, and their bodies slid backward across the ground.

It was fortunate that I had restrained my strength. If I had truly steeled myself, things would not have ended this easily.

“Everyone, calm down. I didn’t want to go this far either.”

「Kgh!」

「What the hell do you think you’re doing?!」

「How dare you lay a hand on the regimental commander…!」

「This is how you repay his kindness?!」

As the atmosphere grew more hostile, Team Leader Choi stepped forward and spoke in a low voice.

“Mr. Jin is only repaying the favor.”

「W-What did you say?」

“If we had left him alone, the enraged Regimental Commander Shao would have killed General Liao.”

「……General Liao deserves to die. Even if our regimental commander hadn’t done it, we would have taken matters into our own hands.」

“I agree. But I don’t know what your country’s Central Committee would think of that—especially the Crown Prince Party, which General Liao belongs to.”

「……!」

“The man you’re talking about is the supreme commander responsible for an entire front. If you kill him, it won’t end as a personal matter.”

Team Leader Choi looked over the Hunters from the Public Security Armed Forces Department one by one.

They were a force numbering around a thousand. I hadn’t thought that far ahead, but if they became involved in an incident like this, they wouldn’t be able to avoid trouble either.

“I’m not telling you to forget what happened today. I’m only saying that now isn’t the time.”

I could feel the hostile atmosphere beginning to settle.

Team Leader Choi’s words were both practical and grounded in emotion. One of the company commanders who had not joined the attack finally spoke.

「I agree. Dealing with that bastard right now would be easy, but… if we did, it would be difficult to deal with the consequences.」

「…….」

「Remember this. Our brothers didn’t die solely because of General Liao.」

After looking around at the horrific sea of corpses and blood, he ground his teeth.

「Let’s wait a little. Just a little longer. The time will come soon.」

「Haaah.」

「……Damn it all!」

Some people looked up at the sky and lamented. Others failed to contain the grief and rage surging inside them.

But it was clear that they had all reached the same tacit agreement.

Once the situation finally came to an end, Team Leader Choi let out a relieved sigh.

“We can finally breathe. It’s fortunate that you stopped Regimental Commander Shao, Mr. Jin.”

“……It was nothing.”

Fortunate. Was this really something we should call fortunate?

Even knowing that there had been no other choice, I was left with a bitter taste in my mouth. I knew the rage and grief Shao Shen must have felt.

“More importantly, it seemed there were survivors.”

“There was a middle-aged couple and one child. They apparently fainted from extreme tension, so they’re being moved somewhere else to rest for now.”

“Are there any other survivors?”

“We’ll find them soon enough.”

Team Leader Choi frowned and looked over my shoulder as he continued.

“Once the order comes down from that utterly incompetent commander, at least.”

Rattle-rattle.

The armored vehicle advancing with a deafening racket stopped about twenty meters ahead of us.

A moment later, under heavy escort, the plump General Liao emerged.

「W-What in the world…?」

At the horrific sight before him, his already fair complexion turned deathly pale.

Watching him bend over and retch for quite some time, I felt disgusted—but I also found myself thinking that he was human after all.

*You bastard. I guess you do feel some guilt.*

Everyone here had probably been thinking the same thing as me.

But the next words General Liao spoke reminded me of a lesson I had forgotten.

People like him always exceeded the limits of imagination.

「N-No. The operation wasn’t supposed to fail!」

“……!”

The world seemed to slow down.

Like a slow-motion scene, I saw shock and rage rise across the faces of the people around me.

I saw Team Leader Choi reaching out toward me and shouting urgently.

“Mr. Jin!”

But it was already too late.

By the time he called my name, I had already crossed the twenty-odd meters and arrived in front of General Liao.

*An operation. An operation…*

I couldn’t hold back a laugh.

I reached out toward the man staring up at me with a blank face, as though he were looking at a ghost.

Crack! Crunch!

It happened in an instant.

Using nothing but physical strength, without a single thread of internal energy, I broke both his arms and crushed his kneecaps.

*Consider yourself lucky I still have a shred of reason left.*

His mouth hung open. His eyes bulged wide.

Then a scream like a pig being slaughtered burst from him.

「Aaaaaaaaargh!!!」

I spat at him as he rolled his eyes back, collapsed to the ground, and convulsed in pain, then turned away.

I didn’t forget to say one thing to the staff officer staring at me with a face drained of all spirit.

“Report it to your superiors if you’ve got a fucking problem, you bastards.”

Team Leader Choi shook his head repeatedly and approached with a high-grade potion.

* * *

The chair was enormous and bizarre.

That was only natural. It had been made from human and monster bones.

But it was not as bizarre or terrifying as its owner.

Tap. Tap-tap.

A finger without a trace of flesh tapped the skull decorating the armrest.

The figure stood well over three meters tall, with an enormous frame. A black robe draped over it rippled like mist.

It looked like a king seated upon a throne, and that wasn’t entirely wrong.

The Arch Lich.

It was an existence worthy of being called the lord of the undead and the king who ruled over death.

But the Arch Lich itself did not think that way. There was a true king elsewhere, and it was merely his loyal servant.

But…

*Was it still too soon?*

The Arch Lich suddenly felt a pang of regret.

It possessed truly formidable magical power, but it was still far weaker than the strength it had once possessed. On top of that, the situation on the battlefield was proving more difficult than expected.

After silently sinking into thought, the Arch Lich opened its mouth.

“Are you listening, my servant?”

The being kneeling in the darkness answered.

“Yes, my lord.”

“Pull back the front line. We’ll draw the human army in.”

“I obey.”

“Go. Deliver my command to every legion within the reach of my power.”

The black knight rose and slowly backed away.

At the final moment, the Arch Lich’s chair was reflected in his eyes, which burned red.

Tap. Tap-tap.

The skull decorating the armrest was far too small to have belonged to an adult.
## Chapter artifact 393

# Chapter 393

War is a succession of battles.

When a battle that has left behind countless dead and rivers of blood finally ends, victory and defeat are decided. Those who survive gather in one place and prepare for the battle of tomorrow.

That was why the commanders of the eastern and western fronts in Sichuan Province had gathered together.

“The casualties are too high.”

The first to break the silence was a middle-aged soldier who looked to be in his forties. Wearing a uniform caked in dried blood, he continued in an exhausted voice.

“We managed to hold the high ground by the skin of our teeth, but we lost more than three thousand troops in a single day.”

A victory that had left nothing but wounds.

Three thousand troops was an enormous loss in itself, but the bigger problem was that more than thirty percent of the dead were Hunters, including the commander and several high-ranking officers.

Even taking into account the three-to-one difference in troop numbers, the damage was staggering.

“Did headquarters send a reply?”

“Of course. They said they’ll send a new commander before dawn after holding an internal meeting.”

“That’s a relief, at least. Then, do you happen to know who the new commander will be…?”

As people exchanged words in the somber atmosphere, someone suddenly spoke up.

“A relief? Do you all really think that?”

“……!”

Words spoken by someone who had remained silent carried weight. Even more so when that person was a living hero of the Great Cataclysm and an S-rank Hunter.

“Half the command staff, including the commander, were torn to pieces by the flying monsters. The troops under them panicked, which only made the casualties worse. Can you really call a situation like this a relief?”

The people flinched beneath the gaze filled with an irresistible aura.

“W-Well, the thing is…”

“You’re trying to make excuses, so I suppose you do know. But…”

A chilly voice slipped from between red lips.

Faye Chen’s gaze moved across the room before stopping abruptly on one man.

“Why don’t you have any excuses?”

After a brief silence, Wu Heixing swirled the alcohol in his crystal glass.

“Why should I make excuses?”

“If you’re asking why, well…”

Faye Chen’s eyes deepened.

“Maybe it’s because some fucking idiot abandoned the area he was assigned to, allowing the flying monsters waiting for that moment to tear the command headquarters apart?”

“I did it to help the front line.”

Wu Heixing’s answer was nothing more than a pathetic excuse. When he abandoned the rear, the troops on the front line under Faye Chen’s command had been successfully holding back the endless assault of the monster army.

“Oh, right. There was that, too. You went charging deep into enemy territory like an ignorant brat because you wanted to earn some military glory, and the formation collapsed. The kids who chased after you to save your ass—do you even know that their bodies were never found?”

“Life and death are common occurrences on a battlefield.”

“Of course. They’re very common.”

Faye Chen continued in a low voice.

“People like you dying without anyone knowing used to be even more common. Come to think of it, the world has gotten pretty nice. If this had been during the Great Cataclysm…”

But Faye Chen’s words never reached the end.

Crack! Crash!

Crystal shards flew in every direction with a sharp sound.

Wu Heixing slowly rose to his feet after smashing his glass.

“That’s enough.”

“Enough? You’re getting awfully casual with your words.”

“There’s a limit to how much I can tolerate, Faye Chen.”

“Go on. Keep talking. Just remember that as your words get shorter, so does your lifespan.”

“How dare a Hong Konger who’s practically a traitor—!”

“Ah. If you mean the Hong Konger who cleaned up the front line you shat all over, then I suppose that’s me.”

Whoooooosh.

The tremendous auras flowing from the two of them spread through the room. Under the overwhelming pressure, the people could barely breathe.

The brief standoff between the two S-rank Hunters ended the next moment with a mocking smile appearing at the corner of Faye Chen’s mouth.

“You’re scared and exhausted, but you still want to earn military glory. That’s why you’re getting more desperate by the day, isn’t it?”

“What?”

“Kid, that’s what war is like. It always drives people to the edge and tests them. You need a strong mind to endure hell like this. For an immature child like you, who’s always lived however he pleased, it was bound to be difficult.”

“……!”

Wu Heixing’s face twisted grotesquely. Every one of Faye Chen’s words had struck him in the heart.

“An S-rank Hunter? So what? Mentally, you’re nothing more than a seven-year-old child. Someone like you is worse than useless in a war like this.”

“Shut your mouth! What the hell do you know…?”

“What do I know? Are you saying that to me?”

At Faye Chen’s derisive snort, Wu Heixing’s face flushed bright red.

He had been born with power and wealth in both hands, but his opponent was a war hero who had fought her way through the Great Cataclysm firsthand.

The media had discriminated against Faye Chen because she was from Hong Kong, but when it came to experience, Wu Heixing could not hold a candle to her.

“Why aren’t you answering?”

Grinding his teeth and refusing to respond, Wu Heixing swept his gaze around the room.

No one had bothered to say anything aloud, but the looks in their eyes resembled Faye Chen’s.

*You’ve got to be fucking kidding me…*

What infuriated him even more was that some of them were members of the Crown Prince Party who had close ties to Wu Heixing.

The Crown Prince Party was the largest faction within the Chinese Communist Party. As the blood descendant of one of the faction’s most prominent leaders, Wu Heixing felt betrayed to the bone.

“I’ll remember what happened today. Every bit of it.”

Wu Heixing turned away after leaving those words behind, thick fumes of liquor trailing from him.

Faye Chen’s low voice flew after him and struck him in the back.

“Remember this, too. A child’s little act of bravado ends today. If a situation like today’s happens again… I won’t forgive you next time.”

Grind.

The first thing Wu Heixing did after returning to his quarters, grinding his teeth, was smash everything within sight.

Boom! Boom-boom-boom!

“Fucking Hong Kong bitch! You goddamn traitor bastards!”

Even amid the chaos, the expensive luxury furnishings brought over on his private jet were smashed to pieces.

After stomping and breaking whatever he could reach while screaming like a madman, Wu Heixing finally lay down on the bed, breathing heavily.

“Damn it.”

The anger refused to subside.

Rather than fading, it only grew hotter the more he thought about it. His heart pounded, and his vision nearly turned white.

*How dare they treat me like this?*

He had been born into the family of one of the most powerful men in China and had risen all the way to this point.

After becoming an S-rank Hunter, the world had completely belonged to him.

No matter what major disaster he caused, the worst that happened was being summoned by his father and scolded a few times. He had never cared about the criticism from the public or opposing factions.

*I’m Wu Heixing. Wu Heixing!*

An S-rank Hunter was the face of a nation and another name for national power. No matter how much public opinion pointed fingers at him, that fact did not change. That was reality.

Was that why he had become more passionate about media interviews and parties than smelly, dirty raids? Why he had stopped training and started using drugs?

But the first war he had ever experienced was chaotic, and watching the monster armies advance endlessly day after day made it difficult to breathe.

For someone who had walked an elite course paved with diamonds, it was an unbearably difficult environment.

On top of that, there was one person whose influence still lingered behind Wu Heixing’s repeated mistakes.

*Jin Taekyung.*

A wall even greater than Lei Fei, the object of his long-standing jealousy—the second such wall he had encountered in his life.

The shadow Jin Taekyung cast was broad and dark.

The fear carved deep into Wu Heixing’s mind by his one-sided defeat would never be shaken off as long as Jin Taekyung remained.

*Right. As long as that peninsula bangzi doesn’t disappear…*

An inexplicable light flashed in Wu Heixing’s eyes as he stared at the ceiling.

Recalling the conversation he had shared with Lee Jungryong on the night of his terrible defeat, he smiled. The anger that had been boiling hot had disappeared long ago.

*Let’s wait and see. Let’s see who gets the last laugh.*

Once his mind calmed, the fatigue he had temporarily forgotten came rushing back and weighed down his eyelids. As drowsiness overcame him, Wu Heixing suddenly thought:

*Damn it. Just how many battles like today’s are we going to have to fight from now on?*

A short while later, Wu Heixing fell fast asleep, unaware that countless monster armies were withdrawing from the front lines under cover of the pitch-dark night.

The great movement was taking place simultaneously across every front in Sichuan Province.

* * *

“……Phew.”

Shao Shen let out a sigh, his eyes red and bloodshot.

He had spent the night with his Sleep Acupoint struck and had only regained consciousness two hours ago.

The moment he opened his eyes, he had gone berserk, shouting that he was going to kill General Liao. Team Leader Choi and I had sweated bullets trying to calm him down.

“Shao Shen, are you all right?”

“Yeah. Are you feeling a little calmer now?”

Shao Shen answered.

“Yes. When I first woke up, I couldn’t put any strength into my body, but I’m fine now. This is more than enough to rip that bastard’s head off.”

“……”

“……”

Calmer, my ass.

Still, unlike his words, only his fists were trembling, so I felt some relief that he did not seem to be planning on playing golf with General Liao’s head right away.

“I’m telling you again, I didn’t want to do that to you. The timing was just bad.”

Shao Shen was silent for a moment before nodding.

“I know, hyung. I know you stepped in on my behalf, too.”

“When did you hear that?”

“The company commanders came and told me. They said that furious hyung broke General Liao’s arms and legs.”

“……As the person who stopped you, it wasn’t something I should have done. But, well, that’s how it turned out.”

Team Leader Choi cut in with a stiff voice.

“If it was something you shouldn’t have done, why did you do it?”

“That’s because, um… I lost my head for a moment.”

“It’s fortunate that the current situation is so chaotic. Otherwise, this could have become a serious problem.”

“Lucky for us, then. If things weren’t like this, that bastard would have died by my hand long ago.”

An incompetent commander was more frightening than an enemy.

General Liao had thrown away nearly a thousand lives and was talking about military glory after the operation had failed. He deserved to die.

“Everything worked out. His injuries are almost healed thanks to a potion, and they have reasons of their own to feel guilty, so they’ll let it slide.”

“Grudges last a long time, Mr. Jin. He’s a high-ranking general of the Central Military Commission, and a pure-blooded member of the Crown Prince Party, notorious for holding grudges. There’s ample room for this to become a problem later.”

“What can we do? The water’s already spilled. We’ll think about it if a problem arises.”

Team Leader Choi was shaking his head in disbelief at my nonchalant answer when Shao Shen spoke in a low voice.

“Don’t worry. The thing you’re concerned about, Mr. Choi, won’t happen.”

“Hm?”

“Shao Shen, did you hear something?”

“Rather than hearing something…”

After hesitating for a moment, Shao Shen shook his head with a stern expression.

“Um… it’s just my personal opinion.”

“……?”

“……?”

What was this suspicious smell?

Team Leader Choi and I were looking at Shao Shen suspiciously when—

“M-m-m-may I come in?”

“Did an earthquake hit your vocal cords? Come in.”

Only then did the person who had been pacing outside the tent cautiously step inside.

It was a familiar face—one of the staff officers who served closest to General Liao.

He was also the man who had pissed himself the day before when he saw me break his superior’s limbs.

“The big country’s little pisser has arrived. What brings you here?”

“G-g-g…”

“S-s-s-say it already. What is it you want to say? Speak properly, please.”

The staff officer flinched, swallowed hard, and answered.

“A-a-a guest has arrived.”

“A guest?”

“Yes.”

“Who? Are visitors even allowed here?”

*It can’t be Mom and Hayeon, can it?*

That absurd thought had just crossed my mind when the staff officer’s answer came flying at me.

“Magic Johnson, a Hunter from the United States, has come to see you.”

I could feel Team Leader Choi clench his butt beside me.
## Chapter artifact 394

# Chapter 394

As expected, the mainland was on an entirely different scale.

I had clearly heard that this was a small provincial city, but once I actually entered it, the area and population were far beyond anything I had expected.

Even after a monster army had swept through the place, quite a few buildings were still standing.

*This one, too.*

At the entrance of the municipal hospital, which was currently being used as a temporary headquarters, a tall white Hunter spotted Team Leader Choi and me before approaching.

“I’ve been waiting for you.”

“Are you the one sent by Magic Johnson…?”

“Yes. My name is Michael Johnson. Please feel free to call me Michael.”

“Ah, yes.”

*Is everyone over there named Johnson? Is there some kind of Johnson family reunion in L.A.?*

I shook Michael’s hand, still puzzled.

After the handshake, he beamed at me.

“What?”

“I’m a huge fan of yours. Lord Fuck.”

“……”

“I’d appreciate it if you called me Jin instead of Lord Fuck.”

“Why? If it were me, I’d love that nickname.”

“Then should I call you Little Johnson?”

Michael answered with a perfectly straight face.

“Nope.”

*Look at how decisive he is.*

I was dumbfounded as I replied.

“It’s the same idea. So please call me Jin.”

“Ah, okay.”

*That Lord Fuck nickname is really spreading to every corner of the globe.*

Cheon Taemin, who had defeated the Demon King and was called the savior of the twenty-first century, had obtained the incredibly cool title Slayer. Even if I beat a Demon God instead of a Demon King, I would probably remain Lord Fuck.

At best, I’d evolve into Lord Fuuuck.

“Don’t take it too hard. Lord Fuck is a warm and friendly nickname, isn’t it?”

“Team Leader. Are you making fun of me?”

“Of course not.”

As Team Leader Choi let out a quiet laugh, Michael recognized him.

“Choi. You came too.”

“Do you know me?”

“Of course. The news of how much Johnson likes you has already spread throughout the Guild.”

“……”

I jabbed Team Leader Choi in the ribs. His expression had darkened in an instant.

“Don’t take it too hard. Johnson’s Johnson likes you, Team Leader.”

“……Mr. Jin. You just said Johnson twice.”

“Did I? I must have misspoken.”

Pretending not to notice Team Leader Choi’s sharp glare, I asked Michael,

“Where is Johnson?”

“Ah, I’ll show you.”

We followed him inside. The moment we entered the lobby, the murmuring noise abruptly vanished, and people’s gazes came flying toward us.

I had heard that several civilians rescued during the night were here, but since this was a temporary headquarters, it seemed to be filled almost entirely with soldiers.

“The atmosphere changes the moment Jin appears.”

“I was already famous, but I’m probably a little more famous after yesterday.”

“Oh, did you kill a Named Monster or something?”

I shrugged at Michael’s question.

“Something like that.”

Considering General Liao’s position within the military, he was a Named Monster in his own right.

The people on that side had issued their own gag order, but somehow the rumor had spread everywhere. Each time I passed by, I heard soldiers whispering under their breath.

“Did you hear? Yesterday, Mr. Jin did something to the commander…”

“If you mean that story, I heard it, but wasn’t it just a rumor?”

“They say it’s not a rumor. It’s true. The Hunters heard it, and apparently even the headquarters operations soldiers confirmed it. They said Rao Yang heard it clearly.”

“Huh. If that’s true, I’m disappointed in Mr. Jin.”

“Me too. I thought he was a hero of the people.”

The reaction was exactly what I had expected.

*Crabs side with crabs, and people’s arms bend inward.*

Naturally, the soldiers wouldn’t be happy about me pulverizing their direct superior…

“He shouldn’t have just broken the man’s limbs. He should’ve ripped his head off.”

“Exactly. How many people died because of that pig bastard?”

“I heard he took a huge cut in the latest defense procurement scandal, too. That’s why he’s keeping quiet and letting it go even after getting his limbs broken. Following Mr. Jin around is the only way he can pick up a few scraps of military glory and save his own skin.”

“That damn thief. Someone like him should be hanged in Tiananmen Square.”

*……What? They seem to like me quite a lot.*

It wasn’t just the ordinary soldiers. Even the officers were whispering among themselves.

They called General Liao an incompetent pig who had sacrificed his troops. Some said they finally understood why they were still using canteens made during the Chinese Civil War.

When the circumstances that had come to light were combined with General Liao’s usual reputation, an endless stream of statements poured out that could have gotten them arrested for insulting a superior.

“The atmosphere is good. At this rate, we won’t have to worry about the aftermath.”

Walking beside me, Team Leader Choi spoke with satisfaction. I answered with a dazed expression.

“Yeah. If I’d known, I should’ve hit him a few more times.”

“Hmm. I still have a few Top-Grade Potions left.”

“Look at you, Team Leader. You’re getting good at jokes.”

“Not entirely a joke.”

“Huh?”

*What got into this guy all of a sudden?*

Team Leader Choi stared straight at me as I struggled to process his unexpected response.

“Mr. Jin is an S-rank Hunter in both name and reality. You’re the dream and symbol of ordinary citizens, as well as a celebrity who enjoys the support of the public. General Liao, on the other hand, is corruption and entrenched privilege personified. Anyone who tries to come after Mr. Jin will have to be prepared to pay an enormous price.”

“So you’re saying it wouldn’t matter if I hit him a little harder?”

“It would matter, but I mean that you won’t be held back by someone like General Liao, who is about to fall.”

“Seriously? You were telling me not to cause trouble just a few hours ago.”

“Even the best sports car will crash if you only step on the accelerator. Someone needs to sit beside you and hit the brakes, like me. And…”

Team Leader Choi continued in a low voice.

“Sometimes you have to maintain the track so the sports car can run properly. Like now.”

“……”

“Yesterday, too many people witnessed what happened. If the gag order was bound to fail anyway, I thought it would be better to spread the story as quickly as possible.”

It didn’t take long for the question marks in my head to turn into exclamation points.

“Team Leader, did you…?”

Team Leader Choi smiled as he looked at me, my mouth hanging open.

“Getting ahead of things and spreading the most favorable rumor possible. That’s a method Vice Guild Master Lee Jungryong uses often.”

“……Huh.”

Everything finally fell into place.

I had wondered why the rumor had spread so quickly that the gag order seemed meaningless. Team Leader Choi had clearly laid the groundwork in advance.

The Hunters from the Public Security Armed Forces Department already hated General Liao intensely, so they would have been easy to mobilize. And the soldiers…

*He opened his wallet.*

In the end, it always came down to money. Team Leader Choi had paid people to talk, and they had spread the rumor in whatever way was most favorable to us.

Besides, wasn’t the military a place crawling with microphones and speakers?

*Rumors spread quickly.*

Ten people opened their mouths, a hundred people heard them, and those hundred people told a thousand more. If you added a generous sprinkling of MSG along the way, the inflated rumor was bound to become accepted as fact before long.

*But he thought of all that and pulled it off in a single night?*

I looked at Team Leader Choi with deep respect.

“Team Leader Choi, are you Zhuge Liang? Zhang Liang?”

“It was nothing special.”

“Team Leader Come. I think I’m about to Choi.”

“……Stop it.”

While we were having that conversation, Michael, who had been walking ahead of us, stopped.

Knock, knock.

“Johnson. It’s Michael.”

Beyond the door marked VIP Private Room, two auras of different sizes reacted. A deep but cheerful voice came from inside.

“Oh, come on in.”

“Apparently so. My assignment ends here, so I’ll be going.”

Michael shrugged at us and stepped aside.

I slid the door open in place of Team Leader Choi, whose butt was clenched tight.

Rattle.

Two people appeared behind the door.

“Haha! So we meet again, charming young men!”

The first was a huge Black man who strode toward us and extended a hand as large as a pot lid—Magic Johnson.

And then…

“Eek!”

A plump pig that shrieked in terror the moment he saw me.

I glanced at General Liao, whose double chin was trembling, then took Magic Johnson’s hand and whispered,

“When did you get here?”

“About… thirty minutes ago?”

“What about the southern front you’re in charge of? And for that matter, why didn’t you come find us right away? Why are you here with this guy?”

“Wait a moment. I’ll answer your questions one at a time. But first, I need to say hello to Choi.”

Snatch.

Magic Johnson caught Team Leader Choi’s hand like a hawk swooping down on its prey and greeted him warmly.

“How have you been? Have you thought about me a lot?”

“…Yes.”

Team Leader Choi’s answer was one hundred percent sincere. He must have thought about all kinds of things on the way here.

But since Magic Johnson had no idea what the answer meant, it was more than enough to set his heart aflutter.

“Oh! Then you’re just like me. We have so much in common, don’t we?”

“……”

*We’re probably very different when it comes to the gender we like.*

“Anyway, it’s good to see you again.”

With his gaze still dripping with longing, Magic Johnson ended his reunion with Team Leader Choi and answered my earlier question.

“And if you’re talking about the southern front I’m in charge of, don’t worry. Nothing will go wrong just because I’ve stepped away for a little while.”

“It sounds like the war is going very well.”

“Hmm. I’m not sure about that. It is encouraging that the monster armies are retreating from every front at the moment.”

“Oh, the monster armies are retreating… What?”

Team Leader Choi and I blinked at each other as though we had planned it.

*What the hell was he talking about?*

Team Leader Choi recovered first and asked Magic Johnson,

“This is the first we’ve heard of this. Mr. Johnson, could you tell us what happened?”

“It’s exactly as I said. The monster armies pulled back during the night. When we looked into it, the same thing had happened on every front.”

“But we didn’t detect any movement on our side.”

“Ah, let me correct that. This western front is the exception.”

“Why?”

“What? Hahaha!”

Magic Johnson slapped my shoulder with a hearty laugh before continuing.

“Because this western front has penetrated deepest into enemy territory. I don’t know what kind of scheme the Arch Lich is plotting, but the western front is already an open highway. They’ve already retreated as far as they can.”

“Oh.”

I had momentarily forgotten.

Unlike the other fronts, which were advancing little by little under Army and Air Force cover, I had simply killed and smashed everything in my way as I pushed forward.

*I did break through with unstoppable momentum, but was it really this much?*

Magic Johnson laughed loudly at my bewildered expression.

“That’s not very Genghis Khan of the twenty-first century. You’ve accomplished an incredible military feat, so why don’t you smile a little?”

“It’s far too early to relax and smile. But putting the monster army’s retreat aside, why are you here?”

“I came to see Choi.”

“……!”

“……!”

“I’m kidding.”

*Look at how pale Team Leader Choi’s face has become. If Magic Johnson makes one more joke, his sphincter might rupture.*

“Since I’m pulling some personnel away for a while, I had to deliver written orders to the commander.”

“You’re pulling them away? Where?”

“Chengdu. A military conference has been convened.”

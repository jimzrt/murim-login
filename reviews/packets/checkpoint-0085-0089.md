# Checkpoint Review — 85–89

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

# Chapters 85–89

## Plot

In the Boss Zone of The Minotaur’s Labyrinth, Im Changsoo plans to exploit Taekyung’s apparent interest in Song Song and use the Level 70 Minotaur Warrior to humiliate him. Taekyung instead kills the boss with a single spear technique, completes the B-rank Gate Clear Quest, and receives a Level Up and its undisclosed reward. Song Song declines his attempts to invite her to dinner.

After the raid, Changsoo transfers the wagered four billion won to Taekyung. His father, Im Chunsoo—the A-rank Guild Master of Sangdong Guild, known as Frozen—learns that Changsoo transferred eight billion won in total, fires him, and begins beating him with an ice club.

Taekyung visits his sick sister Hayeon and discovers that their mother, Kim Jeonghee, has been secretly working in a restaurant. When the restaurant owner insults Jeonghee and attacks Taekyung, he reveals his C-rank Hunter status and has Changsoo confirm both his identity and payment. Jeonghee quits and leaves with him.

At home, Taekyung uses Circulate Qi for Healing on Hayeon and Jeonghee, curing Hayeon’s fever and headache and greatly improving his mother’s condition. He gives each of them a Lesser Potion from his reality Inventory. After learning that Taekyung earned four billion won, Hayeon asks whether she can drop out of school.

## Continuity

- Taekyung killed the Level 70 Minotaur Warrior in one blow, completed the B-rank Gate Clear Quest, leveled up, and received its reward in his reality Inventory.
- Im Changsoo paid Taekyung the promised four billion won.
- Im Chunsoo is Sangdong Guild’s founder and A-rank Guild Master, known as Frozen and for his exceptional ice magic. He fired Changsoo and violently confronted him after discovering Changsoo’s eight-billion-won transfer.
- Kim Jeonghee quit her restaurant job after the owner insulted and attacked Taekyung.
- Kim Minsu is the owner’s son, a D-rank Hunter in Sangdong Guild, but Changsoo does not know him personally.
- Taekyung can safely use the Jin Family’s Cultivation Technique to perform Circulate Qi for Healing on others.
- Hayeon and Jeonghee recovered substantially after receiving the treatment; Taekyung also gave each a Lesser Potion.
- Taekyung’s reality and Murim Inventories remain separate.
- Hayeon has asked about dropping out of school, but no decision has been made.
- Retaliation by Im Chunsoo or Sangdong Guild, Jeonghee’s next circumstances, and Hayeon’s schooling remain unresolved.

## Translation Decisions

- Render 일섬 as **One Annihilation** and 미노타우로스 대전사 as **Minotaur Warrior**.
- Render 관심법 as **mind-reading technique** and preserve the **barbarian against barbarian** wording for 이이제이.
- Retain **Frozen**, **C-rank**, **D-rank**, **Circulate Qi for Healing**, **Lesser Potion**, and **Third Rate**.
- Retain **ajumma** and **goshiwon** with their established explanatory footnotes.
- Use **Minsu** as Kim Minsu’s short form.
- Preserve the established family addresses **Mom** and **Son**.

## Durable state

{
  "active_continuity": [
    "The party sells The Minotaur's Labyrinth byproducts and Magic Gems to the Administration.",
    "Im Kkeokjeong warns that Sangdong Guild is a powerful local Guild capable of threatening Peace Guild.",
    "Im Chunsoo is Sangdong Guild's A-rank Guild Master and founder, known as Frozen for his exceptional ice magic.",
    "Im Chunsoo learned that Changsoo transferred 8 billion won to two accounts, fired him, and began beating him with an ice club.",
    "Sangdong Guild's Team One Leader brought Changsoo to Im Chunsoo's office, which was closed to visitors for half a day.",
    "Im Changsoo transferred the promised four billion won to Jin Taekyung.",
    "Hayeon knows that Kim Jeonghee was secretly working at a restaurant and asked Taekyung not to find her.",
    "Kim Jeonghee is Taekyung and Hayeon's fifty-year-old mother and had worked in a restaurant kitchen for over a year.",
    "Taekyung's father died when a Gate opened downtown during the Great Cataclysm.",
    "Kim Jeonghee defended Taekyung against the restaurant owner's insults and curses.",
    "Taekyung arrived at the restaurant and called Kim Jeonghee Mom.",
    "Kim Jeonghee quit her restaurant kitchen job after the owner insulted and attacked Taekyung, then left with him.",
    "Kim Minsu is the restaurant owner's son, a D-rank Hunter in Sangdong Guild, and is not known personally by Im Changsoo.",
    "Jin Taekyung is a C-rank Hunter rather than the F-rank Hunter the restaurant owner believed him to be; Im Changsoo confirmed Taekyung received four billion won.",
    "Taekyung can use the Jin Family's Cultivation Technique to perform Circulate Qi for Healing on other people.",
    "Hayeon and Kim Jeonghee recovered substantially after receiving Circulate Qi for Healing from Taekyung.",
    "Taekyung's reality and Murim Inventories are separate.",
    "Hayeon learned that Taekyung earned four billion won from the previous day's raid and asked whether she could drop out of school."
  ],
  "continuity_sources": [
    89
  ],
  "open_questions": [
    "Whether Im Chunsoo or Sangdong Guild will retaliate against Peace Guild remains unresolved.",
    "What will happen to Kim Jeonghee after leaving the restaurant remains unresolved.",
    "Whether Hayeon will actually drop out of school remains unresolved."
  ],
  "safe_through": 89,
  "temporary_decisions": [
    "Use Frozen for 프로즌 and preserve the tiger-father/dog-son wordplay in 호부견자.",
    "Use ajumma for 아줌마 with an explanatory footnote.",
    "Retain goshiwon with an explanatory footnote.",
    "Use Minsu for 민수 as the short form of Kim Minsu.",
    "Render 운기요상 as Circulate Qi for Healing.",
    "Render 하급 포션 as Lesser Potion."
  ],
  "version": 1
}

## Reading copies

## Chapter artifact 85

# Chapter 85

“Changsoo hyung. Are you okay?”

“Were you hurt?”

At his team members’ questions, Im Changsoo clenched his teeth.

“Shut up, you bastards. After everything I’ve done for you, you’re just standing around watching?”

“No, it’s just…”

“The situation was a little complicated then. I’m sorry.”

“You disloyal bastards.”

They weren’t bound together by loyalty, but Im Changsoo thought he had given them what they were due and received what he was owed in return. Who had been the one to force the training-camp washouts into the Guild, buy them cars, and give them spending money?

He had received their loyalty in exchange…but being abandoned at the most important moment felt like a stinging blow to the back of the head.

*Fuck, what kind of bullshit is this?*

Several billion won? It was certainly a large amount of money, but it wasn’t beyond Im Changsoo’s means. He could pay it in full by selling just one or two buildings registered under his name.

But he couldn’t tolerate having his pride trampled.

*That bastard deserves to be beaten to death.*

Im Changsoo glared at one person’s back with wide-open eyes.

That bastard in the black leather armor—Jin Taekyung—was the root cause of everything.

*I don’t know where he came from or what he was doing before this…but I’ll make him pay for this humiliation.*

He still didn’t know exactly what Taekyung’s identity was. The one thing he knew for certain was that Taekyung was no ordinary C-rank Hunter.

There wasn’t a single C-rank Hunter in the world who could crush eight B-rank monsters in a head-on fight.

*Why is he hiding his identity? Is he a fugitive criminal? Or someone with a fraudulent registration? The moment we get out of this Gate, I’ll dig up every last thing about him.*

It was at that moment that Jin Taekyung suddenly turned his head toward him and narrowed his eyes.

The predator’s gaze, fixed on its prey, made Im Changsoo’s heart drop.

“Hey.”

“Y-yes?”

“You were just cursing me in your head, weren’t you?”

“N-no, I didn’t.”

“Don’t give me that. The way you stammered gives it away. No wonder the back of my head has been prickling since earlier.”

Im Changsoo recalled the words of his father, a Hunter and war hero from the Great Cataclysm era.

*The more dangerous the situation, the more calmly you have to deal with it.*

“I really didn’t.”

“My mind-reading technique says you’re lying.”

“Mind-reading? There’s no such thing.”

“There’s magic, so why not mind-reading? Let go of your hidebound thinking.”

“Regardless, I swear I didn’t.”

“No, I swear you did. And you’re getting one too.”

Bonk!

Tears sprang to Im Changsoo’s eyes.

It was a forehead flick. He hadn’t even been hit by his father since turning twenty. And now, in front of his team members and several women, he had suffered this humiliation at the hands of someone who looked barely his age.

“Not bad. The feel is exactly like when I hit Hyuk Mujin. Anyway, watch yourself, okay?”

Im Changsoo didn’t know who Hyuk Mujin was, but he lowered his head anyway.

“…Yes.”

“But this damn labyrinth really doesn’t end. Hey, how much farther to the Boss Zone?”

“I don’t know. It’s a labyrinth.”

“And no more monsters are coming out. I’m bored to death.”

“…”

*Of course they aren’t coming out when you beat down every single one you see!*

Im Changsoo and his team didn’t even need to step in. Those five were more than enough. No, Jin Taekyung alone was enough.

*What a monster. Is he really an A-rank Hunter?*

Taekyung alone seemed to have brought down more than thirty monsters. Just when it seemed like he was getting tired, he would suddenly start flying around again.

*The raid is getting faster.*

Normally, a raid slowed down toward the end as fatigue accumulated.

But the raid was getting faster even though they were fighting the same monsters…

*Is he getting stronger the whole time?*

Im Changsoo desperately rejected the thought that had flashed through his mind.

*What is he, a game character leveling up? How could that make any sense?*

Getting hit on the forehead must have broken his brain.

“Hoo.”

As Im Changsoo let out a deep sigh, his team members approached him hesitantly.

“Changsoo hyung…”

“Oppa, are you okay? What do we do? You’ve got a bump on your forehead.”

“I’m in a bad mood, so get lost. The moment you leave, you’re all fired. Got it?”

No matter how badly his dignity had been crushed, even a tiger with its teeth pulled was still a tiger.

His team members swallowed nervously at Im Changsoo’s threat.

*My car payments aren’t even finished.*

*Where will I get accepted if I leave Sangdong Guild?*

*My credit-card bill this month…*

The reason they had been able to enjoy such comfortable lives was Im Changsoo’s support. Since they were all Hunters, they weren’t going to starve to death, but wherever they went, it would be difficult to expect the same treatment.

“You think you’re getting away with it just because you’re leaving? Just wait. Wherever you go, I’ll make sure to place a call in Sangdong Guild’s name. You know this field is small, right?”

At the threat that he would not only drive them out but also ruin their futures, their expressions changed completely.

“Changsoo hyung, that’s going too far.”

“Hyung? I’m only hyung when things are going your way?”

“Oppa, do you really have to take it that far?”

“That’s why you bastards should’ve picked the right person to hitch your wagon to.”

He wanted to slap every one of them across the face, but he forced himself to hold back.

If he raised his voice again, there was no telling when Jin Taekyung might turn around.

*Fuck, how did I end up…*

What kind of pathetic situation was this, being too afraid of a forehead flick to even get angry properly?

Im Changsoo spat on the floor and turned away.

That was when someone grabbed him.

“Changsoo hyung. No, Team Leader Im, you can’t do this.”

“Think it over one more time, oppa. Please?”

“Let go. I don’t want to say it twice.”

“This time, for real. I’ll do everything you tell me. Okay?”

“…Everything I tell you?”

Im Changsoo, who had been about to pull away from his colleague’s hand, suddenly stopped.

He glanced back and saw Jin Taekyung’s group far ahead of them. They had gotten some distance away while he was arguing with his Guild members.

Even from that distance, Song Song’s stunning figure from behind was impossible to miss.

*Wait. Maybe there is a way.*

To Im Changsoo, Jin Taekyung looked like a monster—but he seemed to have one weakness.

A woman named Song Song.

*He was completely smitten earlier.*

There was no need to be perceptive about it. Anyone could tell from a single glance that Jin Taekyung had feelings for Song Song.

*She said she was a C-rank healer, right?*

Subduing a healer was easier than twisting a chicken’s neck. If the woman he liked were being held hostage, Jin Taekyung wouldn’t be able to act freely.

*Then it’s over.*

Apart from Taekyung, the other three weren’t much of a concern.

The old man who was supposedly the Guild Master was a B-rank Hunter, but he was a mage, so close combat would be his worst area. The middle-aged man who was an E-rank tank wasn’t even worth discussing.

The only person who bothered Im Changsoo a little was Choi Minwoo. That guy…

“Can I trust what you just said?”

“Of course.”

“Just trust us.”

“Oppa, why don’t you trust people at all? Are we really only this close?”

Im Changsoo had a raid team made up of four B-rank Hunters and five C-rank Hunters who would obey his commands. They were all people he had trained to live solely on the scraps he handed them.

“Fine. Then listen carefully to what I’m about to say…”

After a short and simple explanation, the team members couldn’t hide their nervousness.

“Will it work?”

“It does seem possible.”

“Oppa, it’s not what I think it is, right? If you’re talking about killing someone, I’m not sure I can.”

“Didn’t you say you’d do everything I told you?”

“Even so, that’s a little…”

“Forget it. I’d like to do that, but I’m not reckless enough to go that far. First, we take the camera. Then we give that son of a bitch a humiliation he’ll never live down.”

“Whew. What a relief. Then I’m definitely on oppa’s side.”

“Do your best. You know what happens if anyone hesitates this time or holds back even a little, right?”

“Of course.”

“Just trust us, Team Leader. No, hyungnim. Hehe.”

A sinister smile spread across Im Changsoo’s lips.

*If he trampled on my pride, he has to pay the price.*

In the Boss Zone they were about to enter, Im Changsoo intended to make Jin Taekyung understand exactly whose toes he had stepped on.

There was even a monster there capable of standing against Jin Taekyung.

*The Minotaur Warrior.*

The boss monster of **The Minotaur’s Labyrinth**.

Despite being only a B-rank monster, it was a monstrous creature whose physical abilities rivaled those of an A-rank.

*Once the Minotaur Warrior wears him down, we’ll make our move.*

Set a barbarian against a barbarian.

Defeat a monster with a monster.

The moment both sides were exhausted would be their opportunity. He could recover both the money he was about to lose for no good reason and the pride that had been dragged through the dirt.

“Hey, hurry up! This is the Boss Zone!”

Jin Taekyung’s shout rang out the next moment.

Im Changsoo smiled broadly.

“Yes! Coming!”

His steps toward the Boss Zone were remarkably light.

* * *

“One Annihilation.”

Kraaaaaash!

From the tip of the spear came the sound of the sky splitting apart.

A white vortex that tore through and devoured everything it touched slammed into the muscular chest of the Minotaur Warrior.

—Moo?

Crack-crack-crack!

There was no need to check whether it was alive or dead.

The moment I pulled my spear from its chest, the System notification rang out.

Ding.

> **System**
>
> - Defeated **Lv. 70 Minotaur Warrior**!
>
> - Level Up!
>
> - Quest, **B-rank Gate Clear**, completed!
>
> - Calculating your contribution… Complete!
>
> - The Quest Success Reward has been deposited into your Inventory!

“Whew.”

The last one should always end with one big hit.

My body was incredibly tired, though.

I shook the blood from my spear and turned around.

“Let’s collect the byproducts and get out of here. I’m starving to dea—why are you all looking at me like that?”

Im Kkeokjeong spoke for everyone.

“You really have to ask?”

He looked back and forth between the dead boss monster’s corpse and me.

His eyes demanded some kind of explanation for how I had finished a B-rank boss monster with a single blow.

“Hmm. Let’s just say I got lucky.”

“Lucky?”

“Yes. Lucky.”

It really was because I had been lucky.

The fact that I had lived in a goshiwon.[^1] The fact that a capsule had been discarded in front of my goshiwon.

All of it.

“Good grief. I’m speechless. Fine.”

The others reacted much the same way as Im Kkeokjeong. Even Team Leader Choi, who had already experienced a raid with me, addressed me with a stunned expression.

“I didn’t expect you to be this capable.”

“If you know now, that’s enough.”

“Could we discuss this?”

“Of course.”

Not now. Later.

I still had something more important to take care of.

With my most charming smile, I approached one person.

“Miss Song, could I ask you for a heal—what are you guys doing over there?”

“Ah.”

“What are you doing? Why are you here?”

“We’re just… just standing here.”

“I-I just think she’s so beautiful.”

The Sangdong Guild members who had been standing next to Song Song jumped in surprise and began spouting all kinds of nonsense.

*What’s wrong with these guys?*

I only meant that they should get lost because they were getting in the way between me and Miss Song.

*Do I really look that scary?*

“Where’s Im Changsoo?”

At a single word from me, the Sangdong Guild members split apart like the Red Sea.

Im Changsoo answered from behind them, his face white as a sheet.

“I’m here.”

“What’s wrong with your face? Are you sick?”

“I-I think I’m coming down with something.”

“Tsk, tsk. Take a potion, you idiot. You’ve got plenty of money at home.”

“…”

“Anyway, hurry up and collect the byproducts. Let’s go. I’m tired.”

“Yes, yessir.”

Once Im Changsoo disappeared with the nuisances, the moment I had been waiting for finally arrived.

I smiled brightly at Song Song.

“You’re hungry, right? How about steak at a nice restaurant for dinner?”

Song Song smiled back at me.

“I’m sorry, but I’m a vegetarian.”

“That’s strange. I thought you ate meat just fine yesterday. How about a salad bar?”

“I’m a carnivore.”

“…”

*I got rejected, right?*

[^1]: A goshiwon is a very small, inexpensive room-for-rent housing arrangement, often used by students and people on tight budgets.
## Chapter artifact 86

# Chapter 86

“Oh, thank you for your hard work.”

The government official in charge came rushing out to greet us.

Well, more accurately, he came to greet Im Changsoo.

After meticulously checking all the byproducts and Magic Gems we had brought, he made a fuss.

“Wow, that’s an incredible amount. There can’t be many Minotaurs left in the labyrinth after this.”

“…”

Im Changsoo’s face was pale. He only nodded without answering, making the official glance around uneasily.

“Team Leader, are you feeling unwell?”

Since when did government officials start worrying about Hunters’ health?

Before he could say anything unnecessary, I jabbed Im Changsoo in the ribs.

“You have to answer him. Chang. Soo.”

“Um… No, I’m fine.”

“Ah, that’s a relief, then.”

Maybe he had sensed the strange atmosphere. The official looked at me suspiciously, but that was as far as it went.

“How would you like to handle the byproducts? As you know, there are two methods.”

As the official explained, there were two ways to sell byproducts.

Personal sales and consignment sales. With the former, the individual owner of the goods handled the transaction personally. With the latter, the goods were entrusted to the Administration, meaning a government agency, for sale.

*Each method has its pros and cons.*

Rare items sold better privately. For everything else, handing it over to a government agency was less of a hassle. It was like the difference between a luxury auction and a market auction.

“What should we do?”

At Im Changsoo’s question, Butler Kim stepped forward. He hadn’t once taken the lead during this Gate raid, but he was still a veteran Hunter. When it came to this sort of thing, he probably knew more than anyone else here.

“We’ll sell them to the Administration.”

They said there was nothing to waste from a cow. The same went for Minotaurs.

Their hides were used to make Equipment, their bones were boiled down into restorative food, and their horns were popular collector’s items among enthusiasts.

“You made the right choice.”

The government official began calculating the byproducts with an expression of pure delight. The Administration was the one buying them, so the reason he was happy was obvious.

*He must be getting a little something off the top.*

Still, whatever the official skimmed off wasn’t my concern.

The cut I was getting today was much bigger.

Tap, tap.

“What about the agreed-upon amount?”

Im Changsoo answered with a rigid expression.

“I-I’ll pay it.”

“By when?”

“I’ll send it by tomorrow.”

Four billion won by tomorrow? The son of a rich family certainly knew how to be decisive. I smiled broadly and handed him a slip of paper.

“Well, that works for me. Here’s my account number. Keep it safe as if it were an heirloom, then send the money tomorrow. It won’t be funny if you say you lost it later. Got it?”

“…Yes, sir.”

That should be enough, right? I said goodbye by giving Im Changsoo a light pat on the back.

As I watched with satisfaction as he staggered away, Im Kkeokjeong asked me,

“Do you think that punk will actually pay?”

“What happens if he doesn’t?”

“You know… it could get a little awkward. Sangdong Guild is a mid-tier Guild with some serious influence around here. If he decides to brazen it out and refuses to pay…”

“Come on, we have video evidence. Surely he wouldn’t.”

“Evidence can be destroyed. More importantly, I’ve heard a few things.”

“Like what?”

Now that he had put it that way, I was starting to get a little worried.

Kkeokjeong glanced around, checking everyone’s reactions, then leaned in and whispered,

“You know who the Sangdong Guild Master is, right?”

“Yes. I heard his name for the first time today, though.”

Im Chunsoo. For some reason, the name brought to mind a middle-aged man with a bulging drinker’s belly, but reality was the exact opposite.

“He’s an A-rank Hunter who made an impressive name for himself during the Great Cataclysm. What do people call him again? Fro… Fro… It’s suddenly slipping my mind.”

“Frozen.”

“Ah, right. Frozen. A mage specializing in ice magic.”

Famous Hunters were often given nicknames to match their abilities.

The same was true of Im Chunsoo. An A-rank Hunter, he had made a name for himself as a mage during the Great Cataclysm. He was particularly skilled with ice-related magic, which had earned him the nickname Frozen.

“When it comes to ice magic, that man is one of the top five in Korea. He used that Fame to build Sangdong Guild into what it is today.”

When the brutal Great Cataclysm finally came to an end, the first-generation Hunters faced a choice.

Retire, or remain active.

Im Chunsoo chose the latter and founded Sangdong Guild.

“That’s impressive. His son doesn’t seem like much.”

Even among A-rank Hunters, it was rare for someone to survive the Great Cataclysm with nothing but their bare fists and gain both wealth and fame. Im Chunsoo’s present was the future many Hunters dreamed of.

“Impressive? It certainly is—the power of bloodlines, that is.”

Kkeokjeong jerked his chin toward Im Changsoo’s retreating back.

“Don’t forget whose blood that punk inherited.”

“What does that…”

“I’m not bragging, but I’ve been in this business for over twenty years. Sangdong Guild was founded when I was still a complete rookie.”

“And?”

“Bucheon was just as fiercely competitive between Guilds back then as it is now. There was no room for a new Guild to squeeze in.”

“But Im Chunsoo broke through anyway?”

“That’s right. That’s why he’s a frightening man.”

“Hmm.”

Did that really mean so much?

Competition between Guilds was nothing new, and in a merit-based society, it was only natural for the capable to survive.

“A man like him would have had excellent abilities as a Hunter and plenty of Fame. He must have had powerful connections, too.”

“Do you think the other Guild Masters didn’t?”

“What?”

“They might have had slightly less Fame than Im Chunsoo, but every one of them had been a war hero. They had entered the market several years before Sangdong Guild and occupied a substantial number of Gates.”

Kkeokjeong continued in a low voice.

“It was a time when all kinds of illegal activity ran rampant because the system hadn’t been fully established yet. The only reason Sangdong Guild exists today is that Im Chunsoo crushed every one of his competitors. He’s no pushover.”

A thought suddenly flashed through my mind.

What would happen if Im Chunsoo found out about what had happened today? How would he react to hearing that his only son had been utterly humiliated?

*This could get complicated.*

When you talked about Korea, you couldn’t leave out connections through school, region, and blood.

Sangdong Guild had held its ground for twenty years. If it was a local power, our Guild was practically a newborn.

If Sangdong Guild came at us in earnest, they’d tear up our birth certificate before we even got started.

“Is the Sangdong Guild Master a nice person, at least?”

“I wouldn’t know. I’ve only heard rumors.”

“Tell me what you’ve heard.”

After thinking for a moment, Kkeokjeong answered,

“Seeing Im Changsoo today reminded me of an old saying. A tiger father and a dog son.”

“A great father and a worthless son? That’s still a compliment, isn’t it? Is he the kind of person you can reason with?”

“No. Try interpreting it literally.”

“…A tiger for a father and a dog for a son?”

“If Changsoo’s personality is that of a son of a bitch, then Im Chunsoo is a tiger. I hear his temper is absolutely fucking terrible.”

“…”

“I’ve also heard that he mellowed out with age, but can a person’s temper really change that easily?”

*For fuck’s sake.*

The more I heard, the colder my spine felt. I had the distinct feeling that something was about to go horribly wrong.

*Damn it. I shouldn’t have made that bet.*

My excitement at the thought of receiving several billion won had lasted only a moment. Now I felt uneasy, like I had taken a huge dump and forgotten to wipe.

I didn’t care what happened to me, but I absolutely refused to let the other Guild members get hurt.

“Taekyung, don’t worry about it too much. I only brought it up just in case.”

“I didn’t just cause trouble, did I?”

“It’ll be fine. Team Leader Choi thought it would be fun and joined the bet, too.”

“Oh, right.”

“Exactly. And look at the way Im Changsoo acted. If I were his father, I would’ve beaten him half to death. He’d be too embarrassed to tell anyone about it.”

He had a point. What could possibly happen?

Hearing that made me feel considerably lighter. I even found myself smiling.

“Thanks, Kkeokjeong ajusshi. No, hyungnim.”

“Then buy us some beef to celebrate becoming a rich man. Wait, no. You should eat it with Miss Song, not me.”

“…Ah.”

He was driving a nail straight through my heart.

As Im Kkeokjeong killed me with words for the second time, I swallowed my tears.

* * *

“What brings you here?”

The speaker was a man with a distinctive appearance.

He was nearing fifty, but his skin was taut and his wiry, spiky hair was black. His large, piercing eyes were enough to make anyone’s knees go weak.

*What the hell is with that look in his eyes…*

The manager of a K Bank branch was no exception. He had already met the man several times, but he was an ordinary person, while the other man was an A-rank Hunter—a living witness who had endured the Great Cataclysm with his entire body.

His tongue tied itself in knots, and cold sweat trickled down his back.

“Well…”

“If you came to waste my valuable time, go back. Otherwise, speak now.”

The words were sharp, but his tone was fairly gentle.

The manager had heard the rumor that Im Chunsoo was trying to mellow his temper with age. Apparently, it hadn’t been a complete waste of effort.

*Damn it.*

The branch manager steeled himself and blurted out,

“I’m sorry, Guild Master. I’ve come regarding your son.”

At the mention of his son, Sangdong Guild Master Im Chunsoo’s eyebrow twitched.

“Changsoo? What about him?”

“Some time ago, you asked me to let you know whenever your son used any of the bank’s services…”

Im Chunsoo nodded as if he understood.

“What is it this time? Did he steal my seal? Or take out a loan against collateral?”

“He transferred a considerable amount of money all at once.”

“He must be fooling around with women again. Obviously. How much?”

“Four billion won to each of two accounts. Eight billion won in total.”

“How much?”

“Eight billion… Hup.”

The branch manager hurriedly swallowed his breath. He had just watched the window behind Im Chunsoo rapidly freeze over.

Hiss.

It was late summer outside, but the office was suddenly ruled by cold and frost.

Im Chunsoo gestured at the trembling branch manager.

“Anything else?”

“I-I brought the relevant documents.”

With shaking hands, the branch manager placed a stack of papers on the desk.

“Good. You may leave.”

“I-I’ll see you next time.”

After the branch manager fled the room, Im Chunsoo picked up the receiver. The phone had a cold-resistance function, so it transmitted the signal without any problems.

Beep, beep. Click.

—Yes, Guild Master. Team One’s Leader speaking.

“Bring that bastard here immediately.”

—…Do you mean Team Leader Im Changsoo?

“Team Leader, my ass. He’s fired as of today. Bring that bastard here now!”

Bang!

The receiver’s life ended there. Ice shattered into hundreds of pieces and covered the desk.

“What a pathetic fool. Even after I warned him…”

Im Chunsoo glared coldly at the wrecked office, then his gaze stopped on one spot: the stack of papers left behind by the K Bank branch manager.

There was no doubt that the documents contained the whereabouts of eight billion won.

*You stupid bastard. Which woman did you fall for this time?*

He read through the papers, turning them one page at a time, for more than ten minutes.

When Im Chunsoo closed the final page, the door flew open with the sound of someone being dragged along.

“Team Leader Im Changsoo. I brought him here.”

An affable-looking middle-aged man stood there. In his firm grip was a young man.

“F-Father!”

“My proud son has arrived.”

At his son’s appearance, the father extended a hand.

Of course, it was not meant as a gesture of forgiveness.

Crackle, crackle, crackle.

Cold surged from Im Chunsoo’s grasp. It changed from gas to liquid, then from liquid to solid, completing its transformation into an ice club as hard as steel.

“I have a lot to ask you, but first, you’re getting hit.”

“Father!”

“Shut up, you little shit!”

The middle-aged man who had brought Im Changsoo there—the Team Leader of Sangdong Guild’s Team One—quietly closed the door.

For the next half a day, no one was allowed to enter.
## Chapter artifact 87

# Chapter 87

“Achoo!”

Rattle, rattle!

Jinho hyung calmly wiped his face with a wet tissue after getting covered in ramen and grains of rice.

“If you don’t like it, say so. Use words.”

“It’s not like that. It just came out of nowhere.”

“Don’t make excuses. You look even more pathetic.”

But I was telling the truth. Instead of answering, I rubbed my nose.

*Is someone badmouthing me?*

*Now that I think about it, there is someone who might have reason to.*

If it was Im Changsoo, he had more than enough motive. His motive was overflowing. Still, he was the Santa Claus who had given me four billion won, so I was happy to take a few insults.

*I wondered if he would, but the bastard actually kept his promise.*

I remembered the text message I had received that morning. The banking app installed on my smartphone notified me of every deposit and withdrawal without exception.

> Jin Taekyung’s 110-***-*** account has been credited with 4,000,000,000 won.

The only minor incident was that Jinho hyung had been the first to discover it. Leaving my smartphone in my room when I went to take a shower had been a mistake.

“You’ve got plenty of money, so why are you eating ramen?”

“You sure are talkative. I put beef in it. You don’t like beef ramen?”

“That’s not what I mean, you punk.”

Bang!

Jinho hyung roughly set down his utensils.

Of course, he hadn’t done it to make a point. He was just full.

“I mean, you’ve got four billion won in your bank account, so why are you eating ramen in a goshiwon?[^1]”

“What’s it to you? I’ll do what I want.”

“…That’s true.”

“And the money only came in an hour ago, all right? I don’t know what to do with it either, so be quiet and let me think.”

I was pretending to be fine, but I had been dazed for a while. I had worked myself to the bone like a worker ant, but the money had always been earmarked for something.

Then a fortune had dropped out of the sky.

Four billion won was enough money to do a lot of things. Naturally, a lot of thoughts followed.

“What are you thinking so hard about? There must have been something you wanted to do first as soon as you got money.”

The thing I wanted to do first…

*There is one thing.*

Slurp.

After sucking in the last strand of noodles, I stood up.

Before leaving the room, I didn’t forget to leave Jinho hyung one parting remark.

“Thanks.”

“Don’t mention it.”

“Don’t forget to wash the pot. I’m off.”

“Hey, hey!”

* * *

“Huh?”

Hayeon’s eyes went round when she saw me standing in front of the front door.

“So it really is you. I saw you on the intercom screen and thought, no way.”

“…If it wasn’t really me, what would I be?”

“Hmm. A graphic?”

“Is that any way to talk to your older brother after not seeing him for so long?”

“What are you talking about? You came the day before yesterday.”

Ah, right. Not much time had passed in the real world.

The time difference was so large that I sometimes got confused myself. As I took off my shoes, I asked,

“What were you doing?”

“Studying.”

“Come to think of it, what about school? It’s a weekday.”

Hayeon answered in a nasal voice.

“They said my fever was thirty-nine degrees. I stuck it out until second period, then left early. Summer vacation starts tomorrow anyway, and we’ve been doing nothing but self-study lately.”

“You’re already on vacation? No, wait. You left school early because you were sick, and you’re studying?”

Somehow, she seemed more impressive than a Peak master. Whenever I got really sick at school, my illness mysteriously disappeared as soon as I left early and came home.

She had a raging fever, and she was still studying. Was her DNA different from mine?

“There is no end to learning.”

Leaving Hayeon, who sounded like a school disciplinarian, behind, I entered the living room. Apart from the two of us, there wasn’t a sign of anyone else in the house.

“Where’s Mom?”

“The bank.”

“You answered that awfully quickly.”

“It’s true.”

“Did Mom tell you to say that?”

“Huh? Tell me to say what?”

I wondered who she took after. Her acting was so natural that if I hadn’t known the truth, I would have been completely fooled.

*I should have told her long ago.*

A bitter smile escaped me before I could stop it. As I turned back toward the entrance, Hayeon grabbed me.

“Where are you going?”

“To find Mom.”

“There’s more than one bank around here. I’ll make you something to eat, so wait here. She’ll be back soon.”

“It’s fine. I’m not going to the bank.”

“What?”

“The restaurant at the intersection in front of the supermarket. Right?”

The strength slowly drained from Hayeon’s hand.

“…You knew?”

“Yeah. For a long time.”

“Mom asked me to keep it a secret.”

“I know that too.”

“Oppa, can’t you stay?”

It was one of Hayeon’s longtime habits. Whenever she had an important favor to ask, she always put *oppa* first.

“I’ll be back.”

I ruffled Hayeon’s hair and left the house.

As the elevator carried me down, I quietly thought about her warmth still lingering in my hand—and why she was studying even while her forehead was burning up.

* * *

A person had only one name written on their resident registration card, but they could be called by many names over the course of their life. Kim Jeonghee, who had turned exactly fifty that year, was no different.

“Ajumma, two more servings of pork belly over here.”

“Yes, just a moment.”

The name she was called most often these days was *ajumma*.[^2] Before that, it had been “Hayeon’s mom.” Before that, “Taekyung’s mom.” Once the children had grown up and work had become busy, those names had disappeared from her life.

The one person who had called her by her real name had already passed away long ago.

*Jeonghee.*

She had met him when she was twenty-two. He had been kind and affectionate. During the chaotic period of the Great Cataclysm, the two of them met in a shelter and fell in love at once.

It had been a happy marriage. Even as the years passed, he continued to call her by name.

*Jeonghee.*

Sometimes, embarrassed to hear him call her by name in front of other people, she had asked him about it.

*Why do you only call me Jeonghee? Other husbands call their wives “so-and-so’s mom,” “honey,” or “the missus.” That’s what everyone else does.*

*Does it bother you?*

*No, it’s not that. I was just curious. We’re getting older too.*

*What does age have to do with it? I call you Jeonghee because I love you as Jeonghee more than I love you as Taekyung’s mom.*

*Why are you acting like this in front of the kids?*

*Uh-oh, Mom’s cheeks are red. Mom and Dad, do you wrestle in the mornings too? You do it every night.*

*…Taekyung, starting today, go to bed early.*

Their parting came earlier than expected. Without warning, a Gate opened in the middle of downtown. The two children lost their father, and she lost her husband—the one person who had been the only one to call her by name.

“Ajumma!”

Kim Jeonghee jolted back to reality. A middle-aged woman with permed hair and flashy earrings was glaring at her.

“Oh, yes, ma’am.”

“What were you doing that you couldn’t even hear me calling you?”

“I’m sorry.”

“What about the grill plates? Are you done washing them?”

“Well, the thing is…”

Her hands had stopped while she was lost in thought. The owner checked the sink and raised her eyes sharply.

“Ajumma, are you going to work like this?”

“…”

“Honestly. If this is how you’re going to do things, I should do it myself. Why would I pay good money to hire you? Am I wrong?”

Kim Jeonghee lowered her head, while the other kitchen workers continued what they were doing, pretending not to hear the owner’s voice.

*Good money, my ass. She works us at minimum wage during the busiest hours.*

*She’s old enough to know better. She knows perfectly well that no amount of caked-on makeup and dressing up will make her a match for Jeonghee ajumma, so she’s taking it out on her.*

*She should watch the counter properly herself in the first place. How many orders did Jeonghee receive while she was off having fun?*

There were many things they wanted to say, but they could only keep them to themselves. The kitchen ajumma who had finally lost her patience and stood up for Kim Jeonghee had been fired last week.

“Can I really leave this place with you in charge?”

“…I’m sorry.”

“I heard your son is a Hunter. He should be making decent money, so why don’t you just stay home and cook? Why come all the way here and be a nuisance to someone else’s business? Ah, is his income not very good because he’s an F-rank Hunter?”

The moment a sneer appeared at the corners of the owner’s mouth, Kim Jeonghee slowly raised her bowed head.

“Boss. That was too much.”

“What?”

“I said you went too far.”

“Are you saying I was wrong?”

“Yes.”

The unfamiliar sensation left the owner speechless. Kim Jeonghee had always been quiet and gentle, but now her eyes had sunk into a deep, cold stare.

“Please apologize for what you just said.”

“A-apologize?”

“Right here. Right now.”

“O-oh my. Fine. Which part of what I said was wrong? Your son really is an F-rank Hunter!”

“Is his rank really that important?”

“Of course it is. What good is an F-rank Hunter? A son like mine has to make good money and have women lining up for him. This shop, too…”

“Your son, the D-rank Hunter, set it up for you. I know. I’ve heard it dozens, if not hundreds, of times.”

The employees, who had pricked up their ears, unconsciously nodded.

The owner’s boasting about her son was a familiar routine they heard several times a day.

How much he made, how big his house was, what kind of car he drove, and how filial he was—so filial that he had even opened a shop for his mother to have something to do. She had repeated it so often that even the regular customers were sick of hearing it.

“Then you know all about it. I run this place as a hobby, but you’re different, aren’t you? You’re working in the kitchen because your son doesn’t make enough money, aren’t you?”

“No, that’s not it.”

Kim Jeonghee continued calmly.

“Our Taekyung grew up right. He never once caused his parents any trouble, even when he was little. He’s still working hard for his family. Money? He earns more than enough.”

“That’s all an excuse.”

“An excuse? This is money my child earned by risking his life. How could I, as his parent, accept it and spend it?”

“Ajumma, are you saying that for my benefit?”

“That depends on how you choose to take it. And since we’re on the subject, when does that amazing son of yours ever show his face?”

“What?”

“I’ve worked here for over a year, but that devoted son of yours hasn’t visited even once. He does at least call you, doesn’t he?”

The kitchen fell silent as death. The owner’s face turned bright red, and her eyes widened.

“Where does a bitch with such a pathetic son get off—”

The employees knew what was coming next. Along with the owner’s machine-gun burst of abuse, the word “fired” was bound to come flying out.

But none of them could have predicted Kim Jeonghee’s reaction.

“Watch your mouth, you goddamn bitch.”

“…”

“…”

It was as if a bomb had gone off.

A deathly silence descended, and everyone’s eyes shook with disbelief. Every person in the kitchen wondered if they had heard correctly.

*What did I just hear?*

*Did Jeonghee ajumma just swear? My God.*

Kim Jeonghee had always been gentle and quick to smile. Even though the owner picked fights with her day after day, she had always bowed her head without a single word of complaint. Now she was glaring at the owner with eyes as cold as ice.

“W-what did you say? What did you just call me?”

“I called you a goddamn bitch, you fucking bitch.”

“Y-you fucking bitch?!”

Before the shock had even faded, a second bomb went off. The owner’s shriek rang all the way out into the dining area.

“Did someone just swear?”

“You heard that too? I think someone just called somebody a fucking bitch.”

“What the hell? Are the employees fighting?”

The murmuring grew louder. Customers and employees alike turned their attention toward the kitchen.

That was when it happened.

Thud. Thud. Thud.

A large young man with his cap pulled low. No one had noticed when he entered, or how long he had been standing there. Not until he started walking toward the kitchen.

“S-sir. I’ll take your order…”

The young man smiled faintly at the male employee who hurried to stop him.

“It’s okay. I didn’t come to order.”

“No, but still, right now…”

“Excuse me.”

Tap.

He had only given the employee a gentle push, but the burly man staggered and fell. The young man pushed open the half-open kitchen door without hesitation.

And then…

“Mom.”

He came face-to-face with the person he loved most in the world.

[^1]: A goshiwon is a tiny, inexpensive room-for-rent housing arrangement, often with shared facilities.

[^2]: *Ajumma* is a familiar Korean term for a married or middle-aged woman, commonly used by customers or employers to address service workers.
## Chapter artifact 88

# Chapter 88

“Son?”

Her eyes widened when she saw me.

My mother was wearing an apron with the restaurant’s name printed on it and a pair of rubber gloves smeared with grease.

My mother.

Her surprised expression soon turned to bewilderment.

“Ta-Taekyung, what are you doing here?”

I gave my flustered mother a broad grin. That was when a shrill voice pierced my ear.

“So you’re the son of Kim ajumma[^2]?”

A middle-aged woman was looking me over warily.

There was no need to ask who she was or what she did. I already knew.

“Hello. My name is Jin Taekyung.”

“Huh? Ahem. Yes.”

The owner gave an unnecessary cough after seeing me bow politely from the waist.

“But what brings you here all of a sudden?”

I answered with a pleasant smile.

“Does a son need a reason to visit his mother?”

“A reason?”

The owner narrowed her eyes.

“Maybe it’s because you’re young, but you’re awfully thoughtless. If someone showed up out of the blue like this, how would you feel if you were the owner?”

“Hmm. I suppose I’d be upset.”

“Exactly!”

“It’s lunchtime, the restaurant is packed, and everyone in the kitchen and dining area is so busy they can barely see straight.”

“…That’s right.”

“And then an employee’s son suddenly shows up without saying a word? From your perspective, Boss, I can understand why you’d be upset. Completely.”

“Y-you do understand.”

*What the hell is this kid?*

That was probably exactly what the owner was thinking.

Ignoring her confused reaction, I grabbed my mother by the arm.

“In that case, we’ll be going now. Mom, go change so we can leave.”

“What?”

“S-son?”

The two of them stared at me in bewilderment.

I asked with an innocent expression,

“Why?”

“What do you mean, why? Why?!”

“Is there some kind of problem?”

“You little punk, are you making fun of an adult? Did you already forget everything you just said?”

“Oh, you mean when I said you might be upset if someone came by while you were busy?”

“Yes! You said yourself that I might be upset, and now you’ve forgotten already? Are you making fun of me right now?!”

“Oh, come on. I’m not making fun of you.”

“Then what is this?”

“What I said before was sincere. From your perspective, Boss, you had every right to feel that way. But…”

I continued with a bright smile.

“My mother isn’t your employee anymore.”

“What?”

“Is that hard to understand? She’s quitting. Starting right now.”

A heavy silence settled over the restaurant.

My mother stared at me blankly, while the owner’s face turned dark red before she shrieked,

“Who said you could do that?!”

“We did.”

“You think I’ll just let you take her away?”

“What happens if you don’t?”

“Y-you!”

“T-three, three! F-four, four!”

That was as far as the owner’s patience went.

“Hey, you fucking son of a bitch!”

The hand she raised along with her vicious curse never reached its target.

Grab!

Someone caught the owner’s wrist in a single motion and glared at her.

My mother spat the words out with an aura fierce enough to make even a First Rate master flinch.

“Whose son do you think you’re laying a hand on, you fucking bitch?”

Good Lord.

I had heard her swear once earlier in the dining area, but this was the first time in my life I had seen my mother curse like this. She never even spoke ill of other people in front of her children, and yet…

“And who are you calling a son of a bitch? Your son is the son of a bitch, you pig!”

“You’ve been getting on my nerves from the start! Hey!”

The owner charged at my mother, but I stepped in front of her.

I was big enough to stand out wherever I went. Simply standing between the two middle-aged women was more than enough.

“Now, now. Calm down. Please calm down.”

“Move! Are you going to move or not? Do you think you’ll get away with this?”

“Yes. I think we’ll live quite comfortably.”

“Gaaaah!”

The owner’s eyes rolled back as she began wildly swinging her arms with a scream.

Of course, none of her attacks posed the slightest threat to me.

*Calling that an attack is embarrassing.*

Compared to the enemies I had faced in Gates and the Murim, her attacks were no more dangerous than the fluttering of a fly’s wings. With my bones, muscles, tendons, and ability to take a hit all dramatically enhanced, even a punch from an ordinary adult man would only tickle.

“Please stop. You look like you’re having a really hard time.”

As expected, the owner’s struggle ended quickly.

She was now in her fifties and morbidly obese; her body clearly had its limits.

“Huff, huff! You Hunter bastard, are you bullying a civilian?”

That she could come out with a line like that—I had to marvel at how the owner’s brain worked.

“Me? Bullying you?”

“Can’t you see that I’m hurt? My fingernail broke and it’s bleeding!”

“You hurt yourself hitting me. I’ve just been standing here, so why are you shaking all by yourself?”

“Whatever!”

This was a bumper crop of bullshit.

I glanced around. The kitchen employees, along with the customers in the dining area, were watching the owner’s stand-up routine with exhausted expressions.

“If you can’t accept what happened, call the police. There must be about fifty witnesses here, so that should work out nicely.”

“…”

“Not going to call? Since you were injured and bled because of a Hunter, you should go to the police station, give a statement, file a complaint, and hire a lawyer. You’ll be busy starting tomorrow.”

I had intended to tease her a little longer, but the more we talked, the more I felt my time slipping away. I clicked my tongue.

“What are you, the mayor? You’re only the owner. Don’t make everyone around you miserable, and try to have a better attitude. We’re leaving.”

I was about to turn around when the owner, her face twisted with resentment, crooked her lips.

“You live in Bucheon, don’t you?”

“So?”

“Which Guild in Bucheon are you with?”

“Would it mean anything if I told you?”

“My son would know. Our Minsu is a Hunter in Bucheon, too.”

“Oh, really?”

“I hear Hunters all know one another after only a degree or two. I wonder how long you’ll last if you get a bad reputation in that line of work.”

“I have a reputation for being hardworking and skilled, so I’ll be around for a long time. Happy?”

“Do you know Kim Minsu? My son must be famous in Bucheon.”

Kim Minsu?

Of course I knew him. Over the past seven years, I had probably crossed paths with more than thirty people named Minsu.

I answered indifferently,

“Do you know Seong Jinho? He’s the most famous person in our goshiwon.[^1]”

“Pfft, a goshiwon? I suppose that’s the level you’d expect from an F-rank Hunter. Is business really that bad?”

“It’s kind of you to worry, but I make a decent living. I made four billion won just yesterday.”

“How much?”

“Four billion won.”

I hadn’t wanted to boast about money like a child, but she just had to tug on a sleeping lion’s nose hairs.

There was one thing I had forgotten, though.

People always made their judgments based on the common sense they possessed.

“Four billion won? An F-rank Hunter made that much?”

“Obviously, he’s bluffing. A Hunter I know said an F-rank Hunter has to work like hell to make even a hundred million won. And did you hear him? He said he made four billion won in a single day, not in a year. It’s not like he won the lottery. Does that make any sense?”

“Geez, I almost thought he was telling the truth.”

The customers in the dining area, along with the kitchen employees who had quietly seemed to be rooting for me, began looking at me doubtfully.

Well, even I had to admit it sounded absurd.

“Son, is that true?”

My mother’s eyes went round.

The owner snorted.

“As if it’s true. Even my Minsu can’t make that much.”

“I’ve been wondering. What rank is this famous Minsu of yours? A-rank?”

“He’s a D-rank Hunter.”

“…”

“What? Is that too high for you to believe?”

“No, well… I’ll admit I’m a little surprised.”

She had sounded so confident that I had thought her son was at least Monkey D. Minsu.

*Where is there a famous D-rank Hunter in Bucheon?*

Perhaps she mistook my momentary silence for shock. The owner let out a series of derisive chuckles.

“A D-rank Hunter like my son is the kind of person who gets respect wherever he goes. An F-rank Hunter must be too embarrassed to even admit what he does for a living.”

“I wasn’t that embarrassed. I spoke just fine.”

“You still get looked down on. Among Hunters, rank is everything.”

“Ah, yes. Rank is everything.”

“If I make one phone call, Minsu will…”

“Yes, yes.”

As I answered halfheartedly and rummaged through my pocket, the owner raised her eyebrows.

“An adult is talking to you. Do you want my Minsu to teach you a lesson?”

“I’m just looking for something. Ah, here it is.”

“What is that?”

“If you’re curious, take a look.”

I had so many point cards and discount coupons in my wallet that finding anything was a chore. When the owner examined the thin silver card I handed her, her mouth fell open.

“…C-rank Hunter?”

“Personally, I think rank is everything for Hunters. What do you think, Boss?”

“N-no way. I heard you were F-rank…”

“I was F-rank. I’m C-rank now. You’re pretty slow when it comes to getting updated information.”

“I-isn’t this fake? The color is completely different from my Minsu’s license!”

“His license is brass-colored, right?”

“…”

“I used one of those myself in the past. Lower-rank Hunters have brass-colored licenses, while mid-rank Hunters have silver ones. You didn’t know that?”

Suppressed laughter erupted from all around us.

The atmosphere had flipped in an instant.

My mother slipped her arm through mine with a proud smile, while the owner’s face turned bright red and she began making excuses.

“D-does a Hunter’s rank really matter? C-rank and D-rank are only one step apart. They’re practically the same.”

*What kind of logic was that supposed to be?*

All I could do was give a hollow laugh at her absurd struggle.

“That’s not something a person who looked down on someone for their Hunter rank should be saying.”

“Are titles all that matter? The company you work for matters more. People respect an assistant manager at a major corporation more than a section manager at a small company. Am I wrong?”

“I don’t know about that, but the customers here don’t seem to agree with you.”

I gestured toward the customers filling the dining area.

Dozens of office workers from small and midsize companies were glaring at the owner without bothering to hide their displeasure.

“What’s with that ajumma?”

“My appetite’s completely gone.”

“The food hasn’t even come out yet. Should we just leave?”

“Yeah. Let’s go.”

“Everyone, move tables. There’s a decent set-meal place right up ahead. I may not be an assistant manager at a major corporation, but I’m a section manager at a small business, so lunch is on me.”

Scrape.

At the middle-aged man’s words, five or six of his subordinates stood and followed him.

Similar scenes began unfolding throughout the dining area.

“Customers, that’s not what happened. Customers!”

“What do you mean, it’s not? Just watch me never come back here.”

“But your orders have already gone in. If you leave like this…”

“Looking at that kitchen, it’ll take an hour anyway. Enough. We’re leaving.”

Despite the dining staff’s attempts to stop them, the customers streamed out like the tide going out.

After barely a minute had passed, fewer than ten customers remained in the dining area.

*Damn. I can already hear the sound of this place going under.*

The owner was trembling with anger and bewilderment.

“You… You people…”

“So which Guild did your son say he was with?”

“Our Minsu is one of the top Hunters in Sangdong Guild! Someone like you…”

“What? Which Guild?”

“Sangdong Guild! They even gave him a house and a car.”

“Oh, Sangdong Guild. Could you wait just a moment?”

What an incredible coincidence.

Holding back my laughter, I pulled out my smartphone and made a call.

Beep. Beep. Beep. Click.

“Uh, what is it?”

“Were we only supposed to call each other when we had business?”

“…I sent you the promised four billion won, though.”

“Ah, I checked that. It came through fine.”

The entire conversation continued over speakerphone, loud enough for everyone to hear.

Four billion won.

The moment it became clear that what I had said earlier was true, everyone’s eyes seemed ready to pop out of their heads. I ignored all the attention and got to the point.

“Do you happen to know a Kim Minsu?”

“Kim Minsu? That’s the first I’ve heard of him.”

“You’re a Team Leader in Sangdong Guild and you don’t even know that? They say he’s a D-rank Hunter in your Guild.”

“D-rank Hunters are a dime a dozen. How would I know all of them? Is that why you called?”

“Yeah. Bye.”

Taking Im Changsoo’s business card in case he tried to stiff me had been a stroke of genius.

Click.

As soon as I hung up, the owner asked in a faltering voice,

“W-who was that?”

“Didn’t you hear? He’s the Team Leader of Sangdong Guild. In simple terms, he’s Mr. Minsu’s boss.”

“…Team Leader? His boss?”

“Oh, and one more thing. He’s also a future employer Mr. Minsu will want to impress. His father is the Guild Master of Sangdong Guild.”

“…”

Her face went white as a sheet.

There was no longer any reason or need to exchange another word with her. I turned toward my mother.

“Let’s go now.”

“Should we, son?”

My mother, Kim Jeonghee, flashed a broad smile and shoved her work clothes into the sink.

Of course, she didn’t forget to leave the owner with one final remark.

“Live like a parent should, you ajumma. Where do you get off casually running your mouth about someone else’s precious child?”

That was the final blow.

The owner lowered her head without answering, and we left the restaurant with light steps.

“Son, have you eaten? There’s cheonggukjang and kimchi pancakes at home.”

“Wow. What a feast.”

The weather was beautiful.

[^1]: A *goshiwon* is a tiny, inexpensive room-for-rent housing arrangement, often with shared facilities.

[^2]: *Ajumma* is a familiar Korean term for a married or middle-aged woman, commonly used by customers or employers to address service workers.
## Chapter artifact 89

# Chapter 89

“Son, slow down. You’ll make yourself sick.”

“You could quit being a Hunter and become a mukbang streamer.”

I finished my meal amid Mom’s concern and Hayeon’s admiration.

That was after five heaping bowls of rice, a whole pot of cheonggukjang, and dozens of kimchi pancakes had vanished.

“Whew. I’m finally starting to feel full.”

“……Are you insane? How much do you usually eat?”

“If it’s tasty, it just keeps going in.”

I had always eaten a lot, but never this much.

Maybe it was because my metabolism and internal organs had improved to a degree that couldn’t even be compared to before. These days, I could put even professional food fighters to shame.

“Maybe I really should become a mukbang streamer.”

“No. Those people need to make a living too. Let humans compete among themselves.”

“Are you saying I’m not human?”

“Yeah. In my eyes, you’re something beyond a pig.”

Hayeon could only shake her head in disbelief as she put down her spoon. I glanced into her rice bowl and saw that half of it was still there.

“If you leave rice, you’ll be punished.”

“You sound like an old man.”

“Don’t you know Koreans run on rice even at death’s door? You have to eat if you want your cold to go away faster.”

“I don’t have an appetite. My head hurts too.”

“Did you go to the hospital?”

“I did. I took the medicine they prescribed, too.”

I stared at Hayeon in silence. Her face was flushed, and beads of sweat had formed on her forehead. She had left school early and stubbornly tried to study, but it seemed her fever had risen even higher than before.

*The medicine she was prescribed doesn’t seem to be working very well.*

Honestly, there was a much simpler way to cure an illness.

She could get treated by a professional healer or drink a potion sold on the market. But most ordinary people avoided doing that because of the expense.

*What a fool.*

The reason I had worked nonstop was so my family could live safely, happily, and without getting sick.

Even though I knew why they couldn’t spend money so easily, I couldn’t help feeling frustrated. How much could one lousy potion cost?

*At the very least, circulating qi once would make her feel much better… Huh?*

A thought suddenly flashed through my mind, and I stopped.

*Wait. Could this actually work?*

“Give me your hand for a second.”

“Huh?”

“Tsk. I said give me your hand.”

Hayeon looked me over as if I were some rare creature.

“What is happening here? Why are you being so gross?”

“You’d rather die than listen to a word I say.”

I grabbed her hand.

“We’re siblings, okay?”

“Stop talking nonsense.”

I raised my internal energy more carefully than ever. Slowly—very slowly—I let a thread of internal energy flow along my hand and into Hayeon’s body.

“Aah!”

Hayeon let out a startled cry. She had clearly noticed the strange sensation caused by my internal energy.

I was worried that it might scatter, but the Jin Family’s Cultivation Technique had already reached a realm stage. It obeyed my control without resistance, even inside someone else’s body.

*This much should be enough.*

The simple demonstration test was over. Now came the real test.

This time, I guided my internal energy toward Hayeon’s dantian.

Under normal circumstances, it would have been as easy as breathing. But Hayeon’s body was different. Her acupoints were narrow, and her insides were clogged with waste.

*This is going to be difficult.*

Even if I separated the modern world and the Murim and considered them independently, I possessed a body far beyond that of an ordinary person.

Hayeon, however, was an ordinary high school student. The waste accumulated over her nineteen years of life was only natural.

*Still, I should do everything I can.*

I could only attempt this because I trusted the Jin Family’s Cultivation Technique’s stability and my own control.

I also remembered to warn Hayeon in advance, just in case.

“It might hurt a little, so bear with it, okay?”

“What? What are you doing?”

“Hmm. I suppose you could call it a particularly stable form of traditional Korean medicine.”

Mom, who had been washing dishes, opened her eyes wide.

“Oh my, traditional medicine? You know how to do that too?”

“I just learned a little.”

“That’s wonderful. Give it a try.”

Hayeon, on the other hand, looked less than enthusiastic.

“Why traditional medicine? I’m not really into that kind of thing.”

“Then trust me and put up with it for a little while.”

“Mom, thank you for raising me all this time. Your useless daughter is leaving without even getting the chance to repay you.”

“…….”

*What the hell, you little shit?*

I almost lost control of my internal energy. I could run around for an hour without sweating a drop, but I was starting to feel a little hot now.

“I’m joking. It’s not like you’d do anything bad to your only little sister, right?”

“Then shut up and stay as still as possible, even if it hurts.”

“Okay.”

I took a deep breath. From this moment on, I was going to clean out Hayeon’s acupoints.

The cleaner was me.

The broom was fifteen years of internal energy.

“Ready?”

“Yes, yes, Teacher. But when exactly are we starting?”

“Right now.”

As soon as I answered, I sent my internal energy flowing.

*Whooosh.*

A wave of gentle yet powerful internal energy began sweeping through the minor meridians throughout Hayeon’s body, washing away the waste that had built up inside her…

* * *

“Hoo.”

“Phew.”

The two breaths that escaped us simultaneously after I let go of her hand carried completely different meanings.

Mine expressed relief.

Hayeon’s expressed refreshment.

*Ding.*

> **System**
>
> - **Circulate Qi for Healing** has been completed successfully.
> - **Internal Energy** increases slightly.

As the System had announced, Circulate Qi for Healing had ended successfully.

The Jin Family’s Cultivation Technique was an internal energy cultivation technique that accumulated internal energy slowly but possessed exceptional stability. Hayeon had accumulated so much waste that the process took some time, but it ended without any major problems.

“Oppa, what was that?”

The fact that she naturally called me Oppa showed that she had been surprised too. I wiped away the sweat that had formed from the tension and answered.

“I told you. It’s a stable traditional medicine treatment.”

“That worked when you were only holding my hand?”

*Do you think it would? It’s all thanks to your brother’s excellence.*

I smoothly changed the subject.

“So? How was it?”

“It hurt at first, but as time passed, it started feeling better and better. My body feels lighter, and my headache is gone. What should I call it…”

Hayeon furrowed her brow before defining it in a single phrase.

“Like I was reborn? Like all the bad energy inside me was washed away. Ah, damn it, I don’t know.”

*That sounds pretty accurate to me.*

In any case, seeing how much better her complexion looked made all the effort worthwhile. I let out a short laugh and said,

“Yeah, then go wash up.”

“Huh?”

“What do you mean, ‘huh’? Is your nose stuffed up? You stink, so go take a shower. Now.”

“I washed this morning. What do you mean I smell—Aagh!”

Hayeon realized that a terrible stench was radiating from her own body, grabbed her nose, and began making a huge fuss.

*It’s only natural.*

Where else would the waste inside her body go? It had to come out somehow. Through sweat, for example, or maybe…

*Grrrbl. Pffft.*

Well, it could come out that way too.

“…….”

But maybe it was because there had been so much waste. The smell was unbelievable.

At this point, I had to wonder if she had actually crapped herself.

“Aah.”

On top of the sweat soaking her body, her stomach had begun sending strange signals. Hayeon almost crawled to the bathroom, while Mom stood there with her mouth hanging open.

“My goodness.”

“It works well, doesn’t it?”

“It really does. I went to a traditional medicine clinic a few times when I was young, but this is amazing.”

“I learned properly. If you ever want to go to a traditional medicine clinic, just come to me. You can do it right now, if you want.”

“Should I? As it happens, I’ve been having some trouble digesting lately…”

Mom smiled brightly and held out her hand.

That was when—

*Bwaaaang. Frrt. Frrt.*

“…….”

“…….”

Mom quietly withdrew her hand.

“……Should we start when Hayeon comes out?”

“……Yes.”

There was only one bathroom in our house.

* * *

*Whooosh.*

Some time after the sound of the toilet flushing, Mom emerged with the most refreshed expression in the world.

“How do you feel?”

“I feel ten years younger.”

That wasn’t an exaggeration.

Even Hayeon, who was only nineteen, had needed more than an hour to expel all the waste from her body.

Mom was middle-aged, so the amount of waste she had accumulated was proportional to the years she had lived. After more than two hours of circulating qi for healing, her condition must have improved to a degree that couldn’t even be compared to before.

“Right? Until just a little while ago, I had a headache and felt dizzy, but now I’m completely better. I took my temperature as soon as I came out of the bathroom, and it was normal.”

Hayeon looked at me as if I were some kind of marvel. The moment she came out of the bathroom, she ate two bowls of rice as if she had never once complained about having no appetite.

“Where did you learn something like this? Were you a healer, Oppa?”

“A healer? No. I just happened to learn it.”

“Which traditional medicine clinic did you learn it at? If it’s nearby, I’ll go there too.”

“……You’d be in big trouble if you went there.”

“Why?”

“You don’t need to know. Just know that there are lots of scary men there.”

“Do they stick the needles in painfully?”

“……They do tend to.”

*If she knew those ‘needles’ were actually knife stabs, what kind of expression would she make?*

I pushed Hayeon away as she kept peppering me with questions and slipped a hand into my pocket.

*Open Inventory.*

A translucent inventory window appeared along with the familiar System notification.

If I had been in the Murim, it would have been packed with the spoils I had obtained after defeating Jopil and various weapons.

But this was reality.

*It would be nice if the inventories were integrated.*

The fact that they were separate seemed more unfortunate the more I thought about it.

Taking just a few high-grade potions to the Murim would be no different from bringing along a few extra lives.

*Well, I should be satisfied that I can recover to some degree by leveling up.*

I clicked my tongue inwardly and pulled my hand from my pocket. Two small bottles filled with red liquid were sloshing in my palm.

### Item Window

**Lesser Potion**

- **Type:** Medicine
- **Grade:** Third Rate
- **Description:** A liquid infused with weak healing magic. It is readily available on the market.
- **Effect:** Restores the body when consumed. The effect is minimal.

They had been issued as raid supplies yesterday. Since I had no particular use for them, I had put them in my Inventory and left them untouched.

*I’m technically supposed to return them.*

Even lesser potions cost more than 200,000 won apiece. It was difficult to find an employer as generous as Team Leader Choi, who handed them out so freely.

“Take one each.”

“Huh? It’s a potion.”

“Why go as far as using a potion? I’m perfectly fine now.”

“I’m worried there might be side effects. If you don’t drink it now, it’ll cost you more later.”

In truth, I was only recommending them to restore their vitality. Circulating qi for healing had no side effects.

“Drink up. You too, Hayeon.”

Mom hesitated, then took hers first. Hayeon cautiously took her cue from Mom and followed suit.

*Gulp. Gulp.*

“How is it?”

Hayeon finished hers in one go and tilted her head.

“I feel a little stronger, maybe. Or maybe not. How would I know? It’s not like I’ve had a potion before.”

“I guess I don’t really know either.”

“You’ll definitely notice the effect when you’re tired or sick. I’ll buy a box and keep it here, so drink one whenever that happens.”

“A box? How many come in a box?”

“Fifty, if you buy the large one?”

“At about 200,000 won each, fifty would be… ten million won? Oppa, are you crazy?”

Hayeon smacked my forearm.

“Just because you made some money this time, are you really going to spend it so recklessly? If you keep overspending like that, that 300 million won will disappear in no time.”

“It’s fine. I’ve been earning well lately.”

“I searched online, and I heard that when you become a C-rank Hunter, you have to replace your equipment and all that. They said you can burn through hundreds of millions like it’s nothing.”

“I told you, it’s fine. I made four billion won yesterday, too.”

“Even if you had four billion won, you shouldn’t throw money around like—wait, how much did you say?”

“Four billion won.”

“…….”

Hayeon’s body went completely rigid.

She stared blankly at me, then turned toward Mom.

“Mom, Oppa says he made four billion won.”

Mom gave an awkward smile and nodded.

Only then did Hayeon ask in a trembling voice,

“Is that true?”

“Yeah.”

“Four billion won?”

“I’m telling you, it is.”

Determination filled Hayeon’s eyes.

“Oppa. Can I drop out of school?”

“…….”

*Didn’t you say there was no end to learning?*

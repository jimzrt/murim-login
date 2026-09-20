# Checkpoint Review — 545–549

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

# Chapters 545–549

## Plot

The Fire Dragon Pavilion is formally established under Jin Taekyung and Cheongpung. The System grants Taekyung the unique title **Fire Dragon Pavilion Master**, the achievement **Murim Alliance Civil Servant with a Sword Rice Bowl**, increased Fame, and a level increase. Jeok Cheongang, appointed chief of the Five Kings Hall, urges Taekyung to keep advancing while protecting the people who depend on him and remembering that others want to protect him.

The Murim Alliance completes its reorganization. The Two Dragons Pavilion is divided into Taekyung’s Fire Dragon Pavilion and Cheongpung’s Azure Dragon Pavilion, while both masters join the central leadership. Mae Jonghak presents the corpse of Jang Sam, a Hubei fisherman transformed into a grotesque mutant known as a Killing Ghost. The Alliance suspects Dark Heaven’s involvement, but the mechanism behind the transformation and the mutants’ ability to absorb human energy remain uncertain.

Taekyung gives the Alliance leaders his firsthand warning about Dark Heaven, describing it as an unprecedented monster-like threat rather than an ordinary demonic faction. He urges an immediate counterattack and maximum preparation during Dark Heaven’s temporary silence. Mae Jonghak then assigns the Fire Dragon Pavilion its first mission after a dispatch to a suspected target goes unanswered for more than seven days.

Taekyung identifies the Nanman Beast Palace as Dark Heaven’s likely next target and mobilizes the six-member Fire Dragon Pavilion. Ju Hwaran uses her previous Nanman escort experience and the Escort King’s records to prepare their route and supplies. The party arranges discreet transport, plans to regroup at Mount Daebyeol, and departs immediately. Hwaran’s former engagement to Sama Pyo creates awkwardness between them, leaving Taekyung unsettled.

## Continuity

- The Fire Dragon Pavilion consists of Jin Taekyung, Ju Hwaran, Song Ilseom, Sama Pyo, Taishan, and Hyuk Mujin. Taekyung leads it; Cheongpung leads the Azure Dragon Pavilion.
- The pavilion’s first mission is to investigate the Nanman Beast Palace. The party will regroup at Mount Daebyeol after arranging transport and leaving discreetly.
- Ju Hwaran knows Nanman’s terrain and hidden routes through prior escort work and the Escort King’s records.
- Mae Jonghak leads the restored Murim Alliance; Jeok Cheongang heads the Five Kings Hall; Murong Yeonghwi remains in Liaoning overseeing the Murong Family’s defenses.
- Dark Heaven can create rifts and grotesque mutants. Jang Sam’s transformation, the mutants’ energy source, and whether they can absorb human energy remain unresolved.
- The Southern Heaven Demon Empress may already be moving toward Nanman’s suspected target. Song Ho’s dispatch there has received no reply for more than seven days.
- Ju Hwaran and Sama Pyo’s political engagement ended for an undisclosed reason, and their unresolved history remains awkward.
- The Lord of Heaven’s identity, his connection to the force Taekyung associates with his original world, Dark Heaven’s method for opening Gates, and the outcome of Jeok Cheongang’s duel with Nangong Cheon remain unknown.

## Translation Decisions

- Render **이룡각** as **Two Dragons Pavilion**, **화룡각** as **Fire Dragon Pavilion**, and **청룡각** as **Azure Dragon Pavilion**.
- Render **남만** as **Nanman**, **남만수궁** as **Nanman Beast Palace**, **대별산** as **Mount Daebyeol**, **광서** as **Guangxi**, **건량** as **dry rations**, and **반 시진** as **half a shichen**.
- Render **만리행** as **Ten-Thousand-Li Journey** and **고잉메리호** as **Going Merry**.
- Preserve **Murim Alliance**, **Alliance Leader**, **Dark Heaven**, **Five Kings Hall**, **Hidden Shadow Pavilion**, **Black Dragon Demon Gate**, **Great Hero Jin**, **Young Lady Ju**, and **Fire Dragon Pavilion Master**.
- Preserve Taekyung’s blunt profanity and financial, monster, no-kids-zone, and P-King humor; Taishan’s clipped, childlike speech; and the chapter’s awkward engagement humor.

## Durable state

{
  "active_continuity": [
    "The six-member Fire Dragon Pavilion, led by Jin Taekyung, must depart immediately for the Nanman Beast Palace and regroup at Mount Daebyeol after arranging discreet transport.",
    "Ju Hwaran is a capable Fire Dragon Pavilion member with prior Nanman escort experience and route knowledge from the Escort King's records.",
    "The Mount Song Resolution restored the Murim Alliance; Mae Jonghak is Alliance Leader, Jeok Cheongang heads the Five Kings Hall, and Murong Yeonghwi oversees Murong Family defenses in Liaoning.",
    "Jin Taekyung is a Supreme Peak master with Three Flowers Gather at the Crown, advanced Qi Sense, exceptional resistance to monster Fear, and public S-rank-level recognition while retaining an A-rank license.",
    "Cheongpung is master of the Azure Dragon Pavilion, creator of Mimi Step, and caretaker of Mimi, whose condition was recently examined by Mungyeong.",
    "Mungyeong ended Taekyung's direct training and assigned him the final task of incorporating martial principles into his learned martial arts.",
    "Zhuge Feng's Demon-Sealing Formation still blocks mana from the exposed Gate, while Jang Taebo processes the Water God Dragon's remains.",
    "Dark Heaven remains an enormous monster-like threat capable of causing rifts and creating mutants; the mechanism behind Jang Sam's transformation remains unresolved.",
    "The Southern Heaven Demon Empress is believed by Taekyung to be moving toward the suspected next target, while Song Ho's dispatch there has received no reply for more than seven days.",
    "The Black Dragon Demon Gate remains a major unorthodox power; Sama Pyo is its Young Sect Leader and Black Dragon Saber, with Taishan as his giant subordinate.",
    "Jin Wikyung is Taekyung's eldest brother and has accepted that Taekyung keeps important secrets, asking to hear them when the crisis is over.",
    "Jeok Cheongang and Mae Jonghak now treat Taekyung's warning about a monster catastrophe as credible enough to justify immediate action."
  ],
  "continuity_sources": [
    549,
    548
  ],
  "open_questions": [
    "What is the Lord of Heaven's identity, how is he connected to the dangerous force Taekyung associates with his original world, and how can Dark Heaven open Gates?",
    "What will Taekyung's party find in Nanman, and what does the Southern Heaven Demon Empress intend there?",
    "What is the outcome of the duel between Jeok Cheongang and Nangong Cheon, the Azure Sky Sword King?",
    "Why did Ju Hwaran and Sama Pyo's political engagement end?",
    "What process created Jang Sam's mutant form, and can Dark Heaven's mutants absorb human energy?"
  ],
  "safe_through": 549,
  "temporary_decisions": [
    "Render 건량 as dry rations, 광서 as Guangxi, 대별산 as Mount Daebyeol, 만리행 as Ten-Thousand-Li Journey, and 고잉메리호 as Going Merry.",
    "Render 반 시진 as half a shichen and retain Nanman, Nanman Beast Palace, Fire Dragon Pavilion, Great Hero, and Young Lady Ju.",
    "Preserve Taekyung's blunt profanity and financial, monster, no-kids-zone, and P-King humor, along with Taishan's clipped childlike speech."
  ],
  "version": 1
}

## Reading copies

## Chapter artifact 545

# Chapter 545

*Fire Dragon Pavilion.*

The moment I muttered those three words—

*Ding. Ding. Ding.*

Along with clear bell tones bursting like celebratory fireworks, a new holographic window came rushing into view.

> **System**
>
> - **Fire Dragon Pavilion** has been registered under its new name!
>
> - All Quest conditions have been fulfilled!
>
> - Quest, **Become My Companion!**, has been successfully completed!
>
> - **Fire Dragon Pavilion** has been officially established!
>
> - You have acquired the unique Title, **Fire Dragon Pavilion Master**!
>
> - You have achieved the rare achievement, **Murim Alliance Civil Servant with a Sword Rice Bowl**!
>
> - You have acquired a large amount of Fame and EXP!

The Quest completion. The achievement. And on top of that, the unique Title **Fire Dragon Pavilion Master**.

Notifications poured down one after another. But the rewards prepared by the System did not end there.

*Ding. Ding. Ding.*

> **System**
>
> - Even now, your name is echoing throughout Murim under Heaven.
>
> - Your total Fame has surpassed 10,000!
>
> - You have achieved the outstanding achievement, **If You Don’t Know Him, You Must Be Dark Heaven**!
>
> - As an achievement reward, some Title effects have been strengthened, and **Charm** and **Intimidation** have increased significantly!
>
> - You have acquired a large amount of Fame and EXP!
>
> - Level Up!

*Oh, shit.*

Was today Christmas or something?

Fame had become something I barely paid attention to anymore. But after gaining a large amount of Fame and breaking through 10,000 at the same time, I had received an unexpected additional reward.

Some Title effects and stats had been strengthened. And on top of that…

*I leveled up.*

The fact that leveling up became more difficult the farther one progressed applied even to crappy online games, but lately, it had reached the point where it was as difficult as plucking a star from the sky. It was almost as though the System had forcibly nerfed me.

At a time when countless battles were sure to lie ahead, each bonus point I gained through leveling up was a treasure that could not be exchanged for a fortune.

*Come to think of it, I must have accumulated quite a few bonus points. And Titles, too.*

Had the last time I checked my Status Window been right after defeating the Water God Dragon?

When I had first come to Murim, I had opened my Status Window dozens of times a day because of my anxiety disorder. But as time passed, I checked it less and less. These days, I hardly looked at it at all.

That was because, once my stats had reached a certain level, I had realized that they were little more than luck. What truly determined the outcome of a decisive moment was martial arts.

*Still, I should organize everything properly one of these days.*

It felt like only yesterday that I had been called the disgrace of my family at Level 10. Now I was a monster who had sailed past Level 100, as well as a nationally famous Supreme Peak master whom no one in Murim failed to recognize.

As I smiled contentedly, thinking about my younger days, Jeok Cheongang spoke in a disgruntled voice.

“Your mouth is splitting open from how happy you are. Is becoming a Pavilion Master truly that wonderful?”

“Oh, it’s not just because of that.”

“Then what? Are you happy because you’ll be separated from this old man?”

“Huh?”

I asked the question, then finally realized why Jeok Cheongang looked so displeased. I paused.

“Are you sulking because of that?”

“Sulking? Me? The Fire King Jeok Cheongang?”

Jeok Cheongang’s eyes bulged as he let out a powerful snort.

“Hmph! What nonsense!”

“Don’t snort so hard. Your boogers are flying. And with a reaction like that, even a passing mutt could tell.”

“You ill-mannered brat! What do you think you know?”

*Well, that settles it.*

I took a step back from Jeok Cheongang, who was spitting as he grew more agitated, and calmly tried to soothe him.

“It can’t be helped. It’s not my fault that you entered the Five Kings Hall.”

The Five Kings Hall was an organization newly established by the new Murim Alliance, which had carried over the old Murim Alliance’s structure.

It had only five members, but it would not be an exaggeration to call it the most powerful fighting force in the Murim Alliance—or even in all of Murim.

Just looking at the lineup, it was practically Murim’s Avengers.

*Thunderbolt Saber King Peng Cheolhu. Azure Sky Sword King Nangong Cheon. Seafaring King Pa Ryun. Fist King Yan Hwapyeong. And…*

The one person standing right in front of me.

The Fire King, Jeok Cheongang.

As could be seen from the titles and names of its members, the name Five Kings Hall had not been chosen for no reason.

It was where five of the Ten Kings who had held their positions firmly throughout the passage of countless years had gathered.

*Living legends, in the truest sense.*

And Jeok Cheongang was the chief seat of the Five Kings Hall.

In terms of seniority and age within Murim, he was practically the water in Bodhidharma’s skull. And no one could dispute the level of his martial arts, which had reached Returned to Youth.

*He had even been considered the best among the Ten Kings during the Great Faction War.*

The Blood Lord I had encountered during the Shaolin Bloodshed had tried to recruit Jeok Cheongang from the very beginning rather than fight him.

He had even said that if the Great Faction War had continued a little longer, Jeok Cheongang would have become one of the Four Saints rather than merely one of the Three Saints.

But…

“To hell with the Five Kings Hall. They’ve slapped a title on me that isn’t even in my fortune.”

The person in question was too busy grumbling to care.

The Five Kings Hall was an organization made up of living legends, and Jeok Cheongang sat at its very top. Yet he seemed to dislike the whole thing immensely.

Hyuk Mujin, who had been watching him closely, cautiously raised his hand.

“Um.”

“What is it?”

“If Great Hero Jeok leaves the Five Kings Hall, could I take his place?”

“……”

“……”

“Perhaps through a recommendation or something…”

*That guy was not merely crazy.*

Jeok Cheongang, who had fallen silent along with me, stared at Hyuk Mujin with a deep gaze.

“Go. Unless you want to die.”

“Yes, sir. I’m sorry.”

“If you flap that twitchy mouth of yours one more time, this old man will have something to apologize to your parents for.”

After issuing the threat in a chilly voice, Jeok Cheongang turned and glared at me.

“And you.”

I quickly waved both hands.

“I don’t need to join the Five Kings Hall.”

“That isn’t what I mean.”

“Then what is it?”

“What are you planning to do from here on out?”

It was a question that contained much more than merely asking about my future movements.

The look in Jeok Cheongang’s eyes as he gazed at me had become a complicated mixture of pride and concern.

“You’ve done well to come this far. I’ll give you that. But from here on…”

“Old Master.”

I cut off the words that were about to continue in a quiet voice and shrugged.

“I’m not as much of a child as you think.”

“……!”

“And I already know what you’re going to say.”

It was not a lie. I could easily guess what Jeok Cheongang was trying to tell me.

From this point onward, the real war would begin.

Not a battle. A war.

Countless lives would be sacrificed as offerings to determine who would rule the world.

The fights I had faced until now had never been easy, but it was obvious that even greater dangers would come crashing down upon us from here on out.

But…

“You said it yourself a moment ago. You asked me what I was hesitating for. You told me to simply move forward.”

That was right. I would simply keep moving forward. Just as I always had.

In my own way.

“I’ll hesitate for a little while, then move forward without holding back.”

Jeok Cheongang silently stared at my noiseless smile before letting out a quiet laugh.

“If you move forward, then you move forward. What does it mean to say you’ll hesitate for a little while?”

“It can’t be helped. Somehow, I’ve ended up with a lot of things to protect.”

I had blood relatives who were as precious to me as my own life. I had companions and subordinates to whom I could entrust my life. And I had a Master with whom I had formed a bond deep enough for me to throw my life away.

I could not—and should not—ever lose something precious again as I had in the past.

“I’ll move forward while protecting everything I have.”

“Hah. You’re a greedy bastard.”

Jeok Cheongang let out a short, hollow laugh before continuing.

“But that is the right answer.”

“Huh?”

“Always be careful and think. No matter what crisis comes crashing down before you, and even if you encounter an opponent you cannot possibly defeat, return alive with that mindset.”

“Old Master…”

“And remember this.”

His voice was different from usual. It was calm and warm, and it slipped into my ears.

“You, too, are someone whom another person wants to protect.”

* * *

Noon.

The dazzling sunlight stabbed into the earth.

*Thud. Thud.*

Several dozen people were walking in the same direction.

Women and men, middle-aged people and the elderly, all mixed together, they continued forward without hesitation until they finally reached their destination.

*Creeeak. Boom!*

The moment they approached, a massive door swung wide open.

Above it, three characters written in a single flowing stroke looked down over the heads of those entering.

Alliance Leader’s Hall.

Located at the heart of the Murim Alliance, it was where the major affairs of all Murim were decided.

That meant the various people entering the Alliance Leader’s Hall were the large and small pillars supporting the current Murim.

And two people among them stood out above all others.

“Smack. Smack-smack.”

One young man constantly stuffed something into his mouth even as he walked. Another young man silently watched him.

The two appeared to be around the same age, but their physiques and the atmosphere they gave off were completely different.

There were, however, two undeniable things they had in common.

The first was that they were prodigies rarely seen even in Murim’s long history.

The second was that they had accumulated an astonishing amount of fame.

Perhaps that was why the gazes directed toward them never disappeared—not from the moment they first entered the hall, nor even after they took their seats.

*Huh. So those young men are…*

*Blazing Flame Divine Dragon Jin Taekyung and Huashan Divine Dragon Cheongpung. This is my first time seeing them from such a close distance. Is this really what they’re like?*

*Impossible! What perfect muscles and bones. He reached the Supreme Peak realm at such a young age. How could anyone belittle him as a kid barely past twenty?*

Wonder and admiration filled the gazes of those finally meeting the young heroes they had heard about only through rumors.

*He may be a Pavilion Master, but what an undisciplined attitude.*

*Tsk, tsk. His martial arts may be strong, but he’s still not fully formed as a person.*

*Giving such important positions to children like that? You will regret this, Alliance Leader.*

Envy and jealousy. Belittlement.

Their gazes and thoughts were as varied as their faces.

But the two young men remained completely unaffected by those stares.

More precisely, they did not care at all.

“Smack, smack. Agu, agu-agu.”

Jin Taekyung watched Cheongpung, who was stuffing dumplings and meat into his mouth, with a deep gaze before muttering,

“What the fuck, is this guy a martial artist or Agumon…”

“Whah?”

“Nothing. Keep stuffing your face, Young Hero Cheongpung.”

“Wahn one?”

“Afraid? What would I be afraid of? You’re the one who scares me. And no, I don’t want one, so swallow before you speak. Dumpling filling is flying all the way over here.”

Jin Taekyung muttered in a resigned voice and reached toward the flying bits of dumpling filling.

*Whoosh. Tick!*

His fingers moved so quickly that even a capable Peak master would have struggled to follow them. As he knocked aside the finely chopped meat and vegetables, gasps and exclamations rose from various parts of the hall.

“Gasp!”

“My word.”

The world was vast and its masters were numerous, but not every one of the several dozen people gathered here was a Supreme Peak master.

Even so, a martial artist’s level could be estimated from a simple movement.

Jin Taekyung was a Supreme Peak master who had opened his Middle Dantian. It would not be an exaggeration to say that his movements belonged to an entirely different realm.

*The Fire King’s Disciple… He truly lives up to his reputation. The rumors were no exaggeration.*

*Damn it. What kind of monster is that?*

*If the Huashan Divine Dragon has reached the same realm… Hah. Astonishing.*

That was the exact moment when the people in the hall were watching the two young men while entertaining their own thoughts.

“The Alliance Leader is entering.”

A deep voice echoed through the main conference hall of the Alliance Leader’s Hall.
## Chapter artifact 546

# Chapter 546

“The Alliance Leader is entering.”

Five doors opened one after another to the accompaniment of a deep voice. As a figure slowly approached from beyond them, everyone rose from their seats at the same time, as though they had rehearsed it.

“Nom, nom. Munch, munch.”

“……”

Everyone except this bastard.

*The more I look at him, the crazier he seems.*

I was not exactly the most polite person myself, but I at least had a basic sense of propriety. I leaned toward Cheongpung, who was determined to safely store every last piece of leftover food inside his mouth, and whispered,

“What the hell are you doing? Do you have a problem with society? Don’t you like the Murim Alliance?”

Cheongpung swallowed what was in his mouth and stood up before answering.

“But there’s still food left, Benefactor.”

“Then stop eating.”

“But the dumplings will get cold.”

“……”

*You bastard, Cheongpung. You Guan Yu bastard. You know the dumplings will get cold, but you have no idea that everyone else’s stares are growing cold…*

*Well, he’s always been like this.*

Cheongpung would not be Cheongpung if he cared about the gazes around him. I let out a small sigh, poked him in the side, and muttered,

“If you’re done eating, let’s focus. Our esteemed Azure Dragon Pavilion Master.”

At the words *Azure Dragon Pavilion Master*, Cheongpung pushed out his lower lip and nodded. Then a small, thoroughly disgruntled voice escaped him.

“Yes, Benefactor.”

The name Two Dragons Pavilion remained unchanged, but the organization had been divided internally into my Fire Dragon Pavilion and Cheongpung’s Azure Dragon Pavilion. According to the conversation I had with Cheongpung on our way here after being summoned to the great conference, he had wanted to give his pavilion a different name—but Mungyeong had fiercely opposed it.

*I don’t like that name.*

*Why? I think Azure Dragon Pavilion sounds pretty cool. Still, it is a little unfair. Aren’t you the Pavilion Master? Shouldn’t you at least be allowed to choose your own name?*

*I thought so too, but Grandpa Mun said he hated it. He threatened to quit if I used a name like that.*

*It was that bad? What name did you want to use originally?*

*Dumpling Pavilion.*

*……*

*Or maybe Sweetmeat Pavilion.*

*……Oh. Right.*

*Hoo. I hate Grandpa Mun. What’s so great about Azure Dragon Pavilion, anyway?*

It was ridiculous even now. *You should be grateful, you lunatic.*

If he was going to go that far, he should have called it Gim Bugak Pavilion.[^1] The words rose to my throat, but I swallowed them back.

Not because it was already in the past.

The highest authority in orthodox Murim had finally entered the great conference hall.

*Tap.*

Footsteps cut through the quiet silence. At last, Murim Alliance Leader Mae Jonghak reached the seat of honor and gave everyone a genial smile.

“You have all gathered.”

Unlike the previous meeting, this gathering included the heads of the key organizations under the Alliance Leader’s Office. That also meant the Murim Alliance’s internal reorganization was finally complete.

*There are quite a lot of us when we’re all gathered like this.*

I quickly surveyed the room. There were unfamiliar faces, as well as several familiar ones.

The unfamiliar faces belonged to masters whose names and sobriquets I had heard but never met. The familiar ones, however, included more than a few people I was glad to see.

“You’re awfully late. My butt nearly went numb.”

The people who could speak to Mae Jonghak that way could be counted on one hand, even if you turned the whole world upside down and shook every soul out of it.

Jeok Cheongang was the most prominent among them. Seated directly beside the seat of honor, he stood with one leg cocked and spoke in his usual surly tone.

Across from him, seated in the middle of the room, Jin Wikyung glanced around nervously before opening his mouth.

“Great Hero Jeok.”

“What?”

“You know how it is.”

“Good grief. Now that you’ve got a title, are you taking the Alliance Leader’s side?”

Jin Wikyung paused for a moment and gave an awkward smile. In the space of just a year and several months, he had taken the helm of the Jin Family of Taiyuan as Acting Family Head and brought astonishing growth to a family that had been slowly declining. Before anyone knew it, he had become one of their number.

“It’s not that—”

“I know. I know. Now the two brothers are making a fuss together.”

Mae Jonghak smiled at the grumbling Jeok Cheongang.

“Don’t be like that, Great Hero Jeok. Or should I call you the head of the Five Kings Hall now?”

“……Hmph. I understood you perfectly well, so stop. There are too many eyes watching.”

“Then I suppose I’ve summoned busy people here only to spout nonsense.”

It was hard to imagine anyone busier than Mae Jonghak, but he was not wrong.

Each person gathered here was a vital part of the vast Murim Alliance, one of the cogs that kept it moving.

*The Two Halls, Three Divisions, Five Pavilions, Five Gardens, and Ten Squads—Nine Squads in the characters.*

The only organization standing shoulder to shoulder with the Alliance Leader’s Hall, led by Murim Alliance Leader Mae Jonghak, was the Five Kings Hall, now headed by Jeok Cheongang. Beneath them were the Three Divisions and Five Pavilions belonging to the Inner Hall, followed by the Five Gardens and Ten Squads, which were occupied by people from the Five Great Families and the Nine Sects and One Gang.

*And there are even more besides them.*

Amazingly, the people gathered here were not everyone. If the unit heads and squad commanders of the Outer Hall were included, even this vast conference hall would not have enough room. They would have to use the training ground.

That was proof of just how enormous the Murim Alliance was. It also meant that Cheongpung and I had been recognized as members of its central leadership.

*Well, it’s still basically an honorary position without any real authority.*

Perhaps it was the difference between a position and a rank. My official position was Pavilion Master, but in terms of actual standing, I was close to the lowest seat among those gathered here.

Of course, there was no one else around my age who held a position like this.

*Ah. There was one other person besides Cheongpung.*

One-Ride Heavenly Dragon Murong Yeonghwi.

A genius who had been called Murim’s greatest young prodigy only two years ago. He was the Lesser Family Head of the Murong Family and had recently been appointed a Squad Leader of the Murim Alliance’s Outer Hall. I had heard that instead of following his father, the Family Head, to Henan, he had remained in Liaoning to oversee the family’s defenses.

*I thought I might finally get to see him in person.*

Then again, there was no stupider act than leaving one’s base undefended just to attend a meeting in Henan. Everyone else here must have completed their defensive preparations in the same way.

*Swish.*

Mae Jonghak slowly raised one hand and spoke.

“All right, everyone, sit down. We don’t have enough time to maintain such formalities.”

But nobody returned to their seats.

More precisely, they could not.

The instant Mae Jonghak raised his hand, something unidentified drifted slowly upward from beyond the doors that remained open.

“How can he use Seizing an Object Through Empty Space so effortlessly…?”

Someone muttered under their breath.

The object was covered by a cloth, so its identity could not be made out. But it was obviously enormous and seemed to possess considerable weight. Exclamations of admiration rose at Mae Jonghak’s internal energy as he moved it without effort.

Yet several people’s faces had already hardened.

Mine must have, too.

*This isn’t about his internal energy. That thing is…*

Of the five senses, the first to react was the nose—my sense of smell.

The scent was so faint that even a martial artist with heightened senses would have had trouble identifying it immediately. But the moment I caught that stench, I understood.

“Benefactor. Is this smell perhaps…?”

Cheongpung’s eyes widened as he asked the question. I gave him a small nod.

“That’s right. It’s the smell of a corpse.”

“……!”

The smell of a corpse was exactly what it sounded like: the stench of a rotting body.

I had encountered that foul odor countless times while traveling between the modern world and Murim. This time, I was more certain than anyone.

At the same time, a suspicion about the corpse’s identity flashed through my mind.

*If my guess is right, then that is…*

The next moment, the cloth stained dark red with blood was pulled away.

Everyone in the great conference hall let out a groan almost simultaneously.

“Hk!”

“W-What in the world…?”

“Alliance Leader, what is the identity of this thing?”

Voices filled with shock burst out from every corner. Those who already knew about it and those who did not were all forced to feel the same shock at that moment.

The sight hidden beneath the cloth was that horrifying.

*A monster.*

There was no other way to describe it.

At first glance, it had the shape of a human being. But unnaturally elongated and thickened joints protruded grotesquely from all over its body, while its wide-open eyes had lost their light and were as large as a child’s fist.

And the creature’s grotesque features did not end there.

“Th-There’s a horn.”

“That’s not all. Its arms…”

A black horn rose from the exact center of its forehead, and four arms protruded from its upper body.

They differed in length and thickness, perhaps because they had been severed during the battle. But no one could dispute that they were human arms.

“Hmm.”

“How could this have happened?”

As people continued to sigh, someone suddenly spoke.

“Infinite Life Buddha. It is indeed unbelievable. I felt the same way at first.”

The speaker was an old Daoist with a snow-white beard reaching his chest and deep-set eyes.

He was the Sect Leader of Wudang.

The people whose attention had focused on him looked puzzled.

“At first…?”

“Do you mean…?”

The Sect Leader of Wudang nodded.

“That is correct. Some of you may already have heard this, but that man—or rather, that thing—was originally a fisherman named Jang Sam.”

Information I had heard earlier in the Hidden Shadow Pavilion now flowed from the old Daoist’s lips.

A fisherman with an ordinary name, no different from anyone else, had disappeared. One month later, he had reappeared as a monster and a Killing Ghost that had thrown Hubei Province into an uproar.

“When it was first discovered, its martial arts were only Third Rate. However, its strength and movements were said to be inhuman. And each time it appeared again, its appearance became more grotesque and its strength greater. As though…”

After a brief hesitation, the Sect Leader of Wudang continued in a voice filled with sorrow.

“As though it harmed people, absorbed their vital essence, and made it its own.”

“……!”

A shock no one could see swept through the great conference hall.

A suffocating silence settled over the gathering. Jeok Cheongang wrinkled his brow and suddenly spoke.

“Are you saying that goddamn monster learned the Essence-Siphoning Great Technique?”

The Sect Leader of Wudang shook his head.

“Infinite Life Buddha. I cannot easily be certain of that either. However, if that thing is the result Dark Heaven intended to create and it can truly use the Essence-Siphoning Great Technique…”

The old Daoist’s voice trailed off, his face rigid.

He was not the only one. Most of the people gathered in the hall looked the same.

*It’s understandable.*

The Essence-Siphoning Great Technique was a demonic martial art so terrible that it was said to have been lost even within the Demonic Cult. Orthodox martial artists regarded it as a martial art created by fiends.

But if Dark Heaven had revived that technique and taught it to monsters they had created…

*That would be a catastrophe. Nothing less.*

Fortunately—or unfortunately—I did not know which—the Sect Leader of Wudang’s guess was wrong.

At least, as far as I knew.

*Most monsters grow rapidly.*

*Didn’t they say an Orc takes only a month to reach adulthood?*

There were two main ways most monsters became stronger.

They were either born as individuals possessing tremendous power from the beginning, or they absorbed mana from other monsters.

*Eating humans might give them a small amount of strength, but most of the people this thing killed were commoners and Third Rate or Second Rate wandering martial artists.*

Humans and monsters were born with fundamentally different types of energy.

If such an interaction were possible between the two species, modern monsters would already be sold as aphrodisiacs or health tonics.

*I can’t be one hundred percent certain since it’s a mutant.*

But based on everything I had experienced so far, that was the more likely possibility.

No, I hoped it was.

If monsters capable of absorbing human energy directly began pouring out into the world, there would be no way to deal with them.

It was just as I was lost in those thoughts that Mae Jonghak’s quiet voice echoed through the great conference hall.

“Pavilion Master Jin. What do you think?”

I turned my head toward the voice calling for Pavilion Master Jin—and froze when I felt everyone’s gazes on me.

*Wait. Pavilion Master Jin means…*

*Fuck. That’s me.*

I still wasn’t used to it, so I had forgotten.

“Are you speaking to me?”

“That’s right. I’m asking for your opinion.”

“Well, I mean. This is quite…”

I hesitated, and Mae Jonghak said in an even voice,

“It’s all right. Say whatever comes to mind.”

“I’m not sure how I should put it.”

“Say it in your own way. Simply and clearly.”

Simply and clearly.

I thought for a moment, then carefully parted my lips.

“In my opinion, things are a little—or perhaps considerably…”

“Considerably?”

I stared into dozens of pairs of burning eyes before answering.

“I think we’re fucked.”

“……!”

“……!”

[^1]: Gim bugak is a Korean snack made from seasoned seaweed coated in rice paste and fried. Its final syllable, *gak*, sounds the same as the Korean word rendered “Pavilion” in the names above.
## Chapter artifact 547

# Chapter 547

A chilling silence descended over the great conference hall.

The reaction had been easy enough to predict even before I opened my mouth.

So had the identity of the first person among the dozens gathered here to spit something sharp at me.

“Do you call that something to say?”

*How does he never fail to live down to my expectations?*

I clicked my tongue inwardly as I watched the middle-aged man with half-white hair speak as though he had been waiting for his chance.

I already knew his name and status. He had glared at me so fiercely during our last gathering that I had wondered what his problem was. As it turned out, we had an indirect connection.

*They say blood never lies.*

The resemblance was unmistakable. The sharply raised eyes, the arrogant gaze that looked down on others, even the way he spoke.

“It seems you didn’t hear me.”

The middle-aged man with half-white hair was Hwangbo Gun, the Family Head of the Hwangbo Family and the father of Shandong Fist Dragon Hwangbo Ak. I slowly blinked at his question.

“Of course I heard you. Do you really think I didn’t?”

“Then why didn’t you answer?”

“Because your question is ridiculous. Of course I considered it speech—it came out of my own mouth. Did I make some kind of animal noise?”

Cheongpung, seated beside me, pricked up his ears.

“Benefactor, can you make animal noises too?”

“You keep your mouth shut, Young Hero Cheongpung. Unless you want to puke up the dumplings in your stomach.”

“Thank you…”

Hwangbo Gun’s face twisted violently as he watched us.

“Do you not understand what kind of gathering this is?”

“Is there anyone here who didn’t know?”

“And yet you dare speak so crudely in front of all these esteemed Seniors!”

“That’s why I was trying not to say anything. Besides, we should hear the Seniors’ opinions too. What do you think?”

At my sudden question, Mae Jonghak nodded.

“Fire Dragon Pavilion Master Jin is right. I have no problem with it. His words may be rough, but we need to face reality.”

“A-Alliance Leader!”

The panic in Hwangbo Gun’s cry was obvious, and I quickly cut him off.

“Yes. We’ve heard the esteemed opinion of the Murim Alliance Leader. While we’re at it, what does our Five Kings Hall Master think?”

Jeok Cheongang looked at Hwangbo Gun as though he were a bug.

“What the hell are you asking for? We’re fucked, aren’t we? Ignore that bastard’s nonsense and continue.”

“Thank you for the fiery answer.”

I turned to Hwangbo Gun and shrugged.

“That’s what those esteemed Seniors have to say.”

“……!”

There were plenty of people here who could be called Seniors, but not one of them could compare to Jeok Cheongang and Mae Jonghak.

If the heads of the Nine Sects and One Gang and the Five Great Families were influential corporals serving as squad leaders and veteran sergeants nearing discharge, then Murim Alliance Leader Mae Jonghak was a battalion commander, while Jeok Cheongang was a command sergeant major.

*If you’re behind in seniority, you should keep your mouth shut.*

And it wasn’t just seniority. Even if he tore off his insignia and challenged Jeok Cheongang as an equal, one punch from the Fire King would send him flying.

That was why even Wind-and-Cloud Sword Lord, the Sect Leader of the Zhongnan Sect and perhaps the foremost among those who disliked Cheongpung and me, kept his mouth firmly shut.

Which meant Hwangbo Gun had been left all alone.

*You have to look before you stretch out your legs. Why did he step forward by himself?*

I had heard that Hwangbo Gun had wielded considerable influence during the Great Faction War. I did not know whether he had always lacked political sense, or whether he had become a runaway locomotive over matters involving his only son, the sole heir of three generations.

I hummed a mournful melody.

“I’m a firefly. I have no friends.”

“You insolent young punk!”

There was no way I could end things there. I drove in the combo I had prepared so carefully.

“Waaah. I’m a baby Pavilion Master.”

“You braaaat!”

Crash!

Hwangbo Gun sprang to his feet, the veins bulging across his tightly clenched fists.

He glared at me with fury, having gained nothing and not even managed to break even, when a voice suddenly rang out.

“‘Punk’… I beg your pardon, but may I ask you one question, Family Head Hwangbo?”

The gentle voice carried a firm resolve beneath it.

Jin Wikyung’s eyes, which had somehow settled coldly on Hwangbo Gun, were devoid of warmth.

“May I ask what position you hold within the Murim Alliance, Family Head Hwangbo?”

“……!”

“Regardless of how young the Fire Dragon Pavilion Master may be, he is the successor to Great Hero Jeok, the Fire King, and a Pavilion Master of the Murim Alliance. Even if we consider seniority within the martial world, he is certainly not beneath you, Family Head Hwangbo.”

He had struck the bull’s-eye. Hwangbo Gun’s face stiffened as his sore spot was hit.

He was the Family Head of the Hwangbo Family, the hegemon of Shandong, but his official position was merely Outer Hall Squad Leader, responsible for the defenses of a single region.

In terms of the Murim Alliance’s official hierarchy, that placed him beneath me, an Inner Hall Pavilion Master.

“That…”

Hwangbo Gun bit down hard on his lips, unable to continue. He looked around for somewhere to seek help.

But contrary to his expectations, the people around him responded without much enthusiasm.

“Amitabha. Would it not be best for you to exercise some restraint, Benefactor Hwangbo?”

“Heavens. Such a disturbance in the sacred Alliance Leader’s Hall.”

“Blazing Flame Divine Dragon. No, I am not taking the Fire Dragon Pavilion Master’s side. Both of you have had enough, so sit down.”

I answered without a hint of shame.

“I’ve been sitting down from the start.”

“Then only one person remains.”

It was obvious whom he meant.

Hwangbo Gun was torn between his rational judgment, which told him he needed to stop, and the last shred of pride possessed by the hegemon of Shandong and Family Head of a great family.

Then a single remark flew toward him, one that solved his indecision.

“Did you get a hidden weapon stuck in your ear?”

It was the Fire King, Jeok Cheongang.

With his brief words, the atmosphere in the great conference hall heated up.

Hwangbo Gun’s frozen figure was reflected in his eyes, which glowed with a red light.

“Sit down. Right now.”

“……!”

Whoooosh!

As his aura surged through the air and crashed over them, Hwangbo Gun’s eyes flew wide.

No—not just his. Every person in the great conference hall reacted the same way.

“Hmm.”

Fist King Yan Hwapyeong, who had been watching the situation in silence, let out a low groan.

“J-Jeok! You bastard…!”

The Thunderbolt Saber King Peng Cheolhu’s gaze churned.

That was how powerful Jeok Cheongang’s aura was. It was overwhelming, like another sun.

Those still in the Peak realm could feel his strength. So could those who had already reached the Supreme Peak realm.

*Returned to Youth.*

The mountain range called martial arts was rugged and vast. Sometimes, one had to pass through steep ravines or climb cliffs as sheer as though they had been carved away.

And Jeok Cheongang…

He was a great martial artist standing proudly atop the peak at the very end.

The man he was now had surpassed the title of Fire King.

Together with one other person in this room.

“Great Hero Jeok.”

The moment Sword Saint Mae Jonghak’s low voice rang out, the hot wind sweeping through the great conference hall vanished.

Jeok Cheongang gathered his aura in an instant and answered gruffly.

“What happened?”

“Hmm.”

“All right. I understand. I only scared him a little because he was making too much noise.”

It was no joke. If he scared him twice, Hwangbo Gun would probably wet himself.

The “bastard” Jeok Cheongang was referring to was already sitting in his seat with a deathly white face.

“It’s finally quiet.”

Mae Jonghak looked at Jeok Cheongang with a gentle but reproachful gaze before parting his lips.

By then, his eyes were fixed directly on me.

“Fire Dragon Pavilion Master.”

“Yes.”

“You have opposed Dark Heaven in Shanxi and Henan, as well as Sichuan and Hubei.”

To be precise, I had been dragged into those incidents, but I quietly nodded.

This was the great conference hall of the Murim Alliance. Dealing with Hwangbo Gun and discussing matters of such importance were two entirely different things.

“That’s right.”

“Few people know Dark Heaven as well as you do. Therefore, I would like to hear your opinion.”

“I was merely present at those incidents. Hidden Shadow Pavilion probably knows the concrete details and what is happening throughout the world better than I do. I already told you everything I knew.”

“I want to hear what you saw and experienced yourself. I want to hear the thoughts held by the person who went through all of it.”

*There we go.*

The words I had spoken before this were nothing more than bait for what I needed to say next.

Yielding and demurring once or twice were virtues. And if Mae Jonghak, with all the authority of the Murim Alliance Leader, went this far to ask for my opinion, it would lend that opinion all the more weight.

*All right.*

I took a small breath.

If my position until now had been the back seat of a car, I had just moved into the passenger seat.

I could not tell a driver setting out along an unfamiliar road in the thick fog of dawn everything I knew, especially without a navigation system.

But I could tell him where the speed bumps were and what awaited us farther down the road we were racing along.

*Even that ominous thought that has refused to leave my mind lately.*

When I finished organizing my thoughts and raised my head, every person in the great conference hall was looking at me.

Dozens of pairs of eyes.

They were people who could save—or kill—hundreds, even thousands, of lives in a war that had already begun.

It was impossible to know how deeply they would take the words of a kid barely past twenty to heart, but…

*It doesn’t matter. If we can win this war. If I can reduce the danger and sacrifice even a little.*

I had to do what I could right now.

Perhaps because of that, the voice that escaped my lips a moment later carried a force unlike its usual tone.

“Dark Heaven…”

* * *

Two shichen later,[^1] only three people remained in the great conference hall after everyone else had left.

The chairs that dozens of people had occupied earlier stood empty, but the silence that had settled over the room at some point refused to leave.

Thousand-Faced Fox Song Ho thought that the people who had left the Alliance Leader’s Hall were probably in the same state by now.

*They had every reason to be.*

The words that had poured from Jin Taekyung’s mouth were that shocking.

No one was unaware of Dark Heaven’s existence or its danger, but no one had warned of the crisis as fiercely as that young man.

*Not even me.*

The Hidden Shadow Pavilion gathered information from every corner of the world and produced countless predictions.

Hundreds of messenger pigeons flew in every day with information tied to their slender ankles, then departed again not long after.

As the head of the Hidden Shadow Pavilion, Thousand-Faced Fox Song Ho was not ignorant of how dangerous Dark Heaven was.

*But…*

The young master of the Fire Dragon Pavilion, Blazing Flame Divine Dragon Jin Taekyung, whose actions had caused one upheaval after another, had thought far beyond Song Ho’s expectations.

When people spoke of danger, he announced disaster. When someone cited the Great Faction War and argued that the Murim Alliance would prevail, he answered with biting sarcasm.

“Are we fighting the Demonic Cult right now? Our opponent is Dark Heaven, Dark Heaven.”

“What Dark Heaven showed us isn’t ordinary demonic martial arts. So what should we call it? Ah, this is driving me crazy. Fine. Let’s call it demonic martial arts for now.”

“I don’t know why, but while Dark Heaven has gone quiet for a little while, we need to begin our counterattack immediately. If we continue like this, we’re finished. Everyone dies.”

“Who said I was being too extreme? You there, Family Head. Have you ever fought something that came back to life even after all four of its limbs had been crushed? Or an imugi? About half an hour ago, did you see a monster and think of nothing but what to eat for dinner?”

“Our opponent is not an ordinary person. Dark Heaven is one enormous monster, and before long, we may have to fight monsters like that.”

“I may have gone a little too far. But I have to say this. We need to take every measure we can right now. Especially if you have some sacred object enshrined at home like a household god.”

Song Ho suddenly furrowed his brow.

From the moment Jin Taekyung began speaking, the area where his prosthetic leg was attached had started to throb. Now, a searing pain had broken out there.

*It wasn’t like this even a year ago.*

The pain that had resumed at some point had begun tormenting him again after he had grown old.

As though warning him that this was no time for such things.

And today, he was even in the company of that young man.

*It was as though he knew. As though he had experienced something in advance and was predicting some truth that I and the Hidden Shadow Pavilion—no, that everyone else—knew nothing about.*

A prediction? No.

Thousand-Faced Fox Song Ho corrected the thought he had just formed.

*A prophecy. It was like a prophecy.*

The question was whether it truly was one.

Could he really trust the words of that young man, whose life had brushed against Dark Heaven more closely than anyone else’s?

Where did the truth end and the exaggeration begin?

It was at that exact moment, while Song Ho was lost in thought, that a voice spoke.

“Believe him.”

“Hm?”

Jeok Cheongang, who remained in the great conference hall, continued when Song Ho looked up sharply.

“I said you should believe him.”

“Great Hero Jeok.”

“I know what you’re going to say. But…”

Jeok Cheongang’s tone suddenly softened.

“The kid I know has never once been wrong.”

“……!”

Song Ho froze at those words, which carried absolute trust.

Then Mae Jonghak, the last of the three people remaining in the hall, suddenly spoke.

“There are certainties in this world that cannot be inferred from information.”

“Alliance Leader. Do you mean…?”

“That’s right.”

Mae Jonghak rose from his seat and continued slowly.

“Have him summoned. We must assign the Fire Dragon Pavilion its first mission.”

[^1]: A shichen is a traditional Chinese time unit lasting approximately two hours.
## Chapter artifact 548

# Chapter 548

“Well done.”

The moment we stepped out of the great conference hall, Jin Wikyung said those words. I answered with a quiet laugh.

“Why are you laughing?”

“I don’t know. Maybe because your expression doesn’t match what you’re saying?”

“Ah.”

Only then did the stiffness leave his face. But the smile at the corners of Jin Wikyung’s mouth looked as though it might fade at any moment.

“To be honest, I don’t know how I should take what you said. Today, you were just so…”

“It’s all right. This reaction is only natural.”

I understood why Jin Wikyung had trailed off. I thought I could understand how he felt.

*If I were in his position, I would have reacted the same way.*

In this world, the word *death* was not as heavy as one might expect.

Murders were rare in the modern world and became known through television and other forms of mass media. Here, people witnessed death frequently.

Things were at least somewhat better in cities with good public order. But outside them, commoners had to live under the threat of bandits or mounted bandits, depending on where they were.

Martial artists were another matter entirely.

*A life spent walking along the edge of a blade.*

There was a reason people called it a mountain of sabers and a forest of swords.

That was why they were always prepared to die. They stoked their fighting spirit and trained their martial arts. And Jin Wikyung, standing before me, was a martial artist too.

The problem was the environment he and all the others had grown up in.

In Murim, people killed people, and people died by human hands. There were fierce beasts and spiritual creatures, but at least everyone knew what they were. They were not unheard-of monsters.

But today, I had claimed that…

Those monsters would cover this world.

I had predicted that a battle would begin in which humans and monsters killed one another.

*I don’t know how much my words really sank in, but they must have felt the danger clearly enough.*

As I continued speaking, some people looked at me with disbelief, while others sank into deep thought despite their confusion.

Even if they did not all believe me immediately, the fact that they had listened carefully meant I had achieved my modest goal.

*At least my audience was made up of martial artists, and I had hard evidence. That’s the only reason my words got through at all.*

If old Confucian scholars had been the audience, they would have shouted “Confucius Akbar!” and staged a protest against supernatural powers. But the people gathered in the great conference hall were not quite so narrow-minded.

At least, not with the corpse of a four-armed monster lying right in front of them.

*The same went for the Water God Dragon’s remains.*

The Water God Dragon’s remains had been separated by body part and were still being transported under the strictest secrecy.

But I had some of the byproducts I had quietly slipped into my inventory just in case, and they were more than sufficient as important physical evidence.

“Come to think of it, Youngest. Where did you get that? I was certain it had all been collected without a single piece missing.”

“What?”

“You know. The imugi you defeated in Hubei…”

“Ahem. Ahem. Cough-cough-cough!”

When I forced out a series of coughs, Cheongpung, who had been listening to our conversation beside me, rummaged through his robes.

“Benefactor. Would you like a sweetmeat? Sweetmeats are the best medicine for a cough.”

“…No. They’re the worst.”

“Yes.”

*When did sweetmeats become miracle medicine?*

At my firm refusal to participate in his experiment, the mad scientist Cheongpung looked dejected and popped a sweetmeat into his own mouth. Jin Wikyung watched him and let out a quiet laugh.

“I understand. I won’t ask any further.”

“Good. I appreciate that.”

As I awkwardly scratched my chin, Jin Wikyung stared at me for a long moment before suddenly speaking.

“Sometimes, I find myself wondering. Whether you, our youngest, are really the same child I knew.”

“……!”

“I won’t ask you outright. Nor will I harbor any further doubts. But there is one wish I have never told you about.”

His gentle voice continued.

“When all of this is over someday, and the time is right, I would like to hear the stories you have not yet been able to tell.”

*The stories I haven’t been able to tell.*

I repeated the words silently to myself.

*When will that time come?*

But if everything really ended as Jin Wikyung said, and if I had finished preparing myself mentally…

Perhaps I would tell him myself the secret I had never been able to share with anyone.

Perhaps such a day would come.

“…I understand.”

And it was at that exact moment, when I gave him a bitter smile and nodded, that—

“There you are, Fire Dragon Pavilion Master.”

*Tap.*

A dull sound rang out with the elderly voice. I turned my head and saw Song Ho, the Chief of the Hidden Shadow Pavilion of the Murim Alliance—the Thousand-Faced Fox.

“The meeting ended half an hour ago. Yet you are still here. Is that a coincidence?”

I shook my head.

The reason I had remained in the Murim Alliance until now was not merely to speak with Jin Wikyung.

“It must have been inevitable.”

“Inevitability, is it? Yes, I suppose so.”

A strange light flickered through the old fox’s crafty eyes. After a brief silence, the Thousand-Faced Fox spoke again.

“Come with me, Fire Dragon Pavilion Master. You already know what this is about, don’t you?”

I did.

I knew who wanted to see me. I knew why.

And the Thousand-Faced Fox’s next words changed my guess into certainty.

“The Alliance Leader is looking for you.”

* * *

*Thud.*

The sound of the door closing behind me echoed unusually loudly. Two people were already waiting for me in the office inside the Alliance Leader’s Hall.

“Have you arrived?”

After Jeok Cheongang’s flat question, Murim Alliance Leader Mae Jonghak gestured toward a seat.

“Sit down. And you all, wait outside for a moment.”

He was not speaking to me or to the Thousand-Faced Fox, who had entered the office right behind me. He was speaking to other people who had not revealed themselves.

*Swish.*

The moment Mae Jonghak finished speaking, several presences vanished like ghosts.

Even the secret guards who always remained around him withdrew. I sat in the empty chair and spoke.

“They’re incredibly skilled. I could barely sense their presence.”

“Most people who enter this room don’t even realize that much. You’re impressive for noticing.”

“Even if they don’t know, wouldn’t they at least guess? It would be strange for someone as important as the Murim Alliance Leader to have no guards at all.”

“Ah. That’s true as well.”

Mae Jonghak scratched his chin like a young man his age and suddenly looked at me. My face was reflected in his clear, deep eyes.

“First, I found what you said in the great conference hall quite impressive.”

“I’m glad to hear that. I don’t know what the others thought.”

“Even if they don’t believe everything, they won’t be able to dismiss it. I promise you that.”

A light remark carried different weight depending on whose lips it came from.

And when the speaker was the Alliance Leader of the Murim Alliance, it was only natural for those words to carry tremendous authority.

*That will give my argument even more weight.*

It was not a bad development. As my expression relaxed slightly, Mae Jonghak smiled.

“You must have been worried.”

“I’d be lying if I said I wasn’t.”

“Since we are on the subject, let me ask you. How certain are you of your own claim?”

“Five-tenths. Fifty-fifty.”

The Thousand-Faced Fox’s face went rigid.

“Did you just say… five-tenths?”

“Is that less than you expected?”

“Damn it. It’s the opposite! You’re saying there’s a fifty-percent chance that the world will be covered in monsters!”

The Thousand-Faced Fox’s lament contained a brief curse, but no one paid attention to it this time.

Rather than feeling offended, I felt relieved.

Their reactions told me that, at the very least, the people gathered here had already accepted my claim as fact.

“What grounds do you have for that fifty percent?”

Mae Jonghak’s question remained calm. I gave him the answer I had already prepared without hesitation.

“Everything I’ve seen and felt while fighting Dark Heaven.”

At that moment, Jeok Cheongang, who had been sipping strong liquor instead of tea, suddenly spoke.

“You could be wrong.”

“I would be more than happy to be cursed out for the rest of my life if that were true.”

I meant it.

I would much rather have my prediction be completely wrong, with Dark Heaven turning out to be nothing special and no mutant monsters ever appearing.

If getting cursed out by everyone meant I could see a happy ending, it would be a bargain.

But…

“It sounds insane, but it’s all true.”

“Damn it. This is driving me crazy.”

“Is it really that hard to believe?”

“I don’t want to believe it. If it were anyone but you saying it, I wouldn’t.”

“……!”

*Where did that sudden burst of emotion come from? What am I supposed to do with this?*

*Thud.*

But emotional or not, to hell with all that. Jeok Cheongang slammed his liquor bottle down and glared at me.

“Tell me it’s a lie instead. If you confess right now, I’ll let you off with three strikes from the Flame Divine Palm.”

“I swear on my balls, right here and now, that I’m not making this up. And three strikes from the Flame Divine Palm would kill me.”

“Whew.”

Jeok Cheongang let out a deep sigh and turned toward Mae Jonghak and the Thousand-Faced Fox.

“This old man doesn’t want to believe it either, but it seems everything that punk says is true. At least when he stakes his balls, he’s sincere.”

“……”

The standard for determining whether something was true was a little strange, but somehow my sincerity seemed to have gotten through.

And just as my worst fears began to take shape, the silence that descended over the office was broken by Mae Jonghak.

“I have one more thing to ask.”

“You can ask two things if you want.”

“No. One is enough.”

*Swish.*

Mae Jonghak crooked one finger as he spoke.

At the same time, a large scroll flew from among the bamboo slips piled behind him and unfurled across the table where we were seated.

*Rustle.*

I stared at what was written—or rather, drawn—on the scroll and muttered,

“This is…”

“You are looking at exactly what you think you are. A complete map of the realm.”

As Mae Jonghak had said, it was a map marked with the geography and terrain of various parts of the realm, along with their names.

But it was larger than any map I had seen in Murim, and there was one particularly notable difference.

“It even shows the locations of the various sects.”

“It was made for the Murim Alliance. Now, let me ask you…”

Mae Jonghak’s calm voice pierced my ears.

“Where do you think Dark Heaven’s next target will be?”

“I can’t be certain.”

“Who in this world can be certain of the future? A simple guess will do.”

*A simple guess…*

I remained silent, lost in thought. Then, suddenly, I raised my hand and pointed to one part of the map.

*Tap.*

“This place.”

The reactions were immediate.

Jeok Cheongang muttered a quiet curse. A sharp light flashed in the Thousand-Faced Fox’s eyes, while Mae Jonghak leaned his upper body toward me.

“Why did you choose that place?”

“If what happened in Hubei happens again, Dark Heaven would be hard-pressed to find a more suitable place.”

“You are referring to that ‘rift.’”

“Yes.”

“Do you believe—or rather, do you guess—that the rift will happen again?”

“I think the possibility is more than high enough. What happened was not a natural disaster. It was something Dark Heaven planned and caused.”

*The word “first” only exists because there is a second.*

Only I had been allowed to glimpse the Water God Dragon’s memories, even if only briefly.

That meant I had no physical evidence or certainty I could confidently present. But the probability that Dark Heaven was targeting *that place* was high.

I continued calmly.

“I don’t know what Dark Heaven is going to do right now. This may not be its next target. But at least one person must have already set out for that place.”

“The Southern Heaven Demon Empress.”

The moment Mae Jonghak spoke the title, countless corpses I had witnessed in Hubei flashed before my eyes.

My fist clenched before I realized it.

“That’s right. If it’s the Southern Heaven Demon Empress… she must have that place in mind.”

“Is that another simple guess?”

“It’s a guess. One close to certainty.”

There was nothing I could be certain of. I merely believed that the thought that had refused to leave my mind for some time carried a considerable likelihood.

Mae Jonghak nodded quietly and turned his gaze toward one person.

“What do you think, Chief of the Hidden Shadow Pavilion?”

“I agree with the Fire Dragon Pavilion Master, and I will add my own support.”

Song Ho answered immediately and continued.

“It has been more than seven days and nights since we sent the dispatch. Since no reply has arrived, there is a considerable chance that trouble has already occurred.”

“I expected that much, but… that was fast.”

“Yes. We could move the Outer Hall forces we had selected in advance, but we might already be too late.”

The Thousand-Faced Fox read the question in my expression and spoke in a calm voice.

“The Hidden Shadow Pavilion’s eyes and ears are scattered throughout the realm. You are not the only one to have made this guess.”

“…You had already been considering that place.”

“To be precise, we began considering it immediately after receiving a report on the circumstances surrounding what happened in Hubei Province. However, that strange phenomenon called a rift was something neither I nor anyone else in this Pavilion anticipated.”

I recalled something I had momentarily forgotten.

The elderly martial artist before me had been the head of the Hidden Shadow Pavilion forty years ago, and he was still its head now.

And there was one person in this room who could issue orders to both him and me.

“Fire Dragon Pavilion Master Jin Taekyung.”

A heavy voice unlike his usual one rang through the office.

Mae Jonghak, the great martial artist known as the Number One Sword Under Heaven and the man standing at the pinnacle of Murim today, stared at me with clear blue eyes.

“I am giving you your first order.”

* * *

*Whoosh!*

A fierce wind rose with every step I took.

Ignoring the eyes of everyone around me, I even used my movement technique to hurry back to my residence. When I arrived, I flung open the door with all my strength.

*Bang!*

The moment the door flew open, I saw a familiar face.

Hyuk Mujin had been lounging around inside the annex before jumping to his feet. He looked back and forth between me and the shattered door, then muttered,

“Welcome back… Wow. The owner is going to cry tears of blood. That door was replaced less than half an hour ago.”

But I had no time to sympathize with the owner’s sorrow.

Instead of greeting him and saying I had returned safely, I tossed out a single sentence.

“Summon everyone.”

“What?”

Hyuk Mujin stared at me, dumbfounded.

“What are you talking about all of a sudden? Wait, summon what?”

“The Fire Dragon Pavilion.”

“What?”

“It’s a mission. Right now.”

“Wait. Hold on! Captain, why all of a sudden? Where are we going?”

I answered the wide-eyed Hyuk Mujin in a low voice.

“Nanman.”
## Chapter artifact 549

# Chapter 549

I was not a general leading an army of thousands.

Even counting me, the Fire Dragon Pavilion had only six members.

It took no more than half an hour for everyone to gather in one place.

“Everyone, pay attention.”

The five people immediately focused their gazes on me, sensing something unusual in the words I had abruptly spoken without so much as a greeting or honorific.

Even Hyuk Mujin, who had gone to summon them, still had no idea what was going on.

I looked over their questioning faces one by one before slowly parting my lips.

“To get straight to the point… I’ve been given a mission.”

There was nothing to leave out or add.

I explained everything exactly as it was, and the short briefing ended in less than fifteen minutes.

Then, just as everyone had fallen silent and begun thinking as though they had made some kind of agreement, one person suddenly spoke.

“So.”

The owner of that calm voice was a familiar face.

Sama Pyo, Young Sect Leader of the Black Dragon Demon Gate, continued while looking at me.

“We’re heading to Nanman.”

I nodded, adding a small correction.

“More precisely, not Nanman itself. The Nanman Beast Palace.”

The Nanman Beast Palace was a mysterious sect that tamed countless animals—including spiritual creatures and venomous beasts—and trained in martial arts modeled after their movements.

I was not sure whether it was an animal protection association or an animal-abuse group, but one thing was certain.

*Honglan. No—the Southern Heaven Demon Empress must be salivating over a place like that.*

Assuming a second “rift” was about to occur, Dark Heaven would have a hard time finding a more suitable location than the Nanman Beast Palace.

It was truly an animal kingdom, a place teeming with more spiritual creatures and venomous beasts than anywhere else under heaven.

Song Ilseom, who had been listening while holding a willow-leaf saber against his chest, muttered,

“Sounds like a miserable journey.”

There was a good reason he had said that.

Nanman, where the Nanman Beast Palace was located, was also called Yunnan in the Central Plains.

It lay directly south of Sichuan and shared borders with Guizhou and Guangxi.

Hearing that, it might have sounded like nothing more than a distant place with no particular problems. But…

*The problem is that Nanman’s geography and climate are unbelievably fucked.*

They said Nanman had a sweltering tropical climate and endless jungles.

There were no well-maintained roads to be found, even if one scrubbed one’s eyes raw. Instead, it was a truly miserable region where fully grown predators and venomous insects treated humans like food delivery.

*That’s only what I’ve heard so far…*

It was difficult to imagine what the place was actually like.

I could vaguely understand why Nanman, despite being properly included on maps of the realm, was still treated as part of the Outer Lands.

*Though from a modern perspective, it really would be a foreign country.*

In the modern world, was Yunnan Vietnam or Myanmar? It had to be somewhere around there, but my memory was hazy because I’d spent world geography class sleeping my ass off.

As I was dredging up those memories, Hyuk Mujin suddenly raised his hand.

“Captain, I have a question.”

“Go ahead.”

“Are we really going?”

“Would we be going fake?”

“I-I think it sounds too dangerous.”

“What does it matter? Everything has been dangerous so far.”

“……You say that so naturally that I have nothing to say.”

“If you have nothing to say, shut your mouth and pack your things.”

“When are we leaving?”

“Ah, did I not mention that?”

I had forgotten something important.

The others had clearly been too focused on the destination and the reason for going to think of it.

I looked at them one by one and tossed out a single sentence.

“Today. Right now.”

“……!”

“……!”

A small ripple spread through the group in an instant. Hyuk Mujin and Taishan, the Tiger Giant Child, were especially affected.

“You’re joking, right?”

“Do I look like I’d joke at a time like this?”

“That makes no sense. What about our clothes and supplies? We need to pack right away.”

“It makes perfect sense. Since when have we ever worried carefully about food, clothing, and shelter? Just bring some fasting pills.”

“Whoosh. Whoosh!”

What the hell? Was that Scorching Yang Qi?

Taishan sprang to his feet, blasting astonishingly hot breath from his nose.

“No! Taishan! Was supposed to eat meat tonight!”

“Meat? Meat sounds good.”

I added one more sentence toward Hyuk Mujin.

“You heard him. Pack some jerky too.”

“Jerky! Tastes bad!”

“……Just shut up and eat whatever the hell you get.”

Look at this guy, who looked like he would eat chopsticks, acting picky about food.

Sama Pyo noticed the meaning in my gaze and shrugged before speaking.

“Taishan. You little rascal.”

“L-Lord.”

“How long are you going to keep behaving so recklessly? If you continue throwing this sort of tantrum, then…”

“Taishan. Won’t do it. Forgive Taishan, Lord.”

The enormous man looked so dejected that I actually felt sorry for him.

*I’ll leave everything involving Taishan to Sama Pyo from now on.*

With that thought, I turned toward Song Ilseom, who was frowning.

“What? Are you dissatisfied too?”

“Of course. It’s Nanman, not somewhere else.”

Song Ilseom clicked his tongue quietly and continued.

“But I’ll overlook it. Unfortunately, I’ve already received a hefty advance payment. And I’m not confident I could afford the tenfold penalty.”

“You’re much more straightforward than I expected. I like it.”

“Once I make a contract, I keep it. If I didn’t, I wouldn’t be known as the Soul-Chasing Guest.”

Song Ilseom tossed out the words with unmistakable conviction and pride, then continued in an even tone.

“Of course, the final decision belongs to the employer, not me. Isn’t that right?”

Naturally, his final question was not directed at me.

Ju Hwaran, the Dagger Hidden Flower, had been sitting in silence and lost in thought from beginning to end. At last, she opened her mouth.

“I think you already know what answer I’m going to give. Don’t you?”

Her clear, gentle voice pierced my ears. I let out a quiet laugh, while Song Ilseom sighed softly.

“I knew this would happen. Damn it. Nanman.”

“I trust I don’t need to remind you of the terms of the contract, Great Hero Song.”

Song Ilseom continued groaning behind her as Ju Hwaran stared at me.

My face was reflected in her dark blue eyes, which held a mysterious light. Seeing them from this close, they looked almost…

“Great Hero Jin?”

“Ah, yes.”

*What was I just thinking? Did I doze off for a moment?*

Ju Hwaran’s call brought me back to my senses.

*No. Don’t.*

This was already a problem. Considering what lay ahead, I needed to face every situation with a clear head.

After repeating that to myself several times and pulling myself together, I spoke as calmly as possible.

“That’s good. I had something to ask you anyway. Namely…”

“About the fastest route to Nanman and what we’ll need? All right.”

“Pardon?”

“Why? Was I wrong?”

“No. That’s not it.”

*It was the exact opposite. She was so accurate that she startled me.*

*What the hell? Has she learned mind reading? Some kind of mind-reading technique?*

As I blinked speechlessly, Ju Hwaran gave me a bright smile.

“There’s no need to be surprised. I’ve been thinking about what I could do since earlier.”

“Oh.”

“I’m now officially a member of the Fire Dragon Pavilion, so I should do my part, as I said I would.”

Tap. Tap-tap.

Her rough, snow-white fingers struck the tabletop at a steady rhythm, as though reminding us that she too was a swordswoman.

Then her voice continued.

“First, as Great Hero Jin said, it would be best to keep our supplies to a minimum. We won’t need extra clothing, and two days’ worth of food in the form of dry rations should be enough.”

“Dry rations? Please, anything but that! Taishan will die!”

At Taishan’s wail, Ju Hwaran quickly added,

“Of course, we’ll bring jerky too.”

“What the hell is his guardian doing? Ah, Young Lady Ju, please continue.”

“Of course. Then…”

After removing the troublesome one from the discussion, Ju Hwaran continued without hesitation.

She went over everything, from the supplies we would need to the fastest route to Nanman.

Fortunately, she had traveled to Nanman on an escort assignment several years earlier. Through the records left behind by her grandfather, the Escort King, she also knew the terrain and hidden roads in various places.

Even Song Ilseom, who had lived as a wandering martial artist and traveled throughout the realm since he had been a snot-nosed child, expressed his surprise.

“There was a road like that?”

Ju Hwaran nodded confidently.

“Of course. According to my grandfather’s records, it’s definitely there.”

“I also stayed there for about a year. But as far as I know…”

“According to my grandfather’s records, it’s definitely there.”

“No, I know that. What I mean is—”

“My grandfather’s records.”

“Excuse me. Could you let me finish?”

“The Escort King.”

“……I believe you. I believe you, so please continue.”

Who was the Escort King?

He was the legend among legends who had successfully completed that legendary Ten-Thousand-Li Journey even while a hundred thousand Demonic Cultists covered the realm.

The will of that very P-King lived on in Ju P. Hwaran.

Like the Going Merry hitting open water, she sailed ahead without a hitch, and before even half an hour had passed, she had completed the entire route plan for traveling to Nanman.

“Whew. I think that covers everything for now. Does anyone have any questions?”

Whoosh!

A thick arm, large enough to belong to a Troll, shot into the air.

“Yes, please ask anything.”

Tiger Giant Child Taishan opened his mouth with a stiff expression.

“Taishan. Understood nothing after jerky.”

“……”

“……”

*Which bastard brought a kid into a no-kids zone?*

I glared sharply at one person.

“Hey, guardian.”

“My apologies.”

Smack.

“Mm. Mm!”

Sama Pyo immediately clamped a hand over Taishan’s mouth after my sharp rebuke, then gave Ju Hwaran a small nod.

“My apologies.”

“……It’s all right.”

Her tone was calm, but she could not hide the lowered voice that accompanied it. Given the circumstances, it could not be helped.

No, it was only natural.

*Even if it was a political marriage, they had been formally engaged.*

Those big-nosed Hollywood bastards, supposedly as cool as ice magic, might be different. Modern Korea, where I had lived, and Murim were both full of Confucian girls and Confucian boys.

It was awkward even for me to watch. How much worse must it have been for Ju Hwaran?

*I don’t even know exactly what happened between them.*

The thought left me feeling strange.

For some reason, the texture of the fabric against my skin began to irritate me. It felt as though someone invisible were poking me again and again with a small, thin needle.

“Captain?”

“Hm?”

Hyuk Mujin’s voice broke through my brief reverie.

I did not even need to turn my head to confirm it. I could feel the gazes fixed on me.

I steadied my scattered thoughts and spoke as casually as I could.

“All right. We’ll move according to what we’ve discussed. Minimal supplies. The time we have is…”

Ju Hwaran answered when she saw my gaze.

“Half a shichen.[^1] Half a shichen at most should be enough. We’ll need to quietly arrange the necessary horses and carriages without attracting attention.”

“Where should we gather?”

“Hmm. What do you think, Great Hero Jin?”

This was not a public mission. We had to move as quickly as possible while remaining discreet.

And to quietly leave the area, which was teeming with countless people, we first needed to split up and choose a secondary meeting point.

“Mount Daebyeol. We’ll meet there.”

“That sounds good.”

Ju Hwaran and the others nodded at the answer I had settled on after careful thought.

[^1]: A shichen is a traditional time unit lasting approximately two hours.

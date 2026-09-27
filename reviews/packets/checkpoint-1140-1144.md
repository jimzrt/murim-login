# Checkpoint Review — 1140–1144

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

# Chapters 1140–1144

## Plot

The Son of Heaven enfeoffs Jin Taekyung as Prince Shangshan and offers him the title Prince of Ye, which he declines. Murim leaders gather in Xining to honor him. After avoiding the Bow Saint for three days, Taekyung meets her by the river. She recounts how the Martial God united Murim and vanished after defeating the Heavenly Demon, then says he wanted to find Taekyung for the sake of the realm. Taekyung suspects she is withholding part of the truth.

Jeok Cheongang wears the pocket watch Taekyung had kept in his Inventory. Jeok says he found it where Taekyung collapsed ten days earlier. Holding it recalls that The Helper gave it to Taekyung as a final gift; its System classification changes from Common to Special, and its Item information says it holds a secret. Hyuk Mujin remembers that its hand has moved, and Taekyung realizes it has moved backward and may have circled one or more times. Taekyung suspects The Helper was the Martial God, and that the Martial God was Cheon Taemin, whose consciousness the System may have preserved in the Inventory. He tells Jeok he has something to discuss.

After Mae Jonghak declares the campaign a fight to protect the realm, more than two hundred thousand troops leave Xining for a cursed forbidden land beyond the desert to fight the Lord of Heaven. Before dawn, Taekyung leaves in a prepared carriage to pursue an unspecified plan and falls into a deep sleep; Jeok waits with the others.

## Continuity

- More than two hundred thousand Murim forces are marching from Xining toward a cursed forbidden land beyond the desert to fight the Lord of Heaven.
- Taekyung left Xining asleep in a prepared carriage to pursue an unspecified plan; Jeok Cheongang is waiting for him.
- Taekyung suspects The Helper was the Martial God and that the Martial God was Cheon Taemin; he theorizes the System preserved Cheon’s consciousness in the Inventory. None of this is confirmed.
- The pocket watch, The Helper’s final gift to Taekyung, returned from the Inventory and was found where Taekyung collapsed. Its classification changed from Common to Special, and its Item information says it holds a secret. Its hand moved backward from the position Hyuk Mujin remembers.
- The Bow Saint says the Martial God sought Taekyung for the sake of the realm; Taekyung suspects she has withheld part of the truth.

## Translation Decisions

- Render 上山王 as “Prince Shangshan” and 寧王 as “Prince of Ye.”
- Render 合從軍 (합종군) as “coalition army” and 팔황 as “Eight Directions.”
- Render 회중시계 as “pocket watch” and 누가 만들었는지 모를 회중시계 as “Pocket Watch of Unknown Make.”

## Durable state

{
  "active_continuity": [
    "More than two hundred thousand Murim forces are marching from Xining toward a cursed forbidden land beyond the desert to fight the Lord of Heaven.",
    "Taekyung suspects The Helper was the Martial God and that the Martial God was Cheon Taemin; he theorizes the System preserved Cheon’s consciousness in the Inventory.",
    "The pocket watch’s hand has moved backward from the position Hyuk Mujin remembers, and its Item information says it holds a secret.",
    "Taekyung left Xining asleep in a prepared carriage to pursue an unspecified plan; Jeok Cheongang is waiting for him."
  ],
  "continuity_sources": [
    1143,
    1144
  ],
  "open_questions": [
    "Are Cheon Taemin and the Martial God the same person, and was Cheon’s consciousness preserved in the System?",
    "What is the pocket watch’s secret, and why did it return from the Inventory?",
    "What is the time ratio between the modern world and Murim?",
    "Who is The Helper, and what is his relationship to the System?",
    "What plan is Taekyung pursuing, and what will happen in the campaign against the Lord of Heaven?"
  ],
  "safe_through": 1144,
  "temporary_decisions": [
    "Render 大明 as “Great Ming” and 親征 as “personal expedition.”",
    "Render 滅魔正天 as “Exterminate the Demons and Set Heaven Right.”",
    "Render 회중시계 as “pocket watch” and 누가 만들었는지 모를 회중시계 as “Pocket Watch of Unknown Make.”",
    "Render 팔황 as “Eight Directions” and 합종군 as “coalition army.”"
  ],
  "version": 1
}

## Reading copies

## Chapter artifact 1140

# Chapter 1140

Long before the countless government and Murim forces appeared, hundreds of banners flying in the wind, the people of Xining City were already bursting with excitement at the news of reinforcements.

“I never thought I’d live to see a sight like this.”

The imperial court and the Murim Alliance, united.

That alone was unprecedented in the history of the continent. But the people gathered under those banners were just as extraordinary.

“T-The Nine Sects and One Gang, and the Five Great Families, too? All of them?”

“That’s right. They’ve even rooted out every last one of those Dark Heaven bastards’ dark arts planted in the Central Plains. What is there to fear now?”

“I-I heard the Silver Flash Spear Hero and the Taebaek Divine Elder have joined them, too.”

“Hold on. The Silver Flash Spear Hero, sure—but wasn’t that old Taebaek Divine Elder a dark-path figure?”

“……I’m a dark-path figure, too.”

“Oh, right. I forgot. You’re with the Yangtze River Channel League.”

“Just laugh it off. Don’t ruin the mood.”

The leaders of the most renowned orthodox sects. Great Heroes who had roamed the realm alone. Even reclusive masters who had supposedly died long ago.

The orthodox martial artists weren’t the only ones unable to hide their excitement. Even the dark-path martial artists, who reached for their weapons at the slightest provocation, felt it this time.

They had already fought alongside the legends known as the Three Saints, but wasn’t this the true unification of the realm?

Even during the terrible Great Faction War, the power of the entire Murim had never gathered in one place with such unity.

And just like the martial artists, the government troops and commoners couldn’t hide their trembling excitement, each for their own reasons.

The Son of Heaven.

A descendant of the dragon.

The father and ruler of all people, sent by Heaven to this land.

They could scarcely believe their ears when they heard that the man said to be impossible to see even if you lived in the Imperial Capital was personally leading a great army here. Before long, they learned it was true.

The Son of Heaven’s lofty authority and grace, known to them only through rumor.

And—

“It’s been a long time, Marquis of Shangshan Jin Taekyung.”

Even his connection to one particular person.

But the Son of Heaven’s next words were something no one there could have predicted.

“No, I suppose I should call you Prince Shangshan now.”

“……!”

“……!”

The sudden sense that the air around them had crackled wasn’t the delusion of just one person.

Martial artists, government troops, commoners.

They all wondered for a moment if they’d shared a collective hallucination. Then, as they looked at one another with wide eyes, they understood.

They hadn’t misheard. Not at all.

The Son of Heaven had just declared it.

No—proclaimed it.

He would enfeoff that young man, not a single drop of whose blood was noble dragon’s blood, as a prince.

A king with a different surname, gone from history for hundreds of years, had just been born anew right here.

And amid the unprecedented scene that had frozen everyone in place, Jin Taekyung—who, for some reason, was staring into empty space—suddenly spoke.

“Wow. The EXP for that achievement is insane.”

“……?”

“……?”

What the hell was he talking about?

Having thrown everyone into confusion with words no one could understand, Jin Taekyung looked straight at the Son of Heaven and continued.

“Your Majesty.”

His expression was utterly serious.

“Since you’re handing them out anyway, could you give me a few more royal titles while you’re at it?”

The Son of Heaven burst out laughing. The people, stunned for a moment, all had the same thought.

He really was a complete madman.

But the madman who’d just become a king wasn’t done yet.

* * *

Afterward, people had to keep asking themselves, over and over, to remember what Jin Taekyung was like.

They’d heard rumors about him here and there.

Before long, they were able to confirm them with their own eyes and ears.

“Is Prince Shangshan not enough? It was also the title held by my younger brother, so it carries considerable significance.”

“Oh, it’s plenty. It’s great. I was just wondering if I could get one more. Hehe.”

At Jin Taekyung’s shameless request for another royal title—as if he were asking for extra broth with his noodles—everyone held their breath.

Some even thought the Son of Heaven, known for his iron-blooded rule, would punish Jin Taekyung on the spot.

That is, for a very brief moment.

“If you tell me why, I see no reason to refuse.”

Huh?

“Um. It’s a little awkward to explain in detail. I’m just giving it a try.”

Why?

“Hm. You must have your reasons. Then you may also take the title of Prince of Ye in Hebei.”

What?

“Thank you, Your Maj—oh.”

“What is it?”

“Nothing. I’ll pass on Prince of Ye. Ah, I guess you can’t have duplicates.”

“I don’t know what you mean, but do as you please.”

……Seriously, what was going on?

The people who’d watched every moment of this exchange were half out of their minds.

Even after the Son of Heaven had traded a few more laughs with Jin Taekyung and headed toward the Inner City with the Imperial Guards, the shock they felt didn’t fade easily.

No—instead, a different kind of shock was waiting for them.

*Thud-thud-thud-thud!*

A flood of men and horses poured through the wide-open city gates, followed by countless banners bearing the emblems of the great sects.

The people who saw the figures emerging with extraordinary auras and gleaming eyes let out cries of amazement. Then a familiar feeling struck them.

And with it, the same shock as before.

“Benefactor Jin, do you remember me?”

“Daoist Jin. You’ve been through so much.”

“Long time no see. Are you hurt?”

Monks and Daoists from the Nine Sects and One Gang, along with renowned masters from the Five Great Families.

As if they’d planned it, they gathered around Jin Taekyung. He greeted the towering figures of the realm’s Murim as casually as if nothing were out of the ordinary.

“How could I forget Master Unnamed? But you’ve gotten even more muscular since I last saw you…… Wow.”

Unnamed, the sole Disciple of Dharma King Hong Dao, and the man who had sworn not to take the seat of Abbot of Shaolin until Dark Heaven was rooted out.

“Heavenly Sword True Person, you came, too. Oh, Cheongpung? He was over there, but now he’s gone. By the way, did your Disciples come with you?”

The Heavenly Sword True Person, who was the Sect Leader of Huashan first and foremost, not merely Sword Saint Mae Jonghak’s Disciple.

And—

“You haven’t changed a bit, Daoist Jin.”

“We owe you a great debt for what happened in Sichuan. If it hadn’t been for you……”

“That reminds me of what happened in Hubei.”

Other Sect Leaders, Family Heads, and heads of sects.

Even an Elder of a great sect could barely get a foot in. Anyone below that rank couldn’t get close enough to greet Jin Taekyung.

There simply wasn’t room.

Surrounded by the leaders of the great sects—including Emei, Wudang, and the Beggars’ Sect—Jin Taekyung looked like a sight straight out of a hallucination.

The arrival of the Sichuan Tang Clan’s Family Head, whose foul temper everyone knew about, and the Palace Lord of the Nanman Beast Palace, whom they’d only heard of in rumors, poured oil on the fire.

“I’ve come to pay my respects to the Tang Family’s Benefactor. Please forgive me for being unavoidably late.”

Tang Sadok, the Myriad-Poison Asura, was said to prefer a drop of poison to a word of conversation. Yet he clasped his hands in a deeply respectful salute.

“Damn it. I thought they’d come to Sichuan, too… But I was held up by those bastards. Even feeding them to that tiger wouldn’t have satisfied me. I have no excuse.”

Yayul Cheok, the burly man wrapped in tiger hide, even lowered his head and watched Jin Taekyung’s face for a reaction.

As if he were a criminal.

“……Was he really this important?”

At the muttered words that slipped from someone’s lips, those who had watched the whole scene felt a shiver they couldn’t explain.

Who were these people?

They were titans who represented the Murim beyond their own provinces, across the entire realm.

Even if Jin Taekyung was the Fire King’s Disciple, there should have been a world of difference between him and those people, given the gulf in age and the forces under their command.

But today, they finally understood.

Or, more accurately, they saw and felt the truth they’d only vaguely suspected until now.

Just how much influence Jin Taekyung held in this world.

And, at the same time, they suddenly sensed it.

The age of the stars and kings was drawing to a close.

That young Divine Dragon, coiled among countless towering trees, was the hero who would swallow the dark clouds of Dark Heaven and soar into the boundless sky.

At last—

A new age was beckoning to the realm.

* * *

Getting away from the gathering hadn’t been easy.

Everyone who’d met me before wanted to greet me, and so did people who’d never met me.

“Great Hero Jin!”

“Oh, yes. Nice to meet you.”

“Please have a drink with me! I’ll treasure it as the honor of a lifetime!”

“I think I’ve heard that about fifty times already…… But sure, pour me one.”

With joy overflowing everywhere, it was only natural that the wine would overflow, too.

I’d clasped hands in salute hundreds of times and received dozens of drinks.

Xining City had long since become one enormous banquet hall. It took a long time before I could finally make my way out.

“Mother, our youngest is a king now. Sniff, sob.”

“Mother Goddess Heaven! Unbeliever Hell! The great Earth Mother Goddess will punish that fucking Lord of Heaven!”

“Long live the Emperor! I’ll cross the desert right now and smash those rebels’ heads in……!”

“……”

This is a mess.

Jin Wikyung had dropped the stern-and-serious act and started crying as soon as he got drunk. The Earth Mother Goddess’s fanatics—who by now practically regarded her as Nanman’s One God—were shouting their slogans.

I left the cries of Great Ming’s subjects, all fired up with loyalty, behind me and walked off alone.

Until all that noise had faded away.

Past the East Gate, as far as the river beyond the reach of Xining City’s lights, which filled every street.

And there, I came face-to-face with someone I hadn’t seen in the past three days.

No—I’d deliberately avoided seeking her out to sort through the thoughts tangling around in my head.

*Shhk.*

My foot pressed slowly into the wet sand, leaving a soft depression.

Standing beside the Bow Saint, I watched the rippling river in silence.

For a long, long time afterward.
## Chapter artifact 1141

# Chapter 1141

The Bow Saint’s lips, long pressed shut, finally parted as the music drifting from beyond the distant city walls began to fade.

“It sounds lovely.”

I wasn’t sure.

I didn’t know whether she meant the sound of the river flowing by or the laughter carried on the breeze.

I could only answer with a quiet nod.

“After a hard-won battle, there was always a feast like that. People would laugh and chatter until dawn, passing cups of wine back and forth without pause.”

The Bow Saint’s soft voice carried memories she’d held onto for a long time.

And in the scene slowly taking shape before my eyes, she must have been just as alone and apart from everyone as she was today.

“They must have wanted to laugh, even if only for a little while. They needed days like that to take even one more step forward.”

Enough time had passed for the mountains and rivers to change hands several times over, but the human heart remained the same.

Then and now, the survivors gathered together and raised their cups.

One for the joy of victory. One to honor their fallen comrades.

And one more for the time they had left, which might be their last.

That was why this was both a feast and a memorial service.

“But I could never join them.”

I’d been staring silently at the river. Only then did I part my lips.

“Why not?”

“The weight pressing down on my body and mind was too much to bear. I was so worried about what lay ahead that I couldn’t even let myself feel those fleeting emotions.”

For the first time, she took her gaze off the river and looked at me, her eyes as composed as ever.

“And whenever that happened, someone would come over without a word and stay by my side.”

“……!”

My fingertips trembled before I could stop them.

I knew.

I knew who the Bow Saint was talking about.

What I hadn’t guessed was that she’d also figured out why I’d come to see her.

“So, what do you want to hear?”

I took a moment to steady my breathing beneath the Bow Saint’s gaze, as if she could see straight through me.

Then I answered.

“The Martial God. I want to know everything about him.”

No.

I needed to know now. I had to.

* * *

Several decades ago, there was a man.

His sect, his face, even his name—none of them were properly known.

But the first time he appeared in history, everyone under Heaven learned of his existence.

“He was like… a divine man who had descended from the heavens.”

In the early days of the Great Faction War, the Demonic Cult drenched Kunlun Mountain in blood and fired the first shot of the war. As the Hundred Thousand Demonic Disciples bore down like a giant wave, the Central Plains Murim fell into utter chaos.

Until *he* appeared.

“Three Supreme Peak fiends, and five thousand Demonic Cultists. After suffering a crushing defeat in their first battle, the Kongtong Sect tried to retreat to Shaanxi at once, but they were caught before they could get far. The reinforcements they hastily gathered couldn’t keep up with the Demonic Cult’s speed.”

And on that day—

A man no one knew stood in the pursuers’ path, and a new sky opened.

“Before even half a day had passed, every enemy had been killed or captured. It was hard to believe one person had done it all.”

But the Huashan reinforcements, arriving late, saw everything with their own eyes.

Amid a battlefield that looked as though a storm had swept through it, a man stood alone among countless corpses.

They were all stunned. They shuddered with awe.

One of them must have felt something beyond awe: the man leading the reinforcements, the head of the Plum Blossom Swordsmen of that generation, who at barely thirty was revered as the Number One Sword Under Heaven.

“Mae Jonghak immediately spread the news to the whole realm, and before long, everyone knew: there was another supreme being who would stand against the Heavenly Demon and protect the Central Plains.”

And so the Martial God was born.

The years of war that followed, lasting more than a decade, became the legend he wrote.

Victory, and more victory.

There were countless defeats and moments of despair, too. But there was also glory and praise, as hot and dazzling as the sun.

He united the Nine Sects and One Gang and the Five Great Families beneath the banner of the Murim Alliance, even as they repeatedly split apart and came back together. He sought no personal gain, pursuing only benevolence and righteousness.

A great hero of his age, held in awe by all.

“I watched it all from close by. Again and again, I marveled at the string of achievements beyond words. There were those who dared to envy him, resent him, and doubt him, but before long, even they came to admire the Martial God deeply.”

Who under Heaven could look straight at the sun?

And without the sun, how could anyone live in this world?

The Martial God was the heavens—and the sun itself.

No matter how many jiazi of internal energy one had accumulated, no matter how high one’s martial prowess, no one dared look straight at him.

Afraid of being blinded, they could only bow their heads in the end.

And the Martial God proved himself.

He defeated a supreme being unlike any other in the thousand-year history of the Demonic Path, then disappeared without a trace not long afterward.

Glory. Honor. History.

Even this vast realm of Murim.

The Martial God cast aside everything he had built without a trace of attachment and left.

“And that was when the legend finally became a myth.”

The Bow Saint raised her head and looked up at the sky.

In the pitch-black night, the stars glittered like her title, though beside the vast heavens above they were little more than tiny lights.

“Those who lived in the same era as me know. The Martial God was truly a miraculous being. No one under Heaven could ever accomplish what he did.”

When her long story ended, silence settled. I’d been looking at her without a word when I suddenly parted my lips.

“Is that all?”

The Bow Saint’s gaze, fixed on the sky, slid slowly toward me.

“What do you mean?”

“I already told you. I want to know everything about him.”

“……Why would you think that isn’t everything?”

Her answer came back just a little too late.

For an instant, I thought her eyes had wavered ever so slightly. Was that just my imagination, or had I mistaken the river reflected in them for a flicker in her gaze?

I hid the question rising in my mind and spoke again.

“I expected a somewhat different story. Of the people I know, you spent the longest time with the Martial God. And you were the one who received his letter.”

“How could I tell you everything about more than a decade in such a short time? Besides, there are plenty of people who remember what he did. Even if I stayed a little closer to him, that wouldn’t change.”

Her voice was as calm as ever, despite the brief flicker of agitation she’d shown a moment earlier.

“The same goes for the letter. In keeping with his final wish, I spent many years searching for the ‘chosen one.’ That’s why we’re here together now.”

That was true. I knew it, too.

The Bow Saint’s words were borne out by the fact that she’d spent decades wandering all over the realm.

And I knew that the woman before me had walked a difficult path as a chivalrous warrior—one I wasn’t qualified to judge.

But I thought her answer was both completely true and incomplete.

*She’s definitely hiding something.*

This wasn’t a passing guess. It was a conclusion drawn from instinct and cold reason.

For all the times we’d shared life and death, short as it had been, the Bow Saint had repeatedly refused to join the rest of our group.

And most importantly—

*That battle ten days ago.*

I remembered the story the Slaughter Saint had cautiously told me the night before, when he came to see me alone.

The Bow Saint’s inexplicable words and actions that day.

Putting it all together, she’d been closer to a bystander than anything else.

At least when it came to whether I lived or died.

*What if our positions had been reversed?*

I’d already turned the question over in my mind more times than I could count. It didn’t even need thinking through.

I would have done everything I could to save the Bow Saint.

Whether I’d moved on instinct or reason.

But she hadn’t.

On the day of the great battle surrounding Xining, she’d told the Slaughter Saint, who wanted to save me, that if Jin Taekyung died that day, then it was fate.

Of course, she wasn’t wrong.

When countless people were dying in every direction, how could one life matter more than another?

But why had the Bow Saint, who’d spent decades searching for the “chosen one” based on nothing but an old letter supposedly left by the Martial God, been so indifferent to my death?

Could it be…

Could she have…

*No. The Martial God…*

Just as I drew in a sharp breath—

*Splash!*

A surge of river water rushed up and touched my toes.

The cold seeped through my leather shoes. Snapping out of my deep thoughts, I instinctively stepped back.

Then I met a pair of eyes watching me intently.

“There’s one last thing I’d like to ask.”

The Bow Saint gave a small nod, and I continued, my voice already trembling.

“Why… did the Martial God want to find me?”

The Bow Saint answered at once.

“For the sake of the realm. That’s all.”

Her eyes shone clearly, and her voice was firm.

I could feel it instinctively.

This was the truth.

Not a single trace of a lie or ill will.

And for now, that was enough.

*For the sake of the realm.*

I swallowed the short phrase that kept ringing in my ears and bowed my head to the Bow Saint.

“Thank you.”

“Was that enough of an answer?”

“To some extent, yes.”

“I’m surprised. I thought you’d want to know more about him.”

“I’d be lying if I said I wasn’t disappointed, but what you’ve told me already helped a lot.”

I wasn’t just saying what she wanted to hear. I wasn’t lying.

Hearing about the beginning and end of the being called the Martial God had finally made me certain of the identity of another person like him—one who had existed beneath a different sky.
## Chapter artifact 1142

# Chapter 1142

Even though the hour of the Rabbit had already begun, the lights of Xining City showed no sign of going out.

People wept and laughed, passing cups of wine back and forth without end as they surrendered themselves to drunkenness.

No—they had no choice.

Wine helped people forget their many emotions.

They could pretend not to notice the tears they’d shed without realizing it, or someone’s wails over the loss of a loved one, and blame it all on the drink.

But one man was different. Sitting on the roof of the tallest pavilion along the main road, he stared silently down at the streets below.

“What are you doing up here?”

At the uninvited voice that suddenly came from behind him, the Fire King, Jeok Cheongang, answered gruffly.

“Just thinking.”

“Thinking?”

“What, do I look like a man who never thinks?”

“Of course not. Your lie was just painfully obvious.”

The uninvited guest—the Slaughter Saint—plopped down beside him without permission and added with a snort of laughter, “Why not be a little honest for once? You could start by admitting you haven’t touched a drop of wine because you’re waiting for your one and only Disciple.”

“……”

“You worry too much. Especially for a Master whose Disciple is the most outstanding man under Heaven.”

At that, Jeok Cheongang’s brows, which had been wriggling like a caterpillar, arched gently.

“Hm. The boy is pretty good.”

“Pretty good? Who else at his age has achieved anything like that, in all of history?”

“Now, now. He was just lucky. He’s still a long way from meeting my expectations.”

“……Then why are you grinning like an idiot?”

“You must be drunk. You’re imagining things.”

Jeok Cheongang’s mouth twitched as if he were having a spasm. The Slaughter Saint shook his head and spoke.

“Anyway, don’t worry for nothing. He must have had a lot to discuss with the Bow Saint.”

“Oh, he went to see the Bow Saint? I had no idea.”

That was true.

Of course, Jeok Cheongang had been waiting for more than two shichen, ever since Jin Taekyung had quietly slipped away. But anyway, he had no idea.

“Would you stop pretending? Not even a toddler would believe your lies.”

Even with his thoughts completely exposed, Jeok Cheongang held onto his usual confidence.

“I’m serious. Besides, I’m not even sure who this Bow Saint is.”

“……Enough. Are you going to pretend to be senile just to get away with one lie?”

“A martial artist should be willing to give up flesh to take bone.”

“It’s the other way around in this case.”

“If I give up bone and take flesh, I still come out ahead. My bones are solid.”

“Now you’re talking nonsense like Jin Taekyung. When it comes to things like this, Master and Disciple really are……”

The Slaughter Saint let out a small sigh and turned away.

He’d gone out of his way to look for them because neither Master nor Disciple was anywhere to be seen, but somehow, both the old and young members of the Fire Gate Clan gave him a headache.

Still, there was something he wanted to say to Jeok Cheongang.

“This might be presumptuous, but may I say something?”

“Absolutely not.”

Ignoring the gruff reply, the Slaughter Saint continued.

“Don’t blame yourself so much.”

“What?”

“It wasn’t your fault that the boy nearly died ten days ago. Nor was it your fault the Dharma King and the Thunderbolt Saber King died.”

“……”

“If you’re guilty of anything, then fine—blame yourself for having a Disciple who’s too outstanding. As for the other two, you can make it up to them by tearing the Lord of Heaven to pieces.”

The Slaughter Saint started to walk away, leaving Jeok Cheongang sitting in silence.

“Do you happen to have any wine?”

“Of course.”

“Leave it here.”

“Ask a little more politely, and I might consider it.”

“Fine. But first, shall we get our ages straight?”

“Come on. That’s harsh, when we’re both getting old.”

With a quiet laugh, the Slaughter Saint tossed the gourd at his waist over his shoulder and left. Once alone again, Jeok Cheongang slowly tipped the gourd full of wine.

Looking toward the Central Plains, spread out thousands of *li* away, he poured the wine onto the ground.

“Monk, and you too, Peng. It may not be much, but make do with this for now. I’ll hold a proper memorial for you in Xinjiang.”

Then, in the next moment, Jeok Cheongang spotted the East Gate beginning to open beneath the hazy moonlight and smiled.

“With my outstanding Disciple.”

*Whoosh.*

Something around his neck glinted as he kicked off the roof and vanished.

* * *

Leaving the Bow Saint behind, I walked alone through Xining City’s dark, winding alleys.

The main road still blazed with colorful lights and rang with countless voices, but there was only one presence on my mind.

*The Martial God.*

This wasn’t the first time I’d heard about him.

More accurately, I’d already heard more than enough.

The Martial God’s deeds, beginning as legend and ending as myth, had long since become sacred and untouchable.

Though their memories varied somewhat, every martial artist I’d met so far had praised the Martial God, regardless of status.

And that string of events felt all too familiar to me.

*Cheon Taemin.*

Better known as the Slayer.

Or Sky, the title he’d earned from his surname.

His footsteps as humanity’s savior and an unprecedented Great Hero were astonishingly similar to those of the Martial God.

Similar enough to make my spine go cold, beyond the point of mere déjà vu.

*At first, I thought they were just alike.*

It hadn’t seemed all that strange.

Heroes with a great mission appearing to quell an age of chaos was something that had happened from time to time throughout history. And to me, Cheon Taemin and the Martial God had seemed like two such heroes.

Yeah. That was what I’d thought.

Until I heard an unbelievable story from someone’s lips just a few months ago.

*“So it was you. You’re the ‘chosen one.’”*

The Bow Saint.

She had been living in the imperial court in disguise, searching for me for a long time.

No—searching for the Player hidden behind the title of chosen one.

*“Blazing Flame Divine Dragon Jin Taekyung. The moment I saw you rise again after suffering what should have been a mortal wound, I finally knew who the chosen one he spoke of was.”*

It was as vivid as if it had happened yesterday.

The shock of that day, like a bolt of lightning driving into the top of my head.

*That was when I started to suspect the Martial God’s identity.*

But finding the answer to that question hadn’t been easy.

After that day, the Bow Saint kept her lips firmly shut, and I’d had no time to spare as I dealt with the flames erupting across the realm.

What’s more, this question seemed to have an obvious answer at first glance, but one thorny problem stood in my way, impossible for me to explain.

*If Cheon Taemin and the Martial God are the same person…… how did I come to Murim?*

The capsule.

That beat-up hunk of junk that had appeared before my eyes out of nowhere was a passage connecting the modern world and Murim. The thin *User Manual* that came with it contained all kinds of information.

Manufacturer, date of manufacture, precautions.

And finally:

Main Features.

> A capsule customized just for one person! Once a user is registered, the capsule is permanently bound to them, and remains so until their death.

Those two lines, at the very top of the Main Features section, were enough to drag me into an endless maze.

After all, I was one of the few people who had seen Cheon Taemin alive with my own eyes.

Granted, he was as good as a vegetable, but there was no doubt he was still breathing.

*Which made it even harder to explain.*

If, as I suspected, Cheon Taemin was a Player who had owned the capsule in the past and had become the Martial God, how could I have acquired ownership of it?

But now it was time to reach some kind of conclusion to this old question.

I decided to adjust my tangled train of thought.

In a very simple way.

*“Which is more likely: that they’re the same person, or that they’re two different people?”*

Even after I regained consciousness, I’d kept asking myself that question over and over.

And the answer had come to me long ago.

*“First: Cheon Taemin and the Martial God are the same person.”*

And second—

*“The System may have recognized Cheon Taemin’s unconscious state as a form of death.”*

Though the second guess was uncertain, after thinking it through as deeply as I could, it was the closest thing to the right answer.

*“There’s one more thing that bothers me: the time ratio……”*

The timelines of the Great Cataclysm in the modern world and the Great Faction War in Murim differed by a factor of about two.

But that was nowhere near the time ratio the System had given me.

One of the biggest reasons I’d been able to grow so quickly was that absurdly generous time ratio.

*“There must be something else I haven’t figured out yet.”*

The System was meticulous.

It might seem capricious at times, in ways I couldn’t understand, but it followed set rules, and there was a valid reason for everything it did.

So it wouldn’t be strange if there were specific conditions or secrets it didn’t reveal unless a Player figured them out for himself.

That was how the System had always worked, and how it would keep working.

And among all the thoughts tangled in my head like a skein of thread, only one presence remained.

“……Who in the world is that old man?”

The Helper.

This was the second time I’d met him face-to-face.

When I first set foot in Murim, he’d been part of the System and taught me to circulate my qi. This time, he’d saved my life.

If he hadn’t guided me to a higher level of enlightenment, I’d surely be a cold corpse by now, buried in Xining City’s graveyard.

Or stuffed into an urn personally picked out by Jeok Cheongang.

Anyway, what mattered was that he wasn’t just the System. He was some kind of special being.

“Yeah. He’s definitely different from what I knew before.”

Just then, my mutter echoed through the dark alley.

“What nonsense are you talking about now?”

The voice sounded gruff at first, but carried a warmth it couldn’t hide.

When Jeok Cheongang suddenly appeared, I started to smile.

Or I would have—if I hadn’t seen the object hanging around his neck.

“……!”

My eyes flew wide, reflecting a pocket watch glinting in the hazy moonlight.
## Chapter artifact 1143

# Chapter 1143

It took three steps to get my stalled brain back up and running.

First, roughly thirty seconds of silence.

Second, someone’s muffled shout, as if it were echoing from deep underwater.

And finally, the grand third step.

Whoosh!

A figure strode closer, and a palm came flying at me with a sharp whistle.

Smack!

Light flashed before my eyes.

As my dulled senses returned, the breath I’d unknowingly been holding burst out of me in a gasp.

“……A-are you back with us?”

I could barely answer. All I managed was a blink.

Jeok Cheongang had come right up to me, staring with a look that mingled confusion and concern.

And peeking out from the gap in his robe, as if it were a third eye, was an object glaring right back at me.

“T-that. That thing.”

“What?”

“No, I mean, uh……”

So much for my brain being back up and running.

My tongue had gone stiff. I couldn’t get the words out, like the mute Samryong. It wasn’t until I saw my Master raising his hand again—for his Disciple’s sake, naturally—that I finally came to my senses.

“W-wait!”

Smack!

Ah, the eardrum-rattling grace of a Master’s boundless kindness.

“……I said wait.”

Jeok Cheongang flinched at the betrayal in my eyes.

“I thought you were on the verge of qi deviation……”

“Wouldn’t you have to be more careful if I really were having qi deviation?”

“You’re fine if you’re only on the verge. Ever heard of fighting fire with fire?”

I wasn’t sure that was the right expression for this situation, but the real issue was something else.

The culprit who’d made Jeok Cheongang suspect I was on the verge of qi deviation was still swaying before my eyes.

As if trying to hypnotize me.

“By the way…… where did you get that?”

Even as I asked, I felt uneasy.

If that unexpected object hanging around Jeok Cheongang’s neck really was the one I knew, how was I supposed to make sense of it?

The answer came right back, and it was enough to make my heart feel even heavier.

“Where did I get it? How would this old man know? You’re the owner. You’d know best.”

“……!”

“What? Is something wrong?”

“N-no.”

I managed to answer, then immediately muttered to myself.

There was one surefire way to find out.

*Open Inventory. Summon.*

It was simple.

I just had to picture it in my mind and issue a command with enough intent behind it.

But this sequence of actions, one I’d repeated hundreds—no, thousands—of times, suddenly felt unfamiliar.

So did the small System window that appeared in the air.

*Beep.*

> **System**
>
> This item does not exist in your **Inventory**.

Shit.

I took a small breath and forced myself to speak calmly.

“I was mistaken. It is mine.”

“That’s what I thought. I’ve seen it a few times before, too. Still, it must have some story behind it. Or it’s important to you.”

“Excuse me?”

“I found it ten days ago, right where you’d collapsed unconscious. It was lying in a pool of blood, but luckily I recognized it. You’d carried it through such a fierce battle, so I figured I ought to keep it safe.”

“……I see.”

“Come to think of it, I’ve forgotten what it’s called. Chairman? Was it a makeup watch?”

I licked my lips, which had gone dry.

“A pocket watch.”

“Ah, right. One of those foreign devices used by the barbarians across the sea. It has such an odd shape that it stuck in my mind.”

The thing about barbarians across the sea was just an excuse. There were too many people around to tell him the truth.

As far as I could tell, this world wasn’t even made up of five oceans and six continents. How would I know if there were blond, tanned punks or tyrannosaurs living across the sea?

But there was at least one thing I knew for certain.

That pocket watch had been buried deep in my Inventory for more than two months.

*Had I taken it out?*

A simple mistake in my memory?

Absolutely not.

I’d half forgotten the thing even existed. How could I have taken it out?

*This makes no sense.*

Right. This really made no sense.

The Inventory was an infinite storehouse that opened and closed only at my will.

But that thing—more precisely, the item called **[Pocket Watch of Unknown Make]**—had somehow broken the System’s rules.

Without me even realizing it.

“I meant to give it back these past few days, but kept forgetting, so I started wearing it around my neck. Good timing, eh?”

I took the pocket watch Jeok Cheongang handed me as if I were under a spell.

And—

“……!”

It suddenly came back to me.

*“All right. It’s time to go. To the place where you belong.”*

That fleeting voice, gentle against my ear, as my vision was swept away and pulled toward somewhere unknown.

*“Take it. It’s the last gift this old man can give you.”*

The hard feel of something I’d instinctively clutched beyond the haze of my fading consciousness, and the glimmer it held inside.

*The Helper.*

There was no doubt. At last, I remembered clearly.

The endless, empty space.

What he’d given me in that place, in our final moments together.

Squeeze.

It happened as I gripped the pocket watch without thinking.

*Ding!*

> **System**
>
> Item information has been updated!
>
> Would you like to view the new information for **[Pocket Watch of Unknown Make]**?
>
> **Y / N**

* * *

After checking the System window, I was weighed down by a heavy silence.

I kept my mouth shut on the way back to our quarters with Jeok Cheongang, as we climbed the stairs, and even when he prodded me, unable to stand the silence.

No—I hadn’t heard him.

The thread of thought holding my senses captive was that long and that tough.

*What is it?*

Memories that remain vivid in the mind long after the years have passed fall into two broad categories.

The unbelievably good kind, or the goddamn awful kind.

And in that regard, the pocket watch in my hand clearly belonged in the latter.

Even after more than two months, I remembered it so clearly that I could recall every last word.

**Item Window**

**[Pocket Watch of Unknown Make]**

**Type:** Common Item  
**Grade:** None  
**Restrictions:** None  
**Description:** A pocket watch made by someone unknown. Extremely sturdy. At a glance, it looks like an old, broken watch. Even on closer inspection, it looks like a broken watch.

The memory came back as fresh as yesterday.

The moment I checked the item information, the anger that had surged from deep in my chest like lava.

*How could I forget? It was such a goddamn awful memory.*

Of course it was. Back then, I’d been bursting with anticipation.

This wasn’t some ordinary run-of-the-mill Quest. The item had been given to me as a Reward for a **[System Update]**.

*I’d gone through all that shit because of an update I didn’t even know existed.*

Right after defeating the Doppelganger in the modern world, I’d been sent straight to Murim. It hadn’t been my choice.

The System Update had started without warning and forced me to Log In. The System stayed dead throughout the update, only returning to normal after I’d wrapped up the events in the imperial palace.

And after going through all that bullshit, how do you think I felt when I got this piece of trash as my Reward?

*Considering how I felt back then, it’s a miracle I didn’t throw it away.*

More accurately, it wasn’t that I didn’t throw it away. I couldn’t.

It was an update reward, after all. I’d held onto a sliver of hope that it might have some hidden use.

But it didn’t take long for that last flicker of hope to burn out completely.

The pocket watch was…… actual garbage.

It was filthy and worn no matter how closely I looked, and clearly broken no matter how long I stared.

I examined it like a judge on an antiques appraisal show scrutinizing a national treasure, but the only unusual thing I found was one faint line inscribed on the back.

*A broken clock is right twice a day.*

Twice a day, my ass.

After a week of watching the second hand stay exactly where it was, I shoved this sturdy piece of trash deep into my Inventory.

I was sure that whoever made it would get the shit beaten out of him if he ever showed his face.

*But…… why is it showing up here again? And like this, out of nowhere?*

I narrowed my eyes at the holographic window floating in the air.

**Item Window**

**[Pocket Watch of Unknown Make]**

**Type:** Special Item  
**Grade:** None  
**Restrictions:** None  
**Description:** A pocket watch made by someone unknown. Extremely sturdy. At a glance, it looks like an old, broken watch. On closer inspection, it seems to hold a secret I have yet to uncover.

The newly updated item information.

Actually, calling this an update seemed a little generous.

Only a few characters had been added or changed.

*The item type, and the last line of the description.*

The change was tiny.

It had gone from a Common Item to a Special Item, and the sentence “Even on closer inspection, it looks like a broken watch” had been replaced with new information. That was all.

But the meaning behind that change didn’t feel small at all.

Especially when I thought about how I’d gotten this useless piece of junk back.

*The Helper. The endless, infinite space. And finally, the pocket watch.*

I kept repeating those three keywords in my head, which was already crowded with thoughts, when—

Tap, scuff, tap.

A set of irregular footsteps drew closer through the slightly open door, and an uninvited guest arrived.

“Buuuurp. Whew. I’m drunk.”

A near-mummy—no, Hyuk Mujin—appeared with a burp like a lion’s roar and looked at Jeok Cheongang and me through half-lidded eyes.

“Well, well, you’re here, are ya? Hehe.”

Before I could say anything, Jeok Cheongang spoke in a dignified tone.

“If you’re drunk, go sleep it off. Unless you want a sound beating.”

Hyuk Mujin answered.

“Nah.”

“……”

“……”

Who knew one word could leave both me and Jeok Cheongang so dumbfounded?

But Hyuk Mujin, who’d just accomplished what no great fiend had ever managed, didn’t stop there.

“Uuugh.”

“Hey, don’t you dare……”

“Bwaaaaargh!”

“……I said don’t.”

What the hell was wrong with this guy?

Jeok Cheongang recoiled in alarm before the torrent of vomit, pouring down like Niagara Falls. I sighed and patted Mujin on the back.

Then, after he’d finished making a whole scene, he lifted his head.

“Huh? Isn’t this that watch? Are ya finally givin’ it to me?”

He spotted the pocket watch around my neck and came out with something I never would’ve expected.

“But did ya finally get it up and running?”

“You crazy bastard, why are you talking about getting it up all of a sudden—wait, what did you say?”

“You fixed it, didn’t ya?”

With his tongue thoroughly twisted, Hyuk Mujin mumbled and grinned as he grabbed the pocket watch swaying before him.

“’Course ya did. It’s showing a different time than the last time I saw it.”

“……!”

What did he just say?
## Chapter artifact 1144

# Chapter 1144

Was this what it felt like to have ice water dumped over your head?

Still frozen in place by the words I hadn’t expected to hear, I grabbed Hyuk Mujin by the shoulder. He was grinning like an idiot.

“What the hell are you talking about?”

Whoosh.

As I spoke in a low voice, I sent a thread of internal energy into him. Focus returned to the eyes of the man who’d been swimming in drink.

“Y-yes?”

“Say that again. What you just said.”

The alcohol had already worn off.

Facing my completely serious expression, Hyuk Mujin swallowed hard.

“What I just said? Which part… Ah, the time?”

“Yeah. This thing. Do you remember it?”

I took the pocket watch from around my neck and shoved it close to him. Hyuk Mujin nodded hastily.

“Of course. That was probably when we were staying at the Imperial Palace…? I begged you for it like crazy because I wanted it so badly, but you said you’d think about it, Captain. Then you never brought it out again.”

Of course he remembered.

I’d vaguely claimed it was a valuable item brought in from the Western Regions, and from then on, he’d pestered me for it practically every day.

“I’d pretty much given up when I heard you were giving it to Young Lady Ju. I didn’t know you still had it.”

That was when it happened.

As Hyuk Mujin turned the pocket watch this way and that, looking at it as if it were still a marvel, the words I’d been waiting for finally came out of his mouth.

“Still, no matter how valuable it is, what woman would be happy to receive a broken watch as a gift? You should fix it before you give it to her.”

“……Fix it?”

“Huh? Am I wrong? The last time I saw it, this long hand here was—yeah, right around there.”

Following the fingertip pointing at the pocket watch’s hour hand, I felt my face stiffen.

“Captain? Did I do something wrong?”

“No. More importantly…”

“I’m sure. What reason would I have to lie about something like this?”

“Right. Of course.”

That was the end of the conversation.

I muttered to myself and waved him away without another word. Hyuk Mujin understood the gesture and withdrew. Watching him go, I fell into thought.

*Yeah. He’s right.*

My gaze moved to the pocket watch resting in my palm.

Why hadn’t I noticed right away?

It had no minute hand, which any ordinary watch should have, and not even any numbers. Its sole hand had moved one position from where it had originally been.

And not forward. Backward.

*Unless it was designed from the start to move counterclockwise…*

Had it already gone around once—or several times—and stopped where it was now?

If so, what did that mean?

*That old man definitely knew something.*

The newly updated item information said the pocket watch held a secret, and The Helper had clearly known what that secret was.

That must have been why he gave it to me as a gift.

But…

How had he known something even I didn’t?

And how had the pocket watch, buried deep in my Inventory for the past few months, found its way back to me like this?

“……No way.”

My heart suddenly began to pound, and my lips went dry.

At the sound of my own voice slipping out between them, Jeok Cheongang said something in response. But my mind, bleached white, was too busy untangling its knotted skein of thoughts to hear him.

And finally—

“……!”

An unbelievable theory struck my mind like lightning.

As swift and decisive as the king’s blade that had cut through the Gordian knot no one else could untie.

That endless, infinite space.

The pocket watch that had begun to move without anyone knowing.

And finally, The Helper—the old man whose identity I couldn’t discern, but whose martial prowess was greater than anyone I’d ever met.

Though our meeting in my consciousness had been brief, I’d felt it clearly.

His presence, like a colossal wall.

An overwhelming pressure more terrifying than anything I’d ever felt from the greatest masters under Heaven, known as the Three Saints.

And there was only one person who could stand above the Three Saints.

*The Martial God.*

I swallowed.

Feeling a shiver run from the crown of my head to the tips of my toes, I recalled the theory I’d pieced together about him less than half a shichen ago.

*The System may have recognized Cheon Taemin’s unconscious state as a form of death.*

If that theory was really true—

And if his consciousness had been preserved in the System for some reason—

Then I’d already met Cheon Taemin. The Martial God.

In the infinite space where he’d been staying.

No—in the Inventory.

*“Good call.”*

The voice I’d heard in the past echoed in my ears like a hallucination.

Along with the meaningless noise that had rung out at the end of the nightmare I’d had three days ago.

*Tick.*

A chill unlike anything I’d ever felt rose up my spine. I stared at the pocket watch, my gaze distant.

At the same time, I thought about the meaning of the dream I’d had that day.

Why The Helper, the old man I suspected was Cheon Taemin, had reminded me of the pocket watch I’d gradually forgotten about.

And the one way to answer all these questions.

“I have something to tell you.”

After a long silence, my one sentence made Jeok Cheongang’s gaze sink deep.

* * *

The grand banquet, where everyone had gotten thoroughly drunk together, lasted only one night. But no one staying in Xining regretted its end.

Blood was thicker than water—and more intoxicating than wine.

That was why no few jars of wine could help them forget the blood they’d already shed.

All the more so when they thought of the blood they still had to shed.

“All preparations are complete.”

High atop the city wall, Sword Saint Mae Jonghak spoke his first words in a calm voice.

The air was still.

Beyond the wall, in the fields where his gaze fell, an army too vast to count had gathered beneath scores, hundreds of banners.

Their eyes, soaked in drink all night, now burned like torches.

“Since the dark clouds of Dark Heaven first loomed over us, the realm has been plunged into turmoil and screams, and we’ve had to shed so much blood.”

It was true.

Dark Heaven had risen only a little over two years ago.

Yet the blood shed in that short time was comparable to the blood spilled over the more than ten years of the Great Faction War.

“We’ve seen with our own eyes and heard with our own ears the results of their vile schemes.”

The conflict in Shanxi had been only the beginning.

Shaolin Temple in Henan had burned along with the life of the eminent monk known as the Dharma King.

Soon after, all of Sichuan was drenched in blood.

Then Hubei, followed by distant Nanman.

The Imperial Capital and Hebei. Even Gansu had been invaded.

“And at last, the will of the entire realm has gathered here in Qinghai.”

His voice, carried endlessly outward by his powerful internal energy, brought tears to the eyes of everyone listening.

They knew.

They knew how much blood had been shed to bring them here.

And they knew how precious and meaningful the blood they would shed from now on would be.

“We will hesitate no longer. We will not retreat.”

Fervor spread through the crowd.

This was their will—all the realm’s will.

“We will fight not for victory, but to protect what we hold dear.”

Their families, who’d been with them from birth, had died.

Friends who’d supported them in times of hardship had died.

Neighbors who’d traded smiles whenever they met had died.

And even if someone had been fortunate enough to escape all of it, their turn would come soon.

Unless they fought back.

Unless they defeated the Lord of Heaven, the dark clouds looming as though they would swallow the realm whole.

This was a war to protect what they held dear.

A holy war to exterminate fiends without equal in all history—and, at the same time, a mandate from Heaven.

“So I ask you…”

With a ringing sound, the snow-white blade emerged from its scabbard.

A purple glow surrounded Mae Jonghak as a vast wave of aura burst from him.

No—at his side, everyone standing tall upon the wall unleashed the countless feelings and surging auras they’d held back.

Along with the Alliance Leader’s Azure Dragon’s Roar, which swept across the dry skies of Qinghai.

“Who among you will retreat in the face of injustice?!”

At that instant—

Clang, clang, clang, clang!

The darkened fields flashed like the sun.

Countless spears and swords thrust high into the sky, and the flags, still hanging limp, began to flap beneath the muffled cries and surging auras of the army.

That was right.

At last, the wind was blowing.

A wind that had begun in the Nine Provinces and Eight Directions, carrying the cold of steel and the stench of bloodshed and vengeance.

It rushed toward the cursed forbidden land beyond the distant desert.

Boom, boom, boom!

Accompanied by the deepest, most powerful beat of war drums yet, an army of more than two hundred thousand advanced, blanketing the vast wilderness.

Murim.

No—the sight of the greatest coalition army in the history of the continent marching as one was so magnificent that everyone on the wall shuddered.

But even then, one man’s eyes trembled.

*Damn it.*

Jin Taekyung felt his heart sink and thought.

This should be the end. So why did it feel like a beginning?

The united blade of the realm, forged through countless hardships, was aimed at the Lord of Heaven. So why did it feel as if he were walking along the edge of a cliff?

*Now’s my only chance.*

The unease pressing down on one corner of his mind like a massive boulder, the questions he couldn’t resolve—

There was only one way to deal with them and move forward.

*Master.*

At Jin Taekyung’s quiet Sound Transmission, Jeok Cheongang gave a small nod.

*So you’ve decided to do it after all.*

That was all he said, and it was enough.

Before dawn, Master and Disciple had shared a long, deep conversation. They had no secrets from each other.

“Go on.”

As his Disciple climbed into the carriage they’d prepared in advance, Jeok Cheongang smiled faintly and added, “This old man will be right here, waiting with everyone.”

With a smile just like his Master’s, the Disciple replied, “I’ll be back.”

And soon, the Disciple fell asleep.

Into a sleep so deep and vivid that he wouldn’t know it even if someone shook him awake.

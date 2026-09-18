# Checkpoint Review — 405–409

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

# Chapters 405–409

## Plot

The allied forces launch mobile warfare across five fronts and advance rapidly toward Suining City, where the Arch Lich is believed to be waiting. Jin Taekyung uses Hero’s Soul and the Flame-Extinguishing Divine Fist to help rout the monsters, but the Arch Lich’s absence and the sudden decline in the enemy army make the victories suspicious.

An intelligence team confirms that Suining City contains a preserved monster army numbering at least thirty thousand, possibly twice that. The coalition halts its advance and accepts Jin’s plan to form a suicide squad of elite Hunters to break through the army and kill the Arch Lich, whose destruction should collapse the undead forces. Jin, Lee Jungryong, and the coerced Wu Heixing join the assault, while Magic Johnson, Prince Felix, and Faye Chen remain behind.

The Skeleton Warlord attempts to use Jin’s promise of granting any request to obtain freedom. Jin throws its skull into the Hunter camp, but the Warlord soon returns and begs to withdraw the request. Jin refuses and recalls it. Before the final assault, Team Leader Choi warns Jin about the danger posed by Lee and Wu. Jin reassures him in his usual joking manner, then helps steady the Western Front’s soldiers with a speech urging them not to give up.

As the allied fronts surround fog-shrouded Suining City, corpses rise and Skeletons emerge from the mist. The battle for the city begins.

## Continuity

- The five allied fronts have advanced to roughly two hundred kilometers from Suining City and are now surrounding it.
- Suining City contains the Arch Lich and a preserved monster army of at least thirty thousand; most surviving monsters are expected to be mid- or low-level.
- The coalition’s suicide squad is intended to penetrate the monster army and kill the Arch Lich. The undead forces are expected to collapse if it dies.
- Jin Taekyung, Lee Jungryong, and Wu Heixing are part of the assault squad. Magic Johnson, Prince Felix, and Faye Chen remain in rear defense.
- Lee Jungryong privately assures Wu Heixing that the operation will not expose him to serious danger, despite Wu’s reluctance and distrust.
- Hero’s Soul was passed from Jin to Shao Shen, who judged Team Leader Choi more suitable and pressed the sword on him. Its final wielder in this operation remains relevant.
- Jin has three jiazi of internal energy and can recover from ordinary fatigue through qi circulation.
- Team Leader Choi is a descendant of Cheon Taemin with exceptional martial talent and substantial internal energy. He trusts Jin but distrusts Lee and Wu.
- Jin’s internal-energy-enhanced speech has raised the Western Front’s morale immediately before the assault.
- The Skeleton Warlord remains Jin’s captive, reluctant companion. Its attempted escape through a freedom wish failed, and its glossy black skull now has a small crack from Jin flicking it.
- The Arch Lich previously gathered immense mana in a ruined space and called for an unidentified adversary; its purpose and preparations remain unresolved.
- The unidentified lord connected to Lei Fei, the Second Fiend assigned to Qingcheng, and the Skeleton Warlord’s original identity remain unresolved.

## Translation Decisions

- Use **Jin Taekyung**, **Team Leader Choi**, **Lee Jungryong**, **Wu Heixing**, **Hero’s Soul**, and **Hero’s Power**.
- Render **기동전** as **mobile warfare** and **결사대** as **suicide squad**.
- Render **쑤이닝시** as **Suining City**.
- Render **스켈레톤 워로드** as **Skeleton Warlord** and **아크 리치** as **Arch Lich**.
- Render **머리를 치다** as **take out the head** in the strategic context of killing the Arch Lich.

## Durable state

{
  "active_continuity": [
    "The Western Front's thousands of Hunters and soldiers are advancing on fog-shrouded Suining City while the other allied fronts surround it.",
    "The battle for Suining City has begun as corpses rise, Skeletons emerge, and monsters move within the encroaching fog.",
    "Jin Taekyung expects defeating the Arch Lich to be the key to stopping the undead threat.",
    "Team Leader Choi deeply trusts Jin Taekyung but fears the operation because Lee Jungryong and Wu Heixing are involved as dangerous, untrustworthy comrades.",
    "Team Leader Choi is a descendant of Cheon Taemin with exceptional martial talent and unusually substantial internal energy.",
    "Jin Taekyung's speech, strengthened by internal energy, has eased the Western Front's tension and encouraged its soldiers before battle.",
    "The Skeleton Warlord remains Jin Taekyung's captive and reluctant companion despite fearing the operation.",
    "The Skeleton Warlord's glossy black skull has acquired a small crack after Jin flicked it."
  ],
  "continuity_sources": [
    409
  ],
  "open_questions": [
    "Who is Lei Fei's unidentified lord, what is the lord's origin, and how does the lord relate to the Arch Lich's objective?",
    "What happened to the Second Fiend assigned to the Qingcheng attack?",
    "Why has the Arch Lich withheld itself from the war, and what is it preparing now?",
    "What kind of being was the Skeleton Warlord before it became an undead commander?",
    "What specific situation will allow Jin to draw out Hero's Power more strongly?"
  ],
  "safe_through": 409,
  "temporary_decisions": [
    "Render 영웅의 혼 as Hero's Soul and 영웅의 힘 as Hero's Power.",
    "Render 기동전 as mobile warfare.",
    "Render 쑤이닝시 as Suining City.",
    "Render 결사대 as suicide squad.",
    "Render 스켈레톤 워로드 as Skeleton Warlord, 아크 리치 as Arch Lich, and 머리를 치다 as take out the head in the context of killing the Arch Lich."
  ],
  "version": 1
}

## Reading copies

## Chapter artifact 405

# Chapter 405

“Then we will begin the operation at 06:30 tomorrow. The fronts concerned are to carry out every order they receive without fail.”

Pop.

The meeting ended with Wei Fenghu, the Minister of National Defense, having the final word.

Lee Jungryong, the Vice Guild Master of Ares Guild, leaned back in his chair as he stared at the five monitors whose screens had gone dark.

*The pace is fast. Much faster than I expected.*

It was not a war that would end easily, nor was it a war that should end easily.

China was both a Hunter powerhouse with an enormous number of Hunters and a closed-off country. It was also one of the few countries where Ares Guild, which had extended its reach across the world through its mercenary business, had failed to establish a proper foothold.

That was why Lee Jungryong did not want China to remain stable. The greater the damage China suffered, the wider the opening would become for him to exploit.

More than a million casualties? Hundreds of trillions of won in property damage?

What did any of that matter? This monster wave might have been a disaster for some people, but for Lee Jungryong, it was an opportunity.

But…

*This time too, Jin Taekyung is the problem.*

Lee Jungryong raised a finger and slowly tapped it against the table.

He had always known that the world did not go according to plan, but lately, whenever Jin Taekyung obstructed him at every turn, a thought kept surfacing.

*He’s dangerous.*

The interest Lee Jungryong had felt when he first learned of Jin Taekyung’s existence had long since vanished without a trace.

If a child who had barely reached an adult’s waist suddenly grew by leaps and bounds over the course of several months and met that adult’s gaze head-on, the adult could not help but be flustered.

What if that child’s growth had not yet stopped?

*He’ll become even more dangerous.*

If the Arch Lich’s rampage had been an opportunity for Lee Jungryong, it had given Jin Taekyung wings.

The man had achieved truly incredible military feats and was receiving the attention of the entire world.

Another war had produced a new hero. Just like the heroes of the chaotic Great Cataclysm era.

*People fear the strong even as they envy them, but heroes are worshiped.*

Lee Jungryong knew that better than anyone. And if this war ended because of Jin Taekyung’s exploits—if it did—then…

Crack.

The tip of his finger, infused with aura, had already bored through the solid wood and reduced it to powder.

Lee Jungryong silently looked down at the table, its center punched clean through.

For now, it was only a small hole. But if it continued to grow, it would soon become impossible to control. He had to fill the hole before the table collapsed.

“Have the Head of Security come in.”

When Lee Jungryong’s quiet voice slipped between his lips, someone waiting outside the door left to carry out the order.

Before long, a familiar presence opened the door and entered.

“You called for me?”

Jin Taekyung was not the only one who had changed over such a short period of time.

Go Jun, Lee Jungryong’s right hand and Head of Security, had undergone many changes as well.

His dark eyes had sunk deeply, and his voice had become dry. A few people who knew the circumstances whispered that after losing to Jin Taekyung, his already rigid expression had grown even gloomier.

Lee Jungryong had a different opinion.

“You look well.”

“I’ve made a little progress.”

“Too much humility is unbecoming. You achieved a great feat on today’s battlefield as well. That is more than enough to deserve praise.”

“……Thank you.”

The sudden attack by the monster army targeting five fronts had left an enormous number of casualties, but the northern front under Lee Jungryong’s command had been an exception.

The elite members of Ares Guild had held back their strength and responded cautiously to the fighting until now. When the attack came, they slaughtered the monster army. Go Jun had also defeated two Death Knights, each one acting as a commander, by himself.

“What were our losses?”

“Eleven severely injured and forty-six lightly injured. There were no deaths. The severely injured will need a little more time to recover, but all the lightly injured have already been healed.”

The more than four thousand casualties among the Hunters and soldiers did not enter the equation.

Lee Jungryong asked the questions, and Go Jun answered them. To the two of them, only Ares Guild was on their side.

“It’s unfortunate about the commander, though. To die such an untimely death. He was quite a tough man……”

At Lee Jungryong’s trailing words, a gloomy light flickered in Go Jun’s sunken eyes.

“I’m sorry. I tried to stop them with everything I had, but there were simply too many monsters.”

“It couldn’t be helped. Did you recover the body?”

“The damage was too severe, so we had no choice but to cremate him. The staff officers who died alongside the commander were treated the same way.”

“Good work. Ah, you know that Lieutenant General Wang Ochun is the new commander, don’t you?”

“Yes. I was just on my way back from meeting him.”

Only a very small number of people, including Lee Jungryong, knew that Lieutenant General Wang Ochun and Go Jun were not meeting for the first time.

For several years, the two had occasionally shared meals at inconspicuous safe houses. Each time, the trunk of Lieutenant General Wang Ochun’s sedan grew heavier.

“What did he say?”

“He said he looked forward to working with me.”

A faint smile appeared around Lee Jungryong’s lips.

“Of course. You’re comrades who will fight together.”

By now, Wang Ochun was probably delighted by the thought that he had been entrusted with an important post. He had no idea that this entire chain of events was not mere good fortune.

Nor did he know that his tough predecessor, now reduced to a handful of ashes, had been preparing a report on Ares Guild’s lackluster performance in battle.

“Watch over him carefully. We can’t lose the commander twice, can we?”

“Understood.”

No one knew what might happen on a battlefield.

A commander who had been on bad terms with someone might be torn to pieces by monsters, while a corrupt military general who loved money might be appointed the new commander.

Lee Jungryong, whose mood had improved somewhat, opened his mouth.

“You’ll have a hard time starting tomorrow, so get plenty of rest tonight.”

“What do you mean by that……?”

“They say we’re to advance as quickly as possible and sweep away the remaining monsters.”

“Mobile warfare, then. Is that the order for every front?”

Lee Jungryong nodded.

The five fronts, including the northern front, would begin mobile warfare tomorrow morning. Within a few days, they would cut off the monster army’s retreat and build a dense encirclement around it.

“They must have lost a considerable amount of strength as well, but their numbers won’t be easy to deal with.”

“What do you think this country has the most of? Even now, hundreds of transport planes are carrying Hunters from every corner of China. Even low-ranking Hunters will be useful as arrow fodder.”

Lee Jungryong explained this in a calm voice before continuing.

“Focus on minimizing the Guild’s losses. In case……”

Lee Jungryong gazed deeply at the table.

“There may come a time when you have to fill a hole.”

“……I’ll keep that in mind.”

It was an inscrutable statement, but to Go Jun, Lee Jungryong was both a revered Master and something no different from a god.

Without voicing any questions, Go Jun silently nodded. Then he suddenly realized that he had failed to ask an important question.

“Where is our final destination?”

Instead of answering, Lee Jungryong raised a hand and pointed toward one place: the map of Sichuan Province covering the wall.

Pshk!

Wind shot from the tip of his finger and pierced one section of the map. Go Jun’s gaze landed on the place-name written beside the hole.

Suining City.

The place where everything in this disaster had begun.

The Arch Lich was there.

* * *

The following dawn, those who woke from sleep realized that they had been divided into two groups.

Those who were leaving and those who were staying.

Naturally, I belonged to the former group, while Team Leader Choi and Shao Shen belonged to the latter.

And only when the time to leave was almost upon them did the two men finally come to their senses and begin resisting the fact that they were staying behind.

“Mr. Jin. I’m perfectly fine.”

“I’m perfectly fine, hyung!”

“I can fight.”

“I’m confident I can fight harder than anyone!”

*……What is this, an echo?*

As I looked at Team Leader Choi and Shao Shen shouting with stiff expressions, I had no choice but to make them an offer.

“Hmm. Then if you can last ten minutes against me, I’ll take you with me.”

“……”

“……”

—Is that what you call an offer, you shameless, wicked human?

*What do you mean, conscience?*

If we were going to argue about it, those two were the ones without a conscience. They could barely run properly, yet they wanted me to take them to the battlefield.

It was good that they were burning with the will to fight, but going to the battlefield in their current condition was a perfect way to get themselves killed.

*And what kind of undead talks about conscience?*

*Damn it. Seriously.*

After issuing that threat in my mind, I continued speaking to the two men, who had become thoroughly dejected.

“For now, focus on recovering. If you spend the next few days getting your feel back and your stamina returns, you might be deployed to the front then. That goes for you too, Shen—not just Team Leader Choi.”

“Hmm.”

“Hmmmm.”

They still did not seem happy about it, but at least they appeared somewhat resigned.

In truth, both of them knew the condition their bodies were in. They could not keep forcing the issue forever.

“Then I’ll be going now…… Ah.”

I had forgotten one thing.

I pretended to rummage through the bag enchanted with space-expansion magic, then took out the item I had stored in my inventory and held it out.

“Here.”

Shao Shen blinked.

“……Hyung?”

“What are you waiting for? Take it. My arm’s going to fall off.”

Shao Shen reflexively accepted what I had offered and asked with a bewildered expression.

“What is this?”

“A gift. Someone I know entrusted it to me, but I think you should have it.”

“A sword this fine?”

“What? You don’t like it?”

“No, that’s not it. I’m just wondering whether I should be accepting something like this……”

Shao Shen hurriedly waved his hands, then gripped the hilt of Hero’s Soul with dazed eyes.

Its weight distribution and balance were close to perfect. An edge impossible to conceal flowed from the transparent blade.

After swallowing hard, he asked,

“Can I really accept this?”

“I’m not giving it to you for no reason. I’m giving it to you because you qualify.”

“Qualify……?”

“That’s right. You qualify.”

The courage he had shown in the last battle. His sacrifice for someone else.

That was enough.

If I kept it, it would only rot away in my inventory. I had been using a spear for a long time already.

I judged that Shao Shen, who was both Chinese and a member of the Public Security Armed Forces Department, was more suited to wield it than I was.

*The sword must have recognized him too, considering that nothing happened even after he gripped the hilt.*

The Skeleton Warlord grumbled quietly.

—This commander can use a sword well too…… And this commander likes swords……

*Huh? What was that?*

It was hard to hear the words of a loser who had secretly grabbed Hero’s Soul from my inventory at dawn and screamed.

—……Hmph, forget it. A cheap sword like that is unworthy of this commander!

“……”

*What is he talking about? Someone who wants it more than you is sitting quietly right here.*

Since I was thinking about it anyway, I discreetly glanced at Team Leader Choi.

In truth, I had agonized over it until the very end—whether to give Hero’s Soul to Shao Shen or Team Leader Choi.

Team Leader Choi was human too, after all. He might have felt hurt.

But apparently, all that worry had been for nothing.

“Congratulations, Regimental Commander Shen. You’ve obtained a truly fine sword.”

At Team Leader Choi’s sincere congratulations, Shao Shen finally came to his senses and looked back and forth between Hero’s Soul and him.

Conflict flickered in his eyes. But soon, a clear smile spread across his lips.

“I don’t think I’m the one this sword belongs to.”

“……?”

“Mr. Choi. Would you accept this sword in my place?”

This was an unexpected turn of events. Still……

*That’s nice to see.*

Team Leader Choi was flustered and politely refused, but Shao Shen had already made up his mind, and his resolve was stronger.

As I watched the two of them pass the sword back and forth, I quietly slipped out of the ward and started walking.

Before I closed the door, Team Leader Choi’s voice reached my ears.

“Of all the swords I’ve seen, this is the one I like best.”

Right. That was all that mattered.

I strode energetically among the troops who had already assembled.

A human wall parted before me amid looks of awe.
## Chapter artifact 406

# Chapter 406

The era of upheaval that began with the descent of Asmodeus, the Demon King, had been grim and chaotic. But after overcoming the crisis, humanity quickly repaired the damage and built a civilization even more advanced than before.

Still, for some people, there were things more important than elevators powered by mana stones or healing potions.

“The internet got faster.”

The man who muttered those words in a reverent voice adjusted his glasses.

It was 11:30 a.m. Behind him, the ramen he had just added to the pot was bubbling away, while cold rice and sour kimchi had been laid out on the table.

Everything was ready. In exactly three minutes, he would add one—no, two—A-grade jumbo eggs he had agonized over before buying during a supermarket sale. After waiting two more minutes, the perfect lunch would be complete.

And until then, the boredom would be solved by the marvelous modern civilization known as the smartphone.

“Let’s see what we have here… Today’s news…”

Humming, the man skimmed through his smartphone screen.

The main page of *Hunter University*, a large online forum he visited often, displayed new best posts ranked by popularity.

1. **[Victory report after victory report—is the monster army already as good as shattered? The UN Security Council issues an official statement: “Humanity is strong. But the war is not over yet. We must not let our guard down until the very end.”]**

2. **[The Miracle of Sichuan Province. Jin Taekyung stood at the center of it all.]**

3. **[National prestige rises by the day as a new hero is born. K-pop and kimchi sales skyrocket.]**

4. **[Scheduled Korea–US summit to proceed… President Doramp makes a startling statement at an official event: “Is this Jin Taekyung’s country? He’s my idol.”]**

5. **[Ares Guild continues its string of victories. Truly living up to its reputation.]**

6. **[Chinese Chairman Xiao Yang: “Every one of them is a hero.”]**

7. **[Maesaeng-i.com Translation: Overseas netizens react to the current situation. “Who the hell is this ‘Lady of the House’ Koreans keep killing every chance they get?”]**

8. **[Japanese Prime Minister Maigumi Shinjiro: “Monster waves must be handled in a Fun, Cool, and Sexy manner.” When a reporter asked what that meant, he grinned and replied, “Explaining it wouldn’t be sexy.”]**

9. **[Russian President Furin: “To me, Shinjiro is like quantum mechanics. No matter how much I look at him, I can’t understand him.”]**

10. **[Web-novel author becomes a prophet: exclusive interview with Zerobic. “How do I feel right now? I’m still stunned. Since we’re on the subject, I’ll be taking a break today.” During the interview, his enraged editor burst in and injured him badly enough to require twelve weeks of treatment, resulting in an unexpected hiatus. Zerobic smiled and said he was happy to be able to rest despite bleeding, while editor Mr. Lee shed tears and said, “He isn’t human.”]**

.

.

.

“Wow. This place is absolutely insane. Completely insane.”

A smile spread across the muttering man’s lips. No matter how far he scrolled, everything was about Jin Taekyung.

Some strange articles seemed to be mixed in here and there, but simply looking at them made a deep sense of pride well up inside his chest.

The comment section was already on the verge of exploding.

> The activity here is insane lately. I’ve been on Hunter University since elementary school, but I’ve never seen it this heated before;;

> └ The truly insane one is Jin Taekyung. He carved through a monster army ten thousand strong all by himself. It still makes no sense when I think about it. How the hell did he do that?

> └ He’s amazing, but let’s get the facts straight. It wasn’t ten thousand, it was a few thousand at most.

> └ LMAOOOO isn’t that still completely insane?

> └ For realㅋㅋㅋㅋ You’re the kind of bastard who’d get a goblin’s poison stinger in the ass and yell, “Ow, please let go gently!” Aren’t you the same guy who used an aura blade with your keyboard last time?

> But at this point, Jin Taekyung doesn’t seem like an ordinary S-rank Hunter. Are all the other S-rank Hunters like that too?

> └ Even during the Great Cataclysm, feats on this level were rare. Cheon Taemin doesn’t count because he was just on another level entirely… But if you look at the records from the Great Cataclysm, Lee Jungryong probably accomplished something similar too.

> └ Hmm. So he still isn’t at Lee Jungryong’s level? Disappointing.

> └ ?? Do you think Lee Jungryong is some old man at a spring on a hill behind the neighborhood? He may be overshadowed by Cheon Taemin, but based on his achievements, martial power, and influence, he’s one of the top-class figures in the entire world.

> └ 222. You only have to look at what happened a week ago. He wiped out the monster army with the fewest casualties across all five fronts. Jin Taekyung is incredible, but Lee Jungryong and Ares Guild are fucking amazing too. The northern front is actually advancing a little faster right now.

> └ Comments like this make me nervous for no reason. I’m worried that a bunch of idiots will show up again and start going wild with the versus arguments.

> └ They’ve been IP-banned to hell, so it should be fine. But at this point, isn’t the whole incident basically over? They’re crushing the monsters through mobile warfare right now.

> └ Undefeated for an entire week ㄷㄷㄷ;

> └ The Arch Lich must have been caught off guard. It went all-out with a surprise attack a week ago and got completely wrecked. The Death Knight Lord is dead, and the ones who survived and ran away are being hunted down now. No chance for them.

> At this point, shouldn’t the Arch Lich be making a move? It’s so quiet that it feels strange.

> └ I had the same thought, so I sent it a KakaoTalk message yesterday as a friendly check-in.

> └ ? To whom?

> └ The Arch Lich. It said it was busy with its promotion match. Apparently, it was excited because winning this game would get it to Gold.

> └ The guy above is fucking insane.

> └ Zerobic is even more insane. Why the hell is that author suddenly taking a break? You have to row when the tide comes in, you idiot.

> └ Stop talking bullshit. The important thing is that if things continue like this, we can suppress this monster wave without suffering any more major losses. Let’s pray that the situation ends soon, then observe a moment of silence for the victims who were sacrificed.

> └ Hmm… I don’t like China, but I agree with this one. Idiots and normal people coexist in every country. Good luck to all the Hunters and soldiers.

> └ Fighting.

The netizens were generally in a cheerful mood.

The monster wave, which had initially been viewed with deadly seriousness, had now become material for nationalistic pride. Even in the comments mourning the dead and cheering on those fighting, there was hope instead of fear.

*Then again, we have been hearing a lot of good news lately.*

The man nodded. It was only natural. According to the battlefield reports from the UN Security Council, there was no doubt that the tide had already turned decisively.

A week ago, the surprise attack launched simultaneously against all five fronts had caused enormous damage. But reinforcements far exceeding the number of casualties had been dispatched, and victory after victory had followed.

*At this rate, it might be over in a few days.*

Their momentum was unstoppable, like splitting bamboo. The western front under Jin Taekyung and the northern front led by Lee Jungryong stood out the most.

*The little punk. I was so worried about him at first, but he’s doing even better than I expected.*

After hesitating for a moment, the man logged into the site and left a comment.

> **Jin Taekyung’s Roommate:** Is that pathetic Jin Taekyung really him? The real Jin Taekyung is a legend. I used to eat ramen with him all the time back in the day, and now he’s become an S-rank Hunter, a king-like figure, and the world’s strongest legendary hero. When I look at him, I’m genuinely moved…

The moment he posted the comment, replies began springing up one after another.

The man gazed at his phone with a pleased expression.

Then Seong Jinho suddenly realized he had forgotten something important.

“No! My ramen!”

* * *

“Man, I could really go for some ramen.”

At my mutter, Team Leader Choi, who was standing beside me, asked a question. After finishing his recovery, he had flown to the front on a jet the previous night.

“Out of nowhere?”

“Yeah. Weird, isn’t it?”

“Given the situation, it makes you seem even more impressive, Mr. Jin.”

Swish!

Hero’s Soul, swung like a streak of light, sliced through both the lizard man’s weapon and its body.

Green blood poured out, accompanied by a stench that stabbed straight into my nose. Feeling my appetite vanish completely, I launched myself forward.

Fwoooosh! Boom!

“Flame-Extinguishing Divine Fist.”

Horrific heat coiled around dozens of lizard men and erupted into flames. The monsters hesitating at the sight were already no different from a defeated army.

Shao Shen read the flow of battle and charged to the front, shouting.

“Charge! Charge!”

“Waaaaaah!”

“Blade of the wind, descend upon this place! Wind Cutter!”

Shwish-shwish-shwish-shwish!

Clang! Slash!

—Kueeeek!

—Kiruk, krk!

Overwhelmed by the human offensive pouring down like a wave, the monsters were helplessly driven back.

The numbers were roughly even, but it was a battle the monsters could not possibly win in terms of morale or the quality of their forces.

Once the front line collapsed like a sandcastle, several terrified monsters turned their backs and began to flee.

*And collapse happens in an instant.*

Fear was contagious.

When one fled, ten followed. After that, an uncontrollable rout began.

Sure enough, my prediction proved accurate, and before long, cries of certain victory rang out.

“Pursue them! Don’t let a single one survive!”

“Get the speed buffs up!”

“Ranged units! Ready—fire!”

Shwish-shwish! Boom!

The Hunters, their momentum at its peak, began slaughtering the monsters fleeing without even maintaining formation.

It did not take long for the six-lane asphalt road, which would have been packed with cars only a month ago, to become buried beneath monster corpses.

“We won again.”

After the battle, I was checking my equipment when Team Leader Choi approached me. I shrugged.

“For someone delivering good news, you don’t look very happy.”

“That’s strange. I was just thinking the same thing while looking at you, Mr. Jin.”

“……Hmm.”

Apparently, we had been thinking along similar lines.

As he said, I was not happy at all, despite our victory.

I had first begun feeling this same sense of incongruity on the second day after we launched our mobile warfare as part of the full-scale counterattack.

“What do you think, Team Leader Choi?”

“What exactly are you asking about? The fact that the number and quality of the monsters have declined so sharply? Or the dozens of victories you’ve achieved over the past week?”

“Both.”

“You’re probably thinking exactly what I am. The current state of the war is certainly encouraging, but… something feels wrong.”

Team Leader Choi looked toward the people celebrating.

Smiles spread across exhausted faces. They were filled with hope—the hope that they would soon end the war and return to the arms of their loved ones.

“It’s not as if I don’t understand. There were so many high-level monsters during the early stages of the war. If the elite forces suffered heavy losses, a situation like this could happen. But…”

“The Arch Lich. That bastard wouldn’t go down this easily. Would it, Team Leader Choi?”

Team Leader Choi gave a small nod before asking,

“Do the higher-ups share our thoughts?”

“Probably. I don’t know about the other S-rank Hunters, but Minister of National Defense Wei Fenghu understood the situation perfectly.”

“That’s a relief, but…”

Team Leader Choi let his voice trail off. He had probably thought of the same thing I had this time as well.

We were practically at our destination, Suining City.

The Arch Lich had not shown itself even once throughout the war. What on earth was it doing right now?

—Hmm. At this point, it should be time to grease its bones. Becoming a magnificent undead requires proper maintenance, you know.

“……”

*Shut up.*

* * *

Swoosh.

A vast space.

The darkness swirling within it was sucked toward somewhere.

The pitch-black darkness vanished, and the light of the setting sun, filtering through shattered windows, touched a single being.

—Come, adversary.

His voice was as cold as the winter wind.

Having gathered its mana, the Arch Lich’s eyes gleamed.
## Chapter artifact 407

# Chapter 407

Daniel Inoue was Japanese American.

A former Navy SEAL, he had awakened as an A-rank Hunter at the age of thirty. After leaving the military, he joined a private military company, where he put his abilities to excellent use.

Mercenary work suited Inoue reasonably well. He had to spend half of every year in conflict zones across the Middle East and Africa, but in exchange, he received enormous pay and long stretches of time off.

His decision to participate in the monster wave that had erupted in China had been made for much the same reason.

“Hey, ninja. What are you thinking about?”

At his comrade’s sudden question, Inoue narrowed his eyes.

“Shut up, Sam. Aren’t you sick of that damn ninja crap yet?”

“What’s the big deal? At this point, you should be used to it.”

“I’m sick of it because of that. Try being called a ninja or samurai since you were seven. It’ll drive you insane.”

“Why? Sounds good to me.”

“You damn Yankee bastard.”

“I’ll take that as a compliment. I’m a Yankees fan.”

The small white man snickered at Inoue’s grumbling.

“Just accept it already. At this point, it’s fate. Your abilities are completely ninja-like, too.”

“…Damn it.”

Inoue muttered a quiet curse.

Just as his comrade had said, the ability he had received upon awakening was optimized for stealth.

Thanks to it, he had become a specialist in espionage and targeted assassinations. But it had also cemented his image as a ninja.

“I heard your girlfriend’s pregnant. How about naming the baby Naruto?”

Inoue raised his middle finger at his relentlessly annoying comrade.

“If you name your son Sasuke, I’ll think about it.”

“Oh, not bad.”

Quiet snickers escaped from the people around them.

The stiff, rigid atmosphere loosened, and Inoue and his comrade exchanged faint smiles.

The two had been close friends and partners for years. Their exchange had been little more than a skit meant to ease the tension before the mission began.

*When the tension gets too high, people tend to make one mistake after another.*

The same was true of combat, but even more so of an espionage operation like this one.

An unknown land where neither communications nor magic could be used. And their opponent was not some stupid, brutal rebel leader, but the Arch Lich who had unleashed an unprecedented monster wave.

*No matter how favorable the battlefield is, letting our guard down is out of the question.*

After silently reminding himself of that, Inoue addressed the twenty intelligence operatives.

“Listen up. From this point on, we’ll infiltrate in pairs. Use hand signals to communicate, and fire the signal flare you’re carrying if there’s an emergency. You’ve all memorized your destinations and routes without missing anything, right?”

“Yes.”

“Good, then… we’ll meet back here in three hours. Dismissed.”

At Inoue’s words announcing the start of the operation, the intelligence operatives nodded and scattered in every direction. Watching them disappear silently and swiftly, his partner Sam jerked his chin toward the path ahead.

“Should we get moving too, ninja?”

“Yeah. You carefree Yankee bastard.”

“Don’t be like that. Your skills are the best. In three hours, you’ll be back after finding out even the color of the Arch Lich’s underwear.”

“…I really hope that’s true.”

With a quiet sigh, Inoue stepped forward. The pale fog covering all of Suining City clung damply to his entire body.

* * *

The advance of the five fronts, which had seemed as though it would never stop, finally came to a halt.

Two hundred kilometers from Suining City, where the Arch Lich was located, a welcome face came to visit us while we were resting and reorganizing.

“Hey, Korean friends. How have you been?”

I sensed a considerable wave of qi nearby, and sure enough, it was him. I bumped fists with Magic Johnson and answered.

“Pretty well.”

“Jin. My lovable Miracle Boy. I missed you.”

“Sorry, but could you leave out the ‘lovable’ part?”

“Then I’ll call you Crazy Boy. You did pull off something crazy, after all.”

Magic Johnson grinned as he added,

“It was also an incredibly heroic act. The same goes for Choi here.”

Team Leader Choi, who was carefully polishing Hero’s Soul, lowered his head slightly.

“It’s good to see you again, Mr. Johnson.”

“Choi, don’t be like that. You’re making things stiff.”

“……!”

“……!”

“Of course, I mean the atmosphere.”

Magic Johnson threw back his head and laughed.

At this point, it was obvious that he enjoyed watching our reactions. He was surprisingly playful for a man of his size.

Well, by now, we knew that everything was a joke whenever we met Magic Johnson.

Even Team Leader Choi, who always did Kegel exercises whenever he met him, gave a quiet laugh before asking,

“But what brings you here?”

“An emergency summons from headquarters. It’s an important matter.”

I frowned and muttered,

“This feels like déjà vu. Haven’t we seen this setup before?”

“Don’t worry, Jin. Nothing like last time will happen.”

By “nothing like last time,” he meant a situation where our main camp got completely wrecked while the S-rank Hunters were away.

Well, the distance between the fronts had narrowed now. Even if everyone gathered together, we were practically close enough to touch noses if we fell over, so it should be fine.

*They aren’t handling this over communications because it must be that important.*

As the Allied Forces continued winning and the monsters retreated, the Arch Lich’s territory had shrunk all the way back to Suining City. At our current location, both communications and magic worked smoothly.

“Do you know what we’re gathering for?”

“No. But I can guarantee that it won’t be a pleasant matter. I’ll stake my life on it.”

“……”

Please. Don’t stake your life on something like that. Give us a little more hope.

But Magic Johnson, as confident as ever, held out his hands toward Team Leader Choi and me.

“Anyway, everyone’s already there. You two are the last guests.”

“Then please lead the way, Mr. Johnson.”

Team Leader Choi took his hand without hesitation. Having already experienced Magic Johnson’s teleportation once, I nervously grabbed his fingers.

“Please drive safely—Gyaaaaaaaah!”

Whoosh!

Along with the sensation of my entire body being crushed like a soda can, I was flung into a new space.

“Gyaaaaaaa…”

“……”

“……”

Damn it. Of all places, it had to be here.

A dozen pairs of eyes stared at me in silence. Under the dumbfounded gazes of the S-rank Hunters and senior Chinese generals, I stopped screaming and quietly took a seat in an empty chair.

“Are we not starting the meeting?”

After a moment at a loss for words, Defense Minister Wei Fenghu finally spoke.

“…Then let us begin the meeting.”

The meeting that followed focused on a single subject: the information delivered by the sole survivor of the intelligence team.

“Daniel Inoue, who was in charge of the intelligence team, escaped from Suining City after eight hours—far beyond the scheduled operation time—and reported discovering a monster army numbering around thirty thousand.”

Thirty thousand…

It was an enormous force, but still within the range we had expected.

The Arch Lich’s monster army had suffered its first defeat a week ago and had been retreating helplessly ever since. In the process, it had been forced to endure tremendous losses.

“Judging by the minister’s expression, that isn’t all, is it?”

Few people here could speak to Minister Wei that casually. Lee Jungryong was one of them, and regardless of his personal feelings toward me, he had more than earned that right.

“Mr. Lee is correct. The estimate based only on what he personally witnessed is thirty thousand. The actual number…”

“Could be twice that, perhaps even more.”

“That is correct.”

“…Hmm.”

Low groans rose from several places around the room. We had expected the enemy to be holding back strength for the final battle, but not that much.

Wei Fenghu continued in a solemn voice.

“But most of the monsters are likely to be mid- or low-level. That is the one small consolation.”

“That applies to us too, Wei Fenghu.”

At the remark from Faye Chen, who had been silently sipping from a liquor glass, Prince Felix nodded.

“That is true. More troops than expected have joined our side, but it would be premature to assume victory.”

“Damn it. Those monsters never end, no matter how many we kill.”

I couldn’t help snorting at Wu Heixing’s grumbling.

“Why are you laughing?”

“Because it’s funny, you idiot.”

“What?”

“Anyone listening to you would think you’d been fighting incredibly hard. You’re the asshole who tried to take a detour during the monster army’s attack a week ago because you were afraid going there early might be dangerous.”

“……!”

His expression was a sight to behold.

He must have thought no one knew, but Wu Heixing’s disgrace had already spread across every front.

“I know you’ve had a rough time too, but don’t whine in front of me or everyone else. It’s starting to piss me off just looking at you.”

“Iik…!”[^1]

“What are you, self-employed? Why do you keep going *iik*?”

[^1]: *Iik* is an angry Korean grunt that sounds identical to the Korean word for “profit.”

Wu Heixing’s face turned bright red. His body twitched as though he might charge at me at any moment, but that was as far as he could go.

The bitter memory of defeat lasted a long time.

Even a hothouse flower that had spent its entire life being treated like royalty would wither in a cold wind.

Of course, there were flowers of an entirely different sort.

Like Team Leader Choi, sitting beside me.

“That’s enough, both of you.”

At Team Leader Choi’s calm intervention, Wu Heixing glared at him.

“Are you ordering me around?”

“If that’s how you took it, that’s unfortunate, Wu Heixing.”

“You…”

Wu Heixing shot to his feet at Team Leader Choi’s complete lack of reaction to his intimidation.

No, he tried to stand.

“Sit.”

“……!”

My aura shot out like an awl, and his body locked in place.

The other S-rank Hunters looked at me with startled eyes as well.

I glanced at Lee Jungryong’s deeply sunken gaze before continuing.

“Just so there’s no misunderstanding, yes, that was an order.”

“You, you…!”

“Sit. I’m not saying it again.”

Whoosh!

A wave of aura surged toward him, and Wu Heixing’s lower lip trembled.

Maybe he really was a genius, even by Murim standards.

No, he was. Becoming an S-rank Hunter in his thirties would have been impossible without that level of talent.

*But he was only half the package.*

Awakening was an unearned windfall. Like someone who had won the lottery, he had been granted extraordinary abilities and mana the moment he turned twenty.

And then he was supposed to build up internal energy like a Murim practitioner and learn Supreme Peak martial arts?

*Well…*

If he learned martial arts, it would make up for his technical shortcomings. But there was no doubt he would drop out long before he reached that point.

Compared to his talent, his effort and will were Third Rate.

“Enough.”

Lee Jungryong’s gentle baritone broke the tension.

The old snake, still looking like a handsome middle-aged man despite being well past sixty, watched me with a smile.

“I thought only your skills had improved, but your killing intent has grown stronger too.”

I met his eyes with an impassive gaze and replied,

“Rolling around in all sorts of places tends to put an edge on you.”

“I heard the western front was particularly fierce.”

“That’s not wrong. Want to come see the western front?”

“I must politely decline. If it was fierce enough that only three people survived, I think I’ll pass.”

“……!”

“The older I get, the more cowardly I become. Ho ho.”

The blood in my entire body seemed to turn cold.

The horrifying battlefield from that day flashed before my eyes, and before I knew it, a faint smile had formed at the corner of my mouth.

“What are you trying to say?”

“Let’s think about something more productive than attacking our own allies. Planning for the final battle would be a good place to start. Jin Taekyung, what do you think?”

I quietly tapped the armrest of my chair.

My stomach twisted, but Lee Jungryong’s words had struck the heart of the matter.

He was right. The battle bearing down on us was practically at our doorstep. That was what we needed to deal with now.

And then one thought came to me.

“A suicide squad.”

“A suicide squad?”

Everyone’s eyes turned toward me. Some nodded as though they agreed, while others looked uneasy.

But both my reason and my instincts were telling me that this was the best way to minimize our losses and win the battle.

“We gather our very best and take out the head.”

Once the Arch Lich is destroyed, the undead army will collapse.
## Chapter artifact 408

# Chapter 408

“A suicide squad.”

The moment the words left Jin Taekyung’s mouth, Wu Heixing forgot his rising anger and nearly shouted.

*You crazy bangzi bastard!*

A suicide squad.

Wasn’t that exactly what it meant—to charge in prepared to die?

Even if they somehow broke through the monster army without knowing its exact numbers, the real monster called the Arch Lich was waiting behind it. The mere thought made the hair on Wu Heixing’s head stand on end.

*This… this is insane.*

It didn’t matter to Wu Heixing how many casualties there were.

China was a Great Nation with a population of over a billion, after all. Even if a hundred thousand or a million people disappeared, they would amount to no more than a handful.

In fact, if that damn bangzi became the vanguard of the suicide squad and died a glorious death, Wu Heixing would be more than happy to celebrate with both hands raised.

But…

“Let’s gather our very best and take out the head.”

That meant Wu Heixing himself would be included in the suicide squad. And he had no intention of taking even the slightest risk.

“Cut that ridiculous bullshit—”

Unable to hold back any longer, Wu Heixing shot to his feet and opened his mouth.

“Oh, that’s an excellent idea.”

“……!”

Wu Heixing stared wide-eyed, unable to continue.

He had never imagined that Lee Jungryong would support Jin Taekyung.

Not anyone else, but Lee Jungryong himself.

“W-What did you just say?”

“I said it was an excellent idea.”

Lee Jungryong continued with a gentle smile.

“We need to end this battle as quickly as possible. The Arch Lich is likely creating new undead even now. If the S-rank Hunters lead the advance and destroy it, the monster army—made up mostly of undead—will collapse, and our casualties will be reduced.”

“M-Mr. Lee.”

“You seem to think the same way I do. Just like everyone else here. Isn’t that right, Mr. Wu?”

“Everyone else? What are you talking about?”

Only then did Wu Heixing look around in confusion.

Not only Wei Fenghu and the other high-ranking Chinese generals, but also Faye Chen, Magic Johnson, and even Prince Felix were nodding slightly and exchanging opinions.

“Hmm. Certainly…”

“Even if we reinforce our forces, the Arch Lich will be doing the same. The longer we drag this out, the larger the battle will become.”

“What if we select A-rank Hunters and other veterans and deploy them at the front, then lead the breakthrough with the S-rank Hunters?”

“It’s certainly dangerous, but it’s an operation with a real chance of success.”

“No matter how powerful a Named Monster the Arch Lich is, we have a good chance if the S-rank Hunters launch a concentrated assault.”

Wu Heixing’s face went white as the conversation reached his ears.

*Have these people lost their minds?*

They were looking favorably upon this insane operation. They must have all gone crazy.

Even Lee Jungryong, whom Wu Heixing had trusted, was supporting Jin Taekyung for some reason.

Wu Heixing, who absolutely did not want to be included in the suicide squad, hurriedly turned toward Jin Taekyung.

“W-Wait! If all the S-rank Hunters leave, wouldn’t that create a massive hole in our forces?”

“Huh.”

Jin Taekyung sucked in a startled breath and looked at Wu Heixing in surprise.

“Wow. You do use your brain once in a while.”

“……”

“You’re right. We should probably leave a few people behind.”

*That damn bangzi.*

But this was no time to be angry. Suppressing his surge of fury, Wu Heixing continued.

“R-Right. So, to prepare for any unforeseen circumstances, I—”

Jin Taekyung abruptly cut him off and turned toward Magic Johnson.

“It seems like you should stay behind. What do you think, Johnson?”

“Me?”

What kind of situation was this? Wu Heixing desperately tried to intervene.

“Magic Johnson? Wouldn’t it be better to have at least one mage come with us?”

“Of course that would be good. It would—but…”

Jin Taekyung smiled pleasantly at Wu Heixing.

“What about the rear?”

“Huh?”

“I’m asking what you’ll do if the Arch Lich teleports behind our lines and attacks us from the rear. Will you stop it?”

“……”

“No matter how powerful the Arch Lich is, it won’t be able to pull something like that if a great mage remains behind to interfere with its magic. And Magic Johnson’s wide-area magic could become the move that turns the tide of battle.”

Every word was perfectly reasonable. Wu Heixing’s mouth snapped shut, and Jin Taekyung clicked his tongue.

“Think before you run your mouth. Stop looking at those ‘watch your rear’ GIFs on the internet and think about the rear in an actual war.”

“……!”

Ignoring Wu Heixing, who had frozen like a statue, Jin Taekyung asked Magic Johnson,

“What do you think?”

“You’re right, Jin. So I’m the only one staying behind?”

Defense Minister Wei Fenghu, who had been silently observing the situation, suddenly spoke.

“The Arch Lich must have left a large number of high-level monsters behind for the final battle. There are far more of them than the number of A-rank Hunters on our side. To maintain an evenly matched battlefield, we need at least two more S-rank Hunters.”

It wasn’t over yet. There were still two positions open.

Wu Heixing, who had found a glimmer of hope, cleared his throat.

“Then, as a last resort, I’ll have to stay—”

“If the others have no objections, I would like to leave Prince Felix out first.”

“What?”

“I’m sorry, but I cannot explain the details. There is a complicated issue involved.”

Felix was not merely an S-rank Hunter. He was practically a symbol of the United Kingdom—a member of the royal family. And not some insignificant branch of it, either. He was third in line to the throne.

Everyone present understood that the “complicated issue” Wei Fenghu could not explain was a diplomatic problem with the United Kingdom.

“Well, his father is the King of the United Kingdom, so I suppose that’s possible. Then the prince is out.”

At Jin Taekyung’s words, Prince Felix spoke with an uncomfortable expression.

“I hope you understand that this is not my own choice. However, since I have been bound to the royal family since birth, I cannot disobey my royal father’s command—”

“It’s fine. I don’t care. I’d actually prefer it this way, since it would leave a bad taste in my mouth if the United Kingdom’s fourth in line to the throne got hurt during the operation I proposed.”

“Third! And show proper respect when speaking to me.”

“Oh, right. Congratulations on the bronze medal. Then, does anyone object to His Highness Prince Felix, a living hotbed of entrenched privilege, sitting this one out on the strength of his connections?”

Wu Heixing unconsciously started to raise his hand, but stopped at the answers that came from Faye Chen and Lee Jungryong.

“I don’t mind.”

“I agree.”

Jin Taekyung nodded and looked pointedly at Wu Heixing.

“What about you?”

“Me?”

“When the one remaining guy asks that, what am I supposed to say? Tinky Winky, Dipsy, or Po. Pick one.”

There was no way out.

Magic Johnson and Prince Felix were foreigners, and they had legitimate reasons. Faye Chen and Lee Jungryong had even agreed.

Wu Heixing squeezed his eyes shut, then opened them and muttered,

“…I agree.”

“Answer properly. If you answer like that, how the hell am I supposed to know whether you mean agreement or Donguibogam[^1]? Are you Heo Jun?”

“…….”

“I… agree.”

“Okay.”

It happened at Quick Attack speed.

One position still remained, but Wu Heixing felt a sense of foreboding.

And it didn’t take long for that foreboding to become certainty.

“I would like Faye Chen to fill the final position.”

But what had thrown Wu Heixing into confusion was that it wasn’t Jin Taekyung who had blocked his last escape route.

It was Lee Jungryong.

*What in the world is that old man thinking?*

Wu Heixing vividly remembered the conversation he had shared with Lee Jungryong on the day Jin Taekyung had trampled him so thoroughly that he still felt humiliated.

*He clearly suggested that we join forces. And now he’s stabbing me in the back like this?*

Faye Chen glanced at Wu Heixing, who was grinding his teeth, and tipped back his liquor glass.

“Well, Mr. Lee, I’m not the sort of person who enjoys danger. But wouldn’t our odds of success be higher if we left that brat behind instead of me?”

“No, Faye Chen. To reduce casualties, it will help us more if you stay.”

“You don’t know that kid. Just looking at him makes even someone who never had any patriotism develop some.”

“Don’t worry. I’ll be here.”

His tone was calm, but filled with certainty.

It was something Lee Jungryong could say because he was Lee Jungryong.

The gaze of the old hero, radiating confidence that no one present could deny, settled on one person.

“And Jin Taekyung. You’re here too, aren’t you?”

His eyes were deeply sunken, impossible to read.

Jin Taekyung silently met Lee Jungryong’s gaze before parting his lips.

“Our dear Vice Guild Master. You certainly have a talent for making obvious things sound complicated.”

“May I take that to mean you will also be joining the suicide squad?”

“Of course.”

“Brave. Heroic, even. In that case, I’ll yield the vanguard to you.”

“Great. Does that mean I get to leave behind a famous quote like Louis Armstrong? Something like, ‘This is one small step for one human being, but the Heavenly Demon’s Reign for monsters.’”

“That’s a bit rough for a quote destined for the history books. And you got the name wrong. It wasn’t Louis Armstrong. It was Neil Armstrong.”

“That’s an impressive amount of schooling. Still, it’s nothing compared to the length of my tissue roll.”

The people around them developed pounding headaches trying to follow Jin Taekyung’s answers, while Wu Heixing fell into despair.

Until barely a month ago, he had been enjoying a lavish yacht party surrounded by dozens of beautiful women.

Now he had been assigned to a suicide squad prepared to die.

And then, in the very next moment—

—Did you think I betrayed you?

“……!”

—Accept it. I promise there won’t be any danger.

As the Sound Transmission pierced his ears, Wu Heixing slowly raised his head.

Lee Jungryong was looking at him with a gentle smile as he continued speaking.

“He’ll carry out his assigned duty well. I guarantee it.”

Jin Taekyung slowly tapped the armrest of his chair as he replied,

“I’m really looking forward to seeing just how brilliantly he performs his duty.”

* * *

The somewhat lengthy meeting came to an end.

The suicide squad would be led by S-rank Hunters, with high-level A-rank Hunters and B-rank veterans making up the rest. The command staff would be working around the clock to select the members.

The Skeleton Warlord had remained silent throughout the meeting. But the moment we returned to the tent assigned to me on the western front, it solemnly declared,

“This commander will sit out this battle.”

“Yeah, fuck off.”

“At least ask why, you treacherous human.”

“Fine. Why?”

“As the commander of the undead army, I find it distasteful to fight my own kind.”

I answered with a dumbfounded expression.

“What the fuck are you talking about? Who’s been sucking the energy out of his own kind to replenish himself until now?”

“…Oh.”

“Let’s be honest. If you said you just didn’t want to go because you were scared of the Arch Lich, would I curse at you?”

“You would.”

“You son of a—… Oh.”

The Skeleton Warlord’s distrust of me deepened even further as it spoke.

“In any case, this commander no longer wishes to participate in this war. Honor the promise you made that day.”

“The promise I made that day?”

“Have you ever seen such a treacherous human? Didn’t you promise that, in exchange for protecting two humans, you would grant any request I made?”

“Oh.”

It had been a while since I’d been rendered speechless.

I had definitely made that promise. Normally, I would have brushed it off like someone pretending to have amnesia, but this time, I couldn’t ignore it in good conscience.

“Fine. What is your wish?”

The Skeleton Warlord shouted as though it had been waiting for the question.

“Give me freedom!”

“Freedom?”

“That is correct. You, treacherous human, have insulted and abused this commander all this time! The total is no less than 408 times!”

“…Are you from an animal rights group?”

“Honor your promise! This commander shall finally find freedom!”

Freedom.

My mind was already complicated enough with thoughts of Lee Jungryong, so I hadn’t expected a wish like this.

After thinking for a moment, I answered,

“Fine. I’ll give you freedom.”

“Ooh! Ooooooh!”

“Then goodbye.”

“Huh?”

Without hesitation, I pulled the Skeleton Warlord’s skull from my Inventory and threw it outside the tent.

Into the middle of the thousands of Hunters swarming around outside.

Clack!

The sound of it hitting something rang out, and the area around the tent erupted into chaos. Shouts rang out from every direction, followed by the booming detonation of magic.

“Monster! Monster attack!”

“Kill it!”

Boom! Kaboom!

How much time passed?

Five minutes? Ten?

Rustle, rustle.

The bottom edge of the tent suddenly began to shift. Then a black, glossy skull rolled in and stopped at my feet.

“Oh, look who it is.”

“……”

“What brings the Skeleton Warlord, proud owner of a free spirit, here?”

“You… human…”

A red glow flickered pitifully in the skull’s empty eye sockets.

Was I imagining it, or was an undead actually whimpering?

The Skeleton Warlord continued in a tearful voice.

“Can I… take back my wish?”

“Oh, of course.”

I continued in a bright customer-service voice.

“But you know wish coupons can’t be exchanged or refunded, right?”

“……”

“Come here, Bones.”

Hop.

The Skeleton Warlord feebly jumped into my arms.

[^1]: *Donguibogam* is a landmark medical encyclopedia compiled by Heo Jun. The joke plays on the similarity between *dongui* (“agreement”) and the title *Donguibogam*.
## Chapter artifact 409

# Chapter 409

The visitor who had not made an appointment arrived before dawn had fully broken.

He carefully entered the tent and met my eyes as I sat cross-legged.

“You were already awake.”

“As you can see.”

I shrugged at Team Leader Choi.

“I haven’t been able to sleep much lately.”

To be precise, I should say I needed less sleep.

With stamina that had surpassed human limits and formidable internal energy amounting to three jiazi,[^1] I could blow away most fatigue by circulating my qi.

“Were you cultivating the Mana Cultivation Method—or rather, the Jin Family’s Cultivation Technique?”

“Yeah, something like that.”

To be exact, it was the Fire Gate Divine Technique, the secret cultivation technique of the Fire Gate Clan. But I couldn’t exactly tell him every last detail.

“I should have come later.”

“No, it’s fine.”

“Didn’t you say that any interruption during cultivation was forbidden? That stopping halfway through could cause qi deviation…”

“Oh, that’s true for you, Team Leader Choi. I’m fine. We’re on different levels.”

“…”

*Warning: your fact attack may hurt someone.*

For a moment, I thought I saw a public-service announcement like that flash across Team Leader Choi’s face.

He looked at me with an uncomfortable expression, then slowly shook his head.

“It is a fact, so I have nothing to say.”

“Even so, your rate of learning is incredible by any standard. I mean that sincerely, so have a little more confidence.”

I meant it. True to his bloodline as the descendant of Cheon Taemin, the hero who had accomplished an indomitable feat in human history, Team Leader Choi possessed extraordinary natural martial talent.

And for some reason, he also had a considerable amount of energy accumulated inside his body, so his progress in martial arts was astonishingly fast.

In short, he was a talent with all the groundwork already laid.

*If he’d learned martial arts from a young age like Wu Heixing… he’d probably hold an S-rank Hunter position by now.*

Team Leader Choi’s expression softened slightly, and he nodded.

“How do I compare to Jin Taekyung?”

“Are you joking? Of course I learned faster.”

“…”

*As if you could compare yourself to me.*

No matter how Team Leader Choi had grown up under Lee Jungryong’s supervision and restraint, the very texture of the lives we had lived was different.

Even after obtaining the System, I’d nearly died several times. Damn it, I’d been through hell.

“Anyway, why did you come? Especially this early.”

“I had something troubling me, so I came despite the imposition.”

“Something troubling you?”

“Yes.”

“Why? Did Johnson confess his love to you?”

“I’m not concerned about that. I know that’s simply Mr. Johnson’s way of showing affection. More importantly, this concerns Guild business.”

“Guild business… Did some bad news come from Korea?”

At my worried question, Team Leader Choi shook his head.

“No. I’m worried because it looks like one of our Guild members is heading into danger.”

“Oh.”

So that was what he meant. Once I understood, I snorted quietly.

“I know who you mean. Tall and handsome, right? With an absolutely wonderful personality.”

“I don’t know about the other qualities, but his personality certainly seems to be something else. In several ways.”

“Hmm. Then I don’t think we’re talking about the same person.”

“Mr. Jin Taekyung.”

Team Leader Choi, who had been trading jokes with me until then, spoke in a lowered voice.

“You know what I mean.”

“Do I?”

“This operation is dangerous.”

“Team Leader Choi. Don’t you trust me?”

“How could I not? You are one of the people in the world I trust more than anyone.”

Team Leader Choi stared at me with deeply serious eyes.

“And you are about to carry out a dangerous operation with people I trust less than anyone in the world.”

Two names came to mind without hesitation.

Lee Jungryong and Wu Heixing. People connected to me by bitter relationships—and comrades who would soon have to entrust their backs to one another.

I scratched my chin and answered.

“‘People I can’t trust.’ I can’t think of a more fitting description.”

“Mr. Jin Taekyung…”

“Team Leader Choi?”

Team Leader Choi closed his mouth as he prepared to say something. I quietly raised a hand and pointed toward the tent flap.

“As you know, I haven’t finished cultivating yet.”

“……!”

“The battle will begin before the day is over. Clear your mind and prepare for the fight ahead.”

Team Leader Choi could not continue. He looked at me with complicated emotions, then let out a deep sigh and rose from his seat.

“I’ll see you shortly.”

“All right. I won’t see you out.”

I felt Team Leader Choi’s presence gradually fade as he left the tent.

Then the Skeleton Warlord, which had been depressed ever since its wish coupon was refunded, spoke in a hopeful tone.

—A very intelligent human. It is not too late. Why not heed that human’s advice?

“You’re really trying.”

—No, if you are going to go, go alone. Why are you taking this commander with you?

“Dying alone would be lonely.”

—Whaaaaaat?!

“I’m joking. It’s just that this is the best option.”

—You call fighting through a gigantic monster army to face the Arch Lich the best option? Are you an evil human—or a lunatic?

Listen to the way this undead bastard talks.

I considered punishing it, then unfolded my legs and reclined diagonally across the bed.

“It is a dangerous operation, but we have a good chance too, so don’t be like that.”

—What if we get there and it doesn’t work?

“Then we fight with everything we’ve got. That’s how we create a chance.”

The Skeleton Warlord muttered in a voice filled with resignation.

—What miraculous logic. This commander is stuck with a madman like you.

“And yet you’re not leaving.”

—Not leaving? You mean I can’t leave!

“What a funny guy. When was it that you came back of your own accord? Ah, never mind. Not feet—your skull.”

—There are vicious humans everywhere around me, all trying to get this commander. What exactly do you expect me to do?

At the Skeleton Warlord’s aggrieved protest, I let out a small laugh.

*Don’t be such a coward.*

I had plenty to say, but decided to save it for later. That was something it needed to realize on its own.

—You laughed. You just laughed!

“When did I?”

I shamelessly pretended nothing had happened and changed the subject.

“Anyway, the key is taking out the Arch Lich. Once it loses its head, its body won’t be able to move.”

—Dullahans can still move without their heads.

“…”

That was true.

I was momentarily convinced, then immediately became dumbfounded. I pulled the Skeleton Warlord out of my Inventory.

“No, but seriously, this bastard has been asking for it.”

—H-Hold on, human. I did not say anything incorrect.

“Right. Dullahans can move without their heads. Let’s see what happens to the Skeleton Warlord.”

*Bash!*

The Skeleton Warlord shrieked when I flicked its skull with lightning speed.

—Agh! A crack! There’s a crack between my brows! I’m telling you, there’s really a crack!

“I hit you while controlling my strength, so what the hell are you talking about… Oh, there really is one.”

Maybe I should have hit it more gently. A tiny crack had appeared in the glossy black skull, its surface gleaming smoothly.

When I lightly touched the bone fragment raised by the impact, the Skeleton Warlord screamed.

—My bone! My bone!

“Fine, I get it, so stop screaming.”

—My bones have been getting increasingly itchy and sensitive lately, and I was already worried, but this madman went and… Sob.

“…”

*Is it suffering from dry skin or something?*

At this rate, it would soon start a channel on iTube and gather a million subscribers as an undead beauty streamer.

*This bastard might not even be a monster…*

The more I saw of it, the more unusual it seemed.

I stared at the Skeleton Warlord in disbelief, then suddenly threw open one side of the tent. The sun was slowly lifting its head in the east.

It was a signal announcing the day ahead—and the battle that would soon begin.

* * *

Suining City lies in the center of the Sichuan Basin and boasts two urban districts, three counties, and a vast area of more than 5,000 square kilometers.

Since ancient times, it had been called the center of central Sichuan Province because of its lofty culture, graceful scenery, and flourishing agriculture, industry, and commerce. But that, too, had now become a thing of the past.

Caw, cawww!

Countless crows flying in flocks across the cloudy sky descended upon corpses sprawled across the ground. No squabbles broke out between the flocks over their prey.

Hundreds of corpses lay scattered everywhere, at the very least, and the crows filled their bellies by pecking at the rotting flesh that had once belonged to humans.

What was the greatest calamity imaginable to humans was an age of plenty for them.

But the crows’ peaceful feast did not last long.

Grk. Grrrk.

At the deep rumble and vibrations rising from the ground, the crows let out nervous cries and took flight all at once.

A few black feathers flung into the air rode the wind across the vast basin.

Countless marching feet and the metal wheels of tanks crushed the feathers as they fluttered down.

Boom. Boom. Boom.

A human army filled the horizon.

The tower shields held by the tanks at the very front scraped against the ground, while thousands of Hunters behind them marched in orderly ranks.

Someone’s tightly pressed lips showed beneath a helmet pulled low.

Thousands of humans swept up in the invisible tide of war simply continued forward in silence.

Toward the city wrapped in pale fog in the distance. Toward the battle that would soon follow—and a glorious victory.

And then, from the center of them all, someone suddenly spoke.

“Fuck, look at that fog. Doesn’t it look like something from one of those disaster movies where monsters come out? Anyone seen that movie?”

Jin Taekyung’s vivid profanity came out of nowhere in the serious atmosphere, and quiet snorts of laughter erupted from various places.

“Heh.”

“Kh.”

“What? I’m the only one who saw it? That masterpiece?”

Just as Jin Taekyung shrugged, an answer came from his right.

“I saw it too.”

“Really? That’s unexpected, Team Leader Choi.”

“What is?”

“You look like the kind of person who’d only watch musicals or orchestral performances, not movies.”

The Hunters who glanced at Choi Minwoo bit their lips to keep from laughing.

Before they knew it, their stiff bodies had relaxed and their breathing had steadied. They felt the tension ease considerably.

Meanwhile, the conversation between the two continued.

“I watch movies occasionally to unwind. I enjoyed the one you mentioned, Mr. Jin.”

“Oh, then you know the final twist too.”

“Of course. Personally, I found it quite unfortunate.”

“Exactly. That’s what I thought while watching it.”

Jin Taekyung continued slowly.

“They could have lived if they hadn’t given up until the very end. They should have fought with everything they had, no matter what. That sort of thing.”

His voice was quiet, but it carried strength.

The voice infused with tremendous internal energy reverberated through the air and spread outward, soon reaching everyone’s ears.

And the thousands of Hunters and soldiers belonging to the Western Front realized something.

That Jin Taekyung’s words might be advice directed straight at them.

“By now, the other fronts are probably surrounding Suining City just like we are, right?”

“They should have it completely surrounded.”

“And the battle will begin soon.”

“We will win.”

At Shao Shen’s firm answer, Jin Taekyung laughed aloud.

“Yeah. We have to. But…”

Jin Taekyung’s laughter abruptly stopped. The next moment, the playful light in his eyes vanished, replaced by a deeply sunken gaze.

The vast basin was reflected in his cold pupils.

“It looks like those guys have a different opinion.”

Tap. Tap-tap-tap.

Grrrk…

Bodies slowly rose to their feet. Skeletons. And fog that slid over the basin, along with the cries of monsters lurking within it.

“From now on…”

Jin Taekyung took a deep breath.

“It begins.”

[^1]: A *jiazi* is a traditional sixty-year cycle.
